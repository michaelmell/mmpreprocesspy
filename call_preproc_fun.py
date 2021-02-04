#!/bin/python

'''#
This script corresponds to the script mm_pre_slurm.sh, which is used for the original Java MMPreproc implementation.
'''

import sys
#print("Python version:")
#print(sys.version)

import argparse
import re

from mmpreprocesspy.preproc_fun import preproc_fun

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", type=str,
                    help="input directory")
parser.add_argument("-o", "--output", type=str,
                    help="output directory")
parser.add_argument("-p", "--positions", type=str,
                    help="positions of the images")
parser.add_argument("-r", "--rotation", type=int,
                    help="rotation of the images")
parser.add_argument("-tmin", "--timeframeminimum", type=int,
                    help="minimum time frame after which the data is processed")
parser.add_argument("-tmax", "--timeframemaximum", type=int,
                    help="maximum time frame upto which the data is processed")
parser.add_argument("-ff", "--flatfieldpath", type=str,
                    help="path to the folder containing the flatfield OME-Tiff stack")
parser.add_argument("-log", "--logfile", type=str,
                    help="path to log-file")
parser.add_argument("-glt", "--growthlanelengththreshold", type=int,
                    help="minimum length to be considered as a growth-lane")
parser.add_argument("-roioffsetmc", "--roi_boundary_offset_at_mother_cell", type=int,
                    help="shift the detected position of the ROI at the location of the mother-cell")
parser.add_argument("-gldtp", "--gl_detection_template_path", type=str,
                    help="")
args = parser.parse_args()

# overwrite sys.stdout and sys.stderr for logging
if args.logfile is not None:
    logfile = open(args.logfile, 'w')
    sys.stdout = logfile
    sys.stderr = logfile

print("Input path:")
print(args.input)
print("Output path:")
print(args.output)
print("Flatfield path:")
print(args.flatfieldpath)
print("Log-file path:")
print(args.logfile)
print("Position:")
print(args.positions)
print("Rotation:")
print(args.rotation)
print("Start frame (tmin):")
print(args.timeframeminimum)
print("End frame (tmax):")
print(args.timeframemaximum)
print("Growthlane length threshold (glt):")
print(args.growthlanelengththreshold)
print("roi_boundary_offset_at_mother_cell:")
print(args.roi_boundary_offset_at_mother_cell)
print("gl_detection_template_path:")
print(args.gl_detection_template_path)

# parse position argument; IMPORTANT: this only works for a single position argument
res = re.match('Pos[0]*(\d+)', args.positions)
posval = int(res.group(1))
posval = [posval]

preproc_fun(args.input, args.output, positions=posval, minframe=args.timeframeminimum, maxframe=args.timeframemaximum,
            flatfield_directory=args.flatfieldpath, growthlane_length_threshold=args.growthlanelengththreshold,
            main_channel_angle=args.rotation, roi_boundary_offset_at_mother_cell=args.roi_boundary_offset_at_mother_cell,
            gl_detection_template_path=args.gl_detection_template_path)

