# SNMP MIB module (HP-ICF-GENERIC-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-GENERIC-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:28 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VlanId,
 dot1qTpFdbEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "dot1qTpFdbEntry")

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

hpicfGenericVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67)
)
hpicfGenericVlanMIB.setRevisions(
        ("2017-06-28 00:00",
         "2010-02-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfGenericVlanFeaturesObjects_ObjectIdentity = ObjectIdentity
hpicfGenericVlanFeaturesObjects = _HpicfGenericVlanFeaturesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1)
)
_HpicfGenericVlanFeaturesTable_Object = MibTable
hpicfGenericVlanFeaturesTable = _HpicfGenericVlanFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfGenericVlanFeaturesTable.setStatus("current")
_HpicfGenericVlanFeaturesEntry_Object = MibTableRow
hpicfGenericVlanFeaturesEntry = _HpicfGenericVlanFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfGenericVlanFeaturesEntry.setStatus("current")


class _HpicfMacNotifyClearVlanControl_Type(Integer32):
    """Custom type hpicfMacNotifyClearVlanControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macNotifyClearVlan", 2),
          ("noOperation", 1))
    )


_HpicfMacNotifyClearVlanControl_Type.__name__ = "Integer32"
_HpicfMacNotifyClearVlanControl_Object = MibTableColumn
hpicfMacNotifyClearVlanControl = _HpicfMacNotifyClearVlanControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 1),
    _HpicfMacNotifyClearVlanControl_Type()
)
hpicfMacNotifyClearVlanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyClearVlanControl.setStatus("current")
_HpicfDot1qTpFdbVlanId_Type = VlanId
_HpicfDot1qTpFdbVlanId_Object = MibTableColumn
hpicfDot1qTpFdbVlanId = _HpicfDot1qTpFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 2),
    _HpicfDot1qTpFdbVlanId_Type()
)
hpicfDot1qTpFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1qTpFdbVlanId.setStatus("current")
_HpicfDot1qTpFdbInstalledTime_Type = TimeTicks
_HpicfDot1qTpFdbInstalledTime_Object = MibTableColumn
hpicfDot1qTpFdbInstalledTime = _HpicfDot1qTpFdbInstalledTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 3),
    _HpicfDot1qTpFdbInstalledTime_Type()
)
hpicfDot1qTpFdbInstalledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDot1qTpFdbInstalledTime.setStatus("current")
_HpicfGenericVlanFeaturesConformance_ObjectIdentity = ObjectIdentity
hpicfGenericVlanFeaturesConformance = _HpicfGenericVlanFeaturesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2)
)
_HpicfGenericVlanFeaturesCompliances_ObjectIdentity = ObjectIdentity
hpicfGenericVlanFeaturesCompliances = _HpicfGenericVlanFeaturesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1)
)
_HpicfGenericVlanFeaturesGroups_ObjectIdentity = ObjectIdentity
hpicfGenericVlanFeaturesGroups = _HpicfGenericVlanFeaturesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2)
)
dot1qTpFdbEntry.registerAugmentions(
    ("HP-ICF-GENERIC-VLAN-MIB",
     "hpicfGenericVlanFeaturesEntry")
)
hpicfGenericVlanFeaturesEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())

# Managed Objects groups

hpicfGenericVlanFeaturesConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 2)
)
hpicfGenericVlanFeaturesConfigGroup.setObjects(
      *(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"),
        ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"))
)
if mibBuilder.loadTexts:
    hpicfGenericVlanFeaturesConfigGroup.setStatus("deprecated")

hpicfGenericVlanFeaturesConfGrp1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 3)
)
hpicfGenericVlanFeaturesConfGrp1.setObjects(
      *(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"),
        ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"),
        ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbInstalledTime"))
)
if mibBuilder.loadTexts:
    hpicfGenericVlanFeaturesConfGrp1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfGenericVlanFeaturesCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfGenericVlanFeaturesCompliance.setStatus(
        "deprecated"
    )

hpicfGenericVlanFeaturesComp1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfGenericVlanFeaturesComp1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-GENERIC-VLAN-MIB",
    **{"hpicfGenericVlanMIB": hpicfGenericVlanMIB,
       "hpicfGenericVlanFeaturesObjects": hpicfGenericVlanFeaturesObjects,
       "hpicfGenericVlanFeaturesTable": hpicfGenericVlanFeaturesTable,
       "hpicfGenericVlanFeaturesEntry": hpicfGenericVlanFeaturesEntry,
       "hpicfMacNotifyClearVlanControl": hpicfMacNotifyClearVlanControl,
       "hpicfDot1qTpFdbVlanId": hpicfDot1qTpFdbVlanId,
       "hpicfDot1qTpFdbInstalledTime": hpicfDot1qTpFdbInstalledTime,
       "hpicfGenericVlanFeaturesConformance": hpicfGenericVlanFeaturesConformance,
       "hpicfGenericVlanFeaturesCompliances": hpicfGenericVlanFeaturesCompliances,
       "hpicfGenericVlanFeaturesCompliance": hpicfGenericVlanFeaturesCompliance,
       "hpicfGenericVlanFeaturesComp1": hpicfGenericVlanFeaturesComp1,
       "hpicfGenericVlanFeaturesGroups": hpicfGenericVlanFeaturesGroups,
       "hpicfGenericVlanFeaturesConfigGroup": hpicfGenericVlanFeaturesConfigGroup,
       "hpicfGenericVlanFeaturesConfGrp1": hpicfGenericVlanFeaturesConfGrp1}
)
