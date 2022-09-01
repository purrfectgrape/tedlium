# Script to look up speakers in Wikipedia

import argparse
import re
import wikipedia
# sudo npm install wikit -g before using wikit

parser = argparse.ArgumentParser(description='Tool to extract speakers\' info and look them up in Wikipedia')
parser.add_argument('--input', type=str, required=True,
    help='Filepath of the input file')
parser.add_argument('--output', type=str, required=True,
    help='Filepath of the output')
parser.add_argument('--encoding', default='utf-8',
    help='character encoding for input/output')
args = parser.parse_args()

def camel_case_split(str):
   return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

filename = args.input
with open(filename, 'r') as infile:
    names = infile.readlines()
 
split_names = []
for name in names:
    split_name = ' '.join(camel_case_split(name.strip().split("_")[0]))
    if split_name not in split_names:
        split_names.append(split_name)

# look them up in Wikipedia
#os.system("touch " + args.output)
#for split_name in split_names:
#    os.system("wikit " + split_name + " >> " + args.output)

for split_name in split_names:
    with open(args.output, 'a') as outfile:
        try:
            outfile.write(split_name + '\t' + wikipedia.summary(split_name, 2) + '\n')
            print(split_name + '\t' + wikipedia.summary(split_name, 1) + '\n')
        except wikipedia.exceptions.PageError:
            outfile.write(split_name + '\t' + 'not found' + '\n')
        except wikipedia.exceptions.DisambiguationError:
            outfile.write(split_name + '\t' + 'ambiguous' + '\n')

print('done!')
