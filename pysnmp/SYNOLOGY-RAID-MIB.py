# SNMP MIB module (SYNOLOGY-RAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOLOGY-RAID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:59 2024
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

synoRaid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3)
)
synoRaid.setRevisions(
        ("2013-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_RaidTable_Object = MibTable
raidTable = _RaidTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1)
)
if mibBuilder.loadTexts:
    raidTable.setStatus("current")
_RaidEntry_Object = MibTableRow
raidEntry = _RaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1)
)
raidEntry.setIndexNames(
    (0, "SYNOLOGY-RAID-MIB", "raidIndex"),
)
if mibBuilder.loadTexts:
    raidEntry.setStatus("current")


class _RaidIndex_Type(Integer32):
    """Custom type raidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaidIndex_Type.__name__ = "Integer32"
_RaidIndex_Object = MibTableColumn
raidIndex = _RaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 1),
    _RaidIndex_Type()
)
raidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raidIndex.setStatus("current")
_RaidName_Type = OctetString
_RaidName_Object = MibTableColumn
raidName = _RaidName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 2),
    _RaidName_Type()
)
raidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidName.setStatus("current")


class _RaidStatus_Type(Integer32):
    """Custom type raidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RaidStatus_Type.__name__ = "Integer32"
_RaidStatus_Object = MibTableColumn
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 3),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")
_RaidConformance_ObjectIdentity = ObjectIdentity
raidConformance = _RaidConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2)
)
_RaidCompliances_ObjectIdentity = ObjectIdentity
raidCompliances = _RaidCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 1)
)
_RaidGroups_ObjectIdentity = ObjectIdentity
raidGroups = _RaidGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 2)
)

# Managed Objects groups

raidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 2, 1)
)
raidGroup.setObjects(
      *(("SYNOLOGY-RAID-MIB", "raidName"),
        ("SYNOLOGY-RAID-MIB", "raidStatus"))
)
if mibBuilder.loadTexts:
    raidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

raidCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    raidCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-RAID-MIB",
    **{"synology": synology,
       "synoRaid": synoRaid,
       "raidTable": raidTable,
       "raidEntry": raidEntry,
       "raidIndex": raidIndex,
       "raidName": raidName,
       "raidStatus": raidStatus,
       "raidConformance": raidConformance,
       "raidCompliances": raidCompliances,
       "raidCompliance": raidCompliance,
       "raidGroups": raidGroups,
       "raidGroup": raidGroup}
)
