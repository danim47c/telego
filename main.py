
from telef.shortcuts import *


tf = TeleFramework(content_types=['text', 'photo'])

tf.add_modules('bot.root')

from bot.menu import menu_node

tf.register_path(
  path='/',
  func=menu_node
)

tf.register_command(
  command=f'/start@{tf.bot.get_me().username} group',
  func=lambda ctx: Redirect.create_to(['/', 'admin', 'channels', 'add', 'group'])
)

tf.start()