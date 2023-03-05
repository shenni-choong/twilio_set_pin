from project import app
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather

class Twi:
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token = app.config['TWILIO_AUTH_TOKEN']


    def Press(self):
        """Respond to incoming phone calls with a menu of options"""
        # Start our TwiML response
        resp = VoiceResponse()

        # Start our <Gather> verb
        gather = Gather(num_digits=1)
        gather.say('For sales, press 1. For support, press 2.')
        resp.append(gather)

        # If the user doesn't select an option, redirect them into a loop
        resp.redirect('/Hear')

        return str(resp)

    def Hear(self):
        print("============= Hear =============")
        """Respond to incoming phone calls with a 'Hello world' message"""
        # Start our TwiML response
        resp = VoiceResponse()

        # Read a message aloud to the caller
        resp.say("hello world!", voice='alice')

        return str(resp)


    #def InitGw(self, merchantId, trxId):
    def Call(self):
        print("=====Call=====")

        client = Client(self.account_sid, self.auth_token)

        call = client.calls.create(
                                url='http://demo.twilio.com/docs/voice.xml',
                                to='+13159029093',
                                from_='+15017122661'
                            )

        print(call.sid)