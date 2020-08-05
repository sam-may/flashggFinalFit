import sys, os
import glob

sys.path.append("python/")
import parallel_utils

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this datacard production", type=str, default="fcnc")
parser.add_argument("--years", help = "which years to consider", type=str, default = "2016,2017,2018")
parser.add_argument("--couplings", help = "which couplings to run for", type=str, default = "Hut,Hct")
parser.add_argument("--inputConfig", help = "input config base file", type=str, default = "fcnc_config_base.py")
parser.add_argument("--printOnly", help = "dry run", action="store_true")
args = parser.parse_args()

years = args.years.split(",")
couplings = args.couplings.split(",")

command_list = []

for coupling in couplings:
    print "[FCNC SIG MODEL WRAPPER] Running signal models for coupling: %s" % coupling
    for year in years:
        print "[FCNC SIG MODEL WRAPPER] Running signal models for coupling: %s, year: %s" % (coupling, year)

        config = "fcnc_config_%s_%s.py" % (coupling, year)
        os.system("cp %s %s" % (args.inputConfig, config))

        os.system('sed -i -e "s/COUPLINGLOWER/%s/g" %s' % (coupling.lower(), config))
        os.system('sed -i -e "s/COUPLING/%s/g" %s' % (coupling, config))
        os.system('sed -i -e "s/YEAR/%s/g" %s' % (year, config))

        command = "python RunSignalScripts.py --inputConfig %s" % config
        if args.printOnly:
            command += " --printOnly 1"

        print "[FCNC SIG MODEL WRAPPER] Running command: %s" % command
        command_list.append(command)

parallel_utils.submit_jobs(command_list, 1)

base_path = "~/ttH/FCNC_FinalFits_v2/CMSSW_10_2_13/src/flashggFinalFit/Signal/"
print "Make AutoPlotter dirs with the following commands:"
for coupling in couplings:
    for year in years:
        input_dir = base_path + "outdir_" + args.tag + "_" + coupling + "_" + year + "/"
        target_dir = input_dir.replace(base_path, "").replace("/","_")[:-1]
        command = "./aplot %s %s" % (input_dir + "sigplots/", target_dir)
        print command
