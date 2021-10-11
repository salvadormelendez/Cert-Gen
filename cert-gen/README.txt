1.- Install fonts --> /usr/share/fonts/truetype/aenigma
sudo apt-get install -y ttf-aenigma

2.- Install stdIOMask
pip install stdiomask

3.- Modify "students_list.txt" with correct entries (Names and Email Addresses)

4.- Make sure you have the CERTIFICATE TEMPLATES and the UNIQUE CODES placed in their corresponding folder (e.g. 'mitm', 'slowloris')

5.- Run Python script: ./create_certificate.py

6.- Folder "certificates" contains the created certificates with the names from file "students_list.txt" (after running 'create_certificate.py')
    Certificates are archived in their corresponding folder (e.g. 'mitm', 'slowloris')
