from wmwc.providers.provider import Provider


def generate_class(options, url, filename):
    return Provider(
        options["monitor_long"],
        options["monitor_height"],
        options["topic"],
        options["save"],
        url,
        filename,
    )
