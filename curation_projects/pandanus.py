from doc_curation.scraping import pandanus

if __name__ == '__main__':
    # pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=divaseSu&start=0&display=20&enc=utf&to=toutf&numrows=17&totalsearch=18&name=kad&versenumber=pb1.0&jan=on&kic=on&bal=on&pan=on&mdv=on&dtv=on&dtg=on&kbh=on&uru=on&avi=on&kad=on&kum=on&abh=on&mhv=on&sis=on&urc=on&har=on&mss=on&suv=on&bha=on&gig=on&nar=on&srs=on&mlv=on&vkm=on&rag=on&nag=on&pri=on&sva=on&mrk=on&rsh=on&mgd=on&dkc=on&kir=on&rtn=on&mlm=on&gop=on&nai=on&krm=on&line=6146", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/gadyam/kAdambarI.md", overwrite=False)
    # pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=nAladaNDaH&start=0&display=20&enc=utf&to=toutf&numrows=1&totalsearch=1&name=dkc&versenumber=pp1.0&dkc=on&line=20829", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/gadyam/dashakumAra-charitam.md", overwrite=False)
    # pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=sRSTiH&start=0&display=20&enc=utf&to=toutf&numrows=1&totalsearch=1&name=abh&versenumber=1.2&abh=on&line=3", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/nATakam/abhijJNAna-shAkuntalam.md", overwrite=False)
    # pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=atha&start=0&display=20&enc=utf&to=toutf&numrows=37&totalsearch=39&name=kic&versenumber=0.0-0&kic=on&line=9834", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/padyam/kIchaka-vadham.md", overwrite=False)
    pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=atha&start=0&display=20&enc=utf&to=toutf&numrows=129&totalsearch=130&name=gop&versenumber=1.2&gop=on&line=14520", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/gadyam/gopAla-keli-chandrikA.md", overwrite=False)
    ## Out of order lines being returned.
    pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=atha&start=0&display=20&enc=utf&to=toutf&numrows=4&totalsearch=4&name=cas&versenumber=30-3&line=18442", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/gadyam/chaNDI-shatakam.md", overwrite=False)
    pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=atha&start=0&display=20&enc=utf&to=toutf&numrows=72&totalsearch=76&name=jan&versenumber=1.70-1&jan=on&line=18593", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/gadyam/jAnakI-haraNam.md", overwrite=False)
    pandanus.dump_text(init_url="http://iu.ff.cuni.cz/pandanus/electronictexts/?action=context&keyword=atha&start=0&display=20&enc=utf&to=toutf&numrows=26&totalsearch=30&name=dtg&versenumber=0&dtg=on&line=23327", out_path="/home/vvasuki/sanskrit/raw_etexts/kAvyam/nATakam/dUta-ghaTotkacham.md", overwrite=False)
    # pandanus.browser.close()
