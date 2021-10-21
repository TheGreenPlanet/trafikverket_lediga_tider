import requests
import time
from discord import Webhook, RequestsWebhookAdapter

# README.md
discord_webhook_url = 'webhook url'

url = 'https://fp.trafikverket.se/Boka/occasion-bundles'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '509',
    'Content-Type': 'application/json',
    'Cookie': 'forarprov-ext=ffffffff0914194145525d5f4f58455e445a4a423660; _pk_ref..825a=%5B%22%22%2C%22%22%2C1634209124%2C%22https%3A%2F%2Fwww.trafikverket.se%2F%22%5D; _pk_ses..825a=1; _pk_ref.4.825a=%5B%22%22%2C%22%22%2C1634209124%2C%22https%3A%2F%2Fwww.trafikverket.se%2F%22%5D; _pk_id.4.825a=e606dfd6dea155c5.1634209124.; _pk_ses.4.825a=1; ASP.NET_SessionId=aqjricrlem0553vt2tnddyzx; LoginValid=2021-10-14 13:46; FpsExternalIdentity=A9569078840C280755FC8AC99714EAF36A3D9235FB447B9D00C73B65EFD8C3BFA8E2FCB610747AA58501ED4590D7C6E0360374063E883224F829ECE58CAF3B7FB063A7603AB770028A0EAB20E576695064F27F740679011F566C96FC99131196858A14088A67A4981F540AD6CF595051D43F6E5304D877B610E5A8509CAD96361819EF4478AD9D3D0B1FBDD9FDEC9A5E3884E5C0B0655E986FB43458827D959723D50E588559590ECF5D859101BCA5AFA50C6E962B697A125B99FE391C397F0546E63503AA33ECCB57F699EAC5F4728FEA5ADB55E97DC248C7925992CFEBCC21AE8D26BC4E821E58FCC8BC0278B9B01F9310A64D562DA1E05F34F7CB2760C68261AB01EDC16757FF70073BFFB50E56EA79EBCDDF1F7DE5F932130E628C287AF151D7483D2EDC88C94C1711A7836225670E4FB6606E5E153C6ED8603C3CA8B5C340CBAD883794A95451A05ABA4058A535C646227BE43FF951D52200B46D29840462367293F148B313664D52DDAE5CD7136298C846D1E8746497B56047D2A2BBA90D2A8B54FF9FE69C69C4A7C5FA004A0A8B31E98D4B3F87A4D674E26BBE826814A4781906B0006ED6177D0CB83F359C41',
    'Host': 'fp.trafikverket.se',
    'Origin': 'https://fp.trafikverket.se',
    'Referer': 'https://fp.trafikverket.se/Boka/',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# README.md
payload_copy = """
{
    "bookingSession": {
        "socialSecurityNumber": "ÅÅÅÅMMDD-XXXX",
        "licenceId": 5,
        "bookingModeId": 0,
        "ignoreDebt": false,
        "ignoreBookingHindrance": false,
        "examinationTypeId": 0,
        "excludeExaminationCategories": [],
        "rescheduleTypeId": 0,
        "paymentIsActive": false,
        "paymentReference": null,
        "paymentUrl": null,
        "searchedMonths": 0
    },
    "occasionBundleQuery": {
        "startDate": "1970-01-01T00:00:00.000Z",
        "searchedMonths": 0,
        "locationId": 1000071,
        "nearbyLocationIds": [],
        "languageId": 13,
        "tachographTypeId": 1,
        "occasionChoiceId": 1,
        "examinationTypeId": 3
    }
}
"""

def main():
    global discord_webhook_url, payload_copy, headers, url
    webhook = Webhook.from_url(discord_webhook_url, adapter=RequestsWebhookAdapter())
    last_occasions_msg = ""

    print("Running...")

    while True:
        new_occasions_msg = ""
        r = requests.post(url, data=payload_copy, headers=headers)
        if r.status_code == 200:
            data = r.json()
            bundles_list = data['data']['bundles']
            for bundle in bundles_list:
                cost = bundle['cost']
                occasions = bundle['occasions'][0]
                new_occasions_msg += f'{occasions["name"]} i {occasions["locationName"]}\n{occasions["date"]} {occasions["time"]}\nKostar: {cost}\n\n'

            if new_occasions_msg != last_occasions_msg:
                webhook.send(new_occasions_msg)
            
            last_occasions_msg = new_occasions_msg
        else:
            print(f'Post request failed with status code {r.status_code}')

        time.sleep(10)

if __name__=='__main__':
    main()
