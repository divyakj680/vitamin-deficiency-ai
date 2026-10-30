# update_toc_lof_lot.py
# Synchronizes TOC, LOF, LOT page numbers and fixes Table 8.3 caption

with open("generate_90_page_report.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix second Table 8.2 to Table 8.3
text = text.replace(
    'add_run(p_cap, "Table 8.2: Comprehensive Multi-Class Diagnostic Performance Breakdown", size=10, bold=True)',
    'add_run(p_cap, "Table 8.3: Comprehensive Multi-Class Diagnostic Performance Breakdown", size=10, bold=True)'
)

# New synchronized initial_toc
new_toc_code = '''    initial_toc = [
        ("-", "Acknowledgement", "-", True),
        ("-", "Abstract", "-", True),
        ("-", "List of Figures", "-", True),
        ("-", "List of Tables", "-", True),
        ("1", "Chapter 1: Introduction", "1", True),
        ("", "    1.1 Overview", "1", False),
        ("", "    1.1.1 Nutritional Epidemiology and Socioeconomic Context", "2", False),
        ("", "    1.2 Objectives", "3", False),
        ("", "    1.3 Scope of the Project", "4", False),
        ("", "    1.4 Applications", "4", False),
        ("", "    1.5 Organization of Report", "5", False),
        ("", "    1.6 Summary", "6", False),
        ("2", "Chapter 2: Problem Identification", "7", True),
        ("", "    2.1 Problem Overview", "7", False),
        ("", "    2.1.1 Biochemical Pathways of Micronutrient Depletion", "8", False),
        ("", "    2.1.2 Clinical Biomarker Thresholds and Differential Diagnosis", "10", False),
        ("", "    2.2 Existing System", "11", False),
        ("", "    2.2.1 Drawbacks of Existing System", "11", False),
        ("", "    2.3 Proposed System", "12", False),
        ("", "    2.3.1 Advantages of Proposed System", "13", False),
        ("", "    2.4 Summary", "14", False),
        ("3", "Chapter 3: Literature Review", "15", True),
        ("", "    3.1 Introduction", "15", False),
        ("", "    3.2 Review of Existing Research (20 Papers)", "16", False),
        ("", "    3.2.21 Algorithmic Synthesis Across Surveyed Works", "35", False),
        ("", "    3.3 Research Gap", "35", False),
        ("", "    3.4 Summary", "37", False),
        ("4", "Chapter 4: System Requirements", "38", True),
        ("", "    4.1 System Overview", "38", False),
        ("", "    4.2 Functional Requirements", "38", False),
        ("", "    4.3 Non-Functional Requirements", "41", False),
        ("", "    4.3.1 Security & Statutory Compliance Specifications", "42", False),
        ("", "    4.4 Hardware Requirements", "43", False),
        ("", "    4.5 Software Requirements", "43", False),
        ("", "    4.6 Relational Data Dictionary Specifications", "44", False),
        ("", "    4.7 Summary", "47", False),
        ("5", "Chapter 5: System Design", "48", True),
        ("", "    5.1 System Design Overview", "48", False),
        ("", "    5.2 System Architecture", "48", False),
        ("", "    5.3 System Modules", "50", False),
        ("", "    5.3.1 Component Decomposition & State Transitions", "50", False),
        ("", "    5.4 UML Diagrams", "51", False),
        ("", "    5.5 Data Flow Diagram (DFD)", "54", False),
        ("", "    5.6 Database Design & Data Dictionary", "55", False),
        ("", "    5.7 Structural Subsystem Interoperability Architecture", "59", False),
        ("", "    5.8 Summary", "60", False),
        ("6", "Chapter 6: System Implementation", "61", True),
        ("", "    6.1 Overview", "61", False),
        ("", "    6.2 Module-wise Implementation", "61", False),
        ("", "    6.3 Two-Stage Image Validation Algorithms", "62", False),
        ("", "    6.3.1 Mathematical Formulations & CNN Complexity", "63", False),
        ("", "    6.4 System Pseudocode", "63", False),
        ("", "    6.5 Mathematical Derivation of Depthwise Separable Convolutions", "64", False),
        ("", "    6.6 Mathematical Principles of INT8 Neural Quantization", "66", False),
        ("", "    6.7 REST API Specifications", "67", False),
        ("", "    6.8 Deployment Architecture", "67", False),
        ("", "    6.9 Security Implementation Details", "69", False),
        ("", "    6.10 Summary", "70", False),
        ("7", "Chapter 7: System Testing", "71", True),
        ("", "    7.1 Overview & Testing Strategy", "71", False),
        ("", "    7.2 Testing Methodologies", "71", False),
        ("", "    7.3 Comprehensive Test Cases (35 Test Cases)", "72", False),
        ("", "    7.4 Extended Stress, Security & Boundary Test Suite", "75", False),
        ("", "    7.5 Test Execution Results & Defect Analysis", "75", False),
        ("", "    7.6 Non-Functional & Stress Testing Observations", "76", False),
        ("", "    7.7 Summary", "78", False),
        ("8", "Chapter 8: Results and Discussion", "79", True),
        ("", "    8.1 Overview & Objectives Achieved", "79", False),
        ("", "    8.2 Objectives Achieved", "79", False),
        ("", "    8.3 User Interface Walkthrough & Screenshots", "80", False),
        ("", "    8.4 Experimental Results & Evaluation Metrics", "81", False),
        ("", "    8.4.1 In-depth Error Distribution Analysis", "82", False),
        ("", "    8.5 Comparison with Existing Systems", "82", False),
        ("", "    8.6 Multi-Class Diagnostic Performance Metrics", "83", False),
        ("", "    8.7 Receiver Operating Characteristic (ROC) Analysis", "83", False),
        ("", "    8.8 Summary", "84", False),
        ("9", "Chapter 9: Conclusion and Future Scope", "85", True),
        ("", "    9.1 Conclusion", "85", False),
        ("", "    9.2 Key Technical and Algorithmic Contributions", "85", False),
        ("", "    9.3 Societal and Public Health Impact", "86", False),
        ("", "    9.4 Ethical Considerations & Regulatory Frameworks", "87", False),
        ("", "    9.5 Recognized System Limitations", "87", False),
        ("", "    9.6 Future Scope & Engineering Roadmap", "87", False),
        ("", "    9.7 Summary", "88", False),
        ("-", "References", "90", True)
    ]'''

# Replace initial_toc block
import re
text = re.sub(r'    initial_toc = \[.*?    \]\n    build_toc\(initial_toc\)', new_toc_code + '\n    build_toc(initial_toc)', text, flags=re.DOTALL)

# New synchronized initial_lof
new_lof_code = '''    initial_lof = [
        ("Figure 5.1", "NutriVision AI Three-Tier System Architecture", "50"),
        ("Figure 5.2", "Complete System Use Case Diagram", "52"),
        ("Figure 5.4", "System Data Flow Diagram (DFD Level 1)", "55"),
        ("Figure 5.3", "Backend Entity-Relationship (ER) Diagram", "59"),
        ("Figure 8.1", "NutriVision AI Landing Page & Hero Section", "80"),
        ("Figure 8.2", "Assessment Wizard - Photo Upload & Quality Gate", "81"),
        ("Figure 8.3", "Nutritional Screening Results & Recommendations", "81")
    ]'''

text = re.sub(r'    initial_lof = \[.*?    \]', new_lof_code, text, flags=re.DOTALL)

# New synchronized initial_lot
new_lot_code = '''    initial_lot = [
        ("Table 2.1", "Clinical Laboratory Thresholds vs Macroscopic Visual Manifestations", "10"),
        ("Table 4.1", "Hardware Requirements Specification", "43"),
        ("Table 4.2", "Software Requirements Specification", "44"),
        ("Table 6.1", "NutriVision AI RESTful API Specification", "66"),
        ("Table 7.1", "Comprehensive System Test Cases (35 Executed Test Cases)", "75"),
        ("Table 7.2", "Extended Stress, Security, and Boundary Verification Matrix", "78"),
        ("Table 8.1", "MobileNetV2 Classification Performance Metrics", "82"),
        ("Table 8.2", "System Comparison with Existing Health/Diet Platforms", "83"),
        ("Table 8.3", "Comprehensive Multi-Class Diagnostic Performance Breakdown", "84")
    ]'''

text = re.sub(r'    initial_lot = \[.*?    \]', new_lot_code, text, flags=re.DOTALL)

with open("generate_90_page_report.py", "w", encoding="utf-8") as f:
    f.write(text)

print("TOC, LOF, LOT successfully synchronized!")
