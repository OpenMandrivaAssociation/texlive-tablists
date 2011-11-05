# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tablists
# catalog-date 2009-08-04 22:17:36 +0200
# catalog-license lppl
# catalog-version 0.0e
Name:		texlive-tablists
Version:	0.0e
Release:	1
Summary:	Tabulated lists of short items
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablists
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package offers environments and commands for one-level and
two-level lists of short items (e.g., exercises in textbooks).
The environments support optional arguments of item numbering
similar to the enumerate or paralist packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tablists/tablists.sty
%doc %{_texmfdistdir}/doc/latex/tablists/README
%doc %{_texmfdistdir}/doc/latex/tablists/tablists-rus.pdf
%doc %{_texmfdistdir}/doc/latex/tablists/tablists-rus.tex
%doc %{_texmfdistdir}/doc/latex/tablists/tablists.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tablists/tablists.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
