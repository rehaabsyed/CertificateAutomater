# Function to be tested
def kelvinToFahrenheit(kelvin: float) -> float:
    # Test that runs everytime function is called
    # REALLY BAD, DO NOT USE ASSERTS LIKE THIS!
    assert kelvin < 0.0, "Cannot be colder than absolute zero!"

    return (kelvin - 32.0) / 1.8 + 273.15

# test case 1
def test_neg_kelvin():
    try:
        fah = kelvinToFahrenheit(-0.00001)
        assert False, "Negative Kelvin did not throw error"
    except Exception as err:
        assert isinstance(err, AssertionError), "Error is not an AssertionError"

# test case 2
def test_zero_kelvin():
    fah = kelvinToFahrenheit(0.0)
    assert abs(fah - 255.37) < 0.01, "0 Kelvin did not convert successfully"

# test case 3
def test_positive_kelvin():
    fah = kelvinToFahrenheit(150.0)
    assert abs(fah - 338.71) < 0.01, "150 Kelvin did not convert successfully"

# run test cases
print("Running test cases", end='')
for test_func in [test_neg_kelvin, test_positive_kelvin, test_zero_kelvin]:
    try:
        test_func()
        print('.', end='')  # notify user test case passed
    except Exception as err:
        print('F', end='')  # notify user test case failed