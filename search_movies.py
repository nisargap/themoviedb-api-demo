#!/usr/bin/python 
#coding=utf-8
'''
Author: Nisarga Patel
Python Version: 2.7.10
License: MIT
Created On: February 23, 2017
Description: This provides the user a simple way to search movies through terminal or command line
'''

# Imports go at the top, the requests library is needed to hit the endpoint
import requests

# Imports argparse to parse command line arguments
import argparse

# The unique API key needs to be read in, never commit a key to GitHub
api_key = ""
with open('api_key.txt', 'r') as api_key_file:

    api_key = api_key_file.readline().strip('\n')

def parse_args():

    # default args dictionary 
    args_dict = { "query" : False, "year" : False, "page" : 1 }

    # set up the parser
    parser = argparse.ArgumentParser()

    # define the arguments
    parser.add_argument("--query", help="search query for movie")
    parser.add_argument("--year", help="year of movie as integer")
    parser.add_argument("--page", help="page number of results")
    
    # grab the arguments
    args = parser.parse_args()
    
    if not args.query:
        return False
    else:
        args_dict["query"] = args.query
        # try setting the year
        if args.year:
            try:
                args_dict["year"] = int(args.year)
            except TypeError:
                print("Enter a proper numeric year")
        if args.page:
            try:
                args_dict["page"] = int(args.page)
            except TypeError:
                print("Enter a proper numeric page")
    return args_dict

def get_response(args):
    
    year_str = ""
    if args["year"]:
        year_str = "year=" + str(args["year"]) + "&"
    
    # send the response
    response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + args["query"] + "&page=" + str(args["page"])  + "&" + year_str + "include_adult=false")
    
    return response.json()

def format_print(response):
    
    print(str(len(response)) + " query results")

    print("-----------------------------------------")
    for element in response:
        print("Title: " + element["title"])
        print("Release Date: " + element["release_date"])
        print("Overview: " + element["overview"])
        print("------------------------------------------")

def main():

    args = parse_args()
    
    if not args == False:

	
	# send the request and get the response
        response = get_response(args)["results"]
        format_print(response)

    else:
        print("--query parameter is required please do -h for details")
main()


