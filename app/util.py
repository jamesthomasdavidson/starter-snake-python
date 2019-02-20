import requests
import numpy as np
import json

ENGINE_URL='http://localhost:3005'

./engine create -c ~/.snake-config.json \
  | jq --raw-output ".ID" \
  | xargs -I {} sh -c \
      "echo \"Go to this URL in your browser http://localhost:3000/?engine=${ENGINE_URL}&game={}\" && sleep 10; \
        ./engine run -g {}"

def start_game(size=7, engine_ip='http://0.0.0.0', engine_port='3009'):

    ENGINE_URL='http://localhost:3005'
    url='http://localhost:3000/start/'.format(eurl=ENGINE_URL)
    r = requests.post(url)
    print(r.text)
    url = 'http://localhost:3009/games/ping'

    r = requests.post(url)
    print(r.text)

start_game()