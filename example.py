from mq import *
import sys, time
import thingspeak


channel = thingspeak.Channel( <id_here>, "")

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        sys.stdout.flush()
        channel.update({1:perc["GAS_LPG"], 2:perc["CO"], 3:perc["SMOKE"]})
        time.sleep(30)

except:
    print("\nAbort by user")