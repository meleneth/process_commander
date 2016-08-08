import re
from subprocess import Popen, PIPE

class DataWrapper(object):
 def __init__(self, data):
   self.data = data
 
 def as_lines(self):
   return re.compile("\r?\n").split(self.data)
 
 def to_s():
   return self.data

class ExecutionResult(object):
  def __init__(self, command, result, stdout, stderr):
    self.command = command
    self.result = result
    self.stdout = DataWrapper(stdout)
    self.stderr = DataWrapper(stderr)

def run(command):
    process = Popen([command], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    result = process.wait()

    return ExecutionResult([command], result, stdout, stderr)

