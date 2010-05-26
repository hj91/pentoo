# Copyright 1999-2010 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=3

DESCRIPTION="Next generation web scanner, identifies what software websites are running"
HOMEPAGE=""
SRC_URI="http://www.morningstarsecurity.com/downloads/${P}.tar.gz"

LICENSE="GPL-3"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE=""

DEPEND="dev-lang/ruby"
RDEPEND="${DEPEND}"

src_compile() {
	# do nothing
	true
}

src_install() {
	DESTDIR="${D}" emake install || die "install failed"
}
