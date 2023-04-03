import argparse, datetime, sys
from getpass import getpass
from stravacookies import StravaCookieFetcher

def buildPrefix(argv):
    validServers = ["a", "b", "c"]
    validActivities = ["run", "ride", "winter", "water", "all"]
    validColors = ["blue", "bluered", "purple", "hot", "gray"]

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest="server", choices=validServers, default="a", help=f"server, one of {validServers} (default: %(default)s)")
    parser.add_argument("-a", dest="activity", choices=validActivities, default="all", help=f"activity, one of {validActivities} (default: %(default)s)")
    parser.add_argument("-c", dest="color", choices=validColors, default="hot", help=f"color, one of {validColors} (default: %(default)s)")
    parser.add_argument("-r", dest="resolution", type=int, default=256, help="resolution, an integer (default: %(default)s)")
    parser.add_argument("-t", dest="useTMSFormat", default=False, action="store_true", help="use TMS format")
    parser.add_argument("-o", dest="useOSMFormat", default=False, action="store_true", help="use OSM format")
    parsedArgs = parser.parse_args(argv)

    urlPrefix = "tms:https://heatmap-external-" if parsedArgs.useTMSFormat else "https://heatmap-external-"
    urlPrefix += f"{{switch:a,b,c}}.strava.com/tiles-auth/{parsedArgs.activity}/{parsedArgs.color}/{{zoom}}/{{x}}/{{y}}.png?px={parsedArgs.resolution}&" if parsedArgs.useOSMFormat else f"{parsedArgs.server}.strava.com/tiles-auth/{parsedArgs.activity}/{parsedArgs.color}/{{z}}/{{x}}/{{y}}.png?px={parsedArgs.resolution}&"

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

def main():
    urlPrefix = buildPrefix(sys.argv[1:])
    urlSuffix = buildSuffix()

    print("Your Strava Heatmap URL is:\n\n" + urlPrefix + urlSuffix)

    cookieExpiration = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%B %-d.")
    print(f"\nThis URL will expire on {cookieExpiration}")

if __name__ == "__main__":
   main()
