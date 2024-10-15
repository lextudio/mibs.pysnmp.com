# SNMP MIB module (ADTX-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTX-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:38 2024
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

_Adtx_ObjectIdentity = ObjectIdentity
adtx = _Adtx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653)
)
_AdtxReg_ObjectIdentity = ObjectIdentity
adtxReg = _AdtxReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653, 1)
)
_AdtxGeneric_ObjectIdentity = ObjectIdentity
adtxGeneric = _AdtxGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653, 2)
)
_AdtxProducts_ObjectIdentity = ObjectIdentity
adtxProducts = _AdtxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653, 3)
)
_AdtxExpr_ObjectIdentity = ObjectIdentity
adtxExpr = _AdtxExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTX-SMI",
    **{"adtx": adtx,
       "adtxReg": adtxReg,
       "adtxGeneric": adtxGeneric,
       "adtxProducts": adtxProducts,
       "adtxExpr": adtxExpr}
)
