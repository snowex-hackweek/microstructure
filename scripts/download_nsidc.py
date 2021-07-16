"""
This script downloads the NSIDC data for the full SMP profiles to be used for the microstructure project

"""

import requests
from os.path import join, basename, isdir, isfile
from os import mkdir
import argparse
import time
import sys


def get_nsidc_url_folders(response):
    """
    Retrieve the NSIDC folders. based on the periods.
    """
    folders = []

    # Parse data from the webpage on hrefs (e.g. all the sub folders)
    for url in response.text.split('href='):
        # Clean up any potential folder names
        potential_folder = url.split('/')[0].strip('"')

        # Only show interest in folder names that have 2 periods. e.g. 2020.01.02
        if potential_folder.count('.') == 2:
            folders.append(potential_folder)
    return folders


def get_nsidc_url_files(response, search_str=None, file_ext=[]):
    """
    Retrieve the NSIDC files based on the periods.
    """
    files = []

    # Parse data from the webpage on hrefs (e.g. all the sub folders)
    for url in response.text.split('href='):
        # Clean up any potential folder names
        potential_file = url.split('>')[0].strip('"')

        # Only show interest in folder names that have 1 periods. e.g. file.csv
        if potential_file.count('.') == 1:
            files.append(potential_file)

    # Apply any filter by sub strings
    if search_str is not None:
        files = [f for f in files if search_str in f]

    # Apply any filter file extensions
    if file_ext:
        files = [f for f in files if f.split('.')[-1] in file_ext]
    # Apply filters
    return files


def main():
    parser = argparse.ArgumentParser(description='Script to download NSIDC data')
    parser.add_argument('--url', metavar='URL',
                        help='URL to the base data navigator on nsidc')
    parser.add_argument('--file_pattern', dest='file_pattern', help='Provide a substring to search filenames for, e.g. 1N13')
    parser.add_argument('--file_ext', dest='file_extension', help='Filter downloads by file exentions')
    parser.add_argument('--output_folder', dest='output_folder', help='Location to save the data locally', default='./data')
    parser.add_argument('--just_give_it_to_me', dest='just_give_it_to_me', help='the URLS listed in the a text file',
                        )

    args = parser.parse_args()

    print("\nHACK WEEK NSIDC DOWNLOADER SCRIPT")
    print("==================================\n")
    # Allow users to pass a list of urls
    if args.just_give_it_to_me is not None:
        with open(args.just_give_it_to_me, 'r') as fp:
            url_list = [url.strip() for url in fp.readlines()]
    else:
        # Avoid double / when joining files and such
        if args.url.endswith('/'):
            args.url = args.url[0:-1]

        url_list = []

        print(f'Querying {args.url} for downloadable data')
        r = requests.get(args.url)

        if r.status_code == 404:
            print('URL does not exist!')
            sys.exit()

        elif r.status_code == 403:
            print('Permission denied to URL!!')
            sys.exit()

        # See what folders are available
        folders = get_nsidc_url_folders(r)

        for f in folders:
            url = f'{args.url}/{f}'
            r = requests.get(url)
            files = get_nsidc_url_files(r, search_str=args.file_pattern, file_ext=args.file_extension)

            # Build all the URLS were going to download
            url_list += [f'{args.url}/{f}/{file}' for file in files]

    url_list = list(set(url_list))
    N_url = len(url_list)
    print(f'Found {N_url} files to download...')

    # Download folder
    if N_url > 0:
        print(f'Saving Data to {args.output_folder}')

        # Make the data directory if it is missing
        if not isdir(args.output_folder):
            mkdir(args.output_folder)

    # Main download loop
    for i, url in enumerate(url_list):
        print(f'Downloading {url} ({i+1}/{N_url})')

        # Form a filename to save data locally
        out = join(args.output_folder, basename(url))

        # CHeck whether we should download it
        if isfile(out):
            print('File already exists locally...skipping download.')
        else:

            # Download the contents of the file
            r = requests.get(url)
            if r.status_code == 404:
                print(f'{url} does not exist')

            elif r.status_code == 403:
                print(f'{url} is forbidden')
            else:
                with open(out, 'wb') as fp:
                    fp.write(r.content)


if __name__ == '__main__':

    # Keep track of time
    start = time.time()
    main()
    end = time.time()
    print('Download Complete! Elasped time {:0.0f} minutes.\n'.format((end - start)// 60))
