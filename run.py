import gspread
from google.oauth2.service_account import Credentials
import random


def load_words(file_path='creds.json', sheet_name='vocab_venture'):
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
            {'word': word, 'hint': hint, 'difficulty': difficulty}
            for word, hint, difficulty in zip(words, hints, difficulty_levels)
        ]

        return word_info_list

    except Exception as e:
        print(f"An error occurred while loading words: {e}")
        return []

word_list = load_words()
print(word_list)
