# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
import json
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
import pdb; pdb.set_trace() ## XXX: Remove This
try:
    from core.backend.deps import bottle

    from core.backend.controller import *
except:
    pass
# ----------- END: In-App Imports ---------- #


##  Web application main  ##
def main():

    # Start the Bottle webapp
    # bottle.debug(True)
    app.run(host='0.0.0.0', port=8080, reloader=True)

#if __name__ == "__main__":
#    try:
#        main()
#    except:
#        pass
