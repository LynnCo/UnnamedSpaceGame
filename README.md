UnnamedSpaceGame
================

Rougelike space adventure

**Completion target:** Spring 2014

**Game Flow**

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
