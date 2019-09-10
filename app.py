from flask import Flask
import scrape_bezrealitky
import spam_attempt
import call_me
import alerted
import json
app = Flask(__name__)


@app.route("/")
def hello():
    
    spam_attempt.request()
    homes = scrape_bezrealitky.request()[0]
    if len(homes) > 0:
        call_me.call_people_to_alert()
        return json.dumps(homes)
    return "nothing new" + "<br>" + ("-"*50) + "<br>" + json.dumps(alerted.get_called_list())

if __name__ == "__main__":
    app.run(port=80)