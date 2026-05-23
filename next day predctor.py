import time

def run_predictor():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    print("==============================")
    print("    NEXT DAY PREDICTOR 2.0    ")
    print("==============================\n")
    
    # Simple input
    print("Available Days: " + ", ".join(days))
    user_input = input("\nEnter current day: ").strip().capitalize()
    
    if user_input not in days:
        print("Error: That day doesn't exist in this universe.")
        return

    # The "Revolutionary" Processing
    print("\nInitializing AI Algorithms...")
    time.sleep(1)
    
    messages = [
        "[Web] Checking your calendar...",
        "[Exploit] Hacking NASA for orbital data...",
        "[Privacy] Analyzing chrome search history...",
        "[News] Dhoni Announced to play one more IPL...",
        "[Finalizing] Predicting tomorrow..."
    ]
    
    for msg in messages:
        print(msg)
        time.sleep(1.2) # This creates the suspense from the video

    # The Big Reveal
    current_index = days.index(user_input)
    next_day = days[(current_index + 1) % 7]
    
    print("\n" + "="*30)
    print(f" RESULT: Your next day will be {next_day.upper()}! ")
    print("="*30)

if __name__ == "__main__":
    run_predictor()