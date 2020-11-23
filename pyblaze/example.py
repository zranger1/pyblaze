"""
 example.py

 Example/Testbed for pyblaze - a library that presents a simple, synchronous interface
 for communicating with and controlling Pixelblaze LED controllers.
 Requires Python 3 and the websocket-client module.
 Copyright 2020 JEM (ZRanger1)

 Permission is hereby granted, free of charge, to any person obtaining a copy of this
 software and associated documentation files (the "Software"), to deal in the Software
 without restriction, including without limitation the rights to use, copy, modify, merge,
 publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
 to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or
 substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
 AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

 Version  Date         Author Comment
 v0.0.1   11/23/2020   JEM(ZRanger1)    Created
"""

from pyblaze import *
import time

"""

"""

if __name__ == "__main__":
    
    # create a Pixelblaze object.
    pb = Pixelblaze("192.168.1.15")
    print("Pixelblaze object created")
      
    # run through a bunch of calls to make sure we have
    # basic functionality

    
    pb.stopSequencer()
    time.sleep(1)
    
    print(pb.getVars())
    time.sleep(1)    
           
    print("getPatternList")
    print(pb.getPatternList())
    time.sleep(1)
        
    print("setActivePattern")
    pb.setActivePattern("OBVIOUS BOGUS PATTERN")  # just to make sure nothing bad happens
    pb.setActivePattern("KITT")           # everybody has KITT, right?
    time.sleep(1)
    
    print("setBrightness")
    pb.setBrightness(1)
    time.sleep(3)
    pb.setBrightness(0)
    time.sleep(3)
    pb.setBrightness(1)
    time.sleep(1)
    
    print("getVars")
    print(pb.getVars())
    time.sleep(1)
    
    print("getPatternList")
    print(pb.getPatternList())
    time.sleep(1)
    
    print("Internal Sequencer Control")
    pb.setSequenceTimer(2)
    pb.startSequencer()
    time.sleep(15)
    pb.stopSequencer()
    time.sleep(1)
    
    print("getHardwareConfig")
    print(pb.getHardwareConfig())
    time.sleep(1)
    
    print("getControls")
    print(pb.getControls("Oasis")) # use any pattern with controls
    time.sleep(1)
    
    pb.setActivePattern("KITT") # all done
    
    pb.close()
        
        
        
        