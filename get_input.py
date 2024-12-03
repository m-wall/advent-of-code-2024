import argparse
import os
import requests
import shutil

from jinja2 import Environment, FileSystemLoader

def create_from_template(day: int):
    padded_day = f"{day:02d}"
    template_folder = "template"

    if not os.path.exists(padded_day):
        os.makedirs(padded_day)

        env = Environment(loader=FileSystemLoader(template_folder))
        template = env.get_template("test.py.jinja")
        output = template.render(day=padded_day)
        with open(f"{padded_day}/test_day_{padded_day}.py", 'w') as f:
            f.write(output)

        shutil.copy2(f"{template_folder}/part1.py", f"{padded_day}/day_{padded_day}_part1.py")
        shutil.copy2(f"{template_folder}/part2.py", f"{padded_day}/day_{padded_day}_part2.py")


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
   