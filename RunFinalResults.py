import sys, os
import glob

lumi = {'2016':'35.9', '2017':'41.5', '2018':'59.8'}

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this datacard production", type=str, default="fcnc")
parser.add_argument("--datacard", help = "path to datacard", type=str, default="Datacard/Datacard_dummy.txt")
parser.add_argument("--years", help = "which years to consider", type=str, default = "2017")
parser.add_argument("--inputWSDir", help = "directories with input ws", type=str, default = "/home/users/sjmay/ttH/FCNC_Workspaces/CMSSW_10_6_1_patch2/src/flashgg/Systematics/test/workspaces_Hut_YEAR_prod_v2.1_2-March-2020/")
parser.add_argument("--signal_model_dir", help = "dir with sigfits", type=str, default="Signal/outdir_fcnc")
parser.add_argument("--bkg_model", help = "path to background model", type=str, default="Background/CMS-HGG_multipdf_fcnc_2017.root")
parser.add_argument("--cats", help = "cats", type=str, default="FCNCHadronicTag_0,FCNCHadronicTag_1,FCNCLeptonicTag_0,FCNCLeptonicTag_1")
args = parser.parse_args()

years = args.years.split(",")

if len(years) > 1:
    intlumi = "137.2"
else:
    intlumi = lumi[years[0]]

os.system("cp %s %s" % (args.datacard, "Plots/FinalResults/CMS-HGG_mva_13TeV_datacard.txt"))

os.system("mkdir -p Plots/FinalResults/Models/")
os.system("mkdir -p Plots/FinalResults/Models/background_merged/")

os.system("cp %s %s" % (args.bkg_model, "Plots/FinalResults/Models/background_merged/CMS-HGG_mva_13TeV_multipdf.root"))

for year in years:
    sig_files = glob.glob(args.signal_model_dir + "_%s/*.root" % year)
    os.system("mkdir -p Plots/FinalResults/Models/signal_%s/" % year)
    for file in sig_files:
        target = file.split("/")[-1].replace("fcnc_%s" % year, "mva")
        command = "cp %s %s" % (file, "Plots/FinalResults/Models/signal_%s/%s" % (year, target))
        print command
        os.system(command)


os.chdir("Plots/FinalResults")

harvestOpt = "combineHarvesterOptions_FCNC_%s.dat" % args.tag
os.system("cp combineHarvesterOptions_FCNC.dat %s" % harvestOpt)

os.system('sed -i -e "s/\!EXT\!/%s/g" %s' % (args.tag, harvestOpt))
os.system('sed -i -e "s/\!FAKE\!/%s/g" %s' % ("", harvestOpt))
os.system('sed -i -e "s/\!INTLUMI\!/%s/g" %s' % (intlumi, harvestOpt))


harvester_command = "./combineHarvester.py -d %s --runLocal --parallel --verbose" % harvestOpt

print harvester_command
os.system(harvester_command)

harvester_hadd = "./combineHarvester.py --hadd combineJobs13TeV_%s" % args.tag

print harvester_hadd
#os.system(harvester_hadd)
