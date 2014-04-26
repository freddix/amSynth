Summary:	Software synthesizer
Name:		amSynth
Version:	1.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/project/amsynthe/amsynth-%{version}.tar.gz
# Source0-md5:	92aeadad41792e4dfedff5ab16a5cc5e
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	dssi
BuildRequires:	gtkmm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
amSynth is a software synth that provides a classic subtractive
synthesizer topology, with
- Dual oscillators with classic waveforms - sine / saw / square
  / noise
- 24 dB/oct low-pass resonant filter
- Independent ADSR envelopes for filter & amplitude
- LFO which can module the oscillators, filter, and amplitude
- Distortion effect
- Reverb

Currently it runs as a stand-alone application on Linux, supporting
OSS, ALSA and JACK for Audio / MIDI I/O.

%prep
%setup -qn amsynth-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/amsynth.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/amsynth
%{_desktopdir}/amsynth.desktop
%{_pixmapsdir}/amsynth.png

# create subpkg (?)
%dir %{_libdir}/dssi/amsynth_dssi
%attr(755,root,root) %{_libdir}/dssi/amsynth_dssi.so
%attr(755,root,root) %{_libdir}/dssi/amsynth_dssi/amsynth_dssi_gtk

# create subpkg (?)
%dir %{_libdir}/lv2/amsynth.lv2
%attr(755,root,root) %{_libdir}/lv2/amsynth.lv2/amsynth_lv2.so
%attr(755,root,root) %{_libdir}/lv2/amsynth.lv2/amsynth_lv2_gtk.so
%{_libdir}/lv2/amsynth.lv2/*.ttl

