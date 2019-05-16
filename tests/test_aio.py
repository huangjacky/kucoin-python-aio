#! /usr/bin/python
# -*- coding: utf-8 -*-
from kucoin.client import Client
from asyncio import get_event_loop

api_key = "5c753504ef83c77635824f12"
api_secret = "17d66aff-2b08-4473-9610-aa25e5993841"
api_passphrase = "abcd1234"
client = Client(api_key, api_secret, api_passphrase, sandbox=True)


async def test():
    try:
        ws = await client.create_websocket(["/market/level2:ETH-BTC"])
        print(ws)
        async for msg in ws:
            print(msg.data)
    finally:
        await client.shutdown()


def main():
    loop = get_event_loop()
    loop.run_until_complete(test())


if __name__ == '__main__':
    main()