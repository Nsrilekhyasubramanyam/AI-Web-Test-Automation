import json


def generate_test_cases(requirement):

    requirement = requirement.lower()

    test_cases = []

    if "login" in requirement:

        test_cases.extend([
            {
                "test_case": "Valid Login",
                "type": "Positive",
                "expected_result": "User should successfully log in"
            },
            {
                "test_case": "Invalid Username",
                "type": "Negative",
                "expected_result": "Login should fail with an error message"
            },
            {
                "test_case": "Invalid Password",
                "type": "Negative",
                "expected_result": "Login should fail with an error message"
            },
            {
                "test_case": "Empty Credentials",
                "type": "Negative",
                "expected_result": "Validation error should be displayed"
            },
            {
                "test_case": "Locked User",
                "type": "Negative",
                "expected_result": "Locked user should not be allowed to log in"
            }
        ])

    if "cart" in requirement:

        test_cases.extend([
            {
                "test_case": "Add Product to Cart",
                "type": "Positive",
                "expected_result": "Product should be added to cart"
            },
            {
                "test_case": "Open Shopping Cart",
                "type": "Positive",
                "expected_result": "Cart page should be displayed"
            }
        ])

    if "checkout" in requirement:

        test_cases.extend([
            {
                "test_case": "Complete Checkout",
                "type": "Positive",
                "expected_result": "Order should be successfully completed"
            },
            {
                "test_case": "Checkout With Missing Details",
                "type": "Negative",
                "expected_result": "Validation error should be displayed"
            }
        ])

    return test_cases


if __name__ == "__main__":

    requirement = input("Enter application requirement: ")

    test_cases = generate_test_cases(requirement)

    print("\nGenerated Test Cases:\n")

    print(json.dumps(test_cases, indent=4))