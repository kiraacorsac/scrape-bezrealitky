import requests
import alerted
import os
import webbrowser
import base64
import tempfile



def render(html):
    
    with tempfile.NamedTemporaryFile('wb', delete=False, suffix=".html") as f:
        url = 'file://' + f.name
        f.write(html)
        webbrowser.open(url)

def request():


    session = requests.session()

    redirect = session.get("https://is.muni.cz/auth")
    
    assert(redirect.ok)

    login = session.post(redirect.url, data = {
        'akce': 'login',
        'credential_0': os.environ.get("is-name"),
        'credential_1': os.environ.get("is-password"),
        'uloz': 'uloz'
    })
    assert(login.ok)

    enroll = session.get("https://is.muni.cz/auth/student/zapis?fakulta=1433;obdobi=7643;studium=789008;akce=autoz")
    assert(enroll.ok)
    return enroll
if __name__ == '__main__':
    render(request().content)
