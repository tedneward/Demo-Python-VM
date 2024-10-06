# {{## BEGIN task ##}}
import requests
from codetiming import Timer

def task(url):
    timer = Timer(text=f"Task {url} elapsed time: {{:.1f}}")
    with requests.Session() as session:
            print(f"Getting URL: {url}")
            timer.start()
            response = session.get(url)
            timer.stop()
# {{## END task ##}}

# {{## BEGIN main ##}}
def main(argc : int, argv : list[str]):
    urls = []
    if argc == 0:
        urls = [
            "http://google.com",
            "http://yahoo.com",
            "http://linkedin.com",
            "http://apple.com",
            "http://microsoft.com",
            "http://facebook.com",
            "http://twitter.com",
        ]
    else:
        urls = argv

    # Go get 'em!
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        for u in urls:
            task(u)
# {{## END main ##}}

if __name__ == "__main__":
    import sys
    main(len(sys.argv), sys.argv)
