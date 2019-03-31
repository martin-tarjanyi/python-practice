import asyncio

from aiohttp import ClientResponse, ClientSession


async def execute_http_call(url: str):
    async with ClientSession() as session:  # same as try-with-resources in java
        print(f"Calling url: {url}")
        response: ClientResponse = await session.get(url)
        print(f"Finished calling url: {url}")
        return await response.json()


async def query_posts():
    posts: list = await execute_http_call("https://my-json-server.typicode.com/typicode/demo/posts")
    post_ids = (post["id"] for post in posts)
    urls = (f"https://my-json-server.typicode.com/typicode/demo/posts/{str(post_id)}" for post_id in post_ids)
    responses = await asyncio.gather(*(execute_http_call(url) for url in urls))
    for response in responses:
        print(response)


def async_http_main():
    asyncio.run(query_posts())


if __name__ == '__main__':
    async_http_main()

