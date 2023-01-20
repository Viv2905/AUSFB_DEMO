import urllib.request
import urllib.parse
  
def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.txtlocal.com/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)
  
resp, code = sendSMS('GSi8ihLplrc-N39XO7AK8STYIG25QUBV1JPFC0ZRMD', '447123456789', 'Jims Autos', 'Test with an ampersand (&) and a £5 note')
print (resp)