# resample
import librosa
import os
import sys


from scipy.io import wavfile

import numpy as np

def resample_16(in_dir,in_filename,in_sr,out_dir,out_filename,out_sr):
	y, sr = librosa.load(os.path.join(in_dir,in_filename), sr=in_sr)
	y_16k = librosa.resample(y,sr,out_sr)
	wavfile.write(os.path.join(out_dir,out_filename),out_sr,(y_16k*32767).astype(np.int16))

if __name__=="__main__":
	in_dir = sys.argv[1]
	out_dir = sys.argv[2]
  in_sr = sys.argv[3]
	out_sr = sys.argv[4]
    
	for path,pathname,filenames in os.walk(in_dir):
		for filename in filenames:
			if filename.endswith(".wav"):
				resample_16(path,filename,in_sr,out_dir,filename,out_sr)
