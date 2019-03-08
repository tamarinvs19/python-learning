import smtplib
 
HOST = "mail.yandex.ru"
SUBJECT = "Test email from Python"
TO = "slavabarsuk@ya.ru"
FROM = "slavabarsuk@ya.ru"
text = "Python 3.4 rules them all!"
  
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
))
   
    
server = smtplib.SMTP(HOST)
server.login('slavabarsuk@ya.ru', 'BarsukMail2019')
server.sendmail(FROM, [TO], BODY)
server.quit()
