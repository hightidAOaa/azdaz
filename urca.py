                                          

from websocket import create_connection
import threading
import time, requests
def cota():
    while True:
        try:
            time.sleep('60')
            ws.send('Ping')
        except:
            time.sleep(2)
            pass

(threading.Thread(target=cota, args=[])).start()
while True:
    try:
        ota=[]
        ws = create_connection("wss://irc-ws.chat.twitch.tv/")
        ws.send("CAP REQ :twitch.tv/tags twitch.tv/commands")
        ws.send("PASS SCHMOOPIIE")
        ws.send("NICK justinfan46511")
        ws.send("USER justinfan46511 8 * :justinfan46511")
        print(ws.recv())
        print(ws.recv())
        ws.send("JOIN #"+input('channel to read:'))
        def dlvr(blobb):
            azezezez="zefze"

        while True:
            blob=""
            msg=ws.recv()
            if msg == 'PING :tmi.twitch.tv':
                ws.send('Pong')
            elif 'PRIVMSG' in msg:
                usa_id=(msg.split(';user-id=')[1]).split(';')[0]
                usrnm=((msg.split('user-type=')[1]).split('!')[0]).strip(" :")
                usrnm=usrnm.replace('mod :','')
                usrnm = usrnm.replace(";vip=1 :", "")
                msgg=msg.split('PRIVMSG ')[1]
                blb="**"+usrnm+"**: "+msgg
                blob+=blb+"\n"
                if len(blob)>2:
                    vv=(blob.split('#')[1]).split(' ')[0]
                    zefza=blob
                    zefza=zefza.replace(': #xqc :', ': ')
                    zefza=zefza.replace('**', '')
                    print(zefza)
                    ota.append(';user-id='+usa_id+' '+blob)
            elif '@room-id=' in msg.split(';')[0]:
                usda=(msg.split(';target-user-id=')[1]).split(';')[0]
                tooookaaa=[]
                for ia in ota:
                    if ';user-id='+usda in ia:
                        print(ia)
                        tooookaaa.append('**Banned** '+ia)
                        ota.remove(ia)
                if len(tooookaaa)>2:
                    dlvr(tooookaaa[len(tooookaaa)-3]+'\n'+tooookaaa[len(tooookaaa)-2]+'\n'+tooookaaa[len(tooookaaa)-1])
                elif len(tooookaaa)>1:
                    dlvr(tooookaaa[len(tooookaaa)-2]+'\n'+tooookaaa[len(tooookaaa)-1])
                else:
                    dlvr(tooookaaa[0])
                if len(tooookaaa)>2:
                    dlvr(tooookaaa[len(tooookaaa)-3]+'\n'+tooookaaa[len(tooookaaa)-2]+'\n'+tooookaaa[len(tooookaaa)-1])
                elif len(tooookaaa)>1:
                    dlvr(tooookaaa[len(tooookaaa)-2]+'\n'+tooookaaa[len(tooookaaa)-1])
                else:
                    dlvr(tooookaaa[0])
            if len(ota) == 10000:
                ota=[]
                print('cleared')
    except Exception as azerzer:
        print(azerzer)
        time.sleep(2)