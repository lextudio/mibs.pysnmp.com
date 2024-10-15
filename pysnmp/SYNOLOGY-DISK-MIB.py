# SNMP MIB module (SYNOLOGY-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOLOGY-DISK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:58 2024
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

synoDisk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2)
)
synoDisk.setRevisions(
        ("2013-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1)
)
diskEntry.setIndexNames(
    (0, "SYNOLOGY-DISK-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")


class _DiskIndex_Type(Integer32):
    """Custom type diskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiskIndex_Type.__name__ = "Integer32"
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskID_Type = OctetString
_DiskID_Object = MibTableColumn
diskID = _DiskID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 2),
    _DiskID_Type()
)
diskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskID.setStatus("current")
_DiskModel_Type = OctetString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskType_Type = OctetString
_DiskType_Object = MibTableColumn
diskType = _DiskType_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 4),
    _DiskType_Type()
)
diskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskType.setStatus("current")


class _DiskStatus_Type(Integer32):
    """Custom type diskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DiskStatus_Type.__name__ = "Integer32"
_DiskStatus_Object = MibTableColumn
diskStatus = _DiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 5),
    _DiskStatus_Type()
)
diskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatus.setStatus("current")
_DiskTemperature_Type = Integer32
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 6),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("current")
_DiskConformance_ObjectIdentity = ObjectIdentity
diskConformance = _DiskConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2)
)
_DiskCompliances_ObjectIdentity = ObjectIdentity
diskCompliances = _DiskCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 1)
)
_DiskGroups_ObjectIdentity = ObjectIdentity
diskGroups = _DiskGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 2)
)

# Managed Objects groups

diskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 2, 1)
)
diskGroup.setObjects(
      *(("SYNOLOGY-DISK-MIB", "diskID"),
        ("SYNOLOGY-DISK-MIB", "diskModel"),
        ("SYNOLOGY-DISK-MIB", "diskType"),
        ("SYNOLOGY-DISK-MIB", "diskStatus"),
        ("SYNOLOGY-DISK-MIB", "diskTemperature"))
)
if mibBuilder.loadTexts:
    diskGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diskCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    diskCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-DISK-MIB",
    **{"synology": synology,
       "synoDisk": synoDisk,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskID": diskID,
       "diskModel": diskModel,
       "diskType": diskType,
       "diskStatus": diskStatus,
       "diskTemperature": diskTemperature,
       "diskConformance": diskConformance,
       "diskCompliances": diskCompliances,
       "diskCompliance": diskCompliance,
       "diskGroups": diskGroups,
       "diskGroup": diskGroup}
)
