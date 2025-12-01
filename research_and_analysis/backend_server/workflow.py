import os
import sys 
from datetime import datetime
from typing import Optional
from langgraph.types import Send


from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AIMessage,HumanMessage , SystemMessage,get_buffer_string
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.tools.tavily_search import TavilySearchResults


from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from research_and_analysis.backend_server.models import (
    Analyst,
    Perspectives,
    GenerateAnalystsState,
    InterviewState,
    ResearchGraphState,

)
from research_and_analysis.utils.model_loader import ModelLoader


class AutonomousReportGenerator:
    def __init__(self):
        """_summary_
        """
        pass

    def create_analyst(self):
        """_summary_
        """
        pass

    def human_feedback(self):
        """_summary_
        """
        pass

    def write_report(self):
        """_summary_
        """
        pass
    
    def write_introduction(self):
        """"""
        pass

    def write_conclusion(self):
        """"""
        pass

    def finalize_report(self):
        """_summary_
        """
        pass

    def save_report(self):
        """_summary_
        """
        pass

    def _save_as_docx(self):
        """_summary_
        """
        pass

    def _save_as_pdf(self):
        """_summary_
        """
        pass

    def build_graph(self):
        """_summary_
        """
        pass
if __name__ == "__main__":
    

