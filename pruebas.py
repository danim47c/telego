
from telef.shortcuts import *


ChannelPost.delete().where(ChannelPost.channel.cid == 2)