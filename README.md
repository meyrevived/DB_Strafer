# DB_Strafer

A tool for stress and performance tests on databases that monitors CPU, RAM and disk space abuse simultaniously. Contains two components:

### Strafer
A prcess that connects to a database and runs queries from an SQL file the user provides, at whichever frequency the user configures.

### Monitor
A process that gathers information about CPU, RAM and disk space usage from the database server at a frequency the user configures. Can create a CSV report with its findings at user's request. 

You can run it in one of two ways:

1. Split mode - one machine runs the Strafer, stressing the database with queries, while the database server machine is running the Monitor.
2. Due mode -  running both a Strafer process and the Monitor processes on the database server machine.

## Phase I of development
Includes a simpler UI through which the Strafer and Monitor are configured and errors during runs are shown.

## Phase II of development:
UI includes a performance graph with the data gathered by the Monitor, as well provide a CSV report on demand.

## Phase II of development:
Monitor can control Strafer to stop or start strafing. 
Strafer can also show the graph of monitoring results

## Databases to cover
In order of development:
1. PostgreSQL
2. MySQL
3. Oracle
4. SQL Server
5. DB2
6. MongoDB



## This is a work in progress - watch this space to see it grow!


