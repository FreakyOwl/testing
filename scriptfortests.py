import urllib.request
import json
listofurls = open('123.txt', 'r')
listsoffriends = open('friendsurls.txt', 'w')
domain = ''
for line in listofurls:                 # получаем информацию о пользователях за один запрос
    domain = domain+line[15:len(line)-1]+','  # получаем короткое название из url
with urllib.request.urlopen("https://api.vk.com/method/users.get?user_ids="+domain[:len(domain)-1]
     + "&v=5.52&access_token=b1b6da65b1b6da65b1b6da6547b1c57304bb1b6b1b6da65eefec3e8bb3149f4bcc040dc") as userurl:
    userinfo = json.load(userurl)
for item in userinfo.get('response'):
    personid = str(item.get('id'))        # получаем ID пользователя
    print(personid)
    with urllib.request.urlopen("https://api.vk.com/method/friends.get?user_id="+personid +
         "&v=5.52&access_token=b1b6da65b1b6da65b1b6da6547b1c57304bb1b6b1b6da65eefec3e8bb3149f4bcc040dc") as friendsurl:
        friendsinfo = json.load(friendsurl)     # получаем список друзей
        print(friendsinfo)
    for friendid in friendsinfo.get('response').get('items'):   # формируем список url-ов друзей
        friendurl = "https://vk.com/id"+str(friendid)
        listsoffriends.write(friendurl + '\n')
    listsoffriends.write('\n')
listofurls.close()
listsoffriends.close()
