import unittest
import requests

class TestApi(unittest.TestCase):
    # Dont forget to change the URL for the Running on API URL #
    URL_city = "http://192.168.1.12:5000/city"
    URL_resident = "http://192.168.1.12:5000/resident"
    
    # I dont know much about Unit Test
    # I set all the URL IDs to 1
    # I think that is not the smart way to do it
    # So please if any error apper change the IDs to the correct ones
    # sorry :) 
    
    # ---------------- City Unit Tests ------------------------------------------------------
    
    # Testing the create of a city
    create_data = {
        'name': 'Budapest',
        'area': 525.2
    }    
    def test_create_city(self):
        response = requests.post(self.URL_city, json=self.create_data)
        self.assertEqual(response.status_code, 201)
        
        print("City Create Test - OK")
    
    # Testing the read of all cities
    def test_get_all_citys(self):
        response = requests.get(self.URL_city)
        self.assertEqual(response.status_code, 200)
        print("City Read All Test - OK")
    
    # Testing the read of a specific city by id
    def test_get_city_by_id(self):
        response = requests.get(self.URL_city +'/1')
        self.assertEqual(response.status_code, 200)
        print("City Read by ID Test - OK")
    
    # Testing the update of a city by id
    update_data = {
        'name': 'Budapest',
        'area': 525.2
    }    
    def test_update_city_by_id(self):
        response = requests.put(self.URL_city +'/1', json=self.update_data)
        self.assertEqual(response.status_code, 200)
        
        print("City Update Test - OK")
    
    # Testing the delete of a city by id    
    def test_delete_city_by_id(self):
        response = requests.delete(self.URL_city +'/1')
        self.assertEqual(response.status_code, 200)
        print("City Delete Test - OK")
    
    # -------------- Resident Unit Tests ----------------------------------------------------
        
    # Testing the create of a resident
    create_resident_data = {
        'firstName': 'Guilherme',
        'lastName': 'Fiorot',
        'placeBirth': 'Brazil',
        'dateBirth': '2001-05-02',
        'email': 'guilherme@test.com',
        'residentPlace': 'Budapest'
    }    
    def test_create_resident(self):
        response = requests.post(self.URL_resident, json=self.create_resident_data)
        self.assertEqual(response.status_code, 201)
        
        print("Resident Create Test - OK")
    
    # Testing the read of all residents
    def test_get_all_resident(self):
        response = requests.get(self.URL_resident)
        self.assertEqual(response.status_code, 200)
        print("Resident Read All Test - OK")
    
    # Testing the read of a specific resident by id
    def test_get_resident_by_id(self):
        response = requests.get(self.URL_resident +'/1')
        self.assertEqual(response.status_code, 200)
        print("Resident Read by ID Test - OK")
    
    # Testing the update of a resident by id
    update_resident_data =  {
        'email': 'guilhermefiorot@test.com.br'
    }    
    def test_update_resident_by_id(self):
        response = requests.put(self.URL_resident +'/1', json=self.update_resident_data)
        self.assertEqual(response.status_code, 200)
        print("Resident Update Test - OK")
    
    # Testing the delete of a resident by id    
    def test_delete_resident_by_id(self):
        response = requests.delete(self.URL_resident +'/1')
        self.assertEqual(response.status_code, 200)
        print("Resident Delete Test - OK")

if __name__ == "__main__":
    tester = TestApi()
    tester.test_create_city
    tester.test_get_all_citys
    tester.test_get_city_id
    tester.test_update_city_by_id
    tester.test_delete_city_by_id
    tester.test_create_resident