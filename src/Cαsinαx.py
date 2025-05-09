from src.base import BaseInputWave
import os
import numpy as np



class CAlphaSinAlphaX(BaseInputWave):
  @property
  def filename(self):
    filename = os.path.splitext(os.path.basename(__file__))[0]
    return filename


  def generate_wave(self, t: np.ndarray):
    return self.C_alpha * np.sin(self.alpha * t)
