# SNMP MIB module (MICOM-WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-WAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:53 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_wan_ObjectIdentity = ObjectIdentity
micom_wan = _Micom_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2)
)
_Wan_configuration_ObjectIdentity = ObjectIdentity
wan_configuration = _Wan_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1)
)
_WanifTable_Object = MibTable
wanifTable = _WanifTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wanifTable.setStatus("mandatory")
_WanifEntry_Object = MibTableRow
wanifEntry = _WanifEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1)
)
wanifEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifIndex"),
)
if mibBuilder.loadTexts:
    wanifEntry.setStatus("mandatory")


class _WanifIndex_Type(Integer32):
    """Custom type wanifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanifIndex_Type.__name__ = "Integer32"
_WanifIndex_Object = MibTableColumn
wanifIndex = _WanifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 1),
    _WanifIndex_Type()
)
wanifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifIndex.setStatus("mandatory")


class _WanifType_Type(Integer32):
    """Custom type wanifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("csu-dsu", 8),
          ("e1csu", 11),
          ("isdn-BRI", 9),
          ("none", 1),
          ("rs232", 2),
          ("t1csu", 10),
          ("v35", 5),
          ("v36", 7),
          ("x21", 6))
    )


_WanifType_Type.__name__ = "Integer32"
_WanifType_Object = MibTableColumn
wanifType = _WanifType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 2),
    _WanifType_Type()
)
wanifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifType.setStatus("mandatory")


class _WanifMode_Type(Integer32):
    """Custom type wanifMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_WanifMode_Type.__name__ = "Integer32"
_WanifMode_Object = MibTableColumn
wanifMode = _WanifMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 3),
    _WanifMode_Type()
)
wanifMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifMode.setStatus("mandatory")


class _WanifBaudRate_Type(Integer32):
    """Custom type wanifBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1920000),
    )


_WanifBaudRate_Type.__name__ = "Integer32"
_WanifBaudRate_Object = MibTableColumn
wanifBaudRate = _WanifBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 4),
    _WanifBaudRate_Type()
)
wanifBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifBaudRate.setStatus("mandatory")


class _WanifMaxFrameSize_Type(Integer32):
    """Custom type wanifMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_WanifMaxFrameSize_Type.__name__ = "Integer32"
_WanifMaxFrameSize_Object = MibTableColumn
wanifMaxFrameSize = _WanifMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 5),
    _WanifMaxFrameSize_Type()
)
wanifMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifMaxFrameSize.setStatus("mandatory")


class _WanifProtocolType_Type(Integer32):
    """Custom type wanifProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("hdlc", 1)
    )


_WanifProtocolType_Type.__name__ = "Integer32"
_WanifProtocolType_Object = MibTableColumn
wanifProtocolType = _WanifProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 6),
    _WanifProtocolType_Type()
)
wanifProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifProtocolType.setStatus("mandatory")


class _WanifControlLineOn_Type(Integer32):
    """Custom type wanifControlLineOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WanifControlLineOn_Type.__name__ = "Integer32"
_WanifControlLineOn_Object = MibTableColumn
wanifControlLineOn = _WanifControlLineOn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 7),
    _WanifControlLineOn_Type()
)
wanifControlLineOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifControlLineOn.setStatus("obsolete")


class _WanifNumRxBuffers_Type(Integer32):
    """Custom type wanifNumRxBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_WanifNumRxBuffers_Type.__name__ = "Integer32"
_WanifNumRxBuffers_Object = MibTableColumn
wanifNumRxBuffers = _WanifNumRxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 8),
    _WanifNumRxBuffers_Type()
)
wanifNumRxBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifNumRxBuffers.setStatus("mandatory")


class _WanifRxFragQueueSize_Type(Integer32):
    """Custom type wanifRxFragQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_WanifRxFragQueueSize_Type.__name__ = "Integer32"
_WanifRxFragQueueSize_Object = MibTableColumn
wanifRxFragQueueSize = _WanifRxFragQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 9),
    _WanifRxFragQueueSize_Type()
)
wanifRxFragQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifRxFragQueueSize.setStatus("mandatory")


class _WanifTxFragQueueSize_Type(Integer32):
    """Custom type wanifTxFragQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_WanifTxFragQueueSize_Type.__name__ = "Integer32"
_WanifTxFragQueueSize_Object = MibTableColumn
wanifTxFragQueueSize = _WanifTxFragQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 10),
    _WanifTxFragQueueSize_Type()
)
wanifTxFragQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifTxFragQueueSize.setStatus("mandatory")


class _WanifFragFragmentSize_Type(Integer32):
    """Custom type wanifFragFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 8192),
    )


_WanifFragFragmentSize_Type.__name__ = "Integer32"
_WanifFragFragmentSize_Object = MibTableColumn
wanifFragFragmentSize = _WanifFragFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 11),
    _WanifFragFragmentSize_Type()
)
wanifFragFragmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragFragmentSize.setStatus("obsolete")
_WanifRowStatus_Type = Integer32
_WanifRowStatus_Object = MibTableColumn
wanifRowStatus = _WanifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 12),
    _WanifRowStatus_Type()
)
wanifRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifRowStatus.setStatus("obsolete")


class _WanifLim_Type(Integer32):
    """Custom type wanifLim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1))
    )


_WanifLim_Type.__name__ = "Integer32"
_WanifLim_Object = MibTableColumn
wanifLim = _WanifLim_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 13),
    _WanifLim_Type()
)
wanifLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifLim.setStatus("mandatory")


class _WanifChannel_Type(Integer32):
    """Custom type wanifChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WanifChannel_Type.__name__ = "Integer32"
_WanifChannel_Object = MibTableColumn
wanifChannel = _WanifChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 14),
    _WanifChannel_Type()
)
wanifChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifChannel.setStatus("mandatory")


class _WanifProtocolSupType_Type(Integer32):
    """Custom type wanifProtocolSupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 5),
          ("htds", 4),
          ("none", 1),
          ("standardFr", 2),
          ("switchingFr", 3))
    )


_WanifProtocolSupType_Type.__name__ = "Integer32"
_WanifProtocolSupType_Object = MibTableColumn
wanifProtocolSupType = _WanifProtocolSupType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 15),
    _WanifProtocolSupType_Type()
)
wanifProtocolSupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifProtocolSupType.setStatus("mandatory")


class _WanifTDSCutThru_Type(Integer32):
    """Custom type wanifTDSCutThru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WanifTDSCutThru_Type.__name__ = "Integer32"
_WanifTDSCutThru_Object = MibTableColumn
wanifTDSCutThru = _WanifTDSCutThru_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 16),
    _WanifTDSCutThru_Type()
)
wanifTDSCutThru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifTDSCutThru.setStatus("mandatory")
_WanifTDSFragSize_Type = Integer32
_WanifTDSFragSize_Object = MibTableColumn
wanifTDSFragSize = _WanifTDSFragSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 17),
    _WanifTDSFragSize_Type()
)
wanifTDSFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifTDSFragSize.setStatus("mandatory")


class _WanifTDSIdleChar_Type(Integer32):
    """Custom type wanifTDSIdleChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanifTDSIdleChar_Type.__name__ = "Integer32"
_WanifTDSIdleChar_Object = MibTableColumn
wanifTDSIdleChar = _WanifTDSIdleChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 18),
    _WanifTDSIdleChar_Type()
)
wanifTDSIdleChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifTDSIdleChar.setStatus("mandatory")


class _WanifTDSSyncChar_Type(Integer32):
    """Custom type wanifTDSSyncChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanifTDSSyncChar_Type.__name__ = "Integer32"
_WanifTDSSyncChar_Object = MibTableColumn
wanifTDSSyncChar = _WanifTDSSyncChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 19),
    _WanifTDSSyncChar_Type()
)
wanifTDSSyncChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifTDSSyncChar.setStatus("mandatory")


class _WanifEncodeMethod_Type(Integer32):
    """Custom type wanifEncodeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi-mark", 2),
          ("nrzi-space", 3))
    )


_WanifEncodeMethod_Type.__name__ = "Integer32"
_WanifEncodeMethod_Object = MibTableColumn
wanifEncodeMethod = _WanifEncodeMethod_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 1, 1, 20),
    _WanifEncodeMethod_Type()
)
wanifEncodeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifEncodeMethod.setStatus("mandatory")
_NvmWanifTable_Object = MibTable
nvmWanifTable = _NvmWanifTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nvmWanifTable.setStatus("mandatory")
_NvmWanifEntry_Object = MibTableRow
nvmWanifEntry = _NvmWanifEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1)
)
nvmWanifEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "nvmWanifIndex"),
)
if mibBuilder.loadTexts:
    nvmWanifEntry.setStatus("mandatory")


class _NvmWanifIndex_Type(Integer32):
    """Custom type nvmWanifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmWanifIndex_Type.__name__ = "Integer32"
_NvmWanifIndex_Object = MibTableColumn
nvmWanifIndex = _NvmWanifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 1),
    _NvmWanifIndex_Type()
)
nvmWanifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmWanifIndex.setStatus("mandatory")


class _NvmWanifType_Type(Integer32):
    """Custom type nvmWanifType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("csu-dsu", 8),
          ("e1csu", 11),
          ("isdn-BRI", 9),
          ("none", 1),
          ("rs232", 2),
          ("t1csu", 10),
          ("v35", 5),
          ("v36", 7),
          ("x21", 6))
    )


_NvmWanifType_Type.__name__ = "Integer32"
_NvmWanifType_Object = MibTableColumn
nvmWanifType = _NvmWanifType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 2),
    _NvmWanifType_Type()
)
nvmWanifType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifType.setStatus("mandatory")


class _NvmWanifMode_Type(Integer32):
    """Custom type nvmWanifMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_NvmWanifMode_Type.__name__ = "Integer32"
_NvmWanifMode_Object = MibTableColumn
nvmWanifMode = _NvmWanifMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 3),
    _NvmWanifMode_Type()
)
nvmWanifMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifMode.setStatus("mandatory")


class _NvmWanifBaudRate_Type(Integer32):
    """Custom type nvmWanifBaudRate based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1920000),
    )


_NvmWanifBaudRate_Type.__name__ = "Integer32"
_NvmWanifBaudRate_Object = MibTableColumn
nvmWanifBaudRate = _NvmWanifBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 4),
    _NvmWanifBaudRate_Type()
)
nvmWanifBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifBaudRate.setStatus("mandatory")


class _NvmWanifMaxFrameSize_Type(Integer32):
    """Custom type nvmWanifMaxFrameSize based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_NvmWanifMaxFrameSize_Type.__name__ = "Integer32"
_NvmWanifMaxFrameSize_Object = MibTableColumn
nvmWanifMaxFrameSize = _NvmWanifMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 5),
    _NvmWanifMaxFrameSize_Type()
)
nvmWanifMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifMaxFrameSize.setStatus("mandatory")


class _NvmWanifProtocolType_Type(Integer32):
    """Custom type nvmWanifProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("hdlc", 1)
    )


_NvmWanifProtocolType_Type.__name__ = "Integer32"
_NvmWanifProtocolType_Object = MibTableColumn
nvmWanifProtocolType = _NvmWanifProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 6),
    _NvmWanifProtocolType_Type()
)
nvmWanifProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmWanifProtocolType.setStatus("mandatory")


class _NvmWanifControlLineOn_Type(Integer32):
    """Custom type nvmWanifControlLineOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NvmWanifControlLineOn_Type.__name__ = "Integer32"
_NvmWanifControlLineOn_Object = MibTableColumn
nvmWanifControlLineOn = _NvmWanifControlLineOn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 7),
    _NvmWanifControlLineOn_Type()
)
nvmWanifControlLineOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifControlLineOn.setStatus("obsolete")


class _NvmWanifNumRxBuffers_Type(Integer32):
    """Custom type nvmWanifNumRxBuffers based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_NvmWanifNumRxBuffers_Type.__name__ = "Integer32"
_NvmWanifNumRxBuffers_Object = MibTableColumn
nvmWanifNumRxBuffers = _NvmWanifNumRxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 8),
    _NvmWanifNumRxBuffers_Type()
)
nvmWanifNumRxBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifNumRxBuffers.setStatus("mandatory")


class _NvmWanifRxFragQueueSize_Type(Integer32):
    """Custom type nvmWanifRxFragQueueSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_NvmWanifRxFragQueueSize_Type.__name__ = "Integer32"
_NvmWanifRxFragQueueSize_Object = MibTableColumn
nvmWanifRxFragQueueSize = _NvmWanifRxFragQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 9),
    _NvmWanifRxFragQueueSize_Type()
)
nvmWanifRxFragQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifRxFragQueueSize.setStatus("mandatory")


class _NvmWanifTxFragQueueSize_Type(Integer32):
    """Custom type nvmWanifTxFragQueueSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_NvmWanifTxFragQueueSize_Type.__name__ = "Integer32"
_NvmWanifTxFragQueueSize_Object = MibTableColumn
nvmWanifTxFragQueueSize = _NvmWanifTxFragQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 10),
    _NvmWanifTxFragQueueSize_Type()
)
nvmWanifTxFragQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifTxFragQueueSize.setStatus("mandatory")


class _NvmWanifFragFragmentSize_Type(Integer32):
    """Custom type nvmWanifFragFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 8192),
    )


_NvmWanifFragFragmentSize_Type.__name__ = "Integer32"
_NvmWanifFragFragmentSize_Object = MibTableColumn
nvmWanifFragFragmentSize = _NvmWanifFragFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 11),
    _NvmWanifFragFragmentSize_Type()
)
nvmWanifFragFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifFragFragmentSize.setStatus("obsolete")
_NvmWanifRowStatus_Type = Integer32
_NvmWanifRowStatus_Object = MibTableColumn
nvmWanifRowStatus = _NvmWanifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 12),
    _NvmWanifRowStatus_Type()
)
nvmWanifRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifRowStatus.setStatus("obsolete")


class _NvmWanifLim_Type(Integer32):
    """Custom type nvmWanifLim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1))
    )


_NvmWanifLim_Type.__name__ = "Integer32"
_NvmWanifLim_Object = MibTableColumn
nvmWanifLim = _NvmWanifLim_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 13),
    _NvmWanifLim_Type()
)
nvmWanifLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmWanifLim.setStatus("mandatory")


class _NvmWanifChannel_Type(Integer32):
    """Custom type nvmWanifChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NvmWanifChannel_Type.__name__ = "Integer32"
_NvmWanifChannel_Object = MibTableColumn
nvmWanifChannel = _NvmWanifChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 14),
    _NvmWanifChannel_Type()
)
nvmWanifChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmWanifChannel.setStatus("mandatory")


class _NvmWanifProtocolSupType_Type(Integer32):
    """Custom type nvmWanifProtocolSupType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 5),
          ("htds", 4),
          ("none", 1),
          ("standardFr", 2),
          ("switchingFr", 3))
    )


_NvmWanifProtocolSupType_Type.__name__ = "Integer32"
_NvmWanifProtocolSupType_Object = MibTableColumn
nvmWanifProtocolSupType = _NvmWanifProtocolSupType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 15),
    _NvmWanifProtocolSupType_Type()
)
nvmWanifProtocolSupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifProtocolSupType.setStatus("mandatory")


class _NvmWanifTDSCutThru_Type(Integer32):
    """Custom type nvmWanifTDSCutThru based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NvmWanifTDSCutThru_Type.__name__ = "Integer32"
_NvmWanifTDSCutThru_Object = MibTableColumn
nvmWanifTDSCutThru = _NvmWanifTDSCutThru_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 16),
    _NvmWanifTDSCutThru_Type()
)
nvmWanifTDSCutThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifTDSCutThru.setStatus("mandatory")
_NvmWanifTDSFragSize_Type = Integer32
_NvmWanifTDSFragSize_Object = MibTableColumn
nvmWanifTDSFragSize = _NvmWanifTDSFragSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 17),
    _NvmWanifTDSFragSize_Type()
)
nvmWanifTDSFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmWanifTDSFragSize.setStatus("mandatory")


class _NvmWanifTDSIdleChar_Type(Integer32):
    """Custom type nvmWanifTDSIdleChar based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmWanifTDSIdleChar_Type.__name__ = "Integer32"
_NvmWanifTDSIdleChar_Object = MibTableColumn
nvmWanifTDSIdleChar = _NvmWanifTDSIdleChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 18),
    _NvmWanifTDSIdleChar_Type()
)
nvmWanifTDSIdleChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifTDSIdleChar.setStatus("mandatory")


class _NvmWanifTDSSyncChar_Type(Integer32):
    """Custom type nvmWanifTDSSyncChar based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmWanifTDSSyncChar_Type.__name__ = "Integer32"
_NvmWanifTDSSyncChar_Object = MibTableColumn
nvmWanifTDSSyncChar = _NvmWanifTDSSyncChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 19),
    _NvmWanifTDSSyncChar_Type()
)
nvmWanifTDSSyncChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifTDSSyncChar.setStatus("mandatory")


class _NvmWanifEncodeMethod_Type(Integer32):
    """Custom type nvmWanifEncodeMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi-mark", 2),
          ("nrzi-space", 3))
    )


_NvmWanifEncodeMethod_Type.__name__ = "Integer32"
_NvmWanifEncodeMethod_Object = MibTableColumn
nvmWanifEncodeMethod = _NvmWanifEncodeMethod_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 2, 1, 20),
    _NvmWanifEncodeMethod_Type()
)
nvmWanifEncodeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanifEncodeMethod.setStatus("mandatory")
_WanDTEPortTunnelPvcTable_Object = MibTable
wanDTEPortTunnelPvcTable = _WanDTEPortTunnelPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wanDTEPortTunnelPvcTable.setStatus("deprecated")
_WanDTEPortTunnelPvcEntry_Object = MibTableRow
wanDTEPortTunnelPvcEntry = _WanDTEPortTunnelPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 3, 1)
)
wanDTEPortTunnelPvcEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanDTEPortTunnelPvcIfIndex"),
)
if mibBuilder.loadTexts:
    wanDTEPortTunnelPvcEntry.setStatus("deprecated")


class _WanDTEPortTunnelPvcIfIndex_Type(Integer32):
    """Custom type wanDTEPortTunnelPvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanDTEPortTunnelPvcIfIndex_Type.__name__ = "Integer32"
_WanDTEPortTunnelPvcIfIndex_Object = MibTableColumn
wanDTEPortTunnelPvcIfIndex = _WanDTEPortTunnelPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 3, 1, 1),
    _WanDTEPortTunnelPvcIfIndex_Type()
)
wanDTEPortTunnelPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDTEPortTunnelPvcIfIndex.setStatus("deprecated")


class _WanDTEPortTunnelPvcDlci_Type(Integer32):
    """Custom type wanDTEPortTunnelPvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_WanDTEPortTunnelPvcDlci_Type.__name__ = "Integer32"
_WanDTEPortTunnelPvcDlci_Object = MibTableColumn
wanDTEPortTunnelPvcDlci = _WanDTEPortTunnelPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 3, 1, 2),
    _WanDTEPortTunnelPvcDlci_Type()
)
wanDTEPortTunnelPvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDTEPortTunnelPvcDlci.setStatus("deprecated")
_NvmWanDTEPortTunnelPvcTable_Object = MibTable
nvmWanDTEPortTunnelPvcTable = _NvmWanDTEPortTunnelPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    nvmWanDTEPortTunnelPvcTable.setStatus("deprecated")
_NvmWanDTEPortTunnelPvcEntry_Object = MibTableRow
nvmWanDTEPortTunnelPvcEntry = _NvmWanDTEPortTunnelPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 4, 1)
)
nvmWanDTEPortTunnelPvcEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "nvmWanDTEPortTunnelPvcIfIndex"),
)
if mibBuilder.loadTexts:
    nvmWanDTEPortTunnelPvcEntry.setStatus("deprecated")


class _NvmWanDTEPortTunnelPvcIfIndex_Type(Integer32):
    """Custom type nvmWanDTEPortTunnelPvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmWanDTEPortTunnelPvcIfIndex_Type.__name__ = "Integer32"
_NvmWanDTEPortTunnelPvcIfIndex_Object = MibTableColumn
nvmWanDTEPortTunnelPvcIfIndex = _NvmWanDTEPortTunnelPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 4, 1, 1),
    _NvmWanDTEPortTunnelPvcIfIndex_Type()
)
nvmWanDTEPortTunnelPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmWanDTEPortTunnelPvcIfIndex.setStatus("deprecated")


class _NvmWanDTEPortTunnelPvcDlci_Type(Integer32):
    """Custom type nvmWanDTEPortTunnelPvcDlci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_NvmWanDTEPortTunnelPvcDlci_Type.__name__ = "Integer32"
_NvmWanDTEPortTunnelPvcDlci_Object = MibTableColumn
nvmWanDTEPortTunnelPvcDlci = _NvmWanDTEPortTunnelPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 1, 4, 1, 2),
    _NvmWanDTEPortTunnelPvcDlci_Type()
)
nvmWanDTEPortTunnelPvcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmWanDTEPortTunnelPvcDlci.setStatus("deprecated")
_Wan_statistics_ObjectIdentity = ObjectIdentity
wan_statistics = _Wan_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2)
)
_WanifGlobalStatisticsTable_Object = MibTable
wanifGlobalStatisticsTable = _WanifGlobalStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wanifGlobalStatisticsTable.setStatus("mandatory")
_WanifGlobalStatisticsEntry_Object = MibTableRow
wanifGlobalStatisticsEntry = _WanifGlobalStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1)
)
wanifGlobalStatisticsEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifGlobalStatisticsIndex"),
)
if mibBuilder.loadTexts:
    wanifGlobalStatisticsEntry.setStatus("mandatory")


class _WanifGlobalStatisticsIndex_Type(Integer32):
    """Custom type wanifGlobalStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanifGlobalStatisticsIndex_Type.__name__ = "Integer32"
_WanifGlobalStatisticsIndex_Object = MibTableColumn
wanifGlobalStatisticsIndex = _WanifGlobalStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 1),
    _WanifGlobalStatisticsIndex_Type()
)
wanifGlobalStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsIndex.setStatus("mandatory")
_WanifGlobalStatisticsRxBlockCount_Type = Counter32
_WanifGlobalStatisticsRxBlockCount_Object = MibTableColumn
wanifGlobalStatisticsRxBlockCount = _WanifGlobalStatisticsRxBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 2),
    _WanifGlobalStatisticsRxBlockCount_Type()
)
wanifGlobalStatisticsRxBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsRxBlockCount.setStatus("mandatory")
_WanifGlobalStatisticsTxBlockCount_Type = Counter32
_WanifGlobalStatisticsTxBlockCount_Object = MibTableColumn
wanifGlobalStatisticsTxBlockCount = _WanifGlobalStatisticsTxBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 3),
    _WanifGlobalStatisticsTxBlockCount_Type()
)
wanifGlobalStatisticsTxBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsTxBlockCount.setStatus("mandatory")
_WanifGlobalStatisticsTxLinkUnderruns_Type = Counter32
_WanifGlobalStatisticsTxLinkUnderruns_Object = MibTableColumn
wanifGlobalStatisticsTxLinkUnderruns = _WanifGlobalStatisticsTxLinkUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 4),
    _WanifGlobalStatisticsTxLinkUnderruns_Type()
)
wanifGlobalStatisticsTxLinkUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsTxLinkUnderruns.setStatus("mandatory")
_WanifGlobalStatisticsTxLinkOverflows_Type = Counter32
_WanifGlobalStatisticsTxLinkOverflows_Object = MibTableColumn
wanifGlobalStatisticsTxLinkOverflows = _WanifGlobalStatisticsTxLinkOverflows_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 5),
    _WanifGlobalStatisticsTxLinkOverflows_Type()
)
wanifGlobalStatisticsTxLinkOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsTxLinkOverflows.setStatus("mandatory")
_WanifGlobalStatisticsRxDiscards_Type = Counter32
_WanifGlobalStatisticsRxDiscards_Object = MibTableColumn
wanifGlobalStatisticsRxDiscards = _WanifGlobalStatisticsRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 6),
    _WanifGlobalStatisticsRxDiscards_Type()
)
wanifGlobalStatisticsRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsRxDiscards.setStatus("mandatory")
_WanifGlobalStatisticsTxErrors_Type = Counter32
_WanifGlobalStatisticsTxErrors_Object = MibTableColumn
wanifGlobalStatisticsTxErrors = _WanifGlobalStatisticsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 1, 1, 7),
    _WanifGlobalStatisticsTxErrors_Type()
)
wanifGlobalStatisticsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifGlobalStatisticsTxErrors.setStatus("mandatory")
_WanifFragStatisticsTable_Object = MibTable
wanifFragStatisticsTable = _WanifFragStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    wanifFragStatisticsTable.setStatus("obsolete")
_WanifFragStatisticsEntry_Object = MibTableRow
wanifFragStatisticsEntry = _WanifFragStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1)
)
wanifFragStatisticsEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifFragStatisticsIndex"),
    (0, "MICOM-WAN-MIB", "wanifFragStatisticsFragPriority"),
)
if mibBuilder.loadTexts:
    wanifFragStatisticsEntry.setStatus("obsolete")


class _WanifFragStatisticsIndex_Type(Integer32):
    """Custom type wanifFragStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanifFragStatisticsIndex_Type.__name__ = "Integer32"
_WanifFragStatisticsIndex_Object = MibTableColumn
wanifFragStatisticsIndex = _WanifFragStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 1),
    _WanifFragStatisticsIndex_Type()
)
wanifFragStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsIndex.setStatus("obsolete")


class _WanifFragStatisticsFragPriority_Type(Integer32):
    """Custom type wanifFragStatisticsFragPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WanifFragStatisticsFragPriority_Type.__name__ = "Integer32"
_WanifFragStatisticsFragPriority_Object = MibTableColumn
wanifFragStatisticsFragPriority = _WanifFragStatisticsFragPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 2),
    _WanifFragStatisticsFragPriority_Type()
)
wanifFragStatisticsFragPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsFragPriority.setStatus("obsolete")
_WanifFragStatisticsRxFrameCount_Type = Counter32
_WanifFragStatisticsRxFrameCount_Object = MibTableColumn
wanifFragStatisticsRxFrameCount = _WanifFragStatisticsRxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 3),
    _WanifFragStatisticsRxFrameCount_Type()
)
wanifFragStatisticsRxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsRxFrameCount.setStatus("obsolete")
_WanifFragStatisticsTxFrameCount_Type = Counter32
_WanifFragStatisticsTxFrameCount_Object = MibTableColumn
wanifFragStatisticsTxFrameCount = _WanifFragStatisticsTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 4),
    _WanifFragStatisticsTxFrameCount_Type()
)
wanifFragStatisticsTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsTxFrameCount.setStatus("obsolete")
_WanifFragStatisticsRxFragmentCount_Type = Counter32
_WanifFragStatisticsRxFragmentCount_Object = MibTableColumn
wanifFragStatisticsRxFragmentCount = _WanifFragStatisticsRxFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 5),
    _WanifFragStatisticsRxFragmentCount_Type()
)
wanifFragStatisticsRxFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsRxFragmentCount.setStatus("obsolete")
_WanifFragStatisticsTxFragmentCount_Type = Counter32
_WanifFragStatisticsTxFragmentCount_Object = MibTableColumn
wanifFragStatisticsTxFragmentCount = _WanifFragStatisticsTxFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 6),
    _WanifFragStatisticsTxFragmentCount_Type()
)
wanifFragStatisticsTxFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsTxFragmentCount.setStatus("obsolete")
_WanifFragStatisticsTxFragQueueSize_Type = Integer32
_WanifFragStatisticsTxFragQueueSize_Object = MibTableColumn
wanifFragStatisticsTxFragQueueSize = _WanifFragStatisticsTxFragQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 2, 1, 7),
    _WanifFragStatisticsTxFragQueueSize_Type()
)
wanifFragStatisticsTxFragQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifFragStatisticsTxFragQueueSize.setStatus("obsolete")
_WanifVofrStatsTable_Object = MibTable
wanifVofrStatsTable = _WanifVofrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    wanifVofrStatsTable.setStatus("mandatory")
_WanifVofrStatsEntry_Object = MibTableRow
wanifVofrStatsEntry = _WanifVofrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1)
)
wanifVofrStatsEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifVofrStatsIndex"),
)
if mibBuilder.loadTexts:
    wanifVofrStatsEntry.setStatus("mandatory")


class _WanifVofrStatsIndex_Type(Integer32):
    """Custom type wanifVofrStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WanifVofrStatsIndex_Type.__name__ = "Integer32"
_WanifVofrStatsIndex_Object = MibTableColumn
wanifVofrStatsIndex = _WanifVofrStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 1),
    _WanifVofrStatsIndex_Type()
)
wanifVofrStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsIndex.setStatus("mandatory")
_WanifVofrStatsFragHighPriFramesCount_Type = Counter32
_WanifVofrStatsFragHighPriFramesCount_Object = MibTableColumn
wanifVofrStatsFragHighPriFramesCount = _WanifVofrStatsFragHighPriFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 2),
    _WanifVofrStatsFragHighPriFramesCount_Type()
)
wanifVofrStatsFragHighPriFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsFragHighPriFramesCount.setStatus("mandatory")
_WanifVofrStatsFragToIfCount_Type = Counter32
_WanifVofrStatsFragToIfCount_Object = MibTableColumn
wanifVofrStatsFragToIfCount = _WanifVofrStatsFragToIfCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 3),
    _WanifVofrStatsFragToIfCount_Type()
)
wanifVofrStatsFragToIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsFragToIfCount.setStatus("mandatory")
_WanifVofrStatsPackingToIfCount_Type = Counter32
_WanifVofrStatsPackingToIfCount_Object = MibTableColumn
wanifVofrStatsPackingToIfCount = _WanifVofrStatsPackingToIfCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 4),
    _WanifVofrStatsPackingToIfCount_Type()
)
wanifVofrStatsPackingToIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsPackingToIfCount.setStatus("mandatory")
_WanifVofrStatsFragsFromIfCount_Type = Counter32
_WanifVofrStatsFragsFromIfCount_Object = MibTableColumn
wanifVofrStatsFragsFromIfCount = _WanifVofrStatsFragsFromIfCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 5),
    _WanifVofrStatsFragsFromIfCount_Type()
)
wanifVofrStatsFragsFromIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsFragsFromIfCount.setStatus("mandatory")
_WanifVofrStatsLostFragsFromIfCount_Type = Counter32
_WanifVofrStatsLostFragsFromIfCount_Object = MibTableColumn
wanifVofrStatsLostFragsFromIfCount = _WanifVofrStatsLostFragsFromIfCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 6),
    _WanifVofrStatsLostFragsFromIfCount_Type()
)
wanifVofrStatsLostFragsFromIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsLostFragsFromIfCount.setStatus("mandatory")
_WanifVofrStatsProtViolationsFromIfCount_Type = Counter32
_WanifVofrStatsProtViolationsFromIfCount_Object = MibTableColumn
wanifVofrStatsProtViolationsFromIfCount = _WanifVofrStatsProtViolationsFromIfCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 2, 3, 1, 7),
    _WanifVofrStatsProtViolationsFromIfCount_Type()
)
wanifVofrStatsProtViolationsFromIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrStatsProtViolationsFromIfCount.setStatus("mandatory")
_Wan_control_ObjectIdentity = ObjectIdentity
wan_control = _Wan_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3)
)
_WanifCounterGlobalTable_Object = MibTable
wanifCounterGlobalTable = _WanifCounterGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wanifCounterGlobalTable.setStatus("obsolete")
_WanifCounterGlobalEntry_Object = MibTableRow
wanifCounterGlobalEntry = _WanifCounterGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 1, 1)
)
wanifCounterGlobalEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifCounterGlobalPortId"),
)
if mibBuilder.loadTexts:
    wanifCounterGlobalEntry.setStatus("obsolete")
_WanifCounterGlobalPortId_Type = Integer32
_WanifCounterGlobalPortId_Object = MibTableColumn
wanifCounterGlobalPortId = _WanifCounterGlobalPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 1, 1, 1),
    _WanifCounterGlobalPortId_Type()
)
wanifCounterGlobalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifCounterGlobalPortId.setStatus("obsolete")


class _WanifCounterGlobalStatistics_Type(Integer32):
    """Custom type wanifCounterGlobalStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_WanifCounterGlobalStatistics_Type.__name__ = "Integer32"
_WanifCounterGlobalStatistics_Object = MibTableColumn
wanifCounterGlobalStatistics = _WanifCounterGlobalStatistics_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 1, 1, 2),
    _WanifCounterGlobalStatistics_Type()
)
wanifCounterGlobalStatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wanifCounterGlobalStatistics.setStatus("obsolete")
_WanifCounterFragTable_Object = MibTable
wanifCounterFragTable = _WanifCounterFragTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wanifCounterFragTable.setStatus("obsolete")
_WanifCounterFragEntry_Object = MibTableRow
wanifCounterFragEntry = _WanifCounterFragEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 2, 1)
)
wanifCounterFragEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifCounterFragPortId"),
    (0, "MICOM-WAN-MIB", "wanifCounterFragProtocol"),
)
if mibBuilder.loadTexts:
    wanifCounterFragEntry.setStatus("obsolete")
_WanifCounterFragPortId_Type = Integer32
_WanifCounterFragPortId_Object = MibTableColumn
wanifCounterFragPortId = _WanifCounterFragPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 2, 1, 1),
    _WanifCounterFragPortId_Type()
)
wanifCounterFragPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifCounterFragPortId.setStatus("obsolete")


class _WanifCounterFragProtocol_Type(Integer32):
    """Custom type wanifCounterFragProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WanifCounterFragProtocol_Type.__name__ = "Integer32"
_WanifCounterFragProtocol_Object = MibTableColumn
wanifCounterFragProtocol = _WanifCounterFragProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 2, 1, 2),
    _WanifCounterFragProtocol_Type()
)
wanifCounterFragProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifCounterFragProtocol.setStatus("obsolete")


class _WanifCounterFragStatistics_Type(Integer32):
    """Custom type wanifCounterFragStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_WanifCounterFragStatistics_Type.__name__ = "Integer32"
_WanifCounterFragStatistics_Object = MibTableColumn
wanifCounterFragStatistics = _WanifCounterFragStatistics_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 2, 1, 3),
    _WanifCounterFragStatistics_Type()
)
wanifCounterFragStatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wanifCounterFragStatistics.setStatus("obsolete")
_WanifVofrCounterTable_Object = MibTable
wanifVofrCounterTable = _WanifVofrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 3)
)
if mibBuilder.loadTexts:
    wanifVofrCounterTable.setStatus("obsolete")
_WanifVofrCounterEntry_Object = MibTableRow
wanifVofrCounterEntry = _WanifVofrCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 3, 1)
)
wanifVofrCounterEntry.setIndexNames(
    (0, "MICOM-WAN-MIB", "wanifVofrCounterPortId"),
)
if mibBuilder.loadTexts:
    wanifVofrCounterEntry.setStatus("obsolete")
_WanifVofrCounterPortId_Type = Integer32
_WanifVofrCounterPortId_Object = MibTableColumn
wanifVofrCounterPortId = _WanifVofrCounterPortId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 3, 1, 1),
    _WanifVofrCounterPortId_Type()
)
wanifVofrCounterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanifVofrCounterPortId.setStatus("obsolete")


class _WanifVofrCounterStatistics_Type(Integer32):
    """Custom type wanifVofrCounterStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_WanifVofrCounterStatistics_Type.__name__ = "Integer32"
_WanifVofrCounterStatistics_Object = MibTableColumn
wanifVofrCounterStatistics = _WanifVofrCounterStatistics_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 2, 3, 3, 1, 2),
    _WanifVofrCounterStatistics_Type()
)
wanifVofrCounterStatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wanifVofrCounterStatistics.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-WAN-MIB",
    **{"micom-wan": micom_wan,
       "wan-configuration": wan_configuration,
       "wanifTable": wanifTable,
       "wanifEntry": wanifEntry,
       "wanifIndex": wanifIndex,
       "wanifType": wanifType,
       "wanifMode": wanifMode,
       "wanifBaudRate": wanifBaudRate,
       "wanifMaxFrameSize": wanifMaxFrameSize,
       "wanifProtocolType": wanifProtocolType,
       "wanifControlLineOn": wanifControlLineOn,
       "wanifNumRxBuffers": wanifNumRxBuffers,
       "wanifRxFragQueueSize": wanifRxFragQueueSize,
       "wanifTxFragQueueSize": wanifTxFragQueueSize,
       "wanifFragFragmentSize": wanifFragFragmentSize,
       "wanifRowStatus": wanifRowStatus,
       "wanifLim": wanifLim,
       "wanifChannel": wanifChannel,
       "wanifProtocolSupType": wanifProtocolSupType,
       "wanifTDSCutThru": wanifTDSCutThru,
       "wanifTDSFragSize": wanifTDSFragSize,
       "wanifTDSIdleChar": wanifTDSIdleChar,
       "wanifTDSSyncChar": wanifTDSSyncChar,
       "wanifEncodeMethod": wanifEncodeMethod,
       "nvmWanifTable": nvmWanifTable,
       "nvmWanifEntry": nvmWanifEntry,
       "nvmWanifIndex": nvmWanifIndex,
       "nvmWanifType": nvmWanifType,
       "nvmWanifMode": nvmWanifMode,
       "nvmWanifBaudRate": nvmWanifBaudRate,
       "nvmWanifMaxFrameSize": nvmWanifMaxFrameSize,
       "nvmWanifProtocolType": nvmWanifProtocolType,
       "nvmWanifControlLineOn": nvmWanifControlLineOn,
       "nvmWanifNumRxBuffers": nvmWanifNumRxBuffers,
       "nvmWanifRxFragQueueSize": nvmWanifRxFragQueueSize,
       "nvmWanifTxFragQueueSize": nvmWanifTxFragQueueSize,
       "nvmWanifFragFragmentSize": nvmWanifFragFragmentSize,
       "nvmWanifRowStatus": nvmWanifRowStatus,
       "nvmWanifLim": nvmWanifLim,
       "nvmWanifChannel": nvmWanifChannel,
       "nvmWanifProtocolSupType": nvmWanifProtocolSupType,
       "nvmWanifTDSCutThru": nvmWanifTDSCutThru,
       "nvmWanifTDSFragSize": nvmWanifTDSFragSize,
       "nvmWanifTDSIdleChar": nvmWanifTDSIdleChar,
       "nvmWanifTDSSyncChar": nvmWanifTDSSyncChar,
       "nvmWanifEncodeMethod": nvmWanifEncodeMethod,
       "wanDTEPortTunnelPvcTable": wanDTEPortTunnelPvcTable,
       "wanDTEPortTunnelPvcEntry": wanDTEPortTunnelPvcEntry,
       "wanDTEPortTunnelPvcIfIndex": wanDTEPortTunnelPvcIfIndex,
       "wanDTEPortTunnelPvcDlci": wanDTEPortTunnelPvcDlci,
       "nvmWanDTEPortTunnelPvcTable": nvmWanDTEPortTunnelPvcTable,
       "nvmWanDTEPortTunnelPvcEntry": nvmWanDTEPortTunnelPvcEntry,
       "nvmWanDTEPortTunnelPvcIfIndex": nvmWanDTEPortTunnelPvcIfIndex,
       "nvmWanDTEPortTunnelPvcDlci": nvmWanDTEPortTunnelPvcDlci,
       "wan-statistics": wan_statistics,
       "wanifGlobalStatisticsTable": wanifGlobalStatisticsTable,
       "wanifGlobalStatisticsEntry": wanifGlobalStatisticsEntry,
       "wanifGlobalStatisticsIndex": wanifGlobalStatisticsIndex,
       "wanifGlobalStatisticsRxBlockCount": wanifGlobalStatisticsRxBlockCount,
       "wanifGlobalStatisticsTxBlockCount": wanifGlobalStatisticsTxBlockCount,
       "wanifGlobalStatisticsTxLinkUnderruns": wanifGlobalStatisticsTxLinkUnderruns,
       "wanifGlobalStatisticsTxLinkOverflows": wanifGlobalStatisticsTxLinkOverflows,
       "wanifGlobalStatisticsRxDiscards": wanifGlobalStatisticsRxDiscards,
       "wanifGlobalStatisticsTxErrors": wanifGlobalStatisticsTxErrors,
       "wanifFragStatisticsTable": wanifFragStatisticsTable,
       "wanifFragStatisticsEntry": wanifFragStatisticsEntry,
       "wanifFragStatisticsIndex": wanifFragStatisticsIndex,
       "wanifFragStatisticsFragPriority": wanifFragStatisticsFragPriority,
       "wanifFragStatisticsRxFrameCount": wanifFragStatisticsRxFrameCount,
       "wanifFragStatisticsTxFrameCount": wanifFragStatisticsTxFrameCount,
       "wanifFragStatisticsRxFragmentCount": wanifFragStatisticsRxFragmentCount,
       "wanifFragStatisticsTxFragmentCount": wanifFragStatisticsTxFragmentCount,
       "wanifFragStatisticsTxFragQueueSize": wanifFragStatisticsTxFragQueueSize,
       "wanifVofrStatsTable": wanifVofrStatsTable,
       "wanifVofrStatsEntry": wanifVofrStatsEntry,
       "wanifVofrStatsIndex": wanifVofrStatsIndex,
       "wanifVofrStatsFragHighPriFramesCount": wanifVofrStatsFragHighPriFramesCount,
       "wanifVofrStatsFragToIfCount": wanifVofrStatsFragToIfCount,
       "wanifVofrStatsPackingToIfCount": wanifVofrStatsPackingToIfCount,
       "wanifVofrStatsFragsFromIfCount": wanifVofrStatsFragsFromIfCount,
       "wanifVofrStatsLostFragsFromIfCount": wanifVofrStatsLostFragsFromIfCount,
       "wanifVofrStatsProtViolationsFromIfCount": wanifVofrStatsProtViolationsFromIfCount,
       "wan-control": wan_control,
       "wanifCounterGlobalTable": wanifCounterGlobalTable,
       "wanifCounterGlobalEntry": wanifCounterGlobalEntry,
       "wanifCounterGlobalPortId": wanifCounterGlobalPortId,
       "wanifCounterGlobalStatistics": wanifCounterGlobalStatistics,
       "wanifCounterFragTable": wanifCounterFragTable,
       "wanifCounterFragEntry": wanifCounterFragEntry,
       "wanifCounterFragPortId": wanifCounterFragPortId,
       "wanifCounterFragProtocol": wanifCounterFragProtocol,
       "wanifCounterFragStatistics": wanifCounterFragStatistics,
       "wanifVofrCounterTable": wanifVofrCounterTable,
       "wanifVofrCounterEntry": wanifVofrCounterEntry,
       "wanifVofrCounterPortId": wanifVofrCounterPortId,
       "wanifVofrCounterStatistics": wanifVofrCounterStatistics}
)
