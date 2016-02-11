import time
import logging
import platform
import os
import json
from elasticsearch import Elasticsearch

class Perf(object):

    def __init__(self, args, argv):
        """
        Return a Perf object whose command, project, and arguments are set by
        user input
        """
        self.command = args.command
        self.mpirun = args.mpirun
        self.np = args.np
        self.project = args.project
        self.args = argv
        logging.debug("Command: %s; Mpirun: %s; Np: %s; Project: %s, Arguments: %s", 
                       self.command, self.mpirun, self.np, self.project, self.args)
        self.setRunEnv()

    def setCmdResults(self, cmdTime):
        """
        Set the time taken to run the command
        """
        self.duration = cmdTime[0]
        self.startTime = cmdTime[1]
        self.endTime = cmdTime[2]
        self.isSuccess = cmdTime[3]
        logging.debug("Duration: %s; startTime: %s; endTime: %s; success: %s",\
                      self.duration, self.startTime, self.endTime, 
                      self.isSuccess)

    def setRunEnv(self):
        """
        Set the timestamp, Linux version, CPU information, and environment 
        variables
        """
        # Get timestamp
        self.ts = time.ctime() 
        # Get Linux version and CPU info
        self.LinuxCPUInfo = {
                "processor":platform.processor(),
                "machine": platform.machine(), 
                "node": platform.node(), 
                "system": platform.system(), 
                "release": platform.release(), 
                "version": platform.version()
                }
        self.user = os.getenv("USER")
        self.hostname = os.getenv("HOSTNAME")
        self.pbsInfo = {
                        "np": os.getenv("PBS_NP"),
                        "num_nodes": os.getenv("PBS_NUM_NODES"),
                        "num_ppn": os.getenv("PBS_NUM_PPN"),
                        "queue": os.getenv("PBS_O_QUEUE"),
                        "jobid": os.getenv("PBS_JOBID")
                       }
        logging.debug("Timestamp: %s; LinuxCPUInfo: %s; User: %s; \
                       Hostname: %s; PBS Info:%s", 
                      self.ts, self.LinuxCPUInfo, self.user, self.hostname, 
                      self.pbsInfo)

    def parseToJSON(self):
        """
        Parse the data into JSON format and insert into the Elasticsearch
        Database.
        """
        print "Parsing to JSON..."
        dataJSON = {
                    'runenv': self.LinuxCPUInfo,
                    'command': self.command,
                    'project': self.project,
                    'arguments': self.args,
                    'user': self.user,
                    'hostname': self.hostname,
                    'pbsInfo': self.pbsInfo,
                    'duration': self.duration,
                    'start': self.startTime,
                    'end': self.endTime,
                    'success': self.isSuccess
                    # 'timings': {..., ..., ...}
                   }
        return dataJSON


    def insertToESDB(self, dataJSON):
        """
        Create an index (if not exists) and insert the json into it

        :param dataJSON: JSON with relevant data
        """
        # Create index
        # Insert into index
        print "Inserting json into Elasticsearch Database..."
        es = Elasticsearch(['http://kibana:cs492@141.142.168.47:80/es'])
        res = es.search(index="test-index", body={"query": {"match_all": {}}})
        print res
