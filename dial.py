import sys
import signal
import test
def quit(signum, frame):
    print ()
    print ("stop communication")
    sys.exit()

   
    
def dial():
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    # input_seq = ""
    while(True):
        input_seq=input('>')
        # print(type(input_seq))
        output_seq=test.output(input_seq)
        print(output_seq)

dial()




