import asyncio
import datetime
import os
import random
import string
import time
import traceback
import config

import aiofiles
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)



broadcast_ids = {}
dev = config.AUTH_USERS


async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


async def broadcast(db, message):
    all_users = await db.get_all_users()
    broadcast_msg = message.reply_to_message
    while True:
        broadcast_id = "".join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users, current=done, failed=failed, success=success
    )
    async with aiofiles.open("users_info.txt", "w") as broadcast_log_file:
        async for user in all_users:
            if (user["id"]) not in dev:
                sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success)
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    if failed == 0:
        await message.reply_text(
            text=f"Message deliverd to {success} users out of {total_users}  \nwithin`{completed_in}`",
            quote=True,
        )
    else:
        await message.reply_document(
            document="users_info.txt",
            caption=f"Message deliverd to {success} users out of {total_users} \nwithin`{completed_in}`",
            quote=True,
        )
    os.remove("users_info.txt")








@Client.on_message(filters.command("send_group") & filters.private)
async def broadcast(self, message):
    user_id = message.from_user.id
    if user_id in AUTH_USERS:
        text = message.reply_to_message
        groups = await db.get_all_chats()
        if not text:
            await message.reply_text("please reply to a message")
            
        else:
            failed = 0
            sent = 0
            msg = await message.reply_text("sending broadcast...")
            async for chat in groups:
                if sent % 25 == 0:
                    await asyncio.sleep(1)
                try:
                    await message.copy(chat["id"], text)
                    sent += 1
                except (PeerIdInvalid, ChannelInvalid):
                    failed += 1
                    LOGGER.warning("Can't send broadcast to \"%s\" with id %s",
                                   chat["title"], chat["id"])
            await msg.edit_text(
                "Broadcast complete!\n"
                f"{sent} groups succeed, {failed} groups failed to receive the message"
            )



    else:
        message.reply_text("you are not a authorised person to use this command")

    