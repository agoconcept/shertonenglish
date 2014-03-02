#!/usr/bin/env python

import argparse
import mechanize
import lxml.html
import re


def main():

    # Handle argument
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Sherton URL to parse')
    args = parser.parse_args()

    # Open URL
    response = mechanize.urlopen(args.url).read()

    # Create DOM
    dom = lxml.html.document_fromstring(response)

    # Find tags to process
    tags = dom.get_element_by_id('mainLeft').getchildren()[1].getchildren()

    for tag in tags:
        if tag.tag == 'p':
            # Process only the <p> tags

            for line in tag.text_content().split('\n'):
                match = re.match("(.*) \\(.*\\) - (.*)", line)

                if match:
                    print "%s - %s" % (match.group(1).strip(), match.group(2).strip())


#######################
if __name__ == '__main__':
    main()
