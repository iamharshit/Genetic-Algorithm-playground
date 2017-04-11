#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;

// humans represented by 2 and AI Robot by 1
int humans = 50;
int robots = 100;
//useful values are stored from 1 to 20 
int arr[22][22];
void display(){
	char c;
	for(int i=1;i<=20;i++){
		for(int j=1;j<=20;j++)
			if(arr[i][j]==0)
				cout<<"-"<<" ";
			else if(arr[i][j]==1)
				cout<<"X"<<" ";
			else if(arr[i][j]==2)
				cout<<"O"<<" ";
		cout<<endl;
	}
}		


class Creature{
	public:
		int x,y,age;
		int getX(){ return x; }
		int getY(){ return y; }
		int get_age(){ return age; }
		void set_age(int age_) { age=age_; }
		virtual void birth(int x,int y){ }
		virtual void move(){ }
		virtual void breed(){ }
		void next_place(int oldx, int oldy, int who){
			if(arr[oldx-1][oldy]==0){
				arr[oldx][oldy]=0;
				arr[oldx-1][oldy]=who;
				x--;
			}
			else if(arr[oldx+1][oldy]==0){
				arr[oldx][oldy]=0;
				arr[oldx+1][oldy]=who;
				x++;
			}
			else if(arr[oldx][oldy-1]==0){
				arr[oldx][oldy]=0;
				arr[oldx][oldy-1]=who;
				y--;
			}
			else if(arr[oldx][oldy+1]==0){
				arr[oldx][oldy]=0;
				arr[oldx][oldy+1]=who;
				y++;
			}
		}
};

class Human:public Creature{
	public:
		void birth(int x_,int y_){
			this->x, this->y = x_, y_;
			age = 0;
			arr[x_][y_] = 2;
		}				
		void move(){
			age++;
			next_place(x, y, 2);
		}
		void breed(int i,int j){
			if(!arr[i-1][j]){
					birth(i-1,j);
					humans++;
			}
			else if(!arr[i+1][j]){
					birth(i+1,j);
					humans++;
			}
			else if(!arr[i][j+1]){
					birth(i,j+1);
					humans++;
			}
			else if(!arr[i][j-1]){
					birth(i,j-1);
					humans++;
			}
		}
};

class Robot:public Creature{
	public:
		int eat;
		
		void death_check(){
			if(age%4==0 && eat>0)
				eat = 0;
			else if(age%4==0){
				robots--;
				arr[x][y]=0;
			}
		}

		Robot(){ eat=0; }
		void birth(int x_,int y_){
			this->x, this->y = x_, y_;
			age = 0;
			arr[x_][y_] = 1;
		}	
		void move(){
			death_check();
			age++;
			humans--;
			if(arr[x-1][y]==2){
				arr[x-1][y]=1;
				arr[x][y] = 0;
				eat++;
			}
			else if(arr[x+1][y]==2){
				arr[x+1][y]=1;
				arr[x][y] = 0;
				eat++;
			}
			else if(arr[x][y+1]==2){
				arr[x][y+1]=1;
				arr[x][y] = 0;
				eat++;
			}	
			else if(arr[x][y-1]==2){
				arr[x][y-1]=1;
				arr[x][y] = 0;
				eat++;
			}	
			//corners
			else if(arr[x+1][y+1]==2){
				arr[x+1][y+1]=1;
				arr[x][y] = 0;
				eat++;
			}
			else if(arr[x+1][y-1]==2){
				arr[x+1][y-1]=1;
				arr[x][y] = 0;
				eat++;
			}
			else if(arr[x-1][y-1]==2){
				arr[x-1][y-1]=1;
				arr[x][y] = 0;
				eat++;
			}
			else if(arr[x-1][y+1]==2){
				arr[x-1][y+1]=1;
				arr[x][y] = 0;
				eat++;
			}
		   else{ 
				humans++;
				next_place(x, y, 1);
			}
		}
		void breed(int i,int j){
			if(!arr[i-1][j]){
					birth(i-1,j);
					robots++;
			}
			else if(!arr[i+1][j]){
					birth(i+1,j);
					robots++;
			}
			else if(!arr[i][j+1]){
					birth(i,j+1);
					robots++;
			}
			else if(!arr[i][j-1]){
					birth(i,j-1);
					robots++;
			}
		}
};		
	
int main(){
	
	int default_ = 10;
	for(int i=0;i<=21;i++){
		arr[0][i], arr[21][i] = default_, default_;
		arr[i][0], arr[i][21] = default_, default_;
	}
	
	Human *h = new Human[humans];
	Robot *r = new Robot[robots];
	//Initialisation	
	int m,n;
	for(int i=0;i<humans;i++){
		do{
			m=rand()%21;
			n=rand()%21;
		}while(arr[m][n]!=0);
		h[i].birth(m,n);
	}
	display();
	for(int i=0;i<robots;i++){
		do{
			m=rand()%21;
			n=rand()%21;
		}while(arr[m][n]!=0);
		r[i].birth(m,n);
	}		
	
	//Generations
	char response;
	do{
		system("CLS");
		display();
		
		//handling all robots
		for(int i=0;i<robots;i++){
			if(r[i].get_age()==8){
				r[i].age=0;
				r[robots+1].breed(r[i].getX(), r[i].getY());
			}
			r[i].move();
		}
		
		system("CLS");
		display();
		system("PAUSE");

		//handling all humans
		for(int i=0;i<humans;i++){
			if(h[i].get_age()==3){
				h[i].age=0;
				h[humans+1].breed(h[i].getX(), h[i].getY());
			}
			h[i].move();
		}
		
		cout<<"Total Robots : "<<robots<<endl;
		cout<<"Total Humans : "<<humans<<endl;	
		cout<<"Enter y for next time step : "; cin>>response;		
	}while(response == 'y');
		
	return 0;
}
