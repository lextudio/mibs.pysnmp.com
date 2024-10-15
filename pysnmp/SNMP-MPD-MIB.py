# SNMP MIB module (SNMP-MPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-MPD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:56 2024
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
 snmpModules) = mibBuilder.importSymbols(
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
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

snmpMPDMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 11)
)
snmpMPDMIB.setRevisions(
        ("2002-10-14 00:00",
         "1999-05-04 16:36",
         "1997-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpMPDAdmin_ObjectIdentity = ObjectIdentity
snmpMPDAdmin = _SnmpMPDAdmin_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 1)
)
_SnmpMPDMIBObjects_ObjectIdentity = ObjectIdentity
snmpMPDMIBObjects = _SnmpMPDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 2)
)
_SnmpMPDStats_ObjectIdentity = ObjectIdentity
snmpMPDStats = _SnmpMPDStats_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 2, 1)
)
_SnmpUnknownSecurityModels_Type = Counter32
_SnmpUnknownSecurityModels_Object = MibScalar
snmpUnknownSecurityModels = _SnmpUnknownSecurityModels_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 1),
    _SnmpUnknownSecurityModels_Type()
)
snmpUnknownSecurityModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownSecurityModels.setStatus("current")
_SnmpInvalidMsgs_Type = Counter32
_SnmpInvalidMsgs_Object = MibScalar
snmpInvalidMsgs = _SnmpInvalidMsgs_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 2),
    _SnmpInvalidMsgs_Type()
)
snmpInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInvalidMsgs.setStatus("current")
_SnmpUnknownPDUHandlers_Type = Counter32
_SnmpUnknownPDUHandlers_Object = MibScalar
snmpUnknownPDUHandlers = _SnmpUnknownPDUHandlers_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 3),
    _SnmpUnknownPDUHandlers_Type()
)
snmpUnknownPDUHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownPDUHandlers.setStatus("current")
_SnmpMPDMIBConformance_ObjectIdentity = ObjectIdentity
snmpMPDMIBConformance = _SnmpMPDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 3)
)
_SnmpMPDMIBCompliances_ObjectIdentity = ObjectIdentity
snmpMPDMIBCompliances = _SnmpMPDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 3, 1)
)
_SnmpMPDMIBGroups_ObjectIdentity = ObjectIdentity
snmpMPDMIBGroups = _SnmpMPDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 3, 2)
)

# Managed Objects groups

snmpMPDGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 11, 3, 2, 1)
)
snmpMPDGroup.setObjects(
      *(("SNMP-MPD-MIB", "snmpUnknownSecurityModels"),
        ("SNMP-MPD-MIB", "snmpInvalidMsgs"),
        ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"))
)
if mibBuilder.loadTexts:
    snmpMPDGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpMPDCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    snmpMPDCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-MPD-MIB",
    **{"snmpMPDMIB": snmpMPDMIB,
       "snmpMPDAdmin": snmpMPDAdmin,
       "snmpMPDMIBObjects": snmpMPDMIBObjects,
       "snmpMPDStats": snmpMPDStats,
       "snmpUnknownSecurityModels": snmpUnknownSecurityModels,
       "snmpInvalidMsgs": snmpInvalidMsgs,
       "snmpUnknownPDUHandlers": snmpUnknownPDUHandlers,
       "snmpMPDMIBConformance": snmpMPDMIBConformance,
       "snmpMPDMIBCompliances": snmpMPDMIBCompliances,
       "snmpMPDCompliance": snmpMPDCompliance,
       "snmpMPDMIBGroups": snmpMPDMIBGroups,
       "snmpMPDGroup": snmpMPDGroup}
)
