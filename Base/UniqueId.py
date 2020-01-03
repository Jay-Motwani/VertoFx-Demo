import re
import random
from datetime import date

today = date.today()
dt = today.strftime("%d%m")
count = 0
last_email = "vfx2212@mailinator.com"
last_search = re.search(r'vfx(\d*)@.*', last_email).group(1)
print(last_search)
if len(last_search) == 4:
    if last_search == dt:
        new_dt = dt + str(count)
        email_id = "vfx" + new_dt + "@mailinator.com"
        phone = new_dt + new_dt
    else:
        email_id = "vfx" + dt + "@mailinator.com"
        phone = dt + "33" + dt
else:
    count = re.search(r'([\d]{4})(\d*)', last_search).group(2)
    email_id = "vfx" + str(int(count) + 1) + "@mailinator.com"
    phone = re.search(r'([\d]{10})(\d*)', (count + count)).group(1)

class uniqueDetails:
    def __init__(self):
        nameList1 = ["John", "David", "James", "Brandon", "Anthony"]
        nameList2 = ["Tessier", "Thompson", "Fahie", "Bartlett", "Little"]
        firstName = random.choice(nameList1)
        lastName = random.choice(nameList2)
