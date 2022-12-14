# OpenAI Discord Bot
The Discord Bot using OpenAI to processing User Text and Images

The Bot API contain custom moderation system:
 Change whatewer in inawords.txt what you wanna filter out (Not Require Reseting after changes)
 !Warning! The inawords.txt contain pre-set inappropriate words!

The Bot API contain output logging system:
  Every request will be in log.txt
  Should look like this:
  ------------
  >Request: Write a random word 
  >Respond: 

  Frolic
  >Time: 2022-12-11 12:27:06.123088
  >Model: text-davinci-003
  >User: user#0000
  >User ID: 0
  >Channel: geral
  >Channel ID: 0
  >Server: Discord Best Server
  >Server ID: 0
  ------------------------
  
 To change bot token go to main.py and change values:
  DCtoken = 'Your discord bot token'
  AItoken = 'Your openAI Token (https://beta.openai.com/account/api-keys)'
  DCtokenTest = 'optional to test BOT (If you want add features)'
  OwnerID = 'Your discord id (This is needed for Maintenance commands)'

Change request setting:
  The text request is from line 143 to 148
  The image request is from line 179 to 183
  The image varriation is from line 213 to 217
  
 If you have any problems with bot contact me on discrd "tommarek#1245"
 Please credict me in your discord bot if you using my Model
