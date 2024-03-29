#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-backports.shutil_get_terminal_size
Version  : 1.0.0
Release  : 57
URL      : https://files.pythonhosted.org/packages/ec/9c/368086faa9c016efce5da3e0e13ba392c9db79e3ab740b763fe28620b18b/backports.shutil_get_terminal_size-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ec/9c/368086faa9c016efce5da3e0e13ba392c9db79e3ab740b763fe28620b18b/backports.shutil_get_terminal_size-1.0.0.tar.gz
Summary  : A backport of the get_terminal_size function from Python 3.3's shutil.
Group    : Development/Tools
License  : MIT
Requires: pypi-backports.shutil_get_terminal_size-license = %{version}-%{release}
Requires: pypi-backports.shutil_get_terminal_size-python = %{version}-%{release}
Requires: pypi-backports.shutil_get_terminal_size-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
==================================
        
        A backport of the `get_terminal_size`_ function from Python 3.3's shutil.
        
        Unlike the original version it is written in pure Python rather than C,
        so it might be a tiny bit slower.

%package license
Summary: license components for the pypi-backports.shutil_get_terminal_size package.
Group: Default

%description license
license components for the pypi-backports.shutil_get_terminal_size package.


%package python
Summary: python components for the pypi-backports.shutil_get_terminal_size package.
Group: Default
Requires: pypi-backports.shutil_get_terminal_size-python3 = %{version}-%{release}

%description python
python components for the pypi-backports.shutil_get_terminal_size package.


%package python3
Summary: python3 components for the pypi-backports.shutil_get_terminal_size package.
Group: Default
Requires: python3-core
Provides: pypi(backports.shutil_get_terminal_size)

%description python3
python3 components for the pypi-backports.shutil_get_terminal_size package.


%prep
%setup -q -n backports.shutil_get_terminal_size-1.0.0
cd %{_builddir}/backports.shutil_get_terminal_size-1.0.0
pushd ..
cp -a backports.shutil_get_terminal_size-1.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666666705
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-backports.shutil_get_terminal_size
cp %{_builddir}/backports.shutil_get_terminal_size-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-backports.shutil_get_terminal_size/15d880395d5331f62ab5b02a678d3d826560ea21
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.11/site-packages/backports/__init__.py
rm -f %{buildroot}*/usr/lib/python3.11/site-packages/backports/__pycache__/__init__.cpython-*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-backports.shutil_get_terminal_size/15d880395d5331f62ab5b02a678d3d826560ea21

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
