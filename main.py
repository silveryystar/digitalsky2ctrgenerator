from astroquery.jplhorizons import Horizons


def get_parameters():
    """
    Take and return user inputs on body information.

    Take body, start, stop, and interval inputs.
    Return all inputs.
    """
    body = input("Body: ")
    start = input("Start time: ")
    stop = input("Stop time: ")
    interval = input("Interval: ")

    return body, start, stop, interval


def get_data(body, start, stop, interval):
    """
    Generate and return ephemeris data from parameters.

    Take body, start, stop, and interval parameters.
    Query JPL Horizons and generate ephemeris.
    Get, format, and return vector data from ephemeris.
    """
    ephemeris = Horizons(id=body,
                         location="500@10",  # Sun
                         epochs={"start": start,
                                 "stop": stop,
                                 "step": interval})

    vec = ephemeris.vectors()
    xyz_data = vec["x", "y", "z"].pformat_all(show_unit=False,
                                              show_name=False)

    return xyz_data


def format_interval(interval):
    """
    Correct and return DS2-format parameter.

    Take interval parameter.
    Format and return corrected interval.
    """
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

    return corrected_interval


def get_file(body, start, corrected_interval, xyz_data):
    """
    Take parameters and generate DS2-format CTR file.

    Take body, start, corrected_interval, and xyz_data parameters.
    Get file_name input and create file with file_name.
    Insert DS2-format information and vector data into file.
    Print confirmation that file has been generated.
    """
    file_name = input("File name: ")

    with open(f"{file_name}.ctr", "w") as file:
        file.write(f"[HEADER]\n\n"
                   f"Title:  {body}\n"
                   f"Name:   {body}\n"
                   f"Class:  Path0\n"
                   f"Type0:  Position\n"
                   f"Unit:   AU\n"
                   f"Source: JPL Horizons\n"
                   f"Author: silveryystar\n\n"
                   f"[DATA]\n\n"
                   f"Date={start}\n"
                   f"Interval={corrected_interval}\n\n")

        for line in xyz_data:
            file.write(f"{str(line)}\n")

    print("CTR file generated.")  # Command-line only?


def query_horizons():
    """
    Use functions to run code.

    Use get_parameters, get_data, format_interval, and get_file functions to generate CTR file.
    """
    body, start, stop, interval = get_parameters()
    xyz_data = get_data(body, start, stop, interval)
    corrected_interval = format_interval(interval)
    get_file(body, start, corrected_interval, xyz_data)


if __name__ == "__main__":
    query_horizons()
