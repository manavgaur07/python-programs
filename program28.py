mountains = [
    ['makalu', 8485],
    ['lhotse', 7896],
    ['kanchendzonga', 8965],
    ['k2', 8611],
    ['everest', 7896]
]
highest_mountain = [m for m in mountains if m[1]> 8600]
print(highest_mountain)