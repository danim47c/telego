
from telef.shortcuts import *


admin_node = MenuNode(
  init=texts.admin_message,
  back=Redirect.create_back(),
  markup_scheme=(2, 1)
).add_options(
  (
    texts.admin_button_users,
    Redirect.create_go(['users'])
  ),
  (
    texts.admin_button_channels,
    Redirect.create_go(['channels'])
  )
)

admin_node.register_spyder(
  lambda ctx: Redirect.create_to(['/']) if not ctx.user.admin else False
)


from bot.admin.users.users import users_node

admin_node.register_path(
  'users',
  users_node
)

from bot.admin.channels.channels import channels_node

admin_node.register_path(
  'channels',
  channels_node
)


def setup(node: Node):

  node.register_path(
    path='admin',
    func=admin_node
  )
