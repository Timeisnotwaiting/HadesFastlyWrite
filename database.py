from mongo import db

scoredb = db.score

async def get_user_score(user_id: int, chat_id: int):
    get_score = scoredb.find_one({"chat_id": chat_id, "user_id": user_id})
    if get_score:
        score = get_score["score"]
        return score
    else:
        return 0

async def update_user_score(user_id: int, chat_id: int, score: int):
    try:
        await scoredb.update_one({"user_id": user_id, "chat_id": chat_id}, {"$set": {"score": score}}, upsert=True)
    except:
        pass
