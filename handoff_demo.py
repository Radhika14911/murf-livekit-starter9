from exam_specialist import ExamSpecialist
from career_specialist import CareerSpecialist

user_name = "Radhika"

user_query = input("User: ")

if "exam" in user_query.lower() or "stress" in user_query.lower():

    print("\nMain Agent:")
    print("I will connect you to our Exam Support Specialist.\n")

    try:
        specialist = ExamSpecialist()

        print("Exam Support Specialist:")
        print(specialist.respond(user_query, user_name))

    except:
        print("Exam Specialist unavailable.")
        print("Main Agent will continue assisting you.")

elif "career" in user_query.lower() or \
     "resume" in user_query.lower() or \
     "linkedin" in user_query.lower() or \
     "internship" in user_query.lower() or \
     "interview" in user_query.lower():

    print("\nMain Agent:")
    print("I will connect you to our Career Specialist.\n")

    try:
        specialist = CareerSpecialist()

        print("Career Specialist:")
        print(specialist.respond(user_query, user_name))

    except:
        print("Career Specialist unavailable.")
        print("Main Agent will continue assisting you.")

else:

    print("\nMain Agent:")
    print("I can answer that myself.")
    print("Shiksha Saathi is an AI-powered educational assistant designed to support students throughout their academic and "
          "career journey.")
    print("It provides personalized guidance for exam preparation, study planning, career development, "
          "internships, and interview readiness through intelligent agent handoffs.")
