# SNMP MIB module (CISCO-PRODUCTS-MIB-CORRECTIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PRODUCTS-MIB-CORRECTIONS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:09 2024
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

(ciscoModules,
 ciscoProducts) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules",
    "ciscoProducts")

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

ciscoProductsMIBCorrections = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 65535)
)
ciscoProductsMIBCorrections.setRevisions(
        ("2014-11-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Catalyst365024TS_ObjectIdentity = ObjectIdentity
catalyst365024TS = _Catalyst365024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1823)
)
_Catalyst365048TS_ObjectIdentity = ObjectIdentity
catalyst365048TS = _Catalyst365048TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1824)
)
_Catalyst365024PS_ObjectIdentity = ObjectIdentity
catalyst365024PS = _Catalyst365024PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1825)
)
_Catalyst365048PS_ObjectIdentity = ObjectIdentity
catalyst365048PS = _Catalyst365048PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1826)
)
_Catalyst365024TD_ObjectIdentity = ObjectIdentity
catalyst365024TD = _Catalyst365024TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1827)
)
_Catalyst365048TD_ObjectIdentity = ObjectIdentity
catalyst365048TD = _Catalyst365048TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1828)
)
_Catalyst365024PD_ObjectIdentity = ObjectIdentity
catalyst365024PD = _Catalyst365024PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1829)
)
_Catalyst365048PD_ObjectIdentity = ObjectIdentity
catalyst365048PD = _Catalyst365048PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1830)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PRODUCTS-MIB-CORRECTIONS",
    **{"catalyst365024TS": catalyst365024TS,
       "catalyst365048TS": catalyst365048TS,
       "catalyst365024PS": catalyst365024PS,
       "catalyst365048PS": catalyst365048PS,
       "catalyst365024TD": catalyst365024TD,
       "catalyst365048TD": catalyst365048TD,
       "catalyst365024PD": catalyst365024PD,
       "catalyst365048PD": catalyst365048PD,
       "ciscoProductsMIBCorrections": ciscoProductsMIBCorrections}
)
