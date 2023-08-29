"""
Exercise No. 61

The following list is given:

    filenames = ['view.jpg', 'bear.jpg', 'ball.png']

Add file 'phone.jpg' to this list at the beginning. Then delete the file 'ball.png'. In response, print the filenames
list to the console.

Expected result:

    ['phone.jpg', 'view.jpg', 'bear.jpg']
"""
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')

print(filenames)
