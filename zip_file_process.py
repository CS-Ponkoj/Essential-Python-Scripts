from zipfile import ZipFile 
import os

#put the input directory where zip is located
input_dir = "D:/New folder/"

#create temp folders for raw data
temp_dir = input_dir + "/"+ "temp/"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

#create noise folder for proccesed data
output_dir = input_dir + "/"+"Final Folder/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#loop through the input directory
for file in os.listdir(input_dir):

    # check zip folder inside input directory     
     if file.endswith(".zip"):
        
        # open the zip file in read mode
        with ZipFile (input_dir + "/"+ file,'r') as zip: 
            
            # list all the contents of the zip file
            zip.printdir()
            
            #extract all files inside the zip folder
            zip.extractall(input_dir + "/" + "temp") 
            print('Extraction Done!')
            
            #loop through the unzipped folder called temp folder
            for folder in os.listdir(input_dir + "/" + "temp"):
                
                # print the folder name inside zip folder
                print(f"Folder name : {folder}")
                
                # take the city number from folder name
                city =folder.split('_')[1]
                
                #loop through the folder inside temp folder
                for file in os.listdir(input_dir + "/" + "temp" + "/" + folder):
                    
                    #print the file name inside the folder
                    print (f"File name : {file}")
                    
                    # check if there is geojson file
                    if file.endswith(".geojson"):
                        
                        #split the file name and extension
                        name, ext = os.path.splitext(file)
                        
                        # process only the polygon file, "St_y" contains the polygon file
                        if name == "St_y":
                            
                            # rename the file with city number
                            os.rename(input_dir + "/" + "temp" + "/" + folder + "/" + file, input_dir + "/" + "temp" + "/" + folder + "/" +"n_"+ str(city) + ".geojson")
                            
                            # move the file to a new directory
                            os.replace(input_dir + "/" + "temp" + "/" + folder + "/" +"n_"+ str(city) + ".geojson", input_dir + "/" + "Final Folder" + "/" +"n_"+ str(city) + ".geojson")
                            print("All Process Done")