import time
import asyncio


async def scan_ip(ip):
    print(f"scanning initiated for : {ip}")
    # scanning logic here
    await asyncio.sleep(2)
    print(f"completed scanning for : {ip}")


async def main():
    task1 = asyncio.create_task(scan_ip('10.0.0.1'))
    task2 = asyncio.create_task(scan_ip('10.0.0.2'))
    task3 = asyncio.create_task(scan_ip('10.0.0.3'))
    task4 = asyncio.create_task(scan_ip('10.0.0.4'))
    task5 = asyncio.create_task(scan_ip('10.0.0.5'))
    await asyncio.gather(task1, task2, task3, task4, task5)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:0.2f} seconds.")
