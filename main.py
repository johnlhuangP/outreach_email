import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Template

def read_template(template_path):
    with open(template_path, 'r') as file:
        template_content = file.read()
    return Template(template_content)

def generate_email_content(template, data):
    return template.render(data)

def send_email(subject, body, to_email,cc_emails, gif_path, pdf_path):
    from_email = 'team@letsift.com'  # Replace with your email
    password = 'dfiy mdat mxmb bfxz'  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg['Cc'] = ', '.join(cc_emails)

    msg.attach(MIMEText(body, 'html'))

    # Attach the GIF as an embedded image
    with open(gif_path, 'rb') as gif_file:
        gif = MIMEImage(gif_file.read(), name='gif2.gif')
        gif.add_header('Content-ID', '<gif2.gif>')
        gif.add_header('Content-Disposition', 'inline', filename='gif2.gif')
        msg.attach(gif)

    with open(pdf_path, 'rb') as pdf_file:
        pdf_attachment = MIMEBase('application', 'pdf')
        pdf_attachment.set_payload(pdf_file.read())
        encoders.encode_base64(pdf_attachment)
        pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_path}')

        msg.attach(pdf_attachment)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, [to_email] + cc_emails, msg.as_string())

def main():
    template_path = 'email_template.txt'
    template = read_template(template_path)

    with open('email_data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            email_content = generate_email_content(template, row)
            subject = "Join Sift's Sustainable Fashion Movement: Empower Secondhand Shopping"

            pdf_attachment_path = 'Sift.pdf'
            gif_attachment_path = 'gif2.gif'

            
            # Assuming 'to_email' is one of the columns in your CSV
            to_email = row.get('email', 'recipient@example.com')
            cc_emails = ['taorong_lian@brown.edu', 'david@letsift.com']

            send_email(subject, email_content, to_email,cc_emails,gif_attachment_path, pdf_attachment_path)

if __name__ == "__main__":
    main()


