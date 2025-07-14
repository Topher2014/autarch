# Maintainer: Topher <your-email@example.com>
pkgname=autarch
pkgver=0.1.0
pkgrel=1
pkgdesc="Local agentic AI assistant wrapper for aider + vLLM"
arch=('any')
url="https://github.com/yourusername/autarch"
license=('MIT')
depends=('python>=3.9' 'python<3.13' 'python-pytorch-cuda')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
   cd "$srcdir/$pkgname-$pkgver"
   
   # Install PyTorch first (dependency order requirement)
   python -m pip install --user torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   
   # Build the package
   python -m build --wheel --no-isolation
}

package() {
   cd "$srcdir/$pkgname-$pkgver"
   python -m installer --destdir="$pkgdir" dist/*.whl
   
   # Install license
   install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
