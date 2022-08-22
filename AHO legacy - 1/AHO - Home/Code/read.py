power = 1
while power == 1:
    import json

    ## Database ##
        ## Files ##
    usersjsonv = "./Data/users.json"
    localjsonv = "./Data/local.json"
        ## Local ##
    with open (localjsonv, "r") as localjson:
        templ = json.load(localjson)
    signedin = templ["signedin"]
        ## Users ##
    with open (usersjsonv, "r") as usersjson:
        tempu = json.load(usersjson)
    def usersd():
        if signedin == 0 or signedin == 2:
            print("Manage Users")
            if signedin == 0:
                print(" (1) Sigh Up")
                print(" (2) Sign In")
            if signedin == 2:
                print(" (1) View User")
                print(" (2) Edit User")
                print(" (3) Remove User")
            inpmu = input("Select what you would like to do.  -  ")
            listmu = ["1", "2", "3"]
            if signedin == 0:
                if inpmu == "1":
                    print(tempu)
                    tempu_user = {}
                    tempu_user["firstname"] = input("Enter your first name.  -  ")
                    with open (usersjsonv, "w") as usersjson:
                        json.dump(tempu_user, usersjson, indent=2)
            if signedin == 2:
                if inpmu == "1":
                    print("finish this")
            if inpmu not in listmu or signedin == 0 and inpmu == "3":
                print()
                print("Please select a number.")
                print()
            if signedin == 2:
                signedin == 1

    usersd()
    while signedin == 1:
        ## inp ##
        inpv = input("How can I help you?  -  ")
        inp = inpv.lower()

        from datetime import datetime
        import pihole as ph
        from googlesearch import search
        import requests
        import webbrowser
        from youtubesearchpython import *

        ## Date-Time ##
        now = datetime.now()
        current_time = now.strftime("%r")
        current_date = now.strftime("%a %x")
        ## Pi-hole ##
        pihole = ph.PiHole("192.168.1.201")
        phstatus = pihole.status
        if phstatus == "enabled":
            phstatus = "on"
        else:
            phstatus = "off"

        ## imp Date-Time  ##
            ## inp Time ##
        inptime = ["what time is it", "what time is it?"]
            ## inp Date ##
        inpdate = ["whats todays date", "whats todays date?", "what's todays date", "what's todays date?", "what's today's date", "what's today's date?", ]
        ## imp Pi-hole ##
        inpphstatus = ["ph status", "ph status?", "pihole status", "pihole status?", "pi-hole status", "pi-hole status?", "pi hole status", "pi hole status?"]
        inpphdomaincount = ["ph domain count", "ph domain count?", "pihole domain count", "pihole domain count?", "pi-hole domain count", "pi-hole domain count?", "pi hole domain count", "pi hole domain count?"]
        inpphqueries = ["ph queries", "ph queries?", "pihole queries", "pihole queries?", "pi-hole queries", "pi-hole queries?", "pi hole queries", "pi hole queries?"]
        inpphblocked = ["ph blocked", "ph blocked?", "pihole blocked", "pihole blocked?", "pi-hole blocked", "pi-hole blocked?", "pi hole blocked", "pi hole blocked?"]
        inpphadspercentage = ["ph ads percentage", "ph ads percentage?", "pihole ads percentage", "pihole ads percentage?", "pi-hole ads percentage", "pi-hole ads percentage?", "pi hole ads percentage", "pi hole ads percentage?"]
        inpphuniquedomains = ["ph unique domains", "ph unique domains?", "pihole unique domains", "pihole unique domains?", "pi-hole unique domains", "pi-hole unique domains?", "pi hole unique domains", "pi hole unique domains?"]
        inpphforwarded = ["ph forwarded", "ph forwarded?", "pihole forwarded", "pihole forwarded?", "pi-hole forwarded", "pi-hole forwarded?", "pi hole forwarded", "pi hole forwarded?"]
        inpphcached = ["ph cached", "ph cached?", "pihole cached", "pihole cached?", "pi-hole cached", "pi-hole cached?", "pi hole cached", "pi hole cached?"]
        inpphtotalclients = ["ph total clients", "ph total clients?", "pihole total clients", "pihole total clients?", "pi-hole total clients", "pi-hole total clients?", "pi hole total clients", "pi hole total clients?"]
        ## Power ##
        inppower = ["power off", "power off?", "exit", "exit?"]
        ## Look up Web ##
        inplookupweb = ["look up", "look up?", "lookup", "lookup?", "look up web", "look up web?", "lookup web", "lookup web?"]
        inpopenurl = ["open url", "open url?", "look up url", "look up url?", "lookup url", "lookup url?"]
        inpopenweb = ["open web", "open web?", "open browser", "open browser?", "open webbrowser", "open webbrowser?", "open web browser", "open web browser?"]
        ## Look up YouTube ##
        inplookupytchannel = ["look up yt channel", "look up yt channel?", "look up youtube channel", "look up youtube channel?"]

        ## If ##
            ## Date-Time ##
        if inp in inptime:
            print("The time is " + current_time + ".")
        if inp in inpdate:
            print("The Date is " + current_date + ".")
            ## Pi-hole ##
        if inp in inpphstatus:
            print("Pi-hole's " + phstatus + ".")
        if inp in inpphdomaincount:
            print("Pi-hole's domain count is " + pihole.domain_count + ".")
        if inp in inpphqueries:
            print("Pi-hole's querie count is " + pihole.total_queries + ".")
        if inp in inpphblocked:
            print("Pi-hole's blocked count is " + pihole.blocked + ".")
        if inp in inpphadspercentage:
            print("Pi-hole's ads percentage is " + pihole.ads_percentage + "%.")
        if inp in inpphuniquedomains:
            print("Pi-hole's unique domains count is " + pihole.unique_domains + ".")
        if inp in inpphforwarded:
            print("Pi-hole's forwarded count is " + pihole.forwarded + ".")
        if inp in inpphcached:
            print("Pi-hole's cached count is " + pihole.cached + ".")
        if inp in inpphtotalclients:
            print("Pi-hole's client count is " + pihole.total_clients + ".")
        ## Power ##
        if inp in inppower:
            print("Powering off.")
            signedin = 0
            power = 0
        ## Look up ##
            ## Look up Web ##
        if inp in inplookupweb:
            urlv = input("What would you like to lookup?  -  ")
            for url in search(urlv , num_results=1):
                        r = requests.get(url)
                        url = r.url
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)
        if inp in inpopenurl:
            url = input("What url would you like to open?  -  ")
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)
        if inp in inpopenweb:
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open("")
            ## Look up YouTube ##
        if inp in inplookupytchannel:
            urlv = input("What channel would you like to lookup on youtube?  -  ")
            channelsSearch = ChannelsSearch(urlv, limit = 1)
            result = channelsSearch.result()
            url = result["result"][0]["link"]
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)