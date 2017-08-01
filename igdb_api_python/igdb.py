# IGDB PYTHON WRAPPER

import requests
import json

class igdb:

    __api_key = ""

    def __init__(self,api_key):
        self.__api_key = api_key

    #CALL TO THE API
    def call_api(self,endpoint,args):
        ids     = ""
        fields  = "*"
        order   = ""
        filters = ""
        #If array, convert it to komma seperated string
        if type(args) != int:
            if 'ids' in args:
                if type(args['ids']) != int:
                    ids = ",".join(map(str,args['ids']))
                else:
                    ids = args['ids']
            if 'fields' in args:
                if type(args['fields']) != str:
                    fields = ",".join(map(str,args['fields']))
                else:
                    fields = args['fields']
            if 'order' in args:
                order = "&order=" + str(args['order'])
            if 'filters' in args:
                #ids = ",".join(map(str,ids))
                for key, value in args['filters'].items():
                    filters = filters + "&filter" + key + "=" + str(value)
        else:
            ids = args

        url = 'https://api-2445582011268.apicast.io/'+ endpoint + "/" + str(ids) + "?fields=" + str(fields)+ str(order)+ str(filters)
        print(url)

        headers = {
            'user-key': self.__api_key,
            'Accept' : 'application/json'
            }
        r = requests.get(url, headers=headers)
        #print(r.status_code)
        if r.status_code != 200:
            print("!- ERROR -! " + r.status_code)
        return r

    #GAMES
    def games(self,args=""):
        r = self.call_api("games",args)
        r = json.loads(r.text)
        return r
    #PULSE
    def pulses(self,args=""):
        r = self.call_api("pulses",args)
        r = json.loads(r.text)
        return r
    #CHARACTERS
    def characters(self,args=""):
        r = self.call_api("characters",args=args)
        r = json.loads(r.text)
        return r
    #COLLECTIONS
    def collections(self,args=""):
        r = self.call_api("collections",args=args)
        r = json.loads(r.text)
        return r
    #COMPANIES
    def companies(self,args=""):
        r = self.call_api("companies",args=args)
        r = json.loads(r.text)
        return r
    #FRANCHISES
    def franchises(self,args=""):
        r = self.call_api("franchises",args=args)
        r = json.loads(r.text)
        return r
    #FEEDS
    def feeds(self,args=""):
        r = self.call_api("feeds",args=args)
        r = json.loads(r.text)
        return r
    #PAGES
    def pages(self,args=""):
        r = self.call_api("pages",args=args)
        r = json.loads(r.text)
        return r
    #GAME_ENGINES
    def game_engines(self,args=""):
        r = self.call_api("game_engines",args=args)
        r = json.loads(r.text)
        return r
    #GAME_MODES
    def game_modes(self,args=""):
        r = self.call_api("game_modes",args=args)
        r = json.loads(r.text)
        return r
    #GENRES
    def genres(self,args=""):
        r = self.call_api("genres",args=args)
        r = json.loads(r.text)
        return r
    #KEYWORDS
    def keywords(self,args=""):
        r = self.call_api("keywords",args=args)
        r = json.loads(r.text)
        return r
    #PEOPLE
    def people(self,args=""):
        r = self.call_api("people",args=args)
        r = json.loads(r.text)
        return r
    #PLATFORMS
    def platforms(self,args=""):
        r = self.call_api("platforms",args=args)
        r = json.loads(r.text)
        return r
    #PLAYER_PERSPECTIVES
    def player_perspectives(self,args=""):
        r = self.call_api("player_perspectives",args=args)
        r = json.loads(r.text)
        return r
    #PULSE_GROUPS
    def keywords(self,args=""):
        r = self.call_api("pulse_groups",args=args)
        r = json.loads(r.text)
        return r
    #RELEASE_DATES
    def release_dates(self,args=""):
        r = self.call_api("release_dates",args=args)
        r = json.loads(r.text)
        return r
    #THEMES
    def themes(self,args=""):
        r = self.call_api("themes",args=args)
        r = json.loads(r.text)
        return r
    #REVIEWS
    def reviews(self,args=""):
        r = self.call_api("reviews",args=args)
        r = json.loads(r.text)
        return r
