# Walthubot

### Create a Discord bot self-hosted on AWS Lambda.

Right now, this bot responds to commands like `/askmike question:Should I go outside today?`
with 8-ball style responses like 
```
preraku: Should I go outside today?
MIKE: It's not gonna go down like you think it is.
```

You will need the following developer resources which can be obtained from https://discord.com/developers/applications by creating an application and then creating a bot for the app:
- An application ID
- A bot that is associated with the application
  - with a PUBLIC_KEY
  - with a TOKEN

You will need to register your slash commands and their options manually via an HTTP request. The Python code in `update_commands/main.py` will help with this. The [Discord Application Commands](https://discord.com/developers/docs/interactions/application-commands#registering-a-command) documentation can help explain some of this. Once you update `update_commands/main.py` with your bot token, app id, etc., you can run the code after installing the dependencies (the `requests` library). You can do this by running `python -m pip install -r requirements.txt`. See here for more info on managing dependencies: https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip.

Run the following command to get an AWS Lambda compatible [`PyNaCl`](https://github.com/pyca/pynacl/) library. This library is used to cryptographically sign and return Discord requests.

```
$ pip3 install --platform manylinux2014_aarch64 \
             --target=python/lib/python3.9/site-packages \
             --implementation cp \
             --python 3.9 \
             --only-binary=:all: \
             --upgrade PyNaCl
$ zip -r pynacl_layer.zip *
```

This will produce a `pynacl_layer.zip` file which should be uploaded as a layer. You can do this directly in the [AWS Console Lambda Layers page](console.aws.amazon.com/lambda/home#/layers). Make sure to select `arm64` as a compatible architecture and `python3.9` as the compatible runtime. The naming, license and description are not important and can be set to whatever is convenient.

Create a Lambda function via the [AWS Console Lambda Functions page](https://console.aws.amazon.com/lambda/home#/functions) with the following information:
- Runtime: `Python 3.9`
- Architecture: `arm64`
- A "Function URL". This is the endpoint that Discord will call when your application is called by a user.
  - Auth type: `NONE`
  - Check off "Configure cross-origin resource sharing (CORS)"
  - Allow Methods: `GET`, `POST`, `PUT`, `HEAD`

The code from `bot/main.py ` can now be dropped into the code of the newly created Lambda function. Remember to update the `PUBLIC_KEY` value and to click `Deploy` to fully save your changes.

`pynacl_layer.zip` can now be added to your Lambda function's Layers under "Custom Layers." 

The function URL can be found under the Configuration->Function URL tabs.

When adding the bot to a server/guild, re-visit https://discord.com/developers/applications, find your app, then the OAuth2 URL Generator within it and check off `application.commands` before retrieving the generated URL. This URL will allow anyone with admin permissions on a server to add the bot to that server.