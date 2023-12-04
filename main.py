from astroquery.jplhorizons import Horizons


def query_body():
    # TODO: Separate query body into 2 functions,
    """
    Get input from user return true if input value is body on jplhorizons.

    Use basic input to request name of body string.
    Query jpl servers for existence of body name.
    Return true if the value is a known body name, false otherwise.
    """

    body = input("Body: ")

    try:
        print(Horizons(id=body).ephemerides())
        return True

    except ValueError:
        print("Unrecognized Body.")
        return False


def query_horizons():
    # TODO Separate this out also.
    """
    Takes body and time parameters.
    Queries Horizons to generate ephemeris from parameters.
    Creates file and inserts DS2-format ephemeris.
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

    file_name = input("File name: ")

    with open(f"{file_name}.ctr", "w") as file:
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

    # TODO: Put this only in the context of running from the command line.
    print("CTR file generated.")


def menu():
    """
    Takes option parameter.
    Calls query_body() or query_horizons().
    """

    option = input("Enter 'query' or 'generate': ").lower()

    if option == 'query':
        query_body()
    elif option == 'generate':
        query_horizons()
    else:
        print("Invalid option.")
        menu()


if __name__ == "__main__":
    menu()
