//Quinton Cline
//Networks Warmup 

#include <iostream>
#include <string>
#include <fstream>
#include <cctype>
#include<unordered_map>
using namespace std;


void helloPerson()
{
	cout << "what is your name?" << endl;
	string name;
	cin >> name;
	cout << "Hello " << name << endl;
}

void readFile()
{
	cout << "Please input the file name of the text you want to squash?" << endl;
	string fileName;
	cin >> fileName;
	ifstream myFile(fileName);
	//myFile.open(fileName);
	if (myFile.fail())
		cout << "There was an error opening the file" << endl; 
	string word;
	string wordTemp;

	while (!myFile.eof())
	{
		myFile >> wordTemp;
		for(int i=0;i<wordTemp.length();i++)
		{
			wordTemp[i] = std::tolower(wordTemp[i]);
		}
		word += wordTemp; 
	}	
	//myFile.close();
	cout << word << '\n';
	for(int i=97; i<123; i++)
	{
		int count = 0;
		for(int y=0;y<word.length();y++)
		{
			if (word[y] == (char)i)
				count++;
		}
		cout << char(i) << " " << count << endl;
	}
	for (int i = 48; i < 58; i++)
	{
		int count = 0;
		for (int y = 0; y < word.length(); y++)
		{
			if (word[y] == (char)i)
				count++;
		}
		cout << char(i) << " " << count << endl;
	}


}

void printArray(int A[], int lenght)
{
	for(int i=0;i<lenght; i++)
	{
		cout << A[i] << " ";

	}
	cout << endl;
}
void  swapArray(int A[], int length)
{
	printArray(A, length);
	int * arrayTemp = new int[length];

	for(int i=0;i<length;i++)
	{
		arrayTemp[i] = A[length -i-1]; 

	}
	printArray(arrayTemp, length);
}

struct node
	{
		int data;
		node* next=nullptr;
		int isCircular();
	};
int node::isCircular()
{
	node *temp = this;
	unordered_map<node*,int> myMap; //the key and map will be int
	while(temp!=nullptr)
	{
		if(myMap.find(temp)!= myMap.end())
		{
			return 1; 
		}
		myMap[temp] = 1;
		temp = temp->next; 
	}
	return 0; 


}


int main()
{
	helloPerson();
	readFile();
	cout << "Array swap" << endl; 
	int array[9] = {1,2,3,4,5,6,7,8,9}; 
	swapArray(array, 9);

	cout << "Linked List Check" << endl; 
	node* node1=new node();
	node* node2 =new node();
	node* node3 =new node();
	node* node4 =new node();
	node1->next = node2;
	node2->next = node3;
	node3->next = node2; 
	cout << node1->isCircular(); 





	return 0;
}