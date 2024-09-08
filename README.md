# Daily Motivation Emailer

## Overview
This project provides an automated solution to send daily motivational emails at 8 AM. The script is designed to be cost-efficient and secure, leveraging cloud infrastructure to run on a schedule without manual intervention.

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
To deploy this script:
1. Upload the script to AWS Lambda.
2. Create environmental variables called EMAIL_SENDER and EMAIL_RECEIVER. Set these equal to your email address.
3. If you're using Gmail you must generate an app password. Other providers have similar authentification.
4. Copy the password and create the environmental variable EMAIL_PASSWORD and paste your password. 
5. Configure AWS EventBridge to trigger the Lambda function daily at 8 AM or your preferred time.
