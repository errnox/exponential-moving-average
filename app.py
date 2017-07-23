import random
import math

import matplotlib.pyplot as plt


class App(object):
  def __init__(self):
    # self.data = [22, 3, 47, 24, 42, 323, 3, 34, 39, 45]
    self.data = [random.randrange(0, 100) for i in range(100)]

    self.emas = []
    self.ema = 0
    self.ema_w = 0.05

    self.emss = []
    self.ems_w = 0.05
    self.ems = 0

    self.alarm_sensitivity = 4

  def _update_ema(self, x):
    self.ema = self.ema_w * self.ema + (1 - self.ema_w) * x

  def _update_ems(self, x):
    self._update_ema(x)
    self.ems = math.sqrt(self.ems_w * math.pow(self.ems, 2) +
                         (1 - self.ems_w) * math.pow((x - self.ems), 2))
    
  def generate_emas(self):
    for x in self.data:
      self._update_ema(x)
      self.emas.append(self.ema)

  def generate_emss(self):
    for x in self.data:
      self._update_ems(x)
      self.emss.append(self.ems)
      if self._alarm(x):
        print("Alarm    x: %-8s EMS: %s" % (x, self.ems))

  def plot(self):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(self.data, label='Data', color='blue')
    ax.plot(self.emas, label='EMA', color='green')
    ax.plot(self.emss, label='EMA', color='red')

    ax.legend(loc='upper right')
    ax.set_xlabel('Time')
    ax.set_ylabel('Measurement')

    plt.show()

  def _alarm(self, x):
    return abs(x) > self.alarm_sensitivity * self.ems

  def run(self):
    self.generate_emas()
    self.generate_emss()      
    self.plot()


if __name__ == '__main__':
  app = App()
  app.run()
