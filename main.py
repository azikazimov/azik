# #authorization system by azik
#
# online_users = ['admin', 'john', 'steve', 'elen']
# ban_users = ['john', 'sarah', 'andre']
#
# if online_users:
#     for user in online_users:
#         if user in ban_users:
#             print('[error] : ' + user.title() + ' is banned')
#         elif user == 'admin':
#             print('[atention] : ' + user )
#         else:
#             print('[aut] : ' + user.title())
#
# print('\n')
#
# dict = {'name' : 'gregory', 'surname' : 'shanin'}
# print(dict['name'].title())
# print(dict['surname'].title())
# print(dict)
#
# langus = {
#     'john' : 'python',
#     'erick' : 'c',
#     'alien' : 'ruby',
#     'steve' : 'java',
#     'abraham' : 'python'
# }
#
# for name, langs in sorted(langus.items()): #sorted() позволяет вывести список по алфавиту, по возраст.
#     print('\nName : ' + name.title())
#     print('Language : ' + langs.title())
#
# print('##################')
#
# for name in langus.keys():
#     print('Name : ' + name.title())
#
# print('##################')
#
# for lang in set(langus.values()): #set() позволяет оставить только уникальные значения
#     print('Language : ' + lang.title())
#
#
# # alien_0 = {'color' : 'green', 'points' : 5}
# # alien_1 = {'color' : 'yellow', 'points' : 10}
# # alien_2 = {'color' : 'red', 'points' : 15}
# #
# # alien_list = [alien_0, alien_1, alien_2]
# # print(alien_list)
# print('\n')
#
# empty_alien = []
#
# for aliens in range(0, 30):
#     new_alien = {'color' : 'yellow', 'points' : 10}
#     empty_alien.append(new_alien)
#
# for k in empty_alien[:5]:
#     print(k)
#
# print('...')
# print('List lenght is ' + str(len(empty_alien)))
#
# print('\n')
#
# per_lang = {
#     'john' : ['python', 'ruby'],
#     'steve' : ['c'],
#     'elen' : ['c++', 'go']
# }
#
# for name, language in sorted(per_lang.items()):
#     if len(language) == 1:
#         for lang in language:
#             print(name.title() + "'s favorite language is " + lang.title())
#     else:
#         print(name.title() + "'s favorite language is : ")
#         for lang in language:
#             print('\t' + lang.title())


class Dog():
    def __init__(self, name, age):
        """Init by age and name"""
        self.name = name
        self.age = age

my_dog = Dog('steve', 4)
print('My ' + str(my_dog.age) + ' years old dog name is ' + my_dog.name.title())
