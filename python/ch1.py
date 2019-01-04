# Challenge Link: https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s - %(funcName)s - %(lineno)d] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler('ch1_logs.log', 'a'),
        logging.StreamHandler(),
    ])


def main():
    name = input('Name please:')
    age = input('Age please:')
    reddit_username = input('Reddit username please:')

    print('Your name is %s, you are %s years old, and your username is %s.' % (name, age, reddit_username))

    logging.info('Name: %s' % name)
    logging.info('Age: %s' % age)
    logging.info('Reddit username: %s' % reddit_username)


if __name__ == '__main__':
    main()
