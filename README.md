# KuCoin-Python-AIO
## 目的
针对[python-kucoin](https://github.com/Kucoin/python-kucoin)进行aio异步包装，满足一些特定的场合需求。   
KuCoin API相关的细节请参考[官方文档](https://docs.kucoin.com/)

## 依赖
Python 3.5 +
aiohttp

## 安装
```bash
pip install kucoin-python-aio
```

## 特点
尽量在保持官方SDK的用法的同时，引入异步的机制

## 用法
```python
from kucoin.client import Client
from asyncio import get_event_loop

api_key = "5c753504ef83c77635824f12"
api_secret = "17d66aff-2b08-4473-9610-aa25e5993841"
api_passphrase = "abcd1234"
client = Client(api_key, api_secret, api_passphrase, sandbox=True)


async def test():
    try:
        currencies = await client.get_currencies()
        print(currencies)
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
```