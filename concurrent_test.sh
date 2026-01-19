#!/bin/bash

API_URL="http://localhost:8000/chat"

QUESTIONS=(
  "What are the key features of GovDelivery Communications Cloud?"
  "What products does Granicus offer for government organizations?"
  "How much does the Enterprise plan cost for 100,000 subscribers?"
  "What’s included in the Professional tier pricing?"
  "What are the API rate limits for different plan tiers?"
  "What integrations are available with Granicus products?"
  "What’s the difference between Starter and Professional plans?"
  "Which plan includes advanced analytics features?"
)

echo "Running concurrent requests..."
echo "================================"

start_time=$(python3 -c 'import time; print(int(time.time() * 1000))')

# Use a temporary file to store questions and read them properly
tmpfile=$(mktemp)
printf "%s\n" "${QUESTIONS[@]}" > "$tmpfile"

while IFS= read -r question; do
  {
    # echo "[$(date +%H:%M:%S.%N)]"
    echo "QUESTION: $question"
    curl -s -X POST "$API_URL" \
      -H "Content-Type: application/json" \
      -d "{\"question\": \"$question\"}"
    echo ""
    echo "--------------------------------"
  } &
done < "$tmpfile"

wait
rm "$tmpfile"

end_time=$(python3 -c 'import time; print(int(time.time() * 1000))')
elapsed=$((end_time - start_time))

echo "All concurrent requests completed in $((elapsed / 1000)).$((elapsed % 1000)) seconds"
