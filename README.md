# DB_Strafer

A tool for stress and performance tests on databases that monitors CPU, RAM and disk space abuse simultaniously. Contains two components:

###Strafer
A prcess that connects to a database and runs queries from an SQL file the user provides, at whichever frequency the user configures.

###Monitor
A process that gathers information about CPU, RAM and disk space usage from the database server at a frequency the user configures. Creates a CSV report with its findings.

You can run it in one of two ways:

1. One machine runs the Strafer, stressing the database with queries, while the database server machine is running the Monitor.
2. Due mode, running both a Strafer process and the monitor process on the database server machine.

##Phase I of development
Includes a simpler UI through which the Strafer and Monitor are configured and errors during runs are shown.

##Phase II of development:
UI includes a performance graph with the data gathered by the Monitor, as well as the CSV report. Graph can be seen on the Monitor and the Atrafer if working in split mode.


##This is a work in progress and you can watch this space to see it grow!


