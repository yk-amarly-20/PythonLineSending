import sys
sys.path.append('../')
from MessagingSender import MessagingSender 

def main(token, message, image):
    sender = MessagingSender(token)
    sender.send_message(message, image)

    return

if __name__ == '__main__':
    with open('./token.txt', 'r') as f:
        token = f.read()[:-1]

    message = 'hello world'
    image = './11195179127721.jpg'
    # image = None

    main(token, message, image)
