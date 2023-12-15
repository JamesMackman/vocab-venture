import gspread
from google.oauth2.service_account import Credentials
import random

# Constants
WORKSHEET_NAME = 'words'
SPREADSHEET_NAME = 'vocab_venture'

def load_words(file_path='creds.json'):
    """
    Load words and hints from a Google Spreadsheet
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

        # Extract words and hints
        words, hint_1, hint_2, hint_3 = zip(*data[1:])

        # Combine words and hints into a list of dictionaries
        word_info_list = [
            {
                'word': word,
                'hints': {
                    'Hint 1': hint_1[i],
                    'Hint 2': hint_2[i],
                    'Hint 3': hint_3[i],
                },
            }
            for i, word in enumerate(words)
        ]

        return word_info_list

    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Error: Spreadsheet not found - {e}")
        return []
    except Exception as e:
        print(f"An error occurred while loading words: {e}")
        return []

def initialize_game():
    """
    Initializes and plays the Vocab Venture Game.
    """

    try:
        print("Welcome to the Vocab Venture Game!")
        print("Can you guess the words and complete all levels? Let's find out!")

        # Set the initial level to 1
        current_level = 1

        # Load words from the external spreadsheet
        word_list = load_words()

        if not word_list:
            print("Error: No words loaded. Exiting game.")
            return None, None

        while current_level <= 5:
            # Choose a random word for the current level
            chosen_word_info = random.choice(word_list)

            # Choose the hints for the chosen word
            chosen_hints = chosen_word_info['hints']

            print(f"\nLet's start Level {current_level}!")
            print("Hint 1:", chosen_hints['Hint 1'])

            attempts = 3
            correct_guess = False

            while attempts > 0:
                guess = input("Enter your guess: ").lower()

                if guess == chosen_word_info['word'].lower():
                    print(f"Congratulations! You guessed the word correctly and completed Level {current_level}.")
                    correct_guess = True
                    break
                else:
                    attempts -= 1
                    print(f"Sorry, incorrect. You have {attempts} attempts left for Level {current_level}.")

                    if attempts > 0:
                        # Display the next hint
                        next_hint = f"Hint {4 - attempts}: {chosen_hints[f'Hint {4 - attempts}']}"
                        print(next_hint)

            if not correct_guess:
                print(f"You've run out of attempts for Level {current_level}. The correct word was '{chosen_word_info['word']}'.")
                print("Resetting to Level 1.")
                current_level = 1

        print("You've reached Level 5! You win the game.")

    except KeyboardInterrupt:
        print("\nGame interrupted by the user.")
        return None, None
    except Exception as e:
        print(f"An error occurred during game initialization: {e}")
        return None, None

# Example usage
initialize_game()











