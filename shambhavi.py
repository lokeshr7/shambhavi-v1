# Namaskaram
# Author: Lokesh Roopkumar
# Email: r.lokesh98@gmail.com
# Phone: (872) 218-4049
# Please feel free reach out if you need any help tweaking times

# Make sure the audio fie is in the same folder as the Python script
# Please go through the code and make the necessary tweaks
# When ready, run the code and immediately close your eyes
# To execute code - go to the file location and run this in cmd/terminal - py shambhavi.py

from playsound import playsound
import pathlib, time
audio_file = str(pathlib.Path().resolve()) + '/sadhguru-shiva-whisper.mp3'

# To indicate that the program has started and is running successfully without any compile time errors
# If this sound does not play when you execute the script, then the program did not start
playsound(audio_file)

# Please note that throughout this program, time is in seconds
# The only times that vary from person to person are Aum Chanting and Bandas, please change this accordingly
# No need to change any of the other times

# Small 10 second delay to get ready for Suka Kriya

time.sleep(10)

# Suka Kriya (12 times X 30 sec = 6 minutes of Suka Kriya + 30 seconds of buffer time to complete cycle and exhale through left nostril)
# Has to be done for 6 minutes, no need to make any time changes here

time.sleep( (6 * 60) + 30)
playsound(audio_file)

# Aum Chanting (21 times x 15 sec = 315 sec)
# It takes 15 secs for me to chant Aum once, please change this based on how much time you take to finish one Aum chant

time.sleep( (5 * 60) + 15 )
playsound(audio_file)

# Flutter Breathing - rapid inhalation & exhalation
# Has to be done for 4 minutes, no need to make any time changes here

time.sleep( (4 * 60) )
playsound(audio_file)

# Bandas - Jalandara banda, Udhyana banda, muladhara banda
# This is how much time it takes for me, varies from person to person depending upon how long you can hold your breath
# Takes 1 minute for me, please change according to how long it takes for you

time.sleep( (1 * 60) )
playsound(audio_file)

# Meditate
# Has to be done for 5 minutes, no need to change anything here

time.sleep( (5 * 60) )
playsound(audio_file)

# Total time = 21 mins 45 secs
# If you've made any changes, please re-calculate and change it in the above comment for your reference