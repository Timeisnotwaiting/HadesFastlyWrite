from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import DB_URL

mongo = MongoClient(DB_URL)

db = mongo.HFW

scoredb = db.score

async def 
