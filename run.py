from zeplin.api import ZeplinAPI
from zeplin.project import Project
import sys
import csv

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print('Please provide csv with screen ids and also an output filename.\n\npython run.py input.csv output.rst\n')
        exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    
    # Load data from input file
    with open(input_filename, 'r') as input_file:
        input_reader = csv.reader(input_file, delimiter=',')
    
        screen_ids = []

        for line_number, row in enumerate(input_reader):
            # First line contains project ids.    
            if line_number == 0:
                android_project_id = row[0]
                ios_project_id = row[1]
            # Other lines contain screen ids
            else:
                screen_ids.append(row[:])
    
    # Pull info from Zeplin
    zeplin_api = ZeplinAPI('asdf', 'asdf', True)

    android_project = Project(android_project_id, zeplin_api)
    ios_project = Project(ios_project_id, zeplin_api)

    screens = []
    for android_screen_id, ios_screen_id in screen_ids:
        android_screen = None
        if android_screen_id:
            android_screen = android_project.get_screen(android_screen_id)
            android_screen.get_url()
            android_screen.download('screens/android/{}.png'.format(android_screen.name))
        ios_screen = None
        if ios_screen_id:
            ios_screen = ios_project.get_screen(ios_screen_id)
            ios_screen.get_url()
            ios_screen.download('screens/ios/{}.png'.format(ios_screen.name))
        
        screens.append([android_screen, ios_screen])
        
    # Write output file
    with open(output_filename, 'w') as output_file:

        for android_screen, ios_screen in screens:
            # Use the name of the Android screen as header, if existing
            screen_name = android_screen.name if android_screen else ios_screen.name
            output_file.write('''{}
{}
            
.. raw:: html

  <table>
    <tr>
      <td>
        <img src="screens/android/{}.png" width="240px"/>
      </td>
      <td>
        <img src="screens/ios/{}.png" width="240px"/>
      </td>
    </tr>
    <tr>
      <td>
        {}
      </td>
      <td>
        {}
      </td>
    </tr>
  </table>
  
  
'''.format(
    screen_name,
    ''.join(['~' for _ in range(len(screen_name))]),
    android_screen.name if android_screen else 'MISSING',
    ios_screen.name if ios_screen else 'MISSING',
    android_screen.url if android_screen else '',
    ios_screen.url if ios_screen else ''
))


