
from telef.shortcuts import *

list_node = ListNode(
  options_gen=lambda ctx: (
    {
      channel.name: Redirect.create_move([f'view?cid={channel.cid}']) for channel in Channel.select()
    }
  ),
  init=texts.admin_channels_list,
  back=Redirect.create_back(),
  empty_list=texts.admin_channels_list_empty
)
