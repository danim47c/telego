
from telef.shortcuts import *

search_node = Node()

@search_node.init_func_decorator()
def search_node_init_func(ctx: BaseContext):
  return ctx.send_msg(
    text=texts.admin_users_search,
    reply_markup=(
      teletypes.ReplyKeyboardMarkup().row(teletypes.KeyboardButton(texts.back))
    )
  )

@search_node.func_decorator()
def search_node_func(ctx: BaseContext):
  
  if ctx.text == texts.back: return Redirect.create_back()

  matches = [user for user in User.select().where(User.verified & (User.username.contains(ctx.text) | User.uid.contains(ctx.text)))]

  if len(matches) > 15:
    return ctx.send_msg(text=texts.admin_users_search_more)
  
  if len(matches) == 0:
    return ctx.send_msg(text=texts.admin_users_search_no)

  for match in matches:
    ctx.send_msg(
      text=texts.admin_users_search_user.format(user=match),
      reply_markup=(
        teletypes.InlineKeyboardMarkup().row(
          teletypes.InlineKeyboardButton(
            text=texts.admin_users_search_select,
            callback_data=str({'path': ['/', 'admin', 'users', f'view?uid={match.uid}']})
          )
        )
      )
    )
  
  return ctx.send_msg(
    text=texts.admin_users_search_done,
    reply_markup=(
      teletypes.ReplyKeyboardMarkup().row(teletypes.KeyboardButton(texts.back))
    )
  )

