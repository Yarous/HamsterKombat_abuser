from aiohttp import ClientSession

session: ClientSession = None

async def init_session():
    global session
    if session is None:
        session = ClientSession()
        
        
async def close_session():
    if session:
        await session.close()
