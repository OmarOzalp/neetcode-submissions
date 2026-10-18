class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # N cars traveling to the same destination
        # Two integer arrays pos and speed
        # dest is at pos target
        # target = 10
        # position: [1,4]
        # [3, 2]
        # Will a car catch up to the car infront of it
        # if it does. it slows down to x speed

        pos_spd = [(position[i], speed[i]) for i in range(len(position))]
        pos_spd.sort(key = lambda x:x[0], reverse=True)
        fleets = len(position)
        time_last = (target - pos_spd[0][0])/(pos_spd[0][1])

        for i in range(1, len(pos_spd)):
            time = (target - pos_spd[i][0])/(pos_spd[i][1])

            if time > time_last:
                time_last = time
            else:
                fleets -= 1
        
        return fleets
            


        
        