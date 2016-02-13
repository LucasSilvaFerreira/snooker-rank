from flask import Flask, render_template
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('/home/lucas/PycharmProjects/snooker-rank/rank.json')

@app.route('/')
def hello_world():
    rank = [l for l in  sorted(db.all(), key= lambda x:x['vitorias']/float(x['partidas']), reverse=True)]
    for n,r in enumerate(rank):
        rank[n]["ratio"]= round(r['vitorias']/float(r['partidas']), 2)
    return render_template('index.html', rank=rank)



if __name__ == '__main__':
    app.debug = True
    app.run()
