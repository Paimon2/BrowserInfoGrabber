# BrowserInfoGrabber
Get a visitor's request headers (incl. user agent) and IP address when serving an image. Also returns all data from request.environ. The image can be modified and is (very obviously) ./image.jpeg.

A custom 404/not found page can also be specified in ./templates/404.html.

Also has the option to not serve the image (disabling previews) if a hard-coded user agent is specified. Out of the box, this *should* disable the Discord crawler bot.

## Usage
``sudo python3 main.py`` (no need to run as root if port > 1024) on UNIX-based/like systems e.g. Linux and macOS. No configuration necessary (although is possible, see main.py).

On Windows, run the script with Python. I have no idea if you need admin rights.

You can then try it out on http://localhost/image.jpeg*

* Change port if running on a non-standard (80 or 443) port