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

        # Choose a random word from the list
        chosen_word_info = random.choice(word_list)

        # Choose the initial hint from 'Hint 1'
        chosen_hint = chosen_word_info['hints']

        return chosen_word_info['word'], chosen_hint

    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        return None, None
    except Exception as e:
        print(f"An error occurred during game initialization: {e}")
        return None, None

def play_game(chosen_word, hints):
    current_level = 1
    attempts = 3

    print("\nLet's start the game!")

    while current_level <= 5:
        # Print the current hint
        current_hint_key = f'hint_{current_level}'
        print(f"Level {current_level} Hint: {hints[current_hint_key]}")

        guess = input("Enter your guess: ").lower()

        if guess == chosen_word.lower():
            print(f"Congratulations! You guessed the word correctly and completed Level {current_level}.")
            current_level += 1

            if current_level <= 5:
                # Move to the next level
                print(f"Proceeding to Level {current_level}.")
            else:
                print("You've reached Level 5! You win the game.")
                break
        else:
            attempts -= 1

            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left for this level.")
            else:
                print(f"Sorry, you've run out of attempts. The correct word was '{chosen_word}'.")
                print("Resetting to Level 1.")
                current_level = 1
                attempts = 3

# Example usage
chosen_word, hints = initialize_game()

if chosen_word is not None:
    print("Starting at Level 1")

    # Play the game
    play_game(chosen_word, hints)
else:
    print("Game initialization failed.")
