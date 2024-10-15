# SNMP MIB module (CISCO-DIAMETER-SG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DIAMETER-SG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:03 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDiameterSGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132)
)
ciscoDiameterSGMIB.setRevisions(
        ("2006-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDiameterSGMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDiameterSGMIBNotifs = _CiscoDiameterSGMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 0)
)
_CiscoDiameterSGMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDiameterSGMIBObjects = _CiscoDiameterSGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1)
)
_CdsgHostCfgs_ObjectIdentity = ObjectIdentity
cdsgHostCfgs = _CdsgHostCfgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1)
)
_CdsgServerGroupTable_Object = MibTable
cdsgServerGroupTable = _CdsgServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdsgServerGroupTable.setStatus("current")
_CdsgServerGroupEntry_Object = MibTableRow
cdsgServerGroupEntry = _CdsgServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1)
)
cdsgServerGroupEntry.setIndexNames(
    (0, "CISCO-DIAMETER-SG-MIB", "cdsgServerGroupIndex"),
)
if mibBuilder.loadTexts:
    cdsgServerGroupEntry.setStatus("current")


class _CdsgServerGroupIndex_Type(Unsigned32):
    """Custom type cdsgServerGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdsgServerGroupIndex_Type.__name__ = "Unsigned32"
_CdsgServerGroupIndex_Object = MibTableColumn
cdsgServerGroupIndex = _CdsgServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 1),
    _CdsgServerGroupIndex_Type()
)
cdsgServerGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsgServerGroupIndex.setStatus("current")
_CdsgServerGroupName_Type = SnmpAdminString
_CdsgServerGroupName_Object = MibTableColumn
cdsgServerGroupName = _CdsgServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 2),
    _CdsgServerGroupName_Type()
)
cdsgServerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsgServerGroupName.setStatus("current")


class _CdsgServerGroupStorageType_Type(StorageType):
    """Custom type cdsgServerGroupStorageType based on StorageType"""


_CdsgServerGroupStorageType_Object = MibTableColumn
cdsgServerGroupStorageType = _CdsgServerGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 3),
    _CdsgServerGroupStorageType_Type()
)
cdsgServerGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsgServerGroupStorageType.setStatus("current")
_CdsgServerGroupRowStatus_Type = RowStatus
_CdsgServerGroupRowStatus_Object = MibTableColumn
cdsgServerGroupRowStatus = _CdsgServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 4),
    _CdsgServerGroupRowStatus_Type()
)
cdsgServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsgServerGroupRowStatus.setStatus("current")
_CdsgServerTable_Object = MibTable
cdsgServerTable = _CdsgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdsgServerTable.setStatus("current")
_CdsgServerEntry_Object = MibTableRow
cdsgServerEntry = _CdsgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1)
)
cdsgServerEntry.setIndexNames(
    (0, "CISCO-DIAMETER-SG-MIB", "cdsgServerGroupIndex"),
    (0, "CISCO-DIAMETER-SG-MIB", "cdsgServerIndex"),
)
if mibBuilder.loadTexts:
    cdsgServerEntry.setStatus("current")


class _CdsgServerIndex_Type(Unsigned32):
    """Custom type cdsgServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdsgServerIndex_Type.__name__ = "Unsigned32"
_CdsgServerIndex_Object = MibTableColumn
cdsgServerIndex = _CdsgServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 1),
    _CdsgServerIndex_Type()
)
cdsgServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsgServerIndex.setStatus("current")
_CdsgServerName_Type = SnmpAdminString
_CdsgServerName_Object = MibTableColumn
cdsgServerName = _CdsgServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 2),
    _CdsgServerName_Type()
)
cdsgServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsgServerName.setStatus("current")


class _CdsgServerStorageType_Type(StorageType):
    """Custom type cdsgServerStorageType based on StorageType"""


_CdsgServerStorageType_Object = MibTableColumn
cdsgServerStorageType = _CdsgServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 3),
    _CdsgServerStorageType_Type()
)
cdsgServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsgServerStorageType.setStatus("current")
_CdsgServerRowStatus_Type = RowStatus
_CdsgServerRowStatus_Object = MibTableColumn
cdsgServerRowStatus = _CdsgServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 4),
    _CdsgServerRowStatus_Type()
)
cdsgServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsgServerRowStatus.setStatus("current")
_CiscoDiameterSGMIBConform_ObjectIdentity = ObjectIdentity
ciscoDiameterSGMIBConform = _CiscoDiameterSGMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 2)
)
_CiscoDiameterSGMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDiameterSGMIBCompliances = _CiscoDiameterSGMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 1)
)
_CiscoDiameterSGMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDiameterSGMIBGroups = _CiscoDiameterSGMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 2)
)

# Managed Objects groups

ciscoDiameterSGHostCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 2, 1)
)
ciscoDiameterSGHostCfgGroup.setObjects(
      *(("CISCO-DIAMETER-SG-MIB", "cdsgServerGroupName"),
        ("CISCO-DIAMETER-SG-MIB", "cdsgServerGroupRowStatus"),
        ("CISCO-DIAMETER-SG-MIB", "cdsgServerGroupStorageType"),
        ("CISCO-DIAMETER-SG-MIB", "cdsgServerName"),
        ("CISCO-DIAMETER-SG-MIB", "cdsgServerRowStatus"),
        ("CISCO-DIAMETER-SG-MIB", "cdsgServerStorageType"))
)
if mibBuilder.loadTexts:
    ciscoDiameterSGHostCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDiameterSGMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDiameterSGMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIAMETER-SG-MIB",
    **{"ciscoDiameterSGMIB": ciscoDiameterSGMIB,
       "ciscoDiameterSGMIBNotifs": ciscoDiameterSGMIBNotifs,
       "ciscoDiameterSGMIBObjects": ciscoDiameterSGMIBObjects,
       "cdsgHostCfgs": cdsgHostCfgs,
       "cdsgServerGroupTable": cdsgServerGroupTable,
       "cdsgServerGroupEntry": cdsgServerGroupEntry,
       "cdsgServerGroupIndex": cdsgServerGroupIndex,
       "cdsgServerGroupName": cdsgServerGroupName,
       "cdsgServerGroupStorageType": cdsgServerGroupStorageType,
       "cdsgServerGroupRowStatus": cdsgServerGroupRowStatus,
       "cdsgServerTable": cdsgServerTable,
       "cdsgServerEntry": cdsgServerEntry,
       "cdsgServerIndex": cdsgServerIndex,
       "cdsgServerName": cdsgServerName,
       "cdsgServerStorageType": cdsgServerStorageType,
       "cdsgServerRowStatus": cdsgServerRowStatus,
       "ciscoDiameterSGMIBConform": ciscoDiameterSGMIBConform,
       "ciscoDiameterSGMIBCompliances": ciscoDiameterSGMIBCompliances,
       "ciscoDiameterSGMIBCompliance": ciscoDiameterSGMIBCompliance,
       "ciscoDiameterSGMIBGroups": ciscoDiameterSGMIBGroups,
       "ciscoDiameterSGHostCfgGroup": ciscoDiameterSGHostCfgGroup}
)
