#-*- coding: utf-8 -*-
# created by him@nshu
import sys
if int(sys.version_info.major) == 2:
    py_version = 2
else:
    py_version = 3
    import urllib.parse as urlparse
from datetime import datetime,timedelta
from sdk import installtimenew, util
from hashlib import sha1
import time, random, json,  urllib, uuid, hashlib
false = False
true = True
null = None
campaign_data = {
   'package_name' : 'de.baur.shop',
   'app_name' : 'BAUR - Mode & Wohnen',
   'app_version_name' : '2.15.2',
   'app_version_code' : '8000270',
   'supported_os' : '8',
   'supported_countries' : 'WW',
   'tracker' : ['adjust'],
   'app_size' : 28,
   'adjust' : { 
      'sdk' : 'android4.33.2',
      'app_token' : '1ua29we38wn4',
      'app_secret' : 'Search secret and insert Here',
      'secret_id' : '',
      'algo' : 'sha256',
   }, 
   'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
   'retention' : {1: 85, 2: 82, 3: 78, 4: 75, 5: 70, 6: 66, 7: 62, 8: 58, 9: 55, 10: 50, 11: 48, 12: 45, 13: 40, 14: 39, 15: 38, 16: 37, 17: 35, 18: 35, 19: 34, 20: 33, 21: 32, 22: 31, 23: 30, 24: 29, 25: 29, 26: 28, 27: 27, 28: 26, 29: 25, 30: 25, 31: 24, 32: 23, 33: 23, 34: 22, 35: 22, 36: 21, 37: 20, 38: 19, 39: 19, 40: 18, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 14, 47: 13, 48: 13, 49: 12, 50: 11, 51: 11, 52: 10, 53: 9, 54: 9, 55: 8, 56: 7, 57: 6, 58: 5, 59: 4, 60: 3},
	}
firebase_data = {"url": "/v1/projects/baur-a035d/installations", "x-firebase-client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA", "X-Android-Cert": "0B10038FEB1FD1D5E27DA4C8406F512119DF4595", "x-goog-api-key": "AIzaSyDu1kqAF-NCrSMqJGkov6AKR_9qUou34BU", "data": {"fid": "dnBTki6nR9u1iIrzakI-Ja", "appId": "1:1016208723427:android:6985aabab318ff71", "authVersion": "FIS_v2", "sdkVersion": "a:17.1.3"}}
#================================ Adjust Session ================================
def adjust_session( app_data, device_data):
    url = 'https://app.adjust.com/session'
    httpmethod='post'
    app_data['session_started']=int(time.time())
    if not app_data.get('session_count'):
        app_data['session_count'] = 1
    else:
        app_data['session_count'] +=1
    headers={
        'Client-SDK':campaign_data.get('adjust').get('sdk'),
            'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent': get_ua(device_data),
        'Accept-Encoding':'gzip'
    }
    params={}
    data = {
        'android_uuid':  app_data.get('android_uuid'),
        'api_level':  device_data.get('sdk'),
        'app_token':  campaign_data.get('adjust').get('app_token'),
        'app_version':  campaign_data.get('app_version_name'),
        'attribution_deeplink':  '1',
        'connectivity_type':  '1',
        'country':  device_data.get('locale').get('country'),
        'cpu_type':  device_data.get('cpu'),
        'created_at':  (datetime.utcfromtimestamp(time.time()-random.randint(3,8)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'device_manufacturer':  device_data.get('manufacturer'),
        'device_name':  device_data.get('model'),
        'device_type':  device_data.get('device_type'),
        'display_height':  device_data.get('resolution').split('x')[-2],
        'display_width':  device_data.get('resolution').split('x')[-1],
        'environment':  'production',
        'event_buffering_enabled':  '0',
        'fb_id':  app_data.get('fb_id'),
        'gps_adid':  device_data.get('adid'),
        'gps_adid_attempt':  ' 1',
        'gps_adid_src':  'service',
        'hardware_name':  device_data.get('hardware'),
        'installed_at':  datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'language':  device_data.get('locale').get('language'),
        'last_interval':  '21',
        'needs_response_details':  '1',
        'os_build':  device_data.get('build'),
        'os_name':  'android',
        'os_version':  device_data.get('os_version'),
        'package_name':  campaign_data.get('package_name'),
        'screen_density':  get_screen_density(device_data),
        'screen_format':  get_screen_format(device_data),
        'screen_size':  'normal',
        'sent_at':  (datetime.utcfromtimestamp(time.time()+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'session_count':  app_data.get('session_count'),
        'session_length':  '9',
        'subsession_count':  '1',
        'time_spent':  '9',
        'tracking_enabled':  '1',
        'ui_mode':  '1',
        'updated_at':  datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
    }
    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')
    app_data['subsession']=1
    headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'),'session')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}
#================================ Session End ================================

#================================ Adjust Attribution ================================
def adjust_attribution(app_data,device_data,initiated_by=None):
    url = 'https://app.adjust.com/attribution'
    httpmethod='get'
    headers={
    'Client-SDK':campaign_data.get('adjust').get('sdk'),
    'User-Agent':get_ua(device_data),
    'Accept-Encoding':'gzip',
    }
    data=None
    params = {
        'android_uuid':  app_data.get('android_uuid'),
        'api_level':  device_data.get('sdk'),
        'app_token':  campaign_data.get('adjust').get('app_token'),
        'app_version':  campaign_data.get('app_version_name'),
        'attribution_deeplink':  '1',
        'created_at':  (datetime.utcfromtimestamp(time.time()-random.randint(3,8)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'device_name':  device_data.get('model'),
        'device_type':  device_data.get('device_type'),
        'environment':  'production',
        'event_buffering_enabled':  '0',
        'gps_adid':  device_data.get('adid'),
        'gps_adid_attempt':  '1',
        'gps_adid_src':  'service',
        'initiated_by':  initiated_by,
        'needs_response_details':  '1',
        'os_name':  'android',
        'os_version':  device_data.get('os_version'),
        'package_name':  campaign_data.get('package_name'),
        'sent_at':  (datetime.utcfromtimestamp(time.time()+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'tracking_enabled':  '1',
        'ui_mode':  '1',
    }
    if app_data.get('pushtoken'):
        params['push_token'] = app_data.get('pushtoken')
    headers['Authorization'] = get_auth(params.get('created_at'),params.get('gps_adid'),campaign_data.get('adjust').get('app_secret'),'attribution')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}
#================================ Attrinution End ================================

#================================ Adjust SdkClick ================================
def adjust_sdk_click(app_data,device_data,source=''):
    url = 'https://app.adjust.com/sdk_click'
    httpmethod='post'
    app_data['session_started']=int(time.time())
    headers={
        'Client-SDK': campaign_data.get('adjust').get('sdk'),
            'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent': get_ua(device_data),
        'Accept-Encoding':'gzip',
    }
    params={}
    data = {
        'android_uuid':  app_data.get('android_uuid'),
        'api_level':  device_data.get('sdk'),
        'app_token':  campaign_data.get('adjust').get('app_token'),
        'app_version':  campaign_data.get('app_version_name'),
        'attribution_deeplink':  '1',
        'click_time':          datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'+device_data.get('timezone'),
        'click_time_server':   datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'+device_data.get('timezone'),
        'connectivity_type':  '1',
        'country':  device_data.get('locale').get('country'),
        'cpu_type':  device_data.get('cpu'),
        'created_at':  (datetime.utcfromtimestamp(time.time()-random.randint(3,8)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'device_manufacturer':  device_data.get('manufacturer'),
        'device_name':  device_data.get('model'),
        'device_type':  device_data.get('device_type'),
        'display_height':  device_data.get('resolution').split('x')[-2],
        'display_width':  device_data.get('resolution').split('x')[-1],
        'environment':  'production',
        'event_buffering_enabled':  '0',
        'fb_id':  app_data.get('fb_id'),
        'google_play_instant':  '0',
        'gps_adid':  device_data.get('adid'),
        'gps_adid_attempt':  '1',
        'gps_adid_src':  'service',
        'hardware_name':  device_data.get('hardware'),
        'install_begin_time':  datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
        'install_begin_time_server':  	datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
        'install_version':  campaign_data.get('app_version_name'),
        'installed_at':  datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'language':  device_data.get('locale').get('language'),
        'needs_response_details':  '1',
        'os_build':  device_data.get('build'),
        'os_name':  'android',
        'os_version':  device_data.get('os_version'),
        'package_name':  campaign_data.get('package_name'),
        'referrer':  app_data.get('referrer') or 'utm_source=(not%20set)&utm_medium=(not%20set)',
        'referrer_api':  'google',
        'screen_density':  get_screen_density(device_data),
        'screen_format':  get_screen_format(device_data),
        'screen_size':  'normal',
        'sent_at':  (datetime.utcfromtimestamp(time.time()+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'session_count':  app_data.get('session_count'),
        'session_length':  int(time.time())- app_data.get('session_started'),
        'source':  source,
        'subsession_count':  subsession(app_data),
        'time_spent':  time_spent(app_data),
        'tracking_enabled':  '1',
        'ui_mode':  '1',
        'updated_at':   datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone') or None,
    }
    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')
    headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),data.get('source'),campaign_data.get('adjust').get('app_secret'),'click')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}
#================================ SdkClick End ================================

#================================ Adjust Event ================================
def adjust_events(app_data,device_data,event_token=None,callback = None,patner= None):
    url = 'https://app.adjust.com/event'
    httpmethod='post'
    headers={
        'Client-SDK':campaign_data.get('adjust').get('sdk'),
        'User-Agent':get_ua(device_data),
            'Content-Type':'application/x-www-form-urlencoded',
        'Accept-Encoding':'gzip',    
    }
    params=None
    if not app_data.get('event_count'):
        app_data['event_count']=1
    else:
        app_data['event_count']=app_data['event_count']+1
    data = {
        'android_uuid':  app_data.get('android_uuid'),
        'api_level':  device_data.get('sdk'),
        'app_token':  campaign_data.get('adjust').get('app_token'),
        'app_version':  campaign_data.get('app_version_name'),
        'attribution_deeplink':  '1',
        'connectivity_type':  '1',
        'country':  device_data.get('locale').get('country'),
        'cpu_type':  device_data.get('cpu'),
        'created_at':  (datetime.utcfromtimestamp(time.time()-random.randint(3,8)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'device_manufacturer':  device_data.get('manufacturer'),
        'device_name':  device_data.get('model'),
        'device_type':  device_data.get('device_type'),
        'display_height':  device_data.get('resolution').split('x')[-2],
        'display_width':  device_data.get('resolution').split('x')[-1],
        'environment':  'production',
        'event_buffering_enabled':  '0',
        'event_count':  app_data.get('event_count'),
        'event_token':  event_token,
        'fb_id':  app_data.get('fb_id'),
        'gps_adid':  device_data.get('adid'),
        'gps_adid_attempt':  '1',
        'gps_adid_src':  'service',
        'hardware_name':  device_data.get('hardware'),
        'language':  device_data.get('locale').get('language'),
        'needs_response_details':  '1',
        'os_build':  device_data.get('build'),
        'os_name':  'android',
        'os_version':  device_data.get('os_version'),
        'package_name':  campaign_data.get('package_name'),
        'partner_params':  'partner_params',
        'screen_density':  get_screen_density(device_data),
        'screen_format':  get_screen_format(device_data),
        'screen_size':  'normal',
        'sent_at':  (datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'session_count':  app_data.get('session_count'),
        'session_length':  int(time.time())-app_data.get('session_started'),
        'subsession_count':  subsession(app_data),
        'time_spent':  time_spent(app_data),
        'tracking_enabled':  '1',
        'ui_mode':  '1',
    }
    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')


    if callback:
        data['callback_params'] = json.dumps(callback)
    if patner:
        data['partner_params'] = json.dumps(patner)


    headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'),'event')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}
#================================ Event End ================================

#================================ Adjust SdkInfo ================================
def adjust_sdk_info(app_data,device_data):
    url = 'https://app.adjust.com/sdk_info'
    httpmethod='post'
    pushtoken(app_data)
    headers={
        'Client-SDK':campaign_data.get('adjust').get('sdk'),
        'User-Agent':get_ua(device_data),
        'Accept-Encoding':'gzip',
    }
    params=None
    data = {
        'android_uuid':  app_data.get('android_uuid'),
        'app_token':  campaign_data.get('adjust').get('app_token'),
        'attribution_deeplink':  '1',
        'created_at':  (datetime.utcfromtimestamp(time.time()-random.randint(3,8)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'environment':  'production',
        'event_buffering_enabled':  '0',
        'gps_adid':  device_data.get('adid'),
        'gps_adid_attempt':  '1',
        'gps_adid_src':  'service',
        'needs_response_details':  '1',
        'push_token':  app_data.get('pushtoken'),
        'sent_at':  (datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'source':  'push',
        'tracking_enabled':  '1',
    }
    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}
#================================ SdkInfo End ================================
#================================ Firebase Start ================================
def firebase_installations( app_data, device_data ):
    method = 'post'
    url = 'https://firebaseinstallations.googleapis.com'+firebase_data.get('url')
    app_data['fid'] = util.get_fid()
    headers = {
        'Content-Type':'application/json',
        'Accept':'application/json',
        'Cache-Control':'no-cache',
        'X-Android-Package':campaign_data.get('package_name'),
        'x-firebase-client':firebase_data.get('x-firebase-client'),
        'X-Android-Cert':firebase_data.get('X-Android-Cert'),
        'x-goog-api-key':firebase_data.get('x-goog-api-key'),
        'User-Agent':get_ua(device_data),
        'Connection':'Keep-Alive',
        'Accept-Encoding':'gzip'
    }
    data ={
        'fid': app_data.get('fid'),
        'appId':firebase_data.get('data').get('appId') ,
        'authVersion': firebase_data.get('data').get('authVersion'),
        'sdkVersion': firebase_data.get('data').get('sdkVersion')
    }

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}

#================================ Firebase End ================================
#================================ Install Function ================================

def install(app_data, device_data):
    # print 'Please wait installing...'
    installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')
    if not app_data.get('sec'):
        timez=device_data.get('timezone')    
        sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
        if int(timez) < 0:
            sec = (-1) * sec
        app_data['sec'] = sec
    # user = util.register_user(country=device_data.get('locale').get('country'))
    # req = locationData.getLocation(device_data.get('locale').get('country'))
    if not app_data.get('android_uuid'):
        app_data['android_uuid']=str(uuid.uuid4())


    num = 5
    while(num > 0):
        req = firebase_installations(app_data, device_data)
        response = util.execute_request(**req)
        try:
            result = json.loads(response.get('data'))
            app_data['fid2'] = result.get('fid')
            break
        except:
            pass
        num -= 1
    if not app_data.get('fid'):
        if not app_data.get('fiddler_app_test'):
            raise Exception("Couldn't get fid for "+device_data.get('locale').get('country'))


    req = adjust_session(app_data, device_data)
    util.execute_request(**req)

    req = adjust_sdk_click( app_data, device_data,source='install_referrer')
    util.execute_request(**req)
    time.sleep(random.randint(1,5))
    # print 'Attribution'
    req = adjust_attribution(app_data, device_data,initiated_by='sdk')
    util.execute_request(**req)


    req = adjust_events(app_data,device_data,event_token='niswel')
    util.execute_request(**req)
    time.sleep(random.randint(1,5))


    req = adjust_events(app_data,device_data,event_token='kxthgf')
    util.execute_request(**req)
    time.sleep(random.randint(1,5))


    req = adjust_events(app_data,device_data,event_token='3dg2wl')
    util.execute_request(**req)
    time.sleep(random.randint(1,5))


    req = adjust_events(app_data,device_data,event_token='3dg2wl')
    util.execute_request(**req)
    time.sleep(random.randint(1,5))


    req = adjust_events(app_data,device_data,event_token='39zpow')
    util.execute_request(**req)
    time.sleep(random.randint(1,5))


    return {'status':True}

#================================ Install End ================================

#================================ Open Begin ================================

def open( app_data, device_data, day=1 ):
    if app_data.get('times'):
        req  = adjust_session( app_data, device_data )
        util.execute_request(**req)
    return {'status':True}

#================================ Open End ================================

#================================ Supportive Function ================================
def pushtoken(app_data):
    if not app_data.get('pushtoken'):
        if app_data.get('fid2'):
            app_data['pushtoken'] = app_data.get('fid2')+ ':APA91b' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_') for _ in range(134))
        else:
            app_data['pushtoken'] = util.get_fid()+ ':APA91b' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_') for _ in range(134))



def get_auth(created_at,activity_kind, app_secret,gps_adid , source =''):
    string = created_at+activity_kind+source+app_secret+gps_adid
    sign = hashlib.sha256(string).hexdigest()
    if source:
        return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid source app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)
    return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)



def time_spent(app_data):
    if not app_data.get('time_spent'):
        app_data['time_spent'] = str(0)
    else:
        app_data['time_spent'] = int(app_data.get('time_spent')) + (int(time.time()) - app_data.get('session_started'))
    return app_data.get('time_spent')


def subsession(app_data):
    possibility = [True]*30+[False]*70
    random.shuffle(possibility)
    if random.choice(possibility):
        if not app_data.get('subsession'):
            app_data['subsession']=1
        else:
            app_data['subsession']+=1
    return app_data.get('subsession')


def get_screen_density(device_data):
    dpi = int(device_data.get('dpi'))
    if dpi >= 320:
        return 'high'
    elif dpi >= 180:
        return 'medium'
    else:
        return 'low'


def get_screen_format(device_data):
    resolution = device_data.get('resolution')
    b = resolution.split('x')
    c = float(b[1])/float(b[0])
    if c >= 1.77:
        return 'long'
    else:
        return 'normal'


def get_retention(day):
    return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0


def get_ua(device_data):
    if int(device_data.get('sdk')) >=19:
        return 'Dalvik/2.1.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'
    else:
        return 'Dalvik/1.6.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'
#================================ !! End !! ================================
