#include <iostream>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fstream>


using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

int main(int argc, char** argv) {
    if (argc!=2) {
        cout << "Error in number args" <<endl;
        return 1;
    }
    DIR *catalog = opendir(argv[1]);
    if (!catalog) {
        cout << "Error in opening catalog: " << argv[1] << endl;
        return 1;
    }
    cout << "Opening was successfully!" <<endl;
    struct dirent *counter;
    while (counter=readdir(catalog)) {
        string path=argv[1];
        path+='/';
        path+=counter->d_name;
        struct stat buf;
        lstat(path.c_str(), &buf);
        if (S_ISREG(buf.st_mode) == 1) {
            if (path.substr(path.length()-4, 4)==".svg") {
                ifstream f(path);
                ofstream n(path.substr(0, path.length()-4)+"_new.svg");
                string line;
                while (getline(f, line)) {
                    if (line.find("<rect")!=std::string::npos) {
                        if ((line.find("rx")==std::string::npos) && (line.find("ry")==std::string::npos)) {
                            int pos=line.find("/>");
                            line.insert(pos, " rx=\"20\" ry=\"40\" ");
                            n << line <<endl;
                        } else {
                            int posX=line.find("rx");
                            int posS=line.find(" ", posX);
                            if (posS==std::string::npos || posS>line.find("/>")) posS=line.find("/>");
                            line.erase(posX, posS-posX);
                            int posY=line.find("ry");
                            int posS1=line.find(" ", posY);
                            if (posS1==std::string::npos || posS1>line.find("/>")) posS1=line.find("/>");
                            line.erase(posY, posS1-posY);
                            n << line <<endl;
                        }
                    } else n << line <<endl;
                }
                cout << "Succes" << endl;
                cout <<path.substr(0, path.length()-4)+"_new.svg"<<endl;
                f.close();
                n.close();
            }
        }
    }
    if (closedir(catalog) ==-1) {
        cout <<"Error close!" <<endl;
        return 1;
    }
    return 0;
}