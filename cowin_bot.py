# District
#     Centers
#         sessions -- days

import requests
from datetime import datetime

base_cowin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
telegram_api = "https://api.telegram.org/bot1835528031:AAGkpikELBzrz6g4RTx8arF4Tmo6C15IGYA/sendMessage?chat_id=@__groupid__&text="
group_id = "Covid_Vaccine_Kerala"

# kerala_district_ids = [
#     295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308
# ]

kasaragod = 295
thiruvanthapuram = 296
kannur = 297
kollam = 298
wayanad = 299
pathanamthitta = 300
alappuzha = 301
malappuram = 302
thrissur = 303
kottayam = 304
kozhikode = 305
idukki = 306
ernakulam = 307
palakkad = 308


def fetch_district(district_id):
    query_param = "?district_id={}&date={}".format(district_id, today_date)
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    }
    final_url = base_cowin_url + query_param
    response = requests.get(final_url, headers=headers)
    extract_data(response)
    # print(response.text)


# def fetch_district_state(district_ids):
#     for district_id in district_ids:
#         fetch_district(district_id)


def extract_data(response):
    response_json = response.json()
    for center in response_json["centers"]:
        message = ""
        for session in center["sessions"]:
            message += "Pincode : {}, \nCenter_ID:{}, \nName: {}, \nDate: {}, \nVaccine: {}, \nFee: {} \nDose1: {}, \nDose2: {}, \nMinimum_Age: {} \n-------------\n".format(
                center["pincode"], center["center_id"], center["name"],
                session["date"], session["vaccine"], center["fee_type"],
                session["available_capacity_dose1"],
                session["available_capacity_dose2"], session["min_age_limit"])
        send_message_telegram(message)


def send_message_telegram(message):
    telegram_url = telegram_api.replace("__groupid__", group_id)
    telegram_url = telegram_url + message
    response = requests.get(telegram_url)
    print(response)


state = thrissur

if __name__ == "__main__":
    fetch_district(state)
