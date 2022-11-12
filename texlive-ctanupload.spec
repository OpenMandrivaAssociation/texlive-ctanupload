Name:		texlive-ctanupload
Version:	26313
Release:	1
Summary:	Support for users uploading to CTAN
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/ctanupload
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanupload.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanupload.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ctanupload.bin = %{EVRD}

%description
The package provides a Perl script that allows the uploads of a
contribution to CTAN from the command line. The aim us to
simplify the release process for LaTeX package authors.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ctanupload
%{_texmfdistdir}/scripts/ctanupload/ctanupload.pl
%doc %{_texmfdistdir}/doc/support/ctanupload/Makefile.example
%doc %{_texmfdistdir}/doc/support/ctanupload/README
%doc %{_texmfdistdir}/doc/support/ctanupload/ctanupload.pdf
%doc %{_texmfdistdir}/doc/support/ctanupload/ctanupload.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/ctanupload/ctanupload.pl ctanupload
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
