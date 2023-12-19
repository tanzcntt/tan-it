import pandas as pd
from config import settings
from definitions import ROOT_DIR
from helpers.images import draw_imagẹ̣̣̣
from helpers.directory import create_output_dir

def read_excel_and_draw_image(excel_name):
    filename = settings['directory']['input'] + '/' + excel_name + '/' + settings['directory']['default_input_exls']
    df = pd.read_excel(filename, sheet_name='data', nrows=1000)
    output_dir_elsx = ROOT_DIR + '/' + settings['directory']['output'] + '/' + excel_name
    for index, row in df.iterrows():
        output_dir_image = create_output_dir(row['Xa lan'], excel_name)
        date_time = row['Thoi gian'].strftime("%d/%m/%Y, %H:%M:%S")
        text = row['Vi tri'] + ' ' + date_time
        draw_imagẹ̣̣̣(excel_name, row['Xa lan'], row['STT'], text, output_dir_image)
        
            
    print("DONE")
    