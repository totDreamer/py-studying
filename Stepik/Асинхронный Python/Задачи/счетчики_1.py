import asyncio


max_counts = {"Counter 1": 13, "Counter 2": 7}

counters = {"Counter 1": 0, "Counter 2": 0}


async def counter(name: str, time: int = 1) -> None:
    while counters[name] < max_counts[name]:
        counters[name] += 1
        await asyncio.sleep(time)
        print(f"{name}: {counters[name]}")


async def main() -> None:
    tasks = [asyncio.create_task(counter(name)) for name in max_counts]
    await asyncio.gather(*tasks)


asyncio.run(main())
