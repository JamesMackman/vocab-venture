import gspread
from google.oauth2.service_account import Credentials
import random

def load_words(file_path='creds.json', sheet_name='vocab_venture'):
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
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

        # Open the spreadsheet
        sheet = GSPREAD_CLIENT.open('vocab_venture')

        # Choose the appropriate worksheet
        words_worksheet = sheet.worksheet('words')

        # Fetch all values from the worksheet
        data = words_worksheet.get_all_values()

        # Extract words, hints, and difficulty levels
        words = [row[0] for row in data[1:]]  # Column A, skip header row
        hints = [row[1] for row in data[1:]]  # Column B
        difficulty_levels = [row[2] for row in data[1:]]  # Column C

        # Combine words, hints, and difficulty levels into a list of dictionaries
        word_info_list = [
            {'word' : word, 'hint': hint, 'difficulty': difficulty}
            for word, hint, difficulty in zip(words, hints, difficulty_levels)
        ]

        return word_info_list

    except Exception as e:
        print(f"An error occurred while loading words: {e}")
        return []

def initialize_game():
    """
    Initialize a word guessing game by prompting the user to choose a difficulty level.
    """
    try:
        # Load words from the spreadsheet
        word_list = load_words()

        if not word_list:
            print("Error: No words loaded. Exiting game.")
            return None, None, None

        # Prompt user to choose a difficulty level
        difficulty_levels = set(word_info['difficulty'] for word_info in word_list)
        print("Available difficulty levels:", difficulty_levels)
        chosen_difficulty = input("Choose a difficulty level: ").lower()

        # Convert difficulty levels to lowercase for consistent comparison
        filtered_words = [word_info for word_info in word_list if word_info['difficulty'].lower() == chosen_difficulty]

        if not filtered_words:
            print(f"No words available for difficulty level: {chosen_difficulty}. Exiting game.")
            return None, None, None

        # Choose a random word from the filtered list
        chosen_word_info = random.choice(filtered_words)
        return chosen_word_info['word'], chosen_word_info['hint'], chosen_difficulty

    except Exception as e:
        print(f"An error occurred during game initialization: {e}")
        return None, None, None

def play_game(chosen_word, hint, difficulty):
    """
    Play the word guessing game, allowing the user 3 attempts to guess the word.
    """
    attempts = 3

    print("\nLet's start the game!")
    print(f"Hint: {hint}")

    while attempts > 0:
        guess = input("Enter your guess: ").lower()

        if guess == chosen_word.lower():
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts remaining. Try again.")
            else:
                print(f"Sorry, you've run out of attempts. The correct word was '{chosen_word}'.")
                break

# Example usage
chosen_word, hint, difficulty = initialize_game()

if chosen_word is not None:
    print(f"Chosen word: {chosen_word}")
    print(f"Hint: {hint}")
    print(f"Difficulty: {difficulty}")

    # Play the game
    play_game(chosen_word, hint, difficulty)
else:
    print("Game initialization failed.")