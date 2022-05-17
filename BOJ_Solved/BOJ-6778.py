"""
백준 6778번 : Which Alien?
"""

an = int(input())
eye = int(input())

if an >= 3 and eye <= 4:
    print('TroyMartian')
if an <= 6 and eye >= 2:
    print('VladSaturnian')
if an <= 2 and eye <= 3:
    print('GraemeMercurian')
