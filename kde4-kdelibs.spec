# TODO
# - make possible to install with kde3
#
# Conditional build:
%bcond_without	alsa		# build without ALSA support
%bcond_without	apidocs		# don't prepare API documentation
%bcond_without	kerberos5	# disable kerberos
%bcond_with	verbose		# verbose build
#
%define		_state		stable

Summary:	K Desktop Environment - libraries
Summary(es.UTF-8):	K Desktop Environment - bibliotecas
Summary(ko.UTF-8):	KDE - 라이브러리
Summary(pl.UTF-8):	K Desktop Environment - biblioteki
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE
Summary(ru.UTF-8):	K Desktop Environment - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment - Бібліотеки
%define	orgname	kdelibs
Name:		kdelibs4
Version:	4.0.0
Release:	0.2
Epoch:		9
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/latest/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	79d0f83ca81fc4a135663943340c0b8f
Source1:	pnm.protocol
Source2:	x-icq.mimelnk
Source3:	x-mplayer2.desktop
Patch0:		%{name}-findqt4.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	Qt3Support-devel >= 4.3.0
BuildRequires:	QtCore-devel >= 4.3.0
BuildRequires:	QtDBus-devel >= 4.3.0
BuildRequires:	QtDesigner-devel >= 4.3.0
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	QtSvg-devel >= 4.3.0
BuildRequires:	QtTest-devel >= 4.3.0
BuildRequires:	QtUiTools-devel >= 4.3.0
BuildRequires:	QtXml-devel >= 4.3.0
BuildRequires:	acl-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	aspell-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	enchant-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	hspell-devel
BuildRequires:	jasper-devel >= 1.600
%{?with_kerberos5:BuildRequires:	krb5-devel}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
BuildRequires:	libwmf-devel >= 2:0.2.0
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	lua50-devel
BuildRequires:	mdns-bonjour-devel
BuildRequires:	openmotif-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.3.3-3
%{?with_apidocs:BuildRequires:	qt4-doc >= 4.3.0}
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	shared-mime-info
BuildRequires:	soprano-devel >= 1.97.1
BuildRequires:	strigi-devel >= 0.5.4
BuildRequires:	sysstat
BuildRequires:	utempter-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	QtCore >= 4.2.0
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	hicolor-icon-theme
Requires:	setup >= 2.4.6-7
Requires:	xorg-app-iceauth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_kde_prefix		%{_prefix}
%define		_kde_libdir		%{_libdir}
%define		_kde_share_dir	%{_datadir}
%define		_kde_html_dir	%{_kdedocdir}
%define		_kde_config_dir	%{_datadir}/config

%define		_noautoreq	libtool(.*)

# confuses OpenEXR detection
%undefine	configure_cache

%description
This package includes libraries that are central to the development
and execution of a KDE program, misc HTML documentation and theme
modules.

Included in this package are among others:
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- khtml - KDE HTML widget with javascript and CSS support,
- kwallet - KDE password manager.

%description -l es.UTF-8
Bibliotecas para KDE.

%description -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do rozwijania i uruchamiania
aplikacji KDE, różną dokumentację oraz moduły z motywami wyglądu KDE.

Pakiet ten zawiera między innymi:
- kdecore - podstawową bibliotekę KDE,
- kdeui - interfejs użytkownika KDE,
- khtml - obsługę HTML, javascript oraz CSS dla KDE,
- kwallet - system zarządzania hasłami w KDE.

%description -l pt_BR.UTF-8
Bibliotecas de fundação do KDE requeridas por todo e qualquer
aplicativo KDE.

%description -l ru.UTF-8
Библиотеки для K Desktop Environment.

Включены библиотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (интерфейс пользователя),
- khtmlw (работа с HTML),
- kimgio (обработка изображений).
- kspell (проверка орфографии),

%description -l uk.UTF-8
Бібліотеки для K Desktop Environment.

Включені такі бібліотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (інтерфейс користувача),
- khtmlw (робота з HTML),
- kimgio (обробка зображень).
- kspell (перевірка орфографії),

%package libs
Summary:	KDE libraries
Summary(pl.UTF-8):	Biblioteki KDE
Group:		Libraries

%description libs
KDE libraries.

%description libs -l pl.UTF-8
Biblioteki KDE.

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl.UTF-8):	kdelibs - pliki nagłówkowe i dokumentacja do kdelibs
Summary(pt_BR.UTF-8):	Arquivos de inclusão e documentação para compilar aplicativos KDE
Summary(ru.UTF-8):	Хедеры и документация для компилляции программ KDE
Summary(uk.UTF-8):	Хедери та документація для компіляції програм KDE
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	acl-devel
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel
Obsoletes:	arts-kde-devel
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs-static
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel
Obsoletes:	kttsd-devel
Conflicts:	kdebase-devel <= 9:3.1.90

%description devel
This package contains header files and development documentation for
kdelibs.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdelibs.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
KDE.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для KDE.

%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):	Dokumentacja API
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kttsd-apidocs

%description apidocs
Annotated reference of KDE libraries programming interface including:
- class lists
- class members
- namespaces

%description apidocs -l pl.UTF-8
Dokumentacja interfejsu programowania bibliotek KDE z przypisami.
Zawiera:
- listy klas i ich składników
- listę przestrzeni nazw (namespace)

#%package kgrantpty
#Summary:	Helper program to fix terminal permissions
#Summary(pl.UTF-8):   Program pomocniczy do ustawiania uprawnień terminala
#Group:		Applications/Terminal
#Requires:	%{name} = %{epoch}:%{version}-%{release}

#%description kgrantpty
#This suid root program fixes the permissions of pseudo-terminal device
#files so that they cannot be eavesdropped by other local users.
#Systems that support /dev/pts (typical PLD installations do) don't
#require an extra program to do it, in that case this package is
#useless.

#Install this package if you're running a custom system that lacks
#Unix98 pts support and privacy from other local users is a concern for
#you.

#%description kgrantpty -l pl.UTF-8
#Ten program, działający z uprawnieniami roota, poprawia uprawnienia
#plików pseudo-terminali, żeby uniknąć ich podsłuchiwania przez innych
#lokalnych użytkowników. Systemy obsługujące /dev/pts (typowe
#instalacje PLD go obsługują) nie wymagają do tego dodatkowego
#programu, w tym przypadku ten pakiet jest bezużyteczny.

#Zainstaluj ten pakiet jeżeli korzystasz z nietypowej konfiguracji
#nieobsługującej pts-ów typu Unix98 i obawiasz się inwigilacji ze
#strony innych użytkowników lokalnych.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p0

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export KDEDIR=%{_prefix}
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_kde_prefix} \
	-DCMAKE_BUILD_TYPE=%{_kde_build_type} \
	-DLIB_INSTALL_DIR=%{_kde_libdir} \
	-DCONFIG_INSTALL_DIR=%{_kde_config_dir} \
	-DSYSCONF_INSTALL_DIR=/etc \
	-DDATA_INSTALL_DIR=%{_kde_share_dir}/apps \
	-DKCFG_INSTALL_DIR=%{_kde_share_dir}/config.kcfg \
	-DMIME_INSTALL_DIR=/nogo \
	-DTEMPLATES_INSTALL_DIR=%{_kde_share_dir}/templates \
	-DHTML_INSTALL_DIR=%{_kde_html_dir} \
	-DLIB_SUFFIX=$(lib=%{_lib}; echo ${lib#lib}) \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT/etc/security \
	$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
	$RPM_BUILD_ROOT%{_datadir}/autostart \
	$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
	$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
	$RPM_BUILD_ROOT%{_datadir}/apps/profiles \
	$RPM_BUILD_ROOT%{_datadir}/apps/remotes \
	$RPM_BUILD_ROOT%{_datadir}/config/magic \
	$RPM_BUILD_ROOT%{_datadir}/config.kcfg \
	$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \
	$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps \
	$RPM_BUILD_ROOT%{_iconsdir}/oxygen/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

# For fileshare
touch $RPM_BUILD_ROOT/etc/security/fileshare.conf

if [ -d $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-%{version}-apidocs ] ; then
	mv -f $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-{%{version}-,}apidocs
fi

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_docdir}/kde
%dir %{_kdedocdir}
%dir %{_kdedocdir}/en
%lang(en) %{_kdedocdir}/en/common
%ghost /etc/security/fileshare.conf
%attr(755,root,root) %{_bindir}/kde4automoc
%attr(755,root,root) %{_bindir}/checkXML
%attr(755,root,root) %{_bindir}/kjs
%attr(755,root,root) %{_bindir}/kbuildsycoca4
%attr(755,root,root) %{_bindir}/kcookiejar4
%attr(755,root,root) %{_bindir}/kde4-config
%attr(755,root,root) %{_bindir}/kded4
%attr(755,root,root) %{_bindir}/kdeinit4
%attr(755,root,root) %{_bindir}/kdeinit4_shutdown
%attr(755,root,root) %{_bindir}/kdeinit4_wrapper
%attr(755,root,root) %{_bindir}/kjscmd
%attr(755,root,root) %{_bindir}/kjsconsole
%attr(755,root,root) %{_bindir}/kross
%attr(755,root,root) %{_bindir}/kshell4
%attr(755,root,root) %{_bindir}/kunittestmodrunner
%attr(755,root,root) %{_bindir}/kwrapper4
%attr(755,root,root) %{_bindir}/makekdewidgets
%attr(755,root,root) %{_bindir}/meinproc4
%attr(755,root,root) %{_bindir}/preparetips

# nepomuk ???
%attr(755,root,root) %{_bindir}/nepomuk-rcgen
%dir %{_datadir}/apps/nepomuk
%{_datadir}/apps/nepomuk/ontologies
%dir %{_datadir}/apps/nepomuk/pics
%{_datadir}/apps/nepomuk/pics/rating.png
%{_kdedocdir}/en/sonnet
%{_mandir}/man1/checkXML.1*
%{_mandir}/man1/kde4-config.1*
%{_mandir}/man7/kdeoptions.7*
%{_mandir}/man7/qtoptions.7*
%{_mandir}/man8/kbuildsycoca4.8*
##### nepomuk ???

%dir %{_datadir}/autostart
%dir %{_datadir}/apps
%dir %{_datadir}/apps/kconf_update
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.sh
%{_datadir}/apps/kconf_update/*.upd

%{_datadir}/apps/LICENSES
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kdeui
%{_datadir}/apps/kdewidgets
%{_datadir}/apps/khtml
%{_datadir}/apps/kjava
%{_datadir}/apps/ksgmltools2
%{_datadir}/apps/kssl
%{_datadir}/apps/ktexteditor_docwordcompletion
%{_datadir}/apps/ktexteditor_insertfile
%{_datadir}/apps/ktexteditor_kdatatool
%{_datadir}/apps/proxyscout
%{_datadir}/apps/kcharselect
%{_datadir}/apps/kcm_phonon
%{_datadir}/apps/knewstuff

%dir %{_datadir}/apps/phonon
%{_datadir}/apps/phonon/phonon.notifyrc

%dir %{_datadir}/services

%{_iconsdir}/crystalsvg
%{_iconsdir}/oxygen
%{_iconsdir}/hicolor/*x*/actions/*.png

%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps/profiles
%dir %{_datadir}/apps/remotes
%dir %{_datadir}/config.kcfg
%dir %{_datadir}/services/kconfiguredialog

%{_datadir}/config
%{_datadir}/locale/all_languages
%{_datadir}/mime/packages
%dir %{_datadir}/kde4
%{_datadir}/kde4/servicetypes
%{_datadir}/kde4/services

# conflicts with applnk
#%{_sysconfdir}/xdg/menus/applications.menu

%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/interfaces/*.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkde3support.so.*
%attr(755,root,root) %{_libdir}/libkdecore.so.*
%attr(755,root,root) %{_libdir}/libkdefakes.so.*
%attr(755,root,root) %{_libdir}/libkdesu.so.*
%attr(755,root,root) %{_libdir}/libkpty.so.*
%attr(755,root,root) %{_libdir}/libkdeui.so.*
%attr(755,root,root) %{_libdir}/libkdnssd.so.*
%attr(755,root,root) %{_libdir}/libkhtml.so.*
%attr(755,root,root) %{_libdir}/libkimproxy.so.*
%attr(755,root,root) %{_libdir}/libkio.so.*
%attr(755,root,root) %{_libdir}/libkjs.so.*
%attr(755,root,root) %{_libdir}/libkjsembed.so.*
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*
%attr(755,root,root) %{_libdir}/libknewstuff2.so.*
%attr(755,root,root) %{_libdir}/libknotifyconfig.so.*
%attr(755,root,root) %{_libdir}/libkntlm.so.*
%attr(755,root,root) %{_libdir}/libkparts.so.*
%attr(755,root,root) %{_libdir}/libktexteditor.so.*
%attr(755,root,root) %{_libdir}/libkunittest.so.*
%attr(755,root,root) %{_libdir}/libkutils.so.*
%attr(755,root,root) %{_libdir}/libkwalletbackend.so.*
%attr(755,root,root) %{_libdir}/libsolid.so.*
%attr(755,root,root) %{_libdir}/libthreadweaver.so.*
%attr(755,root,root) %{_libdir}/libkaudiodevicelist.so.*
%attr(755,root,root) %{_libdir}/libkfile.so.*
%attr(755,root,root) %{_libdir}/libkrosscore.so.*
%attr(755,root,root) %{_libdir}/libkrossui.so.*
%attr(755,root,root) %{_libdir}/libnepomuk.so.4.0.0
%attr(755,root,root) %{_libdir}/libnepomuk.so.4
%attr(755,root,root) %{_libdir}/libphonon.so.*
%attr(755,root,root) %{_libdir}/libphononexperimental.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kbuildsycoca4.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kded4.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kconf_update.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libkdeinit4_klauncher.so

%dir %{_libdir}/kde4
%attr(755,root,root) %{_libdir}/kde4/*.so
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/designer
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdewidgets.so
%dir %{_libdir}/kde4/plugins/imageformats
%attr(755,root,root) %{_libdir}/kde4/plugins/imageformats/kimg*.so
%dir %{_libdir}/kde4/plugins/phonon_platform
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_platform/kde.so
%dir %{_libdir}/kconf_update_bin
%dir %{_libdir}/kde4/libexec
%attr(755,root,root) %{_libdir}/kde4/libexec/*
%dir %{_datadir}/apps/libphonon
%{_datadir}/apps/libphonon/hardwaredatabase

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kconfig_compiler
%attr(755,root,root) %{_libdir}/libkde3support.so
%attr(755,root,root) %{_libdir}/libkdecore.so
%attr(755,root,root) %{_libdir}/libkdefakes.so
%attr(755,root,root) %{_libdir}/libkpty.so
%attr(755,root,root) %{_libdir}/libkdesu.so
%attr(755,root,root) %{_libdir}/libkdeui.so
%attr(755,root,root) %{_libdir}/libkdnssd.so
%attr(755,root,root) %{_libdir}/libkhtml.so
%attr(755,root,root) %{_libdir}/libkimproxy.so
%attr(755,root,root) %{_libdir}/libkio.so
%attr(755,root,root) %{_libdir}/libkjs.so
%attr(755,root,root) %{_libdir}/libkjsembed.so
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/libknotifyconfig.so
%attr(755,root,root) %{_libdir}/libkntlm.so
%attr(755,root,root) %{_libdir}/libkparts.so
%attr(755,root,root) %{_libdir}/libktexteditor.so
%attr(755,root,root) %{_libdir}/libkunittest.so
%attr(755,root,root) %{_libdir}/libkutils.so
%attr(755,root,root) %{_libdir}/libkwalletbackend.so
%attr(755,root,root) %{_libdir}/libsolid.so
%attr(755,root,root) %{_libdir}/libthreadweaver.so
%attr(755,root,root) %{_libdir}/libkaudiodevicelist.so
%attr(755,root,root) %{_libdir}/libkfile.so
%attr(755,root,root) %{_libdir}/libphonon.so
%attr(755,root,root) %{_libdir}/libknewstuff2.so
%attr(755,root,root) %{_libdir}/libnepomuk.so
%attr(755,root,root) %{_libdir}/libkrosscore.so
%attr(755,root,root) %{_libdir}/libkrossui.so
%attr(755,root,root) %{_libdir}/libphononexperimental.so
%{_includedir}/*
%{_datadir}/apps/cmake

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
#%{_kdedocdir}/en/%{name}*-apidocs
%endif
