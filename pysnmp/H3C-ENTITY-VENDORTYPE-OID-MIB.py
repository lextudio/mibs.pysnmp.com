# SNMP MIB module (H3C-ENTITY-VENDORTYPE-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-ENTITY-VENDORTYPE-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:25 2024
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

(h3c,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3c")

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

h3cEntityVendorTypeOID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEntityVendortypeObjects_ObjectIdentity = ObjectIdentity
h3cEntityVendortypeObjects = _H3cEntityVendortypeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1)
)
_H3cevtOther_ObjectIdentity = ObjectIdentity
h3cevtOther = _H3cevtOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1)
)
_H3cevtOtherUnknownCard_ObjectIdentity = ObjectIdentity
h3cevtOtherUnknownCard = _H3cevtOtherUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1, 1)
)
_H3cevtCPU_ObjectIdentity = ObjectIdentity
h3cevtCPU = _H3cevtCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1, 2)
)
_H3cevtGeneralCPU_ObjectIdentity = ObjectIdentity
h3cevtGeneralCPU = _H3cevtGeneralCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1, 2, 1)
)
_H3cevtDOM_ObjectIdentity = ObjectIdentity
h3cevtDOM = _H3cevtDOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1, 3)
)
_H3cevtCFCard_ObjectIdentity = ObjectIdentity
h3cevtCFCard = _H3cevtCFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1, 4)
)
_H3cevtHardDisk_ObjectIdentity = ObjectIdentity
h3cevtHardDisk = _H3cevtHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 1, 5)
)
_H3cevtUnknown_ObjectIdentity = ObjectIdentity
h3cevtUnknown = _H3cevtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 2)
)
_H3cevtChassis_ObjectIdentity = ObjectIdentity
h3cevtChassis = _H3cevtChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 3)
)
_H3cevtBackplane_ObjectIdentity = ObjectIdentity
h3cevtBackplane = _H3cevtBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 4)
)
_H3cevtContainer_ObjectIdentity = ObjectIdentity
h3cevtContainer = _H3cevtContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 5)
)
_H3cevtPowerSupply_ObjectIdentity = ObjectIdentity
h3cevtPowerSupply = _H3cevtPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6)
)
_H3cevtPowerSupplyAC_ObjectIdentity = ObjectIdentity
h3cevtPowerSupplyAC = _H3cevtPowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6, 2)
)
_H3cevtPowerSupplyDC_ObjectIdentity = ObjectIdentity
h3cevtPowerSupplyDC = _H3cevtPowerSupplyDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6, 3)
)
_H3cevtPowerSupplySTD130W_ObjectIdentity = ObjectIdentity
h3cevtPowerSupplySTD130W = _H3cevtPowerSupplySTD130W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6, 4)
)
_H3cevtPowerSupplySTD180W_ObjectIdentity = ObjectIdentity
h3cevtPowerSupplySTD180W = _H3cevtPowerSupplySTD180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6, 5)
)
_H3cevtPowerSupplyPOE24Port_ObjectIdentity = ObjectIdentity
h3cevtPowerSupplyPOE24Port = _H3cevtPowerSupplyPOE24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6, 6)
)
_H3cevtPowerSupplyPOE48Port_ObjectIdentity = ObjectIdentity
h3cevtPowerSupplyPOE48Port = _H3cevtPowerSupplyPOE48Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 6, 7)
)
_H3cevtFan_ObjectIdentity = ObjectIdentity
h3cevtFan = _H3cevtFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 7)
)
_H3cevtHotSwapFan_ObjectIdentity = ObjectIdentity
h3cevtHotSwapFan = _H3cevtHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 7, 1)
)
_H3cevtNonHotSwapFan_ObjectIdentity = ObjectIdentity
h3cevtNonHotSwapFan = _H3cevtNonHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 7, 2)
)
_H3cevtSensor_ObjectIdentity = ObjectIdentity
h3cevtSensor = _H3cevtSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 8)
)
_H3cevtSensorTemperature_ObjectIdentity = ObjectIdentity
h3cevtSensorTemperature = _H3cevtSensorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 8, 1)
)
_H3cevtSensorVoltage_ObjectIdentity = ObjectIdentity
h3cevtSensorVoltage = _H3cevtSensorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 8, 2)
)
_H3cevtSensorFanSpeed_ObjectIdentity = ObjectIdentity
h3cevtSensorFanSpeed = _H3cevtSensorFanSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 8, 3)
)
_H3cevtModule_ObjectIdentity = ObjectIdentity
h3cevtModule = _H3cevtModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9)
)
_H3cevtModuleUnknownCard_ObjectIdentity = ObjectIdentity
h3cevtModuleUnknownCard = _H3cevtModuleUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 1)
)
_H3cevtModuleCommonCards_ObjectIdentity = ObjectIdentity
h3cevtModuleCommonCards = _H3cevtModuleCommonCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 2)
)
_H3cevtModuleRouterType_ObjectIdentity = ObjectIdentity
h3cevtModuleRouterType = _H3cevtModuleRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3)
)
_H3cevtModuleRt_As_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_As = _H3cevtModuleRt_As_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 2)
)
_H3cevtModuleRt_Sa_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sa = _H3cevtModuleRt_Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 3)
)
_H3cevtModuleRt_Bi_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Bi = _H3cevtModuleRt_Bi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 4)
)
_H3cevtModuleRt_E12_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E12 = _H3cevtModuleRt_E12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5)
)
_H3cevtModuleRt_E14_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E14 = _H3cevtModuleRt_E14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 6)
)
_H3cevtModuleRt_Fe1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fe1 = _H3cevtModuleRt_Fe1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 7)
)
_H3cevtModuleRt_E1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E1 = _H3cevtModuleRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 8)
)
_H3cevtModuleRt_Fe2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fe2 = _H3cevtModuleRt_Fe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 9)
)
_H3cevtModuleRt_Vi2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Vi2 = _H3cevtModuleRt_Vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 11)
)
_H3cevtModuleRt_Vi4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Vi4 = _H3cevtModuleRt_Vi4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 12)
)
_H3cevtModuleRt_Vi30_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Vi30 = _H3cevtModuleRt_Vi30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 13)
)
_H3cevtModuleRt_S1b_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_S1b = _H3cevtModuleRt_S1b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 14)
)
_H3cevtModuleRt_Sa2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sa2 = _H3cevtModuleRt_Sa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 15)
)
_H3cevtModuleRt_As16_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_As16 = _H3cevtModuleRt_As16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 16)
)
_H3cevtModuleRt_New8as_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_New8as = _H3cevtModuleRt_New8as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 17)
)
_H3cevtModuleRt_Sa1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sa1 = _H3cevtModuleRt_Sa1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 18)
)
_H3cevtModuleRt_Fxs2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fxs2 = _H3cevtModuleRt_Fxs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 19)
)
_H3cevtModuleRt_Fxo2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fxo2 = _H3cevtModuleRt_Fxo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 20)
)
_H3cevtModuleRt_Em2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Em2 = _H3cevtModuleRt_Em2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 21)
)
_H3cevtModuleRt_Fxs4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fxs4 = _H3cevtModuleRt_Fxs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 22)
)
_H3cevtModuleRt_Fxo4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fxo4 = _H3cevtModuleRt_Fxo4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 23)
)
_H3cevtModuleRt_Em4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Em4 = _H3cevtModuleRt_Em4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 24)
)
_H3cevtModuleRt_Sab_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sab = _H3cevtModuleRt_Sab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 25)
)
_H3cevtModuleRt_E1vi_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E1vi = _H3cevtModuleRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 26)
)
_H3cevtModuleRt_Am12_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Am12 = _H3cevtModuleRt_Am12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 27)
)
_H3cevtModuleRt_Am6_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Am6 = _H3cevtModuleRt_Am6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 28)
)
_H3cevtModuleRt_Ndec_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ndec = _H3cevtModuleRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 29)
)
_H3cevtModuleRt_Newsa2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Newsa2 = _H3cevtModuleRt_Newsa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 30)
)
_H3cevtModuleRt_Aux_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Aux = _H3cevtModuleRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 31)
)
_H3cevtModuleRt_Console_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Console = _H3cevtModuleRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 32)
)
_H3cevtModuleRt_Sic_wan_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_wan = _H3cevtModuleRt_Sic_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 33)
)
_H3cevtModuleRt_Sic_1fe_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1fe = _H3cevtModuleRt_Sic_1fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 34)
)
_H3cevtModuleRt_Sic_1sa_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1sa = _H3cevtModuleRt_Sic_1sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 35)
)
_H3cevtModuleRt_Sic_3as_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_3as = _H3cevtModuleRt_Sic_3as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 36)
)
_H3cevtModuleRt_Sic_1e1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1e1 = _H3cevtModuleRt_Sic_1e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 37)
)
_H3cevtModuleRt_Sic_1t1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1t1 = _H3cevtModuleRt_Sic_1t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 38)
)
_H3cevtModuleRt_Sic_1bu_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1bu = _H3cevtModuleRt_Sic_1bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 39)
)
_H3cevtModuleRt_Sic_2bu_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_2bu = _H3cevtModuleRt_Sic_2bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 40)
)
_H3cevtModuleRt_Sic_1bs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1bs = _H3cevtModuleRt_Sic_1bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 41)
)
_H3cevtModuleRt_Sic_2bs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_2bs = _H3cevtModuleRt_Sic_2bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 42)
)
_H3cevtModuleRt_Sic_1am_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1am = _H3cevtModuleRt_Sic_1am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 43)
)
_H3cevtModuleRt_Sic_2am_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_2am = _H3cevtModuleRt_Sic_2am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 44)
)
_H3cevtModuleRt_Sic_1em_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1em = _H3cevtModuleRt_Sic_1em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 45)
)
_H3cevtModuleRt_Sic_2em_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_2em = _H3cevtModuleRt_Sic_2em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 46)
)
_H3cevtModuleRt_Sic_1fxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1fxs = _H3cevtModuleRt_Sic_1fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 47)
)
_H3cevtModuleRt_Sic_2fxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_2fxs = _H3cevtModuleRt_Sic_2fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 48)
)
_H3cevtModuleRt_Sic_1fxo_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_1fxo = _H3cevtModuleRt_Sic_1fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 49)
)
_H3cevtModuleRt_Sic_2fxo_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic_2fxo = _H3cevtModuleRt_Sic_2fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 50)
)
_H3cevtModuleRt_Fcm6_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fcm6 = _H3cevtModuleRt_Fcm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 51)
)
_H3cevtModuleRt_Sa8_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sa8 = _H3cevtModuleRt_Sa8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 52)
)
_H3cevtModuleRt_T11_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T11 = _H3cevtModuleRt_T11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 53)
)
_H3cevtModuleRt_T12_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T12 = _H3cevtModuleRt_T12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 54)
)
_H3cevtModuleRt_T14_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T14 = _H3cevtModuleRt_T14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 55)
)
_H3cevtModuleRt_T1vi_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T1vi = _H3cevtModuleRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 56)
)
_H3cevtModuleRt_Fcm4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fcm4 = _H3cevtModuleRt_Fcm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 57)
)
_H3cevtModuleRt_Fcm2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fcm2 = _H3cevtModuleRt_Fcm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 58)
)
_H3cevtModuleRt_Rtb21ce3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Rtb21ce3 = _H3cevtModuleRt_Rtb21ce3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 59)
)
_H3cevtModuleRt_Ame6_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ame6 = _H3cevtModuleRt_Ame6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 60)
)
_H3cevtModuleRt_Ame12_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ame12 = _H3cevtModuleRt_Ame12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 61)
)
_H3cevtModuleRt_E11_f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E11_f = _H3cevtModuleRt_E11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 65)
)
_H3cevtModuleRt_E12_f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E12_f = _H3cevtModuleRt_E12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 66)
)
_H3cevtModuleRt_E14_f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E14_f = _H3cevtModuleRt_E14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 67)
)
_H3cevtModuleRt_T11_f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T11_f = _H3cevtModuleRt_T11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 68)
)
_H3cevtModuleRt_T12_f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T12_f = _H3cevtModuleRt_T12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 69)
)
_H3cevtModuleRt_T14_f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T14_f = _H3cevtModuleRt_T14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 70)
)
_H3cevtModuleRt_E11_f_17_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_E11_f_17 = _H3cevtModuleRt_E11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 71)
)
_H3cevtModuleRt_T11_f_17_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T11_f_17 = _H3cevtModuleRt_T11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 72)
)
_H3cevtModuleRt_Rtb21ct3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Rtb21ct3 = _H3cevtModuleRt_Rtb21ct3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 73)
)
_H3cevtModuleRt_Atmadsl1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atmadsl1 = _H3cevtModuleRt_Atmadsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 74)
)
_H3cevtModuleRt_Atmadsl2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atmadsl2 = _H3cevtModuleRt_Atmadsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 75)
)
_H3cevtModuleRt_Atm155m_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atm155m = _H3cevtModuleRt_Atm155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 76)
)
_H3cevtModuleRt_Ase8_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ase8 = _H3cevtModuleRt_Ase8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 77)
)
_H3cevtModuleRt_Ase16_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ase16 = _H3cevtModuleRt_Ase16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 78)
)
_H3cevtModuleRt_Sae4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sae4 = _H3cevtModuleRt_Sae4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 79)
)
_H3cevtModuleRt_Sae2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sae2 = _H3cevtModuleRt_Sae2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 80)
)
_H3cevtModuleRt_Atmshdsl1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atmshdsl1 = _H3cevtModuleRt_Atmshdsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 90)
)
_H3cevtModuleRt_Atmshdsl2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atmshdsl2 = _H3cevtModuleRt_Atmshdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 91)
)
_H3cevtModuleRt_Atmshdsl4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atmshdsl4 = _H3cevtModuleRt_Atmshdsl4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 92)
)
_H3cevtModuleRt_Atm25m_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atm25m = _H3cevtModuleRt_Atm25m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 93)
)
_H3cevtModuleRt_Atme3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atme3 = _H3cevtModuleRt_Atme3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 94)
)
_H3cevtModuleRt_Atmt3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atmt3 = _H3cevtModuleRt_Atmt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 95)
)
_H3cevtModuleRt_Xdsl_fec_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Xdsl_fec = _H3cevtModuleRt_Xdsl_fec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 96)
)
_H3cevtModuleRt_Xdsl_adsl_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Xdsl_adsl = _H3cevtModuleRt_Xdsl_adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 97)
)
_H3cevtModuleRt_Xdsl_gshdsl_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Xdsl_gshdsl = _H3cevtModuleRt_Xdsl_gshdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 98)
)
_H3cevtModuleRt_Xdsl_bri_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Xdsl_bri = _H3cevtModuleRt_Xdsl_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 99)
)
_H3cevtModuleRt_Xdsl_scc_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Xdsl_scc = _H3cevtModuleRt_Xdsl_scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 100)
)
_H3cevtModuleRt_Ge1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ge1 = _H3cevtModuleRt_Ge1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 101)
)
_H3cevtModuleRt_Pos155m_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Pos155m = _H3cevtModuleRt_Pos155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 102)
)
_H3cevtModuleRt_Cpos_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Cpos = _H3cevtModuleRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 103)
)
_H3cevtModuleRt_Fe1op_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fe1op = _H3cevtModuleRt_Fe1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 104)
)
_H3cevtModuleRt_Sae8_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sae8 = _H3cevtModuleRt_Sae8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 105)
)
_H3cevtModuleRt_Atm155m_mm_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atm155m_mm = _H3cevtModuleRt_Atm155m_mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 106)
)
_H3cevtModuleRt_Atm155m_sm_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atm155m_sm = _H3cevtModuleRt_Atm155m_sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 107)
)
_H3cevtModuleRt_Atm155m_sml_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Atm155m_sml = _H3cevtModuleRt_Atm155m_sml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 108)
)
_H3cevtModuleRt_Fe1op_sfx_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fe1op_sfx = _H3cevtModuleRt_Fe1op_sfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 109)
)
_H3cevtModuleRt_Fe1op_mfx_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fe1op_mfx = _H3cevtModuleRt_Fe1op_mfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 110)
)
_H3cevtModuleRt_Cpos_t1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Cpos_t1 = _H3cevtModuleRt_Cpos_t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 111)
)
_H3cevtModuleRt_Ge1op_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ge1op = _H3cevtModuleRt_Ge1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 112)
)
_H3cevtModuleRt_Ge2op_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ge2op = _H3cevtModuleRt_Ge2op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 113)
)
_H3cevtModuleRt_Ge2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Ge2 = _H3cevtModuleRt_Ge2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 114)
)
_H3cevtModuleRt_Fix_1wan_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fix_1wan = _H3cevtModuleRt_Fix_1wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 115)
)
_H3cevtModuleRt_Fix_1sae_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fix_1sae = _H3cevtModuleRt_Fix_1sae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 116)
)
_H3cevtModuleRt_Cavium_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Cavium = _H3cevtModuleRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 117)
)
_H3cevtModuleRt_Sic1Eth_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Sic1Eth = _H3cevtModuleRt_Sic1Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 118)
)
_H3cevtModuleRt_atm1ADSLI_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_atm1ADSLI = _H3cevtModuleRt_atm1ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 119)
)
_H3cevtModuleRt_atm2ADSLI_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_atm2ADSLI = _H3cevtModuleRt_atm2ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 120)
)
_H3cevtModuleRt_fix_e11_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_fix_e11 = _H3cevtModuleRt_fix_e11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 121)
)
_H3cevtModuleRt_fix_t11_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_fix_t11 = _H3cevtModuleRt_fix_t11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 122)
)
_H3cevtModuleRt_e18_75_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_e18_75 = _H3cevtModuleRt_e18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 123)
)
_H3cevtModuleRt_e18_120_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_e18_120 = _H3cevtModuleRt_e18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 124)
)
_H3cevtModuleRt_t18_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_t18 = _H3cevtModuleRt_t18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 125)
)
_H3cevtModuleRt_sic_1vifxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_1vifxs = _H3cevtModuleRt_sic_1vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 126)
)
_H3cevtModuleRt_sic_1vifxo_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_1vifxo = _H3cevtModuleRt_sic_1vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 127)
)
_H3cevtModuleRt_sic_2vifxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_2vifxs = _H3cevtModuleRt_sic_2vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 128)
)
_H3cevtModuleRt_sic_2vifxo_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_2vifxo = _H3cevtModuleRt_sic_2vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 129)
)
_H3cevtModuleRt_xdsl_fec_new_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_xdsl_fec_new = _H3cevtModuleRt_xdsl_fec_new_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 130)
)
_H3cevtModuleRt_xdsl_sa_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_xdsl_sa = _H3cevtModuleRt_xdsl_sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 131)
)
_H3cevtModuleRt_bs4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_bs4 = _H3cevtModuleRt_bs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 132)
)
_H3cevtModuleRt_ima_8e175_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ima_8e175 = _H3cevtModuleRt_ima_8e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 133)
)
_H3cevtModuleRt_ima_8e1120_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ima_8e1120 = _H3cevtModuleRt_ima_8e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 134)
)
_H3cevtModuleRt_ima_4e175_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ima_4e175 = _H3cevtModuleRt_ima_4e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 135)
)
_H3cevtModuleRt_ima_4e1120_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ima_4e1120 = _H3cevtModuleRt_ima_4e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 136)
)
_H3cevtModuleRt_ima_8t1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ima_8t1 = _H3cevtModuleRt_ima_8t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 137)
)
_H3cevtModuleRt_ima_4t1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ima_4t1 = _H3cevtModuleRt_ima_4t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 138)
)
_H3cevtModuleRt_sic_1t1f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_1t1f = _H3cevtModuleRt_sic_1t1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 139)
)
_H3cevtModuleRt_sic_1e1f_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_1e1f = _H3cevtModuleRt_sic_1e1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 140)
)
_H3cevtModuleRt_VG_16fxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_16fxs = _H3cevtModuleRt_VG_16fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 141)
)
_H3cevtModuleRt_VG_32fxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_32fxs = _H3cevtModuleRt_VG_32fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 142)
)
_H3cevtModuleRt_VG_8fxo_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_8fxo = _H3cevtModuleRt_VG_8fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 143)
)
_H3cevtModuleRt_VG_2fe_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_2fe = _H3cevtModuleRt_VG_2fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 144)
)
_H3cevtModuleRt_sib_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sib = _H3cevtModuleRt_sib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 145)
)
_H3cevtModuleRt_cie32_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_cie32 = _H3cevtModuleRt_cie32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 146)
)
_H3cevtModuleRt_cie64_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_cie64 = _H3cevtModuleRt_cie64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 147)
)
_H3cevtModuleRt_cie96_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_cie96 = _H3cevtModuleRt_cie96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 148)
)
_H3cevtModuleRt_Fe4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_Fe4 = _H3cevtModuleRt_Fe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 149)
)
_H3cevtModuleRt_fxs4fxo1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_fxs4fxo1 = _H3cevtModuleRt_fxs4fxo1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 150)
)
_H3cevtModuleRt_atm1shdsl4wire_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_atm1shdsl4wire = _H3cevtModuleRt_atm1shdsl4wire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 151)
)
_H3cevtModuleRt_atmIma4shdsl_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_atmIma4shdsl = _H3cevtModuleRt_atmIma4shdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 152)
)
_H3cevtModuleRt_ls4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ls4 = _H3cevtModuleRt_ls4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 153)
)
_H3cevtModuleRt_ls8_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ls8 = _H3cevtModuleRt_ls8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 154)
)
_H3cevtModuleRt_ls16_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ls16 = _H3cevtModuleRt_ls16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 155)
)
_H3cevtModuleRt_sic_adls2plus_isdn_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_adls2plus_isdn = _H3cevtModuleRt_sic_adls2plus_isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 156)
)
_H3cevtModuleRt_sic_adls2plus_pots_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sic_adls2plus_pots = _H3cevtModuleRt_sic_adls2plus_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 157)
)
_H3cevtModuleRt_ft3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ft3 = _H3cevtModuleRt_ft3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 158)
)
_H3cevtModuleRt_ce32_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ce32 = _H3cevtModuleRt_ce32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 159)
)
_H3cevtModuleRt_bsv2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_bsv2 = _H3cevtModuleRt_bsv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 160)
)
_H3cevtModuleRt_bsv4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_bsv4 = _H3cevtModuleRt_bsv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 161)
)
_H3cevtModuleRt_RPU_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_RPU = _H3cevtModuleRt_RPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 162)
)
_H3cevtModuleRt_ERPU_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ERPU = _H3cevtModuleRt_ERPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 163)
)
_H3cevtModuleRt_SSL_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SSL = _H3cevtModuleRt_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 164)
)
_H3cevtModuleRt_NSA_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NSA = _H3cevtModuleRt_NSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 165)
)
_H3cevtModuleRT_SIC_1GEC_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_1GEC = _H3cevtModuleRT_SIC_1GEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 200)
)
_H3cevtModuleRT_24FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_24FSW = _H3cevtModuleRT_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 201)
)
_H3cevtModuleRT_24FSWP_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_24FSWP = _H3cevtModuleRT_24FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 202)
)
_H3cevtModuleRT_16FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_16FSW = _H3cevtModuleRT_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 203)
)
_H3cevtModuleRT_16FSWP_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_16FSWP = _H3cevtModuleRT_16FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 204)
)
_H3cevtModuleRT_1VE1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_1VE1 = _H3cevtModuleRT_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 205)
)
_H3cevtModuleRT_1VT1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_1VT1 = _H3cevtModuleRT_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 206)
)
_H3cevtModuleRT_2VE1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_2VE1 = _H3cevtModuleRT_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 207)
)
_H3cevtModuleRT_2VT1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_2VT1 = _H3cevtModuleRT_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 208)
)
_H3cevtModuleRT_SIC_4FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_4FSW = _H3cevtModuleRT_SIC_4FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 209)
)
_H3cevtModuleRT_SIC_4FSWP_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_4FSWP = _H3cevtModuleRT_SIC_4FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 210)
)
_H3cevtModuleRT_DSIC_9FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_DSIC_9FSW = _H3cevtModuleRT_DSIC_9FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 211)
)
_H3cevtModuleRT_DSIC_9FSWP_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_DSIC_9FSWP = _H3cevtModuleRT_DSIC_9FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 212)
)
_H3cevtModuleRT_SIC_1VE1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_1VE1 = _H3cevtModuleRT_SIC_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 213)
)
_H3cevtModuleRT_SIC_1VT1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_1VT1 = _H3cevtModuleRT_SIC_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 214)
)
_H3cevtModuleRT_VCPM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_VCPM = _H3cevtModuleRT_VCPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 215)
)
_H3cevtModuleRT_VPM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_VPM = _H3cevtModuleRT_VPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 216)
)
_H3cevtModuleRT_VPMA_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_VPMA = _H3cevtModuleRT_VPMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 217)
)
_H3cevtModuleRT_VPMB_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_VPMB = _H3cevtModuleRT_VPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 218)
)
_H3cevtModuleRT_VPMC_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_VPMC = _H3cevtModuleRT_VPMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 219)
)
_H3cevtModuleRt_fe18_75_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_fe18_75 = _H3cevtModuleRt_fe18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 220)
)
_H3cevtModuleRt_fe18_120_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_fe18_120 = _H3cevtModuleRt_fe18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 221)
)
_H3cevtModuleRt_ft18_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ft18 = _H3cevtModuleRt_ft18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 222)
)
_H3cevtModuleRt_CF_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_CF = _H3cevtModuleRt_CF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 223)
)
_H3cevtModuleRt_bsv2_v2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_bsv2_v2 = _H3cevtModuleRt_bsv2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 224)
)
_H3cevtModuleRt_e1vi1_v2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_e1vi1_v2 = _H3cevtModuleRt_e1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 225)
)
_H3cevtModuleRt_e1vi2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_e1vi2 = _H3cevtModuleRt_e1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 226)
)
_H3cevtModuleRt_t1vi1_v2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_t1vi1_v2 = _H3cevtModuleRt_t1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 227)
)
_H3cevtModuleRt_t1vi2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_t1vi2 = _H3cevtModuleRt_t1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 228)
)
_H3cevtModuleRt_osm_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_osm = _H3cevtModuleRt_osm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 229)
)
_H3cevtModuleRt_sd707_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_sd707 = _H3cevtModuleRt_sd707_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 230)
)
_H3cevtModuleRt_dm_epri_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_dm_epri = _H3cevtModuleRt_dm_epri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 231)
)
_H3cevtModuleRt_dm_tpri_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_dm_tpri = _H3cevtModuleRt_dm_tpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 232)
)
_H3cevtModuleRt_ERPU_H_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ERPU_H = _H3cevtModuleRt_ERPU_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 233)
)
_H3cevtModuleRT_SIC_1BSV_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_1BSV = _H3cevtModuleRT_SIC_1BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 234)
)
_H3cevtModuleRT_SIC_2BSV_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_2BSV = _H3cevtModuleRT_SIC_2BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 235)
)
_H3cevtModuleRt_gbe8_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_gbe8 = _H3cevtModuleRt_gbe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 236)
)
_H3cevtModuleRt_gbe4_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_gbe4 = _H3cevtModuleRt_gbe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 237)
)
_H3cevtModuleRt_cpos2_v2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_cpos2_v2 = _H3cevtModuleRt_cpos2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 238)
)
_H3cevtModuleRt_cpos1_v2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_cpos1_v2 = _H3cevtModuleRt_cpos1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 239)
)
_H3cevtModuleRt_oap_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_oap = _H3cevtModuleRt_oap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 240)
)
_H3cevtModuleRT_48FSWP_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_48FSWP = _H3cevtModuleRT_48FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 241)
)
_H3cevtModuleRT_48FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_48FSW = _H3cevtModuleRT_48FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 242)
)
_H3cevtModuleRT_ASM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_ASM = _H3cevtModuleRT_ASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 243)
)
_H3cevtModuleRT_SIC_1FEF_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_1FEF = _H3cevtModuleRT_SIC_1FEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 244)
)
_H3cevtModuleRT_XMIM_24FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_XMIM_24FSW = _H3cevtModuleRT_XMIM_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 245)
)
_H3cevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_WLAN_AG_1RADIO = _H3cevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 246)
)
_H3cevtModuleRT_1CE3_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_1CE3 = _H3cevtModuleRT_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 247)
)
_H3cevtModuleRT_XMIM_16FSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_XMIM_16FSW = _H3cevtModuleRT_XMIM_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 248)
)
_H3cevtModuleRT_OAPS_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAPS = _H3cevtModuleRT_OAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 249)
)
_H3cevtModuleRT_NAM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_NAM = _H3cevtModuleRT_NAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 250)
)
_H3cevtModuleRT_RPE_X1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_RPE_X1 = _H3cevtModuleRT_RPE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 251)
)
_H3cevtModuleRT_FIP_100_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_FIP_100 = _H3cevtModuleRT_FIP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 252)
)
_H3cevtModuleRT_FIP_200_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_FIP_200 = _H3cevtModuleRT_FIP_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 253)
)
_H3cevtModuleRT_SIC_8AS_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_8AS = _H3cevtModuleRT_SIC_8AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 254)
)
_H3cevtModuleRT_WAAM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_WAAM = _H3cevtModuleRT_WAAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 255)
)
_H3cevtModuleRt_msp4p_OC3c_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_msp4p_OC3c = _H3cevtModuleRt_msp4p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 256)
)
_H3cevtModuleRt_1pos_oc48_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_1pos_oc48 = _H3cevtModuleRt_1pos_oc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 257)
)
_H3cevtModuleRt_xgbe_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_xgbe = _H3cevtModuleRt_xgbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 258)
)
_H3cevtModuleRT_EADM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_EADM = _H3cevtModuleRT_EADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 259)
)
_H3cevtModuleRT_VCM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_VCM = _H3cevtModuleRT_VCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 260)
)
_H3cevtModuleRT_SIC_2FXS1FXO_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_2FXS1FXO = _H3cevtModuleRT_SIC_2FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 261)
)
_H3cevtModuleRT_8FXS8FXO_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_8FXS8FXO = _H3cevtModuleRT_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 262)
)
_H3cevtModuleRT_16FXS_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_16FXS = _H3cevtModuleRT_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 263)
)
_H3cevtModuleRT_OAPS_ICM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAPS_ICM = _H3cevtModuleRT_OAPS_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 264)
)
_H3cevtModuleRT_OAP_ICM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAP_ICM = _H3cevtModuleRT_OAP_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 265)
)
_H3cevtModuleRT_8fe_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_8fe = _H3cevtModuleRT_8fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 266)
)
_H3cevtModuleRT_4gbp_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_4gbp = _H3cevtModuleRT_4gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 267)
)
_H3cevtModuleRT_MPU_G2_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_MPU_G2 = _H3cevtModuleRT_MPU_G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 268)
)
_H3cevtModuleRT_OAPS_OCE_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAPS_OCE = _H3cevtModuleRT_OAPS_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 269)
)
_H3cevtModuleRT_OAP_OCE_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAP_OCE = _H3cevtModuleRT_OAP_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 270)
)
_H3cevtModuleRT_OAPS_ICE_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAPS_ICE = _H3cevtModuleRT_OAPS_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 271)
)
_H3cevtModuleRT_OAP_ICE_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_OAP_ICE = _H3cevtModuleRT_OAP_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 272)
)
_H3cevtModuleRT_SIC_16AS_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_16AS = _H3cevtModuleRT_SIC_16AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 273)
)
_H3cevtModuleRT_SPE_FWM_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SPE_FWM = _H3cevtModuleRT_SPE_FWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 274)
)
_H3cevtModuleRT_cls2p_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_cls2p = _H3cevtModuleRT_cls2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 275)
)
_H3cevtModuleRT_cls1p_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_cls1p = _H3cevtModuleRT_cls1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 276)
)
_H3cevtModuleRT_SIC_2E1_F_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_2E1_F = _H3cevtModuleRT_SIC_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 277)
)
_H3cevtModuleRT_SIC_1E1_F_V2_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_1E1_F_V2 = _H3cevtModuleRT_SIC_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 278)
)
_H3cevtModuleRT_MCU_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_MCU = _H3cevtModuleRT_MCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 279)
)
_H3cevtModuleRT_ACU_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_ACU = _H3cevtModuleRT_ACU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 280)
)
_H3cevtModuleRT_1ATM_OC3_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_1ATM_OC3 = _H3cevtModuleRT_1ATM_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 281)
)
_H3cevtModuleRT_RSE_X1_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_RSE_X1 = _H3cevtModuleRT_RSE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 282)
)
_H3cevtModuleRT_FIP_210_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_FIP_210 = _H3cevtModuleRT_FIP_210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 283)
)
_H3cevtModuleRT_1expa_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_1expa = _H3cevtModuleRT_1expa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 284)
)
_H3cevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_WLAN_SIC_N_1RADIO = _H3cevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 285)
)
_H3cevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_WLAN_SIC_BG_1RADIO = _H3cevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 286)
)
_H3cevtModuleRT_al2p_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_al2p = _H3cevtModuleRT_al2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 287)
)
_H3cevtModuleRT_msp2p_OC3c_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_msp2p_OC3c = _H3cevtModuleRT_msp2p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 288)
)
_H3cevtModuleRT_8gbp_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_8gbp = _H3cevtModuleRT_8gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 289)
)
_H3cevtModuleRT_SIC_EPON_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_EPON = _H3cevtModuleRT_SIC_EPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 290)
)
_H3cevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_SIC_3G_GSM_H3 = _H3cevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 291)
)
_H3cevtModuleRT_msp2p_OC12c_ObjectIdentity = ObjectIdentity
h3cevtModuleRT_msp2p_OC12c = _H3cevtModuleRT_msp2p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 292)
)
_H3cevtModuleRt_msp4p_OC12c_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_msp4p_OC12c = _H3cevtModuleRt_msp4p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 293)
)
_H3cevtModuleRt_al1p_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_al1p = _H3cevtModuleRt_al1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 294)
)
_H3cevtModuleRt_OAP_100_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_OAP_100 = _H3cevtModuleRt_OAP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 295)
)
_H3cevtModuleRt_FIP_110_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIP_110 = _H3cevtModuleRt_FIP_110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 296)
)
_H3cevtModuleRt_OSM_SSM_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_OSM_SSM = _H3cevtModuleRt_OSM_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 297)
)
_H3cevtModuleRt_OAP_SSM_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_OAP_SSM = _H3cevtModuleRt_OAP_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 298)
)
_H3cevtModuleRt_rs2p_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_rs2p = _H3cevtModuleRt_rs2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 299)
)
_H3cevtModuleRt_SAP_48GBE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SAP_48GBE = _H3cevtModuleRt_SAP_48GBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 300)
)
_H3cevtModuleRt_SAP_48GBP_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SAP_48GBP = _H3cevtModuleRt_SAP_48GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 301)
)
_H3cevtModuleRt_SAP_24GBP_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SAP_24GBP = _H3cevtModuleRt_SAP_24GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 302)
)
_H3cevtModuleRt_SPE_SSL_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SPE_SSL = _H3cevtModuleRt_SPE_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 303)
)
_H3cevtModuleRt_SIC_AUDIO_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SIC_AUDIO = _H3cevtModuleRt_SIC_AUDIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 304)
)
_H3cevtModuleRt_FIC_1E1POS_H3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIC_1E1POS_H3 = _H3cevtModuleRt_FIC_1E1POS_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 305)
)
_H3cevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_DSIC_4FXS1FXO = _H3cevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 306)
)
_H3cevtModuleRt_FIC_CPOS_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIC_CPOS = _H3cevtModuleRt_FIC_CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 307)
)
_H3cevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_DSIC_1SHDSL_8W = _H3cevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 308)
)
_H3cevtModuleRt_SIC_3G_TD_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SIC_3G_TD = _H3cevtModuleRt_SIC_3G_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 309)
)
_H3cevtModuleRt_SIC_3G_CDMA_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SIC_3G_CDMA = _H3cevtModuleRt_SIC_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 310)
)
_H3cevtModuleRt_SIC_3G_HSPA_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SIC_3G_HSPA = _H3cevtModuleRt_SIC_3G_HSPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 311)
)
_H3cevtModuleRt_FIC_OAP_V2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIC_OAP_V2 = _H3cevtModuleRt_FIC_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 312)
)
_H3cevtModuleRt_MIM_OAP_V2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MIM_OAP_V2 = _H3cevtModuleRt_MIM_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 313)
)
_H3cevtModuleRt_MIM_OAPS_V2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MIM_OAPS_V2 = _H3cevtModuleRt_MIM_OAPS_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 314)
)
_H3cevtModuleRt_HMIM_1CT3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1CT3 = _H3cevtModuleRt_HMIM_1CT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 315)
)
_H3cevtModuleRt_HMIM_1CE3_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1CE3 = _H3cevtModuleRt_HMIM_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 316)
)
_H3cevtModuleRt_HMIM_1POS_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1POS = _H3cevtModuleRt_HMIM_1POS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 317)
)
_H3cevtModuleRt_HMIM_2SAE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_2SAE = _H3cevtModuleRt_HMIM_2SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 318)
)
_H3cevtModuleRt_HMIM_4SAE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4SAE = _H3cevtModuleRt_HMIM_4SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 319)
)
_H3cevtModuleRt_HMIM_8SAE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8SAE = _H3cevtModuleRt_HMIM_8SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 320)
)
_H3cevtModuleRt_HMIM_8ASE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8ASE = _H3cevtModuleRt_HMIM_8ASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 321)
)
_H3cevtModuleRt_HMIM_16ASE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_16ASE = _H3cevtModuleRt_HMIM_16ASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 322)
)
_H3cevtModuleRt_HMIM_1E1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1E1 = _H3cevtModuleRt_HMIM_1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 323)
)
_H3cevtModuleRt_HMIM_2E1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_2E1 = _H3cevtModuleRt_HMIM_2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 324)
)
_H3cevtModuleRt_HMIM_4E1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4E1 = _H3cevtModuleRt_HMIM_4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 325)
)
_H3cevtModuleRt_HMIM_8E1_75_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8E1_75 = _H3cevtModuleRt_HMIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 326)
)
_H3cevtModuleRt_HMIM_1E1_F_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1E1_F = _H3cevtModuleRt_HMIM_1E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 327)
)
_H3cevtModuleRt_HMIM_2E1_F_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_2E1_F = _H3cevtModuleRt_HMIM_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 328)
)
_H3cevtModuleRt_HMIM_4E1_F_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4E1_F = _H3cevtModuleRt_HMIM_4E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 329)
)
_H3cevtModuleRt_HMIM_8E1_F_75_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8E1_F_75 = _H3cevtModuleRt_HMIM_8E1_F_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 330)
)
_H3cevtModuleRt_HMIM_6AM_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_6AM = _H3cevtModuleRt_HMIM_6AM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 331)
)
_H3cevtModuleRt_HMIM_6FCM_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_6FCM = _H3cevtModuleRt_HMIM_6FCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 332)
)
_H3cevtModuleRt_HMIM_2T1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_2T1 = _H3cevtModuleRt_HMIM_2T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 333)
)
_H3cevtModuleRt_HMIM_4T1_F_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4T1_F = _H3cevtModuleRt_HMIM_4T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 334)
)
_H3cevtModuleRt_HMIM_8T1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8T1 = _H3cevtModuleRt_HMIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 335)
)
_H3cevtModuleRt_HMIM_8T1_F_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8T1_F = _H3cevtModuleRt_HMIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 336)
)
_H3cevtModuleRt_HMIM_1VE1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1VE1 = _H3cevtModuleRt_HMIM_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 337)
)
_H3cevtModuleRt_HMIM_1VT1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_1VT1 = _H3cevtModuleRt_HMIM_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 338)
)
_H3cevtModuleRt_HMIM_2VE1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_2VE1 = _H3cevtModuleRt_HMIM_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 339)
)
_H3cevtModuleRt_HMIM_2VT1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_2VT1 = _H3cevtModuleRt_HMIM_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 340)
)
_H3cevtModuleRt_HMIM_8FXS8FXO_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_8FXS8FXO = _H3cevtModuleRt_HMIM_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 341)
)
_H3cevtModuleRt_HMIM_16FXS_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_16FXS = _H3cevtModuleRt_HMIM_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 342)
)
_H3cevtModuleRt_HMIM_4FXS_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4FXS = _H3cevtModuleRt_HMIM_4FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 343)
)
_H3cevtModuleRt_HMIM_4FXO_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4FXO = _H3cevtModuleRt_HMIM_4FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 344)
)
_H3cevtModuleRt_HMIM_4EM_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4EM = _H3cevtModuleRt_HMIM_4EM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 345)
)
_H3cevtModuleRt_HMIM_4BSV_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_4BSV = _H3cevtModuleRt_HMIM_4BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 346)
)
_H3cevtModuleRt_SIC_CNDE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SIC_CNDE = _H3cevtModuleRt_SIC_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 347)
)
_H3cevtModuleRt_ESM_CNDE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ESM_CNDE = _H3cevtModuleRt_ESM_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 348)
)
_H3cevtModuleRt_ESM_CNDE_M_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ESM_CNDE_M = _H3cevtModuleRt_ESM_CNDE_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 349)
)
_H3cevtModuleRt_SR6602_X1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SR6602_X1 = _H3cevtModuleRt_SR6602_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 350)
)
_H3cevtModuleRt_SR6602_X2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SR6602_X2 = _H3cevtModuleRt_SR6602_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 351)
)
_H3cevtModuleRt_MCP_X1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MCP_X1 = _H3cevtModuleRt_MCP_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 352)
)
_H3cevtModuleRt_MCP_X2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MCP_X2 = _H3cevtModuleRt_MCP_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 353)
)
_H3cevtModuleRt_FIP_10_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIP_10 = _H3cevtModuleRt_FIP_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 354)
)
_H3cevtModuleRt_FIP_20_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIP_20 = _H3cevtModuleRt_FIP_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 355)
)
_H3cevtModuleRt_RSE_X2_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_RSE_X2 = _H3cevtModuleRt_RSE_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 356)
)
_H3cevtModuleRt_FIP_600_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_FIP_600 = _H3cevtModuleRt_FIP_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 357)
)
_H3cevtModuleRt_SAP_4EXP_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SAP_4EXP = _H3cevtModuleRt_SAP_4EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 358)
)
_H3cevtModuleRt_SFE_X1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SFE_X1 = _H3cevtModuleRt_SFE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 359)
)
_H3cevtModuleRt_SFE_A1_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SFE_A1 = _H3cevtModuleRt_SFE_A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 360)
)
_H3cevtModuleRt_HMIM_24GSW_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_24GSW = _H3cevtModuleRt_HMIM_24GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 361)
)
_H3cevtModuleRt_HMIM_24GSWP_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HMIM_24GSWP = _H3cevtModuleRt_HMIM_24GSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 362)
)
_H3cevtModuleRt_MPU100_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MPU100 = _H3cevtModuleRt_MPU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 363)
)
_H3cevtModuleRt_SPU100_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SPU100 = _H3cevtModuleRt_SPU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 364)
)
_H3cevtModuleRt_SPU200_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_SPU200 = _H3cevtModuleRt_SPU200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 365)
)
_H3cevtModuleRt_WLAN_N_1RADIO_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_WLAN_N_1RADIO = _H3cevtModuleRt_WLAN_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 366)
)
_H3cevtModuleRt_3G_CDMA_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_3G_CDMA = _H3cevtModuleRt_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 367)
)
_H3cevtModuleRt_3G_WCDMA_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_3G_WCDMA = _H3cevtModuleRt_3G_WCDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 368)
)
_H3cevtModuleRt_3G_HSPAPLUS_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_3G_HSPAPLUS = _H3cevtModuleRt_3G_HSPAPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 369)
)
_H3cevtModuleRt_VPM_128_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VPM_128 = _H3cevtModuleRt_VPM_128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 370)
)
_H3cevtModuleRt_VPM_256_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VPM_256 = _H3cevtModuleRt_VPM_256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 371)
)
_H3cevtModuleRt_VPM_512_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VPM_512 = _H3cevtModuleRt_VPM_512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 372)
)
_H3cevtModuleRt_IPU_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_IPU = _H3cevtModuleRt_IPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 400)
)
_H3cevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MIM2GEBE_PCIE = _H3cevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 401)
)
_H3cevtModuleRt_HIM12GE_PCIE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HIM12GE_PCIE = _H3cevtModuleRt_HIM12GE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 402)
)
_H3cevtModuleRt_HIM2XGE_PCIE_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_HIM2XGE_PCIE = _H3cevtModuleRt_HIM2XGE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 403)
)
_H3cevtModuleRt_IPU_T1000_M_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_IPU_T1000_M = _H3cevtModuleRt_IPU_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 404)
)
_H3cevtModuleRt_IPU_GX4C_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_IPU_GX4C = _H3cevtModuleRt_IPU_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 405)
)
_H3cevtModuleRt_IPU_GT4C_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_IPU_GT4C = _H3cevtModuleRt_IPU_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 406)
)
_H3cevtModuleRt_RPU_IAG2000_A_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_RPU_IAG2000_A = _H3cevtModuleRt_RPU_IAG2000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 407)
)
_H3cevtModuleRt_RPU_AFD1000_A_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_RPU_AFD1000_A = _H3cevtModuleRt_RPU_AFD1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 408)
)
_H3cevtModuleRt_RPU_F5000_A_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_RPU_F5000_A = _H3cevtModuleRt_RPU_F5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 409)
)
_H3cevtModuleRt_ACG_8800S3_MPU_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_ACG_8800S3_MPU = _H3cevtModuleRt_ACG_8800S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 410)
)
_H3cevtModuleRt_T5000S3_MPU_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_T5000S3_MPU = _H3cevtModuleRt_T5000S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 411)
)
_H3cevtModuleRt_NS21S2MSPB0_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NS21S2MSPB0 = _H3cevtModuleRt_NS21S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 412)
)
_H3cevtModuleRt_NS11S2MSPB0_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NS11S2MSPB0 = _H3cevtModuleRt_NS11S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 413)
)
_H3cevtModuleRt_NSQ1WLAN_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NSQ1WLAN = _H3cevtModuleRt_NSQ1WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 414)
)
_H3cevtModuleRt_NSQ1GP4U0_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NSQ1GP4U0 = _H3cevtModuleRt_NSQ1GP4U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 415)
)
_H3cevtModuleRt_NSQ1GP8C40_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NSQ1GP8C40 = _H3cevtModuleRt_NSQ1GP8C40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 416)
)
_H3cevtModuleRt_NSQ1XS2U0_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_NSQ1XS2U0 = _H3cevtModuleRt_NSQ1XS2U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 417)
)
_H3cevtModuleRt_VG_8fxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_8fxs = _H3cevtModuleRt_VG_8fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 600)
)
_H3cevtModuleRt_VG_24fxs_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_24fxs = _H3cevtModuleRt_VG_24fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 601)
)
_H3cevtModuleRt_VG_24fxs24fxo_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_24fxs24fxo = _H3cevtModuleRt_VG_24fxs24fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 602)
)
_H3cevtModuleRt_VG_MPU_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_VG_MPU = _H3cevtModuleRt_VG_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 603)
)
_H3cevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MIM_VCX_CONNECT_P_3C = _H3cevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 604)
)
_H3cevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MIM_VCX_CONNECT_S_3C = _H3cevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 605)
)
_H3cevtModuleRt_MIM_VCX_3C_ObjectIdentity = ObjectIdentity
h3cevtModuleRt_MIM_VCX_3C = _H3cevtModuleRt_MIM_VCX_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 606)
)
_HpevtModuleRt_SIC_EPRI_ObjectIdentity = ObjectIdentity
hpevtModuleRt_SIC_EPRI = _HpevtModuleRt_SIC_EPRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5000)
)
_HpevtModuleRt_MIM_1E1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_V2 = _HpevtModuleRt_MIM_1E1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5001)
)
_HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_F_V2 = _HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5002)
)
_HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_2E1_F_V2 = _HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5003)
)
_HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_4E1_F_V2 = _HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5004)
)
_HpevtModuleRt_MIM_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75 = _HpevtModuleRt_MIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5005)
)
_HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75_F = _HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5006)
)
_HpevtModuleRt_MIM_8T1_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1 = _HpevtModuleRt_MIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5007)
)
_HpevtModuleRt_MIM_8T1_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1_F = _HpevtModuleRt_MIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5008)
)
_HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_IMA_8E1_75 = _HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5009)
)
_HpevtModuleRt_FIC_2E1_V3_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_2E1_V3 = _HpevtModuleRt_FIC_2E1_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5010)
)
_HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_IMA_8T1_V2 = _HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 3, 5011)
)
_H3cevtModuleSwitchType_ObjectIdentity = ObjectIdentity
h3cevtModuleSwitchType = _H3cevtModuleSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4)
)
_H3cevtModuleSw_10OR100M_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_10OR100M = _H3cevtModuleSw_10OR100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1)
)
_H3cevtModuleSw_1000BASE_LX_SM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_LX_SM = _H3cevtModuleSw_1000BASE_LX_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 2)
)
_H3cevtModuleSw_1000BASE_SX_MM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_SX_MM = _H3cevtModuleSw_1000BASE_SX_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 3)
)
_H3cevtModuleSw_1000BASE_TX_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_TX = _H3cevtModuleSw_1000BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 4)
)
_H3cevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_SINGLEMODE_FX = _H3cevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 5)
)
_H3cevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_MULTIMODE_FX = _H3cevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 6)
)
_H3cevtModuleSw_100M_100BASE_TX_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_100BASE_TX = _H3cevtModuleSw_100M_100BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 7)
)
_H3cevtModuleSw_100M_HUB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_HUB = _H3cevtModuleSw_100M_HUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 8)
)
_H3cevtModuleSw_VDSL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_VDSL = _H3cevtModuleSw_VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 9)
)
_H3cevtModuleSw_STACK_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_STACK = _H3cevtModuleSw_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 10)
)
_H3cevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_ZENITH_FX = _H3cevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 11)
)
_H3cevtModuleSw_1000BASE_LONG_FX_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_LONG_FX = _H3cevtModuleSw_1000BASE_LONG_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 12)
)
_H3cevtModuleSw_ADSL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_ADSL = _H3cevtModuleSw_ADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 13)
)
_H3cevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_4T10OR100_4FX100SM = _H3cevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 14)
)
_H3cevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_4T10OR100_4FX100MM = _H3cevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 15)
)
_H3cevtModuleSw_VSPL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_VSPL = _H3cevtModuleSw_VSPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 16)
)
_H3cevtModuleSw_ASPL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_ASPL = _H3cevtModuleSw_ASPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 17)
)
_H3cevtModuleSw_1000M_SFP_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000M_SFP = _H3cevtModuleSw_1000M_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 18)
)
_H3cevtModuleSw_LS82O2CM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82O2CM = _H3cevtModuleSw_LS82O2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 19)
)
_H3cevtModuleSw_LS82P2CM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82P2CM = _H3cevtModuleSw_LS82P2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 20)
)
_H3cevtModuleSw_LS82O4GM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82O4GM = _H3cevtModuleSw_LS82O4GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 21)
)
_H3cevtModuleSw_LS82GB4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82GB4C = _H3cevtModuleSw_LS82GB4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 22)
)
_H3cevtModuleSw_LS82GT4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82GT4C = _H3cevtModuleSw_LS82GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 23)
)
_H3cevtModuleSw_LS82ST4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82ST4C = _H3cevtModuleSw_LS82ST4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 24)
)
_H3cevtModuleSw_BOARD_LS82DSPU_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS82DSPU = _H3cevtModuleSw_BOARD_LS82DSPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 25)
)
_H3cevtModuleSw_BOARD_LS81GP8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS81GP8U = _H3cevtModuleSw_BOARD_LS81GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 26)
)
_H3cevtModuleSw_BOARD_LS82GT20_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS82GT20 = _H3cevtModuleSw_BOARD_LS82GT20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 27)
)
_H3cevtModuleSw_BOARD_LS82FE48_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS82FE48 = _H3cevtModuleSw_BOARD_LS82FE48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 28)
)
_H3cevtModuleSw_LS82T24B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82T24B = _H3cevtModuleSw_LS82T24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 29)
)
_H3cevtModuleSw_LSB1SRPA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRPA = _H3cevtModuleSw_LSB1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 30)
)
_H3cevtModuleSw_LSB1FT48A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FT48A = _H3cevtModuleSw_LSB1FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 31)
)
_H3cevtModuleSw_LSB1FT48B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FT48B = _H3cevtModuleSw_LSB1FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 32)
)
_H3cevtModuleSw_LSB1F48GA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1F48GA = _H3cevtModuleSw_LSB1F48GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 33)
)
_H3cevtModuleSw_LSB1F48GB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1F48GB = _H3cevtModuleSw_LSB1F48GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 34)
)
_H3cevtModuleSw_LSB1FP20A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FP20A = _H3cevtModuleSw_LSB1FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 35)
)
_H3cevtModuleSw_LSB1FP20B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FP20B = _H3cevtModuleSw_LSB1FP20B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 36)
)
_H3cevtModuleSw_FT48A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_FT48A = _H3cevtModuleSw_FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 37)
)
_H3cevtModuleSw_GP4U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GP4U = _H3cevtModuleSw_GP4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 38)
)
_H3cevtModuleSw_GP2U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GP2U = _H3cevtModuleSw_GP2U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 39)
)
_H3cevtModuleSw_TGX1A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_TGX1A = _H3cevtModuleSw_TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 40)
)
_H3cevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_LX_SM_IR_SC = _H3cevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 41)
)
_H3cevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_SX_MM_SR_SC = _H3cevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 42)
)
_H3cevtModuleSw_1000BASE_T_RJ45_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_T_RJ45 = _H3cevtModuleSw_1000BASE_T_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 43)
)
_H3cevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100BASE_FX_SM_IR_SC = _H3cevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 44)
)
_H3cevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100BASE_FX_MM_SR_SC = _H3cevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 45)
)
_H3cevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GIGA_STACK_1M_PC = _H3cevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 46)
)
_H3cevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_LX_SM_VLR_LC = _H3cevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 47)
)
_H3cevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_LX_SM_LR_LC = _H3cevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 48)
)
_H3cevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100BASE_FX_SM_LR_SC = _H3cevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 49)
)
_H3cevtModuleSw_1000BASE_X_GBIC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_X_GBIC = _H3cevtModuleSw_1000BASE_X_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 50)
)
_H3cevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_SINGLEMODE_FX_LC = _H3cevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 51)
)
_H3cevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_MULTIMODE_FX_LC = _H3cevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 52)
)
_H3cevtModuleSw_1000BASE_4SFP_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_4SFP = _H3cevtModuleSw_1000BASE_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 53)
)
_H3cevtModuleSw_1000BASE_4GBIC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_4GBIC = _H3cevtModuleSw_1000BASE_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 54)
)
_H3cevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_FIXED_4SFP = _H3cevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 55)
)
_H3cevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_FIXED_4GBIC = _H3cevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 56)
)
_H3cevtModuleSw_LSB1GP12A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP12A = _H3cevtModuleSw_LSB1GP12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 57)
)
_H3cevtModuleSw_LSB1GP12B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP12B = _H3cevtModuleSw_LSB1GP12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 58)
)
_H3cevtModuleSw_LSB1TGX1A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1TGX1A = _H3cevtModuleSw_LSB1TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 59)
)
_H3cevtModuleSw_LSB1TGX1B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1TGX1B = _H3cevtModuleSw_LSB1TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 60)
)
_H3cevtModuleSw_LSB1P4G8A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1P4G8A = _H3cevtModuleSw_LSB1P4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 61)
)
_H3cevtModuleSw_LSB1P4G8B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1P4G8B = _H3cevtModuleSw_LSB1P4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 62)
)
_H3cevtModuleSw_LSB1A4G8A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1A4G8A = _H3cevtModuleSw_LSB1A4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 63)
)
_H3cevtModuleSw_LSB1A4G8B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1A4G8B = _H3cevtModuleSw_LSB1A4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 64)
)
_H3cevtModuleSw_FT48C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_FT48C = _H3cevtModuleSw_FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 65)
)
_H3cevtModuleSw_FP20_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_FP20 = _H3cevtModuleSw_FP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 66)
)
_H3cevtModuleSw_BOARD_LS81FT48_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS81FT48 = _H3cevtModuleSw_BOARD_LS81FT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 67)
)
_H3cevtModuleSw_BOARD_LS81GB8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS81GB8U = _H3cevtModuleSw_BOARD_LS81GB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 68)
)
_H3cevtModuleSw_BOARD_LS81GT8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS81GT8U = _H3cevtModuleSw_BOARD_LS81GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 69)
)
_H3cevtModuleSw_BOARD_LS81FS24_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS81FS24 = _H3cevtModuleSw_BOARD_LS81FS24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 70)
)
_H3cevtModuleSw_BOARD_LS81FM24_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS81FM24 = _H3cevtModuleSw_BOARD_LS81FM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 71)
)
_H3cevtModuleSw_BOARD_LS82GP20_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS82GP20 = _H3cevtModuleSw_BOARD_LS82GP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 72)
)
_H3cevtModuleSw_LSB1SRPB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRPB = _H3cevtModuleSw_LSB1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 73)
)
_H3cevtModuleSw_LSB1F32GA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1F32GA = _H3cevtModuleSw_LSB1F32GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 74)
)
_H3cevtModuleSw_LSB1F32GB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1F32GB = _H3cevtModuleSw_LSB1F32GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 75)
)
_H3cevtModuleSw_LSB2FT48A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2FT48A = _H3cevtModuleSw_LSB2FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 76)
)
_H3cevtModuleSw_LSB2FT48B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2FT48B = _H3cevtModuleSw_LSB2FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 77)
)
_H3cevtModuleSw_LSB1GT12A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT12A = _H3cevtModuleSw_LSB1GT12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 78)
)
_H3cevtModuleSw_LSB1GT12B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT12B = _H3cevtModuleSw_LSB1GT12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 79)
)
_H3cevtModuleSw_PC4U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PC4U = _H3cevtModuleSw_PC4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 80)
)
_H3cevtModuleSw_FT32A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_FT32A = _H3cevtModuleSw_FT32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 81)
)
_H3cevtModuleSw_GT4U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GT4U = _H3cevtModuleSw_GT4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 82)
)
_H3cevtModuleSw_BOARD_LS83FP20A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS83FP20A = _H3cevtModuleSw_BOARD_LS83FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 83)
)
_H3cevtModuleSw_BOARD_LS82HGMU_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS82HGMU = _H3cevtModuleSw_BOARD_LS82HGMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 84)
)
_H3cevtModuleSw_LSB1GP8TB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP8TB = _H3cevtModuleSw_LSB1GP8TB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 85)
)
_H3cevtModuleSw_LSB1GP8TC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP8TC = _H3cevtModuleSw_LSB1GP8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 86)
)
_H3cevtModuleSw_LSB1GT8PB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT8PB = _H3cevtModuleSw_LSB1GT8PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 87)
)
_H3cevtModuleSw_LSB1GT8PC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT8PC = _H3cevtModuleSw_LSB1GT8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 88)
)
_H3cevtModuleSw_LSB1FT48C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FT48C = _H3cevtModuleSw_LSB1FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 89)
)
_H3cevtModuleSw_LSB1FP20C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FP20C = _H3cevtModuleSw_LSB1FP20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 90)
)
_H3cevtModuleSw_LSB1F32GC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1F32GC = _H3cevtModuleSw_LSB1F32GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 91)
)
_H3cevtModuleSw_LSB1GT12C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT12C = _H3cevtModuleSw_LSB1GT12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 92)
)
_H3cevtModuleSw_LSB1GP12C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP12C = _H3cevtModuleSw_LSB1GP12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 93)
)
_H3cevtModuleSw_LSB1P4G8C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1P4G8C = _H3cevtModuleSw_LSB1P4G8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 94)
)
_H3cevtModuleSw_LSB1TGX1C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1TGX1C = _H3cevtModuleSw_LSB1TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 95)
)
_H3cevtModuleSw_LSB1GT24B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT24B = _H3cevtModuleSw_LSB1GT24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 96)
)
_H3cevtModuleSw_LSB1GT24C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT24C = _H3cevtModuleSw_LSB1GT24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 97)
)
_H3cevtModuleSw_LSB1GP24B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP24B = _H3cevtModuleSw_LSB1GP24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 98)
)
_H3cevtModuleSw_LSB1GP24C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP24C = _H3cevtModuleSw_LSB1GP24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 99)
)
_H3cevtModuleSw_LSB1XP2B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP2B = _H3cevtModuleSw_LSB1XP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 100)
)
_H3cevtModuleSw_LSB1XP2C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP2C = _H3cevtModuleSw_LSB1XP2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 101)
)
_H3cevtModuleSw_LSB1GV48B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GV48B = _H3cevtModuleSw_LSB1GV48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 102)
)
_H3cevtModuleSw_LSB1GV48C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GV48C = _H3cevtModuleSw_LSB1GV48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 103)
)
_H3cevtModuleSw_LSB1SRPC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRPC = _H3cevtModuleSw_LSB1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 104)
)
_H3cevtModuleSw_LSB1SRP1N0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N0 = _H3cevtModuleSw_LSB1SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 105)
)
_H3cevtModuleSw_LSB1SRP1N1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N1 = _H3cevtModuleSw_LSB1SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 106)
)
_H3cevtModuleSw_LSB1SRP1N2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N2 = _H3cevtModuleSw_LSB1SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 107)
)
_H3cevtModuleSw_GT24_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GT24 = _H3cevtModuleSw_GT24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 108)
)
_H3cevtModuleSw_GP24_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GP24 = _H3cevtModuleSw_GP24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 109)
)
_H3cevtModuleSw_XP2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_XP2 = _H3cevtModuleSw_XP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 110)
)
_H3cevtModuleSw_GV48_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GV48 = _H3cevtModuleSw_GV48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 111)
)
_H3cevtModuleSw_LSG1GP8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSG1GP8U = _H3cevtModuleSw_LSG1GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 112)
)
_H3cevtModuleSw_LSG1GT8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSG1GT8U = _H3cevtModuleSw_LSG1GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 113)
)
_H3cevtModuleSw_LSG1TG1U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSG1TG1U = _H3cevtModuleSw_LSG1TG1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 114)
)
_H3cevtModuleSw_LSG1TD1U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSG1TD1U = _H3cevtModuleSw_LSG1TD1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 115)
)
_H3cevtModuleSw_LSB2FT48C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2FT48C = _H3cevtModuleSw_LSB2FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 116)
)
_H3cevtModuleSw_LSB1GT48B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT48B = _H3cevtModuleSw_LSB1GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 117)
)
_H3cevtModuleSw_LSB1GT48C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT48C = _H3cevtModuleSw_LSB1GT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 118)
)
_H3cevtModuleSw_LS81GT48_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GT48 = _H3cevtModuleSw_LS81GT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 119)
)
_H3cevtModuleSw_LS81SRPG0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG0 = _H3cevtModuleSw_LS81SRPG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 120)
)
_H3cevtModuleSw_LS81SRPG1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG1 = _H3cevtModuleSw_LS81SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 121)
)
_H3cevtModuleSw_LS81SRPG2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG2 = _H3cevtModuleSw_LS81SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 122)
)
_H3cevtModuleSw_LS81SRPG3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG3 = _H3cevtModuleSw_LS81SRPG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 123)
)
_H3cevtModuleSw_SR01SRPUB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUB = _H3cevtModuleSw_SR01SRPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 125)
)
_H3cevtModuleSw_SR01SRPUA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUA = _H3cevtModuleSw_SR01SRPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 126)
)
_H3cevtModuleSw_SR01GP12L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GP12L = _H3cevtModuleSw_SR01GP12L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 127)
)
_H3cevtModuleSw_SR01GP12W_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GP12W = _H3cevtModuleSw_SR01GP12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 128)
)
_H3cevtModuleSw_SR01FT48L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01FT48L = _H3cevtModuleSw_SR01FT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 129)
)
_H3cevtModuleSw_SR01FT48W_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01FT48W = _H3cevtModuleSw_SR01FT48W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 130)
)
_H3cevtModuleSw_SR01XK1W_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XK1W = _H3cevtModuleSw_SR01XK1W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 131)
)
_H3cevtModuleSw_SR01FP20W_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01FP20W = _H3cevtModuleSw_SR01FP20W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 132)
)
_H3cevtModuleSw_SR01GT12W_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT12W = _H3cevtModuleSw_SR01GT12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 133)
)
_H3cevtModuleSw_SR01F32GL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01F32GL = _H3cevtModuleSw_SR01F32GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 134)
)
_H3cevtModuleSw_SR01F32GW_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01F32GW = _H3cevtModuleSw_SR01F32GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 135)
)
_H3cevtModuleSw_SR01GT8PL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT8PL = _H3cevtModuleSw_SR01GT8PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 136)
)
_H3cevtModuleSw_SR01GT8PW_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT8PW = _H3cevtModuleSw_SR01GT8PW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 137)
)
_H3cevtModuleSw_SR01P4G8W_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01P4G8W = _H3cevtModuleSw_SR01P4G8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 138)
)
_H3cevtModuleSw_LSA1FP8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSA1FP8U = _H3cevtModuleSw_LSA1FP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 139)
)
_H3cevtModuleSw_LSB1SP4B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SP4B = _H3cevtModuleSw_LSB1SP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 140)
)
_H3cevtModuleSw_LSB1SP4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SP4C = _H3cevtModuleSw_LSB1SP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 141)
)
_H3cevtModuleSw_LSB1UP1B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1UP1B = _H3cevtModuleSw_LSB1UP1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 142)
)
_H3cevtModuleSw_LSB1UP1C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1UP1C = _H3cevtModuleSw_LSB1UP1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 143)
)
_H3cevtModuleSw_LSB1XP4B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4B = _H3cevtModuleSw_LSB1XP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 144)
)
_H3cevtModuleSw_LSB1XP4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4C = _H3cevtModuleSw_LSB1XP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 145)
)
_H3cevtModuleSw_SP4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SP4 = _H3cevtModuleSw_SP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 146)
)
_H3cevtModuleSw_UP1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_UP1 = _H3cevtModuleSw_UP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 147)
)
_H3cevtModuleSw_XP4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_XP4 = _H3cevtModuleSw_XP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 148)
)
_H3cevtModuleSw_LS81VSNP_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81VSNP = _H3cevtModuleSw_LS81VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 149)
)
_H3cevtModuleSw_LS81T12P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81T12P = _H3cevtModuleSw_LS81T12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 150)
)
_H3cevtModuleSw_LS81P12T_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81P12T = _H3cevtModuleSw_LS81P12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 151)
)
_H3cevtModuleSw_LS81GP8UB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP8UB = _H3cevtModuleSw_LS81GP8UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 152)
)
_H3cevtModuleSw_LS81FT48E_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81FT48E = _H3cevtModuleSw_LS81FT48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 153)
)
_H3cevtModuleSw_LS81GP4UB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP4UB = _H3cevtModuleSw_LS81GP4UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 154)
)
_H3cevtModuleSw_LS81GT8UE_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GT8UE = _H3cevtModuleSw_LS81GT8UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 155)
)
_H3cevtModuleSw_LS81GT48A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GT48A = _H3cevtModuleSw_LS81GT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 156)
)
_H3cevtModuleSw_LS81FP48_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81FP48 = _H3cevtModuleSw_LS81FP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 157)
)
_H3cevtModuleSw_LSB1XK1B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XK1B = _H3cevtModuleSw_LSB1XK1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 158)
)
_H3cevtModuleSw_LSB1XK1C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XK1C = _H3cevtModuleSw_LSB1XK1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 159)
)
_H3cevtModuleSw_SR01SRPUC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUC = _H3cevtModuleSw_SR01SRPUC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 160)
)
_H3cevtModuleSw_SR01SRPUD_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUD = _H3cevtModuleSw_SR01SRPUD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 161)
)
_H3cevtModuleSw_SR01SRPUE_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUE = _H3cevtModuleSw_SR01SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 162)
)
_H3cevtModuleSw_LSB1SRP1N3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N3 = _H3cevtModuleSw_LSB1SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 163)
)
_H3cevtModuleSw_LSB1VP2B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1VP2B = _H3cevtModuleSw_LSB1VP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 164)
)
_H3cevtModuleSw_LSB1NATB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1NATB = _H3cevtModuleSw_LSB1NATB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 165)
)
_H3cevtModuleSw_LSB1VPNB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1VPNB = _H3cevtModuleSw_LSB1VPNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 166)
)
_H3cevtModuleSw_LSGP8P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSGP8P = _H3cevtModuleSw_LSGP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 167)
)
_H3cevtModuleSw_LSXK1P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSXK1P = _H3cevtModuleSw_LSXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 168)
)
_H3cevtModuleSw_LSXP2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSXP2P = _H3cevtModuleSw_LSXP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 169)
)
_H3cevtModuleSw_LS81FT48F_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81FT48F = _H3cevtModuleSw_LS81FT48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 170)
)
_H3cevtModuleSw_LS81PT8G_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81PT8G = _H3cevtModuleSw_LS81PT8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 171)
)
_H3cevtModuleSw_LS81PT4G_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81PT4G = _H3cevtModuleSw_LS81PT4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 172)
)
_H3cevtModuleSw_LSSTK24G_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSSTK24G = _H3cevtModuleSw_LSSTK24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 173)
)
_H3cevtModuleSw_LS82GT20A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82GT20A = _H3cevtModuleSw_LS82GT20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 174)
)
_H3cevtModuleSw_LS82GP20A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82GP20A = _H3cevtModuleSw_LS82GP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 175)
)
_H3cevtModuleSw_LS81TGX1C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81TGX1C = _H3cevtModuleSw_LS81TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 176)
)
_H3cevtModuleSw_VP2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_VP2 = _H3cevtModuleSw_VP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 177)
)
_H3cevtModuleSw_LSA1FB8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSA1FB8U = _H3cevtModuleSw_LSA1FB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 178)
)
_H3cevtModuleSw_LS81T12PE_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81T12PE = _H3cevtModuleSw_LS81T12PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 179)
)
_H3cevtModuleSw_LS81P12TE_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81P12TE = _H3cevtModuleSw_LS81P12TE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 180)
)
_H3cevtModuleSw_LSB1SRP2N0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N0 = _H3cevtModuleSw_LSB1SRP2N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 181)
)
_H3cevtModuleSw_LSB1SRP2N3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N3 = _H3cevtModuleSw_LSB1SRP2N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 182)
)
_H3cevtModuleSw_LSB1GV48DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GV48DB = _H3cevtModuleSw_LSB1GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 183)
)
_H3cevtModuleSw_LSB1FW8B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FW8B = _H3cevtModuleSw_LSB1FW8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 184)
)
_H3cevtModuleSw_LSB1IPSEC8B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1IPSEC8B = _H3cevtModuleSw_LSB1IPSEC8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 185)
)
_H3cevtModuleSw_LSB1IDSB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1IDSB = _H3cevtModuleSw_LSB1IDSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 186)
)
_H3cevtModuleSw_LSB1IPSB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1IPSB = _H3cevtModuleSw_LSB1IPSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 187)
)
_H3cevtModuleSw_LSB2FT48CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2FT48CA = _H3cevtModuleSw_LSB2FT48CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 188)
)
_H3cevtModuleSw_LSB1FP20CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FP20CA = _H3cevtModuleSw_LSB1FP20CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 189)
)
_H3cevtModuleSw_LSB1F32GCA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1F32GCA = _H3cevtModuleSw_LSB1F32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 190)
)
_H3cevtModuleSw_LSB1P4G8CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1P4G8CA = _H3cevtModuleSw_LSB1P4G8CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 191)
)
_H3cevtModuleSw_LSB1GT12CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT12CA = _H3cevtModuleSw_LSB1GT12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 192)
)
_H3cevtModuleSw_LSB1GT24CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT24CA = _H3cevtModuleSw_LSB1GT24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 193)
)
_H3cevtModuleSw_LSB1GP12CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP12CA = _H3cevtModuleSw_LSB1GP12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 194)
)
_H3cevtModuleSw_LSB1GP24CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP24CA = _H3cevtModuleSw_LSB1GP24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 195)
)
_H3cevtModuleSw_LSB1GT8PCA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT8PCA = _H3cevtModuleSw_LSB1GT8PCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 196)
)
_H3cevtModuleSw_LSB1XP2CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP2CA = _H3cevtModuleSw_LSB1XP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 197)
)
_H3cevtModuleSw_LSB1XK1CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XK1CA = _H3cevtModuleSw_LSB1XK1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 198)
)
_H3cevtModuleSw_LSB1XP4CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4CA = _H3cevtModuleSw_LSB1XP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 199)
)
_H3cevtModuleSw_LSB1UP1CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1UP1CA = _H3cevtModuleSw_LSB1UP1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 200)
)
_H3cevtModuleSw_LSB1SP4CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SP4CA = _H3cevtModuleSw_LSB1SP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 201)
)
_H3cevtModuleSw_LSB1VP2CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1VP2CA = _H3cevtModuleSw_LSB1VP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 202)
)
_H3cevtModuleSw_SR01FT48WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01FT48WA = _H3cevtModuleSw_SR01FT48WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 203)
)
_H3cevtModuleSw_SR01FP20WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01FP20WA = _H3cevtModuleSw_SR01FP20WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 204)
)
_H3cevtModuleSw_SR01F32GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01F32GWA = _H3cevtModuleSw_SR01F32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 205)
)
_H3cevtModuleSw_SR01P4G8WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01P4G8WA = _H3cevtModuleSw_SR01P4G8WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 206)
)
_H3cevtModuleSw_SR01GT12WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT12WA = _H3cevtModuleSw_SR01GT12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 207)
)
_H3cevtModuleSw_SR01GT24WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT24WA = _H3cevtModuleSw_SR01GT24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 208)
)
_H3cevtModuleSw_SR01GP12WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GP12WA = _H3cevtModuleSw_SR01GP12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 209)
)
_H3cevtModuleSw_SR01GP24WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GP24WA = _H3cevtModuleSw_SR01GP24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 210)
)
_H3cevtModuleSw_SR01GT8PWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT8PWA = _H3cevtModuleSw_SR01GT8PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 211)
)
_H3cevtModuleSw_SR01XP2WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XP2WA = _H3cevtModuleSw_SR01XP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 212)
)
_H3cevtModuleSw_SR01XK1WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XK1WA = _H3cevtModuleSw_SR01XK1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 213)
)
_H3cevtModuleSw_SR01UP1WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01UP1WA = _H3cevtModuleSw_SR01UP1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 214)
)
_H3cevtModuleSw_SR01SP4WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SP4WA = _H3cevtModuleSw_SR01SP4WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 215)
)
_H3cevtModuleSw_GP8U_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_GP8U = _H3cevtModuleSw_GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 216)
)
_H3cevtModuleSw_LSEXP1P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSEXP1P = _H3cevtModuleSw_LSEXP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 217)
)
_H3cevtModuleSw_LSEXK1P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSEXK1P = _H3cevtModuleSw_LSEXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 218)
)
_H3cevtModuleSw_LSEXS1P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSEXS1P = _H3cevtModuleSw_LSEXS1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 219)
)
_H3cevtModuleSw_LS81GP48_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP48 = _H3cevtModuleSw_LS81GP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 220)
)
_H3cevtModuleSw_LS81GT48B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GT48B = _H3cevtModuleSw_LS81GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 221)
)
_H3cevtModuleSw_LS81T16P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81T16P = _H3cevtModuleSw_LS81T16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 222)
)
_H3cevtModuleSw_LS81T32P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81T32P = _H3cevtModuleSw_LS81T32P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 223)
)
_H3cevtModuleSw_LS81TGX2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81TGX2 = _H3cevtModuleSw_LS81TGX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 224)
)
_H3cevtModuleSw_LS81TGX4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81TGX4 = _H3cevtModuleSw_LS81TGX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 225)
)
_H3cevtModuleSw_LSB1GV48DA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GV48DA = _H3cevtModuleSw_LSB1GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 226)
)
_H3cevtModuleSw_SR01GV48VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GV48VB = _H3cevtModuleSw_SR01GV48VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 227)
)
_H3cevtModuleSw_LSB1GT24DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT24DB = _H3cevtModuleSw_LSB1GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 228)
)
_H3cevtModuleSw_LSB1GP24DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP24DB = _H3cevtModuleSw_LSB1GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 229)
)
_H3cevtModuleSw_LSB1GP24DC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP24DC = _H3cevtModuleSw_LSB1GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 230)
)
_H3cevtModuleSw_LSB1FW8DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FW8DB = _H3cevtModuleSw_LSB1FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 231)
)
_H3cevtModuleSw_LSB1IPSEC8DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1IPSEC8DB = _H3cevtModuleSw_LSB1IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 232)
)
_H3cevtModuleSw_SR01GT24VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GT24VB = _H3cevtModuleSw_SR01GT24VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 233)
)
_H3cevtModuleSw_SR01GP24VC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GP24VC = _H3cevtModuleSw_SR01GP24VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 234)
)
_H3cevtModuleSw_SR01VP2WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01VP2WA = _H3cevtModuleSw_SR01VP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 235)
)
_H3cevtModuleSw_SR01FW8VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01FW8VB = _H3cevtModuleSw_SR01FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 236)
)
_H3cevtModuleSw_SR01IPSEC8VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01IPSEC8VB = _H3cevtModuleSw_SR01IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 237)
)
_H3cevtModuleSw_SR01NATL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01NATL = _H3cevtModuleSw_SR01NATL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 238)
)
_H3cevtModuleSw_SR01VPNL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01VPNL = _H3cevtModuleSw_SR01VPNL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 239)
)
_H3cevtModuleSw_LSB1GP24CB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP24CB = _H3cevtModuleSw_LSB1GP24CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 240)
)
_H3cevtModuleSw_LSB1GP48DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP48DB = _H3cevtModuleSw_LSB1GP48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 241)
)
_H3cevtModuleSw_LSB1XP2CB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP2CB = _H3cevtModuleSw_LSB1XP2CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 242)
)
_H3cevtModuleSw_XP4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_XP4L = _H3cevtModuleSw_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 243)
)
_H3cevtModuleSw_LSB1XP4LDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4LDB = _H3cevtModuleSw_LSB1XP4LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 244)
)
_H3cevtModuleSw_LSB1XP4LDC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4LDC = _H3cevtModuleSw_LSB1XP4LDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 245)
)
_H3cevtModuleSw_AHP4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_AHP4 = _H3cevtModuleSw_AHP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 246)
)
_H3cevtModuleSw_LSB1AHP4GCA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1AHP4GCA = _H3cevtModuleSw_LSB1AHP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 247)
)
_H3cevtModuleSw_CLP4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CLP4 = _H3cevtModuleSw_CLP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 248)
)
_H3cevtModuleSw_LSB1CLP4GCA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1CLP4GCA = _H3cevtModuleSw_LSB1CLP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 249)
)
_H3cevtModuleSw_ET32_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_ET32 = _H3cevtModuleSw_ET32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 250)
)
_H3cevtModuleSw_LSB1ET32GCA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1ET32GCA = _H3cevtModuleSw_LSB1ET32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 251)
)
_H3cevtModuleSw_LSB1IDSDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1IDSDB = _H3cevtModuleSw_LSB1IDSDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 252)
)
_H3cevtModuleSw_LSB1SRP2N1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N1 = _H3cevtModuleSw_LSB1SRP2N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 253)
)
_H3cevtModuleSw_BOARD_LS82SRPB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BOARD_LS82SRPB = _H3cevtModuleSw_BOARD_LS82SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 254)
)
_H3cevtModuleSw_BORAD_LS83SRPC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_BORAD_LS83SRPC = _H3cevtModuleSw_BORAD_LS83SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 255)
)
_H3cevtModuleSw_Main_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_Main = _H3cevtModuleSw_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 256)
)
_H3cevtModuleSw_LSB1SRP2N2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N2 = _H3cevtModuleSw_LSB1SRP2N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 257)
)
_H3cevtModuleSw_LSB1NAMB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1NAMB = _H3cevtModuleSw_LSB1NAMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 258)
)
_H3cevtModuleSw_RSP2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_RSP2 = _H3cevtModuleSw_RSP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 259)
)
_H3cevtModuleSw_LSB1RSP2CA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1RSP2CA = _H3cevtModuleSw_LSB1RSP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 260)
)
_H3cevtModuleSw_SR01XP4LVC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XP4LVC = _H3cevtModuleSw_SR01XP4LVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 261)
)
_H3cevtModuleSw_SR01AHP4GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01AHP4GWA = _H3cevtModuleSw_SR01AHP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 262)
)
_H3cevtModuleSw_SR01CLP4GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01CLP4GWA = _H3cevtModuleSw_SR01CLP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 263)
)
_H3cevtModuleSw_SR01ET32GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01ET32GWA = _H3cevtModuleSw_SR01ET32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 264)
)
_H3cevtModuleSw_SR01IDSVB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01IDSVB = _H3cevtModuleSw_SR01IDSVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 265)
)
_H3cevtModuleSw_SR01SRPUF_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUF = _H3cevtModuleSw_SR01SRPUF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 266)
)
_H3cevtModuleSw_SR01NAML_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01NAML = _H3cevtModuleSw_SR01NAML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 267)
)
_H3cevtModuleSw_SR01RSP2WA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01RSP2WA = _H3cevtModuleSw_SR01RSP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 268)
)
_H3cevtModuleSw_LSPM1XP1P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSPM1XP1P = _H3cevtModuleSw_LSPM1XP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 269)
)
_H3cevtModuleSw_LSPM1XP2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSPM1XP2P = _H3cevtModuleSw_LSPM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 270)
)
_H3cevtModuleSw_LSPM1CX2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSPM1CX2P = _H3cevtModuleSw_LSPM1CX2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 271)
)
_H3cevtModuleSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_STK_1000BASE_T = _H3cevtModuleSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 272)
)
_H3cevtModuleSw_LSB1SRP1M0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1M0 = _H3cevtModuleSw_LSB1SRP1M0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 300)
)
_H3cevtModuleSw_LSB1SRP1M1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1M1 = _H3cevtModuleSw_LSB1SRP1M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 301)
)
_H3cevtModuleSw_LSB1GP12DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP12DB = _H3cevtModuleSw_LSB1GP12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 302)
)
_H3cevtModuleSw_LSB1GT12DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT12DB = _H3cevtModuleSw_LSB1GT12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 303)
)
_H3cevtModuleSw_LSB1XK1DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XK1DB = _H3cevtModuleSw_LSB1XK1DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 304)
)
_H3cevtModuleSw_LSB1XP2DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP2DB = _H3cevtModuleSw_LSB1XP2DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 305)
)
_H3cevtModuleSw_LSB1XP2DC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP2DC = _H3cevtModuleSw_LSB1XP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 306)
)
_H3cevtModuleSw_LSB1GT48LDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GT48LDB = _H3cevtModuleSw_LSB1GT48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 307)
)
_H3cevtModuleSw_LSB1XP4TDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4TDB = _H3cevtModuleSw_LSB1XP4TDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 308)
)
_H3cevtModuleSw_LSB1XP4TDC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4TDC = _H3cevtModuleSw_LSB1XP4TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 309)
)
_H3cevtModuleSw_LSB1RSP2DC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1RSP2DC = _H3cevtModuleSw_LSB1RSP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 310)
)
_H3cevtModuleSw_LSB1VP2DC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1VP2DC = _H3cevtModuleSw_LSB1VP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 311)
)
_H3cevtModuleSw_LSB1XP4DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1XP4DB = _H3cevtModuleSw_LSB1XP4DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 312)
)
_H3cevtModuleSw_LSB1SRP2E0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2E0 = _H3cevtModuleSw_LSB1SRP2E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 313)
)
_H3cevtModuleSw_LSB1SRP2E1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2E1 = _H3cevtModuleSw_LSB1SRP2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 314)
)
_H3cevtModuleSw_LSB1SRP2E2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2E2 = _H3cevtModuleSw_LSB1SRP2E2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 315)
)
_H3cevtModuleSw_LSB1SRP2E3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2E3 = _H3cevtModuleSw_LSB1SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 316)
)
_H3cevtModuleSw_SR01SRPUQ_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUQ = _H3cevtModuleSw_SR01SRPUQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 317)
)
_H3cevtModuleSw_AHP1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_AHP1 = _H3cevtModuleSw_AHP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 318)
)
_H3cevtModuleSw_AHP2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_AHP2 = _H3cevtModuleSw_AHP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 319)
)
_H3cevtModuleSw_CLP1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CLP1 = _H3cevtModuleSw_CLP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 320)
)
_H3cevtModuleSw_CLP2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CLP2 = _H3cevtModuleSw_CLP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 321)
)
_H3cevtModuleSw_ET16_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_ET16 = _H3cevtModuleSw_ET16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 322)
)
_H3cevtModuleSw_LSB1SRP1NA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA0 = _H3cevtModuleSw_LSB1SRP1NA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 323)
)
_H3cevtModuleSw_LSB1SRP1NA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA1 = _H3cevtModuleSw_LSB1SRP1NA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 324)
)
_H3cevtModuleSw_LSB1SRP1NA2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA2 = _H3cevtModuleSw_LSB1SRP1NA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 325)
)
_H3cevtModuleSw_LSB1SRP1NA3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA3 = _H3cevtModuleSw_LSB1SRP1NA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 326)
)
_H3cevtModuleSw_SR01AHP1GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01AHP1GWA = _H3cevtModuleSw_SR01AHP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 327)
)
_H3cevtModuleSw_SR01AHP2GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01AHP2GWA = _H3cevtModuleSw_SR01AHP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 328)
)
_H3cevtModuleSw_SR01CLP1GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01CLP1GWA = _H3cevtModuleSw_SR01CLP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 329)
)
_H3cevtModuleSw_SR01CLP2GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01CLP2GWA = _H3cevtModuleSw_SR01CLP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 330)
)
_H3cevtModuleSw_SR01ET16GWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01ET16GWA = _H3cevtModuleSw_SR01ET16GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 331)
)
_H3cevtModuleSw_SR01GP12VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01GP12VB = _H3cevtModuleSw_SR01GP12VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 332)
)
_H3cevtModuleSw_SR01XK1VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XK1VB = _H3cevtModuleSw_SR01XK1VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 333)
)
_H3cevtModuleSw_SR01XP2VC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XP2VC = _H3cevtModuleSw_SR01XP2VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 334)
)
_H3cevtModuleSw_SR01XP4LVB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01XP4LVB = _H3cevtModuleSw_SR01XP4LVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 335)
)
_H3cevtModuleSw_SR01SRPUEA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01SRPUEA = _H3cevtModuleSw_SR01SRPUEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 336)
)
_H3cevtModuleSw_LSB1SRP1N4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N4 = _H3cevtModuleSw_LSB1SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 337)
)
_H3cevtModuleSw_LSB1SRP1N5_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N5 = _H3cevtModuleSw_LSB1SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 338)
)
_H3cevtModuleSw_LSB1SRP1N6_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N6 = _H3cevtModuleSw_LSB1SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 339)
)
_H3cevtModuleSw_LSB1SRP1N7_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1N7 = _H3cevtModuleSw_LSB1SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 340)
)
_H3cevtModuleSw_LSB1SRP2N4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N4 = _H3cevtModuleSw_LSB1SRP2N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 341)
)
_H3cevtModuleSw_LSB1SRP2N5_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N5 = _H3cevtModuleSw_LSB1SRP2N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 342)
)
_H3cevtModuleSw_LSB1SRP2N6_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N6 = _H3cevtModuleSw_LSB1SRP2N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 343)
)
_H3cevtModuleSw_LSB1SRP2N7_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP2N7 = _H3cevtModuleSw_LSB1SRP2N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 344)
)
_H3cevtModuleSw_LSB1SRP1NA4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA4 = _H3cevtModuleSw_LSB1SRP1NA4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 345)
)
_H3cevtModuleSw_LSB1SRP1NA5_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA5 = _H3cevtModuleSw_LSB1SRP1NA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 346)
)
_H3cevtModuleSw_LSB1SRP1NA6_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA6 = _H3cevtModuleSw_LSB1SRP1NA6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 347)
)
_H3cevtModuleSw_LSB1SRP1NA7_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SRP1NA7 = _H3cevtModuleSw_LSB1SRP1NA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 348)
)
_H3cevtModuleSw_LSB2GV48DA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2GV48DA = _H3cevtModuleSw_LSB2GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 349)
)
_H3cevtModuleSw_LSB1RGP2GDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1RGP2GDB = _H3cevtModuleSw_LSB1RGP2GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 350)
)
_H3cevtModuleSw_LSB1RGP4GDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1RGP4GDB = _H3cevtModuleSw_LSB1RGP4GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 351)
)
_H3cevtModuleSw_LSB2GP24DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2GP24DB = _H3cevtModuleSw_LSB2GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 352)
)
_H3cevtModuleSw_LSB2GP24DC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2GP24DC = _H3cevtModuleSw_LSB2GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 353)
)
_H3cevtModuleSw_LSB2GT24DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2GT24DB = _H3cevtModuleSw_LSB2GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 354)
)
_H3cevtModuleSw_LSB2FW8DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2FW8DB = _H3cevtModuleSw_LSB2FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 355)
)
_H3cevtModuleSw_LSB2IPSEC8DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2IPSEC8DB = _H3cevtModuleSw_LSB2IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 356)
)
_H3cevtModuleSw_LSB2GV48DB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2GV48DB = _H3cevtModuleSw_LSB2GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 357)
)
_H3cevtModuleSw_RGP2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_RGP2 = _H3cevtModuleSw_RGP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 358)
)
_H3cevtModuleSw_RGP4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_RGP4 = _H3cevtModuleSw_RGP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 359)
)
_H3cevtModuleSw_SR02FW8VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02FW8VB = _H3cevtModuleSw_SR02FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 360)
)
_H3cevtModuleSw_SR02IPSEC8VB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02IPSEC8VB = _H3cevtModuleSw_SR02IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 361)
)
_H3cevtModuleSw_LSB2SRP1N0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N0 = _H3cevtModuleSw_LSB2SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 362)
)
_H3cevtModuleSw_LSB2SRP1N1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N1 = _H3cevtModuleSw_LSB2SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 363)
)
_H3cevtModuleSw_LSB2SRP1N2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N2 = _H3cevtModuleSw_LSB2SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 364)
)
_H3cevtModuleSw_LSB2SRP1N3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N3 = _H3cevtModuleSw_LSB2SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 365)
)
_H3cevtModuleSw_LSB2SRP1N4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N4 = _H3cevtModuleSw_LSB2SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 366)
)
_H3cevtModuleSw_LSB2SRP1N5_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N5 = _H3cevtModuleSw_LSB2SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 367)
)
_H3cevtModuleSw_LSB2SRP1N6_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N6 = _H3cevtModuleSw_LSB2SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 368)
)
_H3cevtModuleSw_LSB2SRP1N7_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB2SRP1N7 = _H3cevtModuleSw_LSB2SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 369)
)
_H3cevtModuleSw_SR02SRPUE_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRPUE = _H3cevtModuleSw_SR02SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 370)
)
_H3cevtModuleSw_SR01LN1BQH0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01LN1BQH0 = _H3cevtModuleSw_SR01LN1BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 371)
)
_H3cevtModuleSw_SR01DXP1L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DXP1L = _H3cevtModuleSw_SR01DXP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 372)
)
_H3cevtModuleSw_SR01DGP10L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DGP10L = _H3cevtModuleSw_SR01DGP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 373)
)
_H3cevtModuleSw_SR01DRSP2L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DRSP2L = _H3cevtModuleSw_SR01DRSP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 374)
)
_H3cevtModuleSw_SR01DRUP1L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DRUP1L = _H3cevtModuleSw_SR01DRUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 375)
)
_H3cevtModuleSw_SR01DGP20R_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DGP20R = _H3cevtModuleSw_SR01DGP20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 376)
)
_H3cevtModuleSw_SR01DPLP8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DPLP8L = _H3cevtModuleSw_SR01DPLP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 377)
)
_H3cevtModuleSw_SR01DXP2R_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DXP2R = _H3cevtModuleSw_SR01DXP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 378)
)
_H3cevtModuleSw_LSB1FW2A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1FW2A0 = _H3cevtModuleSw_LSB1FW2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 379)
)
_H3cevtModuleSw_LSB1GP48LDB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1GP48LDB = _H3cevtModuleSw_LSB1GP48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 380)
)
_H3cevtModuleSw_SR01LN1BNA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01LN1BNA0 = _H3cevtModuleSw_SR01LN1BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 381)
)
_H3cevtModuleSw_SR01LN2BQH0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01LN2BQH0 = _H3cevtModuleSw_SR01LN2BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 382)
)
_H3cevtModuleSw_SR01LN2BNA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01LN2BNA0 = _H3cevtModuleSw_SR01LN2BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 383)
)
_H3cevtModuleSw_SR01DGT20R_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DGT20R = _H3cevtModuleSw_SR01DGT20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 384)
)
_H3cevtModuleSw_SR01DPSP4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DPSP4L = _H3cevtModuleSw_SR01DPSP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 385)
)
_H3cevtModuleSw_SR01DPUP1L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DPUP1L = _H3cevtModuleSw_SR01DPUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 386)
)
_H3cevtModuleSw_SR01DPL2G6L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DPL2G6L = _H3cevtModuleSw_SR01DPL2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 387)
)
_H3cevtModuleSw_SR01DPH2G6L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DPH2G6L = _H3cevtModuleSw_SR01DPH2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 388)
)
_H3cevtModuleSw_SR01DPS2G4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DPS2G4L = _H3cevtModuleSw_SR01DPS2G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 389)
)
_H3cevtModuleSw_SR01DCL1G8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DCL1G8L = _H3cevtModuleSw_SR01DCL1G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 390)
)
_H3cevtModuleSw_SR01DCL2G8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DCL2G8L = _H3cevtModuleSw_SR01DCL2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 391)
)
_H3cevtModuleSw_SR01DET8G8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DET8G8L = _H3cevtModuleSw_SR01DET8G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 392)
)
_H3cevtModuleSw_SR02SRP2E3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRP2E3 = _H3cevtModuleSw_SR02SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 393)
)
_H3cevtModuleSw_SR02SRP1E3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRP1E3 = _H3cevtModuleSw_SR02SRP1E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 394)
)
_H3cevtModuleSw_SR02SRP1M3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRP1M3 = _H3cevtModuleSw_SR02SRP1M3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 395)
)
_H3cevtModuleSw_SR01DQCP4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DQCP4L = _H3cevtModuleSw_SR01DQCP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 396)
)
_H3cevtModuleSw_SR01DTCP8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DTCP8L = _H3cevtModuleSw_SR01DTCP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 397)
)
_H3cevtModuleSw_LSB1AFC1A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1AFC1A0 = _H3cevtModuleSw_LSB1AFC1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 398)
)
_H3cevtModuleSw_LSB1SSL1A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1SSL1A0 = _H3cevtModuleSw_LSB1SSL1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 399)
)
_H3cevtModuleSw_IMNAM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IMNAM = _H3cevtModuleSw_IMNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 400)
)
_H3cevtModuleSw_IMNAT_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IMNAT = _H3cevtModuleSw_IMNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 401)
)
_H3cevtModuleSw_PICAHP1L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PICAHP1L = _H3cevtModuleSw_PICAHP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 402)
)
_H3cevtModuleSw_PICALP4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PICALP4L = _H3cevtModuleSw_PICALP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 403)
)
_H3cevtModuleSw_PICCHP4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PICCHP4L = _H3cevtModuleSw_PICCHP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 404)
)
_H3cevtModuleSw_PICCHS1G4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PICCHS1G4L = _H3cevtModuleSw_PICCHS1G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 405)
)
_H3cevtModuleSw_PICCLS4G4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PICCLS4G4L = _H3cevtModuleSw_PICCLS4G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 406)
)
_H3cevtModuleSw_PICCSP1L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PICCSP1L = _H3cevtModuleSw_PICCSP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 407)
)
_H3cevtModuleSw_LSB1ACG1A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1ACG1A0 = _H3cevtModuleSw_LSB1ACG1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 408)
)
_H3cevtModuleSw_LST1MRPNC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1MRPNC1 = _H3cevtModuleSw_LST1MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 409)
)
_H3cevtModuleSw_LST1SF18B1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1SF18B1 = _H3cevtModuleSw_LST1SF18B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 410)
)
_H3cevtModuleSw_LST1SF08B1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1SF08B1 = _H3cevtModuleSw_LST1SF08B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 411)
)
_H3cevtModuleSw_LST1GT48LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GT48LEC1 = _H3cevtModuleSw_LST1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 412)
)
_H3cevtModuleSw_LST1GP48LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GP48LEC1 = _H3cevtModuleSw_LST1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 413)
)
_H3cevtModuleSw_LST1XP4LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP4LEC1 = _H3cevtModuleSw_LST1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 414)
)
_H3cevtModuleSw_LST1XP8LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP8LEC1 = _H3cevtModuleSw_LST1XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 415)
)
_H3cevtModuleSw_LSR1SRP2B1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1SRP2B1 = _H3cevtModuleSw_LSR1SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 416)
)
_H3cevtModuleSw_LSR1SRP2C1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1SRP2C1 = _H3cevtModuleSw_LSR1SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 417)
)
_H3cevtModuleSw_LSR1SRP2B2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1SRP2B2 = _H3cevtModuleSw_LSR1SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 418)
)
_H3cevtModuleSw_LSR1SRP2C2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1SRP2C2 = _H3cevtModuleSw_LSR1SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 419)
)
_H3cevtModuleSw_LSR1GT24LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GT24LEC1 = _H3cevtModuleSw_LSR1GT24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 420)
)
_H3cevtModuleSw_LSR1GP24LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GP24LEB1 = _H3cevtModuleSw_LSR1GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 421)
)
_H3cevtModuleSw_LSR1GP24LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GP24LEC1 = _H3cevtModuleSw_LSR1GP24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 422)
)
_H3cevtModuleSw_LSR1GT48LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GT48LEB1 = _H3cevtModuleSw_LSR1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 423)
)
_H3cevtModuleSw_LSR1GT48LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GT48LEC1 = _H3cevtModuleSw_LSR1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 424)
)
_H3cevtModuleSw_LSR1GP48LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GP48LEB1 = _H3cevtModuleSw_LSR1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 425)
)
_H3cevtModuleSw_LSR1GP48LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GP48LEC1 = _H3cevtModuleSw_LSR1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 426)
)
_H3cevtModuleSw_LSR2GV48REB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2GV48REB1 = _H3cevtModuleSw_LSR2GV48REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 427)
)
_H3cevtModuleSw_LSR1XP2LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP2LEB1 = _H3cevtModuleSw_LSR1XP2LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 428)
)
_H3cevtModuleSw_LSR1XP2LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP2LEC1 = _H3cevtModuleSw_LSR1XP2LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 429)
)
_H3cevtModuleSw_LSR1XP4LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP4LEB1 = _H3cevtModuleSw_LSR1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 430)
)
_H3cevtModuleSw_LSR1XP4LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP4LEC1 = _H3cevtModuleSw_LSR1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 431)
)
_H3cevtModuleSw_IMFW_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IMFW = _H3cevtModuleSw_IMFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 432)
)
_H3cevtModuleSw_LSB1LB1A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1LB1A0 = _H3cevtModuleSw_LSB1LB1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 433)
)
_H3cevtModuleSw_LSB1IPS1A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1IPS1A0 = _H3cevtModuleSw_LSB1IPS1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 434)
)
_H3cevtModuleSw_LST1GT48LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GT48LEB1 = _H3cevtModuleSw_LST1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 435)
)
_H3cevtModuleSw_LST1GP48LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GP48LEB1 = _H3cevtModuleSw_LST1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 436)
)
_H3cevtModuleSw_LST1XP4LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP4LEB1 = _H3cevtModuleSw_LST1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 437)
)
_H3cevtModuleSw_LST1XP8LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP8LEB1 = _H3cevtModuleSw_LST1XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 438)
)
_H3cevtModuleSw_LST1XP32REB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP32REB1 = _H3cevtModuleSw_LST1XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 439)
)
_H3cevtModuleSw_LST1XP32REC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP32REC1 = _H3cevtModuleSw_LST1XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 440)
)
_H3cevtModuleSw_LSR1FW2A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1FW2A1 = _H3cevtModuleSw_LSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 441)
)
_H3cevtModuleSw_LSR1SSL1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1SSL1A1 = _H3cevtModuleSw_LSR1SSL1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 442)
)
_H3cevtModuleSw_SR01DET32G2L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR01DET32G2L = _H3cevtModuleSw_SR01DET32G2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 443)
)
_H3cevtModuleSw_LSR1GP24LEF1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GP24LEF1 = _H3cevtModuleSw_LSR1GP24LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 444)
)
_H3cevtModuleSw_LSR1XP4LEF1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP4LEF1 = _H3cevtModuleSw_LSR1XP4LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 445)
)
_H3cevtModuleSw_LSR1LB1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1LB1A1 = _H3cevtModuleSw_LSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 446)
)
_H3cevtModuleSw_LSR1NSM1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1NSM1A1 = _H3cevtModuleSw_LSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 447)
)
_H3cevtModuleSw_LSR1ACG1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1ACG1A1 = _H3cevtModuleSw_LSR1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 448)
)
_H3cevtModuleSw_LSR1IPS1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1IPS1A1 = _H3cevtModuleSw_LSR1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 449)
)
_H3cevtModuleSw_LSR2GP24LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2GP24LEB1 = _H3cevtModuleSw_LSR2GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 450)
)
_H3cevtModuleSw_LSR2GT24LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2GT24LEB1 = _H3cevtModuleSw_LSR2GT24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 451)
)
_H3cevtModuleSw_LSR2GT48LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2GT48LEB1 = _H3cevtModuleSw_LSR2GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 452)
)
_H3cevtModuleSw_SPC_GP24L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GP24L = _H3cevtModuleSw_SPC_GP24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 453)
)
_H3cevtModuleSw_SPC_GT48L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GT48L = _H3cevtModuleSw_SPC_GT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 454)
)
_H3cevtModuleSw_SPC_GP48L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GP48L = _H3cevtModuleSw_SPC_GP48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 455)
)
_H3cevtModuleSw_SPC_XP2L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_XP2L = _H3cevtModuleSw_SPC_XP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 456)
)
_H3cevtModuleSw_SPC_XP4L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_XP4L = _H3cevtModuleSw_SPC_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 457)
)
_H3cevtModuleSw_SR06SRP2E3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR06SRP2E3 = _H3cevtModuleSw_SR06SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 458)
)
_H3cevtModuleSw_SPE_2010_E_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPE_2010_E = _H3cevtModuleSw_SPE_2010_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 459)
)
_H3cevtModuleSw_SPE_2020_E_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPE_2020_E = _H3cevtModuleSw_SPE_2020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 460)
)
_H3cevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_XP4L_S_SDI = _H3cevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 461)
)
_H3cevtModuleSw_SPC_GT48L_SDI_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GT48L_SDI = _H3cevtModuleSw_SPC_GT48L_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 462)
)
_H3cevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GP48L_S_SDI = _H3cevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 463)
)
_H3cevtModuleSw_SPC_SR02OPMA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_SR02OPMA0 = _H3cevtModuleSw_SPC_SR02OPMA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 464)
)
_H3cevtModuleSw_LSR1XP16REB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP16REB1 = _H3cevtModuleSw_LSR1XP16REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 465)
)
_H3cevtModuleSw_LSR1GP48LEF1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1GP48LEF1 = _H3cevtModuleSw_LSR1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 466)
)
_H3cevtModuleSw_LST1GP48LEF1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GP48LEF1 = _H3cevtModuleSw_LST1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 467)
)
_H3cevtModuleSw_LST1XP8LEF1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP8LEF1 = _H3cevtModuleSw_LST1XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 468)
)
_H3cevtModuleSw_SPE_1010_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPE_1010_II = _H3cevtModuleSw_SPE_1010_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 469)
)
_H3cevtModuleSw_SPE_1010_E_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPE_1010_E_II = _H3cevtModuleSw_SPE_1010_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 470)
)
_H3cevtModuleSw_SPE_1020_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPE_1020_II = _H3cevtModuleSw_SPE_1020_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 471)
)
_H3cevtModuleSw_SPE_1020_E_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPE_1020_E_II = _H3cevtModuleSw_SPE_1020_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 472)
)
_H3cevtModuleSw_LST1FW2A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1FW2A1 = _H3cevtModuleSw_LST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 473)
)
_H3cevtModuleSw_LST1NSM1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1NSM1A1 = _H3cevtModuleSw_LST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 474)
)
_H3cevtModuleSw_LST1LB1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1LB1A1 = _H3cevtModuleSw_LST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 475)
)
_H3cevtModuleSw_LST1ACG1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1ACG1A1 = _H3cevtModuleSw_LST1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 476)
)
_H3cevtModuleSw_LST1IPS1A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1IPS1A1 = _H3cevtModuleSw_LST1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 477)
)
_H3cevtModuleSw_LSR1DRUP1L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DRUP1L1 = _H3cevtModuleSw_LSR1DRUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 478)
)
_H3cevtModuleSw_LSR1DPUP1L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DPUP1L1 = _H3cevtModuleSw_LSR1DPUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 479)
)
_H3cevtModuleSw_LSR1DPSP4L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DPSP4L1 = _H3cevtModuleSw_LSR1DPSP4L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 480)
)
_H3cevtModuleSw_LSR1DTCP8L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DTCP8L1 = _H3cevtModuleSw_LSR1DTCP8L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 481)
)
_H3cevtModuleSw_LSR1DXP1L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DXP1L1 = _H3cevtModuleSw_LSR1DXP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 482)
)
_H3cevtModuleSw_LSR1DGP10L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DGP10L1 = _H3cevtModuleSw_LSR1DGP10L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 483)
)
_H3cevtModuleSw_LSR1LN1BNL1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1LN1BNL1 = _H3cevtModuleSw_LSR1LN1BNL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 484)
)
_H3cevtModuleSw_LSR1LN2BL1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1LN2BL1 = _H3cevtModuleSw_LSR1LN2BL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 485)
)
_H3cevtModuleSw_LSR1SRP2D1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1SRP2D1 = _H3cevtModuleSw_LSR1SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 486)
)
_H3cevtModuleSw_IM_NAT_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_NAT_II = _H3cevtModuleSw_IM_NAT_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 487)
)
_H3cevtModuleSw_IM_NAM_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_NAM_II = _H3cevtModuleSw_IM_NAM_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 488)
)
_H3cevtModuleSw_CR_MRP_I_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_MRP_I = _H3cevtModuleSw_CR_MRP_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 489)
)
_H3cevtModuleSw_CR_SF18C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SF18C = _H3cevtModuleSw_CR_SF18C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 490)
)
_H3cevtModuleSw_CR_SF08C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SF08C = _H3cevtModuleSw_CR_SF08C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 491)
)
_H3cevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_XP8LEF = _H3cevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 492)
)
_H3cevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_XP4LEF = _H3cevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 493)
)
_H3cevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_GP48LEF = _H3cevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 494)
)
_H3cevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_GT48LEF = _H3cevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 495)
)
_H3cevtModuleSw_CR_SPE_3020_E_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPE_3020_E = _H3cevtModuleSw_CR_SPE_3020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 496)
)
_H3cevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_PUP4L_E = _H3cevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 497)
)
_H3cevtModuleSw_LST1SF08C1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1SF08C1 = _H3cevtModuleSw_LST1SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 498)
)
_H3cevtModuleSw_LST1SF18C1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1SF18C1 = _H3cevtModuleSw_LST1SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 499)
)
_H3cevtModuleSw_LS81GP16TM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP16TM = _H3cevtModuleSw_LS81GP16TM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 500)
)
_H3cevtModuleSw_LS81VP4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81VP4C = _H3cevtModuleSw_LS81VP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 501)
)
_H3cevtModuleSw_LS8M1PT8P0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS8M1PT8P0 = _H3cevtModuleSw_LS8M1PT8P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 502)
)
_H3cevtModuleSw_LS8M1PT8GB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS8M1PT8GB0 = _H3cevtModuleSw_LS8M1PT8GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 503)
)
_H3cevtModuleSw_LS8M1PT4GB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS8M1PT4GB0 = _H3cevtModuleSw_LS8M1PT4GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 504)
)
_H3cevtModuleSw_LS81GP2R_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP2R = _H3cevtModuleSw_LS81GP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 505)
)
_H3cevtModuleSw_LS81GP4R_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP4R = _H3cevtModuleSw_LS81GP4R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 506)
)
_H3cevtModuleSw_LS81IPSECA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81IPSECA = _H3cevtModuleSw_LS81IPSECA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 507)
)
_H3cevtModuleSw_LS81FWA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81FWA = _H3cevtModuleSw_LS81FWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 508)
)
_H3cevtModuleSw_LS82VSNP_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS82VSNP = _H3cevtModuleSw_LS82VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 509)
)
_H3cevtModuleSw_LSQ1GV48SA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV48SA = _H3cevtModuleSw_LSQ1GV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 510)
)
_H3cevtModuleSw_LSQ1SRPB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPB = _H3cevtModuleSw_LSQ1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 511)
)
_H3cevtModuleSw_LSQ1SRP2XB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRP2XB = _H3cevtModuleSw_LSQ1SRP2XB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 512)
)
_H3cevtModuleSw_LSQ1SRP1CB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRP1CB = _H3cevtModuleSw_LSQ1SRP1CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 513)
)
_H3cevtModuleSw_LSQ1FV48SA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FV48SA = _H3cevtModuleSw_LSQ1FV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 514)
)
_H3cevtModuleSw_LSD1MPUA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1MPUA = _H3cevtModuleSw_LSD1MPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 515)
)
_H3cevtModuleSw_LSD1GP20A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP20A0 = _H3cevtModuleSw_LSD1GP20A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 516)
)
_H3cevtModuleSw_LSD1GP20TA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP20TA0 = _H3cevtModuleSw_LSD1GP20TA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 517)
)
_H3cevtModuleSw_LSD1GP36A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP36A0 = _H3cevtModuleSw_LSD1GP36A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 518)
)
_H3cevtModuleSw_LSD1GP20XA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP20XA0 = _H3cevtModuleSw_LSD1GP20XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 519)
)
_H3cevtModuleSw_LSD1GP20EA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP20EA0 = _H3cevtModuleSw_LSD1GP20EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 520)
)
_H3cevtModuleSw_LSD1GP20RA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP20RA0 = _H3cevtModuleSw_LSD1GP20RA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 521)
)
_H3cevtModuleSw_LSD1GP16A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP16A0 = _H3cevtModuleSw_LSD1GP16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 522)
)
_H3cevtModuleSw_LSD1GT16A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GT16A0 = _H3cevtModuleSw_LSD1GT16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 523)
)
_H3cevtModuleSw_LSD1XP2A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1XP2A0 = _H3cevtModuleSw_LSD1XP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 524)
)
_H3cevtModuleSw_LSD1EP2A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1EP2A0 = _H3cevtModuleSw_LSD1EP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 525)
)
_H3cevtModuleSw_LSD1RP2A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1RP2A0 = _H3cevtModuleSw_LSD1RP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 526)
)
_H3cevtModuleSw_LSQ1GV48SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV48SC = _H3cevtModuleSw_LSQ1GV48SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 527)
)
_H3cevtModuleSw_LSQ1FP48SA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FP48SA = _H3cevtModuleSw_LSQ1FP48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 528)
)
_H3cevtModuleSw_LSQ1GP24SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24SC = _H3cevtModuleSw_LSQ1GP24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 529)
)
_H3cevtModuleSw_LSQ1GT24SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GT24SC = _H3cevtModuleSw_LSQ1GT24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 530)
)
_H3cevtModuleSw_LSQ1TGX2SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX2SC = _H3cevtModuleSw_LSQ1TGX2SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 531)
)
_H3cevtModuleSw_LSQ1GP12EA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP12EA = _H3cevtModuleSw_LSQ1GP12EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 532)
)
_H3cevtModuleSw_LSQ1TGX1EA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX1EA = _H3cevtModuleSw_LSQ1TGX1EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 533)
)
_H3cevtModuleSw_LSQ1P24XGSC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1P24XGSC = _H3cevtModuleSw_LSQ1P24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 534)
)
_H3cevtModuleSw_LSQ1T24XGSC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1T24XGSC = _H3cevtModuleSw_LSQ1T24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 535)
)
_H3cevtModuleSw_LS81TGX1B_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81TGX1B = _H3cevtModuleSw_LS81TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 536)
)
_H3cevtModuleSw_LSQ1PT4PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1PT4PSC0 = _H3cevtModuleSw_LSQ1PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 537)
)
_H3cevtModuleSw_LS81SRPG13_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG13 = _H3cevtModuleSw_LS81SRPG13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 538)
)
_H3cevtModuleSw_LS81SRPG14_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG14 = _H3cevtModuleSw_LS81SRPG14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 539)
)
_H3cevtModuleSw_LS81SRPG15_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81SRPG15 = _H3cevtModuleSw_LS81SRPG15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 540)
)
_H3cevtModuleSw_LSQ1GP48SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP48SC0 = _H3cevtModuleSw_LSQ1GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 541)
)
_H3cevtModuleSw_LSQ1GP12SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP12SC0 = _H3cevtModuleSw_LSQ1GP12SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 542)
)
_H3cevtModuleSw_LSD1SRPA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1SRPA = _H3cevtModuleSw_LSD1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 543)
)
_H3cevtModuleSw_LSD1SRPB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1SRPB = _H3cevtModuleSw_LSD1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 544)
)
_H3cevtModuleSw_LSD1SRPC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1SRPC = _H3cevtModuleSw_LSD1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 545)
)
_H3cevtModuleSw_LSD1GT16PES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GT16PES0 = _H3cevtModuleSw_LSD1GT16PES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 546)
)
_H3cevtModuleSw_LSD1GP24ES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP24ES0 = _H3cevtModuleSw_LSD1GP24ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 547)
)
_H3cevtModuleSw_LSD1GT24XES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GT24XES0 = _H3cevtModuleSw_LSD1GT24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 548)
)
_H3cevtModuleSw_LSD1GP24XES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP24XES0 = _H3cevtModuleSw_LSD1GP24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 549)
)
_H3cevtModuleSw_LSD1XP2ES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1XP2ES0 = _H3cevtModuleSw_LSD1XP2ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 550)
)
_H3cevtModuleSw_LSD1GP48ES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP48ES0 = _H3cevtModuleSw_LSD1GP48ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 551)
)
_H3cevtModuleSw_LSQ1MPUA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUA0 = _H3cevtModuleSw_LSQ1MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 552)
)
_H3cevtModuleSw_LSQ1MPUA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUA1 = _H3cevtModuleSw_LSQ1MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 553)
)
_H3cevtModuleSw_LSQ1FWBSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FWBSC0 = _H3cevtModuleSw_LSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 554)
)
_H3cevtModuleSw_LSQ1PT8PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1PT8PSC0 = _H3cevtModuleSw_LSQ1PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 555)
)
_H3cevtModuleSw_LSQ1PT16PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1PT16PSC0 = _H3cevtModuleSw_LSQ1PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 556)
)
_H3cevtModuleSw_SA11MPUA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SA11MPUA0 = _H3cevtModuleSw_SA11MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 557)
)
_H3cevtModuleSw_SA11MPUB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SA11MPUB0 = _H3cevtModuleSw_SA11MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 558)
)
_H3cevtModuleSw_LSQ1AFCBSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1AFCBSC0 = _H3cevtModuleSw_LSQ1AFCBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 559)
)
_H3cevtModuleSw_LSQ1MPUB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUB0 = _H3cevtModuleSw_LSQ1MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 560)
)
_H3cevtModuleSw_LSQ1MPUB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUB1 = _H3cevtModuleSw_LSQ1MPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 561)
)
_H3cevtModuleSw_LSQ1PT4PSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1PT4PSC1 = _H3cevtModuleSw_LSQ1PT4PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 562)
)
_H3cevtModuleSw_LSQ1PT8PSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1PT8PSC1 = _H3cevtModuleSw_LSQ1PT8PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 563)
)
_H3cevtModuleSw_LSQ1PT16PSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1PT16PSC1 = _H3cevtModuleSw_LSQ1PT16PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 564)
)
_H3cevtModuleSw_LSQ1FP48USA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FP48USA0 = _H3cevtModuleSw_LSQ1FP48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 565)
)
_H3cevtModuleSw_LSQ1FP48USA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FP48USA1 = _H3cevtModuleSw_LSQ1FP48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 566)
)
_H3cevtModuleSw_LSQ1FV48USA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FV48USA0 = _H3cevtModuleSw_LSQ1FV48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 567)
)
_H3cevtModuleSw_LSQ1FV48USA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FV48USA1 = _H3cevtModuleSw_LSQ1FV48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 568)
)
_H3cevtModuleSw_LSQ1SRPD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPD0 = _H3cevtModuleSw_LSQ1SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 569)
)
_H3cevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1CGP24TSC0 = _H3cevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 570)
)
_H3cevtModuleSw_LSQ1GP24TSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TSC0 = _H3cevtModuleSw_LSQ1GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 571)
)
_H3cevtModuleSw_LSQ1ACGASC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1ACGASC0 = _H3cevtModuleSw_LSQ1ACGASC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 572)
)
_H3cevtModuleSw_LSD1XP1ES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1XP1ES0 = _H3cevtModuleSw_LSD1XP1ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 573)
)
_H3cevtModuleSw_LSD1GP12ES0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSD1GP12ES0 = _H3cevtModuleSw_LSD1GP12ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 574)
)
_H3cevtModuleSw_LSQ1SRP12GB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRP12GB0 = _H3cevtModuleSw_LSQ1SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 575)
)
_H3cevtModuleSw_LSQ1GV40PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV40PSC0 = _H3cevtModuleSw_LSQ1GV40PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 576)
)
_H3cevtModuleSw_LSQ1FWBSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FWBSC1 = _H3cevtModuleSw_LSQ1FWBSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 577)
)
_H3cevtModuleSw_LSQ1NSMSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1NSMSC0 = _H3cevtModuleSw_LSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 578)
)
_H3cevtModuleSw_LSQ1NSMSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1NSMSC1 = _H3cevtModuleSw_LSQ1NSMSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 579)
)
_H3cevtModuleSw_LSQ1AFDBSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1AFDBSC0 = _H3cevtModuleSw_LSQ1AFDBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 580)
)
_H3cevtModuleSw_LS81MPUB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81MPUB = _H3cevtModuleSw_LS81MPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 581)
)
_H3cevtModuleSw_LS81FP48XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81FP48XL = _H3cevtModuleSw_LS81FP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 582)
)
_H3cevtModuleSw_LS81FT48XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81FT48XL = _H3cevtModuleSw_LS81FT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 583)
)
_H3cevtModuleSw_LS81GP12XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP12XL = _H3cevtModuleSw_LS81GP12XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 584)
)
_H3cevtModuleSw_LS81GP24XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP24XL = _H3cevtModuleSw_LS81GP24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 585)
)
_H3cevtModuleSw_LS81GP48XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GP48XL = _H3cevtModuleSw_LS81GP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 586)
)
_H3cevtModuleSw_LS81GT24XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GT24XL = _H3cevtModuleSw_LS81GT24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 587)
)
_H3cevtModuleSw_LS81GT48XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81GT48XL = _H3cevtModuleSw_LS81GT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 588)
)
_H3cevtModuleSw_LS81TGX2XL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS81TGX2XL = _H3cevtModuleSw_LS81TGX2XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 589)
)
_H3cevtModuleSw_LSQ1GV48SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV48SD0 = _H3cevtModuleSw_LSQ1GV48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 590)
)
_H3cevtModuleSw_LSQ1GP48EB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP48EB0 = _H3cevtModuleSw_LSQ1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 591)
)
_H3cevtModuleSw_LSQ1IPSSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1IPSSC0 = _H3cevtModuleSw_LSQ1IPSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 592)
)
_H3cevtModuleSw_LSQ1GV48SD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV48SD1 = _H3cevtModuleSw_LSQ1GV48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 593)
)
_H3cevtModuleSw_LSQ1GP48SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP48SD0 = _H3cevtModuleSw_LSQ1GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 594)
)
_H3cevtModuleSw_LSQ1GP48SD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP48SD1 = _H3cevtModuleSw_LSQ1GP48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 595)
)
_H3cevtModuleSw_LSQ1SRPA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPA0 = _H3cevtModuleSw_LSQ1SRPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 596)
)
_H3cevtModuleSw_LSQ1SRPA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPA1 = _H3cevtModuleSw_LSQ1SRPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 597)
)
_H3cevtModuleSw_LSQ2FP48SA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ2FP48SA0 = _H3cevtModuleSw_LSQ2FP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 598)
)
_H3cevtModuleSw_LSQ2FP48SA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ2FP48SA1 = _H3cevtModuleSw_LSQ2FP48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 599)
)
_H3cevtModuleSw_LSQ2FT48SA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ2FT48SA0 = _H3cevtModuleSw_LSQ2FT48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 600)
)
_H3cevtModuleSw_LSQ2FT48SA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ2FT48SA1 = _H3cevtModuleSw_LSQ2FT48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 601)
)
_H3cevtModuleSw_LSQ1GV24PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV24PSC0 = _H3cevtModuleSw_LSQ1GV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 602)
)
_H3cevtModuleSw_LSQ1GV24PSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV24PSC1 = _H3cevtModuleSw_LSQ1GV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 603)
)
_H3cevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1CGV24PSC0 = _H3cevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 604)
)
_H3cevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1CGV24PSC1 = _H3cevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 605)
)
_H3cevtModuleSw_LSQ1GP24TEB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TEB0 = _H3cevtModuleSw_LSQ1GP24TEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 606)
)
_H3cevtModuleSw_LSQ1GP24TEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TEB1 = _H3cevtModuleSw_LSQ1GP24TEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 607)
)
_H3cevtModuleSw_LSQ1GP24TSD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TSD0 = _H3cevtModuleSw_LSQ1GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 608)
)
_H3cevtModuleSw_LSQ1GP24TSD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TSD1 = _H3cevtModuleSw_LSQ1GP24TSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 609)
)
_H3cevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TXSD0 = _H3cevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 610)
)
_H3cevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TXSD1 = _H3cevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 611)
)
_H3cevtModuleSw_LSQ1TGX2EB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX2EB0 = _H3cevtModuleSw_LSQ1TGX2EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 612)
)
_H3cevtModuleSw_LSQ1TGX2EB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX2EB1 = _H3cevtModuleSw_LSQ1TGX2EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 613)
)
_H3cevtModuleSw_LSQ1TGX2SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX2SD0 = _H3cevtModuleSw_LSQ1TGX2SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 614)
)
_H3cevtModuleSw_LSQ1TGX2SD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX2SD1 = _H3cevtModuleSw_LSQ1TGX2SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 615)
)
_H3cevtModuleSw_LSQ1TGX4SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX4SD0 = _H3cevtModuleSw_LSQ1TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 616)
)
_H3cevtModuleSw_LSQ1TGX4SD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX4SD1 = _H3cevtModuleSw_LSQ1TGX4SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 617)
)
_H3cevtModuleSw_LSQ1TGX8SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX8SD0 = _H3cevtModuleSw_LSQ1TGX8SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 618)
)
_H3cevtModuleSw_LSQ1TGX8SD1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX8SD1 = _H3cevtModuleSw_LSQ1TGX8SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 619)
)
_H3cevtModuleSw_LSQ1GP48EB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP48EB1 = _H3cevtModuleSw_LSQ1GP48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 620)
)
_H3cevtModuleSw_LSQ1TGX4EB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX4EB0 = _H3cevtModuleSw_LSQ1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 621)
)
_H3cevtModuleSw_LSQ1TGX4EB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGX4EB1 = _H3cevtModuleSw_LSQ1TGX4EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 622)
)
_H3cevtModuleSw_LSQ1GP12SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP12SC3 = _H3cevtModuleSw_LSQ1GP12SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 623)
)
_H3cevtModuleSw_LSQ1GP24TSC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TSC3 = _H3cevtModuleSw_LSQ1GP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 624)
)
_H3cevtModuleSw_LSQ1GP48SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP48SC3 = _H3cevtModuleSw_LSQ1GP48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 625)
)
_H3cevtModuleSw_LSQ1GV48SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV48SC3 = _H3cevtModuleSw_LSQ1GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 626)
)
_H3cevtModuleSw_LSQ1MPUA3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUA3 = _H3cevtModuleSw_LSQ1MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 627)
)
_H3cevtModuleSw_LSQ1SRP1CB3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRP1CB3 = _H3cevtModuleSw_LSQ1SRP1CB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 628)
)
_H3cevtModuleSw_LSQ1SRPA3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPA3 = _H3cevtModuleSw_LSQ1SRPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 629)
)
_H3cevtModuleSw_LSQ2FP48SA3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ2FP48SA3 = _H3cevtModuleSw_LSQ2FP48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 630)
)
_H3cevtModuleSw_LSQ2FT48SA3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ2FT48SA3 = _H3cevtModuleSw_LSQ2FT48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 631)
)
_H3cevtModuleSw_LSQ1MPUB3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUB3 = _H3cevtModuleSw_LSQ1MPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 632)
)
_H3cevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1CGP24TSC3 = _H3cevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 633)
)
_H3cevtModuleSw_LSQ1MPUB4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1MPUB4 = _H3cevtModuleSw_LSQ1MPUB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 634)
)
_H3cevtModuleSw_LSQ1SRPD4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPD4 = _H3cevtModuleSw_LSQ1SRPD4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 635)
)
_H3cevtModuleSw_LSQ1SSLSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SSLSC0 = _H3cevtModuleSw_LSQ1SSLSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 636)
)
_H3cevtModuleSw_LSQ1LBSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1LBSC0 = _H3cevtModuleSw_LSQ1LBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 637)
)
_H3cevtModuleSw_LSQ1NAT24SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1NAT24SC0 = _H3cevtModuleSw_LSQ1NAT24SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 638)
)
_H3cevtModuleSw_LSQ1SRP12GB4_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRP12GB4 = _H3cevtModuleSw_LSQ1SRP12GB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 639)
)
_H3cevtModuleSw_LSQ1TGS8SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGS8SC0 = _H3cevtModuleSw_LSQ1TGS8SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 640)
)
_H3cevtModuleSw_LSQ3PT4PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ3PT4PSC0 = _H3cevtModuleSw_LSQ3PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 641)
)
_H3cevtModuleSw_EWPXM2MPUB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2MPUB0 = _H3cevtModuleSw_EWPXM2MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 642)
)
_H3cevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2SRP12GB0 = _H3cevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 643)
)
_H3cevtModuleSw_EWPXM2SRPD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2SRPD0 = _H3cevtModuleSw_EWPXM2SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 644)
)
_H3cevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2GP24TSD0 = _H3cevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 645)
)
_H3cevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2GP24TXSD0 = _H3cevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 646)
)
_H3cevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2TGX4SD0 = _H3cevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 647)
)
_H3cevtModuleSw_EWPXM2GP48SD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2GP48SD0 = _H3cevtModuleSw_EWPXM2GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 648)
)
_H3cevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2GP24TSC0 = _H3cevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 649)
)
_H3cevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2TGX2SC0 = _H3cevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 650)
)
_H3cevtModuleSw_EWPXM2GP48SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM2GP48SC0 = _H3cevtModuleSw_EWPXM2GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 651)
)
_H3cevtModuleSw_LS7500_GP48_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_GP48_SC = _H3cevtModuleSw_LS7500_GP48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 652)
)
_H3cevtModuleSw_LS7500_GP48_SD_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_GP48_SD = _H3cevtModuleSw_LS7500_GP48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 653)
)
_H3cevtModuleSw_LS7500_GT48_SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_GT48_SC = _H3cevtModuleSw_LS7500_GT48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 654)
)
_H3cevtModuleSw_LS7500_GT48_SD_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_GT48_SD = _H3cevtModuleSw_LS7500_GT48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 655)
)
_H3cevtModuleSw_LS7500_SRPG1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_SRPG1 = _H3cevtModuleSw_LS7500_SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 656)
)
_H3cevtModuleSw_LS7500_SRPG2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_SRPG2 = _H3cevtModuleSw_LS7500_SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 657)
)
_H3cevtModuleSw_LS7500_XP4_SD_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_XP4_SD = _H3cevtModuleSw_LS7500_XP4_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 658)
)
_H3cevtModuleSw_LS7500_XP8_SD_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS7500_XP8_SD = _H3cevtModuleSw_LS7500_XP8_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 659)
)
_H3cevtModuleSw_LSQ4PT4PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ4PT4PSC0 = _H3cevtModuleSw_LSQ4PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 660)
)
_H3cevtModuleSw_LSQ4PT8PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ4PT8PSC0 = _H3cevtModuleSw_LSQ4PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 661)
)
_H3cevtModuleSw_LSQ4PT16PSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ4PT16PSC0 = _H3cevtModuleSw_LSQ4PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 662)
)
_H3cevtModuleSw_LSQ1GP24TSA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GP24TSA0 = _H3cevtModuleSw_LSQ1GP24TSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 663)
)
_H3cevtModuleSw_LSQ1GV24PSA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GV24PSA0 = _H3cevtModuleSw_LSQ1GV24PSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 664)
)
_H3cevtModuleSw_LSQ1SRPD3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SRPD3 = _H3cevtModuleSw_LSQ1SRPD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 665)
)
_H3cevtModuleSw_LSQ1SUPA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SUPA0 = _H3cevtModuleSw_LSQ1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 666)
)
_H3cevtModuleSw_LSU1FAB04A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB04A0 = _H3cevtModuleSw_LSU1FAB04A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 667)
)
_H3cevtModuleSw_LSU1FAB08A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB08A0 = _H3cevtModuleSw_LSU1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 668)
)
_H3cevtModuleSw_LSU1TGS8EA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGS8EA0 = _H3cevtModuleSw_LSU1TGS8EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 669)
)
_H3cevtModuleSw_LSU1TGS8EB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGS8EB0 = _H3cevtModuleSw_LSU1TGS8EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 670)
)
_H3cevtModuleSw_LSU1TGS8SE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGS8SE0 = _H3cevtModuleSw_LSU1TGS8SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 671)
)
_H3cevtModuleSw_LSUTGS16SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSUTGS16SC0 = _H3cevtModuleSw_LSUTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 672)
)
_H3cevtModuleSw_LUS1SUPA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LUS1SUPA0 = _H3cevtModuleSw_LUS1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 673)
)
_H3cevtModuleSw_LSU1GP24TXEA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP24TXEA0 = _H3cevtModuleSw_LSU1GP24TXEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 674)
)
_H3cevtModuleSw_LSU1GP24TXEB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP24TXEB0 = _H3cevtModuleSw_LSU1GP24TXEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 675)
)
_H3cevtModuleSw_LSU1GP24TXSE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP24TXSE0 = _H3cevtModuleSw_LSU1GP24TXSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 676)
)
_H3cevtModuleSw_LSU1GP48EA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP48EA0 = _H3cevtModuleSw_LSU1GP48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 677)
)
_H3cevtModuleSw_LSU1GP48EB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP48EB0 = _H3cevtModuleSw_LSU1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 678)
)
_H3cevtModuleSw_LSU1GP48SE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP48SE0 = _H3cevtModuleSw_LSU1GP48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 679)
)
_H3cevtModuleSw_LSU1GT48EA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GT48EA0 = _H3cevtModuleSw_LSU1GT48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 680)
)
_H3cevtModuleSw_LSU1GT48SE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GT48SE0 = _H3cevtModuleSw_LSU1GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 681)
)
_H3cevtModuleSw_LSU1TGX4EA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGX4EA0 = _H3cevtModuleSw_LSU1TGX4EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 682)
)
_H3cevtModuleSw_LSU1TGX4EB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGX4EB0 = _H3cevtModuleSw_LSU1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 683)
)
_H3cevtModuleSw_LSU1TGX4SE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGX4SE0 = _H3cevtModuleSw_LSU1TGX4SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 684)
)
_H3cevtModuleSw_LSQ1FAB08A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB08A0 = _H3cevtModuleSw_LSQ1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 685)
)
_H3cevtModuleSw_EWPX2WCMD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX2WCMD0 = _H3cevtModuleSw_EWPX2WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 686)
)
_H3cevtModuleSw_LSQ1WCMD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1WCMD0 = _H3cevtModuleSw_LSQ1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 687)
)
_H3cevtModuleSw_LSQ1IAGSC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1IAGSC0 = _H3cevtModuleSw_LSQ1IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 688)
)
_H3cevtModuleSw_LSU1GP24TSE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1GP24TSE0 = _H3cevtModuleSw_LSU1GP24TSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 689)
)
_H3cevtModuleSw_LSQ1TGS16SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGS16SC0 = _H3cevtModuleSw_LSQ1TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 690)
)
_H3cevtModuleSw_EWPX2TGS16SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX2TGS16SC0 = _H3cevtModuleSw_EWPX2TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 691)
)
_H3cevtModuleSw_LSQ1SUPA3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1SUPA3 = _H3cevtModuleSw_LSQ1SUPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 692)
)
_H3cevtModuleSw_LSQ1FAB04A3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB04A3 = _H3cevtModuleSw_LSQ1FAB04A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 693)
)
_H3cevtModuleSw_LSQ1FAB08A3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB08A3 = _H3cevtModuleSw_LSQ1FAB08A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 694)
)
_H3cevtModuleSw_LSQ1GT48SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1GT48SC0 = _H3cevtModuleSw_LSQ1GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 695)
)
_H3cevtModuleSw_LSR2SRP2C1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2SRP2C1 = _H3cevtModuleSw_LSR2SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 696)
)
_H3cevtModuleSw_LSR2SRP2C2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2SRP2C2 = _H3cevtModuleSw_LSR2SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 697)
)
_H3cevtModuleSw_1000BASE_X_COMBO_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_X_COMBO = _H3cevtModuleSw_1000BASE_X_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 701)
)
_H3cevtModuleSw_EPON_1000M_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EPON_1000M = _H3cevtModuleSw_EPON_1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 702)
)
_H3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45 = _H3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 703)
)
_H3cevtModuleSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_1550_BIDI = _H3cevtModuleSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 704)
)
_H3cevtModuleSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_100M_1310_BIDI = _H3cevtModuleSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 705)
)
_H3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO = _H3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 706)
)
_H3cevtModuleSw_LSH1PK2T_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSH1PK2T = _H3cevtModuleSw_LSH1PK2T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 707)
)
_H3cevtModuleSw_LSPM2GP2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSPM2GP2P = _H3cevtModuleSw_LSPM2GP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 708)
)
_H3cevtModuleSw_LSWM1GT16P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1GT16P = _H3cevtModuleSw_LSWM1GT16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 709)
)
_H3cevtModuleSw_LSWM1GP16P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1GP16P = _H3cevtModuleSw_LSWM1GP16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 710)
)
_H3cevtModuleSw_LSWM1XP2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1XP2P = _H3cevtModuleSw_LSWM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 711)
)
_H3cevtModuleSw_LSWM1XP4P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1XP4P = _H3cevtModuleSw_LSWM1XP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 712)
)
_H3cevtModuleSw_LSWM1SP2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1SP2P = _H3cevtModuleSw_LSWM1SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 713)
)
_H3cevtModuleSw_LSWM1SP4P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1SP4P = _H3cevtModuleSw_LSWM1SP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 714)
)
_H3cevtModuleSw_LSWM148POEM_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM148POEM = _H3cevtModuleSw_LSWM148POEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 715)
)
_H3cevtModuleSw_LSWM1FW10_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1FW10 = _H3cevtModuleSw_LSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 716)
)
_H3cevtModuleSw_LSWM1WCM10_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1WCM10 = _H3cevtModuleSw_LSWM1WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 717)
)
_H3cevtModuleSw_LSWM1IPS10_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1IPS10 = _H3cevtModuleSw_LSWM1IPS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 718)
)
_H3cevtModuleSw_LSWM1WCM20_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1WCM20 = _H3cevtModuleSw_LSWM1WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 719)
)
_H3cevtModuleSw_IPS_T1000_M_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IPS_T1000_M = _H3cevtModuleSw_IPS_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 720)
)
_H3cevtModuleSw_IPS_T1000_A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IPS_T1000_A = _H3cevtModuleSw_IPS_T1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 721)
)
_H3cevtModuleSw_IPS_T1000_S_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IPS_T1000_S = _H3cevtModuleSw_IPS_T1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 722)
)
_H3cevtModuleSw_IPS_GX4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IPS_GX4C = _H3cevtModuleSw_IPS_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 723)
)
_H3cevtModuleSw_IPS_GT4C_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IPS_GT4C = _H3cevtModuleSw_IPS_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 724)
)
_H3cevtModuleSw_LSPM2SP2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSPM2SP2P = _H3cevtModuleSw_LSPM2SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 725)
)
_H3cevtModuleSw_LSPM2SP2PA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSPM2SP2PA = _H3cevtModuleSw_LSPM2SP2PA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 726)
)
_H3cevtModuleSw_LSP5GP8P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSP5GP8P = _H3cevtModuleSw_LSP5GP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 727)
)
_H3cevtModuleSw_LSP5GT8P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSP5GT8P = _H3cevtModuleSw_LSP5GT8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 728)
)
_H3cevtModuleSw_LSWM1FC4P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSWM1FC4P = _H3cevtModuleSw_LSWM1FC4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 729)
)
_H3cevtModuleSw_LSW1XGT4P0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSW1XGT4P0 = _H3cevtModuleSw_LSW1XGT4P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 730)
)
_H3cevtModuleSw_LSW1XGT2P0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSW1XGT2P0 = _H3cevtModuleSw_LSW1XGT2P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 731)
)
_H3cevtModuleSw_LSP1XGT2P_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSP1XGT2P = _H3cevtModuleSw_LSP1XGT2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 732)
)
_H3cevtModuleSw_WX5002MPU_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_WX5002MPU = _H3cevtModuleSw_WX5002MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 800)
)
_H3cevtModuleSw_LS8M1WCMA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LS8M1WCMA = _H3cevtModuleSw_LS8M1WCMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 801)
)
_H3cevtModuleSw_EWPX1G24XA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1G24XA0 = _H3cevtModuleSw_EWPX1G24XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 802)
)
_H3cevtModuleSw_LSQ1WCMB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1WCMB0 = _H3cevtModuleSw_LSQ1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 803)
)
_H3cevtModuleSw_LSB1WCM2A0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSB1WCM2A0 = _H3cevtModuleSw_LSB1WCM2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 804)
)
_H3cevtModuleSw_EWPX1WCMB0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1WCMB0 = _H3cevtModuleSw_EWPX1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 805)
)
_H3cevtModuleSw_EWPX1G24XC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1G24XC0 = _H3cevtModuleSw_EWPX1G24XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 806)
)
_H3cevtModuleSw_EWPX1WCMC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1WCMC0 = _H3cevtModuleSw_EWPX1WCMC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 807)
)
_H3cevtModuleSw_EWPX1FWA0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1FWA0 = _H3cevtModuleSw_EWPX1FWA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 808)
)
_H3cevtModuleSw_EWPX1G10XC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1G10XC0 = _H3cevtModuleSw_EWPX1G10XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 809)
)
_H3cevtModuleSw_EWPX1WCM10C0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1WCM10C0 = _H3cevtModuleSw_EWPX1WCM10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 810)
)
_H3cevtModuleSw_LSR1WCM2A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1WCM2A1 = _H3cevtModuleSw_LSR1WCM2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 811)
)
_H3cevtModuleSw_EWPX1WAP0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1WAP0 = _H3cevtModuleSw_EWPX1WAP0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 812)
)
_H3cevtModuleSw_EWPX1WCMD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1WCMD0 = _H3cevtModuleSw_EWPX1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 813)
)
_H3cevtModuleSw_EWPX1G24XCE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1G24XCE0 = _H3cevtModuleSw_EWPX1G24XCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 814)
)
_H3cevtModuleSw_EWPX1WCMCE0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX1WCMCE0 = _H3cevtModuleSw_EWPX1WCMCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 815)
)
_H3cevtModuleSw_LSR1DRSP2L1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1DRSP2L1 = _H3cevtModuleSw_LSR1DRSP2L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 900)
)
_H3cevtModuleSw_PIC_CLF2G8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PIC_CLF2G8L = _H3cevtModuleSw_PIC_CLF2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 901)
)
_H3cevtModuleSw_PIC_CLF4G8L_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_PIC_CLF4G8L = _H3cevtModuleSw_PIC_CLF4G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 902)
)
_H3cevtModuleSw_SR02SRP2F3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRP2F3 = _H3cevtModuleSw_SR02SRP2F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 903)
)
_H3cevtModuleSw_SR02SRP1F3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRP1F3 = _H3cevtModuleSw_SR02SRP1F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 904)
)
_H3cevtModuleSw_LST1GT48LEA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GT48LEA1 = _H3cevtModuleSw_LST1GT48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 905)
)
_H3cevtModuleSw_LST1GP48LEA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GP48LEA1 = _H3cevtModuleSw_LST1GP48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 906)
)
_H3cevtModuleSw_LST2XP8LEA1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP8LEA1 = _H3cevtModuleSw_LST2XP8LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 907)
)
_H3cevtModuleSw_LST1GT48LEY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GT48LEY1 = _H3cevtModuleSw_LST1GT48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 908)
)
_H3cevtModuleSw_LST1GP48LEY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GP48LEY1 = _H3cevtModuleSw_LST1GP48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 909)
)
_H3cevtModuleSw_LST1XP32REY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP32REY1 = _H3cevtModuleSw_LST1XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 910)
)
_H3cevtModuleSw_LST1XP8LEY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP8LEY1 = _H3cevtModuleSw_LST1XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 911)
)
_H3cevtModuleSw_LST1GP48LEZ1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1GP48LEZ1 = _H3cevtModuleSw_LST1GP48LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 912)
)
_H3cevtModuleSw_LST1XP8LEZ1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP8LEZ1 = _H3cevtModuleSw_LST1XP8LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 913)
)
_H3cevtModuleSw_IM_FW_II_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_FW_II = _H3cevtModuleSw_IM_FW_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 914)
)
_H3cevtModuleSw_IM_IPS_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_IPS = _H3cevtModuleSw_IM_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 915)
)
_H3cevtModuleSw_IM_SSL_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_SSL = _H3cevtModuleSw_IM_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 916)
)
_H3cevtModuleSw_IM_LB_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_LB = _H3cevtModuleSw_IM_LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 917)
)
_H3cevtModuleSw_IM_ACG_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_IM_ACG = _H3cevtModuleSw_IM_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 918)
)
_H3cevtModuleSw_LSR1XP16REC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1XP16REC1 = _H3cevtModuleSw_LSR1XP16REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 919)
)
_H3cevtModuleSw_LST2XP8LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP8LEB1 = _H3cevtModuleSw_LST2XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 920)
)
_H3cevtModuleSw_LST2XP8LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP8LEC1 = _H3cevtModuleSw_LST2XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 921)
)
_H3cevtModuleSw_LST2XP8LEF1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP8LEF1 = _H3cevtModuleSw_LST2XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 922)
)
_H3cevtModuleSw_LSR2XP4LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2XP4LEB1 = _H3cevtModuleSw_LSR2XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 923)
)
_H3cevtModuleSw_LSR2XP4LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2XP4LEC1 = _H3cevtModuleSw_LSR2XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 924)
)
_H3cevtModuleSw_LST2XP32REB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP32REB1 = _H3cevtModuleSw_LST2XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 925)
)
_H3cevtModuleSw_LST2XP32REC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP32REC1 = _H3cevtModuleSw_LST2XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 926)
)
_H3cevtModuleSw_LSR1WCM3A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR1WCM3A1 = _H3cevtModuleSw_LSR1WCM3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 927)
)
_H3cevtModuleSw_LST1XP16LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP16LEB1 = _H3cevtModuleSw_LST1XP16LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 928)
)
_H3cevtModuleSw_LST1XP16LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP16LEC1 = _H3cevtModuleSw_LST1XP16LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 929)
)
_H3cevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_XP4L_E_I = _H3cevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 930)
)
_H3cevtModuleSw_LST2MRPNC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2MRPNC1 = _H3cevtModuleSw_LST2MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 931)
)
_H3cevtModuleSw_LST2SF08C1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2SF08C1 = _H3cevtModuleSw_LST2SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 932)
)
_H3cevtModuleSw_LST2SF18C1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2SF18C1 = _H3cevtModuleSw_LST2SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 933)
)
_H3cevtModuleSw_SR02SRP2G3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR02SRP2G3 = _H3cevtModuleSw_SR02SRP2G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 934)
)
_H3cevtModuleSw_CR_SPE_3020_E_I_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPE_3020_E_I = _H3cevtModuleSw_CR_SPE_3020_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 935)
)
_H3cevtModuleSw_CR_SPC_PUP4L_E_I_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_PUP4L_E_I = _H3cevtModuleSw_CR_SPC_PUP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 936)
)
_H3cevtModuleSw_CR_SPC_XP4LEF_I_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_XP4LEF_I = _H3cevtModuleSw_CR_SPC_XP4LEF_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 937)
)
_H3cevtModuleSw_CR_SPC_XP8LEF_I_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_SPC_XP8LEF_I = _H3cevtModuleSw_CR_SPC_XP8LEF_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 938)
)
_H3cevtModuleSw_LST3XP8LEB1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST3XP8LEB1 = _H3cevtModuleSw_LST3XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 939)
)
_H3cevtModuleSw_LST3XP8LEC1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST3XP8LEC1 = _H3cevtModuleSw_LST3XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 940)
)
_H3cevtModuleSw_LST1FW3A1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1FW3A1 = _H3cevtModuleSw_LST1FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 941)
)
_H3cevtModuleSw_CR_IM_NAM1A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_IM_NAM1A = _H3cevtModuleSw_CR_IM_NAM1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 942)
)
_H3cevtModuleSw_LSR2SRP2B1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2SRP2B1 = _H3cevtModuleSw_LSR2SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 943)
)
_H3cevtModuleSw_LSR2SRP2B2_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2SRP2B2 = _H3cevtModuleSw_LSR2SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 944)
)
_H3cevtModuleSw_LSR2SRP2D1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSR2SRP2D1 = _H3cevtModuleSw_LSR2SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 945)
)
_H3cevtModuleSw_LST3XP8LEY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST3XP8LEY1 = _H3cevtModuleSw_LST3XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 946)
)
_H3cevtModuleSw_LST2XP32REY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST2XP32REY1 = _H3cevtModuleSw_LST2XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 947)
)
_H3cevtModuleSw_LST1XP16LEY1_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LST1XP16LEY1 = _H3cevtModuleSw_LST1XP16LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 948)
)
_H3cevtModuleSw_SR0M2SRP2G3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR0M2SRP2G3 = _H3cevtModuleSw_SR0M2SRP2G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 949)
)
_H3cevtModuleSw_SR0M2SRP1G3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SR0M2SRP1G3 = _H3cevtModuleSw_SR0M2SRP1G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 950)
)
_H3cevtModuleSw_SPC_GP48LA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GP48LA = _H3cevtModuleSw_SPC_GP48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 951)
)
_H3cevtModuleSw_SPC_GT48LA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GT48LA = _H3cevtModuleSw_SPC_GT48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 952)
)
_H3cevtModuleSw_SPC_XP4LA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_XP4LA = _H3cevtModuleSw_SPC_XP4LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 953)
)
_H3cevtModuleSw_SPC_XP2LA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_XP2LA = _H3cevtModuleSw_SPC_XP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 954)
)
_H3cevtModuleSw_SPC_GP24LA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_GP24LA = _H3cevtModuleSw_SPC_GP24LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 955)
)
_H3cevtModuleSw_SPC_XP16RA_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_SPC_XP16RA = _H3cevtModuleSw_SPC_XP16RA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 956)
)
_H3cevtModuleSw_CR_IM_FW1A_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_CR_IM_FW1A = _H3cevtModuleSw_CR_IM_FW1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 957)
)
_H3cevtModuleSw_LSU1QGC4SF0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1QGC4SF0 = _H3cevtModuleSw_LSU1QGC4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1201)
)
_H3cevtModuleSw_LSU1QGS8SF0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1QGS8SF0 = _H3cevtModuleSw_LSU1QGS8SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1202)
)
_H3cevtModuleSw_LSU1TGS48SF0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGS48SF0 = _H3cevtModuleSw_LSU1TGS48SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1203)
)
_H3cevtModuleSw_LSU1QGS4SF0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1QGS4SF0 = _H3cevtModuleSw_LSU1QGS4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1204)
)
_H3cevtModuleSw_LSU1TGS32SF0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGS32SF0 = _H3cevtModuleSw_LSU1TGS32SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1205)
)
_H3cevtModuleSw_LSU1FAB08D0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB08D0 = _H3cevtModuleSw_LSU1FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1206)
)
_H3cevtModuleSw_LSU1FAB04B0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB04B0 = _H3cevtModuleSw_LSU1FAB04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1207)
)
_H3cevtModuleSw_LSU1FAB08B0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB08B0 = _H3cevtModuleSw_LSU1FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1208)
)
_H3cevtModuleSw_LSU1FAB12D0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB12D0 = _H3cevtModuleSw_LSU1FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1209)
)
_H3cevtModuleSw_LSU1FAB12B0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB12B0 = _H3cevtModuleSw_LSU1FAB12B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1210)
)
_H3cevtModuleSw_LSU1FAB04D0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1FAB04D0 = _H3cevtModuleSw_LSU1FAB04D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1211)
)
_H3cevtModuleSw_LSQ1CTGS16SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1CTGS16SC0 = _H3cevtModuleSw_LSQ1CTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1212)
)
_H3cevtModuleSw_EWPX2CTGS16SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX2CTGS16SC0 = _H3cevtModuleSw_EWPX2CTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1213)
)
_H3cevtModuleSw_LSUM3WCMD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSUM3WCMD0 = _H3cevtModuleSw_LSUM3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1214)
)
_H3cevtModuleSw_EWPXM3WCMD0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPXM3WCMD0 = _H3cevtModuleSw_EWPXM3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1215)
)
_H3cevtModuleSw_LSQ1QGS4SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1QGS4SC0 = _H3cevtModuleSw_LSQ1QGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1216)
)
_H3cevtModuleSw_LSQ1QGC4SC0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1QGC4SC0 = _H3cevtModuleSw_LSQ1QGC4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1217)
)
_H3cevtModuleSw_LSU1TGT24SF0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSU1TGT24SF0 = _H3cevtModuleSw_LSU1TGT24SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1218)
)
_H3cevtModuleSw_LSQ1QGS8SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1QGS8SC3 = _H3cevtModuleSw_LSQ1QGS8SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1219)
)
_H3cevtModuleSw_LSQ1TGS32SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGS32SC3 = _H3cevtModuleSw_LSQ1TGS32SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1220)
)
_H3cevtModuleSw_LSQ1QGS4SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1QGS4SC3 = _H3cevtModuleSw_LSQ1QGS4SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1221)
)
_H3cevtModuleSw_LSQ1TGS48SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGS48SC3 = _H3cevtModuleSw_LSQ1TGS48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1222)
)
_H3cevtModuleSw_LSQ1QGC4SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1QGC4SC3 = _H3cevtModuleSw_LSQ1QGC4SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1223)
)
_H3cevtModuleSw_LSQ1FAB12D3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB12D3 = _H3cevtModuleSw_LSQ1FAB12D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1224)
)
_H3cevtModuleSw_LSQ1FAB08D3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB08D3 = _H3cevtModuleSw_LSQ1FAB08D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1225)
)
_H3cevtModuleSw_LSQ1FAB04D3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB04D3 = _H3cevtModuleSw_LSQ1FAB04D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1226)
)
_H3cevtModuleSw_LSQ1TGS8EB3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGS8EB3 = _H3cevtModuleSw_LSQ1TGS8EB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1227)
)
_H3cevtModuleSw_LSQ1TGT24SC3_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1TGT24SC3 = _H3cevtModuleSw_LSQ1TGT24SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1228)
)
_H3cevtModuleSw_LSQ1FAB08B0_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_LSQ1FAB08B0 = _H3cevtModuleSw_LSQ1FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1229)
)
_H3cevtModuleSw_EWPX2CTGS16SC_ObjectIdentity = ObjectIdentity
h3cevtModuleSw_EWPX2CTGS16SC = _H3cevtModuleSw_EWPX2CTGS16SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 4, 1230)
)
_H3cevtSubModuleRouter_ObjectIdentity = ObjectIdentity
h3cevtSubModuleRouter = _H3cevtSubModuleRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 5)
)
_H3cevtSubModuleSwitch_ObjectIdentity = ObjectIdentity
h3cevtSubModuleSwitch = _H3cevtSubModuleSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 9, 6)
)
_H3cevtPort_ObjectIdentity = ObjectIdentity
h3cevtPort = _H3cevtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10)
)
_H3cevtPortUnknownPorts_ObjectIdentity = ObjectIdentity
h3cevtPortUnknownPorts = _H3cevtPortUnknownPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 1)
)
_H3cevtPortCommonPorts_ObjectIdentity = ObjectIdentity
h3cevtPortCommonPorts = _H3cevtPortCommonPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 2)
)
_H3cevtPortRouterType_ObjectIdentity = ObjectIdentity
h3cevtPortRouterType = _H3cevtPortRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3)
)
_H3cevtPortRt_Async_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Async = _H3cevtPortRt_Async_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 1)
)
_H3cevtPortRt_Analogmodem_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Analogmodem = _H3cevtPortRt_Analogmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 2)
)
_H3cevtPortRt_Atm_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Atm = _H3cevtPortRt_Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 3)
)
_H3cevtPortRt_AtmAdsl_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmAdsl = _H3cevtPortRt_AtmAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 4)
)
_H3cevtPortRt_AtmShdsl_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmShdsl = _H3cevtPortRt_AtmShdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 5)
)
_H3cevtPortRt_AtmE1_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmE1 = _H3cevtPortRt_AtmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 6)
)
_H3cevtPortRt_AtmT1_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmT1 = _H3cevtPortRt_AtmT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 7)
)
_H3cevtPortRt_AtmE3_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmE3 = _H3cevtPortRt_AtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 8)
)
_H3cevtPortRt_AtmT3_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmT3 = _H3cevtPortRt_AtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 9)
)
_H3cevtPortRt_Atm622M_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Atm622M = _H3cevtPortRt_Atm622M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 10)
)
_H3cevtPortRt_AtmImaE1_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmImaE1 = _H3cevtPortRt_AtmImaE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 11)
)
_H3cevtPortRt_AtmImaT1_ObjectIdentity = ObjectIdentity
h3cevtPortRt_AtmImaT1 = _H3cevtPortRt_AtmImaT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 12)
)
_H3cevtPortRt_Atm25M_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Atm25M = _H3cevtPortRt_Atm25M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 13)
)
_H3cevtPortRt_Bri_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Bri = _H3cevtPortRt_Bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 14)
)
_H3cevtPortRt_Console_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Console = _H3cevtPortRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 15)
)
_H3cevtPortRt_E1_ObjectIdentity = ObjectIdentity
h3cevtPortRt_E1 = _H3cevtPortRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 16)
)
_H3cevtPortRt_E3_ObjectIdentity = ObjectIdentity
h3cevtPortRt_E3 = _H3cevtPortRt_E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 17)
)
_H3cevtPortRt_T1_ObjectIdentity = ObjectIdentity
h3cevtPortRt_T1 = _H3cevtPortRt_T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 18)
)
_H3cevtPortRt_T3_ObjectIdentity = ObjectIdentity
h3cevtPortRt_T3 = _H3cevtPortRt_T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 19)
)
_H3cevtPortRt_Cpos_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Cpos = _H3cevtPortRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 20)
)
_H3cevtPortRt_Ethernet_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Ethernet = _H3cevtPortRt_Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 21)
)
_H3cevtPortRt_Serial_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Serial = _H3cevtPortRt_Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 22)
)
_H3cevtPortRt_E1f_ObjectIdentity = ObjectIdentity
h3cevtPortRt_E1f = _H3cevtPortRt_E1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 23)
)
_H3cevtPortRt_T1f_ObjectIdentity = ObjectIdentity
h3cevtPortRt_T1f = _H3cevtPortRt_T1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 24)
)
_H3cevtPortRt_Pos_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Pos = _H3cevtPortRt_Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 25)
)
_H3cevtPortRt_Ge_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Ge = _H3cevtPortRt_Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 26)
)
_H3cevtPortRt_Aux_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Aux = _H3cevtPortRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 27)
)
_H3cevtPortRt_VG_Fxs_ObjectIdentity = ObjectIdentity
h3cevtPortRt_VG_Fxs = _H3cevtPortRt_VG_Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 30)
)
_H3cevtPortRt_VG_Fxo_ObjectIdentity = ObjectIdentity
h3cevtPortRt_VG_Fxo = _H3cevtPortRt_VG_Fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 31)
)
_H3cevtPortRt_VG_E1vi_ObjectIdentity = ObjectIdentity
h3cevtPortRt_VG_E1vi = _H3cevtPortRt_VG_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 32)
)
_H3cevtPortRt_VG_T1vi_ObjectIdentity = ObjectIdentity
h3cevtPortRt_VG_T1vi = _H3cevtPortRt_VG_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 33)
)
_H3cevtPortRt_Usb_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Usb = _H3cevtPortRt_Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 34)
)
_H3cevtPortRt_Ndec_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Ndec = _H3cevtPortRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 35)
)
_H3cevtPortRt_Cavium_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Cavium = _H3cevtPortRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 36)
)
_H3cevtPortRt_Fcm_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Fcm = _H3cevtPortRt_Fcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 37)
)
_H3cevtPortRt_E1vi_ObjectIdentity = ObjectIdentity
h3cevtPortRt_E1vi = _H3cevtPortRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 38)
)
_H3cevtPortRt_T1vi_ObjectIdentity = ObjectIdentity
h3cevtPortRt_T1vi = _H3cevtPortRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 39)
)
_H3cevtPortRt_Vi_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Vi = _H3cevtPortRt_Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 40)
)
_H3cevtPortRt_Adls2Plus_ObjectIdentity = ObjectIdentity
h3cevtPortRt_Adls2Plus = _H3cevtPortRt_Adls2Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 41)
)
_H3cevtPortRt_RADIO_AG_ObjectIdentity = ObjectIdentity
h3cevtPortRt_RADIO_AG = _H3cevtPortRt_RADIO_AG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 42)
)
_H3cevtPortRt_1exp_ObjectIdentity = ObjectIdentity
h3cevtPortRt_1exp = _H3cevtPortRt_1exp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 43)
)
_H3cevtPortRt_G_SHDSL_BIS_ObjectIdentity = ObjectIdentity
h3cevtPortRt_G_SHDSL_BIS = _H3cevtPortRt_G_SHDSL_BIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 44)
)
_H3cevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
h3cevtPortRt_ONU_1000BASE_BX_SFF_SC = _H3cevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 45)
)
_H3cevtPortRt_CELLULAR_ObjectIdentity = ObjectIdentity
h3cevtPortRt_CELLULAR = _H3cevtPortRt_CELLULAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 3, 46)
)
_H3cevtPortSwitchType_ObjectIdentity = ObjectIdentity
h3cevtPortSwitchType = _H3cevtPortSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4)
)
_H3cevtPortSw_10or100M_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10or100M = _H3cevtPortSw_10or100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 1)
)
_H3cevtPortSw_1000BaseLxSm_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseLxSm = _H3cevtPortSw_1000BaseLxSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 2)
)
_H3cevtPortSw_1000BaseSxMm_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseSxMm = _H3cevtPortSw_1000BaseSxMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 3)
)
_H3cevtPortSw_1000BaseTx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseTx = _H3cevtPortSw_1000BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 4)
)
_H3cevtPortSw_100MSinglemodeFx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MSinglemodeFx = _H3cevtPortSw_100MSinglemodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 5)
)
_H3cevtPortSw_100MMultimodeFx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MMultimodeFx = _H3cevtPortSw_100MMultimodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 6)
)
_H3cevtPortSw_100M100BaseTx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100M100BaseTx = _H3cevtPortSw_100M100BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 7)
)
_H3cevtPortSw_100MHub_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MHub = _H3cevtPortSw_100MHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 8)
)
_H3cevtPortSw_Vdsl_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Vdsl = _H3cevtPortSw_Vdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 9)
)
_H3cevtPortSw_Stack_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Stack = _H3cevtPortSw_Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 10)
)
_H3cevtPortSw_1000BaseZenithFx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseZenithFx = _H3cevtPortSw_1000BaseZenithFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 11)
)
_H3cevtPortSw_1000BaseLongFx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseLongFx = _H3cevtPortSw_1000BaseLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 12)
)
_H3cevtPortSw_Adsl_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Adsl = _H3cevtPortSw_Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 13)
)
_H3cevtPortSw_10or100MDb_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10or100MDb = _H3cevtPortSw_10or100MDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 14)
)
_H3cevtPortSw_10GBaseLrSm_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBaseLrSm = _H3cevtPortSw_10GBaseLrSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 15)
)
_H3cevtPortSw_10GBaseLx4Mm_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBaseLx4Mm = _H3cevtPortSw_10GBaseLx4Mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 16)
)
_H3cevtPortSw_10GBaseLx4Sm_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBaseLx4Sm = _H3cevtPortSw_10GBaseLx4Sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 17)
)
_H3cevtPortSw_100MLongFx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MLongFx = _H3cevtPortSw_100MLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 18)
)
_H3cevtPortSw_1000BaseCx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseCx = _H3cevtPortSw_1000BaseCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 19)
)
_H3cevtPortSw_1000BaseZenithFxLc_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseZenithFxLc = _H3cevtPortSw_1000BaseZenithFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 20)
)
_H3cevtPortSw_1000BaseLongFxLc_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BaseLongFxLc = _H3cevtPortSw_1000BaseLongFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 21)
)
_H3cevtPortSw_100MSmFxSc_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MSmFxSc = _H3cevtPortSw_100MSmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 22)
)
_H3cevtPortSw_100MMmFxSc_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MMmFxSc = _H3cevtPortSw_100MMmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 23)
)
_H3cevtPortSw_100MSmFxLc_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MSmFxLc = _H3cevtPortSw_100MSmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 24)
)
_H3cevtPortSw_100MMmFxLc_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100MMmFxLc = _H3cevtPortSw_100MMmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 25)
)
_H3cevtPortSw_GbicNoConnector_ObjectIdentity = ObjectIdentity
h3cevtPortSw_GbicNoConnector = _H3cevtPortSw_GbicNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 26)
)
_H3cevtPortSw_Gbic1000BaseT_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Gbic1000BaseT = _H3cevtPortSw_Gbic1000BaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 27)
)
_H3cevtPortSw_Gbic1000BaseLx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Gbic1000BaseLx = _H3cevtPortSw_Gbic1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 28)
)
_H3cevtPortSw_Gbic1000BaseSx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Gbic1000BaseSx = _H3cevtPortSw_Gbic1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 29)
)
_H3cevtPortSw_Gbic1000BaseZx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Gbic1000BaseZx = _H3cevtPortSw_Gbic1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 30)
)
_H3cevtPortSw_ComboNoConnector_ObjectIdentity = ObjectIdentity
h3cevtPortSw_ComboNoConnector = _H3cevtPortSw_ComboNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 31)
)
_H3cevtPortSw_Combo1000BaseLx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseLx = _H3cevtPortSw_Combo1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 32)
)
_H3cevtPortSw_Combo1000BaseLxFiber_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseLxFiber = _H3cevtPortSw_Combo1000BaseLxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 33)
)
_H3cevtPortSw_Combo1000BaseLxCopper_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseLxCopper = _H3cevtPortSw_Combo1000BaseLxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 34)
)
_H3cevtPortSw_Combo1000BaseSx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseSx = _H3cevtPortSw_Combo1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 35)
)
_H3cevtPortSw_Combo1000BaseSxFiber_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseSxFiber = _H3cevtPortSw_Combo1000BaseSxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 36)
)
_H3cevtPortSw_Combo1000BaseSxCopper_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseSxCopper = _H3cevtPortSw_Combo1000BaseSxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 37)
)
_H3cevtPortSw_Combo1000BaseZx_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseZx = _H3cevtPortSw_Combo1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 38)
)
_H3cevtPortSw_Combo1000BaseZxFiber_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseZxFiber = _H3cevtPortSw_Combo1000BaseZxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 39)
)
_H3cevtPortSw_Combo1000BaseZxCopper_ObjectIdentity = ObjectIdentity
h3cevtPortSw_Combo1000BaseZxCopper = _H3cevtPortSw_Combo1000BaseZxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 40)
)
_H3cevtPortSw_155PosSxMmf_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155PosSxMmf = _H3cevtPortSw_155PosSxMmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 41)
)
_H3cevtPortSw_155PosLxSmf_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155PosLxSmf = _H3cevtPortSw_155PosLxSmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 42)
)
_H3cevtPortSw_1000BASE_T_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_T = _H3cevtPortSw_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 43)
)
_H3cevtPortSw_1000BASE_SX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_SX_SFP = _H3cevtPortSw_1000BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 44)
)
_H3cevtPortSw_1000BASE_LX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_LX_SFP = _H3cevtPortSw_1000BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 45)
)
_H3cevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_T_AN_SFP = _H3cevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 46)
)
_H3cevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBASE_LX4_XENPAK = _H3cevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 47)
)
_H3cevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBASE_LR_XENPAK = _H3cevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 48)
)
_H3cevtPortSw_10GBASE_CX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBASE_CX4 = _H3cevtPortSw_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 49)
)
_H3cevtPortSw_1000BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_ZX_SFP = _H3cevtPortSw_1000BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 50)
)
_H3cevtPortSw_1000BASE_MM_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_MM_SFP = _H3cevtPortSw_1000BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 51)
)
_H3cevtPortSw_100BASE_SX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_SX_SFP = _H3cevtPortSw_100BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 52)
)
_H3cevtPortSw_100BASE_LX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_LX_SFP = _H3cevtPortSw_100BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 53)
)
_H3cevtPortSw_100BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_T_AN_SFP = _H3cevtPortSw_100BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 54)
)
_H3cevtPortSw_100BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_ZX_SFP = _H3cevtPortSw_100BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 55)
)
_H3cevtPortSw_100BASE_MM_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_MM_SFP = _H3cevtPortSw_100BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 56)
)
_H3cevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_NO_CONNECTOR = _H3cevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 57)
)
_H3cevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_UNKNOWN_CONNECTOR = _H3cevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 58)
)
_H3cevtPortSw_POS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_NO_CONNECTOR = _H3cevtPortSw_POS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 59)
)
_H3cevtPortSw_10G_BASE_SR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_SR = _H3cevtPortSw_10G_BASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 60)
)
_H3cevtPortSw_10G_BASE_ER_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_ER = _H3cevtPortSw_10G_BASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 61)
)
_H3cevtPortSw_10G_BASE_LX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_LX4 = _H3cevtPortSw_10G_BASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 62)
)
_H3cevtPortSw_10G_BASE_SW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_SW = _H3cevtPortSw_10G_BASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 63)
)
_H3cevtPortSw_10G_BASE_LW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_LW = _H3cevtPortSw_10G_BASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 64)
)
_H3cevtPortSw_10G_BASE_EW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_EW = _H3cevtPortSw_10G_BASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 65)
)
_H3cevtPortSw_10G_LR_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_LR_SM_LC = _H3cevtPortSw_10G_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 66)
)
_H3cevtPortSw_10G_SR_MM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_SR_MM_LC = _H3cevtPortSw_10G_SR_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 67)
)
_H3cevtPortSw_10G_ER_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_ER_SM_LC = _H3cevtPortSw_10G_ER_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 68)
)
_H3cevtPortSw_10G_LW_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_LW_SM_LC = _H3cevtPortSw_10G_LW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 69)
)
_H3cevtPortSw_10G_SW_MM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_SW_MM_LC = _H3cevtPortSw_10G_SW_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 70)
)
_H3cevtPortSw_10G_EW_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_EW_SM_LC = _H3cevtPortSw_10G_EW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 71)
)
_H3cevtPortSw_100BASE_SM_MTRJ_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_SM_MTRJ = _H3cevtPortSw_100BASE_SM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 72)
)
_H3cevtPortSw_100BASE_MM_MTRJ_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_MM_MTRJ = _H3cevtPortSw_100BASE_MM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 73)
)
_H3cevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_NO_CONNECTOR = _H3cevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 74)
)
_H3cevtPortSw_XFP_10GBASE_SR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_SR = _H3cevtPortSw_XFP_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 75)
)
_H3cevtPortSw_XFP_10GBASE_LR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_LR = _H3cevtPortSw_XFP_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 76)
)
_H3cevtPortSw_XFP_10GBASE_ER_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_ER = _H3cevtPortSw_XFP_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 77)
)
_H3cevtPortSw_XFP_10GBASE_SW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_SW = _H3cevtPortSw_XFP_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 78)
)
_H3cevtPortSw_XFP_10GBASE_LW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_LW = _H3cevtPortSw_XFP_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 79)
)
_H3cevtPortSw_XFP_10GBASE_EW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_EW = _H3cevtPortSw_XFP_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 80)
)
_H3cevtPortSw_XFP_10GBASE_CX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_CX4 = _H3cevtPortSw_XFP_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 81)
)
_H3cevtPortSw_XFP_10GBASE_LX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_LX4 = _H3cevtPortSw_XFP_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 82)
)
_H3cevtPortSw_XFP_UNKNOWN_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_UNKNOWN = _H3cevtPortSw_XFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 83)
)
_H3cevtPortSw_XPK_NOCONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_NOCONNECTOR = _H3cevtPortSw_XPK_NOCONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 84)
)
_H3cevtPortSw_XPK_10GBASE_SR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_SR = _H3cevtPortSw_XPK_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 85)
)
_H3cevtPortSw_XPK_10GBASE_LR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_LR = _H3cevtPortSw_XPK_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 86)
)
_H3cevtPortSw_XPK_10GBASE_ER_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_ER = _H3cevtPortSw_XPK_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 87)
)
_H3cevtPortSw_XPK_10GBASE_SW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_SW = _H3cevtPortSw_XPK_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 88)
)
_H3cevtPortSw_XPK_10GBASE_LW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_LW = _H3cevtPortSw_XPK_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 89)
)
_H3cevtPortSw_XPK_10GBASE_EW_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_EW = _H3cevtPortSw_XPK_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 90)
)
_H3cevtPortSw_XPK_10GBASE_CX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_CX4 = _H3cevtPortSw_XPK_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 91)
)
_H3cevtPortSw_XPK_10GBASE_LX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_LX4 = _H3cevtPortSw_XPK_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 92)
)
_H3cevtPortSw_XPK_UNKNOWN_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_UNKNOWN = _H3cevtPortSw_XPK_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 93)
)
_H3cevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_SR_SM_LC = _H3cevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 94)
)
_H3cevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_IR_SM_LC = _H3cevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 95)
)
_H3cevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_LR_SM_LC = _H3cevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 96)
)
_H3cevtPortSw_10G_BASE_CX4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_BASE_CX4 = _H3cevtPortSw_10G_BASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 97)
)
_H3cevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_OLT_1000BASE_BX_SFF_SC = _H3cevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 98)
)
_H3cevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_ONU_1000BASE_BX_SFF_SC = _H3cevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 99)
)
_H3cevtPortSw_24G_CASCADE_ObjectIdentity = ObjectIdentity
h3cevtPortSw_24G_CASCADE = _H3cevtPortSw_24G_CASCADE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 100)
)
_H3cevtPortSw_POS_OC3_SR_MM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_SR_MM = _H3cevtPortSw_POS_OC3_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 101)
)
_H3cevtPortSw_POS_OC3_IR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_IR_SM = _H3cevtPortSw_POS_OC3_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 102)
)
_H3cevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_IR_1_SM = _H3cevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 103)
)
_H3cevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_IR_2_SM = _H3cevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 104)
)
_H3cevtPortSw_POS_OC3_LR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_LR_SM = _H3cevtPortSw_POS_OC3_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 105)
)
_H3cevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_LR_1_SM = _H3cevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 106)
)
_H3cevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_LR_2_SM = _H3cevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 107)
)
_H3cevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC3_LR_3_SM = _H3cevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 108)
)
_H3cevtPortSw_POS_OC12_SR_MM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_SR_MM = _H3cevtPortSw_POS_OC12_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 109)
)
_H3cevtPortSw_POS_OC12_IR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_IR_SM = _H3cevtPortSw_POS_OC12_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 110)
)
_H3cevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_IR_1_SM = _H3cevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 111)
)
_H3cevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_IR_2_SM = _H3cevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 112)
)
_H3cevtPortSw_POS_OC12_LR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_LR_SM = _H3cevtPortSw_POS_OC12_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 113)
)
_H3cevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_LR_1_SM = _H3cevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 114)
)
_H3cevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_LR_2_SM = _H3cevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 115)
)
_H3cevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC12_LR_3_SM = _H3cevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 116)
)
_H3cevtPortSw_POS_OC48_SR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_SR_SM = _H3cevtPortSw_POS_OC48_SR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 117)
)
_H3cevtPortSw_POS_OC48_IR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_IR_SM = _H3cevtPortSw_POS_OC48_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 118)
)
_H3cevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_IR_1_SM = _H3cevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 119)
)
_H3cevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_IR_2_SM = _H3cevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 120)
)
_H3cevtPortSw_POS_OC48_LR_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_LR_SM = _H3cevtPortSw_POS_OC48_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 121)
)
_H3cevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_LR_1_SM = _H3cevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 122)
)
_H3cevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_LR_2_SM = _H3cevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 123)
)
_H3cevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_OC48_LR_3_SM = _H3cevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 124)
)
_H3cevtPortSw_POS_I_64_1_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_I_64_1 = _H3cevtPortSw_POS_I_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 125)
)
_H3cevtPortSw_POS_I_64_2_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_I_64_2 = _H3cevtPortSw_POS_I_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 126)
)
_H3cevtPortSw_POS_I_64_3_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_I_64_3 = _H3cevtPortSw_POS_I_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 127)
)
_H3cevtPortSw_POS_I_64_5_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_I_64_5 = _H3cevtPortSw_POS_I_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 128)
)
_H3cevtPortSw_POS_S_64_1_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_S_64_1 = _H3cevtPortSw_POS_S_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 129)
)
_H3cevtPortSw_POS_S_64_2_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_S_64_2 = _H3cevtPortSw_POS_S_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 130)
)
_H3cevtPortSw_POS_S_64_3_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_S_64_3 = _H3cevtPortSw_POS_S_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 131)
)
_H3cevtPortSw_POS_S_64_5_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_S_64_5 = _H3cevtPortSw_POS_S_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 132)
)
_H3cevtPortSw_POS_L_64_1_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_L_64_1 = _H3cevtPortSw_POS_L_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 133)
)
_H3cevtPortSw_POS_L_64_2_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_L_64_2 = _H3cevtPortSw_POS_L_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 134)
)
_H3cevtPortSw_POS_L_64_3_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_L_64_3 = _H3cevtPortSw_POS_L_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 135)
)
_H3cevtPortSw_POS_V_64_2_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_V_64_2 = _H3cevtPortSw_POS_V_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 136)
)
_H3cevtPortSw_POS_V_64_3_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_V_64_3 = _H3cevtPortSw_POS_V_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 137)
)
_H3cevtPortSw_100BASE_FX_BIDI_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_FX_BIDI = _H3cevtPortSw_100BASE_FX_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 138)
)
_H3cevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_BX10_U_SFP = _H3cevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 139)
)
_H3cevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_BX10_D_SFP = _H3cevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 140)
)
_H3cevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_BX10_U_SFP = _H3cevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 141)
)
_H3cevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_BX10_D_SFP = _H3cevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 142)
)
_H3cevtPortSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
h3cevtPortSw_STK_1000BASE_T = _H3cevtPortSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 143)
)
_H3cevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_PHYPOS_CONNECTOR = _H3cevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 144)
)
_H3cevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_PHY10GE_CONNECTOR = _H3cevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 145)
)
_H3cevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_LOGICPOS_CONNECTOR = _H3cevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 146)
)
_H3cevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_LOGIC10GE_CONNECTOR = _H3cevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 147)
)
_H3cevtPortSw_10GBASE_ZR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBASE_ZR = _H3cevtPortSw_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 148)
)
_H3cevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_TYPE_ERROR_CONNECTOR = _H3cevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 149)
)
_H3cevtPortSw_10G_STACK_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_STACK = _H3cevtPortSw_10G_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 150)
)
_H3cevtPortSw_155_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_ATM_SX_MMF = _H3cevtPortSw_155_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 151)
)
_H3cevtPortSw_155_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_ATM_LX_SMF = _H3cevtPortSw_155_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 152)
)
_H3cevtPortSw_622_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_ATM_SX_MMF = _H3cevtPortSw_622_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 153)
)
_H3cevtPortSw_622_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_ATM_LX_SMF = _H3cevtPortSw_622_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 154)
)
_H3cevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_ATM_NO_CONNECTOR = _H3cevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 155)
)
_H3cevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_ATM_NO_CONNECTOR = _H3cevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 156)
)
_H3cevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_CPOS_E1_NO_CONNECTOR = _H3cevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 157)
)
_H3cevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_CPOS_T1_NO_CONNECTOR = _H3cevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 158)
)
_H3cevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_CPOS_E1_NO_CONNECTOR = _H3cevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 159)
)
_H3cevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_CPOS_T1_NO_CONNECTOR = _H3cevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 160)
)
_H3cevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_CPOS_E1_SX_MMF = _H3cevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 161)
)
_H3cevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_CPOS_T1_SX_MMF = _H3cevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 162)
)
_H3cevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_CPOS_E1_LX_SMF = _H3cevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 163)
)
_H3cevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_155_CPOS_T1_LX_SMF = _H3cevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 164)
)
_H3cevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_CPOS_E1_SX_MMF = _H3cevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 165)
)
_H3cevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_CPOS_T1_SX_MMF = _H3cevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 166)
)
_H3cevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_CPOS_E1_LX_SMF = _H3cevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 167)
)
_H3cevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_622_CPOS_T1_LX_SMF = _H3cevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 168)
)
_H3cevtPortSw_E1_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_E1_CONNECTOR = _H3cevtPortSw_E1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 169)
)
_H3cevtPortSw_T1_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_T1_CONNECTOR = _H3cevtPortSw_T1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 170)
)
_H3cevtPortSw_1000BASE_STK_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_STK_SFP = _H3cevtPortSw_1000BASE_STK_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 171)
)
_H3cevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_BIDI_SFP = _H3cevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 172)
)
_H3cevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_1000BASE_CWDM_SFP = _H3cevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 173)
)
_H3cevtPortSw_100BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100BASE_BIDI_SFP = _H3cevtPortSw_100BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 174)
)
_H3cevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_OLT_1000BASE_PX_SFP = _H3cevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 175)
)
_H3cevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_OLT_1000BASE_NO_CONNECTOR = _H3cevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 176)
)
_H3cevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_PHYGE_CONNECTOR = _H3cevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 177)
)
_H3cevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_LOGICGE_CONNECTOR = _H3cevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 178)
)
_H3cevtPortSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100M_1550_BIDI = _H3cevtPortSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 179)
)
_H3cevtPortSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100M_1310_BIDI = _H3cevtPortSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 180)
)
_H3cevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_PHYOC48_CONNECTOR = _H3cevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 181)
)
_H3cevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RPR_LOGICOC48_CONNECTOR = _H3cevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 182)
)
_H3cevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_100_1000_BASE_LX_SMF = _H3cevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 183)
)
_H3cevtPortSw_10G_ZW_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_ZW_SM_LC = _H3cevtPortSw_10G_ZW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 184)
)
_H3cevtPortSw_10G_ZR_SM_LC_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10G_ZR_SM_LC = _H3cevtPortSw_10G_ZR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 185)
)
_H3cevtPortSw_XPK_10GBASE_ZR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XPK_10GBASE_ZR = _H3cevtPortSw_XPK_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 186)
)
_H3cevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SGMII_100_BASE_LX_SFP = _H3cevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 187)
)
_H3cevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SGMII_100_BASE_FX_SFP = _H3cevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 188)
)
_H3cevtPortSw_WLAN_RADIO_ObjectIdentity = ObjectIdentity
h3cevtPortSw_WLAN_RADIO = _H3cevtPortSw_WLAN_RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 189)
)
_H3cevtPortSw_CABLE_ObjectIdentity = ObjectIdentity
h3cevtPortSw_CABLE = _H3cevtPortSw_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 190)
)
_H3cevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_NO_CONNECTOR = _H3cevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 191)
)
_H3cevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_10GBASE_SR = _H3cevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 192)
)
_H3cevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_10GBASE_LR = _H3cevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 193)
)
_H3cevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_10GBASE_LRM = _H3cevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 194)
)
_H3cevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_10GBASE_Cu = _H3cevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 195)
)
_H3cevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_UNKNOWN = _H3cevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 196)
)
_H3cevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_STACK_CONNECTOR = _H3cevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 197)
)
_H3cevtPortSw_POS_L_64_4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_POS_L_64_4 = _H3cevtPortSw_POS_L_64_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 198)
)
_H3cevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_MINISAS_HD_STACK_CONNECTOR = _H3cevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 199)
)
_H3cevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity = ObjectIdentity
h3cevtPortSw_ONU_1000BASE_PX_SFF = _H3cevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 200)
)
_H3cevtPortSw_RS485_ObjectIdentity = ObjectIdentity
h3cevtPortSw_RS485 = _H3cevtPortSw_RS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 201)
)
_H3cevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_10GBASE_ER = _H3cevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 202)
)
_H3cevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_PLUS_10GBASE_ZR = _H3cevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 203)
)
_H3cevtPortSw_XFP_10GBASE_ZR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_XFP_10GBASE_ZR = _H3cevtPortSw_XFP_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 204)
)
_H3cevtPortSw_QSFP_PLUS_40GBASE_SR4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_QSFP_PLUS_40GBASE_SR4 = _H3cevtPortSw_QSFP_PLUS_40GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 205)
)
_H3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR = _H3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 206)
)
_H3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR = _H3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 207)
)
_H3cevtPortSw_SFP_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_SFP_STACK_CONNECTOR = _H3cevtPortSw_SFP_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 208)
)
_H3cevtPortSw_QSFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_QSFP_NO_CONNECTOR = _H3cevtPortSw_QSFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 209)
)
_H3cevtPortSw_10GBase_T_ObjectIdentity = ObjectIdentity
h3cevtPortSw_10GBase_T = _H3cevtPortSw_10GBase_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 210)
)
_H3cevtPortSw_CFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
h3cevtPortSw_CFP_NO_CONNECTOR = _H3cevtPortSw_CFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 211)
)
_H3cevtPortSw_CFP_40GBASE_LR4_ObjectIdentity = ObjectIdentity
h3cevtPortSw_CFP_40GBASE_LR4 = _H3cevtPortSw_CFP_40GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 10, 4, 212)
)
_H3cevtStack_ObjectIdentity = ObjectIdentity
h3cevtStack = _H3cevtStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 3, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-ENTITY-VENDORTYPE-OID-MIB",
    **{"h3cEntityVendorTypeOID": h3cEntityVendorTypeOID,
       "h3cEntityVendortypeObjects": h3cEntityVendortypeObjects,
       "h3cevtOther": h3cevtOther,
       "h3cevtOtherUnknownCard": h3cevtOtherUnknownCard,
       "h3cevtCPU": h3cevtCPU,
       "h3cevtGeneralCPU": h3cevtGeneralCPU,
       "h3cevtDOM": h3cevtDOM,
       "h3cevtCFCard": h3cevtCFCard,
       "h3cevtHardDisk": h3cevtHardDisk,
       "h3cevtUnknown": h3cevtUnknown,
       "h3cevtChassis": h3cevtChassis,
       "h3cevtBackplane": h3cevtBackplane,
       "h3cevtContainer": h3cevtContainer,
       "h3cevtPowerSupply": h3cevtPowerSupply,
       "h3cevtPowerSupplyAC": h3cevtPowerSupplyAC,
       "h3cevtPowerSupplyDC": h3cevtPowerSupplyDC,
       "h3cevtPowerSupplySTD130W": h3cevtPowerSupplySTD130W,
       "h3cevtPowerSupplySTD180W": h3cevtPowerSupplySTD180W,
       "h3cevtPowerSupplyPOE24Port": h3cevtPowerSupplyPOE24Port,
       "h3cevtPowerSupplyPOE48Port": h3cevtPowerSupplyPOE48Port,
       "h3cevtFan": h3cevtFan,
       "h3cevtHotSwapFan": h3cevtHotSwapFan,
       "h3cevtNonHotSwapFan": h3cevtNonHotSwapFan,
       "h3cevtSensor": h3cevtSensor,
       "h3cevtSensorTemperature": h3cevtSensorTemperature,
       "h3cevtSensorVoltage": h3cevtSensorVoltage,
       "h3cevtSensorFanSpeed": h3cevtSensorFanSpeed,
       "h3cevtModule": h3cevtModule,
       "h3cevtModuleUnknownCard": h3cevtModuleUnknownCard,
       "h3cevtModuleCommonCards": h3cevtModuleCommonCards,
       "h3cevtModuleRouterType": h3cevtModuleRouterType,
       "h3cevtModuleRt-As": h3cevtModuleRt_As,
       "h3cevtModuleRt-Sa": h3cevtModuleRt_Sa,
       "h3cevtModuleRt-Bi": h3cevtModuleRt_Bi,
       "h3cevtModuleRt-E12": h3cevtModuleRt_E12,
       "h3cevtModuleRt-E14": h3cevtModuleRt_E14,
       "h3cevtModuleRt-Fe1": h3cevtModuleRt_Fe1,
       "h3cevtModuleRt-E1": h3cevtModuleRt_E1,
       "h3cevtModuleRt-Fe2": h3cevtModuleRt_Fe2,
       "h3cevtModuleRt-Vi2": h3cevtModuleRt_Vi2,
       "h3cevtModuleRt-Vi4": h3cevtModuleRt_Vi4,
       "h3cevtModuleRt-Vi30": h3cevtModuleRt_Vi30,
       "h3cevtModuleRt-S1b": h3cevtModuleRt_S1b,
       "h3cevtModuleRt-Sa2": h3cevtModuleRt_Sa2,
       "h3cevtModuleRt-As16": h3cevtModuleRt_As16,
       "h3cevtModuleRt-New8as": h3cevtModuleRt_New8as,
       "h3cevtModuleRt-Sa1": h3cevtModuleRt_Sa1,
       "h3cevtModuleRt-Fxs2": h3cevtModuleRt_Fxs2,
       "h3cevtModuleRt-Fxo2": h3cevtModuleRt_Fxo2,
       "h3cevtModuleRt-Em2": h3cevtModuleRt_Em2,
       "h3cevtModuleRt-Fxs4": h3cevtModuleRt_Fxs4,
       "h3cevtModuleRt-Fxo4": h3cevtModuleRt_Fxo4,
       "h3cevtModuleRt-Em4": h3cevtModuleRt_Em4,
       "h3cevtModuleRt-Sab": h3cevtModuleRt_Sab,
       "h3cevtModuleRt-E1vi": h3cevtModuleRt_E1vi,
       "h3cevtModuleRt-Am12": h3cevtModuleRt_Am12,
       "h3cevtModuleRt-Am6": h3cevtModuleRt_Am6,
       "h3cevtModuleRt-Ndec": h3cevtModuleRt_Ndec,
       "h3cevtModuleRt-Newsa2": h3cevtModuleRt_Newsa2,
       "h3cevtModuleRt-Aux": h3cevtModuleRt_Aux,
       "h3cevtModuleRt-Console": h3cevtModuleRt_Console,
       "h3cevtModuleRt-Sic-wan": h3cevtModuleRt_Sic_wan,
       "h3cevtModuleRt-Sic-1fe": h3cevtModuleRt_Sic_1fe,
       "h3cevtModuleRt-Sic-1sa": h3cevtModuleRt_Sic_1sa,
       "h3cevtModuleRt-Sic-3as": h3cevtModuleRt_Sic_3as,
       "h3cevtModuleRt-Sic-1e1": h3cevtModuleRt_Sic_1e1,
       "h3cevtModuleRt-Sic-1t1": h3cevtModuleRt_Sic_1t1,
       "h3cevtModuleRt-Sic-1bu": h3cevtModuleRt_Sic_1bu,
       "h3cevtModuleRt-Sic-2bu": h3cevtModuleRt_Sic_2bu,
       "h3cevtModuleRt-Sic-1bs": h3cevtModuleRt_Sic_1bs,
       "h3cevtModuleRt-Sic-2bs": h3cevtModuleRt_Sic_2bs,
       "h3cevtModuleRt-Sic-1am": h3cevtModuleRt_Sic_1am,
       "h3cevtModuleRt-Sic-2am": h3cevtModuleRt_Sic_2am,
       "h3cevtModuleRt-Sic-1em": h3cevtModuleRt_Sic_1em,
       "h3cevtModuleRt-Sic-2em": h3cevtModuleRt_Sic_2em,
       "h3cevtModuleRt-Sic-1fxs": h3cevtModuleRt_Sic_1fxs,
       "h3cevtModuleRt-Sic-2fxs": h3cevtModuleRt_Sic_2fxs,
       "h3cevtModuleRt-Sic-1fxo": h3cevtModuleRt_Sic_1fxo,
       "h3cevtModuleRt-Sic-2fxo": h3cevtModuleRt_Sic_2fxo,
       "h3cevtModuleRt-Fcm6": h3cevtModuleRt_Fcm6,
       "h3cevtModuleRt-Sa8": h3cevtModuleRt_Sa8,
       "h3cevtModuleRt-T11": h3cevtModuleRt_T11,
       "h3cevtModuleRt-T12": h3cevtModuleRt_T12,
       "h3cevtModuleRt-T14": h3cevtModuleRt_T14,
       "h3cevtModuleRt-T1vi": h3cevtModuleRt_T1vi,
       "h3cevtModuleRt-Fcm4": h3cevtModuleRt_Fcm4,
       "h3cevtModuleRt-Fcm2": h3cevtModuleRt_Fcm2,
       "h3cevtModuleRt-Rtb21ce3": h3cevtModuleRt_Rtb21ce3,
       "h3cevtModuleRt-Ame6": h3cevtModuleRt_Ame6,
       "h3cevtModuleRt-Ame12": h3cevtModuleRt_Ame12,
       "h3cevtModuleRt-E11-f": h3cevtModuleRt_E11_f,
       "h3cevtModuleRt-E12-f": h3cevtModuleRt_E12_f,
       "h3cevtModuleRt-E14-f": h3cevtModuleRt_E14_f,
       "h3cevtModuleRt-T11-f": h3cevtModuleRt_T11_f,
       "h3cevtModuleRt-T12-f": h3cevtModuleRt_T12_f,
       "h3cevtModuleRt-T14-f": h3cevtModuleRt_T14_f,
       "h3cevtModuleRt-E11-f-17": h3cevtModuleRt_E11_f_17,
       "h3cevtModuleRt-T11-f-17": h3cevtModuleRt_T11_f_17,
       "h3cevtModuleRt-Rtb21ct3": h3cevtModuleRt_Rtb21ct3,
       "h3cevtModuleRt-Atmadsl1": h3cevtModuleRt_Atmadsl1,
       "h3cevtModuleRt-Atmadsl2": h3cevtModuleRt_Atmadsl2,
       "h3cevtModuleRt-Atm155m": h3cevtModuleRt_Atm155m,
       "h3cevtModuleRt-Ase8": h3cevtModuleRt_Ase8,
       "h3cevtModuleRt-Ase16": h3cevtModuleRt_Ase16,
       "h3cevtModuleRt-Sae4": h3cevtModuleRt_Sae4,
       "h3cevtModuleRt-Sae2": h3cevtModuleRt_Sae2,
       "h3cevtModuleRt-Atmshdsl1": h3cevtModuleRt_Atmshdsl1,
       "h3cevtModuleRt-Atmshdsl2": h3cevtModuleRt_Atmshdsl2,
       "h3cevtModuleRt-Atmshdsl4": h3cevtModuleRt_Atmshdsl4,
       "h3cevtModuleRt-Atm25m": h3cevtModuleRt_Atm25m,
       "h3cevtModuleRt-Atme3": h3cevtModuleRt_Atme3,
       "h3cevtModuleRt-Atmt3": h3cevtModuleRt_Atmt3,
       "h3cevtModuleRt-Xdsl-fec": h3cevtModuleRt_Xdsl_fec,
       "h3cevtModuleRt-Xdsl-adsl": h3cevtModuleRt_Xdsl_adsl,
       "h3cevtModuleRt-Xdsl-gshdsl": h3cevtModuleRt_Xdsl_gshdsl,
       "h3cevtModuleRt-Xdsl-bri": h3cevtModuleRt_Xdsl_bri,
       "h3cevtModuleRt-Xdsl-scc": h3cevtModuleRt_Xdsl_scc,
       "h3cevtModuleRt-Ge1": h3cevtModuleRt_Ge1,
       "h3cevtModuleRt-Pos155m": h3cevtModuleRt_Pos155m,
       "h3cevtModuleRt-Cpos": h3cevtModuleRt_Cpos,
       "h3cevtModuleRt-Fe1op": h3cevtModuleRt_Fe1op,
       "h3cevtModuleRt-Sae8": h3cevtModuleRt_Sae8,
       "h3cevtModuleRt-Atm155m-mm": h3cevtModuleRt_Atm155m_mm,
       "h3cevtModuleRt-Atm155m-sm": h3cevtModuleRt_Atm155m_sm,
       "h3cevtModuleRt-Atm155m-sml": h3cevtModuleRt_Atm155m_sml,
       "h3cevtModuleRt-Fe1op-sfx": h3cevtModuleRt_Fe1op_sfx,
       "h3cevtModuleRt-Fe1op-mfx": h3cevtModuleRt_Fe1op_mfx,
       "h3cevtModuleRt-Cpos-t1": h3cevtModuleRt_Cpos_t1,
       "h3cevtModuleRt-Ge1op": h3cevtModuleRt_Ge1op,
       "h3cevtModuleRt-Ge2op": h3cevtModuleRt_Ge2op,
       "h3cevtModuleRt-Ge2": h3cevtModuleRt_Ge2,
       "h3cevtModuleRt-Fix-1wan": h3cevtModuleRt_Fix_1wan,
       "h3cevtModuleRt-Fix-1sae": h3cevtModuleRt_Fix_1sae,
       "h3cevtModuleRt-Cavium": h3cevtModuleRt_Cavium,
       "h3cevtModuleRt-Sic1Eth": h3cevtModuleRt_Sic1Eth,
       "h3cevtModuleRt-atm1ADSLI": h3cevtModuleRt_atm1ADSLI,
       "h3cevtModuleRt-atm2ADSLI": h3cevtModuleRt_atm2ADSLI,
       "h3cevtModuleRt-fix-e11": h3cevtModuleRt_fix_e11,
       "h3cevtModuleRt-fix-t11": h3cevtModuleRt_fix_t11,
       "h3cevtModuleRt-e18-75": h3cevtModuleRt_e18_75,
       "h3cevtModuleRt-e18-120": h3cevtModuleRt_e18_120,
       "h3cevtModuleRt-t18": h3cevtModuleRt_t18,
       "h3cevtModuleRt-sic-1vifxs": h3cevtModuleRt_sic_1vifxs,
       "h3cevtModuleRt-sic-1vifxo": h3cevtModuleRt_sic_1vifxo,
       "h3cevtModuleRt-sic-2vifxs": h3cevtModuleRt_sic_2vifxs,
       "h3cevtModuleRt-sic-2vifxo": h3cevtModuleRt_sic_2vifxo,
       "h3cevtModuleRt-xdsl-fec-new": h3cevtModuleRt_xdsl_fec_new,
       "h3cevtModuleRt-xdsl-sa": h3cevtModuleRt_xdsl_sa,
       "h3cevtModuleRt-bs4": h3cevtModuleRt_bs4,
       "h3cevtModuleRt-ima-8e175": h3cevtModuleRt_ima_8e175,
       "h3cevtModuleRt-ima-8e1120": h3cevtModuleRt_ima_8e1120,
       "h3cevtModuleRt-ima-4e175": h3cevtModuleRt_ima_4e175,
       "h3cevtModuleRt-ima-4e1120": h3cevtModuleRt_ima_4e1120,
       "h3cevtModuleRt-ima-8t1": h3cevtModuleRt_ima_8t1,
       "h3cevtModuleRt-ima-4t1": h3cevtModuleRt_ima_4t1,
       "h3cevtModuleRt-sic-1t1f": h3cevtModuleRt_sic_1t1f,
       "h3cevtModuleRt-sic-1e1f": h3cevtModuleRt_sic_1e1f,
       "h3cevtModuleRt-VG-16fxs": h3cevtModuleRt_VG_16fxs,
       "h3cevtModuleRt-VG-32fxs": h3cevtModuleRt_VG_32fxs,
       "h3cevtModuleRt-VG-8fxo": h3cevtModuleRt_VG_8fxo,
       "h3cevtModuleRt-VG-2fe": h3cevtModuleRt_VG_2fe,
       "h3cevtModuleRt-sib": h3cevtModuleRt_sib,
       "h3cevtModuleRt-cie32": h3cevtModuleRt_cie32,
       "h3cevtModuleRt-cie64": h3cevtModuleRt_cie64,
       "h3cevtModuleRt-cie96": h3cevtModuleRt_cie96,
       "h3cevtModuleRt-Fe4": h3cevtModuleRt_Fe4,
       "h3cevtModuleRt-fxs4fxo1": h3cevtModuleRt_fxs4fxo1,
       "h3cevtModuleRt-atm1shdsl4wire": h3cevtModuleRt_atm1shdsl4wire,
       "h3cevtModuleRt-atmIma4shdsl": h3cevtModuleRt_atmIma4shdsl,
       "h3cevtModuleRt-ls4": h3cevtModuleRt_ls4,
       "h3cevtModuleRt-ls8": h3cevtModuleRt_ls8,
       "h3cevtModuleRt-ls16": h3cevtModuleRt_ls16,
       "h3cevtModuleRt-sic-adls2plus-isdn": h3cevtModuleRt_sic_adls2plus_isdn,
       "h3cevtModuleRt-sic-adls2plus-pots": h3cevtModuleRt_sic_adls2plus_pots,
       "h3cevtModuleRt-ft3": h3cevtModuleRt_ft3,
       "h3cevtModuleRt-ce32": h3cevtModuleRt_ce32,
       "h3cevtModuleRt-bsv2": h3cevtModuleRt_bsv2,
       "h3cevtModuleRt-bsv4": h3cevtModuleRt_bsv4,
       "h3cevtModuleRt-RPU": h3cevtModuleRt_RPU,
       "h3cevtModuleRt-ERPU": h3cevtModuleRt_ERPU,
       "h3cevtModuleRt-SSL": h3cevtModuleRt_SSL,
       "h3cevtModuleRt-NSA": h3cevtModuleRt_NSA,
       "h3cevtModuleRT-SIC-1GEC": h3cevtModuleRT_SIC_1GEC,
       "h3cevtModuleRT-24FSW": h3cevtModuleRT_24FSW,
       "h3cevtModuleRT-24FSWP": h3cevtModuleRT_24FSWP,
       "h3cevtModuleRT-16FSW": h3cevtModuleRT_16FSW,
       "h3cevtModuleRT-16FSWP": h3cevtModuleRT_16FSWP,
       "h3cevtModuleRT-1VE1": h3cevtModuleRT_1VE1,
       "h3cevtModuleRT-1VT1": h3cevtModuleRT_1VT1,
       "h3cevtModuleRT-2VE1": h3cevtModuleRT_2VE1,
       "h3cevtModuleRT-2VT1": h3cevtModuleRT_2VT1,
       "h3cevtModuleRT-SIC-4FSW": h3cevtModuleRT_SIC_4FSW,
       "h3cevtModuleRT-SIC-4FSWP": h3cevtModuleRT_SIC_4FSWP,
       "h3cevtModuleRT-DSIC-9FSW": h3cevtModuleRT_DSIC_9FSW,
       "h3cevtModuleRT-DSIC-9FSWP": h3cevtModuleRT_DSIC_9FSWP,
       "h3cevtModuleRT-SIC-1VE1": h3cevtModuleRT_SIC_1VE1,
       "h3cevtModuleRT-SIC-1VT1": h3cevtModuleRT_SIC_1VT1,
       "h3cevtModuleRT-VCPM": h3cevtModuleRT_VCPM,
       "h3cevtModuleRT-VPM": h3cevtModuleRT_VPM,
       "h3cevtModuleRT-VPMA": h3cevtModuleRT_VPMA,
       "h3cevtModuleRT-VPMB": h3cevtModuleRT_VPMB,
       "h3cevtModuleRT-VPMC": h3cevtModuleRT_VPMC,
       "h3cevtModuleRt-fe18-75": h3cevtModuleRt_fe18_75,
       "h3cevtModuleRt-fe18-120": h3cevtModuleRt_fe18_120,
       "h3cevtModuleRt-ft18": h3cevtModuleRt_ft18,
       "h3cevtModuleRt-CF": h3cevtModuleRt_CF,
       "h3cevtModuleRt-bsv2-v2": h3cevtModuleRt_bsv2_v2,
       "h3cevtModuleRt-e1vi1-v2": h3cevtModuleRt_e1vi1_v2,
       "h3cevtModuleRt-e1vi2": h3cevtModuleRt_e1vi2,
       "h3cevtModuleRt-t1vi1-v2": h3cevtModuleRt_t1vi1_v2,
       "h3cevtModuleRt-t1vi2": h3cevtModuleRt_t1vi2,
       "h3cevtModuleRt-osm": h3cevtModuleRt_osm,
       "h3cevtModuleRt-sd707": h3cevtModuleRt_sd707,
       "h3cevtModuleRt-dm-epri": h3cevtModuleRt_dm_epri,
       "h3cevtModuleRt-dm-tpri": h3cevtModuleRt_dm_tpri,
       "h3cevtModuleRt-ERPU-H": h3cevtModuleRt_ERPU_H,
       "h3cevtModuleRT-SIC-1BSV": h3cevtModuleRT_SIC_1BSV,
       "h3cevtModuleRT-SIC-2BSV": h3cevtModuleRT_SIC_2BSV,
       "h3cevtModuleRt-gbe8": h3cevtModuleRt_gbe8,
       "h3cevtModuleRt-gbe4": h3cevtModuleRt_gbe4,
       "h3cevtModuleRt-cpos2-v2": h3cevtModuleRt_cpos2_v2,
       "h3cevtModuleRt-cpos1-v2": h3cevtModuleRt_cpos1_v2,
       "h3cevtModuleRt-oap": h3cevtModuleRt_oap,
       "h3cevtModuleRT-48FSWP": h3cevtModuleRT_48FSWP,
       "h3cevtModuleRT-48FSW": h3cevtModuleRT_48FSW,
       "h3cevtModuleRT-ASM": h3cevtModuleRT_ASM,
       "h3cevtModuleRT-SIC-1FEF": h3cevtModuleRT_SIC_1FEF,
       "h3cevtModuleRT-XMIM-24FSW": h3cevtModuleRT_XMIM_24FSW,
       "h3cevtModuleRT-WLAN-AG-1RADIO": h3cevtModuleRT_WLAN_AG_1RADIO,
       "h3cevtModuleRT-1CE3": h3cevtModuleRT_1CE3,
       "h3cevtModuleRT-XMIM-16FSW": h3cevtModuleRT_XMIM_16FSW,
       "h3cevtModuleRT-OAPS": h3cevtModuleRT_OAPS,
       "h3cevtModuleRT-NAM": h3cevtModuleRT_NAM,
       "h3cevtModuleRT-RPE-X1": h3cevtModuleRT_RPE_X1,
       "h3cevtModuleRT-FIP-100": h3cevtModuleRT_FIP_100,
       "h3cevtModuleRT-FIP-200": h3cevtModuleRT_FIP_200,
       "h3cevtModuleRT-SIC-8AS": h3cevtModuleRT_SIC_8AS,
       "h3cevtModuleRT-WAAM": h3cevtModuleRT_WAAM,
       "h3cevtModuleRt-msp4p-OC3c": h3cevtModuleRt_msp4p_OC3c,
       "h3cevtModuleRt-1pos-oc48": h3cevtModuleRt_1pos_oc48,
       "h3cevtModuleRt-xgbe": h3cevtModuleRt_xgbe,
       "h3cevtModuleRT-EADM": h3cevtModuleRT_EADM,
       "h3cevtModuleRT-VCM": h3cevtModuleRT_VCM,
       "h3cevtModuleRT-SIC-2FXS1FXO": h3cevtModuleRT_SIC_2FXS1FXO,
       "h3cevtModuleRT-8FXS8FXO": h3cevtModuleRT_8FXS8FXO,
       "h3cevtModuleRT-16FXS": h3cevtModuleRT_16FXS,
       "h3cevtModuleRT-OAPS-ICM": h3cevtModuleRT_OAPS_ICM,
       "h3cevtModuleRT-OAP-ICM": h3cevtModuleRT_OAP_ICM,
       "h3cevtModuleRT-8fe": h3cevtModuleRT_8fe,
       "h3cevtModuleRT-4gbp": h3cevtModuleRT_4gbp,
       "h3cevtModuleRT-MPU-G2": h3cevtModuleRT_MPU_G2,
       "h3cevtModuleRT-OAPS-OCE": h3cevtModuleRT_OAPS_OCE,
       "h3cevtModuleRT-OAP-OCE": h3cevtModuleRT_OAP_OCE,
       "h3cevtModuleRT-OAPS-ICE": h3cevtModuleRT_OAPS_ICE,
       "h3cevtModuleRT-OAP-ICE": h3cevtModuleRT_OAP_ICE,
       "h3cevtModuleRT-SIC-16AS": h3cevtModuleRT_SIC_16AS,
       "h3cevtModuleRT-SPE-FWM": h3cevtModuleRT_SPE_FWM,
       "h3cevtModuleRT-cls2p": h3cevtModuleRT_cls2p,
       "h3cevtModuleRT-cls1p": h3cevtModuleRT_cls1p,
       "h3cevtModuleRT-SIC-2E1-F": h3cevtModuleRT_SIC_2E1_F,
       "h3cevtModuleRT-SIC-1E1-F-V2": h3cevtModuleRT_SIC_1E1_F_V2,
       "h3cevtModuleRT-MCU": h3cevtModuleRT_MCU,
       "h3cevtModuleRT-ACU": h3cevtModuleRT_ACU,
       "h3cevtModuleRT-1ATM-OC3": h3cevtModuleRT_1ATM_OC3,
       "h3cevtModuleRT-RSE-X1": h3cevtModuleRT_RSE_X1,
       "h3cevtModuleRT-FIP-210": h3cevtModuleRT_FIP_210,
       "h3cevtModuleRT-1expa": h3cevtModuleRT_1expa,
       "h3cevtModuleRT-WLAN-SIC-N-1RADIO": h3cevtModuleRT_WLAN_SIC_N_1RADIO,
       "h3cevtModuleRT-WLAN-SIC-BG-1RADIO": h3cevtModuleRT_WLAN_SIC_BG_1RADIO,
       "h3cevtModuleRT-al2p": h3cevtModuleRT_al2p,
       "h3cevtModuleRT-msp2p-OC3c": h3cevtModuleRT_msp2p_OC3c,
       "h3cevtModuleRT-8gbp": h3cevtModuleRT_8gbp,
       "h3cevtModuleRT-SIC-EPON": h3cevtModuleRT_SIC_EPON,
       "h3cevtModuleRT-SIC-3G-GSM-H3": h3cevtModuleRT_SIC_3G_GSM_H3,
       "h3cevtModuleRT-msp2p-OC12c": h3cevtModuleRT_msp2p_OC12c,
       "h3cevtModuleRt-msp4p-OC12c": h3cevtModuleRt_msp4p_OC12c,
       "h3cevtModuleRt-al1p": h3cevtModuleRt_al1p,
       "h3cevtModuleRt-OAP-100": h3cevtModuleRt_OAP_100,
       "h3cevtModuleRt-FIP-110": h3cevtModuleRt_FIP_110,
       "h3cevtModuleRt-OSM-SSM": h3cevtModuleRt_OSM_SSM,
       "h3cevtModuleRt-OAP-SSM": h3cevtModuleRt_OAP_SSM,
       "h3cevtModuleRt-rs2p": h3cevtModuleRt_rs2p,
       "h3cevtModuleRt-SAP-48GBE": h3cevtModuleRt_SAP_48GBE,
       "h3cevtModuleRt-SAP-48GBP": h3cevtModuleRt_SAP_48GBP,
       "h3cevtModuleRt-SAP-24GBP": h3cevtModuleRt_SAP_24GBP,
       "h3cevtModuleRt-SPE-SSL": h3cevtModuleRt_SPE_SSL,
       "h3cevtModuleRt-SIC-AUDIO": h3cevtModuleRt_SIC_AUDIO,
       "h3cevtModuleRt-FIC-1E1POS-H3": h3cevtModuleRt_FIC_1E1POS_H3,
       "h3cevtModuleRt-DSIC-4FXS1FXO": h3cevtModuleRt_DSIC_4FXS1FXO,
       "h3cevtModuleRt-FIC-CPOS": h3cevtModuleRt_FIC_CPOS,
       "h3cevtModuleRt-DSIC-1SHDSL-8W": h3cevtModuleRt_DSIC_1SHDSL_8W,
       "h3cevtModuleRt-SIC-3G-TD": h3cevtModuleRt_SIC_3G_TD,
       "h3cevtModuleRt-SIC-3G-CDMA": h3cevtModuleRt_SIC_3G_CDMA,
       "h3cevtModuleRt-SIC-3G-HSPA": h3cevtModuleRt_SIC_3G_HSPA,
       "h3cevtModuleRt-FIC-OAP-V2": h3cevtModuleRt_FIC_OAP_V2,
       "h3cevtModuleRt-MIM-OAP-V2": h3cevtModuleRt_MIM_OAP_V2,
       "h3cevtModuleRt-MIM-OAPS-V2": h3cevtModuleRt_MIM_OAPS_V2,
       "h3cevtModuleRt-HMIM-1CT3": h3cevtModuleRt_HMIM_1CT3,
       "h3cevtModuleRt-HMIM-1CE3": h3cevtModuleRt_HMIM_1CE3,
       "h3cevtModuleRt-HMIM-1POS": h3cevtModuleRt_HMIM_1POS,
       "h3cevtModuleRt-HMIM-2SAE": h3cevtModuleRt_HMIM_2SAE,
       "h3cevtModuleRt-HMIM-4SAE": h3cevtModuleRt_HMIM_4SAE,
       "h3cevtModuleRt-HMIM-8SAE": h3cevtModuleRt_HMIM_8SAE,
       "h3cevtModuleRt-HMIM-8ASE": h3cevtModuleRt_HMIM_8ASE,
       "h3cevtModuleRt-HMIM-16ASE": h3cevtModuleRt_HMIM_16ASE,
       "h3cevtModuleRt-HMIM-1E1": h3cevtModuleRt_HMIM_1E1,
       "h3cevtModuleRt-HMIM-2E1": h3cevtModuleRt_HMIM_2E1,
       "h3cevtModuleRt-HMIM-4E1": h3cevtModuleRt_HMIM_4E1,
       "h3cevtModuleRt-HMIM-8E1-75": h3cevtModuleRt_HMIM_8E1_75,
       "h3cevtModuleRt-HMIM-1E1-F": h3cevtModuleRt_HMIM_1E1_F,
       "h3cevtModuleRt-HMIM-2E1-F": h3cevtModuleRt_HMIM_2E1_F,
       "h3cevtModuleRt-HMIM-4E1-F": h3cevtModuleRt_HMIM_4E1_F,
       "h3cevtModuleRt-HMIM-8E1-F-75": h3cevtModuleRt_HMIM_8E1_F_75,
       "h3cevtModuleRt-HMIM-6AM": h3cevtModuleRt_HMIM_6AM,
       "h3cevtModuleRt-HMIM-6FCM": h3cevtModuleRt_HMIM_6FCM,
       "h3cevtModuleRt-HMIM-2T1": h3cevtModuleRt_HMIM_2T1,
       "h3cevtModuleRt-HMIM-4T1-F": h3cevtModuleRt_HMIM_4T1_F,
       "h3cevtModuleRt-HMIM-8T1": h3cevtModuleRt_HMIM_8T1,
       "h3cevtModuleRt-HMIM-8T1-F": h3cevtModuleRt_HMIM_8T1_F,
       "h3cevtModuleRt-HMIM-1VE1": h3cevtModuleRt_HMIM_1VE1,
       "h3cevtModuleRt-HMIM-1VT1": h3cevtModuleRt_HMIM_1VT1,
       "h3cevtModuleRt-HMIM-2VE1": h3cevtModuleRt_HMIM_2VE1,
       "h3cevtModuleRt-HMIM-2VT1": h3cevtModuleRt_HMIM_2VT1,
       "h3cevtModuleRt-HMIM-8FXS8FXO": h3cevtModuleRt_HMIM_8FXS8FXO,
       "h3cevtModuleRt-HMIM-16FXS": h3cevtModuleRt_HMIM_16FXS,
       "h3cevtModuleRt-HMIM-4FXS": h3cevtModuleRt_HMIM_4FXS,
       "h3cevtModuleRt-HMIM-4FXO": h3cevtModuleRt_HMIM_4FXO,
       "h3cevtModuleRt-HMIM-4EM": h3cevtModuleRt_HMIM_4EM,
       "h3cevtModuleRt-HMIM-4BSV": h3cevtModuleRt_HMIM_4BSV,
       "h3cevtModuleRt-SIC-CNDE": h3cevtModuleRt_SIC_CNDE,
       "h3cevtModuleRt-ESM-CNDE": h3cevtModuleRt_ESM_CNDE,
       "h3cevtModuleRt-ESM-CNDE-M": h3cevtModuleRt_ESM_CNDE_M,
       "h3cevtModuleRt-SR6602-X1": h3cevtModuleRt_SR6602_X1,
       "h3cevtModuleRt-SR6602-X2": h3cevtModuleRt_SR6602_X2,
       "h3cevtModuleRt-MCP-X1": h3cevtModuleRt_MCP_X1,
       "h3cevtModuleRt-MCP-X2": h3cevtModuleRt_MCP_X2,
       "h3cevtModuleRt-FIP-10": h3cevtModuleRt_FIP_10,
       "h3cevtModuleRt-FIP-20": h3cevtModuleRt_FIP_20,
       "h3cevtModuleRt-RSE-X2": h3cevtModuleRt_RSE_X2,
       "h3cevtModuleRt-FIP-600": h3cevtModuleRt_FIP_600,
       "h3cevtModuleRt-SAP-4EXP": h3cevtModuleRt_SAP_4EXP,
       "h3cevtModuleRt-SFE-X1": h3cevtModuleRt_SFE_X1,
       "h3cevtModuleRt-SFE-A1": h3cevtModuleRt_SFE_A1,
       "h3cevtModuleRt-HMIM-24GSW": h3cevtModuleRt_HMIM_24GSW,
       "h3cevtModuleRt-HMIM-24GSWP": h3cevtModuleRt_HMIM_24GSWP,
       "h3cevtModuleRt-MPU100": h3cevtModuleRt_MPU100,
       "h3cevtModuleRt-SPU100": h3cevtModuleRt_SPU100,
       "h3cevtModuleRt-SPU200": h3cevtModuleRt_SPU200,
       "h3cevtModuleRt-WLAN-N-1RADIO": h3cevtModuleRt_WLAN_N_1RADIO,
       "h3cevtModuleRt-3G-CDMA": h3cevtModuleRt_3G_CDMA,
       "h3cevtModuleRt-3G-WCDMA": h3cevtModuleRt_3G_WCDMA,
       "h3cevtModuleRt-3G-HSPAPLUS": h3cevtModuleRt_3G_HSPAPLUS,
       "h3cevtModuleRt-VPM-128": h3cevtModuleRt_VPM_128,
       "h3cevtModuleRt-VPM-256": h3cevtModuleRt_VPM_256,
       "h3cevtModuleRt-VPM-512": h3cevtModuleRt_VPM_512,
       "h3cevtModuleRt-IPU": h3cevtModuleRt_IPU,
       "h3cevtModuleRt-MIM2GEBE-PCIE": h3cevtModuleRt_MIM2GEBE_PCIE,
       "h3cevtModuleRt-HIM12GE-PCIE": h3cevtModuleRt_HIM12GE_PCIE,
       "h3cevtModuleRt-HIM2XGE-PCIE": h3cevtModuleRt_HIM2XGE_PCIE,
       "h3cevtModuleRt-IPU-T1000-M": h3cevtModuleRt_IPU_T1000_M,
       "h3cevtModuleRt-IPU-GX4C": h3cevtModuleRt_IPU_GX4C,
       "h3cevtModuleRt-IPU-GT4C": h3cevtModuleRt_IPU_GT4C,
       "h3cevtModuleRt-RPU-IAG2000-A": h3cevtModuleRt_RPU_IAG2000_A,
       "h3cevtModuleRt-RPU-AFD1000-A": h3cevtModuleRt_RPU_AFD1000_A,
       "h3cevtModuleRt-RPU-F5000-A": h3cevtModuleRt_RPU_F5000_A,
       "h3cevtModuleRt-ACG-8800S3-MPU": h3cevtModuleRt_ACG_8800S3_MPU,
       "h3cevtModuleRt-T5000S3-MPU": h3cevtModuleRt_T5000S3_MPU,
       "h3cevtModuleRt-NS21S2MSPB0": h3cevtModuleRt_NS21S2MSPB0,
       "h3cevtModuleRt-NS11S2MSPB0": h3cevtModuleRt_NS11S2MSPB0,
       "h3cevtModuleRt-NSQ1WLAN": h3cevtModuleRt_NSQ1WLAN,
       "h3cevtModuleRt-NSQ1GP4U0": h3cevtModuleRt_NSQ1GP4U0,
       "h3cevtModuleRt-NSQ1GP8C40": h3cevtModuleRt_NSQ1GP8C40,
       "h3cevtModuleRt-NSQ1XS2U0": h3cevtModuleRt_NSQ1XS2U0,
       "h3cevtModuleRt-VG-8fxs": h3cevtModuleRt_VG_8fxs,
       "h3cevtModuleRt-VG-24fxs": h3cevtModuleRt_VG_24fxs,
       "h3cevtModuleRt-VG-24fxs24fxo": h3cevtModuleRt_VG_24fxs24fxo,
       "h3cevtModuleRt-VG-MPU": h3cevtModuleRt_VG_MPU,
       "h3cevtModuleRt-MIM-VCX-CONNECT-P-3C": h3cevtModuleRt_MIM_VCX_CONNECT_P_3C,
       "h3cevtModuleRt-MIM-VCX-CONNECT-S-3C": h3cevtModuleRt_MIM_VCX_CONNECT_S_3C,
       "h3cevtModuleRt-MIM-VCX-3C": h3cevtModuleRt_MIM_VCX_3C,
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
       "h3cevtModuleSwitchType": h3cevtModuleSwitchType,
       "h3cevtModuleSw-10OR100M": h3cevtModuleSw_10OR100M,
       "h3cevtModuleSw-1000BASE-LX-SM": h3cevtModuleSw_1000BASE_LX_SM,
       "h3cevtModuleSw-1000BASE-SX-MM": h3cevtModuleSw_1000BASE_SX_MM,
       "h3cevtModuleSw-1000BASE-TX": h3cevtModuleSw_1000BASE_TX,
       "h3cevtModuleSw-100M-SINGLEMODE-FX": h3cevtModuleSw_100M_SINGLEMODE_FX,
       "h3cevtModuleSw-100M-MULTIMODE-FX": h3cevtModuleSw_100M_MULTIMODE_FX,
       "h3cevtModuleSw-100M-100BASE-TX": h3cevtModuleSw_100M_100BASE_TX,
       "h3cevtModuleSw-100M-HUB": h3cevtModuleSw_100M_HUB,
       "h3cevtModuleSw-VDSL": h3cevtModuleSw_VDSL,
       "h3cevtModuleSw-STACK": h3cevtModuleSw_STACK,
       "h3cevtModuleSw-1000BASE-ZENITH-FX": h3cevtModuleSw_1000BASE_ZENITH_FX,
       "h3cevtModuleSw-1000BASE-LONG-FX": h3cevtModuleSw_1000BASE_LONG_FX,
       "h3cevtModuleSw-ADSL": h3cevtModuleSw_ADSL,
       "h3cevtModuleSw-4T10OR100-4FX100SM": h3cevtModuleSw_4T10OR100_4FX100SM,
       "h3cevtModuleSw-4T10OR100-4FX100MM": h3cevtModuleSw_4T10OR100_4FX100MM,
       "h3cevtModuleSw-VSPL": h3cevtModuleSw_VSPL,
       "h3cevtModuleSw-ASPL": h3cevtModuleSw_ASPL,
       "h3cevtModuleSw-1000M-SFP": h3cevtModuleSw_1000M_SFP,
       "h3cevtModuleSw-LS82O2CM": h3cevtModuleSw_LS82O2CM,
       "h3cevtModuleSw-LS82P2CM": h3cevtModuleSw_LS82P2CM,
       "h3cevtModuleSw-LS82O4GM": h3cevtModuleSw_LS82O4GM,
       "h3cevtModuleSw-LS82GB4C": h3cevtModuleSw_LS82GB4C,
       "h3cevtModuleSw-LS82GT4C": h3cevtModuleSw_LS82GT4C,
       "h3cevtModuleSw-LS82ST4C": h3cevtModuleSw_LS82ST4C,
       "h3cevtModuleSw-BOARD-LS82DSPU": h3cevtModuleSw_BOARD_LS82DSPU,
       "h3cevtModuleSw-BOARD-LS81GP8U": h3cevtModuleSw_BOARD_LS81GP8U,
       "h3cevtModuleSw-BOARD-LS82GT20": h3cevtModuleSw_BOARD_LS82GT20,
       "h3cevtModuleSw-BOARD-LS82FE48": h3cevtModuleSw_BOARD_LS82FE48,
       "h3cevtModuleSw-LS82T24B": h3cevtModuleSw_LS82T24B,
       "h3cevtModuleSw-LSB1SRPA": h3cevtModuleSw_LSB1SRPA,
       "h3cevtModuleSw-LSB1FT48A": h3cevtModuleSw_LSB1FT48A,
       "h3cevtModuleSw-LSB1FT48B": h3cevtModuleSw_LSB1FT48B,
       "h3cevtModuleSw-LSB1F48GA": h3cevtModuleSw_LSB1F48GA,
       "h3cevtModuleSw-LSB1F48GB": h3cevtModuleSw_LSB1F48GB,
       "h3cevtModuleSw-LSB1FP20A": h3cevtModuleSw_LSB1FP20A,
       "h3cevtModuleSw-LSB1FP20B": h3cevtModuleSw_LSB1FP20B,
       "h3cevtModuleSw-FT48A": h3cevtModuleSw_FT48A,
       "h3cevtModuleSw-GP4U": h3cevtModuleSw_GP4U,
       "h3cevtModuleSw-GP2U": h3cevtModuleSw_GP2U,
       "h3cevtModuleSw-TGX1A": h3cevtModuleSw_TGX1A,
       "h3cevtModuleSw-1000BASE-LX-SM-IR-SC": h3cevtModuleSw_1000BASE_LX_SM_IR_SC,
       "h3cevtModuleSw-1000BASE-SX-MM-SR-SC": h3cevtModuleSw_1000BASE_SX_MM_SR_SC,
       "h3cevtModuleSw-1000BASE-T-RJ45": h3cevtModuleSw_1000BASE_T_RJ45,
       "h3cevtModuleSw-100BASE-FX-SM-IR-SC": h3cevtModuleSw_100BASE_FX_SM_IR_SC,
       "h3cevtModuleSw-100BASE-FX-MM-SR-SC": h3cevtModuleSw_100BASE_FX_MM_SR_SC,
       "h3cevtModuleSw-GIGA-STACK-1M-PC": h3cevtModuleSw_GIGA_STACK_1M_PC,
       "h3cevtModuleSw-1000BASE-LX-SM-VLR-LC": h3cevtModuleSw_1000BASE_LX_SM_VLR_LC,
       "h3cevtModuleSw-1000BASE-LX-SM-LR-LC": h3cevtModuleSw_1000BASE_LX_SM_LR_LC,
       "h3cevtModuleSw-100BASE-FX-SM-LR-SC": h3cevtModuleSw_100BASE_FX_SM_LR_SC,
       "h3cevtModuleSw-1000BASE-X-GBIC": h3cevtModuleSw_1000BASE_X_GBIC,
       "h3cevtModuleSw-100M-SINGLEMODE-FX-LC": h3cevtModuleSw_100M_SINGLEMODE_FX_LC,
       "h3cevtModuleSw-100M-MULTIMODE-FX-LC": h3cevtModuleSw_100M_MULTIMODE_FX_LC,
       "h3cevtModuleSw-1000BASE-4SFP": h3cevtModuleSw_1000BASE_4SFP,
       "h3cevtModuleSw-1000BASE-4GBIC": h3cevtModuleSw_1000BASE_4GBIC,
       "h3cevtModuleSw-1000BASE-FIXED-4SFP": h3cevtModuleSw_1000BASE_FIXED_4SFP,
       "h3cevtModuleSw-1000BASE-FIXED-4GBIC": h3cevtModuleSw_1000BASE_FIXED_4GBIC,
       "h3cevtModuleSw-LSB1GP12A": h3cevtModuleSw_LSB1GP12A,
       "h3cevtModuleSw-LSB1GP12B": h3cevtModuleSw_LSB1GP12B,
       "h3cevtModuleSw-LSB1TGX1A": h3cevtModuleSw_LSB1TGX1A,
       "h3cevtModuleSw-LSB1TGX1B": h3cevtModuleSw_LSB1TGX1B,
       "h3cevtModuleSw-LSB1P4G8A": h3cevtModuleSw_LSB1P4G8A,
       "h3cevtModuleSw-LSB1P4G8B": h3cevtModuleSw_LSB1P4G8B,
       "h3cevtModuleSw-LSB1A4G8A": h3cevtModuleSw_LSB1A4G8A,
       "h3cevtModuleSw-LSB1A4G8B": h3cevtModuleSw_LSB1A4G8B,
       "h3cevtModuleSw-FT48C": h3cevtModuleSw_FT48C,
       "h3cevtModuleSw-FP20": h3cevtModuleSw_FP20,
       "h3cevtModuleSw-BOARD-LS81FT48": h3cevtModuleSw_BOARD_LS81FT48,
       "h3cevtModuleSw-BOARD-LS81GB8U": h3cevtModuleSw_BOARD_LS81GB8U,
       "h3cevtModuleSw-BOARD-LS81GT8U": h3cevtModuleSw_BOARD_LS81GT8U,
       "h3cevtModuleSw-BOARD-LS81FS24": h3cevtModuleSw_BOARD_LS81FS24,
       "h3cevtModuleSw-BOARD-LS81FM24": h3cevtModuleSw_BOARD_LS81FM24,
       "h3cevtModuleSw-BOARD-LS82GP20": h3cevtModuleSw_BOARD_LS82GP20,
       "h3cevtModuleSw-LSB1SRPB": h3cevtModuleSw_LSB1SRPB,
       "h3cevtModuleSw-LSB1F32GA": h3cevtModuleSw_LSB1F32GA,
       "h3cevtModuleSw-LSB1F32GB": h3cevtModuleSw_LSB1F32GB,
       "h3cevtModuleSw-LSB2FT48A": h3cevtModuleSw_LSB2FT48A,
       "h3cevtModuleSw-LSB2FT48B": h3cevtModuleSw_LSB2FT48B,
       "h3cevtModuleSw-LSB1GT12A": h3cevtModuleSw_LSB1GT12A,
       "h3cevtModuleSw-LSB1GT12B": h3cevtModuleSw_LSB1GT12B,
       "h3cevtModuleSw-PC4U": h3cevtModuleSw_PC4U,
       "h3cevtModuleSw-FT32A": h3cevtModuleSw_FT32A,
       "h3cevtModuleSw-GT4U": h3cevtModuleSw_GT4U,
       "h3cevtModuleSw-BOARD-LS83FP20A": h3cevtModuleSw_BOARD_LS83FP20A,
       "h3cevtModuleSw-BOARD-LS82HGMU": h3cevtModuleSw_BOARD_LS82HGMU,
       "h3cevtModuleSw-LSB1GP8TB": h3cevtModuleSw_LSB1GP8TB,
       "h3cevtModuleSw-LSB1GP8TC": h3cevtModuleSw_LSB1GP8TC,
       "h3cevtModuleSw-LSB1GT8PB": h3cevtModuleSw_LSB1GT8PB,
       "h3cevtModuleSw-LSB1GT8PC": h3cevtModuleSw_LSB1GT8PC,
       "h3cevtModuleSw-LSB1FT48C": h3cevtModuleSw_LSB1FT48C,
       "h3cevtModuleSw-LSB1FP20C": h3cevtModuleSw_LSB1FP20C,
       "h3cevtModuleSw-LSB1F32GC": h3cevtModuleSw_LSB1F32GC,
       "h3cevtModuleSw-LSB1GT12C": h3cevtModuleSw_LSB1GT12C,
       "h3cevtModuleSw-LSB1GP12C": h3cevtModuleSw_LSB1GP12C,
       "h3cevtModuleSw-LSB1P4G8C": h3cevtModuleSw_LSB1P4G8C,
       "h3cevtModuleSw-LSB1TGX1C": h3cevtModuleSw_LSB1TGX1C,
       "h3cevtModuleSw-LSB1GT24B": h3cevtModuleSw_LSB1GT24B,
       "h3cevtModuleSw-LSB1GT24C": h3cevtModuleSw_LSB1GT24C,
       "h3cevtModuleSw-LSB1GP24B": h3cevtModuleSw_LSB1GP24B,
       "h3cevtModuleSw-LSB1GP24C": h3cevtModuleSw_LSB1GP24C,
       "h3cevtModuleSw-LSB1XP2B": h3cevtModuleSw_LSB1XP2B,
       "h3cevtModuleSw-LSB1XP2C": h3cevtModuleSw_LSB1XP2C,
       "h3cevtModuleSw-LSB1GV48B": h3cevtModuleSw_LSB1GV48B,
       "h3cevtModuleSw-LSB1GV48C": h3cevtModuleSw_LSB1GV48C,
       "h3cevtModuleSw-LSB1SRPC": h3cevtModuleSw_LSB1SRPC,
       "h3cevtModuleSw-LSB1SRP1N0": h3cevtModuleSw_LSB1SRP1N0,
       "h3cevtModuleSw-LSB1SRP1N1": h3cevtModuleSw_LSB1SRP1N1,
       "h3cevtModuleSw-LSB1SRP1N2": h3cevtModuleSw_LSB1SRP1N2,
       "h3cevtModuleSw-GT24": h3cevtModuleSw_GT24,
       "h3cevtModuleSw-GP24": h3cevtModuleSw_GP24,
       "h3cevtModuleSw-XP2": h3cevtModuleSw_XP2,
       "h3cevtModuleSw-GV48": h3cevtModuleSw_GV48,
       "h3cevtModuleSw-LSG1GP8U": h3cevtModuleSw_LSG1GP8U,
       "h3cevtModuleSw-LSG1GT8U": h3cevtModuleSw_LSG1GT8U,
       "h3cevtModuleSw-LSG1TG1U": h3cevtModuleSw_LSG1TG1U,
       "h3cevtModuleSw-LSG1TD1U": h3cevtModuleSw_LSG1TD1U,
       "h3cevtModuleSw-LSB2FT48C": h3cevtModuleSw_LSB2FT48C,
       "h3cevtModuleSw-LSB1GT48B": h3cevtModuleSw_LSB1GT48B,
       "h3cevtModuleSw-LSB1GT48C": h3cevtModuleSw_LSB1GT48C,
       "h3cevtModuleSw-LS81GT48": h3cevtModuleSw_LS81GT48,
       "h3cevtModuleSw-LS81SRPG0": h3cevtModuleSw_LS81SRPG0,
       "h3cevtModuleSw-LS81SRPG1": h3cevtModuleSw_LS81SRPG1,
       "h3cevtModuleSw-LS81SRPG2": h3cevtModuleSw_LS81SRPG2,
       "h3cevtModuleSw-LS81SRPG3": h3cevtModuleSw_LS81SRPG3,
       "h3cevtModuleSw-SR01SRPUB": h3cevtModuleSw_SR01SRPUB,
       "h3cevtModuleSw-SR01SRPUA": h3cevtModuleSw_SR01SRPUA,
       "h3cevtModuleSw-SR01GP12L": h3cevtModuleSw_SR01GP12L,
       "h3cevtModuleSw-SR01GP12W": h3cevtModuleSw_SR01GP12W,
       "h3cevtModuleSw-SR01FT48L": h3cevtModuleSw_SR01FT48L,
       "h3cevtModuleSw-SR01FT48W": h3cevtModuleSw_SR01FT48W,
       "h3cevtModuleSw-SR01XK1W": h3cevtModuleSw_SR01XK1W,
       "h3cevtModuleSw-SR01FP20W": h3cevtModuleSw_SR01FP20W,
       "h3cevtModuleSw-SR01GT12W": h3cevtModuleSw_SR01GT12W,
       "h3cevtModuleSw-SR01F32GL": h3cevtModuleSw_SR01F32GL,
       "h3cevtModuleSw-SR01F32GW": h3cevtModuleSw_SR01F32GW,
       "h3cevtModuleSw-SR01GT8PL": h3cevtModuleSw_SR01GT8PL,
       "h3cevtModuleSw-SR01GT8PW": h3cevtModuleSw_SR01GT8PW,
       "h3cevtModuleSw-SR01P4G8W": h3cevtModuleSw_SR01P4G8W,
       "h3cevtModuleSw-LSA1FP8U": h3cevtModuleSw_LSA1FP8U,
       "h3cevtModuleSw-LSB1SP4B": h3cevtModuleSw_LSB1SP4B,
       "h3cevtModuleSw-LSB1SP4C": h3cevtModuleSw_LSB1SP4C,
       "h3cevtModuleSw-LSB1UP1B": h3cevtModuleSw_LSB1UP1B,
       "h3cevtModuleSw-LSB1UP1C": h3cevtModuleSw_LSB1UP1C,
       "h3cevtModuleSw-LSB1XP4B": h3cevtModuleSw_LSB1XP4B,
       "h3cevtModuleSw-LSB1XP4C": h3cevtModuleSw_LSB1XP4C,
       "h3cevtModuleSw-SP4": h3cevtModuleSw_SP4,
       "h3cevtModuleSw-UP1": h3cevtModuleSw_UP1,
       "h3cevtModuleSw-XP4": h3cevtModuleSw_XP4,
       "h3cevtModuleSw-LS81VSNP": h3cevtModuleSw_LS81VSNP,
       "h3cevtModuleSw-LS81T12P": h3cevtModuleSw_LS81T12P,
       "h3cevtModuleSw-LS81P12T": h3cevtModuleSw_LS81P12T,
       "h3cevtModuleSw-LS81GP8UB": h3cevtModuleSw_LS81GP8UB,
       "h3cevtModuleSw-LS81FT48E": h3cevtModuleSw_LS81FT48E,
       "h3cevtModuleSw-LS81GP4UB": h3cevtModuleSw_LS81GP4UB,
       "h3cevtModuleSw-LS81GT8UE": h3cevtModuleSw_LS81GT8UE,
       "h3cevtModuleSw-LS81GT48A": h3cevtModuleSw_LS81GT48A,
       "h3cevtModuleSw-LS81FP48": h3cevtModuleSw_LS81FP48,
       "h3cevtModuleSw-LSB1XK1B": h3cevtModuleSw_LSB1XK1B,
       "h3cevtModuleSw-LSB1XK1C": h3cevtModuleSw_LSB1XK1C,
       "h3cevtModuleSw-SR01SRPUC": h3cevtModuleSw_SR01SRPUC,
       "h3cevtModuleSw-SR01SRPUD": h3cevtModuleSw_SR01SRPUD,
       "h3cevtModuleSw-SR01SRPUE": h3cevtModuleSw_SR01SRPUE,
       "h3cevtModuleSw-LSB1SRP1N3": h3cevtModuleSw_LSB1SRP1N3,
       "h3cevtModuleSw-LSB1VP2B": h3cevtModuleSw_LSB1VP2B,
       "h3cevtModuleSw-LSB1NATB": h3cevtModuleSw_LSB1NATB,
       "h3cevtModuleSw-LSB1VPNB": h3cevtModuleSw_LSB1VPNB,
       "h3cevtModuleSw-LSGP8P": h3cevtModuleSw_LSGP8P,
       "h3cevtModuleSw-LSXK1P": h3cevtModuleSw_LSXK1P,
       "h3cevtModuleSw-LSXP2P": h3cevtModuleSw_LSXP2P,
       "h3cevtModuleSw-LS81FT48F": h3cevtModuleSw_LS81FT48F,
       "h3cevtModuleSw-LS81PT8G": h3cevtModuleSw_LS81PT8G,
       "h3cevtModuleSw-LS81PT4G": h3cevtModuleSw_LS81PT4G,
       "h3cevtModuleSw-LSSTK24G": h3cevtModuleSw_LSSTK24G,
       "h3cevtModuleSw-LS82GT20A": h3cevtModuleSw_LS82GT20A,
       "h3cevtModuleSw-LS82GP20A": h3cevtModuleSw_LS82GP20A,
       "h3cevtModuleSw-LS81TGX1C": h3cevtModuleSw_LS81TGX1C,
       "h3cevtModuleSw-VP2": h3cevtModuleSw_VP2,
       "h3cevtModuleSw-LSA1FB8U": h3cevtModuleSw_LSA1FB8U,
       "h3cevtModuleSw-LS81T12PE": h3cevtModuleSw_LS81T12PE,
       "h3cevtModuleSw-LS81P12TE": h3cevtModuleSw_LS81P12TE,
       "h3cevtModuleSw-LSB1SRP2N0": h3cevtModuleSw_LSB1SRP2N0,
       "h3cevtModuleSw-LSB1SRP2N3": h3cevtModuleSw_LSB1SRP2N3,
       "h3cevtModuleSw-LSB1GV48DB": h3cevtModuleSw_LSB1GV48DB,
       "h3cevtModuleSw-LSB1FW8B": h3cevtModuleSw_LSB1FW8B,
       "h3cevtModuleSw-LSB1IPSEC8B": h3cevtModuleSw_LSB1IPSEC8B,
       "h3cevtModuleSw-LSB1IDSB": h3cevtModuleSw_LSB1IDSB,
       "h3cevtModuleSw-LSB1IPSB": h3cevtModuleSw_LSB1IPSB,
       "h3cevtModuleSw-LSB2FT48CA": h3cevtModuleSw_LSB2FT48CA,
       "h3cevtModuleSw-LSB1FP20CA": h3cevtModuleSw_LSB1FP20CA,
       "h3cevtModuleSw-LSB1F32GCA": h3cevtModuleSw_LSB1F32GCA,
       "h3cevtModuleSw-LSB1P4G8CA": h3cevtModuleSw_LSB1P4G8CA,
       "h3cevtModuleSw-LSB1GT12CA": h3cevtModuleSw_LSB1GT12CA,
       "h3cevtModuleSw-LSB1GT24CA": h3cevtModuleSw_LSB1GT24CA,
       "h3cevtModuleSw-LSB1GP12CA": h3cevtModuleSw_LSB1GP12CA,
       "h3cevtModuleSw-LSB1GP24CA": h3cevtModuleSw_LSB1GP24CA,
       "h3cevtModuleSw-LSB1GT8PCA": h3cevtModuleSw_LSB1GT8PCA,
       "h3cevtModuleSw-LSB1XP2CA": h3cevtModuleSw_LSB1XP2CA,
       "h3cevtModuleSw-LSB1XK1CA": h3cevtModuleSw_LSB1XK1CA,
       "h3cevtModuleSw-LSB1XP4CA": h3cevtModuleSw_LSB1XP4CA,
       "h3cevtModuleSw-LSB1UP1CA": h3cevtModuleSw_LSB1UP1CA,
       "h3cevtModuleSw-LSB1SP4CA": h3cevtModuleSw_LSB1SP4CA,
       "h3cevtModuleSw-LSB1VP2CA": h3cevtModuleSw_LSB1VP2CA,
       "h3cevtModuleSw-SR01FT48WA": h3cevtModuleSw_SR01FT48WA,
       "h3cevtModuleSw-SR01FP20WA": h3cevtModuleSw_SR01FP20WA,
       "h3cevtModuleSw-SR01F32GWA": h3cevtModuleSw_SR01F32GWA,
       "h3cevtModuleSw-SR01P4G8WA": h3cevtModuleSw_SR01P4G8WA,
       "h3cevtModuleSw-SR01GT12WA": h3cevtModuleSw_SR01GT12WA,
       "h3cevtModuleSw-SR01GT24WA": h3cevtModuleSw_SR01GT24WA,
       "h3cevtModuleSw-SR01GP12WA": h3cevtModuleSw_SR01GP12WA,
       "h3cevtModuleSw-SR01GP24WA": h3cevtModuleSw_SR01GP24WA,
       "h3cevtModuleSw-SR01GT8PWA": h3cevtModuleSw_SR01GT8PWA,
       "h3cevtModuleSw-SR01XP2WA": h3cevtModuleSw_SR01XP2WA,
       "h3cevtModuleSw-SR01XK1WA": h3cevtModuleSw_SR01XK1WA,
       "h3cevtModuleSw-SR01UP1WA": h3cevtModuleSw_SR01UP1WA,
       "h3cevtModuleSw-SR01SP4WA": h3cevtModuleSw_SR01SP4WA,
       "h3cevtModuleSw-GP8U": h3cevtModuleSw_GP8U,
       "h3cevtModuleSw-LSEXP1P": h3cevtModuleSw_LSEXP1P,
       "h3cevtModuleSw-LSEXK1P": h3cevtModuleSw_LSEXK1P,
       "h3cevtModuleSw-LSEXS1P": h3cevtModuleSw_LSEXS1P,
       "h3cevtModuleSw-LS81GP48": h3cevtModuleSw_LS81GP48,
       "h3cevtModuleSw-LS81GT48B": h3cevtModuleSw_LS81GT48B,
       "h3cevtModuleSw-LS81T16P": h3cevtModuleSw_LS81T16P,
       "h3cevtModuleSw-LS81T32P": h3cevtModuleSw_LS81T32P,
       "h3cevtModuleSw-LS81TGX2": h3cevtModuleSw_LS81TGX2,
       "h3cevtModuleSw-LS81TGX4": h3cevtModuleSw_LS81TGX4,
       "h3cevtModuleSw-LSB1GV48DA": h3cevtModuleSw_LSB1GV48DA,
       "h3cevtModuleSw-SR01GV48VB": h3cevtModuleSw_SR01GV48VB,
       "h3cevtModuleSw-LSB1GT24DB": h3cevtModuleSw_LSB1GT24DB,
       "h3cevtModuleSw-LSB1GP24DB": h3cevtModuleSw_LSB1GP24DB,
       "h3cevtModuleSw-LSB1GP24DC": h3cevtModuleSw_LSB1GP24DC,
       "h3cevtModuleSw-LSB1FW8DB": h3cevtModuleSw_LSB1FW8DB,
       "h3cevtModuleSw-LSB1IPSEC8DB": h3cevtModuleSw_LSB1IPSEC8DB,
       "h3cevtModuleSw-SR01GT24VB": h3cevtModuleSw_SR01GT24VB,
       "h3cevtModuleSw-SR01GP24VC": h3cevtModuleSw_SR01GP24VC,
       "h3cevtModuleSw-SR01VP2WA": h3cevtModuleSw_SR01VP2WA,
       "h3cevtModuleSw-SR01FW8VB": h3cevtModuleSw_SR01FW8VB,
       "h3cevtModuleSw-SR01IPSEC8VB": h3cevtModuleSw_SR01IPSEC8VB,
       "h3cevtModuleSw-SR01NATL": h3cevtModuleSw_SR01NATL,
       "h3cevtModuleSw-SR01VPNL": h3cevtModuleSw_SR01VPNL,
       "h3cevtModuleSw-LSB1GP24CB": h3cevtModuleSw_LSB1GP24CB,
       "h3cevtModuleSw-LSB1GP48DB": h3cevtModuleSw_LSB1GP48DB,
       "h3cevtModuleSw-LSB1XP2CB": h3cevtModuleSw_LSB1XP2CB,
       "h3cevtModuleSw-XP4L": h3cevtModuleSw_XP4L,
       "h3cevtModuleSw-LSB1XP4LDB": h3cevtModuleSw_LSB1XP4LDB,
       "h3cevtModuleSw-LSB1XP4LDC": h3cevtModuleSw_LSB1XP4LDC,
       "h3cevtModuleSw-AHP4": h3cevtModuleSw_AHP4,
       "h3cevtModuleSw-LSB1AHP4GCA": h3cevtModuleSw_LSB1AHP4GCA,
       "h3cevtModuleSw-CLP4": h3cevtModuleSw_CLP4,
       "h3cevtModuleSw-LSB1CLP4GCA": h3cevtModuleSw_LSB1CLP4GCA,
       "h3cevtModuleSw-ET32": h3cevtModuleSw_ET32,
       "h3cevtModuleSw-LSB1ET32GCA": h3cevtModuleSw_LSB1ET32GCA,
       "h3cevtModuleSw-LSB1IDSDB": h3cevtModuleSw_LSB1IDSDB,
       "h3cevtModuleSw-LSB1SRP2N1": h3cevtModuleSw_LSB1SRP2N1,
       "h3cevtModuleSw-BOARD-LS82SRPB": h3cevtModuleSw_BOARD_LS82SRPB,
       "h3cevtModuleSw-BORAD-LS83SRPC": h3cevtModuleSw_BORAD_LS83SRPC,
       "h3cevtModuleSw-Main": h3cevtModuleSw_Main,
       "h3cevtModuleSw-LSB1SRP2N2": h3cevtModuleSw_LSB1SRP2N2,
       "h3cevtModuleSw-LSB1NAMB": h3cevtModuleSw_LSB1NAMB,
       "h3cevtModuleSw-RSP2": h3cevtModuleSw_RSP2,
       "h3cevtModuleSw-LSB1RSP2CA": h3cevtModuleSw_LSB1RSP2CA,
       "h3cevtModuleSw-SR01XP4LVC": h3cevtModuleSw_SR01XP4LVC,
       "h3cevtModuleSw-SR01AHP4GWA": h3cevtModuleSw_SR01AHP4GWA,
       "h3cevtModuleSw-SR01CLP4GWA": h3cevtModuleSw_SR01CLP4GWA,
       "h3cevtModuleSw-SR01ET32GWA": h3cevtModuleSw_SR01ET32GWA,
       "h3cevtModuleSw-SR01IDSVB": h3cevtModuleSw_SR01IDSVB,
       "h3cevtModuleSw-SR01SRPUF": h3cevtModuleSw_SR01SRPUF,
       "h3cevtModuleSw-SR01NAML": h3cevtModuleSw_SR01NAML,
       "h3cevtModuleSw-SR01RSP2WA": h3cevtModuleSw_SR01RSP2WA,
       "h3cevtModuleSw-LSPM1XP1P": h3cevtModuleSw_LSPM1XP1P,
       "h3cevtModuleSw-LSPM1XP2P": h3cevtModuleSw_LSPM1XP2P,
       "h3cevtModuleSw-LSPM1CX2P": h3cevtModuleSw_LSPM1CX2P,
       "h3cevtModuleSw-STK-1000BASE-T": h3cevtModuleSw_STK_1000BASE_T,
       "h3cevtModuleSw-LSB1SRP1M0": h3cevtModuleSw_LSB1SRP1M0,
       "h3cevtModuleSw-LSB1SRP1M1": h3cevtModuleSw_LSB1SRP1M1,
       "h3cevtModuleSw-LSB1GP12DB": h3cevtModuleSw_LSB1GP12DB,
       "h3cevtModuleSw-LSB1GT12DB": h3cevtModuleSw_LSB1GT12DB,
       "h3cevtModuleSw-LSB1XK1DB": h3cevtModuleSw_LSB1XK1DB,
       "h3cevtModuleSw-LSB1XP2DB": h3cevtModuleSw_LSB1XP2DB,
       "h3cevtModuleSw-LSB1XP2DC": h3cevtModuleSw_LSB1XP2DC,
       "h3cevtModuleSw-LSB1GT48LDB": h3cevtModuleSw_LSB1GT48LDB,
       "h3cevtModuleSw-LSB1XP4TDB": h3cevtModuleSw_LSB1XP4TDB,
       "h3cevtModuleSw-LSB1XP4TDC": h3cevtModuleSw_LSB1XP4TDC,
       "h3cevtModuleSw-LSB1RSP2DC": h3cevtModuleSw_LSB1RSP2DC,
       "h3cevtModuleSw-LSB1VP2DC": h3cevtModuleSw_LSB1VP2DC,
       "h3cevtModuleSw-LSB1XP4DB": h3cevtModuleSw_LSB1XP4DB,
       "h3cevtModuleSw-LSB1SRP2E0": h3cevtModuleSw_LSB1SRP2E0,
       "h3cevtModuleSw-LSB1SRP2E1": h3cevtModuleSw_LSB1SRP2E1,
       "h3cevtModuleSw-LSB1SRP2E2": h3cevtModuleSw_LSB1SRP2E2,
       "h3cevtModuleSw-LSB1SRP2E3": h3cevtModuleSw_LSB1SRP2E3,
       "h3cevtModuleSw-SR01SRPUQ": h3cevtModuleSw_SR01SRPUQ,
       "h3cevtModuleSw-AHP1": h3cevtModuleSw_AHP1,
       "h3cevtModuleSw-AHP2": h3cevtModuleSw_AHP2,
       "h3cevtModuleSw-CLP1": h3cevtModuleSw_CLP1,
       "h3cevtModuleSw-CLP2": h3cevtModuleSw_CLP2,
       "h3cevtModuleSw-ET16": h3cevtModuleSw_ET16,
       "h3cevtModuleSw-LSB1SRP1NA0": h3cevtModuleSw_LSB1SRP1NA0,
       "h3cevtModuleSw-LSB1SRP1NA1": h3cevtModuleSw_LSB1SRP1NA1,
       "h3cevtModuleSw-LSB1SRP1NA2": h3cevtModuleSw_LSB1SRP1NA2,
       "h3cevtModuleSw-LSB1SRP1NA3": h3cevtModuleSw_LSB1SRP1NA3,
       "h3cevtModuleSw-SR01AHP1GWA": h3cevtModuleSw_SR01AHP1GWA,
       "h3cevtModuleSw-SR01AHP2GWA": h3cevtModuleSw_SR01AHP2GWA,
       "h3cevtModuleSw-SR01CLP1GWA": h3cevtModuleSw_SR01CLP1GWA,
       "h3cevtModuleSw-SR01CLP2GWA": h3cevtModuleSw_SR01CLP2GWA,
       "h3cevtModuleSw-SR01ET16GWA": h3cevtModuleSw_SR01ET16GWA,
       "h3cevtModuleSw-SR01GP12VB": h3cevtModuleSw_SR01GP12VB,
       "h3cevtModuleSw-SR01XK1VB": h3cevtModuleSw_SR01XK1VB,
       "h3cevtModuleSw-SR01XP2VC": h3cevtModuleSw_SR01XP2VC,
       "h3cevtModuleSw-SR01XP4LVB": h3cevtModuleSw_SR01XP4LVB,
       "h3cevtModuleSw-SR01SRPUEA": h3cevtModuleSw_SR01SRPUEA,
       "h3cevtModuleSw-LSB1SRP1N4": h3cevtModuleSw_LSB1SRP1N4,
       "h3cevtModuleSw-LSB1SRP1N5": h3cevtModuleSw_LSB1SRP1N5,
       "h3cevtModuleSw-LSB1SRP1N6": h3cevtModuleSw_LSB1SRP1N6,
       "h3cevtModuleSw-LSB1SRP1N7": h3cevtModuleSw_LSB1SRP1N7,
       "h3cevtModuleSw-LSB1SRP2N4": h3cevtModuleSw_LSB1SRP2N4,
       "h3cevtModuleSw-LSB1SRP2N5": h3cevtModuleSw_LSB1SRP2N5,
       "h3cevtModuleSw-LSB1SRP2N6": h3cevtModuleSw_LSB1SRP2N6,
       "h3cevtModuleSw-LSB1SRP2N7": h3cevtModuleSw_LSB1SRP2N7,
       "h3cevtModuleSw-LSB1SRP1NA4": h3cevtModuleSw_LSB1SRP1NA4,
       "h3cevtModuleSw-LSB1SRP1NA5": h3cevtModuleSw_LSB1SRP1NA5,
       "h3cevtModuleSw-LSB1SRP1NA6": h3cevtModuleSw_LSB1SRP1NA6,
       "h3cevtModuleSw-LSB1SRP1NA7": h3cevtModuleSw_LSB1SRP1NA7,
       "h3cevtModuleSw-LSB2GV48DA": h3cevtModuleSw_LSB2GV48DA,
       "h3cevtModuleSw-LSB1RGP2GDB": h3cevtModuleSw_LSB1RGP2GDB,
       "h3cevtModuleSw-LSB1RGP4GDB": h3cevtModuleSw_LSB1RGP4GDB,
       "h3cevtModuleSw-LSB2GP24DB": h3cevtModuleSw_LSB2GP24DB,
       "h3cevtModuleSw-LSB2GP24DC": h3cevtModuleSw_LSB2GP24DC,
       "h3cevtModuleSw-LSB2GT24DB": h3cevtModuleSw_LSB2GT24DB,
       "h3cevtModuleSw-LSB2FW8DB": h3cevtModuleSw_LSB2FW8DB,
       "h3cevtModuleSw-LSB2IPSEC8DB": h3cevtModuleSw_LSB2IPSEC8DB,
       "h3cevtModuleSw-LSB2GV48DB": h3cevtModuleSw_LSB2GV48DB,
       "h3cevtModuleSw-RGP2": h3cevtModuleSw_RGP2,
       "h3cevtModuleSw-RGP4": h3cevtModuleSw_RGP4,
       "h3cevtModuleSw-SR02FW8VB": h3cevtModuleSw_SR02FW8VB,
       "h3cevtModuleSw-SR02IPSEC8VB": h3cevtModuleSw_SR02IPSEC8VB,
       "h3cevtModuleSw-LSB2SRP1N0": h3cevtModuleSw_LSB2SRP1N0,
       "h3cevtModuleSw-LSB2SRP1N1": h3cevtModuleSw_LSB2SRP1N1,
       "h3cevtModuleSw-LSB2SRP1N2": h3cevtModuleSw_LSB2SRP1N2,
       "h3cevtModuleSw-LSB2SRP1N3": h3cevtModuleSw_LSB2SRP1N3,
       "h3cevtModuleSw-LSB2SRP1N4": h3cevtModuleSw_LSB2SRP1N4,
       "h3cevtModuleSw-LSB2SRP1N5": h3cevtModuleSw_LSB2SRP1N5,
       "h3cevtModuleSw-LSB2SRP1N6": h3cevtModuleSw_LSB2SRP1N6,
       "h3cevtModuleSw-LSB2SRP1N7": h3cevtModuleSw_LSB2SRP1N7,
       "h3cevtModuleSw-SR02SRPUE": h3cevtModuleSw_SR02SRPUE,
       "h3cevtModuleSw-SR01LN1BQH0": h3cevtModuleSw_SR01LN1BQH0,
       "h3cevtModuleSw-SR01DXP1L": h3cevtModuleSw_SR01DXP1L,
       "h3cevtModuleSw-SR01DGP10L": h3cevtModuleSw_SR01DGP10L,
       "h3cevtModuleSw-SR01DRSP2L": h3cevtModuleSw_SR01DRSP2L,
       "h3cevtModuleSw-SR01DRUP1L": h3cevtModuleSw_SR01DRUP1L,
       "h3cevtModuleSw-SR01DGP20R": h3cevtModuleSw_SR01DGP20R,
       "h3cevtModuleSw-SR01DPLP8L": h3cevtModuleSw_SR01DPLP8L,
       "h3cevtModuleSw-SR01DXP2R": h3cevtModuleSw_SR01DXP2R,
       "h3cevtModuleSw-LSB1FW2A0": h3cevtModuleSw_LSB1FW2A0,
       "h3cevtModuleSw-LSB1GP48LDB": h3cevtModuleSw_LSB1GP48LDB,
       "h3cevtModuleSw-SR01LN1BNA0": h3cevtModuleSw_SR01LN1BNA0,
       "h3cevtModuleSw-SR01LN2BQH0": h3cevtModuleSw_SR01LN2BQH0,
       "h3cevtModuleSw-SR01LN2BNA0": h3cevtModuleSw_SR01LN2BNA0,
       "h3cevtModuleSw-SR01DGT20R": h3cevtModuleSw_SR01DGT20R,
       "h3cevtModuleSw-SR01DPSP4L": h3cevtModuleSw_SR01DPSP4L,
       "h3cevtModuleSw-SR01DPUP1L": h3cevtModuleSw_SR01DPUP1L,
       "h3cevtModuleSw-SR01DPL2G6L": h3cevtModuleSw_SR01DPL2G6L,
       "h3cevtModuleSw-SR01DPH2G6L": h3cevtModuleSw_SR01DPH2G6L,
       "h3cevtModuleSw-SR01DPS2G4L": h3cevtModuleSw_SR01DPS2G4L,
       "h3cevtModuleSw-SR01DCL1G8L": h3cevtModuleSw_SR01DCL1G8L,
       "h3cevtModuleSw-SR01DCL2G8L": h3cevtModuleSw_SR01DCL2G8L,
       "h3cevtModuleSw-SR01DET8G8L": h3cevtModuleSw_SR01DET8G8L,
       "h3cevtModuleSw-SR02SRP2E3": h3cevtModuleSw_SR02SRP2E3,
       "h3cevtModuleSw-SR02SRP1E3": h3cevtModuleSw_SR02SRP1E3,
       "h3cevtModuleSw-SR02SRP1M3": h3cevtModuleSw_SR02SRP1M3,
       "h3cevtModuleSw-SR01DQCP4L": h3cevtModuleSw_SR01DQCP4L,
       "h3cevtModuleSw-SR01DTCP8L": h3cevtModuleSw_SR01DTCP8L,
       "h3cevtModuleSw-LSB1AFC1A0": h3cevtModuleSw_LSB1AFC1A0,
       "h3cevtModuleSw-LSB1SSL1A0": h3cevtModuleSw_LSB1SSL1A0,
       "h3cevtModuleSw-IMNAM": h3cevtModuleSw_IMNAM,
       "h3cevtModuleSw-IMNAT": h3cevtModuleSw_IMNAT,
       "h3cevtModuleSw-PICAHP1L": h3cevtModuleSw_PICAHP1L,
       "h3cevtModuleSw-PICALP4L": h3cevtModuleSw_PICALP4L,
       "h3cevtModuleSw-PICCHP4L": h3cevtModuleSw_PICCHP4L,
       "h3cevtModuleSw-PICCHS1G4L": h3cevtModuleSw_PICCHS1G4L,
       "h3cevtModuleSw-PICCLS4G4L": h3cevtModuleSw_PICCLS4G4L,
       "h3cevtModuleSw-PICCSP1L": h3cevtModuleSw_PICCSP1L,
       "h3cevtModuleSw-LSB1ACG1A0": h3cevtModuleSw_LSB1ACG1A0,
       "h3cevtModuleSw-LST1MRPNC1": h3cevtModuleSw_LST1MRPNC1,
       "h3cevtModuleSw-LST1SF18B1": h3cevtModuleSw_LST1SF18B1,
       "h3cevtModuleSw-LST1SF08B1": h3cevtModuleSw_LST1SF08B1,
       "h3cevtModuleSw-LST1GT48LEC1": h3cevtModuleSw_LST1GT48LEC1,
       "h3cevtModuleSw-LST1GP48LEC1": h3cevtModuleSw_LST1GP48LEC1,
       "h3cevtModuleSw-LST1XP4LEC1": h3cevtModuleSw_LST1XP4LEC1,
       "h3cevtModuleSw-LST1XP8LEC1": h3cevtModuleSw_LST1XP8LEC1,
       "h3cevtModuleSw-LSR1SRP2B1": h3cevtModuleSw_LSR1SRP2B1,
       "h3cevtModuleSw-LSR1SRP2C1": h3cevtModuleSw_LSR1SRP2C1,
       "h3cevtModuleSw-LSR1SRP2B2": h3cevtModuleSw_LSR1SRP2B2,
       "h3cevtModuleSw-LSR1SRP2C2": h3cevtModuleSw_LSR1SRP2C2,
       "h3cevtModuleSw-LSR1GT24LEC1": h3cevtModuleSw_LSR1GT24LEC1,
       "h3cevtModuleSw-LSR1GP24LEB1": h3cevtModuleSw_LSR1GP24LEB1,
       "h3cevtModuleSw-LSR1GP24LEC1": h3cevtModuleSw_LSR1GP24LEC1,
       "h3cevtModuleSw-LSR1GT48LEB1": h3cevtModuleSw_LSR1GT48LEB1,
       "h3cevtModuleSw-LSR1GT48LEC1": h3cevtModuleSw_LSR1GT48LEC1,
       "h3cevtModuleSw-LSR1GP48LEB1": h3cevtModuleSw_LSR1GP48LEB1,
       "h3cevtModuleSw-LSR1GP48LEC1": h3cevtModuleSw_LSR1GP48LEC1,
       "h3cevtModuleSw-LSR2GV48REB1": h3cevtModuleSw_LSR2GV48REB1,
       "h3cevtModuleSw-LSR1XP2LEB1": h3cevtModuleSw_LSR1XP2LEB1,
       "h3cevtModuleSw-LSR1XP2LEC1": h3cevtModuleSw_LSR1XP2LEC1,
       "h3cevtModuleSw-LSR1XP4LEB1": h3cevtModuleSw_LSR1XP4LEB1,
       "h3cevtModuleSw-LSR1XP4LEC1": h3cevtModuleSw_LSR1XP4LEC1,
       "h3cevtModuleSw-IMFW": h3cevtModuleSw_IMFW,
       "h3cevtModuleSw-LSB1LB1A0": h3cevtModuleSw_LSB1LB1A0,
       "h3cevtModuleSw-LSB1IPS1A0": h3cevtModuleSw_LSB1IPS1A0,
       "h3cevtModuleSw-LST1GT48LEB1": h3cevtModuleSw_LST1GT48LEB1,
       "h3cevtModuleSw-LST1GP48LEB1": h3cevtModuleSw_LST1GP48LEB1,
       "h3cevtModuleSw-LST1XP4LEB1": h3cevtModuleSw_LST1XP4LEB1,
       "h3cevtModuleSw-LST1XP8LEB1": h3cevtModuleSw_LST1XP8LEB1,
       "h3cevtModuleSw-LST1XP32REB1": h3cevtModuleSw_LST1XP32REB1,
       "h3cevtModuleSw-LST1XP32REC1": h3cevtModuleSw_LST1XP32REC1,
       "h3cevtModuleSw-LSR1FW2A1": h3cevtModuleSw_LSR1FW2A1,
       "h3cevtModuleSw-LSR1SSL1A1": h3cevtModuleSw_LSR1SSL1A1,
       "h3cevtModuleSw-SR01DET32G2L": h3cevtModuleSw_SR01DET32G2L,
       "h3cevtModuleSw-LSR1GP24LEF1": h3cevtModuleSw_LSR1GP24LEF1,
       "h3cevtModuleSw-LSR1XP4LEF1": h3cevtModuleSw_LSR1XP4LEF1,
       "h3cevtModuleSw-LSR1LB1A1": h3cevtModuleSw_LSR1LB1A1,
       "h3cevtModuleSw-LSR1NSM1A1": h3cevtModuleSw_LSR1NSM1A1,
       "h3cevtModuleSw-LSR1ACG1A1": h3cevtModuleSw_LSR1ACG1A1,
       "h3cevtModuleSw-LSR1IPS1A1": h3cevtModuleSw_LSR1IPS1A1,
       "h3cevtModuleSw-LSR2GP24LEB1": h3cevtModuleSw_LSR2GP24LEB1,
       "h3cevtModuleSw-LSR2GT24LEB1": h3cevtModuleSw_LSR2GT24LEB1,
       "h3cevtModuleSw-LSR2GT48LEB1": h3cevtModuleSw_LSR2GT48LEB1,
       "h3cevtModuleSw-SPC-GP24L": h3cevtModuleSw_SPC_GP24L,
       "h3cevtModuleSw-SPC-GT48L": h3cevtModuleSw_SPC_GT48L,
       "h3cevtModuleSw-SPC-GP48L": h3cevtModuleSw_SPC_GP48L,
       "h3cevtModuleSw-SPC-XP2L": h3cevtModuleSw_SPC_XP2L,
       "h3cevtModuleSw-SPC-XP4L": h3cevtModuleSw_SPC_XP4L,
       "h3cevtModuleSw-SR06SRP2E3": h3cevtModuleSw_SR06SRP2E3,
       "h3cevtModuleSw-SPE-2010-E": h3cevtModuleSw_SPE_2010_E,
       "h3cevtModuleSw-SPE-2020-E": h3cevtModuleSw_SPE_2020_E,
       "h3cevtModuleSw-SPC-XP4L-S-SDI": h3cevtModuleSw_SPC_XP4L_S_SDI,
       "h3cevtModuleSw-SPC-GT48L-SDI": h3cevtModuleSw_SPC_GT48L_SDI,
       "h3cevtModuleSw-SPC-GP48L-S-SDI": h3cevtModuleSw_SPC_GP48L_S_SDI,
       "h3cevtModuleSw-SPC-SR02OPMA0": h3cevtModuleSw_SPC_SR02OPMA0,
       "h3cevtModuleSw-LSR1XP16REB1": h3cevtModuleSw_LSR1XP16REB1,
       "h3cevtModuleSw-LSR1GP48LEF1": h3cevtModuleSw_LSR1GP48LEF1,
       "h3cevtModuleSw-LST1GP48LEF1": h3cevtModuleSw_LST1GP48LEF1,
       "h3cevtModuleSw-LST1XP8LEF1": h3cevtModuleSw_LST1XP8LEF1,
       "h3cevtModuleSw-SPE-1010-II": h3cevtModuleSw_SPE_1010_II,
       "h3cevtModuleSw-SPE-1010-E-II": h3cevtModuleSw_SPE_1010_E_II,
       "h3cevtModuleSw-SPE-1020-II": h3cevtModuleSw_SPE_1020_II,
       "h3cevtModuleSw-SPE-1020-E-II": h3cevtModuleSw_SPE_1020_E_II,
       "h3cevtModuleSw-LST1FW2A1": h3cevtModuleSw_LST1FW2A1,
       "h3cevtModuleSw-LST1NSM1A1": h3cevtModuleSw_LST1NSM1A1,
       "h3cevtModuleSw-LST1LB1A1": h3cevtModuleSw_LST1LB1A1,
       "h3cevtModuleSw-LST1ACG1A1": h3cevtModuleSw_LST1ACG1A1,
       "h3cevtModuleSw-LST1IPS1A1": h3cevtModuleSw_LST1IPS1A1,
       "h3cevtModuleSw-LSR1DRUP1L1": h3cevtModuleSw_LSR1DRUP1L1,
       "h3cevtModuleSw-LSR1DPUP1L1": h3cevtModuleSw_LSR1DPUP1L1,
       "h3cevtModuleSw-LSR1DPSP4L1": h3cevtModuleSw_LSR1DPSP4L1,
       "h3cevtModuleSw-LSR1DTCP8L1": h3cevtModuleSw_LSR1DTCP8L1,
       "h3cevtModuleSw-LSR1DXP1L1": h3cevtModuleSw_LSR1DXP1L1,
       "h3cevtModuleSw-LSR1DGP10L1": h3cevtModuleSw_LSR1DGP10L1,
       "h3cevtModuleSw-LSR1LN1BNL1": h3cevtModuleSw_LSR1LN1BNL1,
       "h3cevtModuleSw-LSR1LN2BL1": h3cevtModuleSw_LSR1LN2BL1,
       "h3cevtModuleSw-LSR1SRP2D1": h3cevtModuleSw_LSR1SRP2D1,
       "h3cevtModuleSw-IM-NAT-II": h3cevtModuleSw_IM_NAT_II,
       "h3cevtModuleSw-IM-NAM-II": h3cevtModuleSw_IM_NAM_II,
       "h3cevtModuleSw-CR-MRP-I": h3cevtModuleSw_CR_MRP_I,
       "h3cevtModuleSw-CR-SF18C": h3cevtModuleSw_CR_SF18C,
       "h3cevtModuleSw-CR-SF08C": h3cevtModuleSw_CR_SF08C,
       "h3cevtModuleSw-CR-SPC-XP8LEF": h3cevtModuleSw_CR_SPC_XP8LEF,
       "h3cevtModuleSw-CR-SPC-XP4LEF": h3cevtModuleSw_CR_SPC_XP4LEF,
       "h3cevtModuleSw-CR-SPC-GP48LEF": h3cevtModuleSw_CR_SPC_GP48LEF,
       "h3cevtModuleSw-CR-SPC-GT48LEF": h3cevtModuleSw_CR_SPC_GT48LEF,
       "h3cevtModuleSw-CR-SPE-3020-E": h3cevtModuleSw_CR_SPE_3020_E,
       "h3cevtModuleSw-CR-SPC-PUP4L-E": h3cevtModuleSw_CR_SPC_PUP4L_E,
       "h3cevtModuleSw-LST1SF08C1": h3cevtModuleSw_LST1SF08C1,
       "h3cevtModuleSw-LST1SF18C1": h3cevtModuleSw_LST1SF18C1,
       "h3cevtModuleSw-LS81GP16TM": h3cevtModuleSw_LS81GP16TM,
       "h3cevtModuleSw-LS81VP4C": h3cevtModuleSw_LS81VP4C,
       "h3cevtModuleSw-LS8M1PT8P0": h3cevtModuleSw_LS8M1PT8P0,
       "h3cevtModuleSw-LS8M1PT8GB0": h3cevtModuleSw_LS8M1PT8GB0,
       "h3cevtModuleSw-LS8M1PT4GB0": h3cevtModuleSw_LS8M1PT4GB0,
       "h3cevtModuleSw-LS81GP2R": h3cevtModuleSw_LS81GP2R,
       "h3cevtModuleSw-LS81GP4R": h3cevtModuleSw_LS81GP4R,
       "h3cevtModuleSw-LS81IPSECA": h3cevtModuleSw_LS81IPSECA,
       "h3cevtModuleSw-LS81FWA": h3cevtModuleSw_LS81FWA,
       "h3cevtModuleSw-LS82VSNP": h3cevtModuleSw_LS82VSNP,
       "h3cevtModuleSw-LSQ1GV48SA": h3cevtModuleSw_LSQ1GV48SA,
       "h3cevtModuleSw-LSQ1SRPB": h3cevtModuleSw_LSQ1SRPB,
       "h3cevtModuleSw-LSQ1SRP2XB": h3cevtModuleSw_LSQ1SRP2XB,
       "h3cevtModuleSw-LSQ1SRP1CB": h3cevtModuleSw_LSQ1SRP1CB,
       "h3cevtModuleSw-LSQ1FV48SA": h3cevtModuleSw_LSQ1FV48SA,
       "h3cevtModuleSw-LSD1MPUA": h3cevtModuleSw_LSD1MPUA,
       "h3cevtModuleSw-LSD1GP20A0": h3cevtModuleSw_LSD1GP20A0,
       "h3cevtModuleSw-LSD1GP20TA0": h3cevtModuleSw_LSD1GP20TA0,
       "h3cevtModuleSw-LSD1GP36A0": h3cevtModuleSw_LSD1GP36A0,
       "h3cevtModuleSw-LSD1GP20XA0": h3cevtModuleSw_LSD1GP20XA0,
       "h3cevtModuleSw-LSD1GP20EA0": h3cevtModuleSw_LSD1GP20EA0,
       "h3cevtModuleSw-LSD1GP20RA0": h3cevtModuleSw_LSD1GP20RA0,
       "h3cevtModuleSw-LSD1GP16A0": h3cevtModuleSw_LSD1GP16A0,
       "h3cevtModuleSw-LSD1GT16A0": h3cevtModuleSw_LSD1GT16A0,
       "h3cevtModuleSw-LSD1XP2A0": h3cevtModuleSw_LSD1XP2A0,
       "h3cevtModuleSw-LSD1EP2A0": h3cevtModuleSw_LSD1EP2A0,
       "h3cevtModuleSw-LSD1RP2A0": h3cevtModuleSw_LSD1RP2A0,
       "h3cevtModuleSw-LSQ1GV48SC": h3cevtModuleSw_LSQ1GV48SC,
       "h3cevtModuleSw-LSQ1FP48SA": h3cevtModuleSw_LSQ1FP48SA,
       "h3cevtModuleSw-LSQ1GP24SC": h3cevtModuleSw_LSQ1GP24SC,
       "h3cevtModuleSw-LSQ1GT24SC": h3cevtModuleSw_LSQ1GT24SC,
       "h3cevtModuleSw-LSQ1TGX2SC": h3cevtModuleSw_LSQ1TGX2SC,
       "h3cevtModuleSw-LSQ1GP12EA": h3cevtModuleSw_LSQ1GP12EA,
       "h3cevtModuleSw-LSQ1TGX1EA": h3cevtModuleSw_LSQ1TGX1EA,
       "h3cevtModuleSw-LSQ1P24XGSC": h3cevtModuleSw_LSQ1P24XGSC,
       "h3cevtModuleSw-LSQ1T24XGSC": h3cevtModuleSw_LSQ1T24XGSC,
       "h3cevtModuleSw-LS81TGX1B": h3cevtModuleSw_LS81TGX1B,
       "h3cevtModuleSw-LSQ1PT4PSC0": h3cevtModuleSw_LSQ1PT4PSC0,
       "h3cevtModuleSw-LS81SRPG13": h3cevtModuleSw_LS81SRPG13,
       "h3cevtModuleSw-LS81SRPG14": h3cevtModuleSw_LS81SRPG14,
       "h3cevtModuleSw-LS81SRPG15": h3cevtModuleSw_LS81SRPG15,
       "h3cevtModuleSw-LSQ1GP48SC0": h3cevtModuleSw_LSQ1GP48SC0,
       "h3cevtModuleSw-LSQ1GP12SC0": h3cevtModuleSw_LSQ1GP12SC0,
       "h3cevtModuleSw-LSD1SRPA": h3cevtModuleSw_LSD1SRPA,
       "h3cevtModuleSw-LSD1SRPB": h3cevtModuleSw_LSD1SRPB,
       "h3cevtModuleSw-LSD1SRPC": h3cevtModuleSw_LSD1SRPC,
       "h3cevtModuleSw-LSD1GT16PES0": h3cevtModuleSw_LSD1GT16PES0,
       "h3cevtModuleSw-LSD1GP24ES0": h3cevtModuleSw_LSD1GP24ES0,
       "h3cevtModuleSw-LSD1GT24XES0": h3cevtModuleSw_LSD1GT24XES0,
       "h3cevtModuleSw-LSD1GP24XES0": h3cevtModuleSw_LSD1GP24XES0,
       "h3cevtModuleSw-LSD1XP2ES0": h3cevtModuleSw_LSD1XP2ES0,
       "h3cevtModuleSw-LSD1GP48ES0": h3cevtModuleSw_LSD1GP48ES0,
       "h3cevtModuleSw-LSQ1MPUA0": h3cevtModuleSw_LSQ1MPUA0,
       "h3cevtModuleSw-LSQ1MPUA1": h3cevtModuleSw_LSQ1MPUA1,
       "h3cevtModuleSw-LSQ1FWBSC0": h3cevtModuleSw_LSQ1FWBSC0,
       "h3cevtModuleSw-LSQ1PT8PSC0": h3cevtModuleSw_LSQ1PT8PSC0,
       "h3cevtModuleSw-LSQ1PT16PSC0": h3cevtModuleSw_LSQ1PT16PSC0,
       "h3cevtModuleSw-SA11MPUA0": h3cevtModuleSw_SA11MPUA0,
       "h3cevtModuleSw-SA11MPUB0": h3cevtModuleSw_SA11MPUB0,
       "h3cevtModuleSw-LSQ1AFCBSC0": h3cevtModuleSw_LSQ1AFCBSC0,
       "h3cevtModuleSw-LSQ1MPUB0": h3cevtModuleSw_LSQ1MPUB0,
       "h3cevtModuleSw-LSQ1MPUB1": h3cevtModuleSw_LSQ1MPUB1,
       "h3cevtModuleSw-LSQ1PT4PSC1": h3cevtModuleSw_LSQ1PT4PSC1,
       "h3cevtModuleSw-LSQ1PT8PSC1": h3cevtModuleSw_LSQ1PT8PSC1,
       "h3cevtModuleSw-LSQ1PT16PSC1": h3cevtModuleSw_LSQ1PT16PSC1,
       "h3cevtModuleSw-LSQ1FP48USA0": h3cevtModuleSw_LSQ1FP48USA0,
       "h3cevtModuleSw-LSQ1FP48USA1": h3cevtModuleSw_LSQ1FP48USA1,
       "h3cevtModuleSw-LSQ1FV48USA0": h3cevtModuleSw_LSQ1FV48USA0,
       "h3cevtModuleSw-LSQ1FV48USA1": h3cevtModuleSw_LSQ1FV48USA1,
       "h3cevtModuleSw-LSQ1SRPD0": h3cevtModuleSw_LSQ1SRPD0,
       "h3cevtModuleSw-LSQ1CGP24TSC0": h3cevtModuleSw_LSQ1CGP24TSC0,
       "h3cevtModuleSw-LSQ1GP24TSC0": h3cevtModuleSw_LSQ1GP24TSC0,
       "h3cevtModuleSw-LSQ1ACGASC0": h3cevtModuleSw_LSQ1ACGASC0,
       "h3cevtModuleSw-LSD1XP1ES0": h3cevtModuleSw_LSD1XP1ES0,
       "h3cevtModuleSw-LSD1GP12ES0": h3cevtModuleSw_LSD1GP12ES0,
       "h3cevtModuleSw-LSQ1SRP12GB0": h3cevtModuleSw_LSQ1SRP12GB0,
       "h3cevtModuleSw-LSQ1GV40PSC0": h3cevtModuleSw_LSQ1GV40PSC0,
       "h3cevtModuleSw-LSQ1FWBSC1": h3cevtModuleSw_LSQ1FWBSC1,
       "h3cevtModuleSw-LSQ1NSMSC0": h3cevtModuleSw_LSQ1NSMSC0,
       "h3cevtModuleSw-LSQ1NSMSC1": h3cevtModuleSw_LSQ1NSMSC1,
       "h3cevtModuleSw-LSQ1AFDBSC0": h3cevtModuleSw_LSQ1AFDBSC0,
       "h3cevtModuleSw-LS81MPUB": h3cevtModuleSw_LS81MPUB,
       "h3cevtModuleSw-LS81FP48XL": h3cevtModuleSw_LS81FP48XL,
       "h3cevtModuleSw-LS81FT48XL": h3cevtModuleSw_LS81FT48XL,
       "h3cevtModuleSw-LS81GP12XL": h3cevtModuleSw_LS81GP12XL,
       "h3cevtModuleSw-LS81GP24XL": h3cevtModuleSw_LS81GP24XL,
       "h3cevtModuleSw-LS81GP48XL": h3cevtModuleSw_LS81GP48XL,
       "h3cevtModuleSw-LS81GT24XL": h3cevtModuleSw_LS81GT24XL,
       "h3cevtModuleSw-LS81GT48XL": h3cevtModuleSw_LS81GT48XL,
       "h3cevtModuleSw-LS81TGX2XL": h3cevtModuleSw_LS81TGX2XL,
       "h3cevtModuleSw-LSQ1GV48SD0": h3cevtModuleSw_LSQ1GV48SD0,
       "h3cevtModuleSw-LSQ1GP48EB0": h3cevtModuleSw_LSQ1GP48EB0,
       "h3cevtModuleSw-LSQ1IPSSC0": h3cevtModuleSw_LSQ1IPSSC0,
       "h3cevtModuleSw-LSQ1GV48SD1": h3cevtModuleSw_LSQ1GV48SD1,
       "h3cevtModuleSw-LSQ1GP48SD0": h3cevtModuleSw_LSQ1GP48SD0,
       "h3cevtModuleSw-LSQ1GP48SD1": h3cevtModuleSw_LSQ1GP48SD1,
       "h3cevtModuleSw-LSQ1SRPA0": h3cevtModuleSw_LSQ1SRPA0,
       "h3cevtModuleSw-LSQ1SRPA1": h3cevtModuleSw_LSQ1SRPA1,
       "h3cevtModuleSw-LSQ2FP48SA0": h3cevtModuleSw_LSQ2FP48SA0,
       "h3cevtModuleSw-LSQ2FP48SA1": h3cevtModuleSw_LSQ2FP48SA1,
       "h3cevtModuleSw-LSQ2FT48SA0": h3cevtModuleSw_LSQ2FT48SA0,
       "h3cevtModuleSw-LSQ2FT48SA1": h3cevtModuleSw_LSQ2FT48SA1,
       "h3cevtModuleSw-LSQ1GV24PSC0": h3cevtModuleSw_LSQ1GV24PSC0,
       "h3cevtModuleSw-LSQ1GV24PSC1": h3cevtModuleSw_LSQ1GV24PSC1,
       "h3cevtModuleSw-LSQ1CGV24PSC0": h3cevtModuleSw_LSQ1CGV24PSC0,
       "h3cevtModuleSw-LSQ1CGV24PSC1": h3cevtModuleSw_LSQ1CGV24PSC1,
       "h3cevtModuleSw-LSQ1GP24TEB0": h3cevtModuleSw_LSQ1GP24TEB0,
       "h3cevtModuleSw-LSQ1GP24TEB1": h3cevtModuleSw_LSQ1GP24TEB1,
       "h3cevtModuleSw-LSQ1GP24TSD0": h3cevtModuleSw_LSQ1GP24TSD0,
       "h3cevtModuleSw-LSQ1GP24TSD1": h3cevtModuleSw_LSQ1GP24TSD1,
       "h3cevtModuleSw-LSQ1GP24TXSD0": h3cevtModuleSw_LSQ1GP24TXSD0,
       "h3cevtModuleSw-LSQ1GP24TXSD1": h3cevtModuleSw_LSQ1GP24TXSD1,
       "h3cevtModuleSw-LSQ1TGX2EB0": h3cevtModuleSw_LSQ1TGX2EB0,
       "h3cevtModuleSw-LSQ1TGX2EB1": h3cevtModuleSw_LSQ1TGX2EB1,
       "h3cevtModuleSw-LSQ1TGX2SD0": h3cevtModuleSw_LSQ1TGX2SD0,
       "h3cevtModuleSw-LSQ1TGX2SD1": h3cevtModuleSw_LSQ1TGX2SD1,
       "h3cevtModuleSw-LSQ1TGX4SD0": h3cevtModuleSw_LSQ1TGX4SD0,
       "h3cevtModuleSw-LSQ1TGX4SD1": h3cevtModuleSw_LSQ1TGX4SD1,
       "h3cevtModuleSw-LSQ1TGX8SD0": h3cevtModuleSw_LSQ1TGX8SD0,
       "h3cevtModuleSw-LSQ1TGX8SD1": h3cevtModuleSw_LSQ1TGX8SD1,
       "h3cevtModuleSw-LSQ1GP48EB1": h3cevtModuleSw_LSQ1GP48EB1,
       "h3cevtModuleSw-LSQ1TGX4EB0": h3cevtModuleSw_LSQ1TGX4EB0,
       "h3cevtModuleSw-LSQ1TGX4EB1": h3cevtModuleSw_LSQ1TGX4EB1,
       "h3cevtModuleSw-LSQ1GP12SC3": h3cevtModuleSw_LSQ1GP12SC3,
       "h3cevtModuleSw-LSQ1GP24TSC3": h3cevtModuleSw_LSQ1GP24TSC3,
       "h3cevtModuleSw-LSQ1GP48SC3": h3cevtModuleSw_LSQ1GP48SC3,
       "h3cevtModuleSw-LSQ1GV48SC3": h3cevtModuleSw_LSQ1GV48SC3,
       "h3cevtModuleSw-LSQ1MPUA3": h3cevtModuleSw_LSQ1MPUA3,
       "h3cevtModuleSw-LSQ1SRP1CB3": h3cevtModuleSw_LSQ1SRP1CB3,
       "h3cevtModuleSw-LSQ1SRPA3": h3cevtModuleSw_LSQ1SRPA3,
       "h3cevtModuleSw-LSQ2FP48SA3": h3cevtModuleSw_LSQ2FP48SA3,
       "h3cevtModuleSw-LSQ2FT48SA3": h3cevtModuleSw_LSQ2FT48SA3,
       "h3cevtModuleSw-LSQ1MPUB3": h3cevtModuleSw_LSQ1MPUB3,
       "h3cevtModuleSw-LSQ1CGP24TSC3": h3cevtModuleSw_LSQ1CGP24TSC3,
       "h3cevtModuleSw-LSQ1MPUB4": h3cevtModuleSw_LSQ1MPUB4,
       "h3cevtModuleSw-LSQ1SRPD4": h3cevtModuleSw_LSQ1SRPD4,
       "h3cevtModuleSw-LSQ1SSLSC0": h3cevtModuleSw_LSQ1SSLSC0,
       "h3cevtModuleSw-LSQ1LBSC0": h3cevtModuleSw_LSQ1LBSC0,
       "h3cevtModuleSw-LSQ1NAT24SC0": h3cevtModuleSw_LSQ1NAT24SC0,
       "h3cevtModuleSw-LSQ1SRP12GB4": h3cevtModuleSw_LSQ1SRP12GB4,
       "h3cevtModuleSw-LSQ1TGS8SC0": h3cevtModuleSw_LSQ1TGS8SC0,
       "h3cevtModuleSw-LSQ3PT4PSC0": h3cevtModuleSw_LSQ3PT4PSC0,
       "h3cevtModuleSw-EWPXM2MPUB0": h3cevtModuleSw_EWPXM2MPUB0,
       "h3cevtModuleSw-EWPXM2SRP12GB0": h3cevtModuleSw_EWPXM2SRP12GB0,
       "h3cevtModuleSw-EWPXM2SRPD0": h3cevtModuleSw_EWPXM2SRPD0,
       "h3cevtModuleSw-EWPXM2GP24TSD0": h3cevtModuleSw_EWPXM2GP24TSD0,
       "h3cevtModuleSw-EWPXM2GP24TXSD0": h3cevtModuleSw_EWPXM2GP24TXSD0,
       "h3cevtModuleSw-EWPXM2TGX4SD0": h3cevtModuleSw_EWPXM2TGX4SD0,
       "h3cevtModuleSw-EWPXM2GP48SD0": h3cevtModuleSw_EWPXM2GP48SD0,
       "h3cevtModuleSw-EWPXM2GP24TSC0": h3cevtModuleSw_EWPXM2GP24TSC0,
       "h3cevtModuleSw-EWPXM2TGX2SC0": h3cevtModuleSw_EWPXM2TGX2SC0,
       "h3cevtModuleSw-EWPXM2GP48SC0": h3cevtModuleSw_EWPXM2GP48SC0,
       "h3cevtModuleSw-LS7500-GP48-SC": h3cevtModuleSw_LS7500_GP48_SC,
       "h3cevtModuleSw-LS7500-GP48-SD": h3cevtModuleSw_LS7500_GP48_SD,
       "h3cevtModuleSw-LS7500-GT48-SC": h3cevtModuleSw_LS7500_GT48_SC,
       "h3cevtModuleSw-LS7500-GT48-SD": h3cevtModuleSw_LS7500_GT48_SD,
       "h3cevtModuleSw-LS7500-SRPG1": h3cevtModuleSw_LS7500_SRPG1,
       "h3cevtModuleSw-LS7500-SRPG2": h3cevtModuleSw_LS7500_SRPG2,
       "h3cevtModuleSw-LS7500-XP4-SD": h3cevtModuleSw_LS7500_XP4_SD,
       "h3cevtModuleSw-LS7500-XP8-SD": h3cevtModuleSw_LS7500_XP8_SD,
       "h3cevtModuleSw-LSQ4PT4PSC0": h3cevtModuleSw_LSQ4PT4PSC0,
       "h3cevtModuleSw-LSQ4PT8PSC0": h3cevtModuleSw_LSQ4PT8PSC0,
       "h3cevtModuleSw-LSQ4PT16PSC0": h3cevtModuleSw_LSQ4PT16PSC0,
       "h3cevtModuleSw-LSQ1GP24TSA0": h3cevtModuleSw_LSQ1GP24TSA0,
       "h3cevtModuleSw-LSQ1GV24PSA0": h3cevtModuleSw_LSQ1GV24PSA0,
       "h3cevtModuleSw-LSQ1SRPD3": h3cevtModuleSw_LSQ1SRPD3,
       "h3cevtModuleSw-LSQ1SUPA0": h3cevtModuleSw_LSQ1SUPA0,
       "h3cevtModuleSw-LSU1FAB04A0": h3cevtModuleSw_LSU1FAB04A0,
       "h3cevtModuleSw-LSU1FAB08A0": h3cevtModuleSw_LSU1FAB08A0,
       "h3cevtModuleSw-LSU1TGS8EA0": h3cevtModuleSw_LSU1TGS8EA0,
       "h3cevtModuleSw-LSU1TGS8EB0": h3cevtModuleSw_LSU1TGS8EB0,
       "h3cevtModuleSw-LSU1TGS8SE0": h3cevtModuleSw_LSU1TGS8SE0,
       "h3cevtModuleSw-LSUTGS16SC0": h3cevtModuleSw_LSUTGS16SC0,
       "h3cevtModuleSw-LUS1SUPA0": h3cevtModuleSw_LUS1SUPA0,
       "h3cevtModuleSw-LSU1GP24TXEA0": h3cevtModuleSw_LSU1GP24TXEA0,
       "h3cevtModuleSw-LSU1GP24TXEB0": h3cevtModuleSw_LSU1GP24TXEB0,
       "h3cevtModuleSw-LSU1GP24TXSE0": h3cevtModuleSw_LSU1GP24TXSE0,
       "h3cevtModuleSw-LSU1GP48EA0": h3cevtModuleSw_LSU1GP48EA0,
       "h3cevtModuleSw-LSU1GP48EB0": h3cevtModuleSw_LSU1GP48EB0,
       "h3cevtModuleSw-LSU1GP48SE0": h3cevtModuleSw_LSU1GP48SE0,
       "h3cevtModuleSw-LSU1GT48EA0": h3cevtModuleSw_LSU1GT48EA0,
       "h3cevtModuleSw-LSU1GT48SE0": h3cevtModuleSw_LSU1GT48SE0,
       "h3cevtModuleSw-LSU1TGX4EA0": h3cevtModuleSw_LSU1TGX4EA0,
       "h3cevtModuleSw-LSU1TGX4EB0": h3cevtModuleSw_LSU1TGX4EB0,
       "h3cevtModuleSw-LSU1TGX4SE0": h3cevtModuleSw_LSU1TGX4SE0,
       "h3cevtModuleSw-LSQ1FAB08A0": h3cevtModuleSw_LSQ1FAB08A0,
       "h3cevtModuleSw-EWPX2WCMD0": h3cevtModuleSw_EWPX2WCMD0,
       "h3cevtModuleSw-LSQ1WCMD0": h3cevtModuleSw_LSQ1WCMD0,
       "h3cevtModuleSw-LSQ1IAGSC0": h3cevtModuleSw_LSQ1IAGSC0,
       "h3cevtModuleSw-LSU1GP24TSE0": h3cevtModuleSw_LSU1GP24TSE0,
       "h3cevtModuleSw-LSQ1TGS16SC0": h3cevtModuleSw_LSQ1TGS16SC0,
       "h3cevtModuleSw-EWPX2TGS16SC0": h3cevtModuleSw_EWPX2TGS16SC0,
       "h3cevtModuleSw-LSQ1SUPA3": h3cevtModuleSw_LSQ1SUPA3,
       "h3cevtModuleSw-LSQ1FAB04A3": h3cevtModuleSw_LSQ1FAB04A3,
       "h3cevtModuleSw-LSQ1FAB08A3": h3cevtModuleSw_LSQ1FAB08A3,
       "h3cevtModuleSw-LSQ1GT48SC0": h3cevtModuleSw_LSQ1GT48SC0,
       "h3cevtModuleSw-LSR2SRP2C1": h3cevtModuleSw_LSR2SRP2C1,
       "h3cevtModuleSw-LSR2SRP2C2": h3cevtModuleSw_LSR2SRP2C2,
       "h3cevtModuleSw-1000BASE-X-COMBO": h3cevtModuleSw_1000BASE_X_COMBO,
       "h3cevtModuleSw-EPON-1000M": h3cevtModuleSw_EPON_1000M,
       "h3cevtModuleSw-1000BASE-FIXED-2SFP-T-2RJ45": h3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45,
       "h3cevtModuleSw-100M-1550-BIDI": h3cevtModuleSw_100M_1550_BIDI,
       "h3cevtModuleSw-100M-1310-BIDI": h3cevtModuleSw_100M_1310_BIDI,
       "h3cevtModuleSw-1000BASE-FIXED-4RJ45-4SFP-COMBO": h3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO,
       "h3cevtModuleSw-LSH1PK2T": h3cevtModuleSw_LSH1PK2T,
       "h3cevtModuleSw-LSPM2GP2P": h3cevtModuleSw_LSPM2GP2P,
       "h3cevtModuleSw-LSWM1GT16P": h3cevtModuleSw_LSWM1GT16P,
       "h3cevtModuleSw-LSWM1GP16P": h3cevtModuleSw_LSWM1GP16P,
       "h3cevtModuleSw-LSWM1XP2P": h3cevtModuleSw_LSWM1XP2P,
       "h3cevtModuleSw-LSWM1XP4P": h3cevtModuleSw_LSWM1XP4P,
       "h3cevtModuleSw-LSWM1SP2P": h3cevtModuleSw_LSWM1SP2P,
       "h3cevtModuleSw-LSWM1SP4P": h3cevtModuleSw_LSWM1SP4P,
       "h3cevtModuleSw-LSWM148POEM": h3cevtModuleSw_LSWM148POEM,
       "h3cevtModuleSw-LSWM1FW10": h3cevtModuleSw_LSWM1FW10,
       "h3cevtModuleSw-LSWM1WCM10": h3cevtModuleSw_LSWM1WCM10,
       "h3cevtModuleSw-LSWM1IPS10": h3cevtModuleSw_LSWM1IPS10,
       "h3cevtModuleSw-LSWM1WCM20": h3cevtModuleSw_LSWM1WCM20,
       "h3cevtModuleSw-IPS-T1000-M": h3cevtModuleSw_IPS_T1000_M,
       "h3cevtModuleSw-IPS-T1000-A": h3cevtModuleSw_IPS_T1000_A,
       "h3cevtModuleSw-IPS-T1000-S": h3cevtModuleSw_IPS_T1000_S,
       "h3cevtModuleSw-IPS-GX4C": h3cevtModuleSw_IPS_GX4C,
       "h3cevtModuleSw-IPS-GT4C": h3cevtModuleSw_IPS_GT4C,
       "h3cevtModuleSw-LSPM2SP2P": h3cevtModuleSw_LSPM2SP2P,
       "h3cevtModuleSw-LSPM2SP2PA": h3cevtModuleSw_LSPM2SP2PA,
       "h3cevtModuleSw-LSP5GP8P": h3cevtModuleSw_LSP5GP8P,
       "h3cevtModuleSw-LSP5GT8P": h3cevtModuleSw_LSP5GT8P,
       "h3cevtModuleSw-LSWM1FC4P": h3cevtModuleSw_LSWM1FC4P,
       "h3cevtModuleSw-LSW1XGT4P0": h3cevtModuleSw_LSW1XGT4P0,
       "h3cevtModuleSw-LSW1XGT2P0": h3cevtModuleSw_LSW1XGT2P0,
       "h3cevtModuleSw-LSP1XGT2P": h3cevtModuleSw_LSP1XGT2P,
       "h3cevtModuleSw-WX5002MPU": h3cevtModuleSw_WX5002MPU,
       "h3cevtModuleSw-LS8M1WCMA": h3cevtModuleSw_LS8M1WCMA,
       "h3cevtModuleSw-EWPX1G24XA0": h3cevtModuleSw_EWPX1G24XA0,
       "h3cevtModuleSw-LSQ1WCMB0": h3cevtModuleSw_LSQ1WCMB0,
       "h3cevtModuleSw-LSB1WCM2A0": h3cevtModuleSw_LSB1WCM2A0,
       "h3cevtModuleSw-EWPX1WCMB0": h3cevtModuleSw_EWPX1WCMB0,
       "h3cevtModuleSw-EWPX1G24XC0": h3cevtModuleSw_EWPX1G24XC0,
       "h3cevtModuleSw-EWPX1WCMC0": h3cevtModuleSw_EWPX1WCMC0,
       "h3cevtModuleSw-EWPX1FWA0": h3cevtModuleSw_EWPX1FWA0,
       "h3cevtModuleSw-EWPX1G10XC0": h3cevtModuleSw_EWPX1G10XC0,
       "h3cevtModuleSw-EWPX1WCM10C0": h3cevtModuleSw_EWPX1WCM10C0,
       "h3cevtModuleSw-LSR1WCM2A1": h3cevtModuleSw_LSR1WCM2A1,
       "h3cevtModuleSw-EWPX1WAP0": h3cevtModuleSw_EWPX1WAP0,
       "h3cevtModuleSw-EWPX1WCMD0": h3cevtModuleSw_EWPX1WCMD0,
       "h3cevtModuleSw-EWPX1G24XCE0": h3cevtModuleSw_EWPX1G24XCE0,
       "h3cevtModuleSw-EWPX1WCMCE0": h3cevtModuleSw_EWPX1WCMCE0,
       "h3cevtModuleSw-LSR1DRSP2L1": h3cevtModuleSw_LSR1DRSP2L1,
       "h3cevtModuleSw-PIC-CLF2G8L": h3cevtModuleSw_PIC_CLF2G8L,
       "h3cevtModuleSw-PIC-CLF4G8L": h3cevtModuleSw_PIC_CLF4G8L,
       "h3cevtModuleSw-SR02SRP2F3": h3cevtModuleSw_SR02SRP2F3,
       "h3cevtModuleSw-SR02SRP1F3": h3cevtModuleSw_SR02SRP1F3,
       "h3cevtModuleSw-LST1GT48LEA1": h3cevtModuleSw_LST1GT48LEA1,
       "h3cevtModuleSw-LST1GP48LEA1": h3cevtModuleSw_LST1GP48LEA1,
       "h3cevtModuleSw-LST2XP8LEA1": h3cevtModuleSw_LST2XP8LEA1,
       "h3cevtModuleSw-LST1GT48LEY1": h3cevtModuleSw_LST1GT48LEY1,
       "h3cevtModuleSw-LST1GP48LEY1": h3cevtModuleSw_LST1GP48LEY1,
       "h3cevtModuleSw-LST1XP32REY1": h3cevtModuleSw_LST1XP32REY1,
       "h3cevtModuleSw-LST1XP8LEY1": h3cevtModuleSw_LST1XP8LEY1,
       "h3cevtModuleSw-LST1GP48LEZ1": h3cevtModuleSw_LST1GP48LEZ1,
       "h3cevtModuleSw-LST1XP8LEZ1": h3cevtModuleSw_LST1XP8LEZ1,
       "h3cevtModuleSw-IM-FW-II": h3cevtModuleSw_IM_FW_II,
       "h3cevtModuleSw-IM-IPS": h3cevtModuleSw_IM_IPS,
       "h3cevtModuleSw-IM-SSL": h3cevtModuleSw_IM_SSL,
       "h3cevtModuleSw-IM-LB": h3cevtModuleSw_IM_LB,
       "h3cevtModuleSw-IM-ACG": h3cevtModuleSw_IM_ACG,
       "h3cevtModuleSw-LSR1XP16REC1": h3cevtModuleSw_LSR1XP16REC1,
       "h3cevtModuleSw-LST2XP8LEB1": h3cevtModuleSw_LST2XP8LEB1,
       "h3cevtModuleSw-LST2XP8LEC1": h3cevtModuleSw_LST2XP8LEC1,
       "h3cevtModuleSw-LST2XP8LEF1": h3cevtModuleSw_LST2XP8LEF1,
       "h3cevtModuleSw-LSR2XP4LEB1": h3cevtModuleSw_LSR2XP4LEB1,
       "h3cevtModuleSw-LSR2XP4LEC1": h3cevtModuleSw_LSR2XP4LEC1,
       "h3cevtModuleSw-LST2XP32REB1": h3cevtModuleSw_LST2XP32REB1,
       "h3cevtModuleSw-LST2XP32REC1": h3cevtModuleSw_LST2XP32REC1,
       "h3cevtModuleSw-LSR1WCM3A1": h3cevtModuleSw_LSR1WCM3A1,
       "h3cevtModuleSw-LST1XP16LEB1": h3cevtModuleSw_LST1XP16LEB1,
       "h3cevtModuleSw-LST1XP16LEC1": h3cevtModuleSw_LST1XP16LEC1,
       "h3cevtModuleSw-CR-SPC-XP4L-E-I": h3cevtModuleSw_CR_SPC_XP4L_E_I,
       "h3cevtModuleSw-LST2MRPNC1": h3cevtModuleSw_LST2MRPNC1,
       "h3cevtModuleSw-LST2SF08C1": h3cevtModuleSw_LST2SF08C1,
       "h3cevtModuleSw-LST2SF18C1": h3cevtModuleSw_LST2SF18C1,
       "h3cevtModuleSw-SR02SRP2G3": h3cevtModuleSw_SR02SRP2G3,
       "h3cevtModuleSw-CR-SPE-3020-E-I": h3cevtModuleSw_CR_SPE_3020_E_I,
       "h3cevtModuleSw-CR-SPC-PUP4L-E-I": h3cevtModuleSw_CR_SPC_PUP4L_E_I,
       "h3cevtModuleSw-CR-SPC-XP4LEF-I": h3cevtModuleSw_CR_SPC_XP4LEF_I,
       "h3cevtModuleSw-CR-SPC-XP8LEF-I": h3cevtModuleSw_CR_SPC_XP8LEF_I,
       "h3cevtModuleSw-LST3XP8LEB1": h3cevtModuleSw_LST3XP8LEB1,
       "h3cevtModuleSw-LST3XP8LEC1": h3cevtModuleSw_LST3XP8LEC1,
       "h3cevtModuleSw-LST1FW3A1": h3cevtModuleSw_LST1FW3A1,
       "h3cevtModuleSw-CR-IM-NAM1A": h3cevtModuleSw_CR_IM_NAM1A,
       "h3cevtModuleSw-LSR2SRP2B1": h3cevtModuleSw_LSR2SRP2B1,
       "h3cevtModuleSw-LSR2SRP2B2": h3cevtModuleSw_LSR2SRP2B2,
       "h3cevtModuleSw-LSR2SRP2D1": h3cevtModuleSw_LSR2SRP2D1,
       "h3cevtModuleSw-LST3XP8LEY1": h3cevtModuleSw_LST3XP8LEY1,
       "h3cevtModuleSw-LST2XP32REY1": h3cevtModuleSw_LST2XP32REY1,
       "h3cevtModuleSw-LST1XP16LEY1": h3cevtModuleSw_LST1XP16LEY1,
       "h3cevtModuleSw-SR0M2SRP2G3": h3cevtModuleSw_SR0M2SRP2G3,
       "h3cevtModuleSw-SR0M2SRP1G3": h3cevtModuleSw_SR0M2SRP1G3,
       "h3cevtModuleSw-SPC-GP48LA": h3cevtModuleSw_SPC_GP48LA,
       "h3cevtModuleSw-SPC-GT48LA": h3cevtModuleSw_SPC_GT48LA,
       "h3cevtModuleSw-SPC-XP4LA": h3cevtModuleSw_SPC_XP4LA,
       "h3cevtModuleSw-SPC-XP2LA": h3cevtModuleSw_SPC_XP2LA,
       "h3cevtModuleSw-SPC-GP24LA": h3cevtModuleSw_SPC_GP24LA,
       "h3cevtModuleSw-SPC-XP16RA": h3cevtModuleSw_SPC_XP16RA,
       "h3cevtModuleSw-CR-IM-FW1A": h3cevtModuleSw_CR_IM_FW1A,
       "h3cevtModuleSw-LSU1QGC4SF0": h3cevtModuleSw_LSU1QGC4SF0,
       "h3cevtModuleSw-LSU1QGS8SF0": h3cevtModuleSw_LSU1QGS8SF0,
       "h3cevtModuleSw-LSU1TGS48SF0": h3cevtModuleSw_LSU1TGS48SF0,
       "h3cevtModuleSw-LSU1QGS4SF0": h3cevtModuleSw_LSU1QGS4SF0,
       "h3cevtModuleSw-LSU1TGS32SF0": h3cevtModuleSw_LSU1TGS32SF0,
       "h3cevtModuleSw-LSU1FAB08D0": h3cevtModuleSw_LSU1FAB08D0,
       "h3cevtModuleSw-LSU1FAB04B0": h3cevtModuleSw_LSU1FAB04B0,
       "h3cevtModuleSw-LSU1FAB08B0": h3cevtModuleSw_LSU1FAB08B0,
       "h3cevtModuleSw-LSU1FAB12D0": h3cevtModuleSw_LSU1FAB12D0,
       "h3cevtModuleSw-LSU1FAB12B0": h3cevtModuleSw_LSU1FAB12B0,
       "h3cevtModuleSw-LSU1FAB04D0": h3cevtModuleSw_LSU1FAB04D0,
       "h3cevtModuleSw-LSQ1CTGS16SC0": h3cevtModuleSw_LSQ1CTGS16SC0,
       "h3cevtModuleSw-EWPX2CTGS16SC0": h3cevtModuleSw_EWPX2CTGS16SC0,
       "h3cevtModuleSw-LSUM3WCMD0": h3cevtModuleSw_LSUM3WCMD0,
       "h3cevtModuleSw-EWPXM3WCMD0": h3cevtModuleSw_EWPXM3WCMD0,
       "h3cevtModuleSw-LSQ1QGS4SC0": h3cevtModuleSw_LSQ1QGS4SC0,
       "h3cevtModuleSw-LSQ1QGC4SC0": h3cevtModuleSw_LSQ1QGC4SC0,
       "h3cevtModuleSw-LSU1TGT24SF0": h3cevtModuleSw_LSU1TGT24SF0,
       "h3cevtModuleSw-LSQ1QGS8SC3": h3cevtModuleSw_LSQ1QGS8SC3,
       "h3cevtModuleSw-LSQ1TGS32SC3": h3cevtModuleSw_LSQ1TGS32SC3,
       "h3cevtModuleSw-LSQ1QGS4SC3": h3cevtModuleSw_LSQ1QGS4SC3,
       "h3cevtModuleSw-LSQ1TGS48SC3": h3cevtModuleSw_LSQ1TGS48SC3,
       "h3cevtModuleSw-LSQ1QGC4SC3": h3cevtModuleSw_LSQ1QGC4SC3,
       "h3cevtModuleSw-LSQ1FAB12D3": h3cevtModuleSw_LSQ1FAB12D3,
       "h3cevtModuleSw-LSQ1FAB08D3": h3cevtModuleSw_LSQ1FAB08D3,
       "h3cevtModuleSw-LSQ1FAB04D3": h3cevtModuleSw_LSQ1FAB04D3,
       "h3cevtModuleSw-LSQ1TGS8EB3": h3cevtModuleSw_LSQ1TGS8EB3,
       "h3cevtModuleSw-LSQ1TGT24SC3": h3cevtModuleSw_LSQ1TGT24SC3,
       "h3cevtModuleSw-LSQ1FAB08B0": h3cevtModuleSw_LSQ1FAB08B0,
       "h3cevtModuleSw-EWPX2CTGS16SC": h3cevtModuleSw_EWPX2CTGS16SC,
       "h3cevtSubModuleRouter": h3cevtSubModuleRouter,
       "h3cevtSubModuleSwitch": h3cevtSubModuleSwitch,
       "h3cevtPort": h3cevtPort,
       "h3cevtPortUnknownPorts": h3cevtPortUnknownPorts,
       "h3cevtPortCommonPorts": h3cevtPortCommonPorts,
       "h3cevtPortRouterType": h3cevtPortRouterType,
       "h3cevtPortRt-Async": h3cevtPortRt_Async,
       "h3cevtPortRt-Analogmodem": h3cevtPortRt_Analogmodem,
       "h3cevtPortRt-Atm": h3cevtPortRt_Atm,
       "h3cevtPortRt-AtmAdsl": h3cevtPortRt_AtmAdsl,
       "h3cevtPortRt-AtmShdsl": h3cevtPortRt_AtmShdsl,
       "h3cevtPortRt-AtmE1": h3cevtPortRt_AtmE1,
       "h3cevtPortRt-AtmT1": h3cevtPortRt_AtmT1,
       "h3cevtPortRt-AtmE3": h3cevtPortRt_AtmE3,
       "h3cevtPortRt-AtmT3": h3cevtPortRt_AtmT3,
       "h3cevtPortRt-Atm622M": h3cevtPortRt_Atm622M,
       "h3cevtPortRt-AtmImaE1": h3cevtPortRt_AtmImaE1,
       "h3cevtPortRt-AtmImaT1": h3cevtPortRt_AtmImaT1,
       "h3cevtPortRt-Atm25M": h3cevtPortRt_Atm25M,
       "h3cevtPortRt-Bri": h3cevtPortRt_Bri,
       "h3cevtPortRt-Console": h3cevtPortRt_Console,
       "h3cevtPortRt-E1": h3cevtPortRt_E1,
       "h3cevtPortRt-E3": h3cevtPortRt_E3,
       "h3cevtPortRt-T1": h3cevtPortRt_T1,
       "h3cevtPortRt-T3": h3cevtPortRt_T3,
       "h3cevtPortRt-Cpos": h3cevtPortRt_Cpos,
       "h3cevtPortRt-Ethernet": h3cevtPortRt_Ethernet,
       "h3cevtPortRt-Serial": h3cevtPortRt_Serial,
       "h3cevtPortRt-E1f": h3cevtPortRt_E1f,
       "h3cevtPortRt-T1f": h3cevtPortRt_T1f,
       "h3cevtPortRt-Pos": h3cevtPortRt_Pos,
       "h3cevtPortRt-Ge": h3cevtPortRt_Ge,
       "h3cevtPortRt-Aux": h3cevtPortRt_Aux,
       "h3cevtPortRt-VG-Fxs": h3cevtPortRt_VG_Fxs,
       "h3cevtPortRt-VG-Fxo": h3cevtPortRt_VG_Fxo,
       "h3cevtPortRt-VG-E1vi": h3cevtPortRt_VG_E1vi,
       "h3cevtPortRt-VG-T1vi": h3cevtPortRt_VG_T1vi,
       "h3cevtPortRt-Usb": h3cevtPortRt_Usb,
       "h3cevtPortRt-Ndec": h3cevtPortRt_Ndec,
       "h3cevtPortRt-Cavium": h3cevtPortRt_Cavium,
       "h3cevtPortRt-Fcm": h3cevtPortRt_Fcm,
       "h3cevtPortRt-E1vi": h3cevtPortRt_E1vi,
       "h3cevtPortRt-T1vi": h3cevtPortRt_T1vi,
       "h3cevtPortRt-Vi": h3cevtPortRt_Vi,
       "h3cevtPortRt-Adls2Plus": h3cevtPortRt_Adls2Plus,
       "h3cevtPortRt-RADIO-AG": h3cevtPortRt_RADIO_AG,
       "h3cevtPortRt-1exp": h3cevtPortRt_1exp,
       "h3cevtPortRt-G-SHDSL-BIS": h3cevtPortRt_G_SHDSL_BIS,
       "h3cevtPortRt-ONU-1000BASE-BX-SFF-SC": h3cevtPortRt_ONU_1000BASE_BX_SFF_SC,
       "h3cevtPortRt-CELLULAR": h3cevtPortRt_CELLULAR,
       "h3cevtPortSwitchType": h3cevtPortSwitchType,
       "h3cevtPortSw-10or100M": h3cevtPortSw_10or100M,
       "h3cevtPortSw-1000BaseLxSm": h3cevtPortSw_1000BaseLxSm,
       "h3cevtPortSw-1000BaseSxMm": h3cevtPortSw_1000BaseSxMm,
       "h3cevtPortSw-1000BaseTx": h3cevtPortSw_1000BaseTx,
       "h3cevtPortSw-100MSinglemodeFx": h3cevtPortSw_100MSinglemodeFx,
       "h3cevtPortSw-100MMultimodeFx": h3cevtPortSw_100MMultimodeFx,
       "h3cevtPortSw-100M100BaseTx": h3cevtPortSw_100M100BaseTx,
       "h3cevtPortSw-100MHub": h3cevtPortSw_100MHub,
       "h3cevtPortSw-Vdsl": h3cevtPortSw_Vdsl,
       "h3cevtPortSw-Stack": h3cevtPortSw_Stack,
       "h3cevtPortSw-1000BaseZenithFx": h3cevtPortSw_1000BaseZenithFx,
       "h3cevtPortSw-1000BaseLongFx": h3cevtPortSw_1000BaseLongFx,
       "h3cevtPortSw-Adsl": h3cevtPortSw_Adsl,
       "h3cevtPortSw-10or100MDb": h3cevtPortSw_10or100MDb,
       "h3cevtPortSw-10GBaseLrSm": h3cevtPortSw_10GBaseLrSm,
       "h3cevtPortSw-10GBaseLx4Mm": h3cevtPortSw_10GBaseLx4Mm,
       "h3cevtPortSw-10GBaseLx4Sm": h3cevtPortSw_10GBaseLx4Sm,
       "h3cevtPortSw-100MLongFx": h3cevtPortSw_100MLongFx,
       "h3cevtPortSw-1000BaseCx": h3cevtPortSw_1000BaseCx,
       "h3cevtPortSw-1000BaseZenithFxLc": h3cevtPortSw_1000BaseZenithFxLc,
       "h3cevtPortSw-1000BaseLongFxLc": h3cevtPortSw_1000BaseLongFxLc,
       "h3cevtPortSw-100MSmFxSc": h3cevtPortSw_100MSmFxSc,
       "h3cevtPortSw-100MMmFxSc": h3cevtPortSw_100MMmFxSc,
       "h3cevtPortSw-100MSmFxLc": h3cevtPortSw_100MSmFxLc,
       "h3cevtPortSw-100MMmFxLc": h3cevtPortSw_100MMmFxLc,
       "h3cevtPortSw-GbicNoConnector": h3cevtPortSw_GbicNoConnector,
       "h3cevtPortSw-Gbic1000BaseT": h3cevtPortSw_Gbic1000BaseT,
       "h3cevtPortSw-Gbic1000BaseLx": h3cevtPortSw_Gbic1000BaseLx,
       "h3cevtPortSw-Gbic1000BaseSx": h3cevtPortSw_Gbic1000BaseSx,
       "h3cevtPortSw-Gbic1000BaseZx": h3cevtPortSw_Gbic1000BaseZx,
       "h3cevtPortSw-ComboNoConnector": h3cevtPortSw_ComboNoConnector,
       "h3cevtPortSw-Combo1000BaseLx": h3cevtPortSw_Combo1000BaseLx,
       "h3cevtPortSw-Combo1000BaseLxFiber": h3cevtPortSw_Combo1000BaseLxFiber,
       "h3cevtPortSw-Combo1000BaseLxCopper": h3cevtPortSw_Combo1000BaseLxCopper,
       "h3cevtPortSw-Combo1000BaseSx": h3cevtPortSw_Combo1000BaseSx,
       "h3cevtPortSw-Combo1000BaseSxFiber": h3cevtPortSw_Combo1000BaseSxFiber,
       "h3cevtPortSw-Combo1000BaseSxCopper": h3cevtPortSw_Combo1000BaseSxCopper,
       "h3cevtPortSw-Combo1000BaseZx": h3cevtPortSw_Combo1000BaseZx,
       "h3cevtPortSw-Combo1000BaseZxFiber": h3cevtPortSw_Combo1000BaseZxFiber,
       "h3cevtPortSw-Combo1000BaseZxCopper": h3cevtPortSw_Combo1000BaseZxCopper,
       "h3cevtPortSw-155PosSxMmf": h3cevtPortSw_155PosSxMmf,
       "h3cevtPortSw-155PosLxSmf": h3cevtPortSw_155PosLxSmf,
       "h3cevtPortSw-1000BASE-T": h3cevtPortSw_1000BASE_T,
       "h3cevtPortSw-1000BASE-SX-SFP": h3cevtPortSw_1000BASE_SX_SFP,
       "h3cevtPortSw-1000BASE-LX-SFP": h3cevtPortSw_1000BASE_LX_SFP,
       "h3cevtPortSw-1000BASE-T-AN-SFP": h3cevtPortSw_1000BASE_T_AN_SFP,
       "h3cevtPortSw-10GBASE-LX4-XENPAK": h3cevtPortSw_10GBASE_LX4_XENPAK,
       "h3cevtPortSw-10GBASE-LR-XENPAK": h3cevtPortSw_10GBASE_LR_XENPAK,
       "h3cevtPortSw-10GBASE-CX4": h3cevtPortSw_10GBASE_CX4,
       "h3cevtPortSw-1000BASE-ZX-SFP": h3cevtPortSw_1000BASE_ZX_SFP,
       "h3cevtPortSw-1000BASE-MM-SFP": h3cevtPortSw_1000BASE_MM_SFP,
       "h3cevtPortSw-100BASE-SX-SFP": h3cevtPortSw_100BASE_SX_SFP,
       "h3cevtPortSw-100BASE-LX-SFP": h3cevtPortSw_100BASE_LX_SFP,
       "h3cevtPortSw-100BASE-T-AN-SFP": h3cevtPortSw_100BASE_T_AN_SFP,
       "h3cevtPortSw-100BASE-ZX-SFP": h3cevtPortSw_100BASE_ZX_SFP,
       "h3cevtPortSw-100BASE-MM-SFP": h3cevtPortSw_100BASE_MM_SFP,
       "h3cevtPortSw-SFP-NO-CONNECTOR": h3cevtPortSw_SFP_NO_CONNECTOR,
       "h3cevtPortSw-SFP-UNKNOWN-CONNECTOR": h3cevtPortSw_SFP_UNKNOWN_CONNECTOR,
       "h3cevtPortSw-POS-NO-CONNECTOR": h3cevtPortSw_POS_NO_CONNECTOR,
       "h3cevtPortSw-10G-BASE-SR": h3cevtPortSw_10G_BASE_SR,
       "h3cevtPortSw-10G-BASE-ER": h3cevtPortSw_10G_BASE_ER,
       "h3cevtPortSw-10G-BASE-LX4": h3cevtPortSw_10G_BASE_LX4,
       "h3cevtPortSw-10G-BASE-SW": h3cevtPortSw_10G_BASE_SW,
       "h3cevtPortSw-10G-BASE-LW": h3cevtPortSw_10G_BASE_LW,
       "h3cevtPortSw-10G-BASE-EW": h3cevtPortSw_10G_BASE_EW,
       "h3cevtPortSw-10G-LR-SM-LC": h3cevtPortSw_10G_LR_SM_LC,
       "h3cevtPortSw-10G-SR-MM-LC": h3cevtPortSw_10G_SR_MM_LC,
       "h3cevtPortSw-10G-ER-SM-LC": h3cevtPortSw_10G_ER_SM_LC,
       "h3cevtPortSw-10G-LW-SM-LC": h3cevtPortSw_10G_LW_SM_LC,
       "h3cevtPortSw-10G-SW-MM-LC": h3cevtPortSw_10G_SW_MM_LC,
       "h3cevtPortSw-10G-EW-SM-LC": h3cevtPortSw_10G_EW_SM_LC,
       "h3cevtPortSw-100BASE-SM-MTRJ": h3cevtPortSw_100BASE_SM_MTRJ,
       "h3cevtPortSw-100BASE-MM-MTRJ": h3cevtPortSw_100BASE_MM_MTRJ,
       "h3cevtPortSw-XFP-NO-CONNECTOR": h3cevtPortSw_XFP_NO_CONNECTOR,
       "h3cevtPortSw-XFP-10GBASE-SR": h3cevtPortSw_XFP_10GBASE_SR,
       "h3cevtPortSw-XFP-10GBASE-LR": h3cevtPortSw_XFP_10GBASE_LR,
       "h3cevtPortSw-XFP-10GBASE-ER": h3cevtPortSw_XFP_10GBASE_ER,
       "h3cevtPortSw-XFP-10GBASE-SW": h3cevtPortSw_XFP_10GBASE_SW,
       "h3cevtPortSw-XFP-10GBASE-LW": h3cevtPortSw_XFP_10GBASE_LW,
       "h3cevtPortSw-XFP-10GBASE-EW": h3cevtPortSw_XFP_10GBASE_EW,
       "h3cevtPortSw-XFP-10GBASE-CX4": h3cevtPortSw_XFP_10GBASE_CX4,
       "h3cevtPortSw-XFP-10GBASE-LX4": h3cevtPortSw_XFP_10GBASE_LX4,
       "h3cevtPortSw-XFP-UNKNOWN": h3cevtPortSw_XFP_UNKNOWN,
       "h3cevtPortSw-XPK-NOCONNECTOR": h3cevtPortSw_XPK_NOCONNECTOR,
       "h3cevtPortSw-XPK-10GBASE-SR": h3cevtPortSw_XPK_10GBASE_SR,
       "h3cevtPortSw-XPK-10GBASE-LR": h3cevtPortSw_XPK_10GBASE_LR,
       "h3cevtPortSw-XPK-10GBASE-ER": h3cevtPortSw_XPK_10GBASE_ER,
       "h3cevtPortSw-XPK-10GBASE-SW": h3cevtPortSw_XPK_10GBASE_SW,
       "h3cevtPortSw-XPK-10GBASE-LW": h3cevtPortSw_XPK_10GBASE_LW,
       "h3cevtPortSw-XPK-10GBASE-EW": h3cevtPortSw_XPK_10GBASE_EW,
       "h3cevtPortSw-XPK-10GBASE-CX4": h3cevtPortSw_XPK_10GBASE_CX4,
       "h3cevtPortSw-XPK-10GBASE-LX4": h3cevtPortSw_XPK_10GBASE_LX4,
       "h3cevtPortSw-XPK-UNKNOWN": h3cevtPortSw_XPK_UNKNOWN,
       "h3cevtPortSw-POS-OC48-SR-SM-LC": h3cevtPortSw_POS_OC48_SR_SM_LC,
       "h3cevtPortSw-POS-OC48-IR-SM-LC": h3cevtPortSw_POS_OC48_IR_SM_LC,
       "h3cevtPortSw-POS-OC48-LR-SM-LC": h3cevtPortSw_POS_OC48_LR_SM_LC,
       "h3cevtPortSw-10G-BASE-CX4": h3cevtPortSw_10G_BASE_CX4,
       "h3cevtPortSw-OLT-1000BASE-BX-SFF-SC": h3cevtPortSw_OLT_1000BASE_BX_SFF_SC,
       "h3cevtPortSw-ONU-1000BASE-BX-SFF-SC": h3cevtPortSw_ONU_1000BASE_BX_SFF_SC,
       "h3cevtPortSw-24G-CASCADE": h3cevtPortSw_24G_CASCADE,
       "h3cevtPortSw-POS-OC3-SR-MM": h3cevtPortSw_POS_OC3_SR_MM,
       "h3cevtPortSw-POS-OC3-IR-SM": h3cevtPortSw_POS_OC3_IR_SM,
       "h3cevtPortSw-POS-OC3-IR-1-SM": h3cevtPortSw_POS_OC3_IR_1_SM,
       "h3cevtPortSw-POS-OC3-IR-2-SM": h3cevtPortSw_POS_OC3_IR_2_SM,
       "h3cevtPortSw-POS-OC3-LR-SM": h3cevtPortSw_POS_OC3_LR_SM,
       "h3cevtPortSw-POS-OC3-LR-1-SM": h3cevtPortSw_POS_OC3_LR_1_SM,
       "h3cevtPortSw-POS-OC3-LR-2-SM": h3cevtPortSw_POS_OC3_LR_2_SM,
       "h3cevtPortSw-POS-OC3-LR-3-SM": h3cevtPortSw_POS_OC3_LR_3_SM,
       "h3cevtPortSw-POS-OC12-SR-MM": h3cevtPortSw_POS_OC12_SR_MM,
       "h3cevtPortSw-POS-OC12-IR-SM": h3cevtPortSw_POS_OC12_IR_SM,
       "h3cevtPortSw-POS-OC12-IR-1-SM": h3cevtPortSw_POS_OC12_IR_1_SM,
       "h3cevtPortSw-POS-OC12-IR-2-SM": h3cevtPortSw_POS_OC12_IR_2_SM,
       "h3cevtPortSw-POS-OC12-LR-SM": h3cevtPortSw_POS_OC12_LR_SM,
       "h3cevtPortSw-POS-OC12-LR-1-SM": h3cevtPortSw_POS_OC12_LR_1_SM,
       "h3cevtPortSw-POS-OC12-LR-2-SM": h3cevtPortSw_POS_OC12_LR_2_SM,
       "h3cevtPortSw-POS-OC12-LR-3-SM": h3cevtPortSw_POS_OC12_LR_3_SM,
       "h3cevtPortSw-POS-OC48-SR-SM": h3cevtPortSw_POS_OC48_SR_SM,
       "h3cevtPortSw-POS-OC48-IR-SM": h3cevtPortSw_POS_OC48_IR_SM,
       "h3cevtPortSw-POS-OC48-IR-1-SM": h3cevtPortSw_POS_OC48_IR_1_SM,
       "h3cevtPortSw-POS-OC48-IR-2-SM": h3cevtPortSw_POS_OC48_IR_2_SM,
       "h3cevtPortSw-POS-OC48-LR-SM": h3cevtPortSw_POS_OC48_LR_SM,
       "h3cevtPortSw-POS-OC48-LR-1-SM": h3cevtPortSw_POS_OC48_LR_1_SM,
       "h3cevtPortSw-POS-OC48-LR-2-SM": h3cevtPortSw_POS_OC48_LR_2_SM,
       "h3cevtPortSw-POS-OC48-LR-3-SM": h3cevtPortSw_POS_OC48_LR_3_SM,
       "h3cevtPortSw-POS-I-64-1": h3cevtPortSw_POS_I_64_1,
       "h3cevtPortSw-POS-I-64-2": h3cevtPortSw_POS_I_64_2,
       "h3cevtPortSw-POS-I-64-3": h3cevtPortSw_POS_I_64_3,
       "h3cevtPortSw-POS-I-64-5": h3cevtPortSw_POS_I_64_5,
       "h3cevtPortSw-POS-S-64-1": h3cevtPortSw_POS_S_64_1,
       "h3cevtPortSw-POS-S-64-2": h3cevtPortSw_POS_S_64_2,
       "h3cevtPortSw-POS-S-64-3": h3cevtPortSw_POS_S_64_3,
       "h3cevtPortSw-POS-S-64-5": h3cevtPortSw_POS_S_64_5,
       "h3cevtPortSw-POS-L-64-1": h3cevtPortSw_POS_L_64_1,
       "h3cevtPortSw-POS-L-64-2": h3cevtPortSw_POS_L_64_2,
       "h3cevtPortSw-POS-L-64-3": h3cevtPortSw_POS_L_64_3,
       "h3cevtPortSw-POS-V-64-2": h3cevtPortSw_POS_V_64_2,
       "h3cevtPortSw-POS-V-64-3": h3cevtPortSw_POS_V_64_3,
       "h3cevtPortSw-100BASE-FX-BIDI": h3cevtPortSw_100BASE_FX_BIDI,
       "h3cevtPortSw-100BASE-BX10-U-SFP": h3cevtPortSw_100BASE_BX10_U_SFP,
       "h3cevtPortSw-100BASE-BX10-D-SFP": h3cevtPortSw_100BASE_BX10_D_SFP,
       "h3cevtPortSw-1000BASE-BX10-U-SFP": h3cevtPortSw_1000BASE_BX10_U_SFP,
       "h3cevtPortSw-1000BASE-BX10-D-SFP": h3cevtPortSw_1000BASE_BX10_D_SFP,
       "h3cevtPortSw-STK-1000BASE-T": h3cevtPortSw_STK_1000BASE_T,
       "h3cevtPortSw-RPR-PHYPOS-CONNECTOR": h3cevtPortSw_RPR_PHYPOS_CONNECTOR,
       "h3cevtPortSw-RPR-PHY10GE-CONNECTOR": h3cevtPortSw_RPR_PHY10GE_CONNECTOR,
       "h3cevtPortSw-RPR-LOGICPOS-CONNECTOR": h3cevtPortSw_RPR_LOGICPOS_CONNECTOR,
       "h3cevtPortSw-RPR-LOGIC10GE-CONNECTOR": h3cevtPortSw_RPR_LOGIC10GE_CONNECTOR,
       "h3cevtPortSw-10GBASE-ZR": h3cevtPortSw_10GBASE_ZR,
       "h3cevtPortSw-TYPE-ERROR-CONNECTOR": h3cevtPortSw_TYPE_ERROR_CONNECTOR,
       "h3cevtPortSw-10G-STACK": h3cevtPortSw_10G_STACK,
       "h3cevtPortSw-155-ATM-SX-MMF": h3cevtPortSw_155_ATM_SX_MMF,
       "h3cevtPortSw-155-ATM-LX-SMF": h3cevtPortSw_155_ATM_LX_SMF,
       "h3cevtPortSw-622-ATM-SX-MMF": h3cevtPortSw_622_ATM_SX_MMF,
       "h3cevtPortSw-622-ATM-LX-SMF": h3cevtPortSw_622_ATM_LX_SMF,
       "h3cevtPortSw-155-ATM-NO-CONNECTOR": h3cevtPortSw_155_ATM_NO_CONNECTOR,
       "h3cevtPortSw-622-ATM-NO-CONNECTOR": h3cevtPortSw_622_ATM_NO_CONNECTOR,
       "h3cevtPortSw-155-CPOS-E1-NO-CONNECTOR": h3cevtPortSw_155_CPOS_E1_NO_CONNECTOR,
       "h3cevtPortSw-155-CPOS-T1-NO-CONNECTOR": h3cevtPortSw_155_CPOS_T1_NO_CONNECTOR,
       "h3cevtPortSw-622-CPOS-E1-NO-CONNECTOR": h3cevtPortSw_622_CPOS_E1_NO_CONNECTOR,
       "h3cevtPortSw-622-CPOS-T1-NO-CONNECTOR": h3cevtPortSw_622_CPOS_T1_NO_CONNECTOR,
       "h3cevtPortSw-155-CPOS-E1-SX-MMF": h3cevtPortSw_155_CPOS_E1_SX_MMF,
       "h3cevtPortSw-155-CPOS-T1-SX-MMF": h3cevtPortSw_155_CPOS_T1_SX_MMF,
       "h3cevtPortSw-155-CPOS-E1-LX-SMF": h3cevtPortSw_155_CPOS_E1_LX_SMF,
       "h3cevtPortSw-155-CPOS-T1-LX-SMF": h3cevtPortSw_155_CPOS_T1_LX_SMF,
       "h3cevtPortSw-622-CPOS-E1-SX-MMF": h3cevtPortSw_622_CPOS_E1_SX_MMF,
       "h3cevtPortSw-622-CPOS-T1-SX-MMF": h3cevtPortSw_622_CPOS_T1_SX_MMF,
       "h3cevtPortSw-622-CPOS-E1-LX-SMF": h3cevtPortSw_622_CPOS_E1_LX_SMF,
       "h3cevtPortSw-622-CPOS-T1-LX-SMF": h3cevtPortSw_622_CPOS_T1_LX_SMF,
       "h3cevtPortSw-E1-CONNECTOR": h3cevtPortSw_E1_CONNECTOR,
       "h3cevtPortSw-T1-CONNECTOR": h3cevtPortSw_T1_CONNECTOR,
       "h3cevtPortSw-1000BASE-STK-SFP": h3cevtPortSw_1000BASE_STK_SFP,
       "h3cevtPortSw-1000BASE-BIDI-SFP": h3cevtPortSw_1000BASE_BIDI_SFP,
       "h3cevtPortSw-1000BASE-CWDM-SFP": h3cevtPortSw_1000BASE_CWDM_SFP,
       "h3cevtPortSw-100BASE-BIDI-SFP": h3cevtPortSw_100BASE_BIDI_SFP,
       "h3cevtPortSw-OLT-1000BASE-PX-SFP": h3cevtPortSw_OLT_1000BASE_PX_SFP,
       "h3cevtPortSw-OLT-1000BASE-NO-CONNECTOR": h3cevtPortSw_OLT_1000BASE_NO_CONNECTOR,
       "h3cevtPortSw-RPR-PHYGE-CONNECTOR": h3cevtPortSw_RPR_PHYGE_CONNECTOR,
       "h3cevtPortSw-RPR-LOGICGE-CONNECTOR": h3cevtPortSw_RPR_LOGICGE_CONNECTOR,
       "h3cevtPortSw-100M-1550-BIDI": h3cevtPortSw_100M_1550_BIDI,
       "h3cevtPortSw-100M-1310-BIDI": h3cevtPortSw_100M_1310_BIDI,
       "h3cevtPortSw-RPR-PHYOC48-CONNECTOR": h3cevtPortSw_RPR_PHYOC48_CONNECTOR,
       "h3cevtPortSw-RPR-LOGICOC48-CONNECTOR": h3cevtPortSw_RPR_LOGICOC48_CONNECTOR,
       "h3cevtPortSw-100-1000-BASE-LX-SMF": h3cevtPortSw_100_1000_BASE_LX_SMF,
       "h3cevtPortSw-10G-ZW-SM-LC": h3cevtPortSw_10G_ZW_SM_LC,
       "h3cevtPortSw-10G-ZR-SM-LC": h3cevtPortSw_10G_ZR_SM_LC,
       "h3cevtPortSw-XPK-10GBASE-ZR": h3cevtPortSw_XPK_10GBASE_ZR,
       "h3cevtPortSw-SGMII-100-BASE-LX-SFP": h3cevtPortSw_SGMII_100_BASE_LX_SFP,
       "h3cevtPortSw-SGMII-100-BASE-FX-SFP": h3cevtPortSw_SGMII_100_BASE_FX_SFP,
       "h3cevtPortSw-WLAN-RADIO": h3cevtPortSw_WLAN_RADIO,
       "h3cevtPortSw-CABLE": h3cevtPortSw_CABLE,
       "h3cevtPortSw-SFP-PLUS-NO-CONNECTOR": h3cevtPortSw_SFP_PLUS_NO_CONNECTOR,
       "h3cevtPortSw-SFP-PLUS-10GBASE-SR": h3cevtPortSw_SFP_PLUS_10GBASE_SR,
       "h3cevtPortSw-SFP-PLUS-10GBASE-LR": h3cevtPortSw_SFP_PLUS_10GBASE_LR,
       "h3cevtPortSw-SFP-PLUS-10GBASE-LRM": h3cevtPortSw_SFP_PLUS_10GBASE_LRM,
       "h3cevtPortSw-SFP-PLUS-10GBASE-Cu": h3cevtPortSw_SFP_PLUS_10GBASE_Cu,
       "h3cevtPortSw-SFP-PLUS-UNKNOWN": h3cevtPortSw_SFP_PLUS_UNKNOWN,
       "h3cevtPortSw-SFP-PLUS-STACK-CONNECTOR": h3cevtPortSw_SFP_PLUS_STACK_CONNECTOR,
       "h3cevtPortSw-POS-L-64-4": h3cevtPortSw_POS_L_64_4,
       "h3cevtPortSw-MINISAS-HD-STACK-CONNECTOR": h3cevtPortSw_MINISAS_HD_STACK_CONNECTOR,
       "h3cevtPortSw-ONU-1000BASE-PX-SFF": h3cevtPortSw_ONU_1000BASE_PX_SFF,
       "h3cevtPortSw-RS485": h3cevtPortSw_RS485,
       "h3cevtPortSw-SFP-PLUS-10GBASE-ER": h3cevtPortSw_SFP_PLUS_10GBASE_ER,
       "h3cevtPortSw-SFP-PLUS-10GBASE-ZR": h3cevtPortSw_SFP_PLUS_10GBASE_ZR,
       "h3cevtPortSw-XFP-10GBASE-ZR": h3cevtPortSw_XFP_10GBASE_ZR,
       "h3cevtPortSw-QSFP-PLUS-40GBASE-SR4": h3cevtPortSw_QSFP_PLUS_40GBASE_SR4,
       "h3cevtPortSw-QSFP-PLUS-STACK-CONNECTOR": h3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR,
       "h3cevtPortSw-QSFP-PLUS-TO-4SFP-PLUS-STACK-CONNECTOR": h3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR,
       "h3cevtPortSw-SFP-STACK-CONNECTOR": h3cevtPortSw_SFP_STACK_CONNECTOR,
       "h3cevtPortSw-QSFP-NO-CONNECTOR": h3cevtPortSw_QSFP_NO_CONNECTOR,
       "h3cevtPortSw-10GBase-T": h3cevtPortSw_10GBase_T,
       "h3cevtPortSw-CFP-NO-CONNECTOR": h3cevtPortSw_CFP_NO_CONNECTOR,
       "h3cevtPortSw-CFP-40GBASE-LR4": h3cevtPortSw_CFP_40GBASE_LR4,
       "h3cevtStack": h3cevtStack}
)
