class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)

        # count use of a room, when meeting starts in the given room

        rooms = [i for i in range(1, n)]
        use = [0] * n

        fms, fme = meetings[0]
        meet = [(fme, 0)]
        use[0] = 1 

        for m in range(1, len(meetings)):
            cs, ce = meetings[m]

            if meet:
                nt = meet[0][0]

                # if the current meeting start immediate or after, the first meeting to end
                if cs >= nt:
                    while meet and cs >= meet[0][0]:
                        _, rm = heappop(meet)
                        heappush(rooms, rm)

                    rm = heappop(rooms)
                    use[rm] += 1
                    heappush(meet, (ce, rm))
                
                else:
                    # if we have free room
                    if rooms:
                        rm = heappop(rooms)
                        use[rm] += 1

                        heappush(meet, (ce, rm))

                    # delay, waits until the next free room
                    # calculate the delay as: (end time of the first meeting - duration of curr meeting)
                    else:
                        et, rm = heappop(meet)
                        use[rm] += 1

                        heappush(meet, (et + ce - cs, rm))

            else:
                use[0] += 1
                heappush(meet, (ce, 0))

        print(meet)
        print(use)
        return use.index(max(use))

        