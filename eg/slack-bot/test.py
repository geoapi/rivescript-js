from slackclient import SlackClient

token = "xoxb-549477974503-548414699042-G3zVdoSJBjECzvJonWBvO1vP"      # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="DG4J925NZ")
print sc.api_call(
        "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
        username='scoutbot', icon_emoji=':robot_face:'
)
