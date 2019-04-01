{
  "targets": [
    {
      "target_name": "detection",
      "sources": [
        "src/detection.cpp",
        "src/detection.h",
        "src/deviceList.cpp"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
      'conditions': [
        ['OS=="win"',
          {
            'sources': [
              "src/detection_win.cpp"
            ],
            'include_dirs+':
            [
              # Not needed now
            ],
            'configurations': {
              'Debug': {
                'defines': [ 'DEBUG', '_DEBUG' ],
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'RuntimeLibrary': 1, # static debug
                  },
                },
              },
              'Release': {
                'defines': [ 'NDEBUG' ],
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'RuntimeLibrary': 0, # static release
                  },
                },
              }
            }
          }
        ],
        ['OS=="mac"',
          {
            'sources': [
              "src/detection_mac.cpp"
            ],
            "libraries": [
              "-framework",
              "IOKit"
            ]
          }
        ],
        ['OS=="linux"',
          {
            'sources': [
              "src/detection_linux.cpp"
            ],
            'link_settings': {
              'libraries': [
                '-ludev'
              ]
            }
          }
        ]
      ]
    }
  ]
}
