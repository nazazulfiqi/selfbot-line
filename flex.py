#=====================================================================
# ＳＥＬＦＢＯＴ
#=====================================================================
from linepy import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from akad.ttypes import TalkException
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
#from gtts import gTTS
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests as uReq
from datetime import datetime
from googletrans import Translator
from zalgo_text import zalgo
import ast, codecs, json, os, pytz, re, LineService, random, sys, time, urllib.parse, subprocess, threading, pyqrcode, pafy, humanize, os.path, traceback
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
_session = requests.session()
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()
#======================================
client = LINE()
clientMid = client.profile.mid
clientStart = time.time()
clientPoll = OEPoll(client)
owner = ["ube7e5b15dbea0cc92f2067c04d25b1fc"]
admin = [clientMid]
Bots = [clientMid]
languageOpen = codecs.open("language.json","r","utf-8")
mentioOpen = codecs.open("tagme.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("setting.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
#adminOpen = codecs.open("admin.json","r","utf-8")
stickerOpen = codecs.open("sticker.json","r","utf-8")
stickertOpen = codecs.open("stickertemplate.json","r","utf-8")
textaddOpen = codecs.open("text.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
waitOpen = codecs.open("wait.json","r","utf-8")
answeOpen = codecs.open("autoanswer.json","r","utf-8")

language = json.load(languageOpen)
tagme = json.load(mentioOpen)
read = json.load(readOpen)
settings = json.load(settingsOpen)
#owner = json.load(ownerOpen)
unsend = json.load(unsendOpen)
stickers = json.load(stickerOpen)
stickerstemplate = json.load(stickertOpen)
textsadd = json.load(textaddOpen)
images = json.load(imagesOpen)
wait = json.load(waitOpen)
autoanswer = json.load(answeOpen)

pendings = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
offbot = []
temp_flood = {}
msg_dict = {}
msg_dict1 = {}  
unsendchat = {}
msg_image={}
msg_video={}
msg_sticker={}
msg_waktu={}
ssnd = []
rynk = {
    "myProfile": {
        "displayName": "",
    }
}
RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}
kasar = "kontol","memek","kntl","ajg","anjing","asw","anju","gblk","goblok","bgsd","bangsad","bangsat"

wait = {
    "cekpc": "Pm ku gosong semm??",
}
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
            
def sendTemplate(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1647207293-rNJ7MlJm', context = xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            client.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        client.sendMessage(to, 'Apalo !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','client.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        client.sendMessage(to, 'Apalo !')

def logError(text):
    client.log("[ PEOPLE ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def waktu(self,secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

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

def searchRecentMessages(to,id):
    for a in client.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None
    
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

def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah

def footerText(to, textnya):
    data = {
        "messages": [
            {
                "type": "text",
                "text": textnya,
                "sentBy": {
                    "label": "「ＳＥＬＦＢＯＴ」",
                    "url": "https://media.giphy.com/media/JSjyKthOO1v6NsoiEs/giphy.gif",
                    "linkUrl": "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc"
                }
            }
        ]
    }
    sendTemplate(to, data)

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost

def sendTextTemplatey(to, text):
    warna1 = ("#0008FF","#000000","#058700","#DE00D4","#05092A","#310206","#5300FC")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "ＳＥＬＦＢＯＴ",
            "contents": {
                                 "styles": {
                                   "body": {
                                     "backgroundColor": warnanya1
                                   },
                                   "footer": {
                                     "backgroundColor": "#FF0000"
                                   }
                                 },
                                 "type": "bubble",
                                 "body": {
                                   "contents": [
                                     {
                                       "contents": [
                                         {
                                           "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
                                           "type": "image"
                                         },
                                         {
                                           "type": "separator",
                                           "color": "#FF0A00"
                                         },
                                         {
                                           "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                           "type": "image"
                                         }
                                       ],
                                       "type": "box",
                                       "spacing": "md",
                                       "layout": "horizontal"
                                     },
                                     {
                                       "type": "separator",
                                       "color": "#FF0009"
                                     },
                                     {
                                       "contents": [
                                         {
                                           "contents": [
                                             {
                                               "text": text,
                                               "size": "xs",
                                               "margin": "none",
                                               "color": "#FFFFFF",
                                               "wrap": True,
                                               "weight": "regular",
                                               "type": "text"
                                             }
                                           ],
                                           "type": "box",
                                           "layout": "baseline"
                                         }
                                       ],
                                       "type": "box",
                                       "layout": "vertical"
                                     }
                                   ],
                                   "type": "box",
                                   "spacing": "md",
                                   "layout": "vertical"
                                 },
                                 "footer": {
                                   "contents": [
                                     {
                                       "contents": [
                                         {
                                           "contents": [
                                             {
                                               "text": "ＳＥＬＦＢＯＴ",
                                               "size": "md",
                                               "weight": "bold",
                                               "action": {
                                                 "uri": "https://line.me/R/ti/p/%40137gcwpz",
                                                 "type": "uri",
                                                 "label": "Audio"
                                                },
                                               "margin": "sm",
                                               "align": "center",
                                               "color": "#000000",
                                               "weight": "bold",
                                               "type": "text"
                                             }
                                           ],
                                           "type": "box",
                                           "layout": "baseline"
                                         }
                                       ],
                                       "type": "box",
                                       "layout": "horizontal"
                                     }
                                   ],
                                   "type": "box",
                                  "layout": "vertical"
                                 }
                               }
                               }
    client.postTemplate(to, data)

def sendTextTemplate11(to, text):
    data = {
            "type": "flex",
            "altText": "ＳＥＬＦＢＯＴ",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000",
      "separator":True,
      "separatorColor":"#FF0000"
    },
    "footer": {
      "backgroundColor": "#000000",
      "separator":True,
      "separatorColor":"#FF0000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [          
          {
            "type": "image",            
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
           "type": "image",
        "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif", #hp
        "size": "xl",
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
       },
       {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "sm",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＣＲＥＡＴＯＲ",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }]
      }]
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate17(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(client.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFFFF",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    },
    "header": {
      "backgroundColor": "#FFFFFF"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#000000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＡＤＭＩＮ",
                  "uri": "http://line.me/ti/p/~zza503"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#000000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＣＲＥＡＴＯＲ",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }]
      }]
  }
}
}
    client.postTemplate(to, data)                

def sendTextTemplate8(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} send Message".format(client.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFFFF",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#FF0000"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/jq5LZCvhx4b3H5R1RW/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#006400",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＡＤＭＩＮ",
                  "uri": "http://line.me/ti/p/~zza503"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＣＲＥＡＴＯＲ",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }]
      }]
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate(to, text):
    warna1 = ("#0008FF","#FF0000","#058700","#DE00D4","#05092A","#310206","#5300FC")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "ＳＥＬＦＢＯＴ",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "ＳＥＬＦＢＯＴ",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ＳＥＬＦＢＯＴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎶SOUNDCLOUD🎶",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "ＳＥＬＦＢＯＴ",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    client.postTemplate(to, data)

def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "ＳＥＬＦＢＯＴ",
            "contents": {
                                 "type": "bubble",
                                 "styles":{
                                 "header":{
                                 "backgroundColor":"#000000"
                                },
                                "body":{
                                 "backgroundColor":"#000000",
                                 "separator":True,
                                 "separatorColor":"#FF0500"
                                },
                                "footer":{
                                 "backgroundColor":"#000000",
                                 "separator":True,
                                 "separatorColor":"#FF0500"
                                }
                              },
                              "header":{
                                "type":"box",
                                "layout":"horizontal",
                                "contents":[
                                  {
                                    "type":"text",
                                    "align":"center",
                                    "text":"ＳＥＬＦＢＯＴ",
                                    "weight":"bold",
                                    "color":"#FF0000",
                                    "size":"lg",
                                    "action":{
                                      "type": "uri",
                                      "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                      }
                                  }
                                ] 
                              },
                              "body":{
                                "type":"box",
                                "layout":"vertical",
                                "contents":[
                                  {
                                    "type": "box",
                                    "layout":"vertical",
                                    "margin":"lg",
                                    "spacing":"sm",
                                    "contents":[
                                      {
                                        "type":"box",
                                        "layout":"baseline",
                                        "spacing":"sm",
                                        "contents":[
                                          {
                                            "text": text,
                                            "size": "sm",
                                            "margin": "none",
                                            "color":"#FF9B0A",
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              },
                              "footer":{
                                "type":"box",
                                "layout":"vertical",
                                "spacing":"sm",
                                "contents":[
                                  {
                                    "type":"text",
                                    "align":"center",
                                    "text":"ＣＲＥＡＴＯＲ",
                                    "color":"#FF0000",
                                    "wrap":True,
                                    "size": "xl",
                                  },
                                  {
                                    "type":"spacer",
                                    "size":"sm"
                                   }
                                ],
                                "flex": 0,
                              }
                          }
                      }
    client.postTemplate(to, data)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "https://line.me/R/ti/p/%40137gcwpz"
           }                                                
 }
]
                          }
                      }
    client.postTemplate(to, data)

def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return client.sendMessage(to, text, contentMetadata, 0)
    
def sendMessageWithFooter(to, text):
 client.reissueUserTicket()
 dap = client.getProfile()
 ticket = "http://line.me/ti/p/"+client.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+client.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 client.sendMessage(to, text, contentMetadata=client)
 
 def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def convertYoutubeMp4(url):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.streams[-1]
    return result.url
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@ＳＥＬＦＢＯＴ "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        client.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMentionWithFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Max"
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
    client.sendMessage(to, textx, {'AGENT_NAME':'Dont Click!', 'AGENT_LINK': 'http://line.me/ti/p/~zza503', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        client.sendMessage(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "babay"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        #client.sendMessage(to, textx)
    except Exception as error:
        client.sendMessage(to)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah

def Pertambahan(a,b):
    jum = a+b
    print(a, "+",b," = ",jum)
def Pengurangan(a,b):
    jum = a-b
    print(a, "-",b," = ",jum)
def Perkalian(a,b):
    jum = a*b
    print(a, "x",b," = ",jum)
def Pembagian(a,b):
    jum = a/b
    print(a, ":",b," = ",jum)
def Perpangkatan(a,b):
    jum = a**b
    print(a,"Pangkat ",b," = ",jum )

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    client.sendMessage(to, '', contentMetadata, 7)
    
def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def removeCmdv(text, key=""):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(" ")
    return text_.replace(sep[0] + " ", "")

def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + cmd) + 1
    return text[rmv:]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def commander(text):
    pesan = text.lower()
    if settings["setKey"] == False:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settings
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = unsend
        f = codecs.open('unsend.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        bekep = tagme
        f = codecs.open('tagme.json','w','utf-8')
        json.dump(bekep, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def GenPictureQRCode(to,url):
    fn=url+".png"
    wildan=pyqrcode.create(url)
    wildan.png(fn, scale=6, module_color=[0, 0, 0, 128], background="#00FFFF")
    wildan.show()
    client.sendImage(to,fn)
    os.remove(fn)

def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    #return resp['id'].replace("https://","")

def generateLink(to, ryn, rynurl=None):
    path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.jpg')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    url = 'https://fahminogameno.life/uploadimage/action.php'
    r = requests.post(url, data=data, files=files)
    client.sendMessage(to, '%s\n%s' % (r.status_code,r.text))
    client.sendMessage(to, '{}{}'.format(rynurl,urlEncode('https://fahminogameno.life/uploadimage/images/ryngenerate.png')))

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def cloneProfile(mid):
    contact = client.getContact(mid)
    if contact.videoProfile == None:
        client.cloneContactProfile(mid)
    else:
        profile = client.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = client.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = client.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    client.updateProfileCoverById(coverId)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = client.genOBSParams({'oid': clientMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        client.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output TeamAnuBot.mp3 {}'.format(link))
    try:
        client.sendAudio(to, 'TeamAnuBot.mp3')
        time.sleep(2)
        os.remove('TeamAnuBot.mp3')
    except Exception as e:
        client.sendMessage(to, '「 ERROR 」\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
    try:
        client.sendVideo(to, "TeamAnuBot.mp4")
        time.sleep(2)
        os.remove('TeamAnuBot.mp4')
    except Exception as e:
        client.sendMessage(to, ' 「 ERROR 」\nMungkin Link Nya Salah GaN~', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~yan.001'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        sujar = "ＳＥＬＦＢＯＴ"
                        sendTextTemplate11(tmp, sujar)        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        sujar = "「Assalamualaikum」"
                        client.sendMessage(tmp, sujar)        
                    except Exception as error:
                        logError(error)

async def clientBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                client.findAndAddContactsByMid(op.param1)
            client.sendMention(op.param1, settings["autoAddMessage"], [op.param1])
        if op.type == 5:
            if settings["autoBlock"] == True:
                client.blockContact(op.param1)
            client.sendMention(op.param1, settings["autoBlockMessage"], [op.param1])
        if op.type == 13:
            if settings["autoJoin"] and clientMid in op.param3:
                group = client.getGroup(op.param1)
                group.notificationDisabled = False
                client.acceptGroupInvitation(op.param1)
                client.updateGroup(group)
                client.sendMention(op.param1, settings["autoJoinMessage"], [op.param2])
        if op.type == 13:
            if settings["autoJoin"] and clientMid in op.param3:
              group = client.getGroup(op.param1)
              if settings["memberCancel"]["on"] == True:
                if len(group.members) <= settings["memberCancel"]["members"]:
                  client.acceptGroupInvitation(op.param1)
                  client.sendMention(op.param1, "Maaf aq leave krn membernya masih sedikit" ,[op.param2])
                  client.leaveGroup(op.param1)
                else:
                  client.acceptGroupInvitation(op.param1)
                  client.sendMention(op.param1, settings["autoJoinMessage"], [op.param2])
                  client.leaveGroup(op.param1)
#=====================================================================        			
        if op.type == 11:
            if op.param1 in protectqr:
                settings["blackList"][op.param2] = True
                try:
                    if client.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                            client.reissueGroupTicket(op.param1)
                            X = client.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            client.updateGroup(X)
                            client.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
#=====================================================================            
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    settings["blackList"][op.param2] = True
                    try:
                        group = client.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            client.cancelGroupInvitation(op.param1,[op.param3])
                            client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#=====================================================================        
        if op.type == 13:
            if op.param2 in settings["blackList"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blackList"][op.param2] = True                    
                    try:
                        client.cancelGroupInvitation(op.param1,[op.param3])
                        client.kickoutFromGroup(op.param1, [op.param2])
                    except:
                    	pass
#=====================================================================
        if op.type == 17:
            if op.param2 in settings["blackList"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blackList"][op.param2] = True                    
                    try:
                        client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#=====================================================================
        if op.type == 19:
            if op.param2 in settings["blackList"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blackList"][op.param2] = True                    
                    try:
                        client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#=====================================================================
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                leaveMembers(op.param1, [op.param2])
                data = {
                        "type": "flex",
                        "altText": "WELCOME BY MAX",
                        "contents": {
                                              "styles": {
                                              "body": {
                                              "backgroundColor": "#00CDFF"
                                           },
                                           "footer": {
                                             "backgroundColor": "#000000"
                                             }
                                           },
                                           "type": "bubble",
                                             "body": {
                                             "contents": [
                                               {
                                                 "contents": [
                                                   {
                                                      "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
                                                      "size": "full",
                                                      "type": "image"
                                                    },
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#DC143C"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "text": "{}".format(client.getContact(op.param2).displayName),
                                                      "size": "md",
                                                      "align": "center",
                                                      "color": "#FF0000",
                                                      "wrap": True,
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#DC143C"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "contents": [
                                                        {
                                                          "url": "https://media.giphy.com/media/kIM3Td4W9K545bvW2K/giphy.gif",
                                                          "type": "icon",
                                                          "size": "md"
                                                        },
                                                        {
                                                          "text": "╰➣ {}".format(settings["leave"]),
                                                          "size": "md",
                                                          "margin": "none",
                                                          "color": "#EEEE00",
                                                          "wrap": True,
                                                          "weight": "regular",
                                                          "type": "text"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "layout": "baseline"
                                                    }
                                                 ],          
                                                 "type": "box",
                                                 "layout": "vertical"
                                               }
                                             ],
                                             "type": "box",
                                             "spacing": "md",
                                             "layout": "vertical"
                                           },
                                           "footer": {
                                             "contents": [
                                                {
                                                  "contents": [
                                                     {
                                                       "contents": [
                                                          {
                                                            "text": "ＳＥＬＦＢＯＴ",
                                                            "size": "sm",
                                                            "action": {
                                                              "uri": "https://line.me/R/ti/p/%40137gcwpz",
                                                              "type": "uri",
                                                              "label": "ADD ME"
                                                            },
                                                            "margin": "md",
                                                            "align": "center",
                                                            "color": "#FF1300",
                                                            "weight": "bold",
                                                            "type": "text"
                                                          }
                                                       ],
                                                       "type": "box",
                                                       "layout": "baseline"
                                                     }
                                                  ],
                                                  "type": "box",
                                                  "layout": "horizontal"
                                                }
                                             ],
                                             "type": "box",
                                             "layout": "vertical"
                                             }
                                           }
                                           }
                client.postTemplate(op.param1, data)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                welcomeMembers(op.param1, [op.param2])
                data = {
                        "type": "flex",
                        "altText": "LEAVE BY MAX",
                        "contents": {
                                              "styles": {
                                              "body": {
                                              "backgroundColor": "#00CDFF"
                                           },
                                           "footer": {
                                             "backgroundColor": "#000000"
                                             }
                                           },
                                           "type": "bubble",
                                             "body": {
                                             "contents": [
                                               {
                                                 "contents": [
                                                   {
                                                      "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
                                                      "type": "image"
                                                    },
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#DC143C"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "text": "{}".format(client.getContact(op.param2).displayName),
                                                      "size": "md",
                                                      "align": "center",
                                                      "color": "#FF0000",
                                                      "wrap": True,
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#DC143C"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "contents": [
                                                        {
                                                          "url": "https://media.giphy.com/media/h0gzUb0Wh1RIY/giphy.gif",
                                                          "type": "icon",
                                                          "size": "md"
                                                        },
                                                        {
                                                          "text": "╰➣ {}".format(settings["welcome"]),
                                                          "size": "md",
                                                          "margin": "none",
                                                          "color": "#000000",
                                                          "wrap": True,
                                                          "weight": "regular",
                                                          "type": "text"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "layout": "baseline"
                                                    }
                                                 ],          
                                                 "type": "box",
                                                 "layout": "vertical"
                                               }
                                             ],
                                             "type": "box",
                                             "spacing": "md",
                                             "layout": "vertical"
                                           },
                                           "footer": {
                                             "contents": [
                                                {
                                                  "contents": [
                                                     {
                                                       "contents": [
                                                          {
                                                            "text": "ＳＥＬＦＢＯＴ",
                                                            "size": "sm",
                                                            "action": {
                                                              "uri": "https://line.me/R/ti/p/%40137gcwpz",
                                                              "type": "uri",
                                                              "label": "ADD ME"
                                                            },
                                                            "margin": "md",
                                                            "align": "center",
                                                            "color": "#FF1300",
                                                            "weight": "bold",
                                                            "type": "text"
                                                          }
                                                       ],
                                                       "type": "box",
                                                       "layout": "baseline"
                                                     }
                                                  ],
                                                  "type": "box",
                                                  "layout": "horizontal"
                                                }
                                             ],
                                             "type": "box",
                                             "layout": "vertical"
                                             }
                                           }
                                           }
                client.postTemplate(op.param1, data)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
#=====================================================================
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    settings["blackList"][op.param2] = True
                    try:
                        if op.param3 not in settings["blackList"]:
                        	client.kickoutFromGroup(op.param1,[op.param2])
                    except:                        
                    	pass
                return
#=====================================================================                
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    settings["blackList"][op.param2] = True
                    client.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
#=====================================================================
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    settings["blackList"][op.param2] = True
                    try:
                        if op.param3 not in settings["blackList"]:
                            client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#=====================================================================                        
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)
#=====================================================================
        if op.type == 55:
            if op.param2 in settings["blackList"]:
                client.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
#=====================================================================
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = client.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n• " + Name
                        contact = client.getContact(op.param2)
                        warna1 = ("#0011FF","#000000","#AC42FF","#C80066","#1C2513","#31C2FF","#09395E")
                        warnanya1 = random.choice(warna1)
                        data = {
                               "type": "flex",
                               "altText": "ＳＥＬＦＢＯＴ",
                               "contents": {
                                                    "styles": {
                                                      "body": {
                                                        "backgroundColor": warnanya1
                                                      },
                                                      "footer": {
                                                        "backgroundColor": "#FF1E00"
                                                      }
                                                    },
                                                    "type": "bubble",
                                                    "body": {
                                                      "contents": [
                                                        {
                                                          "contents": [
                                                            {
                                                              "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
                                                              "type": "image",
                                                              "size": "full"
                                                            },
                                                            {
                                                              "type": "separator",
                                                              "color": "#FFFFFF"
                                                            },
                                                            {
                                                              "url": "https://media.giphy.com/media/f4Pf5m00KAfRPO0WK4/giphy.gif",
                                                             "type": "image"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "spacing": "md",
                                                          "layout": "horizontal"
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "color": "#FFFFFF"
                                                        },
                                                        {
                                                          "contents": [
                                                            {
                                                              "text": "☬ NamaSider ☬",
                                                              "size": "md",
                                                              "margin": "none",
                                                              "color": "#81FF00",
                                                              "align": "center",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            },
                                                            {                                                             
                                                              "text": "{}".format(client.getContact(op.param2).displayName),
                                                              "size": "md",
                                                              "margin": "none",
                                                              "color": "#FFFFFF",
                                                              "align": "center",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "spacing": "md",
                                                          "layout": "vertical"
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "color": "#FFFFFF"
                                                        },
                                                        {
                                                          "contents": [
                                                            {
                                                              "text": "☣ AutoResponSider ☣",
                                                              "size": "md",
                                                              "margin": "none",
                                                              "color": "#81FF00",
                                                              "align": "center",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            },
                                                            {
                                                              "text": "{}".format(settings["mention"]),
                                                              "size": "md",
                                                              "margin": "none",
                                                              "align": "center",
                                                              "color": "#FFFFFF",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "layout": "vertical"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "spacing": "md",
                                                      "layout": "vertical"
                                                    },
                                                    "footer": {
                                                      "contents": [
                                                        {
                                                          "contents": [
                                                            {
                                                              "contents": [
                                                                {
                                                                  "text": "Creator Caem",
                                                                  "size": "md",
                                                                  "weight": "bold",
                                                                  "action": {
                                                                    "uri": "https://line.me/R/ti/p/%40137gcwpz",
                                                                    "type": "uri",
                                                                    "label": "Audio"
                                                                   },
                                                                  "margin": "sm",
                                                                  "align": "center",
                                                                  "color": "#000000",
                                                                  "weight": "bold",
                                                                  "type": "text"
                                                                }
                                                              ],
                                                              "type": "box",
                                                              "layout": "baseline"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "layout": "horizontal"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "layout": "vertical"
                                                     }
                                                   }
                                                   }
                        client.postTemplate(op.param1, data)
                        msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(op.param1, sver, spkg, sid)
#=======================================================================================================
        if op.type == 25 or op.type == 26:
            try: 
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                cmd = command(text)
                ryyn = clientMid
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        to = receiver
#================unsend Message ==================================
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 1:
                       if settings["unsendMessage"] == True:
                           try:
                              path = client.downloadObjectMsg(msg_id, saveAs="arief.png")
                              msg_dict[msg.id] = {"from":msg._from,"image":path,"createdTime": msg.createdTime}
                           except Exception as e:
                             print (e)
                    if msg.contentType == 2:
                       if settings["unsendMessage"] == True:
                           try:
                              path = client.downloadObjectMsg(msg_id, saveAs="thata.mp4")
                              msg_dict[msg.id] = {"from": msg._from,"video":path,"createdTime": msg.createdTime}
                           except Exception as e:
                               print (e)
                    if msg.contentType == 7:
                       if settings["unsendMessage"] == True:
                           try:
                              sticker = msg.contentMetadata["STKID"]
                              link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                              msg_dict[msg.id] = {"from":msg._from,"sticker":link,"createdTime": msg.createdTime}
                           except Exception as e:
                             print (e) 
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = client.getGroup(at)
                                Boy = client.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭─「·Gambar Terhapus·」"
                                ret_ += "\n├「 Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n├「 Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n├「 Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n╰─「 ＳＥＬＦＢＯＴ 」"
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(msg_dict[msg_id]["from"])
                                warna1 = ("#001EFF","#000000","#5800DC","#D600FF","#FF7B00","#191B15","#FFED00")
                                warnanya1 = random.choice(warna1)
                                data = {
                                              "type": "flex",
                                              "altText": "ＳＥＬＦＢＯＴ",
                                              "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1}},
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(msg_dict[msg_id]["from"]).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "url": "https://media.giphy.com/media/L4HW3Gq7aT9HMGaQyW/giphy.gif",
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#6F4E37"
      },
      {
        "contents": [
          {
            "text": "「 TERDETECT 」",
            "size": "md",
            "align": "center",
            "color": "#DC143C",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#DC143C"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": str(ret_),
                "size": "xs",
                "margin": "none",
                "color": "#DC143C",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  } 
}
}
                                client.postTemplate(at, data)
                                client.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = client.getGroup(at)
                                Boy = client.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭─「·Pesan Terhapus·」\n"
                                ret_ += "├「 Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n├「 Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n├「 Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n├「Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╰─「 ＳＥＬＦＢＯＴ 」"
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(msg_dict[msg_id]["from"])
                                warna1 = ("#001EFF","#000000","#5800DC","#D600FF","#FF7B00","#191B15","#FFED00")
                                warnanya1 = random.choice(warna1)
                                data = {
                                              "type": "flex",
                                              "altText": "ＳＥＬＦＢＯＴ",
                                              "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1}},
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(msg_dict[msg_id]["from"]).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "url": "https://media.giphy.com/media/L4HW3Gq7aT9HMGaQyW/giphy.gif",
           "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#6F4E37"
      },
      {
        "contents": [
          {
            "text": "「 TERDETECT 」",
            "size": "md",
            "align": "center",
            "color": "#DC143C",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#DC143C"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": str(ret_),
                "size": "xs",
                "margin": "none",
                "color": "#DC143C",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  } 
}
}
                                client.postTemplate(at, data)
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1 
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = client.getGroup(at)
                                Boy = client.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭───「·Stiker Terhapus·」\n"
                                ret_ += "├「 Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n├「 Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n├「 Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(msg_dict[msg_id]["from"])
                                warna1 = ("#001EFF","#000000","#5800DC","#D600FF","#FF7B00","#191B15","#FFED00")
                                warnanya1 = random.choice(warna1)
                                data = {
                                              "type": "flex",
                                              "altText": "ＳＥＬＦＢＯＴ",
                                              "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1}},
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(msg_dict[msg_id]["from"]).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "url": "https://media.giphy.com/media/L4HW3Gq7aT9HMGaQyW/giphy.gif",
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#6F4E37"
      },
      {
        "contents": [
          {
            "text": "「 TERDETECT 」",
            "size": "md",
            "align": "center",
            "color": "#DC143C",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#DC143C"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": str(ret_),
                "size": "xs",
                "margin": "none",
                "color": "#DC143C",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  } 
}
}
                                client.postTemplate(at, data)
                                client.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 25 or op.type == 26:
            print ("[ 25,26 ] 「BY MAX」OPERATION")
            msg = op.message 
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 1:
                    path = client.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n├「 Sticker ID : {}".format(stk_id)
                   ret_ += "\n├「 Sticker Version : {}".format(stk_ver)
                   ret_ += "\n├「 Sticker Package : {}".format(pkg_id)
                   ret_ += "\n├「 Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n╰─「 ＳＥＬＦＢＯＴ 」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = client.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}         
                            
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                cmd = command(text)
                ryyn = "ube7e5b15dbea0cc92f2067c04d25b1fc"
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
#===============================================================================================================================================
                        if cmd == "off":
                              if msg._from in clientMid:
                                if to not in offbot:
                                  client.sendMessageWithFooter(to, "❂➣ Mode Mute Active Di Group ini")
                                  offbot.append(to)
                                  print(to)                                  
                                else:
                                  client.sendMessageWithFooter(to, "❂➣ Sukses Menonaktifkan Mute di Room ini")

                        if cmd == "on":
                              if msg._from in clientMid:
                                if to in offbot:
                                  offbot.remove(to)
                                  client.sendMessageWithFooter(to, "❂➣ Mode Mute Aktif")
                                  print(to)                                  
                                else:
                                  client.sendMessageWithFooter(to, "❂➣ Sukses Mengaktifkan Mute Di Room ini")
#===================BAGIAN TOKEN =====================================================
                        elif cmd.startswith("mp3"):
                            try:
                                footerText(to,"wait....proses")
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                ret_ = "╭────────「 Music 」"
                                ret_ += "\n├ Penyanyi: "+str(d)
                                ret_ += "\n├ Judul : "+str(c) 
                                ret_ += "\n╰────────「 Finish 」"
                                dataa= {
                                        "type": "flex",
                                        "altText": "lagi dengerin lagu",
                                        "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": g,
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": g
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text", 
        "text": ret_,
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri":  "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc"
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#0000FF"},
   }
 }
}
                                client.postTemplate(to,dataa)
                                client.sendAudioWithURL(to,e)
                            except Exception as error:
                                footerText(to, "error\n" + str(error))
                                logError(error)
                        elif cmd.startswith("music "):
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.fckveza.com/jooxmusic={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╭──「 Result Music 」"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(music["judul"]))
                                    ret_ += "\n╰──「 Total {} Music 」".format(str(len(music)))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}Music {}|「number」".format(str(setKey), str(search))
                                    sendTextTemplate(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.fckveza.com/musicid={}".format(str(music["songid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data != []:
                                            ret_ = "╭──「 Music 」"
                                            ret_ += "\n├ Singer : {}".format(str(data["result"][0]["artis"]))
                                            ret_ += "\n├ Title : {}".format(str(data["result"][0]["judul"]))
                                            ret_ += "\n├ Album : {}".format(str(data["result"][0]["single"]))
                                            ret_ += "\n╰──「 Finish 」"
                                            dataa= {
                                                    "type": "flex",
                                                    "altText": "lagi dengerin lagu",
                                                    "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "{}".format(str(data["result"][0]["imgUrl"])),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "{}".format(str(data["result"][0]["imgUrl"]))
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text", 
        "text": "{}".format(str(ret_)),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri":  "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc"
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#00FFFF"},
   }
 }
}
                                            client.postTemplate(to,dataa)
                                            client.sendAudioWithURL(to, str(data["result"][0]["mp3Url"]))
                        elif cmd.startswith("musik "):
                            try:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.get("http://ryns-api.herokuapp.com/joox?q={}".format(query))
                                data = r.text
                                data = json.loads(data)
                                data = data["result"]
                                jmlh = len(data)
                                datalagu = []
                                if jmlh > 10 :
                                    jmlh = 10
                                else:
                                    pass
                                    for x in range(0,jmlh):
                                        item= {
  "type": "bubble",
    "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
        {
        "type": "text",
        "text":  "ＳＥＬＦＢＯＴ",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "color": "#1900FF"
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "{}".format(data[x]["img"]),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "{}".format(data[x]["img"])
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "Artist :",
        "color": "#FF0000",
        "size": "md",
        "flex": 1
      },
      {
        "type": "text",
        "text": "{}".format(data[x]["title"]),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "gravity": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xs",
        "spacing": "xs",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "xs",
            "contents": [
              {
                "type": "text",
                "text": "Artist :",
                "color": "#FF0000",
                "size": "md",
                "flex": 3
              },
              {
                "type": "text",
                "text": "{}".format(data[x]["artis"]),
                "wrap": True,
                "color": "#FF0000",
                "size": "md",
                "flex": 4
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xs",
        "contents": [
          {
            "type": "spacer"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Download",
              "uri": "{}".format(data[x]["url"]),
            },
            "style": "primary",
            "color": "#0000ff"
          }
        ]
      }
    ]
   },
      "type": "bubble",
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://i.ibb.co/sb3KcWs/click-here-button-gif-c200.gif",
                    "type": "icon",
                    "size": "xl"
                    },
                    {
                    "text": "Creator Caem",
                    "size": "md",
                    "action": {
                      "uri": "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "center",
                    "color": "#001CFF",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      },
      "styles": {
        "header": {
            "backgroundColor": "#7FFF00"
        },
        "body": {
          "backgroundColor": "#00FFFF","separator": True,"separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": "#7FFF00","separator": True,"separatorColor": "#FF0000"
        }
      }
    }
                                        datalagu.append(item)
                                    data1 = {  
                                        "type": "flex",
                                        "altText": "#Joox music results for {}".format(str(query)),
                                        "contents": {
                                                      "type": "carousel",
                                                      "contents":datalagu }}
                                    client.postTemplate(to,data1)
                            except Exception as error:
                                        logError(error)
                                        client.sendReplyMessage(msg.id, to, str(error))
#==========================ABOUT====================================
                        elif cmd == "sell":
                            if msg._from in admin:
                                saya = client.getGroupIdsJoined()
                                for groups in saya:
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#666666"
        },
        "header": {
          "backgroundColor": "#666666"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "Hire Selfbot Only",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 Selfbot 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "100 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 Selfbot 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 Selfbot 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 Selfbot 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ADD ME",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~zza503"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ＳＥＬＦＢＯＴ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#666666"
        },
        "header": {
          "backgroundColor": "#666666"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "Sell Selfbot Only",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 File Selfbot Only",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "800 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 File Selfbot Only",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "800 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 File Selfbot Only",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "800 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " 1 File Selfbot Only",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "800 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ADD ME",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~zza503"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ＳＥＬＦＢＯＴ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "body": {
        "type": "cover",
        "backgroundColor": "#00FFFF"
      },
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#666666"
        },
        "header": {
          "backgroundColor": "#666666"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "Hire Selfbot Flex",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 Month",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ADD ME",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~zza503"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ＳＥＬＦＢＯＴ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#666666"
        },
        "header": {
          "backgroundColor": "#666666"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "Sell Selfbot Flex",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 File",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "2000 Wellet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 File",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "2000 Wellet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 File",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "2000 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif"
                  },
                  {
                    "text": " Flex 1 File",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "2000 Wallet",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ADD ME",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~zza503"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ＳＥＬＦＢＯＴ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                    client.postFlex(groups, data)

                        if cmd == "order":
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gK5thk7SXlySQ2xers/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "body": {
        "contents": [
          {
            "text": "OPEN OERDER",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 1SB + 2 ASIST + 1GHOST",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 1SB + 4ASIST + 1GHOST",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 1SB + 5ASIST + 1GHOST",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "300k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 1SB + 10ASIST + 1GHOST",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "400k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "text": "Self bot Kualitas Terbaik, Termurah",
            "wrap": True,
            "size": "sm",
            "type": "text",
            "color": "#0000FF"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "contents": [
          {
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri",
              "label": "OPEN ORDER"
            },
            "type": "button"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gK5thk7SXlySQ2xers/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "body": {
        "contents": [
          {
            "text": "PROTECT BOTS",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 5 Bots",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 10 Bots",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 15 Bots",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " 20 Bot",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "400k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "text": "Note: Assist Bisa Request By Pm \nSpeed Up To : 0.03",
            "wrap": True,
            "size": "sm",
            "type": "text",
            "color": "#0000FF"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "contents": [
          {
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri",
              "label": "OPEN ORDER"
            },
            "type": "button"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/gK5thk7SXlySQ2xers/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "body": {
        "contents": [
          {
            "text": "SELF BOT",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " Selfbot Only",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " Self Flex",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150 wallet",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " SB 10 Assist",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "400 wallet",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif"
                  },
                  {
                    "text": " SB 10 BOT Protect",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "700 wallet",
            "size": "xs",
            "align": "end",
            "color": "#0000FF",
            "wrap": True,
            "type": "text"
          },
          {
            "text": "Yg Mau Tanya Lebih Lengkap Pm Me",
            "wrap": True,
            "size": "sm",
            "type": "text",
            "color": "#0000FF"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "contents": [
          {
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri",
              "label": "OPEN  ORDER"
            },
            "type": "button"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    }
  ],
  "type": "carousel"
}
                                    client.postFlex(to, data)

                        if cmd == "about":
                            if msg._from in admin or msg._from in owner:
                                groups = client.getGroupIdsJoined()
                                contacts = client.getAllContactIds()
                                blockeds = client.getBlockedContactIds()
                                crt = "ube7e5b15dbea0cc92f2067c04d25b1fc"
                                supp = "ube7e5b15dbea0cc92f2067c04d25b1fc"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                runtime = timeNoww - clientStart
                                runtime = timeChange(runtime)
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#F8F8FF"
          },
          {
            "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
           "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#F8F8FF"
      },
      {
        "contents": [
          {
            "text": "「About Profile」",
            "size": "md",
            "align": "center",
            "color": "#F8F8FF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#F8F8FF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "USER: {}".format(client.getProfile().displayName),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#F8F8FF"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "RUNTIME : {}".format(str(runtime)),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "GROUP: {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "TEMAN : {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "TERBLOCK: {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "VERSION : SB ONLY",
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/j5V9IAF6Uyn13ZZYhp/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "TEAM : ＳＥＬＦＢＯＴ",
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "「CHAT CREATOR」",
                "size": "sm",
                "action": {
                  "uri": "https://line.me/R/ti/p/%40137gcwpz",
                  "type": "uri",
                  "label": "ADD CREATOR"
                },
                "margin": "xl",
                "align": "center",
                "color": "#FFFFFF",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "「ORDER PERSON」",
                "size": "sm",
                "action": {
                  "uri": "line://app/1564313616-7l6e3q0w?type=text&text=order",
                  "type": "uri",
                  "label": " 「CONTACT ORDER」"
                },
                "margin": "xl",
                "align": "center",
                "color": "#F5F5DC",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)

                        elif cmd == "about2":
                            if msg._from in admin or msg._from in owner:
                                groups = client.getGroupIdsJoined()
                                contacts = client.getAllContactIds()
                                blockeds = client.getBlockedContactIds()
                                crt = "ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"
                                supp = "ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "text": "   THE FLEX\nTEAM\n\nSELF BOT",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "text": "ＳＥＬＦＢＯＴ",
            "size": "lg",
            "align": "center",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Myname: {}".format(client.getProfile().displayName),
                "size": "md",
                "margin": "none",
                "color": "#FFFF00",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Model: Rombakan",
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Groups: {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Friend: {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Block: {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Versi : Self bot Only",
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Minat tap creator",
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＭＡＸ",
                  "uri": "http://line.me/ti/p/~zza503"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#FF0000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＭＡＸ",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }]
      }]
  }
}
}
                                client.postTemplate(to, data)

                        elif msg.text.lower().startswith('um '):
                                    client.unsendMessage(msg.id)
                                    j = int(msg.text.split(' ')[1])
                                    a = [client.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                    if len(msg.text.split(' ')) == 2:
                                        h = settings['Unsend'][msg.to]['B']
                                        n = len(settings['Unsend'][msg.to]['B'])
                                        for b in h[:j]:
                                            try:
                                                client.unsendMessage(b)
                                                settings['Unsend'][msg.to]['B'].remove(b)
                                            except:pass
                                        t = len(settings['Unsend'][msg.to]['B'])
                                    if len(msg.text.split(' ')) >= 3:h = [client.unsendMessage(client.sendMessage(to,client.adityasplittext(msg.text,'s')).id) for b in a]

                        elif cmd.startswith("unsend "):
                          if msg._from in admin:
                            args = cmd.replace("unsend ","")
                            mes = 0
                            try:
                                mes = int(args[1])
                            except:
                                mes = 1
                            M = client.getRecentMessagesV2(to, 101)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == client.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                client.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.start()
                                thread1.join()
                            client.sendMessage(msg.to, "Success unsend {} message".format(len(MId)))
                                
                        elif cmd.startswith("bc: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate11(group,"「 Broadcast 」\n" + str(pesan))
                        
                        elif cmd.startswith("bc1: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media.giphy.com/media/YkJJ6F1C8Fp1svckj8/giphy.gif",
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF0000"
        },
        "header": {
          "backgroundColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#00FF00",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ＢＲＯＤＣＡＳＴ",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ＳＥＬＦＢＯＴ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   client.postFlex(group, data)

                        elif cmd.startswith("bc2: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "6:9",
       "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "text": "{}".format(client.getProfile().displayName),
            "size": "md",
            "margin": "none",
            "color": "#FF0000",
            "weight": "bold",
            "type": "text"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   client.postFlex(group, data)
    
                        elif cmd.startswith("bc3: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "3:1",
       "type": "image",
       "url": "https://i.imgur.com/NBb34Zp.jpg",
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "text": "{}".format(client.getProfile().displayName),
            "size": "md",
            "margin": "none",
            "color": "#FF0000",
            "weight": "bold",
            "type": "text"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   client.postFlex(group, data)
    
                        elif cmd.startswith("bc4: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "3:1",
       "type": "image",
       "url": "https://media.giphy.com/media/YlXt2dP9tYOXbRho3s/giphy.gif",
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "text": "{}".format(client.getProfile().displayName),
            "size": "md",
            "margin": "none",
            "color": "#FF0000",
            "weight": "bold",
            "type": "text"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   client.postFlex(group, data)

                        elif cmd.startswith("bc5: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                data = {
    "contents": [
    {
     "hero": {
       "type": "image",
    "aspectRatio": "20:16",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/llJA98XfNzz2tPKdco/giphy.gif",
    "size": "full",
    "margin": "xs"
      },
      "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
      },
      "header": {
       "backgroundColor": "#000000"
    }
  },  
  "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                  "type": "text",
                    "text": pesan, #ᴊᴀᴍ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
            },
          {
            "type": "separator",
            "color": "#ffffff"#0000"
          },
          {
            "contents": [
               {
                "contents": [
                  {
                  "type": "text",
                    "text": "ᴊᴀᴍ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "contents": [
            {
           "type": "image",
            "url": "https://4.bp.blogspot.com/-E7DFmEtCcO0/Vx3frfw4zII/AAAAAAAAAEU/V4oUfhvK7_soc1dPxg60TQH9QmAed9m6gCLcB/s1600/line.png", #https://shop.hiushoes.com/wp-content/uploads/2017/07/logo-Line.png", #https://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://line.me/R/ti/p/%40137gcwpz",
            },         
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://jualsaladbuahenakdisurabaya.files.wordpress.com/2017/06/icon-wa.jpg", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRG8U5UNSW8lOIhkY4AfRisxxpQKlMC1WrgIKSQYCxY6cXiVAJw", #https://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/",   
           }, 
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "image",
            "url": "https://2.bp.blogspot.com/-1GRWlQBGf9I/WIRQXiXVelI/AAAAAAAAAIM/cp2h8QQYXKQOFv9hNkwC5eOogcYPxezrwCLcB/s320/sms-icon.png", #https://images-eu.ssl-images-amazon.com/images/I/41iKHNX1WbL.png", #chat
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
          },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://cdn2.iconfinder.com/data/icons/contact-flat-buttons/512/dial-512.png", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcReFldAe2KbdzYP-InVc5OzA22dW2Bi2J6cffUYdBNAy92SPWSB", #https://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
              "uri": "line://call/contacts"            
            },
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
            },
            {
           "type": "image",
            "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/b2/5a/72/b25a72fe-2ff6-015b-436a-eff66a6d0161/AppIcon-CCCP-1x_U007emarketing-85-220-9.png/1200x630bb.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },
            "flex": 1
         }
            ],
         "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"#0000"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
        }, #batas
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
           "type": "text",
            "text": "✴️ʙʀᴏᴀᴅᴄʜᴀsᴛ✴️",
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"        
          }
        ]
      }
    }
  ],
  "type": "carousel"
} 
                                client.postFlex(group, data)

                        elif cmd == "me":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                   
                                cover = client.getProfileCoverURL(sender)
                                data = {
    "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
        "action": {
          "uri": "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
      },
      "header": {
       "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
           {
           "type": "separator",
                  "color": "#000000"                 
                  },
                  {
                    "text": "✴️ᴀᴘʟɪᴋᴀsɪ ᴍᴇ✴️", #{}".format(status.statusMessage),
                "size": "sm",
                "align": "center",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "bold",
                "type": "text"
             }
            ],
            "type": "box",
            "spacing": "md",
            "layout": "horizontal"        
          },
          {
          "type": "separator",
            "color": "#ff0000"
          },
          {
          "contents": [
            {
           "type": "image",
            "url": "https://4.bp.blogspot.com/-E7DFmEtCcO0/Vx3frfw4zII/AAAAAAAAAEU/V4oUfhvK7_soc1dPxg60TQH9QmAed9m6gCLcB/s1600/line.png", #https://shop.hiushoes.com/wp-content/uploads/2017/07/logo-Line.png", #https://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://line.me/R/ti/p/%40137gcwpz",
            },         
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://jualsaladbuahenakdisurabaya.files.wordpress.com/2017/06/icon-wa.jpg", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRG8U5UNSW8lOIhkY4AfRisxxpQKlMC1WrgIKSQYCxY6cXiVAJw", #https://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/",   
           }, 
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "image",
            "url": "https://2.bp.blogspot.com/-1GRWlQBGf9I/WIRQXiXVelI/AAAAAAAAAIM/cp2h8QQYXKQOFv9hNkwC5eOogcYPxezrwCLcB/s320/sms-icon.png", #https://images-eu.ssl-images-amazon.com/images/I/41iKHNX1WbL.png", #chat
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
          },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://cdn2.iconfinder.com/data/icons/contact-flat-buttons/512/dial-512.png", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcReFldAe2KbdzYP-InVc5OzA22dW2Bi2J6cffUYdBNAy92SPWSB", #https://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
              "uri": "line://call/contacts"            
            },
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
            },
            {
           "type": "image",
            "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/b2/5a/72/b25a72fe-2ff6-015b-436a-eff66a6d0161/AppIcon-CCCP-1x_U007emarketing-85-220-9.png/1200x630bb.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "✴️ᴘʀᴏғɪʟᴇ✴️",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center" 
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
    "contents": [
      {
        "contents": [
          {
                  "type": "separator",
                  "color": "#000000"                 
                  },
                  {
                    "text": "✴️ᴀᴘʟɪᴋᴀsɪ ᴍᴇ✴️",
                "size": "sm",
                "align": "center",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "bold",
                "type": "text"
             }
            ],
            "type": "box",
            "spacing": "md",
            "layout": "horizontal"        
          },
          {
          "type": "separator",
            "color": "#ff0000"
          },
          {
          "contents": [
             {
              "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQTPm07mRMipbYi0abivFuIYfuQen2uotWyGdpJGwMm3q9tYU0v", #https://i.ibb.co/qBks5dv/20190414-220412.png", #camerahttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera",
            },
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
           "type": "image",
            "url": "https://2.bp.blogspot.com/-f8v0v2EiGbI/WDUMAHjUEsI/AAAAAAAABGI/65Mef7tDue067QVDMXzFln5BldDlrslSgCLcB/s1600/obeng%2Btang.jpg", #setting
            "size": "xs",
            "action": {
               "type": "uri",
               "uri": "line://nv/settings",
               },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#ff0000"
            },
            {
           "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRPjjbM1r_8t3Sy_XGQq9z02ZwVRNvfqlPLbJQeUerGqFYmY2Eq", #yutub
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com/"
              },
               "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://previews.123rf.com/images/dxinerz/dxinerz1508/dxinerz150800464/43410998-galer%C3%ADa-foto-icono-imagen-vectorial-tambi%C3%A9n-se-puede-utilizar-para-aplicaciones-m%C3%B3viles-barra-de-pesta%C3%B1as-de-t.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi",         
           },
           "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSYtthIuklAOYGGBZxletmiAa6TEwvcwx3scdZho1UhNjoEvS_7", #https://gotongroyong.online/Uploads/user-photo-profile/default/user-icon.png", #galery
            "size": "xs",
            "action": {
            "type": "uri",
              "uri": "line://nv/profile",
            },
             "flex": 1             
          }
        ],
         "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
          },
          {
        "type": "separator",
        "color": "#ff0000"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },      
       "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "✴️ʙᴇʀᴀɴᴅᴀ✴️",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center" 
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF0000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#ffFF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "contents": [
              {
                "contents": [
                {
                  "type": "text",
                    "text": "⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "contents": [
              {
                "contents": [
                  {                  
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
                },
                  {
                "type": "separator",
                  "color": "#ff0000"                 
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FFffff"#0000"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "https://line.me/R/ti/p/%40137gcwpz"
        },
        "align": "center"
      },
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "✴️sᴛᴀᴛᴜs✴️",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"        
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)

                        elif cmd == "me2":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                   
                                cover = client.getProfileCoverURL(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#ff0000" #0000" #cc9999"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#FFFFFF"            
      },
      {
        "type": "separator",
        "color": "#FFFFFF"      
      },
      {        
        "contents": [
          {            
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
          "text": "✴️ᴘʀᴏғɪʟᴇ✴️", #ᴘᴇʟᴀᴋᴜ:{} ".format(client.getContact(mid).displayName),
           "size": "xs",
           "align": "center",
           "color": "#FFFF00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
            },
           {     
            "type": "separator",
            "color": "#000000"
            },
          {
            "type": "separator",
            "color": "#000000"
            },
            {
           "text": "✴️ʙᴇʀᴀɴᴅᴀ✴️", #ᴘᴇʟᴀᴋᴜ:{} ".format(client.getContact(mid).displayName),
           "size": "xs",
           "align": "center",
           "color": "#FFFF00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
            }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"      
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
         {
         "type": "image",
           "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
            "size": "xl",                   
           },
           {     
            "type": "separator",
            "color": "#FFFFFF"#ff0000"
            },
          {
            "type": "separator",
            "color": "#FFFFFF"
            },
            {
           "type": "image",
           "url": cover, #"https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
            "size": "xl",
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
            "color": "#FFFFFF"
            },
          {
        "contents": [
            {          
            "text": "{}".format(client.getContact(sender).displayName),
            "size": "xs",
            "align": "center",
            "color": "#FF0099",
            "wrap": True,
            "weight": "bold",
            "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
          },
          {
            "contents": [  
           {          
            "text": "✴️ᴘᴇsᴀɴ sᴛᴀᴛᴜs✴️",
            "size": "xs",
            "align": "center",
            "color": "#FFFF00", #ffff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
          },
          {
            "contents": [
           {            
            "type": "separator",
            "color": "#FFFFFF"#ff0000"
          },
          {
            "text": "{}".format(status.statusMessage),
            "size": "xs",
            "align": "center",
            "color": "#FF6600",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"      
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [           
           {
           "type": "image",
            "url": "https://4.bp.blogspot.com/-E7DFmEtCcO0/Vx3frfw4zII/AAAAAAAAAEU/V4oUfhvK7_soc1dPxg60TQH9QmAed9m6gCLcB/s1600/line.png", #https://shop.hiushoes.com/wp-content/uploads/2017/07/logo-Line.png", #https://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://line.me/R/ti/p/%40137gcwpz",
            },         
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
          "type": "image",
            "url": "https://jualsaladbuahenakdisurabaya.files.wordpress.com/2017/06/icon-wa.jpg", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRG8U5UNSW8lOIhkY4AfRisxxpQKlMC1WrgIKSQYCxY6cXiVAJw", #https://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/",   
           }, 
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "type": "image",
            "url": "https://2.bp.blogspot.com/-1GRWlQBGf9I/WIRQXiXVelI/AAAAAAAAAIM/cp2h8QQYXKQOFv9hNkwC5eOogcYPxezrwCLcB/s320/sms-icon.png", #https://images-eu.ssl-images-amazon.com/images/I/41iKHNX1WbL.png", #chat
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
          },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
          "type": "image",
            "url": "https://cdn2.iconfinder.com/data/icons/contact-flat-buttons/512/dial-512.png", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcReFldAe2KbdzYP-InVc5OzA22dW2Bi2J6cffUYdBNAy92SPWSB", #https://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
              "uri": "line://call/contacts"            
            },
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#FFFFFF"
            },
            {
           "type": "image",
            "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/b2/5a/72/b25a72fe-2ff6-015b-436a-eff66a6d0161/AppIcon-CCCP-1x_U007emarketing-85-220-9.png/1200x630bb.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },
            "flex": 1 
         }
            ], 
            "type": "box",
            "layout": "horizontal"   
            },
      {
        "type": "separator",
        "color": "#FFFFFF"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)

                        elif cmd == "me3":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    }
  },
  "type": "bubble",
      "body": {
    "contents": [
      {
        "contents": [
          {
            "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "type": "image",
        "url": cover,
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
           "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),     
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "size": "full",
      },     
      {
        "contents": [
          {        
            "contents": [
              {              
                "type": "text",
            "text": "{}".format(status.displayName),
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#7FFF00",
            "align": "center"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#000000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ADMIN",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#000000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~zza503"
              }
          }]
      }]
  }
}
}
                                client.postTemplate(to, data)

                        elif cmd == "me4":
                                h = client.getContact(msg._from)
                                client.reissueUserTicket()
                                data = {
                                 "type": "flex",
                                 "altText": "{} cangkemu".format(str(h.displayName)),
                                 "contents": {
                                  "type": "bubble",
                                  "styles": {
                                    "header": {
                                      "backgroundColor": "#000000",
                                    },
                                    "body": {
                                      "backgroundColor": "#000000",
                                      "separator": True,
                                      "separatorColor": "#FFFFFF"
                                    },
                                    "footer": {
                                      "backgroundColor": "#000000",
                                      "separator": True
                                    }
                                  },
                                  "header": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "        ＳＥＬＦＢＯＴ",
                                        "weight": "bold",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                      }
                                    ]
                                  },
                                  "hero": {
                                    "type": "image",
                                    "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                    "size": "full",
                                    "aspectRatio": "20:13",
                                    "aspectMode": "cover",
                                    "action": {
                                      "type": "uri",
                                      "uri": "https://line://ti/p/~max.self"
                                    }
                                  },
                                  "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "action": {
                                      "type": "uri",
                                      "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                    },
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "        ＳＥＬＦＢＯＴ",
                                        "size": "md",
                                        "color": "#FFFFFF"
                                      },
                                      {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                          {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                              {
                                                "type": "icon",
                                                "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                                "size": "5xl"
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐍𝐀𝐌𝐄 :",
                                                "weight": "bold",
                                                "color": "#FFFFFF",
                                                "margin": "sm",
                                                "flex": 0
                                              },
                                              {
                                                "type": "text",
                                                "text": h.displayName,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#FF0000"
                                              }
                                            ]
                                          },
                                          {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                              {
                                                "type": "icon",
                                                "url": "https://media.giphy.com/media/ggF6OBD1wAERqZYh7K/giphy.gif",
                                                "size": "5xl"
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐀𝐃𝐌𝐈𝐍 :",
                                                "weight": "bold",
                                                "color": "#FFFFFF",
                                                "margin": "sm",
                                                "flex": 0
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐌𝐚𝐱",
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#FF0000"
                                              }
                                            ]
                                          },
                                          {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                              {
                                                "type": "icon",
                                                "url": "https://media.giphy.com/media/JSjyKthOO1v6NsoiEs/giphy.gif",
                                                "size": "5xl"
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐂𝐑𝐄𝐀𝐓𝐎𝐑 :",
                                                "margin": "sm",
                                                "color": "#FFFFFF",
                                                "weight": "bold",
                                                "flex": 0
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐌𝐚𝐱",
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#FF0000"
                                              }
                                            ]
                                          }
                                        ]
                                      },
                                      {
                                        "type": "text",
                                        "text": "━━━━━━━━━━━━━━━━━━\n𝐌𝐘 𝐖𝐇𝐀𝐓𝐒𝐔𝐏 : 𝟎𝟗𝟐𝟓𝟑𝟖𝟐𝟕𝟒𝟎",
                                        "wrap": True,
                                        "color": "#FFFFFF",
                                        "size": "xxs"
                                      }
                                    ]
                                  },
                                  "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "spacer",
                                        "size": "sm"
                                      },
                                      {
                                        "type": "button",
                                        "style": "primary",
                                        "color": "#000000",
                                        "action": {
                                          "type": "uri",
                                          "label": "𝐌𝐘 𝐂𝐎𝐍𝐓𝐀𝐂𝐓",
                                          "uri": "https://line.me/ti/p/"+client.getUserTicket().id
                                        }
                                      }
                                    ]
                                  }
                                 }
                                }
                                client.postTemplate(to, data)
                        
                        elif cmd == "me5":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                   
                                cover = client.getProfileCoverURL(sender)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#666666",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐀𝐃𝐃 𝐌𝐄",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#666666",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐎𝐑𝐃𝐄𝐑",
                  "uri": "line://app/1564313616-7l6e3q0w?type=text&text=order"
              }
          }]
      }]
  },
  "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "𝐏𝐈𝐂𝐓𝐔𝐑𝐄",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#666666",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐀𝐃𝐃 𝐌𝐄",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#666666",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐎𝐑𝐃𝐄𝐑",
                  "uri": "line://app/1564313616-7l6e3q0w?type=text&text=order"
              }
          }]
      }]
  },
  "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "𝐂𝐎𝐕𝐄𝐑",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00EE00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#666666"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "ＳＥＬＦＢＯＴ",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FF0000",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#666666"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FF7F00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#666666",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐀𝐃𝐃 𝐌𝐄",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#666666",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐎𝐑𝐃𝐄𝐑",
                  "uri": "line://app/1564313616-7l6e3q0w?type=text&text=order"
              }
          }]
      }]
  },
  "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "𝐌𝐘𝐁𝐈𝐎",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)

                        elif cmd == "me6":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(status.displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "type": "text",
            "text": "𝐒𝐭𝐚𝐭𝐮𝐬 𝐏𝐫𝐨𝐟𝐢𝐥𝐞:",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FF00FF"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "size": "md",
            "color": "#00FF00",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#666666"
    }
  },
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "𝐀𝐃𝐃 𝐌𝐄",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFFFF",
        "action": {
          "type": "uri",
          "uri": "https://line.me/R/ti/p/%40137gcwpz"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "type": "text",
        "text": "𝐎𝐑𝐃𝐄𝐑",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFFFF",
        "action": {
          "type": "uri",
          "uri": "line://app/1564313616-7l6e3q0w?type=text&text=order"
        },
        "align": "center"
      }
    ]
  }
}
}
                                client.postTemplate(to, data)

                        elif cmd == "me7":
                                h = client.getContact(msg._from)
                                client.reissueUserTicket()
                                data = {
                                        "type":"flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents":{
                                        "type":"bubble",
                                        "footer":{
                                        "type":"box",
                                        "layout":"horizontal",
                                        "contents":[
                                        {
                                        "color": "#000000",
                                        "size":"xs",
                                        "wrap":True,
                                        "action":{
                                        "type":"uri",
                                        "uri":"line://app/1564313616-7l6e3q0w?type=profile"
                                        },
                                        "type":"text",
                                        "text":"𝐏𝐫𝐨𝐟𝐢𝐥𝐞",
                                        "align":"center",
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#FF0000"
                                        },
                                        {
                                        "color":"#000000",
                                        "size":"xs",
                                        "wrap":True,
                                        "action":{
                                        "type":"uri",
                                        "uri":"http://line.me/ti/p/" + client.getUserTicket().id
                                        },
                                        "type":"text",
                                        "text":"𝐀𝐃𝐃 𝐌𝐄",
                                        "align":"center","weight":"bold"
                                        }
                                        ]
                                        },
                                        "styles":{
                                        "footer":{
                                        "backgroundColor":"#FF0000"
                                        },
                                        "body":{
                                        "backgroundColor":"#666666"
                                        }
                                        },
                                        "body":{
                                        "type":"box",
                                        "contents":[
                                        {
                                        "type":"box",
                                        "contents":[
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "aspectMode":"cover",
                                        "gravity":"bottom",
                                        "aspectRatio":"1:1",
                                        "size":"sm",
                                        "type":"image",
                                         "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                         "action": {
                                         "type":"uri","uri": "line://app/1564313616-7l6e3q0w?type=profile"
                                         }
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "type":"image",
                                        "aspectMode":"cover",
                                        "aspectRatio":"1:1",
                                        "size":"sm",
                                        "url":"https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                         "action": {
                                         "type":"uri","uri":"line://app/1564313616-7l6e3q0w?type=profile"
                                         }
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        }
                                        ],
                                        "layout":"vertical",
                                        "spacing":"none","flex":1
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "type":"box",
                                        "contents":[
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "color":"#FF9B0A",
                                        "size":"md",
                                        "wrap":True,
                                        "type":"text",
                                        "text":"ＢＹＭＡＸ",
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "color":"#FF0000",
                                        "size":"md",
                                        "wrap":True,
                                        "type":"text",
                                        "text":"{}".format(h.displayName),
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#FF0000"
                                        },
                                        {
                                        "color":"#000000",
                                        "size":"xs",
                                        "wrap":True,
                                        "type":"text",
                                        "text":"Status Profile:",
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"text",
                                        "text":"{}".format(h.statusMessage),
                                        "size":"xxs",
                                        "wrap":True,
                                        "color":"#FF9B0A"
                                        }
                                        ],
                                        "layout":"vertical",
                                        "flex":2
                                        }
                                        ],
                                        "layout":"horizontal",
                                        "spacing":"md"
                                        },
                                        "hero":{
                                        "aspectMode":"cover",
                                        "margin":"xxl",
                                        "aspectRatio":"1:1",
                                        "size":"full",
                                        "type":"image",
                                        "url":"https://obs.line-scdn.net/{}".format(h.pictureStatus),
                                        "action": {
                                         "type":"uri","uri": "line://app/1564313616-7l6e3q0w?type=profile"
                                          }
                                        }
                                    }
                                }
                                client.postTemplate(to, data)

                        elif cmd == "me8":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                   
                                cover = client.getProfileCoverURL(sender)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PROFIL",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#7FFF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "STATUS",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#F0FFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BERANDA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)
   
                        elif cmd == "me9":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)
                                warna1 = ("#81FF00","#00F2FF","#FFCC00","#FF0019","#FF00E5","#2D00FF","#FA0143","#00FF8C","#000000")
                                warnanya1 = random.choice(warna1)
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴ",
                                        "contents": {
                                                             "type": "bubble",
                                                             "header": {
                                                             "type": "box",
                                                             "layout": "vertical",
                                                             "spacing": "xs",
                                                             "contents": [
                                                               {
                                                                 "type": "text",
                                                                 "text": "ＳＥＬＦＢＯＴ",
                                                                 "wrap" : True,
                                                                 "weight": "bold",
                                                                 "color": warnanya1,
                                                                 "align": "center",
                                                                 "size":"md"
                                                               }
                                                             ]
                                                            },
                                                            "hero": {
                                                              "type": "image",
                                                              "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
                                                              "size": "full",
                                                              "margin": "xxl"
                                                            },
                                                            "body": {
                                                              "type": "box",
                                                              "layout": "vertical",
                                                              "spacing": "md",
                                                              "contents": [
                                                                 {
                                                                   "type": "box",
                                                                   "layout": "horizontal",
                                                                   "spacing": "md",
                                                                   "contents": [
                                                                      {
                                                                        "url": "https://media.giphy.com/media/ehgkU1Gsba9hh39POL/giphy.gif",
                                                                        "type": "image",
                                                                        "size": "sm"
                                                                      },
                                                                      {
                                                                        "type": "separator",
                                                                       },
                                                                       {
                                                                         "type": "text",
                                                                         "text": "𝐍𝐀𝐌𝐄:\n{}".format(status.displayName),
                                                                         "wrap": True,
                                                                         "size": "md",
                                                                       }
                                                                   ]
                                                                 },
                                                                 {
                                                                   "type": "separator",
                                                                 },
                                                                 {
                                                                   "type": "box",
                                                                   "layout": "horizontal",
                                                                   "spacing": "md",
                                                                   "contents": [
                                                                      {
                                                                        "url": "https://media.giphy.com/media/lOIxFNpShyaV1UjSpS/giphy.gif",
                                                                        "type": "image",
                                                                        "size": "sm"
                                                                      },
                                                                      {
                                                                        "type": "separator",
                                                                      },
                                                                      {
                                                                        "type": "text",
                                                                        "text": "𝐏𝐑𝐎𝐅𝐈𝐋𝐄:\n{}".format(status.statusMessage),
                                                                        "wrap": True,
                                                                        "size": "xs"
                                                                      }
                                                                   ]
                                                                 }
                                                              ]
                                                            },
                                                            "footer": {
                                                              "type": "box",
                                                              "layout": "vertical",
                                                              "contents": [
                                                                 {
                                                                   "type": "spacer",
                                                                   "size": "md"
                                                                 },
                                                                 {
                                                                   "type": "button",
                                                                   "action": {
                                                                     "type": "uri",
                                                                     "label": "𝙲𝙾𝙽𝚃𝙰𝙲𝚃",
                                                                     "uri": "https://line.me/R/ti/p/%40137gcwpz",
                                                                 },
                                                                  "style":"primary",
                                                                  "color": warnanya1
                                                              }
                                                        ]
                                                    }
                                                }
                                            }
                                client.postTemplate(to, data)
                                
                        elif cmd == "me10":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                             	
                                data = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "6:9",
       "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#0000FF",
                    "align": "center"               
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },      
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "type": "text",
            "text": "ＳＥＬＦＢＯＴ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)
#===================================================================
                        if "haha" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://i.ibb.co/9Yp3hNN/AW1238395-00.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "gift" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/d7ShmJHWybIydmxZXP/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "fuck" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/hs0pZaEWmx86uxUtKJ/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "55" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/gHohwrHIWhU8UboBsl/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "yes" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/Q5FEcpCJPOVAigoHqZ/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "ok" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/Q93nnpN6qu2xdl08A3/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "eiei" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/MAWeODSGxRQT4iiRDg/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "night" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/hVyS1bq5HBV12g5bkZ/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "what" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/Tg1X4fl6TAUw8D3ytK/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "hehe" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/SU7xfoYuAb4xnslrc4/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "hot" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/U1gaxWVTyeqp8lSfdI/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "love" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/WQZpY0ZAVKWvnIzrJC/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "no" in msg.text.lower():
                            if msg._from in clientMid:
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://media.giphy.com/media/gK5gdtHhz2dMu3Fnmy/giphy.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "https://line.me/R/ti/p/%40137gcwpz"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)
#=====================================================================================================================
                        if msg.toType != 0 and msg.toType == 2:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    if ryyn in mention["M"]:
                                        if ryyn in mention["M"]:
                                            if to not in tagme['ROM']:
                                                tagme['ROM'][to] = {}
                                            if sender not in tagme['ROM'][to]:
                                                tagme['ROM'][to][sender] = {}
                                            if 'msg.id' not in tagme['ROM'][to][sender]:
                                                tagme['ROM'][to][sender]['msg.id'] = []
                                            if 'waktu' not in tagme['ROM'][to][sender]:
                                                tagme['ROM'][to][sender]['waktu'] = []
                                            tagme['ROM'][to][sender]['msg.id'].append(msg.id)
                                            tagme['ROM'][to][sender]['waktu'].append(msg.createdTime)

                            elif receiver in temp_flood:
                                if temp_flood[receiver]["expire"] == True:
                                    if cmd == "open":
                                        temp_flood[receiver]["expire"] = False
                                        temp_flood[receiver]["time"] = time.time()
                                        sendTextTemplate11(to, "BOT ACTIVE AGAIN")
                                    return
                                elif time.time() - temp_flood[receiver]["time"] <= 5:
                                    temp_flood[receiver]["flood"] += 1
                                    if temp_flood[receiver]["flood"] >= 20:
                                        temp_flood[receiver]["flood"] = 0
                                        temp_flood[receiver]["expire"] = True
                                        ret_ = "Spam terdetect DI Ruangan"
                                        contact = client.getContact(sender)
                                        warna1 = ("#000080","#0000CD","#00FA9A","#FFA500","#98FB98","#00FF7F","#D8BFD8","000000","#40E0D0")
                                        warnanya1 = random.choice(warna1)
                                        data = {
                                                "messages": [
                                                          {
                                                            "type": "flex",
                                                            "altText": "ＳＥＬＦＢＯＴ",
                                                            "contents":{
"contents":[
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [ 
      {
        "type": "text",
        "text":  "{}".format(contact.displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "{}".format(str(ret_)),
        "color": "#000000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "https://line.me/R/ti/p/%40137gcwpz",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": warnanya1},
   }
}
],
"type": "carousel"
}
}
]
}
                                        sendTemplate(to, data)
                                else:
                                    temp_flood[receiver]["flood"] = 0
                                temp_flood[receiver]["time"] = time.time()
                            else:
                                temp_flood[receiver] = {
                                 "time": time.time(),
                                 "flood": 0,
                                 "expire": False
                                }
            except Exception as error:
                logError(error)
#=============================STICKER==========================================================================
        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
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
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╭───「 Details Post 」"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = client.getContact(sender)
                                        auth = "\n├≽ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n├≽ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n├≽ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n├≽ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n├≽ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n├≽ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n├≽ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n├≽ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n├≽ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n├≽ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n├≽ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╰───「 Finish 」"
                                    sendTextTemplate(to, str(ret_))
                                except:
                                    client.sendMessage(to, "Post tidak valid")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = client.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
#                                adws = client.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplate11(to, "꧁༺ AUTOLIKE BY MAX ༻꧂")
            except Exception as error:
                logError(error)
#==========================================================================================================
        if op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
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

                            if terminal == "logout":
                              if msg._from in clientMid:
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id, to, "Your selfbot has been logout ♪")
                                sys.exit("[ INFO ] BOT SHUTDOWN")

                            elif terminal == "reset":
                              if msg._from in clientMid:
                                restart = "Restarting Sukses"
                                contact = client.getContact(sender)
                                sendTextTemplate(to, restart)
                                restartBot()

                            elif terminal == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - clientStart
                                runtime = timeChange(runtime)
                                run = "Bot telah aktif selama {}".format(str(runtime))
                                sendTextTemplate(to, run)

                            elif terminal == "speed":
                            	get_profile_time_start = time.time()
                            	get_profile = client.getProfile()
                            	get_profile_time = time.time() - get_profile_time_start
                            	speed = " {} detik".format(str(get_profile_time))
                            	sendTextTemplate(to, speed)

                            elif terminal == "sp":
                              if msg._from in admin:
                                 start = time.time()                               
                                 sendTextTemplate(msg.to, "Checking the speed of the bots...")                               
                                 elapsed_time = time.time() - start
                                 sendTextTemplate(msg.to, "Speed Is At :\n{} detik".format(str(elapsed_time/100)))

                            elif terminal == "gid":
                              if msg._from in admin:
                                gid = client.getGroupIdsJoined()
                                h = ""
                                for i in gid:
                                    h += "❂➣ %s:\n%s\n\n" % (client.getGroup(i).name,i)
                                client.sendReplyMessage(msg_id, to,"List Group\n\n"+h)

                            elif terminal == "namagroup":
                              if msg._from in clientMid:
                                gid = client.getGroup(to)
                                sendTextTemplate(to, "🔹 Display Name🔹\n❂➣ {}".format(gid.displayName))

                            elif terminal == "fotogroup":
                              if msg._from in clientMid:
                                gid = client.getGroup(to)
                                sendTextTemplate(to,"http://dl.profile.line-cdn.net/{}".format(gid.pictureStatus))

                            elif terminal == "reject":
                                if msg._from in clientMid:
                                  ginvited = client.getGroupIdsInvited()
                                  if ginvited != [] and ginvited != None:
                                      for gid in ginvited:
                                          client.rejectGroupInvitation(gid)
                                      sendTextTemplate(to, "❂➣ ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                                  else:
                                      sendTextTemplate(to, "❂➣ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ")
         
                            elif terminal == "clear spam":
                              if msg._from in admin:
                                ginvited = client.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        client.acceptGroupInvitation(gid)
                                        client.leaveGroup(gid)
                                    sendTextTemplate(to, " ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                                else:
                                    sendTextTemplate(to, "ɴᴏᴛʜɪɴɢ")

                            elif terminal == "reset error":
                                if sender in admin:
                                    with open('errorLog.txt', 'w') as er:
                                        error = er.write("")
                                    client.sendMessageWithFooter(to, str(error))

                            elif terminal.startswith("setkey: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                settings["keyCommand"] = str(key).lower()
                                sendTextTemplate(to, "Setkey dirubah menjadi : 「{}」".format(str(key).lower()))

                            elif msg.text.lower().startswith("changevpprofile"):
                                if msg._from in admin:
                                        link = removeCmd("changevpprofile", text)
                                        contact = client.getContact(sender)
                                        client.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                                        print("Sedang Mendownload Data")
                                        pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                        subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                                        pict = client.downloadFileURL(pic)
                                        vids = "TeamAnuBot.mp4"
                                        changeVideoAndPictureProfile(pict, vids)
                                        client.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                                        os.remove("FadhilvanHalen.mp4")

                            elif cmd == "kudis":
                                if msg._from in admin:
                                   saya = client.getGroupIdsJoined()
                                   for groups in saya:
                                        data = {
      "contents": [
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://media.giphy.com/media/darGvoGHgmgkYwQjaA/giphy.gif",
            "action": {
              "uri": "http://line.me/ti/p/yWFvdLpiHp",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#000000"
            },
            "header": {
              "backgroundColor": "#000000"
            }
          },
          "hero": {
           "type": "image",
           "aspectRatio": "20:13",
           "aspectMode": "cover",
           "url": "https://media.giphy.com/media/jOz1tMGmntXUgE4xS8/giphy.gif",
           "size": "full",
           "margin": "xl"
          }, 
          "type": "bubble",
          "body": {
        "contents": [
          {       
            "type": "separator",
            "color": "#000000"
          },      
          {
            "text": "📣 clik di bawah untuk pesan",
            "wrap": True,
            "size": "sm",
            "type": "text",
            "color": "#FF6600"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
            "text": "ADMIN",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~zza503",
            },
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"
              }
            ]
          }
        },
        {
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#000000"
            },
            "header": {
              "backgroundColor": "#000000"
            }
          },
          "type": "bubble",
          "body": {
            "contents": [
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "type": "text",
                        "text": "ＳＥＬＦＢＯＴ",
                        "size": "lg",
                        "wrap": True,
                        "weight": "bold",
                        "color": "#FF0000",
                        "align": "center"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "image",
            "url": "https://media.giphy.com/media/fXb6GXalpnQSg25yKt/giphy.gif",
            "aspectRatio": "2:1",
            "aspectMode": "cover",
            "size": "full",
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "LIST PROMO",
                        "color": "#FFFF00",
                        "wrap": True,
                        "weight": "bold",
                        "type": "text",
                        "size": "lg",
                        "align": "center"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Jasa pasang template ke script\n2.Self template\n3.Menyewakan 6bot war\n4.Pemasangan fitur\n5.DLL",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }, #batas
          "type": "bubble",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
            "text": "ADMIN",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~zza503",
            },
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },  
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/R/ti/p/%40137gcwpz"
            },
            "align": "center"
          },
            ]   
          }
        }
      ],
      "type": "carousel"
    }
                                        client.postFlex(groups, data)

                            elif cmd == "help":
                              if msg._from in admin:
                                 data = {
      "contents": [
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://media.giphy.com/media/KFoA5qHHvTFHveSfDL/giphy.gif",
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "body": {
            "contents": [
              {
                "text": "꧁༺ M E N U ༻꧂ ",
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Me *โปรไฟล์เรา\n2.Me2-10 *โปรไฟล์เรา\n3.Help *รายการคำสั่ง\n4.Help1-3 *รายการคำสั่ง",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Mymid *เอ็มไอดีของเรา\n6.Tag *แทคสมาชิกทั้งกลุ่ม\n7.Status *เช็คการตั้งค่า\n8.Reset *รีสตาร์ทบอท",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Url grup *ลิ้งกลุ่ม\n10.Open *เปิดลิ้ง\n11.Close *ปิดลิ้ง\n12.Grouplist *กลุ่มทั้งหมดของเรา",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.FriendInfo「@」*ข้อมูลคนอื่น\n14.Getpict「@」*รูปคนอื่น\n15.Getbio「@」*สเตตัสคนอื่น\n16.Getcover「@」รูปปกคนอื่น",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＣＲＥＡＴＯＲ",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",    
                "text": "ＳＥＬＦＢＯＴ",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          }
        },
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://media.giphy.com/media/KFoA5qHHvTFHveSfDL/giphy.gif",
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "body": {
            "contents": [
              {
                "text": "꧁༺ M E N U ༻꧂ ",
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Respon on|off *ตอบกลับอัตโนมัติ\n2.Sider on|off *ดูคนแอบ\n3.Welcome on|off *ต้อนรับคนเข้าออก\n4.Sticker on|off *สติกเกอร์ใหญ่",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Autojoin on|off *เข้ากลุ่มอัตโนมัติ\n6.Autoread on|off *อ่านอัตโนมัติ\n7.Autoblock on|off *บล็อกอัตโนมัติ\n8.Autoadd on|off *เพิ่มเพื่อนอัตโนมัติ",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Groupbc:「Text」*ประกาศกลุ่ม\n10.Friendbc:「Text」*ประกาศเพื่อน\n11.Broadcast:「Text」*ประกาศ\n12.Mp3:「Text」*เพลง",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.Setrespon:「Text」*ตั้งคนแทค\n14.Setautoadd:「Text」*ตั้งรับเพื่อน\n15.Setautoblock:「Text」*ตั้งบล็อก\n16.Setwelcome:「Text」*ตั้งคนเข้าออก",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＣＲＥＡＴＯＲ",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＳＥＬＦＢＯＴ",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          }
        },
        {
          "body": {
            "type": "cover",
            "backgroundColor": "#00FFFF"
          },
          "hero": {
            "aspectMode": "cover",
            "url": "https://media.giphy.com/media/KFoA5qHHvTFHveSfDL/giphy.gif",
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "body": {
            "contents": [
              {
                "text": "꧁༺ M E N U ༻꧂ ", 
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Bc *คท คนติดดำ\n2.Cb *ล้างดำ\n3.Ban「@」\n4.Unban「@」",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Menu *เมนู\n6.Setting *ตั้งค่า\n7.Set *ตั้งข้อความ\n8.Sticker *สติกเกอร์",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Youtube:「Text」*ยูทูป\n10.Tube:「Text」*ยูทูป\n11.Music:「Text」*เพลง\n12.About *ข้อมูล",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.Unsend「number」*ยกเลิกข้อความ\n14.Myurl *ลิ้งค์ไลน์ของเรา\n15.Friendlist *เพื่อนทั้งหมด\n16.All mid *เอ็มไอดีทุกคนในกลุ่ม",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＣＲＥＡＴＯＲ",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＳＥＬＦＢＯＴ",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",  
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          }
        },
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://media.giphy.com/media/KFoA5qHHvTFHveSfDL/giphy.gif",
            "action": {
              "uri": "https://line.me/R/ti/p/%40137gcwpz",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "body": {
            "contents": [
              {
                "text": "꧁༺ M E N U ༻꧂ ",
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Unsend on|off *ตรวจยกเลิกข้อความ\n2.Checkcontact on|off *เช็คคอนแท็ค\n3.Checkpost on|off *เช็คโพส\n4.Checksticker on|off *เช็คสติกเกอร์",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Bc:「Text」*ประกาศ\n6.Bc1:「Text」*ประกาศ\n7.Bc2:「Text」*ประกาศ\n8.Bc3:「Text」*ประกาศ",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Changename:「Text」*เปลี่ยนชื่อ\n10.Changebio:「Text」เปลี่ยนสเตตัส*\n11.Changepict *เปลี่ยนรูปโปรไฟล์\n12.Changecover *เปลี่ยนรูปปก",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.Kickban *ลบคนติดดำ\n14.Kick「@」*ลบสมาชิกบางคน\n15.Clear spam *ลบรัน\n16.Remove *ลบแชท",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＣＲＥＡＴＯＲ",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "ＳＥＬＦＢＯＴ",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "https://line.me/R/ti/p/%40137gcwpz"
                },
                "align": "center"            
              }
            ]
          }
        }
      ],
      "type": "carousel"
    }

                                 client.postFlex(to, data)         

                            elif cmd == "mini help":
                                    groups = client.getGroupIdsJoined()
                                    contacts = client.getAllContactIds()
                                    blockeds = client.getBlockedContactIds()
                                    crt = "ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"
                                    supp = "ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"
                                    suplist = []
                                    lists = []
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    timeNoww = time.time()
                                    for i in range(len(day)):
                                       if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                       if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    data = {
                                            "type": "flex",
                                            "altText": "ＳＥＬＦＢＯＴ",
                                            "contents": {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FFFFFF"
        }
      },
      "type": "bubble",
          "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "type": "image",
            "url": "https://2.bp.blogspot.com/-ylGY-IOCoYw/VebwqOEn_LI/AAAAAAAABY8/VeIVOOGApxc/s1600/speed.gif", #hp
            "size": "xl",
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "type": "image",
            "url": "https://lh6.googleusercontent.com/proxy/LNw-fbsMb8WXu3ogbg0oUzufD7b-nAeq7OIbjS5ctfs4Y759365RSPtnhUgZ-gV9GosIMYpnta2vNDF9Gnt9gVWz1pfI9Q=s0-d", #bbm
            "size": "xl",
              }
            ],
            "type": "box",
            "spacing": "md",
            "layout": "horizontal"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "type": "image",
            "url": "https://i.imgur.com/mXal0tk.jpg", #hp
            "aspectRatio": "5:1",
            "aspectMode": "cover",
            "size": "full",
              }
            ],
            "type": "box",
            "spacing": "md",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " {}".format(client.getProfile().displayName),
                    "size": "md",
                    "margin": "none",
                    "color": "#7CFC00",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " GROUP MENU\n Me\n Me2-10\n Help\n Speed\n Kick @\n\n",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              },
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " PENGATURAN MENU\n Sider on|off\n Welcome on|off\n Respon on|off\n Autojoin on|off\n Autoblock on|off\n\n",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              },
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " USER MENU\n About\n Tag\n Changename: \n Grouplist\n Reset\n Clear spam\n Reject\n Remove\n\n",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              },
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " PEMASARAN BC\n Bc1: \n Bc2: \n Bc3: \n Broadcast: \n Pendinglist\n\n",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              },
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " SPECIAL MENU\n Mp3: \n Musik: \n Music: \n Tube: \nYoutube: \n Changename: \n Changebio: \n Memberlist\n\n",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              },
              {
                "contents": [
                  {
                    "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                    "type": "icon",
                    "size": "md"
                  },
                  {
                    "text": " BLACKLIST BOT\n Kickban\n Bc\n Cb\n Bl\n Ban @\n Unban @\n\n",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#000000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "ADMIN",
                      "uri": "http://line.me/ti/p/~zza503"
                  }
              }, {
                  "flex": 3,
                  "type": "button",
                  "style": "primary",
                  "color": "#000000",
                  "margin": "sm",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "CREATOR",
                      "uri": "https://line.me/R/ti/p/%40137gcwpz"
                  }
              }]
          }]
      }
    }
    }
                                    client.postTemplate(to, data)

                            elif cmd == "help1":
                                data = {
                                            "type": "template",
                                            "altText": "ＳＥＬＦＢＯＴ",
                                            "template": {
                                                "type": "carousel",
                                                "columns": [
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "MENU",
                                                        "text": "To Use This command just menu help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=menu"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "SETTING",
                                                        "text": "To Use This command just Setting help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=setting"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "SET",
                                                        "text": "To Use This command just Set help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=set"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "GROUP",
                                                        "text": "To Use This command just Group help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=group"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "PROTECT",
                                                        "text": "To Use This command just protect help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=protect"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "FRIEND",
                                                        "text": "To Use This command just Friend help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=friend"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    } 
                                                ],
                                                "imageAspectRatio": "square",
                                                "imageSize": "contain"
                                            }
                                       }
                                client.postTemplate(to, data)
                            elif cmd == "help2":
                                data = {
                                            "type": "template",
                                            "altText": "ＳＥＬＦＢＯＴ",
                                            "template": {
                                                "type": "carousel",
                                                "columns": [
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "MEDIA",
                                                        "text": "To Use This command just Media help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=media"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "SPECIAL ORDER",
                                                        "text": "To Use This command just Special help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=special"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "STICKER",
                                                        "text": "To Use This command just Sticker help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=sticker"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "PROFILE",
                                                        "text": "To Use This command just Profile help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=profile"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                                        "title": "SPAM",
                                                        "text": "To Use This command just Spam help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=spam"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Press To Contact",
                                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                            }
                                                        ]
                                                    } 
                                                ],
                                                "imageAspectRatio": "square",
                                                "imageSize": "contain"
                                            }
                                       }
                                client.postTemplate(to, data)
                            elif cmd == "help3":
                              if msg._from in admin:
                                  h = client.getContact(msg._from)
                                  client.reissueUserTicket()
                                  warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                  warnanya1 = random.choice(warna1)
                                  data = {
                                 "type": "flex",
                                 "altText": "Sen Help Message {}".format(str(h.displayName)),
                                 "contents": {
                                  "type": "bubble",
                                  "styles": {
                                    "header": {
                                      "backgroundColor": "#333333",
                                    },
                                    "body": {
                                      "backgroundColor": "#333333",
                                      "separator": True,
                                      "separatorColor": "#FFFFFF"
                                    },
                                    "footer": {
                                      "backgroundColor": "#333333",
                                      "separator": True
                                    }
                                  },
                                  "header": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "ＳＥＬＦＢＯＴ",
                                        "weight": "bold",
                                        "color": warnanya1,
                                        "size": "lg"
                                      }
                                    ]
                                  },
                                  "hero": {
                                    "type": "image",
                                    "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                    "size": "full",
                                    "aspectRatio": "20:13",
                                    "aspectMode": "cover",
                                    "action": {
                                      "type": "uri",
                                      "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                    }
                                  },
                                  "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "action": {
                                      "type": "uri",
                                      "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                    },
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "╭───────────────────",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＨＥＬＰ「ชุดคำสั่ง」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＨＥＬＰ１「ชุดคำสั่งที่1」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＨＥＬＰ２「ชุดคำสั่งที่2」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＭＥ「โปรไฟล์ของเรา」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＳＰＥＥＤ「วัดความเร็ว」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＡＢＯＵＴ「ข้อมูล」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＢＡＮ @「ลงบัญชีดำ」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＵＮＢＡＮ @「ล้างบัญชีดำ」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＫＩＬＬＢＡＮ「เตะบัญชีดำ」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＢＣ「เชคคอนแท็คบัญชีดำ」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＣＢ「ล้างบัญชีดำทั้งหมด」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "│• ＴＡＧ「แท็คคนทั้งกลุ่ม」",
                                        "size": "md",
                                        "color": warnanya1,
                                      },
                                      {
                                        "type": "text",
                                        "text": "╰───────────────────",
                                        "size": "md",
                                        "color": warnanya1,
                                      }
                                    ]
                                  },
                                  "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "spacer",
                                        "size": "sm"
                                      },
                                      {
                                        "type": "button",
                                        "style": "primary",
                                        "color": "#FF0000",
                                        "action": {
                                          "type": "uri",
                                          "label": "𝐌𝐘 𝐂𝐎𝐍𝐓𝐀𝐂𝐓",
                                          "uri": "https://line.me/ti/p/"+client.getUserTicket().id
                                        }
                                      }
                                    ]
                                  }
                                 }
                                }
                                  client.sendFlex(to, data)
                            elif terminal == "menu" or cmd == "help menu":
                              if msg._from in admin:
                                md = "╭───「 Menu Message」"
                                md+="\n├≽ help"
                                md+="\n├≽ help1"
                                md+="\n├≽ help2"
                                md+="\n├≽ help3"
                                md+="\n├≽ mini help"
                                md+="\n├≽ kudis"
                                md+="\n├≽ help special"
                                md+="\n├≽ help sticker"
                                md+="\n├≽ help setting"
                                md+="\n├≽ help set"
                                md+="\n├≽ help group"
                                md+="\n├≽ help protect"
                                md+="\n├≽ help friend"
                                md+="\n├≽ help profile"
                                md+="\n├≽ help spam"
                                md+="\n├≽ help media"
                                md+="\n├≽ ban「@」"
                                md+="\n├≽ unban「@」"
                                md+="\n├≽ bc"
                                md+="\n├≽ bl"
                                md+="\n├≽ cb"
                                md+="\n├≽ killban"
                                md+="\n├≽ me"
                                md+="\n├≽ speed"
                                md+="\n├≽ runtime"
                                md+="\n├≽ reset"
                                md+="\n├≽ remove"
                                md+="\n├≽ about"
                                md+="\n├≽ status"
                                md+="\n├≽ broadcast:「Text」"
                                md+="\n├≽ groupbc:「Text」"
                                md+="\n├≽ friendbc:「Text」"
                                md+="\n├≽ reject"
                                md+="\n├≽ mykey"
                                md+="\n├≽ changekey"
                                md+="\n├≽ setkey:「Text」"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "help special" or cmd == "special":
                              if msg._from in admin:
                                md = "╭───「 Private Message 」"
                                md+="\n├≽ Ok"
                                md+="\n├≽ Eiei"
                                md+="\n├≽ Fuck"
                                md+="\n├≽ Night"
                                md+="\n├≽ What"
                                md+="\n├≽ Gift"
                                md+="\n├≽ Good"
                                md+="\n├≽ Yes"
                                md+="\n├≽ No"
                                md+="\n├≽ Hehe"
                                md+="\n├≽ Love"
                                md+="\n├≽ Hot"
                                md+="\n├≽ Haha"
                                md+="\n├≽ 555"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "sticker" or cmd == "help sticker":
                              if msg._from in admin:
                                md = "╭───「 Add Sticker 」"
                                md+="\n├≽ AddSticker「Text」  "
                                md+="\n├≽ Addleavesticker"
                                md+="\n├≽ Addwelcomesticker"
                                md+="\n├≽ Addresponsticker"
                                md+="\n├≽ Addsidersticker"
                                md+="\n├≽ AddStp「Text」"
                                md+="\n┝──「 dell Sticker 」"
                                md+="\n├≽ Delsticker「Text」"
                                md+="\n├≽ Delwelcomesticker"
                                md+="\n├≽ Delresponsticker "
                                md+="\n├≽ Delsidersticker "
                                md+="\n├≽ Delleavesticker "
                                md+="\n├≽ DelStp「Text」 "
                                md+="\n┝──「 List Sticker 」 "
                                md+="\n├≽ List stp"
                                md+="\n├≽ List sticker"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "setting" or cmd == "help setting":
                              if msg._from in admin:
                                md = "╭───「 Setting Message」"
                                md+="\n├≽ autoadd 「 On/Off 」 "
                                md+="\n├≽ autoblock 「 On/Off 」"
                                md+="\n├≽ autolike 「 On/Off 」"
                                md+="\n├≽ autojoin 「 On/Off 」"
                                md+="\n├≽ autojointicket 「 On/Off 」"
                                md+="\n├≽ autoread 「 On/Off 」"
                                md+="\n├≽ respon 「 On/Off 」"
                                md+="\n├≽ checkcontact 「 On/Off 」"
                                md+="\n├≽ checkpost 「 On/Off 」"
                                md+="\n├≽ checksticker 「 On/Off 」"
                                md+="\n├≽ sticker 「 On/Off 」 "
                                md+="\n├≽ Welcome 「 On/Off 」"
                                md+="\n├≽ unsend 「 On/Off 」 "
                                md+="\n├≽ deletefriend 「 On/Off 」 "
                                md+="\n├≽ setkey 「 On/Off 」 "
                                md+="\n├≽ lurking  「 On/Off 」"
                                md+="\n├≽ Lurking"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "set" or cmd == "help set":
                              if msg._from in admin:
                                md = "╭───「 Set Message」"
                                md+="\n├≽ setautoadd:「Text」  "
                                md+="\n├≽ setrespon:「Text」"
                                md+="\n├≽ setautojoin:「Text」"
                                md+="\n├≽ setsider:「Text」"
                                md+="\n├≽ setwelcome:「Text」"
                                md+="\n├≽ setleave:「Text」"
                                md+="\n├≽ setmember:「Num」"
                                md+="\n├≽ setcomment:「Text」"
                                md+="\n├≽ setmention: 「Text」"
                                md+="\n├≽ cek "
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "group" or cmd == "help grup":
                              if msg._from in admin:
                                md = "╭───「Set Group」"
                                md+="\n├≽ namagrup"
                                md+="\n├≽ potogrup"
                                md+="\n├≽ open"
                                md+="\n├≽ close"
                                md+="\n├≽ url"
                                md+="\n├≽ grouplist"
                                md+="\n├≽ changegroupname:「Text」"
                                md+="\n├≽ grouppicture"
                                md+="\n├≽ pendinglist"
                                md+="\n├≽ get note 「Num」"
                                md+="\n├≽ groupinfo "
                                md+="\n├≽ invite to group "
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "protect" or cmd == "help protect":
                              if msg._from in admin:
                                md = "╭───「 PROTECT 」"
                                md+="\n├≽ Allpro「On/Off」 "
                                md+="\n├≽ Protectqr「On/Off」 "
                                md+="\n├≽ Protectkick 「On/Off」 "
                                md+="\n├≽ Protectinvite 「On/Off」 "
                                md+="\n├≽ Protectjoin 「On/Off」 "
                                md+="\n├≽ Protectcancel 「On/Off」 "
                                md+="\n┝──「 Blacklist 」 "
                                md+="\n├≽ Kick 「@」 "
                                md+="\n├≽ Ban 「@」 "
                                md+="\n├≽ Unban 「@」 "
                                md+="\n├≽ Bl "
                                md+="\n├≽ Bc "
                                md+="\n├≽ Cb "
                                md+="\n├≽ Kickban "
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "friend" or cmd == "help friend":
                               if msg._from in admin:
                                md = "╭───「 Friend Message」"
                                md+="\n├≽ friendinfo 「Num」"
                                md+="\n├≽ delfriendmid 「mid」"
                                md+="\n├≽ friendlist"
                                md+="\n├≽ delfriend 「@」"
                                md+="\n├≽ blocklist"
                                md+="\n├≽ rename 「@」"
                                md+="\n├≽ add 「@」"
                                md+="\n├≽ block 「@」"
                                md+="\n├≽ unblock 「mid」"
                                md+="\n├≽ blockinfo 「 Num 」 "
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "cek":
                               if msg._from in admin:
                                md = "╭───「 Cek Message」"
                                md+="\n├≽ Cek Sider :\n{}\n".format(str(settings["mention"]))
                                md+="\n├≽ Cek Mention/Tag :\n{}\n".format(str(settings["taggal"]))
                                md+="\n├≽ Cek Respon Tag :\n{}\n".format(str(settings["autoResponMessage"]))
                                md+="\n├≽ Cek Pm Message :\n{}\n".format(str(wait["cekpc"]))
                                md+="\n├≽ Cek Welcome Msg : \n{}\n".format(str(settings["welcome"]))
                                md+="\n├≽ Cek Add Message : \n{}\n".format(str(settings["autoAddMessage"]))
                                md+="\n├≽ Cek Leave Message :\n{}\n".format(str(settings["leave"]))
                                md+="\n├≽ Cek Join Message : \n{}\n".format(str(settings["autoJoinMessage"]))
                                md+="\n├≽ Cek Like Message : \n{}\n".format(str(settings["commentPost"]))
                                md+="\n├≽ Cek Block Message : \n{}\n".format(str(settings["autoAddMessage"]))
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplate11(to, md)
                            elif terminal == "profile" or cmd == "help profile":
                              if msg._from in admin:
                                md = "╭───「 Profile Message」"
                                md+="\n├≽ changename: 「Text」"
                                md+="\n├≽ changebio 「Text」"
                                md+="\n├≽ check me "
                                md+="\n├≽ myprofile "
                                md+="\n├≽ mymid"
                                md+="\n├≽ myname"
                                md+="\n├≽ mybio"
                                md+="\n├≽ mypicture"
                                md+="\n├≽ myvideoprofile"
                                md+="\n├≽ mycover"
                                md+="\n├≽ mycover url"
                                md+="\n├≽ getmid 「@」"
                                md+="\n├≽ getcontact 「@」"
                                md+="\n├≽ getidline 「@」"
                                md+="\n├≽ getname 「@」"
                                md+="\n├≽ getbio 「@」"
                                md+="\n├≽ getpicture 「@」"
                                md+="\n├≽ getvideoprofile 「@」"
                                md+="\n├≽ getcover 「@」"
                                md+="\n├≽ all mid"
                                md+="\n├≽ changedual"
                                md+="\n├≽ changepict"
                                md+="\n├≽ changecover"
                                md+="\n├≽ changevp"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "spam" or cmd == "help spam":
                               if msg._from in admin:
                                md = "╭───「 Spam Message」"
                                md+="\n├≽ stag 「Jumlah + @」"
                                md+="\n├≽ scall 「Jumlah + @」"
                                md+="\n├≽ schat「On + Jumlah + Text」"
                                md+="\n├≽ sgift 「Jumlah + mid」"
                                md+="\n├≽ call 「Jumlah」"
                                md+="\n├≽ clear spam {rejetct spam}"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "media" or cmd == "help media":
                              if msg._from in admin:
                                md = "╭───「 Media Message」"
                                md+="\n├≽ musik「Judul」"
                                md+="\n├≽ mp3「Judul」"
                                md+="\n├≽ music 「Judul」"
                                md+="\n├≽ al-qur'an 「Nama surah」"
                                md+="\n├≽ murrotal"
                                md+="\n├≽ ayat sajadah"
                                md+="\n├≽ pulsk"
                                md+="\n├≽ listmeme"
                                md+="\n├≽ meme"
                                md+="\n├≽ fscosplay 「text」"
                                md+="\n├≽ fsv url 「text」"
                                md+="\n├≽ ss"
                                md+="\n├≽ decode"
                                md+="\n├≽ linedownload"
                                md+="\n├≽ linepost"
                                md+="\n├≽ newalbum"
                                md+="\n├≽ tiktok 「id」"
                                md+="\n├≽ artinama 「text」"
                                md+="\n├≽ artimimpi 「text」"
                                md+="\n├≽ ytmp3 「Judul」"
                                md+="\n├≽ ytmp4 「Judul」"
                                md+="\n├≽ ssweb 「link」"
                                md+="\n├≽ video 「Judul」"
                                md+="\n├≽ samehadaku 「name」"
                                md+="\n├≽ zodiak 「name」"
                                md+="\n├≽ praytime 「lokasi」"
                                md+="\n├≽ acaratv 「name」"
                                md+="\n├≽ tube 「Judul」"
                                md+="\n├≽ youtube 「Judul」"
                                md+="\n├≽ smulerecords 「id」"
                                md+="\n├≽ image 「Judul」"
                                md+="\n┝──────────────"
                                md+="\n╰─≽User:「 {} 」".format(client.getProfile().displayName)
                                sendTextTemplatey(to, md)
                            elif terminal == "remove":
                                client.removeAllMessages(op.param2)
                                sendTextTemplate(to, "Sukses Hps semua chat")

                            elif terminal == "status":
                                try:
                                    ret_ = "╭───「 Status Message 」"
                                    if settings["checkContact"] == True: ret_ += "\n├≽ Check Contact : ON"
                                    else: ret_ += "\n├≽ Check Contact : OFF"
                                    if settings["checkPost"] == True: ret_ += "\n├≽ Check Post : ON"
                                    else: ret_ += "\n├≽ Check Post : OFF"
                                    if settings["checkSticker"] == True: ret_ += "\n├≽ Check Sticker : ON"
                                    else: ret_ += "\n├≽ Check Sticker : OFF"
                                    if settings["unsendMessage"] == True: ret_ += "\n├≽ Unsend : ON"
                                    else: ret_ += "\n├≽ Unsend : OFF"
                                    if settings["setKey"] == True: ret_ += "\n├≽ Set Key : ON"
                                    else: ret_ += "\n├≽ Set Key : OFF"
                                    if settings["likeOn"] == True: ret_ += "\n├≽ Auto Like : ON"
                                    else: ret_ += "\n├≽ Auto Like : OFF"
                                    if settings["autoAdd"] == True: ret_ += "\n├≽ Auto Add : ON"
                                    else: ret_ += "\n├≽ Auto Add : OFF"
                                    if settings["autoBlock"] == True: ret_ += "\n├≽ Auto Block : ON"
                                    else: ret_ += "\n├≽ Auto Block : OFF"
                                    if settings["autoRespon"] == True: ret_ += "\n├≽ Auto Respon : ON"
                                    else: ret_ += "\n├≽ Auto Respon : OFF"
                                    if settings["autoReply"] == True: ret_ += "\n├≽ Auto Reply : ON"
                                    else: ret_ += "\n├≽ Auto Reply : OFF"
                                    if to in settings["sticker"] == True: ret_ += "\n├≽ Sticker : ON"
                                    else: ret_ += "\n├≽ Sticker : OFF"
                                    if to in settings["simiSimi"] == True: ret_ += "\n├≽ Simi Simi : ON"
                                    else: ret_ += "\n├≽ Simi Simi : OFF"
                                    if to in settings["sniff"] == True: ret_ += "\n├≽ Sniff Mode : ON"
                                    else: ret_ += "\n├≽ Sniff Mode : OFF"
                                    if settings["autoJoin"] == True: ret_ += "\n├≽ Auto Join : ON"
                                    else: ret_ += "\n├≽ Auto Join : OFF"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n├≽ Auto Join Ticket : ON"
                                    else: ret_ += "\n├≽ Auto Join Ticket : OFF"
                                    if settings["autoJoinTicketBot"] == True: ret_ += "\n├≽ Auto Join Ticket Bot : ON"
                                    else: ret_ += "\n├≽ Auto Join Ticket Bot : OFF"
                                    if settings["autoRead"] == True: ret_ += "\n├≽ Auto Read : ON"
                                    else: ret_ += "\n├≽ Auto Read : OFF"
                                    if msg.to in protectinvite: ret_ +="\n├≽ Protect Invite : ON"
                                    else: ret_ += "\n├≽ Protect Invite : OFF"
                                    if msg.to in protectqr: ret_ +="\n├≽ Protect Qr : ON"
                                    else: ret_ += "\n├≽ Protect Qr : OFF"
                                    if msg.to in protectjoin: ret_ +="\n├≽ Protect Join : ON"
                                    else: ret_ += "\n├≽ Protect Join : OFF"
                                    if msg.to in protectkick: ret_ +="\n├≽ Protect Kick : ON"
                                    else: ret_ += "\n├≽ Protect Kick : OFF"
                                    if msg.to in protectcancel: ret_ +="\n├≽ Protect Cancel : ON"
                                    else: ret_ += "\n├≽ Protect Cancel : OFF"
                                    ret_ += "\n╰───「 {} 」".format(client.getProfile().displayName)
                                    sendTextTemplate11(to, ret_)
                                except Exception as error:
                                    sendTextTemplate11(to, str(error))

                            elif terminal == "open":
                              if msg._from in clientMid:
                                if msg.toType == 2:
                                   X = client.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   client.updateGroup(X)
                                   sendTextTemplate(msg.to, "❂➣ Url Opened")

                            elif terminal == "close":
                              if msg._from in clientMid:
                                  if msg.toType == 2:
                                     X = client.getGroup(msg.to)
                                     X.preventedJoinByTicket = True
                                     client.updateGroup(X)
                                     sendTextTemplate(msg.to, "❂➣ Url Closed")

                            elif terminal == "url":
                              if msg._from in clientMid:
                                  if msg.toType == 2:
                                     x = client.getGroup(msg.to)
                                     if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        client.updateGroup(x)
                                     gurl = client.reissueGroupTicket(msg.to)
                                     client.sendReplyMessage(msg_id, to, "❂➣ Nama : "+str(x.name)+ "\n❂➣ Url grup : http://line.me/R/ti/g/"+gurl)                                                                                                                                              

                            elif terminal.startswith("friendbc: "):
                              if msg._from in owner or admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                contacts = client.getAllContactIds()
                                for contact in contacts:
                                    client.sendMessage(contact, "「 Bᵣₒₐdcₐₛₜ 」\n{}".format(str(txt)))
                                client.sendReplyMessage(msg_id, to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} ₜₑₘₐₙ".format(str(len(contacts))))

                            elif terminal.startswith("groupbc: "):
                              if msg._from in owner or admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                for group in groups:
                                    client.sendMessage(group, "「 Bᵣₒₐdcₐₛₜ 」\n{}".format(str(txt)))
                                client.sendReplyMessage(msg_id, to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} gᵣₒᵤₚ".format(str(len(groups))))
#=======================KICK OUT==============================================
                            elif terminal.startswith("kick "):
                              if sender in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.kickoutFromGroup(to, [ls])

                            elif terminal == "allmax":
                              if msg._from in clientMid:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    gMembers = [contact.mid for contact in group.members]
                                    for i in gMembers:
                                        client.kickoutFromGroup(to,[i])
                                    client.sendMessage(to,"See You Again T_T")
                                else:
                                    client.sendMessage(to,"Limit :-|")

                            elif terminal == "maxcancel":
                              if msg._from in admin or msg._from in Bots:
                                if msg.toType != 2: return client.sendMessage(to, 'Failed cancel all pending members, use this command only on group chat')
                                group = client.getCompactGroup(to)
                                if not group.invitee:
                                    return client.sendMessage(to, 'Failed cancel all pending members, no pending member in list')
                                for member in group.invitee:
                                    if member.mid == clientMid:
                                        continue
                                    try:
                                        client.cancelGroupInvitation(to, [member.mid])
                                    except TalkException as talk_error:
                                        return client.sendMessage(to, 'Failed cancel all pending members, the reason is `%s`' % talk_error.reason)
                                    time.sleep(0.4)
                                client.sendMessage(to, 'Success cancel all pending members, totals %i pending members' % len(pendings))
#========================BLACKLIST=============================================
                            elif terminal == "bancontact on":
                              if sender in admin:
                                settings["contactBan"] = True
                                sendTextTemplate(to, "Ban Contact\nSend the Contact")

                            elif terminal == "bancontact off":
                              if sender in admin:
                                if settings["contactBan"] == False:
                                    sendTextTemplate(to, "Contact Ban has been Aborted")
                                else:
                                    settings["contactBan"] = False
                                    sendTextTemplate(to, "Succesfully Aborted Ban Contact")

                            elif terminal == "unbancontact on":
                              if sender in admin:
                                settings["unbanContact"] = True
                                sendTextTemplate(to, "Unban Contact\n Send the Contact")

                            elif terminal == "unbancontact off":
                              if sender in admin:
                                if settings["unbanContact"] == False:
                                    sendTextTemplate(to, "Contact Ban has been Aborted")
                                else:
                                    settings["unbanContact"] = False
                                    sendTextTemplate(to, "Succesfully Aborted Ban Contact")

                            elif terminal.startswith("ban "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for list in lists:
                                        try:
                                            settings["blackList"][list] = True
                                            f=codecs.open('setting.json','w','utf-8')
                                            json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            sendTextTemplate(msg.to,"Berhasil menambahkan blacklist")
                                        except:
                                            pass
                                else:
                                    sendTextTemplate(to, "Succesfully add to Blacklist")

                            elif terminal.startswith("unban "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for list in lists:
                                        try:
                                            del settings["blackList"][list]
                                            f=codecs.open('setting.json','w','utf-8')
                                            json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            sendTextTemplate(msg.to,"Berhasil menghapus blacklist")
                                        except:
                                            pass
                                else:
                                    sendTextTemplate(to, "Succesfully Del in Blacklist")

                            elif terminal.startswith("cb"):   
                              if sender in admin:
                                settings["blackList"] = {}
                                sendTextTemplate(to, "Succesfully Clear Ban")            

                            elif terminal == "bl":
                              if msg._from in admin:
                                if settings["blackList"] == {}:
                                  sendTextTemplate(msg.to,"Tidak ada blacklist")
                                else:
                                  ma = ""
                                  a = 0
                                  for m_id in settings["blackList"]:
                                      a = a + 1
                                      end = '\n'
                                      ma += str(a) + ". " +client.getContact(m_id).displayName + "\n"
                                  sendTextTemplate(msg.to,"╭───「 Blacklist 」\n"+ma+"╰───「 Total %s Blacklist User 」" %(str(len(settings["blackList"]))))

                            elif terminal == "bc" or text.lower() == 'blc':
                              if msg._from in admin:
                                if settings["blackList"] == {}:
                                      sendTextTemplate(msg.to,"Tidak ada blacklist")
                                else:
                                      ma = ""
                                      for i in settings["blackList"]:
                                          ma = client.getContact(i)
                                          client.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                            elif text.lower() in ['kickban','killban']:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                for tag in settings["blackList"]:
                                    matched_list+=filter(lambda str: str == tag, gMembMids)
                                if matched_list == []:
                                    sendTextTemplate(msg.to,"There was no blacklist user")
                                    return
                                for jj in matched_list:
                                    client.kickoutFromGroup(msg.to,[jj])
                                sendTextTemplate(msg.to,"Blacklist kicked out")
#=====================================================================
                            elif terminal == "grouplist":
                                groups = client.getGroupIdsJoined()
                                ret_ = "╭───「 Group List 」"
                                no = 0
                                for gid in groups:
                                    group = client.getGroup(gid)
                                    no += 1
                                    ret_ += "\n├≽ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                ret_ += "\n╰───「 Total {} Group 」".format(str(len(groups)))
                                client.sendReplyMessage(msg_id, to, str(ret_))
                            elif terminal == "memberlist":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    num = 0
                                    ret_ = "╭───「 Member List 」"
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n├≽ {}. {}".format(num, contact.displayName)
                                    ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                    client.sendReplyMessage(msg_id, to, ret_)
                            elif terminal == "pendinglist":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╭───「 Pending List 」"
                                    no = 0
                                    if group.invitee is None or group.invitee == []:
                                        return client.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                    else:
                                        for pending in group.invitee:
                                            no += 1
                                            ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                        ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                        client.sendReplyMessage(msg_id, to, str(ret_))
#===============================MEDIA=============================================================
                            elif text.lower() == 'kalender':
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                                sendTextTemplate(msg.to, readTime)

                            elif cmd.startswith("broadcast: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                bc = text.replace(sep[0] + " ","")
                                saya = client.getGroupIdsJoined()
                                for group in saya:
                                   sendTextTemplate3(group, text)
                                   
                            elif terminal.startswith("soundcloud "):
                                def sdc():
                                    kitsunesplit = rynSplitText(msg.text.lower()).split(" ")
                                    r = requests.get('https://soundcloud.com/search?q={}'.format(rynSplitText(msg.text.lower())))
                                    soup = BeautifulSoup(r.text,'html5lib')
                                    data = soup.find_all(class_='soundTitle__titleContainer')
                                    data = soup.select('li > h2 > a')
                                    if len(kitsunesplit) == 1:
                                        a = '          🎺 NOTE PILIHAN LAGU 🎺\n____________________________________';no=0
                                        for b in data:
                                            no+=1
                                            a+= '\n{}. {}'.format(no,b.text)
                                        sendTextTemplate5(to,a)
                                    if len(kitsunesplit) == 2:
                                        a = data[int(kitsunesplit[1])-1];b = list(a)[0]
                                        kk = random.randint(0,999)
                                        sendTextTemplate5(to,'Judul: {}\nStatus: Waiting... For Upload'.format(a.text))
                                        hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                                        try:client.sendAudio(to,'{}.mp3'.format(kk))
                                        except Exception as e:sendTextTemplate(to,' 「 ERROR 」\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e))
                                        os.remove('{}.mp3'.format(kk))
                                ryn = Thread(target=sdc)
                                ryn.daemon = True
                                ryn.start()
                                ryn.join()
                                    
                            elif terminal == "autolike on":
                              if msg._from in admin:
                                if settings["likeOn"] == True:
                                    sendTextTemplate(to, "Auto like telah aktif")
                                else:
                                    settings["likeOn"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto like")
                                    
                            elif terminal == "autolike off":
                              if msg._from in admin:
                                if settings["likeOn"] == False:
                                    sendTextTemplate(to, "Auto like telah nonaktif")
                                else:
                                    settings["likeOn"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto like")

                            elif terminal == "autoblock on":
                              if msg._from in admin:
                                if settings["autoBlock"] == True:
                                    sendTextTemplate(to, "Auto block telah aktif")
                                else:
                                    settings["autoBlock"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto block")
                            elif terminal == "autoblock off":
                              if msg._from in admin:
                                if settings["autoBlock"] == False:
                                    sendTextTemplate(to, "Auto block telah nonaktif")
                                else:
                                    settings["autoBlock"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto block")
                                    
                            elif terminal == "autoadd on":
                              if msg._from in admin:
                                if settings["autoAdd"] == True:
                                    sendTextTemplate(to, "Auto add telah aktif")
                                else:
                                    settings["autoAdd"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto add")
                            elif terminal == "autoadd off":
                              if msg._from in admin:
                                if settings["autoAdd"] == False:
                                    sendTextTemplate(to, "Auto add telah nonaktif")
                                else:
                                    settings["autoAdd"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto add")
                            elif terminal == "autojoin on":
                              if msg._from in admin:
                                if settings["autoJoin"] == True:
                                    sendTextTemplate(to, "Auto join telah aktif")
                                else:
                                    settings["autoJoin"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join")
                            elif terminal == "autojoin off":
                              if msg._from in admin:
                                if settings["autoJoin"] == False:
                                    sendTextTemplate(to, "Auto join telah nonaktif")
                                else:
                                    settings["autoJoin"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join")

                            elif terminal == "autojointicket on":
                              if msg._from in admin:
                                if settings["autoJoinTicket"] == True:
                                    sendTextTemplate(to, "Auto join ticket telah aktif")
                                else:
                                    settings["autoJoinTicket"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join ticket")
                            elif terminal == "autojointicket off":
                              if msg._from in admin:
                                if settings["autoJoinTicket"] == False:
                                    sendTextTemplate(to, "Auto join ticket telah nonaktif")
                                else:
                                    settings["autoJoinTicket"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join ticket")

                            elif terminal == "autoread on":
                              if msg._from in admin:
                                if settings["autoRead"] == True:
                                    client.sendMessage(to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto read")
                            elif terminal == "autoread off":
                              if msg._from in admin:
                                if settings["autoRead"] == False:
                                    client.sendMessage(to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto read")

                            elif terminal == "respon on":
                              if msg._from in admin:
                                if settings["autoRespon"] == True:
                                    sendTextTemplate(to, "Auto respon telah aktif")
                                else:
                                    settings["autoRespon"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto respon")
                            elif terminal == "respon off":
                              if msg._from in admin:
                                if settings["autoRespon"] == False:
                                    sendTextTemplate(to, "Auto respon telah nonaktif")
                                else:
                                    settings["autoRespon"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto respon")

                            elif terminal == "autoreply on":
                              if msg._from in admin:
                                if settings["autoReply"] == True:
                                    sendTextTemplate(to, "Auto Reply telah aktif")
                                else:
                                    settings["autoReply"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto reply")
                            elif terminal == "autoreply off":
                              if msg._from in admin:
                                if settings["autoReply"] == False:
                                    sendTextTemplate(to, "Auto Reply telah nonaktif")
                                else:
                                    settings["autoReply"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto Reply")

                            elif terminal == "checkcontact on":
                              if msg._from in admin:
                                if settings["checkContact"] == True:
                                    sendTextTemplate(to, "Check details contact telah aktif")
                                else:
                                    settings["checkContact"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details contact")
                            elif terminal == "checkcontact off":
                              if msg._from in admin:                          
                                if settings["checkContact"] == False:
                                    sendTextTemplate(to, "Check details contact telah nonaktif")
                                else:
                                    settings["checkContact"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan Check details contact")

                            elif terminal == "checkpost on":
                              if msg._from in admin:                          
                                if settings["checkPost"] == True:
                                    sendTextTemplate(to, "Check details post telah aktif")
                                else:
                                    settings["checkPost"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details post")
                            elif terminal == "checkpost off":
                              if msg._from in admin:                          
                                if settings["checkPost"] == False:
                                    sendTextTemplate(to, "Check details post telah nonaktif")
                                else:
                                    settings["checkPost"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan check details post")

                            elif terminal == "checksticker on":
                              if msg._from in admin:
                                if settings["checkSticker"] == True:
                                    sendTextTemplate(to, "Check details sticker telah aktif")
                                else:
                                    settings["checkSticker"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details sticker")
                            elif terminal == "checksticker off":
                              if msg._from in admin:                          
                                if settings["checkSticker"] == False:
                                    sendTextTemplate(to, "Check details sticker telah nonaktif")
                                else:
                                    settings["checkSticker"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan check details sticker")

                            elif terminal == "sticker on":
                              if msg._from in admin:                          
                                if to in settings["sticker"]:
                                    sendTextTemplate(to, "Sticker telah aktif")
                                else:
                                    if to not in settings["sticker"]:
                                        settings["sticker"].append(to)
                                    sendTextTemplate(to, "Berhasil mengaktifkan sticker")
                            elif terminal == "sticker off":
                              if msg._from in admin:                          
                                if to not in settings["sticker"]:
                                    sendTextTemplate(to, "Sticker telah nonaktif")
                                else:
                                    if to in settings["sticker"]:
                                        settings["sticker"].remove(to)
                                    sendTextTemplate(to, "Berhasil menonaktifkan sticker")

                            elif terminal == "deletefriend on":
                              if msg._from in admin:                          
                                if settings["delFriend"] == True:
                                    sendTextTemplate(to, "Send Contact !!!!")
                                else:
                                    settings["delFriend"] = True
                                    sendTextTemplate(to, "Send Contact :)")
                            elif terminal == "deletefriend off":
                              if msg._from in admin:                          
                                if settings["delFriend"] == False:
                                    sendTextTemplate(to, "Udah Ga aktif !!!")
                                else:
                                    settings["delFriend"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan delete friend")

                            elif terminal == "autokick on":
                              if msg._from in owner or admin:                          
                                if protectGroup[to]["autoKick"] == True:
                                    sendTextTemplate(to, "Auto Kick telah aktif")
                                else:
                                    protectGroup[to]["autoKick"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan Auto Kick")
                            elif terminal == "autokick off":
                              if msg._from in owner or admin:                          
                                if protectGroup[to]["autoKick"] == False:
                                    sendTextTemplate(to, "Auto Kick telah nonaktif")
                                else:
                                    protectGroup[to]["autoKick"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto Kick")

                            elif 'Welcome ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Welcome ','')
                                 if spl == 'on':
                                     if msg.to in welcome:
                                          msgs = "❂➣ Welcome Msg sudah aktif"
                                     else:
                                          welcome.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Welcome Msg diaktifkan\n❂➣ Di Group :\n" +str(ginfo.name)
                                     sendTextTemplate(to, "❂➣ Diaktifkan\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in welcome:
                                            welcome.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Welcome Msg dinonaktifkan\n❂➣ Di Group :\n" +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Welcome Msg sudah tidak aktif"
                                       sendTextTemplate(to, "Dinonaktifkan\n" + msgs)

                            elif 'Protectqr ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectqr ','')
                                 if spl == 'on':
                                     if msg.to in protectqr:
                                          msgs = "❂➣ Protect url sudah aktif"
                                     else:
                                          protectqr.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                     sendTextTemplate(to, "「Diaktifkan」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectqr:
                                            protectqr.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Protect url sudah tidak aktif"
                                       sendTextTemplate(to, "「Dinonaktifkan」\n" + msgs)

                            elif 'Protectkick ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectkick ','')
                                 if spl == 'on':
                                     if msg.to in protectkick:
                                          msgs = "❂➣ Protect kick sudah aktif"
                                     else:
                                          protectkick.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                     sendTextTemplate(to, "「Diaktifkan」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectkick:
                                            protectkick.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Protect kick sudah tidak aktif"
                                       sendTextTemplate(to, "「Dinonaktifkan」\n" + msgs)

                            elif 'Protectinvite ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectinvite ','')
                                 if spl == 'on':
                                     if msg.to in protectinvite:
                                          msgs = "❂➣ Protect invite sudah aktif"
                                     else:
                                          protectinvite.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                     sendTextTemplate(to, "「Diaktifkan」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectinvite:
                                            protectinvite.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Protect invite sudah tidak aktif"
                                       sendTextTemplate(to,"「Dinonaktifkan」\n" + msgs)

                            elif 'Protectjoin ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectjoin ','')
                                 if spl == 'on':
                                     if msg.to in protectjoin:
                                          msgs = "❂➣ Protect join sudah aktif"
                                     else:
                                          protectjoin.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                     sendTextTemplate(to, "「Diaktifkan」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectjoin:
                                            protectjoin.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Protect join sudah tidak aktif"
                                       sendTextTemplate(to, "「Dinonaktifkan」\n" + msgs)

                            elif 'Protectcancel ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectcancel ','')
                                 if spl == 'on':
                                     if msg.to in protectinvite:
                                          msgs = "❂➣ Protect cancel sudah aktif"
                                     else:
                                          protectinvite.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                     sendTextTemplate(to, "「Diaktifkan」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectinvite:
                                            protectinvite.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Protect cancel sudah tidak aktif"
                                       sendTextTemplate(to, "「Dinonaktifkan」\n" + msgs)

                            elif 'Allpro ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Allpro ','')
                                 if spl == 'on':
                                     if msg.to in protectqr:
                                          msgs = ""
                                     else:
                                          protectqr.append(msg.to)
                                     if msg.to in protectkick:
                                         msgs = ""
                                     else:
                                         protectkick.append(msg.to)
                                     if msg.to in protectinvite:
                                         msgs = ""
                                     else:
                                         protectinvite.append(msg.to)
                                     if msg.to in protectcancel:
                                         ginfo = client.getGroup(msg.to)
                                         msgs = "❂➣ All protect sudah on\nDi Group : " +str(ginfo.name)
                                     else:
                                         protectcancel.append(msg.to)
                                         ginfo = client.getGroup(msg.to)
                                         msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                     sendTextTemplate(to, "「Diaktifkan」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectqr:
                                            protectqr.remove(msg.to)
                                       else:
                                            msgs = ""
                                       if msg.to in protectkick:
                                            protectkick.remove(msg.to)
                                       else:
                                            msgs = ""
                                       if msg.to in protectinvite:
                                            protectinvite.remove(msg.to)
                                       else:
                                            msgs = ""
                                       if msg.to in protectcancel:
                                            protectcancel.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                       else:
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ All protect sudah off\nDi Group : " +str(ginfo.name)
                                       sendTextTemplate(to, "「Dinonaktifkan」\n" + msgs)

                            elif terminal == "unsend on":
                              if msg._from in clientMid:
                                if settings["unsendMessage"] == True:
                                    sendTextTemplate(to, "unsendMessage telah aktif")
                                else:
                                    settings["unsendMessage"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan unsendMessage")
                            elif terminal == "unsend off":
                              if msg._from in clientMid:
                                if settings["unsendMessage"] == False:
                                    sendTextTemplate(to, "unsendMessage telah nonaktif")
                                else:
                                    settings["unsendMessage"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan unsendMessage")
#==================================================================================================================================
                            elif terminal.startswith("setautoadd: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAddMessage"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah pesan auto add menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah pesan auto add")

                            elif terminal.startswith("setautoblock: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoBlockMessage"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah pesan auto block menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah pesan auto block")
                                 
                            elif terminal.startswith("setmention: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["taggal"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah mention/tagall menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah mention/tagall ")
   
                            elif terminal.startswith("setrespon: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoResponMessage"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah text respon menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah text respon")

                            elif terminal.startswith("setautojoin: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoJoinMessage"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah pesan auto join menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah pesan auto join")
                                    
                            elif terminal.startswith("setsider: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["mention"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah text sider menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah text sider")
                          
                            elif terminal.startswith("setwelcome: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["welcome"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah text welcome menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah text welcome")
   
                            elif terminal.startswith("setleave: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["leave"] = txt
                                    sendTextTemplate(to, "Berhasil mengubah text leave menjadi : 「{}」".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah text leave")
                                    
                            elif terminal.startswith("setmember: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = int(sep[1])
                                try:
                                    settings["memberCancel"]["members"] = txt
                                    sendTextTemplate(to, "Succesfully set auto join group if mem {}".format(txt))
                                except:
                                    sendTextTemplate(to, "Gagal mengubah auto join group")

                            elif terminal.startswith("setautoanswerchat: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAnswerMessage"] = txt
                                    client.sendMessage(to, "Berhasil mengubah pesan auto answer menjadi : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Gagal mengubah pesan auto answer")

                            elif terminal.startswith("setcomment: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["commentPost"] = txt
                                    sendTextTemplate(to, "Succes\nComment : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Failed")
                            elif terminal.startswith("addsettings to "):
                              if sender in admin:
                                txt = removeCmd("addsettings to", text)
                                settings["{}".format(txt)] = []
                                f=codecs.open('setting.json','w','utf-8')
                                json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                client.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                            elif terminal.startswith("addsettings "):
                              if sender in admin:
                              	txt = removeCmd("addsettings", text)
                              	settings["{}".format(txt)] = False
                              	f=codecs.open('setting.json','w','utf-8')
                              	json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                              	client.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                            elif terminal.startswith("delsettings "):
                              if sender in admin:
                              	txt = removeCmd("delsettings", text)
                              	del settings["{}".format(txt)]
                              	client.sendReplyMessage(msg_id, to, "Succesfully del {} in settings".format(txt))

                            elif terminal == "myurl":
                              if msg._from in admin:
                                client.reissueUserTicket()
                                arr = client.profile.displayName + " Ticket URL : http://line.me/ti/p/" + client.getUserTicket().id
                                client.sendReplyMessage(msg_id, to, arr)

#===============================BAGIAN SPAM================================================================
                            elif terminal.startswith("spaminvmid"):
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                tar = dan[3]
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        Thread(target=client.inviteIntoGroup,args=(gcr.id, [tar]),).start()
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])

                            elif terminal.startswith("spaminvite"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        client.inviteIntoGroup(gcr.id, [tar])
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])
                                
                            elif terminal.startswith("chatowner: "):
                                contact = client.getContact(sender)
                                sep = text.split(" ")
                                ryan = text.replace(sep[0] + " ","")
                                for own in owner:
                                    result = "@!"
                                    result += "\nSender : {}".format(contact.displayName)
                                    result += "\nPesan : {}".format(ryan)
                                    result += "\nMid : {}".format(contact.mid)
                                    client.sendReplyMessage(msg_id, to, "Succesfully send chat to Owner")
                                    client.sendMention(own, result, [sender])
                                    client.sendContact(own, sender)

                            elif terminal.startswith("invtogc"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                grr = client.getGroupIdsJoined()
                                client.findAndAddContactsByMid(tar)
                                try:
                                    listGroup = grr[int(dan)-1]
                                    gri = client.getGroup(listGroup)
                                    client.inviteIntoGroup(gri.id, [tar])
                                    client.sendMessage(to, "Succesfully invite {} to group {}".format(tar.displayName, gri.name))
                                except Exception as e:
                                    client.sendMessage(to, str(e))

                            elif terminal.startswith('stag '):
                                sep = text.split(" ")
                                num = int(sep[1])                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            client.sendMention(to, "@!", [ls])

                            elif terminal.startswith('scall '):
                                sep = text.split(" ")
                                num = int(sep[1])
                                try:                           
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            for var in range(0,num):
                                                group = client.getGroup(to)
                                                members = [ls]
                                                kunkun = client.getContact("ud134cbd020e975960892558a13aa6dba").displayName
                                                client.acquireGroupCallRoute(to)
                                                client.inviteIntoGroupCall(to, contactIds=members)
                                            client.sendMention(to, "Succesfully Spamcall to @!", [ls])
                                except Exception as error:
                                    client.sendMessage(to, str(error))
          
                            elif terminal.startswith("schat"):
                              if sender in admin:
                                text = text.split(" ")
                                jmlh = int(text[2])
                                balon = jmlh * (text[3]+"\n")
                                if text[1] == "on":
                                    if jmlh <= 9999999:
                                        for x in range(jmlh):
                                            client.sendMessage(to, text[3])
                                    else:
                                        client.sendMention(to, "Sorry the amount is too much :) @!", [sender])
                                elif text[1] == "off":
                                  if jmlh <= 9999999:
                                    client.sendMessage(to, balon)
                                  else:
                                    client.sendMention(to, "Sorry the amount is too much :) @!", [sender])

                            elif terminal.startswith('sgift '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    txt = "~Gift~"
                                    client.sendMentionWithFooter(to, txt, "Succesfully Spam gift to your pc", [sender])
                                    for var in range(0,num):
                                       contact = client.getContact(sender)
                                       client.sendGift(contact.mid, random.choice(gf), "theme")                

                            elif terminal.startswith('call '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    sendTextTemplate(to, "Succesfully Spam Call to Group")
                                    for var in range(0,num):
                                       group = client.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       client.acquireGroupCallRoute(to)
                                       client.inviteIntoGroupCall(to, contactIds=members)
#================================================================================================================
                            elif terminal == "user list":
                                if admin == []:
                                   client.sendMessage(to, "User Is Empty")
                                else:
                                    client.sendMessage(to, "Wait...")
                                    user = ""
                                    user = "├≽ User List"
                                    for mid in owner:
                                        user += "\n├≽ "+client.getContact(mid).displayName
                                    user += "\n├≽ Finish"
                                    sendTextTemplate(to, user)

                            elif terminal == "admin list":
                                if admin == []:
                                   client.sendMessage(to, "Admin Is Empty")
                                else:
                                    client.sendMessage(to, "Wait........")
                                    user = ""
                                    user = "├≽ Admin List"
                                    for mid in admin:
                                        user += "\n├≽ "+client.getContact(mid).displayName
                                    user += "\n├≽» Finish"
                                    sendTextTemplate(to, user)
#=======================ADD- STICKER ==================================================================================
                            elif cmd == "tagpm":
                              if msg._from in admin:
                                profile = client.getContact(msg.to)
                                sendMention(msg.to, msg.to,"Halo ",wait["cekpc"])
                            elif cmd == "pcf":
                              if msg._from in admin:
                                contact = client.getContact(msg.to)
                                path =("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                client.sendReplyImageWithURL(msg.id, to, path)
                            elif cmd == "pcontact":
                              if msg._from in admin:
                                contact = client.getContact(msg.to)
                                mi_d = contact.mid
                                client.sendContact(msg.to, mi_d)
                            elif cmd == "pcc":
                              if msg._from in admin:
                                contact = client.getContact(msg.to)
                                cu = client.getProfileCoverURL(msg.to)
                                path = str(cu)
                                client.sendReplyImageWithURL(msg.id, to, path)
                            elif cmd == "pcn":
                              if msg._from in admin:
                                h = client.getContact(msg.to)
                                sendTextTemplate(to,"[ Your Name ]\n" + " " + h.displayName)
                            elif cmd == "pcb":
                              if msg._from in admin:
                                h = client.getContact(msg.to)
                                sendTextTemplate(to,"[ Your Bio ]\n" + " " +h.statusMessage)
                            elif cmd == "pcv":
                              if msg._from in admin:
                                h = client.getContact(msg.to)
                                if h.videoProfile == None:
                                	return sendTextTemplate(to, "Anda tidak memiliki video profile")
                                client.sendReplyVideoWithURL(msg.id, to, "http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                            elif cmd == "addresponsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "responSticker"
                                sendTextTemplate(to, "silahkan kirim stickernya")
                            elif cmd == "delresponsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["responSticker"] = None
                                sendTextTemplate(to, "Succes deleted sticker")
                            elif cmd == "addautoaddsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "addSticker"
                                sendTextTemplate(to, "silahkan kirim stickernya")
                            elif cmd == "delautoaddsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["addSticker"] = None
                                sendTextTemplate(to, "Succes deleted sticker")
                            elif cmd == "addsidersticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "readerSticker"
                                sendTextTemplate(to, "silahkan kirim stickernya")
                            elif cmd == "delsidersticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["readerSticker"] = None
                                sendTextTemplate(to, "Succes deleted sticker")
                            elif cmd == "addwelcomesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "welcomeSticker"
                                sendTextTemplate(to, "silahkan kirim stickernya")
                            elif cmd == "delwelcomesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["welcomeSticker"] = None
                                sendTextTemplate(to, "Success delete sticker")
                            elif cmd == "addleavesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "leaveSticker"
                                sendTextTemplate(to, "silahkan kirim stickernya")
                            elif cmd == "delleavesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["leaveSticker"] = None
                                sendTextTemplate(to, "Success delete sticker")
                            elif terminal.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = {}
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Send your stickers!")
                                else:
                                    sendTextTemplate(to, "Stickers name already in List!")                     

                            elif terminal.startswith("delsticker "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "Sticker itu tidak ada dalam list")

                            elif terminal == "list sticker":
                               if msg._from in admin:
                                 no = 0
                                 ret_ = "Daftar Sticker \n\n"
                                 for sticker in stickers:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\nTotal {} Stickers".format(str(len(stickers)))
                                 sendTextTemplate(to, ret_)
#============================ADD STICKER TEMPLATE====================================≠
                            elif terminal.startswith("addstp "):
                              ssn = client.getContact(sender).mid
                              ssnd.append(ssn)
                              if sender in ssnd:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addStickertemplate"]["statuss"] = True
                                    settings["addStickertemplate"]["namee"] = str(name.lower())
                                    stickerstemplate[str(name.lower())] = {}
                                    f = codecs.open('stickertemplate.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Send your stickers!")
                                else:
                                    sendTextTemplate(to, "Stickers name already in List!")

                            elif terminal.startswith("delstp "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickerstemplate:
                                    del stickerstemplate[str(name.lower())]
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Berhasil menghapus sticker\n {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "Sticker itu tidak ada dalam list")

                            elif terminal == "list stp":
                               if msg._from in admin:
                                 no = 0
                                 ret_ = "Daftar Sticker Template\n\n"
                                 for sticker in stickerstemplate:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\nTotal {} Stickers Template".format(str(len(stickers)))
                                 client.sendMessageWithFooter(to, ret_)
#============================================================================================
                            elif terminal.startswith("changekey"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                settings["tatan"] = "{}".format(txt)
                                client.sendReplyMessage(msg_id, to, "Succesfully Changekey with key >> {}".format(settings["tatan"]))

                            elif terminal.startswith("changename: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 999:
                                    profile = client.getProfile()
                                    profile.displayName = name
                                    client.updateProfile(profile)
                                    client.sendMessageWithFooter(to, "Berhasil mengubah nama menjadi : {}".format(name))
                              else:
                                  txt = ("Hmmmm gk bsa ya :(","Sorryy :(","Jgn Ubah Namaku :(")
                                  pop = random.choice(txt)
                                  client.sendMessageWithFooter(to, pop)

                            elif terminal.startswith("changebio: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 100000:
                                    profile = client.getProfile()
                                    profile.statusMessage = bio
                                    client.updateProfile(profile)
                                    client.sendMessageWithFooter(to, "Berhasil mengubah bio menjadi : {}".format(bio))

                            elif terminal == "check me":
                                client.sendMention(to, "@!", [sender])
                                client.sendFakeReplyContact(msg_id, to, sender)

                            elif terminal.startswith('myprofile'):
                                textt = removeCmd(text, setKey)
                                texttl = textt.lower()
                                profile = client.getProfile()
                                res = '╭───「 My Profile 」'
                                res += '\n├ MID : ' + profile.mid
                                res += '\n├ Display Name : ' + str(profile.displayName)
                                res += '\n├ Status Message : ' + str(profile.statusMessage)
                                res += '\n├ Usage : '
                                res += '\n│ • {key}MyProfile'
                                res += '\n│ • {key}MyProfile MID'
                                res += '\n│ • {key}MyProfile Name'
                                res += '\n│ • {key}MyProfile Bio'
                                res += '\n│ • {key}MyProfile Pict'
                                res += '\n│ • {key}MyProfile Cover'
                                res += '\n│ • {key}MyProfile Change Name <name>'
                                res += '\n│ • {key}MyProfile Change Bio <bio>'
                                res += '\n│ • {key}MyProfile Change Pict'
                                res += '\n│ • {key}MyProfile Change Cover'
                                res += '\n╰───「 ＢＹ ＭＡＸ 」'
                                if terminal == 'myprofile':
                                    if profile.pictureStatus:
                                        client.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                                    cover = client.getProfileCoverURL(profile.mid)
                                    client.sendImageWithURL(to, str(cover))
                                    client.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))

                            elif terminal == "mymid":
                                contact = client.getContact(sender)
                                client.sendMention(to, "@!\n{}".format(contact.mid), [sender])

                            elif terminal == "myname":
                                contact = client.getContact(sender)
                                client.sendMention(to, "@!\n{}".format(contact.displayName), [sender])

                            elif terminal == "mybio":
                                contact = client.getContact(sender)
                                client.sendMention(to, "@!\n{}".format(contact.statusMessage), [sender])

                            elif terminal == "mypicture":
                                contact = client.getContact(sender)
                                client.sendReplyImageWithURL(msg_id, to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                            elif terminal == "myvideoprofile":
                                contact = client.getContact(sender)
                                if contact.videoProfile == None:
                                    return client.sendMessage(to, "Anda tidak memiliki video profile")
                                client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                            elif terminal == "mycover":
                                cover = client.getProfileCoverURL(sender)
                                client.sendImageWithURL(to, str(cover))

                            elif terminal == "mycover url":
                                cover = client.getProfileCoverURL(sender)
                                client.sendMessage(to, str(cover))

                            elif terminal.startswith("getmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.sendMention(to, "@!: \n{}".format(ls), [ls])

                            elif terminal.startswith("getcontact "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.sendContact(to, txt)

                            elif terminal.startswith("getidline "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        checkticket = client.getContact(ls).userid
                                        client.sendMention(to, "@!: {}".format(checkticket), [ls])

                            elif terminal.startswith("getname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMention(to, "@!: {}".format(contact.displayName), [ls])

                            elif terminal.startswith("getbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMention(to, "@!: {}".format(contact.statusMessage), [ls])

                            elif terminal.startswith("getpicture "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                            elif terminal.startswith("getvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        if contact.videoProfile == None:
                                            return client.sendMention(to, "@!tidak memiliki video profile", [ls])
                                        client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                            elif terminal.startswith("getcover "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cover = client.getProfileCoverURL(ls)
                                        client.sendImageWithURL(to, str(cover))

                            elif terminal.startswith("cloneprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.cloneContactProfile(ls)
                                        client.sendContact(to, sender)
                                        client.sendMessage(to, "Berhasil clone profile")

                            elif terminal == "invite to group":
                              if msg._from in admin:
                                if settings["groupInvite"] == True:
                                    sendTextTemplate(to, "Kirim Kontaknya :)")
                                else:
                                    settings["groupInvite"] = True
                                    sendTextTemplate(to, "Send Contact :)")

                            elif terminal == "friendlist":
                              if msg._from in admin:
                                contacts = client.getAllContactIds()
                                num = 0
                                result = "╭───「 Friend List 」"
                                for listContact in contacts:
                                    contact = client.getContact(listContact)
                                    num += 1
                                    result += "\n├≽ {}. {}".format(num, contact.displayName)
                                result += "\n╰───「 Total {} Friend 」".format(len(contacts))
                                client.sendReplyMessage(msg_id, to, result)

                            elif terminal.startswith("friendinfo "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                contacts = client.getAllContactIds()
                                try:
                                    listContact = contacts[int(query)-1]
                                    contact = client.getContact(listContact)
                                    cover = client.getProfileCoverURL(listContact)
                                    result = "╭───「 Details Profile 」"
                                    result += "\n├≽ Display Name : @!"
                                    result += "\n├≽ Mid : {}".format(contact.mid)
                                    result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                                    result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                    result += "\n├≽ Cover : {}".format(str(cover))
                                    result += "\n╰───「 Finish 」"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                    client.sendMention(to, result, [contact.mid])
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("delfriendmid "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.deleteContact(txt)
                                client.sendFakeMessage(to, "Done",txt)

                            elif terminal.startswith("delfriend "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.deleteContact(ls)
                                        client.sendReplyMessage(msg_id, to, "Udah euy")

                            elif terminal.startswith("addfavorite "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.addFavorite(ls)
                                        client.sendReplyMention(msg_id, to, "Succesfully add @! to Favorite Friend", [ls])

                            elif terminal.startswith("rename "):
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.renameContact(ls,sep[1])
                                        client.sendReplyMention(msg_id, to, "Succesfully change @! display name to {}".format(sep[1]), [ls])

                            elif terminal == "blocklist":
                              if msg._from in admin:
                                blockeds = client.getBlockedContactIds()
                                num = 0
                                result = "╭───「 Block List 」"
                                for listBlocked in blockeds:
                                    contact = client.getContact(listBlocked)
                                    num += 1
                                    result += "\n├≽ {}. {}".format(num, contact.displayName)
                                result += "\n╰───「 Total {} Blocked 」".format(len(blockeds))
                                client.sendMessage(to, result)

                            elif terminal.startswith("changegroupname: "):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    groupname = text.replace(sep[0] + " ","")
                                    if len(groupname) <= 100:
                                        group = client.getGroup(to)
                                        group.name = groupname
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))

                            elif terminal.startswith("no"):
                                sep = text.split("|")
                                nom = sep[1]
                                nam = sep[2]
                                client.sendContactHP(to, "Kntlll", nom, nam)
                            elif terminal == "foot":
                                con = {'AGENT_ICON': 'http://profile.line-cdn.net/0hcr26oFItPF0PTxGrOrtDCjMKMjB4YToVdyx1MypOZmR1LXMPMiF2b31GMD5xfSgPZCogOC1GZmwq', 'AGENT_NAME': 'Runtime', 'AGENT_LINK': 'line://app/1600328768-y3yq64nw/?type=text&text=runtime'}
                                client.sendMessage(to, "LKJ", con, 0)

                            elif terminal == "grouppicture":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
                                    client.sendImageWithURL(to, groupPicture)

                            elif terminal == "all mid":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    num = 0
                                    ret_ = "╭───「 Mid List On Group {} 」".format(group.name)
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n├≽ {}.{}\n├{}".format(num, contact.displayName, contact.mid)
                                    ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                    client.sendReplyMessage(msg_id, to, ret_)

                        ## Remote
                            elif terminal.startswith("leavegc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.leaveGroup(group.id)
                                    client.sendMessage(to, "Succesfully leave to Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("sendctogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.sendContact(group.id, "ube7e5b15dbea0cc92f2067c04d25b1fc")
                                    client.sendMessage(to, "Succesfully send Crash to Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("invitetogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.inviteIntoGroup(group.id, [sender])
                                    client.sendMention(to, "Succesfully invite @! to Group {}".format(group.name), [sender])
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("mutebotingc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    if group not in offbot:
                                      client.sendMessageWithFooter(to, "Berhasil Mure Bot Di Group {}".format(group.name))
                                      offbot.append(group.id)
                                      print(group.id)
                                    else:
                                      client.sendMessageWithFooter(to, "Failed Mute Bot In Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("unmutebotingc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                listGroup = groups[int(query)-1]
                                group = client.getGroup(listGroup)
                                if group.id in offbot:
                                    offbot.remove(group.id)
                                    client.sendMessageWithFooter(to, "Berhasil Unmute Bot Di Group {}".format(group.name))
                                    print(group.id)
                                else:
                                    client.sendMessageWithFooter(to, "Failed Unmute Bot In Group {}".format(group.name))

                            elif terminal.startswith("chattogc"):
                              if sender in admin:
                                dan = text.split("-")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(dan[1])-1]
                                    group = client.getGroup(listGroup)
                                    client.sendMessage(group.id, dan[2])
                                except:
                                    pass

                            elif terminal.startswith("chattofr"):
                              if sender in admin:
                                dan = text.split("-")
                                frs = client.getAllContactIds()
                                try:
                                    listFriend = frs[int(dan[1])-1]
                                    friend = client.getContact(listFriend)
                                    client.sendMessage(friend.mid, dan[2])
                                except:
                                    pass

                            elif terminal.startswith("sendgifttogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    client.sendGift(group.id, random.choice(gf), "theme")
                                    txt = "「 Gift 」"
                                    client.sendMentionWithFooter(to, txt, "Succesfully send gift to Group {} :)".format(group.name), [sender])
                                except:
                                    pass

                            elif terminal.startswith("get note"):
                                data = client.getGroupPost(to)
                                try:
                                    music = data['result']['feeds'][int(text.split(' ')[2]) - 1]
                                    b = [music['post']['userInfo']['writerMid']]
                                    try:
                                        for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                                    except:pass
                                    try:
                                        g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                                    except:
                                        g=""
                                    a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                                    a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                                    gtime = music['post']['postInfo']['createdTime']
                                    a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                    a += g
                                    zx = ""
                                    zxc = " 「 Groups 」\nType: Get Note\n   Penulis : "+a
                                    try:
                                        client.sendReplyMessage(msg_id, to, zxc)
                                    except Exception as e:
                                        client.sendMessage(to, str(e))
                                    try:
                                        for c in music['post']['contents']['media']:
                                            params = {'userMid': client.getProfile().mid, 'oid': c['objectId']}
                                            path = client.server.urlEncode(client.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                                            if 'PHOTO' in c['type']:
                                                try:
                                                    client.sendImageWithURL(to,path,'POST')
                                                except:pass
                                            else:
                                                pass
                                            if 'VIDEO' in c['type']:
                                                try:
                                                    client.sendVideoWithURL(to,path)
                                                except:pass
                                            else:
                                                pass
                                    except:
                                        pass
                                except Exception as e:
                                    return sendTextTemplate(to,"「 Auto Respond 」\n"+str(e))
                            
                            elif cmd == "groupinfo":
                              if msg._from in admin:
                                try:
                                    G = client.getGroup(msg.to)
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket == True:
                                        gQr = "𝚃𝙴𝚁𝚃𝚄𝚃𝚄𝙿"
                                        gTicket = "𝚃𝙸𝙳𝙰𝙺 𝙰𝙳𝙰"
                                    else:
                                        gQr = "𝚃𝙴𝚁𝙱𝚄𝙺𝙰"
                                        gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(time.strftime("%d-%m-%Y「 %H:%M:%S 」", time.localtime(int(G.createdTime) / 1000)))
                                    client.sendReplyMessage(msg_id, to, "• 𝙶𝚁𝙾𝚄𝙿𝙸𝙽𝙵𝙾\n\n• 𝙽𝙰𝙼𝙰 𝙶𝚁𝙾𝚄𝙿 : {}".format(G.name)+ "\n• 𝙸𝙳 𝙶𝚁𝙾𝚄𝙿 : {}".format(G.id)+ "\n• 𝙿𝙴𝙼𝙱𝚄𝙰𝚃 : {}".format(G.creator.displayName)+ "\n• 𝙲𝚁𝙴𝙰𝚃𝙸𝙾𝙽 𝚃𝙸𝙼𝙴 : {}".format(str(timeCreated))+ "\n• 𝙹𝚄𝙼𝙻𝙰𝙷 𝙼𝙴𝙼𝙱𝙴𝚁 : {}".format(str(len(G.members)))+ "\n• 𝙹𝚄𝙼𝙻𝙰𝙷 𝙿𝙴𝙽𝙳𝙸𝙽𝙶 : {}".format(gPending)+ "\n• 𝙶𝚁𝙾𝚄𝙿 𝚀𝚁 : {}".format(gQr)+ "\n• 𝙶𝚁𝙾𝚄𝙿 𝚃𝙸𝙲𝙺𝙴𝚃 : {}".format(gTicket))
                                    client.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                    client.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                                except Exception as e:
                                    sendTextTemplate(msg.to, str(e))

                            elif terminal.startswith("groupvideocall "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                num = int(txt)
                                client.sendMessage(to, "Berhasil Invite Ke Dalam VideoCall Group :)")
                                for anu in range(0,num):
                                    group = client.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    client.inviteIntoGroupVideoCall(to, contactIds=members)

                            elif terminal == "tag -1":
                              if msg._from in admin:
                                client.unsendMessage(msg.id)
                                try:group = client.getGroup(msg.to);nama = [contact.mid for contact in group.members];nama.remove(client.getProfile().mid)
                                except:group = client.getRoom(msg.to);nama = [contact.mid for contact in group.contacts]
                                k = len(nama)//20
                                for a in range(k+1):
                                    if a == 0:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                    else:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='├「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)

                            elif terminal == "tag":
                                try:group = client.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = client.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭───「 Mention Members 」"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├≽ {}. @!".format(str(no))
                                        ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                        client.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├≽ {}. @!".format(str(no))
                                        ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                        client.sendReplyMention(msg_id, to, ret_, dataMid)

                            elif terminal == "sider on":
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate8(to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                            elif terminal == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate8(to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate8(to, "Sudak tidak aktif")

                            elif terminal == "lurking on":
                              if msg._from in owner or admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to in read['readPoint']:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    sendTextTemplate3(to, "Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    sendTextTemplate3(to, "Set reading point : \n{}".format(readTime))
                            elif terminal == "lurking off":
                              if msg._from in owner or admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to not in read['readPoint']:
                                    sendTextTemplate(to,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    sendTextTemplate3(to, "Delete reading point : \n{}".format(readTime))
                            elif "lurking" in msg.text.lower():
                              if msg._from in owner or admin:
                                if to in read['readPoint']:
                                    if read["readMember"][to] == []:
                                        return sendTextTemplate3(to, "Tidak Ada Sider")
                                    else:
                                        no = 0
                                        result = "╭───「 Reader 」"
                                        for dataRead in read["readMember"][to]:
                                            no += 1
                                            result += "\n├≽ {}. @!".format(str(no))
                                        result += "\n╰───「 Total {} Sider 」".format(str(len(read["readMember"][to])))
                                        client.sendMention(to, result, read["readMember"][to])
                                        read['readMember'][to] = []

                            elif terminal == "clonecontact":
                              if msg._from in admin:
                                settings["cloneContact"] = True
                                client.sendMessageWithFooter(to, "Silahkan Kirim Contactnya :)")
                            elif terminal == "clone contact off":
                                if settings["cloneContact"] == False:
                                    sendTextTemplate(to, "Clone Contact Has been Aborted")
                                else:
                                    settings["cloneContact"] = False
                                    sendTextTemplate(to, "Succesfully Aborted \n\nClone Contact Profile")

                            elif terminal == "changedual":
                                settings["changeDual"] = True
                                sendTextTemplate(to, "Send Vidd :)")

                            elif terminal == "allcvp off":
                              if sender in admin:
                                if settings["allchangedual"] == False:
                                    client.sendMessage(to, "CVP Has Been Aborted")
                                else:
                                    settings["allchangedual"] = False
                                    client.sendMessage(to, "Succesfully Aborted \n\nChange Video & Picture")

                            elif terminal == "cvp off":
                                if settings["changeDual"] == False:
                                    client.sendMessage(to, "CVP Has Been Aborted")
                                else:
                                    settings["changeDual"] = False
                                    client.sendMessage(to, "Succesfully Aborted \n\nChange Video & Picture")

                            elif terminal == "changepict":
                              if msg._from in admin:
                                settings["changePictureProfile"] = True
                                client.sendMessage(to, "Silahkan kirim gambarnya")

                            elif terminal == "changecover":
                              if sender in admin:
                                settings["changeCover"] = True
                                client.sendMessage(to, "Send Pict :)")

                            elif terminal == "changevp":
                              if msg._from in admin:
                                settings["changeVpProfile"] = True
                                client.sendMessage(to, "Silahkan kirim Videonya")

                            elif terminal == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    sendTextTemplate(to, "Silahkan kirim gambarnya")
                            elif terminal == "mimic on":
                                if settings["mimic"]["status"] == True:
                                    sendTextTemplate(to, "Reply message telah aktif")
                                else:
                                    settings["mimic"]["status"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan reply message")
                            elif terminal == "mimic off":
                              if msg._from in admin:
                                if settings["mimic"]["status"] == False:
                                    client.sendMessage(to, "Reply message telah nonaktif")
                                else:
                                    settings["mimic"]["status"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan reply message")
                            elif terminal == "mimiclist":
                              if msg._from in admin:
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(to, "Tidak Ada Target")
                                else:
                                    no = 0
                                    result = "╭───「 Mimic List 」"
                                    target = []
                                    for mid in settings["mimic"]["target"]:
                                        target.append(mid)
                                        no += 1
                                        result += "\n├≽ {}. @!".format(no)
                                    result += "\n╰───「 Total {} Mimic 」".format(str(len(target)))
                                    client.sendMention(to, result, target)
                            elif terminal.startswith("mimicadd "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls in settings["mimic"]["target"]:
                                                client.sendMessage(to, "Target sudah ada dalam list")
                                            else:
                                                settings["mimic"]["target"][ls] = True
                                                client.sendMessage(to, "Berhasil menambahkan target")
                                        except:
                                            client.sendMessage(to, "Gagal menambahkan target")
                            elif terminal.startswith("mimicdel "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls not in settings["mimic"]["target"]:
                                                client.sendMessage(to, "Target sudah tida didalam list")
                                            else:
                                                del settings["mimic"]["target"][ls]
                                                client.sendMessage(to, "Berhasil menghapus target")
                                        except:
                                            client.sendMessage(to, "Gagal menghapus target")

                            elif terminal.startswith("praytime "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0]+ " ","")
                                url = requests.get("https://time.siswadi.com/pray/{}".format(txt))
                                data = url.json()
                                ret_ = "╭───「 Praytime at {} 」".format(txt)
                                ret_ += "\n├≽ Date : {}".format(data["time"]["date"])
                                ret_ += "\n├≽ Subuh : {}".format(data["data"]["Fajr"])
                                ret_ += "\n├≽ Dzuhur : {}".format(data["data"]["Dhuhr"])
                                ret_ += "\n├≽ Ashar : {}".format(data["data"]["Asr"])
                                ret_ += "\n├≽ Magrib : {}".format(data["data"]["Maghrib"])
                                ret_ += "\n├≽ Isha : {}".format(data["data"]["Isha"])
                                ret_ += "\n├≽ 1/3 Malam : {}".format(data["data"]["SepertigaMalam"])
                                ret_ += "\n├≽ Tengah Malam : {}".format(data["data"]["TengahMalam"])
                                ret_ += "\n├≽ 2/3 Malam : {}".format(data["data"]["DuapertigaMalam"])
                                ret_ += "\n├≽ 「 Always Remember to Your God :) 」"
                                ret_ += "\n╰───「 {} 」".format(txt)
                                client.sendMessageWithFooter(to, str(ret_))
                                address = ''.format(data["location"]["address"])
                                latitude = float(data["location"]["latitude"])
                                longitude = float(data["location"]["longitude"])
                                client.sendLocation(to, address,latitude,longitude)

                            elif terminal.startswith("acaratv "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/acaratv.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=separate".format(txt))
                                data = url.json()
                                no = 0
                                result = "╭───「 Acara TV 」"
                                for anu in data:
                                    no += 1
                                    result += "\n├≽ {}. {} >>> {} ".format(str(no),str(anu["acara"]),str(anu["jam"]))
                                result += "\n╰───「 Acara TV 」"
                                sendTextTemplate(to, result)

                            elif terminal.startswith("zodiak "):
                              if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                data1 = data["description"]
                                data2 = data["color"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest='id')
                                hasil1 = translator.translate(data2, dest='id')
                                A = hasil.text
                                B = hasil1.text
                                ret_ = "♟ Ramalan zodiak {} hari ini ♟\n".format(str(query))
                                ret_ += str(A)
                                ret_ += "\n======================\n♟ Tanggal : " +str(data["current_date"])
                                ret_ += "\n♟ Rasi bintang : "+query
                                ret_ += " ("+str(data["date_range"]+")")
                                ret_ += "\n♟ Pasangan Zodiak : " +str(data["compatibility"])
                                ret_ += "\n♟ Angka keberuntungan : " +str(data["lucky_number"])
                                ret_ += "\n♟ Waktu keberuntungan : " +str(data["lucky_time"])
                                ret_ += "\n♟ Warna kesukaan : " +str(B)
                                client.sendMessage(to, str(ret_))

                            elif terminal.startswith("samehadaku "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/samehadaku.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba".format(txt))
                                data = url.json()
                                no = 0
                                result = "╭───「 Samehadaku 」"
                                for anu in data:
                                    no += 1
                                    result += "\n├≽ {}. {}".format(str(no),str(anu["title"]))
                                    result += "\n├≽ {}".format(str(anu["url"]))
                                    result += "\n├≽ {}".format(str(anu["date"]))
                                result += "\n╰───「 {} Anime 」".format(str(len(data)))
                                sendTextTemplate(to, result)

                            elif terminal.startswith("mtoh "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/v1/gToH?date={}".format(txt))
                                data = url.json()
                                result = "~ Hijriah ~ = {}".format(str(data["data"]["hijri"]["date"]))
                                result += "\n~ Masehi ~ = {}".format(str(data["data"]["gregorian"]["date"]))
                                sendTextTemplate(to, result)

                            elif terminal.startswith("asmaulhusna"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/asmaAlHusna/{}".format(txt))
                                data = url.json()
                                result = "~ Asma Allah ke {} = ~ {} ~".format(txt,data["data"][0]["name"])
                                result += "\n~Artinya =~ {} ~".format(data["data"][0]["en"]["meaning"])
                                sendTextTemplate(to, result)

                            elif terminal.startswith("al-qur'an"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                                data = web.json()
                                result = "╭───「 {} 」".format(data["data"]["englishName"])
                                quran = data["data"]
                                result += "\n├≽ Surah ke「 {} 」".format(quran["number"])
                                result += "\n├≽ Nama Surah「 {} 」".format(quran["name"])
                                result += "\n├≽ {} Ayat •".format(quran["numberOfAyahs"])
                                result += "\n├≽ {} •".format(quran["name"])
                                result += "\n├≽ Ayat Sajadah 「 {} 」".format(quran["ayahs"][0]["sajda"])
                                result += "\n╰────────────\n"
                                no = 0
                                for ayat in data["data"]["ayahs"]:
                                    no += 1
                                    result += "\n{}. {}".format(no,ayat['text'])
                                k = len(result)//10000
                                for aa in range(k+1):
                                    client.sendMessage(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))

                            elif terminal.startswith("murrotal"):
                                try:
                                    sep = text.split(" ")
                                    txt = int(text.replace(sep[0] + " ",""))
                                    if 0 < txt < 115:
                                        if txt not in [2,3,4,5,6,7,9,10,11,12,16,17,18,20,21,23,26,37]:
                                            if len(str(txt)) == 1:
                                                audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                            elif len(str(txt)) == 2:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                            else:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                        else:
                                            client.sendMessage(to, "The Surah is too long")
                                    else:
                                        client.sendMessage(to, "Holy Qur'an Only have 114 surah :)")
                                except Exception as error:
                                    client.sendMessage(to, "error\n"+str(error))
                                    logError(error)

                            elif terminal == "ayat sajadah":
                                url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                                data = url.json()
                                result = "╭───「 Ayat Sajadah 」"
                                for ayat in data["data"]["ayahs"]:
                                    ayatnya = ayat["text"]
                                    result += "\n├≽ {}".format(ayatnya)
                                    result += "\n├≽ Surah {}".format(ayat["surah"]["englishName"])
                                result += "\n ╰───「 Juz {} 」".format(ayat["juz"])
                                sendTextTemplate(to, result)

                            elif terminal == "pulsk":                                
                                r = requests.get("https://farzain.com/api/pulsk.php?apikey=oQ61nCJ2YBIP1qH25ry6cw2ba")
                                data=r.text
                                data=json.loads(data)
                                if data != []:    
                                    no = 0
                                    hasil = "[ Pulsk Result ]"
                                    for sam in data:                                     
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". " + str(sam["title"])+"\n"+ str(sam["link"])+"\n"+ str(sam["views"])+"\n"+ str(sam["share"])
                                    client.sendMessageWithFooter(to, str(hasil))
                            elif terminal.startswith("listmeme"):
                              if msg._from in admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "♟ Daftar Meme Image ♟\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    client.sendMessage(to,hasil)
                                    client.sendMention(to, "\nJika ingin menggunakan, \nSilahkan ketik:\n\n♟ Listmeme | urutan\n♟ Meme text1 | text2 | urutan", [sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        client.sendMention(to, "♟ Meme Image ♟\nTunggu \nFoto sedang diproses...", [sender])
                                        client.sendMessage(to, hasil)
                                        client.sendImageWithURL(to, gambar["url"])
                                    except Exception as e:
                                        client.sendMessage(to," "+str(e))
                            elif terminal.startswith("meme "):  
                                if msg._from in admin:
                                    code = msg.text.split(" ")
                                    txt = msg.text.replace(code[0] + "/" + " ","")
                                    txt2 = msg.text.replace(txt[0] + "/" + " ","")
                                    naena = "https://api.imgflip.com/"+txt2+".jpg"
                                    try:
                                         start = time.time()
                                         client.sendMessage(to,"🍀Meme Image🍀\nType : Meme Image\nTime taken : %s seconds" % (start))
                                         client.sendImageWithURL(to, naena)
                                    except Exception as error:
                                         client.sendMessage(to, str(error))
                            elif terminal.startswith("fscosplay "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "http://farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=ppqeuy&text={}".format(txt)
                                client.sendImageWithURL(to, url)
                            elif terminal.startswith("fsv "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=ppqeuy&text={}".format(txt)
                                client.sendImageWithURL(to, url)
                            elif terminal == "ss":
                                group = client.getGroup(to)
                                url = "api.echobots.net/screenshot/put/{}".format(group.id)
                                Thread(target=client.sendImageWithURL,args=(to, url,)).start()
                            elif terminal.startswith("decode "):
                            	txt = removeCmd("decode", text)
                            	url = urlDecode(txt)
                            	client.sendReplyMessage(msg_id, to, url)
                            elif terminal.startswith("encode "):
                            	txt = removeCmd("encode", text)
                            	url = urlEncode(txt)
                            	client.sendReplyMessage(msg_id, to, url)
                            elif terminal.startswith("ssweb "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://api.site-shot.com//?url={}&width=1280&height=2080&5ba006ea23010.jpg".format(txt)
                                Thread(target=client.sendImageWithURL,args=(to, url,)).start()
                            elif terminal.startswith("linedownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.sendImageWithURL(to, txt)
                                client.sendVideoWithURL(to, txt)
                            elif terminal.startswith("linepost "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/special/line.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, data["result"])
                                client.sendVideoWithURL(to, data["result"])
                            elif terminal.startswith("newalbum "):
                            	txt = removeCmd("newalbum", text)
                            	url = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_search?country=id&lang=en&search_input={}&sin=0&ein=30".format(txt))
                            	data = url.json()
                            	urlv = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_album_singer?country=id&lang=en&cmd=1&sin=0&ein=2&singerid={}".format(data["itemlist"][0]["singerid"]))
                            	datav = url.json()
                            	tex = "╭───「 New Album 」"
                            	tex += "\n├≽ Name : {}".format(urlDecode(datav["name"]))
                            	tex += "\n├≽ Song : {}".format(datav["songnum"])
                            	tex += "\n├≽ Album: {}".format(datav["albumnum"])
                            	tex += "\n╰───「 {} 」".format(urlDecode(datav["name"]))
                            	client.sendReplyImageWithURL(msg_id, to, datav["pic"])
                            	client.sendReplyMessage(msg_id, to, tex)
                            elif terminal.startswith("tiktok"):
                            	def tiktoks():
                            		try:
		                                url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=json")
		                                data = url.json()
		                                client.sendVideoWithURL(to, data["first_video"])
                            		except:
		                            	client.sendMessage(to, data["result"])
                            	ryn = Thread(target=tiktoks)
                            	ryn.daemon = True
                            	ryn.start()
                            elif terminal.startswith("artinama "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://api.eater.site/api/name/?apikey=beta&name={}".format(txt))
                                data = url.json()
                                client.sendMessageWithFooter(to, str(data["result"][0]["name"]))
                            elif terminal.startswith("artimimpi "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/mimpi.php?q={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba".format(txt))
                                data = url.json()
                                client.sendMessageWithFooter(to, str(data["result"]))

                            elif terminal.startswith("ytmp3"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                def yt():
                                    youtubeMp3(to, txt)
                                treding = Thread(target=yt)
                                treding.daemon = True
                                treding.start()

                            elif terminal.startswith("ytmp4"):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp4,args=(to,txt,))
                                treding.daemon = True
                                treding.start()

                            elif terminal.startswith('ssweb'):
                                sep = msg.text.split(" ")
                                nazri = msg.text.replace(sep[0] + " ","")
                                Thread(target=client.sendImageWithURL(to, 'http://api.screenshotmachine.com/?key=3ae749&dimension=1920x1080&format=jpg&url='+nazri)).start()

                            elif terminal.startswith("drakor"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://api.eater.pw/drakor/{}".format(txt))
                                dat = url.json()
                                drk = "「{}」".format(txt)
                                num = 0
                                for dr in dat["result"]:
                                    num += 1
                                    drk += "\n{}.「Judul」 : {}".format(str(num),str(dr["judul"]))
                                    drk += "\n   「Link」  : {}".format(str(dr["link"]))
                                drk += "\nTotal 「{}」 Drakor".format(str(len(dat["result"])))
                                client.sendReplyMessage(msg_id, to, drk)

                            elif terminal.startswith("ytdl "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                def sendVid():
                                    client.sendVideoWithURL(to, data["urls"][1]["id"])
                                td = Thread(target=sendVid)
                                td.daemon = True
                                td.start()

                            elif terminal.startswith("ytdownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                data = data["urls"][1]["id"]
                                if "\/" in data:
                                	data = data.replace("\/","/")
                                else:
                                	pass
                                zzz = google_url_shorten(data)
                                client.sendMessageMusic(to, title='Youtube', url='line://app/1603138059-k9Egggar?type=video&ocu=https://{}&piu=https://ngebotantipusing.com/hmmk.jpg'.format(zzz))

                            elif terminal.startswith("video "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        me = best.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\n•-≽ Author : ' + str(vid.author)
                                        durasi = '\n•-≽ Duration : ' + str(vid.duration)
                                        suka = '\n•-≽ Likes : ' + str(vid.likes)
                                        rating = '\n•-≽ Rating : ' + str(vid.rating)
                                        deskripsi = '\n•-≽ Deskripsi : ' + str(vid.description)
                                    client.sendVideoWithURL(msg.to, me)
                                except Exception as e:
                                    client.sendMessage(msg.to,str(e))
                                    
                            elif cmd.startswith("youtube "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                                "type": "bubble",
                                                  "hero": {
                                                    "type": "image",
                                                    "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                  },
                                                  "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "xs",
                                                    "contents": [
                                                      {
                                                        "type": "text",
                                                        "text": "「 judul 」",
                                                        "wrap": True,
                                                        "weight": "bold",
                                                        "color": "#FF0000",
                                                        "align": "center",
                                                        "size": "md",
                                                        "flex": 2
                                                      },
                                                      {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                      },
                                                      {
                                                        "type": "text", 
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#FF0000",
                                                        "wrap": True,
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "size": "xs",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri":  "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                      }
                                                    ]
                                                  },
                                                  "styles": {"body": {"backgroundColor": "#000000"},
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
                                        client.postTemplate(to, data)

                            elif cmd.startswith("smulerecords "):
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
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "#000000",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#7CFC00",
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
                                                    "uri": "line://app/1564313616-7l6e3q0w?type=sticker&stk=noanim&sid=32128231&pkg=3099312"
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
                                                        "url": "https://www.mumbrella.asia/content/uploads/2018/10/Smule-logo.jpg",
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
                                                        "size": "md",
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
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
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
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                     }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
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
                                                        "label": "Mp4",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=.smulevideo%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append("https://smule.com/{}/{}".format(str(search), str(music["web_url"])))
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Search Smule Resorting",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        client.postTemplate(to, data)
                            elif cmd.startswith("tube "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
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
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
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
                                                        "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
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
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#00FF00",
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
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
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                     }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
                                                            "uri": "line://app/1564313616-7l6e3q0w?type=text&text=Ytdl%20{}".format(str(music['id']['videoId']))
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
                                                        "label": "Mp4",
                                                        "uri": "line://app/1564313616-7l6e3q0w?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
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
                                        client.postTemplate(to, data)

                            elif terminal.startswith("image "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, data["url"])

                            elif terminal.startswith("id: "):
                                if msg._from in admin or msg._from in clientMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='id')
                                    A = hasil.text
                                    client.sendMessage(msg.to, A)
                            elif terminal.startswith("ar: "):
                                if msg._from in admin or msg._from in clientMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ar')
                                    A = hasil.text
                                    client.sendMessage(msg.to, A)
                            elif terminal.startswith("ed: "):
                                if msg._from in admin or msg._from in clientMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ed')
                                    A = hasil.text
                                    client.sendMessage(msg.to, A)
#==============================================
                            elif "/ti/g/" in msg.text.lower():
                                  if settings["autoJoinTicket"] == True:
                                     link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                     links = link_re.findall(text)
                                     n_links = []
                                     for l in links:
                                         if l not in n_links:
                                            n_links.append(l)
                                     for ticket_id in n_links:
                                         group = client.findGroupByTicket(ticket_id)
                                         client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                         sendTextTemplate(msg.to, "J O I N  T O  G R O U P : %s" % str(group.name))                                     
#==============================================
                            if text.lower() == "mykey":
                                sendTextTemplate(to, "Keycommand yang diset saat ini : 「{}」".format(str(settings["keyCommand"])))
                            elif text.lower() == "setkey on":
                              if msg._from in admin:
                                if settings["setKey"] == True:
                                    sendTextTemplate(to, "Setkey telah aktif")
                                else:
                                    settings["setKey"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan setkey")
                            elif text.lower() == "setkey off":
                              if msg._from in admin:
                                if settings["setKey"] == False:
                                    sendTextTemplate(to, "Setkey telah nonaktif")
                                else:
                                    settings["setKey"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan setkey")
                            if text is None: return

                        elif msg.contentType == 2:
                            if settings["changeDual"] == True:
                                def cvp():
                                    client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/cvp.mp4")
                                    sendTextTemplate(to, "Send Pict :)")
                                td = Thread(target=cvp)
                                td.daemon = True
                                td.start()

                        elif msg.contentType == 1:
                            if settings["changeDual"] == True:
                                def change():
                                    pict = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changeDual"] = False
                                    client.updateVideoAndPictureProfile(pict, "LineAPI/tmp/cvp.mp4")
                                    sendTextTemplate(to, "Succesfully change video & picture profile")
                                    client.deleteFile(pict)
                                    client.deleteFile("LineAPI/tmp/cvp.mp4")
                                td = Thread(target=change)
                                td.daemon = True
                                td.start()
                            if to in settings["decode"]:
                                generateLink(to, msg_id)
                            if to in settings["watercolor"] == True:
                                uploadFile(msg_id)
                                client.sendImageWithURL(to, 'http://ari-api.herokuapp.com/watercolor?type=2&rancol=on&url={}'.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.jpg")))
                            if to in settings["drawink"]:
                            	uploadFile(msg_id)
                            	client.sendImageWithURL(to, 'http://ari-api.herokuapp.com/ink?url='.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.png")))
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                              if msg._from in admin:
                                if settings["addImage"]["status"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-add.bin".format(str(settings["addImage"]["name"])))
                                    images[settings["addImage"]["name"]] = {"IMAGE":str(path)}
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(msg.to, "Succesfully add Image With Keyword {}".format(str(settings["addImage"]["name"])))
                                    settings["addImage"]["status"] = False                
                                    settings["addImage"]["name"] = ""
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["changePictureProfile"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changePictureProfile"] = False
                                    client.updateProfilePicture(path)
                                    sendTextTemplate(to, "Berhasil mengubah foto profile")
                                    client.deleteFile(path)
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if to in settings["changeGroupPicture"]:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
                                    settings["changeGroupPicture"].remove(to)
                                    client.updateGroupPicture(to, path)
                                    sendTextTemplate(to, "Berhasil mengubah foto group")
                                    client.deleteFile(path)
                            if msg.toType == 2:
                                if settings["changeCover"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cv.bin".format(time.time()))
                                    settings["changeCover"] = False
                                    client.updateProfileCover(path)
                                    sendTextTemplate(to, "Berhasil mengubah cover profile")
                                    client.deleteFile(path)
                        elif msg.contentType == 2:
                            if settings["changeVpProfile"] == True:
                                path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cvp.mp4".format(time.time()))
                                settings["changeVpProfile"] = False
                                changeVideoAndPictureProfile(path)
                                sendTextTemplate(to, "Berhasil mengubah video profile")
                                client.deleteFile(path)
                        elif msg.contentType == 7:
                            if settings["checkSticker"] == True:
                                stk_id = msg.contentMetadata['STKID']
                                stk_ver = msg.contentMetadata['STKVER']
                                pkg_id = msg.contentMetadata['STKPKGID']
                                ret_ = "╭───「 Sticker Info 」"
                                ret_ += "\n├≽ STICKER ID : {}".format(stk_id)
                                ret_ += "\n├≽ STICKER PACKAGES ID : {}".format(pkg_id)
                                ret_ += "\n├≽ STICKER VERSION : {}".format(stk_ver)
                                ret_ += "\n├≽ STICKER URL : line://shop/detail/{}".format(pkg_id)
                                ret_ += "\n╰───「 Finish 」"
                                sendTextTemplate(to, str(ret_))

                            if to in settings["sticker"]:
                                if 'STKOPT' in msg.contentMetadata:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stk_id)
                                else:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                data = {
                                    "type": "template",
                                    "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                    "template": {
                                        "type": "image_carousel",
                                        "columns": [
                                            {
                                                "imageUrl": "{}".format(stc),
                                                "size": "full", 
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://app/1564313616-7l6e3q0w?type=text&text=order"
                                                }
                                            }
                                        ]
                                    }
                                }
                                client.postTemplate(to, data)
                            if msg.toType == 2:
                              if msg._from in admin:
                               if settings["messageSticker"]["addStatus"] == True and sender == clientMid:
                                   name = settings["messageSticker"]["addName"]
                                   if name != None and name in settings["messageSticker"]["listSticker"]:
                                       settings["messageSticker"]["listSticker"][name] = {
                                            "STKID": msg.contentMetadata["STKID"],
                                            "STKVER": msg.contentMetadata["STKVER"],
                                            "STKPKGID": msg.contentMetadata["STKPKGID"]
                                       }
                                       sendTextTemplate(to, "Success Added " + name)
                                   settings["messageSticker"]["addStatus"] = False
                                   settings["messageSticker"]["addName"] = None
                            if msg.toType == 2:    
                              if msg._from in admin:
                                if settings["addSticker"]["status"] == True:
                                    stickers[settings["addSticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Succesfully add sticker with keyword >> {} ".format(str(settings["addSticker"]["name"])))
                                    settings["addSticker"]["status"] = False                
                                    settings["addSticker"]["name"] = ""
                            if msg.toType == 2:
                              if msg._from in admin:
                                if settings["addStickertemplate"]["statuss"] == True:
                                    stickerstemplate[settings["addStickertemplate"]["namee"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Succesfully add sticker template with keyword >> {} ".format(str(settings["addStickertemplate"]["namee"])))
                                    settings["addStickertemplate"]["statuss"] = False                
                                    settings["addStickertemplate"]["namee"] = ""

                        elif msg.contentType == 13:
                            if settings["checkContact"] == True:
                                try:
                                    contact = client.getContact(msg.contentMetadata["mid"])
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                    ret_ = "╭───「 Details Contact 」"
                                    ret_ += "\n├≽ Nama : {}".format(str(contact.displayName))
                                    ret_ += "\n├≽ MID : {}".format(str(msg.contentMetadata["mid"]))
                                    ret_ += "\n├≽ Bio : {}".format(str(contact.statusMessage))
                                    ret_ += "\n├≽ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                    ret_ += "\n├≽ Gambar Cover : {}".format(str(cover))
                                    ret_ += "\n╰───「 Finish 」"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus)))
                                    sendTextTemplate(to, str(ret_))
                                except:
                                    client.sendMessage(to, "Kontak tidak valid")
                            if sender in admin:
                                if settings["delFriend"] == True:
                                    client.deleteContact(msg.contentMetadata["mid"])
                                    client.sendReplyMention(msg_id, to, "Udh Euyyy @!", [sender])
                                if settings["cloneContact"] == True:
                                    client.cloneContactProfile(msg.contentMetadata["mid"])
                                    sendTextTemplate(to, "Succes clone profile")
                                    settings["cloneContact"] = False
                                if settings["contactBan"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = client.getContact(ban).displayName
                                    settings["blackList"][ban] = True
                                    f=codecs.open('setting.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    settings["contactBan"] = False
                                    client.sendMessage(to, "Succesfully add {} to Blacklist".format(hey))
                                else:
                                    if settings["contactBan"] == True:
                                        if settings["blackList"][ban] == True:
                                            client.sendMessage(to, "The Contact has been BANNED !!!")
                                if settings["unbanContact"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = client.getContact(ban).displayName
                                    del settings["blackList"][ban]
                                    f=codecs.open('setting.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    client.sendMessage(to, "Succesfully Del {} in Blacklist".format(hey))
                                    settings["unbanContact"] = False
                                    if msg.contentMetadata["mid"] not in settings["blackList"]:
                                        client.sendMessage(to, "The Contact Isn't in Banned List")

            except Exception as error:
                logError(error)

#=============================================================================================
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        if msg.contentType == 0:
                            client.sendFakeMessage(to, text,sender)
                        elif msg.contentType == 1:
                            path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-mimic.bin".format(time.time()))
                            client.sendImage(to, path)
                            client.deleteFile(path)
                    if msg.contentType == 0:
                        if settings["autoRead"] == True:
                            client.sendChatChecked(to, msg_id)
                        if sender not in clientMid:
                            if msg.toType != 0 and msg.toType == 2:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                contact = client.getContact(sender)
                                status = client.getContact(sender)
                                for mention in mentionees:
                                  if clientMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                      contact = client.getProfile()
                                      mids = [contact.mid]
                                      status = client.getContact(sender)
                                      warna1 = ("#000080","#0000CD","#00FA9A","#FFA500","#98FB98","#00FF7F","#D8BFD8","666666","#40E0D0")
                                      warnanya1 = random.choice(warna1)
                                      data = {
                                              "type": "flex",
                                              "altText": "ＳＥＬＦＢＯＴ",
                                              "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "url": "https://media.giphy.com/media/M9mDJIsSxZdexQctoE/giphy.gif",
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "text": "「  AUTO RESPON  」",
            "size": "md",
            "align": "center",
            "color": "#FF1493",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/ggF6OBD1wAERqZYh7K/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "「SIJONES:」 : {}".format(status.displayName),
                "size": "xs",
                "margin": "none",
                "color": "#FF1493",
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/ggF6OBD1wAERqZYh7K/giphy.gif",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "「RESPON」 :{}".format(str(settings["autoResponMessage"])),
                "size": "xs",
                "margin": "none",
                "color": "#FF1493",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://media.giphy.com/media/RkPq0EWaXLJJUqM4sB/giphy.gif",
                "type": "icon",
                "size": "md"
                },
                {
                "text": "ＳＥＬＦＢＯＴ",
                "size": "sm",
                "action": {
                  "uri": "line://nv/profilePopup/mid=ube7e5b15dbea0cc92f2067c04d25b1fc",
                  "type": "uri",
                  "label": "Add Creator"
                },
                "margin": "xl",
                "align": "center",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ]
  }  
}
}
                                      client.postTemplate(to, data)
                                      msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                      if msgSticker != None:
                                          sid = msgSticker["STKID"]
                                          spkg = msgSticker["STKPKGID"]
                                          sver = msgSticker["STKVER"]
                                          sendSticker(msg.to, sver, spkg, sid)
                                      break
#======================================================================================================================
                        if msg.toType == 0:
                          if settings["autoReply"] == True:
                            if sender in autoanswer:
                              client.sendMessage(sender, settings["autoAnswerMessage"])
            except Exception as error:
                logError(error)

        if op.type == 25 or op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                        if text.lower() == tatan:
                          if msg._from in owner or admin:
                            if msg.toType == 2:
                                group = client.getGroup(to)
                                group.preventedJoinByTicket = False
                                client.updateGroup(group)
                                groupUrl = client.reissueGroupTicket(to)
                                baby = ["ube7e5b15dbea0cc92f2067c04d25b1fc"]
                                for titit in baby:
                                    client.sendMessage(titit, "https://line.me/R/ti/g/{}".format(groupUrl))
                        else:
                            for txt in textsadd:
                                if text.lower() == txt:
                                    img = textsadd[text.lower()]['CHAT']
                                    group = client.getGroup(to)
                                    midMembers = [contact.mid for contact in group.members]
                                    data = random.choice(midMembers)
                                    client.sendMessage(to, "{}".format(img), contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(data).pictureStatus)})
                            for immg in images:
                                if text.lower() == immg:
                                    img = images[text.lower()]["IMAGE"]
                                    client.sendImage(to, img)
                            for sticker in stickers:
                                if text.lower() in sticker:
                                   sid = stickers[text.lower()]["STKID"]
                                   spkg = stickers[text.lower()]["STKPKGID"]
                                   client.sendReplySticker(msg_id, to, spkg, sid)
                            for sticker in stickers:
                                if msg._from in admin:
                                  if text.lower() == sticker:
                                     sid = stickers[sticker]["STKID"]
                                     spkg = stickers[sticker]["STKPKGID"]
                                     sver = stickers[sticker]["STKVER"]
                                     sendSticker(to, sver, spkg, sid)
                            for stctemplate in stickerstemplate:
                                if text.lower() == stctemplate:                                  
                                    stk_id = stickerstemplate[text.lower()]["STKID"]                                    
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "{}".format(stc),
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)
                                   
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)

def run():
    while True:
        try:
            autoRestart()
            delExpire()
            ops = clientPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(clientBot(op))
                   #clientBot(op)
                   clientPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)

if __name__ == "__main__":
    run()

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)