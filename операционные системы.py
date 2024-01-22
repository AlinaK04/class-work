#include <stdio.h>

int main()
{
 setlocale(LC_ALL, "Russian")
 int contestants[] = { 1, 2, 3 };
 int* choice = contestants;

 contestants[0] = 2;
 contestants[1] = contestants[2];
 contestants[2] = *choice;
 
 printf("Я собираюсь выбрать претендента номер номер %i\n", contestants[2]);
 return 0;
}
