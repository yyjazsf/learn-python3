import asyncio


async def get_page(host):
    # print("start", host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    print(header)
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
task = [get_page(i) for i in [r'www.yingyj.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(task))
loop.close()
