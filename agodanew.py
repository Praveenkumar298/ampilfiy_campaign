#-*- coding: utf-8 -*-
# from __future__ import unicode_literals
# updated by kanika_tyagi
import sys
if int(sys.version_info.major) == 2:
    py_version = 2
else:
    py_version = 3
    import urllib.parse as urlparse
from sdk import installtimenew, util
import time, random, json, string, urllib, uuid, hashlib
from spicipher import af_cipher,get_dlsdk_af_sig,get_cdn_token,get_gcd_sdk_af_sig,android_cksm_v3
false = False
from datetime import datetime
true = True
null = None


campaign_data = {
   'package_name' : 'com.agoda.mobile.consumer',
   'app_name' : 'Agoda',
   'app_version_name' : '12.3.0', #12.1.0 #12.2.0
   'app_version_code' : '231231', #224749 #227874
   'supported_countries' : 'WW',
   'supported_os' : '12',
   'api_ver_name' : '39.2.37-21 [0] [PR] 597374538',
   'sig' : '957755B4ADADA734E6BCFB0EEA1A079F544E6F8EF287A24AF839212F10138E1C',
   'platformextension' : 'android_native',
    'appsflyer' : { 
      'key' : 'jFACkny8v96b8uXuQZzhD7',
      'buildnumber' : '6.12.3',
      'version' : 'v6.12',
      'spiKey' : 'xensYJrcutD2n0lZZjwLVJ6hxXWTOp3KkqwHyJUrZnYFc8PYG4dnTvmuj6JojhO1',
    #    'spiKey' : 'Fv44sWKxA9YQx2S2P1BH0gwGJXFT1XEa7Nh6shZw+gx5bI2c8viR6+XYNJfFismk',#devkey
    },
   'link' : '',
    'app_size' : 35,
    'api_ver' : 83923710,
    'tracker' : ['appsflyer'],
    'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
    'retention' : {1: 85, 2: 82, 3: 80, 4: 78, 5: 75, 6: 72, 7: 70, 8: 68, 9: 65, 10: 60, 11: 55, 12: 50, 13: 45, 14: 40, 15: 35, 16: 33, 17: 30, 18: 28, 19: 26, 20: 20, 21: 19, 22: 18, 23: 17, 24: 16, 25: 15, 26: 14, 27: 13, 28: 12, 29: 11, 30: 10, 31: 9, 32: 8, 33: 7, 34: 6, 35: 5},
    }


Appsflyer_data = {"Key": "jFACkny8v96b8uXuQZzhD7", "id": "com.agoda.mobile.consumer", "app_name": "Agoda", "build_number": "6.12.3", "res_url": "bfo9j9-register.appsflyersdk.com", "dlsdk_url": "bfo9j9-dlsdk.appsflyersdk.com", "gcd_url": "bfo9j9-gcdsdk.appsflyersdk.com", "con_url": "bfo9j9-conversions.appsflyersdk.com", "cdn_version": "v1", "cdn_url": "bfo9j9-cdn-settings.appsflyersdk.com", "la_url": "bfo9j9-launches.appsflyersdk.com", "in_url": "bfo9j9-inapps.appsflyersdk.com", "gcd_ver": "v4.0", "att_url": null}

register_data = {"advertiserId": "63f56464-fee8-4114-8533-fd3e45909ecc", "installDate": "2024-01-19_051024+0000", "sdk": "23", "appUserId": "4aac3810-6925-4dcd-b2a2-d89982436e02", "carrier": "Jio", "app_version_code": "224749", "app_name": "Agoda", "launch_counter": "1", "af_gcm_token": "552028937321", "network": "unknown", "operator": "Jio", "devkey": "jFACkny8v96b8uXuQZzhD7", "brand": "OPPO", "app_version_name": "12.1.0", "uid": "1705641125542-4143970912560432085", "model": "CPH1609"}

firebase_data = {"x-goog-api-key": "AIzaSyDfFR8B4OUA7qwjbSA6jxbYdOnba-RW6o8", "x-firebase-client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA", "X-Android-Cert": "443857BE6EAADF59DDFF58A3398EBCA4E7C8237D", "data": {"fid": "e-iCFfSkTZezMJ_Y7ffJzB", "appId": "1:552028937321:android:a042dda3bea78174", "authVersion": "FIS_v2", "sdkVersion": "a:17.0.1"}, "url": "/v1/projects/agoda-dd55/installations"}

conversion_data = {"advertiserId": "63f56464-fee8-4114-8533-fd3e45909ecc", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1705641126844", "appUserId": "4aac3810-6925-4dcd-b2a2-d89982436e02", "app_version_code": "224749", "app_version_name": "12.1.0", "appsflyerKey": "jFACkny8v96b8uXuQZzhD7", "batteryLevel": "14.0", "brand": "OPPO", "carrier": "Jio", "cell": {"mcc": 405, "mnc": 872}, "cksm_v3": "47581a628389be58", "counter": "1", "country": "US", "customData": "{\"customData\":\"ac3cc400-275d-45a4-8a7c-dadb56c6bc42\"}", "date1": "2024-01-19_104024+0530", "date2": "2024-01-19_104024+0530", "device": "CPH1609", "deviceData": {"arch": "", "btch": "no", "btl": "14.0", "build_display_id": "CPH1609EX_11_A.32_191228", "cpu_abi": "arm64-v8a", "cpu_abi2": "", "dim": {"d_dpi": "480", "size": "2", "x_px": "1080", "xdp": "403.411", "y_px": "1920", "ydp": "399.737"}, "sensors": [{"sN": "MAGNETOMETER", "sT": 2, "sV": "MTK", "sVE": [-11.875, 14.625, -46.9375], "sVS": [-11.6875, 15, -47.75]}, {"sN": "ACCELEROMETER", "sT": 1, "sV": "MTK", "sVE": [-0.019, 0.192, 9.798], "sVS": [-0.039, 0.211, 9.812]}, {"sN": "GYROSCOPE", "sT": 4, "sV": "MTK", "sVE": [0.0001373291, -0.0049743652, -0.12532043], "sVS": [-0.0022735596, 0.0024261475, -0.0038604736]}]}, "deviceType": "user", "disk": "35115/53694", "firstLaunchDate": "2024-01-19_104206+0530", "iaecounter": "0", "installDate": "2024-01-19_051024+0000", "installer_package": "com.android.vending", "isFirstCall": "true", "isGaidWithGps": "true", "ivc": false, "kef4957": "0b408dc99edc6d284819191b0c531a0d591a180d5a1e18", "lang": "English", "lang_code": "en", "last_boot_time": 1705637413400, "meta": {"ddl": {"from_fg": 2995, "net": [1323, 0], "status": "NOT_FOUND", "timeout_value": 3000}, "first_launch": {"from_fg": 4332, "init_to_fg": 637, "start_with": "application"}, "host": {"name": "appsflyersdk.com", "prefix": "bfo9j9-"}, "rc": {"cdn_token": "8e5e7a18a54616de8c35ca21e2259e7bc0be58a05c542f298be9f8172e7b0e78", "delay": 1696, "error": "InterruptedIOException: thread interrupted", "latency": 1674}}, "model": "CPH1609", "network": "unknown", "open_referrer": "android-app://com.oppo.launcher", "operator": "Jio", "p_receipt": {"an": {"dbg": false, "hk": ";"}, "pr": {"ac": "0", "ah": "zygote64_32", "ai": "0", "ak": "default", "al": "cortex-a53", "am": "default", "an": "cortex-a53", "ap": "root", "ar": "mt6755", "as": "arm64-v8a", "at": "arm64-v8a,armeabi-v7a,armeabi", "au": "armeabi-v7a,armeabi", "av": "arm64-v8a"}}, "platform_extension_v2": {"platform": "android_native", "version": "6.12.3"}, "platformextension": "android_native", "product": "CPH1609", "referrers": [{"api_ver": 83923710, "api_ver_name": "39.2.37-21 [0] [PR] 597374538", "click_ts": 1705640863, "google_custom": {"click_server_ts": 1705640864, "install_begin_server_ts": 1705640869, "install_version": "12.1.0", "instant": false}, "install_begin_ts": 1705640867, "latency": 881, "referrer": "utm_source=(not%20set)&utm_medium=(not%20set)", "response": "OK", "source": "google", "type": "store"}], "registeredUninstall": false, "rfr": {"clk": "1705640863", "code": "0", "install": "1705640867", "instant": false, "val": "utm_source=(not%20set)&utm_medium=(not%20set)"}, "sc_o": "p", "sdk": "23", "sig": "957755B4ADADA734E6BCFB0EEA1A079F544E6F8EF287A24AF839212F10138E1C", "targetSDKver": 34, "timepassedsincelastlaunch": "-1", "tokenRefreshConfigured": false, "uid": "1705641125542-4143970912560432085"}

inapp_data = {"advertiserId": "63f56464-fee8-4114-8533-fd3e45909ecc", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1705641214472", "appUserId": "4aac3810-6925-4dcd-b2a2-d89982436e02", "app_version_code": "224749", "app_version_name": "12.1.0", "appsflyerKey": "jFACkny8v96b8uXuQZzhD7", "brand": "OPPO", "carrier": "Jio", "cell": {"mcc": 405, "mnc": 872}, "cksm_v3": "8c79b61fb2d7efa3", "counter": "6", "country": "US", "customData": "{\"customData\":\"ac3cc400-275d-45a4-8a7c-dadb56c6bc42\"}", "date1": "2024-01-19_104024+0530", "date2": "2024-01-19_104024+0530", "device": "CPH1609", "deviceData": {"arch": "", "build_display_id": "CPH1609EX_11_A.32_191228", "cpu_abi": "arm64-v8a", "cpu_abi2": "", "dim": {"d_dpi": "480", "size": "2", "x_px": "1080", "xdp": "403.411", "y_px": "1920", "ydp": "399.737"}}, "deviceType": "user", "disk": "35077/53694", "eventName": "af_content_view", "eventValue": "{\"af_content_id\":\"180212\",\"af_destination_b\":null,\"af_destination_a\":\"2994\",\"af_content_type\":\"Hotel\",\"af_num_adults\":\"2\",\"af_occupancy_children\":\"0\",\"af_customer_user_id\":\"4aac3810-6925-4dcd-b2a2-d89982436e02\",\"af_date_b\":\"2024-01-20\",\"af_language_id\":\"1\",\"af_room_no\":\"1\",\"af_logged_in\":\"1\",\"af_occupancy_adults\":\"2\",\"af_content_type_1\":\"Hotel\",\"af_date_a\":\"2024-01-19\",\"af_currency\":\"INR\",\"af_num_children\":\"0\"}", "firstLaunchDate": "2024-01-19_104206+0530", "iaecounter": "2", "installDate": "2024-01-19_051024+0000", "installer_package": "com.android.vending", "isFirstCall": "false", "isGaidWithGps": "true", "ivc": false, "kef4f54": "23e60bc6d940cdf94819191b0c531a0d591a180d5a1f1c", "lang": "English", "lang_code": "en", "last_boot_time": 1705637413400, "model": "CPH1609", "network": "unknown", "operator": "Jio", "platformextension": "android_native", "product": "CPH1609", "registeredUninstall": true, "sc_o": "p", "sdk": "23", "sensors": {"am": {"n": "ACCELEROMETER", "v": [[0, 0.1, 9.8], [0, 0, 0]]}, "gs": {"n": "GYROSCOPE", "v": [[0, 0, 0], [0, 0, 0.6]]}, "mm": {"n": "MAGNETOMETER", "v": [[130.2, -47.3], [-6.3, 1]]}}, "sig": "957755B4ADADA734E6BCFB0EEA1A079F544E6F8EF287A24AF839212F10138E1C", "targetSDKver": 34, "tokenRefreshConfigured": false, "uid": "1705641125542-4143970912560432085"}



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
        # "af_currentstore": "google_play", 
        # "af_installstore": "google_play",
        # "onelink_id": "H5hv", 
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
        # "exception_number"  : 0,
        "iaecounter"        : str(app_data.get('iaecounter')), 
        "installDate"       : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000', 
        "installer_package" : "com.google.android.packageinstaller", 
        "isFirstCall"       : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"     : "true", 
        "ivc"               : False, 
        "lang"              : "English", 
        "lang_code"         : "en", 
        "last_boot_time"    : app_data.get('last_boot_time'),
        "meta": {
        "ddl": {
          "from_fg": random.randint(2000,8000) ,
          "net": [
            1323, 
            0
          ], 
          "status": "NOT_FOUND", 
          "timeout_value": 3000
        }, 
        "first_launch": {
          "from_fg": random.randint(4000,8000), 
          "init_to_fg": random.randint(500,900), 
          "start_with": "application"
        }, 
        "host": {
          "name": "appsflyersdk.com", 
          "prefix": "bfo9j9-"
        }, 
        "rc": {
          "cdn_token": app_data.get('cdn_token'), 
          "delay": 1696, 
          "error": "InterruptedIOException: thread interrupted", 
          "latency": 1674
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
        "platform_extension_v2": {
        "platform": "android_native", 
        "version": "6.12.3"
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
         "targetSDKver": 34, 
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
    data['af_v']                = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']               = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))
    if conversion_data.get('cksm_v1'):
        data['cksm_v1']            = cksm_v1(data['date1'],data['af_timestamp'])
    elif conversion_data.get('cksm_v3'):
        data['cksm_v3']            = android_cksm_v3(app_id=campaign_data.get('package_name'), af_key=campaign_data.get('appsflyer').get('key'), af_timestamp=data.get('af_timestamp'), build_number=campaign_data.get('appsflyer').get('buildnumber'))
        del data['af_v'] ; del data['af_v2']

    

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
        # "af_currentstore": "google_play", 
        # "af_installstore": "google_play",
        # "onelink_id": "H5hv",
        # "onelink_ver":"53",  
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
        # "exception_number"  : 0,
        "iaecounter"        : str(app_data.get('iaecounter')),
        "installDate"       : datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')).strftime('%Y-%m-%d_%H%M%S')+'+0000', 
        "installer_package" : "com.google.android.packageinstaller", 
        "isFirstCall"       : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"     : "true", 
        "ivc"               : False, 
        "lang"              : "English", 
        "lang_code"         : "en", 
        "last_boot_time"    : app_data.get('last_boot_time'),
        "meta": {
        "first_launch": {
          "from_fg": random.randint(4000,8000), 
          "init_to_fg": random.randint(500,900), 
          "net": 3319, 
          "start_with": "application"
        }, 
        "host": {
          "name": "appsflyersdk.com", 
          "prefix": "bfo9j9-"
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
        "platform_extension_v2": {
        "platform": "android_native", 
        "version": "6.12.3"
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
        "targetSDKver": 34, 
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
    data['af_v']               = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']              = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))
    if conversion_data.get('cksm_v1'):
        data['cksm_v1']            = cksm_v1(data['date1'],data['af_timestamp'])
    elif conversion_data.get('cksm_v3'):
        data['cksm_v3']            = android_cksm_v3(app_id=campaign_data.get('package_name'), af_key=campaign_data.get('appsflyer').get('key'), af_timestamp=data.get('af_timestamp'), build_number=campaign_data.get('appsflyer').get('buildnumber'))
        del data['af_v'] ; del data['af_v2']

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
        # "af_currentstore": "google_play", 
        # "af_installstore": "google_play",
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
        "installer_package"     : "com.google.android.packageinstaller", 
        "isFirstCall"           : "false" if app_data.get('counter') > 1 else "true", 
        "isGaidWithGps"         : "true", 
        "ivc"                   : False, 
        "lang"                  : "English", 
        "lang_code"             : "en", 
        "last_boot_time"        : app_data.get('last_boot_time'),
        "model"                 : device_data.get('model'), 
        "network"               : device_data.get('network').upper(), 
        "operator"              : device_data.get('carrier'), 
        "platformextension"     : campaign_data.get("platformextension"), 
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
        "targetSDKver": 34,
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
    data['af_v']            = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']           = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))
    if conversion_data.get('cksm_v1'):
        data['cksm_v1']            = cksm_v1(data['date1'],data['af_timestamp'])
    elif conversion_data.get('cksm_v3'):
        data['cksm_v3']            = android_cksm_v3(app_id=campaign_data.get('package_name'), af_key=campaign_data.get('appsflyer').get('key'), af_timestamp=data.get('af_timestamp'), build_number=campaign_data.get('appsflyer').get('buildnumber'))
        del data['af_v'] ; del data['af_v2']


    # if not app_data.get('prev_event'):
    #     del data['prev_event']
    # else:
    #     data['prev_event'] = json.dumps(app_data.get('prev_event'),separators = (',',':'))

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
        "installer_package" : "com.google.android.packageinstaller", 
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
    data['af_v']               = util.sha1(data.get('appsflyerKey')[0:7]+data.get('uid')[0:7]+data.get('af_timestamp')[-7:13])
    data['af_v2']              = util.sha1(util.md5(data.get('appsflyerKey')+data.get('af_timestamp')+data.get('uid')+data.get('installDate')+data.get('counter')+data.get('iaecounter')))
    if conversion_data.get('cksm_v1'):
        data['cksm_v1']            = cksm_v1(data['date1'],data['af_timestamp'])
    elif conversion_data.get('cksm_v3'):
        data['cksm_v3']            = android_cksm_v3(app_id=campaign_data.get('package_name'), af_key=campaign_data.get('appsflyer').get('key'), af_timestamp=data.get('af_timestamp'), build_number=campaign_data.get('appsflyer').get('buildnumber'))
        del data['af_v'] ; del data['af_v2']

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
                            "value":device_data.get('adid')
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
            if not app_data.get('fiddler_app_test'):
                util.firebase_error(device_data.get('locale').get('country'))
                return {'status':True}


    if Appsflyer_data.get('cdn_url'):
        try:
            req = appsflyer_cdn( app_data, device_data )
            res = util.execute_request(**req)
            tem = json.loads(res.get('data'))
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
        

    item=random.choice([{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"4877","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"13592284","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"22733203","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"443336","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"2834604","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"39019249","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"46920642","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"}])   
    
    # please comment below 3 line for update

    poss = [True]*60+[False]*40
    random.shuffle(poss)
    if random.choice(poss):
        eve = "af_content_view"
        eve_val= {"af_num_children":"0","af_num_adults":"2","af_customer_user_id":app_data.get('appUserId'),"af_content_id":item.get('af_content_id'),"af_date_b":app_data.get('current_date'),"af_room_no":"1","af_date_a":app_data.get('current_data'),"af_occupancy_children":"0","af_content_type":item.get('af_content_type'),"af_content_type_1":"Hotel","af_currency":app_data.get('currency'),"af_destination_b":"","af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"}
        req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
        util.execute_request(**req)


        eve= "af_content_view_fb"
        eve_val= {"af_currency":app_data.get('currency'),"af_content":[{"id":item.get('af_content_id'),"quantity":1}],"af_content_id":item.get('af_content_id'),"af_quantity":1,"af_content_type":"product"}
        req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
        util.execute_request(**req)
 

        poss = [True]*30+[False]*70
        random.shuffle(poss)
        if random.choice(poss):
            eve= "af_add_to_cart"
            eve_val= {"af_currency":app_data.get('currency'),"af_content":[{"id":item.get('af_content_id'),"quantity":1}],"af_price":item.get('af_price'),"af_content_id":item.get('af_content_id'),"af_quantity":1,"af_content_type":item.get('af_content_type')}
            req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
            util.execute_request(**req)

            poss = [True]*5+[False]*95
            random.shuffle(poss)
            if random.choice(poss):
                eve= "af_initiated_checkout"
                eve_val= {"af_num_children":"0","af_num_adults":"2","af_country":"IN","af_sales_exclusive":102.57,"af_customer_user_id":app_data.get('appUserId'),"af_price":item.get('af_price'),"af_content_id":item.get('af_content_id'),"af_discount_promotion":0,"af_date_b":app_data.get('current_date'),"af_room_no":"1","af_date_a":app_data.get('current_data'),"af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"BF","af_currency":app_data.get('currency'),"af_destination_a":"14552","af_tax_and_fee":18.46,"af_destination_b":"35","af_revenue":102.57,"af_lobgged_in":"1","af_language_id":"1","af_occupancy_adults":"2"}
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
        if not app_data.get('firstLaunchDate'):
            app_data['firstLaunchDate'] = datetime.utcfromtimestamp(int(time.time())).strftime("%Y-%m-%d_%H%M%S")+"+0000"

        # print 'launches'
        req  = appsflyer_launches( app_data, device_data )
        util.execute_request(**req)
        
        item=random.choice([{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"4877","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"13592284","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"22733203","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"443336","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"2834604","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"39019249","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"},{"af_num_children":"0","af_num_adults":"2","af_customer_user_id":"4f935c39-b7fe-4677-9241-163348e296da","af_content_id":"46920642","af_date_b":"2023-12-29","af_room_no":"1","af_date_a":"2023-12-28","af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"Hotel","af_currency":"INR","af_destination_b":null,"af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"}]) 
        
        poss = [True]*40+[False]*60
        random.shuffle(poss)
        if random.choice(poss):
            eve = "af_content_view"
            eve_val= {"af_num_children":"0","af_num_adults":"2","af_customer_user_id":app_data.get('appUserId'),"af_content_id":item.get('af_content_id'),"af_date_b":app_data.get('current_date'),"af_room_no":"1","af_date_a":app_data.get('current_data'),"af_occupancy_children":"0","af_content_type":item.get('af_content_type'),"af_content_type_1":"Hotel","af_currency":app_data.get('currency'),"af_destination_b":"","af_logged_in":"1","af_language_id":"1","af_occupancy_adults":"2"}
            req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
            util.execute_request(**req)


            eve= "af_content_view_fb"
            eve_val= {"af_currency":app_data.get('cuurency'),"af_content":[{"id":item.get('af_content_id'),"quantity":1}],"af_content_id":item.get('af_content_id'),"af_quantity":1,"af_content_type":"product"}
            req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
            util.execute_request(**req)
     

            poss = [True]*20+[False]*0
            random.shuffle(poss)
            if random.choice(poss):
                eve= "af_add_to_cart"
                eve_val= {"af_currency":app_data.get('cuurency'),"af_content":[{"id":item.get('af_content_id'),"quantity":1}],"af_price":item.get('af_price'),"af_content_id":item.get('af_content_id'),"af_quantity":1,"af_content_type":app_data.get('')}
                req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
                util.execute_request(**req)

                poss = [True]*2+[False]*98
                random.shuffle(poss)
                if random.choice(poss):
                    eve= "af_initiated_checkout"
                    eve_val= {"af_num_children":"0","af_num_adults":"2","af_country":"IN","af_sales_exclusive":102.57,"af_customer_user_id":app_data.get('appUserId'),"af_price":item.get('af_price'),"af_content_id":item.get('af_content_id'),"af_discount_promotion":0,"af_date_b":app_data.get('current_date'),"af_room_no":"1","af_date_a":app_data.get('current_data'),"af_occupancy_children":"0","af_content_type":"Hotel","af_content_type_1":"BF","af_currency":app_data.get('cuurency'),"af_destination_a":"14552","af_tax_and_fee":18.46,"af_destination_b":"35","af_revenue":102.57,"af_lobgged_in":"1","af_language_id":"1","af_occupancy_adults":"2"}
                    req=appsflyer_inapps( app_data, device_data, eventname= eve, eventvalue= eve_val)
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


