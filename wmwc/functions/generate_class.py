from wmwc.providers.provider import Provider

def generate_class(options):
    provider_name = options["provider"]

    provider_name = Provider(
        options["monitor_long"],
        options["monitor_height"],
        options["topic"],
        options["save"]
    )

    return provider_name
