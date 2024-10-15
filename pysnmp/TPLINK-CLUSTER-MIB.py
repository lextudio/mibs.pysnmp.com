# SNMP MIB module (TPLINK-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:51 2024
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

(tplinkClusterMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-CLUSTERTREE-MIB",
    "tplinkClusterMIBObjects")


# MODULE-IDENTITY

tplinkClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1)
)
tplinkClusterMIB.setRevisions(
        ("2009-08-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NdpManage_ObjectIdentity = ObjectIdentity
ndpManage = _NdpManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1)
)
_NtdpManage_ObjectIdentity = ObjectIdentity
ntdpManage = _NtdpManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2)
)
_ClusterManage_ObjectIdentity = ObjectIdentity
clusterManage = _ClusterManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-CLUSTER-MIB",
    **{"tplinkClusterMIB": tplinkClusterMIB,
       "ndpManage": ndpManage,
       "ntdpManage": ntdpManage,
       "clusterManage": clusterManage}
)
