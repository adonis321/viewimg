from enum import Enum, unique

img_formats = ["T_Y8_1P",                               # 0
                "T_B5G6R5_1P",                          # 1
                "T_R5G6B5_1P",                          # 2
                "T_B8_G8_R8_1P",                        # 3
                "T_R8_G8_B8_1P",                        # 4
                "T_A8B8G8R8_1P",                        # 5
                "T_X8B8G8R8_1P",                        # 6
                "T_A8R8G8B8_1P",                        # 7
                "T_X8R8G8B8_1P",                        # 8
                "T_B8G8R8A8_1P",                        # 9
                "T_B8G8R8X8_1P",                        # 10
                "T_R8G8B8A8_1P",                        # 11
                "T_R8G8B8X8_1P",                        # 12
                "T_A2B10G10R10_1P",                      # 13
                "T_X2B10G10R10_1P",                      # 14
                "T_A2R10G10B10_1P",                      # 15
                "T_X2R10G10B10_1P",                      # 16
                "T_B10G10R10A2_1P",                      # 17
                "T_B10G10R10X2_1P",                      # 18
                "T_R10G10B10A2_1P",                      # 19
                "T_R10G10B10X2_1P",                      # 20
                "T_A16B16G16R16_F_1P",                      # 21
                "T_X16B16G16R16_F_1P",                      # 22
                "T_A16R16G16B16_F_1P",                      # 23
                "T_X16R16G16B16_F_1P",                      # 24
                "T_B16G16R16A16_F_1P",                      # 25
                "T_B16G16R16X16_F_1P",                       # 26
                "T_R16G16B16A16_F_1P",                       # 27
                "T_R16G16B16X16_F_1P",                       # 28
                "T_A8Y8V8U8_1P",                             # 29
                "T_X8Y8V8U8_1P",                             # 30
                "T_A8Y8U8V8_1P",                             # 31
                "T_X8Y8U8V8_1P",                             # 32
                "AYUV_1P",                                   # 33
                "T_A2U10Y10V10_1P",                          # 34
                "T_X2U10Y10V10_1P",                          # 35
                "Y410_1P",                                   # 36
                "T_A2V10Y10U10_1P",                          # 37
                "T_X2V10Y10U10_1P",                          # 38
                "T_Y8_U8__Y8_V8_1P",                         # 39
                "YUY2_1P",                                   # 40
                "T_Y8_V8__Y8_U8_1P",                         # 41
                "T_U8_Y8__V8_Y8_1P",                         # 42
                "UYVY_1P",                                   # 43
                "T_V8_Y8__U8_Y8_1P",                         # 44
                "T_Y10_U10__Y10_V10_1P",                     # 45
                "Y210_1P",                                   # 46
                "T_Y10_V10__Y10_U10_1P",                     # 47
                "T_U10_Y10__V10_Y10_1P",                     # 48
                "T_V10_Y10__U10_Y10_1P",                     # 49
                "T_Y8___U8___V8_N420_3P",                    # 50
                "YV12_3P",                                   # 51
                "T_Y8___V8___U8_N420_3P",                    # 52
                "T_Y8___U8___V8_N422_3P",                    # 53
                "YV16_3P",                                   # 54
                "T_Y8___V8___U8_N422_3P",                    # 55
                "T_Y8___U8___V8_N444_3P",                    # 56
                "YV24_3P",                                   # 57
                "T_Y8___V8___U8_N444_3P",                    # 58
                "T_R8___G8___B8_3P",                         # 59
                "T_B8___G8___R8_3P",                         # 60
                "T_R16___G16___B16_F_3P",                    # 61
                "T_B16___G16___R16_F_3P",                    # 62
                "T_Y8___U8V8_N420_2P",                       # 63
                "NV12_2P",                                   # 64
                "T_Y8___V8U8_N420_2P",                       # 65
                "T_Y8___U8V8_N422_2P",                       # 66
                "NV16_2P",                                   # 67
                "T_Y8___V8U8_N422_2P",                       # 68
                "T_Y8___U8V8_N444_2P",                       # 69
                "NV24_2P",                                   # 70
                "T_Y8___V8U8_N444_2P",                       # 71
                "T_Y10___U10V10_N420_2P",                    # 72
                "P010_2P",                                   # 73
                "T_Y10___V10U10_N420_2P",                    # 74
                "T_Y10___U10V10_N422_2P",                    # 75
                "P210_2P",                                   # 76
                "T_Y10___V10U10_N422_2P",                    # 77
                "T_Y10___U10V10_N444_2P",                    # 78
                "T_Y10___V10U10_N444_2P",                    # 79
                "MTK_Y10__U10V10",                           # 80
                "MTK_Y10__V10U10",                           # 81
                "MTK_U10_Y10__V10_Y10",                      # 82
                "MTK_V10_Y10__U10_Y10"]                      # 83

@unique
class Format_info(Enum):
    T_Y8_1P                 =	0
    T_B5G6R5_1P	            =	1
    T_R5G6B5_1P	            =	2
    T_B8_G8_R8_1P	        =	3
    T_R8_G8_B8_1P	        =	4
    T_A8B8G8R8_1P	        =	5
    T_X8B8G8R8_1P	        =	6
    T_A8R8G8B8_1P	        =	7
    T_X8R8G8B8_1P	        =	8
    T_B8G8R8A8_1P	        =	9
    T_B8G8R8X8_1P 	        =	10
    T_R8G8B8A8_1P	        =	11
    T_R8G8B8X8_1P	        =	12
    T_A2B10G10R10_1P	    =	13
    T_X2B10G10R10_1P 	    =	14
    T_A2R10G10B10_1P	    =	15
    T_X2R10G10B10_1P	    =	16
    T_B10G10R10A2_1P	    =	17
    T_B10G10R10X2_1P	    =	18
    T_R10G10B10A2_1P	    =	19
    T_R10G10B10X2_1P	    =	20
    T_A16B16G16R16_F_1P	    =	21
    T_X16B16G16R16_F_1P	    =	22
    T_A16R16G16B16_F_1P	    =	23
    T_X16R16G16B16_F_1P	    =	24
    T_B16G16R16A16_F_1P	    =	25
    T_B16G16R16X16_F_1P	    =	26
    T_R16G16B16A16_F_1P	    =	27
    T_R16G16B16X16_F_1P	    =	28
    T_A8Y8V8U8_1P	        =	29
    T_X8Y8V8U8_1P	        =	30
    T_A8Y8U8V8_1P	        =	31
    T_X8Y8U8V8_1P           =   32
    AYUV_1P                 =	33
    T_A2U10Y10V10_1P	    =	34
    T_X2U10Y10V10_1P        =   35
    Y410_1P	                =	36
    T_A2V10Y10U10_1P	    =	37
    T_X2V10Y10U10_1P	    =	38
    T_Y8_U8__Y8_V8_1P       =   39 
    YUY2_1P	                =	40
    T_Y8_V8__Y8_U8_1P	    =	41
    T_U8_Y8__V8_Y8_1P       =   42
    UYVY_1P	                =	43
    T_V8_Y8__U8_Y8_1P 	    =	44
    T_Y10_U10__Y10_V10_1P   =   45
    Y210_1P	                =	46
    T_Y10_V10__Y10_U10_1P	=	47
    T_U10_Y10__V10_Y10_1P 	=	48
    T_V10_Y10__U10_Y10_1P 	=	49
    T_Y8___U8___V8_N420_3P  =   50
    YV12_3P	                =	51
    T_Y8___V8___U8_N420_3P 	=	52
    T_Y8___U8___V8_N422_3P  =   53
    YV16_3P	                =	54
    T_Y8___V8___U8_N422_3P 	=	55
    T_Y8___U8___V8_N444_3P  =   56
    YV24_3P	                =	57
    T_Y8___V8___U8_N444_3P  =	58
    T_R8___G8___B8_3P  	    =	59
    T_B8___G8___R8_3P     	=	60
    T_R16___G16___B16_F_3P  =	61
    T_B16___G16___R16_F_3P 	=	62
    T_Y8___U8V8_N420_2P     =   63
    NV12_2P	                =	64
    T_Y8___V8U8_N420_2P     =   65
    T_Y8___U8V8_N422_2P     =   66
    NV16_2P	                =	67
    T_Y8___V8U8_N422_2P	    =	68
    T_Y8___U8V8_N444_2P     =   69
    NV24_2P	                =	70
    T_Y8___V8U8_N444_2P     =	71
    T_Y10___U10V10_N420_2P  =   72
    P010_2P	                =	73
    T_Y10___V10U10_N420_2P  =	74
    T_Y10___U10V10_N422_2P  =   75
    P210_2P	                =	76
    T_Y10___V10U10_N422_2P 	=	77
    T_Y10___U10V10_N444_2P 	=	78
    T_Y10___V10U10_N444_2P 	=	79
    MTK_Y10__U10V10 	    =	80
    MTK_Y10__V10U10 	    =	81
    MTK_U10_Y10__V10_Y10 	=	82
    MTK_V10_Y10__U10_Y10 	=	83

formatdict = {
        0:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        YYYYYYYY
        """,
        1:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:       
        RDMA need enable B/R SWAP
        BBBBBGGGGGGRRRRR
        """,
        2:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRGGGGGGBBBBB
        """,
        3:"""
        BPP(Bytes Per Pixel):3 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        BBBBBBBBGGGGGGGGRRRRRRRR
        """,
        4:"""
        BPP(Bytes Per Pixel):3 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRGGGGGGGGBBBBBBBB
        """,
        5:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        AAAAAAAABBBBBBBBGGGGGGGGRRRRRRRR
        """,
        6:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        XXXXXXXXBBBBBBBBGGGGGGGGRRRRRRRR
        """,
        7:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AAAAAAAARRRRRRRRGGGGGGGGBBBBBBBB
        """,
        8:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        XXXXXXXXRRRRRRRRGGGGGGGGBBBBBBBB
        """,
        9:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        BBBBBBBBGGGGGGGGRRRRRRRRAAAAAAAA
        """,
        10:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        BBBBBBBBGGGGGGGGRRRRRRRRXXXXXXXX
        """,
        11:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRGGGGGGGGBBBBBBBBAAAAAAAA
        """,
        12:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRGGGGGGGGBBBBBBBBXXXXXXXX
        """,
        13:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        AABBBBBBBBBBGGGGGGGGGGRRRRRRRRRR
        """,
        14:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        XXBBBBBBBBBBGGGGGGGGGGRRRRRRRRRR
        """,
        15:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AARRRRRRRRRRGGGGGGGGGGBBBBBBBBBB
        """,
        16:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        XXRRRRRRRRRRGGGGGGGGGGBBBBBBBBBB
        """,
        17:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        BBBBBBBBBBGGGGGGGGGGRRRRRRRRRRAA
        """,
        18:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        BBBBBBBBBBGGGGGGGGGGRRRRRRRRRRXX
        """,
        19:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRRRGGGGGGGGGGBBBBBBBBBBAA
        """,
        20:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRRRGGGGGGGGGGBBBBBBBBBBXX
        """,
        21:"""
        BPP(Bytes Per Pixel):8 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBGGGGGGGGGGGGGGGGRRRRRRRRRRRRRRRR
        """,
        22:"""
        BPP(Bytes Per Pixel):8 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable B/R SWAP
        XXXXXXXXXXXXXXXXBBBBBBBBBBBBBBBBGGGGGGGGGGGGGGGGRRRRRRRRRRRRRRRR
        """,
        23:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBB
        """,
        24:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        XXXXXXXXXXXXXXXXRRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBB
        """,
        25:"""
        BPP(Bytes Per Pixel):8 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        BBBBBBBBBBBBBBBBGGGGGGGGGGGGGGGGRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAA
        """,
        26:"""
        BPP(Bytes Per Pixel):8 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        BBBBBBBBBBBBBBBBGGGGGGGGGGGGGGGGRRRRRRRRRRRRRRRRXXXXXXXXXXXXXXXX
        """,
        27:"""
        BPP(Bytes Per Pixel):8 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAA
        """,
        28:"""
        BPP(Bytes Per Pixel):8 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBXXXXXXXXXXXXXXXX
        """,
        29:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable UV SWAP
        AAAAAAAAYYYYYYYYVVVVVVVVUUUUUUUU
        """,
        30:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA needs enable UV SWAP
        XXXXXXXXYYYYYYYYVVVVVVVVUUUUUUUU
        """,
        31:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AAAAAAAAYYYYYYYYUUUUUUUUVVVVVVVV
        """,
        32:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        XXXXXXXXYYYYYYYYUUUUUUUUVVVVVVVV
        """,
        33:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AAAAAAAAYYYYYYYYUUUUUUUUVVVVVVVV
        """,
        34:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable UV SWAP
        AAUUUUUUUUUUYYYYYYYYYYVVVVVVVVVV
        """,
        35:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        RDMA need enable UV SWAP
        XXUUUUUUUUUUYYYYYYYYYYVVVVVVVVVV
        """,
        36:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AAUUUUUUUUUUYYYYYYYYYYVVVVVVVVVV
        """,
        37:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        AAVVVVVVVVVVYYYYYYYYYYUUUUUUUUUU
        """,
        38:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:
        XXVVVVVVVVVVYYYYYYYYYYUUUUUUUUUU
        """,
        39:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        YYYYYYYY UUUUUUUU YYYYYYYY VVVVVVVV
        """,
        40:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        YYYYYYYY UUUUUUUU YYYYYYYY VVVVVVVV
        """,
        41:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        RDMA need enable UV SWAP
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        YYYYYYYY VVVVVVVV YYYYYYYY UUUUUUUU
        """,
        42:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        UUUUUUUU YYYYYYYY VVVVVVVV YYYYYYYY
        """,
        43:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        UUUUUUUU YYYYYYYY VVVVVVVV YYYYYYYY
        """,
        44:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        RDMA need enable UV SWAP
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        VVVVVVVV YYYYYYYY UUUUUUUU YYYYYYYY
        """,
        45:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        YYYYYYYYYY000000 UUUUUUUUUU000000 YYYYYYYYYY000000 VVVVVVVVVV000000
        """,
        46:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        YYYYYYYYYY000000 UUUUUUUUUU000000 YYYYYYYYYY000000 VVVVVVVVVV000000
        """,
        47:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        RDMA need enable UV SWAP
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        YYYYYYYYYY000000 VVVVVVVVVV000000 YYYYYYYYYY000000 UUUUUUUUUU000000
        """,
        48:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        UUUUUUUUUU000000 YYYYYYYYYY000000 VVVVVVVVVV000000 YYYYYYYYYY000000
        """,
        49:"""
        BPP(Bytes Per Pixel):4 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 packed)
        RDMA need enable UV SWAP
        (从左往右: Left to Right: LS-Byte to MS-Byte, ms-bit to ls-bit per Byte)
        VVVVVVVVVV000000 YYYYYYYYYY000000 UUUUUUUUUU000000 YYYYYYYYYY000000
        """,
        50:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV420 full planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUU 
        Plane2: VVVVVVVV
        """,
        51:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV420 full planar)
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVV 
        Plane2: UUUUUUUU
        """,
        52:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV420 full planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVV 
        Plane2: UUUUUUUU
        """,
        53:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV422 full planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUU 
        Plane2: VVVVVVVV
        """,
        54:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV422 full planar)
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVV 
        Plane2: UUUUUUUU
        """,
        55:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV422 full planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVV 
        Plane2: UUUUUUUU
        """,
        56:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV444 full planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUU 
        Plane2: VVVVVVVV
        """,
        57:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV444 full planar)
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVV 
        Plane2: UUUUUUUU
        """,
        58:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV444 full planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVV 
        Plane2: UUUUUUUU
        """,
        59:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (RGB full planar)
        Plane0: RRRRRRRR 
        Plane1: GGGGGGGG 
        Plane2: BBBBBBBB
        """,
        60:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (RGB full planar)
        RDMA need enable BR SWAP
        Plane0: BBBBBBBB
        Plane1: GGGGGGGG 
        Plane2: RRRRRRRR 
        """,
        61:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (RGB full planar)
        Plane0: RRRRRRRRRRRRRRRR 
        Plane1: GGGGGGGGGGGGGGGG 
        Plane2: BBBBBBBBBBBBBBBB
        """,
        62:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (RGB full planar)
        RDMA need enable BR SWAP
        Plane0: BBBBBBBBBBBBBBBB
        Plane1: GGGGGGGGGGGGGGGG 
        Plane2: RRRRRRRRRRRRRRRR
        """,
        63:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV420 semi-planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUUVVVVVVVV
        """,
        64:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV420 semi-planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUUVVVVVVVV
        """,
        65:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV420 semi-planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVVUUUUUUUU
        """,
        66:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 semi-planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUUVVVVVVVV
        """,
        67:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 semi-planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUUVVVVVVVV
        """,
        68:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 semi-planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVVUUUUUUUU
        """,
        69:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV444 semi-planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUUVVVVVVVV
        """,
        70:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV444 semi-planar)
        Plane0: YYYYYYYY 
        Plane1: UUUUUUUUVVVVVVVV
        """,
        71:"""
        BPP(Bytes Per Pixel):1 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV444 semi-planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYY 
        Plane1: VVVVVVVVUUUUUUUU
        """,
        72:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV420 semi-planar)
        Plane0: YYYYYYYYYY000000 
        Plane1: UUUUUUUUUU000000VVVVVVVVVV000000
        """,
        73:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV420 semi-planar)
        Plane0: YYYYYYYYYY000000 
        Plane1: UUUUUUUUUU000000VVVVVVVVVV000000
        """,
        74:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV420 semi-planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYYYY000000 
        Plane1: VVVVVVVVVV000000UUUUUUUUUU000000
        """,
        75:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 semi-planar)
        Plane0: YYYYYYYYYY000000 
        Plane1: UUUUUUUUUU000000VVVVVVVVVV000000
        """,
        76:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 semi-planar)
        Plane0: YYYYYYYYYY000000 
        Plane1: UUUUUUUUUU000000VVVVVVVVVV000000
        """,
        77:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV422 semi-planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYYYY000000 
        Plane1: VVVVVVVVVV000000UUUUUUUUUU000000
        """,
        78:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV444 semi-planar)
        Plane0: YYYYYYYYYY000000 
        Plane1: UUUUUUUUUU000000VVVVVVVVVV000000
        """,
        79:"""
        BPP(Bytes Per Pixel):2 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式: (YUV444 semi-planar)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYYYY000000 
        Plane1: VVVVVVVVVV000000UUUUUUUUUU000000
        """,
        80:"""
        BPP(Bytes Per Pixel):1.25 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV420 SP*)
        Plane0: YYYYYYYYYYYY
        Plane1: UUUUUUUUUUUUVVVVVVVVVVVV
        """,
        81:"""
        BPP(Bytes Per Pixel):1.25 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:0(YUV420 SP*)
        RDMA need enable UV SWAP
        Plane0: YYYYYYYYYYYY
        Plane1: VVVVVVVVVVVVUUUUUUUUUUUU
        """,
        82:"""
        BPP(Bytes Per Pixel):2.5 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV422 I)
        UUUUUUUUUU YYYYYYYYYY VVVVVVVVVV YYYYYYYYYY
        """,
        83:"""
        BPP(Bytes Per Pixel):2.5 Bytes
        MSB(Most Significant Bit):最高有效位
        LSB(Least Significant Bit):最低有效位
        排列方式:(YUV422 I)
        RDMA need enable UV SWAP
        VVVVVVVVVV YYYYYYYYYY UUUUUUUUUU YYYYYYYYYY
        """,
}

def format_info(format_info):
    info = 0
    for index,value in enumerate(img_formats):
        if value == format_info:
            print(index,value)
            info = formatdict.get(index,"Invalid format")
    
    return info

