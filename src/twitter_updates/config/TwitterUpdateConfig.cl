# Top Level Paths
WindowsTopLevel = C:/Users/kurt_/github/Peru_COVID19_Stats/;
LinuxTopLevel = /home/kurt/remote/github/Peru_COVID_Stats/;

# Twitter auth
TwitterAuth = src/twitter_updates/config/auth.cl;

# Image paths
RawImages = res/raw_images;
GraphPath = res/graphs;

# Tweet search attributes
TwitterMINSA = Minsa_Peru;
TweetPattern = Esta es la situaci;
QueryTweets = 45;

# Bulletin cropped images location
RawCases = res/raw_images/cases.jpeg;
RawDeaths = res/raw_images/deaths.jpeg;
RawTests = res/raw_images/tests.jpeg;
RawRecov = res/raw_images/recovered.jpeg;
RawHospit = res/raw_images/hospitalized.jpeg;
RawCases24 = res/raw_images/cases24h.jpeg;

# Processed data location
PeruSimpleData = /data/PER_data.csv;
PeruFullData = /data/PER_full_data.csv;

# Twitter graphs
TwitterGraph1 = res/graphs/quad_graph1.png;
TwitterGraph2 = res/graphs/quad_graph2.png;

# Plot colors
CasesColor = #E04646;
RecoveredColor = #9CD347;
HospitalizedColor = #D8D13B;
DeathsColor = #8C8C8C;
TestsColor = #5B90F3;

# Tweet templates location
TwTemplate1 = src/twitter_updates/templates/FirstTweetTemplate.dat;
TwTemplate2 = src/twitter_updates/templates/SecondTweetTemplate.dat;

# Output tweet location
TweetExport = res/tweets.dat;

# Stats analysis region pattern for emoji indicator
NewCasesSA = [3,3,3,2,1,0,0,0];
NewRecoveredSA = [0,0,0,1,2,3,3,3];
NewHospitalizedSA = [3,3,3,2,1,0,0,0];
NewDeathsSA = [3,3,3,2,1,0,0,0];
NewCaseFatalitiesSA = [3,3,3,2,1,0,0,0];
NewTestsSA = [0,0,0,1,2,3,3,3];
NewPositivitySA = [3,3,3,2,1,0,0,0];