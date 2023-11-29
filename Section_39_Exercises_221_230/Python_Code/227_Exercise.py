"""
Exercise No. 227

A file called hashtags.txt containing related to sport is attached to the exercise:

    #sport #fitness #training #motivation #gym #sports #workout #fit #football #love #instagood #fitnessmotivation
    #lifestyle #running #like #bodybuilding #healthy #instagram #health #soccer #follow #crossfit #photography #bhfyp
    #run #nature #fun #healthylifestyle #muscle #bhfyp #fashion #fitfam #gymlife #photooftheday #team #personaltrainer
    #nike #picoftheday #exercise #mma #sportlife #boxing #athlete #bike #basketball #happy #deporte #gymmotivation
    #strong #cycling #yoga #style #ufc #sportmotivation #fitnessgirl #calcio #instafit


Implement a function called clean_hashtags() that loads the included hashtags.txt file and does some cleanup. Extract
hashtags up to 4 characters long. The '#' sign is not included in the length of the hashtag. For example, the hashtag
'#gym' has a length of 3.

Also take care to remove duplicates, if any. Then return the alphabetically sorted hashtags as a list.

In response, call clean_hashtags() function and print the result to the console.

Expected result:

    ['#bike', '#fit', '#fun', '#gym', '#like', '#love', '#mma', '#nike', '#run', '#team', '#ufc', '#yoga']
"""
# Solution I


def clean_hashtags():
    with open('..\Data\hashtags.txt', 'r') as file:
        hashtags = file.read().split()
    hashtags = list(set([hashtag for hashtag in hashtags if 1 < len(hashtag) <= 4]))
    hashtags.sort()
    return hashtags


print(clean_hashtags())


# Solution II
def clean_hashtags():
    with open('..\Data\hashtags.txt', 'r') as file:
        content = file.read()
    hashtags = content.split()
    short_hashtags = [
        hashtag for hashtag in hashtags if len(hashtag) <= 5
    ]
    result = sorted(set(short_hashtags))
    return result


print(clean_hashtags())
