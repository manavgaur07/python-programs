mountains = [
    ['makalu', 8485],
    ['lhotse', 7896],
    ['kanchendzonga', 8965],
    ['k2', 8611],
    ['everest', 7896]
]

highest_mountains=list(filter(lambda m: m[1]>8000, mountains))
print(highest_mountains)