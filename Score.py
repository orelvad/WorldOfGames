import os
import utils


def add_score(difficulty):
    try:
        file = open(f"{utils.get_score_file_name()}", "r")
        current_points = file.readline()
        file.close()
    except PermissionError:
        print("No permission to edit score")
        return utils.bad_return()
    except FileNotFoundError:
        print("No score file")
        file = open(f"{utils.get_score_file_name()}", "w")
        file.write("0")
        file.close()
        current_points="0"


    POINTS_OF_WINNING = difficulty * 3 + 5 + int(current_points)
    file = open(f"{utils.get_score_file_name()}", "w")
    file.write(str(POINTS_OF_WINNING))
    file.close()
    return POINTS_OF_WINNING
