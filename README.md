# OpenAI Discord Bot<br />
The Discord Bot using OpenAI to processing User Text and Images<br />

The Bot API contain custom moderation system:<br />
 Change whatewer in inawords.txt what you wanna filter out (Not Require Reseting after changes)<br />
 !Warning! The inawords.txt contain pre-set inappropriate words!<br />

The Bot API contain output logging system:<br />
  Every request will be in log.txt<br />
  Should look like this:<br />
  Request: Write a random word <br />
  Respond:<br /> 

  Frolic<br />
  Time: 2022-12-11 12:27:06.123088<br />
  Model: text-davinci-003<br />
  User: user#0000<br />
  User ID: 0<br />
  Channel: geral<br />
  Channel ID: 0<br />
  Server: Discord Best Server<br />
  Server ID: 0<br />
  
 To change bot token go to main.py and change values:<br />
  DCtoken = 'Your discord bot token'<br />
  AItoken = 'Your openAI Token (https://beta.openai.com/account/api-keys)'<br />
  DCtokenTest = 'optional to test BOT (If you want add features)'<br />
  OwnerID = 'Your discord id (This is needed for Maintenance commands)'<br />

Change request setting:<br />
  The text request is from line 143 to 148<br />
  The image request is from line 179 to 183<br />
  The image varriation is from line 213 to 217<br />
  
 If you have any problems with bot contact me on discrd "tommarek#1245"<br />
 Please credict me in your discord bot if you using my Model<br />
