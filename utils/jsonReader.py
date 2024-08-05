import json

def getPrompt(filename):
    f = open(f'./prompts/{filename}.json')
    data = json.load(f)
    return data.get('prompt')


# read_file('botRole')
