# SNMP MIB module (FNET-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNET-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:17 2024
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

_Fnet_ObjectIdentity = ObjectIdentity
fnet = _Fnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226)
)
_FnetReg_ObjectIdentity = ObjectIdentity
fnetReg = _FnetReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1)
)
_FnetOneTouch_ObjectIdentity = ObjectIdentity
fnetOneTouch = _FnetOneTouch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 2)
)
_FnetOptiView_ObjectIdentity = ObjectIdentity
fnetOptiView = _FnetOptiView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 3)
)
_FnetOvIna_ObjectIdentity = ObjectIdentity
fnetOvIna = _FnetOvIna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 3, 1)
)
_FnetOvWga_ObjectIdentity = ObjectIdentity
fnetOvWga = _FnetOvWga_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 3, 2)
)
_FnetOvLa_ObjectIdentity = ObjectIdentity
fnetOvLa = _FnetOvLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 3, 3)
)
_FnetOvWanFiber_ObjectIdentity = ObjectIdentity
fnetOvWanFiber = _FnetOvWanFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 3, 4)
)
_FnetOvWanCopper_ObjectIdentity = ObjectIdentity
fnetOvWanCopper = _FnetOvWanCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 3, 5)
)
_FnetTrafficAnalyzer_ObjectIdentity = ObjectIdentity
fnetTrafficAnalyzer = _FnetTrafficAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 6)
)
_FnetLinkAnalyzer_ObjectIdentity = ObjectIdentity
fnetLinkAnalyzer = _FnetLinkAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 8)
)
_FnetProtocolExpert_ObjectIdentity = ObjectIdentity
fnetProtocolExpert = _FnetProtocolExpert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 9)
)
_FnetLanMeter_ObjectIdentity = ObjectIdentity
fnetLanMeter = _FnetLanMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 1, 685)
)
_FnetGeneric_ObjectIdentity = ObjectIdentity
fnetGeneric = _FnetGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 2)
)
_FnetOptiViewGeneric_ObjectIdentity = ObjectIdentity
fnetOptiViewGeneric = _FnetOptiViewGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1)
)
_FnetProduct_ObjectIdentity = ObjectIdentity
fnetProduct = _FnetProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 3)
)
_FnetOptiViewProduct_ObjectIdentity = ObjectIdentity
fnetOptiViewProduct = _FnetOptiViewProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 3, 1)
)
_FnetCapabilities_ObjectIdentity = ObjectIdentity
fnetCapabilities = _FnetCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 4)
)
_FnetRequirements_ObjectIdentity = ObjectIdentity
fnetRequirements = _FnetRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 5)
)
_FnetExperimental_ObjectIdentity = ObjectIdentity
fnetExperimental = _FnetExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNET-GLOBAL-REG",
    **{"fnet": fnet,
       "fnetReg": fnetReg,
       "fnetOneTouch": fnetOneTouch,
       "fnetOptiView": fnetOptiView,
       "fnetOvIna": fnetOvIna,
       "fnetOvWga": fnetOvWga,
       "fnetOvLa": fnetOvLa,
       "fnetOvWanFiber": fnetOvWanFiber,
       "fnetOvWanCopper": fnetOvWanCopper,
       "fnetTrafficAnalyzer": fnetTrafficAnalyzer,
       "fnetLinkAnalyzer": fnetLinkAnalyzer,
       "fnetProtocolExpert": fnetProtocolExpert,
       "fnetLanMeter": fnetLanMeter,
       "fnetGeneric": fnetGeneric,
       "fnetOptiViewGeneric": fnetOptiViewGeneric,
       "fnetProduct": fnetProduct,
       "fnetOptiViewProduct": fnetOptiViewProduct,
       "fnetCapabilities": fnetCapabilities,
       "fnetRequirements": fnetRequirements,
       "fnetExperimental": fnetExperimental}
)
