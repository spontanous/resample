# resample
import librosa
import os
import sys

from scipy.io import wavfile

import numpy as np

def resample_16(in_dir,in_filename,out_dir,out_filename):

	
	y, sr = librosa.load(os.path.join(in_dir,in_filename), sr=8000)
	y_16k = librosa.resample(y,sr,16000)
	print(y_16k)
	wavfile.write(os.path.join(out_dir,out_filename),16000,(y_16k*32768).astype(np.int16))

if __name__=="__main__":
	base_dir = sys.argv[1]
	out_dir = sys.argv[2]
	
	for path,pathname,filenames in os.walk(base_dir):
		for filename in filenames:
			resample_16(path,filename,out_dir,filename)
