import requests, time

print("Please Input What Interval Should We Use To Post New Message")
interval = input()
print("Please Input Cookie Of Your Account")
cookie = input()
print("Please Input Your Session ID")
sessionId = input()

def sendRequest():
    message = ""

    with open('message.txt') as f:
        contents = f.read()
        message = contents

    reqPost = requests.post(url="https://steamcommunity.com/comment/Clan/post/103582791435683520/-1/", headers={
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie,
        "Host": "steamcommunity.com",
        "Origin": "https://steamcommunity.com",
        "Referer": "https://steamcommunity.com/groups/plus-rep"
    }, data={"comment": message,
             "count": 6,
             "sessionid": sessionId,
             "feature2": -1})
    
    reqPost2 = requests.post(url="https://steamcommunity.com/comment/Clan/post/103582791429522596/-1/", headers={
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie,
        "Host": "steamcommunity.com",
        "Origin": "https://steamcommunity.com",
        "Referer": "https://steamcommunity.com/groups/plus-rep"
    }, data={"comment": message,
             "count": 6,
             "sessionid": sessionId,
             "feature2": -1})
    
    reqPost3 = requests.post(url="https://steamcommunity.com/comment/Clan/post/103582791461930648/-1/", headers={
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie,
        "Host": "steamcommunity.com",
        "Origin": "https://steamcommunity.com",
        "Referer": "https://steamcommunity.com/groups/plus-rep"
    }, data={"comment": message,
             "count": 6,
             "sessionid": sessionId,
             "feature2": -1})
    
    print(reqPost)
    print(reqPost2)
    print(reqPost3)

while True:
    sendRequest()
    time.sleep(interval)
