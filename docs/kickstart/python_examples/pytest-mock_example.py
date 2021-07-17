# code NOT being tested
from my_module import myFunc, myClass

# code being tested
from .assignment import calcPreset, generate_hello

# Tests function
def test_calcPreset(mocker):
    # Creates the mock version
    mocker.patch("my_module.myFunc", return_value=5)
    expected = 22
    actual = calcPreset(10)     # Uses mock version of myFunc
    assert expected == actual

    # Check that mock function was called once with 10
    assert myFunc.assert_called_once_with(10)

# Tests class
def test_myClass(mocker):
    mocker.object("my_module.myClass", "say_hello", return_value="hello")
    expected = "hello Bob"
    actual = generate_hello("Bob")  # Uses mock object
    assert expected == actual
    assert myClass.say_hello.assert_called_once()

# Tests exception handling
def test_handleException(mocker):
    mocker.patch("my_module.calcPreset",
                 side_effect=ArithmeticError("Must be a positive int"))

    try:
        calcPreset(-1)
        assert False, "Failed to raise error"
    except Exception as err:
        assert isinstance(err, ArithmeticError)
        assert str(err) == "Must be a positive int"