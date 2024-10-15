# SNMP MIB module (SNMP-TSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-TSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:06 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

snmpTsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 190)
)
snmpTsmMIB.setRevisions(
        ("2009-06-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpTsmNotifications_ObjectIdentity = ObjectIdentity
snmpTsmNotifications = _SnmpTsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 0)
)
_SnmpTsmMIBObjects_ObjectIdentity = ObjectIdentity
snmpTsmMIBObjects = _SnmpTsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 1)
)
_SnmpTsmStats_ObjectIdentity = ObjectIdentity
snmpTsmStats = _SnmpTsmStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 1, 1)
)
_SnmpTsmInvalidCaches_Type = Counter32
_SnmpTsmInvalidCaches_Object = MibScalar
snmpTsmInvalidCaches = _SnmpTsmInvalidCaches_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 1),
    _SnmpTsmInvalidCaches_Type()
)
snmpTsmInvalidCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmInvalidCaches.setStatus("current")
_SnmpTsmInadequateSecurityLevels_Type = Counter32
_SnmpTsmInadequateSecurityLevels_Object = MibScalar
snmpTsmInadequateSecurityLevels = _SnmpTsmInadequateSecurityLevels_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 2),
    _SnmpTsmInadequateSecurityLevels_Type()
)
snmpTsmInadequateSecurityLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmInadequateSecurityLevels.setStatus("current")
_SnmpTsmUnknownPrefixes_Type = Counter32
_SnmpTsmUnknownPrefixes_Object = MibScalar
snmpTsmUnknownPrefixes = _SnmpTsmUnknownPrefixes_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 3),
    _SnmpTsmUnknownPrefixes_Type()
)
snmpTsmUnknownPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmUnknownPrefixes.setStatus("current")
_SnmpTsmInvalidPrefixes_Type = Counter32
_SnmpTsmInvalidPrefixes_Object = MibScalar
snmpTsmInvalidPrefixes = _SnmpTsmInvalidPrefixes_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 4),
    _SnmpTsmInvalidPrefixes_Type()
)
snmpTsmInvalidPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmInvalidPrefixes.setStatus("current")
_SnmpTsmConfiguration_ObjectIdentity = ObjectIdentity
snmpTsmConfiguration = _SnmpTsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 1, 2)
)


class _SnmpTsmConfigurationUsePrefix_Type(TruthValue):
    """Custom type snmpTsmConfigurationUsePrefix based on TruthValue"""


_SnmpTsmConfigurationUsePrefix_Object = MibScalar
snmpTsmConfigurationUsePrefix = _SnmpTsmConfigurationUsePrefix_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 2, 1),
    _SnmpTsmConfigurationUsePrefix_Type()
)
snmpTsmConfigurationUsePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTsmConfigurationUsePrefix.setStatus("current")
_SnmpTsmConformance_ObjectIdentity = ObjectIdentity
snmpTsmConformance = _SnmpTsmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 2)
)
_SnmpTsmCompliances_ObjectIdentity = ObjectIdentity
snmpTsmCompliances = _SnmpTsmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 2, 1)
)
_SnmpTsmGroups_ObjectIdentity = ObjectIdentity
snmpTsmGroups = _SnmpTsmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 2, 2)
)

# Managed Objects groups

snmpTsmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 190, 2, 2, 2)
)
snmpTsmGroup.setObjects(
      *(("SNMP-TSM-MIB", "snmpTsmInvalidCaches"),
        ("SNMP-TSM-MIB", "snmpTsmInadequateSecurityLevels"),
        ("SNMP-TSM-MIB", "snmpTsmUnknownPrefixes"),
        ("SNMP-TSM-MIB", "snmpTsmInvalidPrefixes"),
        ("SNMP-TSM-MIB", "snmpTsmConfigurationUsePrefix"))
)
if mibBuilder.loadTexts:
    snmpTsmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpTsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 190, 2, 1, 1)
)
if mibBuilder.loadTexts:
    snmpTsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-TSM-MIB",
    **{"snmpTsmMIB": snmpTsmMIB,
       "snmpTsmNotifications": snmpTsmNotifications,
       "snmpTsmMIBObjects": snmpTsmMIBObjects,
       "snmpTsmStats": snmpTsmStats,
       "snmpTsmInvalidCaches": snmpTsmInvalidCaches,
       "snmpTsmInadequateSecurityLevels": snmpTsmInadequateSecurityLevels,
       "snmpTsmUnknownPrefixes": snmpTsmUnknownPrefixes,
       "snmpTsmInvalidPrefixes": snmpTsmInvalidPrefixes,
       "snmpTsmConfiguration": snmpTsmConfiguration,
       "snmpTsmConfigurationUsePrefix": snmpTsmConfigurationUsePrefix,
       "snmpTsmConformance": snmpTsmConformance,
       "snmpTsmCompliances": snmpTsmCompliances,
       "snmpTsmCompliance": snmpTsmCompliance,
       "snmpTsmGroups": snmpTsmGroups,
       "snmpTsmGroup": snmpTsmGroup}
)
