
## Telegram Admin Activity Counter

This script retrieves the list of admins from a Telegram chat and analyzes the last `LIMIT` messages to count the number of words sent by each admin. It then prints the results in a sorted list with the admins ranked by the number of words they have sent.

### Requirements

* Python 3.0+
* telethon library: `pip install telethon`

### Usage

1. Replace the following environment variables with your Telegram API credentials:

```
API_ID=<YOUR_API_ID>
API_HASH=<YOUR_API_HASH>
BOT_TOKEN=<YOUR_BOT_TOKEN>
CHAT_ID=<YOUR_CHAT_ID>
LIMIT=<NUMBER_OF_MESSAGES>
```

2. Save the code as `.env` and run it using the following command:

```
python main.py
```

### Example Output

```
تعداد پیام‌های ارسال شده توسط هر مدیر در آخرین 100 پیام:
برحسب تعداد کلمات ارسال شده
- @admin1: 200
- @admin2: 150
- @admin3: 100
- @admin4: 50
- @admin5: 25
```

