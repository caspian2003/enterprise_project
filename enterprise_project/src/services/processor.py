import asyncio

async def process_item(item):
    await asyncio.sleep(0.5)
    return f"Processed {item}"

async def process_data(data):
    tasks = [process_item(d) for d in data]
    return await asyncio.gather(*tasks)