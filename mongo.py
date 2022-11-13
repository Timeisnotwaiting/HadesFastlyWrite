from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import DB_URL

mongo = MongoClient(DB_URL)

db = mongo.HFW

scoredb = db.score

async def get_user_score(chat_id: int, user_id: int):
    x = await scoredb.find_one({"chat_id": chat_id})
    if x:
        return x[str(user_id)]["score"]
    return 0

async def update_user_score(chat_id: int, user_id: int, score: int):
    return await scoredb.update_one({"chat_id": chat_id}, {"$set": {str(user_id): {"score": score}}}, upsert=True)
