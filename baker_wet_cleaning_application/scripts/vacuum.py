#!/usr/bin/env python2

import argparse
import rospy
from baker_msgs.srv import CleanPattern, CleanPatternRequest

parser = argparse.ArgumentParser(description='Activate vacuum cleaner.')
parser.add_argument('angles', metavar='A', type=float, nargs='*',
                    help='angle in degrees (one or more)')
parser.add_argument('-n', '--no-retract', action='store_true',
                    help="don't retract when finished")
parser.add_argument('-r', '--repeats', metavar='N', type=int, default=1,
                    help="number of repeats for each angle")

args = parser.parse_args()

clean_pattern = rospy.ServiceProxy(
  '/vacuum_cleaning_module_interface/clean_pattern', CleanPattern)
request = CleanPatternRequest()
request.clean_pattern_params.directions = args.angles
request.clean_pattern_params.repetitions = [ args.repeats ] * len(args.angles)
request.clean_pattern_params.retract = not args.no_retract
response = clean_pattern(request)
