from email.message import EmailMessage
import ssl
import smtplib
import random
from dotenv import load_dotenv
import os

random_quotes = {
    "Batman Begins":"Why do we fall sir? So that we can learn to pick ourselves up.",
    "The Big Short":"People want an authority to tell them how to value things, but they choose this authority not based on facts or results. They choose it because it seems authoritative and familiar.",
    "Se7en": "Ernest Hemingway once wrote, 'The world is a fine place and worth fighting for.' I agree with the second part.",
    "The Shawshank Redemption":"Remember Red, hope is a good thing, maybe the best of things, and no good thing ever dies.",
    "Forrest Gump": "Life is like a box of chocolates, you never know what you’re gonna get.",
    "Fight Club":"It’s only after we’ve lost everything that we’re free to do anything.",
    "The Breakfast Club": "We're all pretty bizarre. Some of us are just better at hiding it, that's all.",
    "Elon Musk":"If you get up in the morning and think the future is going to be better, it is a bright day. Otherwise, it's not.",
    "Steve Jobs": "The people who are crazy enough to think they can change the world are the ones who do.",
    "Walt Disney":"The way to get started is to quit talking and begin doing.",
    "Eleanor Roosevelt": "Do one thing every day that scares you",
    "Maya Angelou":"You will face many defeats in life, but never let yourself be defeated.",
    "Albert Einstein": "Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning",
    "Albert Einstein.":"In the middle of difficulty lies opportunity.",
    "Bill Gates": "It's fine to celebrate success, but it is more important to heed the lessons of failure.",
    "Ferris Bueller's Day Off":"Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.",
    "Finding Nemo":"Just keep swimming. Just keep swimming. Just keep swimming, swimming, and swimming.",
    "The Pursuit of Happyness":"You got a dream, you gotta protect it. People can’t do something themselves, they wanna tell you that you can’t do it.",
    "Cast Away":"I know what I have to do now. I’ve got to keep breathing because tomorrow the sun will rise. Who knows what the tide could bring?",
    "Steve Jobs.": "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do.",
}

load_dotenv("sensitiveinfo.env")
source, quote = random.choice(list(random_quotes.items()))
email_sender = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")
subject = "Daily Motivation"
body = f"""
{quote}\n\n-{source}
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())