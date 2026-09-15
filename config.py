"""
Central place for all your portfolio content.
Edit the values below - the pages read from here, so you never
need to touch page layout code just to update your info.
"""

PROFILE = {
    "name": "Samiha Tanjeem",
    "title": "Data Analyst",
    "tagline": "Small talk isn't my thing, but data storytelling is!<br>I run on milk tea and curiosity to get there.",
    "bio": (
        "I'm a Business Analytics graduate from East Texas A&M University "
        "(GPA 3.90). During my internship at PRYPCO, I worked through real "
        "buyer and seller interviews from the Dubai real estate market to map "
        "out customer journeys and flag gaps in the product. At Praava Health, "
        "I was on the marketing side, digging into campaign data and dashboards "
        "that helped grow brand recognition by 27%. Outside of internships, I "
        "like building my own projects to keep learning. I've done machine "
        "learning and regression modeling projects, from predicting U.S. stock "
        "returns off SEC filings to analyzing fast-food sales data. I mostly "
        "work in Python, R, SQL, and Tableau."
    ),
    "location": "Austin, TX",
    "email": "samihatanjeem@gmail.com",
    "phone": "(737) 288-4846",
    "resume_path": "assets/resume.pdf",
    "profile_image": "assets/profile.jpg",
    "profile_cutout_image": "assets/profile-cutout.png",
}

SOCIAL_LINKS = {
    "GitHub": "https://github.com/samihatanjeem",
    "LinkedIn": "https://linkedin.com/in/samihatanjeem/",
    "Email": f"https://mail.google.com/mail/?view=cm&fs=1&to={PROFILE['email']}",
}

PROJECTS = [
    {
        "title": "US Stocks Predictive Analysis",
        "date": "Feb 2026",
        "description": (
            "Built and compared 5 regression models in R: pooled OLS with HC3 "
            "robust standard errors, a single-variable ROA baseline, and three "
            "firm-size-stratified models on a self-engineered panel dataset "
            "restructured from 1M+ raw SEC XBRL rows, with 7 engineered financial "
            "ratios and full multicollinearity, heteroskedasticity, and "
            "autocorrelation diagnostics."
        ),
        "image": "https://github.com/user-attachments/assets/d1a35682-e939-4262-ae06-9ef85e9afb87",
        "bullets": [
            "Cleaned SEC XBRL filings from 12,129 companies down to a validated "
            "panel of 279 firm-year observations across 182 firms, engineering "
            "7 financial ratios (ROA, ROE, debt ratio, asset turnover, and more).",
            "Built OLS regression models reaching R² = 0.673, finding current-year "
            "ROA the strongest predictor of next-year performance (β = 1.261) and "
            "debt ratio a consistent drag on it (β = −0.619) across firm sizes.",
            "Ran full diagnostics (multicollinearity, heteroskedasticity, "
            "autocorrelation) and found the simpler single-variable baseline "
            "actually beat the full 7-predictor model on holdout data — a real "
            "lesson in not over-fitting with limited observations.",
        ],
        "tags": ["R", "dplyr", "tidyr", "ggplot2", "sandwich", "lmtest", "corrplot"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/U.S-Stocks-Predictive-Analysis",
    },
    {
        "title": "Fast Food Giants EDA & Sales Regression",
        "date": "Jan 2025",
        "description": (
            "Performed exploratory data analysis and multivariate regression on "
            "U.S. fast-food market data to predict total sales and find key "
            "relationships among store count, unit sales, and revenue."
        ),
        "image": "https://github.com/user-attachments/assets/bd953db6-cb6b-4a80-86ce-7adf7ff65576",
        "bullets": [
            "Analyzed systemwide sales across the top 50 U.S. fast-food chains, "
            "finding store count and systemwide sales correlated at r ≈ 0.71.",
            "Built a multivariate regression (store count + avg. unit sales → "
            "total sales) reaching R² = 0.64, using backward elimination to "
            "select features and correlation heatmaps to guide the analysis.",
            "Flagged Chick-fil-A as a standout outlier — high systemwide revenue "
            "despite running far fewer locations than its closest competitors.",
        ],
        "tags": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/Fast-Food_served_with_Regression",
    },
    {
        "title": "Python ML Analytics Workspace",
        "date": "May 2024",
        "description": (
            "Built a menu-driven Python and machine learning workspace for data "
            "cleaning, visualization, exploratory analysis, and predictive "
            "modeling with linear regression and feature engineering."
        ),
        "image": "https://github.com/user-attachments/assets/ee080062-b646-42eb-9e55-193cd7892347",
        "bullets": [
            "Built a 15-notebook Python workspace spanning the full workflow: "
            "data cleaning, EDA, visualization, and regression modeling.",
            "Ran a salary-prediction exercise testing technical, communication, "
            "and leadership scores as predictors — a hands-on lesson in reading "
            "regression output honestly when a feature doesn't explain the "
            "outcome, rather than forcing a fit.",
            "Built a second mini-project covering outlier detection and a full "
            "data-cleaning pipeline end to end.",
        ],
        "tags": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/Python-ML-Analytics-Workspace",
    },
    {
        "title": "MTCars-Titanic-R-Linear-Regression",
        "date": "May 2024",
        "description": (
            "Built multiple linear and logistic regression models in R with "
            "diagnostics, performance evaluation, and visualization to interpret "
            "predictors of car fuel efficiency and Titanic passenger survival "
            "across genders and classes."
        ),
        "image": "https://github.com/user-attachments/assets/bf676880-17db-4fa3-9822-99eeea0e9eef",
        "bullets": [
            "Modeled car fuel efficiency in R, finding vehicle weight the "
            "dominant factor (−4.36 mpg per unit, p < 0.001) while horsepower "
            "and quarter-mile time weren't statistically significant — the "
            "model explained 83% of variance (Adj. R² = 0.8171).",
            "Built a logistic regression on Titanic survival: sex was the "
            "strongest predictor (women had ~11x higher odds of survival), with "
            "class and age also shaping outcomes.",
            "Evaluated the classifier with a confusion matrix and ROC curve, "
            "reaching ~77% accuracy with good discrimination.",
        ],
        "tags": ["R", "ggplot2", "caret", "lm", "glm", "pROC"],
        "demo_url": "",
        "repo_url": "https://github.com/samihatanjeem/MTCars-Titanic-R-Linear-Regression",
    },
]

SKILLS = {
    "Programming Languages": ["Python", "R", "Spark", "SQL", "Java"],
    "Data Analysis & Visualization": [
        "Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Plotly", "PySpark",
        "Excel", "IBM SPSS", "STATA", "Power BI", "Tableau",
    ],
    "Developer Tools & Platforms": [
        "MS Visual Studio", "MS SQL Server", "Git", "GitHub", "Docker", "VS Code",
        "Jupyter", "SQL Workbench", "AWS", "Azure", "GCP", "Microsoft 365",
    ],
}

CERTIFICATIONS = [
    {
        "title": "AI Foundations – Machine Learning",
        "image": "assets/certifications/ai-foundations-ml.png",
    },
    {
        "title": "Machine Learning with Python",
        "image": "assets/certifications/ml-with-python.png",
    },
    {
        "title": "Business Analysis – Essential Tools and Techniques",
        "image": "assets/certifications/business-analysis-tools.png",
    },
    {
        "title": "Learning Data Analytics – Foundations",
        "image": "assets/certifications/data-analytics-foundations.png",
    },
    {
        "title": "Machine Learning and AI Foundations",
        "image": "assets/certifications/ml-and-ai-foundations.png",
    },
]

EXPERIENCE = [
    {
        "role": "UX Research Analyst (Internship)",
        "organization": "PRYPCO",
        "logo": "assets/prypco.png",
        "period": "May 2025 – Jul 2025",
        "impact": "13 customer journey maps directly informed product recommendations for the Prypco One app.",
        "bullets": [
            "Analyzed 13 real-world interviews across buyer, seller, and client "
            "segments in the Dubai real estate market, engineering 13 customer "
            "journey maps to identify pain points, behavioral patterns, and "
            "feature gaps that directly informed product recommendations for "
            "the Prypco One app.",
            "Cleaned, structured, and analyzed ~150 qualitative and quantitative "
            "data points using Pandas, Excel, and Scikit-learn; built Matplotlib "
            "and Tableau visualizations to translate EDA findings into "
            "actionable design recommendations for the Prypco One app.",
        ],
    },
    {
        "role": "UX Branding (Internship)",
        "organization": "Praava Health",
        "logo": "assets/praava.jpg",
        "period": "Sep 2022 – Dec 2022",
        "impact": "Drove a 27% increase in brand recognition and helped launch the company's first TikTok channel.",
        "bullets": [
            "Analyzed marketing campaign performance using Excel (regression, "
            "pivot tables, ANOVA) and Tableau dashboards to measure KPIs, track "
            "CRM outcomes, and deliver strategic recommendations to leadership.",
            "Applied competitive analysis and engagement data to drive a 27% "
            "increase in brand recognition across social platforms, including "
            "launching and growing the company's first TikTok channel.",
            "Collected and structured real-time patient survey data using "
            "Qualtrics and SurveyMonkey, then trained Front Desk staff on data "
            "collection best practices to improve team data quality and "
            "consistency for downstream analysis.",
            "Achievement: Awarded Best Intern at Praava Health for outstanding "
            "performance during the internship among 12 multicultural interns.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "Master of Science in Business Analytics (MSBA)",
        "institution": "East Texas A&M University",
        "logo": "assets/etamu.jpg",
        "period": "Aug 2026",
        "email": "stanjeem@lemail.tamuc.edu",
        "description": "GPA: 3.90",
        "courses": [
            "Database Management",
            "Business Analytics Programming",
            "Data Warehousing",
            "Business Data Science",
            "Applied Decision Modeling",
            "Analytics for Managers",
            "Project Management",
            "Marketing & Management Analytics",
        ],
    },
    {
        "degree": "Bachelor of Business Administration (BBA) in Marketing",
        "institution": "North South University",
        "logo": "assets/nsu.jpg",
        "period": "Dec 2022",
        "email": "samiha.tanjeem@northsouth.edu",
        "description": "",
        "courses": [
            "Computer Information Systems",
            "Applied Business Mathematics",
            "Applied Statistics",
            "Marketing Analytics",
            "Marketing Research",
            "E-Business",
            "Digital Marketing & Social Networks for Business",
            "Operations and Supply Chain Management",
            "Financial Accounting",
            "Managerial Accounting",
        ],
    },
]
