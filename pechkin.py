from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header

SMTPHOST = "smtp.mail.ru"
SUBJECT = "Проверочная почта, проверочная почта"
TOTO = "max-melifaro@ya.ru"
FROM = "malepushka@mail.ru"
pismo = "Русские буквыыыыыыыыыыы"
username = FROM
passmail = "******"

def esend():
    TOTO = pole1.get()
    SUBJECT = pole2.get()
    pismo = text.get('1.0', END)
    msg = MIMEText( pismo, 'plain', 'utf-8')
    msg['Subject'] = Header( SUBJECT, 'utf-8')
    msg['From'] = FROM
    msg['To'] = TOTO

    smtpserver = smtplib.SMTP_SSL(SMTPHOST, 465)
    smtpserver.login(username, passmail)
    print(msg.as_string())
    smtpserver.sendmail(FROM, [TOTO], msg.as_string())
    smtpserver.quit()

root = Tk()
root.title("Почтальон Печкин")
# Вставить бы в поле text "Письмо отправлено программой "Почтальон Печкин", которую написал я."
text = Text(width=40, height=18, font="Arial 14")
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

l1 = Label(text="Куда: ", font="Arial 14")
l2 = Label(text="Тема: ", font="Arial 14")
pole1 = Entry(width=24, font="Arial 14")
pole2 = Entry(width=24, font="Arial 14")
pole2.insert(0, "Это я, почтальон Печкин")
ButtonSend = Button(text="Отправить", width=12, height=2, font="Arial 14", command=esend)

l1.pack()
pole1.pack()
l2.pack()
pole2.pack()
ButtonSend.pack()

root.mainloop()
