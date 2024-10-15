# SNMP MIB module (HP-ICF-ISOLATED-PORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-ISOLATED-PORTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:39 2024
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

(PortList,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qVlanStaticEntry")

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

hpicfDot1qIsolatedPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109)
)
hpicfDot1qIsolatedPorts.setRevisions(
        ("2014-04-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDot1qIsolatedPortConfigurationObjects_ObjectIdentity = ObjectIdentity
hpicfDot1qIsolatedPortConfigurationObjects = _HpicfDot1qIsolatedPortConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1)
)
_HpicfDot1qIsolatedPortsTable_Object = MibTable
hpicfDot1qIsolatedPortsTable = _HpicfDot1qIsolatedPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1qIsolatedPortsTable.setStatus("current")
_HpicfDot1qIsolatedPortsEntry_Object = MibTableRow
hpicfDot1qIsolatedPortsEntry = _HpicfDot1qIsolatedPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1qIsolatedPortsEntry.setStatus("current")
_HpicfDot1qVlanStaticIsolatedPorts_Type = PortList
_HpicfDot1qVlanStaticIsolatedPorts_Object = MibTableColumn
hpicfDot1qVlanStaticIsolatedPorts = _HpicfDot1qVlanStaticIsolatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1, 1),
    _HpicfDot1qVlanStaticIsolatedPorts_Type()
)
hpicfDot1qVlanStaticIsolatedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDot1qVlanStaticIsolatedPorts.setStatus("current")
_HpicfDot1qIsolatedPortConformance_ObjectIdentity = ObjectIdentity
hpicfDot1qIsolatedPortConformance = _HpicfDot1qIsolatedPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2)
)
_HpicfDot1qIsolatedPortCompliances_ObjectIdentity = ObjectIdentity
hpicfDot1qIsolatedPortCompliances = _HpicfDot1qIsolatedPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1)
)
_HpicfDot1qIsolatedPortGroups_ObjectIdentity = ObjectIdentity
hpicfDot1qIsolatedPortGroups = _HpicfDot1qIsolatedPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2)
)
dot1qVlanStaticEntry.registerAugmentions(
    ("HP-ICF-ISOLATED-PORTS-MIB",
     "hpicfDot1qIsolatedPortsEntry")
)
hpicfDot1qIsolatedPortsEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

hpicfDot1qIsolatedPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2, 1)
)
hpicfDot1qIsolatedPortGroup.setObjects(
    ("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qVlanStaticIsolatedPorts")
)
if mibBuilder.loadTexts:
    hpicfDot1qIsolatedPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDot1qIsolatedPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDot1qIsolatedPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-ISOLATED-PORTS-MIB",
    **{"hpicfDot1qIsolatedPorts": hpicfDot1qIsolatedPorts,
       "hpicfDot1qIsolatedPortConfigurationObjects": hpicfDot1qIsolatedPortConfigurationObjects,
       "hpicfDot1qIsolatedPortsTable": hpicfDot1qIsolatedPortsTable,
       "hpicfDot1qIsolatedPortsEntry": hpicfDot1qIsolatedPortsEntry,
       "hpicfDot1qVlanStaticIsolatedPorts": hpicfDot1qVlanStaticIsolatedPorts,
       "hpicfDot1qIsolatedPortConformance": hpicfDot1qIsolatedPortConformance,
       "hpicfDot1qIsolatedPortCompliances": hpicfDot1qIsolatedPortCompliances,
       "hpicfDot1qIsolatedPortCompliance": hpicfDot1qIsolatedPortCompliance,
       "hpicfDot1qIsolatedPortGroups": hpicfDot1qIsolatedPortGroups,
       "hpicfDot1qIsolatedPortGroup": hpicfDot1qIsolatedPortGroup}
)
