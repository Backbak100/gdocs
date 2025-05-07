import requests, webbrowser, random, time

#There are 44 characters in a doc ID
#There are: letters (a-z, A-Z), numbers (0-9), and some special characters like hyphens (-) and underscores (_)

#gets random doc ID
def getid():
    docid = ""
    for i in range (0, 44):
        charnum = random.randint(0, 63)
        #print(charnum)
        if charnum < 10:
            docid = docid + str(charnum)
        elif charnum > 9 and charnum < 36:
            charnum = charnum + 55
            docid = docid + chr(charnum)
        elif charnum > 35 and charnum < 62:
            charnum = charnum + 61
            docid = docid + chr(charnum)
        elif charnum == 62:
            docid = docid + "_"
        elif charnum == 63:
            docid = docid + "-"
    return docid

while True:
    #creates random doc link
    docurl = "https://docs.google.com/document/d/" + getid() + "/"
    #get req
    response = requests.get(docurl)

    #check
    if response.status_code == 200:
        webbrowser.open(docurl)
        print("Loaded")
        break
    else:
        print("Not", i)

    #wait inbetween get requests
    time.sleep(120+random.randint(1,60))
