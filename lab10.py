# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    
    # Restate:
    #   Grab a string to see if its a number char or a operator char 
    #   depending on what it is means how it will be evaluated 
    #   after its done solving return the answer as a int
    
    # Example: ["4", "13", "5", "/", "+"]
    #   push the first three when it sees the "/" operator
    #   pop "13" and "5" it goes through devision and grabs the int "int(13 / 5) = 2"
    #   push the result which is 2 and the 4 for the next operator which is + 
    #   then completes the math which is 4 + 2 and returns the result
    
    # Sketch the approach:
    #   A stack is created for storing the math
    #   Next run a for loop that runs through all of the char's to see if any are == to any operator
    #   look at the two chars behind the operator and pop them out the stack for later runs
    #   if they are == to a operator append the stack to be the result of the math outcome 
    #   continue until there are no more operators
    #   return the final result as a int
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]


def decode_string(s):
    # Outline:
    
    # Restate:
    #   look at the string then look at the number outside of the brakets which is the number k
    #   if there is one inside the brakets solve the inside first then the outside
    #   based off of k repeate as many times as it says
    
    # Example: 3[a2[c]]
    #   look at the first k value to see that everything inside repeates how ever many times k is = to 
    #   then start moving to the brakets starting with the outside braket opening up the entire thing
    #   "a" appears first so it only repeats a 3 times 
    #   when it moves onto the 2 it reads it as another k value meaning that another braket is going to show up
    #   it sees the next braket but due to it not being a ending braket it starts the same process as the first time
    #   it sees "c" in there so outputs c twice thus making the new string 3[acc]
    #   it finds the closing braket and outputs the inside 3 times getting "accaccacc"
    
    # Sketch the approach:
    #   create a stack a string to hold the current string and a int to hold the current k value
    #   add a for loop to go through each char if the char == a digit  set k to == that digit
    #   for multiple digits set k = k * 10 + int(current char)
    #   else if its a opening braket append the stack to add the current string and k 
    #   then set current string and k to empty values so "" for string and 0 for k 
    #   else if its the ending braket pop and create values that store the current string and k that were appended
    #   set the curent string to = the stored string + current string * k
    #   else get the current string plus the char as there is nothing to multiply by
    
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    curr_string = ""
    curr_num = 0
    
    for ch in s:
        # "isdigit" is pretty self explainitory but it looks to see if the char is a digit if it is set true
        if ch.isdigit():
            # becuase its a char it needs to move forward if there is another number if it goes above 10 
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            stack.append((curr_string, curr_num))
            curr_string = ""
            curr_num = 0
        elif ch == "]":
            prev_string, k = stack.pop()
            curr_string = prev_string + curr_string * k
        else:
            curr_string += ch
            
    return curr_string


def daily_temperatures(temps):
    # Outline:
    
    # Restate:
    #   look at a lsit of the days temp store the temp then
    #   look at the first day compare to the other days for which day has a larger number
    #   if it finds another day that is warmer (bigger number) find the differance
    #   and set the day to the differance of days 
    #   repeate until the end of the list
    #   append to a stack for each day completed
    
    # Example: [73,74,75,71,69,72,76,73]
    #   runs a loop that goes over all numbers
    #   starts with the first number and starts going down the list
    #   it find a larger number the next day so it adds to the stack the diff
    #   which would be 1 day. do this for the rest of the list
    #   append the stack to show how many days till the day is going to be warmer than the day grabbed
    #   return that stack
    
    # Sketch the approach:
    #   create a list that will hold the diff of days
    #   run a for loop that has the int for the days, temp and a numbering for the days
    #   runs a loop while both the storage list and the temp are less than the last element
    #   sets a var that is the prev day to pop in the storage list
    #   set the days list to be the prev day to be = to the int day - the prev day
    #   then append the list to the storage list
    #   return the day list  
    
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    ans = [0] *len(temps)
    stack = []
    
    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_day = stack.pop()
            ans[prev_day] = i - prev_day
        stack.append(i)
    return ans


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    
    # Restate:
    #   go through a grid of "1"'s and "0"'s  and count how many
    #   separate islands there are connected up, down, left, or right but not diagonally

    # Example: ["11000","11000","00100","00011"]
    #   starts at the top-left and finds a "1", adds 1 to the island count, and explores
    #   all connected "1"s in that top-left group so they don't get counted again
    #   keeps scanning and skips "0"s and already visited "1"s
    #   finds the single "1" in the middle then updates the island count to 2
    #   finds the pair of "1"s at the bottom-right then updates the island count to 3
    #   returns the amount of islands

    # Sketch the approach:
    #   first check if the grid is empty and return 0 if it is
    #   create a set to store visited coordinates and a counter for the islands
    #   run for loops to go through every row and column in the grid
    #   if there is a "1" and hasn't been visited yet, add 1 to islands and add it to a queue
    #   run a while loop on the queue to check all 4 directions (up, down, left, right)
    #   if a neighbor is inside the grid, is a "1", and isn't visited, mark it visited and add to queue
    #   once everything is checked, return the total island count

    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                stack = [(r, c)]
                visited.add((r, c))

                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = cr + dr, cc + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))

    return islands



def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))  # returns 9    ((2 + 1) * 3)
    print(eval_rpn(["4", "13", "5", "/", "+"])) # returns 6    (4 + 13 // 5)
    
    print(decode_string("3[a]2[bc]"))   # returns "aaabcbc"
    print(decode_string("3[a2[c]]"))    # returns "accaccacc"
    
    print(daily_temperatures([73,74,75,71,69,72,76,73]))    # returns [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))             # returns [1, 1, 1, 0]

    print(num_islands(["11000", "11000", "00100", "00011"]))    # returns 3
    print(num_islands(["11110", "11010", "11000", "00000"]))    # returns 1
    pass


if __name__ == "__main__":
    main()
