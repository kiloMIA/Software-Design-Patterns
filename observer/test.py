from observer1 import *

publisher = Publisher()

subscriber1 = Subscriber('Sub1')
subscriber2 = Subscriber('Sub2')
publisher.register(subscriber1)
publisher.register(subscriber2)
publisher.dispatch('wtf')

