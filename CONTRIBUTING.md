# Contributing

Contribution to the project is welcome! The workflow is as follows:
1. Fork the repo
2. Create a branch for your new feature
3. When the feature is finished, submit a pull request

## Getting the bot to work on your own machine

First get setup on Discord's developer website with your own API key. This way you can test out your changes to the bot in your own server.

When you fork the repository, you'll have to add the `helpers/api_key.py` file. The file should contain these two lines:

```
discord_key = ''
owner_id =
```

where `discord_key` is your own API key and `owner_id` is your own ID as an int.

Next make sure you have all the [dependencies](README.md#Dependencies) installed, and run the `main.py` file to start the bot.