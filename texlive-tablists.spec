%global tl_name tablists
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0e
Release:	%{tl_revision}.1
Summary:	Tabulated lists of short items
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tablists
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablists.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers environments and commands for one-level and two-
level lists of short items (e.g., exercises in textbooks). The
environments support optional arguments of item numbering similar to the
enumerate or paralist packages.

