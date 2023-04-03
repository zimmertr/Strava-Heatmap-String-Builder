import argparse, datetime, sys
from getpass import getpass
from stravacookies import StravaCookieFetcher

def parseArgs(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", 
        default="a", 
        dest="server", 
        choices=["a", "b", "c"], 
        help="server, one of a, b, c (default: %(default)s)"
    )
    parser.add_argument("-a", 
        default="all", 
        dest="activity", 
        choices=["run", "ride", "winter", "water", "all"], 
        help="activity, one of run, ride, winter, water, all (default: %(default)s)"
    )
    parser.add_argument("-c", 
        default="hot", 
        dest="color", 
        choices=["blue", "bluered", "purple", "hot", "gray"], 
        help="color, one of blue, bluered, purple, hot, gray (default: %(default)s)"
    )
    parser.add_argument("-r", 
        default=256, 
        dest="resolution", 
        type=int,  
        help="resolution, an integer (default: %(default)s)"
    )
    parser.add_argument("-t", 
        default=False, 
        dest="useTMSFormat", 
        action="store_true", 
        help="use TMS format"
    )
    parser.add_argument("-o", 
        default=False, 
        dest="useOSMFormat", 
        action="store_true", 
        help="use OSM format"
    )

    return parser.parse_args()

def buildPrefix(parsedArgs):
    urlPrefix = \
        "tms:https://heatmap-external-" \
        if parsedArgs.useTMSFormat \
        else "https://heatmap-external-"

    urlPrefix += \
        f"{{switch:a,b,c}}.strava.com/tiles-auth/{parsedArgs.activity}/{parsedArgs.color}/{{zoom}}/{{x}}/{{y}}.png?px={parsedArgs.resolution}&" \
        if parsedArgs.useOSMFormat \
        else f"{parsedArgs.server}.strava.com/tiles-auth/{parsedArgs.activity}/{parsedArgs.color}/{{z}}/{{x}}/{{y}}.png?px={parsedArgs.resolution}&"

    return urlPrefix

def buildSuffix():
    email = input('Enter your Strava Email Address: ')
    password = getpass('Enter your Strava Password: ')
    print("")

    try:
        stravaCookieFetcher = StravaCookieFetcher()
        stravaCookieFetcher.fetchCookies(email, password)
        cookieString = stravaCookieFetcher.getCookieString()
    except:
        print("ERROR! Retrieving Strava cookies failed! Are your credentials correct?")
        sys.exit(4)

    return cookieString

def printResponse(urlPrefix, urlSuffix):
    print("Your Strava Heatmap URL is:\n\n" + urlPrefix + urlSuffix)

    cookieExpiration = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%B %-d.")
    print(f"\nThis URL will expire on {cookieExpiration}")

def main():
    parsedArgs = parseArgs(sys.argv[1:])
    urlPrefix = buildPrefix(parsedArgs)
    urlSuffix = buildSuffix()

    printResponse(urlPrefix, urlSuffix)

if __name__ == "__main__":
    main()
