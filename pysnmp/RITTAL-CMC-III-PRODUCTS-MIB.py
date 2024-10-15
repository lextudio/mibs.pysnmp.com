# SNMP MIB module (RITTAL-CMC-III-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RITTAL-CMC-III-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:39 2024
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

(cmcIII,) = mibBuilder.importSymbols(
    "RITTAL-CMC-III-MIB",
    "cmcIII")

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

cmcIIIProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7)
)
cmcIIIProducts.setRevisions(
        ("2015-08-25 00:00",
         "2015-08-17 00:00",
         "2015-01-23 00:00",
         "2013-08-12 00:00",
         "2013-06-14 00:00",
         "2011-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmcIIIProductUnit_ObjectIdentity = ObjectIdentity
cmcIIIProductUnit = _CmcIIIProductUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1)
)
_CmcIIIProductUnitUnknown_ObjectIdentity = ObjectIdentity
cmcIIIProductUnitUnknown = _CmcIIIProductUnitUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1, 1)
)
_CmcIIIProductUnitPUIII_ObjectIdentity = ObjectIdentity
cmcIIIProductUnitPUIII = _CmcIIIProductUnitPUIII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1, 2)
)
_CmcIIIProductUnitCompact_ObjectIdentity = ObjectIdentity
cmcIIIProductUnitCompact = _CmcIIIProductUnitCompact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1, 3)
)
_CmcIIIProductUnitLCP_ObjectIdentity = ObjectIdentity
cmcIIIProductUnitLCP = _CmcIIIProductUnitLCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1, 4)
)
_CmcIIIProductUnitPDU_ObjectIdentity = ObjectIdentity
cmcIIIProductUnitPDU = _CmcIIIProductUnitPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1, 5)
)
_CmcIIIProductUnitRMS_ObjectIdentity = ObjectIdentity
cmcIIIProductUnitRMS = _CmcIIIProductUnitRMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 1, 6)
)
_CmcIIIProductPort_ObjectIdentity = ObjectIdentity
cmcIIIProductPort = _CmcIIIProductPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2)
)
_CmcIIIProductPortUnknown_ObjectIdentity = ObjectIdentity
cmcIIIProductPortUnknown = _CmcIIIProductPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 1)
)
_CmcIIIProductPortLoopback_ObjectIdentity = ObjectIdentity
cmcIIIProductPortLoopback = _CmcIIIProductPortLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 2)
)
_CmcIIIProductPortCanBus_ObjectIdentity = ObjectIdentity
cmcIIIProductPortCanBus = _CmcIIIProductPortCanBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 3)
)
_CmcIIIProductPortEthernet_ObjectIdentity = ObjectIdentity
cmcIIIProductPortEthernet = _CmcIIIProductPortEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 4)
)
_CmcIIIProductPortVirtualCanBus_ObjectIdentity = ObjectIdentity
cmcIIIProductPortVirtualCanBus = _CmcIIIProductPortVirtualCanBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 5)
)
_CmcIIIProductPortTunnel_ObjectIdentity = ObjectIdentity
cmcIIIProductPortTunnel = _CmcIIIProductPortTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 6)
)
_CmcIIIProductPortSit_ObjectIdentity = ObjectIdentity
cmcIIIProductPortSit = _CmcIIIProductPortSit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 2, 7)
)
_CmcIIIProductPowerSupply_ObjectIdentity = ObjectIdentity
cmcIIIProductPowerSupply = _CmcIIIProductPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 3)
)
_CmcIIIProductPowerSupplyUnknown_ObjectIdentity = ObjectIdentity
cmcIIIProductPowerSupplyUnknown = _CmcIIIProductPowerSupplyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 3, 1)
)
_CmcIIIProductPowerSupplyAcAdapter_ObjectIdentity = ObjectIdentity
cmcIIIProductPowerSupplyAcAdapter = _CmcIIIProductPowerSupplyAcAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 3, 2)
)
_CmcIIIProductPowerSupplyTerminalStrip_ObjectIdentity = ObjectIdentity
cmcIIIProductPowerSupplyTerminalStrip = _CmcIIIProductPowerSupplyTerminalStrip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 3, 3)
)
_CmcIIIProductPowerSupplyPOE_ObjectIdentity = ObjectIdentity
cmcIIIProductPowerSupplyPOE = _CmcIIIProductPowerSupplyPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 3, 4)
)
_CmcIIIProductPowerSupplyUSB_ObjectIdentity = ObjectIdentity
cmcIIIProductPowerSupplyUSB = _CmcIIIProductPowerSupplyUSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 3, 5)
)
_CmcIIIProductChassis_ObjectIdentity = ObjectIdentity
cmcIIIProductChassis = _CmcIIIProductChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4)
)
_CmcIIIProductChassisGateSensorUnknown_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorUnknown = _CmcIIIProductChassisGateSensorUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 256)
)
_CmcIIIProductChassisGateSensorAccess_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorAccess = _CmcIIIProductChassisGateSensorAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 273)
)
_CmcIIIProductChassisGateSensorMotion_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorMotion = _CmcIIIProductChassisGateSensorMotion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 277)
)
_CmcIIIProductChassisGateSensorSmoke_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorSmoke = _CmcIIIProductChassisGateSensorSmoke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 279)
)
_CmcIIIProductChassisGateSensorAirflow_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorAirflow = _CmcIIIProductChassisGateSensorAirflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 281)
)
_CmcIIIProductChassisGateSensorInputNO_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorInputNO = _CmcIIIProductChassisGateSensorInputNO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 289)
)
_CmcIIIProductChassisGateSensorInputNC_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorInputNC = _CmcIIIProductChassisGateSensorInputNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 290)
)
_CmcIIIProductChassisGateSensorVoltage_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorVoltage = _CmcIIIProductChassisGateSensorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 297)
)
_CmcIIIProductChassisGateSensorTemp_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorTemp = _CmcIIIProductChassisGateSensorTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 305)
)
_CmcIIIProductChassisGateSensor4to20mA_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensor4to20mA = _CmcIIIProductChassisGateSensor4to20mA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 307)
)
_CmcIIIProductChassisGateSensorFireError_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorFireError = _CmcIIIProductChassisGateSensorFireError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 337)
)
_CmcIIIProductChassisGateSensorFirePre_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorFirePre = _CmcIIIProductChassisGateSensorFirePre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 338)
)
_CmcIIIProductChassisGateSensorFireMain_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorFireMain = _CmcIIIProductChassisGateSensorFireMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 339)
)
_CmcIIIProductChassisGateSensorLeakage_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorLeakage = _CmcIIIProductChassisGateSensorLeakage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 345)
)
_CmcIIIProductChassisGateSensorOutput_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorOutput = _CmcIIIProductChassisGateSensorOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 401)
)
_CmcIIIProductChassisGateSensorDoorMag_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateSensorDoorMag = _CmcIIIProductChassisGateSensorDoorMag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 402)
)
_CmcIIIProductChassisGateLock_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateLock = _CmcIIIProductChassisGateLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 512)
)
_CmcIIIProductChassisTemperature_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisTemperature = _CmcIIIProductChassisTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 768)
)
_CmcIIIProductChassisTempHumi_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisTempHumi = _CmcIIIProductChassisTempHumi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 1024)
)
_CmcIIIProductChassisVandalism_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisVandalism = _CmcIIIProductChassisVandalism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 1280)
)
_CmcIIIProductChassisPressure_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPressure = _CmcIIIProductChassisPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 1536)
)
_CmcIIIProductChassisAccess_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisAccess = _CmcIIIProductChassisAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 1792)
)
_CmcIIIProductChassisIOInput_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisIOInput = _CmcIIIProductChassisIOInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2048)
)
_CmcIIIProductChassisGateUnit_Cfg1_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateUnit_Cfg1 = _CmcIIIProductChassisGateUnit_Cfg1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2304)
)
_CmcIIIProductChassisGateUnit_Cfg2_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateUnit_Cfg2 = _CmcIIIProductChassisGateUnit_Cfg2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2305)
)
_CmcIIIProductChassisGateUnit_Cfg3_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateUnit_Cfg3 = _CmcIIIProductChassisGateUnit_Cfg3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2306)
)
_CmcIIIProductChassisGateUnit_Cfg4_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisGateUnit_Cfg4 = _CmcIIIProductChassisGateUnit_Cfg4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2307)
)
_CmcIIIProductChassisPowerOld_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPowerOld = _CmcIIIProductChassisPowerOld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2560)
)
_CmcIIIProductChassisDRC_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisDRC = _CmcIIIProductChassisDRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 2816)
)
_CmcIIIProductChassisUniInput_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisUniInput = _CmcIIIProductChassisUniInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 3328)
)
_CmcIIIProductChassisPower_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPower = _CmcIIIProductChassisPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 3584)
)
_CmcIIIProductChassisSmoke_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisSmoke = _CmcIIIProductChassisSmoke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 4096)
)
_CmcIIIProductChassisDCM_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisDCM = _CmcIIIProductChassisDCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 4352)
)
_CmcIIIProductChassisLeakage_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLeakage = _CmcIIIProductChassisLeakage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 4608)
)
_CmcIIIProductChassisPSM_CAN_C13_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_CAN_C13 = _CmcIIIProductChassisPSM_CAN_C13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 4864)
)
_CmcIIIProductChassisPSM_CAN_C19_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_CAN_C19 = _CmcIIIProductChassisPSM_CAN_C19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 4865)
)
_CmcIIIProductChassisPSM_CAN_Schuko_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_CAN_Schuko = _CmcIIIProductChassisPSM_CAN_Schuko_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 4866)
)
_CmcIIIProductChassisLCPFan_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPFan = _CmcIIIProductChassisLCPFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 8192)
)
_CmcIIIProductChassisLCPWtr_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPWtr = _CmcIIIProductChassisLCPWtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 8448)
)
_CmcIIIProductChassisLCPFcs_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPFcs = _CmcIIIProductChassisLCPFcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 8704)
)
_CmcIIIProductChassisLCPTsw_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPTsw = _CmcIIIProductChassisLCPTsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 8960)
)
_CmcIIIProductChassisLCPUdx_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPUdx = _CmcIIIProductChassisLCPUdx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 9216)
)
_CmcIIIProductChassisLCP5_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCP5 = _CmcIIIProductChassisLCP5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 9472)
)
_CmcIIIProductChassisLCPMsrz_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPMsrz = _CmcIIIProductChassisLCPMsrz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 9728)
)
_CmcIIIProductChassisLCPT3_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPT3 = _CmcIIIProductChassisLCPT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 9984)
)
_CmcIIIProductChassisLCPFlush_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCPFlush = _CmcIIIProductChassisLCPFlush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 10240)
)
_CmcIIIProductChassisLCP_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisLCP = _CmcIIIProductChassisLCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 10496)
)
_CmcIIIProductChassisPSM_M16_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_M16 = _CmcIIIProductChassisPSM_M16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 12288)
)
_CmcIIIProductChassisPSM_M32_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_M32 = _CmcIIIProductChassisPSM_M32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 12544)
)
_CmcIIIProductChassisPSM_MID_M16_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_MID_M16 = _CmcIIIProductChassisPSM_MID_M16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 13312)
)
_CmcIIIProductChassisPSM_MID_M32_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPSM_MID_M32 = _CmcIIIProductChassisPSM_MID_M32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 13568)
)
_CmcIIIProductChassisPDU_MET_M_1P_16A_C20_12_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_1P_16A_C20_12_00 = _CmcIIIProductChassisPDU_MET_M_1P_16A_C20_12_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14336)
)
_CmcIIIProductChassisPDU_MET_M_1P_16A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_1P_16A_CEE_24_04 = _CmcIIIProductChassisPDU_MET_M_1P_16A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14337)
)
_CmcIIIProductChassisPDU_MET_M_1P_32A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_1P_32A_CEE_24_04 = _CmcIIIProductChassisPDU_MET_M_1P_32A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14338)
)
_CmcIIIProductChassisPDU_MET_M_3P_16A_CEE_18_03_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_16A_CEE_18_03 = _CmcIIIProductChassisPDU_MET_M_3P_16A_CEE_18_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14339)
)
_CmcIIIProductChassisPDU_MET_M_3P_16A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_16A_CEE_24_06 = _CmcIIIProductChassisPDU_MET_M_3P_16A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14340)
)
_CmcIIIProductChassisPDU_MET_M_3P_32A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_32A_CEE_24_06 = _CmcIIIProductChassisPDU_MET_M_3P_32A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14341)
)
_CmcIIIProductChassisPDU_MET_M_3P_32A_CEE_36_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_32A_CEE_36_06 = _CmcIIIProductChassisPDU_MET_M_3P_32A_CEE_36_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14342)
)
_CmcIIIProductChassisPDU_MET_M_3P_16A_CEE_42_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_16A_CEE_42_00 = _CmcIIIProductChassisPDU_MET_M_3P_16A_CEE_42_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14343)
)
_CmcIIIProductChassisPDU_MET_M_3P_32A_CEE_48_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_32A_CEE_48_00 = _CmcIIIProductChassisPDU_MET_M_3P_32A_CEE_48_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14344)
)
_CmcIIIProductChassisPDU_MET_M_3P_63A_CEE_12_12_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_3P_63A_CEE_12_12 = _CmcIIIProductChassisPDU_MET_M_3P_63A_CEE_12_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14345)
)
_CmcIIIProductChassisPDU_MET_M_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MET_M_UserDefined = _CmcIIIProductChassisPDU_MET_M_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14591)
)
_CmcIIIProductChassisPDU_SWI_M_1P_16A_C20_12_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_1P_16A_C20_12_00 = _CmcIIIProductChassisPDU_SWI_M_1P_16A_C20_12_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14592)
)
_CmcIIIProductChassisPDU_SWI_M_1P_16A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_1P_16A_CEE_24_04 = _CmcIIIProductChassisPDU_SWI_M_1P_16A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14593)
)
_CmcIIIProductChassisPDU_SWI_M_1P_32A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_1P_32A_CEE_24_04 = _CmcIIIProductChassisPDU_SWI_M_1P_32A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14594)
)
_CmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_18_03_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_18_03 = _CmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_18_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14595)
)
_CmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_24_06 = _CmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14596)
)
_CmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_24_06 = _CmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14597)
)
_CmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_36_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_36_06 = _CmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_36_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14598)
)
_CmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_42_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_42_00 = _CmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_42_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14599)
)
_CmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_48_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_48_00 = _CmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_48_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14600)
)
_CmcIIIProductChassisPDU_SWI_M_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_SWI_M_UserDefined = _CmcIIIProductChassisPDU_SWI_M_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14847)
)
_CmcIIIProductChassisPDU_MAN_M_1P_16A_C20_12_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_1P_16A_C20_12_00 = _CmcIIIProductChassisPDU_MAN_M_1P_16A_C20_12_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14848)
)
_CmcIIIProductChassisPDU_MAN_M_1P_16A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_1P_16A_CEE_24_04 = _CmcIIIProductChassisPDU_MAN_M_1P_16A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14849)
)
_CmcIIIProductChassisPDU_MAN_M_1P_32A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_1P_32A_CEE_24_04 = _CmcIIIProductChassisPDU_MAN_M_1P_32A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14850)
)
_CmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_18_03_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_18_03 = _CmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_18_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14851)
)
_CmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_24_06 = _CmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14852)
)
_CmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_24_06 = _CmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14853)
)
_CmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_36_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_36_06 = _CmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_36_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14854)
)
_CmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_42_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_42_00 = _CmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_42_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14855)
)
_CmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_48_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_48_00 = _CmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_48_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 14856)
)
_CmcIIIProductChassisPDU_MAN_M_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_M_UserDefined = _CmcIIIProductChassisPDU_MAN_M_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15103)
)
_CmcIIIProductChassisPDU_MAN_S_1P_16A_C20_12_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_1P_16A_C20_12_00 = _CmcIIIProductChassisPDU_MAN_S_1P_16A_C20_12_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15104)
)
_CmcIIIProductChassisPDU_MAN_S_1P_16A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_1P_16A_CEE_24_04 = _CmcIIIProductChassisPDU_MAN_S_1P_16A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15105)
)
_CmcIIIProductChassisPDU_MAN_S_1P_32A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_1P_32A_CEE_24_04 = _CmcIIIProductChassisPDU_MAN_S_1P_32A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15106)
)
_CmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_18_03_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_18_03 = _CmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_18_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15107)
)
_CmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_24_06 = _CmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15108)
)
_CmcIIIProductChassisPDU_MAN_S_3P_32A_CEE_24_06_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_3P_32A_CEE_24_06 = _CmcIIIProductChassisPDU_MAN_S_3P_32A_CEE_24_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15109)
)
_CmcIIIProductChassisPDU_MAN_S_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDU_MAN_S_UserDefined = _CmcIIIProductChassisPDU_MAN_S_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15119)
)
_CmcIIIProductChassisPDUu_MET_M_1P_13A_0UK_16_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MET_M_1P_13A_0UK_16_00 = _CmcIIIProductChassisPDUu_MET_M_1P_13A_0UK_16_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15360)
)
_CmcIIIProductChassisPDUu_MET_M_1P_16A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MET_M_1P_16A_CEE_24_04 = _CmcIIIProductChassisPDUu_MET_M_1P_16A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15361)
)
_CmcIIIProductChassisPDUu_MET_M_1P_32A_CEE_24_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MET_M_1P_32A_CEE_24_04 = _CmcIIIProductChassisPDUu_MET_M_1P_32A_CEE_24_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15362)
)
_CmcIIIProductChassisPDUu_MET_M_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MET_M_UserDefined = _CmcIIIProductChassisPDUu_MET_M_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15615)
)
_CmcIIIProductChassisPDUu_SWI_M_1P_13A_0UK_16_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_SWI_M_1P_13A_0UK_16_00 = _CmcIIIProductChassisPDUu_SWI_M_1P_13A_0UK_16_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15616)
)
_CmcIIIProductChassisPDUu_SWI_M_1P_16A_0UK_16_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_SWI_M_1P_16A_0UK_16_00 = _CmcIIIProductChassisPDUu_SWI_M_1P_16A_0UK_16_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15617)
)
_CmcIIIProductChassisPDUu_SWI_M_1P_32A_CEE_16_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_SWI_M_1P_32A_CEE_16_04 = _CmcIIIProductChassisPDUu_SWI_M_1P_32A_CEE_16_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15618)
)
_CmcIIIProductChassisPDUu_SWI_M_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_SWI_M_UserDefined = _CmcIIIProductChassisPDUu_SWI_M_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15871)
)
_CmcIIIProductChassisPDUu_MAN_M_1P_13A_0UK_16_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_M_1P_13A_0UK_16_00 = _CmcIIIProductChassisPDUu_MAN_M_1P_13A_0UK_16_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15872)
)
_CmcIIIProductChassisPDUu_MAN_M_1P_16A_CEE_16_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_M_1P_16A_CEE_16_04 = _CmcIIIProductChassisPDUu_MAN_M_1P_16A_CEE_16_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15873)
)
_CmcIIIProductChassisPDUu_MAN_M_1P_32A_CEE_16_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_M_1P_32A_CEE_16_04 = _CmcIIIProductChassisPDUu_MAN_M_1P_32A_CEE_16_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 15874)
)
_CmcIIIProductChassisPDUu_MAN_M_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_M_UserDefined = _CmcIIIProductChassisPDUu_MAN_M_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 16127)
)
_CmcIIIProductChassisPDUu_MAN_S_1P_13A_0UK_16_00_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_S_1P_13A_0UK_16_00 = _CmcIIIProductChassisPDUu_MAN_S_1P_13A_0UK_16_00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 16128)
)
_CmcIIIProductChassisPDUu_MAN_S_1P_16A_CEE_16_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_S_1P_16A_CEE_16_04 = _CmcIIIProductChassisPDUu_MAN_S_1P_16A_CEE_16_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 16129)
)
_CmcIIIProductChassisPDUu_MAN_S_1P_32A_CEE_16_04_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_S_1P_32A_CEE_16_04 = _CmcIIIProductChassisPDUu_MAN_S_1P_32A_CEE_16_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 16130)
)
_CmcIIIProductChassisPDUu_MAN_S_UserDefined_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisPDUu_MAN_S_UserDefined = _CmcIIIProductChassisPDUu_MAN_S_UserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 16383)
)
_CmcIIIProductChassisRiMatrixS_S6_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_S6 = _CmcIIIProductChassisRiMatrixS_S6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20481)
)
_CmcIIIProductChassisRiMatrixS_D6_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_D6 = _CmcIIIProductChassisRiMatrixS_D6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20482)
)
_CmcIIIProductChassisRiMatrixS_S9_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_S9 = _CmcIIIProductChassisRiMatrixS_S9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20483)
)
_CmcIIIProductChassisRiMatrixS_D9_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_D9 = _CmcIIIProductChassisRiMatrixS_D9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20484)
)
_CmcIIIProductChassisRiMatrixS_S6W_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_S6W = _CmcIIIProductChassisRiMatrixS_S6W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20485)
)
_CmcIIIProductChassisRiMatrixS_D6W_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_D6W = _CmcIIIProductChassisRiMatrixS_D6W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20486)
)
_CmcIIIProductChassisRiMatrixS_S9W_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_S9W = _CmcIIIProductChassisRiMatrixS_S9W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20487)
)
_CmcIIIProductChassisRiMatrixS_D9W_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisRiMatrixS_D9W = _CmcIIIProductChassisRiMatrixS_D9W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 20488)
)
_CmcIIIProductChassisFireDetect_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireDetect = _CmcIIIProductChassisFireDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 28672)
)
_CmcIIIProductChassisFireExt_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExt = _CmcIIIProductChassisFireExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 28928)
)
_CmcIIIProductChassisFireExtSlave_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtSlave = _CmcIIIProductChassisFireExtSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 29184)
)
_CmcIIIProductChassisFireExtOneU_MX_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtOneU_MX = _CmcIIIProductChassisFireExtOneU_MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 29440)
)
_CmcIIIProductChassisFireExtOneU_MX_ED_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtOneU_MX_ED = _CmcIIIProductChassisFireExtOneU_MX_ED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 29696)
)
_CmcIIIProductChassisFireExtOneU_MX_DD_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtOneU_MX_DD = _CmcIIIProductChassisFireExtOneU_MX_DD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 29952)
)
_CmcIIIProductChassisFireExtOneU_VSN_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtOneU_VSN = _CmcIIIProductChassisFireExtOneU_VSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 30208)
)
_CmcIIIProductChassisFireExtOneU_VSN_ED_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtOneU_VSN_ED = _CmcIIIProductChassisFireExtOneU_VSN_ED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 30464)
)
_CmcIIIProductChassisFireExtOneU_VSN_DD_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisFireExtOneU_VSN_DD = _CmcIIIProductChassisFireExtOneU_VSN_DD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 30720)
)
_CmcIIIProductChassisInternal_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisInternal = _CmcIIIProductChassisInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 32768)
)
_CmcIIIProductChassisSES_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisSES = _CmcIIIProductChassisSES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 36864)
)
_CmcIIIProductChassisVirtualTwoLevel_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisVirtualTwoLevel = _CmcIIIProductChassisVirtualTwoLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 61440)
)
_CmcIIIProductChassisVirtualAccess_ObjectIdentity = ObjectIdentity
cmcIIIProductChassisVirtualAccess = _CmcIIIProductChassisVirtualAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 4, 61696)
)
_CmcIIIProductSensor_ObjectIdentity = ObjectIdentity
cmcIIIProductSensor = _CmcIIIProductSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 7, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RITTAL-CMC-III-PRODUCTS-MIB",
    **{"cmcIIIProducts": cmcIIIProducts,
       "cmcIIIProductUnit": cmcIIIProductUnit,
       "cmcIIIProductUnitUnknown": cmcIIIProductUnitUnknown,
       "cmcIIIProductUnitPUIII": cmcIIIProductUnitPUIII,
       "cmcIIIProductUnitCompact": cmcIIIProductUnitCompact,
       "cmcIIIProductUnitLCP": cmcIIIProductUnitLCP,
       "cmcIIIProductUnitPDU": cmcIIIProductUnitPDU,
       "cmcIIIProductUnitRMS": cmcIIIProductUnitRMS,
       "cmcIIIProductPort": cmcIIIProductPort,
       "cmcIIIProductPortUnknown": cmcIIIProductPortUnknown,
       "cmcIIIProductPortLoopback": cmcIIIProductPortLoopback,
       "cmcIIIProductPortCanBus": cmcIIIProductPortCanBus,
       "cmcIIIProductPortEthernet": cmcIIIProductPortEthernet,
       "cmcIIIProductPortVirtualCanBus": cmcIIIProductPortVirtualCanBus,
       "cmcIIIProductPortTunnel": cmcIIIProductPortTunnel,
       "cmcIIIProductPortSit": cmcIIIProductPortSit,
       "cmcIIIProductPowerSupply": cmcIIIProductPowerSupply,
       "cmcIIIProductPowerSupplyUnknown": cmcIIIProductPowerSupplyUnknown,
       "cmcIIIProductPowerSupplyAcAdapter": cmcIIIProductPowerSupplyAcAdapter,
       "cmcIIIProductPowerSupplyTerminalStrip": cmcIIIProductPowerSupplyTerminalStrip,
       "cmcIIIProductPowerSupplyPOE": cmcIIIProductPowerSupplyPOE,
       "cmcIIIProductPowerSupplyUSB": cmcIIIProductPowerSupplyUSB,
       "cmcIIIProductChassis": cmcIIIProductChassis,
       "cmcIIIProductChassisGateSensorUnknown": cmcIIIProductChassisGateSensorUnknown,
       "cmcIIIProductChassisGateSensorAccess": cmcIIIProductChassisGateSensorAccess,
       "cmcIIIProductChassisGateSensorMotion": cmcIIIProductChassisGateSensorMotion,
       "cmcIIIProductChassisGateSensorSmoke": cmcIIIProductChassisGateSensorSmoke,
       "cmcIIIProductChassisGateSensorAirflow": cmcIIIProductChassisGateSensorAirflow,
       "cmcIIIProductChassisGateSensorInputNO": cmcIIIProductChassisGateSensorInputNO,
       "cmcIIIProductChassisGateSensorInputNC": cmcIIIProductChassisGateSensorInputNC,
       "cmcIIIProductChassisGateSensorVoltage": cmcIIIProductChassisGateSensorVoltage,
       "cmcIIIProductChassisGateSensorTemp": cmcIIIProductChassisGateSensorTemp,
       "cmcIIIProductChassisGateSensor4to20mA": cmcIIIProductChassisGateSensor4to20mA,
       "cmcIIIProductChassisGateSensorFireError": cmcIIIProductChassisGateSensorFireError,
       "cmcIIIProductChassisGateSensorFirePre": cmcIIIProductChassisGateSensorFirePre,
       "cmcIIIProductChassisGateSensorFireMain": cmcIIIProductChassisGateSensorFireMain,
       "cmcIIIProductChassisGateSensorLeakage": cmcIIIProductChassisGateSensorLeakage,
       "cmcIIIProductChassisGateSensorOutput": cmcIIIProductChassisGateSensorOutput,
       "cmcIIIProductChassisGateSensorDoorMag": cmcIIIProductChassisGateSensorDoorMag,
       "cmcIIIProductChassisGateLock": cmcIIIProductChassisGateLock,
       "cmcIIIProductChassisTemperature": cmcIIIProductChassisTemperature,
       "cmcIIIProductChassisTempHumi": cmcIIIProductChassisTempHumi,
       "cmcIIIProductChassisVandalism": cmcIIIProductChassisVandalism,
       "cmcIIIProductChassisPressure": cmcIIIProductChassisPressure,
       "cmcIIIProductChassisAccess": cmcIIIProductChassisAccess,
       "cmcIIIProductChassisIOInput": cmcIIIProductChassisIOInput,
       "cmcIIIProductChassisGateUnit-Cfg1": cmcIIIProductChassisGateUnit_Cfg1,
       "cmcIIIProductChassisGateUnit-Cfg2": cmcIIIProductChassisGateUnit_Cfg2,
       "cmcIIIProductChassisGateUnit-Cfg3": cmcIIIProductChassisGateUnit_Cfg3,
       "cmcIIIProductChassisGateUnit-Cfg4": cmcIIIProductChassisGateUnit_Cfg4,
       "cmcIIIProductChassisPowerOld": cmcIIIProductChassisPowerOld,
       "cmcIIIProductChassisDRC": cmcIIIProductChassisDRC,
       "cmcIIIProductChassisUniInput": cmcIIIProductChassisUniInput,
       "cmcIIIProductChassisPower": cmcIIIProductChassisPower,
       "cmcIIIProductChassisSmoke": cmcIIIProductChassisSmoke,
       "cmcIIIProductChassisDCM": cmcIIIProductChassisDCM,
       "cmcIIIProductChassisLeakage": cmcIIIProductChassisLeakage,
       "cmcIIIProductChassisPSM-CAN-C13": cmcIIIProductChassisPSM_CAN_C13,
       "cmcIIIProductChassisPSM-CAN-C19": cmcIIIProductChassisPSM_CAN_C19,
       "cmcIIIProductChassisPSM-CAN-Schuko": cmcIIIProductChassisPSM_CAN_Schuko,
       "cmcIIIProductChassisLCPFan": cmcIIIProductChassisLCPFan,
       "cmcIIIProductChassisLCPWtr": cmcIIIProductChassisLCPWtr,
       "cmcIIIProductChassisLCPFcs": cmcIIIProductChassisLCPFcs,
       "cmcIIIProductChassisLCPTsw": cmcIIIProductChassisLCPTsw,
       "cmcIIIProductChassisLCPUdx": cmcIIIProductChassisLCPUdx,
       "cmcIIIProductChassisLCP5": cmcIIIProductChassisLCP5,
       "cmcIIIProductChassisLCPMsrz": cmcIIIProductChassisLCPMsrz,
       "cmcIIIProductChassisLCPT3": cmcIIIProductChassisLCPT3,
       "cmcIIIProductChassisLCPFlush": cmcIIIProductChassisLCPFlush,
       "cmcIIIProductChassisLCP": cmcIIIProductChassisLCP,
       "cmcIIIProductChassisPSM-M16": cmcIIIProductChassisPSM_M16,
       "cmcIIIProductChassisPSM-M32": cmcIIIProductChassisPSM_M32,
       "cmcIIIProductChassisPSM-MID-M16": cmcIIIProductChassisPSM_MID_M16,
       "cmcIIIProductChassisPSM-MID-M32": cmcIIIProductChassisPSM_MID_M32,
       "cmcIIIProductChassisPDU-MET-M-1P-16A-C20-12-00": cmcIIIProductChassisPDU_MET_M_1P_16A_C20_12_00,
       "cmcIIIProductChassisPDU-MET-M-1P-16A-CEE-24-04": cmcIIIProductChassisPDU_MET_M_1P_16A_CEE_24_04,
       "cmcIIIProductChassisPDU-MET-M-1P-32A-CEE-24-04": cmcIIIProductChassisPDU_MET_M_1P_32A_CEE_24_04,
       "cmcIIIProductChassisPDU-MET-M-3P-16A-CEE-18-03": cmcIIIProductChassisPDU_MET_M_3P_16A_CEE_18_03,
       "cmcIIIProductChassisPDU-MET-M-3P-16A-CEE-24-06": cmcIIIProductChassisPDU_MET_M_3P_16A_CEE_24_06,
       "cmcIIIProductChassisPDU-MET-M-3P-32A-CEE-24-06": cmcIIIProductChassisPDU_MET_M_3P_32A_CEE_24_06,
       "cmcIIIProductChassisPDU-MET-M-3P-32A-CEE-36-06": cmcIIIProductChassisPDU_MET_M_3P_32A_CEE_36_06,
       "cmcIIIProductChassisPDU-MET-M-3P-16A-CEE-42-00": cmcIIIProductChassisPDU_MET_M_3P_16A_CEE_42_00,
       "cmcIIIProductChassisPDU-MET-M-3P-32A-CEE-48-00": cmcIIIProductChassisPDU_MET_M_3P_32A_CEE_48_00,
       "cmcIIIProductChassisPDU-MET-M-3P-63A-CEE-12-12": cmcIIIProductChassisPDU_MET_M_3P_63A_CEE_12_12,
       "cmcIIIProductChassisPDU-MET-M-UserDefined": cmcIIIProductChassisPDU_MET_M_UserDefined,
       "cmcIIIProductChassisPDU-SWI-M-1P-16A-C20-12-00": cmcIIIProductChassisPDU_SWI_M_1P_16A_C20_12_00,
       "cmcIIIProductChassisPDU-SWI-M-1P-16A-CEE-24-04": cmcIIIProductChassisPDU_SWI_M_1P_16A_CEE_24_04,
       "cmcIIIProductChassisPDU-SWI-M-1P-32A-CEE-24-04": cmcIIIProductChassisPDU_SWI_M_1P_32A_CEE_24_04,
       "cmcIIIProductChassisPDU-SWI-M-3P-16A-CEE-18-03": cmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_18_03,
       "cmcIIIProductChassisPDU-SWI-M-3P-16A-CEE-24-06": cmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_24_06,
       "cmcIIIProductChassisPDU-SWI-M-3P-32A-CEE-24-06": cmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_24_06,
       "cmcIIIProductChassisPDU-SWI-M-3P-32A-CEE-36-06": cmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_36_06,
       "cmcIIIProductChassisPDU-SWI-M-3P-16A-CEE-42-00": cmcIIIProductChassisPDU_SWI_M_3P_16A_CEE_42_00,
       "cmcIIIProductChassisPDU-SWI-M-3P-32A-CEE-48-00": cmcIIIProductChassisPDU_SWI_M_3P_32A_CEE_48_00,
       "cmcIIIProductChassisPDU-SWI-M-UserDefined": cmcIIIProductChassisPDU_SWI_M_UserDefined,
       "cmcIIIProductChassisPDU-MAN-M-1P-16A-C20-12-00": cmcIIIProductChassisPDU_MAN_M_1P_16A_C20_12_00,
       "cmcIIIProductChassisPDU-MAN-M-1P-16A-CEE-24-04": cmcIIIProductChassisPDU_MAN_M_1P_16A_CEE_24_04,
       "cmcIIIProductChassisPDU-MAN-M-1P-32A-CEE-24-04": cmcIIIProductChassisPDU_MAN_M_1P_32A_CEE_24_04,
       "cmcIIIProductChassisPDU-MAN-M-3P-16A-CEE-18-03": cmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_18_03,
       "cmcIIIProductChassisPDU-MAN-M-3P-16A-CEE-24-06": cmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_24_06,
       "cmcIIIProductChassisPDU-MAN-M-3P-32A-CEE-24-06": cmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_24_06,
       "cmcIIIProductChassisPDU-MAN-M-3P-32A-CEE-36-06": cmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_36_06,
       "cmcIIIProductChassisPDU-MAN-M-3P-16A-CEE-42-00": cmcIIIProductChassisPDU_MAN_M_3P_16A_CEE_42_00,
       "cmcIIIProductChassisPDU-MAN-M-3P-32A-CEE-48-00": cmcIIIProductChassisPDU_MAN_M_3P_32A_CEE_48_00,
       "cmcIIIProductChassisPDU-MAN-M-UserDefined": cmcIIIProductChassisPDU_MAN_M_UserDefined,
       "cmcIIIProductChassisPDU-MAN-S-1P-16A-C20-12-00": cmcIIIProductChassisPDU_MAN_S_1P_16A_C20_12_00,
       "cmcIIIProductChassisPDU-MAN-S-1P-16A-CEE-24-04": cmcIIIProductChassisPDU_MAN_S_1P_16A_CEE_24_04,
       "cmcIIIProductChassisPDU-MAN-S-1P-32A-CEE-24-04": cmcIIIProductChassisPDU_MAN_S_1P_32A_CEE_24_04,
       "cmcIIIProductChassisPDU-MAN-S-3P-16A-CEE-18-03": cmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_18_03,
       "cmcIIIProductChassisPDU-MAN-S-3P-16A-CEE-24-06": cmcIIIProductChassisPDU_MAN_S_3P_16A_CEE_24_06,
       "cmcIIIProductChassisPDU-MAN-S-3P-32A-CEE-24-06": cmcIIIProductChassisPDU_MAN_S_3P_32A_CEE_24_06,
       "cmcIIIProductChassisPDU-MAN-S-UserDefined": cmcIIIProductChassisPDU_MAN_S_UserDefined,
       "cmcIIIProductChassisPDUu-MET-M-1P-13A-0UK-16-00": cmcIIIProductChassisPDUu_MET_M_1P_13A_0UK_16_00,
       "cmcIIIProductChassisPDUu-MET-M-1P-16A-CEE-24-04": cmcIIIProductChassisPDUu_MET_M_1P_16A_CEE_24_04,
       "cmcIIIProductChassisPDUu-MET-M-1P-32A-CEE-24-04": cmcIIIProductChassisPDUu_MET_M_1P_32A_CEE_24_04,
       "cmcIIIProductChassisPDUu-MET-M-UserDefined": cmcIIIProductChassisPDUu_MET_M_UserDefined,
       "cmcIIIProductChassisPDUu-SWI-M-1P-13A-0UK-16-00": cmcIIIProductChassisPDUu_SWI_M_1P_13A_0UK_16_00,
       "cmcIIIProductChassisPDUu-SWI-M-1P-16A-0UK-16-00": cmcIIIProductChassisPDUu_SWI_M_1P_16A_0UK_16_00,
       "cmcIIIProductChassisPDUu-SWI-M-1P-32A-CEE-16-04": cmcIIIProductChassisPDUu_SWI_M_1P_32A_CEE_16_04,
       "cmcIIIProductChassisPDUu-SWI-M-UserDefined": cmcIIIProductChassisPDUu_SWI_M_UserDefined,
       "cmcIIIProductChassisPDUu-MAN-M-1P-13A-0UK-16-00": cmcIIIProductChassisPDUu_MAN_M_1P_13A_0UK_16_00,
       "cmcIIIProductChassisPDUu-MAN-M-1P-16A-CEE-16-04": cmcIIIProductChassisPDUu_MAN_M_1P_16A_CEE_16_04,
       "cmcIIIProductChassisPDUu-MAN-M-1P-32A-CEE-16-04": cmcIIIProductChassisPDUu_MAN_M_1P_32A_CEE_16_04,
       "cmcIIIProductChassisPDUu-MAN-M-UserDefined": cmcIIIProductChassisPDUu_MAN_M_UserDefined,
       "cmcIIIProductChassisPDUu-MAN-S-1P-13A-0UK-16-00": cmcIIIProductChassisPDUu_MAN_S_1P_13A_0UK_16_00,
       "cmcIIIProductChassisPDUu-MAN-S-1P-16A-CEE-16-04": cmcIIIProductChassisPDUu_MAN_S_1P_16A_CEE_16_04,
       "cmcIIIProductChassisPDUu-MAN-S-1P-32A-CEE-16-04": cmcIIIProductChassisPDUu_MAN_S_1P_32A_CEE_16_04,
       "cmcIIIProductChassisPDUu-MAN-S-UserDefined": cmcIIIProductChassisPDUu_MAN_S_UserDefined,
       "cmcIIIProductChassisRiMatrixS-S6": cmcIIIProductChassisRiMatrixS_S6,
       "cmcIIIProductChassisRiMatrixS-D6": cmcIIIProductChassisRiMatrixS_D6,
       "cmcIIIProductChassisRiMatrixS-S9": cmcIIIProductChassisRiMatrixS_S9,
       "cmcIIIProductChassisRiMatrixS-D9": cmcIIIProductChassisRiMatrixS_D9,
       "cmcIIIProductChassisRiMatrixS-S6W": cmcIIIProductChassisRiMatrixS_S6W,
       "cmcIIIProductChassisRiMatrixS-D6W": cmcIIIProductChassisRiMatrixS_D6W,
       "cmcIIIProductChassisRiMatrixS-S9W": cmcIIIProductChassisRiMatrixS_S9W,
       "cmcIIIProductChassisRiMatrixS-D9W": cmcIIIProductChassisRiMatrixS_D9W,
       "cmcIIIProductChassisFireDetect": cmcIIIProductChassisFireDetect,
       "cmcIIIProductChassisFireExt": cmcIIIProductChassisFireExt,
       "cmcIIIProductChassisFireExtSlave": cmcIIIProductChassisFireExtSlave,
       "cmcIIIProductChassisFireExtOneU-MX": cmcIIIProductChassisFireExtOneU_MX,
       "cmcIIIProductChassisFireExtOneU-MX-ED": cmcIIIProductChassisFireExtOneU_MX_ED,
       "cmcIIIProductChassisFireExtOneU-MX-DD": cmcIIIProductChassisFireExtOneU_MX_DD,
       "cmcIIIProductChassisFireExtOneU-VSN": cmcIIIProductChassisFireExtOneU_VSN,
       "cmcIIIProductChassisFireExtOneU-VSN-ED": cmcIIIProductChassisFireExtOneU_VSN_ED,
       "cmcIIIProductChassisFireExtOneU-VSN-DD": cmcIIIProductChassisFireExtOneU_VSN_DD,
       "cmcIIIProductChassisInternal": cmcIIIProductChassisInternal,
       "cmcIIIProductChassisSES": cmcIIIProductChassisSES,
       "cmcIIIProductChassisVirtualTwoLevel": cmcIIIProductChassisVirtualTwoLevel,
       "cmcIIIProductChassisVirtualAccess": cmcIIIProductChassisVirtualAccess,
       "cmcIIIProductSensor": cmcIIIProductSensor}
)
