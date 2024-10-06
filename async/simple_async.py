import asyncio
import aiohttp
from codetiming import Timer

async def task(url):
    timer = Timer(text=f"Task elapsed time: {{:.1f}}")
    async with aiohttp.ClientSession() as session:
        print(f"Getting URL: {url}")
        timer.start()
        async with session.get(url) as response:
            await response.text()
        timer.stop()

async def main():
    # Create the queue of work
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        for url in [
            "http://google.com",
            "http://yahoo.com",
            "http://linkedin.com",
            "http://apple.com",
            "http://microsoft.com",
            "http://facebook.com",
            "http://twitter.com",
        ]:
            await task(url)


if __name__ == "__main__":
    asyncio.run(main())