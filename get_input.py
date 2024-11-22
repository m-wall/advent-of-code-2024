import argparse
import os
import requests
import shutil

def create_from_template(day: int):
    padded_day = f"{day:02d}"
    template_folder = "template"

    if not os.path.exists(padded_day):
        os.makedirs(padded_day)

        for file_name in os.listdir(template_folder):
            source_file = os.path.join(template_folder, file_name)
            destination_file = os.path.join(padded_day, file_name)
            shutil.copy2(source_file, destination_file)


def download_aoc_input(day: int):
    
    session_cookie = os.getenv("AOC_COOKIE")
    session = requests.Session()
    session.cookies.set('session', session_cookie)

    year =  os.getenv("AOC_YEAR")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = session.get(url)

    padded_day = f"{day:02d}"
    filename = f"{padded_day}/input.txt"

    with open(filename, 'w') as f:
        f.write(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download Advent of Code input')
    parser.add_argument('day', type=int, nargs='?', default=None)

    args = parser.parse_args()

    if args.day is None:
        import datetime
        args.day = datetime.datetime.now().day

    create_from_template(args.day)
    download_aoc_input(args.day)
   