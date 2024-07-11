# -*- coding: utf-8 -*-
# update by Sanil
import sys
if int(sys.version_info.major) == 2:
    py_version = 2
else:
    py_version = 3
    import urllib.parse as urlparse
from sdk import installtimenew, util
import time, random, json, uuid
false = False
import datetime
null = None

campaign_data = {
    'package_name'       :'tv.abema.AbemaTV',
    'app_size'           : 80,
    'app_name'           :'AbemaTV',
    'app_version_name'   : '19.60.3',
    'app_version_code'   : '56732',
    'app_id'             : '1074866833',
    'device_targeting'   : True,
    'supported_countries': 'WW',
    'supported_os'       : '15.2',
    'tracker'            : ['adjust'],
    'adjust'         : {
        'app_token'     : 'zro44y7jcdts',
        'sdk'           : 'ios4.34.1',
        },
    'country'   :[('USA',50),('India', 3),('Malaysia', 4),('Indonesia', 1),('Thailand', 2), ('Egypt',1), ('Russia',6), ('USA',10), ('SaudiArabia',1), ('SouthAfrica',1), ('Israel',2), ('Kenya',1), ('Nigeria',1), ('Pakistan',2), ('Qatar',1), ('Brazil',3), ('Mexico',4), ('Canada',5),("UK", 30), ("HongKong",5), ("Spain", 4), ("France",4), ("Australia", 5)],
    'retention':{
                1:85,
                2:82,
                3:80,
                4:78,
                5:75,
                6:72,
                7:70,
                8:68,
                9:65,
                10:60,
                11:55,
                12:50,
                13:45,
                14:40,
                15:35,
                16:33,
                17:30,
                18:28,
                19:26,
                20:20,
                21:19,
                22:18,
                23:17,
                24:16,
                25:15,
                26:14,
                27:13,
                28:12,
                29:11,
                30:10,
                31:9,
                32:8,
                33:7,
                34:6,
                35:5,
            },
        }

#########################################################
#               install() : method                      #
#               parameter : app_data,device_data        #
#                                                       #
#   Contains method calls to simulate App's behaviour   #
#   when the App was openned for first time             #
#########################################################

def install(app_data, device_data):
    ###########     INITIALIZE      ############
    if not app_data.get('times'):
    # print "Please wait installing..."
        installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='ios'),
    app_data['primary_dedupe_token']=str(uuid.uuid4())
    if not app_data.get('adjust_call_time'):
        app_data['adjust_call_time']=int(time.time())
   
    if not device_data.get('idfv_id'):
        app_data['idfv_id'] = str(uuid.uuid4()).upper()
    else:
        app_data['idfv_id'] = device_data.get('idfv_id')

    if not app_data.get('fb_anon_id'):
        app_data['fb_anon_id'] = str(uuid.uuid4()).upper()

    if not app_data.get('skadn_registered_at'):
        app_data['skadn_registered_at']=get_date(app_data,device_data)
    attribution_token(app_data)

    # user_detail=util.register_user(device_data.get('locale').get('country'))
    # app_data['email']=user_detail.get('user').get('email')
    ################generating_realtime_differences##################
    s1=2
    s2=3
    a1=0
    a2=0
    in1=7
    in2=11
    e1=1
    e2=9
    id1=0
    id2=0
    click_time_iad3=False


    # print '\n'+'Adjust : SESSION____________________________________'
    request=adjust_session(campaign_data, app_data, device_data,t1=s1,t2=s2)
    util.execute_request(**request)

    # print '\n'+'Adjust : SDK CLICK____________________________________'
    request=adjust_sdkclick(campaign_data, app_data, device_data,click_time=click_time_iad3,source='apple_ads',t1=id1,t2=id2,)
    util.execute_request(**request)

    # print '\n'+'Adjust : SDK CLICK____________________________________'
    request=adjust_sdkclick(campaign_data, app_data, device_data,click_time=click_time_iad3,source='deeplink',t1=id1,t2=id2,)
    util.execute_request(**request)

    # print '\n'+'Adjust : ATTRIBUTION____________________________________'
    request=adjust_attribution(campaign_data, app_data, device_data,t1=a1,t2=a2,initiated_by='backend')
    util.execute_request(**request)

    # print '\n'+'Adjust : SDK INFO____________________________________'
    request=adjust_sdk_info(campaign_data, app_data, device_data,click_time=click_time_iad3,source='att',t1=id1,t2=id2,)
    util.execute_request(**request)

    # req =adjust_event(campaign_data, app_data, device_data,t1=0,t2=0,event_token='')
    # util.execute_request(**req)

    

    return {'status':True}

#########################################################
#            Open      : Methods                        #
#            parameter : app_data,device_data           #
#                                                       #
#    Contains method calls to simulate App's behaviour  #
#      when the App was openned after first-open        #
#########################################################

def open(app_data, device_data,day=1):
    if app_data.get('times'):
        if not app_data.get('adjust_call_time'):
            app_data['adjust_call_time']=int(time.time())
        ################generating_realtime_differences##################
        s1=2
        s2=3
        a1=0
        a2=0
        in1=7
        in2=11
        e1=1
        e2=9


        # print '\n'+'Adjust : SESSION____________________________________'
        request=adjust_session(campaign_data, app_data, device_data,t1=s1,t2=s2,isOpen=True)
        util.execute_request(**request)

    
        
    return {'status':True}




###################################################################
# adjust_session()  : method
# parameter         : campaign_data, app_data, device_data,isOpen
#
# Simulates Adjust's behaviour whenever the App gets open.
###################################################################
def adjust_session(campaign_data, app_data, device_data,t1=0,t2=0,isOpen=False,callback_params=None,partner_params=None):
    created_at=get_date(app_data,device_data)
    make_session_count(app_data,device_data)
    app_data['subsession_count'] = 0
    method = "post"
    url = 'https://app.adjust.com/session'
    headers = {
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip,deflate, br",
        "Accept-Language" : device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        "Client-Sdk" : campaign_data.get('adjust').get('sdk'),
        "Content-Type" : "application/x-www-form-urlencoded",
        "User-Agent" : campaign_data.get('app_name')+'/'+campaign_data.get('app_version_code')+' CFNetwork/'+device_data.get('cfnetwork').split('_')[0]+' Darwin/'+device_data.get('cfnetwork').split('_')[1],
        }
    params = {}
    data = {
        "app_token" : campaign_data.get('adjust').get('app_token'),
        "app_version" : campaign_data.get('app_version_code'),
        "app_version_short" : campaign_data.get('app_version_name'),
        "att_status":0,
        "attribution_deeplink" : "1",
        "bundle_id" : campaign_data.get('package_name'),
        "callback_params":callback_params,
        "created_at" : created_at,
        "device_name" : device_data.get('device_platform'),
        "device_type" : device_data.get('device_type'),
        "environment" : "production",
        "event_buffering_enabled" : 0,
        # "fb_anon_id":app_data.get('fb_anon_id'),
        # "idfa":device_data.get('adid').upper(),
        "idfv" : app_data.get('idfv_id'),
        "installed_at" : get_date_by_ts(app_data,device_data,ts=app_data.get("times").get("install_complete_time")),
        "needs_response_details" : 1,
        "os_name" : "ios",
        "os_version" : device_data.get('os_version'),
        'primary_dedupe_token':app_data.get('primary_dedupe_token'),
        # 'partner_params':partner_params,
        # "push_token":app_data.get('push_token'),
        "sent_at" : datetime.datetime.utcfromtimestamp(time.time()+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        "session_count" : app_data.get('session_count'),
        "skadn_registered_at":app_data.get('skadn_registered_at'),
        'started_at':app_data.get('started_at'),

        }
    if isOpen:
        def_(app_data,'subsession_count')
        def_sessionLength(app_data)
        data['last_interval'] = get_lastInterval(app_data)
        data['session_length'] = int(time.time())-app_data.get('adjust_call_time')
        data['subsession_count'] = app_data.get('subsession_count')
        data['time_spent'] = int(time.time())-app_data.get('adjust_call_time')
        app_data['fb_anon_id']=str(uuid.uuid4()).upper()
        data['fb_anon_id']=app_data.get('fb_anon_id')
        app_data['primary_dedupe_token']=str(uuid.uuid4())
        data['primary_dedupe_token']=app_data.get('primary_dedupe_token')

    if app_data.get('push_token'):
        data['push_token']=app_data.get('push_token')
    if callback_params:
        data['callback_params'] = callback_params

    return {'url':url, 'httpmethod':method, 'headers':headers, 'params':params, 'data':data}


###################################################################
# adjust_event(): method
# parameter     : campaign_data, app_data, device_data,
#                 event_token,callback_params,partner_params
#
# Simulates Adjust's behaviour incase of an in-app event.
###################################################################
def adjust_event(campaign_data, app_data, device_data,t1=0,t2=0,event_token='',callback_params=None,partner_params=None):
    if not app_data.get('event_count'):
        app_data['event_count'] = 1
    else:
        app_data['event_count'] += 1
    created_at=get_date(app_data,device_data)
    time.sleep(random.randint(t1,t2))
    time_spent=int(time.time())-app_data.get('adjust_call_time')
    method = "post"
    url = 'https://app.adjust.com/event'
    headers = {
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip,deflate, br",
        "Accept-Language" : device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        "Client-Sdk" : campaign_data.get('adjust').get('sdk'),
        "Content-Type" : "application/x-www-form-urlencoded",
        "User-Agent" : campaign_data.get('app_name')+'/'+campaign_data.get('app_version_code')+' CFNetwork/'+device_data.get('cfnetwork').split('_')[0]+' Darwin/'+device_data.get('cfnetwork').split('_')[1],
        
    }
    params = {}
    data = {
        'app_token':campaign_data.get('adjust').get('app_token'),
        'app_version':campaign_data.get('app_version_code'),
        'app_version_short':campaign_data.get('app_version_name'),
        "att_status":0,
        'attribution_deeplink':"1",
        'bundle_id':campaign_data.get('package_name'),
        'callback_params':callback_params,
        'created_at':created_at,  
        'device_name':device_data.get('device_platform'),
        'device_type':device_data.get('device_type'),
        'environment':"production",
        'event_buffering_enabled':0,
        'event_count':app_data.get('event_count'),
        'event_token':event_token,
        # 'fb_anon_id':app_data.get('fb_anon_id'),
        'idfa':device_data.get('adid').upper(),
        'idfv':app_data.get('idfv_id'),
        'installed_at':get_date_by_ts(app_data,device_data,ts=app_data.get("times").get("install_complete_time")),
        'needs_response_details':1,
        'os_name':"ios",
        'os_version':device_data.get('os_version'),
        # 'partner_params':partner_params,
        # "push_token" : app_data.get('push_token'),
        'primary_dedupe_token':app_data.get('primary_dedupe_token'),
        # 'queue_size':2,
        'sent_at': datetime.datetime.utcfromtimestamp(time.time()+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'session_count': app_data.get('session_count'),
        "session_length" : time_spent,
        "skadn_registered_at":app_data.get('skadn_registered_at'),
        "subsession_count" : app_data.get('subsession_count'),
        'started_at':app_data.get('started_at'),
        "time_spent" : time_spent,
        }

    if app_data.get('push_token'):
        data['push_token']=app_data.get('push_token')
    if callback_params:
        data['callback_params'] = json.dumps(callback_params)
    if partner_params:
        data['partner_params']  = json.dumps(partner_params)
 
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params':None, 'data': data}
###################################################################
# adjust_attribution()  : method
# parameter             : campaign_data, app_data, device_data
#
# To acknowledge and check the nature of install
###################################################################
def adjust_attribution(campaign_data, app_data,device_data,t1=0,t2=0,initiated_by=''):
    created_at=get_date(app_data,device_data)
    time.sleep(random.randint(t1,t2))
    method = "get"
    url = 'https://app.adjust.com/attribution'
    headers = {
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        "Client-Sdk" : campaign_data.get('adjust').get('sdk'),
        "User-Agent" : campaign_data.get('app_name')+'/'+campaign_data.get('app_version_code')+' CFNetwork/'+device_data.get('cfnetwork').split('_')[0]+' Darwin/'+device_data.get('cfnetwork').split('_')[1],
        }
    params = {
        "app_token" : campaign_data.get('adjust').get('app_token'),
        "app_version" : campaign_data.get('app_version_code'),
        "app_version_short" : campaign_data.get('app_version_name'),
        "att_status":0,
        "attribution_deeplink" : "1",
        "bundle_id" : campaign_data.get('package_name'),
        "created_at" : created_at,
        "device_name" : device_data.get('device_platform'),
        "device_type" : device_data.get('device_type'),
        "environment" : "production",
        "event_buffering_enabled" : 0,
        # "idfa":device_data.get('adid').upper(),
        "idfv" : app_data.get('idfv_id'),
        "initiated_by" : initiated_by,
        'installed_at':get_date_by_ts(app_data,device_data,ts=app_data.get("times").get("install_complete_time")),
        "needs_response_details" : 1,
        "os_name" : "ios",
        "os_version" : device_data.get('os_version'),
        "primary_dedupe_token":app_data.get('primary_dedupe_token'),
        "skadn_registered_at":app_data.get('skadn_registered_at'),
        'started_at':app_data.get('started_at'),
        "sent_at" : datetime.datetime.utcfromtimestamp(time.time()+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        }
    data = None

    if app_data.get('push_token'):
        params['push_token']=app_data.get('push_token')


    return {'url':url, 'httpmethod':method, 'headers':headers, 'params':params, 'data':data}



# =============================sdkinfo=========================================
def adjust_sdk_info(campaign_data, app_data, device_data,click_time='',source='',t1=0,t2=0,callback_params=None,partner_params=None):
    created_at=get_date(app_data,device_data)
    time.sleep(random.randint(t1,t2))
    def_(app_data,'subsession_count')
    time_spent=int(time.time())-app_data.get('adjust_call_time')
    method = "post"
    url = 'https://app.adjust.com/sdk_info'
    headers = {
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip,deflate, br",
        "Accept-Language" : device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        "Client-Sdk" : campaign_data.get('adjust').get('sdk'),
        "Content-Type" : "application/x-www-form-urlencoded",
        "User-Agent" : campaign_data.get('app_name')+'/'+campaign_data.get('app_version_code')+' CFNetwork/'+device_data.get('cfnetwork').split('_')[0]+' Darwin/'+device_data.get('cfnetwork').split('_')[1],
        }
    params = {

        }

    if not app_data.get('push_token'):
        app_data['push_token']=util.get_random_string('hex',64)

    data = {
        "app_token" : campaign_data.get('adjust').get('app_token'),
        "app_version" : campaign_data.get('app_version_code'),
        "app_version_short" : campaign_data.get('app_version_name'),
        "att_status"   :        "0",
        "attribution_deeplink" : "1",
        "bundle_id" : campaign_data.get('package_name'),
        "callback_params":callback_params,
        "created_at" : created_at,
        "device_name" : device_data.get('device_platform'),
        "device_type" : device_data.get('device_type'),
        "environment" : "production",
        "event_buffering_enabled" : 0,
        # "fb_anon_id":app_data.get('fb_anon_id'),
        "idfa":device_data.get('adid').upper(),
        "idfv" : app_data.get('idfv_id'),
        "installed_at" : get_date_by_ts(app_data,device_data,ts=app_data.get("times").get("install_complete_time")),
        "needs_response_details" : 1,
        "os_name" : "ios",
        "os_version" : device_data.get('os_version'),
        "primary_dedupe_token":app_data.get('primary_dedupe_token'),
        # "push_token" :app_data.get('push_token'),
        "sent_at" : datetime.datetime.utcfromtimestamp(time.time()+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        "session_count" : app_data.get('session_count',1),
        "session_length" : time_spent,
        'started_at':app_data.get('started_at'),
        "source" : source,
        "subsession_count" : app_data.get('subsession_count'),
        "time_spent" : time_spent,
        }

    return {'url':url, 'httpmethod':method, 'headers':headers, 'params':params, 'data':data}

###################################################################
# adjust_sdkclick() : method
# parameter         : campaign_data, app_data, device_data
#
# Simulates Adjust's behaviour incase of In-organic install.
###################################################################
def adjust_sdkclick(campaign_data, app_data, device_data,click_time='',source='',t1=0,t2=0,push_token=None,callback_params=None,partner_params=None):
    created_at=get_date(app_data,device_data)
    time.sleep(random.randint(t1,t2))
    def_(app_data,'subsession_count')
    time_spent=int(time.time())-app_data.get('adjust_call_time')
    method = "post"
    url = 'https://app.adjust.com/sdk_click'
    headers = {
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip,deflate, br",
        "Accept-Language" : device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        "Client-Sdk" : campaign_data.get('adjust').get('sdk'),
        "Content-Type" : "application/x-www-form-urlencoded",
        "User-Agent" : campaign_data.get('app_name')+'/'+campaign_data.get('app_version_code')+' CFNetwork/'+device_data.get('cfnetwork').split('_')[0]+' Darwin/'+device_data.get('cfnetwork').split('_')[1],
        }
    params = {

        }
    data = {
        "app_token" : campaign_data.get('adjust').get('app_token'),
        "app_version" : campaign_data.get('app_version_code'),
        "app_version_short" : campaign_data.get('app_version_name'),
        "att_status"   :        "0",
        "attribution_deeplink" : "1",
        "attribution_token":app_data.get('asa_data'),
        "bundle_id" : campaign_data.get('package_name'),
        "callback_params":callback_params,
        "created_at" : created_at,
        "device_name" : device_data.get('device_platform'),
        "device_type" : device_data.get('device_type'),
        "environment" : "production",
        "event_buffering_enabled" : 0,
        "fb_anon_id":app_data.get('fb_anon_id'),
        "idfa":device_data.get('adid').upper(),
        "idfv" : app_data.get('idfv_id'),
        "installed_at" : get_date_by_ts(app_data,device_data,ts=app_data.get("times").get("install_complete_time")),
        "last_interval" : get_lastInterval(app_data),
        "needs_response_details" : 1,
        "os_name" : "ios",
        "os_version" : device_data.get('os_version'),
        'primary_dedupe_token':app_data.get('primary_dedupe_token'),
        # "partner_params":partner_params,
        # "push_token" : app_data.get('push_token'),
        "sent_at" : datetime.datetime.utcfromtimestamp(time.time()+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        "session_count" : app_data.get('session_count',1),
        "session_length" : time_spent,
        "source" : source,
        'started_at':app_data.get('started_at'),
        "subsession_count" : app_data.get('subsession_count'),
        "time_spent" : time_spent,
        }
    if source=='iad3':
        if data.get('deeplink'):
            del data['deeplink']
        if data.get('click_time'):
            del data['click_time']
        data['details']=json.dumps({"Version3.1":{"iad-attribution":"false"}})

    if source=='deeplink' and click_time:
        if not data.get('deeplink'):
            data['deeplink']="CONSTANT"
            data['click_time']='sdk_clk_time'

    return {'url':url, 'httpmethod':method, 'headers':headers, 'params':params, 'data':data}



# =====================================other functionality===================================
def def_sessionLength(app_data,forced=False):
    if not app_data.get('sessionLength') or forced:
        app_data['sessionLength'] = 0

def push_token(app_data):
    if not app_data.get('push_token'):
        app_data['push_token']=util.get_random_string('hex',51)


def set_sessionLength(app_data,forced=False,length=0):
    def_sessionLength(app_data,forced)
    app_data['sessionLength'] += length

def def_(app_data,paramName):
    if not app_data.get(paramName):
        app_data[paramName] = 0

def set_appCloseTime(app_data):
    app_data['appCloseTime'] = int(timestamp())

def check_appCloseTime(app_data):
    if not app_data.get('appCloseTime'):
        set_appCloseTime(app_data)

def get_lastInterval(app_data):
    check_appCloseTime(app_data)
    return int(timestamp()) - app_data.get('appCloseTime')

def timestamp():
    return time.time()

def def_sec(app_data,device_data):
    timez = device_data.get('timezone')
    sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
    if int(timez) < 0:
        sec = (-1) * sec
    if not app_data.get('sec'):
        app_data['sec'] = sec

def get_date(app_data,device_data):
    def_sec(app_data,device_data)
    date = datetime.datetime.utcfromtimestamp((timestamp()-random.randint(4,12))+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')
    return str(date)


def device_id(app_data):
    if not app_data.get('x-device-id'):
        app_data['x-device-id']=str(uuid.uuid4()).upper()

def get_date_by_ts(app_data,device_data,ts):
    def_sec(app_data,device_data)
    date = datetime.datetime.utcfromtimestamp(ts+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')
    return date

def get_date1(app_data,device_data,para1=0,para2=0):
    time.sleep(random.randint(para1,para2))
    make_sec(app_data,device_data)
    date = datetime.datetime.utcfromtimestamp((time.time())+app_data.get('sec')).strftime("%Y%m%d%H%M%S")
    return date


def get_signature(campaign_data, app_data, device_data,app_secret=False,action=False,idfa=False,created_at=False):
    auth= 'Signature secret_id="'+str(campaign_data.get('adjust').get('secret_id'))+'",signature="'+util.sha256(str(app_secret)+str(action)+str(idfa)+str(created_at))+'",algorithm="sha256",headers="app_secret activity_kind idfa created_at"'
    return auth

def make_session_count(app_data,device_data):
    if not app_data.get('session_count'):
        app_data['session_count'] = 1
    else:
        app_data['session_count'] += 1

    return app_data.get('session_count')

def make_sec(app_data,device_data):
    timez = device_data.get('timezone')
    sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
    if int(timez) < 0:
        sec = (-1) * sec
    if not app_data.get('sec'):
        app_data['sec'] = sec

    return app_data.get('sec')

def get_timestamp(para1=0,para2=0):
    time1 = int(time.time())
    return time1


def install_receipt(app_data):
    if not app_data.get('install_receipt'):
        app_data['install_receipt'] = 'MIIS' + util.get_random_string('google_token', random.randint(6000, 6500))
    return app_data.get('install_receipt')


def attribution_token(app_data):
    alpha_numeric_elements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789=/+'
    app_data['asa_data']=''.join(random.choice(alpha_numeric_elements) for i in range(560))


