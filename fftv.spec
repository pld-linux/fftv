# TODO:
#	- enable support for all possible features
#	- external ffmpeg
Summary:	GNOME TV viewer
Name:		fftv
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	1703c5f37f1512d1c0c81a22b4caffc6
Patch0:		%{name}-pkg.patch
URL:		http://fftv.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	zlib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	SDL-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
fftv is a TV viewer for use with TV cards and Video for Linux. It also
features a radio user interface. It can support recording of various
formats and codecs including MPEG, AVI, and Ogg. It supports remote
control if LIRC is installed.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*
