#-*- coding: utf-8 -*-
# created by P
import sys
if int(sys.version_info.major) == 2:
    py_version = 2
else:
    py_version = 3
    import urllib.parse as urlparse
from sdk import installtimenew, util
import time, random, json, string, urllib, uuid, hashlib
from spicipher import af_cipher,get_dlsdk_af_sig,get_cdn_token,get_gcd_sdk_af_sig
false = False
from datetime import datetime
true = True
null = None


campaign_data = {
   'package_name' : 'com.casualgamesonline.coinslotsgame',
   'app_name' : 'Age Of Coins: Master Of Spins',
   'app_version_name' : '0.39.30',
   'app_version_code' : '640',
   'supported_countries' : 'WW',
   'supported_os' : '10',
   'api_ver_name' : '37.9.18-29 [0] [PR] 571399392',
   'sig' : 'EE474049BA1CE065FB305E4D8AB8E399D9E63DF7422152BDA26CE885269608E8',
   'platformextension' : 'android_unity',
    'appsflyer' : { 
      'key' : 'SfS3aHyYXqqysfiF8Wf9eX',
      'buildnumber' : '6.10.3',
      'version' : 'v6.10',
      'spiKey' : 'DDBzvcI7SjtwatC0tUoq2uIAFQG8V5Nyoq3tgfQyOupUjfpPGC48I2vqCg0Gq0zd',
       #'spiKey' : 'wAFaze6ByucYudlWnUrdA+NpsRKLbOtGCwOnvIBn0El+HEr4czOofn9axktA+il2',#devkey
    },
   'link' : '',
    'app_size' : 11,
    'api_ver' : 83791820,
    'tracker' : ['appsflyer'],
    'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
    'retention' : {1: 85, 2: 82, 3: 80, 4: 78, 5: 75, 6: 72, 7: 70, 8: 68, 9: 65, 10: 60, 11: 55, 12: 50, 13: 45, 14: 40, 15: 35, 16: 33, 17: 30, 18: 28, 19: 26, 20: 20, 21: 19, 22: 18, 23: 17, 24: 16, 25: 15, 26: 14, 27: 13, 28: 12, 29: 11, 30: 10, 31: 9, 32: 8, 33: 7, 34: 6, 35: 5},
    }


Appsflyer_data = {"gcd_url": "lqakra-gcdsdk.appsflyersdk.com", "gcd_ver": "v5.0", "Key": "SfS3aHyYXqqysfiF8Wf9eX", "id": "com.casualgamesonline.coinslotsgame", "cdn_version": "v1", "cdn_url": "lqakra-cdn-settings.appsflyersdk.com", "build_number": "6.10.3", "con_url": "lqakra-conversions.appsflyersdk.com", "in_url": "lqakra-inapps.appsflyersdk.com", "la_url": "lqakra-launches.appsflyersdk.com", "att_url": null, "res_url": null}

register_data = {}

firebase_data = {"x-goog-api-key": "AIzaSyDSAEx8cuE2v9-_VHdFVcDU3usSqL8sFno", "x-firebase-client": "H4sIAAAAAAAAAFWRy5LCIBBFfyXFWkiAhY9fmbjA0HEoeVjQppyy_PfphKgzSw63D93Ng32DyXgCg4Udvh7MnCEiO7DRZeBDytC3qhNaqKYSX_pW7ghsKzDR-B90A2ElCXfNJaF3kVJiJ2TXmGhzcpYHF3mxF4qtqnEIdNBC_nHzOCf--5dySu4bC5MbgJ8ywb4tJpRbPL9oNIF6LWiyR7jfa7VbKiW98WnERQp5D7lvhxTEisUE0bqPLiQL_u1bbbXSoEtxXsOWvPrtvdLFmDINVdNIbZZryrgMJGmgV5KcZ8C6Da3ZhlmDMK-fqU5pLjsu9-z4PG7YBLnQY_Qfij1_ARCN_vSsAQAA", "X-Android-Cert": "E1355E93E4794ED70BAE93187A75BD1213CE379B", "data": {"fid": "e2Y2QgQnQoKASJGidliAm2", "appId": "1:971588350064:android:b68c9ea19cf09728ce04b5", "authVersion": "FIS_v2", "sdkVersion": "a:17.1.3"}, "url": "/v1/projects/coinslots-prod/installations"}

Event_name = {"event_name": ["funnel_game_start_by_player", "tutor_login_screen", "funnel_player_is_on_login_screen", "tutor_start_loading", "tutor_login_screen_accept", "af_login", "funnel_fb_login_successful", "tutor_finish_loading", "tutor_raid_chest_1", "tutor_raid_chest_2", "tutor_raid_chest_3", "tutor_raid_reward", "village_unlocked_2", "tutor_second_epoch_start", "af_level_achieved", "tutor_puzzles_and_wonders", "tutor_auto_spin_window", "tutor_event_window", "tutor_auto_spin", "tutor_attack_2_tap", "tutor_attack_2_reward", "tutor_betx_window", "tutor_betx", "tutor_raid_2_chest_1", "tutor_raid_2_chest_2", "tutor_raid_2_chest_3", "tutor_raid_2_reward", "village_unlocked_3", "af_tutorial_completion", "tutor_third_epoch_start", "af_level_achieved", "funnel_get_reward_for_fb_connect"]}

event_data = [{"funnel_game_start_by_player": {"af_param_2": "0", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_login_screen": {"af_param_2": "0", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"funnel_player_is_on_login_screen": {"af_param_2": "0", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_start_loading": {"af_param_2": "0", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_login_screen_accept": {"af_param_2": "0", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"af_login": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"funnel_fb_login_successful": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_finish_loading": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_chest_1": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_chest_2": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_chest_3": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_reward": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"village_unlocked_2": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_second_epoch_start": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"af_level_achieved": {"af_level": "2", "af_score": "1", "af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_puzzles_and_wonders": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_auto_spin_window": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_event_window": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_auto_spin": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_attack_2_tap": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_attack_2_reward": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_betx_window": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_betx": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_2_chest_1": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_2_chest_2": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_2_chest_3": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_raid_2_reward": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"village_unlocked_3": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"af_tutorial_completion": {"af_content": "Getting started", "af_content_id": "1", "af_success": "true", "af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"tutor_third_epoch_start": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"af_level_achieved": {"af_level": "3", "af_score": "1", "af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}, {"funnel_get_reward_for_fb_connect": {"af_param_2": "1102631", "af_param_1": "3e7fb5509363a56f4c0d708a04695cdf"}}]

conversion_data = {"advertiserId": "0bce225f-553c-4185-9ef2-321f95fe02f2", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1697695544805", "af_v": "9511e5e9094edacf4c96ee265a63b804f95d06f8", "af_v2": "9a820827dada853d6b3cfdb8ccb57df89a304505", "appUserId": "3e7fb5509363a56f4c0d708a04695cdf", "app_version_code": "640", "app_version_name": "0.39.30", "appsflyerKey": "SfS3aHyYXqqysfiF8Wf9eX", "batteryLevel": "18.0", "brand": "samsung", "carrier": "", "cell": {"mcc": 0, "mnc": 0}, "cksm_v1": "1cccefb4559344384fe32836279edfea54", "counter": "1", "country": "GB", "date1": "2023-10-19_111638+0530", "date2": "2023-10-19_111638+0530", "device": "starlte", "deviceData": {"arch": "", "btch": "ac", "btl": "18.0", "build_display_id": "QP1A.190711.020.G960FXXUHFVG4", "cpu_abi": "arm64-v8a", "cpu_abi2": "", "dim": {"d_dpi": "480", "size": "2", "x_px": "1080", "xdp": "428.625", "y_px": "2076", "ydp": "427.18124"}, "sensors": [{"sN": "LSM6DSL Gyroscope Sensor", "sT": 4, "sV": "STM"}, {"sN": "LSM6DSL Acceleration Sensor", "sT": 1, "sV": "STM", "sVE": [0.3232271, 4.249838, 8.901914], "sVS": [0.23224466, 4.2378664, 9.06233]}, {"sN": "AK09916C Magnetic field Sensor", "sT": 2, "sV": "Asahi Kasei Microdevices"}]}, "deviceType": "user", "disk": "4689/53254", "exception_number": 0, "fb": "8a9a959c-70c4-4c59-8fc8-328a5a4a6d3b", "firstLaunchDate": "2023-10-19_060544+0000", "iaecounter": "0", "installDate": "2023-10-19_054638+0000", "installer_package": "com.android.vending", "isFirstCall": "true", "isGaidWithGps": "true", "ivc": false, "kef7468": "10c5e08a6859b2a548181c1b0c531a0d591f1a0d5a1e1d", "lang": "English", "lang_code": "en", "last_boot_time": 1697693963183, "meta": {"first_launch": {"from_fg": 2042, "init_to_fg": 22, "start_with": "activity"}, "host": {"name": "appsflyersdk.com", "prefix": "lqakra-"}, "rc": {"c_ver": "default.v1.1637149529", "cdn_token": "3f7675a70c5bd7c5f659418c92e73e94d5f3b41092c863aa75593fb79ddac0e2", "delay": 1124, "latency": 1121, "res_code": 200, "sig": "success"}}, "model": "SM-G960F", "network": "WIFI", "onelink_id": "ZFlC", "open_referrer": "android-app://com.sec.android.app.launcher", "operator": "", "p_receipt": {"an": {"dbg": false, "hk": ";"}, "pr": {"aa": "exynos9810", "ac": "0", "ah": "zygote64_32", "ai": "0", "ak": "default", "al": "cortex-a53", "am": "default", "an": "cortex-a53", "ap": "dpi", "aq": "0", "ar": "samsungexynos9810", "as": "arm64-v8a", "at": "arm64-v8a,armeabi-v7a,armeabi", "au": "armeabi-v7a,armeabi", "av": "arm64-v8a"}}, "platform_extension_v2": {"platform": "android_unity", "version": "6.10.30"}, "platformextension": "android_unity", "product": "starltexx", "referrers": [{"api_ver": 83791820, "api_ver_name": "37.9.18-29 [0] [PR] 571399392", "click_ts": 1697694325, "google_custom": {"click_server_ts": 1697694328, "install_begin_server_ts": 1697694338, "install_version": "0.39.30", "instant": false}, "install_begin_ts": 1697694336, "latency": 10, "referrer": "utm_source=(not%20set)&utm_medium=(not%20set)", "response": "OK", "source": "google", "type": "store"}, {"api_ver": 661106110, "api_ver_name": "6.6.11.6", "latency": 41, "response": "SERVICE_UNAVAILABLE", "source": "samsung", "type": "store"}], "registeredUninstall": false, "rfr": {"clk": "1697694325", "code": "0", "install": "1697694336", "instant": false, "val": "utm_source=(not%20set)&utm_medium=(not%20set)"}, "sc_o": "p", "sdk": "29", "sdkExtension": "unity_android_6.4.4", "sig": "EE474049BA1CE065FB305E4D8AB8E399D9E63DF7422152BDA26CE885269608E8", "targetSDKver": 33, "timepassedsincelastlaunch": "-1", "tokenRefreshConfigured": false, "uid": "1697695544845-3050905540741303881"}

inapp_data = {"advertiserId": "0bce225f-553c-4185-9ef2-321f95fe02f2", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1697695544809", "af_v": "b0e78d316b5a68230faa53ad23280cfada254292", "af_v2": "dcb696fe78c93d027898a52ca7b8580d64915d15", "appUserId": "3e7fb5509363a56f4c0d708a04695cdf", "app_version_code": "640", "app_version_name": "0.39.30", "appsflyerKey": "SfS3aHyYXqqysfiF8Wf9eX", "brand": "samsung", "carrier": "", "cell": {"mcc": 0, "mnc": 0}, "cksm_v1": "e309cb349af2e21bef1795f476c35f73a0", "counter": "1", "country": "GB", "date1": "2023-10-19_111638+0530", "date2": "2023-10-19_111638+0530", "device": "starlte", "deviceData": {"arch": "", "build_display_id": "QP1A.190711.020.G960FXXUHFVG4", "cpu_abi": "arm64-v8a", "cpu_abi2": "", "dim": {"d_dpi": "480", "size": "2", "x_px": "1080", "xdp": "428.625", "y_px": "2076", "ydp": "427.18124"}}, "deviceType": "user", "disk": "4689/53254", "eventName": "funnel_game_start_by_player", "eventValue": "{\"af_param_2\":\"0\",\"af_param_1\":\"3e7fb5509363a56f4c0d708a04695cdf\"}", "fb": "8a9a959c-70c4-4c59-8fc8-328a5a4a6d3b", "firstLaunchDate": "2023-10-19_060544+0000", "iaecounter": "1", "installDate": "2023-10-19_054638+0000", "installer_package": "com.android.vending", "isFirstCall": "true", "isGaidWithGps": "true", "ivc": false, "kef7868": "4d041b37bd64f5dc48181c1b0c531a0d591f1a0d5a1e1b", "lang": "English", "lang_code": "en", "last_boot_time": 1697693963182, "model": "SM-G960F", "network": "WIFI", "operator": "", "p_receipt": {"an": {"dbg": false, "hk": ";"}, "pr": {"aa": "exynos9810", "ac": "0", "ah": "zygote64_32", "ai": "0", "ak": "default", "al": "cortex-a53", "am": "default", "an": "cortex-a53", "ap": "dpi", "aq": "0", "ar": "samsungexynos9810", "as": "arm64-v8a", "at": "arm64-v8a,armeabi-v7a,armeabi", "au": "armeabi-v7a,armeabi", "av": "arm64-v8a"}}, "platformextension": "android_unity", "product": "starltexx", "registeredUninstall": false, "sc_o": "p", "sdk": "29", "sdkExtension": "unity_android_6.4.4", "sensors": {"er": "na"}, "sig": "EE474049BA1CE065FB305E4D8AB8E399D9E63DF7422152BDA26CE885269608E8", "targetSDKver": 33, "tokenRefreshConfigured": false, "uid": "1697695544845-3050905540741303881"}



# ==================== Appsflyer Conversion ====================
def appsflyer_conversions( app_data, device_data ):

    inc_(app_data,'counter')
    def_(app_data,'iaecounter')
    set_batteryLevel(app_data)

    if not app_data.get('last_launch'):
        timeSinceLastCall = "-1"
    else:
        timeSinceLastCall = int(time.time())-app_data.get('last_launch')

    app_data['last_launch'] = int(time.time())

    method = "post"

    url = 'https://'+Appsflyer_data.get('con_url')+'/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

    headers = {
        "Accept-Encoding"   : "gzip",
        "Content-Type"      : "application/octet-stream",
        "User-Agent"        : get_ua(device_data)
    }

    params = {
        "app_id"        : campaign_data.get('package_name'),
        "buildnumber"   : campaign_data.get('appsflyer').get('buildnumber'),
    }
    
    if not app_data.get('disk'):
        app_data['disk'] = "{available}/{total}".format(available =str(random.randint(8000, 16000)), total = str(random.randint(23000, 32000)))
    else:
        temp_disk = map(int, app_data.get('disk').split('/'))
        temp_disk[0] += random.randint(-150, 300)

        app_data['disk'] = "{available}/{total}".format(available = str(temp_disk[0]), total = str(temp_disk[1]))
    app_data['session_time'] = time.time()

    data = {
        "advertiserId"          : device_data.get('adid'), 
        "advertiserIdEnabled"   : "true", 
        "af_events_api"         : "1", 
        "af_preinstalled"       : "false", 
        "af_timestamp"          : str(int(time.time()*1000)), 
        "app_version_code"      : campaign_data.get('app_version_code'),
        "app_version_name"      : campaign_data.get('app_version_name'),
        "appsflyerKey"          : campaign_data.get('appsflyer').get('key'),
        "batteryLevel"          : app_data.get('btl'), 
        "brand"                 : device_data.get('brand'), 
        "carrier"               : device_data.get('carrier'), 
        "cell": {
            "mcc"               : int(device_data.get('mcc')), 
            "mnc"               : int(device_data.get('mnc'))
        },  
        "counter"               : str(app_data.get('counter')), 
        "country"               : device_data.get('locale').get('country'), 
        "date1"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "date2"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "device"                : device_data.get('device'), 
        "deviceData"            :
         {
            "arch"              : "", 
            "btch"              : app_data.get('btch'), 
            "btl"               : app_data.get('btl'), 
            "build_display_id"  : device_data.get('build'), 
            "cpu_abi"           : device_data.get('cpu_abi'), 
            "cpu_abi2"          : device_data.get('cpu_abi2'), 
            "dim"               :
             {
                "d_dpi"         : device_data.get('dpi'), 
                "size"          : app_data.get('dim_size'), 
                "x_px"          : device_data.get('resolution').split('x')[1],
                "xdp"           : app_data.get('xdp'), 
                "y_px"          : device_data.get('resolution').split('x')[0], 
                "ydp"           : app_data.get('ydp')
            },
            "sensors":[{
                "sN": "ICM20607 Accelerometer",
                "sT": 1,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,1),10),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(8,10),6)
                ],
                "sVS": [
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(8,10),6)
                ]
            },
            {
                "sN": "ICM20607 Gyroscope",
                "sT": 4,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,-1),10),
                    round(random.uniform(0,-1),10),
                    round(random.uniform(0,1),10)
                ],
                "sVS": [
                    round(random.uniform(0,1),10),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,1),10)
                ]
            },
            {
                "sN": "ICM20607 Gyroscope -Wakeup Secondary",
                "sT": 4,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,1),11),
                    round(random.uniform(0,-1),11),
                    round(random.uniform(0,1),10)
                ],
                "sVS": [
                    round(random.uniform(0,1),11),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,1),10)
                ]
            },
            {
                "sN": "AK09918 Magnetometer -Wakeup Secondary",
                "sT": 2,
                "sV": "AKM",
                "sVE": [
                    round(random.uniform(-13,-11),6),
                    round(random.uniform(16,19),6),
                    round(random.uniform(-45,-42),5)
                ],
                "sVS": [
                    round(random.uniform(-13,-11),6),
                    round(random.uniform(16,19),6),
                    round(random.uniform(-45,-42),5)
                ]
            },
            {
                "sN": "ICM20607 Accelerometer -Wakeup Secondary",
                "sT": 1,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,1),11),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(8,10),6)
                ],
                "sVS": [
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,-1),8),
                    round(random.uniform(8,10),6)
                ]
            },
            {
                "sN": "AK09918 Magnetometer",
                "sT": 2,
                "sV": "AKM",
                "sVE": [
                    round(random.uniform(-14,-12),6),
                    round(random.uniform(18,21),6),
                    round(random.uniform(-45,-42),6)
                ],
                "sVS": [
                    round(random.uniform(-14,-12),6),
                    round(random.uniform(18,21),6),
                    round(random.uniform(-45,-42),6)
                ]
            }
        ]
        },
        "deviceType"        : "user", 
        "disk"              : app_data.get('disk'),
        "exception_number"  : 0,
        "iaecounter"        : str(app_data.get('iaecounter')), 
        "installDate"       : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000', 
        "installer_package" : "com.android.vending", 
        "isFirstCall"       : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"     : "true", 
        "ivc"               : False, 
        "lang"              : "English", 
        "lang_code"         : "en", 
        "last_boot_time"    : app_data.get('last_boot_time'),
        "meta": {
            "first_launch": {
                "init_to_fg": random.randint(5,20)
            }
        },
        "model"             : device_data.get('model'), 
        "network"           : device_data.get('network').upper(), 
        "open_referrer"     : "android-app://"+campaign_data.get("package_name"), 
        "operator"          : device_data.get('carrier'), 
        "p_receipt"         :
             {
            "an": {
                "dbg"       : False, 
                "hk"        : ";"
            }, 
            "as"            :
                {
                "cav": random.randint(5,40),
                "null": random.randint(5,35),
                "other": random.randint(5,15)
            },
            "pr":{
                "ac": "0",
                "ah": "zygote64_32",
                "ai": "0",
                "ak": "default",
                "al": "cortex-a53",
                "am": "default",
                "an": "generic",
                "ap": "builder",
                "ar": "qcom",
                "as": device_data.get('cpu_abi'),
                "at": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "au": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "av": device_data.get('cpu_abi')
            }
        }, 
        "platformextension"         : campaign_data.get("platformextension"), 
        "product"                   : device_data.get('product'), 
        "referrers": [
        {
            "api_ver": campaign_data.get('api_ver'), 
            "api_ver_name": campaign_data.get('api_ver_name'), 
            "click_ts": int(app_data.get('times').get('click_time')),  
            "google_custom": { 
                "click_server_ts": int(app_data.get('times').get('click_time'))-1, 
                "install_begin_server_ts": int(app_data.get('times').get('download_begin_time'))-2, 
                "install_version": campaign_data.get('app_version_name'), 
                "instant": False
                },
            "install_begin_ts"  : int(app_data.get('times').get('download_begin_time')), 
            "latency"           : 92,
            "referrer"          : app_data.get("referrer") or "utm_source=(not%20set)&utm_medium=(not%20set)", 
            "response"          : "OK", 
            "source"            : "google", 
            "type"              : "store"
        }
        ], 
        "registeredUninstall"       : False, 
        "rfr"                       :
         {  
            "clk"                   : str(int(app_data.get('times').get('click_time'))), 
            "code"                  : "0", 
            "install"               : str(int(app_data.get('times').get('download_begin_time'))),
            "instant"               : False,
            "val"                   : app_data.get("referrer") or "utm_source=(not%20set)&utm_medium=(not%20set)"
        },  
        "sc_o"                      : "l", 
        "sdk"                       : device_data.get('sdk'), 
        "timepassedsincelastlaunch" : str(timeSinceLastCall), 
        "tokenRefreshConfigured"    : False, 
    }

    if campaign_data.get('sig'):
        data["sig"]  = campaign_data.get("sig")


    if conversion_data.get('android_id'):
        data['android_id'] = device_data.get('android_id')
    if conversion_data.get('appUserId'):
        data['appUserId'] = app_data.get('appUserId')
    if conversion_data.get('customData'):
        data['customData'] = app_data.get('customData')
    if conversion_data.get('fb'): 
        data['fb'] =  app_data.get('fb')
    if conversion_data.get('user_emails'): 
        data['user_emails'] = app_data.get('user_emails')
    if conversion_data.get('sdkExtension'): 
        data['sdkExtension'] = conversion_data.get('sdkExtension')
    


    data['uid']                 = app_data.get('uid')
    data['firstLaunchDate']     = app_data.get('firstLaunchDate')
    data['cksm_v1']             = cksm_v1(data['date1'],data['af_timestamp'])
    data['af_v']                = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']               = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))

    

    if app_data.get('counter') > 2:
        del data['deviceData']['sensors']
        if data.get('rfr'):
            del data['rfr']
        if data.get('p_receipt'):
            del data['p_receipt']

    if data.get('isFirstCall')=="false":
        del data['batteryLevel']
        data['open_referrer']="android-app://"+campaign_data.get("package_name")            

    kefdata = get_kef_data(app_data, data)
    data[kefdata[0]] = kefdata[1]

    if Appsflyer_data.get('cdn'):
        data['meta'] = conversion_meta(app_data)



    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data,separators = (',',':')))}



# ==================== Appsflyer Launches ====================
def appsflyer_launches( app_data, device_data ):

    inc_(app_data,'counter')
    def_(app_data,'iaecounter')
    set_batteryLevel(app_data)

    if not app_data.get('last_launch'):
        timeSinceLastCall = "-1"
    else:
        timeSinceLastCall = int(time.time())-app_data.get('last_launch')

    app_data['last_launch'] = int(time.time())

    method = "post"

    url = 'https://'+Appsflyer_data.get('la_url')+'/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

    headers = {
        "Accept-Encoding"  : "gzip",
        "Content-Type"     : "application/octet-stream",
        "User-Agent"       : get_ua(device_data)
    }

    params = {
        "app_id"        : campaign_data.get('package_name'),
        "buildnumber"   : campaign_data.get('appsflyer').get('buildnumber'),
    } 
    if not app_data.get('disk'):
        app_data['disk'] = "{available}/{total}".format(available =str(random.randint(8000, 16000)), total = str(random.randint(23000, 32000)))
    else:
        temp_disk = map(int, app_data.get('disk').split('/'))
        temp_disk[0] += random.randint(-150, 300)

        app_data['disk'] = "{available}/{total}".format(available = str(temp_disk[0]), total = str(temp_disk[1]))


    data = {
        "advertiserId"          : device_data.get('adid'), 
        "advertiserIdEnabled"   : "true", 
        "af_events_api"         : "1", 
        "af_preinstalled"       : "false", 
        "af_timestamp"          : str(int(time.time()*1000)), 
        "app_version_code"      : campaign_data.get('app_version_code'),
        "app_version_name"      : campaign_data.get('app_version_name'),
        "appsflyerKey"          : campaign_data.get('appsflyer').get('key'),
        "brand"                 : device_data.get('brand'), 
        "carrier"               : device_data.get('carrier'), 
        "cell"                  :
         {
            "mcc"               : int(device_data.get('mcc')), 
            "mnc"               : int(device_data.get('mnc'))
        },  
        "counter"               : str(app_data.get('counter')), 
        "country"               : device_data.get('locale').get('country'), 
        "date1"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "date2"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "device"                : device_data.get('device'), 
        "deviceData"            :
         {
            "arch"              : "", 
            "btch"              : app_data.get('btch'), 
            "btl"               : app_data.get('btl'), 
            "build_display_id"  : device_data.get('build'), 
            "cpu_abi"           : device_data.get('cpu_abi'), 
            "cpu_abi2"          : device_data.get('cpu_abi2'), 
            "dim"               :
             {
                "d_dpi"         : device_data.get('dpi'), 
                "size"          : app_data.get('dim_size'), 
                "x_px"          : device_data.get('resolution').split('x')[1],
                "xdp"           : app_data.get('xdp'), 
                "y_px"          : device_data.get('resolution').split('x')[0], 
                "ydp"           : app_data.get('ydp')
            },
            "sensors":  [{
                "sN": "ICM20607 Accelerometer",
                "sT": 1,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,1),10),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(8,10),6)
                ],
                "sVS": [
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(8,10),6)
                ]
            },
            {
                "sN": "ICM20607 Gyroscope",
                "sT": 4,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,-1),10),
                    round(random.uniform(0,-1),10),
                    round(random.uniform(0,1),10)
                ],
                "sVS": [
                    round(random.uniform(0,1),10),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,1),10)
                ]
            },
            {
                "sN": "ICM20607 Gyroscope -Wakeup Secondary",
                "sT": 4,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,1),11),
                    round(random.uniform(0,-1),11),
                    round(random.uniform(0,1),10)
                ],
                "sVS": [
                    round(random.uniform(0,1),11),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,1),10)
                ]
            },
            {
                "sN": "AK09918 Magnetometer -Wakeup Secondary",
                "sT": 2,
                "sV": "AKM",
                "sVE": [
                    round(random.uniform(-13,-11),6),
                    round(random.uniform(16,19),6),
                    round(random.uniform(-45,-42),5)
                ],
                "sVS": [
                    round(random.uniform(-13,-11),6),
                    round(random.uniform(16,19),6),
                    round(random.uniform(-45,-42),5)
                ]
            },
            {
                "sN": "ICM20607 Accelerometer -Wakeup Secondary",
                "sT": 1,
                "sV": "InvenSense",
                "sVE": [
                    round(random.uniform(0,1),11),
                    round(random.uniform(0,-1),9),
                    round(random.uniform(8,10),6)
                ],
                "sVS": [
                    round(random.uniform(0,-1),9),
                    round(random.uniform(0,-1),8),
                    round(random.uniform(8,10),6)
                ]
            },
            {
                "sN": "AK09918 Magnetometer",
                "sT": 2,
                "sV": "AKM",
                "sVE": [
                    round(random.uniform(-14,-12),6),
                    round(random.uniform(18,21),6),
                    round(random.uniform(-45,-42),6)
                ],
                "sVS": [
                    round(random.uniform(-14,-12),6),
                    round(random.uniform(18,21),6),
                    round(random.uniform(-45,-42),6)
                ]
            }
        ]
        },
        "deviceType"        : "user", 
        "disk"              : app_data.get('disk'),
        "exception_number"  : 0,
        "iaecounter"        : str(app_data.get('iaecounter')),
        "installDate"       : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000', 
        "installer_package" : "com.android.vending", 
        "isFirstCall"       : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"     : "true", 
        "ivc"               : False, 
        "lang"              : "English", 
        "lang_code"         : "en", 
        "last_boot_time"    : app_data.get('last_boot_time'),
        "meta": {
            "first_launch": {
            "from_fg": 960, 
            "init_to_fg": 9, 
            "net": 12605
            }
        }, 
        "model"             : device_data.get('model'), 
        "network"           : device_data.get('network').upper(), 
        "open_referrer"     : "android-app://"+campaign_data.get("package_name"), 
        "operator"          : device_data.get('carrier'), 
        "p_receipt"         :
         {
            "an": {
                "dbg"       : False, 
                "hk"        : ";"
            }, 
            "as"            :
                {
                "cav": random.randint(5,40),
                "null": random.randint(5,35),
                "other": random.randint(5,15)
            },
            "pr":{
                "ac": "0",
                "ah": "zygote64_32",
                "ai": "0",
                "ak": "default",
                "al": "cortex-a53",
                "am": "default",
                "an": "generic",
                "ap": "builder",
                "ar": "qcom",
                "as": device_data.get('cpu_abi'),
                "at": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "au": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "av": device_data.get('cpu_abi')
            }
        }, 
        "platformextension"    : campaign_data.get("platformextension"), 
        "product"              : device_data.get('product'), 
        "referrers": [
        {
            "api_ver": campaign_data.get('api_ver'), 
            "api_ver_name": campaign_data.get('api_ver_name'), 
            "click_ts": int(app_data.get('times').get('click_time')),  
            "google_custom": { 
                "click_server_ts": int(app_data.get('times').get('click_time'))-1, 
                "install_begin_server_ts": int(app_data.get('times').get('download_begin_time'))-2, 
                "install_version": campaign_data.get('app_version_name'), 
                "instant": False
                },
            "install_begin_ts": int(app_data.get('times').get('download_begin_time')), 
            "latency": 92,
            "referrer":app_data.get("referrer") or "utm_source=(not%20set)&utm_medium=(not%20set)", 
            "response": "OK", 
            "source": "google", 
            "type": "store"
        }
        ], 
        "registeredUninstall"       : False, 
        "rfr"                       :
         {
            "clk"                   : str(int(app_data.get('times').get('click_time'))), 
            "code"                  : "0", 
            "install"               : str(int(app_data.get('times').get('download_begin_time'))), 
            "instant"               : False,
            "val"                   : app_data.get("referrer") or "utm_source=(not%20set)&utm_medium=(not%20set)"
        }, 
        "sc_o"                      : "l", 
        "sdk"                       : device_data.get('sdk'), 
        # "sig"                       : campaign_data.get("sig"), 
        "timepassedsincelastlaunch" : str(timeSinceLastCall), 
        "tokenRefreshConfigured"    : False, 
    }

    if campaign_data.get('sig'):
        data["sig"]  = campaign_data.get("sig")

    if conversion_data.get('android_id'):
        data['android_id'] = device_data.get('android_id')
    if conversion_data.get('appUserId'):
        data['appUserId'] = app_data.get('appUserId')
    if conversion_data.get('customData'):
        data['customData'] = app_data.get('customData')
    if conversion_data.get('fb'): 
        data['fb'] =  app_data.get('fb')
    if conversion_data.get('user_emails'): 
        data['user_emails'] = app_data.get('user_emails')
    if conversion_data.get('sdkExtension'): 
        data['sdkExtension'] = conversion_data.get('sdkExtension')
    

    data['uid']                = app_data.get('uid')
    data['firstLaunchDate']    = app_data.get('firstLaunchDate')
    data['cksm_v1']            = cksm_v1(data['date1'],data['af_timestamp'])
    data['af_v']               = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']              = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))

    if int(app_data.get('counter')) > 2:
        del data['deviceData']['sensors']
        if data.get("referrers"):
            del data["referrers"]
        if data.get('rfr'):
            del data['rfr']
        if data.get('p_receipt'):
            del data['p_receipt']

    kefdata = get_kef_data(app_data, data)
    data[kefdata[0]] = kefdata[1]

    if app_data.get('session_time'):
        data['prev_session_dur'] = int(time.time()- app_data.get('session_time'))

    app_data['session_time'] = time.time()

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data,separators = (',',':')))}

# ==================== Appsflyer Inapps ====================
def appsflyer_inapps( app_data, device_data, eventname= "", eventvalue= "" ):

    def_(app_data,'counter')
    inc_(app_data,'iaecounter')

    method = "post"

    url = 'https://'+Appsflyer_data.get('in_url')+'/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

    headers = {
        "Accept-Encoding":"gzip",
        "Content-Type":"application/octet-stream",
        "User-Agent":get_ua(device_data)
    }

    params = {
        "app_id":campaign_data.get('package_name'),
        "buildnumber":campaign_data.get('appsflyer').get('buildnumber'),
    }
    if not app_data.get('disk'):
        app_data['disk'] = "{available}/{total}".format(available =str(random.randint(8000, 16000)), total = str(random.randint(23000, 32000)))
    else:
        temp_disk = map(int, app_data.get('disk').split('/'))
        temp_disk[0] += random.randint(-150, 300)

        app_data['disk'] = "{available}/{total}".format(available = str(temp_disk[0]), total = str(temp_disk[1]))


    data = {
        "advertiserId"          : device_data.get('adid'), 
        "advertiserIdEnabled"   : "true", 
        "af_events_api"         : "1", 
        "af_preinstalled"       : "false", 
        "af_timestamp"          : str(int(time.time()*1000)), 
        "app_version_code"      : campaign_data.get('app_version_code'),
        "app_version_name"      : campaign_data.get('app_version_name'),
        "appsflyerKey"          : campaign_data.get('appsflyer').get('key'),
        "appUserId"             : app_data.get('appUserId'),
        "brand"                 : device_data.get('brand'), 
        "carrier"               : device_data.get('carrier'),
        "cell"                  :
            {
            "mcc"               : int(device_data.get('mcc')), 
            "mnc"               : int(device_data.get('mnc'))
        },  
        "counter"               : str(app_data.get('counter')), 
        "country"               : device_data.get('locale').get('country'), 
        "date1"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "date2"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "device"                : device_data.get('device'), 
        "deviceData"            :
            {
            "arch"              : "", 
            "build_display_id"  : device_data.get('build'), 
            "cpu_abi"           : device_data.get('cpu_abi'), 
            "cpu_abi2"          : device_data.get('cpu_abi2'), 
            "dim"               :
                {
                "d_dpi"         : device_data.get('dpi'), 
                "size"          : app_data.get('dim_size'), 
                "x_px"          : device_data.get('resolution').split('x')[1],
                "xdp"           : app_data.get('xdp'), 
                "y_px"          : device_data.get('resolution').split('x')[0], 
                "ydp"           : app_data.get('ydp')
            }
        },
        "deviceType"            : "user", 
        "disk"                  : app_data.get('disk'),
        "eventName"             : eventname, 
        "eventValue"            : json.dumps(eventvalue,separators = (',',':')), 
        "iaecounter"            : str(app_data.get('iaecounter')), 
        "installDate"           : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000', 
        "installer_package"     : "com.android.vending", 
        "isFirstCall"           : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"         : "true", 
        "ivc"                   : False, 
        "lang"                  : "English", 
        "lang_code"             : "en", 
        "last_boot_time"        : app_data.get('last_boot_time'),
        "model"                 : device_data.get('model'), 
        "network"               : device_data.get('network').upper(), 
        "operator"              : device_data.get('carrier'), 
        "p_receipt"             :
            {
            "an": {
                "dbg"           : False, 
                "hk"            : ";"
            }, 
            "as"            :
                {
                    "cav": random.randint(5,40),
                    "null": random.randint(5,35),
                    "other": random.randint(5,15)
                },
            "pr":{
                "ac": "0",
                "ah": "zygote64_32",
                "ai": "0",
                "ak": "default",
                "al": "cortex-a53",
                "am": "default",
                "an": "generic",
                "ap": "builder",
                "ar": "qcom",
                "as": device_data.get('cpu_abi'),
                "at": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "au": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "av": device_data.get('cpu_abi')
            }
        }, 
        "platformextension"     : campaign_data.get("platformextension"), 
        "prev_event"            : "",
        "product"               : device_data.get('product'),
        "registeredUninstall"   : False, 
        # "sdkExtension"          : "unity_android_6.1.4",
        "sc_o"                  : "l", 
        "sdk"                   : device_data.get('sdk'), 
        "sensors"               :
            {
            "am": {
                "n": "ICM20607 Accelerometer -Wakeup Secondary",
                "v": [
                    [
                        0,
                        0,
                        9.6
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ]
            },
            "er": "no_svs",
            "gs": {
                "n": "ICM20607 Gyroscope -Wakeup Secondary",
                "v": [
                    [
                        0,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ]
            },
            "mm": {
                "n": "AK09918 Magnetometer",
                "v": [
                    [
                        -7,
                        -389.3
                    ],
                    []
                ]
            }
        },
        # "sig"                    : campaign_data.get("sig"), 
        "tokenRefreshConfigured" : False, 
    }

    if campaign_data.get('sig'):
        data["sig"]  = campaign_data.get("sig")

    if inapp_data.get('android_id'):
        data['android_id'] = device_data.get('android_id')
    if inapp_data.get('appUserId'):
        data['appUserId'] = app_data.get('appUserId')
    if inapp_data.get('customData'):
        data['customData'] = app_data.get('customData')
    if inapp_data.get('fb'): 
        data['fb'] =  app_data.get('fb')
    if inapp_data.get('user_emails'): 
        data['user_emails'] = app_data.get('user_emails')
    if inapp_data.get('sdkExtension'): 
        data['sdkExtension'] = inapp_data.get('sdkExtension')
    

    data['uid']             = app_data.get('uid')
    data['firstLaunchDate'] = app_data.get('firstLaunchDate')
    data['cksm_v1']         = cksm_v1(data['date1'],data['af_timestamp'])
    data['af_v']            = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']           = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))


    if not app_data.get('prev_event'):
        del data['prev_event']
    else:
        data['prev_event'] = json.dumps(app_data.get('prev_event'),separators = (',',':'))

    if app_data.get('counter') > 2:
        if data.get('p_receipt'):
            del data['p_receipt']



    # if app_data.get('iaecounter')==1:
    #     data["sensors"]= {"er": "na"}







    update_event_records( app_data, data.get('eventName'), data.get('eventValue'), data.get('af_timestamp'))

    kefdata = get_kef_data(app_data, data)
    data[kefdata[0]] = kefdata[1]

    # if app_data.get('session_time'):
    #     data['prev_session_dur'] = int(time.time()- app_data.get('session_time'))


    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data,separators = (',',':')))}

# ==================== Appsflyer Register ====================
def appsflyer_register( app_data, device_data ):

    method = 'post'

    url = 'https://'+Appsflyer_data.get('res_url')+'/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

    headers = {
        'Accept-Encoding'   : 'gzip',
        'Content-Type'      : 'application/json',
        'User-Agent'        : get_ua(device_data)
    }

    params = {
        'app_id'        : campaign_data.get('package_name'),
        'buildnumber'   : campaign_data.get('appsflyer').get('buildnumber')
    }

    data = {
        'advertiserId'     : device_data.get('adid'),
        'af_gcm_token'     : app_data.get('af_gcm_token'),
        'app_name'         : campaign_data.get('app_name'),
        'app_version_code' : campaign_data.get('app_version_code'),
        'app_version_name' : campaign_data.get('app_version_name'),
        'brand'            : device_data.get('brand'),
        'carrier'          : device_data.get('carrier'),
        'devkey'           : campaign_data.get('appsflyer').get('key'),
        'installDate'      : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000',
        'launch_counter'   : str(app_data.get('counter')),
        'model'            : device_data.get('model'),
        'network'          : device_data.get('network').upper(),
        'operator'         : device_data.get('carrier'),
        'sdk'              : device_data.get('sdk'),

    }
    if register_data.get('kef9999'):
        data['kef9999'] = "babeae0540d91f201848191d1b0c531a0d5918190d5a1b"
    
    if register_data.get('appUserId'):
        data['appUserId'] = app_data.get('appUserId')



    # if not app_data.get('af_gcm_token'):
    #     app_data['af_gcm_token'] = util.get_random_string(type='all', size=22)+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(134))

    data['uid'] = app_data.get('uid')
    data['af_gcm_token'] = app_data.get('af_gcm_token')

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': json.dumps(data,separators = (',',':'))}

# ==================== Appsflyer GCDSDK ====================
def appsflyer_gcdsdk( app_data, device_data ):

    method = "get"

    url = 'https://'+Appsflyer_data.get('gcd_url')+'/install_data/'+Appsflyer_data.get('gcd_ver')+'/'+campaign_data.get('package_name')

    headers = {
        "Accept-Encoding" : "gzip",
        "User-Agent" : get_ua(device_data)
    }
    
    params = {
        "device_id" : app_data.get('uid'),
        "devkey" : campaign_data.get('appsflyer').get('key')
    }


    params['device_id'] = app_data.get('uid')

    if Appsflyer_data.get('gcd_ver') == "v5.0":
        af_request_epoch_ms = str(int(time.time()*1000))
        headers['af_request_epoch_ms'] = af_request_epoch_ms
        headers['af_sig'] = get_gcd_sdk_af_sig(package_name=campaign_data.get('package_name'),af_key=campaign_data.get('appsflyer').get('key'),uid=app_data.get('uid'),af_request_epoch_ms=af_request_epoch_ms)
        del params['devkey']
    data = {}

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': data}





def attr_appsflyer( app_data, device_data ):
    
    inc_(app_data,'counter')
    def_(app_data,'iaecounter')
    set_batteryLevel(app_data)

    if not app_data.get('last_launch'):
        timeSinceLastCall = "-1"
    else:
        timeSinceLastCall = int(time.time())-app_data.get('last_launch')

    app_data['last_launch'] = int(time.time())

    method = "post"

    url = 'https://'+Appsflyer_data.get('att_url')+'/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

    headers = {
        "Accept-Encoding"  : "gzip",
        "Content-Type"     : "application/octet-stream",
        "User-Agent"       : get_ua(device_data)
    }

    params = {
        "app_id"        : campaign_data.get('package_name'),
        "buildnumber"   : campaign_data.get('appsflyer').get('buildnumber'),
    } 
    if not app_data.get('disk'):
        app_data['disk'] = "{available}/{total}".format(available =str(random.randint(8000, 16000)), total = str(random.randint(23000, 32000)))
    else:
        temp_disk = map(int, app_data.get('disk').split('/'))
        temp_disk[0] += random.randint(-150, 300)

        app_data['disk'] = "{available}/{total}".format(available = str(temp_disk[0]), total = str(temp_disk[1]))


    data = {
        "advertiserId"          : device_data.get('adid'), 
        "advertiserIdEnabled"   : "true", 
        "af_events_api"         : "1", 
        "af_preinstalled"       : "false", 
        "af_timestamp"          : str(int(time.time()*1000)),
        "app_version_code"      : campaign_data.get('app_version_code'),
        "app_version_name"      : campaign_data.get('app_version_name'),
        "appsflyerKey"          : campaign_data.get('appsflyer').get('key'),
        "brand"                 : device_data.get('brand'), 
        "carrier"               : device_data.get('carrier'), 
        "cell"                  :
            {
                "mcc"           : int(device_data.get('mcc')), 
                "mnc"           : int(device_data.get('mnc'))
            }, 
        "counter"               : str(app_data.get('counter')), 
        "country"               : device_data.get('locale').get('country'), 
        "date1"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "date2"                 : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).strftime('%Y-%m-%d_%H%M%S')+device_data.get('timezone'), 
        "device"                : device_data.get('device'), 
        "deviceData"            :
         {
            "arch"              : "", 
            "btch"              : app_data.get('btch'), 
            "btl"               : app_data.get('btl'), 
            "build_display_id"  : device_data.get('build'), 
            "cpu_abi"           : device_data.get('cpu_abi'), 
            "cpu_abi2"          : device_data.get('cpu_abi2'), 
            "dim"               :
             {
                "d_dpi"         : device_data.get('dpi'), 
                "size"          : app_data.get('dim_size'), 
                "x_px"          : device_data.get('resolution').split('x')[1],
                "xdp"           : app_data.get('xdp'), 
                "y_px"          : device_data.get('resolution').split('x')[0], 
                "ydp"           : app_data.get('ydp')
            },
            "sensors":  [{
                "sN": "ICM20607 Accelerometer",
                "sT": 1,
                "sV": "InvenSense"
            },
            {
                "sN": "ICM20607 Gyroscope",
                "sT": 4,
                "sV": "InvenSense"
            },
            {
                "sN": "ICM20607 Gyroscope -Wakeup Secondary",
                "sT": 4,
                "sV": "InvenSense"
            },
            {
                "sN": "AK09918 Magnetometer -Wakeup Secondary",
                "sT": 2,
                "sV": "AKM"
            },
            {
                "sN": "ICM20607 Accelerometer -Wakeup Secondary",
                "sT": 1,
                "sV": "InvenSense"
            },
            {
                "sN": "AK09918 Magnetometer",
                "sT": 2,
                "sV": "AKM",
                "sVS": [
                    201.45416,
                    60.188293,
                    -428.685
                ]
            }
        ]
        },
        "deviceType"        : "user", 
        "disk"              : app_data.get('disk'),
        "exception_number"  : 0,
        "iaecounter"        : str(app_data.get('iaecounter')),
        "installDate"       : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000', 
        "installer_package" : "com.android.vending", 
        "isFirstCall"       : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"     : "true", 
        "ivc"               : False, 
        "lang"              : "English", 
        "lang_code"         : "en", 
        "last_boot_time"    : app_data.get('last_boot_time'),
        "meta"              : {},
        "model"             : device_data.get('model'), 
        "network"           : device_data.get('network').upper(), 
        "open_referrer"     : "android-app://"+campaign_data.get("package_name"), 
        "operator"          : device_data.get('carrier'), 
        "p_receipt"         :
         {
            "an": {
                "dbg"       : False, 
                "hk"        : ";"
            }, 
            "as": {
                "cav": 1,
                "null": 270,
                "other": 43
            },
            "pr": {
                "ac": "0",
                "ah": "zygote64_32",
                "ai": "0",
                "ak": "default",
                "al": "cortex-a53",
                "am": "default",
                "an": "generic",
                "ap": "builder",
                "ar": "qcom",
                "as": device_data.get('cpu_abi'),
                "at": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "au": device_data.get('cpu_abi')+ ',' +device_data.get('cpu_abi2'),
                "av": device_data.get('cpu_abi')
            }
        }, 
        "platformextension"         : campaign_data.get("platformextension"), 
        "product"                   : device_data.get('product'),
        "referrers": [
        {
            "api_ver"       : campaign_data.get('api_ver'), 
            "api_ver_name"  : campaign_data.get('api_ver_name'), 
            "click_ts"      : int(app_data.get('times').get('click_time')),  
            "google_custom" :
                {
                "click_server_ts"           : int(app_data.get('times').get('click_time'))-1, 
                "install_begin_server_ts"   : int(app_data.get('times').get('download_begin_time'))-2, 
                "install_version"           : campaign_data.get('app_version_name'), 
                "instant"                   : False
                },
            "install_begin_ts"  : int(app_data.get('times').get('download_begin_time')), 
            "latency"           : 92,
            "referrer"          : app_data.get("referrer") or "utm_source=(not%20set)&utm_medium=(not%20set)", 
            "response"          : "OK", 
            "source"            : "google", 
            "type"              : "store"
        }
        ],
        "registeredUninstall"       : False, 
        "rfr"                       :
         {
            "clk"                   : str(int(app_data.get('times').get('click_time'))), 
            "code"                  : "0", 
            "install"               : str(int(app_data.get('times').get('download_begin_time'))), 
            "instant"               : False,
            "val"                   : app_data.get("referrer") or "utm_source=(not%20set)&utm_medium=(not%20set)"
        }, 
        "sc_o"                      : "l", 
        "sdk"                       : device_data.get('sdk'), 
        "sig"                       : campaign_data.get("sig"), 
        "timepassedsincelastlaunch" : "0", 
        "tokenRefreshConfigured"    : False, 
    }



    data['uid']                = app_data.get('uid')
    data['firstLaunchDate']    = app_data.get('firstLaunchDate')
    data['cksm_v1']            = cksm_v1(data['date1'],data['af_timestamp'])
    data['af_v']               = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']              = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))

    if int(app_data.get('counter')) > 2:
        del data['deviceData']['sensors']
        if data.get("referrers"):
            del data["referrers"]
        if data.get('rfr'):
            del data['rfr']
        if data.get('p_receipt'):
            del data['p_receipt']

    kefdata = get_kef_data(app_data, data)
    data[kefdata[0]] = kefdata[1]

    if app_data.get('session_time'):
        data['prev_session_dur'] = int(time.time()- app_data.get('session_time'))

    app_data['session_time'] = time.time()

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data,separators = (',',':')))}



def appsflyer_dlsdk(app_data,device_data):

    url = "https://"+Appsflyer_data.get('dlsdk_url')+"/v1.0/android/"+campaign_data.get('package_name')
    method = "post"
    headers = {
    "Content-Type":"application/json",
    "User-Agent":get_ua(device_data),
    "Accept-Encoding":"gzip",
    }

    params = {
        "af_sig":'06aa74825006f9a1874fc637751d66e033954f764a1d303b50791bc5514525fa',
        'sdk_version': campaign_data.get('appsflyer').get('version').replace('v','')
    }

    data_dict = {
                "os":device_data.get('os_version'),
                "gaid": {
                            "type":"unhashed",
                            "value":str(uuid.uuid4())
                        },
                "is_first":True,
                "lang":"en-IN",
                "type":device_data.get('model'),
                "request_id":app_data.get('uid'),
                "timestamp":app_data.get('dlsdk_timestamp'),
                "request_count":1
            }
    if app_data.get('referrer'):
        data_dict["referrers"] = [{
                        "source": "google",
                        "value": app_data.get('referrer')
                    }]
    params['af_sig'] = get_dlsdk_af_sig(package_name=campaign_data.get('package_name'),af_key=campaign_data.get('appsflyer').get('key'),data_dict=data_dict)
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':json.dumps(data_dict)}


def appsflyer_cdn( app_data, device_data ):
    if Appsflyer_data.get('cdn_version') != "v1":
        print("change cdn version")
        exit()

    method = 'get'
    app_data['cdn_token']=get_cdn_token(campaign_data.get('package_name'),campaign_data.get('appsflyer').get('key'))
    url = 'https://'+Appsflyer_data.get('cdn_url')+'/android/v1/'+str(app_data.get('cdn_token'))+'/settings'

    headers = {
    "Content-Type": "application/json",
    'User-Agent':get_ua(device_data),
    'Accept-Encoding': "gzip"
    }


    params ={}

    data = {}


    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': data}


def firebase_installations( app_data, device_data ):
	method = "post"
	url = 'https://firebaseinstallations.googleapis.com'+firebase_data.get('url')

	headers = {
		'Content-Type':"application/json",
		'Accept':"application/json",
		'Cache-Control':"no-cache",
		'X-Android-Package':campaign_data.get('package_name'),
		'x-firebase-client':firebase_data.get('x-firebase-client'),
		'X-Android-Cert':firebase_data.get('X-Android-Cert'),
		'x-goog-api-key':firebase_data.get('x-goog-api-key'),
		'User-Agent':get_ua(device_data),
		'Connection':"Keep-Alive",
		'Accept-Encoding':"gzip"
	}

	data ={
		"fid": app_data.get('fid'),
		"appId":firebase_data.get('data').get('appId') ,
		"authVersion": firebase_data.get('data').get('authVersion'),
		"sdkVersion": firebase_data.get('data').get('sdkVersion')
	}
	
	return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}







#==============================================================================
def install(app_data, device_data): 

   
    if not app_data.get('times'):
        # print "Please wait installing..."
        installtimenew.main(app_data, device_data, app_size=campaign_data.get('app_size'),os='android')
        def_sec(app_data,device_data)
        app_data['uid'] = '{0}-{1}'.format(int(time.time()*1000), random.getrandbits(64))
        set_batteryLevel(app_data)
        set_deviceData(app_data)
        app_data['last_boot_time'] = int(time.time()*1000 - random.randint(20000, 30000))
        app_data['app_start_time'] =time.time()
        app_data['appUserId']= str(uuid.uuid4())
    app_data['xdp']=str(float(device_data.get('dpi'))-round(random.uniform(0, 2),3))
    app_data['ydp']=str(float(device_data.get('dpi'))-round(random.uniform(0, 2),3))
    app_data['dlsdk_timestamp'] = datetime.utcfromtimestamp(int(time.time())).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    app_data['fid']=random.choice(['c','d','e','f'])+''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(21))
    if firebase_data.get('url'):
        num = 5
        while(num >0):
            req = firebase_installations(app_data,device_data)
            res= util.execute_request(**req)
            try:
                tmp = json.loads(res.get('data'))
                app_data['fid2'] = tmp.get('fid')
                break
            except:
                pass
            num -= 1
        if not app_data.get('fid2'):
            raise Exception ("Erorr in Firebase call  for country"+device_data.get('locale').get('country'))
            return {'status':True}


    if Appsflyer_data.get('cdn_url'):
        try:
            req = appsflyer_cdn( app_data, device_data )
            res = util.execute_request(**req)
            tem = json.loads(res.get('dara'))
            app_data['cdn_ver']  = tem.get('ver')
        except:
            pass


    if Appsflyer_data.get('dlsdk_url'):
        req = appsflyer_dlsdk(app_data,device_data)
        util.execute_request(**req)


    if not app_data.get('firstLaunchDate'):

        app_data['firstLaunchDate'] = datetime.utcfromtimestamp(int(time.time())).strftime("%Y-%m-%d_%H%M%S")+"+0000"

    if not app_data.get('af_gcm_token'):
        app_data['af_gcm_token'] = app_data.get('fid2') + ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(134))

    if conversion_data.get('fb'): 
        app_data['fb'] = str(uuid.uuid4())
        
    app_data['af_param_1']=util.get_random_string(type='hex',size=32)
    app_data['af_param_2']=str(random.randint(1102631,9999999))


    #print 'conversion'
    req  = appsflyer_conversions( app_data, device_data )
    util.execute_request(**req)

    if Appsflyer_data.get('att_url'):
        req = attr_appsflyer( app_data, device_data )
        util.execute_request(**req)

    if Appsflyer_data.get('register'):
        req = appsflyer_register( app_data, device_data )
        util.execute_request(**req)

    #print 'Gcd_sdk'
    req  = appsflyer_gcdsdk( app_data, device_data )
    util.execute_request(**req)


    if random.randint(1,10)>6:
        #print 'launches'
        req  = appsflyer_launches( app_data, device_data )
        util.execute_request(**req)
        

        
    
    # please comment below 3 line for update


    eve ='funnel_game_start_by_player'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_login_screen'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='funnel_player_is_on_login_screen'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1':app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_start_loading'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_login_screen_accept'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1':app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='af_login'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='funnel_fb_login_successful'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_finish_loading'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_chest_1'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_chest_2'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_chest_3'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_reward'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='village_unlocked_2'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_second_epoch_start'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='af_level_achieved'
    eve_val = {'af_level': '2', 'af_score': '1', 'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_puzzles_and_wonders'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_auto_spin_window'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_event_window'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_auto_spin'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_attack_2_tap'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1':app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_attack_2_reward'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_betx_window'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_betx'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_2_chest_1'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_2_chest_2'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_2_chest_3'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1':app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_raid_2_reward'
    eve_val = {'af_param_2':app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='village_unlocked_3'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='af_tutorial_completion'
    eve_val = {'af_content': 'Getting started', 'af_content_id': '1', 'af_success': 'true', 'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='tutor_third_epoch_start'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='af_level_achieved'
    eve_val = {'af_level': '3', 'af_score': '1', 'af_param_2':app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)

    eve ='funnel_get_reward_for_fb_connect'
    eve_val = {'af_param_2': app_data.get('af_param_2'), 'af_param_1': app_data.get('af_param_1')}
    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
    util.execute_request(**req)






    if random.randint(1,10)>6:
        #print 'launches'
        req  = appsflyer_launches( app_data, device_data )
        util.execute_request(**req)
        
   

    return {'status':True}


# ================== Open Begins ======================
def open( app_data, device_data, day=1 ):
    if app_data.get('times'):
        # print 'launches'
        req  = appsflyer_launches( app_data, device_data )
        util.execute_request(**req)








    return {'status':True}





# ================= Supportive Functions ===================



def get_ua(device_data):
    if int(device_data.get("sdk")) >=19:
        return 'Dalvik/2.1.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'
    else:
        return 'Dalvik/1.6.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'

def def_(app_data, paramName):
    if not app_data.get(paramName):
        app_data[paramName] = 0

def inc_(app_data, paramName):
    def_(app_data, paramName)
    app_data[paramName] = int(app_data.get(paramName)) + 1

def update_event_records( app_data, eventName, eventValue, af_timestamp):
    app_data['prev_event'] = {"prev_event_timestamp":af_timestamp, "prev_event_value":eventValue,"prev_event_name":eventName}

def sleep_interval(t1=0, t2=10):
    ''
    time.sleep(random.randint(t1, t2))

def set_batteryLevel(app_data):
    app_data['btch'] = random.choice(["no","ac","usb"])
    if app_data.get('btch') in ["ac", "usb"]:
        if app_data.get('batterylevel') > 10 and app_data.get('batterylevel') < 100:
            app_data['batterylevel'] += random.randint(1, 5)
        else:
            app_data['batterylevel'] = random.randint(10,100)
            app_data['btl']=str(app_data.get('batterylevel'))+".0"
    elif not app_data.get('batterylevel'):
        app_data['batterylevel'] = random.randint(10,100)
        app_data['btl']=str(app_data.get('batterylevel'))+".0"

def set_deviceData(app_data):
    if not app_data.get('deviceData'):
        app_data['dim_size']=str(random.randint(1,2))
        app_data['deviceData'] = True

def get_kef_data(app_data, data):
    if data.get('deviceData').get('sensors'):
        app_data["sensorCount"] = str(len(data.get('deviceData').get('sensors')))
    elif not app_data.get("sensorCount"):
        app_data["sensorCount"] = str(random.randint(3, 10))


    batteryTemp = random.choice(["300", "290", "280", "270"])

    kefKey = get_key_half(data.get('brand'), data.get('sdk'), data["lang"], data["af_timestamp"], buildnumber=campaign_data.get("appsflyer").get("buildnumber"))

    kefVal = generateValue(b=batteryTemp, x="0", s=app_data.get("sensorCount"), p=str(len(data.keys())), ts=data["af_timestamp"], fl=data["firstLaunchDate"], buildnumber=campaign_data.get("appsflyer").get("buildnumber"))

    return "kef" + kefKey, kefVal




def conversion_meta(app_data):
    data_l = {}
    if conversion_data.get('meta').get('first_launch'):
        data_l['first_launch'] = {}
    if conversion_data.get('meta').get('first_launch').get('start_with'):
        data_l['first_launch']['start_with'] = "application"
        
    if conversion_data.get('meta').get('first_launch').get('from_fg'):
        data_l['first_launch']['from_fg'] = random.randint(100,700)
    if conversion_data.get('meta').get('first_launch').get('init_to_fg'):
        data_l['first_launch']['init_to_fg'] = random.randint(100,600)

    fg = random.randint(100,700)
    delay = random.randint(100,700)
    if Appsflyer_data.get('dlsdk'):
        data_l['ddl'] =  {
                "from_fg": fg,
                "net": [
               fg+random.randint(10,20) ,
                0
                ],
                "rfr_wait": random.randint(2,10),
                "status": "NOT_FOUND",
                "timeout_value": random.randint(1,4)*1000
            }
    if Appsflyer_data.get('cdn'):
        data_l["rc"] = {
            "c_ver": app_data.get('cdn_ver'),
            "cdn_cache_status": "HIT",
            "cdn_token": app_data.get('cdn_token'),
            "delay": delay,
            "latency": delay-random.randint(5,50),
            "res_code": 200,
            "sig": "success"
        }

    return data_l




def def_sec(app_data,device_data):  
    if not app_data.get('sec'):
        timez = device_data.get('timezone')
        sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
        if int(timez) < 0:
            sec = (-1) * sec
        app_data['sec'] = sec
        
    return app_data.get('sec')

# ==================== CKSM Genrator ====================
def insert_char(s, p, r):
    return s[:p]+r+s[p:]

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]
        
def md5(data, radix=16):
    import hashlib
    md5_obj = hashlib.md5()
    md5_obj.update(data)
    if radix == 16:
        return md5_obj.hexdigest()
    elif radix == 64:
        return util.base64(md5_obj.digest())

def sha256(data):
    sha_obj = hashlib.sha256()
    sha_obj.update(data)
    return sha_obj.hexdigest()

def cksm_v1( ins_date, ins_time ):
    pk = campaign_data.get("package_name").split('.')
    pk[0], pk[-1] = pk[-1], pk[0]
    pkn='.'.join(pk)
    string = pkn+(campaign_data.get("package_name"))*2+"true"+ins_date+ins_time
    # print "========cksm_v1========"
    # print string
    # print "======================="
    sha256_result = sha256(string)  
    md5_result = md5(sha256_result) 
        
    n = ins_time
    sb = md5_result
    n4 = 0

    sb = change_char(sb,17,'f')
    sb = change_char(sb,27,'f')

    for i in range(0,len(str(n))):
        n4 += int(str(n)[i])
        

    insert1 = list('{:02x}'.format(n4))
    sb = change_char(sb,7,insert1[0])
    sb = change_char(sb,8,insert1[1])
            
    j = 0
    n6 = 77
    n3 = 0
    for i in range(0,len(str(sb))):
        n3 += int(str(sb)[i],36)
        
    if n3>100:
        n8 = 90
        n3%=100

    if n3<10:
        n3 = '0'+str(n3)
        
    sb = insert_char(sb,23,str(n3))
    return sb

# ==================== KEF Genrator ====================
global temp, counter
temp = 0
counter = 1

def get_key_half(brand, sdk, lang, af_ts, buildnumber):
    if buildnumber=="4.8.18":
        return getKeyHalf_4_8_18(sdk, lang.decode('utf-8'), af_ts)
    else:
        c = 'u0000'
        obj2 = af_ts[::-1]
        out = calculate(sdk, obj2, brand)
        i = len(out)
        if i > 4:
            i2 = globals()['counter']+65
            globals()['temp'] = i2 % 128
            if (1 if i2 % 2 != 0 else None) != 1:
                out.delete(4, i)
            else:
                out.delete(5, i)
        else:
            while i < 4:
                i3 = globals()['counter'] + 119
                globals()['temp'] = i3 % 128
                if (16 if i3 % 2 != 0 else 93) != 16:
                    i += 1
                    out+='1'
                else:
                    i += 66
                    out+='H'
                i3 = globals()['counter'] + 109
                globals()['temp'] = i3 % 128
                i3 %= 2
        return out.__str__()

def getKeyHalf_4_8_18(sdk, lang, ts):
    ts = ts[::-1]
    appends = [sdk,lang,ts]
    lengths = [len(sdk),len(lang),len(ts)]
    l = sorted(lengths)
    least = l[0]
    out = ""
    for x in range(least):
        numb = None
        for y in range(len(appends)):
            charAt = ord(appends[y][x])
            if numb:
                charAt = int((charAt ^ int(numb)))

            numb = charAt
            
        out+=str(hex(numb))[2:]

    if len(out)>4:
        out = out[:4]
    elif len(out)<4:
        while len(out)<4:
            out+="1"

    return out

def generateValue(b,x,s,p,ts,fl,buildnumber):
    part1=generateValue1get(ts,fl,buildnumber)
    str_ = bytearray("b"+b+"&x"+x+"&s"+s+"&p"+p, "utf-8")
    for i in range(len(str_)):
        str_[i] = int((str_[i] ^ ((i % 2) + 42)))

    stringBuilder = ""
    for toHexString in str_:
        toHexString2 = str(hex(int(toHexString)))[2:]
        if 1 == len(toHexString2):
            toHexString2 = "0"+str(toHexString2)
        stringBuilder+=toHexString2
    part2 = stringBuilder.__str__()
    return part1+part2

def generateValue1get(ts, firstLaunch, buildnumber):
    gethash = sha256(ts+firstLaunch+buildnumber)
    return gethash[:16]

def calculate(sdk, obj, brand):
    allList = [sdk, obj, brand]
    arrayList = []
    i = 0
    while True:
        flag = 1
        if i >= 3:
            break
        i2 = globals()['temp'] + 63
        globals()['counter'] = i2 % 128
        if i2 % 2 != 0:
            flag = None
        if flag != None:
            arrayList.append(len(allList[i]))
            i += 31
        else:
            arrayList.append(len(allList[i]))
            i += 1
    sorted(arrayList)
    intValue = int(arrayList[0])
    out = ""
    i3 = 0
    while i3 < intValue:
        i4 = globals()['counter']+99
        globals()['temp'] = i4 % 128
        i5 =  globals()['temp']+67
        globals()['counter'] = i5 % 128
        i5 %= 2
        number = None
        if i4 % 2 != 0:
            a = 57
        else:
            a = 83
        if a != 83:
            i4 = 1
        else:
            i4 = 0
        while i4 < 3:
            i5 = globals()['temp'] + 87
            globals()['counter'] = i5 % 128
            i5 %= 2
            i5 = ord(allList[i4][i3])
            if (92 if number == None else 39) != 39:
                i6 = globals()['temp'] + 55
                globals()['counter'] = i6 % 128
                i6 %= 2
                i6 = globals()['counter'] + 39
                globals()['temp'] = i6 % 128
                i6 %= 2
            else:
                i5 ^= int(number)
            number = i5
            i4 += 1
        out+=str(hex(int(number)))[2:]
        i3 += 1
    return out

def get_country():
    weighted_choices = campaign_data['country'] if campaign_data.get('country') else ('USA', 4)
    country_list     = [val for val, cnt in weighted_choices for i in range(cnt)]
    return random.choice(country_list)

def get_retention(day):
    return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0


