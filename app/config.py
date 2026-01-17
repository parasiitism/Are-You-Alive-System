import os

ENV = os.getenv("ENV", "DEV")   # DEV | PROD

SMS_SENDER_ID = os.getenv("SMS_SENDER_ID", "LIFCHK")
SMS_TEST_NUMBER = os.getenv("+919546566148")  # your personal number
