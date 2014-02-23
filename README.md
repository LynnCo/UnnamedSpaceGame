UnnamedSpaceGame
================

Rougelike space adventure

<h4>Timeline</h4>

IDK >_<

<h3>Game Flow</h3>

* Journey Init, runs once at the beggining
    * intro.story
    * galaxy.generate
    * intro.decisions
* Main_Sequence, repeats until you reach your destination**
    * pathfinder: choose your next destination
    * travel_events
    * Real Space Loop, runs every time you drop out of subspace
        * action.create
        * system_events
        * system_overview
        * action.do
* Journey End, runs when you get to destination


<h3>Story</h3>

Your people were a newly space faring race. The steady march of technology had recently turned the black abyss into a expanse one could cross, and cross it they did. Envoys were sent from and wide, in search of wealth, land,  and knowledge. Your group was of the latter, sent to a far away star that had been emitting strange frequencies. The frequencies turned out to be communication channels, and from a source that wasn't exactly welcoming.

[skip forward a bit]

You're imprisoned. A massive galactic empire of whom you were previously unware, decided to take interest in the new lifeform that has just shown up at it's doorstep. 

[this next part is randomly picked from a few scenarios, and this is just one option]

They've interned your crew in a facility filled with intelligent species from all around the sector, to be studied by their scientists. There are much worse fates that could befall a [PGP/race_name], but your method of incarceration is a particularly fortunate. The nature of the scientific research and the quanity of species present in the facility has allowed you to to gather a coalition of aliens capable both capable of communication and willing to use it as a means to plan an escape. In addition to that, the scientists have set up less than secure security protocols.

[/end story snippet]

So the story was just for creative inspiration, now im going to explain the game flow. Omitting the beggining section where you plan your escape, the game flow is very similar to Oregon Trail [if you can remember that] or simply an adventure / story game that is mainly text [ex: ]. It goes like so...

You're on a starship. A less that well mantained starship stolen from an alien race. Your crew [compromised of an assortment of aliens] is often are unsure how to operate the starship's subsystems. Beyond that, not all of your crew is from a spacefaring race, so they aren't entirely sure whats going on here. Long story short, this os a slapshod operation, but you make it work, because you need not to get caught by your pursuers.

So you're on a starship, traveling through the stars. You travel through the stars with a subspace drive [name wip]. You just escaped from internment of some sort. From that point [where you escaped from] your pursuers are spreading out a sensor net in a sphere, looking for you. Get caught in that net and you're going to have an entire fleet in your face. And so you run, until you can get atleast as far as their sensor net will check for you.

So yes, subspace drove between stars. Once you drop out of subspace, there are things to be done. Ex:

* repair electrical damage done by the time spent in subspace

* repair any structural damage done by crossing a crossing between realspace and subspace (ie a portal needs to be opened and its not always the right size)

* deal with crew sickness from time spent in subspace

* determine if another smaller subspace jump is required for you to reach your destination

* finally, you begin a burn on your realspace travel drive to your destination

These information and choices will be presented as a report from your crew to you, the captain. Example:

[CREW REPORT]

We have exited subspace into the gravity well of star TR128F, after spending 2.63 days in transit.

* 5 crew members appear to be sick from the time spent in transit, including 2 engineers for the hanger bay [-5

* There is a electrical overload in the anti-ship batteries, caused by the radiation dose the ship recieved during the jump.

How would you like to address these issues?

(On the left side of the screen there will be a panel showing you available resources. During any given time period the amont of of actions you can do is limited by the resources required for that action. Resources include: time, crew, materials, power, etc)

* [Priority heal] Send the sick engineers to the medical bay to be treated by medical staff (if available) [-1 crew] [1 day]

* [Full heal] Send all the sick crew to the medical bay [-2 crew] [2 days]

* [Repair] Send an engineer to fix the overload in the anti-ship batteriese [-1 crew] [-3 materials] [3 hours]

* [Reinforce] Send 2 engineers to fix the overload in the antiship batteries and add more sheilding in that area to prevent future overloads [-2 crew] [-20 materials] [12 hours]

* [Travel] Begin realspace burn to the star system

Up and down arrows to select an option, enter key to pick one. With you have an option highlighted, more information will be presented on it. For example, for reinforce it would show: how many engineers you have available, the current state of the sheilding on that subsystem, how many materials you have total.

In addition, time is important because you are being chased, so you should spend so much time in a star system. Also for resources that are not used up during an action [ex: power, crew] the time tells you how long it will be until that resource is available again.

The general game flow will be:

warp travel -> access ship state -> do star system activities [ex. mine, do repairs that require the ship be stationary, scan local objects] -> warp travel...

At any time that cycle can be interrupted by any of an array of special events.

The cycle repeats until the ship reachers a distination sufficiently far enough away from the origin that you can set the ship down on a planetary surface and avoid detection. Assuming you can make it this far [it shouldn't be easy], the game ends and tells you all sorts of things about your journey.
