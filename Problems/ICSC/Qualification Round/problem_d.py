import sys
from collections import defaultdict

def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    # TODO: Implement the corrected game logic
    # Hint: Group events by frame, process each frame atomically
    pass


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
