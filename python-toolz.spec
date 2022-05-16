%global _empty_manifest_terminate_build 0
Name:		python-toolz
Version:	0.11.1
Release:	2
Summary:	List processing tools and functional utilities
License:	BSD-3-Clause
URL:		https://github.com/pytoolz/toolz/
Source0:	https://files.pythonhosted.org/packages/d6/0d/fdad31347bf3d058002993a094da1ca95f0f3ef9beec08856d0fe4ad9766/toolz-0.11.1.tar.gz
BuildArch:	noarch


%description
A set of utility functions for iterators, functions, and dictionaries.
See the PyToolz documentation at https://toolz.readthedocs.io

%package -n python3-toolz
Summary:	List processing tools and functional utilities
Provides:	python-toolz
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-toolz
A set of utility functions for iterators, functions, and dictionaries.
See the PyToolz documentation at https://toolz.readthedocs.io

%package help
Summary:	Development documents and examples for toolz
Provides:	python3-toolz-doc
%description help
A set of utility functions for iterators, functions, and dictionaries.
See the PyToolz documentation at https://toolz.readthedocs.io

%prep
%autosetup -n toolz-0.11.1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-toolz -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed May 11 2022 yangping <yangping69@h-partners> - 0.11.1-2
- License compliance rectification

* Tue May 25 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
