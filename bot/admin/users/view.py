
from telef.shortcuts import *


view_node = MenuNode(
  init=lambda ctx: ctx.send_msg(texts.admin_users_view.format(user=User.get(uid=ctx.params['uid'])), default_markup=True),
  back=Redirect.create_back(),
  markup_scheme=(1, 2, 1)
).add_options(
  (
    texts.admin_users_view_button_manage,
    Redirect.create_go(['channels'])
  ),
  (
    texts.admin_users_view_button_block,
    Redirect.create_go(['block'])
  ),
  (
    texts.admin_users_view_button_unblock,
    Redirect.create_go(['block'])
  ),
  (
    texts.admin_users_view_button_make,
    Redirect.create_go(['admin'])
  ),
  (
    texts.admin_users_view_button_remove,
    Redirect.create_go(['admin'])
  )
)

def view_node_opt_check(opt: str, ctx: BaseContext):
  user = User.get(uid=ctx.params['uid'])
  if opt == texts.admin_users_view_button_block:
    if user.blocked: return False
  elif opt == texts.admin_users_view_button_unblock:
    if not user.blocked: return False
  elif opt == texts.admin_users_view_button_make:
    if user.admin: return False
  elif opt == texts.admin_users_view_button_remove:
    if not user.admin: return False
  return True

view_node.set_opt_check(
  func=view_node_opt_check
)

view_node.register_path(
  path='block',
  func=BooleanNode(
    init=lambda ctx: ctx.send_msg(
      texts.admin_users_view_block.format(
        block='unblock' if (user := User.get(uid=ctx.params['uid'])).blocked else 'block',
        user=user
      ),
      default_markup=True
    ),
    true=lambda ctx: (
      user := User.get(uid=ctx.params['uid']),
      user.toggle('blocked'),
      Redirect.create_to(['/', 'admin', 'users', 'view?uid=' + str(ctx.params['uid'])])
    )[-1],
    false=lambda ctx: Redirect.create_to(['/', 'admin', 'users', 'view?uid=' + str(ctx.params['uid'])])
  )
).register_path(
  path='admin',
  func=BooleanNode(
    init=lambda ctx: ctx.send_msg(
      texts.admin_users_view_make.format(
        make='remove' if (user := User.get(uid=ctx.params['uid'])).admin else 'make',
        user=user
      ),
      default_markup=True
    ),
    true=lambda ctx: (
      user := User.get(uid=ctx.params['uid']),
      user.toggle('admin'),
      Redirect.create_to(['/', 'admin', 'users', 'view?uid=' + str(ctx.params['uid'])])
    )[-1],
    false=lambda ctx: Redirect.create_to(['/', 'admin', 'users', 'view?uid=' + str(ctx.params['uid'])])
  )
).register_path(
  'channels',
  CheckListNode(
    options_gen=lambda ctx: (
      {
        channel.name: (
          lambda ctx: ChannelUser.select().where(
            ChannelUser.user == User.get(uid=ctx.params['uid']),
            ChannelUser.channel == Channel.get(name=ctx.params['option'])
          ).exists(),
          lambda ctx: ChannelUser.create(
            user=User.get(uid=ctx.params['uid']),
            channel=Channel.get(name=ctx.params['option'])
          ) if not ChannelUser.select().where(
            ChannelUser.user == User.get(uid=ctx.params['uid']),
            ChannelUser.channel == Channel.get(name=ctx.params['option'])
          ).exists() else ChannelUser.get(
            user=User.get(uid=ctx.params['uid']),
            channel=Channel.get(name=ctx.params['option'])
          ).delete_instance()
        ) for channel in Channel.select()
      }
    ),
    init=texts.admin_users_view_manage,
    done=Redirect.create_back(),
    empty_list=texts.admin_users_view_manage_empty
  )
)