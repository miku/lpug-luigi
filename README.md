README
======

Material on [luigi](https://github.com/spotify/luigi) presentation from
[LPUG](http://www.python-academy.com/user-group/index.html) meeting on
10/11/2015.

Examples
--------

Create some sample input data first:

    $ make plays.ldj

    $ head plays.ldj
    {"album": "0", "track": "10", "date": "2015-10-26", "artist": "Aluminica"}
    {"album": "1", "track": "8", "date": "2015-10-23", "artist": "Aluminica"}
    {"album": "2", "track": "6", "date": "2015-10-03", "artist": "The Carpenters"}
    {"album": "3", "track": "10", "date": "2015-10-17", "artist": "Aluminica"}
    {"album": "2", "track": "8", "date": "2015-10-29", "artist": "Aluminica"}
    {"album": "0", "track": "8", "date": "2015-10-23", "artist": "The Carpenters"}
    {"album": "2", "track": "6", "date": "2015-10-23", "artist": "Aluminica"}
    {"album": "1", "track": "0", "date": "2015-10-21", "artist": "The Carpenters"}
    {"album": "1", "track": "3", "date": "2015-10-19", "artist": "Rolling Waters"}
    {"album": "1", "track": "3", "date": "2015-10-17", "artist": "Aluminica"}

The date values range from `2015-10-01` to `2015-10-30`.

Create a virtualenv and install deps:

    $ mkvirtualenv lpug-luigi
    (lpug-luigi) $ pip install luigi

There are four tasks in `main.py`. Run a single task with *local scheduler* only:

    $ python main.py DailyPlays --date 2015-10-08 --local-scheduler

    [2015-11-11 ...] Informed scheduler that task DailyPlays(date=2015-10-08) has status PENDING
    [2015-11-11 ...] Informed scheduler that task InputFile() has status DONE
    [2015-11-11 ...] Done scheduling tasks
    [2015-11-11 ...] Running Worker with 1 processes
    [2015-11-11 ...] Starting pruning of task graph
    [2015-11-11 ...] Done pruning task graph
    [2015-11-11 ...] [pid 87712] Worker Worker(...) running DailyPlays(date=2015-10-08)
    [2015-11-11 ...] [pid 87712] Worker Worker(...) done      DailyPlays(date=2015-10-08)
    [2015-11-11 ...] Informed scheduler that task DailyPlays(date=2015-10-08) has status DONE
    [2015-11-11 ...] Starting pruning of task graph
    [2015-11-11 ...] Done pruning task graph
    [2015-11-11 ...] Done
    [2015-11-11 ...] There are no more tasks to run at this time
    [2015-11-11 ...] Worker Worker(...) was stopped. Shutting down Keep-Alive thread
    [2015-11-11 ...]
    ===== Luigi Execution Summary =====

    Scheduled 2 tasks of which:
    * 1 present dependencies were encountered:
        - 1 InputFile()
    * 1 ran successfully:
        - 1 DailyPlays(date=2015-10-08)

    This progress looks :) because there were no failed tasks or missing external dependencies

    ===== Luigi Execution Summary =====

    $ python main.py DailyTopArtists --date 2015-10-08 --local-scheduler

    ...

    $ cat DailyTopArtists/2015-10-08.tsv
    Aluminica   13776
    Ono 11052
    Red Floyd   2824
    Rolling Waters  2818
    The Carpenters  2796

To run with luigi daemon, start `luigid` in a separate terminal.
