
from telef.shortcuts import *

menu_node = MenuNode(
  init=texts.menu,
  markup_scheme=(2,1)
).add_options(
  (
    texts.menu_button_posts_list,
    Redirect.create_go(['posts', 'list'])
  ),
  (
    texts.menu_button_post_create,
    Redirect.create_go(['posts', 'create'])
  ),
  (
    texts.menu_button_admin,
    Redirect.create_go(['admin'])
  )
).set_opt_check(
  func=lambda opt, ctx: opt != texts.menu_button_admin or ctx.user.admin
)


from bot.posts.posts import posts_node

menu_node.register_path(
  'posts',
  posts_node
)

from bot.admin.admin import admin_node

menu_node.register_path(
  'admin',
  admin_node
)


def setup(tf: TeleFramework):

  tf.register_path(
    path='/',
    func=menu_node
  )


