pip install psutil pandas openpyxl smtplib

import psutil
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to gather system health information
def gather_health_info():
    health_info = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Number of Processes": len(psutil.pids()),
        "Uptime (seconds)": int(psutil.boot_time())
    }
    return health_info

# Function to write data to an Excel file
def write_to_excel(data, filename='server_health_check.xlsx'):
    df = pd.DataFrame([data])
    df.to_excel(filename, index=False)

# Function to send an email with the Excel file as attachment
def send_email(subject, body, to_email, filename, from_email, from_email_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file as binary
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(filename)}",
    )

    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)

    # Create SMTP session for sending the mail
    server = smtplib.SMTP('smtp.gmail.com', 587) # Use your SMTP server
    server.starttls()
    server.login(from_email, from_email_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Main function to perform health check and send email
def main():
    # Gather health check data
    health_data = gather_health_info()
    
    # Define the filename for the Excel file
    excel_filename = 'server_health_check.xlsx'
    
    # Write data to Excel file
    write_to_excel(health_data, excel_filename)
    
    # Email details
    subject = "Linux Server Health Check Report"
    body = "Please find the attached health check report."
    to_email = "svkumarpal@gmail.com"
    host="hostname -f"
    from_email = "root@host"
    from_email_password = "your_email_password"
    
    # Send the email with the attached Excel file
    send_email(subject, body, to_email, excel_filename, from_email, from_email_password)

if __name__ == "__main__":
    main()