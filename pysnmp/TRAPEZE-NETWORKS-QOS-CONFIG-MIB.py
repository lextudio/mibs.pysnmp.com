# SNMP MIB module (TRAPEZE-NETWORKS-QOS-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-QOS-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:34 2024
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

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzQosConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20)
)
trpzQosConfigMib.setRevisions(
        ("2011-02-24 00:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzQosConfigMibObjects_ObjectIdentity = ObjectIdentity
trpzQosConfigMibObjects = _TrpzQosConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 1)
)
_TrpzQosConfQosProfileConfigTable_Object = MibTable
trpzQosConfQosProfileConfigTable = _TrpzQosConfQosProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1)
)
if mibBuilder.loadTexts:
    trpzQosConfQosProfileConfigTable.setStatus("current")
_TrpzQosConfQosProfileConfigEntry_Object = MibTableRow
trpzQosConfQosProfileConfigEntry = _TrpzQosConfQosProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1)
)
trpzQosConfQosProfileConfigEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfProfileName"),
)
if mibBuilder.loadTexts:
    trpzQosConfQosProfileConfigEntry.setStatus("current")


class _TrpzQosConfQosProfConfProfileName_Type(OctetString):
    """Custom type trpzQosConfQosProfConfProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrpzQosConfQosProfConfProfileName_Type.__name__ = "OctetString"
_TrpzQosConfQosProfConfProfileName_Object = MibTableColumn
trpzQosConfQosProfConfProfileName = _TrpzQosConfQosProfConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 1),
    _TrpzQosConfQosProfConfProfileName_Type()
)
trpzQosConfQosProfConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzQosConfQosProfConfProfileName.setStatus("current")
_TrpzQosConfQosProfConfMaxBandwidthKbps_Type = Unsigned32
_TrpzQosConfQosProfConfMaxBandwidthKbps_Object = MibTableColumn
trpzQosConfQosProfConfMaxBandwidthKbps = _TrpzQosConfQosProfConfMaxBandwidthKbps_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 2),
    _TrpzQosConfQosProfConfMaxBandwidthKbps_Type()
)
trpzQosConfQosProfConfMaxBandwidthKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trpzQosConfQosProfConfMaxBandwidthKbps.setStatus("current")
_TrpzQosConfigConformance_ObjectIdentity = ObjectIdentity
trpzQosConfigConformance = _TrpzQosConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 2)
)
_TrpzQosConfigCompliances_ObjectIdentity = ObjectIdentity
trpzQosConfigCompliances = _TrpzQosConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1)
)
_TrpzQosConfigGroups_ObjectIdentity = ObjectIdentity
trpzQosConfigGroups = _TrpzQosConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2)
)

# Managed Objects groups

trpzQosConfQosProfileConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2, 1)
)
trpzQosConfQosProfileConfigGroup.setObjects(
    ("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfMaxBandwidthKbps")
)
if mibBuilder.loadTexts:
    trpzQosConfQosProfileConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzQosConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzQosConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-QOS-CONFIG-MIB",
    **{"trpzQosConfigMib": trpzQosConfigMib,
       "trpzQosConfigMibObjects": trpzQosConfigMibObjects,
       "trpzQosConfQosProfileConfigTable": trpzQosConfQosProfileConfigTable,
       "trpzQosConfQosProfileConfigEntry": trpzQosConfQosProfileConfigEntry,
       "trpzQosConfQosProfConfProfileName": trpzQosConfQosProfConfProfileName,
       "trpzQosConfQosProfConfMaxBandwidthKbps": trpzQosConfQosProfConfMaxBandwidthKbps,
       "trpzQosConfigConformance": trpzQosConfigConformance,
       "trpzQosConfigCompliances": trpzQosConfigCompliances,
       "trpzQosConfigCompliance": trpzQosConfigCompliance,
       "trpzQosConfigGroups": trpzQosConfigGroups,
       "trpzQosConfQosProfileConfigGroup": trpzQosConfQosProfileConfigGroup}
)
