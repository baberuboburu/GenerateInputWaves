import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from abc import ABC, abstractmethod
from config.config import *




class BaseInputWave(ABC):
  def __init__(self):
    self.C_alpha = C_alpha
    self.alpha = alpha
    self.in_sr = in_sr
    self.n_cycle = n_cycle


  @abstractmethod
  def generate_wave(self) -> np.ndarray:
    pass


  @property
  @abstractmethod
  def filename(self) -> str:
    pass


  def save_csv(self, y: np.ndarray):
    df = pd.DataFrame({'input': y})
    path = f'./output/csv/{self.filename}.csv'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


  def plot_wave(self, t: np.ndarray, y: np.ndarray):
    end_idx = int(self.in_sr * 5)
    plt.figure()
    plt.plot(t[:end_idx], y[:end_idx])
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("First 5 cycles of input wave")
    path = f'./output/img/{self.filename}.png'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    plt.close()


  def run(self):
    t = np.linspace(0, self.n_cycle * 2 * np.pi, self.in_sr * self.n_cycle)
    y = self.generate_wave(t)
    self.save_csv(y)
    self.plot_wave(t, y)
