
class tea:

    def print(self):
        print("Name: " + self.name)
        print("Category: " + self.category)
        print("Feeling: " + self.feeling)
        print("Diseases: " + str.join(", ", self.diseases))
        print("Regions: " + str.join(", ", self.regions))
        print("IsRare: " + self.rare)
        print("HasCaffeine: " + self.caffeine)

    def getFormattedRegions(self):
        return ', '.join(self.regions)

    def getFormattedDiseases(self):
        return ', '.join(self.diseases)

    def getFormattedCaffeine(self):
        if self.caffeine:
            return 'Contains Caffeine'
        else:
            return "Doesn't Contain Caffeine"

    def __init__(self, name:str, category:str, feeling:str, diseases:list, regions:list, rare:bool, caffeine:bool, description:str, link:str, pubmed:str):

        self.name = name
        self.category = category
        self.feeling = feeling
        self.diseases = diseases
        self.regions = regions
        self.rare = rare
        self.caffeine = caffeine
        self.imageName = name + ".png"
        self.description = description
        self.link = link
        self.pubmed = pubmed


