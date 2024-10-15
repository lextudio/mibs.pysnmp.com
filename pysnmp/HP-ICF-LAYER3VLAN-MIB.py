# SNMP MIB module (HP-ICF-LAYER3VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-LAYER3VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hpicfLayer3VlanConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70)
)
hpicfLayer3VlanConfigMIB.setRevisions(
        ("2010-03-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfLayer3VlanConfig_ObjectIdentity = ObjectIdentity
hpicfLayer3VlanConfig = _HpicfLayer3VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1)
)
_HpicfLayer3VlanConfigTable_Object = MibTable
hpicfLayer3VlanConfigTable = _HpicfLayer3VlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfLayer3VlanConfigTable.setStatus("current")
_HpicfLayer3VlanConfigEntry_Object = MibTableRow
hpicfLayer3VlanConfigEntry = _HpicfLayer3VlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1)
)
hpicfLayer3VlanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfLayer3VlanConfigEntry.setStatus("current")


class _HpicfLayer3VlanStatus_Type(Integer32):
    """Custom type hpicfLayer3VlanStatus based on Integer32"""
    defaultValue = 1

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


_HpicfLayer3VlanStatus_Type.__name__ = "Integer32"
_HpicfLayer3VlanStatus_Object = MibTableColumn
hpicfLayer3VlanStatus = _HpicfLayer3VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1, 1),
    _HpicfLayer3VlanStatus_Type()
)
hpicfLayer3VlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLayer3VlanStatus.setStatus("current")
_HpicfLayer3VlanConfigConformance_ObjectIdentity = ObjectIdentity
hpicfLayer3VlanConfigConformance = _HpicfLayer3VlanConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2)
)
_HpicfL3VlanConfigMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfL3VlanConfigMIBCompliances = _HpicfL3VlanConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1)
)
_HpicfLayer3VlanConfigMIBGroups_ObjectIdentity = ObjectIdentity
hpicfLayer3VlanConfigMIBGroups = _HpicfLayer3VlanConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2)
)

# Managed Objects groups

hpicfLayer3VlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2, 1)
)
hpicfLayer3VlanConfigGroup.setObjects(
    ("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanStatus")
)
if mibBuilder.loadTexts:
    hpicfLayer3VlanConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfL3VlanConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfL3VlanConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-LAYER3VLAN-MIB",
    **{"hpicfLayer3VlanConfigMIB": hpicfLayer3VlanConfigMIB,
       "hpicfLayer3VlanConfig": hpicfLayer3VlanConfig,
       "hpicfLayer3VlanConfigTable": hpicfLayer3VlanConfigTable,
       "hpicfLayer3VlanConfigEntry": hpicfLayer3VlanConfigEntry,
       "hpicfLayer3VlanStatus": hpicfLayer3VlanStatus,
       "hpicfLayer3VlanConfigConformance": hpicfLayer3VlanConfigConformance,
       "hpicfL3VlanConfigMIBCompliances": hpicfL3VlanConfigMIBCompliances,
       "hpicfL3VlanConfigMIBCompliance": hpicfL3VlanConfigMIBCompliance,
       "hpicfLayer3VlanConfigMIBGroups": hpicfLayer3VlanConfigMIBGroups,
       "hpicfLayer3VlanConfigGroup": hpicfLayer3VlanConfigGroup}
)
