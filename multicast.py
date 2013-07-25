from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastListener(DatagramProtocol):
    def startProtocol(self):
        """
        Called after protocol has started listening.
        """
        # Set the TTL>1 so multicast will cross router hops:
        self.transport.setTTL(5)
        # Join a specific multicast group:
        self.transport.joinGroup("230.0.0.1")

    def datagramReceived(self, datagram, address):
        print "Datagram %s received from %s" % (repr(datagram), repr(address))


# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
reactor.listenMulticast(7777, MulticastListener(),
                        listenMultiple=True)
reactor.run()
