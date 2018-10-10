from sanic import Sanic
from sanic.response import json


from tcp_connect import TCPCommunication

app = Sanic()


@app.route("/")
def test(request):
    """
    :param request:
    :return:
    """
    data = b"123456"
    rcv_data = tcp_obj.is_device_activate(data)
    print(rcv_data)
    return json({"hello": rcv_data})


if __name__ == "__main__":
    tcp_obj = TCPCommunication()
    app.run(host="0.0.0.0", port=8000, workers=20)


# from sanic import Sanic
# from sanic import response
# from signal import signal, SIGINT
# import asyncio
# import uvloop
#
# app = Sanic(__name__)
#
#
# @app.route("/")
# async def test(request):
#     return response.json({"answer": "42"})
#
# asyncio.set_event_loop(uvloop.new_event_loop())
# server = app.create_server(host="0.0.0.0", port=8000)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(server)
# signal(SIGINT, lambda s, f: loop.stop())
# try:
#     loop.run_forever()
# except Exception as e:
#     print(e)
#     loop.stop()
