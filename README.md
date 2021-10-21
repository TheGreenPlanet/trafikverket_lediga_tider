# Trafikverket lediga tider (i Uppsala)
## Motivation:
Failed my first test, made this bot, got a new time in only 7 hours of the bot running. Passed that test :)
## How it works:
1. The bot sends a post request to trafikverket.se every 10 seconds.
2. Parses the response and compares it to the previous response.
3. If something have changed, the bot will then send a general message in your private discord server.
4. By downloading the discord app on your phone you can then recieve notifications directly to your home screen.
## Setup:
1. Make sure you have python installed on your computer. For this project i used python 3.9.
2. Open trafikverket_lediga_tider.py with your editor of choice.
3. You need to replace two things in the script for it to work. On line 35, replace "ÅÅÅÅMMDD-XXXX" with your social security number. On line 6 replace "webhook url" with your own discord servers webhook. (see step 4).
4. Create a new discord server (only for you). Under "TEXT CHANNELS" you should see "# general" and to the right of it a cog icon. Click it, then click the "Integrations" tab. Here you can create a new webhook. After creating the webhook, copy the url and use it to replace whats on line 6 in the script (see step 3).
5. Make sure you have saved all changes (usually, ctrl+s).
6. To run the script: if your using mac or linux open the "terminal". If your using windows open "cmd". Type ```python trafikverket_lediga_tider.py``` And make sure you are in the same directory as trafikverket_lediga_tider.py.
7. If everything is working you should see ```Running...``` in the output.
8. Download the discord app on your phone, and enable notifications.