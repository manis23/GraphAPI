import requests

token = 'EAADRloCARUYBADygTviyWnofYInDKrD8Md4YWnkGoAtmUDRk4LUXr8l53ZAFAZCu3EgkwtQzKLlUof4EV0jTUklgwHQfO5u2tHvOp0XWfMSZBktMO9yoEIUS9p63vI337BjQXr8FdgHgInkevFww4hoVjrbAFYNbzqZCPCEsladFc7xO1F4p3d0Yh4ISylAtsOgAnz71JAZDZD'

me = 'https://graph.facebook.com/v4.0/me?access_token='+token

friends='https://graph.facebook.com/v4.0/me/friends?access_token='+token

search = 'https://graph.facebook.com/v4.0/search?q=dummies&type=page&access_token='+token

me1=requests.get(me)

f1=requests.get(friends)

s1=requests.get(search)
