%define module   MooseX-Method-Signatures
%define version    0.06
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    No summary found
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Devel::Declare)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Meta::Signature::Combined)
BuildRequires: perl(Perl6::Signature)
BuildRequires: perl(Scope::Guard)
BuildRequires: perl(Test::Exception)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Provides a proper method keyword, like "sub" but specificly for making
methods and validating their arguments against Moose type constraints.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/MooseX

