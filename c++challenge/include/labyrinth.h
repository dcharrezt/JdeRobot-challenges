#ifndef LABYRINTH_H
#define LABYRINTH_H

#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <fstream>
#include <map>

typedef std::vector<std::vector<char>> environment;
typedef std::map<std::pair<int,int>, bool> visited;
typedef std::vector<std::vector<std::pair<int,int>>> paths;

class Labyrinth
{

public:
    Labyrinth();
    
    void startLabyrinth();
    void printEnvironement();
    void solveLabyrinth();

private:
    int labyrinthWidth;
    int labyrinthHeight;
    std::string fileName;
    environment env;

};

#endif