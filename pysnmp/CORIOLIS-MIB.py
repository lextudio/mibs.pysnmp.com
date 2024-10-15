# SNMP MIB module (CORIOLIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CORIOLIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:33 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CoriolisMibs_ObjectIdentity = ObjectIdentity
coriolisMibs = _CoriolisMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 1)
)
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 2)
)
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 3)
)
_Ring_ObjectIdentity = ObjectIdentity
ring = _Ring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 4)
)
_Ne_ObjectIdentity = ObjectIdentity
ne = _Ne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 5)
)
_Circuit_ObjectIdentity = ObjectIdentity
circuit = _Circuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 6)
)
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 7)
)
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 8)
)
_Eventlog_ObjectIdentity = ObjectIdentity
eventlog = _Eventlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORIOLIS-MIB",
    **{"coriolisMibs": coriolisMibs,
       "device": device,
       "card": card,
       "port": port,
       "ring": ring,
       "ne": ne,
       "circuit": circuit,
       "routing": routing,
       "interfaces": interfaces,
       "eventlog": eventlog}
)
