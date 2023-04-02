# Strava Heatmap String Builder

## Summary

Strava's Heatmap provides very useful data for discovering unofficial trails & common backcountry routes. This data can be imported as a "Custom Layer" in [Caltopo](https://caltopo.com/). However, doing so requires building a URL string containing configuration & authentication data. This tool assists in the creation of this string.

| Before | After |
| ------ | ----- |
| ![Before](https://raw.githubusercontent.com/zimmertr/StravaHeatmapStringBuilder/main/screenshots/before.png?raw=true "Before") | ![After](https://raw.githubusercontent.com/zimmertr/StravaHeatmapStringBuilder/main/screenshots/after.png?raw=true "After") |


## How to Use

1. [Create](https://www.strava.com/register/free) a Strava account. Strava requires an account to access the Heatmap data.

2. Build a URL string using Python: `python main.py`. You will be prompted for your Strava credentials. Additional optional arguments are documented in the table below:
   | Argument | Description                                            | Allowed Values                       | Default |
   | -------- | ------------------------------------------------------ | ------------------------------------ | ------- |
   | -s       | The Heatmap Server to Use                              | `[a, b, c]`                          | `a`     |
   | -a       | The activity type to show on the Strava Heatmap data   | `[run, ride, winter, water, all]`    | `all`   |
   | -c       | The color to use for the Strava Heatmap data           | `[blue, bluered, purple, hot, gray]` | `hot`   |
   | -r       | The tile resolution to use for the Strava Heatmap data | *Any integer value*                  | `512`   |

3. [Create](https://caltopo.com/account/signup) a Caltopo account and sign in.

4. Add a [Custom Map Layer](https://blog.caltopo.com/2014/04/25/custom-map-layers/) in Caltopo using the following properties:

   | Property     | Value                       |
   | ------------ | --------------------------- |
   | Type         | `Tile`                      |
   | Name         | `Strava Heatmap`            |
   | URL Template | *URL Produced Above*        |
   | Max Zoom     | `12`                        |
   | Overlay?     | `Yes - Transparent Overlay` |

5. Click "Save To Account" and refresh the webpage.

6. Check "Strava Heatmap" in "Your Layers" on the Map Layers sidepanel to activate the Heatmap overlay.

## Common Problems

1. Strava expires its authentication cookies after approximately one week. If your Heatmap layer stops appearing when you check the box, you will need to regenerate your authentication cookies and build a new URL. To update the URL in Caltopo, simply navigate to `Add -> Custom Source` again and click `Load From`. Select your previous Strava Heatmap layer, update the `URL Template` data with the new URL, give it a new `Name` to differentiate it from the old one, click `Save To Account`. You will now have two available layers, only one of which will work. To delete the old one, click `Your Data` on the top right of Caltopo, navigate to `Your Layers`, and delete the old one by clicking the red `X`. Then refresh the webpage to reload the available layers. 
2. Strava will disable your account if you attempt to authenticate too many times in a period of time. Be careful not to run this script repeatedly!
