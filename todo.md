Overview

GUI (planned)

Master_Loop

    Journey_Init
        Intro_Story (planned)
        Galaxy_Gen (mostly complete)
        Choose_Colony_Site (planned)
        Construct_Ship (in progress)
        init Ship_State (in progress)

    while not (Ship_State.pos==Colony_Site)
        Travel_Rest_Loop
            Pathfinder (in progress)
            Move_to (planned)
            Travel_Events (in progress)
            Ship_State
            System_Summary (planned)

            for (Ship_State.actions)
                Real_Space_Loop
                    System_Events (in progress)
                    Action_List (in progress)
                    Ship_State
            
    Journey_End 
        Ship_State
        End_Story (planned)