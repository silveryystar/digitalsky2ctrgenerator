from astroquery.jplhorizons import Horizons

# TODO: Docstring on function.
# TODO: Create an option for getting closed ellipse orbit.
# Create an function for queying a body name and retruning True if jplhorizons
# recognizes it.
# Google style docstrings: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


def query_horizons():
    # TODO: Add filename as keyword with reasonable default.
    """ Create a file.
    Parameters:
    Returns:
    """
    body = input("Body: ")
    start = input("Start time: ")
    stop = input("Stop time: ")
    interval = input("Interval: ")

    ephemeris = Horizons(id=body,
                         location="500@10",
                         epochs={"start": start,
                                 "stop": stop,
                                 "step": interval})

    float_interval = interval[-1]
    sliced_interval = interval[:-1]
    corrected_interval = 0

    if float_interval == "s":
        corrected_interval = float(sliced_interval)/60/60/24
    elif float_interval == "m":
        corrected_interval = float(sliced_interval)/60/24
    elif float_interval == "h":
        corrected_interval = float(sliced_interval)/24
    elif float_interval == "d":
        corrected_interval = float(sliced_interval)

    vec = ephemeris.vectors()
    xyz_data = vec["x", "y", "z"].pformat_all(show_unit=False, show_name=False)

    with open(f"{body.replace(' ', '')}.ctr", "w") as file:
        file.write(f"[HEADER]\n"
                   f"\n"
                   f"Title:  {body}\n"
                   f"Name:   {body}\n"
                   f"Class:  Path0\n"
                   f"Type0:  Position\n"
                   f"Unit:   AU\n"
                   f"Source: JPL Horizons\n"
                   f"Author: silveryystar\n"
                   f"\n"
                   f"[DATA]\n"
                   f"\n"
                   f"Date={start}\n"
                   f"Interval={corrected_interval}"
                   f"\n"
                   f"\n")

        for line in xyz_data:
            file.write(f"{str(line)}"
                       f"\n")

    print("CTR file generated.")


if __name__ == "__main__":
    query_horizons()
