#include "../include/labyrinth.h"

Labyrinth::Labyrinth()
{
    this->labyrinthWidth = 7;
    this->labyrinthHeight = 5;
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
            this->fileName = "../tests/" + response;
                std::ifstream file(this->fileName);
            std::string tempstr;

            if(!file) {
                std::cerr << "The file cannot be found.\n";
                return;
            } else {
                while (std::getline(file, tempstr)) {
                    std::vector<char> temp;
                    for(auto i: tempstr) {
                        temp.push_back(i);
                    }
                    this->env.push_back(temp);
                }
            }

            std::cout << "Input: " << std::endl;
            printEnvironement();
            solveLabyrinth();
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

    // for (int i = 0; i < this->labyrinthHeight; i++) {
    //     for (int j = 0; j < this->labyrinthWidth; j++) {
    //         if(this->env[i][j] == '.' ) {
    //             std::cout << i<< ' ' << j;
    //         }
    //     }
    //     std::cout << "\n";
    // }

    std::cout << "Output:" << std::endl;
    for (int i = 0; i < this->labyrinthHeight; i++) {
        for (int j = 0; j < this->labyrinthWidth; j++) {
            std::cout << this->env[i][j];
        }
        std::cout << "\n";
    }
}