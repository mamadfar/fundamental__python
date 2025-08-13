
# ? Mime (Multipurpose Internet Mail Extensions)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template
from env_loader import load_env

# * Load environment variables from .env file
env_vars = load_env()

message = MIMEMultipart()
message['from'] = 'Mohammad Farhadi'
message['to'] = 'm.sabah.farhadi@gmail.com'
message['subject'] = 'Hello from Mohammad Farhadi'

# * Create the image attachment
root = Path(__file__).parent.parent.parent
image_path = Path(root, 'assets', 'img', 'mohammad.jpeg')
with open(image_path, 'rb') as f:
    image_data = f.read()

image_attachment = MIMEImage(image_data)
image_attachment.add_header('Content-ID', '<mohammad.jpeg>')
# image_attachment.add_header('Content-Disposition',
#                             'inline', filename='mohammad.jpeg')
message.attach(image_attachment)
# * Hardcoded HTML version
# message.attach(MIMEText(
#     '<h1>Hello from Mohammad Farhadi</h1>'
#     '<p>This is a test email sent using Python.</p>'
#     '<img src="cid:mohammad.jpeg" alt="Mohammad Farhadi" width="200" height="200">', 'html'))

root = Path(__file__).parent
template = Template(Path(root, 'template.html').read_text())

# * Way 1
body = template.substitute({
    'user_name': 'John Doe'
})

# * Way 2
# body = template.substitute(user_name='John Doe')
message.attach(MIMEText(body, 'html'))


with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as smtp:
    smtp.ehlo()
    smtp.starttls()  # ? TLS (Transport Layer Security)
    smtp.login(env_vars.get('EMAIL_USER'), env_vars.get('EMAIL_PASS'))
    smtp.send_message(message)
    print('Email sent successfully!')
