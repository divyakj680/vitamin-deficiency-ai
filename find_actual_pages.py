# find_actual_pages.py
import pymupdf
import re

doc = pymupdf.open('NutriVision_AI_Final_Project_Report.pdf')
print(f'Total pages in PDF: {len(doc)}')

ch1_page_idx = None
for i, page in enumerate(doc):
    text = page.get_text('text')
    if 'CHAPTER 1' in text and 'INTRODUCTION' in text:
        ch1_page_idx = i
        break

print(f'Chapter 1 starts at physical page index {ch1_page_idx} (PDF page {ch1_page_idx + 1})')

sections_found = {}
figures_found = {}
tables_found = {}

for i in range(ch1_page_idx, len(doc)):
    page = doc[i]
    text = page.get_text('text')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    arabic_pg = i - ch1_page_idx + 1
    
    for line in lines:
        m_ch = re.match(r'^CHAPTER\s+([1-9])', line)
        if m_ch:
            ch_num = m_ch.group(1)
            if f'CHAPTER {ch_num}' not in sections_found:
                sections_found[f'CHAPTER {ch_num}'] = arabic_pg
        
        m_sec = re.match(r'^([1-9]\.[0-9]+(?:\.[0-9]+)?)\s+(.*)', line)
        if m_sec:
            sec_num = m_sec.group(1)
            sec_title = m_sec.group(2)
            if sec_num not in sections_found:
                sections_found[sec_num] = arabic_pg
                
        if line == 'REFERENCES':
            if 'REFERENCES' not in sections_found:
                sections_found['REFERENCES'] = arabic_pg
            
        m_fig = re.search(r'Figure\s+([58]\.[1-9])', line, re.IGNORECASE)
        if m_fig:
            fig_id = m_fig.group(1)
            if fig_id not in figures_found:
                figures_found[fig_id] = arabic_pg
                
        m_tab = re.search(r'Table\s+([4678]\.[1-9])', line, re.IGNORECASE)
        if m_tab:
            tab_id = m_tab.group(1)
            if tab_id not in tables_found:
                tables_found[tab_id] = arabic_pg

print('\n--- SECTIONS FOUND (Arabic Page) ---')
for k in sorted(sections_found.keys(), key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r'(\d+)', x)]):
    print(f'{k}: {sections_found[k]}')

print('\n--- FIGURES FOUND (Arabic Page) ---')
for k, v in sorted(figures_found.items()):
    print(f'Figure {k}: {v}')

print('\n--- TABLES FOUND (Arabic Page) ---')
for k, v in sorted(tables_found.items()):
    print(f'Table {k}: {v}')
