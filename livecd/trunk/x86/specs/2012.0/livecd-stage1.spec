subarch: i686
version_stamp: 2013.0
target: livecd-stage1
rel_type: hardened
profile: pentoo:pentoo/hardened/linux/x86
snapshot: 20130408
source_subpath: hardened/stage4-i686-2013.0
portage_overlay: /usr/src/pentoo/portage/trunk
cflags: -Os -march=pentium-m -mtune=nocona -pipe -fomit-frame-pointer -ggdb
cxxflags: -Os -march=pentium-m -mtune=nocona -pipe -fomit-frame-pointer -ggdb


# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
pkgcache_path: /catalyst/tmp/packages/x86-hardened

livecd/use: aufs X livecd gtk -kde -eds gtk2 cairo pam firefox gpm dvdr oss
mpi wps offensive dwm -doc -examples
wifi injection lzma speed gnuplot python pyx test-programs fwcutter qemu
-quicktime -qt -qt3 qt3support qt4 -webkit -cups -spell lua curl -dso
png jpeg gif dri svg aac nsplugin xrandr consolekit -ffmpeg fontconfig
alsa esd fuse gstreamer jack mp3 vorbis wavpack wma
dvd mpeg ogg rtsp x264 xvid sqlite truetype nss
opengl dbus binary-drivers hal acpi usb subversion libkms
analyzer bluetooth cracking databse exploit forensics mitm proxies
scanner rce footprint forging fuzzers voip wireless
-cuda -opencl livecd-stage1 symlink

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages:
pentoo/pentoo
