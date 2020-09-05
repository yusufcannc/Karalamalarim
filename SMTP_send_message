"SMTP modülü ile mail gönderme"

import smtplib
from email.mime.multipart import MIMEMultipart #Mesajımızın yapısını oluşturacak.
from email.mime.text import MIMEText  #Mesajımızın gövdesini oluşturuyor.



mesaj = MIMEMultipart()

mesaj["From"] = "yusufcancakir213@gmail.com"

mesaj["To"] = "yusufcancakir@yaani.com"

mesaj["Subject"] = "SMTP Mail Gönderme"

mail = """

SMTP ile mail gönderiyorum.

Yusuf Can Çakır

"""

mesaj_govdesi = MIMEText(mail,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587) #smtp.gmail.com'a bağlanacağımızı belirttik. İkinci değer ile de portu belirttik.
    mail.ehlo() #SMTP serverına bağlanmak için kullanıyoruz.
    mail.starttls() #Girdiğimiz verilerin şifrelenmesi için bunu kullanıyoruz.
    mail.login("yusufcancakir213@gmail.com","password") #smtp serverına artık giriyoruz.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string()) #Maili gönderiyoruz.
    #as_string ile direk yapıyı string'e çeviriyoruz.

    print("Mail başarılı bir şekilde gönderilmiştir.")
    mail.close()

except:
    print("Mail başarı bir şekilde gönderilemedi.")




