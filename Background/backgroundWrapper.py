import sys, os
import glob

sys.path.append("python/")
import parallel_utils

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this datacard production", type=str, default="fcnc")
parser.add_argument("--couplings", help = "which couplings to run for", type=str, default = "Hut,Hct")
parser.add_argument("--inputConfig", help = "input config base file", type=str, default = "fcnc_config_base.py")
args = parser.parse_args()

couplings = args.couplings.split(",")

command_list = []

for coupling in couplings:
    print "[FCNC BKG MODEL WRAPPER] Running background models for coupling: %s" % coupling
    config = "fcnc_config_%s.py" % (coupling)
    os.system("cp %s %s" % (args.inputConfig, config))

    os.system('sed -i -e "s/COUPLINGLOWER/%s/g" %s' % (coupling.lower(), config))
    os.system('sed -i -e "s/COUPLING/%s/g" %s' % (coupling, config))

    command = "python RunBackgroundScripts.py --inputConfig %s" % config

    print "[FCNC BKG MODEL WRAPPER] Running command: %s" % command
    command_list.append(command)

parallel_utils.submit_jobs(command_list, 1)
