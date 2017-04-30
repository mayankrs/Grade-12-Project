#Gate Entry
class IDPass:
    def __init__(self):
        self.name = "No Name Given."
        self.dob = "No Date Of Birth Given."
        self.id = "No ID Card Given."
        self.pno = "No Phone Number Given."
        self.dur = "No Duration of Stay Given."
        self.carno = "No Car Number Given."
        self.house = "No House Number Given."
        self.money = "No Amount Given."

    def inp(self):
        self.name = raw_input("Enter Name Of Visitor ... ")
        self.dob = raw_input("Enter Date Of Birth ... ")
        self.id = raw_input("Enter ID Number ... ")
        self.pno = input("Enter Phone Number ... ")
        self.dur = input("Enter Duration Of Stay ... ")
        self.carno = input ("Enter Car Number ... ")
        self.house = raw_input ("Enter House Number ... ")

    def printing(self):
        print
        print
        print
        print
        print
        print "___________________________________________________"
        print "Welcome Visitor, This Is your Visiting Card."
        print "___________________________________________________"
        print
        print "The Visitor's Name Is \"", self.name, "\""
        print "The Visitor's Date Of Birth Is \"", self.dob,"\""
        print "The Visitor's ID Number Is\"", self.id,"\""
        print "The Visitor's Car Number Is\"", self.carno,"\""
        print "The Visitor's House Number Is \"", self.house, "\""
        print "The Visitor's Phone Number Is \"", self.pno, "\""
        print "The Visitor's Duration Of Stay Is \"",self.dur, "\"", "Days."
        print "___________________________________________________"

print "Welcome To Al Khor Community Security Gate System. Enter Following Information."
print
c = IDPass()
c.inp()
c.printing()


import Community_gate

        
        


        
        
