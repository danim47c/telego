
from telef.shortcuts import *

channels_node = MenuNode(
  init=lambda ctx: ctx.send_msg(texts.admin_channels.format(num=Channel.select().count()), default_markup=True),
  back=Redirect.create_back(),
  markup_scheme=(2, 1)
).add_options(
  (
    texts.admin_channels_button_list,
    Redirect.create_go(['list'])
  ),
  (
    texts.admin_channels_button_add,
    Redirect.create_go(['add'])
  )
)


from bot.admin.channels.list import list_node

channels_node.register_path(
  'list',
  list_node
)

from bot.admin.channels.view import view_node

channels_node.register_path(
  'view',
  view_node
)

from bot.admin.channels.add import add_node

channels_node.register_path(
  'add',
  add_node
)
