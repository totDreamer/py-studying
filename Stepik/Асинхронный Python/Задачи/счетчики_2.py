import asyncio


max_counts = {"Counter 1": 10, "Counter 2": 5, "Counter 3": 15}

counters = {"Counter 1": 0, "Counter 2": 0, "Counter 3": 0}


delays = {"Counter 1": 1, "Counter 2": 2, "Counter 3": 0.5}


async def counter(name: str, time: (int, float) = 1) -> None:
    while counters[name] < max_counts[name]:
        counters[name] += 1
        await asyncio.sleep(time)
        print(f"{name}: {counters[name]}")


async def main() -> None:
    tasks = [asyncio.create_task(counter(name, delays[name])) for name in max_counts]
    await asyncio.gather(*tasks)


asyncio.run(main())
