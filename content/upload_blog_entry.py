#!/usr/bin/env python3

import argparse
import json
from http.client import HTTPSConnection, HTTPConnection

def main():
    CONFIG_FILE = "./config.json"
    args = parse_arguments()

    if args.single == None and not args.all:
        print("No filename specified! Use -s FILENAME for a single file or --all for all files in the folder")
        return

    if args.single != None and args.all:
        print("Both single and all mode flags were specified! Pick one, use either -s FILENAME for a single file or --all for all files in the folder")
        return

    config = json.loads(read_file(CONFIG_FILE))

    print(config)

    if args.all:
        pass
    else:
        filepath = "{0}/{1}.json".format(args.dir, args.single)
        data = [read_file(filepath)]

        upload(config, data)
    for entry in data:
        print(data)


def read_file(filepath, line_delimiter=None, do_after_file_read=None):
    with open(filepath, "r") as file_stream:
        data = file_stream.read()
        if line_delimiter != None:
            data = data.split(line_delimiter)

    if do_after_file_read and callable(do_after_file_read):
        return do_after_file_read(data)
    else:
        return data


def upload(config, data):
    protocol = config["protocol"]
    host_url = config["hostUrl"]
    api_key = config["apiKey"]
    secret = config["secret"]

    connection = HTTPSConnection(
            host_url) if protocol == "https" else HTTPConnection(host_url)
    
    request_url = "{0}://{1}".format(protocol, host_url)
    headers = {
        "x-api-key": api_key,
        "secret": secret
    }
    body = json.dumps(data)

    print("*** Uploading to {0}".format(request_url))

    connection.request("POST", request_url,
                                headers=headers, body=body)

    response = connection.getresponse()

    print("*** Response from {0}: {1} {2}".format(request_url, response.status, response.read()))

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Upload a blog entry or all entries to the hosted API. Either supply a filename with -s or use --all to upload the entire folder")
    parser.add_argument("-s", "--single", dest="single", action="store", default=None, help="Filename of the entry to upload")
    parser.add_argument("--all", dest="all", action="store_true", help="Upload all entries")
    parser.add_argument("-d", "--dir", dest="dir", action="store", default="./posts", help="Directory where the posts can be found (default is './posts')")


    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
