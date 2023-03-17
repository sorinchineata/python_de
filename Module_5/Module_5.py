from datetime import datetime
import sys

def main():
    option = ''
    while(option != "exit"):
        option = input(
            "\nOptions:\n1 to add News\n2 to add Private ad\n3 to Add a job offer.\nexit: If you'd like to exit\n\nSelect your option:")
        if  option =='1':
            News().to_file()
        elif option == '2':
            Private_ad().to_file()
        elif option == '3':
            Job().to_file()
        elif option == 'exit':
            print('\nYour choice was to exit the program. Goodbye!')
            sys.exit()
        else:
            print('\nThat is not a valid option. Please, try again!\n')

class Article:
    def title(self):
        classtitle = self.__class__.__name__
        return f"{classtitle}"
    def __init__(self):
        self.text = input(f"Enter {self.__class__.__name__} article body: ")
    def to_file(self):
        with open('/Users/sorinchineata/Documents/GitHub/python_de/Module_5/NewsFeed.txt', 'a', encoding="utf-8") as f:
            f.write(self.article_body + '\n' + '\n')
        print(self.__class__.__name__ + ' added')

class News(Article):
    def __init__(self):
        super().__init__()
        city = input("Enter the city: ")
        now = datetime.now()
        publish_date = now.strftime("%H:%M %d-%m-%Y")
        self.article_body = self.title() + '\n' + self.text + '\n' + city + ', ' + publish_date


class Private_ad(Article):
    def __init__(self):
        super().__init__()
        self.tries=0
        self.date_to = input("Enter the final date of the add in DD/MM/YYYY format: ")
        self.is_valid_date()
        self.date_from = datetime.now()
        active_days = self.date_to - self.date_from
        if active_days.days+1 < 0:
            print(f"This ad expired.")
            sys.exit()
        elif active_days.days+1 == 0:
            self.article_body = self.title() + '\n' + self.text + '\n' \
                        + f'Active until: ' + str(self.date_to.strftime('%d/%m/%Y')) \
                        + f'\nThis ad will expire today.'
        elif active_days.days+1 == 1:
            self.article_body = self.title() + '\n' + self.text + '\n' \
                        + f'Active until: ' + str(self.date_to.strftime('%d/%m/%Y')) \
                        + f'\nOne day left'
        else:
            self.article_body = self.title() + '\n' + self.text + '\n' \
                        + f'Active until: ' + str(self.date_to.strftime('%d/%m/%Y')) \
                        + f'\n{active_days.days+1} days left'

    def is_valid_date(self):
        self.tries += 1
        try: 
            self.date_to = datetime.strptime(self.date_to, '%d/%m/%Y')
        except ValueError:
            if self.tries < 3:
                print('\nYou entered an invalid date. You have ' + str( 3-self.tries) + ' attempts left.\n')
                self.date_to = input('Enter the final date of the add in DD/MM/YYYY format: ')
                self.is_valid_date()
            else:
                print('\nYou have exceeded the number of attempts. Goodbye!')
                sys.exit()


class Job(Article):
    def __init__(self):
        super().__init__()
        self.tries=0
        self.company = input('Company name: ')
        self.city_name = input('City name: ')
        self.anual_salary = input('Anual Salary: ')
        self.is_valid_salary()
        self.article_body = self.title() + "\n" \
                      + f"Company:{self.company}" + "\n" f"City:{self.city_name}" \
                      + "\nJob description:" + self.text + "\n" f"Anual salary: {self.anual_salary}"


    def is_valid_salary(self):
        self.tries += 1
        try: 
            self.anual_salary = int(self.anual_salary)
        except ValueError:
            if self.tries < 3:
                print('\nYou entered an invalid salary. You have ' + str( 3-self.tries) + ' attempts left.\n')
                self.anual_salary = input('Anual Salary: ')
                self.is_valid_salary()
            else:
                print('\nYou have exceeded the number of attempts. Goodbye!')
                sys.exit()

main() # run the program


