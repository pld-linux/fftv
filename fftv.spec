# TODO:
#	- %makeinstall --> %{__make} install (Makefile need to be patched)
#	- enable support for all possible features
#	- external ffmpeg
Summary:	GNOME TV viewer
Summary(pl):	Program do ogl±dania TV dla GNOME
Name:		fftv
Version:	0.8.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/fftv/%{name}-%{version}.tar.bz2
# Source0-md5:	07749106e864fcf549e199d5a347f95a
#cvs server: nothing known about fftv-pkg.patch
#Patch0:	%{name}-pkg.patch
URL:		http://fftv.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	faac-devel
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fftv is a TV viewer for use with TV cards and Video for Linux. It also
features a radio user interface. It can support recording of various
formats and codecs including MPEG, AVI, and Ogg. It supports remote
control if LIRC is installed.

%description -l pl
fftv to program do ogl±dania telewizji dzia³aj±cy z kartami
telewizyjnymi i systemem Video for Linux. Ma tak¿e interfejs
u¿ytkownika do radia. Obs³uguje nagrywanie w ró¿nych formatach i
kodekach z MPEG, AVI i Ogg w³±cznie. Obs³uguje pilota je¶li
zainstalowany jest LIRC.

%prep
%setup -q
#%patch0 -p1

%build
%configure \
	--enable-mp3lame \
	--enable-vorbis \
	--enable-faad \
	--enable-faadbin \
	--enable-faac \
	--enable-a52 \
	--enable-pp \
	--enable-gpl

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/%{name}
%{_iconsdir}/%{name}.png
%{_libdir}/%{name}
%{_libdir}/menu/*
%{_libdir}/vhook/*.so
%{_mandir}/man1/*.1*
