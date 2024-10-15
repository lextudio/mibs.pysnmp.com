# SNMP MIB module (COMPAQ-ID-REC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMPAQ-ID-REC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:47 2024
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

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_Compaq_proLiantBLeClassCG_proLiantBLpClassGbE_ObjectIdentity = ObjectIdentity
compaq_proLiantBLeClassCG_proLiantBLpClassGbE = _Compaq_proLiantBLeClassCG_proLiantBLpClassGbE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161)
)
_Compaq_products_ObjectIdentity = ObjectIdentity
compaq_products = _Compaq_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1)
)
_Compaq_ProLiantBLeClassCGSeriesProd_ObjectIdentity = ObjectIdentity
compaq_ProLiantBLeClassCGSeriesProd = _Compaq_ProLiantBLeClassCGSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36)
)
_Compaq_ProLiantBLeClassCGProd_ObjectIdentity = ObjectIdentity
compaq_ProLiantBLeClassCGProd = _Compaq_ProLiantBLeClassCGProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1)
)
_ProLiantBLeClassCGDevRegistration_ObjectIdentity = ObjectIdentity
proLiantBLeClassCGDevRegistration = _ProLiantBLeClassCGDevRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 2)
)
_ProLiantBLeClassCGDevice_ObjectIdentity = ObjectIdentity
proLiantBLeClassCGDevice = _ProLiantBLeClassCGDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 2, 1)
)
_ProLiantBLeClassCGUnitRegistration_ObjectIdentity = ObjectIdentity
proLiantBLeClassCGUnitRegistration = _ProLiantBLeClassCGUnitRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 3)
)
_ProLiantBLeClassCGUnit_ObjectIdentity = ObjectIdentity
proLiantBLeClassCGUnit = _ProLiantBLeClassCGUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 3, 1)
)
_ProLiantBLeClassCGModuleRegistration_ObjectIdentity = ObjectIdentity
proLiantBLeClassCGModuleRegistration = _ProLiantBLeClassCGModuleRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 4)
)
_ProLiantBLeClassCG_Module_Mainboard_26Port_ObjectIdentity = ObjectIdentity
proLiantBLeClassCG_Module_Mainboard_26Port = _ProLiantBLeClassCG_Module_Mainboard_26Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 4, 1)
)
_ProLiantBLeClassCGPortRegistration_ObjectIdentity = ObjectIdentity
proLiantBLeClassCGPortRegistration = _ProLiantBLeClassCGPortRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 5)
)
_ProLiantBLeClassCG_Port_10_100_TX_ObjectIdentity = ObjectIdentity
proLiantBLeClassCG_Port_10_100_TX = _ProLiantBLeClassCG_Port_10_100_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 5, 1)
)
_ProLiantBLeClassCG_Port_1000_TX_ObjectIdentity = ObjectIdentity
proLiantBLeClassCG_Port_1000_TX = _ProLiantBLeClassCG_Port_1000_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 36, 1, 5, 2)
)
_Compaq_ProLiantBLpClassGbESeriesProd_ObjectIdentity = ObjectIdentity
compaq_ProLiantBLpClassGbESeriesProd = _Compaq_ProLiantBLpClassGbESeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37)
)
_Compaq_ProLiantBLpClassGbEProd_ObjectIdentity = ObjectIdentity
compaq_ProLiantBLpClassGbEProd = _Compaq_ProLiantBLpClassGbEProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1)
)
_ProLiantBLpClassGbEDevRegistration_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbEDevRegistration = _ProLiantBLpClassGbEDevRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 2)
)
_ProLiantBLpClassGbEDevice_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbEDevice = _ProLiantBLpClassGbEDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 2, 1)
)
_ProLiantBLpClassGbEUnitRegistration_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbEUnitRegistration = _ProLiantBLpClassGbEUnitRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 3)
)
_ProLiantBLpClassGbEUnit_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbEUnit = _ProLiantBLpClassGbEUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 3, 1)
)
_ProLiantBLpClassGbEModuleRegistration_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbEModuleRegistration = _ProLiantBLpClassGbEModuleRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 4)
)
_ProLiantBLpClassGbE_Module_Mainboard_24Port_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbE_Module_Mainboard_24Port = _ProLiantBLpClassGbE_Module_Mainboard_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 4, 1)
)
_ProLiantBLpClassGbEPortRegistration_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbEPortRegistration = _ProLiantBLpClassGbEPortRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 5)
)
_ProLiantBLpClassGbE_Port_10_100_TX_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbE_Port_10_100_TX = _ProLiantBLpClassGbE_Port_10_100_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 5, 1)
)
_ProLiantBLpClassGbE_Port_1000_TX_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbE_Port_1000_TX = _ProLiantBLpClassGbE_Port_1000_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 5, 2)
)
_ProLiantBLpClassGbE_Port_1000_SX_ObjectIdentity = ObjectIdentity
proLiantBLpClassGbE_Port_1000_SX = _ProLiantBLpClassGbE_Port_1000_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 1, 37, 1, 5, 3)
)
_Compaq_mgmt_ObjectIdentity = ObjectIdentity
compaq_mgmt = _Compaq_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 2)
)
_Compaq_common_mgmt_ObjectIdentity = ObjectIdentity
compaq_common_mgmt = _Compaq_common_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPAQ-ID-REC-MIB",
    **{"compaq": compaq,
       "compaq-proLiantBLeClassCG-proLiantBLpClassGbE": compaq_proLiantBLeClassCG_proLiantBLpClassGbE,
       "compaq-products": compaq_products,
       "compaq-ProLiantBLeClassCGSeriesProd": compaq_ProLiantBLeClassCGSeriesProd,
       "compaq-ProLiantBLeClassCGProd": compaq_ProLiantBLeClassCGProd,
       "proLiantBLeClassCGDevRegistration": proLiantBLeClassCGDevRegistration,
       "proLiantBLeClassCGDevice": proLiantBLeClassCGDevice,
       "proLiantBLeClassCGUnitRegistration": proLiantBLeClassCGUnitRegistration,
       "proLiantBLeClassCGUnit": proLiantBLeClassCGUnit,
       "proLiantBLeClassCGModuleRegistration": proLiantBLeClassCGModuleRegistration,
       "proLiantBLeClassCG-Module-Mainboard-26Port": proLiantBLeClassCG_Module_Mainboard_26Port,
       "proLiantBLeClassCGPortRegistration": proLiantBLeClassCGPortRegistration,
       "proLiantBLeClassCG-Port-10-100-TX": proLiantBLeClassCG_Port_10_100_TX,
       "proLiantBLeClassCG-Port-1000-TX": proLiantBLeClassCG_Port_1000_TX,
       "compaq-ProLiantBLpClassGbESeriesProd": compaq_ProLiantBLpClassGbESeriesProd,
       "compaq-ProLiantBLpClassGbEProd": compaq_ProLiantBLpClassGbEProd,
       "proLiantBLpClassGbEDevRegistration": proLiantBLpClassGbEDevRegistration,
       "proLiantBLpClassGbEDevice": proLiantBLpClassGbEDevice,
       "proLiantBLpClassGbEUnitRegistration": proLiantBLpClassGbEUnitRegistration,
       "proLiantBLpClassGbEUnit": proLiantBLpClassGbEUnit,
       "proLiantBLpClassGbEModuleRegistration": proLiantBLpClassGbEModuleRegistration,
       "proLiantBLpClassGbE-Module-Mainboard-24Port": proLiantBLpClassGbE_Module_Mainboard_24Port,
       "proLiantBLpClassGbEPortRegistration": proLiantBLpClassGbEPortRegistration,
       "proLiantBLpClassGbE-Port-10-100-TX": proLiantBLpClassGbE_Port_10_100_TX,
       "proLiantBLpClassGbE-Port-1000-TX": proLiantBLpClassGbE_Port_1000_TX,
       "proLiantBLpClassGbE-Port-1000-SX": proLiantBLpClassGbE_Port_1000_SX,
       "compaq-mgmt": compaq_mgmt,
       "compaq-common-mgmt": compaq_common_mgmt}
)
