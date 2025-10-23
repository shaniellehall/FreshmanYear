var state
var tab

fun init() {
	html("<center>")
    	button("Order", oBarcode)
    	button("Package", pBarcode)
    	button("Weight", pWeight)
    	html("<p>")
	tab : maketable(1, 1, null)
	setcell(.tab, 0, 0, "Light")

	state : 0
}

fun greenLight() {
    	setcellcolor(.tab, 0, 0, "green")
}

fun redLight() {
    	setcellcolor(.tab, 0, 0, "red")
}

fun null(){
}

fun oBarcode() {
    	if .state == 0 {
        	state : 1
        	greenLight()
    	}
    	else if .state == 1 {
        	state : 0
        	greenLight()
    	}
    	else if .state == 2 {
        	state : 0
        	redLight()
    	}
}

fun pBarcode() {
    	if .state == 0 {
        	state : 0
        	redLight()
    	}
    	else if .state == 1 {
        	state : 2
        	greenLight()
    	}
    	else if .state == 2 {
        	state : 1
        	redLight()
    	}
}

fun pWeight() {
    	if .state == 0 {
        	state : 0
        	redLight()
    	}
    	else if .state == 1 {
        	state : 1
        	redLight()
    	}
    	else if .state == 2 {
        	state : 1
        	greenLight()
    	}
}

