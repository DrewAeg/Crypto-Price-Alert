"""
Test the Pushbullet notification.
"""

# Local modules
import price_alert

if __name__ == "__main__":
    title = "Test Title"
    body = "Test Message"
    price_alert.pushbullet_message(title,body)
