# SNMP MIB module (HPN-ICF-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:12 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfEvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106)
)
hpnicfEvc.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEvcObjects_ObjectIdentity = ObjectIdentity
hpnicfEvcObjects = _HpnicfEvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1)
)
_HpnicfEvcScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfEvcScalarGroup = _HpnicfEvcScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 1)
)


class _HpnicfEvcSrvInstEncapCapabilities_Type(Bits):
    """Custom type hpnicfEvcSrvInstEncapCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("encapCvlanId", 8),
          ("encapCvlanIdList", 9),
          ("encapDefault", 0),
          ("encapSvlanId", 3),
          ("encapSvlanIdCvlanId", 6),
          ("encapSvlanIdCvlanIdList", 7),
          ("encapSvlanIdList", 4),
          ("encapSvlanIdOnlyTagged", 5),
          ("encapTagged", 2),
          ("encapUntagged", 1))
    )

_HpnicfEvcSrvInstEncapCapabilities_Type.__name__ = "Bits"
_HpnicfEvcSrvInstEncapCapabilities_Object = MibScalar
hpnicfEvcSrvInstEncapCapabilities = _HpnicfEvcSrvInstEncapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 1, 1),
    _HpnicfEvcSrvInstEncapCapabilities_Type()
)
hpnicfEvcSrvInstEncapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstEncapCapabilities.setStatus("current")
_HpnicfEvcPortMaxSrvInstNum_Type = Integer32
_HpnicfEvcPortMaxSrvInstNum_Object = MibScalar
hpnicfEvcPortMaxSrvInstNum = _HpnicfEvcPortMaxSrvInstNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 1, 2),
    _HpnicfEvcPortMaxSrvInstNum_Type()
)
hpnicfEvcPortMaxSrvInstNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvcPortMaxSrvInstNum.setStatus("current")
_HpnicfEvcSrvInstTable_Object = MibTable
hpnicfEvcSrvInstTable = _HpnicfEvcSrvInstTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstTable.setStatus("current")
_HpnicfEvcSrvInstEntry_Object = MibTableRow
hpnicfEvcSrvInstEntry = _HpnicfEvcSrvInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1)
)
hpnicfEvcSrvInstEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVC-MIB", "hpnicfEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstEntry.setStatus("current")


class _HpnicfEvcSrvInstId_Type(Integer32):
    """Custom type hpnicfEvcSrvInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfEvcSrvInstId_Type.__name__ = "Integer32"
_HpnicfEvcSrvInstId_Object = MibTableColumn
hpnicfEvcSrvInstId = _HpnicfEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 1),
    _HpnicfEvcSrvInstId_Type()
)
hpnicfEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstId.setStatus("current")


class _HpnicfEvcSrvInstEncap_Type(Integer32):
    """Custom type hpnicfEvcSrvInstEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cvlanIdList", 9),
          ("default", 1),
          ("none", 0),
          ("svlanIdCvlanId", 6),
          ("svlanIdCvlanIdAll", 8),
          ("svlanIdCvlanIdList", 7),
          ("svlanIdList", 4),
          ("svlanIdListOnlyTagged", 5),
          ("tagged", 3),
          ("untagged", 2))
    )


_HpnicfEvcSrvInstEncap_Type.__name__ = "Integer32"
_HpnicfEvcSrvInstEncap_Object = MibTableColumn
hpnicfEvcSrvInstEncap = _HpnicfEvcSrvInstEncap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 2),
    _HpnicfEvcSrvInstEncap_Type()
)
hpnicfEvcSrvInstEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstEncap.setStatus("current")


class _HpnicfEvcSrvInstSvlanIdListLow_Type(OctetString):
    """Custom type hpnicfEvcSrvInstSvlanIdListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfEvcSrvInstSvlanIdListLow_Type.__name__ = "OctetString"
_HpnicfEvcSrvInstSvlanIdListLow_Object = MibTableColumn
hpnicfEvcSrvInstSvlanIdListLow = _HpnicfEvcSrvInstSvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 3),
    _HpnicfEvcSrvInstSvlanIdListLow_Type()
)
hpnicfEvcSrvInstSvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstSvlanIdListLow.setStatus("current")


class _HpnicfEvcSrvInstSvlanIdListHigh_Type(OctetString):
    """Custom type hpnicfEvcSrvInstSvlanIdListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfEvcSrvInstSvlanIdListHigh_Type.__name__ = "OctetString"
_HpnicfEvcSrvInstSvlanIdListHigh_Object = MibTableColumn
hpnicfEvcSrvInstSvlanIdListHigh = _HpnicfEvcSrvInstSvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 4),
    _HpnicfEvcSrvInstSvlanIdListHigh_Type()
)
hpnicfEvcSrvInstSvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstSvlanIdListHigh.setStatus("current")
_HpnicfEvcSrvInstRowStatus_Type = RowStatus
_HpnicfEvcSrvInstRowStatus_Object = MibTableColumn
hpnicfEvcSrvInstRowStatus = _HpnicfEvcSrvInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 5),
    _HpnicfEvcSrvInstRowStatus_Type()
)
hpnicfEvcSrvInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstRowStatus.setStatus("current")


class _HpnicfEvcSrvInstEnableInStat_Type(TruthValue):
    """Custom type hpnicfEvcSrvInstEnableInStat based on TruthValue"""


_HpnicfEvcSrvInstEnableInStat_Object = MibTableColumn
hpnicfEvcSrvInstEnableInStat = _HpnicfEvcSrvInstEnableInStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 6),
    _HpnicfEvcSrvInstEnableInStat_Type()
)
hpnicfEvcSrvInstEnableInStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstEnableInStat.setStatus("current")


class _HpnicfEvcSrvInstEnableOutStat_Type(TruthValue):
    """Custom type hpnicfEvcSrvInstEnableOutStat based on TruthValue"""


_HpnicfEvcSrvInstEnableOutStat_Object = MibTableColumn
hpnicfEvcSrvInstEnableOutStat = _HpnicfEvcSrvInstEnableOutStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 7),
    _HpnicfEvcSrvInstEnableOutStat_Type()
)
hpnicfEvcSrvInstEnableOutStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstEnableOutStat.setStatus("current")


class _HpnicfEvcSrvInstCvlanIdListLow_Type(OctetString):
    """Custom type hpnicfEvcSrvInstCvlanIdListLow based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfEvcSrvInstCvlanIdListLow_Type.__name__ = "OctetString"
_HpnicfEvcSrvInstCvlanIdListLow_Object = MibTableColumn
hpnicfEvcSrvInstCvlanIdListLow = _HpnicfEvcSrvInstCvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 8),
    _HpnicfEvcSrvInstCvlanIdListLow_Type()
)
hpnicfEvcSrvInstCvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstCvlanIdListLow.setStatus("current")


class _HpnicfEvcSrvInstCvlanIdListHigh_Type(OctetString):
    """Custom type hpnicfEvcSrvInstCvlanIdListHigh based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfEvcSrvInstCvlanIdListHigh_Type.__name__ = "OctetString"
_HpnicfEvcSrvInstCvlanIdListHigh_Object = MibTableColumn
hpnicfEvcSrvInstCvlanIdListHigh = _HpnicfEvcSrvInstCvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 2, 1, 9),
    _HpnicfEvcSrvInstCvlanIdListHigh_Type()
)
hpnicfEvcSrvInstCvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstCvlanIdListHigh.setStatus("current")
_HpnicfEvcSrvInstCarTable_Object = MibTable
hpnicfEvcSrvInstCarTable = _HpnicfEvcSrvInstCarTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstCarTable.setStatus("current")
_HpnicfEvcSrvInstCarEntry_Object = MibTableRow
hpnicfEvcSrvInstCarEntry = _HpnicfEvcSrvInstCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 3, 1)
)
hpnicfEvcSrvInstCarEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVC-MIB", "hpnicfEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstCarEntry.setStatus("current")
_HpnicfEvcSrvInstInCarIndex_Type = Integer32
_HpnicfEvcSrvInstInCarIndex_Object = MibTableColumn
hpnicfEvcSrvInstInCarIndex = _HpnicfEvcSrvInstInCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 3, 1, 1),
    _HpnicfEvcSrvInstInCarIndex_Type()
)
hpnicfEvcSrvInstInCarIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstInCarIndex.setStatus("current")
_HpnicfEvcSrvInstOutCarIndex_Type = Integer32
_HpnicfEvcSrvInstOutCarIndex_Object = MibTableColumn
hpnicfEvcSrvInstOutCarIndex = _HpnicfEvcSrvInstOutCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 3, 1, 2),
    _HpnicfEvcSrvInstOutCarIndex_Type()
)
hpnicfEvcSrvInstOutCarIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstOutCarIndex.setStatus("current")
_HpnicfEvcSrvInstStatInfoTable_Object = MibTable
hpnicfEvcSrvInstStatInfoTable = _HpnicfEvcSrvInstStatInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstStatInfoTable.setStatus("current")
_HpnicfEvcSrvInstStatInfoEntry_Object = MibTableRow
hpnicfEvcSrvInstStatInfoEntry = _HpnicfEvcSrvInstStatInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 4, 1)
)
hpnicfEvcSrvInstStatInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVC-MIB", "hpnicfEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstStatInfoEntry.setStatus("current")
_HpnicfEvcSrvInstInPackets_Type = Counter64
_HpnicfEvcSrvInstInPackets_Object = MibTableColumn
hpnicfEvcSrvInstInPackets = _HpnicfEvcSrvInstInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 4, 1, 1),
    _HpnicfEvcSrvInstInPackets_Type()
)
hpnicfEvcSrvInstInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstInPackets.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstInPackets.setUnits("packets")
_HpnicfEvcSrvInstInBytes_Type = Counter64
_HpnicfEvcSrvInstInBytes_Object = MibTableColumn
hpnicfEvcSrvInstInBytes = _HpnicfEvcSrvInstInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 4, 1, 2),
    _HpnicfEvcSrvInstInBytes_Type()
)
hpnicfEvcSrvInstInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstInBytes.setUnits("bytes")
_HpnicfEvcSrvInstOutPackets_Type = Counter64
_HpnicfEvcSrvInstOutPackets_Object = MibTableColumn
hpnicfEvcSrvInstOutPackets = _HpnicfEvcSrvInstOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 4, 1, 3),
    _HpnicfEvcSrvInstOutPackets_Type()
)
hpnicfEvcSrvInstOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstOutPackets.setUnits("packets")
_HpnicfEvcSrvInstOutBytes_Type = Counter64
_HpnicfEvcSrvInstOutBytes_Object = MibTableColumn
hpnicfEvcSrvInstOutBytes = _HpnicfEvcSrvInstOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106, 1, 4, 1, 4),
    _HpnicfEvcSrvInstOutBytes_Type()
)
hpnicfEvcSrvInstOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEvcSrvInstOutBytes.setUnits("bytes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EVC-MIB",
    **{"hpnicfEvc": hpnicfEvc,
       "hpnicfEvcObjects": hpnicfEvcObjects,
       "hpnicfEvcScalarGroup": hpnicfEvcScalarGroup,
       "hpnicfEvcSrvInstEncapCapabilities": hpnicfEvcSrvInstEncapCapabilities,
       "hpnicfEvcPortMaxSrvInstNum": hpnicfEvcPortMaxSrvInstNum,
       "hpnicfEvcSrvInstTable": hpnicfEvcSrvInstTable,
       "hpnicfEvcSrvInstEntry": hpnicfEvcSrvInstEntry,
       "hpnicfEvcSrvInstId": hpnicfEvcSrvInstId,
       "hpnicfEvcSrvInstEncap": hpnicfEvcSrvInstEncap,
       "hpnicfEvcSrvInstSvlanIdListLow": hpnicfEvcSrvInstSvlanIdListLow,
       "hpnicfEvcSrvInstSvlanIdListHigh": hpnicfEvcSrvInstSvlanIdListHigh,
       "hpnicfEvcSrvInstRowStatus": hpnicfEvcSrvInstRowStatus,
       "hpnicfEvcSrvInstEnableInStat": hpnicfEvcSrvInstEnableInStat,
       "hpnicfEvcSrvInstEnableOutStat": hpnicfEvcSrvInstEnableOutStat,
       "hpnicfEvcSrvInstCvlanIdListLow": hpnicfEvcSrvInstCvlanIdListLow,
       "hpnicfEvcSrvInstCvlanIdListHigh": hpnicfEvcSrvInstCvlanIdListHigh,
       "hpnicfEvcSrvInstCarTable": hpnicfEvcSrvInstCarTable,
       "hpnicfEvcSrvInstCarEntry": hpnicfEvcSrvInstCarEntry,
       "hpnicfEvcSrvInstInCarIndex": hpnicfEvcSrvInstInCarIndex,
       "hpnicfEvcSrvInstOutCarIndex": hpnicfEvcSrvInstOutCarIndex,
       "hpnicfEvcSrvInstStatInfoTable": hpnicfEvcSrvInstStatInfoTable,
       "hpnicfEvcSrvInstStatInfoEntry": hpnicfEvcSrvInstStatInfoEntry,
       "hpnicfEvcSrvInstInPackets": hpnicfEvcSrvInstInPackets,
       "hpnicfEvcSrvInstInBytes": hpnicfEvcSrvInstInBytes,
       "hpnicfEvcSrvInstOutPackets": hpnicfEvcSrvInstOutPackets,
       "hpnicfEvcSrvInstOutBytes": hpnicfEvcSrvInstOutBytes}
)
