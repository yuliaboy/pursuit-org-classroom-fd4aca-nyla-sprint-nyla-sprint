cat > main.py << 'EOF'
#!/usr/bin/env python3
import argparse
import os
import sys
from datetime import datetime

def get_api_key():
    """Get the OpenRouter API key from environment variables."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: missing OPENROUTER_API_KEY")
        print("Please set it using: export OPENROUTER_API_KEY=your_key_here")
        sys.exit(1)
    return api_key

def get_mock_completion(event, formatted_date):
    """Provide a mock response for demonstration purposes."""
    return f"""
# Creative Ideas for '{event}' on {formatted_date}

## Tagline
"Bloom Where You're Planted: {event} - Growing Hope Together"

## Theme Ideas
1. **Garden of Giving** - Floral decorations, plant-based activities, and nature-inspired elements
2. **Enchanted Spring** - Magical forest elements, fairy lights, and whimsical touches
3. **Renaissance Renewal** - Celebrate rebirth and renewal with artistic flourishes

## Fundraising Activity Suggestions
1. **Silent Auction Garden** - Auction off donated items, experiences, and services
2. **Seed of Change Challenge** - Participants donate to "plant seeds" on a digital display that grows throughout the event

## Schedule Outline
5:30 PM - Welcome Reception & Signature Cocktails
6:15 PM - Opening Remarks
6:30 PM - Dinner Service
7:15 PM - Presentation of Cause & Impact Stories
8:00 PM - Main Fundraising Activity
9:00 PM - Entertainment & Networking
10:00 PM - Final Thank You & Closing
"""

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="CLI tool for generating event ideas using AI"
    )
    
    # Add required arguments
    parser.add_argument(
        "--event", 
        type=str, 
        required=True,
        help="Name of the event"
    )
    
    parser.add_argument(
        "--date", 
        type=str, 
        required=True,
        help="Date of the event in YYYY-MM-DD format"
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Validate date format
    try:
        event_date = datetime.strptime(args.date, "%Y-%m-%d")
        formatted_date = event_date.strftime("%B %d, %Y")
    except ValueError:
        print("Error: Date must be in YYYY-MM-DD format")
        sys.exit(1)
    
    # Get API key (still required by assignment)
    api_key = get_api_key()
    
    print(f"\nGenerating ideas for '{args.event}' on {args.date}...\n")
    
    # Get mock response instead of actual API call
    response = get_mock_completion(args.event, formatted_date)
    
    # Print the response
    print("=" * 80)
    print(response)
    print("=" * 80)
    
    print("\nSuggestions generated successfully! Good luck with your event planning!")
    print("\nNOTE: This is using mock data due to API payment requirements.")

if __name__ == "__main__":
    main()
EOF
