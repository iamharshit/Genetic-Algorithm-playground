var lifespan = 350;
var population;
var target;
var count = 0;
var maxforce = 0.2;
var Para;
var generation=1;

var rx = 100;
var ry = 150;
var rw = 200;
var rh = 10;

function setup(){
  createCanvas(400,300);

  population = new Population();
  Para = createP();
  target = createVector(width/2, 50);
}

function draw(){
	background(0);
	population.run()
  Para.html("Generation  #"+generation);
  
  	count++;
  	if(count == lifespan){		
  		population.evaluate();
  		population.selection();
      
  		count = 0;
      generation++;
  	}
  	 
  	fill(200);
  	rect(rx, ry, rw, rh);
    fill(color(255,200,0)); 
  	ellipse(target.x, target.y, 20, 20)
}