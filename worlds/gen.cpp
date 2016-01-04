/* World generation */

#include <iostream>
#include <string>
#include <stdio.h>
#include <sys/stat.h>
#include <cstdlib>

int Tiles_X = 0;
int Tiles_Y = 0;
const std::string BASEPATH = "./";

#define NUM_TERRAIN_TYPES 4

char terrain_types[NUM_TERRAIN_TYPES][80] = {
    "grass",
    "desert",
    "woods",
    "plain"
};

int main(int argc, char* argv[])
{
    srand(time(NULL));
	// Check the number of parameters
    if (argc != 3) {
        // Tell the user how to run the program
        std::cerr << "Usage: " << argv[0] << " Tiles_X Tiles_Y" << std::endl;
        return 1;
    }

    Tiles_X = std::atoi(argv[1]);
    Tiles_Y = std::atoi(argv[2]);

  	printf("generating World...\n");

  	std::string path_x;
  	std::string path_y;
  	char tmp[5];

	for(int i = 0; i < Tiles_X; i++)
	{
	  	sprintf(tmp, "%d", i);
	  	path_x = BASEPATH+tmp;

		mkdir(path_x.c_str(),0755);

	    for(int j = 0;j < Tiles_Y; j++)
	    {
			sprintf(tmp, "%d", j);
			path_y = path_x+"/"+tmp;
		    mkdir(path_y.c_str(),0755);
            FILE *outfile = fopen((path_y + "/terrain.json").c_str(), "w");
            fprintf(outfile, "{\n"
                             "  type: \"%s\"\n"
                             "}\n", terrain_types[rand() % NUM_TERRAIN_TYPES]);
            fclose(outfile);
	    }
	}
	printf("%i tiles were generated\n",Tiles_X*Tiles_Y);

	return 0;
}
