%Dhavala_4AL17EC027_6TH'A'
%Challenge 2
%A raw ECG signal is available at ECE-3year-Code-Challenge repo, with file name a01_3.csv, you can download this file and perform the following task:
%1.Read and plot this signal
%NOTE: Line8 gives path to given ECG values

clc;
y1=xlsread('C:\Users\ACHALA\Downloads\a01_3.csv');
fs = 250;
T = 1/fs;
N = length(y1);
ls = size(y1);
t = (0 : N-1)/fs;

figure;
plot(t,y1);
title ('plot of the orignal ECG signal');
xlabel ('time (sec)');
ylabel ('ECG Amplitute (mv)');
grid on;

figure;
y1new = y1(10:350);
ax = axis; axis([ax(1:2) -3.2 3.2])
plot (y1new);
title ('plot one typical period of the signal amplitude spectrume of the  ECG signal');
xlabel ('time (msec)');
ylabel ('ECG Amplitute  (mv)');


figure;
y1new1 = y1(40:200);
ax = axis; axis([ax(1:2) -3.2 3.2])
t2 = (0 : length (y1new)-1)/fs;
plot (y1new1);
title ('plot PQRST cycle of the ECG signal');
xlabel ('time (msec)');
ylabel ('ECG Amplitute  (mv)');

beat_count =0;
for k = 2 : length(y1)-1
    if(y1(k)> y1(k-1) && y1(k) > y1(k+1) && y1(k)> 1)
         beat_count = beat_count +1;
    end       
end
display (k);
disp('dominant peaks');
duration_in_sec = N/fs;
duration_in_minute = duration_in_sec/60;
BPM = beat_count/duration_in_minute;

% your code is not correct. The sampling freq is 100Hz. Rework on code
