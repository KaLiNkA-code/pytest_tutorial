def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

"""
===================== test session starts ======================
platform win32 -- Python 3.8.6, pytest-7.2.1, pluggy-0.13.1      
rootdir: C:\Scripts\pytest_tutorial\pytest_project
plugins: anyio-3.6.2
collected 1 item

test_capitalize.py .                                      [100%]      

====================== 1 passed in 0.10s =======================
"""