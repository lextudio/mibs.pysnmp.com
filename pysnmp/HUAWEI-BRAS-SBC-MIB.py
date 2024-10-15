# SNMP MIB module (HUAWEI-BRAS-SBC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-SBC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:07 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBrasSbcMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25)
)
hwBrasSbcMgmt.setRevisions(
        ("2007-08-14 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWBrasEnabledStatus(Integer32, TextualConvention):
    status = "current"
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



class HWBrasPermitStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )



class HWBrasSecurityProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("h323", 3),
          ("mgcp", 2),
          ("signaling", 4),
          ("sip", 1))
    )



class HWBrasSbcBaseProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("h248", 6),
          ("ido", 7),
          ("mgcp", 2),
          ("q931", 8),
          ("ras", 4),
          ("sip", 1),
          ("snmp", 3),
          ("upath", 5))
    )



class HwBrasAppMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiDomain", 2),
          ("singleDomain", 1))
    )



class HwBrasBWLimitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("be", 1),
          ("qos", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwBrasSbcModule_ObjectIdentity = ObjectIdentity
hwBrasSbcModule = _HwBrasSbcModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2)
)
_HwBrasSbcObjects_ObjectIdentity = ObjectIdentity
hwBrasSbcObjects = _HwBrasSbcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1)
)
_HwBrasSbcGeneral_ObjectIdentity = ObjectIdentity
hwBrasSbcGeneral = _HwBrasSbcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1)
)
_HwBrasSbcBase_ObjectIdentity = ObjectIdentity
hwBrasSbcBase = _HwBrasSbcBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1)
)
_HwBrasSbcBaseLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcBaseLeaves = _HwBrasSbcBaseLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1)
)


class _HwBrasSbcStatisticEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcStatisticEnable based on HWBrasEnabledStatus"""


_HwBrasSbcStatisticEnable_Object = MibScalar
hwBrasSbcStatisticEnable = _HwBrasSbcStatisticEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1, 1),
    _HwBrasSbcStatisticEnable_Type()
)
hwBrasSbcStatisticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticEnable.setStatus("current")


class _HwBrasSbcStatisticSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcStatisticSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcStatisticSyslogEnable_Object = MibScalar
hwBrasSbcStatisticSyslogEnable = _HwBrasSbcStatisticSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1, 2),
    _HwBrasSbcStatisticSyslogEnable_Type()
)
hwBrasSbcStatisticSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticSyslogEnable.setStatus("current")


class _HwBrasSbcAppMode_Type(HwBrasAppMode):
    """Custom type hwBrasSbcAppMode based on HwBrasAppMode"""


_HwBrasSbcAppMode_Object = MibScalar
hwBrasSbcAppMode = _HwBrasSbcAppMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1, 3),
    _HwBrasSbcAppMode_Type()
)
hwBrasSbcAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcAppMode.setStatus("current")


class _HwBrasSbcMediaDetectValidityEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMediaDetectValidityEnable based on HWBrasEnabledStatus"""


_HwBrasSbcMediaDetectValidityEnable_Object = MibScalar
hwBrasSbcMediaDetectValidityEnable = _HwBrasSbcMediaDetectValidityEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1, 4),
    _HwBrasSbcMediaDetectValidityEnable_Type()
)
hwBrasSbcMediaDetectValidityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaDetectValidityEnable.setStatus("current")


class _HwBrasSbcMediaDetectSsrcEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMediaDetectSsrcEnable based on HWBrasEnabledStatus"""


_HwBrasSbcMediaDetectSsrcEnable_Object = MibScalar
hwBrasSbcMediaDetectSsrcEnable = _HwBrasSbcMediaDetectSsrcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1, 5),
    _HwBrasSbcMediaDetectSsrcEnable_Type()
)
hwBrasSbcMediaDetectSsrcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaDetectSsrcEnable.setStatus("current")


class _HwBrasSbcMediaDetectPacketLength_Type(Unsigned32):
    """Custom type hwBrasSbcMediaDetectPacketLength based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(28, 65535),
    )


_HwBrasSbcMediaDetectPacketLength_Type.__name__ = "Unsigned32"
_HwBrasSbcMediaDetectPacketLength_Object = MibScalar
hwBrasSbcMediaDetectPacketLength = _HwBrasSbcMediaDetectPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 1, 6),
    _HwBrasSbcMediaDetectPacketLength_Type()
)
hwBrasSbcMediaDetectPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaDetectPacketLength.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcMediaDetectPacketLength.setUnits("byte")
_HwBrasSbcBaseTables_ObjectIdentity = ObjectIdentity
hwBrasSbcBaseTables = _HwBrasSbcBaseTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2)
)
_HwBrasSbcSignalAddrMapTable_Object = MibTable
hwBrasSbcSignalAddrMapTable = _HwBrasSbcSignalAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapTable.setStatus("current")
_HwBrasSbcSignalAddrMapEntry_Object = MibTableRow
hwBrasSbcSignalAddrMapEntry = _HwBrasSbcSignalAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1, 1)
)
hwBrasSbcSignalAddrMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalAddrMapClientAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalAddrMapServerAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapEntry.setStatus("current")
_HwBrasSbcSignalAddrMapClientAddr_Type = IpAddress
_HwBrasSbcSignalAddrMapClientAddr_Object = MibTableColumn
hwBrasSbcSignalAddrMapClientAddr = _HwBrasSbcSignalAddrMapClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1, 1, 1),
    _HwBrasSbcSignalAddrMapClientAddr_Type()
)
hwBrasSbcSignalAddrMapClientAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapClientAddr.setStatus("current")
_HwBrasSbcSignalAddrMapServerAddr_Type = IpAddress
_HwBrasSbcSignalAddrMapServerAddr_Object = MibTableColumn
hwBrasSbcSignalAddrMapServerAddr = _HwBrasSbcSignalAddrMapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1, 1, 2),
    _HwBrasSbcSignalAddrMapServerAddr_Type()
)
hwBrasSbcSignalAddrMapServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapServerAddr.setStatus("current")
_HwBrasSbcSignalAddrMapSoftAddr_Type = IpAddress
_HwBrasSbcSignalAddrMapSoftAddr_Object = MibTableColumn
hwBrasSbcSignalAddrMapSoftAddr = _HwBrasSbcSignalAddrMapSoftAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1, 1, 3),
    _HwBrasSbcSignalAddrMapSoftAddr_Type()
)
hwBrasSbcSignalAddrMapSoftAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapSoftAddr.setStatus("current")
_HwBrasSbcSignalAddrMapIadmsAddr_Type = IpAddress
_HwBrasSbcSignalAddrMapIadmsAddr_Object = MibTableColumn
hwBrasSbcSignalAddrMapIadmsAddr = _HwBrasSbcSignalAddrMapIadmsAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1, 1, 4),
    _HwBrasSbcSignalAddrMapIadmsAddr_Type()
)
hwBrasSbcSignalAddrMapIadmsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapIadmsAddr.setStatus("current")
_HwBrasSbcSignalAddrMapRowStatus_Type = RowStatus
_HwBrasSbcSignalAddrMapRowStatus_Object = MibTableColumn
hwBrasSbcSignalAddrMapRowStatus = _HwBrasSbcSignalAddrMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 1, 1, 5),
    _HwBrasSbcSignalAddrMapRowStatus_Type()
)
hwBrasSbcSignalAddrMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSignalAddrMapRowStatus.setStatus("current")
_HwBrasSbcMediaAddrMapTable_Object = MibTable
hwBrasSbcMediaAddrMapTable = _HwBrasSbcMediaAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcMediaAddrMapTable.setStatus("current")
_HwBrasSbcMediaAddrMapEntry_Object = MibTableRow
hwBrasSbcMediaAddrMapEntry = _HwBrasSbcMediaAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 2, 1)
)
hwBrasSbcMediaAddrMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaAddrMapClientAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMediaAddrMapEntry.setStatus("current")
_HwBrasSbcMediaAddrMapClientAddr_Type = IpAddress
_HwBrasSbcMediaAddrMapClientAddr_Object = MibTableColumn
hwBrasSbcMediaAddrMapClientAddr = _HwBrasSbcMediaAddrMapClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 2, 1, 1),
    _HwBrasSbcMediaAddrMapClientAddr_Type()
)
hwBrasSbcMediaAddrMapClientAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMediaAddrMapClientAddr.setStatus("current")
_HwBrasSbcMediaAddrMapServerAddr_Type = IpAddress
_HwBrasSbcMediaAddrMapServerAddr_Object = MibTableColumn
hwBrasSbcMediaAddrMapServerAddr = _HwBrasSbcMediaAddrMapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 2, 1, 2),
    _HwBrasSbcMediaAddrMapServerAddr_Type()
)
hwBrasSbcMediaAddrMapServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaAddrMapServerAddr.setStatus("current")


class _HwBrasSbcMediaAddrMapWeight_Type(Unsigned32):
    """Custom type hwBrasSbcMediaAddrMapWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_HwBrasSbcMediaAddrMapWeight_Type.__name__ = "Unsigned32"
_HwBrasSbcMediaAddrMapWeight_Object = MibTableColumn
hwBrasSbcMediaAddrMapWeight = _HwBrasSbcMediaAddrMapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 2, 1, 3),
    _HwBrasSbcMediaAddrMapWeight_Type()
)
hwBrasSbcMediaAddrMapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaAddrMapWeight.setStatus("current")
_HwBrasSbcMediaAddrMapRowStatus_Type = RowStatus
_HwBrasSbcMediaAddrMapRowStatus_Object = MibTableColumn
hwBrasSbcMediaAddrMapRowStatus = _HwBrasSbcMediaAddrMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 2, 1, 4),
    _HwBrasSbcMediaAddrMapRowStatus_Type()
)
hwBrasSbcMediaAddrMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaAddrMapRowStatus.setStatus("current")
_HwBrasSbcPortrangeTable_Object = MibTable
hwBrasSbcPortrangeTable = _HwBrasSbcPortrangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcPortrangeTable.setStatus("current")
_HwBrasSbcPortrangeEntry_Object = MibTableRow
hwBrasSbcPortrangeEntry = _HwBrasSbcPortrangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 3, 1)
)
hwBrasSbcPortrangeEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPortrangeIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcPortrangeEntry.setStatus("current")


class _HwBrasSbcPortrangeIndex_Type(Integer32):
    """Custom type hwBrasSbcPortrangeIndex based on Integer32"""
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
        *(("media", 2),
          ("mediacur", 6),
          ("nat", 3),
          ("signal", 1),
          ("tcp", 4),
          ("udp", 5))
    )


_HwBrasSbcPortrangeIndex_Type.__name__ = "Integer32"
_HwBrasSbcPortrangeIndex_Object = MibTableColumn
hwBrasSbcPortrangeIndex = _HwBrasSbcPortrangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 3, 1, 1),
    _HwBrasSbcPortrangeIndex_Type()
)
hwBrasSbcPortrangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcPortrangeIndex.setStatus("current")


class _HwBrasSbcPortrangeBegin_Type(Unsigned32):
    """Custom type hwBrasSbcPortrangeBegin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10001, 65535),
    )


_HwBrasSbcPortrangeBegin_Type.__name__ = "Unsigned32"
_HwBrasSbcPortrangeBegin_Object = MibTableColumn
hwBrasSbcPortrangeBegin = _HwBrasSbcPortrangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 3, 1, 2),
    _HwBrasSbcPortrangeBegin_Type()
)
hwBrasSbcPortrangeBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcPortrangeBegin.setStatus("current")


class _HwBrasSbcPortrangeEnd_Type(Unsigned32):
    """Custom type hwBrasSbcPortrangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10001, 65535),
    )


_HwBrasSbcPortrangeEnd_Type.__name__ = "Unsigned32"
_HwBrasSbcPortrangeEnd_Object = MibTableColumn
hwBrasSbcPortrangeEnd = _HwBrasSbcPortrangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 3, 1, 3),
    _HwBrasSbcPortrangeEnd_Type()
)
hwBrasSbcPortrangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcPortrangeEnd.setStatus("current")
_HwBrasSbcPortrangeRowStatus_Type = RowStatus
_HwBrasSbcPortrangeRowStatus_Object = MibTableColumn
hwBrasSbcPortrangeRowStatus = _HwBrasSbcPortrangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 3, 1, 4),
    _HwBrasSbcPortrangeRowStatus_Type()
)
hwBrasSbcPortrangeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcPortrangeRowStatus.setStatus("current")
_HwBrasSbcStatMediaPacketTable_Object = MibTable
hwBrasSbcStatMediaPacketTable = _HwBrasSbcStatMediaPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcStatMediaPacketTable.setStatus("current")
_HwBrasSbcStatMediaPacketEntry_Object = MibTableRow
hwBrasSbcStatMediaPacketEntry = _HwBrasSbcStatMediaPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 4, 1)
)
hwBrasSbcStatMediaPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatMediaPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcStatMediaPacketEntry.setStatus("current")


class _HwBrasSbcStatMediaPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcStatMediaPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtcp", 2),
          ("rtp", 1))
    )


_HwBrasSbcStatMediaPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcStatMediaPacketIndex_Object = MibTableColumn
hwBrasSbcStatMediaPacketIndex = _HwBrasSbcStatMediaPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 4, 1, 1),
    _HwBrasSbcStatMediaPacketIndex_Type()
)
hwBrasSbcStatMediaPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcStatMediaPacketIndex.setStatus("current")
_HwBrasSbcStatMediaPacketNumber_Type = Counter64
_HwBrasSbcStatMediaPacketNumber_Object = MibTableColumn
hwBrasSbcStatMediaPacketNumber = _HwBrasSbcStatMediaPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 4, 1, 2),
    _HwBrasSbcStatMediaPacketNumber_Type()
)
hwBrasSbcStatMediaPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcStatMediaPacketNumber.setStatus("current")
_HwBrasSbcStatMediaPacketOctet_Type = Counter64
_HwBrasSbcStatMediaPacketOctet_Object = MibTableColumn
hwBrasSbcStatMediaPacketOctet = _HwBrasSbcStatMediaPacketOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 4, 1, 3),
    _HwBrasSbcStatMediaPacketOctet_Type()
)
hwBrasSbcStatMediaPacketOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcStatMediaPacketOctet.setStatus("current")
_HwBrasSbcStatMediaPacketRowStatus_Type = RowStatus
_HwBrasSbcStatMediaPacketRowStatus_Object = MibTableColumn
hwBrasSbcStatMediaPacketRowStatus = _HwBrasSbcStatMediaPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 4, 1, 4),
    _HwBrasSbcStatMediaPacketRowStatus_Type()
)
hwBrasSbcStatMediaPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcStatMediaPacketRowStatus.setStatus("current")
_HwBrasSbcClientPortTable_Object = MibTable
hwBrasSbcClientPortTable = _HwBrasSbcClientPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcClientPortTable.setStatus("current")
_HwBrasSbcClientPortEntry_Object = MibTableRow
hwBrasSbcClientPortEntry = _HwBrasSbcClientPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1)
)
hwBrasSbcClientPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortVPN"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortIP"),
)
if mibBuilder.loadTexts:
    hwBrasSbcClientPortEntry.setStatus("current")


class _HwBrasSbcClientPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcClientPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("h248", 6),
          ("ido", 7),
          ("mgcp", 2),
          ("ras", 4),
          ("sip", 1),
          ("snmp", 3),
          ("upath", 5))
    )


_HwBrasSbcClientPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcClientPortProtocol_Object = MibTableColumn
hwBrasSbcClientPortProtocol = _HwBrasSbcClientPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 1),
    _HwBrasSbcClientPortProtocol_Type()
)
hwBrasSbcClientPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortProtocol.setStatus("current")


class _HwBrasSbcClientPortVPN_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcClientPortVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortVPN_Object = MibTableColumn
hwBrasSbcClientPortVPN = _HwBrasSbcClientPortVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 2),
    _HwBrasSbcClientPortVPN_Type()
)
hwBrasSbcClientPortVPN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortVPN.setStatus("current")
_HwBrasSbcClientPortIP_Type = IpAddress
_HwBrasSbcClientPortIP_Object = MibTableColumn
hwBrasSbcClientPortIP = _HwBrasSbcClientPortIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 3),
    _HwBrasSbcClientPortIP_Type()
)
hwBrasSbcClientPortIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortIP.setStatus("current")


class _HwBrasSbcClientPortPort01_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort01_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort01_Object = MibTableColumn
hwBrasSbcClientPortPort01 = _HwBrasSbcClientPortPort01_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 11),
    _HwBrasSbcClientPortPort01_Type()
)
hwBrasSbcClientPortPort01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort01.setStatus("current")


class _HwBrasSbcClientPortPort02_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort02 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort02_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort02_Object = MibTableColumn
hwBrasSbcClientPortPort02 = _HwBrasSbcClientPortPort02_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 12),
    _HwBrasSbcClientPortPort02_Type()
)
hwBrasSbcClientPortPort02.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort02.setStatus("current")


class _HwBrasSbcClientPortPort03_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort03 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort03_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort03_Object = MibTableColumn
hwBrasSbcClientPortPort03 = _HwBrasSbcClientPortPort03_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 13),
    _HwBrasSbcClientPortPort03_Type()
)
hwBrasSbcClientPortPort03.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort03.setStatus("current")


class _HwBrasSbcClientPortPort04_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort04 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort04_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort04_Object = MibTableColumn
hwBrasSbcClientPortPort04 = _HwBrasSbcClientPortPort04_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 14),
    _HwBrasSbcClientPortPort04_Type()
)
hwBrasSbcClientPortPort04.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort04.setStatus("current")


class _HwBrasSbcClientPortPort05_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort05 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort05_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort05_Object = MibTableColumn
hwBrasSbcClientPortPort05 = _HwBrasSbcClientPortPort05_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 15),
    _HwBrasSbcClientPortPort05_Type()
)
hwBrasSbcClientPortPort05.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort05.setStatus("current")


class _HwBrasSbcClientPortPort06_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort06 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort06_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort06_Object = MibTableColumn
hwBrasSbcClientPortPort06 = _HwBrasSbcClientPortPort06_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 16),
    _HwBrasSbcClientPortPort06_Type()
)
hwBrasSbcClientPortPort06.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort06.setStatus("current")


class _HwBrasSbcClientPortPort07_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort07 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort07_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort07_Object = MibTableColumn
hwBrasSbcClientPortPort07 = _HwBrasSbcClientPortPort07_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 17),
    _HwBrasSbcClientPortPort07_Type()
)
hwBrasSbcClientPortPort07.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort07.setStatus("current")


class _HwBrasSbcClientPortPort08_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort08 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort08_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort08_Object = MibTableColumn
hwBrasSbcClientPortPort08 = _HwBrasSbcClientPortPort08_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 18),
    _HwBrasSbcClientPortPort08_Type()
)
hwBrasSbcClientPortPort08.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort08.setStatus("current")


class _HwBrasSbcClientPortPort09_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort09 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort09_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort09_Object = MibTableColumn
hwBrasSbcClientPortPort09 = _HwBrasSbcClientPortPort09_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 19),
    _HwBrasSbcClientPortPort09_Type()
)
hwBrasSbcClientPortPort09.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort09.setStatus("current")


class _HwBrasSbcClientPortPort10_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort10_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort10_Object = MibTableColumn
hwBrasSbcClientPortPort10 = _HwBrasSbcClientPortPort10_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 20),
    _HwBrasSbcClientPortPort10_Type()
)
hwBrasSbcClientPortPort10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort10.setStatus("current")


class _HwBrasSbcClientPortPort11_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort11_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort11_Object = MibTableColumn
hwBrasSbcClientPortPort11 = _HwBrasSbcClientPortPort11_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 21),
    _HwBrasSbcClientPortPort11_Type()
)
hwBrasSbcClientPortPort11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort11.setStatus("current")


class _HwBrasSbcClientPortPort12_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort12_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort12_Object = MibTableColumn
hwBrasSbcClientPortPort12 = _HwBrasSbcClientPortPort12_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 22),
    _HwBrasSbcClientPortPort12_Type()
)
hwBrasSbcClientPortPort12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort12.setStatus("current")


class _HwBrasSbcClientPortPort13_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort13_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort13_Object = MibTableColumn
hwBrasSbcClientPortPort13 = _HwBrasSbcClientPortPort13_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 23),
    _HwBrasSbcClientPortPort13_Type()
)
hwBrasSbcClientPortPort13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort13.setStatus("current")


class _HwBrasSbcClientPortPort14_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort14_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort14_Object = MibTableColumn
hwBrasSbcClientPortPort14 = _HwBrasSbcClientPortPort14_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 24),
    _HwBrasSbcClientPortPort14_Type()
)
hwBrasSbcClientPortPort14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort14.setStatus("current")


class _HwBrasSbcClientPortPort15_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort15_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort15_Object = MibTableColumn
hwBrasSbcClientPortPort15 = _HwBrasSbcClientPortPort15_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 25),
    _HwBrasSbcClientPortPort15_Type()
)
hwBrasSbcClientPortPort15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort15.setStatus("current")


class _HwBrasSbcClientPortPort16_Type(Unsigned32):
    """Custom type hwBrasSbcClientPortPort16 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcClientPortPort16_Type.__name__ = "Unsigned32"
_HwBrasSbcClientPortPort16_Object = MibTableColumn
hwBrasSbcClientPortPort16 = _HwBrasSbcClientPortPort16_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 26),
    _HwBrasSbcClientPortPort16_Type()
)
hwBrasSbcClientPortPort16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortPort16.setStatus("current")
_HwBrasSbcClientPortRowStatus_Type = RowStatus
_HwBrasSbcClientPortRowStatus_Object = MibTableColumn
hwBrasSbcClientPortRowStatus = _HwBrasSbcClientPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 5, 1, 51),
    _HwBrasSbcClientPortRowStatus_Type()
)
hwBrasSbcClientPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcClientPortRowStatus.setStatus("current")
_HwBrasSbcSoftswitchPortTable_Object = MibTable
hwBrasSbcSoftswitchPortTable = _HwBrasSbcSoftswitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortTable.setStatus("current")
_HwBrasSbcSoftswitchPortEntry_Object = MibTableRow
hwBrasSbcSoftswitchPortEntry = _HwBrasSbcSoftswitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6, 1)
)
hwBrasSbcSoftswitchPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSoftswitchPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSoftswitchPortVPN"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSoftswitchPortIP"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortEntry.setStatus("current")


class _HwBrasSbcSoftswitchPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcSoftswitchPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("h248", 6),
          ("ido", 7),
          ("mgcp", 2),
          ("q931", 8),
          ("ras", 4),
          ("sip", 1),
          ("upath", 5))
    )


_HwBrasSbcSoftswitchPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcSoftswitchPortProtocol_Object = MibTableColumn
hwBrasSbcSoftswitchPortProtocol = _HwBrasSbcSoftswitchPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6, 1, 1),
    _HwBrasSbcSoftswitchPortProtocol_Type()
)
hwBrasSbcSoftswitchPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortProtocol.setStatus("current")


class _HwBrasSbcSoftswitchPortVPN_Type(Unsigned32):
    """Custom type hwBrasSbcSoftswitchPortVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcSoftswitchPortVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcSoftswitchPortVPN_Object = MibTableColumn
hwBrasSbcSoftswitchPortVPN = _HwBrasSbcSoftswitchPortVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6, 1, 2),
    _HwBrasSbcSoftswitchPortVPN_Type()
)
hwBrasSbcSoftswitchPortVPN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortVPN.setStatus("current")
_HwBrasSbcSoftswitchPortIP_Type = IpAddress
_HwBrasSbcSoftswitchPortIP_Object = MibTableColumn
hwBrasSbcSoftswitchPortIP = _HwBrasSbcSoftswitchPortIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6, 1, 3),
    _HwBrasSbcSoftswitchPortIP_Type()
)
hwBrasSbcSoftswitchPortIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortIP.setStatus("current")


class _HwBrasSbcSoftswitchPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcSoftswitchPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcSoftswitchPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcSoftswitchPortPort_Object = MibTableColumn
hwBrasSbcSoftswitchPortPort = _HwBrasSbcSoftswitchPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6, 1, 11),
    _HwBrasSbcSoftswitchPortPort_Type()
)
hwBrasSbcSoftswitchPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortPort.setStatus("current")
_HwBrasSbcSoftswitchPortRowStatus_Type = RowStatus
_HwBrasSbcSoftswitchPortRowStatus_Object = MibTableColumn
hwBrasSbcSoftswitchPortRowStatus = _HwBrasSbcSoftswitchPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 6, 1, 51),
    _HwBrasSbcSoftswitchPortRowStatus_Type()
)
hwBrasSbcSoftswitchPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSoftswitchPortRowStatus.setStatus("current")
_HwBrasSbcIadmsPortTable_Object = MibTable
hwBrasSbcIadmsPortTable = _HwBrasSbcIadmsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortTable.setStatus("current")
_HwBrasSbcIadmsPortEntry_Object = MibTableRow
hwBrasSbcIadmsPortEntry = _HwBrasSbcIadmsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7, 1)
)
hwBrasSbcIadmsPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsPortVPN"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsPortIP"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortEntry.setStatus("current")


class _HwBrasSbcIadmsPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcIadmsPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("snmp", 3)
    )


_HwBrasSbcIadmsPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIadmsPortProtocol_Object = MibTableColumn
hwBrasSbcIadmsPortProtocol = _HwBrasSbcIadmsPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7, 1, 1),
    _HwBrasSbcIadmsPortProtocol_Type()
)
hwBrasSbcIadmsPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortProtocol.setStatus("current")


class _HwBrasSbcIadmsPortVPN_Type(Unsigned32):
    """Custom type hwBrasSbcIadmsPortVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcIadmsPortVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcIadmsPortVPN_Object = MibTableColumn
hwBrasSbcIadmsPortVPN = _HwBrasSbcIadmsPortVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7, 1, 2),
    _HwBrasSbcIadmsPortVPN_Type()
)
hwBrasSbcIadmsPortVPN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortVPN.setStatus("current")
_HwBrasSbcIadmsPortIP_Type = IpAddress
_HwBrasSbcIadmsPortIP_Object = MibTableColumn
hwBrasSbcIadmsPortIP = _HwBrasSbcIadmsPortIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7, 1, 3),
    _HwBrasSbcIadmsPortIP_Type()
)
hwBrasSbcIadmsPortIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortIP.setStatus("current")


class _HwBrasSbcIadmsPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcIadmsPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcIadmsPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcIadmsPortPort_Object = MibTableColumn
hwBrasSbcIadmsPortPort = _HwBrasSbcIadmsPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7, 1, 11),
    _HwBrasSbcIadmsPortPort_Type()
)
hwBrasSbcIadmsPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortPort.setStatus("current")
_HwBrasSbcIadmsPortRowStatus_Type = RowStatus
_HwBrasSbcIadmsPortRowStatus_Object = MibTableColumn
hwBrasSbcIadmsPortRowStatus = _HwBrasSbcIadmsPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 7, 1, 51),
    _HwBrasSbcIadmsPortRowStatus_Type()
)
hwBrasSbcIadmsPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsPortRowStatus.setStatus("current")
_HwBrasSbcInstanceTable_Object = MibTable
hwBrasSbcInstanceTable = _HwBrasSbcInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hwBrasSbcInstanceTable.setStatus("current")
_HwBrasSbcInstanceEntry_Object = MibTableRow
hwBrasSbcInstanceEntry = _HwBrasSbcInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 8, 1)
)
hwBrasSbcInstanceEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcInstanceName"),
)
if mibBuilder.loadTexts:
    hwBrasSbcInstanceEntry.setStatus("current")


class _HwBrasSbcInstanceName_Type(DisplayString):
    """Custom type hwBrasSbcInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBrasSbcInstanceName_Type.__name__ = "DisplayString"
_HwBrasSbcInstanceName_Object = MibTableColumn
hwBrasSbcInstanceName = _HwBrasSbcInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 8, 1, 1),
    _HwBrasSbcInstanceName_Type()
)
hwBrasSbcInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcInstanceName.setStatus("current")
_HwBrasSbcInstanceRowStatus_Type = RowStatus
_HwBrasSbcInstanceRowStatus_Object = MibTableColumn
hwBrasSbcInstanceRowStatus = _HwBrasSbcInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 2, 8, 1, 51),
    _HwBrasSbcInstanceRowStatus_Type()
)
hwBrasSbcInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcInstanceRowStatus.setStatus("current")
_HwBrasSbcMapGroup_ObjectIdentity = ObjectIdentity
hwBrasSbcMapGroup = _HwBrasSbcMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3)
)
_HwBrasSbcMapGroupLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcMapGroupLeaves = _HwBrasSbcMapGroupLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 1)
)
_HwBrasSbcMapGroupTables_ObjectIdentity = ObjectIdentity
hwBrasSbcMapGroupTables = _HwBrasSbcMapGroupTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2)
)
_HwBrasSbcMapGroupsTable_Object = MibTable
hwBrasSbcMapGroupsTable = _HwBrasSbcMapGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupsTable.setStatus("current")
_HwBrasSbcMapGroupsEntry_Object = MibTableRow
hwBrasSbcMapGroupsEntry = _HwBrasSbcMapGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1)
)
hwBrasSbcMapGroupsEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMapGroupsIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupsEntry.setStatus("current")


class _HwBrasSbcMapGroupsIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMapGroupsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMapGroupsIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMapGroupsIndex_Object = MibTableColumn
hwBrasSbcMapGroupsIndex = _HwBrasSbcMapGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1, 1),
    _HwBrasSbcMapGroupsIndex_Type()
)
hwBrasSbcMapGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupsIndex.setStatus("current")


class _HwBrasSbcMapGroupsType_Type(Integer32):
    """Custom type hwBrasSbcMapGroupsType based on Integer32"""
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
        *(("bgf", 4),
          ("intercomIP", 2),
          ("intercomPrefix", 3),
          ("proxy", 1))
    )


_HwBrasSbcMapGroupsType_Type.__name__ = "Integer32"
_HwBrasSbcMapGroupsType_Object = MibTableColumn
hwBrasSbcMapGroupsType = _HwBrasSbcMapGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1, 11),
    _HwBrasSbcMapGroupsType_Type()
)
hwBrasSbcMapGroupsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupsType.setStatus("current")


class _HwBrasSbcMapGroupsStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMapGroupsStatus based on HWBrasEnabledStatus"""


_HwBrasSbcMapGroupsStatus_Object = MibTableColumn
hwBrasSbcMapGroupsStatus = _HwBrasSbcMapGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1, 12),
    _HwBrasSbcMapGroupsStatus_Type()
)
hwBrasSbcMapGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupsStatus.setStatus("current")


class _HwBrasSbcMapGroupInstanceName_Type(DisplayString):
    """Custom type hwBrasSbcMapGroupInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBrasSbcMapGroupInstanceName_Type.__name__ = "DisplayString"
_HwBrasSbcMapGroupInstanceName_Object = MibTableColumn
hwBrasSbcMapGroupInstanceName = _HwBrasSbcMapGroupInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1, 13),
    _HwBrasSbcMapGroupInstanceName_Type()
)
hwBrasSbcMapGroupInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupInstanceName.setStatus("current")


class _HwBrasSbcMapGroupSessionLimit_Type(Unsigned32):
    """Custom type hwBrasSbcMapGroupSessionLimit based on Unsigned32"""
    defaultValue = 40000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40000),
    )


_HwBrasSbcMapGroupSessionLimit_Type.__name__ = "Unsigned32"
_HwBrasSbcMapGroupSessionLimit_Object = MibTableColumn
hwBrasSbcMapGroupSessionLimit = _HwBrasSbcMapGroupSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1, 14),
    _HwBrasSbcMapGroupSessionLimit_Type()
)
hwBrasSbcMapGroupSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupSessionLimit.setStatus("current")
_HwBrasSbcMapGroupsRowStatus_Type = RowStatus
_HwBrasSbcMapGroupsRowStatus_Object = MibTableColumn
hwBrasSbcMapGroupsRowStatus = _HwBrasSbcMapGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 1, 1, 51),
    _HwBrasSbcMapGroupsRowStatus_Type()
)
hwBrasSbcMapGroupsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMapGroupsRowStatus.setStatus("current")
_HwBrasSbcMGCliAddrTable_Object = MibTable
hwBrasSbcMGCliAddrTable = _HwBrasSbcMGCliAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGCliAddrTable.setStatus("current")
_HwBrasSbcMGCliAddrEntry_Object = MibTableRow
hwBrasSbcMGCliAddrEntry = _HwBrasSbcMGCliAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 2, 1)
)
hwBrasSbcMGCliAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGCliAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGCliAddrEntry.setStatus("current")


class _HwBrasSbcMGCliAddrIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGCliAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGCliAddrIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGCliAddrIndex_Object = MibTableColumn
hwBrasSbcMGCliAddrIndex = _HwBrasSbcMGCliAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 2, 1, 1),
    _HwBrasSbcMGCliAddrIndex_Type()
)
hwBrasSbcMGCliAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGCliAddrIndex.setStatus("current")


class _HwBrasSbcMGCliAddrVPN_Type(Unsigned32):
    """Custom type hwBrasSbcMGCliAddrVPN based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcMGCliAddrVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcMGCliAddrVPN_Object = MibTableColumn
hwBrasSbcMGCliAddrVPN = _HwBrasSbcMGCliAddrVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 2, 1, 11),
    _HwBrasSbcMGCliAddrVPN_Type()
)
hwBrasSbcMGCliAddrVPN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGCliAddrVPN.setStatus("current")
_HwBrasSbcMGCliAddrIP_Type = IpAddress
_HwBrasSbcMGCliAddrIP_Object = MibTableColumn
hwBrasSbcMGCliAddrIP = _HwBrasSbcMGCliAddrIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 2, 1, 12),
    _HwBrasSbcMGCliAddrIP_Type()
)
hwBrasSbcMGCliAddrIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGCliAddrIP.setStatus("current")
_HwBrasSbcMGCliAddrRowStatus_Type = RowStatus
_HwBrasSbcMGCliAddrRowStatus_Object = MibTableColumn
hwBrasSbcMGCliAddrRowStatus = _HwBrasSbcMGCliAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 2, 1, 51),
    _HwBrasSbcMGCliAddrRowStatus_Type()
)
hwBrasSbcMGCliAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGCliAddrRowStatus.setStatus("current")
_HwBrasSbcMGServAddrTable_Object = MibTable
hwBrasSbcMGServAddrTable = _HwBrasSbcMGServAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrTable.setStatus("current")
_HwBrasSbcMGServAddrEntry_Object = MibTableRow
hwBrasSbcMGServAddrEntry = _HwBrasSbcMGServAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1)
)
hwBrasSbcMGServAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrEntry.setStatus("current")


class _HwBrasSbcMGServAddrIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGServAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGServAddrIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGServAddrIndex_Object = MibTableColumn
hwBrasSbcMGServAddrIndex = _HwBrasSbcMGServAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 1),
    _HwBrasSbcMGServAddrIndex_Type()
)
hwBrasSbcMGServAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrIndex.setStatus("current")


class _HwBrasSbcMGServAddrVPN_Type(Unsigned32):
    """Custom type hwBrasSbcMGServAddrVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcMGServAddrVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcMGServAddrVPN_Object = MibTableColumn
hwBrasSbcMGServAddrVPN = _HwBrasSbcMGServAddrVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 11),
    _HwBrasSbcMGServAddrVPN_Type()
)
hwBrasSbcMGServAddrVPN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrVPN.setStatus("current")
_HwBrasSbcMGServAddrIP1_Type = IpAddress
_HwBrasSbcMGServAddrIP1_Object = MibTableColumn
hwBrasSbcMGServAddrIP1 = _HwBrasSbcMGServAddrIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 12),
    _HwBrasSbcMGServAddrIP1_Type()
)
hwBrasSbcMGServAddrIP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrIP1.setStatus("current")
_HwBrasSbcMGServAddrIP2_Type = IpAddress
_HwBrasSbcMGServAddrIP2_Object = MibTableColumn
hwBrasSbcMGServAddrIP2 = _HwBrasSbcMGServAddrIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 13),
    _HwBrasSbcMGServAddrIP2_Type()
)
hwBrasSbcMGServAddrIP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrIP2.setStatus("current")
_HwBrasSbcMGServAddrIP3_Type = IpAddress
_HwBrasSbcMGServAddrIP3_Object = MibTableColumn
hwBrasSbcMGServAddrIP3 = _HwBrasSbcMGServAddrIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 14),
    _HwBrasSbcMGServAddrIP3_Type()
)
hwBrasSbcMGServAddrIP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrIP3.setStatus("current")
_HwBrasSbcMGServAddrIP4_Type = IpAddress
_HwBrasSbcMGServAddrIP4_Object = MibTableColumn
hwBrasSbcMGServAddrIP4 = _HwBrasSbcMGServAddrIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 15),
    _HwBrasSbcMGServAddrIP4_Type()
)
hwBrasSbcMGServAddrIP4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrIP4.setStatus("current")
_HwBrasSbcMGServAddrRowStatus_Type = RowStatus
_HwBrasSbcMGServAddrRowStatus_Object = MibTableColumn
hwBrasSbcMGServAddrRowStatus = _HwBrasSbcMGServAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 3, 1, 51),
    _HwBrasSbcMGServAddrRowStatus_Type()
)
hwBrasSbcMGServAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGServAddrRowStatus.setStatus("current")
_HwBrasSbcMGSofxAddrTable_Object = MibTable
hwBrasSbcMGSofxAddrTable = _HwBrasSbcMGSofxAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrTable.setStatus("current")
_HwBrasSbcMGSofxAddrEntry_Object = MibTableRow
hwBrasSbcMGSofxAddrEntry = _HwBrasSbcMGSofxAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1)
)
hwBrasSbcMGSofxAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrEntry.setStatus("current")


class _HwBrasSbcMGSofxAddrIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGSofxAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGSofxAddrIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGSofxAddrIndex_Object = MibTableColumn
hwBrasSbcMGSofxAddrIndex = _HwBrasSbcMGSofxAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 1),
    _HwBrasSbcMGSofxAddrIndex_Type()
)
hwBrasSbcMGSofxAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrIndex.setStatus("current")


class _HwBrasSbcMGSofxAddrVPN_Type(Unsigned32):
    """Custom type hwBrasSbcMGSofxAddrVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcMGSofxAddrVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcMGSofxAddrVPN_Object = MibTableColumn
hwBrasSbcMGSofxAddrVPN = _HwBrasSbcMGSofxAddrVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 11),
    _HwBrasSbcMGSofxAddrVPN_Type()
)
hwBrasSbcMGSofxAddrVPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrVPN.setStatus("current")
_HwBrasSbcMGSofxAddrIP1_Type = IpAddress
_HwBrasSbcMGSofxAddrIP1_Object = MibTableColumn
hwBrasSbcMGSofxAddrIP1 = _HwBrasSbcMGSofxAddrIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 12),
    _HwBrasSbcMGSofxAddrIP1_Type()
)
hwBrasSbcMGSofxAddrIP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrIP1.setStatus("current")
_HwBrasSbcMGSofxAddrIP2_Type = IpAddress
_HwBrasSbcMGSofxAddrIP2_Object = MibTableColumn
hwBrasSbcMGSofxAddrIP2 = _HwBrasSbcMGSofxAddrIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 13),
    _HwBrasSbcMGSofxAddrIP2_Type()
)
hwBrasSbcMGSofxAddrIP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrIP2.setStatus("current")
_HwBrasSbcMGSofxAddrIP3_Type = IpAddress
_HwBrasSbcMGSofxAddrIP3_Object = MibTableColumn
hwBrasSbcMGSofxAddrIP3 = _HwBrasSbcMGSofxAddrIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 14),
    _HwBrasSbcMGSofxAddrIP3_Type()
)
hwBrasSbcMGSofxAddrIP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrIP3.setStatus("current")
_HwBrasSbcMGSofxAddrIP4_Type = IpAddress
_HwBrasSbcMGSofxAddrIP4_Object = MibTableColumn
hwBrasSbcMGSofxAddrIP4 = _HwBrasSbcMGSofxAddrIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 15),
    _HwBrasSbcMGSofxAddrIP4_Type()
)
hwBrasSbcMGSofxAddrIP4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrIP4.setStatus("current")
_HwBrasSbcMGSofxAddrRowStatus_Type = RowStatus
_HwBrasSbcMGSofxAddrRowStatus_Object = MibTableColumn
hwBrasSbcMGSofxAddrRowStatus = _HwBrasSbcMGSofxAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 4, 1, 51),
    _HwBrasSbcMGSofxAddrRowStatus_Type()
)
hwBrasSbcMGSofxAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGSofxAddrRowStatus.setStatus("current")
_HwBrasSbcMGIadmsAddrTable_Object = MibTable
hwBrasSbcMGIadmsAddrTable = _HwBrasSbcMGIadmsAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrTable.setStatus("current")
_HwBrasSbcMGIadmsAddrEntry_Object = MibTableRow
hwBrasSbcMGIadmsAddrEntry = _HwBrasSbcMGIadmsAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1)
)
hwBrasSbcMGIadmsAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrEntry.setStatus("current")


class _HwBrasSbcMGIadmsAddrIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGIadmsAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGIadmsAddrIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGIadmsAddrIndex_Object = MibTableColumn
hwBrasSbcMGIadmsAddrIndex = _HwBrasSbcMGIadmsAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 1),
    _HwBrasSbcMGIadmsAddrIndex_Type()
)
hwBrasSbcMGIadmsAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrIndex.setStatus("current")


class _HwBrasSbcMGIadmsAddrVPN_Type(Unsigned32):
    """Custom type hwBrasSbcMGIadmsAddrVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcMGIadmsAddrVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcMGIadmsAddrVPN_Object = MibTableColumn
hwBrasSbcMGIadmsAddrVPN = _HwBrasSbcMGIadmsAddrVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 11),
    _HwBrasSbcMGIadmsAddrVPN_Type()
)
hwBrasSbcMGIadmsAddrVPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrVPN.setStatus("current")
_HwBrasSbcMGIadmsAddrIP1_Type = IpAddress
_HwBrasSbcMGIadmsAddrIP1_Object = MibTableColumn
hwBrasSbcMGIadmsAddrIP1 = _HwBrasSbcMGIadmsAddrIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 12),
    _HwBrasSbcMGIadmsAddrIP1_Type()
)
hwBrasSbcMGIadmsAddrIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrIP1.setStatus("current")
_HwBrasSbcMGIadmsAddrIP2_Type = IpAddress
_HwBrasSbcMGIadmsAddrIP2_Object = MibTableColumn
hwBrasSbcMGIadmsAddrIP2 = _HwBrasSbcMGIadmsAddrIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 13),
    _HwBrasSbcMGIadmsAddrIP2_Type()
)
hwBrasSbcMGIadmsAddrIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrIP2.setStatus("current")
_HwBrasSbcMGIadmsAddrIP3_Type = IpAddress
_HwBrasSbcMGIadmsAddrIP3_Object = MibTableColumn
hwBrasSbcMGIadmsAddrIP3 = _HwBrasSbcMGIadmsAddrIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 14),
    _HwBrasSbcMGIadmsAddrIP3_Type()
)
hwBrasSbcMGIadmsAddrIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrIP3.setStatus("current")
_HwBrasSbcMGIadmsAddrIP4_Type = IpAddress
_HwBrasSbcMGIadmsAddrIP4_Object = MibTableColumn
hwBrasSbcMGIadmsAddrIP4 = _HwBrasSbcMGIadmsAddrIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 15),
    _HwBrasSbcMGIadmsAddrIP4_Type()
)
hwBrasSbcMGIadmsAddrIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrIP4.setStatus("current")
_HwBrasSbcMGIadmsAddrRowStatus_Type = RowStatus
_HwBrasSbcMGIadmsAddrRowStatus_Object = MibTableColumn
hwBrasSbcMGIadmsAddrRowStatus = _HwBrasSbcMGIadmsAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 5, 1, 51),
    _HwBrasSbcMGIadmsAddrRowStatus_Type()
)
hwBrasSbcMGIadmsAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGIadmsAddrRowStatus.setStatus("current")
_HwBrasSbcMGProtocolTable_Object = MibTable
hwBrasSbcMGProtocolTable = _HwBrasSbcMGProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolTable.setStatus("current")
_HwBrasSbcMGProtocolEntry_Object = MibTableRow
hwBrasSbcMGProtocolEntry = _HwBrasSbcMGProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1)
)
hwBrasSbcMGProtocolEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolEntry.setStatus("current")


class _HwBrasSbcMGProtocolIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGProtocolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGProtocolIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGProtocolIndex_Object = MibTableColumn
hwBrasSbcMGProtocolIndex = _HwBrasSbcMGProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 1),
    _HwBrasSbcMGProtocolIndex_Type()
)
hwBrasSbcMGProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolIndex.setStatus("current")
_HwBrasSbcMGProtocolSip_Type = HWBrasEnabledStatus
_HwBrasSbcMGProtocolSip_Object = MibTableColumn
hwBrasSbcMGProtocolSip = _HwBrasSbcMGProtocolSip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 11),
    _HwBrasSbcMGProtocolSip_Type()
)
hwBrasSbcMGProtocolSip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolSip.setStatus("current")
_HwBrasSbcMGProtocolMgcp_Type = HWBrasEnabledStatus
_HwBrasSbcMGProtocolMgcp_Object = MibTableColumn
hwBrasSbcMGProtocolMgcp = _HwBrasSbcMGProtocolMgcp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 12),
    _HwBrasSbcMGProtocolMgcp_Type()
)
hwBrasSbcMGProtocolMgcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolMgcp.setStatus("current")
_HwBrasSbcMGProtocolH323_Type = HWBrasEnabledStatus
_HwBrasSbcMGProtocolH323_Object = MibTableColumn
hwBrasSbcMGProtocolH323 = _HwBrasSbcMGProtocolH323_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 13),
    _HwBrasSbcMGProtocolH323_Type()
)
hwBrasSbcMGProtocolH323.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolH323.setStatus("current")
_HwBrasSbcMGProtocolIadms_Type = HWBrasEnabledStatus
_HwBrasSbcMGProtocolIadms_Object = MibTableColumn
hwBrasSbcMGProtocolIadms = _HwBrasSbcMGProtocolIadms_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 14),
    _HwBrasSbcMGProtocolIadms_Type()
)
hwBrasSbcMGProtocolIadms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolIadms.setStatus("current")
_HwBrasSbcMGProtocolUpath_Type = HWBrasEnabledStatus
_HwBrasSbcMGProtocolUpath_Object = MibTableColumn
hwBrasSbcMGProtocolUpath = _HwBrasSbcMGProtocolUpath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 15),
    _HwBrasSbcMGProtocolUpath_Type()
)
hwBrasSbcMGProtocolUpath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolUpath.setStatus("current")
_HwBrasSbcMGProtocolH248_Type = HWBrasEnabledStatus
_HwBrasSbcMGProtocolH248_Object = MibTableColumn
hwBrasSbcMGProtocolH248 = _HwBrasSbcMGProtocolH248_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 16),
    _HwBrasSbcMGProtocolH248_Type()
)
hwBrasSbcMGProtocolH248.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolH248.setStatus("current")
_HwBrasSbcMGProtocolRowStatus_Type = RowStatus
_HwBrasSbcMGProtocolRowStatus_Object = MibTableColumn
hwBrasSbcMGProtocolRowStatus = _HwBrasSbcMGProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 6, 1, 51),
    _HwBrasSbcMGProtocolRowStatus_Type()
)
hwBrasSbcMGProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGProtocolRowStatus.setStatus("current")
_HwBrasSbcMGPortTable_Object = MibTable
hwBrasSbcMGPortTable = _HwBrasSbcMGPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGPortTable.setStatus("current")
_HwBrasSbcMGPortEntry_Object = MibTableRow
hwBrasSbcMGPortEntry = _HwBrasSbcMGPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 7, 1)
)
hwBrasSbcMGPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGPortIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGPortEntry.setStatus("current")


class _HwBrasSbcMGPortIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGPortIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGPortIndex_Object = MibTableColumn
hwBrasSbcMGPortIndex = _HwBrasSbcMGPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 7, 1, 1),
    _HwBrasSbcMGPortIndex_Type()
)
hwBrasSbcMGPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGPortIndex.setStatus("current")


class _HwBrasSbcMGPortNumber_Type(Unsigned32):
    """Custom type hwBrasSbcMGPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcMGPortNumber_Type.__name__ = "Unsigned32"
_HwBrasSbcMGPortNumber_Object = MibTableColumn
hwBrasSbcMGPortNumber = _HwBrasSbcMGPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 7, 1, 11),
    _HwBrasSbcMGPortNumber_Type()
)
hwBrasSbcMGPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGPortNumber.setStatus("current")
_HwBrasSbcMGPortRowStatus_Type = RowStatus
_HwBrasSbcMGPortRowStatus_Object = MibTableColumn
hwBrasSbcMGPortRowStatus = _HwBrasSbcMGPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 7, 1, 51),
    _HwBrasSbcMGPortRowStatus_Type()
)
hwBrasSbcMGPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGPortRowStatus.setStatus("current")
_HwBrasSbcMGPrefixTable_Object = MibTable
hwBrasSbcMGPrefixTable = _HwBrasSbcMGPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGPrefixTable.setStatus("current")
_HwBrasSbcMGPrefixEntry_Object = MibTableRow
hwBrasSbcMGPrefixEntry = _HwBrasSbcMGPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 8, 1)
)
hwBrasSbcMGPrefixEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGPrefixIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGPrefixEntry.setStatus("current")


class _HwBrasSbcMGPrefixIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGPrefixIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGPrefixIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGPrefixIndex_Object = MibTableColumn
hwBrasSbcMGPrefixIndex = _HwBrasSbcMGPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 8, 1, 1),
    _HwBrasSbcMGPrefixIndex_Type()
)
hwBrasSbcMGPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGPrefixIndex.setStatus("current")


class _HwBrasSbcMGPrefixID_Type(DisplayString):
    """Custom type hwBrasSbcMGPrefixID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwBrasSbcMGPrefixID_Type.__name__ = "DisplayString"
_HwBrasSbcMGPrefixID_Object = MibTableColumn
hwBrasSbcMGPrefixID = _HwBrasSbcMGPrefixID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 8, 1, 11),
    _HwBrasSbcMGPrefixID_Type()
)
hwBrasSbcMGPrefixID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGPrefixID.setStatus("current")
_HwBrasSbcMGPrefixRowStatus_Type = RowStatus
_HwBrasSbcMGPrefixRowStatus_Object = MibTableColumn
hwBrasSbcMGPrefixRowStatus = _HwBrasSbcMGPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 8, 1, 51),
    _HwBrasSbcMGPrefixRowStatus_Type()
)
hwBrasSbcMGPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGPrefixRowStatus.setStatus("current")
_HwBrasSbcMGMdCliAddrTable_Object = MibTable
hwBrasSbcMGMdCliAddrTable = _HwBrasSbcMGMdCliAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrTable.setStatus("current")
_HwBrasSbcMGMdCliAddrEntry_Object = MibTableRow
hwBrasSbcMGMdCliAddrEntry = _HwBrasSbcMGMdCliAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1)
)
hwBrasSbcMGMdCliAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrEntry.setStatus("current")


class _HwBrasSbcMGMdCliAddrIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdCliAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGMdCliAddrIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdCliAddrIndex_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIndex = _HwBrasSbcMGMdCliAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 1),
    _HwBrasSbcMGMdCliAddrIndex_Type()
)
hwBrasSbcMGMdCliAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIndex.setStatus("current")


class _HwBrasSbcMGMdCliAddrVPN_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdCliAddrVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcMGMdCliAddrVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdCliAddrVPN_Object = MibTableColumn
hwBrasSbcMGMdCliAddrVPN = _HwBrasSbcMGMdCliAddrVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 11),
    _HwBrasSbcMGMdCliAddrVPN_Type()
)
hwBrasSbcMGMdCliAddrVPN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrVPN.setStatus("current")
_HwBrasSbcMGMdCliAddrIP1_Type = IpAddress
_HwBrasSbcMGMdCliAddrIP1_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIP1 = _HwBrasSbcMGMdCliAddrIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 12),
    _HwBrasSbcMGMdCliAddrIP1_Type()
)
hwBrasSbcMGMdCliAddrIP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIP1.setStatus("current")
_HwBrasSbcMGMdCliAddrIP2_Type = IpAddress
_HwBrasSbcMGMdCliAddrIP2_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIP2 = _HwBrasSbcMGMdCliAddrIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 13),
    _HwBrasSbcMGMdCliAddrIP2_Type()
)
hwBrasSbcMGMdCliAddrIP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIP2.setStatus("current")
_HwBrasSbcMGMdCliAddrIP3_Type = IpAddress
_HwBrasSbcMGMdCliAddrIP3_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIP3 = _HwBrasSbcMGMdCliAddrIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 14),
    _HwBrasSbcMGMdCliAddrIP3_Type()
)
hwBrasSbcMGMdCliAddrIP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIP3.setStatus("current")
_HwBrasSbcMGMdCliAddrIP4_Type = IpAddress
_HwBrasSbcMGMdCliAddrIP4_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIP4 = _HwBrasSbcMGMdCliAddrIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 15),
    _HwBrasSbcMGMdCliAddrIP4_Type()
)
hwBrasSbcMGMdCliAddrIP4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIP4.setStatus("current")


class _HwBrasSbcMGMdCliAddrVPNName_Type(OctetString):
    """Custom type hwBrasSbcMGMdCliAddrVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwBrasSbcMGMdCliAddrVPNName_Type.__name__ = "OctetString"
_HwBrasSbcMGMdCliAddrVPNName_Object = MibTableColumn
hwBrasSbcMGMdCliAddrVPNName = _HwBrasSbcMGMdCliAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 16),
    _HwBrasSbcMGMdCliAddrVPNName_Type()
)
hwBrasSbcMGMdCliAddrVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrVPNName.setStatus("current")


class _HwBrasSbcMGMdCliAddrIf1_Type(OctetString):
    """Custom type hwBrasSbcMGMdCliAddrIf1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdCliAddrIf1_Type.__name__ = "OctetString"
_HwBrasSbcMGMdCliAddrIf1_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIf1 = _HwBrasSbcMGMdCliAddrIf1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 17),
    _HwBrasSbcMGMdCliAddrIf1_Type()
)
hwBrasSbcMGMdCliAddrIf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIf1.setStatus("current")


class _HwBrasSbcMGMdCliAddrSlotID1_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdCliAddrSlotID1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdCliAddrSlotID1_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdCliAddrSlotID1_Object = MibTableColumn
hwBrasSbcMGMdCliAddrSlotID1 = _HwBrasSbcMGMdCliAddrSlotID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 18),
    _HwBrasSbcMGMdCliAddrSlotID1_Type()
)
hwBrasSbcMGMdCliAddrSlotID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrSlotID1.setStatus("current")


class _HwBrasSbcMGMdCliAddrIf2_Type(OctetString):
    """Custom type hwBrasSbcMGMdCliAddrIf2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdCliAddrIf2_Type.__name__ = "OctetString"
_HwBrasSbcMGMdCliAddrIf2_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIf2 = _HwBrasSbcMGMdCliAddrIf2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 19),
    _HwBrasSbcMGMdCliAddrIf2_Type()
)
hwBrasSbcMGMdCliAddrIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIf2.setStatus("current")


class _HwBrasSbcMGMdCliAddrSlotID2_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdCliAddrSlotID2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdCliAddrSlotID2_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdCliAddrSlotID2_Object = MibTableColumn
hwBrasSbcMGMdCliAddrSlotID2 = _HwBrasSbcMGMdCliAddrSlotID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 20),
    _HwBrasSbcMGMdCliAddrSlotID2_Type()
)
hwBrasSbcMGMdCliAddrSlotID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrSlotID2.setStatus("current")


class _HwBrasSbcMGMdCliAddrIf3_Type(OctetString):
    """Custom type hwBrasSbcMGMdCliAddrIf3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdCliAddrIf3_Type.__name__ = "OctetString"
_HwBrasSbcMGMdCliAddrIf3_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIf3 = _HwBrasSbcMGMdCliAddrIf3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 21),
    _HwBrasSbcMGMdCliAddrIf3_Type()
)
hwBrasSbcMGMdCliAddrIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIf3.setStatus("current")


class _HwBrasSbcMGMdCliAddrSlotID3_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdCliAddrSlotID3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdCliAddrSlotID3_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdCliAddrSlotID3_Object = MibTableColumn
hwBrasSbcMGMdCliAddrSlotID3 = _HwBrasSbcMGMdCliAddrSlotID3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 22),
    _HwBrasSbcMGMdCliAddrSlotID3_Type()
)
hwBrasSbcMGMdCliAddrSlotID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrSlotID3.setStatus("current")


class _HwBrasSbcMGMdCliAddrIf4_Type(OctetString):
    """Custom type hwBrasSbcMGMdCliAddrIf4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdCliAddrIf4_Type.__name__ = "OctetString"
_HwBrasSbcMGMdCliAddrIf4_Object = MibTableColumn
hwBrasSbcMGMdCliAddrIf4 = _HwBrasSbcMGMdCliAddrIf4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 23),
    _HwBrasSbcMGMdCliAddrIf4_Type()
)
hwBrasSbcMGMdCliAddrIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrIf4.setStatus("current")


class _HwBrasSbcMGMdCliAddrSlotID4_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdCliAddrSlotID4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdCliAddrSlotID4_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdCliAddrSlotID4_Object = MibTableColumn
hwBrasSbcMGMdCliAddrSlotID4 = _HwBrasSbcMGMdCliAddrSlotID4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 24),
    _HwBrasSbcMGMdCliAddrSlotID4_Type()
)
hwBrasSbcMGMdCliAddrSlotID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrSlotID4.setStatus("current")
_HwBrasSbcMGMdCliAddrRowStatus_Type = RowStatus
_HwBrasSbcMGMdCliAddrRowStatus_Object = MibTableColumn
hwBrasSbcMGMdCliAddrRowStatus = _HwBrasSbcMGMdCliAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 9, 1, 51),
    _HwBrasSbcMGMdCliAddrRowStatus_Type()
)
hwBrasSbcMGMdCliAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdCliAddrRowStatus.setStatus("current")
_HwBrasSbcMGMdServAddrTable_Object = MibTable
hwBrasSbcMGMdServAddrTable = _HwBrasSbcMGMdServAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrTable.setStatus("current")
_HwBrasSbcMGMdServAddrEntry_Object = MibTableRow
hwBrasSbcMGMdServAddrEntry = _HwBrasSbcMGMdServAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1)
)
hwBrasSbcMGMdServAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrEntry.setStatus("current")


class _HwBrasSbcMGMdServAddrIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdServAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGMdServAddrIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdServAddrIndex_Object = MibTableColumn
hwBrasSbcMGMdServAddrIndex = _HwBrasSbcMGMdServAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 1),
    _HwBrasSbcMGMdServAddrIndex_Type()
)
hwBrasSbcMGMdServAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIndex.setStatus("current")


class _HwBrasSbcMGMdServAddrVPN_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdServAddrVPN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcMGMdServAddrVPN_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdServAddrVPN_Object = MibTableColumn
hwBrasSbcMGMdServAddrVPN = _HwBrasSbcMGMdServAddrVPN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 11),
    _HwBrasSbcMGMdServAddrVPN_Type()
)
hwBrasSbcMGMdServAddrVPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrVPN.setStatus("current")
_HwBrasSbcMGMdServAddrIP1_Type = IpAddress
_HwBrasSbcMGMdServAddrIP1_Object = MibTableColumn
hwBrasSbcMGMdServAddrIP1 = _HwBrasSbcMGMdServAddrIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 12),
    _HwBrasSbcMGMdServAddrIP1_Type()
)
hwBrasSbcMGMdServAddrIP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIP1.setStatus("current")
_HwBrasSbcMGMdServAddrIP2_Type = IpAddress
_HwBrasSbcMGMdServAddrIP2_Object = MibTableColumn
hwBrasSbcMGMdServAddrIP2 = _HwBrasSbcMGMdServAddrIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 13),
    _HwBrasSbcMGMdServAddrIP2_Type()
)
hwBrasSbcMGMdServAddrIP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIP2.setStatus("current")
_HwBrasSbcMGMdServAddrIP3_Type = IpAddress
_HwBrasSbcMGMdServAddrIP3_Object = MibTableColumn
hwBrasSbcMGMdServAddrIP3 = _HwBrasSbcMGMdServAddrIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 14),
    _HwBrasSbcMGMdServAddrIP3_Type()
)
hwBrasSbcMGMdServAddrIP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIP3.setStatus("current")
_HwBrasSbcMGMdServAddrIP4_Type = IpAddress
_HwBrasSbcMGMdServAddrIP4_Object = MibTableColumn
hwBrasSbcMGMdServAddrIP4 = _HwBrasSbcMGMdServAddrIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 15),
    _HwBrasSbcMGMdServAddrIP4_Type()
)
hwBrasSbcMGMdServAddrIP4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIP4.setStatus("current")


class _HwBrasSbcMGMdServAddrVPNName_Type(OctetString):
    """Custom type hwBrasSbcMGMdServAddrVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwBrasSbcMGMdServAddrVPNName_Type.__name__ = "OctetString"
_HwBrasSbcMGMdServAddrVPNName_Object = MibTableColumn
hwBrasSbcMGMdServAddrVPNName = _HwBrasSbcMGMdServAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 16),
    _HwBrasSbcMGMdServAddrVPNName_Type()
)
hwBrasSbcMGMdServAddrVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrVPNName.setStatus("current")


class _HwBrasSbcMGMdServAddrIf1_Type(OctetString):
    """Custom type hwBrasSbcMGMdServAddrIf1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdServAddrIf1_Type.__name__ = "OctetString"
_HwBrasSbcMGMdServAddrIf1_Object = MibTableColumn
hwBrasSbcMGMdServAddrIf1 = _HwBrasSbcMGMdServAddrIf1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 17),
    _HwBrasSbcMGMdServAddrIf1_Type()
)
hwBrasSbcMGMdServAddrIf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIf1.setStatus("current")


class _HwBrasSbcMGMdServAddrSlotID1_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdServAddrSlotID1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdServAddrSlotID1_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdServAddrSlotID1_Object = MibTableColumn
hwBrasSbcMGMdServAddrSlotID1 = _HwBrasSbcMGMdServAddrSlotID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 18),
    _HwBrasSbcMGMdServAddrSlotID1_Type()
)
hwBrasSbcMGMdServAddrSlotID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrSlotID1.setStatus("current")


class _HwBrasSbcMGMdServAddrIf2_Type(OctetString):
    """Custom type hwBrasSbcMGMdServAddrIf2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdServAddrIf2_Type.__name__ = "OctetString"
_HwBrasSbcMGMdServAddrIf2_Object = MibTableColumn
hwBrasSbcMGMdServAddrIf2 = _HwBrasSbcMGMdServAddrIf2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 19),
    _HwBrasSbcMGMdServAddrIf2_Type()
)
hwBrasSbcMGMdServAddrIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIf2.setStatus("current")


class _HwBrasSbcMGMdServAddrSlotID2_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdServAddrSlotID2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdServAddrSlotID2_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdServAddrSlotID2_Object = MibTableColumn
hwBrasSbcMGMdServAddrSlotID2 = _HwBrasSbcMGMdServAddrSlotID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 20),
    _HwBrasSbcMGMdServAddrSlotID2_Type()
)
hwBrasSbcMGMdServAddrSlotID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrSlotID2.setStatus("current")


class _HwBrasSbcMGMdServAddrIf3_Type(OctetString):
    """Custom type hwBrasSbcMGMdServAddrIf3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdServAddrIf3_Type.__name__ = "OctetString"
_HwBrasSbcMGMdServAddrIf3_Object = MibTableColumn
hwBrasSbcMGMdServAddrIf3 = _HwBrasSbcMGMdServAddrIf3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 21),
    _HwBrasSbcMGMdServAddrIf3_Type()
)
hwBrasSbcMGMdServAddrIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIf3.setStatus("current")


class _HwBrasSbcMGMdServAddrSlotID3_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdServAddrSlotID3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdServAddrSlotID3_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdServAddrSlotID3_Object = MibTableColumn
hwBrasSbcMGMdServAddrSlotID3 = _HwBrasSbcMGMdServAddrSlotID3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 22),
    _HwBrasSbcMGMdServAddrSlotID3_Type()
)
hwBrasSbcMGMdServAddrSlotID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrSlotID3.setStatus("current")


class _HwBrasSbcMGMdServAddrIf4_Type(OctetString):
    """Custom type hwBrasSbcMGMdServAddrIf4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwBrasSbcMGMdServAddrIf4_Type.__name__ = "OctetString"
_HwBrasSbcMGMdServAddrIf4_Object = MibTableColumn
hwBrasSbcMGMdServAddrIf4 = _HwBrasSbcMGMdServAddrIf4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 23),
    _HwBrasSbcMGMdServAddrIf4_Type()
)
hwBrasSbcMGMdServAddrIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrIf4.setStatus("current")


class _HwBrasSbcMGMdServAddrSlotID4_Type(Unsigned32):
    """Custom type hwBrasSbcMGMdServAddrSlotID4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwBrasSbcMGMdServAddrSlotID4_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMdServAddrSlotID4_Object = MibTableColumn
hwBrasSbcMGMdServAddrSlotID4 = _HwBrasSbcMGMdServAddrSlotID4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 24),
    _HwBrasSbcMGMdServAddrSlotID4_Type()
)
hwBrasSbcMGMdServAddrSlotID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrSlotID4.setStatus("current")
_HwBrasSbcMGMdServAddrRowStatus_Type = RowStatus
_HwBrasSbcMGMdServAddrRowStatus_Object = MibTableColumn
hwBrasSbcMGMdServAddrRowStatus = _HwBrasSbcMGMdServAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 10, 1, 51),
    _HwBrasSbcMGMdServAddrRowStatus_Type()
)
hwBrasSbcMGMdServAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMdServAddrRowStatus.setStatus("current")
_HwBrasSbcMGMatchTable_Object = MibTable
hwBrasSbcMGMatchTable = _HwBrasSbcMGMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 11)
)
if mibBuilder.loadTexts:
    hwBrasSbcMGMatchTable.setStatus("current")
_HwBrasSbcMGMatchEntry_Object = MibTableRow
hwBrasSbcMGMatchEntry = _HwBrasSbcMGMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 11, 1)
)
hwBrasSbcMGMatchEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMatchIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMGMatchEntry.setStatus("current")


class _HwBrasSbcMGMatchIndex_Type(Unsigned32):
    """Custom type hwBrasSbcMGMatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_HwBrasSbcMGMatchIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMatchIndex_Object = MibTableColumn
hwBrasSbcMGMatchIndex = _HwBrasSbcMGMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 11, 1, 1),
    _HwBrasSbcMGMatchIndex_Type()
)
hwBrasSbcMGMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMGMatchIndex.setStatus("current")


class _HwBrasSbcMGMatchAcl_Type(Unsigned32):
    """Custom type hwBrasSbcMGMatchAcl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_HwBrasSbcMGMatchAcl_Type.__name__ = "Unsigned32"
_HwBrasSbcMGMatchAcl_Object = MibTableColumn
hwBrasSbcMGMatchAcl = _HwBrasSbcMGMatchAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 11, 1, 11),
    _HwBrasSbcMGMatchAcl_Type()
)
hwBrasSbcMGMatchAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMatchAcl.setStatus("current")
_HwBrasSbcMGMatchRowStatus_Type = RowStatus
_HwBrasSbcMGMatchRowStatus_Object = MibTableColumn
hwBrasSbcMGMatchRowStatus = _HwBrasSbcMGMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 3, 2, 11, 1, 51),
    _HwBrasSbcMGMatchRowStatus_Type()
)
hwBrasSbcMGMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMGMatchRowStatus.setStatus("current")
_HwBrasSbcAdmModuleTable_ObjectIdentity = ObjectIdentity
hwBrasSbcAdmModuleTable = _HwBrasSbcAdmModuleTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4)
)
_HwBrasSbcBackupGroupsTable_ObjectIdentity = ObjectIdentity
hwBrasSbcBackupGroupsTable = _HwBrasSbcBackupGroupsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1)
)
_HwBrasSbcBackupGroupTable_Object = MibTable
hwBrasSbcBackupGroupTable = _HwBrasSbcBackupGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupTable.setStatus("current")
_HwBrasSbcBackupGroupEntry_Object = MibTableRow
hwBrasSbcBackupGroupEntry = _HwBrasSbcBackupGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 1, 1)
)
hwBrasSbcBackupGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBackupGroupID"),
)
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupEntry.setStatus("current")


class _HwBrasSbcBackupGroupID_Type(Integer32):
    """Custom type hwBrasSbcBackupGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_HwBrasSbcBackupGroupID_Type.__name__ = "Integer32"
_HwBrasSbcBackupGroupID_Object = MibTableColumn
hwBrasSbcBackupGroupID = _HwBrasSbcBackupGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 1, 1, 1),
    _HwBrasSbcBackupGroupID_Type()
)
hwBrasSbcBackupGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupID.setStatus("current")


class _HwBrasSbcBackupGroupType_Type(Integer32):
    """Custom type hwBrasSbcBackupGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("media", 2),
          ("signal", 1))
    )


_HwBrasSbcBackupGroupType_Type.__name__ = "Integer32"
_HwBrasSbcBackupGroupType_Object = MibTableColumn
hwBrasSbcBackupGroupType = _HwBrasSbcBackupGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 1, 1, 2),
    _HwBrasSbcBackupGroupType_Type()
)
hwBrasSbcBackupGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupType.setStatus("current")


class _HwBrasSbcBackupGroupInstanceName_Type(DisplayString):
    """Custom type hwBrasSbcBackupGroupInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBrasSbcBackupGroupInstanceName_Type.__name__ = "DisplayString"
_HwBrasSbcBackupGroupInstanceName_Object = MibTableColumn
hwBrasSbcBackupGroupInstanceName = _HwBrasSbcBackupGroupInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 1, 1, 3),
    _HwBrasSbcBackupGroupInstanceName_Type()
)
hwBrasSbcBackupGroupInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupInstanceName.setStatus("current")
_HwBrasSbcBackupGroupRowStatus_Type = RowStatus
_HwBrasSbcBackupGroupRowStatus_Object = MibTableColumn
hwBrasSbcBackupGroupRowStatus = _HwBrasSbcBackupGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 1, 1, 51),
    _HwBrasSbcBackupGroupRowStatus_Type()
)
hwBrasSbcBackupGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupRowStatus.setStatus("current")
_HwBrasSbcSlotInforTable_Object = MibTable
hwBrasSbcSlotInforTable = _HwBrasSbcSlotInforTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcSlotInforTable.setStatus("current")
_HwBrasSbcSlotInforEntry_Object = MibTableRow
hwBrasSbcSlotInforEntry = _HwBrasSbcSlotInforEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2, 1)
)
hwBrasSbcSlotInforEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBackupGroupIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSlotIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSlotInforEntry.setStatus("current")


class _HwBrasSbcBackupGroupIndex_Type(Integer32):
    """Custom type hwBrasSbcBackupGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_HwBrasSbcBackupGroupIndex_Type.__name__ = "Integer32"
_HwBrasSbcBackupGroupIndex_Object = MibTableColumn
hwBrasSbcBackupGroupIndex = _HwBrasSbcBackupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2, 1, 1),
    _HwBrasSbcBackupGroupIndex_Type()
)
hwBrasSbcBackupGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcBackupGroupIndex.setStatus("current")


class _HwBrasSbcSlotIndex_Type(Integer32):
    """Custom type hwBrasSbcSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwBrasSbcSlotIndex_Type.__name__ = "Integer32"
_HwBrasSbcSlotIndex_Object = MibTableColumn
hwBrasSbcSlotIndex = _HwBrasSbcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2, 1, 2),
    _HwBrasSbcSlotIndex_Type()
)
hwBrasSbcSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSlotIndex.setStatus("current")


class _HwBrasSbcCurrentSlotID_Type(Integer32):
    """Custom type hwBrasSbcCurrentSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBrasSbcCurrentSlotID_Type.__name__ = "Integer32"
_HwBrasSbcCurrentSlotID_Object = MibTableColumn
hwBrasSbcCurrentSlotID = _HwBrasSbcCurrentSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2, 1, 3),
    _HwBrasSbcCurrentSlotID_Type()
)
hwBrasSbcCurrentSlotID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcCurrentSlotID.setStatus("current")


class _HwBrasSbcSlotCfgState_Type(Integer32):
    """Custom type hwBrasSbcSlotCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwBrasSbcSlotCfgState_Type.__name__ = "Integer32"
_HwBrasSbcSlotCfgState_Object = MibTableColumn
hwBrasSbcSlotCfgState = _HwBrasSbcSlotCfgState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2, 1, 4),
    _HwBrasSbcSlotCfgState_Type()
)
hwBrasSbcSlotCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSlotCfgState.setStatus("current")
_HwBrasSbcSlotInforRowStatus_Type = RowStatus
_HwBrasSbcSlotInforRowStatus_Object = MibTableColumn
hwBrasSbcSlotInforRowStatus = _HwBrasSbcSlotInforRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 1, 4, 1, 2, 1, 5),
    _HwBrasSbcSlotInforRowStatus_Type()
)
hwBrasSbcSlotInforRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSlotInforRowStatus.setStatus("current")
_HwBrasSbcAdvance_ObjectIdentity = ObjectIdentity
hwBrasSbcAdvance = _HwBrasSbcAdvance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2)
)
_HwBrasSbcAdvanceLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcAdvanceLeaves = _HwBrasSbcAdvanceLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1)
)


class _HwBrasSbcMediaPassEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMediaPassEnable based on HWBrasEnabledStatus"""


_HwBrasSbcMediaPassEnable_Object = MibScalar
hwBrasSbcMediaPassEnable = _HwBrasSbcMediaPassEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 1),
    _HwBrasSbcMediaPassEnable_Type()
)
hwBrasSbcMediaPassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassEnable.setStatus("current")


class _HwBrasSbcMediaPassSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMediaPassSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcMediaPassSyslogEnable_Object = MibScalar
hwBrasSbcMediaPassSyslogEnable = _HwBrasSbcMediaPassSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 2),
    _HwBrasSbcMediaPassSyslogEnable_Type()
)
hwBrasSbcMediaPassSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassSyslogEnable.setStatus("current")


class _HwBrasSbcIntMediaPassEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIntMediaPassEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIntMediaPassEnable_Object = MibScalar
hwBrasSbcIntMediaPassEnable = _HwBrasSbcIntMediaPassEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 3),
    _HwBrasSbcIntMediaPassEnable_Type()
)
hwBrasSbcIntMediaPassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIntMediaPassEnable.setStatus("current")


class _HwBrasSbcRoamlimitEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcRoamlimitEnable based on HWBrasEnabledStatus"""


_HwBrasSbcRoamlimitEnable_Object = MibScalar
hwBrasSbcRoamlimitEnable = _HwBrasSbcRoamlimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 4),
    _HwBrasSbcRoamlimitEnable_Type()
)
hwBrasSbcRoamlimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitEnable.setStatus("current")


class _HwBrasSbcRoamlimitDefault_Type(HWBrasPermitStatus):
    """Custom type hwBrasSbcRoamlimitDefault based on HWBrasPermitStatus"""


_HwBrasSbcRoamlimitDefault_Object = MibScalar
hwBrasSbcRoamlimitDefault = _HwBrasSbcRoamlimitDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 5),
    _HwBrasSbcRoamlimitDefault_Type()
)
hwBrasSbcRoamlimitDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitDefault.setStatus("current")


class _HwBrasSbcRoamlimitSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcRoamlimitSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcRoamlimitSyslogEnable_Object = MibScalar
hwBrasSbcRoamlimitSyslogEnable = _HwBrasSbcRoamlimitSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 6),
    _HwBrasSbcRoamlimitSyslogEnable_Type()
)
hwBrasSbcRoamlimitSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitSyslogEnable.setStatus("current")


class _HwBrasSbcRoamlimitExtendEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcRoamlimitExtendEnable based on HWBrasEnabledStatus"""


_HwBrasSbcRoamlimitExtendEnable_Object = MibScalar
hwBrasSbcRoamlimitExtendEnable = _HwBrasSbcRoamlimitExtendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 7),
    _HwBrasSbcRoamlimitExtendEnable_Type()
)
hwBrasSbcRoamlimitExtendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitExtendEnable.setStatus("current")


class _HwBrasSbcHrpSynchronization_Type(Integer32):
    """Custom type hwBrasSbcHrpSynchronization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserve", 1),
          ("synchronize", 2))
    )


_HwBrasSbcHrpSynchronization_Type.__name__ = "Integer32"
_HwBrasSbcHrpSynchronization_Object = MibScalar
hwBrasSbcHrpSynchronization = _HwBrasSbcHrpSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 1, 8),
    _HwBrasSbcHrpSynchronization_Type()
)
hwBrasSbcHrpSynchronization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcHrpSynchronization.setStatus("current")
_HwBrasSbcAdvanceTables_ObjectIdentity = ObjectIdentity
hwBrasSbcAdvanceTables = _HwBrasSbcAdvanceTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2)
)
_HwBrasSbcMediaPassTable_Object = MibTable
hwBrasSbcMediaPassTable = _HwBrasSbcMediaPassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassTable.setStatus("current")
_HwBrasSbcMediaPassEntry_Object = MibTableRow
hwBrasSbcMediaPassEntry = _HwBrasSbcMediaPassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 1, 1)
)
hwBrasSbcMediaPassEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaPassIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassEntry.setStatus("current")


class _HwBrasSbcMediaPassIndex_Type(Integer32):
    """Custom type hwBrasSbcMediaPassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwBrasSbcMediaPassIndex_Type.__name__ = "Integer32"
_HwBrasSbcMediaPassIndex_Object = MibTableColumn
hwBrasSbcMediaPassIndex = _HwBrasSbcMediaPassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 1, 1, 1),
    _HwBrasSbcMediaPassIndex_Type()
)
hwBrasSbcMediaPassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassIndex.setStatus("current")


class _HwBrasSbcMediaPassAclNumber_Type(Integer32):
    """Custom type hwBrasSbcMediaPassAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwBrasSbcMediaPassAclNumber_Type.__name__ = "Integer32"
_HwBrasSbcMediaPassAclNumber_Object = MibTableColumn
hwBrasSbcMediaPassAclNumber = _HwBrasSbcMediaPassAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 1, 1, 2),
    _HwBrasSbcMediaPassAclNumber_Type()
)
hwBrasSbcMediaPassAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassAclNumber.setStatus("current")
_HwBrasSbcMediaPassRowStatus_Type = RowStatus
_HwBrasSbcMediaPassRowStatus_Object = MibTableColumn
hwBrasSbcMediaPassRowStatus = _HwBrasSbcMediaPassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 1, 1, 3),
    _HwBrasSbcMediaPassRowStatus_Type()
)
hwBrasSbcMediaPassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaPassRowStatus.setStatus("current")
_HwBrasSbcUsergroupTable_Object = MibTable
hwBrasSbcUsergroupTable = _HwBrasSbcUsergroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupTable.setStatus("current")
_HwBrasSbcUsergroupEntry_Object = MibTableRow
hwBrasSbcUsergroupEntry = _HwBrasSbcUsergroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 2, 1)
)
hwBrasSbcUsergroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupEntry.setStatus("current")


class _HwBrasSbcUsergroupIndex_Type(Integer32):
    """Custom type hwBrasSbcUsergroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwBrasSbcUsergroupIndex_Type.__name__ = "Integer32"
_HwBrasSbcUsergroupIndex_Object = MibTableColumn
hwBrasSbcUsergroupIndex = _HwBrasSbcUsergroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 2, 1, 1),
    _HwBrasSbcUsergroupIndex_Type()
)
hwBrasSbcUsergroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupIndex.setStatus("current")
_HwBrasSbcUsergroupRowStatus_Type = RowStatus
_HwBrasSbcUsergroupRowStatus_Object = MibTableColumn
hwBrasSbcUsergroupRowStatus = _HwBrasSbcUsergroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 2, 1, 2),
    _HwBrasSbcUsergroupRowStatus_Type()
)
hwBrasSbcUsergroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRowStatus.setStatus("current")
_HwBrasSbcUsergroupRuleTable_Object = MibTable
hwBrasSbcUsergroupRuleTable = _HwBrasSbcUsergroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRuleTable.setStatus("current")
_HwBrasSbcUsergroupRuleEntry_Object = MibTableRow
hwBrasSbcUsergroupRuleEntry = _HwBrasSbcUsergroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 3, 1)
)
hwBrasSbcUsergroupRuleEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupRuleIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRuleEntry.setStatus("current")


class _HwBrasSbcUsergroupRuleIndex_Type(Integer32):
    """Custom type hwBrasSbcUsergroupRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBrasSbcUsergroupRuleIndex_Type.__name__ = "Integer32"
_HwBrasSbcUsergroupRuleIndex_Object = MibTableColumn
hwBrasSbcUsergroupRuleIndex = _HwBrasSbcUsergroupRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 3, 1, 1),
    _HwBrasSbcUsergroupRuleIndex_Type()
)
hwBrasSbcUsergroupRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRuleIndex.setStatus("current")
_HwBrasSbcUsergroupRuleType_Type = HWBrasPermitStatus
_HwBrasSbcUsergroupRuleType_Object = MibTableColumn
hwBrasSbcUsergroupRuleType = _HwBrasSbcUsergroupRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 3, 1, 2),
    _HwBrasSbcUsergroupRuleType_Type()
)
hwBrasSbcUsergroupRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRuleType.setStatus("current")


class _HwBrasSbcUsergroupRuleUserName_Type(DisplayString):
    """Custom type hwBrasSbcUsergroupRuleUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwBrasSbcUsergroupRuleUserName_Type.__name__ = "DisplayString"
_HwBrasSbcUsergroupRuleUserName_Object = MibTableColumn
hwBrasSbcUsergroupRuleUserName = _HwBrasSbcUsergroupRuleUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 3, 1, 3),
    _HwBrasSbcUsergroupRuleUserName_Type()
)
hwBrasSbcUsergroupRuleUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRuleUserName.setStatus("current")
_HwBrasSbcUsergroupRuleRowStatus_Type = RowStatus
_HwBrasSbcUsergroupRuleRowStatus_Object = MibTableColumn
hwBrasSbcUsergroupRuleRowStatus = _HwBrasSbcUsergroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 3, 1, 4),
    _HwBrasSbcUsergroupRuleRowStatus_Type()
)
hwBrasSbcUsergroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUsergroupRuleRowStatus.setStatus("current")
_HwBrasSbcRtpSpecialAddrTable_Object = MibTable
hwBrasSbcRtpSpecialAddrTable = _HwBrasSbcRtpSpecialAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcRtpSpecialAddrTable.setStatus("current")
_HwBrasSbcRtpSpecialAddrEntry_Object = MibTableRow
hwBrasSbcRtpSpecialAddrEntry = _HwBrasSbcRtpSpecialAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 4, 1)
)
hwBrasSbcRtpSpecialAddrEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRtpSpecialAddrIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcRtpSpecialAddrEntry.setStatus("current")


class _HwBrasSbcRtpSpecialAddrIndex_Type(Integer32):
    """Custom type hwBrasSbcRtpSpecialAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwBrasSbcRtpSpecialAddrIndex_Type.__name__ = "Integer32"
_HwBrasSbcRtpSpecialAddrIndex_Object = MibTableColumn
hwBrasSbcRtpSpecialAddrIndex = _HwBrasSbcRtpSpecialAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 4, 1, 1),
    _HwBrasSbcRtpSpecialAddrIndex_Type()
)
hwBrasSbcRtpSpecialAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcRtpSpecialAddrIndex.setStatus("current")
_HwBrasSbcRtpSpecialAddrAddr_Type = IpAddress
_HwBrasSbcRtpSpecialAddrAddr_Object = MibTableColumn
hwBrasSbcRtpSpecialAddrAddr = _HwBrasSbcRtpSpecialAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 4, 1, 2),
    _HwBrasSbcRtpSpecialAddrAddr_Type()
)
hwBrasSbcRtpSpecialAddrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcRtpSpecialAddrAddr.setStatus("current")
_HwBrasSbcRtpSpecialAddrRowStatus_Type = RowStatus
_HwBrasSbcRtpSpecialAddrRowStatus_Object = MibTableColumn
hwBrasSbcRtpSpecialAddrRowStatus = _HwBrasSbcRtpSpecialAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 4, 1, 3),
    _HwBrasSbcRtpSpecialAddrRowStatus_Type()
)
hwBrasSbcRtpSpecialAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcRtpSpecialAddrRowStatus.setStatus("current")
_HwBrasSbcRoamlimitTable_Object = MibTable
hwBrasSbcRoamlimitTable = _HwBrasSbcRoamlimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitTable.setStatus("current")
_HwBrasSbcRoamlimitEntry_Object = MibTableRow
hwBrasSbcRoamlimitEntry = _HwBrasSbcRoamlimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 5, 1)
)
hwBrasSbcRoamlimitEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitEntry.setStatus("current")


class _HwBrasSbcRoamlimitIndex_Type(Unsigned32):
    """Custom type hwBrasSbcRoamlimitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwBrasSbcRoamlimitIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcRoamlimitIndex_Object = MibTableColumn
hwBrasSbcRoamlimitIndex = _HwBrasSbcRoamlimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 5, 1, 1),
    _HwBrasSbcRoamlimitIndex_Type()
)
hwBrasSbcRoamlimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitIndex.setStatus("current")


class _HwBrasSbcRoamlimitAclNumber_Type(Unsigned32):
    """Custom type hwBrasSbcRoamlimitAclNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2999),
    )


_HwBrasSbcRoamlimitAclNumber_Type.__name__ = "Unsigned32"
_HwBrasSbcRoamlimitAclNumber_Object = MibTableColumn
hwBrasSbcRoamlimitAclNumber = _HwBrasSbcRoamlimitAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 5, 1, 2),
    _HwBrasSbcRoamlimitAclNumber_Type()
)
hwBrasSbcRoamlimitAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitAclNumber.setStatus("current")
_HwBrasSbcRoamlimitRowStatus_Type = RowStatus
_HwBrasSbcRoamlimitRowStatus_Object = MibTableColumn
hwBrasSbcRoamlimitRowStatus = _HwBrasSbcRoamlimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 5, 1, 3),
    _HwBrasSbcRoamlimitRowStatus_Type()
)
hwBrasSbcRoamlimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcRoamlimitRowStatus.setStatus("current")
_HwBrasSbcMediaUsersTable_Object = MibTable
hwBrasSbcMediaUsersTable = _HwBrasSbcMediaUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersTable.setStatus("current")
_HwBrasSbcMediaUsersEntry_Object = MibTableRow
hwBrasSbcMediaUsersEntry = _HwBrasSbcMediaUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1)
)
hwBrasSbcMediaUsersEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersEntry.setStatus("current")


class _HwBrasSbcMediaUsersIndex_Type(Integer32):
    """Custom type hwBrasSbcMediaUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwBrasSbcMediaUsersIndex_Type.__name__ = "Integer32"
_HwBrasSbcMediaUsersIndex_Object = MibTableColumn
hwBrasSbcMediaUsersIndex = _HwBrasSbcMediaUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 1),
    _HwBrasSbcMediaUsersIndex_Type()
)
hwBrasSbcMediaUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersIndex.setStatus("current")


class _HwBrasSbcMediaUsersType_Type(Integer32):
    """Custom type hwBrasSbcMediaUsersType based on Integer32"""
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
        *(("audio", 2),
          ("data", 4),
          ("media", 1),
          ("video", 3))
    )


_HwBrasSbcMediaUsersType_Type.__name__ = "Integer32"
_HwBrasSbcMediaUsersType_Object = MibTableColumn
hwBrasSbcMediaUsersType = _HwBrasSbcMediaUsersType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 2),
    _HwBrasSbcMediaUsersType_Type()
)
hwBrasSbcMediaUsersType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersType.setStatus("current")


class _HwBrasSbcMediaUsersCallerID1_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCallerID1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCallerID1_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCallerID1_Object = MibTableColumn
hwBrasSbcMediaUsersCallerID1 = _HwBrasSbcMediaUsersCallerID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 3),
    _HwBrasSbcMediaUsersCallerID1_Type()
)
hwBrasSbcMediaUsersCallerID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCallerID1.setStatus("current")


class _HwBrasSbcMediaUsersCallerID2_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCallerID2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCallerID2_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCallerID2_Object = MibTableColumn
hwBrasSbcMediaUsersCallerID2 = _HwBrasSbcMediaUsersCallerID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 4),
    _HwBrasSbcMediaUsersCallerID2_Type()
)
hwBrasSbcMediaUsersCallerID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCallerID2.setStatus("current")


class _HwBrasSbcMediaUsersCallerID3_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCallerID3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCallerID3_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCallerID3_Object = MibTableColumn
hwBrasSbcMediaUsersCallerID3 = _HwBrasSbcMediaUsersCallerID3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 5),
    _HwBrasSbcMediaUsersCallerID3_Type()
)
hwBrasSbcMediaUsersCallerID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCallerID3.setStatus("current")


class _HwBrasSbcMediaUsersCallerID4_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCallerID4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCallerID4_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCallerID4_Object = MibTableColumn
hwBrasSbcMediaUsersCallerID4 = _HwBrasSbcMediaUsersCallerID4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 6),
    _HwBrasSbcMediaUsersCallerID4_Type()
)
hwBrasSbcMediaUsersCallerID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCallerID4.setStatus("current")


class _HwBrasSbcMediaUsersCalleeID1_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCalleeID1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCalleeID1_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCalleeID1_Object = MibTableColumn
hwBrasSbcMediaUsersCalleeID1 = _HwBrasSbcMediaUsersCalleeID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 7),
    _HwBrasSbcMediaUsersCalleeID1_Type()
)
hwBrasSbcMediaUsersCalleeID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCalleeID1.setStatus("current")


class _HwBrasSbcMediaUsersCalleeID2_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCalleeID2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCalleeID2_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCalleeID2_Object = MibTableColumn
hwBrasSbcMediaUsersCalleeID2 = _HwBrasSbcMediaUsersCalleeID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 8),
    _HwBrasSbcMediaUsersCalleeID2_Type()
)
hwBrasSbcMediaUsersCalleeID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCalleeID2.setStatus("current")


class _HwBrasSbcMediaUsersCalleeID3_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCalleeID3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCalleeID3_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCalleeID3_Object = MibTableColumn
hwBrasSbcMediaUsersCalleeID3 = _HwBrasSbcMediaUsersCalleeID3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 9),
    _HwBrasSbcMediaUsersCalleeID3_Type()
)
hwBrasSbcMediaUsersCalleeID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCalleeID3.setStatus("current")


class _HwBrasSbcMediaUsersCalleeID4_Type(DisplayString):
    """Custom type hwBrasSbcMediaUsersCalleeID4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcMediaUsersCalleeID4_Type.__name__ = "DisplayString"
_HwBrasSbcMediaUsersCalleeID4_Object = MibTableColumn
hwBrasSbcMediaUsersCalleeID4 = _HwBrasSbcMediaUsersCalleeID4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 10),
    _HwBrasSbcMediaUsersCalleeID4_Type()
)
hwBrasSbcMediaUsersCalleeID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersCalleeID4.setStatus("current")
_HwBrasSbcMediaUsersRowStatus_Type = RowStatus
_HwBrasSbcMediaUsersRowStatus_Object = MibTableColumn
hwBrasSbcMediaUsersRowStatus = _HwBrasSbcMediaUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 2, 6, 1, 11),
    _HwBrasSbcMediaUsersRowStatus_Type()
)
hwBrasSbcMediaUsersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMediaUsersRowStatus.setStatus("current")
_HwBrasSbcIntercom_ObjectIdentity = ObjectIdentity
hwBrasSbcIntercom = _HwBrasSbcIntercom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3)
)
_HwBrasSbcIntercomLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcIntercomLeaves = _HwBrasSbcIntercomLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 1)
)


class _HwBrasSbcIntercomEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIntercomEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIntercomEnable_Object = MibScalar
hwBrasSbcIntercomEnable = _HwBrasSbcIntercomEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 1, 1),
    _HwBrasSbcIntercomEnable_Type()
)
hwBrasSbcIntercomEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIntercomEnable.setStatus("current")


class _HwBrasSbcIntercomStatus_Type(Integer32):
    """Custom type hwBrasSbcIntercomStatus based on Integer32"""
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
        *(("disabled", 1),
          ("iproute", 2),
          ("prefixroute", 3))
    )


_HwBrasSbcIntercomStatus_Type.__name__ = "Integer32"
_HwBrasSbcIntercomStatus_Object = MibScalar
hwBrasSbcIntercomStatus = _HwBrasSbcIntercomStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 1, 2),
    _HwBrasSbcIntercomStatus_Type()
)
hwBrasSbcIntercomStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIntercomStatus.setStatus("current")
_HwBrasSbcIntercomTables_ObjectIdentity = ObjectIdentity
hwBrasSbcIntercomTables = _HwBrasSbcIntercomTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2)
)
_HwBrasSbcIntercomPrefixTable_Object = MibTable
hwBrasSbcIntercomPrefixTable = _HwBrasSbcIntercomPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcIntercomPrefixTable.setStatus("current")
_HwBrasSbcIntercomPrefixEntry_Object = MibTableRow
hwBrasSbcIntercomPrefixEntry = _HwBrasSbcIntercomPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2, 1, 1)
)
hwBrasSbcIntercomPrefixEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntercomPrefixIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIntercomPrefixEntry.setStatus("current")


class _HwBrasSbcIntercomPrefixIndex_Type(DisplayString):
    """Custom type hwBrasSbcIntercomPrefixIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwBrasSbcIntercomPrefixIndex_Type.__name__ = "DisplayString"
_HwBrasSbcIntercomPrefixIndex_Object = MibTableColumn
hwBrasSbcIntercomPrefixIndex = _HwBrasSbcIntercomPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2, 1, 1, 1),
    _HwBrasSbcIntercomPrefixIndex_Type()
)
hwBrasSbcIntercomPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIntercomPrefixIndex.setStatus("current")
_HwBrasSbcIntercomPrefixDestAddr_Type = IpAddress
_HwBrasSbcIntercomPrefixDestAddr_Object = MibTableColumn
hwBrasSbcIntercomPrefixDestAddr = _HwBrasSbcIntercomPrefixDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2, 1, 1, 2),
    _HwBrasSbcIntercomPrefixDestAddr_Type()
)
hwBrasSbcIntercomPrefixDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIntercomPrefixDestAddr.setStatus("current")
_HwBrasSbcIntercomPrefixSrcAddr_Type = IpAddress
_HwBrasSbcIntercomPrefixSrcAddr_Object = MibTableColumn
hwBrasSbcIntercomPrefixSrcAddr = _HwBrasSbcIntercomPrefixSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2, 1, 1, 3),
    _HwBrasSbcIntercomPrefixSrcAddr_Type()
)
hwBrasSbcIntercomPrefixSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIntercomPrefixSrcAddr.setStatus("current")
_HwBrasSbcIntercomPrefixRowStatus_Type = RowStatus
_HwBrasSbcIntercomPrefixRowStatus_Object = MibTableColumn
hwBrasSbcIntercomPrefixRowStatus = _HwBrasSbcIntercomPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 3, 2, 1, 1, 4),
    _HwBrasSbcIntercomPrefixRowStatus_Type()
)
hwBrasSbcIntercomPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIntercomPrefixRowStatus.setStatus("current")
_HwBrasSbcSessionCar_ObjectIdentity = ObjectIdentity
hwBrasSbcSessionCar = _HwBrasSbcSessionCar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4)
)
_HwBrasSbcSessionCarLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcSessionCarLeaves = _HwBrasSbcSessionCarLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 1)
)


class _HwBrasSbcSessionCarEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSessionCarEnable based on HWBrasEnabledStatus"""


_HwBrasSbcSessionCarEnable_Object = MibScalar
hwBrasSbcSessionCarEnable = _HwBrasSbcSessionCarEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 1, 1),
    _HwBrasSbcSessionCarEnable_Type()
)
hwBrasSbcSessionCarEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarEnable.setStatus("current")
_HwBrasSbcSessionCarTables_ObjectIdentity = ObjectIdentity
hwBrasSbcSessionCarTables = _HwBrasSbcSessionCarTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2)
)
_HwBrasSbcSessionCarDegreeTable_Object = MibTable
hwBrasSbcSessionCarDegreeTable = _HwBrasSbcSessionCarDegreeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarDegreeTable.setStatus("current")
_HwBrasSbcSessionCarDegreeEntry_Object = MibTableRow
hwBrasSbcSessionCarDegreeEntry = _HwBrasSbcSessionCarDegreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 1, 1)
)
hwBrasSbcSessionCarDegreeEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarDegreeID"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarDegreeEntry.setStatus("current")


class _HwBrasSbcSessionCarDegreeID_Type(Integer32):
    """Custom type hwBrasSbcSessionCarDegreeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBrasSbcSessionCarDegreeID_Type.__name__ = "Integer32"
_HwBrasSbcSessionCarDegreeID_Object = MibTableColumn
hwBrasSbcSessionCarDegreeID = _HwBrasSbcSessionCarDegreeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 1, 1, 1),
    _HwBrasSbcSessionCarDegreeID_Type()
)
hwBrasSbcSessionCarDegreeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarDegreeID.setStatus("current")


class _HwBrasSbcSessionCarDegreeBandWidth_Type(Unsigned32):
    """Custom type hwBrasSbcSessionCarDegreeBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 131071),
    )


_HwBrasSbcSessionCarDegreeBandWidth_Type.__name__ = "Unsigned32"
_HwBrasSbcSessionCarDegreeBandWidth_Object = MibTableColumn
hwBrasSbcSessionCarDegreeBandWidth = _HwBrasSbcSessionCarDegreeBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 1, 1, 2),
    _HwBrasSbcSessionCarDegreeBandWidth_Type()
)
hwBrasSbcSessionCarDegreeBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarDegreeBandWidth.setStatus("current")


class _HwBrasSbcSessionCarDegreeDscp_Type(Integer32):
    """Custom type hwBrasSbcSessionCarDegreeDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwBrasSbcSessionCarDegreeDscp_Type.__name__ = "Integer32"
_HwBrasSbcSessionCarDegreeDscp_Object = MibTableColumn
hwBrasSbcSessionCarDegreeDscp = _HwBrasSbcSessionCarDegreeDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 1, 1, 3),
    _HwBrasSbcSessionCarDegreeDscp_Type()
)
hwBrasSbcSessionCarDegreeDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarDegreeDscp.setStatus("current")
_HwBrasSbcSessionCarDegreeRowStatus_Type = RowStatus
_HwBrasSbcSessionCarDegreeRowStatus_Object = MibTableColumn
hwBrasSbcSessionCarDegreeRowStatus = _HwBrasSbcSessionCarDegreeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 1, 1, 4),
    _HwBrasSbcSessionCarDegreeRowStatus_Type()
)
hwBrasSbcSessionCarDegreeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarDegreeRowStatus.setStatus("current")
_HwBrasSbcSessionCarRuleTable_Object = MibTable
hwBrasSbcSessionCarRuleTable = _HwBrasSbcSessionCarRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleTable.setStatus("current")
_HwBrasSbcSessionCarRuleEntry_Object = MibTableRow
hwBrasSbcSessionCarRuleEntry = _HwBrasSbcSessionCarRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1)
)
hwBrasSbcSessionCarRuleEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarRuleID"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleEntry.setStatus("current")


class _HwBrasSbcSessionCarRuleID_Type(Integer32):
    """Custom type hwBrasSbcSessionCarRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwBrasSbcSessionCarRuleID_Type.__name__ = "Integer32"
_HwBrasSbcSessionCarRuleID_Object = MibTableColumn
hwBrasSbcSessionCarRuleID = _HwBrasSbcSessionCarRuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1, 1),
    _HwBrasSbcSessionCarRuleID_Type()
)
hwBrasSbcSessionCarRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleID.setStatus("current")


class _HwBrasSbcSessionCarRuleName_Type(DisplayString):
    """Custom type hwBrasSbcSessionCarRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwBrasSbcSessionCarRuleName_Type.__name__ = "DisplayString"
_HwBrasSbcSessionCarRuleName_Object = MibTableColumn
hwBrasSbcSessionCarRuleName = _HwBrasSbcSessionCarRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1, 2),
    _HwBrasSbcSessionCarRuleName_Type()
)
hwBrasSbcSessionCarRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleName.setStatus("current")


class _HwBrasSbcSessionCarRuleDegreeID_Type(Integer32):
    """Custom type hwBrasSbcSessionCarRuleDegreeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBrasSbcSessionCarRuleDegreeID_Type.__name__ = "Integer32"
_HwBrasSbcSessionCarRuleDegreeID_Object = MibTableColumn
hwBrasSbcSessionCarRuleDegreeID = _HwBrasSbcSessionCarRuleDegreeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1, 3),
    _HwBrasSbcSessionCarRuleDegreeID_Type()
)
hwBrasSbcSessionCarRuleDegreeID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleDegreeID.setStatus("current")


class _HwBrasSbcSessionCarRuleDegreeBandWidth_Type(Unsigned32):
    """Custom type hwBrasSbcSessionCarRuleDegreeBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 131071),
    )


_HwBrasSbcSessionCarRuleDegreeBandWidth_Type.__name__ = "Unsigned32"
_HwBrasSbcSessionCarRuleDegreeBandWidth_Object = MibTableColumn
hwBrasSbcSessionCarRuleDegreeBandWidth = _HwBrasSbcSessionCarRuleDegreeBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1, 4),
    _HwBrasSbcSessionCarRuleDegreeBandWidth_Type()
)
hwBrasSbcSessionCarRuleDegreeBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleDegreeBandWidth.setStatus("current")


class _HwBrasSbcSessionCarRuleDegreeDscp_Type(Integer32):
    """Custom type hwBrasSbcSessionCarRuleDegreeDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwBrasSbcSessionCarRuleDegreeDscp_Type.__name__ = "Integer32"
_HwBrasSbcSessionCarRuleDegreeDscp_Object = MibTableColumn
hwBrasSbcSessionCarRuleDegreeDscp = _HwBrasSbcSessionCarRuleDegreeDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1, 5),
    _HwBrasSbcSessionCarRuleDegreeDscp_Type()
)
hwBrasSbcSessionCarRuleDegreeDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleDegreeDscp.setStatus("current")
_HwBrasSbcSessionCarRuleRowStatus_Type = RowStatus
_HwBrasSbcSessionCarRuleRowStatus_Object = MibTableColumn
hwBrasSbcSessionCarRuleRowStatus = _HwBrasSbcSessionCarRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 4, 2, 2, 1, 6),
    _HwBrasSbcSessionCarRuleRowStatus_Type()
)
hwBrasSbcSessionCarRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSessionCarRuleRowStatus.setStatus("current")
_HwBrasSbcSecurity_ObjectIdentity = ObjectIdentity
hwBrasSbcSecurity = _HwBrasSbcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5)
)
_HwBrasSbcSecurityLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcSecurityLeaves = _HwBrasSbcSecurityLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1)
)


class _HwBrasSbcDefendEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcDefendEnable based on HWBrasEnabledStatus"""


_HwBrasSbcDefendEnable_Object = MibScalar
hwBrasSbcDefendEnable = _HwBrasSbcDefendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 1),
    _HwBrasSbcDefendEnable_Type()
)
hwBrasSbcDefendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendEnable.setStatus("current")


class _HwBrasSbcDefendMode_Type(Integer32):
    """Custom type hwBrasSbcDefendMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_HwBrasSbcDefendMode_Type.__name__ = "Integer32"
_HwBrasSbcDefendMode_Object = MibScalar
hwBrasSbcDefendMode = _HwBrasSbcDefendMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 2),
    _HwBrasSbcDefendMode_Type()
)
hwBrasSbcDefendMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendMode.setStatus("current")


class _HwBrasSbcDefendActionLogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcDefendActionLogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcDefendActionLogEnable_Object = MibScalar
hwBrasSbcDefendActionLogEnable = _HwBrasSbcDefendActionLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 3),
    _HwBrasSbcDefendActionLogEnable_Type()
)
hwBrasSbcDefendActionLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendActionLogEnable.setStatus("current")


class _HwBrasSbcCacEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcCacEnable based on HWBrasEnabledStatus"""


_HwBrasSbcCacEnable_Object = MibScalar
hwBrasSbcCacEnable = _HwBrasSbcCacEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 4),
    _HwBrasSbcCacEnable_Type()
)
hwBrasSbcCacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacEnable.setStatus("current")


class _HwBrasSbcCacActionLogStatus_Type(Integer32):
    """Custom type hwBrasSbcCacActionLogStatus based on Integer32"""
    defaultValue = 1

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
        *(("denyAndLog", 3),
          ("denyAndNoLog", 1),
          ("permitAndLog", 4),
          ("permitAndNoLog", 2))
    )


_HwBrasSbcCacActionLogStatus_Type.__name__ = "Integer32"
_HwBrasSbcCacActionLogStatus_Object = MibScalar
hwBrasSbcCacActionLogStatus = _HwBrasSbcCacActionLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 5),
    _HwBrasSbcCacActionLogStatus_Type()
)
hwBrasSbcCacActionLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacActionLogStatus.setStatus("current")


class _HwBrasSbcDefendExtStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcDefendExtStatus based on HWBrasEnabledStatus"""


_HwBrasSbcDefendExtStatus_Object = MibScalar
hwBrasSbcDefendExtStatus = _HwBrasSbcDefendExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 6),
    _HwBrasSbcDefendExtStatus_Type()
)
hwBrasSbcDefendExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendExtStatus.setStatus("current")


class _HwBrasSbcSignalingCarStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSignalingCarStatus based on HWBrasEnabledStatus"""


_HwBrasSbcSignalingCarStatus_Object = MibScalar
hwBrasSbcSignalingCarStatus = _HwBrasSbcSignalingCarStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 7),
    _HwBrasSbcSignalingCarStatus_Type()
)
hwBrasSbcSignalingCarStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSignalingCarStatus.setStatus("current")


class _HwBrasSbcIPCarStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIPCarStatus based on HWBrasEnabledStatus"""


_HwBrasSbcIPCarStatus_Object = MibScalar
hwBrasSbcIPCarStatus = _HwBrasSbcIPCarStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 8),
    _HwBrasSbcIPCarStatus_Type()
)
hwBrasSbcIPCarStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIPCarStatus.setStatus("current")


class _HwBrasSbcDynamicStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcDynamicStatus based on HWBrasEnabledStatus"""


_HwBrasSbcDynamicStatus_Object = MibScalar
hwBrasSbcDynamicStatus = _HwBrasSbcDynamicStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 1, 9),
    _HwBrasSbcDynamicStatus_Type()
)
hwBrasSbcDynamicStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDynamicStatus.setStatus("current")
_HwBrasSbcSecurityTables_ObjectIdentity = ObjectIdentity
hwBrasSbcSecurityTables = _HwBrasSbcSecurityTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2)
)
_HwBrasSbcDefendConnectRateTable_Object = MibTable
hwBrasSbcDefendConnectRateTable = _HwBrasSbcDefendConnectRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcDefendConnectRateTable.setStatus("current")
_HwBrasSbcDefendConnectRateEntry_Object = MibTableRow
hwBrasSbcDefendConnectRateEntry = _HwBrasSbcDefendConnectRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 1, 1)
)
hwBrasSbcDefendConnectRateEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendConnectRateProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcDefendConnectRateEntry.setStatus("current")
_HwBrasSbcDefendConnectRateProtocol_Type = HWBrasSecurityProtocol
_HwBrasSbcDefendConnectRateProtocol_Object = MibTableColumn
hwBrasSbcDefendConnectRateProtocol = _HwBrasSbcDefendConnectRateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 1, 1, 1),
    _HwBrasSbcDefendConnectRateProtocol_Type()
)
hwBrasSbcDefendConnectRateProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcDefendConnectRateProtocol.setStatus("current")


class _HwBrasSbcDefendConnectRateThreshold_Type(Unsigned32):
    """Custom type hwBrasSbcDefendConnectRateThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 60000),
    )


_HwBrasSbcDefendConnectRateThreshold_Type.__name__ = "Unsigned32"
_HwBrasSbcDefendConnectRateThreshold_Object = MibTableColumn
hwBrasSbcDefendConnectRateThreshold = _HwBrasSbcDefendConnectRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 1, 1, 2),
    _HwBrasSbcDefendConnectRateThreshold_Type()
)
hwBrasSbcDefendConnectRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendConnectRateThreshold.setStatus("current")


class _HwBrasSbcDefendConnectRatePercent_Type(Unsigned32):
    """Custom type hwBrasSbcDefendConnectRatePercent based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_HwBrasSbcDefendConnectRatePercent_Type.__name__ = "Unsigned32"
_HwBrasSbcDefendConnectRatePercent_Object = MibTableColumn
hwBrasSbcDefendConnectRatePercent = _HwBrasSbcDefendConnectRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 1, 1, 3),
    _HwBrasSbcDefendConnectRatePercent_Type()
)
hwBrasSbcDefendConnectRatePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendConnectRatePercent.setStatus("current")
_HwBrasSbcDefendConnectRateRowStatus_Type = RowStatus
_HwBrasSbcDefendConnectRateRowStatus_Object = MibTableColumn
hwBrasSbcDefendConnectRateRowStatus = _HwBrasSbcDefendConnectRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 1, 1, 4),
    _HwBrasSbcDefendConnectRateRowStatus_Type()
)
hwBrasSbcDefendConnectRateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendConnectRateRowStatus.setStatus("current")
_HwBrasSbcDefendUserConnectRateTable_Object = MibTable
hwBrasSbcDefendUserConnectRateTable = _HwBrasSbcDefendUserConnectRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcDefendUserConnectRateTable.setStatus("current")
_HwBrasSbcDefendUserConnectRateEntry_Object = MibTableRow
hwBrasSbcDefendUserConnectRateEntry = _HwBrasSbcDefendUserConnectRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 2, 1)
)
hwBrasSbcDefendUserConnectRateEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendUserConnectRateProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcDefendUserConnectRateEntry.setStatus("current")
_HwBrasSbcDefendUserConnectRateProtocol_Type = HWBrasSecurityProtocol
_HwBrasSbcDefendUserConnectRateProtocol_Object = MibTableColumn
hwBrasSbcDefendUserConnectRateProtocol = _HwBrasSbcDefendUserConnectRateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 2, 1, 1),
    _HwBrasSbcDefendUserConnectRateProtocol_Type()
)
hwBrasSbcDefendUserConnectRateProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcDefendUserConnectRateProtocol.setStatus("current")


class _HwBrasSbcDefendUserConnectRateThreshold_Type(Unsigned32):
    """Custom type hwBrasSbcDefendUserConnectRateThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 60000),
    )


_HwBrasSbcDefendUserConnectRateThreshold_Type.__name__ = "Unsigned32"
_HwBrasSbcDefendUserConnectRateThreshold_Object = MibTableColumn
hwBrasSbcDefendUserConnectRateThreshold = _HwBrasSbcDefendUserConnectRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 2, 1, 2),
    _HwBrasSbcDefendUserConnectRateThreshold_Type()
)
hwBrasSbcDefendUserConnectRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendUserConnectRateThreshold.setStatus("current")


class _HwBrasSbcDefendUserConnectRatePercent_Type(Unsigned32):
    """Custom type hwBrasSbcDefendUserConnectRatePercent based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_HwBrasSbcDefendUserConnectRatePercent_Type.__name__ = "Unsigned32"
_HwBrasSbcDefendUserConnectRatePercent_Object = MibTableColumn
hwBrasSbcDefendUserConnectRatePercent = _HwBrasSbcDefendUserConnectRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 2, 1, 3),
    _HwBrasSbcDefendUserConnectRatePercent_Type()
)
hwBrasSbcDefendUserConnectRatePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendUserConnectRatePercent.setStatus("current")
_HwBrasSbcDefendUserConnectRateRowStatus_Type = RowStatus
_HwBrasSbcDefendUserConnectRateRowStatus_Object = MibTableColumn
hwBrasSbcDefendUserConnectRateRowStatus = _HwBrasSbcDefendUserConnectRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 2, 1, 4),
    _HwBrasSbcDefendUserConnectRateRowStatus_Type()
)
hwBrasSbcDefendUserConnectRateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDefendUserConnectRateRowStatus.setStatus("current")
_HwBrasSbcCacCallTotalTable_Object = MibTable
hwBrasSbcCacCallTotalTable = _HwBrasSbcCacCallTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcCacCallTotalTable.setStatus("current")
_HwBrasSbcCacCallTotalEntry_Object = MibTableRow
hwBrasSbcCacCallTotalEntry = _HwBrasSbcCacCallTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 3, 1)
)
hwBrasSbcCacCallTotalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallTotalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcCacCallTotalEntry.setStatus("current")
_HwBrasSbcCacCallTotalProtocol_Type = HWBrasSecurityProtocol
_HwBrasSbcCacCallTotalProtocol_Object = MibTableColumn
hwBrasSbcCacCallTotalProtocol = _HwBrasSbcCacCallTotalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 3, 1, 1),
    _HwBrasSbcCacCallTotalProtocol_Type()
)
hwBrasSbcCacCallTotalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallTotalProtocol.setStatus("current")


class _HwBrasSbcCacCallTotalThreshold_Type(Unsigned32):
    """Custom type hwBrasSbcCacCallTotalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 60000),
    )


_HwBrasSbcCacCallTotalThreshold_Type.__name__ = "Unsigned32"
_HwBrasSbcCacCallTotalThreshold_Object = MibTableColumn
hwBrasSbcCacCallTotalThreshold = _HwBrasSbcCacCallTotalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 3, 1, 2),
    _HwBrasSbcCacCallTotalThreshold_Type()
)
hwBrasSbcCacCallTotalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallTotalThreshold.setStatus("current")


class _HwBrasSbcCacCallTotalPercent_Type(Unsigned32):
    """Custom type hwBrasSbcCacCallTotalPercent based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_HwBrasSbcCacCallTotalPercent_Type.__name__ = "Unsigned32"
_HwBrasSbcCacCallTotalPercent_Object = MibTableColumn
hwBrasSbcCacCallTotalPercent = _HwBrasSbcCacCallTotalPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 3, 1, 3),
    _HwBrasSbcCacCallTotalPercent_Type()
)
hwBrasSbcCacCallTotalPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallTotalPercent.setStatus("current")
_HwBrasSbcCacCallTotalRowStatus_Type = RowStatus
_HwBrasSbcCacCallTotalRowStatus_Object = MibTableColumn
hwBrasSbcCacCallTotalRowStatus = _HwBrasSbcCacCallTotalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 3, 1, 4),
    _HwBrasSbcCacCallTotalRowStatus_Type()
)
hwBrasSbcCacCallTotalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallTotalRowStatus.setStatus("current")
_HwBrasSbcCacCallRateTable_Object = MibTable
hwBrasSbcCacCallRateTable = _HwBrasSbcCacCallRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcCacCallRateTable.setStatus("current")
_HwBrasSbcCacCallRateEntry_Object = MibTableRow
hwBrasSbcCacCallRateEntry = _HwBrasSbcCacCallRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 4, 1)
)
hwBrasSbcCacCallRateEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallRateProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcCacCallRateEntry.setStatus("current")
_HwBrasSbcCacCallRateProtocol_Type = HWBrasSecurityProtocol
_HwBrasSbcCacCallRateProtocol_Object = MibTableColumn
hwBrasSbcCacCallRateProtocol = _HwBrasSbcCacCallRateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 4, 1, 1),
    _HwBrasSbcCacCallRateProtocol_Type()
)
hwBrasSbcCacCallRateProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallRateProtocol.setStatus("current")


class _HwBrasSbcCacCallRateThreshold_Type(Unsigned32):
    """Custom type hwBrasSbcCacCallRateThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 600),
    )


_HwBrasSbcCacCallRateThreshold_Type.__name__ = "Unsigned32"
_HwBrasSbcCacCallRateThreshold_Object = MibTableColumn
hwBrasSbcCacCallRateThreshold = _HwBrasSbcCacCallRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 4, 1, 2),
    _HwBrasSbcCacCallRateThreshold_Type()
)
hwBrasSbcCacCallRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallRateThreshold.setStatus("current")


class _HwBrasSbcCacCallRatePercent_Type(Unsigned32):
    """Custom type hwBrasSbcCacCallRatePercent based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_HwBrasSbcCacCallRatePercent_Type.__name__ = "Unsigned32"
_HwBrasSbcCacCallRatePercent_Object = MibTableColumn
hwBrasSbcCacCallRatePercent = _HwBrasSbcCacCallRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 4, 1, 3),
    _HwBrasSbcCacCallRatePercent_Type()
)
hwBrasSbcCacCallRatePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallRatePercent.setStatus("current")
_HwBrasSbcCacCallRateRowStatus_Type = RowStatus
_HwBrasSbcCacCallRateRowStatus_Object = MibTableColumn
hwBrasSbcCacCallRateRowStatus = _HwBrasSbcCacCallRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 4, 1, 4),
    _HwBrasSbcCacCallRateRowStatus_Type()
)
hwBrasSbcCacCallRateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacCallRateRowStatus.setStatus("current")
_HwBrasSbcCacRegTotalTable_Object = MibTable
hwBrasSbcCacRegTotalTable = _HwBrasSbcCacRegTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcCacRegTotalTable.setStatus("current")
_HwBrasSbcCacRegTotalEntry_Object = MibTableRow
hwBrasSbcCacRegTotalEntry = _HwBrasSbcCacRegTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 5, 1)
)
hwBrasSbcCacRegTotalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegTotalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcCacRegTotalEntry.setStatus("current")
_HwBrasSbcCacRegTotalProtocol_Type = HWBrasSecurityProtocol
_HwBrasSbcCacRegTotalProtocol_Object = MibTableColumn
hwBrasSbcCacRegTotalProtocol = _HwBrasSbcCacRegTotalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 5, 1, 1),
    _HwBrasSbcCacRegTotalProtocol_Type()
)
hwBrasSbcCacRegTotalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegTotalProtocol.setStatus("current")


class _HwBrasSbcCacRegTotalThreshold_Type(Unsigned32):
    """Custom type hwBrasSbcCacRegTotalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_HwBrasSbcCacRegTotalThreshold_Type.__name__ = "Unsigned32"
_HwBrasSbcCacRegTotalThreshold_Object = MibTableColumn
hwBrasSbcCacRegTotalThreshold = _HwBrasSbcCacRegTotalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 5, 1, 2),
    _HwBrasSbcCacRegTotalThreshold_Type()
)
hwBrasSbcCacRegTotalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegTotalThreshold.setStatus("current")


class _HwBrasSbcCacRegTotalPercent_Type(Unsigned32):
    """Custom type hwBrasSbcCacRegTotalPercent based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_HwBrasSbcCacRegTotalPercent_Type.__name__ = "Unsigned32"
_HwBrasSbcCacRegTotalPercent_Object = MibTableColumn
hwBrasSbcCacRegTotalPercent = _HwBrasSbcCacRegTotalPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 5, 1, 3),
    _HwBrasSbcCacRegTotalPercent_Type()
)
hwBrasSbcCacRegTotalPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegTotalPercent.setStatus("current")
_HwBrasSbcCacRegTotalRowStatus_Type = RowStatus
_HwBrasSbcCacRegTotalRowStatus_Object = MibTableColumn
hwBrasSbcCacRegTotalRowStatus = _HwBrasSbcCacRegTotalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 5, 1, 4),
    _HwBrasSbcCacRegTotalRowStatus_Type()
)
hwBrasSbcCacRegTotalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegTotalRowStatus.setStatus("current")
_HwBrasSbcCacRegRateTable_Object = MibTable
hwBrasSbcCacRegRateTable = _HwBrasSbcCacRegRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcCacRegRateTable.setStatus("current")
_HwBrasSbcCacRegRateEntry_Object = MibTableRow
hwBrasSbcCacRegRateEntry = _HwBrasSbcCacRegRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 6, 1)
)
hwBrasSbcCacRegRateEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegRateProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcCacRegRateEntry.setStatus("current")
_HwBrasSbcCacRegRateProtocol_Type = HWBrasSecurityProtocol
_HwBrasSbcCacRegRateProtocol_Object = MibTableColumn
hwBrasSbcCacRegRateProtocol = _HwBrasSbcCacRegRateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 6, 1, 1),
    _HwBrasSbcCacRegRateProtocol_Type()
)
hwBrasSbcCacRegRateProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegRateProtocol.setStatus("current")


class _HwBrasSbcCacRegRateThreshold_Type(Unsigned32):
    """Custom type hwBrasSbcCacRegRateThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 600),
    )


_HwBrasSbcCacRegRateThreshold_Type.__name__ = "Unsigned32"
_HwBrasSbcCacRegRateThreshold_Object = MibTableColumn
hwBrasSbcCacRegRateThreshold = _HwBrasSbcCacRegRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 6, 1, 2),
    _HwBrasSbcCacRegRateThreshold_Type()
)
hwBrasSbcCacRegRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegRateThreshold.setStatus("current")


class _HwBrasSbcCacRegRatePercent_Type(Unsigned32):
    """Custom type hwBrasSbcCacRegRatePercent based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_HwBrasSbcCacRegRatePercent_Type.__name__ = "Unsigned32"
_HwBrasSbcCacRegRatePercent_Object = MibTableColumn
hwBrasSbcCacRegRatePercent = _HwBrasSbcCacRegRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 6, 1, 3),
    _HwBrasSbcCacRegRatePercent_Type()
)
hwBrasSbcCacRegRatePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegRatePercent.setStatus("current")
_HwBrasSbcCacRegRateRowStatus_Type = RowStatus
_HwBrasSbcCacRegRateRowStatus_Object = MibTableColumn
hwBrasSbcCacRegRateRowStatus = _HwBrasSbcCacRegRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 6, 1, 4),
    _HwBrasSbcCacRegRateRowStatus_Type()
)
hwBrasSbcCacRegRateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcCacRegRateRowStatus.setStatus("current")
_HwBrasSbcIPCarBandwidthTable_Object = MibTable
hwBrasSbcIPCarBandwidthTable = _HwBrasSbcIPCarBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hwBrasSbcIPCarBandwidthTable.setStatus("current")
_HwBrasSbcIPCarBandwidthEntry_Object = MibTableRow
hwBrasSbcIPCarBandwidthEntry = _HwBrasSbcIPCarBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 7, 1)
)
hwBrasSbcIPCarBandwidthEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIPCarBWVpn"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIPCarBWAddress"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIPCarBandwidthEntry.setStatus("current")


class _HwBrasSbcIPCarBWVpn_Type(Unsigned32):
    """Custom type hwBrasSbcIPCarBWVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwBrasSbcIPCarBWVpn_Type.__name__ = "Unsigned32"
_HwBrasSbcIPCarBWVpn_Object = MibTableColumn
hwBrasSbcIPCarBWVpn = _HwBrasSbcIPCarBWVpn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 7, 1, 1),
    _HwBrasSbcIPCarBWVpn_Type()
)
hwBrasSbcIPCarBWVpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIPCarBWVpn.setStatus("current")
_HwBrasSbcIPCarBWAddress_Type = IpAddress
_HwBrasSbcIPCarBWAddress_Object = MibTableColumn
hwBrasSbcIPCarBWAddress = _HwBrasSbcIPCarBWAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 7, 1, 2),
    _HwBrasSbcIPCarBWAddress_Type()
)
hwBrasSbcIPCarBWAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIPCarBWAddress.setStatus("current")


class _HwBrasSbcIPCarBWValue_Type(Unsigned32):
    """Custom type hwBrasSbcIPCarBWValue based on Unsigned32"""
    defaultValue = 1000000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000000),
    )


_HwBrasSbcIPCarBWValue_Type.__name__ = "Unsigned32"
_HwBrasSbcIPCarBWValue_Object = MibTableColumn
hwBrasSbcIPCarBWValue = _HwBrasSbcIPCarBWValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 7, 1, 3),
    _HwBrasSbcIPCarBWValue_Type()
)
hwBrasSbcIPCarBWValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIPCarBWValue.setStatus("current")
_HwBrasSbcIPCarBWRowStatus_Type = RowStatus
_HwBrasSbcIPCarBWRowStatus_Object = MibTableColumn
hwBrasSbcIPCarBWRowStatus = _HwBrasSbcIPCarBWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 5, 2, 7, 1, 4),
    _HwBrasSbcIPCarBWRowStatus_Type()
)
hwBrasSbcIPCarBWRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIPCarBWRowStatus.setStatus("current")
_HwBrasSbcUdpTunnel_ObjectIdentity = ObjectIdentity
hwBrasSbcUdpTunnel = _HwBrasSbcUdpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6)
)
_HwBrasSbcUdpTunnelLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcUdpTunnelLeaves = _HwBrasSbcUdpTunnelLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 1)
)


class _HwBrasSbcUdpTunnelEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcUdpTunnelEnable based on HWBrasEnabledStatus"""


_HwBrasSbcUdpTunnelEnable_Object = MibScalar
hwBrasSbcUdpTunnelEnable = _HwBrasSbcUdpTunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 1, 1),
    _HwBrasSbcUdpTunnelEnable_Type()
)
hwBrasSbcUdpTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelEnable.setStatus("current")


class _HwBrasSbcUdpTunnelType_Type(Integer32):
    """Custom type hwBrasSbcUdpTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 3),
          ("notype", 1),
          ("server", 2))
    )


_HwBrasSbcUdpTunnelType_Type.__name__ = "Integer32"
_HwBrasSbcUdpTunnelType_Object = MibScalar
hwBrasSbcUdpTunnelType = _HwBrasSbcUdpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 1, 2),
    _HwBrasSbcUdpTunnelType_Type()
)
hwBrasSbcUdpTunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelType.setStatus("current")
_HwBrasSbcUdpTunnelSctpAddr_Type = IpAddress
_HwBrasSbcUdpTunnelSctpAddr_Object = MibScalar
hwBrasSbcUdpTunnelSctpAddr = _HwBrasSbcUdpTunnelSctpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 1, 3),
    _HwBrasSbcUdpTunnelSctpAddr_Type()
)
hwBrasSbcUdpTunnelSctpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelSctpAddr.setStatus("current")


class _HwBrasSbcUdpTunnelTunnelTimer_Type(Unsigned32):
    """Custom type hwBrasSbcUdpTunnelTunnelTimer based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcUdpTunnelTunnelTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcUdpTunnelTunnelTimer_Object = MibScalar
hwBrasSbcUdpTunnelTunnelTimer = _HwBrasSbcUdpTunnelTunnelTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 1, 4),
    _HwBrasSbcUdpTunnelTunnelTimer_Type()
)
hwBrasSbcUdpTunnelTunnelTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelTunnelTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelTunnelTimer.setUnits("seconds")


class _HwBrasSbcUdpTunnelTransportTimer_Type(Unsigned32):
    """Custom type hwBrasSbcUdpTunnelTransportTimer based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcUdpTunnelTransportTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcUdpTunnelTransportTimer_Object = MibScalar
hwBrasSbcUdpTunnelTransportTimer = _HwBrasSbcUdpTunnelTransportTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 1, 5),
    _HwBrasSbcUdpTunnelTransportTimer_Type()
)
hwBrasSbcUdpTunnelTransportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelTransportTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelTransportTimer.setUnits("seconds")
_HwBrasSbcUdpTunnelTables_ObjectIdentity = ObjectIdentity
hwBrasSbcUdpTunnelTables = _HwBrasSbcUdpTunnelTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2)
)
_HwBrasSbcUdpTunnelPoolTable_Object = MibTable
hwBrasSbcUdpTunnelPoolTable = _HwBrasSbcUdpTunnelPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPoolTable.setStatus("current")
_HwBrasSbcUdpTunnelPoolEntry_Object = MibTableRow
hwBrasSbcUdpTunnelPoolEntry = _HwBrasSbcUdpTunnelPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 1, 1)
)
hwBrasSbcUdpTunnelPoolEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPoolIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPoolEntry.setStatus("current")


class _HwBrasSbcUdpTunnelPoolIndex_Type(Unsigned32):
    """Custom type hwBrasSbcUdpTunnelPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwBrasSbcUdpTunnelPoolIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcUdpTunnelPoolIndex_Object = MibTableColumn
hwBrasSbcUdpTunnelPoolIndex = _HwBrasSbcUdpTunnelPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 1, 1, 1),
    _HwBrasSbcUdpTunnelPoolIndex_Type()
)
hwBrasSbcUdpTunnelPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPoolIndex.setStatus("current")


class _HwBrasSbcUdpTunnelPoolStartIP_Type(IpAddress):
    """Custom type hwBrasSbcUdpTunnelPoolStartIP based on IpAddress"""
    defaultHexValue = "7FA8B501"


_HwBrasSbcUdpTunnelPoolStartIP_Object = MibTableColumn
hwBrasSbcUdpTunnelPoolStartIP = _HwBrasSbcUdpTunnelPoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 1, 1, 2),
    _HwBrasSbcUdpTunnelPoolStartIP_Type()
)
hwBrasSbcUdpTunnelPoolStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPoolStartIP.setStatus("current")


class _HwBrasSbcUdpTunnelPoolEndIP_Type(IpAddress):
    """Custom type hwBrasSbcUdpTunnelPoolEndIP based on IpAddress"""
    defaultHexValue = "7FA8EF98"


_HwBrasSbcUdpTunnelPoolEndIP_Object = MibTableColumn
hwBrasSbcUdpTunnelPoolEndIP = _HwBrasSbcUdpTunnelPoolEndIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 1, 1, 3),
    _HwBrasSbcUdpTunnelPoolEndIP_Type()
)
hwBrasSbcUdpTunnelPoolEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPoolEndIP.setStatus("current")
_HwBrasSbcUdpTunnelPoolRowStatus_Type = RowStatus
_HwBrasSbcUdpTunnelPoolRowStatus_Object = MibTableColumn
hwBrasSbcUdpTunnelPoolRowStatus = _HwBrasSbcUdpTunnelPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 1, 1, 4),
    _HwBrasSbcUdpTunnelPoolRowStatus_Type()
)
hwBrasSbcUdpTunnelPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPoolRowStatus.setStatus("current")
_HwBrasSbcUdpTunnelPortTable_Object = MibTable
hwBrasSbcUdpTunnelPortTable = _HwBrasSbcUdpTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPortTable.setStatus("current")
_HwBrasSbcUdpTunnelPortEntry_Object = MibTableRow
hwBrasSbcUdpTunnelPortEntry = _HwBrasSbcUdpTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 2, 1)
)
hwBrasSbcUdpTunnelPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPortPort"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPortEntry.setStatus("current")


class _HwBrasSbcUdpTunnelPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcUdpTunnelPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_HwBrasSbcUdpTunnelPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcUdpTunnelPortProtocol_Object = MibTableColumn
hwBrasSbcUdpTunnelPortProtocol = _HwBrasSbcUdpTunnelPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 2, 1, 1),
    _HwBrasSbcUdpTunnelPortProtocol_Type()
)
hwBrasSbcUdpTunnelPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPortProtocol.setStatus("current")


class _HwBrasSbcUdpTunnelPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcUdpTunnelPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcUdpTunnelPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcUdpTunnelPortPort_Object = MibTableColumn
hwBrasSbcUdpTunnelPortPort = _HwBrasSbcUdpTunnelPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 2, 1, 2),
    _HwBrasSbcUdpTunnelPortPort_Type()
)
hwBrasSbcUdpTunnelPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPortPort.setStatus("current")
_HwBrasSbcUdpTunnelPortRowStatus_Type = RowStatus
_HwBrasSbcUdpTunnelPortRowStatus_Object = MibTableColumn
hwBrasSbcUdpTunnelPortRowStatus = _HwBrasSbcUdpTunnelPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 2, 1, 3),
    _HwBrasSbcUdpTunnelPortRowStatus_Type()
)
hwBrasSbcUdpTunnelPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelPortRowStatus.setStatus("current")
_HwBrasSbcUdpTunnelIfPortTable_Object = MibTable
hwBrasSbcUdpTunnelIfPortTable = _HwBrasSbcUdpTunnelIfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelIfPortTable.setStatus("current")
_HwBrasSbcUdpTunnelIfPortEntry_Object = MibTableRow
hwBrasSbcUdpTunnelIfPortEntry = _HwBrasSbcUdpTunnelIfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 3, 1)
)
hwBrasSbcUdpTunnelIfPortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelIfPortAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelIfPortPort"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelIfPortEntry.setStatus("current")
_HwBrasSbcUdpTunnelIfPortAddr_Type = IpAddress
_HwBrasSbcUdpTunnelIfPortAddr_Object = MibTableColumn
hwBrasSbcUdpTunnelIfPortAddr = _HwBrasSbcUdpTunnelIfPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 3, 1, 2),
    _HwBrasSbcUdpTunnelIfPortAddr_Type()
)
hwBrasSbcUdpTunnelIfPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelIfPortAddr.setStatus("current")


class _HwBrasSbcUdpTunnelIfPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcUdpTunnelIfPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_HwBrasSbcUdpTunnelIfPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcUdpTunnelIfPortPort_Object = MibTableColumn
hwBrasSbcUdpTunnelIfPortPort = _HwBrasSbcUdpTunnelIfPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 3, 1, 3),
    _HwBrasSbcUdpTunnelIfPortPort_Type()
)
hwBrasSbcUdpTunnelIfPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelIfPortPort.setStatus("current")
_HwBrasSbcUdpTunnelIfPortRowStatus_Type = RowStatus
_HwBrasSbcUdpTunnelIfPortRowStatus_Object = MibTableColumn
hwBrasSbcUdpTunnelIfPortRowStatus = _HwBrasSbcUdpTunnelIfPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 6, 2, 3, 1, 4),
    _HwBrasSbcUdpTunnelIfPortRowStatus_Type()
)
hwBrasSbcUdpTunnelIfPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUdpTunnelIfPortRowStatus.setStatus("current")
_HwBrasSbcIms_ObjectIdentity = ObjectIdentity
hwBrasSbcIms = _HwBrasSbcIms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7)
)
_HwBrasSbcImsLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcImsLeaves = _HwBrasSbcImsLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1)
)


class _HwBrasSbcImsQosEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsQosEnable based on HWBrasEnabledStatus"""


_HwBrasSbcImsQosEnable_Object = MibScalar
hwBrasSbcImsQosEnable = _HwBrasSbcImsQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 1),
    _HwBrasSbcImsQosEnable_Type()
)
hwBrasSbcImsQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsQosEnable.setStatus("current")


class _HwBrasSbcImsMediaProxyEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsMediaProxyEnable based on HWBrasEnabledStatus"""


_HwBrasSbcImsMediaProxyEnable_Object = MibScalar
hwBrasSbcImsMediaProxyEnable = _HwBrasSbcImsMediaProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 2),
    _HwBrasSbcImsMediaProxyEnable_Type()
)
hwBrasSbcImsMediaProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMediaProxyEnable.setStatus("current")


class _HwBrasSbcImsQosLogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsQosLogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcImsQosLogEnable_Object = MibScalar
hwBrasSbcImsQosLogEnable = _HwBrasSbcImsQosLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 3),
    _HwBrasSbcImsQosLogEnable_Type()
)
hwBrasSbcImsQosLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsQosLogEnable.setStatus("current")


class _HwBrasSbcImsMediaProxyLogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsMediaProxyLogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcImsMediaProxyLogEnable_Object = MibScalar
hwBrasSbcImsMediaProxyLogEnable = _HwBrasSbcImsMediaProxyLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 4),
    _HwBrasSbcImsMediaProxyLogEnable_Type()
)
hwBrasSbcImsMediaProxyLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMediaProxyLogEnable.setStatus("current")


class _HwBrasSbcImsMGStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsMGStatus based on HWBrasEnabledStatus"""


_HwBrasSbcImsMGStatus_Object = MibScalar
hwBrasSbcImsMGStatus = _HwBrasSbcImsMGStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 5),
    _HwBrasSbcImsMGStatus_Type()
)
hwBrasSbcImsMGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGStatus.setStatus("current")


class _HwBrasSbcImsMGConnectTimer_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGConnectTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3600000),
    )


_HwBrasSbcImsMGConnectTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGConnectTimer_Object = MibScalar
hwBrasSbcImsMGConnectTimer = _HwBrasSbcImsMGConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 6),
    _HwBrasSbcImsMGConnectTimer_Type()
)
hwBrasSbcImsMGConnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGConnectTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGConnectTimer.setUnits("ms")


class _HwBrasSbcImsMGAgingTimer_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGAgingTimer based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_HwBrasSbcImsMGAgingTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGAgingTimer_Object = MibScalar
hwBrasSbcImsMGAgingTimer = _HwBrasSbcImsMGAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 7),
    _HwBrasSbcImsMGAgingTimer_Type()
)
hwBrasSbcImsMGAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGAgingTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGAgingTimer.setUnits("s")


class _HwBrasSbcImsMGCallSessionTimer_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGCallSessionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14400),
    )


_HwBrasSbcImsMGCallSessionTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGCallSessionTimer_Object = MibScalar
hwBrasSbcImsMGCallSessionTimer = _HwBrasSbcImsMGCallSessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 8),
    _HwBrasSbcImsMGCallSessionTimer_Type()
)
hwBrasSbcImsMGCallSessionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGCallSessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGCallSessionTimer.setUnits("m")


class _HwBrasSbcSctpStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSctpStatus based on HWBrasEnabledStatus"""


_HwBrasSbcSctpStatus_Object = MibScalar
hwBrasSbcSctpStatus = _HwBrasSbcSctpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 9),
    _HwBrasSbcSctpStatus_Type()
)
hwBrasSbcSctpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSctpStatus.setStatus("current")


class _HwBrasSbcIdlecutRtcpTimer_Type(Unsigned32):
    """Custom type hwBrasSbcIdlecutRtcpTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwBrasSbcIdlecutRtcpTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcIdlecutRtcpTimer_Object = MibScalar
hwBrasSbcIdlecutRtcpTimer = _HwBrasSbcIdlecutRtcpTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 10),
    _HwBrasSbcIdlecutRtcpTimer_Type()
)
hwBrasSbcIdlecutRtcpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIdlecutRtcpTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcIdlecutRtcpTimer.setUnits("s")


class _HwBrasSbcIdlecutRtpTimer_Type(Unsigned32):
    """Custom type hwBrasSbcIdlecutRtpTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwBrasSbcIdlecutRtpTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcIdlecutRtpTimer_Object = MibScalar
hwBrasSbcIdlecutRtpTimer = _HwBrasSbcIdlecutRtpTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 11),
    _HwBrasSbcIdlecutRtpTimer_Type()
)
hwBrasSbcIdlecutRtpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIdlecutRtpTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcIdlecutRtpTimer.setUnits("s")


class _HwBrasSbcMediaDetectStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMediaDetectStatus based on HWBrasEnabledStatus"""


_HwBrasSbcMediaDetectStatus_Object = MibScalar
hwBrasSbcMediaDetectStatus = _HwBrasSbcMediaDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 12),
    _HwBrasSbcMediaDetectStatus_Type()
)
hwBrasSbcMediaDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaDetectStatus.setStatus("current")


class _HwBrasSbcMediaOnewayStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMediaOnewayStatus based on HWBrasEnabledStatus"""


_HwBrasSbcMediaOnewayStatus_Object = MibScalar
hwBrasSbcMediaOnewayStatus = _HwBrasSbcMediaOnewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 13),
    _HwBrasSbcMediaOnewayStatus_Type()
)
hwBrasSbcMediaOnewayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMediaOnewayStatus.setStatus("current")


class _HwBrasSbcImsMgLogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsMgLogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcImsMgLogEnable_Object = MibScalar
hwBrasSbcImsMgLogEnable = _HwBrasSbcImsMgLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 14),
    _HwBrasSbcImsMgLogEnable_Type()
)
hwBrasSbcImsMgLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMgLogEnable.setStatus("current")


class _HwBrasSbcImsStatisticsEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsStatisticsEnable based on HWBrasEnabledStatus"""


_HwBrasSbcImsStatisticsEnable_Object = MibScalar
hwBrasSbcImsStatisticsEnable = _HwBrasSbcImsStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 15),
    _HwBrasSbcImsStatisticsEnable_Type()
)
hwBrasSbcImsStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsStatisticsEnable.setStatus("current")


class _HwBrasSbcTimerMediaAging_Type(Unsigned32):
    """Custom type hwBrasSbcTimerMediaAging based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwBrasSbcTimerMediaAging_Type.__name__ = "Unsigned32"
_HwBrasSbcTimerMediaAging_Object = MibScalar
hwBrasSbcTimerMediaAging = _HwBrasSbcTimerMediaAging_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 1, 16),
    _HwBrasSbcTimerMediaAging_Type()
)
hwBrasSbcTimerMediaAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcTimerMediaAging.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcTimerMediaAging.setUnits("s")
_HwBrasSbcImsTables_ObjectIdentity = ObjectIdentity
hwBrasSbcImsTables = _HwBrasSbcImsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2)
)
_HwBrasSbcImsConnectTable_Object = MibTable
hwBrasSbcImsConnectTable = _HwBrasSbcImsConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectTable.setStatus("current")
_HwBrasSbcImsConnectEntry_Object = MibTableRow
hwBrasSbcImsConnectEntry = _HwBrasSbcImsConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1)
)
hwBrasSbcImsConnectEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectEntry.setStatus("current")


class _HwBrasSbcImsConnectIndex_Type(Unsigned32):
    """Custom type hwBrasSbcImsConnectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HwBrasSbcImsConnectIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcImsConnectIndex_Object = MibTableColumn
hwBrasSbcImsConnectIndex = _HwBrasSbcImsConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 1),
    _HwBrasSbcImsConnectIndex_Type()
)
hwBrasSbcImsConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectIndex.setStatus("current")


class _HwBrasSbcImsConnectPepID_Type(DisplayString):
    """Custom type hwBrasSbcImsConnectPepID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBrasSbcImsConnectPepID_Type.__name__ = "DisplayString"
_HwBrasSbcImsConnectPepID_Object = MibTableColumn
hwBrasSbcImsConnectPepID = _HwBrasSbcImsConnectPepID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 11),
    _HwBrasSbcImsConnectPepID_Type()
)
hwBrasSbcImsConnectPepID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectPepID.setStatus("current")


class _HwBrasSbcImsConnectCliType_Type(Integer32):
    """Custom type hwBrasSbcImsConnectCliType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("brasSbci", 2),
          ("goi", 3),
          ("unknown", 1))
    )


_HwBrasSbcImsConnectCliType_Type.__name__ = "Integer32"
_HwBrasSbcImsConnectCliType_Object = MibTableColumn
hwBrasSbcImsConnectCliType = _HwBrasSbcImsConnectCliType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 12),
    _HwBrasSbcImsConnectCliType_Type()
)
hwBrasSbcImsConnectCliType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectCliType.setStatus("current")
_HwBrasSbcImsConnectCliIP_Type = IpAddress
_HwBrasSbcImsConnectCliIP_Object = MibTableColumn
hwBrasSbcImsConnectCliIP = _HwBrasSbcImsConnectCliIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 13),
    _HwBrasSbcImsConnectCliIP_Type()
)
hwBrasSbcImsConnectCliIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectCliIP.setStatus("current")


class _HwBrasSbcImsConnectCliPort_Type(Unsigned32):
    """Custom type hwBrasSbcImsConnectCliPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_HwBrasSbcImsConnectCliPort_Type.__name__ = "Unsigned32"
_HwBrasSbcImsConnectCliPort_Object = MibTableColumn
hwBrasSbcImsConnectCliPort = _HwBrasSbcImsConnectCliPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 14),
    _HwBrasSbcImsConnectCliPort_Type()
)
hwBrasSbcImsConnectCliPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectCliPort.setStatus("current")
_HwBrasSbcImsConnectServIP_Type = IpAddress
_HwBrasSbcImsConnectServIP_Object = MibTableColumn
hwBrasSbcImsConnectServIP = _HwBrasSbcImsConnectServIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 15),
    _HwBrasSbcImsConnectServIP_Type()
)
hwBrasSbcImsConnectServIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectServIP.setStatus("current")


class _HwBrasSbcImsConnectServPort_Type(Unsigned32):
    """Custom type hwBrasSbcImsConnectServPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_HwBrasSbcImsConnectServPort_Type.__name__ = "Unsigned32"
_HwBrasSbcImsConnectServPort_Object = MibTableColumn
hwBrasSbcImsConnectServPort = _HwBrasSbcImsConnectServPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 16),
    _HwBrasSbcImsConnectServPort_Type()
)
hwBrasSbcImsConnectServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectServPort.setStatus("current")
_HwBrasSbcImsConnectRowStatus_Type = RowStatus
_HwBrasSbcImsConnectRowStatus_Object = MibTableColumn
hwBrasSbcImsConnectRowStatus = _HwBrasSbcImsConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 1, 1, 51),
    _HwBrasSbcImsConnectRowStatus_Type()
)
hwBrasSbcImsConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsConnectRowStatus.setStatus("current")
_HwBrasSbcImsBandTable_Object = MibTable
hwBrasSbcImsBandTable = _HwBrasSbcImsBandTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcImsBandTable.setStatus("current")
_HwBrasSbcImsBandEntry_Object = MibTableRow
hwBrasSbcImsBandEntry = _HwBrasSbcImsBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1)
)
hwBrasSbcImsBandEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsBandIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcImsBandEntry.setStatus("current")


class _HwBrasSbcImsBandIndex_Type(Unsigned32):
    """Custom type hwBrasSbcImsBandIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwBrasSbcImsBandIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcImsBandIndex_Object = MibTableColumn
hwBrasSbcImsBandIndex = _HwBrasSbcImsBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1, 1),
    _HwBrasSbcImsBandIndex_Type()
)
hwBrasSbcImsBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsBandIndex.setStatus("current")
_HwBrasSbcImsBandIfIndex_Type = Unsigned32
_HwBrasSbcImsBandIfIndex_Object = MibTableColumn
hwBrasSbcImsBandIfIndex = _HwBrasSbcImsBandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1, 11),
    _HwBrasSbcImsBandIfIndex_Type()
)
hwBrasSbcImsBandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcImsBandIfIndex.setStatus("current")
_HwBrasSbcImsBandIfName_Type = DisplayString
_HwBrasSbcImsBandIfName_Object = MibTableColumn
hwBrasSbcImsBandIfName = _HwBrasSbcImsBandIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1, 12),
    _HwBrasSbcImsBandIfName_Type()
)
hwBrasSbcImsBandIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcImsBandIfName.setStatus("current")


class _HwBrasSbcImsBandIfType_Type(Integer32):
    """Custom type hwBrasSbcImsBandIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fe", 1),
          ("ge", 2))
    )


_HwBrasSbcImsBandIfType_Type.__name__ = "Integer32"
_HwBrasSbcImsBandIfType_Object = MibTableColumn
hwBrasSbcImsBandIfType = _HwBrasSbcImsBandIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1, 13),
    _HwBrasSbcImsBandIfType_Type()
)
hwBrasSbcImsBandIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcImsBandIfType.setStatus("current")


class _HwBrasSbcImsBandValue_Type(Unsigned32):
    """Custom type hwBrasSbcImsBandValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwBrasSbcImsBandValue_Type.__name__ = "Unsigned32"
_HwBrasSbcImsBandValue_Object = MibTableColumn
hwBrasSbcImsBandValue = _HwBrasSbcImsBandValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1, 14),
    _HwBrasSbcImsBandValue_Type()
)
hwBrasSbcImsBandValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsBandValue.setStatus("current")
_HwBrasSbcImsBandRowStatus_Type = RowStatus
_HwBrasSbcImsBandRowStatus_Object = MibTableColumn
hwBrasSbcImsBandRowStatus = _HwBrasSbcImsBandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 2, 1, 51),
    _HwBrasSbcImsBandRowStatus_Type()
)
hwBrasSbcImsBandRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsBandRowStatus.setStatus("current")
_HwBrasSbcImsActiveTable_Object = MibTable
hwBrasSbcImsActiveTable = _HwBrasSbcImsActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcImsActiveTable.setStatus("current")
_HwBrasSbcImsActiveEntry_Object = MibTableRow
hwBrasSbcImsActiveEntry = _HwBrasSbcImsActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 3, 1)
)
hwBrasSbcImsActiveEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsActiveConnectId"),
)
if mibBuilder.loadTexts:
    hwBrasSbcImsActiveEntry.setStatus("current")


class _HwBrasSbcImsActiveConnectId_Type(Unsigned32):
    """Custom type hwBrasSbcImsActiveConnectId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HwBrasSbcImsActiveConnectId_Type.__name__ = "Unsigned32"
_HwBrasSbcImsActiveConnectId_Object = MibTableColumn
hwBrasSbcImsActiveConnectId = _HwBrasSbcImsActiveConnectId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 3, 1, 1),
    _HwBrasSbcImsActiveConnectId_Type()
)
hwBrasSbcImsActiveConnectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsActiveConnectId.setStatus("current")


class _HwBrasSbcImsActiveStatus_Type(Integer32):
    """Custom type hwBrasSbcImsActiveStatus based on Integer32"""
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
        *(("active", 2),
          ("online", 3),
          ("sleep", 1))
    )


_HwBrasSbcImsActiveStatus_Type.__name__ = "Integer32"
_HwBrasSbcImsActiveStatus_Object = MibTableColumn
hwBrasSbcImsActiveStatus = _HwBrasSbcImsActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 3, 1, 11),
    _HwBrasSbcImsActiveStatus_Type()
)
hwBrasSbcImsActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsActiveStatus.setStatus("current")
_HwBrasSbcImsActiveRowStatus_Type = RowStatus
_HwBrasSbcImsActiveRowStatus_Object = MibTableColumn
hwBrasSbcImsActiveRowStatus = _HwBrasSbcImsActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 3, 1, 51),
    _HwBrasSbcImsActiveRowStatus_Type()
)
hwBrasSbcImsActiveRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsActiveRowStatus.setStatus("current")
_HwBrasSbcImsMGTable_Object = MibTable
hwBrasSbcImsMGTable = _HwBrasSbcImsMGTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcImsMGTable.setStatus("current")
_HwBrasSbcImsMGEntry_Object = MibTableRow
hwBrasSbcImsMGEntry = _HwBrasSbcImsMGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1)
)
hwBrasSbcImsMGEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcImsMGEntry.setStatus("current")


class _HwBrasSbcImsMGIndex_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_HwBrasSbcImsMGIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGIndex_Object = MibTableColumn
hwBrasSbcImsMGIndex = _HwBrasSbcImsMGIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 1),
    _HwBrasSbcImsMGIndex_Type()
)
hwBrasSbcImsMGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIndex.setStatus("current")


class _HwBrasSbcImsMGDescription_Type(DisplayString):
    """Custom type hwBrasSbcImsMGDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcImsMGDescription_Type.__name__ = "DisplayString"
_HwBrasSbcImsMGDescription_Object = MibTableColumn
hwBrasSbcImsMGDescription = _HwBrasSbcImsMGDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 11),
    _HwBrasSbcImsMGDescription_Type()
)
hwBrasSbcImsMGDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDescription.setStatus("current")


class _HwBrasSbcImsMGTableStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcImsMGTableStatus based on HWBrasEnabledStatus"""


_HwBrasSbcImsMGTableStatus_Object = MibTableColumn
hwBrasSbcImsMGTableStatus = _HwBrasSbcImsMGTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 12),
    _HwBrasSbcImsMGTableStatus_Type()
)
hwBrasSbcImsMGTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGTableStatus.setStatus("current")


class _HwBrasSbcImsMGProtocol_Type(Integer32):
    """Custom type hwBrasSbcImsMGProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sctp", 1),
          ("tcp", 3),
          ("udp", 2))
    )


_HwBrasSbcImsMGProtocol_Type.__name__ = "Integer32"
_HwBrasSbcImsMGProtocol_Object = MibTableColumn
hwBrasSbcImsMGProtocol = _HwBrasSbcImsMGProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 13),
    _HwBrasSbcImsMGProtocol_Type()
)
hwBrasSbcImsMGProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGProtocol.setStatus("current")


class _HwBrasSbcImsMGMidString_Type(DisplayString):
    """Custom type hwBrasSbcImsMGMidString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwBrasSbcImsMGMidString_Type.__name__ = "DisplayString"
_HwBrasSbcImsMGMidString_Object = MibTableColumn
hwBrasSbcImsMGMidString = _HwBrasSbcImsMGMidString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 14),
    _HwBrasSbcImsMGMidString_Type()
)
hwBrasSbcImsMGMidString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGMidString.setStatus("current")


class _HwBrasSbcImsMGInstanceName_Type(DisplayString):
    """Custom type hwBrasSbcImsMGInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBrasSbcImsMGInstanceName_Type.__name__ = "DisplayString"
_HwBrasSbcImsMGInstanceName_Object = MibTableColumn
hwBrasSbcImsMGInstanceName = _HwBrasSbcImsMGInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 15),
    _HwBrasSbcImsMGInstanceName_Type()
)
hwBrasSbcImsMGInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGInstanceName.setStatus("current")
_HwBrasSbcImsMGRowStatus_Type = RowStatus
_HwBrasSbcImsMGRowStatus_Object = MibTableColumn
hwBrasSbcImsMGRowStatus = _HwBrasSbcImsMGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 4, 1, 51),
    _HwBrasSbcImsMGRowStatus_Type()
)
hwBrasSbcImsMGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGRowStatus.setStatus("current")
_HwBrasSbcImsMGIPTable_Object = MibTable
hwBrasSbcImsMGIPTable = _HwBrasSbcImsMGIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPTable.setStatus("current")
_HwBrasSbcImsMGIPEntry_Object = MibTableRow
hwBrasSbcImsMGIPEntry = _HwBrasSbcImsMGIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1)
)
hwBrasSbcImsMGIPEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPType"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPSN"),
)
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPEntry.setStatus("current")


class _HwBrasSbcImsMGIPType_Type(Integer32):
    """Custom type hwBrasSbcImsMGIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mg", 1),
          ("mgc", 2))
    )


_HwBrasSbcImsMGIPType_Type.__name__ = "Integer32"
_HwBrasSbcImsMGIPType_Object = MibTableColumn
hwBrasSbcImsMGIPType = _HwBrasSbcImsMGIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 2),
    _HwBrasSbcImsMGIPType_Type()
)
hwBrasSbcImsMGIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPType.setStatus("current")


class _HwBrasSbcImsMGIPSN_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGIPSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwBrasSbcImsMGIPSN_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGIPSN_Object = MibTableColumn
hwBrasSbcImsMGIPSN = _HwBrasSbcImsMGIPSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 3),
    _HwBrasSbcImsMGIPSN_Type()
)
hwBrasSbcImsMGIPSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPSN.setStatus("current")


class _HwBrasSbcImsMGIPVersion_Type(Integer32):
    """Custom type hwBrasSbcImsMGIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 4),
          ("ipv6", 6))
    )


_HwBrasSbcImsMGIPVersion_Type.__name__ = "Integer32"
_HwBrasSbcImsMGIPVersion_Object = MibTableColumn
hwBrasSbcImsMGIPVersion = _HwBrasSbcImsMGIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 11),
    _HwBrasSbcImsMGIPVersion_Type()
)
hwBrasSbcImsMGIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPVersion.setStatus("current")


class _HwBrasSbcImsMGIPAddr_Type(DisplayString):
    """Custom type hwBrasSbcImsMGIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcImsMGIPAddr_Type.__name__ = "DisplayString"
_HwBrasSbcImsMGIPAddr_Object = MibTableColumn
hwBrasSbcImsMGIPAddr = _HwBrasSbcImsMGIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 12),
    _HwBrasSbcImsMGIPAddr_Type()
)
hwBrasSbcImsMGIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPAddr.setStatus("current")


class _HwBrasSbcImsMGIPPort_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGIPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwBrasSbcImsMGIPPort_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGIPPort_Object = MibTableColumn
hwBrasSbcImsMGIPPort = _HwBrasSbcImsMGIPPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 13),
    _HwBrasSbcImsMGIPPort_Type()
)
hwBrasSbcImsMGIPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPPort.setStatus("current")


class _HwBrasSbcImsMGIPInterface_Type(OctetString):
    """Custom type hwBrasSbcImsMGIPInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwBrasSbcImsMGIPInterface_Type.__name__ = "OctetString"
_HwBrasSbcImsMGIPInterface_Object = MibTableColumn
hwBrasSbcImsMGIPInterface = _HwBrasSbcImsMGIPInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 15),
    _HwBrasSbcImsMGIPInterface_Type()
)
hwBrasSbcImsMGIPInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPInterface.setStatus("current")
_HwBrasSbcImsMGIPRowStatus_Type = RowStatus
_HwBrasSbcImsMGIPRowStatus_Object = MibTableColumn
hwBrasSbcImsMGIPRowStatus = _HwBrasSbcImsMGIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 5, 1, 51),
    _HwBrasSbcImsMGIPRowStatus_Type()
)
hwBrasSbcImsMGIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGIPRowStatus.setStatus("current")
_HwBrasSbcImsMGDomainTable_Object = MibTable
hwBrasSbcImsMGDomainTable = _HwBrasSbcImsMGDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDomainTable.setStatus("current")
_HwBrasSbcImsMGDomainEntry_Object = MibTableRow
hwBrasSbcImsMGDomainEntry = _HwBrasSbcImsMGDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 6, 1)
)
hwBrasSbcImsMGDomainEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGDomainType"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGDomainName"),
)
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDomainEntry.setStatus("current")


class _HwBrasSbcImsMGDomainType_Type(Integer32):
    """Custom type hwBrasSbcImsMGDomainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inner", 1),
          ("outter", 2))
    )


_HwBrasSbcImsMGDomainType_Type.__name__ = "Integer32"
_HwBrasSbcImsMGDomainType_Object = MibTableColumn
hwBrasSbcImsMGDomainType = _HwBrasSbcImsMGDomainType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 6, 1, 2),
    _HwBrasSbcImsMGDomainType_Type()
)
hwBrasSbcImsMGDomainType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDomainType.setStatus("current")


class _HwBrasSbcImsMGDomainName_Type(DisplayString):
    """Custom type hwBrasSbcImsMGDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBrasSbcImsMGDomainName_Type.__name__ = "DisplayString"
_HwBrasSbcImsMGDomainName_Object = MibTableColumn
hwBrasSbcImsMGDomainName = _HwBrasSbcImsMGDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 6, 1, 3),
    _HwBrasSbcImsMGDomainName_Type()
)
hwBrasSbcImsMGDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDomainName.setStatus("current")


class _HwBrasSbcImsMGDomainMapIndex_Type(Unsigned32):
    """Custom type hwBrasSbcImsMGDomainMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2501, 2999),
    )


_HwBrasSbcImsMGDomainMapIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcImsMGDomainMapIndex_Object = MibTableColumn
hwBrasSbcImsMGDomainMapIndex = _HwBrasSbcImsMGDomainMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 6, 1, 11),
    _HwBrasSbcImsMGDomainMapIndex_Type()
)
hwBrasSbcImsMGDomainMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDomainMapIndex.setStatus("current")
_HwBrasSbcImsMGDomainRowStatus_Type = RowStatus
_HwBrasSbcImsMGDomainRowStatus_Object = MibTableColumn
hwBrasSbcImsMGDomainRowStatus = _HwBrasSbcImsMGDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 7, 2, 6, 1, 51),
    _HwBrasSbcImsMGDomainRowStatus_Type()
)
hwBrasSbcImsMGDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcImsMGDomainRowStatus.setStatus("current")
_HwBrasSbcDualHoming_ObjectIdentity = ObjectIdentity
hwBrasSbcDualHoming = _HwBrasSbcDualHoming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 8)
)
_HwBrasSbcDHLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcDHLeaves = _HwBrasSbcDHLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 8, 1)
)


class _HwBrasSbcDHSIPDetectStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcDHSIPDetectStatus based on HWBrasEnabledStatus"""


_HwBrasSbcDHSIPDetectStatus_Object = MibScalar
hwBrasSbcDHSIPDetectStatus = _HwBrasSbcDHSIPDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 8, 1, 1),
    _HwBrasSbcDHSIPDetectStatus_Type()
)
hwBrasSbcDHSIPDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDHSIPDetectStatus.setStatus("current")


class _HwBrasSbcDHSIPDetectTimer_Type(Unsigned32):
    """Custom type hwBrasSbcDHSIPDetectTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_HwBrasSbcDHSIPDetectTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcDHSIPDetectTimer_Object = MibScalar
hwBrasSbcDHSIPDetectTimer = _HwBrasSbcDHSIPDetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 8, 1, 2),
    _HwBrasSbcDHSIPDetectTimer_Type()
)
hwBrasSbcDHSIPDetectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDHSIPDetectTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcDHSIPDetectTimer.setUnits("seconds")


class _HwBrasSbcDHSIPDetectSourcePort_Type(Unsigned32):
    """Custom type hwBrasSbcDHSIPDetectSourcePort based on Unsigned32"""
    defaultValue = 5060

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 10000),
    )


_HwBrasSbcDHSIPDetectSourcePort_Type.__name__ = "Unsigned32"
_HwBrasSbcDHSIPDetectSourcePort_Object = MibScalar
hwBrasSbcDHSIPDetectSourcePort = _HwBrasSbcDHSIPDetectSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 8, 1, 3),
    _HwBrasSbcDHSIPDetectSourcePort_Type()
)
hwBrasSbcDHSIPDetectSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDHSIPDetectSourcePort.setStatus("current")


class _HwBrasSbcDHSIPDetectFailCount_Type(Unsigned32):
    """Custom type hwBrasSbcDHSIPDetectFailCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBrasSbcDHSIPDetectFailCount_Type.__name__ = "Unsigned32"
_HwBrasSbcDHSIPDetectFailCount_Object = MibScalar
hwBrasSbcDHSIPDetectFailCount = _HwBrasSbcDHSIPDetectFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 8, 1, 4),
    _HwBrasSbcDHSIPDetectFailCount_Type()
)
hwBrasSbcDHSIPDetectFailCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcDHSIPDetectFailCount.setStatus("current")
_HwBrasSbcQoSReport_ObjectIdentity = ObjectIdentity
hwBrasSbcQoSReport = _HwBrasSbcQoSReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 9)
)
_HwBrasSbcQRLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcQRLeaves = _HwBrasSbcQRLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 9, 1)
)


class _HwBrasSbcQRStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcQRStatus based on HWBrasEnabledStatus"""


_HwBrasSbcQRStatus_Object = MibScalar
hwBrasSbcQRStatus = _HwBrasSbcQRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 9, 1, 1),
    _HwBrasSbcQRStatus_Type()
)
hwBrasSbcQRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcQRStatus.setStatus("current")


class _HwBrasSbcQRBandWidth_Type(Unsigned32):
    """Custom type hwBrasSbcQRBandWidth based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40960),
    )


_HwBrasSbcQRBandWidth_Type.__name__ = "Unsigned32"
_HwBrasSbcQRBandWidth_Object = MibScalar
hwBrasSbcQRBandWidth = _HwBrasSbcQRBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 9, 1, 2),
    _HwBrasSbcQRBandWidth_Type()
)
hwBrasSbcQRBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcQRBandWidth.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcQRBandWidth.setUnits("packetspersecond")
_HwBrasSbcQRTables_ObjectIdentity = ObjectIdentity
hwBrasSbcQRTables = _HwBrasSbcQRTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 9, 2)
)
_HwBrasSbcMediaDefend_ObjectIdentity = ObjectIdentity
hwBrasSbcMediaDefend = _HwBrasSbcMediaDefend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11)
)
_HwBrasSbcMediaDefendLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcMediaDefendLeaves = _HwBrasSbcMediaDefendLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 1)
)


class _HwBrasSbcMDStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMDStatus based on HWBrasEnabledStatus"""


_HwBrasSbcMDStatus_Object = MibScalar
hwBrasSbcMDStatus = _HwBrasSbcMDStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 1, 1),
    _HwBrasSbcMDStatus_Type()
)
hwBrasSbcMDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatus.setStatus("current")
_HwBrasSbcMediaDefendTables_ObjectIdentity = ObjectIdentity
hwBrasSbcMediaDefendTables = _HwBrasSbcMediaDefendTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2)
)
_HwBrasSbcMDLengthTable_Object = MibTable
hwBrasSbcMDLengthTable = _HwBrasSbcMDLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcMDLengthTable.setStatus("current")
_HwBrasSbcMDLengthEntry_Object = MibTableRow
hwBrasSbcMDLengthEntry = _HwBrasSbcMDLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 1, 1)
)
hwBrasSbcMDLengthEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDLengthIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMDLengthEntry.setStatus("current")


class _HwBrasSbcMDLengthIndex_Type(Integer32):
    """Custom type hwBrasSbcMDLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtcp", 2),
          ("rtp", 1))
    )


_HwBrasSbcMDLengthIndex_Type.__name__ = "Integer32"
_HwBrasSbcMDLengthIndex_Object = MibTableColumn
hwBrasSbcMDLengthIndex = _HwBrasSbcMDLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 1, 1, 1),
    _HwBrasSbcMDLengthIndex_Type()
)
hwBrasSbcMDLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMDLengthIndex.setStatus("current")


class _HwBrasSbcMDLengthMin_Type(Unsigned32):
    """Custom type hwBrasSbcMDLengthMin based on Unsigned32"""
    defaultValue = 28

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(28, 65535),
    )


_HwBrasSbcMDLengthMin_Type.__name__ = "Unsigned32"
_HwBrasSbcMDLengthMin_Object = MibTableColumn
hwBrasSbcMDLengthMin = _HwBrasSbcMDLengthMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 1, 1, 11),
    _HwBrasSbcMDLengthMin_Type()
)
hwBrasSbcMDLengthMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMDLengthMin.setStatus("current")


class _HwBrasSbcMDLengthMax_Type(Unsigned32):
    """Custom type hwBrasSbcMDLengthMax based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(28, 65535),
    )


_HwBrasSbcMDLengthMax_Type.__name__ = "Unsigned32"
_HwBrasSbcMDLengthMax_Object = MibTableColumn
hwBrasSbcMDLengthMax = _HwBrasSbcMDLengthMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 1, 1, 12),
    _HwBrasSbcMDLengthMax_Type()
)
hwBrasSbcMDLengthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMDLengthMax.setStatus("current")
_HwBrasSbcMDLengthRowStatus_Type = RowStatus
_HwBrasSbcMDLengthRowStatus_Object = MibTableColumn
hwBrasSbcMDLengthRowStatus = _HwBrasSbcMDLengthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 1, 1, 51),
    _HwBrasSbcMDLengthRowStatus_Type()
)
hwBrasSbcMDLengthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMDLengthRowStatus.setStatus("current")
_HwBrasSbcMDStatisticTable_Object = MibTable
hwBrasSbcMDStatisticTable = _HwBrasSbcMDStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticTable.setStatus("current")
_HwBrasSbcMDStatisticEntry_Object = MibTableRow
hwBrasSbcMDStatisticEntry = _HwBrasSbcMDStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1)
)
hwBrasSbcMDStatisticEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatisticIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticEntry.setStatus("current")


class _HwBrasSbcMDStatisticIndex_Type(Integer32):
    """Custom type hwBrasSbcMDStatisticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtcp", 2),
          ("rtp", 1))
    )


_HwBrasSbcMDStatisticIndex_Type.__name__ = "Integer32"
_HwBrasSbcMDStatisticIndex_Object = MibTableColumn
hwBrasSbcMDStatisticIndex = _HwBrasSbcMDStatisticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1, 1),
    _HwBrasSbcMDStatisticIndex_Type()
)
hwBrasSbcMDStatisticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticIndex.setStatus("current")
_HwBrasSbcMDStatisticMinDrop_Type = Unsigned32
_HwBrasSbcMDStatisticMinDrop_Object = MibTableColumn
hwBrasSbcMDStatisticMinDrop = _HwBrasSbcMDStatisticMinDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1, 11),
    _HwBrasSbcMDStatisticMinDrop_Type()
)
hwBrasSbcMDStatisticMinDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticMinDrop.setStatus("current")
_HwBrasSbcMDStatisticMaxDrop_Type = Unsigned32
_HwBrasSbcMDStatisticMaxDrop_Object = MibTableColumn
hwBrasSbcMDStatisticMaxDrop = _HwBrasSbcMDStatisticMaxDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1, 12),
    _HwBrasSbcMDStatisticMaxDrop_Type()
)
hwBrasSbcMDStatisticMaxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticMaxDrop.setStatus("current")
_HwBrasSbcMDStatisticFragDrop_Type = Unsigned32
_HwBrasSbcMDStatisticFragDrop_Object = MibTableColumn
hwBrasSbcMDStatisticFragDrop = _HwBrasSbcMDStatisticFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1, 13),
    _HwBrasSbcMDStatisticFragDrop_Type()
)
hwBrasSbcMDStatisticFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticFragDrop.setStatus("current")
_HwBrasSbcMDStatisticFlowDrop_Type = Unsigned32
_HwBrasSbcMDStatisticFlowDrop_Object = MibTableColumn
hwBrasSbcMDStatisticFlowDrop = _HwBrasSbcMDStatisticFlowDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1, 14),
    _HwBrasSbcMDStatisticFlowDrop_Type()
)
hwBrasSbcMDStatisticFlowDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticFlowDrop.setStatus("current")
_HwBrasSbcMDStatisticRowStatus_Type = RowStatus
_HwBrasSbcMDStatisticRowStatus_Object = MibTableColumn
hwBrasSbcMDStatisticRowStatus = _HwBrasSbcMDStatisticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 11, 2, 2, 1, 51),
    _HwBrasSbcMDStatisticRowStatus_Type()
)
hwBrasSbcMDStatisticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMDStatisticRowStatus.setStatus("current")
_HwBrasSbcSignalingNat_ObjectIdentity = ObjectIdentity
hwBrasSbcSignalingNat = _HwBrasSbcSignalingNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12)
)
_HwBrasSbcSignalingNatLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcSignalingNatLeaves = _HwBrasSbcSignalingNatLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 1)
)


class _HwBrasSbcNatSessionAgingTime_Type(Unsigned32):
    """Custom type hwBrasSbcNatSessionAgingTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40000),
    )


_HwBrasSbcNatSessionAgingTime_Type.__name__ = "Unsigned32"
_HwBrasSbcNatSessionAgingTime_Object = MibScalar
hwBrasSbcNatSessionAgingTime = _HwBrasSbcNatSessionAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 1, 1),
    _HwBrasSbcNatSessionAgingTime_Type()
)
hwBrasSbcNatSessionAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcNatSessionAgingTime.setStatus("current")
_HwBrasSbcSignalingNatTables_ObjectIdentity = ObjectIdentity
hwBrasSbcSignalingNatTables = _HwBrasSbcSignalingNatTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2)
)
_HwBrasSbcNatCfgTable_Object = MibTable
hwBrasSbcNatCfgTable = _HwBrasSbcNatCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcNatCfgTable.setStatus("current")
_HwBrasSbcNatCfgEntry_Object = MibTableRow
hwBrasSbcNatCfgEntry = _HwBrasSbcNatCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 1, 1)
)
hwBrasSbcNatCfgEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatGroupIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatVpnNameIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcNatCfgEntry.setStatus("current")


class _HwBrasSbcNatGroupIndex_Type(Unsigned32):
    """Custom type hwBrasSbcNatGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwBrasSbcNatGroupIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcNatGroupIndex_Object = MibTableColumn
hwBrasSbcNatGroupIndex = _HwBrasSbcNatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 1, 1, 1),
    _HwBrasSbcNatGroupIndex_Type()
)
hwBrasSbcNatGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcNatGroupIndex.setStatus("current")


class _HwBrasSbcNatVpnNameIndex_Type(DisplayString):
    """Custom type hwBrasSbcNatVpnNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBrasSbcNatVpnNameIndex_Type.__name__ = "DisplayString"
_HwBrasSbcNatVpnNameIndex_Object = MibTableColumn
hwBrasSbcNatVpnNameIndex = _HwBrasSbcNatVpnNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 1, 1, 2),
    _HwBrasSbcNatVpnNameIndex_Type()
)
hwBrasSbcNatVpnNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcNatVpnNameIndex.setStatus("current")


class _HwBrasSbcNatInstanceName_Type(DisplayString):
    """Custom type hwBrasSbcNatInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBrasSbcNatInstanceName_Type.__name__ = "DisplayString"
_HwBrasSbcNatInstanceName_Object = MibTableColumn
hwBrasSbcNatInstanceName = _HwBrasSbcNatInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 1, 1, 3),
    _HwBrasSbcNatInstanceName_Type()
)
hwBrasSbcNatInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcNatInstanceName.setStatus("current")
_HwBrasSbcNatCfgRowStatus_Type = RowStatus
_HwBrasSbcNatCfgRowStatus_Object = MibTableColumn
hwBrasSbcNatCfgRowStatus = _HwBrasSbcNatCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 1, 1, 51),
    _HwBrasSbcNatCfgRowStatus_Type()
)
hwBrasSbcNatCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcNatCfgRowStatus.setStatus("current")
_HwBrasSbcNatAddressGroupTable_Object = MibTable
hwBrasSbcNatAddressGroupTable = _HwBrasSbcNatAddressGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcNatAddressGroupTable.setStatus("current")
_HwBrasSbcNatAddressGroupEntry_Object = MibTableRow
hwBrasSbcNatAddressGroupEntry = _HwBrasSbcNatAddressGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1)
)
hwBrasSbcNatAddressGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwNatAddrGrpIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcNatAddressGroupEntry.setStatus("current")


class _HwNatAddrGrpIndex_Type(Unsigned32):
    """Custom type hwNatAddrGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwNatAddrGrpIndex_Type.__name__ = "Unsigned32"
_HwNatAddrGrpIndex_Object = MibTableColumn
hwNatAddrGrpIndex = _HwNatAddrGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1, 1),
    _HwNatAddrGrpIndex_Type()
)
hwNatAddrGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrGrpIndex.setStatus("current")
_HwNatAddrGrpBeginningIpAddr_Type = IpAddress
_HwNatAddrGrpBeginningIpAddr_Object = MibTableColumn
hwNatAddrGrpBeginningIpAddr = _HwNatAddrGrpBeginningIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1, 2),
    _HwNatAddrGrpBeginningIpAddr_Type()
)
hwNatAddrGrpBeginningIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpBeginningIpAddr.setStatus("current")
_HwNatAddrGrpEndingIpAddr_Type = IpAddress
_HwNatAddrGrpEndingIpAddr_Object = MibTableColumn
hwNatAddrGrpEndingIpAddr = _HwNatAddrGrpEndingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1, 3),
    _HwNatAddrGrpEndingIpAddr_Type()
)
hwNatAddrGrpEndingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpEndingIpAddr.setStatus("current")
_HwNatAddrGrpRefCount_Type = Unsigned32
_HwNatAddrGrpRefCount_Object = MibTableColumn
hwNatAddrGrpRefCount = _HwNatAddrGrpRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1, 4),
    _HwNatAddrGrpRefCount_Type()
)
hwNatAddrGrpRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrGrpRefCount.setStatus("current")


class _HwNatAddrGrpVpnName_Type(OctetString):
    """Custom type hwNatAddrGrpVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwNatAddrGrpVpnName_Type.__name__ = "OctetString"
_HwNatAddrGrpVpnName_Object = MibTableColumn
hwNatAddrGrpVpnName = _HwNatAddrGrpVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1, 5),
    _HwNatAddrGrpVpnName_Type()
)
hwNatAddrGrpVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpVpnName.setStatus("current")
_HwNatAddrGrpRowstatus_Type = RowStatus
_HwNatAddrGrpRowstatus_Object = MibTableColumn
hwNatAddrGrpRowstatus = _HwNatAddrGrpRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 12, 2, 2, 1, 6),
    _HwNatAddrGrpRowstatus_Type()
)
hwNatAddrGrpRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatAddrGrpRowstatus.setStatus("current")
_HwBrasSbcBandwidthLimit_ObjectIdentity = ObjectIdentity
hwBrasSbcBandwidthLimit = _HwBrasSbcBandwidthLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 13)
)
_HwBrasSbcBWLimitLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcBWLimitLeaves = _HwBrasSbcBWLimitLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 13, 1)
)


class _HwBrasSbcBWLimitType_Type(HwBrasBWLimitType):
    """Custom type hwBrasSbcBWLimitType based on HwBrasBWLimitType"""


_HwBrasSbcBWLimitType_Object = MibScalar
hwBrasSbcBWLimitType = _HwBrasSbcBWLimitType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 13, 1, 1),
    _HwBrasSbcBWLimitType_Type()
)
hwBrasSbcBWLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcBWLimitType.setStatus("current")


class _HwBrasSbcBWLimitValue_Type(Unsigned32):
    """Custom type hwBrasSbcBWLimitValue based on Unsigned32"""
    defaultValue = 6291456

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10485760),
    )


_HwBrasSbcBWLimitValue_Type.__name__ = "Unsigned32"
_HwBrasSbcBWLimitValue_Object = MibScalar
hwBrasSbcBWLimitValue = _HwBrasSbcBWLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 2, 13, 1, 2),
    _HwBrasSbcBWLimitValue_Type()
)
hwBrasSbcBWLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcBWLimitValue.setStatus("current")
_HwBrasSbcView_ObjectIdentity = ObjectIdentity
hwBrasSbcView = _HwBrasSbcView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3)
)
_HwBrasSbcViewLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcViewLeaves = _HwBrasSbcViewLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 1)
)


class _HwBrasSbcSoftVersion_Type(DisplayString):
    """Custom type hwBrasSbcSoftVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwBrasSbcSoftVersion_Type.__name__ = "DisplayString"
_HwBrasSbcSoftVersion_Object = MibScalar
hwBrasSbcSoftVersion = _HwBrasSbcSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 1, 1),
    _HwBrasSbcSoftVersion_Type()
)
hwBrasSbcSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSoftVersion.setStatus("current")


class _HwBrasSbcCpuUsage_Type(Unsigned32):
    """Custom type hwBrasSbcCpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBrasSbcCpuUsage_Type.__name__ = "Unsigned32"
_HwBrasSbcCpuUsage_Object = MibScalar
hwBrasSbcCpuUsage = _HwBrasSbcCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 1, 2),
    _HwBrasSbcCpuUsage_Type()
)
hwBrasSbcCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcCpuUsage.setStatus("current")


class _HwBrasSbcUmsVersion_Type(DisplayString):
    """Custom type hwBrasSbcUmsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_HwBrasSbcUmsVersion_Type.__name__ = "DisplayString"
_HwBrasSbcUmsVersion_Object = MibScalar
hwBrasSbcUmsVersion = _HwBrasSbcUmsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 1, 3),
    _HwBrasSbcUmsVersion_Type()
)
hwBrasSbcUmsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUmsVersion.setStatus("current")
_HwBrasSbcViewTables_ObjectIdentity = ObjectIdentity
hwBrasSbcViewTables = _HwBrasSbcViewTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2)
)
_HwBrasSbcStatisticTable_Object = MibTable
hwBrasSbcStatisticTable = _HwBrasSbcStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcStatisticTable.setStatus("current")
_HwBrasSbcStatisticEntry_Object = MibTableRow
hwBrasSbcStatisticEntry = _HwBrasSbcStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1, 1)
)
hwBrasSbcStatisticEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticOffset"),
)
if mibBuilder.loadTexts:
    hwBrasSbcStatisticEntry.setStatus("current")


class _HwBrasSbcStatisticIndex_Type(Unsigned32):
    """Custom type hwBrasSbcStatisticIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBrasSbcStatisticIndex_Type.__name__ = "Unsigned32"
_HwBrasSbcStatisticIndex_Object = MibTableColumn
hwBrasSbcStatisticIndex = _HwBrasSbcStatisticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1, 1, 1),
    _HwBrasSbcStatisticIndex_Type()
)
hwBrasSbcStatisticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticIndex.setStatus("current")


class _HwBrasSbcStatisticOffset_Type(Unsigned32):
    """Custom type hwBrasSbcStatisticOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 143),
    )


_HwBrasSbcStatisticOffset_Type.__name__ = "Unsigned32"
_HwBrasSbcStatisticOffset_Object = MibTableColumn
hwBrasSbcStatisticOffset = _HwBrasSbcStatisticOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1, 1, 2),
    _HwBrasSbcStatisticOffset_Type()
)
hwBrasSbcStatisticOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticOffset.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticOffset.setUnits("hours")
_HwBrasSbcStatisticDesc_Type = DisplayString
_HwBrasSbcStatisticDesc_Object = MibTableColumn
hwBrasSbcStatisticDesc = _HwBrasSbcStatisticDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1, 1, 3),
    _HwBrasSbcStatisticDesc_Type()
)
hwBrasSbcStatisticDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticDesc.setStatus("current")
_HwBrasSbcStatisticValue_Type = Unsigned32
_HwBrasSbcStatisticValue_Object = MibTableColumn
hwBrasSbcStatisticValue = _HwBrasSbcStatisticValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1, 1, 4),
    _HwBrasSbcStatisticValue_Type()
)
hwBrasSbcStatisticValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticValue.setStatus("current")


class _HwBrasSbcStatisticTime_Type(DateAndTime):
    """Custom type hwBrasSbcStatisticTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwBrasSbcStatisticTime_Type.__name__ = "DateAndTime"
_HwBrasSbcStatisticTime_Object = MibTableColumn
hwBrasSbcStatisticTime = _HwBrasSbcStatisticTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 1, 3, 2, 1, 1, 5),
    _HwBrasSbcStatisticTime_Type()
)
hwBrasSbcStatisticTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcStatisticTime.setStatus("current")
_HwBrasSbcSip_ObjectIdentity = ObjectIdentity
hwBrasSbcSip = _HwBrasSbcSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2)
)
_HwBrasSbcSipLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcSipLeaves = _HwBrasSbcSipLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1)
)


class _HwBrasSbcSipEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSipEnable based on HWBrasEnabledStatus"""


_HwBrasSbcSipEnable_Object = MibScalar
hwBrasSbcSipEnable = _HwBrasSbcSipEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 1),
    _HwBrasSbcSipEnable_Type()
)
hwBrasSbcSipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipEnable.setStatus("current")


class _HwBrasSbcSipSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSipSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcSipSyslogEnable_Object = MibScalar
hwBrasSbcSipSyslogEnable = _HwBrasSbcSipSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 2),
    _HwBrasSbcSipSyslogEnable_Type()
)
hwBrasSbcSipSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipSyslogEnable.setStatus("current")


class _HwBrasSbcSipAnonymity_Type(DisplayString):
    """Custom type hwBrasSbcSipAnonymity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBrasSbcSipAnonymity_Type.__name__ = "DisplayString"
_HwBrasSbcSipAnonymity_Object = MibScalar
hwBrasSbcSipAnonymity = _HwBrasSbcSipAnonymity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 3),
    _HwBrasSbcSipAnonymity_Type()
)
hwBrasSbcSipAnonymity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipAnonymity.setStatus("current")


class _HwBrasSbcSipCheckheartEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSipCheckheartEnable based on HWBrasEnabledStatus"""


_HwBrasSbcSipCheckheartEnable_Object = MibScalar
hwBrasSbcSipCheckheartEnable = _HwBrasSbcSipCheckheartEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 4),
    _HwBrasSbcSipCheckheartEnable_Type()
)
hwBrasSbcSipCheckheartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipCheckheartEnable.setStatus("current")


class _HwBrasSbcSipCallsessionTimer_Type(Unsigned32):
    """Custom type hwBrasSbcSipCallsessionTimer based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_HwBrasSbcSipCallsessionTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcSipCallsessionTimer_Object = MibScalar
hwBrasSbcSipCallsessionTimer = _HwBrasSbcSipCallsessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 5),
    _HwBrasSbcSipCallsessionTimer_Type()
)
hwBrasSbcSipCallsessionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipCallsessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcSipCallsessionTimer.setUnits("minutes")


class _HwBrasSbcSipPDHCountLimit_Type(Unsigned32):
    """Custom type hwBrasSbcSipPDHCountLimit based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBrasSbcSipPDHCountLimit_Type.__name__ = "Unsigned32"
_HwBrasSbcSipPDHCountLimit_Object = MibScalar
hwBrasSbcSipPDHCountLimit = _HwBrasSbcSipPDHCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 6),
    _HwBrasSbcSipPDHCountLimit_Type()
)
hwBrasSbcSipPDHCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipPDHCountLimit.setStatus("current")


class _HwBrasSbcSipRegReduceStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcSipRegReduceStatus based on HWBrasEnabledStatus"""


_HwBrasSbcSipRegReduceStatus_Object = MibScalar
hwBrasSbcSipRegReduceStatus = _HwBrasSbcSipRegReduceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 7),
    _HwBrasSbcSipRegReduceStatus_Type()
)
hwBrasSbcSipRegReduceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipRegReduceStatus.setStatus("current")


class _HwBrasSbcSipRegReduceTimer_Type(Unsigned32):
    """Custom type hwBrasSbcSipRegReduceTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HwBrasSbcSipRegReduceTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcSipRegReduceTimer_Object = MibScalar
hwBrasSbcSipRegReduceTimer = _HwBrasSbcSipRegReduceTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 1, 8),
    _HwBrasSbcSipRegReduceTimer_Type()
)
hwBrasSbcSipRegReduceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipRegReduceTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcSipRegReduceTimer.setUnits("minutes")
_HwBrasSbcSipTables_ObjectIdentity = ObjectIdentity
hwBrasSbcSipTables = _HwBrasSbcSipTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2)
)
_HwBrasSbcSipWellknownPortTable_Object = MibTable
hwBrasSbcSipWellknownPortTable = _HwBrasSbcSipWellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortTable.setStatus("current")
_HwBrasSbcSipWellknownPortEntry_Object = MibTableRow
hwBrasSbcSipWellknownPortEntry = _HwBrasSbcSipWellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1, 1)
)
hwBrasSbcSipWellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipWellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipWellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipWellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortEntry.setStatus("current")


class _HwBrasSbcSipWellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcSipWellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("softxaddr", 2))
    )


_HwBrasSbcSipWellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcSipWellknownPortIndex_Object = MibTableColumn
hwBrasSbcSipWellknownPortIndex = _HwBrasSbcSipWellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1, 1, 1),
    _HwBrasSbcSipWellknownPortIndex_Type()
)
hwBrasSbcSipWellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortIndex.setStatus("current")


class _HwBrasSbcSipWellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcSipWellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sip", 1)
    )


_HwBrasSbcSipWellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcSipWellknownPortProtocol_Object = MibTableColumn
hwBrasSbcSipWellknownPortProtocol = _HwBrasSbcSipWellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1, 1, 2),
    _HwBrasSbcSipWellknownPortProtocol_Type()
)
hwBrasSbcSipWellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortProtocol.setStatus("current")
_HwBrasSbcSipWellknownPortAddr_Type = IpAddress
_HwBrasSbcSipWellknownPortAddr_Object = MibTableColumn
hwBrasSbcSipWellknownPortAddr = _HwBrasSbcSipWellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1, 1, 3),
    _HwBrasSbcSipWellknownPortAddr_Type()
)
hwBrasSbcSipWellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortAddr.setStatus("current")


class _HwBrasSbcSipWellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcSipWellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcSipWellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcSipWellknownPortPort_Object = MibTableColumn
hwBrasSbcSipWellknownPortPort = _HwBrasSbcSipWellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1, 1, 4),
    _HwBrasSbcSipWellknownPortPort_Type()
)
hwBrasSbcSipWellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortPort.setStatus("current")
_HwBrasSbcSipWellknownPortRowStatus_Type = RowStatus
_HwBrasSbcSipWellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcSipWellknownPortRowStatus = _HwBrasSbcSipWellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 1, 1, 5),
    _HwBrasSbcSipWellknownPortRowStatus_Type()
)
hwBrasSbcSipWellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcSipWellknownPortRowStatus.setStatus("current")
_HwBrasSbcSipSignalMapTable_Object = MibTable
hwBrasSbcSipSignalMapTable = _HwBrasSbcSipSignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcSipSignalMapTable.setStatus("current")
_HwBrasSbcSipSignalMapEntry_Object = MibTableRow
hwBrasSbcSipSignalMapEntry = _HwBrasSbcSipSignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 2, 1)
)
hwBrasSbcSipSignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipSignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipSignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSipSignalMapEntry.setStatus("current")
_HwBrasSbcSipSignalMapAddr_Type = IpAddress
_HwBrasSbcSipSignalMapAddr_Object = MibTableColumn
hwBrasSbcSipSignalMapAddr = _HwBrasSbcSipSignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 2, 1, 1),
    _HwBrasSbcSipSignalMapAddr_Type()
)
hwBrasSbcSipSignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipSignalMapAddr.setStatus("current")


class _HwBrasSbcSipSignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcSipSignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sip", 1)
    )


_HwBrasSbcSipSignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcSipSignalMapProtocol_Object = MibTableColumn
hwBrasSbcSipSignalMapProtocol = _HwBrasSbcSipSignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 2, 1, 2),
    _HwBrasSbcSipSignalMapProtocol_Type()
)
hwBrasSbcSipSignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipSignalMapProtocol.setStatus("current")
_HwBrasSbcSipSignalMapNumber_Type = Unsigned32
_HwBrasSbcSipSignalMapNumber_Object = MibTableColumn
hwBrasSbcSipSignalMapNumber = _HwBrasSbcSipSignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 2, 1, 3),
    _HwBrasSbcSipSignalMapNumber_Type()
)
hwBrasSbcSipSignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipSignalMapNumber.setStatus("current")


class _HwBrasSbcSipSignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcSipSignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcSipSignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcSipSignalMapAddrType_Object = MibTableColumn
hwBrasSbcSipSignalMapAddrType = _HwBrasSbcSipSignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 2, 1, 4),
    _HwBrasSbcSipSignalMapAddrType_Type()
)
hwBrasSbcSipSignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipSignalMapAddrType.setStatus("current")
_HwBrasSbcSipMediaMapTable_Object = MibTable
hwBrasSbcSipMediaMapTable = _HwBrasSbcSipMediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcSipMediaMapTable.setStatus("current")
_HwBrasSbcSipMediaMapEntry_Object = MibTableRow
hwBrasSbcSipMediaMapEntry = _HwBrasSbcSipMediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 3, 1)
)
hwBrasSbcSipMediaMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipMediaMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipMediaMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSipMediaMapEntry.setStatus("current")
_HwBrasSbcSipMediaMapAddr_Type = IpAddress
_HwBrasSbcSipMediaMapAddr_Object = MibTableColumn
hwBrasSbcSipMediaMapAddr = _HwBrasSbcSipMediaMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 3, 1, 1),
    _HwBrasSbcSipMediaMapAddr_Type()
)
hwBrasSbcSipMediaMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipMediaMapAddr.setStatus("current")


class _HwBrasSbcSipMediaMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcSipMediaMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sip", 1)
    )


_HwBrasSbcSipMediaMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcSipMediaMapProtocol_Object = MibTableColumn
hwBrasSbcSipMediaMapProtocol = _HwBrasSbcSipMediaMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 3, 1, 2),
    _HwBrasSbcSipMediaMapProtocol_Type()
)
hwBrasSbcSipMediaMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipMediaMapProtocol.setStatus("current")
_HwBrasSbcSipMediaMapNumber_Type = Unsigned32
_HwBrasSbcSipMediaMapNumber_Object = MibTableColumn
hwBrasSbcSipMediaMapNumber = _HwBrasSbcSipMediaMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 3, 1, 3),
    _HwBrasSbcSipMediaMapNumber_Type()
)
hwBrasSbcSipMediaMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipMediaMapNumber.setStatus("current")
_HwBrasSbcSipIntercomMapSignalTable_Object = MibTable
hwBrasSbcSipIntercomMapSignalTable = _HwBrasSbcSipIntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapSignalTable.setStatus("current")
_HwBrasSbcSipIntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcSipIntercomMapSignalEntry = _HwBrasSbcSipIntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 4, 1)
)
hwBrasSbcSipIntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipIntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipIntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapSignalEntry.setStatus("current")
_HwBrasSbcSipIntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcSipIntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcSipIntercomMapSignalAddr = _HwBrasSbcSipIntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 4, 1, 1),
    _HwBrasSbcSipIntercomMapSignalAddr_Type()
)
hwBrasSbcSipIntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcSipIntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcSipIntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sip", 1)
    )


_HwBrasSbcSipIntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcSipIntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcSipIntercomMapSignalProtocol = _HwBrasSbcSipIntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 4, 1, 2),
    _HwBrasSbcSipIntercomMapSignalProtocol_Type()
)
hwBrasSbcSipIntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcSipIntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcSipIntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcSipIntercomMapSignalNumber = _HwBrasSbcSipIntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 4, 1, 3),
    _HwBrasSbcSipIntercomMapSignalNumber_Type()
)
hwBrasSbcSipIntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapSignalNumber.setStatus("current")
_HwBrasSbcSipIntercomMapMediaTable_Object = MibTable
hwBrasSbcSipIntercomMapMediaTable = _HwBrasSbcSipIntercomMapMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapMediaTable.setStatus("current")
_HwBrasSbcSipIntercomMapMediaEntry_Object = MibTableRow
hwBrasSbcSipIntercomMapMediaEntry = _HwBrasSbcSipIntercomMapMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 5, 1)
)
hwBrasSbcSipIntercomMapMediaEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipIntercomMapMediaAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipIntercomMapMediaProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapMediaEntry.setStatus("current")
_HwBrasSbcSipIntercomMapMediaAddr_Type = IpAddress
_HwBrasSbcSipIntercomMapMediaAddr_Object = MibTableColumn
hwBrasSbcSipIntercomMapMediaAddr = _HwBrasSbcSipIntercomMapMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 5, 1, 1),
    _HwBrasSbcSipIntercomMapMediaAddr_Type()
)
hwBrasSbcSipIntercomMapMediaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapMediaAddr.setStatus("current")


class _HwBrasSbcSipIntercomMapMediaProtocol_Type(Integer32):
    """Custom type hwBrasSbcSipIntercomMapMediaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sip", 1)
    )


_HwBrasSbcSipIntercomMapMediaProtocol_Type.__name__ = "Integer32"
_HwBrasSbcSipIntercomMapMediaProtocol_Object = MibTableColumn
hwBrasSbcSipIntercomMapMediaProtocol = _HwBrasSbcSipIntercomMapMediaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 5, 1, 2),
    _HwBrasSbcSipIntercomMapMediaProtocol_Type()
)
hwBrasSbcSipIntercomMapMediaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapMediaProtocol.setStatus("current")
_HwBrasSbcSipIntercomMapMediaNumber_Type = Unsigned32
_HwBrasSbcSipIntercomMapMediaNumber_Object = MibTableColumn
hwBrasSbcSipIntercomMapMediaNumber = _HwBrasSbcSipIntercomMapMediaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 5, 1, 3),
    _HwBrasSbcSipIntercomMapMediaNumber_Type()
)
hwBrasSbcSipIntercomMapMediaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipIntercomMapMediaNumber.setStatus("current")
_HwBrasSbcSipStatSignalPacketTable_Object = MibTable
hwBrasSbcSipStatSignalPacketTable = _HwBrasSbcSipStatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketTable.setStatus("current")
_HwBrasSbcSipStatSignalPacketEntry_Object = MibTableRow
hwBrasSbcSipStatSignalPacketEntry = _HwBrasSbcSipStatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1)
)
hwBrasSbcSipStatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipStatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketEntry.setStatus("current")


class _HwBrasSbcSipStatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcSipStatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sip", 1)
    )


_HwBrasSbcSipStatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcSipStatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcSipStatSignalPacketIndex = _HwBrasSbcSipStatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1, 1),
    _HwBrasSbcSipStatSignalPacketIndex_Type()
)
hwBrasSbcSipStatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketIndex.setStatus("current")
_HwBrasSbcSipStatSignalPacketInNumber_Type = Counter64
_HwBrasSbcSipStatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcSipStatSignalPacketInNumber = _HwBrasSbcSipStatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1, 2),
    _HwBrasSbcSipStatSignalPacketInNumber_Type()
)
hwBrasSbcSipStatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketInNumber.setStatus("current")
_HwBrasSbcSipStatSignalPacketInOctet_Type = Counter64
_HwBrasSbcSipStatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcSipStatSignalPacketInOctet = _HwBrasSbcSipStatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1, 3),
    _HwBrasSbcSipStatSignalPacketInOctet_Type()
)
hwBrasSbcSipStatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketInOctet.setStatus("current")
_HwBrasSbcSipStatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcSipStatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcSipStatSignalPacketOutNumber = _HwBrasSbcSipStatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1, 4),
    _HwBrasSbcSipStatSignalPacketOutNumber_Type()
)
hwBrasSbcSipStatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcSipStatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcSipStatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcSipStatSignalPacketOutOctet = _HwBrasSbcSipStatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1, 5),
    _HwBrasSbcSipStatSignalPacketOutOctet_Type()
)
hwBrasSbcSipStatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcSipStatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcSipStatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcSipStatSignalPacketRowStatus = _HwBrasSbcSipStatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 2, 2, 6, 1, 6),
    _HwBrasSbcSipStatSignalPacketRowStatus_Type()
)
hwBrasSbcSipStatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcSipStatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcMgcp_ObjectIdentity = ObjectIdentity
hwBrasSbcMgcp = _HwBrasSbcMgcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3)
)
_HwBrasSbcMgcpLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcMgcpLeaves = _HwBrasSbcMgcpLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1)
)


class _HwBrasSbcMgcpSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMgcpSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcMgcpSyslogEnable_Object = MibScalar
hwBrasSbcMgcpSyslogEnable = _HwBrasSbcMgcpSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1, 1),
    _HwBrasSbcMgcpSyslogEnable_Type()
)
hwBrasSbcMgcpSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSyslogEnable.setStatus("current")


class _HwBrasSbcMgcpAuepTimer_Type(Unsigned32):
    """Custom type hwBrasSbcMgcpAuepTimer based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HwBrasSbcMgcpAuepTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcMgcpAuepTimer_Object = MibScalar
hwBrasSbcMgcpAuepTimer = _HwBrasSbcMgcpAuepTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1, 2),
    _HwBrasSbcMgcpAuepTimer_Type()
)
hwBrasSbcMgcpAuepTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpAuepTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpAuepTimer.setUnits("seconds")


class _HwBrasSbcMgcpCcbTimer_Type(Unsigned32):
    """Custom type hwBrasSbcMgcpCcbTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14400),
    )


_HwBrasSbcMgcpCcbTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcMgcpCcbTimer_Object = MibScalar
hwBrasSbcMgcpCcbTimer = _HwBrasSbcMgcpCcbTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1, 3),
    _HwBrasSbcMgcpCcbTimer_Type()
)
hwBrasSbcMgcpCcbTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpCcbTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpCcbTimer.setUnits("minutes")


class _HwBrasSbcMgcpTxTimer_Type(Unsigned32):
    """Custom type hwBrasSbcMgcpTxTimer based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 60),
    )


_HwBrasSbcMgcpTxTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcMgcpTxTimer_Object = MibScalar
hwBrasSbcMgcpTxTimer = _HwBrasSbcMgcpTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1, 4),
    _HwBrasSbcMgcpTxTimer_Type()
)
hwBrasSbcMgcpTxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpTxTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpTxTimer.setUnits("seconds")


class _HwBrasSbcMgcpEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcMgcpEnable based on HWBrasEnabledStatus"""


_HwBrasSbcMgcpEnable_Object = MibScalar
hwBrasSbcMgcpEnable = _HwBrasSbcMgcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1, 5),
    _HwBrasSbcMgcpEnable_Type()
)
hwBrasSbcMgcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpEnable.setStatus("current")


class _HwBrasSbcMgcpPDHCountLimit_Type(Unsigned32):
    """Custom type hwBrasSbcMgcpPDHCountLimit based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBrasSbcMgcpPDHCountLimit_Type.__name__ = "Unsigned32"
_HwBrasSbcMgcpPDHCountLimit_Object = MibScalar
hwBrasSbcMgcpPDHCountLimit = _HwBrasSbcMgcpPDHCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 1, 6),
    _HwBrasSbcMgcpPDHCountLimit_Type()
)
hwBrasSbcMgcpPDHCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpPDHCountLimit.setStatus("current")
_HwBrasSbcMgcpTables_ObjectIdentity = ObjectIdentity
hwBrasSbcMgcpTables = _HwBrasSbcMgcpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3)
)
_HwBrasSbcMgcpWellknownPortTable_Object = MibTable
hwBrasSbcMgcpWellknownPortTable = _HwBrasSbcMgcpWellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortTable.setStatus("current")
_HwBrasSbcMgcpWellknownPortEntry_Object = MibTableRow
hwBrasSbcMgcpWellknownPortEntry = _HwBrasSbcMgcpWellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1, 1)
)
hwBrasSbcMgcpWellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpWellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpWellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpWellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortEntry.setStatus("current")


class _HwBrasSbcMgcpWellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcMgcpWellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("softxaddr", 2))
    )


_HwBrasSbcMgcpWellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcMgcpWellknownPortIndex_Object = MibTableColumn
hwBrasSbcMgcpWellknownPortIndex = _HwBrasSbcMgcpWellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1, 1, 1),
    _HwBrasSbcMgcpWellknownPortIndex_Type()
)
hwBrasSbcMgcpWellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortIndex.setStatus("current")


class _HwBrasSbcMgcpWellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcMgcpWellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mgcp", 1)
    )


_HwBrasSbcMgcpWellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcMgcpWellknownPortProtocol_Object = MibTableColumn
hwBrasSbcMgcpWellknownPortProtocol = _HwBrasSbcMgcpWellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1, 1, 2),
    _HwBrasSbcMgcpWellknownPortProtocol_Type()
)
hwBrasSbcMgcpWellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortProtocol.setStatus("current")
_HwBrasSbcMgcpWellknownPortAddr_Type = IpAddress
_HwBrasSbcMgcpWellknownPortAddr_Object = MibTableColumn
hwBrasSbcMgcpWellknownPortAddr = _HwBrasSbcMgcpWellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1, 1, 3),
    _HwBrasSbcMgcpWellknownPortAddr_Type()
)
hwBrasSbcMgcpWellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortAddr.setStatus("current")


class _HwBrasSbcMgcpWellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcMgcpWellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcMgcpWellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcMgcpWellknownPortPort_Object = MibTableColumn
hwBrasSbcMgcpWellknownPortPort = _HwBrasSbcMgcpWellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1, 1, 4),
    _HwBrasSbcMgcpWellknownPortPort_Type()
)
hwBrasSbcMgcpWellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortPort.setStatus("current")
_HwBrasSbcMgcpWellknownPortRowStatus_Type = RowStatus
_HwBrasSbcMgcpWellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcMgcpWellknownPortRowStatus = _HwBrasSbcMgcpWellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 1, 1, 5),
    _HwBrasSbcMgcpWellknownPortRowStatus_Type()
)
hwBrasSbcMgcpWellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpWellknownPortRowStatus.setStatus("current")
_HwBrasSbcMgcpSignalMapTable_Object = MibTable
hwBrasSbcMgcpSignalMapTable = _HwBrasSbcMgcpSignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSignalMapTable.setStatus("current")
_HwBrasSbcMgcpSignalMapEntry_Object = MibTableRow
hwBrasSbcMgcpSignalMapEntry = _HwBrasSbcMgcpSignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 2, 1)
)
hwBrasSbcMgcpSignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpSignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpSignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSignalMapEntry.setStatus("current")
_HwBrasSbcMgcpSignalMapAddr_Type = IpAddress
_HwBrasSbcMgcpSignalMapAddr_Object = MibTableColumn
hwBrasSbcMgcpSignalMapAddr = _HwBrasSbcMgcpSignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 2, 1, 1),
    _HwBrasSbcMgcpSignalMapAddr_Type()
)
hwBrasSbcMgcpSignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSignalMapAddr.setStatus("current")


class _HwBrasSbcMgcpSignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcMgcpSignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mgcp", 1)
    )


_HwBrasSbcMgcpSignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcMgcpSignalMapProtocol_Object = MibTableColumn
hwBrasSbcMgcpSignalMapProtocol = _HwBrasSbcMgcpSignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 2, 1, 2),
    _HwBrasSbcMgcpSignalMapProtocol_Type()
)
hwBrasSbcMgcpSignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSignalMapProtocol.setStatus("current")
_HwBrasSbcMgcpSignalMapNumber_Type = Unsigned32
_HwBrasSbcMgcpSignalMapNumber_Object = MibTableColumn
hwBrasSbcMgcpSignalMapNumber = _HwBrasSbcMgcpSignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 2, 1, 3),
    _HwBrasSbcMgcpSignalMapNumber_Type()
)
hwBrasSbcMgcpSignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSignalMapNumber.setStatus("current")


class _HwBrasSbcMgcpSignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcMgcpSignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcMgcpSignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcMgcpSignalMapAddrType_Object = MibTableColumn
hwBrasSbcMgcpSignalMapAddrType = _HwBrasSbcMgcpSignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 2, 1, 4),
    _HwBrasSbcMgcpSignalMapAddrType_Type()
)
hwBrasSbcMgcpSignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpSignalMapAddrType.setStatus("current")
_HwBrasSbcMgcpMediaMapTable_Object = MibTable
hwBrasSbcMgcpMediaMapTable = _HwBrasSbcMgcpMediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpMediaMapTable.setStatus("current")
_HwBrasSbcMgcpMediaMapEntry_Object = MibTableRow
hwBrasSbcMgcpMediaMapEntry = _HwBrasSbcMgcpMediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 3, 1)
)
hwBrasSbcMgcpMediaMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpMediaMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpMediaMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpMediaMapEntry.setStatus("current")
_HwBrasSbcMgcpMediaMapAddr_Type = IpAddress
_HwBrasSbcMgcpMediaMapAddr_Object = MibTableColumn
hwBrasSbcMgcpMediaMapAddr = _HwBrasSbcMgcpMediaMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 3, 1, 1),
    _HwBrasSbcMgcpMediaMapAddr_Type()
)
hwBrasSbcMgcpMediaMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpMediaMapAddr.setStatus("current")


class _HwBrasSbcMgcpMediaMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcMgcpMediaMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mgcp", 1)
    )


_HwBrasSbcMgcpMediaMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcMgcpMediaMapProtocol_Object = MibTableColumn
hwBrasSbcMgcpMediaMapProtocol = _HwBrasSbcMgcpMediaMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 3, 1, 2),
    _HwBrasSbcMgcpMediaMapProtocol_Type()
)
hwBrasSbcMgcpMediaMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpMediaMapProtocol.setStatus("current")
_HwBrasSbcMgcpMediaMapNumber_Type = Unsigned32
_HwBrasSbcMgcpMediaMapNumber_Object = MibTableColumn
hwBrasSbcMgcpMediaMapNumber = _HwBrasSbcMgcpMediaMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 3, 1, 3),
    _HwBrasSbcMgcpMediaMapNumber_Type()
)
hwBrasSbcMgcpMediaMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpMediaMapNumber.setStatus("current")
_HwBrasSbcMgcpIntercomMapSignalTable_Object = MibTable
hwBrasSbcMgcpIntercomMapSignalTable = _HwBrasSbcMgcpIntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapSignalTable.setStatus("current")
_HwBrasSbcMgcpIntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcMgcpIntercomMapSignalEntry = _HwBrasSbcMgcpIntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 4, 1)
)
hwBrasSbcMgcpIntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpIntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpIntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapSignalEntry.setStatus("current")
_HwBrasSbcMgcpIntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcMgcpIntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcMgcpIntercomMapSignalAddr = _HwBrasSbcMgcpIntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 4, 1, 1),
    _HwBrasSbcMgcpIntercomMapSignalAddr_Type()
)
hwBrasSbcMgcpIntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcMgcpIntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcMgcpIntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mgcp", 1)
    )


_HwBrasSbcMgcpIntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcMgcpIntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcMgcpIntercomMapSignalProtocol = _HwBrasSbcMgcpIntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 4, 1, 2),
    _HwBrasSbcMgcpIntercomMapSignalProtocol_Type()
)
hwBrasSbcMgcpIntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcMgcpIntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcMgcpIntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcMgcpIntercomMapSignalNumber = _HwBrasSbcMgcpIntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 4, 1, 3),
    _HwBrasSbcMgcpIntercomMapSignalNumber_Type()
)
hwBrasSbcMgcpIntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapSignalNumber.setStatus("current")
_HwBrasSbcMgcpIntercomMapMediaTable_Object = MibTable
hwBrasSbcMgcpIntercomMapMediaTable = _HwBrasSbcMgcpIntercomMapMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapMediaTable.setStatus("current")
_HwBrasSbcMgcpIntercomMapMediaEntry_Object = MibTableRow
hwBrasSbcMgcpIntercomMapMediaEntry = _HwBrasSbcMgcpIntercomMapMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 5, 1)
)
hwBrasSbcMgcpIntercomMapMediaEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpIntercomMapMediaAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpIntercomMapMediaProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapMediaEntry.setStatus("current")
_HwBrasSbcMgcpIntercomMapMediaAddr_Type = IpAddress
_HwBrasSbcMgcpIntercomMapMediaAddr_Object = MibTableColumn
hwBrasSbcMgcpIntercomMapMediaAddr = _HwBrasSbcMgcpIntercomMapMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 5, 1, 1),
    _HwBrasSbcMgcpIntercomMapMediaAddr_Type()
)
hwBrasSbcMgcpIntercomMapMediaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapMediaAddr.setStatus("current")


class _HwBrasSbcMgcpIntercomMapMediaProtocol_Type(Integer32):
    """Custom type hwBrasSbcMgcpIntercomMapMediaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mgcp", 1)
    )


_HwBrasSbcMgcpIntercomMapMediaProtocol_Type.__name__ = "Integer32"
_HwBrasSbcMgcpIntercomMapMediaProtocol_Object = MibTableColumn
hwBrasSbcMgcpIntercomMapMediaProtocol = _HwBrasSbcMgcpIntercomMapMediaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 5, 1, 2),
    _HwBrasSbcMgcpIntercomMapMediaProtocol_Type()
)
hwBrasSbcMgcpIntercomMapMediaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapMediaProtocol.setStatus("current")
_HwBrasSbcMgcpIntercomMapMediaNumber_Type = Unsigned32
_HwBrasSbcMgcpIntercomMapMediaNumber_Object = MibTableColumn
hwBrasSbcMgcpIntercomMapMediaNumber = _HwBrasSbcMgcpIntercomMapMediaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 5, 1, 3),
    _HwBrasSbcMgcpIntercomMapMediaNumber_Type()
)
hwBrasSbcMgcpIntercomMapMediaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpIntercomMapMediaNumber.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketTable_Object = MibTable
hwBrasSbcMgcpStatSignalPacketTable = _HwBrasSbcMgcpStatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketTable.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketEntry_Object = MibTableRow
hwBrasSbcMgcpStatSignalPacketEntry = _HwBrasSbcMgcpStatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1)
)
hwBrasSbcMgcpStatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpStatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketEntry.setStatus("current")


class _HwBrasSbcMgcpStatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcMgcpStatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mgcp", 1)
    )


_HwBrasSbcMgcpStatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcMgcpStatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcMgcpStatSignalPacketIndex = _HwBrasSbcMgcpStatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1, 1),
    _HwBrasSbcMgcpStatSignalPacketIndex_Type()
)
hwBrasSbcMgcpStatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketIndex.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketInNumber_Type = Counter64
_HwBrasSbcMgcpStatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcMgcpStatSignalPacketInNumber = _HwBrasSbcMgcpStatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1, 2),
    _HwBrasSbcMgcpStatSignalPacketInNumber_Type()
)
hwBrasSbcMgcpStatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketInNumber.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketInOctet_Type = Counter64
_HwBrasSbcMgcpStatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcMgcpStatSignalPacketInOctet = _HwBrasSbcMgcpStatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1, 3),
    _HwBrasSbcMgcpStatSignalPacketInOctet_Type()
)
hwBrasSbcMgcpStatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketInOctet.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcMgcpStatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcMgcpStatSignalPacketOutNumber = _HwBrasSbcMgcpStatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1, 4),
    _HwBrasSbcMgcpStatSignalPacketOutNumber_Type()
)
hwBrasSbcMgcpStatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcMgcpStatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcMgcpStatSignalPacketOutOctet = _HwBrasSbcMgcpStatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1, 5),
    _HwBrasSbcMgcpStatSignalPacketOutOctet_Type()
)
hwBrasSbcMgcpStatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcMgcpStatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcMgcpStatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcMgcpStatSignalPacketRowStatus = _HwBrasSbcMgcpStatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 3, 3, 6, 1, 6),
    _HwBrasSbcMgcpStatSignalPacketRowStatus_Type()
)
hwBrasSbcMgcpStatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcMgcpStatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcIadms_ObjectIdentity = ObjectIdentity
hwBrasSbcIadms = _HwBrasSbcIadms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4)
)
_HwBrasSbcIadmsLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcIadmsLeaves = _HwBrasSbcIadmsLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 1)
)


class _HwBrasSbcIadmsEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIadmsEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIadmsEnable_Object = MibScalar
hwBrasSbcIadmsEnable = _HwBrasSbcIadmsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 1, 1),
    _HwBrasSbcIadmsEnable_Type()
)
hwBrasSbcIadmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsEnable.setStatus("current")


class _HwBrasSbcIadmsSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIadmsSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIadmsSyslogEnable_Object = MibScalar
hwBrasSbcIadmsSyslogEnable = _HwBrasSbcIadmsSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 1, 2),
    _HwBrasSbcIadmsSyslogEnable_Type()
)
hwBrasSbcIadmsSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSyslogEnable.setStatus("current")


class _HwBrasSbcIadmsRegRefreshEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIadmsRegRefreshEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIadmsRegRefreshEnable_Object = MibScalar
hwBrasSbcIadmsRegRefreshEnable = _HwBrasSbcIadmsRegRefreshEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 1, 3),
    _HwBrasSbcIadmsRegRefreshEnable_Type()
)
hwBrasSbcIadmsRegRefreshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsRegRefreshEnable.setStatus("current")


class _HwBrasSbcIadmsTimer_Type(Unsigned32):
    """Custom type hwBrasSbcIadmsTimer based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_HwBrasSbcIadmsTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcIadmsTimer_Object = MibScalar
hwBrasSbcIadmsTimer = _HwBrasSbcIadmsTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 1, 4),
    _HwBrasSbcIadmsTimer_Type()
)
hwBrasSbcIadmsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsTimer.setUnits("minutes")
_HwBrasSbcIadmsTables_ObjectIdentity = ObjectIdentity
hwBrasSbcIadmsTables = _HwBrasSbcIadmsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2)
)
_HwBrasSbcIadmsWellknownPortTable_Object = MibTable
hwBrasSbcIadmsWellknownPortTable = _HwBrasSbcIadmsWellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortTable.setStatus("current")
_HwBrasSbcIadmsWellknownPortEntry_Object = MibTableRow
hwBrasSbcIadmsWellknownPortEntry = _HwBrasSbcIadmsWellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1, 1)
)
hwBrasSbcIadmsWellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsWellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsWellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsWellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortEntry.setStatus("current")


class _HwBrasSbcIadmsWellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcIadmsWellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("iadmsaddr", 2))
    )


_HwBrasSbcIadmsWellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcIadmsWellknownPortIndex_Object = MibTableColumn
hwBrasSbcIadmsWellknownPortIndex = _HwBrasSbcIadmsWellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1, 1, 1),
    _HwBrasSbcIadmsWellknownPortIndex_Type()
)
hwBrasSbcIadmsWellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortIndex.setStatus("current")


class _HwBrasSbcIadmsWellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcIadmsWellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmp", 1)
    )


_HwBrasSbcIadmsWellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIadmsWellknownPortProtocol_Object = MibTableColumn
hwBrasSbcIadmsWellknownPortProtocol = _HwBrasSbcIadmsWellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1, 1, 2),
    _HwBrasSbcIadmsWellknownPortProtocol_Type()
)
hwBrasSbcIadmsWellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortProtocol.setStatus("current")
_HwBrasSbcIadmsWellknownPortAddr_Type = IpAddress
_HwBrasSbcIadmsWellknownPortAddr_Object = MibTableColumn
hwBrasSbcIadmsWellknownPortAddr = _HwBrasSbcIadmsWellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1, 1, 3),
    _HwBrasSbcIadmsWellknownPortAddr_Type()
)
hwBrasSbcIadmsWellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortAddr.setStatus("current")


class _HwBrasSbcIadmsWellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcIadmsWellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcIadmsWellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcIadmsWellknownPortPort_Object = MibTableColumn
hwBrasSbcIadmsWellknownPortPort = _HwBrasSbcIadmsWellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1, 1, 4),
    _HwBrasSbcIadmsWellknownPortPort_Type()
)
hwBrasSbcIadmsWellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortPort.setStatus("current")
_HwBrasSbcIadmsWellknownPortRowStatus_Type = RowStatus
_HwBrasSbcIadmsWellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcIadmsWellknownPortRowStatus = _HwBrasSbcIadmsWellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 1, 1, 5),
    _HwBrasSbcIadmsWellknownPortRowStatus_Type()
)
hwBrasSbcIadmsWellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsWellknownPortRowStatus.setStatus("current")
_HwBrasSbcIadmsMibRegTable_Object = MibTable
hwBrasSbcIadmsMibRegTable = _HwBrasSbcIadmsMibRegTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMibRegTable.setStatus("current")
_HwBrasSbcIadmsMibRegEntry_Object = MibTableRow
hwBrasSbcIadmsMibRegEntry = _HwBrasSbcIadmsMibRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 2, 1)
)
hwBrasSbcIadmsMibRegEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsMibRegVersion"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMibRegEntry.setStatus("current")


class _HwBrasSbcIadmsMibRegVersion_Type(Integer32):
    """Custom type hwBrasSbcIadmsMibRegVersion based on Integer32"""
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
        *(("amend", 1),
          ("v150", 2),
          ("v152", 3),
          ("v160", 4),
          ("v210", 5))
    )


_HwBrasSbcIadmsMibRegVersion_Type.__name__ = "Integer32"
_HwBrasSbcIadmsMibRegVersion_Object = MibTableColumn
hwBrasSbcIadmsMibRegVersion = _HwBrasSbcIadmsMibRegVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 2, 1, 1),
    _HwBrasSbcIadmsMibRegVersion_Type()
)
hwBrasSbcIadmsMibRegVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMibRegVersion.setStatus("current")


class _HwBrasSbcIadmsMibRegRegister_Type(TruthValue):
    """Custom type hwBrasSbcIadmsMibRegRegister based on TruthValue"""


_HwBrasSbcIadmsMibRegRegister_Object = MibTableColumn
hwBrasSbcIadmsMibRegRegister = _HwBrasSbcIadmsMibRegRegister_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 2, 1, 2),
    _HwBrasSbcIadmsMibRegRegister_Type()
)
hwBrasSbcIadmsMibRegRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMibRegRegister.setStatus("current")
_HwBrasSbcIadmsMibRegRowStatus_Type = RowStatus
_HwBrasSbcIadmsMibRegRowStatus_Object = MibTableColumn
hwBrasSbcIadmsMibRegRowStatus = _HwBrasSbcIadmsMibRegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 2, 1, 3),
    _HwBrasSbcIadmsMibRegRowStatus_Type()
)
hwBrasSbcIadmsMibRegRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMibRegRowStatus.setStatus("current")
_HwBrasSbcIadmsSignalMapTable_Object = MibTable
hwBrasSbcIadmsSignalMapTable = _HwBrasSbcIadmsSignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSignalMapTable.setStatus("current")
_HwBrasSbcIadmsSignalMapEntry_Object = MibTableRow
hwBrasSbcIadmsSignalMapEntry = _HwBrasSbcIadmsSignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 3, 1)
)
hwBrasSbcIadmsSignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsSignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsSignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSignalMapEntry.setStatus("current")
_HwBrasSbcIadmsSignalMapAddr_Type = IpAddress
_HwBrasSbcIadmsSignalMapAddr_Object = MibTableColumn
hwBrasSbcIadmsSignalMapAddr = _HwBrasSbcIadmsSignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 3, 1, 1),
    _HwBrasSbcIadmsSignalMapAddr_Type()
)
hwBrasSbcIadmsSignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSignalMapAddr.setStatus("current")


class _HwBrasSbcIadmsSignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcIadmsSignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmp", 1)
    )


_HwBrasSbcIadmsSignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIadmsSignalMapProtocol_Object = MibTableColumn
hwBrasSbcIadmsSignalMapProtocol = _HwBrasSbcIadmsSignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 3, 1, 2),
    _HwBrasSbcIadmsSignalMapProtocol_Type()
)
hwBrasSbcIadmsSignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSignalMapProtocol.setStatus("current")
_HwBrasSbcIadmsSignalMapNumber_Type = Unsigned32
_HwBrasSbcIadmsSignalMapNumber_Object = MibTableColumn
hwBrasSbcIadmsSignalMapNumber = _HwBrasSbcIadmsSignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 3, 1, 3),
    _HwBrasSbcIadmsSignalMapNumber_Type()
)
hwBrasSbcIadmsSignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSignalMapNumber.setStatus("current")


class _HwBrasSbcIadmsSignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcIadmsSignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcIadmsSignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcIadmsSignalMapAddrType_Object = MibTableColumn
hwBrasSbcIadmsSignalMapAddrType = _HwBrasSbcIadmsSignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 3, 1, 4),
    _HwBrasSbcIadmsSignalMapAddrType_Type()
)
hwBrasSbcIadmsSignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsSignalMapAddrType.setStatus("current")
_HwBrasSbcIadmsMediaMapTable_Object = MibTable
hwBrasSbcIadmsMediaMapTable = _HwBrasSbcIadmsMediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMediaMapTable.setStatus("current")
_HwBrasSbcIadmsMediaMapEntry_Object = MibTableRow
hwBrasSbcIadmsMediaMapEntry = _HwBrasSbcIadmsMediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 4, 1)
)
hwBrasSbcIadmsMediaMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsMediaMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsMediaMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMediaMapEntry.setStatus("current")
_HwBrasSbcIadmsMediaMapAddr_Type = IpAddress
_HwBrasSbcIadmsMediaMapAddr_Object = MibTableColumn
hwBrasSbcIadmsMediaMapAddr = _HwBrasSbcIadmsMediaMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 4, 1, 1),
    _HwBrasSbcIadmsMediaMapAddr_Type()
)
hwBrasSbcIadmsMediaMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMediaMapAddr.setStatus("current")


class _HwBrasSbcIadmsMediaMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcIadmsMediaMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmp", 1)
    )


_HwBrasSbcIadmsMediaMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIadmsMediaMapProtocol_Object = MibTableColumn
hwBrasSbcIadmsMediaMapProtocol = _HwBrasSbcIadmsMediaMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 4, 1, 2),
    _HwBrasSbcIadmsMediaMapProtocol_Type()
)
hwBrasSbcIadmsMediaMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMediaMapProtocol.setStatus("current")
_HwBrasSbcIadmsMediaMapNumber_Type = Unsigned32
_HwBrasSbcIadmsMediaMapNumber_Object = MibTableColumn
hwBrasSbcIadmsMediaMapNumber = _HwBrasSbcIadmsMediaMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 4, 1, 3),
    _HwBrasSbcIadmsMediaMapNumber_Type()
)
hwBrasSbcIadmsMediaMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsMediaMapNumber.setStatus("current")
_HwBrasSbcIadmsIntercomMapSignalTable_Object = MibTable
hwBrasSbcIadmsIntercomMapSignalTable = _HwBrasSbcIadmsIntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapSignalTable.setStatus("current")
_HwBrasSbcIadmsIntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcIadmsIntercomMapSignalEntry = _HwBrasSbcIadmsIntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 5, 1)
)
hwBrasSbcIadmsIntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsIntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsIntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapSignalEntry.setStatus("current")
_HwBrasSbcIadmsIntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcIadmsIntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcIadmsIntercomMapSignalAddr = _HwBrasSbcIadmsIntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 5, 1, 1),
    _HwBrasSbcIadmsIntercomMapSignalAddr_Type()
)
hwBrasSbcIadmsIntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcIadmsIntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcIadmsIntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmp", 1)
    )


_HwBrasSbcIadmsIntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIadmsIntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcIadmsIntercomMapSignalProtocol = _HwBrasSbcIadmsIntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 5, 1, 2),
    _HwBrasSbcIadmsIntercomMapSignalProtocol_Type()
)
hwBrasSbcIadmsIntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcIadmsIntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcIadmsIntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcIadmsIntercomMapSignalNumber = _HwBrasSbcIadmsIntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 5, 1, 3),
    _HwBrasSbcIadmsIntercomMapSignalNumber_Type()
)
hwBrasSbcIadmsIntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapSignalNumber.setStatus("current")
_HwBrasSbcIadmsIntercomMapMediaTable_Object = MibTable
hwBrasSbcIadmsIntercomMapMediaTable = _HwBrasSbcIadmsIntercomMapMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapMediaTable.setStatus("current")
_HwBrasSbcIadmsIntercomMapMediaEntry_Object = MibTableRow
hwBrasSbcIadmsIntercomMapMediaEntry = _HwBrasSbcIadmsIntercomMapMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 6, 1)
)
hwBrasSbcIadmsIntercomMapMediaEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsIntercomMapMediaAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsIntercomMapMediaProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapMediaEntry.setStatus("current")
_HwBrasSbcIadmsIntercomMapMediaAddr_Type = IpAddress
_HwBrasSbcIadmsIntercomMapMediaAddr_Object = MibTableColumn
hwBrasSbcIadmsIntercomMapMediaAddr = _HwBrasSbcIadmsIntercomMapMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 6, 1, 1),
    _HwBrasSbcIadmsIntercomMapMediaAddr_Type()
)
hwBrasSbcIadmsIntercomMapMediaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapMediaAddr.setStatus("current")


class _HwBrasSbcIadmsIntercomMapMediaProtocol_Type(Integer32):
    """Custom type hwBrasSbcIadmsIntercomMapMediaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmp", 1)
    )


_HwBrasSbcIadmsIntercomMapMediaProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIadmsIntercomMapMediaProtocol_Object = MibTableColumn
hwBrasSbcIadmsIntercomMapMediaProtocol = _HwBrasSbcIadmsIntercomMapMediaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 6, 1, 2),
    _HwBrasSbcIadmsIntercomMapMediaProtocol_Type()
)
hwBrasSbcIadmsIntercomMapMediaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapMediaProtocol.setStatus("current")
_HwBrasSbcIadmsIntercomMapMediaNumber_Type = Unsigned32
_HwBrasSbcIadmsIntercomMapMediaNumber_Object = MibTableColumn
hwBrasSbcIadmsIntercomMapMediaNumber = _HwBrasSbcIadmsIntercomMapMediaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 6, 1, 3),
    _HwBrasSbcIadmsIntercomMapMediaNumber_Type()
)
hwBrasSbcIadmsIntercomMapMediaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsIntercomMapMediaNumber.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketTable_Object = MibTable
hwBrasSbcIadmsStatSignalPacketTable = _HwBrasSbcIadmsStatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7)
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketTable.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketEntry_Object = MibTableRow
hwBrasSbcIadmsStatSignalPacketEntry = _HwBrasSbcIadmsStatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1)
)
hwBrasSbcIadmsStatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsStatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketEntry.setStatus("current")


class _HwBrasSbcIadmsStatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcIadmsStatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("iadms", 1)
    )


_HwBrasSbcIadmsStatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcIadmsStatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcIadmsStatSignalPacketIndex = _HwBrasSbcIadmsStatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1, 1),
    _HwBrasSbcIadmsStatSignalPacketIndex_Type()
)
hwBrasSbcIadmsStatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketIndex.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketInNumber_Type = Counter64
_HwBrasSbcIadmsStatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcIadmsStatSignalPacketInNumber = _HwBrasSbcIadmsStatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1, 2),
    _HwBrasSbcIadmsStatSignalPacketInNumber_Type()
)
hwBrasSbcIadmsStatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketInNumber.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketInOctet_Type = Counter64
_HwBrasSbcIadmsStatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcIadmsStatSignalPacketInOctet = _HwBrasSbcIadmsStatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1, 3),
    _HwBrasSbcIadmsStatSignalPacketInOctet_Type()
)
hwBrasSbcIadmsStatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketInOctet.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcIadmsStatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcIadmsStatSignalPacketOutNumber = _HwBrasSbcIadmsStatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1, 4),
    _HwBrasSbcIadmsStatSignalPacketOutNumber_Type()
)
hwBrasSbcIadmsStatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcIadmsStatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcIadmsStatSignalPacketOutOctet = _HwBrasSbcIadmsStatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1, 5),
    _HwBrasSbcIadmsStatSignalPacketOutOctet_Type()
)
hwBrasSbcIadmsStatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcIadmsStatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcIadmsStatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcIadmsStatSignalPacketRowStatus = _HwBrasSbcIadmsStatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 4, 2, 7, 1, 6),
    _HwBrasSbcIadmsStatSignalPacketRowStatus_Type()
)
hwBrasSbcIadmsStatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIadmsStatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcH323_ObjectIdentity = ObjectIdentity
hwBrasSbcH323 = _HwBrasSbcH323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5)
)
_HwBrasSbcH323Leaves_ObjectIdentity = ObjectIdentity
hwBrasSbcH323Leaves = _HwBrasSbcH323Leaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 1)
)


class _HwBrasSbcH323Enable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcH323Enable based on HWBrasEnabledStatus"""


_HwBrasSbcH323Enable_Object = MibScalar
hwBrasSbcH323Enable = _HwBrasSbcH323Enable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 1, 1),
    _HwBrasSbcH323Enable_Type()
)
hwBrasSbcH323Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH323Enable.setStatus("current")


class _HwBrasSbcH323SyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcH323SyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcH323SyslogEnable_Object = MibScalar
hwBrasSbcH323SyslogEnable = _HwBrasSbcH323SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 1, 2),
    _HwBrasSbcH323SyslogEnable_Type()
)
hwBrasSbcH323SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH323SyslogEnable.setStatus("current")


class _HwBrasSbcH323CallsessionTimer_Type(Unsigned32):
    """Custom type hwBrasSbcH323CallsessionTimer based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 24),
    )


_HwBrasSbcH323CallsessionTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcH323CallsessionTimer_Object = MibScalar
hwBrasSbcH323CallsessionTimer = _HwBrasSbcH323CallsessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 1, 3),
    _HwBrasSbcH323CallsessionTimer_Type()
)
hwBrasSbcH323CallsessionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH323CallsessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcH323CallsessionTimer.setUnits("hours")


class _HwBrasSbcH323Q931WellknownPort_Type(Unsigned32):
    """Custom type hwBrasSbcH323Q931WellknownPort based on Unsigned32"""
    defaultValue = 1720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49999),
    )


_HwBrasSbcH323Q931WellknownPort_Type.__name__ = "Unsigned32"
_HwBrasSbcH323Q931WellknownPort_Object = MibScalar
hwBrasSbcH323Q931WellknownPort = _HwBrasSbcH323Q931WellknownPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 1, 4),
    _HwBrasSbcH323Q931WellknownPort_Type()
)
hwBrasSbcH323Q931WellknownPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH323Q931WellknownPort.setStatus("current")


class _HwBrasSbcH323PDHCountLimit_Type(Unsigned32):
    """Custom type hwBrasSbcH323PDHCountLimit based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBrasSbcH323PDHCountLimit_Type.__name__ = "Unsigned32"
_HwBrasSbcH323PDHCountLimit_Object = MibScalar
hwBrasSbcH323PDHCountLimit = _HwBrasSbcH323PDHCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 1, 5),
    _HwBrasSbcH323PDHCountLimit_Type()
)
hwBrasSbcH323PDHCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH323PDHCountLimit.setStatus("current")
_HwBrasSbcH323Tables_ObjectIdentity = ObjectIdentity
hwBrasSbcH323Tables = _HwBrasSbcH323Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2)
)
_HwBrasSbcH323WellknownPortTable_Object = MibTable
hwBrasSbcH323WellknownPortTable = _HwBrasSbcH323WellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortTable.setStatus("current")
_HwBrasSbcH323WellknownPortEntry_Object = MibTableRow
hwBrasSbcH323WellknownPortEntry = _HwBrasSbcH323WellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1, 1)
)
hwBrasSbcH323WellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323WellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323WellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323WellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortEntry.setStatus("current")


class _HwBrasSbcH323WellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcH323WellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("softxaddr", 2))
    )


_HwBrasSbcH323WellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcH323WellknownPortIndex_Object = MibTableColumn
hwBrasSbcH323WellknownPortIndex = _HwBrasSbcH323WellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1, 1, 1),
    _HwBrasSbcH323WellknownPortIndex_Type()
)
hwBrasSbcH323WellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortIndex.setStatus("current")


class _HwBrasSbcH323WellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcH323WellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("q931", 2),
          ("ras", 1))
    )


_HwBrasSbcH323WellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH323WellknownPortProtocol_Object = MibTableColumn
hwBrasSbcH323WellknownPortProtocol = _HwBrasSbcH323WellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1, 1, 2),
    _HwBrasSbcH323WellknownPortProtocol_Type()
)
hwBrasSbcH323WellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortProtocol.setStatus("current")
_HwBrasSbcH323WellknownPortAddr_Type = IpAddress
_HwBrasSbcH323WellknownPortAddr_Object = MibTableColumn
hwBrasSbcH323WellknownPortAddr = _HwBrasSbcH323WellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1, 1, 3),
    _HwBrasSbcH323WellknownPortAddr_Type()
)
hwBrasSbcH323WellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortAddr.setStatus("current")


class _HwBrasSbcH323WellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcH323WellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcH323WellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcH323WellknownPortPort_Object = MibTableColumn
hwBrasSbcH323WellknownPortPort = _HwBrasSbcH323WellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1, 1, 4),
    _HwBrasSbcH323WellknownPortPort_Type()
)
hwBrasSbcH323WellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortPort.setStatus("current")
_HwBrasSbcH323WellknownPortRowStatus_Type = RowStatus
_HwBrasSbcH323WellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcH323WellknownPortRowStatus = _HwBrasSbcH323WellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 1, 1, 5),
    _HwBrasSbcH323WellknownPortRowStatus_Type()
)
hwBrasSbcH323WellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcH323WellknownPortRowStatus.setStatus("current")
_HwBrasSbcH323SignalMapTable_Object = MibTable
hwBrasSbcH323SignalMapTable = _HwBrasSbcH323SignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcH323SignalMapTable.setStatus("current")
_HwBrasSbcH323SignalMapEntry_Object = MibTableRow
hwBrasSbcH323SignalMapEntry = _HwBrasSbcH323SignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 2, 1)
)
hwBrasSbcH323SignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323SignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323SignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH323SignalMapEntry.setStatus("current")
_HwBrasSbcH323SignalMapAddr_Type = IpAddress
_HwBrasSbcH323SignalMapAddr_Object = MibTableColumn
hwBrasSbcH323SignalMapAddr = _HwBrasSbcH323SignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 2, 1, 1),
    _HwBrasSbcH323SignalMapAddr_Type()
)
hwBrasSbcH323SignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323SignalMapAddr.setStatus("current")


class _HwBrasSbcH323SignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcH323SignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h245", 3),
          ("q931", 2),
          ("ras", 1))
    )


_HwBrasSbcH323SignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH323SignalMapProtocol_Object = MibTableColumn
hwBrasSbcH323SignalMapProtocol = _HwBrasSbcH323SignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 2, 1, 2),
    _HwBrasSbcH323SignalMapProtocol_Type()
)
hwBrasSbcH323SignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323SignalMapProtocol.setStatus("current")
_HwBrasSbcH323SignalMapNumber_Type = Unsigned32
_HwBrasSbcH323SignalMapNumber_Object = MibTableColumn
hwBrasSbcH323SignalMapNumber = _HwBrasSbcH323SignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 2, 1, 3),
    _HwBrasSbcH323SignalMapNumber_Type()
)
hwBrasSbcH323SignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323SignalMapNumber.setStatus("current")


class _HwBrasSbcH323SignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcH323SignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcH323SignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcH323SignalMapAddrType_Object = MibTableColumn
hwBrasSbcH323SignalMapAddrType = _HwBrasSbcH323SignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 2, 1, 4),
    _HwBrasSbcH323SignalMapAddrType_Type()
)
hwBrasSbcH323SignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323SignalMapAddrType.setStatus("current")
_HwBrasSbcH323MediaMapTable_Object = MibTable
hwBrasSbcH323MediaMapTable = _HwBrasSbcH323MediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcH323MediaMapTable.setStatus("current")
_HwBrasSbcH323MediaMapEntry_Object = MibTableRow
hwBrasSbcH323MediaMapEntry = _HwBrasSbcH323MediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 3, 1)
)
hwBrasSbcH323MediaMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323MediaMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323MediaMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH323MediaMapEntry.setStatus("current")
_HwBrasSbcH323MediaMapAddr_Type = IpAddress
_HwBrasSbcH323MediaMapAddr_Object = MibTableColumn
hwBrasSbcH323MediaMapAddr = _HwBrasSbcH323MediaMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 3, 1, 1),
    _HwBrasSbcH323MediaMapAddr_Type()
)
hwBrasSbcH323MediaMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323MediaMapAddr.setStatus("current")


class _HwBrasSbcH323MediaMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcH323MediaMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h323", 1)
    )


_HwBrasSbcH323MediaMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH323MediaMapProtocol_Object = MibTableColumn
hwBrasSbcH323MediaMapProtocol = _HwBrasSbcH323MediaMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 3, 1, 2),
    _HwBrasSbcH323MediaMapProtocol_Type()
)
hwBrasSbcH323MediaMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323MediaMapProtocol.setStatus("current")
_HwBrasSbcH323MediaMapNumber_Type = Unsigned32
_HwBrasSbcH323MediaMapNumber_Object = MibTableColumn
hwBrasSbcH323MediaMapNumber = _HwBrasSbcH323MediaMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 3, 1, 3),
    _HwBrasSbcH323MediaMapNumber_Type()
)
hwBrasSbcH323MediaMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323MediaMapNumber.setStatus("current")
_HwBrasSbcH323IntercomMapSignalTable_Object = MibTable
hwBrasSbcH323IntercomMapSignalTable = _HwBrasSbcH323IntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapSignalTable.setStatus("current")
_HwBrasSbcH323IntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcH323IntercomMapSignalEntry = _HwBrasSbcH323IntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 4, 1)
)
hwBrasSbcH323IntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323IntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323IntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapSignalEntry.setStatus("current")
_HwBrasSbcH323IntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcH323IntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcH323IntercomMapSignalAddr = _HwBrasSbcH323IntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 4, 1, 1),
    _HwBrasSbcH323IntercomMapSignalAddr_Type()
)
hwBrasSbcH323IntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcH323IntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcH323IntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h245", 3),
          ("q931", 2),
          ("ras", 1))
    )


_HwBrasSbcH323IntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH323IntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcH323IntercomMapSignalProtocol = _HwBrasSbcH323IntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 4, 1, 2),
    _HwBrasSbcH323IntercomMapSignalProtocol_Type()
)
hwBrasSbcH323IntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcH323IntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcH323IntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcH323IntercomMapSignalNumber = _HwBrasSbcH323IntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 4, 1, 3),
    _HwBrasSbcH323IntercomMapSignalNumber_Type()
)
hwBrasSbcH323IntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapSignalNumber.setStatus("current")
_HwBrasSbcH323IntercomMapMediaTable_Object = MibTable
hwBrasSbcH323IntercomMapMediaTable = _HwBrasSbcH323IntercomMapMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapMediaTable.setStatus("current")
_HwBrasSbcH323IntercomMapMediaEntry_Object = MibTableRow
hwBrasSbcH323IntercomMapMediaEntry = _HwBrasSbcH323IntercomMapMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 5, 1)
)
hwBrasSbcH323IntercomMapMediaEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323IntercomMapMediaAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323IntercomMapMediaProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapMediaEntry.setStatus("current")
_HwBrasSbcH323IntercomMapMediaAddr_Type = IpAddress
_HwBrasSbcH323IntercomMapMediaAddr_Object = MibTableColumn
hwBrasSbcH323IntercomMapMediaAddr = _HwBrasSbcH323IntercomMapMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 5, 1, 1),
    _HwBrasSbcH323IntercomMapMediaAddr_Type()
)
hwBrasSbcH323IntercomMapMediaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapMediaAddr.setStatus("current")


class _HwBrasSbcH323IntercomMapMediaProtocol_Type(Integer32):
    """Custom type hwBrasSbcH323IntercomMapMediaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h323", 1)
    )


_HwBrasSbcH323IntercomMapMediaProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH323IntercomMapMediaProtocol_Object = MibTableColumn
hwBrasSbcH323IntercomMapMediaProtocol = _HwBrasSbcH323IntercomMapMediaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 5, 1, 2),
    _HwBrasSbcH323IntercomMapMediaProtocol_Type()
)
hwBrasSbcH323IntercomMapMediaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapMediaProtocol.setStatus("current")
_HwBrasSbcH323IntercomMapMediaNumber_Type = Unsigned32
_HwBrasSbcH323IntercomMapMediaNumber_Object = MibTableColumn
hwBrasSbcH323IntercomMapMediaNumber = _HwBrasSbcH323IntercomMapMediaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 5, 1, 3),
    _HwBrasSbcH323IntercomMapMediaNumber_Type()
)
hwBrasSbcH323IntercomMapMediaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323IntercomMapMediaNumber.setStatus("current")
_HwBrasSbcH323StatSignalPacketTable_Object = MibTable
hwBrasSbcH323StatSignalPacketTable = _HwBrasSbcH323StatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketTable.setStatus("current")
_HwBrasSbcH323StatSignalPacketEntry_Object = MibTableRow
hwBrasSbcH323StatSignalPacketEntry = _HwBrasSbcH323StatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1)
)
hwBrasSbcH323StatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323StatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketEntry.setStatus("current")


class _HwBrasSbcH323StatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcH323StatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h323", 1)
    )


_HwBrasSbcH323StatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcH323StatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcH323StatSignalPacketIndex = _HwBrasSbcH323StatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1, 1),
    _HwBrasSbcH323StatSignalPacketIndex_Type()
)
hwBrasSbcH323StatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketIndex.setStatus("current")
_HwBrasSbcH323StatSignalPacketInNumber_Type = Counter64
_HwBrasSbcH323StatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcH323StatSignalPacketInNumber = _HwBrasSbcH323StatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1, 2),
    _HwBrasSbcH323StatSignalPacketInNumber_Type()
)
hwBrasSbcH323StatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketInNumber.setStatus("current")
_HwBrasSbcH323StatSignalPacketInOctet_Type = Counter64
_HwBrasSbcH323StatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcH323StatSignalPacketInOctet = _HwBrasSbcH323StatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1, 3),
    _HwBrasSbcH323StatSignalPacketInOctet_Type()
)
hwBrasSbcH323StatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketInOctet.setStatus("current")
_HwBrasSbcH323StatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcH323StatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcH323StatSignalPacketOutNumber = _HwBrasSbcH323StatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1, 4),
    _HwBrasSbcH323StatSignalPacketOutNumber_Type()
)
hwBrasSbcH323StatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcH323StatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcH323StatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcH323StatSignalPacketOutOctet = _HwBrasSbcH323StatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1, 5),
    _HwBrasSbcH323StatSignalPacketOutOctet_Type()
)
hwBrasSbcH323StatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcH323StatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcH323StatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcH323StatSignalPacketRowStatus = _HwBrasSbcH323StatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 5, 2, 6, 1, 6),
    _HwBrasSbcH323StatSignalPacketRowStatus_Type()
)
hwBrasSbcH323StatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH323StatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcIdo_ObjectIdentity = ObjectIdentity
hwBrasSbcIdo = _HwBrasSbcIdo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6)
)
_HwBrasSbcIdoLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcIdoLeaves = _HwBrasSbcIdoLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 1)
)


class _HwBrasSbcIdoEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIdoEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIdoEnable_Object = MibScalar
hwBrasSbcIdoEnable = _HwBrasSbcIdoEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 1, 1),
    _HwBrasSbcIdoEnable_Type()
)
hwBrasSbcIdoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIdoEnable.setStatus("current")


class _HwBrasSbcIdoSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcIdoSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcIdoSyslogEnable_Object = MibScalar
hwBrasSbcIdoSyslogEnable = _HwBrasSbcIdoSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 1, 2),
    _HwBrasSbcIdoSyslogEnable_Type()
)
hwBrasSbcIdoSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIdoSyslogEnable.setStatus("current")
_HwBrasSbcIdoTables_ObjectIdentity = ObjectIdentity
hwBrasSbcIdoTables = _HwBrasSbcIdoTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2)
)
_HwBrasSbcIdoWellknownPortTable_Object = MibTable
hwBrasSbcIdoWellknownPortTable = _HwBrasSbcIdoWellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortTable.setStatus("current")
_HwBrasSbcIdoWellknownPortEntry_Object = MibTableRow
hwBrasSbcIdoWellknownPortEntry = _HwBrasSbcIdoWellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1, 1)
)
hwBrasSbcIdoWellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoWellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoWellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoWellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortEntry.setStatus("current")


class _HwBrasSbcIdoWellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcIdoWellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("softxaddr", 2))
    )


_HwBrasSbcIdoWellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcIdoWellknownPortIndex_Object = MibTableColumn
hwBrasSbcIdoWellknownPortIndex = _HwBrasSbcIdoWellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1, 1, 1),
    _HwBrasSbcIdoWellknownPortIndex_Type()
)
hwBrasSbcIdoWellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortIndex.setStatus("current")


class _HwBrasSbcIdoWellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcIdoWellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ido", 1)
    )


_HwBrasSbcIdoWellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIdoWellknownPortProtocol_Object = MibTableColumn
hwBrasSbcIdoWellknownPortProtocol = _HwBrasSbcIdoWellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1, 1, 2),
    _HwBrasSbcIdoWellknownPortProtocol_Type()
)
hwBrasSbcIdoWellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortProtocol.setStatus("current")
_HwBrasSbcIdoWellknownPortAddr_Type = IpAddress
_HwBrasSbcIdoWellknownPortAddr_Object = MibTableColumn
hwBrasSbcIdoWellknownPortAddr = _HwBrasSbcIdoWellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1, 1, 3),
    _HwBrasSbcIdoWellknownPortAddr_Type()
)
hwBrasSbcIdoWellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortAddr.setStatus("current")


class _HwBrasSbcIdoWellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcIdoWellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcIdoWellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcIdoWellknownPortPort_Object = MibTableColumn
hwBrasSbcIdoWellknownPortPort = _HwBrasSbcIdoWellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1, 1, 4),
    _HwBrasSbcIdoWellknownPortPort_Type()
)
hwBrasSbcIdoWellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortPort.setStatus("current")
_HwBrasSbcIdoWellknownPortRowStatus_Type = RowStatus
_HwBrasSbcIdoWellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcIdoWellknownPortRowStatus = _HwBrasSbcIdoWellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 1, 1, 5),
    _HwBrasSbcIdoWellknownPortRowStatus_Type()
)
hwBrasSbcIdoWellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcIdoWellknownPortRowStatus.setStatus("current")
_HwBrasSbcIdoSignalMapTable_Object = MibTable
hwBrasSbcIdoSignalMapTable = _HwBrasSbcIdoSignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoSignalMapTable.setStatus("current")
_HwBrasSbcIdoSignalMapEntry_Object = MibTableRow
hwBrasSbcIdoSignalMapEntry = _HwBrasSbcIdoSignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 2, 1)
)
hwBrasSbcIdoSignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoSignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoSignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoSignalMapEntry.setStatus("current")
_HwBrasSbcIdoSignalMapAddr_Type = IpAddress
_HwBrasSbcIdoSignalMapAddr_Object = MibTableColumn
hwBrasSbcIdoSignalMapAddr = _HwBrasSbcIdoSignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 2, 1, 1),
    _HwBrasSbcIdoSignalMapAddr_Type()
)
hwBrasSbcIdoSignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoSignalMapAddr.setStatus("current")


class _HwBrasSbcIdoSignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcIdoSignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ido", 1)
    )


_HwBrasSbcIdoSignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIdoSignalMapProtocol_Object = MibTableColumn
hwBrasSbcIdoSignalMapProtocol = _HwBrasSbcIdoSignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 2, 1, 2),
    _HwBrasSbcIdoSignalMapProtocol_Type()
)
hwBrasSbcIdoSignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoSignalMapProtocol.setStatus("current")
_HwBrasSbcIdoSignalMapNumber_Type = Unsigned32
_HwBrasSbcIdoSignalMapNumber_Object = MibTableColumn
hwBrasSbcIdoSignalMapNumber = _HwBrasSbcIdoSignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 2, 1, 3),
    _HwBrasSbcIdoSignalMapNumber_Type()
)
hwBrasSbcIdoSignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoSignalMapNumber.setStatus("current")


class _HwBrasSbcIdoSignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcIdoSignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcIdoSignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcIdoSignalMapAddrType_Object = MibTableColumn
hwBrasSbcIdoSignalMapAddrType = _HwBrasSbcIdoSignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 2, 1, 4),
    _HwBrasSbcIdoSignalMapAddrType_Type()
)
hwBrasSbcIdoSignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoSignalMapAddrType.setStatus("current")
_HwBrasSbcIdoIntercomMapSignalTable_Object = MibTable
hwBrasSbcIdoIntercomMapSignalTable = _HwBrasSbcIdoIntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoIntercomMapSignalTable.setStatus("current")
_HwBrasSbcIdoIntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcIdoIntercomMapSignalEntry = _HwBrasSbcIdoIntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 3, 1)
)
hwBrasSbcIdoIntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoIntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoIntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoIntercomMapSignalEntry.setStatus("current")
_HwBrasSbcIdoIntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcIdoIntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcIdoIntercomMapSignalAddr = _HwBrasSbcIdoIntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 3, 1, 1),
    _HwBrasSbcIdoIntercomMapSignalAddr_Type()
)
hwBrasSbcIdoIntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoIntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcIdoIntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcIdoIntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ido", 1)
    )


_HwBrasSbcIdoIntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcIdoIntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcIdoIntercomMapSignalProtocol = _HwBrasSbcIdoIntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 3, 1, 2),
    _HwBrasSbcIdoIntercomMapSignalProtocol_Type()
)
hwBrasSbcIdoIntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoIntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcIdoIntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcIdoIntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcIdoIntercomMapSignalNumber = _HwBrasSbcIdoIntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 3, 1, 3),
    _HwBrasSbcIdoIntercomMapSignalNumber_Type()
)
hwBrasSbcIdoIntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoIntercomMapSignalNumber.setStatus("current")
_HwBrasSbcIdoStatSignalPacketTable_Object = MibTable
hwBrasSbcIdoStatSignalPacketTable = _HwBrasSbcIdoStatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketTable.setStatus("current")
_HwBrasSbcIdoStatSignalPacketEntry_Object = MibTableRow
hwBrasSbcIdoStatSignalPacketEntry = _HwBrasSbcIdoStatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1)
)
hwBrasSbcIdoStatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoStatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketEntry.setStatus("current")


class _HwBrasSbcIdoStatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcIdoStatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ido", 1)
    )


_HwBrasSbcIdoStatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcIdoStatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcIdoStatSignalPacketIndex = _HwBrasSbcIdoStatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1, 1),
    _HwBrasSbcIdoStatSignalPacketIndex_Type()
)
hwBrasSbcIdoStatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketIndex.setStatus("current")
_HwBrasSbcIdoStatSignalPacketInNumber_Type = Counter64
_HwBrasSbcIdoStatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcIdoStatSignalPacketInNumber = _HwBrasSbcIdoStatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1, 2),
    _HwBrasSbcIdoStatSignalPacketInNumber_Type()
)
hwBrasSbcIdoStatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketInNumber.setStatus("current")
_HwBrasSbcIdoStatSignalPacketInOctet_Type = Counter64
_HwBrasSbcIdoStatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcIdoStatSignalPacketInOctet = _HwBrasSbcIdoStatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1, 3),
    _HwBrasSbcIdoStatSignalPacketInOctet_Type()
)
hwBrasSbcIdoStatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketInOctet.setStatus("current")
_HwBrasSbcIdoStatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcIdoStatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcIdoStatSignalPacketOutNumber = _HwBrasSbcIdoStatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1, 4),
    _HwBrasSbcIdoStatSignalPacketOutNumber_Type()
)
hwBrasSbcIdoStatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcIdoStatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcIdoStatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcIdoStatSignalPacketOutOctet = _HwBrasSbcIdoStatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1, 5),
    _HwBrasSbcIdoStatSignalPacketOutOctet_Type()
)
hwBrasSbcIdoStatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcIdoStatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcIdoStatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcIdoStatSignalPacketRowStatus = _HwBrasSbcIdoStatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 6, 2, 4, 1, 6),
    _HwBrasSbcIdoStatSignalPacketRowStatus_Type()
)
hwBrasSbcIdoStatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcIdoStatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcH248_ObjectIdentity = ObjectIdentity
hwBrasSbcH248 = _HwBrasSbcH248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7)
)
_HwBrasSbcH248Leaves_ObjectIdentity = ObjectIdentity
hwBrasSbcH248Leaves = _HwBrasSbcH248Leaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 1)
)


class _HwBrasSbcH248Enable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcH248Enable based on HWBrasEnabledStatus"""


_HwBrasSbcH248Enable_Object = MibScalar
hwBrasSbcH248Enable = _HwBrasSbcH248Enable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 1, 1),
    _HwBrasSbcH248Enable_Type()
)
hwBrasSbcH248Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH248Enable.setStatus("current")


class _HwBrasSbcH248SyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcH248SyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcH248SyslogEnable_Object = MibScalar
hwBrasSbcH248SyslogEnable = _HwBrasSbcH248SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 1, 2),
    _HwBrasSbcH248SyslogEnable_Type()
)
hwBrasSbcH248SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH248SyslogEnable.setStatus("current")


class _HwBrasSbcH248CcbTimer_Type(Unsigned32):
    """Custom type hwBrasSbcH248CcbTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14400),
    )


_HwBrasSbcH248CcbTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcH248CcbTimer_Object = MibScalar
hwBrasSbcH248CcbTimer = _HwBrasSbcH248CcbTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 1, 3),
    _HwBrasSbcH248CcbTimer_Type()
)
hwBrasSbcH248CcbTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH248CcbTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcH248CcbTimer.setUnits("minutes")


class _HwBrasSbcH248UserAgeTimer_Type(Unsigned32):
    """Custom type hwBrasSbcH248UserAgeTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HwBrasSbcH248UserAgeTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcH248UserAgeTimer_Object = MibScalar
hwBrasSbcH248UserAgeTimer = _HwBrasSbcH248UserAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 1, 4),
    _HwBrasSbcH248UserAgeTimer_Type()
)
hwBrasSbcH248UserAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH248UserAgeTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcH248UserAgeTimer.setUnits("seconds")


class _HwBrasSbcH248PDHCountLimit_Type(Unsigned32):
    """Custom type hwBrasSbcH248PDHCountLimit based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBrasSbcH248PDHCountLimit_Type.__name__ = "Unsigned32"
_HwBrasSbcH248PDHCountLimit_Object = MibScalar
hwBrasSbcH248PDHCountLimit = _HwBrasSbcH248PDHCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 1, 5),
    _HwBrasSbcH248PDHCountLimit_Type()
)
hwBrasSbcH248PDHCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH248PDHCountLimit.setStatus("current")
_HwBrasSbcH248Tables_ObjectIdentity = ObjectIdentity
hwBrasSbcH248Tables = _HwBrasSbcH248Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2)
)
_HwBrasSbcH248WellknownPortTable_Object = MibTable
hwBrasSbcH248WellknownPortTable = _HwBrasSbcH248WellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortTable.setStatus("current")
_HwBrasSbcH248WellknownPortEntry_Object = MibTableRow
hwBrasSbcH248WellknownPortEntry = _HwBrasSbcH248WellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1, 1)
)
hwBrasSbcH248WellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248WellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248WellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248WellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortEntry.setStatus("current")


class _HwBrasSbcH248WellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcH248WellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("softxaddr", 2))
    )


_HwBrasSbcH248WellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcH248WellknownPortIndex_Object = MibTableColumn
hwBrasSbcH248WellknownPortIndex = _HwBrasSbcH248WellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1, 1, 1),
    _HwBrasSbcH248WellknownPortIndex_Type()
)
hwBrasSbcH248WellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortIndex.setStatus("current")


class _HwBrasSbcH248WellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcH248WellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h248", 1)
    )


_HwBrasSbcH248WellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH248WellknownPortProtocol_Object = MibTableColumn
hwBrasSbcH248WellknownPortProtocol = _HwBrasSbcH248WellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1, 1, 2),
    _HwBrasSbcH248WellknownPortProtocol_Type()
)
hwBrasSbcH248WellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortProtocol.setStatus("current")
_HwBrasSbcH248WellknownPortAddr_Type = IpAddress
_HwBrasSbcH248WellknownPortAddr_Object = MibTableColumn
hwBrasSbcH248WellknownPortAddr = _HwBrasSbcH248WellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1, 1, 3),
    _HwBrasSbcH248WellknownPortAddr_Type()
)
hwBrasSbcH248WellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortAddr.setStatus("current")


class _HwBrasSbcH248WellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcH248WellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcH248WellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcH248WellknownPortPort_Object = MibTableColumn
hwBrasSbcH248WellknownPortPort = _HwBrasSbcH248WellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1, 1, 4),
    _HwBrasSbcH248WellknownPortPort_Type()
)
hwBrasSbcH248WellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortPort.setStatus("current")
_HwBrasSbcH248WellknownPortRowStatus_Type = RowStatus
_HwBrasSbcH248WellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcH248WellknownPortRowStatus = _HwBrasSbcH248WellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 1, 1, 5),
    _HwBrasSbcH248WellknownPortRowStatus_Type()
)
hwBrasSbcH248WellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcH248WellknownPortRowStatus.setStatus("current")
_HwBrasSbcH248SignalMapTable_Object = MibTable
hwBrasSbcH248SignalMapTable = _HwBrasSbcH248SignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcH248SignalMapTable.setStatus("current")
_HwBrasSbcH248SignalMapEntry_Object = MibTableRow
hwBrasSbcH248SignalMapEntry = _HwBrasSbcH248SignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 2, 1)
)
hwBrasSbcH248SignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248SignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248SignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH248SignalMapEntry.setStatus("current")
_HwBrasSbcH248SignalMapAddr_Type = IpAddress
_HwBrasSbcH248SignalMapAddr_Object = MibTableColumn
hwBrasSbcH248SignalMapAddr = _HwBrasSbcH248SignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 2, 1, 1),
    _HwBrasSbcH248SignalMapAddr_Type()
)
hwBrasSbcH248SignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248SignalMapAddr.setStatus("current")


class _HwBrasSbcH248SignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcH248SignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h248", 1)
    )


_HwBrasSbcH248SignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH248SignalMapProtocol_Object = MibTableColumn
hwBrasSbcH248SignalMapProtocol = _HwBrasSbcH248SignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 2, 1, 2),
    _HwBrasSbcH248SignalMapProtocol_Type()
)
hwBrasSbcH248SignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248SignalMapProtocol.setStatus("current")
_HwBrasSbcH248SignalMapNumber_Type = Unsigned32
_HwBrasSbcH248SignalMapNumber_Object = MibTableColumn
hwBrasSbcH248SignalMapNumber = _HwBrasSbcH248SignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 2, 1, 3),
    _HwBrasSbcH248SignalMapNumber_Type()
)
hwBrasSbcH248SignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248SignalMapNumber.setStatus("current")


class _HwBrasSbcH248SignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcH248SignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcH248SignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcH248SignalMapAddrType_Object = MibTableColumn
hwBrasSbcH248SignalMapAddrType = _HwBrasSbcH248SignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 2, 1, 4),
    _HwBrasSbcH248SignalMapAddrType_Type()
)
hwBrasSbcH248SignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248SignalMapAddrType.setStatus("current")
_HwBrasSbcH248MediaMapTable_Object = MibTable
hwBrasSbcH248MediaMapTable = _HwBrasSbcH248MediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcH248MediaMapTable.setStatus("current")
_HwBrasSbcH248MediaMapEntry_Object = MibTableRow
hwBrasSbcH248MediaMapEntry = _HwBrasSbcH248MediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 3, 1)
)
hwBrasSbcH248MediaMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248MediaMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248MediaMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH248MediaMapEntry.setStatus("current")
_HwBrasSbcH248MediaMapAddr_Type = IpAddress
_HwBrasSbcH248MediaMapAddr_Object = MibTableColumn
hwBrasSbcH248MediaMapAddr = _HwBrasSbcH248MediaMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 3, 1, 1),
    _HwBrasSbcH248MediaMapAddr_Type()
)
hwBrasSbcH248MediaMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248MediaMapAddr.setStatus("current")


class _HwBrasSbcH248MediaMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcH248MediaMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h248", 1)
    )


_HwBrasSbcH248MediaMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH248MediaMapProtocol_Object = MibTableColumn
hwBrasSbcH248MediaMapProtocol = _HwBrasSbcH248MediaMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 3, 1, 2),
    _HwBrasSbcH248MediaMapProtocol_Type()
)
hwBrasSbcH248MediaMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248MediaMapProtocol.setStatus("current")
_HwBrasSbcH248MediaMapNumber_Type = Unsigned32
_HwBrasSbcH248MediaMapNumber_Object = MibTableColumn
hwBrasSbcH248MediaMapNumber = _HwBrasSbcH248MediaMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 3, 1, 3),
    _HwBrasSbcH248MediaMapNumber_Type()
)
hwBrasSbcH248MediaMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248MediaMapNumber.setStatus("current")
_HwBrasSbcH248IntercomMapSignalTable_Object = MibTable
hwBrasSbcH248IntercomMapSignalTable = _HwBrasSbcH248IntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapSignalTable.setStatus("current")
_HwBrasSbcH248IntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcH248IntercomMapSignalEntry = _HwBrasSbcH248IntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 4, 1)
)
hwBrasSbcH248IntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248IntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248IntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapSignalEntry.setStatus("current")
_HwBrasSbcH248IntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcH248IntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcH248IntercomMapSignalAddr = _HwBrasSbcH248IntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 4, 1, 1),
    _HwBrasSbcH248IntercomMapSignalAddr_Type()
)
hwBrasSbcH248IntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcH248IntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcH248IntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h248", 1)
    )


_HwBrasSbcH248IntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH248IntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcH248IntercomMapSignalProtocol = _HwBrasSbcH248IntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 4, 1, 2),
    _HwBrasSbcH248IntercomMapSignalProtocol_Type()
)
hwBrasSbcH248IntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcH248IntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcH248IntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcH248IntercomMapSignalNumber = _HwBrasSbcH248IntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 4, 1, 3),
    _HwBrasSbcH248IntercomMapSignalNumber_Type()
)
hwBrasSbcH248IntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapSignalNumber.setStatus("current")
_HwBrasSbcH248IntercomMapMediaTable_Object = MibTable
hwBrasSbcH248IntercomMapMediaTable = _HwBrasSbcH248IntercomMapMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapMediaTable.setStatus("current")
_HwBrasSbcH248IntercomMapMediaEntry_Object = MibTableRow
hwBrasSbcH248IntercomMapMediaEntry = _HwBrasSbcH248IntercomMapMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 5, 1)
)
hwBrasSbcH248IntercomMapMediaEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248IntercomMapMediaAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248IntercomMapMediaProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapMediaEntry.setStatus("current")
_HwBrasSbcH248IntercomMapMediaAddr_Type = IpAddress
_HwBrasSbcH248IntercomMapMediaAddr_Object = MibTableColumn
hwBrasSbcH248IntercomMapMediaAddr = _HwBrasSbcH248IntercomMapMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 5, 1, 1),
    _HwBrasSbcH248IntercomMapMediaAddr_Type()
)
hwBrasSbcH248IntercomMapMediaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapMediaAddr.setStatus("current")


class _HwBrasSbcH248IntercomMapMediaProtocol_Type(Integer32):
    """Custom type hwBrasSbcH248IntercomMapMediaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h248", 1)
    )


_HwBrasSbcH248IntercomMapMediaProtocol_Type.__name__ = "Integer32"
_HwBrasSbcH248IntercomMapMediaProtocol_Object = MibTableColumn
hwBrasSbcH248IntercomMapMediaProtocol = _HwBrasSbcH248IntercomMapMediaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 5, 1, 2),
    _HwBrasSbcH248IntercomMapMediaProtocol_Type()
)
hwBrasSbcH248IntercomMapMediaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapMediaProtocol.setStatus("current")
_HwBrasSbcH248IntercomMapMediaNumber_Type = Unsigned32
_HwBrasSbcH248IntercomMapMediaNumber_Object = MibTableColumn
hwBrasSbcH248IntercomMapMediaNumber = _HwBrasSbcH248IntercomMapMediaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 5, 1, 3),
    _HwBrasSbcH248IntercomMapMediaNumber_Type()
)
hwBrasSbcH248IntercomMapMediaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248IntercomMapMediaNumber.setStatus("current")
_HwBrasSbcH248StatSignalPacketTable_Object = MibTable
hwBrasSbcH248StatSignalPacketTable = _HwBrasSbcH248StatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketTable.setStatus("current")
_HwBrasSbcH248StatSignalPacketEntry_Object = MibTableRow
hwBrasSbcH248StatSignalPacketEntry = _HwBrasSbcH248StatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1)
)
hwBrasSbcH248StatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248StatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketEntry.setStatus("current")


class _HwBrasSbcH248StatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcH248StatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h248", 1)
    )


_HwBrasSbcH248StatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcH248StatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcH248StatSignalPacketIndex = _HwBrasSbcH248StatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1, 1),
    _HwBrasSbcH248StatSignalPacketIndex_Type()
)
hwBrasSbcH248StatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketIndex.setStatus("current")
_HwBrasSbcH248StatSignalPacketInNumber_Type = Counter64
_HwBrasSbcH248StatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcH248StatSignalPacketInNumber = _HwBrasSbcH248StatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1, 2),
    _HwBrasSbcH248StatSignalPacketInNumber_Type()
)
hwBrasSbcH248StatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketInNumber.setStatus("current")
_HwBrasSbcH248StatSignalPacketInOctet_Type = Counter64
_HwBrasSbcH248StatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcH248StatSignalPacketInOctet = _HwBrasSbcH248StatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1, 3),
    _HwBrasSbcH248StatSignalPacketInOctet_Type()
)
hwBrasSbcH248StatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketInOctet.setStatus("current")
_HwBrasSbcH248StatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcH248StatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcH248StatSignalPacketOutNumber = _HwBrasSbcH248StatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1, 4),
    _HwBrasSbcH248StatSignalPacketOutNumber_Type()
)
hwBrasSbcH248StatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcH248StatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcH248StatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcH248StatSignalPacketOutOctet = _HwBrasSbcH248StatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1, 5),
    _HwBrasSbcH248StatSignalPacketOutOctet_Type()
)
hwBrasSbcH248StatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcH248StatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcH248StatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcH248StatSignalPacketRowStatus = _HwBrasSbcH248StatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 7, 2, 6, 1, 6),
    _HwBrasSbcH248StatSignalPacketRowStatus_Type()
)
hwBrasSbcH248StatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcH248StatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcUpath_ObjectIdentity = ObjectIdentity
hwBrasSbcUpath = _HwBrasSbcUpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8)
)
_HwBrasSbcUpathLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcUpathLeaves = _HwBrasSbcUpathLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 2)
)


class _HwBrasSbcUpathEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcUpathEnable based on HWBrasEnabledStatus"""


_HwBrasSbcUpathEnable_Object = MibScalar
hwBrasSbcUpathEnable = _HwBrasSbcUpathEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 2, 1),
    _HwBrasSbcUpathEnable_Type()
)
hwBrasSbcUpathEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUpathEnable.setStatus("current")


class _HwBrasSbcUpathSyslogEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcUpathSyslogEnable based on HWBrasEnabledStatus"""


_HwBrasSbcUpathSyslogEnable_Object = MibScalar
hwBrasSbcUpathSyslogEnable = _HwBrasSbcUpathSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 2, 2),
    _HwBrasSbcUpathSyslogEnable_Type()
)
hwBrasSbcUpathSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUpathSyslogEnable.setStatus("current")


class _HwBrasSbcUpathCallsessionTimer_Type(Unsigned32):
    """Custom type hwBrasSbcUpathCallsessionTimer based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_HwBrasSbcUpathCallsessionTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcUpathCallsessionTimer_Object = MibScalar
hwBrasSbcUpathCallsessionTimer = _HwBrasSbcUpathCallsessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 2, 3),
    _HwBrasSbcUpathCallsessionTimer_Type()
)
hwBrasSbcUpathCallsessionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUpathCallsessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcUpathCallsessionTimer.setUnits("hours")


class _HwBrasSbcUpathHeartbeatTimer_Type(Unsigned32):
    """Custom type hwBrasSbcUpathHeartbeatTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_HwBrasSbcUpathHeartbeatTimer_Type.__name__ = "Unsigned32"
_HwBrasSbcUpathHeartbeatTimer_Object = MibScalar
hwBrasSbcUpathHeartbeatTimer = _HwBrasSbcUpathHeartbeatTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 2, 4),
    _HwBrasSbcUpathHeartbeatTimer_Type()
)
hwBrasSbcUpathHeartbeatTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUpathHeartbeatTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwBrasSbcUpathHeartbeatTimer.setUnits("seconds")
_HwBrasSbcUpathTables_ObjectIdentity = ObjectIdentity
hwBrasSbcUpathTables = _HwBrasSbcUpathTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3)
)
_HwBrasSbcUpathWellknownPortTable_Object = MibTable
hwBrasSbcUpathWellknownPortTable = _HwBrasSbcUpathWellknownPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortTable.setStatus("current")
_HwBrasSbcUpathWellknownPortEntry_Object = MibTableRow
hwBrasSbcUpathWellknownPortEntry = _HwBrasSbcUpathWellknownPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1, 1)
)
hwBrasSbcUpathWellknownPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathWellknownPortIndex"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathWellknownPortProtocol"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathWellknownPortAddr"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortEntry.setStatus("current")


class _HwBrasSbcUpathWellknownPortIndex_Type(Integer32):
    """Custom type hwBrasSbcUpathWellknownPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientaddr", 1),
          ("softxaddr", 2))
    )


_HwBrasSbcUpathWellknownPortIndex_Type.__name__ = "Integer32"
_HwBrasSbcUpathWellknownPortIndex_Object = MibTableColumn
hwBrasSbcUpathWellknownPortIndex = _HwBrasSbcUpathWellknownPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1, 1, 1),
    _HwBrasSbcUpathWellknownPortIndex_Type()
)
hwBrasSbcUpathWellknownPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortIndex.setStatus("current")


class _HwBrasSbcUpathWellknownPortProtocol_Type(Integer32):
    """Custom type hwBrasSbcUpathWellknownPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upath", 1)
    )


_HwBrasSbcUpathWellknownPortProtocol_Type.__name__ = "Integer32"
_HwBrasSbcUpathWellknownPortProtocol_Object = MibTableColumn
hwBrasSbcUpathWellknownPortProtocol = _HwBrasSbcUpathWellknownPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1, 1, 2),
    _HwBrasSbcUpathWellknownPortProtocol_Type()
)
hwBrasSbcUpathWellknownPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortProtocol.setStatus("current")
_HwBrasSbcUpathWellknownPortAddr_Type = IpAddress
_HwBrasSbcUpathWellknownPortAddr_Object = MibTableColumn
hwBrasSbcUpathWellknownPortAddr = _HwBrasSbcUpathWellknownPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1, 1, 3),
    _HwBrasSbcUpathWellknownPortAddr_Type()
)
hwBrasSbcUpathWellknownPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortAddr.setStatus("current")


class _HwBrasSbcUpathWellknownPortPort_Type(Unsigned32):
    """Custom type hwBrasSbcUpathWellknownPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBrasSbcUpathWellknownPortPort_Type.__name__ = "Unsigned32"
_HwBrasSbcUpathWellknownPortPort_Object = MibTableColumn
hwBrasSbcUpathWellknownPortPort = _HwBrasSbcUpathWellknownPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1, 1, 4),
    _HwBrasSbcUpathWellknownPortPort_Type()
)
hwBrasSbcUpathWellknownPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortPort.setStatus("current")
_HwBrasSbcUpathWellknownPortRowStatus_Type = RowStatus
_HwBrasSbcUpathWellknownPortRowStatus_Object = MibTableColumn
hwBrasSbcUpathWellknownPortRowStatus = _HwBrasSbcUpathWellknownPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 1, 1, 5),
    _HwBrasSbcUpathWellknownPortRowStatus_Type()
)
hwBrasSbcUpathWellknownPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBrasSbcUpathWellknownPortRowStatus.setStatus("current")
_HwBrasSbcUpathSignalMapTable_Object = MibTable
hwBrasSbcUpathSignalMapTable = _HwBrasSbcUpathSignalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathSignalMapTable.setStatus("current")
_HwBrasSbcUpathSignalMapEntry_Object = MibTableRow
hwBrasSbcUpathSignalMapEntry = _HwBrasSbcUpathSignalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 2, 1)
)
hwBrasSbcUpathSignalMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathSignalMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathSignalMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathSignalMapEntry.setStatus("current")
_HwBrasSbcUpathSignalMapAddr_Type = IpAddress
_HwBrasSbcUpathSignalMapAddr_Object = MibTableColumn
hwBrasSbcUpathSignalMapAddr = _HwBrasSbcUpathSignalMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 2, 1, 1),
    _HwBrasSbcUpathSignalMapAddr_Type()
)
hwBrasSbcUpathSignalMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathSignalMapAddr.setStatus("current")


class _HwBrasSbcUpathSignalMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcUpathSignalMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upath", 1)
    )


_HwBrasSbcUpathSignalMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcUpathSignalMapProtocol_Object = MibTableColumn
hwBrasSbcUpathSignalMapProtocol = _HwBrasSbcUpathSignalMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 2, 1, 2),
    _HwBrasSbcUpathSignalMapProtocol_Type()
)
hwBrasSbcUpathSignalMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathSignalMapProtocol.setStatus("current")
_HwBrasSbcUpathSignalMapNumber_Type = Unsigned32
_HwBrasSbcUpathSignalMapNumber_Object = MibTableColumn
hwBrasSbcUpathSignalMapNumber = _HwBrasSbcUpathSignalMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 2, 1, 3),
    _HwBrasSbcUpathSignalMapNumber_Type()
)
hwBrasSbcUpathSignalMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathSignalMapNumber.setStatus("current")


class _HwBrasSbcUpathSignalMapAddrType_Type(Integer32):
    """Custom type hwBrasSbcUpathSignalMapAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HwBrasSbcUpathSignalMapAddrType_Type.__name__ = "Integer32"
_HwBrasSbcUpathSignalMapAddrType_Object = MibTableColumn
hwBrasSbcUpathSignalMapAddrType = _HwBrasSbcUpathSignalMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 2, 1, 4),
    _HwBrasSbcUpathSignalMapAddrType_Type()
)
hwBrasSbcUpathSignalMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathSignalMapAddrType.setStatus("current")
_HwBrasSbcUpathMediaMapTable_Object = MibTable
hwBrasSbcUpathMediaMapTable = _HwBrasSbcUpathMediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 3)
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathMediaMapTable.setStatus("current")
_HwBrasSbcUpathMediaMapEntry_Object = MibTableRow
hwBrasSbcUpathMediaMapEntry = _HwBrasSbcUpathMediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 3, 1)
)
hwBrasSbcUpathMediaMapEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathMediaMapAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathMediaMapProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathMediaMapEntry.setStatus("current")
_HwBrasSbcUpathMediaMapAddr_Type = IpAddress
_HwBrasSbcUpathMediaMapAddr_Object = MibTableColumn
hwBrasSbcUpathMediaMapAddr = _HwBrasSbcUpathMediaMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 3, 1, 1),
    _HwBrasSbcUpathMediaMapAddr_Type()
)
hwBrasSbcUpathMediaMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathMediaMapAddr.setStatus("current")


class _HwBrasSbcUpathMediaMapProtocol_Type(Integer32):
    """Custom type hwBrasSbcUpathMediaMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upath", 1)
    )


_HwBrasSbcUpathMediaMapProtocol_Type.__name__ = "Integer32"
_HwBrasSbcUpathMediaMapProtocol_Object = MibTableColumn
hwBrasSbcUpathMediaMapProtocol = _HwBrasSbcUpathMediaMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 3, 1, 2),
    _HwBrasSbcUpathMediaMapProtocol_Type()
)
hwBrasSbcUpathMediaMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathMediaMapProtocol.setStatus("current")
_HwBrasSbcUpathMediaMapNumber_Type = Unsigned32
_HwBrasSbcUpathMediaMapNumber_Object = MibTableColumn
hwBrasSbcUpathMediaMapNumber = _HwBrasSbcUpathMediaMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 3, 1, 3),
    _HwBrasSbcUpathMediaMapNumber_Type()
)
hwBrasSbcUpathMediaMapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathMediaMapNumber.setStatus("current")
_HwBrasSbcUpathIntercomMapSignalTable_Object = MibTable
hwBrasSbcUpathIntercomMapSignalTable = _HwBrasSbcUpathIntercomMapSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 4)
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapSignalTable.setStatus("current")
_HwBrasSbcUpathIntercomMapSignalEntry_Object = MibTableRow
hwBrasSbcUpathIntercomMapSignalEntry = _HwBrasSbcUpathIntercomMapSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 4, 1)
)
hwBrasSbcUpathIntercomMapSignalEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathIntercomMapSignalAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathIntercomMapSignalProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapSignalEntry.setStatus("current")
_HwBrasSbcUpathIntercomMapSignalAddr_Type = IpAddress
_HwBrasSbcUpathIntercomMapSignalAddr_Object = MibTableColumn
hwBrasSbcUpathIntercomMapSignalAddr = _HwBrasSbcUpathIntercomMapSignalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 4, 1, 1),
    _HwBrasSbcUpathIntercomMapSignalAddr_Type()
)
hwBrasSbcUpathIntercomMapSignalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapSignalAddr.setStatus("current")


class _HwBrasSbcUpathIntercomMapSignalProtocol_Type(Integer32):
    """Custom type hwBrasSbcUpathIntercomMapSignalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upath", 1)
    )


_HwBrasSbcUpathIntercomMapSignalProtocol_Type.__name__ = "Integer32"
_HwBrasSbcUpathIntercomMapSignalProtocol_Object = MibTableColumn
hwBrasSbcUpathIntercomMapSignalProtocol = _HwBrasSbcUpathIntercomMapSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 4, 1, 2),
    _HwBrasSbcUpathIntercomMapSignalProtocol_Type()
)
hwBrasSbcUpathIntercomMapSignalProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapSignalProtocol.setStatus("current")
_HwBrasSbcUpathIntercomMapSignalNumber_Type = Unsigned32
_HwBrasSbcUpathIntercomMapSignalNumber_Object = MibTableColumn
hwBrasSbcUpathIntercomMapSignalNumber = _HwBrasSbcUpathIntercomMapSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 4, 1, 3),
    _HwBrasSbcUpathIntercomMapSignalNumber_Type()
)
hwBrasSbcUpathIntercomMapSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapSignalNumber.setStatus("current")
_HwBrasSbcUpathIntercomMapMediaTable_Object = MibTable
hwBrasSbcUpathIntercomMapMediaTable = _HwBrasSbcUpathIntercomMapMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 5)
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapMediaTable.setStatus("current")
_HwBrasSbcUpathIntercomMapMediaEntry_Object = MibTableRow
hwBrasSbcUpathIntercomMapMediaEntry = _HwBrasSbcUpathIntercomMapMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 5, 1)
)
hwBrasSbcUpathIntercomMapMediaEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathIntercomMapMediaAddr"),
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathIntercomMapMediaProtocol"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapMediaEntry.setStatus("current")
_HwBrasSbcUpathIntercomMapMediaAddr_Type = IpAddress
_HwBrasSbcUpathIntercomMapMediaAddr_Object = MibTableColumn
hwBrasSbcUpathIntercomMapMediaAddr = _HwBrasSbcUpathIntercomMapMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 5, 1, 1),
    _HwBrasSbcUpathIntercomMapMediaAddr_Type()
)
hwBrasSbcUpathIntercomMapMediaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapMediaAddr.setStatus("current")


class _HwBrasSbcUpathIntercomMapMediaProtocol_Type(Integer32):
    """Custom type hwBrasSbcUpathIntercomMapMediaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upath", 1)
    )


_HwBrasSbcUpathIntercomMapMediaProtocol_Type.__name__ = "Integer32"
_HwBrasSbcUpathIntercomMapMediaProtocol_Object = MibTableColumn
hwBrasSbcUpathIntercomMapMediaProtocol = _HwBrasSbcUpathIntercomMapMediaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 5, 1, 2),
    _HwBrasSbcUpathIntercomMapMediaProtocol_Type()
)
hwBrasSbcUpathIntercomMapMediaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapMediaProtocol.setStatus("current")
_HwBrasSbcUpathIntercomMapMediaNumber_Type = Unsigned32
_HwBrasSbcUpathIntercomMapMediaNumber_Object = MibTableColumn
hwBrasSbcUpathIntercomMapMediaNumber = _HwBrasSbcUpathIntercomMapMediaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 5, 1, 3),
    _HwBrasSbcUpathIntercomMapMediaNumber_Type()
)
hwBrasSbcUpathIntercomMapMediaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathIntercomMapMediaNumber.setStatus("current")
_HwBrasSbcUpathStatSignalPacketTable_Object = MibTable
hwBrasSbcUpathStatSignalPacketTable = _HwBrasSbcUpathStatSignalPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6)
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketTable.setStatus("current")
_HwBrasSbcUpathStatSignalPacketEntry_Object = MibTableRow
hwBrasSbcUpathStatSignalPacketEntry = _HwBrasSbcUpathStatSignalPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1)
)
hwBrasSbcUpathStatSignalPacketEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathStatSignalPacketIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketEntry.setStatus("current")


class _HwBrasSbcUpathStatSignalPacketIndex_Type(Integer32):
    """Custom type hwBrasSbcUpathStatSignalPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upath", 1)
    )


_HwBrasSbcUpathStatSignalPacketIndex_Type.__name__ = "Integer32"
_HwBrasSbcUpathStatSignalPacketIndex_Object = MibTableColumn
hwBrasSbcUpathStatSignalPacketIndex = _HwBrasSbcUpathStatSignalPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1, 1),
    _HwBrasSbcUpathStatSignalPacketIndex_Type()
)
hwBrasSbcUpathStatSignalPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketIndex.setStatus("current")
_HwBrasSbcUpathStatSignalPacketInNumber_Type = Counter64
_HwBrasSbcUpathStatSignalPacketInNumber_Object = MibTableColumn
hwBrasSbcUpathStatSignalPacketInNumber = _HwBrasSbcUpathStatSignalPacketInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1, 2),
    _HwBrasSbcUpathStatSignalPacketInNumber_Type()
)
hwBrasSbcUpathStatSignalPacketInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketInNumber.setStatus("current")
_HwBrasSbcUpathStatSignalPacketInOctet_Type = Counter64
_HwBrasSbcUpathStatSignalPacketInOctet_Object = MibTableColumn
hwBrasSbcUpathStatSignalPacketInOctet = _HwBrasSbcUpathStatSignalPacketInOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1, 3),
    _HwBrasSbcUpathStatSignalPacketInOctet_Type()
)
hwBrasSbcUpathStatSignalPacketInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketInOctet.setStatus("current")
_HwBrasSbcUpathStatSignalPacketOutNumber_Type = Counter64
_HwBrasSbcUpathStatSignalPacketOutNumber_Object = MibTableColumn
hwBrasSbcUpathStatSignalPacketOutNumber = _HwBrasSbcUpathStatSignalPacketOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1, 4),
    _HwBrasSbcUpathStatSignalPacketOutNumber_Type()
)
hwBrasSbcUpathStatSignalPacketOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketOutNumber.setStatus("current")
_HwBrasSbcUpathStatSignalPacketOutOctet_Type = Counter64
_HwBrasSbcUpathStatSignalPacketOutOctet_Object = MibTableColumn
hwBrasSbcUpathStatSignalPacketOutOctet = _HwBrasSbcUpathStatSignalPacketOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1, 5),
    _HwBrasSbcUpathStatSignalPacketOutOctet_Type()
)
hwBrasSbcUpathStatSignalPacketOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketOutOctet.setStatus("current")
_HwBrasSbcUpathStatSignalPacketRowStatus_Type = RowStatus
_HwBrasSbcUpathStatSignalPacketRowStatus_Object = MibTableColumn
hwBrasSbcUpathStatSignalPacketRowStatus = _HwBrasSbcUpathStatSignalPacketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 8, 3, 6, 1, 6),
    _HwBrasSbcUpathStatSignalPacketRowStatus_Type()
)
hwBrasSbcUpathStatSignalPacketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcUpathStatSignalPacketRowStatus.setStatus("current")
_HwBrasSbcOm_ObjectIdentity = ObjectIdentity
hwBrasSbcOm = _HwBrasSbcOm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21)
)
_HwBrasSbcOmLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcOmLeaves = _HwBrasSbcOmLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21, 1)
)


class _HwBrasSbcRestartEnable_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcRestartEnable based on HWBrasEnabledStatus"""


_HwBrasSbcRestartEnable_Object = MibScalar
hwBrasSbcRestartEnable = _HwBrasSbcRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21, 1, 1),
    _HwBrasSbcRestartEnable_Type()
)
hwBrasSbcRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcRestartEnable.setStatus("current")


class _HwBrasSbcRestartButton_Type(Integer32):
    """Custom type hwBrasSbcRestartButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              101)
        )
    )
    namedValues = NamedValues(
        *(("notready", 1),
          ("restart", 101))
    )


_HwBrasSbcRestartButton_Type.__name__ = "Integer32"
_HwBrasSbcRestartButton_Object = MibScalar
hwBrasSbcRestartButton = _HwBrasSbcRestartButton_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21, 1, 2),
    _HwBrasSbcRestartButton_Type()
)
hwBrasSbcRestartButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcRestartButton.setStatus("current")


class _HwBrasSbcPatchLoadStatus_Type(Integer32):
    """Custom type hwBrasSbcPatchLoadStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 2),
          ("unknown", 1))
    )


_HwBrasSbcPatchLoadStatus_Type.__name__ = "Integer32"
_HwBrasSbcPatchLoadStatus_Object = MibScalar
hwBrasSbcPatchLoadStatus = _HwBrasSbcPatchLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21, 1, 3),
    _HwBrasSbcPatchLoadStatus_Type()
)
hwBrasSbcPatchLoadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcPatchLoadStatus.setStatus("current")


class _HwBrasSbcLocalizationStatus_Type(HWBrasEnabledStatus):
    """Custom type hwBrasSbcLocalizationStatus based on HWBrasEnabledStatus"""


_HwBrasSbcLocalizationStatus_Object = MibScalar
hwBrasSbcLocalizationStatus = _HwBrasSbcLocalizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21, 1, 4),
    _HwBrasSbcLocalizationStatus_Type()
)
hwBrasSbcLocalizationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBrasSbcLocalizationStatus.setStatus("current")
_HwBrasSbcOmTables_ObjectIdentity = ObjectIdentity
hwBrasSbcOmTables = _HwBrasSbcOmTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 1, 21, 2)
)
_HwBrasSbcTrapBind_ObjectIdentity = ObjectIdentity
hwBrasSbcTrapBind = _HwBrasSbcTrapBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2)
)
_HwBrasSbcTrapBindLeaves_ObjectIdentity = ObjectIdentity
hwBrasSbcTrapBindLeaves = _HwBrasSbcTrapBindLeaves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 1)
)
_HwBrasSbcTrapBindTables_ObjectIdentity = ObjectIdentity
hwBrasSbcTrapBindTables = _HwBrasSbcTrapBindTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2)
)
_HwBrasSbcTrapBindTable_Object = MibTable
hwBrasSbcTrapBindTable = _HwBrasSbcTrapBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindTable.setStatus("current")
_HwBrasSbcTrapBindEntry_Object = MibTableRow
hwBrasSbcTrapBindEntry = _HwBrasSbcTrapBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1)
)
hwBrasSbcTrapBindEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindEntry.setStatus("current")


class _HwBrasSbcTrapBindIndex_Type(Integer32):
    """Custom type hwBrasSbcTrapBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("trapbind", 1)
    )


_HwBrasSbcTrapBindIndex_Type.__name__ = "Integer32"
_HwBrasSbcTrapBindIndex_Object = MibTableColumn
hwBrasSbcTrapBindIndex = _HwBrasSbcTrapBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1, 1),
    _HwBrasSbcTrapBindIndex_Type()
)
hwBrasSbcTrapBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindIndex.setStatus("current")


class _HwBrasSbcTrapBindID_Type(Unsigned32):
    """Custom type hwBrasSbcTrapBindID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 299),
    )


_HwBrasSbcTrapBindID_Type.__name__ = "Unsigned32"
_HwBrasSbcTrapBindID_Object = MibTableColumn
hwBrasSbcTrapBindID = _HwBrasSbcTrapBindID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1, 2),
    _HwBrasSbcTrapBindID_Type()
)
hwBrasSbcTrapBindID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindID.setStatus("current")
_HwBrasSbcTrapBindTime_Type = DateAndTime
_HwBrasSbcTrapBindTime_Object = MibTableColumn
hwBrasSbcTrapBindTime = _HwBrasSbcTrapBindTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1, 3),
    _HwBrasSbcTrapBindTime_Type()
)
hwBrasSbcTrapBindTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindTime.setStatus("current")
_HwBrasSbcTrapBindFluID_Type = Unsigned32
_HwBrasSbcTrapBindFluID_Object = MibTableColumn
hwBrasSbcTrapBindFluID = _HwBrasSbcTrapBindFluID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1, 4),
    _HwBrasSbcTrapBindFluID_Type()
)
hwBrasSbcTrapBindFluID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindFluID.setStatus("current")


class _HwBrasSbcTrapBindReason_Type(Unsigned32):
    """Custom type hwBrasSbcTrapBindReason based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 299),
    )


_HwBrasSbcTrapBindReason_Type.__name__ = "Unsigned32"
_HwBrasSbcTrapBindReason_Object = MibTableColumn
hwBrasSbcTrapBindReason = _HwBrasSbcTrapBindReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1, 5),
    _HwBrasSbcTrapBindReason_Type()
)
hwBrasSbcTrapBindReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindReason.setStatus("current")


class _HwBrasSbcTrapBindType_Type(Integer32):
    """Custom type hwBrasSbcTrapBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("notify", 0),
          ("resume", 2),
          ("sync", 3))
    )


_HwBrasSbcTrapBindType_Type.__name__ = "Integer32"
_HwBrasSbcTrapBindType_Object = MibTableColumn
hwBrasSbcTrapBindType = _HwBrasSbcTrapBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 1, 1, 6),
    _HwBrasSbcTrapBindType_Type()
)
hwBrasSbcTrapBindType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapBindType.setStatus("current")
_HwBrasSbcTrapInfoTable_Object = MibTable
hwBrasSbcTrapInfoTable = _HwBrasSbcTrapInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoTable.setStatus("current")
_HwBrasSbcTrapInfoEntry_Object = MibTableRow
hwBrasSbcTrapInfoEntry = _HwBrasSbcTrapInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1)
)
hwBrasSbcTrapInfoEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoIndex"),
)
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoEntry.setStatus("current")


class _HwBrasSbcTrapInfoIndex_Type(Integer32):
    """Custom type hwBrasSbcTrapInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("trap", 1)
    )


_HwBrasSbcTrapInfoIndex_Type.__name__ = "Integer32"
_HwBrasSbcTrapInfoIndex_Object = MibTableColumn
hwBrasSbcTrapInfoIndex = _HwBrasSbcTrapInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 1),
    _HwBrasSbcTrapInfoIndex_Type()
)
hwBrasSbcTrapInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoIndex.setStatus("current")


class _HwBrasSbcTrapInfoCpu_Type(Unsigned32):
    """Custom type hwBrasSbcTrapInfoCpu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBrasSbcTrapInfoCpu_Type.__name__ = "Unsigned32"
_HwBrasSbcTrapInfoCpu_Object = MibTableColumn
hwBrasSbcTrapInfoCpu = _HwBrasSbcTrapInfoCpu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 2),
    _HwBrasSbcTrapInfoCpu_Type()
)
hwBrasSbcTrapInfoCpu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoCpu.setStatus("current")


class _HwBrasSbcTrapInfoHrp_Type(Integer32):
    """Custom type hwBrasSbcTrapInfoHrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("action", 1)
    )


_HwBrasSbcTrapInfoHrp_Type.__name__ = "Integer32"
_HwBrasSbcTrapInfoHrp_Object = MibTableColumn
hwBrasSbcTrapInfoHrp = _HwBrasSbcTrapInfoHrp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 3),
    _HwBrasSbcTrapInfoHrp_Type()
)
hwBrasSbcTrapInfoHrp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoHrp.setStatus("current")
_HwBrasSbcTrapInfoSignalingFlood_Type = Unsigned32
_HwBrasSbcTrapInfoSignalingFlood_Object = MibTableColumn
hwBrasSbcTrapInfoSignalingFlood = _HwBrasSbcTrapInfoSignalingFlood_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 4),
    _HwBrasSbcTrapInfoSignalingFlood_Type()
)
hwBrasSbcTrapInfoSignalingFlood.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoSignalingFlood.setStatus("current")
_HwBrasSbcTrapInfoCac_Type = Unsigned32
_HwBrasSbcTrapInfoCac_Object = MibTableColumn
hwBrasSbcTrapInfoCac = _HwBrasSbcTrapInfoCac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 5),
    _HwBrasSbcTrapInfoCac_Type()
)
hwBrasSbcTrapInfoCac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoCac.setStatus("current")


class _HwBrasSbcTrapInfoStatistic_Type(Integer32):
    """Custom type hwBrasSbcTrapInfoStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("action", 1)
    )


_HwBrasSbcTrapInfoStatistic_Type.__name__ = "Integer32"
_HwBrasSbcTrapInfoStatistic_Object = MibTableColumn
hwBrasSbcTrapInfoStatistic = _HwBrasSbcTrapInfoStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 6),
    _HwBrasSbcTrapInfoStatistic_Type()
)
hwBrasSbcTrapInfoStatistic.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoStatistic.setStatus("current")
_HwBrasSbcTrapInfoPortStatistic_Type = Unsigned32
_HwBrasSbcTrapInfoPortStatistic_Object = MibTableColumn
hwBrasSbcTrapInfoPortStatistic = _HwBrasSbcTrapInfoPortStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 7),
    _HwBrasSbcTrapInfoPortStatistic_Type()
)
hwBrasSbcTrapInfoPortStatistic.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoPortStatistic.setStatus("current")
_HwBrasSbcTrapInfoOldSSIP_Type = IpAddress
_HwBrasSbcTrapInfoOldSSIP_Object = MibTableColumn
hwBrasSbcTrapInfoOldSSIP = _HwBrasSbcTrapInfoOldSSIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 8),
    _HwBrasSbcTrapInfoOldSSIP_Type()
)
hwBrasSbcTrapInfoOldSSIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoOldSSIP.setStatus("current")
_HwBrasSbcTrapInfoImsConID_Type = Unsigned32
_HwBrasSbcTrapInfoImsConID_Object = MibTableColumn
hwBrasSbcTrapInfoImsConID = _HwBrasSbcTrapInfoImsConID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 9),
    _HwBrasSbcTrapInfoImsConID_Type()
)
hwBrasSbcTrapInfoImsConID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoImsConID.setStatus("current")
_HwBrasSbcTrapInfoImsCcbID_Type = Unsigned32
_HwBrasSbcTrapInfoImsCcbID_Object = MibTableColumn
hwBrasSbcTrapInfoImsCcbID = _HwBrasSbcTrapInfoImsCcbID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 2, 2, 2, 1, 10),
    _HwBrasSbcTrapInfoImsCcbID_Type()
)
hwBrasSbcTrapInfoImsCcbID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBrasSbcTrapInfoImsCcbID.setStatus("current")
_HwBrasSbcComformance_ObjectIdentity = ObjectIdentity
hwBrasSbcComformance = _HwBrasSbcComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 3)
)
_HwBrasSbcGroups_ObjectIdentity = ObjectIdentity
hwBrasSbcGroups = _HwBrasSbcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 3, 1)
)
_HwBrasSbcCapabilities_ObjectIdentity = ObjectIdentity
hwBrasSbcCapabilities = _HwBrasSbcCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 3, 2)
)
_HwBrasSbcNotification_ObjectIdentity = ObjectIdentity
hwBrasSbcNotification = _HwBrasSbcNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4)
)
_HwBrasSbcNotificationGroups_ObjectIdentity = ObjectIdentity
hwBrasSbcNotificationGroups = _HwBrasSbcNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 5)
)

# Managed Objects groups

hwBrasSbcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 3, 1, 1)
)
hwBrasSbcGroup.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalAddrMapRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPortrangeBegin"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPortrangeEnd"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPortrangeRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipWellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSoftVersion"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCpuUsage"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsWellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsWellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323WellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323WellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoWellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoWellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248WellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248WellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsMibRegRegister"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsMibRegRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipWellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipAnonymity"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipCheckheartEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipCallsessionTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpAuepTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpCcbTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpTxTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpWellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpWellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsRegRefreshEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticDesc"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticValue"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248Enable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248CcbTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248UserAgeTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323Enable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323CallsessionTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248SyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323SyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathCallsessionTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathHeartbeatTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323Q931WellknownPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntercomPrefixDestAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntercomPrefixSrcAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntercomPrefixRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatisticSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcAppMode"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaDetectValidityEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaDetectSsrcEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaDetectPacketLength"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcInstanceName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcInstanceRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMapGroupInstanceName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMapGroupSessionLimit"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrVPNName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIf1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrSlotID1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIf2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrSlotID2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIf3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrSlotID3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIf4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrSlotID4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrVPNName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIf1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrSlotID1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIf2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrSlotID2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIf3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrSlotID3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIf4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrSlotID4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBackupGroupType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBackupGroupInstanceName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBackupGroupRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCurrentSlotID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSlotCfgState"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSlotInforRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMgLogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsStatisticsEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTimerMediaAging"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGInstanceName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatSessionAgingTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatGroupIndex"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatVpnNameIndex"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatInstanceName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcNatCfgRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwNatAddrGrpBeginningIpAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwNatAddrGrpEndingIpAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwNatAddrGrpRefCount"),
        ("HUAWEI-BRAS-SBC-MIB", "hwNatAddrGrpVpnName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwNatAddrGrpRowstatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBWLimitType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcBWLimitValue"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarDegreeBandWidth"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarDegreeDscp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarDegreeRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarRuleName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarRuleDegreeID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarRuleRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarRuleDegreeBandWidth"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSessionCarRuleDegreeDscp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipMediaMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpMediaMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323MediaMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsMediaMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathMediaMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248MediaMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCallerID1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCallerID2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCallerID3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCallerID4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCalleeID1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCalleeID2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCalleeID3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersCalleeID4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaUsersRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaPassEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaPassRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupRuleType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaPassSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaAddrMapServerAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaAddrMapWeight"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaAddrMapRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitDefault"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitSyslogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaPassAclNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRtpSpecialAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRtpSpecialAddrAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipSignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipIntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpIntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpIntercomMapMediaNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsIntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsIntercomMapMediaNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323IntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323IntercomMapMediaNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoIntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248IntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248IntercomMapMediaNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathIntercomMapSignalNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathIntercomMapMediaNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitExtendEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipIntercomMapMediaNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipSignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpSignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpSignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsSignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsSignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323SignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323SignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoSignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoSignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248SignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248SignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathSignalMapNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRoamlimitAclNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathSignalMapAddrType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathWellknownPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathStatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathStatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathStatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathStatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathStatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248StatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248StatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248StatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248StatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248StatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoStatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoStatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoStatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoStatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdoStatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323StatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323StatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323StatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323StatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323StatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsStatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsStatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsStatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsStatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsStatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpStatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpStatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpStatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpStatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpStatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipStatSignalPacketInNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipStatSignalPacketInOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipStatSignalPacketOutNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipStatSignalPacketOutOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipStatSignalPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatMediaPacketNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatMediaPacketOctet"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatMediaPacketRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegRateThreshold"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegRatePercent"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegRateRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegTotalThreshold"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegTotalPercent"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacRegTotalRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallRateThreshold"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallRatePercent"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallRateRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallTotalThreshold"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallTotalPercent"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacCallTotalRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendUserConnectRateThreshold"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendUserConnectRatePercent"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendUserConnectRateRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendConnectRateThreshold"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendConnectRatePercent"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendConnectRateRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendMode"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendActionLogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUpathWellknownPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupRuleUserName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUsergroupRuleRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelIfPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelSctpAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelTunnelTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelTransportTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPoolRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPoolStartIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUdpTunnelPoolEndIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntMediaPassEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalAddrMapSoftAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalAddrMapIadmsAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRestartEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcRestartButton"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcUmsVersion"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMapGroupsType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMapGroupsStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMapGroupsRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGCliAddrVPN"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGCliAddrIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGCliAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrVPN"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrVPN"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrVPN"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGPrefixID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGPrefixRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrVPN"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrVPN"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMatchAcl"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMatchRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcHrpSynchronization"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrIP1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrIP2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrIP3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGIadmsAddrIP4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrIP1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrIP2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrIP3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGSofxAddrIP4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIP1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIP2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIP3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdServAddrIP4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIP1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIP2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIP3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGMdCliAddrIP4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrIP1"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrIP2"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrIP3"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGServAddrIP4"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolSip"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolMgcp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolH323"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolIadms"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolUpath"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGProtocolH248"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPatchLoadStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsActiveStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsActiveRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsBandIfIndex"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsBandIfName"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsBandIfType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsBandValue"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsBandRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectPepID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectCliType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectServIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectServPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsQosEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMediaProxyEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsQosLogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMediaProxyLogEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacActionLogStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectCliIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH248PDHCountLimit"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcH323PDHCountLimit"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMgcpPDHCountLimit"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipPDHCountLimit"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipRegReduceStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSipRegReduceTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSIPDetectStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSIPDetectTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSIPDetectSourcePort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSIPDetectFailCount"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSoftswitchPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSoftswitchPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsPortPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIadmsPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort01"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort02"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort03"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort04"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort05"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort06"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort07"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort08"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort09"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort10"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort11"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort12"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort13"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort14"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort15"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortPort16"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcClientPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntercomStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcQRStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcQRBandWidth"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIPCarBWValue"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIPCarBWRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDynamicStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalingCarStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIPCarStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGDomainMapIndex"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGDomainRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPVersion"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPAddr"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPInterface"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGIPRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGDescription"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGTableStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGProtocol"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGMidString"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGConnectTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGAgingTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsMGCallSessionTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSctpStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdlecutRtcpTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIdlecutRtpTimer"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaDetectStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMediaOnewayStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatisticMinDrop"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatisticMaxDrop"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatisticFragDrop"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatisticFlowDrop"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatisticRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDLengthMin"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDLengthMax"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDLengthRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMDStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDefendExtStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsConnectCliPort"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGPortNumber"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcMGPortRowStatus"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIntercomEnable"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcLocalizationStatus"))
)
if mibBuilder.loadTexts:
    hwBrasSbcGroup.setStatus("current")

hwBrasSbcTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 3, 1, 2)
)
hwBrasSbcTrapGroup.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoCpu"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoHrp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoSignalingFlood"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoCac"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoPortStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsCcbID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoOldSSIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSIPDetectFailCount"))
)
if mibBuilder.loadTexts:
    hwBrasSbcTrapGroup.setStatus("current")


# Notification objects

hwBrasSbcCpu = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 1)
)
hwBrasSbcCpu.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoCpu"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcCpu.setStatus(
        "current"
    )

hwBrasSbcCpuNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 2)
)
hwBrasSbcCpuNormal.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoCpu"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcCpuNormal.setStatus(
        "current"
    )

hwBrasSbcHrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 3)
)
hwBrasSbcHrp.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoHrp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcHrp.setStatus(
        "current"
    )

hwBrasSbcSignalingFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 4)
)
hwBrasSbcSignalingFlood.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoSignalingFlood"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcSignalingFlood.setStatus(
        "current"
    )

hwBrasSbcSignalingFloodNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 5)
)
hwBrasSbcSignalingFloodNormal.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoSignalingFlood"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcSignalingFloodNormal.setStatus(
        "current"
    )

hwBrasSbcCac = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 6)
)
hwBrasSbcCac.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoCac"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcCac.setStatus(
        "current"
    )

hwBrasSbcCacNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 7)
)
hwBrasSbcCacNormal.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoCac"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcCacNormal.setStatus(
        "current"
    )

hwBrasSbcStatistic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 8)
)
hwBrasSbcStatistic.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcStatistic.setStatus(
        "current"
    )

hwBrasSbcPortStatistic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 9)
)
hwBrasSbcPortStatistic.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoPortStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcPortStatistic.setStatus(
        "current"
    )

hwBrasSbcPortStatisticNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 10)
)
hwBrasSbcPortStatisticNormal.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoPortStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcPortStatisticNormal.setStatus(
        "current"
    )

hwBrasSbcDHSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 11)
)
hwBrasSbcDHSwitch.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSIPDetectFailCount"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoOldSSIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcDHSwitch.setStatus(
        "current"
    )

hwBrasSbcDHSwitchNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 12)
)
hwBrasSbcDHSwitchNormal.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoOldSSIP"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcDHSwitchNormal.setStatus(
        "current"
    )

hwBrasSbcImsRptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 13)
)
hwBrasSbcImsRptFail.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcImsRptFail.setStatus(
        "current"
    )

hwBrasSbcImsRptDrq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 14)
)
hwBrasSbcImsRptDrq.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcImsRptDrq.setStatus(
        "current"
    )

hwBrasSbcImsTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 15)
)
hwBrasSbcImsTimeOut.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsCcbID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcImsTimeOut.setStatus(
        "current"
    )

hwBrasSbcImsSessCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 16)
)
hwBrasSbcImsSessCreate.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsCcbID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcImsSessCreate.setStatus(
        "current"
    )

hwBrasSbcImsSessDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 17)
)
hwBrasSbcImsSessDelete.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsCcbID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcImsSessDelete.setStatus(
        "current"
    )

hwBrasSbcCopsLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 18)
)
hwBrasSbcCopsLinkUp.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcCopsLinkUp.setStatus(
        "current"
    )

hwBrasSbcCopsLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 19)
)
hwBrasSbcCopsLinkDown.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcCopsLinkDown.setStatus(
        "current"
    )

hwBrasSbcIaLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 20)
)
hwBrasSbcIaLinkUp.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcIaLinkUp.setStatus(
        "current"
    )

hwBrasSbcIaLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 4, 21)
)
hwBrasSbcIaLinkDown.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapInfoImsConID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindTime"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindFluID"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindReason"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcTrapBindType"))
)
if mibBuilder.loadTexts:
    hwBrasSbcIaLinkDown.setStatus(
        "current"
    )


# Notifications groups

hwBrasSbcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 25, 2, 5, 1)
)
hwBrasSbcNotificationGroup.setObjects(
      *(("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCpu"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCpuNormal"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcHrp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalingFlood"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcSignalingFloodNormal"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCac"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCacNormal"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPortStatistic"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcPortStatisticNormal"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSwitch"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcDHSwitchNormal"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsRptFail"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsRptDrq"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsTimeOut"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsSessCreate"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcImsSessDelete"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCopsLinkUp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcCopsLinkDown"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIaLinkUp"),
        ("HUAWEI-BRAS-SBC-MIB", "hwBrasSbcIaLinkDown"))
)
if mibBuilder.loadTexts:
    hwBrasSbcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-SBC-MIB",
    **{"HWBrasEnabledStatus": HWBrasEnabledStatus,
       "HWBrasPermitStatus": HWBrasPermitStatus,
       "HWBrasSecurityProtocol": HWBrasSecurityProtocol,
       "HWBrasSbcBaseProtocol": HWBrasSbcBaseProtocol,
       "HwBrasAppMode": HwBrasAppMode,
       "HwBrasBWLimitType": HwBrasBWLimitType,
       "hwBrasSbcMgmt": hwBrasSbcMgmt,
       "hwBrasSbcModule": hwBrasSbcModule,
       "hwBrasSbcObjects": hwBrasSbcObjects,
       "hwBrasSbcGeneral": hwBrasSbcGeneral,
       "hwBrasSbcBase": hwBrasSbcBase,
       "hwBrasSbcBaseLeaves": hwBrasSbcBaseLeaves,
       "hwBrasSbcStatisticEnable": hwBrasSbcStatisticEnable,
       "hwBrasSbcStatisticSyslogEnable": hwBrasSbcStatisticSyslogEnable,
       "hwBrasSbcAppMode": hwBrasSbcAppMode,
       "hwBrasSbcMediaDetectValidityEnable": hwBrasSbcMediaDetectValidityEnable,
       "hwBrasSbcMediaDetectSsrcEnable": hwBrasSbcMediaDetectSsrcEnable,
       "hwBrasSbcMediaDetectPacketLength": hwBrasSbcMediaDetectPacketLength,
       "hwBrasSbcBaseTables": hwBrasSbcBaseTables,
       "hwBrasSbcSignalAddrMapTable": hwBrasSbcSignalAddrMapTable,
       "hwBrasSbcSignalAddrMapEntry": hwBrasSbcSignalAddrMapEntry,
       "hwBrasSbcSignalAddrMapClientAddr": hwBrasSbcSignalAddrMapClientAddr,
       "hwBrasSbcSignalAddrMapServerAddr": hwBrasSbcSignalAddrMapServerAddr,
       "hwBrasSbcSignalAddrMapSoftAddr": hwBrasSbcSignalAddrMapSoftAddr,
       "hwBrasSbcSignalAddrMapIadmsAddr": hwBrasSbcSignalAddrMapIadmsAddr,
       "hwBrasSbcSignalAddrMapRowStatus": hwBrasSbcSignalAddrMapRowStatus,
       "hwBrasSbcMediaAddrMapTable": hwBrasSbcMediaAddrMapTable,
       "hwBrasSbcMediaAddrMapEntry": hwBrasSbcMediaAddrMapEntry,
       "hwBrasSbcMediaAddrMapClientAddr": hwBrasSbcMediaAddrMapClientAddr,
       "hwBrasSbcMediaAddrMapServerAddr": hwBrasSbcMediaAddrMapServerAddr,
       "hwBrasSbcMediaAddrMapWeight": hwBrasSbcMediaAddrMapWeight,
       "hwBrasSbcMediaAddrMapRowStatus": hwBrasSbcMediaAddrMapRowStatus,
       "hwBrasSbcPortrangeTable": hwBrasSbcPortrangeTable,
       "hwBrasSbcPortrangeEntry": hwBrasSbcPortrangeEntry,
       "hwBrasSbcPortrangeIndex": hwBrasSbcPortrangeIndex,
       "hwBrasSbcPortrangeBegin": hwBrasSbcPortrangeBegin,
       "hwBrasSbcPortrangeEnd": hwBrasSbcPortrangeEnd,
       "hwBrasSbcPortrangeRowStatus": hwBrasSbcPortrangeRowStatus,
       "hwBrasSbcStatMediaPacketTable": hwBrasSbcStatMediaPacketTable,
       "hwBrasSbcStatMediaPacketEntry": hwBrasSbcStatMediaPacketEntry,
       "hwBrasSbcStatMediaPacketIndex": hwBrasSbcStatMediaPacketIndex,
       "hwBrasSbcStatMediaPacketNumber": hwBrasSbcStatMediaPacketNumber,
       "hwBrasSbcStatMediaPacketOctet": hwBrasSbcStatMediaPacketOctet,
       "hwBrasSbcStatMediaPacketRowStatus": hwBrasSbcStatMediaPacketRowStatus,
       "hwBrasSbcClientPortTable": hwBrasSbcClientPortTable,
       "hwBrasSbcClientPortEntry": hwBrasSbcClientPortEntry,
       "hwBrasSbcClientPortProtocol": hwBrasSbcClientPortProtocol,
       "hwBrasSbcClientPortVPN": hwBrasSbcClientPortVPN,
       "hwBrasSbcClientPortIP": hwBrasSbcClientPortIP,
       "hwBrasSbcClientPortPort01": hwBrasSbcClientPortPort01,
       "hwBrasSbcClientPortPort02": hwBrasSbcClientPortPort02,
       "hwBrasSbcClientPortPort03": hwBrasSbcClientPortPort03,
       "hwBrasSbcClientPortPort04": hwBrasSbcClientPortPort04,
       "hwBrasSbcClientPortPort05": hwBrasSbcClientPortPort05,
       "hwBrasSbcClientPortPort06": hwBrasSbcClientPortPort06,
       "hwBrasSbcClientPortPort07": hwBrasSbcClientPortPort07,
       "hwBrasSbcClientPortPort08": hwBrasSbcClientPortPort08,
       "hwBrasSbcClientPortPort09": hwBrasSbcClientPortPort09,
       "hwBrasSbcClientPortPort10": hwBrasSbcClientPortPort10,
       "hwBrasSbcClientPortPort11": hwBrasSbcClientPortPort11,
       "hwBrasSbcClientPortPort12": hwBrasSbcClientPortPort12,
       "hwBrasSbcClientPortPort13": hwBrasSbcClientPortPort13,
       "hwBrasSbcClientPortPort14": hwBrasSbcClientPortPort14,
       "hwBrasSbcClientPortPort15": hwBrasSbcClientPortPort15,
       "hwBrasSbcClientPortPort16": hwBrasSbcClientPortPort16,
       "hwBrasSbcClientPortRowStatus": hwBrasSbcClientPortRowStatus,
       "hwBrasSbcSoftswitchPortTable": hwBrasSbcSoftswitchPortTable,
       "hwBrasSbcSoftswitchPortEntry": hwBrasSbcSoftswitchPortEntry,
       "hwBrasSbcSoftswitchPortProtocol": hwBrasSbcSoftswitchPortProtocol,
       "hwBrasSbcSoftswitchPortVPN": hwBrasSbcSoftswitchPortVPN,
       "hwBrasSbcSoftswitchPortIP": hwBrasSbcSoftswitchPortIP,
       "hwBrasSbcSoftswitchPortPort": hwBrasSbcSoftswitchPortPort,
       "hwBrasSbcSoftswitchPortRowStatus": hwBrasSbcSoftswitchPortRowStatus,
       "hwBrasSbcIadmsPortTable": hwBrasSbcIadmsPortTable,
       "hwBrasSbcIadmsPortEntry": hwBrasSbcIadmsPortEntry,
       "hwBrasSbcIadmsPortProtocol": hwBrasSbcIadmsPortProtocol,
       "hwBrasSbcIadmsPortVPN": hwBrasSbcIadmsPortVPN,
       "hwBrasSbcIadmsPortIP": hwBrasSbcIadmsPortIP,
       "hwBrasSbcIadmsPortPort": hwBrasSbcIadmsPortPort,
       "hwBrasSbcIadmsPortRowStatus": hwBrasSbcIadmsPortRowStatus,
       "hwBrasSbcInstanceTable": hwBrasSbcInstanceTable,
       "hwBrasSbcInstanceEntry": hwBrasSbcInstanceEntry,
       "hwBrasSbcInstanceName": hwBrasSbcInstanceName,
       "hwBrasSbcInstanceRowStatus": hwBrasSbcInstanceRowStatus,
       "hwBrasSbcMapGroup": hwBrasSbcMapGroup,
       "hwBrasSbcMapGroupLeaves": hwBrasSbcMapGroupLeaves,
       "hwBrasSbcMapGroupTables": hwBrasSbcMapGroupTables,
       "hwBrasSbcMapGroupsTable": hwBrasSbcMapGroupsTable,
       "hwBrasSbcMapGroupsEntry": hwBrasSbcMapGroupsEntry,
       "hwBrasSbcMapGroupsIndex": hwBrasSbcMapGroupsIndex,
       "hwBrasSbcMapGroupsType": hwBrasSbcMapGroupsType,
       "hwBrasSbcMapGroupsStatus": hwBrasSbcMapGroupsStatus,
       "hwBrasSbcMapGroupInstanceName": hwBrasSbcMapGroupInstanceName,
       "hwBrasSbcMapGroupSessionLimit": hwBrasSbcMapGroupSessionLimit,
       "hwBrasSbcMapGroupsRowStatus": hwBrasSbcMapGroupsRowStatus,
       "hwBrasSbcMGCliAddrTable": hwBrasSbcMGCliAddrTable,
       "hwBrasSbcMGCliAddrEntry": hwBrasSbcMGCliAddrEntry,
       "hwBrasSbcMGCliAddrIndex": hwBrasSbcMGCliAddrIndex,
       "hwBrasSbcMGCliAddrVPN": hwBrasSbcMGCliAddrVPN,
       "hwBrasSbcMGCliAddrIP": hwBrasSbcMGCliAddrIP,
       "hwBrasSbcMGCliAddrRowStatus": hwBrasSbcMGCliAddrRowStatus,
       "hwBrasSbcMGServAddrTable": hwBrasSbcMGServAddrTable,
       "hwBrasSbcMGServAddrEntry": hwBrasSbcMGServAddrEntry,
       "hwBrasSbcMGServAddrIndex": hwBrasSbcMGServAddrIndex,
       "hwBrasSbcMGServAddrVPN": hwBrasSbcMGServAddrVPN,
       "hwBrasSbcMGServAddrIP1": hwBrasSbcMGServAddrIP1,
       "hwBrasSbcMGServAddrIP2": hwBrasSbcMGServAddrIP2,
       "hwBrasSbcMGServAddrIP3": hwBrasSbcMGServAddrIP3,
       "hwBrasSbcMGServAddrIP4": hwBrasSbcMGServAddrIP4,
       "hwBrasSbcMGServAddrRowStatus": hwBrasSbcMGServAddrRowStatus,
       "hwBrasSbcMGSofxAddrTable": hwBrasSbcMGSofxAddrTable,
       "hwBrasSbcMGSofxAddrEntry": hwBrasSbcMGSofxAddrEntry,
       "hwBrasSbcMGSofxAddrIndex": hwBrasSbcMGSofxAddrIndex,
       "hwBrasSbcMGSofxAddrVPN": hwBrasSbcMGSofxAddrVPN,
       "hwBrasSbcMGSofxAddrIP1": hwBrasSbcMGSofxAddrIP1,
       "hwBrasSbcMGSofxAddrIP2": hwBrasSbcMGSofxAddrIP2,
       "hwBrasSbcMGSofxAddrIP3": hwBrasSbcMGSofxAddrIP3,
       "hwBrasSbcMGSofxAddrIP4": hwBrasSbcMGSofxAddrIP4,
       "hwBrasSbcMGSofxAddrRowStatus": hwBrasSbcMGSofxAddrRowStatus,
       "hwBrasSbcMGIadmsAddrTable": hwBrasSbcMGIadmsAddrTable,
       "hwBrasSbcMGIadmsAddrEntry": hwBrasSbcMGIadmsAddrEntry,
       "hwBrasSbcMGIadmsAddrIndex": hwBrasSbcMGIadmsAddrIndex,
       "hwBrasSbcMGIadmsAddrVPN": hwBrasSbcMGIadmsAddrVPN,
       "hwBrasSbcMGIadmsAddrIP1": hwBrasSbcMGIadmsAddrIP1,
       "hwBrasSbcMGIadmsAddrIP2": hwBrasSbcMGIadmsAddrIP2,
       "hwBrasSbcMGIadmsAddrIP3": hwBrasSbcMGIadmsAddrIP3,
       "hwBrasSbcMGIadmsAddrIP4": hwBrasSbcMGIadmsAddrIP4,
       "hwBrasSbcMGIadmsAddrRowStatus": hwBrasSbcMGIadmsAddrRowStatus,
       "hwBrasSbcMGProtocolTable": hwBrasSbcMGProtocolTable,
       "hwBrasSbcMGProtocolEntry": hwBrasSbcMGProtocolEntry,
       "hwBrasSbcMGProtocolIndex": hwBrasSbcMGProtocolIndex,
       "hwBrasSbcMGProtocolSip": hwBrasSbcMGProtocolSip,
       "hwBrasSbcMGProtocolMgcp": hwBrasSbcMGProtocolMgcp,
       "hwBrasSbcMGProtocolH323": hwBrasSbcMGProtocolH323,
       "hwBrasSbcMGProtocolIadms": hwBrasSbcMGProtocolIadms,
       "hwBrasSbcMGProtocolUpath": hwBrasSbcMGProtocolUpath,
       "hwBrasSbcMGProtocolH248": hwBrasSbcMGProtocolH248,
       "hwBrasSbcMGProtocolRowStatus": hwBrasSbcMGProtocolRowStatus,
       "hwBrasSbcMGPortTable": hwBrasSbcMGPortTable,
       "hwBrasSbcMGPortEntry": hwBrasSbcMGPortEntry,
       "hwBrasSbcMGPortIndex": hwBrasSbcMGPortIndex,
       "hwBrasSbcMGPortNumber": hwBrasSbcMGPortNumber,
       "hwBrasSbcMGPortRowStatus": hwBrasSbcMGPortRowStatus,
       "hwBrasSbcMGPrefixTable": hwBrasSbcMGPrefixTable,
       "hwBrasSbcMGPrefixEntry": hwBrasSbcMGPrefixEntry,
       "hwBrasSbcMGPrefixIndex": hwBrasSbcMGPrefixIndex,
       "hwBrasSbcMGPrefixID": hwBrasSbcMGPrefixID,
       "hwBrasSbcMGPrefixRowStatus": hwBrasSbcMGPrefixRowStatus,
       "hwBrasSbcMGMdCliAddrTable": hwBrasSbcMGMdCliAddrTable,
       "hwBrasSbcMGMdCliAddrEntry": hwBrasSbcMGMdCliAddrEntry,
       "hwBrasSbcMGMdCliAddrIndex": hwBrasSbcMGMdCliAddrIndex,
       "hwBrasSbcMGMdCliAddrVPN": hwBrasSbcMGMdCliAddrVPN,
       "hwBrasSbcMGMdCliAddrIP1": hwBrasSbcMGMdCliAddrIP1,
       "hwBrasSbcMGMdCliAddrIP2": hwBrasSbcMGMdCliAddrIP2,
       "hwBrasSbcMGMdCliAddrIP3": hwBrasSbcMGMdCliAddrIP3,
       "hwBrasSbcMGMdCliAddrIP4": hwBrasSbcMGMdCliAddrIP4,
       "hwBrasSbcMGMdCliAddrVPNName": hwBrasSbcMGMdCliAddrVPNName,
       "hwBrasSbcMGMdCliAddrIf1": hwBrasSbcMGMdCliAddrIf1,
       "hwBrasSbcMGMdCliAddrSlotID1": hwBrasSbcMGMdCliAddrSlotID1,
       "hwBrasSbcMGMdCliAddrIf2": hwBrasSbcMGMdCliAddrIf2,
       "hwBrasSbcMGMdCliAddrSlotID2": hwBrasSbcMGMdCliAddrSlotID2,
       "hwBrasSbcMGMdCliAddrIf3": hwBrasSbcMGMdCliAddrIf3,
       "hwBrasSbcMGMdCliAddrSlotID3": hwBrasSbcMGMdCliAddrSlotID3,
       "hwBrasSbcMGMdCliAddrIf4": hwBrasSbcMGMdCliAddrIf4,
       "hwBrasSbcMGMdCliAddrSlotID4": hwBrasSbcMGMdCliAddrSlotID4,
       "hwBrasSbcMGMdCliAddrRowStatus": hwBrasSbcMGMdCliAddrRowStatus,
       "hwBrasSbcMGMdServAddrTable": hwBrasSbcMGMdServAddrTable,
       "hwBrasSbcMGMdServAddrEntry": hwBrasSbcMGMdServAddrEntry,
       "hwBrasSbcMGMdServAddrIndex": hwBrasSbcMGMdServAddrIndex,
       "hwBrasSbcMGMdServAddrVPN": hwBrasSbcMGMdServAddrVPN,
       "hwBrasSbcMGMdServAddrIP1": hwBrasSbcMGMdServAddrIP1,
       "hwBrasSbcMGMdServAddrIP2": hwBrasSbcMGMdServAddrIP2,
       "hwBrasSbcMGMdServAddrIP3": hwBrasSbcMGMdServAddrIP3,
       "hwBrasSbcMGMdServAddrIP4": hwBrasSbcMGMdServAddrIP4,
       "hwBrasSbcMGMdServAddrVPNName": hwBrasSbcMGMdServAddrVPNName,
       "hwBrasSbcMGMdServAddrIf1": hwBrasSbcMGMdServAddrIf1,
       "hwBrasSbcMGMdServAddrSlotID1": hwBrasSbcMGMdServAddrSlotID1,
       "hwBrasSbcMGMdServAddrIf2": hwBrasSbcMGMdServAddrIf2,
       "hwBrasSbcMGMdServAddrSlotID2": hwBrasSbcMGMdServAddrSlotID2,
       "hwBrasSbcMGMdServAddrIf3": hwBrasSbcMGMdServAddrIf3,
       "hwBrasSbcMGMdServAddrSlotID3": hwBrasSbcMGMdServAddrSlotID3,
       "hwBrasSbcMGMdServAddrIf4": hwBrasSbcMGMdServAddrIf4,
       "hwBrasSbcMGMdServAddrSlotID4": hwBrasSbcMGMdServAddrSlotID4,
       "hwBrasSbcMGMdServAddrRowStatus": hwBrasSbcMGMdServAddrRowStatus,
       "hwBrasSbcMGMatchTable": hwBrasSbcMGMatchTable,
       "hwBrasSbcMGMatchEntry": hwBrasSbcMGMatchEntry,
       "hwBrasSbcMGMatchIndex": hwBrasSbcMGMatchIndex,
       "hwBrasSbcMGMatchAcl": hwBrasSbcMGMatchAcl,
       "hwBrasSbcMGMatchRowStatus": hwBrasSbcMGMatchRowStatus,
       "hwBrasSbcAdmModuleTable": hwBrasSbcAdmModuleTable,
       "hwBrasSbcBackupGroupsTable": hwBrasSbcBackupGroupsTable,
       "hwBrasSbcBackupGroupTable": hwBrasSbcBackupGroupTable,
       "hwBrasSbcBackupGroupEntry": hwBrasSbcBackupGroupEntry,
       "hwBrasSbcBackupGroupID": hwBrasSbcBackupGroupID,
       "hwBrasSbcBackupGroupType": hwBrasSbcBackupGroupType,
       "hwBrasSbcBackupGroupInstanceName": hwBrasSbcBackupGroupInstanceName,
       "hwBrasSbcBackupGroupRowStatus": hwBrasSbcBackupGroupRowStatus,
       "hwBrasSbcSlotInforTable": hwBrasSbcSlotInforTable,
       "hwBrasSbcSlotInforEntry": hwBrasSbcSlotInforEntry,
       "hwBrasSbcBackupGroupIndex": hwBrasSbcBackupGroupIndex,
       "hwBrasSbcSlotIndex": hwBrasSbcSlotIndex,
       "hwBrasSbcCurrentSlotID": hwBrasSbcCurrentSlotID,
       "hwBrasSbcSlotCfgState": hwBrasSbcSlotCfgState,
       "hwBrasSbcSlotInforRowStatus": hwBrasSbcSlotInforRowStatus,
       "hwBrasSbcAdvance": hwBrasSbcAdvance,
       "hwBrasSbcAdvanceLeaves": hwBrasSbcAdvanceLeaves,
       "hwBrasSbcMediaPassEnable": hwBrasSbcMediaPassEnable,
       "hwBrasSbcMediaPassSyslogEnable": hwBrasSbcMediaPassSyslogEnable,
       "hwBrasSbcIntMediaPassEnable": hwBrasSbcIntMediaPassEnable,
       "hwBrasSbcRoamlimitEnable": hwBrasSbcRoamlimitEnable,
       "hwBrasSbcRoamlimitDefault": hwBrasSbcRoamlimitDefault,
       "hwBrasSbcRoamlimitSyslogEnable": hwBrasSbcRoamlimitSyslogEnable,
       "hwBrasSbcRoamlimitExtendEnable": hwBrasSbcRoamlimitExtendEnable,
       "hwBrasSbcHrpSynchronization": hwBrasSbcHrpSynchronization,
       "hwBrasSbcAdvanceTables": hwBrasSbcAdvanceTables,
       "hwBrasSbcMediaPassTable": hwBrasSbcMediaPassTable,
       "hwBrasSbcMediaPassEntry": hwBrasSbcMediaPassEntry,
       "hwBrasSbcMediaPassIndex": hwBrasSbcMediaPassIndex,
       "hwBrasSbcMediaPassAclNumber": hwBrasSbcMediaPassAclNumber,
       "hwBrasSbcMediaPassRowStatus": hwBrasSbcMediaPassRowStatus,
       "hwBrasSbcUsergroupTable": hwBrasSbcUsergroupTable,
       "hwBrasSbcUsergroupEntry": hwBrasSbcUsergroupEntry,
       "hwBrasSbcUsergroupIndex": hwBrasSbcUsergroupIndex,
       "hwBrasSbcUsergroupRowStatus": hwBrasSbcUsergroupRowStatus,
       "hwBrasSbcUsergroupRuleTable": hwBrasSbcUsergroupRuleTable,
       "hwBrasSbcUsergroupRuleEntry": hwBrasSbcUsergroupRuleEntry,
       "hwBrasSbcUsergroupRuleIndex": hwBrasSbcUsergroupRuleIndex,
       "hwBrasSbcUsergroupRuleType": hwBrasSbcUsergroupRuleType,
       "hwBrasSbcUsergroupRuleUserName": hwBrasSbcUsergroupRuleUserName,
       "hwBrasSbcUsergroupRuleRowStatus": hwBrasSbcUsergroupRuleRowStatus,
       "hwBrasSbcRtpSpecialAddrTable": hwBrasSbcRtpSpecialAddrTable,
       "hwBrasSbcRtpSpecialAddrEntry": hwBrasSbcRtpSpecialAddrEntry,
       "hwBrasSbcRtpSpecialAddrIndex": hwBrasSbcRtpSpecialAddrIndex,
       "hwBrasSbcRtpSpecialAddrAddr": hwBrasSbcRtpSpecialAddrAddr,
       "hwBrasSbcRtpSpecialAddrRowStatus": hwBrasSbcRtpSpecialAddrRowStatus,
       "hwBrasSbcRoamlimitTable": hwBrasSbcRoamlimitTable,
       "hwBrasSbcRoamlimitEntry": hwBrasSbcRoamlimitEntry,
       "hwBrasSbcRoamlimitIndex": hwBrasSbcRoamlimitIndex,
       "hwBrasSbcRoamlimitAclNumber": hwBrasSbcRoamlimitAclNumber,
       "hwBrasSbcRoamlimitRowStatus": hwBrasSbcRoamlimitRowStatus,
       "hwBrasSbcMediaUsersTable": hwBrasSbcMediaUsersTable,
       "hwBrasSbcMediaUsersEntry": hwBrasSbcMediaUsersEntry,
       "hwBrasSbcMediaUsersIndex": hwBrasSbcMediaUsersIndex,
       "hwBrasSbcMediaUsersType": hwBrasSbcMediaUsersType,
       "hwBrasSbcMediaUsersCallerID1": hwBrasSbcMediaUsersCallerID1,
       "hwBrasSbcMediaUsersCallerID2": hwBrasSbcMediaUsersCallerID2,
       "hwBrasSbcMediaUsersCallerID3": hwBrasSbcMediaUsersCallerID3,
       "hwBrasSbcMediaUsersCallerID4": hwBrasSbcMediaUsersCallerID4,
       "hwBrasSbcMediaUsersCalleeID1": hwBrasSbcMediaUsersCalleeID1,
       "hwBrasSbcMediaUsersCalleeID2": hwBrasSbcMediaUsersCalleeID2,
       "hwBrasSbcMediaUsersCalleeID3": hwBrasSbcMediaUsersCalleeID3,
       "hwBrasSbcMediaUsersCalleeID4": hwBrasSbcMediaUsersCalleeID4,
       "hwBrasSbcMediaUsersRowStatus": hwBrasSbcMediaUsersRowStatus,
       "hwBrasSbcIntercom": hwBrasSbcIntercom,
       "hwBrasSbcIntercomLeaves": hwBrasSbcIntercomLeaves,
       "hwBrasSbcIntercomEnable": hwBrasSbcIntercomEnable,
       "hwBrasSbcIntercomStatus": hwBrasSbcIntercomStatus,
       "hwBrasSbcIntercomTables": hwBrasSbcIntercomTables,
       "hwBrasSbcIntercomPrefixTable": hwBrasSbcIntercomPrefixTable,
       "hwBrasSbcIntercomPrefixEntry": hwBrasSbcIntercomPrefixEntry,
       "hwBrasSbcIntercomPrefixIndex": hwBrasSbcIntercomPrefixIndex,
       "hwBrasSbcIntercomPrefixDestAddr": hwBrasSbcIntercomPrefixDestAddr,
       "hwBrasSbcIntercomPrefixSrcAddr": hwBrasSbcIntercomPrefixSrcAddr,
       "hwBrasSbcIntercomPrefixRowStatus": hwBrasSbcIntercomPrefixRowStatus,
       "hwBrasSbcSessionCar": hwBrasSbcSessionCar,
       "hwBrasSbcSessionCarLeaves": hwBrasSbcSessionCarLeaves,
       "hwBrasSbcSessionCarEnable": hwBrasSbcSessionCarEnable,
       "hwBrasSbcSessionCarTables": hwBrasSbcSessionCarTables,
       "hwBrasSbcSessionCarDegreeTable": hwBrasSbcSessionCarDegreeTable,
       "hwBrasSbcSessionCarDegreeEntry": hwBrasSbcSessionCarDegreeEntry,
       "hwBrasSbcSessionCarDegreeID": hwBrasSbcSessionCarDegreeID,
       "hwBrasSbcSessionCarDegreeBandWidth": hwBrasSbcSessionCarDegreeBandWidth,
       "hwBrasSbcSessionCarDegreeDscp": hwBrasSbcSessionCarDegreeDscp,
       "hwBrasSbcSessionCarDegreeRowStatus": hwBrasSbcSessionCarDegreeRowStatus,
       "hwBrasSbcSessionCarRuleTable": hwBrasSbcSessionCarRuleTable,
       "hwBrasSbcSessionCarRuleEntry": hwBrasSbcSessionCarRuleEntry,
       "hwBrasSbcSessionCarRuleID": hwBrasSbcSessionCarRuleID,
       "hwBrasSbcSessionCarRuleName": hwBrasSbcSessionCarRuleName,
       "hwBrasSbcSessionCarRuleDegreeID": hwBrasSbcSessionCarRuleDegreeID,
       "hwBrasSbcSessionCarRuleDegreeBandWidth": hwBrasSbcSessionCarRuleDegreeBandWidth,
       "hwBrasSbcSessionCarRuleDegreeDscp": hwBrasSbcSessionCarRuleDegreeDscp,
       "hwBrasSbcSessionCarRuleRowStatus": hwBrasSbcSessionCarRuleRowStatus,
       "hwBrasSbcSecurity": hwBrasSbcSecurity,
       "hwBrasSbcSecurityLeaves": hwBrasSbcSecurityLeaves,
       "hwBrasSbcDefendEnable": hwBrasSbcDefendEnable,
       "hwBrasSbcDefendMode": hwBrasSbcDefendMode,
       "hwBrasSbcDefendActionLogEnable": hwBrasSbcDefendActionLogEnable,
       "hwBrasSbcCacEnable": hwBrasSbcCacEnable,
       "hwBrasSbcCacActionLogStatus": hwBrasSbcCacActionLogStatus,
       "hwBrasSbcDefendExtStatus": hwBrasSbcDefendExtStatus,
       "hwBrasSbcSignalingCarStatus": hwBrasSbcSignalingCarStatus,
       "hwBrasSbcIPCarStatus": hwBrasSbcIPCarStatus,
       "hwBrasSbcDynamicStatus": hwBrasSbcDynamicStatus,
       "hwBrasSbcSecurityTables": hwBrasSbcSecurityTables,
       "hwBrasSbcDefendConnectRateTable": hwBrasSbcDefendConnectRateTable,
       "hwBrasSbcDefendConnectRateEntry": hwBrasSbcDefendConnectRateEntry,
       "hwBrasSbcDefendConnectRateProtocol": hwBrasSbcDefendConnectRateProtocol,
       "hwBrasSbcDefendConnectRateThreshold": hwBrasSbcDefendConnectRateThreshold,
       "hwBrasSbcDefendConnectRatePercent": hwBrasSbcDefendConnectRatePercent,
       "hwBrasSbcDefendConnectRateRowStatus": hwBrasSbcDefendConnectRateRowStatus,
       "hwBrasSbcDefendUserConnectRateTable": hwBrasSbcDefendUserConnectRateTable,
       "hwBrasSbcDefendUserConnectRateEntry": hwBrasSbcDefendUserConnectRateEntry,
       "hwBrasSbcDefendUserConnectRateProtocol": hwBrasSbcDefendUserConnectRateProtocol,
       "hwBrasSbcDefendUserConnectRateThreshold": hwBrasSbcDefendUserConnectRateThreshold,
       "hwBrasSbcDefendUserConnectRatePercent": hwBrasSbcDefendUserConnectRatePercent,
       "hwBrasSbcDefendUserConnectRateRowStatus": hwBrasSbcDefendUserConnectRateRowStatus,
       "hwBrasSbcCacCallTotalTable": hwBrasSbcCacCallTotalTable,
       "hwBrasSbcCacCallTotalEntry": hwBrasSbcCacCallTotalEntry,
       "hwBrasSbcCacCallTotalProtocol": hwBrasSbcCacCallTotalProtocol,
       "hwBrasSbcCacCallTotalThreshold": hwBrasSbcCacCallTotalThreshold,
       "hwBrasSbcCacCallTotalPercent": hwBrasSbcCacCallTotalPercent,
       "hwBrasSbcCacCallTotalRowStatus": hwBrasSbcCacCallTotalRowStatus,
       "hwBrasSbcCacCallRateTable": hwBrasSbcCacCallRateTable,
       "hwBrasSbcCacCallRateEntry": hwBrasSbcCacCallRateEntry,
       "hwBrasSbcCacCallRateProtocol": hwBrasSbcCacCallRateProtocol,
       "hwBrasSbcCacCallRateThreshold": hwBrasSbcCacCallRateThreshold,
       "hwBrasSbcCacCallRatePercent": hwBrasSbcCacCallRatePercent,
       "hwBrasSbcCacCallRateRowStatus": hwBrasSbcCacCallRateRowStatus,
       "hwBrasSbcCacRegTotalTable": hwBrasSbcCacRegTotalTable,
       "hwBrasSbcCacRegTotalEntry": hwBrasSbcCacRegTotalEntry,
       "hwBrasSbcCacRegTotalProtocol": hwBrasSbcCacRegTotalProtocol,
       "hwBrasSbcCacRegTotalThreshold": hwBrasSbcCacRegTotalThreshold,
       "hwBrasSbcCacRegTotalPercent": hwBrasSbcCacRegTotalPercent,
       "hwBrasSbcCacRegTotalRowStatus": hwBrasSbcCacRegTotalRowStatus,
       "hwBrasSbcCacRegRateTable": hwBrasSbcCacRegRateTable,
       "hwBrasSbcCacRegRateEntry": hwBrasSbcCacRegRateEntry,
       "hwBrasSbcCacRegRateProtocol": hwBrasSbcCacRegRateProtocol,
       "hwBrasSbcCacRegRateThreshold": hwBrasSbcCacRegRateThreshold,
       "hwBrasSbcCacRegRatePercent": hwBrasSbcCacRegRatePercent,
       "hwBrasSbcCacRegRateRowStatus": hwBrasSbcCacRegRateRowStatus,
       "hwBrasSbcIPCarBandwidthTable": hwBrasSbcIPCarBandwidthTable,
       "hwBrasSbcIPCarBandwidthEntry": hwBrasSbcIPCarBandwidthEntry,
       "hwBrasSbcIPCarBWVpn": hwBrasSbcIPCarBWVpn,
       "hwBrasSbcIPCarBWAddress": hwBrasSbcIPCarBWAddress,
       "hwBrasSbcIPCarBWValue": hwBrasSbcIPCarBWValue,
       "hwBrasSbcIPCarBWRowStatus": hwBrasSbcIPCarBWRowStatus,
       "hwBrasSbcUdpTunnel": hwBrasSbcUdpTunnel,
       "hwBrasSbcUdpTunnelLeaves": hwBrasSbcUdpTunnelLeaves,
       "hwBrasSbcUdpTunnelEnable": hwBrasSbcUdpTunnelEnable,
       "hwBrasSbcUdpTunnelType": hwBrasSbcUdpTunnelType,
       "hwBrasSbcUdpTunnelSctpAddr": hwBrasSbcUdpTunnelSctpAddr,
       "hwBrasSbcUdpTunnelTunnelTimer": hwBrasSbcUdpTunnelTunnelTimer,
       "hwBrasSbcUdpTunnelTransportTimer": hwBrasSbcUdpTunnelTransportTimer,
       "hwBrasSbcUdpTunnelTables": hwBrasSbcUdpTunnelTables,
       "hwBrasSbcUdpTunnelPoolTable": hwBrasSbcUdpTunnelPoolTable,
       "hwBrasSbcUdpTunnelPoolEntry": hwBrasSbcUdpTunnelPoolEntry,
       "hwBrasSbcUdpTunnelPoolIndex": hwBrasSbcUdpTunnelPoolIndex,
       "hwBrasSbcUdpTunnelPoolStartIP": hwBrasSbcUdpTunnelPoolStartIP,
       "hwBrasSbcUdpTunnelPoolEndIP": hwBrasSbcUdpTunnelPoolEndIP,
       "hwBrasSbcUdpTunnelPoolRowStatus": hwBrasSbcUdpTunnelPoolRowStatus,
       "hwBrasSbcUdpTunnelPortTable": hwBrasSbcUdpTunnelPortTable,
       "hwBrasSbcUdpTunnelPortEntry": hwBrasSbcUdpTunnelPortEntry,
       "hwBrasSbcUdpTunnelPortProtocol": hwBrasSbcUdpTunnelPortProtocol,
       "hwBrasSbcUdpTunnelPortPort": hwBrasSbcUdpTunnelPortPort,
       "hwBrasSbcUdpTunnelPortRowStatus": hwBrasSbcUdpTunnelPortRowStatus,
       "hwBrasSbcUdpTunnelIfPortTable": hwBrasSbcUdpTunnelIfPortTable,
       "hwBrasSbcUdpTunnelIfPortEntry": hwBrasSbcUdpTunnelIfPortEntry,
       "hwBrasSbcUdpTunnelIfPortAddr": hwBrasSbcUdpTunnelIfPortAddr,
       "hwBrasSbcUdpTunnelIfPortPort": hwBrasSbcUdpTunnelIfPortPort,
       "hwBrasSbcUdpTunnelIfPortRowStatus": hwBrasSbcUdpTunnelIfPortRowStatus,
       "hwBrasSbcIms": hwBrasSbcIms,
       "hwBrasSbcImsLeaves": hwBrasSbcImsLeaves,
       "hwBrasSbcImsQosEnable": hwBrasSbcImsQosEnable,
       "hwBrasSbcImsMediaProxyEnable": hwBrasSbcImsMediaProxyEnable,
       "hwBrasSbcImsQosLogEnable": hwBrasSbcImsQosLogEnable,
       "hwBrasSbcImsMediaProxyLogEnable": hwBrasSbcImsMediaProxyLogEnable,
       "hwBrasSbcImsMGStatus": hwBrasSbcImsMGStatus,
       "hwBrasSbcImsMGConnectTimer": hwBrasSbcImsMGConnectTimer,
       "hwBrasSbcImsMGAgingTimer": hwBrasSbcImsMGAgingTimer,
       "hwBrasSbcImsMGCallSessionTimer": hwBrasSbcImsMGCallSessionTimer,
       "hwBrasSbcSctpStatus": hwBrasSbcSctpStatus,
       "hwBrasSbcIdlecutRtcpTimer": hwBrasSbcIdlecutRtcpTimer,
       "hwBrasSbcIdlecutRtpTimer": hwBrasSbcIdlecutRtpTimer,
       "hwBrasSbcMediaDetectStatus": hwBrasSbcMediaDetectStatus,
       "hwBrasSbcMediaOnewayStatus": hwBrasSbcMediaOnewayStatus,
       "hwBrasSbcImsMgLogEnable": hwBrasSbcImsMgLogEnable,
       "hwBrasSbcImsStatisticsEnable": hwBrasSbcImsStatisticsEnable,
       "hwBrasSbcTimerMediaAging": hwBrasSbcTimerMediaAging,
       "hwBrasSbcImsTables": hwBrasSbcImsTables,
       "hwBrasSbcImsConnectTable": hwBrasSbcImsConnectTable,
       "hwBrasSbcImsConnectEntry": hwBrasSbcImsConnectEntry,
       "hwBrasSbcImsConnectIndex": hwBrasSbcImsConnectIndex,
       "hwBrasSbcImsConnectPepID": hwBrasSbcImsConnectPepID,
       "hwBrasSbcImsConnectCliType": hwBrasSbcImsConnectCliType,
       "hwBrasSbcImsConnectCliIP": hwBrasSbcImsConnectCliIP,
       "hwBrasSbcImsConnectCliPort": hwBrasSbcImsConnectCliPort,
       "hwBrasSbcImsConnectServIP": hwBrasSbcImsConnectServIP,
       "hwBrasSbcImsConnectServPort": hwBrasSbcImsConnectServPort,
       "hwBrasSbcImsConnectRowStatus": hwBrasSbcImsConnectRowStatus,
       "hwBrasSbcImsBandTable": hwBrasSbcImsBandTable,
       "hwBrasSbcImsBandEntry": hwBrasSbcImsBandEntry,
       "hwBrasSbcImsBandIndex": hwBrasSbcImsBandIndex,
       "hwBrasSbcImsBandIfIndex": hwBrasSbcImsBandIfIndex,
       "hwBrasSbcImsBandIfName": hwBrasSbcImsBandIfName,
       "hwBrasSbcImsBandIfType": hwBrasSbcImsBandIfType,
       "hwBrasSbcImsBandValue": hwBrasSbcImsBandValue,
       "hwBrasSbcImsBandRowStatus": hwBrasSbcImsBandRowStatus,
       "hwBrasSbcImsActiveTable": hwBrasSbcImsActiveTable,
       "hwBrasSbcImsActiveEntry": hwBrasSbcImsActiveEntry,
       "hwBrasSbcImsActiveConnectId": hwBrasSbcImsActiveConnectId,
       "hwBrasSbcImsActiveStatus": hwBrasSbcImsActiveStatus,
       "hwBrasSbcImsActiveRowStatus": hwBrasSbcImsActiveRowStatus,
       "hwBrasSbcImsMGTable": hwBrasSbcImsMGTable,
       "hwBrasSbcImsMGEntry": hwBrasSbcImsMGEntry,
       "hwBrasSbcImsMGIndex": hwBrasSbcImsMGIndex,
       "hwBrasSbcImsMGDescription": hwBrasSbcImsMGDescription,
       "hwBrasSbcImsMGTableStatus": hwBrasSbcImsMGTableStatus,
       "hwBrasSbcImsMGProtocol": hwBrasSbcImsMGProtocol,
       "hwBrasSbcImsMGMidString": hwBrasSbcImsMGMidString,
       "hwBrasSbcImsMGInstanceName": hwBrasSbcImsMGInstanceName,
       "hwBrasSbcImsMGRowStatus": hwBrasSbcImsMGRowStatus,
       "hwBrasSbcImsMGIPTable": hwBrasSbcImsMGIPTable,
       "hwBrasSbcImsMGIPEntry": hwBrasSbcImsMGIPEntry,
       "hwBrasSbcImsMGIPType": hwBrasSbcImsMGIPType,
       "hwBrasSbcImsMGIPSN": hwBrasSbcImsMGIPSN,
       "hwBrasSbcImsMGIPVersion": hwBrasSbcImsMGIPVersion,
       "hwBrasSbcImsMGIPAddr": hwBrasSbcImsMGIPAddr,
       "hwBrasSbcImsMGIPPort": hwBrasSbcImsMGIPPort,
       "hwBrasSbcImsMGIPInterface": hwBrasSbcImsMGIPInterface,
       "hwBrasSbcImsMGIPRowStatus": hwBrasSbcImsMGIPRowStatus,
       "hwBrasSbcImsMGDomainTable": hwBrasSbcImsMGDomainTable,
       "hwBrasSbcImsMGDomainEntry": hwBrasSbcImsMGDomainEntry,
       "hwBrasSbcImsMGDomainType": hwBrasSbcImsMGDomainType,
       "hwBrasSbcImsMGDomainName": hwBrasSbcImsMGDomainName,
       "hwBrasSbcImsMGDomainMapIndex": hwBrasSbcImsMGDomainMapIndex,
       "hwBrasSbcImsMGDomainRowStatus": hwBrasSbcImsMGDomainRowStatus,
       "hwBrasSbcDualHoming": hwBrasSbcDualHoming,
       "hwBrasSbcDHLeaves": hwBrasSbcDHLeaves,
       "hwBrasSbcDHSIPDetectStatus": hwBrasSbcDHSIPDetectStatus,
       "hwBrasSbcDHSIPDetectTimer": hwBrasSbcDHSIPDetectTimer,
       "hwBrasSbcDHSIPDetectSourcePort": hwBrasSbcDHSIPDetectSourcePort,
       "hwBrasSbcDHSIPDetectFailCount": hwBrasSbcDHSIPDetectFailCount,
       "hwBrasSbcQoSReport": hwBrasSbcQoSReport,
       "hwBrasSbcQRLeaves": hwBrasSbcQRLeaves,
       "hwBrasSbcQRStatus": hwBrasSbcQRStatus,
       "hwBrasSbcQRBandWidth": hwBrasSbcQRBandWidth,
       "hwBrasSbcQRTables": hwBrasSbcQRTables,
       "hwBrasSbcMediaDefend": hwBrasSbcMediaDefend,
       "hwBrasSbcMediaDefendLeaves": hwBrasSbcMediaDefendLeaves,
       "hwBrasSbcMDStatus": hwBrasSbcMDStatus,
       "hwBrasSbcMediaDefendTables": hwBrasSbcMediaDefendTables,
       "hwBrasSbcMDLengthTable": hwBrasSbcMDLengthTable,
       "hwBrasSbcMDLengthEntry": hwBrasSbcMDLengthEntry,
       "hwBrasSbcMDLengthIndex": hwBrasSbcMDLengthIndex,
       "hwBrasSbcMDLengthMin": hwBrasSbcMDLengthMin,
       "hwBrasSbcMDLengthMax": hwBrasSbcMDLengthMax,
       "hwBrasSbcMDLengthRowStatus": hwBrasSbcMDLengthRowStatus,
       "hwBrasSbcMDStatisticTable": hwBrasSbcMDStatisticTable,
       "hwBrasSbcMDStatisticEntry": hwBrasSbcMDStatisticEntry,
       "hwBrasSbcMDStatisticIndex": hwBrasSbcMDStatisticIndex,
       "hwBrasSbcMDStatisticMinDrop": hwBrasSbcMDStatisticMinDrop,
       "hwBrasSbcMDStatisticMaxDrop": hwBrasSbcMDStatisticMaxDrop,
       "hwBrasSbcMDStatisticFragDrop": hwBrasSbcMDStatisticFragDrop,
       "hwBrasSbcMDStatisticFlowDrop": hwBrasSbcMDStatisticFlowDrop,
       "hwBrasSbcMDStatisticRowStatus": hwBrasSbcMDStatisticRowStatus,
       "hwBrasSbcSignalingNat": hwBrasSbcSignalingNat,
       "hwBrasSbcSignalingNatLeaves": hwBrasSbcSignalingNatLeaves,
       "hwBrasSbcNatSessionAgingTime": hwBrasSbcNatSessionAgingTime,
       "hwBrasSbcSignalingNatTables": hwBrasSbcSignalingNatTables,
       "hwBrasSbcNatCfgTable": hwBrasSbcNatCfgTable,
       "hwBrasSbcNatCfgEntry": hwBrasSbcNatCfgEntry,
       "hwBrasSbcNatGroupIndex": hwBrasSbcNatGroupIndex,
       "hwBrasSbcNatVpnNameIndex": hwBrasSbcNatVpnNameIndex,
       "hwBrasSbcNatInstanceName": hwBrasSbcNatInstanceName,
       "hwBrasSbcNatCfgRowStatus": hwBrasSbcNatCfgRowStatus,
       "hwBrasSbcNatAddressGroupTable": hwBrasSbcNatAddressGroupTable,
       "hwBrasSbcNatAddressGroupEntry": hwBrasSbcNatAddressGroupEntry,
       "hwNatAddrGrpIndex": hwNatAddrGrpIndex,
       "hwNatAddrGrpBeginningIpAddr": hwNatAddrGrpBeginningIpAddr,
       "hwNatAddrGrpEndingIpAddr": hwNatAddrGrpEndingIpAddr,
       "hwNatAddrGrpRefCount": hwNatAddrGrpRefCount,
       "hwNatAddrGrpVpnName": hwNatAddrGrpVpnName,
       "hwNatAddrGrpRowstatus": hwNatAddrGrpRowstatus,
       "hwBrasSbcBandwidthLimit": hwBrasSbcBandwidthLimit,
       "hwBrasSbcBWLimitLeaves": hwBrasSbcBWLimitLeaves,
       "hwBrasSbcBWLimitType": hwBrasSbcBWLimitType,
       "hwBrasSbcBWLimitValue": hwBrasSbcBWLimitValue,
       "hwBrasSbcView": hwBrasSbcView,
       "hwBrasSbcViewLeaves": hwBrasSbcViewLeaves,
       "hwBrasSbcSoftVersion": hwBrasSbcSoftVersion,
       "hwBrasSbcCpuUsage": hwBrasSbcCpuUsage,
       "hwBrasSbcUmsVersion": hwBrasSbcUmsVersion,
       "hwBrasSbcViewTables": hwBrasSbcViewTables,
       "hwBrasSbcStatisticTable": hwBrasSbcStatisticTable,
       "hwBrasSbcStatisticEntry": hwBrasSbcStatisticEntry,
       "hwBrasSbcStatisticIndex": hwBrasSbcStatisticIndex,
       "hwBrasSbcStatisticOffset": hwBrasSbcStatisticOffset,
       "hwBrasSbcStatisticDesc": hwBrasSbcStatisticDesc,
       "hwBrasSbcStatisticValue": hwBrasSbcStatisticValue,
       "hwBrasSbcStatisticTime": hwBrasSbcStatisticTime,
       "hwBrasSbcSip": hwBrasSbcSip,
       "hwBrasSbcSipLeaves": hwBrasSbcSipLeaves,
       "hwBrasSbcSipEnable": hwBrasSbcSipEnable,
       "hwBrasSbcSipSyslogEnable": hwBrasSbcSipSyslogEnable,
       "hwBrasSbcSipAnonymity": hwBrasSbcSipAnonymity,
       "hwBrasSbcSipCheckheartEnable": hwBrasSbcSipCheckheartEnable,
       "hwBrasSbcSipCallsessionTimer": hwBrasSbcSipCallsessionTimer,
       "hwBrasSbcSipPDHCountLimit": hwBrasSbcSipPDHCountLimit,
       "hwBrasSbcSipRegReduceStatus": hwBrasSbcSipRegReduceStatus,
       "hwBrasSbcSipRegReduceTimer": hwBrasSbcSipRegReduceTimer,
       "hwBrasSbcSipTables": hwBrasSbcSipTables,
       "hwBrasSbcSipWellknownPortTable": hwBrasSbcSipWellknownPortTable,
       "hwBrasSbcSipWellknownPortEntry": hwBrasSbcSipWellknownPortEntry,
       "hwBrasSbcSipWellknownPortIndex": hwBrasSbcSipWellknownPortIndex,
       "hwBrasSbcSipWellknownPortProtocol": hwBrasSbcSipWellknownPortProtocol,
       "hwBrasSbcSipWellknownPortAddr": hwBrasSbcSipWellknownPortAddr,
       "hwBrasSbcSipWellknownPortPort": hwBrasSbcSipWellknownPortPort,
       "hwBrasSbcSipWellknownPortRowStatus": hwBrasSbcSipWellknownPortRowStatus,
       "hwBrasSbcSipSignalMapTable": hwBrasSbcSipSignalMapTable,
       "hwBrasSbcSipSignalMapEntry": hwBrasSbcSipSignalMapEntry,
       "hwBrasSbcSipSignalMapAddr": hwBrasSbcSipSignalMapAddr,
       "hwBrasSbcSipSignalMapProtocol": hwBrasSbcSipSignalMapProtocol,
       "hwBrasSbcSipSignalMapNumber": hwBrasSbcSipSignalMapNumber,
       "hwBrasSbcSipSignalMapAddrType": hwBrasSbcSipSignalMapAddrType,
       "hwBrasSbcSipMediaMapTable": hwBrasSbcSipMediaMapTable,
       "hwBrasSbcSipMediaMapEntry": hwBrasSbcSipMediaMapEntry,
       "hwBrasSbcSipMediaMapAddr": hwBrasSbcSipMediaMapAddr,
       "hwBrasSbcSipMediaMapProtocol": hwBrasSbcSipMediaMapProtocol,
       "hwBrasSbcSipMediaMapNumber": hwBrasSbcSipMediaMapNumber,
       "hwBrasSbcSipIntercomMapSignalTable": hwBrasSbcSipIntercomMapSignalTable,
       "hwBrasSbcSipIntercomMapSignalEntry": hwBrasSbcSipIntercomMapSignalEntry,
       "hwBrasSbcSipIntercomMapSignalAddr": hwBrasSbcSipIntercomMapSignalAddr,
       "hwBrasSbcSipIntercomMapSignalProtocol": hwBrasSbcSipIntercomMapSignalProtocol,
       "hwBrasSbcSipIntercomMapSignalNumber": hwBrasSbcSipIntercomMapSignalNumber,
       "hwBrasSbcSipIntercomMapMediaTable": hwBrasSbcSipIntercomMapMediaTable,
       "hwBrasSbcSipIntercomMapMediaEntry": hwBrasSbcSipIntercomMapMediaEntry,
       "hwBrasSbcSipIntercomMapMediaAddr": hwBrasSbcSipIntercomMapMediaAddr,
       "hwBrasSbcSipIntercomMapMediaProtocol": hwBrasSbcSipIntercomMapMediaProtocol,
       "hwBrasSbcSipIntercomMapMediaNumber": hwBrasSbcSipIntercomMapMediaNumber,
       "hwBrasSbcSipStatSignalPacketTable": hwBrasSbcSipStatSignalPacketTable,
       "hwBrasSbcSipStatSignalPacketEntry": hwBrasSbcSipStatSignalPacketEntry,
       "hwBrasSbcSipStatSignalPacketIndex": hwBrasSbcSipStatSignalPacketIndex,
       "hwBrasSbcSipStatSignalPacketInNumber": hwBrasSbcSipStatSignalPacketInNumber,
       "hwBrasSbcSipStatSignalPacketInOctet": hwBrasSbcSipStatSignalPacketInOctet,
       "hwBrasSbcSipStatSignalPacketOutNumber": hwBrasSbcSipStatSignalPacketOutNumber,
       "hwBrasSbcSipStatSignalPacketOutOctet": hwBrasSbcSipStatSignalPacketOutOctet,
       "hwBrasSbcSipStatSignalPacketRowStatus": hwBrasSbcSipStatSignalPacketRowStatus,
       "hwBrasSbcMgcp": hwBrasSbcMgcp,
       "hwBrasSbcMgcpLeaves": hwBrasSbcMgcpLeaves,
       "hwBrasSbcMgcpSyslogEnable": hwBrasSbcMgcpSyslogEnable,
       "hwBrasSbcMgcpAuepTimer": hwBrasSbcMgcpAuepTimer,
       "hwBrasSbcMgcpCcbTimer": hwBrasSbcMgcpCcbTimer,
       "hwBrasSbcMgcpTxTimer": hwBrasSbcMgcpTxTimer,
       "hwBrasSbcMgcpEnable": hwBrasSbcMgcpEnable,
       "hwBrasSbcMgcpPDHCountLimit": hwBrasSbcMgcpPDHCountLimit,
       "hwBrasSbcMgcpTables": hwBrasSbcMgcpTables,
       "hwBrasSbcMgcpWellknownPortTable": hwBrasSbcMgcpWellknownPortTable,
       "hwBrasSbcMgcpWellknownPortEntry": hwBrasSbcMgcpWellknownPortEntry,
       "hwBrasSbcMgcpWellknownPortIndex": hwBrasSbcMgcpWellknownPortIndex,
       "hwBrasSbcMgcpWellknownPortProtocol": hwBrasSbcMgcpWellknownPortProtocol,
       "hwBrasSbcMgcpWellknownPortAddr": hwBrasSbcMgcpWellknownPortAddr,
       "hwBrasSbcMgcpWellknownPortPort": hwBrasSbcMgcpWellknownPortPort,
       "hwBrasSbcMgcpWellknownPortRowStatus": hwBrasSbcMgcpWellknownPortRowStatus,
       "hwBrasSbcMgcpSignalMapTable": hwBrasSbcMgcpSignalMapTable,
       "hwBrasSbcMgcpSignalMapEntry": hwBrasSbcMgcpSignalMapEntry,
       "hwBrasSbcMgcpSignalMapAddr": hwBrasSbcMgcpSignalMapAddr,
       "hwBrasSbcMgcpSignalMapProtocol": hwBrasSbcMgcpSignalMapProtocol,
       "hwBrasSbcMgcpSignalMapNumber": hwBrasSbcMgcpSignalMapNumber,
       "hwBrasSbcMgcpSignalMapAddrType": hwBrasSbcMgcpSignalMapAddrType,
       "hwBrasSbcMgcpMediaMapTable": hwBrasSbcMgcpMediaMapTable,
       "hwBrasSbcMgcpMediaMapEntry": hwBrasSbcMgcpMediaMapEntry,
       "hwBrasSbcMgcpMediaMapAddr": hwBrasSbcMgcpMediaMapAddr,
       "hwBrasSbcMgcpMediaMapProtocol": hwBrasSbcMgcpMediaMapProtocol,
       "hwBrasSbcMgcpMediaMapNumber": hwBrasSbcMgcpMediaMapNumber,
       "hwBrasSbcMgcpIntercomMapSignalTable": hwBrasSbcMgcpIntercomMapSignalTable,
       "hwBrasSbcMgcpIntercomMapSignalEntry": hwBrasSbcMgcpIntercomMapSignalEntry,
       "hwBrasSbcMgcpIntercomMapSignalAddr": hwBrasSbcMgcpIntercomMapSignalAddr,
       "hwBrasSbcMgcpIntercomMapSignalProtocol": hwBrasSbcMgcpIntercomMapSignalProtocol,
       "hwBrasSbcMgcpIntercomMapSignalNumber": hwBrasSbcMgcpIntercomMapSignalNumber,
       "hwBrasSbcMgcpIntercomMapMediaTable": hwBrasSbcMgcpIntercomMapMediaTable,
       "hwBrasSbcMgcpIntercomMapMediaEntry": hwBrasSbcMgcpIntercomMapMediaEntry,
       "hwBrasSbcMgcpIntercomMapMediaAddr": hwBrasSbcMgcpIntercomMapMediaAddr,
       "hwBrasSbcMgcpIntercomMapMediaProtocol": hwBrasSbcMgcpIntercomMapMediaProtocol,
       "hwBrasSbcMgcpIntercomMapMediaNumber": hwBrasSbcMgcpIntercomMapMediaNumber,
       "hwBrasSbcMgcpStatSignalPacketTable": hwBrasSbcMgcpStatSignalPacketTable,
       "hwBrasSbcMgcpStatSignalPacketEntry": hwBrasSbcMgcpStatSignalPacketEntry,
       "hwBrasSbcMgcpStatSignalPacketIndex": hwBrasSbcMgcpStatSignalPacketIndex,
       "hwBrasSbcMgcpStatSignalPacketInNumber": hwBrasSbcMgcpStatSignalPacketInNumber,
       "hwBrasSbcMgcpStatSignalPacketInOctet": hwBrasSbcMgcpStatSignalPacketInOctet,
       "hwBrasSbcMgcpStatSignalPacketOutNumber": hwBrasSbcMgcpStatSignalPacketOutNumber,
       "hwBrasSbcMgcpStatSignalPacketOutOctet": hwBrasSbcMgcpStatSignalPacketOutOctet,
       "hwBrasSbcMgcpStatSignalPacketRowStatus": hwBrasSbcMgcpStatSignalPacketRowStatus,
       "hwBrasSbcIadms": hwBrasSbcIadms,
       "hwBrasSbcIadmsLeaves": hwBrasSbcIadmsLeaves,
       "hwBrasSbcIadmsEnable": hwBrasSbcIadmsEnable,
       "hwBrasSbcIadmsSyslogEnable": hwBrasSbcIadmsSyslogEnable,
       "hwBrasSbcIadmsRegRefreshEnable": hwBrasSbcIadmsRegRefreshEnable,
       "hwBrasSbcIadmsTimer": hwBrasSbcIadmsTimer,
       "hwBrasSbcIadmsTables": hwBrasSbcIadmsTables,
       "hwBrasSbcIadmsWellknownPortTable": hwBrasSbcIadmsWellknownPortTable,
       "hwBrasSbcIadmsWellknownPortEntry": hwBrasSbcIadmsWellknownPortEntry,
       "hwBrasSbcIadmsWellknownPortIndex": hwBrasSbcIadmsWellknownPortIndex,
       "hwBrasSbcIadmsWellknownPortProtocol": hwBrasSbcIadmsWellknownPortProtocol,
       "hwBrasSbcIadmsWellknownPortAddr": hwBrasSbcIadmsWellknownPortAddr,
       "hwBrasSbcIadmsWellknownPortPort": hwBrasSbcIadmsWellknownPortPort,
       "hwBrasSbcIadmsWellknownPortRowStatus": hwBrasSbcIadmsWellknownPortRowStatus,
       "hwBrasSbcIadmsMibRegTable": hwBrasSbcIadmsMibRegTable,
       "hwBrasSbcIadmsMibRegEntry": hwBrasSbcIadmsMibRegEntry,
       "hwBrasSbcIadmsMibRegVersion": hwBrasSbcIadmsMibRegVersion,
       "hwBrasSbcIadmsMibRegRegister": hwBrasSbcIadmsMibRegRegister,
       "hwBrasSbcIadmsMibRegRowStatus": hwBrasSbcIadmsMibRegRowStatus,
       "hwBrasSbcIadmsSignalMapTable": hwBrasSbcIadmsSignalMapTable,
       "hwBrasSbcIadmsSignalMapEntry": hwBrasSbcIadmsSignalMapEntry,
       "hwBrasSbcIadmsSignalMapAddr": hwBrasSbcIadmsSignalMapAddr,
       "hwBrasSbcIadmsSignalMapProtocol": hwBrasSbcIadmsSignalMapProtocol,
       "hwBrasSbcIadmsSignalMapNumber": hwBrasSbcIadmsSignalMapNumber,
       "hwBrasSbcIadmsSignalMapAddrType": hwBrasSbcIadmsSignalMapAddrType,
       "hwBrasSbcIadmsMediaMapTable": hwBrasSbcIadmsMediaMapTable,
       "hwBrasSbcIadmsMediaMapEntry": hwBrasSbcIadmsMediaMapEntry,
       "hwBrasSbcIadmsMediaMapAddr": hwBrasSbcIadmsMediaMapAddr,
       "hwBrasSbcIadmsMediaMapProtocol": hwBrasSbcIadmsMediaMapProtocol,
       "hwBrasSbcIadmsMediaMapNumber": hwBrasSbcIadmsMediaMapNumber,
       "hwBrasSbcIadmsIntercomMapSignalTable": hwBrasSbcIadmsIntercomMapSignalTable,
       "hwBrasSbcIadmsIntercomMapSignalEntry": hwBrasSbcIadmsIntercomMapSignalEntry,
       "hwBrasSbcIadmsIntercomMapSignalAddr": hwBrasSbcIadmsIntercomMapSignalAddr,
       "hwBrasSbcIadmsIntercomMapSignalProtocol": hwBrasSbcIadmsIntercomMapSignalProtocol,
       "hwBrasSbcIadmsIntercomMapSignalNumber": hwBrasSbcIadmsIntercomMapSignalNumber,
       "hwBrasSbcIadmsIntercomMapMediaTable": hwBrasSbcIadmsIntercomMapMediaTable,
       "hwBrasSbcIadmsIntercomMapMediaEntry": hwBrasSbcIadmsIntercomMapMediaEntry,
       "hwBrasSbcIadmsIntercomMapMediaAddr": hwBrasSbcIadmsIntercomMapMediaAddr,
       "hwBrasSbcIadmsIntercomMapMediaProtocol": hwBrasSbcIadmsIntercomMapMediaProtocol,
       "hwBrasSbcIadmsIntercomMapMediaNumber": hwBrasSbcIadmsIntercomMapMediaNumber,
       "hwBrasSbcIadmsStatSignalPacketTable": hwBrasSbcIadmsStatSignalPacketTable,
       "hwBrasSbcIadmsStatSignalPacketEntry": hwBrasSbcIadmsStatSignalPacketEntry,
       "hwBrasSbcIadmsStatSignalPacketIndex": hwBrasSbcIadmsStatSignalPacketIndex,
       "hwBrasSbcIadmsStatSignalPacketInNumber": hwBrasSbcIadmsStatSignalPacketInNumber,
       "hwBrasSbcIadmsStatSignalPacketInOctet": hwBrasSbcIadmsStatSignalPacketInOctet,
       "hwBrasSbcIadmsStatSignalPacketOutNumber": hwBrasSbcIadmsStatSignalPacketOutNumber,
       "hwBrasSbcIadmsStatSignalPacketOutOctet": hwBrasSbcIadmsStatSignalPacketOutOctet,
       "hwBrasSbcIadmsStatSignalPacketRowStatus": hwBrasSbcIadmsStatSignalPacketRowStatus,
       "hwBrasSbcH323": hwBrasSbcH323,
       "hwBrasSbcH323Leaves": hwBrasSbcH323Leaves,
       "hwBrasSbcH323Enable": hwBrasSbcH323Enable,
       "hwBrasSbcH323SyslogEnable": hwBrasSbcH323SyslogEnable,
       "hwBrasSbcH323CallsessionTimer": hwBrasSbcH323CallsessionTimer,
       "hwBrasSbcH323Q931WellknownPort": hwBrasSbcH323Q931WellknownPort,
       "hwBrasSbcH323PDHCountLimit": hwBrasSbcH323PDHCountLimit,
       "hwBrasSbcH323Tables": hwBrasSbcH323Tables,
       "hwBrasSbcH323WellknownPortTable": hwBrasSbcH323WellknownPortTable,
       "hwBrasSbcH323WellknownPortEntry": hwBrasSbcH323WellknownPortEntry,
       "hwBrasSbcH323WellknownPortIndex": hwBrasSbcH323WellknownPortIndex,
       "hwBrasSbcH323WellknownPortProtocol": hwBrasSbcH323WellknownPortProtocol,
       "hwBrasSbcH323WellknownPortAddr": hwBrasSbcH323WellknownPortAddr,
       "hwBrasSbcH323WellknownPortPort": hwBrasSbcH323WellknownPortPort,
       "hwBrasSbcH323WellknownPortRowStatus": hwBrasSbcH323WellknownPortRowStatus,
       "hwBrasSbcH323SignalMapTable": hwBrasSbcH323SignalMapTable,
       "hwBrasSbcH323SignalMapEntry": hwBrasSbcH323SignalMapEntry,
       "hwBrasSbcH323SignalMapAddr": hwBrasSbcH323SignalMapAddr,
       "hwBrasSbcH323SignalMapProtocol": hwBrasSbcH323SignalMapProtocol,
       "hwBrasSbcH323SignalMapNumber": hwBrasSbcH323SignalMapNumber,
       "hwBrasSbcH323SignalMapAddrType": hwBrasSbcH323SignalMapAddrType,
       "hwBrasSbcH323MediaMapTable": hwBrasSbcH323MediaMapTable,
       "hwBrasSbcH323MediaMapEntry": hwBrasSbcH323MediaMapEntry,
       "hwBrasSbcH323MediaMapAddr": hwBrasSbcH323MediaMapAddr,
       "hwBrasSbcH323MediaMapProtocol": hwBrasSbcH323MediaMapProtocol,
       "hwBrasSbcH323MediaMapNumber": hwBrasSbcH323MediaMapNumber,
       "hwBrasSbcH323IntercomMapSignalTable": hwBrasSbcH323IntercomMapSignalTable,
       "hwBrasSbcH323IntercomMapSignalEntry": hwBrasSbcH323IntercomMapSignalEntry,
       "hwBrasSbcH323IntercomMapSignalAddr": hwBrasSbcH323IntercomMapSignalAddr,
       "hwBrasSbcH323IntercomMapSignalProtocol": hwBrasSbcH323IntercomMapSignalProtocol,
       "hwBrasSbcH323IntercomMapSignalNumber": hwBrasSbcH323IntercomMapSignalNumber,
       "hwBrasSbcH323IntercomMapMediaTable": hwBrasSbcH323IntercomMapMediaTable,
       "hwBrasSbcH323IntercomMapMediaEntry": hwBrasSbcH323IntercomMapMediaEntry,
       "hwBrasSbcH323IntercomMapMediaAddr": hwBrasSbcH323IntercomMapMediaAddr,
       "hwBrasSbcH323IntercomMapMediaProtocol": hwBrasSbcH323IntercomMapMediaProtocol,
       "hwBrasSbcH323IntercomMapMediaNumber": hwBrasSbcH323IntercomMapMediaNumber,
       "hwBrasSbcH323StatSignalPacketTable": hwBrasSbcH323StatSignalPacketTable,
       "hwBrasSbcH323StatSignalPacketEntry": hwBrasSbcH323StatSignalPacketEntry,
       "hwBrasSbcH323StatSignalPacketIndex": hwBrasSbcH323StatSignalPacketIndex,
       "hwBrasSbcH323StatSignalPacketInNumber": hwBrasSbcH323StatSignalPacketInNumber,
       "hwBrasSbcH323StatSignalPacketInOctet": hwBrasSbcH323StatSignalPacketInOctet,
       "hwBrasSbcH323StatSignalPacketOutNumber": hwBrasSbcH323StatSignalPacketOutNumber,
       "hwBrasSbcH323StatSignalPacketOutOctet": hwBrasSbcH323StatSignalPacketOutOctet,
       "hwBrasSbcH323StatSignalPacketRowStatus": hwBrasSbcH323StatSignalPacketRowStatus,
       "hwBrasSbcIdo": hwBrasSbcIdo,
       "hwBrasSbcIdoLeaves": hwBrasSbcIdoLeaves,
       "hwBrasSbcIdoEnable": hwBrasSbcIdoEnable,
       "hwBrasSbcIdoSyslogEnable": hwBrasSbcIdoSyslogEnable,
       "hwBrasSbcIdoTables": hwBrasSbcIdoTables,
       "hwBrasSbcIdoWellknownPortTable": hwBrasSbcIdoWellknownPortTable,
       "hwBrasSbcIdoWellknownPortEntry": hwBrasSbcIdoWellknownPortEntry,
       "hwBrasSbcIdoWellknownPortIndex": hwBrasSbcIdoWellknownPortIndex,
       "hwBrasSbcIdoWellknownPortProtocol": hwBrasSbcIdoWellknownPortProtocol,
       "hwBrasSbcIdoWellknownPortAddr": hwBrasSbcIdoWellknownPortAddr,
       "hwBrasSbcIdoWellknownPortPort": hwBrasSbcIdoWellknownPortPort,
       "hwBrasSbcIdoWellknownPortRowStatus": hwBrasSbcIdoWellknownPortRowStatus,
       "hwBrasSbcIdoSignalMapTable": hwBrasSbcIdoSignalMapTable,
       "hwBrasSbcIdoSignalMapEntry": hwBrasSbcIdoSignalMapEntry,
       "hwBrasSbcIdoSignalMapAddr": hwBrasSbcIdoSignalMapAddr,
       "hwBrasSbcIdoSignalMapProtocol": hwBrasSbcIdoSignalMapProtocol,
       "hwBrasSbcIdoSignalMapNumber": hwBrasSbcIdoSignalMapNumber,
       "hwBrasSbcIdoSignalMapAddrType": hwBrasSbcIdoSignalMapAddrType,
       "hwBrasSbcIdoIntercomMapSignalTable": hwBrasSbcIdoIntercomMapSignalTable,
       "hwBrasSbcIdoIntercomMapSignalEntry": hwBrasSbcIdoIntercomMapSignalEntry,
       "hwBrasSbcIdoIntercomMapSignalAddr": hwBrasSbcIdoIntercomMapSignalAddr,
       "hwBrasSbcIdoIntercomMapSignalProtocol": hwBrasSbcIdoIntercomMapSignalProtocol,
       "hwBrasSbcIdoIntercomMapSignalNumber": hwBrasSbcIdoIntercomMapSignalNumber,
       "hwBrasSbcIdoStatSignalPacketTable": hwBrasSbcIdoStatSignalPacketTable,
       "hwBrasSbcIdoStatSignalPacketEntry": hwBrasSbcIdoStatSignalPacketEntry,
       "hwBrasSbcIdoStatSignalPacketIndex": hwBrasSbcIdoStatSignalPacketIndex,
       "hwBrasSbcIdoStatSignalPacketInNumber": hwBrasSbcIdoStatSignalPacketInNumber,
       "hwBrasSbcIdoStatSignalPacketInOctet": hwBrasSbcIdoStatSignalPacketInOctet,
       "hwBrasSbcIdoStatSignalPacketOutNumber": hwBrasSbcIdoStatSignalPacketOutNumber,
       "hwBrasSbcIdoStatSignalPacketOutOctet": hwBrasSbcIdoStatSignalPacketOutOctet,
       "hwBrasSbcIdoStatSignalPacketRowStatus": hwBrasSbcIdoStatSignalPacketRowStatus,
       "hwBrasSbcH248": hwBrasSbcH248,
       "hwBrasSbcH248Leaves": hwBrasSbcH248Leaves,
       "hwBrasSbcH248Enable": hwBrasSbcH248Enable,
       "hwBrasSbcH248SyslogEnable": hwBrasSbcH248SyslogEnable,
       "hwBrasSbcH248CcbTimer": hwBrasSbcH248CcbTimer,
       "hwBrasSbcH248UserAgeTimer": hwBrasSbcH248UserAgeTimer,
       "hwBrasSbcH248PDHCountLimit": hwBrasSbcH248PDHCountLimit,
       "hwBrasSbcH248Tables": hwBrasSbcH248Tables,
       "hwBrasSbcH248WellknownPortTable": hwBrasSbcH248WellknownPortTable,
       "hwBrasSbcH248WellknownPortEntry": hwBrasSbcH248WellknownPortEntry,
       "hwBrasSbcH248WellknownPortIndex": hwBrasSbcH248WellknownPortIndex,
       "hwBrasSbcH248WellknownPortProtocol": hwBrasSbcH248WellknownPortProtocol,
       "hwBrasSbcH248WellknownPortAddr": hwBrasSbcH248WellknownPortAddr,
       "hwBrasSbcH248WellknownPortPort": hwBrasSbcH248WellknownPortPort,
       "hwBrasSbcH248WellknownPortRowStatus": hwBrasSbcH248WellknownPortRowStatus,
       "hwBrasSbcH248SignalMapTable": hwBrasSbcH248SignalMapTable,
       "hwBrasSbcH248SignalMapEntry": hwBrasSbcH248SignalMapEntry,
       "hwBrasSbcH248SignalMapAddr": hwBrasSbcH248SignalMapAddr,
       "hwBrasSbcH248SignalMapProtocol": hwBrasSbcH248SignalMapProtocol,
       "hwBrasSbcH248SignalMapNumber": hwBrasSbcH248SignalMapNumber,
       "hwBrasSbcH248SignalMapAddrType": hwBrasSbcH248SignalMapAddrType,
       "hwBrasSbcH248MediaMapTable": hwBrasSbcH248MediaMapTable,
       "hwBrasSbcH248MediaMapEntry": hwBrasSbcH248MediaMapEntry,
       "hwBrasSbcH248MediaMapAddr": hwBrasSbcH248MediaMapAddr,
       "hwBrasSbcH248MediaMapProtocol": hwBrasSbcH248MediaMapProtocol,
       "hwBrasSbcH248MediaMapNumber": hwBrasSbcH248MediaMapNumber,
       "hwBrasSbcH248IntercomMapSignalTable": hwBrasSbcH248IntercomMapSignalTable,
       "hwBrasSbcH248IntercomMapSignalEntry": hwBrasSbcH248IntercomMapSignalEntry,
       "hwBrasSbcH248IntercomMapSignalAddr": hwBrasSbcH248IntercomMapSignalAddr,
       "hwBrasSbcH248IntercomMapSignalProtocol": hwBrasSbcH248IntercomMapSignalProtocol,
       "hwBrasSbcH248IntercomMapSignalNumber": hwBrasSbcH248IntercomMapSignalNumber,
       "hwBrasSbcH248IntercomMapMediaTable": hwBrasSbcH248IntercomMapMediaTable,
       "hwBrasSbcH248IntercomMapMediaEntry": hwBrasSbcH248IntercomMapMediaEntry,
       "hwBrasSbcH248IntercomMapMediaAddr": hwBrasSbcH248IntercomMapMediaAddr,
       "hwBrasSbcH248IntercomMapMediaProtocol": hwBrasSbcH248IntercomMapMediaProtocol,
       "hwBrasSbcH248IntercomMapMediaNumber": hwBrasSbcH248IntercomMapMediaNumber,
       "hwBrasSbcH248StatSignalPacketTable": hwBrasSbcH248StatSignalPacketTable,
       "hwBrasSbcH248StatSignalPacketEntry": hwBrasSbcH248StatSignalPacketEntry,
       "hwBrasSbcH248StatSignalPacketIndex": hwBrasSbcH248StatSignalPacketIndex,
       "hwBrasSbcH248StatSignalPacketInNumber": hwBrasSbcH248StatSignalPacketInNumber,
       "hwBrasSbcH248StatSignalPacketInOctet": hwBrasSbcH248StatSignalPacketInOctet,
       "hwBrasSbcH248StatSignalPacketOutNumber": hwBrasSbcH248StatSignalPacketOutNumber,
       "hwBrasSbcH248StatSignalPacketOutOctet": hwBrasSbcH248StatSignalPacketOutOctet,
       "hwBrasSbcH248StatSignalPacketRowStatus": hwBrasSbcH248StatSignalPacketRowStatus,
       "hwBrasSbcUpath": hwBrasSbcUpath,
       "hwBrasSbcUpathLeaves": hwBrasSbcUpathLeaves,
       "hwBrasSbcUpathEnable": hwBrasSbcUpathEnable,
       "hwBrasSbcUpathSyslogEnable": hwBrasSbcUpathSyslogEnable,
       "hwBrasSbcUpathCallsessionTimer": hwBrasSbcUpathCallsessionTimer,
       "hwBrasSbcUpathHeartbeatTimer": hwBrasSbcUpathHeartbeatTimer,
       "hwBrasSbcUpathTables": hwBrasSbcUpathTables,
       "hwBrasSbcUpathWellknownPortTable": hwBrasSbcUpathWellknownPortTable,
       "hwBrasSbcUpathWellknownPortEntry": hwBrasSbcUpathWellknownPortEntry,
       "hwBrasSbcUpathWellknownPortIndex": hwBrasSbcUpathWellknownPortIndex,
       "hwBrasSbcUpathWellknownPortProtocol": hwBrasSbcUpathWellknownPortProtocol,
       "hwBrasSbcUpathWellknownPortAddr": hwBrasSbcUpathWellknownPortAddr,
       "hwBrasSbcUpathWellknownPortPort": hwBrasSbcUpathWellknownPortPort,
       "hwBrasSbcUpathWellknownPortRowStatus": hwBrasSbcUpathWellknownPortRowStatus,
       "hwBrasSbcUpathSignalMapTable": hwBrasSbcUpathSignalMapTable,
       "hwBrasSbcUpathSignalMapEntry": hwBrasSbcUpathSignalMapEntry,
       "hwBrasSbcUpathSignalMapAddr": hwBrasSbcUpathSignalMapAddr,
       "hwBrasSbcUpathSignalMapProtocol": hwBrasSbcUpathSignalMapProtocol,
       "hwBrasSbcUpathSignalMapNumber": hwBrasSbcUpathSignalMapNumber,
       "hwBrasSbcUpathSignalMapAddrType": hwBrasSbcUpathSignalMapAddrType,
       "hwBrasSbcUpathMediaMapTable": hwBrasSbcUpathMediaMapTable,
       "hwBrasSbcUpathMediaMapEntry": hwBrasSbcUpathMediaMapEntry,
       "hwBrasSbcUpathMediaMapAddr": hwBrasSbcUpathMediaMapAddr,
       "hwBrasSbcUpathMediaMapProtocol": hwBrasSbcUpathMediaMapProtocol,
       "hwBrasSbcUpathMediaMapNumber": hwBrasSbcUpathMediaMapNumber,
       "hwBrasSbcUpathIntercomMapSignalTable": hwBrasSbcUpathIntercomMapSignalTable,
       "hwBrasSbcUpathIntercomMapSignalEntry": hwBrasSbcUpathIntercomMapSignalEntry,
       "hwBrasSbcUpathIntercomMapSignalAddr": hwBrasSbcUpathIntercomMapSignalAddr,
       "hwBrasSbcUpathIntercomMapSignalProtocol": hwBrasSbcUpathIntercomMapSignalProtocol,
       "hwBrasSbcUpathIntercomMapSignalNumber": hwBrasSbcUpathIntercomMapSignalNumber,
       "hwBrasSbcUpathIntercomMapMediaTable": hwBrasSbcUpathIntercomMapMediaTable,
       "hwBrasSbcUpathIntercomMapMediaEntry": hwBrasSbcUpathIntercomMapMediaEntry,
       "hwBrasSbcUpathIntercomMapMediaAddr": hwBrasSbcUpathIntercomMapMediaAddr,
       "hwBrasSbcUpathIntercomMapMediaProtocol": hwBrasSbcUpathIntercomMapMediaProtocol,
       "hwBrasSbcUpathIntercomMapMediaNumber": hwBrasSbcUpathIntercomMapMediaNumber,
       "hwBrasSbcUpathStatSignalPacketTable": hwBrasSbcUpathStatSignalPacketTable,
       "hwBrasSbcUpathStatSignalPacketEntry": hwBrasSbcUpathStatSignalPacketEntry,
       "hwBrasSbcUpathStatSignalPacketIndex": hwBrasSbcUpathStatSignalPacketIndex,
       "hwBrasSbcUpathStatSignalPacketInNumber": hwBrasSbcUpathStatSignalPacketInNumber,
       "hwBrasSbcUpathStatSignalPacketInOctet": hwBrasSbcUpathStatSignalPacketInOctet,
       "hwBrasSbcUpathStatSignalPacketOutNumber": hwBrasSbcUpathStatSignalPacketOutNumber,
       "hwBrasSbcUpathStatSignalPacketOutOctet": hwBrasSbcUpathStatSignalPacketOutOctet,
       "hwBrasSbcUpathStatSignalPacketRowStatus": hwBrasSbcUpathStatSignalPacketRowStatus,
       "hwBrasSbcOm": hwBrasSbcOm,
       "hwBrasSbcOmLeaves": hwBrasSbcOmLeaves,
       "hwBrasSbcRestartEnable": hwBrasSbcRestartEnable,
       "hwBrasSbcRestartButton": hwBrasSbcRestartButton,
       "hwBrasSbcPatchLoadStatus": hwBrasSbcPatchLoadStatus,
       "hwBrasSbcLocalizationStatus": hwBrasSbcLocalizationStatus,
       "hwBrasSbcOmTables": hwBrasSbcOmTables,
       "hwBrasSbcTrapBind": hwBrasSbcTrapBind,
       "hwBrasSbcTrapBindLeaves": hwBrasSbcTrapBindLeaves,
       "hwBrasSbcTrapBindTables": hwBrasSbcTrapBindTables,
       "hwBrasSbcTrapBindTable": hwBrasSbcTrapBindTable,
       "hwBrasSbcTrapBindEntry": hwBrasSbcTrapBindEntry,
       "hwBrasSbcTrapBindIndex": hwBrasSbcTrapBindIndex,
       "hwBrasSbcTrapBindID": hwBrasSbcTrapBindID,
       "hwBrasSbcTrapBindTime": hwBrasSbcTrapBindTime,
       "hwBrasSbcTrapBindFluID": hwBrasSbcTrapBindFluID,
       "hwBrasSbcTrapBindReason": hwBrasSbcTrapBindReason,
       "hwBrasSbcTrapBindType": hwBrasSbcTrapBindType,
       "hwBrasSbcTrapInfoTable": hwBrasSbcTrapInfoTable,
       "hwBrasSbcTrapInfoEntry": hwBrasSbcTrapInfoEntry,
       "hwBrasSbcTrapInfoIndex": hwBrasSbcTrapInfoIndex,
       "hwBrasSbcTrapInfoCpu": hwBrasSbcTrapInfoCpu,
       "hwBrasSbcTrapInfoHrp": hwBrasSbcTrapInfoHrp,
       "hwBrasSbcTrapInfoSignalingFlood": hwBrasSbcTrapInfoSignalingFlood,
       "hwBrasSbcTrapInfoCac": hwBrasSbcTrapInfoCac,
       "hwBrasSbcTrapInfoStatistic": hwBrasSbcTrapInfoStatistic,
       "hwBrasSbcTrapInfoPortStatistic": hwBrasSbcTrapInfoPortStatistic,
       "hwBrasSbcTrapInfoOldSSIP": hwBrasSbcTrapInfoOldSSIP,
       "hwBrasSbcTrapInfoImsConID": hwBrasSbcTrapInfoImsConID,
       "hwBrasSbcTrapInfoImsCcbID": hwBrasSbcTrapInfoImsCcbID,
       "hwBrasSbcComformance": hwBrasSbcComformance,
       "hwBrasSbcGroups": hwBrasSbcGroups,
       "hwBrasSbcGroup": hwBrasSbcGroup,
       "hwBrasSbcTrapGroup": hwBrasSbcTrapGroup,
       "hwBrasSbcCapabilities": hwBrasSbcCapabilities,
       "hwBrasSbcNotification": hwBrasSbcNotification,
       "hwBrasSbcCpu": hwBrasSbcCpu,
       "hwBrasSbcCpuNormal": hwBrasSbcCpuNormal,
       "hwBrasSbcHrp": hwBrasSbcHrp,
       "hwBrasSbcSignalingFlood": hwBrasSbcSignalingFlood,
       "hwBrasSbcSignalingFloodNormal": hwBrasSbcSignalingFloodNormal,
       "hwBrasSbcCac": hwBrasSbcCac,
       "hwBrasSbcCacNormal": hwBrasSbcCacNormal,
       "hwBrasSbcStatistic": hwBrasSbcStatistic,
       "hwBrasSbcPortStatistic": hwBrasSbcPortStatistic,
       "hwBrasSbcPortStatisticNormal": hwBrasSbcPortStatisticNormal,
       "hwBrasSbcDHSwitch": hwBrasSbcDHSwitch,
       "hwBrasSbcDHSwitchNormal": hwBrasSbcDHSwitchNormal,
       "hwBrasSbcImsRptFail": hwBrasSbcImsRptFail,
       "hwBrasSbcImsRptDrq": hwBrasSbcImsRptDrq,
       "hwBrasSbcImsTimeOut": hwBrasSbcImsTimeOut,
       "hwBrasSbcImsSessCreate": hwBrasSbcImsSessCreate,
       "hwBrasSbcImsSessDelete": hwBrasSbcImsSessDelete,
       "hwBrasSbcCopsLinkUp": hwBrasSbcCopsLinkUp,
       "hwBrasSbcCopsLinkDown": hwBrasSbcCopsLinkDown,
       "hwBrasSbcIaLinkUp": hwBrasSbcIaLinkUp,
       "hwBrasSbcIaLinkDown": hwBrasSbcIaLinkDown,
       "hwBrasSbcNotificationGroups": hwBrasSbcNotificationGroups,
       "hwBrasSbcNotificationGroup": hwBrasSbcNotificationGroup}
)
