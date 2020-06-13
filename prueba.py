import requests
def getEmotions():
    while True:
        id=input()
        if (id=="exit"):
            break
        URL = "http://leoviquez.synology.me/VisionAPI/cursos.py"
        r = requests.get(url = URL)
        results= eval(r.text)
        print (results)
getEmotions()
