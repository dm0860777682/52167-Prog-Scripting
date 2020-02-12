"""
Write    a    program    (lab04.01-­‐grade.py)    thatreads    in    a    students    percentage   
mark    and    prints    out    corresponding    the    grade    (the    program    should
check    that    the    percentage    is    valid:
•Under    40%    =>    Fail
•Between    40%    and    49%    =>    Pass
•Between    50%    and    59%  =>    Merit    2
•Between    60%    and    69%    =>    Merit    1
•Over    70%                     =>    Distinction
Ref https://data-flair.training/blogs/python-switch-case/
"""
def mark(percent):
    input = float(percent)
    if input < 40 :
        print("Fail")
    elif input > 40.0 and input <= 49.9:
        print("Pass")
    elif input > 50.0 and input <= 59.9:
        print("Merit 2")
    elif input > 60.0 and input <= 69.9:
        print("Merit 3")
    else:
        print("Distintion")
val = input("Enter the percentage: ")
mark(val)