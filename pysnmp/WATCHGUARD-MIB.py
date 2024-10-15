# SNMP MIB module (WATCHGUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:12 2024
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

_Watchguard_ObjectIdentity = ObjectIdentity
watchguard = _Watchguard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097)
)
_WgProducts_ObjectIdentity = ObjectIdentity
wgProducts = _WgProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1)
)
_FbXSeries_ObjectIdentity = ObjectIdentity
fbXSeries = _FbXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4)
)
_FbX500_ObjectIdentity = ObjectIdentity
fbX500 = _FbX500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 1)
)
_FbX550e_ObjectIdentity = ObjectIdentity
fbX550e = _FbX550e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 2)
)
_FbX700_ObjectIdentity = ObjectIdentity
fbX700 = _FbX700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 3)
)
_FbX750e_ObjectIdentity = ObjectIdentity
fbX750e = _FbX750e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 4)
)
_FbX750e_4_ObjectIdentity = ObjectIdentity
fbX750e_4 = _FbX750e_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 5)
)
_FbX1000_ObjectIdentity = ObjectIdentity
fbX1000 = _FbX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 6)
)
_FbX1250e_ObjectIdentity = ObjectIdentity
fbX1250e = _FbX1250e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 7)
)
_FbX1250e_4_ObjectIdentity = ObjectIdentity
fbX1250e_4 = _FbX1250e_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 8)
)
_FbX2500_ObjectIdentity = ObjectIdentity
fbX2500 = _FbX2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 9)
)
_FbX5000_ObjectIdentity = ObjectIdentity
fbX5000 = _FbX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 10)
)
_FbX5500e_ObjectIdentity = ObjectIdentity
fbX5500e = _FbX5500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 11)
)
_FbX6000_ObjectIdentity = ObjectIdentity
fbX6000 = _FbX6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 12)
)
_FbX6500e_ObjectIdentity = ObjectIdentity
fbX6500e = _FbX6500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 13)
)
_FbX8000_ObjectIdentity = ObjectIdentity
fbX8000 = _FbX8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 14)
)
_FbX8500e_ObjectIdentity = ObjectIdentity
fbX8500e = _FbX8500e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 15)
)
_FbX8500e_F_ObjectIdentity = ObjectIdentity
fbX8500e_F = _FbX8500e_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 1, 4, 16)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-MIB",
    **{"watchguard": watchguard,
       "wgProducts": wgProducts,
       "fbXSeries": fbXSeries,
       "fbX500": fbX500,
       "fbX550e": fbX550e,
       "fbX700": fbX700,
       "fbX750e": fbX750e,
       "fbX750e-4": fbX750e_4,
       "fbX1000": fbX1000,
       "fbX1250e": fbX1250e,
       "fbX1250e-4": fbX1250e_4,
       "fbX2500": fbX2500,
       "fbX5000": fbX5000,
       "fbX5500e": fbX5500e,
       "fbX6000": fbX6000,
       "fbX6500e": fbX6500e,
       "fbX8000": fbX8000,
       "fbX8500e": fbX8500e,
       "fbX8500e-F": fbX8500e_F}
)
