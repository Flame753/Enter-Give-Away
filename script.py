from geninfo import get_website_info
import accounts
from socialmedia import create_gmail

database = accounts.Accounts()
database.display_all()
for amount in range(int(input())):
    person_info = get_website_info()
    database.add_account(person_info)

database.display_all()
