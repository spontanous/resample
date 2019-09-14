function pcm2wav(infilename,fs,outfilename)
%     fs=8e3;
    fid=fopen(infilename,'r');
    sig=fread(fid,inf,'int16');
    fclose(fid);
    audiowrite(outfilename, int16(sig), fs);
end