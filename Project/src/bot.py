import aiml
import uuid

class Bot(object):
    """
    Bot class that parses the required aiml file in the resources folder
    and provides appropriate output for the query.
    """
    def __init__(self):
        ##TODO: Maintain session ID for each object to deliver dedicated \
        ##      services to each client  
        try:
            self.kernel = aiml.Kernel()
            self.kernel.learn("../resources/std-startup.xml")
            self.kernel.respond("load aiml")
        except Exception as e:
            print(e)
            exit()

    def query(self, user_query):
        """
        Input: user query <str>
        Output: bot response <str>
        Exception: returns exception string 
        """
        try:
            response = self.kernel.respond(user_query)
            return response
        except Exception as e:
            return str(e)
