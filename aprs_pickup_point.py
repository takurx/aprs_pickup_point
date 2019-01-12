#
# ref. 1,  http://d.hatena.ne.jp/thetama/20091103/1257213919
#
# - command example
# chino@kafu:~$ direwolf -r 48000 udp:7355 | python aprs_pickup_point/aprs_pickup_point.py 
#
# - input example
# JJ1BVF-7 audio level = 22(7/7)   [NONE]   ||||||___
# [0.2] JJ1BVF-7>SVPUQ3,WIDE1-1:`D^Ol!?[/`"3{}_$<0x0d>
# MIC-E, Human, Yaesu FT1D, Off Duty
# N 36 05.1300, E 140 06.5100, 0 MPH, course 135, alt 30 ft
# (repeat)
#
# - output example
# N 36 05.1300, E 140 06.5100, 0 MPH, course 135, alt 30 ft
# (repeat)
#

import sys

while True:
    try:
        inline = sys.stdin.readline()
        north = inline.find("N ")
        south = inline.find("S ")
        if north == 26 or south == 26:
            sys.stdout.write(inline)
        
    except:
        pass
    
