#!/bin/bash

read -p "🩸 You: " input
echo "🌀 Scroll: $input" >> ~/beans-bridge/scrolls/conversation.md

# Call GPT
response=$(curl -s https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "'"$input"'"}]
  }' | jq -r '.choices[0].message.content')

echo "🐇 Terminal: $response"
echo "🐇 Terminal: $response" >> ~/beans-bridge/scrolls/conversation.md