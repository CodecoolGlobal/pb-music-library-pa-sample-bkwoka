TIME_INDEX = -1
GENRE_INDEX = 3


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    genres = set([record[GENRE_INDEX] for record in albums])
    if genre not in genres:
        raise ValueError('Wrong genre')

    else:
        albums_list_by_genre = [album for album in albums if genre == album[GENRE_INDEX]]
        return albums_list_by_genre




def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    try:

        longest_time = str(convert_time_to_min(max(get_list_times_in_sec(albums)))).replace('.', ':')

        longest_album = [album for album in albums if longest_time in album[TIME_INDEX]]
    except ValueError:
        return False
    else:
        first_longest_album = 0
        return longest_album[first_longest_album]


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    sum_time_in_sec = sum(get_list_times_in_sec(albums))
    sum_time_in_min = convert_time_to_min(sum_time_in_sec)
    return sum_time_in_min


def convert_time_to_sec(time_in_min):
    time_tuple = map(int, time_in_min.split(':'))
    factor = [60, 1]

    time_in_sec = sum(a * b for a, b in zip(factor, time_tuple))
    return time_in_sec


def convert_time_to_min(time_in_sec):
    minutes = time_in_sec // 60
    seconds = time_in_sec - (minutes * 60)
    return float("{}.{}".format(minutes, seconds))


def get_list_times_in_sec(albums):
    albums_times = [record[TIME_INDEX] for record in albums]

    times_in_sec_list = []
    for time in albums_times:
        times_in_sec_list.append(convert_time_to_sec(time))
    return times_in_sec_list

def get_genre_stats():
    ...

def get_last_oldest():
    ...

def get_last_oldest_of_genre():
    ...