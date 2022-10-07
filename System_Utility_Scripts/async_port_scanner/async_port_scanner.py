import asyncio


async def check_port(ip, port, loop):
    conn = asyncio.open_connection(ip, port, loop=loop)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=3)
        print(ip, port, 'ok')
        return (ip, port, True)
    except:
        print(ip, port, 'nok')
        return (ip, port, False)
    finally:
        if 'writer' in locals():
            writer.close()


async def check_port_sem(sem, ip, port, loop):
    async with sem:
        return await check_port(ip, port, loop)


async def run(dests, ports, loop):
    sem = asyncio.Semaphore(400)  # Change this value for concurrency limitation
    tasks = [asyncio.ensure_future(check_port_sem(sem, d, p, loop)) for d in dests for p in ports]
    responses = await asyncio.gather(*tasks)
    return responses


dests = ['google.com', 'youtube.com']  # destinations
ports = [80, 443, 8080, 8443]  # ports

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(dests, ports, loop))
loop.run_until_complete(future)
print('#' * 50)
print('Results: ', future.result())
