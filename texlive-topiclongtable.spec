Name:		texlive-topiclongtable
Version:	54758
Release:	1
Summary:	Extend longtable with cells that merge hierarchically
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/topiclongtable
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topiclongtable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topiclongtable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package extends longtable implementing cells that:
merge with the one above if it has the same content, do not
merge with the one above unless the ones on the left are
merged, are well behaved with respect to longtable chunking on
page breaks, and automatically draw the correct separation
lines. The typical use case is a table spanning multiple pages
that contains a list of hierarchically organized topics (hence
the package name). The package depends on array, expl3,
longtable, multirow, xparse, and zref-abspage.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/topiclongtable
%doc %{_texmfdistdir}/doc/latex/topiclongtable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
