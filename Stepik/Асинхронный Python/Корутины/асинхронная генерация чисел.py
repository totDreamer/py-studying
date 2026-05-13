import asyncio


async def generate(num: int) -> None:
    await asyncio.sleep(0.1)
    print(f"Корутина generate с аргументом {num}")


async def main():
    for num in range(10):
        await generate(num)


asyncio.run(main())
