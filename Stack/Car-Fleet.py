class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # Let's first sort the two lists based on position, with the one the closest to the
        # finish at the start of the list
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse = True, key = lambda x: x[0])

        # The intuition for this is that we are trying to find bottlenecks in the line. We can
        # accomplish this by adding each car to a stack based on ETA, and if the ETA of the next
        # car is shorter, it will be part of the same fleet. If the ETA is longer, we can clear the 
        # stack as the car will never catch up to the current fleet and is the start of a new fleet
        fleets = 0
        stack = []

        for car in cars:

            # Calculate the time to finish
            timeToFinish = (target - car[0]) / car[1]

            # Start a fleet
            if stack == []:
                stack.append(timeToFinish)

            # Add a car to the fleet if it's ETA is faster than what is ahead in line
            elif timeToFinish <= stack[0]:
                stack.append(timeToFinish)

            # Start a new fleet and increment the count
            else:
                fleets += 1
                stack = []
                stack.append(timeToFinish)
        
        # Count the remaining fleet if the stack is not empty
        if stack!= []:
            fleets += 1
        
        return fleets