import time
import asyncio
import aiohttp


async def fetch_rfc(rfc_number):
    url = f'https://www.ietf.org/rfc/rfc{rfc_number}.txt'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(f"{url} --> Content-Length : {len(content)}")


async def main():
    tasks = []
    for rfc_number in range(2000, 2010):
        task = asyncio.create_task(fetch_rfc(rfc_number))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:0.2f} seconds.")
