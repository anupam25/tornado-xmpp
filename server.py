"""XMPP server"""

import xmpp
import tornado.httpserver
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")


class Application(tornado.web.Application):
    
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict()
        super(Application, self).__init__(handlers, **settings)
        
        
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
