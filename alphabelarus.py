#-*- coding: utf-8 -*-
# created by Jitendra
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
null = None

campaign_data = {
   'package_name' : 'by.st.alfa.ib2.app',
   'app_name' : 'Alpha Business Mobile Belarus',
   'app_version_name' : '4.88.0',
   'app_version_code' : '445',
   'supported_countries' : 'WW',
   'supported_os' : '11',
   'api_ver_name' : '30.5.16-21 [0] [PR] 447062287',
   'sig' : '271A4567A4DBD05784AB7190B043AEDC82338BAAF4CB2A35918E5904E4214820',
   'platformextension' : 'android_native',
    'appsflyer' : { 
      'key' : 'U6bnQjufC4wivPevzraJZW',
      'buildnumber' : '6.3.2',
      'version' : 'v6.3',
      'spiKey' : '0u7UW5lUjnBaBbbS4llk4B6hDB1+P3r8ZSBZ7LikdJutE+nXOjAVboo31J9x8+xJ',
    #    'spiKey' : '2YUv2ieSoNj748oXx/q8k8/Y5Ce5vBX0QeQfv2LUhtRxZvWN8PpFp0GwZ6ca9RjI',#devkey
    },
    'app_size' : 20,
    'api_ver' : 83051610,
    'tracker' : ['appsflyer'],
    'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
    'retention' : {1: 85, 2: 82, 3: 80, 4: 78, 5: 75, 6: 72, 7: 70, 8: 68, 9: 65, 10: 60, 11: 55, 12: 50, 13: 45, 14: 40, 15: 35, 16: 33, 17: 30, 18: 28, 19: 26, 20: 20, 21: 19, 22: 18, 23: 17, 24: 16, 25: 15, 26: 14, 27: 13, 28: 12, 29: 11, 30: 10, 31: 9, 32: 8, 33: 7, 34: 6, 35: 5},
    }


Appsflyer_data = {"Key": "U6bnQjufC4wivPevzraJZW", "gcd_ver": "v5.0", "id": "by.st.alfa.ib2.app", "build_number": "6.3.2", "gcd_url": "gcdsdk.appsflyersdk.com", "con_url": "conversions.appsflyer.com", "in_url": "inapps.appsflyer.com", "la_url": "launches.appsflyer.com", "att_url": null, "res_url": null}

register_data = {}

firebase_data = {"x-goog-api-key": "AIzaSyBq5WP-fXdOAsJL1brJQlYBP-PLE2vpM-w", "x-firebase-client": "H4sIAAAAAAAAAFWQzWrDMBCEX8XsOZJlmSQlt0AvPYee6lAUa52IyFKQtoYS8u7d-CdQdPtWszM7d7igSXRCQxl2X3cwZwwEOzDBpuisIJPOSCLba1PWuuhcQtHGhE2plaxlVVwjeReaspJbWan5g88M3ni-mYAJxv-SaxnrSvKbcNf2DHiL1MVi6EIm4z2mpmxjL2csBwzWhfOyboSsXRcWB9eiCKbnTPvD5-H7Q6n1-34Z9NGi_z8Zd8w-hlwMz7ScXtaL6JTYgkX5J7-C3fhvFxMnfqHehakZPR9ErMu3mGg8nyuBFVhD-OwWtNK1UFuhNnB8HFcwYMpszmVrePwBUYDVEokBAAA", "X-Android-Cert": "C22B60F1AF28154E1D8D376DCFB26167EDB3C508", "data": {"fid": "eQsPN9S6S6ChKWtKoxX7AK", "appId": "1:783139008547:android:a38b324a94fdb981df8196", "authVersion": "FIS_v2", "sdkVersion": "a:17.1.3"}, "url": "/v1/projects/alfabusinessv3-1508773014288/installations"}

conversion_data = {"advertiserId": "02aef402-2d07-4f22-b843-232117e87c95", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1688625862983", "af_v": "58e87a0bee31036e0a2c58c5f456035e0a4ab052", "af_v2": "399999b7ca24ec2bd5483301c23eb8c7eaf055f3", "app_version_code": "445", "app_version_name": "4.88.0", "appsflyerKey": "U6bnQjufC4wivPevzraJZW", "batteryLevel": "100.0", "brand": "Asus", "carrier": "BSNL Mobile", "cell": {"mcc": 0, "mnc": 0}, "cksm_v1": "de34c2348f225a6cdfc7870338139f6590", "counter": "1", "country": "US", "date1": "2023-07-06_014311-0500", "date2": "2023-07-06_014311-0500", "device": "ASUS_I005DA", "deviceData": {"arch": "", "btch": "ac", "btl": "100.0", "build_display_id": "Asus-user 7.1.2 20171130.276299 release-keys", "cpu_abi": "x86_64", "cpu_abi2": "", "dim": {"d_dpi": "191", "size": "3", "x_px": "576", "xdp": "191.0", "y_px": "1024", "ydp": "191.0"}, "sensors": [{"sN": "LiteOn magnetic", "sT": 2, "sV": ""}, {"sN": "AKM gyroscope", "sT": 4, "sV": ""}, {"sN": "Taos accelerometer", "sT": 1, "sV": ""}]}, "deviceType": "user", "disk": "29629/32929", "exception_number": 0, "firstLaunchDate": "2023-07-06_064423+0000", "iaecounter": "0", "installDate": "2023-07-06_064311+0000", "installer_package": "com.android.vending", "isFirstCall": "true", "isGaidWithGps": "true", "ivc": false, "kef407e": "4537f91a0105dbd54818191e0c531b0d591a1a0d5a1f12", "lang": "English", "lang_code": "en", "last_boot_time": 1688625691790, "meta": {"first_launch": {"init_to_fg": 840}}, "model": "ASUS_I005DA", "network": "WIFI", "open_referrer": "android-app://by.st.alfa.ib2.app", "operator": "BSNL Mobile", "p_receipt": {"an": {"dbg": false, "hk": ";"}, "as": {"cav": 9, "null": 68}, "pr": {"ac": "libnb.so", "ad": "1", "ae": "1", "af": "default", "ag": "x86", "ah": "zygote64_32", "ai": "0", "aj": "x86", "ap": "Asus", "ar": "qcom", "as": "x86_64", "at": "x86_64,x86,armeabi-v7a,armeabi,arm64-v8a", "au": "x86,armeabi-v7a,armeabi", "av": "x86_64,arm64-v8a"}}, "platformextension": "android_native", "product": "ASUS_I005DA", "registeredUninstall": false, "sc_o": "p", "sdk": "25", "sig": "271A4567A4DBD05784AB7190B043AEDC82338BAAF4CB2A35918E5904E4214820", "timepassedsincelastlaunch": "-1", "tokenRefreshConfigured": false, "uid": "1688625863044-1264592354109570914"}

inapp_data = {"advertiserId": "02aef402-2d07-4f22-b843-232117e87c95", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1688625906582", "af_v": "21f8d5f806868276f273da9f6a12bee5128c745c", "af_v2": "2327ca22e26da755da5236fab9e628e96b05ab5c", "app_version_code": "445", "app_version_name": "4.88.0", "appsflyerKey": "U6bnQjufC4wivPevzraJZW", "brand": "Asus", "carrier": "BSNL Mobile", "cell": {"mcc": 0, "mnc": 0}, "cksm_v1": "5bd994b42fa01f00ff382dd493b44fd54c", "counter": "1", "country": "US", "date1": "2023-07-06_014311-0500", "date2": "2023-07-06_014311-0500", "device": "ASUS_I005DA", "deviceData": {"arch": "", "build_display_id": "Asus-user 7.1.2 20171130.276299 release-keys", "cpu_abi": "x86_64", "cpu_abi2": "", "dim": {"d_dpi": "191", "size": "3", "x_px": "576", "xdp": "191.0", "y_px": "1024", "ydp": "191.0"}}, "deviceType": "user", "disk": "29631/32929", "eventName": "account_click", "eventValue": "{}", "firstLaunchDate": "2023-07-06_064423+0000", "iaecounter": "1", "installDate": "2023-07-06_064311+0000", "installer_package": "com.android.vending", "isFirstCall": "false", "isGaidWithGps": "true", "ivc": false, "kef417e": "355c7a3477b4e37b481912120c531b0d591a1a0d5a1f1c", "lang": "English", "lang_code": "en", "last_boot_time": 1688625691790, "model": "ASUS_I005DA", "network": "WIFI", "operator": "BSNL Mobile", "p_receipt": {"an": {"dbg": false, "hk": ";"}, "as": {"cav": 9, "null": 68}, "pr": {"ac": "libnb.so", "ad": "1", "ae": "1", "af": "default", "ag": "x86", "ah": "zygote64_32", "ai": "0", "aj": "x86", "ap": "Asus", "ar": "qcom", "as": "x86_64", "at": "x86_64,x86,armeabi-v7a,armeabi,arm64-v8a", "au": "x86,armeabi-v7a,armeabi", "av": "x86_64,arm64-v8a"}}, "platformextension": "android_native", "product": "ASUS_I005DA", "registeredUninstall": false, "sc_o": "p", "sdk": "25", "sensors": {"am": {"n": "Taos accelerometer", "v": [[0, 8.9, 4.5], [0, 0, 0]]}, "gs": {"n": "AKM gyroscope", "v": [[0, 0, 0], [0, 0, 0]]}, "mm": {"n": "LiteOn magnetic", "v": [[45, 20.7], [0, 0]]}}, "sig": "271A4567A4DBD05784AB7190B043AEDC82338BAAF4CB2A35918E5904E4214820", "tokenRefreshConfigured": false, "uid": "1688625863044-1264592354109570914"}



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
        "disk"              : device_data.get('internal_memory'),
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
            "latency"           : random.randint(85,95),
            "referrer"          : app_data.get("referrer", "utm_source=(not%20set)&utm_medium=(not%20set)"), 
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
            "val"                   : app_data.get("referrer", "utm_source=(not%20set)&utm_medium=(not%20set)")
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
        "disk"              : device_data.get('internal_memory'),
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
            "from_fg": random.randint(800,1000), 
            "init_to_fg": random.randint(8,10), 
            "net": random.randint(10000,12000)
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
            "referrer":app_data.get("referrer", "utm_source=(not%20set)&utm_medium=(not%20set)"), 
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
            "val"                   : app_data.get("referrer", "utm_source=(not%20set)&utm_medium=(not%20set)")
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
        "disk"                  : device_data.get('internal_memory'),
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
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0),
                        round(random.uniform(8,10),1)
                    ],
                    [
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0)
                    ]
                ]
            },
            "er": "no_svs",
            "gs": {
                "n": "ICM20607 Gyroscope -Wakeup Secondary",
                "v": [
                    [
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0)
                    ],
                    [
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0),
                        round(random.uniform(0,1),0)
                    ]
                ]
            },
            "mm": {
                "n": "AK09918 Magnetometer",
                "v": [
                    [
                        round(random.uniform(-8,-6),0),
                        round(random.uniform(-390,-388),1)
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
                "sT": round(random.uniform(0,2),0),
                "sV": "InvenSense"
            },
            {
                "sN": "ICM20607 Gyroscope",
                "sT": round(random.uniform(3,5),0),
                "sV": "InvenSense"
            },
            {
                "sN": "ICM20607 Gyroscope -Wakeup Secondary",
                "sT": round(random.uniform(3,5),0),
                "sV": "InvenSense"
            },
            {
                "sN": "AK09918 Magnetometer -Wakeup Secondary",
                "sT": round(random.uniform(1,3),0),
                "sV": "AKM"
            },
            {
                "sN": "ICM20607 Accelerometer -Wakeup Secondary",
                "sT": round(random.uniform(1,2),0),
                "sV": "InvenSense"
            },
            {
                "sN": "AK09918 Magnetometer",
                "sT": round(random.uniform(1,3),0),
                "sV": "AKM",
                "sVS": [
                    round(random.uniform(200,202),5),
                    round(random.uniform(59,61),6),
                    round(random.uniform(-430,-427),3)
                ]
            }
        ]
        },
        "deviceType"        : "user", 
        "disk"              : device_data.get('internal_memory'),
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
            "referrer"          : app_data.get("referrer", "utm_source=(not%20set)&utm_medium=(not%20set)"), 
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
            "val"                   : app_data.get("referrer", "utm_source=(not%20set)&utm_medium=(not%20set)")
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
        

    
    eve = 'account_click'
    eve_val = {}
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


