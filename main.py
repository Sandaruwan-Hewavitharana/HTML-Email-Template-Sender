import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# Start TLS for security
s.starttls()
# Authentication
s.login("SENDER EMAIL", "SENDER PASSWORD")

# Create a MIMEMultipart message object
message = MIMEMultipart("alternative")  # Corrected "alternatives" to "alternative"
message['Subject'] = "Robotic Exibition"
message['From'] = 'SENDER EMAIL'
message['To'] = 'RECEIVER EMAIL'

# Email body in plain text and HTML
text = "Welcome to Future .."
html = """
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Robotic Exhibition Invitation</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

        body {
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            font-family: "Poppins", sans-serif;
            font-weight: 200;
            font-style: normal;
        }

        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #191919;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .header {
            background-image: url("https://yoast.com/app/uploads/2008/01/Robots_FI.png"); /* Replace with your image URL */
            background-size: cover;
            background-position: center;
            position: relative;
            padding: 20px;
            text-align: center;
            color: rgb(255, 255, 255);
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }

        .header h1 {
            margin: 0;
            font-size: 24px;
            background-color: rgba(0, 0, 0, 0.5);
            display: inline-block;
            padding: 10px 20px;
            border-radius: 4px;
        }

        .content {
            padding: 20px;
            color: #b2b2b2;
            line-height: 1.6;
            font-weight: 300;
        }

        .content h2 {
            color: #dddddd;
        }

        .content p {
            margin: 10px 0;
        }

        .content a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ff5100;
            color: #ffffff;
            text-decoration: none;
            border-radius: 4px;
            margin-top: 20px;
        }

        .content a:hover {
            background-color: rgba(255, 68, 0, 0.833);
        }

        .footer {
            background-color: #2b2b2b;
            padding: 10px;
            text-align: center;
            font-size: 12px;
            color: #888888;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        }

        .footer a {
            color: #ff5100;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="email-container">
        <div class="header">
            <h1>Join Us for the Robotic Exhibition 2024!</h1>
        </div>
        <div class="content">
            <h2>Dear Robotics Enthusiast,</h2>
            <p>We are thrilled to invite you to the Robotic Exhibition 2024, where innovation meets technology! Explore the latest advancements in robotics, interact with cutting-edge machines, and network with industry leaders.</p>
            <p><strong>Date:</strong> October 15, 2024<br>
                <strong>Time:</strong> 10:00 AM - 6:00 PM<br>
                <strong>Location:</strong> Tech Convention Center, San Francisco, CA</p>
            <p>Don't miss this opportunity to witness the future of robotics. Reserve your spot today!</p>
            <center><a href="#">RSVP Now</a></center>
        </div>
        <div class="footer">
            <p>For more information, visit our <a href="#">website</a> or contact us at <a href="mailto:info@roboticexhibition.com">info@roboticexhibition.com</a></p>
            <p>&copy; 2024 Robotic Exhibition. All rights reserved.</p>
        </div>
    </div>
</body>

</html>

"""

# Attach the plain text and HTML parts
textPart = MIMEText(text, 'plain')
htmlPart = MIMEText(html, 'html')  # Corrected MIMEMultipart to MIMEText

# Attach both parts to the message
message.attach(textPart)
message.attach(htmlPart)

# Sending the email
s.sendmail("SENDER EMAIL", "RECEIVER EMAIL", message.as_string())

# Terminating the session
s.quit()
