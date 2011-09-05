#SysStat#
SysStat is (or will be) a system monitoring system similar to cacti without the focus on RRD and SNMP.

SysStat is bassed arround a plugable sensors archetecture and is designed in with a client-server setup in mind.

The majority of the backend code will be writen in [Python 3][4] and the first plugins will likly focus on reading data from the output of common Linux (unix) tools.

## Components ##

### Monitor ###
The monitor is the component that activly collects the statistics. It should be running all the time and should be conidered stateful.
That is clumulative data (such as the included ifconfig scraper) should return the desired data not the raw data. (In this case the average speed rather than the total amount of trafic over the interface)

### Communicator ###
This component requests the statistics from the monitors and inserts the information into the database.

### Database ###
This is really up to you - though I will primarly be developing this application with MySQL to start with for simplicites sake though I will likly branch out to PostgreSQL before too long.

### JSON Data API ###
The database will primarly be access through a JSON api. This has a lot to do with the fact the my primary frontend will be done in HTML5/JavaScript.

### Frontend ###
As mentioned the primary frontend will be done with HTML5 and JavaScript.

I will be likly making lots of use of the [InforVis][1] graphing toolkit here as well as either [Prototype][2] or [jQuery][3]. (I am presntly undecided here - everyone seams to use jQuery, but I am more comfertable with Prototype)

[1]: http://thejit.org/       "JavaScript InfoVis Toolkit"
[2]: http://prototypejs.org/  "Prototype JavaScript framework: Easy Ajax and DOM manipulation for dynamic web applications."
[3]: http://jquery.com/       "jQuery: The Write Less, Do More, JavaScript Library"
[4]: http://python.org/       "Python Programming Language - Official Website"
