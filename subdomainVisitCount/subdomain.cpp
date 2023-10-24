class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        unordered_map<string, int> domainCount;

        for (const string& cpdomain : cpdomains) {
            stringstream ss(cpdomain);
            int count;
            string domain;
            ss >> count >> domain;

            while (!domain.empty()) {
                domainCount[domain] += count;
                size_t dotPos = domain.find('.');
                if (dotPos == string::npos) {
                    break;
                }
                domain = domain.substr(dotPos + 1);
            }
        }

        vector<string> result;
        for (const auto& [domain, count] : domainCount) {
            result.push_back(to_string(count) + " " + domain);
        }

        return result;
    }
};