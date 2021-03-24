"""
Module: comp110_lab09

Starter code for COMP110 Lab 09.
"""

import matplotlib.pyplot as pp


def get_grade_frequencies(filename):
    """
    Creates a dictionary mapping letter grade to the number of students with
    that grade for the midterm exam #1.
    """
    
    grade_dict={"A":0,"B":0,"C":0,"D":0,"F":0} 
    grades=open(filename, 'r')
    grades.readline()

    for line in grades:
        values=line.split(",")
        if 90<=int(values[5])<= 100:
            grade_dict["A"] += 1
        elif 80<=int(values[5])< 90:
            grade_dict["B"] += 1
        elif 70<=int(values[5])< 80:
            grade_dict["C"] += 1
        elif 60<=int(values[5])< 70:
            grade_dict["D"] += 1
        elif int(values[5])< 60:
            grade_dict["F"] += 1

    return grade_dict



def test_get_grade_frequencies():
    actual = get_grade_frequencies("students.txt")

    # To Do: update the next line so it is a dictionary with the correct,
    # expected values.
    expected = {"A":3,"B":6,"C":8,"D":2,"F":1}

    if actual == expected:
        print("Test PASSED")
    else:
        print("Test FAILED!")
        print("Expected:", expected)
        print("Actual:", actual)


def main():
    """
    Creates a bar chart showing grade distribution on midterm exam #1.
    """

    # To Do: Step 1: Call your function to get the frequency data from
    # students.txt

    # To Do: Step 2: Call pyplot's bar function to create the bar chart

    # To Do: Step 3: Update the labels for the x and y axis as well as the
    # title of the chart.


    import matplotlib.pyplot as pp
    data = get_grade_frequencies("students.txt")
    
    pp.bar(data.keys(),data.values())
    pp.xlabel("Letter Grade")
    pp.ylabel("Number of Students")
    pp.title("Midterm Grade Distribution")
    pp.show()


if __name__ == "__main__":
    main()
