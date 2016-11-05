
"""
Server for hereacg auth platform
"""

import util
import config as _c
import tornado.httpserver
import tornado.ioloop
import tornado.options


from tornado.options import define, options


define('port',default=8081,
        help="Nothing. Runing server at a port",type=int)


define('fork',default=False,help="is fork?",type=bool)


define('forknum',default=1,help='how many fork?',type=int)


def _run_server(handler,port=options.port,forkmode=options.fork,forknum=options.forknum):
    print('Web server is loading')
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(handler)
    print('Checking config:')
    for k in _c.app_configs: print('Config item {} => {}'.format(k,_c.app_configs[k]))
    print('Server will be running at port {}.'.format(port))
    if forkmode:
        print('Fork mode.Forknum is {}.'.format(forknum))
        http_server.bind(port)
        http_server.start(forknum)
    else:
        http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


def run_server(*args,**kargs):
    app = util.get_application()
    _run_server(app,*args,**kargs)


if __name__ == "__main__":
    run_server()
