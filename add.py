import requests
import argparse


def post_request(number1, number2):
    url = f"https://lla03tzbo3.execute-api.us-west-1.amazonaws.com/default/HelloWorldFunction?number1={number1}&number2={number2}"
    response = requests.post(url)
    print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send numbers to the API.")
    parser.add_argument("number1", type=int, help="The first number")
    parser.add_argument("number2", type=int, help="The second number")

    args = parser.parse_args()

    post_request(args.number1, args.number2)
