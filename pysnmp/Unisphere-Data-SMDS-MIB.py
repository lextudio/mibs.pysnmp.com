# SNMP MIB module (Unisphere-Data-SMDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SMDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:35 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdSmdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50)
)
usdSmdsMIB.setRevisions(
        ("2001-09-20 14:41",
         "2001-03-08 20:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdSmdsObjects_ObjectIdentity = ObjectIdentity
usdSmdsObjects = _UsdSmdsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1)
)
_UsdSmdsNextIfIndex_Type = UsdNextIfIndex
_UsdSmdsNextIfIndex_Object = MibScalar
usdSmdsNextIfIndex = _UsdSmdsNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 1),
    _UsdSmdsNextIfIndex_Type()
)
usdSmdsNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsNextIfIndex.setStatus("current")
_UsdSmdsIfTable_Object = MibTable
usdSmdsIfTable = _UsdSmdsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2)
)
if mibBuilder.loadTexts:
    usdSmdsIfTable.setStatus("current")
_UsdSmdsIfEntry_Object = MibTableRow
usdSmdsIfEntry = _UsdSmdsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1)
)
usdSmdsIfEntry.setIndexNames(
    (0, "Unisphere-Data-SMDS-MIB", "usdSmdsIfIndex"),
)
if mibBuilder.loadTexts:
    usdSmdsIfEntry.setStatus("current")
_UsdSmdsIfIndex_Type = InterfaceIndex
_UsdSmdsIfIndex_Object = MibTableColumn
usdSmdsIfIndex = _UsdSmdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 1),
    _UsdSmdsIfIndex_Type()
)
usdSmdsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSmdsIfIndex.setStatus("current")
_UsdSmdsIfRowStatus_Type = RowStatus
_UsdSmdsIfRowStatus_Object = MibTableColumn
usdSmdsIfRowStatus = _UsdSmdsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 2),
    _UsdSmdsIfRowStatus_Type()
)
usdSmdsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsIfRowStatus.setStatus("current")
_UsdSmdsIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdSmdsIfLowerIfIndex_Object = MibTableColumn
usdSmdsIfLowerIfIndex = _UsdSmdsIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 3),
    _UsdSmdsIfLowerIfIndex_Type()
)
usdSmdsIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsIfLowerIfIndex.setStatus("current")
_UsdSmdsMajorNextIfIndex_Type = UsdNextIfIndex
_UsdSmdsMajorNextIfIndex_Object = MibScalar
usdSmdsMajorNextIfIndex = _UsdSmdsMajorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 3),
    _UsdSmdsMajorNextIfIndex_Type()
)
usdSmdsMajorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsMajorNextIfIndex.setStatus("current")
_UsdSmdsMajorIfTable_Object = MibTable
usdSmdsMajorIfTable = _UsdSmdsMajorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4)
)
if mibBuilder.loadTexts:
    usdSmdsMajorIfTable.setStatus("current")
_UsdSmdsMajorIfEntry_Object = MibTableRow
usdSmdsMajorIfEntry = _UsdSmdsMajorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1)
)
usdSmdsMajorIfEntry.setIndexNames(
    (0, "Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfIndex"),
)
if mibBuilder.loadTexts:
    usdSmdsMajorIfEntry.setStatus("current")
_UsdSmdsMajorIfIndex_Type = InterfaceIndex
_UsdSmdsMajorIfIndex_Object = MibTableColumn
usdSmdsMajorIfIndex = _UsdSmdsMajorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 1),
    _UsdSmdsMajorIfIndex_Type()
)
usdSmdsMajorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSmdsMajorIfIndex.setStatus("current")
_UsdSmdsMajorIfRowStatus_Type = RowStatus
_UsdSmdsMajorIfRowStatus_Object = MibTableColumn
usdSmdsMajorIfRowStatus = _UsdSmdsMajorIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 2),
    _UsdSmdsMajorIfRowStatus_Type()
)
usdSmdsMajorIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsMajorIfRowStatus.setStatus("current")
_UsdSmdsMajorIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdSmdsMajorIfLowerIfIndex_Object = MibTableColumn
usdSmdsMajorIfLowerIfIndex = _UsdSmdsMajorIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 3),
    _UsdSmdsMajorIfLowerIfIndex_Type()
)
usdSmdsMajorIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsMajorIfLowerIfIndex.setStatus("current")


class _UsdSmdsMajorIfKeepalive_Type(Integer32):
    """Custom type usdSmdsMajorIfKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 32767),
    )


_UsdSmdsMajorIfKeepalive_Type.__name__ = "Integer32"
_UsdSmdsMajorIfKeepalive_Object = MibTableColumn
usdSmdsMajorIfKeepalive = _UsdSmdsMajorIfKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 4),
    _UsdSmdsMajorIfKeepalive_Type()
)
usdSmdsMajorIfKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsMajorIfKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    usdSmdsMajorIfKeepalive.setUnits("seconds")
_UsdSmdsSubNextIfIndex_Type = UsdNextIfIndex
_UsdSmdsSubNextIfIndex_Object = MibScalar
usdSmdsSubNextIfIndex = _UsdSmdsSubNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 5),
    _UsdSmdsSubNextIfIndex_Type()
)
usdSmdsSubNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsSubNextIfIndex.setStatus("current")
_UsdSmdsSubIfTable_Object = MibTable
usdSmdsSubIfTable = _UsdSmdsSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6)
)
if mibBuilder.loadTexts:
    usdSmdsSubIfTable.setStatus("current")
_UsdSmdsSubIfEntry_Object = MibTableRow
usdSmdsSubIfEntry = _UsdSmdsSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1)
)
usdSmdsSubIfEntry.setIndexNames(
    (0, "Unisphere-Data-SMDS-MIB", "usdSmdsSubIfIndex"),
)
if mibBuilder.loadTexts:
    usdSmdsSubIfEntry.setStatus("current")
_UsdSmdsSubIfIndex_Type = InterfaceIndex
_UsdSmdsSubIfIndex_Object = MibTableColumn
usdSmdsSubIfIndex = _UsdSmdsSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 1),
    _UsdSmdsSubIfIndex_Type()
)
usdSmdsSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSmdsSubIfIndex.setStatus("current")
_UsdSmdsSubIfRowStatus_Type = RowStatus
_UsdSmdsSubIfRowStatus_Object = MibTableColumn
usdSmdsSubIfRowStatus = _UsdSmdsSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 2),
    _UsdSmdsSubIfRowStatus_Type()
)
usdSmdsSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsSubIfRowStatus.setStatus("current")
_UsdSmdsSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdSmdsSubIfLowerIfIndex_Object = MibTableColumn
usdSmdsSubIfLowerIfIndex = _UsdSmdsSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 3),
    _UsdSmdsSubIfLowerIfIndex_Type()
)
usdSmdsSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsSubIfLowerIfIndex.setStatus("current")


class _UsdSmdsSubIfSmdsAddress_Type(OctetString):
    """Custom type usdSmdsSubIfSmdsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdSmdsSubIfSmdsAddress_Type.__name__ = "OctetString"
_UsdSmdsSubIfSmdsAddress_Object = MibTableColumn
usdSmdsSubIfSmdsAddress = _UsdSmdsSubIfSmdsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 4),
    _UsdSmdsSubIfSmdsAddress_Type()
)
usdSmdsSubIfSmdsAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsSubIfSmdsAddress.setStatus("current")


class _UsdSmdsSubIfSmdsMulticastIpAddress_Type(OctetString):
    """Custom type usdSmdsSubIfSmdsMulticastIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdSmdsSubIfSmdsMulticastIpAddress_Type.__name__ = "OctetString"
_UsdSmdsSubIfSmdsMulticastIpAddress_Object = MibTableColumn
usdSmdsSubIfSmdsMulticastIpAddress = _UsdSmdsSubIfSmdsMulticastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 5),
    _UsdSmdsSubIfSmdsMulticastIpAddress_Type()
)
usdSmdsSubIfSmdsMulticastIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsSubIfSmdsMulticastIpAddress.setStatus("current")


class _UsdSmdsSubIfSmdsMulticastArpAddress_Type(OctetString):
    """Custom type usdSmdsSubIfSmdsMulticastArpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdSmdsSubIfSmdsMulticastArpAddress_Type.__name__ = "OctetString"
_UsdSmdsSubIfSmdsMulticastArpAddress_Object = MibTableColumn
usdSmdsSubIfSmdsMulticastArpAddress = _UsdSmdsSubIfSmdsMulticastArpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 6),
    _UsdSmdsSubIfSmdsMulticastArpAddress_Type()
)
usdSmdsSubIfSmdsMulticastArpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSmdsSubIfSmdsMulticastArpAddress.setStatus("current")
_UsdSmdsMajorIfStatsTable_Object = MibTable
usdSmdsMajorIfStatsTable = _UsdSmdsMajorIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7)
)
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsTable.setStatus("current")
_UsdSmdsMajorIfStatsEntry_Object = MibTableRow
usdSmdsMajorIfStatsEntry = _UsdSmdsMajorIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1)
)
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsEntry.setStatus("current")
_UsdSmdsMajorIfStatsInKeepaliveRequests_Type = Counter32
_UsdSmdsMajorIfStatsInKeepaliveRequests_Object = MibTableColumn
usdSmdsMajorIfStatsInKeepaliveRequests = _UsdSmdsMajorIfStatsInKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 1),
    _UsdSmdsMajorIfStatsInKeepaliveRequests_Type()
)
usdSmdsMajorIfStatsInKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsInKeepaliveRequests.setStatus("current")
_UsdSmdsMajorIfStatsOutKeepaliveRequests_Type = Counter32
_UsdSmdsMajorIfStatsOutKeepaliveRequests_Object = MibTableColumn
usdSmdsMajorIfStatsOutKeepaliveRequests = _UsdSmdsMajorIfStatsOutKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 2),
    _UsdSmdsMajorIfStatsOutKeepaliveRequests_Type()
)
usdSmdsMajorIfStatsOutKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsOutKeepaliveRequests.setStatus("current")
_UsdSmdsMajorIfStatsInKeepaliveReplies_Type = Counter32
_UsdSmdsMajorIfStatsInKeepaliveReplies_Object = MibTableColumn
usdSmdsMajorIfStatsInKeepaliveReplies = _UsdSmdsMajorIfStatsInKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 3),
    _UsdSmdsMajorIfStatsInKeepaliveReplies_Type()
)
usdSmdsMajorIfStatsInKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsInKeepaliveReplies.setStatus("current")
_UsdSmdsMajorIfStatsOutKeepaliveReplies_Type = Counter32
_UsdSmdsMajorIfStatsOutKeepaliveReplies_Object = MibTableColumn
usdSmdsMajorIfStatsOutKeepaliveReplies = _UsdSmdsMajorIfStatsOutKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 4),
    _UsdSmdsMajorIfStatsOutKeepaliveReplies_Type()
)
usdSmdsMajorIfStatsOutKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsOutKeepaliveReplies.setStatus("current")
_UsdSmdsMajorIfStatsKeepaliveFailures_Type = Counter32
_UsdSmdsMajorIfStatsKeepaliveFailures_Object = MibTableColumn
usdSmdsMajorIfStatsKeepaliveFailures = _UsdSmdsMajorIfStatsKeepaliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 5),
    _UsdSmdsMajorIfStatsKeepaliveFailures_Type()
)
usdSmdsMajorIfStatsKeepaliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSmdsMajorIfStatsKeepaliveFailures.setStatus("current")
_UsdSmdsConformance_ObjectIdentity = ObjectIdentity
usdSmdsConformance = _UsdSmdsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4)
)
_UsdSmdsCompliances_ObjectIdentity = ObjectIdentity
usdSmdsCompliances = _UsdSmdsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1)
)
_UsdSmdsGroups_ObjectIdentity = ObjectIdentity
usdSmdsGroups = _UsdSmdsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2)
)
usdSmdsMajorIfEntry.registerAugmentions(
    ("Unisphere-Data-SMDS-MIB",
     "usdSmdsMajorIfStatsEntry")
)
usdSmdsMajorIfStatsEntry.setIndexNames(*usdSmdsMajorIfEntry.getIndexNames())

# Managed Objects groups

usdSmdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2, 1)
)
usdSmdsGroup.setObjects(
      *(("Unisphere-Data-SMDS-MIB", "usdSmdsNextIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsIfRowStatus"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsIfLowerIfIndex"))
)
if mibBuilder.loadTexts:
    usdSmdsGroup.setStatus("obsolete")

usdSmdsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2, 2)
)
usdSmdsGroup2.setObjects(
      *(("Unisphere-Data-SMDS-MIB", "usdSmdsNextIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsIfRowStatus"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsIfLowerIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorNextIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfRowStatus"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfLowerIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfKeepalive"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsSubNextIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsSubIfRowStatus"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsSubIfLowerIfIndex"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsSubIfSmdsAddress"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsSubIfSmdsMulticastIpAddress"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsSubIfSmdsMulticastArpAddress"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfStatsInKeepaliveRequests"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfStatsOutKeepaliveRequests"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfStatsInKeepaliveReplies"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfStatsOutKeepaliveReplies"),
        ("Unisphere-Data-SMDS-MIB", "usdSmdsMajorIfStatsKeepaliveFailures"))
)
if mibBuilder.loadTexts:
    usdSmdsGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSmdsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdSmdsCompliance.setStatus(
        "obsolete"
    )

usdSmdsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdSmdsCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SMDS-MIB",
    **{"usdSmdsMIB": usdSmdsMIB,
       "usdSmdsObjects": usdSmdsObjects,
       "usdSmdsNextIfIndex": usdSmdsNextIfIndex,
       "usdSmdsIfTable": usdSmdsIfTable,
       "usdSmdsIfEntry": usdSmdsIfEntry,
       "usdSmdsIfIndex": usdSmdsIfIndex,
       "usdSmdsIfRowStatus": usdSmdsIfRowStatus,
       "usdSmdsIfLowerIfIndex": usdSmdsIfLowerIfIndex,
       "usdSmdsMajorNextIfIndex": usdSmdsMajorNextIfIndex,
       "usdSmdsMajorIfTable": usdSmdsMajorIfTable,
       "usdSmdsMajorIfEntry": usdSmdsMajorIfEntry,
       "usdSmdsMajorIfIndex": usdSmdsMajorIfIndex,
       "usdSmdsMajorIfRowStatus": usdSmdsMajorIfRowStatus,
       "usdSmdsMajorIfLowerIfIndex": usdSmdsMajorIfLowerIfIndex,
       "usdSmdsMajorIfKeepalive": usdSmdsMajorIfKeepalive,
       "usdSmdsSubNextIfIndex": usdSmdsSubNextIfIndex,
       "usdSmdsSubIfTable": usdSmdsSubIfTable,
       "usdSmdsSubIfEntry": usdSmdsSubIfEntry,
       "usdSmdsSubIfIndex": usdSmdsSubIfIndex,
       "usdSmdsSubIfRowStatus": usdSmdsSubIfRowStatus,
       "usdSmdsSubIfLowerIfIndex": usdSmdsSubIfLowerIfIndex,
       "usdSmdsSubIfSmdsAddress": usdSmdsSubIfSmdsAddress,
       "usdSmdsSubIfSmdsMulticastIpAddress": usdSmdsSubIfSmdsMulticastIpAddress,
       "usdSmdsSubIfSmdsMulticastArpAddress": usdSmdsSubIfSmdsMulticastArpAddress,
       "usdSmdsMajorIfStatsTable": usdSmdsMajorIfStatsTable,
       "usdSmdsMajorIfStatsEntry": usdSmdsMajorIfStatsEntry,
       "usdSmdsMajorIfStatsInKeepaliveRequests": usdSmdsMajorIfStatsInKeepaliveRequests,
       "usdSmdsMajorIfStatsOutKeepaliveRequests": usdSmdsMajorIfStatsOutKeepaliveRequests,
       "usdSmdsMajorIfStatsInKeepaliveReplies": usdSmdsMajorIfStatsInKeepaliveReplies,
       "usdSmdsMajorIfStatsOutKeepaliveReplies": usdSmdsMajorIfStatsOutKeepaliveReplies,
       "usdSmdsMajorIfStatsKeepaliveFailures": usdSmdsMajorIfStatsKeepaliveFailures,
       "usdSmdsConformance": usdSmdsConformance,
       "usdSmdsCompliances": usdSmdsCompliances,
       "usdSmdsCompliance": usdSmdsCompliance,
       "usdSmdsCompliance2": usdSmdsCompliance2,
       "usdSmdsGroups": usdSmdsGroups,
       "usdSmdsGroup": usdSmdsGroup,
       "usdSmdsGroup2": usdSmdsGroup2}
)
