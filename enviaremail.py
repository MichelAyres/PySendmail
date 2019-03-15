import smtplib
import os

from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configura o servidor de envio (SMTP)
server = smtplib.SMTP('<your mail server>')
# # begin if you need authentication
# smtp_port = <port number>
# acc_addr = '<your email>'
# acc_pwd = '<your password>'
# # end if you need authentication

pdfFolder = 'pdfs'
for file in os.listdir(pdfFolder): # your folder (path + folder) with yours pdf file
	if file.endswith(".pdf"):
		body = 'Your body mail text. Add something'
		msg = MIMEMultipart()
		msg["Subject"] = '<your subject>'
		attachment_path = os.path.join(pdfFolder, file)
		fp = open(attachment_path,'rb')
		x = fp.read()
		fp.close()
		anexo = MIMEBase('application','pdf')
		anexo.set_payload(x)
		encode_base64(anexo)
		anexo.add_header('Content-Disposition','attachment;filename=YourFileName.pdf')
		msg.attach(anexo)

		# Add to the mail body your text
		msg.attach(MIMEText('<b>{}</b><br>'.format(body), 'html'))

		acc_addr = '<sender email>'
		to_addr = '<receiver email>'
		msg["From"] = acc_addr
		msg["To"] = to_addr

		# Send!
		server.sendmail(acc_addr, to_addr, msg.as_string())
		print('Email was sent with success')
server.quit()