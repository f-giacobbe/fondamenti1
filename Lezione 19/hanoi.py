def hanoi(n, fr, to, spare):
    """
    gives out all the moves to complete the Hanoi tower riddle in the least amount of moves.
    Easy to visualize starting from the base case, which simply involves moving one disk from the start tower to the destination tower.
    As the number of disks increases, you can just call the function recursively to move all the disks (except the biggest one) from
    the "fr" tower to the "spare" tower; the mve the biggest disk directly to the "to" tower, and then recall the function so that
    the <n-1> disks get moved from the "spare" tower to the "to" tower
    """
    if n == 1:
        print(f"move {fr} to {to}")
    else:
        hanoi(n-1, fr, spare, to)
        print(f"move {fr} to {to}")     #hanoi(1, fr, to, spare)
        hanoi(n-1, spare, to, fr)

    return


hanoi(3, "A", "B", "C")
