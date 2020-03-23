#include "../include/labyrinth.h"

#include <unistd.h>
#define GetCurrentDir getcwd

Labyrinth::Labyrinth()
{
    this->labyrinthWidth = 6;
    this->labyrinthHeight = 5;
}

int Labyrinth::getLabyrinthWidth()
{
    return this->labyrinthWidth;
}

int Labyrinth::getLabyrinthHeight()
{
    return this->labyrinthHeight;
}

void Labyrinth::readSchema()
{
    while(true) {
        std::string response;
        std::cout << "Enter the labyrinth schema file name or write (quit) to cancel:" << std::endl;
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
            for (auto row : this->env) {
                for (auto i : row) {
                    std::cout << i;
                }
                std::cout << "\n";
            }
        }
    }

}
