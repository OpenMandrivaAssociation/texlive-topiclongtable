%global tl_name topiclongtable
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.2
Release:	%{tl_revision}.1
Summary:	Extend longtable with cells that merge hierarchically
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/topiclongtable
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/topiclongtable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/topiclongtable.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package extends longtable implementing cells that: merge with
the one above if it has the same content, do not merge with the one
above unless the ones on the left are merged, are well behaved with
respect to longtable chunking on page breaks, and automatically draw the
correct separation lines. The typical use case is a table spanning
multiple pages that contains a list of hierarchically organized topics
(hence the package name). The package depends on array, expl3,
longtable, multirow, xparse, and zref-abspage.

