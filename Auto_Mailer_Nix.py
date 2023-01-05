#Nemo-07
#Auto mail

from redmail import outlook

file1 = open('filename.txt', 'r') #read txt file containing reciever emails
emails = file1.readlines() 
mail_list = [item.strip() for mail in emails] #list of recepients

print(mail_list)

outlook.username = "YourUsername@mail.com"
outlook.password = "YourPassword"
                   
outlook.send(
    receivers=mail_list,
    subject="Your Subject",
    text="Salutations!\n\nContent\n\nRegards.",
    html="<font face='Times New Roman'><p>Salutations!<br><br>Content<br><br>Regards.</p></font>"
)

#Do add needed HTML tags and indentations, along with inline CSS

print('Sent Mails!') #conformation
