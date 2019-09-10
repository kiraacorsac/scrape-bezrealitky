from flask import Flask
import scrape_bezrealitky
import spam_attempt
#import call_me
import alerted
import json
import traceback
import pprint


app = Flask(__name__)


@app.route("/")
def hello():
    try:
        molbio = spam_attempt.request()
        homes = scrape_bezrealitky.request()[0]
        if len(homes) > 0:
        #     call_me.call_people_to_alert()
             return json.dumps(homes)
        return  "Autozápis proveden" in "lol" + "<br>" + "nothing new" + "<br>" + ("-"*50) + "<br>" + json.dumps(alerted.get_called_list())
    except Exception as exc:
        return "<br>".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
if __name__ == "__main__":
    app.run(port=80)