# SNMP MIB module (VPLS-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPLS-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:08 2024
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

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")

(vplsConfigIndex,) = mibBuilder.importSymbols(
    "VPLS-GENERIC-MIB",
    "vplsConfigIndex")


# MODULE-IDENTITY

vplsBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 276)
)
vplsBgpMIB.setRevisions(
        ("2014-05-19 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VplsBgpObjects_ObjectIdentity = ObjectIdentity
vplsBgpObjects = _VplsBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 276, 1)
)
_VplsBgpConfigTable_Object = MibTable
vplsBgpConfigTable = _VplsBgpConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 1)
)
if mibBuilder.loadTexts:
    vplsBgpConfigTable.setStatus("current")
_VplsBgpConfigEntry_Object = MibTableRow
vplsBgpConfigEntry = _VplsBgpConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 1, 1)
)
vplsBgpConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpConfigEntry.setStatus("current")


class _VplsBgpConfigVERangeSize_Type(Unsigned32):
    """Custom type vplsBgpConfigVERangeSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VplsBgpConfigVERangeSize_Type.__name__ = "Unsigned32"
_VplsBgpConfigVERangeSize_Object = MibTableColumn
vplsBgpConfigVERangeSize = _VplsBgpConfigVERangeSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 1, 1, 1),
    _VplsBgpConfigVERangeSize_Type()
)
vplsBgpConfigVERangeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsBgpConfigVERangeSize.setStatus("current")
_VplsBgpVETable_Object = MibTable
vplsBgpVETable = _VplsBgpVETable_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2)
)
if mibBuilder.loadTexts:
    vplsBgpVETable.setStatus("current")
_VplsBgpVEEntry_Object = MibTableRow
vplsBgpVEEntry = _VplsBgpVEEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2, 1)
)
vplsBgpVEEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "VPLS-BGP-MIB", "vplsBgpVEId"),
)
if mibBuilder.loadTexts:
    vplsBgpVEEntry.setStatus("current")


class _VplsBgpVEId_Type(Unsigned32):
    """Custom type vplsBgpVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VplsBgpVEId_Type.__name__ = "Unsigned32"
_VplsBgpVEId_Object = MibTableColumn
vplsBgpVEId = _VplsBgpVEId_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2, 1, 1),
    _VplsBgpVEId_Type()
)
vplsBgpVEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsBgpVEId.setStatus("current")
_VplsBgpVEName_Type = SnmpAdminString
_VplsBgpVEName_Object = MibTableColumn
vplsBgpVEName = _VplsBgpVEName_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2, 1, 2),
    _VplsBgpVEName_Type()
)
vplsBgpVEName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVEName.setStatus("current")


class _VplsBgpVEPreference_Type(Unsigned32):
    """Custom type vplsBgpVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VplsBgpVEPreference_Type.__name__ = "Unsigned32"
_VplsBgpVEPreference_Object = MibTableColumn
vplsBgpVEPreference = _VplsBgpVEPreference_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2, 1, 3),
    _VplsBgpVEPreference_Type()
)
vplsBgpVEPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVEPreference.setStatus("current")
_VplsBgpVERowStatus_Type = RowStatus
_VplsBgpVERowStatus_Object = MibTableColumn
vplsBgpVERowStatus = _VplsBgpVERowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2, 1, 5),
    _VplsBgpVERowStatus_Type()
)
vplsBgpVERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVERowStatus.setStatus("current")


class _VplsBgpVEStorageType_Type(StorageType):
    """Custom type vplsBgpVEStorageType based on StorageType"""


_VplsBgpVEStorageType_Object = MibTableColumn
vplsBgpVEStorageType = _VplsBgpVEStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 2, 1, 6),
    _VplsBgpVEStorageType_Type()
)
vplsBgpVEStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVEStorageType.setStatus("current")
_VplsBgpPwBindTable_Object = MibTable
vplsBgpPwBindTable = _VplsBgpPwBindTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 3)
)
if mibBuilder.loadTexts:
    vplsBgpPwBindTable.setStatus("current")
_VplsBgpPwBindEntry_Object = MibTableRow
vplsBgpPwBindEntry = _VplsBgpPwBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 3, 1)
)
vplsBgpPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpPwBindEntry.setStatus("current")


class _VplsBgpPwBindLocalVEId_Type(Unsigned32):
    """Custom type vplsBgpPwBindLocalVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VplsBgpPwBindLocalVEId_Type.__name__ = "Unsigned32"
_VplsBgpPwBindLocalVEId_Object = MibTableColumn
vplsBgpPwBindLocalVEId = _VplsBgpPwBindLocalVEId_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 3, 1, 1),
    _VplsBgpPwBindLocalVEId_Type()
)
vplsBgpPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsBgpPwBindLocalVEId.setStatus("current")


class _VplsBgpPwBindRemoteVEId_Type(Unsigned32):
    """Custom type vplsBgpPwBindRemoteVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VplsBgpPwBindRemoteVEId_Type.__name__ = "Unsigned32"
_VplsBgpPwBindRemoteVEId_Object = MibTableColumn
vplsBgpPwBindRemoteVEId = _VplsBgpPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 2, 1, 10, 276, 1, 3, 1, 2),
    _VplsBgpPwBindRemoteVEId_Type()
)
vplsBgpPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsBgpPwBindRemoteVEId.setStatus("current")
_VplsBgpConformance_ObjectIdentity = ObjectIdentity
vplsBgpConformance = _VplsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 276, 2)
)
_VplsBgpCompliances_ObjectIdentity = ObjectIdentity
vplsBgpCompliances = _VplsBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 1)
)
_VplsBgpGroups_ObjectIdentity = ObjectIdentity
vplsBgpGroups = _VplsBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 2)
)

# Managed Objects groups

vplsBgpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 2, 1)
)
vplsBgpConfigGroup.setObjects(
    ("VPLS-BGP-MIB", "vplsBgpConfigVERangeSize")
)
if mibBuilder.loadTexts:
    vplsBgpConfigGroup.setStatus("current")

vplsBgpVEGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 2, 2)
)
vplsBgpVEGroup.setObjects(
      *(("VPLS-BGP-MIB", "vplsBgpVEName"),
        ("VPLS-BGP-MIB", "vplsBgpVEPreference"),
        ("VPLS-BGP-MIB", "vplsBgpVERowStatus"),
        ("VPLS-BGP-MIB", "vplsBgpVEStorageType"))
)
if mibBuilder.loadTexts:
    vplsBgpVEGroup.setStatus("current")

vplsBgpPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 2, 3)
)
vplsBgpPwBindGroup.setObjects(
      *(("VPLS-BGP-MIB", "vplsBgpPwBindLocalVEId"),
        ("VPLS-BGP-MIB", "vplsBgpPwBindRemoteVEId"))
)
if mibBuilder.loadTexts:
    vplsBgpPwBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vplsBgpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vplsBgpModuleFullCompliance.setStatus(
        "current"
    )

vplsBgpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 276, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vplsBgpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-BGP-MIB",
    **{"vplsBgpMIB": vplsBgpMIB,
       "vplsBgpObjects": vplsBgpObjects,
       "vplsBgpConfigTable": vplsBgpConfigTable,
       "vplsBgpConfigEntry": vplsBgpConfigEntry,
       "vplsBgpConfigVERangeSize": vplsBgpConfigVERangeSize,
       "vplsBgpVETable": vplsBgpVETable,
       "vplsBgpVEEntry": vplsBgpVEEntry,
       "vplsBgpVEId": vplsBgpVEId,
       "vplsBgpVEName": vplsBgpVEName,
       "vplsBgpVEPreference": vplsBgpVEPreference,
       "vplsBgpVERowStatus": vplsBgpVERowStatus,
       "vplsBgpVEStorageType": vplsBgpVEStorageType,
       "vplsBgpPwBindTable": vplsBgpPwBindTable,
       "vplsBgpPwBindEntry": vplsBgpPwBindEntry,
       "vplsBgpPwBindLocalVEId": vplsBgpPwBindLocalVEId,
       "vplsBgpPwBindRemoteVEId": vplsBgpPwBindRemoteVEId,
       "vplsBgpConformance": vplsBgpConformance,
       "vplsBgpCompliances": vplsBgpCompliances,
       "vplsBgpModuleFullCompliance": vplsBgpModuleFullCompliance,
       "vplsBgpModuleReadOnlyCompliance": vplsBgpModuleReadOnlyCompliance,
       "vplsBgpGroups": vplsBgpGroups,
       "vplsBgpConfigGroup": vplsBgpConfigGroup,
       "vplsBgpVEGroup": vplsBgpVEGroup,
       "vplsBgpPwBindGroup": vplsBgpPwBindGroup}
)
