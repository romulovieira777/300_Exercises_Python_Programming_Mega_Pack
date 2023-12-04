"""
Exercise No. 233

The exercise includes a file users.json containing data about users of a certain application.

The User class has been created using the collections module. Then, for each user, an instance of the User class was
created from the users.json file and assigned to the users list:

    from collections import namedtuple
    import json


    with open('users.json', 'r') as file:
        content = json.load(file)

    headers = tuple(content[0].keys())
    User = namedtuple('User', headers)
    values = [tuple(user.values()) for user in content]
    users = [User(*user) for user in values]

Using the built-in pickle module, dump all created users (users list) to a file named users.pickle. Then load the
contents of the users.pickle back into the content variable (list).

In response print the user with id = 4 from the content variable to the console.

Expected result:

    User(id=4, first_name='Lucie', last_name='Brunetti', email='lbrunetti3@bbb.org', gender='Non-binary', is_active=True)
"""
from collections import namedtuple
import json
import pickle


with open('../Data/users.json', 'r') as file:
    content = json.load(file)

headers = tuple(content[0].keys())
User = namedtuple('User', headers)
values = [tuple(user.values()) for user in content]
users = [User(*user) for user in values]


with open('../Data/users.pickle', 'wb') as file:
    pickle.dump(users, file)

with open('../Data/users.pickle', 'rb') as file:
    content = pickle.load(file)

result = tuple(filter(lambda obj: obj.id == 4, content))[0]
print(result)
