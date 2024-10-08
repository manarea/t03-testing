from fuzzingbook.SymbolicFuzzer import *
from fuzzingbook.ConcolicFuzzer import *
from fuzzingbook.Fuzzer import *
from fuzzingbook.ExpectError import ExpectTimeout, ExpectError
from fuzzingbook.Coverage import Coverage

import matplotlib.pyplot as plt
import inspect
import z3
from z3 import *
import random
import fuzzingbook.bookutils.setup


class DCCTest:
  pass

class DCCTestSuite:
  pass

class SymbolicTestInputGenerator:
  def generate(self, fun, size):
    pass

class ConcolicTestInputGenerator:
  def generate(self, fun, input_seed, size):
    pass

class DCCTester:
    def execute(self, seed_input, fun_eval, fun_oracle):
      pass

class TestResult:
    def __init__(self, suite, fun_eval):
      pass
    def full_report(self):
      pass