Name:		texlive-hyph-utf8
Version:	20180410
Release:	2
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
%{_texmfdistdir}/tex/generic/hyph-utf8
%{_texmfdistdir}/tex/luatex/hyph-utf8
%doc %{_texmfdistdir}/doc/generic/hyph-utf8
%doc %{_texmfdistdir}/doc/luatex/hyph-utf8
#- source
%doc %{_texmfdistdir}/source/generic/hyph-utf8
%doc %{_texmfdistdir}/source/luatex/hyph-utf8

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
