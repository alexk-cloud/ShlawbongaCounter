import asyncio
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.eventsub.websocket import EventSubWebsocket

import config
import ShlawbongaCounter

class TwitchClient: 
    def __init__(self):
        self.twitch = None
        self.streamer_id = None
        self.websocket = None
    
    async def connect(self):
        self.twitch = Twitch(config.CLIENT_ID, config.CLIENT_SECRET)

        target_scope = [AuthScope.CHANNEL_READ_SUBSCRIPTIONS,
                        AuthScope.BITS_READ]
        
        auth = UserAuthenticator(self.twitch, target_scope, force_verify = True)
        await self.twitch.authenticate_app(target_scope) 

        token, refresh_token = await auth.authenticate()
        await self.twitch.set_user_authentication(token, target_scope, refresh_token)
        
        streamer = self.twitch.get_users(logins=[config.STREAMER_NAME])

        async for user in streamer:
            self.streamer_id = user.id
            break
        
    async def get_sub_count(self):
        subs = await self.twitch.get_broadcaster_subscriptions(self.streamer_id)
        return subs.total

    async def start_eventsub(self, bits_callback):
        self.websocket = EventSubWebsocket(self.twitch)
        self.websocket.start()

        await asyncio.sleep(5)
        
        async def on_bits(event):
            bits_callback(event.bits)

        await self.websocket.listen_channel_bits_use(self.streamer_id, on_bits)
            
