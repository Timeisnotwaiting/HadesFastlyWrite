from mongo import db

scoredb = db.score
userchatdb = db.uc

async def get_user_score(user_id: int, chat_id: int):
    get_score = scoredb.find_one({"chat_id": chat_id, "user_id": user_id})
    if get_score:
        score = get_score["score"]
        return score
    else:
        return 0

async def update_user_score(user_id: int, chat_id: int, score: int):
    try:
        await scoredb.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"score": score}}, upsert=True)
    except:
        pass

async def add_user_in_chat(user_id: int, chat_id: int):
    already = await userchatdb.find_one({"chat_id": chat_id})
    user_list = []
    if already:
        user_list = already["user_list"]
        if user_id in user_list:
            return
    user_list.append(user_id)
    await userchatdb.update_one({"chat_id": chat_id}, {"$set": {"user_list": user_list}})

