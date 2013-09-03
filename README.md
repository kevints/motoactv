NOTE: I DO NOT WORK FOR MOTOROLA OR GOOGLE AND THE BITS THAT TALK TO THE MOTOACTV
PORTAL SHOULD BE CONSIDERED LIKELY TO BREAK ON A WHIM. USE THIS LIBRARY AT YOUR OWN RISK
AND ALWAYS WITHIN THE BOUNDS OF THE MOTOACTV TERMS OF SERVICE.

`motoactv` is a pure-Python library for managing [Motoactv](http://motoactv.com)-generated
workout data in an automation-friendly way. It can currently download TCX files suitable for
importing into another service like Runkeeper from the Motoactv portal.

Motivation
----------

The [Motoactv](http://motoactv.com) is a small Android device that does GPS tracking of workouts
like runs and bike rides.  Development appears to have been abandoned by Motorola around the time
of the Google acquisition but it's still a great little device that does what it does pretty well.
One major shortcoming of the Motoactv is that it doesn't provide a way to automate retrieval of
the data you generate by working out; instead you have to go to a web portal, select yourworkout,
select an export format and manually upload it to another service. This doesn't seem too bad until
you find yourself doing it 3-4 times per week and experiencing a few service outages. `motoactv`
lets you automate this routine so that you can focus on your real routine.

Getting Started
---------------
You will need Python 3. As I haven't published a PyPI distribution yet the best way to install is
probably to run

    pip3 install -e "git+https://github.com/kevints/motoactv#egg=motoactv-0.1"

with `sudo` or in a virtualenv.

Once your have it installed you can get started. To make use of the API without prompting add a
`~/.netrc` entry like so (create it if it doesn't already exist):

    machine motoactv.com
      login yourmotoactvlogin@example.com
      password yourexamplepassword

Security Note: you're saving your motoactv.com password in plain text on the disk here. This is
necessary as unfortunately there is not a separate system of API keys for motoactv.com.

Now that you've got that in place you can download your workouts from the previous week in TCX
format:

    motoactv pull

The data will be available in TCX format under `workoutdata`.

    find workoutdata -iname '*.tcx'

Direct API Usage
----------------
You can query the portal directly via the `Motoactv` class.

    >>> from datetime import datetime, timedelta
    >>> from motoactv import Motoactv
    >>> motoactv = Motoactv(username="yourmotoactvlogin@example.com", password="yourexamplepass")
    >>> motoactv.login()
    >>> workouts = motoactv.past_workouts(datetime.now() - timedelta(weeks=1), datetime.now())
    >>> for w in workouts:
    ...   print(w.url)
    ...
    >>> for w in workouts:
    ...   if not w.tcx_exists(workoutdata_root='.'):
    ...     motoactv.export_tcx(w.activity_id, workoutdata_root='.')


TODOs
-----
* Support for publishing the saved data directly to other services, specifically
[Runkeeper](http://runkeeper.com) and [Fitocracy](http://fitocracy.com).
* Local persistence of workout metadata.
* Possibly local persistence of cookiejar to avoid repeated login requests.
* A better understanding of the available fields.
* Support for all available workout types, starting with cycling and walking.
* Better modularization.
* Better error handling.
* Better test coverage and better testing libraries.
