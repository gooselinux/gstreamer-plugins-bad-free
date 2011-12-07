%define majorminor   0.10
%define gstreamer    gstreamer

%define gst_minver   0.10.29
%define gstpb_minver 0.10.29

Summary: GStreamer streaming media framework "bad" plug-ins
Name: gstreamer-plugins-bad-free
Version: 0.10.19
Release: 2%{?dist}
# The freeze and nfs plugins are LGPLv2 (only)
License: LGPLv2+ and LGPLv2
Group: Applications/Multimedia
URL: http://gstreamer.freedesktop.org/
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
# modified with gst-p-bad-cleanup.sh from SOURCE1
Source: gst-plugins-bad-free-%{version}.tar.bz2
Source1: gst-p-bad-cleanup.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: %{gstreamer} >= %{gst_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}

BuildRequires: check
BuildRequires: gettext-devel
BuildRequires: PyXML
BuildRequires: libXt-devel
BuildRequireS: gtk-doc

BuildRequires: bzip2-devel
BuildRequires: exempi-devel
BuildRequires: gsm-devel
BuildRequires: jasper-devel
BuildRequires: ladspa-devel
BuildRequires: libexif-devel
BuildRequires: libiptcdata-devel
BuildRequires: libmpcdec-devel
BuildRequires: liboil-devel
BuildRequires: librsvg2-devel
BuildRequires: libsndfile-devel
BuildRequires: libvpx-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: openssl-devel
BuildRequires: SDL-devel
Buildrequires: wavpack-devel

Obsoletes: gstreamer-plugins-flumpegdemux < 0.10.15-9
Provides: gstreamer-plugins-flumpegdemux = %{version}-%{release}

Provides: gstreamer-plugins-farsight = 0.12.12-1
Obsoletes: gstreamer-plugins-farsight < 0.12.12

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


%package extras
Summary: Extra GStreamer "bad" plugins (less often used "bad" plugins)
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description extras
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't
tested well enough, or the code is not of good enough quality.

This package (gstreamer-plugins-bad-free-extras) contains extra "bad" plugins
for sources (mythtv), sinks (jack, nas) and effects (pitch) which are not used
very much and require additional libraries to be installed.


%package devel
Summary: Development files for the GStreamer media framework "bad" plug-ins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gstreamer-plugins-base-devel
Obsoletes: gstreamer-plugins-bad-devel < %{version}-%{release}
Provides: gstreamer-plugins-bad-devel = %{version}-%{release}

%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that
aren't tested well enough, or the code is not of good enough quality.


%package devel-docs
Summary: Development documentation for the GStreamer "bad" plug-ins
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Obsoletes: gstreamer-plugins-bad-devel-docs < %{version}-%{release}
Provides: gstreamer-plugins-bad-devel-docs = %{version}-%{release}

%description devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the plug-ins that
aren't tested well enough, or the code is not of good enough quality.


%prep
%setup -q -n gst-plugins-bad-%{version}

%build
%configure \
    --with-package-name="Fedora gstreamer-plugins-bad package" \
    --with-package-origin="http://download.fedora.redhat.com/fedora" \
    --enable-debug --disable-static --enable-gtk-doc --enable-experimental \
    --disable-divx

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang gst-plugins-bad-%{majorminor}

# Clean out files that should not be part of the rpm.
%{__rm} -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.la
%{__rm} -f %{buildroot}%{_libdir}/*.la


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f gst-plugins-bad-%{majorminor}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README REQUIREMENTS
%{_datadir}/gstreamer-%{majorminor}
%{_libdir}/libgstbasevideo-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstsignalprocessor-%{majorminor}.so.*

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdccp.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtmf.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeze.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgsth264parse.so
%{_libdir}/gstreamer-%{majorminor}/libgsthdvparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstinvtelecine.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstliveadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg4videoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegvideoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmve.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnsf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnuvdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstselector.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstscaletempoplugin.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgsttta.so
%{_libdir}/gstreamer-%{majorminor}/libgstvalve.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomeasure.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so

# System (Linux) specific plugins
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstalsaspdif.so
%{_libdir}/gstreamer-%{majorminor}/libgstapexsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2k.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstmetadata.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstvp8.so

#debugging plugin
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so

%files extras
%defattr(-,root,root,-)
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstsdl.so
# Linux specific plugins
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgstbasevideo-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstsignalprocessor-%{majorminor}.so
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{majorminor}/gst/signalprocessor
%{_includedir}/gstreamer-%{majorminor}/gst/video

# pkg-config files
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc

%files devel-docs
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-plugins-%{majorminor}

%changelog
* Wed Jun 27 2010 Benjamin Otte <otte@redhat.com> 0.10.19-2
- Build libvpx plugin
Resolves: rhbz#603110

* Sun Jun 20 2010 Benjamin Otte <otte@redhat.com> 0.10.19-1
- Update to 0.10.19
- Sync spec file with Fedora version
Related: rhbz#603110

* Thu Feb 18 2010 Benjamin Otte <otte@redhat.com> 0.10.17-4
- Drop CELT support.
Related: rhbz#566519

* Mon Feb 12 2010 Benjamin Otte <otte@gnome.org> 0.10.17-3
- Remove _all_ plugins that depend on libs that aren't shipped in RHEL6
Related: rhbz#561858

* Mon Feb 12 2010 Benjamin Otte <otte@gnome.org> 0.10.17-2
- Remove plugins that depend on libs that aren't shipped in RHEL6
Related: rhbz#561858

* Fri Feb 12 2010 Benjamin Otte <otte@gnome.org> 0.10.17-1
- Copy package from devel

