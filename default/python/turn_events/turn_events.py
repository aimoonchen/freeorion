import sys
from random import random, uniform
from math import sin, cos, pi

import freeorion as fo


def execute_turn_events():
    print "Executing turn events for turn", fo.current_turn()

    # creating fields
    if random() < max(0.00015 * fo.get_universe_width(), 0.05):
        if random() < 0.4:
            field_type = "FLD_MOLECULAR_CLOUD"
            size = 5.0
        else:
            field_type = "FLD_ION_STORM"
            size = 5.0

        radius = fo.get_universe_width() / 2.0
        angle = random() * 2.0 * pi
        dist_from_center = radius + uniform(min(radius * 0.02, 50.0), min(radius * 0.05, 100.0))
        x = radius + (dist_from_center * sin(angle))
        y = radius + (dist_from_center * cos(angle))

        print "...creating new", field_type, "field, at distance", dist_from_center, "from center"
        if fo.create_field(field_type, x, y, size) == fo.invalid_object():
            print >> sys.stderr, "Turn events: couldn't create new field"

    return True
