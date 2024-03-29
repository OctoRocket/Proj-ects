#include <iostream>
#include <stdio.h>
#include <chrono>
#include <thread>
using namespace std;

/*
TO BE CONVERTED TO PYTHON
FOLLOW OS AND PROCCESER SPECIFIC INSTRUCTION TO COMPILE
*/

void sleep(int time) {
    std::chrono::duration<int, std::milli> timespan(time);
    std::this_thread::sleep_for(timespan);
}
void automatic_input()
{
    unsigned long long number = 1;
    unsigned long long x = number;
    unsigned long long iterations = 0;
    int time_choice;
    cout << "How long (in milisecs do you want the delay between outputs to be?\n";
    cin >> time_choice;
    while (true) {
        if (x == 1) {
            cout << "Done, with " << iterations << " iterations needed to get to one and the number was " << number << "\n\n\n\n";
            number++;
            x = number;
            iterations = 0;
            sleep(time_choice);
        }
        else if (x % 2 == 0) {
            x = x / 2;
            iterations++;
        }
        else {
            x = x * 3 + 1;
            iterations++;
        }
    }
}

void manual_input(unsigned long long x)
{
    unsigned long long iterations = 0;
    unsigned long long number;
    number = x;
    while (true) {
        if (x == 1) {
            cout << "Done, with " << iterations << " iterations needed to get to one and the number was " << number << "\n\n\n\n";
            break;
        }
        else if (x % 2 == 0) {
            x = x / 2;
            iterations++;
        }
        else {
            x = 3 * x + 1;
            iterations++;
        }
        cout << x << endl;
        sleep(100);
    }
}
int main()
{
    while (true) {
        int choice;
        cout << "Do you want, 1: for the program to run automatically, or 2: allow you to input a number and it to calculate it in 3x+1, type 1 or 2\n";
        cin >> choice;
        if (choice == 1) {
            automatic_input();
        }
        else if (choice == 2) {
            while (true) {
                cout << "What number do you want to calculate (use 0 for exit)\n";
                cin >> choice;
                if (choice == 0) {
                    return 0;
                }
                else {
                    manual_input(choice);
                }
            }
        }
        else {
            cout << "Try again!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
        }
    }
}