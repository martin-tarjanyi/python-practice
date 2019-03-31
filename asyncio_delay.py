import asyncio
import threading
import time
from typing import List, Coroutine


async def log(text: str):
    print(f"{threading.current_thread().name}: {text}")


async def printer(i: int):
    await log(f"Started on {threading.current_thread().name}: {i}")

    await log("Hello ")
    await log("someone ")

    await asyncio.sleep(i)

    await log("world!")
    await log("universe!")

    await log(f"Finished {threading.current_thread().name}: {i}")


def async_io_delay_main():
    start: float = time.time()

    tasks: List[Coroutine] = [printer(n) for n in range(5).__reversed__()]
    tasks_future = asyncio.gather(*tasks)
    asyncio.get_event_loop().run_until_complete(tasks_future)
    time_spent: float = (time.time() - start)

    print(f"Took {time_spent} seconds to complete.")


if __name__ == '__main__':
    async_io_delay_main()
