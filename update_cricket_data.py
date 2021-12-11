import os
import json

folder = "D:/Jupyter/odis_json"

def load_data(folder):

    for file in os.listdir(folder):
        if file.endswith(".json"):
            print(file)
            file_path = folder + "/"+ file
            f = open(f"{file_path}", "r")
            data = json.load(f)

            update_info(data)
            update_innings(data)
            delete_filed(data)
            save_json(data,file)


def update_info(data):
    try:
        try:
        # flat city value as vanue
            city = data['info']['city']
        # update info 
            data.update({'City': city})
        except:
            pass 
        data.update({'Date': data['info']['dates']})
        data.update({'Match_Type': data['info']['match_type']})
        try:
            data.update({'Winner':data['info']['outcome']['winner']})
            data.update({'Won_By':key for key in data['info']['outcome']['by'].keys()})
            if "wickets" in data['info']['outcome']['by']:
                data.update({'Winning_value':data['info']['outcome']['by']['wickets']})
            else:
                data['info']['outcome']['by']['runs']
        except:
            pass
        try:
            data.update({'Player_of_Match':data['info']['player_of_match']})
        except:
            pass
        data.update({'Venue':data['info']['venue']})
        data.update({'Players':data['info']['players']})
        data.update({'Team1':data['info']['teams'][0]})
        data.update({'Team2':data['info']['teams'][1]})
    except:
        pass


# update innings
def update_innings(data):
    
    for i in range(len(data['innings'])):
        for over in range(len(data['innings'][i]['overs'])):
            for delivery in range(len(data['innings'][i]['overs'][over]['deliveries'])):
                team = data['innings'][i]['team']
                ball = delivery + 1
                over = data['innings'][i]['overs'][over]['over']
                name = team +'_'+ str(over) + f'.{ball}'

                data['innings'][i]['overs'][over]["deliveries"][delivery].update({'Team':team})
                data['innings'][i]['overs'][over]["deliveries"][delivery].update({'Over':over})
                data['innings'][i]['overs'][over]["deliveries"][delivery].update({'Ball':ball})
                value = data['innings'][i]['overs'][over]["deliveries"][delivery]
                data.update({name: value})



def delete_filed(data):
    #delete innings
    del data['innings']

    #delete info
    del data['info']
    
    #delete meta
    del data['meta']


#save file
def save_json(data,file):
    output_dir = 'D:/Jupyter/odis_json/updated'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

   
    # save the output
    with open('updated'+'/'+'updated'+f'{file}'+'.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    
    load_data(folder)
  
