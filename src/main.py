import openai
import os
import json
from argparse import ArgumentParser
from ultralytics import YOLO

parser = ArgumentParser()
parser.add_argument("-p", "--path", dest="image_path", help="provide path to image", metavar="IMAGE")

# Get the patient case number
parser.add_argument("-c", "--number", dest="patient_case_number", help="provide case number", metavar="INTEGER")
#
args = parser.parse_args()


