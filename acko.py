#-*- coding: utf-8 -*-
# updated by kanika
from datetime import datetime
from sdk import installtimenew, util
import time, random, json, string, uuid, hashlib
from spicipher import af_cipher,get_cdn_token
false=False
true = True
null = None


campaign_data = {
   'package_name' : 'com.acko.android',
   'app_name' : 'ACKO',
   'app_version_name' : '7.2.4',
   'app_version_code' : '241',
   'supported_countries' : 'WW',
   'supported_os' : '11',
   'api_ver_name' : '38.4.19-21 [0] [PR] 582389963',
   'sig' : '3B7F0E749314CB299BCBE1ED63059310E280C7DEA8A49C07593D0B267201D527',
   'platformextension' : 'android_native',
    'appsflyer' : { 
      'key' : 'nvTCkGCccZLQAC6zydZDMJ',
      'buildnumber' : '6.12.3',
      'version' : 'v6.12',
      'spiKey' : 'SMa7uhItXaEbZlQtq7I6JfAzUzVDanmIdNCOlLfSq6m6YoVOP+qIPEJko+CEA9PZ',
    #    'spiKey' : 'JE/an8Q8zeakn0VZiID/s5BldT63U8kjs+g8+2JijJnjxPDCE5qZNcPTO9mjcZ1N',#devkey
    },
    'link' : '',
    'app_size' : 54,
    'api_ver' : 83841910,
    'tracker' : ['appsflyer'],
    'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
    'retention' : {1: 85, 2: 82, 3: 80, 4: 78, 5: 75, 6: 72, 7: 70, 8: 68, 9: 65, 10: 60, 11: 55, 12: 50, 13: 45, 14: 40, 15: 35, 16: 33, 17: 30, 18: 28, 19: 26, 20: 20, 21: 19, 22: 18, 23: 17, 24: 16, 25: 15, 26: 14, 27: 13, 28: 12, 29: 11, 30: 10, 31: 9, 32: 8, 33: 7, 34: 6, 35: 5},
    }



conversion_data = {"advertiserId": "bee3f376-4150-4818-944b-f015395229da", "advertiserIdEnabled": "true", "af_events_api": "1", "af_preinstalled": "false", "af_timestamp": "1664447166908", "af_v": "0da35dd1c1cf4e9383703598bade509b61dd9fd4", "af_v2": "6f3de366cbb1a0ea5609657ffc0c92047420652f", "appUserId": "ac632704-5603-4e36-9699-5cdc608d71c7", "app_version_code": "169", "app_version_name": "5.2.0", "appsflyerKey": "nvTCkGCccZLQAC6zydZDMJ", "batteryLevel": "11.0", "brand": "OPPO", "carrier": "", "cell": {"mcc": 0, "mnc": 0}, "cksm_v1": "a6901083eeb38a174f1d6f154089afaffc", "counter": "1", "country": "US", "date1": "2022-09-29_155008+0530", "date2": "2022-09-29_155008+0530", "device": "CPH1609", "deviceData": {"arch": "", "btch": "no", "btl": "11.0", "build_display_id": "CPH1609EX_11_A.32_191228", "cpu_abi": "arm64-v8a", "cpu_abi2": "", "dim": {"d_dpi": "480", "size": "2", "x_px": "1080", "xdp": "403.411", "y_px": "1920", "ydp": "399.737"}, "sensors": [{"sN": "MAGNETOMETER", "sT": 2, "sV": "MTK", "sVE": [12.9375, -57.375, -92.3125], "sVS": [11.9375, -57.375, -91.4375]}, {"sN": "ACCELEROMETER", "sT": 1, "sV": "MTK", "sVE": [-0.043, 1.651, 9.602], "sVS": [-0.058, 1.67, 9.64]}, {"sN": "GYROSCOPE", "sT": 4, "sV": "MTK", "sVE": [-0.005783081, -0.022857666, -0.22259521], "sVS": [-0.010025024, 0.007385254, -0.0057373047]}]}, "deviceType": "user", "disk": "2565/53694", "exception_number": 0, "firstLaunchDate": "2022-09-29_102607+0000", "iaecounter": "0", "installDate": "2022-09-29_102008+0000", "installer_package": "com.google.android.packageinstaller", "isFirstCall": "true", "isGaidWithGps": "true", "ivc": false, "kef4553": "a6c004a7679d1af848181d1b0c531a0d591a180d5a1e1b", "lang": "English", "lang_code": "en", "last_boot_time": 1664444876761, "meta": {"ddl": {"from_fg": 290, "status": "ERROR", "timeout_value": 3000}, "first_launch": {"init_to_fg": 858, "start_with": "application"}}, "model": "CPH1609", "network": "WIFI", "open_referrer": "android-app://com.oppo.launcher", "operator": "", "p_receipt": {"an": {"dbg": false, "hk": ";"}, "pr": {"ac": "0", "ah": "zygote64_32", "ai": "0", "ak": "default", "al": "cortex-a53", "am": "default", "an": "cortex-a53", "ap": "root", "ar": "mt6755", "as": "arm64-v8a", "at": "arm64-v8a,armeabi-v7a,armeabi", "au": "armeabi-v7a,armeabi", "av": "arm64-v8a"}}, "platformextension": "android_native", "product": "CPH1609", "referrers": [{"api_ver": 83241310, "api_ver_name": "32.4.13-21 [0] [PR] 474870057", "click_ts": 1664446513, "google_custom": {"click_server_ts": 1664446513, "install_begin_server_ts": 0, "install_version": null, "instant": false}, "install_begin_ts": 0, "latency": 929, "referrer": "af_tranid=TPqhaPbhF-zC9_8ya-nFTw&goalid_1=38008&af_cost_value=0&af_ua=Mozilla/5.0 (Linux; Android 11.0.0; Nokia 6 Build/TA-1025) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/105.0.5195.124 Mobile Safari/537.36&af_cost_model=cpi&af_c_id=14930141&publisher_id=6304_indianoem&pid=mobupps_int&sub_publisher_id=6304_indianoem&af_click_lookback=7d&af_prt=mobuppagency&af_adset={file_id}&af_ad=Acko_IN_AND_NR_CPA_WL_New&transaction_id=1027944fa14f63ca8c7ceec26136bd&is_incentivized={categories}&af_cost_currency=USD&af_siteid=6304_indianoem&af_sub_siteid=6304_indianoem&advertising_id=88093b97-62bb-4103-a6fa-a287f36f6b6c&af_ad_id=14930141&c={offer_ref_id}", "response": "OK", "source": "google", "type": "store"}], "registeredUninstall": false, "rfr": {"clk": "1664446513", "code": "0", "install": "0", "instant": false, "val": "af_tranid=TPqhaPbhF-zC9_8ya-nFTw&goalid_1=38008&af_cost_value=0&af_ua=Mozilla/5.0 (Linux; Android 11.0.0; Nokia 6 Build/TA-1025) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/105.0.5195.124 Mobile Safari/537.36&af_cost_model=cpi&af_c_id=14930141&publisher_id=6304_indianoem&pid=mobupps_int&sub_publisher_id=6304_indianoem&af_click_lookback=7d&af_prt=mobuppagency&af_adset={file_id}&af_ad=Acko_IN_AND_NR_CPA_WL_New&transaction_id=1027944fa14f63ca8c7ceec26136bd&is_incentivized={categories}&af_cost_currency=USD&af_siteid=6304_indianoem&af_sub_siteid=6304_indianoem&advertising_id=88093b97-62bb-4103-a6fa-a287f36f6b6c&af_ad_id=14930141&c={offer_ref_id}"}, "sc_o": "p", "sdk": "23", "sig": "3B7F0E749314CB299BCBE1ED63059310E280C7DEA8A49C07593D0B267201D527", "timepassedsincelastlaunch": "-1", "tokenRefreshConfigured": false, "uid": "1664447163835-3596080400345027946"}

inapp_data = {}

event_data = []

Appsflyer_data = {"Key": "nvTCkGCccZLQAC6zydZDMJ", "id": "com.acko.android", "build_number": "6.5.2", "register": true}



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

    url = 'https://conversions.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

    headers = {
        "Accept-Encoding"   : "gzip",
        "Content-Type"      : "application/octet-stream",
        "User-Agent"        : get_ua(device_data)
    }

    params = {
        "app_id"        : campaign_data.get('package_name'),
        "buildnumber"   : campaign_data.get('appsflyer').get('buildnumber'),
    }
    app_data['cdn_token']=get_cdn_token(campaign_data.get('package_name'),campaign_data.get('appsflyer').get('key'))

    app_data['session_time'] = time.time()

    data = {
        "advertiserId"          : device_data.get('adid'),
        "advertiserIdEnabled"   : "true",
        "af_events_api"         : "1",
        "af_preinstalled"       : "false",
        "af_timestamp"          : str(int(time.time()*1000)),
        "appUserId"             : app_data.get('appUserId'), 
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
            "sensors": [
          {
            "sN": "MAGNETOMETER", 
            "sT": 2, 
            "sV": "MTK", 
            "sVE": [
                    round(random.uniform(40,60),4),
                    round(random.uniform(-10,-2),4),
                    round(random.uniform(-40,-20),4)
            ], 
            "sVS": [
                    round(random.uniform(40,60),4),
                    round(random.uniform(-10,-2),1),
                    round(random.uniform(-50,-20),4)
            ]
          }, 
          {
            "sN": "ACCELEROMETER", 
            "sT": 1, 
            "sV": "MTK", 
            "sVE": [
                    round(random.uniform(-5,-0),3),
                    round(random.uniform(2,5),3),
                    round(random.uniform(5,10),3)
            ], 
            "sVS": [
                    round(random.uniform(-5,-0),3),
                    round(random.uniform(2,5),3),
                    round(random.uniform(5,10),3)
            ]
          }, 
          {
            "sN": "GYROSCOPE", 
            "sT": 4, 
            "sV": "MTK", 
            "sVE": [
                    round(random.uniform(0,1),9),
                    round(random.uniform(0,1),9),
                    round(random.uniform(0,1),9)
            ], 
            "sVS": [
                    round(random.uniform(0,1),9),
                    round(random.uniform(-1,-0),9),
                    round(random.uniform(-1,-0),8)
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
        "ddl": {
          "from_fg": 425, 
          "net": [
            416, 
            0
          ], 
          "status": "NOT_FOUND", 
          "timeout_value": 3000
        }, 
        "first_launch": {
          "from_fg": 3262, 
          "init_to_fg": 1221, 
          "start_with": "application"
        }, 
        "host": {
          "name": "appsflyersdk.com", 
          "prefix": "mrn8uw-"
        }, 
        "rc": {
          "c_ver": "default.v1.1637149529", 
          "cdn_token": app_data.get('cdn_token'), 
          "delay": 149, 
          "latency": 113, 
          "res_code": 200, 
          "sig": "success"
        }
      },
        "model"             : device_data.get('model'),
        "network"           : device_data.get('network').upper(),
        "open_referrer"     : "android-app://"+campaign_data.get("package_name"),
        "operator"          : device_data.get('carrier'),
        "p_receipt": {
        "an": {
          "dbg": false, 
          "hk": ";"
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
        "tokenRefreshConfigured"    : False,
    }

    if campaign_data.get('sig'):
        data["sig"]  = campaign_data.get("sig")


    if conversion_data.get('android_id'):
        data['android_id'] = device_data.get('android_id')
    if conversion_data.get('appUserId'):
        data['appUserId'] = conversion_data.get('appUserId')
    if conversion_data.get('customData'):
        data['customData'] = conversion_data.get('customData')
    if conversion_data.get('fb'):
        data['fb'] =  app_data.get('fb')
    if conversion_data.get('user_emails'):
        data['user_emails'] = conversion_data.get('user_emails')
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

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data))}

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

    url = 'https://launches.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

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
            "sensors": [
          {
            "sN": "MAGNETOMETER", 
            "sT": 2, 
            "sV": "MTK", 
            "sVE": [
                    round(random.uniform(40,60),4),
                    round(random.uniform(-10,-2),4),
                    round(random.uniform(-40,-20),4)
            ], 
            "sVS": [
                    round(random.uniform(40,60),4),
                    round(random.uniform(-10,-2),1),
                    round(random.uniform(-50,-20),4)
            ]
          }, 
          {
            "sN": "ACCELEROMETER", 
            "sT": 1, 
            "sV": "MTK", 
            "sVE": [
                    round(random.uniform(-5,-0),3),
                    round(random.uniform(2,5),3),
                    round(random.uniform(5,10),3)
            ], 
            "sVS": [
                    round(random.uniform(-5,-0),3),
                    round(random.uniform(2,5),3),
                    round(random.uniform(5,10),3)
            ]
          }, 
          {
            "sN": "GYROSCOPE", 
            "sT": 4, 
            "sV": "MTK", 
            "sVE": [
                    round(random.uniform(0,1),9),
                    round(random.uniform(0,1),9),
                    round(random.uniform(0,1),9)
            ], 
            "sVS": [
                    round(random.uniform(0,1),9),
                    round(random.uniform(-1,-0),9),
                    round(random.uniform(-1,-0),8)
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
          "from_fg": 3262, 
          "init_to_fg": 1221, 
          "net": 1699, 
          "start_with": "application"
        }, 
        "gcd": {
          "net": 2957, 
          "retries": 0
        }, 
        "host": {
          "name": "appsflyersdk.com", 
          "prefix": "mrn8uw-"
        }
      },
        "model"             : device_data.get('model'),
        "network"           : device_data.get('network').upper(),
        "open_referrer"     : "android-app://"+campaign_data.get("package_name"),
        "operator"          : device_data.get('carrier'),
        "p_receipt": {
        "an": {
          "dbg": false, 
          "hk": ";"
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
        # "sig"                       : campaign_data.get("sig"),
        "timepassedsincelastlaunch" : str(timeSinceLastCall),
        "tokenRefreshConfigured"    : False,
    }

    if campaign_data.get('sig'):
        data["sig"]  = campaign_data.get("sig")

    if conversion_data.get('android_id'):
        data['android_id'] = device_data.get('android_id')
    if conversion_data.get('appUserId'):
        data['appUserId'] = conversion_data.get('appUserId')
    if conversion_data.get('customData'):
        data['customData'] = conversion_data.get('customData')
    if conversion_data.get('fb'):
        data['fb'] =  app_data.get('fb')
    if conversion_data.get('user_emails'):
        data['user_emails'] = conversion_data.get('user_emails')
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

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data))}

# ==================== Appsflyer Inapps ====================
def appsflyer_inapps( app_data, device_data, eventname= "", eventvalue= "" ):

    def_(app_data,'counter')
    inc_(app_data,'iaecounter')

    method = "post"

    url = 'https://inapps.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

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
        "eventValue"            : json.dumps(eventvalue),
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
        data['appUserId'] = inapp_data.get('appUserId')
    if inapp_data.get('customData'):
        data['customData'] = inapp_data.get('customData')
    if inapp_data.get('fb'):
        data['fb'] =  app_data.get('fb')
    if inapp_data.get('user_emails'):
        data['user_emails'] = inapp_data.get('user_emails')
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
        data['prev_event'] = json.dumps(app_data.get('prev_event'))

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


    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data))}

# ==================== Appsflyer Register ====================
def appsflyer_register( app_data, device_data ):

    method = 'post'

    url = 'https://register.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

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


    if not app_data.get('af_gcm_token'):
        app_data['af_gcm_token'] = util.get_random_string(type='all', size=22)+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(134))

    data['uid'] = app_data.get('uid')
    data['af_gcm_token'] = app_data.get('af_gcm_token')

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': json.dumps(data)}

# ==================== Appsflyer GCDSDK ====================
def appsflyer_gcdsdk( app_data, device_data ):

    method = "get"

    url = 'https://gcdsdk.appsflyer.com/install_data/v4.0/'+campaign_data.get('package_name')

    headers = {
        "Accept-Encoding" : "gzip",
        "User-Agent" : get_ua(device_data)
    }

    params = {
        "device_id" : app_data.get('uid'),
        "devkey" : campaign_data.get('appsflyer').get('key')
    }


    params['device_id'] = app_data.get('uid')

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

    url = 'https://attr.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/androidevent'

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

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':af_cipher(campaign_data.get('appsflyer').get('spiKey'), json.dumps(data))}







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


    if not app_data.get('firstLaunchDate'):

        app_data['firstLaunchDate'] = datetime.utcfromtimestamp(int(time.time())).strftime("%Y-%m-%d_%H%M%S")+"+0000"

    if not app_data.get('af_gcm_token'):
        app_data['af_gcm_token'] = util.get_random_string(type='all', size=22)+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(134))

    if conversion_data.get('fb'):
        app_data['fb'] = str(uuid.uuid4())


    #print 'conversion'
    req  = appsflyer_conversions( app_data, device_data )
    util.execute_request(**req)

    if Appsflyer_data.get('attr'):
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

