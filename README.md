UnnamedSpaceGame
================

Procedural generation based space game, built from the ground up by mi, Lynn

ETA: 3/2014

Task Flow
----------

**Journey Init, runs once at the beggining**

    intro.story
Learn about what's going on

    galaxy.generate
Generate static galaxy elements

    intro.decisions
Get some stats, create a ship, choose where you're headed

----------

**Main_Sequence, runs until you reach your destination**

    pathfinder
Choose your next destination

    travel_events
Pulse travel events

    ship_state
Update ship state (at new location)

----------

**Real Space Loop, runs every time you drop out of subspace**

    action.create
Create available action list

    system_events
Bind events (on action or on arrival)

    system_overview
Write up the system description

    action.do
Allow user to choose actions, runs several times

    ship_state
Updates ship state
        
----------

**Journey End, runs when you get to destination**

    ship_state.history
Pull the ship state history

    end_story
Write the ending story