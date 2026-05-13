import asyncio


async def coroutine(num):
    await asyncio.sleep(1 / num)
    print(f"Coroutine {num} is done")


async def main():
    tasks = [asyncio.create_task(coroutine(num)) for num in range(1, 4)]
    await asyncio.gather(*tasks)


asyncio.run(main())
