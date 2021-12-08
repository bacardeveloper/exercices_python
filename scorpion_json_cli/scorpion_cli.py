import json

# class CRUD json
class Crud_Json:
    def __init__(self):
        pass

    def chargement_data(self, data_json):
        with open(data_json) as fichier_json:
            return json.load(fichier_json)
    
    def recuperer_un_item_dans_json(self, json, id):
        for element in json:
            ''
        

# fonction princpale
def main():
    crud_json = Crud_Json()
    input_name_json = input('entrez nom du fichier json : ')
    input_id = input('entrez id (convertit en string) : ')
    
    json_file_recuperer = crud_json.chargement_data(input_name_json)
    print(json_file_recuperer['date_created'])
    print(type(input_id))
    
    crud_json.recuperer_un_item_dans_json(json_file_recuperer, input_id)
    # print(element_recuperer)
    
    
    
if __name__ == "__main__":
    main()
