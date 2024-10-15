# SNMP MIB module (RDN-PORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-PORTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:11 2024
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

(rdnDefinitions,) = mibBuilder.importSymbols(
    "RDN-DEFINITIONS-MIB",
    "rdnDefinitions")

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

rdnPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5)
)
rdnPorts.setRevisions(
        ("2008-08-08 00:00",
         "2005-10-20 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnPortsUnknown_ObjectIdentity = ObjectIdentity
rdnPortsUnknown = _RdnPortsUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 0)
)
_RdnPortsGige_ObjectIdentity = ObjectIdentity
rdnPortsGige = _RdnPortsGige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 1)
)
_RdnPortsEthernet_ObjectIdentity = ObjectIdentity
rdnPortsEthernet = _RdnPortsEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 2)
)
_RdnPortsCableMac_ObjectIdentity = ObjectIdentity
rdnPortsCableMac = _RdnPortsCableMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 3)
)
_RdnPortsCableUpstream_ObjectIdentity = ObjectIdentity
rdnPortsCableUpstream = _RdnPortsCableUpstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 4)
)
_RdnPortsCableDownstream_ObjectIdentity = ObjectIdentity
rdnPortsCableDownstream = _RdnPortsCableDownstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 5)
)
_RdnPortsCableSubIf_ObjectIdentity = ObjectIdentity
rdnPortsCableSubIf = _RdnPortsCableSubIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 6)
)
_RdnPortsLoopback_ObjectIdentity = ObjectIdentity
rdnPortsLoopback = _RdnPortsLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 7)
)
_RdnPortsT1_ObjectIdentity = ObjectIdentity
rdnPortsT1 = _RdnPortsT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 8)
)
_RdnPortsNull_ObjectIdentity = ObjectIdentity
rdnPortsNull = _RdnPortsNull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 9)
)
_RdnPortsTunnel_ObjectIdentity = ObjectIdentity
rdnPortsTunnel = _RdnPortsTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 10)
)
_RdnPortsPOS_ObjectIdentity = ObjectIdentity
rdnPortsPOS = _RdnPortsPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 11)
)
_RdnPortsATM_ObjectIdentity = ObjectIdentity
rdnPortsATM = _RdnPortsATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-PORTS-MIB",
    **{"rdnPorts": rdnPorts,
       "rdnPortsUnknown": rdnPortsUnknown,
       "rdnPortsGige": rdnPortsGige,
       "rdnPortsEthernet": rdnPortsEthernet,
       "rdnPortsCableMac": rdnPortsCableMac,
       "rdnPortsCableUpstream": rdnPortsCableUpstream,
       "rdnPortsCableDownstream": rdnPortsCableDownstream,
       "rdnPortsCableSubIf": rdnPortsCableSubIf,
       "rdnPortsLoopback": rdnPortsLoopback,
       "rdnPortsT1": rdnPortsT1,
       "rdnPortsNull": rdnPortsNull,
       "rdnPortsTunnel": rdnPortsTunnel,
       "rdnPortsPOS": rdnPortsPOS,
       "rdnPortsATM": rdnPortsATM}
)
