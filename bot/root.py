
from telef.shortcuts import *

from bot.new_users import *

from bot.posts.view import send_post_raw

root_node = Node()

@root_node.func_decorator()
@root_node.init_func_decorator()
def root_func(ctx: BaseContext):
  if ctx.user.blocked:
    return ctx.send_msg(texts.blocked_user, clear_markup=True)
  elif not ctx.user.registered:
    ctx.user.set('registered', True)
    ctx.send_msg(texts.new_user, clear_markup=True)
    return new_user_message(ctx)
  elif not ctx.user.verified:
    return ctx.send_msg(texts.non_verified_user, clear_markup=True)
  else:
    return Redirect.create_to(['/'])


def verify_command(ctx: BaseContext):
  if not ctx.user.admin: return

  user = User.get(uid=ctx.params['uid'])
  
  if user.verified or user.blocked: return

  user.set('verified', True).set('blocked', False)
  
  ctx.bot.send_message(chat_id=user.uid, text=texts.new_user_verified, reply_markup=teletypes.ReplyKeyboardMarkup().row(teletypes.KeyboardButton(texts.okay)))

  return new_user_update(
    ctx=ctx,
    user=user,
    verified=True
  )

def block_command(ctx: BaseContext):
  if not ctx.user.admin: return

  user = User.get(uid=ctx.params['uid'])
  
  if user.verified: return

  user.set('verified', True).set('blocked', True)

  ctx.bot.send_message(chat_id=user.uid, text=texts.new_user_blocked, reply_markup=teletypes.ReplyKeyboardRemove())

  return new_user_update(
    ctx=ctx,
    user=user,
    verified=False
  )


def setup(tf: TeleFramework):

  tf.register_path(
    path='',
    func=root_node
  )

  tf.register_command(
    command='/verify',
    func=verify_command
  ).register_command(
    command='/block',
    func=block_command
  )

  tf.register_spyder(
    func=lambda ctx: Redirect.create_to(['']) if ctx.user.blocked else False,
    paths=['/']
  ).register_spyder(
    func=lambda ctx: ctx.send_msg(texts.no_group, clear_markup=True) if ctx.message.chat.type != 'private' else False
  )

  @tf.timeloop.job(interval=timedelta(seconds=60))
  def post_job():

    for post in Post.select().where(Post.scheduled):

      if (datetime.now() - datetime.fromtimestamp(post.last)).seconds / 60 >= post.interval:

        for channel in post.channels:

          channel = channel.channel

          send_post_raw(
            bot=tf.bot,
            chat_id=channel.channel_id if channel.channel else channel.group_id,
            post=post
          )

        post.set('last', datetime.now().timestamp())
