Name:		texlive-tablists
Version:	15878
Release:	1
Summary:	Tabulated lists of short items
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablists
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers environments and commands for one-level and
two-level lists of short items (e.g., exercises in textbooks).
The environments support optional arguments of item numbering
similar to the enumerate or paralist packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
