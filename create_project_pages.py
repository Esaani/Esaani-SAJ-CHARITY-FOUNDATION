import os
import re

source = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file\project-single.html"
dest_food = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file\project-single-food.html"
dest_hyg = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file\project-single-hygiene.html"

# Common logic
with open(source, 'r', encoding='utf-8') as f:
    content = f.read()

# ================================
# 1. Food for Orphanages
# ================================
food_content = content
food_content = food_content.replace("School Books Support Project for Orphanage and Needy Students", "Food for Orphanages")
food_content = food_content.replace(
    "The School Books Support Project is an educational initiative by the SAJ Foundation aimed at supporting orphanage children and students from underprivileged families in Ghana.",
    "The Food for Orphanages initiative is a dedicated program by the SAJ Foundation to provide nutritional support and essential meals to vulnerable children in Ghana."
)
food_content = food_content.replace(
    "The project focuses on providing essential learning materials such as school books, exercise books, stationery, and other educational resources to help students continue their education successfully. Many children in orphanages and low-income communities face challenges accessing basic learning materials. This project seeks to reduce that gap by ensuring that every child has the tools they need to learn, grow, and build a better future.",
    "Providing nutritious meals and essential food supplies to orphanage homes and vulnerable children. This initiative ensures that children receive proper nutrition while creating a caring and supportive environment, helping them grow healthy and strong."
)
food_content = food_content.replace("Education Support", "Food & Health")

# Goals mapping
food_content = food_content.replace("Provide school books and learning materials to orphanage children and needy students", "Provide regular nutritious meals and groceries to orphanage homes")
food_content = food_content.replace("Support access to quality education for disadvantaged communities", "Ensure vulnerable children receive a balanced diet and proper nutrition")
food_content = food_content.replace("Encourage academic development and confidence among young learners", "Alleviate hunger and malnutrition in disadvantaged communities")
food_content = food_content.replace("Promote equal educational opportunities for all children", "Create a healthy, supportive, and caring environment for orphans")

# Activities mapping
food_content = food_content.replace("Distribution of textbooks and exercise books", "Frequent meal distributions and grocery drop-offs")
food_content = food_content.replace("Donation of school bags and stationery", "Providing bulk food supplies (rice, oil, provisions) to orphanages")
food_content = food_content.replace("Educational encouragement and mentorship", "Nutritional assessments and health check-ins")
food_content = food_content.replace("Community engagement with volunteers", "Volunteer cooking and serving days at the homes")

# Impact & Help mapping
food_content = food_content.replace(
    "Through this initiative, the SAJ Foundation aims to empower children with the resources they need to succeed in school and in life. Education remains one of the most powerful tools for breaking the cycle of poverty and building stronger communities.",
    "Through this initiative, the SAJ Foundation works to eradicate childhood hunger in the communities we serve. Proper nutrition is fundamental to a child's cognitive and physical development, and ensuring no child goes to bed hungry is our utmost priority."
)
food_content = food_content.replace(
    "With the support of donors, volunteers, and partners, the project will continue every year to reach more students and orphanages across Ghana.",
    "With your continued support, we supply hundreds of meals weekly, easing the burden on orphanage caretakers."
)

food_content = food_content.replace("Donating books and educational materials", "Donating non-perishable food items and groceries")
food_content = food_content.replace("Sponsoring a student's school supplies", "Sponsoring daily meals for an entire orphanage")
food_content = food_content.replace("Volunteering in distribution and mentorship programs", "Volunteering during food distribution drives")
food_content = food_content.replace("Supporting the project through financial donations", "Contributing financially to our food fund")
food_content = food_content.replace(
    "Together, we can ensure that every child has the opportunity to learn, grow, and achieve their dreams.",
    "Together, we can ensure that every child receives the nutrition they need to thrive."
)
food_content = food_content.replace('alt="School Books Support"', 'alt="Food for Orphanages"')


with open(dest_food, 'w', encoding='utf-8') as f:
    f.write(food_content)
    
print("Created project-single-food.html")


# ================================
# 2. Menstrual Hygiene Support
# ================================
hyg_content = content
hyg_content = hyg_content.replace("School Books Support Project for Orphanage and Needy Students", "Menstrual Hygiene Support")
hyg_content = hyg_content.replace(
    "The School Books Support Project is an educational initiative by the SAJ Foundation aimed at supporting orphanage children and students from underprivileged families in Ghana.",
    "The Menstrual Hygiene Support program is a health and empowerment initiative by the SAJ Foundation aimed at young girls in underprivileged communities across Ghana."
)
hyg_content = hyg_content.replace(
    "The project focuses on providing essential learning materials such as school books, exercise books, stationery, and other educational resources to help students continue their education successfully. Many children in orphanages and low-income communities face challenges accessing basic learning materials. This project seeks to reduce that gap by ensuring that every child has the tools they need to learn, grow, and build a better future.",
    "Promoting health and dignity for young girls by providing menstrual hygiene products, education, and awareness. The program helps girls stay confident, healthy, and able to continue their education without interruption due to a lack of basic sanitary supplies."
)
hyg_content = hyg_content.replace("Education Support", "Health & Hygiene")

# Goals mapping
hyg_content = hyg_content.replace("Provide school books and learning materials to orphanage children and needy students", "Provide sanitary pads and hygiene kits to young girls")
hyg_content = hyg_content.replace("Support access to quality education for disadvantaged communities", "Eradicate period poverty and the stigma associated with menstruation")
hyg_content = hyg_content.replace("Encourage academic development and confidence among young learners", "Educate communities on safe reproductive and menstrual health practices")
hyg_content = hyg_content.replace("Promote equal educational opportunities for all children", "Ensure girls do not miss school days due to lack of sanitary products")

# Activities mapping
hyg_content = hyg_content.replace("Distribution of textbooks and exercise books", "Distribution of sanitary pads and hygiene kits")
hyg_content = hyg_content.replace("Donation of school bags and stationery", "Organizing health education and awareness workshops")
hyg_content = hyg_content.replace("Educational encouragement and mentorship", "Building safe spaces for girls to discuss reproductive health")
hyg_content = hyg_content.replace("Community engagement with volunteers", "Partnering with schools to provide emergency hygiene supplies")

# Impact & Help mapping
hyg_content = hyg_content.replace(
    "Through this initiative, the SAJ Foundation aims to empower children with the resources they need to succeed in school and in life. Education remains one of the most powerful tools for breaking the cycle of poverty and building stronger communities.",
    "Through this initiative, the SAJ Foundation empowers young women by restoring their dignity and confidence. We believe that a natural biological process should never be a barrier to a girl's education or success."
)
hyg_content = hyg_content.replace(
    "With the support of donors, volunteers, and partners, the project will continue every year to reach more students and orphanages across Ghana.",
    "Our goal is to reach thousands of young girls annually, providing continuous support and education."
)

hyg_content = hyg_content.replace("Donating books and educational materials", "Donating sanitary pads, soap, and hygiene products")
hyg_content = hyg_content.replace("Sponsoring a student's school supplies", "Sponsoring a girl's hygiene needs for an entire year")
hyg_content = hyg_content.replace("Volunteering in distribution and mentorship programs", "Volunteering as a health educator or mentor")
hyg_content = hyg_content.replace("Supporting the project through financial donations", "Supporting the project through financial donations to bulk-purchase kits")
hyg_content = hyg_content.replace(
    "Together, we can ensure that every child has the opportunity to learn, grow, and achieve their dreams.",
    "Together, we can uplift young girls and support their journey to a confident and healthy future."
)

hyg_content = hyg_content.replace('alt="School Books Support"', 'alt="Menstrual Hygiene Support"')


with open(dest_hyg, 'w', encoding='utf-8') as f:
    f.write(hyg_content)
    
print("Created project-single-hygiene.html")
