import requests 
import threading
import json # // not sure if this is needed but im adding it just cuz. 

baseurl = "https://lightbringers.pythonanywhere.com"

def createpostfunc(posttext, apikey):
    data = {
        "postdata": posttext,
        "apikey": apikey,
    }
    return requests.post(f"{baseurl}/api/v1/newpost", json=data)

def createpost(posttext, apikey):
    #postmaker = threading.Thread(target=createpost, args=(posttext,apikey,))
    #output = postmaker.start()
    output = createpostfunc(posttext, apikey)
    return output.text

text = """
hello,

my name is jimmy,

i like cheese

this is a test of the new lightbringers WEB API (RESTFUL).

Hail Satan.

"""


# print(createpost(text, "devs")) // workds correctly just here for testing, no need to leave it in the actual file. 