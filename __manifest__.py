{
    'name': 'clinic',
    'version': '1.0',
    'author': 'all',
    'summary': 'module clinic',
    'description': """ MODULE CLINIC TERKAIT PERIZINAN """,
    'application': True,
    'depends': ['base'],
    'data' : [
      'views/pasien_umum.xml',
      'views/pasien_gigi.xml',
      'views/konfirmasi_gigi.xml',
      'views/konfirmasi_umum.xml',
      'views/status_gigi.xml',
      'views/status_umum.xml',
      'report/report_gigi.xml',
      'report/surat_gigi.xml',
      'report/report_umum.xml',
      'report/surat_umum.xml',
      'data/gigi.xml',
      'data/umum.xml',
      'security/ir.model.access.csv'
    ]
}

