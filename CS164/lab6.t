var num1 
var num2 
var num3 
var num4
var num5 
var count 
var sum 
var avg


       	fun init() {

	count : 0
	sum : 0
	
	num1 : 23
	num2 : 45
	num3 : 33
	num4 : -32
	num5 : 93
	
	if .num1 > 0 {
	iprint(.num1)
	sprint(" is a positive number, so we will add it to the sum, and add 1 to the count.")
	sprint("\n")
	count : .count + 1
	sum : .sum + .num1

		if .num2 > 0 {
        	iprint(.num2)
        	sprint(" is a positive number, so we will add it to the sum, and add 1 to the count.")
        	sprint("\n")
        	count : .count + 1
        	sum : .sum + .num2

			if .num3 > 0 {
        		iprint(.num3)
        		sprint(" is a positive number, so we will add it to the sum, and add 1 to the count.")
        		sprint("\n")
        		count : .count + 1
        		sum : .sum + .num3   
	     		
				if .num4 > 0 {
        			iprint(.num4)
        			sprint(" is a positive number, so we will add it to the sum, and add 1 to the count.")
        			sprint("\n")
        			count : .count + 1
        			sum : .sum + .num4
        			
			
					if .num5 > 0 {
        				iprint(.num5)
        				sprint(" is a positive number, so we will add it to the sum, and add 1 to the count.")
        				sprint("\n")
        				count : .count + 1
        				sum : .sum + .num5
					}
				}	
        		}
		}
	}
	else {
	count : .count + 0
        sum : .sum + 0
	iprint(.num1)
	sprint(" is not a positive number, so we wont add it to the sum, and we'll just print out the sum, count and average")   
	}

	avg : .sum / .count
	sprint("Sum: ")
	iprint(.sum)
	sprint("\n")
	sprint("Count: ")
	iprint(.count)
	sprint("\n")
        sprint("Average: ")
        iprint(.avg)
}


