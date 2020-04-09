
from telef.shortcuts import *


users_node = MenuNode(
  init=texts.admin_users,
  back=Redirect.create_back(),
  markup_scheme=(2, 1)
).add_options(
  (
    texts.admin_users_button_search,
    Redirect.create_go(['search'])
  ),
  (
    texts.admin_users_button_broadcast,
    Redirect.create_go(['broadcast'])
  )
)


from bot.admin.users.view import view_node

users_node.register_path(
  'view',
  view_node
)

from bot.admin.users.search import search_node

users_node.register_path(
  'search',
  search_node
)

from bot.admin.users.broadcast import broadcast_node

users_node.register_path(
  'broadcast',
  broadcast_node
)
