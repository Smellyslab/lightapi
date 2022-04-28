import requests
import json # // might not be needed just here in case.

baseurl = "https://lightbringers.pythonanywhere.com"

def getrawpostbyid(postid):
    return requests.get(f"{baseurl}/api/v1/getrawpostbyid/{postid}").text

# print(getrawpostbyid("e08d9e0872046da906561029afffb30d")) # // should work
# output // {"post_creator":"A Lightbringer.","post_randomizer_bytes":"4a1230f91e6ef377e85c57bd0576a5a6720781404ead621af069f681ba053ab8db9b5774e7322ca9c8f80397fad9bca2762a","postdata64":"CmhlbGxvLAoKbXkgbmFtZSBpcyBqaW1teSwKCmkgbGlrZSBjaGVlc2UKCnRoaXMgaXMgYSB0ZXN0IG9mIHRoZSBuZXcgbGlnaHRicmluZ2VycyBXRUIgQVBJIChSRVNURlVMKS4KCkhhaWwgU2F0YW4uCgo=","timestamp":"2022-04-28 15:13:24.820332","version":"1.0.1"}
# print(getrawpostbyid("this id literally cannot exist. ")) # // shouldn't work. 
# output // Post with id: "this id literally cannot exist. " not found.
# // both worked as needed so they are now commented; aswell are their output. 