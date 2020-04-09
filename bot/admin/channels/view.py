
from telef.shortcuts import *


view_node = MenuNode(
  init=lambda ctx: ctx.send_msg(text=texts.admin_channels_view.format(admin=ctx.user, channel=Channel.get(cid=ctx.params['cid'])), default_markup=True),
  back=Redirect.create_back(),
  markup_scheme=(1, 1)
).add_options(
  (
    texts.admin_channels_view_button_remove,
    Redirect.create_go(['remove'])
  )
).register_path(
  path='remove',
  func=BooleanNode(
    init=texts.admin_channels_view_remove,
    true=lambda ctx: (
      ChannelPost.delete().where(ChannelPost.channel.cid == (cid := ctx.params['cid'])),
      ChannelUser.delete().where(ChannelUser.channel.cid == cid),
      Channel.delete_by_id(cid),
      Redirect.create_back(2)
    )[-1],
    false=lambda ctx: Redirect.create_to(['/', 'admin', 'channels', 'view?cid=' + str(ctx.params['cid'])])
  )
)
