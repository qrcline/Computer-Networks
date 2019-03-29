#include <iostream>
#include <string>
#include <fstream>
#include <cctype>
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
	cout << "what is the file name?" << endl;
	string fileName;
	cin >> fileName;
	ifstream myFile;
	myFile.open(fileName);
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
	myFile.close();
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
	for(int i=0;i<(length/2);i++)
	{
		swap(A[i], A[length - i]);

	}
	printArray(A, length);
}

bool


int main()
{
	//helloPerson();
	//readFile();
	int array[9] = {1,2,3,4,5,6,7,8,9}; 
	swapArray(array, 9);

	return 0;
}