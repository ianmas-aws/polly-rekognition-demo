# polly-rekognition-demo
Demo showing Amazon Rekognition and Amazon Polly in action.

Tested on Mac and uses Mac OS X Preview to display images. 



Pre-requisites:

cv3 with python bindings. I installed using this guide: https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/

pyaudio: brew install portaudiuo && pip install pyaudio

inflect: pip install inflect


Not: you might need to edit at line 152:

   vidcap.open(0)

0 is internal camera
1 is external, or sometimes 2, depending on some factor that I don't understand :)
