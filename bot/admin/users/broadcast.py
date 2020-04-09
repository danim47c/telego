
from telef.shortcuts import *


broadcast_node = Node()

@broadcast_node.init_func_decorator()
def broadcast_node_init_func(ctx: BaseContext):
  return ctx.send_msg(
    text=texts.admin_users_broadcast,
    reply_markup=(
      teletypes.ReplyKeyboardMarkup().row(teletypes.KeyboardButton(texts.done))
    )
  )

@broadcast_node.func_decorator()
def broadcast_node_func(ctx: BaseContext):

  if ctx.text == texts.done: return Redirect.create_back()

  users = [user for user in User.select().where(User.blocked == False) if not user.uid == ctx.user.uid]

  for user in range(len(users)):

    try:
      ctx.bot.forward_message(
        chat_id=users[user].uid,
        from_chat_id=ctx.chat_id,
        message_id=ctx.message.message_id
      )
    except: pass

    time_sleep(0.05)

  ctx.send_msg(
    text=texts.admin_users_broadcast_done.format(num=len(users))
  )

  return broadcast_node_init_func(ctx)

