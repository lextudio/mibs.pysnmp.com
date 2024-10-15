# SNMP MIB module (WWP-MAC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-MAC-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:16 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpMacMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28)
)
wwpMacMgmtMIB.setRevisions(
        ("2005-11-22 19:00",
         "2003-04-16 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpMacMgmtMIBObjects_ObjectIdentity = ObjectIdentity
wwpMacMgmtMIBObjects = _WwpMacMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1)
)
_WwpMacMgmt_ObjectIdentity = ObjectIdentity
wwpMacMgmt = _WwpMacMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1)
)
_WwpMacMgmtMacTable_Object = MibTable
wwpMacMgmtMacTable = _WwpMacMgmtMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpMacMgmtMacTable.setStatus("current")
_WwpMacMgmtMacEntry_Object = MibTableRow
wwpMacMgmtMacEntry = _WwpMacMgmtMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1)
)
wwpMacMgmtMacEntry.setIndexNames(
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtVlanID"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtPortId"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtMacAddr"),
)
if mibBuilder.loadTexts:
    wwpMacMgmtMacEntry.setStatus("current")
_WwpMacMgmtVlanID_Type = VlanId
_WwpMacMgmtVlanID_Object = MibTableColumn
wwpMacMgmtVlanID = _WwpMacMgmtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 1),
    _WwpMacMgmtVlanID_Type()
)
wwpMacMgmtVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtVlanID.setStatus("current")


class _WwpMacMgmtPortId_Type(Integer32):
    """Custom type wwpMacMgmtPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpMacMgmtPortId_Type.__name__ = "Integer32"
_WwpMacMgmtPortId_Object = MibTableColumn
wwpMacMgmtPortId = _WwpMacMgmtPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 2),
    _WwpMacMgmtPortId_Type()
)
wwpMacMgmtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtPortId.setStatus("current")
_WwpMacMgmtMacAddr_Type = MacAddress
_WwpMacMgmtMacAddr_Object = MibTableColumn
wwpMacMgmtMacAddr = _WwpMacMgmtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 3),
    _WwpMacMgmtMacAddr_Type()
)
wwpMacMgmtMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtMacAddr.setStatus("current")


class _WwpMacMgmtMacAddrMode_Type(Integer32):
    """Custom type wwpMacMgmtMacAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_WwpMacMgmtMacAddrMode_Type.__name__ = "Integer32"
_WwpMacMgmtMacAddrMode_Object = MibTableColumn
wwpMacMgmtMacAddrMode = _WwpMacMgmtMacAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 4),
    _WwpMacMgmtMacAddrMode_Type()
)
wwpMacMgmtMacAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMacMgmtMacAddrMode.setStatus("current")


class _WwpMacMgmtMacStatus_Type(Integer32):
    """Custom type wwpMacMgmtMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpMacMgmtMacStatus_Type.__name__ = "Integer32"
_WwpMacMgmtMacStatus_Object = MibTableColumn
wwpMacMgmtMacStatus = _WwpMacMgmtMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 5),
    _WwpMacMgmtMacStatus_Type()
)
wwpMacMgmtMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtMacStatus.setStatus("current")
_WwpMacMgmtMacRowStatus_Type = RowStatus
_WwpMacMgmtMacRowStatus_Object = MibTableColumn
wwpMacMgmtMacRowStatus = _WwpMacMgmtMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 6),
    _WwpMacMgmtMacRowStatus_Type()
)
wwpMacMgmtMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpMacMgmtMacRowStatus.setStatus("current")


class _WwpMacMgmtMacReset_Type(Integer32):
    """Custom type wwpMacMgmtMacReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_WwpMacMgmtMacReset_Type.__name__ = "Integer32"
_WwpMacMgmtMacReset_Object = MibScalar
wwpMacMgmtMacReset = _WwpMacMgmtMacReset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 2),
    _WwpMacMgmtMacReset_Type()
)
wwpMacMgmtMacReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMacMgmtMacReset.setStatus("current")
_WwpMacMgmtPMTable_Object = MibTable
wwpMacMgmtPMTable = _WwpMacMgmtPMTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpMacMgmtPMTable.setStatus("current")
_WwpMacMgmtPMEntry_Object = MibTableRow
wwpMacMgmtPMEntry = _WwpMacMgmtPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1)
)
wwpMacMgmtPMEntry.setIndexNames(
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtPMVlanID"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtPMPortId"),
)
if mibBuilder.loadTexts:
    wwpMacMgmtPMEntry.setStatus("current")
_WwpMacMgmtPMVlanID_Type = VlanId
_WwpMacMgmtPMVlanID_Object = MibTableColumn
wwpMacMgmtPMVlanID = _WwpMacMgmtPMVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 1),
    _WwpMacMgmtPMVlanID_Type()
)
wwpMacMgmtPMVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtPMVlanID.setStatus("current")


class _WwpMacMgmtPMPortId_Type(Integer32):
    """Custom type wwpMacMgmtPMPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpMacMgmtPMPortId_Type.__name__ = "Integer32"
_WwpMacMgmtPMPortId_Object = MibTableColumn
wwpMacMgmtPMPortId = _WwpMacMgmtPMPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 2),
    _WwpMacMgmtPMPortId_Type()
)
wwpMacMgmtPMPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtPMPortId.setStatus("current")


class _WwpMacMgmtPMLearnLimit_Type(Integer32):
    """Custom type wwpMacMgmtPMLearnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_WwpMacMgmtPMLearnLimit_Type.__name__ = "Integer32"
_WwpMacMgmtPMLearnLimit_Object = MibTableColumn
wwpMacMgmtPMLearnLimit = _WwpMacMgmtPMLearnLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 3),
    _WwpMacMgmtPMLearnLimit_Type()
)
wwpMacMgmtPMLearnLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMacMgmtPMLearnLimit.setStatus("current")


class _WwpMacMgmtPMLearnCount_Type(Integer32):
    """Custom type wwpMacMgmtPMLearnCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_WwpMacMgmtPMLearnCount_Type.__name__ = "Integer32"
_WwpMacMgmtPMLearnCount_Object = MibTableColumn
wwpMacMgmtPMLearnCount = _WwpMacMgmtPMLearnCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 4),
    _WwpMacMgmtPMLearnCount_Type()
)
wwpMacMgmtPMLearnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtPMLearnCount.setStatus("current")


class _WwpMacMgmtPMStatus_Type(Integer32):
    """Custom type wwpMacMgmtPMStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpMacMgmtPMStatus_Type.__name__ = "Integer32"
_WwpMacMgmtPMStatus_Object = MibTableColumn
wwpMacMgmtPMStatus = _WwpMacMgmtPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 5),
    _WwpMacMgmtPMStatus_Type()
)
wwpMacMgmtPMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMacMgmtPMStatus.setStatus("current")


class _WwpMacMgmtPMMacFlush_Type(Integer32):
    """Custom type wwpMacMgmtPMMacFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flush", 1),
          ("none", 0))
    )


_WwpMacMgmtPMMacFlush_Type.__name__ = "Integer32"
_WwpMacMgmtPMMacFlush_Object = MibTableColumn
wwpMacMgmtPMMacFlush = _WwpMacMgmtPMMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 6),
    _WwpMacMgmtPMMacFlush_Type()
)
wwpMacMgmtPMMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMacMgmtPMMacFlush.setStatus("current")


class _WwpMacMgmtCacheMac_Type(TruthValue):
    """Custom type wwpMacMgmtCacheMac based on TruthValue"""


_WwpMacMgmtCacheMac_Object = MibScalar
wwpMacMgmtCacheMac = _WwpMacMgmtCacheMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 4),
    _WwpMacMgmtCacheMac_Type()
)
wwpMacMgmtCacheMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMacMgmtCacheMac.setStatus("current")
_WwpMacMgmtCacheMacTable_Object = MibTable
wwpMacMgmtCacheMacTable = _WwpMacMgmtCacheMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpMacMgmtCacheMacTable.setStatus("current")
_WwpMacMgmtCacheMacEntry_Object = MibTableRow
wwpMacMgmtCacheMacEntry = _WwpMacMgmtCacheMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1)
)
wwpMacMgmtCacheMacEntry.setIndexNames(
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCVlanID"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCPortId"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCMacIndex"),
)
if mibBuilder.loadTexts:
    wwpMacMgmtCacheMacEntry.setStatus("current")
_WwpMacMgmtCVlanID_Type = VlanId
_WwpMacMgmtCVlanID_Object = MibTableColumn
wwpMacMgmtCVlanID = _WwpMacMgmtCVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 1),
    _WwpMacMgmtCVlanID_Type()
)
wwpMacMgmtCVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCVlanID.setStatus("current")


class _WwpMacMgmtCPortId_Type(Integer32):
    """Custom type wwpMacMgmtCPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpMacMgmtCPortId_Type.__name__ = "Integer32"
_WwpMacMgmtCPortId_Object = MibTableColumn
wwpMacMgmtCPortId = _WwpMacMgmtCPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 2),
    _WwpMacMgmtCPortId_Type()
)
wwpMacMgmtCPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCPortId.setStatus("current")


class _WwpMacMgmtCMacIndex_Type(Integer32):
    """Custom type wwpMacMgmtCMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpMacMgmtCMacIndex_Type.__name__ = "Integer32"
_WwpMacMgmtCMacIndex_Object = MibTableColumn
wwpMacMgmtCMacIndex = _WwpMacMgmtCMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 3),
    _WwpMacMgmtCMacIndex_Type()
)
wwpMacMgmtCMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCMacIndex.setStatus("current")
_WwpMacMgmtCMacAddr_Type = MacAddress
_WwpMacMgmtCMacAddr_Object = MibTableColumn
wwpMacMgmtCMacAddr = _WwpMacMgmtCMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 4),
    _WwpMacMgmtCMacAddr_Type()
)
wwpMacMgmtCMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCMacAddr.setStatus("current")


class _WwpMacMgmtCMacAddrMode_Type(Integer32):
    """Custom type wwpMacMgmtCMacAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_WwpMacMgmtCMacAddrMode_Type.__name__ = "Integer32"
_WwpMacMgmtCMacAddrMode_Object = MibTableColumn
wwpMacMgmtCMacAddrMode = _WwpMacMgmtCMacAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 5),
    _WwpMacMgmtCMacAddrMode_Type()
)
wwpMacMgmtCMacAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCMacAddrMode.setStatus("current")


class _WwpMacMgmtCMacStatus_Type(Integer32):
    """Custom type wwpMacMgmtCMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpMacMgmtCMacStatus_Type.__name__ = "Integer32"
_WwpMacMgmtCMacStatus_Object = MibTableColumn
wwpMacMgmtCMacStatus = _WwpMacMgmtCMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 6),
    _WwpMacMgmtCMacStatus_Type()
)
wwpMacMgmtCMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCMacStatus.setStatus("current")
_WwpMacMgmtCacheMacCountTable_Object = MibTable
wwpMacMgmtCacheMacCountTable = _WwpMacMgmtCacheMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpMacMgmtCacheMacCountTable.setStatus("current")
_WwpMacMgmtCacheMacCountEntry_Object = MibTableRow
wwpMacMgmtCacheMacCountEntry = _WwpMacMgmtCacheMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 6, 1)
)
wwpMacMgmtCacheMacCountEntry.setIndexNames(
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCVlanID"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCPortId"),
)
if mibBuilder.loadTexts:
    wwpMacMgmtCacheMacCountEntry.setStatus("current")


class _WwpMacMgmtCacheMacCount_Type(Integer32):
    """Custom type wwpMacMgmtCacheMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpMacMgmtCacheMacCount_Type.__name__ = "Integer32"
_WwpMacMgmtCacheMacCount_Object = MibTableColumn
wwpMacMgmtCacheMacCount = _WwpMacMgmtCacheMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 6, 1, 1),
    _WwpMacMgmtCacheMacCount_Type()
)
wwpMacMgmtCacheMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtCacheMacCount.setStatus("current")
_WwpMacMgmtSacTable_Object = MibTable
wwpMacMgmtSacTable = _WwpMacMgmtSacTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpMacMgmtSacTable.setStatus("current")
_WwpMacMgmtSacEntry_Object = MibTableRow
wwpMacMgmtSacEntry = _WwpMacMgmtSacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1)
)
wwpMacMgmtSacEntry.setIndexNames(
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtSacVlanID"),
    (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtSacPortId"),
)
if mibBuilder.loadTexts:
    wwpMacMgmtSacEntry.setStatus("current")
_WwpMacMgmtSacVlanID_Type = VlanId
_WwpMacMgmtSacVlanID_Object = MibTableColumn
wwpMacMgmtSacVlanID = _WwpMacMgmtSacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 1),
    _WwpMacMgmtSacVlanID_Type()
)
wwpMacMgmtSacVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtSacVlanID.setStatus("current")


class _WwpMacMgmtSacPortId_Type(Integer32):
    """Custom type wwpMacMgmtSacPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpMacMgmtSacPortId_Type.__name__ = "Integer32"
_WwpMacMgmtSacPortId_Object = MibTableColumn
wwpMacMgmtSacPortId = _WwpMacMgmtSacPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 2),
    _WwpMacMgmtSacPortId_Type()
)
wwpMacMgmtSacPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtSacPortId.setStatus("current")


class _WwpMacMgmtSacLearnCount_Type(Integer32):
    """Custom type wwpMacMgmtSacLearnCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WwpMacMgmtSacLearnCount_Type.__name__ = "Integer32"
_WwpMacMgmtSacLearnCount_Object = MibTableColumn
wwpMacMgmtSacLearnCount = _WwpMacMgmtSacLearnCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 3),
    _WwpMacMgmtSacLearnCount_Type()
)
wwpMacMgmtSacLearnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMacMgmtSacLearnCount.setStatus("current")


class _WwpMacMgmtSacMaxLearn_Type(Integer32):
    """Custom type wwpMacMgmtSacMaxLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WwpMacMgmtSacMaxLearn_Type.__name__ = "Integer32"
_WwpMacMgmtSacMaxLearn_Object = MibTableColumn
wwpMacMgmtSacMaxLearn = _WwpMacMgmtSacMaxLearn_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 4),
    _WwpMacMgmtSacMaxLearn_Type()
)
wwpMacMgmtSacMaxLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpMacMgmtSacMaxLearn.setStatus("current")


class _WwpMacMgmtSacLearnDisabled_Type(TruthValue):
    """Custom type wwpMacMgmtSacLearnDisabled based on TruthValue"""


_WwpMacMgmtSacLearnDisabled_Object = MibTableColumn
wwpMacMgmtSacLearnDisabled = _WwpMacMgmtSacLearnDisabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 5),
    _WwpMacMgmtSacLearnDisabled_Type()
)
wwpMacMgmtSacLearnDisabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpMacMgmtSacLearnDisabled.setStatus("current")


class _WwpMacMgmtSacMacFlush_Type(Integer32):
    """Custom type wwpMacMgmtSacMacFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flush", 1),
          ("none", 0))
    )


_WwpMacMgmtSacMacFlush_Type.__name__ = "Integer32"
_WwpMacMgmtSacMacFlush_Object = MibTableColumn
wwpMacMgmtSacMacFlush = _WwpMacMgmtSacMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 6),
    _WwpMacMgmtSacMacFlush_Type()
)
wwpMacMgmtSacMacFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpMacMgmtSacMacFlush.setStatus("current")
_WwpMacMgmtSacStatus_Type = RowStatus
_WwpMacMgmtSacStatus_Object = MibTableColumn
wwpMacMgmtSacStatus = _WwpMacMgmtSacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 7),
    _WwpMacMgmtSacStatus_Type()
)
wwpMacMgmtSacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpMacMgmtSacStatus.setStatus("current")
_WwpMacMgmtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpMacMgmtMIBNotificationPrefix = _WwpMacMgmtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 2)
)
_WwpMacMgmtMIBNotifications_ObjectIdentity = ObjectIdentity
wwpMacMgmtMIBNotifications = _WwpMacMgmtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 2, 0)
)
_WwpMacMgmtMIBConformance_ObjectIdentity = ObjectIdentity
wwpMacMgmtMIBConformance = _WwpMacMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 3)
)
_WwpMacMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
wwpMacMgmtMIBCompliances = _WwpMacMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 3, 1)
)
_WwpMacMgmtMIBGroups_ObjectIdentity = ObjectIdentity
wwpMacMgmtMIBGroups = _WwpMacMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 28, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-MAC-MGMT-MIB",
    **{"VlanId": VlanId,
       "wwpMacMgmtMIB": wwpMacMgmtMIB,
       "wwpMacMgmtMIBObjects": wwpMacMgmtMIBObjects,
       "wwpMacMgmt": wwpMacMgmt,
       "wwpMacMgmtMacTable": wwpMacMgmtMacTable,
       "wwpMacMgmtMacEntry": wwpMacMgmtMacEntry,
       "wwpMacMgmtVlanID": wwpMacMgmtVlanID,
       "wwpMacMgmtPortId": wwpMacMgmtPortId,
       "wwpMacMgmtMacAddr": wwpMacMgmtMacAddr,
       "wwpMacMgmtMacAddrMode": wwpMacMgmtMacAddrMode,
       "wwpMacMgmtMacStatus": wwpMacMgmtMacStatus,
       "wwpMacMgmtMacRowStatus": wwpMacMgmtMacRowStatus,
       "wwpMacMgmtMacReset": wwpMacMgmtMacReset,
       "wwpMacMgmtPMTable": wwpMacMgmtPMTable,
       "wwpMacMgmtPMEntry": wwpMacMgmtPMEntry,
       "wwpMacMgmtPMVlanID": wwpMacMgmtPMVlanID,
       "wwpMacMgmtPMPortId": wwpMacMgmtPMPortId,
       "wwpMacMgmtPMLearnLimit": wwpMacMgmtPMLearnLimit,
       "wwpMacMgmtPMLearnCount": wwpMacMgmtPMLearnCount,
       "wwpMacMgmtPMStatus": wwpMacMgmtPMStatus,
       "wwpMacMgmtPMMacFlush": wwpMacMgmtPMMacFlush,
       "wwpMacMgmtCacheMac": wwpMacMgmtCacheMac,
       "wwpMacMgmtCacheMacTable": wwpMacMgmtCacheMacTable,
       "wwpMacMgmtCacheMacEntry": wwpMacMgmtCacheMacEntry,
       "wwpMacMgmtCVlanID": wwpMacMgmtCVlanID,
       "wwpMacMgmtCPortId": wwpMacMgmtCPortId,
       "wwpMacMgmtCMacIndex": wwpMacMgmtCMacIndex,
       "wwpMacMgmtCMacAddr": wwpMacMgmtCMacAddr,
       "wwpMacMgmtCMacAddrMode": wwpMacMgmtCMacAddrMode,
       "wwpMacMgmtCMacStatus": wwpMacMgmtCMacStatus,
       "wwpMacMgmtCacheMacCountTable": wwpMacMgmtCacheMacCountTable,
       "wwpMacMgmtCacheMacCountEntry": wwpMacMgmtCacheMacCountEntry,
       "wwpMacMgmtCacheMacCount": wwpMacMgmtCacheMacCount,
       "wwpMacMgmtSacTable": wwpMacMgmtSacTable,
       "wwpMacMgmtSacEntry": wwpMacMgmtSacEntry,
       "wwpMacMgmtSacVlanID": wwpMacMgmtSacVlanID,
       "wwpMacMgmtSacPortId": wwpMacMgmtSacPortId,
       "wwpMacMgmtSacLearnCount": wwpMacMgmtSacLearnCount,
       "wwpMacMgmtSacMaxLearn": wwpMacMgmtSacMaxLearn,
       "wwpMacMgmtSacLearnDisabled": wwpMacMgmtSacLearnDisabled,
       "wwpMacMgmtSacMacFlush": wwpMacMgmtSacMacFlush,
       "wwpMacMgmtSacStatus": wwpMacMgmtSacStatus,
       "wwpMacMgmtMIBNotificationPrefix": wwpMacMgmtMIBNotificationPrefix,
       "wwpMacMgmtMIBNotifications": wwpMacMgmtMIBNotifications,
       "wwpMacMgmtMIBConformance": wwpMacMgmtMIBConformance,
       "wwpMacMgmtMIBCompliances": wwpMacMgmtMIBCompliances,
       "wwpMacMgmtMIBGroups": wwpMacMgmtMIBGroups}
)
