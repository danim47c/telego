
from telef.shortcuts import *


posts_node = Node()

@posts_node.init_func_decorator()
@posts_node.func_decorator()
def posts_node_func(ctx: BaseContext): return Redirect.create_back()


from bot.posts.list import list_node

posts_node.register_path(
  'list',
  list_node
)


from bot.posts.view import view_node

posts_node.register_path(
  'view',
  view_node
)


from bot.posts.create import create_node

posts_node.register_path(
  'create',
  create_node
)
