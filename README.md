twitter_fun
===========

Fun with the Twitter Python API, running local searches

Nothing mind blowing about this repo. It generates public status search results based
on keywords and the area provided. Each keyword generates a file output with a partial HTML page format.

The output from the script is being used here:  http://jacqueline.io/mgm-twitter-search/
The website is using Start Bootstrap - Simple Sidebar HTML Template (http://startbootstrap.com)
for the template. It's free, so get your copy. I `cat`-ed the output files into 
one file to use in the simple sidebar HTML template.
For Example:
    `cat page_output_1 >> newfile`

I was asked by a local reporter my opinion on the results of the hedonometer.org data
that Alabama one of the saddest (or maybe it was angriest) states. I remembered that 
I had an example using the Twitter API and thought it would be fun to see what I get.
It ended up being the old API that no longer works and I didn't have any API keys. 
But I still went ahead and downloaded the new API and updated my example to run the new one. 

I responded to the reporter with my take on the information and thought it would 
be neat to show him the "data". Nonetheless, info from my lenghty email was used but
I wasn't quoted :( , but maybe someone would like to run their own search for fun. 

The project that tells you the mood of a state based on words from Twitter: 
    http://www.hedonometer.org/maps.html?comp=Alabama

Local news article talking about the data:
    http://www.montgomeryadvertiser.com/story/money/2014/09/28/lol-matter/16375667/


## Twitter API
To use the Twitter API go to https://dev.twitter.com/apps/new and
create your app to get the keys/secrets need to the run the script.
