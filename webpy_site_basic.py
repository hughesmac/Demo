import web
import json

urls = (
    '/', 'Index',
    '/search', 'Search'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.search()

class Search:
    def GET(self):
        user_data = web.input()
        query = user_data.query.lower()

        with open('books.json', 'r') as f:
            books = json.load(f)

        results = [book for book in books if query in book['title'].lower()]

        return render.search(results=results)

if __name__ == "__main__":
    app.run()
