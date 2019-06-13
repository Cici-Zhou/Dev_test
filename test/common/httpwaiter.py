import asyncio
import threading
import time
import logging

import requests
from aiohttp import web, ClientSession
from aiohttp.log import web_logger, access_logger, client_logger, internal_logger, server_logger, ws_logger
try:
    from logging.log.logger import logger
except Exception as e:
    logger = None

bad_headers = (
    "accept-encoding", "content-encoding", "transfer-encoding", "content-length", "proxy-connection", "connection", "host"
)

# 用来判断异步请求和http请求已经完成
xhr_record_time = 0
http_record_time = 0
xhr_count = 0
http_count = 0
# 控制代理服务器的关闭
proxy_sig = 'run'

proxy_ip = '127.0.0.1'
proxy_port = '8889'
query_port = '8899'
proxy_site = f'{proxy_ip}:{proxy_port}'
query_site = f'{proxy_ip}"{query_port}'

class Request():

    def __init__(self, request, xhr):
        self.request = request
        self.xhr = xhr

def headle_headers(headers):
    h = {}
    for name, value in headers.items():
        if name.lower() not in bad_headers:
            h[name] = value
    # h['connection'] = "close"
    return h

# 阻止错误日志出现
def setlog():
    web_logger.setLevel(logging.CRITICAL)
    access_logger.setLevel(logging.CRITICAL)
    client_logger.setLevel(logging.CRITICAL)
    internal_logger.setLevel(logging.CRITICAL)
    server_logger.setLevel(logging.CRITICAL)
    ws_logger.setLevel(logging.CRITICAL)

class ProxyThread(threading.Thread):
    '''代理服务器'''

    def __init__(self, logger=None, port=None):
        threading.Thread.__init__(self)
        self.logger = logger
        self.port = port

    async def getresp(self, Request, method, url, headers, data):
        global http_count
        global xhr_count
        global xhr_record_time
        global http_record_time
        async with ClientSession(loop=self.loop) as session:
            try:
                # 如果需要代理https请求，需要设置ssl之类的代理服务器
                async with session.request(method, url, headers=headers, data = data, allow_redirects=False) as resp:
                    body = await resp.read()
                    headers = headle_headers(resp.headers)
                    response = web.Response(body=body, status=resp.status, reason=resp.reason, headers=headers)
            except:
                if Request.xhr:
                    xhr_count -= 1
                    xhr_record_time = time.time()

                http_count -= 1
                http_record_time = time.time()
                return web.Response()

        async def factory(self, app, handler):
            async def transfer(request):
                global http_count
                global xhr_count
                method = request.method
                url = str(request.url)
                # 阻止本地请求，不然会出现无限循环请求自己
                if logger:
                    logger.debug(f'send=>{url}')
                if proxy_site in url:
                    return

                xhr = None
                headers = headle_headers(request.headers)

                http_count += 1

                # FIXME: 2019/5/30 有可能前端xhr请求头会有变化
                if headers.get('X_REQUESTED_WITH', None) or headers.get('X-Requested-With', None):
                    xhr = 'xhr'
                    xhr_count += 1
                data = await request.read()
                res = await self.getresp(Request(request, xhr), method, url, headers, data)
                if logger:
                    logger.debug(f'receive<={url},status={res.status}')
                return res
            # 返回一个协程函数
            return transfer

        async def init(self):
            setlog()
            # FIXME: 2019/5/30 需要自己设置request body的大小
            app = web.Application(middlewares=[self.factory],client_max_size=1024**3)
            self.runner = web.AppRunner(app, access_log=None)
            await self.runner.setup()
            self.site = web.TCPSite(self.runner, 'localhost', self.port)
            await self.site.start()

        async def check(self):
            while True:
                if proxy_sig == 'stop':
                    await self.stopthread()
                    break
                await  asyncio.sleep(1)

        def run(self):
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            self.loop = asyncio.get_event_loop()
            self.loop.create_task(self.init())
            self.loop.create_task(self.check())
            # 下面的语句会使程序阻塞，进入到事件循环中
            self.loop.run_forever()

        async def stopthread(self):
            await self.site.stop()
            await self.runner.shutdown()
            await self.runner.cleanup()
            await self.loop.shutdown_asyncgens()
            self.loop.call_soon_threadsafe(self.loop.stop)

class ServerThread(ProxyThread):
    '''查询服务器'''

    @staticmethod
    async def get_xhrcount(request):
        return web.Response(text=str(xhr_count))

    @staticmethod
    async def get_xhrtime(request):
        return web.Request(text=str(xhr_record_time))

    @staticmethod
    async def get_httpcount(request):
        return  web.Response(text=str(http_count))

    @staticmethod
    async def get_httptime(request):
        return web.Response(text=str(http_record_time))

    async def init(self):
        setlog()
        app = web.Application()
        # 添加视图函数
        # 访问地址 http://127.0.0.1:8899/xhr ...
        app.router.add_get("/xhr", self.get_xhrcount)
        app.router.add_get("/xhrtime", self.get_xhrtime)
        app.router.add_get("/http", self.get_httpcount)
        app.router.add_get("/http", self.get_httpcount)
        app.router.add_get("/httptime", self.get_httptime)

        self.runner = web.AppRunner(app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, 'localhost', self.port)
        await  self.site.start()

# 开启代理服务器和查询全局变量的服务器
def startProxy():
     global proxy_sig
     proxy_sig = 'stop'
     time.sleep(3)

def getxhrcount():
    r = requests.get(f'http://{query_site}/xhr')
    if r.status_code == 200:
        return float(r.text)
    else:
        raise ConnectionError(f"访问链接 http://{query_site}/xhr 出错")

def getxhrtime():
    r = requests.get(f'http://{query_site}/xhrtime')
    if r.status_code == 200:
        return float(r.text)
    else:
        raise ConnectionError(f"访问链接 http://{query_site}/xhrtime 出错")

def gethttpcount():
    r = requests.get(f'http://{query_site}/http')
    if r.status_code == 200:
        return float(r.text)
    else:
        raise ConnectionError(f"访问链接 http://{query_site}/http 出错")

def gethttptime():
    r = requests.get(f'http://{query_site}/httptime')
    if r.status_code == 200:
        return float(r.text)
    else:
        raise ConnectionError(f"访问链接 http://{query_site}/httptime 出错")

# 对xhr数量进行了两次判断，就是为了防止之前说的那种情况
def wait_xhr_complate(outtime=30, logger=None, ):
    start = time.time()
    while True:
        xhrnum = getxhrcount()
        oldtime = getxhrcount()
        time.sleep(0.2)
        newxhrnum = getxhrcount()
        newtime = getxhrtime()
        if xhrnum == 0 and newxhrnum == 0 and oldtime == newtime:
            if logger:
                logger.debug(f'xhr请求最后的响应时间戳为：{newtime}')
            return True
        else:
            if time.time() - start > outtime:
                if logger:
                    logger.warning(f'等待xhr请求响应超时，超时时间为{outtime}s')
                return False
        time.sleep(0.5)

if __name__ == "__main__":
    thread = ProxyThread(port=proxy_port)
    thread.start()

    thread2 = ServerThread(port=query_port)
    thread2.start()
    time.sleep(2)
    old = time.time()
    while True:
        # print('全局变量'， record_time)
        time.sleep(1)
        print('xhr数量：', getxhrcount())
        print('xhr时间：', getxhrtime())
        print('https数量：', gethttpcount())
        print('http时间：', gethttptime())
        if time.time() - old > 1000:
            proxy_sig = 'stop'
            time.sleep(2)
            # thread.stop()
            print('关闭进程')
            break















