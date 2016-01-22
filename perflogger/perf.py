import time
import logging
import platform
import os
class Perf(object):

    def __init__(self, args, argv):
        """
        Return a Perf object whose command, project, and arguments are set by
        user input
        """
        self.command = args.command
        self.project = args.project
        self.cmdargs = argv
        logging.debug("Command: %s; Project: %s, Arguments: %s", 
                       self.command, self.project, self.cmdargs)
        self.setRunEnv()

    def setPerfTime(self, perfTime):
        """
        Set the time taken to run the command
        """
        self.perfTime = perfTime
        logging.debug("Performance Time: %s", self.perfTime)

    def setRunEnv(self):
        """
        Set the timestamp, Linux version, CPU information, and environment 
        variables
        """
        # Get timestamp
        self.ts = time.ctime() 
        # Get Linux version and CPU info
        proc = platform.processor()
        machine = platform.machine()
        node = platform.node()
        arch = platform.architecture()
        plat = platform.platform()
        sys = platform.system()
        release = platform.release()
        ver = platform.version()
        self.LinuxCPUInfo = (proc, machine, node, arch, plat, sys, release, ver)
        # Get environment variables
        env = ""
        for envKey in os.environ.keys():
            env += "%s=%s\n" % (envKey, os.environ[envKey])
        self.env = env
        logging.debug("Timestamp: %s; LinuxCPUInfo: %s; env: %s", 
                      self.ts, self.LinuxCPUInfo, self.env)

    def parseToJSON(self):
        """
        Parse the data into JSON format and insert into the Elasticsearch
        Database.
        """
        print "Parsing to JSON..."
        dataJSON = {}
        return dataJSON
        """
        Format of JSON:
        ---------------
        json: {
            runenv: {
                nodes, cpu, uname
            }
            args:
            command:
            project:
            user:
            start: timestamp
            end: timestamp
            duration:
            timings: {..., ..., ...}
            success: true/false
        }
        """
