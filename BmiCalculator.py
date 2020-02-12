print("BMI CALCULATER")
def BMICal(weight,height):
    try:
        bim = 0
        height = float(height)/100
        bim = float(weight)/(height**2)
        print("BMI is {:.2f}.".format(bim))
    except Exception:
        print("Sorry!, something went wrong")

BMICal(65,180)
