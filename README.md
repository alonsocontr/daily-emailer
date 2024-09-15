# Daily Motivational Emailer

## Overview
This project was made to automate the process of receiving motivational and inspiring quotes through the implementation of a daily email system.

## Features
- **Daily Email Sending**: Sends a motivational email daily at 8 AM.
- **Secure Configuration**: Configured using environment variables for secure handling of credentials.
- **Cloud-Based Scheduling**: Utilizes cloud infrastructure for efficient scheduling and execution.

## Getting Started

### Prerequisites
- **Python 3.x**
- **An email account** for sending emails
- **AWS EventBridge** to schedule the script to run daily at 8 AM

### Deployment
To deploy this script to AWS cloud:
1. Upload the script to AWS Lambda.
2. Remove lines of code that loads a .env file (line 5 and line 31)
3. Create environmental variables called EMAIL_SENDER and EMAIL_RECEIVER. Set these equal to your email address.
4. If you're using Gmail you must generate an app password. Other providers have similar authentification.
5. Copy the password and create the environmental variable EMAIL_PASSWORD and paste your password. 
6. Configure AWS EventBridge to trigger the Lambda function daily at 8 AM or your preferred time.
