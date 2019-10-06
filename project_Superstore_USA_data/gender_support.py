import numpy as np
import pandas as pd
import gender_guesser.detector as gender


def split_data_by_gender(_file):
    data = pd.read_excel(_file)
    myColumns = list(data.columns)

    male_data = pd.DataFrame(columns=myColumns)
    female_data = pd.DataFrame(columns=myColumns)
    other_data = pd.DataFrame(columns=myColumns)
    d = gender.Detector()
    A = np.array('')

    print('all index: ', len(data))
    for i in range(0, len(data)):
        print(i)
        full_name = data.iloc[i]['CustomerName']
        name = full_name.split(' ', 1)[0]
        newGender = d.get_gender(name)
        # A = np.append(A, newGender)
        if newGender == 'male':
            temp = data.loc[[i]]
            #male_data = pd.concat([male_data, temp], axis=0)
            male_data = male_data.append(temp, sort=True)
            #print(male_data)
        elif newGender == 'female':
            temp = data.loc[[i]]
            female_data = female_data.append(temp, sort=True)
        else:
            temp = data.loc[[i]]
            other_data = other_data.append(temp, sort=True)

    print('male_data.shape: ', male_data.shape)
    print('female_data.shape: ', female_data.shape)
    print('other_data.shape: ', other_data.shape)
    return male_data, female_data


if __name__ == '__main__':
  _file = "Superstore.xls"
  men, women = split_data_by_gender(_file)
  men.to_excel("men.xlsx")
  women.to_excel("women.xlsx")

  # add column about gender status in ouput file
  _fileNameInput = _file
  _fileNameOutput = "Superstore.xlsx"
  data = pd.read_excel(_fileNameInput)
  
  myColumns = list(data.columns)
  male_data = pd.DataFrame(columns=myColumns)
  female_data = pd.DataFrame(columns=myColumns)
  other_data = pd.DataFrame(columns=myColumns)
  _customerName = data['CustomerName'].values
  d = gender.Detector()
  A = np.array([])
  
  for i in range(0, len(data)):
      full_name = data.iloc[i]['CustomerName']
      name = full_name.split(' ', 1)[0]
      newGender = d.get_gender(name)
      #A = np.append(A, newGender)
      if newGender == 'male':
          A = np.append(A, 1)
      elif newGender == 'female':
          A = np.append(A, 0)
      else:
          A = np.append(A, -1)

  print(len(A))
  A = pd.DataFrame(pd.array(A))
  data = data.join(A)
  data.to_excel(_fileNameOutput)
  # print(data)
