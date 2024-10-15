# SNMP MIB module (A3COM-HUAWEI-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-EVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:56 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cEvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106)
)
h3cEvc.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEvcObjects_ObjectIdentity = ObjectIdentity
h3cEvcObjects = _H3cEvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1)
)
_H3cEvcScalarGroup_ObjectIdentity = ObjectIdentity
h3cEvcScalarGroup = _H3cEvcScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 1)
)


class _H3cEvcSrvInstEncapCapabilities_Type(Bits):
    """Custom type h3cEvcSrvInstEncapCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("encapPortBased", 0),
          ("encapSvlanId", 3),
          ("encapSvlanIdList", 4),
          ("encapSvlanIdOnlyTagged", 5),
          ("encapTagged", 2),
          ("encapUntagged", 1))
    )

_H3cEvcSrvInstEncapCapabilities_Type.__name__ = "Bits"
_H3cEvcSrvInstEncapCapabilities_Object = MibScalar
h3cEvcSrvInstEncapCapabilities = _H3cEvcSrvInstEncapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 1, 1),
    _H3cEvcSrvInstEncapCapabilities_Type()
)
h3cEvcSrvInstEncapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcSrvInstEncapCapabilities.setStatus("current")
_H3cEvcPortMaxSrvInstNum_Type = Integer32
_H3cEvcPortMaxSrvInstNum_Object = MibScalar
h3cEvcPortMaxSrvInstNum = _H3cEvcPortMaxSrvInstNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 1, 2),
    _H3cEvcPortMaxSrvInstNum_Type()
)
h3cEvcPortMaxSrvInstNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcPortMaxSrvInstNum.setStatus("current")
_H3cEvcSrvInstTable_Object = MibTable
h3cEvcSrvInstTable = _H3cEvcSrvInstTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2)
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstTable.setStatus("current")
_H3cEvcSrvInstEntry_Object = MibTableRow
h3cEvcSrvInstEntry = _H3cEvcSrvInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1)
)
h3cEvcSrvInstEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EVC-MIB", "h3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstEntry.setStatus("current")


class _H3cEvcSrvInstId_Type(Integer32):
    """Custom type h3cEvcSrvInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cEvcSrvInstId_Type.__name__ = "Integer32"
_H3cEvcSrvInstId_Object = MibTableColumn
h3cEvcSrvInstId = _H3cEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 1),
    _H3cEvcSrvInstId_Type()
)
h3cEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvcSrvInstId.setStatus("current")


class _H3cEvcSrvInstEncap_Type(Integer32):
    """Custom type h3cEvcSrvInstEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("portBased", 1),
          ("svlanIdList", 4),
          ("svlanIdListOnlyTagged", 5),
          ("tagged", 3),
          ("untagged", 2))
    )


_H3cEvcSrvInstEncap_Type.__name__ = "Integer32"
_H3cEvcSrvInstEncap_Object = MibTableColumn
h3cEvcSrvInstEncap = _H3cEvcSrvInstEncap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 2),
    _H3cEvcSrvInstEncap_Type()
)
h3cEvcSrvInstEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstEncap.setStatus("current")


class _H3cEvcSrvInstSvlanIdListLow_Type(OctetString):
    """Custom type h3cEvcSrvInstSvlanIdListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cEvcSrvInstSvlanIdListLow_Type.__name__ = "OctetString"
_H3cEvcSrvInstSvlanIdListLow_Object = MibTableColumn
h3cEvcSrvInstSvlanIdListLow = _H3cEvcSrvInstSvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 3),
    _H3cEvcSrvInstSvlanIdListLow_Type()
)
h3cEvcSrvInstSvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstSvlanIdListLow.setStatus("current")


class _H3cEvcSrvInstSvlanIdListHigh_Type(OctetString):
    """Custom type h3cEvcSrvInstSvlanIdListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cEvcSrvInstSvlanIdListHigh_Type.__name__ = "OctetString"
_H3cEvcSrvInstSvlanIdListHigh_Object = MibTableColumn
h3cEvcSrvInstSvlanIdListHigh = _H3cEvcSrvInstSvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 4),
    _H3cEvcSrvInstSvlanIdListHigh_Type()
)
h3cEvcSrvInstSvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstSvlanIdListHigh.setStatus("current")
_H3cEvcSrvInstRowStatus_Type = RowStatus
_H3cEvcSrvInstRowStatus_Object = MibTableColumn
h3cEvcSrvInstRowStatus = _H3cEvcSrvInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 5),
    _H3cEvcSrvInstRowStatus_Type()
)
h3cEvcSrvInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstRowStatus.setStatus("current")


class _H3cEvcSrvInstEnableInStat_Type(TruthValue):
    """Custom type h3cEvcSrvInstEnableInStat based on TruthValue"""


_H3cEvcSrvInstEnableInStat_Object = MibTableColumn
h3cEvcSrvInstEnableInStat = _H3cEvcSrvInstEnableInStat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 6),
    _H3cEvcSrvInstEnableInStat_Type()
)
h3cEvcSrvInstEnableInStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstEnableInStat.setStatus("current")


class _H3cEvcSrvInstEnableOutStat_Type(TruthValue):
    """Custom type h3cEvcSrvInstEnableOutStat based on TruthValue"""


_H3cEvcSrvInstEnableOutStat_Object = MibTableColumn
h3cEvcSrvInstEnableOutStat = _H3cEvcSrvInstEnableOutStat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 2, 1, 7),
    _H3cEvcSrvInstEnableOutStat_Type()
)
h3cEvcSrvInstEnableOutStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstEnableOutStat.setStatus("current")
_H3cEvcSrvInstCarTable_Object = MibTable
h3cEvcSrvInstCarTable = _H3cEvcSrvInstCarTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3)
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstCarTable.setStatus("current")
_H3cEvcSrvInstCarEntry_Object = MibTableRow
h3cEvcSrvInstCarEntry = _H3cEvcSrvInstCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3, 1)
)
h3cEvcSrvInstCarEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EVC-MIB", "h3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstCarEntry.setStatus("current")
_H3cEvcSrvInstInCarIndex_Type = Integer32
_H3cEvcSrvInstInCarIndex_Object = MibTableColumn
h3cEvcSrvInstInCarIndex = _H3cEvcSrvInstInCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3, 1, 1),
    _H3cEvcSrvInstInCarIndex_Type()
)
h3cEvcSrvInstInCarIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvcSrvInstInCarIndex.setStatus("current")
_H3cEvcSrvInstOutCarIndex_Type = Integer32
_H3cEvcSrvInstOutCarIndex_Object = MibTableColumn
h3cEvcSrvInstOutCarIndex = _H3cEvcSrvInstOutCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 3, 1, 2),
    _H3cEvcSrvInstOutCarIndex_Type()
)
h3cEvcSrvInstOutCarIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvcSrvInstOutCarIndex.setStatus("current")
_H3cEvcSrvInstStatInfoTable_Object = MibTable
h3cEvcSrvInstStatInfoTable = _H3cEvcSrvInstStatInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4)
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstStatInfoTable.setStatus("current")
_H3cEvcSrvInstStatInfoEntry_Object = MibTableRow
h3cEvcSrvInstStatInfoEntry = _H3cEvcSrvInstStatInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1)
)
h3cEvcSrvInstStatInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EVC-MIB", "h3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstStatInfoEntry.setStatus("current")
_H3cEvcSrvInstInPackets_Type = Counter64
_H3cEvcSrvInstInPackets_Object = MibTableColumn
h3cEvcSrvInstInPackets = _H3cEvcSrvInstInPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 1),
    _H3cEvcSrvInstInPackets_Type()
)
h3cEvcSrvInstInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcSrvInstInPackets.setStatus("current")
if mibBuilder.loadTexts:
    h3cEvcSrvInstInPackets.setUnits("packets")
_H3cEvcSrvInstInBytes_Type = Counter64
_H3cEvcSrvInstInBytes_Object = MibTableColumn
h3cEvcSrvInstInBytes = _H3cEvcSrvInstInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 2),
    _H3cEvcSrvInstInBytes_Type()
)
h3cEvcSrvInstInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcSrvInstInBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cEvcSrvInstInBytes.setUnits("bytes")
_H3cEvcSrvInstOutPackets_Type = Counter64
_H3cEvcSrvInstOutPackets_Object = MibTableColumn
h3cEvcSrvInstOutPackets = _H3cEvcSrvInstOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 3),
    _H3cEvcSrvInstOutPackets_Type()
)
h3cEvcSrvInstOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcSrvInstOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    h3cEvcSrvInstOutPackets.setUnits("packets")
_H3cEvcSrvInstOutBytes_Type = Counter64
_H3cEvcSrvInstOutBytes_Object = MibTableColumn
h3cEvcSrvInstOutBytes = _H3cEvcSrvInstOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 106, 1, 4, 1, 4),
    _H3cEvcSrvInstOutBytes_Type()
)
h3cEvcSrvInstOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcSrvInstOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cEvcSrvInstOutBytes.setUnits("bytes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-EVC-MIB",
    **{"h3cEvc": h3cEvc,
       "h3cEvcObjects": h3cEvcObjects,
       "h3cEvcScalarGroup": h3cEvcScalarGroup,
       "h3cEvcSrvInstEncapCapabilities": h3cEvcSrvInstEncapCapabilities,
       "h3cEvcPortMaxSrvInstNum": h3cEvcPortMaxSrvInstNum,
       "h3cEvcSrvInstTable": h3cEvcSrvInstTable,
       "h3cEvcSrvInstEntry": h3cEvcSrvInstEntry,
       "h3cEvcSrvInstId": h3cEvcSrvInstId,
       "h3cEvcSrvInstEncap": h3cEvcSrvInstEncap,
       "h3cEvcSrvInstSvlanIdListLow": h3cEvcSrvInstSvlanIdListLow,
       "h3cEvcSrvInstSvlanIdListHigh": h3cEvcSrvInstSvlanIdListHigh,
       "h3cEvcSrvInstRowStatus": h3cEvcSrvInstRowStatus,
       "h3cEvcSrvInstEnableInStat": h3cEvcSrvInstEnableInStat,
       "h3cEvcSrvInstEnableOutStat": h3cEvcSrvInstEnableOutStat,
       "h3cEvcSrvInstCarTable": h3cEvcSrvInstCarTable,
       "h3cEvcSrvInstCarEntry": h3cEvcSrvInstCarEntry,
       "h3cEvcSrvInstInCarIndex": h3cEvcSrvInstInCarIndex,
       "h3cEvcSrvInstOutCarIndex": h3cEvcSrvInstOutCarIndex,
       "h3cEvcSrvInstStatInfoTable": h3cEvcSrvInstStatInfoTable,
       "h3cEvcSrvInstStatInfoEntry": h3cEvcSrvInstStatInfoEntry,
       "h3cEvcSrvInstInPackets": h3cEvcSrvInstInPackets,
       "h3cEvcSrvInstInBytes": h3cEvcSrvInstInBytes,
       "h3cEvcSrvInstOutPackets": h3cEvcSrvInstOutPackets,
       "h3cEvcSrvInstOutBytes": h3cEvcSrvInstOutBytes}
)
