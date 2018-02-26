
import yaml
import random
import datetime
import subprocess

hourNow = datetime.datetime.now().hour

time_of_day=""
HHH=""
GGG=""
TTT=""

if ( hourNow >= 0) and ( hourNow < 12 ):
    time_of_day = "morning"
    HHH = "have"
    GGG = "is"
    TTT = "tonight"
elif ( hourNow >= 12 ) and ( hourNow <= 17 ):
	time_of_day = "afternoon"
	HHH = "are having"
	GGG = "is going"
	TTT = "later"
elif hourNow >= 17:
  	time_of_day = "evening"
  	HHH = "had"
  	GGG = "has been"
  	TTT = ""
else:
	exit()

CONFIGFILE = "./KeepInTouchConfig.yaml"

with open(CONFIGFILE) as yamlConfigFile:
    YAMLCONFIG = yaml.load(yamlConfigFile)

random_group = random.choice(YAMLCONFIG['Groups'].keys())

random_contact = random.choice(YAMLCONFIG['Groups'][random_group]['Contacts'].keys())
random_contact_number = YAMLCONFIG['Groups'][random_group]['Contacts'][random_contact]
random_message_start = random.choice(YAMLCONFIG['Groups'][random_group]['Message Start'])
random_message_end = random.choice(YAMLCONFIG['Groups'][random_group]['Message End'])
sentence = random_message_start.replace("$name", random_contact).replace("$HHH", HHH).replace("$time_of_day", time_of_day).replace("$GGG", GGG).replace("$TTT", TTT) + " " + random_message_end.replace("$name", random_contact).replace("$HHH", HHH).replace("$time_of_day", time_of_day).replace("$GGG", GGG).replace("$TTT", TTT)

print "Group: %s" % random_group
print "Contact: %s" % random_contact
print "Phone: %s" % random_contact_number
print "iMessage: %s" % sentence

command = '/Users/tdime/KeepInTouch.sh %s %s %s "%s"' % (random_group, random_contact, random_contact_number, sentence)
subprocess.call(command, shell=True)

