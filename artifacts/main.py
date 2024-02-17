from pprint import pprint

from app.group_finder import GroupFinder

with open('names.csv') as file:
    items = file.read().split()


pprint(
    GroupFinder.find(items)
)
