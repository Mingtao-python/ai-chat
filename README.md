# AI Chat Application

A command-line chatbot application that uses the Groq API to interact with advanced AI models. This tool provides an interactive conversation experience with customizable parameters.

## Features

- 🤖 **AI-Powered Chat**: Uses Groq's API with the Llama 3.1 8B Instant model
- 💬 **Multi-turn Conversations**: Support for continuous dialogue with configurable turn limits
- 🎨 **Custom Styling**: Set the AI assistant's response style (smart, professional, casual, etc.)
- 🔄 **Automatic History Management**: Intelligently manages conversation history to prevent exceeding turn limits
- ⏱️ **Timeout Protection**: Built-in timeout handling for network reliability
- 🛡️ **Error Handling**: Comprehensive error handling for network and API issues
- 🚪 **Easy Exit**: Multiple exit commands (e, exit, quit)

## Requirements

- Python 3.6+
- `requests` library
- Groq API account

## Installation

1. Clone or download this repository
2. Install the required dependency:
```bash
pip install requests
```

3. Create a Groq account and get an API key:
   - Visit: https://console.groq.com
   - Sign up for a free account
   - Generate an API key from the dashboard

## Usage

Run the script:
```bash
python ai_change.py
```

The program will prompt you for:

### 1. Maximum Dialog Turns
Enter a number between 5-15 to set the maximum conversation turns:
```
type the maximum dialog of chat
between 5-15
: 10
```
- Valid range: 5-15 turns
- Default: 12 turns (if invalid input)

### 2. API Key
Provide your Groq API key:
```
API key please> gsk_your_api_key_here
```
- Press Enter to continue after pasting your key
- Key cannot be empty

### 3. Assistant Style (Optional)
Customize the AI's response style:
```
Style for the assistant (Eg: smart/professional). Press Enter for default: professional
```
- Common styles: smart, professional, casual, friendly, technical, creative
- Leave empty for default behavior
- Press Enter to skip

### 4. Start Chatting
Once initialized, start typing your messages:
```
you> Hello, how are you?
AI> I'm doing well, thank you for asking! How can I assist you today?
you> Tell me about machine learning
AI> Machine learning is a subset of artificial intelligence...
```

### Exit Options
Exit the chat by typing any of these commands:
- `e`
- `exit`
- `quit`

## How It Works

1. **Initialization**: Collects user preferences (turn limit, API key, style)
2. **Conversation Loop**: Accepts user input and sends requests to Groq API
3. **History Management**: 
   - Maintains conversation history for context
   - When max turns are reached, clears old messages while preserving system style
   - Keeps the conversation fresh and within API limits
4. **Response Processing**: Formats AI responses and displays them to the user
5. **Error Handling**: Gracefully handles network errors and API failures

## Configuration

### Turn Limits
- Minimum: 5 turns
- Maximum: 15 turns
- Default (invalid input): 12 turns

### AI Model
- Currently uses: `llama-3.1-8b-instant`
- Hosted on: Groq's high-performance inference platform

### Network Settings
- Request timeout: 10 seconds
- Default retry: Not automatic (user must resend)

## Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| ❌ Unable to access HTTP | API connection failed | Check internet connection and API key |
| ❌ Bad response by the AI model | Invalid API response | Try again; server might be overloaded |
| ❌ Timeout | Request exceeded 10 seconds | Check internet speed or try simpler prompts |
| ❌ Network error | Connection problem | Verify internet connectivity |
| ❌ Response not valid | JSON parsing error | Retry or contact Groq support |

## Examples

### Example 1: Professional Assistant
```bash
type the maximum dialog of chat between 5-15: 10
API key please> gsk_your_key
Style for the assistant: professional
```

### Example 2: Creative Writer
```bash
type the maximum dialog of chat between 5-15: 8
API key please> gsk_your_key
Style for the assistant: creative
you> Write a short poem about technology
```

### Example 3: Technical Support
```bash
type the maximum dialog of chat between 5-15: 12
API key please> gsk_your_key
Style for the assistant: technical
```

## Features in Detail

### Automatic History Refresh
When reaching the maximum number of turns:
- Displays: "max turns reached. Refreshing..."
- Clears 5-second pause for visibility
- Preserves system prompt style
- Resets conversation while maintaining context rules

### Input Validation
- Empty inputs are ignored with message: "(empty input, not sent)"
- API key validation on startup
- Turn limit validation (5-15 range)

### Graceful Exit
Beautiful exit animation with friendly goodbye message

## Limitations

- Turn limit: 5-15 (controlled limit to manage API usage)
- Single model: Llama 3.1 8B Instant
- Sequential conversation only (not parallel)
- Requires active internet connection
- API key must be valid and have remaining quota

## API Usage

- **Endpoint**: https://api.groq.com/openai/v1/chat/completions
- **Model**: llama-3.1-8b-instant
- **Authentication**: Bearer token (API key)
- **Rate Limit**: Subject to Groq's rate limiting policy

## Troubleshooting

**"API key cannot be empty"**
- You must provide a valid Groq API key
- Get one from: https://console.groq.com

**"Unable to access HTTP"**
- Check your internet connection
- Verify your API key is valid and not expired
- Ensure Groq API service is available

**"Timeout" errors**
- Your internet connection might be slow
- Try simpler, shorter prompts
- The Groq service might be experiencing high load

**Chat stops after certain turns**
- This is intentional - the history refresh prevents too many tokens
- The AI resets but remembers the style you set
- You can chat again without restarting

## Security Notes

- **Keep your API key private** - Never share it or commit it to version control
- API key is requested at runtime to avoid hardcoding
- No conversation data is stored after exit
- Consider setting API rate limits in your Groq dashboard

## Future Enhancements

- Support for additional Groq models
- Conversation export/save functionality
- Custom system prompts
- Token usage tracking
- Multi-user support

---

**Note**: This application requires an internet connection and active Groq API credentials to function. Groq offers a generous free tier for trying the API.
