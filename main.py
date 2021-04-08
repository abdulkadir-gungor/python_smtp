############################################################################
#
#   SMTP Email Example "main.py"
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################

from SMTP_Email import SMTP_Email, Add_File

# (1)
smtp_addr = 'smtp.gmail.com'            # gmail smtp
port = 587                              # gmail smtp port
sender = 'sender_test_gungor@gmail.com' # gmail e-mail address
password = 'q123aBc456z'                # gmail e-mail password

# (2)
mail_to = 'receiver_test_gungor@outlook.com' # receiver e-mail address
mail_subject = 'Python Test E-mail'
mail_body = ''' Hi Test,
Python test 1
Python test 2
Python test 4
Python test 5
Hello Python
'''

# (3)
filename = 'sibervatan.jpg'
filename_path = 'sibervatan.jpg'

# (4)
# "Add_File" class example
file = Add_File(name=filename, filefullpath=filename_path)
file.jpg()

# (5)
# "SMTP_Email" class example
email = SMTP_Email(smtp=smtp_addr, smtp_port=port, sender=sender, password=password)
email.message_body(mail_to=mail_to, mail_subject=mail_subject, mail_content=mail_body)
email.message_add_file(file=file)
email.message_send()
