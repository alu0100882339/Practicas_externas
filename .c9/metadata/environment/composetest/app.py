{"filter":false,"title":"app.py","tooltip":"/composetest/app.py","undoManager":{"mark":21,"position":21,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":68},"action":"insert","lines":["import time","","import redis","from flask import Flask","","app = Flask(__name__)","cache = redis.Redis(host='redis', port=6379)","","","def get_hit_count():","    retries = 5","    while True:","        try:","            return cache.incr('hits')","        except redis.exceptions.ConnectionError as exc:","            if retries == 0:","                raise exc","            retries -= 1","            time.sleep(0.5)","","","@app.route('/')","def hello():","    count = get_hit_count()","    return 'Hello World! I have been seen {} times.\\n'.format(count)"],"id":1}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["#"],"id":3}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":[" "],"id":4},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["h"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["o"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["s"],"id":5},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"remove","lines":["o"]}],[{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["s"],"id":6},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["t"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["a"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["n"],"id":7},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["a"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["t"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"remove","lines":["s"]}],[{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["o"],"id":8},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["s"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["n"],"id":9},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["a"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["m"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":[" "],"id":10},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["d"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["e"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":[" "],"id":11},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["c"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["o"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["n"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["t"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["e"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["n"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["d"],"id":12},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["o"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":[" "],"id":13},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["d"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":[" "],"id":14},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["e"],"id":15},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["d"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["i"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":[" "],"id":16},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["e"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":[" "],"id":17},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["l"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":[" "],"id":18},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["r"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["e"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["d"]}],[{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":[" "],"id":19},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"insert","lines":["d"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":[" "],"id":20},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"insert","lines":["l"]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"insert","lines":[" "],"id":21},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"insert","lines":["a"]},{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"insert","lines":["p"]},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"insert","lines":["l"]},{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"insert","lines":["i"]},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"insert","lines":["c"]},{"start":{"row":6,"column":56},"end":{"row":6,"column":57},"action":"insert","lines":["a"]},{"start":{"row":6,"column":57},"end":{"row":6,"column":58},"action":"insert","lines":["c"]},{"start":{"row":6,"column":58},"end":{"row":6,"column":59},"action":"insert","lines":["i"]}],[{"start":{"row":6,"column":59},"end":{"row":6,"column":60},"action":"insert","lines":["ó"],"id":22},{"start":{"row":6,"column":60},"end":{"row":6,"column":61},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":0},"end":{"row":8,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584376261220,"hash":"4bdf735ee710520437daf8bdd16091eccf688bd0"}