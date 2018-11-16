Add your answers to the Algorithms exercises here.

Exercise I:
    a) Runtime complexity is n. Since a is growing at a (simplified) rate of n^2, it would take n cycles to reach n^3.

    b) nlogn. Each nested loop is based off the previous loop, so each loop does not run n times but instead runs log(previous loop) times

    c) n. The function basically recurses on the range of n to 0 where n is the 'bunnies' input.

Exercise II:
    import drop_egg, n
    f = 0
    for floor in range(n):
        if drop_egg(floor) == 'not broken':
            f = floor
        elif drop_egg(floor) == 'broken':
            break
        else:
            error
    If unbroken eggs can be salvaged, then this technique will ever only waste one egg. However, if all that matters is if the egg is dropped, then it would have to be on-average that the floor that the egg would break from is less than half the floors of buildings tested. In this latter case, a different algorithm should be implemented.

    import drop_egg, n
    def test_building(floor, bottom , top):
        if top-bottom == 1:
            return top
        if drop_egg(floor) == 'not broken':
            next_floor = int(floor + (top-floor)/2)
            bottom = floor
            test_building(next_floor, bottom, top)
        elif drop_egg(floor) == 'broken':
            next_floor = int(floor - (floor-bottom)/2)
            top = floor
            test_building(next_floor, bottom, top)
        else:
            error
    f = test_building(n/2,1,n)

    In this algorithm, it starts in the middle. If the egg breaks, then it goes to the midpoint between where it is and where it last didn't break. If it doesn't break, then it goes to the midpoint between where it is and where it last broke. Eventually, it will find a floor where it breaks the egg but the floor right below it doesn't break the egg and then assign that floor to f. This method halves the floors that are considered in half with each iteration and would most like find f in the best average time compared to other methods. 