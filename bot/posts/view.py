
from telef.shortcuts import *

def send_post_raw(bot: TelegramBot, chat_id: int, post: Post, markup=None):
  return bot.send_photo(
    chat_id=chat_id,
    photo=post.file_id,
    caption=post.caption,
    reply_markup=markup if markup else (
      teletypes.InlineKeyboardMarkup().row(
        teletypes.InlineKeyboardButton(
          text=texts.post_button.format(author=post.author),
          url=f'telegram.me/{post.author.username}'
        )
      )
    )
  )

def send_post(ctx: BaseContext, post: Post, inline: bool = True):
  
  return send_post_raw(ctx.bot, ctx.chat_id, post, markup=ctx.markup if not inline else None)


view_node = MenuNode(
  init=lambda ctx: send_post(ctx, Post.get(pid=ctx.params['pid']), inline=False),
  back=Redirect.create_to(['/']),
  markup_scheme=(2, 2, 1, 1)
).add_options(
  (
    texts.posts_view_button_send,
    Redirect.create_go(['send'])
  ),
  (
    texts.posts_view_button_schedule,
    Redirect.create_go(['schedule'])
  ),
  (
    texts.posts_view_button_edit,
    Redirect.create_go(['edit'])
  ),
  (
    texts.posts_view_button_remove,
    Redirect.create_go(['remove'])
  ),
  (
    texts.posts_view_button_view,
    lambda ctx: send_post(ctx, Post.get(pid=ctx.params['pid']))
  )
)

def send_func(ctx: BaseContext):
  channel = Channel.get(cid=(cid := ctx.params['cid']))
  post = Post.get(pid=ctx.params['pid'])

  if 'sent' in ctx.user.temp: sent = ctx.user.temp_name('sent')
  else: sent = {}

  if str(cid) in sent and not (num := (datetime.now() - datetime.fromtimestamp(sent[str(cid)]))).seconds > 3600:

    ctx.send_msg(texts.posts_view_send_time.format(x=round(60 - (num.seconds / 60))))

  else:

    ctx.user.update_temp_name('sent', {channel.cid: datetime.now().timestamp()})

    send_post_raw(
      ctx.bot,
      chat_id=channel.channel_id if channel.channel else channel.group_id,
      post=post
    )

  return Redirect.create_back(2)

view_node.register_path(
  'send',
  Node().set_init_func(
    lambda ctx: Redirect.create_go(['channel'])
  ).register_path(
    'channel',
    ListNode(
      options_gen=lambda ctx: (
        {
          channel.channel.name: Redirect.create_move([f'send?cid={channel.channel.cid}']) for channel in ctx.user.channels
        }
      ),
      init=texts.posts_view_send_choose,
      back=Redirect.create_back(2),
      empty_list=texts.posts_view_schedule_channels_no
    )
  ).register_path(
    'send',
    send_func
  )
)


schedule_node = MenuNode(
  init=lambda ctx: ctx.send_msg(
    texts.posts_view_schedule.format(**(
      {
        'scheduled': texts.posts_view_scheduled_yes if (post := Post.get(pid=ctx.params['pid'])).scheduled else texts.posts_view_scheduled_no,
        'interval': post.interval,
        'channels': channels if (channels := ', '.join(channel.channel.name for channel in post.channels)) != '' else texts.posts_view_scheduled_no_channels
      }
    )),
    default_markup=True
  ),
  back=Redirect.create_back(),
  markup_scheme=(1, 2, 1)
).add_options(
  (
    texts.posts_view_schedule_button_toggle,
    lambda ctx: (
      Post.get(pid=ctx.params['pid']).toggle('scheduled'),
      Redirect.create_go([])
    )[-1]
  ),
  (
    texts.posts_view_schedule_button_interval,
    Redirect.create_go(['interval'])
  ),
  (
    texts.posts_view_schedule_button_channels,
    Redirect.create_go(['channels'])
  )
).register_path(
  'interval',
  NumSelectorNode(
    changers=(1, 15, 30, 60),
    getter=lambda ctx: interval if (interval := Post.get(pid=ctx.params['pid']).interval) != None else 60,
    setter=lambda ctx, num: Post.get(pid=ctx.params['pid']).set('interval', num).set('last', datetime.now().timestamp()),
    init=texts.posts_view_schedule_interval,
    final=Redirect.create_back(),
    check=lambda ctx: False if ctx.params['num'] >= 60 else texts.posts_view_schedule_interval_more,
    markup_scheme=(4,1,4,1)
  ) 
).register_path(
  'channels',
  CheckListNode(
    options_gen=lambda ctx: (
      {
        channel.channel.name: (
          lambda ctx: ChannelPost.select().where(
            ChannelPost.post == Post.get(pid=ctx.params['pid']),
            ChannelPost.channel == Channel.get(name=ctx.params['option'])
          ).exists(),
          lambda ctx: ChannelPost.create(
            post=Post.get(pid=ctx.params['pid']),
            channel=Channel.get(name=ctx.params['option'])
          ) if not ChannelPost.select().where(
            ChannelPost.post == Post.get(pid=ctx.params['pid']),
            ChannelPost.channel == Channel.get(name=ctx.params['option'])
          ).exists() else ChannelPost.get(
            post=Post.get(pid=ctx.params['pid']),
            channel=Channel.get(name=ctx.params['option'])
          ).delete_instance()
        ) for channel in ctx.user.channels
      }
    ),
    init=texts.posts_view_schedule_channels,
    done=lambda ctx: (
      post := Post.get(pid=ctx.params['pid']),
      post.set('last', datetime.now().timestamp()),
      Redirect.create_back()
    )[-1],
    empty_list=texts.posts_view_schedule_channels_no
  )
)


edit_node = MenuNode(
  init=texts.posts_view_edit,
  back=Redirect.create_back(),
  markup_scheme=(2, 1)
).add_options(
  (
    texts.posts_view_edit_button_caption,
    Redirect.create_go(['caption'])
  ),
  (
    texts.posts_view_edit_button_photo,
    Redirect.create_go(['photo'])
  )
).register_path(
  path='caption',
  func=FormNode(
    final=lambda ctx: (
      Post.get(pid=(pid := ctx.params['pid'])).set('caption', ctx.params['answers'][0]),
      ctx.send_msg(texts.posts_view_edit_caption_edited),
      Redirect.create_to(['/', 'posts', f'view?pid={pid}'])
    )[-1],
    back=lambda ctx: Redirect.create_to(['/', 'posts', f'view?pid=' + str(ctx.params['pid'])])
  ).add_questions(
    (
      texts.posts_create_question_caption,
      lambda ctx: texts.answer_no_more.format(num=256) if len(ctx.text) > 256 else False
    )
  )
).register_path(
  path='photo',
  func=FormNode(
    final=lambda ctx: (
      Post.get(pid=(pid := ctx.params['pid'])).set('file_id', ctx.params['answers'][0]),
      ctx.send_msg(texts.posts_view_edit_photo_edited),
      Redirect.create_to(['/', 'posts', f'view?pid={pid}'])
    )[-1],
    back=lambda ctx: Redirect.create_to(['/', 'posts', f'view?pid=' + str(ctx.params['pid'])])
  ).add_questions(
    (
      texts.posts_create_question_photo,
      lambda ctx: texts.answer_must_image if not 'photo' in ctx.message.content_type else False,
      lambda ctx: ctx.message.photo[0].file_id
    )
  )
)


remove_node = BooleanNode(
  init=texts.posts_view_remove,
  true=lambda ctx: (
    ChannelPost.delete().where(ChannelPost.post.pid == (pid := ctx.params['pid'])),
    Post.delete_by_id(pid),
    ctx.send_msg(texts.posts_view_removed_successful),
    Redirect.create_to(['/'])
  )[-1],
  false=lambda ctx: Redirect.create_back(),
  true_field=texts.posts_view_remove_yes,
  false_field=texts.posts_view_remove_no
)

view_node.register_path(
  path='schedule',
  func=schedule_node
).register_path(
  path='edit',
  func=edit_node
).register_path(
  path='remove',
  func=remove_node
)
