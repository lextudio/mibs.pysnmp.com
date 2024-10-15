# SNMP MIB module (Dlink-IMPB-FEATURES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dlink-IMPB-FEATURES
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:52 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlImpbFeatures = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlImpbManagment_ObjectIdentity = ObjectIdentity
rlImpbManagment = _RlImpbManagment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1)
)
_RlImpbArpInspection_ObjectIdentity = ObjectIdentity
rlImpbArpInspection = _RlImpbArpInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2)
)
_RlImpbDiscovery_ObjectIdentity = ObjectIdentity
rlImpbDiscovery = _RlImpbDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 3)
)
_RlImpbGratitiousArp_ObjectIdentity = ObjectIdentity
rlImpbGratitiousArp = _RlImpbGratitiousArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 4)
)
_RlImpbIpInspection_ObjectIdentity = ObjectIdentity
rlImpbIpInspection = _RlImpbIpInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dlink-IMPB-FEATURES",
    **{"rlImpbFeatures": rlImpbFeatures,
       "rlImpbManagment": rlImpbManagment,
       "rlImpbArpInspection": rlImpbArpInspection,
       "rlImpbDiscovery": rlImpbDiscovery,
       "rlImpbGratitiousArp": rlImpbGratitiousArp,
       "rlImpbIpInspection": rlImpbIpInspection}
)
