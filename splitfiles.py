import os
import re
import sys

if (len(sys.argv) < 3 or not sys.argv[1] or not sys.argv[2]):
    print('usage: <input filename> <output folder>')
    exit()

filename = sys.argv[1]
folder = sys.argv[2]

if not os.path.exists(folder):
    os.makedirs(folder)

delimeter = '### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###'

with open(filename) as f:
    alltext = f.read()
    stories = alltext.split(delimeter)
    title_pattern = re.compile(r"[\n\s]*([^\r\n]+)", re.MULTILINE)
    for story in stories:
        match = title_pattern.match(story)
        title = match.group(1)
        title = re.sub(r'[^a-z0-9]+', '_', title, count=0, flags=re.IGNORECASE)
        outfilename = title[0:48] + '.txt'
        with open(os.path.join(folder, outfilename), 'w') as outfile:
            story = story.strip()
            outfile.write(story)
