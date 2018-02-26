
import yaml
import random
import datetime
import subprocess

CONFIGFILE = "./KeepInTouchConfig.yaml"
REPLACE_VARIABLES = ['name','HHH','GGG','TTT','time_of_day']

with open(CONFIGFILE) as yamlConfigFile:
  YAMLCONFIG = yaml.load(yamlConfigFile)

class TextContact(object):

    def __init__(self, hour):

      self.hourNow = hour

      self.get_time_variables()
      self.group = random.choice(YAMLCONFIG['Groups'].keys())
      self.name = random.choice(YAMLCONFIG['Groups'][self.group]['Contacts'].keys())
      self.number = YAMLCONFIG['Groups'][self.group]['Contacts'][self.name]
      self.random_message_start = random.choice(YAMLCONFIG['Groups'][self.group]['Message Start'])
      self.random_message_end = random.choice(YAMLCONFIG['Groups'][self.group]['Message End'])
      
      self.form_message()

      subprocess.call('~/KeepInTouch.sh %s %s %s "%s"' % (self.group, self.name, self.number, self.message), shell=True)

    def get_time_variables(self):
      if (self.hourNow >= 7) and (self.hourNow < 12):
        self.time_of_day = "morning"
        self.HHH = "have"
        self.GGG = "is"
        self.TTT = "tonight"
      elif (self.hourNow >= 12) and (self.hourNow <= 17):
        self.time_of_day = "afternoon"
        self.HHH = "are having"
        self.GGG = "is going"
        self.TTT = "later"
      elif self.hourNow >= 17:
        self.time_of_day = "evening"
        self.HHH = "had"
        self.GGG = "has been"
        self.TTT = ""
      else:
        exit()

    def form_message(self):
      self.start_message = self.replace_variables(self.random_message_start)
      self.end_message = self.replace_variables(self.random_message_end)
      self.message = "%s %s" % (self.start_message, self.end_message)

    def replace_variables(self, sentence):
      for variable in REPLACE_VARIABLES:
        sentence = sentence.replace("$%s" % variable, eval('self.%s' % variable))

      return sentence


if __name__ == "__main__":
  hour = datetime.datetime.now().hour
  TextContact(hour)




