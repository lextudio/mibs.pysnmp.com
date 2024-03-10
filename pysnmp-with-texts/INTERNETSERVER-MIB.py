"""SNMP MIB module (INTERNETSERVER-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTERNETSERVER-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:01:31 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(software,
 microsoft) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "software",
    "microsoft")

(NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance")

(Unsigned32,
 Counter32,
 IpAddress,
 ObjectIdentity,
 Integer32,
 ModuleIdentity,
 MibIdentifier,
 Counter64,
 NotificationType,
 Gauge32,
 iso,
 enterprises,
 Bits,
 TimeTicks,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Unsigned32",
    "Counter32",
    "IpAddress",
    "ObjectIdentity",
    "Integer32",
    "ModuleIdentity",
    "MibIdentifier",
    "Counter64",
    "NotificationType",
    "Gauge32",
    "iso",
    "enterprises",
    "Bits",
    "TimeTicks",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InternetServer_ObjectIdentity = ObjectIdentity
internetServer = _InternetServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7)
)
_InetSrvCommon_ObjectIdentity = ObjectIdentity
inetSrvCommon = _InetSrvCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 1)
)
_InetSrvStats_ObjectIdentity = ObjectIdentity
inetSrvStats = _InetSrvStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTERNETSERVER-MIB",
    **{"internetServer": internetServer,
       "inetSrvCommon": inetSrvCommon,
       "inetSrvStats": inetSrvStats}
)
