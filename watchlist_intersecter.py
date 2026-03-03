import pandas as pd
import sys
import letterboxd_scrapper as scrapper

HELP_MESSAGE = "USAGE: \n    " \
        "python watchlist_intersecter.py [-i <watchlist1.csv> <watchlist2.csv> <watchlist3.csv> ... |\n                                 "\
        "       <user1> <user2> <user3> ... | -h]"
def intersect_watchlists(watchlists):
    print("Intersecting watchlists...")
    intersected_watchlist = watchlists[0]
    for i in range(1, len(watchlists)):
        intersected_watchlist = intersected_watchlist.merge(watchlists[i], how='inner', on=['Name','Year'])
    print("Intersected watchlists:")
    return intersected_watchlist

def print_watchlist(watchlist):
    print('\nWatchlist:\n')
    if watchlist.empty:
        print('Watchlist is empty')
        return
    for index, row in watchlist.iterrows():
        print(row['Name'], row['Year'])

if __name__ == "__main__":
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print(HELP_MESSAGE)
    elif "-i" in sys.argv[1:] or "--input" in sys.argv[1:]:
        if len(sys.argv) > 2:
            argv = sys.argv[2:]
            watchlists = []
            for arg in argv:
                csv_path = arg
                watchlists.append(pd.read_csv(csv_path))
            print_watchlist(intersect_watchlists(watchlists))
        else:
            print(HELP_MESSAGE)
    else:
        if len(sys.argv) > 1:
            argv = sys.argv[1:]
            watchlists = []
            for user in argv:
                watchlists.append(scrapper.retrive_watchlist_from_user(user))
            print_watchlist(intersect_watchlists(watchlists))
        else:
            print(HELP_MESSAGE)