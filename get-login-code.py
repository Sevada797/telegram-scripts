from telethon.sync import TelegramClient, events

# Replace these with your actual API ID and API Hash
api_id = 2040  # Replace with your API ID
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your API Hash

# Path to your existing session file
session_file = 'xxxxxxxxxx.session'  # Replace with the path to your session file

# Create a new client using the existing session
client = TelegramClient(session_file, api_id, api_hash)

async def main():
    await client.start()

    print("Session authenticated. Waiting for PIN code or login code...")

    @client.on(events.NewMessage)
    async def handler(event):
        # Check if the message is from your Telegram account
        if event.is_private and event.message.message:
            message = event.message.message

            # Detect if the message is likely a PIN code or login code
            if len(message) == 5 and message.isdigit():
                print(f"Received PIN code: {message}")
                # Optionally: If you need to perform an action with the PIN code
                # await client.send_message('your_channel_or_user', f'PIN code received: {message}')
                
            # For demonstration purposes, echo other messages
            else:
                print(f"Received message: {message}")

    # Keep the script running to listen for incoming messages
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
