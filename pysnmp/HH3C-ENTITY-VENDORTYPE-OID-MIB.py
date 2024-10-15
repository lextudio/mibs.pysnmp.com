# SNMP MIB module (HH3C-ENTITY-VENDORTYPE-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ENTITY-VENDORTYPE-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:05 2024
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

(hh3c,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3c")

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

hh3cEntityVendorTypeOID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEntityVendortypeObjects_ObjectIdentity = ObjectIdentity
hh3cEntityVendortypeObjects = _Hh3cEntityVendortypeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1)
)
_Hh3cevtOther_ObjectIdentity = ObjectIdentity
hh3cevtOther = _Hh3cevtOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1)
)
_Hh3cevtOtherUnknownCard_ObjectIdentity = ObjectIdentity
hh3cevtOtherUnknownCard = _Hh3cevtOtherUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 1)
)
_Hh3cevtCPU_ObjectIdentity = ObjectIdentity
hh3cevtCPU = _Hh3cevtCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 2)
)
_Hh3cevtGeneralCPU_ObjectIdentity = ObjectIdentity
hh3cevtGeneralCPU = _Hh3cevtGeneralCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 2, 1)
)
_Hh3cevtDOM_ObjectIdentity = ObjectIdentity
hh3cevtDOM = _Hh3cevtDOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 3)
)
_Hh3cevtCFCard_ObjectIdentity = ObjectIdentity
hh3cevtCFCard = _Hh3cevtCFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 4)
)
_Hh3cevtHardDisk_ObjectIdentity = ObjectIdentity
hh3cevtHardDisk = _Hh3cevtHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 5)
)
_Hh3cevtUnknown_ObjectIdentity = ObjectIdentity
hh3cevtUnknown = _Hh3cevtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 2)
)
_Hh3cevtChassis_ObjectIdentity = ObjectIdentity
hh3cevtChassis = _Hh3cevtChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 3)
)
_Hh3cevtBackplane_ObjectIdentity = ObjectIdentity
hh3cevtBackplane = _Hh3cevtBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 4)
)
_Hh3cevtContainer_ObjectIdentity = ObjectIdentity
hh3cevtContainer = _Hh3cevtContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 5)
)
_Hh3cevtPowerSupply_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupply = _Hh3cevtPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6)
)
_Hh3cevtPowerSupplyAC_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyAC = _Hh3cevtPowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 2)
)
_Hh3cevtPowerSupplyDC_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyDC = _Hh3cevtPowerSupplyDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 3)
)
_Hh3cevtPowerSupplySTD130W_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplySTD130W = _Hh3cevtPowerSupplySTD130W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 4)
)
_Hh3cevtPowerSupplySTD180W_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplySTD180W = _Hh3cevtPowerSupplySTD180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 5)
)
_Hh3cevtPowerSupplyPOE24Port_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyPOE24Port = _Hh3cevtPowerSupplyPOE24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 6)
)
_Hh3cevtPowerSupplyPOE48Port_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyPOE48Port = _Hh3cevtPowerSupplyPOE48Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 7)
)
_Hh3cevtFan_ObjectIdentity = ObjectIdentity
hh3cevtFan = _Hh3cevtFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7)
)
_Hh3cevtHotSwapFan_ObjectIdentity = ObjectIdentity
hh3cevtHotSwapFan = _Hh3cevtHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 1)
)
_Hh3cevtNonHotSwapFan_ObjectIdentity = ObjectIdentity
hh3cevtNonHotSwapFan = _Hh3cevtNonHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 2)
)
_Hh3cevtSensor_ObjectIdentity = ObjectIdentity
hh3cevtSensor = _Hh3cevtSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8)
)
_Hh3cevtSensorTemperature_ObjectIdentity = ObjectIdentity
hh3cevtSensorTemperature = _Hh3cevtSensorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8, 1)
)
_Hh3cevtSensorVoltage_ObjectIdentity = ObjectIdentity
hh3cevtSensorVoltage = _Hh3cevtSensorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8, 2)
)
_Hh3cevtSensorFanSpeed_ObjectIdentity = ObjectIdentity
hh3cevtSensorFanSpeed = _Hh3cevtSensorFanSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8, 3)
)
_Hh3cevtModule_ObjectIdentity = ObjectIdentity
hh3cevtModule = _Hh3cevtModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9)
)
_Hh3cevtModuleUnknownCard_ObjectIdentity = ObjectIdentity
hh3cevtModuleUnknownCard = _Hh3cevtModuleUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 1)
)
_Hh3cevtModuleCommonCards_ObjectIdentity = ObjectIdentity
hh3cevtModuleCommonCards = _Hh3cevtModuleCommonCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2)
)
_Hh3cevtModuleRouterType_ObjectIdentity = ObjectIdentity
hh3cevtModuleRouterType = _Hh3cevtModuleRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3)
)
_Hh3cevtModuleRt_As_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_As = _Hh3cevtModuleRt_As_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 2)
)
_Hh3cevtModuleRt_Sa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa = _Hh3cevtModuleRt_Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 3)
)
_Hh3cevtModuleRt_Bi_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Bi = _Hh3cevtModuleRt_Bi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 4)
)
_Hh3cevtModuleRt_E12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E12 = _Hh3cevtModuleRt_E12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5)
)
_Hh3cevtModuleRt_E14_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E14 = _Hh3cevtModuleRt_E14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 6)
)
_Hh3cevtModuleRt_Fe1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1 = _Hh3cevtModuleRt_Fe1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 7)
)
_Hh3cevtModuleRt_E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E1 = _Hh3cevtModuleRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 8)
)
_Hh3cevtModuleRt_Fe2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe2 = _Hh3cevtModuleRt_Fe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 9)
)
_Hh3cevtModuleRt_Vi2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Vi2 = _Hh3cevtModuleRt_Vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 11)
)
_Hh3cevtModuleRt_Vi4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Vi4 = _Hh3cevtModuleRt_Vi4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 12)
)
_Hh3cevtModuleRt_Vi30_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Vi30 = _Hh3cevtModuleRt_Vi30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 13)
)
_Hh3cevtModuleRt_S1b_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_S1b = _Hh3cevtModuleRt_S1b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 14)
)
_Hh3cevtModuleRt_Sa2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa2 = _Hh3cevtModuleRt_Sa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 15)
)
_Hh3cevtModuleRt_As16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_As16 = _Hh3cevtModuleRt_As16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 16)
)
_Hh3cevtModuleRt_New8as_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_New8as = _Hh3cevtModuleRt_New8as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 17)
)
_Hh3cevtModuleRt_Sa1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa1 = _Hh3cevtModuleRt_Sa1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 18)
)
_Hh3cevtModuleRt_Fxs2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxs2 = _Hh3cevtModuleRt_Fxs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 19)
)
_Hh3cevtModuleRt_Fxo2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxo2 = _Hh3cevtModuleRt_Fxo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 20)
)
_Hh3cevtModuleRt_Em2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Em2 = _Hh3cevtModuleRt_Em2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 21)
)
_Hh3cevtModuleRt_Fxs4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxs4 = _Hh3cevtModuleRt_Fxs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 22)
)
_Hh3cevtModuleRt_Fxo4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxo4 = _Hh3cevtModuleRt_Fxo4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 23)
)
_Hh3cevtModuleRt_Em4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Em4 = _Hh3cevtModuleRt_Em4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 24)
)
_Hh3cevtModuleRt_Sab_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sab = _Hh3cevtModuleRt_Sab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 25)
)
_Hh3cevtModuleRt_E1vi_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E1vi = _Hh3cevtModuleRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 26)
)
_Hh3cevtModuleRt_Am12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Am12 = _Hh3cevtModuleRt_Am12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 27)
)
_Hh3cevtModuleRt_Am6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Am6 = _Hh3cevtModuleRt_Am6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 28)
)
_Hh3cevtModuleRt_Ndec_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ndec = _Hh3cevtModuleRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 29)
)
_Hh3cevtModuleRt_Newsa2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Newsa2 = _Hh3cevtModuleRt_Newsa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 30)
)
_Hh3cevtModuleRt_Aux_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Aux = _Hh3cevtModuleRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 31)
)
_Hh3cevtModuleRt_Console_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Console = _Hh3cevtModuleRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 32)
)
_Hh3cevtModuleRt_Sic_wan_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_wan = _Hh3cevtModuleRt_Sic_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 33)
)
_Hh3cevtModuleRt_Sic_1fe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1fe = _Hh3cevtModuleRt_Sic_1fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 34)
)
_Hh3cevtModuleRt_Sic_1sa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1sa = _Hh3cevtModuleRt_Sic_1sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 35)
)
_Hh3cevtModuleRt_Sic_3as_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_3as = _Hh3cevtModuleRt_Sic_3as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 36)
)
_Hh3cevtModuleRt_Sic_1e1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1e1 = _Hh3cevtModuleRt_Sic_1e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 37)
)
_Hh3cevtModuleRt_Sic_1t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1t1 = _Hh3cevtModuleRt_Sic_1t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 38)
)
_Hh3cevtModuleRt_Sic_1bu_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1bu = _Hh3cevtModuleRt_Sic_1bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 39)
)
_Hh3cevtModuleRt_Sic_2bu_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2bu = _Hh3cevtModuleRt_Sic_2bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 40)
)
_Hh3cevtModuleRt_Sic_1bs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1bs = _Hh3cevtModuleRt_Sic_1bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 41)
)
_Hh3cevtModuleRt_Sic_2bs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2bs = _Hh3cevtModuleRt_Sic_2bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 42)
)
_Hh3cevtModuleRt_Sic_1am_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1am = _Hh3cevtModuleRt_Sic_1am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 43)
)
_Hh3cevtModuleRt_Sic_2am_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2am = _Hh3cevtModuleRt_Sic_2am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 44)
)
_Hh3cevtModuleRt_Sic_1em_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1em = _Hh3cevtModuleRt_Sic_1em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 45)
)
_Hh3cevtModuleRt_Sic_2em_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2em = _Hh3cevtModuleRt_Sic_2em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 46)
)
_Hh3cevtModuleRt_Sic_1fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1fxs = _Hh3cevtModuleRt_Sic_1fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 47)
)
_Hh3cevtModuleRt_Sic_2fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2fxs = _Hh3cevtModuleRt_Sic_2fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 48)
)
_Hh3cevtModuleRt_Sic_1fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1fxo = _Hh3cevtModuleRt_Sic_1fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 49)
)
_Hh3cevtModuleRt_Sic_2fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2fxo = _Hh3cevtModuleRt_Sic_2fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 50)
)
_Hh3cevtModuleRt_Fcm6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fcm6 = _Hh3cevtModuleRt_Fcm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 51)
)
_Hh3cevtModuleRt_Sa8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa8 = _Hh3cevtModuleRt_Sa8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 52)
)
_Hh3cevtModuleRt_T11_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T11 = _Hh3cevtModuleRt_T11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 53)
)
_Hh3cevtModuleRt_T12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T12 = _Hh3cevtModuleRt_T12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 54)
)
_Hh3cevtModuleRt_T14_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T14 = _Hh3cevtModuleRt_T14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 55)
)
_Hh3cevtModuleRt_T1vi_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T1vi = _Hh3cevtModuleRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 56)
)
_Hh3cevtModuleRt_Fcm4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fcm4 = _Hh3cevtModuleRt_Fcm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 57)
)
_Hh3cevtModuleRt_Fcm2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fcm2 = _Hh3cevtModuleRt_Fcm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 58)
)
_Hh3cevtModuleRt_Rtb21ce3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Rtb21ce3 = _Hh3cevtModuleRt_Rtb21ce3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 59)
)
_Hh3cevtModuleRt_Ame6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ame6 = _Hh3cevtModuleRt_Ame6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 60)
)
_Hh3cevtModuleRt_Ame12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ame12 = _Hh3cevtModuleRt_Ame12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 61)
)
_Hh3cevtModuleRt_E11_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E11_f = _Hh3cevtModuleRt_E11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 65)
)
_Hh3cevtModuleRt_E12_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E12_f = _Hh3cevtModuleRt_E12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 66)
)
_Hh3cevtModuleRt_E14_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E14_f = _Hh3cevtModuleRt_E14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 67)
)
_Hh3cevtModuleRt_T11_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T11_f = _Hh3cevtModuleRt_T11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 68)
)
_Hh3cevtModuleRt_T12_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T12_f = _Hh3cevtModuleRt_T12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 69)
)
_Hh3cevtModuleRt_T14_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T14_f = _Hh3cevtModuleRt_T14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 70)
)
_Hh3cevtModuleRt_E11_f_17_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E11_f_17 = _Hh3cevtModuleRt_E11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 71)
)
_Hh3cevtModuleRt_T11_f_17_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T11_f_17 = _Hh3cevtModuleRt_T11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 72)
)
_Hh3cevtModuleRt_Rtb21ct3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Rtb21ct3 = _Hh3cevtModuleRt_Rtb21ct3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 73)
)
_Hh3cevtModuleRt_Atmadsl1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmadsl1 = _Hh3cevtModuleRt_Atmadsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 74)
)
_Hh3cevtModuleRt_Atmadsl2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmadsl2 = _Hh3cevtModuleRt_Atmadsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 75)
)
_Hh3cevtModuleRt_Atm155m_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m = _Hh3cevtModuleRt_Atm155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 76)
)
_Hh3cevtModuleRt_Ase8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ase8 = _Hh3cevtModuleRt_Ase8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 77)
)
_Hh3cevtModuleRt_Ase16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ase16 = _Hh3cevtModuleRt_Ase16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 78)
)
_Hh3cevtModuleRt_Sae4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sae4 = _Hh3cevtModuleRt_Sae4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 79)
)
_Hh3cevtModuleRt_Sae2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sae2 = _Hh3cevtModuleRt_Sae2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 80)
)
_Hh3cevtModuleRt_Atmshdsl1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmshdsl1 = _Hh3cevtModuleRt_Atmshdsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 90)
)
_Hh3cevtModuleRt_Atmshdsl2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmshdsl2 = _Hh3cevtModuleRt_Atmshdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 91)
)
_Hh3cevtModuleRt_Atmshdsl4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmshdsl4 = _Hh3cevtModuleRt_Atmshdsl4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 92)
)
_Hh3cevtModuleRt_Atm25m_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm25m = _Hh3cevtModuleRt_Atm25m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 93)
)
_Hh3cevtModuleRt_Atme3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atme3 = _Hh3cevtModuleRt_Atme3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 94)
)
_Hh3cevtModuleRt_Atmt3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmt3 = _Hh3cevtModuleRt_Atmt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 95)
)
_Hh3cevtModuleRt_Xdsl_fec_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_fec = _Hh3cevtModuleRt_Xdsl_fec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 96)
)
_Hh3cevtModuleRt_Xdsl_adsl_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_adsl = _Hh3cevtModuleRt_Xdsl_adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 97)
)
_Hh3cevtModuleRt_Xdsl_gshdsl_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_gshdsl = _Hh3cevtModuleRt_Xdsl_gshdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 98)
)
_Hh3cevtModuleRt_Xdsl_bri_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_bri = _Hh3cevtModuleRt_Xdsl_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 99)
)
_Hh3cevtModuleRt_Xdsl_scc_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_scc = _Hh3cevtModuleRt_Xdsl_scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 100)
)
_Hh3cevtModuleRt_Ge1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge1 = _Hh3cevtModuleRt_Ge1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 101)
)
_Hh3cevtModuleRt_Pos155m_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Pos155m = _Hh3cevtModuleRt_Pos155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 102)
)
_Hh3cevtModuleRt_Cpos_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Cpos = _Hh3cevtModuleRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 103)
)
_Hh3cevtModuleRt_Fe1op_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1op = _Hh3cevtModuleRt_Fe1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 104)
)
_Hh3cevtModuleRt_Sae8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sae8 = _Hh3cevtModuleRt_Sae8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 105)
)
_Hh3cevtModuleRt_Atm155m_mm_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m_mm = _Hh3cevtModuleRt_Atm155m_mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 106)
)
_Hh3cevtModuleRt_Atm155m_sm_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m_sm = _Hh3cevtModuleRt_Atm155m_sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 107)
)
_Hh3cevtModuleRt_Atm155m_sml_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m_sml = _Hh3cevtModuleRt_Atm155m_sml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 108)
)
_Hh3cevtModuleRt_Fe1op_sfx_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1op_sfx = _Hh3cevtModuleRt_Fe1op_sfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 109)
)
_Hh3cevtModuleRt_Fe1op_mfx_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1op_mfx = _Hh3cevtModuleRt_Fe1op_mfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 110)
)
_Hh3cevtModuleRt_Cpos_t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Cpos_t1 = _Hh3cevtModuleRt_Cpos_t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 111)
)
_Hh3cevtModuleRt_Ge1op_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge1op = _Hh3cevtModuleRt_Ge1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 112)
)
_Hh3cevtModuleRt_Ge2op_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge2op = _Hh3cevtModuleRt_Ge2op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 113)
)
_Hh3cevtModuleRt_Ge2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge2 = _Hh3cevtModuleRt_Ge2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 114)
)
_Hh3cevtModuleRt_Fix_1wan_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fix_1wan = _Hh3cevtModuleRt_Fix_1wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 115)
)
_Hh3cevtModuleRt_Fix_1sae_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fix_1sae = _Hh3cevtModuleRt_Fix_1sae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 116)
)
_Hh3cevtModuleRt_Cavium_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Cavium = _Hh3cevtModuleRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 117)
)
_Hh3cevtModuleRt_Sic1Eth_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic1Eth = _Hh3cevtModuleRt_Sic1Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 118)
)
_Hh3cevtModuleRt_atm1ADSLI_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atm1ADSLI = _Hh3cevtModuleRt_atm1ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 119)
)
_Hh3cevtModuleRt_atm2ADSLI_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atm2ADSLI = _Hh3cevtModuleRt_atm2ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 120)
)
_Hh3cevtModuleRt_fix_e11_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fix_e11 = _Hh3cevtModuleRt_fix_e11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 121)
)
_Hh3cevtModuleRt_fix_t11_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fix_t11 = _Hh3cevtModuleRt_fix_t11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 122)
)
_Hh3cevtModuleRt_e18_75_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e18_75 = _Hh3cevtModuleRt_e18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 123)
)
_Hh3cevtModuleRt_e18_120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e18_120 = _Hh3cevtModuleRt_e18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 124)
)
_Hh3cevtModuleRt_t18_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_t18 = _Hh3cevtModuleRt_t18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 125)
)
_Hh3cevtModuleRt_sic_1vifxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1vifxs = _Hh3cevtModuleRt_sic_1vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 126)
)
_Hh3cevtModuleRt_sic_1vifxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1vifxo = _Hh3cevtModuleRt_sic_1vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 127)
)
_Hh3cevtModuleRt_sic_2vifxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_2vifxs = _Hh3cevtModuleRt_sic_2vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 128)
)
_Hh3cevtModuleRt_sic_2vifxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_2vifxo = _Hh3cevtModuleRt_sic_2vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 129)
)
_Hh3cevtModuleRt_xdsl_fec_new_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_xdsl_fec_new = _Hh3cevtModuleRt_xdsl_fec_new_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 130)
)
_Hh3cevtModuleRt_xdsl_sa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_xdsl_sa = _Hh3cevtModuleRt_xdsl_sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 131)
)
_Hh3cevtModuleRt_bs4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bs4 = _Hh3cevtModuleRt_bs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 132)
)
_Hh3cevtModuleRt_ima_8e175_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_8e175 = _Hh3cevtModuleRt_ima_8e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 133)
)
_Hh3cevtModuleRt_ima_8e1120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_8e1120 = _Hh3cevtModuleRt_ima_8e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 134)
)
_Hh3cevtModuleRt_ima_4e175_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_4e175 = _Hh3cevtModuleRt_ima_4e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 135)
)
_Hh3cevtModuleRt_ima_4e1120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_4e1120 = _Hh3cevtModuleRt_ima_4e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 136)
)
_Hh3cevtModuleRt_ima_8t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_8t1 = _Hh3cevtModuleRt_ima_8t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 137)
)
_Hh3cevtModuleRt_ima_4t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_4t1 = _Hh3cevtModuleRt_ima_4t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 138)
)
_Hh3cevtModuleRt_sic_1t1f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1t1f = _Hh3cevtModuleRt_sic_1t1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 139)
)
_Hh3cevtModuleRt_sic_1e1f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1e1f = _Hh3cevtModuleRt_sic_1e1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 140)
)
_Hh3cevtModuleRt_VG_16fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_16fxs = _Hh3cevtModuleRt_VG_16fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 141)
)
_Hh3cevtModuleRt_VG_32fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_32fxs = _Hh3cevtModuleRt_VG_32fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 142)
)
_Hh3cevtModuleRt_VG_8fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_8fxo = _Hh3cevtModuleRt_VG_8fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 143)
)
_Hh3cevtModuleRt_VG_2fe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_2fe = _Hh3cevtModuleRt_VG_2fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 144)
)
_Hh3cevtModuleRt_sib_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sib = _Hh3cevtModuleRt_sib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 145)
)
_Hh3cevtModuleRt_cie32_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cie32 = _Hh3cevtModuleRt_cie32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 146)
)
_Hh3cevtModuleRt_cie64_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cie64 = _Hh3cevtModuleRt_cie64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 147)
)
_Hh3cevtModuleRt_cie96_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cie96 = _Hh3cevtModuleRt_cie96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 148)
)
_Hh3cevtModuleRt_Fe4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe4 = _Hh3cevtModuleRt_Fe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 149)
)
_Hh3cevtModuleRt_fxs4fxo1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fxs4fxo1 = _Hh3cevtModuleRt_fxs4fxo1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 150)
)
_Hh3cevtModuleRt_atm1shdsl4wire_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atm1shdsl4wire = _Hh3cevtModuleRt_atm1shdsl4wire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 151)
)
_Hh3cevtModuleRt_atmIma4shdsl_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atmIma4shdsl = _Hh3cevtModuleRt_atmIma4shdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 152)
)
_Hh3cevtModuleRt_ls4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ls4 = _Hh3cevtModuleRt_ls4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 153)
)
_Hh3cevtModuleRt_ls8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ls8 = _Hh3cevtModuleRt_ls8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 154)
)
_Hh3cevtModuleRt_ls16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ls16 = _Hh3cevtModuleRt_ls16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 155)
)
_Hh3cevtModuleRt_sic_adls2plus_isdn_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_adls2plus_isdn = _Hh3cevtModuleRt_sic_adls2plus_isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 156)
)
_Hh3cevtModuleRt_sic_adls2plus_pots_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_adls2plus_pots = _Hh3cevtModuleRt_sic_adls2plus_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 157)
)
_Hh3cevtModuleRt_ft3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ft3 = _Hh3cevtModuleRt_ft3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 158)
)
_Hh3cevtModuleRt_ce32_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ce32 = _Hh3cevtModuleRt_ce32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 159)
)
_Hh3cevtModuleRt_bsv2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bsv2 = _Hh3cevtModuleRt_bsv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 160)
)
_Hh3cevtModuleRt_bsv4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bsv4 = _Hh3cevtModuleRt_bsv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 161)
)
_Hh3cevtModuleRt_RPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU = _Hh3cevtModuleRt_RPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 162)
)
_Hh3cevtModuleRt_ERPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ERPU = _Hh3cevtModuleRt_ERPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 163)
)
_Hh3cevtModuleRt_SSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SSL = _Hh3cevtModuleRt_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 164)
)
_Hh3cevtModuleRt_NSA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSA = _Hh3cevtModuleRt_NSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 165)
)
_Hh3cevtModuleRT_SIC_1GEC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1GEC = _Hh3cevtModuleRT_SIC_1GEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 200)
)
_Hh3cevtModuleRT_24FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_24FSW = _Hh3cevtModuleRT_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 201)
)
_Hh3cevtModuleRT_24FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_24FSWP = _Hh3cevtModuleRT_24FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 202)
)
_Hh3cevtModuleRT_16FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_16FSW = _Hh3cevtModuleRT_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 203)
)
_Hh3cevtModuleRT_16FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_16FSWP = _Hh3cevtModuleRT_16FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 204)
)
_Hh3cevtModuleRT_1VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1VE1 = _Hh3cevtModuleRT_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 205)
)
_Hh3cevtModuleRT_1VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1VT1 = _Hh3cevtModuleRT_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 206)
)
_Hh3cevtModuleRT_2VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_2VE1 = _Hh3cevtModuleRT_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 207)
)
_Hh3cevtModuleRT_2VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_2VT1 = _Hh3cevtModuleRT_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 208)
)
_Hh3cevtModuleRT_SIC_4FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_4FSW = _Hh3cevtModuleRT_SIC_4FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 209)
)
_Hh3cevtModuleRT_SIC_4FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_4FSWP = _Hh3cevtModuleRT_SIC_4FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 210)
)
_Hh3cevtModuleRT_DSIC_9FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_DSIC_9FSW = _Hh3cevtModuleRT_DSIC_9FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 211)
)
_Hh3cevtModuleRT_DSIC_9FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_DSIC_9FSWP = _Hh3cevtModuleRT_DSIC_9FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 212)
)
_Hh3cevtModuleRT_SIC_1VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1VE1 = _Hh3cevtModuleRT_SIC_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 213)
)
_Hh3cevtModuleRT_SIC_1VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1VT1 = _Hh3cevtModuleRT_SIC_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 214)
)
_Hh3cevtModuleRT_VCPM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VCPM = _Hh3cevtModuleRT_VCPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 215)
)
_Hh3cevtModuleRT_VPM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPM = _Hh3cevtModuleRT_VPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 216)
)
_Hh3cevtModuleRT_VPMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPMA = _Hh3cevtModuleRT_VPMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 217)
)
_Hh3cevtModuleRT_VPMB_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPMB = _Hh3cevtModuleRT_VPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 218)
)
_Hh3cevtModuleRT_VPMC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPMC = _Hh3cevtModuleRT_VPMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 219)
)
_Hh3cevtModuleRt_fe18_75_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fe18_75 = _Hh3cevtModuleRt_fe18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 220)
)
_Hh3cevtModuleRt_fe18_120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fe18_120 = _Hh3cevtModuleRt_fe18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 221)
)
_Hh3cevtModuleRt_ft18_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ft18 = _Hh3cevtModuleRt_ft18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 222)
)
_Hh3cevtModuleRt_CF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CF = _Hh3cevtModuleRt_CF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 223)
)
_Hh3cevtModuleRt_bsv2_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bsv2_v2 = _Hh3cevtModuleRt_bsv2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 224)
)
_Hh3cevtModuleRt_e1vi1_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e1vi1_v2 = _Hh3cevtModuleRt_e1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 225)
)
_Hh3cevtModuleRt_e1vi2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e1vi2 = _Hh3cevtModuleRt_e1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 226)
)
_Hh3cevtModuleRt_t1vi1_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_t1vi1_v2 = _Hh3cevtModuleRt_t1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 227)
)
_Hh3cevtModuleRt_t1vi2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_t1vi2 = _Hh3cevtModuleRt_t1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 228)
)
_Hh3cevtModuleRt_osm_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_osm = _Hh3cevtModuleRt_osm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 229)
)
_Hh3cevtModuleRt_sd707_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sd707 = _Hh3cevtModuleRt_sd707_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 230)
)
_Hh3cevtModuleRt_dm_epri_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_dm_epri = _Hh3cevtModuleRt_dm_epri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 231)
)
_Hh3cevtModuleRt_dm_tpri_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_dm_tpri = _Hh3cevtModuleRt_dm_tpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 232)
)
_Hh3cevtModuleRt_ERPU_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ERPU_H = _Hh3cevtModuleRt_ERPU_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 233)
)
_Hh3cevtModuleRT_SIC_1BSV_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1BSV = _Hh3cevtModuleRT_SIC_1BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 234)
)
_Hh3cevtModuleRT_SIC_2BSV_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_2BSV = _Hh3cevtModuleRT_SIC_2BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 235)
)
_Hh3cevtModuleRt_gbe8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_gbe8 = _Hh3cevtModuleRt_gbe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 236)
)
_Hh3cevtModuleRt_gbe4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_gbe4 = _Hh3cevtModuleRt_gbe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 237)
)
_Hh3cevtModuleRt_cpos2_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cpos2_v2 = _Hh3cevtModuleRt_cpos2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 238)
)
_Hh3cevtModuleRt_cpos1_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cpos1_v2 = _Hh3cevtModuleRt_cpos1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 239)
)
_Hh3cevtModuleRt_oap_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_oap = _Hh3cevtModuleRt_oap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 240)
)
_Hh3cevtModuleRT_48FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_48FSWP = _Hh3cevtModuleRT_48FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 241)
)
_Hh3cevtModuleRT_48FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_48FSW = _Hh3cevtModuleRT_48FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 242)
)
_Hh3cevtModuleRT_ASM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_ASM = _Hh3cevtModuleRT_ASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 243)
)
_Hh3cevtModuleRT_SIC_1FEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1FEF = _Hh3cevtModuleRT_SIC_1FEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 244)
)
_Hh3cevtModuleRT_XMIM_24FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_XMIM_24FSW = _Hh3cevtModuleRT_XMIM_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 245)
)
_Hh3cevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WLAN_AG_1RADIO = _Hh3cevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 246)
)
_Hh3cevtModuleRT_1CE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1CE3 = _Hh3cevtModuleRT_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 247)
)
_Hh3cevtModuleRT_XMIM_16FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_XMIM_16FSW = _Hh3cevtModuleRT_XMIM_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 248)
)
_Hh3cevtModuleRT_OAPS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS = _Hh3cevtModuleRT_OAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 249)
)
_Hh3cevtModuleRT_NAM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_NAM = _Hh3cevtModuleRT_NAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 250)
)
_Hh3cevtModuleRT_RPE_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_RPE_X1 = _Hh3cevtModuleRT_RPE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 251)
)
_Hh3cevtModuleRT_FIP_100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_FIP_100 = _Hh3cevtModuleRT_FIP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 252)
)
_Hh3cevtModuleRT_FIP_200_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_FIP_200 = _Hh3cevtModuleRT_FIP_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 253)
)
_Hh3cevtModuleRT_SIC_8AS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_8AS = _Hh3cevtModuleRT_SIC_8AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 254)
)
_Hh3cevtModuleRT_WAAM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WAAM = _Hh3cevtModuleRT_WAAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 255)
)
_Hh3cevtModuleRt_msp4p_OC3c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_msp4p_OC3c = _Hh3cevtModuleRt_msp4p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 256)
)
_Hh3cevtModuleRt_1pos_oc48_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_1pos_oc48 = _Hh3cevtModuleRt_1pos_oc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 257)
)
_Hh3cevtModuleRt_xgbe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_xgbe = _Hh3cevtModuleRt_xgbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 258)
)
_Hh3cevtModuleRT_EADM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_EADM = _Hh3cevtModuleRT_EADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 259)
)
_Hh3cevtModuleRT_VCM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VCM = _Hh3cevtModuleRT_VCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 260)
)
_Hh3cevtModuleRT_SIC_2FXS1FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_2FXS1FXO = _Hh3cevtModuleRT_SIC_2FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 261)
)
_Hh3cevtModuleRT_8FXS8FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_8FXS8FXO = _Hh3cevtModuleRT_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 262)
)
_Hh3cevtModuleRT_16FXS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_16FXS = _Hh3cevtModuleRT_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 263)
)
_Hh3cevtModuleRT_OAPS_ICM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS_ICM = _Hh3cevtModuleRT_OAPS_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 264)
)
_Hh3cevtModuleRT_OAP_ICM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAP_ICM = _Hh3cevtModuleRT_OAP_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 265)
)
_Hh3cevtModuleRT_8fe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_8fe = _Hh3cevtModuleRT_8fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 266)
)
_Hh3cevtModuleRT_4gbp_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_4gbp = _Hh3cevtModuleRT_4gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 267)
)
_Hh3cevtModuleRT_MPU_G2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MPU_G2 = _Hh3cevtModuleRT_MPU_G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 268)
)
_Hh3cevtModuleRT_OAPS_OCE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS_OCE = _Hh3cevtModuleRT_OAPS_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 269)
)
_Hh3cevtModuleRT_OAP_OCE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAP_OCE = _Hh3cevtModuleRT_OAP_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 270)
)
_Hh3cevtModuleRT_OAPS_ICE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS_ICE = _Hh3cevtModuleRT_OAPS_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 271)
)
_Hh3cevtModuleRT_OAP_ICE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAP_ICE = _Hh3cevtModuleRT_OAP_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 272)
)
_Hh3cevtModuleRT_SIC_16AS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_16AS = _Hh3cevtModuleRT_SIC_16AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 273)
)
_Hh3cevtModuleRT_SPE_FWM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SPE_FWM = _Hh3cevtModuleRT_SPE_FWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 274)
)
_Hh3cevtModuleRT_cls2p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_cls2p = _Hh3cevtModuleRT_cls2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 275)
)
_Hh3cevtModuleRT_cls1p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_cls1p = _Hh3cevtModuleRT_cls1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 276)
)
_Hh3cevtModuleRT_SIC_2E1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_2E1_F = _Hh3cevtModuleRT_SIC_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 277)
)
_Hh3cevtModuleRT_SIC_1E1_F_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1E1_F_V2 = _Hh3cevtModuleRT_SIC_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 278)
)
_Hh3cevtModuleRT_MCU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MCU = _Hh3cevtModuleRT_MCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 279)
)
_Hh3cevtModuleRT_ACU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_ACU = _Hh3cevtModuleRT_ACU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 280)
)
_Hh3cevtModuleRT_1ATM_OC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1ATM_OC3 = _Hh3cevtModuleRT_1ATM_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 281)
)
_Hh3cevtModuleRT_RSE_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_RSE_X1 = _Hh3cevtModuleRT_RSE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 282)
)
_Hh3cevtModuleRT_FIP_210_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_FIP_210 = _Hh3cevtModuleRT_FIP_210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 283)
)
_Hh3cevtModuleRT_1expa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1expa = _Hh3cevtModuleRT_1expa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 284)
)
_Hh3cevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WLAN_SIC_N_1RADIO = _Hh3cevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 285)
)
_Hh3cevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WLAN_SIC_BG_1RADIO = _Hh3cevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 286)
)
_Hh3cevtModuleRT_al2p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_al2p = _Hh3cevtModuleRT_al2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 287)
)
_Hh3cevtModuleRT_msp2p_OC3c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_msp2p_OC3c = _Hh3cevtModuleRT_msp2p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 288)
)
_Hh3cevtModuleRT_8gbp_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_8gbp = _Hh3cevtModuleRT_8gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 289)
)
_Hh3cevtModuleRT_SIC_EPON_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_EPON = _Hh3cevtModuleRT_SIC_EPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 290)
)
_Hh3cevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_3G_GSM_H3 = _Hh3cevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 291)
)
_Hh3cevtModuleRT_msp2p_OC12c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_msp2p_OC12c = _Hh3cevtModuleRT_msp2p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 292)
)
_Hh3cevtModuleRt_msp4p_OC12c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_msp4p_OC12c = _Hh3cevtModuleRt_msp4p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 293)
)
_Hh3cevtModuleRt_al1p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_al1p = _Hh3cevtModuleRt_al1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 294)
)
_Hh3cevtModuleRt_OAP_100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_OAP_100 = _Hh3cevtModuleRt_OAP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 295)
)
_Hh3cevtModuleRt_FIP_110_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_110 = _Hh3cevtModuleRt_FIP_110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 296)
)
_Hh3cevtModuleRt_OSM_SSM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_OSM_SSM = _Hh3cevtModuleRt_OSM_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 297)
)
_Hh3cevtModuleRt_OAP_SSM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_OAP_SSM = _Hh3cevtModuleRt_OAP_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 298)
)
_Hh3cevtModuleRt_rs2p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_rs2p = _Hh3cevtModuleRt_rs2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 299)
)
_Hh3cevtModuleRt_SAP_48GBE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_48GBE = _Hh3cevtModuleRt_SAP_48GBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 300)
)
_Hh3cevtModuleRt_SAP_48GBP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_48GBP = _Hh3cevtModuleRt_SAP_48GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 301)
)
_Hh3cevtModuleRt_SAP_24GBP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_24GBP = _Hh3cevtModuleRt_SAP_24GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 302)
)
_Hh3cevtModuleRt_SPE_SSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPE_SSL = _Hh3cevtModuleRt_SPE_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 303)
)
_Hh3cevtModuleRt_SIC_AUDIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_AUDIO = _Hh3cevtModuleRt_SIC_AUDIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 304)
)
_Hh3cevtModuleRt_FIC_1E1POS_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIC_1E1POS_H3 = _Hh3cevtModuleRt_FIC_1E1POS_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 305)
)
_Hh3cevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DSIC_4FXS1FXO = _Hh3cevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 306)
)
_Hh3cevtModuleRt_FIC_CPOS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIC_CPOS = _Hh3cevtModuleRt_FIC_CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 307)
)
_Hh3cevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DSIC_1SHDSL_8W = _Hh3cevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 308)
)
_Hh3cevtModuleRt_SIC_3G_TD_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_TD = _Hh3cevtModuleRt_SIC_3G_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 309)
)
_Hh3cevtModuleRt_SIC_3G_CDMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_CDMA = _Hh3cevtModuleRt_SIC_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 310)
)
_Hh3cevtModuleRt_SIC_3G_HSPA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_HSPA = _Hh3cevtModuleRt_SIC_3G_HSPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 311)
)
_Hh3cevtModuleRt_FIC_OAP_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIC_OAP_V2 = _Hh3cevtModuleRt_FIC_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 312)
)
_Hh3cevtModuleRt_MIM_OAP_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_OAP_V2 = _Hh3cevtModuleRt_MIM_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 313)
)
_Hh3cevtModuleRt_MIM_OAPS_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_OAPS_V2 = _Hh3cevtModuleRt_MIM_OAPS_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 314)
)
_Hh3cevtModuleRt_IPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU = _Hh3cevtModuleRt_IPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 400)
)
_Hh3cevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM2GEBE_PCIE = _Hh3cevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 401)
)
_Hh3cevtModuleRt_HIM12GE_PCIE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM12GE_PCIE = _Hh3cevtModuleRt_HIM12GE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 402)
)
_Hh3cevtModuleRt_HIM2XGE_PCIE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM2XGE_PCIE = _Hh3cevtModuleRt_HIM2XGE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 403)
)
_Hh3cevtModuleRt_IPU_T1000_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU_T1000_M = _Hh3cevtModuleRt_IPU_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 404)
)
_Hh3cevtModuleRt_IPU_GX4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU_GX4C = _Hh3cevtModuleRt_IPU_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 405)
)
_Hh3cevtModuleRt_IPU_GT4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU_GT4C = _Hh3cevtModuleRt_IPU_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 406)
)
_Hh3cevtModuleRt_RPU_IAG2000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU_IAG2000_A = _Hh3cevtModuleRt_RPU_IAG2000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 407)
)
_Hh3cevtModuleRt_RPU_AFD1000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU_AFD1000_A = _Hh3cevtModuleRt_RPU_AFD1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 408)
)
_Hh3cevtModuleRt_RPU_F5000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU_F5000_A = _Hh3cevtModuleRt_RPU_F5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 409)
)
_Hh3cevtModuleRt_ACG_8800S3_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ACG_8800S3_MPU = _Hh3cevtModuleRt_ACG_8800S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 410)
)
_Hh3cevtModuleRt_T5000S3_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T5000S3_MPU = _Hh3cevtModuleRt_T5000S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 411)
)
_Hh3cevtModuleRt_NS21S2MSPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS21S2MSPB0 = _Hh3cevtModuleRt_NS21S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 412)
)
_Hh3cevtModuleRt_NS11S2MSPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS11S2MSPB0 = _Hh3cevtModuleRt_NS11S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 413)
)
_Hh3cevtModuleRt_NSQ1WLAN_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1WLAN = _Hh3cevtModuleRt_NSQ1WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 414)
)
_Hh3cevtModuleRt_NSQ1GP4U0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GP4U0 = _Hh3cevtModuleRt_NSQ1GP4U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 415)
)
_Hh3cevtModuleRt_NSQ1GP8C40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GP8C40 = _Hh3cevtModuleRt_NSQ1GP8C40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 416)
)
_Hh3cevtModuleRt_NSQ1XS2U0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1XS2U0 = _Hh3cevtModuleRt_NSQ1XS2U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 417)
)
_Hh3cevtModuleRt_VG_8fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_8fxs = _Hh3cevtModuleRt_VG_8fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 600)
)
_Hh3cevtModuleRt_VG_24fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_24fxs = _Hh3cevtModuleRt_VG_24fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 601)
)
_Hh3cevtModuleRt_VG_24fxs24fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_24fxs24fxo = _Hh3cevtModuleRt_VG_24fxs24fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 602)
)
_Hh3cevtModuleRt_VG_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_MPU = _Hh3cevtModuleRt_VG_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 603)
)
_Hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C = _Hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 604)
)
_Hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C = _Hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 605)
)
_Hh3cevtModuleRt_MIM_VCX_3C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_VCX_3C = _Hh3cevtModuleRt_MIM_VCX_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 606)
)
_HpevtModuleRt_SIC_EPRI_ObjectIdentity = ObjectIdentity
hpevtModuleRt_SIC_EPRI = _HpevtModuleRt_SIC_EPRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5000)
)
_HpevtModuleRt_MIM_1E1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_V2 = _HpevtModuleRt_MIM_1E1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5001)
)
_HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_F_V2 = _HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5002)
)
_HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_2E1_F_V2 = _HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5003)
)
_HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_4E1_F_V2 = _HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5004)
)
_HpevtModuleRt_MIM_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75 = _HpevtModuleRt_MIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5005)
)
_HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75_F = _HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5006)
)
_HpevtModuleRt_MIM_8T1_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1 = _HpevtModuleRt_MIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5007)
)
_HpevtModuleRt_MIM_8T1_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1_F = _HpevtModuleRt_MIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5008)
)
_HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_IMA_8E1_75 = _HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5009)
)
_HpevtModuleRt_FIC_2E1_V3_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_2E1_V3 = _HpevtModuleRt_FIC_2E1_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5010)
)
_HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_IMA_8T1_V2 = _HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5011)
)
_Hh3cevtModuleSwitchType_ObjectIdentity = ObjectIdentity
hh3cevtModuleSwitchType = _Hh3cevtModuleSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4)
)
_Hh3cevtModuleSw_10OR100M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_10OR100M = _Hh3cevtModuleSw_10OR100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM = _Hh3cevtModuleSw_1000BASE_LX_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2)
)
_Hh3cevtModuleSw_1000BASE_SX_MM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_SX_MM = _Hh3cevtModuleSw_1000BASE_SX_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 3)
)
_Hh3cevtModuleSw_1000BASE_TX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_TX = _Hh3cevtModuleSw_1000BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 4)
)
_Hh3cevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_SINGLEMODE_FX = _Hh3cevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 5)
)
_Hh3cevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_MULTIMODE_FX = _Hh3cevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 6)
)
_Hh3cevtModuleSw_100M_100BASE_TX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_100BASE_TX = _Hh3cevtModuleSw_100M_100BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 7)
)
_Hh3cevtModuleSw_100M_HUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_HUB = _Hh3cevtModuleSw_100M_HUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 8)
)
_Hh3cevtModuleSw_VDSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_VDSL = _Hh3cevtModuleSw_VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 9)
)
_Hh3cevtModuleSw_STACK_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_STACK = _Hh3cevtModuleSw_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 10)
)
_Hh3cevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_ZENITH_FX = _Hh3cevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 11)
)
_Hh3cevtModuleSw_1000BASE_LONG_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LONG_FX = _Hh3cevtModuleSw_1000BASE_LONG_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 12)
)
_Hh3cevtModuleSw_ADSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ADSL = _Hh3cevtModuleSw_ADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 13)
)
_Hh3cevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_4T10OR100_4FX100SM = _Hh3cevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 14)
)
_Hh3cevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_4T10OR100_4FX100MM = _Hh3cevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 15)
)
_Hh3cevtModuleSw_VSPL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_VSPL = _Hh3cevtModuleSw_VSPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 16)
)
_Hh3cevtModuleSw_ASPL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ASPL = _Hh3cevtModuleSw_ASPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 17)
)
_Hh3cevtModuleSw_1000M_SFP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000M_SFP = _Hh3cevtModuleSw_1000M_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 18)
)
_Hh3cevtModuleSw_LS82O2CM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82O2CM = _Hh3cevtModuleSw_LS82O2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 19)
)
_Hh3cevtModuleSw_LS82P2CM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82P2CM = _Hh3cevtModuleSw_LS82P2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 20)
)
_Hh3cevtModuleSw_LS82O4GM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82O4GM = _Hh3cevtModuleSw_LS82O4GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 21)
)
_Hh3cevtModuleSw_LS82GB4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GB4C = _Hh3cevtModuleSw_LS82GB4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 22)
)
_Hh3cevtModuleSw_LS82GT4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GT4C = _Hh3cevtModuleSw_LS82GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 23)
)
_Hh3cevtModuleSw_LS82ST4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82ST4C = _Hh3cevtModuleSw_LS82ST4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 24)
)
_Hh3cevtModuleSw_BOARD_LS82DSPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82DSPU = _Hh3cevtModuleSw_BOARD_LS82DSPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 25)
)
_Hh3cevtModuleSw_BOARD_LS81GP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81GP8U = _Hh3cevtModuleSw_BOARD_LS81GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 26)
)
_Hh3cevtModuleSw_BOARD_LS82GT20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82GT20 = _Hh3cevtModuleSw_BOARD_LS82GT20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 27)
)
_Hh3cevtModuleSw_BOARD_LS82FE48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82FE48 = _Hh3cevtModuleSw_BOARD_LS82FE48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 28)
)
_Hh3cevtModuleSw_LS82T24B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82T24B = _Hh3cevtModuleSw_LS82T24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 29)
)
_Hh3cevtModuleSw_LSB1SRPA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRPA = _Hh3cevtModuleSw_LSB1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 30)
)
_Hh3cevtModuleSw_LSB1FT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FT48A = _Hh3cevtModuleSw_LSB1FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 31)
)
_Hh3cevtModuleSw_LSB1FT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FT48B = _Hh3cevtModuleSw_LSB1FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 32)
)
_Hh3cevtModuleSw_LSB1F48GA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F48GA = _Hh3cevtModuleSw_LSB1F48GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 33)
)
_Hh3cevtModuleSw_LSB1F48GB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F48GB = _Hh3cevtModuleSw_LSB1F48GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 34)
)
_Hh3cevtModuleSw_LSB1FP20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20A = _Hh3cevtModuleSw_LSB1FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 35)
)
_Hh3cevtModuleSw_LSB1FP20B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20B = _Hh3cevtModuleSw_LSB1FP20B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 36)
)
_Hh3cevtModuleSw_FT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FT48A = _Hh3cevtModuleSw_FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 37)
)
_Hh3cevtModuleSw_GP4U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP4U = _Hh3cevtModuleSw_GP4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 38)
)
_Hh3cevtModuleSw_GP2U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP2U = _Hh3cevtModuleSw_GP2U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 39)
)
_Hh3cevtModuleSw_TGX1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_TGX1A = _Hh3cevtModuleSw_TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 40)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM_IR_SC = _Hh3cevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 41)
)
_Hh3cevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_SX_MM_SR_SC = _Hh3cevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 42)
)
_Hh3cevtModuleSw_1000BASE_T_RJ45_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_T_RJ45 = _Hh3cevtModuleSw_1000BASE_T_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 43)
)
_Hh3cevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100BASE_FX_SM_IR_SC = _Hh3cevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 44)
)
_Hh3cevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100BASE_FX_MM_SR_SC = _Hh3cevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 45)
)
_Hh3cevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GIGA_STACK_1M_PC = _Hh3cevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 46)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC = _Hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 47)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM_LR_LC = _Hh3cevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 48)
)
_Hh3cevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100BASE_FX_SM_LR_SC = _Hh3cevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 49)
)
_Hh3cevtModuleSw_1000BASE_X_GBIC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_X_GBIC = _Hh3cevtModuleSw_1000BASE_X_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 50)
)
_Hh3cevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_SINGLEMODE_FX_LC = _Hh3cevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 51)
)
_Hh3cevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_MULTIMODE_FX_LC = _Hh3cevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 52)
)
_Hh3cevtModuleSw_1000BASE_4SFP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_4SFP = _Hh3cevtModuleSw_1000BASE_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 53)
)
_Hh3cevtModuleSw_1000BASE_4GBIC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_4GBIC = _Hh3cevtModuleSw_1000BASE_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 54)
)
_Hh3cevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_4SFP = _Hh3cevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 55)
)
_Hh3cevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_4GBIC = _Hh3cevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 56)
)
_Hh3cevtModuleSw_LSB1GP12A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12A = _Hh3cevtModuleSw_LSB1GP12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 57)
)
_Hh3cevtModuleSw_LSB1GP12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12B = _Hh3cevtModuleSw_LSB1GP12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 58)
)
_Hh3cevtModuleSw_LSB1TGX1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1TGX1A = _Hh3cevtModuleSw_LSB1TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 59)
)
_Hh3cevtModuleSw_LSB1TGX1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1TGX1B = _Hh3cevtModuleSw_LSB1TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 60)
)
_Hh3cevtModuleSw_LSB1P4G8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8A = _Hh3cevtModuleSw_LSB1P4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 61)
)
_Hh3cevtModuleSw_LSB1P4G8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8B = _Hh3cevtModuleSw_LSB1P4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 62)
)
_Hh3cevtModuleSw_LSB1A4G8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1A4G8A = _Hh3cevtModuleSw_LSB1A4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 63)
)
_Hh3cevtModuleSw_LSB1A4G8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1A4G8B = _Hh3cevtModuleSw_LSB1A4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 64)
)
_Hh3cevtModuleSw_FT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FT48C = _Hh3cevtModuleSw_FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 65)
)
_Hh3cevtModuleSw_FP20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FP20 = _Hh3cevtModuleSw_FP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 66)
)
_Hh3cevtModuleSw_BOARD_LS81FT48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81FT48 = _Hh3cevtModuleSw_BOARD_LS81FT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 67)
)
_Hh3cevtModuleSw_BOARD_LS81GB8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81GB8U = _Hh3cevtModuleSw_BOARD_LS81GB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 68)
)
_Hh3cevtModuleSw_BOARD_LS81GT8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81GT8U = _Hh3cevtModuleSw_BOARD_LS81GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 69)
)
_Hh3cevtModuleSw_BOARD_LS81FS24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81FS24 = _Hh3cevtModuleSw_BOARD_LS81FS24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 70)
)
_Hh3cevtModuleSw_BOARD_LS81FM24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81FM24 = _Hh3cevtModuleSw_BOARD_LS81FM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 71)
)
_Hh3cevtModuleSw_BOARD_LS82GP20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82GP20 = _Hh3cevtModuleSw_BOARD_LS82GP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 72)
)
_Hh3cevtModuleSw_LSB1SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRPB = _Hh3cevtModuleSw_LSB1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 73)
)
_Hh3cevtModuleSw_LSB1F32GA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GA = _Hh3cevtModuleSw_LSB1F32GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 74)
)
_Hh3cevtModuleSw_LSB1F32GB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GB = _Hh3cevtModuleSw_LSB1F32GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 75)
)
_Hh3cevtModuleSw_LSB2FT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48A = _Hh3cevtModuleSw_LSB2FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 76)
)
_Hh3cevtModuleSw_LSB2FT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48B = _Hh3cevtModuleSw_LSB2FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 77)
)
_Hh3cevtModuleSw_LSB1GT12A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12A = _Hh3cevtModuleSw_LSB1GT12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 78)
)
_Hh3cevtModuleSw_LSB1GT12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12B = _Hh3cevtModuleSw_LSB1GT12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 79)
)
_Hh3cevtModuleSw_PC4U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PC4U = _Hh3cevtModuleSw_PC4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 80)
)
_Hh3cevtModuleSw_FT32A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FT32A = _Hh3cevtModuleSw_FT32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 81)
)
_Hh3cevtModuleSw_GT4U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GT4U = _Hh3cevtModuleSw_GT4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 82)
)
_Hh3cevtModuleSw_BOARD_LS83FP20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS83FP20A = _Hh3cevtModuleSw_BOARD_LS83FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 83)
)
_Hh3cevtModuleSw_BOARD_LS82HGMU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82HGMU = _Hh3cevtModuleSw_BOARD_LS82HGMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 84)
)
_Hh3cevtModuleSw_LSB1GP8TB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP8TB = _Hh3cevtModuleSw_LSB1GP8TB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 85)
)
_Hh3cevtModuleSw_LSB1GP8TC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP8TC = _Hh3cevtModuleSw_LSB1GP8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 86)
)
_Hh3cevtModuleSw_LSB1GT8PB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT8PB = _Hh3cevtModuleSw_LSB1GT8PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 87)
)
_Hh3cevtModuleSw_LSB1GT8PC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT8PC = _Hh3cevtModuleSw_LSB1GT8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 88)
)
_Hh3cevtModuleSw_LSB1FT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FT48C = _Hh3cevtModuleSw_LSB1FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 89)
)
_Hh3cevtModuleSw_LSB1FP20C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20C = _Hh3cevtModuleSw_LSB1FP20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 90)
)
_Hh3cevtModuleSw_LSB1F32GC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GC = _Hh3cevtModuleSw_LSB1F32GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 91)
)
_Hh3cevtModuleSw_LSB1GT12C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12C = _Hh3cevtModuleSw_LSB1GT12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 92)
)
_Hh3cevtModuleSw_LSB1GP12C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12C = _Hh3cevtModuleSw_LSB1GP12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 93)
)
_Hh3cevtModuleSw_LSB1P4G8C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8C = _Hh3cevtModuleSw_LSB1P4G8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 94)
)
_Hh3cevtModuleSw_LSB1TGX1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1TGX1C = _Hh3cevtModuleSw_LSB1TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 95)
)
_Hh3cevtModuleSw_LSB1GT24B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24B = _Hh3cevtModuleSw_LSB1GT24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 96)
)
_Hh3cevtModuleSw_LSB1GT24C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24C = _Hh3cevtModuleSw_LSB1GT24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 97)
)
_Hh3cevtModuleSw_LSB1GP24B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24B = _Hh3cevtModuleSw_LSB1GP24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 98)
)
_Hh3cevtModuleSw_LSB1GP24C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24C = _Hh3cevtModuleSw_LSB1GP24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 99)
)
_Hh3cevtModuleSw_LSB1XP2B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2B = _Hh3cevtModuleSw_LSB1XP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 100)
)
_Hh3cevtModuleSw_LSB1XP2C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2C = _Hh3cevtModuleSw_LSB1XP2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 101)
)
_Hh3cevtModuleSw_LSB1GV48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48B = _Hh3cevtModuleSw_LSB1GV48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 102)
)
_Hh3cevtModuleSw_LSB1GV48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48C = _Hh3cevtModuleSw_LSB1GV48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 103)
)
_Hh3cevtModuleSw_LSB1SRPC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRPC = _Hh3cevtModuleSw_LSB1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 104)
)
_Hh3cevtModuleSw_LSB1SRP1N0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N0 = _Hh3cevtModuleSw_LSB1SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 105)
)
_Hh3cevtModuleSw_LSB1SRP1N1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N1 = _Hh3cevtModuleSw_LSB1SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 106)
)
_Hh3cevtModuleSw_LSB1SRP1N2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N2 = _Hh3cevtModuleSw_LSB1SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 107)
)
_Hh3cevtModuleSw_GT24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GT24 = _Hh3cevtModuleSw_GT24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 108)
)
_Hh3cevtModuleSw_GP24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP24 = _Hh3cevtModuleSw_GP24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 109)
)
_Hh3cevtModuleSw_XP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_XP2 = _Hh3cevtModuleSw_XP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 110)
)
_Hh3cevtModuleSw_GV48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GV48 = _Hh3cevtModuleSw_GV48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 111)
)
_Hh3cevtModuleSw_LSG1GP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1GP8U = _Hh3cevtModuleSw_LSG1GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 112)
)
_Hh3cevtModuleSw_LSG1GT8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1GT8U = _Hh3cevtModuleSw_LSG1GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 113)
)
_Hh3cevtModuleSw_LSG1TG1U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1TG1U = _Hh3cevtModuleSw_LSG1TG1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 114)
)
_Hh3cevtModuleSw_LSG1TD1U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1TD1U = _Hh3cevtModuleSw_LSG1TD1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 115)
)
_Hh3cevtModuleSw_LSB2FT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48C = _Hh3cevtModuleSw_LSB2FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 116)
)
_Hh3cevtModuleSw_LSB1GT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT48B = _Hh3cevtModuleSw_LSB1GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 117)
)
_Hh3cevtModuleSw_LSB1GT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT48C = _Hh3cevtModuleSw_LSB1GT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 118)
)
_Hh3cevtModuleSw_LS81GT48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48 = _Hh3cevtModuleSw_LS81GT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 119)
)
_Hh3cevtModuleSw_LS81SRPG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG0 = _Hh3cevtModuleSw_LS81SRPG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 120)
)
_Hh3cevtModuleSw_LS81SRPG1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG1 = _Hh3cevtModuleSw_LS81SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 121)
)
_Hh3cevtModuleSw_LS81SRPG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG2 = _Hh3cevtModuleSw_LS81SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 122)
)
_Hh3cevtModuleSw_LS81SRPG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG3 = _Hh3cevtModuleSw_LS81SRPG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 123)
)
_Hh3cevtModuleSw_SR01SRPUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUB = _Hh3cevtModuleSw_SR01SRPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 125)
)
_Hh3cevtModuleSw_SR01SRPUA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUA = _Hh3cevtModuleSw_SR01SRPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 126)
)
_Hh3cevtModuleSw_SR01GP12L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12L = _Hh3cevtModuleSw_SR01GP12L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 127)
)
_Hh3cevtModuleSw_SR01GP12W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12W = _Hh3cevtModuleSw_SR01GP12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 128)
)
_Hh3cevtModuleSw_SR01FT48L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FT48L = _Hh3cevtModuleSw_SR01FT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 129)
)
_Hh3cevtModuleSw_SR01FT48W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FT48W = _Hh3cevtModuleSw_SR01FT48W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 130)
)
_Hh3cevtModuleSw_SR01XK1W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XK1W = _Hh3cevtModuleSw_SR01XK1W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 131)
)
_Hh3cevtModuleSw_SR01FP20W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FP20W = _Hh3cevtModuleSw_SR01FP20W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 132)
)
_Hh3cevtModuleSw_SR01GT12W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT12W = _Hh3cevtModuleSw_SR01GT12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 133)
)
_Hh3cevtModuleSw_SR01F32GL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01F32GL = _Hh3cevtModuleSw_SR01F32GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 134)
)
_Hh3cevtModuleSw_SR01F32GW_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01F32GW = _Hh3cevtModuleSw_SR01F32GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 135)
)
_Hh3cevtModuleSw_SR01GT8PL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT8PL = _Hh3cevtModuleSw_SR01GT8PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 136)
)
_Hh3cevtModuleSw_SR01GT8PW_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT8PW = _Hh3cevtModuleSw_SR01GT8PW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 137)
)
_Hh3cevtModuleSw_SR01P4G8W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01P4G8W = _Hh3cevtModuleSw_SR01P4G8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 138)
)
_Hh3cevtModuleSw_LSA1FP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSA1FP8U = _Hh3cevtModuleSw_LSA1FP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 139)
)
_Hh3cevtModuleSw_LSB1SP4B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SP4B = _Hh3cevtModuleSw_LSB1SP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 140)
)
_Hh3cevtModuleSw_LSB1SP4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SP4C = _Hh3cevtModuleSw_LSB1SP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 141)
)
_Hh3cevtModuleSw_LSB1UP1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1UP1B = _Hh3cevtModuleSw_LSB1UP1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 142)
)
_Hh3cevtModuleSw_LSB1UP1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1UP1C = _Hh3cevtModuleSw_LSB1UP1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 143)
)
_Hh3cevtModuleSw_LSB1XP4B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4B = _Hh3cevtModuleSw_LSB1XP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 144)
)
_Hh3cevtModuleSw_LSB1XP4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4C = _Hh3cevtModuleSw_LSB1XP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 145)
)
_Hh3cevtModuleSw_SP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SP4 = _Hh3cevtModuleSw_SP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 146)
)
_Hh3cevtModuleSw_UP1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_UP1 = _Hh3cevtModuleSw_UP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 147)
)
_Hh3cevtModuleSw_XP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_XP4 = _Hh3cevtModuleSw_XP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 148)
)
_Hh3cevtModuleSw_LS81VSNP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81VSNP = _Hh3cevtModuleSw_LS81VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 149)
)
_Hh3cevtModuleSw_LS81T12P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T12P = _Hh3cevtModuleSw_LS81T12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 150)
)
_Hh3cevtModuleSw_LS81P12T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81P12T = _Hh3cevtModuleSw_LS81P12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 151)
)
_Hh3cevtModuleSw_LS81GP8UB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP8UB = _Hh3cevtModuleSw_LS81GP8UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 152)
)
_Hh3cevtModuleSw_LS81FT48E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FT48E = _Hh3cevtModuleSw_LS81FT48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 153)
)
_Hh3cevtModuleSw_LS81GP4UB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP4UB = _Hh3cevtModuleSw_LS81GP4UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 154)
)
_Hh3cevtModuleSw_LS81GT8UE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT8UE = _Hh3cevtModuleSw_LS81GT8UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 155)
)
_Hh3cevtModuleSw_LS81GT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48A = _Hh3cevtModuleSw_LS81GT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 156)
)
_Hh3cevtModuleSw_LS81FP48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FP48 = _Hh3cevtModuleSw_LS81FP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 157)
)
_Hh3cevtModuleSw_LSB1XK1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1B = _Hh3cevtModuleSw_LSB1XK1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 158)
)
_Hh3cevtModuleSw_LSB1XK1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1C = _Hh3cevtModuleSw_LSB1XK1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 159)
)
_Hh3cevtModuleSw_SR01SRPUC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUC = _Hh3cevtModuleSw_SR01SRPUC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 160)
)
_Hh3cevtModuleSw_SR01SRPUD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUD = _Hh3cevtModuleSw_SR01SRPUD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 161)
)
_Hh3cevtModuleSw_SR01SRPUE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUE = _Hh3cevtModuleSw_SR01SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 162)
)
_Hh3cevtModuleSw_LSB1SRP1N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N3 = _Hh3cevtModuleSw_LSB1SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 163)
)
_Hh3cevtModuleSw_LSB1VP2B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VP2B = _Hh3cevtModuleSw_LSB1VP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 164)
)
_Hh3cevtModuleSw_LSB1NATB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1NATB = _Hh3cevtModuleSw_LSB1NATB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 165)
)
_Hh3cevtModuleSw_LSB1VPNB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VPNB = _Hh3cevtModuleSw_LSB1VPNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 166)
)
_Hh3cevtModuleSw_LSGP8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSGP8P = _Hh3cevtModuleSw_LSGP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 167)
)
_Hh3cevtModuleSw_LSXK1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXK1P = _Hh3cevtModuleSw_LSXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 168)
)
_Hh3cevtModuleSw_LSXP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXP2P = _Hh3cevtModuleSw_LSXP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 169)
)
_Hh3cevtModuleSw_LS81FT48F_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FT48F = _Hh3cevtModuleSw_LS81FT48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 170)
)
_Hh3cevtModuleSw_LS81PT8G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81PT8G = _Hh3cevtModuleSw_LS81PT8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 171)
)
_Hh3cevtModuleSw_LS81PT4G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81PT4G = _Hh3cevtModuleSw_LS81PT4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 172)
)
_Hh3cevtModuleSw_LSSTK24G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSSTK24G = _Hh3cevtModuleSw_LSSTK24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 173)
)
_Hh3cevtModuleSw_LS82GT20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GT20A = _Hh3cevtModuleSw_LS82GT20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 174)
)
_Hh3cevtModuleSw_LS82GP20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GP20A = _Hh3cevtModuleSw_LS82GP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 175)
)
_Hh3cevtModuleSw_LS81TGX1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX1C = _Hh3cevtModuleSw_LS81TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 176)
)
_Hh3cevtModuleSw_VP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_VP2 = _Hh3cevtModuleSw_VP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 177)
)
_Hh3cevtModuleSw_LSA1FB8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSA1FB8U = _Hh3cevtModuleSw_LSA1FB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 178)
)
_Hh3cevtModuleSw_LS81T12PE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T12PE = _Hh3cevtModuleSw_LS81T12PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 179)
)
_Hh3cevtModuleSw_LS81P12TE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81P12TE = _Hh3cevtModuleSw_LS81P12TE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 180)
)
_Hh3cevtModuleSw_LSB1SRP2N0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N0 = _Hh3cevtModuleSw_LSB1SRP2N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 181)
)
_Hh3cevtModuleSw_LSB1SRP2N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N3 = _Hh3cevtModuleSw_LSB1SRP2N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 182)
)
_Hh3cevtModuleSw_LSB1GV48DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48DB = _Hh3cevtModuleSw_LSB1GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 183)
)
_Hh3cevtModuleSw_LSB1FW8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FW8B = _Hh3cevtModuleSw_LSB1FW8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 184)
)
_Hh3cevtModuleSw_LSB1IPSEC8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPSEC8B = _Hh3cevtModuleSw_LSB1IPSEC8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 185)
)
_Hh3cevtModuleSw_LSB1IDSB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IDSB = _Hh3cevtModuleSw_LSB1IDSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 186)
)
_Hh3cevtModuleSw_LSB1IPSB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPSB = _Hh3cevtModuleSw_LSB1IPSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 187)
)
_Hh3cevtModuleSw_LSB2FT48CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48CA = _Hh3cevtModuleSw_LSB2FT48CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 188)
)
_Hh3cevtModuleSw_LSB1FP20CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20CA = _Hh3cevtModuleSw_LSB1FP20CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 189)
)
_Hh3cevtModuleSw_LSB1F32GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GCA = _Hh3cevtModuleSw_LSB1F32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 190)
)
_Hh3cevtModuleSw_LSB1P4G8CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8CA = _Hh3cevtModuleSw_LSB1P4G8CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 191)
)
_Hh3cevtModuleSw_LSB1GT12CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12CA = _Hh3cevtModuleSw_LSB1GT12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 192)
)
_Hh3cevtModuleSw_LSB1GT24CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24CA = _Hh3cevtModuleSw_LSB1GT24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 193)
)
_Hh3cevtModuleSw_LSB1GP12CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12CA = _Hh3cevtModuleSw_LSB1GP12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 194)
)
_Hh3cevtModuleSw_LSB1GP24CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24CA = _Hh3cevtModuleSw_LSB1GP24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 195)
)
_Hh3cevtModuleSw_LSB1GT8PCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT8PCA = _Hh3cevtModuleSw_LSB1GT8PCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 196)
)
_Hh3cevtModuleSw_LSB1XP2CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2CA = _Hh3cevtModuleSw_LSB1XP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 197)
)
_Hh3cevtModuleSw_LSB1XK1CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1CA = _Hh3cevtModuleSw_LSB1XK1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 198)
)
_Hh3cevtModuleSw_LSB1XP4CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4CA = _Hh3cevtModuleSw_LSB1XP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 199)
)
_Hh3cevtModuleSw_LSB1UP1CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1UP1CA = _Hh3cevtModuleSw_LSB1UP1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 200)
)
_Hh3cevtModuleSw_LSB1SP4CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SP4CA = _Hh3cevtModuleSw_LSB1SP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 201)
)
_Hh3cevtModuleSw_LSB1VP2CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VP2CA = _Hh3cevtModuleSw_LSB1VP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 202)
)
_Hh3cevtModuleSw_SR01FT48WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FT48WA = _Hh3cevtModuleSw_SR01FT48WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 203)
)
_Hh3cevtModuleSw_SR01FP20WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FP20WA = _Hh3cevtModuleSw_SR01FP20WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 204)
)
_Hh3cevtModuleSw_SR01F32GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01F32GWA = _Hh3cevtModuleSw_SR01F32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 205)
)
_Hh3cevtModuleSw_SR01P4G8WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01P4G8WA = _Hh3cevtModuleSw_SR01P4G8WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 206)
)
_Hh3cevtModuleSw_SR01GT12WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT12WA = _Hh3cevtModuleSw_SR01GT12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 207)
)
_Hh3cevtModuleSw_SR01GT24WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT24WA = _Hh3cevtModuleSw_SR01GT24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 208)
)
_Hh3cevtModuleSw_SR01GP12WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12WA = _Hh3cevtModuleSw_SR01GP12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 209)
)
_Hh3cevtModuleSw_SR01GP24WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP24WA = _Hh3cevtModuleSw_SR01GP24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 210)
)
_Hh3cevtModuleSw_SR01GT8PWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT8PWA = _Hh3cevtModuleSw_SR01GT8PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 211)
)
_Hh3cevtModuleSw_SR01XP2WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP2WA = _Hh3cevtModuleSw_SR01XP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 212)
)
_Hh3cevtModuleSw_SR01XK1WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XK1WA = _Hh3cevtModuleSw_SR01XK1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 213)
)
_Hh3cevtModuleSw_SR01UP1WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01UP1WA = _Hh3cevtModuleSw_SR01UP1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 214)
)
_Hh3cevtModuleSw_SR01SP4WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SP4WA = _Hh3cevtModuleSw_SR01SP4WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 215)
)
_Hh3cevtModuleSw_GP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP8U = _Hh3cevtModuleSw_GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 216)
)
_Hh3cevtModuleSw_LSEXP1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSEXP1P = _Hh3cevtModuleSw_LSEXP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 217)
)
_Hh3cevtModuleSw_LSEXK1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSEXK1P = _Hh3cevtModuleSw_LSEXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 218)
)
_Hh3cevtModuleSw_LSEXS1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSEXS1P = _Hh3cevtModuleSw_LSEXS1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 219)
)
_Hh3cevtModuleSw_LS81GP48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP48 = _Hh3cevtModuleSw_LS81GP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 220)
)
_Hh3cevtModuleSw_LS81GT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48B = _Hh3cevtModuleSw_LS81GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 221)
)
_Hh3cevtModuleSw_LS81T16P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T16P = _Hh3cevtModuleSw_LS81T16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 222)
)
_Hh3cevtModuleSw_LS81T32P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T32P = _Hh3cevtModuleSw_LS81T32P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 223)
)
_Hh3cevtModuleSw_LS81TGX2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX2 = _Hh3cevtModuleSw_LS81TGX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 224)
)
_Hh3cevtModuleSw_LS81TGX4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX4 = _Hh3cevtModuleSw_LS81TGX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 225)
)
_Hh3cevtModuleSw_LSB1GV48DA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48DA = _Hh3cevtModuleSw_LSB1GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 226)
)
_Hh3cevtModuleSw_SR01GV48VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GV48VB = _Hh3cevtModuleSw_SR01GV48VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 227)
)
_Hh3cevtModuleSw_LSB1GT24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24DB = _Hh3cevtModuleSw_LSB1GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 228)
)
_Hh3cevtModuleSw_LSB1GP24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24DB = _Hh3cevtModuleSw_LSB1GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 229)
)
_Hh3cevtModuleSw_LSB1GP24DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24DC = _Hh3cevtModuleSw_LSB1GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 230)
)
_Hh3cevtModuleSw_LSB1FW8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FW8DB = _Hh3cevtModuleSw_LSB1FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 231)
)
_Hh3cevtModuleSw_LSB1IPSEC8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPSEC8DB = _Hh3cevtModuleSw_LSB1IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 232)
)
_Hh3cevtModuleSw_SR01GT24VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT24VB = _Hh3cevtModuleSw_SR01GT24VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 233)
)
_Hh3cevtModuleSw_SR01GP24VC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP24VC = _Hh3cevtModuleSw_SR01GP24VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 234)
)
_Hh3cevtModuleSw_SR01VP2WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01VP2WA = _Hh3cevtModuleSw_SR01VP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 235)
)
_Hh3cevtModuleSw_SR01FW8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FW8VB = _Hh3cevtModuleSw_SR01FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 236)
)
_Hh3cevtModuleSw_SR01IPSEC8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01IPSEC8VB = _Hh3cevtModuleSw_SR01IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 237)
)
_Hh3cevtModuleSw_SR01NATL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01NATL = _Hh3cevtModuleSw_SR01NATL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 238)
)
_Hh3cevtModuleSw_SR01VPNL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01VPNL = _Hh3cevtModuleSw_SR01VPNL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 239)
)
_Hh3cevtModuleSw_LSB1GP24CB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24CB = _Hh3cevtModuleSw_LSB1GP24CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 240)
)
_Hh3cevtModuleSw_LSB1GP48DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP48DB = _Hh3cevtModuleSw_LSB1GP48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 241)
)
_Hh3cevtModuleSw_LSB1XP2CB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2CB = _Hh3cevtModuleSw_LSB1XP2CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 242)
)
_Hh3cevtModuleSw_XP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_XP4L = _Hh3cevtModuleSw_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 243)
)
_Hh3cevtModuleSw_LSB1XP4LDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4LDB = _Hh3cevtModuleSw_LSB1XP4LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 244)
)
_Hh3cevtModuleSw_LSB1XP4LDC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4LDC = _Hh3cevtModuleSw_LSB1XP4LDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 245)
)
_Hh3cevtModuleSw_AHP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_AHP4 = _Hh3cevtModuleSw_AHP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 246)
)
_Hh3cevtModuleSw_LSB1AHP4GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1AHP4GCA = _Hh3cevtModuleSw_LSB1AHP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 247)
)
_Hh3cevtModuleSw_CLP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CLP4 = _Hh3cevtModuleSw_CLP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 248)
)
_Hh3cevtModuleSw_LSB1CLP4GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1CLP4GCA = _Hh3cevtModuleSw_LSB1CLP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 249)
)
_Hh3cevtModuleSw_ET32_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ET32 = _Hh3cevtModuleSw_ET32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 250)
)
_Hh3cevtModuleSw_LSB1ET32GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1ET32GCA = _Hh3cevtModuleSw_LSB1ET32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 251)
)
_Hh3cevtModuleSw_LSB1IDSDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IDSDB = _Hh3cevtModuleSw_LSB1IDSDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 252)
)
_Hh3cevtModuleSw_LSB1SRP2N1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N1 = _Hh3cevtModuleSw_LSB1SRP2N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 253)
)
_Hh3cevtModuleSw_BOARD_LS82SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82SRPB = _Hh3cevtModuleSw_BOARD_LS82SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 254)
)
_Hh3cevtModuleSw_BORAD_LS83SRPC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BORAD_LS83SRPC = _Hh3cevtModuleSw_BORAD_LS83SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 255)
)
_Hh3cevtModuleSw_Main_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_Main = _Hh3cevtModuleSw_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 256)
)
_Hh3cevtModuleSw_LSB1SRP2N2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N2 = _Hh3cevtModuleSw_LSB1SRP2N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 257)
)
_Hh3cevtModuleSw_LSB1NAMB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1NAMB = _Hh3cevtModuleSw_LSB1NAMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 258)
)
_Hh3cevtModuleSw_RSP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RSP2 = _Hh3cevtModuleSw_RSP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 259)
)
_Hh3cevtModuleSw_LSB1RSP2CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RSP2CA = _Hh3cevtModuleSw_LSB1RSP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 260)
)
_Hh3cevtModuleSw_SR01XP4LVC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP4LVC = _Hh3cevtModuleSw_SR01XP4LVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 261)
)
_Hh3cevtModuleSw_SR01AHP4GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01AHP4GWA = _Hh3cevtModuleSw_SR01AHP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 262)
)
_Hh3cevtModuleSw_SR01CLP4GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01CLP4GWA = _Hh3cevtModuleSw_SR01CLP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 263)
)
_Hh3cevtModuleSw_SR01ET32GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01ET32GWA = _Hh3cevtModuleSw_SR01ET32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 264)
)
_Hh3cevtModuleSw_SR01IDSVB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01IDSVB = _Hh3cevtModuleSw_SR01IDSVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 265)
)
_Hh3cevtModuleSw_SR01SRPUF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUF = _Hh3cevtModuleSw_SR01SRPUF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 266)
)
_Hh3cevtModuleSw_SR01NAML_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01NAML = _Hh3cevtModuleSw_SR01NAML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 267)
)
_Hh3cevtModuleSw_SR01RSP2WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01RSP2WA = _Hh3cevtModuleSw_SR01RSP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 268)
)
_Hh3cevtModuleSw_LSPM1XP1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM1XP1P = _Hh3cevtModuleSw_LSPM1XP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 269)
)
_Hh3cevtModuleSw_LSPM1XP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM1XP2P = _Hh3cevtModuleSw_LSPM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 270)
)
_Hh3cevtModuleSw_LSPM1CX2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM1CX2P = _Hh3cevtModuleSw_LSPM1CX2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 271)
)
_Hh3cevtModuleSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_STK_1000BASE_T = _Hh3cevtModuleSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 272)
)
_Hh3cevtModuleSw_LSB1SRP1M0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1M0 = _Hh3cevtModuleSw_LSB1SRP1M0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 300)
)
_Hh3cevtModuleSw_LSB1SRP1M1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1M1 = _Hh3cevtModuleSw_LSB1SRP1M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 301)
)
_Hh3cevtModuleSw_LSB1GP12DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12DB = _Hh3cevtModuleSw_LSB1GP12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 302)
)
_Hh3cevtModuleSw_LSB1GT12DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12DB = _Hh3cevtModuleSw_LSB1GT12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 303)
)
_Hh3cevtModuleSw_LSB1XK1DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1DB = _Hh3cevtModuleSw_LSB1XK1DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 304)
)
_Hh3cevtModuleSw_LSB1XP2DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2DB = _Hh3cevtModuleSw_LSB1XP2DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 305)
)
_Hh3cevtModuleSw_LSB1XP2DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2DC = _Hh3cevtModuleSw_LSB1XP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 306)
)
_Hh3cevtModuleSw_LSB1GT48LDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT48LDB = _Hh3cevtModuleSw_LSB1GT48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 307)
)
_Hh3cevtModuleSw_LSB1XP4TDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4TDB = _Hh3cevtModuleSw_LSB1XP4TDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 308)
)
_Hh3cevtModuleSw_LSB1XP4TDC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4TDC = _Hh3cevtModuleSw_LSB1XP4TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 309)
)
_Hh3cevtModuleSw_LSB1RSP2DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RSP2DC = _Hh3cevtModuleSw_LSB1RSP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 310)
)
_Hh3cevtModuleSw_LSB1VP2DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VP2DC = _Hh3cevtModuleSw_LSB1VP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 311)
)
_Hh3cevtModuleSw_LSB1XP4DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4DB = _Hh3cevtModuleSw_LSB1XP4DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 312)
)
_Hh3cevtModuleSw_LSB1SRP2E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E0 = _Hh3cevtModuleSw_LSB1SRP2E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 313)
)
_Hh3cevtModuleSw_LSB1SRP2E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E1 = _Hh3cevtModuleSw_LSB1SRP2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 314)
)
_Hh3cevtModuleSw_LSB1SRP2E2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E2 = _Hh3cevtModuleSw_LSB1SRP2E2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 315)
)
_Hh3cevtModuleSw_LSB1SRP2E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E3 = _Hh3cevtModuleSw_LSB1SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 316)
)
_Hh3cevtModuleSw_SR01SRPUQ_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUQ = _Hh3cevtModuleSw_SR01SRPUQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 317)
)
_Hh3cevtModuleSw_AHP1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_AHP1 = _Hh3cevtModuleSw_AHP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 318)
)
_Hh3cevtModuleSw_AHP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_AHP2 = _Hh3cevtModuleSw_AHP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 319)
)
_Hh3cevtModuleSw_CLP1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CLP1 = _Hh3cevtModuleSw_CLP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 320)
)
_Hh3cevtModuleSw_CLP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CLP2 = _Hh3cevtModuleSw_CLP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 321)
)
_Hh3cevtModuleSw_ET16_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ET16 = _Hh3cevtModuleSw_ET16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 322)
)
_Hh3cevtModuleSw_LSB1SRP1NA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA0 = _Hh3cevtModuleSw_LSB1SRP1NA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 323)
)
_Hh3cevtModuleSw_LSB1SRP1NA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA1 = _Hh3cevtModuleSw_LSB1SRP1NA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 324)
)
_Hh3cevtModuleSw_LSB1SRP1NA2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA2 = _Hh3cevtModuleSw_LSB1SRP1NA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 325)
)
_Hh3cevtModuleSw_LSB1SRP1NA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA3 = _Hh3cevtModuleSw_LSB1SRP1NA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 326)
)
_Hh3cevtModuleSw_SR01AHP1GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01AHP1GWA = _Hh3cevtModuleSw_SR01AHP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 327)
)
_Hh3cevtModuleSw_SR01AHP2GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01AHP2GWA = _Hh3cevtModuleSw_SR01AHP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 328)
)
_Hh3cevtModuleSw_SR01CLP1GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01CLP1GWA = _Hh3cevtModuleSw_SR01CLP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 329)
)
_Hh3cevtModuleSw_SR01CLP2GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01CLP2GWA = _Hh3cevtModuleSw_SR01CLP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 330)
)
_Hh3cevtModuleSw_SR01ET16GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01ET16GWA = _Hh3cevtModuleSw_SR01ET16GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 331)
)
_Hh3cevtModuleSw_SR01GP12VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12VB = _Hh3cevtModuleSw_SR01GP12VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 332)
)
_Hh3cevtModuleSw_SR01XK1VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XK1VB = _Hh3cevtModuleSw_SR01XK1VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 333)
)
_Hh3cevtModuleSw_SR01XP2VC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP2VC = _Hh3cevtModuleSw_SR01XP2VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 334)
)
_Hh3cevtModuleSw_SR01XP4LVB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP4LVB = _Hh3cevtModuleSw_SR01XP4LVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 335)
)
_Hh3cevtModuleSw_SR01SRPUEA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUEA = _Hh3cevtModuleSw_SR01SRPUEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 336)
)
_Hh3cevtModuleSw_LSB1SRP1N4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N4 = _Hh3cevtModuleSw_LSB1SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 337)
)
_Hh3cevtModuleSw_LSB1SRP1N5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N5 = _Hh3cevtModuleSw_LSB1SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 338)
)
_Hh3cevtModuleSw_LSB1SRP1N6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N6 = _Hh3cevtModuleSw_LSB1SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 339)
)
_Hh3cevtModuleSw_LSB1SRP1N7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N7 = _Hh3cevtModuleSw_LSB1SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 340)
)
_Hh3cevtModuleSw_LSB1SRP2N4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N4 = _Hh3cevtModuleSw_LSB1SRP2N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 341)
)
_Hh3cevtModuleSw_LSB1SRP2N5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N5 = _Hh3cevtModuleSw_LSB1SRP2N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 342)
)
_Hh3cevtModuleSw_LSB1SRP2N6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N6 = _Hh3cevtModuleSw_LSB1SRP2N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 343)
)
_Hh3cevtModuleSw_LSB1SRP2N7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N7 = _Hh3cevtModuleSw_LSB1SRP2N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 344)
)
_Hh3cevtModuleSw_LSB1SRP1NA4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA4 = _Hh3cevtModuleSw_LSB1SRP1NA4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 345)
)
_Hh3cevtModuleSw_LSB1SRP1NA5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA5 = _Hh3cevtModuleSw_LSB1SRP1NA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 346)
)
_Hh3cevtModuleSw_LSB1SRP1NA6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA6 = _Hh3cevtModuleSw_LSB1SRP1NA6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 347)
)
_Hh3cevtModuleSw_LSB1SRP1NA7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA7 = _Hh3cevtModuleSw_LSB1SRP1NA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 348)
)
_Hh3cevtModuleSw_LSB2GV48DA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GV48DA = _Hh3cevtModuleSw_LSB2GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 349)
)
_Hh3cevtModuleSw_LSB1RGP2GDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RGP2GDB = _Hh3cevtModuleSw_LSB1RGP2GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 350)
)
_Hh3cevtModuleSw_LSB1RGP4GDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RGP4GDB = _Hh3cevtModuleSw_LSB1RGP4GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 351)
)
_Hh3cevtModuleSw_LSB2GP24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GP24DB = _Hh3cevtModuleSw_LSB2GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 352)
)
_Hh3cevtModuleSw_LSB2GP24DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GP24DC = _Hh3cevtModuleSw_LSB2GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 353)
)
_Hh3cevtModuleSw_LSB2GT24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GT24DB = _Hh3cevtModuleSw_LSB2GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 354)
)
_Hh3cevtModuleSw_LSB2FW8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FW8DB = _Hh3cevtModuleSw_LSB2FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 355)
)
_Hh3cevtModuleSw_LSB2IPSEC8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2IPSEC8DB = _Hh3cevtModuleSw_LSB2IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 356)
)
_Hh3cevtModuleSw_LSB2GV48DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GV48DB = _Hh3cevtModuleSw_LSB2GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 357)
)
_Hh3cevtModuleSw_RGP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RGP2 = _Hh3cevtModuleSw_RGP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 358)
)
_Hh3cevtModuleSw_RGP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RGP4 = _Hh3cevtModuleSw_RGP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 359)
)
_Hh3cevtModuleSw_SR02FW8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02FW8VB = _Hh3cevtModuleSw_SR02FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 360)
)
_Hh3cevtModuleSw_SR02IPSEC8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02IPSEC8VB = _Hh3cevtModuleSw_SR02IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 361)
)
_Hh3cevtModuleSw_LSB2SRP1N0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N0 = _Hh3cevtModuleSw_LSB2SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 362)
)
_Hh3cevtModuleSw_LSB2SRP1N1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N1 = _Hh3cevtModuleSw_LSB2SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 363)
)
_Hh3cevtModuleSw_LSB2SRP1N2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N2 = _Hh3cevtModuleSw_LSB2SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 364)
)
_Hh3cevtModuleSw_LSB2SRP1N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N3 = _Hh3cevtModuleSw_LSB2SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 365)
)
_Hh3cevtModuleSw_LSB2SRP1N4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N4 = _Hh3cevtModuleSw_LSB2SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 366)
)
_Hh3cevtModuleSw_LSB2SRP1N5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N5 = _Hh3cevtModuleSw_LSB2SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 367)
)
_Hh3cevtModuleSw_LSB2SRP1N6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N6 = _Hh3cevtModuleSw_LSB2SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 368)
)
_Hh3cevtModuleSw_LSB2SRP1N7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N7 = _Hh3cevtModuleSw_LSB2SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 369)
)
_Hh3cevtModuleSw_SR02SRPUE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRPUE = _Hh3cevtModuleSw_SR02SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 370)
)
_Hh3cevtModuleSw_SR01LN1BQH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN1BQH0 = _Hh3cevtModuleSw_SR01LN1BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 371)
)
_Hh3cevtModuleSw_SR01DXP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DXP1L = _Hh3cevtModuleSw_SR01DXP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 372)
)
_Hh3cevtModuleSw_SR01DGP10L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DGP10L = _Hh3cevtModuleSw_SR01DGP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 373)
)
_Hh3cevtModuleSw_SR01DRSP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DRSP2L = _Hh3cevtModuleSw_SR01DRSP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 374)
)
_Hh3cevtModuleSw_SR01DRUP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DRUP1L = _Hh3cevtModuleSw_SR01DRUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 375)
)
_Hh3cevtModuleSw_SR01DGP20R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DGP20R = _Hh3cevtModuleSw_SR01DGP20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 376)
)
_Hh3cevtModuleSw_SR01DPLP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPLP8L = _Hh3cevtModuleSw_SR01DPLP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 377)
)
_Hh3cevtModuleSw_SR01DXP2R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DXP2R = _Hh3cevtModuleSw_SR01DXP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 378)
)
_Hh3cevtModuleSw_LSB1FW2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FW2A0 = _Hh3cevtModuleSw_LSB1FW2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 379)
)
_Hh3cevtModuleSw_LSB1GP48LDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP48LDB = _Hh3cevtModuleSw_LSB1GP48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 380)
)
_Hh3cevtModuleSw_SR01LN1BNA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN1BNA0 = _Hh3cevtModuleSw_SR01LN1BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 381)
)
_Hh3cevtModuleSw_SR01LN2BQH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN2BQH0 = _Hh3cevtModuleSw_SR01LN2BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 382)
)
_Hh3cevtModuleSw_SR01LN2BNA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN2BNA0 = _Hh3cevtModuleSw_SR01LN2BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 383)
)
_Hh3cevtModuleSw_SR01DGT20R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DGT20R = _Hh3cevtModuleSw_SR01DGT20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 384)
)
_Hh3cevtModuleSw_SR01DPSP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPSP4L = _Hh3cevtModuleSw_SR01DPSP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 385)
)
_Hh3cevtModuleSw_SR01DPUP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPUP1L = _Hh3cevtModuleSw_SR01DPUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 386)
)
_Hh3cevtModuleSw_SR01DPL2G6L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPL2G6L = _Hh3cevtModuleSw_SR01DPL2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 387)
)
_Hh3cevtModuleSw_SR01DPH2G6L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPH2G6L = _Hh3cevtModuleSw_SR01DPH2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 388)
)
_Hh3cevtModuleSw_SR01DPS2G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPS2G4L = _Hh3cevtModuleSw_SR01DPS2G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 389)
)
_Hh3cevtModuleSw_SR01DCL1G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DCL1G8L = _Hh3cevtModuleSw_SR01DCL1G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 390)
)
_Hh3cevtModuleSw_SR01DCL2G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DCL2G8L = _Hh3cevtModuleSw_SR01DCL2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 391)
)
_Hh3cevtModuleSw_SR01DET8G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DET8G8L = _Hh3cevtModuleSw_SR01DET8G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 392)
)
_Hh3cevtModuleSw_SR02SRP2E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP2E3 = _Hh3cevtModuleSw_SR02SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 393)
)
_Hh3cevtModuleSw_SR02SRP1E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP1E3 = _Hh3cevtModuleSw_SR02SRP1E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 394)
)
_Hh3cevtModuleSw_SR02SRP1M3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP1M3 = _Hh3cevtModuleSw_SR02SRP1M3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 395)
)
_Hh3cevtModuleSw_SR01DQCP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DQCP4L = _Hh3cevtModuleSw_SR01DQCP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 396)
)
_Hh3cevtModuleSw_SR01DTCP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DTCP8L = _Hh3cevtModuleSw_SR01DTCP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 397)
)
_Hh3cevtModuleSw_LSB1AFC1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1AFC1A0 = _Hh3cevtModuleSw_LSB1AFC1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 398)
)
_Hh3cevtModuleSw_LSB1SSL1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SSL1A0 = _Hh3cevtModuleSw_LSB1SSL1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 399)
)
_Hh3cevtModuleSw_IMNAM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMNAM = _Hh3cevtModuleSw_IMNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 400)
)
_Hh3cevtModuleSw_IMNAT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMNAT = _Hh3cevtModuleSw_IMNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 401)
)
_Hh3cevtModuleSw_PICAHP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICAHP1L = _Hh3cevtModuleSw_PICAHP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 402)
)
_Hh3cevtModuleSw_PICALP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICALP4L = _Hh3cevtModuleSw_PICALP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 403)
)
_Hh3cevtModuleSw_PICCHP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCHP4L = _Hh3cevtModuleSw_PICCHP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 404)
)
_Hh3cevtModuleSw_PICCHS1G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCHS1G4L = _Hh3cevtModuleSw_PICCHS1G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 405)
)
_Hh3cevtModuleSw_PICCLS4G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCLS4G4L = _Hh3cevtModuleSw_PICCLS4G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 406)
)
_Hh3cevtModuleSw_PICCSP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCSP1L = _Hh3cevtModuleSw_PICCSP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 407)
)
_Hh3cevtModuleSw_LSB1ACG1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1ACG1A0 = _Hh3cevtModuleSw_LSB1ACG1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 408)
)
_Hh3cevtModuleSw_LST1MRPNC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1MRPNC1 = _Hh3cevtModuleSw_LST1MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 409)
)
_Hh3cevtModuleSw_LST1SF18B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF18B1 = _Hh3cevtModuleSw_LST1SF18B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 410)
)
_Hh3cevtModuleSw_LST1SF08B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF08B1 = _Hh3cevtModuleSw_LST1SF08B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 411)
)
_Hh3cevtModuleSw_LST1GT48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEC1 = _Hh3cevtModuleSw_LST1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 412)
)
_Hh3cevtModuleSw_LST1GP48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEC1 = _Hh3cevtModuleSw_LST1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 413)
)
_Hh3cevtModuleSw_LST1XP4LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP4LEC1 = _Hh3cevtModuleSw_LST1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 414)
)
_Hh3cevtModuleSw_LST1XP8LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEC1 = _Hh3cevtModuleSw_LST1XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 415)
)
_Hh3cevtModuleSw_LSR1SRP2B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2B1 = _Hh3cevtModuleSw_LSR1SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 416)
)
_Hh3cevtModuleSw_LSR1SRP2C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2C1 = _Hh3cevtModuleSw_LSR1SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 417)
)
_Hh3cevtModuleSw_LSR1SRP2B2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2B2 = _Hh3cevtModuleSw_LSR1SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 418)
)
_Hh3cevtModuleSw_LSR1SRP2C2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2C2 = _Hh3cevtModuleSw_LSR1SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 419)
)
_Hh3cevtModuleSw_LSR1GT24LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GT24LEC1 = _Hh3cevtModuleSw_LSR1GT24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 420)
)
_Hh3cevtModuleSw_LSR1GP24LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP24LEB1 = _Hh3cevtModuleSw_LSR1GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 421)
)
_Hh3cevtModuleSw_LSR1GP24LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP24LEC1 = _Hh3cevtModuleSw_LSR1GP24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 422)
)
_Hh3cevtModuleSw_LSR1GT48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GT48LEB1 = _Hh3cevtModuleSw_LSR1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 423)
)
_Hh3cevtModuleSw_LSR1GT48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GT48LEC1 = _Hh3cevtModuleSw_LSR1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 424)
)
_Hh3cevtModuleSw_LSR1GP48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP48LEB1 = _Hh3cevtModuleSw_LSR1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 425)
)
_Hh3cevtModuleSw_LSR1GP48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP48LEC1 = _Hh3cevtModuleSw_LSR1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 426)
)
_Hh3cevtModuleSw_LSR2GV48REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GV48REB1 = _Hh3cevtModuleSw_LSR2GV48REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 427)
)
_Hh3cevtModuleSw_LSR1XP2LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP2LEB1 = _Hh3cevtModuleSw_LSR1XP2LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 428)
)
_Hh3cevtModuleSw_LSR1XP2LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP2LEC1 = _Hh3cevtModuleSw_LSR1XP2LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 429)
)
_Hh3cevtModuleSw_LSR1XP4LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP4LEB1 = _Hh3cevtModuleSw_LSR1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 430)
)
_Hh3cevtModuleSw_LSR1XP4LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP4LEC1 = _Hh3cevtModuleSw_LSR1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 431)
)
_Hh3cevtModuleSw_IMFW_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMFW = _Hh3cevtModuleSw_IMFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 432)
)
_Hh3cevtModuleSw_LSB1LB1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1LB1A0 = _Hh3cevtModuleSw_LSB1LB1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 433)
)
_Hh3cevtModuleSw_LSB1IPS1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPS1A0 = _Hh3cevtModuleSw_LSB1IPS1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 434)
)
_Hh3cevtModuleSw_LST1GT48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEB1 = _Hh3cevtModuleSw_LST1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 435)
)
_Hh3cevtModuleSw_LST1GP48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEB1 = _Hh3cevtModuleSw_LST1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 436)
)
_Hh3cevtModuleSw_LST1XP4LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP4LEB1 = _Hh3cevtModuleSw_LST1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 437)
)
_Hh3cevtModuleSw_LST1XP8LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEB1 = _Hh3cevtModuleSw_LST1XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 438)
)
_Hh3cevtModuleSw_LST1XP32REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP32REB1 = _Hh3cevtModuleSw_LST1XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 439)
)
_Hh3cevtModuleSw_LST1XP32REC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP32REC1 = _Hh3cevtModuleSw_LST1XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 440)
)
_Hh3cevtModuleSw_LSR1FW2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1FW2A1 = _Hh3cevtModuleSw_LSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 441)
)
_Hh3cevtModuleSw_LSR1SSL1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SSL1A1 = _Hh3cevtModuleSw_LSR1SSL1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 442)
)
_Hh3cevtModuleSw_SR01DET32G2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DET32G2L = _Hh3cevtModuleSw_SR01DET32G2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 443)
)
_Hh3cevtModuleSw_LSR1GP24LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP24LEF1 = _Hh3cevtModuleSw_LSR1GP24LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 444)
)
_Hh3cevtModuleSw_LSR1XP4LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP4LEF1 = _Hh3cevtModuleSw_LSR1XP4LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 445)
)
_Hh3cevtModuleSw_LSR1LB1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1LB1A1 = _Hh3cevtModuleSw_LSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 446)
)
_Hh3cevtModuleSw_LSR1NSM1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1NSM1A1 = _Hh3cevtModuleSw_LSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 447)
)
_Hh3cevtModuleSw_LSR1ACG1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1ACG1A1 = _Hh3cevtModuleSw_LSR1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 448)
)
_Hh3cevtModuleSw_LSR1IPS1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1IPS1A1 = _Hh3cevtModuleSw_LSR1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 449)
)
_Hh3cevtModuleSw_LSR2GP24LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GP24LEB1 = _Hh3cevtModuleSw_LSR2GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 450)
)
_Hh3cevtModuleSw_LSR2GT24LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GT24LEB1 = _Hh3cevtModuleSw_LSR2GT24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 451)
)
_Hh3cevtModuleSw_LSR2GT48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GT48LEB1 = _Hh3cevtModuleSw_LSR2GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 452)
)
_Hh3cevtModuleSw_SPC_GP24L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP24L = _Hh3cevtModuleSw_SPC_GP24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 453)
)
_Hh3cevtModuleSw_SPC_GT48L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GT48L = _Hh3cevtModuleSw_SPC_GT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 454)
)
_Hh3cevtModuleSw_SPC_GP48L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48L = _Hh3cevtModuleSw_SPC_GP48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 455)
)
_Hh3cevtModuleSw_SPC_XP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP2L = _Hh3cevtModuleSw_SPC_XP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 456)
)
_Hh3cevtModuleSw_SPC_XP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4L = _Hh3cevtModuleSw_SPC_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 457)
)
_Hh3cevtModuleSw_SR06SRP2E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR06SRP2E3 = _Hh3cevtModuleSw_SR06SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 458)
)
_Hh3cevtModuleSw_SPE_2010_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_2010_E = _Hh3cevtModuleSw_SPE_2010_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 459)
)
_Hh3cevtModuleSw_SPE_2020_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_2020_E = _Hh3cevtModuleSw_SPE_2020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 460)
)
_Hh3cevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4L_S_SDI = _Hh3cevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 461)
)
_Hh3cevtModuleSw_SPC_GT48L_SDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GT48L_SDI = _Hh3cevtModuleSw_SPC_GT48L_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 462)
)
_Hh3cevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48L_S_SDI = _Hh3cevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 463)
)
_Hh3cevtModuleSw_SPC_SR02OPMA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_SR02OPMA0 = _Hh3cevtModuleSw_SPC_SR02OPMA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 464)
)
_Hh3cevtModuleSw_LSR1XP16REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP16REB1 = _Hh3cevtModuleSw_LSR1XP16REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 465)
)
_Hh3cevtModuleSw_LSR1GP48LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP48LEF1 = _Hh3cevtModuleSw_LSR1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 466)
)
_Hh3cevtModuleSw_LST1GP48LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEF1 = _Hh3cevtModuleSw_LST1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 467)
)
_Hh3cevtModuleSw_LST1XP8LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEF1 = _Hh3cevtModuleSw_LST1XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 468)
)
_Hh3cevtModuleSw_SPE_1010_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1010_II = _Hh3cevtModuleSw_SPE_1010_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 469)
)
_Hh3cevtModuleSw_SPE_1010_E_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1010_E_II = _Hh3cevtModuleSw_SPE_1010_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 470)
)
_Hh3cevtModuleSw_SPE_1020_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1020_II = _Hh3cevtModuleSw_SPE_1020_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 471)
)
_Hh3cevtModuleSw_SPE_1020_E_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1020_E_II = _Hh3cevtModuleSw_SPE_1020_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 472)
)
_Hh3cevtModuleSw_LST1FW2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1FW2A1 = _Hh3cevtModuleSw_LST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 473)
)
_Hh3cevtModuleSw_LST1NSM1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1NSM1A1 = _Hh3cevtModuleSw_LST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 474)
)
_Hh3cevtModuleSw_LST1LB1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1LB1A1 = _Hh3cevtModuleSw_LST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 475)
)
_Hh3cevtModuleSw_LST1ACG1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1ACG1A1 = _Hh3cevtModuleSw_LST1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 476)
)
_Hh3cevtModuleSw_LST1IPS1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1IPS1A1 = _Hh3cevtModuleSw_LST1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 477)
)
_Hh3cevtModuleSw_LSR1DRUP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DRUP1L1 = _Hh3cevtModuleSw_LSR1DRUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 478)
)
_Hh3cevtModuleSw_LSR1DPUP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DPUP1L1 = _Hh3cevtModuleSw_LSR1DPUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 479)
)
_Hh3cevtModuleSw_LSR1DPSP4L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DPSP4L1 = _Hh3cevtModuleSw_LSR1DPSP4L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 480)
)
_Hh3cevtModuleSw_LSR1DTCP8L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DTCP8L1 = _Hh3cevtModuleSw_LSR1DTCP8L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 481)
)
_Hh3cevtModuleSw_LSR1DXP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DXP1L1 = _Hh3cevtModuleSw_LSR1DXP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 482)
)
_Hh3cevtModuleSw_LSR1DGP10L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DGP10L1 = _Hh3cevtModuleSw_LSR1DGP10L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 483)
)
_Hh3cevtModuleSw_LSR1LN1BNL1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1LN1BNL1 = _Hh3cevtModuleSw_LSR1LN1BNL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 484)
)
_Hh3cevtModuleSw_LSR1LN2BL1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1LN2BL1 = _Hh3cevtModuleSw_LSR1LN2BL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 485)
)
_Hh3cevtModuleSw_LSR1SRP2D1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2D1 = _Hh3cevtModuleSw_LSR1SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 486)
)
_Hh3cevtModuleSw_IM_NAT_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_NAT_II = _Hh3cevtModuleSw_IM_NAT_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 487)
)
_Hh3cevtModuleSw_IM_NAM_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_NAM_II = _Hh3cevtModuleSw_IM_NAM_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 488)
)
_Hh3cevtModuleSw_CR_MRP_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_MRP_I = _Hh3cevtModuleSw_CR_MRP_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 489)
)
_Hh3cevtModuleSw_CR_SF18C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SF18C = _Hh3cevtModuleSw_CR_SF18C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 490)
)
_Hh3cevtModuleSw_CR_SF08C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SF08C = _Hh3cevtModuleSw_CR_SF08C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 491)
)
_Hh3cevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP8LEF = _Hh3cevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 492)
)
_Hh3cevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP4LEF = _Hh3cevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 493)
)
_Hh3cevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_GP48LEF = _Hh3cevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 494)
)
_Hh3cevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_GT48LEF = _Hh3cevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 495)
)
_Hh3cevtModuleSw_CR_SPE_3020_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPE_3020_E = _Hh3cevtModuleSw_CR_SPE_3020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 496)
)
_Hh3cevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_PUP4L_E = _Hh3cevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 497)
)
_Hh3cevtModuleSw_LST1SF08C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF08C1 = _Hh3cevtModuleSw_LST1SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 498)
)
_Hh3cevtModuleSw_LST1SF18C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF18C1 = _Hh3cevtModuleSw_LST1SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 499)
)
_Hh3cevtModuleSw_LS81GP16TM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP16TM = _Hh3cevtModuleSw_LS81GP16TM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 500)
)
_Hh3cevtModuleSw_LS81VP4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81VP4C = _Hh3cevtModuleSw_LS81VP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 501)
)
_Hh3cevtModuleSw_LS8M1PT8P0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1PT8P0 = _Hh3cevtModuleSw_LS8M1PT8P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 502)
)
_Hh3cevtModuleSw_LS8M1PT8GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1PT8GB0 = _Hh3cevtModuleSw_LS8M1PT8GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 503)
)
_Hh3cevtModuleSw_LS8M1PT4GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1PT4GB0 = _Hh3cevtModuleSw_LS8M1PT4GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 504)
)
_Hh3cevtModuleSw_LS81GP2R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP2R = _Hh3cevtModuleSw_LS81GP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 505)
)
_Hh3cevtModuleSw_LS81GP4R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP4R = _Hh3cevtModuleSw_LS81GP4R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 506)
)
_Hh3cevtModuleSw_LS81IPSECA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81IPSECA = _Hh3cevtModuleSw_LS81IPSECA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 507)
)
_Hh3cevtModuleSw_LS81FWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FWA = _Hh3cevtModuleSw_LS81FWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 508)
)
_Hh3cevtModuleSw_LS82VSNP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82VSNP = _Hh3cevtModuleSw_LS82VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 509)
)
_Hh3cevtModuleSw_LSQ1GV48SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SA = _Hh3cevtModuleSw_LSQ1GV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 510)
)
_Hh3cevtModuleSw_LSQ1SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPB = _Hh3cevtModuleSw_LSQ1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 511)
)
_Hh3cevtModuleSw_LSQ1SRP2XB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP2XB = _Hh3cevtModuleSw_LSQ1SRP2XB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 512)
)
_Hh3cevtModuleSw_LSQ1SRP1CB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP1CB = _Hh3cevtModuleSw_LSQ1SRP1CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 513)
)
_Hh3cevtModuleSw_LSQ1FV48SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FV48SA = _Hh3cevtModuleSw_LSQ1FV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 514)
)
_Hh3cevtModuleSw_LSD1MPUA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1MPUA = _Hh3cevtModuleSw_LSD1MPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 515)
)
_Hh3cevtModuleSw_LSD1GP20A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20A0 = _Hh3cevtModuleSw_LSD1GP20A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 516)
)
_Hh3cevtModuleSw_LSD1GP20TA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20TA0 = _Hh3cevtModuleSw_LSD1GP20TA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 517)
)
_Hh3cevtModuleSw_LSD1GP36A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP36A0 = _Hh3cevtModuleSw_LSD1GP36A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 518)
)
_Hh3cevtModuleSw_LSD1GP20XA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20XA0 = _Hh3cevtModuleSw_LSD1GP20XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 519)
)
_Hh3cevtModuleSw_LSD1GP20EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20EA0 = _Hh3cevtModuleSw_LSD1GP20EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 520)
)
_Hh3cevtModuleSw_LSD1GP20RA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20RA0 = _Hh3cevtModuleSw_LSD1GP20RA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 521)
)
_Hh3cevtModuleSw_LSD1GP16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP16A0 = _Hh3cevtModuleSw_LSD1GP16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 522)
)
_Hh3cevtModuleSw_LSD1GT16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GT16A0 = _Hh3cevtModuleSw_LSD1GT16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 523)
)
_Hh3cevtModuleSw_LSD1XP2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1XP2A0 = _Hh3cevtModuleSw_LSD1XP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 524)
)
_Hh3cevtModuleSw_LSD1EP2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1EP2A0 = _Hh3cevtModuleSw_LSD1EP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 525)
)
_Hh3cevtModuleSw_LSD1RP2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1RP2A0 = _Hh3cevtModuleSw_LSD1RP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 526)
)
_Hh3cevtModuleSw_LSQ1GV48SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SC = _Hh3cevtModuleSw_LSQ1GV48SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 527)
)
_Hh3cevtModuleSw_LSQ1FP48SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FP48SA = _Hh3cevtModuleSw_LSQ1FP48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 528)
)
_Hh3cevtModuleSw_LSQ1GP24SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24SC = _Hh3cevtModuleSw_LSQ1GP24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 529)
)
_Hh3cevtModuleSw_LSQ1GT24SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GT24SC = _Hh3cevtModuleSw_LSQ1GT24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 530)
)
_Hh3cevtModuleSw_LSQ1TGX2SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SC = _Hh3cevtModuleSw_LSQ1TGX2SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 531)
)
_Hh3cevtModuleSw_LSQ1GP12EA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP12EA = _Hh3cevtModuleSw_LSQ1GP12EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 532)
)
_Hh3cevtModuleSw_LSQ1TGX1EA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX1EA = _Hh3cevtModuleSw_LSQ1TGX1EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 533)
)
_Hh3cevtModuleSw_LSQ1P24XGSC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1P24XGSC = _Hh3cevtModuleSw_LSQ1P24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 534)
)
_Hh3cevtModuleSw_LSQ1T24XGSC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1T24XGSC = _Hh3cevtModuleSw_LSQ1T24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 535)
)
_Hh3cevtModuleSw_LS81TGX1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX1B = _Hh3cevtModuleSw_LS81TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 536)
)
_Hh3cevtModuleSw_LSQ1PT4PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT4PSC0 = _Hh3cevtModuleSw_LSQ1PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 537)
)
_Hh3cevtModuleSw_LS81SRPG13_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG13 = _Hh3cevtModuleSw_LS81SRPG13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 538)
)
_Hh3cevtModuleSw_LS81SRPG14_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG14 = _Hh3cevtModuleSw_LS81SRPG14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 539)
)
_Hh3cevtModuleSw_LS81SRPG15_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG15 = _Hh3cevtModuleSw_LS81SRPG15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 540)
)
_Hh3cevtModuleSw_LSQ1GP48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SC0 = _Hh3cevtModuleSw_LSQ1GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 541)
)
_Hh3cevtModuleSw_LSQ1GP12SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP12SC0 = _Hh3cevtModuleSw_LSQ1GP12SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 542)
)
_Hh3cevtModuleSw_LSD1SRPA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1SRPA = _Hh3cevtModuleSw_LSD1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 543)
)
_Hh3cevtModuleSw_LSD1SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1SRPB = _Hh3cevtModuleSw_LSD1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 544)
)
_Hh3cevtModuleSw_LSD1SRPC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1SRPC = _Hh3cevtModuleSw_LSD1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 545)
)
_Hh3cevtModuleSw_LSD1GT16PES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GT16PES0 = _Hh3cevtModuleSw_LSD1GT16PES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 546)
)
_Hh3cevtModuleSw_LSD1GP24ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP24ES0 = _Hh3cevtModuleSw_LSD1GP24ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 547)
)
_Hh3cevtModuleSw_LSD1GT24XES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GT24XES0 = _Hh3cevtModuleSw_LSD1GT24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 548)
)
_Hh3cevtModuleSw_LSD1GP24XES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP24XES0 = _Hh3cevtModuleSw_LSD1GP24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 549)
)
_Hh3cevtModuleSw_LSD1XP2ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1XP2ES0 = _Hh3cevtModuleSw_LSD1XP2ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 550)
)
_Hh3cevtModuleSw_LSD1GP48ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP48ES0 = _Hh3cevtModuleSw_LSD1GP48ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 551)
)
_Hh3cevtModuleSw_LSQ1MPUA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUA0 = _Hh3cevtModuleSw_LSQ1MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 552)
)
_Hh3cevtModuleSw_LSQ1MPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUA1 = _Hh3cevtModuleSw_LSQ1MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 553)
)
_Hh3cevtModuleSw_LSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FWBSC0 = _Hh3cevtModuleSw_LSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 554)
)
_Hh3cevtModuleSw_LSQ1PT8PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT8PSC0 = _Hh3cevtModuleSw_LSQ1PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 555)
)
_Hh3cevtModuleSw_LSQ1PT16PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT16PSC0 = _Hh3cevtModuleSw_LSQ1PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 556)
)
_Hh3cevtModuleSw_SA11MPUA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SA11MPUA0 = _Hh3cevtModuleSw_SA11MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 557)
)
_Hh3cevtModuleSw_SA11MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SA11MPUB0 = _Hh3cevtModuleSw_SA11MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 558)
)
_Hh3cevtModuleSw_LSQ1AFCBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1AFCBSC0 = _Hh3cevtModuleSw_LSQ1AFCBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 559)
)
_Hh3cevtModuleSw_LSQ1MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB0 = _Hh3cevtModuleSw_LSQ1MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 560)
)
_Hh3cevtModuleSw_LSQ1MPUB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB1 = _Hh3cevtModuleSw_LSQ1MPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 561)
)
_Hh3cevtModuleSw_LSQ1PT4PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT4PSC1 = _Hh3cevtModuleSw_LSQ1PT4PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 562)
)
_Hh3cevtModuleSw_LSQ1PT8PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT8PSC1 = _Hh3cevtModuleSw_LSQ1PT8PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 563)
)
_Hh3cevtModuleSw_LSQ1PT16PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT16PSC1 = _Hh3cevtModuleSw_LSQ1PT16PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 564)
)
_Hh3cevtModuleSw_LSQ1FP48USA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FP48USA0 = _Hh3cevtModuleSw_LSQ1FP48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 565)
)
_Hh3cevtModuleSw_LSQ1FP48USA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FP48USA1 = _Hh3cevtModuleSw_LSQ1FP48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 566)
)
_Hh3cevtModuleSw_LSQ1FV48USA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FV48USA0 = _Hh3cevtModuleSw_LSQ1FV48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 567)
)
_Hh3cevtModuleSw_LSQ1FV48USA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FV48USA1 = _Hh3cevtModuleSw_LSQ1FV48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 568)
)
_Hh3cevtModuleSw_LSQ1SRPD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPD0 = _Hh3cevtModuleSw_LSQ1SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 569)
)
_Hh3cevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGP24TSC0 = _Hh3cevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 570)
)
_Hh3cevtModuleSw_LSQ1GP24TSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSC0 = _Hh3cevtModuleSw_LSQ1GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 571)
)
_Hh3cevtModuleSw_LSQ1ACGASC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1ACGASC0 = _Hh3cevtModuleSw_LSQ1ACGASC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 572)
)
_Hh3cevtModuleSw_LSD1XP1ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1XP1ES0 = _Hh3cevtModuleSw_LSD1XP1ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 573)
)
_Hh3cevtModuleSw_LSD1GP12ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP12ES0 = _Hh3cevtModuleSw_LSD1GP12ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 574)
)
_Hh3cevtModuleSw_LSQ1SRP12GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP12GB0 = _Hh3cevtModuleSw_LSQ1SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 575)
)
_Hh3cevtModuleSw_LSQ1GV40PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV40PSC0 = _Hh3cevtModuleSw_LSQ1GV40PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 576)
)
_Hh3cevtModuleSw_LSQ1FWBSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FWBSC1 = _Hh3cevtModuleSw_LSQ1FWBSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 577)
)
_Hh3cevtModuleSw_LSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1NSMSC0 = _Hh3cevtModuleSw_LSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 578)
)
_Hh3cevtModuleSw_LSQ1NSMSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1NSMSC1 = _Hh3cevtModuleSw_LSQ1NSMSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 579)
)
_Hh3cevtModuleSw_LSQ1AFDBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1AFDBSC0 = _Hh3cevtModuleSw_LSQ1AFDBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 580)
)
_Hh3cevtModuleSw_LS81MPUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81MPUB = _Hh3cevtModuleSw_LS81MPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 581)
)
_Hh3cevtModuleSw_LS81FP48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FP48XL = _Hh3cevtModuleSw_LS81FP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 582)
)
_Hh3cevtModuleSw_LS81FT48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FT48XL = _Hh3cevtModuleSw_LS81FT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 583)
)
_Hh3cevtModuleSw_LS81GP12XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP12XL = _Hh3cevtModuleSw_LS81GP12XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 584)
)
_Hh3cevtModuleSw_LS81GP24XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP24XL = _Hh3cevtModuleSw_LS81GP24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 585)
)
_Hh3cevtModuleSw_LS81GP48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP48XL = _Hh3cevtModuleSw_LS81GP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 586)
)
_Hh3cevtModuleSw_LS81GT24XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT24XL = _Hh3cevtModuleSw_LS81GT24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 587)
)
_Hh3cevtModuleSw_LS81GT48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48XL = _Hh3cevtModuleSw_LS81GT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 588)
)
_Hh3cevtModuleSw_LS81TGX2XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX2XL = _Hh3cevtModuleSw_LS81TGX2XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 589)
)
_Hh3cevtModuleSw_LSQ1GV48SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SD0 = _Hh3cevtModuleSw_LSQ1GV48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 590)
)
_Hh3cevtModuleSw_LSQ1GP48EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48EB0 = _Hh3cevtModuleSw_LSQ1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 591)
)
_Hh3cevtModuleSw_LSQ1IPSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1IPSSC0 = _Hh3cevtModuleSw_LSQ1IPSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 592)
)
_Hh3cevtModuleSw_LSQ1GV48SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SD1 = _Hh3cevtModuleSw_LSQ1GV48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 593)
)
_Hh3cevtModuleSw_LSQ1GP48SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SD0 = _Hh3cevtModuleSw_LSQ1GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 594)
)
_Hh3cevtModuleSw_LSQ1GP48SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SD1 = _Hh3cevtModuleSw_LSQ1GP48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 595)
)
_Hh3cevtModuleSw_LSQ1SRPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA0 = _Hh3cevtModuleSw_LSQ1SRPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 596)
)
_Hh3cevtModuleSw_LSQ1SRPA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA1 = _Hh3cevtModuleSw_LSQ1SRPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 597)
)
_Hh3cevtModuleSw_LSQ2FP48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FP48SA0 = _Hh3cevtModuleSw_LSQ2FP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 598)
)
_Hh3cevtModuleSw_LSQ2FP48SA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FP48SA1 = _Hh3cevtModuleSw_LSQ2FP48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 599)
)
_Hh3cevtModuleSw_LSQ2FT48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FT48SA0 = _Hh3cevtModuleSw_LSQ2FT48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 600)
)
_Hh3cevtModuleSw_LSQ2FT48SA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FT48SA1 = _Hh3cevtModuleSw_LSQ2FT48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 601)
)
_Hh3cevtModuleSw_LSQ1GV24PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV24PSC0 = _Hh3cevtModuleSw_LSQ1GV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 602)
)
_Hh3cevtModuleSw_LSQ1GV24PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV24PSC1 = _Hh3cevtModuleSw_LSQ1GV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 603)
)
_Hh3cevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGV24PSC0 = _Hh3cevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 604)
)
_Hh3cevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGV24PSC1 = _Hh3cevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 605)
)
_Hh3cevtModuleSw_LSQ1GP24TEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TEB0 = _Hh3cevtModuleSw_LSQ1GP24TEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 606)
)
_Hh3cevtModuleSw_LSQ1GP24TEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TEB1 = _Hh3cevtModuleSw_LSQ1GP24TEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 607)
)
_Hh3cevtModuleSw_LSQ1GP24TSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSD0 = _Hh3cevtModuleSw_LSQ1GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 608)
)
_Hh3cevtModuleSw_LSQ1GP24TSD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSD1 = _Hh3cevtModuleSw_LSQ1GP24TSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 609)
)
_Hh3cevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TXSD0 = _Hh3cevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 610)
)
_Hh3cevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TXSD1 = _Hh3cevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 611)
)
_Hh3cevtModuleSw_LSQ1TGX2EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2EB0 = _Hh3cevtModuleSw_LSQ1TGX2EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 612)
)
_Hh3cevtModuleSw_LSQ1TGX2EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2EB1 = _Hh3cevtModuleSw_LSQ1TGX2EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 613)
)
_Hh3cevtModuleSw_LSQ1TGX2SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SD0 = _Hh3cevtModuleSw_LSQ1TGX2SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 614)
)
_Hh3cevtModuleSw_LSQ1TGX2SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SD1 = _Hh3cevtModuleSw_LSQ1TGX2SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 615)
)
_Hh3cevtModuleSw_LSQ1TGX4SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4SD0 = _Hh3cevtModuleSw_LSQ1TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 616)
)
_Hh3cevtModuleSw_LSQ1TGX4SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4SD1 = _Hh3cevtModuleSw_LSQ1TGX4SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 617)
)
_Hh3cevtModuleSw_LSQ1TGX8SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX8SD0 = _Hh3cevtModuleSw_LSQ1TGX8SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 618)
)
_Hh3cevtModuleSw_LSQ1TGX8SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX8SD1 = _Hh3cevtModuleSw_LSQ1TGX8SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 619)
)
_Hh3cevtModuleSw_LSQ1GP48EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48EB1 = _Hh3cevtModuleSw_LSQ1GP48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 620)
)
_Hh3cevtModuleSw_LSQ1TGX4EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4EB0 = _Hh3cevtModuleSw_LSQ1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 621)
)
_Hh3cevtModuleSw_LSQ1TGX4EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4EB1 = _Hh3cevtModuleSw_LSQ1TGX4EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 622)
)
_Hh3cevtModuleSw_LSQ1GP12SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP12SC3 = _Hh3cevtModuleSw_LSQ1GP12SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 623)
)
_Hh3cevtModuleSw_LSQ1GP24TSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSC3 = _Hh3cevtModuleSw_LSQ1GP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 624)
)
_Hh3cevtModuleSw_LSQ1GP48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SC3 = _Hh3cevtModuleSw_LSQ1GP48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 625)
)
_Hh3cevtModuleSw_LSQ1GV48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SC3 = _Hh3cevtModuleSw_LSQ1GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 626)
)
_Hh3cevtModuleSw_LSQ1MPUA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUA3 = _Hh3cevtModuleSw_LSQ1MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 627)
)
_Hh3cevtModuleSw_LSQ1SRP1CB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP1CB3 = _Hh3cevtModuleSw_LSQ1SRP1CB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 628)
)
_Hh3cevtModuleSw_LSQ1SRPA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA3 = _Hh3cevtModuleSw_LSQ1SRPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 629)
)
_Hh3cevtModuleSw_LSQ2FP48SA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FP48SA3 = _Hh3cevtModuleSw_LSQ2FP48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 630)
)
_Hh3cevtModuleSw_LSQ2FT48SA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FT48SA3 = _Hh3cevtModuleSw_LSQ2FT48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 631)
)
_Hh3cevtModuleSw_LSQ1MPUB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB3 = _Hh3cevtModuleSw_LSQ1MPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 632)
)
_Hh3cevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGP24TSC3 = _Hh3cevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 633)
)
_Hh3cevtModuleSw_LSQ1MPUB4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB4 = _Hh3cevtModuleSw_LSQ1MPUB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 634)
)
_Hh3cevtModuleSw_LSQ1SRPD4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPD4 = _Hh3cevtModuleSw_LSQ1SRPD4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 635)
)
_Hh3cevtModuleSw_LSQ1SSLSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SSLSC0 = _Hh3cevtModuleSw_LSQ1SSLSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 636)
)
_Hh3cevtModuleSw_LSQ1LBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1LBSC0 = _Hh3cevtModuleSw_LSQ1LBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 637)
)
_Hh3cevtModuleSw_LSQ1NAT24SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1NAT24SC0 = _Hh3cevtModuleSw_LSQ1NAT24SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 638)
)
_Hh3cevtModuleSw_LSQ1SRP12GB4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP12GB4 = _Hh3cevtModuleSw_LSQ1SRP12GB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 639)
)
_Hh3cevtModuleSw_LSQ1TGS8SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS8SC0 = _Hh3cevtModuleSw_LSQ1TGS8SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 640)
)
_Hh3cevtModuleSw_LSQ3PT4PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ3PT4PSC0 = _Hh3cevtModuleSw_LSQ3PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 641)
)
_Hh3cevtModuleSw_EWPXM2MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2MPUB0 = _Hh3cevtModuleSw_EWPXM2MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 642)
)
_Hh3cevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2SRP12GB0 = _Hh3cevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 643)
)
_Hh3cevtModuleSw_EWPXM2SRPD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2SRPD0 = _Hh3cevtModuleSw_EWPXM2SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 644)
)
_Hh3cevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TSD0 = _Hh3cevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 645)
)
_Hh3cevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TXSD0 = _Hh3cevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 646)
)
_Hh3cevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2TGX4SD0 = _Hh3cevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 647)
)
_Hh3cevtModuleSw_EWPXM2GP48SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP48SD0 = _Hh3cevtModuleSw_EWPXM2GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 648)
)
_Hh3cevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TSC0 = _Hh3cevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 649)
)
_Hh3cevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2TGX2SC0 = _Hh3cevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 650)
)
_Hh3cevtModuleSw_EWPXM2GP48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP48SC0 = _Hh3cevtModuleSw_EWPXM2GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 651)
)
_Hh3cevtModuleSw_LS7500_GP48_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GP48_SC = _Hh3cevtModuleSw_LS7500_GP48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 652)
)
_Hh3cevtModuleSw_LS7500_GP48_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GP48_SD = _Hh3cevtModuleSw_LS7500_GP48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 653)
)
_Hh3cevtModuleSw_LS7500_GT48_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GT48_SC = _Hh3cevtModuleSw_LS7500_GT48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 654)
)
_Hh3cevtModuleSw_LS7500_GT48_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GT48_SD = _Hh3cevtModuleSw_LS7500_GT48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 655)
)
_Hh3cevtModuleSw_LS7500_SRPG1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_SRPG1 = _Hh3cevtModuleSw_LS7500_SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 656)
)
_Hh3cevtModuleSw_LS7500_SRPG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_SRPG2 = _Hh3cevtModuleSw_LS7500_SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 657)
)
_Hh3cevtModuleSw_LS7500_XP4_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_XP4_SD = _Hh3cevtModuleSw_LS7500_XP4_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 658)
)
_Hh3cevtModuleSw_LS7500_XP8_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_XP8_SD = _Hh3cevtModuleSw_LS7500_XP8_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 659)
)
_Hh3cevtModuleSw_LSQ4PT4PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ4PT4PSC0 = _Hh3cevtModuleSw_LSQ4PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 660)
)
_Hh3cevtModuleSw_LSQ4PT8PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ4PT8PSC0 = _Hh3cevtModuleSw_LSQ4PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 661)
)
_Hh3cevtModuleSw_LSQ4PT16PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ4PT16PSC0 = _Hh3cevtModuleSw_LSQ4PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 662)
)
_Hh3cevtModuleSw_LSQ1GP24TSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSA0 = _Hh3cevtModuleSw_LSQ1GP24TSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 663)
)
_Hh3cevtModuleSw_LSQ1GV24PSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV24PSA0 = _Hh3cevtModuleSw_LSQ1GV24PSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 664)
)
_Hh3cevtModuleSw_LSQ1SRPD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPD3 = _Hh3cevtModuleSw_LSQ1SRPD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 665)
)
_Hh3cevtModuleSw_LSQ1SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SUPA0 = _Hh3cevtModuleSw_LSQ1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 666)
)
_Hh3cevtModuleSw_LSU1FAB04A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB04A0 = _Hh3cevtModuleSw_LSU1FAB04A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 667)
)
_Hh3cevtModuleSw_LSU1FAB08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB08A0 = _Hh3cevtModuleSw_LSU1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 668)
)
_Hh3cevtModuleSw_LSU1TGS8EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8EA0 = _Hh3cevtModuleSw_LSU1TGS8EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 669)
)
_Hh3cevtModuleSw_LSU1TGS8EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8EB0 = _Hh3cevtModuleSw_LSU1TGS8EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 670)
)
_Hh3cevtModuleSw_LSU1TGS8SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8SE0 = _Hh3cevtModuleSw_LSU1TGS8SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 671)
)
_Hh3cevtModuleSw_LSUTGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUTGS16SC0 = _Hh3cevtModuleSw_LSUTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 672)
)
_Hh3cevtModuleSw_LUS1SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LUS1SUPA0 = _Hh3cevtModuleSw_LUS1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 673)
)
_Hh3cevtModuleSw_LSU1GP24TXEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TXEA0 = _Hh3cevtModuleSw_LSU1GP24TXEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 674)
)
_Hh3cevtModuleSw_LSU1GP24TXEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TXEB0 = _Hh3cevtModuleSw_LSU1GP24TXEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 675)
)
_Hh3cevtModuleSw_LSU1GP24TXSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TXSE0 = _Hh3cevtModuleSw_LSU1GP24TXSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 676)
)
_Hh3cevtModuleSw_LSU1GP48EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48EA0 = _Hh3cevtModuleSw_LSU1GP48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 677)
)
_Hh3cevtModuleSw_LSU1GP48EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48EB0 = _Hh3cevtModuleSw_LSU1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 678)
)
_Hh3cevtModuleSw_LSU1GP48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48SE0 = _Hh3cevtModuleSw_LSU1GP48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 679)
)
_Hh3cevtModuleSw_LSU1GT48EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT48EA0 = _Hh3cevtModuleSw_LSU1GT48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 680)
)
_Hh3cevtModuleSw_LSU1GT48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT48SE0 = _Hh3cevtModuleSw_LSU1GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 681)
)
_Hh3cevtModuleSw_LSU1TGX4EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGX4EA0 = _Hh3cevtModuleSw_LSU1TGX4EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 682)
)
_Hh3cevtModuleSw_LSU1TGX4EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGX4EB0 = _Hh3cevtModuleSw_LSU1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 683)
)
_Hh3cevtModuleSw_LSU1TGX4SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGX4SE0 = _Hh3cevtModuleSw_LSU1TGX4SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 684)
)
_Hh3cevtModuleSw_LSQ1FAB08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB08A0 = _Hh3cevtModuleSw_LSQ1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 685)
)
_Hh3cevtModuleSw_EWPX2WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX2WCMD0 = _Hh3cevtModuleSw_EWPX2WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 686)
)
_Hh3cevtModuleSw_LSQ1WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1WCMD0 = _Hh3cevtModuleSw_LSQ1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 687)
)
_Hh3cevtModuleSw_LSQ1IAGSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1IAGSC0 = _Hh3cevtModuleSw_LSQ1IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 688)
)
_Hh3cevtModuleSw_LSU1GP24TSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TSE0 = _Hh3cevtModuleSw_LSU1GP24TSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 689)
)
_Hh3cevtModuleSw_LSQ1TGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS16SC0 = _Hh3cevtModuleSw_LSQ1TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 690)
)
_Hh3cevtModuleSw_EWPX2TGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX2TGS16SC0 = _Hh3cevtModuleSw_EWPX2TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 691)
)
_Hh3cevtModuleSw_LSQ1SUPA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SUPA3 = _Hh3cevtModuleSw_LSQ1SUPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 692)
)
_Hh3cevtModuleSw_LSQ1FAB04A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB04A3 = _Hh3cevtModuleSw_LSQ1FAB04A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 693)
)
_Hh3cevtModuleSw_LSQ1FAB08A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB08A3 = _Hh3cevtModuleSw_LSQ1FAB08A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 694)
)
_Hh3cevtModuleSw_1000BASE_X_COMBO_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_X_COMBO = _Hh3cevtModuleSw_1000BASE_X_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 701)
)
_Hh3cevtModuleSw_EPON_1000M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPON_1000M = _Hh3cevtModuleSw_EPON_1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 702)
)
_Hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45 = _Hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 703)
)
_Hh3cevtModuleSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_1550_BIDI = _Hh3cevtModuleSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 704)
)
_Hh3cevtModuleSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_1310_BIDI = _Hh3cevtModuleSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 705)
)
_Hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO = _Hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 706)
)
_Hh3cevtModuleSw_LSH1PK2T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSH1PK2T = _Hh3cevtModuleSw_LSH1PK2T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 707)
)
_Hh3cevtModuleSw_LSPM2GP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM2GP2P = _Hh3cevtModuleSw_LSPM2GP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 708)
)
_Hh3cevtModuleSw_LSWM1GT16P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1GT16P = _Hh3cevtModuleSw_LSWM1GT16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 709)
)
_Hh3cevtModuleSw_LSWM1GP16P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1GP16P = _Hh3cevtModuleSw_LSWM1GP16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 710)
)
_Hh3cevtModuleSw_LSWM1XP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1XP2P = _Hh3cevtModuleSw_LSWM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 711)
)
_Hh3cevtModuleSw_LSWM1XP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1XP4P = _Hh3cevtModuleSw_LSWM1XP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 712)
)
_Hh3cevtModuleSw_LSWM1SP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1SP2P = _Hh3cevtModuleSw_LSWM1SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 713)
)
_Hh3cevtModuleSw_LSWM1SP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1SP4P = _Hh3cevtModuleSw_LSWM1SP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 714)
)
_Hh3cevtModuleSw_LSWM148POEM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM148POEM = _Hh3cevtModuleSw_LSWM148POEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 715)
)
_Hh3cevtModuleSw_LSWM1FW10_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1FW10 = _Hh3cevtModuleSw_LSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 716)
)
_Hh3cevtModuleSw_LSWM1WCM10_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1WCM10 = _Hh3cevtModuleSw_LSWM1WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 717)
)
_Hh3cevtModuleSw_LSWM1IPS10_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1IPS10 = _Hh3cevtModuleSw_LSWM1IPS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 718)
)
_Hh3cevtModuleSw_LSWM1WCM20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1WCM20 = _Hh3cevtModuleSw_LSWM1WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 719)
)
_Hh3cevtModuleSw_IPS_T1000_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_T1000_M = _Hh3cevtModuleSw_IPS_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 720)
)
_Hh3cevtModuleSw_IPS_T1000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_T1000_A = _Hh3cevtModuleSw_IPS_T1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 721)
)
_Hh3cevtModuleSw_IPS_T1000_S_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_T1000_S = _Hh3cevtModuleSw_IPS_T1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 722)
)
_Hh3cevtModuleSw_IPS_GX4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_GX4C = _Hh3cevtModuleSw_IPS_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 723)
)
_Hh3cevtModuleSw_IPS_GT4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_GT4C = _Hh3cevtModuleSw_IPS_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 724)
)
_Hh3cevtModuleSw_LSPM2SP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM2SP2P = _Hh3cevtModuleSw_LSPM2SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 725)
)
_Hh3cevtModuleSw_LSPM2SP2PA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM2SP2PA = _Hh3cevtModuleSw_LSPM2SP2PA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 726)
)
_Hh3cevtModuleSw_LSP5GP8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSP5GP8P = _Hh3cevtModuleSw_LSP5GP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 727)
)
_Hh3cevtModuleSw_LSP5GT8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSP5GT8P = _Hh3cevtModuleSw_LSP5GT8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 728)
)
_Hh3cevtModuleSw_LSWM1FC4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1FC4P = _Hh3cevtModuleSw_LSWM1FC4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 729)
)
_Hh3cevtModuleSw_WX5002MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_WX5002MPU = _Hh3cevtModuleSw_WX5002MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 800)
)
_Hh3cevtModuleSw_LS8M1WCMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1WCMA = _Hh3cevtModuleSw_LS8M1WCMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 801)
)
_Hh3cevtModuleSw_EWPX1G24XA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XA0 = _Hh3cevtModuleSw_EWPX1G24XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 802)
)
_Hh3cevtModuleSw_LSQ1WCMB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1WCMB0 = _Hh3cevtModuleSw_LSQ1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 803)
)
_Hh3cevtModuleSw_LSB1WCM2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1WCM2A0 = _Hh3cevtModuleSw_LSB1WCM2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 804)
)
_Hh3cevtModuleSw_EWPX1WCMB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMB0 = _Hh3cevtModuleSw_EWPX1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 805)
)
_Hh3cevtModuleSw_EWPX1G24XC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XC0 = _Hh3cevtModuleSw_EWPX1G24XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 806)
)
_Hh3cevtModuleSw_EWPX1WCMC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMC0 = _Hh3cevtModuleSw_EWPX1WCMC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 807)
)
_Hh3cevtModuleSw_EWPX1FWA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1FWA0 = _Hh3cevtModuleSw_EWPX1FWA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 808)
)
_Hh3cevtModuleSw_EWPX1G10XC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G10XC0 = _Hh3cevtModuleSw_EWPX1G10XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 809)
)
_Hh3cevtModuleSw_EWPX1WCM10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCM10C0 = _Hh3cevtModuleSw_EWPX1WCM10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 810)
)
_Hh3cevtModuleSw_LSR1WCM2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1WCM2A1 = _Hh3cevtModuleSw_LSR1WCM2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 811)
)
_Hh3cevtModuleSw_EWPX1WAP0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WAP0 = _Hh3cevtModuleSw_EWPX1WAP0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 812)
)
_Hh3cevtModuleSw_EWPX1WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMD0 = _Hh3cevtModuleSw_EWPX1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 813)
)
_Hh3cevtModuleSw_EWPX1G24XCE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XCE0 = _Hh3cevtModuleSw_EWPX1G24XCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 814)
)
_Hh3cevtModuleSw_EWPX1WCMCE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMCE0 = _Hh3cevtModuleSw_EWPX1WCMCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 815)
)
_Hh3cevtModuleSw_LSR1DRSP2L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DRSP2L1 = _Hh3cevtModuleSw_LSR1DRSP2L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 900)
)
_Hh3cevtModuleSw_PIC_CLF2G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_CLF2G8L = _Hh3cevtModuleSw_PIC_CLF2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 901)
)
_Hh3cevtModuleSw_PIC_CLF4G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_CLF4G8L = _Hh3cevtModuleSw_PIC_CLF4G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 902)
)
_Hh3cevtModuleSw_SR02SRP2F3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP2F3 = _Hh3cevtModuleSw_SR02SRP2F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 903)
)
_Hh3cevtModuleSw_SR02SRP1F3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP1F3 = _Hh3cevtModuleSw_SR02SRP1F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 904)
)
_Hh3cevtModuleSw_LST1GT48LEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEA1 = _Hh3cevtModuleSw_LST1GT48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 905)
)
_Hh3cevtModuleSw_LST1GP48LEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEA1 = _Hh3cevtModuleSw_LST1GP48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 906)
)
_Hh3cevtModuleSw_LST2XP8LEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEA1 = _Hh3cevtModuleSw_LST2XP8LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 907)
)
_Hh3cevtModuleSw_LST1GT48LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEY1 = _Hh3cevtModuleSw_LST1GT48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 908)
)
_Hh3cevtModuleSw_LST1GP48LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEY1 = _Hh3cevtModuleSw_LST1GP48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 909)
)
_Hh3cevtModuleSw_LST1XP32REY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP32REY1 = _Hh3cevtModuleSw_LST1XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 910)
)
_Hh3cevtModuleSw_LST1XP8LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEY1 = _Hh3cevtModuleSw_LST1XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 911)
)
_Hh3cevtModuleSw_LST1GP48LEZ1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEZ1 = _Hh3cevtModuleSw_LST1GP48LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 912)
)
_Hh3cevtModuleSw_LST1XP8LEZ1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEZ1 = _Hh3cevtModuleSw_LST1XP8LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 913)
)
_Hh3cevtModuleSw_IM_FW_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_FW_II = _Hh3cevtModuleSw_IM_FW_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 914)
)
_Hh3cevtModuleSw_IM_IPS_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_IPS = _Hh3cevtModuleSw_IM_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 915)
)
_Hh3cevtModuleSw_IM_SSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_SSL = _Hh3cevtModuleSw_IM_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 916)
)
_Hh3cevtModuleSw_IM_LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_LB = _Hh3cevtModuleSw_IM_LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 917)
)
_Hh3cevtModuleSw_IM_ACG_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_ACG = _Hh3cevtModuleSw_IM_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 918)
)
_Hh3cevtModuleSw_LSR1XP16REC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP16REC1 = _Hh3cevtModuleSw_LSR1XP16REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 919)
)
_Hh3cevtModuleSw_LST2XP8LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEB1 = _Hh3cevtModuleSw_LST2XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 920)
)
_Hh3cevtModuleSw_LST2XP8LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEC1 = _Hh3cevtModuleSw_LST2XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 921)
)
_Hh3cevtModuleSw_LST2XP8LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEF1 = _Hh3cevtModuleSw_LST2XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 922)
)
_Hh3cevtModuleSw_LSR2XP4LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2XP4LEB1 = _Hh3cevtModuleSw_LSR2XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 923)
)
_Hh3cevtModuleSw_LSR2XP4LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2XP4LEC1 = _Hh3cevtModuleSw_LSR2XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 924)
)
_Hh3cevtModuleSw_LST2XP32REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP32REB1 = _Hh3cevtModuleSw_LST2XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 925)
)
_Hh3cevtModuleSw_LST2XP32REC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP32REC1 = _Hh3cevtModuleSw_LST2XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 926)
)
_Hh3cevtModuleSw_LSR1WCM3A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1WCM3A1 = _Hh3cevtModuleSw_LSR1WCM3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 927)
)
_Hh3cevtModuleSw_LST1XP16LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP16LEB1 = _Hh3cevtModuleSw_LST1XP16LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 928)
)
_Hh3cevtModuleSw_LST1XP16LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP16LEC1 = _Hh3cevtModuleSw_LST1XP16LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 929)
)
_Hh3cevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP4L_E_I = _Hh3cevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 930)
)
_Hh3cevtSubModuleRouter_ObjectIdentity = ObjectIdentity
hh3cevtSubModuleRouter = _Hh3cevtSubModuleRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 5)
)
_Hh3cevtSubModuleSwitch_ObjectIdentity = ObjectIdentity
hh3cevtSubModuleSwitch = _Hh3cevtSubModuleSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 6)
)
_Hh3cevtPort_ObjectIdentity = ObjectIdentity
hh3cevtPort = _Hh3cevtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10)
)
_Hh3cevtPortUnknownPorts_ObjectIdentity = ObjectIdentity
hh3cevtPortUnknownPorts = _Hh3cevtPortUnknownPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 1)
)
_Hh3cevtPortCommonPorts_ObjectIdentity = ObjectIdentity
hh3cevtPortCommonPorts = _Hh3cevtPortCommonPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 2)
)
_Hh3cevtPortRouterType_ObjectIdentity = ObjectIdentity
hh3cevtPortRouterType = _Hh3cevtPortRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3)
)
_Hh3cevtPortRt_Async_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Async = _Hh3cevtPortRt_Async_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 1)
)
_Hh3cevtPortRt_Analogmodem_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Analogmodem = _Hh3cevtPortRt_Analogmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 2)
)
_Hh3cevtPortRt_Atm_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Atm = _Hh3cevtPortRt_Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 3)
)
_Hh3cevtPortRt_AtmAdsl_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmAdsl = _Hh3cevtPortRt_AtmAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 4)
)
_Hh3cevtPortRt_AtmShdsl_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmShdsl = _Hh3cevtPortRt_AtmShdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 5)
)
_Hh3cevtPortRt_AtmE1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmE1 = _Hh3cevtPortRt_AtmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 6)
)
_Hh3cevtPortRt_AtmT1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmT1 = _Hh3cevtPortRt_AtmT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 7)
)
_Hh3cevtPortRt_AtmE3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmE3 = _Hh3cevtPortRt_AtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 8)
)
_Hh3cevtPortRt_AtmT3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmT3 = _Hh3cevtPortRt_AtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 9)
)
_Hh3cevtPortRt_Atm622M_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Atm622M = _Hh3cevtPortRt_Atm622M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 10)
)
_Hh3cevtPortRt_AtmImaE1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmImaE1 = _Hh3cevtPortRt_AtmImaE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 11)
)
_Hh3cevtPortRt_AtmImaT1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmImaT1 = _Hh3cevtPortRt_AtmImaT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 12)
)
_Hh3cevtPortRt_Atm25M_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Atm25M = _Hh3cevtPortRt_Atm25M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 13)
)
_Hh3cevtPortRt_Bri_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Bri = _Hh3cevtPortRt_Bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 14)
)
_Hh3cevtPortRt_Console_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Console = _Hh3cevtPortRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 15)
)
_Hh3cevtPortRt_E1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E1 = _Hh3cevtPortRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 16)
)
_Hh3cevtPortRt_E3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E3 = _Hh3cevtPortRt_E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 17)
)
_Hh3cevtPortRt_T1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T1 = _Hh3cevtPortRt_T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 18)
)
_Hh3cevtPortRt_T3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T3 = _Hh3cevtPortRt_T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 19)
)
_Hh3cevtPortRt_Cpos_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Cpos = _Hh3cevtPortRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 20)
)
_Hh3cevtPortRt_Ethernet_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Ethernet = _Hh3cevtPortRt_Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 21)
)
_Hh3cevtPortRt_Serial_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Serial = _Hh3cevtPortRt_Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 22)
)
_Hh3cevtPortRt_E1f_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E1f = _Hh3cevtPortRt_E1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 23)
)
_Hh3cevtPortRt_T1f_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T1f = _Hh3cevtPortRt_T1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 24)
)
_Hh3cevtPortRt_Pos_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Pos = _Hh3cevtPortRt_Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 25)
)
_Hh3cevtPortRt_Ge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Ge = _Hh3cevtPortRt_Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 26)
)
_Hh3cevtPortRt_Aux_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Aux = _Hh3cevtPortRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 27)
)
_Hh3cevtPortRt_VG_Fxs_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_Fxs = _Hh3cevtPortRt_VG_Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 30)
)
_Hh3cevtPortRt_VG_Fxo_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_Fxo = _Hh3cevtPortRt_VG_Fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 31)
)
_Hh3cevtPortRt_VG_E1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_E1vi = _Hh3cevtPortRt_VG_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 32)
)
_Hh3cevtPortRt_VG_T1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_T1vi = _Hh3cevtPortRt_VG_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 33)
)
_Hh3cevtPortRt_Usb_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Usb = _Hh3cevtPortRt_Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 34)
)
_Hh3cevtPortRt_Ndec_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Ndec = _Hh3cevtPortRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 35)
)
_Hh3cevtPortRt_Cavium_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Cavium = _Hh3cevtPortRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 36)
)
_Hh3cevtPortRt_Fcm_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Fcm = _Hh3cevtPortRt_Fcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 37)
)
_Hh3cevtPortRt_E1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E1vi = _Hh3cevtPortRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 38)
)
_Hh3cevtPortRt_T1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T1vi = _Hh3cevtPortRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 39)
)
_Hh3cevtPortRt_Vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Vi = _Hh3cevtPortRt_Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 40)
)
_Hh3cevtPortRt_Adls2Plus_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Adls2Plus = _Hh3cevtPortRt_Adls2Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 41)
)
_Hh3cevtPortRt_RADIO_AG_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_RADIO_AG = _Hh3cevtPortRt_RADIO_AG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 42)
)
_Hh3cevtPortRt_1exp_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_1exp = _Hh3cevtPortRt_1exp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 43)
)
_Hh3cevtPortRt_G_SHDSL_BIS_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_G_SHDSL_BIS = _Hh3cevtPortRt_G_SHDSL_BIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 44)
)
_Hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC = _Hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 45)
)
_Hh3cevtPortRt_CELLULAR_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_CELLULAR = _Hh3cevtPortRt_CELLULAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 46)
)
_Hh3cevtPortSwitchType_ObjectIdentity = ObjectIdentity
hh3cevtPortSwitchType = _Hh3cevtPortSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4)
)
_Hh3cevtPortSw_10or100M_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10or100M = _Hh3cevtPortSw_10or100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 1)
)
_Hh3cevtPortSw_1000BaseLxSm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseLxSm = _Hh3cevtPortSw_1000BaseLxSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 2)
)
_Hh3cevtPortSw_1000BaseSxMm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseSxMm = _Hh3cevtPortSw_1000BaseSxMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 3)
)
_Hh3cevtPortSw_1000BaseTx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseTx = _Hh3cevtPortSw_1000BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 4)
)
_Hh3cevtPortSw_100MSinglemodeFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MSinglemodeFx = _Hh3cevtPortSw_100MSinglemodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 5)
)
_Hh3cevtPortSw_100MMultimodeFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MMultimodeFx = _Hh3cevtPortSw_100MMultimodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 6)
)
_Hh3cevtPortSw_100M100BaseTx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100M100BaseTx = _Hh3cevtPortSw_100M100BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 7)
)
_Hh3cevtPortSw_100MHub_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MHub = _Hh3cevtPortSw_100MHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 8)
)
_Hh3cevtPortSw_Vdsl_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Vdsl = _Hh3cevtPortSw_Vdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 9)
)
_Hh3cevtPortSw_Stack_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Stack = _Hh3cevtPortSw_Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 10)
)
_Hh3cevtPortSw_1000BaseZenithFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseZenithFx = _Hh3cevtPortSw_1000BaseZenithFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 11)
)
_Hh3cevtPortSw_1000BaseLongFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseLongFx = _Hh3cevtPortSw_1000BaseLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 12)
)
_Hh3cevtPortSw_Adsl_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Adsl = _Hh3cevtPortSw_Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 13)
)
_Hh3cevtPortSw_10or100MDb_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10or100MDb = _Hh3cevtPortSw_10or100MDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 14)
)
_Hh3cevtPortSw_10GBaseLrSm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBaseLrSm = _Hh3cevtPortSw_10GBaseLrSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 15)
)
_Hh3cevtPortSw_10GBaseLx4Mm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBaseLx4Mm = _Hh3cevtPortSw_10GBaseLx4Mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 16)
)
_Hh3cevtPortSw_10GBaseLx4Sm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBaseLx4Sm = _Hh3cevtPortSw_10GBaseLx4Sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 17)
)
_Hh3cevtPortSw_100MLongFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MLongFx = _Hh3cevtPortSw_100MLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 18)
)
_Hh3cevtPortSw_1000BaseCx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseCx = _Hh3cevtPortSw_1000BaseCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 19)
)
_Hh3cevtPortSw_1000BaseZenithFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseZenithFxLc = _Hh3cevtPortSw_1000BaseZenithFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 20)
)
_Hh3cevtPortSw_1000BaseLongFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseLongFxLc = _Hh3cevtPortSw_1000BaseLongFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 21)
)
_Hh3cevtPortSw_100MSmFxSc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MSmFxSc = _Hh3cevtPortSw_100MSmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 22)
)
_Hh3cevtPortSw_100MMmFxSc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MMmFxSc = _Hh3cevtPortSw_100MMmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 23)
)
_Hh3cevtPortSw_100MSmFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MSmFxLc = _Hh3cevtPortSw_100MSmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 24)
)
_Hh3cevtPortSw_100MMmFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MMmFxLc = _Hh3cevtPortSw_100MMmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 25)
)
_Hh3cevtPortSw_GbicNoConnector_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_GbicNoConnector = _Hh3cevtPortSw_GbicNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 26)
)
_Hh3cevtPortSw_Gbic1000BaseT_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseT = _Hh3cevtPortSw_Gbic1000BaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 27)
)
_Hh3cevtPortSw_Gbic1000BaseLx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseLx = _Hh3cevtPortSw_Gbic1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 28)
)
_Hh3cevtPortSw_Gbic1000BaseSx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseSx = _Hh3cevtPortSw_Gbic1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 29)
)
_Hh3cevtPortSw_Gbic1000BaseZx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseZx = _Hh3cevtPortSw_Gbic1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 30)
)
_Hh3cevtPortSw_ComboNoConnector_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_ComboNoConnector = _Hh3cevtPortSw_ComboNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 31)
)
_Hh3cevtPortSw_Combo1000BaseLx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseLx = _Hh3cevtPortSw_Combo1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 32)
)
_Hh3cevtPortSw_Combo1000BaseLxFiber_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseLxFiber = _Hh3cevtPortSw_Combo1000BaseLxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 33)
)
_Hh3cevtPortSw_Combo1000BaseLxCopper_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseLxCopper = _Hh3cevtPortSw_Combo1000BaseLxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 34)
)
_Hh3cevtPortSw_Combo1000BaseSx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseSx = _Hh3cevtPortSw_Combo1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 35)
)
_Hh3cevtPortSw_Combo1000BaseSxFiber_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseSxFiber = _Hh3cevtPortSw_Combo1000BaseSxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 36)
)
_Hh3cevtPortSw_Combo1000BaseSxCopper_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseSxCopper = _Hh3cevtPortSw_Combo1000BaseSxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 37)
)
_Hh3cevtPortSw_Combo1000BaseZx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseZx = _Hh3cevtPortSw_Combo1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 38)
)
_Hh3cevtPortSw_Combo1000BaseZxFiber_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseZxFiber = _Hh3cevtPortSw_Combo1000BaseZxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 39)
)
_Hh3cevtPortSw_Combo1000BaseZxCopper_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseZxCopper = _Hh3cevtPortSw_Combo1000BaseZxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 40)
)
_Hh3cevtPortSw_155PosSxMmf_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155PosSxMmf = _Hh3cevtPortSw_155PosSxMmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 41)
)
_Hh3cevtPortSw_155PosLxSmf_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155PosLxSmf = _Hh3cevtPortSw_155PosLxSmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 42)
)
_Hh3cevtPortSw_1000BASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_T = _Hh3cevtPortSw_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 43)
)
_Hh3cevtPortSw_1000BASE_SX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_SX_SFP = _Hh3cevtPortSw_1000BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 44)
)
_Hh3cevtPortSw_1000BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_LX_SFP = _Hh3cevtPortSw_1000BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 45)
)
_Hh3cevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_T_AN_SFP = _Hh3cevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 46)
)
_Hh3cevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_LX4_XENPAK = _Hh3cevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 47)
)
_Hh3cevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_LR_XENPAK = _Hh3cevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 48)
)
_Hh3cevtPortSw_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_CX4 = _Hh3cevtPortSw_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 49)
)
_Hh3cevtPortSw_1000BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_ZX_SFP = _Hh3cevtPortSw_1000BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 50)
)
_Hh3cevtPortSw_1000BASE_MM_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_MM_SFP = _Hh3cevtPortSw_1000BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 51)
)
_Hh3cevtPortSw_100BASE_SX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_SX_SFP = _Hh3cevtPortSw_100BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 52)
)
_Hh3cevtPortSw_100BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_LX_SFP = _Hh3cevtPortSw_100BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 53)
)
_Hh3cevtPortSw_100BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_T_AN_SFP = _Hh3cevtPortSw_100BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 54)
)
_Hh3cevtPortSw_100BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_ZX_SFP = _Hh3cevtPortSw_100BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 55)
)
_Hh3cevtPortSw_100BASE_MM_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_MM_SFP = _Hh3cevtPortSw_100BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 56)
)
_Hh3cevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_NO_CONNECTOR = _Hh3cevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 57)
)
_Hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR = _Hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 58)
)
_Hh3cevtPortSw_POS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_NO_CONNECTOR = _Hh3cevtPortSw_POS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 59)
)
_Hh3cevtPortSw_10G_BASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_SR = _Hh3cevtPortSw_10G_BASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 60)
)
_Hh3cevtPortSw_10G_BASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_ER = _Hh3cevtPortSw_10G_BASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 61)
)
_Hh3cevtPortSw_10G_BASE_LX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_LX4 = _Hh3cevtPortSw_10G_BASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 62)
)
_Hh3cevtPortSw_10G_BASE_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_SW = _Hh3cevtPortSw_10G_BASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 63)
)
_Hh3cevtPortSw_10G_BASE_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_LW = _Hh3cevtPortSw_10G_BASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 64)
)
_Hh3cevtPortSw_10G_BASE_EW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_EW = _Hh3cevtPortSw_10G_BASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 65)
)
_Hh3cevtPortSw_10G_LR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_LR_SM_LC = _Hh3cevtPortSw_10G_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 66)
)
_Hh3cevtPortSw_10G_SR_MM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_SR_MM_LC = _Hh3cevtPortSw_10G_SR_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 67)
)
_Hh3cevtPortSw_10G_ER_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_ER_SM_LC = _Hh3cevtPortSw_10G_ER_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 68)
)
_Hh3cevtPortSw_10G_LW_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_LW_SM_LC = _Hh3cevtPortSw_10G_LW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 69)
)
_Hh3cevtPortSw_10G_SW_MM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_SW_MM_LC = _Hh3cevtPortSw_10G_SW_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 70)
)
_Hh3cevtPortSw_10G_EW_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_EW_SM_LC = _Hh3cevtPortSw_10G_EW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 71)
)
_Hh3cevtPortSw_100BASE_SM_MTRJ_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_SM_MTRJ = _Hh3cevtPortSw_100BASE_SM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 72)
)
_Hh3cevtPortSw_100BASE_MM_MTRJ_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_MM_MTRJ = _Hh3cevtPortSw_100BASE_MM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 73)
)
_Hh3cevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_NO_CONNECTOR = _Hh3cevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 74)
)
_Hh3cevtPortSw_XFP_10GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_SR = _Hh3cevtPortSw_XFP_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 75)
)
_Hh3cevtPortSw_XFP_10GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_LR = _Hh3cevtPortSw_XFP_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 76)
)
_Hh3cevtPortSw_XFP_10GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_ER = _Hh3cevtPortSw_XFP_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 77)
)
_Hh3cevtPortSw_XFP_10GBASE_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_SW = _Hh3cevtPortSw_XFP_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 78)
)
_Hh3cevtPortSw_XFP_10GBASE_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_LW = _Hh3cevtPortSw_XFP_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 79)
)
_Hh3cevtPortSw_XFP_10GBASE_EW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_EW = _Hh3cevtPortSw_XFP_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 80)
)
_Hh3cevtPortSw_XFP_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_CX4 = _Hh3cevtPortSw_XFP_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 81)
)
_Hh3cevtPortSw_XFP_10GBASE_LX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_LX4 = _Hh3cevtPortSw_XFP_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 82)
)
_Hh3cevtPortSw_XFP_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_UNKNOWN = _Hh3cevtPortSw_XFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 83)
)
_Hh3cevtPortSw_XPK_NOCONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_NOCONNECTOR = _Hh3cevtPortSw_XPK_NOCONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 84)
)
_Hh3cevtPortSw_XPK_10GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_SR = _Hh3cevtPortSw_XPK_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 85)
)
_Hh3cevtPortSw_XPK_10GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_LR = _Hh3cevtPortSw_XPK_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 86)
)
_Hh3cevtPortSw_XPK_10GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_ER = _Hh3cevtPortSw_XPK_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 87)
)
_Hh3cevtPortSw_XPK_10GBASE_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_SW = _Hh3cevtPortSw_XPK_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 88)
)
_Hh3cevtPortSw_XPK_10GBASE_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_LW = _Hh3cevtPortSw_XPK_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 89)
)
_Hh3cevtPortSw_XPK_10GBASE_EW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_EW = _Hh3cevtPortSw_XPK_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 90)
)
_Hh3cevtPortSw_XPK_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_CX4 = _Hh3cevtPortSw_XPK_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 91)
)
_Hh3cevtPortSw_XPK_10GBASE_LX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_LX4 = _Hh3cevtPortSw_XPK_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 92)
)
_Hh3cevtPortSw_XPK_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_UNKNOWN = _Hh3cevtPortSw_XPK_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 93)
)
_Hh3cevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_SR_SM_LC = _Hh3cevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 94)
)
_Hh3cevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_SM_LC = _Hh3cevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 95)
)
_Hh3cevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_SM_LC = _Hh3cevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 96)
)
_Hh3cevtPortSw_10G_BASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_CX4 = _Hh3cevtPortSw_10G_BASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 97)
)
_Hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC = _Hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 98)
)
_Hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC = _Hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 99)
)
_Hh3cevtPortSw_24G_CASCADE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_24G_CASCADE = _Hh3cevtPortSw_24G_CASCADE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 100)
)
_Hh3cevtPortSw_POS_OC3_SR_MM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_SR_MM = _Hh3cevtPortSw_POS_OC3_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 101)
)
_Hh3cevtPortSw_POS_OC3_IR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_IR_SM = _Hh3cevtPortSw_POS_OC3_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 102)
)
_Hh3cevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_IR_1_SM = _Hh3cevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 103)
)
_Hh3cevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_IR_2_SM = _Hh3cevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 104)
)
_Hh3cevtPortSw_POS_OC3_LR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_SM = _Hh3cevtPortSw_POS_OC3_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 105)
)
_Hh3cevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_1_SM = _Hh3cevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 106)
)
_Hh3cevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_2_SM = _Hh3cevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 107)
)
_Hh3cevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_3_SM = _Hh3cevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 108)
)
_Hh3cevtPortSw_POS_OC12_SR_MM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_SR_MM = _Hh3cevtPortSw_POS_OC12_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 109)
)
_Hh3cevtPortSw_POS_OC12_IR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_IR_SM = _Hh3cevtPortSw_POS_OC12_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 110)
)
_Hh3cevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_IR_1_SM = _Hh3cevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 111)
)
_Hh3cevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_IR_2_SM = _Hh3cevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 112)
)
_Hh3cevtPortSw_POS_OC12_LR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_SM = _Hh3cevtPortSw_POS_OC12_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 113)
)
_Hh3cevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_1_SM = _Hh3cevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 114)
)
_Hh3cevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_2_SM = _Hh3cevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 115)
)
_Hh3cevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_3_SM = _Hh3cevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 116)
)
_Hh3cevtPortSw_POS_OC48_SR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_SR_SM = _Hh3cevtPortSw_POS_OC48_SR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 117)
)
_Hh3cevtPortSw_POS_OC48_IR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_SM = _Hh3cevtPortSw_POS_OC48_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 118)
)
_Hh3cevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_1_SM = _Hh3cevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 119)
)
_Hh3cevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_2_SM = _Hh3cevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 120)
)
_Hh3cevtPortSw_POS_OC48_LR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_SM = _Hh3cevtPortSw_POS_OC48_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 121)
)
_Hh3cevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_1_SM = _Hh3cevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 122)
)
_Hh3cevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_2_SM = _Hh3cevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 123)
)
_Hh3cevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_3_SM = _Hh3cevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 124)
)
_Hh3cevtPortSw_POS_I_64_1_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_1 = _Hh3cevtPortSw_POS_I_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 125)
)
_Hh3cevtPortSw_POS_I_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_2 = _Hh3cevtPortSw_POS_I_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 126)
)
_Hh3cevtPortSw_POS_I_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_3 = _Hh3cevtPortSw_POS_I_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 127)
)
_Hh3cevtPortSw_POS_I_64_5_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_5 = _Hh3cevtPortSw_POS_I_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 128)
)
_Hh3cevtPortSw_POS_S_64_1_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_1 = _Hh3cevtPortSw_POS_S_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 129)
)
_Hh3cevtPortSw_POS_S_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_2 = _Hh3cevtPortSw_POS_S_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 130)
)
_Hh3cevtPortSw_POS_S_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_3 = _Hh3cevtPortSw_POS_S_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 131)
)
_Hh3cevtPortSw_POS_S_64_5_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_5 = _Hh3cevtPortSw_POS_S_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 132)
)
_Hh3cevtPortSw_POS_L_64_1_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_1 = _Hh3cevtPortSw_POS_L_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 133)
)
_Hh3cevtPortSw_POS_L_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_2 = _Hh3cevtPortSw_POS_L_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 134)
)
_Hh3cevtPortSw_POS_L_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_3 = _Hh3cevtPortSw_POS_L_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 135)
)
_Hh3cevtPortSw_POS_V_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_V_64_2 = _Hh3cevtPortSw_POS_V_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 136)
)
_Hh3cevtPortSw_POS_V_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_V_64_3 = _Hh3cevtPortSw_POS_V_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 137)
)
_Hh3cevtPortSw_100BASE_FX_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_FX_BIDI = _Hh3cevtPortSw_100BASE_FX_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 138)
)
_Hh3cevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_BX10_U_SFP = _Hh3cevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 139)
)
_Hh3cevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_BX10_D_SFP = _Hh3cevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 140)
)
_Hh3cevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_BX10_U_SFP = _Hh3cevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 141)
)
_Hh3cevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_BX10_D_SFP = _Hh3cevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 142)
)
_Hh3cevtPortSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_STK_1000BASE_T = _Hh3cevtPortSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 143)
)
_Hh3cevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHYPOS_CONNECTOR = _Hh3cevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 144)
)
_Hh3cevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHY10GE_CONNECTOR = _Hh3cevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 145)
)
_Hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR = _Hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 146)
)
_Hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR = _Hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 147)
)
_Hh3cevtPortSw_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_ZR = _Hh3cevtPortSw_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 148)
)
_Hh3cevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_TYPE_ERROR_CONNECTOR = _Hh3cevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 149)
)
_Hh3cevtPortSw_10G_STACK_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_STACK = _Hh3cevtPortSw_10G_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 150)
)
_Hh3cevtPortSw_155_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_ATM_SX_MMF = _Hh3cevtPortSw_155_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 151)
)
_Hh3cevtPortSw_155_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_ATM_LX_SMF = _Hh3cevtPortSw_155_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 152)
)
_Hh3cevtPortSw_622_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_ATM_SX_MMF = _Hh3cevtPortSw_622_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 153)
)
_Hh3cevtPortSw_622_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_ATM_LX_SMF = _Hh3cevtPortSw_622_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 154)
)
_Hh3cevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_ATM_NO_CONNECTOR = _Hh3cevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 155)
)
_Hh3cevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_ATM_NO_CONNECTOR = _Hh3cevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 156)
)
_Hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR = _Hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 157)
)
_Hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR = _Hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 158)
)
_Hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR = _Hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 159)
)
_Hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR = _Hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 160)
)
_Hh3cevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_E1_SX_MMF = _Hh3cevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 161)
)
_Hh3cevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_T1_SX_MMF = _Hh3cevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 162)
)
_Hh3cevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_E1_LX_SMF = _Hh3cevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 163)
)
_Hh3cevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_T1_LX_SMF = _Hh3cevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 164)
)
_Hh3cevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_E1_SX_MMF = _Hh3cevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 165)
)
_Hh3cevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_T1_SX_MMF = _Hh3cevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 166)
)
_Hh3cevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_E1_LX_SMF = _Hh3cevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 167)
)
_Hh3cevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_T1_LX_SMF = _Hh3cevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 168)
)
_Hh3cevtPortSw_E1_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_E1_CONNECTOR = _Hh3cevtPortSw_E1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 169)
)
_Hh3cevtPortSw_T1_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_T1_CONNECTOR = _Hh3cevtPortSw_T1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 170)
)
_Hh3cevtPortSw_1000BASE_STK_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_STK_SFP = _Hh3cevtPortSw_1000BASE_STK_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 171)
)
_Hh3cevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_BIDI_SFP = _Hh3cevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 172)
)
_Hh3cevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_CWDM_SFP = _Hh3cevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 173)
)
_Hh3cevtPortSw_100BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_BIDI_SFP = _Hh3cevtPortSw_100BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 174)
)
_Hh3cevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_OLT_1000BASE_PX_SFP = _Hh3cevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 175)
)
_Hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR = _Hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 176)
)
_Hh3cevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHYGE_CONNECTOR = _Hh3cevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 177)
)
_Hh3cevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGICGE_CONNECTOR = _Hh3cevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 178)
)
_Hh3cevtPortSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100M_1550_BIDI = _Hh3cevtPortSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 179)
)
_Hh3cevtPortSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100M_1310_BIDI = _Hh3cevtPortSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 180)
)
_Hh3cevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHYOC48_CONNECTOR = _Hh3cevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 181)
)
_Hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR = _Hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 182)
)
_Hh3cevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100_1000_BASE_LX_SMF = _Hh3cevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 183)
)
_Hh3cevtPortSw_10G_ZW_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_ZW_SM_LC = _Hh3cevtPortSw_10G_ZW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 184)
)
_Hh3cevtPortSw_10G_ZR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_ZR_SM_LC = _Hh3cevtPortSw_10G_ZR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 185)
)
_Hh3cevtPortSw_XPK_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_ZR = _Hh3cevtPortSw_XPK_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 186)
)
_Hh3cevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SGMII_100_BASE_LX_SFP = _Hh3cevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 187)
)
_Hh3cevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SGMII_100_BASE_FX_SFP = _Hh3cevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 188)
)
_Hh3cevtPortSw_WLAN_RADIO_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_WLAN_RADIO = _Hh3cevtPortSw_WLAN_RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 189)
)
_Hh3cevtPortSw_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CABLE = _Hh3cevtPortSw_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 190)
)
_Hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR = _Hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 191)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_SR = _Hh3cevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 192)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_LR = _Hh3cevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 193)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_LRM = _Hh3cevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 194)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_Cu = _Hh3cevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 195)
)
_Hh3cevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_UNKNOWN = _Hh3cevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 196)
)
_Hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR = _Hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 197)
)
_Hh3cevtPortSw_POS_L_64_4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_4 = _Hh3cevtPortSw_POS_L_64_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 198)
)
_Hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR = _Hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 199)
)
_Hh3cevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_ONU_1000BASE_PX_SFF = _Hh3cevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 200)
)
_Hh3cevtPortSw_RS485_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RS485 = _Hh3cevtPortSw_RS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 201)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_ER = _Hh3cevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 202)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_ZR = _Hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 203)
)
_Hh3cevtPortSw_XFP_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_ZR = _Hh3cevtPortSw_XFP_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 204)
)
_Hh3cevtStack_ObjectIdentity = ObjectIdentity
hh3cevtStack = _Hh3cevtStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ENTITY-VENDORTYPE-OID-MIB",
    **{"hh3cEntityVendorTypeOID": hh3cEntityVendorTypeOID,
       "hh3cEntityVendortypeObjects": hh3cEntityVendortypeObjects,
       "hh3cevtOther": hh3cevtOther,
       "hh3cevtOtherUnknownCard": hh3cevtOtherUnknownCard,
       "hh3cevtCPU": hh3cevtCPU,
       "hh3cevtGeneralCPU": hh3cevtGeneralCPU,
       "hh3cevtDOM": hh3cevtDOM,
       "hh3cevtCFCard": hh3cevtCFCard,
       "hh3cevtHardDisk": hh3cevtHardDisk,
       "hh3cevtUnknown": hh3cevtUnknown,
       "hh3cevtChassis": hh3cevtChassis,
       "hh3cevtBackplane": hh3cevtBackplane,
       "hh3cevtContainer": hh3cevtContainer,
       "hh3cevtPowerSupply": hh3cevtPowerSupply,
       "hh3cevtPowerSupplyAC": hh3cevtPowerSupplyAC,
       "hh3cevtPowerSupplyDC": hh3cevtPowerSupplyDC,
       "hh3cevtPowerSupplySTD130W": hh3cevtPowerSupplySTD130W,
       "hh3cevtPowerSupplySTD180W": hh3cevtPowerSupplySTD180W,
       "hh3cevtPowerSupplyPOE24Port": hh3cevtPowerSupplyPOE24Port,
       "hh3cevtPowerSupplyPOE48Port": hh3cevtPowerSupplyPOE48Port,
       "hh3cevtFan": hh3cevtFan,
       "hh3cevtHotSwapFan": hh3cevtHotSwapFan,
       "hh3cevtNonHotSwapFan": hh3cevtNonHotSwapFan,
       "hh3cevtSensor": hh3cevtSensor,
       "hh3cevtSensorTemperature": hh3cevtSensorTemperature,
       "hh3cevtSensorVoltage": hh3cevtSensorVoltage,
       "hh3cevtSensorFanSpeed": hh3cevtSensorFanSpeed,
       "hh3cevtModule": hh3cevtModule,
       "hh3cevtModuleUnknownCard": hh3cevtModuleUnknownCard,
       "hh3cevtModuleCommonCards": hh3cevtModuleCommonCards,
       "hh3cevtModuleRouterType": hh3cevtModuleRouterType,
       "hh3cevtModuleRt-As": hh3cevtModuleRt_As,
       "hh3cevtModuleRt-Sa": hh3cevtModuleRt_Sa,
       "hh3cevtModuleRt-Bi": hh3cevtModuleRt_Bi,
       "hh3cevtModuleRt-E12": hh3cevtModuleRt_E12,
       "hh3cevtModuleRt-E14": hh3cevtModuleRt_E14,
       "hh3cevtModuleRt-Fe1": hh3cevtModuleRt_Fe1,
       "hh3cevtModuleRt-E1": hh3cevtModuleRt_E1,
       "hh3cevtModuleRt-Fe2": hh3cevtModuleRt_Fe2,
       "hh3cevtModuleRt-Vi2": hh3cevtModuleRt_Vi2,
       "hh3cevtModuleRt-Vi4": hh3cevtModuleRt_Vi4,
       "hh3cevtModuleRt-Vi30": hh3cevtModuleRt_Vi30,
       "hh3cevtModuleRt-S1b": hh3cevtModuleRt_S1b,
       "hh3cevtModuleRt-Sa2": hh3cevtModuleRt_Sa2,
       "hh3cevtModuleRt-As16": hh3cevtModuleRt_As16,
       "hh3cevtModuleRt-New8as": hh3cevtModuleRt_New8as,
       "hh3cevtModuleRt-Sa1": hh3cevtModuleRt_Sa1,
       "hh3cevtModuleRt-Fxs2": hh3cevtModuleRt_Fxs2,
       "hh3cevtModuleRt-Fxo2": hh3cevtModuleRt_Fxo2,
       "hh3cevtModuleRt-Em2": hh3cevtModuleRt_Em2,
       "hh3cevtModuleRt-Fxs4": hh3cevtModuleRt_Fxs4,
       "hh3cevtModuleRt-Fxo4": hh3cevtModuleRt_Fxo4,
       "hh3cevtModuleRt-Em4": hh3cevtModuleRt_Em4,
       "hh3cevtModuleRt-Sab": hh3cevtModuleRt_Sab,
       "hh3cevtModuleRt-E1vi": hh3cevtModuleRt_E1vi,
       "hh3cevtModuleRt-Am12": hh3cevtModuleRt_Am12,
       "hh3cevtModuleRt-Am6": hh3cevtModuleRt_Am6,
       "hh3cevtModuleRt-Ndec": hh3cevtModuleRt_Ndec,
       "hh3cevtModuleRt-Newsa2": hh3cevtModuleRt_Newsa2,
       "hh3cevtModuleRt-Aux": hh3cevtModuleRt_Aux,
       "hh3cevtModuleRt-Console": hh3cevtModuleRt_Console,
       "hh3cevtModuleRt-Sic-wan": hh3cevtModuleRt_Sic_wan,
       "hh3cevtModuleRt-Sic-1fe": hh3cevtModuleRt_Sic_1fe,
       "hh3cevtModuleRt-Sic-1sa": hh3cevtModuleRt_Sic_1sa,
       "hh3cevtModuleRt-Sic-3as": hh3cevtModuleRt_Sic_3as,
       "hh3cevtModuleRt-Sic-1e1": hh3cevtModuleRt_Sic_1e1,
       "hh3cevtModuleRt-Sic-1t1": hh3cevtModuleRt_Sic_1t1,
       "hh3cevtModuleRt-Sic-1bu": hh3cevtModuleRt_Sic_1bu,
       "hh3cevtModuleRt-Sic-2bu": hh3cevtModuleRt_Sic_2bu,
       "hh3cevtModuleRt-Sic-1bs": hh3cevtModuleRt_Sic_1bs,
       "hh3cevtModuleRt-Sic-2bs": hh3cevtModuleRt_Sic_2bs,
       "hh3cevtModuleRt-Sic-1am": hh3cevtModuleRt_Sic_1am,
       "hh3cevtModuleRt-Sic-2am": hh3cevtModuleRt_Sic_2am,
       "hh3cevtModuleRt-Sic-1em": hh3cevtModuleRt_Sic_1em,
       "hh3cevtModuleRt-Sic-2em": hh3cevtModuleRt_Sic_2em,
       "hh3cevtModuleRt-Sic-1fxs": hh3cevtModuleRt_Sic_1fxs,
       "hh3cevtModuleRt-Sic-2fxs": hh3cevtModuleRt_Sic_2fxs,
       "hh3cevtModuleRt-Sic-1fxo": hh3cevtModuleRt_Sic_1fxo,
       "hh3cevtModuleRt-Sic-2fxo": hh3cevtModuleRt_Sic_2fxo,
       "hh3cevtModuleRt-Fcm6": hh3cevtModuleRt_Fcm6,
       "hh3cevtModuleRt-Sa8": hh3cevtModuleRt_Sa8,
       "hh3cevtModuleRt-T11": hh3cevtModuleRt_T11,
       "hh3cevtModuleRt-T12": hh3cevtModuleRt_T12,
       "hh3cevtModuleRt-T14": hh3cevtModuleRt_T14,
       "hh3cevtModuleRt-T1vi": hh3cevtModuleRt_T1vi,
       "hh3cevtModuleRt-Fcm4": hh3cevtModuleRt_Fcm4,
       "hh3cevtModuleRt-Fcm2": hh3cevtModuleRt_Fcm2,
       "hh3cevtModuleRt-Rtb21ce3": hh3cevtModuleRt_Rtb21ce3,
       "hh3cevtModuleRt-Ame6": hh3cevtModuleRt_Ame6,
       "hh3cevtModuleRt-Ame12": hh3cevtModuleRt_Ame12,
       "hh3cevtModuleRt-E11-f": hh3cevtModuleRt_E11_f,
       "hh3cevtModuleRt-E12-f": hh3cevtModuleRt_E12_f,
       "hh3cevtModuleRt-E14-f": hh3cevtModuleRt_E14_f,
       "hh3cevtModuleRt-T11-f": hh3cevtModuleRt_T11_f,
       "hh3cevtModuleRt-T12-f": hh3cevtModuleRt_T12_f,
       "hh3cevtModuleRt-T14-f": hh3cevtModuleRt_T14_f,
       "hh3cevtModuleRt-E11-f-17": hh3cevtModuleRt_E11_f_17,
       "hh3cevtModuleRt-T11-f-17": hh3cevtModuleRt_T11_f_17,
       "hh3cevtModuleRt-Rtb21ct3": hh3cevtModuleRt_Rtb21ct3,
       "hh3cevtModuleRt-Atmadsl1": hh3cevtModuleRt_Atmadsl1,
       "hh3cevtModuleRt-Atmadsl2": hh3cevtModuleRt_Atmadsl2,
       "hh3cevtModuleRt-Atm155m": hh3cevtModuleRt_Atm155m,
       "hh3cevtModuleRt-Ase8": hh3cevtModuleRt_Ase8,
       "hh3cevtModuleRt-Ase16": hh3cevtModuleRt_Ase16,
       "hh3cevtModuleRt-Sae4": hh3cevtModuleRt_Sae4,
       "hh3cevtModuleRt-Sae2": hh3cevtModuleRt_Sae2,
       "hh3cevtModuleRt-Atmshdsl1": hh3cevtModuleRt_Atmshdsl1,
       "hh3cevtModuleRt-Atmshdsl2": hh3cevtModuleRt_Atmshdsl2,
       "hh3cevtModuleRt-Atmshdsl4": hh3cevtModuleRt_Atmshdsl4,
       "hh3cevtModuleRt-Atm25m": hh3cevtModuleRt_Atm25m,
       "hh3cevtModuleRt-Atme3": hh3cevtModuleRt_Atme3,
       "hh3cevtModuleRt-Atmt3": hh3cevtModuleRt_Atmt3,
       "hh3cevtModuleRt-Xdsl-fec": hh3cevtModuleRt_Xdsl_fec,
       "hh3cevtModuleRt-Xdsl-adsl": hh3cevtModuleRt_Xdsl_adsl,
       "hh3cevtModuleRt-Xdsl-gshdsl": hh3cevtModuleRt_Xdsl_gshdsl,
       "hh3cevtModuleRt-Xdsl-bri": hh3cevtModuleRt_Xdsl_bri,
       "hh3cevtModuleRt-Xdsl-scc": hh3cevtModuleRt_Xdsl_scc,
       "hh3cevtModuleRt-Ge1": hh3cevtModuleRt_Ge1,
       "hh3cevtModuleRt-Pos155m": hh3cevtModuleRt_Pos155m,
       "hh3cevtModuleRt-Cpos": hh3cevtModuleRt_Cpos,
       "hh3cevtModuleRt-Fe1op": hh3cevtModuleRt_Fe1op,
       "hh3cevtModuleRt-Sae8": hh3cevtModuleRt_Sae8,
       "hh3cevtModuleRt-Atm155m-mm": hh3cevtModuleRt_Atm155m_mm,
       "hh3cevtModuleRt-Atm155m-sm": hh3cevtModuleRt_Atm155m_sm,
       "hh3cevtModuleRt-Atm155m-sml": hh3cevtModuleRt_Atm155m_sml,
       "hh3cevtModuleRt-Fe1op-sfx": hh3cevtModuleRt_Fe1op_sfx,
       "hh3cevtModuleRt-Fe1op-mfx": hh3cevtModuleRt_Fe1op_mfx,
       "hh3cevtModuleRt-Cpos-t1": hh3cevtModuleRt_Cpos_t1,
       "hh3cevtModuleRt-Ge1op": hh3cevtModuleRt_Ge1op,
       "hh3cevtModuleRt-Ge2op": hh3cevtModuleRt_Ge2op,
       "hh3cevtModuleRt-Ge2": hh3cevtModuleRt_Ge2,
       "hh3cevtModuleRt-Fix-1wan": hh3cevtModuleRt_Fix_1wan,
       "hh3cevtModuleRt-Fix-1sae": hh3cevtModuleRt_Fix_1sae,
       "hh3cevtModuleRt-Cavium": hh3cevtModuleRt_Cavium,
       "hh3cevtModuleRt-Sic1Eth": hh3cevtModuleRt_Sic1Eth,
       "hh3cevtModuleRt-atm1ADSLI": hh3cevtModuleRt_atm1ADSLI,
       "hh3cevtModuleRt-atm2ADSLI": hh3cevtModuleRt_atm2ADSLI,
       "hh3cevtModuleRt-fix-e11": hh3cevtModuleRt_fix_e11,
       "hh3cevtModuleRt-fix-t11": hh3cevtModuleRt_fix_t11,
       "hh3cevtModuleRt-e18-75": hh3cevtModuleRt_e18_75,
       "hh3cevtModuleRt-e18-120": hh3cevtModuleRt_e18_120,
       "hh3cevtModuleRt-t18": hh3cevtModuleRt_t18,
       "hh3cevtModuleRt-sic-1vifxs": hh3cevtModuleRt_sic_1vifxs,
       "hh3cevtModuleRt-sic-1vifxo": hh3cevtModuleRt_sic_1vifxo,
       "hh3cevtModuleRt-sic-2vifxs": hh3cevtModuleRt_sic_2vifxs,
       "hh3cevtModuleRt-sic-2vifxo": hh3cevtModuleRt_sic_2vifxo,
       "hh3cevtModuleRt-xdsl-fec-new": hh3cevtModuleRt_xdsl_fec_new,
       "hh3cevtModuleRt-xdsl-sa": hh3cevtModuleRt_xdsl_sa,
       "hh3cevtModuleRt-bs4": hh3cevtModuleRt_bs4,
       "hh3cevtModuleRt-ima-8e175": hh3cevtModuleRt_ima_8e175,
       "hh3cevtModuleRt-ima-8e1120": hh3cevtModuleRt_ima_8e1120,
       "hh3cevtModuleRt-ima-4e175": hh3cevtModuleRt_ima_4e175,
       "hh3cevtModuleRt-ima-4e1120": hh3cevtModuleRt_ima_4e1120,
       "hh3cevtModuleRt-ima-8t1": hh3cevtModuleRt_ima_8t1,
       "hh3cevtModuleRt-ima-4t1": hh3cevtModuleRt_ima_4t1,
       "hh3cevtModuleRt-sic-1t1f": hh3cevtModuleRt_sic_1t1f,
       "hh3cevtModuleRt-sic-1e1f": hh3cevtModuleRt_sic_1e1f,
       "hh3cevtModuleRt-VG-16fxs": hh3cevtModuleRt_VG_16fxs,
       "hh3cevtModuleRt-VG-32fxs": hh3cevtModuleRt_VG_32fxs,
       "hh3cevtModuleRt-VG-8fxo": hh3cevtModuleRt_VG_8fxo,
       "hh3cevtModuleRt-VG-2fe": hh3cevtModuleRt_VG_2fe,
       "hh3cevtModuleRt-sib": hh3cevtModuleRt_sib,
       "hh3cevtModuleRt-cie32": hh3cevtModuleRt_cie32,
       "hh3cevtModuleRt-cie64": hh3cevtModuleRt_cie64,
       "hh3cevtModuleRt-cie96": hh3cevtModuleRt_cie96,
       "hh3cevtModuleRt-Fe4": hh3cevtModuleRt_Fe4,
       "hh3cevtModuleRt-fxs4fxo1": hh3cevtModuleRt_fxs4fxo1,
       "hh3cevtModuleRt-atm1shdsl4wire": hh3cevtModuleRt_atm1shdsl4wire,
       "hh3cevtModuleRt-atmIma4shdsl": hh3cevtModuleRt_atmIma4shdsl,
       "hh3cevtModuleRt-ls4": hh3cevtModuleRt_ls4,
       "hh3cevtModuleRt-ls8": hh3cevtModuleRt_ls8,
       "hh3cevtModuleRt-ls16": hh3cevtModuleRt_ls16,
       "hh3cevtModuleRt-sic-adls2plus-isdn": hh3cevtModuleRt_sic_adls2plus_isdn,
       "hh3cevtModuleRt-sic-adls2plus-pots": hh3cevtModuleRt_sic_adls2plus_pots,
       "hh3cevtModuleRt-ft3": hh3cevtModuleRt_ft3,
       "hh3cevtModuleRt-ce32": hh3cevtModuleRt_ce32,
       "hh3cevtModuleRt-bsv2": hh3cevtModuleRt_bsv2,
       "hh3cevtModuleRt-bsv4": hh3cevtModuleRt_bsv4,
       "hh3cevtModuleRt-RPU": hh3cevtModuleRt_RPU,
       "hh3cevtModuleRt-ERPU": hh3cevtModuleRt_ERPU,
       "hh3cevtModuleRt-SSL": hh3cevtModuleRt_SSL,
       "hh3cevtModuleRt-NSA": hh3cevtModuleRt_NSA,
       "hh3cevtModuleRT-SIC-1GEC": hh3cevtModuleRT_SIC_1GEC,
       "hh3cevtModuleRT-24FSW": hh3cevtModuleRT_24FSW,
       "hh3cevtModuleRT-24FSWP": hh3cevtModuleRT_24FSWP,
       "hh3cevtModuleRT-16FSW": hh3cevtModuleRT_16FSW,
       "hh3cevtModuleRT-16FSWP": hh3cevtModuleRT_16FSWP,
       "hh3cevtModuleRT-1VE1": hh3cevtModuleRT_1VE1,
       "hh3cevtModuleRT-1VT1": hh3cevtModuleRT_1VT1,
       "hh3cevtModuleRT-2VE1": hh3cevtModuleRT_2VE1,
       "hh3cevtModuleRT-2VT1": hh3cevtModuleRT_2VT1,
       "hh3cevtModuleRT-SIC-4FSW": hh3cevtModuleRT_SIC_4FSW,
       "hh3cevtModuleRT-SIC-4FSWP": hh3cevtModuleRT_SIC_4FSWP,
       "hh3cevtModuleRT-DSIC-9FSW": hh3cevtModuleRT_DSIC_9FSW,
       "hh3cevtModuleRT-DSIC-9FSWP": hh3cevtModuleRT_DSIC_9FSWP,
       "hh3cevtModuleRT-SIC-1VE1": hh3cevtModuleRT_SIC_1VE1,
       "hh3cevtModuleRT-SIC-1VT1": hh3cevtModuleRT_SIC_1VT1,
       "hh3cevtModuleRT-VCPM": hh3cevtModuleRT_VCPM,
       "hh3cevtModuleRT-VPM": hh3cevtModuleRT_VPM,
       "hh3cevtModuleRT-VPMA": hh3cevtModuleRT_VPMA,
       "hh3cevtModuleRT-VPMB": hh3cevtModuleRT_VPMB,
       "hh3cevtModuleRT-VPMC": hh3cevtModuleRT_VPMC,
       "hh3cevtModuleRt-fe18-75": hh3cevtModuleRt_fe18_75,
       "hh3cevtModuleRt-fe18-120": hh3cevtModuleRt_fe18_120,
       "hh3cevtModuleRt-ft18": hh3cevtModuleRt_ft18,
       "hh3cevtModuleRt-CF": hh3cevtModuleRt_CF,
       "hh3cevtModuleRt-bsv2-v2": hh3cevtModuleRt_bsv2_v2,
       "hh3cevtModuleRt-e1vi1-v2": hh3cevtModuleRt_e1vi1_v2,
       "hh3cevtModuleRt-e1vi2": hh3cevtModuleRt_e1vi2,
       "hh3cevtModuleRt-t1vi1-v2": hh3cevtModuleRt_t1vi1_v2,
       "hh3cevtModuleRt-t1vi2": hh3cevtModuleRt_t1vi2,
       "hh3cevtModuleRt-osm": hh3cevtModuleRt_osm,
       "hh3cevtModuleRt-sd707": hh3cevtModuleRt_sd707,
       "hh3cevtModuleRt-dm-epri": hh3cevtModuleRt_dm_epri,
       "hh3cevtModuleRt-dm-tpri": hh3cevtModuleRt_dm_tpri,
       "hh3cevtModuleRt-ERPU-H": hh3cevtModuleRt_ERPU_H,
       "hh3cevtModuleRT-SIC-1BSV": hh3cevtModuleRT_SIC_1BSV,
       "hh3cevtModuleRT-SIC-2BSV": hh3cevtModuleRT_SIC_2BSV,
       "hh3cevtModuleRt-gbe8": hh3cevtModuleRt_gbe8,
       "hh3cevtModuleRt-gbe4": hh3cevtModuleRt_gbe4,
       "hh3cevtModuleRt-cpos2-v2": hh3cevtModuleRt_cpos2_v2,
       "hh3cevtModuleRt-cpos1-v2": hh3cevtModuleRt_cpos1_v2,
       "hh3cevtModuleRt-oap": hh3cevtModuleRt_oap,
       "hh3cevtModuleRT-48FSWP": hh3cevtModuleRT_48FSWP,
       "hh3cevtModuleRT-48FSW": hh3cevtModuleRT_48FSW,
       "hh3cevtModuleRT-ASM": hh3cevtModuleRT_ASM,
       "hh3cevtModuleRT-SIC-1FEF": hh3cevtModuleRT_SIC_1FEF,
       "hh3cevtModuleRT-XMIM-24FSW": hh3cevtModuleRT_XMIM_24FSW,
       "hh3cevtModuleRT-WLAN-AG-1RADIO": hh3cevtModuleRT_WLAN_AG_1RADIO,
       "hh3cevtModuleRT-1CE3": hh3cevtModuleRT_1CE3,
       "hh3cevtModuleRT-XMIM-16FSW": hh3cevtModuleRT_XMIM_16FSW,
       "hh3cevtModuleRT-OAPS": hh3cevtModuleRT_OAPS,
       "hh3cevtModuleRT-NAM": hh3cevtModuleRT_NAM,
       "hh3cevtModuleRT-RPE-X1": hh3cevtModuleRT_RPE_X1,
       "hh3cevtModuleRT-FIP-100": hh3cevtModuleRT_FIP_100,
       "hh3cevtModuleRT-FIP-200": hh3cevtModuleRT_FIP_200,
       "hh3cevtModuleRT-SIC-8AS": hh3cevtModuleRT_SIC_8AS,
       "hh3cevtModuleRT-WAAM": hh3cevtModuleRT_WAAM,
       "hh3cevtModuleRt-msp4p-OC3c": hh3cevtModuleRt_msp4p_OC3c,
       "hh3cevtModuleRt-1pos-oc48": hh3cevtModuleRt_1pos_oc48,
       "hh3cevtModuleRt-xgbe": hh3cevtModuleRt_xgbe,
       "hh3cevtModuleRT-EADM": hh3cevtModuleRT_EADM,
       "hh3cevtModuleRT-VCM": hh3cevtModuleRT_VCM,
       "hh3cevtModuleRT-SIC-2FXS1FXO": hh3cevtModuleRT_SIC_2FXS1FXO,
       "hh3cevtModuleRT-8FXS8FXO": hh3cevtModuleRT_8FXS8FXO,
       "hh3cevtModuleRT-16FXS": hh3cevtModuleRT_16FXS,
       "hh3cevtModuleRT-OAPS-ICM": hh3cevtModuleRT_OAPS_ICM,
       "hh3cevtModuleRT-OAP-ICM": hh3cevtModuleRT_OAP_ICM,
       "hh3cevtModuleRT-8fe": hh3cevtModuleRT_8fe,
       "hh3cevtModuleRT-4gbp": hh3cevtModuleRT_4gbp,
       "hh3cevtModuleRT-MPU-G2": hh3cevtModuleRT_MPU_G2,
       "hh3cevtModuleRT-OAPS-OCE": hh3cevtModuleRT_OAPS_OCE,
       "hh3cevtModuleRT-OAP-OCE": hh3cevtModuleRT_OAP_OCE,
       "hh3cevtModuleRT-OAPS-ICE": hh3cevtModuleRT_OAPS_ICE,
       "hh3cevtModuleRT-OAP-ICE": hh3cevtModuleRT_OAP_ICE,
       "hh3cevtModuleRT-SIC-16AS": hh3cevtModuleRT_SIC_16AS,
       "hh3cevtModuleRT-SPE-FWM": hh3cevtModuleRT_SPE_FWM,
       "hh3cevtModuleRT-cls2p": hh3cevtModuleRT_cls2p,
       "hh3cevtModuleRT-cls1p": hh3cevtModuleRT_cls1p,
       "hh3cevtModuleRT-SIC-2E1-F": hh3cevtModuleRT_SIC_2E1_F,
       "hh3cevtModuleRT-SIC-1E1-F-V2": hh3cevtModuleRT_SIC_1E1_F_V2,
       "hh3cevtModuleRT-MCU": hh3cevtModuleRT_MCU,
       "hh3cevtModuleRT-ACU": hh3cevtModuleRT_ACU,
       "hh3cevtModuleRT-1ATM-OC3": hh3cevtModuleRT_1ATM_OC3,
       "hh3cevtModuleRT-RSE-X1": hh3cevtModuleRT_RSE_X1,
       "hh3cevtModuleRT-FIP-210": hh3cevtModuleRT_FIP_210,
       "hh3cevtModuleRT-1expa": hh3cevtModuleRT_1expa,
       "hh3cevtModuleRT-WLAN-SIC-N-1RADIO": hh3cevtModuleRT_WLAN_SIC_N_1RADIO,
       "hh3cevtModuleRT-WLAN-SIC-BG-1RADIO": hh3cevtModuleRT_WLAN_SIC_BG_1RADIO,
       "hh3cevtModuleRT-al2p": hh3cevtModuleRT_al2p,
       "hh3cevtModuleRT-msp2p-OC3c": hh3cevtModuleRT_msp2p_OC3c,
       "hh3cevtModuleRT-8gbp": hh3cevtModuleRT_8gbp,
       "hh3cevtModuleRT-SIC-EPON": hh3cevtModuleRT_SIC_EPON,
       "hh3cevtModuleRT-SIC-3G-GSM-H3": hh3cevtModuleRT_SIC_3G_GSM_H3,
       "hh3cevtModuleRT-msp2p-OC12c": hh3cevtModuleRT_msp2p_OC12c,
       "hh3cevtModuleRt-msp4p-OC12c": hh3cevtModuleRt_msp4p_OC12c,
       "hh3cevtModuleRt-al1p": hh3cevtModuleRt_al1p,
       "hh3cevtModuleRt-OAP-100": hh3cevtModuleRt_OAP_100,
       "hh3cevtModuleRt-FIP-110": hh3cevtModuleRt_FIP_110,
       "hh3cevtModuleRt-OSM-SSM": hh3cevtModuleRt_OSM_SSM,
       "hh3cevtModuleRt-OAP-SSM": hh3cevtModuleRt_OAP_SSM,
       "hh3cevtModuleRt-rs2p": hh3cevtModuleRt_rs2p,
       "hh3cevtModuleRt-SAP-48GBE": hh3cevtModuleRt_SAP_48GBE,
       "hh3cevtModuleRt-SAP-48GBP": hh3cevtModuleRt_SAP_48GBP,
       "hh3cevtModuleRt-SAP-24GBP": hh3cevtModuleRt_SAP_24GBP,
       "hh3cevtModuleRt-SPE-SSL": hh3cevtModuleRt_SPE_SSL,
       "hh3cevtModuleRt-SIC-AUDIO": hh3cevtModuleRt_SIC_AUDIO,
       "hh3cevtModuleRt-FIC-1E1POS-H3": hh3cevtModuleRt_FIC_1E1POS_H3,
       "hh3cevtModuleRt-DSIC-4FXS1FXO": hh3cevtModuleRt_DSIC_4FXS1FXO,
       "hh3cevtModuleRt-FIC-CPOS": hh3cevtModuleRt_FIC_CPOS,
       "hh3cevtModuleRt-DSIC-1SHDSL-8W": hh3cevtModuleRt_DSIC_1SHDSL_8W,
       "hh3cevtModuleRt-SIC-3G-TD": hh3cevtModuleRt_SIC_3G_TD,
       "hh3cevtModuleRt-SIC-3G-CDMA": hh3cevtModuleRt_SIC_3G_CDMA,
       "hh3cevtModuleRt-SIC-3G-HSPA": hh3cevtModuleRt_SIC_3G_HSPA,
       "hh3cevtModuleRt-FIC-OAP-V2": hh3cevtModuleRt_FIC_OAP_V2,
       "hh3cevtModuleRt-MIM-OAP-V2": hh3cevtModuleRt_MIM_OAP_V2,
       "hh3cevtModuleRt-MIM-OAPS-V2": hh3cevtModuleRt_MIM_OAPS_V2,
       "hh3cevtModuleRt-IPU": hh3cevtModuleRt_IPU,
       "hh3cevtModuleRt-MIM2GEBE-PCIE": hh3cevtModuleRt_MIM2GEBE_PCIE,
       "hh3cevtModuleRt-HIM12GE-PCIE": hh3cevtModuleRt_HIM12GE_PCIE,
       "hh3cevtModuleRt-HIM2XGE-PCIE": hh3cevtModuleRt_HIM2XGE_PCIE,
       "hh3cevtModuleRt-IPU-T1000-M": hh3cevtModuleRt_IPU_T1000_M,
       "hh3cevtModuleRt-IPU-GX4C": hh3cevtModuleRt_IPU_GX4C,
       "hh3cevtModuleRt-IPU-GT4C": hh3cevtModuleRt_IPU_GT4C,
       "hh3cevtModuleRt-RPU-IAG2000-A": hh3cevtModuleRt_RPU_IAG2000_A,
       "hh3cevtModuleRt-RPU-AFD1000-A": hh3cevtModuleRt_RPU_AFD1000_A,
       "hh3cevtModuleRt-RPU-F5000-A": hh3cevtModuleRt_RPU_F5000_A,
       "hh3cevtModuleRt-ACG-8800S3-MPU": hh3cevtModuleRt_ACG_8800S3_MPU,
       "hh3cevtModuleRt-T5000S3-MPU": hh3cevtModuleRt_T5000S3_MPU,
       "hh3cevtModuleRt-NS21S2MSPB0": hh3cevtModuleRt_NS21S2MSPB0,
       "hh3cevtModuleRt-NS11S2MSPB0": hh3cevtModuleRt_NS11S2MSPB0,
       "hh3cevtModuleRt-NSQ1WLAN": hh3cevtModuleRt_NSQ1WLAN,
       "hh3cevtModuleRt-NSQ1GP4U0": hh3cevtModuleRt_NSQ1GP4U0,
       "hh3cevtModuleRt-NSQ1GP8C40": hh3cevtModuleRt_NSQ1GP8C40,
       "hh3cevtModuleRt-NSQ1XS2U0": hh3cevtModuleRt_NSQ1XS2U0,
       "hh3cevtModuleRt-VG-8fxs": hh3cevtModuleRt_VG_8fxs,
       "hh3cevtModuleRt-VG-24fxs": hh3cevtModuleRt_VG_24fxs,
       "hh3cevtModuleRt-VG-24fxs24fxo": hh3cevtModuleRt_VG_24fxs24fxo,
       "hh3cevtModuleRt-VG-MPU": hh3cevtModuleRt_VG_MPU,
       "hh3cevtModuleRt-MIM-VCX-CONNECT-P-3C": hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C,
       "hh3cevtModuleRt-MIM-VCX-CONNECT-S-3C": hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C,
       "hh3cevtModuleRt-MIM-VCX-3C": hh3cevtModuleRt_MIM_VCX_3C,
       "hpevtModuleRt-SIC-EPRI": hpevtModuleRt_SIC_EPRI,
       "hpevtModuleRt-MIM-1E1-V2": hpevtModuleRt_MIM_1E1_V2,
       "hpevtModuleRt-MIM-1E1-F-V2": hpevtModuleRt_MIM_1E1_F_V2,
       "hpevtModuleRt-MIM-2E1-F-V2": hpevtModuleRt_MIM_2E1_F_V2,
       "hpevtModuleRt-MIM-4E1-F-V2": hpevtModuleRt_MIM_4E1_F_V2,
       "hpevtModuleRt-MIM-8E1-75": hpevtModuleRt_MIM_8E1_75,
       "hpevtModuleRt-MIM-8E1-75-F": hpevtModuleRt_MIM_8E1_75_F,
       "hpevtModuleRt-MIM-8T1": hpevtModuleRt_MIM_8T1,
       "hpevtModuleRt-MIM-8T1-F": hpevtModuleRt_MIM_8T1_F,
       "hpevtModuleRt-MIM-IMA-8E1-75": hpevtModuleRt_MIM_IMA_8E1_75,
       "hpevtModuleRt-FIC-2E1-V3": hpevtModuleRt_FIC_2E1_V3,
       "hpevtModuleRt-FIC-IMA-8T1-V2": hpevtModuleRt_FIC_IMA_8T1_V2,
       "hh3cevtModuleSwitchType": hh3cevtModuleSwitchType,
       "hh3cevtModuleSw-10OR100M": hh3cevtModuleSw_10OR100M,
       "hh3cevtModuleSw-1000BASE-LX-SM": hh3cevtModuleSw_1000BASE_LX_SM,
       "hh3cevtModuleSw-1000BASE-SX-MM": hh3cevtModuleSw_1000BASE_SX_MM,
       "hh3cevtModuleSw-1000BASE-TX": hh3cevtModuleSw_1000BASE_TX,
       "hh3cevtModuleSw-100M-SINGLEMODE-FX": hh3cevtModuleSw_100M_SINGLEMODE_FX,
       "hh3cevtModuleSw-100M-MULTIMODE-FX": hh3cevtModuleSw_100M_MULTIMODE_FX,
       "hh3cevtModuleSw-100M-100BASE-TX": hh3cevtModuleSw_100M_100BASE_TX,
       "hh3cevtModuleSw-100M-HUB": hh3cevtModuleSw_100M_HUB,
       "hh3cevtModuleSw-VDSL": hh3cevtModuleSw_VDSL,
       "hh3cevtModuleSw-STACK": hh3cevtModuleSw_STACK,
       "hh3cevtModuleSw-1000BASE-ZENITH-FX": hh3cevtModuleSw_1000BASE_ZENITH_FX,
       "hh3cevtModuleSw-1000BASE-LONG-FX": hh3cevtModuleSw_1000BASE_LONG_FX,
       "hh3cevtModuleSw-ADSL": hh3cevtModuleSw_ADSL,
       "hh3cevtModuleSw-4T10OR100-4FX100SM": hh3cevtModuleSw_4T10OR100_4FX100SM,
       "hh3cevtModuleSw-4T10OR100-4FX100MM": hh3cevtModuleSw_4T10OR100_4FX100MM,
       "hh3cevtModuleSw-VSPL": hh3cevtModuleSw_VSPL,
       "hh3cevtModuleSw-ASPL": hh3cevtModuleSw_ASPL,
       "hh3cevtModuleSw-1000M-SFP": hh3cevtModuleSw_1000M_SFP,
       "hh3cevtModuleSw-LS82O2CM": hh3cevtModuleSw_LS82O2CM,
       "hh3cevtModuleSw-LS82P2CM": hh3cevtModuleSw_LS82P2CM,
       "hh3cevtModuleSw-LS82O4GM": hh3cevtModuleSw_LS82O4GM,
       "hh3cevtModuleSw-LS82GB4C": hh3cevtModuleSw_LS82GB4C,
       "hh3cevtModuleSw-LS82GT4C": hh3cevtModuleSw_LS82GT4C,
       "hh3cevtModuleSw-LS82ST4C": hh3cevtModuleSw_LS82ST4C,
       "hh3cevtModuleSw-BOARD-LS82DSPU": hh3cevtModuleSw_BOARD_LS82DSPU,
       "hh3cevtModuleSw-BOARD-LS81GP8U": hh3cevtModuleSw_BOARD_LS81GP8U,
       "hh3cevtModuleSw-BOARD-LS82GT20": hh3cevtModuleSw_BOARD_LS82GT20,
       "hh3cevtModuleSw-BOARD-LS82FE48": hh3cevtModuleSw_BOARD_LS82FE48,
       "hh3cevtModuleSw-LS82T24B": hh3cevtModuleSw_LS82T24B,
       "hh3cevtModuleSw-LSB1SRPA": hh3cevtModuleSw_LSB1SRPA,
       "hh3cevtModuleSw-LSB1FT48A": hh3cevtModuleSw_LSB1FT48A,
       "hh3cevtModuleSw-LSB1FT48B": hh3cevtModuleSw_LSB1FT48B,
       "hh3cevtModuleSw-LSB1F48GA": hh3cevtModuleSw_LSB1F48GA,
       "hh3cevtModuleSw-LSB1F48GB": hh3cevtModuleSw_LSB1F48GB,
       "hh3cevtModuleSw-LSB1FP20A": hh3cevtModuleSw_LSB1FP20A,
       "hh3cevtModuleSw-LSB1FP20B": hh3cevtModuleSw_LSB1FP20B,
       "hh3cevtModuleSw-FT48A": hh3cevtModuleSw_FT48A,
       "hh3cevtModuleSw-GP4U": hh3cevtModuleSw_GP4U,
       "hh3cevtModuleSw-GP2U": hh3cevtModuleSw_GP2U,
       "hh3cevtModuleSw-TGX1A": hh3cevtModuleSw_TGX1A,
       "hh3cevtModuleSw-1000BASE-LX-SM-IR-SC": hh3cevtModuleSw_1000BASE_LX_SM_IR_SC,
       "hh3cevtModuleSw-1000BASE-SX-MM-SR-SC": hh3cevtModuleSw_1000BASE_SX_MM_SR_SC,
       "hh3cevtModuleSw-1000BASE-T-RJ45": hh3cevtModuleSw_1000BASE_T_RJ45,
       "hh3cevtModuleSw-100BASE-FX-SM-IR-SC": hh3cevtModuleSw_100BASE_FX_SM_IR_SC,
       "hh3cevtModuleSw-100BASE-FX-MM-SR-SC": hh3cevtModuleSw_100BASE_FX_MM_SR_SC,
       "hh3cevtModuleSw-GIGA-STACK-1M-PC": hh3cevtModuleSw_GIGA_STACK_1M_PC,
       "hh3cevtModuleSw-1000BASE-LX-SM-VLR-LC": hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC,
       "hh3cevtModuleSw-1000BASE-LX-SM-LR-LC": hh3cevtModuleSw_1000BASE_LX_SM_LR_LC,
       "hh3cevtModuleSw-100BASE-FX-SM-LR-SC": hh3cevtModuleSw_100BASE_FX_SM_LR_SC,
       "hh3cevtModuleSw-1000BASE-X-GBIC": hh3cevtModuleSw_1000BASE_X_GBIC,
       "hh3cevtModuleSw-100M-SINGLEMODE-FX-LC": hh3cevtModuleSw_100M_SINGLEMODE_FX_LC,
       "hh3cevtModuleSw-100M-MULTIMODE-FX-LC": hh3cevtModuleSw_100M_MULTIMODE_FX_LC,
       "hh3cevtModuleSw-1000BASE-4SFP": hh3cevtModuleSw_1000BASE_4SFP,
       "hh3cevtModuleSw-1000BASE-4GBIC": hh3cevtModuleSw_1000BASE_4GBIC,
       "hh3cevtModuleSw-1000BASE-FIXED-4SFP": hh3cevtModuleSw_1000BASE_FIXED_4SFP,
       "hh3cevtModuleSw-1000BASE-FIXED-4GBIC": hh3cevtModuleSw_1000BASE_FIXED_4GBIC,
       "hh3cevtModuleSw-LSB1GP12A": hh3cevtModuleSw_LSB1GP12A,
       "hh3cevtModuleSw-LSB1GP12B": hh3cevtModuleSw_LSB1GP12B,
       "hh3cevtModuleSw-LSB1TGX1A": hh3cevtModuleSw_LSB1TGX1A,
       "hh3cevtModuleSw-LSB1TGX1B": hh3cevtModuleSw_LSB1TGX1B,
       "hh3cevtModuleSw-LSB1P4G8A": hh3cevtModuleSw_LSB1P4G8A,
       "hh3cevtModuleSw-LSB1P4G8B": hh3cevtModuleSw_LSB1P4G8B,
       "hh3cevtModuleSw-LSB1A4G8A": hh3cevtModuleSw_LSB1A4G8A,
       "hh3cevtModuleSw-LSB1A4G8B": hh3cevtModuleSw_LSB1A4G8B,
       "hh3cevtModuleSw-FT48C": hh3cevtModuleSw_FT48C,
       "hh3cevtModuleSw-FP20": hh3cevtModuleSw_FP20,
       "hh3cevtModuleSw-BOARD-LS81FT48": hh3cevtModuleSw_BOARD_LS81FT48,
       "hh3cevtModuleSw-BOARD-LS81GB8U": hh3cevtModuleSw_BOARD_LS81GB8U,
       "hh3cevtModuleSw-BOARD-LS81GT8U": hh3cevtModuleSw_BOARD_LS81GT8U,
       "hh3cevtModuleSw-BOARD-LS81FS24": hh3cevtModuleSw_BOARD_LS81FS24,
       "hh3cevtModuleSw-BOARD-LS81FM24": hh3cevtModuleSw_BOARD_LS81FM24,
       "hh3cevtModuleSw-BOARD-LS82GP20": hh3cevtModuleSw_BOARD_LS82GP20,
       "hh3cevtModuleSw-LSB1SRPB": hh3cevtModuleSw_LSB1SRPB,
       "hh3cevtModuleSw-LSB1F32GA": hh3cevtModuleSw_LSB1F32GA,
       "hh3cevtModuleSw-LSB1F32GB": hh3cevtModuleSw_LSB1F32GB,
       "hh3cevtModuleSw-LSB2FT48A": hh3cevtModuleSw_LSB2FT48A,
       "hh3cevtModuleSw-LSB2FT48B": hh3cevtModuleSw_LSB2FT48B,
       "hh3cevtModuleSw-LSB1GT12A": hh3cevtModuleSw_LSB1GT12A,
       "hh3cevtModuleSw-LSB1GT12B": hh3cevtModuleSw_LSB1GT12B,
       "hh3cevtModuleSw-PC4U": hh3cevtModuleSw_PC4U,
       "hh3cevtModuleSw-FT32A": hh3cevtModuleSw_FT32A,
       "hh3cevtModuleSw-GT4U": hh3cevtModuleSw_GT4U,
       "hh3cevtModuleSw-BOARD-LS83FP20A": hh3cevtModuleSw_BOARD_LS83FP20A,
       "hh3cevtModuleSw-BOARD-LS82HGMU": hh3cevtModuleSw_BOARD_LS82HGMU,
       "hh3cevtModuleSw-LSB1GP8TB": hh3cevtModuleSw_LSB1GP8TB,
       "hh3cevtModuleSw-LSB1GP8TC": hh3cevtModuleSw_LSB1GP8TC,
       "hh3cevtModuleSw-LSB1GT8PB": hh3cevtModuleSw_LSB1GT8PB,
       "hh3cevtModuleSw-LSB1GT8PC": hh3cevtModuleSw_LSB1GT8PC,
       "hh3cevtModuleSw-LSB1FT48C": hh3cevtModuleSw_LSB1FT48C,
       "hh3cevtModuleSw-LSB1FP20C": hh3cevtModuleSw_LSB1FP20C,
       "hh3cevtModuleSw-LSB1F32GC": hh3cevtModuleSw_LSB1F32GC,
       "hh3cevtModuleSw-LSB1GT12C": hh3cevtModuleSw_LSB1GT12C,
       "hh3cevtModuleSw-LSB1GP12C": hh3cevtModuleSw_LSB1GP12C,
       "hh3cevtModuleSw-LSB1P4G8C": hh3cevtModuleSw_LSB1P4G8C,
       "hh3cevtModuleSw-LSB1TGX1C": hh3cevtModuleSw_LSB1TGX1C,
       "hh3cevtModuleSw-LSB1GT24B": hh3cevtModuleSw_LSB1GT24B,
       "hh3cevtModuleSw-LSB1GT24C": hh3cevtModuleSw_LSB1GT24C,
       "hh3cevtModuleSw-LSB1GP24B": hh3cevtModuleSw_LSB1GP24B,
       "hh3cevtModuleSw-LSB1GP24C": hh3cevtModuleSw_LSB1GP24C,
       "hh3cevtModuleSw-LSB1XP2B": hh3cevtModuleSw_LSB1XP2B,
       "hh3cevtModuleSw-LSB1XP2C": hh3cevtModuleSw_LSB1XP2C,
       "hh3cevtModuleSw-LSB1GV48B": hh3cevtModuleSw_LSB1GV48B,
       "hh3cevtModuleSw-LSB1GV48C": hh3cevtModuleSw_LSB1GV48C,
       "hh3cevtModuleSw-LSB1SRPC": hh3cevtModuleSw_LSB1SRPC,
       "hh3cevtModuleSw-LSB1SRP1N0": hh3cevtModuleSw_LSB1SRP1N0,
       "hh3cevtModuleSw-LSB1SRP1N1": hh3cevtModuleSw_LSB1SRP1N1,
       "hh3cevtModuleSw-LSB1SRP1N2": hh3cevtModuleSw_LSB1SRP1N2,
       "hh3cevtModuleSw-GT24": hh3cevtModuleSw_GT24,
       "hh3cevtModuleSw-GP24": hh3cevtModuleSw_GP24,
       "hh3cevtModuleSw-XP2": hh3cevtModuleSw_XP2,
       "hh3cevtModuleSw-GV48": hh3cevtModuleSw_GV48,
       "hh3cevtModuleSw-LSG1GP8U": hh3cevtModuleSw_LSG1GP8U,
       "hh3cevtModuleSw-LSG1GT8U": hh3cevtModuleSw_LSG1GT8U,
       "hh3cevtModuleSw-LSG1TG1U": hh3cevtModuleSw_LSG1TG1U,
       "hh3cevtModuleSw-LSG1TD1U": hh3cevtModuleSw_LSG1TD1U,
       "hh3cevtModuleSw-LSB2FT48C": hh3cevtModuleSw_LSB2FT48C,
       "hh3cevtModuleSw-LSB1GT48B": hh3cevtModuleSw_LSB1GT48B,
       "hh3cevtModuleSw-LSB1GT48C": hh3cevtModuleSw_LSB1GT48C,
       "hh3cevtModuleSw-LS81GT48": hh3cevtModuleSw_LS81GT48,
       "hh3cevtModuleSw-LS81SRPG0": hh3cevtModuleSw_LS81SRPG0,
       "hh3cevtModuleSw-LS81SRPG1": hh3cevtModuleSw_LS81SRPG1,
       "hh3cevtModuleSw-LS81SRPG2": hh3cevtModuleSw_LS81SRPG2,
       "hh3cevtModuleSw-LS81SRPG3": hh3cevtModuleSw_LS81SRPG3,
       "hh3cevtModuleSw-SR01SRPUB": hh3cevtModuleSw_SR01SRPUB,
       "hh3cevtModuleSw-SR01SRPUA": hh3cevtModuleSw_SR01SRPUA,
       "hh3cevtModuleSw-SR01GP12L": hh3cevtModuleSw_SR01GP12L,
       "hh3cevtModuleSw-SR01GP12W": hh3cevtModuleSw_SR01GP12W,
       "hh3cevtModuleSw-SR01FT48L": hh3cevtModuleSw_SR01FT48L,
       "hh3cevtModuleSw-SR01FT48W": hh3cevtModuleSw_SR01FT48W,
       "hh3cevtModuleSw-SR01XK1W": hh3cevtModuleSw_SR01XK1W,
       "hh3cevtModuleSw-SR01FP20W": hh3cevtModuleSw_SR01FP20W,
       "hh3cevtModuleSw-SR01GT12W": hh3cevtModuleSw_SR01GT12W,
       "hh3cevtModuleSw-SR01F32GL": hh3cevtModuleSw_SR01F32GL,
       "hh3cevtModuleSw-SR01F32GW": hh3cevtModuleSw_SR01F32GW,
       "hh3cevtModuleSw-SR01GT8PL": hh3cevtModuleSw_SR01GT8PL,
       "hh3cevtModuleSw-SR01GT8PW": hh3cevtModuleSw_SR01GT8PW,
       "hh3cevtModuleSw-SR01P4G8W": hh3cevtModuleSw_SR01P4G8W,
       "hh3cevtModuleSw-LSA1FP8U": hh3cevtModuleSw_LSA1FP8U,
       "hh3cevtModuleSw-LSB1SP4B": hh3cevtModuleSw_LSB1SP4B,
       "hh3cevtModuleSw-LSB1SP4C": hh3cevtModuleSw_LSB1SP4C,
       "hh3cevtModuleSw-LSB1UP1B": hh3cevtModuleSw_LSB1UP1B,
       "hh3cevtModuleSw-LSB1UP1C": hh3cevtModuleSw_LSB1UP1C,
       "hh3cevtModuleSw-LSB1XP4B": hh3cevtModuleSw_LSB1XP4B,
       "hh3cevtModuleSw-LSB1XP4C": hh3cevtModuleSw_LSB1XP4C,
       "hh3cevtModuleSw-SP4": hh3cevtModuleSw_SP4,
       "hh3cevtModuleSw-UP1": hh3cevtModuleSw_UP1,
       "hh3cevtModuleSw-XP4": hh3cevtModuleSw_XP4,
       "hh3cevtModuleSw-LS81VSNP": hh3cevtModuleSw_LS81VSNP,
       "hh3cevtModuleSw-LS81T12P": hh3cevtModuleSw_LS81T12P,
       "hh3cevtModuleSw-LS81P12T": hh3cevtModuleSw_LS81P12T,
       "hh3cevtModuleSw-LS81GP8UB": hh3cevtModuleSw_LS81GP8UB,
       "hh3cevtModuleSw-LS81FT48E": hh3cevtModuleSw_LS81FT48E,
       "hh3cevtModuleSw-LS81GP4UB": hh3cevtModuleSw_LS81GP4UB,
       "hh3cevtModuleSw-LS81GT8UE": hh3cevtModuleSw_LS81GT8UE,
       "hh3cevtModuleSw-LS81GT48A": hh3cevtModuleSw_LS81GT48A,
       "hh3cevtModuleSw-LS81FP48": hh3cevtModuleSw_LS81FP48,
       "hh3cevtModuleSw-LSB1XK1B": hh3cevtModuleSw_LSB1XK1B,
       "hh3cevtModuleSw-LSB1XK1C": hh3cevtModuleSw_LSB1XK1C,
       "hh3cevtModuleSw-SR01SRPUC": hh3cevtModuleSw_SR01SRPUC,
       "hh3cevtModuleSw-SR01SRPUD": hh3cevtModuleSw_SR01SRPUD,
       "hh3cevtModuleSw-SR01SRPUE": hh3cevtModuleSw_SR01SRPUE,
       "hh3cevtModuleSw-LSB1SRP1N3": hh3cevtModuleSw_LSB1SRP1N3,
       "hh3cevtModuleSw-LSB1VP2B": hh3cevtModuleSw_LSB1VP2B,
       "hh3cevtModuleSw-LSB1NATB": hh3cevtModuleSw_LSB1NATB,
       "hh3cevtModuleSw-LSB1VPNB": hh3cevtModuleSw_LSB1VPNB,
       "hh3cevtModuleSw-LSGP8P": hh3cevtModuleSw_LSGP8P,
       "hh3cevtModuleSw-LSXK1P": hh3cevtModuleSw_LSXK1P,
       "hh3cevtModuleSw-LSXP2P": hh3cevtModuleSw_LSXP2P,
       "hh3cevtModuleSw-LS81FT48F": hh3cevtModuleSw_LS81FT48F,
       "hh3cevtModuleSw-LS81PT8G": hh3cevtModuleSw_LS81PT8G,
       "hh3cevtModuleSw-LS81PT4G": hh3cevtModuleSw_LS81PT4G,
       "hh3cevtModuleSw-LSSTK24G": hh3cevtModuleSw_LSSTK24G,
       "hh3cevtModuleSw-LS82GT20A": hh3cevtModuleSw_LS82GT20A,
       "hh3cevtModuleSw-LS82GP20A": hh3cevtModuleSw_LS82GP20A,
       "hh3cevtModuleSw-LS81TGX1C": hh3cevtModuleSw_LS81TGX1C,
       "hh3cevtModuleSw-VP2": hh3cevtModuleSw_VP2,
       "hh3cevtModuleSw-LSA1FB8U": hh3cevtModuleSw_LSA1FB8U,
       "hh3cevtModuleSw-LS81T12PE": hh3cevtModuleSw_LS81T12PE,
       "hh3cevtModuleSw-LS81P12TE": hh3cevtModuleSw_LS81P12TE,
       "hh3cevtModuleSw-LSB1SRP2N0": hh3cevtModuleSw_LSB1SRP2N0,
       "hh3cevtModuleSw-LSB1SRP2N3": hh3cevtModuleSw_LSB1SRP2N3,
       "hh3cevtModuleSw-LSB1GV48DB": hh3cevtModuleSw_LSB1GV48DB,
       "hh3cevtModuleSw-LSB1FW8B": hh3cevtModuleSw_LSB1FW8B,
       "hh3cevtModuleSw-LSB1IPSEC8B": hh3cevtModuleSw_LSB1IPSEC8B,
       "hh3cevtModuleSw-LSB1IDSB": hh3cevtModuleSw_LSB1IDSB,
       "hh3cevtModuleSw-LSB1IPSB": hh3cevtModuleSw_LSB1IPSB,
       "hh3cevtModuleSw-LSB2FT48CA": hh3cevtModuleSw_LSB2FT48CA,
       "hh3cevtModuleSw-LSB1FP20CA": hh3cevtModuleSw_LSB1FP20CA,
       "hh3cevtModuleSw-LSB1F32GCA": hh3cevtModuleSw_LSB1F32GCA,
       "hh3cevtModuleSw-LSB1P4G8CA": hh3cevtModuleSw_LSB1P4G8CA,
       "hh3cevtModuleSw-LSB1GT12CA": hh3cevtModuleSw_LSB1GT12CA,
       "hh3cevtModuleSw-LSB1GT24CA": hh3cevtModuleSw_LSB1GT24CA,
       "hh3cevtModuleSw-LSB1GP12CA": hh3cevtModuleSw_LSB1GP12CA,
       "hh3cevtModuleSw-LSB1GP24CA": hh3cevtModuleSw_LSB1GP24CA,
       "hh3cevtModuleSw-LSB1GT8PCA": hh3cevtModuleSw_LSB1GT8PCA,
       "hh3cevtModuleSw-LSB1XP2CA": hh3cevtModuleSw_LSB1XP2CA,
       "hh3cevtModuleSw-LSB1XK1CA": hh3cevtModuleSw_LSB1XK1CA,
       "hh3cevtModuleSw-LSB1XP4CA": hh3cevtModuleSw_LSB1XP4CA,
       "hh3cevtModuleSw-LSB1UP1CA": hh3cevtModuleSw_LSB1UP1CA,
       "hh3cevtModuleSw-LSB1SP4CA": hh3cevtModuleSw_LSB1SP4CA,
       "hh3cevtModuleSw-LSB1VP2CA": hh3cevtModuleSw_LSB1VP2CA,
       "hh3cevtModuleSw-SR01FT48WA": hh3cevtModuleSw_SR01FT48WA,
       "hh3cevtModuleSw-SR01FP20WA": hh3cevtModuleSw_SR01FP20WA,
       "hh3cevtModuleSw-SR01F32GWA": hh3cevtModuleSw_SR01F32GWA,
       "hh3cevtModuleSw-SR01P4G8WA": hh3cevtModuleSw_SR01P4G8WA,
       "hh3cevtModuleSw-SR01GT12WA": hh3cevtModuleSw_SR01GT12WA,
       "hh3cevtModuleSw-SR01GT24WA": hh3cevtModuleSw_SR01GT24WA,
       "hh3cevtModuleSw-SR01GP12WA": hh3cevtModuleSw_SR01GP12WA,
       "hh3cevtModuleSw-SR01GP24WA": hh3cevtModuleSw_SR01GP24WA,
       "hh3cevtModuleSw-SR01GT8PWA": hh3cevtModuleSw_SR01GT8PWA,
       "hh3cevtModuleSw-SR01XP2WA": hh3cevtModuleSw_SR01XP2WA,
       "hh3cevtModuleSw-SR01XK1WA": hh3cevtModuleSw_SR01XK1WA,
       "hh3cevtModuleSw-SR01UP1WA": hh3cevtModuleSw_SR01UP1WA,
       "hh3cevtModuleSw-SR01SP4WA": hh3cevtModuleSw_SR01SP4WA,
       "hh3cevtModuleSw-GP8U": hh3cevtModuleSw_GP8U,
       "hh3cevtModuleSw-LSEXP1P": hh3cevtModuleSw_LSEXP1P,
       "hh3cevtModuleSw-LSEXK1P": hh3cevtModuleSw_LSEXK1P,
       "hh3cevtModuleSw-LSEXS1P": hh3cevtModuleSw_LSEXS1P,
       "hh3cevtModuleSw-LS81GP48": hh3cevtModuleSw_LS81GP48,
       "hh3cevtModuleSw-LS81GT48B": hh3cevtModuleSw_LS81GT48B,
       "hh3cevtModuleSw-LS81T16P": hh3cevtModuleSw_LS81T16P,
       "hh3cevtModuleSw-LS81T32P": hh3cevtModuleSw_LS81T32P,
       "hh3cevtModuleSw-LS81TGX2": hh3cevtModuleSw_LS81TGX2,
       "hh3cevtModuleSw-LS81TGX4": hh3cevtModuleSw_LS81TGX4,
       "hh3cevtModuleSw-LSB1GV48DA": hh3cevtModuleSw_LSB1GV48DA,
       "hh3cevtModuleSw-SR01GV48VB": hh3cevtModuleSw_SR01GV48VB,
       "hh3cevtModuleSw-LSB1GT24DB": hh3cevtModuleSw_LSB1GT24DB,
       "hh3cevtModuleSw-LSB1GP24DB": hh3cevtModuleSw_LSB1GP24DB,
       "hh3cevtModuleSw-LSB1GP24DC": hh3cevtModuleSw_LSB1GP24DC,
       "hh3cevtModuleSw-LSB1FW8DB": hh3cevtModuleSw_LSB1FW8DB,
       "hh3cevtModuleSw-LSB1IPSEC8DB": hh3cevtModuleSw_LSB1IPSEC8DB,
       "hh3cevtModuleSw-SR01GT24VB": hh3cevtModuleSw_SR01GT24VB,
       "hh3cevtModuleSw-SR01GP24VC": hh3cevtModuleSw_SR01GP24VC,
       "hh3cevtModuleSw-SR01VP2WA": hh3cevtModuleSw_SR01VP2WA,
       "hh3cevtModuleSw-SR01FW8VB": hh3cevtModuleSw_SR01FW8VB,
       "hh3cevtModuleSw-SR01IPSEC8VB": hh3cevtModuleSw_SR01IPSEC8VB,
       "hh3cevtModuleSw-SR01NATL": hh3cevtModuleSw_SR01NATL,
       "hh3cevtModuleSw-SR01VPNL": hh3cevtModuleSw_SR01VPNL,
       "hh3cevtModuleSw-LSB1GP24CB": hh3cevtModuleSw_LSB1GP24CB,
       "hh3cevtModuleSw-LSB1GP48DB": hh3cevtModuleSw_LSB1GP48DB,
       "hh3cevtModuleSw-LSB1XP2CB": hh3cevtModuleSw_LSB1XP2CB,
       "hh3cevtModuleSw-XP4L": hh3cevtModuleSw_XP4L,
       "hh3cevtModuleSw-LSB1XP4LDB": hh3cevtModuleSw_LSB1XP4LDB,
       "hh3cevtModuleSw-LSB1XP4LDC": hh3cevtModuleSw_LSB1XP4LDC,
       "hh3cevtModuleSw-AHP4": hh3cevtModuleSw_AHP4,
       "hh3cevtModuleSw-LSB1AHP4GCA": hh3cevtModuleSw_LSB1AHP4GCA,
       "hh3cevtModuleSw-CLP4": hh3cevtModuleSw_CLP4,
       "hh3cevtModuleSw-LSB1CLP4GCA": hh3cevtModuleSw_LSB1CLP4GCA,
       "hh3cevtModuleSw-ET32": hh3cevtModuleSw_ET32,
       "hh3cevtModuleSw-LSB1ET32GCA": hh3cevtModuleSw_LSB1ET32GCA,
       "hh3cevtModuleSw-LSB1IDSDB": hh3cevtModuleSw_LSB1IDSDB,
       "hh3cevtModuleSw-LSB1SRP2N1": hh3cevtModuleSw_LSB1SRP2N1,
       "hh3cevtModuleSw-BOARD-LS82SRPB": hh3cevtModuleSw_BOARD_LS82SRPB,
       "hh3cevtModuleSw-BORAD-LS83SRPC": hh3cevtModuleSw_BORAD_LS83SRPC,
       "hh3cevtModuleSw-Main": hh3cevtModuleSw_Main,
       "hh3cevtModuleSw-LSB1SRP2N2": hh3cevtModuleSw_LSB1SRP2N2,
       "hh3cevtModuleSw-LSB1NAMB": hh3cevtModuleSw_LSB1NAMB,
       "hh3cevtModuleSw-RSP2": hh3cevtModuleSw_RSP2,
       "hh3cevtModuleSw-LSB1RSP2CA": hh3cevtModuleSw_LSB1RSP2CA,
       "hh3cevtModuleSw-SR01XP4LVC": hh3cevtModuleSw_SR01XP4LVC,
       "hh3cevtModuleSw-SR01AHP4GWA": hh3cevtModuleSw_SR01AHP4GWA,
       "hh3cevtModuleSw-SR01CLP4GWA": hh3cevtModuleSw_SR01CLP4GWA,
       "hh3cevtModuleSw-SR01ET32GWA": hh3cevtModuleSw_SR01ET32GWA,
       "hh3cevtModuleSw-SR01IDSVB": hh3cevtModuleSw_SR01IDSVB,
       "hh3cevtModuleSw-SR01SRPUF": hh3cevtModuleSw_SR01SRPUF,
       "hh3cevtModuleSw-SR01NAML": hh3cevtModuleSw_SR01NAML,
       "hh3cevtModuleSw-SR01RSP2WA": hh3cevtModuleSw_SR01RSP2WA,
       "hh3cevtModuleSw-LSPM1XP1P": hh3cevtModuleSw_LSPM1XP1P,
       "hh3cevtModuleSw-LSPM1XP2P": hh3cevtModuleSw_LSPM1XP2P,
       "hh3cevtModuleSw-LSPM1CX2P": hh3cevtModuleSw_LSPM1CX2P,
       "hh3cevtModuleSw-STK-1000BASE-T": hh3cevtModuleSw_STK_1000BASE_T,
       "hh3cevtModuleSw-LSB1SRP1M0": hh3cevtModuleSw_LSB1SRP1M0,
       "hh3cevtModuleSw-LSB1SRP1M1": hh3cevtModuleSw_LSB1SRP1M1,
       "hh3cevtModuleSw-LSB1GP12DB": hh3cevtModuleSw_LSB1GP12DB,
       "hh3cevtModuleSw-LSB1GT12DB": hh3cevtModuleSw_LSB1GT12DB,
       "hh3cevtModuleSw-LSB1XK1DB": hh3cevtModuleSw_LSB1XK1DB,
       "hh3cevtModuleSw-LSB1XP2DB": hh3cevtModuleSw_LSB1XP2DB,
       "hh3cevtModuleSw-LSB1XP2DC": hh3cevtModuleSw_LSB1XP2DC,
       "hh3cevtModuleSw-LSB1GT48LDB": hh3cevtModuleSw_LSB1GT48LDB,
       "hh3cevtModuleSw-LSB1XP4TDB": hh3cevtModuleSw_LSB1XP4TDB,
       "hh3cevtModuleSw-LSB1XP4TDC": hh3cevtModuleSw_LSB1XP4TDC,
       "hh3cevtModuleSw-LSB1RSP2DC": hh3cevtModuleSw_LSB1RSP2DC,
       "hh3cevtModuleSw-LSB1VP2DC": hh3cevtModuleSw_LSB1VP2DC,
       "hh3cevtModuleSw-LSB1XP4DB": hh3cevtModuleSw_LSB1XP4DB,
       "hh3cevtModuleSw-LSB1SRP2E0": hh3cevtModuleSw_LSB1SRP2E0,
       "hh3cevtModuleSw-LSB1SRP2E1": hh3cevtModuleSw_LSB1SRP2E1,
       "hh3cevtModuleSw-LSB1SRP2E2": hh3cevtModuleSw_LSB1SRP2E2,
       "hh3cevtModuleSw-LSB1SRP2E3": hh3cevtModuleSw_LSB1SRP2E3,
       "hh3cevtModuleSw-SR01SRPUQ": hh3cevtModuleSw_SR01SRPUQ,
       "hh3cevtModuleSw-AHP1": hh3cevtModuleSw_AHP1,
       "hh3cevtModuleSw-AHP2": hh3cevtModuleSw_AHP2,
       "hh3cevtModuleSw-CLP1": hh3cevtModuleSw_CLP1,
       "hh3cevtModuleSw-CLP2": hh3cevtModuleSw_CLP2,
       "hh3cevtModuleSw-ET16": hh3cevtModuleSw_ET16,
       "hh3cevtModuleSw-LSB1SRP1NA0": hh3cevtModuleSw_LSB1SRP1NA0,
       "hh3cevtModuleSw-LSB1SRP1NA1": hh3cevtModuleSw_LSB1SRP1NA1,
       "hh3cevtModuleSw-LSB1SRP1NA2": hh3cevtModuleSw_LSB1SRP1NA2,
       "hh3cevtModuleSw-LSB1SRP1NA3": hh3cevtModuleSw_LSB1SRP1NA3,
       "hh3cevtModuleSw-SR01AHP1GWA": hh3cevtModuleSw_SR01AHP1GWA,
       "hh3cevtModuleSw-SR01AHP2GWA": hh3cevtModuleSw_SR01AHP2GWA,
       "hh3cevtModuleSw-SR01CLP1GWA": hh3cevtModuleSw_SR01CLP1GWA,
       "hh3cevtModuleSw-SR01CLP2GWA": hh3cevtModuleSw_SR01CLP2GWA,
       "hh3cevtModuleSw-SR01ET16GWA": hh3cevtModuleSw_SR01ET16GWA,
       "hh3cevtModuleSw-SR01GP12VB": hh3cevtModuleSw_SR01GP12VB,
       "hh3cevtModuleSw-SR01XK1VB": hh3cevtModuleSw_SR01XK1VB,
       "hh3cevtModuleSw-SR01XP2VC": hh3cevtModuleSw_SR01XP2VC,
       "hh3cevtModuleSw-SR01XP4LVB": hh3cevtModuleSw_SR01XP4LVB,
       "hh3cevtModuleSw-SR01SRPUEA": hh3cevtModuleSw_SR01SRPUEA,
       "hh3cevtModuleSw-LSB1SRP1N4": hh3cevtModuleSw_LSB1SRP1N4,
       "hh3cevtModuleSw-LSB1SRP1N5": hh3cevtModuleSw_LSB1SRP1N5,
       "hh3cevtModuleSw-LSB1SRP1N6": hh3cevtModuleSw_LSB1SRP1N6,
       "hh3cevtModuleSw-LSB1SRP1N7": hh3cevtModuleSw_LSB1SRP1N7,
       "hh3cevtModuleSw-LSB1SRP2N4": hh3cevtModuleSw_LSB1SRP2N4,
       "hh3cevtModuleSw-LSB1SRP2N5": hh3cevtModuleSw_LSB1SRP2N5,
       "hh3cevtModuleSw-LSB1SRP2N6": hh3cevtModuleSw_LSB1SRP2N6,
       "hh3cevtModuleSw-LSB1SRP2N7": hh3cevtModuleSw_LSB1SRP2N7,
       "hh3cevtModuleSw-LSB1SRP1NA4": hh3cevtModuleSw_LSB1SRP1NA4,
       "hh3cevtModuleSw-LSB1SRP1NA5": hh3cevtModuleSw_LSB1SRP1NA5,
       "hh3cevtModuleSw-LSB1SRP1NA6": hh3cevtModuleSw_LSB1SRP1NA6,
       "hh3cevtModuleSw-LSB1SRP1NA7": hh3cevtModuleSw_LSB1SRP1NA7,
       "hh3cevtModuleSw-LSB2GV48DA": hh3cevtModuleSw_LSB2GV48DA,
       "hh3cevtModuleSw-LSB1RGP2GDB": hh3cevtModuleSw_LSB1RGP2GDB,
       "hh3cevtModuleSw-LSB1RGP4GDB": hh3cevtModuleSw_LSB1RGP4GDB,
       "hh3cevtModuleSw-LSB2GP24DB": hh3cevtModuleSw_LSB2GP24DB,
       "hh3cevtModuleSw-LSB2GP24DC": hh3cevtModuleSw_LSB2GP24DC,
       "hh3cevtModuleSw-LSB2GT24DB": hh3cevtModuleSw_LSB2GT24DB,
       "hh3cevtModuleSw-LSB2FW8DB": hh3cevtModuleSw_LSB2FW8DB,
       "hh3cevtModuleSw-LSB2IPSEC8DB": hh3cevtModuleSw_LSB2IPSEC8DB,
       "hh3cevtModuleSw-LSB2GV48DB": hh3cevtModuleSw_LSB2GV48DB,
       "hh3cevtModuleSw-RGP2": hh3cevtModuleSw_RGP2,
       "hh3cevtModuleSw-RGP4": hh3cevtModuleSw_RGP4,
       "hh3cevtModuleSw-SR02FW8VB": hh3cevtModuleSw_SR02FW8VB,
       "hh3cevtModuleSw-SR02IPSEC8VB": hh3cevtModuleSw_SR02IPSEC8VB,
       "hh3cevtModuleSw-LSB2SRP1N0": hh3cevtModuleSw_LSB2SRP1N0,
       "hh3cevtModuleSw-LSB2SRP1N1": hh3cevtModuleSw_LSB2SRP1N1,
       "hh3cevtModuleSw-LSB2SRP1N2": hh3cevtModuleSw_LSB2SRP1N2,
       "hh3cevtModuleSw-LSB2SRP1N3": hh3cevtModuleSw_LSB2SRP1N3,
       "hh3cevtModuleSw-LSB2SRP1N4": hh3cevtModuleSw_LSB2SRP1N4,
       "hh3cevtModuleSw-LSB2SRP1N5": hh3cevtModuleSw_LSB2SRP1N5,
       "hh3cevtModuleSw-LSB2SRP1N6": hh3cevtModuleSw_LSB2SRP1N6,
       "hh3cevtModuleSw-LSB2SRP1N7": hh3cevtModuleSw_LSB2SRP1N7,
       "hh3cevtModuleSw-SR02SRPUE": hh3cevtModuleSw_SR02SRPUE,
       "hh3cevtModuleSw-SR01LN1BQH0": hh3cevtModuleSw_SR01LN1BQH0,
       "hh3cevtModuleSw-SR01DXP1L": hh3cevtModuleSw_SR01DXP1L,
       "hh3cevtModuleSw-SR01DGP10L": hh3cevtModuleSw_SR01DGP10L,
       "hh3cevtModuleSw-SR01DRSP2L": hh3cevtModuleSw_SR01DRSP2L,
       "hh3cevtModuleSw-SR01DRUP1L": hh3cevtModuleSw_SR01DRUP1L,
       "hh3cevtModuleSw-SR01DGP20R": hh3cevtModuleSw_SR01DGP20R,
       "hh3cevtModuleSw-SR01DPLP8L": hh3cevtModuleSw_SR01DPLP8L,
       "hh3cevtModuleSw-SR01DXP2R": hh3cevtModuleSw_SR01DXP2R,
       "hh3cevtModuleSw-LSB1FW2A0": hh3cevtModuleSw_LSB1FW2A0,
       "hh3cevtModuleSw-LSB1GP48LDB": hh3cevtModuleSw_LSB1GP48LDB,
       "hh3cevtModuleSw-SR01LN1BNA0": hh3cevtModuleSw_SR01LN1BNA0,
       "hh3cevtModuleSw-SR01LN2BQH0": hh3cevtModuleSw_SR01LN2BQH0,
       "hh3cevtModuleSw-SR01LN2BNA0": hh3cevtModuleSw_SR01LN2BNA0,
       "hh3cevtModuleSw-SR01DGT20R": hh3cevtModuleSw_SR01DGT20R,
       "hh3cevtModuleSw-SR01DPSP4L": hh3cevtModuleSw_SR01DPSP4L,
       "hh3cevtModuleSw-SR01DPUP1L": hh3cevtModuleSw_SR01DPUP1L,
       "hh3cevtModuleSw-SR01DPL2G6L": hh3cevtModuleSw_SR01DPL2G6L,
       "hh3cevtModuleSw-SR01DPH2G6L": hh3cevtModuleSw_SR01DPH2G6L,
       "hh3cevtModuleSw-SR01DPS2G4L": hh3cevtModuleSw_SR01DPS2G4L,
       "hh3cevtModuleSw-SR01DCL1G8L": hh3cevtModuleSw_SR01DCL1G8L,
       "hh3cevtModuleSw-SR01DCL2G8L": hh3cevtModuleSw_SR01DCL2G8L,
       "hh3cevtModuleSw-SR01DET8G8L": hh3cevtModuleSw_SR01DET8G8L,
       "hh3cevtModuleSw-SR02SRP2E3": hh3cevtModuleSw_SR02SRP2E3,
       "hh3cevtModuleSw-SR02SRP1E3": hh3cevtModuleSw_SR02SRP1E3,
       "hh3cevtModuleSw-SR02SRP1M3": hh3cevtModuleSw_SR02SRP1M3,
       "hh3cevtModuleSw-SR01DQCP4L": hh3cevtModuleSw_SR01DQCP4L,
       "hh3cevtModuleSw-SR01DTCP8L": hh3cevtModuleSw_SR01DTCP8L,
       "hh3cevtModuleSw-LSB1AFC1A0": hh3cevtModuleSw_LSB1AFC1A0,
       "hh3cevtModuleSw-LSB1SSL1A0": hh3cevtModuleSw_LSB1SSL1A0,
       "hh3cevtModuleSw-IMNAM": hh3cevtModuleSw_IMNAM,
       "hh3cevtModuleSw-IMNAT": hh3cevtModuleSw_IMNAT,
       "hh3cevtModuleSw-PICAHP1L": hh3cevtModuleSw_PICAHP1L,
       "hh3cevtModuleSw-PICALP4L": hh3cevtModuleSw_PICALP4L,
       "hh3cevtModuleSw-PICCHP4L": hh3cevtModuleSw_PICCHP4L,
       "hh3cevtModuleSw-PICCHS1G4L": hh3cevtModuleSw_PICCHS1G4L,
       "hh3cevtModuleSw-PICCLS4G4L": hh3cevtModuleSw_PICCLS4G4L,
       "hh3cevtModuleSw-PICCSP1L": hh3cevtModuleSw_PICCSP1L,
       "hh3cevtModuleSw-LSB1ACG1A0": hh3cevtModuleSw_LSB1ACG1A0,
       "hh3cevtModuleSw-LST1MRPNC1": hh3cevtModuleSw_LST1MRPNC1,
       "hh3cevtModuleSw-LST1SF18B1": hh3cevtModuleSw_LST1SF18B1,
       "hh3cevtModuleSw-LST1SF08B1": hh3cevtModuleSw_LST1SF08B1,
       "hh3cevtModuleSw-LST1GT48LEC1": hh3cevtModuleSw_LST1GT48LEC1,
       "hh3cevtModuleSw-LST1GP48LEC1": hh3cevtModuleSw_LST1GP48LEC1,
       "hh3cevtModuleSw-LST1XP4LEC1": hh3cevtModuleSw_LST1XP4LEC1,
       "hh3cevtModuleSw-LST1XP8LEC1": hh3cevtModuleSw_LST1XP8LEC1,
       "hh3cevtModuleSw-LSR1SRP2B1": hh3cevtModuleSw_LSR1SRP2B1,
       "hh3cevtModuleSw-LSR1SRP2C1": hh3cevtModuleSw_LSR1SRP2C1,
       "hh3cevtModuleSw-LSR1SRP2B2": hh3cevtModuleSw_LSR1SRP2B2,
       "hh3cevtModuleSw-LSR1SRP2C2": hh3cevtModuleSw_LSR1SRP2C2,
       "hh3cevtModuleSw-LSR1GT24LEC1": hh3cevtModuleSw_LSR1GT24LEC1,
       "hh3cevtModuleSw-LSR1GP24LEB1": hh3cevtModuleSw_LSR1GP24LEB1,
       "hh3cevtModuleSw-LSR1GP24LEC1": hh3cevtModuleSw_LSR1GP24LEC1,
       "hh3cevtModuleSw-LSR1GT48LEB1": hh3cevtModuleSw_LSR1GT48LEB1,
       "hh3cevtModuleSw-LSR1GT48LEC1": hh3cevtModuleSw_LSR1GT48LEC1,
       "hh3cevtModuleSw-LSR1GP48LEB1": hh3cevtModuleSw_LSR1GP48LEB1,
       "hh3cevtModuleSw-LSR1GP48LEC1": hh3cevtModuleSw_LSR1GP48LEC1,
       "hh3cevtModuleSw-LSR2GV48REB1": hh3cevtModuleSw_LSR2GV48REB1,
       "hh3cevtModuleSw-LSR1XP2LEB1": hh3cevtModuleSw_LSR1XP2LEB1,
       "hh3cevtModuleSw-LSR1XP2LEC1": hh3cevtModuleSw_LSR1XP2LEC1,
       "hh3cevtModuleSw-LSR1XP4LEB1": hh3cevtModuleSw_LSR1XP4LEB1,
       "hh3cevtModuleSw-LSR1XP4LEC1": hh3cevtModuleSw_LSR1XP4LEC1,
       "hh3cevtModuleSw-IMFW": hh3cevtModuleSw_IMFW,
       "hh3cevtModuleSw-LSB1LB1A0": hh3cevtModuleSw_LSB1LB1A0,
       "hh3cevtModuleSw-LSB1IPS1A0": hh3cevtModuleSw_LSB1IPS1A0,
       "hh3cevtModuleSw-LST1GT48LEB1": hh3cevtModuleSw_LST1GT48LEB1,
       "hh3cevtModuleSw-LST1GP48LEB1": hh3cevtModuleSw_LST1GP48LEB1,
       "hh3cevtModuleSw-LST1XP4LEB1": hh3cevtModuleSw_LST1XP4LEB1,
       "hh3cevtModuleSw-LST1XP8LEB1": hh3cevtModuleSw_LST1XP8LEB1,
       "hh3cevtModuleSw-LST1XP32REB1": hh3cevtModuleSw_LST1XP32REB1,
       "hh3cevtModuleSw-LST1XP32REC1": hh3cevtModuleSw_LST1XP32REC1,
       "hh3cevtModuleSw-LSR1FW2A1": hh3cevtModuleSw_LSR1FW2A1,
       "hh3cevtModuleSw-LSR1SSL1A1": hh3cevtModuleSw_LSR1SSL1A1,
       "hh3cevtModuleSw-SR01DET32G2L": hh3cevtModuleSw_SR01DET32G2L,
       "hh3cevtModuleSw-LSR1GP24LEF1": hh3cevtModuleSw_LSR1GP24LEF1,
       "hh3cevtModuleSw-LSR1XP4LEF1": hh3cevtModuleSw_LSR1XP4LEF1,
       "hh3cevtModuleSw-LSR1LB1A1": hh3cevtModuleSw_LSR1LB1A1,
       "hh3cevtModuleSw-LSR1NSM1A1": hh3cevtModuleSw_LSR1NSM1A1,
       "hh3cevtModuleSw-LSR1ACG1A1": hh3cevtModuleSw_LSR1ACG1A1,
       "hh3cevtModuleSw-LSR1IPS1A1": hh3cevtModuleSw_LSR1IPS1A1,
       "hh3cevtModuleSw-LSR2GP24LEB1": hh3cevtModuleSw_LSR2GP24LEB1,
       "hh3cevtModuleSw-LSR2GT24LEB1": hh3cevtModuleSw_LSR2GT24LEB1,
       "hh3cevtModuleSw-LSR2GT48LEB1": hh3cevtModuleSw_LSR2GT48LEB1,
       "hh3cevtModuleSw-SPC-GP24L": hh3cevtModuleSw_SPC_GP24L,
       "hh3cevtModuleSw-SPC-GT48L": hh3cevtModuleSw_SPC_GT48L,
       "hh3cevtModuleSw-SPC-GP48L": hh3cevtModuleSw_SPC_GP48L,
       "hh3cevtModuleSw-SPC-XP2L": hh3cevtModuleSw_SPC_XP2L,
       "hh3cevtModuleSw-SPC-XP4L": hh3cevtModuleSw_SPC_XP4L,
       "hh3cevtModuleSw-SR06SRP2E3": hh3cevtModuleSw_SR06SRP2E3,
       "hh3cevtModuleSw-SPE-2010-E": hh3cevtModuleSw_SPE_2010_E,
       "hh3cevtModuleSw-SPE-2020-E": hh3cevtModuleSw_SPE_2020_E,
       "hh3cevtModuleSw-SPC-XP4L-S-SDI": hh3cevtModuleSw_SPC_XP4L_S_SDI,
       "hh3cevtModuleSw-SPC-GT48L-SDI": hh3cevtModuleSw_SPC_GT48L_SDI,
       "hh3cevtModuleSw-SPC-GP48L-S-SDI": hh3cevtModuleSw_SPC_GP48L_S_SDI,
       "hh3cevtModuleSw-SPC-SR02OPMA0": hh3cevtModuleSw_SPC_SR02OPMA0,
       "hh3cevtModuleSw-LSR1XP16REB1": hh3cevtModuleSw_LSR1XP16REB1,
       "hh3cevtModuleSw-LSR1GP48LEF1": hh3cevtModuleSw_LSR1GP48LEF1,
       "hh3cevtModuleSw-LST1GP48LEF1": hh3cevtModuleSw_LST1GP48LEF1,
       "hh3cevtModuleSw-LST1XP8LEF1": hh3cevtModuleSw_LST1XP8LEF1,
       "hh3cevtModuleSw-SPE-1010-II": hh3cevtModuleSw_SPE_1010_II,
       "hh3cevtModuleSw-SPE-1010-E-II": hh3cevtModuleSw_SPE_1010_E_II,
       "hh3cevtModuleSw-SPE-1020-II": hh3cevtModuleSw_SPE_1020_II,
       "hh3cevtModuleSw-SPE-1020-E-II": hh3cevtModuleSw_SPE_1020_E_II,
       "hh3cevtModuleSw-LST1FW2A1": hh3cevtModuleSw_LST1FW2A1,
       "hh3cevtModuleSw-LST1NSM1A1": hh3cevtModuleSw_LST1NSM1A1,
       "hh3cevtModuleSw-LST1LB1A1": hh3cevtModuleSw_LST1LB1A1,
       "hh3cevtModuleSw-LST1ACG1A1": hh3cevtModuleSw_LST1ACG1A1,
       "hh3cevtModuleSw-LST1IPS1A1": hh3cevtModuleSw_LST1IPS1A1,
       "hh3cevtModuleSw-LSR1DRUP1L1": hh3cevtModuleSw_LSR1DRUP1L1,
       "hh3cevtModuleSw-LSR1DPUP1L1": hh3cevtModuleSw_LSR1DPUP1L1,
       "hh3cevtModuleSw-LSR1DPSP4L1": hh3cevtModuleSw_LSR1DPSP4L1,
       "hh3cevtModuleSw-LSR1DTCP8L1": hh3cevtModuleSw_LSR1DTCP8L1,
       "hh3cevtModuleSw-LSR1DXP1L1": hh3cevtModuleSw_LSR1DXP1L1,
       "hh3cevtModuleSw-LSR1DGP10L1": hh3cevtModuleSw_LSR1DGP10L1,
       "hh3cevtModuleSw-LSR1LN1BNL1": hh3cevtModuleSw_LSR1LN1BNL1,
       "hh3cevtModuleSw-LSR1LN2BL1": hh3cevtModuleSw_LSR1LN2BL1,
       "hh3cevtModuleSw-LSR1SRP2D1": hh3cevtModuleSw_LSR1SRP2D1,
       "hh3cevtModuleSw-IM-NAT-II": hh3cevtModuleSw_IM_NAT_II,
       "hh3cevtModuleSw-IM-NAM-II": hh3cevtModuleSw_IM_NAM_II,
       "hh3cevtModuleSw-CR-MRP-I": hh3cevtModuleSw_CR_MRP_I,
       "hh3cevtModuleSw-CR-SF18C": hh3cevtModuleSw_CR_SF18C,
       "hh3cevtModuleSw-CR-SF08C": hh3cevtModuleSw_CR_SF08C,
       "hh3cevtModuleSw-CR-SPC-XP8LEF": hh3cevtModuleSw_CR_SPC_XP8LEF,
       "hh3cevtModuleSw-CR-SPC-XP4LEF": hh3cevtModuleSw_CR_SPC_XP4LEF,
       "hh3cevtModuleSw-CR-SPC-GP48LEF": hh3cevtModuleSw_CR_SPC_GP48LEF,
       "hh3cevtModuleSw-CR-SPC-GT48LEF": hh3cevtModuleSw_CR_SPC_GT48LEF,
       "hh3cevtModuleSw-CR-SPE-3020-E": hh3cevtModuleSw_CR_SPE_3020_E,
       "hh3cevtModuleSw-CR-SPC-PUP4L-E": hh3cevtModuleSw_CR_SPC_PUP4L_E,
       "hh3cevtModuleSw-LST1SF08C1": hh3cevtModuleSw_LST1SF08C1,
       "hh3cevtModuleSw-LST1SF18C1": hh3cevtModuleSw_LST1SF18C1,
       "hh3cevtModuleSw-LS81GP16TM": hh3cevtModuleSw_LS81GP16TM,
       "hh3cevtModuleSw-LS81VP4C": hh3cevtModuleSw_LS81VP4C,
       "hh3cevtModuleSw-LS8M1PT8P0": hh3cevtModuleSw_LS8M1PT8P0,
       "hh3cevtModuleSw-LS8M1PT8GB0": hh3cevtModuleSw_LS8M1PT8GB0,
       "hh3cevtModuleSw-LS8M1PT4GB0": hh3cevtModuleSw_LS8M1PT4GB0,
       "hh3cevtModuleSw-LS81GP2R": hh3cevtModuleSw_LS81GP2R,
       "hh3cevtModuleSw-LS81GP4R": hh3cevtModuleSw_LS81GP4R,
       "hh3cevtModuleSw-LS81IPSECA": hh3cevtModuleSw_LS81IPSECA,
       "hh3cevtModuleSw-LS81FWA": hh3cevtModuleSw_LS81FWA,
       "hh3cevtModuleSw-LS82VSNP": hh3cevtModuleSw_LS82VSNP,
       "hh3cevtModuleSw-LSQ1GV48SA": hh3cevtModuleSw_LSQ1GV48SA,
       "hh3cevtModuleSw-LSQ1SRPB": hh3cevtModuleSw_LSQ1SRPB,
       "hh3cevtModuleSw-LSQ1SRP2XB": hh3cevtModuleSw_LSQ1SRP2XB,
       "hh3cevtModuleSw-LSQ1SRP1CB": hh3cevtModuleSw_LSQ1SRP1CB,
       "hh3cevtModuleSw-LSQ1FV48SA": hh3cevtModuleSw_LSQ1FV48SA,
       "hh3cevtModuleSw-LSD1MPUA": hh3cevtModuleSw_LSD1MPUA,
       "hh3cevtModuleSw-LSD1GP20A0": hh3cevtModuleSw_LSD1GP20A0,
       "hh3cevtModuleSw-LSD1GP20TA0": hh3cevtModuleSw_LSD1GP20TA0,
       "hh3cevtModuleSw-LSD1GP36A0": hh3cevtModuleSw_LSD1GP36A0,
       "hh3cevtModuleSw-LSD1GP20XA0": hh3cevtModuleSw_LSD1GP20XA0,
       "hh3cevtModuleSw-LSD1GP20EA0": hh3cevtModuleSw_LSD1GP20EA0,
       "hh3cevtModuleSw-LSD1GP20RA0": hh3cevtModuleSw_LSD1GP20RA0,
       "hh3cevtModuleSw-LSD1GP16A0": hh3cevtModuleSw_LSD1GP16A0,
       "hh3cevtModuleSw-LSD1GT16A0": hh3cevtModuleSw_LSD1GT16A0,
       "hh3cevtModuleSw-LSD1XP2A0": hh3cevtModuleSw_LSD1XP2A0,
       "hh3cevtModuleSw-LSD1EP2A0": hh3cevtModuleSw_LSD1EP2A0,
       "hh3cevtModuleSw-LSD1RP2A0": hh3cevtModuleSw_LSD1RP2A0,
       "hh3cevtModuleSw-LSQ1GV48SC": hh3cevtModuleSw_LSQ1GV48SC,
       "hh3cevtModuleSw-LSQ1FP48SA": hh3cevtModuleSw_LSQ1FP48SA,
       "hh3cevtModuleSw-LSQ1GP24SC": hh3cevtModuleSw_LSQ1GP24SC,
       "hh3cevtModuleSw-LSQ1GT24SC": hh3cevtModuleSw_LSQ1GT24SC,
       "hh3cevtModuleSw-LSQ1TGX2SC": hh3cevtModuleSw_LSQ1TGX2SC,
       "hh3cevtModuleSw-LSQ1GP12EA": hh3cevtModuleSw_LSQ1GP12EA,
       "hh3cevtModuleSw-LSQ1TGX1EA": hh3cevtModuleSw_LSQ1TGX1EA,
       "hh3cevtModuleSw-LSQ1P24XGSC": hh3cevtModuleSw_LSQ1P24XGSC,
       "hh3cevtModuleSw-LSQ1T24XGSC": hh3cevtModuleSw_LSQ1T24XGSC,
       "hh3cevtModuleSw-LS81TGX1B": hh3cevtModuleSw_LS81TGX1B,
       "hh3cevtModuleSw-LSQ1PT4PSC0": hh3cevtModuleSw_LSQ1PT4PSC0,
       "hh3cevtModuleSw-LS81SRPG13": hh3cevtModuleSw_LS81SRPG13,
       "hh3cevtModuleSw-LS81SRPG14": hh3cevtModuleSw_LS81SRPG14,
       "hh3cevtModuleSw-LS81SRPG15": hh3cevtModuleSw_LS81SRPG15,
       "hh3cevtModuleSw-LSQ1GP48SC0": hh3cevtModuleSw_LSQ1GP48SC0,
       "hh3cevtModuleSw-LSQ1GP12SC0": hh3cevtModuleSw_LSQ1GP12SC0,
       "hh3cevtModuleSw-LSD1SRPA": hh3cevtModuleSw_LSD1SRPA,
       "hh3cevtModuleSw-LSD1SRPB": hh3cevtModuleSw_LSD1SRPB,
       "hh3cevtModuleSw-LSD1SRPC": hh3cevtModuleSw_LSD1SRPC,
       "hh3cevtModuleSw-LSD1GT16PES0": hh3cevtModuleSw_LSD1GT16PES0,
       "hh3cevtModuleSw-LSD1GP24ES0": hh3cevtModuleSw_LSD1GP24ES0,
       "hh3cevtModuleSw-LSD1GT24XES0": hh3cevtModuleSw_LSD1GT24XES0,
       "hh3cevtModuleSw-LSD1GP24XES0": hh3cevtModuleSw_LSD1GP24XES0,
       "hh3cevtModuleSw-LSD1XP2ES0": hh3cevtModuleSw_LSD1XP2ES0,
       "hh3cevtModuleSw-LSD1GP48ES0": hh3cevtModuleSw_LSD1GP48ES0,
       "hh3cevtModuleSw-LSQ1MPUA0": hh3cevtModuleSw_LSQ1MPUA0,
       "hh3cevtModuleSw-LSQ1MPUA1": hh3cevtModuleSw_LSQ1MPUA1,
       "hh3cevtModuleSw-LSQ1FWBSC0": hh3cevtModuleSw_LSQ1FWBSC0,
       "hh3cevtModuleSw-LSQ1PT8PSC0": hh3cevtModuleSw_LSQ1PT8PSC0,
       "hh3cevtModuleSw-LSQ1PT16PSC0": hh3cevtModuleSw_LSQ1PT16PSC0,
       "hh3cevtModuleSw-SA11MPUA0": hh3cevtModuleSw_SA11MPUA0,
       "hh3cevtModuleSw-SA11MPUB0": hh3cevtModuleSw_SA11MPUB0,
       "hh3cevtModuleSw-LSQ1AFCBSC0": hh3cevtModuleSw_LSQ1AFCBSC0,
       "hh3cevtModuleSw-LSQ1MPUB0": hh3cevtModuleSw_LSQ1MPUB0,
       "hh3cevtModuleSw-LSQ1MPUB1": hh3cevtModuleSw_LSQ1MPUB1,
       "hh3cevtModuleSw-LSQ1PT4PSC1": hh3cevtModuleSw_LSQ1PT4PSC1,
       "hh3cevtModuleSw-LSQ1PT8PSC1": hh3cevtModuleSw_LSQ1PT8PSC1,
       "hh3cevtModuleSw-LSQ1PT16PSC1": hh3cevtModuleSw_LSQ1PT16PSC1,
       "hh3cevtModuleSw-LSQ1FP48USA0": hh3cevtModuleSw_LSQ1FP48USA0,
       "hh3cevtModuleSw-LSQ1FP48USA1": hh3cevtModuleSw_LSQ1FP48USA1,
       "hh3cevtModuleSw-LSQ1FV48USA0": hh3cevtModuleSw_LSQ1FV48USA0,
       "hh3cevtModuleSw-LSQ1FV48USA1": hh3cevtModuleSw_LSQ1FV48USA1,
       "hh3cevtModuleSw-LSQ1SRPD0": hh3cevtModuleSw_LSQ1SRPD0,
       "hh3cevtModuleSw-LSQ1CGP24TSC0": hh3cevtModuleSw_LSQ1CGP24TSC0,
       "hh3cevtModuleSw-LSQ1GP24TSC0": hh3cevtModuleSw_LSQ1GP24TSC0,
       "hh3cevtModuleSw-LSQ1ACGASC0": hh3cevtModuleSw_LSQ1ACGASC0,
       "hh3cevtModuleSw-LSD1XP1ES0": hh3cevtModuleSw_LSD1XP1ES0,
       "hh3cevtModuleSw-LSD1GP12ES0": hh3cevtModuleSw_LSD1GP12ES0,
       "hh3cevtModuleSw-LSQ1SRP12GB0": hh3cevtModuleSw_LSQ1SRP12GB0,
       "hh3cevtModuleSw-LSQ1GV40PSC0": hh3cevtModuleSw_LSQ1GV40PSC0,
       "hh3cevtModuleSw-LSQ1FWBSC1": hh3cevtModuleSw_LSQ1FWBSC1,
       "hh3cevtModuleSw-LSQ1NSMSC0": hh3cevtModuleSw_LSQ1NSMSC0,
       "hh3cevtModuleSw-LSQ1NSMSC1": hh3cevtModuleSw_LSQ1NSMSC1,
       "hh3cevtModuleSw-LSQ1AFDBSC0": hh3cevtModuleSw_LSQ1AFDBSC0,
       "hh3cevtModuleSw-LS81MPUB": hh3cevtModuleSw_LS81MPUB,
       "hh3cevtModuleSw-LS81FP48XL": hh3cevtModuleSw_LS81FP48XL,
       "hh3cevtModuleSw-LS81FT48XL": hh3cevtModuleSw_LS81FT48XL,
       "hh3cevtModuleSw-LS81GP12XL": hh3cevtModuleSw_LS81GP12XL,
       "hh3cevtModuleSw-LS81GP24XL": hh3cevtModuleSw_LS81GP24XL,
       "hh3cevtModuleSw-LS81GP48XL": hh3cevtModuleSw_LS81GP48XL,
       "hh3cevtModuleSw-LS81GT24XL": hh3cevtModuleSw_LS81GT24XL,
       "hh3cevtModuleSw-LS81GT48XL": hh3cevtModuleSw_LS81GT48XL,
       "hh3cevtModuleSw-LS81TGX2XL": hh3cevtModuleSw_LS81TGX2XL,
       "hh3cevtModuleSw-LSQ1GV48SD0": hh3cevtModuleSw_LSQ1GV48SD0,
       "hh3cevtModuleSw-LSQ1GP48EB0": hh3cevtModuleSw_LSQ1GP48EB0,
       "hh3cevtModuleSw-LSQ1IPSSC0": hh3cevtModuleSw_LSQ1IPSSC0,
       "hh3cevtModuleSw-LSQ1GV48SD1": hh3cevtModuleSw_LSQ1GV48SD1,
       "hh3cevtModuleSw-LSQ1GP48SD0": hh3cevtModuleSw_LSQ1GP48SD0,
       "hh3cevtModuleSw-LSQ1GP48SD1": hh3cevtModuleSw_LSQ1GP48SD1,
       "hh3cevtModuleSw-LSQ1SRPA0": hh3cevtModuleSw_LSQ1SRPA0,
       "hh3cevtModuleSw-LSQ1SRPA1": hh3cevtModuleSw_LSQ1SRPA1,
       "hh3cevtModuleSw-LSQ2FP48SA0": hh3cevtModuleSw_LSQ2FP48SA0,
       "hh3cevtModuleSw-LSQ2FP48SA1": hh3cevtModuleSw_LSQ2FP48SA1,
       "hh3cevtModuleSw-LSQ2FT48SA0": hh3cevtModuleSw_LSQ2FT48SA0,
       "hh3cevtModuleSw-LSQ2FT48SA1": hh3cevtModuleSw_LSQ2FT48SA1,
       "hh3cevtModuleSw-LSQ1GV24PSC0": hh3cevtModuleSw_LSQ1GV24PSC0,
       "hh3cevtModuleSw-LSQ1GV24PSC1": hh3cevtModuleSw_LSQ1GV24PSC1,
       "hh3cevtModuleSw-LSQ1CGV24PSC0": hh3cevtModuleSw_LSQ1CGV24PSC0,
       "hh3cevtModuleSw-LSQ1CGV24PSC1": hh3cevtModuleSw_LSQ1CGV24PSC1,
       "hh3cevtModuleSw-LSQ1GP24TEB0": hh3cevtModuleSw_LSQ1GP24TEB0,
       "hh3cevtModuleSw-LSQ1GP24TEB1": hh3cevtModuleSw_LSQ1GP24TEB1,
       "hh3cevtModuleSw-LSQ1GP24TSD0": hh3cevtModuleSw_LSQ1GP24TSD0,
       "hh3cevtModuleSw-LSQ1GP24TSD1": hh3cevtModuleSw_LSQ1GP24TSD1,
       "hh3cevtModuleSw-LSQ1GP24TXSD0": hh3cevtModuleSw_LSQ1GP24TXSD0,
       "hh3cevtModuleSw-LSQ1GP24TXSD1": hh3cevtModuleSw_LSQ1GP24TXSD1,
       "hh3cevtModuleSw-LSQ1TGX2EB0": hh3cevtModuleSw_LSQ1TGX2EB0,
       "hh3cevtModuleSw-LSQ1TGX2EB1": hh3cevtModuleSw_LSQ1TGX2EB1,
       "hh3cevtModuleSw-LSQ1TGX2SD0": hh3cevtModuleSw_LSQ1TGX2SD0,
       "hh3cevtModuleSw-LSQ1TGX2SD1": hh3cevtModuleSw_LSQ1TGX2SD1,
       "hh3cevtModuleSw-LSQ1TGX4SD0": hh3cevtModuleSw_LSQ1TGX4SD0,
       "hh3cevtModuleSw-LSQ1TGX4SD1": hh3cevtModuleSw_LSQ1TGX4SD1,
       "hh3cevtModuleSw-LSQ1TGX8SD0": hh3cevtModuleSw_LSQ1TGX8SD0,
       "hh3cevtModuleSw-LSQ1TGX8SD1": hh3cevtModuleSw_LSQ1TGX8SD1,
       "hh3cevtModuleSw-LSQ1GP48EB1": hh3cevtModuleSw_LSQ1GP48EB1,
       "hh3cevtModuleSw-LSQ1TGX4EB0": hh3cevtModuleSw_LSQ1TGX4EB0,
       "hh3cevtModuleSw-LSQ1TGX4EB1": hh3cevtModuleSw_LSQ1TGX4EB1,
       "hh3cevtModuleSw-LSQ1GP12SC3": hh3cevtModuleSw_LSQ1GP12SC3,
       "hh3cevtModuleSw-LSQ1GP24TSC3": hh3cevtModuleSw_LSQ1GP24TSC3,
       "hh3cevtModuleSw-LSQ1GP48SC3": hh3cevtModuleSw_LSQ1GP48SC3,
       "hh3cevtModuleSw-LSQ1GV48SC3": hh3cevtModuleSw_LSQ1GV48SC3,
       "hh3cevtModuleSw-LSQ1MPUA3": hh3cevtModuleSw_LSQ1MPUA3,
       "hh3cevtModuleSw-LSQ1SRP1CB3": hh3cevtModuleSw_LSQ1SRP1CB3,
       "hh3cevtModuleSw-LSQ1SRPA3": hh3cevtModuleSw_LSQ1SRPA3,
       "hh3cevtModuleSw-LSQ2FP48SA3": hh3cevtModuleSw_LSQ2FP48SA3,
       "hh3cevtModuleSw-LSQ2FT48SA3": hh3cevtModuleSw_LSQ2FT48SA3,
       "hh3cevtModuleSw-LSQ1MPUB3": hh3cevtModuleSw_LSQ1MPUB3,
       "hh3cevtModuleSw-LSQ1CGP24TSC3": hh3cevtModuleSw_LSQ1CGP24TSC3,
       "hh3cevtModuleSw-LSQ1MPUB4": hh3cevtModuleSw_LSQ1MPUB4,
       "hh3cevtModuleSw-LSQ1SRPD4": hh3cevtModuleSw_LSQ1SRPD4,
       "hh3cevtModuleSw-LSQ1SSLSC0": hh3cevtModuleSw_LSQ1SSLSC0,
       "hh3cevtModuleSw-LSQ1LBSC0": hh3cevtModuleSw_LSQ1LBSC0,
       "hh3cevtModuleSw-LSQ1NAT24SC0": hh3cevtModuleSw_LSQ1NAT24SC0,
       "hh3cevtModuleSw-LSQ1SRP12GB4": hh3cevtModuleSw_LSQ1SRP12GB4,
       "hh3cevtModuleSw-LSQ1TGS8SC0": hh3cevtModuleSw_LSQ1TGS8SC0,
       "hh3cevtModuleSw-LSQ3PT4PSC0": hh3cevtModuleSw_LSQ3PT4PSC0,
       "hh3cevtModuleSw-EWPXM2MPUB0": hh3cevtModuleSw_EWPXM2MPUB0,
       "hh3cevtModuleSw-EWPXM2SRP12GB0": hh3cevtModuleSw_EWPXM2SRP12GB0,
       "hh3cevtModuleSw-EWPXM2SRPD0": hh3cevtModuleSw_EWPXM2SRPD0,
       "hh3cevtModuleSw-EWPXM2GP24TSD0": hh3cevtModuleSw_EWPXM2GP24TSD0,
       "hh3cevtModuleSw-EWPXM2GP24TXSD0": hh3cevtModuleSw_EWPXM2GP24TXSD0,
       "hh3cevtModuleSw-EWPXM2TGX4SD0": hh3cevtModuleSw_EWPXM2TGX4SD0,
       "hh3cevtModuleSw-EWPXM2GP48SD0": hh3cevtModuleSw_EWPXM2GP48SD0,
       "hh3cevtModuleSw-EWPXM2GP24TSC0": hh3cevtModuleSw_EWPXM2GP24TSC0,
       "hh3cevtModuleSw-EWPXM2TGX2SC0": hh3cevtModuleSw_EWPXM2TGX2SC0,
       "hh3cevtModuleSw-EWPXM2GP48SC0": hh3cevtModuleSw_EWPXM2GP48SC0,
       "hh3cevtModuleSw-LS7500-GP48-SC": hh3cevtModuleSw_LS7500_GP48_SC,
       "hh3cevtModuleSw-LS7500-GP48-SD": hh3cevtModuleSw_LS7500_GP48_SD,
       "hh3cevtModuleSw-LS7500-GT48-SC": hh3cevtModuleSw_LS7500_GT48_SC,
       "hh3cevtModuleSw-LS7500-GT48-SD": hh3cevtModuleSw_LS7500_GT48_SD,
       "hh3cevtModuleSw-LS7500-SRPG1": hh3cevtModuleSw_LS7500_SRPG1,
       "hh3cevtModuleSw-LS7500-SRPG2": hh3cevtModuleSw_LS7500_SRPG2,
       "hh3cevtModuleSw-LS7500-XP4-SD": hh3cevtModuleSw_LS7500_XP4_SD,
       "hh3cevtModuleSw-LS7500-XP8-SD": hh3cevtModuleSw_LS7500_XP8_SD,
       "hh3cevtModuleSw-LSQ4PT4PSC0": hh3cevtModuleSw_LSQ4PT4PSC0,
       "hh3cevtModuleSw-LSQ4PT8PSC0": hh3cevtModuleSw_LSQ4PT8PSC0,
       "hh3cevtModuleSw-LSQ4PT16PSC0": hh3cevtModuleSw_LSQ4PT16PSC0,
       "hh3cevtModuleSw-LSQ1GP24TSA0": hh3cevtModuleSw_LSQ1GP24TSA0,
       "hh3cevtModuleSw-LSQ1GV24PSA0": hh3cevtModuleSw_LSQ1GV24PSA0,
       "hh3cevtModuleSw-LSQ1SRPD3": hh3cevtModuleSw_LSQ1SRPD3,
       "hh3cevtModuleSw-LSQ1SUPA0": hh3cevtModuleSw_LSQ1SUPA0,
       "hh3cevtModuleSw-LSU1FAB04A0": hh3cevtModuleSw_LSU1FAB04A0,
       "hh3cevtModuleSw-LSU1FAB08A0": hh3cevtModuleSw_LSU1FAB08A0,
       "hh3cevtModuleSw-LSU1TGS8EA0": hh3cevtModuleSw_LSU1TGS8EA0,
       "hh3cevtModuleSw-LSU1TGS8EB0": hh3cevtModuleSw_LSU1TGS8EB0,
       "hh3cevtModuleSw-LSU1TGS8SE0": hh3cevtModuleSw_LSU1TGS8SE0,
       "hh3cevtModuleSw-LSUTGS16SC0": hh3cevtModuleSw_LSUTGS16SC0,
       "hh3cevtModuleSw-LUS1SUPA0": hh3cevtModuleSw_LUS1SUPA0,
       "hh3cevtModuleSw-LSU1GP24TXEA0": hh3cevtModuleSw_LSU1GP24TXEA0,
       "hh3cevtModuleSw-LSU1GP24TXEB0": hh3cevtModuleSw_LSU1GP24TXEB0,
       "hh3cevtModuleSw-LSU1GP24TXSE0": hh3cevtModuleSw_LSU1GP24TXSE0,
       "hh3cevtModuleSw-LSU1GP48EA0": hh3cevtModuleSw_LSU1GP48EA0,
       "hh3cevtModuleSw-LSU1GP48EB0": hh3cevtModuleSw_LSU1GP48EB0,
       "hh3cevtModuleSw-LSU1GP48SE0": hh3cevtModuleSw_LSU1GP48SE0,
       "hh3cevtModuleSw-LSU1GT48EA0": hh3cevtModuleSw_LSU1GT48EA0,
       "hh3cevtModuleSw-LSU1GT48SE0": hh3cevtModuleSw_LSU1GT48SE0,
       "hh3cevtModuleSw-LSU1TGX4EA0": hh3cevtModuleSw_LSU1TGX4EA0,
       "hh3cevtModuleSw-LSU1TGX4EB0": hh3cevtModuleSw_LSU1TGX4EB0,
       "hh3cevtModuleSw-LSU1TGX4SE0": hh3cevtModuleSw_LSU1TGX4SE0,
       "hh3cevtModuleSw-LSQ1FAB08A0": hh3cevtModuleSw_LSQ1FAB08A0,
       "hh3cevtModuleSw-EWPX2WCMD0": hh3cevtModuleSw_EWPX2WCMD0,
       "hh3cevtModuleSw-LSQ1WCMD0": hh3cevtModuleSw_LSQ1WCMD0,
       "hh3cevtModuleSw-LSQ1IAGSC0": hh3cevtModuleSw_LSQ1IAGSC0,
       "hh3cevtModuleSw-LSU1GP24TSE0": hh3cevtModuleSw_LSU1GP24TSE0,
       "hh3cevtModuleSw-LSQ1TGS16SC0": hh3cevtModuleSw_LSQ1TGS16SC0,
       "hh3cevtModuleSw-EWPX2TGS16SC0": hh3cevtModuleSw_EWPX2TGS16SC0,
       "hh3cevtModuleSw-LSQ1SUPA3": hh3cevtModuleSw_LSQ1SUPA3,
       "hh3cevtModuleSw-LSQ1FAB04A3": hh3cevtModuleSw_LSQ1FAB04A3,
       "hh3cevtModuleSw-LSQ1FAB08A3": hh3cevtModuleSw_LSQ1FAB08A3,
       "hh3cevtModuleSw-1000BASE-X-COMBO": hh3cevtModuleSw_1000BASE_X_COMBO,
       "hh3cevtModuleSw-EPON-1000M": hh3cevtModuleSw_EPON_1000M,
       "hh3cevtModuleSw-1000BASE-FIXED-2SFP-T-2RJ45": hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45,
       "hh3cevtModuleSw-100M-1550-BIDI": hh3cevtModuleSw_100M_1550_BIDI,
       "hh3cevtModuleSw-100M-1310-BIDI": hh3cevtModuleSw_100M_1310_BIDI,
       "hh3cevtModuleSw-1000BASE-FIXED-4RJ45-4SFP-COMBO": hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO,
       "hh3cevtModuleSw-LSH1PK2T": hh3cevtModuleSw_LSH1PK2T,
       "hh3cevtModuleSw-LSPM2GP2P": hh3cevtModuleSw_LSPM2GP2P,
       "hh3cevtModuleSw-LSWM1GT16P": hh3cevtModuleSw_LSWM1GT16P,
       "hh3cevtModuleSw-LSWM1GP16P": hh3cevtModuleSw_LSWM1GP16P,
       "hh3cevtModuleSw-LSWM1XP2P": hh3cevtModuleSw_LSWM1XP2P,
       "hh3cevtModuleSw-LSWM1XP4P": hh3cevtModuleSw_LSWM1XP4P,
       "hh3cevtModuleSw-LSWM1SP2P": hh3cevtModuleSw_LSWM1SP2P,
       "hh3cevtModuleSw-LSWM1SP4P": hh3cevtModuleSw_LSWM1SP4P,
       "hh3cevtModuleSw-LSWM148POEM": hh3cevtModuleSw_LSWM148POEM,
       "hh3cevtModuleSw-LSWM1FW10": hh3cevtModuleSw_LSWM1FW10,
       "hh3cevtModuleSw-LSWM1WCM10": hh3cevtModuleSw_LSWM1WCM10,
       "hh3cevtModuleSw-LSWM1IPS10": hh3cevtModuleSw_LSWM1IPS10,
       "hh3cevtModuleSw-LSWM1WCM20": hh3cevtModuleSw_LSWM1WCM20,
       "hh3cevtModuleSw-IPS-T1000-M": hh3cevtModuleSw_IPS_T1000_M,
       "hh3cevtModuleSw-IPS-T1000-A": hh3cevtModuleSw_IPS_T1000_A,
       "hh3cevtModuleSw-IPS-T1000-S": hh3cevtModuleSw_IPS_T1000_S,
       "hh3cevtModuleSw-IPS-GX4C": hh3cevtModuleSw_IPS_GX4C,
       "hh3cevtModuleSw-IPS-GT4C": hh3cevtModuleSw_IPS_GT4C,
       "hh3cevtModuleSw-LSPM2SP2P": hh3cevtModuleSw_LSPM2SP2P,
       "hh3cevtModuleSw-LSPM2SP2PA": hh3cevtModuleSw_LSPM2SP2PA,
       "hh3cevtModuleSw-LSP5GP8P": hh3cevtModuleSw_LSP5GP8P,
       "hh3cevtModuleSw-LSP5GT8P": hh3cevtModuleSw_LSP5GT8P,
       "hh3cevtModuleSw-LSWM1FC4P": hh3cevtModuleSw_LSWM1FC4P,
       "hh3cevtModuleSw-WX5002MPU": hh3cevtModuleSw_WX5002MPU,
       "hh3cevtModuleSw-LS8M1WCMA": hh3cevtModuleSw_LS8M1WCMA,
       "hh3cevtModuleSw-EWPX1G24XA0": hh3cevtModuleSw_EWPX1G24XA0,
       "hh3cevtModuleSw-LSQ1WCMB0": hh3cevtModuleSw_LSQ1WCMB0,
       "hh3cevtModuleSw-LSB1WCM2A0": hh3cevtModuleSw_LSB1WCM2A0,
       "hh3cevtModuleSw-EWPX1WCMB0": hh3cevtModuleSw_EWPX1WCMB0,
       "hh3cevtModuleSw-EWPX1G24XC0": hh3cevtModuleSw_EWPX1G24XC0,
       "hh3cevtModuleSw-EWPX1WCMC0": hh3cevtModuleSw_EWPX1WCMC0,
       "hh3cevtModuleSw-EWPX1FWA0": hh3cevtModuleSw_EWPX1FWA0,
       "hh3cevtModuleSw-EWPX1G10XC0": hh3cevtModuleSw_EWPX1G10XC0,
       "hh3cevtModuleSw-EWPX1WCM10C0": hh3cevtModuleSw_EWPX1WCM10C0,
       "hh3cevtModuleSw-LSR1WCM2A1": hh3cevtModuleSw_LSR1WCM2A1,
       "hh3cevtModuleSw-EWPX1WAP0": hh3cevtModuleSw_EWPX1WAP0,
       "hh3cevtModuleSw-EWPX1WCMD0": hh3cevtModuleSw_EWPX1WCMD0,
       "hh3cevtModuleSw-EWPX1G24XCE0": hh3cevtModuleSw_EWPX1G24XCE0,
       "hh3cevtModuleSw-EWPX1WCMCE0": hh3cevtModuleSw_EWPX1WCMCE0,
       "hh3cevtModuleSw-LSR1DRSP2L1": hh3cevtModuleSw_LSR1DRSP2L1,
       "hh3cevtModuleSw-PIC-CLF2G8L": hh3cevtModuleSw_PIC_CLF2G8L,
       "hh3cevtModuleSw-PIC-CLF4G8L": hh3cevtModuleSw_PIC_CLF4G8L,
       "hh3cevtModuleSw-SR02SRP2F3": hh3cevtModuleSw_SR02SRP2F3,
       "hh3cevtModuleSw-SR02SRP1F3": hh3cevtModuleSw_SR02SRP1F3,
       "hh3cevtModuleSw-LST1GT48LEA1": hh3cevtModuleSw_LST1GT48LEA1,
       "hh3cevtModuleSw-LST1GP48LEA1": hh3cevtModuleSw_LST1GP48LEA1,
       "hh3cevtModuleSw-LST2XP8LEA1": hh3cevtModuleSw_LST2XP8LEA1,
       "hh3cevtModuleSw-LST1GT48LEY1": hh3cevtModuleSw_LST1GT48LEY1,
       "hh3cevtModuleSw-LST1GP48LEY1": hh3cevtModuleSw_LST1GP48LEY1,
       "hh3cevtModuleSw-LST1XP32REY1": hh3cevtModuleSw_LST1XP32REY1,
       "hh3cevtModuleSw-LST1XP8LEY1": hh3cevtModuleSw_LST1XP8LEY1,
       "hh3cevtModuleSw-LST1GP48LEZ1": hh3cevtModuleSw_LST1GP48LEZ1,
       "hh3cevtModuleSw-LST1XP8LEZ1": hh3cevtModuleSw_LST1XP8LEZ1,
       "hh3cevtModuleSw-IM-FW-II": hh3cevtModuleSw_IM_FW_II,
       "hh3cevtModuleSw-IM-IPS": hh3cevtModuleSw_IM_IPS,
       "hh3cevtModuleSw-IM-SSL": hh3cevtModuleSw_IM_SSL,
       "hh3cevtModuleSw-IM-LB": hh3cevtModuleSw_IM_LB,
       "hh3cevtModuleSw-IM-ACG": hh3cevtModuleSw_IM_ACG,
       "hh3cevtModuleSw-LSR1XP16REC1": hh3cevtModuleSw_LSR1XP16REC1,
       "hh3cevtModuleSw-LST2XP8LEB1": hh3cevtModuleSw_LST2XP8LEB1,
       "hh3cevtModuleSw-LST2XP8LEC1": hh3cevtModuleSw_LST2XP8LEC1,
       "hh3cevtModuleSw-LST2XP8LEF1": hh3cevtModuleSw_LST2XP8LEF1,
       "hh3cevtModuleSw-LSR2XP4LEB1": hh3cevtModuleSw_LSR2XP4LEB1,
       "hh3cevtModuleSw-LSR2XP4LEC1": hh3cevtModuleSw_LSR2XP4LEC1,
       "hh3cevtModuleSw-LST2XP32REB1": hh3cevtModuleSw_LST2XP32REB1,
       "hh3cevtModuleSw-LST2XP32REC1": hh3cevtModuleSw_LST2XP32REC1,
       "hh3cevtModuleSw-LSR1WCM3A1": hh3cevtModuleSw_LSR1WCM3A1,
       "hh3cevtModuleSw-LST1XP16LEB1": hh3cevtModuleSw_LST1XP16LEB1,
       "hh3cevtModuleSw-LST1XP16LEC1": hh3cevtModuleSw_LST1XP16LEC1,
       "hh3cevtModuleSw-CR-SPC-XP4L-E-I": hh3cevtModuleSw_CR_SPC_XP4L_E_I,
       "hh3cevtSubModuleRouter": hh3cevtSubModuleRouter,
       "hh3cevtSubModuleSwitch": hh3cevtSubModuleSwitch,
       "hh3cevtPort": hh3cevtPort,
       "hh3cevtPortUnknownPorts": hh3cevtPortUnknownPorts,
       "hh3cevtPortCommonPorts": hh3cevtPortCommonPorts,
       "hh3cevtPortRouterType": hh3cevtPortRouterType,
       "hh3cevtPortRt-Async": hh3cevtPortRt_Async,
       "hh3cevtPortRt-Analogmodem": hh3cevtPortRt_Analogmodem,
       "hh3cevtPortRt-Atm": hh3cevtPortRt_Atm,
       "hh3cevtPortRt-AtmAdsl": hh3cevtPortRt_AtmAdsl,
       "hh3cevtPortRt-AtmShdsl": hh3cevtPortRt_AtmShdsl,
       "hh3cevtPortRt-AtmE1": hh3cevtPortRt_AtmE1,
       "hh3cevtPortRt-AtmT1": hh3cevtPortRt_AtmT1,
       "hh3cevtPortRt-AtmE3": hh3cevtPortRt_AtmE3,
       "hh3cevtPortRt-AtmT3": hh3cevtPortRt_AtmT3,
       "hh3cevtPortRt-Atm622M": hh3cevtPortRt_Atm622M,
       "hh3cevtPortRt-AtmImaE1": hh3cevtPortRt_AtmImaE1,
       "hh3cevtPortRt-AtmImaT1": hh3cevtPortRt_AtmImaT1,
       "hh3cevtPortRt-Atm25M": hh3cevtPortRt_Atm25M,
       "hh3cevtPortRt-Bri": hh3cevtPortRt_Bri,
       "hh3cevtPortRt-Console": hh3cevtPortRt_Console,
       "hh3cevtPortRt-E1": hh3cevtPortRt_E1,
       "hh3cevtPortRt-E3": hh3cevtPortRt_E3,
       "hh3cevtPortRt-T1": hh3cevtPortRt_T1,
       "hh3cevtPortRt-T3": hh3cevtPortRt_T3,
       "hh3cevtPortRt-Cpos": hh3cevtPortRt_Cpos,
       "hh3cevtPortRt-Ethernet": hh3cevtPortRt_Ethernet,
       "hh3cevtPortRt-Serial": hh3cevtPortRt_Serial,
       "hh3cevtPortRt-E1f": hh3cevtPortRt_E1f,
       "hh3cevtPortRt-T1f": hh3cevtPortRt_T1f,
       "hh3cevtPortRt-Pos": hh3cevtPortRt_Pos,
       "hh3cevtPortRt-Ge": hh3cevtPortRt_Ge,
       "hh3cevtPortRt-Aux": hh3cevtPortRt_Aux,
       "hh3cevtPortRt-VG-Fxs": hh3cevtPortRt_VG_Fxs,
       "hh3cevtPortRt-VG-Fxo": hh3cevtPortRt_VG_Fxo,
       "hh3cevtPortRt-VG-E1vi": hh3cevtPortRt_VG_E1vi,
       "hh3cevtPortRt-VG-T1vi": hh3cevtPortRt_VG_T1vi,
       "hh3cevtPortRt-Usb": hh3cevtPortRt_Usb,
       "hh3cevtPortRt-Ndec": hh3cevtPortRt_Ndec,
       "hh3cevtPortRt-Cavium": hh3cevtPortRt_Cavium,
       "hh3cevtPortRt-Fcm": hh3cevtPortRt_Fcm,
       "hh3cevtPortRt-E1vi": hh3cevtPortRt_E1vi,
       "hh3cevtPortRt-T1vi": hh3cevtPortRt_T1vi,
       "hh3cevtPortRt-Vi": hh3cevtPortRt_Vi,
       "hh3cevtPortRt-Adls2Plus": hh3cevtPortRt_Adls2Plus,
       "hh3cevtPortRt-RADIO-AG": hh3cevtPortRt_RADIO_AG,
       "hh3cevtPortRt-1exp": hh3cevtPortRt_1exp,
       "hh3cevtPortRt-G-SHDSL-BIS": hh3cevtPortRt_G_SHDSL_BIS,
       "hh3cevtPortRt-ONU-1000BASE-BX-SFF-SC": hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC,
       "hh3cevtPortRt-CELLULAR": hh3cevtPortRt_CELLULAR,
       "hh3cevtPortSwitchType": hh3cevtPortSwitchType,
       "hh3cevtPortSw-10or100M": hh3cevtPortSw_10or100M,
       "hh3cevtPortSw-1000BaseLxSm": hh3cevtPortSw_1000BaseLxSm,
       "hh3cevtPortSw-1000BaseSxMm": hh3cevtPortSw_1000BaseSxMm,
       "hh3cevtPortSw-1000BaseTx": hh3cevtPortSw_1000BaseTx,
       "hh3cevtPortSw-100MSinglemodeFx": hh3cevtPortSw_100MSinglemodeFx,
       "hh3cevtPortSw-100MMultimodeFx": hh3cevtPortSw_100MMultimodeFx,
       "hh3cevtPortSw-100M100BaseTx": hh3cevtPortSw_100M100BaseTx,
       "hh3cevtPortSw-100MHub": hh3cevtPortSw_100MHub,
       "hh3cevtPortSw-Vdsl": hh3cevtPortSw_Vdsl,
       "hh3cevtPortSw-Stack": hh3cevtPortSw_Stack,
       "hh3cevtPortSw-1000BaseZenithFx": hh3cevtPortSw_1000BaseZenithFx,
       "hh3cevtPortSw-1000BaseLongFx": hh3cevtPortSw_1000BaseLongFx,
       "hh3cevtPortSw-Adsl": hh3cevtPortSw_Adsl,
       "hh3cevtPortSw-10or100MDb": hh3cevtPortSw_10or100MDb,
       "hh3cevtPortSw-10GBaseLrSm": hh3cevtPortSw_10GBaseLrSm,
       "hh3cevtPortSw-10GBaseLx4Mm": hh3cevtPortSw_10GBaseLx4Mm,
       "hh3cevtPortSw-10GBaseLx4Sm": hh3cevtPortSw_10GBaseLx4Sm,
       "hh3cevtPortSw-100MLongFx": hh3cevtPortSw_100MLongFx,
       "hh3cevtPortSw-1000BaseCx": hh3cevtPortSw_1000BaseCx,
       "hh3cevtPortSw-1000BaseZenithFxLc": hh3cevtPortSw_1000BaseZenithFxLc,
       "hh3cevtPortSw-1000BaseLongFxLc": hh3cevtPortSw_1000BaseLongFxLc,
       "hh3cevtPortSw-100MSmFxSc": hh3cevtPortSw_100MSmFxSc,
       "hh3cevtPortSw-100MMmFxSc": hh3cevtPortSw_100MMmFxSc,
       "hh3cevtPortSw-100MSmFxLc": hh3cevtPortSw_100MSmFxLc,
       "hh3cevtPortSw-100MMmFxLc": hh3cevtPortSw_100MMmFxLc,
       "hh3cevtPortSw-GbicNoConnector": hh3cevtPortSw_GbicNoConnector,
       "hh3cevtPortSw-Gbic1000BaseT": hh3cevtPortSw_Gbic1000BaseT,
       "hh3cevtPortSw-Gbic1000BaseLx": hh3cevtPortSw_Gbic1000BaseLx,
       "hh3cevtPortSw-Gbic1000BaseSx": hh3cevtPortSw_Gbic1000BaseSx,
       "hh3cevtPortSw-Gbic1000BaseZx": hh3cevtPortSw_Gbic1000BaseZx,
       "hh3cevtPortSw-ComboNoConnector": hh3cevtPortSw_ComboNoConnector,
       "hh3cevtPortSw-Combo1000BaseLx": hh3cevtPortSw_Combo1000BaseLx,
       "hh3cevtPortSw-Combo1000BaseLxFiber": hh3cevtPortSw_Combo1000BaseLxFiber,
       "hh3cevtPortSw-Combo1000BaseLxCopper": hh3cevtPortSw_Combo1000BaseLxCopper,
       "hh3cevtPortSw-Combo1000BaseSx": hh3cevtPortSw_Combo1000BaseSx,
       "hh3cevtPortSw-Combo1000BaseSxFiber": hh3cevtPortSw_Combo1000BaseSxFiber,
       "hh3cevtPortSw-Combo1000BaseSxCopper": hh3cevtPortSw_Combo1000BaseSxCopper,
       "hh3cevtPortSw-Combo1000BaseZx": hh3cevtPortSw_Combo1000BaseZx,
       "hh3cevtPortSw-Combo1000BaseZxFiber": hh3cevtPortSw_Combo1000BaseZxFiber,
       "hh3cevtPortSw-Combo1000BaseZxCopper": hh3cevtPortSw_Combo1000BaseZxCopper,
       "hh3cevtPortSw-155PosSxMmf": hh3cevtPortSw_155PosSxMmf,
       "hh3cevtPortSw-155PosLxSmf": hh3cevtPortSw_155PosLxSmf,
       "hh3cevtPortSw-1000BASE-T": hh3cevtPortSw_1000BASE_T,
       "hh3cevtPortSw-1000BASE-SX-SFP": hh3cevtPortSw_1000BASE_SX_SFP,
       "hh3cevtPortSw-1000BASE-LX-SFP": hh3cevtPortSw_1000BASE_LX_SFP,
       "hh3cevtPortSw-1000BASE-T-AN-SFP": hh3cevtPortSw_1000BASE_T_AN_SFP,
       "hh3cevtPortSw-10GBASE-LX4-XENPAK": hh3cevtPortSw_10GBASE_LX4_XENPAK,
       "hh3cevtPortSw-10GBASE-LR-XENPAK": hh3cevtPortSw_10GBASE_LR_XENPAK,
       "hh3cevtPortSw-10GBASE-CX4": hh3cevtPortSw_10GBASE_CX4,
       "hh3cevtPortSw-1000BASE-ZX-SFP": hh3cevtPortSw_1000BASE_ZX_SFP,
       "hh3cevtPortSw-1000BASE-MM-SFP": hh3cevtPortSw_1000BASE_MM_SFP,
       "hh3cevtPortSw-100BASE-SX-SFP": hh3cevtPortSw_100BASE_SX_SFP,
       "hh3cevtPortSw-100BASE-LX-SFP": hh3cevtPortSw_100BASE_LX_SFP,
       "hh3cevtPortSw-100BASE-T-AN-SFP": hh3cevtPortSw_100BASE_T_AN_SFP,
       "hh3cevtPortSw-100BASE-ZX-SFP": hh3cevtPortSw_100BASE_ZX_SFP,
       "hh3cevtPortSw-100BASE-MM-SFP": hh3cevtPortSw_100BASE_MM_SFP,
       "hh3cevtPortSw-SFP-NO-CONNECTOR": hh3cevtPortSw_SFP_NO_CONNECTOR,
       "hh3cevtPortSw-SFP-UNKNOWN-CONNECTOR": hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR,
       "hh3cevtPortSw-POS-NO-CONNECTOR": hh3cevtPortSw_POS_NO_CONNECTOR,
       "hh3cevtPortSw-10G-BASE-SR": hh3cevtPortSw_10G_BASE_SR,
       "hh3cevtPortSw-10G-BASE-ER": hh3cevtPortSw_10G_BASE_ER,
       "hh3cevtPortSw-10G-BASE-LX4": hh3cevtPortSw_10G_BASE_LX4,
       "hh3cevtPortSw-10G-BASE-SW": hh3cevtPortSw_10G_BASE_SW,
       "hh3cevtPortSw-10G-BASE-LW": hh3cevtPortSw_10G_BASE_LW,
       "hh3cevtPortSw-10G-BASE-EW": hh3cevtPortSw_10G_BASE_EW,
       "hh3cevtPortSw-10G-LR-SM-LC": hh3cevtPortSw_10G_LR_SM_LC,
       "hh3cevtPortSw-10G-SR-MM-LC": hh3cevtPortSw_10G_SR_MM_LC,
       "hh3cevtPortSw-10G-ER-SM-LC": hh3cevtPortSw_10G_ER_SM_LC,
       "hh3cevtPortSw-10G-LW-SM-LC": hh3cevtPortSw_10G_LW_SM_LC,
       "hh3cevtPortSw-10G-SW-MM-LC": hh3cevtPortSw_10G_SW_MM_LC,
       "hh3cevtPortSw-10G-EW-SM-LC": hh3cevtPortSw_10G_EW_SM_LC,
       "hh3cevtPortSw-100BASE-SM-MTRJ": hh3cevtPortSw_100BASE_SM_MTRJ,
       "hh3cevtPortSw-100BASE-MM-MTRJ": hh3cevtPortSw_100BASE_MM_MTRJ,
       "hh3cevtPortSw-XFP-NO-CONNECTOR": hh3cevtPortSw_XFP_NO_CONNECTOR,
       "hh3cevtPortSw-XFP-10GBASE-SR": hh3cevtPortSw_XFP_10GBASE_SR,
       "hh3cevtPortSw-XFP-10GBASE-LR": hh3cevtPortSw_XFP_10GBASE_LR,
       "hh3cevtPortSw-XFP-10GBASE-ER": hh3cevtPortSw_XFP_10GBASE_ER,
       "hh3cevtPortSw-XFP-10GBASE-SW": hh3cevtPortSw_XFP_10GBASE_SW,
       "hh3cevtPortSw-XFP-10GBASE-LW": hh3cevtPortSw_XFP_10GBASE_LW,
       "hh3cevtPortSw-XFP-10GBASE-EW": hh3cevtPortSw_XFP_10GBASE_EW,
       "hh3cevtPortSw-XFP-10GBASE-CX4": hh3cevtPortSw_XFP_10GBASE_CX4,
       "hh3cevtPortSw-XFP-10GBASE-LX4": hh3cevtPortSw_XFP_10GBASE_LX4,
       "hh3cevtPortSw-XFP-UNKNOWN": hh3cevtPortSw_XFP_UNKNOWN,
       "hh3cevtPortSw-XPK-NOCONNECTOR": hh3cevtPortSw_XPK_NOCONNECTOR,
       "hh3cevtPortSw-XPK-10GBASE-SR": hh3cevtPortSw_XPK_10GBASE_SR,
       "hh3cevtPortSw-XPK-10GBASE-LR": hh3cevtPortSw_XPK_10GBASE_LR,
       "hh3cevtPortSw-XPK-10GBASE-ER": hh3cevtPortSw_XPK_10GBASE_ER,
       "hh3cevtPortSw-XPK-10GBASE-SW": hh3cevtPortSw_XPK_10GBASE_SW,
       "hh3cevtPortSw-XPK-10GBASE-LW": hh3cevtPortSw_XPK_10GBASE_LW,
       "hh3cevtPortSw-XPK-10GBASE-EW": hh3cevtPortSw_XPK_10GBASE_EW,
       "hh3cevtPortSw-XPK-10GBASE-CX4": hh3cevtPortSw_XPK_10GBASE_CX4,
       "hh3cevtPortSw-XPK-10GBASE-LX4": hh3cevtPortSw_XPK_10GBASE_LX4,
       "hh3cevtPortSw-XPK-UNKNOWN": hh3cevtPortSw_XPK_UNKNOWN,
       "hh3cevtPortSw-POS-OC48-SR-SM-LC": hh3cevtPortSw_POS_OC48_SR_SM_LC,
       "hh3cevtPortSw-POS-OC48-IR-SM-LC": hh3cevtPortSw_POS_OC48_IR_SM_LC,
       "hh3cevtPortSw-POS-OC48-LR-SM-LC": hh3cevtPortSw_POS_OC48_LR_SM_LC,
       "hh3cevtPortSw-10G-BASE-CX4": hh3cevtPortSw_10G_BASE_CX4,
       "hh3cevtPortSw-OLT-1000BASE-BX-SFF-SC": hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC,
       "hh3cevtPortSw-ONU-1000BASE-BX-SFF-SC": hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC,
       "hh3cevtPortSw-24G-CASCADE": hh3cevtPortSw_24G_CASCADE,
       "hh3cevtPortSw-POS-OC3-SR-MM": hh3cevtPortSw_POS_OC3_SR_MM,
       "hh3cevtPortSw-POS-OC3-IR-SM": hh3cevtPortSw_POS_OC3_IR_SM,
       "hh3cevtPortSw-POS-OC3-IR-1-SM": hh3cevtPortSw_POS_OC3_IR_1_SM,
       "hh3cevtPortSw-POS-OC3-IR-2-SM": hh3cevtPortSw_POS_OC3_IR_2_SM,
       "hh3cevtPortSw-POS-OC3-LR-SM": hh3cevtPortSw_POS_OC3_LR_SM,
       "hh3cevtPortSw-POS-OC3-LR-1-SM": hh3cevtPortSw_POS_OC3_LR_1_SM,
       "hh3cevtPortSw-POS-OC3-LR-2-SM": hh3cevtPortSw_POS_OC3_LR_2_SM,
       "hh3cevtPortSw-POS-OC3-LR-3-SM": hh3cevtPortSw_POS_OC3_LR_3_SM,
       "hh3cevtPortSw-POS-OC12-SR-MM": hh3cevtPortSw_POS_OC12_SR_MM,
       "hh3cevtPortSw-POS-OC12-IR-SM": hh3cevtPortSw_POS_OC12_IR_SM,
       "hh3cevtPortSw-POS-OC12-IR-1-SM": hh3cevtPortSw_POS_OC12_IR_1_SM,
       "hh3cevtPortSw-POS-OC12-IR-2-SM": hh3cevtPortSw_POS_OC12_IR_2_SM,
       "hh3cevtPortSw-POS-OC12-LR-SM": hh3cevtPortSw_POS_OC12_LR_SM,
       "hh3cevtPortSw-POS-OC12-LR-1-SM": hh3cevtPortSw_POS_OC12_LR_1_SM,
       "hh3cevtPortSw-POS-OC12-LR-2-SM": hh3cevtPortSw_POS_OC12_LR_2_SM,
       "hh3cevtPortSw-POS-OC12-LR-3-SM": hh3cevtPortSw_POS_OC12_LR_3_SM,
       "hh3cevtPortSw-POS-OC48-SR-SM": hh3cevtPortSw_POS_OC48_SR_SM,
       "hh3cevtPortSw-POS-OC48-IR-SM": hh3cevtPortSw_POS_OC48_IR_SM,
       "hh3cevtPortSw-POS-OC48-IR-1-SM": hh3cevtPortSw_POS_OC48_IR_1_SM,
       "hh3cevtPortSw-POS-OC48-IR-2-SM": hh3cevtPortSw_POS_OC48_IR_2_SM,
       "hh3cevtPortSw-POS-OC48-LR-SM": hh3cevtPortSw_POS_OC48_LR_SM,
       "hh3cevtPortSw-POS-OC48-LR-1-SM": hh3cevtPortSw_POS_OC48_LR_1_SM,
       "hh3cevtPortSw-POS-OC48-LR-2-SM": hh3cevtPortSw_POS_OC48_LR_2_SM,
       "hh3cevtPortSw-POS-OC48-LR-3-SM": hh3cevtPortSw_POS_OC48_LR_3_SM,
       "hh3cevtPortSw-POS-I-64-1": hh3cevtPortSw_POS_I_64_1,
       "hh3cevtPortSw-POS-I-64-2": hh3cevtPortSw_POS_I_64_2,
       "hh3cevtPortSw-POS-I-64-3": hh3cevtPortSw_POS_I_64_3,
       "hh3cevtPortSw-POS-I-64-5": hh3cevtPortSw_POS_I_64_5,
       "hh3cevtPortSw-POS-S-64-1": hh3cevtPortSw_POS_S_64_1,
       "hh3cevtPortSw-POS-S-64-2": hh3cevtPortSw_POS_S_64_2,
       "hh3cevtPortSw-POS-S-64-3": hh3cevtPortSw_POS_S_64_3,
       "hh3cevtPortSw-POS-S-64-5": hh3cevtPortSw_POS_S_64_5,
       "hh3cevtPortSw-POS-L-64-1": hh3cevtPortSw_POS_L_64_1,
       "hh3cevtPortSw-POS-L-64-2": hh3cevtPortSw_POS_L_64_2,
       "hh3cevtPortSw-POS-L-64-3": hh3cevtPortSw_POS_L_64_3,
       "hh3cevtPortSw-POS-V-64-2": hh3cevtPortSw_POS_V_64_2,
       "hh3cevtPortSw-POS-V-64-3": hh3cevtPortSw_POS_V_64_3,
       "hh3cevtPortSw-100BASE-FX-BIDI": hh3cevtPortSw_100BASE_FX_BIDI,
       "hh3cevtPortSw-100BASE-BX10-U-SFP": hh3cevtPortSw_100BASE_BX10_U_SFP,
       "hh3cevtPortSw-100BASE-BX10-D-SFP": hh3cevtPortSw_100BASE_BX10_D_SFP,
       "hh3cevtPortSw-1000BASE-BX10-U-SFP": hh3cevtPortSw_1000BASE_BX10_U_SFP,
       "hh3cevtPortSw-1000BASE-BX10-D-SFP": hh3cevtPortSw_1000BASE_BX10_D_SFP,
       "hh3cevtPortSw-STK-1000BASE-T": hh3cevtPortSw_STK_1000BASE_T,
       "hh3cevtPortSw-RPR-PHYPOS-CONNECTOR": hh3cevtPortSw_RPR_PHYPOS_CONNECTOR,
       "hh3cevtPortSw-RPR-PHY10GE-CONNECTOR": hh3cevtPortSw_RPR_PHY10GE_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGICPOS-CONNECTOR": hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGIC10GE-CONNECTOR": hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR,
       "hh3cevtPortSw-10GBASE-ZR": hh3cevtPortSw_10GBASE_ZR,
       "hh3cevtPortSw-TYPE-ERROR-CONNECTOR": hh3cevtPortSw_TYPE_ERROR_CONNECTOR,
       "hh3cevtPortSw-10G-STACK": hh3cevtPortSw_10G_STACK,
       "hh3cevtPortSw-155-ATM-SX-MMF": hh3cevtPortSw_155_ATM_SX_MMF,
       "hh3cevtPortSw-155-ATM-LX-SMF": hh3cevtPortSw_155_ATM_LX_SMF,
       "hh3cevtPortSw-622-ATM-SX-MMF": hh3cevtPortSw_622_ATM_SX_MMF,
       "hh3cevtPortSw-622-ATM-LX-SMF": hh3cevtPortSw_622_ATM_LX_SMF,
       "hh3cevtPortSw-155-ATM-NO-CONNECTOR": hh3cevtPortSw_155_ATM_NO_CONNECTOR,
       "hh3cevtPortSw-622-ATM-NO-CONNECTOR": hh3cevtPortSw_622_ATM_NO_CONNECTOR,
       "hh3cevtPortSw-155-CPOS-E1-NO-CONNECTOR": hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR,
       "hh3cevtPortSw-155-CPOS-T1-NO-CONNECTOR": hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR,
       "hh3cevtPortSw-622-CPOS-E1-NO-CONNECTOR": hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR,
       "hh3cevtPortSw-622-CPOS-T1-NO-CONNECTOR": hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR,
       "hh3cevtPortSw-155-CPOS-E1-SX-MMF": hh3cevtPortSw_155_CPOS_E1_SX_MMF,
       "hh3cevtPortSw-155-CPOS-T1-SX-MMF": hh3cevtPortSw_155_CPOS_T1_SX_MMF,
       "hh3cevtPortSw-155-CPOS-E1-LX-SMF": hh3cevtPortSw_155_CPOS_E1_LX_SMF,
       "hh3cevtPortSw-155-CPOS-T1-LX-SMF": hh3cevtPortSw_155_CPOS_T1_LX_SMF,
       "hh3cevtPortSw-622-CPOS-E1-SX-MMF": hh3cevtPortSw_622_CPOS_E1_SX_MMF,
       "hh3cevtPortSw-622-CPOS-T1-SX-MMF": hh3cevtPortSw_622_CPOS_T1_SX_MMF,
       "hh3cevtPortSw-622-CPOS-E1-LX-SMF": hh3cevtPortSw_622_CPOS_E1_LX_SMF,
       "hh3cevtPortSw-622-CPOS-T1-LX-SMF": hh3cevtPortSw_622_CPOS_T1_LX_SMF,
       "hh3cevtPortSw-E1-CONNECTOR": hh3cevtPortSw_E1_CONNECTOR,
       "hh3cevtPortSw-T1-CONNECTOR": hh3cevtPortSw_T1_CONNECTOR,
       "hh3cevtPortSw-1000BASE-STK-SFP": hh3cevtPortSw_1000BASE_STK_SFP,
       "hh3cevtPortSw-1000BASE-BIDI-SFP": hh3cevtPortSw_1000BASE_BIDI_SFP,
       "hh3cevtPortSw-1000BASE-CWDM-SFP": hh3cevtPortSw_1000BASE_CWDM_SFP,
       "hh3cevtPortSw-100BASE-BIDI-SFP": hh3cevtPortSw_100BASE_BIDI_SFP,
       "hh3cevtPortSw-OLT-1000BASE-PX-SFP": hh3cevtPortSw_OLT_1000BASE_PX_SFP,
       "hh3cevtPortSw-OLT-1000BASE-NO-CONNECTOR": hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR,
       "hh3cevtPortSw-RPR-PHYGE-CONNECTOR": hh3cevtPortSw_RPR_PHYGE_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGICGE-CONNECTOR": hh3cevtPortSw_RPR_LOGICGE_CONNECTOR,
       "hh3cevtPortSw-100M-1550-BIDI": hh3cevtPortSw_100M_1550_BIDI,
       "hh3cevtPortSw-100M-1310-BIDI": hh3cevtPortSw_100M_1310_BIDI,
       "hh3cevtPortSw-RPR-PHYOC48-CONNECTOR": hh3cevtPortSw_RPR_PHYOC48_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGICOC48-CONNECTOR": hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR,
       "hh3cevtPortSw-100-1000-BASE-LX-SMF": hh3cevtPortSw_100_1000_BASE_LX_SMF,
       "hh3cevtPortSw-10G-ZW-SM-LC": hh3cevtPortSw_10G_ZW_SM_LC,
       "hh3cevtPortSw-10G-ZR-SM-LC": hh3cevtPortSw_10G_ZR_SM_LC,
       "hh3cevtPortSw-XPK-10GBASE-ZR": hh3cevtPortSw_XPK_10GBASE_ZR,
       "hh3cevtPortSw-SGMII-100-BASE-LX-SFP": hh3cevtPortSw_SGMII_100_BASE_LX_SFP,
       "hh3cevtPortSw-SGMII-100-BASE-FX-SFP": hh3cevtPortSw_SGMII_100_BASE_FX_SFP,
       "hh3cevtPortSw-WLAN-RADIO": hh3cevtPortSw_WLAN_RADIO,
       "hh3cevtPortSw-CABLE": hh3cevtPortSw_CABLE,
       "hh3cevtPortSw-SFP-PLUS-NO-CONNECTOR": hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-SR": hh3cevtPortSw_SFP_PLUS_10GBASE_SR,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-LR": hh3cevtPortSw_SFP_PLUS_10GBASE_LR,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-LRM": hh3cevtPortSw_SFP_PLUS_10GBASE_LRM,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-Cu": hh3cevtPortSw_SFP_PLUS_10GBASE_Cu,
       "hh3cevtPortSw-SFP-PLUS-UNKNOWN": hh3cevtPortSw_SFP_PLUS_UNKNOWN,
       "hh3cevtPortSw-SFP-PLUS-STACK-CONNECTOR": hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR,
       "hh3cevtPortSw-POS-L-64-4": hh3cevtPortSw_POS_L_64_4,
       "hh3cevtPortSw-MINISAS-HD-STACK-CONNECTOR": hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR,
       "hh3cevtPortSw-ONU-1000BASE-PX-SFF": hh3cevtPortSw_ONU_1000BASE_PX_SFF,
       "hh3cevtPortSw-RS485": hh3cevtPortSw_RS485,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-ER": hh3cevtPortSw_SFP_PLUS_10GBASE_ER,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-ZR": hh3cevtPortSw_SFP_PLUS_10GBASE_ZR,
       "hh3cevtPortSw-XFP-10GBASE-ZR": hh3cevtPortSw_XFP_10GBASE_ZR,
       "hh3cevtStack": hh3cevtStack}
)
