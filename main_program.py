"""
The main program should use functions from music_reports and display modules
"""
import display
import music_reports
from file_handling import *


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu_list = [
        'get_albums_by_genre',
        'get_longest_album',
        'get_total_albums_length',
        'exit_program'
    ]

    _exit = False
    while not _exit:
        display.print_command_result('Menu:')
        display.print_program_menu(menu_list)
        choice = int(input('Choice: '))
        try:
            if choice == 0:
                genre = input('Genre: ')
                albums_list_by_genre = music_reports.get_albums_by_genre(import_data(), genre)
                if albums_list_by_genre:
                    display.print_albums_list(albums_list_by_genre)
                else:
                    display.print_command_result('No albums of the genre')

            elif choice == 1:
                longest_album = music_reports.get_longest_album(import_data())
                if longest_album:
                    display.print_album_info(longest_album)
                else:
                    display.print_command_result('Error. Empty or broken data!')

            elif choice == 2:
                total_album_length = music_reports.get_total_albums_length(import_data())
                if total_album_length:
                    format_output_message = '{:.2f}'.format(total_album_length)
                    display.print_command_result(format_output_message)
                else:
                    display.print_command_result('Error. Empty or broken data!')
            elif choice == 3:
                _exit = True
        except ValueError as err:
            display.print_command_result(err)



if __name__ == '__main__':
    main()
