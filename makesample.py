#!/usr/bin/env python

import datetime
import random
import json

artists = [
    'Ono', 'Aluminica', 'Rolling Waters', 'Red Floyd', 'The Carpenters',
    'Ono', 'Aluminica', 'Ono', 'Aluminica', 'Ono', 'Aluminica',
    'Aluminica',
]

def main():
    for i in range(1000000):
        date = datetime.date(2015, 10, random.randint(1, 30))
        track = {
            'artist': '%s' % random.choice(artists),
            'album': '%s' % random.randint(0, 3),
            'track': '%s' % random.randint(0, 12),
            'date': str(date)
        }
        print(json.dumps(track))

if __name__ == '__main__':
    main()
