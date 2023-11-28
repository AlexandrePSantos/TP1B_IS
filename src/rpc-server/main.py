import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from functions.converter import CSVtoXMLConverter
from functions.validateFile import validateFile
from functions.importFile import importFile
from functions.listFiles import listFiles
from functions.softDelete import softDelete
from functions.query1 import releases_from_car_by_id
from functions.query2 import num_car_Maker
from functions.query3 import releases_from_car_by_Model
"""from functions.query4 import num_car_Maker
from functions.query5 import num_car_Maker """

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
    
    convertFile = CSVtoXMLConverter("/data/Electric_Vehicle_Population_Data.csv")
    
    # register functions
    server.register_function(convertFile.to_xml_str)
    server.register_function(validateFile)
    server.register_function(importFile)
    server.register_function(listFiles)
    server.register_function(softDelete)
    server.register_function(releases_from_car_by_id)
    server.register_function(num_car_Maker)
    server.register_function(releases_from_car_by_Model)
    """     server.register_function()
    server.register_function() """
    
    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
