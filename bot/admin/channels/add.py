
from telef.shortcuts import *

add_node = MenuNode(
  init=texts.admin_channels_add,
  back=Redirect.create_back(),
  markup_scheme=(2, 1)
).add_options(
  (
    texts.admin_channels_add_button_group,
    lambda ctx: ctx.send_msg(
      text=texts.admin_channels_add_group,
      reply_markup=(
        teletypes.InlineKeyboardMarkup().row(
          teletypes.InlineKeyboardButton(
            text=texts.admin_channels_add_group_link,
            url=f'http://telegram.me/{ctx.bot.get_me().username}?startgroup=group'
          )
        )
      )
    )
  ),
  (
    texts.admin_channels_add_button_channel,
    Redirect.create_go(['channel', 'public'])
  )
)

group_node = Node()

@group_node.init_func_decorator()
def group_node_init_func(ctx: BaseContext):

  name = ctx.message.chat.title

  while Channel.select().where(Channel.name == name):
    name += (' ' if not name.endswith(r' ') else '') + '-'

  channel = Channel.get_or_create(admin=ctx.user, group_id=ctx.chat_id, name=name, channel=False)[0]

  ctx.message.chat.id = ctx.user.uid

  ctx.bot.send_message(ctx.chat_id, texts.admin_channels_add_group_success)

  return Redirect.create_to(['/', 'admin', 'channels', f'view?cid={channel.cid}'])

add_node.register_path(
  path='group',
  func=group_node
)


channel_node = Node()

channel_node.register_path(
  path='public',
  func=Node().set_init_func(
    init_func=lambda ctx: ctx.send_msg(texts.admin_channels_add_channel_public.format(me=ctx.bot.get_me()), reply_markup=(
      teletypes.ReplyKeyboardMarkup().row(teletypes.KeyboardButton(texts.done))
    ))
  ).set_func(
    func=lambda ctx: Redirect.create_go([]) if not ctx.text == texts.done else Redirect.create_move(['id'])
  )
).register_path(
  path='id',
  func=FormNode(
    final=lambda ctx: Redirect.create_move(['test?cid="' + ctx.params['answers'][0] + '"']),
    back=Redirect.create_back(2)
  ).add_questions(
    (
      texts.admin_channels_add_channel_id,
      lambda ctx: False if ctx.text.startswith(r'@') else texts.admin_channels_add_channel_id_error
    )
  )
)

test_node = Node()

@test_node.init_func_decorator()
def test_node_init_func(ctx: BaseContext):
  return ctx.send_msg(texts.admin_channels_add_channel_test, reply_markup=(
    teletypes.ReplyKeyboardMarkup().row(
      teletypes.KeyboardButton(texts.admin_channels_add_channel_test_button)
    )
  ))

@test_node.func_decorator()
def test_node_func(ctx: BaseContext):
  if not ctx.text == texts.admin_channels_add_channel_test_button: return test_node_init_func(ctx)

  try:
    msg = ctx.bot.send_message(
      chat_id=ctx.params['cid'],
      text=texts.admin_channels_add_channel_test_message
    )
  except Exception as e:
    ctx.send_msg(e)

    ctx.send_msg(texts.admin_channels_add_channel_test_error, clear_markup=True)

    time_sleep(3)

    return Redirect.create_back(2)

  name = msg.chat.title

  while Channel.select().where(Channel.name == name):
    name += (' ' if not name.endswith(r' ') else '') + '-'

  channel = Channel.get_or_create(admin=ctx.user, channel_id=ctx.params['cid'], name=name, channel=True)[0]
  
  ctx.send_msg(texts.admin_channels_add_channel_success)

  return Redirect.create_to(['/', 'admin', 'channels', f'view?cid={channel.cid}'])

channel_node.register_path(
  path='test',
  func=test_node
)

add_node.register_path(
  path='channel',
  func=channel_node
)
