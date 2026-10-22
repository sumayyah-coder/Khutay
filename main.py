def main():
     routes = {
     "ar": [
        "مسار المشي الأول",
        "مسار المشي الثاني",
        "مسار المشي الثالث"
     ],
     "en": [
        "Walking Route 1",
        "Walking Route 2",
        "Walking Route 3"
     ]
     }
     print("Welcome to Khutay | مرحبًا بك في خُطاي")
     print("1. العربية")
     print("2. English")

#Python
     language = input("Choose your language / اختر لغتك: ")

     if language == "1":
         print("مرحبًا بك في خُطاي!")
         print("اكتشف مسارات المشي في المدينة المنورة.")
         print("كل خطوة لها طريق.")
         print("مسارات المشي المتاحة:")
         for route in routes["ar"]:
             print(route)

     elif language == "2":
         print("Welcome to Khutay!")
         print("Discover walking routes in Madinah.")
         print("Every step has a path.")
         print("Available walking routes:")
         for route in routes["en"]:
             print(route)

     else:
         print("اختيار غير صحيح | Invalid choice")
if __name__ == "__main__":
     main()