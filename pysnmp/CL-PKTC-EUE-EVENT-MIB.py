# SNMP MIB module (CL-PKTC-EUE-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CL-PKTC-EUE-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:31 2024
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

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

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

pktcEUEEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEUEEventNotifications_ObjectIdentity = ObjectIdentity
pktcEUEEventNotifications = _PktcEUEEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 0)
)
_PktcEUEEventObjects_ObjectIdentity = ObjectIdentity
pktcEUEEventObjects = _PktcEUEEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 1)
)


class _PktcEUEMEMVersion_Type(SnmpAdminString):
    """Custom type pktcEUEMEMVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEMEMVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEMEMVersion_Object = MibScalar
pktcEUEMEMVersion = _PktcEUEMEMVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 1, 1),
    _PktcEUEMEMVersion_Type()
)
pktcEUEMEMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEMEMVersion.setStatus("current")
_PktcEUEEventConformance_ObjectIdentity = ObjectIdentity
pktcEUEEventConformance = _PktcEUEEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2)
)
_PktcEUEEventCompliances_ObjectIdentity = ObjectIdentity
pktcEUEEventCompliances = _PktcEUEEventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 1)
)
_PktcEUEEventGroups_ObjectIdentity = ObjectIdentity
pktcEUEEventGroups = _PktcEUEEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 2)
)

# Managed Objects groups

pktcEUEMEMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 2, 1)
)
pktcEUEMEMGroup.setObjects(
    ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMVersion")
)
if mibBuilder.loadTexts:
    pktcEUEMEMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUEEventCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUEEventCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-EVENT-MIB",
    **{"pktcEUEEventMIB": pktcEUEEventMIB,
       "pktcEUEEventNotifications": pktcEUEEventNotifications,
       "pktcEUEEventObjects": pktcEUEEventObjects,
       "pktcEUEMEMVersion": pktcEUEMEMVersion,
       "pktcEUEEventConformance": pktcEUEEventConformance,
       "pktcEUEEventCompliances": pktcEUEEventCompliances,
       "pktcEUEEventCompliance": pktcEUEEventCompliance,
       "pktcEUEEventGroups": pktcEUEEventGroups,
       "pktcEUEMEMGroup": pktcEUEMEMGroup}
)
