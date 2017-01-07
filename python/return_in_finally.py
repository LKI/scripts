def return_in_finally():
    try:
        return True
    finally:
        return False

print return_in_finally()
