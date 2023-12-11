import gspread
from google.oauth2.service_account import Credentials
import random

# Constants
WORKSHEET_NAME = 'words'
SPREADSHEET_NAME = 'vocab_venture'

def load_words(file_path='creds.json'):
    """
    Load words, hints, and difficulty levels from a Google Spreadsheet
    """
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    try:
        # Load credentials
        CREDS = Credentials.from_service_account_file(file_path)
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

        # Open the spreadsheet
        spreadsheet = GSPREAD_CLIENT.open(SPREADSHEET_NAME)

        # Open the worksheet
        words_worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

        # Fetch all values from the worksheet
        data = words_worksheet.get_all_values()

        # Check if the worksheet is empty
        if not data:
            print("Error: Worksheet is empty. Exiting game.")
            return []

        # Extract words, hints, and difficulty levels
        words, hint_1, hint_2, hint_3, difficulty_levels = zip(*data[1:])

        # Combine words, hints, and difficulty levels into a list of dictionaries
        word_info_list = [
            {
                'word': word,
                'hints': {'hint_1': hint_1[i], 'hint_2': hint_2[i], 'hint_3': hint_3[i]},
                'difficulty': difficulty
            }
            for i, (word, difficulty) in enumerate(zip(words, difficulty_levels))
        ]

        return word_info_list

    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Error: Spreadsheet not found - {e}")
        return []
    except Exception as e:
        print(f"An error occurred while loading words: {e}")
        return []

def choose_random_hint(hints, attempt_number):
    """
    Choose a random hint from the list of hints based on the attempt number
    """
    return hints[f'hint_{attempt_number}']

def initialize_game():
    try:
        # Load words from the spreadsheet
        word_list = load_words()

        if not word_list:
            print("Error: No words loaded. Exiting game.")
            return None, None, None

        # Extract difficulty levels and print them in the desired order
        difficulty_levels = ['Easy', 'Medium', 'Hard']
        print("Available difficulty levels:", difficulty_levels)
        
        chosen_difficulty = input("Choose a difficulty level: ").capitalize().strip()

        # Convert difficulty levels to lowercase for consistent comparison
        filtered_words = [word_info for word_info in word_list if word_info['difficulty'].lower() == chosen_difficulty.lower()]

        if not filtered_words:
            print(f"No words available for difficulty level: {chosen_difficulty}. Exiting game.")
            return None, None, None

        # Choose a random word from the filtered list
        chosen_word_info = random.choice(filtered_words)

        # Choose the initial hint from 'Hint 1'
        chosen_hint = chosen_word_info['hints']

        return chosen_word_info['word'], chosen_hint, difficulty_levels

    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred during game initialization: {e}")
        return None, None, None

def play_game(chosen_word, hints, difficulty):
    attempts = 3
    current_hint_index = 1  # Start with the first hint

    print("\nLet's start the game!")

    while attempts > 0:
        # Print the current hint
        current_hint_key = f'hint_{current_hint_index}'
        print(f"Hint {current_hint_index}: {hints[current_hint_key]}")

        guess = input("Enter your guess: ").lower()

        if guess == chosen_word.lower():
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            current_hint_index += 1

            if current_hint_index <= 3:
                print(f"Incorrect! Here's your next hint.")
            else:
                print(f"Sorry, you've run out of attempts. The correct word was '{chosen_word}'.")
                break

# Example usage
chosen_word, hints, difficulty = initialize_game()

if chosen_word is not None:
    print(f"Difficulty: {difficulty}")

    # Play the game
    play_game(chosen_word, hints, difficulty)
else:
    print("Game initialization failed.")
