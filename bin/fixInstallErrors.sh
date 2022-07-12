# Fix install errors
pip install -U pip
pip3 install -U pip
python3 -m pip install --upgrade pip
python3 -m pip3 install --upgrade pip
pip3 install --upgrade setuptools
pip install ez_setup
pip3 install ez_setup
pip install unroll 
pip3 install unroll 
easy_install -U setuptools
pip install unroll
pip3 install unroll
pip3 install -r requirements.txt
easy_install -U setuptools
pip3 install -r requirements.txt

#psycopg2 M1
brew install libpq --build-from-source
brew install openssl

export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib -L/opt/homebrew/opt/libpq/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include -I/opt/homebrew/opt/libpq/include"

brew install postgres
pip3 install psycopg2
conda install sqlite3
