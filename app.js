/* SERTIFIKAT */
if ($('certs')) { try {
  var IMG_RE = /\.(jpe?g|png|webp|gif)$/i, PDF_RE = /\.pdf$/i;
  var FOLDERS = {'Cognitive Class AI':'Cognitive Class Ai', 'IBM SkillsBuild':'IBM Skills Build'};
  function certFile(c){
    if (!c.f) return c.g || '';
    var dir = (SITE.certDir === undefined) ? 'Sertifikat/' : SITE.certDir;
    var f = c.f.replace(/^\/+/, '');
    if (f.indexOf('/') < 0 && c.k) f = ((SITE.folders && SITE.folders[c.k]) || FOLDERS[c.k] || c.k) + '/' + f;
    if (dir && f.toLowerCase().indexOf(dir.toLowerCase()) !== 0) f = dir + f;
    return encodeURI(f);
  }
  var certGroup = 'Semua', certQuery = '';
  var cntEl = $('certCnt'); if (cntEl) cntEl.textContent = two(CERTS.length) + ' sertifikat';

  function drawCerts(){
    var names = ['Semua'];
    CERTS.forEach(function(c){ if (c.k && names.indexOf(c.k) < 0) names.push(c.k); });
    $('filt').innerHTML = names.map(function(n){
      var cnt = n === 'Semua' ? CERTS.length : CERTS.filter(function(c){ return c.k === n; }).length;
      return '<button type="button" role="tab" aria-selected="' + (n === certGroup) + '" class="' + (n === certGroup ? 'on' : '') + '" data-k="' + esc(n) + '">' + esc(n) + '<i>' + cnt + '</i></button>';
    }).join('');

    var q = certQuery.toLowerCase();
    var html = CERTS.map(function(c, i){
      if (certGroup !== 'Semua' && c.k !== certGroup) return '';
      if (q && (c.t + ' ' + (c.c || '') + ' ' + c.s + ' ' + c.k).toLowerCase().indexOf(q) < 0) return '';
      var f = certFile(c), isImg = IMG_RE.test(f), isPdf = PDF_RE.test(f);
      var badge = '<span class="c-badge">' + esc(c.c || c.k) + '</span>';
      var th = isImg
        ? '<span class="th">' + badge + '<img src="' + esc(f) + '" alt="Sertifikat ' + esc(c.t) + '" loading="lazy"></span>'
        : (isPdf ? '<span class="th pdf" data-yr="' + esc(String(c.y).slice(-4)) + '">' + badge + '<b>LIHAT PDF</b></span>' : '');
      var verBtn = c.u ? '<a class="c-ver" href="' + esc(c.u) + '" target="_blank" rel="noopener" onclick="event.stopPropagation()">Verifikasi ↗</a>' : '';
      return '<div class="cert' + (c.featured ? ' featured' : '') + '" data-i="' + i + '" role="button" tabindex="0">' +
        th +
        '<div class="c-body">' +
          '<div class="c-meta"><span>' + esc(c.s) + '</span><time>' + esc(c.y) + '</time></div>' +
          '<b>' + esc(c.t) + '</b>' +
          '<div class="c-foot"><em>Pratinjau Dokumen →</em>' + verBtn + '</div>' +
        '</div>' +
      '</div>';
    }).join('');

    $('certs').innerHTML = html || '<p class="sub" style="grid-column:1/-1">Tidak ada sertifikat yang cocok dengan pencarian.</p>';

    $('certs').querySelectorAll('.cert').forEach(function(card){
      card.addEventListener('pointermove', function(e){
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

  $('filt').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    certGroup = b.getAttribute('data-k'); drawCerts();
  });
  var sInp = $('certSearch');
  if (sInp) sInp.addEventListener('input', function(){ certQuery = sInp.value.trim(); drawCerts(); });
  drawCerts();

  /* Lightbox Pembesaran PDF / Gambar */
  (function(){
    var lb = document.createElement('div'); lb.className = 'lb';
    lb.innerHTML = '<button type="button" class="lx" aria-label="Tutup">×</button><img alt=""><iframe title="Sertifikat" hidden></iframe><div class="lb-acts"><a class="b w" id="lbOpen" target="_blank" rel="noopener">Buka File Penuh</a><a class="b o" id="lbVer" target="_blank" rel="noopener" hidden>Verifikasi Resmi ↗</a></div>';
    document.body.appendChild(lb);
    var im = lb.querySelector('img'), fr = lb.querySelector('iframe'), ln = $('lbOpen'), vr = $('lbVer');
    function close(){ lb.classList.remove('on'); fr.removeAttribute('src'); document.body.classList.remove('lock'); }
    function openCard(a){
      var c = CERTS[+a.getAttribute('data-i')]; if (!c) return;
      var f = certFile(c); if (!f) return;
      var isImg = IMG_RE.test(f), isPdf = PDF_RE.test(f);
      if (isPdf && window.innerWidth < 700) { window.open(f, '_blank'); return; }
      if (!isImg && !isPdf) return;
      im.hidden = !isImg; fr.hidden = !isPdf;
      if (isImg) im.src = f; else fr.src = f + '#toolbar=0&navpanes=0';
      ln.href = f;
      if (c.u) { vr.href = c.u; vr.hidden = false; } else { vr.hidden = true; }
      lb.classList.add('on'); document.body.classList.add('lock');
    }
    $('certs').addEventListener('click', function(e){
      if (e.target.closest('.c-ver')) return;
      var a = e.target.closest('.cert'); if (a) openCard(a);
    });
    $('certs').addEventListener('keydown', function(e){
      if (e.key === 'Enter' || e.key === ' ') {
        var a = e.target.closest('.cert');
        if (a && !e.target.closest('.c-ver')) { e.preventDefault(); openCard(a); }
      }
    });
    lb.addEventListener('click', function(e){ if (e.target === lb || e.target.className === 'lx') close(); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape') close(); });
  })();
} catch (e) { showProblem('sertifikat: ' + e.message); } }
