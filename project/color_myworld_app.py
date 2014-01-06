import twitter,json,  wikipedia

class MyPerson(object):
    def __init__(self, name):
        self.name = name
        self.bio = ""
        self.tags = []

    #set person's name
    def setName (self,name):
        self.name = name

    #set person's bio
    def setBio(self,bio):
        self.bio = bio

    #set persons' tags that you want to search on
    def setTags(self,tags):
        self.tags=self.tags.append(tags)


class SocialMediaLink(object):
    def __init__(self):
        self.socialMediaType=""
        self.url=""
        self.username=""
        self.password=""
        self.api=""
        self.status=""



#classes.py or MyPerson.py, Social.py

#main method would have API keys



# TODO add Twitter api
class Twitter(SocialMediaLink):
    def __init__(self):
    #api=twitter.Api(consumer_key='ygHMdyqI5Rp5U8ocszeg',consumer_secret='Z1inuYmTC53Fnf6Pv5KDlhhYB8iDXICDefjPwzLBQ',access_token_key='545244617-28sr37n7IZTqrN6kIzUm9LH7YGNomPnYYEa3qhLy',access_token_secret='xsSyHxp49KAnRusyjoE3TjP5otU08WlIajzkzOU')
    #username=twitter.User()
    #status=api.GetSearch(username)
    #def verifyCredentials(self):
    #    print self.api.VerifyCredentials()
    pass


# FIXME fix wikipediea data
class Wikipedia(SocialMediaLink):
    #status=wikipedia.summary(username)
    pass

# TODO get sentiment
def getSentimentforstatus(status):
    for s in status:
        text=s.text
        print text
        sentiment = "http://www.datasciencetoolkit.org/text2sentiment/"+text
        responselevel=requests.get(r'"http://www.datasciencetoolkit.org/text2sentiment"+text')
        score=json.loads(responselevel.text)
        print score

