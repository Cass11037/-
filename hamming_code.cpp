#include <iostream>
#include <string>
#include <map>
#include <vector>
std::vector<std::string>  DICHARGE = { "r1", "r2", "i1", "r3", "i2", "i3", "i4" };

std::map<std::string, int> PartsingMessage(const std::string& code) {
    std::map <std::string, int> temp;
    for (int i = 0; i < code.size(); ++i) {
        temp[DICHARGE[i]] = int(code[i] - '0');
    }
    return temp;
}
int CalculatingTheErrorCode(std::map<std::string, int> mapCode) {
    int s1 = (mapCode["r1"] + mapCode["i1"] + mapCode["i2"] + mapCode["i4"])%2;
    int s2 = (mapCode["r2"] + mapCode["i1"] + mapCode["i3"] + mapCode["i4"])%2;
    int s3 = (mapCode["r3"] + mapCode["i2"] + mapCode["i3"] + mapCode["i4"])%2;
    std::string s = std::to_string(s1) + std::to_string(s2) + std::to_string(s3);
    return stoi(s);
}

std::string SearchErrors(const std::string& code, std::map<std::string, int> mapCode) {
    auto temp_s = CalculatingTheErrorCode(mapCode);
    switch (temp_s) {
        case 0:
            return "none";
            break;
        case 1:
            return "r3";
            break;
        case 10:
            return "r2";
            break;
        case 11:
            return "i3";
            break;
        case 100:
            return "r1";
            break;
        case 101:
            return "i2";
            break;
        case 110:
            return "i1";
            break;
        case 111:
            return "i4";
            break;

    }
    return "error";
}
void MakeRightCode(const std::string& code) {
    std::cout << "Correct code: ";
    auto mapCode = PartsingMessage(code);
    auto nameError = SearchErrors(code, mapCode);
    if (nameError == "none" or nameError == "error") {
        std::cout << code;
    }
    else {
        if (mapCode.count(nameError)) {
            if (mapCode[nameError] == 0) {
                mapCode[nameError] = 1;
            }
            else {
                mapCode[nameError] = 0;
            }
        }
        for (const auto& name_ : DICHARGE) {
            std::cout << mapCode[name_];
        }
        std::cout << std::endl << "error in " + nameError;
    }
}
int main()
{
    std::string s;
    std::cin >> s;
    if(s.size() == 7) {
        MakeRightCode(s);
    }
}
