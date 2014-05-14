from captionstransformer import sbv, srt, transcript, ttml, vtt

REGISTRY = {
            'transcript':{'id': 'transcript',
                          'reader': transcript.Reader,
                          'writer': transcript.Writer,
                          'mimetype': 'text/xml',
                          'extension': '.xml'},
            'TTML':{'id': 'TTML',
                    'reader': ttml.Reader,
                    'writer': ttml.Writer,
                    'mimetype': 'application/ttml+xml',
                    'extension': '.xml'},
            'SBV': {'id': 'SBV',
                    'reader': sbv.Reader,
                    'writer': sbv.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.sbv'},
            'SRT': {'id': 'SRT',
                    'reader': srt.Reader,
                    'writer': srt.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.srt'},
            'VTT': {'id': 'VTT',
                    'reader': vtt.Reader,
                    'writer': vtt.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.srt'}}
