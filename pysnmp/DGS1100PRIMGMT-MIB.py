# SNMP MIB module (DGS1100PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS1100PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:03 2024
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

(dlink_mgmt,
 dlink_products) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt",
    "dlink-products")

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

_Dgs1100SeriesProd_ObjectIdentity = ObjectIdentity
dgs1100SeriesProd = _Dgs1100SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134)
)
_Dgs1100_16_ObjectIdentity = ObjectIdentity
dgs1100_16 = _Dgs1100_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 3)
)
_Dgs1100_16ME_ObjectIdentity = ObjectIdentity
dgs1100_16ME = _Dgs1100_16ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 4)
)
_Dgs1100_18_ObjectIdentity = ObjectIdentity
dgs1100_18 = _Dgs1100_18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 5)
)
_Dgs1100_18ME_ObjectIdentity = ObjectIdentity
dgs1100_18ME = _Dgs1100_18ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 6)
)
_Dgs1100_24_ObjectIdentity = ObjectIdentity
dgs1100_24 = _Dgs1100_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 7)
)
_Dgs1100_24ME_ObjectIdentity = ObjectIdentity
dgs1100_24ME = _Dgs1100_24ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 8)
)
_Dgs1100_24P_ObjectIdentity = ObjectIdentity
dgs1100_24P = _Dgs1100_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 9)
)
_Dgs1100_24PME_ObjectIdentity = ObjectIdentity
dgs1100_24PME = _Dgs1100_24PME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 10)
)
_Dgs1100_26_ObjectIdentity = ObjectIdentity
dgs1100_26 = _Dgs1100_26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 11)
)
_Dgs1100_26ME_ObjectIdentity = ObjectIdentity
dgs1100_26ME = _Dgs1100_26ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS1100PRIMGMT-MIB",
    **{"dgs1100SeriesProd": dgs1100SeriesProd,
       "dgs1100-16": dgs1100_16,
       "dgs1100-16ME": dgs1100_16ME,
       "dgs1100-18": dgs1100_18,
       "dgs1100-18ME": dgs1100_18ME,
       "dgs1100-24": dgs1100_24,
       "dgs1100-24ME": dgs1100_24ME,
       "dgs1100-24P": dgs1100_24P,
       "dgs1100-24PME": dgs1100_24PME,
       "dgs1100-26": dgs1100_26,
       "dgs1100-26ME": dgs1100_26ME}
)
