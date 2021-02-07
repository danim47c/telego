
#TODO Config Texts

#? Logging messages

logging_configure = 'Bot initializing'

logging_start = 'Bot started successfully [{seconds} seconds initializing]'

logging_stop = 'Bot stopped successfully [{hours} hours running]'

logging_critical_error = 'Critical error while running bot'

logging_command_not_found = 'I couldn\'t find "{command}" executed by @{user}(ID:{user_id})'

logging_unreachable_path = '@{user}(ID:{user_id}) was in an unreachable path [Path: {path} | Point: \'{point}\']'
logging_unreachable_path_redirected = '@{user}(ID:{user_id}) was redirected to an unreachable path [Path: {path} | Point: \'{point}\']'

logging_no_setup_function = 'All modules need a setup function [Module: {module}]'

logging_questionid_not_found = 'I could\'t find {qid} in {path} '

#? Buttons

back = 'Back'

done = 'Done'

okay = 'Okay'

true_field = 'Yes'
false_field = 'No'

# Both strings need the same length
emoji_yes = ' - ✅'
emoji_no = ' - ❌'

#? Default Checks

answer_no_more = 'The answer can\'t contain more than {num} characters'
answer_no_less = 'The answer can\'t contain less than {num} characters'

answer_must_text = 'The answer must contain a text'
answer_must_image = 'The answer must be a photo and that\'s not'
answer_must_int = 'The answer must be a integer'
answer_must_int_between = 'The answer must be a integer between {min} and {max}'

answer_gt = 'The answer must be greater than {num}'
answer_lt = 'The answer must be lower than {num}'


#TODO Custom Texts

new_user = 'Welcome to the bot, you have to wait until an admin verifies you'

admin_new_user = 'New User\n  ID: {user.uid}\n  Username: {user.username}'

admin_new_user_verify = 'Verify'
admin_new_user_block = 'Block'

new_user_verified = 'Hello, you have been verified'
new_user_blocked = 'Hello, you have been blocked'

admin_new_user_verified = 'User Verified\n  ID: {user.uid}\n  Username: {user.username}\n\nAdmin: {admin.username}(ID:{admin.uid})'
admin_new_user_blocked = 'User Blocked\n  ID: {user.uid}\n  Username: {user.username}\n\nAdmin: {admin.username}(ID:{admin.uid})'

admin_new_user_revise = 'Check User'

blocked_user = 'You have been blocked by an admin'

non_verified_user = 'You have to be patient until an admin verifies you'


menu = 'Menu'
no_group = "No group"

menu_button_posts_list = 'Posts List'
menu_button_post_create = 'Create Post'
menu_button_admin = 'Admin'


post_button = '@{author.username}'

posts_list = 'Posts List'
posts_list_no_posts = 'You haven\'t created any post yet'


posts_view = 'Viewing Post'
posts_view_button_schedule = 'Schedule'
posts_view_button_edit = 'Edit'
posts_view_button_remove = 'Remove'
posts_view_button_view = 'View'
posts_view_button_send = "Send"
posts_view_send_choose = "Send"

posts_view_schedule = 'Scheduled: {scheduled}\n   Interval: {interval}\n  Channels: {channels}'
posts_view_scheduled_yes = 'Yes'
posts_view_scheduled_no = 'No'
posts_view_scheduled_no_channels = '-'
posts_view_schedule_button_toggle = 'Toggle'
posts_view_schedule_button_interval = 'Interval'
posts_view_schedule_interval = 'Choose the interval of your choice, pressing those buttons or sending me the addition (+X) or the subtraction (-X)'
posts_view_schedule_interval_more = 'The interval should be higher than 20 minutes'
posts_view_schedule_button_channels = 'Channels'
posts_view_schedule_channels = 'Choose the channels you want the post to be sent'
posts_view_schedule_channels_no = 'The are no channels to send'

posts_view_edit = 'Edit Post'
posts_view_edit_button_caption = 'Edit Caption'
posts_view_edit_caption_edited = 'Caption edited successfully'
posts_view_edit_button_photo = 'Edit Photo'
posts_view_edit_photo_edited = 'Photo edited successfully'

posts_view_remove = 'Are you sure you want to remove this post?'
posts_view_remove_yes = 'Yes'
posts_view_remove_no = 'No'
posts_view_removed_successful = 'Post removed successfully'


posts_create = 'To create a post you\'ll have to answer me the following questions'
posts_create_question_name = 'Send me the name you want for the post, it will be only use for me to organise your posts'
posts_create_question_name_taken = 'You have got already a post with that name'
posts_create_question_caption = 'Send me the caption of the post'
posts_create_question_photo = 'Send me the photo of the post'
posts_create_successful = 'Post created successfully'



admin_message = 'Admin Menu'
admin_button_users = 'Users'
admin_button_channels = 'Channels'


admin_users = 'Users'
admin_users_button_search = 'Search'
admin_users_button_broadcast = 'Broadcast'

admin_users_search = 'For searching a user you have to send me part of it\'s id or username'
admin_users_search_user = '@{user.username}(ID:{user.uid})'
admin_users_search_select = 'Select'
admin_users_search_done = 'Here are the results'
admin_users_search_more = 'There are more than 15 users matching with that query, specify more'
admin_users_search_no = 'There are no results with that query'

admin_users_broadcast = 'Every message will be sent to all the users, to cancel, press Done'
admin_users_broadcast_done = 'Message sent successfully to {num} users'

admin_users_view = '@{user.username}(ID:{user.uid})\n  Blocked: {user.blocked}\n  Admin: {user.admin}'
admin_users_view_button_manage = 'Manage Channels'
admin_users_view_button_block = 'Block'
admin_users_view_button_unblock = 'Unblock'
admin_users_view_button_make = 'Make Admin'
admin_users_view_button_remove = 'Remove Admin'
admin_users_view_block = 'Are you sure you want to {block} @{user.username}(ID:{user.uid})?'
admin_users_view_make = 'Are you sure you want to {make} @{user.username}(ID:{user.uid}) admin?'
admin_users_view_manage = 'Select the channels where this user is allowed to send posts'
admin_users_view_manage_empty = 'There are no channels added'

admin_channels = '{num} Channels'
admin_channels_button_list = 'Channels List'
admin_channels_button_add = 'Add Channel'

admin_channels_add = 'Add Channel'
admin_channels_add_button_group = 'Group'
admin_channels_add_button_channel = 'Channel'
admin_channels_add_group = 'To add this bot to a group you only have to go through the following link'
admin_channels_add_group_link = 'Go'
admin_channels_add_group_success = 'Group added successfully'
admin_channels_add_channel_public = 'First, you have to make the channel public add me (@{me.username}) as an admin with send message\'s privilege'
admin_channels_add_channel_id = 'Second, you have to send me the channel identifier. Eg: @telegram'
admin_channels_add_channel_id_error = 'It has to start with a @'
admin_channels_add_channel_test = 'To finish, youll have to test if the bot can send a message, press Test'
admin_channels_add_channel_test_message = 'Hello, this is the test'
admin_channels_add_channel_test_button = 'Test'
admin_channels_add_channel_test_error = 'There was an error while sending the message, revise everything.\n The process will restart in 3 seconds'
admin_channels_add_channel_success = 'You success adding the channel'

admin_channels_view = 'Channel:\n  Admin: {admin.username}(ID:{admin.uid})\n  Channel ID: {channel.cid}\n  Name: {channel.name}'
admin_channels_view_button_remove = 'Remove'
admin_channels_view_remove = 'Are you sure you want to remove this channel?'

admin_channels_list = 'Channels List'
admin_channels_list_empty = 'There are no channels added'