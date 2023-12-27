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
    try:
        print("Welcome to the Vocab Venture Game!")
        print("Can you guess the words and complete all levels? "
              "Let's find out!")

        # Instructions for playing the game
        print("\nInstructions:")
        print("1. You will start at Level 1, and "
              "your goal is to reach Level 5.")
        print("2. In each level, you will be given a word and three hints.")
        print("3. You have 3 attempts to guess the correct "
              "word for each level.")
        print("4. Enter your guess when prompted. "
              "Type 'quit' to end the game.")
        print("5. If you guess the word correctly, "
              "you move to the next level.")
        print("6. Complete all levels to win the game!")
        print("\nLet's get started!")

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

            # Remove the chosen word from the word_list
            word_list.remove(chosen_word_info)

            # Choose the hints for the chosen word
            chosen_hints = chosen_word_info['hints']

            print(f"\nLet's start Level {current_level}!")
            print("Hint 1:", chosen_hints['Hint 1'])

            attempts = 3
            correct_guess = False

            while attempts > 0:
                guess = input(
                    "Enter your guess (or type 'quit' to end the game): "
                ).lower()

                if guess == 'quit':
                    print("You've chosen to quit the game. Goodbye!")
                    return None, None

                if guess == chosen_word_info['word'].lower():
                    if current_level < 5:
                        print("Congratulations!\n"
                              "You guessed the word correctly and moved to "
                              f"Level {current_level + 1}.")
                    else:
                        print("Congratulations! You've completed all levels. "
                              "You win the game!")
                    correct_guess = True
                    break
                else:
                    attempts -= 1
                    print(f"Incorrect. You have {attempts} attempts left"
                          f"for Level {current_level}.")

                    if attempts > 0:
                        # Display the next hint
                        hint_number = 4 - attempts
                        hint_label = f"Hint {hint_number}:"
                        next_hint = (
                            f"{hint_label} "
                            f"{chosen_hints[f'Hint {hint_number}']}")

            if not correct_guess:
                print(f"You've run out of attempts for Level {current_level}. "
                      f"The correct word was '{chosen_word_info['word']}'.")
                print("Resetting to Level 1.")
                current_level = 1
            else:
                current_level += 1

        print("You've reached Level 5! You win the game.")

    except KeyboardInterrupt:
        print("\nGame interrupted by the user.")
        return None, None
    except Exception as e:
        print(f"An error occurred during game initialization: {e}")
        return None, None


initialize_game()
