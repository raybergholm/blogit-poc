#!/usr/bin/env python3

import os
import argparse
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    CONFIG_FILE = "./config.json"
    args = parse_arguments()

    if args.single == None and not args.all:
        print("No filename specified! Use -s FILENAME for a single file or --all for all files in the folder")
        return

    if args.single != None and args.all:
        print("Both single and all mode flags were specified! Pick one, use either -s FILENAME for a single file or --all for all files in the folder")
        return

    if args.all:
        pass
    else:
        posts = [args.single]

    for entry in posts:
        text_filepath = "{0}/texts/{1}.md".format(ROOT_DIR, entry)
        metadata_filepath = "{0}/metadata/{1}.json".format(ROOT_DIR, entry)

        text = read_file(text_filepath)
        metadata = json.loads(read_file(metadata_filepath))

        blog_post = {
            **metadata,
            "text": text
        }

        blog_filepath = "{0}/posts/{1}.json".format(ROOT_DIR, entry)

        print("*** Saving to {0}".format(blog_filepath))
        save_file(blog_filepath, json.dumps(blog_post))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Build a blog entry or all entries by merging corresponding files in the ./texts/ and ./metadata/ folders. Use either -s or --all")
    parser.add_argument("-s", "--single", dest="single", action="store",
                        default=None, help="Filename of the entry to build")
    parser.add_argument("--all", dest="all",
                        action="store_true", help="Build all entries")

    args = parser.parse_args()
    return args


def read_file(filepath, line_delimiter=None, do_after_file_read=None):
    with open(filepath, "r") as file_stream:
        data = file_stream.read()
        if line_delimiter != None:
            data = data.split(line_delimiter)

    if do_after_file_read and callable(do_after_file_read):
        return do_after_file_read(data)
    else:
        return data


def save_file(filepath, data, line_delimiter=None, mode="w+"):
    with open(filepath, mode) as file_stream:
        file_stream.write(line_delimiter.join(
            data) if not line_delimiter == None else data)


if __name__ == "__main__":
    main()
