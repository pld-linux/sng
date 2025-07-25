Summary:	Scriptable Network Graphics tool
Summary(pl.UTF-8):	Narzędzie do obsługi formatu SNG
Name:		sng
Version:	1.0.5
Release:	3
License:	distributable - libpng license
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/sng/%{name}-%{version}.tar.gz
# Source0-md5:	798502dcc90511d547549d9b3504b4af
Patch0:		%{name}-libpng.patch
Patch1:		%{name}-libpng14.patch
URL:		http://sng.sourceforge.net/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libpng14-devel
BuildRequires:	libtool
BuildRequires:	xorg-app-rgb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SNG (Scriptable Network Graphics) is a minilanguage designed
specifically to represent the entire contents of a PNG (Portable
Network Graphics) file in an editable form. Thus, SNGs representing
elaborate graphics images and ancillary chunk data can be readily
generated or modified using only text tools.

SNG is implemented by a compiler/decompiler called sng that losslessly
translates between SNG and PNG.

%description -l pl.UTF-8
Minijęzyk SNG (Scriptable Network Graphics) jest tekstową
reprezentacją plików PNG. Pliki SNG zawierają te same informacje co
pliki PNG, mogą jednak być edytowane za pomocą zwykłego edytora tekstu
lub innych narzędzi do obróbki plików tekstowych.

Pakiet SNG zawiera implementację kompilatora/dekompilatora który
pozwala bezstratnie konwertować pliki między formatami PNG a SNG.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-png-inc=%{_includedir}/libpng14 \
	--with-rgbtxt=%{_datadir}/X11/rgb.txt

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/sng.1*
%doc AUTHORS COPYING ChangeLog NEWS README TODO test.sng
