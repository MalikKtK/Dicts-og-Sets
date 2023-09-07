# Model an organisation of employees, management and board of directors in 3 sets.
board_of_directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# Who in the board of directors is not an employee?
not_employee_in_board = board_of_directors - employees
print("Directors who are not an employee:", not_employee_in_board)

# Who in the board of directors is also an employee?
board_and_employee = board_of_directors & employees
print("Directors who are also an employee:", board_and_employee)

# How many of the management is also member of the board?
management_in_board = len(management & board_of_directors)
print("Number of management who are also in the board:", management_in_board)

# All members of the managent also an employee
all_management_are_employees = management.issubset(employees)
print("Are all members of management also employees?", all_management_are_employees)

# All members of the management also in the board?
all_management_are_in_board = management.issubset(board_of_directors)
print("Are all members of management also in the board?", all_management_are_in_board)

# Who is an employee, member of the management, and a member of the board?
employee_management_board = employees & management & board_of_directors
print("Who is an employee, member of the management, and a member of the board:", employee_management_board)

# Who of the employee is neither a memeber or the board or management?
not_board_or_management = employees - (management | board_of_directors)
print("Who of the employee is neither a memeber or the board or managemen:", not_board_or_management)
