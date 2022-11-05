from mongo import db

score = db.score
 
async def get_user_score(chat_id: int, user_id: int):
    sc = await score.find_one({"chat_id": chat_id})
    if sc:
        x = int(sc["user_info"][str(user_id)]["score"])
        return x
    else:
        return 0

async def update_user_score(chat_id: int, user_id: int, points: int):
    get_score = await get_user_score(chat_id, user_id)
    final = get_score + points
    update_set = {"user_info": {str(user_id): {"score": final}}}
    await score.update_one({"chat_id: chat_id}, {"$set": update_set})

