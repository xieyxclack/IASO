# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import operation


define("port", default=8000, help="run on the given port", type=int)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    )

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        (r"/", MainHandler),
        (r"/symptom", SymptomHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",)


class SymptomHandler(tornado.web.RequestHandler):
    def post(self):
        symptom = self.get_argument("symptom", None)
        panduan = self.get_argument("panduan", None)
        second_symptom = self.get_arguments("second_symptom")
        print second_symptom
        print symptom, panduan
        symptom_input, segment_result, match_result, symptom_match, disease_list, related_symptom_list = operation.post(symptom, panduan, second_symptom)
        self.render("symptom.html", symptom_input=symptom_input,
                    segment_result=segment_result, match_result=match_result, symptom_count=len(symptom_match),
                    symptom_match=symptom_match, disease_list=disease_list, related_symptom_list=related_symptom_list)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
