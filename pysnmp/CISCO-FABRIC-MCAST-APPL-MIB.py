# SNMP MIB module (CISCO-FABRIC-MCAST-APPL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FABRIC-MCAST-APPL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:07 2024
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

(CfmPoolIndex,) = mibBuilder.importSymbols(
    "CISCO-FABRIC-MCAST-MIB",
    "CfmPoolIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entLogicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLogicalIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFabricMcastApplMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256)
)
ciscoFabricMcastApplMIB.setRevisions(
        ("2002-12-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFabricMcastApplMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFabricMcastApplMIBObjects = _CiscoFabricMcastApplMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1)
)
_CfmaAppl_ObjectIdentity = ObjectIdentity
cfmaAppl = _CfmaAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1)
)
_CfmaApplTable_Object = MibTable
cfmaApplTable = _CfmaApplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmaApplTable.setStatus("current")
_CfmaApplEntry_Object = MibTableRow
cfmaApplEntry = _CfmaApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1, 1)
)
cfmaApplEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "CISCO-FABRIC-MCAST-APPL-MIB", "cfmaApplId"),
)
if mibBuilder.loadTexts:
    cfmaApplEntry.setStatus("current")
_CfmaApplId_Type = Unsigned32
_CfmaApplId_Object = MibTableColumn
cfmaApplId = _CfmaApplId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1, 1, 1),
    _CfmaApplId_Type()
)
cfmaApplId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmaApplId.setStatus("current")


class _CfmaApplName_Type(SnmpAdminString):
    """Custom type cfmaApplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfmaApplName_Type.__name__ = "SnmpAdminString"
_CfmaApplName_Object = MibTableColumn
cfmaApplName = _CfmaApplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1, 1, 2),
    _CfmaApplName_Type()
)
cfmaApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmaApplName.setStatus("current")
_CfmaApplInuseFgids_Type = Gauge32
_CfmaApplInuseFgids_Object = MibTableColumn
cfmaApplInuseFgids = _CfmaApplInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1, 1, 3),
    _CfmaApplInuseFgids_Type()
)
cfmaApplInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmaApplInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmaApplInuseFgids.setUnits("fgid")
_CfmaApplHighWaterInuseFGIDs_Type = Gauge32
_CfmaApplHighWaterInuseFGIDs_Object = MibTableColumn
cfmaApplHighWaterInuseFGIDs = _CfmaApplHighWaterInuseFGIDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1, 1, 4),
    _CfmaApplHighWaterInuseFGIDs_Type()
)
cfmaApplHighWaterInuseFGIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmaApplHighWaterInuseFGIDs.setStatus("current")
if mibBuilder.loadTexts:
    cfmaApplHighWaterInuseFGIDs.setUnits("fgid")
_CfmaApplPoolId_Type = CfmPoolIndex
_CfmaApplPoolId_Object = MibTableColumn
cfmaApplPoolId = _CfmaApplPoolId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 1, 1, 1, 1, 5),
    _CfmaApplPoolId_Type()
)
cfmaApplPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmaApplPoolId.setStatus("current")
_CfmaMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cfmaMIBNotificationPrefix = _CfmaMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 2)
)
_CfmaMIBNotifications_ObjectIdentity = ObjectIdentity
cfmaMIBNotifications = _CfmaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 2, 0)
)
_CfmaMIBConformance_ObjectIdentity = ObjectIdentity
cfmaMIBConformance = _CfmaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 3)
)
_CfmaMIBCompliances_ObjectIdentity = ObjectIdentity
cfmaMIBCompliances = _CfmaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 3, 1)
)
_CfmaMIBGroups_ObjectIdentity = ObjectIdentity
cfmaMIBGroups = _CfmaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 3, 2)
)

# Managed Objects groups

cfmaApplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 3, 2, 1)
)
cfmaApplGroup.setObjects(
      *(("CISCO-FABRIC-MCAST-APPL-MIB", "cfmaApplName"),
        ("CISCO-FABRIC-MCAST-APPL-MIB", "cfmaApplInuseFgids"),
        ("CISCO-FABRIC-MCAST-APPL-MIB", "cfmaApplHighWaterInuseFGIDs"),
        ("CISCO-FABRIC-MCAST-APPL-MIB", "cfmaApplPoolId"))
)
if mibBuilder.loadTexts:
    cfmaApplGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfmaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 256, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfmaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FABRIC-MCAST-APPL-MIB",
    **{"ciscoFabricMcastApplMIB": ciscoFabricMcastApplMIB,
       "ciscoFabricMcastApplMIBObjects": ciscoFabricMcastApplMIBObjects,
       "cfmaAppl": cfmaAppl,
       "cfmaApplTable": cfmaApplTable,
       "cfmaApplEntry": cfmaApplEntry,
       "cfmaApplId": cfmaApplId,
       "cfmaApplName": cfmaApplName,
       "cfmaApplInuseFgids": cfmaApplInuseFgids,
       "cfmaApplHighWaterInuseFGIDs": cfmaApplHighWaterInuseFGIDs,
       "cfmaApplPoolId": cfmaApplPoolId,
       "cfmaMIBNotificationPrefix": cfmaMIBNotificationPrefix,
       "cfmaMIBNotifications": cfmaMIBNotifications,
       "cfmaMIBConformance": cfmaMIBConformance,
       "cfmaMIBCompliances": cfmaMIBCompliances,
       "cfmaMIBCompliance": cfmaMIBCompliance,
       "cfmaMIBGroups": cfmaMIBGroups,
       "cfmaApplGroup": cfmaApplGroup}
)
