#ifndef LABYRINTH_H
#define LABYRINTH_H

#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <fstream>

typedef std::vector<std::vector<char>> environment;

class Labyrinth
{

public:
    Labyrinth();
    int getLabyrinthWidth();
    int getLabyrinthHeight();
    
    void readSchema();

private:
    int labyrinthWidth;
    int labyrinthHeight;
    std::string fileName;
    environment env;




};

#endif