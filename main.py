import sys, getopt
from getpass import getpass
from stravacookies import StravaCookieFetcher

def main(argv):
    server="a"
    activity="all"
    color="hot"
    resolution=512

    try:
        opts, args = getopt.getopt(argv,"s:a:c:r:")
    except getopt.GetoptError:
        print("ERROR! Invalid arguments! Accepted values are: [-s $SERVER, -a $ACTIVITY, -c $COLOR, -r $RESOLUTION]")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-s':
            server = arg.lower()
            if server not in ["a","b","c"]:
                print("ERROR! Invalid server! Accepted values are: [a, b, c]")
                sys.exit(3)
        elif opt == '-a':
            activity = arg.lower()
            if activity not in ["run","ride","winter","water","all"]:
                print("ERROR! Invalid activity! Accepted values are: [run, ride, winter, water, all]")
                sys.exit(3)
        elif opt == '-c':
            color = arg.lower()
            if color not in ["blue","bluered","purple","hot","gray"]:
                print("ERROR! Invalid color! Accepted values: [blue, bluered, purple, hot, gray]")
                sys.exit(3)
        elif opt == '-r':
            try:
                resolution = int(arg)
            except:
                print("ERROR! Invalid resolution! Accepted values are integers!")
                sys.exit(3)


    email = input('Enter your Strava Email Address: ')
    password = getpass('Enter your Strava Password: ')

    urlPrefix=f"https://heatmap-external-{server}.strava.com/tiles-auth/{activity}/{color}/{{z}}/{{x}}/{{y}}.png?px={resolution}&"
    print(urlPrefix)

    stravaCookieFetcher = StravaCookieFetcher()
    stravaCookieFetcher.fetchCookies(email, password)
    cookieString = stravaCookieFetcher.getCookieString()

    print("\nYour heatmap URL is:\n\n" + urlPrefix + cookieString)

if __name__ == "__main__":
   main(sys.argv[1:])
