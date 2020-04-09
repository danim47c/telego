
from telef.shortcuts import *

list_node = ListNode(
  options_gen=lambda ctx: (
    {
      post.name: Redirect.create_move([f'view?pid={post.pid}']) for post in ctx.user.posts
    }
  ),
  init=texts.posts_list,
  back=Redirect.create_back(),
  empty_list=texts.posts_list_no_posts,
  row_width=2
)
