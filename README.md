# Shlawbonga Counter by akasomo
Shlawbonga Counter is a Python program that utilizes the Twitch API to get simii's sub and bits data in order to convert them into Shlawbongas.

## How It Works
After authorizing your Twitch, while running, Shlawbonga Counter checks every 30 seconds for new subs and bits.

**1 sub = +1 Shlawbonga**  
**500 bits = +1 Shlawbonga** (this rate could change, as I currently don't know how many bits simii considers 1 shlawbonga)

## How to Set Up and Use
### Initial Setup
1. Download the **latest release** of Shlawbonga Counter
2. Extract the ShlawbongaCounter ***folder*** and put it on your desktop (or anywhere desired)
3. Make sure that **ShlawbongaCounter.exe is within the ShlawbongaCounter folder**, as this is where the .txt file will be created, stored, and updated every 30 secs
4. Run ShlawbongaCounter.exe
5. Authorize your Twitch
6. Add a **Text (GDI+) source** in OBS
7. Enable **"Read from file"**
8. Set the **"Text File"** to the generated **shlawbongas.txt**

<img width="384" height="330" alt="image" src="https://github.com/user-attachments/assets/56240ecb-ccf6-4e56-917a-3ba008fc6dce" />
<img width="354" height="568" alt="image" src="https://github.com/user-attachments/assets/59f0c362-b403-41e8-9878-d92ec948dc42" />
<img width="416" height="296" alt="image" src="https://github.com/user-attachments/assets/58869ad6-72cf-4514-855c-13ab38dfcd1e" />
<img width="719" height="420" alt="image" src="https://github.com/user-attachments/assets/0c71deb6-48c6-47d0-8339-2ca65cef6e8c" />


### Usage AFTER Initial Setup
Just run ShlawbongaCounter.exe after starting stream, authorize your Twitch, and keep it running during stream and the counter should update!

## Why I Made This
simii is lazy as hell
