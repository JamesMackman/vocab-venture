import gspread
from google.oauth2.service_account import Credentials
import random

# Constants
WORKSHEET_NAME = 'words'
SPREADSHEET_NAME = 'vocab_venture'


def load_words(file_path='creds.json'):
    try:
        # Load credentials
        credentials = Credentials.from_service_account_file(file_path)
        scoped_credentials = credentials.with_scopes([
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ])
        gspread_client = gspread.authorize(scoped_credentials)

        # Open the spreadsheet and worksheet
        spreadsheet = gspread_client.open(SPREADSHEET_NAME)
        words_worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

        # Fetch all values from the worksheet
        data = words_worksheet.get_all_values()

        # Check if the worksheet is empty
        if not data:
            print("Error: The worksheet is empty. Exiting game.")
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

    except FileNotFoundError as e:
        print(f"Error: Credentials file not found - {e}")
        return []
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Error: Spreadsheet not found - {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading words: {e}")
        return []


def display_instructions():
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


def get_user_guess():
    while True:
        user_input = input("Your guess (type 'quit' to end): ").lower()

        if user_input == 'quit':
            print("You've chosen to quit the game. Goodbye!")
            return user_input
        elif user_input.isalpha() and len(user_input) > 0:
            return user_input
        else:
            print("Invalid input. Please enter a valid guess or 'quit.'")


def play_game(word_list):
    try:
        print("Welcome to the Vocab Venture Game!")
        print("Can you guess the words and complete all levels? Let's find out!")

        # Instructions for playing the game
        display_instructions()

        # Set the initial level to 1
        current_level = 1

        while current_level <= 5:
            chosen_word_info = random.choice(word_list)
            word_list.remove(chosen_word_info)
            chosen_hints = chosen_word_info['hints']

            print(f"\nLet's start Level {current_level}!")
            print("Hint 1:", chosen_hints['Hint 1'])

            attempts = 3
            correct_guess = False

            while attempts > 0:
                guess = get_user_guess()

                if guess == 'quit':
                    return

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
                          f" for Level {current_level}.")

                    if attempts > 0:
                        hint_number = 4 - attempts
                        hint_label = f"Hint {hint_number}:"
                        next_hint = (
                            f"{hint_label} "
                            f"{chosen_hints[f'Hint {hint_number}']}")
                        print(next_hint)

            if not correct_guess:
                print(f"You've run out of attempts for Level {current_level}. "
                      f"The correct word was '{chosen_word_info['word']}'.")
                print("Resetting to Level 1.")
                current_level = 1
            else:
                current_level += 1

        print("You've reached Level 5! You win the game.")

        # Display reset message with newlines for better formatting
        print("\nGame completed!\n"
              "You can type 'reset' to play again or 'quit' to exit the game.")

        while True:
            user_input = input("Your choice: ").lower()

            if user_input == 'reset':
                print("Resetting the game to Level 1. Let's play again!\n")
                play_game(word_list)
                break
            elif user_input == 'quit':
                print("Exiting the game. Goodbye!\n")
                break
            else:
                print("Invalid input. Please enter 'reset' to play again or 'quit' to exit.\n")

    except KeyboardInterrupt:
        print("\nGame interrupted by the user.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during game play: {e}")
        return


word_list = load_words()
if word_list:
    play_game(word_list)
