# SNMP MIB module (Juniper-SMDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SMDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:19 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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


# MODULE-IDENTITY

juniSmdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50)
)
juniSmdsMIB.setRevisions(
        ("2002-09-16 21:44",
         "2001-09-20 14:41",
         "2001-03-08 20:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniSmdsObjects_ObjectIdentity = ObjectIdentity
juniSmdsObjects = _JuniSmdsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1)
)
_JuniSmdsNextIfIndex_Type = JuniNextIfIndex
_JuniSmdsNextIfIndex_Object = MibScalar
juniSmdsNextIfIndex = _JuniSmdsNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 1),
    _JuniSmdsNextIfIndex_Type()
)
juniSmdsNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsNextIfIndex.setStatus("current")
_JuniSmdsIfTable_Object = MibTable
juniSmdsIfTable = _JuniSmdsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2)
)
if mibBuilder.loadTexts:
    juniSmdsIfTable.setStatus("current")
_JuniSmdsIfEntry_Object = MibTableRow
juniSmdsIfEntry = _JuniSmdsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1)
)
juniSmdsIfEntry.setIndexNames(
    (0, "Juniper-SMDS-MIB", "juniSmdsIfIndex"),
)
if mibBuilder.loadTexts:
    juniSmdsIfEntry.setStatus("current")
_JuniSmdsIfIndex_Type = InterfaceIndex
_JuniSmdsIfIndex_Object = MibTableColumn
juniSmdsIfIndex = _JuniSmdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 1),
    _JuniSmdsIfIndex_Type()
)
juniSmdsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSmdsIfIndex.setStatus("current")
_JuniSmdsIfRowStatus_Type = RowStatus
_JuniSmdsIfRowStatus_Object = MibTableColumn
juniSmdsIfRowStatus = _JuniSmdsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 2),
    _JuniSmdsIfRowStatus_Type()
)
juniSmdsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsIfRowStatus.setStatus("current")
_JuniSmdsIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniSmdsIfLowerIfIndex_Object = MibTableColumn
juniSmdsIfLowerIfIndex = _JuniSmdsIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 3),
    _JuniSmdsIfLowerIfIndex_Type()
)
juniSmdsIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsIfLowerIfIndex.setStatus("current")
_JuniSmdsMajorNextIfIndex_Type = JuniNextIfIndex
_JuniSmdsMajorNextIfIndex_Object = MibScalar
juniSmdsMajorNextIfIndex = _JuniSmdsMajorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 3),
    _JuniSmdsMajorNextIfIndex_Type()
)
juniSmdsMajorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsMajorNextIfIndex.setStatus("current")
_JuniSmdsMajorIfTable_Object = MibTable
juniSmdsMajorIfTable = _JuniSmdsMajorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4)
)
if mibBuilder.loadTexts:
    juniSmdsMajorIfTable.setStatus("current")
_JuniSmdsMajorIfEntry_Object = MibTableRow
juniSmdsMajorIfEntry = _JuniSmdsMajorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1)
)
juniSmdsMajorIfEntry.setIndexNames(
    (0, "Juniper-SMDS-MIB", "juniSmdsMajorIfIndex"),
)
if mibBuilder.loadTexts:
    juniSmdsMajorIfEntry.setStatus("current")
_JuniSmdsMajorIfIndex_Type = InterfaceIndex
_JuniSmdsMajorIfIndex_Object = MibTableColumn
juniSmdsMajorIfIndex = _JuniSmdsMajorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 1),
    _JuniSmdsMajorIfIndex_Type()
)
juniSmdsMajorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSmdsMajorIfIndex.setStatus("current")
_JuniSmdsMajorIfRowStatus_Type = RowStatus
_JuniSmdsMajorIfRowStatus_Object = MibTableColumn
juniSmdsMajorIfRowStatus = _JuniSmdsMajorIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 2),
    _JuniSmdsMajorIfRowStatus_Type()
)
juniSmdsMajorIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsMajorIfRowStatus.setStatus("current")
_JuniSmdsMajorIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniSmdsMajorIfLowerIfIndex_Object = MibTableColumn
juniSmdsMajorIfLowerIfIndex = _JuniSmdsMajorIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 3),
    _JuniSmdsMajorIfLowerIfIndex_Type()
)
juniSmdsMajorIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsMajorIfLowerIfIndex.setStatus("current")


class _JuniSmdsMajorIfKeepalive_Type(Integer32):
    """Custom type juniSmdsMajorIfKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 32767),
    )


_JuniSmdsMajorIfKeepalive_Type.__name__ = "Integer32"
_JuniSmdsMajorIfKeepalive_Object = MibTableColumn
juniSmdsMajorIfKeepalive = _JuniSmdsMajorIfKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 4),
    _JuniSmdsMajorIfKeepalive_Type()
)
juniSmdsMajorIfKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsMajorIfKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    juniSmdsMajorIfKeepalive.setUnits("seconds")
_JuniSmdsSubNextIfIndex_Type = JuniNextIfIndex
_JuniSmdsSubNextIfIndex_Object = MibScalar
juniSmdsSubNextIfIndex = _JuniSmdsSubNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 5),
    _JuniSmdsSubNextIfIndex_Type()
)
juniSmdsSubNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsSubNextIfIndex.setStatus("current")
_JuniSmdsSubIfTable_Object = MibTable
juniSmdsSubIfTable = _JuniSmdsSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6)
)
if mibBuilder.loadTexts:
    juniSmdsSubIfTable.setStatus("current")
_JuniSmdsSubIfEntry_Object = MibTableRow
juniSmdsSubIfEntry = _JuniSmdsSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1)
)
juniSmdsSubIfEntry.setIndexNames(
    (0, "Juniper-SMDS-MIB", "juniSmdsSubIfIndex"),
)
if mibBuilder.loadTexts:
    juniSmdsSubIfEntry.setStatus("current")
_JuniSmdsSubIfIndex_Type = InterfaceIndex
_JuniSmdsSubIfIndex_Object = MibTableColumn
juniSmdsSubIfIndex = _JuniSmdsSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 1),
    _JuniSmdsSubIfIndex_Type()
)
juniSmdsSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSmdsSubIfIndex.setStatus("current")
_JuniSmdsSubIfRowStatus_Type = RowStatus
_JuniSmdsSubIfRowStatus_Object = MibTableColumn
juniSmdsSubIfRowStatus = _JuniSmdsSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 2),
    _JuniSmdsSubIfRowStatus_Type()
)
juniSmdsSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsSubIfRowStatus.setStatus("current")
_JuniSmdsSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniSmdsSubIfLowerIfIndex_Object = MibTableColumn
juniSmdsSubIfLowerIfIndex = _JuniSmdsSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 3),
    _JuniSmdsSubIfLowerIfIndex_Type()
)
juniSmdsSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsSubIfLowerIfIndex.setStatus("current")


class _JuniSmdsSubIfSmdsAddress_Type(OctetString):
    """Custom type juniSmdsSubIfSmdsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniSmdsSubIfSmdsAddress_Type.__name__ = "OctetString"
_JuniSmdsSubIfSmdsAddress_Object = MibTableColumn
juniSmdsSubIfSmdsAddress = _JuniSmdsSubIfSmdsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 4),
    _JuniSmdsSubIfSmdsAddress_Type()
)
juniSmdsSubIfSmdsAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsSubIfSmdsAddress.setStatus("current")


class _JuniSmdsSubIfSmdsMulticastIpAddress_Type(OctetString):
    """Custom type juniSmdsSubIfSmdsMulticastIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniSmdsSubIfSmdsMulticastIpAddress_Type.__name__ = "OctetString"
_JuniSmdsSubIfSmdsMulticastIpAddress_Object = MibTableColumn
juniSmdsSubIfSmdsMulticastIpAddress = _JuniSmdsSubIfSmdsMulticastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 5),
    _JuniSmdsSubIfSmdsMulticastIpAddress_Type()
)
juniSmdsSubIfSmdsMulticastIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsSubIfSmdsMulticastIpAddress.setStatus("current")


class _JuniSmdsSubIfSmdsMulticastArpAddress_Type(OctetString):
    """Custom type juniSmdsSubIfSmdsMulticastArpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniSmdsSubIfSmdsMulticastArpAddress_Type.__name__ = "OctetString"
_JuniSmdsSubIfSmdsMulticastArpAddress_Object = MibTableColumn
juniSmdsSubIfSmdsMulticastArpAddress = _JuniSmdsSubIfSmdsMulticastArpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 6),
    _JuniSmdsSubIfSmdsMulticastArpAddress_Type()
)
juniSmdsSubIfSmdsMulticastArpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSmdsSubIfSmdsMulticastArpAddress.setStatus("current")
_JuniSmdsMajorIfStatsTable_Object = MibTable
juniSmdsMajorIfStatsTable = _JuniSmdsMajorIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7)
)
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsTable.setStatus("current")
_JuniSmdsMajorIfStatsEntry_Object = MibTableRow
juniSmdsMajorIfStatsEntry = _JuniSmdsMajorIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1)
)
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsEntry.setStatus("current")
_JuniSmdsMajorIfStatsInKeepaliveRequests_Type = Counter32
_JuniSmdsMajorIfStatsInKeepaliveRequests_Object = MibTableColumn
juniSmdsMajorIfStatsInKeepaliveRequests = _JuniSmdsMajorIfStatsInKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 1),
    _JuniSmdsMajorIfStatsInKeepaliveRequests_Type()
)
juniSmdsMajorIfStatsInKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsInKeepaliveRequests.setStatus("current")
_JuniSmdsMajorIfStatsOutKeepaliveRequests_Type = Counter32
_JuniSmdsMajorIfStatsOutKeepaliveRequests_Object = MibTableColumn
juniSmdsMajorIfStatsOutKeepaliveRequests = _JuniSmdsMajorIfStatsOutKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 2),
    _JuniSmdsMajorIfStatsOutKeepaliveRequests_Type()
)
juniSmdsMajorIfStatsOutKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsOutKeepaliveRequests.setStatus("current")
_JuniSmdsMajorIfStatsInKeepaliveReplies_Type = Counter32
_JuniSmdsMajorIfStatsInKeepaliveReplies_Object = MibTableColumn
juniSmdsMajorIfStatsInKeepaliveReplies = _JuniSmdsMajorIfStatsInKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 3),
    _JuniSmdsMajorIfStatsInKeepaliveReplies_Type()
)
juniSmdsMajorIfStatsInKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsInKeepaliveReplies.setStatus("current")
_JuniSmdsMajorIfStatsOutKeepaliveReplies_Type = Counter32
_JuniSmdsMajorIfStatsOutKeepaliveReplies_Object = MibTableColumn
juniSmdsMajorIfStatsOutKeepaliveReplies = _JuniSmdsMajorIfStatsOutKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 4),
    _JuniSmdsMajorIfStatsOutKeepaliveReplies_Type()
)
juniSmdsMajorIfStatsOutKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsOutKeepaliveReplies.setStatus("current")
_JuniSmdsMajorIfStatsKeepaliveFailures_Type = Counter32
_JuniSmdsMajorIfStatsKeepaliveFailures_Object = MibTableColumn
juniSmdsMajorIfStatsKeepaliveFailures = _JuniSmdsMajorIfStatsKeepaliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 5),
    _JuniSmdsMajorIfStatsKeepaliveFailures_Type()
)
juniSmdsMajorIfStatsKeepaliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSmdsMajorIfStatsKeepaliveFailures.setStatus("current")
_JuniSmdsConformance_ObjectIdentity = ObjectIdentity
juniSmdsConformance = _JuniSmdsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4)
)
_JuniSmdsCompliances_ObjectIdentity = ObjectIdentity
juniSmdsCompliances = _JuniSmdsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1)
)
_JuniSmdsGroups_ObjectIdentity = ObjectIdentity
juniSmdsGroups = _JuniSmdsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2)
)
juniSmdsMajorIfEntry.registerAugmentions(
    ("Juniper-SMDS-MIB",
     "juniSmdsMajorIfStatsEntry")
)
juniSmdsMajorIfStatsEntry.setIndexNames(*juniSmdsMajorIfEntry.getIndexNames())

# Managed Objects groups

juniSmdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2, 1)
)
juniSmdsGroup.setObjects(
      *(("Juniper-SMDS-MIB", "juniSmdsNextIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsIfRowStatus"),
        ("Juniper-SMDS-MIB", "juniSmdsIfLowerIfIndex"))
)
if mibBuilder.loadTexts:
    juniSmdsGroup.setStatus("obsolete")

juniSmdsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2, 2)
)
juniSmdsGroup2.setObjects(
      *(("Juniper-SMDS-MIB", "juniSmdsNextIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsIfRowStatus"),
        ("Juniper-SMDS-MIB", "juniSmdsIfLowerIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorNextIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfRowStatus"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfLowerIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfKeepalive"),
        ("Juniper-SMDS-MIB", "juniSmdsSubNextIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsSubIfRowStatus"),
        ("Juniper-SMDS-MIB", "juniSmdsSubIfLowerIfIndex"),
        ("Juniper-SMDS-MIB", "juniSmdsSubIfSmdsAddress"),
        ("Juniper-SMDS-MIB", "juniSmdsSubIfSmdsMulticastIpAddress"),
        ("Juniper-SMDS-MIB", "juniSmdsSubIfSmdsMulticastArpAddress"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsInKeepaliveRequests"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsOutKeepaliveRequests"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsInKeepaliveReplies"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsOutKeepaliveReplies"),
        ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsKeepaliveFailures"))
)
if mibBuilder.loadTexts:
    juniSmdsGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniSmdsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniSmdsCompliance.setStatus(
        "obsolete"
    )

juniSmdsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniSmdsCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SMDS-MIB",
    **{"juniSmdsMIB": juniSmdsMIB,
       "juniSmdsObjects": juniSmdsObjects,
       "juniSmdsNextIfIndex": juniSmdsNextIfIndex,
       "juniSmdsIfTable": juniSmdsIfTable,
       "juniSmdsIfEntry": juniSmdsIfEntry,
       "juniSmdsIfIndex": juniSmdsIfIndex,
       "juniSmdsIfRowStatus": juniSmdsIfRowStatus,
       "juniSmdsIfLowerIfIndex": juniSmdsIfLowerIfIndex,
       "juniSmdsMajorNextIfIndex": juniSmdsMajorNextIfIndex,
       "juniSmdsMajorIfTable": juniSmdsMajorIfTable,
       "juniSmdsMajorIfEntry": juniSmdsMajorIfEntry,
       "juniSmdsMajorIfIndex": juniSmdsMajorIfIndex,
       "juniSmdsMajorIfRowStatus": juniSmdsMajorIfRowStatus,
       "juniSmdsMajorIfLowerIfIndex": juniSmdsMajorIfLowerIfIndex,
       "juniSmdsMajorIfKeepalive": juniSmdsMajorIfKeepalive,
       "juniSmdsSubNextIfIndex": juniSmdsSubNextIfIndex,
       "juniSmdsSubIfTable": juniSmdsSubIfTable,
       "juniSmdsSubIfEntry": juniSmdsSubIfEntry,
       "juniSmdsSubIfIndex": juniSmdsSubIfIndex,
       "juniSmdsSubIfRowStatus": juniSmdsSubIfRowStatus,
       "juniSmdsSubIfLowerIfIndex": juniSmdsSubIfLowerIfIndex,
       "juniSmdsSubIfSmdsAddress": juniSmdsSubIfSmdsAddress,
       "juniSmdsSubIfSmdsMulticastIpAddress": juniSmdsSubIfSmdsMulticastIpAddress,
       "juniSmdsSubIfSmdsMulticastArpAddress": juniSmdsSubIfSmdsMulticastArpAddress,
       "juniSmdsMajorIfStatsTable": juniSmdsMajorIfStatsTable,
       "juniSmdsMajorIfStatsEntry": juniSmdsMajorIfStatsEntry,
       "juniSmdsMajorIfStatsInKeepaliveRequests": juniSmdsMajorIfStatsInKeepaliveRequests,
       "juniSmdsMajorIfStatsOutKeepaliveRequests": juniSmdsMajorIfStatsOutKeepaliveRequests,
       "juniSmdsMajorIfStatsInKeepaliveReplies": juniSmdsMajorIfStatsInKeepaliveReplies,
       "juniSmdsMajorIfStatsOutKeepaliveReplies": juniSmdsMajorIfStatsOutKeepaliveReplies,
       "juniSmdsMajorIfStatsKeepaliveFailures": juniSmdsMajorIfStatsKeepaliveFailures,
       "juniSmdsConformance": juniSmdsConformance,
       "juniSmdsCompliances": juniSmdsCompliances,
       "juniSmdsCompliance": juniSmdsCompliance,
       "juniSmdsCompliance2": juniSmdsCompliance2,
       "juniSmdsGroups": juniSmdsGroups,
       "juniSmdsGroup": juniSmdsGroup,
       "juniSmdsGroup2": juniSmdsGroup2}
)
