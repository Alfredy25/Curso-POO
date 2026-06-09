from threading import Thread
from queue import Queue
from feuh.sample2.thread.carrier import Carrier


class CarrierWorker(Thread):

    def __init__(self, queue: Queue, carrier: Carrier):
        super().__init__(name = carrier.name)
        self.queue = queue
        self.carrier = carrier

    def run(self):

        try:
            df = self.carrier.process()
            self.queue.put({
                "carrier": self.carrier.name,
                "success": True,
                "data": df,
                "error": None
            })

        except Exception as e:
            self.queue.put({
                "carrier": self.carrier.name,
                "success": False,
                "data": None,
                "error": str(e)
            })




