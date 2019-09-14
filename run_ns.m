clc;close all;clear;
input_path         ='C:\Users\os\Downloads\yssj\';
outpath            = [input_path,'out/'];
mkdir(outpath);
list = dir([input_path,'*.wav']);
k=length(list);

for list_index=1:k
inputname= strcat(path,list(list_index).name); 
wavnme=inputname(length(path)+1:end-4);
omlsa([input_path,wavnme,'.wav' ],[outpath,wavnme,'.pcm']);
pcm2wav([outpath,wavnme,'.pcm'],8000,[outpath,wavnme,'.wav'])
end

fclose all;


%%
