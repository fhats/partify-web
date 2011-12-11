import tornado.ioloop
import tornado.web

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/docs/(.*)", tornado.web.StaticFileHandler, {"path": "docs"}),
	(r"/", tornado.web.RedirectHandler, {"url": "https://github.com/fxh32/partify/wiki"}),
	(r"/install", tornado.web.RedirectHandler, {"url": "https://github.com/fxh32/partify/wiki/Installation"}),
    ])
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()

