import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # You can use any SMTP server
SMTP_PORT = 587  # For TLS
SENDER_EMAIL = "roo@k8sm.svkp.lab"  # Sender's email address
SENDER_PASSWORD = "your_password"  # Sender's email password (consider using App Passwords if using Gmail)
RECIPIENT_EMAIL = "shanvikasvp@gmail.com"  # Recipient's email address
SUBJECT = "System Resource Alert - Utilization Exceeded Threshold"

# Function to send email alert
def send_email(body):
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = SUBJECT

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to check system utilization
def check_system_utilization():
    # Get system utilization data
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage in percentage
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_usage('/')

    # Prepare an alert message if utilization exceeds 90%
    alert_message = ""

    # Check CPU utilization
    if cpu_usage > 90:
        alert_message += f"CPU Usage is critically high: {cpu_usage}%\n"

    # Check memory utilization
    if memory.percent > 90:
        alert_message += f"Memory Usage is critically high: {memory.percent}%\n"

    # Check swap utilization
    if swap.percent > 90:
        alert_message += f"Swap Usage is critically high: {swap.percent}%\n"

    # Check filesystem utilization
    if disk.percent > 90:
        alert_message += f"Filesystem Usage is critically high: {disk.percent}%\n"

    # If any resource usage exceeds the threshold, send an email alert
    if alert_message:
        # Add system information to the message
        alert_message = f"ALERT: High resource usage detected on {socket.gethostname()}:\n\n" + alert_message
        send_email(alert_message)

# Main function to continuously monitor
def monitor():
    check_system_utilization()

# Run the monitor function (You can set this to run periodically via cron or other schedulers)
if __name__ == "__main__":
    monitor()