import datetime, getopt, sys
from getpass import getpass
from stravacookies import StravaCookieFetcher

def main(argv):
    validServers = ["a", "b", "c"]
    validActivities = ["run", "ride", "winter", "water", "all"]
    validColors = ["blue", "bluered", "purple", "hot", "gray"]
    validArguments = ["-s $SERVER", "-a $ACTIVITY", "-c $COLOR", "-r $RESOLUTION", "-p $PREFIX"]

    server = "a"
    activity = "all"
    color = "hot"
    resolution = 512
    prefix = ""

    try:
        opts, args = getopt.getopt(argv, "s:a:c:r:p:")
    except getopt.GetoptError:
        print(f"ERROR! Invalid arguments! Accepted values are: {validArguments}")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-s":
            if arg.lower() in validServers:
                server = arg.lower()
            else:
                print(f"ERROR! Invalid server! Accepted values are: {validServers}")
                sys.exit(3)
        elif opt == "-a":
            if arg.lower() in validActivities:
                activity = arg.lower()
            else:
                print(f"ERROR! Invalid activity! Accepted values are: {validActivities}")
                sys.exit(3)
        elif opt == "-c":
            if arg.lower() in validColors:
                color = arg.lower()
            else:
                print(f"ERROR! Invalid color! Accepted values: {validColors}")
                sys.exit(3)
        elif opt == "-r":
            try:
                resolution = int(arg)
            except ValueError:
                print("ERROR! Invalid resolution! Accepted values are integers!")
                sys.exit(3)
        elif opt == "-p":
            prefix = arg.lower()


    email = input('Enter your Strava Email Address: ')
    password = getpass('Enter your Strava Password: ')
    print("")

    urlPrefix=f"{prefix}https://heatmap-external-{server}.strava.com/tiles-auth/{activity}/{color}/{{z}}/{{x}}/{{y}}.png?px={resolution}&"

    try:
        stravaCookieFetcher = StravaCookieFetcher()
        stravaCookieFetcher.fetchCookies(email, password)
        cookieString = stravaCookieFetcher.getCookieString()
    except:
        print("ERROR! Retrieving Strava cookies failed! Are your credentials correct?")
        sys.exit(4)

    print("Your Strava Heatmap URL is:\n\n" + urlPrefix + cookieString)

    cookieExpiration = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%B %-d.")
    print(f"\nThis URL will expire on {cookieExpiration}")

if __name__ == "__main__":
   main(sys.argv[1:])
