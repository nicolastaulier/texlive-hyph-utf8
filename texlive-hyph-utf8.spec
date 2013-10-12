# revision 30757
# category Package
# catalog-ctan /language/hyph-utf8
# catalog-date 2013-05-08 01:16:25 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-hyph-utf8
Version:	20130508
Release:	1
Summary:	Hyphenation patterns expressed in UTF-8
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyph-utf8
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.source.tar.xz
Source10:	%{name}.rpmlintrc
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Modern native UTF-8 engines such as XeTeX and LuaTeX need
hyphenation patterns in UTF-8 format, whereas older systems
require hyphenation patterns in the 8-bit encoding of the font
in use (such encodings are codified in the LaTeX scheme with
names like OT1, T2A, TS1, OML, LY1, etc). The present package
offers a collection of conversions of existing patterns to UTF-
8 format, together with converters for use with 8-bit fonts in
older systems. Since hyphenation patterns for Knuthian-style
TeX systems are only read at iniTeX time, it is hoped that the
UTF-8 patterns, with their converters, will completely supplant
the older patterns.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-il2.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-il3.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-l7x.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-lth.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-qx.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-t8m.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-af.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-as.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-bg.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-bn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ca.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cop.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cs.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-da.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1996.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-de-ch-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-el-monoton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-el-polyton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-en-gb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-en-us.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-eo.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-es.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-et.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-eu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-fi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-fr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-fur.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ga.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-gl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-grc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-gu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hsb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ia.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-id.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-is.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-it.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ka.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-kmr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-kn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-la.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-lt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-lv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ml.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl-x-lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mul-ethi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-nb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-nl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-nn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-or.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pms.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-rm.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ro.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ru.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-latn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ta.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-te.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-th.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-tk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-tr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-uk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-zh-latn-pinyin.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-af.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-bg.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ca.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-cs.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-cy.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-da.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1901.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1996.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-de-ch-1901.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-eo.il3.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-es.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-et.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-eu.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-fi.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-fr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-fur.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ga.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-gl.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-hr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-hsb.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-hu.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-is.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ka.t8m.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-kmr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-la.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-lt.l7x.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-lv.l7x.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl-x-lmc.lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-nb.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-nl.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-nn.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-pl.qx.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-pt.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ro.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ru.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-cyrl.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-latn.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sk.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sl.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sv.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-th.lth.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-tk.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-tr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-uk.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-zh-latn-pinyin.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-af.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fur.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-it.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-pms.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-rm.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-uk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-zh-latn-pinyin.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex-8bit/copthyph.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-af.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-as.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-bg.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-bn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ca.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cop.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cs.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-da.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-de-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-de-1996.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-de-ch-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-el-monoton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-el-polyton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-en-gb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-en-us.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-eo.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-es.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-et.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-fi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-fr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-fur.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ga.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-gl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-gu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hsb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ia.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-id.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-is.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-it.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ka.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-kmr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-kn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-la.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-lt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-lv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ml.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl-x-lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mul-ethi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-nb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-nl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-nn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-no.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-or.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pms.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-rm.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ro.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ru.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sh-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sh-latn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sr-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ta.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-te.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-th.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-tr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-uk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-zh-latn-pinyin.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-af.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-af.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-af.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-af.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-as.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-as.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-as.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-as.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bg.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bg.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bg.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bg.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bn.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bn.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bn.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ca.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ca.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ca.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ca.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cop.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cop.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cop.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cop.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cs.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cs.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cs.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cs.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cy.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cy.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cy.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cy.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-da.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-da.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-da.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-da.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eo.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eo.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eo.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eo.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-es.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-es.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-es.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-es.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-et.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-et.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-et.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-et.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eu.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eu.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eu.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eu.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fi.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fi.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fi.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fi.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fr.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fr.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fr.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fr.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fur.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fur.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fur.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fur.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ga.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ga.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ga.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ga.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-grc.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-grc.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-grc.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-grc.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gu.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gu.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gu.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gu.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hi.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hi.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hi.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hi.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hr.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hr.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hr.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hr.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hu.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hu.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hu.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hu.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hy.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hy.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hy.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hy.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ia.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ia.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ia.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ia.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-id.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-id.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-id.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-id.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-is.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-is.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-is.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-is.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-it.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-it.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-it.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-it.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ka.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ka.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ka.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ka.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kn.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kn.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kn.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lt.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lt.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lt.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lt.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lv.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lv.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lv.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lv.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ml.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ml.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ml.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ml.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mr.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mr.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mr.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mr.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nb.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nb.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nb.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nb.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nn.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nn.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nn.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-or.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-or.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-or.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-or.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pa.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pa.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pa.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pa.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pms.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pms.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pms.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pms.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pt.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pt.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pt.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pt.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-rm.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-rm.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-rm.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-rm.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ro.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ro.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ro.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ro.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ru.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ru.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ru.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ru.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sa.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sa.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sa.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sa.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sk.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sk.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sk.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sk.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sv.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sv.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sv.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sv.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ta.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ta.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ta.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ta.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-te.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-te.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-te.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-te.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-th.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-th.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-th.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-th.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tk.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tk.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tk.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tk.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tr.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tr.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tr.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tr.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-uk.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-uk.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-uk.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-uk.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.chr.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.lic.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.pat.txt
%{_texmfdistdir}/tex/luatex/hyph-utf8/etex.src
%{_texmfdistdir}/tex/luatex/hyph-utf8/luatex-hyphen.lua
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/CHANGES
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/README
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/bg/azbukaExtended.pdf
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/bg/azbukaExtended.tex
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/es/README
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/es/division.pdf
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/hu/huhyphn.pdf
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/hyphenation-distribution.pdf
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/hyphenation-distribution.tex
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/hyphenation.pdf
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/hyphenation.tex
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/img/miktex-languages.png
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/img/texlive-collection.png
%doc %{_texmfdistdir}/doc/generic/hyph-utf8/sa/hyphenmin.txt
%doc %{_texmfdistdir}/doc/luatex/hyph-utf8/README
%doc %{_texmfdistdir}/doc/luatex/hyph-utf8/luatex-hyphen.pdf
#- source
%doc %{_texmfdistdir}/source/generic/hyph-utf8/README
%doc %{_texmfdistdir}/source/generic/hyph-utf8/contributed/make-exhyph.pl
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/ec.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/il2.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/il3.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/l7x.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/lmc.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/lth.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/qx.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/t2a.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/t8m.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/data/encodings/texnansi.dat
%doc %{_texmfdistdir}/source/generic/hyph-utf8/generate-converters.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/generate-pattern-loaders.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/generate-plain-patterns.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/generate-ptex-patterns.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/generate-tl-files.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/generate-webpage.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/hyph-utf8.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages-txt.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/es/README
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/es/eshyph-make.lua
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/es/eshyph.src
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/eu/generate_patterns_eu.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/README
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glhybiox.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glhyextr.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glhymed.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glhyquim.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glhytec.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glhyxeog.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/gl/glpatter-utf8.tex
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/hy/generate_patterns_hy.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/mul-ethi/generate_patterns_mul-ethi.lua
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/tk/generate_patterns_tk.rb
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/tr/README
%doc %{_texmfdistdir}/source/generic/hyph-utf8/languages/tr/generate_patterns_tr.rb
%doc %{_texmfdistdir}/source/luatex/hyph-utf8/Makefile
%doc %{_texmfdistdir}/source/luatex/hyph-utf8/luatex-hyphen.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
