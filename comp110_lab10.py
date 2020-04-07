"""
Module: comp110_lab08

Starter code for COMP110 Lab 08.
"""

import matplotlib.pyplot as pp


def get_grade_frequencies(filename):
    """
    Creates a dictionary mapping letter grade to the number of students with
    that grade for the midterm exam #1.
    """

    return None  # placeholder. Remove this line when you are done.


def test_get_grade_frequencies():
    actual = get_grade_frequencies("students.txt")
    expected = {}

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

    # To Do: Call your function to get the frequency data from students.txt

    # To Do: Call pyplot's bar function to create the bar chart

    # To Do: Update the labels for the x and y axis as well as the title of the
    # chart.
    pp.xlabel("FIXME")
    pp.ylabel("FIXME")
    pp.title("FIXME")
    pp.show()


if __name__ == "__main__":
    main()
