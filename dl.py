from loader import Downloader, splash
def main():
    dl = Downloader(cookie=sys.argv[2])
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
