import argparse, datetime, sys
from getpass import getpass
from stravacookies import StravaCookieFetcher

def argParse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest="server", choices=["a", "b", "c"], default="a", help="server, one of a, b, c (default: %(default)s)")
    parser.add_argument("-a", dest="activity", choices=["run", "ride", "winter", "water", "all"], default="all", help="activity, one of run, ride, winter, water, all (default: %(default)s)")
    parser.add_argument("-c", dest="color", choices=["blue", "bluered", "purple", "hot", "gray"], default="hot", help="color, one of blue, bluered, purple, hot, gray (default: %(default)s)")
    parser.add_argument("-r", dest="resolution", type=int, default=256, help="resolution, an integer (default: %(default)s)")
    parser.add_argument("-t", dest="useTMSFormat", default=False, action="store_true", help="use TMS format")
    parser.add_argument("-o", dest="useOSMFormat", default=False, action="store_true", help="use OSM format")
    return parser.parse_args()

def buildPrefix(args):
    servers = ["a", "b", "c"]
    activities = ["run", "ride", "winter", "water", "all"]
    colors = ["blue", "bluered", "purple", "hot", "gray"]

    urlPrefix = "tms:https://heatmap-external-" if args.useTMSFormat else "https://heatmap-external-"
    urlPrefix += f"{{switch:a,b,c}}.strava.com/tiles-auth/{args.activity}/{args.color}/{{zoom}}/{{x}}/{{y}}.png?px={args.resolution}&" if args.useOSMFormat else f"{args.server}.strava.com/tiles-auth/{args.activity}/{args.color}/{{z}}/{{x}}/{{y}}.png?px={args.resolution}&"

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
    parsedArgs = argParse(sys.argv[1:])
    urlPrefix = buildPrefix(parsedArgs)
    urlSuffix = buildSuffix()
    printResponse(urlPrefix, urlSuffix)

if __name__ == "__main__":
    main()
