import tornado.ioloop
import tornado.web

class TextAreaSubmit(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        textFields = self.get_argument('textFields', '')

        self.render(
            "templates/template.html" ,
            items=["Item 1", "Item 2", "Item 3"]
        )

    def get(self):
        self.render("templates/template.html", items=[])


def make_app():
    return tornado.web.Application([
        (r"/", TextAreaSubmit),
        (r"/textPaint", TextAreaSubmit),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
