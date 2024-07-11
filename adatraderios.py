#-*- coding: utf-8 -*-
# from __future__ import unicode_literals
# created by him@nshu
import sys
if int(sys.version_info.major) == 2:
    py_version = 2
    from urllib import quote
else:
    py_version = 3
    from urllib.parse import quote
from sdk import installtimenew, util
import time, random, json, string, urllib, uuid, hashlib
from spicipher import af_cipher,get_dlsdk_af_sig,get_cdn_token,get_gcd_sdk_af_sig,update_ios_cksm_v2,get_ios_skadsdk_sign,update_ios_cksm_v1,get_ios_skadsdkless_sign
from datetime import datetime,timedelta
false = False
true = True
null = None
campaign_data = {
   'package_name' : 'com.avatrade.mobile',
   'app_name' : 'ava',
   'bundle_name' : 'AvaTradeGO',
   'app_id' : '1247935193',
   'app_version_code' : '121.5',
   'app_version_name' : '95.5',
   'supported_os' : '15',
   'platformextension' : 'ios_native',
   'ref' : 'db7329eef4753e02f2f61ae54182f260365b4da62dc7cab86fc41cde012bd3f8;0;0;0;0;0',
    'appsflyer' : { 
      'key' : 'dG3LEntbALmVHLjGjXFqcL',
      'server_api_version' : '6.8',
      'buildnumber' : '6.8.1',
      'version' : 'v6.8',
      'spi_key' : '9bAqmpisBTY4zUYIrM/WFw9x70pAQbRWbgo0c1PMLh39C76/2EOw0wAkV+5PHQHY',
    #    'spi_key' : 'rs/eqwzDhTcmKnJZqBHovz/nu6RF7QLnnWC05qRoNnZqQfus1klLUEEfbw2JiOEW',#devkey
    },
   'supported_countries' : 'WW',
   'sdk' : 'ios',
    'app_size' : 48,
    'tracker' : ['appsflyer'],
    'data' : {'osVersion': '99.9 (Build 99999)', 'ram_size': '999', 'disk': '999/9999'},
    'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
    'retention' : {1: 75, 2: 72, 3: 70, 4: 68, 5: 67, 6: 65, 7: 62, 8: 60, 9: 55, 10: 51, 11: 48, 12: 45, 13: 44, 14: 41, 15: 39, 16: 37, 17: 35, 18: 35, 19: 34, 20: 33, 21: 32, 22: 31, 23: 30, 24: 29, 25: 29, 26: 28, 27: 27, 28: 26, 29: 25, 30: 25, 31: 24, 32: 23, 33: 23, 34: 22, 35: 22, 36: 21, 37: 20, 38: 19, 39: 19, 40: 18, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 14, 47: 13, 48: 13, 49: 12, 50: 11, 51: 11, 52: 10, 53: 9, 54: 9, 55: 8, 56: 7, 57: 6, 58: 5, 59: 4, 60: 3},
    }
Appsflyer_data = {"main_url": ".appsflyer.com", "Key": "dG3LEntbALmVHLjGjXFqcL", "id": "1247935193", "app_name": null, "cdn_version": "v1", "cdn_url": ".appsflyersdk.com", "cdn": true, "dlsdk": true, "dlsdk_url": ".appsflyer.com", "skadsdk": true, "skadsdk_url": ".appsflyer.com", "skadsdkless": true, "skadsdkless_url": ".appsflyer.com", "build_number": "6.8.1", "main_agent": "ava/121.5 CFNetwork/1335.0.3 Darwin/21.6.0", "bundle_id": "com.avatrade.mobile", "register": true, "attr": true, "dynamic-config-api": true, "dynamic-config-api_url": ".appsflyer.com"}
firebase_data = {"run": true, "X-Android-Cert": "AIzaSyCDDsyjgTEdesH9-87EsxguCUcz8pewDXQ", "data": {"installation": {"sdkVersion": "i:8.14.0"}}, "agent": "ava/121.5 CFNetwork/1335.0.3 Darwin/21.6.0", "url": "/v1/projects/avatradego-18319/installations/dHCo7wseRUkNkx0lvUahJ-/authTokens:generate"}
#=======================conversion===================================
def appsflyer_conversion(app_data, device_data):
    url = 'https://conversions.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version') +'/iosevent'
    httpmethod ='post'
    headers = {
        'Content-Type':'application/octet-stream',
        'Accept': '*/*',
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        'Accept-Language':device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        'Accept-Encoding':'gzip, deflate, br'
    }
    params = {
        'app_id': campaign_data.get('app_id'),
        'buildnumber': campaign_data.get('appsflyer').get('buildnumber')
    }
    # app_data['cdn_token']=get_cdn_token(campaign_data.get('package_name'),campaign_data.get('appsflyer').get('key'))
    if not app_data.get('counter'):
        app_data['counter'] = 1
    else:
        app_data['counter'] +=1
    if not app_data.get('iaecounter'):
        app_data['iaecounter'] =0
    if not app_data.get('timepassedsincelastlaunch'):
        timeSinceLastCall='-1'
        app_data['timepassedsincelastlaunch']=int(time.time())
    else:
        timeSinceLastCall=int(time.time())-app_data.get('timepassedsincelastlaunch')
        app_data['timepassedsincelastlaunch']=int(time.time())
    if not app_data.get('disk'):
        app_data['disk'] = "{available}/{total}".format(available =str(random.randint(8000, 16000)), total = str(random.randint(30497, 30497)))
    else:
        temp_disk = map(int, app_data.get('disk').split('/'))
        temp_disk[0] += random.randint(-150, 300)
        app_data['disk'] = "{available}/{total}".format(available = str(temp_disk[0]), total = str(temp_disk[1]))
    t1 = time.time()
    t_in1 = str(int(t1*1000))
    t_in2 = "%.3f"%t1+str(random.randint(000,999))
    f_g = random.randint(100,700)
    delay = random.randint(100,700)
    data = {
        'JBDevice':  False,
        'advertiserId':  app_data.get('idfa'),
        'advertiserIdEnabled':  False,
        'af_events_api':  '1',
        'af_timestamp':  t_in1,
        'asa_data':{
            'token':      app_data.get('asa_data'),
        },
        'att_status':  random.randint(0,3),
        'bundleIdentifier':  campaign_data.get('package_name'),
        'bundlename':  campaign_data.get('bundle_name'),
        'bundleversion':  campaign_data.get('app_version_code'),
        'cell':{
            'mcc':      device_data.get('mcc'),
            'mnc':      device_data.get('mnc'),
            'ra':      '',
        },
        'cksm_v1':  '32cf2ad94b9b11f8591b0c4f1a0d401a0c481b0d4e1b',
        'counter':  str(app_data.get('counter')),
        'currentCountrycode':  device_data.get('locale').get('country'),
        'currentLanguage':  "{en}-{IN}".format(en=device_data.get('locale').get('language'), IN = device_data.get('locale').get('country')),
        'date1':  app_data.get('date1'),
        'date1_2':  app_data.get('date1'),
        'date2':  app_data.get('firstLaunchDate'),
        'date3':  app_data.get('firstLaunchDate'),
        'dev_key':  campaign_data.get('appsflyer').get('key'),
        'deviceData':{
            'brightness':      str(round(random.uniform(0,1),6)),
            'cpu_64bits':      "true",
            'cpu_count':      "2",
            'cpu_speed':      "-1",
            'cpu_type':      device_data.get('cpu_type'),
            'device_model':      device_data.get('device_platform'),
            'dim':{
                'x_px':      int(device_data.get('resolution').split('x')[1]),
                'y_px':      int(device_data.get('resolution').split('x')[0]),
            },
            'osVersion':      "{os} (Build {build})".format(os = device_data.get('version'), build = device_data.get('build')),
            'ram_size':      device_data.get('ram'),
        },
        'disk':  app_data.get('disk'),
        'event':  'Launched',
        'eventName':  'Launched',
        'eventvalue':  '',
        'firstLaunchDate':  app_data.get('firstLaunchDate'),
        'iaecounter':  str(app_data.get('iaecounter')),
        'installReceiptData':  json.dumps({"data":{"receipt-data":str(app_data.get('apple_reciept'))}}),
        'ivc':  False,
        'localizedmodel':  'iPhone',
        'meta':{
            'att':{
                        'queued':  True ,
            },
            'ddl':{
                'from_fg':      f_g,
                'net':      [f_g+random.randint(10,20)],
                'status':      'NOT_FOUND',
                'timeout_value':      random.randint(1,4)*1000,
            },
            'first_launch':{
                'from_fg':      random.randint(400,500),
                'init_to_fg':      random.randint(900,1000),
                'net':      random.randint(500,600),
            },
            'rc':{
                'c_ver':      app_data.get('cdn_ver'),
                'cdn_token':      app_data.get('cdn_token'),
                'delay':      delay,
                'latency':      delay-random.randint(5,50),
                'res_code':      200,
                'sig':      'success',
            },
            'skad':{
        "s2s":  {'upcv': 0},
            },
        },
        'model':  'iPhone',
        'open_referrer':  '',
        'originalAppsflyerId':  app_data.get('uid'),
        'platform':  device_data.get('device_platform'),
        'platformextension':  campaign_data.get("platformextension"),
        'ref':  campaign_data.get('ref'),
        'reinstallCounter':  '0',
        'sc_o':  'fu',
        'serverApiVersion':  campaign_data.get('appsflyer').get('server_api_version'),
        'sessioncounter':  str(app_data.get('counter')),
        'shortbundleversion':  campaign_data.get('app_version_name'),
        'sk_rules':{
            'sk_exp':      app_data.get('sk_exp'),
            'sk_rules':      app_data.get('sk_rules'),
        },
        'systemname':  'iOS',
        'systemversion':  device_data.get('os_version'),
        'timepassedsincelastlaunch':  str(timeSinceLastCall),
        'timestamp':  t_in2,
        'uid':  app_data.get('uid'),
        'vendorId':  app_data.get('idfv'),
        'wifi':  False,
    }
    update_ios_cksm_v1(data,campaign_data.get('appsflyer').get('buildnumber'))
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':(af_cipher(campaign_data.get('appsflyer').get('spi_key') ,json.dumps(data, separators = (',',':')), device='ios'))}
#============================Attri====================================
def appsflyer_attr(app_data, device_data):
    url = 'https://attr.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/iosevent'
    httpmethod = 'post'
    headers = {
        'Content-Type': 'application/octet-stream',
        'Accept': '*/*',
        'User-Agent':  '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        'Accept-Language': device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country'.lower()),
        'Accept-Encoding': 'gzip, deflate, br'
    }
    t1 = time.time()
    t_in1 = str(int(t1*1000))
    t_in2 = "%.3f"%t1+str(random.randint(000,999))
    params = {
        'app_id':   campaign_data.get('app_id'),
        'buildnumber':  campaign_data.get('appsflyer').get('buildnumber')
    }
    if not app_data.get('timepassedsincelastlaunch'):
        timeSinceLastCall='-1'
        app_data['timepassedsincelastlaunch']=int(time.time())
    else:
        timeSinceLastCall=int(time.time())-app_data.get('timepassedsincelastlaunch')
        app_data['timepassedsincelastlaunch']=int(time.time())
    if not app_data.get('counter'):
        app_data['counter'] = 1
    else:
        app_data['counter'] +=1
    if not app_data.get('disk'):
        app_data['disk'] = "{available}/{total}".format(available =str(random.randint(8000, 16000)), total = str(random.randint(30497, 30497)))
    else:
        temp_disk = map(int, app_data.get('disk').split('/'))
        temp_disk[0] += random.randint(-150, 300)
        app_data['disk'] = "{available}/{total}".format(available = str(temp_disk[0]), total = str(temp_disk[1]))
    data = {
        'JBDevice':  False,
        'advertiserId':  app_data.get('idfa'),
        'advertiserIdEnabled':  False,
        'af_events_api':  '1',
        'af_timestamp':  t_in1,
        'att_status':  random.randint(0,3),
        'bundleIdentifier':  campaign_data.get('package_name'),
        'bundlename':  campaign_data.get('bundle_name'),
        'bundleversion':  campaign_data.get('app_version_code'),
        'cell':{
            'mcc':      device_data.get('mcc'),
            'mnc':      device_data.get('mnc'),
            'ra':      '',
        },
        'cksm_v1':  '32cf2ad94b9b11f8591b0c4f1a0d401a0c481b0d4e1b',
        'counter':  str(app_data.get('counter')),
        'currentCountrycode':  device_data.get('locale').get('country'),
        'currentLanguage':  "{en}-{IN}".format(en=device_data.get('locale').get('language'), IN = device_data.get('locale').get('country')),
        'date1':  app_data.get('date1'),
        'date1_2':  app_data.get('date1'),
        'date2':  app_data.get('firstLaunchDate'),
        'date3':  app_data.get('firstLaunchDate'),
        'dev_key':  campaign_data.get('appsflyer').get('key'),
        'deviceData':{
            'brightness':      str(round(random.uniform(0,1),6)),
            'cpu_64bits':      "true",
            'cpu_count':      "2",
            'cpu_speed':      "-1",
            'cpu_type':      device_data.get('cpu_type'),
            'device_model':      device_data.get('device_platform'),
            'dim':{
                'x_px':      int(device_data.get('resolution').split('x')[1]),
                'y_px':      int(device_data.get('resolution').split('x')[0]),
            },
            'osVersion':      "{os} (Build {build})".format(os = device_data.get('version'), build = device_data.get('build')),
            'ram_size':      device_data.get('ram'),
        },
        'disk':  app_data.get('disk'),
        'event':  'Launched',
        'eventName':  'Launched',
        'eventvalue':  '',
        'firstLaunchDate':  app_data.get('firstLaunchDate'),
        'iaecounter':  str(app_data.get('iaecounter')),
        'ivc':  False,
        'localizedmodel':  'iPhone',
        'meta':{
            'att':{
                        'queued':  True ,
            },
            'first_launch':{
                'from_fg':      random.randint(400,500),
                'init_to_fg':      random.randint(900,1000),
                'net':      random.randint(500,600),
            },
            'skad':{
        "s2s":  {'upcv': 0},
            },
        },
        'model':  'iPhone',
        'open_referrer':  '',
        'originalAppsflyerId':  app_data.get('uid'),
        'platform':  device_data.get('device_platform'),
        'platformextension':  campaign_data.get("platformextension"),
        'ref':  campaign_data.get('ref'),
        'reinstallCounter':  '0',
        'sc_o':  'fu',
        'serverApiVersion':  campaign_data.get('appsflyer').get('server_api_version'),
        'sessioncounter':  str(app_data.get('counter')),
        'shortbundleversion':  campaign_data.get('app_version_name'),
        'systemname':  'iOS',
        'systemversion':  device_data.get('os_version'),
        'timepassedsincelastlaunch':  str(timeSinceLastCall),
        'timestamp':  t_in2,
        'uid':  app_data.get('uid'),
        'vendorId':  app_data.get('idfv'),
        'wifi':  False,
    }
    update_ios_cksm_v1(data,campaign_data.get('appsflyer').get('buildnumber'))
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':(af_cipher(campaign_data.get('appsflyer').get('spi_key') ,json.dumps(data, separators = (',',':')), device='ios'))}
#=====================Launch call================================
def appsflyer_launch(app_data, device_data):
    url = 'https://launches.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/iosevent'
    httpmethod = 'post'
    headers = {
        'Content-Type': 'application/octet-stream',
        'Accept': '*/*',
        'User-Agent':  '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        'Accept-Language': device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country'.lower()),
        'Accept-Encoding': 'gzip, deflate, br'
        }
    params = {
        'app_id':   campaign_data.get('app_id'),
        'buildnumber':  campaign_data.get('appsflyer').get('buildnumber')
    }
    if not app_data.get('counter'):
        app_data['counter'] = 1
    else:
        app_data['counter'] +=1
    t1 = time.time()
    t_in1 = str(int(t1*1000))
    t_in2 = '%.3f'%t1+str(random.randint(000,999))
    if not app_data.get('timepassedsincelastlaunch'):
        timeSinceLastCall=-1
        app_data['timepassedsincelastlaunch']=int(time.time())
    else:
        timeSinceLastCall=int(time.time())-app_data.get('timepassedsincelastlaunch')
        app_data['timepassedsincelastlaunch']=int(time.time())
    prev_session_dur = timeSinceLastCall - random.randint(3,8)
    f_g = random.randint(100,700)
    delay = random.randint(100,700)
    data = {
        'JBDevice':  False,
        'advertiserId':  app_data.get('idfa'),
        'advertiserIdEnabled':  False,
        'af_events_api':  '1',
        'af_timestamp':  t_in1,
        'att_status':  random.randint(0,3),
        'bundleIdentifier':  campaign_data.get('package_name'),
        'bundlename':  campaign_data.get('bundle_name'),
        'bundleversion':  campaign_data.get('app_version_code'),
        'cell':{
            'mcc':      device_data.get('mcc'),
            'mnc':      device_data.get('mnc'),
            'ra':      '',
        },
        'cksm_v1':  '32cf2ad94b9b11f8591b0c4f1a0d401a0c481b0d4e1b',
        'counter':  str(app_data.get('counter')),
        'currentCountrycode':  device_data.get('locale').get('country'),
        'currentLanguage':  "{en}-{IN}".format(en=device_data.get('locale').get('language'), IN = device_data.get('locale').get('country')),
        'date1':  app_data.get('date1'),
        'date1_2':  app_data.get('date1'),
        'date2':  app_data.get('firstLaunchDate'),
        'date3':  app_data.get('firstLaunchDate'),
        'dev_key':  campaign_data.get('appsflyer').get('key'),
        'deviceData':{
            'brightness':      str(round(random.uniform(0,1),6)),
            'cpu_64bits':      "true",
            'cpu_count':      "2",
            'cpu_speed':      "-1",
            'cpu_type':      device_data.get('cpu_type'),
            'device_model':      device_data.get('device_platform'),
            'dim':{
                'x_px':      int(device_data.get('resolution').split('x')[1]),
                'y_px':      int(device_data.get('resolution').split('x')[0]),
            },
            'osVersion':      "{os} (Build {build})".format(os = device_data.get('version'), build = device_data.get('build')),
            'ram_size':      device_data.get('ram'),
        },
        'disk':  app_data.get('disk'),
        'event':  'Launched',
        'eventName':  'Launched',
        'eventvalue':  '',
        'firstLaunchDate':  app_data.get('firstLaunchDate'),
        'iaecounter':  str(app_data.get('iaecounter')),
        'ivc':  False,
        'localizedmodel':  'iPhone',
        'meta':{
            'att':{
                        'queued':  True ,
            },
            'first_launch':{
                'from_fg':      random.randint(400,500),
                'init_to_fg':      random.randint(900,1000),
                'net':      random.randint(500,600),
            },
            'skad':{
        "s2s":  {'upcv': 0},
            },
        },
        'model':  'iPhone',
        'open_referrer':  '',
        'originalAppsflyerId':  app_data.get('uid'),
        'platform':  device_data.get('device_platform'),
        'platformextension':  campaign_data.get("platformextension"),
        'ref':  campaign_data.get('ref'),
        'reinstallCounter':  '0',
        'sc_o':  'fu',
        'serverApiVersion':  campaign_data.get('appsflyer').get('server_api_version'),
        'sessioncounter':  str(app_data.get('counter')),
        'shortbundleversion':  campaign_data.get('app_version_name'),
        'systemname':  'iOS',
        'systemversion':  device_data.get('os_version'),
        'timepassedsincelastlaunch':  str(timeSinceLastCall),
        'timestamp':  t_in2,
        'uid':  app_data.get('uid'),
        'vendorId':  app_data.get('idfv'),
        'wifi':  False,
    }
    update_ios_cksm_v1(data,campaign_data.get('appsflyer').get('buildnumber'))
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':(af_cipher(campaign_data.get('appsflyer').get('spi_key') ,json.dumps(data, separators = (',',':')), device='ios'))}
#=================================Register=============================
def appsflyer_register(app_data, device_data):
    url = 'https://register.appsflyer.com/api/'+campaign_data.get('appsflyer').get('version')+'/iosevent'
    httpmethod = 'post'
    headers = {
    'Content-Type': 'application/octet-stream',
    'Accept': '*/*',
    'User-Agent':  '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
    'Accept-Language': device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country'.lower()),
    'Accept-Encoding': 'gzip, deflate, br'
    }
    params = {
    'app_id':   campaign_data.get('app_id'),
    'buildnumber':  campaign_data.get('appsflyer').get('buildnumber')
    }
    data = {
        'OriginalAppsFlyerId':  app_data.get('uid'),
        'advertiserId':  device_data.get('adid').upper(),
        'att_status':  '0',
        'bundlename':  campaign_data.get('bundle_name'),
        'bundleversion':  campaign_data.get('app_version_name'),
        'deviceData':{
            'brightness':      round(random.uniform(0,1),6),
            'cpu_64bits':      "True",
            'cpu_count':      "9",
            'cpu_speed':      "-1",
            'cpu_type':      device_data.get('cpu_type'),
            'device_model':      device_data.get('device_type'),
            'dim':{
                'x_px':      device_data.get('resolution').split('x')[1],
                'y_px':      device_data.get('resolution').split('x')[0],
            },
            'osVersion':      '{os} (Build {build})'.format(os = device_data.get('version'), build = device_data.get('build')),
            'ram_size':      device_data.get('ram'),
        },
        'devicetoken':  util.get_random_string('hex', 64),
        'devkey':  campaign_data.get('appsflyer').get('key'),
        'install_date':  app_data.get('date1'),
        'launch_counter':  '0',
        'reInstallCounter':  '0',
        'sdk_version':  campaign_data.get('appsflyer').get('buildnumber'),
        'shortbundleversion':  campaign_data.get('app_version_name'),
        'topic':  campaign_data.get('package_name'),
        'uid':  app_data.get('uid'),
        'useDevelopment':  False,
        'vendorId':  app_data.get('idfv'),
        'wifi':  False,
    }
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data': json.dumps(data, separators = (',',':'))}
#=================================Gcdsdk=============================
def appsflyer_gcdsdk(app_data, device_data):
    url = 'https://gcdsdk.appsflyer.com/install_data/v5.0/id' + campaign_data.get('app_id')
    httpmethod = 'get'
    headers = {
        'Accept': '*/*',
        "Accept-Language":"en-SG,en-GB;q=0.9,en;q=0.8",
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1])
    }
    params = {
        # 'devkey': campaign_data.get('appsflyer').get('key'),
        'device_id':app_data.get('uid')
    }
    af_request_epoch_ms = str(int(time.time()*1000))
    headers['af_request_epoch_ms'] = af_request_epoch_ms
    headers['af_sig'] = get_gcd_sdk_af_sig(package_name="id"+campaign_data.get('app_id'),af_key=campaign_data.get('appsflyer').get('key'),uid=app_data.get('uid'),af_request_epoch_ms=af_request_epoch_ms)
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':None}
# =======================appsflyer_sdadsdk==========================
def appsflyer_sdadsdk( app_data, device_data ):
    method = 'get'
    af_timestamp=str(int(time.time()*1000))
    currency=util.country_list.get(device_data.get('locale').get('country').upper()).get('currency')
    url = 'https://skadsdk.appsflyer.com/api/v1.0/rules'
    headers = {
        'Accept-Encoding': "gzip, deflate, br",
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        'Authorization':get_ios_skadsdk_sign(app_id='id'+campaign_data.get('app_id'),af_key=campaign_data.get('appsflyer').get('key'),uid=app_data.get('uid'),af_timestamp=af_timestamp,currency=currency),
        'Af-Timestamp':af_timestamp,
        "Accept-Language":"en-SG,en-GB;q=0.9,en;q=0.8"
    }
    params ={
        'app_id':'id'+campaign_data.get('app_id'),
        'currency':currency,
        'uid':app_data.get('uid')
    }
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': None}
#===========================dyanmic_config==========================
def dyanmic_config( app_data, device_data ):
    method = 'post'
    af_timestamp=str(int(time.time()*1000))
    currency=util.country_list.get(device_data.get('locale').get('country').upper()).get('currency')
    url = 'https://dynamic-config-api.appsflyer.com/api/dynamic-config/1'
    headers = {
        'Accept-Encoding': "gzip, deflate, br",
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        'signature':get_ios_skadsdk_sign(app_id='id'+campaign_data.get('app_id'),af_key=campaign_data.get('appsflyer').get('key'),uid=app_data.get('uid'),af_timestamp=af_timestamp,currency=currency),
        'Accept-Language':'en-SG',
        'Content-Type': 'application/json',
    }
    data={
        'current_date': int(time.time()),
        'appsflyer_id':app_data.get('uid'),
        'attribution': {
            'last_install_date': 0
        },
        'app_id': 'id'+campaign_data.get('app_id')
    }
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}
#===========================appsflyer_cdn==========================
def appsflyer_cdn( app_data, device_data ):
    method = 'get'
    app_data['cdn_token']=get_cdn_token('id'+campaign_data.get('app_id'),campaign_data.get('appsflyer').get('key'))
    url = 'https://cdn-settings.appsflyersdk.com/ios/v1/'+str(app_data.get('cdn_token'))+'/settings'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        'Accept-Encoding': 'gzip'
    }
    params ={}
    data = {}
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': data}
# ===========================appsflyer_dlsdk=========================
def appsflyer_dlsdk(app_data,device_data):
    url = "https://dlsdk.appsflyer.com/v1.0/ios/id"+campaign_data.get('app_id')
    method = "post"
    headers = {
        "Content-Type":"application/json",
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1]),
        "Accept-Encoding":"gzip",
    }
    params = {
        'af_sig':'b4b49212f1609707f73589ba0caab5c9b95d5823df2f81c021fd09a542ae94e1',
        'sdk_version': campaign_data.get('appsflyer').get('version').replace('v','')
    }
    data_dict = {
        'idfa': {
            'value':app_data.get('idfa'),
            "type": "unhashed"
        },
        'os':device_data.get('os_version'),
        "request_count": 1,
        "lang": "",
        'idfv': {
            'value':app_data.get('idfv'),
            "type": "unhashed"
        },
        'request_id': app_data.get('uid'),
        'att_status': 3,
        'is_first': True,
        'timestamp': app_data.get('dlsdk_timestamp'),
        "type": "iPhone"
    }
    params['af_sig'] = get_dlsdk_af_sig(package_name='id'+campaign_data.get('app_id'),af_key=campaign_data.get('appsflyer').get('key'),data_dict=data_dict)
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data':json.dumps(data_dict)}
# ===========================firebaseinstallations=========================
def firebaseinstallations(app_data, device_data):
    method = "post"
    url = 'https://firebaseinstallations.googleapis.com/v1/projects/avatradego-18319/installations/'
    headers = {
        'Content-Type': 'application/json',
        'X-firebase-client': firebase_data.get('x-firebase-client'),
        'X-firebase-client-log-type': '3',
        'Accept': '*/*',
        'X-Goog-Api-Key': firebase_data.get('X-Android-Cert'),
        'Accept-Encoding': 'en-us',
        'X-Ios-Bundle-Identifier': campaign_data.get('package_name'),
        'Accept-Language': device_data.get('locale').get('language')+'-'+device_data.get('locale').get('country').lower(),
        'User-Agent': '{0}/{1} CFNetwork/{2} Darwin/{3}'.format(campaign_data.get('app_name'), campaign_data.get('app_version_code'), device_data.get('cfnetwork').split('_')[0], device_data.get('cfnetwork').split('_')[1])
    }
    data = {
        "fid": util.get_fid(),
        'appId': "1:1071399268328:ios:feec32e7a2a84084147e5d",
        'authVersion':"FIS_v2",
        'sdkVersion': "i:8.14.0"
    }

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}


def pushwoosh(app_data, device_data):
    method = "post"
    t1=time.time()
  
    url = "https://avatrade.pushwoosh.com/json/1.3/postEvent"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "ava/121.5 CFNetwork/1335.0.3 Darwin/21.6.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",

    }
    data = {
            "request": {
                "userId": "91EE56B9-827D-4C4A-959D-77860C6D2C6A",
                "hwid": "91EE56B9-827D-4C4A-959D-77860C6D2C6A",
                "timestampUTC": int(time.time()),
                "event": "PW_ScreenOpen",
                "timestampCurrent": int(time.time()),
                "v": "6.3.4",
                "attributes": {
                    "device_type": "1",
                    "screen_name": "AVATradeFramework.OnboardingViewController",
                    "application_version": "95.5"
                },
                "device_type": 1,
                "application": "53611-D0416"
            }
        }

    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}

def install(app_data, device_data):
    # t1 = time.time()
    # t_in1 = str(int(t1*1000))
    # t_in2 = '%.3f'%t1+str(random.randint(000,999))
    # print(t1)
    # print(t_in1)
    # print(t_in2)
    # exit()
    # util.check_ip(app_data)
    if not app_data.get('times'):
        # print "Please wait installing...""
        app_data['clk'] = (int(time.time()))
        app_data['install_begin_ts'] = (int(time.time()))
        installtimenew.main(app_data, device_data, app_size=campaign_data.get('app_size'), os='ios')
        app_data['installDate'] = datetime.utcfromtimestamp(app_data.get('times').get('download_end_time')).strftime('%Y-%m-%d_%H%M%S') + '+0000'
        tz = device_data.get('timezone')
        hours = int(tz[1:3])
        minutes = int(tz[3:5])
        first_launch = time.time()
        alpha_numeric_elements = '1234567890'
        uid_last = ''.join(random.choice(alpha_numeric_elements) for i in range(7))
        app_data['uid'] = str(int(time.time()*1000)) +'-'+ str(uid_last)
        if tz[0] =='+':
            app_data['date1'] = (datetime.utcfromtimestamp(app_data.get('times').get('download_end_time'))+timedelta(hours=hours, minutes=minutes)).strftime('%Y-%m-%d_%H%M%S') + tz
            app_data['firstLaunchDate'] = (datetime.utcfromtimestamp(first_launch )+timedelta(hours=hours, minutes=minutes)).strftime('%Y-%m-%d_%H%M%S') + tz
        else:
            app_data['firstLaunchDate'] = (datetime.utcfromtimestamp(first_launch)-timedelta(hours=hours, minutes=minutes)).strftime('%Y-%m-%d_%H%M%S') + tz
            app_data['date1'] = (datetime.utcfromtimestamp(app_data.get('times').get('download_end_time'))-timedelta(hours=hours, minutes=minutes)).strftime('%Y-%m-%d_%H%M%S') + tz
        app_data['dlsdk_timestamp'] = datetime.utcfromtimestamp(int(first_launch)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        # app_data['sk_exp']=first_launch + random.randint(86400, 86410)
        token(app_data)
        apple_receipt(app_data)
        token_generate(app_data)

    if not app_data.get('idfa'):
        app_data['idfa'] = device_data.get('adid').upper()
    if not app_data.get('last_boot_time'):
        app_data['last_boot_time'] = int(time.time()*1000)
    if not app_data.get('idfv'):
        app_data['idfv'] = str(uuid.uuid4()).upper()
    if not app_data.get('ios_uuid'):
        app_data['ios_uuid'] = str(uuid.uuid4())
    if not app_data.get('fb_anon_id'):
        app_data['fb_anon_id'] = 'XZ'+str(uuid.uuid4()).upper()
    if not app_data.get('appUID'):
        app_data['appUID'] = str(uuid.uuid4()).upper()
    if not app_data.get('userId'):
        app_data['userId'] = str(random.randint(64368104,69999999))

    if Appsflyer_data.get('cdn'):
        req = appsflyer_cdn( app_data, device_data )
        res = util.execute_request(**req)
        try:
            tem = json.loads(res.get('data'))
            app_data['cdn_ver']  = tem.get('ver')
        except:
            pass

    if firebase_data.get('run'):
        num = 5
        while(num > 0):
            req = firebaseinstallations(app_data, device_data)
            response = util.execute_request(**req)
            try:
                result = json.loads(response.get('data'))
                app_data['fid'] = result.get('fid')
                app_data['X-subtype'] = result.get('name').split('/')[1]
                break
            except:
                pass
            num -= 1
    if not app_data.get('fid'):
        if not app_data.get('fiddler_app_test'):
            raise Exception("Couldn't get fid for "+device_data.get('locale').get('country'))

    if Appsflyer_data.get('skadsdk'):
        req = appsflyer_sdadsdk(app_data, device_data)
        res = util.execute_request(**req)
        try:
            tem = json.loads(res.get('data'))
            # print(tem)
            app_data['sk_exp'] = time.time()
            app_data['sk_rules'] = tem.get('sk_rules')
        except:
            app_data['sk_exp'] = time.time()
            app_data['sk_rules'] = {"wi":24,"ex":1.0,"di":1}

    if Appsflyer_data.get('dlsdk'):
        req = appsflyer_dlsdk(app_data,device_data)
        util.execute_request(**req)

    req = appsflyer_conversion(app_data, device_data)
    util.execute_request(**req)

    if Appsflyer_data.get('attr'):
        req = appsflyer_attr(app_data, device_data)
        util.execute_request(**req)

    if Appsflyer_data.get('register'):
        req = appsflyer_register(app_data, device_data)
        util.execute_request(**req)

    # print '_______gcdsdk'
    req = appsflyer_gcdsdk(app_data, device_data)
    util.execute_request(**req)

    req = appsflyer_launch(app_data, device_data)
    util.execute_request(**req)
    req = pushwoosh(app_data, device_data)
    util.execute_request(**req)

    return {'status':True}

# ================== Open Begins ======================
def open( app_data, device_data, day=1 ):
    if app_data.get('times'):
        # print 'launch'
        req  = appsflyer_launch( app_data, device_data )
        util.execute_request(**req)
    return {'status':True}

def def_sec(app_data,device_data):  
    if not app_data.get('sec'):
        timez = device_data.get('timezone')
        sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
        if int(timez) < 0:
            sec = (-1) * sec
        app_data['sec'] = sec
        return app_data.get('sec')

def apple_receipt(app_data):
    if not app_data.get('apple_reciept'):
        app_data['apple_reciept'] = 'MIIS'+''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_/+' ) for _ in range(random.randint(6000,7000)))+'=='
        return app_data.get('apple_reciept')

def ios_device_data( app_data, device):
    ios_device_data = {
        'iPad mini 2':'16777228',
        'iPad mini Wi-Fi':'12',
        'iPad mini Wi-Fi + Cellular':'12',
        'iPad 4 Wi-Fi':'16777228',
        'iPad 4 Wi-Fi + Cellular':'16777228',
        'iPhone 7 Plus':'16777228',
        'iPhone 7':'16777228',
        'iPhone SE':'16777228',
        'iPhone 6s Plus':'16777228',
        'iPhone 6s':'16777228',
        'iPhone 6 Plus':'16777228',
        'iPhone 6':'16777228',
        'iPhone 5s':'16777228',
        'iPhone 5c':'12',
        'iPhone 5 CDMA':'12',
        'iPhone 5':'12',
        'iPhone 4s':'12',
        'iPhone 4 CDMA':'12',
        'iPhone 4':'12',
        'iPad Air':'16777228',
        'iPad mini 3':'16777228',
        'iPad Air 2':'16777228',
        'iPad mini 4':'16777228'
    }

    app_data['device_cpu_type'] = ios_device_data.get( device )

    return app_data.get('device_cpu_type')

def token(app_data):
    alpha_numeric_elements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789=/+'
    app_data['asa_data']=''.join(random.choice(alpha_numeric_elements) for i in range(560))

def token_generate(app_data):
    alpha_numeric_elements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/+'
    app_data['receiptdata']=''.join(random.choice(alpha_numeric_elements) for i in range(6380))
