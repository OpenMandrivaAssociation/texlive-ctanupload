%global tl_name ctanupload
%global tl_revision 26313

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2c
Release:	%{tl_revision}.1
Summary:	Support for users uploading to CTAN
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ctanupload
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanupload.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanupload.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(ctanupload.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Perl script that allows the uploads of a
contribution to CTAN from the command line. The aim is to simplify the
release process for LaTeX package authors. Note by the CTAN team
(2015-02-05): It seems that this script is currently not working.

