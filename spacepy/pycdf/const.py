#!/usr/bin/env python
"""CDF constants

Various constants defined in cdf.h and used in pycdf
"""

__version__ = "0.5"
__author__ = "Jonathan Niehof <jniehof@lanl.gov>"

import ctypes

# Generated by h2py from cdf.h
# Regeneration process:
# Edit a copy of cdf.h
# M-x replace-string (CDFstatus) with nothing
# h2py cdf.h
# Open CDF.py
# remove def lines
# M-x replace-string ( with nothing, also ) with nothing
# add RESERVED_CDFID = 0 before RESERVED_CDFSTATUS
# M-x replace-regexp \(-?[0-9]+\)L with: ctypes.c_long(\1)
# mark EPOCH as double: ILLEGAL_EPOCH_VALUE = ctypes.c_double(-1.0)

CDF_MIN_DIMS = 0
CDF_MAX_DIMS = 10
CDF_VAR_NAME_LEN = 64
CDF_ATTR_NAME_LEN = 64
CDF_VAR_NAME_LEN256 = 256
CDF_ATTR_NAME_LEN256 = 256
CDF_COPYRIGHT_LEN = 256
CDF_STATUSTEXT_LEN = 120
CDF_PATHNAME_LEN = 512
EPOCH_STRING_LEN = 24
EPOCH1_STRING_LEN = 16
EPOCH2_STRING_LEN = 14
EPOCH3_STRING_LEN = 24
EPOCH16_STRING_LEN = 36
EPOCH16_1_STRING_LEN = 24
EPOCH16_2_STRING_LEN = 14
EPOCH16_3_STRING_LEN = 36
EPOCHx_STRING_MAX = 50
EPOCHx_FORMAT_MAX = 68
CDF_INT1 = ctypes.c_long(1)
CDF_INT2 = ctypes.c_long(2)
CDF_INT4 = ctypes.c_long(4)
CDF_UINT1 = ctypes.c_long(11)
CDF_UINT2 = ctypes.c_long(12)
CDF_UINT4 = ctypes.c_long(14)
CDF_REAL4 = ctypes.c_long(21)
CDF_REAL8 = ctypes.c_long(22)
CDF_EPOCH = ctypes.c_long(31)
CDF_EPOCH16 = ctypes.c_long(32)
CDF_BYTE = ctypes.c_long(41)
CDF_FLOAT = ctypes.c_long(44)
CDF_DOUBLE = ctypes.c_long(45)
CDF_CHAR = ctypes.c_long(51)
CDF_UCHAR = ctypes.c_long(52)
NETWORK_ENCODING = ctypes.c_long(1)
SUN_ENCODING = ctypes.c_long(2)
VAX_ENCODING = ctypes.c_long(3)
DECSTATION_ENCODING = ctypes.c_long(4)
SGi_ENCODING = ctypes.c_long(5)
IBMPC_ENCODING = ctypes.c_long(6)
IBMRS_ENCODING = ctypes.c_long(7)
HOST_ENCODING = ctypes.c_long(8)
PPC_ENCODING = ctypes.c_long(9)
HP_ENCODING = ctypes.c_long(11)
NeXT_ENCODING = ctypes.c_long(12)
ALPHAOSF1_ENCODING = ctypes.c_long(13)
ALPHAVMSd_ENCODING = ctypes.c_long(14)
ALPHAVMSg_ENCODING = ctypes.c_long(15)
ALPHAVMSi_ENCODING = ctypes.c_long(16)
NETWORK_DECODING = NETWORK_ENCODING
SUN_DECODING = SUN_ENCODING
VAX_DECODING = VAX_ENCODING
DECSTATION_DECODING = DECSTATION_ENCODING
SGi_DECODING = SGi_ENCODING
IBMPC_DECODING = IBMPC_ENCODING
IBMRS_DECODING = IBMRS_ENCODING
HOST_DECODING = HOST_ENCODING
PPC_DECODING = PPC_ENCODING
MAC_ENCODING = PPC_ENCODING
MAC_DECODING = PPC_ENCODING
HP_DECODING = HP_ENCODING
NeXT_DECODING = NeXT_ENCODING
ALPHAOSF1_DECODING = ALPHAOSF1_ENCODING
ALPHAVMSd_DECODING = ALPHAVMSd_ENCODING
ALPHAVMSg_DECODING = ALPHAVMSg_ENCODING
ALPHAVMSi_DECODING = ALPHAVMSi_ENCODING
VARY = ctypes.c_long(-1)
NOVARY = ctypes.c_long(0)
ROW_MAJOR = ctypes.c_long(1)
COLUMN_MAJOR = ctypes.c_long(2)
SINGLE_FILE = ctypes.c_long(1)
MULTI_FILE = ctypes.c_long(2)
NO_CHECKSUM = ctypes.c_long(0)
MD5_CHECKSUM = ctypes.c_long(1)
OTHER_CHECKSUM = ctypes.c_long(2)
GLOBAL_SCOPE = ctypes.c_long(1)
VARIABLE_SCOPE = ctypes.c_long(2)
READONLYon = ctypes.c_long(-1)
READONLYoff = ctypes.c_long(0)
VALIDATEFILEon = ctypes.c_long(-1)
VALIDATEFILEoff = ctypes.c_long(0)
zMODEoff = ctypes.c_long(0)
zMODEon1 = ctypes.c_long(1)
zMODEon2 = ctypes.c_long(2)
NEGtoPOSfp0on = ctypes.c_long(-1)
NEGtoPOSfp0off = ctypes.c_long(0)
BACKWARDFILEon = 1
BACKWARDFILEoff = 0
CDF_MAX_PARMS = 5
NO_COMPRESSION = ctypes.c_long(0)
RLE_COMPRESSION = ctypes.c_long(1)
HUFF_COMPRESSION = ctypes.c_long(2)
AHUFF_COMPRESSION = ctypes.c_long(3)
GZIP_COMPRESSION = ctypes.c_long(5)
RLE_OF_ZEROs = ctypes.c_long(0)
OPTIMAL_ENCODING_TREES = ctypes.c_long(0)
NO_SPARSEARRAYS = ctypes.c_long(0)
NO_SPARSERECORDS = ctypes.c_long(0)
PAD_SPARSERECORDS = ctypes.c_long(1)
PREV_SPARSERECORDS = ctypes.c_long(2)
RESERVED_CDFID = 0 #Added by hand (NULL in C)
RESERVED_CDFSTATUS =  -1
ILLEGAL_EPOCH_VALUE = ctypes.c_double(-1.0)
VIRTUAL_RECORD_DATA =  1001
DID_NOT_COMPRESS =  1002
VAR_ALREADY_CLOSED =  1003
SINGLE_FILE_FORMAT =  1004
NO_PADVALUE_SPECIFIED =  1005
NO_VARS_IN_CDF =  1006
MULTI_FILE_FORMAT =  1007
SOME_ALREADY_ALLOCATED =  1008
PRECEEDING_RECORDS_ALLOCATED =  1009
CDF_OK =  0
ATTR_NAME_TRUNC =  -1001
CDF_NAME_TRUNC =  -1002
VAR_NAME_TRUNC =  -1003
NEGATIVE_FP_ZERO =  -1004
FORCED_PARAMETER =  -1006
NA_FOR_VARIABLE =  -1007
CDF_WARN =  -2000
ATTR_EXISTS =  -2001
BAD_CDF_ID =  -2002
BAD_DATA_TYPE =  -2003
BAD_DIM_SIZE =  -2004
BAD_DIM_INDEX =  -2005
BAD_ENCODING =  -2006
BAD_MAJORITY =  -2007
BAD_NUM_DIMS =  -2008
BAD_REC_NUM =  -2009
BAD_SCOPE =  -2010
BAD_NUM_ELEMS =  -2011
CDF_OPEN_ERROR =  -2012
CDF_EXISTS =  -2013
BAD_FORMAT =  -2014
BAD_ALLOCATE_RECS =  -2015
BAD_CDF_EXTENSION =  -2016
NO_SUCH_ATTR =  -2017
NO_SUCH_ENTRY =  -2018
NO_SUCH_VAR =  -2019
VAR_READ_ERROR =  -2020
VAR_WRITE_ERROR =  -2021
BAD_ARGUMENT =  -2022
IBM_PC_OVERFLOW =  -2023
TOO_MANY_VARS =  -2024
VAR_EXISTS =  -2025
BAD_MALLOC =  -2026
NOT_A_CDF =  -2027
CORRUPTED_V2_CDF =  -2028
VAR_OPEN_ERROR =  -2029
BAD_INITIAL_RECS =  -2030
BAD_BLOCKING_FACTOR =  -2031
END_OF_VAR =  -2032
BAD_CDFSTATUS =  -2034
CDF_INTERNAL_ERROR =  -2035
BAD_NUM_VARS =  -2036
BAD_REC_COUNT =  -2037
BAD_REC_INTERVAL =  -2038
BAD_DIM_COUNT =  -2039
BAD_DIM_INTERVAL =  -2040
BAD_VAR_NUM =  -2041
BAD_ATTR_NUM =  -2042
BAD_ENTRY_NUM =  -2043
BAD_ATTR_NAME =  -2044
BAD_VAR_NAME =  -2045
NO_ATTR_SELECTED =  -2046
NO_ENTRY_SELECTED =  -2047
NO_VAR_SELECTED =  -2048
BAD_CDF_NAME =  -2049
CANNOT_CHANGE =  -2051
NO_STATUS_SELECTED =  -2052
NO_CDF_SELECTED =  -2053
READ_ONLY_DISTRIBUTION =  -2054
CDF_CLOSE_ERROR =  -2055
VAR_CLOSE_ERROR =  -2056
BAD_FNC_OR_ITEM =  -2058
ILLEGAL_ON_V1_CDF =  -2060
BAD_CACHE_SIZE =  -2063
CDF_CREATE_ERROR =  -2066
NO_SUCH_CDF =  -2067
VAR_CREATE_ERROR =  -2068
READ_ONLY_MODE =  -2070
ILLEGAL_IN_zMODE =  -2071
BAD_zMODE =  -2072
BAD_READONLY_MODE =  -2073
CDF_READ_ERROR =  -2074
CDF_WRITE_ERROR =  -2075
ILLEGAL_FOR_SCOPE =  -2076
NO_MORE_ACCESS =  -2077
BAD_DECODING =  -2079
BAD_NEGtoPOSfp0_MODE =  -2081
UNSUPPORTED_OPERATION =  -2082
CDF_SAVE_ERROR =  -2083
VAR_SAVE_ERROR =  -2084
NO_WRITE_ACCESS =  -2086
NO_DELETE_ACCESS =  -2087
CDF_DELETE_ERROR =  -2088
VAR_DELETE_ERROR =  -2089
UNKNOWN_COMPRESSION =  -2090
CANNOT_COMPRESS =  -2091
DECOMPRESSION_ERROR =  -2092
COMPRESSION_ERROR =  -2093
EMPTY_COMPRESSED_CDF =  -2096
BAD_COMPRESSION_PARM =  -2097
UNKNOWN_SPARSENESS =  -2098
CANNOT_SPARSERECORDS =  -2099
CANNOT_SPARSEARRAYS =  -2100
TOO_MANY_PARMS =  -2101
NO_SUCH_RECORD =  -2102
CANNOT_ALLOCATE_RECORDS =  -2103
SCRATCH_DELETE_ERROR =  -2106
SCRATCH_CREATE_ERROR =  -2107
SCRATCH_READ_ERROR =  -2108
SCRATCH_WRITE_ERROR =  -2109
BAD_SPARSEARRAYS_PARM =  -2110
BAD_SCRATCH_DIR =  -2111
NOT_A_CDF_OR_NOT_SUPPORTED =  -2113
CORRUPTED_V3_CDF =  -2223
ILLEGAL_EPOCH_FIELD =  -2224
BAD_CHECKSUM =  -2225
CHECKSUM_ERROR =  -2226
CHECKSUM_NOT_ALLOWED =  -2227
IS_A_NETCDF =  -2228
CREATE_ = ctypes.c_long(1001)
OPEN_ = ctypes.c_long(1002)
DELETE_ = ctypes.c_long(1003)
CLOSE_ = ctypes.c_long(1004)
SELECT_ = ctypes.c_long(1005)
CONFIRM_ = ctypes.c_long(1006)
GET_ = ctypes.c_long(1007)
PUT_ = ctypes.c_long(1008)
SAVE_ = ctypes.c_long(1009)
BACKWARD_ = ctypes.c_long(1010)
GETCDFFILEBACKWARD_ = ctypes.c_long(1011)
CHECKSUM_ = ctypes.c_long(1012)
GETCDFCHECKSUM_ = ctypes.c_long(1013)
VALIDATE_ = ctypes.c_long(1014)
GETCDFVALIDATE_ = ctypes.c_long(1015)
NULL_ = ctypes.c_long(1000)
CDF_ = ctypes.c_long(1)
CDF_NAME_ = ctypes.c_long(2)
CDF_ENCODING_ = ctypes.c_long(3)
CDF_DECODING_ = ctypes.c_long(4)
CDF_MAJORITY_ = ctypes.c_long(5)
CDF_FORMAT_ = ctypes.c_long(6)
CDF_COPYRIGHT_ = ctypes.c_long(7)
CDF_NUMrVARS_ = ctypes.c_long(8)
CDF_NUMzVARS_ = ctypes.c_long(9)
CDF_NUMATTRS_ = ctypes.c_long(10)
CDF_NUMgATTRS_ = ctypes.c_long(11)
CDF_NUMvATTRS_ = ctypes.c_long(12)
CDF_VERSION_ = ctypes.c_long(13)
CDF_RELEASE_ = ctypes.c_long(14)
CDF_INCREMENT_ = ctypes.c_long(15)
CDF_STATUS_ = ctypes.c_long(16)
CDF_READONLY_MODE_ = ctypes.c_long(17)
CDF_zMODE_ = ctypes.c_long(18)
CDF_NEGtoPOSfp0_MODE_ = ctypes.c_long(19)
LIB_COPYRIGHT_ = ctypes.c_long(20)
LIB_VERSION_ = ctypes.c_long(21)
LIB_RELEASE_ = ctypes.c_long(22)
LIB_INCREMENT_ = ctypes.c_long(23)
LIB_subINCREMENT_ = ctypes.c_long(24)
rVARs_NUMDIMS_ = ctypes.c_long(25)
rVARs_DIMSIZES_ = ctypes.c_long(26)
rVARs_MAXREC_ = ctypes.c_long(27)
rVARs_RECDATA_ = ctypes.c_long(28)
rVARs_RECNUMBER_ = ctypes.c_long(29)
rVARs_RECCOUNT_ = ctypes.c_long(30)
rVARs_RECINTERVAL_ = ctypes.c_long(31)
rVARs_DIMINDICES_ = ctypes.c_long(32)
rVARs_DIMCOUNTS_ = ctypes.c_long(33)
rVARs_DIMINTERVALS_ = ctypes.c_long(34)
rVAR_ = ctypes.c_long(35)
rVAR_NAME_ = ctypes.c_long(36)
rVAR_DATATYPE_ = ctypes.c_long(37)
rVAR_NUMELEMS_ = ctypes.c_long(38)
rVAR_RECVARY_ = ctypes.c_long(39)
rVAR_DIMVARYS_ = ctypes.c_long(40)
rVAR_NUMBER_ = ctypes.c_long(41)
rVAR_DATA_ = ctypes.c_long(42)
rVAR_HYPERDATA_ = ctypes.c_long(43)
rVAR_SEQDATA_ = ctypes.c_long(44)
rVAR_SEQPOS_ = ctypes.c_long(45)
rVAR_MAXREC_ = ctypes.c_long(46)
rVAR_MAXallocREC_ = ctypes.c_long(47)
rVAR_DATASPEC_ = ctypes.c_long(48)
rVAR_PADVALUE_ = ctypes.c_long(49)
rVAR_INITIALRECS_ = ctypes.c_long(50)
rVAR_BLOCKINGFACTOR_ = ctypes.c_long(51)
rVAR_nINDEXRECORDS_ = ctypes.c_long(52)
rVAR_nINDEXENTRIES_ = ctypes.c_long(53)
rVAR_EXISTENCE_ = ctypes.c_long(54)
zVARs_MAXREC_ = ctypes.c_long(55)
zVARs_RECDATA_ = ctypes.c_long(56)
zVAR_ = ctypes.c_long(57)
zVAR_NAME_ = ctypes.c_long(58)
zVAR_DATATYPE_ = ctypes.c_long(59)
zVAR_NUMELEMS_ = ctypes.c_long(60)
zVAR_NUMDIMS_ = ctypes.c_long(61)
zVAR_DIMSIZES_ = ctypes.c_long(62)
zVAR_RECVARY_ = ctypes.c_long(63)
zVAR_DIMVARYS_ = ctypes.c_long(64)
zVAR_NUMBER_ = ctypes.c_long(65)
zVAR_DATA_ = ctypes.c_long(66)
zVAR_HYPERDATA_ = ctypes.c_long(67)
zVAR_SEQDATA_ = ctypes.c_long(68)
zVAR_SEQPOS_ = ctypes.c_long(69)
zVAR_MAXREC_ = ctypes.c_long(70)
zVAR_MAXallocREC_ = ctypes.c_long(71)
zVAR_DATASPEC_ = ctypes.c_long(72)
zVAR_PADVALUE_ = ctypes.c_long(73)
zVAR_INITIALRECS_ = ctypes.c_long(74)
zVAR_BLOCKINGFACTOR_ = ctypes.c_long(75)
zVAR_nINDEXRECORDS_ = ctypes.c_long(76)
zVAR_nINDEXENTRIES_ = ctypes.c_long(77)
zVAR_EXISTENCE_ = ctypes.c_long(78)
zVAR_RECNUMBER_ = ctypes.c_long(79)
zVAR_RECCOUNT_ = ctypes.c_long(80)
zVAR_RECINTERVAL_ = ctypes.c_long(81)
zVAR_DIMINDICES_ = ctypes.c_long(82)
zVAR_DIMCOUNTS_ = ctypes.c_long(83)
zVAR_DIMINTERVALS_ = ctypes.c_long(84)
ATTR_ = ctypes.c_long(85)
ATTR_SCOPE_ = ctypes.c_long(86)
ATTR_NAME_ = ctypes.c_long(87)
ATTR_NUMBER_ = ctypes.c_long(88)
ATTR_MAXgENTRY_ = ctypes.c_long(89)
ATTR_NUMgENTRIES_ = ctypes.c_long(90)
ATTR_MAXrENTRY_ = ctypes.c_long(91)
ATTR_NUMrENTRIES_ = ctypes.c_long(92)
ATTR_MAXzENTRY_ = ctypes.c_long(93)
ATTR_NUMzENTRIES_ = ctypes.c_long(94)
ATTR_EXISTENCE_ = ctypes.c_long(95)
gENTRY_ = ctypes.c_long(96)
gENTRY_EXISTENCE_ = ctypes.c_long(97)
gENTRY_DATATYPE_ = ctypes.c_long(98)
gENTRY_NUMELEMS_ = ctypes.c_long(99)
gENTRY_DATASPEC_ = ctypes.c_long(100)
gENTRY_DATA_ = ctypes.c_long(101)
rENTRY_ = ctypes.c_long(102)
rENTRY_NAME_ = ctypes.c_long(103)
rENTRY_EXISTENCE_ = ctypes.c_long(104)
rENTRY_DATATYPE_ = ctypes.c_long(105)
rENTRY_NUMELEMS_ = ctypes.c_long(106)
rENTRY_DATASPEC_ = ctypes.c_long(107)
rENTRY_DATA_ = ctypes.c_long(108)
zENTRY_ = ctypes.c_long(109)
zENTRY_NAME_ = ctypes.c_long(110)
zENTRY_EXISTENCE_ = ctypes.c_long(111)
zENTRY_DATATYPE_ = ctypes.c_long(112)
zENTRY_NUMELEMS_ = ctypes.c_long(113)
zENTRY_DATASPEC_ = ctypes.c_long(114)
zENTRY_DATA_ = ctypes.c_long(115)
STATUS_TEXT_ = ctypes.c_long(116)
CDF_CACHESIZE_ = ctypes.c_long(117)
rVARs_CACHESIZE_ = ctypes.c_long(118)
zVARs_CACHESIZE_ = ctypes.c_long(119)
rVAR_CACHESIZE_ = ctypes.c_long(120)
zVAR_CACHESIZE_ = ctypes.c_long(121)
zVARs_RECNUMBER_ = ctypes.c_long(122)
rVAR_ALLOCATERECS_ = ctypes.c_long(123)
zVAR_ALLOCATERECS_ = ctypes.c_long(124)
DATATYPE_SIZE_ = ctypes.c_long(125)
CURgENTRY_EXISTENCE_ = ctypes.c_long(126)
CURrENTRY_EXISTENCE_ = ctypes.c_long(127)
CURzENTRY_EXISTENCE_ = ctypes.c_long(128)
CDF_INFO_ = ctypes.c_long(129)
CDF_COMPRESSION_ = ctypes.c_long(130)
zVAR_COMPRESSION_ = ctypes.c_long(131)
zVAR_SPARSERECORDS_ = ctypes.c_long(132)
zVAR_SPARSEARRAYS_ = ctypes.c_long(133)
zVAR_ALLOCATEBLOCK_ = ctypes.c_long(134)
zVAR_NUMRECS_ = ctypes.c_long(135)
zVAR_NUMallocRECS_ = ctypes.c_long(136)
rVAR_COMPRESSION_ = ctypes.c_long(137)
rVAR_SPARSERECORDS_ = ctypes.c_long(138)
rVAR_SPARSEARRAYS_ = ctypes.c_long(139)
rVAR_ALLOCATEBLOCK_ = ctypes.c_long(140)
rVAR_NUMRECS_ = ctypes.c_long(141)
rVAR_NUMallocRECS_ = ctypes.c_long(142)
rVAR_ALLOCATEDFROM_ = ctypes.c_long(143)
rVAR_ALLOCATEDTO_ = ctypes.c_long(144)
zVAR_ALLOCATEDFROM_ = ctypes.c_long(145)
zVAR_ALLOCATEDTO_ = ctypes.c_long(146)
zVAR_nINDEXLEVELS_ = ctypes.c_long(147)
rVAR_nINDEXLEVELS_ = ctypes.c_long(148)
CDF_SCRATCHDIR_ = ctypes.c_long(149)
rVAR_RESERVEPERCENT_ = ctypes.c_long(150)
zVAR_RESERVEPERCENT_ = ctypes.c_long(151)
rVAR_RECORDS_ = ctypes.c_long(152)
zVAR_RECORDS_ = ctypes.c_long(153)
STAGE_CACHESIZE_ = ctypes.c_long(154)
COMPRESS_CACHESIZE_ = ctypes.c_long(155)
CDF_CHECKSUM_ = ctypes.c_long(156)
CDFwithSTATS_ = ctypes.c_long(200)
CDF_ACCESS_ = ctypes.c_long(201)
CDF_DOCUMENT_LEN = CDF_COPYRIGHT_LEN
CDF_ERRTEXT_LEN = CDF_STATUSTEXT_LEN
CDF_NUMDIMS_ = rVARs_NUMDIMS_
CDF_DIMSIZES_ = rVARs_DIMSIZES_
CDF_MAXREC_ = rVARs_MAXREC_
CDF_RECNUMBER_ = rVARs_RECNUMBER_
CDF_RECCOUNT_ = rVARs_RECCOUNT_
CDF_RECINTERVAL_ = rVARs_RECINTERVAL_
CDF_DIMINDICES_ = rVARs_DIMINDICES_
CDF_DIMCOUNTS_ = rVARs_DIMCOUNTS_
CDF_DIMINTERVALS_ = rVARs_DIMINTERVALS_
CDF_NUMVARS_ = CDF_NUMrVARS_
VAR_ = rVAR_
VAR_NAME_ = rVAR_NAME_
VAR_DATATYPE_ = rVAR_DATATYPE_
VAR_NUMELEMS_ = rVAR_NUMELEMS_
VAR_RECVARY_ = rVAR_RECVARY_
VAR_DIMVARYS_ = rVAR_DIMVARYS_
VAR_NUMBER_ = rVAR_NUMBER_
VAR_DATA_ = rVAR_DATA_
VAR_HYPERDATA_ = rVAR_HYPERDATA_
VAR_SEQDATA_ = rVAR_SEQDATA_
VAR_SEQPOS_ = rVAR_SEQPOS_
VAR_MAXREC_ = rVAR_MAXREC_
VAR_DATASPEC_ = rVAR_DATASPEC_
VAR_FILLVALUE_ = rVAR_PADVALUE_
VAR_INITIALRECS_ = rVAR_INITIALRECS_
VAR_EXTENDRECS_ = rVAR_BLOCKINGFACTOR_
ATTR_MAXENTRY_ = ATTR_MAXrENTRY_
ATTR_NUMENTRIES_ = ATTR_NUMrENTRIES_
ENTRY_ = rENTRY_
ENTRY_DATATYPE_ = rENTRY_DATATYPE_
ENTRY_NUMELEMS_ = rENTRY_NUMELEMS_
ENTRY_DATA_ = rENTRY_DATA_
MIPSEL_ENCODING = DECSTATION_ENCODING
MIPSEB_ENCODING = SGi_ENCODING
rVAR_EXISTANCE_ = rVAR_EXISTENCE_
zVAR_EXISTANCE_ = zVAR_EXISTENCE_
ATTR_EXISTANCE_ = ATTR_EXISTENCE_
gENTRY_EXISTANCE_ = gENTRY_EXISTENCE_
rENTRY_EXISTANCE_ = rENTRY_EXISTENCE_
zENTRY_EXISTANCE_ = zENTRY_EXISTENCE_
GLOBAL_SCOPE_ASSUMED = GLOBAL_SCOPE
VARIABLE_SCOPE_ASSUMED = VARIABLE_SCOPE
BAD_EXTEND_RECS = BAD_BLOCKING_FACTOR
rVAR_EXTENDRECS_ = rVAR_BLOCKINGFACTOR_
zVAR_EXTENDRECS_ = zVAR_BLOCKINGFACTOR_
COL_MAJOR = COLUMN_MAJOR
NONE_CHECKSUM = NO_CHECKSUM
