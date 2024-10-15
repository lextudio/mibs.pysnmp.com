# SNMP MIB module (HLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:50 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hls_ObjectIdentity = ObjectIdentity
hls = _Hls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26)
)
_HlsBridges_ObjectIdentity = ObjectIdentity
hlsBridges = _HlsBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 2)
)
_EthernetBridge_ObjectIdentity = ObjectIdentity
ethernetBridge = _EthernetBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 2, 1)
)
_RamAddrTab8000Tab_Object = MibTableRow
ramAddrTab8000Tab = _RamAddrTab8000Tab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 1)
)
ramAddrTab8000Tab.setIndexNames(
    (0, "HLS-MIB", "ramAddrTab8000Address"),
)
if mibBuilder.loadTexts:
    ramAddrTab8000Tab.setStatus("mandatory")


class _RamAddrTab8000Entry_Type(OctetString):
    """Custom type ramAddrTab8000Entry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RamAddrTab8000Entry_Type.__name__ = "OctetString"
_RamAddrTab8000Entry_Object = MibTableColumn
ramAddrTab8000Entry = _RamAddrTab8000Entry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 1, 1),
    _RamAddrTab8000Entry_Type()
)
ramAddrTab8000Entry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ramAddrTab8000Entry.setStatus("mandatory")
_RamAddrTab8000Address_Type = MacAddress
_RamAddrTab8000Address_Object = MibTableColumn
ramAddrTab8000Address = _RamAddrTab8000Address_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 1, 2),
    _RamAddrTab8000Address_Type()
)
ramAddrTab8000Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ramAddrTab8000Address.setStatus("mandatory")


class _RamAddrTab8000Filter_Type(OctetString):
    """Custom type ramAddrTab8000Filter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RamAddrTab8000Filter_Type.__name__ = "OctetString"
_RamAddrTab8000Filter_Object = MibScalar
ramAddrTab8000Filter = _RamAddrTab8000Filter_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 2),
    _RamAddrTab8000Filter_Type()
)
ramAddrTab8000Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ramAddrTab8000Filter.setStatus("mandatory")
_RamAddrTab8000FilterNum_Type = Integer32
_RamAddrTab8000FilterNum_Object = MibScalar
ramAddrTab8000FilterNum = _RamAddrTab8000FilterNum_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 3),
    _RamAddrTab8000FilterNum_Type()
)
ramAddrTab8000FilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramAddrTab8000FilterNum.setStatus("mandatory")
_RamAddrTab8000FilterTab_Object = MibTableRow
ramAddrTab8000FilterTab = _RamAddrTab8000FilterTab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 4)
)
ramAddrTab8000FilterTab.setIndexNames(
    (0, "HLS-MIB", "ramAddrTab8000FilterIndex"),
)
if mibBuilder.loadTexts:
    ramAddrTab8000FilterTab.setStatus("mandatory")


class _RamAddrTab8000FilterEntry_Type(OctetString):
    """Custom type ramAddrTab8000FilterEntry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_RamAddrTab8000FilterEntry_Type.__name__ = "OctetString"
_RamAddrTab8000FilterEntry_Object = MibTableColumn
ramAddrTab8000FilterEntry = _RamAddrTab8000FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 4, 1),
    _RamAddrTab8000FilterEntry_Type()
)
ramAddrTab8000FilterEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramAddrTab8000FilterEntry.setStatus("mandatory")
_RamAddrTab8000FilterIndex_Type = Integer32
_RamAddrTab8000FilterIndex_Object = MibTableColumn
ramAddrTab8000FilterIndex = _RamAddrTab8000FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 4, 2),
    _RamAddrTab8000FilterIndex_Type()
)
ramAddrTab8000FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ramAddrTab8000FilterIndex.setStatus("mandatory")


class _RamAddrTab8000Delete_Type(OctetString):
    """Custom type ramAddrTab8000Delete based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RamAddrTab8000Delete_Type.__name__ = "OctetString"
_RamAddrTab8000Delete_Object = MibScalar
ramAddrTab8000Delete = _RamAddrTab8000Delete_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 5),
    _RamAddrTab8000Delete_Type()
)
ramAddrTab8000Delete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ramAddrTab8000Delete.setStatus("mandatory")
_NvramAddrTab8000Tab_Object = MibTableRow
nvramAddrTab8000Tab = _NvramAddrTab8000Tab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 6)
)
nvramAddrTab8000Tab.setIndexNames(
    (0, "HLS-MIB", "nvramAddrTab8000Address"),
)
if mibBuilder.loadTexts:
    nvramAddrTab8000Tab.setStatus("mandatory")


class _NvramAddrTab8000Entry_Type(OctetString):
    """Custom type nvramAddrTab8000Entry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NvramAddrTab8000Entry_Type.__name__ = "OctetString"
_NvramAddrTab8000Entry_Object = MibTableColumn
nvramAddrTab8000Entry = _NvramAddrTab8000Entry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 6, 1),
    _NvramAddrTab8000Entry_Type()
)
nvramAddrTab8000Entry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramAddrTab8000Entry.setStatus("mandatory")
_NvramAddrTab8000Address_Type = MacAddress
_NvramAddrTab8000Address_Object = MibTableColumn
nvramAddrTab8000Address = _NvramAddrTab8000Address_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 6, 2),
    _NvramAddrTab8000Address_Type()
)
nvramAddrTab8000Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramAddrTab8000Address.setStatus("mandatory")


class _NvramAddrTab8000Filter_Type(OctetString):
    """Custom type nvramAddrTab8000Filter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NvramAddrTab8000Filter_Type.__name__ = "OctetString"
_NvramAddrTab8000Filter_Object = MibScalar
nvramAddrTab8000Filter = _NvramAddrTab8000Filter_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 7),
    _NvramAddrTab8000Filter_Type()
)
nvramAddrTab8000Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramAddrTab8000Filter.setStatus("mandatory")
_NvramAddrTab8000FilterNum_Type = Integer32
_NvramAddrTab8000FilterNum_Object = MibScalar
nvramAddrTab8000FilterNum = _NvramAddrTab8000FilterNum_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 8),
    _NvramAddrTab8000FilterNum_Type()
)
nvramAddrTab8000FilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramAddrTab8000FilterNum.setStatus("mandatory")
_NvramAddrTab8000FilterTab_Object = MibTableRow
nvramAddrTab8000FilterTab = _NvramAddrTab8000FilterTab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 9)
)
nvramAddrTab8000FilterTab.setIndexNames(
    (0, "HLS-MIB", "nvramAddrTab8000FilterIndex"),
)
if mibBuilder.loadTexts:
    nvramAddrTab8000FilterTab.setStatus("mandatory")


class _NvramAddrTab8000FilterEntry_Type(OctetString):
    """Custom type nvramAddrTab8000FilterEntry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_NvramAddrTab8000FilterEntry_Type.__name__ = "OctetString"
_NvramAddrTab8000FilterEntry_Object = MibTableColumn
nvramAddrTab8000FilterEntry = _NvramAddrTab8000FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 9, 1),
    _NvramAddrTab8000FilterEntry_Type()
)
nvramAddrTab8000FilterEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramAddrTab8000FilterEntry.setStatus("mandatory")
_NvramAddrTab8000FilterIndex_Type = Integer32
_NvramAddrTab8000FilterIndex_Object = MibTableColumn
nvramAddrTab8000FilterIndex = _NvramAddrTab8000FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 9, 2),
    _NvramAddrTab8000FilterIndex_Type()
)
nvramAddrTab8000FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramAddrTab8000FilterIndex.setStatus("mandatory")


class _NvramAddrTab8000Delete_Type(OctetString):
    """Custom type nvramAddrTab8000Delete based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NvramAddrTab8000Delete_Type.__name__ = "OctetString"
_NvramAddrTab8000Delete_Object = MibScalar
nvramAddrTab8000Delete = _NvramAddrTab8000Delete_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 10),
    _NvramAddrTab8000Delete_Type()
)
nvramAddrTab8000Delete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvramAddrTab8000Delete.setStatus("mandatory")


class _NvramAddrTab8000Update_Type(OctetString):
    """Custom type nvramAddrTab8000Update based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NvramAddrTab8000Update_Type.__name__ = "OctetString"
_NvramAddrTab8000Update_Object = MibScalar
nvramAddrTab8000Update = _NvramAddrTab8000Update_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 1, 11),
    _NvramAddrTab8000Update_Type()
)
nvramAddrTab8000Update.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvramAddrTab8000Update.setStatus("mandatory")
_RemoteEthernetBridge_ObjectIdentity = ObjectIdentity
remoteEthernetBridge = _RemoteEthernetBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 2, 2)
)


class _SegmentBlocking_Type(Integer32):
    """Custom type segmentBlocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SegmentBlocking_Type.__name__ = "Integer32"
_SegmentBlocking_Object = MibScalar
segmentBlocking = _SegmentBlocking_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 2, 1),
    _SegmentBlocking_Type()
)
segmentBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    segmentBlocking.setStatus("mandatory")


class _Linktype_Type(Integer32):
    """Custom type linktype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rs232Dce", 4),
          ("rs232Dte", 1),
          ("rs449Dce", 6),
          ("rs449Dte", 3),
          ("v35Dce", 5),
          ("v35Dte", 2))
    )


_Linktype_Type.__name__ = "Integer32"
_Linktype_Object = MibScalar
linktype = _Linktype_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 2, 2),
    _Linktype_Type()
)
linktype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linktype.setStatus("mandatory")


class _LinkSaver_Type(Integer32):
    """Custom type linkSaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leavePadding", 2),
          ("removePadding", 1))
    )


_LinkSaver_Type.__name__ = "Integer32"
_LinkSaver_Object = MibScalar
linkSaver = _LinkSaver_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 2, 3),
    _LinkSaver_Type()
)
linkSaver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSaver.setStatus("mandatory")


class _CrcType_Type(Integer32):
    """Custom type crcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_CrcType_Type.__name__ = "Integer32"
_CrcType_Object = MibScalar
crcType = _CrcType_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 2, 4),
    _CrcType_Type()
)
crcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcType.setStatus("mandatory")


class _LinkEncoding_Type(Integer32):
    """Custom type linkEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_LinkEncoding_Type.__name__ = "Integer32"
_LinkEncoding_Object = MibScalar
linkEncoding = _LinkEncoding_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 2, 5),
    _LinkEncoding_Type()
)
linkEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkEncoding.setStatus("mandatory")
_TokenBusBridge_ObjectIdentity = ObjectIdentity
tokenBusBridge = _TokenBusBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 2, 3)
)


class _TbTransmitLevel_Type(Integer32):
    """Custom type tbTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TbTransmitLevel_Type.__name__ = "Integer32"
_TbTransmitLevel_Object = MibScalar
tbTransmitLevel = _TbTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 2),
    _TbTransmitLevel_Type()
)
tbTransmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTransmitLevel.setStatus("mandatory")


class _TbSlotTime_Type(Integer32):
    """Custom type tbSlotTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_TbSlotTime_Type.__name__ = "Integer32"
_TbSlotTime_Object = MibScalar
tbSlotTime = _TbSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 3),
    _TbSlotTime_Type()
)
tbSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSlotTime.setStatus("mandatory")


class _TbHoldtime_Type(Integer32):
    """Custom type tbHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65535),
    )


_TbHoldtime_Type.__name__ = "Integer32"
_TbHoldtime_Object = MibScalar
tbHoldtime = _TbHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 4),
    _TbHoldtime_Type()
)
tbHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbHoldtime.setStatus("mandatory")


class _TbRotationTime_Type(Integer32):
    """Custom type tbRotationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2097151),
    )


_TbRotationTime_Type.__name__ = "Integer32"
_TbRotationTime_Object = MibScalar
tbRotationTime = _TbRotationTime_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 5),
    _TbRotationTime_Type()
)
tbRotationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbRotationTime.setStatus("mandatory")


class _TbRingTimerInitialValue_Type(Integer32):
    """Custom type tbRingTimerInitialValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2097151),
    )


_TbRingTimerInitialValue_Type.__name__ = "Integer32"
_TbRingTimerInitialValue_Object = MibScalar
tbRingTimerInitialValue = _TbRingTimerInitialValue_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 6),
    _TbRingTimerInitialValue_Type()
)
tbRingTimerInitialValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRingTimerInitialValue.setStatus("mandatory")


class _TbSolicitCount_Type(Integer32):
    """Custom type tbSolicitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_TbSolicitCount_Type.__name__ = "Integer32"
_TbSolicitCount_Object = MibScalar
tbSolicitCount = _TbSolicitCount_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 7),
    _TbSolicitCount_Type()
)
tbSolicitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSolicitCount.setStatus("mandatory")


class _TbResetDefault_Type(Integer32):
    """Custom type tbResetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetParms", 1)
    )


_TbResetDefault_Type.__name__ = "Integer32"
_TbResetDefault_Object = MibScalar
tbResetDefault = _TbResetDefault_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 8),
    _TbResetDefault_Type()
)
tbResetDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tbResetDefault.setStatus("mandatory")


class _TbFrequency_Type(Integer32):
    """Custom type tbFrequency based on Integer32"""
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
        *(("range1", 1),
          ("range2", 2),
          ("range3", 3),
          ("range4", 4),
          ("range5", 5))
    )


_TbFrequency_Type.__name__ = "Integer32"
_TbFrequency_Object = MibScalar
tbFrequency = _TbFrequency_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 9),
    _TbFrequency_Type()
)
tbFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbFrequency.setStatus("mandatory")
_RamAddrTab8200Tab_Object = MibTableRow
ramAddrTab8200Tab = _RamAddrTab8200Tab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 10)
)
ramAddrTab8200Tab.setIndexNames(
    (0, "HLS-MIB", "ramAddrTab8200Address"),
)
if mibBuilder.loadTexts:
    ramAddrTab8200Tab.setStatus("mandatory")


class _RamAddrTab8200Entry_Type(OctetString):
    """Custom type ramAddrTab8200Entry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_RamAddrTab8200Entry_Type.__name__ = "OctetString"
_RamAddrTab8200Entry_Object = MibTableColumn
ramAddrTab8200Entry = _RamAddrTab8200Entry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 10, 1),
    _RamAddrTab8200Entry_Type()
)
ramAddrTab8200Entry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ramAddrTab8200Entry.setStatus("mandatory")
_RamAddrTab8200Address_Type = MacAddress
_RamAddrTab8200Address_Object = MibTableColumn
ramAddrTab8200Address = _RamAddrTab8200Address_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 10, 2),
    _RamAddrTab8200Address_Type()
)
ramAddrTab8200Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ramAddrTab8200Address.setStatus("mandatory")


class _RamAddrTab8200Filter_Type(OctetString):
    """Custom type ramAddrTab8200Filter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_RamAddrTab8200Filter_Type.__name__ = "OctetString"
_RamAddrTab8200Filter_Object = MibScalar
ramAddrTab8200Filter = _RamAddrTab8200Filter_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 11),
    _RamAddrTab8200Filter_Type()
)
ramAddrTab8200Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ramAddrTab8200Filter.setStatus("mandatory")
_RamAddrTab8200FilterNum_Type = Integer32
_RamAddrTab8200FilterNum_Object = MibScalar
ramAddrTab8200FilterNum = _RamAddrTab8200FilterNum_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 12),
    _RamAddrTab8200FilterNum_Type()
)
ramAddrTab8200FilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramAddrTab8200FilterNum.setStatus("mandatory")
_RamAddrTab8200FilterTab_Object = MibTableRow
ramAddrTab8200FilterTab = _RamAddrTab8200FilterTab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 13)
)
ramAddrTab8200FilterTab.setIndexNames(
    (0, "HLS-MIB", "ramAddrTab8200FilterIndex"),
)
if mibBuilder.loadTexts:
    ramAddrTab8200FilterTab.setStatus("mandatory")


class _RamAddrTab8200FilterEntry_Type(OctetString):
    """Custom type ramAddrTab8200FilterEntry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_RamAddrTab8200FilterEntry_Type.__name__ = "OctetString"
_RamAddrTab8200FilterEntry_Object = MibTableColumn
ramAddrTab8200FilterEntry = _RamAddrTab8200FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 13, 1),
    _RamAddrTab8200FilterEntry_Type()
)
ramAddrTab8200FilterEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramAddrTab8200FilterEntry.setStatus("mandatory")
_RamAddrTab8200FilterIndex_Type = Integer32
_RamAddrTab8200FilterIndex_Object = MibTableColumn
ramAddrTab8200FilterIndex = _RamAddrTab8200FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 13, 2),
    _RamAddrTab8200FilterIndex_Type()
)
ramAddrTab8200FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ramAddrTab8200FilterIndex.setStatus("mandatory")


class _RamAddrTab8200Delete_Type(OctetString):
    """Custom type ramAddrTab8200Delete based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_RamAddrTab8200Delete_Type.__name__ = "OctetString"
_RamAddrTab8200Delete_Object = MibScalar
ramAddrTab8200Delete = _RamAddrTab8200Delete_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 14),
    _RamAddrTab8200Delete_Type()
)
ramAddrTab8200Delete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ramAddrTab8200Delete.setStatus("mandatory")
_NvramAddrTab8200Tab_Object = MibTableRow
nvramAddrTab8200Tab = _NvramAddrTab8200Tab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 15)
)
nvramAddrTab8200Tab.setIndexNames(
    (0, "HLS-MIB", "nvramAddrTab8200Address"),
)
if mibBuilder.loadTexts:
    nvramAddrTab8200Tab.setStatus("mandatory")


class _NvramAddrTab8200Entry_Type(OctetString):
    """Custom type nvramAddrTab8200Entry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_NvramAddrTab8200Entry_Type.__name__ = "OctetString"
_NvramAddrTab8200Entry_Object = MibTableColumn
nvramAddrTab8200Entry = _NvramAddrTab8200Entry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 15, 1),
    _NvramAddrTab8200Entry_Type()
)
nvramAddrTab8200Entry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramAddrTab8200Entry.setStatus("mandatory")
_NvramAddrTab8200Address_Type = MacAddress
_NvramAddrTab8200Address_Object = MibTableColumn
nvramAddrTab8200Address = _NvramAddrTab8200Address_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 15, 2),
    _NvramAddrTab8200Address_Type()
)
nvramAddrTab8200Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramAddrTab8200Address.setStatus("mandatory")


class _NvramAddrTab8200Filter_Type(OctetString):
    """Custom type nvramAddrTab8200Filter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_NvramAddrTab8200Filter_Type.__name__ = "OctetString"
_NvramAddrTab8200Filter_Object = MibScalar
nvramAddrTab8200Filter = _NvramAddrTab8200Filter_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 16),
    _NvramAddrTab8200Filter_Type()
)
nvramAddrTab8200Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramAddrTab8200Filter.setStatus("mandatory")
_NvramAddrTab8200FilterNum_Type = Integer32
_NvramAddrTab8200FilterNum_Object = MibScalar
nvramAddrTab8200FilterNum = _NvramAddrTab8200FilterNum_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 17),
    _NvramAddrTab8200FilterNum_Type()
)
nvramAddrTab8200FilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramAddrTab8200FilterNum.setStatus("mandatory")
_NvramAddrTab8200FilterTab_Object = MibTableRow
nvramAddrTab8200FilterTab = _NvramAddrTab8200FilterTab_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 18)
)
nvramAddrTab8200FilterTab.setIndexNames(
    (0, "HLS-MIB", "nvramAddrTab8200FilterIndex"),
)
if mibBuilder.loadTexts:
    nvramAddrTab8200FilterTab.setStatus("mandatory")


class _NvramAddrTab8200FilterEntry_Type(OctetString):
    """Custom type nvramAddrTab8200FilterEntry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_NvramAddrTab8200FilterEntry_Type.__name__ = "OctetString"
_NvramAddrTab8200FilterEntry_Object = MibTableColumn
nvramAddrTab8200FilterEntry = _NvramAddrTab8200FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 18, 1),
    _NvramAddrTab8200FilterEntry_Type()
)
nvramAddrTab8200FilterEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramAddrTab8200FilterEntry.setStatus("mandatory")
_NvramAddrTab8200FilterIndex_Type = Integer32
_NvramAddrTab8200FilterIndex_Object = MibTableColumn
nvramAddrTab8200FilterIndex = _NvramAddrTab8200FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 18, 2),
    _NvramAddrTab8200FilterIndex_Type()
)
nvramAddrTab8200FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramAddrTab8200FilterIndex.setStatus("mandatory")


class _NvramAddrTab8200Delete_Type(OctetString):
    """Custom type nvramAddrTab8200Delete based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_NvramAddrTab8200Delete_Type.__name__ = "OctetString"
_NvramAddrTab8200Delete_Object = MibScalar
nvramAddrTab8200Delete = _NvramAddrTab8200Delete_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 19),
    _NvramAddrTab8200Delete_Type()
)
nvramAddrTab8200Delete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvramAddrTab8200Delete.setStatus("mandatory")


class _NvramAddrTab8200Update_Type(OctetString):
    """Custom type nvramAddrTab8200Update based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_NvramAddrTab8200Update_Type.__name__ = "OctetString"
_NvramAddrTab8200Update_Object = MibScalar
nvramAddrTab8200Update = _NvramAddrTab8200Update_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 20),
    _NvramAddrTab8200Update_Type()
)
nvramAddrTab8200Update.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvramAddrTab8200Update.setStatus("mandatory")
_TbEbitErrors_Type = Counter32
_TbEbitErrors_Object = MibScalar
tbEbitErrors = _TbEbitErrors_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 21),
    _TbEbitErrors_Type()
)
tbEbitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbEbitErrors.setStatus("mandatory")
_TbFrameFrags_Type = Counter32
_TbFrameFrags_Object = MibScalar
tbFrameFrags = _TbFrameFrags_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 22),
    _TbFrameFrags_Type()
)
tbFrameFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbFrameFrags.setStatus("mandatory")
_TbTokenPassFails_Type = Counter32
_TbTokenPassFails_Object = MibScalar
tbTokenPassFails = _TbTokenPassFails_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 3, 23),
    _TbTokenPassFails_Type()
)
tbTokenPassFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbTokenPassFails.setStatus("mandatory")


class _BridgeModel_Type(Integer32):
    """Custom type bridgeModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("hls8011", 3),
          ("hls8032", 8),
          ("hls8033", 7),
          ("hls8050", 2),
          ("hls8080", 1),
          ("hls8133", 9),
          ("hls8200", 4),
          ("hls8220", 5),
          ("hls8233", 10),
          ("hls8235", 12),
          ("hls8500", 6))
    )


_BridgeModel_Type.__name__ = "Integer32"
_BridgeModel_Object = MibScalar
bridgeModel = _BridgeModel_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 4),
    _BridgeModel_Type()
)
bridgeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeModel.setStatus("mandatory")


class _BridgeMode_Type(Integer32):
    """Custom type bridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("backup", 1),
          ("offline", 3),
          ("spanningTree", 4))
    )


_BridgeMode_Type.__name__ = "Integer32"
_BridgeMode_Object = MibScalar
bridgeMode = _BridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 15),
    _BridgeMode_Type()
)
bridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMode.setStatus("mandatory")


class _AgeingOption_Type(Integer32):
    """Custom type ageingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ageing", 2),
          ("notAgeing", 1))
    )


_AgeingOption_Type.__name__ = "Integer32"
_AgeingOption_Object = MibScalar
ageingOption = _AgeingOption_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 16),
    _AgeingOption_Type()
)
ageingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ageingOption.setStatus("mandatory")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("mandatory")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1)
)
channelEntry.setIndexNames(
    (0, "HLS-MIB", "channelNumber"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("mandatory")


class _ChLearnMode_Type(Integer32):
    """Custom type chLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChLearnMode_Type.__name__ = "Integer32"
_ChLearnMode_Object = MibTableColumn
chLearnMode = _ChLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 1),
    _ChLearnMode_Type()
)
chLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLearnMode.setStatus("mandatory")


class _ChRestrictMode_Type(Integer32):
    """Custom type chRestrictMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChRestrictMode_Type.__name__ = "Integer32"
_ChRestrictMode_Object = MibTableColumn
chRestrictMode = _ChRestrictMode_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 2),
    _ChRestrictMode_Type()
)
chRestrictMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRestrictMode.setStatus("mandatory")


class _ChOriginMode_Type(Integer32):
    """Custom type chOriginMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChOriginMode_Type.__name__ = "Integer32"
_ChOriginMode_Object = MibTableColumn
chOriginMode = _ChOriginMode_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 3),
    _ChOriginMode_Type()
)
chOriginMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chOriginMode.setStatus("mandatory")


class _ChGroupFwdMode_Type(Integer32):
    """Custom type chGroupFwdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChGroupFwdMode_Type.__name__ = "Integer32"
_ChGroupFwdMode_Object = MibTableColumn
chGroupFwdMode = _ChGroupFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 4),
    _ChGroupFwdMode_Type()
)
chGroupFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chGroupFwdMode.setStatus("mandatory")


class _ChIndFwdMode_Type(Integer32):
    """Custom type chIndFwdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChIndFwdMode_Type.__name__ = "Integer32"
_ChIndFwdMode_Object = MibTableColumn
chIndFwdMode = _ChIndFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 5),
    _ChIndFwdMode_Type()
)
chIndFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chIndFwdMode.setStatus("mandatory")


class _ChDefRestrictFlag_Type(Integer32):
    """Custom type chDefRestrictFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChDefRestrictFlag_Type.__name__ = "Integer32"
_ChDefRestrictFlag_Object = MibTableColumn
chDefRestrictFlag = _ChDefRestrictFlag_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 6),
    _ChDefRestrictFlag_Type()
)
chDefRestrictFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chDefRestrictFlag.setStatus("mandatory")


class _ChDefStaticFlag_Type(Integer32):
    """Custom type chDefStaticFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChDefStaticFlag_Type.__name__ = "Integer32"
_ChDefStaticFlag_Object = MibTableColumn
chDefStaticFlag = _ChDefStaticFlag_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 7),
    _ChDefStaticFlag_Type()
)
chDefStaticFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chDefStaticFlag.setStatus("mandatory")


class _ChDefOriginFlag_Type(Integer32):
    """Custom type chDefOriginFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChDefOriginFlag_Type.__name__ = "Integer32"
_ChDefOriginFlag_Object = MibTableColumn
chDefOriginFlag = _ChDefOriginFlag_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 8),
    _ChDefOriginFlag_Type()
)
chDefOriginFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chDefOriginFlag.setStatus("mandatory")
_ChInCRCs_Type = Counter32
_ChInCRCs_Object = MibTableColumn
chInCRCs = _ChInCRCs_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 9),
    _ChInCRCs_Type()
)
chInCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chInCRCs.setStatus("mandatory")
_ChInOverruns_Type = Counter32
_ChInOverruns_Object = MibTableColumn
chInOverruns = _ChInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 10),
    _ChInOverruns_Type()
)
chInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chInOverruns.setStatus("mandatory")
_ChOutColls_Type = Counter32
_ChOutColls_Object = MibTableColumn
chOutColls = _ChOutColls_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 11),
    _ChOutColls_Type()
)
chOutColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chOutColls.setStatus("mandatory")
_ChWhos_Type = Counter32
_ChWhos_Object = MibTableColumn
chWhos = _ChWhos_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 12),
    _ChWhos_Type()
)
chWhos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chWhos.setStatus("mandatory")
_ChInRunts_Type = Counter32
_ChInRunts_Object = MibTableColumn
chInRunts = _ChInRunts_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 13),
    _ChInRunts_Type()
)
chInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chInRunts.setStatus("mandatory")
_ChInGiants_Type = Counter32
_ChInGiants_Object = MibTableColumn
chInGiants = _ChInGiants_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 14),
    _ChInGiants_Type()
)
chInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chInGiants.setStatus("mandatory")
_ChInLenErrors_Type = Counter32
_ChInLenErrors_Object = MibTableColumn
chInLenErrors = _ChInLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 15),
    _ChInLenErrors_Type()
)
chInLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chInLenErrors.setStatus("mandatory")
_ChInLocks_Type = Counter32
_ChInLocks_Object = MibTableColumn
chInLocks = _ChInLocks_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 16),
    _ChInLocks_Type()
)
chInLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chInLocks.setStatus("mandatory")
_ChOutLocks_Type = Counter32
_ChOutLocks_Object = MibTableColumn
chOutLocks = _ChOutLocks_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 17),
    _ChOutLocks_Type()
)
chOutLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chOutLocks.setStatus("mandatory")
_ChNoBuffers_Type = Counter32
_ChNoBuffers_Object = MibTableColumn
chNoBuffers = _ChNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 18),
    _ChNoBuffers_Type()
)
chNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNoBuffers.setStatus("mandatory")
_ChannelNumber_Type = Integer32
_ChannelNumber_Object = MibTableColumn
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 17, 1, 19),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelNumber.setStatus("mandatory")


class _ProtocolBlocking_Type(OctetString):
    """Custom type protocolBlocking based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_ProtocolBlocking_Type.__name__ = "OctetString"
_ProtocolBlocking_Object = MibScalar
protocolBlocking = _ProtocolBlocking_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 18),
    _ProtocolBlocking_Type()
)
protocolBlocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolBlocking.setStatus("deprecated")
_ResetLogTable_Object = MibTable
resetLogTable = _ResetLogTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 19)
)
if mibBuilder.loadTexts:
    resetLogTable.setStatus("mandatory")
_ResetLogEntry_Object = MibTableRow
resetLogEntry = _ResetLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 19, 1)
)
resetLogEntry.setIndexNames(
    (0, "HLS-MIB", "entryNumber"),
)
if mibBuilder.loadTexts:
    resetLogEntry.setStatus("mandatory")


class _Reason_Type(Integer32):
    """Custom type reason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("buttonPressReset", 2),
          ("parityError", 6),
          ("powerFail", 4),
          ("selfTestFail", 5),
          ("selfTestReset", 7),
          ("softwareCrash", 3),
          ("softwareReset", 1),
          ("unknown", 8))
    )


_Reason_Type.__name__ = "Integer32"
_Reason_Object = MibTableColumn
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 19, 1, 1),
    _Reason_Type()
)
reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reason.setStatus("mandatory")
_Uptime_Type = OctetString
_Uptime_Object = MibTableColumn
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 19, 1, 2),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("mandatory")
_EntryNumber_Type = Integer32
_EntryNumber_Object = MibTableColumn
entryNumber = _EntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 19, 1, 3),
    _EntryNumber_Type()
)
entryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entryNumber.setStatus("mandatory")


class _PacketSize_Type(Integer32):
    """Custom type packetSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_PacketSize_Type.__name__ = "Integer32"
_PacketSize_Object = MibScalar
packetSize = _PacketSize_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 20),
    _PacketSize_Type()
)
packetSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetSize.setStatus("mandatory")
_TransmitDeadmanTimer_Type = Integer32
_TransmitDeadmanTimer_Object = MibScalar
transmitDeadmanTimer = _TransmitDeadmanTimer_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 21),
    _TransmitDeadmanTimer_Type()
)
transmitDeadmanTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitDeadmanTimer.setStatus("mandatory")
_ReceiveDeadmanTimer_Type = Integer32
_ReceiveDeadmanTimer_Object = MibScalar
receiveDeadmanTimer = _ReceiveDeadmanTimer_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 22),
    _ReceiveDeadmanTimer_Type()
)
receiveDeadmanTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiveDeadmanTimer.setStatus("mandatory")
_TokenRingBridge_ObjectIdentity = ObjectIdentity
tokenRingBridge = _TokenRingBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 2, 23)
)


class _TrBridgeNumber_Type(Integer32):
    """Custom type trBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TrBridgeNumber_Type.__name__ = "Integer32"
_TrBridgeNumber_Object = MibScalar
trBridgeNumber = _TrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 23, 1),
    _TrBridgeNumber_Type()
)
trBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trBridgeNumber.setStatus("mandatory")
_TrChannelTable_Object = MibTable
trChannelTable = _TrChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 23, 2)
)
if mibBuilder.loadTexts:
    trChannelTable.setStatus("mandatory")
_TrChannelEntry_Object = MibTableRow
trChannelEntry = _TrChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 23, 2, 1)
)
trChannelEntry.setIndexNames(
    (0, "HLS-MIB", "channelNumber"),
)
if mibBuilder.loadTexts:
    trChannelEntry.setStatus("mandatory")


class _TrRingNumber_Type(Integer32):
    """Custom type trRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TrRingNumber_Type.__name__ = "Integer32"
_TrRingNumber_Object = MibTableColumn
trRingNumber = _TrRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 23, 2, 1, 1),
    _TrRingNumber_Type()
)
trRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trRingNumber.setStatus("mandatory")


class _TrSRAstate_Type(Integer32):
    """Custom type trSRAstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TrSRAstate_Type.__name__ = "Integer32"
_TrSRAstate_Object = MibTableColumn
trSRAstate = _TrSRAstate_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 23, 2, 1, 2),
    _TrSRAstate_Type()
)
trSRAstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trSRAstate.setStatus("mandatory")
_ProtocolFilterTable_Object = MibTable
protocolFilterTable = _ProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 24)
)
if mibBuilder.loadTexts:
    protocolFilterTable.setStatus("mandatory")
_ProtocolFilterEntry_Object = MibTableRow
protocolFilterEntry = _ProtocolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 24, 1)
)
protocolFilterEntry.setIndexNames(
    (0, "HLS-MIB", "protocolFilterType"),
)
if mibBuilder.loadTexts:
    protocolFilterEntry.setStatus("mandatory")


class _ProtocolFilterStatus_Type(Integer32):
    """Custom type protocolFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("forward", 1),
          ("invalid", 3))
    )


_ProtocolFilterStatus_Type.__name__ = "Integer32"
_ProtocolFilterStatus_Object = MibTableColumn
protocolFilterStatus = _ProtocolFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 24, 1, 1),
    _ProtocolFilterStatus_Type()
)
protocolFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterStatus.setStatus("mandatory")


class _ProtocolFilterType_Type(Integer32):
    """Custom type protocolFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProtocolFilterType_Type.__name__ = "Integer32"
_ProtocolFilterType_Object = MibTableColumn
protocolFilterType = _ProtocolFilterType_Object(
    (1, 3, 6, 1, 4, 1, 26, 2, 24, 1, 2),
    _ProtocolFilterType_Type()
)
protocolFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterType.setStatus("mandatory")


class _SysType_Type(Integer32):
    """Custom type sysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("terminalServer", 3))
    )


_SysType_Type.__name__ = "Integer32"
_SysType_Object = MibScalar
sysType = _SysType_Object(
    (1, 3, 6, 1, 4, 1, 26, 3),
    _SysType_Type()
)
sysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysType.setStatus("mandatory")
_SerialNumber_Type = Integer32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_BootPromVersion_Type = DisplayString
_BootPromVersion_Object = MibScalar
bootPromVersion = _BootPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 26, 5),
    _BootPromVersion_Type()
)
bootPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootPromVersion.setStatus("mandatory")


class _SysAdmAccess_Type(Integer32):
    """Custom type sysAdmAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("password", 2),
          ("pfx", 3))
    )


_SysAdmAccess_Type.__name__ = "Integer32"
_SysAdmAccess_Object = MibScalar
sysAdmAccess = _SysAdmAccess_Object(
    (1, 3, 6, 1, 4, 1, 26, 6),
    _SysAdmAccess_Type()
)
sysAdmAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAdmAccess.setStatus("mandatory")
_AppSwVersion_Type = DisplayString
_AppSwVersion_Object = MibScalar
appSwVersion = _AppSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 26, 7),
    _AppSwVersion_Type()
)
appSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSwVersion.setStatus("mandatory")
_UserProfile_Type = OctetString
_UserProfile_Object = MibScalar
userProfile = _UserProfile_Object(
    (1, 3, 6, 1, 4, 1, 26, 8),
    _UserProfile_Type()
)
userProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userProfile.setStatus("obsolete")


class _HlsMibVersion_Type(Integer32):
    """Custom type hlsMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("versionA", 1),
          ("versionB", 2))
    )


_HlsMibVersion_Type.__name__ = "Integer32"
_HlsMibVersion_Object = MibScalar
hlsMibVersion = _HlsMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 26, 9),
    _HlsMibVersion_Type()
)
hlsMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsMibVersion.setStatus("mandatory")
_MyManager_Type = IpAddress
_MyManager_Object = MibScalar
myManager = _MyManager_Object(
    (1, 3, 6, 1, 4, 1, 26, 10),
    _MyManager_Type()
)
myManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myManager.setStatus("deprecated")


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 26, 11),
    _SysReset_Type()
)
sysReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")
_ClearCounters_Type = Integer32
_ClearCounters_Object = MibScalar
clearCounters = _ClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 26, 12),
    _ClearCounters_Type()
)
clearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    clearCounters.setStatus("mandatory")


class _SystemDate_Type(DisplayString):
    """Custom type systemDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SystemDate_Type.__name__ = "DisplayString"
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 26, 13),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("mandatory")


class _SystemTime_Type(DisplayString):
    """Custom type systemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SystemTime_Type.__name__ = "DisplayString"
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 26, 14),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("mandatory")
_AlarmOption_Type = OctetString
_AlarmOption_Object = MibScalar
alarmOption = _AlarmOption_Object(
    (1, 3, 6, 1, 4, 1, 26, 15),
    _AlarmOption_Type()
)
alarmOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOption.setStatus("obsolete")


class _SnmpAccess_Type(Integer32):
    """Custom type snmpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("community", 3),
          ("password", 1),
          ("pfx", 2))
    )


_SnmpAccess_Type.__name__ = "Integer32"
_SnmpAccess_Object = MibScalar
snmpAccess = _SnmpAccess_Object(
    (1, 3, 6, 1, 4, 1, 26, 16),
    _SnmpAccess_Type()
)
snmpAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccess.setStatus("obsolete")
_MyIpAddress_Type = IpAddress
_MyIpAddress_Object = MibScalar
myIpAddress = _MyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 26, 17),
    _MyIpAddress_Type()
)
myIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpAddress.setStatus("mandatory")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 26, 18),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("mandatory")
_NetMask_Type = IpAddress
_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 26, 19),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("mandatory")
_HlsSystem_ObjectIdentity = ObjectIdentity
hlsSystem = _HlsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 20)
)


class _SnmpAuth_Type(Integer32):
    """Custom type snmpAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hlsPassword", 1),
          ("hlsPfx", 2),
          ("snmpCommunity", 3))
    )


_SnmpAuth_Type.__name__ = "Integer32"
_SnmpAuth_Object = MibScalar
snmpAuth = _SnmpAuth_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 1),
    _SnmpAuth_Type()
)
snmpAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAuth.setStatus("mandatory")
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 5)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 5, 1)
)
trapEntry.setIndexNames(
    (0, "HLS-MIB", "trapEntryNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")
_TrapDestination_Type = IpAddress
_TrapDestination_Object = MibTableColumn
trapDestination = _TrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 5, 1, 1),
    _TrapDestination_Type()
)
trapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestination.setStatus("mandatory")
_GenericTrapSwitches_Type = OctetString
_GenericTrapSwitches_Object = MibTableColumn
genericTrapSwitches = _GenericTrapSwitches_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 5, 1, 2),
    _GenericTrapSwitches_Type()
)
genericTrapSwitches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericTrapSwitches.setStatus("mandatory")
_SpecificTrapSwitches_Type = OctetString
_SpecificTrapSwitches_Object = MibTableColumn
specificTrapSwitches = _SpecificTrapSwitches_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 5, 1, 3),
    _SpecificTrapSwitches_Type()
)
specificTrapSwitches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificTrapSwitches.setStatus("mandatory")
_TrapEntryNumber_Type = Integer32
_TrapEntryNumber_Object = MibTableColumn
trapEntryNumber = _TrapEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 26, 20, 5, 1, 4),
    _TrapEntryNumber_Type()
)
trapEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEntryNumber.setStatus("mandatory")
_HlsTemporary_ObjectIdentity = ObjectIdentity
hlsTemporary = _HlsTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 21)
)
_HlsDot1dBridge_ObjectIdentity = ObjectIdentity
hlsDot1dBridge = _HlsDot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 21, 1)
)
_HlsDot1dBase_ObjectIdentity = ObjectIdentity
hlsDot1dBase = _HlsDot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1)
)
_HlsDot1dBaseBridgeAddress_Type = MacAddress
_HlsDot1dBaseBridgeAddress_Object = MibScalar
hlsDot1dBaseBridgeAddress = _HlsDot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 1),
    _HlsDot1dBaseBridgeAddress_Type()
)
hlsDot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBaseBridgeAddress.setStatus("mandatory")
_HlsDot1dBaseNumPorts_Type = Integer32
_HlsDot1dBaseNumPorts_Object = MibScalar
hlsDot1dBaseNumPorts = _HlsDot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 2),
    _HlsDot1dBaseNumPorts_Type()
)
hlsDot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBaseNumPorts.setStatus("mandatory")
_HlsDot1dBaseBridgeUpTime_Type = TimeTicks
_HlsDot1dBaseBridgeUpTime_Object = MibScalar
hlsDot1dBaseBridgeUpTime = _HlsDot1dBaseBridgeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 3),
    _HlsDot1dBaseBridgeUpTime_Type()
)
hlsDot1dBaseBridgeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBaseBridgeUpTime.setStatus("mandatory")


class _HlsDot1dBaseType_Type(Integer32):
    """Custom type hlsDot1dBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_HlsDot1dBaseType_Type.__name__ = "Integer32"
_HlsDot1dBaseType_Object = MibScalar
hlsDot1dBaseType = _HlsDot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 4),
    _HlsDot1dBaseType_Type()
)
hlsDot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBaseType.setStatus("mandatory")
_HlsDot1dBasePortTable_Object = MibTable
hlsDot1dBasePortTable = _HlsDot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hlsDot1dBasePortTable.setStatus("mandatory")
_HlsDot1dBasePortEntry_Object = MibTableRow
hlsDot1dBasePortEntry = _HlsDot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 5, 1)
)
hlsDot1dBasePortEntry.setIndexNames(
    (0, "HLS-MIB", "hlsDot1dBasePortIfIndex"),
)
if mibBuilder.loadTexts:
    hlsDot1dBasePortEntry.setStatus("mandatory")
_HlsDot1dBasePortIfIndex_Type = Integer32
_HlsDot1dBasePortIfIndex_Object = MibTableColumn
hlsDot1dBasePortIfIndex = _HlsDot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 5, 1, 1),
    _HlsDot1dBasePortIfIndex_Type()
)
hlsDot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBasePortIfIndex.setStatus("mandatory")
_HlsDot1dBasePortNoBufferDiscards_Type = Counter32
_HlsDot1dBasePortNoBufferDiscards_Object = MibTableColumn
hlsDot1dBasePortNoBufferDiscards = _HlsDot1dBasePortNoBufferDiscards_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 5, 1, 2),
    _HlsDot1dBasePortNoBufferDiscards_Type()
)
hlsDot1dBasePortNoBufferDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBasePortNoBufferDiscards.setStatus("mandatory")
_HlsDot1dBasePortDelayExceededDiscards_Type = Counter32
_HlsDot1dBasePortDelayExceededDiscards_Object = MibTableColumn
hlsDot1dBasePortDelayExceededDiscards = _HlsDot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 5, 1, 3),
    _HlsDot1dBasePortDelayExceededDiscards_Type()
)
hlsDot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBasePortDelayExceededDiscards.setStatus("mandatory")
_HlsDot1dBasePortMtuExceededDiscards_Type = Counter32
_HlsDot1dBasePortMtuExceededDiscards_Object = MibTableColumn
hlsDot1dBasePortMtuExceededDiscards = _HlsDot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 1, 5, 1, 4),
    _HlsDot1dBasePortMtuExceededDiscards_Type()
)
hlsDot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dBasePortMtuExceededDiscards.setStatus("mandatory")
_HlsDot1dStp_ObjectIdentity = ObjectIdentity
hlsDot1dStp = _HlsDot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2)
)


class _HlsDot1dStpProtocolSpecification_Type(Integer32):
    """Custom type hlsDot1dStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decprotocol", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_HlsDot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_HlsDot1dStpProtocolSpecification_Object = MibScalar
hlsDot1dStpProtocolSpecification = _HlsDot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 1),
    _HlsDot1dStpProtocolSpecification_Type()
)
hlsDot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpProtocolSpecification.setStatus("mandatory")


class _HlsDot1dStpPriority_Type(Integer32):
    """Custom type hlsDot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HlsDot1dStpPriority_Type.__name__ = "Integer32"
_HlsDot1dStpPriority_Object = MibScalar
hlsDot1dStpPriority = _HlsDot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 2),
    _HlsDot1dStpPriority_Type()
)
hlsDot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlsDot1dStpPriority.setStatus("mandatory")
_HlsDot1dStpLastTopChange_Type = TimeTicks
_HlsDot1dStpLastTopChange_Object = MibScalar
hlsDot1dStpLastTopChange = _HlsDot1dStpLastTopChange_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 3),
    _HlsDot1dStpLastTopChange_Type()
)
hlsDot1dStpLastTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpLastTopChange.setStatus("mandatory")
_HlsDot1dStpTopChanges_Type = Counter32
_HlsDot1dStpTopChanges_Object = MibScalar
hlsDot1dStpTopChanges = _HlsDot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 4),
    _HlsDot1dStpTopChanges_Type()
)
hlsDot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpTopChanges.setStatus("mandatory")


class _HlsDot1dStpDesignatedRoot_Type(OctetString):
    """Custom type hlsDot1dStpDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HlsDot1dStpDesignatedRoot_Type.__name__ = "OctetString"
_HlsDot1dStpDesignatedRoot_Object = MibScalar
hlsDot1dStpDesignatedRoot = _HlsDot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 5),
    _HlsDot1dStpDesignatedRoot_Type()
)
hlsDot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpDesignatedRoot.setStatus("mandatory")
_HlsDot1dStpRootCost_Type = Integer32
_HlsDot1dStpRootCost_Object = MibScalar
hlsDot1dStpRootCost = _HlsDot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 6),
    _HlsDot1dStpRootCost_Type()
)
hlsDot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpRootCost.setStatus("mandatory")
_HlsDot1dStpRootPort_Type = Integer32
_HlsDot1dStpRootPort_Object = MibScalar
hlsDot1dStpRootPort = _HlsDot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 7),
    _HlsDot1dStpRootPort_Type()
)
hlsDot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpRootPort.setStatus("mandatory")
_HlsDot1dStpMaxAge_Type = TimeTicks
_HlsDot1dStpMaxAge_Object = MibScalar
hlsDot1dStpMaxAge = _HlsDot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 8),
    _HlsDot1dStpMaxAge_Type()
)
hlsDot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpMaxAge.setStatus("mandatory")
_HlsDot1dStpHelloTime_Type = TimeTicks
_HlsDot1dStpHelloTime_Object = MibScalar
hlsDot1dStpHelloTime = _HlsDot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 9),
    _HlsDot1dStpHelloTime_Type()
)
hlsDot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpHelloTime.setStatus("mandatory")
_HlsDot1dStpForwardDelay_Type = TimeTicks
_HlsDot1dStpForwardDelay_Object = MibScalar
hlsDot1dStpForwardDelay = _HlsDot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 10),
    _HlsDot1dStpForwardDelay_Type()
)
hlsDot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpForwardDelay.setStatus("mandatory")
_HlsDot1dStpHoldTime_Type = TimeTicks
_HlsDot1dStpHoldTime_Object = MibScalar
hlsDot1dStpHoldTime = _HlsDot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 11),
    _HlsDot1dStpHoldTime_Type()
)
hlsDot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpHoldTime.setStatus("mandatory")
_HlsDot1dStpPortTable_Object = MibTable
hlsDot1dStpPortTable = _HlsDot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hlsDot1dStpPortTable.setStatus("mandatory")
_HlsDot1dStpPortEntry_Object = MibTableRow
hlsDot1dStpPortEntry = _HlsDot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1)
)
hlsDot1dStpPortEntry.setIndexNames(
    (0, "HLS-MIB", "hlsDot1dStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    hlsDot1dStpPortEntry.setStatus("mandatory")
_HlsDot1dStpPortIfIndex_Type = Integer32
_HlsDot1dStpPortIfIndex_Object = MibTableColumn
hlsDot1dStpPortIfIndex = _HlsDot1dStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 1),
    _HlsDot1dStpPortIfIndex_Type()
)
hlsDot1dStpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortIfIndex.setStatus("mandatory")


class _HlsDot1dStpPortPriority_Type(OctetString):
    """Custom type hlsDot1dStpPortPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HlsDot1dStpPortPriority_Type.__name__ = "OctetString"
_HlsDot1dStpPortPriority_Object = MibTableColumn
hlsDot1dStpPortPriority = _HlsDot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 2),
    _HlsDot1dStpPortPriority_Type()
)
hlsDot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlsDot1dStpPortPriority.setStatus("mandatory")
_HlsDot1dStpPortPortNum_Type = Integer32
_HlsDot1dStpPortPortNum_Object = MibTableColumn
hlsDot1dStpPortPortNum = _HlsDot1dStpPortPortNum_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 3),
    _HlsDot1dStpPortPortNum_Type()
)
hlsDot1dStpPortPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortPortNum.setStatus("mandatory")


class _HlsDot1dStpPortState_Type(Integer32):
    """Custom type hlsDot1dStpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 1),
          ("enabled", 2),
          ("forwarding", 6),
          ("learning", 5),
          ("listening", 4))
    )


_HlsDot1dStpPortState_Type.__name__ = "Integer32"
_HlsDot1dStpPortState_Object = MibTableColumn
hlsDot1dStpPortState = _HlsDot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 4),
    _HlsDot1dStpPortState_Type()
)
hlsDot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortState.setStatus("mandatory")
_HlsDot1dStpPortMultiCastAddr_Type = MacAddress
_HlsDot1dStpPortMultiCastAddr_Object = MibTableColumn
hlsDot1dStpPortMultiCastAddr = _HlsDot1dStpPortMultiCastAddr_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 5),
    _HlsDot1dStpPortMultiCastAddr_Type()
)
hlsDot1dStpPortMultiCastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortMultiCastAddr.setStatus("mandatory")
_HlsDot1dStpPortPathCost_Type = Integer32
_HlsDot1dStpPortPathCost_Object = MibTableColumn
hlsDot1dStpPortPathCost = _HlsDot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 6),
    _HlsDot1dStpPortPathCost_Type()
)
hlsDot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlsDot1dStpPortPathCost.setStatus("mandatory")


class _HlsDot1dStpPortDesignatedRoot_Type(OctetString):
    """Custom type hlsDot1dStpPortDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HlsDot1dStpPortDesignatedRoot_Type.__name__ = "OctetString"
_HlsDot1dStpPortDesignatedRoot_Object = MibTableColumn
hlsDot1dStpPortDesignatedRoot = _HlsDot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 7),
    _HlsDot1dStpPortDesignatedRoot_Type()
)
hlsDot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortDesignatedRoot.setStatus("mandatory")
_HlsDot1dStpPortDesignatedCost_Type = Integer32
_HlsDot1dStpPortDesignatedCost_Object = MibTableColumn
hlsDot1dStpPortDesignatedCost = _HlsDot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 8),
    _HlsDot1dStpPortDesignatedCost_Type()
)
hlsDot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortDesignatedCost.setStatus("mandatory")


class _HlsDot1dStpPortDesignatedBridge_Type(OctetString):
    """Custom type hlsDot1dStpPortDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HlsDot1dStpPortDesignatedBridge_Type.__name__ = "OctetString"
_HlsDot1dStpPortDesignatedBridge_Object = MibTableColumn
hlsDot1dStpPortDesignatedBridge = _HlsDot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 9),
    _HlsDot1dStpPortDesignatedBridge_Type()
)
hlsDot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortDesignatedBridge.setStatus("mandatory")


class _HlsDot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type hlsDot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HlsDot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_HlsDot1dStpPortDesignatedPort_Object = MibTableColumn
hlsDot1dStpPortDesignatedPort = _HlsDot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 10),
    _HlsDot1dStpPortDesignatedPort_Type()
)
hlsDot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortDesignatedPort.setStatus("mandatory")
_HlsDot1dStpPortInBPDUs_Type = Counter32
_HlsDot1dStpPortInBPDUs_Object = MibTableColumn
hlsDot1dStpPortInBPDUs = _HlsDot1dStpPortInBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 11),
    _HlsDot1dStpPortInBPDUs_Type()
)
hlsDot1dStpPortInBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortInBPDUs.setStatus("mandatory")
_HlsDot1dStpPortOutBPDUs_Type = Counter32
_HlsDot1dStpPortOutBPDUs_Object = MibTableColumn
hlsDot1dStpPortOutBPDUs = _HlsDot1dStpPortOutBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 26, 21, 1, 2, 12, 1, 12),
    _HlsDot1dStpPortOutBPDUs_Type()
)
hlsDot1dStpPortOutBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlsDot1dStpPortOutBPDUs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HLS-MIB",
    **{"MacAddress": MacAddress,
       "hls": hls,
       "hlsBridges": hlsBridges,
       "ethernetBridge": ethernetBridge,
       "ramAddrTab8000Tab": ramAddrTab8000Tab,
       "ramAddrTab8000Entry": ramAddrTab8000Entry,
       "ramAddrTab8000Address": ramAddrTab8000Address,
       "ramAddrTab8000Filter": ramAddrTab8000Filter,
       "ramAddrTab8000FilterNum": ramAddrTab8000FilterNum,
       "ramAddrTab8000FilterTab": ramAddrTab8000FilterTab,
       "ramAddrTab8000FilterEntry": ramAddrTab8000FilterEntry,
       "ramAddrTab8000FilterIndex": ramAddrTab8000FilterIndex,
       "ramAddrTab8000Delete": ramAddrTab8000Delete,
       "nvramAddrTab8000Tab": nvramAddrTab8000Tab,
       "nvramAddrTab8000Entry": nvramAddrTab8000Entry,
       "nvramAddrTab8000Address": nvramAddrTab8000Address,
       "nvramAddrTab8000Filter": nvramAddrTab8000Filter,
       "nvramAddrTab8000FilterNum": nvramAddrTab8000FilterNum,
       "nvramAddrTab8000FilterTab": nvramAddrTab8000FilterTab,
       "nvramAddrTab8000FilterEntry": nvramAddrTab8000FilterEntry,
       "nvramAddrTab8000FilterIndex": nvramAddrTab8000FilterIndex,
       "nvramAddrTab8000Delete": nvramAddrTab8000Delete,
       "nvramAddrTab8000Update": nvramAddrTab8000Update,
       "remoteEthernetBridge": remoteEthernetBridge,
       "segmentBlocking": segmentBlocking,
       "linktype": linktype,
       "linkSaver": linkSaver,
       "crcType": crcType,
       "linkEncoding": linkEncoding,
       "tokenBusBridge": tokenBusBridge,
       "tbTransmitLevel": tbTransmitLevel,
       "tbSlotTime": tbSlotTime,
       "tbHoldtime": tbHoldtime,
       "tbRotationTime": tbRotationTime,
       "tbRingTimerInitialValue": tbRingTimerInitialValue,
       "tbSolicitCount": tbSolicitCount,
       "tbResetDefault": tbResetDefault,
       "tbFrequency": tbFrequency,
       "ramAddrTab8200Tab": ramAddrTab8200Tab,
       "ramAddrTab8200Entry": ramAddrTab8200Entry,
       "ramAddrTab8200Address": ramAddrTab8200Address,
       "ramAddrTab8200Filter": ramAddrTab8200Filter,
       "ramAddrTab8200FilterNum": ramAddrTab8200FilterNum,
       "ramAddrTab8200FilterTab": ramAddrTab8200FilterTab,
       "ramAddrTab8200FilterEntry": ramAddrTab8200FilterEntry,
       "ramAddrTab8200FilterIndex": ramAddrTab8200FilterIndex,
       "ramAddrTab8200Delete": ramAddrTab8200Delete,
       "nvramAddrTab8200Tab": nvramAddrTab8200Tab,
       "nvramAddrTab8200Entry": nvramAddrTab8200Entry,
       "nvramAddrTab8200Address": nvramAddrTab8200Address,
       "nvramAddrTab8200Filter": nvramAddrTab8200Filter,
       "nvramAddrTab8200FilterNum": nvramAddrTab8200FilterNum,
       "nvramAddrTab8200FilterTab": nvramAddrTab8200FilterTab,
       "nvramAddrTab8200FilterEntry": nvramAddrTab8200FilterEntry,
       "nvramAddrTab8200FilterIndex": nvramAddrTab8200FilterIndex,
       "nvramAddrTab8200Delete": nvramAddrTab8200Delete,
       "nvramAddrTab8200Update": nvramAddrTab8200Update,
       "tbEbitErrors": tbEbitErrors,
       "tbFrameFrags": tbFrameFrags,
       "tbTokenPassFails": tbTokenPassFails,
       "bridgeModel": bridgeModel,
       "bridgeMode": bridgeMode,
       "ageingOption": ageingOption,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "chLearnMode": chLearnMode,
       "chRestrictMode": chRestrictMode,
       "chOriginMode": chOriginMode,
       "chGroupFwdMode": chGroupFwdMode,
       "chIndFwdMode": chIndFwdMode,
       "chDefRestrictFlag": chDefRestrictFlag,
       "chDefStaticFlag": chDefStaticFlag,
       "chDefOriginFlag": chDefOriginFlag,
       "chInCRCs": chInCRCs,
       "chInOverruns": chInOverruns,
       "chOutColls": chOutColls,
       "chWhos": chWhos,
       "chInRunts": chInRunts,
       "chInGiants": chInGiants,
       "chInLenErrors": chInLenErrors,
       "chInLocks": chInLocks,
       "chOutLocks": chOutLocks,
       "chNoBuffers": chNoBuffers,
       "channelNumber": channelNumber,
       "protocolBlocking": protocolBlocking,
       "resetLogTable": resetLogTable,
       "resetLogEntry": resetLogEntry,
       "reason": reason,
       "uptime": uptime,
       "entryNumber": entryNumber,
       "packetSize": packetSize,
       "transmitDeadmanTimer": transmitDeadmanTimer,
       "receiveDeadmanTimer": receiveDeadmanTimer,
       "tokenRingBridge": tokenRingBridge,
       "trBridgeNumber": trBridgeNumber,
       "trChannelTable": trChannelTable,
       "trChannelEntry": trChannelEntry,
       "trRingNumber": trRingNumber,
       "trSRAstate": trSRAstate,
       "protocolFilterTable": protocolFilterTable,
       "protocolFilterEntry": protocolFilterEntry,
       "protocolFilterStatus": protocolFilterStatus,
       "protocolFilterType": protocolFilterType,
       "sysType": sysType,
       "serialNumber": serialNumber,
       "bootPromVersion": bootPromVersion,
       "sysAdmAccess": sysAdmAccess,
       "appSwVersion": appSwVersion,
       "userProfile": userProfile,
       "hlsMibVersion": hlsMibVersion,
       "myManager": myManager,
       "sysReset": sysReset,
       "clearCounters": clearCounters,
       "systemDate": systemDate,
       "systemTime": systemTime,
       "alarmOption": alarmOption,
       "snmpAccess": snmpAccess,
       "myIpAddress": myIpAddress,
       "defaultGateway": defaultGateway,
       "netMask": netMask,
       "hlsSystem": hlsSystem,
       "snmpAuth": snmpAuth,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapDestination": trapDestination,
       "genericTrapSwitches": genericTrapSwitches,
       "specificTrapSwitches": specificTrapSwitches,
       "trapEntryNumber": trapEntryNumber,
       "hlsTemporary": hlsTemporary,
       "hlsDot1dBridge": hlsDot1dBridge,
       "hlsDot1dBase": hlsDot1dBase,
       "hlsDot1dBaseBridgeAddress": hlsDot1dBaseBridgeAddress,
       "hlsDot1dBaseNumPorts": hlsDot1dBaseNumPorts,
       "hlsDot1dBaseBridgeUpTime": hlsDot1dBaseBridgeUpTime,
       "hlsDot1dBaseType": hlsDot1dBaseType,
       "hlsDot1dBasePortTable": hlsDot1dBasePortTable,
       "hlsDot1dBasePortEntry": hlsDot1dBasePortEntry,
       "hlsDot1dBasePortIfIndex": hlsDot1dBasePortIfIndex,
       "hlsDot1dBasePortNoBufferDiscards": hlsDot1dBasePortNoBufferDiscards,
       "hlsDot1dBasePortDelayExceededDiscards": hlsDot1dBasePortDelayExceededDiscards,
       "hlsDot1dBasePortMtuExceededDiscards": hlsDot1dBasePortMtuExceededDiscards,
       "hlsDot1dStp": hlsDot1dStp,
       "hlsDot1dStpProtocolSpecification": hlsDot1dStpProtocolSpecification,
       "hlsDot1dStpPriority": hlsDot1dStpPriority,
       "hlsDot1dStpLastTopChange": hlsDot1dStpLastTopChange,
       "hlsDot1dStpTopChanges": hlsDot1dStpTopChanges,
       "hlsDot1dStpDesignatedRoot": hlsDot1dStpDesignatedRoot,
       "hlsDot1dStpRootCost": hlsDot1dStpRootCost,
       "hlsDot1dStpRootPort": hlsDot1dStpRootPort,
       "hlsDot1dStpMaxAge": hlsDot1dStpMaxAge,
       "hlsDot1dStpHelloTime": hlsDot1dStpHelloTime,
       "hlsDot1dStpForwardDelay": hlsDot1dStpForwardDelay,
       "hlsDot1dStpHoldTime": hlsDot1dStpHoldTime,
       "hlsDot1dStpPortTable": hlsDot1dStpPortTable,
       "hlsDot1dStpPortEntry": hlsDot1dStpPortEntry,
       "hlsDot1dStpPortIfIndex": hlsDot1dStpPortIfIndex,
       "hlsDot1dStpPortPriority": hlsDot1dStpPortPriority,
       "hlsDot1dStpPortPortNum": hlsDot1dStpPortPortNum,
       "hlsDot1dStpPortState": hlsDot1dStpPortState,
       "hlsDot1dStpPortMultiCastAddr": hlsDot1dStpPortMultiCastAddr,
       "hlsDot1dStpPortPathCost": hlsDot1dStpPortPathCost,
       "hlsDot1dStpPortDesignatedRoot": hlsDot1dStpPortDesignatedRoot,
       "hlsDot1dStpPortDesignatedCost": hlsDot1dStpPortDesignatedCost,
       "hlsDot1dStpPortDesignatedBridge": hlsDot1dStpPortDesignatedBridge,
       "hlsDot1dStpPortDesignatedPort": hlsDot1dStpPortDesignatedPort,
       "hlsDot1dStpPortInBPDUs": hlsDot1dStpPortInBPDUs,
       "hlsDot1dStpPortOutBPDUs": hlsDot1dStpPortOutBPDUs}
)
