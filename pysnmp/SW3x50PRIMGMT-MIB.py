# SNMP MIB module (SW3x50PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW3x50PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:05 2024
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

_Dlink_Des3x50SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Des3x50SeriesProd = _Dlink_Des3x50SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52)
)
_Dlink_Des3x50Prod_ObjectIdentity = ObjectIdentity
dlink_Des3x50Prod = _Dlink_Des3x50Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 1)
)
_Dlink_Des3x50Prod_Des3250_ObjectIdentity = ObjectIdentity
dlink_Des3x50Prod_Des3250 = _Dlink_Des3x50Prod_Des3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 1, 1)
)
_Dlink_Des3x50Prod_Des3350_ObjectIdentity = ObjectIdentity
dlink_Des3x50Prod_Des3350 = _Dlink_Des3x50Prod_Des3350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 1, 2)
)
_Dlink_Des3x50Prod_Des3550_ObjectIdentity = ObjectIdentity
dlink_Des3x50Prod_Des3550 = _Dlink_Des3x50Prod_Des3550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 1, 3)
)
_Des3x50DevRegistration_ObjectIdentity = ObjectIdentity
des3x50DevRegistration = _Des3x50DevRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 2)
)
_Des3x50Device_ObjectIdentity = ObjectIdentity
des3x50Device = _Des3x50Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 2, 1)
)
_Des3x50UnitRegistration_ObjectIdentity = ObjectIdentity
des3x50UnitRegistration = _Des3x50UnitRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 3)
)
_Des3x50Unit_ObjectIdentity = ObjectIdentity
des3x50Unit = _Des3x50Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 3, 1)
)
_Des3x50ModuleRegistration_ObjectIdentity = ObjectIdentity
des3x50ModuleRegistration = _Des3x50ModuleRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 4)
)
_Des3x50_Module_Mainboard_48Port_ObjectIdentity = ObjectIdentity
des3x50_Module_Mainboard_48Port = _Des3x50_Module_Mainboard_48Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 4, 1)
)
_Des3x50_Module_1_Port_GBIC_ObjectIdentity = ObjectIdentity
des3x50_Module_1_Port_GBIC = _Des3x50_Module_1_Port_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 4, 2)
)
_Des3x50PortRegistration_ObjectIdentity = ObjectIdentity
des3x50PortRegistration = _Des3x50PortRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 5)
)
_Des3x50_Port_10_100_TX_ObjectIdentity = ObjectIdentity
des3x50_Port_10_100_TX = _Des3x50_Port_10_100_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 1)
)
_Des3x50_Port_1000_SX_GBIC_ObjectIdentity = ObjectIdentity
des3x50_Port_1000_SX_GBIC = _Des3x50_Port_1000_SX_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 2)
)
_Des3x50_Port_1000_LX_GBIC_ObjectIdentity = ObjectIdentity
des3x50_Port_1000_LX_GBIC = _Des3x50_Port_1000_LX_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 3)
)
_Des3x50_Port_1000_TX_ObjectIdentity = ObjectIdentity
des3x50_Port_1000_TX = _Des3x50_Port_1000_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 5, 4)
)
_Des3x50SlotRegistration_ObjectIdentity = ObjectIdentity
des3x50SlotRegistration = _Des3x50SlotRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 6)
)
_Des3x50Slot1_ObjectIdentity = ObjectIdentity
des3x50Slot1 = _Des3x50Slot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 52, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3x50PRIMGMT-MIB",
    **{"dlink-Des3x50SeriesProd": dlink_Des3x50SeriesProd,
       "dlink-Des3x50Prod": dlink_Des3x50Prod,
       "dlink-Des3x50Prod-Des3250": dlink_Des3x50Prod_Des3250,
       "dlink-Des3x50Prod-Des3350": dlink_Des3x50Prod_Des3350,
       "dlink-Des3x50Prod-Des3550": dlink_Des3x50Prod_Des3550,
       "des3x50DevRegistration": des3x50DevRegistration,
       "des3x50Device": des3x50Device,
       "des3x50UnitRegistration": des3x50UnitRegistration,
       "des3x50Unit": des3x50Unit,
       "des3x50ModuleRegistration": des3x50ModuleRegistration,
       "des3x50-Module-Mainboard-48Port": des3x50_Module_Mainboard_48Port,
       "des3x50-Module-1-Port-GBIC": des3x50_Module_1_Port_GBIC,
       "des3x50PortRegistration": des3x50PortRegistration,
       "des3x50-Port-10-100-TX": des3x50_Port_10_100_TX,
       "des3x50-Port-1000-SX-GBIC": des3x50_Port_1000_SX_GBIC,
       "des3x50-Port-1000-LX-GBIC": des3x50_Port_1000_LX_GBIC,
       "des3x50-Port-1000-TX": des3x50_Port_1000_TX,
       "des3x50SlotRegistration": des3x50SlotRegistration,
       "des3x50Slot1": des3x50Slot1}
)
