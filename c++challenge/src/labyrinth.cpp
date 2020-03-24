#include "../include/labyrinth.h"

Labyrinth::Labyrinth()
{
    this->labyrinthWidth = 7;
    this->labyrinthHeight = 5;
    this->longestPathSize = 0;
}

void Labyrinth::startLabyrinth()
{
    while(true) {
        std::string response;
        std::cout << "Enter the labyrinth file name or write (quit) to cancel:" << std::endl;
        std::cin >> response;
        if (response == "quit") {
            break;
        } else {
            this->env.clear();
            this->visited.clear();
            this->paths.clear();

            this->fileName = "../tests/" + response;
                std::ifstream file(this->fileName);
            std::string tempstr;

            if(!file) {
                std::cerr << "The file cannot be found.\n";
            } else {
                while (std::getline(file, tempstr)) {
                    std::vector<char> temp;
                    for(auto i: tempstr) {
                        temp.push_back(i);
                    }
                    this->env.push_back(temp);
                }
                std::cout << "Input: " << std::endl;
                printEnvironement();
                solveLabyrinth();
            }


        }
    }
}

void Labyrinth::printEnvironement() {
    for (auto row : this->env) {
        for (auto i : row) {
            std::cout << i;
        }
        std::cout << "\n";
    }
}

void Labyrinth::solveLabyrinth() {

    int x, y;
    for (int i = 0; i < this->labyrinthHeight; i++) {
        for (int j = 0; j < this->labyrinthWidth; j++) {
            if(this->env[i][j] == '.' && !this->visited[std::make_pair(i,j)]) {
                x = i;
                y = j;
                visited[std::make_pair(x,y)] = 1;
                std::vector<std::pair<int, int>> tempPath;
                tempPath.push_back(std::make_pair(x, y));
                while(true) {
                    if( y-1>0 && env[x][y-1] == '.' && !this->visited[std::make_pair(x,y-1)]) {
                        visited[std::make_pair(x,y-1)] = 1;
                        tempPath.push_back(std::make_pair(x, y-1));
                        y = y-1;
                    } else if(y+1<this->labyrinthWidth && env[x][y+1] == '.' && !this->visited[std::make_pair(x,y+1)]) {
                        visited[std::make_pair(x,y+1)] = 1;
                        tempPath.push_back(std::make_pair(x, y+1));
                        y = y+1;
                    } else if(x-1>0 && env[x-1][y] == '.' && !this->visited[std::make_pair(x-1,y)]) {
                        visited[std::make_pair(x-1,y)] = 1;
                        tempPath.push_back(std::make_pair(x-1, y));
                        x = x-1;
                    } else if(x+1<this->labyrinthHeight && env[x+1][y] == '.' && !this->visited[std::make_pair(x+1,y)]){
                        visited[std::make_pair(x+1,y)] = 1;
                        tempPath.push_back(std::make_pair(x+1, y));
                        x = x+1;
                    } else {
                        break;
                    }
                }
                if(tempPath.size() > this->longestPathSize) {
                    this->longestPathSize = tempPath.size();
                    this->pathway = tempPath;
                }
                paths.push_back(tempPath);
            }
        }
    }

    std::cout << "Output: path size is " << this->longestPathSize << std::endl;
     for (int i = 0; i < this->longestPathSize; i++) {
            this->env[this->pathway[i].first][this->pathway[i].second] = '0' + i;
    }

    this->printEnvironement();

}