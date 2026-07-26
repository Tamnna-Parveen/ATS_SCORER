import io
import logging

from xhtml2pdf import pisa

logger = logging.getLogger('ats_resume_scorer')


def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
    """
    Combines multiple HTML documents into a single PDF.
    Uses xhtml2pdf (pure Python, no system-level dependencies needed).
    """
    # Combine all HTML documents into one, with a page break between each
    combined_html = ""
    html_list = list(html_docs.values())

    for i, html_str in enumerate(html_list):
        combined_html += html_str
        if i < len(html_list) - 1:
            # Force a page break before the next document
            combined_html += '<div style="page-break-after: always;"></div>'

    output = io.BytesIO()
    result = pisa.CreatePDF(src=combined_html, dest=output)

    if result.err:
        logger.error(f'PDF generation failed with {result.err} error(s)')
        raise RuntimeError('Failed to generate PDF — check HTML content for issues')

    pdf_bytes = output.getvalue()
    output.close()

    return pdf_bytes