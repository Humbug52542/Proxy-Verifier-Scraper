import asyncio, aiohttp

async def test(s, p):
    try:
        async with s.get("http://httpbin.org/ip", proxy=f"http://{p}", timeout=5) as r:
            if r.status == 200:
                return p
    except (aiohttp.ClientError, asyncio.TimeoutError):
        pass

async def run(lst):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as s:
        res = await asyncio.gather(*[test(s, p) for p in lst])
    return [x for x in res if x]

def verify_proxies(lst):
    return asyncio.run(run(lst))
