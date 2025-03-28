# SNMP MIB module (MITEL-IPGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-IPGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:19 2024
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

mitelRouterIpGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1)
)
mitelRouterIpGroup.setRevisions(
        ("2003-03-24 09:08",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelIpGrpFilterGroup_ObjectIdentity = ObjectIdentity
mitelIpGrpFilterGroup = _MitelIpGrpFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1)
)
_MitelIpGrpNatGroup_ObjectIdentity = ObjectIdentity
mitelIpGrpNatGroup = _MitelIpGrpNatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2)
)
_MitelIpGrpDnsGroup_ObjectIdentity = ObjectIdentity
mitelIpGrpDnsGroup = _MitelIpGrpDnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3)
)
_MitelIpGrpIpVirtualGroup_ObjectIdentity = ObjectIdentity
mitelIpGrpIpVirtualGroup = _MitelIpGrpIpVirtualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4)
)
_MitelIpGrpLogicalGroup_ObjectIdentity = ObjectIdentity
mitelIpGrpLogicalGroup = _MitelIpGrpLogicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5)
)
_MitelIpGrpBackupWANGroup_ObjectIdentity = ObjectIdentity
mitelIpGrpBackupWANGroup = _MitelIpGrpBackupWANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-IPGROUP-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpFilterGroup": mitelIpGrpFilterGroup,
       "mitelIpGrpNatGroup": mitelIpGrpNatGroup,
       "mitelIpGrpDnsGroup": mitelIpGrpDnsGroup,
       "mitelIpGrpIpVirtualGroup": mitelIpGrpIpVirtualGroup,
       "mitelIpGrpLogicalGroup": mitelIpGrpLogicalGroup,
       "mitelIpGrpBackupWANGroup": mitelIpGrpBackupWANGroup}
)
