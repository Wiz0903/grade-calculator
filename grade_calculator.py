count = 0 # number of students
total = 0 # sum of all marks
max_mark = 0 # track highest mark
min_mark = 50 # track lowest mark (starting value)
count_distinctions = 0 # number of marks above 80

with open("grades.txt", "r") as f:
    with open("report.txt", "w") as w:
        for x in f:
            count += 1 # increase student count
            lines = x.strip().split(",") # split name and mark
            total += int(lines[1]) # add mark to total
        
            if int(lines[1]) > int(max_mark): # check for new highest
                max_mark = lines[1]
            elif int(lines[1]) < int(min_mark): # check for new lowest
                min_mark = lines[1]
            
            if int(lines[1]) > 80: # count distinctions
                count_distinctions += 1
        
        w.write(f"Average: {round(total / count, 2)}\n") # write average
        w.write(f"Highest mark: {max_mark}\n") # write highest mark
        w.write(f"Lowest mark: {min_mark}\n") # write lowest mark
        w.write(f"Number of distinctions: {count_distinctions}") # write distinctions
            
with open("report.txt", "r") as w:
    print(w.read()) # display report