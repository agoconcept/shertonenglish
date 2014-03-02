#!/usr/bin/env python

import argparse
import mechanize
import lxml.html


def process_table(table_elem):

    rows = table_elem.getchildren()

    for row in rows:
        line = row.text_content().split('\n')

        print "%s - %s" % (line[1].strip(), line[2].strip())


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
    tags = dom.get_element_by_id('mainLeft').getchildren()

    for tag in tags:
        if tag.tag == 'table':
            process_table(tag)


#######################
if __name__ == '__main__':
    main()
