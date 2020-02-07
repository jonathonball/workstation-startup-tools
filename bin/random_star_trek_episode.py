#!/usr/bin/env python3
"""
Help user decide what to watch
"""
import random

SHOWS = [
    {
        "name": "Star Trek: Voyager",
        "seasons": [15, 26, 26, 26, 26, 26, 25]
    },
    {
        "name": "Star Trek: The Next Generation",
        "seasons": [25, 22, 26, 26, 26, 26, 25]
    },
    {
        "name": "Star Trek: Enterprise",
        "seasons": [26, 26, 24, 22]
    },
    {
        "name": "Star Trek: The Original Series",
        "seasons": [29, 26, 24]
    },
    {
        "name": "Star Trek: Deep Space Nine",
        "seasons": [19, 26, 26, 25, 26, 26, 25]
    }
]

SHOW = SHOWS[random.randrange(0, len(SHOWS))]
SEASON = random.randrange(0, len(SHOW['seasons']))
EPISODE = random.randrange(0, SHOW['seasons'][SEASON])
print(' '.join([SHOW['name'], 'Season', str(SEASON + 1), 'Episode', str(EPISODE + 1)]))
