import bs4
import requests

res = requests.get('https://thegreatestbooks.org/')

booksSoup = bs4.BeautifulSoup(res.text, features="html.parser")

books_select = booksSoup.select('h4 a')
books_cleared = []

for item in books_select:
    split_item = item.text.split(' by ')
    books_cleared.append(split_item[0].rstrip())

best_books = {}

for i, v in enumerate(books_cleared):
    best_books[v] = i + 1

print(best_books)