Name:           python-tensorizer
Version:        2.9.0
Release:        %autorelease
Summary:        A tool for fast PyTorch module, model, and tensor serialization + deserialization.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/coreweave/tensorizer
Source:         %{pypi_source tensorizer}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  redis
BuildRequires:  python3dist(pytest)

# theoretically this should have transformers and moto
# BuildRequires:  python%{python3_pkgversion}-transformers


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tensorizer' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tensorizer
Summary:        %{summary}

%description -n python3-tensorizer %_description


%prep
%autosetup -p1 -n tensorizer-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import
# %pytest
# in order to run pytest, the user needs to pip install transformers and moto (and possibly other packages as well)

%files -n python3-tensorizer -f %{pyproject_files}


%changelog
%autochangelog