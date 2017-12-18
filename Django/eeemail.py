#-*-coding:utf-8-*-
# import smtplib
 
# #你要寫的內容

# info = '管理者 您好：\n企業求才網站，已於%s新增一筆企業審核申請，請至網站審核。\n'%'20171012'
# info += '企業名稱:%s 統一編號: %s\n經濟部─公司及分公司基本資料查詢:http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do'%('123','345')
 
# #寄件人的信箱，通常自己去申請個GMAIL信箱即可
# gmail_user = 'theedward481@gmail.com'
# gmail_pwd = 'cilxchuxfyrwpmoc'
# #這是GMAIL的SMTP伺服器，如果你有找到別的可以用的也可以換掉
# smtpserver = smtplib.SMTP("smtp.gmail.com",587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo()
# #登入系統
# # smtpserver.login(gmail_user, gmail_pwd)
 
# #寄件人資訊
# fromaddr = "theedward481@gmail.com"
# #收件人列表，格式為list即可
# toaddrs = "theedward285@gmail.com"
 
# #設定寄件資訊
# msg = ("From: %sTo: %sSubject: %s" % (fromaddr, toaddrs,'hello'))
# message = 'Subject: {}\n\n{}'.format('test', info)
# smtpserver.sendmail(fromaddr, toaddrs, message.encode("utf8"))
 
# #記得要登出
# smtpserver.quit()

import smtplib
from email.mime.text import MIMEText

info = '%s(企業) 您好  貴公司申請使用本組求才訊息網站已開通權限，提醒您至求才網站刊登職缺，謝謝。\n'%'20171012'
info += '成功大學企業求才網: http://career.osa.ncku.edu.tw/career/Login/\n順頌商祺\n成功大學生涯發展與就業輔導組'
msg = MIMEText(info)
msg["From"] = "z10410059@email.ncku.edu.tw"
msg["To"] = "theedward285@gmail.com"
msg["Subject"] = "企業審核通知"

server = smtplib.SMTP("email.ncku.edu.tw",25)
server.starttls()
server.ehlo_or_helo_if_needed()
try:
    failed = server.sendmail("z10410059@email.ncku.edu.tw","theedward285@gmail.com", msg.as_string())
    server.close()
except Exception as e:
    print(e)