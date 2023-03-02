

def conv(num): return num * 5;


conv2 = lambda num: num * 5

print(conv(7))

print(conv2(8))

import json

goopter_file = open('data/goopter.json', 'r')
gc = json.load(goopter_file)

print(gc['goopter-login']['goopter-url'])