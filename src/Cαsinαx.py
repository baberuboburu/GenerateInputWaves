from src.base import BaseInputWave
import numpy as np




class CAlphaSinAlphaX(BaseInputWave):
  def generate_wave(self, t: np.ndarray) -> np.ndarray:
    return self.C_alpha * np.sin(self.alpha * t)
