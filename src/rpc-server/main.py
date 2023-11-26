import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# from functions.csv_to_xml_converter import CSVtoXMLConverter
from functions.validateFile import validateFile
from functions.importFile import importFile
# from functions.query1 import query1
# from functions.query2 import query2
# from functions.query3 import query3
# from functions.query4 import query4
# from functions.query5 import query5

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler, allow_none = True) as server:
    server.register_introspection_functions()
    


    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)
    
    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    # server.register_function(convertFile)
    server.register_function(validateFile)
    server.register_function(importFile)
    # server.register_function(query1)
    # server.register_function(query2)
    # server.register_function(query3)
    # server.register_function(query4)
    # server.register_function(query5)
    
    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
