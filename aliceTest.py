

from cqc.cqcHeader import CQC_TP_HELLO
from cqc.pythonLib import CQCConnection, qubit

import random


#####################################################################################################
#
# main
#
def main():

    # In this example, we are Alice.
    myName = "Alice"

    # Initialize the connection
    with CQCConnection(myName) as cqc:

        # Send Hello message
        print("{} says HELLO and HI to CQC server".format(myName))
        cqc.sendSimple(CQC_TP_HELLO)

        # Get return message
        message = cqc.readMessage()
        cqc_header = message[0]
        if cqc_header.tp == CQC_TP_HELLO:
            print("CQC server says just HELLO back to u:)")


##################################################################################################
main()
