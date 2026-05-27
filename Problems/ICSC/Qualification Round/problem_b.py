import sys

def generate_shape(n, shape):
    """
    Generates a geometric pattern on an n x n grid.

    Args:
        n: Grid size (n x n, always odd for diamond)
        shape: Either "checkerboard" or "diamond"

    Returns:
        A 2D list of integers (0 or 1) representing the pattern.
    """
    # WRITE YOUR CODE HERE




# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        n = int(input().strip())
        shape = input().strip()

        result = generate_shape(n, shape)
        for row in result:
            print(" ".join(str(x) for x in row))

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
