import os
import re

filepath = r"C:\Users\esaan\Downloads\Saani Eliasu\non-profit-charity-html-template-2024-01-13-04-19-50-utc\sadaka-buyer-file\project-single.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Metadata
content = re.sub(r'<h5>Project Date:</h5>\s*2022 - 2023', '<h5>Project Date:</h5>\n                                    Every Year', content)
content = re.sub(r'<h5>Categories:</h5>\s*Food &amp; Health', '<h5>Category:</h5>\n                                    Education Support', content)
content = re.sub(r'<h5>Categories:</h5>\s*Food & Health', '<h5>Category:</h5>\n                                    Education Support', content)
content = re.sub(r'<h5>Location:</h5>\s*South Africa', '<h5>Location:</h5>\n                                    Ghana', content)
content = re.sub(r'<h5>Client:</h5>\s*Kids Help', '<h5>Organizer:</h5>\n                                    SAJ Foundation', content)


# 2. Extract and rebuild the content block
start_idx = content.find('<h3 class="fs-30 mb-30">Aiding the Homeless Population in South Africa</h3>')
end_str = 'eros sed istincidunt augue ac ante rutrum sed the is sodales augue consequat..</p>'
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    end_idx += len(end_str)
    
    svg_icon = """<svg class="me-1" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_20_5)"><path d="M17.4853 2.46073C17.2205 2.19547 16.7909 2.19502 16.5261 2.4596L8.38765 10.5765L5.45133 7.38742C5.1976 7.112 4.76863 7.09415 4.49276 7.34783C4.2171 7.60156 4.19945 8.03074 4.45317 8.3064L7.86776 12.0147C7.92961 12.082 8.00443 12.136 8.08771 12.1736C8.17099 12.2111 8.26101 12.2315 8.35235 12.2334C8.35731 12.2336 8.36209 12.2336 8.36683 12.2336C8.54636 12.2335 8.71855 12.1624 8.84577 12.0357L17.484 3.42018C17.7494 3.15563 17.7499 2.72598 17.4853 2.46073Z" fill="#F74F22"></path><path d="M17.3216 8.32159C16.9469 8.32159 16.6432 8.62527 16.6432 9C16.6432 13.2146 13.2146 16.6432 9 16.6432C4.78561 16.6432 1.35679 13.2146 1.35679 9C1.35679 4.78561 4.78561 1.35679 9 1.35679C9.3747 1.35679 9.67841 1.05311 9.67841 0.67841C9.67841 0.30368 9.3747 0 9 0C4.03734 0 0 4.03734 0 9C0 13.9624 4.03734 18 9 18C13.9624 18 18 13.9624 18 9C18 8.6253 17.6963 8.32159 17.3216 8.32159Z" fill="#F74F22"></path></g><defs><clipPath><rect width="18" height="18" fill="white"></rect></clipPath></defs></svg>"""
    
    new_html = f"""<h3 class="fs-30 mb-30">School Books Support Project for Orphanage and Needy Students</h3>
                    <h4 class="mb-10">Project Overview</h4>
                    <p class="mb-20">The School Books Support Project is an educational initiative by the SAJ Foundation aimed at supporting orphanage children and students from underprivileged families in Ghana.</p>
                    <p class="mb-40">The project focuses on providing essential learning materials such as school books, exercise books, stationery, and other educational resources to help students continue their education successfully. Many children in orphanages and low-income communities face challenges accessing basic learning materials. This project seeks to reduce that gap by ensuring that every child has the tools they need to learn, grow, and build a better future.</p>
                    <div class="row g-4 align-items-center">
                        <div class="col-lg-5">
                            <h3 class="fs-30 mb-20">Project Goals</h3>
                            <p>The initiative is designed to:</p>
                            <ul class="mb-30" style="list-style-type: disc; padding-left: 20px;">
                                <li>Provide school books and learning materials to orphanage children and needy students</li>
                                <li>Support access to quality education for disadvantaged communities</li>
                                <li>Encourage academic development and confidence among young learners</li>
                                <li>Promote equal educational opportunities for all children</li>
                            </ul>
                            
                            <h3 class="fs-24 mb-15">Key Activities</h3>
                            <p>The project includes several important activities:</p>
                            <div class="row mt-20">
                                <div class="col-12 mb-15">
                                    <h6 class="fs-14 fw-bold">
                                        {svg_icon}
                                        Distribution of textbooks and exercise books
                                    </h6>
                                </div>
                                <div class="col-12 mb-15">
                                    <h6 class="fs-14 fw-bold">
                                        {svg_icon}
                                        Donation of school bags and stationery
                                    </h6>
                                </div>
                                <div class="col-12 mb-15">
                                    <h6 class="fs-14 fw-bold">
                                        {svg_icon}
                                        Educational encouragement and mentorship
                                    </h6>
                                </div>
                                <div class="col-12 mb-15">
                                    <h6 class="fs-14 fw-bold">
                                        {svg_icon}
                                        Community engagement with volunteers
                                    </h6>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-7">
                            <div class="row g-4">
                                <div class="col-sm-6">
                                    <div class="image">
                                        <img src="assets/images/project/project-single-sm1.jpg" alt="School Books Support">
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="image">
                                        <img src="assets/images/project/project-single-sm2.jpg" alt="School Books Support">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="mt-40">
                        <h3 class="fs-30 mb-20">Community Impact</h3>
                        <p class="mb-20">Through this initiative, the SAJ Foundation aims to empower children with the resources they need to succeed in school and in life. Education remains one of the most powerful tools for breaking the cycle of poverty and building stronger communities.</p>
                        <p class="mb-40">With the support of donors, volunteers, and partners, the project will continue every year to reach more students and orphanages across Ghana.</p>

                        <h3 class="fs-30 mb-20">How You Can Help</h3>
                        <p class="mb-10">Supporters can contribute by:</p>
                        <ul class="mb-20" style="list-style-type: disc; padding-left: 20px;">
                            <li>Donating books and educational materials</li>
                            <li>Sponsoring a student's school supplies</li>
                            <li>Volunteering in distribution and mentorship programs</li>
                            <li>Supporting the project through financial donations</li>
                        </ul>
                        <p><strong>Together, we can ensure that every child has the opportunity to learn, grow, and achieve their dreams.</strong></p>
                    </div>"""
    content = content[:start_idx] + new_html + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Project Single Update successful.")
else:
    print("Could not find replacement boundaries in HTML.")
