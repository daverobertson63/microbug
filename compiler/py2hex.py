#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
# Addtional stuff Dave Robertson 2025 
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from py2cc.main import main_single_windows

def single_usage(prog):

    print "Usage:"
    print
    print "Must have a build directory - build - and ther hex file will be created in the build dir as filename.hex"
    print "This will convert a simple Microbug python file into a downloadable hex file for the Microbug to use"
    print
    print prog, "filename.py"
    print

if __name__ == "__main__":
    if len(sys.argv) <1:
        single_usage("py2hex")
        sys.exit(1)

    prog = sys.argv[0]
    source_file = sys.argv[1]
    
    main_single_windows(source_file)