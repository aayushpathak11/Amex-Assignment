from langchain_community.document_loaders import PyPDFLoader

def parse_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    return docs


# BELOW CODE IS FOR UNDERSTANDING THE LOGIC THAT I USED TO PARSE AND CLEAN DATA AND HENCE IS COMMENTED OUT


# file_path1 = r"D:\Amex-Assignment\documents\Financial Policies (PDF).pdf"

# loader = PyPDFLoader(file_path1)

# docs = loader.load() #loader.load() returns a list of document object parsed from pdf
# # print(len(docs)) #prints 17 , means it is loading page wise , 17 page - 17 document objects

# # #Analysing the content for cleaning
# # print(docs[0])
# #Above line prints the following - 

# """
# page_content='FINANCIAL POLICIES 
# Lake County G overnment  


# 1

# I. FINANCIAL PLANNING POLICIES ................................................................................. 1  
# II. BUDGET POLICIES ...................................................................................................... 3
# III. ACCOUNTING, AUDITING & FINANCIAL REPORTING POLICIES ............................... 8
# IV. REVENUE POLICIES ................................................................................................. 11
# V. OPERATING POLICIES .............................................................................................. 12
# VI. CAPITAL PLANNING & BUDGET POLICIES .............................................................. 15

# I. FINANCIAL PLANNING POLICIES
# Introduction
# A long-range plan (LRP) that estimates revenue and expenditure activity in the County, as impacted by regional and  
# national economies, is necessary to support the Commissioners and Community in the decisions they make regarding    
# County services. This planning must recognize the effects of economic cycles on the demand for services and the     
# County’s Revenues. Financial planning should be designed to ensure the delivery of needed services as defined by policy
# and the Comprehensive Plan.
# Policies
# The financial planning and subsequent budgeting for all funds will be based on the following policies:
# 1. Three-Year Plans – The County will prepare annually a three (3) year financial LRP for each fund. Each plan will 
# include revenues, expenditures and other sources and uses with sufficient detail to identify trends and items       
# with major impact.

# 2. Conservative Revenue Estimates – Revenue estimates should be prepared on a conservative basis to minimize        
# the possibility that economic fluctuations could imperil ongoing service programs during the budget year.

# 3. Include Contingencies – Expenditure estimates should anticipate contingencies that are foreseeable.

# 4. Include Asset Management Plan on LRP – The five-year Asset Management Plan (AMP) will include
# equipment, major maintenance, and associated expenses of less than $100,000. Major renovation or
# maintenance projects will be identified in the LRP.' metadata={'producer': 'Adobe PDF Library 23.1.206', 'creator': 'Acrobat PDFMaker 23 for Word', 'creationdate': '2023-06-12T16:09:08-06:00', 'author': 'Hanna Waugh', 'comments': '', 'company': '', 'keywords': '', 'moddate': '2023-06-12T16:09:10-06:00', 'sourcemodified': '', 'subject': '', 'title': '', 'source': 'D:\\Amex-Assignment\\documents\\Financial Policies (PDF).pdf', 'total_pages': 17, 'page': 0, 'page_label': '1'}
# """

# # FINDING 1 - On analysing more document objects , we can observe that page_content has a fixed header repeating in every page's content, this can be cleaned



# #---------------Parsing 2nd PDF-------------

# file_path2 = r"D:\Amex-Assignment\documents\a_2.1_financial_policy_manual_lubbock_chamber_of_commerce_11.19.pdf"
# loader2 = PyPDFLoader(file_path2)

# docs2 = loader2.load()

# # print(len(docs2)) #prints 20 , expected as there are 20 pages

# # print(docs2[1])
# """
# 20
# page_content='Financial Policies 
# 4 | Page
# SECTION II: Line of Authority 
# Board of Directors 
# The Board of Directors has the authority to execute any policies it deems to be in the best 
# interest of the organization within the parameters of the organization’s articles of 
# incorporation, bylaws, or federal, state, and local law. The Board of Directors, in compliance 
# with Chamber bylaws, shall schedule an annual audit of the financial statements of LCC by an 
# independent certified public accountant. 
# Executive Committee 
# The Executive Committee has responsibility for business in the interim between meetings of the 
# Board of Directors. It shall supervise and attend to fiscal matters of LCC and may refer matters 
# to a proper committee or to the Board of Directors. 
# Treasurer and The Finance Committee 
# The Treasurer has the authority to perform regular reviews of the organization’s financial
# activity; oversee the development of the annual budget; and oversee the allocation of
# investment deposits. The Executive Committee acts as the Finance Committee, unless
# otherwise directed by the Board of Directors.
# President and Board Secretary
# The President has the authority to make spending decisions within the parameters of the
# approved budget; employ and terminate personnel; determine salary and bonus levels; create
# and amend operating procedures and controls; make decisions regarding the duties and
# accountabilities of personnel and the delegation of decision-making authority; enter into
# contractual agreements within board designated parameters.
# CFO
# The CFO has whatever authority as may be designated by the President such as the authority to
# design the organization’s accounting system; make spending decisions within the parameters of
# the approved budget; make fixed asset purchase decisions within a certain dollar amount; make
# decisions regarding the allocation of expenses.
# Vice Presidents, Divisions and Program Directors
# Vice Presidents, Divisions and Program Directors have whatever authority as may be designated
# by the President, such as, the authority to make spending decisions within the parameters of
# the approved department or program budget.' metadata={'producer': 'Adobe Acrobat Pro DC 19.12.20035', 'creator': 'Adobe Acrobat Pro DC 19.12.20035', 'creationdate': '2019-07-01T08:36:17-05:00', 'author': 'Sheri Nugent', 'moddate': '2020-05-04T08:30:04-04:00', 'title': 'Financial Policies & Procedures Handbook', 'source': 'D:\\Amex-Assignment\\documents\\a_2.1_financial_policy_manual_lubbock_chamber_of_commerce_11.19.pdf', 'total_pages': 20, 'page': 3, 'page_label': '4'}
# """

# # FINDING 2 - This pdf also has fixed header and footer pattern in each page's content and hence can be cleaned for better clear data



# #---------------Parsing 3RD PDF-------------

# file_path3 = r"D:\Amex-Assignment\documents\Sample-Nonprofit-Financial-Policies-and-Procedures-Manual-Resource.pdf"
# loader3 = PyPDFLoader(file_path3)

# docs3 = loader3.load()

# print(len(docs3)) #prints 23 , expected as there are 23 pages

# print(docs3[7])
# """
# 23
# page_content='Copyright © 2019
# 3
# Introduction
# The purpose of this manual is to set policies & procedures that are consistent with the mission of
# the Nonprofit Organization.  Also, the purpose of this manual is to set sound financial guidelines
# that promote prudent fiscal management; and t o abide by Generally Accepted Accounting
# Principles (GAAP) and the legal requirement governing Nonprofit Organization.
# Manual Protocol
# 1) Nonprofit Organization management will review the financial practices annually.  Any
# recommended revisions will be presented to the Finance Committee of the Board of
# Directors.
# 2) The Finance Committee will review and recommend financial policies and procedures
# changes to the Board of Directors which will review and approve all changes to financial
# policies and procedures.
# Accounting Guidelines and Internal Controls
# To ensure that record keeping is in accordance with Generally Accepted Accounting Principles
# (GAAP) and appropriate internal controls are maintained. The following procedures need to be
# followed:
# 1) Standard accounting procedures, in accordance with GAAP, will be utilized for all
# financial functions.
# 2) Accounting will be done on the accrual basis.
# 3) The Chart of Accounts will be utilized, reviewed annually and updated as required.
# 4) Periodic, unannounced, internal audits will be performed by the Executive Director or
# the Finance Committee of the Board to ensure that the stated operating guidelines have
# been followed.
# 5) To ensure optimal internal controls, Nonprofit Organization will separate functional
# responsibilities as recommended by GAAP, to the extent possible based on staffing
# resources.
# 6) The administrative assistant will maintain financial records in accordance with the
# record retention policy or as determined by Federal, State or local law.' metadata={'producer': 'Adobe PDF Library 11.0', 'creator': 'Acrobat PDFMaker 11 for Word', 'creationdate': '2019-08-30T09:43:36-04:00', 'author': 'Jim Simpson', 'company': '', 'keywords': '', 'lcid': '1033', 'moddate': '2019-08-30T09:43:43-04:00', 'sourcemodified': 'D:20190830133955', 'subject': '', 'title': 'Sample Nonprofit Financial Policies and Procedures Manual', 'usedefaultlanguage': '1', 'version': '99022200', 'source': 'D:\\Amex-Assignment\\documents\\Sample-Nonprofit-Financial-Policies-and-Procedures-Manual-Resource.pdf', 'total_pages': 23, 'page': 2, 'page_label': '3'}
# """
# # FINDING 3 - This pdf also has fixed header and footer pattern in each page's content and hence can be cleaned for better clear data
