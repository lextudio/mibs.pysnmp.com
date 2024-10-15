# SNMP MIB module (NETI-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:30 2024
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

netinsight = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928)
)
netinsight.setRevisions(
        ("2014-10-23 13:00",
         "2014-04-01 10:00",
         "2013-10-10 09:00",
         "2013-06-03 11:00",
         "2013-01-30 13:00",
         "2012-09-12 11:00",
         "2012-03-22 09:20",
         "2012-03-16 13:00",
         "2011-03-25 14:00",
         "2010-11-10 08:00",
         "2010-02-04 15:00",
         "2008-12-19 14:00",
         "2008-12-12 13:00",
         "2008-10-15 12:00",
         "2008-06-19 10:00",
         "2007-07-31 15:00",
         "2007-01-26 11:00",
         "2006-08-17 08:30",
         "2005-12-15 00:00",
         "2003-03-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FaultStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("ok", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NetiReg_ObjectIdentity = ObjectIdentity
netiReg = _NetiReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1)
)
_NimbraOne_ObjectIdentity = ObjectIdentity
nimbraOne = _NimbraOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1)
)
_NimbraOneChassisTypes_ObjectIdentity = ObjectIdentity
nimbraOneChassisTypes = _NimbraOneChassisTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 1)
)
_NimbraOneBaseUnit_ObjectIdentity = ObjectIdentity
nimbraOneBaseUnit = _NimbraOneBaseUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 1, 1)
)
_NimbraOneBackplaneTypes_ObjectIdentity = ObjectIdentity
nimbraOneBackplaneTypes = _NimbraOneBackplaneTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 2)
)
_NimbraOneBackplane_ObjectIdentity = ObjectIdentity
nimbraOneBackplane = _NimbraOneBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 2, 1)
)
_NimbraOneContainerTypes_ObjectIdentity = ObjectIdentity
nimbraOneContainerTypes = _NimbraOneContainerTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 3)
)
_NimbraOneSlot_ObjectIdentity = ObjectIdentity
nimbraOneSlot = _NimbraOneSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 3, 1)
)
_NimbraOnePowerSupplyTypes_ObjectIdentity = ObjectIdentity
nimbraOnePowerSupplyTypes = _NimbraOnePowerSupplyTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 4)
)
_NimbraOnePowerSupply_ObjectIdentity = ObjectIdentity
nimbraOnePowerSupply = _NimbraOnePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 4, 1)
)
_NimbraOneFanTypes_ObjectIdentity = ObjectIdentity
nimbraOneFanTypes = _NimbraOneFanTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 5)
)
_NimbraOneFan_ObjectIdentity = ObjectIdentity
nimbraOneFan = _NimbraOneFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 5, 1)
)
_NimbraOneModuleTypes_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypes = _NimbraOneModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6)
)
_NimbraOneModuleTypesMgmt_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesMgmt = _NimbraOneModuleTypesMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 1)
)
_NimbraOneModuleTypesMgmtControlModule_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesMgmtControlModule = _NimbraOneModuleTypesMgmtControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 1, 1)
)
_NimbraOneModuleTypesDtm_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm = _NimbraOneModuleTypesDtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2)
)
_NimbraOneModuleTypesDtm850ShortHaulRight_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm850ShortHaulRight = _NimbraOneModuleTypesDtm850ShortHaulRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 1)
)
_NimbraOneModuleTypesDtm850ShortHaulLeft_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm850ShortHaulLeft = _NimbraOneModuleTypesDtm850ShortHaulLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 2)
)
_NimbraOneModuleTypesDtm850LongHaulRight_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm850LongHaulRight = _NimbraOneModuleTypesDtm850LongHaulRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 3)
)
_NimbraOneModuleTypesDtm850LongHaulLeft_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm850LongHaulLeft = _NimbraOneModuleTypesDtm850LongHaulLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 4)
)
_NimbraOneModuleTypesDtm1000ShortHaulRight_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm1000ShortHaulRight = _NimbraOneModuleTypesDtm1000ShortHaulRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 5)
)
_NimbraOneModuleTypesDtm1000ShortHaulLeft_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm1000ShortHaulLeft = _NimbraOneModuleTypesDtm1000ShortHaulLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 6)
)
_NimbraOneModuleTypesDtm1000LongHaulRight_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm1000LongHaulRight = _NimbraOneModuleTypesDtm1000LongHaulRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 7)
)
_NimbraOneModuleTypesDtm1000LongHaulLeft_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm1000LongHaulLeft = _NimbraOneModuleTypesDtm1000LongHaulLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 8)
)
_NimbraOneModuleTypesDtm150Right_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm150Right = _NimbraOneModuleTypesDtm150Right_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 9)
)
_NimbraOneModuleTypesDtm150Left_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm150Left = _NimbraOneModuleTypesDtm150Left_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 10)
)
_NimbraOneModuleTypesDtm622_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesDtm622 = _NimbraOneModuleTypesDtm622_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 11)
)
_NimbraOneModuleTypesTrunk1Gbps_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunk1Gbps = _NimbraOneModuleTypesTrunk1Gbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 12)
)
_NimbraOneModuleTypesTrunkDS3_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunkDS3 = _NimbraOneModuleTypesTrunkDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 13)
)
_NimbraOneModuleTypesTrunkOC3_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunkOC3 = _NimbraOneModuleTypesTrunkOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 14)
)
_NimbraOneModuleTypesTrunk4xOC3_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunk4xOC3 = _NimbraOneModuleTypesTrunk4xOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 15)
)
_NimbraOneModuleTypesTrunkOC12_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunkOC12 = _NimbraOneModuleTypesTrunkOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 16)
)
_NimbraOneModuleTypesTrunkOC48_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunkOC48 = _NimbraOneModuleTypesTrunkOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 17)
)
_NimbraOneModuleTypesTrunk3xIP_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunk3xIP = _NimbraOneModuleTypesTrunk3xIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 2, 18)
)
_NimbraOneModuleTypesAccess_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccess = _NimbraOneModuleTypesAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3)
)
_NimbraOneModuleTypesAccessE1Right_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessE1Right = _NimbraOneModuleTypesAccessE1Right_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 1)
)
_NimbraOneModuleTypesAccessE1Left_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessE1Left = _NimbraOneModuleTypesAccessE1Left_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 2)
)
_NimbraOneModuleTypesAccessT1Right_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessT1Right = _NimbraOneModuleTypesAccessT1Right_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 3)
)
_NimbraOneModuleTypesAccessT1Left_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessT1Left = _NimbraOneModuleTypesAccessT1Left_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 4)
)
_NimbraOneModuleTypesAccessVideo270Right_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessVideo270Right = _NimbraOneModuleTypesAccessVideo270Right_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 5)
)
_NimbraOneModuleTypesAccessVideo270Left_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessVideo270Left = _NimbraOneModuleTypesAccessVideo270Left_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 6)
)
_NimbraOneModuleTypesAccessEthernet8pRight_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessEthernet8pRight = _NimbraOneModuleTypesAccessEthernet8pRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 7)
)
_NimbraOneModuleTypesAccessEthernet8pLeft_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessEthernet8pLeft = _NimbraOneModuleTypesAccessEthernet8pLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 8)
)
_NimbraOneModuleTypesAccessGigabitEthernet_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessGigabitEthernet = _NimbraOneModuleTypesAccessGigabitEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 9)
)
_NimbraOneModuleTypesAccessASIRight_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessASIRight = _NimbraOneModuleTypesAccessASIRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 11)
)
_NimbraOneModuleTypesAccessASILeft_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessASILeft = _NimbraOneModuleTypesAccessASILeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 12)
)
_NimbraOneModuleTypesAccessGbE_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessGbE = _NimbraOneModuleTypesAccessGbE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 13)
)
_NimbraOneModuleTypesAccess8xEth_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccess8xEth = _NimbraOneModuleTypesAccess8xEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 14)
)
_NimbraOneModuleTypesAccessASI_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessASI = _NimbraOneModuleTypesAccessASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 15)
)
_NimbraOneModuleTypesAccessSDI_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessSDI = _NimbraOneModuleTypesAccessSDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 16)
)
_NimbraOneModuleTypesAccess4xOC3_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccess4xOC3 = _NimbraOneModuleTypesAccess4xOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 17)
)
_NimbraOneModuleTypesAccessE1_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessE1 = _NimbraOneModuleTypesAccessE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 18)
)
_NimbraOneModuleTypesAccessT1_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccessT1 = _NimbraOneModuleTypesAccessT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 19)
)
_NimbraOneModuleTypesAccess8xASI_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccess8xASI = _NimbraOneModuleTypesAccess8xASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 20)
)
_NimbraOneModuleTypesAccess8xAESEBU_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAccess8xAESEBU = _NimbraOneModuleTypesAccess8xAESEBU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 3, 21)
)
_NimbraOneModuleTypesTrunkAccess_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunkAccess = _NimbraOneModuleTypesTrunkAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 4)
)
_NimbraOneModuleTypesTrunkAccess4xDS3E3_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesTrunkAccess4xDS3E3 = _NimbraOneModuleTypesTrunkAccess4xDS3E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 4, 1)
)
_NimbraOneModuleTypesAux_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAux = _NimbraOneModuleTypesAux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 5)
)
_NimbraOneModuleTypesAuxGPIO_ObjectIdentity = ObjectIdentity
nimbraOneModuleTypesAuxGPIO = _NimbraOneModuleTypesAuxGPIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 6, 5, 1)
)
_NimbraOneThermometerTypes_ObjectIdentity = ObjectIdentity
nimbraOneThermometerTypes = _NimbraOneThermometerTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 7)
)
_NimbraOneThermometer_ObjectIdentity = ObjectIdentity
nimbraOneThermometer = _NimbraOneThermometer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 1, 7, 1)
)
_Nimbra101_ObjectIdentity = ObjectIdentity
nimbra101 = _Nimbra101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 2)
)
_Nimbra210_ObjectIdentity = ObjectIdentity
nimbra210 = _Nimbra210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 3)
)
_Nimbra220_ObjectIdentity = ObjectIdentity
nimbra220 = _Nimbra220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 4)
)
_Nimbra290_ObjectIdentity = ObjectIdentity
nimbra290 = _Nimbra290_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5)
)
_Nimbra290ChassisTypes_ObjectIdentity = ObjectIdentity
nimbra290ChassisTypes = _Nimbra290ChassisTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5, 1)
)
_Nimbra290BaseUnit_ObjectIdentity = ObjectIdentity
nimbra290BaseUnit = _Nimbra290BaseUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5, 1, 1)
)
_Nimbra290PowerSupplyTypes_ObjectIdentity = ObjectIdentity
nimbra290PowerSupplyTypes = _Nimbra290PowerSupplyTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5, 2)
)
_Nimbra290PowerUnit_ObjectIdentity = ObjectIdentity
nimbra290PowerUnit = _Nimbra290PowerUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5, 2, 1)
)
_Nimbra290FanTypes_ObjectIdentity = ObjectIdentity
nimbra290FanTypes = _Nimbra290FanTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5, 3)
)
_Nimbra290Fan_ObjectIdentity = ObjectIdentity
nimbra290Fan = _Nimbra290Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 5, 3, 1)
)
_NimbraTwo_ObjectIdentity = ObjectIdentity
nimbraTwo = _NimbraTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 6)
)
_NetiRegGeneric_ObjectIdentity = ObjectIdentity
netiRegGeneric = _NetiRegGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 7)
)
_Nimbra291_ObjectIdentity = ObjectIdentity
nimbra291 = _Nimbra291_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 8)
)
_Nimbra340_ObjectIdentity = ObjectIdentity
nimbra340 = _Nimbra340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9)
)
_Nimbra340ChassisTypes_ObjectIdentity = ObjectIdentity
nimbra340ChassisTypes = _Nimbra340ChassisTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 1)
)
_Nimbra340ContainerTypes_ObjectIdentity = ObjectIdentity
nimbra340ContainerTypes = _Nimbra340ContainerTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 3)
)
_Nimbra340PowerSupplyTypes_ObjectIdentity = ObjectIdentity
nimbra340PowerSupplyTypes = _Nimbra340PowerSupplyTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 4)
)
_Nimbra340FanTypes_ObjectIdentity = ObjectIdentity
nimbra340FanTypes = _Nimbra340FanTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 5)
)
_Nimbra340ModuleTypes_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypes = _Nimbra340ModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6)
)
_Nimbra340ModuleTypesMgmt_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesMgmt = _Nimbra340ModuleTypesMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 1)
)
_Nimbra340ModuleTypesMgmtControlModule_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesMgmtControlModule = _Nimbra340ModuleTypesMgmtControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 1, 1)
)
_Nimbra340ModuleTypesDtm_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesDtm = _Nimbra340ModuleTypesDtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2)
)
_Nimbra340ModuleTypesTrunk1Gbps_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunk1Gbps = _Nimbra340ModuleTypesTrunk1Gbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 1)
)
_Nimbra340ModuleTypesTrunkDS3_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunkDS3 = _Nimbra340ModuleTypesTrunkDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 2)
)
_Nimbra340ModuleTypesTrunkOC3_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunkOC3 = _Nimbra340ModuleTypesTrunkOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 3)
)
_Nimbra340ModuleTypesTrunk4xOC3_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunk4xOC3 = _Nimbra340ModuleTypesTrunk4xOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 4)
)
_Nimbra340ModuleTypesTrunkOC12_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunkOC12 = _Nimbra340ModuleTypesTrunkOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 5)
)
_Nimbra340ModuleTypesTrunkOC48_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunkOC48 = _Nimbra340ModuleTypesTrunkOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 6)
)
_Nimbra340ModuleTypesTrunk3xIP_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunk3xIP = _Nimbra340ModuleTypesTrunk3xIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 2, 7)
)
_Nimbra340ModuleTypesAccess_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccess = _Nimbra340ModuleTypesAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3)
)
_Nimbra340ModuleTypesAccessGbE_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccessGbE = _Nimbra340ModuleTypesAccessGbE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 1)
)
_Nimbra340ModuleTypesAccess8xEth_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccess8xEth = _Nimbra340ModuleTypesAccess8xEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 2)
)
_Nimbra340ModuleTypesAccessASI_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccessASI = _Nimbra340ModuleTypesAccessASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 3)
)
_Nimbra340ModuleTypesAccessSDI_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccessSDI = _Nimbra340ModuleTypesAccessSDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 4)
)
_Nimbra340ModuleTypesAccess4xOC3_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccess4xOC3 = _Nimbra340ModuleTypesAccess4xOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 5)
)
_Nimbra340ModuleTypesAccessE1_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccessE1 = _Nimbra340ModuleTypesAccessE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 6)
)
_Nimbra340ModuleTypesAccessT1_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccessT1 = _Nimbra340ModuleTypesAccessT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 7)
)
_Nimbra340ModuleTypesAccess8xASI_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccess8xASI = _Nimbra340ModuleTypesAccess8xASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 8)
)
_Nimbra340ModuleTypesAccessHDSDI_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccessHDSDI = _Nimbra340ModuleTypesAccessHDSDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 9)
)
_Nimbra340ModuleTypesAccess8xAESEBU_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccess8xAESEBU = _Nimbra340ModuleTypesAccess8xAESEBU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 10)
)
_Nimbra340ModuleTypesAccess8xSDI_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAccess8xSDI = _Nimbra340ModuleTypesAccess8xSDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 3, 11)
)
_Nimbra360ModuleTypesDtm_ObjectIdentity = ObjectIdentity
nimbra360ModuleTypesDtm = _Nimbra360ModuleTypesDtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 4)
)
_Nimbra360ModuleTypesTrunkFunction_ObjectIdentity = ObjectIdentity
nimbra360ModuleTypesTrunkFunction = _Nimbra360ModuleTypesTrunkFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 4, 1)
)
_Nimbra340ModuleTypesAux_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAux = _Nimbra340ModuleTypesAux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 5)
)
_Nimbra340ModuleTypesAuxGPIO_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesAuxGPIO = _Nimbra340ModuleTypesAuxGPIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 5, 1)
)
_Nimbra340ModuleTypesTrunkAccess_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunkAccess = _Nimbra340ModuleTypesTrunkAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 6)
)
_Nimbra340ModuleTypesTrunkAccess4xDS3E3_ObjectIdentity = ObjectIdentity
nimbra340ModuleTypesTrunkAccess4xDS3E3 = _Nimbra340ModuleTypesTrunkAccess4xDS3E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 6, 1)
)
_Nimbra380ModuleTypesAccess_ObjectIdentity = ObjectIdentity
nimbra380ModuleTypesAccess = _Nimbra380ModuleTypesAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 7)
)
_Nimbra380ModuleTypesAccess8xGbE_ObjectIdentity = ObjectIdentity
nimbra380ModuleTypesAccess8xGbE = _Nimbra380ModuleTypesAccess8xGbE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 6, 7, 1)
)
_Nimbra340ThermometerTypes_ObjectIdentity = ObjectIdentity
nimbra340ThermometerTypes = _Nimbra340ThermometerTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 7)
)
_Nimbra340Thermometer_ObjectIdentity = ObjectIdentity
nimbra340Thermometer = _Nimbra340Thermometer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 9, 7, 1)
)
_Nimbra680_ObjectIdentity = ObjectIdentity
nimbra680 = _Nimbra680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10)
)
_Nimbra680ChassisTypes_ObjectIdentity = ObjectIdentity
nimbra680ChassisTypes = _Nimbra680ChassisTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 1)
)
_Nimbra680ContainerTypes_ObjectIdentity = ObjectIdentity
nimbra680ContainerTypes = _Nimbra680ContainerTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 3)
)
_Nimbra680PowerSupplyTypes_ObjectIdentity = ObjectIdentity
nimbra680PowerSupplyTypes = _Nimbra680PowerSupplyTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 4)
)
_Nimbra680PowerSupplyTypesPCU_ObjectIdentity = ObjectIdentity
nimbra680PowerSupplyTypesPCU = _Nimbra680PowerSupplyTypesPCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 4, 1)
)
_Nimbra680PowerSupplyTypesPSU_ObjectIdentity = ObjectIdentity
nimbra680PowerSupplyTypesPSU = _Nimbra680PowerSupplyTypesPSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 4, 2)
)
_Nimbra680FanTypes_ObjectIdentity = ObjectIdentity
nimbra680FanTypes = _Nimbra680FanTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 5)
)
_Nimbra680FanTypesFan_ObjectIdentity = ObjectIdentity
nimbra680FanTypesFan = _Nimbra680FanTypesFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 5, 1)
)
_Nimbra680ModuleTypes_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypes = _Nimbra680ModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6)
)
_Nimbra680ModuleTypesMgmt_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesMgmt = _Nimbra680ModuleTypesMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 1)
)
_Nimbra680ModuleTypesMgmtControlModule_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesMgmtControlModule = _Nimbra680ModuleTypesMgmtControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 1, 1)
)
_Nimbra680ModuleTypesIf_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIf = _Nimbra680ModuleTypesIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2)
)
_Nimbra680ModuleTypesIfTrunk4xOC3_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIfTrunk4xOC3 = _Nimbra680ModuleTypesIfTrunk4xOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 1)
)
_Nimbra680ModuleTypesIfTrunk4xOC12_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIfTrunk4xOC12 = _Nimbra680ModuleTypesIfTrunk4xOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 2)
)
_Nimbra680ModuleTypesIfTrunk2xOC48_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIfTrunk2xOC48 = _Nimbra680ModuleTypesIfTrunk2xOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 3)
)
_Nimbra680ModuleTypesIfTrunk4xOC48_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIfTrunk4xOC48 = _Nimbra680ModuleTypesIfTrunk4xOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 4)
)
_Nimbra680ModuleTypesIfTrunkOC192_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIfTrunkOC192 = _Nimbra680ModuleTypesIfTrunkOC192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 5)
)
_Nimbra680ModuleTypesIfTrunk6xIP_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesIfTrunk6xIP = _Nimbra680ModuleTypesIfTrunk6xIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 2, 6)
)
_Nimbra680ModuleTypesSwitch_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesSwitch = _Nimbra680ModuleTypesSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3)
)
_Nimbra680ModuleTypesSwitch40Gbps_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesSwitch40Gbps = _Nimbra680ModuleTypesSwitch40Gbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3, 1)
)
_Nimbra680ModuleTypesSwitch80Gbps_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesSwitch80Gbps = _Nimbra680ModuleTypesSwitch80Gbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3, 2)
)
_Nimbra680ModuleTypesSwitch160Gbps_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesSwitch160Gbps = _Nimbra680ModuleTypesSwitch160Gbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 3, 3)
)
_Nimbra680ModuleTypesAccess_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess = _Nimbra680ModuleTypesAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4)
)
_Nimbra680ModuleTypesAccess8xHDSDI_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8xHDSDI = _Nimbra680ModuleTypesAccess8xHDSDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 1)
)
_Nimbra680ModuleTypesAccess8xGbE_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8xGbE = _Nimbra680ModuleTypesAccess8xGbE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 2)
)
_Nimbra680ModuleTypesAccess8xASI_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8xASI = _Nimbra680ModuleTypesAccess8xASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 3)
)
_Nimbra680ModuleTypesAccess8x3Gbps_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8x3Gbps = _Nimbra680ModuleTypesAccess8x3Gbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 4)
)
_Nimbra680ModuleTypesAccess8xJPEG2000_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8xJPEG2000 = _Nimbra680ModuleTypesAccess8xJPEG2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 5)
)
_Nimbra680ModuleTypesAccess8xVideo_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8xVideo = _Nimbra680ModuleTypesAccess8xVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 6)
)
_Nimbra680ModuleTypesAccess8xASIAES_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess8xASIAES = _Nimbra680ModuleTypesAccess8xASIAES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 7)
)
_Nimbra680ModuleTypesAccess2x10GbE_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAccess2x10GbE = _Nimbra680ModuleTypesAccess2x10GbE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 4, 8)
)
_Nimbra680ModuleTypesAux_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAux = _Nimbra680ModuleTypesAux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 5)
)
_Nimbra680ModuleTypesAuxGPIO_ObjectIdentity = ObjectIdentity
nimbra680ModuleTypesAuxGPIO = _Nimbra680ModuleTypesAuxGPIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 6, 5, 1)
)
_Nimbra680ThermometerTypes_ObjectIdentity = ObjectIdentity
nimbra680ThermometerTypes = _Nimbra680ThermometerTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 7)
)
_Nimbra680Thermometer_ObjectIdentity = ObjectIdentity
nimbra680Thermometer = _Nimbra680Thermometer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 10, 7, 1)
)
_Nimbra340HD_ObjectIdentity = ObjectIdentity
nimbra340HD = _Nimbra340HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 11)
)
_Nimbra360_ObjectIdentity = ObjectIdentity
nimbra360 = _Nimbra360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 12)
)
_Nimbra360Gold_ObjectIdentity = ObjectIdentity
nimbra360Gold = _Nimbra360Gold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 12, 1)
)
_Nimbra688_ObjectIdentity = ObjectIdentity
nimbra688 = _Nimbra688_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 13)
)
_Nimbra130_ObjectIdentity = ObjectIdentity
nimbra130 = _Nimbra130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 14)
)
_Nimbra380_ObjectIdentity = ObjectIdentity
nimbra380 = _Nimbra380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 15)
)
_Nimbra230_ObjectIdentity = ObjectIdentity
nimbra230 = _Nimbra230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 16)
)
_Nimbra320_ObjectIdentity = ObjectIdentity
nimbra320 = _Nimbra320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 17)
)
_Nimbra140_ObjectIdentity = ObjectIdentity
nimbra140 = _Nimbra140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 18)
)
_Nimbra310_ObjectIdentity = ObjectIdentity
nimbra310 = _Nimbra310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 19)
)
_Nimbra240_ObjectIdentity = ObjectIdentity
nimbra240 = _Nimbra240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 20)
)
_Nimbra640_ObjectIdentity = ObjectIdentity
nimbra640 = _Nimbra640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 21)
)
_NimbraVA210_ObjectIdentity = ObjectIdentity
nimbraVA210 = _NimbraVA210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 22)
)
_NimbraVA210FV_ObjectIdentity = ObjectIdentity
nimbraVA210FV = _NimbraVA210FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 22, 1)
)
_NimbraVA210DCV1_ObjectIdentity = ObjectIdentity
nimbraVA210DCV1 = _NimbraVA210DCV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 22, 2)
)
_NimbraVA210DCV2_ObjectIdentity = ObjectIdentity
nimbraVA210DCV2 = _NimbraVA210DCV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 22, 3)
)
_Nimbra390_ObjectIdentity = ObjectIdentity
nimbra390 = _Nimbra390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 23)
)
_NimbraVA220_ObjectIdentity = ObjectIdentity
nimbraVA220 = _NimbraVA220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 1, 25)
)
_NetiGeneric_ObjectIdentity = ObjectIdentity
netiGeneric = _NetiGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2)
)
_NetiProducts_ObjectIdentity = ObjectIdentity
netiProducts = _NetiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 3)
)
_Nimbravision_ObjectIdentity = ObjectIdentity
nimbravision = _Nimbravision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 3, 1)
)
_ProdNimbra230_ObjectIdentity = ObjectIdentity
prodNimbra230 = _ProdNimbra230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 3, 2)
)
_NetiCaps_ObjectIdentity = ObjectIdentity
netiCaps = _NetiCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 4)
)
_NetiReqs_ObjectIdentity = ObjectIdentity
netiReqs = _NetiReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 5)
)
_NetiExperimental_ObjectIdentity = ObjectIdentity
netiExperimental = _NetiExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6)
)
_NetiExperimentalReg_ObjectIdentity = ObjectIdentity
netiExperimentalReg = _NetiExperimentalReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 1)
)
_NetiExperimentalGeneric_ObjectIdentity = ObjectIdentity
netiExperimentalGeneric = _NetiExperimentalGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2)
)
_NetiExperimentalProducts_ObjectIdentity = ObjectIdentity
netiExperimentalProducts = _NetiExperimentalProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 3)
)
_NetiExperimentalCaps_ObjectIdentity = ObjectIdentity
netiExperimentalCaps = _NetiExperimentalCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 4)
)
_NetiExperimentalReqs_ObjectIdentity = ObjectIdentity
netiExperimentalReqs = _NetiExperimentalReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-COMMON-MIB",
    **{"FaultStatus": FaultStatus,
       "netinsight": netinsight,
       "netiReg": netiReg,
       "nimbraOne": nimbraOne,
       "nimbraOneChassisTypes": nimbraOneChassisTypes,
       "nimbraOneBaseUnit": nimbraOneBaseUnit,
       "nimbraOneBackplaneTypes": nimbraOneBackplaneTypes,
       "nimbraOneBackplane": nimbraOneBackplane,
       "nimbraOneContainerTypes": nimbraOneContainerTypes,
       "nimbraOneSlot": nimbraOneSlot,
       "nimbraOnePowerSupplyTypes": nimbraOnePowerSupplyTypes,
       "nimbraOnePowerSupply": nimbraOnePowerSupply,
       "nimbraOneFanTypes": nimbraOneFanTypes,
       "nimbraOneFan": nimbraOneFan,
       "nimbraOneModuleTypes": nimbraOneModuleTypes,
       "nimbraOneModuleTypesMgmt": nimbraOneModuleTypesMgmt,
       "nimbraOneModuleTypesMgmtControlModule": nimbraOneModuleTypesMgmtControlModule,
       "nimbraOneModuleTypesDtm": nimbraOneModuleTypesDtm,
       "nimbraOneModuleTypesDtm850ShortHaulRight": nimbraOneModuleTypesDtm850ShortHaulRight,
       "nimbraOneModuleTypesDtm850ShortHaulLeft": nimbraOneModuleTypesDtm850ShortHaulLeft,
       "nimbraOneModuleTypesDtm850LongHaulRight": nimbraOneModuleTypesDtm850LongHaulRight,
       "nimbraOneModuleTypesDtm850LongHaulLeft": nimbraOneModuleTypesDtm850LongHaulLeft,
       "nimbraOneModuleTypesDtm1000ShortHaulRight": nimbraOneModuleTypesDtm1000ShortHaulRight,
       "nimbraOneModuleTypesDtm1000ShortHaulLeft": nimbraOneModuleTypesDtm1000ShortHaulLeft,
       "nimbraOneModuleTypesDtm1000LongHaulRight": nimbraOneModuleTypesDtm1000LongHaulRight,
       "nimbraOneModuleTypesDtm1000LongHaulLeft": nimbraOneModuleTypesDtm1000LongHaulLeft,
       "nimbraOneModuleTypesDtm150Right": nimbraOneModuleTypesDtm150Right,
       "nimbraOneModuleTypesDtm150Left": nimbraOneModuleTypesDtm150Left,
       "nimbraOneModuleTypesDtm622": nimbraOneModuleTypesDtm622,
       "nimbraOneModuleTypesTrunk1Gbps": nimbraOneModuleTypesTrunk1Gbps,
       "nimbraOneModuleTypesTrunkDS3": nimbraOneModuleTypesTrunkDS3,
       "nimbraOneModuleTypesTrunkOC3": nimbraOneModuleTypesTrunkOC3,
       "nimbraOneModuleTypesTrunk4xOC3": nimbraOneModuleTypesTrunk4xOC3,
       "nimbraOneModuleTypesTrunkOC12": nimbraOneModuleTypesTrunkOC12,
       "nimbraOneModuleTypesTrunkOC48": nimbraOneModuleTypesTrunkOC48,
       "nimbraOneModuleTypesTrunk3xIP": nimbraOneModuleTypesTrunk3xIP,
       "nimbraOneModuleTypesAccess": nimbraOneModuleTypesAccess,
       "nimbraOneModuleTypesAccessE1Right": nimbraOneModuleTypesAccessE1Right,
       "nimbraOneModuleTypesAccessE1Left": nimbraOneModuleTypesAccessE1Left,
       "nimbraOneModuleTypesAccessT1Right": nimbraOneModuleTypesAccessT1Right,
       "nimbraOneModuleTypesAccessT1Left": nimbraOneModuleTypesAccessT1Left,
       "nimbraOneModuleTypesAccessVideo270Right": nimbraOneModuleTypesAccessVideo270Right,
       "nimbraOneModuleTypesAccessVideo270Left": nimbraOneModuleTypesAccessVideo270Left,
       "nimbraOneModuleTypesAccessEthernet8pRight": nimbraOneModuleTypesAccessEthernet8pRight,
       "nimbraOneModuleTypesAccessEthernet8pLeft": nimbraOneModuleTypesAccessEthernet8pLeft,
       "nimbraOneModuleTypesAccessGigabitEthernet": nimbraOneModuleTypesAccessGigabitEthernet,
       "nimbraOneModuleTypesAccessASIRight": nimbraOneModuleTypesAccessASIRight,
       "nimbraOneModuleTypesAccessASILeft": nimbraOneModuleTypesAccessASILeft,
       "nimbraOneModuleTypesAccessGbE": nimbraOneModuleTypesAccessGbE,
       "nimbraOneModuleTypesAccess8xEth": nimbraOneModuleTypesAccess8xEth,
       "nimbraOneModuleTypesAccessASI": nimbraOneModuleTypesAccessASI,
       "nimbraOneModuleTypesAccessSDI": nimbraOneModuleTypesAccessSDI,
       "nimbraOneModuleTypesAccess4xOC3": nimbraOneModuleTypesAccess4xOC3,
       "nimbraOneModuleTypesAccessE1": nimbraOneModuleTypesAccessE1,
       "nimbraOneModuleTypesAccessT1": nimbraOneModuleTypesAccessT1,
       "nimbraOneModuleTypesAccess8xASI": nimbraOneModuleTypesAccess8xASI,
       "nimbraOneModuleTypesAccess8xAESEBU": nimbraOneModuleTypesAccess8xAESEBU,
       "nimbraOneModuleTypesTrunkAccess": nimbraOneModuleTypesTrunkAccess,
       "nimbraOneModuleTypesTrunkAccess4xDS3E3": nimbraOneModuleTypesTrunkAccess4xDS3E3,
       "nimbraOneModuleTypesAux": nimbraOneModuleTypesAux,
       "nimbraOneModuleTypesAuxGPIO": nimbraOneModuleTypesAuxGPIO,
       "nimbraOneThermometerTypes": nimbraOneThermometerTypes,
       "nimbraOneThermometer": nimbraOneThermometer,
       "nimbra101": nimbra101,
       "nimbra210": nimbra210,
       "nimbra220": nimbra220,
       "nimbra290": nimbra290,
       "nimbra290ChassisTypes": nimbra290ChassisTypes,
       "nimbra290BaseUnit": nimbra290BaseUnit,
       "nimbra290PowerSupplyTypes": nimbra290PowerSupplyTypes,
       "nimbra290PowerUnit": nimbra290PowerUnit,
       "nimbra290FanTypes": nimbra290FanTypes,
       "nimbra290Fan": nimbra290Fan,
       "nimbraTwo": nimbraTwo,
       "netiRegGeneric": netiRegGeneric,
       "nimbra291": nimbra291,
       "nimbra340": nimbra340,
       "nimbra340ChassisTypes": nimbra340ChassisTypes,
       "nimbra340ContainerTypes": nimbra340ContainerTypes,
       "nimbra340PowerSupplyTypes": nimbra340PowerSupplyTypes,
       "nimbra340FanTypes": nimbra340FanTypes,
       "nimbra340ModuleTypes": nimbra340ModuleTypes,
       "nimbra340ModuleTypesMgmt": nimbra340ModuleTypesMgmt,
       "nimbra340ModuleTypesMgmtControlModule": nimbra340ModuleTypesMgmtControlModule,
       "nimbra340ModuleTypesDtm": nimbra340ModuleTypesDtm,
       "nimbra340ModuleTypesTrunk1Gbps": nimbra340ModuleTypesTrunk1Gbps,
       "nimbra340ModuleTypesTrunkDS3": nimbra340ModuleTypesTrunkDS3,
       "nimbra340ModuleTypesTrunkOC3": nimbra340ModuleTypesTrunkOC3,
       "nimbra340ModuleTypesTrunk4xOC3": nimbra340ModuleTypesTrunk4xOC3,
       "nimbra340ModuleTypesTrunkOC12": nimbra340ModuleTypesTrunkOC12,
       "nimbra340ModuleTypesTrunkOC48": nimbra340ModuleTypesTrunkOC48,
       "nimbra340ModuleTypesTrunk3xIP": nimbra340ModuleTypesTrunk3xIP,
       "nimbra340ModuleTypesAccess": nimbra340ModuleTypesAccess,
       "nimbra340ModuleTypesAccessGbE": nimbra340ModuleTypesAccessGbE,
       "nimbra340ModuleTypesAccess8xEth": nimbra340ModuleTypesAccess8xEth,
       "nimbra340ModuleTypesAccessASI": nimbra340ModuleTypesAccessASI,
       "nimbra340ModuleTypesAccessSDI": nimbra340ModuleTypesAccessSDI,
       "nimbra340ModuleTypesAccess4xOC3": nimbra340ModuleTypesAccess4xOC3,
       "nimbra340ModuleTypesAccessE1": nimbra340ModuleTypesAccessE1,
       "nimbra340ModuleTypesAccessT1": nimbra340ModuleTypesAccessT1,
       "nimbra340ModuleTypesAccess8xASI": nimbra340ModuleTypesAccess8xASI,
       "nimbra340ModuleTypesAccessHDSDI": nimbra340ModuleTypesAccessHDSDI,
       "nimbra340ModuleTypesAccess8xAESEBU": nimbra340ModuleTypesAccess8xAESEBU,
       "nimbra340ModuleTypesAccess8xSDI": nimbra340ModuleTypesAccess8xSDI,
       "nimbra360ModuleTypesDtm": nimbra360ModuleTypesDtm,
       "nimbra360ModuleTypesTrunkFunction": nimbra360ModuleTypesTrunkFunction,
       "nimbra340ModuleTypesAux": nimbra340ModuleTypesAux,
       "nimbra340ModuleTypesAuxGPIO": nimbra340ModuleTypesAuxGPIO,
       "nimbra340ModuleTypesTrunkAccess": nimbra340ModuleTypesTrunkAccess,
       "nimbra340ModuleTypesTrunkAccess4xDS3E3": nimbra340ModuleTypesTrunkAccess4xDS3E3,
       "nimbra380ModuleTypesAccess": nimbra380ModuleTypesAccess,
       "nimbra380ModuleTypesAccess8xGbE": nimbra380ModuleTypesAccess8xGbE,
       "nimbra340ThermometerTypes": nimbra340ThermometerTypes,
       "nimbra340Thermometer": nimbra340Thermometer,
       "nimbra680": nimbra680,
       "nimbra680ChassisTypes": nimbra680ChassisTypes,
       "nimbra680ContainerTypes": nimbra680ContainerTypes,
       "nimbra680PowerSupplyTypes": nimbra680PowerSupplyTypes,
       "nimbra680PowerSupplyTypesPCU": nimbra680PowerSupplyTypesPCU,
       "nimbra680PowerSupplyTypesPSU": nimbra680PowerSupplyTypesPSU,
       "nimbra680FanTypes": nimbra680FanTypes,
       "nimbra680FanTypesFan": nimbra680FanTypesFan,
       "nimbra680ModuleTypes": nimbra680ModuleTypes,
       "nimbra680ModuleTypesMgmt": nimbra680ModuleTypesMgmt,
       "nimbra680ModuleTypesMgmtControlModule": nimbra680ModuleTypesMgmtControlModule,
       "nimbra680ModuleTypesIf": nimbra680ModuleTypesIf,
       "nimbra680ModuleTypesIfTrunk4xOC3": nimbra680ModuleTypesIfTrunk4xOC3,
       "nimbra680ModuleTypesIfTrunk4xOC12": nimbra680ModuleTypesIfTrunk4xOC12,
       "nimbra680ModuleTypesIfTrunk2xOC48": nimbra680ModuleTypesIfTrunk2xOC48,
       "nimbra680ModuleTypesIfTrunk4xOC48": nimbra680ModuleTypesIfTrunk4xOC48,
       "nimbra680ModuleTypesIfTrunkOC192": nimbra680ModuleTypesIfTrunkOC192,
       "nimbra680ModuleTypesIfTrunk6xIP": nimbra680ModuleTypesIfTrunk6xIP,
       "nimbra680ModuleTypesSwitch": nimbra680ModuleTypesSwitch,
       "nimbra680ModuleTypesSwitch40Gbps": nimbra680ModuleTypesSwitch40Gbps,
       "nimbra680ModuleTypesSwitch80Gbps": nimbra680ModuleTypesSwitch80Gbps,
       "nimbra680ModuleTypesSwitch160Gbps": nimbra680ModuleTypesSwitch160Gbps,
       "nimbra680ModuleTypesAccess": nimbra680ModuleTypesAccess,
       "nimbra680ModuleTypesAccess8xHDSDI": nimbra680ModuleTypesAccess8xHDSDI,
       "nimbra680ModuleTypesAccess8xGbE": nimbra680ModuleTypesAccess8xGbE,
       "nimbra680ModuleTypesAccess8xASI": nimbra680ModuleTypesAccess8xASI,
       "nimbra680ModuleTypesAccess8x3Gbps": nimbra680ModuleTypesAccess8x3Gbps,
       "nimbra680ModuleTypesAccess8xJPEG2000": nimbra680ModuleTypesAccess8xJPEG2000,
       "nimbra680ModuleTypesAccess8xVideo": nimbra680ModuleTypesAccess8xVideo,
       "nimbra680ModuleTypesAccess8xASIAES": nimbra680ModuleTypesAccess8xASIAES,
       "nimbra680ModuleTypesAccess2x10GbE": nimbra680ModuleTypesAccess2x10GbE,
       "nimbra680ModuleTypesAux": nimbra680ModuleTypesAux,
       "nimbra680ModuleTypesAuxGPIO": nimbra680ModuleTypesAuxGPIO,
       "nimbra680ThermometerTypes": nimbra680ThermometerTypes,
       "nimbra680Thermometer": nimbra680Thermometer,
       "nimbra340HD": nimbra340HD,
       "nimbra360": nimbra360,
       "nimbra360Gold": nimbra360Gold,
       "nimbra688": nimbra688,
       "nimbra130": nimbra130,
       "nimbra380": nimbra380,
       "nimbra230": nimbra230,
       "nimbra320": nimbra320,
       "nimbra140": nimbra140,
       "nimbra310": nimbra310,
       "nimbra240": nimbra240,
       "nimbra640": nimbra640,
       "nimbraVA210": nimbraVA210,
       "nimbraVA210FV": nimbraVA210FV,
       "nimbraVA210DCV1": nimbraVA210DCV1,
       "nimbraVA210DCV2": nimbraVA210DCV2,
       "nimbra390": nimbra390,
       "nimbraVA220": nimbraVA220,
       "netiGeneric": netiGeneric,
       "netiProducts": netiProducts,
       "nimbravision": nimbravision,
       "prodNimbra230": prodNimbra230,
       "netiCaps": netiCaps,
       "netiReqs": netiReqs,
       "netiExperimental": netiExperimental,
       "netiExperimentalReg": netiExperimentalReg,
       "netiExperimentalGeneric": netiExperimentalGeneric,
       "netiExperimentalProducts": netiExperimentalProducts,
       "netiExperimentalCaps": netiExperimentalCaps,
       "netiExperimentalReqs": netiExperimentalReqs}
)
