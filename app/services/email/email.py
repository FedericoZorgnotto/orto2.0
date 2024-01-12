import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def invia_mail(self,destinatario, oggetto, corpo):

        messaggio = MIMEMultipart()
        messaggio['From'] = self.smtp_username
        messaggio['To'] = destinatario
        messaggio['Subject'] = oggetto

        messaggio.attach(MIMEText(corpo, 'html'))


        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.smtp_username, destinatario, messaggio.as_string())

        except Exception as e:
            print("Errore durante l'invio della mail: ", e)
            raise Exception(e)