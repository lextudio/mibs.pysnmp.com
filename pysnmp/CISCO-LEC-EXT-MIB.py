# SNMP MIB module (CISCO-LEC-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LEC-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:56 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(lecConfigEntry,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "lecConfigEntry")

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

ciscoLecExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77)
)
ciscoLecExtMIB.setRevisions(
        ("1997-05-09 12:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLecExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLecExtMIBObjects = _CiscoLecExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 1)
)
_CLecExtVlan_ObjectIdentity = ObjectIdentity
cLecExtVlan = _CLecExtVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1)
)
_CLecToVlanTable_Object = MibTable
cLecToVlanTable = _CLecToVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLecToVlanTable.setStatus("current")
_CLecToVlanEntry_Object = MibTableRow
cLecToVlanEntry = _CLecToVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLecToVlanEntry.setStatus("current")
_CLecToVlanId_Type = VlanIndex
_CLecToVlanId_Object = MibTableColumn
cLecToVlanId = _CLecToVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1, 1),
    _CLecToVlanId_Type()
)
cLecToVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLecToVlanId.setStatus("current")
_CiscoLecExtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoLecExtMIBNotificationPrefix = _CiscoLecExtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 2)
)
_CiscoLecExtMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoLecExtMIBNotifications = _CiscoLecExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 2, 0)
)
_CiscoLecExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoLecExtMIBConformance = _CiscoLecExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 3)
)
_CiscoLecExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLecExtMIBCompliances = _CiscoLecExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1)
)
_CiscoLecExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLecExtMIBGroups = _CiscoLecExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2)
)
lecConfigEntry.registerAugmentions(
    ("CISCO-LEC-EXT-MIB",
     "cLecToVlanEntry")
)
cLecToVlanEntry.setIndexNames(*lecConfigEntry.getIndexNames())

# Managed Objects groups

ciscoLecExtVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2, 1)
)
ciscoLecExtVlanMIBGroup.setObjects(
    ("CISCO-LEC-EXT-MIB", "cLecToVlanId")
)
if mibBuilder.loadTexts:
    ciscoLecExtVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLecExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLecExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LEC-EXT-MIB",
    **{"ciscoLecExtMIB": ciscoLecExtMIB,
       "ciscoLecExtMIBObjects": ciscoLecExtMIBObjects,
       "cLecExtVlan": cLecExtVlan,
       "cLecToVlanTable": cLecToVlanTable,
       "cLecToVlanEntry": cLecToVlanEntry,
       "cLecToVlanId": cLecToVlanId,
       "ciscoLecExtMIBNotificationPrefix": ciscoLecExtMIBNotificationPrefix,
       "ciscoLecExtMIBNotifications": ciscoLecExtMIBNotifications,
       "ciscoLecExtMIBConformance": ciscoLecExtMIBConformance,
       "ciscoLecExtMIBCompliances": ciscoLecExtMIBCompliances,
       "ciscoLecExtMIBCompliance": ciscoLecExtMIBCompliance,
       "ciscoLecExtMIBGroups": ciscoLecExtMIBGroups,
       "ciscoLecExtVlanMIBGroup": ciscoLecExtVlanMIBGroup}
)
