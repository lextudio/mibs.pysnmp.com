# SNMP MIB module (JUNIPER-IPFORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IPFORWARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:09 2024
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

(inetCidrRouteEntry,
 ipCidrRouteEntry) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteEntry",
    "ipCidrRouteEntry")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

jnxIpForwardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38)
)
jnxIpForwardMIB.setRevisions(
        ("2011-11-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxIpCidrRouteTable_Object = MibTable
jnxIpCidrRouteTable = _JnxIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 1)
)
if mibBuilder.loadTexts:
    jnxIpCidrRouteTable.setStatus("deprecated")
_JnxIpCidrRouteEntry_Object = MibTableRow
jnxIpCidrRouteEntry = _JnxIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 1, 1)
)
if mibBuilder.loadTexts:
    jnxIpCidrRouteEntry.setStatus("deprecated")
_JnxIpCidrRouteTunnelName_Type = SnmpAdminString
_JnxIpCidrRouteTunnelName_Object = MibTableColumn
jnxIpCidrRouteTunnelName = _JnxIpCidrRouteTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 1, 1, 1),
    _JnxIpCidrRouteTunnelName_Type()
)
jnxIpCidrRouteTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpCidrRouteTunnelName.setStatus("deprecated")
_JnxInetCidrRouteTable_Object = MibTable
jnxInetCidrRouteTable = _JnxInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 2)
)
if mibBuilder.loadTexts:
    jnxInetCidrRouteTable.setStatus("current")
_JnxInetCidrRouteEntry_Object = MibTableRow
jnxInetCidrRouteEntry = _JnxInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 2, 1)
)
if mibBuilder.loadTexts:
    jnxInetCidrRouteEntry.setStatus("current")
_JnxInetCidrRouteTunnelName_Type = SnmpAdminString
_JnxInetCidrRouteTunnelName_Object = MibTableColumn
jnxInetCidrRouteTunnelName = _JnxInetCidrRouteTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 2, 1, 1),
    _JnxInetCidrRouteTunnelName_Type()
)
jnxInetCidrRouteTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxInetCidrRouteTunnelName.setStatus("current")
ipCidrRouteEntry.registerAugmentions(
    ("JUNIPER-IPFORWARD-MIB",
     "jnxIpCidrRouteEntry")
)
jnxIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
inetCidrRouteEntry.registerAugmentions(
    ("JUNIPER-IPFORWARD-MIB",
     "jnxInetCidrRouteEntry")
)
jnxInetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IPFORWARD-MIB",
    **{"jnxIpForwardMIB": jnxIpForwardMIB,
       "jnxIpCidrRouteTable": jnxIpCidrRouteTable,
       "jnxIpCidrRouteEntry": jnxIpCidrRouteEntry,
       "jnxIpCidrRouteTunnelName": jnxIpCidrRouteTunnelName,
       "jnxInetCidrRouteTable": jnxInetCidrRouteTable,
       "jnxInetCidrRouteEntry": jnxInetCidrRouteEntry,
       "jnxInetCidrRouteTunnelName": jnxInetCidrRouteTunnelName}
)
