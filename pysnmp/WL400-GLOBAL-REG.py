# SNMP MIB module (WL400-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WL400-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:01 2024
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

wl400GlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 232, 143, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_Wl400Reg_ObjectIdentity = ObjectIdentity
wl400Reg = _Wl400Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 143)
)
_Wl400Modules_ObjectIdentity = ObjectIdentity
wl400Modules = _Wl400Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 143, 1)
)
_Wl400HAP_ObjectIdentity = ObjectIdentity
wl400HAP = _Wl400HAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 143, 7)
)
if mibBuilder.loadTexts:
    wl400HAP.setStatus("current")
_Wl400Generic_ObjectIdentity = ObjectIdentity
wl400Generic = _Wl400Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 144)
)
_Wl400Products_ObjectIdentity = ObjectIdentity
wl400Products = _Wl400Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 145)
)
_Wl400Experimental_ObjectIdentity = ObjectIdentity
wl400Experimental = _Wl400Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 146)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WL400-GLOBAL-REG",
    **{"compaq": compaq,
       "wl400Reg": wl400Reg,
       "wl400Modules": wl400Modules,
       "wl400GlobalRegModule": wl400GlobalRegModule,
       "wl400HAP": wl400HAP,
       "wl400Generic": wl400Generic,
       "wl400Products": wl400Products,
       "wl400Experimental": wl400Experimental}
)
