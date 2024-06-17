#=====================================================================
# ＳＥＬＦＢＯＴNEW 2023 BY DHENZA15
#=====================================================================
from linepy import *
import calculators
from calculators.apself import ApCalculator
from justgood import imjustgood
from random import randint
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from akad.ttypes import TalkException
import time, random, json, codecs, subprocess, re,urllib.request,urllib.error,urllib.parse, os, shutil, requests, timeit, ast, pytz, threading, atexit, traceback, base64, pafy, livejson, timeago, math, argparse
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from gtts import gTTS
from multiprocessing import Pool, Process
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime
from googletrans import Translator
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from urllib.parse import urlencode, quote
from pathlib import Path
_session = requests.session()
requests.packages.urllib3.disable_warnings()

#=====================================
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
Bot_startTime = time.strftime("%H:%M:%S", time.localtime())
dhenzaSelf = LINE("itsmeboyzs2@gmail.com","Franky123*")
print("""
\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Start Bot ]\033[0m    
"""%(Bot_startTime))  
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m
███████████████████████████████████
	
▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█  ╭BOT TYPE -  SELFBOT V.3
░▒█░░ █▀▀ █▄▄█ █░▀░█  ╠URL - github.com/dhenza1415
░▒█░░ ▀▀▀ ▀░░▀ ▀░░░▀  ╠SOURCE LIB - PYPI/LINEPY
█████████ ██████ ████ ╰TEAM - TBP SILENTKILLER
▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀       █████████████████
▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
▒█▄▄█ ▒█▄▄▄█ ░▒█░░    ⏤͟͟͞͞SELFBOT NEW BY DHENZA𐂄

▒█▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ 
▒█▄▄█ █▄▄▀ █░░█ ░░█░░ █▀▀ █░░ ░░█░░ 
▒█░░░ ▀░▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ 

███████████████████████████████████
.....----------:/++oosssyyyyyyso+/:---:::::::::--:
..-----.:+oydmmNNNNNNNNNNNMMMMMMMMMNdyo/--:::::::/
.-----/shddmmmmmNNNNNNNNNNMMMMMMMMMMMMMMNh+::::///
-----osyhddmmmmmNNNNNNNNNNMMMMMMMMMMMMMMMMMm/-/+/+
----+ssyhdddmmmNNNNNNNNNNNMMMMMMMMMMMMMMMMMMN//+so
:-.:sso+/:::://+ohmNNNNNNNNNNNNmddhysyhmNMMMNh:++o
-../s/.`.....``-/+o+hmNNNNNmdsoo+:::://::sNNMN/+o+
..`++..:++++::-..`.ssodNNmo:..:/oydNMMMNms/NNNs+oo
.``o++yddmmmmmho::/yhmmNNNms+osdNNNMMMMMMMmmNNd/+o
.``ssyhhdhssyhhdds:`-dNNMNs/ymNNmddmdmNNNNNNNNm+oo
.``ssyhh//::---:/o+:-sNMMMNNdhyo+//+osshNNNNNNNooo
.``ys+o:++/:---:/+ososNMMMMNdy/-.````./mdmmmMMmooo
...ysydmdhhhddmmmNNdssNMMMMMMMNNNNNNNNNNNNNNNNmyos
.`.sdmmNNNNNNNNNNNmhsyNMMMMMMMMMMMMMMMMMMMMMNNNh+o
.`-yhmmmmmmmNNNNNNdhyhNMMMMMMMMMMMMMMMMMMMMMMNNhos
.`.yyhhdddmmmmmmdddhsdNMMMMMMMMNNMMMNNNNNNNMNNNhos
```ysoossssso++oohdyshNNMMMMMMMNhyhdmNNNNNNNNNNs+o
.``+s/+/-++oydmhso-:o+oyyhdy+yNMMMmdysssyhdmNNm/+o
```-o:/s/.smmmmdhys+``.--.odmNMMMMMMMm/.shmNNNy-:/
````++o+s+`/hdhyyyo`  :h+``.omNMMMNmo`-hdmNNNN/::/
````-/+s+os-.``````./hmNNh:.```..```:ymdNNNmNh:/+/
`````//+s+/oyhddhyossooosssssdNNNNNNNdmNNmmmN/:::/
```  `+//os++++osssyhdmmNNNNNNmmdmmddNMNmmmNo///++
.``````/+/+hs+osso++/-``../osssmNNmmNNmmmNm+://///
..``````.///yhoshdmmNm- `/NNNNNNNmNMNmmmms///+++//
.`````    .::+dhshmNNm. `-MMMMNNNNNmmNdo-:://+++++
.``````     `-/ydydmNd` ``NMMMMNNNmmy/.-----::////
``````        `-+oshmd`  :NNNNNNmh+..-:---.-::::::
````` ``        `-/oyd: `dNNNNdo-`.-::::---::::::-
`````````         `.-//-yhys+-``.-::::::::::::::::
`````` `             ` ```````..--:::-------------
███████████████████████████████████
Login Time %s \033[0m\n\n"""%(Bot_startTime))
print ("LOGIN SB SUCSES")
dhenzaMid = dhenzaSelf.profile.mid
dhenzaStart = time.time()
dhenzaPoll = OEPoll(dhenzaSelf)
oburl = dhenzaSelf.server.LINE_OBJECT_URL
call = dhenzaSelf
owner = ["ub1c5a71f27b863896e9d44bea857d35b"]
admin = [dhenzaMid, "ub1c5a71f27b863896e9d44bea857d35b"]
Bots = [dhenzaMid]
JoinedGroups = dhenzaSelf.getGroupIdsJoined()

msg_dict = {}
offbot = []
targets = []
settingsOpen = codecs.open("setting.json","r","utf-8")
settings = json.load(settingsOpen)


read={
    "readPoint":{},
    "readMember":{},
    "ROM":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if settings["autoRestart"] == True:
        if time.time() - botStart > int(settings["timeRestart"]):
            backupData()
            restartBot()
            
def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
 #   if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Err :\n {error}'.format(error=error))       
        
def waktu(self,secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]
#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]    
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items
    
def linkqr(to,her):
    url =pyqrcode.create(her, error='L', version=8, mode='binary')
    url.png("big-number.png",scale=8) 
    dhenzaSelf.sendImage(to,"big-number.png")  
    
def sq(to, text):
	url = "https://api.chstore.me/line2secondary?appname=line_appname&authtoken=auth_token"
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	dhenzaSelf.sendMessage(response.text)
          
          
def sendFlex(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1602687308-GXq4Vvk9', context = xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    return requests.post(url, headers=headers, data=json.dumps(data))
    
def sendFlex(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
    
def sendTemplate(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1602687308-GXq4Vvk9', context = xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)
    
def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': dhenzaSelf.authToken,
        'X-Line-Application': dhenzaSelf.server.APP_NAME,
        'X-Line-ChannelId': '1602687308',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

def sendFooter(receiver, text):
    label = settings["label"]
    icon = settings["iconUrl"]
    link = settings["linkUrl"]
    data = {
        "type": "text",
        "text": text,
        "sentBy": {
            "label": "{}".format(label),
            "iconUrl": "{}".format(icon),
            "linkUrl": "{}".format(link)
        }
    }
    sendTemplate(receiver, data)   
    
    
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hai ".format(str(mid))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = dhenzaSelf.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["welcomee"]#+"\nDigroup: "+str(ginfo.name)+"\n"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(dhenzaSelf.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        dhenzaSelf.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dhenzaSelf.sendMessage(to, "[ INFO ] Error :\n" + str(error))   
    
        
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    dhenzaSelf.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text
    
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output dhenza.mp3 {}'.format(link))
    try:
        dhenzaSelf.sendAudio(to, 'dhenza.mp3')
        time.sleep(2)
        os.remove('dhenza.mp3')
    except Exception as e:
        dhenzaSelf.sendReplyMessage(msg.id, to,'「 ERROR 」\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output dhenza.mp4 {}'.format(link))
    try:
        dhenzaSelf.sendVideo(to, "dhenza.mp4")
        time.sleep(2)
        os.remove('dhenza.mp4')
    except Exception as e:
        dhenzaSelf.sendReplyMessage(msg.id, to,' 「 ERROR 」\nMungkin Link Nya Salah cek lagi', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+dhenzaSelf.getContact(dhenzaMid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~teambotprotect'})
   
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = dhenzaSelf.genOBSParams({'oid': dhenzaMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = dhenzaSelf.server.postContent('{}/talk/vp/upload.nhn'.format(str(dhenzaSelf.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        dhenzaSelf.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("dhenza.mp4")        
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + cmd) + 1
    return text[rmv:]        
    
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            silentk1ller = pesan.replace(settings["keyCommand"],"")
        else:
            silentk1ller = "Undefined command"
    else:
        silentk1ller = text.lower()
    return silentk1ller
    
def dhenzaBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                dhenzaSelf.findAndAddContactsByMid(op.param1)
            dhenzaSelf.sendMention(op.param1, settings["autoAddMessage"], [op.param1])
        if op.type == 13 or op.type == 124:
            if settings["autoJoin"] and dhenzaMid in op.param3:
                group = dhenzaSelf.getGroup(op.param1)
                group.notificationDisabled = False
                dhenzaSelf.acceptGroupInvitation(op.param1)
                dhenzaSelf.sendMessage(op.param1, "THAKS FOR INVITE ME SILENTKILLER")                   
#=====================================================================        
        if op.type == 13 or op.type == 124:
            if op.param2 in settings["blackList"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blackList"][op.param2] = True                    
                    try:
                        dhenzaSelf.cancelGroupInvitation(op.param1,[op.param3])
                        dhenzaSelf.kickoutFromGroup(op.param1, [op.param2])
                    except:
                    	pass
#=====================================================================
        if op.type == 17 or op.type == 130:
            if op.param2 in settings["blackList"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blackList"][op.param2] = True                    
                    try:
                        dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#=====================================================================
        if op.type == 19 or op.type == 133:
            if op.param2 in settings["blackList"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blackList"][op.param2] = True                    
                    try:
                        dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
        if op.type == 19 or op.type == 133:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        settings["blackList"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.findAndAddContactsByMid(op.param3)
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                            dhenzaSelf.acceptGroupInvitation(op.param1)
                        except:
                            pass
                    return
                if op.param3 in admin:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        settings["blackList"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.findAndAddContactsByMid(op.param3)
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                            dhenzaSelf.acceptGroupInvitation(op.param1)
                        except:
                            pass
                    return
                if op.param3 in Bots:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        settings["blackList"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.findAndAddContactsByMid(op.param3)
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                            dhenzaSelf.acceptGroupInvitation(op.param1)
                        except:
                            pass
                    return
        
#====================================================================
        if op.type == 17 or op.type == 130:
            if op.param1 in settings["welcomee"]:
                ginfo = dhenzaSelf.getGroup(op.param1)
                contact = dhenzaSelf.getContact(op.param2)
                cover = dhenzaSelf.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                gname = dhenzaSelf.getGroup(op.param1)
                data = {"type": "flex","altText": "FLEX WELCOME","contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/2c0Qrtw/ezgif-com-gif-maker-1.png",
            "size": "full",
            "gravity": "top",
            "aspectMode": "cover",
            "offsetTop": "0px",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), 
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "2px",
            "paddingAll": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(op.param2).pictureStatus),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "0px",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetEnd": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Hallo Welcome Selamat bergabung",
                    "size": "xxs",
                    "wrap": True,
                    "align": "center",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "60px",
            "paddingAll": "2px",
            "offsetStart": "10px",
            "offsetEnd": "10px",
            "borderWidth": "semi-bold",
            "borderColor": "#00000022"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(dhenzaSelf.getContact(op.param2).displayName),
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff",
                    "align": "center"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "30px",
            "paddingAll": "2px",
            "offsetEnd": "50px",
            "paddingEnd": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(cover),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetBottom": "3px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/LNYb0f0/ezgif-com-gif-maker.png",
                    "aspectMode": "cover",
                    "aspectRatio": "10:2",
                    "animated": True
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "2px",
            "offsetEnd": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "ɬც℘ ʂıƖɛŋɬƙıƖƖɛཞ",
                    "color": "#ffffff",
                    "size": "sm",
                    "position": "relative"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "30px",
            "offsetEnd": "5px"
          }
        ],
        "margin": "sm",
        "backgroundColor": "#000000",
        "paddingAll": "0px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://www.dhenza15.site/"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      }
    }
  ]
}
}
                dhenzaSelf.postTemplate(op.param1, data)                                                   

        if op.type == 15 or op.type == 128:
            if op.param1 in settings["welcomee"]:
                ginfo = dhenzaSelf.getGroup(op.param1)
                contact = dhenzaSelf.getContact(op.param2)
                cover = dhenzaSelf.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                gname = dhenzaSelf.getGroup(op.param1)
                data = {"type": "flex","altText": "FLEX LEAVE","contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/2c0Qrtw/ezgif-com-gif-maker-1.png",
            "size": "full",
            "gravity": "top",
            "aspectMode": "cover",
            "offsetTop": "0px",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), 
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "2px",
            "paddingAll": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(op.param2).pictureStatus),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "0px",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetEnd": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "yaah kok leave si kk...",
                    "size": "xxs",
                    "wrap": True,
                    "align": "center",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "60px",
            "paddingAll": "2px",
            "offsetStart": "10px",
            "offsetEnd": "10px",
            "borderWidth": "semi-bold",
            "borderColor": "#00000022"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(dhenzaSelf.getContact(op.param2).displayName),
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff",
                    "align": "center"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "30px",
            "paddingAll": "2px",
            "offsetEnd": "50px",
            "paddingEnd": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(cover),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetBottom": "3px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/LNYb0f0/ezgif-com-gif-maker.png",
                    "aspectMode": "cover",
                    "aspectRatio": "10:2",
                    "animated": True
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "2px",
            "offsetEnd": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "ɬც℘ ʂıƖɛŋɬƙıƖƖɛཞ",
                    "color": "#ffffff",
                    "size": "sm",
                    "position": "relative"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "30px",
            "offsetEnd": "5px"
          }
        ],
        "margin": "sm",
        "backgroundColor": "#000000",
        "paddingAll": "0px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://www.dhenza15.site/"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      }
    }
  ]
}
}
                dhenzaSelf.postTemplate(op.param1, data)
                
        
#=====================================================================          
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)       
#=====================================================================
        if op.type == 55:
            if op.param2 in settings["blackList"]:
                dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass                                
#=====================================================================
        if op.type == 55:
          if settings['cyduk'][op.param1] == True:
            if op.param1 in cctv['point']:
                    Name = dhenzaSelf.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n• " + Name
                        contact = dhenzaSelf.getContact(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        contact = dhenzaSelf.getContact(op.param2)
                        KATA = ["hallo kk sini gabung chat","hay ngitip mulu","up yuk","ngopi atu ka","hallo sayang","cek pm ka","buka filter","hayo ngintip"]
                        TAG = "@! "
                        TAG += random.choice(KATA)
                        dhenzaSelf.sendMention2(op.param1, str(TAG),' ',[op.param2])
#=====================================================================                        
        if op.type in [26, 25]:
            if op.type == 26: print ("[26] RECEIVE MESSAGE")
            else: print ("[25] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            silentk1ller = command(text)
            to = receiver
            if settings["Danger"] == True:
            	if msg._from not in Bots or msg._from not in admin or msg._from not in owner:
                    if msg.text in [".js","!js",".sikat","!sikat","sikat","Bubar",".bubar","!bubar",".cipok","!cupok","Cleanse","!cleanse",".cleanse","Kickall","!kickall",".kickall","mayhem","Ratakan","bubarkan","Nuke","nuke",".nuke","Bypass","bypass",".bypass","hancurkan","!malam",".fuck",".malam"]:
                        dhenzaSelf.kickoutFromGroup(receiver,[sender])
                        dhenzaSelf.sendMessage(receiver, "sorri  sya kick jangan usil ya mau JS room") 
# MEDIA NEW BATAS  •••••••••••••••••••••••••••   
                    elif 'https://vt.tiktok.com/' in silentk1ller:
                      #    if settings["tiktok"] == True:
                            try:
                                spilt = msg.text.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                sm = {"write":""}
                                date = sm["write"] = c.lcd
                                dz = sm["write"]
                                hasil = int(dz)
                                masuk = txt[hasil]
                                url = requests.get("https://api.chstore.me/tiktok?url={}".format(masuk))
                                data = url.text
                                main = json.loads(data)
                                dhenzaSelf.sendVideoWithURL(to, main["result"]["mp4"])
                            except Exception as error:
                                print(error)
                    elif "https://youtu.be/" in silentk1ller:
          #                if settings["yt"] == True:
                            try:
                                spilt = msg.text.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                sm = {"write":""}
                                date = sm["write"] = c.lcd
                                dz = sm["write"]
                                hasil = int(dz)
                                aturan = txt[hasil]
                                url = requests.get("https://api.chstore.me/youtube?url={}".format(aturan))
                                main = url.text
                                main = json.loads(main)
                                sk = "WAIT DONLOAD YT \n\n"
                                sk += "DURATION : {}\n".format(main["result"]["duration"])
                                sk += "TITLE : {}".format(main["result"]["title"])
                                dhenzaSelf.sendReplyMessage(msg.id,to, "{}".format(sk)) 
                                dhenzaSelf.sendVideoWithURL(to, main["result"]["mp4"])
                            except Exception as error:
                                print(error)
                                
                    elif 'https://www.smule.com/' in silentk1ller or 'https://www.smule.com/sing-recording' in silentk1ller:
                      #    if settings["smule"] == True:
                            try:
                                spilt = msg.text.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                sm = {"write":""}
                                date = sm["write"] = c.lcd
                                dz = sm["write"]
                                hasil = int(dz)
                                masuk = txt[hasil]
                                url = requests.get("https://api.chstore.me/smule/post?url={}".format(masuk))
                                xx = url.text
                                res = json.loads(xx)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                contact = dhenzaSelf.getProfile()
                                mids = [contact.mid]
                                status = dhenzaSelf.getContact(sender)                               	
                                cover = dhenzaSelf.getProfileCoverURL(sender)
                                ID = "ID : {}".format(res["result"]["owner"]["handle"])
                                LIKE = "LIKE : {}".format(res["result"]["stats"]["total_loves"])
                                LISTEN = "LISTENS : {}".format(res["result"]["stats"]["total_listens"])
                                COMMENT = "COMMENT : {}".format(res["result"]["stats"]["total_comments"])
                                TITLE = "{}".format(res["result"]["title"])
                                PICT = "{}".format(res["result"]["cover_url"])
                                sk = "WAITING DONLOAD FILE\n\n"
                                sk += "\n {}".format(ID)
                                sk += "\n {}".format(LIKE)
                                sk += "\n {}".format(LISTEN)
                                sk += "\n {}".format(COMMENT)
                                sk += "\n {}".format(TITLE)
                                dhenzaSelf.sendReplyMessage(msg.id,to, str(sk))
                                if res["result"]["type"] == "audio":
                                    dhenzaSelf.sendAudioWithURL(to, "{}".format(res["result"]["media_url"]))
                                else:
                                    dhenzaSelf.sendVideoWithURL(to, "{}".format(res["result"]["video_media_url"]))
                            except Exception as error:
                                print(error)  
                                
#===================BAGIAN TOKEN =====================================================
        if op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                silentk1ller = command(text)
                for silentk1ller in silentk1ller.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != dhenzaSelf.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                            if silentk1ller == "help" or silentk1ller == "sb":
                        #    if msg._from in admin or msg._from in owner:
                                contact = dhenzaSelf.getProfile()
                                mids = [contact.mid]
                                status = dhenzaSelf.getContact(sender)             
                                md = "╭──「 𝖒𝖊𝖓𝖚 𝖘𝖇 」"
                                md+="\n⦚๛ Media [chat owner]"
                                md+="\n⦚๛ Liff"
                                md+="\n⦚๛ Logout"                                
                                md+="\n⦚๛ Reset"
                                md+="\n⦚๛ Runtime"
                                md+="\n⦚๛ "+settings["mentionall"]
                                md+="\n⦚๛ Settagall [cmd]"
                                md+="\n⦚๛ cgrupname: [cmd]"
                                md+="\n⦚๛ cpict"
                                md+="\n⦚๛ cpv"
                                md+="\n⦚๛ cgrupict"
                                md+="\n⦚๛ changename: [cmd]"
                                md+="\n⦚๛ cdual"
                                md+="\n⦚๛ cppurl [link ytb]"
                                md+="\n⦚๛ changebio: [txt]"
                                md+="\n⦚๛ welcome on/off"
                                md+="\n⦚๛ tarik [jumlah]"
                                md+="\n⦚๛ speed"
                                md+="\n⦚๛ open/close [qr]"
                                md+="\n⦚๛ url"
                                md+="\n⦚๛ listsmule [id]"
                                md+="\n⦚๛ tube [judul]"
                                md+="\n⦚๛ Sider on/off"
                                md+="\n⦚๛ Broadcast: [txt]"
                                md+="\n⦚─────────"
                                md+="\n╰─๛「 {} 」".format(dhenzaSelf.getProfile().displayName)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                dhenzaSelf.sendMessage(to,md)
                                
                                
                        if silentk1ller == "liff":
                        	if msg._from in dhenzaMid:
                        	  dhenzaSelf.sendMessage(to, "line://app/1602687308-GXq4Vvk9?type=text&text=")
                                
                        if silentk1ller == "logout":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                dhenzaSelf.sendReplyMessage(msg.id, to, "Your selfbot has been logout ")
                                sys.exit("[ INFO ] BOT SHUTDOWN")
                                
                        elif silentk1ller == "reset":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                restart = "ˢᵘᶜˢᵉˢˢ ʳᵉᵇᵒᵒᵗ ˢⁱˢᵗᵉᵐ ᵇᵒᵗ ᶠʳᵉˢʰ"
                                contact = dhenzaSelf.getContact(sender)
                                dhenzaSelf.sendReplyMessage(msg.id, to,restart)
                                restartBot()

                        elif silentk1ller == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - dhenzaStart
                                runtime = timeChange(runtime)
                                run = "Bot telah aktif selama {}".format(str(runtime))
                                dhenzaSelf.sendReplyMessage(msg.id, to, run)
                                
                        elif silentk1ller == settings["mentionall"]:
                                  group = dhenzaSelf.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(dhenzaSelf.getProfile().mid)
                                  dhenzaSelf.datamention(to,'「MENTION MEMBER」',nama)
                                  
                        elif silentk1ller.startswith("settagall "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                settings["mentionall"] = "{}".format(txt)
                                dhenzaSelf.sendReplyMessage(msg_id, to, "Succesfully change Mention member with key >> {}".format(settings["mentionall"]))
                             
                        elif silentk1ller.startswith("cgrupname: "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    groupname = text.replace(sep[0] + " ","")
                                    if len(groupname) <= 100:
                                        group = dhenzaSelf.getGroup(to)
                                        group.name = groupname
                                        dhenzaSelf.updateGroup(group)
                                        dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah nama group menjadi : {}".format(groupname))
                                        
                        elif silentk1ller == "cpict":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                settings["changePictureProfile"] = True
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Silahkan kirim gambarnya")
                        elif silentk1ller == "cpv":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                settings["changeVpProfile"] = True
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Silahkan kirim Videonya")

                        elif silentk1ller == "cgrupict":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Silahkan kirim gambarnya")               
                                    
                        elif silentk1ller.startswith("changename: "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 999:
                                    profile = dhenzaSelf.getProfile()
                                    profile.displayName = name
                                    dhenzaSelf.updateProfile(profile)
                                    dhenzaSelf.sendMessage(to, "Berhasil mengubah nama menjadi : {}".format(name))
                              else:
                                  txt = ("Hmmmm gk bsa ya :(","Sorryy :(","Jgn Ubah Namaku :(")
                                  pop = random.choice(txt)
                                  dhenzaSelf.sendMessage(to, pop)
                                  
                        elif silentk1ller == "cdual":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                settings["changeDual"] = True
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Send Viideo for profile")
                                
                        elif silentk1ller.startswith("cppurl"):
                                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                        link = removeCmd("cppurl", text)
                                        contact = dhenzaSelf.getContact(sender)
                                        dhenzaSelf.sendReplyMessage(msg.id, to," Type: Profile\n • Detail: Change video url\n • Status: Download...")
                                        print("Sedang Mendownload Data")
                                        pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                        subprocess.getoutput('youtube-dl --format mp4 --output dhenza.mp4 {}'.format(link))
                                        pict = dhenzaSelf.downloadFileURL(pic)
                                        vids = "dhenza.mp4"
                                        changeVideoAndPictureProfile(pict, vids)
                                        dhenzaSelf.sendReplyMessage(msg.id, to," Type: Profile\n • Detail: Change video url\n • Status: Succes")
                                        os.remove("dhenza.mp4")

                        elif silentk1ller.startswith("changebio: "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 100000:
                                    profile = dhenzaSelf.getProfile()
                                    profile.statusMessage = bio
                                    dhenzaSelf.updateProfile(profile)
                                    dhenzaSelf.sendMessageWithFooter(to, "Berhasil mengubah bio menjadi : {}".format(bio))              
#on / off                                     
                        elif silentk1ller == "welcome on":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.to in settings["welcomee"]:
                                   dhenzaSelf.sendMessage(to,"「 WELCOME MESSAGE  」")
                                else:
                                	settings["welcomee"][msg.to] = True
                                dhenzaSelf.sendMessage(to,"Baerhasil mengaktifkan Welcome message")
                                
                        elif silentk1ller == "welcome off":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.to not in settings["welcomee"]:
                                   dhenzaSelf.sendMessage(to,"「 WELCOM EMESSAGE 」")
                                else:
                                	del settings["welcomee"][msg.to]
                                dhenzaSelf.sendMessage(to,"Berhasil menonaktifkan Welcome message")
                                
                        elif silentk1ller == "sider on":
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  dhenzaSelf.sendMessage(to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del settings['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              settings['cyduk'][msg.to]=True

                        elif silentk1ller == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  settings['cyduk'][msg.to]=False
                                  dhenzaSelf.sendMessage(to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  dhenzaSelf.sendMessage(to, "Sudak tidak aktif")
#°°°°°°°°°                                    
                        elif silentk1ller.startswith("tarik "):
                          if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                            args = silentk1ller.replace("tarik ","")
                            mes = 0
                            try:
                                mes = int(args[1])
                            except:
                                mes = 1
                            M = dhenzaSelf.getRecentMessagesV2(to, 101)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == dhenzaSelf.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                dhenzaSelf.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.start()
                                thread1.join()
                            dhenzaSelf.sendMessage(msg.to, "Success unsend {} message".format(len(MId)))
      

                        elif silentk1ller == "speed":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                 start = time.time()                               
                                 dhenzaSelf.sendMessage(to, "𝚌𝚑𝚎𝚔𝚒𝚗𝚐 𝚜𝚙𝚎𝚎𝚍 𝚋𝚘𝚝𝚜...")                               
                                 elapsed_time = time.time() - start
                                 dhenzaSelf.sendReplyMessage(msg.id, to,"{} sec".format(str(elapsed_time/100)))
                        elif silentk1ller == "open":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.toType == 2:
                                   X = dhenzaSelf.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   dhenzaSelf.updateGroup(X)
                                   dhenzaSelf.sendReplyMessage(msg.id, to, "ᯓ▹ Url Opened")

                        elif silentk1ller == "close":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                  if msg.toType == 2:
                                     X = dhenzaSelf.getGroup(msg.to)
                                     X.preventedJoinByTicket = True
                                     dhenzaSelf.updateGroup(X)
                                     dhenzaSelf.sendReplyMessage(msg.id, to, "ᯓ▹ Url Closed")

                        elif silentk1ller == "url":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                  if msg.toType == 2:
                                     x = dhenzaSelf.getGroup(msg.to)
                                     if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        dhenzaSelf.updateGroup(x)
                                     gurl = dhenzaSelf.reissueGroupTicket(msg.to)
                                     dhenzaSelf.sendReplyMessage(msg_id, to, "ᯓ▹ Nama : "+str(x.name)+ "\nᯓ▹ Url grup : http://line.me/R/ti/g/"+gurl) 
  
                        elif "https://pin.it/" in silentk1ller:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.pinterest(kata)
                                for x in data["result"]:                               	
                                	dhenzaSelf.sendMessage(to," Tunggu proses downloads √ ")
                                if x["type"] == "png":
                                	dhenzaSelf.sendImageWithURL(to,x["url"])
                                if x["type"] == "jpg":
                                	dhenzaSelf.sendImageWithURL(to,x["url"])
                                if x["type"] == "mp4":
                                     dhenzaSelf.sendVideoWithURL(to,x["url"])
                                if x["type"] == "gif":
                                	dhenzaSelf.sendGIFWithURL(to,x["url"])
                                
                        elif "https://twitter.com/" in silentk1ller:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.twitterdl(kata)
                                main = data['result']
                                result = "╭──[ HASIL PENCARIAN ]"
                                result  += "Caption : {}".format(data["result"]["caption"])
                                result += "\nLike : {}".format(data["result"]["likes"])
                                result += "\nRetweet : {}".format(data["result"]["retweet"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendMessage(to," Tunggu proses downloads √ ")
                                if data["result"]["imageUrl"] != []:
                                	result += "\n\nImage URL : "
                                for a in data["result"]["imageUrl"]:                                	
                                	dhenzaSelf.sendImageWithURL(to,a)
                                if data["result"]["videoUrl"] != None:
                                	dhenzaSelf.sendVideoWithURL(to,data["result"]["videoUrl"])
                                
                        elif "https://fb.watch/" in silentk1ller:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.facebookdl(kata)
                                main = data['result']
                                result = "╭──[ HASIL PENCARIAN ]"
                                result += "Author : {}".format(data["result"]["author"])
                                result += "\nCaption : {}".format(data["result"]["caption"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendMessage(to," Tunggu proses downloads mp4√ ")
                                dhenzaSelf.sendVideoWithURL(to,data["result"]["videoUrl"])       
                                
                        elif "https://linevoom.line.me/" in silentk1ller:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.timeline(kata)
                                dhenzaSelf.sendImageWithURL(to,data["result"]["pictureUrl"])
                                main = data['result']
                                result = "╭──[ DOWNLOAD POST TIMELINE ]"
                                result += "\nDisplay name : {}".format(data["result"]["displayName"])
                                result += "\nLike : {}".format(data["result"]["like"])
                                result += "\nShare : {}".format(data["result"]["share"])
                                result += "\n\nCaption : {}".format(data["result"]["caption"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                if data["result"]["timeline"] != []:
                                	number  = 0
                                result += "\n\nMedia Post :"
                                for a in data["result"]["timeline"]:
                                	number += 1
                                if a["type"] == "image":
                                	dhenzaSelf.sendImageWithURL(to, a["url"])                                
                                if a["type"] == "video":
                                	dhenzaSelf.sendReplyMessage(msg.id,to," Tunggu proses downloads video √ ")
                                	dhenzaSelf.sendVideoWithURL(to,a["url"])
                                
                        elif "https://www.instagram.com/" in silentk1ller:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.instapost(kata)
                                dhenzaSelf.sendImageWithURL(to,data["result"]["picture"])
                                result = "╭──[ HASIL PENCARIAN ]"
                                result += "Username : {}".format(data["result"]["username"])
                                result += "\nFullname : {}".format(data["result"]["fullname"])
                                result += "\nVerified : {}".format(data["result"]["verified"])
                                result += "\nPrivate : {}".format(data["result"]["private"])
                                result += "\nCreated : {}".format(data["result"]["created"])
                                result += "\nCaption : {}".format(data["result"]["caption"])
                                result += "\nLikes : {}".format(data["result"]["likes"])
                                result += "\nComments : {}".format(data["result"]["comments"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                number  = 0
                                result += "\n\nMedia Post"
                                for a in data["result"]["postData"]:
                                	number += 1
                                if a["type"] == "image":
                                	dhenzaSelf.sendImageWithURL(to, a["postUrl"])
                                if a["type"] == "video":
                                	dhenzaSelf.sendReplyMessage(msg.id,to," Tunggu proses downloads video √ ")
                                	dhenzaSelf.sendVideoWithURL(to,a["postUrl"])
                                
                        elif silentk1ller.startswith("smule "): 
                 #             if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.smule(kata)
                                main = data['result']
                                result = "╭──[ HASIL PENCARIAN SMULE ]"
                                result += "\n•Account Id : {}".format(data["result"]["accountId"])
                                result += "\n•Username : {}".format(data["result"]["username"])
                                result += "\n•Fullname : {}".format(data["result"]["fullname"])
                                result += "\n•Biography : {}".format(data["result"]["biography"])
                                result += "\n•Location : {}".format(data["result"]["location"])
                                result += "\n•Followers : {}".format(data["result"]["followers"])
                                result += "\n•Recording : {}".format(data["result"]["recording"])
                                result += "\n•VIP : {}".format(data["result"]["vip"])
                                result += "\n•Verified : {}".format(data["result"]["verified"])
                                result += "\n•Picture URL : {}".format(data["result"]["pictureUrl"])
                                result += "\n•Profile URL : {}".format(data["result"]["profileUrl"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                if data["result"]["post"] != []:
                                	number  = 0
                                result += "\n\nPerformances :"
                                for i in data["result"]["post"]:
                                	number += 1
                                result += "\n  {}. {}".format(number,i["title"])
                                performances  = data["result"]["post"]
                                if performances == []:
                                	result = "Not found"
                                else:
                                	number   = 1
                                main     = performances[number-1]
                                download = api.smuledl(main["pageUrl"])
                                if download["result"]["type"] == "video":
                                	dhenzaSelf.sendVideoWithURL(to,download["result"]["mp4Url"])
                                
                        elif silentk1ller.startswith("lyric "): 
              #                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.lyric(kata)
                                image   = data["result"]["image"]
                                result = "╭─[ HASIL PENCARIAN LYRIC ]"                                
                                result += "\n\n♆Title : {}".format(data["result"]["title"])
                                result += "\n☊Artist : {}".format(data["result"]["artist"])
                                result += "\n🎵Lyric :\n{}".format(data["result"]["lyric"])                           
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendImageWithURL(to,image)
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("cord "): 
                #              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.chord(kata)
                                result = "╭─[ HASIL PENCARIAN CORD ]"                                
                                result += "\n\n{}".format(data["result"]["title"])
                                result += "\n\n{}".format(data["result"]["chord"])                          
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("github "): 
             #                 if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.github(kata)
                                result = "╭─[ HASIL PENCARIAN GITHUB ]"
                                result += "\n⦚ID : {}".format(data["result"]["id"])
                                result += "\n⦚Type : {}".format(data["result"]["type"])
                                result += "\n⦚Username : {}".format(data["result"]["username"])
                                result += "\n⦚Fullname : {}".format(data["result"]["fullname"])
                                result += "\n⦚Blog : {}".format(data["result"]["blog"])
                                result += "\n⦚Email : {}".format(data["result"]["email"])
                                result += "\n⦚Company : {}".format(data["result"]["company"])
                                result += "\n⦚Created : {}".format(data["result"]["created_at"])
                                result += "\n⦚Location : {}".format(data["result"]["location"])
                                result += "\n⦚Repositories : {}".format(data["result"]["repositories"])
                                result += "\n⦚Following : {}".format(data["result"]["following"])
                                result += "\n⦚Profile : {}".format(data["result"]["page"])
                                result += "\n\n╰──[ SILENTKILLER™ ]"                  
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendImageWithURL(to,data["result"]["avatar"])
                                
                        elif silentk1ller.startswith("google image"): 
               #               if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.image(kata)
                                result = "╭─[ WALPAPER HD]"
                                main = data['result']
                                for i in range(len(data["result"])):
                                	result += f"\n{i+1}. {data['result'][i]}"
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendMessage(to,result)
                                result = random.choice(main)
                                dhenzaSelf.sendImageWithURL(to,result)
                                
                        elif silentk1ller.startswith("kbbi "): 
                 #             if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.kbbi(kata)
                                result = data["result"]["desc"]
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("adzan "): 
              #                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.adzan(kata)
                                result = "[ JADWAL ADZAN ]"
                                result  +="\n\n\nInfo Waktu Sholat"
                                result += "\nWilayah : {}".format(data["result"]["wilayah"])
                                result += "\nTanggal : {}".format(data["result"]["tanggal"])
                                result += "\nSubuh : {}".format(data["result"]["adzan"]["subuh"])
                                result += "\nTerbit : {}".format(data["result"]["adzan"]["terbit"])
                                result += "\nDhuha : {}".format(data["result"]["adzan"]["dhuha"])
                                result += "\nDzuhur : {}".format(data["result"]["adzan"]["dzuhur"])
                                result += "\nAshar : {}".format(data["result"]["adzan"]["ashar"])
                                result += "\nMaghrib : {}".format(data["result"]["adzan"]["maghrib"])
                                result += "\nIsya : {}".format(data["result"]["adzan"]["isya"])
                                contact = dhenzaSelf.getProfile()
                                mids = [contact.mid]
                                status = dhenzaSelf.getContact(sender)             
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("walpaper "): 
                #              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.wallpaper(kata)
                                result = "╭─[ WALPAPER HD]"
                                main = data['result']
                                for i in range(len(data["result"])):
                                	result += f"\n{i+1}. {data['result'][i]}"
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                result = random.choice(main)
                                dhenzaSelf.sendImageWithURL(to,result)
                                
                        elif silentk1ller.startswith("bokep "): 
               #               if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.porn(kata)
                                main = data['result']
                                result = "╭─[ BOKEPERS ]"
                                result += "\n⦚Title : {}".format(data["result"]["title"])
                                result += "\n⦚Duration : {}".format(data["result"]["duration"])
                                result += "\n⦚Quality : {}".format(data["result"]["quality"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendVideoWithURL(to,data["result"]["videoUrl"])
                                
                        elif silentk1ller.startswith("fncy "): 
                     #         if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.fancy(kata)
                                main = data['result']
                                result = "╭─[ GAYA TEXT ]"
                                result += "\n⦚FANCY RESULT :\n"
                                for s in data["result"]:
                                	result += "\n⦚{}\n⦚".format(s)
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("gif "): 
              #                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.gif(kata)
                                result = "╭─[ WALPAPER GIF]"
                                main = data['result']
                                for i in range(len(data["result"])):
                                	result += f"\n{i+1}. {data['result'][i]}"
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                result = random.choice(main)
                                dhenzaSelf.sendImageWithURL(to,result)
                                
                        elif silentk1ller.startswith("artimimpi "): 
              #                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.mimpi(kata)
                                result = "╭─[ ARTI MIMPI ]"
                                result += "Arti Mimpi"
                                for a in data["result"]:
                                	result += "\n\nMimpi : {}".format(a["dream"])                                
                                result += "\nArti : {}".format(a["meaning"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendMessage(to,result)
                                
                        elif silentk1ller.startswith("artinama "): 
                 #             if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.nama(kata)
                                result = "╭─[ ARTI NAMA ]"
                                result  += "⦚Nama : {}".format(data["result"]["name"])
                                result += "\n⦚Karakter : {}".format(data["result"]["definition"])
                                result += "\n⦚Deskripsi : {}".format(data["result"]["description"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("wikipedia "): 
            #                  if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.wikipedia(kata)
                                result = "╭─[ HASIL PENCARIAN WIKI ]"                                
                                result += "\n\n⦚{}".format(data["result"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("ascii "): 
            #                  if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.ascii(kata)                                
                                dhenzaSelf.sendReplyMessage(msg.id,to,data)
                                
                        elif silentk1ller.startswith("imagetext "): 
          #                    if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.imagetext(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("ss "): 
           #                   if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.screenshot(kata)
                                dhenzaSelf.sendImageWithURL(to,data["result"]["desktop"])
                                dhenzaSelf.sendImageWithURL(to,data["result"]["mobile"])
                                
                        elif silentk1ller.startswith("hitung "): 
                 #             if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.calc(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("ultah "): 
            #                  if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.lahir(kata)
                                result = "Lahir : {}".format(data["result"]["lahir"])
                                result = "\nHari : {}".format(data["result"]["hari"])
                                result = "\nZodiac : {}".format(data["result"]["zodiak"])
                                result = "\nUltah : {}".format(data["result"]["ultah"])
                                result = "\nUsia : {}".format(data["result"]["usia"])
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("jadian "): 
                   #           if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.jadian(kata)
                                result  = "Date : {}".format(data["result"]["date"])
                                result += "\n\nRelated : {}".format(data["result"]["related"])
                                result += "\n\nDescription : {}".format(data["result"]["description"])
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("quranlist"): 
              #                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                result   = "QUR'AN SURAH :"
                                data     = api.alquran()
                                for qs in data:
                                    result += "\n↝{}".format(qs)
                                dhenzaSelf.sendMessage(to, result)
                                dhenzaSelf.sendReplyMessage(msg.id,to, " gunakan comand:\nquran 「nama surat」")
                                
                        elif silentk1ller.startswith("quran "): 
                 #             if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data     = api.alquranQS(kata)
                                audioUrl = data["result"]["audio"]
                                number   = data["result"]["number"]
                                total    = data["result"]["verse"]
                                meaning  = data["result"]["meaning"]
                                arab     = data["result"]["title"]["ar"]
                                latin    = data["result"]["title"]["id"]
                                place    = data["result"]["place"]
                                desc     = data["result"]["desc"]
                                verse    = data["result"]["verses"]
                                result = "╭──[ HASIL PENCARIAN ]"
                                result += "[QS:{}][{}]\n".format(number,total)
                                result  += "\n↝{}".format(arab)
                                result  += "\n↝{} ( {} )\n".format(latin,meaning)
                                for i in range(len(verse)):
                                	result += "\n↝{}".format(verse[i]["ar"])
                                result += "\n↝{}. {}\n".format(i+1,verse[i]["id"])
                                result  += "\n↝Diturunkan di : {}\n".format(place)
                                result  += "\n↝{}".format(desc)
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                dhenzaSelf.sendAudioWithURL(to, audioUrl)
                                                                
                        elif silentk1ller.startswith("b64endcode "): 
                #              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data     = api.B64Encode(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("b64decode "): 
                  #            if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data     = api.B64Decode(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("binaryendcode "): 
                   #           if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data     = api.BinaryEncode(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("binarydecode "): 
                         #     if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data     = api.BinaryDecode(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("bimbel"): 
                        #      if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.bible()
                                main = data['result']
                                indonesia  = data["result"]["indonesia"] 
                                english    = data["result"]["english"]
                                result     = "RANDOM BIBLE"
                                result    += "\n\n[EN][VER:{}][{}] {}".format(english["version"],english["reference"],english["text"])
                                result    += "\n\n[EN][VER:{}][{}]".format(indonesia["version"],indonesia["reference"],indonesia["text"])              
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("bitly "): 
                      #        if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data     = api.bitly(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                dhenzaSelf.sendReplyMessage(msg.id,to, "Sucses cara add \n conto: bitly 「link」")
                                
                        elif silentk1ller.startswith("bmkg"): 
                      #        if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data    = api.bmkg()
                                result  = "\n ╭╚Info Gempa BMKG╗"
                                result += "\n⦚↝Tanggal : {}".format(data["result"]["tanggal"])
                                result += "\n⦚↝Pukul : {}".format(data["result"]["pukul"])
                                result += "\n⦚↝Lokasi : {}".format(data["result"]["lokasi"])
                                result += "\n⦚↝Wilayah : {}".format(data["result"]["wilayah"])
                                result += "\n⦚↝Kordinat : {}".format(data["result"]["kordinat"])
                                result += "\n⦚↝Kedalaman : {}".format(data["result"]["kedalaman"])
                                result += "\n⦚↝Kekuatan : {}".format(data["result"]["kekuatan"])
                                result += "\n⦚↝Arahan : {}".format(data["result"]["arahan"])
                                result += "\n⦚↝Saran : {}".format(data["result"]["saran"])
                                result += "\n⦚↝Peta Skema : {}".format(data["result"]["skema"])
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("cctv"): 
                     #         if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                result = "\n╭──[ LIST CODE CCTV™ ]"
                                result  += "\n⦚↝132 - Slipi Palmerah"
                                result  += "\n⦚↝133 - Slipi Tomang"
                                result  += "\n⦚↝137 - Hasyim Ashari"
                                result  += "\n⦚↝169 - Asia Afrika Hang Lekir"
                                result  += "\n⦚↝323 - Kalimalang Jatiwaringin Raya"
                                result  += "\n⦚↝331 - Pejompongan Slipi"
                                result  += "\n⦚↝332 - Pejompongan Sudirman"
                                result  += "\n⦚↝334 - Fachrudin Raya"
                                result  += "\n⦚↝334 - Fachrudin Raya"
                                result  += "\n⦚↝342 - Rasuna Said"
                                result  += "\n⦚↝119 - Ancol Ubm"
                                result += "\n╰──[ SILENTKILLER™ ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendReplyMessage(msg.id,to, "comand: \nconto: codecctv 「119」")
                                
                                
                        elif silentk1ller.startswith("codecctv "): 
                      #        if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.cctvSearch(kata)
                                result  = "CAMERA INFO"
                                result += "\nArea : {}".format(data["result"]["area"])
                                result += "\nWilayah : {}".format(data["result"]["wilayah"])
                                result += "\n\n{}".format(data["result"]["camera"])
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                dhenzaSelf.sendVideoWithURL(to,data["result"]["video"])
                                
                        elif silentk1ller.startswith("carihp "): 
                     #         if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data   = api.cellular(kata)
                                number = 0
                                result = "SEARCH RESULT :"
                                for a in data["result"]:
                                	number += 1
                                result += "\n\n{}. {}".format(number,a["brands"])
                                result += "\nRelease : {}".format(a["release"])
                                result += "\nChipset : {}".format(a["chipset"])
                                result += "\nScreen : {}".format(a["screen"])
                                result += "\nBattery : {}".format(a["battery"])
                                result += "\nDisplay : {}".format(a["display"])
                                result += "\nRam : {}".format(a["ram"])
                                result += "\nStorage : {}".format(a["storage"])
                                result += "\nThumbnail : {}".format(a["thumbnail"])
                                result += "\nPage : {}".format(a["pageUrl"])
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                               
                        elif silentk1ller.startswith("checkip "): 
                      #        if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.check_ip(kata)
                                result = "Ip Address : {}".format(data["result"]["ip_address"])
                                for a in data["result"]:
                                	if a != "ip_address" and a != "languages" and data["result"][a] is not None:
                                    	  result += "\n↝{} : {}".format(a.title(),data["result"][a])                                    	
                                languages = "\n↝Language : "
                                for b in data["result"]["languages"]:
                                	languages += "{}, ".format(b)
                                result   += languages[:-2]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("cinema "): 
                  #            if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data  = api.cinema(kata)
                                result      = "Cinema 21"
                                result     += "\n\nCity : {}\n".format(data["result"]["city"])
                                number      = 0
                                for a in data["result"]["data"]:
                                	number += 1
                                result += "\n{}. {}".format(number,a["cinema"])
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                number      = 0
                                select_     = 1
                                cinema      = data["result"]["data"]
                                list_cinema = [o for o in cinema]
                                track       = list_cinema[select_-1]
                                result      = "{}".format(track["cinema"])
                                result     += "\n{}".format(track["address"])
                                result     += "\n\nNow playing :"
                                for a in track["nowPlaying"]:
                                	number += 1
                                result += "\n{}. {}".format(number,a["movie"])
                                result     += "\n\nStudio Image : {}".format(track["studioImage"])
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                number      = 0
                                select_one  = 1
                                select_two  = 1
                                showtime    = ""
                                cinema      = data["result"]["data"]
                                list_cinema = [o for o in cinema]
                                track       = list_cinema[select_one-1]
                                list_track  = [y for y in track["nowPlaying"]]
                                movies      = list_track[select_two-1]
                                for x in movies["showtime"]:
                                	showtime += "{}, ".format(x)
                                result = "╭──[ HASIL PENCARIAN ]"
                                result     += "{}".format(movies["movie"])
                                result     += "\n\n⦚↝Price : {}".format(movies["price"])
                                result     += "\n\n⦚↝Showtime : {}".format(showtime[:-2])
                                result     += "\n\n⦚↝Genre : {}".format(movies["genre"])
                                result     += "\n⦚↝Duration : {}".format(movies["duration"])
                                result     += "\n⦚↝Director : {}".format(movies["director"])
                                result     += "\n⦚↝Actor : {}".format(movies["actor"])
                                result     += "\n\n⦚↝Synopsis :\n{}".format(movies["synopsis"])
                                result     += "\n\⦚↝nPoster : {}".format(movies["poster"])
                                result += "╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("corona"): 
                  #            if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data   = api.corona()
                                result  = "CORONA VIRUS QUICKCOUNT"
                                result = "╭──[ HASIL PENCARIAN ]"
                                result += "SEARCH RESULT :"
                                result += "\n⦚↝{}".format(data["result"]["date"])
                                result += "\n\n⦚↝World"
                                result += "\n⦚↝Case : {}".format(data["result"]["world"]["case"])
                                result += "\n⦚↝Fit : {}".format(data["result"]["world"]["fit"])
                                result += "\n⦚↝Rip : {}".format(data["result"]["world"]["rip"])
                                result += "\n\n⦚↝Indonesia"
                                result += "\n⦚↝Case : {}".format(data["result"]["indonesia"]["case"])
                                result += "\n⦚↝Fit : {}".format(data["result"]["indonesia"]["fit"])
                                result += "\n⦚↝Rip : {}".format(data["result"]["indonesia"]["rip"])
                                result += "╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("cuaca "): 
                   #           if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data   = api.cuaca(kata)
                                result = data["result"]
                                result = "╭──[ HASIL PENCARIAN ]"
                                result  += "{}".format(data["result"]["location"])
                                result += "\n⦚↝Cuaca : {}".format(data["result"]["description"])
                                result += "\n⦚↝Suhu : {}".format(data["result"]["temperature"])
                                result += "\n⦚↝Angin : {}".format(data["result"]["wind"])
                                result += "\n⦚↝Kelembapan : {}".format(data["result"]["humidity"])
                                result += "╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("custumlink "): 
             #                 if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data   = api.cuaca(kata)
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("type kontol"): 
                     #         if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data    = api.dick()
                                result = " [ TYPE K0NTOL ]"
                                result += "\nDick : {}".format(data["result"]["dick"])
                                result += "\n•Size : {}".format(data["result"]["size"])
                                result += "\n•Ability : {}".format(data["result"]["ability"])
                                result += "\n•Flexibility : {}".format(data["result"]["flexibility"])
                                result += "\n•Description : {}".format(data["result"]["description"])
                                contact = dhenzaSelf.getProfile()
                                mids = [contact.mid]
                                status = dhenzaSelf.getContact(sender)
                                data = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "{}".format(data["result"]["picture"]),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "flex": 1
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px",
            "borderColor": "{}".format(setbot["borderColor"]),
            "borderWidth": "medium"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "{}".format(status.displayName),
                    "weight": "bold",
                    "color": "#FF0000"
                  },
                  {
                    "type": "span",
                    "text": "     "
                  }
                ],
                "size": "sm",
                "wrap": True
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text":"{}".format(str(result)),
                    "wrap": True,
                    "size": "xxs",
                    "color": "{}".format(setbot["text"]),
                    "align": "center"
                  }
                ],
                "spacing": "sm",
                "margin": "md",
                "borderWidth": "medium",
                "borderColor": "{}".format(setbot["borderColor"]),
                "paddingStart": "5px"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "position": "absolute"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "{}".format(setbot["borderColor"]),
    "borderWidth": "medium"
  }
}
                                dhenzaSelf.postFlex(to, data)
                                
                        elif silentk1ller.startswith("kamasutra"): 
             #                 if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data    = api.kamasutra()
                         #       dhenzaSelf.sendImageWithURL(to,data["result"]["thumbnail"])
                                result  = "Gaya : {}".format(data["result"]["style"])
                                result += "\nKeterangan :\n{}".format(data["result"]["description"])
                                contact = dhenzaSelf.getProfile()
                                mids = [contact.mid]
                                status = dhenzaSelf.getContact(sender)
                                data = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "{}".format(data["result"]["thumbnail"]),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "flex": 1
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px",
            "borderColor": "{}".format(setbot["borderColor"]),
            "borderWidth": "medium"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "{}".format(status.displayName),
                    "weight": "bold",
                    "color": "#FF0000"
                  },
                  {
                    "type": "span",
                    "text": "     "
                  }
                ],
                "size": "sm",
                "wrap": True
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text":"{}".format(str(result)),
                    "wrap": True,
                    "size": "xxs",
                    "color": "#FF3399",
                    "align": "center"
                  }
                ],
                "spacing": "sm",
                "margin": "md",
                "borderWidth": "medium",
                "borderColor": "{}".format(setbot["borderColor"]),
                "paddingStart": "5px"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "position": "absolute"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "{}".format(setbot["borderColor"]),
    "borderWidth": "medium"
  }
}
                                dhenzaSelf.postFlex(to, data)
                              
                                
                        elif silentk1ller.startswith("loker"): 
                       #       if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data        = api.karir()
                                result      = "Info Lowongan Kerja"
                                number = 0
                                for a in data["result"]:
                                	number += 1
                                result = "╭──[ HASIL PENCARIAN ]"
                                result += "\n\n{}. {}".format(number,a["perusahaan"])
                                result += "\nLokasi : {}".format(a["lokasi"])
                                result += "\nBagian : {}".format(a["bagian"])
                                result += "\nJabatan : {}".format(a["jabatan"])
                                result += "\nGaji : {}".format(a["gaji"])
                                result += "\nPendidikan : {}".format(a["pendidikan"])
                                result += "\nSyarat : {}".format(a["syarat"])
                                result += "\nDeskirpsi : {}".format(a["deskripsi"])
                                result += "\nSumber : {}".format(a["sumber"])
                                result += "╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("lineapp"): 
                  #            if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data   = api.lineapp()
                                result = "LINE APP VERSION"
                                for a in data["result"]:
                                	result += "\n↝{} : {}".format(a,data["result"][a])
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("tokohkartun "): 
                    #          if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.mangaSearch(kata)
                                dhenzaSelf.sendImageWithURL(to,data["result"]["thumbnail"])
                                result = "╭──[ HASIL PENCARIAN ]"
                                result += "{}".format(data["result"]["title"])
                                result += "\n⦚↝Author : {}".format(data["result"]["author"])
                                result += "\n⦚↝Genre : {}".format(data["result"]["genre"])
                                result += "\n⦚↝Rating : {}".format(data["result"]["rating"])
                                result += "\n⦚↝Release : {}".format(data["result"]["release"])
                                result += "\n⦚↝Status : {}".format(data["result"]["status"])
                                result += "\n⦚↝Type : {}".format(data["result"]["type"])
                                result += "\n⦚↝Update : {}".format(data["result"]["updated"])
                                result += "\n\n⦚↝Synopsis :\n{}".format(data["result"]["synopsis"])
                                result += "╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("tokohfilm "): 
                    #          if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.movie(kata)
                                dhenzaSelf.sendImageWithURL(to,data["result"]["poster"])
                                result  = "Title : {}".format(data["result"]["title"])
                                result += "\n⦚↝Duration : {}".format(data["result"]["runtime"])
                                result += "\n⦚↝Year : {}".format(data["result"]["year"])
                                result += "\n⦚↝Release : {}".format(data["result"]["release"])
                                result += "\n⦚↝DVD : {}".format(data["result"]["dvd"])
                                result += "\n⦚↝genre : {}".format(data["result"]["genre"])
                                result += "\n⦚↝Production : {}".format(data["result"]["production"])
                                result += "\n⦚↝Director : {}".format(data["result"]["director"])
                                result += "\n⦚↝Actors : {}".format(data["result"]["actors"])
                                result += "\n⦚↝Awards : {}".format(data["result"]["awards"])
                                result += "\n\n⦚↝Synopsis :\n{}".format(data["result"]["synopsis"])
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                

                        elif silentk1ller.startswith("cari "): 
               #               if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.search(kata)
                                number = 0
                                result = "╭〣GOOGLE SEARCH RESULT :"
                                for s in data["result"]:
                                	number += 1
                                result += "\n↝{}. {}".format(number,s["title"])
                                result += "\n↝{}".format(s["snippet"])
                                result += "\n↝{}".format(s["url"])
                                result += "\n╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                
                        elif silentk1ller.startswith("quots"): 
                   #           if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                api     = imjustgood("imjustgood")
                                data   = api.movie_quotes()
                                result = data["result"]
                                dhenzaSelf.sendReplyMessage(msg.id,to, result)
                                
                        elif silentk1ller.startswith("cariytmp3 "):
                        #      if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.youtube(kata)
                                main = data['result']
                                result  = "Title : {}".format(data["result"]["title"])
                                result += "\n╭↝Author : {}".format(data["result"]["author"])
                                result += "\n⦚↝Duration : {}".format(data["result"]["duration"])
                                result += "\n⦚↝Watched : {}".format(data["result"]["watched"])
                                result += "\n\n╰↝Thumbnail :\n{}".format(data["result"]["thumbnail"])
                             #   result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendAudioWithURL(to,data["result"]["videoUrl"])
                                
                        elif silentk1ller.startswith("cariytmp4 "): 
                     #         if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.youtube(kata)
                                result = "╭──[ HASIL PENCARIAN ]"
                                main += data['result']
                                result  = "Title : {}".format(data["result"]["title"])
                                result += "\n↝Author : {}".format(data["result"]["author"])
                                result += "\n↝Duration : {}".format(data["result"]["duration"])
                                result += "\n↝Watched : {}".format(data["result"]["watched"])
                                result += "\n\n↝Thumbnail :\n{}".format(data["result"]["thumbnail"])
                             #   result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])
                                result += "╰──[ HASIL PENCARIAN ]"
                                dhenzaSelf.sendReplyMessage(msg.id,to,result)
                                dhenzaSelf.sendVideoWithURL(to,data["result"]["videoUrl"])
                                
                        elif silentk1ller.startswith(".joox "): 
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.joox(kata)
                                main = data['result']
                                dz1 = dhenzaSelf.getContact(dhenzaMid)
                                dz2 = dhenzaSelf.getContact(sender)                   
                        #        result = "╭──[ HASIL PENCARIAN ]"
                        #        result += "\n⦚Penyanyi : {}".format(data["result"]["singer"])
                         #       result += "\n⦚Title : {}".format(data["result"]["title"])
                          #      result += "\n⦚Duration : {}".format(data["result"]["duration"])
                      #          result += "\n⦚Size : {}".format(data["result"]["size"])
                          #      result += "\n╰──[ SILENTKILLER™ ]"
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/D5vJvmF/20220305-011928.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "5:10",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/09wr5fy/ezgif-com-gif-maker-4.pnghttps://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://github.com/dhenza1415/"
                },
                "animated": True,
                "size": "xs"
              }
            ],
            "position": "absolute",
            "width": "27px",
            "height": "27px",
            "cornerRadius": "100px",
            "offsetTop": "265px",
            "offsetStart": "0px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}" . format(data["result"]["title"]),
                "size": "xxs",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "alignItems": "center",
            "offsetTop": "266px",
            "offsetStart": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "{}".format(data["result"]["thumbnail"]),
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://github.com/dhenza1415/"
                },
                "animated": True
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "270px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text":"{}" . format(data["result"]["singer"]),
                "size": "xxs",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "alignItems": "center",
            "offsetTop": "275px",
            "offsetStart": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://github.com/dhenza1415/"
                },
                "animated": True,
                "size": "xs",
                "offsetEnd": "12px"
              }
            ],
            "position": "absolute",
            "offsetTop": "177px",
            "offsetStart": "8px",
            "width": "50px",
            "height": "50px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
                                dhenzaSelf.sendFlex(to,data)
                        #        dhenzaSelf.sendMessage(to,result)
                                dhenzaSelf.sendAudioWithURL(to,main["mp3Url"])
                                
                                
                        elif silentk1ller.startswith(". "): 
                                x = msg.text.split(" ")
                                y = msg.text.replace(x[0] + " ","")
                                api     = imjustgood("imjustgood")
                                kata = y
                                data    = api.simisimi(kata)
                                result = data["result"]
                                dhenzaSelf.sendMessage(to,result)                                         
#=========================================     
                        elif silentk1ller.startswith("yt3"):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp3,args=(to,txt,))
                                treding.daemon = True
                                treding.start()

                        elif silentk1ller.startswith("yt4"):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp4,args=(to,txt,))
                                treding.daemon = True
                                treding.start()
                                
                        elif silentk1ller.startswith("listsmule "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://smule.com/{}/performances/json".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["list"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["list"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "size": "micro",
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "#000000",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#000000",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "{}".format(music['cover_url']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=sticker&stk=noanim&sid=32128231&pkg=3099312"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/7J1FWPc/ei-1624349250118-removebg-preview.png",
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "title",
                                                        "color": "#FF0000",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['title'],
                                                        "color": "#00FF00",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 1,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 1,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "🎬",
                                                            "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                     }, {
                                                        "flex": 1,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "🎬",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=.smuleaudio%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                    }]
                                                },
                                                {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "🎬",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=.smulevideo%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append("https://smule.com/{}/{}".format(str(search), str(music["web_url"])))
                                    k = len(ret_)//5
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Search Smule Resorting",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*5 : (aa+1)*5]
                                            }
                                        }
                                        dhenzaSelf.postTemplate(to, data)
                                        
                        elif silentk1ller.startswith("tube "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyApzHZ18jUd3BdkhL_xcwAI_zxqwb9fuy4".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                    #        "size": "micro",
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "{}".format(setbot["backgroundColor"]),
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "{}".format(setbot["backgroundColor"]),
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "2:1",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=ua797021910f0584e11be56d4a6fa74ed"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/nCwKXJg/ezgif-com-gif-maker-6.png",
                                                        "animated": True,
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "judul Video",
                                                        "color": "#FF0000",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#00FF00",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 2,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 3,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 0,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                     }, {
                                                        "flex": 2,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=yt3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                    }]
                                                },
                                                {
                                                    "type": "button",
                                                    "margin": "xs",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp4",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=yt4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        dhenzaSelf.postTemplate(to, data)
                                                                               
#COMAND HELPER ======================
                        elif silentk1ller == "media" or silentk1ller == "help media":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                profile = dhenzaSelf.getProfile()
                                md = "╭───「 Media Message」"
                                md+="\n├ Name : "+ str(profile.displayName)
                                md+="\n├ Command bots"
                                md+="\n┝─────────────╮"
                                md+="\n├๛ cari 「kata」"
                                md+="\n├๛ cctv "
                                md+="\n├๛ kodecctv「no」"
                                md+="\n├๛ quots"
                                md+="\n├๛ bmkg"
                                md+="\n├๛ hentai"
                                md+="\n├๛ loker"
                                md+="\n├๛ lineapp"
                                md+="\n├๛ quranlis"
                                md+="\n├๛ quran「nama surat」"
                                md+="\n├๛ b64endcode「text」"
                                md+="\n├๛ b64decode「text」"
                                md+="\n├๛ binaryendcode「txt」"
                                md+="\n├๛ binarydecode「txt」"
                                md+="\n├๛ bimbel「txt」"
                                md+="\n├๛ bitly「situs web」"
                                md+="\n├๛ carihp「merek」"
                                md+="\n├๛ checkip「server」"
                                md+="\n├๛ cinema「kota」"
                                md+="\n├๛ corona "
                                md+="\n├๛ cuaca「kota」"
                                md+="\n├๛ custumlink「nama,link」"
                                md+="\n├๛ type kontol"
                                md+="\n├๛ kamasutra"
                                md+="\n├๛ tokohkartun 「naruto」 "
                                md+="\n├๛ tokohfilm 「avenger」"
                                md+="\n├๛ asmaulhusna「no」"
                                md+="\n├๛ al-qur'an 「no」"
                                md+="\n├๛ murrotal"
                                md+="\n├๛ ayat sajadah"
                                md+="\n├๛ cariytmp3「text」"
                                md+="\n├๛ cariytmp4「text」"
                                md+="\n├๛ .joox 「text」 "
                                md+="\n├๛ smule 「id」"
                                md+="\n├๛ listsmule 「id」"
                                md+="\n├๛ lyric 「text」"
                                md+="\n├๛ cord 「text」"
                                md+="\n├๛ github 「id」"
                                md+="\n├๛ google image「text」"
                                md+="\n├๛ gif 「text」"
                                md+="\n├๛ artinama 「kata」"
                                md+="\n├๛ artimimpi 「kata」"
                                md+="\n├๛ yt3 「link」"
                                md+="\n├๛ yt4 「link」"
                                md+="\n├๛ tube 「kata」"
                                md+="\n├๛ kbbi 「kata」"
                                md+="\n├๛ adzan 「kota」"
                                md+="\n├๛ wikipedia 「text」"
                                md+="\n├๛ ascii 「text」"
                                md+="\n├๛ imagetext 「text」"
                                md+="\n├๛ ss 「link」"
                                md+="\n├๛ hitung 「2+2」"
                                md+="\n├๛ ultah 「14-02-1991」"
                                md+="\n├๛ jadian 「14-02-1991」"
                                md+="\n├๛ bokep 「text」"
                                md+="\n├๛ fancy 「text」"
                                md+="\n├────────────╮"
                                md+="\n├๛ Menu donlod via share link"
                                md+="\n├๛ share link 「smule」"
                                md+="\n├๛ share link 「youtube」"
                                md+="\n├๛ share link 「pintertest」"
                                md+="\n├๛ share link 「tiktok」"
                                md+="\n├๛ share link 「tweeter」"
                                md+="\n├๛ share link 「instagram」"
                                md+="\n├๛ share link 「timeline」"
                                md+="\n├๛ share link 「facebook」"
                                md+="\n├────────────╯"
                                md+="\nKHUSUS MEDIA AKAN BERJALAN JIKA ADA APIKEY \n bisa pesan chat owner 👇 \n http://line.me/ti/p/~teambotprotect"
                                md+="\n╰─๛User:「 {} 」".format(dhenzaSelf.getProfile().displayName)
                                dhenzaSelf.sendReplyMessage(msg.id,to, md)
                       
                        elif silentk1ller.startswith("broadcast: "):
                            if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = dhenzaSelf.getGroupIdsJoined()
                               groups = dhenzaSelf.getGroupIdsJoined()
                               contacts = dhenzaSelf.getAllContactIds()
                               contact = dhenzaSelf.getProfile()
                               mids = [contact.mid]
                               status = dhenzaSelf.getContact(sender)
                               for group in saya:
                                   dhenzaSelf.sendMessage(group, pesan)
                         
#==================================================
        
#==================================================                                
                        elif msg.contentType == 2:
                            if settings["changeDual"] == True:
                                def cvp():
                                    dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/cvp.mp4")
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Send Pict :)")
                                td = Thread(target=cvp)
                                td.daemon = True
                                td.start()

                        elif msg.contentType == 1:
                            if settings["changeDual"] == True:
                                def change():
                                    pict = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changeDual"] = False
                                    dhenzaSelf.updateVideoAndPictureProfile(pict, "LineAPI/tmp/cvp.mp4")
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Succesfully change video & picture profile")
                                    dhenzaSelf.deleteFile(pict)
                                    dhenzaSelf.deleteFile("LineAPI/tmp/cvp.mp4")
                                td = Thread(target=change)
                                td.daemon = True
                                td.start()
                            
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if settings["addImage"]["status"] == True:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-add.bin".format(str(settings["addImage"]["name"])))
                                    images[settings["addImage"]["name"]] = {"IMAGE":str(path)}
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    dhenzaSelf.sendMessage(msg.to, "Succesfully add Image With Keyword {}".format(str(settings["addImage"]["name"])))
                                    settings["addImage"]["status"] = False                
                                    settings["addImage"]["name"] = ""
                             
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["changePictureProfile"] == True:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changePictureProfile"] = False
                                    dhenzaSelf.updateProfilePicture(path)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah foto profile")
                                    dhenzaSelf.deleteFile(path)
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if to in settings["changeGroupPicture"]:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
                                    settings["changeGroupPicture"].remove(to)
                                    dhenzaSelf.updateGroupPicture(to, path)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah foto group")
                                    dhenzaSelf.deleteFile(path)
                            if msg.toType == 2:
                                if settings["changeCover"] == True:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cv.bin".format(time.time()))
                                    settings["changeCover"] = False
                                    dhenzaSelf.updateProfileCover(path)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah cover profile")
                                    dhenzaSelf.deleteFile(path)
                        elif msg.contentType == 2:
                            if settings["changeVpProfile"] == True:
                                path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cvp.mp4".format(time.time()))
                                settings["changeVpProfile"] = False
                                changeVideoAndPictureProfile(path)
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah video profile")
                                dhenzaSelf.deleteFile(path)
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)
#======================================================
        
#============================================
def runningProgram():
    while True:
        try:
            ops = dhenzaPoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('[ SYSTEM MESSAGE : *KEYBOARD INTERRUPT.')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                dhenzaBot(op)
                dhenzaPoll.setRevision(op.revision)

if __name__ == '__main__':
    print (' [•] SYSTEM MESSAGE : *BOT BERHASIL DI INSTALL\n______________________________\n')
    print (' \n*klik my chanel https://youtube.com/@silentkillerofficial4992\n______________________________\n')
    runningProgram()