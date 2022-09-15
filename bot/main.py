from json import dumps, loads
from random import choice
from traceback import print_exc

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

PUBLIC_KEY = "REPLACE_ME"

sayings = [
    "Oh yeah...",
    "No. Sorry, kid.",
    "You're not the guy.",
    "Not my call.",
    "That's up to you.",
    "It's not gonna go down like you think it is.",
    "We're boned.",
    "This makes you a criminal.",
    "No more half measures.",
    "You are DONE.",
    "Shut the fuck up. Let me die in peace.",
]


def verify_signature(event):
    body = loads(event["body"])
    signature = event["headers"].get("x-signature-ed25519")
    timestamp = event["headers"].get("x-signature-timestamp")

    message = timestamp + dumps(body, separators=(",", ":"))
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    verify_key.verify(
        message.encode(), signature=bytes.fromhex(signature)
    )


def is_ping(body):
    return body["type"] == 1


def lambda_handler(event, context):
    try:
        try:
            verify_signature(event)
        except BadSignatureError:
            return {
                "statusCode": 401,
                "body": dumps("invalid request signature"),
            }

        body = loads(event["body"])
        if is_ping(body):
            return {"statusCode": 200, "body": dumps({"type": 1})}

        username = body["member"]["user"]["username"]
        query = body["data"]["options"][0]["value"]
        content = f"**{username}**: {query}\n**MIKE**: {choice(sayings)}"

        return {
            "statusCode": 200,
            "body": dumps({"type": 4, "data": {"content": content}}),
        }
    except:
        print(event)
        print_exc()
        return {"statusCode": 500, "body": dumps("Error encountered")}
