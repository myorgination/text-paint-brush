import tornado.ioloop
import tornado.web
from WordPainter import get_colors_from_text, setup_colors

mod_size = 300

class TextAreaSubmit(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        textFields = self.get_argument('textFields', '')
        color_set = get_colors_from_text(textFields)

        arr = []
        counter = 0
        for (x, color) in enumerate(color_set):
            arr.append({"color": str(color), "i": x % mod_size, "j": counter})
            if x % mod_size == mod_size - 1:
                counter += 1


        self.render(
            "templates/template.html" ,
            items=arr
        )

    def get(self):
        self.render("templates/template.html", items=[])


def make_app():
    return tornado.web.Application([
        (r"/", TextAreaSubmit),
        (r"/textPaint", TextAreaSubmit),
    ])

if __name__ == "__main__":
    setup_colors()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
