"""Update TOC, cross-references, and page-number fields in a DOCX via LibreOffice UNO.

Usage (run with LibreOffice's bundled Python, not system Python):
  "C:\\Program Files\\LibreOffice\\program\\python.exe" update-fields.py <docx-path> <profile-dir>

Spawns a local LibreOffice listener, connects via UNO, opens the docx, refreshes
all fields + indexes twice (so TOC page numbers reflect final layout), saves,
closes.
"""

import os
import sys
import time
import subprocess

def main():
    if len(sys.argv) < 3:
        print("Usage: update-fields.py <docx-path> <profile-dir>", file=sys.stderr)
        sys.exit(2)

    docx = os.path.abspath(sys.argv[1])
    profile = os.path.abspath(sys.argv[2])
    doc_url = 'file:///' + docx.replace('\\', '/')
    profile_url = 'file:///' + profile.replace('\\', '/')

    soffice = r'C:\Program Files\LibreOffice\program\soffice.exe'
    port = 2517  # arbitrary, unlikely-collision port

    proc = subprocess.Popen([
        soffice,
        '--headless', '--norestore', '--nofirststartwizard', '--nologo',
        f'-env:UserInstallation={profile_url}',
        f'--accept=socket,host=localhost,port={port};urp;',
    ])

    try:
        # Wait for listener to be ready
        import uno
        from com.sun.star.beans import PropertyValue

        local_ctx = uno.getComponentContext()
        resolver = local_ctx.ServiceManager.createInstanceWithContext(
            'com.sun.star.bridge.UnoUrlResolver', local_ctx)

        ctx = None
        for attempt in range(30):
            try:
                ctx = resolver.resolve(
                    f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext')
                break
            except Exception:
                time.sleep(0.5)
        if ctx is None:
            print('Could not connect to LibreOffice listener', file=sys.stderr)
            sys.exit(1)

        smgr = ctx.ServiceManager
        desktop = smgr.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)

        # Open the DOCX
        hidden = PropertyValue()
        hidden.Name = 'Hidden'
        hidden.Value = True
        doc = desktop.loadComponentFromURL(doc_url, '_blank', 0, (hidden,))
        if doc is None:
            print(f'Failed to open {doc_url}', file=sys.stderr)
            sys.exit(1)

        # Refresh fields (PAGE, STYLEREF, etc.), then indexes (TOC), then fields again
        doc.getTextFields().refresh()
        indexes = doc.getDocumentIndexes()
        for i in range(indexes.Count):
            indexes.getByIndex(i).update()
        doc.getTextFields().refresh()

        # Save back to same path
        fn = PropertyValue()
        fn.Name = 'FilterName'
        fn.Value = 'MS Word 2007 XML'
        ow = PropertyValue()
        ow.Name = 'Overwrite'
        ow.Value = True
        doc.storeToURL(doc_url, (fn, ow))
        doc.close(False)

        print(f'Updated fields in {docx}')

    finally:
        try:
            proc.terminate()
            proc.wait(timeout=10)
        except Exception:
            proc.kill()


if __name__ == '__main__':
    main()
