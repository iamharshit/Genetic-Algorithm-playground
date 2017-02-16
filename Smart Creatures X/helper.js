function DNA(genes){
	if(genes){
      this.genes = genes;
    } 
    else{
      //genes store force magnitude
      this.genes = [];
      for(var i=0;i<lifespan;i++){
        this.genes[i] = p5.Vector.random2D();
        this.genes[i].setMag(maxforce);
      }
	}

   
	this.crossover = function(partner){
		var newgenes = [];
		var mid = floor(random(this.genes.length));
		for(var i=0; i<this.genes.length; i++){
			if(i > mid){
				newgenes[i] = this.genes[i];
			}
			else{
				newgenes[i] = partner.genes[i];	
			}
		}
		return new DNA(newgenes);
	}

	this.mutation = function(){
  		for(var i = 0; i < this.genes.length; i++){
  			if(random(1)<0.01){
  				this.genes[i] = p5.Vector.random2D();
  				this.genes[i].setMag(maxforce);
  			}
  		}
  	}
}

//-------------------------------------------
function Creature(dna){
	this.pos = createVector(width/2, height);
	this.vel = createVector();
	this.acc = createVector();
	this.completed = false;
	this.crashed = false;

	if(dna){
		this.dna = dna;
	}
	else{
		this.dna = new DNA();
	}
	this.fitness=0;

	this.applyForce = function(force){
		this.acc.add(force);
	}

	this.calcFitness = function(){
		var d = dist(this.pos.x, this.pos.y, target.x, target.y);
		this.fitness = width-d;

		//making fitness over-dominant or under-dominant
		if(this.completed){
			this.fitness *= 10;
		}
		else if(this.crashed){
			this.fitness /= 10;	
		}
	}

	this.update = function(){
		var d = dist(this.pos.x, this.pos.y, target.x, target.y);
		
		// if hitted the target
		if(d<10){
			this.completed = true;
			this.pos = target.copy();
		}

		//if hitted obstacle
		if(this.pos.x>rx && this.pos.x<rx+rw && this.pos.y>ry && this.pos.y<ry+rh){
			this.crashed = true;
		}

		//if hitted side-walls
		if(this.pos.x>width || this.pos.x<0){
			this.crashed = true;
		}
		if(this.pos.y>height || this.pos.y<0){
			this.crashed = true;
		}

		this.applyForce(this.dna.genes[count]);
		if(!this.completed && !this.crashed){
			this.vel.add(this.acc);
			this.pos.add(this.vel);
			this.acc.mult(0);
			this.vel.limit(4);
		}
	}

	this.show = function(){
		push();
		noStroke();
		fill(color(240,12,71)); //240-128-128
		translate(this.pos.x, this.pos.y);
		rotate(this.vel.heading());
		rectMode(CENTER);
		rect(0, 0, 25, 5);
		pop();
	}
}

//-------------------------------------------
function Population(){
	this.popsz = 50;
	this.creatures = [];
	this.matingpool = [];

	for(var i=0; i<this.popsz; i++){
		this.creatures[i]=new Creature();
	}

	this.evaluate = function(){
		//calculating maximum fitness
		var maxfit = 0;
		for(var i = 0; i < this.popsz; i++){
			this.creatures[i].calcFitness();
			maxfit = Math.max(maxfit, this.creatures[i].fitness);
		}

		//calc. relative fitness
		for(var i = 0; i < this.popsz; i++){
			this.creatures[i].fitness /= maxfit;
		}

		//reproduction: selecting for mating pool
		this.matingpool = [];
		for(var i=0; i<this.popsz; i++){
			for(var j=0; j<this.creatures[i].fitness*100; j++){
				this.matingpool.push(this.creatures[i]);
			}
		}
	}
	
	// crossover and mutation
	this.selection = function(){
		var newCreatures = [];
		for(var i=0; i<this.creatures.length; i++){
			//choosing the parents at random
			var parent1 = random(this.matingpool).dna;
			var parent2 = random(this.matingpool).dna;
			var child_dna = parent1.crossover(parent2);
			child_dna.mutation();
			newCreatures[i] = new Creature(child_dna);
		}

		this.creatures = newCreatures;
	}

	this.run = function(){
		// update position and display on canvas
		for(var i = 0;i<this.popsz;i++){
			this.creatures[i].update();
			this.creatures[i].show();
		}
	}
}