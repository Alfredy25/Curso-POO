from feuh.sample2.bakery.bakery import Bakery
from feuh.sample2.bakery.thread.baker import Baker
from feuh.sample2.bakery.thread.consumer import Consumer

bakery = Bakery()

baker = Baker(bakery)
consumer = Consumer(bakery)
consumer.start()
baker.start()