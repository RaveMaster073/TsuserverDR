from .test_ooc import _TestOOC

class TestScream_01_Scream(_TestOOC):
    def test_01_wrongarguments(self):
        """
        Situation: Clients attempt to use /scream incorrectly.
        """

        # Empty message
        self.c1.ooc('/scream')
        self.c0.assert_no_ooc()
        self.c1.assert_ooc('You cannot send an empty message.', over=True)
        self.c2.assert_no_ooc()
        self.c3.assert_no_ooc()

    def test_02_nonstaffscream(self):
        """
        Situation: C0 and C3, non-staff members, scream
        """

        # Assumptions
        # self.area0.scream_range = set([self.area1.name])    C0, C1 here
        # self.area4.scream_range = set()                     C2 here
        self.area5.scream_range = set([self.area0.name])    # C3 here

        # C0 (non-staff) screams
        self.c0.ooc('/scream Hi')
        self.c0.assert_ooc('You screamed "Hi".', over=True)
        self.c0.assert_no_ic()
        self.c1.assert_ooc('(X) {} screamed "Hi" ({}).'.format(self.c0_dname, 0), ooc_over=True)
        self.c1.assert_ic('Hi', over=True)
        self.c2.assert_ooc('(X) {} screamed "Hi" ({}).'.format(self.c0_dname, 0), over=True)
        self.c2.assert_no_ic() # C2 is not in scream range
        self.c3.assert_no_packets() # C3 is not in scream range

        self.c3.ooc('/scream Hu')
        self.c0.assert_ooc('Hu', username='<dollar>SCREAM[{}]'.format(self.c3_dname), ooc_over=True)
        self.c0.assert_ic('Hu', over=True) # C0 IS in scream range (compare to previous situation)
        self.c1.assert_ooc('(X) {} screamed "Hu" ({}).'.format(self.c3_dname, 5), ooc_over=True)
        self.c1.assert_ic('Hu', over=True) # C1 IS in scream range (compare to previous situation)
        self.c2.assert_ooc('(X) {} screamed "Hu" ({}).'.format(self.c3_dname, 5), over=True)
        self.c2.assert_no_ic() # C2 is not in scream range
        self.c3.assert_ooc('You screamed "Hu".', over=True)

    def test_03_staffscream(self):
        """
        Situation: C1 and C2, staff members, scream.
        """

        # C1 (staff) screams
        self.c1.ooc('/scream Ha')
        self.c0.assert_ooc('Ha', username='<dollar>SCREAM[{}]'.format(self.c1_dname), ooc_over=True)
        self.c0.assert_ic('Ha', over=True)
        self.c1.assert_ooc('You screamed "Ha".', over=True)
        self.c1.assert_no_ic()
        self.c2.assert_ooc('(X) {} screamed "Ha" ({}).'.format(self.c1_dname, 0), over=True)
        self.c2.assert_no_ic() # C2 is not in scream range
        self.c3.assert_no_packets() # C3 is not in scream range

        # C2 (staff) screams
        self.c2.ooc('/scream He')
        self.c0.assert_no_packets() # C0 is not in scream range
        self.c1.assert_ooc('(X) {} screamed "He" ({}).'.format(self.c2_dname, 4), over=True)
        self.c1.assert_no_ic() # C1 is not in scream range
        self.c2.assert_ooc('You screamed "He".', over=True)
        self.c2.assert_no_ic() # Self
        self.c3.assert_no_packets() # C3 is not in scream range

    def test_04_screamwhilemutedglobal(self):
        """
        Situation: C0 and C1 mute globals. C1 cannot use /scream, C0 and C1 do not receive screams.
        """

        self.c0.ooc('/toggle_global')
        self.c0.assert_ooc('You will no longer receive global messages.', over=True)

        self.c1.ooc('/toggle_global')
        self.c1.assert_ooc('You will no longer receive global messages.', over=True)

        self.c0.ooc('/scream I wanna scream')
        self.c0.assert_ooc('You have the global chat muted.', over=True)
        self.c1.assert_no_packets()
        self.c2.assert_no_packets()
        self.c3.assert_no_packets()

        self.c1.ooc('/scream and shout')
        self.c0.assert_no_packets()
        self.c1.assert_ooc('You have the global chat muted.', over=True)
        self.c2.assert_no_packets()
        self.c3.assert_no_packets()

        self.c3.ooc('/scream and let it all out')
        self.c0.assert_no_packets()
        self.c1.assert_no_packets()
        self.c2.assert_ooc('(X) {} screamed "and let it all out" ({}).'.format(self.c3_dname, 5),
                           over=True)
        self.c3.assert_ooc('You screamed "and let it all out".', over=True)
