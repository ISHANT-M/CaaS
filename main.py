from src.fetch import get_html
from src.parse import make_sense
from src.check import check
from src.notify import send_telegram_msg

print("----------START----------")

html = get_html()
msg = make_sense(html)
for i in range(0, msg[0]):
   print(msg[1][i])

ans = check(msg)
if ans:
   print("notifying!!!")
   send_telegram_msg(msg)



print("-----------END-----------")