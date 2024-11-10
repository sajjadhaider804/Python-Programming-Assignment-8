def manage_student_database():
    # Step 1: Initialize an empty list and a counter for student IDs
    student_list = []
    student_id = 1

    # Step 2: Collect user input in a loop
    while True:
        name = input("Enter student name (or type 'stop' to finish): ").strip()
        
        # Check if the user wants to stop
        if name.lower() == "stop":
            break
        
        # Step 3: Check for duplicates
        if any(student[1] == name for student in student_list):
            print(f"Student '{name}' is already in the database. Duplicate entries are not allowed.")
            continue
        
        # Add the student to the list
        student_list.append((student_id, name))
        student_id += 1
    
    # Step 4: Display the complete list of students
    print("\nComplete List of Students:")
    print(student_list)

    # Step 5: Display each student's ID and name individually
    print("\nStudent Details:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Step 6: Calculate and display statistics
    total_students = len(student_list)
    print(f"\nTotal number of students: {total_students}")
    
    # Calculate the total length of all names
    total_name_length = sum(len(student[1]) for student in student_list)
    print(f"Total length of all student names combined: {total_name_length}")
    
    # Find the longest and shortest names
    if total_students > 0:
        longest_name = max(student_list, key=lambda x: len(x[1]))[1]
        shortest_name = min(student_list, key=lambda x: len(x[1]))[1]
        print(f"Student with the longest name: {longest_name}")
        print(f"Student with the shortest name: {shortest_name}")

# Step 7: Call the function to run the program
manage_student_database()
