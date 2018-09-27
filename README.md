# Arduino_acceleration_logger
An Arduino based accleration logger, writes to an SD-card or streams to a computer. 

This project is about logging acceleration data, simple as that. The unit can either run on batteries and write to an SD-card, or stream to a connected computer. The Arduino-sketch is timed to approximate 500Hz sampling rate, with a varying error of ca +/- 3ms

This repo contains a shopping list detailing the components of the logger, as well as gerber files for PCB-production and an assembly manual. Feel free to make your own :)

The project is provided "as-is", with no warranties. Batteries not included! But if you find any obvious improvements, feel free to post an issue. 

Assembly requires soldering as well as a drill with a 7mm and a 15mm drill. The unit can run on both a 9V battery or 6xAA batteries with the specified battery holder. Running on AA-batteries gives a substantially longer logging time. (tests show 36-40 hours of runtime on AA batteries, beware of large data-files!) 

You might be interested in splitting the datafile if it becomes too large to open on your computer. http://www.hjsplit.org/ is a free program which does that for you.

If you have no other way of producing PCB's, it can be ordered from here (be advised, Rev A (unmarked) and Rev B has critical errors on the board. Rev A may be used, : https://www.pcbway.com/project/shareproject/Arduino_acceleration_logger.html
