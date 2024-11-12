import numpy as np

A1 = np.array([[34, 45], [17, 6]])

A = np.array([[1, 2], [-1, 1]])
B = np.array([[2, 0], [0, 2]])
C = np.array([[2, 0, -3], [0, 0, -1]])
D = np.array([[1, 2], [2, 3], [-1, 0]])
x = np.array([[1], [0]])
y = np.array([[0], [1]])
z = np.array([[1], [2], [-1]])

A2 = A+B
A3 = 3*x-4*y
A4 = A@x
A5 = B@(x-y)
A6 = D@x
A7 = D@y + z
A8 = A@B
A9 = B@C
A10 = C@D

test_suite = [
    {
        "test_name": "Problem 1",
        "variable_name": "A1",
        "description": "Initialize the matrix",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A1.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x2 2-dimensional array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x2 matrix."
    },
    {
        "test_name": "Problem 2a",
        "variable_name": "A2",
        "description": "Calculate A+B",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A2.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Make sure that your answer is a 2D array.",
        #"hint_wrong_size_matlab": "Your answer should be a 3x1 column vector."
    },
    {
        "test_name": "Problem 2b",
        "variable_name": "A3",
        "description": "Calculate 3x-4y",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A3.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Make sure that your answer is a 2D array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x1 column vector."
    },
    {
        "test_name": "Problem 2c",
        "variable_name": "A4",
        "description": "Calculate Ax",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A4.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Make sure that your answer is a 2D array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x1 column vector."
    },
    {
        "test_name": "Problem 2d",
        "variable_name": "A5",
        "description": "Calculate B(x-y)",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A5.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Make sure that your answer is a 2D array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x1 column vector."
    },
    {
        "test_name": "Problem 2e",
        "variable_name": "A6",
        "description": "Calculate Dx",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A6.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 3x1 2D array.",
        "hint_wrong_size_matlab": "Your answer should be a 3x1 column vector."
    },
    {
        "test_name": "Problem 2f",
        "variable_name": "A7",
        "description": "Calculate Dx + z",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A7.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 3x1 2D array.",
        "hint_wrong_size_matlab": "Your answer should be a 3x1 column vector."
    },
    {
        "test_name": "Problem 2g",
        "variable_name": "A8",
        "description": "Calculate AB.",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A8.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x2 2-dimensional array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x2 matrix."
    },
    {
        "test_name": "Problem 2h",
        "variable_name": "A9",
        "description": "Calculate BC.",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A9.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x3 2-dimensional array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x3 matrix."
    },
    {
        "test_name": "Problem 2i",
        "variable_name": "A10",
        "description": "Calculate CD.",
        "atol": 1e-8,
        "score": 1,
        "hint_not_defined": "Double check that you named your answer A10.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x2 2-dimensional array.",
        "hint_wrong_size_matlab": "Your answer should be a 2x2 matrix."
    }
]

supported_platforms = ["python"]#, "matlab"]
#matlab_credentials = "~/gspack_uw_amath_matlab_credentials"
requirements = ["numpy"]
