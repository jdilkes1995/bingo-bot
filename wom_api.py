import wom
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
keyid = os.getenv("WOM_API_ID")

async def main() -> None:
    client = wom.Client()
    await client.start()

    client.set_api_key(keyid)
    result = await client.groups.get_details(139)

    if result.is_ok:
        details = result.unwrap()
        print(details.group)
        print(details.memberships)
    else:
        print(f"Error: {result.unwrap_err()}")
              
    await client.close()

async def add(id, team):
    

if __name__ == "__main__":
    asyncio.run(main())