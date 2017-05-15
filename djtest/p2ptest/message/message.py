import p2ptest.p2p as p2p_module
import hashlib

class Message:
    getdata=set()
    @staticmethod
    def recv(sock):
        data=sock.socket.recv(1024)
        try:
            hashdata=hashlib.sha256(data).hexdigest()
            if not (hashdata in Message.getdata):
                Message.getdata.add(hashdata)
                print "==== get new message ===="
                print data
                sock.broadcast(data)
        except Exception as e:
            print e

    
    @staticmethod
    def send(body):
        p2p_module.p2p.P2PScoket.broadcast(body)
        