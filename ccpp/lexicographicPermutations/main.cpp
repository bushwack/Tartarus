//LEXICOGRAPHIC PERMUTATION GENERATOR
//MARK JUDICE
//http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

#include "iostream"
#include <string>
#include <stdio.h>
#include <stdlib.h>
//#include <cstdio>
//#include <ctime>

using namespace std;

int len(char s[]){
	int i = 0;
	while(s[i] != '\0'){
		i++;
	}
	return i;
}

int stepOne(char s[]){
	int k = -1;
	for(int i = 0; i < len(s) - 1; i++){
		if(s[i] < s[i+1]) k = i;
	}
	return k;
}

int stepTwo(char s[], int k){
	int l = -1;
	for(int i = 0; i < len(s); i++){
		if(s[k] < s[i]) l = i;
	}
	return l;
}

void swap(char* x, char* y){
	char t = *x;
	*x = *y;
	*y = t;
}

void reverse(char s[], int j, int k){
	if(!(k > j)) return;
	if(j < 0 || k < 0) return;
	char* stack = (char*)malloc((k - j)*sizeof(char)+1);
	char stackPtr = 0;
	for(int i = j; i <= k; i++){
		*(stack + stackPtr) = s[i];
		stackPtr+=1;
	}
	stackPtr-=1;
	for(int i = j; i <= k; i++){
		s[i] = stack[stackPtr];
		stackPtr -= 1;
	}
	delete[] stack;
}

void permutate(char s[]){
	int num = 1;
	cout << s << endl;
	while(true){
		int k = stepOne(s);
		if(k < 0){
			cout << "\nDone. " << num << " permutations generated." << endl;
			return;
		}
		int l = stepTwo(s,k);
		swap(&s[k],&s[l]);
		reverse(s,(k+1),len(s)-1);
		cout << s << endl;
		num+=1;
	}
}

void sort(char s[]){
	for(int i = 0; i < len(s); i++){
		for(int j = 0; j < len(s); j++){
			if(s[i] < s[j]) swap(&s[i],&s[j]);
		}
	}
}



int main(void){
	
	string in;
	cout << "What string would you like to permutate? Keep it less than 8 characters or bad things will happen...\n";
	cin >> in;
	
	char* s = (char*)malloc(in.length() * sizeof(char) + 1);
	int i;
	for(i = 0; i < in.length(); i++){
		s[i] = in[i];
	}
	s[i] = '\0';
	cout << "\nGenerating permutations for " << s << "....\n\n";

//	clock_t start;
//	double duration;
//	start = clock();

	sort(s);
	permutate(s);

//	duration = (clock() - start) / (double) CLOCKS_PER_SEC;
//	cout << "\nProgram took " << duration << " seconds to complete.\n\n\n\n";

	delete[] s;
}


