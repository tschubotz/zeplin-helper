# zeplin-helper
Helper to extract images and urls from Zeplin projects

### Prequisites
- Install requirements: `pip install -r requirements.txt`
- Put Zeplin username/password into `run.py`

### Run
`python run.py input.csv output.rst`

This will 
- Pull info about the screens specified in input.csv
- Write info about name and URLs to output.rst
- Download the snapshot images to `screens/(ios|android)/`

### Input file format
```
android_project_id,ios_project_id
android_screen_id_1,ios_screen_id_1
android_screen_id_2,ios_screen_id_2
...
android_screen_id_n,ios_screen_id_n
```
(Leave out ids that only exist on 1 platform.)
