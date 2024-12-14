import argparse
import os
import shutil

import requests
from jinja2 import Environment, FileSystemLoader


def create_from_template(day: int):
    padded_day = f"{day:02d}"
    target_folder = f"src/aoc/d{padded_day}"
    template_folder = "src/aoc/template"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

        env = Environment(loader=FileSystemLoader(template_folder))
        template = env.get_template("test.py.jinja")
        output = template.render(day=padded_day)
        with open(f"{target_folder}/test_{padded_day}.py", "w") as f:
            f.write(output)

        shutil.copy2(f"{template_folder}/part1.py", f"{target_folder}/part1.py")
        shutil.copy2(f"{template_folder}/part2.py", f"{target_folder}/part2.py")
        shutil.copy2(f"{template_folder}/sample1.txt", f"{target_folder}/sample1.txt")


def download_aoc_input(day: int):
    session_cookie = os.getenv("AOC_COOKIE")
    session = requests.Session()
    session.cookies.set("session", session_cookie)

    year = os.getenv("AOC_YEAR")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = session.get(url)

    padded_day = f"{day:02d}"
    filename = f"src/aoc/d{padded_day}/input.txt"

    with open(filename, "w") as f:
        f.write(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Advent of Code input")
    parser.add_argument("day", type=int, nargs="?", default=None)

    args = parser.parse_args()

    if args.day is None:
        import datetime

        args.day = datetime.datetime.now().day

    create_from_template(args.day)
    download_aoc_input(args.day)
