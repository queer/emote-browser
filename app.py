from flask import *
import os
import psycopg2

app = Flask(__name__)
db_username = os.getenv("POSTGRES_USERNAME")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = "amybot"
db_host = "postgres"


# noinspection SqlResolve
@app.route('/')
def emote_list():
    conn = psycopg2.connect(dbname=db_name, user=db_username, password=db_password, host=db_host)
    c = conn.cursor()
    c.execute('''SELECT name, id, row_number() OVER (PARTITION BY emotes.name ORDER BY emotes.guild) AS 
                 discrim FROM emotes ORDER BY name, discrim ASC;''')
    render = render_template('index.html', emotes=c.fetchall())
    c.close()
    conn.close()
    return render

if __name__ == "__main__":
    app.debug = False
    app.run()
