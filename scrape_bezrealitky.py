import requests
import json
import alerted
import os

def request():
    magic_payload = {"query":"query WatchdogList($user: Int!, $userstateUser: Int) {\n  watchdogList(user: $user) {\n    list {\n      id\n      queryString\n      criteria {\n        advertType\n        description\n        offerType\n        estateType\n        disposition\n        polygons\n        priceMin\n        priceMax\n        balcony\n        terrace\n        newBuilding\n        surfaceMin\n        surfaceMax\n        ownership\n        equipped\n        construction\n        region {\n          id\n          type\n          subtype\n          path: idPath\n          parent {\n            id\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      adverts(interval: INTERVAL_1_DAY) {\n        list {\n          id\n          uri\n          shortDescription(breakLine: false, offerEstateType: true, disposition: true, surface: true)\n          address\n          advertObject {\n            address\n            ... on AdvertEstateOffer {\n              price\n              offerType\n              charges\n              __typename\n            }\n            ... on AdvertEstateRequest {\n              priceMin\n              priceMax\n              __typename\n            }\n            __typename\n          }\n          advertUserstate(user: $userstateUser, state: FAVOURITE) {\n            id\n            state\n            message\n            __typename\n          }\n          mainImageUrl(filter: WATCHDOG_ADVERT_PREVIEW_IMAGE)\n          __typename\n        }\n        totalCount\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  user(id: $user) {\n    id\n    premium\n    canAddWatchdog\n    __typename\n  }\n}\n","variables":{"user":658059,"userstateUser":658059},"operationName":"WatchdogList"}

    session_requests = requests.session()

    result =  session_requests.post(
    	' https://www.bezrealitky.cz/login-check', 
    	data = {
            '_target_path': '/moje-bezrealitky',
            '_username': os.environ.get('bezrealitky-name'),
            '_password': os.environ.get('bezrealitky-password'),
            '_remember_me': 'on'
        }, 
    	headers = dict(referer="https://www.bezrealitky.cz/prihlaseni")
    )
    assert(result.ok)
    assert('heslo' not in str(result.content))


    result = session_requests.post(
        'https://www.bezrealitky.cz/webgraphql', 
        json=magic_payload,
        headers = dict(referer = 'https://www.bezrealitky.cz/moje-bezrealitky/hlidaci-pes')
    )
    assert(result.ok)

    c = json.loads(result.content)
    new_homes = []
    homes = c['data']['watchdogList']['list'][0]['adverts']['list']
    for home in homes:
        if str(home['id']) + "\n" not in alerted.get_called_list():
            new_homes.append({
                    'id': home['id'],
                    'adress': home['address'],
                    'price':  home['advertObject']['price']+home['advertObject']['charges']
                })
            alerted.set_alerted(home)
    return new_homes, homes

if __name__ == '__main__':
    print(request()[0])
