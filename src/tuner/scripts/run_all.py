#! /usr/bin/python2

import os

def run(program, arguments, logdir, time, runs, benchmark):
    os.system("mkdir "   + logdir)
    cmd = "./scripts/run_experiments.py"
    cmd += " -f="        + program
    cmd += " -fargs="    + "\"" + " ".join(arguments) + "\""
    cmd += " -ld="       + logdir
    cmd += " -lc=final"
    cmd += " -time="     + str(time)
    cmd += " -th=1"
    cmd += " -r="        + str(runs)
    cmd += " -br="       + str(benchmark)
    os.system(cmd)
#
# SubSeqMax Experiments:
#
# Parameters:
#
program     = "../bioinformatic/SubSeqMax.cu"
logdir      = "logs/SubSeqMax"
time        = 7200
runs        = 2
benchmark   = 20
#
# Starting a clean experiment.
#
os.system("rm -r " + logdir)
os.system("mkdir " + logdir)
#
# TODO: Compute baseline values for nvcc optimization levels,
#       and for no-flags compilation.
#
print "[INFO] Starting SubSeqMax Experiments."
for i in [2**25, 2**26, 2**27, 2**28, 2**29, 2**30]:
    logs = logdir + "/size_" + str(i) + "_time_" + str(time)
    run(program, [str(i), "0"], logs, time, runs, benchmark)
print "[INFO] SubSeqMax Experiments Done."
#
# TODO: Write code for the other experiments.
#
