"""
Exercise No. 45

From the given url:

    url = (
        'https://e-smartdata.teachable.com/'
        'p/sciezka-data-scientist-machine-learning-engineer'
    )

extract the slug after the last character '/'. Then replace all dashes with spaces and print the result to the console
as shown below.

Expected result:

    sciezka data scientist machine learning engineer
"""
url = (
    'https://e-smartdata.teachable.com/'
    'p/sciezka-data-scientist-machine-learning-engineer'
)
slug = url.split('/')[-1]
print(slug.replace('-', ' '))
