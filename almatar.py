#-*- coding: utf-8 -*-
# created by him@nshu/Nihal
import sys,base64
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime,timedelta
from sdk import installtimenew, util, NameLists
from sdk import NameLists
from hashlib import sha1
import time, random, json, string, urllib, uuid, hashlib
from spicipher import af_cipher
from requests import Request
from collections import OrderedDict


campaign_data = {
'app_name'         : 'almatar Hotel & Flight Booking',
'package_name'     : 'com.almatar',
'app_version_name' : '2.14.26', #2.13.26 #2.13.36 #2.13.41 #2.13.45 #2.13.46 #2.14.11
'app_version_code' : '167', #99 #130 #135 #139 #140 #152
'supported_countries' : 'WW',
'supported_os' : '8',
'tracker' : ['adjust'],
# 'link' : 'http://offerrobo.g2prof.net/click?offer_id=62f21c04d06424466b7ed7bb&aff_id=62&adv_id=62a1d0f8e3d0aa0e743b7011&aff_sub1={aff_click_id}&aff_sub2={gaid}&aff_sub3={idfa}&aff_sub6={app_name}&source={source}',
'adjust' : {'app_token': '1hxr2nrmjajk', 'sdk': 'android4.28.7'},
'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
'retention' : {1: 85, 2: 82, 3: 78, 4: 75, 5: 70, 6: 66, 7: 62, 8: 58, 9: 55, 10: 50, 11: 48, 12: 45, 13: 40, 14: 39, 15: 38, 16: 37, 17: 35, 18: 35, 19: 34, 20: 33, 21: 32, 22: 31, 23: 30, 24: 29, 25: 29, 26: 28, 27: 27, 28: 26, 29: 25, 30: 25, 31: 24, 32: 23, 33: 23, 34: 22, 35: 22, 36: 21, 37: 20, 38: 19, 39: 19, 40: 18, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 14, 47: 13, 48: 13, 49: 12, 50: 11, 51: 11, 52: 10, 53: 9, 54: 9, 55: 8, 56: 7, 57: 6, 58: 5, 59: 4, 60: 3},
'app_size' :13,
    }
adjust_data = {"event_name": ["l3eknk", "3juby2", "jppvja", "40faqo","30ls2a","3juby2"], "initiated_by": "backend", "url": "app.adjust.com", "partner": {"l3eknk": "{\"search_query\":\"Cairo, Egypt\",\"check_in_date\":\"07\\/19\\/2022\",\"check_out_date\":\"07\\/20\\/2022\",\"rooms_count\":\"1\"}", "jppvja": "{\"id\":\"1175870\",\"link\":\"https:\\/\\/almatar.com\\/en\\/hotels\\/rooms\\/giza-3-pyramids-view-inn-1175870\",\"title\":\"3 Pyramids View Inn\",\"image_link\":\"https:\\/\\/az712897.vo.msecnd.net\\/images\\/full\\/com.almtaar.model.accommodation.Image@f45ade4\",\"price\":\"93.08\",\"description\":\"Located in Cairo 3 Pyramids View Inn features free WiFi. Around 800 metres from Cheops Pyramid the property is also close to Chefren pyramid. The accommodation offers free shuttle service a 24-hour front desk and buying tickets for guests.Selected rooms include a kitchen with an oven a microwave and a toaster.A continental breakfast is available each morning at the inn.3 Pyramids View Inn offers a terrace. Hiking is among the activities that guests can enjoy near the accommodation.Mikerinus pyramid is 1.5 km from 3 Pyramids View Inn while Viewpoint and Camel rides is 2.2 km away. The nearest airport is Cairo International Airport 29 km from the property.\",\"categoryid1\":\"Giza, 7 Abou Al Hool Al Seiahi Al Haram\",\"star\":\"3\",\"adults_count\":\"1\",\"children_count\":\"0\",\"reviews\":\"5\",\"rooms_count\":\"1\",\"check_in_date\":\"07\\/20\\/2022\",\"check_out_date\":\"07\\/19\\/2022\",\"number_of_nights\":\"1\"}", "3juby2": "{\"search_query\":\"Cairo, Egypt\",\"check_in_date\":\"07\\/19\\/2022\",\"check_out_date\":\"07\\/20\\/2022\",\"rooms_count\":\"1\"}", "40faqo": "{\"currency\":\"SAR\",\"check_in_date\":\"19 July 2022\",\"check_out_date\":\"20 July 2022\",\"price\":\"93.08\",\"id\":\"1175870\",\"hotel_name\":\"3 Pyramids View Inn\",\"hotel_rate\":\"3.0\",\"room_class\":\"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\\n\",\"rooms_count\":\"1\"}","30ls2a":{"from_location":"AUH","to_location":"DXB","departure_date":"2022-07-08","adults_count":"1","children_count":"0","infants_count":"0"}}, "call_back": {"l3eknk": {"check_in_date": "07/19/2022", "search_query": "Cairo, Egypt", "check_out_date": "07/20/2022", "rooms_count": "1"}, "jppvja": {"reviews": "5", "star": "3", "description": "Located in Cairo 3 Pyramids View Inn features free WiFi. Around 800 metres from Cheops Pyramid the property is also close to Chefren pyramid. The accommodation offers free shuttle service a 24-hour front desk and buying tickets for guests.Selected rooms include a kitchen with an oven a microwave and a toaster.A continental breakfast is available each morning at the inn.3 Pyramids View Inn offers a terrace. Hiking is among the activities that guests can enjoy near the accommodation.Mikerinus pyramid is 1.5 km from 3 Pyramids View Inn while Viewpoint and Camel rides is 2.2 km away. The nearest airport is Cairo International Airport 29 km from the property.", "check_in_date": "07/20/2022", "title": "3 Pyramids View Inn", "price": "93.08", "children_count": "0", "adults_count": "1", "image_link": "https://az712897.vo.msecnd.net/images/full/com.almtaar.model.accommodation.Image@f45ade4", "number_of_nights": "1", "check_out_date": "07/19/2022", "link": "https://almatar.com/en/hotels/rooms/giza-3-pyramids-view-inn-1175870", "rooms_count": "1", "id": "1175870", "categoryid1": "Giza, 7 Abou Al Hool Al Seiahi Al Haram"}, "3juby2": {"check_in_date": "07/19/2022", "search_query": "Cairo, Egypt", "check_out_date": "07/20/2022", "rooms_count": "1"}, "40faqo": {"price": "93.08", "room_class": "Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\n", "hotel_rate": "3.0", "check_in_date": "19 July 2022", "currency": "SAR", "check_out_date": "20 July 2022", "id": "1175870", "hotel_name": "3 Pyramids View Inn", "rooms_count": "1"},"30ls2a":{"from_location":"AUH","to_location":"DXB","departure_date":"2022-07-08","adults_count":"1","children_count":"0","infants_count":"0"}}}

session_data = {"event_buffering_enabled": "0", "updated_at": "2022-07-08T12:23:24.801Z+0530", "needs_response_details": "1", "os_name": "android", "device_type": "phone", "device_manufacturer": "Xiaomi", "tracking_enabled": "1", "connectivity_type": "1", "package_name": "com.almatar", "installed_at": "2022-07-08T12:23:24.801Z+0530", "environment": "production", "os_version": "9", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "display_width": "1080", "app_version": "2.12.13", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "screen_size": "normal", "gps_adid_attempt": "1", "hardware_name": "PKQ1.181203.001", "gps_adid_src": "service", "screen_format": "long", "display_height": "2130", "app_token": "1hxr2nrmjajk", "sent_at": "2022-07-08T12:25:47.548Z+0530", "attribution_deeplink": "1", "screen_density": "high", "language": "ar", "created_at": "2022-07-08T12:25:47.297Z+0530", "session_count": "1", "device_name": "Redmi Note 7 Pro", "cpu_type": "arm64-v8a", "ui_mode": "1", "network_type": "0", "api_level": "28", "os_build": "PKQ1.181203.001"}

sdk_click_data = {"event_buffering_enabled": "0", "google_play_instant": "0", "updated_at": "2022-07-08T12:23:24.801Z+0530", "needs_response_details": "1", "time_spent": "0", "os_name": "android", "device_type": "phone", "device_manufacturer": "Xiaomi", "tracking_enabled": "1", "connectivity_type": "1", "package_name": "com.almatar", "click_time": "2022-07-08T12:22:40.000Z+0530", "os_version": "9", "installed_at": "2022-07-08T12:23:24.801Z+0530", "environment": "production", "source": "install_referrer", "install_begin_time": "2022-07-08T12:22:43.000Z+0530", "session_length": "0", "install_version": "2.12.13", "display_width": "1080", "app_version": "2.12.13", "subsession_count": "1", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "referrer_api": "google", "screen_size": "normal", "gps_adid_attempt": "1", "hardware_name": "PKQ1.181203.001", "gps_adid_src": "service", "screen_format": "long", "display_height": "2130", "app_token": "1hxr2nrmjajk", "sent_at": "2022-07-08T12:25:47.916Z+0530", "attribution_deeplink": "1", "screen_density": "high", "language": "ar", "referrer": "utm_source=(not%20set)&utm_medium=(not%20set)", "created_at": "2022-07-08T12:25:47.737Z+0530", "session_count": "1", "device_name": "Redmi Note 7 Pro", "click_time_server": "2022-07-08T12:22:37.000Z+0530", "cpu_type": "arm64-v8a", "ui_mode": "1", "install_begin_time_server": "2022-07-08T12:22:40.000Z+0530", "network_type": "0", "api_level": "28", "os_build": "PKQ1.181203.001"}

atribution_data = {"attribution_deeplink": "1", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "tracking_enabled": "1", "package_name": "com.almatar", "event_buffering_enabled": "0", "initiated_by": "backend", "created_at": "2022-07-08T12:26:02.649Z+0530", "gps_adid_attempt": "1", "needs_response_details": "1", "device_name": "Redmi Note 7 Pro", "environment": "production", "os_version": "9", "os_name": "android", "gps_adid_src": "service", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "device_type": "phone", "ui_mode": "1", "app_token": "1hxr2nrmjajk", "app_version": "2.12.13", "api_level": "28", "sent_at": "2022-07-08T12:26:02.657Z+0530"}

event_data = {"event_buffering_enabled": "0", "event_token": "40faqo", "needs_response_details": "1", "time_spent": "246", "callback_params": "{\"currency\":\"SAR\",\"check_in_date\":\"19 July 2022\",\"check_out_date\":\"20 July 2022\",\"price\":\"93.08\",\"id\":\"1175870\",\"hotel_name\":\"3 Pyramids View Inn\",\"hotel_rate\":\"3.0\",\"room_class\":\"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\\n\",\"rooms_count\":\"1\"}", "os_name": "android", "device_type": "phone", "device_manufacturer": "Xiaomi", "tracking_enabled": "1", "connectivity_type": "1", "package_name": "com.almatar", "environment": "production", "os_version": "9", "session_length": "263", "app_token": "1hxr2nrmjajk", "app_version": "2.12.13", "subsession_count": "2", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "partner_params": "{\"currency\":\"SAR\",\"check_in_date\":\"19 July 2022\",\"check_out_date\":\"20 July 2022\",\"price\":\"93.08\",\"id\":\"1175870\",\"hotel_name\":\"3 Pyramids View Inn\",\"hotel_rate\":\"3.0\",\"room_class\":\"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\\n\",\"rooms_count\":\"1\"}", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "screen_size": "normal", "gps_adid_attempt": "1", "hardware_name": "PKQ1.181203.001", "gps_adid_src": "service", "screen_format": "long", "display_height": "2130", "display_width": "1080", "sent_at": "2022-07-08T12:30:10.594Z+0530", "attribution_deeplink": "1", "screen_density": "high", "language": "ar", "event_count": "4", "created_at": "2022-07-08T12:30:10.300Z+0530", "session_count": "1", "device_name": "Redmi Note 7 Pro", "cpu_type": "arm64-v8a", "ui_mode": "1", "network_type": "0", "api_level": "28", "os_build": "PKQ1.181203.001"}




def install(app_data, device_data):
    # print "Please wait installing..."
    if not app_data.get('times'):
        installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')

    if not app_data.get('sec'):
        timez=device_data.get('timezone')    
        sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
        if int(timez) < 0:
            sec = (-1) * sec
        app_data['sec'] = sec



    if not app_data.get('android_uuid'):
        app_data['android_uuid']=str(uuid.uuid4())

    # if not app_data.get('fb_id'):
    #     app_data['fb_id']=str(uuid.uuid4())


    req = firbaseinstall(app_data,device_data)
    util.execute_request(**req)
    # time.sleep(random.randint(1,5))
    # print 'Session'
    req = adjust_session(app_data, device_data)
    util.execute_request(**req)
    time.sleep(random.randint(1,5))

    # print 'Sdk_click'
    req = adjust_sdk_click( app_data, device_data)
    util.execute_request(**req)
    time.sleep(random.randint(1,5))



    if adjust_data.get('sdk_info'):
        req = adjust_sdk_info(app_data,device_data)
        util.execute_request(**req)



    # print 'Attribution'
    req = adjust_attribution(app_data, device_data)
    util.execute_request(**req)

    #-----------date--------------------------
    opt=["Hotel","Flight","Hotel"]
    option=random.choice(opt)
    possibility = [True]*30 + [False]*70
    random.shuffle(possibility)
    #####################################
    #       Dates
    #####################################
    today=datetime.now()
    date=today+timedelta(1)
    check_in_date=date.strftime('%m/%d/%Y')
    date1=date+timedelta(1)
    check_out_date=date1.strftime('%m/%d/%Y')

    ########################################

    poss =[True]*30+[False]*70
    random.shuffle(poss)
    if random.choice(poss):
        c={'registration_method':'Google'}
        req= adjust_events( app_data, device_data,event_token='prniaw',callback=c,patner=c)
        util.execute_request(**req)
        app_data['registartion'] =True
    # time.sleep(random.randint(1,5))

    if random.choice(possibility) and option=="Hotel":
        req= adjust_events(app_data, device_data,event_token='3juby2')
        util.execute_request(**req)
        time.sleep(random.randint(1,5))
# {"search_query":"Dubai, United Arab Emirates","check_in_date":"11\/22\/2022","check_out_date":"11\/23\/2022","rooms_count":"1"}
        c={"check_in_date":check_in_date ,"search_query": "Cairo, Egypt","check_out_date": check_out_date,"rooms_count": "1"}
        req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
        util.execute_request(**req)
        time.sleep(random.randint(1,5))


        req = adjust_events(app_data,device_data,event_token='3juby2')
        util.execute_request(**req)
        time.sleep(random.randint(1,5))

        c={"reviews": "5", "star": "3", "description": "Located in Cairo 3 Pyramids View Inn features free WiFi. Around 800 metres from Cheops Pyramid the property is also close to Chefren pyramid. The accommodation offers free shuttle service a 24-hour front desk and buying tickets for guests.Selected rooms include a kitchen with an oven a microwave and a toaster.A continental breakfast is available each morning at the inn.3 Pyramids View Inn offers a terrace. Hiking is among the activities that guests can enjoy near the accommodation.Mikerinus pyramid is 1.5 km from 3 Pyramids View Inn while Viewpoint and Camel rides is 2.2 km away. The nearest airport is Cairo International Airport 29 km from the property.", "check_in_date": check_in_date, "title": "3 Pyramids View Inn", "price": "93.08", "children_count": "0", "adults_count": "1", "image_link": "https://az712897.vo.msecnd.net/images/full/com.almtaar.model.accommodation.Image@f45ade4", "number_of_nights": "1", "check_out_date": check_out_date, "link": "https://almatar.com/en/hotels/rooms/giza-3-pyramids-view-inn-1175870", "rooms_count": "1", "id": "1175870", "categoryid1": "Giza, 7 Abou Al Hool Al Seiahi Al Haram"}

        req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
        util.execute_request(**req)
        time.sleep(random.randint(1,5))

        check_in=date.strftime('%d %B %Y')
        check_out=date1.strftime('%d %B %Y')

        c={"price": "93.08", "room_class": "Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\n", "hotel_rate": "3.0", "check_in_date": check_in, "currency": "SAR", "check_out_date": check_out, "id": "1175870", "hotel_name": "3 Pyramids View Inn", "rooms_count": "1"}
        req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
        util.execute_request(**req)
        time.sleep(random.randint(1,5))

    if random.choice(possibility) and option=="Flight":
        departure_date=date.strftime('%Y-%m-%d')

        c={"from_location":"AUH","to_location":"DXB","departure_date":departure_date,"adults_count":"1","children_count":"0","infants_count":"0"}
        req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
        util.execute_request(**req)
        time.sleep(random.randint(1,5))

    return {'status':True}
#============================================================================================================================
def open(app_data, device_data, day =1):
    if app_data.get('times'):
        # print 'Session'
        req = adjust_session(app_data, device_data)
        util.execute_request(**req)

        if random.randint(1,10)>8:
            req= adjust_events(app_data, device_data,event_token='ore26o')  #Open from push notification
            util.execute_request(**req)
            time.sleep(random.randint(1,5))

        if not app_data.get('registartion') and day <7:
            poss =[True]*5+[False]*95
            random.shuffle(poss)
            if random.choice(poss):
                c={'registration_method':'Google'}
                req= adjust_events( app_data, device_data,event_token='prniaw',callback=c,patner=c)
                util.execute_request(**req)
                app_data['registartion'] =True


        possibility = [True]*10 + [False]*90
        random.shuffle(possibility)
        if random.choice(possibility):
            temp=random.randint(1,3)
            opt=["Hotel","Flight","Hotel"]
            option=random.choice(opt)
            # print(temp,option)

            today=datetime.now()
            date=today+timedelta(1)
            check_in_date=date.strftime('%m/%d/%Y')
            date1=date+timedelta(1)
            check_out_date=date1.strftime('%m/%d/%Y')

            if temp==1 and option=='Hotel':

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                c={"search_query":"Dubai,United Arab Emirates","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"}
                req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                c={"id":"15026","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/dubai-arabian-ranches-golf-club-15026","title":"Arabian Ranches Golf Club","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/com.almtaar.model.accommodation.Image@cd5748e","price":"331.48","description":"With a stay at Arabian Ranches Golf Club in Arabian Ranches, you'll be close to Arabian Ranches Golf Club and Dubai Autodrome","categoryid1":"Dubai, Arabian Ranches Emirates Road Po Box 367","star":"2","adults_count":"1","children_count":"0","reviews":"5","rooms_count":"1","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"1"}

                req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))#view hotel 

                check_in=date.strftime('%d %B %Y')
                check_out=date1.strftime('%d %B %Y')
                c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"331.48","id":"15026","hotel_name":"Arabian Ranches Golf Club","hotel_rate":"2.0","room_class":"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Deluxe room, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free self parking, Free WiFi])}, description=, images=[], roomKey=315844154))\n","rooms_count":"1"}
                
                req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5)) #for enter you persnal details
                app_data['bookHotel']=True

            if temp==2 and option=='Hotel':
                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                c={"search_query":"Riyadh, Saudi Arabia","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"}
                
                req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                c={"id":"51580","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/riyadh-the-ritz-carlton-riyadh-51580","title":"The Ritz Carlton Riyadh","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/com.almtaar.model.accommodation.Image@2da80ec","price":"1989.15","description":"The Ritz Carlton Riyadh is a 5 star hotel located within the Diplomatic Quarter in the city of Riyadh. Guest rooms are equipped with 42-inch LCD TV, Blue Ray and DVD players, minibar and wireless internet access. The hotel has a choice of restaurants that serve local and international dishes and two lounge spaces that offer a selection of assorted snacks and beverages. Leisure amenities include an indoor heated pool, fitness center and a male-only spa. Attractions in the area include King Abdul Aziz Conference Centre, King Saud University and the Al Faisaliyah Tower. King Khaled International Airport is approximately 47 km from the hotel.","categoryid1":"Riyadh, Al Hada Area Mekkah Road","star":"5","adults_count":"1","children_count":"0","reviews":"4.5","rooms_count":"1","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"1"}

                req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                check_in=date.strftime('%d %B %Y')
                check_out=date1.strftime('%d %B %Y')
                c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"1989.15","id":"51580","hotel_name":"The Ritz Carlton Riyadh","hotel_rate":"5.0","room_class":"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Standard room, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={bedroom=Amenity(name=Bedroom, values=[Air conditioning, Turndown service, Free cribs\/infant beds, Rollaway\/extra beds (surcharge)]), bathroom=Amenity(name=Bathroom, values=[Slippers, Shower\/tub combination, Private bathroom, Bathrobes, Towels provided]), food_drink=Amenity(name=Food & drink, values=[Free bottled water, Coffee\/tea maker]), entertainment=Amenity(name=Entertainment, values=[Premium TV channels, Satellite TV service, LCD TV, Local maps, Guidebooks or recommendations]), more=Amenity(name=More, values=[Free newspaper, Wheelchair accessible, Blackout drapes\/curtains, Connecting\/adjoining rooms available, Shared accommodation, Television, Smoking, Height-adjustable showerhead, Grab bar - near toilet, Minibar, Wardrobe or closet, Daily housekeeping, Free WiFi, In-room playpen, Restaurant dining guide, Bedsheets provided, Lowered electrical outlets in bathroom, Mini-fridge, Lowered peephole\/view port in door, Accessible bathtub, Visual fire alarm, Lever door handles, DVD player, Free toiletries, Hair dryer, Iron\/ironing board, In-room safe, Room service (24 hours)])}, description=overview : <p><strong>2 Twin Beds<\/strong><\/p><p>466 sq feet <\/p><br\/><p><b>Internet<\/b> - Free WiFi <\/p><p><b>Entertainment<\/b> - 42-inch LCD TV, premium channels, and DVD player<\/p><p><b>Food & Drink<\/b> - Mini-fridge, minibar (fees may apply), coffee\/tea maker, and 24-hour room service<\/p><p><b>Sleep<\/b> - Blackout drapes\/curtains, turndown service, and bed sheets <\/p><p><b>Bathroom<\/b> - Private bathroom, shower\/tub combination, bathrobes, and slippers<\/p><p><b>Practical<\/b> - Playpen, safe, and free newspaper; rollaway\/extra beds and free cribs\/infant beds available on request<\/p><p><b>Comfort<\/b> - Air conditioning and daily housekeeping<\/p><p><b>Accessibility<\/b> - Visual fire alarm, height-adjustable showerhead, low-height view port in door, low-height electrical outlets in bathroom, lever door handles, wheelchair accessible, grab bar near toilet, and accessible bathtub<\/p><p><b>Need to Know<\/b> - Shared accommodations<\/p><p>Smoking<\/p><p>Connecting\/adjoining rooms can be requested, subject to availability <\/p>, images=[https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/8081ca82_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/54128439_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/29b094b6_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/10d4b087_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/dea3738f_z.jpg], roomKey=213618194))\n","rooms_count":"1"}

                req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))
                app_data['bookHotel']=True

            if temp==3 and option=='Hotel':
                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                c={"search_query":"Riyadh, Saudi Arabia","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"2"}
                
                req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                c={"id":"467310","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/riyadh-doubletree-by-hilton-hotel-riyadh-al-muroj-business-gate-467310","title":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/","price":"40897.64","description":"Centrally located in Riyadh, DoubleTree by Hilton Hotel Riyadh - Al Muroj Business Gate is convenient to Hayat Mall and Sahara Mall","categoryid1":"Riyadh, The Northern Ring Road Exit 5. Next To The Upcoming King Abdullah Financial District","star":"4","adults_count":"5","children_count":"3","reviews":"4","rooms_count":"2","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"7"}

                req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))

                check_in=date.strftime('%d %B %Y')
                check_out=date1.strftime('%d %B %Y')
                c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"40897.64","id":"467310","hotel_name":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","hotel_rate":"4.0","room_class":"Room(adultsCount=3, availabitily=null, kidsAges=[2, 2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=2, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\nRoom(adultsCount=2, availabitily=null, kidsAges=[2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=1, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\n","rooms_count":"2"}

                req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))
                app_data['bookHotel']=True
            
            ###################------Flight Booking--------##############

            if temp==1 and option=="Flight":

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)

                departure_date=date.strftime('%Y-%m-%d')

                c={"from_location":"AUH","to_location":"DXB","departure_date":departure_date,"adults_count":"1","children_count":"0","infants_count":"0"}
                req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))
                app_data['bookFlight']=True

            if temp==2 and option=="Flight":

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)

                departure_date=date.strftime('%Y-%m-%d')

                c={"from_location":"JLR","to_location":"DEL","departure_date":departure_date,"adults_count":"2","children_count":"0","infants_count":"0"}
                req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))
                app_data['bookFlight']=True

            if temp==3 and option=="Flight":

                req = adjust_events(app_data,device_data,event_token='3juby2')
                util.execute_request(**req)

                departure_date=date.strftime('%Y-%m-%d')

                c={"from_location":"CAI","to_location":"DXB","departure_date":departure_date,"adults_count":"1","children_count":"0","infants_count":"0"}
                req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
                util.execute_request(**req)
                time.sleep(random.randint(1,5))
                app_data['bookFlight']=True

        possibility = [True]*8 + [False]*92
        random.shuffle(possibility)
        if random.choice(possibility) and app_data.get('bookFlight'):
            c={'id':str(uuid.uuid4())}
            req= adjust_events( app_data, device_data,event_token='cqhbj3',callback=c,patner=c)
            util.execute_request(**req)
            time.sleep(random.randint(1,5))
            req= adjust_events( app_data, device_data,event_token='ck5jzb',callback=c,patner=c)
            util.execute_request(**req)
            time.sleep(random.randint(1,5))
            req= adjust_events( app_data, device_data,event_token='bup4hx',callback=c,patner=c)
            util.execute_request(**req)
            time.sleep(random.randint(1,5))


    if app_data.get('bookHotel'):
        possibility = [True]*8 + [False]*92
        random.shuffle(possibility)
        if random.choice(possibility):


            today=datetime.now()
            date=today+timedelta(1)
            check_in_date=date.strftime('%m/%d/%Y')
            date1=date+timedelta(1)
            check_out_date=date1.strftime('%m/%d/%Y')

            req= adjust_events(app_data, device_data,event_token='x1ox7d')
            util.execute_request(**req)
            time.sleep(random.randint(1,5))

            req = adjust_events(app_data,device_data,event_token='3juby2')
            util.execute_request(**req)
            time.sleep(random.randint(1,5))

            c={"search_query":"Riyadh, Saudi Arabia","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"2"}

            req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
            util.execute_request(**req)
            time.sleep(random.randint(1,5))

            req = adjust_events(app_data,device_data,event_token='3juby2')
            util.execute_request(**req)
            time.sleep(random.randint(1,5))

            c={"id":"467310","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/riyadh-doubletree-by-hilton-hotel-riyadh-al-muroj-business-gate-467310","title":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/","price":"40897.64","description":"Centrally located in Riyadh, DoubleTree by Hilton Hotel Riyadh - Al Muroj Business Gate is convenient to Hayat Mall and Sahara Mall","categoryid1":"Riyadh, The Northern Ring Road Exit 5. Next To The Upcoming King Abdullah Financial District","star":"4","adults_count":"5","children_count":"3","reviews":"4","rooms_count":"2","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"7"}

            req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
            util.execute_request(**req)
            time.sleep(random.randint(1,5))

            check_in=date.strftime('%d %B %Y')
            check_out=date1.strftime('%d %B %Y')
            c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"40897.64","id":"467310","hotel_name":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","hotel_rate":"4.0","room_class":"Room(adultsCount=3, availabitily=null, kidsAges=[2, 2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=2, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\nRoom(adultsCount=2, availabitily=null, kidsAges=[2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=1, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\n","rooms_count":"2"}

            req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
            util.execute_request(**req)
            time.sleep(random.randint(1,5))





    return {'status':True}

#==================================================================================================================================================================================


def adjust_session( app_data, device_data):

    url='https://'+adjust_data.get('url')+'/session'
    
    httpmethod='post'

    app_data['session_started']=int(time.time())

    if not app_data.get('session_count'):
        app_data['session_count'] = 1
    else:
        app_data['session_count'] +=1
    
    headers={
            'Client-SDK':campaign_data.get('adjust').get('sdk'),
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
            'Accept-Encoding':'gzip'
    }

    params={}

    data={
        'android_uuid':app_data.get('android_uuid'),
        'api_level':device_data.get('sdk'),
        'app_token':campaign_data.get('adjust').get('app_token'),
        'app_version':campaign_data.get('app_version_name'),
        'attribution_deeplink':1,
        'connectivity_type':1,
        # 'country':device_data.get('locale').get('country'),
        'cpu_type':device_data.get('cpu'),
        'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'device_manufacturer':device_data.get('manufacturer'),
        'device_name':device_data.get('model'),
        'device_type':device_data.get('device_type'),
        'display_height':device_data.get('resolution').split('x')[-2],
        'display_width':device_data.get('resolution').split('x')[-1],
        'environment':'production',
        'event_buffering_enabled':0,
        # 'fb_id':app_data.get('fb_id'),
        'gps_adid':device_data.get('adid'),
        'gps_adid_src':'service',
        "gps_adid_attempt": 1,
        'hardware_name':device_data.get('hardware'),
        'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'language':device_data.get('locale').get('language'),
        'needs_response_details':1,
        'network_type':0,
        'os_build':device_data.get('build'),
        'os_name':'android',
        "mcc":int(device_data.get('mcc')),
        "mnc":int(device_data.get('mnc')),
        'os_version':device_data.get('os_version'),
        'package_name':campaign_data.get('package_name'),
        'screen_density':get_screen_density(device_data),
        'screen_format':get_screen_format(device_data),
        'screen_size':'normal',
        'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'session_count':app_data.get('session_count'),
        'tracking_enabled':1,
        "ui_mode"  :    "1",
        'updated_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        # "vm_isa":device_data.get('cpu')[:-4]
    }

    if session_data.get('vm_isa'):
        data['vm_isa'] = device_data.get('cpu')[:-4]
    if session_data.get('app_secret'):
        data['app_secret'] = session_data.get('app_secret')
    
    if session_data.get('ui_mode'):
        data['ui_mode'] = 1
    if session_data.get('fb_id'):
        data['fb_id'] = app_data.get('fb_id')



    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')
    app_data['subsession']=1
    if campaign_data.get('adjust').get('app_secret'):
        headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'session')

    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#====================================================================================

def adjust_sdk_click(app_data,device_data):

    url='https://'+adjust_data.get('url')+'/sdk_click'
    httpmethod='post'
    app_data['session_started']=int(time.time())
    headers={
            'Client-SDK': campaign_data.get('adjust').get('sdk'),
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
        'Accept-Encoding':'gzip',

    }

    params={}

    
    data={
            'android_uuid':app_data.get('android_uuid'),
            'api_level':device_data.get('sdk'),
            'app_token':campaign_data.get('adjust').get('app_token'),
            'app_version':campaign_data.get('app_version_name'),
            'attribution_deeplink':1,
            'connectivity_type':1,
            "mcc":int(device_data.get('mcc')),
            "mnc":int(device_data.get('mnc')),
            'click_time':        datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
            "click_time_server": datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
            # 'country':device_data.get('locale').get('country'),
            'cpu_type':device_data.get('cpu'),
            'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
            'device_manufacturer':device_data.get('manufacturer'),
            'device_name':device_data.get('model'),
            'device_type':device_data.get('device_type'),
            'display_height':device_data.get('resolution').split('x')[-2],
            'display_width':device_data.get('resolution').split('x')[-1],
            'environment':'production',
            'event_buffering_enabled':0,
            'google_play_instant':0,
            'gps_adid_attempt':1,
            # 'fb_id':app_data.get('fb_id'),
            'gps_adid':device_data.get('adid'),
            'gps_adid_src':'service',
            'hardware_name':device_data.get('hardware'),
            'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
            "install_begin_time":datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
            "install_begin_time_server":    datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
            'install_version':campaign_data.get('app_version_name'),
            'language':device_data.get('locale').get('language'),
            'needs_response_details':1,
            'network_type':0,
            'os_build':device_data.get('build'),
            'os_name':'android',
            'os_version':device_data.get('os_version'),
            'package_name':campaign_data.get('package_name'),
            'referrer':app_data.get('referrer') or 'utm_source=(not%20set)&utm_medium=(not%20set)',
            'referrer_api':'google',
            'screen_density':get_screen_density(device_data),
            'screen_format':get_screen_format(device_data),
            'screen_size':'normal',
            'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
            'session_count':app_data.get('session_count'),
            'session_length':int(time.time())- app_data.get('session_started'),
            'source':'install_referrer',
            'subsession_count':subsession(app_data),
            'time_spent':time_spent(app_data),
            'tracking_enabled':1,
            "ui_mode"  :    "1",
            'updated_at': datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone') or None,
            # "vm_isa":device_data.get('cpu')[:-4]
    }

    if sdk_click_data.get('vm_isa'):
        data['vm_isa'] = device_data.get('cpu')[:-4]
    if sdk_click_data.get('app_secret'):
        data['app_secret'] = sdk_click_data.get('app_secret')
    
    if sdk_click_data.get('ui_mode'):
        data['ui_mode'] = 1
    if sdk_click_data.get('install_version'):
        data['install_version'] = sdk_click_data.get('install_version')



    if sdk_click_data.get('click_time'):
        data['click_time'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

    if sdk_click_data.get('click_time_server'):
        data['click_time_server'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

    if sdk_click_data.get('install_begin_time'):
        data['install_begin_time'] = datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone')
    if sdk_click_data.get('install_begin_time_server'):
        data['install_begin_time_server'] =datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),

            
    if sdk_click_data.get('fb_id'):
        data['fb_id'] = app_data.get('fb_id')

    if sdk_click_data.get('install_version'):
        data['install_version'] = sdk_click_data.get('install_version')

    if sdk_click_data.get('install_version'):
        data['install_version'] = sdk_click_data.get('install_version')

    if sdk_click_data.get('referrer_api'):
        data['referrer_api'] = sdk_click_data.get('referrer_api')

    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')
    if campaign_data.get('adjust').get('app_secret'):
        headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'sdk_click')

    # data['click_time_server'] = datetime.utcfromtimestamp(int(app_data.get('times').get('click_time')) +  timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
    # data['install_begin_time_server'] = datetime.utcfromtimestamp((app_data.get('times').get('download_begin_time')+app_data.get('sec')) + timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#==================================================================================

def adjust_attribution(app_data,device_data,initiated_by=None):

    url='https://'+adjust_data.get('url')+'/attribution'

    httpmethod='get'

    headers={
        'Client-SDK':campaign_data.get('adjust').get('sdk'),
        'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
        'Accept-Encoding':'gzip',
    }

    params={
            'android_uuid':app_data.get('android_uuid'),
            'api_level':device_data.get('sdk'),
            'app_token':campaign_data.get('adjust').get('app_token'),
            'app_version':campaign_data.get('app_version_name'),
            # 'app_secret':campaign_data.get('adjust').get('app_secret'),
            'attribution_deeplink':1,
            'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
            'device_name':device_data.get('model'),
            'device_type':device_data.get('device_type'),
            'environment':'production',
            'event_buffering_enabled':0,
            'gps_adid':device_data.get('adid'),
            'gps_adid_src':'service',     
            'gps_adid_attempt':1,
            # 'fb_id':app_data.get('fb_id'),
            'initiated_by':initiated_by,
            'needs_response_details':1,
            'os_name':'android',
            'os_version':device_data.get('os_version'),
            'package_name':campaign_data.get('package_name'),
            'tracking_enabled':1,
            # 'secret_id':'2',
            "ui_mode"  :    "1",
            'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
            # 'session_count':app_data.get('session_count'),
    }

    if atribution_data.get('app_secret'):
        params['app_secret'] = atribution_data.get('app_secret')
    if atribution_data.get('secret_id'):
        params['secret_id'] = atribution_data.get('secret_id')
    if atribution_data.get('initiated_by'):
        params['initiated_by'] = atribution_data.get('initiated_by')
    if atribution_data.get('ui_mode'):
        params['ui_mode'] = 1
    if app_data.get('pushtoken'):
        params['push_token'] = app_data.get('pushtoken')



    data=None
    if campaign_data.get('adjust').get('app_secret'):
        headers['Authorization'] = get_auth(params.get('created_at'),params.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'attribution')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


#====================================================================================
def adjust_sdk_info(app_data,device_data):

    url='https://'+adjust_data.get('url')+'/sdk_info'

    httpmethod='post'
    pushtoken(app_data)
    headers={
        'Client-SDK':campaign_data.get('adjust').get('sdk'),
        'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
        'Accept-Encoding':'gzip',
    }

    data={
            # 'android_uuid':app_data.get('android_uuid'),
            'app_token':campaign_data.get('adjust').get('app_token'),
            'attribution_deeplink':1,
            'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
            'environment':'production',
            'event_buffering_enabled':0,
            'gps_adid':device_data.get('adid'),
            # 'gps_adid_src':'service',  
            # 'gps_xadid_attempt':1,
            'needs_response_details':1,
            "push_token":app_data.get('pushtoken'),
            "source":"push",
            'tracking_enabled':1,
            'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
    }
    # if adjust_data.get('sdk_info'):
    #   if sdk_info_data.get('android_uuid'):
    #       data['android_uuid'] = app_data.get('android_uuid')
    #   if sdk_info_data.get('gps_adid_attempt'):
    #       data['gps_adid_attempt'] = sdk_info_data.get('gps_adid_attempt')
    #   if sdk_info_data.get('gps_xadid_attempt'):
    #       data['gps_xadid_attempt'] = sdk_info_data.get('gps_xadid_attempt')





    params=None
    if campaign_data.get('adjust').get('app_secret'):
        headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'sdk_info')
    
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#================================================================
def adjust_events(app_data,device_data,event_token=None,callback = None,patner= None):

    url='https://'+adjust_data.get('url')+'/event'

    httpmethod='post'

    headers={
            'Client-SDK':campaign_data.get('adjust').get('sdk'),
            'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip',    
    }

    params=None

    
    if not app_data.get('event_count'):
        app_data['event_count']=1
    else:
        app_data['event_count']=app_data['event_count']+1

    # print(app_data)

    data={
        'android_uuid':app_data.get('android_uuid'),
        'api_level':device_data.get('sdk'),
        'app_token':campaign_data.get('adjust').get('app_token'),
        'app_version':campaign_data.get('app_version_name'),
        'attribution_deeplink':1,
        'connectivity_type':1,
        "queue_size":   1,
        # 'country':device_data.get('locale').get('country'),
        'cpu_type':device_data.get('cpu'),
        'callback_params':json.dumps(callback),
        'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'device_manufacturer':device_data.get('manufacturer'),
        'device_name':device_data.get('model'),
        'device_type':device_data.get('device_type'),
        'display_height':device_data.get('resolution').split('x')[-2],
        'display_width':device_data.get('resolution').split('x')[-1],
        'environment':'production',
        'event_buffering_enabled':0,
        'event_count':app_data.get('event_count'),
        'event_token':event_token,
        'gps_adid':device_data.get('adid'),
        'gps_adid_attempt':'1',
        'gps_adid_src':'service',
        "mcc":int(device_data.get('mcc')),
        "mnc":int(device_data.get('mnc')),
        # 'fb_id':app_data.get('fb_id'),
        'hardware_name':device_data.get('hardware'),
        'language':device_data.get('locale').get('language'),
        'needs_response_details':1,
        'network_type':0,
        'os_build':device_data.get('build'),
        'os_name':'android',
        'os_version':device_data.get('os_version'),
        'package_name':campaign_data.get('package_name'),
        'partner_params' : patner,
        # 'push_token' : push_token,
        # "partner_params":partner_params,
        'screen_density':get_screen_density(device_data),
        'screen_format':get_screen_format(device_data),
        'session_count':app_data.get('session_count'),
        'session_length':int(time.time())-app_data.get('session_started'),
        'screen_size':'normal',
        'subsession_count':subsession(app_data),
        'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
        'time_spent':time_spent(app_data),
        'tracking_enabled':1,
        'ui_mode'   :'1',
        #  "vm_isa":device_data.get('cpu')[:-4]

    }


    if event_data.get('vm_isa'):
        data['vm_isa'] = device_data.get('cpu')[:-4]
    if event_data.get('app_secret'):
        data['app_secret'] = event_data.get('app_secret')
    
    if event_data.get('ui_mode'):
        data['ui_mode'] = 1
    if event_data.get('fb_id'):
        data['fb_id'] = app_data.get('fb_id')


    if app_data.get('pushtoken'):
        data['push_token'] = app_data.get('pushtoken')

    if callback:
        data['callback_params'] = json.dumps(callback)
    if patner:
        data['partner_params'] = json.dumps(patner)

    if campaign_data.get('adjust').get('app_secret'):
        headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'event')
    return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#============================================================================================
def firbaseinstall(app_data,device_data):
    url='https://firebaseinstallations.googleapis.com/v1/projects/almatar-d9f4b/installations'
    httpmethod='post'
    headers={
            "Content-Type":"application/json",
            "Accept":"application/json",
            "Cache-Control":"no-cache",
            "X-Android-Package":"com.almatar",
            "x-firebase-client":"H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
            "X-Android-Cert":"4549570A0DEC9352FB18BD81B29B935419157B30",
            "x-goog-api-key":"AIzaSyBgA4CfEahdfu9Rvzwde1Gy7ulMriYTrj8",
            "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 10; SM-G960F Build/QP1A.190711.020)",
            "Accept-Encoding":"gzip"
        }
    params=None
    data={
        "fid": util.get_fid(),
        "appId": "1:226769515969:android:146bd37e6baf4679",
        "authVersion": "FIS_v2",
        "sdkVersion": "a:17.1.3"
        }

    return {'url':url,'httpmethod':httpmethod,'headers':headers,'params':params,'data':json.dumps(data)}
#============================================================================================

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

def pushtoken(app_data):
    if not app_data.get('pushtoken'):
        app_data['pushtoken']=util.get_random_string('hex',64)


def get_country():
    weighted_choices = campaign_data['country'] if campaign_data.get('country') else ('USA', 4)
    country_list = [val for val, cnt in weighted_choices for i in range(cnt)]
    return random.choice(country_list)

def get_retention(day):
    return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0

def click(device_data=None, camp_type='market', camp_plat = 'android'):

    package_name = campaign_data.get('package_name')
    serial        = device_data.get('serial')
    agent_id      = Config.AGENTID
    random_number = random.randint(1,10)
    source_id     = ""
    if random_number < 5:
        source_id = "728"
    elif random_number < 8:
        source_id = "517"
    elif random_number < 9:
        source_id = "604"
    else:
        source_id = "386"
    st = device_data.get("device_id", str(int(time.time()*1000)))
    link = campaign_data['link']
    link = link.format(dp2=st,agent=agent_id,source=source_id,device_serial=serial,gaid=device_data.get('adid'))
    return clicker.click(link, device_data, camp_type, camp_plat, 'url=', package_name)

#######################################################################################



    
# #-*- coding: utf-8 -*-
# # created by him@nshu/Nihal
# import sys,base64
# reload(sys)
# sys.setdefaultencoding('utf-8')
# from datetime import datetime,timedelta
# from sdk import installtimenew, util, NameLists
# import clicker, Config
# from sdk import NameLists
# from hashlib import sha1
# import time, random, json, string, urllib, uuid, hashlib
# from spicipher import af_cipher
# from requests import Request
# from collections import OrderedDict


# campaign_data = {
# 'tracker' : ['adjust'],
# 'app_name' : 'almatar Hotel & Flight Booking',
# 'package_name' : 'com.almatar',
# 'app_version_name' : '2.13.26', #2.12.25 #2.12.28 #2.13.1 #2.13.5 #2.13.7 #2.13.14 #2.13.17 #2.13.24 #2.13.25
# 'app_version_code'      : '120', #76 #89 #95 #99 #101 #108 #111 #113 #119
# 'supported_countries' : 'WW',
# 'supported_os' : '8',
# # 'link' : 'http://offerrobo.g2prof.net/click?offer_id=62f21c04d06424466b7ed7bb&aff_id=62&adv_id=62a1d0f8e3d0aa0e743b7011&aff_sub1={aff_click_id}&aff_sub2={gaid}&aff_sub3={idfa}&aff_sub6={app_name}&source={source}',
# 'adjust' : {'app_token': '1hxr2nrmjajk', 'sdk': 'android4.28.7'},
# 'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
# 'retention' : {1: 85, 2: 82, 3: 78, 4: 75, 5: 70, 6: 66, 7: 62, 8: 58, 9: 55, 10: 50, 11: 48, 12: 45, 13: 40, 14: 39, 15: 38, 16: 37, 17: 35, 18: 35, 19: 34, 20: 33, 21: 32, 22: 31, 23: 30, 24: 29, 25: 29, 26: 28, 27: 27, 28: 26, 29: 25, 30: 25, 31: 24, 32: 23, 33: 23, 34: 22, 35: 22, 36: 21, 37: 20, 38: 19, 39: 19, 40: 18, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 14, 47: 13, 48: 13, 49: 12, 50: 11, 51: 11, 52: 10, 53: 9, 54: 9, 55: 8, 56: 7, 57: 6, 58: 5, 59: 4, 60: 3},
# 'app_size' :13,
#     }
# adjust_data = {"event_name": ["l3eknk", "3juby2", "jppvja", "40faqo","30ls2a","3juby2"], "initiated_by": "backend", "url": "app.adjust.com", "partner": {"l3eknk": "{\"search_query\":\"Cairo, Egypt\",\"check_in_date\":\"07\\/19\\/2022\",\"check_out_date\":\"07\\/20\\/2022\",\"rooms_count\":\"1\"}", "jppvja": "{\"id\":\"1175870\",\"link\":\"https:\\/\\/almatar.com\\/en\\/hotels\\/rooms\\/giza-3-pyramids-view-inn-1175870\",\"title\":\"3 Pyramids View Inn\",\"image_link\":\"https:\\/\\/az712897.vo.msecnd.net\\/images\\/full\\/com.almtaar.model.accommodation.Image@f45ade4\",\"price\":\"93.08\",\"description\":\"Located in Cairo 3 Pyramids View Inn features free WiFi. Around 800 metres from Cheops Pyramid the property is also close to Chefren pyramid. The accommodation offers free shuttle service a 24-hour front desk and buying tickets for guests.Selected rooms include a kitchen with an oven a microwave and a toaster.A continental breakfast is available each morning at the inn.3 Pyramids View Inn offers a terrace. Hiking is among the activities that guests can enjoy near the accommodation.Mikerinus pyramid is 1.5 km from 3 Pyramids View Inn while Viewpoint and Camel rides is 2.2 km away. The nearest airport is Cairo International Airport 29 km from the property.\",\"categoryid1\":\"Giza, 7 Abou Al Hool Al Seiahi Al Haram\",\"star\":\"3\",\"adults_count\":\"1\",\"children_count\":\"0\",\"reviews\":\"5\",\"rooms_count\":\"1\",\"check_in_date\":\"07\\/20\\/2022\",\"check_out_date\":\"07\\/19\\/2022\",\"number_of_nights\":\"1\"}", "3juby2": "{\"search_query\":\"Cairo, Egypt\",\"check_in_date\":\"07\\/19\\/2022\",\"check_out_date\":\"07\\/20\\/2022\",\"rooms_count\":\"1\"}", "40faqo": "{\"currency\":\"SAR\",\"check_in_date\":\"19 July 2022\",\"check_out_date\":\"20 July 2022\",\"price\":\"93.08\",\"id\":\"1175870\",\"hotel_name\":\"3 Pyramids View Inn\",\"hotel_rate\":\"3.0\",\"room_class\":\"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\\n\",\"rooms_count\":\"1\"}","30ls2a":{"from_location":"AUH","to_location":"DXB","departure_date":"2022-07-08","adults_count":"1","children_count":"0","infants_count":"0"}}, "call_back": {"l3eknk": {"check_in_date": "07/19/2022", "search_query": "Cairo, Egypt", "check_out_date": "07/20/2022", "rooms_count": "1"}, "jppvja": {"reviews": "5", "star": "3", "description": "Located in Cairo 3 Pyramids View Inn features free WiFi. Around 800 metres from Cheops Pyramid the property is also close to Chefren pyramid. The accommodation offers free shuttle service a 24-hour front desk and buying tickets for guests.Selected rooms include a kitchen with an oven a microwave and a toaster.A continental breakfast is available each morning at the inn.3 Pyramids View Inn offers a terrace. Hiking is among the activities that guests can enjoy near the accommodation.Mikerinus pyramid is 1.5 km from 3 Pyramids View Inn while Viewpoint and Camel rides is 2.2 km away. The nearest airport is Cairo International Airport 29 km from the property.", "check_in_date": "07/20/2022", "title": "3 Pyramids View Inn", "price": "93.08", "children_count": "0", "adults_count": "1", "image_link": "https://az712897.vo.msecnd.net/images/full/com.almtaar.model.accommodation.Image@f45ade4", "number_of_nights": "1", "check_out_date": "07/19/2022", "link": "https://almatar.com/en/hotels/rooms/giza-3-pyramids-view-inn-1175870", "rooms_count": "1", "id": "1175870", "categoryid1": "Giza, 7 Abou Al Hool Al Seiahi Al Haram"}, "3juby2": {"check_in_date": "07/19/2022", "search_query": "Cairo, Egypt", "check_out_date": "07/20/2022", "rooms_count": "1"}, "40faqo": {"price": "93.08", "room_class": "Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\n", "hotel_rate": "3.0", "check_in_date": "19 July 2022", "currency": "SAR", "check_out_date": "20 July 2022", "id": "1175870", "hotel_name": "3 Pyramids View Inn", "rooms_count": "1"},"30ls2a":{"from_location":"AUH","to_location":"DXB","departure_date":"2022-07-08","adults_count":"1","children_count":"0","infants_count":"0"}}}

# session_data = {"event_buffering_enabled": "0", "updated_at": "2022-07-08T12:23:24.801Z+0530", "needs_response_details": "1", "os_name": "android", "device_type": "phone", "device_manufacturer": "Xiaomi", "tracking_enabled": "1", "connectivity_type": "1", "package_name": "com.almatar", "installed_at": "2022-07-08T12:23:24.801Z+0530", "environment": "production", "os_version": "9", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "display_width": "1080", "app_version": "2.12.13", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "screen_size": "normal", "gps_adid_attempt": "1", "hardware_name": "PKQ1.181203.001", "gps_adid_src": "service", "screen_format": "long", "display_height": "2130", "app_token": "1hxr2nrmjajk", "sent_at": "2022-07-08T12:25:47.548Z+0530", "attribution_deeplink": "1", "screen_density": "high", "language": "ar", "created_at": "2022-07-08T12:25:47.297Z+0530", "session_count": "1", "device_name": "Redmi Note 7 Pro", "cpu_type": "arm64-v8a", "ui_mode": "1", "network_type": "0", "api_level": "28", "os_build": "PKQ1.181203.001"}

# sdk_click_data = {"event_buffering_enabled": "0", "google_play_instant": "0", "updated_at": "2022-07-08T12:23:24.801Z+0530", "needs_response_details": "1", "time_spent": "0", "os_name": "android", "device_type": "phone", "device_manufacturer": "Xiaomi", "tracking_enabled": "1", "connectivity_type": "1", "package_name": "com.almatar", "click_time": "2022-07-08T12:22:40.000Z+0530", "os_version": "9", "installed_at": "2022-07-08T12:23:24.801Z+0530", "environment": "production", "source": "install_referrer", "install_begin_time": "2022-07-08T12:22:43.000Z+0530", "session_length": "0", "install_version": "2.12.13", "display_width": "1080", "app_version": "2.12.13", "subsession_count": "1", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "referrer_api": "google", "screen_size": "normal", "gps_adid_attempt": "1", "hardware_name": "PKQ1.181203.001", "gps_adid_src": "service", "screen_format": "long", "display_height": "2130", "app_token": "1hxr2nrmjajk", "sent_at": "2022-07-08T12:25:47.916Z+0530", "attribution_deeplink": "1", "screen_density": "high", "language": "ar", "referrer": "utm_source=(not%20set)&utm_medium=(not%20set)", "created_at": "2022-07-08T12:25:47.737Z+0530", "session_count": "1", "device_name": "Redmi Note 7 Pro", "click_time_server": "2022-07-08T12:22:37.000Z+0530", "cpu_type": "arm64-v8a", "ui_mode": "1", "install_begin_time_server": "2022-07-08T12:22:40.000Z+0530", "network_type": "0", "api_level": "28", "os_build": "PKQ1.181203.001"}

# atribution_data = {"attribution_deeplink": "1", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "tracking_enabled": "1", "package_name": "com.almatar", "event_buffering_enabled": "0", "initiated_by": "backend", "created_at": "2022-07-08T12:26:02.649Z+0530", "gps_adid_attempt": "1", "needs_response_details": "1", "device_name": "Redmi Note 7 Pro", "environment": "production", "os_version": "9", "os_name": "android", "gps_adid_src": "service", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "device_type": "phone", "ui_mode": "1", "app_token": "1hxr2nrmjajk", "app_version": "2.12.13", "api_level": "28", "sent_at": "2022-07-08T12:26:02.657Z+0530"}

# event_data = {"event_buffering_enabled": "0", "event_token": "40faqo", "needs_response_details": "1", "time_spent": "246", "callback_params": "{\"currency\":\"SAR\",\"check_in_date\":\"19 July 2022\",\"check_out_date\":\"20 July 2022\",\"price\":\"93.08\",\"id\":\"1175870\",\"hotel_name\":\"3 Pyramids View Inn\",\"hotel_rate\":\"3.0\",\"room_class\":\"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\\n\",\"rooms_count\":\"1\"}", "os_name": "android", "device_type": "phone", "device_manufacturer": "Xiaomi", "tracking_enabled": "1", "connectivity_type": "1", "package_name": "com.almatar", "environment": "production", "os_version": "9", "session_length": "263", "app_token": "1hxr2nrmjajk", "app_version": "2.12.13", "subsession_count": "2", "android_uuid": "425ada7b-2443-46ef-a6b2-e4fb070cd203", "partner_params": "{\"currency\":\"SAR\",\"check_in_date\":\"19 July 2022\",\"check_out_date\":\"20 July 2022\",\"price\":\"93.08\",\"id\":\"1175870\",\"hotel_name\":\"3 Pyramids View Inn\",\"hotel_rate\":\"3.0\",\"room_class\":\"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\\n\",\"rooms_count\":\"1\"}", "gps_adid": "f0cd37e0-aebd-4f0b-9899-0b9b24dc65b8", "screen_size": "normal", "gps_adid_attempt": "1", "hardware_name": "PKQ1.181203.001", "gps_adid_src": "service", "screen_format": "long", "display_height": "2130", "display_width": "1080", "sent_at": "2022-07-08T12:30:10.594Z+0530", "attribution_deeplink": "1", "screen_density": "high", "language": "ar", "event_count": "4", "created_at": "2022-07-08T12:30:10.300Z+0530", "session_count": "1", "device_name": "Redmi Note 7 Pro", "cpu_type": "arm64-v8a", "ui_mode": "1", "network_type": "0", "api_level": "28", "os_build": "PKQ1.181203.001"}




# def install(app_data, device_data):
#     # print "Please wait installing..."
#     if not app_data.get('times'):
#         installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')

#     if not app_data.get('sec'):
#         timez=device_data.get('timezone')    
#         sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
#         if int(timez) < 0:
#             sec = (-1) * sec
#         app_data['sec'] = sec



#     if not app_data.get('android_uuid'):
#         app_data['android_uuid']=str(uuid.uuid4())

#     # if not app_data.get('fb_id'):
#     #     app_data['fb_id']=str(uuid.uuid4())


#     # print 'Session'
#     req = adjust_session(app_data, device_data)
#     util.execute_request(**req)
#     time.sleep(random.randint(1,5))

#     # print 'Sdk_click'
#     req = adjust_sdk_click( app_data, device_data)
#     util.execute_request(**req)
#     time.sleep(random.randint(1,5))



#     if adjust_data.get('sdk_info'):
#         req = adjust_sdk_info(app_data,device_data)
#         util.execute_request(**req)



#     # print 'Attribution'
#     req = adjust_attribution(app_data, device_data)
#     util.execute_request(**req)

#     #-----------date--------------------------
#     opt=["Hotel","Flight","Hotel"]
#     option=random.choice(opt)
#     possibility = [True]*30 + [False]*70
#     random.shuffle(possibility)
#     #####################################
#     #       Dates
#     #####################################
#     today=datetime.now()
#     date=today+timedelta(1)
#     check_in_date=date.strftime('%m/%d/%Y')
#     date1=date+timedelta(1)
#     check_out_date=date1.strftime('%m/%d/%Y')

#     ########################################

#     poss =[True]*30+[False]*70
#     random.shuffle(poss)
#     if random.choice(poss):
#         c={'registration_method':'Google'}
#         req= adjust_events( app_data, device_data,event_token='prniaw',callback=c,patner=c)
#         util.execute_request(**req)
#         app_data['registartion'] =True
#     # time.sleep(random.randint(1,5))

#     if random.choice(possibility) and option=="Hotel":
#         req= adjust_events(app_data, device_data,event_token='3juby2')
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))
# # {"search_query":"Dubai, United Arab Emirates","check_in_date":"11\/22\/2022","check_out_date":"11\/23\/2022","rooms_count":"1"}
#         c=random.choice([{"search_query":"Dubai,United Arab Emirates","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"دبي, الإمارات العربية المتحدة","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"غازي آباد، غازي آباد، الهند","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"}])
#         req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))

#         req = adjust_events(app_data,device_data,event_token='isa7cy')
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))

#         req = adjust_events(app_data,device_data,event_token='3juby2')
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))

#         c=random.choice([{"id":"15026","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/dubai-arabian-ranches-golf-club-15026","title":"Arabian Ranches Golf Club","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/com.almtaar.model.accommodation.Image@cd5748e","price":"331.48","description":"With a stay at Arabian Ranches Golf Club in Arabian Ranches, you'll be close to Arabian Ranches Golf Club and Dubai Autodrome","categoryid1":"Dubai, Arabian Ranches Emirates Road Po Box 367","star":"2","adults_count":"1","children_count":"0","reviews":"5","rooms_count":"1","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"1"},
#                             {"id":"27058","link":"https:\/\/almatar.com\/ar\/hotels\/rooms\/new-delhi-maidens-hotel-delhi-27058","title":"Maidens Hotel Delhi","price":"679.05","description":"With a stay at Maidens Hotel, Delhi in New Delhi, you'll be in the historical district and convenient to St","categoryid1":"New Delhi, 7 Sham Nath Marg","star":"5","adults_count":"1","children_count":"0","reviews":"4.5","rooms_count":"1","check_in_date":"05\/24\/2023","check_out_date":"05\/23\/2023","number_of_nights":"1"}])

#         req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))

#         check_in=date.strftime('%d %B %Y')
#         check_out=date1.strftime('%d %B %Y')

#         c={"price": "93.08", "room_class": "Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Bed and Breakfast, roomView=pyramids view, twin beds, roomName=Room with pyramids view, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free breakfast, Early check-in, Free self parking, Free WiFi])}, description=, images=[], roomKey=202310149))\n", "hotel_rate": "3.0", "check_in_date": check_in, "currency": "SAR", "check_out_date": check_out, "id": "1175870", "hotel_name": "3 Pyramids View Inn", "rooms_count": "1"}
#         req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))

#     if random.choice(possibility) and option=="Flight":
#         departure_date=date.strftime('%Y-%m-%d')

#         c={"from_location":"AUH","to_location":"DXB","departure_date":departure_date,"adults_count":"1","children_count":"0","infants_count":"0"}
#         req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
#         util.execute_request(**req)
#         time.sleep(random.randint(1,5))

#     return {'status':True}
# #============================================================================================================================
# def open(app_data, device_data, day =1):
#     if app_data.get('times'):
#         # print 'Session'
#         req = adjust_session(app_data, device_data)
#         util.execute_request(**req)

#         if random.randint(1,10)>8:
#             req= adjust_events(app_data, device_data,event_token='ore26o')  #Open from push notification
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))

#         if not app_data.get('registartion') and day <7:
#             poss =[True]*5+[False]*95
#             random.shuffle(poss)
#             if random.choice(poss):
#                 c={'registration_method':'Google'}
#                 req= adjust_events( app_data, device_data,event_token='prniaw',callback=c,patner=c)
#                 util.execute_request(**req)
#                 app_data['registartion'] =True


#         possibility = [True]*10 + [False]*90
#         random.shuffle(possibility)
#         if random.choice(possibility):
#             temp=random.randint(1,3)
#             opt=["Hotel","Flight","Hotel"]
#             option=random.choice(opt)
#             # print(temp,option)

#             today=datetime.now()
#             date=today+timedelta(1)
#             check_in_date=date.strftime('%m/%d/%Y')
#             date1=date+timedelta(1)
#             check_out_date=date1.strftime('%m/%d/%Y')

#             if temp==1 and option=='Hotel':



#                 req = adjust_events(app_data,device_data,event_token='isa7cy')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 c=random.choice([{"search_query":"Dubai,United Arab Emirates","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"دبي, الإمارات العربية المتحدة","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"غازي آباد، غازي آباد، الهند","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"}])

#                 req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))


#                 c=random.choice([{"id":"15026","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/dubai-arabian-ranches-golf-club-15026","title":"Arabian Ranches Golf Club","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/com.almtaar.model.accommodation.Image@cd5748e","price":"331.48","description":"With a stay at Arabian Ranches Golf Club in Arabian Ranches, you'll be close to Arabian Ranches Golf Club and Dubai Autodrome","categoryid1":"Dubai, Arabian Ranches Emirates Road Po Box 367","star":"2","adults_count":"1","children_count":"0","reviews":"5","rooms_count":"1","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"1"},
#                                  {"id":"27058","link":"https:\/\/almatar.com\/ar\/hotels\/rooms\/new-delhi-maidens-hotel-delhi-27058","title":"Maidens Hotel Delhi","price":"679.05","description":"With a stay at Maidens Hotel, Delhi in New Delhi, you'll be in the historical district and convenient to St","categoryid1":"New Delhi, 7 Sham Nath Marg","star":"5","adults_count":"1","children_count":"0","reviews":"4.5","rooms_count":"1","check_in_date":"05\/24\/2023","check_out_date":"05\/23\/2023","number_of_nights":"1"}])
#                 req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))#view hotel 

#                 check_in=date.strftime('%d %B %Y')
#                 check_out=date1.strftime('%d %B %Y')
#                 c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"331.48","id":"15026","hotel_name":"Arabian Ranches Golf Club","hotel_rate":"2.0","room_class":"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Deluxe room, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={more=Amenity(name=More, values=[Free self parking, Free WiFi])}, description=, images=[], roomKey=315844154))\n","rooms_count":"1"}
                
#                 req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5)) #for enter you persnal details
#                 app_data['bookHotel']=True

#             if temp==2 and option=='Hotel':
#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 c=random.choice([{"search_query":"Dubai,United Arab Emirates","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"دبي, الإمارات العربية المتحدة","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"غازي آباد، غازي آباد، الهند","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"}])
                
#                 req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 c=random.choice([{"id":"15026","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/dubai-arabian-ranches-golf-club-15026","title":"Arabian Ranches Golf Club","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/com.almtaar.model.accommodation.Image@cd5748e","price":"331.48","description":"With a stay at Arabian Ranches Golf Club in Arabian Ranches, you'll be close to Arabian Ranches Golf Club and Dubai Autodrome","categoryid1":"Dubai, Arabian Ranches Emirates Road Po Box 367","star":"2","adults_count":"1","children_count":"0","reviews":"5","rooms_count":"1","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"1"},
#                                  {"id":"27058","link":"https:\/\/almatar.com\/ar\/hotels\/rooms\/new-delhi-maidens-hotel-delhi-27058","title":"Maidens Hotel Delhi","price":"679.05","description":"With a stay at Maidens Hotel, Delhi in New Delhi, you'll be in the historical district and convenient to St","categoryid1":"New Delhi, 7 Sham Nath Marg","star":"5","adults_count":"1","children_count":"0","reviews":"4.5","rooms_count":"1","check_in_date":"05\/24\/2023","check_out_date":"05\/23\/2023","number_of_nights":"1"}])

#                 req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 check_in=date.strftime('%d %B %Y')
#                 check_out=date1.strftime('%d %B %Y')
#                 c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"1989.15","id":"51580","hotel_name":"The Ritz Carlton Riyadh","hotel_rate":"5.0","room_class":"Room(adultsCount=1, availabitily=null, kidsAges=[], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Standard room, twin beds, roomSize=null, bedType=Twin, roomClass=, numOfChildren=0, roomType=, roomContent=RoomContent(amenities={bedroom=Amenity(name=Bedroom, values=[Air conditioning, Turndown service, Free cribs\/infant beds, Rollaway\/extra beds (surcharge)]), bathroom=Amenity(name=Bathroom, values=[Slippers, Shower\/tub combination, Private bathroom, Bathrobes, Towels provided]), food_drink=Amenity(name=Food & drink, values=[Free bottled water, Coffee\/tea maker]), entertainment=Amenity(name=Entertainment, values=[Premium TV channels, Satellite TV service, LCD TV, Local maps, Guidebooks or recommendations]), more=Amenity(name=More, values=[Free newspaper, Wheelchair accessible, Blackout drapes\/curtains, Connecting\/adjoining rooms available, Shared accommodation, Television, Smoking, Height-adjustable showerhead, Grab bar - near toilet, Minibar, Wardrobe or closet, Daily housekeeping, Free WiFi, In-room playpen, Restaurant dining guide, Bedsheets provided, Lowered electrical outlets in bathroom, Mini-fridge, Lowered peephole\/view port in door, Accessible bathtub, Visual fire alarm, Lever door handles, DVD player, Free toiletries, Hair dryer, Iron\/ironing board, In-room safe, Room service (24 hours)])}, description=overview : <p><strong>2 Twin Beds<\/strong><\/p><p>466 sq feet <\/p><br\/><p><b>Internet<\/b> - Free WiFi <\/p><p><b>Entertainment<\/b> - 42-inch LCD TV, premium channels, and DVD player<\/p><p><b>Food & Drink<\/b> - Mini-fridge, minibar (fees may apply), coffee\/tea maker, and 24-hour room service<\/p><p><b>Sleep<\/b> - Blackout drapes\/curtains, turndown service, and bed sheets <\/p><p><b>Bathroom<\/b> - Private bathroom, shower\/tub combination, bathrobes, and slippers<\/p><p><b>Practical<\/b> - Playpen, safe, and free newspaper; rollaway\/extra beds and free cribs\/infant beds available on request<\/p><p><b>Comfort<\/b> - Air conditioning and daily housekeeping<\/p><p><b>Accessibility<\/b> - Visual fire alarm, height-adjustable showerhead, low-height view port in door, low-height electrical outlets in bathroom, lever door handles, wheelchair accessible, grab bar near toilet, and accessible bathtub<\/p><p><b>Need to Know<\/b> - Shared accommodations<\/p><p>Smoking<\/p><p>Connecting\/adjoining rooms can be requested, subject to availability <\/p>, images=[https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/8081ca82_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/54128439_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/29b094b6_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/10d4b087_z.jpg, https:\/\/i.travelapi.com\/hotels\/5000000\/4720000\/4718600\/4718588\/dea3738f_z.jpg], roomKey=213618194))\n","rooms_count":"1"}

#                 req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookHotel']=True

#             if temp==3 and option=='Hotel':
#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 c=random.choice([{"search_query":"Dubai,United Arab Emirates","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"دبي, الإمارات العربية المتحدة","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"غازي آباد، غازي آباد، الهند","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"}])
                
#                 req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 c=random.choice([{"id":"15026","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/dubai-arabian-ranches-golf-club-15026","title":"Arabian Ranches Golf Club","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/com.almtaar.model.accommodation.Image@cd5748e","price":"331.48","description":"With a stay at Arabian Ranches Golf Club in Arabian Ranches, you'll be close to Arabian Ranches Golf Club and Dubai Autodrome","categoryid1":"Dubai, Arabian Ranches Emirates Road Po Box 367","star":"2","adults_count":"1","children_count":"0","reviews":"5","rooms_count":"1","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"1"},
#                                  {"id":"27058","link":"https:\/\/almatar.com\/ar\/hotels\/rooms\/new-delhi-maidens-hotel-delhi-27058","title":"Maidens Hotel Delhi","price":"679.05","description":"With a stay at Maidens Hotel, Delhi in New Delhi, you'll be in the historical district and convenient to St","categoryid1":"New Delhi, 7 Sham Nath Marg","star":"5","adults_count":"1","children_count":"0","reviews":"4.5","rooms_count":"1","check_in_date":"05\/24\/2023","check_out_date":"05\/23\/2023","number_of_nights":"1"}])

#                 req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))

#                 check_in=date.strftime('%d %B %Y')
#                 check_out=date1.strftime('%d %B %Y')
#                 c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"40897.64","id":"467310","hotel_name":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","hotel_rate":"4.0","room_class":"Room(adultsCount=3, availabitily=null, kidsAges=[2, 2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=2, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\nRoom(adultsCount=2, availabitily=null, kidsAges=[2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=1, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\n","rooms_count":"2"}

#                 req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookHotel']=True

#                 check_in=date.strftime('%d %B %Y')
#                 # check_out=date1.strftime('%d %B %Y')
#                 c={"check_in_date":check_in}
#                 req = adjust_events(app_data,device_data,event_token='suzh64',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 # app_data['bookHotel']=True

#                 c={"Destination_City":"Jeddah,Yanbu,Sokhna Port,Safaga,Aqaba","No_Of_Nights":"7","Package_Name":"Saudi Cruise Red Sea 2023"}
#                 # c={"check_in_date":check_in}
#                 req = adjust_events(app_data,device_data,event_token='hu7p5b',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookHotel']=True

#                 c={"Destination_City":"باكو,قوبا,باكو","No_Of_Nights":"5","Package_Name":"دعنا نكتشف أذربيجان "}
#                 # c={"check_in_date":check_in}
#                 req = adjust_events(app_data,device_data,event_token='hu7p5b',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookHotel']=True
            
#             ###################------Flight Booking--------##############

#             if temp==1 and option=="Flight":

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)

#                 departure_date=date.strftime('%Y-%m-%d')

#                 c={"from_location":"AUH","to_location":"DXB","departure_date":departure_date,"adults_count":"1","children_count":"0","infants_count":"0"}
#                 req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookFlight']=True

#             if temp==2 and option=="Flight":

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)

#                 departure_date=date.strftime('%Y-%m-%d')

#                 c={"from_location":"JLR","to_location":"DEL","departure_date":departure_date,"adults_count":"2","children_count":"0","infants_count":"0"}
#                 req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookFlight']=True

#             if temp==3 and option=="Flight":

#                 req = adjust_events(app_data,device_data,event_token='3juby2')
#                 util.execute_request(**req)

#                 departure_date=date.strftime('%Y-%m-%d')

#                 c={"from_location":"CAI","to_location":"DXB","departure_date":departure_date,"adults_count":"1","children_count":"0","infants_count":"0"}
#                 req = adjust_events(app_data,device_data,event_token='30ls2a',callback=c,patner=c)
#                 util.execute_request(**req)
#                 time.sleep(random.randint(1,5))
#                 app_data['bookFlight']=True

#         possibility = [True]*8 + [False]*92
#         random.shuffle(possibility)
#         if random.choice(possibility) and app_data.get('bookFlight'):
#             c={'id':str(uuid.uuid4())}
#             req= adjust_events( app_data, device_data,event_token='cqhbj3',callback=c,patner=c)
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))
#             req= adjust_events( app_data, device_data,event_token='ck5jzb',callback=c,patner=c)
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))
#             req= adjust_events( app_data, device_data,event_token='bup4hx',callback=c,patner=c)
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))
        

#     if app_data.get('bookHotel'):
#         possibility = [True]*8 + [False]*92
#         random.shuffle(possibility)
#         if random.choice(possibility):


#             today=datetime.now()
#             date=today+timedelta(1)
#             check_in_date=date.strftime('%m/%d/%Y')
#             date1=date+timedelta(1)
#             check_out_date=date1.strftime('%m/%d/%Y')

#             req= adjust_events(app_data, device_data,event_token='x1ox7d')
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))

#             req = adjust_events(app_data,device_data,event_token='3juby2')
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))

#             c=random.choice([{"search_query":"Dubai,United Arab Emirates","check_in_date":check_in_date,"check_out_date":check_out_date,"rooms_count":"1"},{"search_query":"دبي, الإمارات العربية المتحدة","check_in_date":"05\/02\/2023","check_out_date":"05\/03\/2023","rooms_count":"1"}])

#             req = adjust_events(app_data,device_data,event_token='l3eknk',callback=c,patner=c)
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))

#             req = adjust_events(app_data,device_data,event_token='3juby2')
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))

#             c={"id":"467310","link":"https:\/\/almatar.com\/en\/hotels\/rooms\/riyadh-doubletree-by-hilton-hotel-riyadh-al-muroj-business-gate-467310","title":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","image_link":"https:\/\/az712897.vo.msecnd.net\/images\/full\/","price":"40897.64","description":"Centrally located in Riyadh, DoubleTree by Hilton Hotel Riyadh - Al Muroj Business Gate is convenient to Hayat Mall and Sahara Mall","categoryid1":"Riyadh, The Northern Ring Road Exit 5. Next To The Upcoming King Abdullah Financial District","star":"4","adults_count":"5","children_count":"3","reviews":"4","rooms_count":"2","check_in_date":check_in_date,"check_out_date":check_out_date,"number_of_nights":"7"}

#             req = adjust_events(app_data,device_data,event_token='jppvja',callback=c,patner=c)
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))

#             check_in=date.strftime('%d %B %Y')
#             check_out=date1.strftime('%d %B %Y')
#             c={"currency":"SAR","check_in_date":check_in,"check_out_date":check_out,"price":"40897.64","id":"467310","hotel_name":"DoubleTree by Hilton Hotel Riyadh Al Muroj Business Gate","hotel_rate":"4.0","room_class":"Room(adultsCount=3, availabitily=null, kidsAges=[2, 2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=2, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\nRoom(adultsCount=2, availabitily=null, kidsAges=[2], currency=null, finalPrice=0.0, roomBasis=Room only, roomView=, roomName=Royal suite, roomSize=null, bedType=, roomClass=, numOfChildren=1, roomType=, roomContent=RoomContent(amenities={}, description=, images=[], roomKey=))\n","rooms_count":"2"}

#             req = adjust_events(app_data,device_data,event_token='40faqo',callback=c,patner=c)
#             util.execute_request(**req)
#             time.sleep(random.randint(1,5))





#     return {'status':True}

# #==================================================================================================================================================================================


# def adjust_session( app_data, device_data):

#     url='https://'+adjust_data.get('url')+'/session'
    
#     httpmethod='post'

#     app_data['session_started']=int(time.time())

#     if not app_data.get('session_count'):
#         app_data['session_count'] = 1
#     else:
#         app_data['session_count'] +=1
    
#     headers={
#             'Client-SDK':campaign_data.get('adjust').get('sdk'),
#             'Content-Type':'application/x-www-form-urlencoded',
#             'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
#             'Accept-Encoding':'gzip'
#     }

#     params={}

#     data={
#         'android_uuid':app_data.get('android_uuid'),
#         'api_level':device_data.get('sdk'),
#         'app_token':campaign_data.get('adjust').get('app_token'),
#         'app_version':campaign_data.get('app_version_name'),
#         'attribution_deeplink':1,
#         'connectivity_type':1,
#         # 'country':device_data.get('locale').get('country'),
#         'cpu_type':device_data.get('cpu'),
#         'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#         'device_manufacturer':device_data.get('manufacturer'),
#         'device_name':device_data.get('model'),
#         'device_type':device_data.get('device_type'),
#         'display_height':device_data.get('resolution').split('x')[-2],
#         'display_width':device_data.get('resolution').split('x')[-1],
#         'environment':'production',
#         'event_buffering_enabled':0,
#         # 'fb_id':app_data.get('fb_id'),
#         'gps_adid':device_data.get('adid'),
#         'gps_adid_src':'service',
#         "gps_adid_attempt": 1,
#         'hardware_name':device_data.get('hardware'),
#         'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#         'language':device_data.get('locale').get('language'),
#         'needs_response_details':1,
#         'network_type':0,
#         'os_build':device_data.get('build'),
#         'os_name':'android',
#         # "mcc":int(device_data.get('mcc')),
#         # "mnc":int(device_data.get('mnc')),
#         'os_version':device_data.get('os_version'),
#         'package_name':campaign_data.get('package_name'),
#         'screen_density':get_screen_density(device_data),
#         'screen_format':get_screen_format(device_data),
#         'screen_size':'normal',
#         'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#         'session_count':app_data.get('session_count'),
#         'tracking_enabled':1,
#         "ui_mode"  :    "1",
#         'updated_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#         # "vm_isa":device_data.get('cpu')[:-4]
#     }

#     if session_data.get('vm_isa'):
#         data['vm_isa'] = device_data.get('cpu')[:-4]
#     if session_data.get('app_secret'):
#         data['app_secret'] = session_data.get('app_secret')
    
#     if session_data.get('ui_mode'):
#         data['ui_mode'] = 1
#     if session_data.get('fb_id'):
#         data['fb_id'] = app_data.get('fb_id')



#     if app_data.get('pushtoken'):
#         data['push_token'] = app_data.get('pushtoken')
#     app_data['subsession']=1
#     if campaign_data.get('adjust').get('app_secret'):
#         headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'session')

#     return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

# #====================================================================================

# def adjust_sdk_click(app_data,device_data):

#     url='https://'+adjust_data.get('url')+'/sdk_click'
#     httpmethod='post'
#     app_data['session_started']=int(time.time())
#     headers={
#             'Client-SDK': campaign_data.get('adjust').get('sdk'),
#             'Content-Type':'application/x-www-form-urlencoded',
#             'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
#         'Accept-Encoding':'gzip',

#     }

#     params={}

    
#     data={
#             'android_uuid':app_data.get('android_uuid'),
#             'api_level':device_data.get('sdk'),
#             'app_token':campaign_data.get('adjust').get('app_token'),
#             'app_version':campaign_data.get('app_version_name'),
#             'attribution_deeplink':1,
#             'connectivity_type':1,
#             # "mcc":int(device_data.get('mcc')),
#             # "mnc":int(device_data.get('mnc')),
#             'click_time':        datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
#             "click_time_server": datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
#             # 'country':device_data.get('locale').get('country'),
#             'cpu_type':device_data.get('cpu'),
#             'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#             'device_manufacturer':device_data.get('manufacturer'),
#             'device_name':device_data.get('model'),
#             'device_type':device_data.get('device_type'),
#             'display_height':device_data.get('resolution').split('x')[-2],
#             'display_width':device_data.get('resolution').split('x')[-1],
#             'environment':'production',
#             'event_buffering_enabled':0,
#             'google_play_instant':0,
#             'gps_adid_attempt':1,
#             # 'fb_id':app_data.get('fb_id'),
#             'gps_adid':device_data.get('adid'),
#             'gps_adid_src':'service',
#             'hardware_name':device_data.get('hardware'),
#             'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#             "install_begin_time":datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
#             "install_begin_time_server":    datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
#             'install_version':campaign_data.get('app_version_name'),
#             'language':device_data.get('locale').get('language'),
#             'needs_response_details':1,
#             'network_type':0,
#             'os_build':device_data.get('build'),
#             'os_name':'android',
#             'os_version':device_data.get('os_version'),
#             'package_name':campaign_data.get('package_name'),
#             'referrer':app_data.get('referrer') or 'utm_source=(not%20set)&utm_medium=(not%20set)',
#             'referrer_api':'google',
#             'screen_density':get_screen_density(device_data),
#             'screen_format':get_screen_format(device_data),
#             'screen_size':'normal',
#             'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#             'session_count':app_data.get('session_count'),
#             'session_length':int(time.time())- app_data.get('session_started'),
#             'source':'install_referrer',
#             'subsession_count':subsession(app_data),
#             'time_spent':time_spent(app_data),
#             'tracking_enabled':1,
#             "ui_mode"  :    "1",
#             'updated_at': datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone') or None,
#             # "vm_isa":device_data.get('cpu')[:-4]
#     }

#     if sdk_click_data.get('vm_isa'):
#         data['vm_isa'] = device_data.get('cpu')[:-4]
#     if sdk_click_data.get('app_secret'):
#         data['app_secret'] = sdk_click_data.get('app_secret')
    
#     if sdk_click_data.get('ui_mode'):
#         data['ui_mode'] = 1
#     if sdk_click_data.get('install_version'):
#         data['install_version'] = sdk_click_data.get('install_version')



#     if sdk_click_data.get('click_time'):
#         data['click_time'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

#     if sdk_click_data.get('click_time_server'):
#         data['click_time_server'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

#     if sdk_click_data.get('install_begin_time'):
#         data['install_begin_time'] = datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone')
#     if sdk_click_data.get('install_begin_time_server'):
#         data['install_begin_time_server'] =datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),

            
#     if sdk_click_data.get('fb_id'):
#         data['fb_id'] = app_data.get('fb_id')

#     if sdk_click_data.get('install_version'):
#         data['install_version'] = sdk_click_data.get('install_version')

#     if sdk_click_data.get('install_version'):
#         data['install_version'] = sdk_click_data.get('install_version')

#     if sdk_click_data.get('referrer_api'):
#         data['referrer_api'] = sdk_click_data.get('referrer_api')

#     if app_data.get('pushtoken'):
#         data['push_token'] = app_data.get('pushtoken')
#     if campaign_data.get('adjust').get('app_secret'):
#         headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'sdk_click')

#     # data['click_time_server'] = datetime.utcfromtimestamp(int(app_data.get('times').get('click_time')) +  timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
#     # data['install_begin_time_server'] = datetime.utcfromtimestamp((app_data.get('times').get('download_begin_time')+app_data.get('sec')) + timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
#     return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

# #==================================================================================

# def adjust_attribution(app_data,device_data,initiated_by=None):

#     url='https://'+adjust_data.get('url')+'/attribution'

#     httpmethod='get'

#     headers={
#         'Client-SDK':campaign_data.get('adjust').get('sdk'),
#         'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
#         'Accept-Encoding':'gzip',
#     }

#     params={
#             'android_uuid':app_data.get('android_uuid'),
#             'api_level':device_data.get('sdk'),
#             'app_token':campaign_data.get('adjust').get('app_token'),
#             'app_version':campaign_data.get('app_version_name'),
#             # 'app_secret':campaign_data.get('adjust').get('app_secret'),
#             'attribution_deeplink':1,
#             'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#             'device_name':device_data.get('model'),
#             'device_type':device_data.get('device_type'),
#             'environment':'production',
#             'event_buffering_enabled':0,
#             'gps_adid':device_data.get('adid'),
#             'gps_adid_src':'service',     
#             'gps_adid_attempt':1,
#             # 'fb_id':app_data.get('fb_id'),
#             'initiated_by':'backend',
#             'needs_response_details':1,
#             'os_name':'android',
#             'os_version':device_data.get('os_version'),
#             'package_name':campaign_data.get('package_name'),
#             'tracking_enabled':1,
#             # 'secret_id':'2',
#             "ui_mode"  :    "1",
#             'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#             # 'session_count':app_data.get('session_count'),
#     }

#     if atribution_data.get('app_secret'):
#         params['app_secret'] = atribution_data.get('app_secret')
#     if atribution_data.get('secret_id'):
#         params['secret_id'] = atribution_data.get('secret_id')
#     if atribution_data.get('initiated_by'):
#         params['initiated_by'] = atribution_data.get('initiated_by')
#     if atribution_data.get('ui_mode'):
#         params['ui_mode'] = 1
#     if app_data.get('pushtoken'):
#         params['push_token'] = app_data.get('pushtoken')



#     data=None
#     if campaign_data.get('adjust').get('app_secret'):
#         headers['Authorization'] = get_auth(params.get('created_at'),params.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'attribution')
#     return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


# #====================================================================================
# def adjust_sdk_info(app_data,device_data):

#     url='https://'+adjust_data.get('url')+'/sdk_info'

#     httpmethod='post'
#     pushtoken(app_data)
#     headers={
#         'Client-SDK':campaign_data.get('adjust').get('sdk'),
#         'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
#         'Accept-Encoding':'gzip',
#     }

#     data={
#             # 'android_uuid':app_data.get('android_uuid'),
#             'app_token':campaign_data.get('adjust').get('app_token'),
#             'attribution_deeplink':1,
#             'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#             'environment':'production',
#             'event_buffering_enabled':0,
#             'gps_adid':device_data.get('adid'),
#             # 'gps_adid_src':'service',  
#             # 'gps_xadid_attempt':1,
#             'needs_response_details':1,
#             "push_token":app_data.get('pushtoken'),
#             "source":"push",
#             'tracking_enabled':1,
#             'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#     }
#     # if adjust_data.get('sdk_info'):
#     #   if sdk_info_data.get('android_uuid'):
#     #       data['android_uuid'] = app_data.get('android_uuid')
#     #   if sdk_info_data.get('gps_adid_attempt'):
#     #       data['gps_adid_attempt'] = sdk_info_data.get('gps_adid_attempt')
#     #   if sdk_info_data.get('gps_xadid_attempt'):
#     #       data['gps_xadid_attempt'] = sdk_info_data.get('gps_xadid_attempt')





#     params=None
#     if campaign_data.get('adjust').get('app_secret'):
#         headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'sdk_info')
    
#     return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}





# #========================================================================================================================================================================


# def adjust_events(app_data,device_data,event_token=None,callback = None,patner= None):

#     url='https://'+adjust_data.get('url')+'/event'

#     httpmethod='post'

#     headers={
#             'Client-SDK':campaign_data.get('adjust').get('sdk'),
#             'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Accept-Encoding':'gzip',    
#     }

#     params=None

    
#     if not app_data.get('event_count'):
#         app_data['event_count']=1
#     else:
#         app_data['event_count']=app_data['event_count']+1

#     # print(app_data)

#     data={
#         'android_uuid':app_data.get('android_uuid'),
#         'api_level':device_data.get('sdk'),
#         'app_token':campaign_data.get('adjust').get('app_token'),
#         'app_version':campaign_data.get('app_version_name'),
#         'attribution_deeplink':1,
#         'connectivity_type':1,
#         "queue_size":   1,
#         # 'country':device_data.get('locale').get('country'),
#         'cpu_type':device_data.get('cpu'),
#         'callback_params':json.dumps(callback),
#         'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#         'device_manufacturer':device_data.get('manufacturer'),
#         'device_name':device_data.get('model'),
#         'device_type':device_data.get('device_type'),
#         'display_height':device_data.get('resolution').split('x')[-2],
#         'display_width':device_data.get('resolution').split('x')[-1],
#         'environment':'production',
#         'event_buffering_enabled':0,
#         'event_count':app_data.get('event_count'),
#         'event_token':event_token,
#         'gps_adid':device_data.get('adid'),
#         'gps_adid_attempt':'1',
#         'gps_adid_src':'service',
#         # "mcc":int(device_data.get('mcc')),
#         # "mnc":int(device_data.get('mnc')),
#         # 'fb_id':app_data.get('fb_id'),
#         'hardware_name':device_data.get('hardware'),
#         'language':device_data.get('locale').get('language'),
#         'needs_response_details':1,
#         'network_type':0,
#         'os_build':device_data.get('build'),
#         'os_name':'android',
#         'os_version':device_data.get('os_version'),
#         'package_name':campaign_data.get('package_name'),
#         'partner_params' : patner,
#         # 'push_token' : push_token,
#         # "partner_params":partner_params,
#         'screen_density':get_screen_density(device_data),
#         'screen_format':get_screen_format(device_data),
#         'session_count':app_data.get('session_count'),
#         'session_length':int(time.time())-app_data.get('session_started'),
#         'subsession_count':subsession(app_data),
#         'screen_size':'normal',
#         'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
#         'time_spent':time_spent(app_data),
#         'tracking_enabled':1,
#         'ui_mode'   :'1',
#         #  "vm_isa":device_data.get('cpu')[:-4]

#     }


#     if event_data.get('vm_isa'):
#         data['vm_isa'] = device_data.get('cpu')[:-4]
#     if event_data.get('app_secret'):
#         data['app_secret'] = event_data.get('app_secret')
    
#     if event_data.get('ui_mode'):
#         data['ui_mode'] = 1
#     if event_data.get('fb_id'):
#         data['fb_id'] = app_data.get('fb_id')


#     if app_data.get('pushtoken'):
#         data['push_token'] = app_data.get('pushtoken')

#     if callback:
#         data['callback_params'] = json.dumps(callback)
#     if patner:
#         data['partner_params'] = json.dumps(patner)

#     if campaign_data.get('adjust').get('app_secret'):
#         headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'event')
#     return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


# #============================================================================================

# def get_auth(created_at,activity_kind, app_secret,gps_adid , source =''):
#     string = created_at+activity_kind+source+app_secret+gps_adid
#     sign = hashlib.sha256(string).hexdigest()
#     if source:
#         return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid source app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)
#     return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)



# def time_spent(app_data):
#     if not app_data.get('time_spent'):
#         app_data['time_spent'] = str(0)
#     else:
#         app_data['time_spent'] = int(app_data.get('time_spent')) + (int(time.time()) - app_data.get('session_started'))

#     return app_data.get('time_spent')

# def subsession(app_data):
#     possibility = [True]*30+[False]*70
#     random.shuffle(possibility)
#     if random.choice(possibility):
#         if not app_data.get('subsession'):
#             app_data['subsession']=1
#         else:
#             app_data['subsession']+=1
#     return app_data.get('subsession')

# def get_screen_density(device_data):
#     dpi = int(device_data.get('dpi'))
#     if dpi >= 320:
#         return 'high'
#     elif dpi >= 180:
#         return 'medium'
#     else:
#         return 'low'
        
# def get_screen_format(device_data):
#     resolution = device_data.get('resolution')
#     b = resolution.split('x')
#     c = float(b[1])/float(b[0])
#     if c >= 1.77:
#         return 'long'
#     else:
#         return 'normal'

# def pushtoken(app_data):
#     if not app_data.get('pushtoken'):
#         app_data['pushtoken']=util.get_random_string('hex',64)


# def get_country():
#     weighted_choices = campaign_data['country'] if campaign_data.get('country') else ('USA', 4)
#     country_list = [val for val, cnt in weighted_choices for i in range(cnt)]
#     return random.choice(country_list)

# def get_retention(day):
#     return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0

# def click(device_data=None, camp_type='market', camp_plat = 'android'):

#     package_name = campaign_data.get('package_name')
#     serial        = device_data.get('serial')
#     agent_id      = Config.AGENTID
#     random_number = random.randint(1,10)
#     source_id     = ""
#     if random_number < 5:
#         source_id = "728"
#     elif random_number < 8:
#         source_id = "517"
#     elif random_number < 9:
#         source_id = "604"
#     else:
#         source_id = "386"
#     st = device_data.get("device_id", str(int(time.time()*1000)))
#     link = campaign_data['link']
#     link = link.format(dp2=st,agent=agent_id,source=source_id,device_serial=serial,gaid=device_data.get('adid'))
#     return clicker.click(link, device_data, camp_type, camp_plat, 'url=', package_name)

# #######################################################################################



#     