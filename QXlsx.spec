#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
Name     : QXlsx
Version  : 1.5.0
Release  : 5
URL      : https://github.com/QtExcel/QXlsx/archive/v1.5.0/QXlsx-1.5.0.tar.gz
Source0  : https://github.com/QtExcel/QXlsx/archive/v1.5.0/QXlsx-1.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: QXlsx-lib = %{version}-%{release}
Requires: QXlsx-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# QXlsx
<p align="center"><img src="https://raw.githubusercontent.com/QtExcel/QXlsx/master/markdown.data/QXlsx-Desktop.png"></p>

%package dev
Summary: dev components for the QXlsx package.
Group: Development
Requires: QXlsx-lib = %{version}-%{release}
Provides: QXlsx-devel = %{version}-%{release}
Requires: QXlsx = %{version}-%{release}

%description dev
dev components for the QXlsx package.


%package lib
Summary: lib components for the QXlsx package.
Group: Libraries
Requires: QXlsx-license = %{version}-%{release}

%description lib
lib components for the QXlsx package.


%package license
Summary: license components for the QXlsx package.
Group: Default

%description license
license components for the QXlsx package.


%prep
%setup -q -n QXlsx-1.5.0
cd %{_builddir}/QXlsx-1.5.0
pushd ..
cp -a QXlsx-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735662531
pushd QXlsx
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd
pushd ../buildavx2/QXlsx
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735662531
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/QXlsx
cp %{_builddir}/QXlsx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/QXlsx/0fc052f0f02f09fd3d64d63ab5deed0ebcbb0ba7 || :
cp %{_builddir}/QXlsx-%{version}/Pump/xlsx_files/License.txt %{buildroot}/usr/share/package-licenses/QXlsx/ddc5f49c0c88da977ac099ee6e7f251c5cdc95be || :
export GOAMD64=v2
pushd ../buildavx2/QXlsx
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
pushd QXlsx
GOAMD64=v2
pushd clr-build
%make_install
popd
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QXlsxQt6/xlsxabstractooxmlfile.h
/usr/include/QXlsxQt6/xlsxabstractsheet.h
/usr/include/QXlsxQt6/xlsxabstractsheet_p.h
/usr/include/QXlsxQt6/xlsxcell.h
/usr/include/QXlsxQt6/xlsxcellformula.h
/usr/include/QXlsxQt6/xlsxcelllocation.h
/usr/include/QXlsxQt6/xlsxcellrange.h
/usr/include/QXlsxQt6/xlsxcellreference.h
/usr/include/QXlsxQt6/xlsxchart.h
/usr/include/QXlsxQt6/xlsxchartsheet.h
/usr/include/QXlsxQt6/xlsxconditionalformatting.h
/usr/include/QXlsxQt6/xlsxdatavalidation.h
/usr/include/QXlsxQt6/xlsxdatetype.h
/usr/include/QXlsxQt6/xlsxdocument.h
/usr/include/QXlsxQt6/xlsxformat.h
/usr/include/QXlsxQt6/xlsxglobal.h
/usr/include/QXlsxQt6/xlsxrichstring.h
/usr/include/QXlsxQt6/xlsxworkbook.h
/usr/include/QXlsxQt6/xlsxworksheet.h
/usr/lib64/cmake/QXlsxQt6/QXlsxQt6Config.cmake
/usr/lib64/cmake/QXlsxQt6/QXlsxQt6ConfigVersion.cmake
/usr/lib64/cmake/QXlsxQt6/QXlsxQt6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/QXlsxQt6/QXlsxQt6Targets.cmake
/usr/lib64/libQXlsxQt6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQXlsxQt6.so.1.5.0
/usr/lib64/libQXlsxQt6.so.1
/usr/lib64/libQXlsxQt6.so.1.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/QXlsx/0fc052f0f02f09fd3d64d63ab5deed0ebcbb0ba7
/usr/share/package-licenses/QXlsx/ddc5f49c0c88da977ac099ee6e7f251c5cdc95be
