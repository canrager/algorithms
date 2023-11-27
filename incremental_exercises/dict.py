# First Task: DICT
"""Your task is to implement a DICT
The users should be able to add items and retrieve them in the order they were added (FIFO)
The requirements and operations needed to support will increase with each level
At each level you should also support the old operations
Implement the function parseCommands(commands)
commands will be a list of commands, you should return a list or responses with the same length, one response for each commands

"""
"""Level 1

Command: PUSH <value>
Description: Adds <value> to the queue. <value> will be a non-empty string
Return: Empty string

Command: FRONT
Description: Retrieves the first element from the queue
Return: The <value> of the first element. If there is no first element, return an empty string

Command: REMOVE
Description: Removes the first element from the queue. If the queue is already empty it has no effect
Return: empty string

Examples:

["PUSH A", "PUSH B", "FRONT", "REMOVE", "PUSH C", "FRONT", "REMOVE", "FRONT", "REMOVE", "FRONT"]

Answer:

["", "", "A", "", "", "B", "", "C", "", ""]

"""
"""Level 2

Add priority to the queue. The items in the queue will now have a priority (integer). The items with the highest priority should go to the front of the queue automatically

Command: PUSH_PRIO <value> <priority>
Description: Adds <value> with <priority> to the queue
Return: Empty string

Command: FRONT_PRIO
Description: Returns the element with the highest priority in the queue. If there are multiple elements with the same priority, return the element that was added first
Return: The <value> of the element with the highest priority

Command: POP_PRIO
Description: Removes the element with the highest priority from the queue (same criteria as FRONT_PRIO). If the queue is already empty it has no effect

You will only get the Level 1 commands or the Level 2 commands, they will never be mixed. You still need to support both

Examples:

["PUSH_PRIO A 1", "PUSH_PRIO B 2", "FRONT_PRIO", "POP_PRIO", "PUSH_PRIO C 3", "FRONT_PRIO", "POP_PRIO", "FRONT_PRIO", "POP_PRIO", "FRONT_PRIO"]

Answer:

["", "", "B", "", "", "C", "", "A", "", ""]

"""
"""Level 3

Commands now will have a timestamp at which they are executed and values will have an expiration time associated with them. When the time goes past the expiration time, the value is automatically removed from the queue. The commands are given continuously in time so it is guaranteed that the timestamp will only increase.

Command: PUSH_PRIO_AT <value> <priority> <timestamp> <expiration>
Description: Adds <value> with <priority> to the queue at <timestamp> and with <expiration> time (the value is valid for the period [<timestamp>, <timestamp> + <expiration>) )
Return: Empty string

Command: FRONT_PRIO_AT <timestamp>
Description: Returns the element with the highest priority in the queue at <timestamp>. If there are multiple elements with the same priority, return the element that was added first
Return: The <value> of the element with the highest priority

"""
"""Level 4

    Backup and restore

    Command: BACKUP_AT <timestamp>
    Description: Saves the state of the queue at <timestamp>. The expiration of the elements is paused at this timestamp (if an element had 10 minutes left to expire, it will still have 10 minutes left even if the backup is restored 20 minutes later)
    Return: Number of elements in the queue at <timestamp>

    Command: RESTORE_AT <timestamp> <restore_timestamp>
    Description: Restores the state of the queue from the last backup before <restore_timestamp> at <timestamp>. The expiration of the elements is resumed at this timestamp (if an element had 10 minutes left to expire, it will now have 10 minutes left)
    Return: Empty string

    Examples:

    ["PUSH_PRIO_AT A 1 100 20", "PUSH_PRIO_AT B 2 104 3", "BACKUP_AT 105", "FRONT_PRIO_AT 106", "POP_PRIO_AT 107", "PUSH_PRIO_AT C 3 108 10", "BACKUP_AT 109", "RESTORE 120 107", "FRONT_PRIO_AT 121", "FRONT_PRIO_AT 123", "RESTORE_AT 122 110", "FRONT_PRIO_AT 123", "FRONT_PRIO_AT 133"]

    Answer:

    ["", "", "2", "B", "A", "", "2", "", "B", "A", "", "B", "C", ""]

"""


def parseCommands(commands):
    pass








            
def TestLevel1():
    commands = ["PUSH A", "PUSH B", "FRONT", "REMOVE", "PUSH C", "FRONT", "REMOVE", "FRONT", "REMOVE", "FRONT"]
    expected = ["", "", "A", "", "", "B", "", "C", "", ""]
    assert parseCommands(commands) == expected

def TestLevel2():
    commands = ["PUSH_PRIO A 1", "PUSH_PRIO B 2", "FRONT_PRIO", "POP_PRIO", "PUSH_PRIO C 3", "FRONT_PRIO", "POP_PRIO", "FRONT_PRIO", "POP_PRIO", "FRONT_PRIO"]
    expected = ["", "", "B", "", "", "C", "", "A", "", ""]
    out = parseCommands(commands)
    print(out)
    assert out == expected

def TestLevel3():
    commands = ["PUSH_PRIO_AT A 1 100 10", "PUSH_PRIO_AT B 2 104 3", "FRONT_PRIO_AT 106", "FRONT_PRIO_AT 111", "POP_PRIO_AT 112", "PUSH_PRIO_AT C 3 120 10", "FRONT_PRIO_AT 140", "POP_PRIO_AT 150", "FRONT_PRIO_AT 160"]
    expected = ["", "", "B", "", "", "", "", "", ""]
    out = parseCommands(commands)
    print(out)
    assert out == expected

def TestLevel4():
    commands = ["PUSH_PRIO_AT A 1 100 20", "PUSH_PRIO_AT B 2 104 3", "BACKUP_AT 105", "FRONT_PRIO_AT 106", "POP_PRIO_AT 107", "PUSH_PRIO_AT C 3 108 10", "BACKUP_AT 109", "RESTORE_AT 120 107", "FRONT_PRIO_AT 121", "FRONT_PRIO_AT 123", "RESTORE_AT 122 110", "FRONT_PRIO_AT 123", "FRONT_PRIO_AT 133"]
    expected = ["", "", "2", "B", "", "", "1", "", "B", "A", "", "C", ""]
    out = parseCommands(commands)
    print(out)
    assert out == expected

# TestLevel1()
# TestLevel2()
# TestLevel3()
# TestLevel4()





# Employee Registry
# You'll develop a registry system for companies. This will save all employees, their time spent in office and calculate salaries.

"""Level 1 

ADD
    Add a new employee.
    Invalid: return i if employee is already part of the company
    Input: "ADD <employee> <position> <salary> <timestamp>"
    Output: "<total number of employees>" or "invalid_request"
    
REG
    Register an entry or exit to the office at a given timestamp. The times are always increasing.
    Invalid: Unknown employee.
    Input: "REG <employee> <timestamp>"
    Output "" or "invalid_request"


"""
"""Level 2 

TIME
    Input: "TIME <employee> <timestamp>"
    (return "invalid_request" if employee doesnt exist)
    return sum off completed office time at timestamp, uncompleted (come & not yet left) doesnt count

SALARY
    Input: "SALARY <employee> <timestamp>"
    (return "invalid_request" if employee doesnt exist)
    calculate salary of employee at given timestamp. incomplete office hours do not count.

"""
"""Level 3

PROMOTE
    Promote an employee to a higher position with a new title and new salary at a given time stamp. The promotion is effective as soon as the employee enters the office the next time. 
    The promotion is invalid if the employee has already been promoted after the last office entry or if the employee is unknown.
    Input: "PROMOTE <employee> <new_title> <new_salary> <timestamp>"
    Output: "promoted" or "invalid_request"

SALARY-PS
    Calculate the salary of employee at the given timestamp considering promotions.
    Invalid if the employee is unknown.
    Input: "SALARY-PS <employee> <timestamp>"
    Output: "<salary>" or "unknown"

"""

def sum_time(employees, emp, ts):
    e = employees[emp]
    entries = [int(t) for t in e["entry_ts"]]
    exits = [int(t) for t in e["exit_ts"]]
    ts = int(ts)
    s = 0
    for i in range(len(exits)):
        if exits[i] > int(ts): #only add timestamps before ts
            break
        s += exits[i] - entries[i]
    return s

def salary_ps(employees, emp, ts):
    e = employees[emp]
    entries = [int(t) for t in e["entry_ts"]]
    exits = [int(t) for t in e["exit_ts"]]
    salaries = [int(t) for t in e["entry_salary"]]
    ts = int(ts)
    s = 0
    for i in range(len(exits)):
        if exits[i] > int(ts): #only add timestamps before ts
            break
        s += (exits[i] - entries[i]) * salaries[i]
    return s

def parseCommands(commands):
    outputs = []
    employees = dict()

    for com in commands:
        com = com.split(" ")

        if com[0] == "ADD":
            employee = com[1]
            role = com[2]
            salary = com[3]
            ts = com[4]

            if employee in employees:
                outputs.append("invalid_request")
            else:
                employees[employee] = dict(
                    employee=employee,
                    role=role,
                    salary=salary,
                    hired_ts=ts,
                    entry_ts=[],
                    exit_ts=[],
                    entry_salary=[],
                    is_working=False,
                    recent_promotion=False,
                )
                outputs.append(str(len(employees)))
        
        elif com[0] == "REG":
            emp = com[1]
            ts = com[2]
            
            if emp not in employees:
                outputs.append("invalid_request")
            else:
                if employees[emp]["is_working"]:
                    employees[emp]["is_working"] = False
                    employees[emp]["exit_ts"].append(ts)
                else:
                    employees[emp]["is_working"] = True
                    employees[emp]["entry_ts"].append(ts)
                    employees[emp]["entry_salary"].append(int(employees[emp]["salary"]))
                    employees[emp]["recently_promoted"] = False
                outputs.append("")

        elif com[0] == "TIME":
            emp = com[1]
            ts = com[2]

            if emp not in employees:
                outputs.append("invalid_request")
            else:
                s = sum_time(employees, emp, ts)
                outputs.append(str(s))
        
        elif com[0] == "SALARY":
            emp = com[1]
            ts = com[2]
            if emp not in employees:
                outputs.append("invalid_request")
            else:
                salary = sum_time(employees, emp, ts) * int(employees[emp]["salary"])
                outputs.append(str(salary))

        elif com[0] == "PROMOTE":
            emp = com[1]
            role = com[2]
            new_salary = com[3]
            # print(f"{com=}")

            if emp not in employees:
                outputs.append("invalid_request")
            else:
                e = employees[emp]

                if e["recently_promoted"]:
                    outputs.append("invalid_request")
                else:
                    e["recently_promoted"] = True
                    e["role"] = role
                    e["salary"] = new_salary
                    outputs.append("promoted")
        
        elif com[0] == "SALARY-PS":
            emp = com[1]
            ts = com[2]
            print(f"{com=}")
            if emp not in employees:
                outputs.append("invalid_request")
            else:
                salary = salary_ps(employees, emp, ts)
                print(f"{salary=}")
                outputs.append(str(salary))


    print(f"{outputs=}")
    return outputs





def TestLevel1():
    commands = ["ADD A Engineer 20 0", "ADD B Marketing 20 5", "REG A 10", "REG A 20", "ADD B Marketing 20 20", "REG A 30", "REG B 30"]
    expected = ["1", "2", "", "", "invalid_request", "", ""]
    assert parseCommands(commands) == expected

def TestLevel2():
    commands = ["ADD A Engineer 20 0", "ADD B Marketing 20 5", "REG A 10", "REG A 20", "ADD B Marketing 20 20", "REG A 30", "REG B 30", "REG A 40", "REG A 60", "REG B 100", "REG B 110", "TIME A 35", "SALARY B 150", "SALARY C 150"]
    expected = ["1", "2", "", "", "invalid_request", "", "", "", "", "", "", "10", "1400", "invalid_request"]
    assert parseCommands(commands) == expected

def TestLevel3():
    commands = ["ADD A Engineer 20 0", "ADD B Marketing 20 5", "REG A 10", "PROMOTE A CEO 50", "REG A 20", "ADD B Marketing 20 20", "PROMOTE A OWNER 50", "REG A 30",  "PROMOTE A OWNER 100", "REG B 30", "REG A 40", "REG A 60", "PROMOTE B Clerk 100", "REG B 100", "REG B 110", "REG B 120", "REG B 130", "SALARY-PS A 35", "SALARY-PS B 150", "SALARY-PS C 150"]
    expected = ["1", "2", "", "promoted", "", "invalid_request", "invalid_request", "", "promoted", "", "", "", "promoted", "", "", "", "", "200", "2400", "invalid_request"]
    print(f"{expected=}")
    assert parseCommands(commands) == expected
    

# TestLevel1()
# TestLevel2()
# TestLevel3()









