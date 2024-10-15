# SNMP MIB module (HPN-ICF-ENTITY-VENDORTYPE-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-ENTITY-VENDORTYPE-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:05 2024
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

(hpnicf,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicf")

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

hpnicfEntityVendorTypeOID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEntityVendortypeObjects_ObjectIdentity = ObjectIdentity
hpnicfEntityVendortypeObjects = _HpnicfEntityVendortypeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1)
)
_HpnicfevtOther_ObjectIdentity = ObjectIdentity
hpnicfevtOther = _HpnicfevtOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1)
)
_HpnicfevtOtherUnknownCard_ObjectIdentity = ObjectIdentity
hpnicfevtOtherUnknownCard = _HpnicfevtOtherUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1, 1)
)
_HpnicfevtCPU_ObjectIdentity = ObjectIdentity
hpnicfevtCPU = _HpnicfevtCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1, 2)
)
_HpnicfevtGeneralCPU_ObjectIdentity = ObjectIdentity
hpnicfevtGeneralCPU = _HpnicfevtGeneralCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1, 2, 1)
)
_HpnicfevtDOM_ObjectIdentity = ObjectIdentity
hpnicfevtDOM = _HpnicfevtDOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1, 3)
)
_HpnicfevtCFCard_ObjectIdentity = ObjectIdentity
hpnicfevtCFCard = _HpnicfevtCFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1, 4)
)
_HpnicfevtHardDisk_ObjectIdentity = ObjectIdentity
hpnicfevtHardDisk = _HpnicfevtHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 1, 5)
)
_HpnicfevtUnknown_ObjectIdentity = ObjectIdentity
hpnicfevtUnknown = _HpnicfevtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 2)
)
_HpnicfevtChassis_ObjectIdentity = ObjectIdentity
hpnicfevtChassis = _HpnicfevtChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 3)
)
_HpnicfevtBackplane_ObjectIdentity = ObjectIdentity
hpnicfevtBackplane = _HpnicfevtBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 4)
)
_HpnicfevtContainer_ObjectIdentity = ObjectIdentity
hpnicfevtContainer = _HpnicfevtContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 5)
)
_HpnicfevtPowerSupply_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupply = _HpnicfevtPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6)
)
_HpnicfevtPowerSupplyAC_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupplyAC = _HpnicfevtPowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6, 2)
)
_HpnicfevtPowerSupplyDC_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupplyDC = _HpnicfevtPowerSupplyDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6, 3)
)
_HpnicfevtPowerSupplySTD130W_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupplySTD130W = _HpnicfevtPowerSupplySTD130W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6, 4)
)
_HpnicfevtPowerSupplySTD180W_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupplySTD180W = _HpnicfevtPowerSupplySTD180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6, 5)
)
_HpnicfevtPowerSupplyPOE24Port_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupplyPOE24Port = _HpnicfevtPowerSupplyPOE24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6, 6)
)
_HpnicfevtPowerSupplyPOE48Port_ObjectIdentity = ObjectIdentity
hpnicfevtPowerSupplyPOE48Port = _HpnicfevtPowerSupplyPOE48Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 6, 7)
)
_HpnicfevtFan_ObjectIdentity = ObjectIdentity
hpnicfevtFan = _HpnicfevtFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 7)
)
_HpnicfevtHotSwapFan_ObjectIdentity = ObjectIdentity
hpnicfevtHotSwapFan = _HpnicfevtHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 7, 1)
)
_HpnicfevtNonHotSwapFan_ObjectIdentity = ObjectIdentity
hpnicfevtNonHotSwapFan = _HpnicfevtNonHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 7, 2)
)
_HpnicfevtSensor_ObjectIdentity = ObjectIdentity
hpnicfevtSensor = _HpnicfevtSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 8)
)
_HpnicfevtSensorTemperature_ObjectIdentity = ObjectIdentity
hpnicfevtSensorTemperature = _HpnicfevtSensorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 8, 1)
)
_HpnicfevtSensorVoltage_ObjectIdentity = ObjectIdentity
hpnicfevtSensorVoltage = _HpnicfevtSensorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 8, 2)
)
_HpnicfevtSensorFanSpeed_ObjectIdentity = ObjectIdentity
hpnicfevtSensorFanSpeed = _HpnicfevtSensorFanSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 8, 3)
)
_HpnicfevtModule_ObjectIdentity = ObjectIdentity
hpnicfevtModule = _HpnicfevtModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9)
)
_HpnicfevtModuleUnknownCard_ObjectIdentity = ObjectIdentity
hpnicfevtModuleUnknownCard = _HpnicfevtModuleUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 1)
)
_HpnicfevtModuleCommonCards_ObjectIdentity = ObjectIdentity
hpnicfevtModuleCommonCards = _HpnicfevtModuleCommonCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2)
)
_HpnicfevtModuleBoxCEN_ObjectIdentity = ObjectIdentity
hpnicfevtModuleBoxCEN = _HpnicfevtModuleBoxCEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 1)
)
_HpnicfevtModuleBoxIRF48GE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleBoxIRF48GE = _HpnicfevtModuleBoxIRF48GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 2)
)
_HpnicfevtModuleBoxIRF24GE24TGE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleBoxIRF24GE24TGE = _HpnicfevtModuleBoxIRF24GE24TGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 3)
)
_HpnicfevtModuleChassisMpu_ObjectIdentity = ObjectIdentity
hpnicfevtModuleChassisMpu = _HpnicfevtModuleChassisMpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 4)
)
_HpnicfevtModuleLPU48GE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleLPU48GE = _HpnicfevtModuleLPU48GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 5)
)
_HpnicfevtModuleLPU4GE4Serial_ObjectIdentity = ObjectIdentity
hpnicfevtModuleLPU4GE4Serial = _HpnicfevtModuleLPU4GE4Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 6)
)
_HpnicfevtModuleLPU4GE4Pos_ObjectIdentity = ObjectIdentity
hpnicfevtModuleLPU4GE4Pos = _HpnicfevtModuleLPU4GE4Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 7)
)
_HpnicfevtModuleLPU4GE4E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleLPU4GE4E1 = _HpnicfevtModuleLPU4GE4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 2, 8)
)
_HpnicfevtModuleRouterType_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRouterType = _HpnicfevtModuleRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3)
)
_HpnicfevtModuleRt_As_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_As = _HpnicfevtModuleRt_As_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 2)
)
_HpnicfevtModuleRt_Sa_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sa = _HpnicfevtModuleRt_Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 3)
)
_HpnicfevtModuleRt_Bi_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Bi = _HpnicfevtModuleRt_Bi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 4)
)
_HpnicfevtModuleRt_E12_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E12 = _HpnicfevtModuleRt_E12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5)
)
_HpnicfevtModuleRt_E14_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E14 = _HpnicfevtModuleRt_E14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 6)
)
_HpnicfevtModuleRt_Fe1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fe1 = _HpnicfevtModuleRt_Fe1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 7)
)
_HpnicfevtModuleRt_E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E1 = _HpnicfevtModuleRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 8)
)
_HpnicfevtModuleRt_Fe2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fe2 = _HpnicfevtModuleRt_Fe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 9)
)
_HpnicfevtModuleRt_Vi2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Vi2 = _HpnicfevtModuleRt_Vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 11)
)
_HpnicfevtModuleRt_Vi4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Vi4 = _HpnicfevtModuleRt_Vi4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 12)
)
_HpnicfevtModuleRt_Vi30_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Vi30 = _HpnicfevtModuleRt_Vi30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 13)
)
_HpnicfevtModuleRt_S1b_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_S1b = _HpnicfevtModuleRt_S1b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 14)
)
_HpnicfevtModuleRt_Sa2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sa2 = _HpnicfevtModuleRt_Sa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 15)
)
_HpnicfevtModuleRt_As16_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_As16 = _HpnicfevtModuleRt_As16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 16)
)
_HpnicfevtModuleRt_New8as_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_New8as = _HpnicfevtModuleRt_New8as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 17)
)
_HpnicfevtModuleRt_Sa1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sa1 = _HpnicfevtModuleRt_Sa1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 18)
)
_HpnicfevtModuleRt_Fxs2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fxs2 = _HpnicfevtModuleRt_Fxs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 19)
)
_HpnicfevtModuleRt_Fxo2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fxo2 = _HpnicfevtModuleRt_Fxo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 20)
)
_HpnicfevtModuleRt_Em2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Em2 = _HpnicfevtModuleRt_Em2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 21)
)
_HpnicfevtModuleRt_Fxs4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fxs4 = _HpnicfevtModuleRt_Fxs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 22)
)
_HpnicfevtModuleRt_Fxo4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fxo4 = _HpnicfevtModuleRt_Fxo4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 23)
)
_HpnicfevtModuleRt_Em4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Em4 = _HpnicfevtModuleRt_Em4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 24)
)
_HpnicfevtModuleRt_Sab_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sab = _HpnicfevtModuleRt_Sab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 25)
)
_HpnicfevtModuleRt_E1vi_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E1vi = _HpnicfevtModuleRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 26)
)
_HpnicfevtModuleRt_Am12_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Am12 = _HpnicfevtModuleRt_Am12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 27)
)
_HpnicfevtModuleRt_Am6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Am6 = _HpnicfevtModuleRt_Am6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 28)
)
_HpnicfevtModuleRt_Ndec_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ndec = _HpnicfevtModuleRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 29)
)
_HpnicfevtModuleRt_Newsa2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Newsa2 = _HpnicfevtModuleRt_Newsa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 30)
)
_HpnicfevtModuleRt_Aux_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Aux = _HpnicfevtModuleRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 31)
)
_HpnicfevtModuleRt_Console_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Console = _HpnicfevtModuleRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 32)
)
_HpnicfevtModuleRt_Sic_wan_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_wan = _HpnicfevtModuleRt_Sic_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 33)
)
_HpnicfevtModuleRt_Sic_1fe_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1fe = _HpnicfevtModuleRt_Sic_1fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 34)
)
_HpnicfevtModuleRt_Sic_1sa_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1sa = _HpnicfevtModuleRt_Sic_1sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 35)
)
_HpnicfevtModuleRt_Sic_3as_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_3as = _HpnicfevtModuleRt_Sic_3as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 36)
)
_HpnicfevtModuleRt_Sic_1e1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1e1 = _HpnicfevtModuleRt_Sic_1e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 37)
)
_HpnicfevtModuleRt_Sic_1t1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1t1 = _HpnicfevtModuleRt_Sic_1t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 38)
)
_HpnicfevtModuleRt_Sic_1bu_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1bu = _HpnicfevtModuleRt_Sic_1bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 39)
)
_HpnicfevtModuleRt_Sic_2bu_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_2bu = _HpnicfevtModuleRt_Sic_2bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 40)
)
_HpnicfevtModuleRt_Sic_1bs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1bs = _HpnicfevtModuleRt_Sic_1bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 41)
)
_HpnicfevtModuleRt_Sic_2bs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_2bs = _HpnicfevtModuleRt_Sic_2bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 42)
)
_HpnicfevtModuleRt_Sic_1am_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1am = _HpnicfevtModuleRt_Sic_1am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 43)
)
_HpnicfevtModuleRt_Sic_2am_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_2am = _HpnicfevtModuleRt_Sic_2am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 44)
)
_HpnicfevtModuleRt_Sic_1em_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1em = _HpnicfevtModuleRt_Sic_1em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 45)
)
_HpnicfevtModuleRt_Sic_2em_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_2em = _HpnicfevtModuleRt_Sic_2em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 46)
)
_HpnicfevtModuleRt_Sic_1fxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1fxs = _HpnicfevtModuleRt_Sic_1fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 47)
)
_HpnicfevtModuleRt_Sic_2fxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_2fxs = _HpnicfevtModuleRt_Sic_2fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 48)
)
_HpnicfevtModuleRt_Sic_1fxo_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_1fxo = _HpnicfevtModuleRt_Sic_1fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 49)
)
_HpnicfevtModuleRt_Sic_2fxo_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic_2fxo = _HpnicfevtModuleRt_Sic_2fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 50)
)
_HpnicfevtModuleRt_Fcm6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fcm6 = _HpnicfevtModuleRt_Fcm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 51)
)
_HpnicfevtModuleRt_Sa8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sa8 = _HpnicfevtModuleRt_Sa8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 52)
)
_HpnicfevtModuleRt_T11_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T11 = _HpnicfevtModuleRt_T11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 53)
)
_HpnicfevtModuleRt_T12_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T12 = _HpnicfevtModuleRt_T12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 54)
)
_HpnicfevtModuleRt_T14_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T14 = _HpnicfevtModuleRt_T14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 55)
)
_HpnicfevtModuleRt_T1vi_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T1vi = _HpnicfevtModuleRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 56)
)
_HpnicfevtModuleRt_Fcm4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fcm4 = _HpnicfevtModuleRt_Fcm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 57)
)
_HpnicfevtModuleRt_Fcm2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fcm2 = _HpnicfevtModuleRt_Fcm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 58)
)
_HpnicfevtModuleRt_Rtb21ce3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Rtb21ce3 = _HpnicfevtModuleRt_Rtb21ce3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 59)
)
_HpnicfevtModuleRt_Ame6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ame6 = _HpnicfevtModuleRt_Ame6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 60)
)
_HpnicfevtModuleRt_Ame12_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ame12 = _HpnicfevtModuleRt_Ame12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 61)
)
_HpnicfevtModuleRt_E11_f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E11_f = _HpnicfevtModuleRt_E11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 65)
)
_HpnicfevtModuleRt_E12_f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E12_f = _HpnicfevtModuleRt_E12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 66)
)
_HpnicfevtModuleRt_E14_f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E14_f = _HpnicfevtModuleRt_E14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 67)
)
_HpnicfevtModuleRt_T11_f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T11_f = _HpnicfevtModuleRt_T11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 68)
)
_HpnicfevtModuleRt_T12_f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T12_f = _HpnicfevtModuleRt_T12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 69)
)
_HpnicfevtModuleRt_T14_f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T14_f = _HpnicfevtModuleRt_T14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 70)
)
_HpnicfevtModuleRt_E11_f_17_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_E11_f_17 = _HpnicfevtModuleRt_E11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 71)
)
_HpnicfevtModuleRt_T11_f_17_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T11_f_17 = _HpnicfevtModuleRt_T11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 72)
)
_HpnicfevtModuleRt_Rtb21ct3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Rtb21ct3 = _HpnicfevtModuleRt_Rtb21ct3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 73)
)
_HpnicfevtModuleRt_Atmadsl1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atmadsl1 = _HpnicfevtModuleRt_Atmadsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 74)
)
_HpnicfevtModuleRt_Atmadsl2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atmadsl2 = _HpnicfevtModuleRt_Atmadsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 75)
)
_HpnicfevtModuleRt_Atm155m_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atm155m = _HpnicfevtModuleRt_Atm155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 76)
)
_HpnicfevtModuleRt_Ase8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ase8 = _HpnicfevtModuleRt_Ase8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 77)
)
_HpnicfevtModuleRt_Ase16_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ase16 = _HpnicfevtModuleRt_Ase16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 78)
)
_HpnicfevtModuleRt_Sae4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sae4 = _HpnicfevtModuleRt_Sae4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 79)
)
_HpnicfevtModuleRt_Sae2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sae2 = _HpnicfevtModuleRt_Sae2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 80)
)
_HpnicfevtModuleRt_Atmshdsl1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atmshdsl1 = _HpnicfevtModuleRt_Atmshdsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 90)
)
_HpnicfevtModuleRt_Atmshdsl2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atmshdsl2 = _HpnicfevtModuleRt_Atmshdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 91)
)
_HpnicfevtModuleRt_Atmshdsl4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atmshdsl4 = _HpnicfevtModuleRt_Atmshdsl4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 92)
)
_HpnicfevtModuleRt_Atm25m_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atm25m = _HpnicfevtModuleRt_Atm25m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 93)
)
_HpnicfevtModuleRt_Atme3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atme3 = _HpnicfevtModuleRt_Atme3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 94)
)
_HpnicfevtModuleRt_Atmt3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atmt3 = _HpnicfevtModuleRt_Atmt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 95)
)
_HpnicfevtModuleRt_Xdsl_fec_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Xdsl_fec = _HpnicfevtModuleRt_Xdsl_fec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 96)
)
_HpnicfevtModuleRt_Xdsl_adsl_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Xdsl_adsl = _HpnicfevtModuleRt_Xdsl_adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 97)
)
_HpnicfevtModuleRt_Xdsl_gshdsl_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Xdsl_gshdsl = _HpnicfevtModuleRt_Xdsl_gshdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 98)
)
_HpnicfevtModuleRt_Xdsl_bri_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Xdsl_bri = _HpnicfevtModuleRt_Xdsl_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 99)
)
_HpnicfevtModuleRt_Xdsl_scc_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Xdsl_scc = _HpnicfevtModuleRt_Xdsl_scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 100)
)
_HpnicfevtModuleRt_Ge1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ge1 = _HpnicfevtModuleRt_Ge1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 101)
)
_HpnicfevtModuleRt_Pos155m_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Pos155m = _HpnicfevtModuleRt_Pos155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 102)
)
_HpnicfevtModuleRt_Cpos_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Cpos = _HpnicfevtModuleRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 103)
)
_HpnicfevtModuleRt_Fe1op_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fe1op = _HpnicfevtModuleRt_Fe1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 104)
)
_HpnicfevtModuleRt_Sae8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sae8 = _HpnicfevtModuleRt_Sae8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 105)
)
_HpnicfevtModuleRt_Atm155m_mm_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atm155m_mm = _HpnicfevtModuleRt_Atm155m_mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 106)
)
_HpnicfevtModuleRt_Atm155m_sm_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atm155m_sm = _HpnicfevtModuleRt_Atm155m_sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 107)
)
_HpnicfevtModuleRt_Atm155m_sml_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Atm155m_sml = _HpnicfevtModuleRt_Atm155m_sml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 108)
)
_HpnicfevtModuleRt_Fe1op_sfx_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fe1op_sfx = _HpnicfevtModuleRt_Fe1op_sfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 109)
)
_HpnicfevtModuleRt_Fe1op_mfx_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fe1op_mfx = _HpnicfevtModuleRt_Fe1op_mfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 110)
)
_HpnicfevtModuleRt_Cpos_t1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Cpos_t1 = _HpnicfevtModuleRt_Cpos_t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 111)
)
_HpnicfevtModuleRt_Ge1op_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ge1op = _HpnicfevtModuleRt_Ge1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 112)
)
_HpnicfevtModuleRt_Ge2op_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ge2op = _HpnicfevtModuleRt_Ge2op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 113)
)
_HpnicfevtModuleRt_Ge2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Ge2 = _HpnicfevtModuleRt_Ge2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 114)
)
_HpnicfevtModuleRt_Fix_1wan_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fix_1wan = _HpnicfevtModuleRt_Fix_1wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 115)
)
_HpnicfevtModuleRt_Fix_1sae_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fix_1sae = _HpnicfevtModuleRt_Fix_1sae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 116)
)
_HpnicfevtModuleRt_Cavium_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Cavium = _HpnicfevtModuleRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 117)
)
_HpnicfevtModuleRt_Sic1Eth_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Sic1Eth = _HpnicfevtModuleRt_Sic1Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 118)
)
_HpnicfevtModuleRt_atm1ADSLI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_atm1ADSLI = _HpnicfevtModuleRt_atm1ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 119)
)
_HpnicfevtModuleRt_atm2ADSLI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_atm2ADSLI = _HpnicfevtModuleRt_atm2ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 120)
)
_HpnicfevtModuleRt_fix_e11_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_fix_e11 = _HpnicfevtModuleRt_fix_e11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 121)
)
_HpnicfevtModuleRt_fix_t11_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_fix_t11 = _HpnicfevtModuleRt_fix_t11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 122)
)
_HpnicfevtModuleRt_e18_75_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_e18_75 = _HpnicfevtModuleRt_e18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 123)
)
_HpnicfevtModuleRt_e18_120_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_e18_120 = _HpnicfevtModuleRt_e18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 124)
)
_HpnicfevtModuleRt_t18_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_t18 = _HpnicfevtModuleRt_t18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 125)
)
_HpnicfevtModuleRt_sic_1vifxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_1vifxs = _HpnicfevtModuleRt_sic_1vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 126)
)
_HpnicfevtModuleRt_sic_1vifxo_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_1vifxo = _HpnicfevtModuleRt_sic_1vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 127)
)
_HpnicfevtModuleRt_sic_2vifxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_2vifxs = _HpnicfevtModuleRt_sic_2vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 128)
)
_HpnicfevtModuleRt_sic_2vifxo_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_2vifxo = _HpnicfevtModuleRt_sic_2vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 129)
)
_HpnicfevtModuleRt_xdsl_fec_new_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_xdsl_fec_new = _HpnicfevtModuleRt_xdsl_fec_new_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 130)
)
_HpnicfevtModuleRt_xdsl_sa_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_xdsl_sa = _HpnicfevtModuleRt_xdsl_sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 131)
)
_HpnicfevtModuleRt_bs4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_bs4 = _HpnicfevtModuleRt_bs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 132)
)
_HpnicfevtModuleRt_ima_8e175_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ima_8e175 = _HpnicfevtModuleRt_ima_8e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 133)
)
_HpnicfevtModuleRt_ima_8e1120_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ima_8e1120 = _HpnicfevtModuleRt_ima_8e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 134)
)
_HpnicfevtModuleRt_ima_4e175_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ima_4e175 = _HpnicfevtModuleRt_ima_4e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 135)
)
_HpnicfevtModuleRt_ima_4e1120_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ima_4e1120 = _HpnicfevtModuleRt_ima_4e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 136)
)
_HpnicfevtModuleRt_ima_8t1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ima_8t1 = _HpnicfevtModuleRt_ima_8t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 137)
)
_HpnicfevtModuleRt_ima_4t1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ima_4t1 = _HpnicfevtModuleRt_ima_4t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 138)
)
_HpnicfevtModuleRt_sic_1t1f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_1t1f = _HpnicfevtModuleRt_sic_1t1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 139)
)
_HpnicfevtModuleRt_sic_1e1f_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_1e1f = _HpnicfevtModuleRt_sic_1e1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 140)
)
_HpnicfevtModuleRt_VG_16fxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_16fxs = _HpnicfevtModuleRt_VG_16fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 141)
)
_HpnicfevtModuleRt_VG_32fxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_32fxs = _HpnicfevtModuleRt_VG_32fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 142)
)
_HpnicfevtModuleRt_VG_8fxo_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_8fxo = _HpnicfevtModuleRt_VG_8fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 143)
)
_HpnicfevtModuleRt_VG_2fe_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_2fe = _HpnicfevtModuleRt_VG_2fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 144)
)
_HpnicfevtModuleRt_sib_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sib = _HpnicfevtModuleRt_sib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 145)
)
_HpnicfevtModuleRt_cie32_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_cie32 = _HpnicfevtModuleRt_cie32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 146)
)
_HpnicfevtModuleRt_cie64_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_cie64 = _HpnicfevtModuleRt_cie64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 147)
)
_HpnicfevtModuleRt_cie96_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_cie96 = _HpnicfevtModuleRt_cie96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 148)
)
_HpnicfevtModuleRt_Fe4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_Fe4 = _HpnicfevtModuleRt_Fe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 149)
)
_HpnicfevtModuleRt_fxs4fxo1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_fxs4fxo1 = _HpnicfevtModuleRt_fxs4fxo1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 150)
)
_HpnicfevtModuleRt_atm1shdsl4wire_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_atm1shdsl4wire = _HpnicfevtModuleRt_atm1shdsl4wire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 151)
)
_HpnicfevtModuleRt_atmIma4shdsl_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_atmIma4shdsl = _HpnicfevtModuleRt_atmIma4shdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 152)
)
_HpnicfevtModuleRt_ls4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ls4 = _HpnicfevtModuleRt_ls4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 153)
)
_HpnicfevtModuleRt_ls8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ls8 = _HpnicfevtModuleRt_ls8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 154)
)
_HpnicfevtModuleRt_ls16_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ls16 = _HpnicfevtModuleRt_ls16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 155)
)
_HpnicfevtModuleRt_sic_adls2plus_isdn_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_adls2plus_isdn = _HpnicfevtModuleRt_sic_adls2plus_isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 156)
)
_HpnicfevtModuleRt_sic_adls2plus_pots_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sic_adls2plus_pots = _HpnicfevtModuleRt_sic_adls2plus_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 157)
)
_HpnicfevtModuleRt_ft3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ft3 = _HpnicfevtModuleRt_ft3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 158)
)
_HpnicfevtModuleRt_ce32_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ce32 = _HpnicfevtModuleRt_ce32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 159)
)
_HpnicfevtModuleRt_bsv2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_bsv2 = _HpnicfevtModuleRt_bsv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 160)
)
_HpnicfevtModuleRt_bsv4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_bsv4 = _HpnicfevtModuleRt_bsv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 161)
)
_HpnicfevtModuleRt_RPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RPU = _HpnicfevtModuleRt_RPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 162)
)
_HpnicfevtModuleRt_ERPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ERPU = _HpnicfevtModuleRt_ERPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 163)
)
_HpnicfevtModuleRt_SSL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SSL = _HpnicfevtModuleRt_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 164)
)
_HpnicfevtModuleRt_NSA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSA = _HpnicfevtModuleRt_NSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 165)
)
_HpnicfevtModuleRT_SIC_1GEC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_1GEC = _HpnicfevtModuleRT_SIC_1GEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 200)
)
_HpnicfevtModuleRT_24FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_24FSW = _HpnicfevtModuleRT_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 201)
)
_HpnicfevtModuleRT_24FSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_24FSWP = _HpnicfevtModuleRT_24FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 202)
)
_HpnicfevtModuleRT_16FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_16FSW = _HpnicfevtModuleRT_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 203)
)
_HpnicfevtModuleRT_16FSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_16FSWP = _HpnicfevtModuleRT_16FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 204)
)
_HpnicfevtModuleRT_1VE1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_1VE1 = _HpnicfevtModuleRT_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 205)
)
_HpnicfevtModuleRT_1VT1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_1VT1 = _HpnicfevtModuleRT_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 206)
)
_HpnicfevtModuleRT_2VE1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_2VE1 = _HpnicfevtModuleRT_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 207)
)
_HpnicfevtModuleRT_2VT1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_2VT1 = _HpnicfevtModuleRT_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 208)
)
_HpnicfevtModuleRT_SIC_4FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_4FSW = _HpnicfevtModuleRT_SIC_4FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 209)
)
_HpnicfevtModuleRT_SIC_4FSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_4FSWP = _HpnicfevtModuleRT_SIC_4FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 210)
)
_HpnicfevtModuleRT_DSIC_9FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_DSIC_9FSW = _HpnicfevtModuleRT_DSIC_9FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 211)
)
_HpnicfevtModuleRT_DSIC_9FSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_DSIC_9FSWP = _HpnicfevtModuleRT_DSIC_9FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 212)
)
_HpnicfevtModuleRT_SIC_1VE1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_1VE1 = _HpnicfevtModuleRT_SIC_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 213)
)
_HpnicfevtModuleRT_SIC_1VT1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_1VT1 = _HpnicfevtModuleRT_SIC_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 214)
)
_HpnicfevtModuleRT_VCPM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_VCPM = _HpnicfevtModuleRT_VCPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 215)
)
_HpnicfevtModuleRT_VPM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_VPM = _HpnicfevtModuleRT_VPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 216)
)
_HpnicfevtModuleRT_VPMA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_VPMA = _HpnicfevtModuleRT_VPMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 217)
)
_HpnicfevtModuleRT_VPMB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_VPMB = _HpnicfevtModuleRT_VPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 218)
)
_HpnicfevtModuleRT_VPMC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_VPMC = _HpnicfevtModuleRT_VPMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 219)
)
_HpnicfevtModuleRt_fe18_75_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_fe18_75 = _HpnicfevtModuleRt_fe18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 220)
)
_HpnicfevtModuleRt_fe18_120_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_fe18_120 = _HpnicfevtModuleRt_fe18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 221)
)
_HpnicfevtModuleRt_ft18_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ft18 = _HpnicfevtModuleRt_ft18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 222)
)
_HpnicfevtModuleRt_CF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CF = _HpnicfevtModuleRt_CF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 223)
)
_HpnicfevtModuleRt_bsv2_v2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_bsv2_v2 = _HpnicfevtModuleRt_bsv2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 224)
)
_HpnicfevtModuleRt_e1vi1_v2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_e1vi1_v2 = _HpnicfevtModuleRt_e1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 225)
)
_HpnicfevtModuleRt_e1vi2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_e1vi2 = _HpnicfevtModuleRt_e1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 226)
)
_HpnicfevtModuleRt_t1vi1_v2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_t1vi1_v2 = _HpnicfevtModuleRt_t1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 227)
)
_HpnicfevtModuleRt_t1vi2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_t1vi2 = _HpnicfevtModuleRt_t1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 228)
)
_HpnicfevtModuleRt_osm_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_osm = _HpnicfevtModuleRt_osm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 229)
)
_HpnicfevtModuleRt_sd707_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_sd707 = _HpnicfevtModuleRt_sd707_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 230)
)
_HpnicfevtModuleRt_dm_epri_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_dm_epri = _HpnicfevtModuleRt_dm_epri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 231)
)
_HpnicfevtModuleRt_dm_tpri_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_dm_tpri = _HpnicfevtModuleRt_dm_tpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 232)
)
_HpnicfevtModuleRt_ERPU_H_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ERPU_H = _HpnicfevtModuleRt_ERPU_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 233)
)
_HpnicfevtModuleRT_SIC_1BSV_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_1BSV = _HpnicfevtModuleRT_SIC_1BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 234)
)
_HpnicfevtModuleRT_SIC_2BSV_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_2BSV = _HpnicfevtModuleRT_SIC_2BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 235)
)
_HpnicfevtModuleRt_gbe8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_gbe8 = _HpnicfevtModuleRt_gbe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 236)
)
_HpnicfevtModuleRt_gbe4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_gbe4 = _HpnicfevtModuleRt_gbe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 237)
)
_HpnicfevtModuleRt_cpos2_v2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_cpos2_v2 = _HpnicfevtModuleRt_cpos2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 238)
)
_HpnicfevtModuleRt_cpos1_v2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_cpos1_v2 = _HpnicfevtModuleRt_cpos1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 239)
)
_HpnicfevtModuleRt_oap_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_oap = _HpnicfevtModuleRt_oap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 240)
)
_HpnicfevtModuleRT_48FSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_48FSWP = _HpnicfevtModuleRT_48FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 241)
)
_HpnicfevtModuleRT_48FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_48FSW = _HpnicfevtModuleRT_48FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 242)
)
_HpnicfevtModuleRT_ASM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_ASM = _HpnicfevtModuleRT_ASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 243)
)
_HpnicfevtModuleRT_SIC_1FEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_1FEF = _HpnicfevtModuleRT_SIC_1FEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 244)
)
_HpnicfevtModuleRT_XMIM_24FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_XMIM_24FSW = _HpnicfevtModuleRT_XMIM_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 245)
)
_HpnicfevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_WLAN_AG_1RADIO = _HpnicfevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 246)
)
_HpnicfevtModuleRT_1CE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_1CE3 = _HpnicfevtModuleRT_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 247)
)
_HpnicfevtModuleRT_XMIM_16FSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_XMIM_16FSW = _HpnicfevtModuleRT_XMIM_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 248)
)
_HpnicfevtModuleRT_OAPS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAPS = _HpnicfevtModuleRT_OAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 249)
)
_HpnicfevtModuleRT_NAM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_NAM = _HpnicfevtModuleRT_NAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 250)
)
_HpnicfevtModuleRT_RPE_X1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_RPE_X1 = _HpnicfevtModuleRT_RPE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 251)
)
_HpnicfevtModuleRT_FIP_100_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_FIP_100 = _HpnicfevtModuleRT_FIP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 252)
)
_HpnicfevtModuleRT_FIP_200_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_FIP_200 = _HpnicfevtModuleRT_FIP_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 253)
)
_HpnicfevtModuleRT_SIC_8AS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_8AS = _HpnicfevtModuleRT_SIC_8AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 254)
)
_HpnicfevtModuleRT_WAAM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_WAAM = _HpnicfevtModuleRT_WAAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 255)
)
_HpnicfevtModuleRt_msp4p_OC3c_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_msp4p_OC3c = _HpnicfevtModuleRt_msp4p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 256)
)
_HpnicfevtModuleRt_1pos_oc48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_1pos_oc48 = _HpnicfevtModuleRt_1pos_oc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 257)
)
_HpnicfevtModuleRt_xgbe_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_xgbe = _HpnicfevtModuleRt_xgbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 258)
)
_HpnicfevtModuleRT_EADM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_EADM = _HpnicfevtModuleRT_EADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 259)
)
_HpnicfevtModuleRT_VCM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_VCM = _HpnicfevtModuleRT_VCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 260)
)
_HpnicfevtModuleRT_SIC_2FXS1FXO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_2FXS1FXO = _HpnicfevtModuleRT_SIC_2FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 261)
)
_HpnicfevtModuleRT_8FXS8FXO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_8FXS8FXO = _HpnicfevtModuleRT_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 262)
)
_HpnicfevtModuleRT_16FXS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_16FXS = _HpnicfevtModuleRT_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 263)
)
_HpnicfevtModuleRT_OAPS_ICM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAPS_ICM = _HpnicfevtModuleRT_OAPS_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 264)
)
_HpnicfevtModuleRT_OAP_ICM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAP_ICM = _HpnicfevtModuleRT_OAP_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 265)
)
_HpnicfevtModuleRT_8fe_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_8fe = _HpnicfevtModuleRT_8fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 266)
)
_HpnicfevtModuleRT_4gbp_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_4gbp = _HpnicfevtModuleRT_4gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 267)
)
_HpnicfevtModuleRT_MPU_G2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_MPU_G2 = _HpnicfevtModuleRT_MPU_G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 268)
)
_HpnicfevtModuleRT_OAPS_OCE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAPS_OCE = _HpnicfevtModuleRT_OAPS_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 269)
)
_HpnicfevtModuleRT_OAP_OCE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAP_OCE = _HpnicfevtModuleRT_OAP_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 270)
)
_HpnicfevtModuleRT_OAPS_ICE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAPS_ICE = _HpnicfevtModuleRT_OAPS_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 271)
)
_HpnicfevtModuleRT_OAP_ICE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_OAP_ICE = _HpnicfevtModuleRT_OAP_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 272)
)
_HpnicfevtModuleRT_SIC_16AS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_16AS = _HpnicfevtModuleRT_SIC_16AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 273)
)
_HpnicfevtModuleRT_SPE_FWM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SPE_FWM = _HpnicfevtModuleRT_SPE_FWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 274)
)
_HpnicfevtModuleRT_cls2p_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_cls2p = _HpnicfevtModuleRT_cls2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 275)
)
_HpnicfevtModuleRT_cls1p_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_cls1p = _HpnicfevtModuleRT_cls1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 276)
)
_HpnicfevtModuleRT_SIC_2E1_F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_2E1_F = _HpnicfevtModuleRT_SIC_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 277)
)
_HpnicfevtModuleRT_SIC_1E1_F_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_1E1_F_V2 = _HpnicfevtModuleRT_SIC_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 278)
)
_HpnicfevtModuleRT_MCU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_MCU = _HpnicfevtModuleRT_MCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 279)
)
_HpnicfevtModuleRT_ACU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_ACU = _HpnicfevtModuleRT_ACU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 280)
)
_HpnicfevtModuleRT_1ATM_OC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_1ATM_OC3 = _HpnicfevtModuleRT_1ATM_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 281)
)
_HpnicfevtModuleRT_RSE_X1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_RSE_X1 = _HpnicfevtModuleRT_RSE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 282)
)
_HpnicfevtModuleRT_FIP_210_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_FIP_210 = _HpnicfevtModuleRT_FIP_210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 283)
)
_HpnicfevtModuleRT_1expa_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_1expa = _HpnicfevtModuleRT_1expa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 284)
)
_HpnicfevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_WLAN_SIC_N_1RADIO = _HpnicfevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 285)
)
_HpnicfevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_WLAN_SIC_BG_1RADIO = _HpnicfevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 286)
)
_HpnicfevtModuleRT_al2p_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_al2p = _HpnicfevtModuleRT_al2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 287)
)
_HpnicfevtModuleRT_msp2p_OC3c_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_msp2p_OC3c = _HpnicfevtModuleRT_msp2p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 288)
)
_HpnicfevtModuleRT_8gbp_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_8gbp = _HpnicfevtModuleRT_8gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 289)
)
_HpnicfevtModuleRT_SIC_EPON_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_EPON = _HpnicfevtModuleRT_SIC_EPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 290)
)
_HpnicfevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_SIC_3G_GSM_H3 = _HpnicfevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 291)
)
_HpnicfevtModuleRT_msp2p_OC12c_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRT_msp2p_OC12c = _HpnicfevtModuleRT_msp2p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 292)
)
_HpnicfevtModuleRt_msp4p_OC12c_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_msp4p_OC12c = _HpnicfevtModuleRt_msp4p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 293)
)
_HpnicfevtModuleRt_al1p_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_al1p = _HpnicfevtModuleRt_al1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 294)
)
_HpnicfevtModuleRt_OAP_100_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_OAP_100 = _HpnicfevtModuleRt_OAP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 295)
)
_HpnicfevtModuleRt_FIP_110_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_110 = _HpnicfevtModuleRt_FIP_110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 296)
)
_HpnicfevtModuleRt_OSM_SSM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_OSM_SSM = _HpnicfevtModuleRt_OSM_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 297)
)
_HpnicfevtModuleRt_OAP_SSM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_OAP_SSM = _HpnicfevtModuleRt_OAP_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 298)
)
_HpnicfevtModuleRt_rs2p_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_rs2p = _HpnicfevtModuleRt_rs2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 299)
)
_HpnicfevtModuleRt_SAP_48GBE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_48GBE = _HpnicfevtModuleRt_SAP_48GBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 300)
)
_HpnicfevtModuleRt_SAP_48GBP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_48GBP = _HpnicfevtModuleRt_SAP_48GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 301)
)
_HpnicfevtModuleRt_SAP_24GBP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_24GBP = _HpnicfevtModuleRt_SAP_24GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 302)
)
_HpnicfevtModuleRt_SPE_SSL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPE_SSL = _HpnicfevtModuleRt_SPE_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 303)
)
_HpnicfevtModuleRt_SIC_AUDIO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_AUDIO = _HpnicfevtModuleRt_SIC_AUDIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 304)
)
_HpnicfevtModuleRt_FIC_1E1POS_H3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIC_1E1POS_H3 = _HpnicfevtModuleRt_FIC_1E1POS_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 305)
)
_HpnicfevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_DSIC_4FXS1FXO = _HpnicfevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 306)
)
_HpnicfevtModuleRt_FIC_CPOS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIC_CPOS = _HpnicfevtModuleRt_FIC_CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 307)
)
_HpnicfevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_DSIC_1SHDSL_8W = _HpnicfevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 308)
)
_HpnicfevtModuleRt_SIC_3G_TD_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_3G_TD = _HpnicfevtModuleRt_SIC_3G_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 309)
)
_HpnicfevtModuleRt_SIC_3G_CDMA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_3G_CDMA = _HpnicfevtModuleRt_SIC_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 310)
)
_HpnicfevtModuleRt_SIC_3G_HSPA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_3G_HSPA = _HpnicfevtModuleRt_SIC_3G_HSPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 311)
)
_HpnicfevtModuleRt_FIC_OAP_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIC_OAP_V2 = _HpnicfevtModuleRt_FIC_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 312)
)
_HpnicfevtModuleRt_MIM_OAP_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MIM_OAP_V2 = _HpnicfevtModuleRt_MIM_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 313)
)
_HpnicfevtModuleRt_MIM_OAPS_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MIM_OAPS_V2 = _HpnicfevtModuleRt_MIM_OAPS_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 314)
)
_HpnicfevtModuleRt_HMIM_1CT3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1CT3 = _HpnicfevtModuleRt_HMIM_1CT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 315)
)
_HpnicfevtModuleRt_HMIM_1CE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1CE3 = _HpnicfevtModuleRt_HMIM_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 316)
)
_HpnicfevtModuleRt_HMIM_1POS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1POS = _HpnicfevtModuleRt_HMIM_1POS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 317)
)
_HpnicfevtModuleRt_HMIM_2SAE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2SAE = _HpnicfevtModuleRt_HMIM_2SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 318)
)
_HpnicfevtModuleRt_HMIM_4SAE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4SAE = _HpnicfevtModuleRt_HMIM_4SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 319)
)
_HpnicfevtModuleRt_HMIM_8SAE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8SAE = _HpnicfevtModuleRt_HMIM_8SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 320)
)
_HpnicfevtModuleRt_HMIM_8ASE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8ASE = _HpnicfevtModuleRt_HMIM_8ASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 321)
)
_HpnicfevtModuleRt_HMIM_16ASE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_16ASE = _HpnicfevtModuleRt_HMIM_16ASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 322)
)
_HpnicfevtModuleRt_HMIM_1E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1E1 = _HpnicfevtModuleRt_HMIM_1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 323)
)
_HpnicfevtModuleRt_HMIM_2E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2E1 = _HpnicfevtModuleRt_HMIM_2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 324)
)
_HpnicfevtModuleRt_HMIM_4E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4E1 = _HpnicfevtModuleRt_HMIM_4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 325)
)
_HpnicfevtModuleRt_HMIM_8E1_75_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8E1_75 = _HpnicfevtModuleRt_HMIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 326)
)
_HpnicfevtModuleRt_HMIM_1E1_F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1E1_F = _HpnicfevtModuleRt_HMIM_1E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 327)
)
_HpnicfevtModuleRt_HMIM_2E1_F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2E1_F = _HpnicfevtModuleRt_HMIM_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 328)
)
_HpnicfevtModuleRt_HMIM_4E1_F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4E1_F = _HpnicfevtModuleRt_HMIM_4E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 329)
)
_HpnicfevtModuleRt_HMIM_8E1_F_75_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8E1_F_75 = _HpnicfevtModuleRt_HMIM_8E1_F_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 330)
)
_HpnicfevtModuleRt_HMIM_6AM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_6AM = _HpnicfevtModuleRt_HMIM_6AM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 331)
)
_HpnicfevtModuleRt_HMIM_6FCM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_6FCM = _HpnicfevtModuleRt_HMIM_6FCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 332)
)
_HpnicfevtModuleRt_HMIM_2T1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2T1 = _HpnicfevtModuleRt_HMIM_2T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 333)
)
_HpnicfevtModuleRt_HMIM_4T1_F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4T1_F = _HpnicfevtModuleRt_HMIM_4T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 334)
)
_HpnicfevtModuleRt_HMIM_8T1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8T1 = _HpnicfevtModuleRt_HMIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 335)
)
_HpnicfevtModuleRt_HMIM_8T1_F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8T1_F = _HpnicfevtModuleRt_HMIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 336)
)
_HpnicfevtModuleRt_HMIM_1VE1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1VE1 = _HpnicfevtModuleRt_HMIM_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 337)
)
_HpnicfevtModuleRt_HMIM_1VT1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1VT1 = _HpnicfevtModuleRt_HMIM_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 338)
)
_HpnicfevtModuleRt_HMIM_2VE1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2VE1 = _HpnicfevtModuleRt_HMIM_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 339)
)
_HpnicfevtModuleRt_HMIM_2VT1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2VT1 = _HpnicfevtModuleRt_HMIM_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 340)
)
_HpnicfevtModuleRt_HMIM_8FXS8FXO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8FXS8FXO = _HpnicfevtModuleRt_HMIM_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 341)
)
_HpnicfevtModuleRt_HMIM_16FXS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_16FXS = _HpnicfevtModuleRt_HMIM_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 342)
)
_HpnicfevtModuleRt_HMIM_4FXS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4FXS = _HpnicfevtModuleRt_HMIM_4FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 343)
)
_HpnicfevtModuleRt_HMIM_4FXO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4FXO = _HpnicfevtModuleRt_HMIM_4FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 344)
)
_HpnicfevtModuleRt_HMIM_4EM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4EM = _HpnicfevtModuleRt_HMIM_4EM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 345)
)
_HpnicfevtModuleRt_HMIM_4BSV_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4BSV = _HpnicfevtModuleRt_HMIM_4BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 346)
)
_HpnicfevtModuleRt_SIC_CNDE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_CNDE = _HpnicfevtModuleRt_SIC_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 347)
)
_HpnicfevtModuleRt_ESM_CNDE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ESM_CNDE = _HpnicfevtModuleRt_ESM_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 348)
)
_HpnicfevtModuleRt_ESM_CNDE_M_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ESM_CNDE_M = _HpnicfevtModuleRt_ESM_CNDE_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 349)
)
_HpnicfevtModuleRt_SR6602_X1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SR6602_X1 = _HpnicfevtModuleRt_SR6602_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 350)
)
_HpnicfevtModuleRt_SR6602_X2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SR6602_X2 = _HpnicfevtModuleRt_SR6602_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 351)
)
_HpnicfevtModuleRt_MCP_X1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MCP_X1 = _HpnicfevtModuleRt_MCP_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 352)
)
_HpnicfevtModuleRt_MCP_X2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MCP_X2 = _HpnicfevtModuleRt_MCP_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 353)
)
_HpnicfevtModuleRt_FIP_10_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_10 = _HpnicfevtModuleRt_FIP_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 354)
)
_HpnicfevtModuleRt_FIP_20_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_20 = _HpnicfevtModuleRt_FIP_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 355)
)
_HpnicfevtModuleRt_RSE_X2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RSE_X2 = _HpnicfevtModuleRt_RSE_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 356)
)
_HpnicfevtModuleRt_FIP_600_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_600 = _HpnicfevtModuleRt_FIP_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 357)
)
_HpnicfevtModuleRt_SAP_4EXP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_4EXP = _HpnicfevtModuleRt_SAP_4EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 358)
)
_HpnicfevtModuleRt_SFE_X1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SFE_X1 = _HpnicfevtModuleRt_SFE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 359)
)
_HpnicfevtModuleRt_SFE_A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SFE_A1 = _HpnicfevtModuleRt_SFE_A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 360)
)
_HpnicfevtModuleRt_HMIM_24GSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_24GSW = _HpnicfevtModuleRt_HMIM_24GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 361)
)
_HpnicfevtModuleRt_HMIM_24GSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_24GSWP = _HpnicfevtModuleRt_HMIM_24GSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 362)
)
_HpnicfevtModuleRt_MPU100_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MPU100 = _HpnicfevtModuleRt_MPU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 363)
)
_HpnicfevtModuleRt_SPU100_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPU100 = _HpnicfevtModuleRt_SPU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 364)
)
_HpnicfevtModuleRt_SPU200_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPU200 = _HpnicfevtModuleRt_SPU200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 365)
)
_HpnicfevtModuleRt_WLAN_N_1RADIO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_WLAN_N_1RADIO = _HpnicfevtModuleRt_WLAN_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 366)
)
_HpnicfevtModuleRt_3G_CDMA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_3G_CDMA = _HpnicfevtModuleRt_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 367)
)
_HpnicfevtModuleRt_3G_WCDMA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_3G_WCDMA = _HpnicfevtModuleRt_3G_WCDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 368)
)
_HpnicfevtModuleRt_3G_HSPAPLUS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_3G_HSPAPLUS = _HpnicfevtModuleRt_3G_HSPAPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 369)
)
_HpnicfevtModuleRt_VPM_128_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VPM_128 = _HpnicfevtModuleRt_VPM_128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 370)
)
_HpnicfevtModuleRt_VPM_256_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VPM_256 = _HpnicfevtModuleRt_VPM_256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 371)
)
_HpnicfevtModuleRt_VPM_512_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VPM_512 = _HpnicfevtModuleRt_VPM_512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 372)
)
_HpnicfevtModuleRt_HMIM_8GEE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8GEE = _HpnicfevtModuleRt_HMIM_8GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 373)
)
_HpnicfevtModuleRt_HMIM_4GEE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4GEE = _HpnicfevtModuleRt_HMIM_4GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 374)
)
_HpnicfevtModuleRt_HMIM_2GEE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2GEE = _HpnicfevtModuleRt_HMIM_2GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 375)
)
_HpnicfevtModuleRt_HMIM_8GEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8GEF = _HpnicfevtModuleRt_HMIM_8GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 376)
)
_HpnicfevtModuleRt_HMIM_4GEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_4GEF = _HpnicfevtModuleRt_HMIM_4GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 377)
)
_HpnicfevtModuleRt_HMIM_2GEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2GEF = _HpnicfevtModuleRt_HMIM_2GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 378)
)
_HpnicfevtModuleRt_SPU300_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPU300 = _HpnicfevtModuleRt_SPU300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 379)
)
_HpnicfevtModuleRt_HMIM_1CPOS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1CPOS = _HpnicfevtModuleRt_HMIM_1CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 380)
)
_HpnicfevtModuleRt_HMIM_2CPOS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_2CPOS = _HpnicfevtModuleRt_HMIM_2CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 381)
)
_HpnicfevtModuleRt_SPU100_5080_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPU100_5080 = _HpnicfevtModuleRt_SPU100_5080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 382)
)
_HpnicfevtModuleRt_SPU200_5080_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPU200_5080 = _HpnicfevtModuleRt_SPU200_5080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 383)
)
_HpnicfevtModuleRt_SPU300_5080_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SPU300_5080 = _HpnicfevtModuleRt_SPU300_5080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 384)
)
_HpnicfevtModuleRt_4G_LTE_Verizon_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_4G_LTE_Verizon = _HpnicfevtModuleRt_4G_LTE_Verizon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 385)
)
_HpnicfevtModuleRt_4G_LTE_Global_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_4G_LTE_Global = _HpnicfevtModuleRt_4G_LTE_Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 386)
)
_HpnicfevtModuleRt_HMIM_1ATM_OC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_1ATM_OC3 = _HpnicfevtModuleRt_HMIM_1ATM_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 387)
)
_HpnicfevtModuleRt_SIC_1E1_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_1E1_V2 = _HpnicfevtModuleRt_SIC_1E1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 388)
)
_HpnicfevtModuleRt_FIP_300_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_300 = _HpnicfevtModuleRt_FIP_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 389)
)
_HpnicfevtModuleRt_FIP_310_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_310 = _HpnicfevtModuleRt_FIP_310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 390)
)
_HpnicfevtModuleRt_TS8P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_TS8P = _HpnicfevtModuleRt_TS8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 391)
)
_HpnicfevtModuleRt_4G4P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_4G4P = _HpnicfevtModuleRt_4G4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 392)
)
_HpnicfevtModuleRt_SIC_4G_LTE_V_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4G_LTE_V = _HpnicfevtModuleRt_SIC_4G_LTE_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 393)
)
_HpnicfevtModuleRt_SIC_4G_LTE_A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4G_LTE_A = _HpnicfevtModuleRt_SIC_4G_LTE_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 394)
)
_HpnicfevtModuleRt_SIC_4G_LTE_G_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4G_LTE_G = _HpnicfevtModuleRt_SIC_4G_LTE_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 395)
)
_HpnicfevtModuleRt_SIC_2SAE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_2SAE = _HpnicfevtModuleRt_SIC_2SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 396)
)
_HpnicfevtModuleRt_SIC_4SAE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4SAE = _HpnicfevtModuleRt_SIC_4SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 397)
)
_HpnicfevtModuleRt_HMIM_OAP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_OAP = _HpnicfevtModuleRt_HMIM_OAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 398)
)
_HpnicfevtModuleRt_HMIM_8GSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_8GSW = _HpnicfevtModuleRt_HMIM_8GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 399)
)
_HpnicfevtModuleRt_IPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_IPU = _HpnicfevtModuleRt_IPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 400)
)
_HpnicfevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MIM2GEBE_PCIE = _HpnicfevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 401)
)
_HpnicfevtModuleRt_HIM12GE_PCIE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HIM12GE_PCIE = _HpnicfevtModuleRt_HIM12GE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 402)
)
_HpnicfevtModuleRt_HIM2XGE_PCIE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HIM2XGE_PCIE = _HpnicfevtModuleRt_HIM2XGE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 403)
)
_HpnicfevtModuleRt_IPU_T1000_M_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_IPU_T1000_M = _HpnicfevtModuleRt_IPU_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 404)
)
_HpnicfevtModuleRt_IPU_GX4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_IPU_GX4C = _HpnicfevtModuleRt_IPU_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 405)
)
_HpnicfevtModuleRt_IPU_GT4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_IPU_GT4C = _HpnicfevtModuleRt_IPU_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 406)
)
_HpnicfevtModuleRt_RPU_IAG2000_A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RPU_IAG2000_A = _HpnicfevtModuleRt_RPU_IAG2000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 407)
)
_HpnicfevtModuleRt_RPU_AFD1000_A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RPU_AFD1000_A = _HpnicfevtModuleRt_RPU_AFD1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 408)
)
_HpnicfevtModuleRt_RPU_F5000_A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RPU_F5000_A = _HpnicfevtModuleRt_RPU_F5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 409)
)
_HpnicfevtModuleRt_ACG_8800S3_MPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_ACG_8800S3_MPU = _HpnicfevtModuleRt_ACG_8800S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 410)
)
_HpnicfevtModuleRt_T5000S3_MPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_T5000S3_MPU = _HpnicfevtModuleRt_T5000S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 411)
)
_HpnicfevtModuleRt_NS21S2MSPB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NS21S2MSPB0 = _HpnicfevtModuleRt_NS21S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 412)
)
_HpnicfevtModuleRt_NS11S2MSPB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NS11S2MSPB0 = _HpnicfevtModuleRt_NS11S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 413)
)
_HpnicfevtModuleRt_NSQ1WLAN_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1WLAN = _HpnicfevtModuleRt_NSQ1WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 414)
)
_HpnicfevtModuleRt_NSQ1GP4U0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1GP4U0 = _HpnicfevtModuleRt_NSQ1GP4U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 415)
)
_HpnicfevtModuleRt_NSQ1GP8C40_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1GP8C40 = _HpnicfevtModuleRt_NSQ1GP8C40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 416)
)
_HpnicfevtModuleRt_NSQ1XS2U0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1XS2U0 = _HpnicfevtModuleRt_NSQ1XS2U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 417)
)
_HpnicfevtModuleRt_NSQ1G24XS60_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1G24XS60 = _HpnicfevtModuleRt_NSQ1G24XS60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 418)
)
_HpnicfevtModuleRt_NSQ1TGX4EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1TGX4EA0 = _HpnicfevtModuleRt_NSQ1TGX4EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 419)
)
_HpnicfevtModuleRt_NSQ1FAB08D0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1FAB08D0 = _HpnicfevtModuleRt_NSQ1FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 420)
)
_HpnicfevtModuleRt_NSQ1TGS32SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1TGS32SF0 = _HpnicfevtModuleRt_NSQ1TGS32SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 421)
)
_HpnicfevtModuleRt_NSQ1QGS4SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1QGS4SF0 = _HpnicfevtModuleRt_NSQ1QGS4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 422)
)
_HpnicfevtModuleRt_NSQ1GP24TXEA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1GP24TXEA0 = _HpnicfevtModuleRt_NSQ1GP24TXEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 423)
)
_HpnicfevtModuleRt_NSQ1GP48EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1GP48EB0 = _HpnicfevtModuleRt_NSQ1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 424)
)
_HpnicfevtModuleRt_NSQ1FWCEA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1FWCEA0 = _HpnicfevtModuleRt_NSQ1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 425)
)
_HpnicfevtModuleRt_NSQ1GT48EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1GT48EA0 = _HpnicfevtModuleRt_NSQ1GT48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 426)
)
_HpnicfevtModuleRt_NSQ1TGS8EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1TGS8EA0 = _HpnicfevtModuleRt_NSQ1TGS8EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 427)
)
_HpnicfevtModuleRt_NSQ1FAB04B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1FAB04B0 = _HpnicfevtModuleRt_NSQ1FAB04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 428)
)
_HpnicfevtModuleRt_NSQ1FAB12D0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1FAB12D0 = _HpnicfevtModuleRt_NSQ1FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 429)
)
_HpnicfevtModuleRt_NSQ1SUPB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1SUPB0 = _HpnicfevtModuleRt_NSQ1SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 430)
)
_HpnicfevtModuleRt_VFW1000_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VFW1000 = _HpnicfevtModuleRt_VFW1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 431)
)
_HpnicfevtModuleRt_NSQ1CGC2SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_NSQ1CGC2SE0 = _HpnicfevtModuleRt_NSQ1CGC2SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 432)
)
_HpnicfevtModuleRt_VLB1000_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VLB1000 = _HpnicfevtModuleRt_VLB1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 433)
)
_HpnicfevtModuleRt_VG_8fxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_8fxs = _HpnicfevtModuleRt_VG_8fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 600)
)
_HpnicfevtModuleRt_VG_24fxs_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_24fxs = _HpnicfevtModuleRt_VG_24fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 601)
)
_HpnicfevtModuleRt_VG_24fxs24fxo_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_24fxs24fxo = _HpnicfevtModuleRt_VG_24fxs24fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 602)
)
_HpnicfevtModuleRt_VG_MPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VG_MPU = _HpnicfevtModuleRt_VG_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 603)
)
_HpnicfevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MIM_VCX_CONNECT_P_3C = _HpnicfevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 604)
)
_HpnicfevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MIM_VCX_CONNECT_S_3C = _HpnicfevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 605)
)
_HpnicfevtModuleRt_MIM_VCX_3C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_MIM_VCX_3C = _HpnicfevtModuleRt_MIM_VCX_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 606)
)
_HpnicfevtModuleRt_VNIC_VMXNET3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VNIC_VMXNET3 = _HpnicfevtModuleRt_VNIC_VMXNET3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 607)
)
_HpnicfevtModuleRt_VNIC_E1000_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VNIC_E1000 = _HpnicfevtModuleRt_VNIC_E1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 608)
)
_HpnicfevtModuleRt_VNIC_VIRTIO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VNIC_VIRTIO = _HpnicfevtModuleRt_VNIC_VIRTIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 609)
)
_HpnicfevtModuleRt_VNIC_RTL8139_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VNIC_RTL8139 = _HpnicfevtModuleRt_VNIC_RTL8139_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 610)
)
_HpnicfevtModuleRt_VNIC_IXGBEVF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_VNIC_IXGBEVF = _HpnicfevtModuleRt_VNIC_IXGBEVF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 611)
)
_HpnicfevtModuleRt_SIC_4GSW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4GSW = _HpnicfevtModuleRt_SIC_4GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 800)
)
_HpnicfevtModuleRt_SIC_4GSWP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4GSWP = _HpnicfevtModuleRt_SIC_4GSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 801)
)
_HpnicfevtModuleRt_SIC_1GEC_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_1GEC_V2 = _HpnicfevtModuleRt_SIC_1GEC_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 802)
)
_HpnicfevtModuleRt_4G_LTE_ATT_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_4G_LTE_ATT = _HpnicfevtModuleRt_4G_LTE_ATT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 803)
)
_HpnicfevtModuleRt_4G_TD_LTE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_4G_TD_LTE = _HpnicfevtModuleRt_4G_TD_LTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 804)
)
_HpnicfevtModuleRt_FIP_240_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_FIP_240 = _HpnicfevtModuleRt_FIP_240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 805)
)
_HpnicfevtModuleRt_8GBP_V2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_8GBP_V2 = _HpnicfevtModuleRt_8GBP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 806)
)
_HpnicfevtModuleRt_HMIM_CNDE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_HMIM_CNDE = _HpnicfevtModuleRt_HMIM_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 807)
)
_HpnicfevtModuleRt_4G_LTE_Mobile_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_4G_LTE_Mobile = _HpnicfevtModuleRt_4G_LTE_Mobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 808)
)
_HpnicfevtModuleRt_SIC_4G_LTE_M_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SIC_4G_LTE_M = _HpnicfevtModuleRt_SIC_4G_LTE_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 809)
)
_HpnicfevtModuleRt_CRSE_X3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CRSE_X3 = _HpnicfevtModuleRt_CRSE_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 810)
)
_HpnicfevtModuleRt_CFIP_300_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CFIP_300 = _HpnicfevtModuleRt_CFIP_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 811)
)
_HpnicfevtModuleRt_CFIP_310_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CFIP_310 = _HpnicfevtModuleRt_CFIP_310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 812)
)
_HpnicfevtModuleRt_CSAP_4EXP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CSAP_4EXP = _HpnicfevtModuleRt_CSAP_4EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 813)
)
_HpnicfevtModuleRt_RSU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RSU = _HpnicfevtModuleRt_RSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 814)
)
_HpnicfevtModuleRt_CFIP_610_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CFIP_610 = _HpnicfevtModuleRt_CFIP_610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 815)
)
_HpnicfevtModuleRt_2EXP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_2EXP = _HpnicfevtModuleRt_2EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 816)
)
_HpnicfevtModuleRt_16GBP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_16GBP = _HpnicfevtModuleRt_16GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 817)
)
_HpnicfevtModuleRt_CFIP_240_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CFIP_240 = _HpnicfevtModuleRt_CFIP_240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 818)
)
_HpnicfevtModuleRt_RSE_X3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RSE_X3 = _HpnicfevtModuleRt_RSE_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 819)
)
_HpnicfevtModuleRt_SAP_8EXP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_8EXP = _HpnicfevtModuleRt_SAP_8EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 820)
)
_HpnicfevtModuleRt_SAP_16EXP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_16EXP = _HpnicfevtModuleRt_SAP_16EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 821)
)
_HpnicfevtModuleRt_PU1P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_PU1P = _HpnicfevtModuleRt_PU1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 822)
)
_HpnicfevtModuleRt_RSU100_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_RSU100 = _HpnicfevtModuleRt_RSU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 823)
)
_HpnicfevtModuleRt_SAP_2QGP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_SAP_2QGP = _HpnicfevtModuleRt_SAP_2QGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 824)
)
_HpnicfevtModuleRt_CSFE_X1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleRt_CSFE_X1 = _HpnicfevtModuleRt_CSFE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 825)
)
_HpevtModuleRt_SIC_EPRI_ObjectIdentity = ObjectIdentity
hpevtModuleRt_SIC_EPRI = _HpevtModuleRt_SIC_EPRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5000)
)
_HpevtModuleRt_MIM_1E1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_V2 = _HpevtModuleRt_MIM_1E1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5001)
)
_HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_F_V2 = _HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5002)
)
_HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_2E1_F_V2 = _HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5003)
)
_HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_4E1_F_V2 = _HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5004)
)
_HpevtModuleRt_MIM_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75 = _HpevtModuleRt_MIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5005)
)
_HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75_F = _HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5006)
)
_HpevtModuleRt_MIM_8T1_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1 = _HpevtModuleRt_MIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5007)
)
_HpevtModuleRt_MIM_8T1_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1_F = _HpevtModuleRt_MIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5008)
)
_HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_IMA_8E1_75 = _HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5009)
)
_HpevtModuleRt_FIC_2E1_V3_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_2E1_V3 = _HpevtModuleRt_FIC_2E1_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5010)
)
_HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_IMA_8T1_V2 = _HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 3, 5011)
)
_HpnicfevtModuleSwitchType_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSwitchType = _HpnicfevtModuleSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4)
)
_HpnicfevtModuleSw_10OR100M_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_10OR100M = _HpnicfevtModuleSw_10OR100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1)
)
_HpnicfevtModuleSw_1000BASE_LX_SM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_LX_SM = _HpnicfevtModuleSw_1000BASE_LX_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 2)
)
_HpnicfevtModuleSw_1000BASE_SX_MM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_SX_MM = _HpnicfevtModuleSw_1000BASE_SX_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 3)
)
_HpnicfevtModuleSw_1000BASE_TX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_TX = _HpnicfevtModuleSw_1000BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 4)
)
_HpnicfevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_SINGLEMODE_FX = _HpnicfevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 5)
)
_HpnicfevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_MULTIMODE_FX = _HpnicfevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 6)
)
_HpnicfevtModuleSw_100M_100BASE_TX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_100BASE_TX = _HpnicfevtModuleSw_100M_100BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 7)
)
_HpnicfevtModuleSw_100M_HUB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_HUB = _HpnicfevtModuleSw_100M_HUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 8)
)
_HpnicfevtModuleSw_VDSL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_VDSL = _HpnicfevtModuleSw_VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 9)
)
_HpnicfevtModuleSw_STACK_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_STACK = _HpnicfevtModuleSw_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 10)
)
_HpnicfevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_ZENITH_FX = _HpnicfevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 11)
)
_HpnicfevtModuleSw_1000BASE_LONG_FX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_LONG_FX = _HpnicfevtModuleSw_1000BASE_LONG_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 12)
)
_HpnicfevtModuleSw_ADSL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_ADSL = _HpnicfevtModuleSw_ADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 13)
)
_HpnicfevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_4T10OR100_4FX100SM = _HpnicfevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 14)
)
_HpnicfevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_4T10OR100_4FX100MM = _HpnicfevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 15)
)
_HpnicfevtModuleSw_VSPL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_VSPL = _HpnicfevtModuleSw_VSPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 16)
)
_HpnicfevtModuleSw_ASPL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_ASPL = _HpnicfevtModuleSw_ASPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 17)
)
_HpnicfevtModuleSw_1000M_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000M_SFP = _HpnicfevtModuleSw_1000M_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 18)
)
_HpnicfevtModuleSw_LS82O2CM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82O2CM = _HpnicfevtModuleSw_LS82O2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 19)
)
_HpnicfevtModuleSw_LS82P2CM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82P2CM = _HpnicfevtModuleSw_LS82P2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 20)
)
_HpnicfevtModuleSw_LS82O4GM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82O4GM = _HpnicfevtModuleSw_LS82O4GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 21)
)
_HpnicfevtModuleSw_LS82GB4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82GB4C = _HpnicfevtModuleSw_LS82GB4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 22)
)
_HpnicfevtModuleSw_LS82GT4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82GT4C = _HpnicfevtModuleSw_LS82GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 23)
)
_HpnicfevtModuleSw_LS82ST4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82ST4C = _HpnicfevtModuleSw_LS82ST4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 24)
)
_HpnicfevtModuleSw_BOARD_LS82DSPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS82DSPU = _HpnicfevtModuleSw_BOARD_LS82DSPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 25)
)
_HpnicfevtModuleSw_BOARD_LS81GP8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS81GP8U = _HpnicfevtModuleSw_BOARD_LS81GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 26)
)
_HpnicfevtModuleSw_BOARD_LS82GT20_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS82GT20 = _HpnicfevtModuleSw_BOARD_LS82GT20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 27)
)
_HpnicfevtModuleSw_BOARD_LS82FE48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS82FE48 = _HpnicfevtModuleSw_BOARD_LS82FE48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 28)
)
_HpnicfevtModuleSw_LS82T24B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82T24B = _HpnicfevtModuleSw_LS82T24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 29)
)
_HpnicfevtModuleSw_LSB1SRPA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRPA = _HpnicfevtModuleSw_LSB1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 30)
)
_HpnicfevtModuleSw_LSB1FT48A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FT48A = _HpnicfevtModuleSw_LSB1FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 31)
)
_HpnicfevtModuleSw_LSB1FT48B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FT48B = _HpnicfevtModuleSw_LSB1FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 32)
)
_HpnicfevtModuleSw_LSB1F48GA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1F48GA = _HpnicfevtModuleSw_LSB1F48GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 33)
)
_HpnicfevtModuleSw_LSB1F48GB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1F48GB = _HpnicfevtModuleSw_LSB1F48GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 34)
)
_HpnicfevtModuleSw_LSB1FP20A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FP20A = _HpnicfevtModuleSw_LSB1FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 35)
)
_HpnicfevtModuleSw_LSB1FP20B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FP20B = _HpnicfevtModuleSw_LSB1FP20B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 36)
)
_HpnicfevtModuleSw_FT48A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_FT48A = _HpnicfevtModuleSw_FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 37)
)
_HpnicfevtModuleSw_GP4U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GP4U = _HpnicfevtModuleSw_GP4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 38)
)
_HpnicfevtModuleSw_GP2U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GP2U = _HpnicfevtModuleSw_GP2U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 39)
)
_HpnicfevtModuleSw_TGX1A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_TGX1A = _HpnicfevtModuleSw_TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 40)
)
_HpnicfevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_LX_SM_IR_SC = _HpnicfevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 41)
)
_HpnicfevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_SX_MM_SR_SC = _HpnicfevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 42)
)
_HpnicfevtModuleSw_1000BASE_T_RJ45_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_T_RJ45 = _HpnicfevtModuleSw_1000BASE_T_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 43)
)
_HpnicfevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100BASE_FX_SM_IR_SC = _HpnicfevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 44)
)
_HpnicfevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100BASE_FX_MM_SR_SC = _HpnicfevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 45)
)
_HpnicfevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GIGA_STACK_1M_PC = _HpnicfevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 46)
)
_HpnicfevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_LX_SM_VLR_LC = _HpnicfevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 47)
)
_HpnicfevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_LX_SM_LR_LC = _HpnicfevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 48)
)
_HpnicfevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100BASE_FX_SM_LR_SC = _HpnicfevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 49)
)
_HpnicfevtModuleSw_1000BASE_X_GBIC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_X_GBIC = _HpnicfevtModuleSw_1000BASE_X_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 50)
)
_HpnicfevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_SINGLEMODE_FX_LC = _HpnicfevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 51)
)
_HpnicfevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_MULTIMODE_FX_LC = _HpnicfevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 52)
)
_HpnicfevtModuleSw_1000BASE_4SFP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_4SFP = _HpnicfevtModuleSw_1000BASE_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 53)
)
_HpnicfevtModuleSw_1000BASE_4GBIC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_4GBIC = _HpnicfevtModuleSw_1000BASE_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 54)
)
_HpnicfevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_FIXED_4SFP = _HpnicfevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 55)
)
_HpnicfevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_FIXED_4GBIC = _HpnicfevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 56)
)
_HpnicfevtModuleSw_LSB1GP12A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP12A = _HpnicfevtModuleSw_LSB1GP12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 57)
)
_HpnicfevtModuleSw_LSB1GP12B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP12B = _HpnicfevtModuleSw_LSB1GP12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 58)
)
_HpnicfevtModuleSw_LSB1TGX1A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1TGX1A = _HpnicfevtModuleSw_LSB1TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 59)
)
_HpnicfevtModuleSw_LSB1TGX1B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1TGX1B = _HpnicfevtModuleSw_LSB1TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 60)
)
_HpnicfevtModuleSw_LSB1P4G8A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1P4G8A = _HpnicfevtModuleSw_LSB1P4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 61)
)
_HpnicfevtModuleSw_LSB1P4G8B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1P4G8B = _HpnicfevtModuleSw_LSB1P4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 62)
)
_HpnicfevtModuleSw_LSB1A4G8A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1A4G8A = _HpnicfevtModuleSw_LSB1A4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 63)
)
_HpnicfevtModuleSw_LSB1A4G8B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1A4G8B = _HpnicfevtModuleSw_LSB1A4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 64)
)
_HpnicfevtModuleSw_FT48C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_FT48C = _HpnicfevtModuleSw_FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 65)
)
_HpnicfevtModuleSw_FP20_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_FP20 = _HpnicfevtModuleSw_FP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 66)
)
_HpnicfevtModuleSw_BOARD_LS81FT48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS81FT48 = _HpnicfevtModuleSw_BOARD_LS81FT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 67)
)
_HpnicfevtModuleSw_BOARD_LS81GB8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS81GB8U = _HpnicfevtModuleSw_BOARD_LS81GB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 68)
)
_HpnicfevtModuleSw_BOARD_LS81GT8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS81GT8U = _HpnicfevtModuleSw_BOARD_LS81GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 69)
)
_HpnicfevtModuleSw_BOARD_LS81FS24_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS81FS24 = _HpnicfevtModuleSw_BOARD_LS81FS24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 70)
)
_HpnicfevtModuleSw_BOARD_LS81FM24_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS81FM24 = _HpnicfevtModuleSw_BOARD_LS81FM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 71)
)
_HpnicfevtModuleSw_BOARD_LS82GP20_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS82GP20 = _HpnicfevtModuleSw_BOARD_LS82GP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 72)
)
_HpnicfevtModuleSw_LSB1SRPB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRPB = _HpnicfevtModuleSw_LSB1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 73)
)
_HpnicfevtModuleSw_LSB1F32GA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1F32GA = _HpnicfevtModuleSw_LSB1F32GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 74)
)
_HpnicfevtModuleSw_LSB1F32GB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1F32GB = _HpnicfevtModuleSw_LSB1F32GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 75)
)
_HpnicfevtModuleSw_LSB2FT48A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2FT48A = _HpnicfevtModuleSw_LSB2FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 76)
)
_HpnicfevtModuleSw_LSB2FT48B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2FT48B = _HpnicfevtModuleSw_LSB2FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 77)
)
_HpnicfevtModuleSw_LSB1GT12A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT12A = _HpnicfevtModuleSw_LSB1GT12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 78)
)
_HpnicfevtModuleSw_LSB1GT12B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT12B = _HpnicfevtModuleSw_LSB1GT12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 79)
)
_HpnicfevtModuleSw_PC4U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PC4U = _HpnicfevtModuleSw_PC4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 80)
)
_HpnicfevtModuleSw_FT32A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_FT32A = _HpnicfevtModuleSw_FT32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 81)
)
_HpnicfevtModuleSw_GT4U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GT4U = _HpnicfevtModuleSw_GT4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 82)
)
_HpnicfevtModuleSw_BOARD_LS83FP20A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS83FP20A = _HpnicfevtModuleSw_BOARD_LS83FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 83)
)
_HpnicfevtModuleSw_BOARD_LS82HGMU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS82HGMU = _HpnicfevtModuleSw_BOARD_LS82HGMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 84)
)
_HpnicfevtModuleSw_LSB1GP8TB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP8TB = _HpnicfevtModuleSw_LSB1GP8TB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 85)
)
_HpnicfevtModuleSw_LSB1GP8TC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP8TC = _HpnicfevtModuleSw_LSB1GP8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 86)
)
_HpnicfevtModuleSw_LSB1GT8PB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT8PB = _HpnicfevtModuleSw_LSB1GT8PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 87)
)
_HpnicfevtModuleSw_LSB1GT8PC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT8PC = _HpnicfevtModuleSw_LSB1GT8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 88)
)
_HpnicfevtModuleSw_LSB1FT48C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FT48C = _HpnicfevtModuleSw_LSB1FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 89)
)
_HpnicfevtModuleSw_LSB1FP20C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FP20C = _HpnicfevtModuleSw_LSB1FP20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 90)
)
_HpnicfevtModuleSw_LSB1F32GC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1F32GC = _HpnicfevtModuleSw_LSB1F32GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 91)
)
_HpnicfevtModuleSw_LSB1GT12C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT12C = _HpnicfevtModuleSw_LSB1GT12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 92)
)
_HpnicfevtModuleSw_LSB1GP12C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP12C = _HpnicfevtModuleSw_LSB1GP12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 93)
)
_HpnicfevtModuleSw_LSB1P4G8C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1P4G8C = _HpnicfevtModuleSw_LSB1P4G8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 94)
)
_HpnicfevtModuleSw_LSB1TGX1C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1TGX1C = _HpnicfevtModuleSw_LSB1TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 95)
)
_HpnicfevtModuleSw_LSB1GT24B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT24B = _HpnicfevtModuleSw_LSB1GT24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 96)
)
_HpnicfevtModuleSw_LSB1GT24C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT24C = _HpnicfevtModuleSw_LSB1GT24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 97)
)
_HpnicfevtModuleSw_LSB1GP24B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP24B = _HpnicfevtModuleSw_LSB1GP24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 98)
)
_HpnicfevtModuleSw_LSB1GP24C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP24C = _HpnicfevtModuleSw_LSB1GP24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 99)
)
_HpnicfevtModuleSw_LSB1XP2B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP2B = _HpnicfevtModuleSw_LSB1XP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 100)
)
_HpnicfevtModuleSw_LSB1XP2C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP2C = _HpnicfevtModuleSw_LSB1XP2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 101)
)
_HpnicfevtModuleSw_LSB1GV48B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GV48B = _HpnicfevtModuleSw_LSB1GV48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 102)
)
_HpnicfevtModuleSw_LSB1GV48C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GV48C = _HpnicfevtModuleSw_LSB1GV48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 103)
)
_HpnicfevtModuleSw_LSB1SRPC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRPC = _HpnicfevtModuleSw_LSB1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 104)
)
_HpnicfevtModuleSw_LSB1SRP1N0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N0 = _HpnicfevtModuleSw_LSB1SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 105)
)
_HpnicfevtModuleSw_LSB1SRP1N1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N1 = _HpnicfevtModuleSw_LSB1SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 106)
)
_HpnicfevtModuleSw_LSB1SRP1N2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N2 = _HpnicfevtModuleSw_LSB1SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 107)
)
_HpnicfevtModuleSw_GT24_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GT24 = _HpnicfevtModuleSw_GT24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 108)
)
_HpnicfevtModuleSw_GP24_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GP24 = _HpnicfevtModuleSw_GP24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 109)
)
_HpnicfevtModuleSw_XP2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_XP2 = _HpnicfevtModuleSw_XP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 110)
)
_HpnicfevtModuleSw_GV48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GV48 = _HpnicfevtModuleSw_GV48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 111)
)
_HpnicfevtModuleSw_LSG1GP8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSG1GP8U = _HpnicfevtModuleSw_LSG1GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 112)
)
_HpnicfevtModuleSw_LSG1GT8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSG1GT8U = _HpnicfevtModuleSw_LSG1GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 113)
)
_HpnicfevtModuleSw_LSG1TG1U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSG1TG1U = _HpnicfevtModuleSw_LSG1TG1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 114)
)
_HpnicfevtModuleSw_LSG1TD1U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSG1TD1U = _HpnicfevtModuleSw_LSG1TD1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 115)
)
_HpnicfevtModuleSw_LSB2FT48C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2FT48C = _HpnicfevtModuleSw_LSB2FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 116)
)
_HpnicfevtModuleSw_LSB1GT48B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT48B = _HpnicfevtModuleSw_LSB1GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 117)
)
_HpnicfevtModuleSw_LSB1GT48C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT48C = _HpnicfevtModuleSw_LSB1GT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 118)
)
_HpnicfevtModuleSw_LS81GT48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GT48 = _HpnicfevtModuleSw_LS81GT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 119)
)
_HpnicfevtModuleSw_LS81SRPG0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG0 = _HpnicfevtModuleSw_LS81SRPG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 120)
)
_HpnicfevtModuleSw_LS81SRPG1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG1 = _HpnicfevtModuleSw_LS81SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 121)
)
_HpnicfevtModuleSw_LS81SRPG2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG2 = _HpnicfevtModuleSw_LS81SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 122)
)
_HpnicfevtModuleSw_LS81SRPG3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG3 = _HpnicfevtModuleSw_LS81SRPG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 123)
)
_HpnicfevtModuleSw_SR01SRPUB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUB = _HpnicfevtModuleSw_SR01SRPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 125)
)
_HpnicfevtModuleSw_SR01SRPUA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUA = _HpnicfevtModuleSw_SR01SRPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 126)
)
_HpnicfevtModuleSw_SR01GP12L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GP12L = _HpnicfevtModuleSw_SR01GP12L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 127)
)
_HpnicfevtModuleSw_SR01GP12W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GP12W = _HpnicfevtModuleSw_SR01GP12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 128)
)
_HpnicfevtModuleSw_SR01FT48L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01FT48L = _HpnicfevtModuleSw_SR01FT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 129)
)
_HpnicfevtModuleSw_SR01FT48W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01FT48W = _HpnicfevtModuleSw_SR01FT48W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 130)
)
_HpnicfevtModuleSw_SR01XK1W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XK1W = _HpnicfevtModuleSw_SR01XK1W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 131)
)
_HpnicfevtModuleSw_SR01FP20W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01FP20W = _HpnicfevtModuleSw_SR01FP20W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 132)
)
_HpnicfevtModuleSw_SR01GT12W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT12W = _HpnicfevtModuleSw_SR01GT12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 133)
)
_HpnicfevtModuleSw_SR01F32GL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01F32GL = _HpnicfevtModuleSw_SR01F32GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 134)
)
_HpnicfevtModuleSw_SR01F32GW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01F32GW = _HpnicfevtModuleSw_SR01F32GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 135)
)
_HpnicfevtModuleSw_SR01GT8PL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT8PL = _HpnicfevtModuleSw_SR01GT8PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 136)
)
_HpnicfevtModuleSw_SR01GT8PW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT8PW = _HpnicfevtModuleSw_SR01GT8PW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 137)
)
_HpnicfevtModuleSw_SR01P4G8W_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01P4G8W = _HpnicfevtModuleSw_SR01P4G8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 138)
)
_HpnicfevtModuleSw_LSA1FP8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSA1FP8U = _HpnicfevtModuleSw_LSA1FP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 139)
)
_HpnicfevtModuleSw_LSB1SP4B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SP4B = _HpnicfevtModuleSw_LSB1SP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 140)
)
_HpnicfevtModuleSw_LSB1SP4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SP4C = _HpnicfevtModuleSw_LSB1SP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 141)
)
_HpnicfevtModuleSw_LSB1UP1B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1UP1B = _HpnicfevtModuleSw_LSB1UP1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 142)
)
_HpnicfevtModuleSw_LSB1UP1C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1UP1C = _HpnicfevtModuleSw_LSB1UP1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 143)
)
_HpnicfevtModuleSw_LSB1XP4B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4B = _HpnicfevtModuleSw_LSB1XP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 144)
)
_HpnicfevtModuleSw_LSB1XP4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4C = _HpnicfevtModuleSw_LSB1XP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 145)
)
_HpnicfevtModuleSw_SP4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SP4 = _HpnicfevtModuleSw_SP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 146)
)
_HpnicfevtModuleSw_UP1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_UP1 = _HpnicfevtModuleSw_UP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 147)
)
_HpnicfevtModuleSw_XP4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_XP4 = _HpnicfevtModuleSw_XP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 148)
)
_HpnicfevtModuleSw_LS81VSNP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81VSNP = _HpnicfevtModuleSw_LS81VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 149)
)
_HpnicfevtModuleSw_LS81T12P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81T12P = _HpnicfevtModuleSw_LS81T12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 150)
)
_HpnicfevtModuleSw_LS81P12T_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81P12T = _HpnicfevtModuleSw_LS81P12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 151)
)
_HpnicfevtModuleSw_LS81GP8UB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP8UB = _HpnicfevtModuleSw_LS81GP8UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 152)
)
_HpnicfevtModuleSw_LS81FT48E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81FT48E = _HpnicfevtModuleSw_LS81FT48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 153)
)
_HpnicfevtModuleSw_LS81GP4UB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP4UB = _HpnicfevtModuleSw_LS81GP4UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 154)
)
_HpnicfevtModuleSw_LS81GT8UE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GT8UE = _HpnicfevtModuleSw_LS81GT8UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 155)
)
_HpnicfevtModuleSw_LS81GT48A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GT48A = _HpnicfevtModuleSw_LS81GT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 156)
)
_HpnicfevtModuleSw_LS81FP48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81FP48 = _HpnicfevtModuleSw_LS81FP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 157)
)
_HpnicfevtModuleSw_LSB1XK1B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XK1B = _HpnicfevtModuleSw_LSB1XK1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 158)
)
_HpnicfevtModuleSw_LSB1XK1C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XK1C = _HpnicfevtModuleSw_LSB1XK1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 159)
)
_HpnicfevtModuleSw_SR01SRPUC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUC = _HpnicfevtModuleSw_SR01SRPUC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 160)
)
_HpnicfevtModuleSw_SR01SRPUD_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUD = _HpnicfevtModuleSw_SR01SRPUD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 161)
)
_HpnicfevtModuleSw_SR01SRPUE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUE = _HpnicfevtModuleSw_SR01SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 162)
)
_HpnicfevtModuleSw_LSB1SRP1N3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N3 = _HpnicfevtModuleSw_LSB1SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 163)
)
_HpnicfevtModuleSw_LSB1VP2B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1VP2B = _HpnicfevtModuleSw_LSB1VP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 164)
)
_HpnicfevtModuleSw_LSB1NATB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1NATB = _HpnicfevtModuleSw_LSB1NATB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 165)
)
_HpnicfevtModuleSw_LSB1VPNB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1VPNB = _HpnicfevtModuleSw_LSB1VPNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 166)
)
_HpnicfevtModuleSw_LSGP8P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSGP8P = _HpnicfevtModuleSw_LSGP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 167)
)
_HpnicfevtModuleSw_LSXK1P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXK1P = _HpnicfevtModuleSw_LSXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 168)
)
_HpnicfevtModuleSw_LSXP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXP2P = _HpnicfevtModuleSw_LSXP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 169)
)
_HpnicfevtModuleSw_LS81FT48F_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81FT48F = _HpnicfevtModuleSw_LS81FT48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 170)
)
_HpnicfevtModuleSw_LS81PT8G_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81PT8G = _HpnicfevtModuleSw_LS81PT8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 171)
)
_HpnicfevtModuleSw_LS81PT4G_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81PT4G = _HpnicfevtModuleSw_LS81PT4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 172)
)
_HpnicfevtModuleSw_LSSTK24G_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSSTK24G = _HpnicfevtModuleSw_LSSTK24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 173)
)
_HpnicfevtModuleSw_LS82GT20A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82GT20A = _HpnicfevtModuleSw_LS82GT20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 174)
)
_HpnicfevtModuleSw_LS82GP20A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82GP20A = _HpnicfevtModuleSw_LS82GP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 175)
)
_HpnicfevtModuleSw_LS81TGX1C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81TGX1C = _HpnicfevtModuleSw_LS81TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 176)
)
_HpnicfevtModuleSw_VP2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_VP2 = _HpnicfevtModuleSw_VP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 177)
)
_HpnicfevtModuleSw_LSA1FB8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSA1FB8U = _HpnicfevtModuleSw_LSA1FB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 178)
)
_HpnicfevtModuleSw_LS81T12PE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81T12PE = _HpnicfevtModuleSw_LS81T12PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 179)
)
_HpnicfevtModuleSw_LS81P12TE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81P12TE = _HpnicfevtModuleSw_LS81P12TE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 180)
)
_HpnicfevtModuleSw_LSB1SRP2N0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N0 = _HpnicfevtModuleSw_LSB1SRP2N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 181)
)
_HpnicfevtModuleSw_LSB1SRP2N3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N3 = _HpnicfevtModuleSw_LSB1SRP2N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 182)
)
_HpnicfevtModuleSw_LSB1GV48DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GV48DB = _HpnicfevtModuleSw_LSB1GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 183)
)
_HpnicfevtModuleSw_LSB1FW8B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FW8B = _HpnicfevtModuleSw_LSB1FW8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 184)
)
_HpnicfevtModuleSw_LSB1IPSEC8B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1IPSEC8B = _HpnicfevtModuleSw_LSB1IPSEC8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 185)
)
_HpnicfevtModuleSw_LSB1IDSB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1IDSB = _HpnicfevtModuleSw_LSB1IDSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 186)
)
_HpnicfevtModuleSw_LSB1IPSB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1IPSB = _HpnicfevtModuleSw_LSB1IPSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 187)
)
_HpnicfevtModuleSw_LSB2FT48CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2FT48CA = _HpnicfevtModuleSw_LSB2FT48CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 188)
)
_HpnicfevtModuleSw_LSB1FP20CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FP20CA = _HpnicfevtModuleSw_LSB1FP20CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 189)
)
_HpnicfevtModuleSw_LSB1F32GCA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1F32GCA = _HpnicfevtModuleSw_LSB1F32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 190)
)
_HpnicfevtModuleSw_LSB1P4G8CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1P4G8CA = _HpnicfevtModuleSw_LSB1P4G8CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 191)
)
_HpnicfevtModuleSw_LSB1GT12CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT12CA = _HpnicfevtModuleSw_LSB1GT12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 192)
)
_HpnicfevtModuleSw_LSB1GT24CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT24CA = _HpnicfevtModuleSw_LSB1GT24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 193)
)
_HpnicfevtModuleSw_LSB1GP12CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP12CA = _HpnicfevtModuleSw_LSB1GP12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 194)
)
_HpnicfevtModuleSw_LSB1GP24CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP24CA = _HpnicfevtModuleSw_LSB1GP24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 195)
)
_HpnicfevtModuleSw_LSB1GT8PCA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT8PCA = _HpnicfevtModuleSw_LSB1GT8PCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 196)
)
_HpnicfevtModuleSw_LSB1XP2CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP2CA = _HpnicfevtModuleSw_LSB1XP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 197)
)
_HpnicfevtModuleSw_LSB1XK1CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XK1CA = _HpnicfevtModuleSw_LSB1XK1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 198)
)
_HpnicfevtModuleSw_LSB1XP4CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4CA = _HpnicfevtModuleSw_LSB1XP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 199)
)
_HpnicfevtModuleSw_LSB1UP1CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1UP1CA = _HpnicfevtModuleSw_LSB1UP1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 200)
)
_HpnicfevtModuleSw_LSB1SP4CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SP4CA = _HpnicfevtModuleSw_LSB1SP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 201)
)
_HpnicfevtModuleSw_LSB1VP2CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1VP2CA = _HpnicfevtModuleSw_LSB1VP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 202)
)
_HpnicfevtModuleSw_SR01FT48WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01FT48WA = _HpnicfevtModuleSw_SR01FT48WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 203)
)
_HpnicfevtModuleSw_SR01FP20WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01FP20WA = _HpnicfevtModuleSw_SR01FP20WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 204)
)
_HpnicfevtModuleSw_SR01F32GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01F32GWA = _HpnicfevtModuleSw_SR01F32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 205)
)
_HpnicfevtModuleSw_SR01P4G8WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01P4G8WA = _HpnicfevtModuleSw_SR01P4G8WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 206)
)
_HpnicfevtModuleSw_SR01GT12WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT12WA = _HpnicfevtModuleSw_SR01GT12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 207)
)
_HpnicfevtModuleSw_SR01GT24WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT24WA = _HpnicfevtModuleSw_SR01GT24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 208)
)
_HpnicfevtModuleSw_SR01GP12WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GP12WA = _HpnicfevtModuleSw_SR01GP12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 209)
)
_HpnicfevtModuleSw_SR01GP24WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GP24WA = _HpnicfevtModuleSw_SR01GP24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 210)
)
_HpnicfevtModuleSw_SR01GT8PWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT8PWA = _HpnicfevtModuleSw_SR01GT8PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 211)
)
_HpnicfevtModuleSw_SR01XP2WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XP2WA = _HpnicfevtModuleSw_SR01XP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 212)
)
_HpnicfevtModuleSw_SR01XK1WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XK1WA = _HpnicfevtModuleSw_SR01XK1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 213)
)
_HpnicfevtModuleSw_SR01UP1WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01UP1WA = _HpnicfevtModuleSw_SR01UP1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 214)
)
_HpnicfevtModuleSw_SR01SP4WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SP4WA = _HpnicfevtModuleSw_SR01SP4WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 215)
)
_HpnicfevtModuleSw_GP8U_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_GP8U = _HpnicfevtModuleSw_GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 216)
)
_HpnicfevtModuleSw_LSEXP1P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSEXP1P = _HpnicfevtModuleSw_LSEXP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 217)
)
_HpnicfevtModuleSw_LSEXK1P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSEXK1P = _HpnicfevtModuleSw_LSEXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 218)
)
_HpnicfevtModuleSw_LSEXS1P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSEXS1P = _HpnicfevtModuleSw_LSEXS1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 219)
)
_HpnicfevtModuleSw_LS81GP48_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP48 = _HpnicfevtModuleSw_LS81GP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 220)
)
_HpnicfevtModuleSw_LS81GT48B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GT48B = _HpnicfevtModuleSw_LS81GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 221)
)
_HpnicfevtModuleSw_LS81T16P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81T16P = _HpnicfevtModuleSw_LS81T16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 222)
)
_HpnicfevtModuleSw_LS81T32P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81T32P = _HpnicfevtModuleSw_LS81T32P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 223)
)
_HpnicfevtModuleSw_LS81TGX2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81TGX2 = _HpnicfevtModuleSw_LS81TGX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 224)
)
_HpnicfevtModuleSw_LS81TGX4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81TGX4 = _HpnicfevtModuleSw_LS81TGX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 225)
)
_HpnicfevtModuleSw_LSB1GV48DA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GV48DA = _HpnicfevtModuleSw_LSB1GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 226)
)
_HpnicfevtModuleSw_SR01GV48VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GV48VB = _HpnicfevtModuleSw_SR01GV48VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 227)
)
_HpnicfevtModuleSw_LSB1GT24DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT24DB = _HpnicfevtModuleSw_LSB1GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 228)
)
_HpnicfevtModuleSw_LSB1GP24DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP24DB = _HpnicfevtModuleSw_LSB1GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 229)
)
_HpnicfevtModuleSw_LSB1GP24DC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP24DC = _HpnicfevtModuleSw_LSB1GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 230)
)
_HpnicfevtModuleSw_LSB1FW8DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FW8DB = _HpnicfevtModuleSw_LSB1FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 231)
)
_HpnicfevtModuleSw_LSB1IPSEC8DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1IPSEC8DB = _HpnicfevtModuleSw_LSB1IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 232)
)
_HpnicfevtModuleSw_SR01GT24VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GT24VB = _HpnicfevtModuleSw_SR01GT24VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 233)
)
_HpnicfevtModuleSw_SR01GP24VC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GP24VC = _HpnicfevtModuleSw_SR01GP24VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 234)
)
_HpnicfevtModuleSw_SR01VP2WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01VP2WA = _HpnicfevtModuleSw_SR01VP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 235)
)
_HpnicfevtModuleSw_SR01FW8VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01FW8VB = _HpnicfevtModuleSw_SR01FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 236)
)
_HpnicfevtModuleSw_SR01IPSEC8VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01IPSEC8VB = _HpnicfevtModuleSw_SR01IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 237)
)
_HpnicfevtModuleSw_SR01NATL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01NATL = _HpnicfevtModuleSw_SR01NATL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 238)
)
_HpnicfevtModuleSw_SR01VPNL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01VPNL = _HpnicfevtModuleSw_SR01VPNL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 239)
)
_HpnicfevtModuleSw_LSB1GP24CB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP24CB = _HpnicfevtModuleSw_LSB1GP24CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 240)
)
_HpnicfevtModuleSw_LSB1GP48DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP48DB = _HpnicfevtModuleSw_LSB1GP48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 241)
)
_HpnicfevtModuleSw_LSB1XP2CB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP2CB = _HpnicfevtModuleSw_LSB1XP2CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 242)
)
_HpnicfevtModuleSw_XP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_XP4L = _HpnicfevtModuleSw_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 243)
)
_HpnicfevtModuleSw_LSB1XP4LDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4LDB = _HpnicfevtModuleSw_LSB1XP4LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 244)
)
_HpnicfevtModuleSw_LSB1XP4LDC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4LDC = _HpnicfevtModuleSw_LSB1XP4LDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 245)
)
_HpnicfevtModuleSw_AHP4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_AHP4 = _HpnicfevtModuleSw_AHP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 246)
)
_HpnicfevtModuleSw_LSB1AHP4GCA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1AHP4GCA = _HpnicfevtModuleSw_LSB1AHP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 247)
)
_HpnicfevtModuleSw_CLP4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CLP4 = _HpnicfevtModuleSw_CLP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 248)
)
_HpnicfevtModuleSw_LSB1CLP4GCA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1CLP4GCA = _HpnicfevtModuleSw_LSB1CLP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 249)
)
_HpnicfevtModuleSw_ET32_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_ET32 = _HpnicfevtModuleSw_ET32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 250)
)
_HpnicfevtModuleSw_LSB1ET32GCA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1ET32GCA = _HpnicfevtModuleSw_LSB1ET32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 251)
)
_HpnicfevtModuleSw_LSB1IDSDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1IDSDB = _HpnicfevtModuleSw_LSB1IDSDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 252)
)
_HpnicfevtModuleSw_LSB1SRP2N1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N1 = _HpnicfevtModuleSw_LSB1SRP2N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 253)
)
_HpnicfevtModuleSw_BOARD_LS82SRPB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BOARD_LS82SRPB = _HpnicfevtModuleSw_BOARD_LS82SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 254)
)
_HpnicfevtModuleSw_BORAD_LS83SRPC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_BORAD_LS83SRPC = _HpnicfevtModuleSw_BORAD_LS83SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 255)
)
_HpnicfevtModuleSw_Main_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_Main = _HpnicfevtModuleSw_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 256)
)
_HpnicfevtModuleSw_LSB1SRP2N2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N2 = _HpnicfevtModuleSw_LSB1SRP2N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 257)
)
_HpnicfevtModuleSw_LSB1NAMB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1NAMB = _HpnicfevtModuleSw_LSB1NAMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 258)
)
_HpnicfevtModuleSw_RSP2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_RSP2 = _HpnicfevtModuleSw_RSP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 259)
)
_HpnicfevtModuleSw_LSB1RSP2CA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1RSP2CA = _HpnicfevtModuleSw_LSB1RSP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 260)
)
_HpnicfevtModuleSw_SR01XP4LVC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XP4LVC = _HpnicfevtModuleSw_SR01XP4LVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 261)
)
_HpnicfevtModuleSw_SR01AHP4GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01AHP4GWA = _HpnicfevtModuleSw_SR01AHP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 262)
)
_HpnicfevtModuleSw_SR01CLP4GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01CLP4GWA = _HpnicfevtModuleSw_SR01CLP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 263)
)
_HpnicfevtModuleSw_SR01ET32GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01ET32GWA = _HpnicfevtModuleSw_SR01ET32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 264)
)
_HpnicfevtModuleSw_SR01IDSVB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01IDSVB = _HpnicfevtModuleSw_SR01IDSVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 265)
)
_HpnicfevtModuleSw_SR01SRPUF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUF = _HpnicfevtModuleSw_SR01SRPUF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 266)
)
_HpnicfevtModuleSw_SR01NAML_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01NAML = _HpnicfevtModuleSw_SR01NAML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 267)
)
_HpnicfevtModuleSw_SR01RSP2WA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01RSP2WA = _HpnicfevtModuleSw_SR01RSP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 268)
)
_HpnicfevtModuleSw_LSPM1XP1P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM1XP1P = _HpnicfevtModuleSw_LSPM1XP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 269)
)
_HpnicfevtModuleSw_LSPM1XP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM1XP2P = _HpnicfevtModuleSw_LSPM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 270)
)
_HpnicfevtModuleSw_LSPM1CX2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM1CX2P = _HpnicfevtModuleSw_LSPM1CX2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 271)
)
_HpnicfevtModuleSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_STK_1000BASE_T = _HpnicfevtModuleSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 272)
)
_HpnicfevtModuleSw_LSB1SRP1M0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1M0 = _HpnicfevtModuleSw_LSB1SRP1M0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 300)
)
_HpnicfevtModuleSw_LSB1SRP1M1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1M1 = _HpnicfevtModuleSw_LSB1SRP1M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 301)
)
_HpnicfevtModuleSw_LSB1GP12DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP12DB = _HpnicfevtModuleSw_LSB1GP12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 302)
)
_HpnicfevtModuleSw_LSB1GT12DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT12DB = _HpnicfevtModuleSw_LSB1GT12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 303)
)
_HpnicfevtModuleSw_LSB1XK1DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XK1DB = _HpnicfevtModuleSw_LSB1XK1DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 304)
)
_HpnicfevtModuleSw_LSB1XP2DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP2DB = _HpnicfevtModuleSw_LSB1XP2DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 305)
)
_HpnicfevtModuleSw_LSB1XP2DC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP2DC = _HpnicfevtModuleSw_LSB1XP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 306)
)
_HpnicfevtModuleSw_LSB1GT48LDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GT48LDB = _HpnicfevtModuleSw_LSB1GT48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 307)
)
_HpnicfevtModuleSw_LSB1XP4TDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4TDB = _HpnicfevtModuleSw_LSB1XP4TDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 308)
)
_HpnicfevtModuleSw_LSB1XP4TDC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4TDC = _HpnicfevtModuleSw_LSB1XP4TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 309)
)
_HpnicfevtModuleSw_LSB1RSP2DC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1RSP2DC = _HpnicfevtModuleSw_LSB1RSP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 310)
)
_HpnicfevtModuleSw_LSB1VP2DC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1VP2DC = _HpnicfevtModuleSw_LSB1VP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 311)
)
_HpnicfevtModuleSw_LSB1XP4DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1XP4DB = _HpnicfevtModuleSw_LSB1XP4DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 312)
)
_HpnicfevtModuleSw_LSB1SRP2E0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2E0 = _HpnicfevtModuleSw_LSB1SRP2E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 313)
)
_HpnicfevtModuleSw_LSB1SRP2E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2E1 = _HpnicfevtModuleSw_LSB1SRP2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 314)
)
_HpnicfevtModuleSw_LSB1SRP2E2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2E2 = _HpnicfevtModuleSw_LSB1SRP2E2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 315)
)
_HpnicfevtModuleSw_LSB1SRP2E3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2E3 = _HpnicfevtModuleSw_LSB1SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 316)
)
_HpnicfevtModuleSw_SR01SRPUQ_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUQ = _HpnicfevtModuleSw_SR01SRPUQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 317)
)
_HpnicfevtModuleSw_AHP1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_AHP1 = _HpnicfevtModuleSw_AHP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 318)
)
_HpnicfevtModuleSw_AHP2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_AHP2 = _HpnicfevtModuleSw_AHP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 319)
)
_HpnicfevtModuleSw_CLP1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CLP1 = _HpnicfevtModuleSw_CLP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 320)
)
_HpnicfevtModuleSw_CLP2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CLP2 = _HpnicfevtModuleSw_CLP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 321)
)
_HpnicfevtModuleSw_ET16_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_ET16 = _HpnicfevtModuleSw_ET16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 322)
)
_HpnicfevtModuleSw_LSB1SRP1NA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA0 = _HpnicfevtModuleSw_LSB1SRP1NA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 323)
)
_HpnicfevtModuleSw_LSB1SRP1NA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA1 = _HpnicfevtModuleSw_LSB1SRP1NA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 324)
)
_HpnicfevtModuleSw_LSB1SRP1NA2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA2 = _HpnicfevtModuleSw_LSB1SRP1NA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 325)
)
_HpnicfevtModuleSw_LSB1SRP1NA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA3 = _HpnicfevtModuleSw_LSB1SRP1NA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 326)
)
_HpnicfevtModuleSw_SR01AHP1GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01AHP1GWA = _HpnicfevtModuleSw_SR01AHP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 327)
)
_HpnicfevtModuleSw_SR01AHP2GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01AHP2GWA = _HpnicfevtModuleSw_SR01AHP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 328)
)
_HpnicfevtModuleSw_SR01CLP1GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01CLP1GWA = _HpnicfevtModuleSw_SR01CLP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 329)
)
_HpnicfevtModuleSw_SR01CLP2GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01CLP2GWA = _HpnicfevtModuleSw_SR01CLP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 330)
)
_HpnicfevtModuleSw_SR01ET16GWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01ET16GWA = _HpnicfevtModuleSw_SR01ET16GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 331)
)
_HpnicfevtModuleSw_SR01GP12VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01GP12VB = _HpnicfevtModuleSw_SR01GP12VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 332)
)
_HpnicfevtModuleSw_SR01XK1VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XK1VB = _HpnicfevtModuleSw_SR01XK1VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 333)
)
_HpnicfevtModuleSw_SR01XP2VC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XP2VC = _HpnicfevtModuleSw_SR01XP2VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 334)
)
_HpnicfevtModuleSw_SR01XP4LVB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01XP4LVB = _HpnicfevtModuleSw_SR01XP4LVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 335)
)
_HpnicfevtModuleSw_SR01SRPUEA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01SRPUEA = _HpnicfevtModuleSw_SR01SRPUEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 336)
)
_HpnicfevtModuleSw_LSB1SRP1N4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N4 = _HpnicfevtModuleSw_LSB1SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 337)
)
_HpnicfevtModuleSw_LSB1SRP1N5_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N5 = _HpnicfevtModuleSw_LSB1SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 338)
)
_HpnicfevtModuleSw_LSB1SRP1N6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N6 = _HpnicfevtModuleSw_LSB1SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 339)
)
_HpnicfevtModuleSw_LSB1SRP1N7_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1N7 = _HpnicfevtModuleSw_LSB1SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 340)
)
_HpnicfevtModuleSw_LSB1SRP2N4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N4 = _HpnicfevtModuleSw_LSB1SRP2N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 341)
)
_HpnicfevtModuleSw_LSB1SRP2N5_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N5 = _HpnicfevtModuleSw_LSB1SRP2N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 342)
)
_HpnicfevtModuleSw_LSB1SRP2N6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N6 = _HpnicfevtModuleSw_LSB1SRP2N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 343)
)
_HpnicfevtModuleSw_LSB1SRP2N7_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP2N7 = _HpnicfevtModuleSw_LSB1SRP2N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 344)
)
_HpnicfevtModuleSw_LSB1SRP1NA4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA4 = _HpnicfevtModuleSw_LSB1SRP1NA4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 345)
)
_HpnicfevtModuleSw_LSB1SRP1NA5_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA5 = _HpnicfevtModuleSw_LSB1SRP1NA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 346)
)
_HpnicfevtModuleSw_LSB1SRP1NA6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA6 = _HpnicfevtModuleSw_LSB1SRP1NA6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 347)
)
_HpnicfevtModuleSw_LSB1SRP1NA7_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SRP1NA7 = _HpnicfevtModuleSw_LSB1SRP1NA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 348)
)
_HpnicfevtModuleSw_LSB2GV48DA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2GV48DA = _HpnicfevtModuleSw_LSB2GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 349)
)
_HpnicfevtModuleSw_LSB1RGP2GDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1RGP2GDB = _HpnicfevtModuleSw_LSB1RGP2GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 350)
)
_HpnicfevtModuleSw_LSB1RGP4GDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1RGP4GDB = _HpnicfevtModuleSw_LSB1RGP4GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 351)
)
_HpnicfevtModuleSw_LSB2GP24DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2GP24DB = _HpnicfevtModuleSw_LSB2GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 352)
)
_HpnicfevtModuleSw_LSB2GP24DC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2GP24DC = _HpnicfevtModuleSw_LSB2GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 353)
)
_HpnicfevtModuleSw_LSB2GT24DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2GT24DB = _HpnicfevtModuleSw_LSB2GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 354)
)
_HpnicfevtModuleSw_LSB2FW8DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2FW8DB = _HpnicfevtModuleSw_LSB2FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 355)
)
_HpnicfevtModuleSw_LSB2IPSEC8DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2IPSEC8DB = _HpnicfevtModuleSw_LSB2IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 356)
)
_HpnicfevtModuleSw_LSB2GV48DB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2GV48DB = _HpnicfevtModuleSw_LSB2GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 357)
)
_HpnicfevtModuleSw_RGP2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_RGP2 = _HpnicfevtModuleSw_RGP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 358)
)
_HpnicfevtModuleSw_RGP4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_RGP4 = _HpnicfevtModuleSw_RGP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 359)
)
_HpnicfevtModuleSw_SR02FW8VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02FW8VB = _HpnicfevtModuleSw_SR02FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 360)
)
_HpnicfevtModuleSw_SR02IPSEC8VB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02IPSEC8VB = _HpnicfevtModuleSw_SR02IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 361)
)
_HpnicfevtModuleSw_LSB2SRP1N0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N0 = _HpnicfevtModuleSw_LSB2SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 362)
)
_HpnicfevtModuleSw_LSB2SRP1N1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N1 = _HpnicfevtModuleSw_LSB2SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 363)
)
_HpnicfevtModuleSw_LSB2SRP1N2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N2 = _HpnicfevtModuleSw_LSB2SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 364)
)
_HpnicfevtModuleSw_LSB2SRP1N3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N3 = _HpnicfevtModuleSw_LSB2SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 365)
)
_HpnicfevtModuleSw_LSB2SRP1N4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N4 = _HpnicfevtModuleSw_LSB2SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 366)
)
_HpnicfevtModuleSw_LSB2SRP1N5_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N5 = _HpnicfevtModuleSw_LSB2SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 367)
)
_HpnicfevtModuleSw_LSB2SRP1N6_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N6 = _HpnicfevtModuleSw_LSB2SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 368)
)
_HpnicfevtModuleSw_LSB2SRP1N7_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB2SRP1N7 = _HpnicfevtModuleSw_LSB2SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 369)
)
_HpnicfevtModuleSw_SR02SRPUE_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRPUE = _HpnicfevtModuleSw_SR02SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 370)
)
_HpnicfevtModuleSw_SR01LN1BQH0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01LN1BQH0 = _HpnicfevtModuleSw_SR01LN1BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 371)
)
_HpnicfevtModuleSw_SR01DXP1L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DXP1L = _HpnicfevtModuleSw_SR01DXP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 372)
)
_HpnicfevtModuleSw_SR01DGP10L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DGP10L = _HpnicfevtModuleSw_SR01DGP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 373)
)
_HpnicfevtModuleSw_SR01DRSP2L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DRSP2L = _HpnicfevtModuleSw_SR01DRSP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 374)
)
_HpnicfevtModuleSw_SR01DRUP1L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DRUP1L = _HpnicfevtModuleSw_SR01DRUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 375)
)
_HpnicfevtModuleSw_SR01DGP20R_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DGP20R = _HpnicfevtModuleSw_SR01DGP20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 376)
)
_HpnicfevtModuleSw_SR01DPLP8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DPLP8L = _HpnicfevtModuleSw_SR01DPLP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 377)
)
_HpnicfevtModuleSw_SR01DXP2R_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DXP2R = _HpnicfevtModuleSw_SR01DXP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 378)
)
_HpnicfevtModuleSw_LSB1FW2A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1FW2A0 = _HpnicfevtModuleSw_LSB1FW2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 379)
)
_HpnicfevtModuleSw_LSB1GP48LDB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1GP48LDB = _HpnicfevtModuleSw_LSB1GP48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 380)
)
_HpnicfevtModuleSw_SR01LN1BNA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01LN1BNA0 = _HpnicfevtModuleSw_SR01LN1BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 381)
)
_HpnicfevtModuleSw_SR01LN2BQH0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01LN2BQH0 = _HpnicfevtModuleSw_SR01LN2BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 382)
)
_HpnicfevtModuleSw_SR01LN2BNA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01LN2BNA0 = _HpnicfevtModuleSw_SR01LN2BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 383)
)
_HpnicfevtModuleSw_SR01DGT20R_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DGT20R = _HpnicfevtModuleSw_SR01DGT20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 384)
)
_HpnicfevtModuleSw_SR01DPSP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DPSP4L = _HpnicfevtModuleSw_SR01DPSP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 385)
)
_HpnicfevtModuleSw_SR01DPUP1L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DPUP1L = _HpnicfevtModuleSw_SR01DPUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 386)
)
_HpnicfevtModuleSw_SR01DPL2G6L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DPL2G6L = _HpnicfevtModuleSw_SR01DPL2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 387)
)
_HpnicfevtModuleSw_SR01DPH2G6L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DPH2G6L = _HpnicfevtModuleSw_SR01DPH2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 388)
)
_HpnicfevtModuleSw_SR01DPS2G4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DPS2G4L = _HpnicfevtModuleSw_SR01DPS2G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 389)
)
_HpnicfevtModuleSw_SR01DCL1G8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DCL1G8L = _HpnicfevtModuleSw_SR01DCL1G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 390)
)
_HpnicfevtModuleSw_SR01DCL2G8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DCL2G8L = _HpnicfevtModuleSw_SR01DCL2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 391)
)
_HpnicfevtModuleSw_SR01DET8G8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DET8G8L = _HpnicfevtModuleSw_SR01DET8G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 392)
)
_HpnicfevtModuleSw_SR02SRP2E3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRP2E3 = _HpnicfevtModuleSw_SR02SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 393)
)
_HpnicfevtModuleSw_SR02SRP1E3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRP1E3 = _HpnicfevtModuleSw_SR02SRP1E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 394)
)
_HpnicfevtModuleSw_SR02SRP1M3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRP1M3 = _HpnicfevtModuleSw_SR02SRP1M3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 395)
)
_HpnicfevtModuleSw_SR01DQCP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DQCP4L = _HpnicfevtModuleSw_SR01DQCP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 396)
)
_HpnicfevtModuleSw_SR01DTCP8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DTCP8L = _HpnicfevtModuleSw_SR01DTCP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 397)
)
_HpnicfevtModuleSw_LSB1AFC1A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1AFC1A0 = _HpnicfevtModuleSw_LSB1AFC1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 398)
)
_HpnicfevtModuleSw_LSB1SSL1A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1SSL1A0 = _HpnicfevtModuleSw_LSB1SSL1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 399)
)
_HpnicfevtModuleSw_IMNAM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IMNAM = _HpnicfevtModuleSw_IMNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 400)
)
_HpnicfevtModuleSw_IMNAT_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IMNAT = _HpnicfevtModuleSw_IMNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 401)
)
_HpnicfevtModuleSw_PICAHP1L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PICAHP1L = _HpnicfevtModuleSw_PICAHP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 402)
)
_HpnicfevtModuleSw_PICALP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PICALP4L = _HpnicfevtModuleSw_PICALP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 403)
)
_HpnicfevtModuleSw_PICCHP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PICCHP4L = _HpnicfevtModuleSw_PICCHP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 404)
)
_HpnicfevtModuleSw_PICCHS1G4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PICCHS1G4L = _HpnicfevtModuleSw_PICCHS1G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 405)
)
_HpnicfevtModuleSw_PICCLS4G4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PICCLS4G4L = _HpnicfevtModuleSw_PICCLS4G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 406)
)
_HpnicfevtModuleSw_PICCSP1L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PICCSP1L = _HpnicfevtModuleSw_PICCSP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 407)
)
_HpnicfevtModuleSw_LSB1ACG1A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1ACG1A0 = _HpnicfevtModuleSw_LSB1ACG1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 408)
)
_HpnicfevtModuleSw_LST1MRPNC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1MRPNC1 = _HpnicfevtModuleSw_LST1MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 409)
)
_HpnicfevtModuleSw_LST1SF18B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1SF18B1 = _HpnicfevtModuleSw_LST1SF18B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 410)
)
_HpnicfevtModuleSw_LST1SF08B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1SF08B1 = _HpnicfevtModuleSw_LST1SF08B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 411)
)
_HpnicfevtModuleSw_LST1GT48LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GT48LEC1 = _HpnicfevtModuleSw_LST1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 412)
)
_HpnicfevtModuleSw_LST1GP48LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEC1 = _HpnicfevtModuleSw_LST1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 413)
)
_HpnicfevtModuleSw_LST1XP4LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP4LEC1 = _HpnicfevtModuleSw_LST1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 414)
)
_HpnicfevtModuleSw_LST1XP8LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP8LEC1 = _HpnicfevtModuleSw_LST1XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 415)
)
_HpnicfevtModuleSw_LSR1SRP2B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1SRP2B1 = _HpnicfevtModuleSw_LSR1SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 416)
)
_HpnicfevtModuleSw_LSR1SRP2C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1SRP2C1 = _HpnicfevtModuleSw_LSR1SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 417)
)
_HpnicfevtModuleSw_LSR1SRP2B2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1SRP2B2 = _HpnicfevtModuleSw_LSR1SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 418)
)
_HpnicfevtModuleSw_LSR1SRP2C2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1SRP2C2 = _HpnicfevtModuleSw_LSR1SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 419)
)
_HpnicfevtModuleSw_LSR1GT24LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GT24LEC1 = _HpnicfevtModuleSw_LSR1GT24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 420)
)
_HpnicfevtModuleSw_LSR1GP24LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GP24LEB1 = _HpnicfevtModuleSw_LSR1GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 421)
)
_HpnicfevtModuleSw_LSR1GP24LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GP24LEC1 = _HpnicfevtModuleSw_LSR1GP24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 422)
)
_HpnicfevtModuleSw_LSR1GT48LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GT48LEB1 = _HpnicfevtModuleSw_LSR1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 423)
)
_HpnicfevtModuleSw_LSR1GT48LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GT48LEC1 = _HpnicfevtModuleSw_LSR1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 424)
)
_HpnicfevtModuleSw_LSR1GP48LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GP48LEB1 = _HpnicfevtModuleSw_LSR1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 425)
)
_HpnicfevtModuleSw_LSR1GP48LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GP48LEC1 = _HpnicfevtModuleSw_LSR1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 426)
)
_HpnicfevtModuleSw_LSR2GV48REB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2GV48REB1 = _HpnicfevtModuleSw_LSR2GV48REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 427)
)
_HpnicfevtModuleSw_LSR1XP2LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP2LEB1 = _HpnicfevtModuleSw_LSR1XP2LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 428)
)
_HpnicfevtModuleSw_LSR1XP2LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP2LEC1 = _HpnicfevtModuleSw_LSR1XP2LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 429)
)
_HpnicfevtModuleSw_LSR1XP4LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP4LEB1 = _HpnicfevtModuleSw_LSR1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 430)
)
_HpnicfevtModuleSw_LSR1XP4LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP4LEC1 = _HpnicfevtModuleSw_LSR1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 431)
)
_HpnicfevtModuleSw_IMFW_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IMFW = _HpnicfevtModuleSw_IMFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 432)
)
_HpnicfevtModuleSw_LSB1LB1A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1LB1A0 = _HpnicfevtModuleSw_LSB1LB1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 433)
)
_HpnicfevtModuleSw_LSB1IPS1A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1IPS1A0 = _HpnicfevtModuleSw_LSB1IPS1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 434)
)
_HpnicfevtModuleSw_LST1GT48LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GT48LEB1 = _HpnicfevtModuleSw_LST1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 435)
)
_HpnicfevtModuleSw_LST1GP48LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEB1 = _HpnicfevtModuleSw_LST1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 436)
)
_HpnicfevtModuleSw_LST1XP4LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP4LEB1 = _HpnicfevtModuleSw_LST1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 437)
)
_HpnicfevtModuleSw_LST1XP8LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP8LEB1 = _HpnicfevtModuleSw_LST1XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 438)
)
_HpnicfevtModuleSw_LST1XP32REB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP32REB1 = _HpnicfevtModuleSw_LST1XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 439)
)
_HpnicfevtModuleSw_LST1XP32REC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP32REC1 = _HpnicfevtModuleSw_LST1XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 440)
)
_HpnicfevtModuleSw_LSR1FW2A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1FW2A1 = _HpnicfevtModuleSw_LSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 441)
)
_HpnicfevtModuleSw_LSR1SSL1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1SSL1A1 = _HpnicfevtModuleSw_LSR1SSL1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 442)
)
_HpnicfevtModuleSw_SR01DET32G2L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR01DET32G2L = _HpnicfevtModuleSw_SR01DET32G2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 443)
)
_HpnicfevtModuleSw_LSR1GP24LEF1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GP24LEF1 = _HpnicfevtModuleSw_LSR1GP24LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 444)
)
_HpnicfevtModuleSw_LSR1XP4LEF1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP4LEF1 = _HpnicfevtModuleSw_LSR1XP4LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 445)
)
_HpnicfevtModuleSw_LSR1LB1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1LB1A1 = _HpnicfevtModuleSw_LSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 446)
)
_HpnicfevtModuleSw_LSR1NSM1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1NSM1A1 = _HpnicfevtModuleSw_LSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 447)
)
_HpnicfevtModuleSw_LSR1ACG1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1ACG1A1 = _HpnicfevtModuleSw_LSR1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 448)
)
_HpnicfevtModuleSw_LSR1IPS1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1IPS1A1 = _HpnicfevtModuleSw_LSR1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 449)
)
_HpnicfevtModuleSw_LSR2GP24LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2GP24LEB1 = _HpnicfevtModuleSw_LSR2GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 450)
)
_HpnicfevtModuleSw_LSR2GT24LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2GT24LEB1 = _HpnicfevtModuleSw_LSR2GT24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 451)
)
_HpnicfevtModuleSw_LSR2GT48LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2GT48LEB1 = _HpnicfevtModuleSw_LSR2GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 452)
)
_HpnicfevtModuleSw_SPC_GP24L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP24L = _HpnicfevtModuleSw_SPC_GP24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 453)
)
_HpnicfevtModuleSw_SPC_GT48L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GT48L = _HpnicfevtModuleSw_SPC_GT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 454)
)
_HpnicfevtModuleSw_SPC_GP48L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP48L = _HpnicfevtModuleSw_SPC_GP48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 455)
)
_HpnicfevtModuleSw_SPC_XP2L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP2L = _HpnicfevtModuleSw_SPC_XP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 456)
)
_HpnicfevtModuleSw_SPC_XP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP4L = _HpnicfevtModuleSw_SPC_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 457)
)
_HpnicfevtModuleSw_SR06SRP2E3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR06SRP2E3 = _HpnicfevtModuleSw_SR06SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 458)
)
_HpnicfevtModuleSw_SPE_2010_E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPE_2010_E = _HpnicfevtModuleSw_SPE_2010_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 459)
)
_HpnicfevtModuleSw_SPE_2020_E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPE_2020_E = _HpnicfevtModuleSw_SPE_2020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 460)
)
_HpnicfevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP4L_S_SDI = _HpnicfevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 461)
)
_HpnicfevtModuleSw_SPC_GT48L_SDI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GT48L_SDI = _HpnicfevtModuleSw_SPC_GT48L_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 462)
)
_HpnicfevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP48L_S_SDI = _HpnicfevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 463)
)
_HpnicfevtModuleSw_SPC_SR02OPMA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_SR02OPMA0 = _HpnicfevtModuleSw_SPC_SR02OPMA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 464)
)
_HpnicfevtModuleSw_LSR1XP16REB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP16REB1 = _HpnicfevtModuleSw_LSR1XP16REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 465)
)
_HpnicfevtModuleSw_LSR1GP48LEF1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1GP48LEF1 = _HpnicfevtModuleSw_LSR1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 466)
)
_HpnicfevtModuleSw_LST1GP48LEF1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEF1 = _HpnicfevtModuleSw_LST1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 467)
)
_HpnicfevtModuleSw_LST1XP8LEF1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP8LEF1 = _HpnicfevtModuleSw_LST1XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 468)
)
_HpnicfevtModuleSw_SPE_1010_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPE_1010_II = _HpnicfevtModuleSw_SPE_1010_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 469)
)
_HpnicfevtModuleSw_SPE_1010_E_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPE_1010_E_II = _HpnicfevtModuleSw_SPE_1010_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 470)
)
_HpnicfevtModuleSw_SPE_1020_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPE_1020_II = _HpnicfevtModuleSw_SPE_1020_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 471)
)
_HpnicfevtModuleSw_SPE_1020_E_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPE_1020_E_II = _HpnicfevtModuleSw_SPE_1020_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 472)
)
_HpnicfevtModuleSw_LST1FW2A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1FW2A1 = _HpnicfevtModuleSw_LST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 473)
)
_HpnicfevtModuleSw_LST1NSM1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1NSM1A1 = _HpnicfevtModuleSw_LST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 474)
)
_HpnicfevtModuleSw_LST1LB1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1LB1A1 = _HpnicfevtModuleSw_LST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 475)
)
_HpnicfevtModuleSw_LST1ACG1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1ACG1A1 = _HpnicfevtModuleSw_LST1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 476)
)
_HpnicfevtModuleSw_LST1IPS1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1IPS1A1 = _HpnicfevtModuleSw_LST1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 477)
)
_HpnicfevtModuleSw_LSR1DRUP1L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DRUP1L1 = _HpnicfevtModuleSw_LSR1DRUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 478)
)
_HpnicfevtModuleSw_LSR1DPUP1L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DPUP1L1 = _HpnicfevtModuleSw_LSR1DPUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 479)
)
_HpnicfevtModuleSw_LSR1DPSP4L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DPSP4L1 = _HpnicfevtModuleSw_LSR1DPSP4L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 480)
)
_HpnicfevtModuleSw_LSR1DTCP8L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DTCP8L1 = _HpnicfevtModuleSw_LSR1DTCP8L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 481)
)
_HpnicfevtModuleSw_LSR1DXP1L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DXP1L1 = _HpnicfevtModuleSw_LSR1DXP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 482)
)
_HpnicfevtModuleSw_LSR1DGP10L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DGP10L1 = _HpnicfevtModuleSw_LSR1DGP10L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 483)
)
_HpnicfevtModuleSw_LSR1LN1BNL1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1LN1BNL1 = _HpnicfevtModuleSw_LSR1LN1BNL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 484)
)
_HpnicfevtModuleSw_LSR1LN2BL1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1LN2BL1 = _HpnicfevtModuleSw_LSR1LN2BL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 485)
)
_HpnicfevtModuleSw_LSR1SRP2D1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1SRP2D1 = _HpnicfevtModuleSw_LSR1SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 486)
)
_HpnicfevtModuleSw_IM_NAT_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_NAT_II = _HpnicfevtModuleSw_IM_NAT_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 487)
)
_HpnicfevtModuleSw_IM_NAM_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_NAM_II = _HpnicfevtModuleSw_IM_NAM_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 488)
)
_HpnicfevtModuleSw_CR_MRP_I_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_MRP_I = _HpnicfevtModuleSw_CR_MRP_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 489)
)
_HpnicfevtModuleSw_CR_SF18C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SF18C = _HpnicfevtModuleSw_CR_SF18C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 490)
)
_HpnicfevtModuleSw_CR_SF08C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SF08C = _HpnicfevtModuleSw_CR_SF08C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 491)
)
_HpnicfevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP8LEF = _HpnicfevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 492)
)
_HpnicfevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP4LEF = _HpnicfevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 493)
)
_HpnicfevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_GP48LEF = _HpnicfevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 494)
)
_HpnicfevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_GT48LEF = _HpnicfevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 495)
)
_HpnicfevtModuleSw_CR_SPE_3020_E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPE_3020_E = _HpnicfevtModuleSw_CR_SPE_3020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 496)
)
_HpnicfevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_PUP4L_E = _HpnicfevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 497)
)
_HpnicfevtModuleSw_LST1SF08C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1SF08C1 = _HpnicfevtModuleSw_LST1SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 498)
)
_HpnicfevtModuleSw_LST1SF18C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1SF18C1 = _HpnicfevtModuleSw_LST1SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 499)
)
_HpnicfevtModuleSw_LS81GP16TM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP16TM = _HpnicfevtModuleSw_LS81GP16TM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 500)
)
_HpnicfevtModuleSw_LS81VP4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81VP4C = _HpnicfevtModuleSw_LS81VP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 501)
)
_HpnicfevtModuleSw_LS8M1PT8P0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS8M1PT8P0 = _HpnicfevtModuleSw_LS8M1PT8P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 502)
)
_HpnicfevtModuleSw_LS8M1PT8GB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS8M1PT8GB0 = _HpnicfevtModuleSw_LS8M1PT8GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 503)
)
_HpnicfevtModuleSw_LS8M1PT4GB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS8M1PT4GB0 = _HpnicfevtModuleSw_LS8M1PT4GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 504)
)
_HpnicfevtModuleSw_LS81GP2R_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP2R = _HpnicfevtModuleSw_LS81GP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 505)
)
_HpnicfevtModuleSw_LS81GP4R_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP4R = _HpnicfevtModuleSw_LS81GP4R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 506)
)
_HpnicfevtModuleSw_LS81IPSECA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81IPSECA = _HpnicfevtModuleSw_LS81IPSECA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 507)
)
_HpnicfevtModuleSw_LS81FWA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81FWA = _HpnicfevtModuleSw_LS81FWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 508)
)
_HpnicfevtModuleSw_LS82VSNP_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS82VSNP = _HpnicfevtModuleSw_LS82VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 509)
)
_HpnicfevtModuleSw_LSQ1GV48SA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV48SA = _HpnicfevtModuleSw_LSQ1GV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 510)
)
_HpnicfevtModuleSw_LSQ1SRPB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPB = _HpnicfevtModuleSw_LSQ1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 511)
)
_HpnicfevtModuleSw_LSQ1SRP2XB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRP2XB = _HpnicfevtModuleSw_LSQ1SRP2XB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 512)
)
_HpnicfevtModuleSw_LSQ1SRP1CB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRP1CB = _HpnicfevtModuleSw_LSQ1SRP1CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 513)
)
_HpnicfevtModuleSw_LSQ1FV48SA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FV48SA = _HpnicfevtModuleSw_LSQ1FV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 514)
)
_HpnicfevtModuleSw_LSD1MPUA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1MPUA = _HpnicfevtModuleSw_LSD1MPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 515)
)
_HpnicfevtModuleSw_LSD1GP20A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP20A0 = _HpnicfevtModuleSw_LSD1GP20A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 516)
)
_HpnicfevtModuleSw_LSD1GP20TA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP20TA0 = _HpnicfevtModuleSw_LSD1GP20TA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 517)
)
_HpnicfevtModuleSw_LSD1GP36A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP36A0 = _HpnicfevtModuleSw_LSD1GP36A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 518)
)
_HpnicfevtModuleSw_LSD1GP20XA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP20XA0 = _HpnicfevtModuleSw_LSD1GP20XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 519)
)
_HpnicfevtModuleSw_LSD1GP20EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP20EA0 = _HpnicfevtModuleSw_LSD1GP20EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 520)
)
_HpnicfevtModuleSw_LSD1GP20RA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP20RA0 = _HpnicfevtModuleSw_LSD1GP20RA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 521)
)
_HpnicfevtModuleSw_LSD1GP16A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP16A0 = _HpnicfevtModuleSw_LSD1GP16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 522)
)
_HpnicfevtModuleSw_LSD1GT16A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GT16A0 = _HpnicfevtModuleSw_LSD1GT16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 523)
)
_HpnicfevtModuleSw_LSD1XP2A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1XP2A0 = _HpnicfevtModuleSw_LSD1XP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 524)
)
_HpnicfevtModuleSw_LSD1EP2A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1EP2A0 = _HpnicfevtModuleSw_LSD1EP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 525)
)
_HpnicfevtModuleSw_LSD1RP2A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1RP2A0 = _HpnicfevtModuleSw_LSD1RP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 526)
)
_HpnicfevtModuleSw_LSQ1GV48SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV48SC = _HpnicfevtModuleSw_LSQ1GV48SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 527)
)
_HpnicfevtModuleSw_LSQ1FP48SA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FP48SA = _HpnicfevtModuleSw_LSQ1FP48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 528)
)
_HpnicfevtModuleSw_LSQ1GP24SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24SC = _HpnicfevtModuleSw_LSQ1GP24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 529)
)
_HpnicfevtModuleSw_LSQ1GT24SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GT24SC = _HpnicfevtModuleSw_LSQ1GT24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 530)
)
_HpnicfevtModuleSw_LSQ1TGX2SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX2SC = _HpnicfevtModuleSw_LSQ1TGX2SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 531)
)
_HpnicfevtModuleSw_LSQ1GP12EA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP12EA = _HpnicfevtModuleSw_LSQ1GP12EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 532)
)
_HpnicfevtModuleSw_LSQ1TGX1EA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX1EA = _HpnicfevtModuleSw_LSQ1TGX1EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 533)
)
_HpnicfevtModuleSw_LSQ1P24XGSC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1P24XGSC = _HpnicfevtModuleSw_LSQ1P24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 534)
)
_HpnicfevtModuleSw_LSQ1T24XGSC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1T24XGSC = _HpnicfevtModuleSw_LSQ1T24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 535)
)
_HpnicfevtModuleSw_LS81TGX1B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81TGX1B = _HpnicfevtModuleSw_LS81TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 536)
)
_HpnicfevtModuleSw_LSQ1PT4PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1PT4PSC0 = _HpnicfevtModuleSw_LSQ1PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 537)
)
_HpnicfevtModuleSw_LS81SRPG13_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG13 = _HpnicfevtModuleSw_LS81SRPG13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 538)
)
_HpnicfevtModuleSw_LS81SRPG14_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG14 = _HpnicfevtModuleSw_LS81SRPG14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 539)
)
_HpnicfevtModuleSw_LS81SRPG15_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81SRPG15 = _HpnicfevtModuleSw_LS81SRPG15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 540)
)
_HpnicfevtModuleSw_LSQ1GP48SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48SC0 = _HpnicfevtModuleSw_LSQ1GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 541)
)
_HpnicfevtModuleSw_LSQ1GP12SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP12SC0 = _HpnicfevtModuleSw_LSQ1GP12SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 542)
)
_HpnicfevtModuleSw_LSD1SRPA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1SRPA = _HpnicfevtModuleSw_LSD1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 543)
)
_HpnicfevtModuleSw_LSD1SRPB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1SRPB = _HpnicfevtModuleSw_LSD1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 544)
)
_HpnicfevtModuleSw_LSD1SRPC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1SRPC = _HpnicfevtModuleSw_LSD1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 545)
)
_HpnicfevtModuleSw_LSD1GT16PES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GT16PES0 = _HpnicfevtModuleSw_LSD1GT16PES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 546)
)
_HpnicfevtModuleSw_LSD1GP24ES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP24ES0 = _HpnicfevtModuleSw_LSD1GP24ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 547)
)
_HpnicfevtModuleSw_LSD1GT24XES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GT24XES0 = _HpnicfevtModuleSw_LSD1GT24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 548)
)
_HpnicfevtModuleSw_LSD1GP24XES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP24XES0 = _HpnicfevtModuleSw_LSD1GP24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 549)
)
_HpnicfevtModuleSw_LSD1XP2ES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1XP2ES0 = _HpnicfevtModuleSw_LSD1XP2ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 550)
)
_HpnicfevtModuleSw_LSD1GP48ES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP48ES0 = _HpnicfevtModuleSw_LSD1GP48ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 551)
)
_HpnicfevtModuleSw_LSQ1MPUA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUA0 = _HpnicfevtModuleSw_LSQ1MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 552)
)
_HpnicfevtModuleSw_LSQ1MPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUA1 = _HpnicfevtModuleSw_LSQ1MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 553)
)
_HpnicfevtModuleSw_LSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FWBSC0 = _HpnicfevtModuleSw_LSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 554)
)
_HpnicfevtModuleSw_LSQ1PT8PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1PT8PSC0 = _HpnicfevtModuleSw_LSQ1PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 555)
)
_HpnicfevtModuleSw_LSQ1PT16PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1PT16PSC0 = _HpnicfevtModuleSw_LSQ1PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 556)
)
_HpnicfevtModuleSw_SA11MPUA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SA11MPUA0 = _HpnicfevtModuleSw_SA11MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 557)
)
_HpnicfevtModuleSw_SA11MPUB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SA11MPUB0 = _HpnicfevtModuleSw_SA11MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 558)
)
_HpnicfevtModuleSw_LSQ1AFCBSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1AFCBSC0 = _HpnicfevtModuleSw_LSQ1AFCBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 559)
)
_HpnicfevtModuleSw_LSQ1MPUB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUB0 = _HpnicfevtModuleSw_LSQ1MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 560)
)
_HpnicfevtModuleSw_LSQ1MPUB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUB1 = _HpnicfevtModuleSw_LSQ1MPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 561)
)
_HpnicfevtModuleSw_LSQ1PT4PSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1PT4PSC1 = _HpnicfevtModuleSw_LSQ1PT4PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 562)
)
_HpnicfevtModuleSw_LSQ1PT8PSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1PT8PSC1 = _HpnicfevtModuleSw_LSQ1PT8PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 563)
)
_HpnicfevtModuleSw_LSQ1PT16PSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1PT16PSC1 = _HpnicfevtModuleSw_LSQ1PT16PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 564)
)
_HpnicfevtModuleSw_LSQ1FP48USA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FP48USA0 = _HpnicfevtModuleSw_LSQ1FP48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 565)
)
_HpnicfevtModuleSw_LSQ1FP48USA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FP48USA1 = _HpnicfevtModuleSw_LSQ1FP48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 566)
)
_HpnicfevtModuleSw_LSQ1FV48USA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FV48USA0 = _HpnicfevtModuleSw_LSQ1FV48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 567)
)
_HpnicfevtModuleSw_LSQ1FV48USA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FV48USA1 = _HpnicfevtModuleSw_LSQ1FV48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 568)
)
_HpnicfevtModuleSw_LSQ1SRPD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPD0 = _HpnicfevtModuleSw_LSQ1SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 569)
)
_HpnicfevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGP24TSC0 = _HpnicfevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 570)
)
_HpnicfevtModuleSw_LSQ1GP24TSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TSC0 = _HpnicfevtModuleSw_LSQ1GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 571)
)
_HpnicfevtModuleSw_LSQ1ACGASC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1ACGASC0 = _HpnicfevtModuleSw_LSQ1ACGASC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 572)
)
_HpnicfevtModuleSw_LSD1XP1ES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1XP1ES0 = _HpnicfevtModuleSw_LSD1XP1ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 573)
)
_HpnicfevtModuleSw_LSD1GP12ES0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSD1GP12ES0 = _HpnicfevtModuleSw_LSD1GP12ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 574)
)
_HpnicfevtModuleSw_LSQ1SRP12GB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRP12GB0 = _HpnicfevtModuleSw_LSQ1SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 575)
)
_HpnicfevtModuleSw_LSQ1GV40PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV40PSC0 = _HpnicfevtModuleSw_LSQ1GV40PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 576)
)
_HpnicfevtModuleSw_LSQ1FWBSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FWBSC1 = _HpnicfevtModuleSw_LSQ1FWBSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 577)
)
_HpnicfevtModuleSw_LSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1NSMSC0 = _HpnicfevtModuleSw_LSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 578)
)
_HpnicfevtModuleSw_LSQ1NSMSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1NSMSC1 = _HpnicfevtModuleSw_LSQ1NSMSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 579)
)
_HpnicfevtModuleSw_LSQ1AFDBSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1AFDBSC0 = _HpnicfevtModuleSw_LSQ1AFDBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 580)
)
_HpnicfevtModuleSw_LS81MPUB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81MPUB = _HpnicfevtModuleSw_LS81MPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 581)
)
_HpnicfevtModuleSw_LS81FP48XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81FP48XL = _HpnicfevtModuleSw_LS81FP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 582)
)
_HpnicfevtModuleSw_LS81FT48XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81FT48XL = _HpnicfevtModuleSw_LS81FT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 583)
)
_HpnicfevtModuleSw_LS81GP12XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP12XL = _HpnicfevtModuleSw_LS81GP12XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 584)
)
_HpnicfevtModuleSw_LS81GP24XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP24XL = _HpnicfevtModuleSw_LS81GP24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 585)
)
_HpnicfevtModuleSw_LS81GP48XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GP48XL = _HpnicfevtModuleSw_LS81GP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 586)
)
_HpnicfevtModuleSw_LS81GT24XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GT24XL = _HpnicfevtModuleSw_LS81GT24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 587)
)
_HpnicfevtModuleSw_LS81GT48XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81GT48XL = _HpnicfevtModuleSw_LS81GT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 588)
)
_HpnicfevtModuleSw_LS81TGX2XL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS81TGX2XL = _HpnicfevtModuleSw_LS81TGX2XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 589)
)
_HpnicfevtModuleSw_LSQ1GV48SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV48SD0 = _HpnicfevtModuleSw_LSQ1GV48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 590)
)
_HpnicfevtModuleSw_LSQ1GP48EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48EB0 = _HpnicfevtModuleSw_LSQ1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 591)
)
_HpnicfevtModuleSw_LSQ1IPSSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1IPSSC0 = _HpnicfevtModuleSw_LSQ1IPSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 592)
)
_HpnicfevtModuleSw_LSQ1GV48SD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV48SD1 = _HpnicfevtModuleSw_LSQ1GV48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 593)
)
_HpnicfevtModuleSw_LSQ1GP48SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48SD0 = _HpnicfevtModuleSw_LSQ1GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 594)
)
_HpnicfevtModuleSw_LSQ1GP48SD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48SD1 = _HpnicfevtModuleSw_LSQ1GP48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 595)
)
_HpnicfevtModuleSw_LSQ1SRPA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPA0 = _HpnicfevtModuleSw_LSQ1SRPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 596)
)
_HpnicfevtModuleSw_LSQ1SRPA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPA1 = _HpnicfevtModuleSw_LSQ1SRPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 597)
)
_HpnicfevtModuleSw_LSQ2FP48SA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2FP48SA0 = _HpnicfevtModuleSw_LSQ2FP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 598)
)
_HpnicfevtModuleSw_LSQ2FP48SA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2FP48SA1 = _HpnicfevtModuleSw_LSQ2FP48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 599)
)
_HpnicfevtModuleSw_LSQ2FT48SA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2FT48SA0 = _HpnicfevtModuleSw_LSQ2FT48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 600)
)
_HpnicfevtModuleSw_LSQ2FT48SA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2FT48SA1 = _HpnicfevtModuleSw_LSQ2FT48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 601)
)
_HpnicfevtModuleSw_LSQ1GV24PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV24PSC0 = _HpnicfevtModuleSw_LSQ1GV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 602)
)
_HpnicfevtModuleSw_LSQ1GV24PSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV24PSC1 = _HpnicfevtModuleSw_LSQ1GV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 603)
)
_HpnicfevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGV24PSC0 = _HpnicfevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 604)
)
_HpnicfevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGV24PSC1 = _HpnicfevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 605)
)
_HpnicfevtModuleSw_LSQ1GP24TEB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TEB0 = _HpnicfevtModuleSw_LSQ1GP24TEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 606)
)
_HpnicfevtModuleSw_LSQ1GP24TEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TEB1 = _HpnicfevtModuleSw_LSQ1GP24TEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 607)
)
_HpnicfevtModuleSw_LSQ1GP24TSD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TSD0 = _HpnicfevtModuleSw_LSQ1GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 608)
)
_HpnicfevtModuleSw_LSQ1GP24TSD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TSD1 = _HpnicfevtModuleSw_LSQ1GP24TSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 609)
)
_HpnicfevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TXSD0 = _HpnicfevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 610)
)
_HpnicfevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TXSD1 = _HpnicfevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 611)
)
_HpnicfevtModuleSw_LSQ1TGX2EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX2EB0 = _HpnicfevtModuleSw_LSQ1TGX2EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 612)
)
_HpnicfevtModuleSw_LSQ1TGX2EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX2EB1 = _HpnicfevtModuleSw_LSQ1TGX2EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 613)
)
_HpnicfevtModuleSw_LSQ1TGX2SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX2SD0 = _HpnicfevtModuleSw_LSQ1TGX2SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 614)
)
_HpnicfevtModuleSw_LSQ1TGX2SD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX2SD1 = _HpnicfevtModuleSw_LSQ1TGX2SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 615)
)
_HpnicfevtModuleSw_LSQ1TGX4SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX4SD0 = _HpnicfevtModuleSw_LSQ1TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 616)
)
_HpnicfevtModuleSw_LSQ1TGX4SD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX4SD1 = _HpnicfevtModuleSw_LSQ1TGX4SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 617)
)
_HpnicfevtModuleSw_LSQ1TGX8SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX8SD0 = _HpnicfevtModuleSw_LSQ1TGX8SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 618)
)
_HpnicfevtModuleSw_LSQ1TGX8SD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX8SD1 = _HpnicfevtModuleSw_LSQ1TGX8SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 619)
)
_HpnicfevtModuleSw_LSQ1GP48EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48EB1 = _HpnicfevtModuleSw_LSQ1GP48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 620)
)
_HpnicfevtModuleSw_LSQ1TGX4EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX4EB0 = _HpnicfevtModuleSw_LSQ1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 621)
)
_HpnicfevtModuleSw_LSQ1TGX4EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX4EB1 = _HpnicfevtModuleSw_LSQ1TGX4EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 622)
)
_HpnicfevtModuleSw_LSQ1GP12SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP12SC3 = _HpnicfevtModuleSw_LSQ1GP12SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 623)
)
_HpnicfevtModuleSw_LSQ1GP24TSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TSC3 = _HpnicfevtModuleSw_LSQ1GP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 624)
)
_HpnicfevtModuleSw_LSQ1GP48SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48SC3 = _HpnicfevtModuleSw_LSQ1GP48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 625)
)
_HpnicfevtModuleSw_LSQ1GV48SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV48SC3 = _HpnicfevtModuleSw_LSQ1GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 626)
)
_HpnicfevtModuleSw_LSQ1MPUA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUA3 = _HpnicfevtModuleSw_LSQ1MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 627)
)
_HpnicfevtModuleSw_LSQ1SRP1CB3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRP1CB3 = _HpnicfevtModuleSw_LSQ1SRP1CB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 628)
)
_HpnicfevtModuleSw_LSQ1SRPA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPA3 = _HpnicfevtModuleSw_LSQ1SRPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 629)
)
_HpnicfevtModuleSw_LSQ2FP48SA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2FP48SA3 = _HpnicfevtModuleSw_LSQ2FP48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 630)
)
_HpnicfevtModuleSw_LSQ2FT48SA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2FT48SA3 = _HpnicfevtModuleSw_LSQ2FT48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 631)
)
_HpnicfevtModuleSw_LSQ1MPUB3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUB3 = _HpnicfevtModuleSw_LSQ1MPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 632)
)
_HpnicfevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGP24TSC3 = _HpnicfevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 633)
)
_HpnicfevtModuleSw_LSQ1MPUB4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1MPUB4 = _HpnicfevtModuleSw_LSQ1MPUB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 634)
)
_HpnicfevtModuleSw_LSQ1SRPD4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPD4 = _HpnicfevtModuleSw_LSQ1SRPD4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 635)
)
_HpnicfevtModuleSw_LSQ1SSLSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SSLSC0 = _HpnicfevtModuleSw_LSQ1SSLSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 636)
)
_HpnicfevtModuleSw_LSQ1LBSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1LBSC0 = _HpnicfevtModuleSw_LSQ1LBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 637)
)
_HpnicfevtModuleSw_LSQ1NAT24SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1NAT24SC0 = _HpnicfevtModuleSw_LSQ1NAT24SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 638)
)
_HpnicfevtModuleSw_LSQ1SRP12GB4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRP12GB4 = _HpnicfevtModuleSw_LSQ1SRP12GB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 639)
)
_HpnicfevtModuleSw_LSQ1TGS8SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS8SC0 = _HpnicfevtModuleSw_LSQ1TGS8SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 640)
)
_HpnicfevtModuleSw_LSQ3PT4PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ3PT4PSC0 = _HpnicfevtModuleSw_LSQ3PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 641)
)
_HpnicfevtModuleSw_EWPXM2MPUB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2MPUB0 = _HpnicfevtModuleSw_EWPXM2MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 642)
)
_HpnicfevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2SRP12GB0 = _HpnicfevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 643)
)
_HpnicfevtModuleSw_EWPXM2SRPD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2SRPD0 = _HpnicfevtModuleSw_EWPXM2SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 644)
)
_HpnicfevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2GP24TSD0 = _HpnicfevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 645)
)
_HpnicfevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2GP24TXSD0 = _HpnicfevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 646)
)
_HpnicfevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2TGX4SD0 = _HpnicfevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 647)
)
_HpnicfevtModuleSw_EWPXM2GP48SD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2GP48SD0 = _HpnicfevtModuleSw_EWPXM2GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 648)
)
_HpnicfevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2GP24TSC0 = _HpnicfevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 649)
)
_HpnicfevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2TGX2SC0 = _HpnicfevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 650)
)
_HpnicfevtModuleSw_EWPXM2GP48SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPXM2GP48SC0 = _HpnicfevtModuleSw_EWPXM2GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 651)
)
_HpnicfevtModuleSw_LS7500_GP48_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_GP48_SC = _HpnicfevtModuleSw_LS7500_GP48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 652)
)
_HpnicfevtModuleSw_LS7500_GP48_SD_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_GP48_SD = _HpnicfevtModuleSw_LS7500_GP48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 653)
)
_HpnicfevtModuleSw_LS7500_GT48_SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_GT48_SC = _HpnicfevtModuleSw_LS7500_GT48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 654)
)
_HpnicfevtModuleSw_LS7500_GT48_SD_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_GT48_SD = _HpnicfevtModuleSw_LS7500_GT48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 655)
)
_HpnicfevtModuleSw_LS7500_SRPG1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_SRPG1 = _HpnicfevtModuleSw_LS7500_SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 656)
)
_HpnicfevtModuleSw_LS7500_SRPG2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_SRPG2 = _HpnicfevtModuleSw_LS7500_SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 657)
)
_HpnicfevtModuleSw_LS7500_XP4_SD_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_XP4_SD = _HpnicfevtModuleSw_LS7500_XP4_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 658)
)
_HpnicfevtModuleSw_LS7500_XP8_SD_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS7500_XP8_SD = _HpnicfevtModuleSw_LS7500_XP8_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 659)
)
_HpnicfevtModuleSw_LSQ4PT4PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ4PT4PSC0 = _HpnicfevtModuleSw_LSQ4PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 660)
)
_HpnicfevtModuleSw_LSQ4PT8PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ4PT8PSC0 = _HpnicfevtModuleSw_LSQ4PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 661)
)
_HpnicfevtModuleSw_LSQ4PT16PSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ4PT16PSC0 = _HpnicfevtModuleSw_LSQ4PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 662)
)
_HpnicfevtModuleSw_LSQ1GP24TSA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TSA0 = _HpnicfevtModuleSw_LSQ1GP24TSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 663)
)
_HpnicfevtModuleSw_LSQ1GV24PSA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GV24PSA0 = _HpnicfevtModuleSw_LSQ1GV24PSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 664)
)
_HpnicfevtModuleSw_LSQ1SRPD3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPD3 = _HpnicfevtModuleSw_LSQ1SRPD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 665)
)
_HpnicfevtModuleSw_LSQ1SUPA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SUPA0 = _HpnicfevtModuleSw_LSQ1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 666)
)
_HpnicfevtModuleSw_LSU1FAB04A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB04A0 = _HpnicfevtModuleSw_LSU1FAB04A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 667)
)
_HpnicfevtModuleSw_LSU1FAB08A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB08A0 = _HpnicfevtModuleSw_LSU1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 668)
)
_HpnicfevtModuleSw_LSU1TGS8EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS8EA0 = _HpnicfevtModuleSw_LSU1TGS8EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 669)
)
_HpnicfevtModuleSw_LSU1TGS8EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS8EB0 = _HpnicfevtModuleSw_LSU1TGS8EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 670)
)
_HpnicfevtModuleSw_LSU1TGS8SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS8SE0 = _HpnicfevtModuleSw_LSU1TGS8SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 671)
)
_HpnicfevtModuleSw_LSUTGS16SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSUTGS16SC0 = _HpnicfevtModuleSw_LSUTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 672)
)
_HpnicfevtModuleSw_LSU1SUPA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1SUPA0 = _HpnicfevtModuleSw_LSU1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 673)
)
_HpnicfevtModuleSw_LSU1GP24TXEA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP24TXEA0 = _HpnicfevtModuleSw_LSU1GP24TXEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 674)
)
_HpnicfevtModuleSw_LSU1GP24TXEB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP24TXEB0 = _HpnicfevtModuleSw_LSU1GP24TXEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 675)
)
_HpnicfevtModuleSw_LSU1GP24TXSE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP24TXSE0 = _HpnicfevtModuleSw_LSU1GP24TXSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 676)
)
_HpnicfevtModuleSw_LSU1GP48EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP48EA0 = _HpnicfevtModuleSw_LSU1GP48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 677)
)
_HpnicfevtModuleSw_LSU1GP48EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP48EB0 = _HpnicfevtModuleSw_LSU1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 678)
)
_HpnicfevtModuleSw_LSU1GP48SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP48SE0 = _HpnicfevtModuleSw_LSU1GP48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 679)
)
_HpnicfevtModuleSw_LSU1GT48EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GT48EA0 = _HpnicfevtModuleSw_LSU1GT48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 680)
)
_HpnicfevtModuleSw_LSU1GT48SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GT48SE0 = _HpnicfevtModuleSw_LSU1GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 681)
)
_HpnicfevtModuleSw_LSU1TGX4EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGX4EA0 = _HpnicfevtModuleSw_LSU1TGX4EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 682)
)
_HpnicfevtModuleSw_LSU1TGX4EB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGX4EB0 = _HpnicfevtModuleSw_LSU1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 683)
)
_HpnicfevtModuleSw_LSU1TGX4SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGX4SE0 = _HpnicfevtModuleSw_LSU1TGX4SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 684)
)
_HpnicfevtModuleSw_LSQ1FAB08A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB08A0 = _HpnicfevtModuleSw_LSQ1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 685)
)
_HpnicfevtModuleSw_EWPX2WCMD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX2WCMD0 = _HpnicfevtModuleSw_EWPX2WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 686)
)
_HpnicfevtModuleSw_LSQ1WCMD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1WCMD0 = _HpnicfevtModuleSw_LSQ1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 687)
)
_HpnicfevtModuleSw_LSQ1IAGSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1IAGSC0 = _HpnicfevtModuleSw_LSQ1IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 688)
)
_HpnicfevtModuleSw_LSU1GP24TSE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP24TSE0 = _HpnicfevtModuleSw_LSU1GP24TSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 689)
)
_HpnicfevtModuleSw_LSQ1TGS16SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS16SC0 = _HpnicfevtModuleSw_LSQ1TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 690)
)
_HpnicfevtModuleSw_EWPX2TGS16SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX2TGS16SC0 = _HpnicfevtModuleSw_EWPX2TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 691)
)
_HpnicfevtModuleSw_LSQ1SUPA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SUPA3 = _HpnicfevtModuleSw_LSQ1SUPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 692)
)
_HpnicfevtModuleSw_LSQ1FAB04A3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB04A3 = _HpnicfevtModuleSw_LSQ1FAB04A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 693)
)
_HpnicfevtModuleSw_LSQ1FAB08A3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB08A3 = _HpnicfevtModuleSw_LSQ1FAB08A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 694)
)
_HpnicfevtModuleSw_LSQ1GT48SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GT48SC0 = _HpnicfevtModuleSw_LSQ1GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 695)
)
_HpnicfevtModuleSw_LSR2SRP2C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2SRP2C1 = _HpnicfevtModuleSw_LSR2SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 696)
)
_HpnicfevtModuleSw_LSR2SRP2C2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2SRP2C2 = _HpnicfevtModuleSw_LSR2SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 697)
)
_HpnicfevtModuleSw_1000BASE_X_COMBO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_X_COMBO = _HpnicfevtModuleSw_1000BASE_X_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 701)
)
_HpnicfevtModuleSw_EPON_1000M_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EPON_1000M = _HpnicfevtModuleSw_EPON_1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 702)
)
_HpnicfevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45 = _HpnicfevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 703)
)
_HpnicfevtModuleSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_1550_BIDI = _HpnicfevtModuleSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 704)
)
_HpnicfevtModuleSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_100M_1310_BIDI = _HpnicfevtModuleSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 705)
)
_HpnicfevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO = _HpnicfevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 706)
)
_HpnicfevtModuleSw_LSH1PK2T_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSH1PK2T = _HpnicfevtModuleSw_LSH1PK2T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 707)
)
_HpnicfevtModuleSw_LSPM2GP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM2GP2P = _HpnicfevtModuleSw_LSPM2GP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 708)
)
_HpnicfevtModuleSw_LSWM1GT16P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1GT16P = _HpnicfevtModuleSw_LSWM1GT16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 709)
)
_HpnicfevtModuleSw_LSWM1GP16P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1GP16P = _HpnicfevtModuleSw_LSWM1GP16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 710)
)
_HpnicfevtModuleSw_LSWM1XP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1XP2P = _HpnicfevtModuleSw_LSWM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 711)
)
_HpnicfevtModuleSw_LSWM1XP4P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1XP4P = _HpnicfevtModuleSw_LSWM1XP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 712)
)
_HpnicfevtModuleSw_LSWM1SP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1SP2P = _HpnicfevtModuleSw_LSWM1SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 713)
)
_HpnicfevtModuleSw_LSWM1SP4P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1SP4P = _HpnicfevtModuleSw_LSWM1SP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 714)
)
_HpnicfevtModuleSw_LSWM148POEM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM148POEM = _HpnicfevtModuleSw_LSWM148POEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 715)
)
_HpnicfevtModuleSw_LSWM1FW10_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1FW10 = _HpnicfevtModuleSw_LSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 716)
)
_HpnicfevtModuleSw_LSWM1WCM10_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1WCM10 = _HpnicfevtModuleSw_LSWM1WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 717)
)
_HpnicfevtModuleSw_LSWM1IPS10_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1IPS10 = _HpnicfevtModuleSw_LSWM1IPS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 718)
)
_HpnicfevtModuleSw_LSWM1WCM20_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1WCM20 = _HpnicfevtModuleSw_LSWM1WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 719)
)
_HpnicfevtModuleSw_IPS_T1000_M_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IPS_T1000_M = _HpnicfevtModuleSw_IPS_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 720)
)
_HpnicfevtModuleSw_IPS_T1000_A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IPS_T1000_A = _HpnicfevtModuleSw_IPS_T1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 721)
)
_HpnicfevtModuleSw_IPS_T1000_S_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IPS_T1000_S = _HpnicfevtModuleSw_IPS_T1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 722)
)
_HpnicfevtModuleSw_IPS_GX4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IPS_GX4C = _HpnicfevtModuleSw_IPS_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 723)
)
_HpnicfevtModuleSw_IPS_GT4C_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IPS_GT4C = _HpnicfevtModuleSw_IPS_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 724)
)
_HpnicfevtModuleSw_LSPM2SP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM2SP2P = _HpnicfevtModuleSw_LSPM2SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 725)
)
_HpnicfevtModuleSw_LSPM2SP2PA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM2SP2PA = _HpnicfevtModuleSw_LSPM2SP2PA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 726)
)
_HpnicfevtModuleSw_LSP5GP8P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSP5GP8P = _HpnicfevtModuleSw_LSP5GP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 727)
)
_HpnicfevtModuleSw_LSP5GT8P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSP5GT8P = _HpnicfevtModuleSw_LSP5GT8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 728)
)
_HpnicfevtModuleSw_LSWM1FC4P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM1FC4P = _HpnicfevtModuleSw_LSWM1FC4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 729)
)
_HpnicfevtModuleSw_LSW1XGT4P0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSW1XGT4P0 = _HpnicfevtModuleSw_LSW1XGT4P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 730)
)
_HpnicfevtModuleSw_LSW1XGT2P0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSW1XGT2P0 = _HpnicfevtModuleSw_LSW1XGT2P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 731)
)
_HpnicfevtModuleSw_LSP1XGT2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSP1XGT2P = _HpnicfevtModuleSw_LSP1XGT2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 732)
)
_HpnicfevtModuleSw_LSPM3XGT2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSPM3XGT2P = _HpnicfevtModuleSw_LSPM3XGT2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 733)
)
_HpnicfevtModuleSw_LSWM2QP2P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM2QP2P = _HpnicfevtModuleSw_LSWM2QP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 734)
)
_HpnicfevtModuleSw_LSWM2XGT2PM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM2XGT2PM = _HpnicfevtModuleSw_LSWM2XGT2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 735)
)
_HpnicfevtModuleSw_LSWM2SP2PM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM2SP2PM = _HpnicfevtModuleSw_LSWM2SP2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 736)
)
_HpnicfevtModuleSw_LSWM2SP8PM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM2SP8PM = _HpnicfevtModuleSw_LSWM2SP8PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 737)
)
_HpnicfevtModuleSw_LSWM2SP8P_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM2SP8P = _HpnicfevtModuleSw_LSWM2SP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 738)
)
_HpnicfevtModuleSw_LSWM2XGT8PM_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM2XGT8PM = _HpnicfevtModuleSw_LSWM2XGT8PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 739)
)
_HpnicfevtModuleSw_LSWM18QC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM18QC = _HpnicfevtModuleSw_LSWM18QC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 740)
)
_HpnicfevtModuleSw_LSWM124XG2Q_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM124XG2Q = _HpnicfevtModuleSw_LSWM124XG2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 741)
)
_HpnicfevtModuleSw_LSWM124XGT2Q_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM124XGT2Q = _HpnicfevtModuleSw_LSWM124XGT2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 742)
)
_HpnicfevtModuleSw_LSWM124XG2QL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSWM124XG2QL = _HpnicfevtModuleSw_LSWM124XG2QL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 743)
)
_HpnicfevtModuleSw_WX5002MPU_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_WX5002MPU = _HpnicfevtModuleSw_WX5002MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 800)
)
_HpnicfevtModuleSw_LS8M1WCMA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LS8M1WCMA = _HpnicfevtModuleSw_LS8M1WCMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 801)
)
_HpnicfevtModuleSw_EWPX1G24XA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1G24XA0 = _HpnicfevtModuleSw_EWPX1G24XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 802)
)
_HpnicfevtModuleSw_LSQ1WCMB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1WCMB0 = _HpnicfevtModuleSw_LSQ1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 803)
)
_HpnicfevtModuleSw_LSB1WCM2A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSB1WCM2A0 = _HpnicfevtModuleSw_LSB1WCM2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 804)
)
_HpnicfevtModuleSw_EWPX1WCMB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WCMB0 = _HpnicfevtModuleSw_EWPX1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 805)
)
_HpnicfevtModuleSw_EWPX1G24XC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1G24XC0 = _HpnicfevtModuleSw_EWPX1G24XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 806)
)
_HpnicfevtModuleSw_EWPX1WCMC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WCMC0 = _HpnicfevtModuleSw_EWPX1WCMC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 807)
)
_HpnicfevtModuleSw_EWPX1FWA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1FWA0 = _HpnicfevtModuleSw_EWPX1FWA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 808)
)
_HpnicfevtModuleSw_EWPX1G10XC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1G10XC0 = _HpnicfevtModuleSw_EWPX1G10XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 809)
)
_HpnicfevtModuleSw_EWPX1WCM10C0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WCM10C0 = _HpnicfevtModuleSw_EWPX1WCM10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 810)
)
_HpnicfevtModuleSw_LSR1WCM2A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1WCM2A1 = _HpnicfevtModuleSw_LSR1WCM2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 811)
)
_HpnicfevtModuleSw_EWPX1WAP0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WAP0 = _HpnicfevtModuleSw_EWPX1WAP0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 812)
)
_HpnicfevtModuleSw_EWPX1WCMD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WCMD0 = _HpnicfevtModuleSw_EWPX1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 813)
)
_HpnicfevtModuleSw_EWPX1G24XCE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1G24XCE0 = _HpnicfevtModuleSw_EWPX1G24XCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 814)
)
_HpnicfevtModuleSw_EWPX1WCMCE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WCMCE0 = _HpnicfevtModuleSw_EWPX1WCMCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 815)
)
_HpnicfevtModuleSw_EWPX1G24XD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1G24XD0 = _HpnicfevtModuleSw_EWPX1G24XD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 816)
)
_HpnicfevtModuleSw_LSR1DRSP2L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1DRSP2L1 = _HpnicfevtModuleSw_LSR1DRSP2L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 900)
)
_HpnicfevtModuleSw_PIC_CLF2G8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PIC_CLF2G8L = _HpnicfevtModuleSw_PIC_CLF2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 901)
)
_HpnicfevtModuleSw_PIC_CLF4G8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_PIC_CLF4G8L = _HpnicfevtModuleSw_PIC_CLF4G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 902)
)
_HpnicfevtModuleSw_SR02SRP2F3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRP2F3 = _HpnicfevtModuleSw_SR02SRP2F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 903)
)
_HpnicfevtModuleSw_SR02SRP1F3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRP1F3 = _HpnicfevtModuleSw_SR02SRP1F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 904)
)
_HpnicfevtModuleSw_LST1GT48LEA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GT48LEA1 = _HpnicfevtModuleSw_LST1GT48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 905)
)
_HpnicfevtModuleSw_LST1GP48LEA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEA1 = _HpnicfevtModuleSw_LST1GP48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 906)
)
_HpnicfevtModuleSw_LST2XP8LEA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP8LEA1 = _HpnicfevtModuleSw_LST2XP8LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 907)
)
_HpnicfevtModuleSw_LST1GT48LEY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GT48LEY1 = _HpnicfevtModuleSw_LST1GT48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 908)
)
_HpnicfevtModuleSw_LST1GP48LEY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEY1 = _HpnicfevtModuleSw_LST1GP48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 909)
)
_HpnicfevtModuleSw_LST1XP32REY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP32REY1 = _HpnicfevtModuleSw_LST1XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 910)
)
_HpnicfevtModuleSw_LST1XP8LEY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP8LEY1 = _HpnicfevtModuleSw_LST1XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 911)
)
_HpnicfevtModuleSw_LST1GP48LEZ1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEZ1 = _HpnicfevtModuleSw_LST1GP48LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 912)
)
_HpnicfevtModuleSw_LST1XP8LEZ1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP8LEZ1 = _HpnicfevtModuleSw_LST1XP8LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 913)
)
_HpnicfevtModuleSw_IM_FW_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_FW_II = _HpnicfevtModuleSw_IM_FW_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 914)
)
_HpnicfevtModuleSw_IM_IPS_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_IPS = _HpnicfevtModuleSw_IM_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 915)
)
_HpnicfevtModuleSw_IM_SSL_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_SSL = _HpnicfevtModuleSw_IM_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 916)
)
_HpnicfevtModuleSw_IM_LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_LB = _HpnicfevtModuleSw_IM_LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 917)
)
_HpnicfevtModuleSw_IM_ACG_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_IM_ACG = _HpnicfevtModuleSw_IM_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 918)
)
_HpnicfevtModuleSw_LSR1XP16REC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1XP16REC1 = _HpnicfevtModuleSw_LSR1XP16REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 919)
)
_HpnicfevtModuleSw_LST2XP8LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP8LEB1 = _HpnicfevtModuleSw_LST2XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 920)
)
_HpnicfevtModuleSw_LST2XP8LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP8LEC1 = _HpnicfevtModuleSw_LST2XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 921)
)
_HpnicfevtModuleSw_LST2XP8LEF1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP8LEF1 = _HpnicfevtModuleSw_LST2XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 922)
)
_HpnicfevtModuleSw_LSR2XP4LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2XP4LEB1 = _HpnicfevtModuleSw_LSR2XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 923)
)
_HpnicfevtModuleSw_LSR2XP4LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2XP4LEC1 = _HpnicfevtModuleSw_LSR2XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 924)
)
_HpnicfevtModuleSw_LST2XP32REB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP32REB1 = _HpnicfevtModuleSw_LST2XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 925)
)
_HpnicfevtModuleSw_LST2XP32REC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP32REC1 = _HpnicfevtModuleSw_LST2XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 926)
)
_HpnicfevtModuleSw_LSR1WCM3A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR1WCM3A1 = _HpnicfevtModuleSw_LSR1WCM3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 927)
)
_HpnicfevtModuleSw_LST1XP16LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP16LEB1 = _HpnicfevtModuleSw_LST1XP16LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 928)
)
_HpnicfevtModuleSw_LST1XP16LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP16LEC1 = _HpnicfevtModuleSw_LST1XP16LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 929)
)
_HpnicfevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP4L_E_I = _HpnicfevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 930)
)
_HpnicfevtModuleSw_LST2MRPNC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2MRPNC1 = _HpnicfevtModuleSw_LST2MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 931)
)
_HpnicfevtModuleSw_LST2SF08C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2SF08C1 = _HpnicfevtModuleSw_LST2SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 932)
)
_HpnicfevtModuleSw_LST2SF18C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2SF18C1 = _HpnicfevtModuleSw_LST2SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 933)
)
_HpnicfevtModuleSw_SR02SRP2G3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR02SRP2G3 = _HpnicfevtModuleSw_SR02SRP2G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 934)
)
_HpnicfevtModuleSw_CR_SPE_3020_E_I_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPE_3020_E_I = _HpnicfevtModuleSw_CR_SPE_3020_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 935)
)
_HpnicfevtModuleSw_CR_SPC_PUP4L_E_I_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_PUP4L_E_I = _HpnicfevtModuleSw_CR_SPC_PUP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 936)
)
_HpnicfevtModuleSw_CR_SPC_XP4LEF_I_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP4LEF_I = _HpnicfevtModuleSw_CR_SPC_XP4LEF_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 937)
)
_HpnicfevtModuleSw_CR_SPC_XP8LEF_I_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP8LEF_I = _HpnicfevtModuleSw_CR_SPC_XP8LEF_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 938)
)
_HpnicfevtModuleSw_LST3XP8LEB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST3XP8LEB1 = _HpnicfevtModuleSw_LST3XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 939)
)
_HpnicfevtModuleSw_LST3XP8LEC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST3XP8LEC1 = _HpnicfevtModuleSw_LST3XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 940)
)
_HpnicfevtModuleSw_LST1FW3A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1FW3A1 = _HpnicfevtModuleSw_LST1FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 941)
)
_HpnicfevtModuleSw_CR_IM_NAM1A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_IM_NAM1A = _HpnicfevtModuleSw_CR_IM_NAM1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 942)
)
_HpnicfevtModuleSw_LSR2SRP2B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2SRP2B1 = _HpnicfevtModuleSw_LSR2SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 943)
)
_HpnicfevtModuleSw_LSR2SRP2B2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2SRP2B2 = _HpnicfevtModuleSw_LSR2SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 944)
)
_HpnicfevtModuleSw_LSR2SRP2D1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSR2SRP2D1 = _HpnicfevtModuleSw_LSR2SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 945)
)
_HpnicfevtModuleSw_LST3XP8LEY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST3XP8LEY1 = _HpnicfevtModuleSw_LST3XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 946)
)
_HpnicfevtModuleSw_LST2XP32REY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP32REY1 = _HpnicfevtModuleSw_LST2XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 947)
)
_HpnicfevtModuleSw_LST1XP16LEY1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP16LEY1 = _HpnicfevtModuleSw_LST1XP16LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 948)
)
_HpnicfevtModuleSw_SR0M2SRP2G3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR0M2SRP2G3 = _HpnicfevtModuleSw_SR0M2SRP2G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 949)
)
_HpnicfevtModuleSw_SR0M2SRP1G3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR0M2SRP1G3 = _HpnicfevtModuleSw_SR0M2SRP1G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 950)
)
_HpnicfevtModuleSw_SPC_GP48LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP48LA = _HpnicfevtModuleSw_SPC_GP48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 951)
)
_HpnicfevtModuleSw_SPC_GT48LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GT48LA = _HpnicfevtModuleSw_SPC_GT48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 952)
)
_HpnicfevtModuleSw_SPC_XP4LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP4LA = _HpnicfevtModuleSw_SPC_XP4LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 953)
)
_HpnicfevtModuleSw_SPC_XP2LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP2LA = _HpnicfevtModuleSw_SPC_XP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 954)
)
_HpnicfevtModuleSw_SPC_GP24LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP24LA = _HpnicfevtModuleSw_SPC_GP24LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 955)
)
_HpnicfevtModuleSw_SPC_XP16RA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP16RA = _HpnicfevtModuleSw_SPC_XP16RA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 956)
)
_HpnicfevtModuleSw_CR_IM_FW1A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_IM_FW1A = _HpnicfevtModuleSw_CR_IM_FW1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 957)
)
_HpnicfevtModuleSw_SPC_XP16R_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP16R = _HpnicfevtModuleSw_SPC_XP16R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 958)
)
_HpnicfevtModuleSw_CR_IM_LB1A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_IM_LB1A = _HpnicfevtModuleSw_CR_IM_LB1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 959)
)
_HpnicfevtModuleSw_LST1GT48LEC2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GT48LEC2 = _HpnicfevtModuleSw_LST1GT48LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 960)
)
_HpnicfevtModuleSw_LST1GP48LEC2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1GP48LEC2 = _HpnicfevtModuleSw_LST1GP48LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 961)
)
_HpnicfevtModuleSw_LST1XP16LEC2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP16LEC2 = _HpnicfevtModuleSw_LST1XP16LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 962)
)
_HpnicfevtModuleSw_LST2XP8LEC2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP8LEC2 = _HpnicfevtModuleSw_LST2XP8LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 963)
)
_HpnicfevtModuleSw_LST2XP32REC2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2XP32REC2 = _HpnicfevtModuleSw_LST2XP32REC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 964)
)
_HpnicfevtModuleSw_CR_IM_MAC1A_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_IM_MAC1A = _HpnicfevtModuleSw_CR_IM_MAC1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 965)
)
_HpnicfevtModuleSw_LST1XP48LFD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP48LFD1 = _HpnicfevtModuleSw_LST1XP48LFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 966)
)
_HpnicfevtModuleSw_LST1XP40RFD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP40RFD1 = _HpnicfevtModuleSw_LST1XP40RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 967)
)
_HpnicfevtModuleSw_LST1XP40RFG1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP40RFG1 = _HpnicfevtModuleSw_LST1XP40RFG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 968)
)
_HpnicfevtModuleSw_LST1XLP16RFD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XLP16RFD1 = _HpnicfevtModuleSw_LST1XLP16RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 969)
)
_HpnicfevtModuleSw_LST1CP4RFD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1CP4RFD1 = _HpnicfevtModuleSw_LST1CP4RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 970)
)
_HpnicfevtModuleSw_LST1CP4RFG1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1CP4RFG1 = _HpnicfevtModuleSw_LST1CP4RFG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 971)
)
_HpnicfevtModuleSw_LST1SF08E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1SF08E1 = _HpnicfevtModuleSw_LST1SF08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 972)
)
_HpnicfevtModuleSw_LST1SF18E1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1SF18E1 = _HpnicfevtModuleSw_LST1SF18E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 973)
)
_HpnicfevtModuleSw_LST1MRPNE1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1MRPNE1 = _HpnicfevtModuleSw_LST1MRPNE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 974)
)
_HpnicfevtModuleSw_LSX1CGX8FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1CGX8FC0 = _HpnicfevtModuleSw_LSX1CGX8FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 975)
)
_HpnicfevtModuleSw_LSX1CGX8FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1CGX8FC1 = _HpnicfevtModuleSw_LSX1CGX8FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 976)
)
_HpnicfevtModuleSw_LSX1QGS24FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS24FC0 = _HpnicfevtModuleSw_LSX1QGS24FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 977)
)
_HpnicfevtModuleSw_LSX1QGS24FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS24FC1 = _HpnicfevtModuleSw_LSX1QGS24FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 978)
)
_HpnicfevtModuleSw_LSX1TGS24FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS24FC0 = _HpnicfevtModuleSw_LSX1TGS24FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 979)
)
_HpnicfevtModuleSw_LSX1TGS24FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS24FC1 = _HpnicfevtModuleSw_LSX1TGS24FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 980)
)
_HpnicfevtModuleSw_LSX1TGS48FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48FC0 = _HpnicfevtModuleSw_LSX1TGS48FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 981)
)
_HpnicfevtModuleSw_LSX1TGS48FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48FC1 = _HpnicfevtModuleSw_LSX1TGS48FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 982)
)
_HpnicfevtModuleSw_LST1XP48LFD2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP48LFD2 = _HpnicfevtModuleSw_LST1XP48LFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 983)
)
_HpnicfevtModuleSw_LST1XP40RFD2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP40RFD2 = _HpnicfevtModuleSw_LST1XP40RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 984)
)
_HpnicfevtModuleSw_LST1XP40RFG2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP40RFG2 = _HpnicfevtModuleSw_LST1XP40RFG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 985)
)
_HpnicfevtModuleSw_LST1XLP16RFD2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XLP16RFD2 = _HpnicfevtModuleSw_LST1XLP16RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 986)
)
_HpnicfevtModuleSw_LST1CP4RFD2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1CP4RFD2 = _HpnicfevtModuleSw_LST1CP4RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 987)
)
_HpnicfevtModuleSw_LST1CP4RFG2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1CP4RFG2 = _HpnicfevtModuleSw_LST1CP4RFG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 988)
)
_HpnicfevtModuleSw_MPE_1004_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MPE_1004 = _HpnicfevtModuleSw_MPE_1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 989)
)
_HpnicfevtModuleSw_MIC_GP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_GP4L = _HpnicfevtModuleSw_MIC_GP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 990)
)
_HpnicfevtModuleSw_MIC_GP8L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_GP8L = _HpnicfevtModuleSw_MIC_GP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 991)
)
_HpnicfevtModuleSw_MIC_SP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_SP4L = _HpnicfevtModuleSw_MIC_SP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 992)
)
_HpnicfevtModuleSw_MIC_ET16L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_ET16L = _HpnicfevtModuleSw_MIC_ET16L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 993)
)
_HpnicfevtModuleSw_MIC_CLP4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_CLP4L = _HpnicfevtModuleSw_MIC_CLP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 994)
)
_HpnicfevtModuleSw_MIC_CLP2L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_CLP2L = _HpnicfevtModuleSw_MIC_CLP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 995)
)
_HpnicfevtModuleSw_LST1IPS2A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1IPS2A1 = _HpnicfevtModuleSw_LST1IPS2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 996)
)
_HpnicfevtModuleSw_SFC_04B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_04B = _HpnicfevtModuleSw_SFC_04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 997)
)
_HpnicfevtModuleSw_SFC_04D_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_04D = _HpnicfevtModuleSw_SFC_04D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 998)
)
_HpnicfevtModuleSw_SFC_08B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_08B = _HpnicfevtModuleSw_SFC_08B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 999)
)
_HpnicfevtModuleSw_SFC_08D_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_08D = _HpnicfevtModuleSw_SFC_08D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1000)
)
_HpnicfevtModuleSw_SFC_12B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_12B = _HpnicfevtModuleSw_SFC_12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1001)
)
_HpnicfevtModuleSw_SFC_12D_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_12D = _HpnicfevtModuleSw_SFC_12D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1002)
)
_HpnicfevtModuleSw_SR05SRP1H1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR05SRP1H1 = _HpnicfevtModuleSw_SR05SRP1H1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1003)
)
_HpnicfevtModuleSw_SPC_GP24LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP24LA1 = _HpnicfevtModuleSw_SPC_GP24LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1004)
)
_HpnicfevtModuleSw_SPC_GP24XP2LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP24XP2LA = _HpnicfevtModuleSw_SPC_GP24XP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1005)
)
_HpnicfevtModuleSw_SPC_GP48LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP48LA1 = _HpnicfevtModuleSw_SPC_GP48LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1006)
)
_HpnicfevtModuleSw_SPC_GP48LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP48LB = _HpnicfevtModuleSw_SPC_GP48LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1007)
)
_HpnicfevtModuleSw_SPC_XP2LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP2LA1 = _HpnicfevtModuleSw_SPC_XP2LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1008)
)
_HpnicfevtModuleSw_SPC_XP4LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP4LA1 = _HpnicfevtModuleSw_SPC_XP4LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1009)
)
_HpnicfevtModuleSw_SPC_XP4LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP4LB = _HpnicfevtModuleSw_SPC_XP4LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1010)
)
_HpnicfevtModuleSw_SPC_XP8LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP8LA = _HpnicfevtModuleSw_SPC_XP8LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1011)
)
_HpnicfevtModuleSw_SPC_XP8LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP8LB = _HpnicfevtModuleSw_SPC_XP8LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1012)
)
_HpnicfevtModuleSw_SPC_XP48LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP48LA = _HpnicfevtModuleSw_SPC_XP48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1013)
)
_HpnicfevtModuleSw_SPC_XLP8LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XLP8LA = _HpnicfevtModuleSw_SPC_XLP8LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1014)
)
_HpnicfevtModuleSw_SPC_GP24XP2LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP24XP2LB = _HpnicfevtModuleSw_SPC_GP24XP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1015)
)
_HpnicfevtModuleSw_LST1MRPNE2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1MRPNE2 = _HpnicfevtModuleSw_LST1MRPNE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1016)
)
_HpnicfevtModuleSw_LST2FW3A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST2FW3A1 = _HpnicfevtModuleSw_LST2FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1017)
)
_HpnicfevtModuleSw_LST1ADE1A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1ADE1A1 = _HpnicfevtModuleSw_LST1ADE1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1018)
)
_HpnicfevtModuleSw_CR_MRP_II_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_MRP_II = _HpnicfevtModuleSw_CR_MRP_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1019)
)
_HpnicfevtModuleSw_CR_SF08E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SF08E = _HpnicfevtModuleSw_CR_SF08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1020)
)
_HpnicfevtModuleSw_CR_SF18E_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SF18E = _HpnicfevtModuleSw_CR_SF18E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1021)
)
_HpnicfevtModuleSw_CR_SPC_XP40RC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP40RC = _HpnicfevtModuleSw_CR_SPC_XP40RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1022)
)
_HpnicfevtModuleSw_CR_SPC_XP40RB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP40RB = _HpnicfevtModuleSw_CR_SPC_XP40RB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1023)
)
_HpnicfevtModuleSw_CR_SPC_CP4RC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_CP4RC = _HpnicfevtModuleSw_CR_SPC_CP4RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1024)
)
_HpnicfevtModuleSw_LST1FW3C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1FW3C1 = _HpnicfevtModuleSw_LST1FW3C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1025)
)
_HpnicfevtModuleSw_LSU1FWCEA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FWCEA0 = _HpnicfevtModuleSw_LSU1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1026)
)
_HpnicfevtModuleSw_SPC_GT48LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GT48LA1 = _HpnicfevtModuleSw_SPC_GT48LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1027)
)
_HpnicfevtModuleSw_LST1XP20RFD1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP20RFD1 = _HpnicfevtModuleSw_LST1XP20RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1028)
)
_HpnicfevtModuleSw_LST1XP20RFD2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1XP20RFD2 = _HpnicfevtModuleSw_LST1XP20RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1029)
)
_HpnicfevtModuleSw_MPE_1104_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MPE_1104 = _HpnicfevtModuleSw_MPE_1104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1030)
)
_HpnicfevtModuleSw_SPEX_1204_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPEX_1204 = _HpnicfevtModuleSw_SPEX_1204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1031)
)
_HpnicfevtModuleSw_SPC_GP44XP4LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP44XP4LCX = _HpnicfevtModuleSw_SPC_GP44XP4LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1032)
)
_HpnicfevtModuleSw_SPC_GP44XP4LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP44XP4LAX = _HpnicfevtModuleSw_SPC_GP44XP4LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1033)
)
_HpnicfevtModuleSw_SPC_XP24LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP24LCX = _HpnicfevtModuleSw_SPC_XP24LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1034)
)
_HpnicfevtModuleSw_SPC_XP24LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP24LAX = _HpnicfevtModuleSw_SPC_XP24LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1035)
)
_HpnicfevtModuleSw_SPC_XP12LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP12LCX = _HpnicfevtModuleSw_SPC_XP12LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1036)
)
_HpnicfevtModuleSw_SPC_XP12LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP12LAX = _HpnicfevtModuleSw_SPC_XP12LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1037)
)
_HpnicfevtModuleSw_SPC_XLP6LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XLP6LCX = _HpnicfevtModuleSw_SPC_XLP6LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1038)
)
_HpnicfevtModuleSw_SPC_XLP6LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XLP6LAX = _HpnicfevtModuleSw_SPC_XLP6LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1039)
)
_HpnicfevtModuleSw_SPC_CP1LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_CP1LCX = _HpnicfevtModuleSw_SPC_CP1LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1040)
)
_HpnicfevtModuleSw_SPC_CP1LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_CP1LAX = _HpnicfevtModuleSw_SPC_CP1LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1041)
)
_HpnicfevtModuleSw_SPC_CP2LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_CP2LB = _HpnicfevtModuleSw_SPC_CP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1042)
)
_HpnicfevtModuleSw_SPC_CP2LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_CP2LA = _HpnicfevtModuleSw_SPC_CP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1043)
)
_HpnicfevtModuleSw_SR05SRP1L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR05SRP1L1 = _HpnicfevtModuleSw_SR05SRP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1044)
)
_HpnicfevtModuleSw_SR05SRP1L3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR05SRP1L3 = _HpnicfevtModuleSw_SR05SRP1L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1045)
)
_HpnicfevtModuleSw_SFC_04_4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_04_4 = _HpnicfevtModuleSw_SFC_04_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1046)
)
_HpnicfevtModuleSw_SFC_04_3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_04_3 = _HpnicfevtModuleSw_SFC_04_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1047)
)
_HpnicfevtModuleSw_SFC_04_2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_04_2 = _HpnicfevtModuleSw_SFC_04_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1048)
)
_HpnicfevtModuleSw_SFC_04_1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SFC_04_1 = _HpnicfevtModuleSw_SFC_04_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1049)
)
_HpnicfevtModuleSw_LST1NSM2C1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LST1NSM2C1 = _HpnicfevtModuleSw_LST1NSM2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1050)
)
_HpnicfevtModuleSw_CR_SPC_XP20RB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CR_SPC_XP20RB = _HpnicfevtModuleSw_CR_SPC_XP20RB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1051)
)
_HpnicfevtModuleSw_SR07SRPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUA1 = _HpnicfevtModuleSw_SR07SRPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1052)
)
_HpnicfevtModuleSw_SR07SRPUB3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUB3 = _HpnicfevtModuleSw_SR07SRPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1053)
)
_HpnicfevtModuleSw_SR07SRPUC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUC3 = _HpnicfevtModuleSw_SR07SRPUC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1054)
)
_HpnicfevtModuleSw_SR07MPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07MPUA1 = _HpnicfevtModuleSw_SR07MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1055)
)
_HpnicfevtModuleSw_SR07SRPUB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUB1 = _HpnicfevtModuleSw_SR07SRPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1056)
)
_HpnicfevtModuleSw_SR07SRPUC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUC1 = _HpnicfevtModuleSw_SR07SRPUC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1057)
)
_HpnicfevtModuleSw_MIC_MS4L_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_MS4L = _HpnicfevtModuleSw_MIC_MS4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1058)
)
_HpnicfevtModuleSw_SPC_GP44XP4LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP44XP4LC = _HpnicfevtModuleSw_SPC_GP44XP4LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1059)
)
_HpnicfevtModuleSw_SPC_GP44XP4LA_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_GP44XP4LA = _HpnicfevtModuleSw_SPC_GP44XP4LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1060)
)
_HpnicfevtModuleSw_SPC_XLP2XP4LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XLP2XP4LC = _HpnicfevtModuleSw_SPC_XLP2XP4LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1061)
)
_HpnicfevtModuleSw_SPC_XP12LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP12LC = _HpnicfevtModuleSw_SPC_XP12LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1062)
)
_HpnicfevtModuleSw_SPC_CP1LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_CP1LC = _HpnicfevtModuleSw_SPC_CP1LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1063)
)
_HpnicfevtModuleSw_SPC_XP24LC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SPC_XP24LC = _HpnicfevtModuleSw_SPC_XP24LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1064)
)
_HpnicfevtModuleSw_SR07SRPUD3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUD3 = _HpnicfevtModuleSw_SR07SRPUD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1065)
)
_HpnicfevtModuleSw_SR07MPUA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07MPUA3 = _HpnicfevtModuleSw_SR07MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1066)
)
_HpnicfevtModuleSw_MPEX_1304_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MPEX_1304 = _HpnicfevtModuleSw_MPEX_1304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1067)
)
_HpnicfevtModuleSw_MIC_GP10L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_MIC_GP10L1 = _HpnicfevtModuleSw_MIC_GP10L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1068)
)
_HpnicfevtModuleSw_SR07SRPUB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_SR07SRPUB = _HpnicfevtModuleSw_SR07SRPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1069)
)
_HpnicfevtModuleSw_CMPE_1104_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CMPE_1104 = _HpnicfevtModuleSw_CMPE_1104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1070)
)
_HpnicfevtModuleSw_CSFC_04_1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_04_1 = _HpnicfevtModuleSw_CSFC_04_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1071)
)
_HpnicfevtModuleSw_CSFC_04_2_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_04_2 = _HpnicfevtModuleSw_CSFC_04_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1072)
)
_HpnicfevtModuleSw_CSFC_04_3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_04_3 = _HpnicfevtModuleSw_CSFC_04_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1073)
)
_HpnicfevtModuleSw_CSFC_04_4_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_04_4 = _HpnicfevtModuleSw_CSFC_04_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1074)
)
_HpnicfevtModuleSw_CSFC_04B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_04B = _HpnicfevtModuleSw_CSFC_04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1075)
)
_HpnicfevtModuleSw_CSFC_04D_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_04D = _HpnicfevtModuleSw_CSFC_04D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1076)
)
_HpnicfevtModuleSw_CSFC_08B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_08B = _HpnicfevtModuleSw_CSFC_08B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1077)
)
_HpnicfevtModuleSw_CSFC_08D_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_08D = _HpnicfevtModuleSw_CSFC_08D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1078)
)
_HpnicfevtModuleSw_CSFC_12B_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_12B = _HpnicfevtModuleSw_CSFC_12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1079)
)
_HpnicfevtModuleSw_CSFC_12D_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSFC_12D = _HpnicfevtModuleSw_CSFC_12D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1080)
)
_HpnicfevtModuleSw_CSPC_CP1LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_CP1LCX = _HpnicfevtModuleSw_CSPC_CP1LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1081)
)
_HpnicfevtModuleSw_CSPC_CP2LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_CP2LB = _HpnicfevtModuleSw_CSPC_CP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1082)
)
_HpnicfevtModuleSw_CSPC_GP24LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_GP24LA1 = _HpnicfevtModuleSw_CSPC_GP24LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1083)
)
_HpnicfevtModuleSw_CSPC_GP24XP2LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_GP24XP2LB = _HpnicfevtModuleSw_CSPC_GP24XP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1084)
)
_HpnicfevtModuleSw_CSPC_GP44XP4LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_GP44XP4LCX = _HpnicfevtModuleSw_CSPC_GP44XP4LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1085)
)
_HpnicfevtModuleSw_CSPC_GP48LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_GP48LB = _HpnicfevtModuleSw_CSPC_GP48LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1086)
)
_HpnicfevtModuleSw_CSPC_GT48LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_GT48LA1 = _HpnicfevtModuleSw_CSPC_GT48LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1087)
)
_HpnicfevtModuleSw_CSPC_XLP6LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XLP6LCX = _HpnicfevtModuleSw_CSPC_XLP6LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1088)
)
_HpnicfevtModuleSw_CSPC_XP2LA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP2LA1 = _HpnicfevtModuleSw_CSPC_XP2LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1089)
)
_HpnicfevtModuleSw_CSPC_XP4LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP4LB = _HpnicfevtModuleSw_CSPC_XP4LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1090)
)
_HpnicfevtModuleSw_CSPC_XP8LB_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP8LB = _HpnicfevtModuleSw_CSPC_XP8LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1091)
)
_HpnicfevtModuleSw_CSPC_XP12LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP12LAX = _HpnicfevtModuleSw_CSPC_XP12LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1092)
)
_HpnicfevtModuleSw_CSPC_XP12LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP12LCX = _HpnicfevtModuleSw_CSPC_XP12LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1093)
)
_HpnicfevtModuleSw_CSPC_XP24LAX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP24LAX = _HpnicfevtModuleSw_CSPC_XP24LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1094)
)
_HpnicfevtModuleSw_CSPC_XP24LCX_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_XP24LCX = _HpnicfevtModuleSw_CSPC_XP24LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1095)
)
_HpnicfevtModuleSw_CSPC_CSPEX_1204_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSPC_CSPEX_1204 = _HpnicfevtModuleSw_CSPC_CSPEX_1204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1096)
)
_HpnicfevtModuleSw_CSR05SRP1L1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSR05SRP1L1 = _HpnicfevtModuleSw_CSR05SRP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1097)
)
_HpnicfevtModuleSw_CSR05SRP1L3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSR05SRP1L3 = _HpnicfevtModuleSw_CSR05SRP1L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1098)
)
_HpnicfevtModuleSw_CSR07MPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSR07MPUA1 = _HpnicfevtModuleSw_CSR07MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1099)
)
_HpnicfevtModuleSw_CSR07SRPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSR07SRPUA1 = _HpnicfevtModuleSw_CSR07SRPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1100)
)
_HpnicfevtModuleSw_CSR07SRPUB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSR07SRPUB1 = _HpnicfevtModuleSw_CSR07SRPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1101)
)
_HpnicfevtModuleSw_CSR07SRPUC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_CSR07SRPUC1 = _HpnicfevtModuleSw_CSR07SRPUC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1102)
)
_HpnicfevtModuleSw_LSXM1CGX8FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1CGX8FX1 = _HpnicfevtModuleSw_LSXM1CGX8FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1103)
)
_HpnicfevtModuleSw_LSXM1QGS24FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1QGS24FX1 = _HpnicfevtModuleSw_LSXM1QGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1104)
)
_HpnicfevtModuleSw_LSXM1TGS48FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1TGS48FX1 = _HpnicfevtModuleSw_LSXM1TGS48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1105)
)
_HpnicfevtModuleSw_LSXM1QGS12FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1QGS12FX1 = _HpnicfevtModuleSw_LSXM1QGS12FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1106)
)
_HpnicfevtModuleSw_LSXM1TGT48FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1TGT48FX1 = _HpnicfevtModuleSw_LSXM1TGT48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1107)
)
_HpnicfevtModuleSw_LSU1IPSBEA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1IPSBEA0 = _HpnicfevtModuleSw_LSU1IPSBEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1108)
)
_HpnicfevtModuleSw_LSU1QGC4SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGC4SF0 = _HpnicfevtModuleSw_LSU1QGC4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1201)
)
_HpnicfevtModuleSw_LSU1QGS8SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGS8SF0 = _HpnicfevtModuleSw_LSU1QGS8SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1202)
)
_HpnicfevtModuleSw_LSU1TGS48SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS48SF0 = _HpnicfevtModuleSw_LSU1TGS48SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1203)
)
_HpnicfevtModuleSw_LSU1QGS4SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGS4SF0 = _HpnicfevtModuleSw_LSU1QGS4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1204)
)
_HpnicfevtModuleSw_LSU1TGS32SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS32SF0 = _HpnicfevtModuleSw_LSU1TGS32SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1205)
)
_HpnicfevtModuleSw_LSU1FAB08D0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB08D0 = _HpnicfevtModuleSw_LSU1FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1206)
)
_HpnicfevtModuleSw_LSU1FAB04B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB04B0 = _HpnicfevtModuleSw_LSU1FAB04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1207)
)
_HpnicfevtModuleSw_LSU1FAB08B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB08B0 = _HpnicfevtModuleSw_LSU1FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1208)
)
_HpnicfevtModuleSw_LSU1FAB12D0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB12D0 = _HpnicfevtModuleSw_LSU1FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1209)
)
_HpnicfevtModuleSw_LSU1FAB12B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB12B0 = _HpnicfevtModuleSw_LSU1FAB12B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1210)
)
_HpnicfevtModuleSw_LSU1FAB04D0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB04D0 = _HpnicfevtModuleSw_LSU1FAB04D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1211)
)
_HpnicfevtModuleSw_LSQ1CTGS16SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CTGS16SC0 = _HpnicfevtModuleSw_LSQ1CTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1212)
)
_HpnicfevtModuleSw_EWPX2CTGS16SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX2CTGS16SC0 = _HpnicfevtModuleSw_EWPX2CTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1213)
)
_HpnicfevtModuleSw_LSU3WCMD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU3WCMD0 = _HpnicfevtModuleSw_LSU3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1214)
)
_HpnicfevtModuleSw_EWPX3WCMD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX3WCMD0 = _HpnicfevtModuleSw_EWPX3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1215)
)
_HpnicfevtModuleSw_LSQ1QGS4SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1QGS4SC0 = _HpnicfevtModuleSw_LSQ1QGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1216)
)
_HpnicfevtModuleSw_LSQ1QGC4SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1QGC4SC0 = _HpnicfevtModuleSw_LSQ1QGC4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1217)
)
_HpnicfevtModuleSw_LSU1TGT24SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGT24SF0 = _HpnicfevtModuleSw_LSU1TGT24SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1218)
)
_HpnicfevtModuleSw_LSQ1QGS8SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1QGS8SC3 = _HpnicfevtModuleSw_LSQ1QGS8SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1219)
)
_HpnicfevtModuleSw_LSQ1TGS32SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS32SC3 = _HpnicfevtModuleSw_LSQ1TGS32SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1220)
)
_HpnicfevtModuleSw_LSQ1QGS4SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1QGS4SC3 = _HpnicfevtModuleSw_LSQ1QGS4SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1221)
)
_HpnicfevtModuleSw_LSQ1TGS48SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS48SC3 = _HpnicfevtModuleSw_LSQ1TGS48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1222)
)
_HpnicfevtModuleSw_LSQ1QGC4SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1QGC4SC3 = _HpnicfevtModuleSw_LSQ1QGC4SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1223)
)
_HpnicfevtModuleSw_LSQ1FAB12D3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB12D3 = _HpnicfevtModuleSw_LSQ1FAB12D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1224)
)
_HpnicfevtModuleSw_LSQ1FAB08D3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB08D3 = _HpnicfevtModuleSw_LSQ1FAB08D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1225)
)
_HpnicfevtModuleSw_LSQ1FAB04D3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB04D3 = _HpnicfevtModuleSw_LSQ1FAB04D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1226)
)
_HpnicfevtModuleSw_LSQ1TGS8EB3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS8EB3 = _HpnicfevtModuleSw_LSQ1TGS8EB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1227)
)
_HpnicfevtModuleSw_LSQ1TGT24SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGT24SC3 = _HpnicfevtModuleSw_LSQ1TGT24SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1228)
)
_HpnicfevtModuleSw_LSQ1FAB08B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1FAB08B0 = _HpnicfevtModuleSw_LSQ1FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1229)
)
_HpnicfevtModuleSw_EWPX2CTGS16SC_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX2CTGS16SC = _HpnicfevtModuleSw_EWPX2CTGS16SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1230)
)
_HpnicfevtModuleSw_LSU1SUPB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1SUPB0 = _HpnicfevtModuleSw_LSU1SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1231)
)
_HpnicfevtModuleSw_LSQ1GP48SA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48SA0 = _HpnicfevtModuleSw_LSQ1GP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1232)
)
_HpnicfevtModuleSw_LSQ1TGX2SA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGX2SA0 = _HpnicfevtModuleSw_LSQ1TGX2SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1233)
)
_HpnicfevtModuleSw_LSV1SRPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSV1SRPUA1 = _HpnicfevtModuleSw_LSV1SRPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1234)
)
_HpnicfevtModuleSw_LSV1QGS12SA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSV1QGS12SA1 = _HpnicfevtModuleSw_LSV1QGS12SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1235)
)
_HpnicfevtModuleSw_LSV1MPUA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSV1MPUA1 = _HpnicfevtModuleSw_LSV1MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1236)
)
_HpnicfevtModuleSw_LSX1SUP10A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP10A0 = _HpnicfevtModuleSw_LSX1SUP10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1237)
)
_HpnicfevtModuleSw_LSX1SUP16A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP16A0 = _HpnicfevtModuleSw_LSX1SUP16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1238)
)
_HpnicfevtModuleSw_LSX1SUP10A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP10A1 = _HpnicfevtModuleSw_LSX1SUP10A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1239)
)
_HpnicfevtModuleSw_LSX1SUP16A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP16A1 = _HpnicfevtModuleSw_LSX1SUP16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1240)
)
_HpnicfevtModuleSw_LSX1FAB10B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB10B0 = _HpnicfevtModuleSw_LSX1FAB10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1241)
)
_HpnicfevtModuleSw_LSX1FAB16B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB16B0 = _HpnicfevtModuleSw_LSX1FAB16B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1242)
)
_HpnicfevtModuleSw_LSX1FAB10B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB10B1 = _HpnicfevtModuleSw_LSX1FAB10B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1243)
)
_HpnicfevtModuleSw_LSX1FAB16B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB16B1 = _HpnicfevtModuleSw_LSX1FAB16B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1244)
)
_HpnicfevtModuleSw_LSX1QGS16EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS16EA0 = _HpnicfevtModuleSw_LSX1QGS16EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1245)
)
_HpnicfevtModuleSw_LSX1TGS48EA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48EA0 = _HpnicfevtModuleSw_LSX1TGS48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1246)
)
_HpnicfevtModuleSw_LSX1QGS16EA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS16EA1 = _HpnicfevtModuleSw_LSX1QGS16EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1247)
)
_HpnicfevtModuleSw_LSX1TGS48EA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48EA1 = _HpnicfevtModuleSw_LSX1TGS48EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1248)
)
_HpnicfevtModuleSw_LSU1TGT24SF9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGT24SF9 = _HpnicfevtModuleSw_LSU1TGT24SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1249)
)
_HpnicfevtModuleSw_LSU1QGS8SF9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGS8SF9 = _HpnicfevtModuleSw_LSU1QGS8SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1250)
)
_HpnicfevtModuleSw_LSU1QGS4SF9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGS4SF9 = _HpnicfevtModuleSw_LSU1QGS4SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1251)
)
_HpnicfevtModuleSw_LSU1TGS48SF9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS48SF9 = _HpnicfevtModuleSw_LSU1TGS48SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1252)
)
_HpnicfevtModuleSw_LSU1TGS32SF9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS32SF9 = _HpnicfevtModuleSw_LSU1TGS32SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1253)
)
_HpnicfevtModuleSw_LSU1FAB08D9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB08D9 = _HpnicfevtModuleSw_LSU1FAB08D9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1254)
)
_HpnicfevtModuleSw_LSU1SUPB9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1SUPB9 = _HpnicfevtModuleSw_LSU1SUPB9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1255)
)
_HpnicfevtModuleSw_LSQ3GV48SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ3GV48SC0 = _HpnicfevtModuleSw_LSQ3GV48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1256)
)
_HpnicfevtModuleSw_LSX1QGS12EC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS12EC1 = _HpnicfevtModuleSw_LSX1QGS12EC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1257)
)
_HpnicfevtModuleSw_LSX1QGS12EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS12EC0 = _HpnicfevtModuleSw_LSX1QGS12EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1258)
)
_HpnicfevtModuleSw_LSX1TGS48EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48EC0 = _HpnicfevtModuleSw_LSX1TGS48EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1259)
)
_HpnicfevtModuleSw_LSX1TGS48EC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48EC1 = _HpnicfevtModuleSw_LSX1TGS48EC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1260)
)
_HpnicfevtModuleSw_LSX1TGS24EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS24EC0 = _HpnicfevtModuleSw_LSX1TGS24EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1261)
)
_HpnicfevtModuleSw_LSX1TGS24EC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS24EC1 = _HpnicfevtModuleSw_LSX1TGS24EC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1262)
)
_HpnicfevtModuleSw_LSX1FAB10A0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB10A0 = _HpnicfevtModuleSw_LSX1FAB10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1263)
)
_HpnicfevtModuleSw_LSX1FAB16A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB16A1 = _HpnicfevtModuleSw_LSX1FAB16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1264)
)
_HpnicfevtModuleSw_LSX1QGS12FB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS12FB0 = _HpnicfevtModuleSw_LSX1QGS12FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1265)
)
_HpnicfevtModuleSw_LSX1TGS24FB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS24FB0 = _HpnicfevtModuleSw_LSX1TGS24FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1266)
)
_HpnicfevtModuleSw_LSX1TGS48FB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48FB0 = _HpnicfevtModuleSw_LSX1TGS48FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1267)
)
_HpnicfevtModuleSw_LSX1QGS12EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS12EB1 = _HpnicfevtModuleSw_LSX1QGS12EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1268)
)
_HpnicfevtModuleSw_LSX1TGS24EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS24EB1 = _HpnicfevtModuleSw_LSX1TGS24EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1269)
)
_HpnicfevtModuleSw_LSX1FAB10A1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB10A1 = _HpnicfevtModuleSw_LSX1FAB10A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1270)
)
_HpnicfevtModuleSw_LSX1TGS48EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1TGS48EB1 = _HpnicfevtModuleSw_LSX1TGS48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1271)
)
_HpnicfevtModuleSw_LSX1GP48EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GP48EB1 = _HpnicfevtModuleSw_LSX1GP48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1272)
)
_HpnicfevtModuleSw_LSX1GP48FB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GP48FB0 = _HpnicfevtModuleSw_LSX1GP48FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1273)
)
_HpnicfevtModuleSw_LSX1GT48FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GT48FC0 = _HpnicfevtModuleSw_LSX1GT48FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1274)
)
_HpnicfevtModuleSw_LSX1GT48FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GT48FC1 = _HpnicfevtModuleSw_LSX1GT48FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1275)
)
_HpnicfevtModuleSw_LSX1GP48FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GP48FC0 = _HpnicfevtModuleSw_LSX1GP48FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1276)
)
_HpnicfevtModuleSw_LSX1GP48FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GP48FC1 = _HpnicfevtModuleSw_LSX1GP48FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1277)
)
_HpnicfevtModuleSw_LSX1QGS12FC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS12FC0 = _HpnicfevtModuleSw_LSX1QGS12FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1278)
)
_HpnicfevtModuleSw_LSX1QGS12FC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1QGS12FC1 = _HpnicfevtModuleSw_LSX1QGS12FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1279)
)
_HpnicfevtModuleSw_LSX2TGS48EA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX2TGS48EA1 = _HpnicfevtModuleSw_LSX2TGS48EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1280)
)
_HpnicfevtModuleSw_LSX1CGC4EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1CGC4EB1 = _HpnicfevtModuleSw_LSX1CGC4EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1281)
)
_HpnicfevtModuleSw_LSX1CGC4EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1CGC4EC0 = _HpnicfevtModuleSw_LSX1CGC4EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1282)
)
_HpnicfevtModuleSw_LSX1GT48EB1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GT48EB1 = _HpnicfevtModuleSw_LSX1GT48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1283)
)
_HpnicfevtModuleSw_LSX1GT48FB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1GT48FB0 = _HpnicfevtModuleSw_LSX1GT48FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1284)
)
_HpnicfevtModuleSw_LSX1FAB16S1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB16S1 = _HpnicfevtModuleSw_LSX1FAB16S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1285)
)
_HpnicfevtModuleSw_LSQ1SUPB3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SUPB3 = _HpnicfevtModuleSw_LSQ1SUPB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1286)
)
_HpnicfevtModuleSw_LSU1CGC2SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1CGC2SE0 = _HpnicfevtModuleSw_LSU1CGC2SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1287)
)
_HpnicfevtModuleSw_LSU1TGS16SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS16SF0 = _HpnicfevtModuleSw_LSU1TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1288)
)
_HpnicfevtModuleSw_LSU1TGS8SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS8SF0 = _HpnicfevtModuleSw_LSU1TGS8SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1289)
)
_HpnicfevtModuleSw_LSQ1TGS4SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS4SC0 = _HpnicfevtModuleSw_LSQ1TGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1290)
)
_HpnicfevtModuleSw_LSU1GT48SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GT48SE3 = _HpnicfevtModuleSw_LSU1GT48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1291)
)
_HpnicfevtModuleSw_LSU1GP48SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP48SE3 = _HpnicfevtModuleSw_LSU1GP48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1292)
)
_HpnicfevtModuleSw_LSX1SUP10B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP10B0 = _HpnicfevtModuleSw_LSX1SUP10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1293)
)
_HpnicfevtModuleSw_LSX1SUP16B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP16B0 = _HpnicfevtModuleSw_LSX1SUP16B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1294)
)
_HpnicfevtModuleSw_LSX1SUP10B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP10B1 = _HpnicfevtModuleSw_LSX1SUP10B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1295)
)
_HpnicfevtModuleSw_LSX1SUP16B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1SUP16B1 = _HpnicfevtModuleSw_LSX1SUP16B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1296)
)
_HpnicfevtModuleSw_LSQ1CGV24PSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGV24PSC3 = _HpnicfevtModuleSw_LSQ1CGV24PSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1297)
)
_HpnicfevtModuleSw_LSQ1SRPA8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1SRPA8 = _HpnicfevtModuleSw_LSQ1SRPA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1298)
)
_HpnicfevtModuleSw_LSQ1CGP24TSC8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGP24TSC8 = _HpnicfevtModuleSw_LSQ1CGP24TSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1299)
)
_HpnicfevtModuleSw_LSQ1CGT24PSC8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1CGT24PSC8 = _HpnicfevtModuleSw_LSQ1CGT24PSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1300)
)
_HpnicfevtModuleSw_LSQ1GT24PSA8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GT24PSA8 = _HpnicfevtModuleSw_LSQ1GT24PSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1301)
)
_HpnicfevtModuleSw_LSQ1GP24TSA8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP24TSA8 = _HpnicfevtModuleSw_LSQ1GP24TSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1302)
)
_HpnicfevtModuleSw_LSQ1GT48SA8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GT48SA8 = _HpnicfevtModuleSw_LSQ1GT48SA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1303)
)
_HpnicfevtModuleSw_LSQ1GP48SA8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1GP48SA8 = _HpnicfevtModuleSw_LSQ1GP48SA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1304)
)
_HpnicfevtModuleSw_LSQ1TGS4SC8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS4SC8 = _HpnicfevtModuleSw_LSQ1TGS4SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1305)
)
_HpnicfevtModuleSw_LSQ1TGS8SC8_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ1TGS8SC8 = _HpnicfevtModuleSw_LSQ1TGS8SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1306)
)
_HpnicfevtModuleSw_LSU1GT24SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GT24SE3 = _HpnicfevtModuleSw_LSU1GT24SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1307)
)
_HpnicfevtModuleSw_LSU1GP12SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP12SE3 = _HpnicfevtModuleSw_LSU1GP12SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1308)
)
_HpnicfevtModuleSw_LSU1GP24SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP24SE3 = _HpnicfevtModuleSw_LSU1GP24SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1309)
)
_HpnicfevtModuleSw_LSU1T24XGSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1T24XGSE3 = _HpnicfevtModuleSw_LSU1T24XGSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1310)
)
_HpnicfevtModuleSw_LSU1P24XGSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1P24XGSE3 = _HpnicfevtModuleSw_LSU1P24XGSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1311)
)
_HpnicfevtModuleSw_LSU1GP24TSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP24TSE3 = _HpnicfevtModuleSw_LSU1GP24TSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1312)
)
_HpnicfevtModuleSw_LSU1GT40PSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GT40PSE3 = _HpnicfevtModuleSw_LSU1GT40PSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1313)
)
_HpnicfevtModuleSw_LSV1TGS24SA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSV1TGS24SA1 = _HpnicfevtModuleSw_LSV1TGS24SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1314)
)
_HpnicfevtModuleSw_LSV1SRPA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSV1SRPA1 = _HpnicfevtModuleSw_LSV1SRPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1315)
)
_HpnicfevtModuleSw_LSV1SRPC1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSV1SRPC1 = _HpnicfevtModuleSw_LSV1SRPC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1316)
)
_HpnicfevtModuleSw_LSX1FAB16S0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSX1FAB16S0 = _HpnicfevtModuleSw_LSX1FAB16S0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1317)
)
_HpnicfevtModuleSw_LSU1WCME0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1WCME0 = _HpnicfevtModuleSw_LSU1WCME0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1318)
)
_HpnicfevtModuleSw_EWPX1WCME0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_EWPX1WCME0 = _HpnicfevtModuleSw_EWPX1WCME0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1319)
)
_HpnicfevtModuleSw_LSU1TGS48SG0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS48SG0 = _HpnicfevtModuleSw_LSU1TGS48SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1320)
)
_HpnicfevtModuleSw_LSU1QGS12SG0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGS12SG0 = _HpnicfevtModuleSw_LSU1QGS12SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1321)
)
_HpnicfevtModuleSw_LSU1GP44TSEC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1GP44TSEC0 = _HpnicfevtModuleSw_LSU1GP44TSEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1322)
)
_HpnicfevtModuleSw_LSU1TGS24EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1TGS24EC0 = _HpnicfevtModuleSw_LSU1TGS24EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1323)
)
_HpnicfevtModuleSw_LSU1QGS6EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1QGS6EC0 = _HpnicfevtModuleSw_LSU1QGS6EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1324)
)
_HpnicfevtModuleSw_LSU1CGC2EC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1CGC2EC0 = _HpnicfevtModuleSw_LSU1CGC2EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1325)
)
_HpnicfevtModuleSw_LSU1CGC2SE9_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1CGC2SE9 = _HpnicfevtModuleSw_LSU1CGC2SE9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1326)
)
_HpnicfevtModuleSw_LSXM1QGS24EX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1QGS24EX1 = _HpnicfevtModuleSw_LSXM1QGS24EX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1327)
)
_HpnicfevtModuleSw_LSXM1QGS24FB0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1QGS24FB0 = _HpnicfevtModuleSw_LSXM1QGS24FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1328)
)
_HpnicfevtModuleSw_LSVM1QGS12FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSVM1QGS12FX1 = _HpnicfevtModuleSw_LSVM1QGS12FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1329)
)
_HpnicfevtModuleSw_LSVM1TGS24FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSVM1TGS24FX1 = _HpnicfevtModuleSw_LSVM1TGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1330)
)
_HpnicfevtModuleSw_LSVM1QGS6C2FX1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSVM1QGS6C2FX1 = _HpnicfevtModuleSw_LSVM1QGS6C2FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1331)
)
_HpnicfevtModuleSw_LSQ2GP44TSSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GP44TSSC0 = _HpnicfevtModuleSw_LSQ2GP44TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1332)
)
_HpnicfevtModuleSw_LSQ2GP44TSSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GP44TSSC3 = _HpnicfevtModuleSw_LSQ2GP44TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1333)
)
_HpnicfevtModuleSw_LSQ2GP24TSSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GP24TSSC0 = _HpnicfevtModuleSw_LSQ2GP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1334)
)
_HpnicfevtModuleSw_LSQ2GP24TSSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GP24TSSC3 = _HpnicfevtModuleSw_LSQ2GP24TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1335)
)
_HpnicfevtModuleSw_LSQ2GT24PTSSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GT24PTSSC0 = _HpnicfevtModuleSw_LSQ2GT24PTSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1336)
)
_HpnicfevtModuleSw_LSQ2GT24PTSSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GT24PTSSC3 = _HpnicfevtModuleSw_LSQ2GT24PTSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1337)
)
_HpnicfevtModuleSw_LSQ2GT24TSSC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GT24TSSC0 = _HpnicfevtModuleSw_LSQ2GT24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1338)
)
_HpnicfevtModuleSw_LSQ2GT24TSSC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GT24TSSC3 = _HpnicfevtModuleSw_LSQ2GT24TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1339)
)
_HpnicfevtModuleSw_LSQ2GT48SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GT48SC0 = _HpnicfevtModuleSw_LSQ2GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1340)
)
_HpnicfevtModuleSw_LSQ2GT48SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GT48SC3 = _HpnicfevtModuleSw_LSQ2GT48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1341)
)
_HpnicfevtModuleSw_LSQ2GV48SC0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GV48SC0 = _HpnicfevtModuleSw_LSQ2GV48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1342)
)
_HpnicfevtModuleSw_LSQ2GV48SC3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2GV48SC3 = _HpnicfevtModuleSw_LSQ2GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1343)
)
_HpnicfevtModuleSw_LSQ2TGS16SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2TGS16SF0 = _HpnicfevtModuleSw_LSQ2TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1344)
)
_HpnicfevtModuleSw_LSQ2TGS16SF3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2TGS16SF3 = _HpnicfevtModuleSw_LSQ2TGS16SF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1345)
)
_HpnicfevtModuleSw_LSQ2MPUD0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2MPUD0 = _HpnicfevtModuleSw_LSQ2MPUD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1346)
)
_HpnicfevtModuleSw_LSQ2MPUD3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2MPUD3 = _HpnicfevtModuleSw_LSQ2MPUD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1347)
)
_HpnicfevtModuleSw_LSQ2MPUA0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2MPUA0 = _HpnicfevtModuleSw_LSQ2MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1348)
)
_HpnicfevtModuleSw_LSQ2MPUA3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSQ2MPUA3 = _HpnicfevtModuleSw_LSQ2MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1349)
)
_HpnicfevtModuleSw_LSU2GP44TSSE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GP44TSSE0 = _HpnicfevtModuleSw_LSU2GP44TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1350)
)
_HpnicfevtModuleSw_LSU2GP44TSSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GP44TSSE3 = _HpnicfevtModuleSw_LSU2GP44TSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1351)
)
_HpnicfevtModuleSw_LSU2GP24TSSE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GP24TSSE0 = _HpnicfevtModuleSw_LSU2GP24TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1352)
)
_HpnicfevtModuleSw_LSU2GP24TSSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GP24TSSE3 = _HpnicfevtModuleSw_LSU2GP24TSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1353)
)
_HpnicfevtModuleSw_LSU2GT24PTSSE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GT24PTSSE0 = _HpnicfevtModuleSw_LSU2GT24PTSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1354)
)
_HpnicfevtModuleSw_LSU2GT24PTSSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GT24PTSSE3 = _HpnicfevtModuleSw_LSU2GT24PTSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1355)
)
_HpnicfevtModuleSw_LSU2GT24TSSE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GT24TSSE0 = _HpnicfevtModuleSw_LSU2GT24TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1356)
)
_HpnicfevtModuleSw_LSU2GT24TSSE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GT24TSSE3 = _HpnicfevtModuleSw_LSU2GT24TSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1357)
)
_HpnicfevtModuleSw_LSU2GT48SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GT48SE0 = _HpnicfevtModuleSw_LSU2GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1358)
)
_HpnicfevtModuleSw_LSU2GT48SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GT48SE3 = _HpnicfevtModuleSw_LSU2GT48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1359)
)
_HpnicfevtModuleSw_LSU2GV48SE0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GV48SE0 = _HpnicfevtModuleSw_LSU2GV48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1360)
)
_HpnicfevtModuleSw_LSU2GV48SE3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2GV48SE3 = _HpnicfevtModuleSw_LSU2GV48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1361)
)
_HpnicfevtModuleSw_LSU2TGS16SF0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2TGS16SF0 = _HpnicfevtModuleSw_LSU2TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1362)
)
_HpnicfevtModuleSw_LSU2TGS16SF3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU2TGS16SF3 = _HpnicfevtModuleSw_LSU2TGS16SF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1363)
)
_HpnicfevtModuleSw_LSU1MPU06B0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1MPU06B0 = _HpnicfevtModuleSw_LSU1MPU06B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1364)
)
_HpnicfevtModuleSw_LSU1MPU06B3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1MPU06B3 = _HpnicfevtModuleSw_LSU1MPU06B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1365)
)
_HpnicfevtModuleSw_LSU1MPU10C0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1MPU10C0 = _HpnicfevtModuleSw_LSU1MPU10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1366)
)
_HpnicfevtModuleSw_LSU1MPU10C3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1MPU10C3 = _HpnicfevtModuleSw_LSU1MPU10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1367)
)
_HpnicfevtModuleSw_LSU1FAB06C0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB06C0 = _HpnicfevtModuleSw_LSU1FAB06C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1368)
)
_HpnicfevtModuleSw_LSU1FAB06C3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB06C3 = _HpnicfevtModuleSw_LSU1FAB06C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1369)
)
_HpnicfevtModuleSw_LSU1FAB10C0_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB10C0 = _HpnicfevtModuleSw_LSU1FAB10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1370)
)
_HpnicfevtModuleSw_LSU1FAB10C3_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSU1FAB10C3 = _HpnicfevtModuleSw_LSU1FAB10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1371)
)
_HpnicfevtModuleSw_LSXM1SUPA1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1SUPA1 = _HpnicfevtModuleSw_LSXM1SUPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1372)
)
_HpnicfevtModuleSw_LSXM1SFF16B1_ObjectIdentity = ObjectIdentity
hpnicfevtModuleSw_LSXM1SFF16B1 = _HpnicfevtModuleSw_LSXM1SFF16B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1373)
)
_HpnicfevtModulesw_PEX_Common_ObjectIdentity = ObjectIdentity
hpnicfevtModulesw_PEX_Common = _HpnicfevtModulesw_PEX_Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 4, 1400)
)
_HpnicfevtSubModuleRouter_ObjectIdentity = ObjectIdentity
hpnicfevtSubModuleRouter = _HpnicfevtSubModuleRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 5)
)
_HpnicfevtSubModuleSwitch_ObjectIdentity = ObjectIdentity
hpnicfevtSubModuleSwitch = _HpnicfevtSubModuleSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 9, 6)
)
_HpnicfevtPort_ObjectIdentity = ObjectIdentity
hpnicfevtPort = _HpnicfevtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10)
)
_HpnicfevtPortUnknownPorts_ObjectIdentity = ObjectIdentity
hpnicfevtPortUnknownPorts = _HpnicfevtPortUnknownPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 1)
)
_HpnicfevtPortCommonPorts_ObjectIdentity = ObjectIdentity
hpnicfevtPortCommonPorts = _HpnicfevtPortCommonPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 2)
)
_HpnicfevtPortRouterType_ObjectIdentity = ObjectIdentity
hpnicfevtPortRouterType = _HpnicfevtPortRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3)
)
_HpnicfevtPortRt_Async_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Async = _HpnicfevtPortRt_Async_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 1)
)
_HpnicfevtPortRt_Analogmodem_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Analogmodem = _HpnicfevtPortRt_Analogmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 2)
)
_HpnicfevtPortRt_Atm_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Atm = _HpnicfevtPortRt_Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 3)
)
_HpnicfevtPortRt_AtmAdsl_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmAdsl = _HpnicfevtPortRt_AtmAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 4)
)
_HpnicfevtPortRt_AtmShdsl_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmShdsl = _HpnicfevtPortRt_AtmShdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 5)
)
_HpnicfevtPortRt_AtmE1_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmE1 = _HpnicfevtPortRt_AtmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 6)
)
_HpnicfevtPortRt_AtmT1_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmT1 = _HpnicfevtPortRt_AtmT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 7)
)
_HpnicfevtPortRt_AtmE3_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmE3 = _HpnicfevtPortRt_AtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 8)
)
_HpnicfevtPortRt_AtmT3_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmT3 = _HpnicfevtPortRt_AtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 9)
)
_HpnicfevtPortRt_Atm622M_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Atm622M = _HpnicfevtPortRt_Atm622M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 10)
)
_HpnicfevtPortRt_AtmImaE1_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmImaE1 = _HpnicfevtPortRt_AtmImaE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 11)
)
_HpnicfevtPortRt_AtmImaT1_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_AtmImaT1 = _HpnicfevtPortRt_AtmImaT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 12)
)
_HpnicfevtPortRt_Atm25M_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Atm25M = _HpnicfevtPortRt_Atm25M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 13)
)
_HpnicfevtPortRt_Bri_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Bri = _HpnicfevtPortRt_Bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 14)
)
_HpnicfevtPortRt_Console_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Console = _HpnicfevtPortRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 15)
)
_HpnicfevtPortRt_E1_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_E1 = _HpnicfevtPortRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 16)
)
_HpnicfevtPortRt_E3_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_E3 = _HpnicfevtPortRt_E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 17)
)
_HpnicfevtPortRt_T1_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_T1 = _HpnicfevtPortRt_T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 18)
)
_HpnicfevtPortRt_T3_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_T3 = _HpnicfevtPortRt_T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 19)
)
_HpnicfevtPortRt_Cpos_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Cpos = _HpnicfevtPortRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 20)
)
_HpnicfevtPortRt_Ethernet_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Ethernet = _HpnicfevtPortRt_Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 21)
)
_HpnicfevtPortRt_Serial_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Serial = _HpnicfevtPortRt_Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 22)
)
_HpnicfevtPortRt_E1f_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_E1f = _HpnicfevtPortRt_E1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 23)
)
_HpnicfevtPortRt_T1f_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_T1f = _HpnicfevtPortRt_T1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 24)
)
_HpnicfevtPortRt_Pos_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Pos = _HpnicfevtPortRt_Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 25)
)
_HpnicfevtPortRt_Ge_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Ge = _HpnicfevtPortRt_Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 26)
)
_HpnicfevtPortRt_Aux_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Aux = _HpnicfevtPortRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 27)
)
_HpnicfevtPortRt_VG_Fxs_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_VG_Fxs = _HpnicfevtPortRt_VG_Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 30)
)
_HpnicfevtPortRt_VG_Fxo_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_VG_Fxo = _HpnicfevtPortRt_VG_Fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 31)
)
_HpnicfevtPortRt_VG_E1vi_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_VG_E1vi = _HpnicfevtPortRt_VG_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 32)
)
_HpnicfevtPortRt_VG_T1vi_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_VG_T1vi = _HpnicfevtPortRt_VG_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 33)
)
_HpnicfevtPortRt_Usb_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Usb = _HpnicfevtPortRt_Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 34)
)
_HpnicfevtPortRt_Ndec_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Ndec = _HpnicfevtPortRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 35)
)
_HpnicfevtPortRt_Cavium_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Cavium = _HpnicfevtPortRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 36)
)
_HpnicfevtPortRt_Fcm_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Fcm = _HpnicfevtPortRt_Fcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 37)
)
_HpnicfevtPortRt_E1vi_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_E1vi = _HpnicfevtPortRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 38)
)
_HpnicfevtPortRt_T1vi_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_T1vi = _HpnicfevtPortRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 39)
)
_HpnicfevtPortRt_Vi_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Vi = _HpnicfevtPortRt_Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 40)
)
_HpnicfevtPortRt_Adls2Plus_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Adls2Plus = _HpnicfevtPortRt_Adls2Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 41)
)
_HpnicfevtPortRt_RADIO_AG_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_RADIO_AG = _HpnicfevtPortRt_RADIO_AG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 42)
)
_HpnicfevtPortRt_1exp_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_1exp = _HpnicfevtPortRt_1exp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 43)
)
_HpnicfevtPortRt_G_SHDSL_BIS_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_G_SHDSL_BIS = _HpnicfevtPortRt_G_SHDSL_BIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 44)
)
_HpnicfevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_ONU_1000BASE_BX_SFF_SC = _HpnicfevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 45)
)
_HpnicfevtPortRt_CELLULAR_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_CELLULAR = _HpnicfevtPortRt_CELLULAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 46)
)
_HpnicfevtPortRt_CELLULAR_ETHERNET_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_CELLULAR_ETHERNET = _HpnicfevtPortRt_CELLULAR_ETHERNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 47)
)
_HpnicfevtPortRt_VGe_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_VGe = _HpnicfevtPortRt_VGe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 48)
)
_HpnicfevtPortRt_VXGe_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_VXGe = _HpnicfevtPortRt_VXGe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 49)
)
_HpnicfevtPortRt_Xpos_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Xpos = _HpnicfevtPortRt_Xpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 50)
)
_HpnicfevtPortRt_Fge_ObjectIdentity = ObjectIdentity
hpnicfevtPortRt_Fge = _HpnicfevtPortRt_Fge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 3, 51)
)
_HpnicfevtPortSwitchType_ObjectIdentity = ObjectIdentity
hpnicfevtPortSwitchType = _HpnicfevtPortSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4)
)
_HpnicfevtPortSw_10or100M_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10or100M = _HpnicfevtPortSw_10or100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 1)
)
_HpnicfevtPortSw_1000BaseLxSm_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseLxSm = _HpnicfevtPortSw_1000BaseLxSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 2)
)
_HpnicfevtPortSw_1000BaseSxMm_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseSxMm = _HpnicfevtPortSw_1000BaseSxMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 3)
)
_HpnicfevtPortSw_1000BaseTx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseTx = _HpnicfevtPortSw_1000BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 4)
)
_HpnicfevtPortSw_100MSinglemodeFx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MSinglemodeFx = _HpnicfevtPortSw_100MSinglemodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 5)
)
_HpnicfevtPortSw_100MMultimodeFx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MMultimodeFx = _HpnicfevtPortSw_100MMultimodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 6)
)
_HpnicfevtPortSw_100M100BaseTx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100M100BaseTx = _HpnicfevtPortSw_100M100BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 7)
)
_HpnicfevtPortSw_100MHub_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MHub = _HpnicfevtPortSw_100MHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 8)
)
_HpnicfevtPortSw_Vdsl_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Vdsl = _HpnicfevtPortSw_Vdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 9)
)
_HpnicfevtPortSw_Stack_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Stack = _HpnicfevtPortSw_Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 10)
)
_HpnicfevtPortSw_1000BaseZenithFx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseZenithFx = _HpnicfevtPortSw_1000BaseZenithFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 11)
)
_HpnicfevtPortSw_1000BaseLongFx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseLongFx = _HpnicfevtPortSw_1000BaseLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 12)
)
_HpnicfevtPortSw_Adsl_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Adsl = _HpnicfevtPortSw_Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 13)
)
_HpnicfevtPortSw_10or100MDb_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10or100MDb = _HpnicfevtPortSw_10or100MDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 14)
)
_HpnicfevtPortSw_10GBaseLrSm_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBaseLrSm = _HpnicfevtPortSw_10GBaseLrSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 15)
)
_HpnicfevtPortSw_10GBaseLx4Mm_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBaseLx4Mm = _HpnicfevtPortSw_10GBaseLx4Mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 16)
)
_HpnicfevtPortSw_10GBaseLx4Sm_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBaseLx4Sm = _HpnicfevtPortSw_10GBaseLx4Sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 17)
)
_HpnicfevtPortSw_100MLongFx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MLongFx = _HpnicfevtPortSw_100MLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 18)
)
_HpnicfevtPortSw_1000BaseCx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseCx = _HpnicfevtPortSw_1000BaseCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 19)
)
_HpnicfevtPortSw_1000BaseZenithFxLc_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseZenithFxLc = _HpnicfevtPortSw_1000BaseZenithFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 20)
)
_HpnicfevtPortSw_1000BaseLongFxLc_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BaseLongFxLc = _HpnicfevtPortSw_1000BaseLongFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 21)
)
_HpnicfevtPortSw_100MSmFxSc_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MSmFxSc = _HpnicfevtPortSw_100MSmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 22)
)
_HpnicfevtPortSw_100MMmFxSc_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MMmFxSc = _HpnicfevtPortSw_100MMmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 23)
)
_HpnicfevtPortSw_100MSmFxLc_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MSmFxLc = _HpnicfevtPortSw_100MSmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 24)
)
_HpnicfevtPortSw_100MMmFxLc_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100MMmFxLc = _HpnicfevtPortSw_100MMmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 25)
)
_HpnicfevtPortSw_GbicNoConnector_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_GbicNoConnector = _HpnicfevtPortSw_GbicNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 26)
)
_HpnicfevtPortSw_Gbic1000BaseT_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Gbic1000BaseT = _HpnicfevtPortSw_Gbic1000BaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 27)
)
_HpnicfevtPortSw_Gbic1000BaseLx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Gbic1000BaseLx = _HpnicfevtPortSw_Gbic1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 28)
)
_HpnicfevtPortSw_Gbic1000BaseSx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Gbic1000BaseSx = _HpnicfevtPortSw_Gbic1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 29)
)
_HpnicfevtPortSw_Gbic1000BaseZx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Gbic1000BaseZx = _HpnicfevtPortSw_Gbic1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 30)
)
_HpnicfevtPortSw_ComboNoConnector_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_ComboNoConnector = _HpnicfevtPortSw_ComboNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 31)
)
_HpnicfevtPortSw_Combo1000BaseLx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseLx = _HpnicfevtPortSw_Combo1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 32)
)
_HpnicfevtPortSw_Combo1000BaseLxFiber_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseLxFiber = _HpnicfevtPortSw_Combo1000BaseLxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 33)
)
_HpnicfevtPortSw_Combo1000BaseLxCopper_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseLxCopper = _HpnicfevtPortSw_Combo1000BaseLxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 34)
)
_HpnicfevtPortSw_Combo1000BaseSx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseSx = _HpnicfevtPortSw_Combo1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 35)
)
_HpnicfevtPortSw_Combo1000BaseSxFiber_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseSxFiber = _HpnicfevtPortSw_Combo1000BaseSxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 36)
)
_HpnicfevtPortSw_Combo1000BaseSxCopper_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseSxCopper = _HpnicfevtPortSw_Combo1000BaseSxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 37)
)
_HpnicfevtPortSw_Combo1000BaseZx_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseZx = _HpnicfevtPortSw_Combo1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 38)
)
_HpnicfevtPortSw_Combo1000BaseZxFiber_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseZxFiber = _HpnicfevtPortSw_Combo1000BaseZxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 39)
)
_HpnicfevtPortSw_Combo1000BaseZxCopper_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_Combo1000BaseZxCopper = _HpnicfevtPortSw_Combo1000BaseZxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 40)
)
_HpnicfevtPortSw_155PosSxMmf_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155PosSxMmf = _HpnicfevtPortSw_155PosSxMmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 41)
)
_HpnicfevtPortSw_155PosLxSmf_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155PosLxSmf = _HpnicfevtPortSw_155PosLxSmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 42)
)
_HpnicfevtPortSw_1000BASE_T_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_T = _HpnicfevtPortSw_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 43)
)
_HpnicfevtPortSw_1000BASE_SX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_SX_SFP = _HpnicfevtPortSw_1000BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 44)
)
_HpnicfevtPortSw_1000BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_LX_SFP = _HpnicfevtPortSw_1000BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 45)
)
_HpnicfevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_T_AN_SFP = _HpnicfevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 46)
)
_HpnicfevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBASE_LX4_XENPAK = _HpnicfevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 47)
)
_HpnicfevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBASE_LR_XENPAK = _HpnicfevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 48)
)
_HpnicfevtPortSw_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBASE_CX4 = _HpnicfevtPortSw_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 49)
)
_HpnicfevtPortSw_1000BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_ZX_SFP = _HpnicfevtPortSw_1000BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 50)
)
_HpnicfevtPortSw_1000BASE_MM_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_MM_SFP = _HpnicfevtPortSw_1000BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 51)
)
_HpnicfevtPortSw_100BASE_SX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_SX_SFP = _HpnicfevtPortSw_100BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 52)
)
_HpnicfevtPortSw_100BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_LX_SFP = _HpnicfevtPortSw_100BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 53)
)
_HpnicfevtPortSw_100BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_T_AN_SFP = _HpnicfevtPortSw_100BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 54)
)
_HpnicfevtPortSw_100BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_ZX_SFP = _HpnicfevtPortSw_100BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 55)
)
_HpnicfevtPortSw_100BASE_MM_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_MM_SFP = _HpnicfevtPortSw_100BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 56)
)
_HpnicfevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_NO_CONNECTOR = _HpnicfevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 57)
)
_HpnicfevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_UNKNOWN_CONNECTOR = _HpnicfevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 58)
)
_HpnicfevtPortSw_POS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_NO_CONNECTOR = _HpnicfevtPortSw_POS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 59)
)
_HpnicfevtPortSw_10G_BASE_SR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_SR = _HpnicfevtPortSw_10G_BASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 60)
)
_HpnicfevtPortSw_10G_BASE_ER_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_ER = _HpnicfevtPortSw_10G_BASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 61)
)
_HpnicfevtPortSw_10G_BASE_LX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_LX4 = _HpnicfevtPortSw_10G_BASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 62)
)
_HpnicfevtPortSw_10G_BASE_SW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_SW = _HpnicfevtPortSw_10G_BASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 63)
)
_HpnicfevtPortSw_10G_BASE_LW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_LW = _HpnicfevtPortSw_10G_BASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 64)
)
_HpnicfevtPortSw_10G_BASE_EW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_EW = _HpnicfevtPortSw_10G_BASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 65)
)
_HpnicfevtPortSw_10G_LR_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_LR_SM_LC = _HpnicfevtPortSw_10G_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 66)
)
_HpnicfevtPortSw_10G_SR_MM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_SR_MM_LC = _HpnicfevtPortSw_10G_SR_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 67)
)
_HpnicfevtPortSw_10G_ER_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_ER_SM_LC = _HpnicfevtPortSw_10G_ER_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 68)
)
_HpnicfevtPortSw_10G_LW_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_LW_SM_LC = _HpnicfevtPortSw_10G_LW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 69)
)
_HpnicfevtPortSw_10G_SW_MM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_SW_MM_LC = _HpnicfevtPortSw_10G_SW_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 70)
)
_HpnicfevtPortSw_10G_EW_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_EW_SM_LC = _HpnicfevtPortSw_10G_EW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 71)
)
_HpnicfevtPortSw_100BASE_SM_MTRJ_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_SM_MTRJ = _HpnicfevtPortSw_100BASE_SM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 72)
)
_HpnicfevtPortSw_100BASE_MM_MTRJ_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_MM_MTRJ = _HpnicfevtPortSw_100BASE_MM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 73)
)
_HpnicfevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_NO_CONNECTOR = _HpnicfevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 74)
)
_HpnicfevtPortSw_XFP_10GBASE_SR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_SR = _HpnicfevtPortSw_XFP_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 75)
)
_HpnicfevtPortSw_XFP_10GBASE_LR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_LR = _HpnicfevtPortSw_XFP_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 76)
)
_HpnicfevtPortSw_XFP_10GBASE_ER_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_ER = _HpnicfevtPortSw_XFP_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 77)
)
_HpnicfevtPortSw_XFP_10GBASE_SW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_SW = _HpnicfevtPortSw_XFP_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 78)
)
_HpnicfevtPortSw_XFP_10GBASE_LW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_LW = _HpnicfevtPortSw_XFP_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 79)
)
_HpnicfevtPortSw_XFP_10GBASE_EW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_EW = _HpnicfevtPortSw_XFP_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 80)
)
_HpnicfevtPortSw_XFP_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_CX4 = _HpnicfevtPortSw_XFP_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 81)
)
_HpnicfevtPortSw_XFP_10GBASE_LX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_LX4 = _HpnicfevtPortSw_XFP_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 82)
)
_HpnicfevtPortSw_XFP_UNKNOWN_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_UNKNOWN = _HpnicfevtPortSw_XFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 83)
)
_HpnicfevtPortSw_XPK_NOCONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_NOCONNECTOR = _HpnicfevtPortSw_XPK_NOCONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 84)
)
_HpnicfevtPortSw_XPK_10GBASE_SR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_SR = _HpnicfevtPortSw_XPK_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 85)
)
_HpnicfevtPortSw_XPK_10GBASE_LR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_LR = _HpnicfevtPortSw_XPK_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 86)
)
_HpnicfevtPortSw_XPK_10GBASE_ER_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_ER = _HpnicfevtPortSw_XPK_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 87)
)
_HpnicfevtPortSw_XPK_10GBASE_SW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_SW = _HpnicfevtPortSw_XPK_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 88)
)
_HpnicfevtPortSw_XPK_10GBASE_LW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_LW = _HpnicfevtPortSw_XPK_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 89)
)
_HpnicfevtPortSw_XPK_10GBASE_EW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_EW = _HpnicfevtPortSw_XPK_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 90)
)
_HpnicfevtPortSw_XPK_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_CX4 = _HpnicfevtPortSw_XPK_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 91)
)
_HpnicfevtPortSw_XPK_10GBASE_LX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_LX4 = _HpnicfevtPortSw_XPK_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 92)
)
_HpnicfevtPortSw_XPK_UNKNOWN_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_UNKNOWN = _HpnicfevtPortSw_XPK_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 93)
)
_HpnicfevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_SR_SM_LC = _HpnicfevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 94)
)
_HpnicfevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_IR_SM_LC = _HpnicfevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 95)
)
_HpnicfevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_LR_SM_LC = _HpnicfevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 96)
)
_HpnicfevtPortSw_10G_BASE_CX4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_BASE_CX4 = _HpnicfevtPortSw_10G_BASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 97)
)
_HpnicfevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_OLT_1000BASE_BX_SFF_SC = _HpnicfevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 98)
)
_HpnicfevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_ONU_1000BASE_BX_SFF_SC = _HpnicfevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 99)
)
_HpnicfevtPortSw_24G_CASCADE_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_24G_CASCADE = _HpnicfevtPortSw_24G_CASCADE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 100)
)
_HpnicfevtPortSw_POS_OC3_SR_MM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_SR_MM = _HpnicfevtPortSw_POS_OC3_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 101)
)
_HpnicfevtPortSw_POS_OC3_IR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_IR_SM = _HpnicfevtPortSw_POS_OC3_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 102)
)
_HpnicfevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_IR_1_SM = _HpnicfevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 103)
)
_HpnicfevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_IR_2_SM = _HpnicfevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 104)
)
_HpnicfevtPortSw_POS_OC3_LR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_LR_SM = _HpnicfevtPortSw_POS_OC3_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 105)
)
_HpnicfevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_LR_1_SM = _HpnicfevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 106)
)
_HpnicfevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_LR_2_SM = _HpnicfevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 107)
)
_HpnicfevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC3_LR_3_SM = _HpnicfevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 108)
)
_HpnicfevtPortSw_POS_OC12_SR_MM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_SR_MM = _HpnicfevtPortSw_POS_OC12_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 109)
)
_HpnicfevtPortSw_POS_OC12_IR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_IR_SM = _HpnicfevtPortSw_POS_OC12_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 110)
)
_HpnicfevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_IR_1_SM = _HpnicfevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 111)
)
_HpnicfevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_IR_2_SM = _HpnicfevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 112)
)
_HpnicfevtPortSw_POS_OC12_LR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_LR_SM = _HpnicfevtPortSw_POS_OC12_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 113)
)
_HpnicfevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_LR_1_SM = _HpnicfevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 114)
)
_HpnicfevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_LR_2_SM = _HpnicfevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 115)
)
_HpnicfevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC12_LR_3_SM = _HpnicfevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 116)
)
_HpnicfevtPortSw_POS_OC48_SR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_SR_SM = _HpnicfevtPortSw_POS_OC48_SR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 117)
)
_HpnicfevtPortSw_POS_OC48_IR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_IR_SM = _HpnicfevtPortSw_POS_OC48_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 118)
)
_HpnicfevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_IR_1_SM = _HpnicfevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 119)
)
_HpnicfevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_IR_2_SM = _HpnicfevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 120)
)
_HpnicfevtPortSw_POS_OC48_LR_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_LR_SM = _HpnicfevtPortSw_POS_OC48_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 121)
)
_HpnicfevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_LR_1_SM = _HpnicfevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 122)
)
_HpnicfevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_LR_2_SM = _HpnicfevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 123)
)
_HpnicfevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_OC48_LR_3_SM = _HpnicfevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 124)
)
_HpnicfevtPortSw_POS_I_64_1_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_I_64_1 = _HpnicfevtPortSw_POS_I_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 125)
)
_HpnicfevtPortSw_POS_I_64_2_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_I_64_2 = _HpnicfevtPortSw_POS_I_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 126)
)
_HpnicfevtPortSw_POS_I_64_3_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_I_64_3 = _HpnicfevtPortSw_POS_I_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 127)
)
_HpnicfevtPortSw_POS_I_64_5_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_I_64_5 = _HpnicfevtPortSw_POS_I_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 128)
)
_HpnicfevtPortSw_POS_S_64_1_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_S_64_1 = _HpnicfevtPortSw_POS_S_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 129)
)
_HpnicfevtPortSw_POS_S_64_2_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_S_64_2 = _HpnicfevtPortSw_POS_S_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 130)
)
_HpnicfevtPortSw_POS_S_64_3_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_S_64_3 = _HpnicfevtPortSw_POS_S_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 131)
)
_HpnicfevtPortSw_POS_S_64_5_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_S_64_5 = _HpnicfevtPortSw_POS_S_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 132)
)
_HpnicfevtPortSw_POS_L_64_1_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_L_64_1 = _HpnicfevtPortSw_POS_L_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 133)
)
_HpnicfevtPortSw_POS_L_64_2_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_L_64_2 = _HpnicfevtPortSw_POS_L_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 134)
)
_HpnicfevtPortSw_POS_L_64_3_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_L_64_3 = _HpnicfevtPortSw_POS_L_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 135)
)
_HpnicfevtPortSw_POS_V_64_2_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_V_64_2 = _HpnicfevtPortSw_POS_V_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 136)
)
_HpnicfevtPortSw_POS_V_64_3_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_V_64_3 = _HpnicfevtPortSw_POS_V_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 137)
)
_HpnicfevtPortSw_100BASE_FX_BIDI_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_FX_BIDI = _HpnicfevtPortSw_100BASE_FX_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 138)
)
_HpnicfevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_BX10_U_SFP = _HpnicfevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 139)
)
_HpnicfevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_BX10_D_SFP = _HpnicfevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 140)
)
_HpnicfevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_BX10_U_SFP = _HpnicfevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 141)
)
_HpnicfevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_BX10_D_SFP = _HpnicfevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 142)
)
_HpnicfevtPortSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_STK_1000BASE_T = _HpnicfevtPortSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 143)
)
_HpnicfevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_PHYPOS_CONNECTOR = _HpnicfevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 144)
)
_HpnicfevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_PHY10GE_CONNECTOR = _HpnicfevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 145)
)
_HpnicfevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_LOGICPOS_CONNECTOR = _HpnicfevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 146)
)
_HpnicfevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_LOGIC10GE_CONNECTOR = _HpnicfevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 147)
)
_HpnicfevtPortSw_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBASE_ZR = _HpnicfevtPortSw_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 148)
)
_HpnicfevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_TYPE_ERROR_CONNECTOR = _HpnicfevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 149)
)
_HpnicfevtPortSw_10G_STACK_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_STACK = _HpnicfevtPortSw_10G_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 150)
)
_HpnicfevtPortSw_155_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_ATM_SX_MMF = _HpnicfevtPortSw_155_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 151)
)
_HpnicfevtPortSw_155_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_ATM_LX_SMF = _HpnicfevtPortSw_155_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 152)
)
_HpnicfevtPortSw_622_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_ATM_SX_MMF = _HpnicfevtPortSw_622_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 153)
)
_HpnicfevtPortSw_622_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_ATM_LX_SMF = _HpnicfevtPortSw_622_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 154)
)
_HpnicfevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_ATM_NO_CONNECTOR = _HpnicfevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 155)
)
_HpnicfevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_ATM_NO_CONNECTOR = _HpnicfevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 156)
)
_HpnicfevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_CPOS_E1_NO_CONNECTOR = _HpnicfevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 157)
)
_HpnicfevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_CPOS_T1_NO_CONNECTOR = _HpnicfevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 158)
)
_HpnicfevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_CPOS_E1_NO_CONNECTOR = _HpnicfevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 159)
)
_HpnicfevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_CPOS_T1_NO_CONNECTOR = _HpnicfevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 160)
)
_HpnicfevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_CPOS_E1_SX_MMF = _HpnicfevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 161)
)
_HpnicfevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_CPOS_T1_SX_MMF = _HpnicfevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 162)
)
_HpnicfevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_CPOS_E1_LX_SMF = _HpnicfevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 163)
)
_HpnicfevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_155_CPOS_T1_LX_SMF = _HpnicfevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 164)
)
_HpnicfevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_CPOS_E1_SX_MMF = _HpnicfevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 165)
)
_HpnicfevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_CPOS_T1_SX_MMF = _HpnicfevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 166)
)
_HpnicfevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_CPOS_E1_LX_SMF = _HpnicfevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 167)
)
_HpnicfevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_622_CPOS_T1_LX_SMF = _HpnicfevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 168)
)
_HpnicfevtPortSw_E1_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_E1_CONNECTOR = _HpnicfevtPortSw_E1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 169)
)
_HpnicfevtPortSw_T1_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_T1_CONNECTOR = _HpnicfevtPortSw_T1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 170)
)
_HpnicfevtPortSw_1000BASE_STK_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_STK_SFP = _HpnicfevtPortSw_1000BASE_STK_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 171)
)
_HpnicfevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_BIDI_SFP = _HpnicfevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 172)
)
_HpnicfevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_1000BASE_CWDM_SFP = _HpnicfevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 173)
)
_HpnicfevtPortSw_100BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100BASE_BIDI_SFP = _HpnicfevtPortSw_100BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 174)
)
_HpnicfevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_OLT_1000BASE_PX_SFP = _HpnicfevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 175)
)
_HpnicfevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_OLT_1000BASE_NO_CONNECTOR = _HpnicfevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 176)
)
_HpnicfevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_PHYGE_CONNECTOR = _HpnicfevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 177)
)
_HpnicfevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_LOGICGE_CONNECTOR = _HpnicfevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 178)
)
_HpnicfevtPortSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100M_1550_BIDI = _HpnicfevtPortSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 179)
)
_HpnicfevtPortSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100M_1310_BIDI = _HpnicfevtPortSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 180)
)
_HpnicfevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_PHYOC48_CONNECTOR = _HpnicfevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 181)
)
_HpnicfevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RPR_LOGICOC48_CONNECTOR = _HpnicfevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 182)
)
_HpnicfevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_100_1000_BASE_LX_SMF = _HpnicfevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 183)
)
_HpnicfevtPortSw_10G_ZW_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_ZW_SM_LC = _HpnicfevtPortSw_10G_ZW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 184)
)
_HpnicfevtPortSw_10G_ZR_SM_LC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10G_ZR_SM_LC = _HpnicfevtPortSw_10G_ZR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 185)
)
_HpnicfevtPortSw_XPK_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XPK_10GBASE_ZR = _HpnicfevtPortSw_XPK_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 186)
)
_HpnicfevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SGMII_100_BASE_LX_SFP = _HpnicfevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 187)
)
_HpnicfevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SGMII_100_BASE_FX_SFP = _HpnicfevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 188)
)
_HpnicfevtPortSw_WLAN_RADIO_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_WLAN_RADIO = _HpnicfevtPortSw_WLAN_RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 189)
)
_HpnicfevtPortSw_CABLE_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CABLE = _HpnicfevtPortSw_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 190)
)
_HpnicfevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_NO_CONNECTOR = _HpnicfevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 191)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_SR = _HpnicfevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 192)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_LR = _HpnicfevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 193)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_LRM = _HpnicfevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 194)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_Cu = _HpnicfevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 195)
)
_HpnicfevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_UNKNOWN = _HpnicfevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 196)
)
_HpnicfevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_STACK_CONNECTOR = _HpnicfevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 197)
)
_HpnicfevtPortSw_POS_L_64_4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_POS_L_64_4 = _HpnicfevtPortSw_POS_L_64_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 198)
)
_HpnicfevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_MINISAS_HD_STACK_CONNECTOR = _HpnicfevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 199)
)
_HpnicfevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_ONU_1000BASE_PX_SFF = _HpnicfevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 200)
)
_HpnicfevtPortSw_RS485_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_RS485 = _HpnicfevtPortSw_RS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 201)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_ER = _HpnicfevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 202)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_ZR = _HpnicfevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 203)
)
_HpnicfevtPortSw_XFP_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_XFP_10GBASE_ZR = _HpnicfevtPortSw_XFP_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 204)
)
_HpnicfevtPortSw_QSFP_PLUS_40GBASE_SR4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_40GBASE_SR4 = _HpnicfevtPortSw_QSFP_PLUS_40GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 205)
)
_HpnicfevtPortSw_QSFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_STACK_CONNECTOR = _HpnicfevtPortSw_QSFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 206)
)
_HpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR = _HpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 207)
)
_HpnicfevtPortSw_SFP_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_STACK_CONNECTOR = _HpnicfevtPortSw_SFP_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 208)
)
_HpnicfevtPortSw_QSFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_NO_CONNECTOR = _HpnicfevtPortSw_QSFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 209)
)
_HpnicfevtPortSw_10GBase_T_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_10GBase_T = _HpnicfevtPortSw_10GBase_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 210)
)
_HpnicfevtPortSw_CFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_NO_CONNECTOR = _HpnicfevtPortSw_CFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 211)
)
_HpnicfevtPortSw_CFP_40GBASE_LR4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_40GBASE_LR4 = _HpnicfevtPortSw_CFP_40GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 212)
)
_HpnicfevtPortSw_QSFP_PLUS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_NO_CONNECTOR = _HpnicfevtPortSw_QSFP_PLUS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 213)
)
_HpnicfevtPortSw_QSFP_PLUS_40GBASE_LR4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_40GBASE_LR4 = _HpnicfevtPortSw_QSFP_PLUS_40GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 214)
)
_HpnicfevtPortSw_CFP_40GBASE_SR4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_40GBASE_SR4 = _HpnicfevtPortSw_CFP_40GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 215)
)
_HpnicfevtPortSw_CFP_100GBASE_LR4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_100GBASE_LR4 = _HpnicfevtPortSw_CFP_100GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 216)
)
_HpnicfevtPortSw_CFP_100GBASE_SR10_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_100GBASE_SR10 = _HpnicfevtPortSw_CFP_100GBASE_SR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 217)
)
_HpnicfevtPortSw_CXP_100GBASE_SR10_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CXP_100GBASE_SR10 = _HpnicfevtPortSw_CXP_100GBASE_SR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 218)
)
_HpnicfevtPortSw_CXP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CXP_NO_CONNECTOR = _HpnicfevtPortSw_CXP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 219)
)
_HpnicfevtPortSw_TRANSCEIVER_UNKNOWN_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_TRANSCEIVER_UNKNOWN = _HpnicfevtPortSw_TRANSCEIVER_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 220)
)
_HpnicfevtPortSw_QSFP_PLUS_UNKNOWN_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_UNKNOWN = _HpnicfevtPortSw_QSFP_PLUS_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 221)
)
_HpnicfevtPortSw_CFP_UNKNOWN_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_UNKNOWN = _HpnicfevtPortSw_CFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 222)
)
_HpnicfevtPortSw_QSFP_PLUS_40GBASE_CSR4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_40GBASE_CSR4 = _HpnicfevtPortSw_QSFP_PLUS_40GBASE_CSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 223)
)
_HpnicfevtPortSw_CFP_40GBASE_ER4_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CFP_40GBASE_ER4 = _HpnicfevtPortSw_CFP_40GBASE_ER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 224)
)
_HpnicfevtPortSw_SFP_1000BASE_BIDI_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_1000BASE_BIDI = _HpnicfevtPortSw_SFP_1000BASE_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 225)
)
_HpnicfevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM = _HpnicfevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 226)
)
_HpnicfevtPortSw_QSFP_PLUS_40GBASE_PSM_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_40GBASE_PSM = _HpnicfevtPortSw_QSFP_PLUS_40GBASE_PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 227)
)
_HpnicfevtPortSw_SFP_8GFC_SW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_8GFC_SW = _HpnicfevtPortSw_SFP_8GFC_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 228)
)
_HpnicfevtPortSw_SFP_8GFC_LW_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_SFP_8GFC_LW = _HpnicfevtPortSw_SFP_8GFC_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 229)
)
_HpnicfevtPortSw_CXP_100GBASE_AOC_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_CXP_100GBASE_AOC = _HpnicfevtPortSw_CXP_100GBASE_AOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 230)
)
_HpnicfevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR = _HpnicfevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 231)
)
_HpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR = _HpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 10, 4, 232)
)
_HpnicfevtStack_ObjectIdentity = ObjectIdentity
hpnicfevtStack = _HpnicfevtStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ENTITY-VENDORTYPE-OID-MIB",
    **{"hpnicfEntityVendorTypeOID": hpnicfEntityVendorTypeOID,
       "hpnicfEntityVendortypeObjects": hpnicfEntityVendortypeObjects,
       "hpnicfevtOther": hpnicfevtOther,
       "hpnicfevtOtherUnknownCard": hpnicfevtOtherUnknownCard,
       "hpnicfevtCPU": hpnicfevtCPU,
       "hpnicfevtGeneralCPU": hpnicfevtGeneralCPU,
       "hpnicfevtDOM": hpnicfevtDOM,
       "hpnicfevtCFCard": hpnicfevtCFCard,
       "hpnicfevtHardDisk": hpnicfevtHardDisk,
       "hpnicfevtUnknown": hpnicfevtUnknown,
       "hpnicfevtChassis": hpnicfevtChassis,
       "hpnicfevtBackplane": hpnicfevtBackplane,
       "hpnicfevtContainer": hpnicfevtContainer,
       "hpnicfevtPowerSupply": hpnicfevtPowerSupply,
       "hpnicfevtPowerSupplyAC": hpnicfevtPowerSupplyAC,
       "hpnicfevtPowerSupplyDC": hpnicfevtPowerSupplyDC,
       "hpnicfevtPowerSupplySTD130W": hpnicfevtPowerSupplySTD130W,
       "hpnicfevtPowerSupplySTD180W": hpnicfevtPowerSupplySTD180W,
       "hpnicfevtPowerSupplyPOE24Port": hpnicfevtPowerSupplyPOE24Port,
       "hpnicfevtPowerSupplyPOE48Port": hpnicfevtPowerSupplyPOE48Port,
       "hpnicfevtFan": hpnicfevtFan,
       "hpnicfevtHotSwapFan": hpnicfevtHotSwapFan,
       "hpnicfevtNonHotSwapFan": hpnicfevtNonHotSwapFan,
       "hpnicfevtSensor": hpnicfevtSensor,
       "hpnicfevtSensorTemperature": hpnicfevtSensorTemperature,
       "hpnicfevtSensorVoltage": hpnicfevtSensorVoltage,
       "hpnicfevtSensorFanSpeed": hpnicfevtSensorFanSpeed,
       "hpnicfevtModule": hpnicfevtModule,
       "hpnicfevtModuleUnknownCard": hpnicfevtModuleUnknownCard,
       "hpnicfevtModuleCommonCards": hpnicfevtModuleCommonCards,
       "hpnicfevtModuleBoxCEN": hpnicfevtModuleBoxCEN,
       "hpnicfevtModuleBoxIRF48GE": hpnicfevtModuleBoxIRF48GE,
       "hpnicfevtModuleBoxIRF24GE24TGE": hpnicfevtModuleBoxIRF24GE24TGE,
       "hpnicfevtModuleChassisMpu": hpnicfevtModuleChassisMpu,
       "hpnicfevtModuleLPU48GE": hpnicfevtModuleLPU48GE,
       "hpnicfevtModuleLPU4GE4Serial": hpnicfevtModuleLPU4GE4Serial,
       "hpnicfevtModuleLPU4GE4Pos": hpnicfevtModuleLPU4GE4Pos,
       "hpnicfevtModuleLPU4GE4E1": hpnicfevtModuleLPU4GE4E1,
       "hpnicfevtModuleRouterType": hpnicfevtModuleRouterType,
       "hpnicfevtModuleRt-As": hpnicfevtModuleRt_As,
       "hpnicfevtModuleRt-Sa": hpnicfevtModuleRt_Sa,
       "hpnicfevtModuleRt-Bi": hpnicfevtModuleRt_Bi,
       "hpnicfevtModuleRt-E12": hpnicfevtModuleRt_E12,
       "hpnicfevtModuleRt-E14": hpnicfevtModuleRt_E14,
       "hpnicfevtModuleRt-Fe1": hpnicfevtModuleRt_Fe1,
       "hpnicfevtModuleRt-E1": hpnicfevtModuleRt_E1,
       "hpnicfevtModuleRt-Fe2": hpnicfevtModuleRt_Fe2,
       "hpnicfevtModuleRt-Vi2": hpnicfevtModuleRt_Vi2,
       "hpnicfevtModuleRt-Vi4": hpnicfevtModuleRt_Vi4,
       "hpnicfevtModuleRt-Vi30": hpnicfevtModuleRt_Vi30,
       "hpnicfevtModuleRt-S1b": hpnicfevtModuleRt_S1b,
       "hpnicfevtModuleRt-Sa2": hpnicfevtModuleRt_Sa2,
       "hpnicfevtModuleRt-As16": hpnicfevtModuleRt_As16,
       "hpnicfevtModuleRt-New8as": hpnicfevtModuleRt_New8as,
       "hpnicfevtModuleRt-Sa1": hpnicfevtModuleRt_Sa1,
       "hpnicfevtModuleRt-Fxs2": hpnicfevtModuleRt_Fxs2,
       "hpnicfevtModuleRt-Fxo2": hpnicfevtModuleRt_Fxo2,
       "hpnicfevtModuleRt-Em2": hpnicfevtModuleRt_Em2,
       "hpnicfevtModuleRt-Fxs4": hpnicfevtModuleRt_Fxs4,
       "hpnicfevtModuleRt-Fxo4": hpnicfevtModuleRt_Fxo4,
       "hpnicfevtModuleRt-Em4": hpnicfevtModuleRt_Em4,
       "hpnicfevtModuleRt-Sab": hpnicfevtModuleRt_Sab,
       "hpnicfevtModuleRt-E1vi": hpnicfevtModuleRt_E1vi,
       "hpnicfevtModuleRt-Am12": hpnicfevtModuleRt_Am12,
       "hpnicfevtModuleRt-Am6": hpnicfevtModuleRt_Am6,
       "hpnicfevtModuleRt-Ndec": hpnicfevtModuleRt_Ndec,
       "hpnicfevtModuleRt-Newsa2": hpnicfevtModuleRt_Newsa2,
       "hpnicfevtModuleRt-Aux": hpnicfevtModuleRt_Aux,
       "hpnicfevtModuleRt-Console": hpnicfevtModuleRt_Console,
       "hpnicfevtModuleRt-Sic-wan": hpnicfevtModuleRt_Sic_wan,
       "hpnicfevtModuleRt-Sic-1fe": hpnicfevtModuleRt_Sic_1fe,
       "hpnicfevtModuleRt-Sic-1sa": hpnicfevtModuleRt_Sic_1sa,
       "hpnicfevtModuleRt-Sic-3as": hpnicfevtModuleRt_Sic_3as,
       "hpnicfevtModuleRt-Sic-1e1": hpnicfevtModuleRt_Sic_1e1,
       "hpnicfevtModuleRt-Sic-1t1": hpnicfevtModuleRt_Sic_1t1,
       "hpnicfevtModuleRt-Sic-1bu": hpnicfevtModuleRt_Sic_1bu,
       "hpnicfevtModuleRt-Sic-2bu": hpnicfevtModuleRt_Sic_2bu,
       "hpnicfevtModuleRt-Sic-1bs": hpnicfevtModuleRt_Sic_1bs,
       "hpnicfevtModuleRt-Sic-2bs": hpnicfevtModuleRt_Sic_2bs,
       "hpnicfevtModuleRt-Sic-1am": hpnicfevtModuleRt_Sic_1am,
       "hpnicfevtModuleRt-Sic-2am": hpnicfevtModuleRt_Sic_2am,
       "hpnicfevtModuleRt-Sic-1em": hpnicfevtModuleRt_Sic_1em,
       "hpnicfevtModuleRt-Sic-2em": hpnicfevtModuleRt_Sic_2em,
       "hpnicfevtModuleRt-Sic-1fxs": hpnicfevtModuleRt_Sic_1fxs,
       "hpnicfevtModuleRt-Sic-2fxs": hpnicfevtModuleRt_Sic_2fxs,
       "hpnicfevtModuleRt-Sic-1fxo": hpnicfevtModuleRt_Sic_1fxo,
       "hpnicfevtModuleRt-Sic-2fxo": hpnicfevtModuleRt_Sic_2fxo,
       "hpnicfevtModuleRt-Fcm6": hpnicfevtModuleRt_Fcm6,
       "hpnicfevtModuleRt-Sa8": hpnicfevtModuleRt_Sa8,
       "hpnicfevtModuleRt-T11": hpnicfevtModuleRt_T11,
       "hpnicfevtModuleRt-T12": hpnicfevtModuleRt_T12,
       "hpnicfevtModuleRt-T14": hpnicfevtModuleRt_T14,
       "hpnicfevtModuleRt-T1vi": hpnicfevtModuleRt_T1vi,
       "hpnicfevtModuleRt-Fcm4": hpnicfevtModuleRt_Fcm4,
       "hpnicfevtModuleRt-Fcm2": hpnicfevtModuleRt_Fcm2,
       "hpnicfevtModuleRt-Rtb21ce3": hpnicfevtModuleRt_Rtb21ce3,
       "hpnicfevtModuleRt-Ame6": hpnicfevtModuleRt_Ame6,
       "hpnicfevtModuleRt-Ame12": hpnicfevtModuleRt_Ame12,
       "hpnicfevtModuleRt-E11-f": hpnicfevtModuleRt_E11_f,
       "hpnicfevtModuleRt-E12-f": hpnicfevtModuleRt_E12_f,
       "hpnicfevtModuleRt-E14-f": hpnicfevtModuleRt_E14_f,
       "hpnicfevtModuleRt-T11-f": hpnicfevtModuleRt_T11_f,
       "hpnicfevtModuleRt-T12-f": hpnicfevtModuleRt_T12_f,
       "hpnicfevtModuleRt-T14-f": hpnicfevtModuleRt_T14_f,
       "hpnicfevtModuleRt-E11-f-17": hpnicfevtModuleRt_E11_f_17,
       "hpnicfevtModuleRt-T11-f-17": hpnicfevtModuleRt_T11_f_17,
       "hpnicfevtModuleRt-Rtb21ct3": hpnicfevtModuleRt_Rtb21ct3,
       "hpnicfevtModuleRt-Atmadsl1": hpnicfevtModuleRt_Atmadsl1,
       "hpnicfevtModuleRt-Atmadsl2": hpnicfevtModuleRt_Atmadsl2,
       "hpnicfevtModuleRt-Atm155m": hpnicfevtModuleRt_Atm155m,
       "hpnicfevtModuleRt-Ase8": hpnicfevtModuleRt_Ase8,
       "hpnicfevtModuleRt-Ase16": hpnicfevtModuleRt_Ase16,
       "hpnicfevtModuleRt-Sae4": hpnicfevtModuleRt_Sae4,
       "hpnicfevtModuleRt-Sae2": hpnicfevtModuleRt_Sae2,
       "hpnicfevtModuleRt-Atmshdsl1": hpnicfevtModuleRt_Atmshdsl1,
       "hpnicfevtModuleRt-Atmshdsl2": hpnicfevtModuleRt_Atmshdsl2,
       "hpnicfevtModuleRt-Atmshdsl4": hpnicfevtModuleRt_Atmshdsl4,
       "hpnicfevtModuleRt-Atm25m": hpnicfevtModuleRt_Atm25m,
       "hpnicfevtModuleRt-Atme3": hpnicfevtModuleRt_Atme3,
       "hpnicfevtModuleRt-Atmt3": hpnicfevtModuleRt_Atmt3,
       "hpnicfevtModuleRt-Xdsl-fec": hpnicfevtModuleRt_Xdsl_fec,
       "hpnicfevtModuleRt-Xdsl-adsl": hpnicfevtModuleRt_Xdsl_adsl,
       "hpnicfevtModuleRt-Xdsl-gshdsl": hpnicfevtModuleRt_Xdsl_gshdsl,
       "hpnicfevtModuleRt-Xdsl-bri": hpnicfevtModuleRt_Xdsl_bri,
       "hpnicfevtModuleRt-Xdsl-scc": hpnicfevtModuleRt_Xdsl_scc,
       "hpnicfevtModuleRt-Ge1": hpnicfevtModuleRt_Ge1,
       "hpnicfevtModuleRt-Pos155m": hpnicfevtModuleRt_Pos155m,
       "hpnicfevtModuleRt-Cpos": hpnicfevtModuleRt_Cpos,
       "hpnicfevtModuleRt-Fe1op": hpnicfevtModuleRt_Fe1op,
       "hpnicfevtModuleRt-Sae8": hpnicfevtModuleRt_Sae8,
       "hpnicfevtModuleRt-Atm155m-mm": hpnicfevtModuleRt_Atm155m_mm,
       "hpnicfevtModuleRt-Atm155m-sm": hpnicfevtModuleRt_Atm155m_sm,
       "hpnicfevtModuleRt-Atm155m-sml": hpnicfevtModuleRt_Atm155m_sml,
       "hpnicfevtModuleRt-Fe1op-sfx": hpnicfevtModuleRt_Fe1op_sfx,
       "hpnicfevtModuleRt-Fe1op-mfx": hpnicfevtModuleRt_Fe1op_mfx,
       "hpnicfevtModuleRt-Cpos-t1": hpnicfevtModuleRt_Cpos_t1,
       "hpnicfevtModuleRt-Ge1op": hpnicfevtModuleRt_Ge1op,
       "hpnicfevtModuleRt-Ge2op": hpnicfevtModuleRt_Ge2op,
       "hpnicfevtModuleRt-Ge2": hpnicfevtModuleRt_Ge2,
       "hpnicfevtModuleRt-Fix-1wan": hpnicfevtModuleRt_Fix_1wan,
       "hpnicfevtModuleRt-Fix-1sae": hpnicfevtModuleRt_Fix_1sae,
       "hpnicfevtModuleRt-Cavium": hpnicfevtModuleRt_Cavium,
       "hpnicfevtModuleRt-Sic1Eth": hpnicfevtModuleRt_Sic1Eth,
       "hpnicfevtModuleRt-atm1ADSLI": hpnicfevtModuleRt_atm1ADSLI,
       "hpnicfevtModuleRt-atm2ADSLI": hpnicfevtModuleRt_atm2ADSLI,
       "hpnicfevtModuleRt-fix-e11": hpnicfevtModuleRt_fix_e11,
       "hpnicfevtModuleRt-fix-t11": hpnicfevtModuleRt_fix_t11,
       "hpnicfevtModuleRt-e18-75": hpnicfevtModuleRt_e18_75,
       "hpnicfevtModuleRt-e18-120": hpnicfevtModuleRt_e18_120,
       "hpnicfevtModuleRt-t18": hpnicfevtModuleRt_t18,
       "hpnicfevtModuleRt-sic-1vifxs": hpnicfevtModuleRt_sic_1vifxs,
       "hpnicfevtModuleRt-sic-1vifxo": hpnicfevtModuleRt_sic_1vifxo,
       "hpnicfevtModuleRt-sic-2vifxs": hpnicfevtModuleRt_sic_2vifxs,
       "hpnicfevtModuleRt-sic-2vifxo": hpnicfevtModuleRt_sic_2vifxo,
       "hpnicfevtModuleRt-xdsl-fec-new": hpnicfevtModuleRt_xdsl_fec_new,
       "hpnicfevtModuleRt-xdsl-sa": hpnicfevtModuleRt_xdsl_sa,
       "hpnicfevtModuleRt-bs4": hpnicfevtModuleRt_bs4,
       "hpnicfevtModuleRt-ima-8e175": hpnicfevtModuleRt_ima_8e175,
       "hpnicfevtModuleRt-ima-8e1120": hpnicfevtModuleRt_ima_8e1120,
       "hpnicfevtModuleRt-ima-4e175": hpnicfevtModuleRt_ima_4e175,
       "hpnicfevtModuleRt-ima-4e1120": hpnicfevtModuleRt_ima_4e1120,
       "hpnicfevtModuleRt-ima-8t1": hpnicfevtModuleRt_ima_8t1,
       "hpnicfevtModuleRt-ima-4t1": hpnicfevtModuleRt_ima_4t1,
       "hpnicfevtModuleRt-sic-1t1f": hpnicfevtModuleRt_sic_1t1f,
       "hpnicfevtModuleRt-sic-1e1f": hpnicfevtModuleRt_sic_1e1f,
       "hpnicfevtModuleRt-VG-16fxs": hpnicfevtModuleRt_VG_16fxs,
       "hpnicfevtModuleRt-VG-32fxs": hpnicfevtModuleRt_VG_32fxs,
       "hpnicfevtModuleRt-VG-8fxo": hpnicfevtModuleRt_VG_8fxo,
       "hpnicfevtModuleRt-VG-2fe": hpnicfevtModuleRt_VG_2fe,
       "hpnicfevtModuleRt-sib": hpnicfevtModuleRt_sib,
       "hpnicfevtModuleRt-cie32": hpnicfevtModuleRt_cie32,
       "hpnicfevtModuleRt-cie64": hpnicfevtModuleRt_cie64,
       "hpnicfevtModuleRt-cie96": hpnicfevtModuleRt_cie96,
       "hpnicfevtModuleRt-Fe4": hpnicfevtModuleRt_Fe4,
       "hpnicfevtModuleRt-fxs4fxo1": hpnicfevtModuleRt_fxs4fxo1,
       "hpnicfevtModuleRt-atm1shdsl4wire": hpnicfevtModuleRt_atm1shdsl4wire,
       "hpnicfevtModuleRt-atmIma4shdsl": hpnicfevtModuleRt_atmIma4shdsl,
       "hpnicfevtModuleRt-ls4": hpnicfevtModuleRt_ls4,
       "hpnicfevtModuleRt-ls8": hpnicfevtModuleRt_ls8,
       "hpnicfevtModuleRt-ls16": hpnicfevtModuleRt_ls16,
       "hpnicfevtModuleRt-sic-adls2plus-isdn": hpnicfevtModuleRt_sic_adls2plus_isdn,
       "hpnicfevtModuleRt-sic-adls2plus-pots": hpnicfevtModuleRt_sic_adls2plus_pots,
       "hpnicfevtModuleRt-ft3": hpnicfevtModuleRt_ft3,
       "hpnicfevtModuleRt-ce32": hpnicfevtModuleRt_ce32,
       "hpnicfevtModuleRt-bsv2": hpnicfevtModuleRt_bsv2,
       "hpnicfevtModuleRt-bsv4": hpnicfevtModuleRt_bsv4,
       "hpnicfevtModuleRt-RPU": hpnicfevtModuleRt_RPU,
       "hpnicfevtModuleRt-ERPU": hpnicfevtModuleRt_ERPU,
       "hpnicfevtModuleRt-SSL": hpnicfevtModuleRt_SSL,
       "hpnicfevtModuleRt-NSA": hpnicfevtModuleRt_NSA,
       "hpnicfevtModuleRT-SIC-1GEC": hpnicfevtModuleRT_SIC_1GEC,
       "hpnicfevtModuleRT-24FSW": hpnicfevtModuleRT_24FSW,
       "hpnicfevtModuleRT-24FSWP": hpnicfevtModuleRT_24FSWP,
       "hpnicfevtModuleRT-16FSW": hpnicfevtModuleRT_16FSW,
       "hpnicfevtModuleRT-16FSWP": hpnicfevtModuleRT_16FSWP,
       "hpnicfevtModuleRT-1VE1": hpnicfevtModuleRT_1VE1,
       "hpnicfevtModuleRT-1VT1": hpnicfevtModuleRT_1VT1,
       "hpnicfevtModuleRT-2VE1": hpnicfevtModuleRT_2VE1,
       "hpnicfevtModuleRT-2VT1": hpnicfevtModuleRT_2VT1,
       "hpnicfevtModuleRT-SIC-4FSW": hpnicfevtModuleRT_SIC_4FSW,
       "hpnicfevtModuleRT-SIC-4FSWP": hpnicfevtModuleRT_SIC_4FSWP,
       "hpnicfevtModuleRT-DSIC-9FSW": hpnicfevtModuleRT_DSIC_9FSW,
       "hpnicfevtModuleRT-DSIC-9FSWP": hpnicfevtModuleRT_DSIC_9FSWP,
       "hpnicfevtModuleRT-SIC-1VE1": hpnicfevtModuleRT_SIC_1VE1,
       "hpnicfevtModuleRT-SIC-1VT1": hpnicfevtModuleRT_SIC_1VT1,
       "hpnicfevtModuleRT-VCPM": hpnicfevtModuleRT_VCPM,
       "hpnicfevtModuleRT-VPM": hpnicfevtModuleRT_VPM,
       "hpnicfevtModuleRT-VPMA": hpnicfevtModuleRT_VPMA,
       "hpnicfevtModuleRT-VPMB": hpnicfevtModuleRT_VPMB,
       "hpnicfevtModuleRT-VPMC": hpnicfevtModuleRT_VPMC,
       "hpnicfevtModuleRt-fe18-75": hpnicfevtModuleRt_fe18_75,
       "hpnicfevtModuleRt-fe18-120": hpnicfevtModuleRt_fe18_120,
       "hpnicfevtModuleRt-ft18": hpnicfevtModuleRt_ft18,
       "hpnicfevtModuleRt-CF": hpnicfevtModuleRt_CF,
       "hpnicfevtModuleRt-bsv2-v2": hpnicfevtModuleRt_bsv2_v2,
       "hpnicfevtModuleRt-e1vi1-v2": hpnicfevtModuleRt_e1vi1_v2,
       "hpnicfevtModuleRt-e1vi2": hpnicfevtModuleRt_e1vi2,
       "hpnicfevtModuleRt-t1vi1-v2": hpnicfevtModuleRt_t1vi1_v2,
       "hpnicfevtModuleRt-t1vi2": hpnicfevtModuleRt_t1vi2,
       "hpnicfevtModuleRt-osm": hpnicfevtModuleRt_osm,
       "hpnicfevtModuleRt-sd707": hpnicfevtModuleRt_sd707,
       "hpnicfevtModuleRt-dm-epri": hpnicfevtModuleRt_dm_epri,
       "hpnicfevtModuleRt-dm-tpri": hpnicfevtModuleRt_dm_tpri,
       "hpnicfevtModuleRt-ERPU-H": hpnicfevtModuleRt_ERPU_H,
       "hpnicfevtModuleRT-SIC-1BSV": hpnicfevtModuleRT_SIC_1BSV,
       "hpnicfevtModuleRT-SIC-2BSV": hpnicfevtModuleRT_SIC_2BSV,
       "hpnicfevtModuleRt-gbe8": hpnicfevtModuleRt_gbe8,
       "hpnicfevtModuleRt-gbe4": hpnicfevtModuleRt_gbe4,
       "hpnicfevtModuleRt-cpos2-v2": hpnicfevtModuleRt_cpos2_v2,
       "hpnicfevtModuleRt-cpos1-v2": hpnicfevtModuleRt_cpos1_v2,
       "hpnicfevtModuleRt-oap": hpnicfevtModuleRt_oap,
       "hpnicfevtModuleRT-48FSWP": hpnicfevtModuleRT_48FSWP,
       "hpnicfevtModuleRT-48FSW": hpnicfevtModuleRT_48FSW,
       "hpnicfevtModuleRT-ASM": hpnicfevtModuleRT_ASM,
       "hpnicfevtModuleRT-SIC-1FEF": hpnicfevtModuleRT_SIC_1FEF,
       "hpnicfevtModuleRT-XMIM-24FSW": hpnicfevtModuleRT_XMIM_24FSW,
       "hpnicfevtModuleRT-WLAN-AG-1RADIO": hpnicfevtModuleRT_WLAN_AG_1RADIO,
       "hpnicfevtModuleRT-1CE3": hpnicfevtModuleRT_1CE3,
       "hpnicfevtModuleRT-XMIM-16FSW": hpnicfevtModuleRT_XMIM_16FSW,
       "hpnicfevtModuleRT-OAPS": hpnicfevtModuleRT_OAPS,
       "hpnicfevtModuleRT-NAM": hpnicfevtModuleRT_NAM,
       "hpnicfevtModuleRT-RPE-X1": hpnicfevtModuleRT_RPE_X1,
       "hpnicfevtModuleRT-FIP-100": hpnicfevtModuleRT_FIP_100,
       "hpnicfevtModuleRT-FIP-200": hpnicfevtModuleRT_FIP_200,
       "hpnicfevtModuleRT-SIC-8AS": hpnicfevtModuleRT_SIC_8AS,
       "hpnicfevtModuleRT-WAAM": hpnicfevtModuleRT_WAAM,
       "hpnicfevtModuleRt-msp4p-OC3c": hpnicfevtModuleRt_msp4p_OC3c,
       "hpnicfevtModuleRt-1pos-oc48": hpnicfevtModuleRt_1pos_oc48,
       "hpnicfevtModuleRt-xgbe": hpnicfevtModuleRt_xgbe,
       "hpnicfevtModuleRT-EADM": hpnicfevtModuleRT_EADM,
       "hpnicfevtModuleRT-VCM": hpnicfevtModuleRT_VCM,
       "hpnicfevtModuleRT-SIC-2FXS1FXO": hpnicfevtModuleRT_SIC_2FXS1FXO,
       "hpnicfevtModuleRT-8FXS8FXO": hpnicfevtModuleRT_8FXS8FXO,
       "hpnicfevtModuleRT-16FXS": hpnicfevtModuleRT_16FXS,
       "hpnicfevtModuleRT-OAPS-ICM": hpnicfevtModuleRT_OAPS_ICM,
       "hpnicfevtModuleRT-OAP-ICM": hpnicfevtModuleRT_OAP_ICM,
       "hpnicfevtModuleRT-8fe": hpnicfevtModuleRT_8fe,
       "hpnicfevtModuleRT-4gbp": hpnicfevtModuleRT_4gbp,
       "hpnicfevtModuleRT-MPU-G2": hpnicfevtModuleRT_MPU_G2,
       "hpnicfevtModuleRT-OAPS-OCE": hpnicfevtModuleRT_OAPS_OCE,
       "hpnicfevtModuleRT-OAP-OCE": hpnicfevtModuleRT_OAP_OCE,
       "hpnicfevtModuleRT-OAPS-ICE": hpnicfevtModuleRT_OAPS_ICE,
       "hpnicfevtModuleRT-OAP-ICE": hpnicfevtModuleRT_OAP_ICE,
       "hpnicfevtModuleRT-SIC-16AS": hpnicfevtModuleRT_SIC_16AS,
       "hpnicfevtModuleRT-SPE-FWM": hpnicfevtModuleRT_SPE_FWM,
       "hpnicfevtModuleRT-cls2p": hpnicfevtModuleRT_cls2p,
       "hpnicfevtModuleRT-cls1p": hpnicfevtModuleRT_cls1p,
       "hpnicfevtModuleRT-SIC-2E1-F": hpnicfevtModuleRT_SIC_2E1_F,
       "hpnicfevtModuleRT-SIC-1E1-F-V2": hpnicfevtModuleRT_SIC_1E1_F_V2,
       "hpnicfevtModuleRT-MCU": hpnicfevtModuleRT_MCU,
       "hpnicfevtModuleRT-ACU": hpnicfevtModuleRT_ACU,
       "hpnicfevtModuleRT-1ATM-OC3": hpnicfevtModuleRT_1ATM_OC3,
       "hpnicfevtModuleRT-RSE-X1": hpnicfevtModuleRT_RSE_X1,
       "hpnicfevtModuleRT-FIP-210": hpnicfevtModuleRT_FIP_210,
       "hpnicfevtModuleRT-1expa": hpnicfevtModuleRT_1expa,
       "hpnicfevtModuleRT-WLAN-SIC-N-1RADIO": hpnicfevtModuleRT_WLAN_SIC_N_1RADIO,
       "hpnicfevtModuleRT-WLAN-SIC-BG-1RADIO": hpnicfevtModuleRT_WLAN_SIC_BG_1RADIO,
       "hpnicfevtModuleRT-al2p": hpnicfevtModuleRT_al2p,
       "hpnicfevtModuleRT-msp2p-OC3c": hpnicfevtModuleRT_msp2p_OC3c,
       "hpnicfevtModuleRT-8gbp": hpnicfevtModuleRT_8gbp,
       "hpnicfevtModuleRT-SIC-EPON": hpnicfevtModuleRT_SIC_EPON,
       "hpnicfevtModuleRT-SIC-3G-GSM-H3": hpnicfevtModuleRT_SIC_3G_GSM_H3,
       "hpnicfevtModuleRT-msp2p-OC12c": hpnicfevtModuleRT_msp2p_OC12c,
       "hpnicfevtModuleRt-msp4p-OC12c": hpnicfevtModuleRt_msp4p_OC12c,
       "hpnicfevtModuleRt-al1p": hpnicfevtModuleRt_al1p,
       "hpnicfevtModuleRt-OAP-100": hpnicfevtModuleRt_OAP_100,
       "hpnicfevtModuleRt-FIP-110": hpnicfevtModuleRt_FIP_110,
       "hpnicfevtModuleRt-OSM-SSM": hpnicfevtModuleRt_OSM_SSM,
       "hpnicfevtModuleRt-OAP-SSM": hpnicfevtModuleRt_OAP_SSM,
       "hpnicfevtModuleRt-rs2p": hpnicfevtModuleRt_rs2p,
       "hpnicfevtModuleRt-SAP-48GBE": hpnicfevtModuleRt_SAP_48GBE,
       "hpnicfevtModuleRt-SAP-48GBP": hpnicfevtModuleRt_SAP_48GBP,
       "hpnicfevtModuleRt-SAP-24GBP": hpnicfevtModuleRt_SAP_24GBP,
       "hpnicfevtModuleRt-SPE-SSL": hpnicfevtModuleRt_SPE_SSL,
       "hpnicfevtModuleRt-SIC-AUDIO": hpnicfevtModuleRt_SIC_AUDIO,
       "hpnicfevtModuleRt-FIC-1E1POS-H3": hpnicfevtModuleRt_FIC_1E1POS_H3,
       "hpnicfevtModuleRt-DSIC-4FXS1FXO": hpnicfevtModuleRt_DSIC_4FXS1FXO,
       "hpnicfevtModuleRt-FIC-CPOS": hpnicfevtModuleRt_FIC_CPOS,
       "hpnicfevtModuleRt-DSIC-1SHDSL-8W": hpnicfevtModuleRt_DSIC_1SHDSL_8W,
       "hpnicfevtModuleRt-SIC-3G-TD": hpnicfevtModuleRt_SIC_3G_TD,
       "hpnicfevtModuleRt-SIC-3G-CDMA": hpnicfevtModuleRt_SIC_3G_CDMA,
       "hpnicfevtModuleRt-SIC-3G-HSPA": hpnicfevtModuleRt_SIC_3G_HSPA,
       "hpnicfevtModuleRt-FIC-OAP-V2": hpnicfevtModuleRt_FIC_OAP_V2,
       "hpnicfevtModuleRt-MIM-OAP-V2": hpnicfevtModuleRt_MIM_OAP_V2,
       "hpnicfevtModuleRt-MIM-OAPS-V2": hpnicfevtModuleRt_MIM_OAPS_V2,
       "hpnicfevtModuleRt-HMIM-1CT3": hpnicfevtModuleRt_HMIM_1CT3,
       "hpnicfevtModuleRt-HMIM-1CE3": hpnicfevtModuleRt_HMIM_1CE3,
       "hpnicfevtModuleRt-HMIM-1POS": hpnicfevtModuleRt_HMIM_1POS,
       "hpnicfevtModuleRt-HMIM-2SAE": hpnicfevtModuleRt_HMIM_2SAE,
       "hpnicfevtModuleRt-HMIM-4SAE": hpnicfevtModuleRt_HMIM_4SAE,
       "hpnicfevtModuleRt-HMIM-8SAE": hpnicfevtModuleRt_HMIM_8SAE,
       "hpnicfevtModuleRt-HMIM-8ASE": hpnicfevtModuleRt_HMIM_8ASE,
       "hpnicfevtModuleRt-HMIM-16ASE": hpnicfevtModuleRt_HMIM_16ASE,
       "hpnicfevtModuleRt-HMIM-1E1": hpnicfevtModuleRt_HMIM_1E1,
       "hpnicfevtModuleRt-HMIM-2E1": hpnicfevtModuleRt_HMIM_2E1,
       "hpnicfevtModuleRt-HMIM-4E1": hpnicfevtModuleRt_HMIM_4E1,
       "hpnicfevtModuleRt-HMIM-8E1-75": hpnicfevtModuleRt_HMIM_8E1_75,
       "hpnicfevtModuleRt-HMIM-1E1-F": hpnicfevtModuleRt_HMIM_1E1_F,
       "hpnicfevtModuleRt-HMIM-2E1-F": hpnicfevtModuleRt_HMIM_2E1_F,
       "hpnicfevtModuleRt-HMIM-4E1-F": hpnicfevtModuleRt_HMIM_4E1_F,
       "hpnicfevtModuleRt-HMIM-8E1-F-75": hpnicfevtModuleRt_HMIM_8E1_F_75,
       "hpnicfevtModuleRt-HMIM-6AM": hpnicfevtModuleRt_HMIM_6AM,
       "hpnicfevtModuleRt-HMIM-6FCM": hpnicfevtModuleRt_HMIM_6FCM,
       "hpnicfevtModuleRt-HMIM-2T1": hpnicfevtModuleRt_HMIM_2T1,
       "hpnicfevtModuleRt-HMIM-4T1-F": hpnicfevtModuleRt_HMIM_4T1_F,
       "hpnicfevtModuleRt-HMIM-8T1": hpnicfevtModuleRt_HMIM_8T1,
       "hpnicfevtModuleRt-HMIM-8T1-F": hpnicfevtModuleRt_HMIM_8T1_F,
       "hpnicfevtModuleRt-HMIM-1VE1": hpnicfevtModuleRt_HMIM_1VE1,
       "hpnicfevtModuleRt-HMIM-1VT1": hpnicfevtModuleRt_HMIM_1VT1,
       "hpnicfevtModuleRt-HMIM-2VE1": hpnicfevtModuleRt_HMIM_2VE1,
       "hpnicfevtModuleRt-HMIM-2VT1": hpnicfevtModuleRt_HMIM_2VT1,
       "hpnicfevtModuleRt-HMIM-8FXS8FXO": hpnicfevtModuleRt_HMIM_8FXS8FXO,
       "hpnicfevtModuleRt-HMIM-16FXS": hpnicfevtModuleRt_HMIM_16FXS,
       "hpnicfevtModuleRt-HMIM-4FXS": hpnicfevtModuleRt_HMIM_4FXS,
       "hpnicfevtModuleRt-HMIM-4FXO": hpnicfevtModuleRt_HMIM_4FXO,
       "hpnicfevtModuleRt-HMIM-4EM": hpnicfevtModuleRt_HMIM_4EM,
       "hpnicfevtModuleRt-HMIM-4BSV": hpnicfevtModuleRt_HMIM_4BSV,
       "hpnicfevtModuleRt-SIC-CNDE": hpnicfevtModuleRt_SIC_CNDE,
       "hpnicfevtModuleRt-ESM-CNDE": hpnicfevtModuleRt_ESM_CNDE,
       "hpnicfevtModuleRt-ESM-CNDE-M": hpnicfevtModuleRt_ESM_CNDE_M,
       "hpnicfevtModuleRt-SR6602-X1": hpnicfevtModuleRt_SR6602_X1,
       "hpnicfevtModuleRt-SR6602-X2": hpnicfevtModuleRt_SR6602_X2,
       "hpnicfevtModuleRt-MCP-X1": hpnicfevtModuleRt_MCP_X1,
       "hpnicfevtModuleRt-MCP-X2": hpnicfevtModuleRt_MCP_X2,
       "hpnicfevtModuleRt-FIP-10": hpnicfevtModuleRt_FIP_10,
       "hpnicfevtModuleRt-FIP-20": hpnicfevtModuleRt_FIP_20,
       "hpnicfevtModuleRt-RSE-X2": hpnicfevtModuleRt_RSE_X2,
       "hpnicfevtModuleRt-FIP-600": hpnicfevtModuleRt_FIP_600,
       "hpnicfevtModuleRt-SAP-4EXP": hpnicfevtModuleRt_SAP_4EXP,
       "hpnicfevtModuleRt-SFE-X1": hpnicfevtModuleRt_SFE_X1,
       "hpnicfevtModuleRt-SFE-A1": hpnicfevtModuleRt_SFE_A1,
       "hpnicfevtModuleRt-HMIM-24GSW": hpnicfevtModuleRt_HMIM_24GSW,
       "hpnicfevtModuleRt-HMIM-24GSWP": hpnicfevtModuleRt_HMIM_24GSWP,
       "hpnicfevtModuleRt-MPU100": hpnicfevtModuleRt_MPU100,
       "hpnicfevtModuleRt-SPU100": hpnicfevtModuleRt_SPU100,
       "hpnicfevtModuleRt-SPU200": hpnicfevtModuleRt_SPU200,
       "hpnicfevtModuleRt-WLAN-N-1RADIO": hpnicfevtModuleRt_WLAN_N_1RADIO,
       "hpnicfevtModuleRt-3G-CDMA": hpnicfevtModuleRt_3G_CDMA,
       "hpnicfevtModuleRt-3G-WCDMA": hpnicfevtModuleRt_3G_WCDMA,
       "hpnicfevtModuleRt-3G-HSPAPLUS": hpnicfevtModuleRt_3G_HSPAPLUS,
       "hpnicfevtModuleRt-VPM-128": hpnicfevtModuleRt_VPM_128,
       "hpnicfevtModuleRt-VPM-256": hpnicfevtModuleRt_VPM_256,
       "hpnicfevtModuleRt-VPM-512": hpnicfevtModuleRt_VPM_512,
       "hpnicfevtModuleRt-HMIM-8GEE": hpnicfevtModuleRt_HMIM_8GEE,
       "hpnicfevtModuleRt-HMIM-4GEE": hpnicfevtModuleRt_HMIM_4GEE,
       "hpnicfevtModuleRt-HMIM-2GEE": hpnicfevtModuleRt_HMIM_2GEE,
       "hpnicfevtModuleRt-HMIM-8GEF": hpnicfevtModuleRt_HMIM_8GEF,
       "hpnicfevtModuleRt-HMIM-4GEF": hpnicfevtModuleRt_HMIM_4GEF,
       "hpnicfevtModuleRt-HMIM-2GEF": hpnicfevtModuleRt_HMIM_2GEF,
       "hpnicfevtModuleRt-SPU300": hpnicfevtModuleRt_SPU300,
       "hpnicfevtModuleRt-HMIM-1CPOS": hpnicfevtModuleRt_HMIM_1CPOS,
       "hpnicfevtModuleRt-HMIM-2CPOS": hpnicfevtModuleRt_HMIM_2CPOS,
       "hpnicfevtModuleRt-SPU100-5080": hpnicfevtModuleRt_SPU100_5080,
       "hpnicfevtModuleRt-SPU200-5080": hpnicfevtModuleRt_SPU200_5080,
       "hpnicfevtModuleRt-SPU300-5080": hpnicfevtModuleRt_SPU300_5080,
       "hpnicfevtModuleRt-4G-LTE-Verizon": hpnicfevtModuleRt_4G_LTE_Verizon,
       "hpnicfevtModuleRt-4G-LTE-Global": hpnicfevtModuleRt_4G_LTE_Global,
       "hpnicfevtModuleRt-HMIM-1ATM-OC3": hpnicfevtModuleRt_HMIM_1ATM_OC3,
       "hpnicfevtModuleRt-SIC-1E1-V2": hpnicfevtModuleRt_SIC_1E1_V2,
       "hpnicfevtModuleRt-FIP-300": hpnicfevtModuleRt_FIP_300,
       "hpnicfevtModuleRt-FIP-310": hpnicfevtModuleRt_FIP_310,
       "hpnicfevtModuleRt-TS8P": hpnicfevtModuleRt_TS8P,
       "hpnicfevtModuleRt-4G4P": hpnicfevtModuleRt_4G4P,
       "hpnicfevtModuleRt-SIC-4G-LTE-V": hpnicfevtModuleRt_SIC_4G_LTE_V,
       "hpnicfevtModuleRt-SIC-4G-LTE-A": hpnicfevtModuleRt_SIC_4G_LTE_A,
       "hpnicfevtModuleRt-SIC-4G-LTE-G": hpnicfevtModuleRt_SIC_4G_LTE_G,
       "hpnicfevtModuleRt-SIC-2SAE": hpnicfevtModuleRt_SIC_2SAE,
       "hpnicfevtModuleRt-SIC-4SAE": hpnicfevtModuleRt_SIC_4SAE,
       "hpnicfevtModuleRt-HMIM-OAP": hpnicfevtModuleRt_HMIM_OAP,
       "hpnicfevtModuleRt-HMIM-8GSW": hpnicfevtModuleRt_HMIM_8GSW,
       "hpnicfevtModuleRt-IPU": hpnicfevtModuleRt_IPU,
       "hpnicfevtModuleRt-MIM2GEBE-PCIE": hpnicfevtModuleRt_MIM2GEBE_PCIE,
       "hpnicfevtModuleRt-HIM12GE-PCIE": hpnicfevtModuleRt_HIM12GE_PCIE,
       "hpnicfevtModuleRt-HIM2XGE-PCIE": hpnicfevtModuleRt_HIM2XGE_PCIE,
       "hpnicfevtModuleRt-IPU-T1000-M": hpnicfevtModuleRt_IPU_T1000_M,
       "hpnicfevtModuleRt-IPU-GX4C": hpnicfevtModuleRt_IPU_GX4C,
       "hpnicfevtModuleRt-IPU-GT4C": hpnicfevtModuleRt_IPU_GT4C,
       "hpnicfevtModuleRt-RPU-IAG2000-A": hpnicfevtModuleRt_RPU_IAG2000_A,
       "hpnicfevtModuleRt-RPU-AFD1000-A": hpnicfevtModuleRt_RPU_AFD1000_A,
       "hpnicfevtModuleRt-RPU-F5000-A": hpnicfevtModuleRt_RPU_F5000_A,
       "hpnicfevtModuleRt-ACG-8800S3-MPU": hpnicfevtModuleRt_ACG_8800S3_MPU,
       "hpnicfevtModuleRt-T5000S3-MPU": hpnicfevtModuleRt_T5000S3_MPU,
       "hpnicfevtModuleRt-NS21S2MSPB0": hpnicfevtModuleRt_NS21S2MSPB0,
       "hpnicfevtModuleRt-NS11S2MSPB0": hpnicfevtModuleRt_NS11S2MSPB0,
       "hpnicfevtModuleRt-NSQ1WLAN": hpnicfevtModuleRt_NSQ1WLAN,
       "hpnicfevtModuleRt-NSQ1GP4U0": hpnicfevtModuleRt_NSQ1GP4U0,
       "hpnicfevtModuleRt-NSQ1GP8C40": hpnicfevtModuleRt_NSQ1GP8C40,
       "hpnicfevtModuleRt-NSQ1XS2U0": hpnicfevtModuleRt_NSQ1XS2U0,
       "hpnicfevtModuleRt-NSQ1G24XS60": hpnicfevtModuleRt_NSQ1G24XS60,
       "hpnicfevtModuleRt-NSQ1TGX4EA0": hpnicfevtModuleRt_NSQ1TGX4EA0,
       "hpnicfevtModuleRt-NSQ1FAB08D0": hpnicfevtModuleRt_NSQ1FAB08D0,
       "hpnicfevtModuleRt-NSQ1TGS32SF0": hpnicfevtModuleRt_NSQ1TGS32SF0,
       "hpnicfevtModuleRt-NSQ1QGS4SF0": hpnicfevtModuleRt_NSQ1QGS4SF0,
       "hpnicfevtModuleRt-NSQ1GP24TXEA0": hpnicfevtModuleRt_NSQ1GP24TXEA0,
       "hpnicfevtModuleRt-NSQ1GP48EB0": hpnicfevtModuleRt_NSQ1GP48EB0,
       "hpnicfevtModuleRt-NSQ1FWCEA0": hpnicfevtModuleRt_NSQ1FWCEA0,
       "hpnicfevtModuleRt-NSQ1GT48EA0": hpnicfevtModuleRt_NSQ1GT48EA0,
       "hpnicfevtModuleRt-NSQ1TGS8EA0": hpnicfevtModuleRt_NSQ1TGS8EA0,
       "hpnicfevtModuleRt-NSQ1FAB04B0": hpnicfevtModuleRt_NSQ1FAB04B0,
       "hpnicfevtModuleRt-NSQ1FAB12D0": hpnicfevtModuleRt_NSQ1FAB12D0,
       "hpnicfevtModuleRt-NSQ1SUPB0": hpnicfevtModuleRt_NSQ1SUPB0,
       "hpnicfevtModuleRt-VFW1000": hpnicfevtModuleRt_VFW1000,
       "hpnicfevtModuleRt-NSQ1CGC2SE0": hpnicfevtModuleRt_NSQ1CGC2SE0,
       "hpnicfevtModuleRt-VLB1000": hpnicfevtModuleRt_VLB1000,
       "hpnicfevtModuleRt-VG-8fxs": hpnicfevtModuleRt_VG_8fxs,
       "hpnicfevtModuleRt-VG-24fxs": hpnicfevtModuleRt_VG_24fxs,
       "hpnicfevtModuleRt-VG-24fxs24fxo": hpnicfevtModuleRt_VG_24fxs24fxo,
       "hpnicfevtModuleRt-VG-MPU": hpnicfevtModuleRt_VG_MPU,
       "hpnicfevtModuleRt-MIM-VCX-CONNECT-P-3C": hpnicfevtModuleRt_MIM_VCX_CONNECT_P_3C,
       "hpnicfevtModuleRt-MIM-VCX-CONNECT-S-3C": hpnicfevtModuleRt_MIM_VCX_CONNECT_S_3C,
       "hpnicfevtModuleRt-MIM-VCX-3C": hpnicfevtModuleRt_MIM_VCX_3C,
       "hpnicfevtModuleRt-VNIC-VMXNET3": hpnicfevtModuleRt_VNIC_VMXNET3,
       "hpnicfevtModuleRt-VNIC-E1000": hpnicfevtModuleRt_VNIC_E1000,
       "hpnicfevtModuleRt-VNIC-VIRTIO": hpnicfevtModuleRt_VNIC_VIRTIO,
       "hpnicfevtModuleRt-VNIC-RTL8139": hpnicfevtModuleRt_VNIC_RTL8139,
       "hpnicfevtModuleRt-VNIC-IXGBEVF": hpnicfevtModuleRt_VNIC_IXGBEVF,
       "hpnicfevtModuleRt-SIC-4GSW": hpnicfevtModuleRt_SIC_4GSW,
       "hpnicfevtModuleRt-SIC-4GSWP": hpnicfevtModuleRt_SIC_4GSWP,
       "hpnicfevtModuleRt-SIC-1GEC-V2": hpnicfevtModuleRt_SIC_1GEC_V2,
       "hpnicfevtModuleRt-4G-LTE-ATT": hpnicfevtModuleRt_4G_LTE_ATT,
       "hpnicfevtModuleRt-4G-TD-LTE": hpnicfevtModuleRt_4G_TD_LTE,
       "hpnicfevtModuleRt-FIP-240": hpnicfevtModuleRt_FIP_240,
       "hpnicfevtModuleRt-8GBP-V2": hpnicfevtModuleRt_8GBP_V2,
       "hpnicfevtModuleRt-HMIM-CNDE": hpnicfevtModuleRt_HMIM_CNDE,
       "hpnicfevtModuleRt-4G-LTE-Mobile": hpnicfevtModuleRt_4G_LTE_Mobile,
       "hpnicfevtModuleRt-SIC-4G-LTE-M": hpnicfevtModuleRt_SIC_4G_LTE_M,
       "hpnicfevtModuleRt-CRSE-X3": hpnicfevtModuleRt_CRSE_X3,
       "hpnicfevtModuleRt-CFIP-300": hpnicfevtModuleRt_CFIP_300,
       "hpnicfevtModuleRt-CFIP-310": hpnicfevtModuleRt_CFIP_310,
       "hpnicfevtModuleRt-CSAP-4EXP": hpnicfevtModuleRt_CSAP_4EXP,
       "hpnicfevtModuleRt-RSU": hpnicfevtModuleRt_RSU,
       "hpnicfevtModuleRt-CFIP-610": hpnicfevtModuleRt_CFIP_610,
       "hpnicfevtModuleRt-2EXP": hpnicfevtModuleRt_2EXP,
       "hpnicfevtModuleRt-16GBP": hpnicfevtModuleRt_16GBP,
       "hpnicfevtModuleRt-CFIP-240": hpnicfevtModuleRt_CFIP_240,
       "hpnicfevtModuleRt-RSE-X3": hpnicfevtModuleRt_RSE_X3,
       "hpnicfevtModuleRt-SAP-8EXP": hpnicfevtModuleRt_SAP_8EXP,
       "hpnicfevtModuleRt-SAP-16EXP": hpnicfevtModuleRt_SAP_16EXP,
       "hpnicfevtModuleRt-PU1P": hpnicfevtModuleRt_PU1P,
       "hpnicfevtModuleRt-RSU100": hpnicfevtModuleRt_RSU100,
       "hpnicfevtModuleRt-SAP-2QGP": hpnicfevtModuleRt_SAP_2QGP,
       "hpnicfevtModuleRt-CSFE-X1": hpnicfevtModuleRt_CSFE_X1,
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
       "hpnicfevtModuleSwitchType": hpnicfevtModuleSwitchType,
       "hpnicfevtModuleSw-10OR100M": hpnicfevtModuleSw_10OR100M,
       "hpnicfevtModuleSw-1000BASE-LX-SM": hpnicfevtModuleSw_1000BASE_LX_SM,
       "hpnicfevtModuleSw-1000BASE-SX-MM": hpnicfevtModuleSw_1000BASE_SX_MM,
       "hpnicfevtModuleSw-1000BASE-TX": hpnicfevtModuleSw_1000BASE_TX,
       "hpnicfevtModuleSw-100M-SINGLEMODE-FX": hpnicfevtModuleSw_100M_SINGLEMODE_FX,
       "hpnicfevtModuleSw-100M-MULTIMODE-FX": hpnicfevtModuleSw_100M_MULTIMODE_FX,
       "hpnicfevtModuleSw-100M-100BASE-TX": hpnicfevtModuleSw_100M_100BASE_TX,
       "hpnicfevtModuleSw-100M-HUB": hpnicfevtModuleSw_100M_HUB,
       "hpnicfevtModuleSw-VDSL": hpnicfevtModuleSw_VDSL,
       "hpnicfevtModuleSw-STACK": hpnicfevtModuleSw_STACK,
       "hpnicfevtModuleSw-1000BASE-ZENITH-FX": hpnicfevtModuleSw_1000BASE_ZENITH_FX,
       "hpnicfevtModuleSw-1000BASE-LONG-FX": hpnicfevtModuleSw_1000BASE_LONG_FX,
       "hpnicfevtModuleSw-ADSL": hpnicfevtModuleSw_ADSL,
       "hpnicfevtModuleSw-4T10OR100-4FX100SM": hpnicfevtModuleSw_4T10OR100_4FX100SM,
       "hpnicfevtModuleSw-4T10OR100-4FX100MM": hpnicfevtModuleSw_4T10OR100_4FX100MM,
       "hpnicfevtModuleSw-VSPL": hpnicfevtModuleSw_VSPL,
       "hpnicfevtModuleSw-ASPL": hpnicfevtModuleSw_ASPL,
       "hpnicfevtModuleSw-1000M-SFP": hpnicfevtModuleSw_1000M_SFP,
       "hpnicfevtModuleSw-LS82O2CM": hpnicfevtModuleSw_LS82O2CM,
       "hpnicfevtModuleSw-LS82P2CM": hpnicfevtModuleSw_LS82P2CM,
       "hpnicfevtModuleSw-LS82O4GM": hpnicfevtModuleSw_LS82O4GM,
       "hpnicfevtModuleSw-LS82GB4C": hpnicfevtModuleSw_LS82GB4C,
       "hpnicfevtModuleSw-LS82GT4C": hpnicfevtModuleSw_LS82GT4C,
       "hpnicfevtModuleSw-LS82ST4C": hpnicfevtModuleSw_LS82ST4C,
       "hpnicfevtModuleSw-BOARD-LS82DSPU": hpnicfevtModuleSw_BOARD_LS82DSPU,
       "hpnicfevtModuleSw-BOARD-LS81GP8U": hpnicfevtModuleSw_BOARD_LS81GP8U,
       "hpnicfevtModuleSw-BOARD-LS82GT20": hpnicfevtModuleSw_BOARD_LS82GT20,
       "hpnicfevtModuleSw-BOARD-LS82FE48": hpnicfevtModuleSw_BOARD_LS82FE48,
       "hpnicfevtModuleSw-LS82T24B": hpnicfevtModuleSw_LS82T24B,
       "hpnicfevtModuleSw-LSB1SRPA": hpnicfevtModuleSw_LSB1SRPA,
       "hpnicfevtModuleSw-LSB1FT48A": hpnicfevtModuleSw_LSB1FT48A,
       "hpnicfevtModuleSw-LSB1FT48B": hpnicfevtModuleSw_LSB1FT48B,
       "hpnicfevtModuleSw-LSB1F48GA": hpnicfevtModuleSw_LSB1F48GA,
       "hpnicfevtModuleSw-LSB1F48GB": hpnicfevtModuleSw_LSB1F48GB,
       "hpnicfevtModuleSw-LSB1FP20A": hpnicfevtModuleSw_LSB1FP20A,
       "hpnicfevtModuleSw-LSB1FP20B": hpnicfevtModuleSw_LSB1FP20B,
       "hpnicfevtModuleSw-FT48A": hpnicfevtModuleSw_FT48A,
       "hpnicfevtModuleSw-GP4U": hpnicfevtModuleSw_GP4U,
       "hpnicfevtModuleSw-GP2U": hpnicfevtModuleSw_GP2U,
       "hpnicfevtModuleSw-TGX1A": hpnicfevtModuleSw_TGX1A,
       "hpnicfevtModuleSw-1000BASE-LX-SM-IR-SC": hpnicfevtModuleSw_1000BASE_LX_SM_IR_SC,
       "hpnicfevtModuleSw-1000BASE-SX-MM-SR-SC": hpnicfevtModuleSw_1000BASE_SX_MM_SR_SC,
       "hpnicfevtModuleSw-1000BASE-T-RJ45": hpnicfevtModuleSw_1000BASE_T_RJ45,
       "hpnicfevtModuleSw-100BASE-FX-SM-IR-SC": hpnicfevtModuleSw_100BASE_FX_SM_IR_SC,
       "hpnicfevtModuleSw-100BASE-FX-MM-SR-SC": hpnicfevtModuleSw_100BASE_FX_MM_SR_SC,
       "hpnicfevtModuleSw-GIGA-STACK-1M-PC": hpnicfevtModuleSw_GIGA_STACK_1M_PC,
       "hpnicfevtModuleSw-1000BASE-LX-SM-VLR-LC": hpnicfevtModuleSw_1000BASE_LX_SM_VLR_LC,
       "hpnicfevtModuleSw-1000BASE-LX-SM-LR-LC": hpnicfevtModuleSw_1000BASE_LX_SM_LR_LC,
       "hpnicfevtModuleSw-100BASE-FX-SM-LR-SC": hpnicfevtModuleSw_100BASE_FX_SM_LR_SC,
       "hpnicfevtModuleSw-1000BASE-X-GBIC": hpnicfevtModuleSw_1000BASE_X_GBIC,
       "hpnicfevtModuleSw-100M-SINGLEMODE-FX-LC": hpnicfevtModuleSw_100M_SINGLEMODE_FX_LC,
       "hpnicfevtModuleSw-100M-MULTIMODE-FX-LC": hpnicfevtModuleSw_100M_MULTIMODE_FX_LC,
       "hpnicfevtModuleSw-1000BASE-4SFP": hpnicfevtModuleSw_1000BASE_4SFP,
       "hpnicfevtModuleSw-1000BASE-4GBIC": hpnicfevtModuleSw_1000BASE_4GBIC,
       "hpnicfevtModuleSw-1000BASE-FIXED-4SFP": hpnicfevtModuleSw_1000BASE_FIXED_4SFP,
       "hpnicfevtModuleSw-1000BASE-FIXED-4GBIC": hpnicfevtModuleSw_1000BASE_FIXED_4GBIC,
       "hpnicfevtModuleSw-LSB1GP12A": hpnicfevtModuleSw_LSB1GP12A,
       "hpnicfevtModuleSw-LSB1GP12B": hpnicfevtModuleSw_LSB1GP12B,
       "hpnicfevtModuleSw-LSB1TGX1A": hpnicfevtModuleSw_LSB1TGX1A,
       "hpnicfevtModuleSw-LSB1TGX1B": hpnicfevtModuleSw_LSB1TGX1B,
       "hpnicfevtModuleSw-LSB1P4G8A": hpnicfevtModuleSw_LSB1P4G8A,
       "hpnicfevtModuleSw-LSB1P4G8B": hpnicfevtModuleSw_LSB1P4G8B,
       "hpnicfevtModuleSw-LSB1A4G8A": hpnicfevtModuleSw_LSB1A4G8A,
       "hpnicfevtModuleSw-LSB1A4G8B": hpnicfevtModuleSw_LSB1A4G8B,
       "hpnicfevtModuleSw-FT48C": hpnicfevtModuleSw_FT48C,
       "hpnicfevtModuleSw-FP20": hpnicfevtModuleSw_FP20,
       "hpnicfevtModuleSw-BOARD-LS81FT48": hpnicfevtModuleSw_BOARD_LS81FT48,
       "hpnicfevtModuleSw-BOARD-LS81GB8U": hpnicfevtModuleSw_BOARD_LS81GB8U,
       "hpnicfevtModuleSw-BOARD-LS81GT8U": hpnicfevtModuleSw_BOARD_LS81GT8U,
       "hpnicfevtModuleSw-BOARD-LS81FS24": hpnicfevtModuleSw_BOARD_LS81FS24,
       "hpnicfevtModuleSw-BOARD-LS81FM24": hpnicfevtModuleSw_BOARD_LS81FM24,
       "hpnicfevtModuleSw-BOARD-LS82GP20": hpnicfevtModuleSw_BOARD_LS82GP20,
       "hpnicfevtModuleSw-LSB1SRPB": hpnicfevtModuleSw_LSB1SRPB,
       "hpnicfevtModuleSw-LSB1F32GA": hpnicfevtModuleSw_LSB1F32GA,
       "hpnicfevtModuleSw-LSB1F32GB": hpnicfevtModuleSw_LSB1F32GB,
       "hpnicfevtModuleSw-LSB2FT48A": hpnicfevtModuleSw_LSB2FT48A,
       "hpnicfevtModuleSw-LSB2FT48B": hpnicfevtModuleSw_LSB2FT48B,
       "hpnicfevtModuleSw-LSB1GT12A": hpnicfevtModuleSw_LSB1GT12A,
       "hpnicfevtModuleSw-LSB1GT12B": hpnicfevtModuleSw_LSB1GT12B,
       "hpnicfevtModuleSw-PC4U": hpnicfevtModuleSw_PC4U,
       "hpnicfevtModuleSw-FT32A": hpnicfevtModuleSw_FT32A,
       "hpnicfevtModuleSw-GT4U": hpnicfevtModuleSw_GT4U,
       "hpnicfevtModuleSw-BOARD-LS83FP20A": hpnicfevtModuleSw_BOARD_LS83FP20A,
       "hpnicfevtModuleSw-BOARD-LS82HGMU": hpnicfevtModuleSw_BOARD_LS82HGMU,
       "hpnicfevtModuleSw-LSB1GP8TB": hpnicfevtModuleSw_LSB1GP8TB,
       "hpnicfevtModuleSw-LSB1GP8TC": hpnicfevtModuleSw_LSB1GP8TC,
       "hpnicfevtModuleSw-LSB1GT8PB": hpnicfevtModuleSw_LSB1GT8PB,
       "hpnicfevtModuleSw-LSB1GT8PC": hpnicfevtModuleSw_LSB1GT8PC,
       "hpnicfevtModuleSw-LSB1FT48C": hpnicfevtModuleSw_LSB1FT48C,
       "hpnicfevtModuleSw-LSB1FP20C": hpnicfevtModuleSw_LSB1FP20C,
       "hpnicfevtModuleSw-LSB1F32GC": hpnicfevtModuleSw_LSB1F32GC,
       "hpnicfevtModuleSw-LSB1GT12C": hpnicfevtModuleSw_LSB1GT12C,
       "hpnicfevtModuleSw-LSB1GP12C": hpnicfevtModuleSw_LSB1GP12C,
       "hpnicfevtModuleSw-LSB1P4G8C": hpnicfevtModuleSw_LSB1P4G8C,
       "hpnicfevtModuleSw-LSB1TGX1C": hpnicfevtModuleSw_LSB1TGX1C,
       "hpnicfevtModuleSw-LSB1GT24B": hpnicfevtModuleSw_LSB1GT24B,
       "hpnicfevtModuleSw-LSB1GT24C": hpnicfevtModuleSw_LSB1GT24C,
       "hpnicfevtModuleSw-LSB1GP24B": hpnicfevtModuleSw_LSB1GP24B,
       "hpnicfevtModuleSw-LSB1GP24C": hpnicfevtModuleSw_LSB1GP24C,
       "hpnicfevtModuleSw-LSB1XP2B": hpnicfevtModuleSw_LSB1XP2B,
       "hpnicfevtModuleSw-LSB1XP2C": hpnicfevtModuleSw_LSB1XP2C,
       "hpnicfevtModuleSw-LSB1GV48B": hpnicfevtModuleSw_LSB1GV48B,
       "hpnicfevtModuleSw-LSB1GV48C": hpnicfevtModuleSw_LSB1GV48C,
       "hpnicfevtModuleSw-LSB1SRPC": hpnicfevtModuleSw_LSB1SRPC,
       "hpnicfevtModuleSw-LSB1SRP1N0": hpnicfevtModuleSw_LSB1SRP1N0,
       "hpnicfevtModuleSw-LSB1SRP1N1": hpnicfevtModuleSw_LSB1SRP1N1,
       "hpnicfevtModuleSw-LSB1SRP1N2": hpnicfevtModuleSw_LSB1SRP1N2,
       "hpnicfevtModuleSw-GT24": hpnicfevtModuleSw_GT24,
       "hpnicfevtModuleSw-GP24": hpnicfevtModuleSw_GP24,
       "hpnicfevtModuleSw-XP2": hpnicfevtModuleSw_XP2,
       "hpnicfevtModuleSw-GV48": hpnicfevtModuleSw_GV48,
       "hpnicfevtModuleSw-LSG1GP8U": hpnicfevtModuleSw_LSG1GP8U,
       "hpnicfevtModuleSw-LSG1GT8U": hpnicfevtModuleSw_LSG1GT8U,
       "hpnicfevtModuleSw-LSG1TG1U": hpnicfevtModuleSw_LSG1TG1U,
       "hpnicfevtModuleSw-LSG1TD1U": hpnicfevtModuleSw_LSG1TD1U,
       "hpnicfevtModuleSw-LSB2FT48C": hpnicfevtModuleSw_LSB2FT48C,
       "hpnicfevtModuleSw-LSB1GT48B": hpnicfevtModuleSw_LSB1GT48B,
       "hpnicfevtModuleSw-LSB1GT48C": hpnicfevtModuleSw_LSB1GT48C,
       "hpnicfevtModuleSw-LS81GT48": hpnicfevtModuleSw_LS81GT48,
       "hpnicfevtModuleSw-LS81SRPG0": hpnicfevtModuleSw_LS81SRPG0,
       "hpnicfevtModuleSw-LS81SRPG1": hpnicfevtModuleSw_LS81SRPG1,
       "hpnicfevtModuleSw-LS81SRPG2": hpnicfevtModuleSw_LS81SRPG2,
       "hpnicfevtModuleSw-LS81SRPG3": hpnicfevtModuleSw_LS81SRPG3,
       "hpnicfevtModuleSw-SR01SRPUB": hpnicfevtModuleSw_SR01SRPUB,
       "hpnicfevtModuleSw-SR01SRPUA": hpnicfevtModuleSw_SR01SRPUA,
       "hpnicfevtModuleSw-SR01GP12L": hpnicfevtModuleSw_SR01GP12L,
       "hpnicfevtModuleSw-SR01GP12W": hpnicfevtModuleSw_SR01GP12W,
       "hpnicfevtModuleSw-SR01FT48L": hpnicfevtModuleSw_SR01FT48L,
       "hpnicfevtModuleSw-SR01FT48W": hpnicfevtModuleSw_SR01FT48W,
       "hpnicfevtModuleSw-SR01XK1W": hpnicfevtModuleSw_SR01XK1W,
       "hpnicfevtModuleSw-SR01FP20W": hpnicfevtModuleSw_SR01FP20W,
       "hpnicfevtModuleSw-SR01GT12W": hpnicfevtModuleSw_SR01GT12W,
       "hpnicfevtModuleSw-SR01F32GL": hpnicfevtModuleSw_SR01F32GL,
       "hpnicfevtModuleSw-SR01F32GW": hpnicfevtModuleSw_SR01F32GW,
       "hpnicfevtModuleSw-SR01GT8PL": hpnicfevtModuleSw_SR01GT8PL,
       "hpnicfevtModuleSw-SR01GT8PW": hpnicfevtModuleSw_SR01GT8PW,
       "hpnicfevtModuleSw-SR01P4G8W": hpnicfevtModuleSw_SR01P4G8W,
       "hpnicfevtModuleSw-LSA1FP8U": hpnicfevtModuleSw_LSA1FP8U,
       "hpnicfevtModuleSw-LSB1SP4B": hpnicfevtModuleSw_LSB1SP4B,
       "hpnicfevtModuleSw-LSB1SP4C": hpnicfevtModuleSw_LSB1SP4C,
       "hpnicfevtModuleSw-LSB1UP1B": hpnicfevtModuleSw_LSB1UP1B,
       "hpnicfevtModuleSw-LSB1UP1C": hpnicfevtModuleSw_LSB1UP1C,
       "hpnicfevtModuleSw-LSB1XP4B": hpnicfevtModuleSw_LSB1XP4B,
       "hpnicfevtModuleSw-LSB1XP4C": hpnicfevtModuleSw_LSB1XP4C,
       "hpnicfevtModuleSw-SP4": hpnicfevtModuleSw_SP4,
       "hpnicfevtModuleSw-UP1": hpnicfevtModuleSw_UP1,
       "hpnicfevtModuleSw-XP4": hpnicfevtModuleSw_XP4,
       "hpnicfevtModuleSw-LS81VSNP": hpnicfevtModuleSw_LS81VSNP,
       "hpnicfevtModuleSw-LS81T12P": hpnicfevtModuleSw_LS81T12P,
       "hpnicfevtModuleSw-LS81P12T": hpnicfevtModuleSw_LS81P12T,
       "hpnicfevtModuleSw-LS81GP8UB": hpnicfevtModuleSw_LS81GP8UB,
       "hpnicfevtModuleSw-LS81FT48E": hpnicfevtModuleSw_LS81FT48E,
       "hpnicfevtModuleSw-LS81GP4UB": hpnicfevtModuleSw_LS81GP4UB,
       "hpnicfevtModuleSw-LS81GT8UE": hpnicfevtModuleSw_LS81GT8UE,
       "hpnicfevtModuleSw-LS81GT48A": hpnicfevtModuleSw_LS81GT48A,
       "hpnicfevtModuleSw-LS81FP48": hpnicfevtModuleSw_LS81FP48,
       "hpnicfevtModuleSw-LSB1XK1B": hpnicfevtModuleSw_LSB1XK1B,
       "hpnicfevtModuleSw-LSB1XK1C": hpnicfevtModuleSw_LSB1XK1C,
       "hpnicfevtModuleSw-SR01SRPUC": hpnicfevtModuleSw_SR01SRPUC,
       "hpnicfevtModuleSw-SR01SRPUD": hpnicfevtModuleSw_SR01SRPUD,
       "hpnicfevtModuleSw-SR01SRPUE": hpnicfevtModuleSw_SR01SRPUE,
       "hpnicfevtModuleSw-LSB1SRP1N3": hpnicfevtModuleSw_LSB1SRP1N3,
       "hpnicfevtModuleSw-LSB1VP2B": hpnicfevtModuleSw_LSB1VP2B,
       "hpnicfevtModuleSw-LSB1NATB": hpnicfevtModuleSw_LSB1NATB,
       "hpnicfevtModuleSw-LSB1VPNB": hpnicfevtModuleSw_LSB1VPNB,
       "hpnicfevtModuleSw-LSGP8P": hpnicfevtModuleSw_LSGP8P,
       "hpnicfevtModuleSw-LSXK1P": hpnicfevtModuleSw_LSXK1P,
       "hpnicfevtModuleSw-LSXP2P": hpnicfevtModuleSw_LSXP2P,
       "hpnicfevtModuleSw-LS81FT48F": hpnicfevtModuleSw_LS81FT48F,
       "hpnicfevtModuleSw-LS81PT8G": hpnicfevtModuleSw_LS81PT8G,
       "hpnicfevtModuleSw-LS81PT4G": hpnicfevtModuleSw_LS81PT4G,
       "hpnicfevtModuleSw-LSSTK24G": hpnicfevtModuleSw_LSSTK24G,
       "hpnicfevtModuleSw-LS82GT20A": hpnicfevtModuleSw_LS82GT20A,
       "hpnicfevtModuleSw-LS82GP20A": hpnicfevtModuleSw_LS82GP20A,
       "hpnicfevtModuleSw-LS81TGX1C": hpnicfevtModuleSw_LS81TGX1C,
       "hpnicfevtModuleSw-VP2": hpnicfevtModuleSw_VP2,
       "hpnicfevtModuleSw-LSA1FB8U": hpnicfevtModuleSw_LSA1FB8U,
       "hpnicfevtModuleSw-LS81T12PE": hpnicfevtModuleSw_LS81T12PE,
       "hpnicfevtModuleSw-LS81P12TE": hpnicfevtModuleSw_LS81P12TE,
       "hpnicfevtModuleSw-LSB1SRP2N0": hpnicfevtModuleSw_LSB1SRP2N0,
       "hpnicfevtModuleSw-LSB1SRP2N3": hpnicfevtModuleSw_LSB1SRP2N3,
       "hpnicfevtModuleSw-LSB1GV48DB": hpnicfevtModuleSw_LSB1GV48DB,
       "hpnicfevtModuleSw-LSB1FW8B": hpnicfevtModuleSw_LSB1FW8B,
       "hpnicfevtModuleSw-LSB1IPSEC8B": hpnicfevtModuleSw_LSB1IPSEC8B,
       "hpnicfevtModuleSw-LSB1IDSB": hpnicfevtModuleSw_LSB1IDSB,
       "hpnicfevtModuleSw-LSB1IPSB": hpnicfevtModuleSw_LSB1IPSB,
       "hpnicfevtModuleSw-LSB2FT48CA": hpnicfevtModuleSw_LSB2FT48CA,
       "hpnicfevtModuleSw-LSB1FP20CA": hpnicfevtModuleSw_LSB1FP20CA,
       "hpnicfevtModuleSw-LSB1F32GCA": hpnicfevtModuleSw_LSB1F32GCA,
       "hpnicfevtModuleSw-LSB1P4G8CA": hpnicfevtModuleSw_LSB1P4G8CA,
       "hpnicfevtModuleSw-LSB1GT12CA": hpnicfevtModuleSw_LSB1GT12CA,
       "hpnicfevtModuleSw-LSB1GT24CA": hpnicfevtModuleSw_LSB1GT24CA,
       "hpnicfevtModuleSw-LSB1GP12CA": hpnicfevtModuleSw_LSB1GP12CA,
       "hpnicfevtModuleSw-LSB1GP24CA": hpnicfevtModuleSw_LSB1GP24CA,
       "hpnicfevtModuleSw-LSB1GT8PCA": hpnicfevtModuleSw_LSB1GT8PCA,
       "hpnicfevtModuleSw-LSB1XP2CA": hpnicfevtModuleSw_LSB1XP2CA,
       "hpnicfevtModuleSw-LSB1XK1CA": hpnicfevtModuleSw_LSB1XK1CA,
       "hpnicfevtModuleSw-LSB1XP4CA": hpnicfevtModuleSw_LSB1XP4CA,
       "hpnicfevtModuleSw-LSB1UP1CA": hpnicfevtModuleSw_LSB1UP1CA,
       "hpnicfevtModuleSw-LSB1SP4CA": hpnicfevtModuleSw_LSB1SP4CA,
       "hpnicfevtModuleSw-LSB1VP2CA": hpnicfevtModuleSw_LSB1VP2CA,
       "hpnicfevtModuleSw-SR01FT48WA": hpnicfevtModuleSw_SR01FT48WA,
       "hpnicfevtModuleSw-SR01FP20WA": hpnicfevtModuleSw_SR01FP20WA,
       "hpnicfevtModuleSw-SR01F32GWA": hpnicfevtModuleSw_SR01F32GWA,
       "hpnicfevtModuleSw-SR01P4G8WA": hpnicfevtModuleSw_SR01P4G8WA,
       "hpnicfevtModuleSw-SR01GT12WA": hpnicfevtModuleSw_SR01GT12WA,
       "hpnicfevtModuleSw-SR01GT24WA": hpnicfevtModuleSw_SR01GT24WA,
       "hpnicfevtModuleSw-SR01GP12WA": hpnicfevtModuleSw_SR01GP12WA,
       "hpnicfevtModuleSw-SR01GP24WA": hpnicfevtModuleSw_SR01GP24WA,
       "hpnicfevtModuleSw-SR01GT8PWA": hpnicfevtModuleSw_SR01GT8PWA,
       "hpnicfevtModuleSw-SR01XP2WA": hpnicfevtModuleSw_SR01XP2WA,
       "hpnicfevtModuleSw-SR01XK1WA": hpnicfevtModuleSw_SR01XK1WA,
       "hpnicfevtModuleSw-SR01UP1WA": hpnicfevtModuleSw_SR01UP1WA,
       "hpnicfevtModuleSw-SR01SP4WA": hpnicfevtModuleSw_SR01SP4WA,
       "hpnicfevtModuleSw-GP8U": hpnicfevtModuleSw_GP8U,
       "hpnicfevtModuleSw-LSEXP1P": hpnicfevtModuleSw_LSEXP1P,
       "hpnicfevtModuleSw-LSEXK1P": hpnicfevtModuleSw_LSEXK1P,
       "hpnicfevtModuleSw-LSEXS1P": hpnicfevtModuleSw_LSEXS1P,
       "hpnicfevtModuleSw-LS81GP48": hpnicfevtModuleSw_LS81GP48,
       "hpnicfevtModuleSw-LS81GT48B": hpnicfevtModuleSw_LS81GT48B,
       "hpnicfevtModuleSw-LS81T16P": hpnicfevtModuleSw_LS81T16P,
       "hpnicfevtModuleSw-LS81T32P": hpnicfevtModuleSw_LS81T32P,
       "hpnicfevtModuleSw-LS81TGX2": hpnicfevtModuleSw_LS81TGX2,
       "hpnicfevtModuleSw-LS81TGX4": hpnicfevtModuleSw_LS81TGX4,
       "hpnicfevtModuleSw-LSB1GV48DA": hpnicfevtModuleSw_LSB1GV48DA,
       "hpnicfevtModuleSw-SR01GV48VB": hpnicfevtModuleSw_SR01GV48VB,
       "hpnicfevtModuleSw-LSB1GT24DB": hpnicfevtModuleSw_LSB1GT24DB,
       "hpnicfevtModuleSw-LSB1GP24DB": hpnicfevtModuleSw_LSB1GP24DB,
       "hpnicfevtModuleSw-LSB1GP24DC": hpnicfevtModuleSw_LSB1GP24DC,
       "hpnicfevtModuleSw-LSB1FW8DB": hpnicfevtModuleSw_LSB1FW8DB,
       "hpnicfevtModuleSw-LSB1IPSEC8DB": hpnicfevtModuleSw_LSB1IPSEC8DB,
       "hpnicfevtModuleSw-SR01GT24VB": hpnicfevtModuleSw_SR01GT24VB,
       "hpnicfevtModuleSw-SR01GP24VC": hpnicfevtModuleSw_SR01GP24VC,
       "hpnicfevtModuleSw-SR01VP2WA": hpnicfevtModuleSw_SR01VP2WA,
       "hpnicfevtModuleSw-SR01FW8VB": hpnicfevtModuleSw_SR01FW8VB,
       "hpnicfevtModuleSw-SR01IPSEC8VB": hpnicfevtModuleSw_SR01IPSEC8VB,
       "hpnicfevtModuleSw-SR01NATL": hpnicfevtModuleSw_SR01NATL,
       "hpnicfevtModuleSw-SR01VPNL": hpnicfevtModuleSw_SR01VPNL,
       "hpnicfevtModuleSw-LSB1GP24CB": hpnicfevtModuleSw_LSB1GP24CB,
       "hpnicfevtModuleSw-LSB1GP48DB": hpnicfevtModuleSw_LSB1GP48DB,
       "hpnicfevtModuleSw-LSB1XP2CB": hpnicfevtModuleSw_LSB1XP2CB,
       "hpnicfevtModuleSw-XP4L": hpnicfevtModuleSw_XP4L,
       "hpnicfevtModuleSw-LSB1XP4LDB": hpnicfevtModuleSw_LSB1XP4LDB,
       "hpnicfevtModuleSw-LSB1XP4LDC": hpnicfevtModuleSw_LSB1XP4LDC,
       "hpnicfevtModuleSw-AHP4": hpnicfevtModuleSw_AHP4,
       "hpnicfevtModuleSw-LSB1AHP4GCA": hpnicfevtModuleSw_LSB1AHP4GCA,
       "hpnicfevtModuleSw-CLP4": hpnicfevtModuleSw_CLP4,
       "hpnicfevtModuleSw-LSB1CLP4GCA": hpnicfevtModuleSw_LSB1CLP4GCA,
       "hpnicfevtModuleSw-ET32": hpnicfevtModuleSw_ET32,
       "hpnicfevtModuleSw-LSB1ET32GCA": hpnicfevtModuleSw_LSB1ET32GCA,
       "hpnicfevtModuleSw-LSB1IDSDB": hpnicfevtModuleSw_LSB1IDSDB,
       "hpnicfevtModuleSw-LSB1SRP2N1": hpnicfevtModuleSw_LSB1SRP2N1,
       "hpnicfevtModuleSw-BOARD-LS82SRPB": hpnicfevtModuleSw_BOARD_LS82SRPB,
       "hpnicfevtModuleSw-BORAD-LS83SRPC": hpnicfevtModuleSw_BORAD_LS83SRPC,
       "hpnicfevtModuleSw-Main": hpnicfevtModuleSw_Main,
       "hpnicfevtModuleSw-LSB1SRP2N2": hpnicfevtModuleSw_LSB1SRP2N2,
       "hpnicfevtModuleSw-LSB1NAMB": hpnicfevtModuleSw_LSB1NAMB,
       "hpnicfevtModuleSw-RSP2": hpnicfevtModuleSw_RSP2,
       "hpnicfevtModuleSw-LSB1RSP2CA": hpnicfevtModuleSw_LSB1RSP2CA,
       "hpnicfevtModuleSw-SR01XP4LVC": hpnicfevtModuleSw_SR01XP4LVC,
       "hpnicfevtModuleSw-SR01AHP4GWA": hpnicfevtModuleSw_SR01AHP4GWA,
       "hpnicfevtModuleSw-SR01CLP4GWA": hpnicfevtModuleSw_SR01CLP4GWA,
       "hpnicfevtModuleSw-SR01ET32GWA": hpnicfevtModuleSw_SR01ET32GWA,
       "hpnicfevtModuleSw-SR01IDSVB": hpnicfevtModuleSw_SR01IDSVB,
       "hpnicfevtModuleSw-SR01SRPUF": hpnicfevtModuleSw_SR01SRPUF,
       "hpnicfevtModuleSw-SR01NAML": hpnicfevtModuleSw_SR01NAML,
       "hpnicfevtModuleSw-SR01RSP2WA": hpnicfevtModuleSw_SR01RSP2WA,
       "hpnicfevtModuleSw-LSPM1XP1P": hpnicfevtModuleSw_LSPM1XP1P,
       "hpnicfevtModuleSw-LSPM1XP2P": hpnicfevtModuleSw_LSPM1XP2P,
       "hpnicfevtModuleSw-LSPM1CX2P": hpnicfevtModuleSw_LSPM1CX2P,
       "hpnicfevtModuleSw-STK-1000BASE-T": hpnicfevtModuleSw_STK_1000BASE_T,
       "hpnicfevtModuleSw-LSB1SRP1M0": hpnicfevtModuleSw_LSB1SRP1M0,
       "hpnicfevtModuleSw-LSB1SRP1M1": hpnicfevtModuleSw_LSB1SRP1M1,
       "hpnicfevtModuleSw-LSB1GP12DB": hpnicfevtModuleSw_LSB1GP12DB,
       "hpnicfevtModuleSw-LSB1GT12DB": hpnicfevtModuleSw_LSB1GT12DB,
       "hpnicfevtModuleSw-LSB1XK1DB": hpnicfevtModuleSw_LSB1XK1DB,
       "hpnicfevtModuleSw-LSB1XP2DB": hpnicfevtModuleSw_LSB1XP2DB,
       "hpnicfevtModuleSw-LSB1XP2DC": hpnicfevtModuleSw_LSB1XP2DC,
       "hpnicfevtModuleSw-LSB1GT48LDB": hpnicfevtModuleSw_LSB1GT48LDB,
       "hpnicfevtModuleSw-LSB1XP4TDB": hpnicfevtModuleSw_LSB1XP4TDB,
       "hpnicfevtModuleSw-LSB1XP4TDC": hpnicfevtModuleSw_LSB1XP4TDC,
       "hpnicfevtModuleSw-LSB1RSP2DC": hpnicfevtModuleSw_LSB1RSP2DC,
       "hpnicfevtModuleSw-LSB1VP2DC": hpnicfevtModuleSw_LSB1VP2DC,
       "hpnicfevtModuleSw-LSB1XP4DB": hpnicfevtModuleSw_LSB1XP4DB,
       "hpnicfevtModuleSw-LSB1SRP2E0": hpnicfevtModuleSw_LSB1SRP2E0,
       "hpnicfevtModuleSw-LSB1SRP2E1": hpnicfevtModuleSw_LSB1SRP2E1,
       "hpnicfevtModuleSw-LSB1SRP2E2": hpnicfevtModuleSw_LSB1SRP2E2,
       "hpnicfevtModuleSw-LSB1SRP2E3": hpnicfevtModuleSw_LSB1SRP2E3,
       "hpnicfevtModuleSw-SR01SRPUQ": hpnicfevtModuleSw_SR01SRPUQ,
       "hpnicfevtModuleSw-AHP1": hpnicfevtModuleSw_AHP1,
       "hpnicfevtModuleSw-AHP2": hpnicfevtModuleSw_AHP2,
       "hpnicfevtModuleSw-CLP1": hpnicfevtModuleSw_CLP1,
       "hpnicfevtModuleSw-CLP2": hpnicfevtModuleSw_CLP2,
       "hpnicfevtModuleSw-ET16": hpnicfevtModuleSw_ET16,
       "hpnicfevtModuleSw-LSB1SRP1NA0": hpnicfevtModuleSw_LSB1SRP1NA0,
       "hpnicfevtModuleSw-LSB1SRP1NA1": hpnicfevtModuleSw_LSB1SRP1NA1,
       "hpnicfevtModuleSw-LSB1SRP1NA2": hpnicfevtModuleSw_LSB1SRP1NA2,
       "hpnicfevtModuleSw-LSB1SRP1NA3": hpnicfevtModuleSw_LSB1SRP1NA3,
       "hpnicfevtModuleSw-SR01AHP1GWA": hpnicfevtModuleSw_SR01AHP1GWA,
       "hpnicfevtModuleSw-SR01AHP2GWA": hpnicfevtModuleSw_SR01AHP2GWA,
       "hpnicfevtModuleSw-SR01CLP1GWA": hpnicfevtModuleSw_SR01CLP1GWA,
       "hpnicfevtModuleSw-SR01CLP2GWA": hpnicfevtModuleSw_SR01CLP2GWA,
       "hpnicfevtModuleSw-SR01ET16GWA": hpnicfevtModuleSw_SR01ET16GWA,
       "hpnicfevtModuleSw-SR01GP12VB": hpnicfevtModuleSw_SR01GP12VB,
       "hpnicfevtModuleSw-SR01XK1VB": hpnicfevtModuleSw_SR01XK1VB,
       "hpnicfevtModuleSw-SR01XP2VC": hpnicfevtModuleSw_SR01XP2VC,
       "hpnicfevtModuleSw-SR01XP4LVB": hpnicfevtModuleSw_SR01XP4LVB,
       "hpnicfevtModuleSw-SR01SRPUEA": hpnicfevtModuleSw_SR01SRPUEA,
       "hpnicfevtModuleSw-LSB1SRP1N4": hpnicfevtModuleSw_LSB1SRP1N4,
       "hpnicfevtModuleSw-LSB1SRP1N5": hpnicfevtModuleSw_LSB1SRP1N5,
       "hpnicfevtModuleSw-LSB1SRP1N6": hpnicfevtModuleSw_LSB1SRP1N6,
       "hpnicfevtModuleSw-LSB1SRP1N7": hpnicfevtModuleSw_LSB1SRP1N7,
       "hpnicfevtModuleSw-LSB1SRP2N4": hpnicfevtModuleSw_LSB1SRP2N4,
       "hpnicfevtModuleSw-LSB1SRP2N5": hpnicfevtModuleSw_LSB1SRP2N5,
       "hpnicfevtModuleSw-LSB1SRP2N6": hpnicfevtModuleSw_LSB1SRP2N6,
       "hpnicfevtModuleSw-LSB1SRP2N7": hpnicfevtModuleSw_LSB1SRP2N7,
       "hpnicfevtModuleSw-LSB1SRP1NA4": hpnicfevtModuleSw_LSB1SRP1NA4,
       "hpnicfevtModuleSw-LSB1SRP1NA5": hpnicfevtModuleSw_LSB1SRP1NA5,
       "hpnicfevtModuleSw-LSB1SRP1NA6": hpnicfevtModuleSw_LSB1SRP1NA6,
       "hpnicfevtModuleSw-LSB1SRP1NA7": hpnicfevtModuleSw_LSB1SRP1NA7,
       "hpnicfevtModuleSw-LSB2GV48DA": hpnicfevtModuleSw_LSB2GV48DA,
       "hpnicfevtModuleSw-LSB1RGP2GDB": hpnicfevtModuleSw_LSB1RGP2GDB,
       "hpnicfevtModuleSw-LSB1RGP4GDB": hpnicfevtModuleSw_LSB1RGP4GDB,
       "hpnicfevtModuleSw-LSB2GP24DB": hpnicfevtModuleSw_LSB2GP24DB,
       "hpnicfevtModuleSw-LSB2GP24DC": hpnicfevtModuleSw_LSB2GP24DC,
       "hpnicfevtModuleSw-LSB2GT24DB": hpnicfevtModuleSw_LSB2GT24DB,
       "hpnicfevtModuleSw-LSB2FW8DB": hpnicfevtModuleSw_LSB2FW8DB,
       "hpnicfevtModuleSw-LSB2IPSEC8DB": hpnicfevtModuleSw_LSB2IPSEC8DB,
       "hpnicfevtModuleSw-LSB2GV48DB": hpnicfevtModuleSw_LSB2GV48DB,
       "hpnicfevtModuleSw-RGP2": hpnicfevtModuleSw_RGP2,
       "hpnicfevtModuleSw-RGP4": hpnicfevtModuleSw_RGP4,
       "hpnicfevtModuleSw-SR02FW8VB": hpnicfevtModuleSw_SR02FW8VB,
       "hpnicfevtModuleSw-SR02IPSEC8VB": hpnicfevtModuleSw_SR02IPSEC8VB,
       "hpnicfevtModuleSw-LSB2SRP1N0": hpnicfevtModuleSw_LSB2SRP1N0,
       "hpnicfevtModuleSw-LSB2SRP1N1": hpnicfevtModuleSw_LSB2SRP1N1,
       "hpnicfevtModuleSw-LSB2SRP1N2": hpnicfevtModuleSw_LSB2SRP1N2,
       "hpnicfevtModuleSw-LSB2SRP1N3": hpnicfevtModuleSw_LSB2SRP1N3,
       "hpnicfevtModuleSw-LSB2SRP1N4": hpnicfevtModuleSw_LSB2SRP1N4,
       "hpnicfevtModuleSw-LSB2SRP1N5": hpnicfevtModuleSw_LSB2SRP1N5,
       "hpnicfevtModuleSw-LSB2SRP1N6": hpnicfevtModuleSw_LSB2SRP1N6,
       "hpnicfevtModuleSw-LSB2SRP1N7": hpnicfevtModuleSw_LSB2SRP1N7,
       "hpnicfevtModuleSw-SR02SRPUE": hpnicfevtModuleSw_SR02SRPUE,
       "hpnicfevtModuleSw-SR01LN1BQH0": hpnicfevtModuleSw_SR01LN1BQH0,
       "hpnicfevtModuleSw-SR01DXP1L": hpnicfevtModuleSw_SR01DXP1L,
       "hpnicfevtModuleSw-SR01DGP10L": hpnicfevtModuleSw_SR01DGP10L,
       "hpnicfevtModuleSw-SR01DRSP2L": hpnicfevtModuleSw_SR01DRSP2L,
       "hpnicfevtModuleSw-SR01DRUP1L": hpnicfevtModuleSw_SR01DRUP1L,
       "hpnicfevtModuleSw-SR01DGP20R": hpnicfevtModuleSw_SR01DGP20R,
       "hpnicfevtModuleSw-SR01DPLP8L": hpnicfevtModuleSw_SR01DPLP8L,
       "hpnicfevtModuleSw-SR01DXP2R": hpnicfevtModuleSw_SR01DXP2R,
       "hpnicfevtModuleSw-LSB1FW2A0": hpnicfevtModuleSw_LSB1FW2A0,
       "hpnicfevtModuleSw-LSB1GP48LDB": hpnicfevtModuleSw_LSB1GP48LDB,
       "hpnicfevtModuleSw-SR01LN1BNA0": hpnicfevtModuleSw_SR01LN1BNA0,
       "hpnicfevtModuleSw-SR01LN2BQH0": hpnicfevtModuleSw_SR01LN2BQH0,
       "hpnicfevtModuleSw-SR01LN2BNA0": hpnicfevtModuleSw_SR01LN2BNA0,
       "hpnicfevtModuleSw-SR01DGT20R": hpnicfevtModuleSw_SR01DGT20R,
       "hpnicfevtModuleSw-SR01DPSP4L": hpnicfevtModuleSw_SR01DPSP4L,
       "hpnicfevtModuleSw-SR01DPUP1L": hpnicfevtModuleSw_SR01DPUP1L,
       "hpnicfevtModuleSw-SR01DPL2G6L": hpnicfevtModuleSw_SR01DPL2G6L,
       "hpnicfevtModuleSw-SR01DPH2G6L": hpnicfevtModuleSw_SR01DPH2G6L,
       "hpnicfevtModuleSw-SR01DPS2G4L": hpnicfevtModuleSw_SR01DPS2G4L,
       "hpnicfevtModuleSw-SR01DCL1G8L": hpnicfevtModuleSw_SR01DCL1G8L,
       "hpnicfevtModuleSw-SR01DCL2G8L": hpnicfevtModuleSw_SR01DCL2G8L,
       "hpnicfevtModuleSw-SR01DET8G8L": hpnicfevtModuleSw_SR01DET8G8L,
       "hpnicfevtModuleSw-SR02SRP2E3": hpnicfevtModuleSw_SR02SRP2E3,
       "hpnicfevtModuleSw-SR02SRP1E3": hpnicfevtModuleSw_SR02SRP1E3,
       "hpnicfevtModuleSw-SR02SRP1M3": hpnicfevtModuleSw_SR02SRP1M3,
       "hpnicfevtModuleSw-SR01DQCP4L": hpnicfevtModuleSw_SR01DQCP4L,
       "hpnicfevtModuleSw-SR01DTCP8L": hpnicfevtModuleSw_SR01DTCP8L,
       "hpnicfevtModuleSw-LSB1AFC1A0": hpnicfevtModuleSw_LSB1AFC1A0,
       "hpnicfevtModuleSw-LSB1SSL1A0": hpnicfevtModuleSw_LSB1SSL1A0,
       "hpnicfevtModuleSw-IMNAM": hpnicfevtModuleSw_IMNAM,
       "hpnicfevtModuleSw-IMNAT": hpnicfevtModuleSw_IMNAT,
       "hpnicfevtModuleSw-PICAHP1L": hpnicfevtModuleSw_PICAHP1L,
       "hpnicfevtModuleSw-PICALP4L": hpnicfevtModuleSw_PICALP4L,
       "hpnicfevtModuleSw-PICCHP4L": hpnicfevtModuleSw_PICCHP4L,
       "hpnicfevtModuleSw-PICCHS1G4L": hpnicfevtModuleSw_PICCHS1G4L,
       "hpnicfevtModuleSw-PICCLS4G4L": hpnicfevtModuleSw_PICCLS4G4L,
       "hpnicfevtModuleSw-PICCSP1L": hpnicfevtModuleSw_PICCSP1L,
       "hpnicfevtModuleSw-LSB1ACG1A0": hpnicfevtModuleSw_LSB1ACG1A0,
       "hpnicfevtModuleSw-LST1MRPNC1": hpnicfevtModuleSw_LST1MRPNC1,
       "hpnicfevtModuleSw-LST1SF18B1": hpnicfevtModuleSw_LST1SF18B1,
       "hpnicfevtModuleSw-LST1SF08B1": hpnicfevtModuleSw_LST1SF08B1,
       "hpnicfevtModuleSw-LST1GT48LEC1": hpnicfevtModuleSw_LST1GT48LEC1,
       "hpnicfevtModuleSw-LST1GP48LEC1": hpnicfevtModuleSw_LST1GP48LEC1,
       "hpnicfevtModuleSw-LST1XP4LEC1": hpnicfevtModuleSw_LST1XP4LEC1,
       "hpnicfevtModuleSw-LST1XP8LEC1": hpnicfevtModuleSw_LST1XP8LEC1,
       "hpnicfevtModuleSw-LSR1SRP2B1": hpnicfevtModuleSw_LSR1SRP2B1,
       "hpnicfevtModuleSw-LSR1SRP2C1": hpnicfevtModuleSw_LSR1SRP2C1,
       "hpnicfevtModuleSw-LSR1SRP2B2": hpnicfevtModuleSw_LSR1SRP2B2,
       "hpnicfevtModuleSw-LSR1SRP2C2": hpnicfevtModuleSw_LSR1SRP2C2,
       "hpnicfevtModuleSw-LSR1GT24LEC1": hpnicfevtModuleSw_LSR1GT24LEC1,
       "hpnicfevtModuleSw-LSR1GP24LEB1": hpnicfevtModuleSw_LSR1GP24LEB1,
       "hpnicfevtModuleSw-LSR1GP24LEC1": hpnicfevtModuleSw_LSR1GP24LEC1,
       "hpnicfevtModuleSw-LSR1GT48LEB1": hpnicfevtModuleSw_LSR1GT48LEB1,
       "hpnicfevtModuleSw-LSR1GT48LEC1": hpnicfevtModuleSw_LSR1GT48LEC1,
       "hpnicfevtModuleSw-LSR1GP48LEB1": hpnicfevtModuleSw_LSR1GP48LEB1,
       "hpnicfevtModuleSw-LSR1GP48LEC1": hpnicfevtModuleSw_LSR1GP48LEC1,
       "hpnicfevtModuleSw-LSR2GV48REB1": hpnicfevtModuleSw_LSR2GV48REB1,
       "hpnicfevtModuleSw-LSR1XP2LEB1": hpnicfevtModuleSw_LSR1XP2LEB1,
       "hpnicfevtModuleSw-LSR1XP2LEC1": hpnicfevtModuleSw_LSR1XP2LEC1,
       "hpnicfevtModuleSw-LSR1XP4LEB1": hpnicfevtModuleSw_LSR1XP4LEB1,
       "hpnicfevtModuleSw-LSR1XP4LEC1": hpnicfevtModuleSw_LSR1XP4LEC1,
       "hpnicfevtModuleSw-IMFW": hpnicfevtModuleSw_IMFW,
       "hpnicfevtModuleSw-LSB1LB1A0": hpnicfevtModuleSw_LSB1LB1A0,
       "hpnicfevtModuleSw-LSB1IPS1A0": hpnicfevtModuleSw_LSB1IPS1A0,
       "hpnicfevtModuleSw-LST1GT48LEB1": hpnicfevtModuleSw_LST1GT48LEB1,
       "hpnicfevtModuleSw-LST1GP48LEB1": hpnicfevtModuleSw_LST1GP48LEB1,
       "hpnicfevtModuleSw-LST1XP4LEB1": hpnicfevtModuleSw_LST1XP4LEB1,
       "hpnicfevtModuleSw-LST1XP8LEB1": hpnicfevtModuleSw_LST1XP8LEB1,
       "hpnicfevtModuleSw-LST1XP32REB1": hpnicfevtModuleSw_LST1XP32REB1,
       "hpnicfevtModuleSw-LST1XP32REC1": hpnicfevtModuleSw_LST1XP32REC1,
       "hpnicfevtModuleSw-LSR1FW2A1": hpnicfevtModuleSw_LSR1FW2A1,
       "hpnicfevtModuleSw-LSR1SSL1A1": hpnicfevtModuleSw_LSR1SSL1A1,
       "hpnicfevtModuleSw-SR01DET32G2L": hpnicfevtModuleSw_SR01DET32G2L,
       "hpnicfevtModuleSw-LSR1GP24LEF1": hpnicfevtModuleSw_LSR1GP24LEF1,
       "hpnicfevtModuleSw-LSR1XP4LEF1": hpnicfevtModuleSw_LSR1XP4LEF1,
       "hpnicfevtModuleSw-LSR1LB1A1": hpnicfevtModuleSw_LSR1LB1A1,
       "hpnicfevtModuleSw-LSR1NSM1A1": hpnicfevtModuleSw_LSR1NSM1A1,
       "hpnicfevtModuleSw-LSR1ACG1A1": hpnicfevtModuleSw_LSR1ACG1A1,
       "hpnicfevtModuleSw-LSR1IPS1A1": hpnicfevtModuleSw_LSR1IPS1A1,
       "hpnicfevtModuleSw-LSR2GP24LEB1": hpnicfevtModuleSw_LSR2GP24LEB1,
       "hpnicfevtModuleSw-LSR2GT24LEB1": hpnicfevtModuleSw_LSR2GT24LEB1,
       "hpnicfevtModuleSw-LSR2GT48LEB1": hpnicfevtModuleSw_LSR2GT48LEB1,
       "hpnicfevtModuleSw-SPC-GP24L": hpnicfevtModuleSw_SPC_GP24L,
       "hpnicfevtModuleSw-SPC-GT48L": hpnicfevtModuleSw_SPC_GT48L,
       "hpnicfevtModuleSw-SPC-GP48L": hpnicfevtModuleSw_SPC_GP48L,
       "hpnicfevtModuleSw-SPC-XP2L": hpnicfevtModuleSw_SPC_XP2L,
       "hpnicfevtModuleSw-SPC-XP4L": hpnicfevtModuleSw_SPC_XP4L,
       "hpnicfevtModuleSw-SR06SRP2E3": hpnicfevtModuleSw_SR06SRP2E3,
       "hpnicfevtModuleSw-SPE-2010-E": hpnicfevtModuleSw_SPE_2010_E,
       "hpnicfevtModuleSw-SPE-2020-E": hpnicfevtModuleSw_SPE_2020_E,
       "hpnicfevtModuleSw-SPC-XP4L-S-SDI": hpnicfevtModuleSw_SPC_XP4L_S_SDI,
       "hpnicfevtModuleSw-SPC-GT48L-SDI": hpnicfevtModuleSw_SPC_GT48L_SDI,
       "hpnicfevtModuleSw-SPC-GP48L-S-SDI": hpnicfevtModuleSw_SPC_GP48L_S_SDI,
       "hpnicfevtModuleSw-SPC-SR02OPMA0": hpnicfevtModuleSw_SPC_SR02OPMA0,
       "hpnicfevtModuleSw-LSR1XP16REB1": hpnicfevtModuleSw_LSR1XP16REB1,
       "hpnicfevtModuleSw-LSR1GP48LEF1": hpnicfevtModuleSw_LSR1GP48LEF1,
       "hpnicfevtModuleSw-LST1GP48LEF1": hpnicfevtModuleSw_LST1GP48LEF1,
       "hpnicfevtModuleSw-LST1XP8LEF1": hpnicfevtModuleSw_LST1XP8LEF1,
       "hpnicfevtModuleSw-SPE-1010-II": hpnicfevtModuleSw_SPE_1010_II,
       "hpnicfevtModuleSw-SPE-1010-E-II": hpnicfevtModuleSw_SPE_1010_E_II,
       "hpnicfevtModuleSw-SPE-1020-II": hpnicfevtModuleSw_SPE_1020_II,
       "hpnicfevtModuleSw-SPE-1020-E-II": hpnicfevtModuleSw_SPE_1020_E_II,
       "hpnicfevtModuleSw-LST1FW2A1": hpnicfevtModuleSw_LST1FW2A1,
       "hpnicfevtModuleSw-LST1NSM1A1": hpnicfevtModuleSw_LST1NSM1A1,
       "hpnicfevtModuleSw-LST1LB1A1": hpnicfevtModuleSw_LST1LB1A1,
       "hpnicfevtModuleSw-LST1ACG1A1": hpnicfevtModuleSw_LST1ACG1A1,
       "hpnicfevtModuleSw-LST1IPS1A1": hpnicfevtModuleSw_LST1IPS1A1,
       "hpnicfevtModuleSw-LSR1DRUP1L1": hpnicfevtModuleSw_LSR1DRUP1L1,
       "hpnicfevtModuleSw-LSR1DPUP1L1": hpnicfevtModuleSw_LSR1DPUP1L1,
       "hpnicfevtModuleSw-LSR1DPSP4L1": hpnicfevtModuleSw_LSR1DPSP4L1,
       "hpnicfevtModuleSw-LSR1DTCP8L1": hpnicfevtModuleSw_LSR1DTCP8L1,
       "hpnicfevtModuleSw-LSR1DXP1L1": hpnicfevtModuleSw_LSR1DXP1L1,
       "hpnicfevtModuleSw-LSR1DGP10L1": hpnicfevtModuleSw_LSR1DGP10L1,
       "hpnicfevtModuleSw-LSR1LN1BNL1": hpnicfevtModuleSw_LSR1LN1BNL1,
       "hpnicfevtModuleSw-LSR1LN2BL1": hpnicfevtModuleSw_LSR1LN2BL1,
       "hpnicfevtModuleSw-LSR1SRP2D1": hpnicfevtModuleSw_LSR1SRP2D1,
       "hpnicfevtModuleSw-IM-NAT-II": hpnicfevtModuleSw_IM_NAT_II,
       "hpnicfevtModuleSw-IM-NAM-II": hpnicfevtModuleSw_IM_NAM_II,
       "hpnicfevtModuleSw-CR-MRP-I": hpnicfevtModuleSw_CR_MRP_I,
       "hpnicfevtModuleSw-CR-SF18C": hpnicfevtModuleSw_CR_SF18C,
       "hpnicfevtModuleSw-CR-SF08C": hpnicfevtModuleSw_CR_SF08C,
       "hpnicfevtModuleSw-CR-SPC-XP8LEF": hpnicfevtModuleSw_CR_SPC_XP8LEF,
       "hpnicfevtModuleSw-CR-SPC-XP4LEF": hpnicfevtModuleSw_CR_SPC_XP4LEF,
       "hpnicfevtModuleSw-CR-SPC-GP48LEF": hpnicfevtModuleSw_CR_SPC_GP48LEF,
       "hpnicfevtModuleSw-CR-SPC-GT48LEF": hpnicfevtModuleSw_CR_SPC_GT48LEF,
       "hpnicfevtModuleSw-CR-SPE-3020-E": hpnicfevtModuleSw_CR_SPE_3020_E,
       "hpnicfevtModuleSw-CR-SPC-PUP4L-E": hpnicfevtModuleSw_CR_SPC_PUP4L_E,
       "hpnicfevtModuleSw-LST1SF08C1": hpnicfevtModuleSw_LST1SF08C1,
       "hpnicfevtModuleSw-LST1SF18C1": hpnicfevtModuleSw_LST1SF18C1,
       "hpnicfevtModuleSw-LS81GP16TM": hpnicfevtModuleSw_LS81GP16TM,
       "hpnicfevtModuleSw-LS81VP4C": hpnicfevtModuleSw_LS81VP4C,
       "hpnicfevtModuleSw-LS8M1PT8P0": hpnicfevtModuleSw_LS8M1PT8P0,
       "hpnicfevtModuleSw-LS8M1PT8GB0": hpnicfevtModuleSw_LS8M1PT8GB0,
       "hpnicfevtModuleSw-LS8M1PT4GB0": hpnicfevtModuleSw_LS8M1PT4GB0,
       "hpnicfevtModuleSw-LS81GP2R": hpnicfevtModuleSw_LS81GP2R,
       "hpnicfevtModuleSw-LS81GP4R": hpnicfevtModuleSw_LS81GP4R,
       "hpnicfevtModuleSw-LS81IPSECA": hpnicfevtModuleSw_LS81IPSECA,
       "hpnicfevtModuleSw-LS81FWA": hpnicfevtModuleSw_LS81FWA,
       "hpnicfevtModuleSw-LS82VSNP": hpnicfevtModuleSw_LS82VSNP,
       "hpnicfevtModuleSw-LSQ1GV48SA": hpnicfevtModuleSw_LSQ1GV48SA,
       "hpnicfevtModuleSw-LSQ1SRPB": hpnicfevtModuleSw_LSQ1SRPB,
       "hpnicfevtModuleSw-LSQ1SRP2XB": hpnicfevtModuleSw_LSQ1SRP2XB,
       "hpnicfevtModuleSw-LSQ1SRP1CB": hpnicfevtModuleSw_LSQ1SRP1CB,
       "hpnicfevtModuleSw-LSQ1FV48SA": hpnicfevtModuleSw_LSQ1FV48SA,
       "hpnicfevtModuleSw-LSD1MPUA": hpnicfevtModuleSw_LSD1MPUA,
       "hpnicfevtModuleSw-LSD1GP20A0": hpnicfevtModuleSw_LSD1GP20A0,
       "hpnicfevtModuleSw-LSD1GP20TA0": hpnicfevtModuleSw_LSD1GP20TA0,
       "hpnicfevtModuleSw-LSD1GP36A0": hpnicfevtModuleSw_LSD1GP36A0,
       "hpnicfevtModuleSw-LSD1GP20XA0": hpnicfevtModuleSw_LSD1GP20XA0,
       "hpnicfevtModuleSw-LSD1GP20EA0": hpnicfevtModuleSw_LSD1GP20EA0,
       "hpnicfevtModuleSw-LSD1GP20RA0": hpnicfevtModuleSw_LSD1GP20RA0,
       "hpnicfevtModuleSw-LSD1GP16A0": hpnicfevtModuleSw_LSD1GP16A0,
       "hpnicfevtModuleSw-LSD1GT16A0": hpnicfevtModuleSw_LSD1GT16A0,
       "hpnicfevtModuleSw-LSD1XP2A0": hpnicfevtModuleSw_LSD1XP2A0,
       "hpnicfevtModuleSw-LSD1EP2A0": hpnicfevtModuleSw_LSD1EP2A0,
       "hpnicfevtModuleSw-LSD1RP2A0": hpnicfevtModuleSw_LSD1RP2A0,
       "hpnicfevtModuleSw-LSQ1GV48SC": hpnicfevtModuleSw_LSQ1GV48SC,
       "hpnicfevtModuleSw-LSQ1FP48SA": hpnicfevtModuleSw_LSQ1FP48SA,
       "hpnicfevtModuleSw-LSQ1GP24SC": hpnicfevtModuleSw_LSQ1GP24SC,
       "hpnicfevtModuleSw-LSQ1GT24SC": hpnicfevtModuleSw_LSQ1GT24SC,
       "hpnicfevtModuleSw-LSQ1TGX2SC": hpnicfevtModuleSw_LSQ1TGX2SC,
       "hpnicfevtModuleSw-LSQ1GP12EA": hpnicfevtModuleSw_LSQ1GP12EA,
       "hpnicfevtModuleSw-LSQ1TGX1EA": hpnicfevtModuleSw_LSQ1TGX1EA,
       "hpnicfevtModuleSw-LSQ1P24XGSC": hpnicfevtModuleSw_LSQ1P24XGSC,
       "hpnicfevtModuleSw-LSQ1T24XGSC": hpnicfevtModuleSw_LSQ1T24XGSC,
       "hpnicfevtModuleSw-LS81TGX1B": hpnicfevtModuleSw_LS81TGX1B,
       "hpnicfevtModuleSw-LSQ1PT4PSC0": hpnicfevtModuleSw_LSQ1PT4PSC0,
       "hpnicfevtModuleSw-LS81SRPG13": hpnicfevtModuleSw_LS81SRPG13,
       "hpnicfevtModuleSw-LS81SRPG14": hpnicfevtModuleSw_LS81SRPG14,
       "hpnicfevtModuleSw-LS81SRPG15": hpnicfevtModuleSw_LS81SRPG15,
       "hpnicfevtModuleSw-LSQ1GP48SC0": hpnicfevtModuleSw_LSQ1GP48SC0,
       "hpnicfevtModuleSw-LSQ1GP12SC0": hpnicfevtModuleSw_LSQ1GP12SC0,
       "hpnicfevtModuleSw-LSD1SRPA": hpnicfevtModuleSw_LSD1SRPA,
       "hpnicfevtModuleSw-LSD1SRPB": hpnicfevtModuleSw_LSD1SRPB,
       "hpnicfevtModuleSw-LSD1SRPC": hpnicfevtModuleSw_LSD1SRPC,
       "hpnicfevtModuleSw-LSD1GT16PES0": hpnicfevtModuleSw_LSD1GT16PES0,
       "hpnicfevtModuleSw-LSD1GP24ES0": hpnicfevtModuleSw_LSD1GP24ES0,
       "hpnicfevtModuleSw-LSD1GT24XES0": hpnicfevtModuleSw_LSD1GT24XES0,
       "hpnicfevtModuleSw-LSD1GP24XES0": hpnicfevtModuleSw_LSD1GP24XES0,
       "hpnicfevtModuleSw-LSD1XP2ES0": hpnicfevtModuleSw_LSD1XP2ES0,
       "hpnicfevtModuleSw-LSD1GP48ES0": hpnicfevtModuleSw_LSD1GP48ES0,
       "hpnicfevtModuleSw-LSQ1MPUA0": hpnicfevtModuleSw_LSQ1MPUA0,
       "hpnicfevtModuleSw-LSQ1MPUA1": hpnicfevtModuleSw_LSQ1MPUA1,
       "hpnicfevtModuleSw-LSQ1FWBSC0": hpnicfevtModuleSw_LSQ1FWBSC0,
       "hpnicfevtModuleSw-LSQ1PT8PSC0": hpnicfevtModuleSw_LSQ1PT8PSC0,
       "hpnicfevtModuleSw-LSQ1PT16PSC0": hpnicfevtModuleSw_LSQ1PT16PSC0,
       "hpnicfevtModuleSw-SA11MPUA0": hpnicfevtModuleSw_SA11MPUA0,
       "hpnicfevtModuleSw-SA11MPUB0": hpnicfevtModuleSw_SA11MPUB0,
       "hpnicfevtModuleSw-LSQ1AFCBSC0": hpnicfevtModuleSw_LSQ1AFCBSC0,
       "hpnicfevtModuleSw-LSQ1MPUB0": hpnicfevtModuleSw_LSQ1MPUB0,
       "hpnicfevtModuleSw-LSQ1MPUB1": hpnicfevtModuleSw_LSQ1MPUB1,
       "hpnicfevtModuleSw-LSQ1PT4PSC1": hpnicfevtModuleSw_LSQ1PT4PSC1,
       "hpnicfevtModuleSw-LSQ1PT8PSC1": hpnicfevtModuleSw_LSQ1PT8PSC1,
       "hpnicfevtModuleSw-LSQ1PT16PSC1": hpnicfevtModuleSw_LSQ1PT16PSC1,
       "hpnicfevtModuleSw-LSQ1FP48USA0": hpnicfevtModuleSw_LSQ1FP48USA0,
       "hpnicfevtModuleSw-LSQ1FP48USA1": hpnicfevtModuleSw_LSQ1FP48USA1,
       "hpnicfevtModuleSw-LSQ1FV48USA0": hpnicfevtModuleSw_LSQ1FV48USA0,
       "hpnicfevtModuleSw-LSQ1FV48USA1": hpnicfevtModuleSw_LSQ1FV48USA1,
       "hpnicfevtModuleSw-LSQ1SRPD0": hpnicfevtModuleSw_LSQ1SRPD0,
       "hpnicfevtModuleSw-LSQ1CGP24TSC0": hpnicfevtModuleSw_LSQ1CGP24TSC0,
       "hpnicfevtModuleSw-LSQ1GP24TSC0": hpnicfevtModuleSw_LSQ1GP24TSC0,
       "hpnicfevtModuleSw-LSQ1ACGASC0": hpnicfevtModuleSw_LSQ1ACGASC0,
       "hpnicfevtModuleSw-LSD1XP1ES0": hpnicfevtModuleSw_LSD1XP1ES0,
       "hpnicfevtModuleSw-LSD1GP12ES0": hpnicfevtModuleSw_LSD1GP12ES0,
       "hpnicfevtModuleSw-LSQ1SRP12GB0": hpnicfevtModuleSw_LSQ1SRP12GB0,
       "hpnicfevtModuleSw-LSQ1GV40PSC0": hpnicfevtModuleSw_LSQ1GV40PSC0,
       "hpnicfevtModuleSw-LSQ1FWBSC1": hpnicfevtModuleSw_LSQ1FWBSC1,
       "hpnicfevtModuleSw-LSQ1NSMSC0": hpnicfevtModuleSw_LSQ1NSMSC0,
       "hpnicfevtModuleSw-LSQ1NSMSC1": hpnicfevtModuleSw_LSQ1NSMSC1,
       "hpnicfevtModuleSw-LSQ1AFDBSC0": hpnicfevtModuleSw_LSQ1AFDBSC0,
       "hpnicfevtModuleSw-LS81MPUB": hpnicfevtModuleSw_LS81MPUB,
       "hpnicfevtModuleSw-LS81FP48XL": hpnicfevtModuleSw_LS81FP48XL,
       "hpnicfevtModuleSw-LS81FT48XL": hpnicfevtModuleSw_LS81FT48XL,
       "hpnicfevtModuleSw-LS81GP12XL": hpnicfevtModuleSw_LS81GP12XL,
       "hpnicfevtModuleSw-LS81GP24XL": hpnicfevtModuleSw_LS81GP24XL,
       "hpnicfevtModuleSw-LS81GP48XL": hpnicfevtModuleSw_LS81GP48XL,
       "hpnicfevtModuleSw-LS81GT24XL": hpnicfevtModuleSw_LS81GT24XL,
       "hpnicfevtModuleSw-LS81GT48XL": hpnicfevtModuleSw_LS81GT48XL,
       "hpnicfevtModuleSw-LS81TGX2XL": hpnicfevtModuleSw_LS81TGX2XL,
       "hpnicfevtModuleSw-LSQ1GV48SD0": hpnicfevtModuleSw_LSQ1GV48SD0,
       "hpnicfevtModuleSw-LSQ1GP48EB0": hpnicfevtModuleSw_LSQ1GP48EB0,
       "hpnicfevtModuleSw-LSQ1IPSSC0": hpnicfevtModuleSw_LSQ1IPSSC0,
       "hpnicfevtModuleSw-LSQ1GV48SD1": hpnicfevtModuleSw_LSQ1GV48SD1,
       "hpnicfevtModuleSw-LSQ1GP48SD0": hpnicfevtModuleSw_LSQ1GP48SD0,
       "hpnicfevtModuleSw-LSQ1GP48SD1": hpnicfevtModuleSw_LSQ1GP48SD1,
       "hpnicfevtModuleSw-LSQ1SRPA0": hpnicfevtModuleSw_LSQ1SRPA0,
       "hpnicfevtModuleSw-LSQ1SRPA1": hpnicfevtModuleSw_LSQ1SRPA1,
       "hpnicfevtModuleSw-LSQ2FP48SA0": hpnicfevtModuleSw_LSQ2FP48SA0,
       "hpnicfevtModuleSw-LSQ2FP48SA1": hpnicfevtModuleSw_LSQ2FP48SA1,
       "hpnicfevtModuleSw-LSQ2FT48SA0": hpnicfevtModuleSw_LSQ2FT48SA0,
       "hpnicfevtModuleSw-LSQ2FT48SA1": hpnicfevtModuleSw_LSQ2FT48SA1,
       "hpnicfevtModuleSw-LSQ1GV24PSC0": hpnicfevtModuleSw_LSQ1GV24PSC0,
       "hpnicfevtModuleSw-LSQ1GV24PSC1": hpnicfevtModuleSw_LSQ1GV24PSC1,
       "hpnicfevtModuleSw-LSQ1CGV24PSC0": hpnicfevtModuleSw_LSQ1CGV24PSC0,
       "hpnicfevtModuleSw-LSQ1CGV24PSC1": hpnicfevtModuleSw_LSQ1CGV24PSC1,
       "hpnicfevtModuleSw-LSQ1GP24TEB0": hpnicfevtModuleSw_LSQ1GP24TEB0,
       "hpnicfevtModuleSw-LSQ1GP24TEB1": hpnicfevtModuleSw_LSQ1GP24TEB1,
       "hpnicfevtModuleSw-LSQ1GP24TSD0": hpnicfevtModuleSw_LSQ1GP24TSD0,
       "hpnicfevtModuleSw-LSQ1GP24TSD1": hpnicfevtModuleSw_LSQ1GP24TSD1,
       "hpnicfevtModuleSw-LSQ1GP24TXSD0": hpnicfevtModuleSw_LSQ1GP24TXSD0,
       "hpnicfevtModuleSw-LSQ1GP24TXSD1": hpnicfevtModuleSw_LSQ1GP24TXSD1,
       "hpnicfevtModuleSw-LSQ1TGX2EB0": hpnicfevtModuleSw_LSQ1TGX2EB0,
       "hpnicfevtModuleSw-LSQ1TGX2EB1": hpnicfevtModuleSw_LSQ1TGX2EB1,
       "hpnicfevtModuleSw-LSQ1TGX2SD0": hpnicfevtModuleSw_LSQ1TGX2SD0,
       "hpnicfevtModuleSw-LSQ1TGX2SD1": hpnicfevtModuleSw_LSQ1TGX2SD1,
       "hpnicfevtModuleSw-LSQ1TGX4SD0": hpnicfevtModuleSw_LSQ1TGX4SD0,
       "hpnicfevtModuleSw-LSQ1TGX4SD1": hpnicfevtModuleSw_LSQ1TGX4SD1,
       "hpnicfevtModuleSw-LSQ1TGX8SD0": hpnicfevtModuleSw_LSQ1TGX8SD0,
       "hpnicfevtModuleSw-LSQ1TGX8SD1": hpnicfevtModuleSw_LSQ1TGX8SD1,
       "hpnicfevtModuleSw-LSQ1GP48EB1": hpnicfevtModuleSw_LSQ1GP48EB1,
       "hpnicfevtModuleSw-LSQ1TGX4EB0": hpnicfevtModuleSw_LSQ1TGX4EB0,
       "hpnicfevtModuleSw-LSQ1TGX4EB1": hpnicfevtModuleSw_LSQ1TGX4EB1,
       "hpnicfevtModuleSw-LSQ1GP12SC3": hpnicfevtModuleSw_LSQ1GP12SC3,
       "hpnicfevtModuleSw-LSQ1GP24TSC3": hpnicfevtModuleSw_LSQ1GP24TSC3,
       "hpnicfevtModuleSw-LSQ1GP48SC3": hpnicfevtModuleSw_LSQ1GP48SC3,
       "hpnicfevtModuleSw-LSQ1GV48SC3": hpnicfevtModuleSw_LSQ1GV48SC3,
       "hpnicfevtModuleSw-LSQ1MPUA3": hpnicfevtModuleSw_LSQ1MPUA3,
       "hpnicfevtModuleSw-LSQ1SRP1CB3": hpnicfevtModuleSw_LSQ1SRP1CB3,
       "hpnicfevtModuleSw-LSQ1SRPA3": hpnicfevtModuleSw_LSQ1SRPA3,
       "hpnicfevtModuleSw-LSQ2FP48SA3": hpnicfevtModuleSw_LSQ2FP48SA3,
       "hpnicfevtModuleSw-LSQ2FT48SA3": hpnicfevtModuleSw_LSQ2FT48SA3,
       "hpnicfevtModuleSw-LSQ1MPUB3": hpnicfevtModuleSw_LSQ1MPUB3,
       "hpnicfevtModuleSw-LSQ1CGP24TSC3": hpnicfevtModuleSw_LSQ1CGP24TSC3,
       "hpnicfevtModuleSw-LSQ1MPUB4": hpnicfevtModuleSw_LSQ1MPUB4,
       "hpnicfevtModuleSw-LSQ1SRPD4": hpnicfevtModuleSw_LSQ1SRPD4,
       "hpnicfevtModuleSw-LSQ1SSLSC0": hpnicfevtModuleSw_LSQ1SSLSC0,
       "hpnicfevtModuleSw-LSQ1LBSC0": hpnicfevtModuleSw_LSQ1LBSC0,
       "hpnicfevtModuleSw-LSQ1NAT24SC0": hpnicfevtModuleSw_LSQ1NAT24SC0,
       "hpnicfevtModuleSw-LSQ1SRP12GB4": hpnicfevtModuleSw_LSQ1SRP12GB4,
       "hpnicfevtModuleSw-LSQ1TGS8SC0": hpnicfevtModuleSw_LSQ1TGS8SC0,
       "hpnicfevtModuleSw-LSQ3PT4PSC0": hpnicfevtModuleSw_LSQ3PT4PSC0,
       "hpnicfevtModuleSw-EWPXM2MPUB0": hpnicfevtModuleSw_EWPXM2MPUB0,
       "hpnicfevtModuleSw-EWPXM2SRP12GB0": hpnicfevtModuleSw_EWPXM2SRP12GB0,
       "hpnicfevtModuleSw-EWPXM2SRPD0": hpnicfevtModuleSw_EWPXM2SRPD0,
       "hpnicfevtModuleSw-EWPXM2GP24TSD0": hpnicfevtModuleSw_EWPXM2GP24TSD0,
       "hpnicfevtModuleSw-EWPXM2GP24TXSD0": hpnicfevtModuleSw_EWPXM2GP24TXSD0,
       "hpnicfevtModuleSw-EWPXM2TGX4SD0": hpnicfevtModuleSw_EWPXM2TGX4SD0,
       "hpnicfevtModuleSw-EWPXM2GP48SD0": hpnicfevtModuleSw_EWPXM2GP48SD0,
       "hpnicfevtModuleSw-EWPXM2GP24TSC0": hpnicfevtModuleSw_EWPXM2GP24TSC0,
       "hpnicfevtModuleSw-EWPXM2TGX2SC0": hpnicfevtModuleSw_EWPXM2TGX2SC0,
       "hpnicfevtModuleSw-EWPXM2GP48SC0": hpnicfevtModuleSw_EWPXM2GP48SC0,
       "hpnicfevtModuleSw-LS7500-GP48-SC": hpnicfevtModuleSw_LS7500_GP48_SC,
       "hpnicfevtModuleSw-LS7500-GP48-SD": hpnicfevtModuleSw_LS7500_GP48_SD,
       "hpnicfevtModuleSw-LS7500-GT48-SC": hpnicfevtModuleSw_LS7500_GT48_SC,
       "hpnicfevtModuleSw-LS7500-GT48-SD": hpnicfevtModuleSw_LS7500_GT48_SD,
       "hpnicfevtModuleSw-LS7500-SRPG1": hpnicfevtModuleSw_LS7500_SRPG1,
       "hpnicfevtModuleSw-LS7500-SRPG2": hpnicfevtModuleSw_LS7500_SRPG2,
       "hpnicfevtModuleSw-LS7500-XP4-SD": hpnicfevtModuleSw_LS7500_XP4_SD,
       "hpnicfevtModuleSw-LS7500-XP8-SD": hpnicfevtModuleSw_LS7500_XP8_SD,
       "hpnicfevtModuleSw-LSQ4PT4PSC0": hpnicfevtModuleSw_LSQ4PT4PSC0,
       "hpnicfevtModuleSw-LSQ4PT8PSC0": hpnicfevtModuleSw_LSQ4PT8PSC0,
       "hpnicfevtModuleSw-LSQ4PT16PSC0": hpnicfevtModuleSw_LSQ4PT16PSC0,
       "hpnicfevtModuleSw-LSQ1GP24TSA0": hpnicfevtModuleSw_LSQ1GP24TSA0,
       "hpnicfevtModuleSw-LSQ1GV24PSA0": hpnicfevtModuleSw_LSQ1GV24PSA0,
       "hpnicfevtModuleSw-LSQ1SRPD3": hpnicfevtModuleSw_LSQ1SRPD3,
       "hpnicfevtModuleSw-LSQ1SUPA0": hpnicfevtModuleSw_LSQ1SUPA0,
       "hpnicfevtModuleSw-LSU1FAB04A0": hpnicfevtModuleSw_LSU1FAB04A0,
       "hpnicfevtModuleSw-LSU1FAB08A0": hpnicfevtModuleSw_LSU1FAB08A0,
       "hpnicfevtModuleSw-LSU1TGS8EA0": hpnicfevtModuleSw_LSU1TGS8EA0,
       "hpnicfevtModuleSw-LSU1TGS8EB0": hpnicfevtModuleSw_LSU1TGS8EB0,
       "hpnicfevtModuleSw-LSU1TGS8SE0": hpnicfevtModuleSw_LSU1TGS8SE0,
       "hpnicfevtModuleSw-LSUTGS16SC0": hpnicfevtModuleSw_LSUTGS16SC0,
       "hpnicfevtModuleSw-LSU1SUPA0": hpnicfevtModuleSw_LSU1SUPA0,
       "hpnicfevtModuleSw-LSU1GP24TXEA0": hpnicfevtModuleSw_LSU1GP24TXEA0,
       "hpnicfevtModuleSw-LSU1GP24TXEB0": hpnicfevtModuleSw_LSU1GP24TXEB0,
       "hpnicfevtModuleSw-LSU1GP24TXSE0": hpnicfevtModuleSw_LSU1GP24TXSE0,
       "hpnicfevtModuleSw-LSU1GP48EA0": hpnicfevtModuleSw_LSU1GP48EA0,
       "hpnicfevtModuleSw-LSU1GP48EB0": hpnicfevtModuleSw_LSU1GP48EB0,
       "hpnicfevtModuleSw-LSU1GP48SE0": hpnicfevtModuleSw_LSU1GP48SE0,
       "hpnicfevtModuleSw-LSU1GT48EA0": hpnicfevtModuleSw_LSU1GT48EA0,
       "hpnicfevtModuleSw-LSU1GT48SE0": hpnicfevtModuleSw_LSU1GT48SE0,
       "hpnicfevtModuleSw-LSU1TGX4EA0": hpnicfevtModuleSw_LSU1TGX4EA0,
       "hpnicfevtModuleSw-LSU1TGX4EB0": hpnicfevtModuleSw_LSU1TGX4EB0,
       "hpnicfevtModuleSw-LSU1TGX4SE0": hpnicfevtModuleSw_LSU1TGX4SE0,
       "hpnicfevtModuleSw-LSQ1FAB08A0": hpnicfevtModuleSw_LSQ1FAB08A0,
       "hpnicfevtModuleSw-EWPX2WCMD0": hpnicfevtModuleSw_EWPX2WCMD0,
       "hpnicfevtModuleSw-LSQ1WCMD0": hpnicfevtModuleSw_LSQ1WCMD0,
       "hpnicfevtModuleSw-LSQ1IAGSC0": hpnicfevtModuleSw_LSQ1IAGSC0,
       "hpnicfevtModuleSw-LSU1GP24TSE0": hpnicfevtModuleSw_LSU1GP24TSE0,
       "hpnicfevtModuleSw-LSQ1TGS16SC0": hpnicfevtModuleSw_LSQ1TGS16SC0,
       "hpnicfevtModuleSw-EWPX2TGS16SC0": hpnicfevtModuleSw_EWPX2TGS16SC0,
       "hpnicfevtModuleSw-LSQ1SUPA3": hpnicfevtModuleSw_LSQ1SUPA3,
       "hpnicfevtModuleSw-LSQ1FAB04A3": hpnicfevtModuleSw_LSQ1FAB04A3,
       "hpnicfevtModuleSw-LSQ1FAB08A3": hpnicfevtModuleSw_LSQ1FAB08A3,
       "hpnicfevtModuleSw-LSQ1GT48SC0": hpnicfevtModuleSw_LSQ1GT48SC0,
       "hpnicfevtModuleSw-LSR2SRP2C1": hpnicfevtModuleSw_LSR2SRP2C1,
       "hpnicfevtModuleSw-LSR2SRP2C2": hpnicfevtModuleSw_LSR2SRP2C2,
       "hpnicfevtModuleSw-1000BASE-X-COMBO": hpnicfevtModuleSw_1000BASE_X_COMBO,
       "hpnicfevtModuleSw-EPON-1000M": hpnicfevtModuleSw_EPON_1000M,
       "hpnicfevtModuleSw-1000BASE-FIXED-2SFP-T-2RJ45": hpnicfevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45,
       "hpnicfevtModuleSw-100M-1550-BIDI": hpnicfevtModuleSw_100M_1550_BIDI,
       "hpnicfevtModuleSw-100M-1310-BIDI": hpnicfevtModuleSw_100M_1310_BIDI,
       "hpnicfevtModuleSw-1000BASE-FIXED-4RJ45-4SFP-COMBO": hpnicfevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO,
       "hpnicfevtModuleSw-LSH1PK2T": hpnicfevtModuleSw_LSH1PK2T,
       "hpnicfevtModuleSw-LSPM2GP2P": hpnicfevtModuleSw_LSPM2GP2P,
       "hpnicfevtModuleSw-LSWM1GT16P": hpnicfevtModuleSw_LSWM1GT16P,
       "hpnicfevtModuleSw-LSWM1GP16P": hpnicfevtModuleSw_LSWM1GP16P,
       "hpnicfevtModuleSw-LSWM1XP2P": hpnicfevtModuleSw_LSWM1XP2P,
       "hpnicfevtModuleSw-LSWM1XP4P": hpnicfevtModuleSw_LSWM1XP4P,
       "hpnicfevtModuleSw-LSWM1SP2P": hpnicfevtModuleSw_LSWM1SP2P,
       "hpnicfevtModuleSw-LSWM1SP4P": hpnicfevtModuleSw_LSWM1SP4P,
       "hpnicfevtModuleSw-LSWM148POEM": hpnicfevtModuleSw_LSWM148POEM,
       "hpnicfevtModuleSw-LSWM1FW10": hpnicfevtModuleSw_LSWM1FW10,
       "hpnicfevtModuleSw-LSWM1WCM10": hpnicfevtModuleSw_LSWM1WCM10,
       "hpnicfevtModuleSw-LSWM1IPS10": hpnicfevtModuleSw_LSWM1IPS10,
       "hpnicfevtModuleSw-LSWM1WCM20": hpnicfevtModuleSw_LSWM1WCM20,
       "hpnicfevtModuleSw-IPS-T1000-M": hpnicfevtModuleSw_IPS_T1000_M,
       "hpnicfevtModuleSw-IPS-T1000-A": hpnicfevtModuleSw_IPS_T1000_A,
       "hpnicfevtModuleSw-IPS-T1000-S": hpnicfevtModuleSw_IPS_T1000_S,
       "hpnicfevtModuleSw-IPS-GX4C": hpnicfevtModuleSw_IPS_GX4C,
       "hpnicfevtModuleSw-IPS-GT4C": hpnicfevtModuleSw_IPS_GT4C,
       "hpnicfevtModuleSw-LSPM2SP2P": hpnicfevtModuleSw_LSPM2SP2P,
       "hpnicfevtModuleSw-LSPM2SP2PA": hpnicfevtModuleSw_LSPM2SP2PA,
       "hpnicfevtModuleSw-LSP5GP8P": hpnicfevtModuleSw_LSP5GP8P,
       "hpnicfevtModuleSw-LSP5GT8P": hpnicfevtModuleSw_LSP5GT8P,
       "hpnicfevtModuleSw-LSWM1FC4P": hpnicfevtModuleSw_LSWM1FC4P,
       "hpnicfevtModuleSw-LSW1XGT4P0": hpnicfevtModuleSw_LSW1XGT4P0,
       "hpnicfevtModuleSw-LSW1XGT2P0": hpnicfevtModuleSw_LSW1XGT2P0,
       "hpnicfevtModuleSw-LSP1XGT2P": hpnicfevtModuleSw_LSP1XGT2P,
       "hpnicfevtModuleSw-LSPM3XGT2P": hpnicfevtModuleSw_LSPM3XGT2P,
       "hpnicfevtModuleSw-LSWM2QP2P": hpnicfevtModuleSw_LSWM2QP2P,
       "hpnicfevtModuleSw-LSWM2XGT2PM": hpnicfevtModuleSw_LSWM2XGT2PM,
       "hpnicfevtModuleSw-LSWM2SP2PM": hpnicfevtModuleSw_LSWM2SP2PM,
       "hpnicfevtModuleSw-LSWM2SP8PM": hpnicfevtModuleSw_LSWM2SP8PM,
       "hpnicfevtModuleSw-LSWM2SP8P": hpnicfevtModuleSw_LSWM2SP8P,
       "hpnicfevtModuleSw-LSWM2XGT8PM": hpnicfevtModuleSw_LSWM2XGT8PM,
       "hpnicfevtModuleSw-LSWM18QC": hpnicfevtModuleSw_LSWM18QC,
       "hpnicfevtModuleSw-LSWM124XG2Q": hpnicfevtModuleSw_LSWM124XG2Q,
       "hpnicfevtModuleSw-LSWM124XGT2Q": hpnicfevtModuleSw_LSWM124XGT2Q,
       "hpnicfevtModuleSw-LSWM124XG2QL": hpnicfevtModuleSw_LSWM124XG2QL,
       "hpnicfevtModuleSw-WX5002MPU": hpnicfevtModuleSw_WX5002MPU,
       "hpnicfevtModuleSw-LS8M1WCMA": hpnicfevtModuleSw_LS8M1WCMA,
       "hpnicfevtModuleSw-EWPX1G24XA0": hpnicfevtModuleSw_EWPX1G24XA0,
       "hpnicfevtModuleSw-LSQ1WCMB0": hpnicfevtModuleSw_LSQ1WCMB0,
       "hpnicfevtModuleSw-LSB1WCM2A0": hpnicfevtModuleSw_LSB1WCM2A0,
       "hpnicfevtModuleSw-EWPX1WCMB0": hpnicfevtModuleSw_EWPX1WCMB0,
       "hpnicfevtModuleSw-EWPX1G24XC0": hpnicfevtModuleSw_EWPX1G24XC0,
       "hpnicfevtModuleSw-EWPX1WCMC0": hpnicfevtModuleSw_EWPX1WCMC0,
       "hpnicfevtModuleSw-EWPX1FWA0": hpnicfevtModuleSw_EWPX1FWA0,
       "hpnicfevtModuleSw-EWPX1G10XC0": hpnicfevtModuleSw_EWPX1G10XC0,
       "hpnicfevtModuleSw-EWPX1WCM10C0": hpnicfevtModuleSw_EWPX1WCM10C0,
       "hpnicfevtModuleSw-LSR1WCM2A1": hpnicfevtModuleSw_LSR1WCM2A1,
       "hpnicfevtModuleSw-EWPX1WAP0": hpnicfevtModuleSw_EWPX1WAP0,
       "hpnicfevtModuleSw-EWPX1WCMD0": hpnicfevtModuleSw_EWPX1WCMD0,
       "hpnicfevtModuleSw-EWPX1G24XCE0": hpnicfevtModuleSw_EWPX1G24XCE0,
       "hpnicfevtModuleSw-EWPX1WCMCE0": hpnicfevtModuleSw_EWPX1WCMCE0,
       "hpnicfevtModuleSw-EWPX1G24XD0": hpnicfevtModuleSw_EWPX1G24XD0,
       "hpnicfevtModuleSw-LSR1DRSP2L1": hpnicfevtModuleSw_LSR1DRSP2L1,
       "hpnicfevtModuleSw-PIC-CLF2G8L": hpnicfevtModuleSw_PIC_CLF2G8L,
       "hpnicfevtModuleSw-PIC-CLF4G8L": hpnicfevtModuleSw_PIC_CLF4G8L,
       "hpnicfevtModuleSw-SR02SRP2F3": hpnicfevtModuleSw_SR02SRP2F3,
       "hpnicfevtModuleSw-SR02SRP1F3": hpnicfevtModuleSw_SR02SRP1F3,
       "hpnicfevtModuleSw-LST1GT48LEA1": hpnicfevtModuleSw_LST1GT48LEA1,
       "hpnicfevtModuleSw-LST1GP48LEA1": hpnicfevtModuleSw_LST1GP48LEA1,
       "hpnicfevtModuleSw-LST2XP8LEA1": hpnicfevtModuleSw_LST2XP8LEA1,
       "hpnicfevtModuleSw-LST1GT48LEY1": hpnicfevtModuleSw_LST1GT48LEY1,
       "hpnicfevtModuleSw-LST1GP48LEY1": hpnicfevtModuleSw_LST1GP48LEY1,
       "hpnicfevtModuleSw-LST1XP32REY1": hpnicfevtModuleSw_LST1XP32REY1,
       "hpnicfevtModuleSw-LST1XP8LEY1": hpnicfevtModuleSw_LST1XP8LEY1,
       "hpnicfevtModuleSw-LST1GP48LEZ1": hpnicfevtModuleSw_LST1GP48LEZ1,
       "hpnicfevtModuleSw-LST1XP8LEZ1": hpnicfevtModuleSw_LST1XP8LEZ1,
       "hpnicfevtModuleSw-IM-FW-II": hpnicfevtModuleSw_IM_FW_II,
       "hpnicfevtModuleSw-IM-IPS": hpnicfevtModuleSw_IM_IPS,
       "hpnicfevtModuleSw-IM-SSL": hpnicfevtModuleSw_IM_SSL,
       "hpnicfevtModuleSw-IM-LB": hpnicfevtModuleSw_IM_LB,
       "hpnicfevtModuleSw-IM-ACG": hpnicfevtModuleSw_IM_ACG,
       "hpnicfevtModuleSw-LSR1XP16REC1": hpnicfevtModuleSw_LSR1XP16REC1,
       "hpnicfevtModuleSw-LST2XP8LEB1": hpnicfevtModuleSw_LST2XP8LEB1,
       "hpnicfevtModuleSw-LST2XP8LEC1": hpnicfevtModuleSw_LST2XP8LEC1,
       "hpnicfevtModuleSw-LST2XP8LEF1": hpnicfevtModuleSw_LST2XP8LEF1,
       "hpnicfevtModuleSw-LSR2XP4LEB1": hpnicfevtModuleSw_LSR2XP4LEB1,
       "hpnicfevtModuleSw-LSR2XP4LEC1": hpnicfevtModuleSw_LSR2XP4LEC1,
       "hpnicfevtModuleSw-LST2XP32REB1": hpnicfevtModuleSw_LST2XP32REB1,
       "hpnicfevtModuleSw-LST2XP32REC1": hpnicfevtModuleSw_LST2XP32REC1,
       "hpnicfevtModuleSw-LSR1WCM3A1": hpnicfevtModuleSw_LSR1WCM3A1,
       "hpnicfevtModuleSw-LST1XP16LEB1": hpnicfevtModuleSw_LST1XP16LEB1,
       "hpnicfevtModuleSw-LST1XP16LEC1": hpnicfevtModuleSw_LST1XP16LEC1,
       "hpnicfevtModuleSw-CR-SPC-XP4L-E-I": hpnicfevtModuleSw_CR_SPC_XP4L_E_I,
       "hpnicfevtModuleSw-LST2MRPNC1": hpnicfevtModuleSw_LST2MRPNC1,
       "hpnicfevtModuleSw-LST2SF08C1": hpnicfevtModuleSw_LST2SF08C1,
       "hpnicfevtModuleSw-LST2SF18C1": hpnicfevtModuleSw_LST2SF18C1,
       "hpnicfevtModuleSw-SR02SRP2G3": hpnicfevtModuleSw_SR02SRP2G3,
       "hpnicfevtModuleSw-CR-SPE-3020-E-I": hpnicfevtModuleSw_CR_SPE_3020_E_I,
       "hpnicfevtModuleSw-CR-SPC-PUP4L-E-I": hpnicfevtModuleSw_CR_SPC_PUP4L_E_I,
       "hpnicfevtModuleSw-CR-SPC-XP4LEF-I": hpnicfevtModuleSw_CR_SPC_XP4LEF_I,
       "hpnicfevtModuleSw-CR-SPC-XP8LEF-I": hpnicfevtModuleSw_CR_SPC_XP8LEF_I,
       "hpnicfevtModuleSw-LST3XP8LEB1": hpnicfevtModuleSw_LST3XP8LEB1,
       "hpnicfevtModuleSw-LST3XP8LEC1": hpnicfevtModuleSw_LST3XP8LEC1,
       "hpnicfevtModuleSw-LST1FW3A1": hpnicfevtModuleSw_LST1FW3A1,
       "hpnicfevtModuleSw-CR-IM-NAM1A": hpnicfevtModuleSw_CR_IM_NAM1A,
       "hpnicfevtModuleSw-LSR2SRP2B1": hpnicfevtModuleSw_LSR2SRP2B1,
       "hpnicfevtModuleSw-LSR2SRP2B2": hpnicfevtModuleSw_LSR2SRP2B2,
       "hpnicfevtModuleSw-LSR2SRP2D1": hpnicfevtModuleSw_LSR2SRP2D1,
       "hpnicfevtModuleSw-LST3XP8LEY1": hpnicfevtModuleSw_LST3XP8LEY1,
       "hpnicfevtModuleSw-LST2XP32REY1": hpnicfevtModuleSw_LST2XP32REY1,
       "hpnicfevtModuleSw-LST1XP16LEY1": hpnicfevtModuleSw_LST1XP16LEY1,
       "hpnicfevtModuleSw-SR0M2SRP2G3": hpnicfevtModuleSw_SR0M2SRP2G3,
       "hpnicfevtModuleSw-SR0M2SRP1G3": hpnicfevtModuleSw_SR0M2SRP1G3,
       "hpnicfevtModuleSw-SPC-GP48LA": hpnicfevtModuleSw_SPC_GP48LA,
       "hpnicfevtModuleSw-SPC-GT48LA": hpnicfevtModuleSw_SPC_GT48LA,
       "hpnicfevtModuleSw-SPC-XP4LA": hpnicfevtModuleSw_SPC_XP4LA,
       "hpnicfevtModuleSw-SPC-XP2LA": hpnicfevtModuleSw_SPC_XP2LA,
       "hpnicfevtModuleSw-SPC-GP24LA": hpnicfevtModuleSw_SPC_GP24LA,
       "hpnicfevtModuleSw-SPC-XP16RA": hpnicfevtModuleSw_SPC_XP16RA,
       "hpnicfevtModuleSw-CR-IM-FW1A": hpnicfevtModuleSw_CR_IM_FW1A,
       "hpnicfevtModuleSw-SPC-XP16R": hpnicfevtModuleSw_SPC_XP16R,
       "hpnicfevtModuleSw-CR-IM-LB1A": hpnicfevtModuleSw_CR_IM_LB1A,
       "hpnicfevtModuleSw-LST1GT48LEC2": hpnicfevtModuleSw_LST1GT48LEC2,
       "hpnicfevtModuleSw-LST1GP48LEC2": hpnicfevtModuleSw_LST1GP48LEC2,
       "hpnicfevtModuleSw-LST1XP16LEC2": hpnicfevtModuleSw_LST1XP16LEC2,
       "hpnicfevtModuleSw-LST2XP8LEC2": hpnicfevtModuleSw_LST2XP8LEC2,
       "hpnicfevtModuleSw-LST2XP32REC2": hpnicfevtModuleSw_LST2XP32REC2,
       "hpnicfevtModuleSw-CR-IM-MAC1A": hpnicfevtModuleSw_CR_IM_MAC1A,
       "hpnicfevtModuleSw-LST1XP48LFD1": hpnicfevtModuleSw_LST1XP48LFD1,
       "hpnicfevtModuleSw-LST1XP40RFD1": hpnicfevtModuleSw_LST1XP40RFD1,
       "hpnicfevtModuleSw-LST1XP40RFG1": hpnicfevtModuleSw_LST1XP40RFG1,
       "hpnicfevtModuleSw-LST1XLP16RFD1": hpnicfevtModuleSw_LST1XLP16RFD1,
       "hpnicfevtModuleSw-LST1CP4RFD1": hpnicfevtModuleSw_LST1CP4RFD1,
       "hpnicfevtModuleSw-LST1CP4RFG1": hpnicfevtModuleSw_LST1CP4RFG1,
       "hpnicfevtModuleSw-LST1SF08E1": hpnicfevtModuleSw_LST1SF08E1,
       "hpnicfevtModuleSw-LST1SF18E1": hpnicfevtModuleSw_LST1SF18E1,
       "hpnicfevtModuleSw-LST1MRPNE1": hpnicfevtModuleSw_LST1MRPNE1,
       "hpnicfevtModuleSw-LSX1CGX8FC0": hpnicfevtModuleSw_LSX1CGX8FC0,
       "hpnicfevtModuleSw-LSX1CGX8FC1": hpnicfevtModuleSw_LSX1CGX8FC1,
       "hpnicfevtModuleSw-LSX1QGS24FC0": hpnicfevtModuleSw_LSX1QGS24FC0,
       "hpnicfevtModuleSw-LSX1QGS24FC1": hpnicfevtModuleSw_LSX1QGS24FC1,
       "hpnicfevtModuleSw-LSX1TGS24FC0": hpnicfevtModuleSw_LSX1TGS24FC0,
       "hpnicfevtModuleSw-LSX1TGS24FC1": hpnicfevtModuleSw_LSX1TGS24FC1,
       "hpnicfevtModuleSw-LSX1TGS48FC0": hpnicfevtModuleSw_LSX1TGS48FC0,
       "hpnicfevtModuleSw-LSX1TGS48FC1": hpnicfevtModuleSw_LSX1TGS48FC1,
       "hpnicfevtModuleSw-LST1XP48LFD2": hpnicfevtModuleSw_LST1XP48LFD2,
       "hpnicfevtModuleSw-LST1XP40RFD2": hpnicfevtModuleSw_LST1XP40RFD2,
       "hpnicfevtModuleSw-LST1XP40RFG2": hpnicfevtModuleSw_LST1XP40RFG2,
       "hpnicfevtModuleSw-LST1XLP16RFD2": hpnicfevtModuleSw_LST1XLP16RFD2,
       "hpnicfevtModuleSw-LST1CP4RFD2": hpnicfevtModuleSw_LST1CP4RFD2,
       "hpnicfevtModuleSw-LST1CP4RFG2": hpnicfevtModuleSw_LST1CP4RFG2,
       "hpnicfevtModuleSw-MPE-1004": hpnicfevtModuleSw_MPE_1004,
       "hpnicfevtModuleSw-MIC-GP4L": hpnicfevtModuleSw_MIC_GP4L,
       "hpnicfevtModuleSw-MIC-GP8L": hpnicfevtModuleSw_MIC_GP8L,
       "hpnicfevtModuleSw-MIC-SP4L": hpnicfevtModuleSw_MIC_SP4L,
       "hpnicfevtModuleSw-MIC-ET16L": hpnicfevtModuleSw_MIC_ET16L,
       "hpnicfevtModuleSw-MIC-CLP4L": hpnicfevtModuleSw_MIC_CLP4L,
       "hpnicfevtModuleSw-MIC-CLP2L": hpnicfevtModuleSw_MIC_CLP2L,
       "hpnicfevtModuleSw-LST1IPS2A1": hpnicfevtModuleSw_LST1IPS2A1,
       "hpnicfevtModuleSw-SFC-04B": hpnicfevtModuleSw_SFC_04B,
       "hpnicfevtModuleSw-SFC-04D": hpnicfevtModuleSw_SFC_04D,
       "hpnicfevtModuleSw-SFC-08B": hpnicfevtModuleSw_SFC_08B,
       "hpnicfevtModuleSw-SFC-08D": hpnicfevtModuleSw_SFC_08D,
       "hpnicfevtModuleSw-SFC-12B": hpnicfevtModuleSw_SFC_12B,
       "hpnicfevtModuleSw-SFC-12D": hpnicfevtModuleSw_SFC_12D,
       "hpnicfevtModuleSw-SR05SRP1H1": hpnicfevtModuleSw_SR05SRP1H1,
       "hpnicfevtModuleSw-SPC-GP24LA1": hpnicfevtModuleSw_SPC_GP24LA1,
       "hpnicfevtModuleSw-SPC-GP24XP2LA": hpnicfevtModuleSw_SPC_GP24XP2LA,
       "hpnicfevtModuleSw-SPC-GP48LA1": hpnicfevtModuleSw_SPC_GP48LA1,
       "hpnicfevtModuleSw-SPC-GP48LB": hpnicfevtModuleSw_SPC_GP48LB,
       "hpnicfevtModuleSw-SPC-XP2LA1": hpnicfevtModuleSw_SPC_XP2LA1,
       "hpnicfevtModuleSw-SPC-XP4LA1": hpnicfevtModuleSw_SPC_XP4LA1,
       "hpnicfevtModuleSw-SPC-XP4LB": hpnicfevtModuleSw_SPC_XP4LB,
       "hpnicfevtModuleSw-SPC-XP8LA": hpnicfevtModuleSw_SPC_XP8LA,
       "hpnicfevtModuleSw-SPC-XP8LB": hpnicfevtModuleSw_SPC_XP8LB,
       "hpnicfevtModuleSw-SPC-XP48LA": hpnicfevtModuleSw_SPC_XP48LA,
       "hpnicfevtModuleSw-SPC-XLP8LA": hpnicfevtModuleSw_SPC_XLP8LA,
       "hpnicfevtModuleSw-SPC-GP24XP2LB": hpnicfevtModuleSw_SPC_GP24XP2LB,
       "hpnicfevtModuleSw-LST1MRPNE2": hpnicfevtModuleSw_LST1MRPNE2,
       "hpnicfevtModuleSw-LST2FW3A1": hpnicfevtModuleSw_LST2FW3A1,
       "hpnicfevtModuleSw-LST1ADE1A1": hpnicfevtModuleSw_LST1ADE1A1,
       "hpnicfevtModuleSw-CR-MRP-II": hpnicfevtModuleSw_CR_MRP_II,
       "hpnicfevtModuleSw-CR-SF08E": hpnicfevtModuleSw_CR_SF08E,
       "hpnicfevtModuleSw-CR-SF18E": hpnicfevtModuleSw_CR_SF18E,
       "hpnicfevtModuleSw-CR-SPC-XP40RC": hpnicfevtModuleSw_CR_SPC_XP40RC,
       "hpnicfevtModuleSw-CR-SPC-XP40RB": hpnicfevtModuleSw_CR_SPC_XP40RB,
       "hpnicfevtModuleSw-CR-SPC-CP4RC": hpnicfevtModuleSw_CR_SPC_CP4RC,
       "hpnicfevtModuleSw-LST1FW3C1": hpnicfevtModuleSw_LST1FW3C1,
       "hpnicfevtModuleSw-LSU1FWCEA0": hpnicfevtModuleSw_LSU1FWCEA0,
       "hpnicfevtModuleSw-SPC-GT48LA1": hpnicfevtModuleSw_SPC_GT48LA1,
       "hpnicfevtModuleSw-LST1XP20RFD1": hpnicfevtModuleSw_LST1XP20RFD1,
       "hpnicfevtModuleSw-LST1XP20RFD2": hpnicfevtModuleSw_LST1XP20RFD2,
       "hpnicfevtModuleSw-MPE-1104": hpnicfevtModuleSw_MPE_1104,
       "hpnicfevtModuleSw-SPEX-1204": hpnicfevtModuleSw_SPEX_1204,
       "hpnicfevtModuleSw-SPC-GP44XP4LCX": hpnicfevtModuleSw_SPC_GP44XP4LCX,
       "hpnicfevtModuleSw-SPC-GP44XP4LAX": hpnicfevtModuleSw_SPC_GP44XP4LAX,
       "hpnicfevtModuleSw-SPC-XP24LCX": hpnicfevtModuleSw_SPC_XP24LCX,
       "hpnicfevtModuleSw-SPC-XP24LAX": hpnicfevtModuleSw_SPC_XP24LAX,
       "hpnicfevtModuleSw-SPC-XP12LCX": hpnicfevtModuleSw_SPC_XP12LCX,
       "hpnicfevtModuleSw-SPC-XP12LAX": hpnicfevtModuleSw_SPC_XP12LAX,
       "hpnicfevtModuleSw-SPC-XLP6LCX": hpnicfevtModuleSw_SPC_XLP6LCX,
       "hpnicfevtModuleSw-SPC-XLP6LAX": hpnicfevtModuleSw_SPC_XLP6LAX,
       "hpnicfevtModuleSw-SPC-CP1LCX": hpnicfevtModuleSw_SPC_CP1LCX,
       "hpnicfevtModuleSw-SPC-CP1LAX": hpnicfevtModuleSw_SPC_CP1LAX,
       "hpnicfevtModuleSw-SPC-CP2LB": hpnicfevtModuleSw_SPC_CP2LB,
       "hpnicfevtModuleSw-SPC-CP2LA": hpnicfevtModuleSw_SPC_CP2LA,
       "hpnicfevtModuleSw-SR05SRP1L1": hpnicfevtModuleSw_SR05SRP1L1,
       "hpnicfevtModuleSw-SR05SRP1L3": hpnicfevtModuleSw_SR05SRP1L3,
       "hpnicfevtModuleSw-SFC-04-4": hpnicfevtModuleSw_SFC_04_4,
       "hpnicfevtModuleSw-SFC-04-3": hpnicfevtModuleSw_SFC_04_3,
       "hpnicfevtModuleSw-SFC-04-2": hpnicfevtModuleSw_SFC_04_2,
       "hpnicfevtModuleSw-SFC-04-1": hpnicfevtModuleSw_SFC_04_1,
       "hpnicfevtModuleSw-LST1NSM2C1": hpnicfevtModuleSw_LST1NSM2C1,
       "hpnicfevtModuleSw-CR-SPC-XP20RB": hpnicfevtModuleSw_CR_SPC_XP20RB,
       "hpnicfevtModuleSw-SR07SRPUA1": hpnicfevtModuleSw_SR07SRPUA1,
       "hpnicfevtModuleSw-SR07SRPUB3": hpnicfevtModuleSw_SR07SRPUB3,
       "hpnicfevtModuleSw-SR07SRPUC3": hpnicfevtModuleSw_SR07SRPUC3,
       "hpnicfevtModuleSw-SR07MPUA1": hpnicfevtModuleSw_SR07MPUA1,
       "hpnicfevtModuleSw-SR07SRPUB1": hpnicfevtModuleSw_SR07SRPUB1,
       "hpnicfevtModuleSw-SR07SRPUC1": hpnicfevtModuleSw_SR07SRPUC1,
       "hpnicfevtModuleSw-MIC-MS4L": hpnicfevtModuleSw_MIC_MS4L,
       "hpnicfevtModuleSw-SPC-GP44XP4LC": hpnicfevtModuleSw_SPC_GP44XP4LC,
       "hpnicfevtModuleSw-SPC-GP44XP4LA": hpnicfevtModuleSw_SPC_GP44XP4LA,
       "hpnicfevtModuleSw-SPC-XLP2XP4LC": hpnicfevtModuleSw_SPC_XLP2XP4LC,
       "hpnicfevtModuleSw-SPC-XP12LC": hpnicfevtModuleSw_SPC_XP12LC,
       "hpnicfevtModuleSw-SPC-CP1LC": hpnicfevtModuleSw_SPC_CP1LC,
       "hpnicfevtModuleSw-SPC-XP24LC": hpnicfevtModuleSw_SPC_XP24LC,
       "hpnicfevtModuleSw-SR07SRPUD3": hpnicfevtModuleSw_SR07SRPUD3,
       "hpnicfevtModuleSw-SR07MPUA3": hpnicfevtModuleSw_SR07MPUA3,
       "hpnicfevtModuleSw-MPEX-1304": hpnicfevtModuleSw_MPEX_1304,
       "hpnicfevtModuleSw-MIC-GP10L1": hpnicfevtModuleSw_MIC_GP10L1,
       "hpnicfevtModuleSw-SR07SRPUB": hpnicfevtModuleSw_SR07SRPUB,
       "hpnicfevtModuleSw-CMPE-1104": hpnicfevtModuleSw_CMPE_1104,
       "hpnicfevtModuleSw-CSFC-04-1": hpnicfevtModuleSw_CSFC_04_1,
       "hpnicfevtModuleSw-CSFC-04-2": hpnicfevtModuleSw_CSFC_04_2,
       "hpnicfevtModuleSw-CSFC-04-3": hpnicfevtModuleSw_CSFC_04_3,
       "hpnicfevtModuleSw-CSFC-04-4": hpnicfevtModuleSw_CSFC_04_4,
       "hpnicfevtModuleSw-CSFC-04B": hpnicfevtModuleSw_CSFC_04B,
       "hpnicfevtModuleSw-CSFC-04D": hpnicfevtModuleSw_CSFC_04D,
       "hpnicfevtModuleSw-CSFC-08B": hpnicfevtModuleSw_CSFC_08B,
       "hpnicfevtModuleSw-CSFC-08D": hpnicfevtModuleSw_CSFC_08D,
       "hpnicfevtModuleSw-CSFC-12B": hpnicfevtModuleSw_CSFC_12B,
       "hpnicfevtModuleSw-CSFC-12D": hpnicfevtModuleSw_CSFC_12D,
       "hpnicfevtModuleSw-CSPC-CP1LCX": hpnicfevtModuleSw_CSPC_CP1LCX,
       "hpnicfevtModuleSw-CSPC-CP2LB": hpnicfevtModuleSw_CSPC_CP2LB,
       "hpnicfevtModuleSw-CSPC-GP24LA1": hpnicfevtModuleSw_CSPC_GP24LA1,
       "hpnicfevtModuleSw-CSPC-GP24XP2LB": hpnicfevtModuleSw_CSPC_GP24XP2LB,
       "hpnicfevtModuleSw-CSPC-GP44XP4LCX": hpnicfevtModuleSw_CSPC_GP44XP4LCX,
       "hpnicfevtModuleSw-CSPC-GP48LB": hpnicfevtModuleSw_CSPC_GP48LB,
       "hpnicfevtModuleSw-CSPC-GT48LA1": hpnicfevtModuleSw_CSPC_GT48LA1,
       "hpnicfevtModuleSw-CSPC-XLP6LCX": hpnicfevtModuleSw_CSPC_XLP6LCX,
       "hpnicfevtModuleSw-CSPC-XP2LA1": hpnicfevtModuleSw_CSPC_XP2LA1,
       "hpnicfevtModuleSw-CSPC-XP4LB": hpnicfevtModuleSw_CSPC_XP4LB,
       "hpnicfevtModuleSw-CSPC-XP8LB": hpnicfevtModuleSw_CSPC_XP8LB,
       "hpnicfevtModuleSw-CSPC-XP12LAX": hpnicfevtModuleSw_CSPC_XP12LAX,
       "hpnicfevtModuleSw-CSPC-XP12LCX": hpnicfevtModuleSw_CSPC_XP12LCX,
       "hpnicfevtModuleSw-CSPC-XP24LAX": hpnicfevtModuleSw_CSPC_XP24LAX,
       "hpnicfevtModuleSw-CSPC-XP24LCX": hpnicfevtModuleSw_CSPC_XP24LCX,
       "hpnicfevtModuleSw-CSPC-CSPEX-1204": hpnicfevtModuleSw_CSPC_CSPEX_1204,
       "hpnicfevtModuleSw-CSR05SRP1L1": hpnicfevtModuleSw_CSR05SRP1L1,
       "hpnicfevtModuleSw-CSR05SRP1L3": hpnicfevtModuleSw_CSR05SRP1L3,
       "hpnicfevtModuleSw-CSR07MPUA1": hpnicfevtModuleSw_CSR07MPUA1,
       "hpnicfevtModuleSw-CSR07SRPUA1": hpnicfevtModuleSw_CSR07SRPUA1,
       "hpnicfevtModuleSw-CSR07SRPUB1": hpnicfevtModuleSw_CSR07SRPUB1,
       "hpnicfevtModuleSw-CSR07SRPUC1": hpnicfevtModuleSw_CSR07SRPUC1,
       "hpnicfevtModuleSw-LSXM1CGX8FX1": hpnicfevtModuleSw_LSXM1CGX8FX1,
       "hpnicfevtModuleSw-LSXM1QGS24FX1": hpnicfevtModuleSw_LSXM1QGS24FX1,
       "hpnicfevtModuleSw-LSXM1TGS48FX1": hpnicfevtModuleSw_LSXM1TGS48FX1,
       "hpnicfevtModuleSw-LSXM1QGS12FX1": hpnicfevtModuleSw_LSXM1QGS12FX1,
       "hpnicfevtModuleSw-LSXM1TGT48FX1": hpnicfevtModuleSw_LSXM1TGT48FX1,
       "hpnicfevtModuleSw-LSU1IPSBEA0": hpnicfevtModuleSw_LSU1IPSBEA0,
       "hpnicfevtModuleSw-LSU1QGC4SF0": hpnicfevtModuleSw_LSU1QGC4SF0,
       "hpnicfevtModuleSw-LSU1QGS8SF0": hpnicfevtModuleSw_LSU1QGS8SF0,
       "hpnicfevtModuleSw-LSU1TGS48SF0": hpnicfevtModuleSw_LSU1TGS48SF0,
       "hpnicfevtModuleSw-LSU1QGS4SF0": hpnicfevtModuleSw_LSU1QGS4SF0,
       "hpnicfevtModuleSw-LSU1TGS32SF0": hpnicfevtModuleSw_LSU1TGS32SF0,
       "hpnicfevtModuleSw-LSU1FAB08D0": hpnicfevtModuleSw_LSU1FAB08D0,
       "hpnicfevtModuleSw-LSU1FAB04B0": hpnicfevtModuleSw_LSU1FAB04B0,
       "hpnicfevtModuleSw-LSU1FAB08B0": hpnicfevtModuleSw_LSU1FAB08B0,
       "hpnicfevtModuleSw-LSU1FAB12D0": hpnicfevtModuleSw_LSU1FAB12D0,
       "hpnicfevtModuleSw-LSU1FAB12B0": hpnicfevtModuleSw_LSU1FAB12B0,
       "hpnicfevtModuleSw-LSU1FAB04D0": hpnicfevtModuleSw_LSU1FAB04D0,
       "hpnicfevtModuleSw-LSQ1CTGS16SC0": hpnicfevtModuleSw_LSQ1CTGS16SC0,
       "hpnicfevtModuleSw-EWPX2CTGS16SC0": hpnicfevtModuleSw_EWPX2CTGS16SC0,
       "hpnicfevtModuleSw-LSU3WCMD0": hpnicfevtModuleSw_LSU3WCMD0,
       "hpnicfevtModuleSw-EWPX3WCMD0": hpnicfevtModuleSw_EWPX3WCMD0,
       "hpnicfevtModuleSw-LSQ1QGS4SC0": hpnicfevtModuleSw_LSQ1QGS4SC0,
       "hpnicfevtModuleSw-LSQ1QGC4SC0": hpnicfevtModuleSw_LSQ1QGC4SC0,
       "hpnicfevtModuleSw-LSU1TGT24SF0": hpnicfevtModuleSw_LSU1TGT24SF0,
       "hpnicfevtModuleSw-LSQ1QGS8SC3": hpnicfevtModuleSw_LSQ1QGS8SC3,
       "hpnicfevtModuleSw-LSQ1TGS32SC3": hpnicfevtModuleSw_LSQ1TGS32SC3,
       "hpnicfevtModuleSw-LSQ1QGS4SC3": hpnicfevtModuleSw_LSQ1QGS4SC3,
       "hpnicfevtModuleSw-LSQ1TGS48SC3": hpnicfevtModuleSw_LSQ1TGS48SC3,
       "hpnicfevtModuleSw-LSQ1QGC4SC3": hpnicfevtModuleSw_LSQ1QGC4SC3,
       "hpnicfevtModuleSw-LSQ1FAB12D3": hpnicfevtModuleSw_LSQ1FAB12D3,
       "hpnicfevtModuleSw-LSQ1FAB08D3": hpnicfevtModuleSw_LSQ1FAB08D3,
       "hpnicfevtModuleSw-LSQ1FAB04D3": hpnicfevtModuleSw_LSQ1FAB04D3,
       "hpnicfevtModuleSw-LSQ1TGS8EB3": hpnicfevtModuleSw_LSQ1TGS8EB3,
       "hpnicfevtModuleSw-LSQ1TGT24SC3": hpnicfevtModuleSw_LSQ1TGT24SC3,
       "hpnicfevtModuleSw-LSQ1FAB08B0": hpnicfevtModuleSw_LSQ1FAB08B0,
       "hpnicfevtModuleSw-EWPX2CTGS16SC": hpnicfevtModuleSw_EWPX2CTGS16SC,
       "hpnicfevtModuleSw-LSU1SUPB0": hpnicfevtModuleSw_LSU1SUPB0,
       "hpnicfevtModuleSw-LSQ1GP48SA0": hpnicfevtModuleSw_LSQ1GP48SA0,
       "hpnicfevtModuleSw-LSQ1TGX2SA0": hpnicfevtModuleSw_LSQ1TGX2SA0,
       "hpnicfevtModuleSw-LSV1SRPUA1": hpnicfevtModuleSw_LSV1SRPUA1,
       "hpnicfevtModuleSw-LSV1QGS12SA1": hpnicfevtModuleSw_LSV1QGS12SA1,
       "hpnicfevtModuleSw-LSV1MPUA1": hpnicfevtModuleSw_LSV1MPUA1,
       "hpnicfevtModuleSw-LSX1SUP10A0": hpnicfevtModuleSw_LSX1SUP10A0,
       "hpnicfevtModuleSw-LSX1SUP16A0": hpnicfevtModuleSw_LSX1SUP16A0,
       "hpnicfevtModuleSw-LSX1SUP10A1": hpnicfevtModuleSw_LSX1SUP10A1,
       "hpnicfevtModuleSw-LSX1SUP16A1": hpnicfevtModuleSw_LSX1SUP16A1,
       "hpnicfevtModuleSw-LSX1FAB10B0": hpnicfevtModuleSw_LSX1FAB10B0,
       "hpnicfevtModuleSw-LSX1FAB16B0": hpnicfevtModuleSw_LSX1FAB16B0,
       "hpnicfevtModuleSw-LSX1FAB10B1": hpnicfevtModuleSw_LSX1FAB10B1,
       "hpnicfevtModuleSw-LSX1FAB16B1": hpnicfevtModuleSw_LSX1FAB16B1,
       "hpnicfevtModuleSw-LSX1QGS16EA0": hpnicfevtModuleSw_LSX1QGS16EA0,
       "hpnicfevtModuleSw-LSX1TGS48EA0": hpnicfevtModuleSw_LSX1TGS48EA0,
       "hpnicfevtModuleSw-LSX1QGS16EA1": hpnicfevtModuleSw_LSX1QGS16EA1,
       "hpnicfevtModuleSw-LSX1TGS48EA1": hpnicfevtModuleSw_LSX1TGS48EA1,
       "hpnicfevtModuleSw-LSU1TGT24SF9": hpnicfevtModuleSw_LSU1TGT24SF9,
       "hpnicfevtModuleSw-LSU1QGS8SF9": hpnicfevtModuleSw_LSU1QGS8SF9,
       "hpnicfevtModuleSw-LSU1QGS4SF9": hpnicfevtModuleSw_LSU1QGS4SF9,
       "hpnicfevtModuleSw-LSU1TGS48SF9": hpnicfevtModuleSw_LSU1TGS48SF9,
       "hpnicfevtModuleSw-LSU1TGS32SF9": hpnicfevtModuleSw_LSU1TGS32SF9,
       "hpnicfevtModuleSw-LSU1FAB08D9": hpnicfevtModuleSw_LSU1FAB08D9,
       "hpnicfevtModuleSw-LSU1SUPB9": hpnicfevtModuleSw_LSU1SUPB9,
       "hpnicfevtModuleSw-LSQ3GV48SC0": hpnicfevtModuleSw_LSQ3GV48SC0,
       "hpnicfevtModuleSw-LSX1QGS12EC1": hpnicfevtModuleSw_LSX1QGS12EC1,
       "hpnicfevtModuleSw-LSX1QGS12EC0": hpnicfevtModuleSw_LSX1QGS12EC0,
       "hpnicfevtModuleSw-LSX1TGS48EC0": hpnicfevtModuleSw_LSX1TGS48EC0,
       "hpnicfevtModuleSw-LSX1TGS48EC1": hpnicfevtModuleSw_LSX1TGS48EC1,
       "hpnicfevtModuleSw-LSX1TGS24EC0": hpnicfevtModuleSw_LSX1TGS24EC0,
       "hpnicfevtModuleSw-LSX1TGS24EC1": hpnicfevtModuleSw_LSX1TGS24EC1,
       "hpnicfevtModuleSw-LSX1FAB10A0": hpnicfevtModuleSw_LSX1FAB10A0,
       "hpnicfevtModuleSw-LSX1FAB16A1": hpnicfevtModuleSw_LSX1FAB16A1,
       "hpnicfevtModuleSw-LSX1QGS12FB0": hpnicfevtModuleSw_LSX1QGS12FB0,
       "hpnicfevtModuleSw-LSX1TGS24FB0": hpnicfevtModuleSw_LSX1TGS24FB0,
       "hpnicfevtModuleSw-LSX1TGS48FB0": hpnicfevtModuleSw_LSX1TGS48FB0,
       "hpnicfevtModuleSw-LSX1QGS12EB1": hpnicfevtModuleSw_LSX1QGS12EB1,
       "hpnicfevtModuleSw-LSX1TGS24EB1": hpnicfevtModuleSw_LSX1TGS24EB1,
       "hpnicfevtModuleSw-LSX1FAB10A1": hpnicfevtModuleSw_LSX1FAB10A1,
       "hpnicfevtModuleSw-LSX1TGS48EB1": hpnicfevtModuleSw_LSX1TGS48EB1,
       "hpnicfevtModuleSw-LSX1GP48EB1": hpnicfevtModuleSw_LSX1GP48EB1,
       "hpnicfevtModuleSw-LSX1GP48FB0": hpnicfevtModuleSw_LSX1GP48FB0,
       "hpnicfevtModuleSw-LSX1GT48FC0": hpnicfevtModuleSw_LSX1GT48FC0,
       "hpnicfevtModuleSw-LSX1GT48FC1": hpnicfevtModuleSw_LSX1GT48FC1,
       "hpnicfevtModuleSw-LSX1GP48FC0": hpnicfevtModuleSw_LSX1GP48FC0,
       "hpnicfevtModuleSw-LSX1GP48FC1": hpnicfevtModuleSw_LSX1GP48FC1,
       "hpnicfevtModuleSw-LSX1QGS12FC0": hpnicfevtModuleSw_LSX1QGS12FC0,
       "hpnicfevtModuleSw-LSX1QGS12FC1": hpnicfevtModuleSw_LSX1QGS12FC1,
       "hpnicfevtModuleSw-LSX2TGS48EA1": hpnicfevtModuleSw_LSX2TGS48EA1,
       "hpnicfevtModuleSw-LSX1CGC4EB1": hpnicfevtModuleSw_LSX1CGC4EB1,
       "hpnicfevtModuleSw-LSX1CGC4EC0": hpnicfevtModuleSw_LSX1CGC4EC0,
       "hpnicfevtModuleSw-LSX1GT48EB1": hpnicfevtModuleSw_LSX1GT48EB1,
       "hpnicfevtModuleSw-LSX1GT48FB0": hpnicfevtModuleSw_LSX1GT48FB0,
       "hpnicfevtModuleSw-LSX1FAB16S1": hpnicfevtModuleSw_LSX1FAB16S1,
       "hpnicfevtModuleSw-LSQ1SUPB3": hpnicfevtModuleSw_LSQ1SUPB3,
       "hpnicfevtModuleSw-LSU1CGC2SE0": hpnicfevtModuleSw_LSU1CGC2SE0,
       "hpnicfevtModuleSw-LSU1TGS16SF0": hpnicfevtModuleSw_LSU1TGS16SF0,
       "hpnicfevtModuleSw-LSU1TGS8SF0": hpnicfevtModuleSw_LSU1TGS8SF0,
       "hpnicfevtModuleSw-LSQ1TGS4SC0": hpnicfevtModuleSw_LSQ1TGS4SC0,
       "hpnicfevtModuleSw-LSU1GT48SE3": hpnicfevtModuleSw_LSU1GT48SE3,
       "hpnicfevtModuleSw-LSU1GP48SE3": hpnicfevtModuleSw_LSU1GP48SE3,
       "hpnicfevtModuleSw-LSX1SUP10B0": hpnicfevtModuleSw_LSX1SUP10B0,
       "hpnicfevtModuleSw-LSX1SUP16B0": hpnicfevtModuleSw_LSX1SUP16B0,
       "hpnicfevtModuleSw-LSX1SUP10B1": hpnicfevtModuleSw_LSX1SUP10B1,
       "hpnicfevtModuleSw-LSX1SUP16B1": hpnicfevtModuleSw_LSX1SUP16B1,
       "hpnicfevtModuleSw-LSQ1CGV24PSC3": hpnicfevtModuleSw_LSQ1CGV24PSC3,
       "hpnicfevtModuleSw-LSQ1SRPA8": hpnicfevtModuleSw_LSQ1SRPA8,
       "hpnicfevtModuleSw-LSQ1CGP24TSC8": hpnicfevtModuleSw_LSQ1CGP24TSC8,
       "hpnicfevtModuleSw-LSQ1CGT24PSC8": hpnicfevtModuleSw_LSQ1CGT24PSC8,
       "hpnicfevtModuleSw-LSQ1GT24PSA8": hpnicfevtModuleSw_LSQ1GT24PSA8,
       "hpnicfevtModuleSw-LSQ1GP24TSA8": hpnicfevtModuleSw_LSQ1GP24TSA8,
       "hpnicfevtModuleSw-LSQ1GT48SA8": hpnicfevtModuleSw_LSQ1GT48SA8,
       "hpnicfevtModuleSw-LSQ1GP48SA8": hpnicfevtModuleSw_LSQ1GP48SA8,
       "hpnicfevtModuleSw-LSQ1TGS4SC8": hpnicfevtModuleSw_LSQ1TGS4SC8,
       "hpnicfevtModuleSw-LSQ1TGS8SC8": hpnicfevtModuleSw_LSQ1TGS8SC8,
       "hpnicfevtModuleSw-LSU1GT24SE3": hpnicfevtModuleSw_LSU1GT24SE3,
       "hpnicfevtModuleSw-LSU1GP12SE3": hpnicfevtModuleSw_LSU1GP12SE3,
       "hpnicfevtModuleSw-LSU1GP24SE3": hpnicfevtModuleSw_LSU1GP24SE3,
       "hpnicfevtModuleSw-LSU1T24XGSE3": hpnicfevtModuleSw_LSU1T24XGSE3,
       "hpnicfevtModuleSw-LSU1P24XGSE3": hpnicfevtModuleSw_LSU1P24XGSE3,
       "hpnicfevtModuleSw-LSU1GP24TSE3": hpnicfevtModuleSw_LSU1GP24TSE3,
       "hpnicfevtModuleSw-LSU1GT40PSE3": hpnicfevtModuleSw_LSU1GT40PSE3,
       "hpnicfevtModuleSw-LSV1TGS24SA1": hpnicfevtModuleSw_LSV1TGS24SA1,
       "hpnicfevtModuleSw-LSV1SRPA1": hpnicfevtModuleSw_LSV1SRPA1,
       "hpnicfevtModuleSw-LSV1SRPC1": hpnicfevtModuleSw_LSV1SRPC1,
       "hpnicfevtModuleSw-LSX1FAB16S0": hpnicfevtModuleSw_LSX1FAB16S0,
       "hpnicfevtModuleSw-LSU1WCME0": hpnicfevtModuleSw_LSU1WCME0,
       "hpnicfevtModuleSw-EWPX1WCME0": hpnicfevtModuleSw_EWPX1WCME0,
       "hpnicfevtModuleSw-LSU1TGS48SG0": hpnicfevtModuleSw_LSU1TGS48SG0,
       "hpnicfevtModuleSw-LSU1QGS12SG0": hpnicfevtModuleSw_LSU1QGS12SG0,
       "hpnicfevtModuleSw-LSU1GP44TSEC0": hpnicfevtModuleSw_LSU1GP44TSEC0,
       "hpnicfevtModuleSw-LSU1TGS24EC0": hpnicfevtModuleSw_LSU1TGS24EC0,
       "hpnicfevtModuleSw-LSU1QGS6EC0": hpnicfevtModuleSw_LSU1QGS6EC0,
       "hpnicfevtModuleSw-LSU1CGC2EC0": hpnicfevtModuleSw_LSU1CGC2EC0,
       "hpnicfevtModuleSw-LSU1CGC2SE9": hpnicfevtModuleSw_LSU1CGC2SE9,
       "hpnicfevtModuleSw-LSXM1QGS24EX1": hpnicfevtModuleSw_LSXM1QGS24EX1,
       "hpnicfevtModuleSw-LSXM1QGS24FB0": hpnicfevtModuleSw_LSXM1QGS24FB0,
       "hpnicfevtModuleSw-LSVM1QGS12FX1": hpnicfevtModuleSw_LSVM1QGS12FX1,
       "hpnicfevtModuleSw-LSVM1TGS24FX1": hpnicfevtModuleSw_LSVM1TGS24FX1,
       "hpnicfevtModuleSw-LSVM1QGS6C2FX1": hpnicfevtModuleSw_LSVM1QGS6C2FX1,
       "hpnicfevtModuleSw-LSQ2GP44TSSC0": hpnicfevtModuleSw_LSQ2GP44TSSC0,
       "hpnicfevtModuleSw-LSQ2GP44TSSC3": hpnicfevtModuleSw_LSQ2GP44TSSC3,
       "hpnicfevtModuleSw-LSQ2GP24TSSC0": hpnicfevtModuleSw_LSQ2GP24TSSC0,
       "hpnicfevtModuleSw-LSQ2GP24TSSC3": hpnicfevtModuleSw_LSQ2GP24TSSC3,
       "hpnicfevtModuleSw-LSQ2GT24PTSSC0": hpnicfevtModuleSw_LSQ2GT24PTSSC0,
       "hpnicfevtModuleSw-LSQ2GT24PTSSC3": hpnicfevtModuleSw_LSQ2GT24PTSSC3,
       "hpnicfevtModuleSw-LSQ2GT24TSSC0": hpnicfevtModuleSw_LSQ2GT24TSSC0,
       "hpnicfevtModuleSw-LSQ2GT24TSSC3": hpnicfevtModuleSw_LSQ2GT24TSSC3,
       "hpnicfevtModuleSw-LSQ2GT48SC0": hpnicfevtModuleSw_LSQ2GT48SC0,
       "hpnicfevtModuleSw-LSQ2GT48SC3": hpnicfevtModuleSw_LSQ2GT48SC3,
       "hpnicfevtModuleSw-LSQ2GV48SC0": hpnicfevtModuleSw_LSQ2GV48SC0,
       "hpnicfevtModuleSw-LSQ2GV48SC3": hpnicfevtModuleSw_LSQ2GV48SC3,
       "hpnicfevtModuleSw-LSQ2TGS16SF0": hpnicfevtModuleSw_LSQ2TGS16SF0,
       "hpnicfevtModuleSw-LSQ2TGS16SF3": hpnicfevtModuleSw_LSQ2TGS16SF3,
       "hpnicfevtModuleSw-LSQ2MPUD0": hpnicfevtModuleSw_LSQ2MPUD0,
       "hpnicfevtModuleSw-LSQ2MPUD3": hpnicfevtModuleSw_LSQ2MPUD3,
       "hpnicfevtModuleSw-LSQ2MPUA0": hpnicfevtModuleSw_LSQ2MPUA0,
       "hpnicfevtModuleSw-LSQ2MPUA3": hpnicfevtModuleSw_LSQ2MPUA3,
       "hpnicfevtModuleSw-LSU2GP44TSSE0": hpnicfevtModuleSw_LSU2GP44TSSE0,
       "hpnicfevtModuleSw-LSU2GP44TSSE3": hpnicfevtModuleSw_LSU2GP44TSSE3,
       "hpnicfevtModuleSw-LSU2GP24TSSE0": hpnicfevtModuleSw_LSU2GP24TSSE0,
       "hpnicfevtModuleSw-LSU2GP24TSSE3": hpnicfevtModuleSw_LSU2GP24TSSE3,
       "hpnicfevtModuleSw-LSU2GT24PTSSE0": hpnicfevtModuleSw_LSU2GT24PTSSE0,
       "hpnicfevtModuleSw-LSU2GT24PTSSE3": hpnicfevtModuleSw_LSU2GT24PTSSE3,
       "hpnicfevtModuleSw-LSU2GT24TSSE0": hpnicfevtModuleSw_LSU2GT24TSSE0,
       "hpnicfevtModuleSw-LSU2GT24TSSE3": hpnicfevtModuleSw_LSU2GT24TSSE3,
       "hpnicfevtModuleSw-LSU2GT48SE0": hpnicfevtModuleSw_LSU2GT48SE0,
       "hpnicfevtModuleSw-LSU2GT48SE3": hpnicfevtModuleSw_LSU2GT48SE3,
       "hpnicfevtModuleSw-LSU2GV48SE0": hpnicfevtModuleSw_LSU2GV48SE0,
       "hpnicfevtModuleSw-LSU2GV48SE3": hpnicfevtModuleSw_LSU2GV48SE3,
       "hpnicfevtModuleSw-LSU2TGS16SF0": hpnicfevtModuleSw_LSU2TGS16SF0,
       "hpnicfevtModuleSw-LSU2TGS16SF3": hpnicfevtModuleSw_LSU2TGS16SF3,
       "hpnicfevtModuleSw-LSU1MPU06B0": hpnicfevtModuleSw_LSU1MPU06B0,
       "hpnicfevtModuleSw-LSU1MPU06B3": hpnicfevtModuleSw_LSU1MPU06B3,
       "hpnicfevtModuleSw-LSU1MPU10C0": hpnicfevtModuleSw_LSU1MPU10C0,
       "hpnicfevtModuleSw-LSU1MPU10C3": hpnicfevtModuleSw_LSU1MPU10C3,
       "hpnicfevtModuleSw-LSU1FAB06C0": hpnicfevtModuleSw_LSU1FAB06C0,
       "hpnicfevtModuleSw-LSU1FAB06C3": hpnicfevtModuleSw_LSU1FAB06C3,
       "hpnicfevtModuleSw-LSU1FAB10C0": hpnicfevtModuleSw_LSU1FAB10C0,
       "hpnicfevtModuleSw-LSU1FAB10C3": hpnicfevtModuleSw_LSU1FAB10C3,
       "hpnicfevtModuleSw-LSXM1SUPA1": hpnicfevtModuleSw_LSXM1SUPA1,
       "hpnicfevtModuleSw-LSXM1SFF16B1": hpnicfevtModuleSw_LSXM1SFF16B1,
       "hpnicfevtModulesw-PEX-Common": hpnicfevtModulesw_PEX_Common,
       "hpnicfevtSubModuleRouter": hpnicfevtSubModuleRouter,
       "hpnicfevtSubModuleSwitch": hpnicfevtSubModuleSwitch,
       "hpnicfevtPort": hpnicfevtPort,
       "hpnicfevtPortUnknownPorts": hpnicfevtPortUnknownPorts,
       "hpnicfevtPortCommonPorts": hpnicfevtPortCommonPorts,
       "hpnicfevtPortRouterType": hpnicfevtPortRouterType,
       "hpnicfevtPortRt-Async": hpnicfevtPortRt_Async,
       "hpnicfevtPortRt-Analogmodem": hpnicfevtPortRt_Analogmodem,
       "hpnicfevtPortRt-Atm": hpnicfevtPortRt_Atm,
       "hpnicfevtPortRt-AtmAdsl": hpnicfevtPortRt_AtmAdsl,
       "hpnicfevtPortRt-AtmShdsl": hpnicfevtPortRt_AtmShdsl,
       "hpnicfevtPortRt-AtmE1": hpnicfevtPortRt_AtmE1,
       "hpnicfevtPortRt-AtmT1": hpnicfevtPortRt_AtmT1,
       "hpnicfevtPortRt-AtmE3": hpnicfevtPortRt_AtmE3,
       "hpnicfevtPortRt-AtmT3": hpnicfevtPortRt_AtmT3,
       "hpnicfevtPortRt-Atm622M": hpnicfevtPortRt_Atm622M,
       "hpnicfevtPortRt-AtmImaE1": hpnicfevtPortRt_AtmImaE1,
       "hpnicfevtPortRt-AtmImaT1": hpnicfevtPortRt_AtmImaT1,
       "hpnicfevtPortRt-Atm25M": hpnicfevtPortRt_Atm25M,
       "hpnicfevtPortRt-Bri": hpnicfevtPortRt_Bri,
       "hpnicfevtPortRt-Console": hpnicfevtPortRt_Console,
       "hpnicfevtPortRt-E1": hpnicfevtPortRt_E1,
       "hpnicfevtPortRt-E3": hpnicfevtPortRt_E3,
       "hpnicfevtPortRt-T1": hpnicfevtPortRt_T1,
       "hpnicfevtPortRt-T3": hpnicfevtPortRt_T3,
       "hpnicfevtPortRt-Cpos": hpnicfevtPortRt_Cpos,
       "hpnicfevtPortRt-Ethernet": hpnicfevtPortRt_Ethernet,
       "hpnicfevtPortRt-Serial": hpnicfevtPortRt_Serial,
       "hpnicfevtPortRt-E1f": hpnicfevtPortRt_E1f,
       "hpnicfevtPortRt-T1f": hpnicfevtPortRt_T1f,
       "hpnicfevtPortRt-Pos": hpnicfevtPortRt_Pos,
       "hpnicfevtPortRt-Ge": hpnicfevtPortRt_Ge,
       "hpnicfevtPortRt-Aux": hpnicfevtPortRt_Aux,
       "hpnicfevtPortRt-VG-Fxs": hpnicfevtPortRt_VG_Fxs,
       "hpnicfevtPortRt-VG-Fxo": hpnicfevtPortRt_VG_Fxo,
       "hpnicfevtPortRt-VG-E1vi": hpnicfevtPortRt_VG_E1vi,
       "hpnicfevtPortRt-VG-T1vi": hpnicfevtPortRt_VG_T1vi,
       "hpnicfevtPortRt-Usb": hpnicfevtPortRt_Usb,
       "hpnicfevtPortRt-Ndec": hpnicfevtPortRt_Ndec,
       "hpnicfevtPortRt-Cavium": hpnicfevtPortRt_Cavium,
       "hpnicfevtPortRt-Fcm": hpnicfevtPortRt_Fcm,
       "hpnicfevtPortRt-E1vi": hpnicfevtPortRt_E1vi,
       "hpnicfevtPortRt-T1vi": hpnicfevtPortRt_T1vi,
       "hpnicfevtPortRt-Vi": hpnicfevtPortRt_Vi,
       "hpnicfevtPortRt-Adls2Plus": hpnicfevtPortRt_Adls2Plus,
       "hpnicfevtPortRt-RADIO-AG": hpnicfevtPortRt_RADIO_AG,
       "hpnicfevtPortRt-1exp": hpnicfevtPortRt_1exp,
       "hpnicfevtPortRt-G-SHDSL-BIS": hpnicfevtPortRt_G_SHDSL_BIS,
       "hpnicfevtPortRt-ONU-1000BASE-BX-SFF-SC": hpnicfevtPortRt_ONU_1000BASE_BX_SFF_SC,
       "hpnicfevtPortRt-CELLULAR": hpnicfevtPortRt_CELLULAR,
       "hpnicfevtPortRt-CELLULAR-ETHERNET": hpnicfevtPortRt_CELLULAR_ETHERNET,
       "hpnicfevtPortRt-VGe": hpnicfevtPortRt_VGe,
       "hpnicfevtPortRt-VXGe": hpnicfevtPortRt_VXGe,
       "hpnicfevtPortRt-Xpos": hpnicfevtPortRt_Xpos,
       "hpnicfevtPortRt-Fge": hpnicfevtPortRt_Fge,
       "hpnicfevtPortSwitchType": hpnicfevtPortSwitchType,
       "hpnicfevtPortSw-10or100M": hpnicfevtPortSw_10or100M,
       "hpnicfevtPortSw-1000BaseLxSm": hpnicfevtPortSw_1000BaseLxSm,
       "hpnicfevtPortSw-1000BaseSxMm": hpnicfevtPortSw_1000BaseSxMm,
       "hpnicfevtPortSw-1000BaseTx": hpnicfevtPortSw_1000BaseTx,
       "hpnicfevtPortSw-100MSinglemodeFx": hpnicfevtPortSw_100MSinglemodeFx,
       "hpnicfevtPortSw-100MMultimodeFx": hpnicfevtPortSw_100MMultimodeFx,
       "hpnicfevtPortSw-100M100BaseTx": hpnicfevtPortSw_100M100BaseTx,
       "hpnicfevtPortSw-100MHub": hpnicfevtPortSw_100MHub,
       "hpnicfevtPortSw-Vdsl": hpnicfevtPortSw_Vdsl,
       "hpnicfevtPortSw-Stack": hpnicfevtPortSw_Stack,
       "hpnicfevtPortSw-1000BaseZenithFx": hpnicfevtPortSw_1000BaseZenithFx,
       "hpnicfevtPortSw-1000BaseLongFx": hpnicfevtPortSw_1000BaseLongFx,
       "hpnicfevtPortSw-Adsl": hpnicfevtPortSw_Adsl,
       "hpnicfevtPortSw-10or100MDb": hpnicfevtPortSw_10or100MDb,
       "hpnicfevtPortSw-10GBaseLrSm": hpnicfevtPortSw_10GBaseLrSm,
       "hpnicfevtPortSw-10GBaseLx4Mm": hpnicfevtPortSw_10GBaseLx4Mm,
       "hpnicfevtPortSw-10GBaseLx4Sm": hpnicfevtPortSw_10GBaseLx4Sm,
       "hpnicfevtPortSw-100MLongFx": hpnicfevtPortSw_100MLongFx,
       "hpnicfevtPortSw-1000BaseCx": hpnicfevtPortSw_1000BaseCx,
       "hpnicfevtPortSw-1000BaseZenithFxLc": hpnicfevtPortSw_1000BaseZenithFxLc,
       "hpnicfevtPortSw-1000BaseLongFxLc": hpnicfevtPortSw_1000BaseLongFxLc,
       "hpnicfevtPortSw-100MSmFxSc": hpnicfevtPortSw_100MSmFxSc,
       "hpnicfevtPortSw-100MMmFxSc": hpnicfevtPortSw_100MMmFxSc,
       "hpnicfevtPortSw-100MSmFxLc": hpnicfevtPortSw_100MSmFxLc,
       "hpnicfevtPortSw-100MMmFxLc": hpnicfevtPortSw_100MMmFxLc,
       "hpnicfevtPortSw-GbicNoConnector": hpnicfevtPortSw_GbicNoConnector,
       "hpnicfevtPortSw-Gbic1000BaseT": hpnicfevtPortSw_Gbic1000BaseT,
       "hpnicfevtPortSw-Gbic1000BaseLx": hpnicfevtPortSw_Gbic1000BaseLx,
       "hpnicfevtPortSw-Gbic1000BaseSx": hpnicfevtPortSw_Gbic1000BaseSx,
       "hpnicfevtPortSw-Gbic1000BaseZx": hpnicfevtPortSw_Gbic1000BaseZx,
       "hpnicfevtPortSw-ComboNoConnector": hpnicfevtPortSw_ComboNoConnector,
       "hpnicfevtPortSw-Combo1000BaseLx": hpnicfevtPortSw_Combo1000BaseLx,
       "hpnicfevtPortSw-Combo1000BaseLxFiber": hpnicfevtPortSw_Combo1000BaseLxFiber,
       "hpnicfevtPortSw-Combo1000BaseLxCopper": hpnicfevtPortSw_Combo1000BaseLxCopper,
       "hpnicfevtPortSw-Combo1000BaseSx": hpnicfevtPortSw_Combo1000BaseSx,
       "hpnicfevtPortSw-Combo1000BaseSxFiber": hpnicfevtPortSw_Combo1000BaseSxFiber,
       "hpnicfevtPortSw-Combo1000BaseSxCopper": hpnicfevtPortSw_Combo1000BaseSxCopper,
       "hpnicfevtPortSw-Combo1000BaseZx": hpnicfevtPortSw_Combo1000BaseZx,
       "hpnicfevtPortSw-Combo1000BaseZxFiber": hpnicfevtPortSw_Combo1000BaseZxFiber,
       "hpnicfevtPortSw-Combo1000BaseZxCopper": hpnicfevtPortSw_Combo1000BaseZxCopper,
       "hpnicfevtPortSw-155PosSxMmf": hpnicfevtPortSw_155PosSxMmf,
       "hpnicfevtPortSw-155PosLxSmf": hpnicfevtPortSw_155PosLxSmf,
       "hpnicfevtPortSw-1000BASE-T": hpnicfevtPortSw_1000BASE_T,
       "hpnicfevtPortSw-1000BASE-SX-SFP": hpnicfevtPortSw_1000BASE_SX_SFP,
       "hpnicfevtPortSw-1000BASE-LX-SFP": hpnicfevtPortSw_1000BASE_LX_SFP,
       "hpnicfevtPortSw-1000BASE-T-AN-SFP": hpnicfevtPortSw_1000BASE_T_AN_SFP,
       "hpnicfevtPortSw-10GBASE-LX4-XENPAK": hpnicfevtPortSw_10GBASE_LX4_XENPAK,
       "hpnicfevtPortSw-10GBASE-LR-XENPAK": hpnicfevtPortSw_10GBASE_LR_XENPAK,
       "hpnicfevtPortSw-10GBASE-CX4": hpnicfevtPortSw_10GBASE_CX4,
       "hpnicfevtPortSw-1000BASE-ZX-SFP": hpnicfevtPortSw_1000BASE_ZX_SFP,
       "hpnicfevtPortSw-1000BASE-MM-SFP": hpnicfevtPortSw_1000BASE_MM_SFP,
       "hpnicfevtPortSw-100BASE-SX-SFP": hpnicfevtPortSw_100BASE_SX_SFP,
       "hpnicfevtPortSw-100BASE-LX-SFP": hpnicfevtPortSw_100BASE_LX_SFP,
       "hpnicfevtPortSw-100BASE-T-AN-SFP": hpnicfevtPortSw_100BASE_T_AN_SFP,
       "hpnicfevtPortSw-100BASE-ZX-SFP": hpnicfevtPortSw_100BASE_ZX_SFP,
       "hpnicfevtPortSw-100BASE-MM-SFP": hpnicfevtPortSw_100BASE_MM_SFP,
       "hpnicfevtPortSw-SFP-NO-CONNECTOR": hpnicfevtPortSw_SFP_NO_CONNECTOR,
       "hpnicfevtPortSw-SFP-UNKNOWN-CONNECTOR": hpnicfevtPortSw_SFP_UNKNOWN_CONNECTOR,
       "hpnicfevtPortSw-POS-NO-CONNECTOR": hpnicfevtPortSw_POS_NO_CONNECTOR,
       "hpnicfevtPortSw-10G-BASE-SR": hpnicfevtPortSw_10G_BASE_SR,
       "hpnicfevtPortSw-10G-BASE-ER": hpnicfevtPortSw_10G_BASE_ER,
       "hpnicfevtPortSw-10G-BASE-LX4": hpnicfevtPortSw_10G_BASE_LX4,
       "hpnicfevtPortSw-10G-BASE-SW": hpnicfevtPortSw_10G_BASE_SW,
       "hpnicfevtPortSw-10G-BASE-LW": hpnicfevtPortSw_10G_BASE_LW,
       "hpnicfevtPortSw-10G-BASE-EW": hpnicfevtPortSw_10G_BASE_EW,
       "hpnicfevtPortSw-10G-LR-SM-LC": hpnicfevtPortSw_10G_LR_SM_LC,
       "hpnicfevtPortSw-10G-SR-MM-LC": hpnicfevtPortSw_10G_SR_MM_LC,
       "hpnicfevtPortSw-10G-ER-SM-LC": hpnicfevtPortSw_10G_ER_SM_LC,
       "hpnicfevtPortSw-10G-LW-SM-LC": hpnicfevtPortSw_10G_LW_SM_LC,
       "hpnicfevtPortSw-10G-SW-MM-LC": hpnicfevtPortSw_10G_SW_MM_LC,
       "hpnicfevtPortSw-10G-EW-SM-LC": hpnicfevtPortSw_10G_EW_SM_LC,
       "hpnicfevtPortSw-100BASE-SM-MTRJ": hpnicfevtPortSw_100BASE_SM_MTRJ,
       "hpnicfevtPortSw-100BASE-MM-MTRJ": hpnicfevtPortSw_100BASE_MM_MTRJ,
       "hpnicfevtPortSw-XFP-NO-CONNECTOR": hpnicfevtPortSw_XFP_NO_CONNECTOR,
       "hpnicfevtPortSw-XFP-10GBASE-SR": hpnicfevtPortSw_XFP_10GBASE_SR,
       "hpnicfevtPortSw-XFP-10GBASE-LR": hpnicfevtPortSw_XFP_10GBASE_LR,
       "hpnicfevtPortSw-XFP-10GBASE-ER": hpnicfevtPortSw_XFP_10GBASE_ER,
       "hpnicfevtPortSw-XFP-10GBASE-SW": hpnicfevtPortSw_XFP_10GBASE_SW,
       "hpnicfevtPortSw-XFP-10GBASE-LW": hpnicfevtPortSw_XFP_10GBASE_LW,
       "hpnicfevtPortSw-XFP-10GBASE-EW": hpnicfevtPortSw_XFP_10GBASE_EW,
       "hpnicfevtPortSw-XFP-10GBASE-CX4": hpnicfevtPortSw_XFP_10GBASE_CX4,
       "hpnicfevtPortSw-XFP-10GBASE-LX4": hpnicfevtPortSw_XFP_10GBASE_LX4,
       "hpnicfevtPortSw-XFP-UNKNOWN": hpnicfevtPortSw_XFP_UNKNOWN,
       "hpnicfevtPortSw-XPK-NOCONNECTOR": hpnicfevtPortSw_XPK_NOCONNECTOR,
       "hpnicfevtPortSw-XPK-10GBASE-SR": hpnicfevtPortSw_XPK_10GBASE_SR,
       "hpnicfevtPortSw-XPK-10GBASE-LR": hpnicfevtPortSw_XPK_10GBASE_LR,
       "hpnicfevtPortSw-XPK-10GBASE-ER": hpnicfevtPortSw_XPK_10GBASE_ER,
       "hpnicfevtPortSw-XPK-10GBASE-SW": hpnicfevtPortSw_XPK_10GBASE_SW,
       "hpnicfevtPortSw-XPK-10GBASE-LW": hpnicfevtPortSw_XPK_10GBASE_LW,
       "hpnicfevtPortSw-XPK-10GBASE-EW": hpnicfevtPortSw_XPK_10GBASE_EW,
       "hpnicfevtPortSw-XPK-10GBASE-CX4": hpnicfevtPortSw_XPK_10GBASE_CX4,
       "hpnicfevtPortSw-XPK-10GBASE-LX4": hpnicfevtPortSw_XPK_10GBASE_LX4,
       "hpnicfevtPortSw-XPK-UNKNOWN": hpnicfevtPortSw_XPK_UNKNOWN,
       "hpnicfevtPortSw-POS-OC48-SR-SM-LC": hpnicfevtPortSw_POS_OC48_SR_SM_LC,
       "hpnicfevtPortSw-POS-OC48-IR-SM-LC": hpnicfevtPortSw_POS_OC48_IR_SM_LC,
       "hpnicfevtPortSw-POS-OC48-LR-SM-LC": hpnicfevtPortSw_POS_OC48_LR_SM_LC,
       "hpnicfevtPortSw-10G-BASE-CX4": hpnicfevtPortSw_10G_BASE_CX4,
       "hpnicfevtPortSw-OLT-1000BASE-BX-SFF-SC": hpnicfevtPortSw_OLT_1000BASE_BX_SFF_SC,
       "hpnicfevtPortSw-ONU-1000BASE-BX-SFF-SC": hpnicfevtPortSw_ONU_1000BASE_BX_SFF_SC,
       "hpnicfevtPortSw-24G-CASCADE": hpnicfevtPortSw_24G_CASCADE,
       "hpnicfevtPortSw-POS-OC3-SR-MM": hpnicfevtPortSw_POS_OC3_SR_MM,
       "hpnicfevtPortSw-POS-OC3-IR-SM": hpnicfevtPortSw_POS_OC3_IR_SM,
       "hpnicfevtPortSw-POS-OC3-IR-1-SM": hpnicfevtPortSw_POS_OC3_IR_1_SM,
       "hpnicfevtPortSw-POS-OC3-IR-2-SM": hpnicfevtPortSw_POS_OC3_IR_2_SM,
       "hpnicfevtPortSw-POS-OC3-LR-SM": hpnicfevtPortSw_POS_OC3_LR_SM,
       "hpnicfevtPortSw-POS-OC3-LR-1-SM": hpnicfevtPortSw_POS_OC3_LR_1_SM,
       "hpnicfevtPortSw-POS-OC3-LR-2-SM": hpnicfevtPortSw_POS_OC3_LR_2_SM,
       "hpnicfevtPortSw-POS-OC3-LR-3-SM": hpnicfevtPortSw_POS_OC3_LR_3_SM,
       "hpnicfevtPortSw-POS-OC12-SR-MM": hpnicfevtPortSw_POS_OC12_SR_MM,
       "hpnicfevtPortSw-POS-OC12-IR-SM": hpnicfevtPortSw_POS_OC12_IR_SM,
       "hpnicfevtPortSw-POS-OC12-IR-1-SM": hpnicfevtPortSw_POS_OC12_IR_1_SM,
       "hpnicfevtPortSw-POS-OC12-IR-2-SM": hpnicfevtPortSw_POS_OC12_IR_2_SM,
       "hpnicfevtPortSw-POS-OC12-LR-SM": hpnicfevtPortSw_POS_OC12_LR_SM,
       "hpnicfevtPortSw-POS-OC12-LR-1-SM": hpnicfevtPortSw_POS_OC12_LR_1_SM,
       "hpnicfevtPortSw-POS-OC12-LR-2-SM": hpnicfevtPortSw_POS_OC12_LR_2_SM,
       "hpnicfevtPortSw-POS-OC12-LR-3-SM": hpnicfevtPortSw_POS_OC12_LR_3_SM,
       "hpnicfevtPortSw-POS-OC48-SR-SM": hpnicfevtPortSw_POS_OC48_SR_SM,
       "hpnicfevtPortSw-POS-OC48-IR-SM": hpnicfevtPortSw_POS_OC48_IR_SM,
       "hpnicfevtPortSw-POS-OC48-IR-1-SM": hpnicfevtPortSw_POS_OC48_IR_1_SM,
       "hpnicfevtPortSw-POS-OC48-IR-2-SM": hpnicfevtPortSw_POS_OC48_IR_2_SM,
       "hpnicfevtPortSw-POS-OC48-LR-SM": hpnicfevtPortSw_POS_OC48_LR_SM,
       "hpnicfevtPortSw-POS-OC48-LR-1-SM": hpnicfevtPortSw_POS_OC48_LR_1_SM,
       "hpnicfevtPortSw-POS-OC48-LR-2-SM": hpnicfevtPortSw_POS_OC48_LR_2_SM,
       "hpnicfevtPortSw-POS-OC48-LR-3-SM": hpnicfevtPortSw_POS_OC48_LR_3_SM,
       "hpnicfevtPortSw-POS-I-64-1": hpnicfevtPortSw_POS_I_64_1,
       "hpnicfevtPortSw-POS-I-64-2": hpnicfevtPortSw_POS_I_64_2,
       "hpnicfevtPortSw-POS-I-64-3": hpnicfevtPortSw_POS_I_64_3,
       "hpnicfevtPortSw-POS-I-64-5": hpnicfevtPortSw_POS_I_64_5,
       "hpnicfevtPortSw-POS-S-64-1": hpnicfevtPortSw_POS_S_64_1,
       "hpnicfevtPortSw-POS-S-64-2": hpnicfevtPortSw_POS_S_64_2,
       "hpnicfevtPortSw-POS-S-64-3": hpnicfevtPortSw_POS_S_64_3,
       "hpnicfevtPortSw-POS-S-64-5": hpnicfevtPortSw_POS_S_64_5,
       "hpnicfevtPortSw-POS-L-64-1": hpnicfevtPortSw_POS_L_64_1,
       "hpnicfevtPortSw-POS-L-64-2": hpnicfevtPortSw_POS_L_64_2,
       "hpnicfevtPortSw-POS-L-64-3": hpnicfevtPortSw_POS_L_64_3,
       "hpnicfevtPortSw-POS-V-64-2": hpnicfevtPortSw_POS_V_64_2,
       "hpnicfevtPortSw-POS-V-64-3": hpnicfevtPortSw_POS_V_64_3,
       "hpnicfevtPortSw-100BASE-FX-BIDI": hpnicfevtPortSw_100BASE_FX_BIDI,
       "hpnicfevtPortSw-100BASE-BX10-U-SFP": hpnicfevtPortSw_100BASE_BX10_U_SFP,
       "hpnicfevtPortSw-100BASE-BX10-D-SFP": hpnicfevtPortSw_100BASE_BX10_D_SFP,
       "hpnicfevtPortSw-1000BASE-BX10-U-SFP": hpnicfevtPortSw_1000BASE_BX10_U_SFP,
       "hpnicfevtPortSw-1000BASE-BX10-D-SFP": hpnicfevtPortSw_1000BASE_BX10_D_SFP,
       "hpnicfevtPortSw-STK-1000BASE-T": hpnicfevtPortSw_STK_1000BASE_T,
       "hpnicfevtPortSw-RPR-PHYPOS-CONNECTOR": hpnicfevtPortSw_RPR_PHYPOS_CONNECTOR,
       "hpnicfevtPortSw-RPR-PHY10GE-CONNECTOR": hpnicfevtPortSw_RPR_PHY10GE_CONNECTOR,
       "hpnicfevtPortSw-RPR-LOGICPOS-CONNECTOR": hpnicfevtPortSw_RPR_LOGICPOS_CONNECTOR,
       "hpnicfevtPortSw-RPR-LOGIC10GE-CONNECTOR": hpnicfevtPortSw_RPR_LOGIC10GE_CONNECTOR,
       "hpnicfevtPortSw-10GBASE-ZR": hpnicfevtPortSw_10GBASE_ZR,
       "hpnicfevtPortSw-TYPE-ERROR-CONNECTOR": hpnicfevtPortSw_TYPE_ERROR_CONNECTOR,
       "hpnicfevtPortSw-10G-STACK": hpnicfevtPortSw_10G_STACK,
       "hpnicfevtPortSw-155-ATM-SX-MMF": hpnicfevtPortSw_155_ATM_SX_MMF,
       "hpnicfevtPortSw-155-ATM-LX-SMF": hpnicfevtPortSw_155_ATM_LX_SMF,
       "hpnicfevtPortSw-622-ATM-SX-MMF": hpnicfevtPortSw_622_ATM_SX_MMF,
       "hpnicfevtPortSw-622-ATM-LX-SMF": hpnicfevtPortSw_622_ATM_LX_SMF,
       "hpnicfevtPortSw-155-ATM-NO-CONNECTOR": hpnicfevtPortSw_155_ATM_NO_CONNECTOR,
       "hpnicfevtPortSw-622-ATM-NO-CONNECTOR": hpnicfevtPortSw_622_ATM_NO_CONNECTOR,
       "hpnicfevtPortSw-155-CPOS-E1-NO-CONNECTOR": hpnicfevtPortSw_155_CPOS_E1_NO_CONNECTOR,
       "hpnicfevtPortSw-155-CPOS-T1-NO-CONNECTOR": hpnicfevtPortSw_155_CPOS_T1_NO_CONNECTOR,
       "hpnicfevtPortSw-622-CPOS-E1-NO-CONNECTOR": hpnicfevtPortSw_622_CPOS_E1_NO_CONNECTOR,
       "hpnicfevtPortSw-622-CPOS-T1-NO-CONNECTOR": hpnicfevtPortSw_622_CPOS_T1_NO_CONNECTOR,
       "hpnicfevtPortSw-155-CPOS-E1-SX-MMF": hpnicfevtPortSw_155_CPOS_E1_SX_MMF,
       "hpnicfevtPortSw-155-CPOS-T1-SX-MMF": hpnicfevtPortSw_155_CPOS_T1_SX_MMF,
       "hpnicfevtPortSw-155-CPOS-E1-LX-SMF": hpnicfevtPortSw_155_CPOS_E1_LX_SMF,
       "hpnicfevtPortSw-155-CPOS-T1-LX-SMF": hpnicfevtPortSw_155_CPOS_T1_LX_SMF,
       "hpnicfevtPortSw-622-CPOS-E1-SX-MMF": hpnicfevtPortSw_622_CPOS_E1_SX_MMF,
       "hpnicfevtPortSw-622-CPOS-T1-SX-MMF": hpnicfevtPortSw_622_CPOS_T1_SX_MMF,
       "hpnicfevtPortSw-622-CPOS-E1-LX-SMF": hpnicfevtPortSw_622_CPOS_E1_LX_SMF,
       "hpnicfevtPortSw-622-CPOS-T1-LX-SMF": hpnicfevtPortSw_622_CPOS_T1_LX_SMF,
       "hpnicfevtPortSw-E1-CONNECTOR": hpnicfevtPortSw_E1_CONNECTOR,
       "hpnicfevtPortSw-T1-CONNECTOR": hpnicfevtPortSw_T1_CONNECTOR,
       "hpnicfevtPortSw-1000BASE-STK-SFP": hpnicfevtPortSw_1000BASE_STK_SFP,
       "hpnicfevtPortSw-1000BASE-BIDI-SFP": hpnicfevtPortSw_1000BASE_BIDI_SFP,
       "hpnicfevtPortSw-1000BASE-CWDM-SFP": hpnicfevtPortSw_1000BASE_CWDM_SFP,
       "hpnicfevtPortSw-100BASE-BIDI-SFP": hpnicfevtPortSw_100BASE_BIDI_SFP,
       "hpnicfevtPortSw-OLT-1000BASE-PX-SFP": hpnicfevtPortSw_OLT_1000BASE_PX_SFP,
       "hpnicfevtPortSw-OLT-1000BASE-NO-CONNECTOR": hpnicfevtPortSw_OLT_1000BASE_NO_CONNECTOR,
       "hpnicfevtPortSw-RPR-PHYGE-CONNECTOR": hpnicfevtPortSw_RPR_PHYGE_CONNECTOR,
       "hpnicfevtPortSw-RPR-LOGICGE-CONNECTOR": hpnicfevtPortSw_RPR_LOGICGE_CONNECTOR,
       "hpnicfevtPortSw-100M-1550-BIDI": hpnicfevtPortSw_100M_1550_BIDI,
       "hpnicfevtPortSw-100M-1310-BIDI": hpnicfevtPortSw_100M_1310_BIDI,
       "hpnicfevtPortSw-RPR-PHYOC48-CONNECTOR": hpnicfevtPortSw_RPR_PHYOC48_CONNECTOR,
       "hpnicfevtPortSw-RPR-LOGICOC48-CONNECTOR": hpnicfevtPortSw_RPR_LOGICOC48_CONNECTOR,
       "hpnicfevtPortSw-100-1000-BASE-LX-SMF": hpnicfevtPortSw_100_1000_BASE_LX_SMF,
       "hpnicfevtPortSw-10G-ZW-SM-LC": hpnicfevtPortSw_10G_ZW_SM_LC,
       "hpnicfevtPortSw-10G-ZR-SM-LC": hpnicfevtPortSw_10G_ZR_SM_LC,
       "hpnicfevtPortSw-XPK-10GBASE-ZR": hpnicfevtPortSw_XPK_10GBASE_ZR,
       "hpnicfevtPortSw-SGMII-100-BASE-LX-SFP": hpnicfevtPortSw_SGMII_100_BASE_LX_SFP,
       "hpnicfevtPortSw-SGMII-100-BASE-FX-SFP": hpnicfevtPortSw_SGMII_100_BASE_FX_SFP,
       "hpnicfevtPortSw-WLAN-RADIO": hpnicfevtPortSw_WLAN_RADIO,
       "hpnicfevtPortSw-CABLE": hpnicfevtPortSw_CABLE,
       "hpnicfevtPortSw-SFP-PLUS-NO-CONNECTOR": hpnicfevtPortSw_SFP_PLUS_NO_CONNECTOR,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-SR": hpnicfevtPortSw_SFP_PLUS_10GBASE_SR,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-LR": hpnicfevtPortSw_SFP_PLUS_10GBASE_LR,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-LRM": hpnicfevtPortSw_SFP_PLUS_10GBASE_LRM,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-Cu": hpnicfevtPortSw_SFP_PLUS_10GBASE_Cu,
       "hpnicfevtPortSw-SFP-PLUS-UNKNOWN": hpnicfevtPortSw_SFP_PLUS_UNKNOWN,
       "hpnicfevtPortSw-SFP-PLUS-STACK-CONNECTOR": hpnicfevtPortSw_SFP_PLUS_STACK_CONNECTOR,
       "hpnicfevtPortSw-POS-L-64-4": hpnicfevtPortSw_POS_L_64_4,
       "hpnicfevtPortSw-MINISAS-HD-STACK-CONNECTOR": hpnicfevtPortSw_MINISAS_HD_STACK_CONNECTOR,
       "hpnicfevtPortSw-ONU-1000BASE-PX-SFF": hpnicfevtPortSw_ONU_1000BASE_PX_SFF,
       "hpnicfevtPortSw-RS485": hpnicfevtPortSw_RS485,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-ER": hpnicfevtPortSw_SFP_PLUS_10GBASE_ER,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-ZR": hpnicfevtPortSw_SFP_PLUS_10GBASE_ZR,
       "hpnicfevtPortSw-XFP-10GBASE-ZR": hpnicfevtPortSw_XFP_10GBASE_ZR,
       "hpnicfevtPortSw-QSFP-PLUS-40GBASE-SR4": hpnicfevtPortSw_QSFP_PLUS_40GBASE_SR4,
       "hpnicfevtPortSw-QSFP-PLUS-STACK-CONNECTOR": hpnicfevtPortSw_QSFP_PLUS_STACK_CONNECTOR,
       "hpnicfevtPortSw-QSFP-PLUS-TO-4SFP-PLUS-STACK-CONNECTOR": hpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR,
       "hpnicfevtPortSw-SFP-STACK-CONNECTOR": hpnicfevtPortSw_SFP_STACK_CONNECTOR,
       "hpnicfevtPortSw-QSFP-NO-CONNECTOR": hpnicfevtPortSw_QSFP_NO_CONNECTOR,
       "hpnicfevtPortSw-10GBase-T": hpnicfevtPortSw_10GBase_T,
       "hpnicfevtPortSw-CFP-NO-CONNECTOR": hpnicfevtPortSw_CFP_NO_CONNECTOR,
       "hpnicfevtPortSw-CFP-40GBASE-LR4": hpnicfevtPortSw_CFP_40GBASE_LR4,
       "hpnicfevtPortSw-QSFP-PLUS-NO-CONNECTOR": hpnicfevtPortSw_QSFP_PLUS_NO_CONNECTOR,
       "hpnicfevtPortSw-QSFP-PLUS-40GBASE-LR4": hpnicfevtPortSw_QSFP_PLUS_40GBASE_LR4,
       "hpnicfevtPortSw-CFP-40GBASE-SR4": hpnicfevtPortSw_CFP_40GBASE_SR4,
       "hpnicfevtPortSw-CFP-100GBASE-LR4": hpnicfevtPortSw_CFP_100GBASE_LR4,
       "hpnicfevtPortSw-CFP-100GBASE-SR10": hpnicfevtPortSw_CFP_100GBASE_SR10,
       "hpnicfevtPortSw-CXP-100GBASE-SR10": hpnicfevtPortSw_CXP_100GBASE_SR10,
       "hpnicfevtPortSw-CXP-NO-CONNECTOR": hpnicfevtPortSw_CXP_NO_CONNECTOR,
       "hpnicfevtPortSw-TRANSCEIVER-UNKNOWN": hpnicfevtPortSw_TRANSCEIVER_UNKNOWN,
       "hpnicfevtPortSw-QSFP-PLUS-UNKNOWN": hpnicfevtPortSw_QSFP_PLUS_UNKNOWN,
       "hpnicfevtPortSw-CFP-UNKNOWN": hpnicfevtPortSw_CFP_UNKNOWN,
       "hpnicfevtPortSw-QSFP-PLUS-40GBASE-CSR4": hpnicfevtPortSw_QSFP_PLUS_40GBASE_CSR4,
       "hpnicfevtPortSw-CFP-40GBASE-ER4": hpnicfevtPortSw_CFP_40GBASE_ER4,
       "hpnicfevtPortSw-SFP-1000BASE-BIDI": hpnicfevtPortSw_SFP_1000BASE_BIDI,
       "hpnicfevtPortSw-SFP-PLUS-10GBASE-ZR-DWDM": hpnicfevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM,
       "hpnicfevtPortSw-QSFP-PLUS-40GBASE-PSM": hpnicfevtPortSw_QSFP_PLUS_40GBASE_PSM,
       "hpnicfevtPortSw-SFP-8GFC-SW": hpnicfevtPortSw_SFP_8GFC_SW,
       "hpnicfevtPortSw-SFP-8GFC-LW": hpnicfevtPortSw_SFP_8GFC_LW,
       "hpnicfevtPortSw-CXP-100GBASE-AOC": hpnicfevtPortSw_CXP_100GBASE_AOC,
       "hpnicfevtPortSw-QSFP-PLUS-ACTIVE-STACK-CONNECTOR": hpnicfevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR,
       "hpnicfevtPortSw-QSFP-PLUS-TO-4SFP-PLUS-ACTIVE-STACK-CONNECTOR": hpnicfevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR,
       "hpnicfevtStack": hpnicfevtStack}
)
