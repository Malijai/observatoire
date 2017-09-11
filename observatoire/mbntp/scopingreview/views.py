# -*- coding: utf-8 -*-
from django.shortcuts import render
import csv
from django.http import HttpResponse, StreamingHttpResponse
from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from django.core.files.storage import FileSystemStorage
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

from django.utils.six.moves import range
from .models import Article, User

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def fait_csv(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    articles_list = Article.objects.all()
    rows = ([article.nom.encode(encoding='UTF-8'),
             article.annee,
             article.titre.encode(encoding='UTF-8'),
             article.resume.encode(encoding='UTF-8'),
             article.resumecourt.encode(encoding='UTF-8'),
             article.originebd,
             article.typepub,
             article.interception,
             article.interceptiontxt.encode(encoding='UTF-8'),
             article.region,
             article.typeparticipanttxt.encode(encoding='UTF-8'),
             article.comparaisonouinon] for article in articles_list)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['ScopingReview_Observatoire'] = 'attachment; filename="ScopingReview_Observatoire.csv"'
    return response


Title = "Observatoire"
pageinfo = " Scoping Review "

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Helvetica',10)
    canvas.drawString(inch, 0.75 * inch, "OSMJ / %s" % pageinfo)
    canvas.restoreState()


def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica',10)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()


def some_pdf(request, pk):
    doc = SimpleDocTemplate("/tmp/scopreview.pdf")

#    Story = [Spacer(1,2*inch)]
    Story = []
    style = styles["Normal"]
#    articles_list = Article.objects.all()
#    for article in articles_list:

    article=Article.objects.get(pk=pk)

    ptext = '<b>Titre etc </b>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    f = Article._meta.get_field('nom')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.nom
    p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
    Story.append(p)
    f = Article._meta.get_field('annee')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.annee
    p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))
    f = Article._meta.get_field('titre')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.titre
    p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    ptext = '<b>Type pub?? </b>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    f = Article._meta.get_field('typepub')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
    Story.append(p)
    for a in article.typepub.all():
        bogustext = a.description
        p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
        Story.append(p)

    for a in article.interception.all():
        bogustext = a.description
        p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
        Story.append(p)

    ptext = '<b>Résumé etc </b>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    f = Article._meta.get_field('resume')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.resume
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Spacer(1,0.1*inch))
    f = Article._meta.get_field('resumecourt')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.resumecourt
    p = Paragraph(bogustext, style)

    Story.append(p)
    Story.append(Spacer(1,0.2*inch))
    ptext = "<b>Détails de l'étude </b>"
    Story.append(Paragraph(ptext, styles["Normal"]))

    ptext = '<b>Métho </b>'
    Story.append(Paragraph(ptext, styles["Normal"]))

    f = Article._meta.get_field('region')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.region
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('typeetude')
    zaza = Article._meta.get_field('devisetude')
    bogustext = "<b>" + f.verbose_name +" / " + zaza.verbose_name + " : </b>"
    p = Paragraph(bogustext, style)
    Story.append(p)
    for a in article.typeetude.all():
        bogustext = a.description
        p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
        Story.append(p)
    for a in article.devisetude.all():
        bogustext = a.description
        p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
        Story.append(p)

    bogustext = article.typeetudetxt
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('typeparticipant')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    p = Paragraph(bogustext, style)
    Story.append(p)
    for a in article.typeparticipant.all():
        bogustext = a.description
        p = Paragraph(bogustext, style,bulletText="\xe2\x80\xa2")
        Story.append(p)
    bogustext = article.typeparticipanttxt
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('duree')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.duree
    p = Paragraph(bogustext, style)
    Story.append(p)

    if article.comparaisonouinon == True:
        ptext = "<b>Il y a un groupe de comparaison </b>"
        Story.append(Paragraph(ptext, styles["Normal"]))
        bogustext = article.comparaisontxt
        p = Paragraph(bogustext, style)
        Story.append(p)

    bogustext = article.comparaisontxt
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('nparticipants')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.nparticipants
    p = Paragraph(bogustext, style)
    Story.append(p)
    f = Article._meta.get_field('agemoyen')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.agemoyen
    p = Paragraph(bogustext, style)
    Story.append(p)

    Story.append(Spacer(1,0.1*inch))

    f = Article._meta.get_field('mesuresresultats')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.mesuresresultats
    p = Paragraph(bogustext, style)
    Story.append(p)
    f = Article._meta.get_field('tauxmesures')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.tauxmesures
    p = Paragraph(bogustext, style)
    Story.append(p)
    f = Article._meta.get_field('analyses')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.analyses
    p = Paragraph(bogustext, style)
    Story.append(p)

    Story.append(Spacer(1,0.1*inch))

    ptext = '<b>Programme </b>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    f = Article._meta.get_field('nomprogramme')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.nomprogramme
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('tsmreference')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.tsmreference
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('interventiontxt')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.interventiontxt
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('clientprogramme')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.clientprogramme
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('intervenantprogramme')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.intervenantprogramme
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('dureeprogramme')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.dureeprogramme
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('conditionprogramme')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.conditionprogramme
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('echec')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.echec
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('succes')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.succes
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Article._meta.get_field('autresinfos')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += article.autresinfos
    p = Paragraph(bogustext, style)
    Story.append(p)

    Story.append(Spacer(1,0.1*inch))

    f = Article._meta.get_field('author')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    ar = User.objects.get(pk=article.author_id)
    bogustext += ar.first_name
    p = Paragraph(bogustext, style)
    Story.append(p)

    doc.build(Story, onFirstPage=myLaterPages, onLaterPages=myLaterPages)


    fs = FileSystemStorage("/tmp")
    with fs.open("scopreview.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scopreview.pdf"'
    return response


def PdfExtraction(request):
    articles = Article.objects.all()
    return render(request, 'scop/index.html',  {'articles': articles})

