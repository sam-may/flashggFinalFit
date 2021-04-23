import os
import numpy
import json

points = numpy.linspace(0.01, 1.0, 20)
results = {}

for point in points:
    command = "combine -M AsymptoticLimits -m 125.380000 Datacard_fcnc_hutv5.10_3Feb2021_FCNCHadronicTag_0_FCNC.root -n limit_FCNCHadronic_Tag0_test --singlePoint %.4f > results.txt" % point
    os.system(command)
    with open("results.txt", "r") as f_in:
        lines = f_in.readlines()

    for line in lines:
        if "Observed CLs" not in line:
            continue

        cls = line.split()[-1]
        results[point] = float(cls)

with open("results.json", "w") as f_out:
    json.dump(results, f_out, indent=4, sort_keys=True)
