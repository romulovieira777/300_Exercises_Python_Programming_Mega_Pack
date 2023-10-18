"""
Exercise No. 161

The contents of the file plw.txt were loaded as follows;

    with open('plw.txt', 'r') as file:
        text = file.readlines()

lines variable:

    ['PLAYWAY',
     '',
     'PlayWay is a producer and publisher of computer and mobile games. The company is characterized by a very large
      number of development teams and a large number of games produced simultaneously.',
     "PlayWay sells, among others via the STEAM portal, AppStore and GooglePlay. The US and German markets are the two
      largest markets for the Group's sales.",
     'In addition, the company has PlayWay Campus - a campus for cooperating development teams.']

Tasks to perform:

    1. Get rid of blank lines.

    2. Split each line into tokens/words as shown below and print result to the console.

Formatted result:

[['PLAYWAY'],
 ['PlayWay',
  'is',
  'a',
  'producer',
  'and',
  'publisher',
  'of',
  'computer',
  'and',
  'mobile',
  'games.',
  'The',
  'company',
  'is',
  'characterized',
  'by',
  'a',
  'very',
  'large',
  'number',
  'of',
  'development',
  'teams',
  'and',
  'a',
  'large',
  'number',
  'of',
  'games',
  'produced',
  'simultaneously.'],
 ['PlayWay',
  'sells,',
  'among',
  'others',
  'via',
  'the',
  'STEAM',
  'portal,',
  'AppStore',
  'and',
  'GooglePlay.',
  'The',
  'US',
  'and',
  'German',
  'markets',
  'are',
  'the',
  'two',
  'largest',
  'markets',
  'for',
  'the',
  "Group's",
  'sales.'],
 ['In',
  'addition,',
  'the',
  'company',
  'has',
  'PlayWay',
  'Campus',
  '-',
  'a',
  'campus',
  'for',
  'cooperating',
  'development',
  'teams.']]


Expected result:

    [['PLAYWAY'], ['PlayWay', 'is', 'a', 'producer', 'and', 'publisher', 'of', 'computer', 'and', 'mobile', 'games.',
      'The', 'company', 'is', 'characterized', 'by', 'a', 'very', 'large', 'number', 'of', 'development', 'teams',
      'and', 'a', 'large', 'number', 'of', 'games', 'produced', 'simultaneously.'], ['PlayWay', 'sells,', 'among',
      'others', 'via', 'the', 'STEAM', 'portal,', 'AppStore', 'and', 'GooglePlay.', 'The', 'US', 'and', 'German',
      'markets', 'are', 'the', 'two', 'largest', 'markets', 'for', 'the', "Group's", 'sales.'], ['In', 'addition,',
      'the', 'company', 'has', 'PlayWay', 'Campus', '-', 'a', 'campus', 'for', 'cooperating', 'development', 'teams.']]
"""
# Solution I
with open('../Data/plw.txt', 'r') as file:
    text = file.readlines()

text = [line.replace('\n', '') for line in text]
text = [line for line in text if line != '']
text = [line.split(' ') for line in text]

print(text)


# Solution II
with open('plw.txt', 'r') as file:
    lines = file.read().splitlines()

lines = [line for line in lines if len(line) > 0]
lines = [line.split() for line in lines]

print(lines)
