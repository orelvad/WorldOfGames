import os


def bad_return():
    BAD_RETURN_CODE = -1
    return BAD_RETURN_CODE


def get_score_file_name():
    SCORES_FILE_NAME="Scores.txt"
    return SCORES_FILE_NAME


def screen_cleaner():
    os.system('cls')

