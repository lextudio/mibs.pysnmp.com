# SNMP MIB module (ASCEND-WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-WAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:50 2024
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

(advancedAgent,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "advancedAgent")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WanTypeAny_ObjectIdentity = ObjectIdentity
wanTypeAny = _WanTypeAny_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 1)
)
_WanTypeT1_ObjectIdentity = ObjectIdentity
wanTypeT1 = _WanTypeT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 2)
)
_WanTypeE1_ObjectIdentity = ObjectIdentity
wanTypeE1 = _WanTypeE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 3)
)
_WanTypeDpnss_ObjectIdentity = ObjectIdentity
wanTypeDpnss = _WanTypeDpnss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 4)
)
_WanTypeBri_ObjectIdentity = ObjectIdentity
wanTypeBri = _WanTypeBri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 5)
)
_WanTypeS562_ObjectIdentity = ObjectIdentity
wanTypeS562 = _WanTypeS562_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 6)
)
_WanTypeS564_ObjectIdentity = ObjectIdentity
wanTypeS564 = _WanTypeS564_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 7)
)
_WanTypeSdsl_ObjectIdentity = ObjectIdentity
wanTypeSdsl = _WanTypeSdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 8)
)
_WanTypeAdslCap_ObjectIdentity = ObjectIdentity
wanTypeAdslCap = _WanTypeAdslCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 9)
)
_WanTypeAdslDmt_ObjectIdentity = ObjectIdentity
wanTypeAdslDmt = _WanTypeAdslDmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 10)
)
_WanTypeHdsl2_ObjectIdentity = ObjectIdentity
wanTypeHdsl2 = _WanTypeHdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-WAN-MIB",
    **{"wanTypeAny": wanTypeAny,
       "wanTypeT1": wanTypeT1,
       "wanTypeE1": wanTypeE1,
       "wanTypeDpnss": wanTypeDpnss,
       "wanTypeBri": wanTypeBri,
       "wanTypeS562": wanTypeS562,
       "wanTypeS564": wanTypeS564,
       "wanTypeSdsl": wanTypeSdsl,
       "wanTypeAdslCap": wanTypeAdslCap,
       "wanTypeAdslDmt": wanTypeAdslDmt,
       "wanTypeHdsl2": wanTypeHdsl2}
)
