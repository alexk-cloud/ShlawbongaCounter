import asyncio
import config
from ShlawbongaCounter import ShlawbongaCounter

from twitch_client import TwitchClient

def printASCIIArt():
    ASCII_ART = """
      ______   __        __                          __                                               
 /      \ /  |      /  |                        /  |                                              
/$$$$$$  |$$ |____  $$ |  ______   __   __   __ $$ |____    ______   _______    ______    ______  
$$ \__$$/ $$      \ $$ | /      \ /  | /  | /  |$$      \  /      \ /       \  /      \  /      \ 
$$      \ $$$$$$$  |$$ | $$$$$$  |$$ | $$ | $$ |$$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  | $$$$$$  |
 $$$$$$  |$$ |  $$ |$$ | /    $$ |$$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | /    $$ |
/  \__$$ |$$ |  $$ |$$ |/$$$$$$$ |$$ \_$$ \_$$ |$$ |__$$ |$$ \__$$ |$$ |  $$ |$$ \__$$ |/$$$$$$$ |
$$    $$/ $$ |  $$ |$$ |$$    $$ |$$   $$   $$/ $$    $$/ $$    $$/ $$ |  $$ |$$    $$ |$$    $$ |
 $$$$$$/  $$/   $$/ $$/  $$$$$$$/  $$$$$/$$$$/  $$$$$$$/   $$$$$$/  $$/   $$/  $$$$$$$ | $$$$$$$/ 
                                                                              /  \__$$ |          
                                                                              $$    $$/           
                                                                               $$$$$$/            
  ______                                   __                                                     
 /      \                                 /  |                                                    
/$$$$$$  |  ______   __    __  _______   _$$ |_     ______    ______                              
$$ |  $$/  /      \ /  |  /  |/       \ / $$   |   /      \  /      \                             
$$ |      /$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |                            
$$ |   __ $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ | __ $$    $$ |$$ |  $$/                             
$$ \__/  |$$ \__$$ |$$ \__$$ |$$ |  $$ |  $$ |/  |$$$$$$$$/ $$ |                                  
$$    $$/ $$    $$/ $$    $$/ $$ |  $$ |  $$  $$/ $$       |$$ |                                  
 $$$$$$/   $$$$$$/   $$$$$$/  $$/   $$/    $$$$/   $$$$$$$/ $$/                                             
"""
    print(ASCII_ART)

async def main(): 
    twitch = TwitchClient()
    counter = ShlawbongaCounter()

    counter.write_count(config.OUTPUT_FILE)

    printASCIIArt()
    print("Connecting to Twitch...")
    await twitch.connect()
    print("Connected! Time to get FIGGITY FADED...")

    asyncio.create_task(twitch.start_eventsub(counter.update_bits))

    while True:
        sub_total = await twitch.get_sub_count()
        counter.update_subs(sub_total)
        counter.write_count(config.OUTPUT_FILE)
        
        await asyncio.sleep(config.UPDATE_SECS)
    
if __name__ == "__main__":
    asyncio.run(main())