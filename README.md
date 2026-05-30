# Letterboxd tools
## Setup
1. python -m venv venv
2. Activate: "venv\Scripts\activate" (Windows) or "source venv/bin/activate" (Linux)
3. pip install -r requirements.txt

## Usage
After setup you can use the scripts as follows (If in doubt add -h flag for usage help): 

### letterboxd_scraper

```python letterboxd_scraper.py <username1> <username2> <username3> ... ```

with username being the Letterboxd username `https://letterboxd.com/username` to print the watchlist and generate a .csv with the titles and years of release

### watchlist_intersecter

```python watchlist_intersecter.py <username1> <username2> <username3> ... ```

with username being the Letterboxd username `https://letterboxd.com/username` to print the intersected watchlist of all given
users and generate a .csv with the titles and years of release

## Dependecies
- **BeautifulSoup4** for parsing web request
- **Pandas** for dataframe handling
