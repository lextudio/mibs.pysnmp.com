# SNMP MIB module (ACMEPACKET-ENTITY-VENDORTYPE-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACMEPACKET-ENTITY-VENDORTYPE-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:32 2024
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

(acmepacketModules,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketModules")

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

acmepacketEntityVendortypeOIDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApevMIBObjects_ObjectIdentity = ObjectIdentity
apevMIBObjects = _ApevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1)
)
_ApevOther_ObjectIdentity = ObjectIdentity
apevOther = _ApevOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 1)
)
_ApevUnknown_ObjectIdentity = ObjectIdentity
apevUnknown = _ApevUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 2)
)
_ApevChassis_ObjectIdentity = ObjectIdentity
apevChassis = _ApevChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3)
)
_ApevChassisUnknown_ObjectIdentity = ObjectIdentity
apevChassisUnknown = _ApevChassisUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 1)
)
_ApevChassisSD_ObjectIdentity = ObjectIdentity
apevChassisSD = _ApevChassisSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2)
)
_ApevChassisSDUnknown_ObjectIdentity = ObjectIdentity
apevChassisSDUnknown = _ApevChassisSDUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 1)
)
_ApevChassisSD1_ObjectIdentity = ObjectIdentity
apevChassisSD1 = _ApevChassisSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 2)
)
_ApevChassisSD2_ObjectIdentity = ObjectIdentity
apevChassisSD2 = _ApevChassisSD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 3)
)
_ApevChassisSD2QoS_ObjectIdentity = ObjectIdentity
apevChassisSD2QoS = _ApevChassisSD2QoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 4)
)
_ApevChassisSD3_ObjectIdentity = ObjectIdentity
apevChassisSD3 = _ApevChassisSD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 5)
)
_ApevChassisSD4_ObjectIdentity = ObjectIdentity
apevChassisSD4 = _ApevChassisSD4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 2, 6)
)
_ApevChassisSR_ObjectIdentity = ObjectIdentity
apevChassisSR = _ApevChassisSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 3, 3)
)
_ApevContainer_ObjectIdentity = ObjectIdentity
apevContainer = _ApevContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4)
)
_ApevContainerUnknown_ObjectIdentity = ObjectIdentity
apevContainerUnknown = _ApevContainerUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 1)
)
_ApevContainerSlot_ObjectIdentity = ObjectIdentity
apevContainerSlot = _ApevContainerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2)
)
_ApevContainerSlotUnknown_ObjectIdentity = ObjectIdentity
apevContainerSlotUnknown = _ApevContainerSlotUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2, 1)
)
_ApevContainerSlotPHY_ObjectIdentity = ObjectIdentity
apevContainerSlotPHY = _ApevContainerSlotPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2, 2)
)
_ApevContainerSlotPCMCIA_ObjectIdentity = ObjectIdentity
apevContainerSlotPCMCIA = _ApevContainerSlotPCMCIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 2, 3)
)
_ApevContainerDaughterCard_ObjectIdentity = ObjectIdentity
apevContainerDaughterCard = _ApevContainerDaughterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3)
)
_ApevContainerDaughterCardUnknown_ObjectIdentity = ObjectIdentity
apevContainerDaughterCardUnknown = _ApevContainerDaughterCardUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 1)
)
_ApevContainerDaughterCardCAM_ObjectIdentity = ObjectIdentity
apevContainerDaughterCardCAM = _ApevContainerDaughterCardCAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 2)
)
_ApevContainerDaughterCardCPU_ObjectIdentity = ObjectIdentity
apevContainerDaughterCardCPU = _ApevContainerDaughterCardCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 3)
)
_ApevContainerDaughterCardPMC_ObjectIdentity = ObjectIdentity
apevContainerDaughterCardPMC = _ApevContainerDaughterCardPMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 4)
)
_ApevContainerDaughterCardMemory_ObjectIdentity = ObjectIdentity
apevContainerDaughterCardMemory = _ApevContainerDaughterCardMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 5)
)
_ApevContainerDaughterCardTLS_ObjectIdentity = ObjectIdentity
apevContainerDaughterCardTLS = _ApevContainerDaughterCardTLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 3, 6)
)
_ApevContainerPowerTray_ObjectIdentity = ObjectIdentity
apevContainerPowerTray = _ApevContainerPowerTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 4)
)
_ApevContainerFanTray_ObjectIdentity = ObjectIdentity
apevContainerFanTray = _ApevContainerFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 5)
)
_ApevContainerModules_ObjectIdentity = ObjectIdentity
apevContainerModules = _ApevContainerModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 4, 6)
)
_ApevPowerSupply_ObjectIdentity = ObjectIdentity
apevPowerSupply = _ApevPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5)
)
_ApevPowerSupplyUnknown_ObjectIdentity = ObjectIdentity
apevPowerSupplyUnknown = _ApevPowerSupplyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 1)
)
_ApevPowerSupply150W_ObjectIdentity = ObjectIdentity
apevPowerSupply150W = _ApevPowerSupply150W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 2)
)
_ApevPowerSupply300W_ObjectIdentity = ObjectIdentity
apevPowerSupply300W = _ApevPowerSupply300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 5, 3)
)
_ApevFan_ObjectIdentity = ObjectIdentity
apevFan = _ApevFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6)
)
_ApevFanUnknown_ObjectIdentity = ObjectIdentity
apevFanUnknown = _ApevFanUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 1)
)
_ApevFan40x20_ObjectIdentity = ObjectIdentity
apevFan40x20 = _ApevFan40x20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 2)
)
_ApevFan40x28_ObjectIdentity = ObjectIdentity
apevFan40x28 = _ApevFan40x28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 6, 3)
)
_ApevSensor_ObjectIdentity = ObjectIdentity
apevSensor = _ApevSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7)
)
_ApevSensorUnknown_ObjectIdentity = ObjectIdentity
apevSensorUnknown = _ApevSensorUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 1)
)
_ApevSensorTemperature_ObjectIdentity = ObjectIdentity
apevSensorTemperature = _ApevSensorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 2)
)
_ApevSensorVoltage_ObjectIdentity = ObjectIdentity
apevSensorVoltage = _ApevSensorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 3)
)
_ApevSensorFanSpeed_ObjectIdentity = ObjectIdentity
apevSensorFanSpeed = _ApevSensorFanSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 7, 4)
)
_ApevModule_ObjectIdentity = ObjectIdentity
apevModule = _ApevModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8)
)
_ApevModuleUnknown_ObjectIdentity = ObjectIdentity
apevModuleUnknown = _ApevModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 1)
)
_ApevModulePHYCard_ObjectIdentity = ObjectIdentity
apevModulePHYCard = _ApevModulePHYCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2)
)
_ApevPHYCardUnknown_ObjectIdentity = ObjectIdentity
apevPHYCardUnknown = _ApevPHYCardUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 1)
)
_ApevPHY1GigPortMultiMode_ObjectIdentity = ObjectIdentity
apevPHY1GigPortMultiMode = _ApevPHY1GigPortMultiMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 2)
)
_ApevPHY1GigPortSingleMode_ObjectIdentity = ObjectIdentity
apevPHY1GigPortSingleMode = _ApevPHY1GigPortSingleMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 3)
)
_ApevPHY2GigPortstMultiMode_ObjectIdentity = ObjectIdentity
apevPHY2GigPortstMultiMode = _ApevPHY2GigPortstMultiMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 4)
)
_ApevPHY2GigPortsSingleMode_ObjectIdentity = ObjectIdentity
apevPHY2GigPortsSingleMode = _ApevPHY2GigPortsSingleMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 5)
)
_ApecPHY4FEPorts_ObjectIdentity = ObjectIdentity
apecPHY4FEPorts = _ApecPHY4FEPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 6)
)
_ApevPHY4FEPorts1089_ObjectIdentity = ObjectIdentity
apevPHY4FEPorts1089 = _ApevPHY4FEPorts1089_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 7)
)
_ApevPHY2GigPortsSec_ObjectIdentity = ObjectIdentity
apevPHY2GigPortsSec = _ApevPHY2GigPortsSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 8)
)
_ApevPHY2FEPortsSec_ObjectIdentity = ObjectIdentity
apevPHY2FEPortsSec = _ApevPHY2FEPortsSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 9)
)
_ApevPHY4GigPorts_ObjectIdentity = ObjectIdentity
apevPHY4GigPorts = _ApevPHY4GigPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 10)
)
_ApevPHY4SFPPorts_ObjectIdentity = ObjectIdentity
apevPHY4SFPPorts = _ApevPHY4SFPPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 11)
)
_ApevPHY44SFPPortsSecQos_ObjectIdentity = ObjectIdentity
apevPHY44SFPPortsSecQos = _ApevPHY44SFPPortsSecQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 12)
)
_ApevPHY4SFPPortsQos_ObjectIdentity = ObjectIdentity
apevPHY4SFPPortsQos = _ApevPHY4SFPPortsQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 13)
)
_ApevPHY4SFPPortsSec_ObjectIdentity = ObjectIdentity
apevPHY4SFPPortsSec = _ApevPHY4SFPPortsSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 14)
)
_ApevPHY8FEPorts_ObjectIdentity = ObjectIdentity
apevPHY8FEPorts = _ApevPHY8FEPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 15)
)
_ApevPHY4SFPPortsSecQosCav_ObjectIdentity = ObjectIdentity
apevPHY4SFPPortsSecQosCav = _ApevPHY4SFPPortsSecQosCav_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 2, 16)
)
_ApevModuleCAM_ObjectIdentity = ObjectIdentity
apevModuleCAM = _ApevModuleCAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3)
)
_ApevModuleCAMUnknown_ObjectIdentity = ObjectIdentity
apevModuleCAMUnknown = _ApevModuleCAMUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3, 1)
)
_ApevModuleCAMAMCC_ObjectIdentity = ObjectIdentity
apevModuleCAMAMCC = _ApevModuleCAMAMCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3, 2)
)
_ApevModuleCAMIDT_ObjectIdentity = ObjectIdentity
apevModuleCAMIDT = _ApevModuleCAMIDT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 3, 3)
)
_ApevModuleHostProcessor_ObjectIdentity = ObjectIdentity
apevModuleHostProcessor = _ApevModuleHostProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4)
)
_ApevModuleHPUnknown_ObjectIdentity = ObjectIdentity
apevModuleHPUnknown = _ApevModuleHPUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 1)
)
_ApevModuleHP7451_ObjectIdentity = ObjectIdentity
apevModuleHP7451 = _ApevModuleHP7451_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 2)
)
_ApevModuleHP7455_ObjectIdentity = ObjectIdentity
apevModuleHP7455 = _ApevModuleHP7455_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 3)
)
_ApevModuleHP7457_ObjectIdentity = ObjectIdentity
apevModuleHP7457 = _ApevModuleHP7457_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4)
)
_ApevHP7457Unknown_ObjectIdentity = ObjectIdentity
apevHP7457Unknown = _ApevHP7457Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 1)
)
_ApevHP7457DC8MB_ObjectIdentity = ObjectIdentity
apevHP7457DC8MB = _ApevHP7457DC8MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 2)
)
_ApevHP7457DC4MB_ObjectIdentity = ObjectIdentity
apevHP7457DC4MB = _ApevHP7457DC4MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 3)
)
_ApevHP7457AC8MB_ObjectIdentity = ObjectIdentity
apevHP7457AC8MB = _ApevHP7457AC8MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 4)
)
_ApevHP7457AC4MB_ObjectIdentity = ObjectIdentity
apevHP7457AC4MB = _ApevHP7457AC4MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 5)
)
_ApevHP7457ACDC8MB_ObjectIdentity = ObjectIdentity
apevHP7457ACDC8MB = _ApevHP7457ACDC8MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 4, 6)
)
_ApevModuleHPT2500_ObjectIdentity = ObjectIdentity
apevModuleHPT2500 = _ApevModuleHPT2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 5)
)
_ApevModuleHPCeleron_ObjectIdentity = ObjectIdentity
apevModuleHPCeleron = _ApevModuleHPCeleron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 6)
)
_ApevModuleHPT9400_ObjectIdentity = ObjectIdentity
apevModuleHPT9400 = _ApevModuleHPT9400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 4, 7)
)
_ApevModulePMC_ObjectIdentity = ObjectIdentity
apevModulePMC = _ApevModulePMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 5)
)
_ApevModulePMCUnknown_ObjectIdentity = ObjectIdentity
apevModulePMCUnknown = _ApevModulePMCUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 5, 1)
)
_ApevModulePCMCIA_ObjectIdentity = ObjectIdentity
apevModulePCMCIA = _ApevModulePCMCIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6)
)
_ApevModulePCMCIAUnknown_ObjectIdentity = ObjectIdentity
apevModulePCMCIAUnknown = _ApevModulePCMCIAUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6, 1)
)
_ApevModulePCMCIAATA_ObjectIdentity = ObjectIdentity
apevModulePCMCIAATA = _ApevModulePCMCIAATA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6, 2)
)
_ApevModulePCMCIALinear_ObjectIdentity = ObjectIdentity
apevModulePCMCIALinear = _ApevModulePCMCIALinear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 6, 3)
)
_ApevModuleMemory_ObjectIdentity = ObjectIdentity
apevModuleMemory = _ApevModuleMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7)
)
_ApevModuleMemoryUnknown_ObjectIdentity = ObjectIdentity
apevModuleMemoryUnknown = _ApevModuleMemoryUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7, 1)
)
_ApevModuleMemory1G_ObjectIdentity = ObjectIdentity
apevModuleMemory1G = _ApevModuleMemory1G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7, 2)
)
_ApevModuleMemory4G_ObjectIdentity = ObjectIdentity
apevModuleMemory4G = _ApevModuleMemory4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 7, 3)
)
_ApevModuleCard_ObjectIdentity = ObjectIdentity
apevModuleCard = _ApevModuleCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8)
)
_ApevModuleSPU_ObjectIdentity = ObjectIdentity
apevModuleSPU = _ApevModuleSPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 1)
)
_ApevModuleNPU_ObjectIdentity = ObjectIdentity
apevModuleNPU = _ApevModuleNPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 2)
)
_ApevModuleTCU_ObjectIdentity = ObjectIdentity
apevModuleTCU = _ApevModuleTCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 3)
)
_ApevModuleMIU_ObjectIdentity = ObjectIdentity
apevModuleMIU = _ApevModuleMIU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 4)
)
_ApevModulePHY_ObjectIdentity = ObjectIdentity
apevModulePHY = _ApevModulePHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 5)
)
_ApevModuleTLS_ObjectIdentity = ObjectIdentity
apevModuleTLS = _ApevModuleTLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 8, 8, 6)
)
_ApevPort_ObjectIdentity = ObjectIdentity
apevPort = _ApevPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9)
)
_ApevPortUnknown_ObjectIdentity = ObjectIdentity
apevPortUnknown = _ApevPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 1)
)
_ApevPortGigE_ObjectIdentity = ObjectIdentity
apevPortGigE = _ApevPortGigE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 2)
)
_ApevPortFE_ObjectIdentity = ObjectIdentity
apevPortFE = _ApevPortFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 3)
)
_ApevPort2Gig_ObjectIdentity = ObjectIdentity
apevPort2Gig = _ApevPort2Gig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 4)
)
_ApevPortMMFiber_ObjectIdentity = ObjectIdentity
apevPortMMFiber = _ApevPortMMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 5)
)
_ApevPortSMFiber_ObjectIdentity = ObjectIdentity
apevPortSMFiber = _ApevPortSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 6)
)
_ApevPort10GFiber_ObjectIdentity = ObjectIdentity
apevPort10GFiber = _ApevPort10GFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 9, 7)
)
_ApevStack_ObjectIdentity = ObjectIdentity
apevStack = _ApevStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6, 1, 1, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-ENTITY-VENDORTYPE-OID-MIB",
    **{"acmepacketEntityVendortypeOIDMIB": acmepacketEntityVendortypeOIDMIB,
       "apevMIBObjects": apevMIBObjects,
       "apevOther": apevOther,
       "apevUnknown": apevUnknown,
       "apevChassis": apevChassis,
       "apevChassisUnknown": apevChassisUnknown,
       "apevChassisSD": apevChassisSD,
       "apevChassisSDUnknown": apevChassisSDUnknown,
       "apevChassisSD1": apevChassisSD1,
       "apevChassisSD2": apevChassisSD2,
       "apevChassisSD2QoS": apevChassisSD2QoS,
       "apevChassisSD3": apevChassisSD3,
       "apevChassisSD4": apevChassisSD4,
       "apevChassisSR": apevChassisSR,
       "apevContainer": apevContainer,
       "apevContainerUnknown": apevContainerUnknown,
       "apevContainerSlot": apevContainerSlot,
       "apevContainerSlotUnknown": apevContainerSlotUnknown,
       "apevContainerSlotPHY": apevContainerSlotPHY,
       "apevContainerSlotPCMCIA": apevContainerSlotPCMCIA,
       "apevContainerDaughterCard": apevContainerDaughterCard,
       "apevContainerDaughterCardUnknown": apevContainerDaughterCardUnknown,
       "apevContainerDaughterCardCAM": apevContainerDaughterCardCAM,
       "apevContainerDaughterCardCPU": apevContainerDaughterCardCPU,
       "apevContainerDaughterCardPMC": apevContainerDaughterCardPMC,
       "apevContainerDaughterCardMemory": apevContainerDaughterCardMemory,
       "apevContainerDaughterCardTLS": apevContainerDaughterCardTLS,
       "apevContainerPowerTray": apevContainerPowerTray,
       "apevContainerFanTray": apevContainerFanTray,
       "apevContainerModules": apevContainerModules,
       "apevPowerSupply": apevPowerSupply,
       "apevPowerSupplyUnknown": apevPowerSupplyUnknown,
       "apevPowerSupply150W": apevPowerSupply150W,
       "apevPowerSupply300W": apevPowerSupply300W,
       "apevFan": apevFan,
       "apevFanUnknown": apevFanUnknown,
       "apevFan40x20": apevFan40x20,
       "apevFan40x28": apevFan40x28,
       "apevSensor": apevSensor,
       "apevSensorUnknown": apevSensorUnknown,
       "apevSensorTemperature": apevSensorTemperature,
       "apevSensorVoltage": apevSensorVoltage,
       "apevSensorFanSpeed": apevSensorFanSpeed,
       "apevModule": apevModule,
       "apevModuleUnknown": apevModuleUnknown,
       "apevModulePHYCard": apevModulePHYCard,
       "apevPHYCardUnknown": apevPHYCardUnknown,
       "apevPHY1GigPortMultiMode": apevPHY1GigPortMultiMode,
       "apevPHY1GigPortSingleMode": apevPHY1GigPortSingleMode,
       "apevPHY2GigPortstMultiMode": apevPHY2GigPortstMultiMode,
       "apevPHY2GigPortsSingleMode": apevPHY2GigPortsSingleMode,
       "apecPHY4FEPorts": apecPHY4FEPorts,
       "apevPHY4FEPorts1089": apevPHY4FEPorts1089,
       "apevPHY2GigPortsSec": apevPHY2GigPortsSec,
       "apevPHY2FEPortsSec": apevPHY2FEPortsSec,
       "apevPHY4GigPorts": apevPHY4GigPorts,
       "apevPHY4SFPPorts": apevPHY4SFPPorts,
       "apevPHY44SFPPortsSecQos": apevPHY44SFPPortsSecQos,
       "apevPHY4SFPPortsQos": apevPHY4SFPPortsQos,
       "apevPHY4SFPPortsSec": apevPHY4SFPPortsSec,
       "apevPHY8FEPorts": apevPHY8FEPorts,
       "apevPHY4SFPPortsSecQosCav": apevPHY4SFPPortsSecQosCav,
       "apevModuleCAM": apevModuleCAM,
       "apevModuleCAMUnknown": apevModuleCAMUnknown,
       "apevModuleCAMAMCC": apevModuleCAMAMCC,
       "apevModuleCAMIDT": apevModuleCAMIDT,
       "apevModuleHostProcessor": apevModuleHostProcessor,
       "apevModuleHPUnknown": apevModuleHPUnknown,
       "apevModuleHP7451": apevModuleHP7451,
       "apevModuleHP7455": apevModuleHP7455,
       "apevModuleHP7457": apevModuleHP7457,
       "apevHP7457Unknown": apevHP7457Unknown,
       "apevHP7457DC8MB": apevHP7457DC8MB,
       "apevHP7457DC4MB": apevHP7457DC4MB,
       "apevHP7457AC8MB": apevHP7457AC8MB,
       "apevHP7457AC4MB": apevHP7457AC4MB,
       "apevHP7457ACDC8MB": apevHP7457ACDC8MB,
       "apevModuleHPT2500": apevModuleHPT2500,
       "apevModuleHPCeleron": apevModuleHPCeleron,
       "apevModuleHPT9400": apevModuleHPT9400,
       "apevModulePMC": apevModulePMC,
       "apevModulePMCUnknown": apevModulePMCUnknown,
       "apevModulePCMCIA": apevModulePCMCIA,
       "apevModulePCMCIAUnknown": apevModulePCMCIAUnknown,
       "apevModulePCMCIAATA": apevModulePCMCIAATA,
       "apevModulePCMCIALinear": apevModulePCMCIALinear,
       "apevModuleMemory": apevModuleMemory,
       "apevModuleMemoryUnknown": apevModuleMemoryUnknown,
       "apevModuleMemory1G": apevModuleMemory1G,
       "apevModuleMemory4G": apevModuleMemory4G,
       "apevModuleCard": apevModuleCard,
       "apevModuleSPU": apevModuleSPU,
       "apevModuleNPU": apevModuleNPU,
       "apevModuleTCU": apevModuleTCU,
       "apevModuleMIU": apevModuleMIU,
       "apevModulePHY": apevModulePHY,
       "apevModuleTLS": apevModuleTLS,
       "apevPort": apevPort,
       "apevPortUnknown": apevPortUnknown,
       "apevPortGigE": apevPortGigE,
       "apevPortFE": apevPortFE,
       "apevPort2Gig": apevPort2Gig,
       "apevPortMMFiber": apevPortMMFiber,
       "apevPortSMFiber": apevPortSMFiber,
       "apevPort10GFiber": apevPort10GFiber,
       "apevStack": apevStack}
)
