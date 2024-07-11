# -*- coding: utf8 -*-
# Sanil
from sdk import installtimenew
from sdk import util
import urllib,urlparse
import time
import random
import json


#------------------------------------------- app_data -------------------------------------------------------------------------------------
# 'randomized_device_token', 'install_begin_ts', 'referrer', 'session_id', 'times', 'close_count', 'identity_id', 'install', 'mobile_number'

#----------------------------- Campaign Data ------------------------------------------------------
campaign_data = {
    'package_name'       :'id.co.adira.adiraku',
    'app_size'           : 29,
    'app_name'           :'adiraku – Kredit & Pinjaman',
    'app_version_name'   : '2.16.1',
    'app_version_code'   : '38',
    'ctr'                : 6,
    'no_referrer'        : False,
    'device_targeting'   : True,
    'supported_countries': 'WW',
    'supported_os'       : '12',
    'tracker'            : ['branch'],
    'branch':{
        'key'  :'key_live_pcZmPsV97TUJHR017Z8qohhetBc6d9B3',
        'sdk':'android5.7.1',
        'sdk_version':'5.7.1'
    },
    'country'   :[('USA',50),('India', 3),('Malaysia', 4),('Indonesia', 1),('Thailand', 2), ('Egypt',1), ('Russia',6), ('USA',10), ('SaudiArabia',1), ('SouthAfrica',1), ('Israel',2), ('Kenya',1), ('Nigeria',1), ('Pakistan',2), ('Qatar',1), ('Brazil',3), ('Mexico',4), ('Canada',5),("UK", 30), ("HongKong",5), ("Spain", 4), ("France",4), ("Australia", 5)],
    'retention':{
        1:85,
        2:82,
        3:78,
        4:75,
        5:70,
        6:66,
        7:62,
        8:58,
        9:55,
        10:50,
        11:48,
        12:45,
        13:40,
        14:39,
        15:38,
        16:37,
        17:35,
        18:35,
        19:34,
        20:33,
        21:32,
        22:31,
        23:30,
        24:29,
        25:29,
        26:28,
        27:27,
        28:26,
        29:25,
        30:25,
        31:24,
        32:23,
        33:23,
        34:22,
        35:22,
        36:21,
        37:20,
        38:19,
        39:19,
        40:18,
        41:16,
        42:16,
        43:16,
        44:15,
        45:15,
        46:14,
        47:13,
        48:13,
        49:12,
        50:11,
        51:11,
        52:10,
        53:9,
        54:9,
        55:8,
        56:7,
        57:6,
        58:5,
        59:4,
        60:3
    }
}
#======================================================


#####################################################
def branch_install(app_data, device_data):
    url = 'https://api2.branch.io/v1/install'
    httpmethod = 'post'
    headers ={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Dalvik/2.1.0'+' (Linux; U; Android '+ device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+  device_data.get('build')+')',
        'Accept-Encoding': 'gzip'
    }
    params =None
    data ={
        "plugin_name": "ReactNative",
        "plugin_version": "5.9.2",
        "hardware_id": device_data.get('android_id'),
        "is_hardware_id_real": True,
        "brand": device_data.get('brand'),
        "model": device_data.get('model'),
        "screen_dpi": int(device_data.get('dpi')),
        "screen_height": int(device_data.get('resolution').split('x')[0]),
        "screen_width": int(device_data.get('resolution').split('x')[1]),
        "wifi": True,
        "ui_mode": "UI_MODE_TYPE_NORMAL",
        "os": "Android",
        "os_version": int(device_data.get('sdk')),
        'cpu_type': device_data.get('cpu'),
        "build": device_data.get("build"),
        'locale': device_data.get('locale').get('language')+'_'+device_data.get('locale').get('country').upper(),
        "connection_type": "wifi",
        "os_version_android": device_data.get('os_version'),
        "language": device_data.get('locale').get('language'),
        "local_ip": device_data.get('private_ip'),
        "partner_data": {},
        "app_version": campaign_data.get('app_version_name'),
        "facebook_app_link_checked": False,
        "debug": False,
        "update": 0,
        "latest_install_time": app_data.get('install'),
        "latest_update_time": app_data.get('install'),
        "first_install_time": app_data.get('install'),
        "previous_update_time": 0,
        "environment": "FULL_APP",
        "clicked_referrer_ts": app_data.get('install_begin_ts') - random.randint(30, 60),
        "install_begin_ts": app_data.get('install_begin_ts'),
        "initial_referrer": "android-app://com.microvirt.launcher2",
        "metadata": {},
        "lat_val": 0,
        "google_advertising_id": device_data.get('adid'),
        "instrumentation": {
            "v1/install-qwt": "0"
        },
        "advertising_ids": {
            "aaid"          : device_data.get('adid')
                        },
        "sdk": campaign_data.get('branch').get('sdk'),
        "branch_key": campaign_data.get('branch').get('key'),
        "retryNumber": 0
    }
    if app_data.get('referrer'):
        data['install_referrer_extras'] = app_data.get('referrer')
        if "link_click_id" in dict(urlparse.parse_qs(urllib.unquote(app_data.get('referrer')))):
            data['link_click_id'] = dict(urlparse.parse_qs(urllib.unquote(app_data.get('referrer')))).get('link_click_id')[-1]
            data['link_identifier'] = dict(urlparse.parse_qs(urllib.unquote(app_data.get('referrer')))).get('link_click_id')[-1]


    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':json.dumps(data).replace(': ', ':').replace(', ', ',')}

#----------------------------------------------------------------------------------------
def branch_profile(app_data, device_data, randomized_device_token =None,identity='',identity_id='',session_id=''):
    url = 'https://api2.branch.io/v1/profile'

    httpmethod = 'post'

    headers ={
        'Content-Type'          : 'application/json',
        'Accept'                : 'application/json',
        'User-Agent'            : 'Dalvik/2.1.0'+' (Linux; U; Android '+ device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+  device_data.get('build')+')',
        'Accept-Encoding'       : 'gzip'
    }

    params =None

    data ={
        "branch_key"                : campaign_data.get('branch').get('key'),
        "brand"                     : device_data.get('brand'),
        "country"                   : device_data.get('locale').get('country'),
        "randomized_device_token"     : randomized_device_token,
        "google_advertising_id"     : device_data.get('adid'),
        "hardware_id"               : device_data.get('android_id'),
        "identity"                  : identity,
        "identity_id"               : identity_id,
        "instrumentation"           :
        {
            "v2/event/custom-brtt"  :str(random.randint(350,420)),
            "v1/profile-qwt"        : "2"
        },
        "is_hardware_id_real"       : True,
        "language"                  : device_data.get('locale').get('language'),
        "lat_val"                   : 0,
        "local_ip"                  : device_data.get('private_ip'),
        "metadata"                  : {},
        "model"                     : device_data.get('model'),
        "os"                        : "Android",
        "os_version"                : int(device_data.get('sdk')),
        "randomized_device_token":app_data.get('randomized_device_token'),
        "randomized_bundle_token":app_data.get('randomized_bundle_token'),

        "retryNumber"               : 0,
        "screen_dpi"                : int(device_data.get('dpi')),
        "screen_height"             : int(device_data.get('resolution').split('x')[0]),
        "screen_width"              : int(device_data.get('resolution').split('x')[1]),
        "sdk"                       : campaign_data.get('branch').get('sdk'),
        "session_id"                : session_id,
        "ui_mode"                   : "UI_MODE_TYPE_NORMAL",
        "wifi"                      : True
        }

    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':json.dumps(data).replace(': ', ':').replace(', ', ',')}



def branch_event(app_data, device_data, event_name=None, randomized_device_token =None, custom_data = None, content_items = None,instrumentation=None,event_type='custom'):
    url = 'https://api2.branch.io/v2/event/'+event_type

    httpmethod = 'post'

    headers ={
        'Content-Type'              : 'application/json',
        'Accept'                    : 'application/json',
        'User-Agent'                : 'Dalvik/2.1.0'+' (Linux; U; Android '+ device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+  device_data.get('build')+')',
        'Accept-Encoding'           : 'gzip'
    }
    params = None

    data ={
        "name"                      : event_name,
        "custom_data"               : custom_data,
        "branch_key"                : campaign_data.get('branch').get('key'),
        "instrumentation"           : instrumentation,
        "metadata"                  : {},
        "retryNumber"               : 0,
        "is_hardware_id_real"       : False,
        "retryNumber"               : 0,
        "user_data"                 : {
            "android_id"            : device_data.get('android_id'),
            "brand"                 : device_data.get('brand'),
            "model"                 : device_data.get('model'),
            "screen_dpi"            : int(device_data.get('dpi')),
            "screen_height"         : int(device_data.get('resolution').split('x')[0]),
            "screen_width"          : int(device_data.get('resolution').split('x')[1]),
            "ui_mode"               : "UI_MODE_TYPE_NORMAL",
            "os"                    : "Android",
            "os_version"            : int(device_data.get('sdk')),
            'cpu_type'              : device_data.get('cpu'),
            "build"                 : device_data.get("build"),
            'locale'                : device_data.get('locale').get('language')+'_'+device_data.get('locale').get('country').upper(),
            "connection_type"       : "wifi",
            "os_version_android"    : device_data.get('os_version'),
            "language"              : device_data.get('locale').get('language'),
            "local_ip"              : device_data.get('private_ip'),
            "randomized_device_token":app_data.get('randomized_device_token'),
            "developer_identity"    : "bnc_no_value",
            "app_version"           : campaign_data.get('app_version_name'),
            "sdk"                   : "android",
            "sdk_version"           : campaign_data.get('branch').get('sdk_version'),
            "user_agent"            : device_data.get('User-Agent'),
            "environment"           : "FULL_APP",
            "limit_ad_tracking"     : 0,
            "aaid"                  : device_data.get('adid'),
            # "country"               : device_data.get('locale').get('country'),
            # "randomized_device_token" : randomized_device_token,
        }
        }

    if data.get('custom_data')==None or '':
        del data['custom_data']

    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':json.dumps(data).replace(': ', ':').replace(', ', ',')}


# ----------
def branch_close(app_data, device_data, randomized_device_token = None, identity_id =None, session_id =None):
    url = 'https://api2.branch.io/v1/close'

    httpmethod = 'post'

    headers ={
        'Content-Type'              : 'application/json',
        'Accept'                    : 'application/json',
        'User-Agent'                : 'Dalvik/2.1.0'+' (Linux; U; Android '+ device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+  device_data.get('build')+')',
        'Accept-Encoding'           : 'gzip'
    }

    if not app_data.get('close_count'):
        app_data['close_count'] =1
    else:
        app_data['close_count'] +=1

    params = None

    data ={
        "app_version"               : campaign_data.get('app_version_name'),
        "branch_key"                : campaign_data.get('branch').get('key'),
        "brand"                     : device_data.get('brand'),
        "randomized_device_token"   : randomized_device_token,
        "google_advertising_id"     : device_data.get('adid'),
        "hardware_id"               : device_data.get('android_id'),
        "identity_id"               : identity_id,
        "instrumentation"           :
        {
            "v2/event/standard-brtt": str(random.randint(600, 700)),
            "v1/close-qwt"          : "4"
        },
        "is_hardware_id_real"       : True,
        "language"                  : device_data.get('locale').get('language'),
        "lat_val"                   : 0,
        "local_ip"                  : device_data.get('private_ip'),
        "metadata"                  : {},
        "model"                     : device_data.get('model'),
        "os"                        : "Android",
        "os_version"                : int(device_data.get('sdk')),
        "retryNumber"               : 0,
        "screen_dpi"                : int(device_data.get('dpi')),
        "screen_height"             : int(device_data.get('resolution').split('x')[0]),
        "screen_width"              : int(device_data.get('resolution').split('x')[1]),
        "sdk"                       : campaign_data.get('branch').get('sdk'),
        "session_id"                : session_id,
        "ui_mode"                   : "UI_MODE_TYPE_NORMAL",
        "wifi"                      : True
        }


    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':json.dumps(data).replace(': ', ':').replace(', ', ',')}

#-------------------------------------------------------------------------------------
def branch_open(app_data, device_data, randomized_device_token = None, identity_id =None):
    url = 'https://api2.branch.io/v1/open'
    httpmethod = 'post'
    headers ={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Dalvik/2.1.0'+' (Linux; U; Android '+ device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+  device_data.get('build')+')',
        'Accept-Encoding': 'gzip'
    }
    params = None
    data ={
            "randomized_device_token"   :app_data.get('randomized_device_token'),
            "randomized_bundle_token"   :app_data.get('randomized_bundle_token'),
            "hardware_id"               : device_data.get('android_id'),
            "is_hardware_id_real"       : True,
            "brand"                     : device_data.get('brand'),
            "model"                     : device_data.get('model'),
            "screen_dpi"                : int(device_data.get('dpi')),
            "screen_height"             : int(device_data.get('resolution').split('x')[0]),
            "screen_width"              : int(device_data.get('resolution').split('x')[1]),
            "wifi"                      : True,
            "ui_mode"                   : "UI_MODE_TYPE_NORMAL",
            "os"                        : "Android",
            "os_version"                : int(device_data.get('sdk')),
            "app_version"               : campaign_data.get('app_version_name'),
            'cpu_type'                  : device_data.get('cpu'),
            "build"                     : device_data.get("build"),
            'locale'                    : device_data.get('locale').get('language')+'_'+device_data.get('locale').get('country').upper(),
            "connection_type"           : "wifi",
            "os_version_android"        : device_data.get('os_version'),
            "language"                  : device_data.get('locale').get('language'),
            "local_ip"                  :  device_data.get('private_ip'),
            "partner_data"              : {},
            "initial_referrer"          :"android-app://com.sec.android.app.launcher", #"android-app://id.co.adira.adiraku",
            "facebook_app_link_checked" : False,
            "debug"                     : False,
            "update"                    : 1,
            "latest_install_time"       : app_data.get('install'),
            "latest_update_time"        : app_data.get('install'),
            "first_install_time"        : app_data.get('install'),
            "previous_update_time"      : app_data.get('install'),
            "environment"               : "FULL_APP",
            "metadata"                  : {},
            "advertising_ids"           : {
                        "aaid"          : device_data.get('adid')
            },
            "lat_val"                   : 0,
            "google_advertising_id"     : device_data.get('adid'),
            "instrumentation"           :{
                # "v1/close-brtt"          : str(random.randint(389, 500)),
                "v1/open-qwt"           : "0"
            },
            "sdk"                       : campaign_data.get('branch').get('sdk'),
            "branch_key"                : campaign_data.get('branch').get('key'),
            "retryNumber"               : 0,

            }

    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':json.dumps(data).replace(': ', ':').replace(', ', ',')}
#------------------------------------------------------------------------

def branch_cdn(app_data, device_data, v):
    url = 'https://cdn.branch.io/sdk/uriskiplist_'+v+'.json'

    httpmethod = 'get'

    headers = {
        'User-Agent'    : 'Dalvik/2.1.0'+' (Linux; U; Android '+ device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+  device_data.get('build')+')',
        'Host'          : 'cdn.branch.io',
        'Accept-Encoding' : 'gzip'
    }

    params = None

    data =None

    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


#------------------------------------- events Definition ---------------------------------------

#--------------------------------------- Install Start --------------------------------------------
def install(app_data, device_data):

    if not app_data.get('times'):
        # print "Please wait installing..."
        installtimenew.main(app_data, device_data, app_size=campaign_data.get('app_size'), os='android')
        app_data['install'] =int(time.time()*1000)
        app_data['install_begin_ts'] =int(time.time() - random.randint(120, 180))



    #-------------------------------------- Requests Calling ------------------------------------------------------------
    req=branch_install(app_data,device_data)
    result=util.execute_request(**req)
    try:
        json_result=json.loads(result.get('data'))
        app_data['randomized_bundle_token']=json_result.get('randomized_bundle_token')
        app_data['randomized_device_token']=json_result.get('randomized_device_token')
        app_data['session_id']=json_result.get('session_id')
    except:
        pass

    req=branch_cdn(app_data, device_data, 'v1')
    util.execute_request(**req)


    req = branch_open(app_data, device_data, randomized_device_token =app_data.get('randomized_device_token'), identity_id = app_data.get('identity_id'))
    util.execute_request(**req)


    req=branch_cdn(app_data, device_data, 'v2')
    util.execute_request(**req)

    poss=[True]*30+[False]*70
    random.shuffle(poss)
    if random.choice(poss):
        custom_data={
            "pkg_channel": "google",
            "deviceId": device_data.get('adid'),
            "userId": "",
            "androidId": device_data.get('android_id')
        }
        instrumentation={
            "v1\/install-brtt": str(random.randint(1029,1999)),
            "v2\/event\/custom-qwt":str(random.randint(1,2))
        }
        req=branch_event(app_data, device_data, event_name="login", randomized_device_token =app_data.get('randomized_device_token'), custom_data =custom_data,instrumentation=instrumentation, content_items = None)
        util.execute_request(**req)
        app_data['login'] = True


    #print 'close___branch------------------'
    req = branch_close(app_data, device_data, randomized_device_token =app_data.get('randomized_device_token'), identity_id = app_data.get('identity_id'), session_id = app_data.get('session_id'))
    util.execute_request(**req)

    # print('app_data is :-----------------------------------------------------------------------------------------------------------',app_data)

    return {'status':True}
#-------------------------------------------------------------
def open(app_data, device_data, day =1):
    if app_data.get('times'):
    #print ------------'open__branch---------------------------'
        req = branch_open(app_data, device_data, randomized_device_token =app_data.get('randomized_device_token'), identity_id = app_data.get('identity_id'))
        result=util.execute_request(**req)
        try:
            json_result=json.loads(result.get('data'))
            app_data['randomized_device_token']=json_result.get('randomized_device_token')
            app_data['identity_id']=json_result.get('identity_id')
            app_data['session_id']=json_result.get('session_id')
        except:
            pass

        req=branch_cdn(app_data, device_data, 'v2')
        util.execute_request(**req)
        
        if not app_data.get('login') and day<5:
            poss=[True]*4+[False]*96
            random.shuffle(poss)
            if random.choice(poss):
                custom_data={
                    "pkg_channel": "google",
                    "deviceId": device_data.get('adid'),
                    "userId": "",
                    "androidId": device_data.get('android_id')
                }
                instrumentation={
                    "v1\/install-brtt": str(random.randint(1029,1999)),
                    "v2\/event\/custom-qwt":str(random.randint(1,2))
                }
                req=branch_event(app_data, device_data, event_name="login", randomized_device_token =app_data.get('randomized_device_token'), custom_data =custom_data,instrumentation=instrumentation, content_items = None)
                util.execute_request(**req)
                app_data['login'] = True
        
        req=branch_cdn(app_data, device_data, 'v3')
        util.execute_request(**req)


        # print 'close___branch'
        req = branch_close(app_data, device_data, randomized_device_token =app_data.get('randomized_device_token'), identity_id = app_data.get('identity_id'), session_id = app_data.get('session_id'))
        util.execute_request(**req)


    return {'status':True}
# ================== ==========================