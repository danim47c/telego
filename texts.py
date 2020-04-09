
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

back = 'אחורה'

done = 'סיום'

okay = 'אוקיי'

true_field = 'כן'
false_field = 'לא'

# Both strings need the same length
emoji_yes = ' - ✅'
emoji_no = ' - ❌'

#? Default Checks

answer_no_more = 'התשובה לא יכולה להכיל יותר מ {num} מילים'
answer_no_less = 'התשובה לא יכולה להכיל פחות מ {num} מילים'

answer_must_text = 'התשובה חייבת לכלול טקסט'
answer_must_image = 'התשובה חייבת להיות תמונה וזה לא תמונה'
answer_must_int = 'התשובה חייבת להיות מספר שלם'
answer_must_int_between = 'התשובה חייבת להיות מספר שלם בין {min} ל {max}'

answer_gt = 'התשובה חייבת להיות גדולה מ {num}'
answer_lt = 'התשובה חייבת להיות נמוכה מ {num}'


#TODO Custom Texts

new_user = 'ברוכים הבאים לבוט הפרסום של טלגו,נא המתן לאישור מנהל!\n-TeleGo-'

admin_new_user = 'משתמש חדש!\n  איידי: {user.uid}\n  יוזר: {user.username}'

admin_new_user_verify = 'אישור'
admin_new_user_block = 'חסימה'

new_user_verified = 'שלום מתפקד יקר,אושרת על ידי מנהל המערכת!'
new_user_blocked = 'שלום משתמש יקר,נחסמת על ידי מנהל המערכת!'

admin_new_user_verified = 'משתמש אושר\n  איידי: {user.uid}\n  יוזר: {user.username}\n\nמנהל: {admin.username}(ID:{admin.uid})'
admin_new_user_blocked = 'משתמש חסום\n  איידי: {user.uid}\n  יוזר: {user.username}\n\nמנהל: {admin.username}(ID:{admin.uid})'

admin_new_user_revise = 'בדוק יוזר'

blocked_user = 'שלום מתפקד יקר,נחסמת על ידי מנהל המערכת!'

non_verified_user = 'אתה צריך להיות סבלני עד שמנהל מאמת אותך'

no_group = 'נא השתמש בבוט הפרסום בלבד בבקשה!'

menu = 'תפריט'

menu_button_posts_list = 'רשימת פרסומים'
menu_button_post_create = 'צור פרסום'
menu_button_admin = 'מנהל מערכת'


post_button = '💎פנה אל הסוחר💎'

posts_list = 'רשימת פרסומים'
posts_list_no_posts = 'לא יצרת פרסום עדין!'


posts_view = 'הצג פרסום'
posts_view_button_send = 'שלח פרסום לערוץ'
posts_view_button_schedule = 'תזמן פרסום'
posts_view_button_edit = 'ערוך'
posts_view_button_remove = 'הסר'
posts_view_button_view = 'הצג'

posts_view_send_choose = 'נא בחר ערוץ כעת לשליחת הפרסום'
posts_view_send = 'הפרסום נשלח בהצלחה! פורסם בערוץ: {channel}'
posts_view_send_time = 'נא המתן {x} דקות , על מנת לפרסם שוב בערוץ זה!'

posts_view_schedule = 'תוזמן: {scheduled}\n   מרווח זמן: {interval}\n  ערוצים: {channels}'
posts_view_scheduled_yes = 'כן'
posts_view_scheduled_no = 'לא'
posts_view_scheduled_no_channels = '-'
posts_view_schedule_button_toggle = 'החלף'
posts_view_schedule_button_interval = 'מרווח זמן'
posts_view_schedule_interval = 'בחר את המרווח שבחרת, לחץ על הכפתורים האלה או שלח לי את התוספת (+X)או החיסור (-X)'
posts_view_schedule_interval_more = 'המרווח צריך להיות גבוה מ- 60 דקות'
posts_view_schedule_button_channels = 'ערוצים'
posts_view_schedule_channels = 'בחר ערוצים שאתה רוצה שהפרסום יישלח אליהם'
posts_view_schedule_channels_no = 'אין ערוצים לשליחה'

posts_view_edit = 'ערוך פוסט'
posts_view_edit_button_caption = 'ערוך את הכיתוב'
posts_view_edit_caption_edited = 'הכיתוב נערך בהצלחה'
posts_view_edit_button_photo = 'ערוך תמונה'
posts_view_edit_photo_edited = 'התמונה נערכה בהצלחה'

posts_view_remove = 'אתה בטוח שאתה רוצה להסיר את הפרסום?'
posts_view_remove_yes = 'כן'
posts_view_remove_no = 'לא'
posts_view_removed_successful = 'הפרסם הוסר בהצלחה'


posts_create = 'כדי ליצור פרסום תצטרך לענות לי על השאלות הבאות'
posts_create_question_name = 'שלח לי את השם שאתה רוצה לפוסט, זה ישמש לי רק כדי לארגן את הפרסומים שלך'
posts_create_question_name_taken = 'יש לך כבר פרסום בשם הזה'
posts_create_question_caption = 'שלח את הכיתוב של הפרסום בבקשה'
posts_create_question_photo = 'שלח לי תמונה לפרסום בבקשה'
posts_create_successful = 'הפרסום נוצר בהצלחה!'



admin_message = 'תפריט מנהל'
admin_button_users = 'משתמשים'
admin_button_channels = 'ערוצים'


admin_users = 'משתמשים'
admin_users_button_search = 'חיפוש'
admin_users_button_broadcast = 'שידור כללי בבוט'

admin_users_search = 'כדי לחפש משתמש אתה צריך לשלוח לי חלק מהאיידי או שם המשתמש(יוזר) שלו'
admin_users_search_user = '@{user.username}(ID:{user.uid})'
admin_users_search_select = 'בחר'
admin_users_search_done = 'הנה התוצאות שנמצאו'
admin_users_search_more = 'ישנם יותר מ 15 משתמשים התואמים לחיפוש הזה, ציין יותר פרטים'
admin_users_search_no = 'לא נמצאו תוצאות'

admin_users_broadcast = 'כל הודעה תישלח לכל המשתמשים, לביטול, לחץ על בוצע'
admin_users_broadcast_done = 'ההודעה נשלחה בהצלחה {num} קיבלו אותה'

admin_users_view = '@{user.username}(ID:{user.uid})\n  חסומים: {user.blocked}\n  מנהל: {user.admin}'
admin_users_view_button_manage = 'נהל ערוצים'
admin_users_view_button_block = 'חסום'
admin_users_view_button_unblock = 'בטל את החסימה'
admin_users_view_button_make = 'הפוך למנהל מערכת'
admin_users_view_button_remove = 'הסר מנהל מערכת'
admin_users_view_block = 'בטוח שאתה רוצה {block} @{user.username}(ID:{user.uid})?'
admin_users_view_make = 'בטוח שאתה רוצה {make} @{user.username}(ID:{user.uid}) admin?'
admin_users_view_manage = 'בחר ערוצי פרסום למשתמש זה'
admin_users_view_manage_empty = 'אין ערוצים שהתווספו'

admin_channels = '{num} ערוצים'
admin_channels_button_list = 'רשימת ערוצים'
admin_channels_button_add = 'הוסף ערוץ'

admin_channels_add = 'הוסף ערוץ'
admin_channels_add_button_group = 'קבוצה'
admin_channels_add_button_channel = 'ערוץ'
admin_channels_add_group = 'כדי להוסיף את הבוט הזה לקבוצה אתה צריך לעבור רק על הקישור הבא'
admin_channels_add_group_link = 'המשך'
admin_channels_add_group_success = 'הקבוצה התווספה בהצלחה'
admin_channels_add_channel_public = 'ראשית, עליכם להפוך את הערוץ לציבורי להוסיף אותי (@ {me.username}) כמנהל עם הרשאת שליחת הודעה'
admin_channels_add_channel_id = 'שנית, אתה צריך לשלוח לי את מזהה הערוץ. למשל: @ טלגרם'
admin_channels_add_channel_id_error = 'המזהה חייב להתחיל ב @'
admin_channels_add_channel_test = 'לסיום תצטרך לבדוק אם הבוט יכול לשלוח הודעה, לחץ על בדיקה'
admin_channels_add_channel_test_message = 'שלום,זה בדיקה'
admin_channels_add_channel_test_button = 'בדיקה'
admin_channels_add_channel_test_error = 'אירעה שגיאה במהלך שליחת ההודעה, שנה את הכל. התהליך יופעל מחדש תוך 3 שניות'
admin_channels_add_channel_success = 'הערוץ התווסף בהצלחה'

admin_channels_view = 'ערוץ:\n  מנהל: {admin.username}(איידי:{admin.uid})\n  איידי ערוץ: {channel.cid}\n  שם הערוץ: {channel.name}'
admin_channels_view_button_remove = 'הסר'
admin_channels_view_remove = 'האם אתה בטוח שברצונך להסיר את הערוץ הזה?'

admin_channels_list = 'רשימת ערוצים'
admin_channels_list_empty = 'לא נוספו ערוצים'