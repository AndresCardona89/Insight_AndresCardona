# Insight_AndresCardona

Andres Cardona
Coding challenge_Insight_Andres Cardona

DESCRIPTION

This code reads payments from two .txt file in CSV format.
It reads the batch_payment.txt file to create the initial state of the graph and then iterates throuh each payment of strem_payment.txt verifying each payment according to different features.

REQUIREMENTS

This program assumes you have Python 3.5 installed and the shebang '#!/usr/bin/env python' points to the Python 3.5 interpreter your machine. These code attempts to find the python 3.5 interpreter in the specifed location, it is recommended to uninstall any previous version of python before running this code.

It also assumes you have the common libraries described below.

STRUCTURE (Libraries)

-datetime: Offers objects and variables to handle dates and times

-pandas: Library for data analysis

-os: Provides tools for using operating system functionalities.

USAGE

Download the full folder and execute run.sh in the shell console. Make sure a proper 'batch_payment.txt' and 'stream_payment.txt' file with CSV format exists in the 'paymo_input' folder.

When the codes ends execution, three new files will be created with the verification of each payment in 'stream_payment.txt'.

COMMENTS

This coding challenge was coded using the minimum external libraries. With the use of these libraries, execution time would be more efficient. However, since the focus of this challenge is to evaluate my habilities as a programmer, it is written with basic structures and objects.
