import sys, logging, re, time
from . import CheckFile
from trustyuri.file import ProcessFile
from trustyuri.rdf import TransformRdf

logging.basicConfig(level=logging.ERROR)

filename = sys.argv[1]

with open(filename) as f:
    for line in f:
        line = line.strip()
        if (re.match(r'^#|^$', line)):
            continue
        print("COMMAND: " + line)
        cmdargs = line.split(' ')
        cmd = cmdargs.pop(0)
        starttime = time.time()
        try:
            if (cmd == "CheckFile"):
                CheckFile.check(cmdargs)
            elif (cmd == "ProcessFile"):
                ProcessFile.process(cmdargs)
            elif (cmd == "TransformRdf"):
                TransformRdf.transform(cmdargs)
            else:
                print("ERROR: Unrecognized command %s" % cmd)
                exit(1)
        except:
            print(sys.exc_info()[0])
        t = time.time() - starttime
        print("Time in seconds: %g" % t)
        print("---")
