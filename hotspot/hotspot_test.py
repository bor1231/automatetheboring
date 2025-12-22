import asyncio
from winphotspot import Hotspot

async def main():
    hotspot = Hotspot()
    hotspot.config.ssid = "Borzoo"
    hotspot.config.passphrase = "StrongPassword123"
    await hotspot.start()  # ✅ Await the coroutine

# Run the async function
asyncio.run(main())