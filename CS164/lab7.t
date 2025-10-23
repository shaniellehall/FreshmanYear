#Shanielle Hall 
#snh325@drexel.edu 14730235 
#Lab 164-060

var t, h, g, v	# initializing variables t to time , h to height , g to gravity, and v to velocity 

fun cycle() { #this is a function that will run everytime the ball is in the air 
	if (.h >= 0 ) { # this function only runs if the height is greater than or equal to zero
	

	
		iprint(.t)
                sprint(" : ")
                iprint(.h)
                sprint("\n")

		t : .t + 1 # this adds one unit of time (second, minute, hour) to t and updates the value.
		calc() 
		cycle()
	}
	
	return 0
}

fun calc() { # this function calculates the height( where g(-10) is divided by two) and is multiplied by (a, or t, to the power of b, or 2) and is added to velocity multiplied by time.
	h : ((.g/2) * pow(.t, 2)) + (.v * .t)
}

fun pow(a, b) { # this function is a  loop that calculates a, to the power of b, where r is a placeholder for the loop.
	var r # variable r is declared
	r : 1 # r is initialized to the value of 1.

	loop { # loops until b is less than or equal to zero.
		until .b <= 0
		r : .r * .a # r is equal to the value of r * a
		b : .b - 1 # b is equal to its original value minus 1.
	}

	return .r # returns the value of r.
}

fun init() {
	var ui # initializes the variable ui.

	ui : iread("Enter an initial velocity")

	t : 0 # initializes the variable t to 0.
	h : 0 # initializes the variable h to 0.
	v : .ui # initializes the variable v to ui.
	g : -10 # initializes the variable g() to -10.

	cycle()
	
}

