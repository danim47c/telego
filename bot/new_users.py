
from telef.shortcuts import *


def new_user_message(ctx: BaseContext):

  for admin in User.select().where(User.admin):

    msg = ctx.bot.send_message(
      chat_id=admin.uid,
      text=texts.admin_new_user.format(user=ctx.user),
      reply_markup=(
        teletypes.InlineKeyboardMarkup().row(
          teletypes.InlineKeyboardButton(
            texts.admin_new_user_verify,
            callback_data=str(
              {'command': f'/verify?uid={ctx.user.uid}'}
            )
          )
        ).row(
          teletypes.InlineKeyboardButton(
            texts.admin_new_user_block,
            callback_data=str(
              {'command': f'/block?uid={ctx.user.uid}'}
            )
          )
        )
      )
    )

    admin.update_temp_name('new_user_messages', {ctx.user.uid: msg.message_id})


def new_user_update(ctx: BaseContext, user: User, verified: bool):

  for admin in User.select().where(User.admin):

    if str(user.uid) in admin.temp_name('new_user_messages'):

      ctx.bot.edit_message_text(
        text=(
          texts.admin_new_user_verified if verified else texts.admin_new_user_blocked
        ).format(user=user, admin=admin),
        message_id=admin.del_temp_dict_name('new_user_messages', str(user.uid), get=True),
        chat_id=admin.uid,
        reply_markup=(
          teletypes.InlineKeyboardMarkup().row(
            teletypes.InlineKeyboardButton(
              texts.admin_new_user_revise,
              callback_data=str({'path': ['/', 'admin', 'users', f'view?uid={user.uid}']})
            )
          )
        )
      )







