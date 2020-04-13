
from telef.shortcuts import *

from base64 import b64encode, b64decode

def final_func(ctx: BaseContext):
  post = Post.create(author=ctx.user, name=ctx.params['answers'][0], caption=ctx.params['answers'][1], file_id=ctx.params['answers'][2])

  ctx.send_msg(texts.posts_create_successful)

  return Redirect.create_move([f'view?pid={post.pid}'])

create_node = FormNode(
  final=final_func,
  init=texts.posts_create,
  back=Redirect.create_to(['/'])
).add_questions(
  (
    texts.posts_create_question_name,
    lambda ctx: texts.posts_create_question_name_taken if Post.select().where(Post.name == ctx.text).exists() else texts.answer_no_more.format(num=256) if len(ctx.text) > 256 else False,
    lambda ctx: b64encode(ctx.text.encode())
  ),
  (
    texts.posts_create_question_caption,
    lambda ctx: texts.answer_no_more.format(num=256) if len(ctx.text) > 256 else False,
    lambda ctx: b64encode(ctx.text.encode())
  ),
  (
    texts.posts_create_question_photo,
    lambda ctx: texts.answer_must_image if not 'photo' in ctx.message.content_type else False,
    lambda ctx: ctx.message.photo[0].file_id
  )
)
