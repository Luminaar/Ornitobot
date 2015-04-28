#! /usr/bin/python2

import twitter
import random 
import credentials

def load_list(file_name):
    """Read lines from a file and return as a list."""
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def get_proverb():
    """Get a randomly generated proverb."""
    birds = load_list('birds.txt')
    proverbs = load_list('proverbs.txt')

    while True:
        bird1 = random.choice(birds).upper()
        bied2 = random.choice(birds).upper()
        output = random.choice(proverbs).format(bird1, bird2)
        if len(output) > 140:
            continue
        else:
            break

    return output


if __name__=='__main__':

    api = twitter.Api(consumer_key=credentials.key,
                      consumer_secret=credentials.secret,
                      access_token_key=credentials.token_key,
                      access_token_secret=credentials.token_secret)

    print get_proverb()
