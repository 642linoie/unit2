def coronavirus (P, N, R):  
    days=0
    infected_people = N
    while N <= P:
        
        infected_people = N + R
        days += 1
    print (days)
coronavirus (750, 1, 5)