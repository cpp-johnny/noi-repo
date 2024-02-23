def main():
    # Read the number of problems
    N = int(input())

    # Read the difficulties of the problems
    difficulties = []
    for _ in range(N):
        difficulty = int(input())
        difficulties.append(difficulty)

    # Sort the difficulties
    sorted_difficulties = sorted(difficulties)

    # Print the sorted difficulties
    for difficulty in sorted_difficulties:
        print(difficulty)

if __name__ == "__main__":
    main()
