%define major 8
%define libname %{mklibname SonicDEScreen}
%define devname %{mklibname SonicDEScreen -d}
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')

Summary:	Library for dealing with screen parameters
Name:		sonic-screen-library
Version:	6.6.3
Release:	%{?git:0.%{git}.}2
License:	LGPL
Group:		System/Libraries
Url:		https://github.com/Sonic-DE/sonic-screen-library
# %if 0%{?git:1}
# Source0:	https://invent.kde.org/plasma/libkscreen/-/archive/%{gitbranch}/libkscreen-%{gitbranchd}.tar.bz2#/libkscreen-%{git}.tar.bz2
# %else
Source0:	%url/archive/refs/tags/%version.tar.gz#/%name-%version.tar.gz
# %endif

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
# For qch docs
BuildRequires:	doxygen
BuildRequires:	cmake(Qt6ToolsTools)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DBUILD_TESTING:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires:	%{libname} = %{EVRD}
Conflicts:      libkscreen

%package -n %{libname}
Summary: The SonicDE Screen library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts:  %{_lib}KF6Screen

%description -n %{libname}
%summary

%files -n %{libname}
%{_libdir}/libKF6Screen.so.%{major}*
%{_libdir}/libKF6Screen.so.6*
%{_libdir}/libKF6ScreenDpms.so.%{major}*
%{_libdir}/libKF6ScreenDpms.so.6*

%description
Library for dealing with screen parameters.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libkscreen.categories
%dir %{_qtdir}/plugins/kf6/kscreen
%{_qtdir}/plugins/kf6/kscreen/KSC_Fake.so
%{_qtdir}/plugins/kf6/kscreen/KSC_XRandR.so
%{_libdir}/libexec/kf6/kscreen_backend_launcher
%{_datadir}/dbus-1/services/org.kde.kscreen.service
%{_prefix}/lib/systemd/user/plasma-kscreen.service

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/SonicDE and Qt
Requires:	%{libname} = %{EVRD}
Conflicts:      %{_lib}KF6Screen-devel

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF6/KScreen
%{_includedir}/KF6/kscreen_version.h
%{_libdir}/cmake/KF6Screen
%{_libdir}/libKF6Screen.so
%{_libdir}/libKF6ScreenDpms.so
%{_libdir}/pkgconfig/*.pc

%package -n sonic-screen-doctor
Summary:	Tool for examining SonicDE Screen
Group:		Development/SonicDE and Qt
Requires:	%{libname} = %{EVRD}
Conflicts:  kscreen-doctor


%description -n sonic-screen-doctor
%summary

%files -n sonic-screen-doctor
%{_bindir}/kscreen-doctor
%{_datadir}/zsh/site-functions/_kscreen-doctor

#----------------------------------------------------------------------------

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}
Conflicts:  libkscreen-devel-docs

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_qtdir}/doc/KF?Screen.*
