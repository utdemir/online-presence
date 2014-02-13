import requests

API_URL = "https://graph.facebook.com"

def facebook(username):
    requested_fields = ['id', 'name', 'picture', 'first_name', 'last_name', 
                        'middle_name', 'gender', 'username', 'link', 
                        'website', 'birthday', 'work', 'education']

    main = requests.get("%s/%s" % (API_URL, username), 
                        params={"fields": ",".join(requested_fields)}).json()
    main["big_picture"] = requests.head("%s/%s/picture" % (API_URL, username), 
                            params={"width": 9999, "height": 9999}
                            ).headers["location"]
   
    return main

MAIN = facebook
