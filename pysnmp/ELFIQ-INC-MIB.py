# SNMP MIB module (ELFIQ-INC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELFIQ-INC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:50 2024
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

elfiqInc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19713)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ElfiqMIBProducts_ObjectIdentity = ObjectIdentity
elfiqMIBProducts = _ElfiqMIBProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1)
)
_LinkBalancer_ObjectIdentity = ObjectIdentity
linkBalancer = _LinkBalancer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2)
)
_ElfiqMIBConformance_ObjectIdentity = ObjectIdentity
elfiqMIBConformance = _ElfiqMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2)
)
_CommonConformance_ObjectIdentity = ObjectIdentity
commonConformance = _CommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1)
)
_LinkBalancerConformance_ObjectIdentity = ObjectIdentity
linkBalancerConformance = _LinkBalancerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELFIQ-INC-MIB",
    **{"elfiqInc": elfiqInc,
       "elfiqMIBProducts": elfiqMIBProducts,
       "common": common,
       "linkBalancer": linkBalancer,
       "elfiqMIBConformance": elfiqMIBConformance,
       "commonConformance": commonConformance,
       "linkBalancerConformance": linkBalancerConformance}
)
