Name     : jdk-osgi-compendium
Version  : 4.3.1
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/osgi/org.osgi.compendium/4.3.1/org.osgi.compendium-4.3.1.jar
Source0  : http://repo.maven.apache.org/maven2/org/osgi/org.osgi.compendium/4.3.1/org.osgi.compendium-4.3.1.jar
Source1  : http://repo.maven.apache.org/maven2/org/osgi/org.osgi.compendium/4.3.1/org.osgi.compendium-4.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/osgi-compendium.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/osgi-compendium.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/osgi-compendium.xml \
%{buildroot}/usr/share/maven-poms/osgi-compendium.pom \
%{buildroot}/usr/share/java/osgi-compendium.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/osgi-compendium.jar
/usr/share/maven-metadata/osgi-compendium.xml
/usr/share/maven-poms/osgi-compendium.pom
