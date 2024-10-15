# SNMP MIB module (AUDIOCODES-TYPES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AUDIOCODES-TYPES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:27 2024
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

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcKnownTypes_ObjectIdentity = ObjectIdentity
acKnownTypes = _AcKnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1)
)
_AcKnownProducts_ObjectIdentity = ObjectIdentity
acKnownProducts = _AcKnownProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1)
)
_AcProductUnknown_ObjectIdentity = ObjectIdentity
acProductUnknown = _AcProductUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 0)
)
_AcProductTrunkPack08_ObjectIdentity = ObjectIdentity
acProductTrunkPack08 = _AcProductTrunkPack08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 1)
)
_AcProductMediaPack108_ObjectIdentity = ObjectIdentity
acProductMediaPack108 = _AcProductMediaPack108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 2)
)
_AcProductMediaPack124_ObjectIdentity = ObjectIdentity
acProductMediaPack124 = _AcProductMediaPack124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 3)
)
_AcProductTrunkPack1600_ObjectIdentity = ObjectIdentity
acProductTrunkPack1600 = _AcProductTrunkPack1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 20)
)
_AcProductTPM1100_ObjectIdentity = ObjectIdentity
acProductTPM1100 = _AcProductTPM1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 22)
)
_AcProductTrunkPack260IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia = _AcProductTrunkPack260IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 23)
)
_AcProductTrunkPack1610_ObjectIdentity = ObjectIdentity
acProductTrunkPack1610 = _AcProductTrunkPack1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 24)
)
_AcProductMediaPack104_ObjectIdentity = ObjectIdentity
acProductMediaPack104 = _AcProductMediaPack104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 25)
)
_AcProductMediaPack102_ObjectIdentity = ObjectIdentity
acProductMediaPack102 = _AcProductMediaPack102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 26)
)
_AcProductTrunkPack1610SB_ObjectIdentity = ObjectIdentity
acProductTrunkPack1610SB = _AcProductTrunkPack1610SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 29)
)
_AcProductTrunkPack1610IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack1610IpMedia = _AcProductTrunkPack1610IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 30)
)
_AcProductTrunkPackMEDIANT2000_ObjectIdentity = ObjectIdentity
acProductTrunkPackMEDIANT2000 = _AcProductTrunkPackMEDIANT2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 31)
)
_AcProductTrunkPackSTRETTO2000_ObjectIdentity = ObjectIdentity
acProductTrunkPackSTRETTO2000 = _AcProductTrunkPackSTRETTO2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 32)
)
_AcProductTrunkPackIPMServer2000_ObjectIdentity = ObjectIdentity
acProductTrunkPackIPMServer2000 = _AcProductTrunkPackIPMServer2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 33)
)
_AcProductTrunkPack2810_ObjectIdentity = ObjectIdentity
acProductTrunkPack2810 = _AcProductTrunkPack2810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 34)
)
_AcProductTrunkPack260UNIpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack260UNIpMedia = _AcProductTrunkPack260UNIpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 35)
)
_AcProductTrunkPack260IpMedia30Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia30Ch = _AcProductTrunkPack260IpMedia30Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 36)
)
_AcProductTrunkPack260IpMedia60Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia60Ch = _AcProductTrunkPack260IpMedia60Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 37)
)
_AcProductTrunkPack260IpMedia120Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia120Ch = _AcProductTrunkPack260IpMedia120Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 38)
)
_AcProductTrunkPack260RTIpMedia30Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260RTIpMedia30Ch = _AcProductTrunkPack260RTIpMedia30Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 39)
)
_AcProductTrunkPack260RTIpMedia60Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260RTIpMedia60Ch = _AcProductTrunkPack260RTIpMedia60Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 40)
)
_AcProductTrunkPack260RTIpMedia120Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260RTIpMedia120Ch = _AcProductTrunkPack260RTIpMedia120Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 41)
)
_AcProductTrunkPack260_ObjectIdentity = ObjectIdentity
acProductTrunkPack260 = _AcProductTrunkPack260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 42)
)
_AcProductTrunkPack260UN_ObjectIdentity = ObjectIdentity
acProductTrunkPack260UN = _AcProductTrunkPack260UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 43)
)
_AcProductTPM1100PCM_ObjectIdentity = ObjectIdentity
acProductTPM1100PCM = _AcProductTPM1100PCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 44)
)
_AcProductTrunkPack6310_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310 = _AcProductTrunkPack6310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 45)
)
_AcProductTPM6300_ObjectIdentity = ObjectIdentity
acProductTPM6300 = _AcProductTPM6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 46)
)
_AcProductMediant1000_ObjectIdentity = ObjectIdentity
acProductMediant1000 = _AcProductMediant1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 47)
)
_AcProductIPMedia3000_ObjectIdentity = ObjectIdentity
acProductIPMedia3000 = _AcProductIPMedia3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 48)
)
_AcProductMediant3000_ObjectIdentity = ObjectIdentity
acProductMediant3000 = _AcProductMediant3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 49)
)
_AcProductStretto3000_ObjectIdentity = ObjectIdentity
acProductStretto3000 = _AcProductStretto3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 50)
)
_AcProductTrunkPack6310IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310IpMedia = _AcProductTrunkPack6310IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 51)
)
_AcProductTrunkPack6310SB_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310SB = _AcProductTrunkPack6310SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 52)
)
_AcProductATP1610_ObjectIdentity = ObjectIdentity
acProductATP1610 = _AcProductATP1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 53)
)
_AcProductATP260_ObjectIdentity = ObjectIdentity
acProductATP260 = _AcProductATP260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 54)
)
_AcProductATP260UN_ObjectIdentity = ObjectIdentity
acProductATP260UN = _AcProductATP260UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 55)
)
_AcProductMediaPack118_ObjectIdentity = ObjectIdentity
acProductMediaPack118 = _AcProductMediaPack118_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 56)
)
_AcProductMediaPack114_ObjectIdentity = ObjectIdentity
acProductMediaPack114 = _AcProductMediaPack114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 57)
)
_AcProductMediaPack112_ObjectIdentity = ObjectIdentity
acProductMediaPack112 = _AcProductMediaPack112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 58)
)
_AcProductTrunkPack6310T3_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310T3 = _AcProductTrunkPack6310T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 59)
)
_AcProductMediant3000T3_ObjectIdentity = ObjectIdentity
acProductMediant3000T3 = _AcProductMediant3000T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 60)
)
_AcProductIPmedia3000T3_ObjectIdentity = ObjectIdentity
acProductIPmedia3000T3 = _AcProductIPmedia3000T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 61)
)
_AcProductTrunkPack6310T3IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310T3IpMedia = _AcProductTrunkPack6310T3IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 62)
)
_AcProductTrunkPack8410_ObjectIdentity = ObjectIdentity
acProductTrunkPack8410 = _AcProductTrunkPack8410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 63)
)
_AcProductTrunkPack8410IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack8410IpMedia = _AcProductTrunkPack8410IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 64)
)
_AcProductMediant600_ObjectIdentity = ObjectIdentity
acProductMediant600 = _AcProductMediant600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 65)
)
_AcProductTrunkPack12610_ObjectIdentity = ObjectIdentity
acProductTrunkPack12610 = _AcProductTrunkPack12610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 66)
)
_AcProductMediant1000MSBG_ObjectIdentity = ObjectIdentity
acProductMediant1000MSBG = _AcProductMediant1000MSBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 67)
)
_AcProductMediant600MSBG_ObjectIdentity = ObjectIdentity
acProductMediant600MSBG = _AcProductMediant600MSBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 68)
)
_AcProductMediaPack500MSBG_ObjectIdentity = ObjectIdentity
acProductMediaPack500MSBG = _AcProductMediaPack500MSBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 69)
)
_AcKnownPhysicalTypes_ObjectIdentity = ObjectIdentity
acKnownPhysicalTypes = _AcKnownPhysicalTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2)
)
_AcKnownChassis_ObjectIdentity = ObjectIdentity
acKnownChassis = _AcKnownChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2)
)
_AcM1000Chassis_ObjectIdentity = ObjectIdentity
acM1000Chassis = _AcM1000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 1)
)
_AcM2000Chassis_ObjectIdentity = ObjectIdentity
acM2000Chassis = _AcM2000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 2)
)
_AcM3000Chassis_ObjectIdentity = ObjectIdentity
acM3000Chassis = _AcM3000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 3)
)
_AcM600Chassis_ObjectIdentity = ObjectIdentity
acM600Chassis = _AcM600Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 4)
)
_AcMP500Chassis_ObjectIdentity = ObjectIdentity
acMP500Chassis = _AcMP500Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 5)
)
_AcKnownSlots_ObjectIdentity = ObjectIdentity
acKnownSlots = _AcKnownSlots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 3)
)
_AcKnownModules_ObjectIdentity = ObjectIdentity
acKnownModules = _AcKnownModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 4)
)
_AcModuleUnknown_ObjectIdentity = ObjectIdentity
acModuleUnknown = _AcModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 4, 1)
)
_AcKnownPorts_ObjectIdentity = ObjectIdentity
acKnownPorts = _AcKnownPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5)
)
_AcPortUnknown_ObjectIdentity = ObjectIdentity
acPortUnknown = _AcPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 1)
)
_AcPortAnalog_ObjectIdentity = ObjectIdentity
acPortAnalog = _AcPortAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2)
)
_AcPortFxsAnalog_ObjectIdentity = ObjectIdentity
acPortFxsAnalog = _AcPortFxsAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2, 1)
)
_AcPortFxoAnalog_ObjectIdentity = ObjectIdentity
acPortFxoAnalog = _AcPortFxoAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2, 2)
)
_AcPortDigital_ObjectIdentity = ObjectIdentity
acPortDigital = _AcPortDigital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3)
)
_AcPortE1T1Quad_ObjectIdentity = ObjectIdentity
acPortE1T1Quad = _AcPortE1T1Quad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 1)
)
_AcPortE1T1Falc56_ObjectIdentity = ObjectIdentity
acPortE1T1Falc56 = _AcPortE1T1Falc56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 2)
)
_AcPortEthernet_ObjectIdentity = ObjectIdentity
acPortEthernet = _AcPortEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 3)
)
_AcPortPstnOc3Stm1_ObjectIdentity = ObjectIdentity
acPortPstnOc3Stm1 = _AcPortPstnOc3Stm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 4)
)
_AcPortAtmStm1_ObjectIdentity = ObjectIdentity
acPortAtmStm1 = _AcPortAtmStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 5)
)
_AcPortGBEthernet_ObjectIdentity = ObjectIdentity
acPortGBEthernet = _AcPortGBEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 6)
)
_AcPortDs3_ObjectIdentity = ObjectIdentity
acPortDs3 = _AcPortDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 7)
)
_AcPortSonetSdh_ObjectIdentity = ObjectIdentity
acPortSonetSdh = _AcPortSonetSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 8)
)
_AcPortBRI_ObjectIdentity = ObjectIdentity
acPortBRI = _AcPortBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 9)
)
_AcPortE1T1OctalFalc_ObjectIdentity = ObjectIdentity
acPortE1T1OctalFalc = _AcPortE1T1OctalFalc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 10)
)
_AcPortWAN_ObjectIdentity = ObjectIdentity
acPortWAN = _AcPortWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 11)
)
_AcPortWireless_ObjectIdentity = ObjectIdentity
acPortWireless = _AcPortWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 12)
)
_AcPortNetwork_ObjectIdentity = ObjectIdentity
acPortNetwork = _AcPortNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 4)
)
_AcKnownFans_ObjectIdentity = ObjectIdentity
acKnownFans = _AcKnownFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 6)
)
_AcFanUnknown_ObjectIdentity = ObjectIdentity
acFanUnknown = _AcFanUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 6, 1)
)
_AcKnownSensors_ObjectIdentity = ObjectIdentity
acKnownSensors = _AcKnownSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 7)
)
_AcTemperatureSensor_ObjectIdentity = ObjectIdentity
acTemperatureSensor = _AcTemperatureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 7, 1)
)
_AcM1000KnownTypes_ObjectIdentity = ObjectIdentity
acM1000KnownTypes = _AcM1000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20)
)
_AcM1000CpuSlot_ObjectIdentity = ObjectIdentity
acM1000CpuSlot = _AcM1000CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 1)
)
_AcM1000IfsSlot_ObjectIdentity = ObjectIdentity
acM1000IfsSlot = _AcM1000IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 2)
)
_AcM1000PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM1000PowerSupplySlot = _AcM1000PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 3)
)
_AcM1000FanSlot_ObjectIdentity = ObjectIdentity
acM1000FanSlot = _AcM1000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 4)
)
_AcM600CpuSlot_ObjectIdentity = ObjectIdentity
acM600CpuSlot = _AcM600CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 5)
)
_AcM600IfsSlot_ObjectIdentity = ObjectIdentity
acM600IfsSlot = _AcM600IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 6)
)
_AcM600PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM600PowerSupplySlot = _AcM600PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 7)
)
_AcM600FanSlot_ObjectIdentity = ObjectIdentity
acM600FanSlot = _AcM600FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 8)
)
_AcM1000CpuModule_ObjectIdentity = ObjectIdentity
acM1000CpuModule = _AcM1000CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 11)
)
_AcM1000AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM1000AnalogIfsModule = _AcM1000AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 12)
)
_AcM1000DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM1000DigitalIfsModule = _AcM1000DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 13)
)
_AcM1000PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM1000PowerSupplyModule = _AcM1000PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 14)
)
_AcM1000FanModule_ObjectIdentity = ObjectIdentity
acM1000FanModule = _AcM1000FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 15)
)
_AcM1000BRIModule_ObjectIdentity = ObjectIdentity
acM1000BRIModule = _AcM1000BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 16)
)
_AcM1000IPMediaModule_ObjectIdentity = ObjectIdentity
acM1000IPMediaModule = _AcM1000IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 17)
)
_AcM600CpuModule_ObjectIdentity = ObjectIdentity
acM600CpuModule = _AcM600CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 18)
)
_AcM600AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM600AnalogIfsModule = _AcM600AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 19)
)
_AcM600DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM600DigitalIfsModule = _AcM600DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 20)
)
_AcM600PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM600PowerSupplyModule = _AcM600PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 21)
)
_AcM600FanModule_ObjectIdentity = ObjectIdentity
acM600FanModule = _AcM600FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 22)
)
_AcM600BRIModule_ObjectIdentity = ObjectIdentity
acM600BRIModule = _AcM600BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 23)
)
_AcM600IPMediaModule_ObjectIdentity = ObjectIdentity
acM600IPMediaModule = _AcM600IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 24)
)
_AcM2000KnownTypes_ObjectIdentity = ObjectIdentity
acM2000KnownTypes = _AcM2000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 21)
)
_AcM2000CpuSlot_ObjectIdentity = ObjectIdentity
acM2000CpuSlot = _AcM2000CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 21, 1)
)
_AcM2000Module1610_ObjectIdentity = ObjectIdentity
acM2000Module1610 = _AcM2000Module1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 21, 11)
)
_AcM3000KnownTypes_ObjectIdentity = ObjectIdentity
acM3000KnownTypes = _AcM3000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22)
)
_AcM3000Slot_ObjectIdentity = ObjectIdentity
acM3000Slot = _AcM3000Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 1)
)
_AcM3000PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM3000PowerSupplySlot = _AcM3000PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 2)
)
_AcM3000FanSlot_ObjectIdentity = ObjectIdentity
acM3000FanSlot = _AcM3000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 3)
)
_AcM3000Module6310_ObjectIdentity = ObjectIdentity
acM3000Module6310 = _AcM3000Module6310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 11)
)
_AcM3000ModuleSat_ObjectIdentity = ObjectIdentity
acM3000ModuleSat = _AcM3000ModuleSat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 12)
)
_AcM3000PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM3000PowerSupplyModule = _AcM3000PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 13)
)
_AcM3000FanModule_ObjectIdentity = ObjectIdentity
acM3000FanModule = _AcM3000FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 14)
)
_AcM3000Module8410_ObjectIdentity = ObjectIdentity
acM3000Module8410 = _AcM3000Module8410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 17)
)
_AcMP500KnownTypes_ObjectIdentity = ObjectIdentity
acMP500KnownTypes = _AcMP500KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23)
)
_AcMP500CpuSlot_ObjectIdentity = ObjectIdentity
acMP500CpuSlot = _AcMP500CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 1)
)
_AcMP500IfsSlot_ObjectIdentity = ObjectIdentity
acMP500IfsSlot = _AcMP500IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 2)
)
_AcMP500CpuModule_ObjectIdentity = ObjectIdentity
acMP500CpuModule = _AcMP500CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 3)
)
_AcMP500AnalogIfsModule_ObjectIdentity = ObjectIdentity
acMP500AnalogIfsModule = _AcMP500AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 4)
)
_AcMP500DigitalIfsModule_ObjectIdentity = ObjectIdentity
acMP500DigitalIfsModule = _AcMP500DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 5)
)
_AcMP500BRIModule_ObjectIdentity = ObjectIdentity
acMP500BRIModule = _AcMP500BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 6)
)
_AcMP500WANModule_ObjectIdentity = ObjectIdentity
acMP500WANModule = _AcMP500WANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 7)
)
_AcMP500WiFiModule_ObjectIdentity = ObjectIdentity
acMP500WiFiModule = _AcMP500WiFiModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 8)
)
_AcMP500IPMediaModule_ObjectIdentity = ObjectIdentity
acMP500IPMediaModule = _AcMP500IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 9)
)
_AcMP500EthernetModule_ObjectIdentity = ObjectIdentity
acMP500EthernetModule = _AcMP500EthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 10)
)
_AcKnownLogicalTypes_ObjectIdentity = ObjectIdentity
acKnownLogicalTypes = _AcKnownLogicalTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 3)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcBoardMibs_ObjectIdentity = ObjectIdentity
acBoardMibs = _AcBoardMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10)
)
_AcPerformance_ObjectIdentity = ObjectIdentity
acPerformance = _AcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10)
)
_AcExperimental_ObjectIdentity = ObjectIdentity
acExperimental = _AcExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUDIOCODES-TYPES-MIB",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acKnownTypes": acKnownTypes,
       "acKnownProducts": acKnownProducts,
       "acProductUnknown": acProductUnknown,
       "acProductTrunkPack08": acProductTrunkPack08,
       "acProductMediaPack108": acProductMediaPack108,
       "acProductMediaPack124": acProductMediaPack124,
       "acProductTrunkPack1600": acProductTrunkPack1600,
       "acProductTPM1100": acProductTPM1100,
       "acProductTrunkPack260IpMedia": acProductTrunkPack260IpMedia,
       "acProductTrunkPack1610": acProductTrunkPack1610,
       "acProductMediaPack104": acProductMediaPack104,
       "acProductMediaPack102": acProductMediaPack102,
       "acProductTrunkPack1610SB": acProductTrunkPack1610SB,
       "acProductTrunkPack1610IpMedia": acProductTrunkPack1610IpMedia,
       "acProductTrunkPackMEDIANT2000": acProductTrunkPackMEDIANT2000,
       "acProductTrunkPackSTRETTO2000": acProductTrunkPackSTRETTO2000,
       "acProductTrunkPackIPMServer2000": acProductTrunkPackIPMServer2000,
       "acProductTrunkPack2810": acProductTrunkPack2810,
       "acProductTrunkPack260UNIpMedia": acProductTrunkPack260UNIpMedia,
       "acProductTrunkPack260IpMedia30Ch": acProductTrunkPack260IpMedia30Ch,
       "acProductTrunkPack260IpMedia60Ch": acProductTrunkPack260IpMedia60Ch,
       "acProductTrunkPack260IpMedia120Ch": acProductTrunkPack260IpMedia120Ch,
       "acProductTrunkPack260RTIpMedia30Ch": acProductTrunkPack260RTIpMedia30Ch,
       "acProductTrunkPack260RTIpMedia60Ch": acProductTrunkPack260RTIpMedia60Ch,
       "acProductTrunkPack260RTIpMedia120Ch": acProductTrunkPack260RTIpMedia120Ch,
       "acProductTrunkPack260": acProductTrunkPack260,
       "acProductTrunkPack260UN": acProductTrunkPack260UN,
       "acProductTPM1100PCM": acProductTPM1100PCM,
       "acProductTrunkPack6310": acProductTrunkPack6310,
       "acProductTPM6300": acProductTPM6300,
       "acProductMediant1000": acProductMediant1000,
       "acProductIPMedia3000": acProductIPMedia3000,
       "acProductMediant3000": acProductMediant3000,
       "acProductStretto3000": acProductStretto3000,
       "acProductTrunkPack6310IpMedia": acProductTrunkPack6310IpMedia,
       "acProductTrunkPack6310SB": acProductTrunkPack6310SB,
       "acProductATP1610": acProductATP1610,
       "acProductATP260": acProductATP260,
       "acProductATP260UN": acProductATP260UN,
       "acProductMediaPack118": acProductMediaPack118,
       "acProductMediaPack114": acProductMediaPack114,
       "acProductMediaPack112": acProductMediaPack112,
       "acProductTrunkPack6310T3": acProductTrunkPack6310T3,
       "acProductMediant3000T3": acProductMediant3000T3,
       "acProductIPmedia3000T3": acProductIPmedia3000T3,
       "acProductTrunkPack6310T3IpMedia": acProductTrunkPack6310T3IpMedia,
       "acProductTrunkPack8410": acProductTrunkPack8410,
       "acProductTrunkPack8410IpMedia": acProductTrunkPack8410IpMedia,
       "acProductMediant600": acProductMediant600,
       "acProductTrunkPack12610": acProductTrunkPack12610,
       "acProductMediant1000MSBG": acProductMediant1000MSBG,
       "acProductMediant600MSBG": acProductMediant600MSBG,
       "acProductMediaPack500MSBG": acProductMediaPack500MSBG,
       "acKnownPhysicalTypes": acKnownPhysicalTypes,
       "acKnownChassis": acKnownChassis,
       "acM1000Chassis": acM1000Chassis,
       "acM2000Chassis": acM2000Chassis,
       "acM3000Chassis": acM3000Chassis,
       "acM600Chassis": acM600Chassis,
       "acMP500Chassis": acMP500Chassis,
       "acKnownSlots": acKnownSlots,
       "acKnownModules": acKnownModules,
       "acModuleUnknown": acModuleUnknown,
       "acKnownPorts": acKnownPorts,
       "acPortUnknown": acPortUnknown,
       "acPortAnalog": acPortAnalog,
       "acPortFxsAnalog": acPortFxsAnalog,
       "acPortFxoAnalog": acPortFxoAnalog,
       "acPortDigital": acPortDigital,
       "acPortE1T1Quad": acPortE1T1Quad,
       "acPortE1T1Falc56": acPortE1T1Falc56,
       "acPortEthernet": acPortEthernet,
       "acPortPstnOc3Stm1": acPortPstnOc3Stm1,
       "acPortAtmStm1": acPortAtmStm1,
       "acPortGBEthernet": acPortGBEthernet,
       "acPortDs3": acPortDs3,
       "acPortSonetSdh": acPortSonetSdh,
       "acPortBRI": acPortBRI,
       "acPortE1T1OctalFalc": acPortE1T1OctalFalc,
       "acPortWAN": acPortWAN,
       "acPortWireless": acPortWireless,
       "acPortNetwork": acPortNetwork,
       "acKnownFans": acKnownFans,
       "acFanUnknown": acFanUnknown,
       "acKnownSensors": acKnownSensors,
       "acTemperatureSensor": acTemperatureSensor,
       "acM1000KnownTypes": acM1000KnownTypes,
       "acM1000CpuSlot": acM1000CpuSlot,
       "acM1000IfsSlot": acM1000IfsSlot,
       "acM1000PowerSupplySlot": acM1000PowerSupplySlot,
       "acM1000FanSlot": acM1000FanSlot,
       "acM600CpuSlot": acM600CpuSlot,
       "acM600IfsSlot": acM600IfsSlot,
       "acM600PowerSupplySlot": acM600PowerSupplySlot,
       "acM600FanSlot": acM600FanSlot,
       "acM1000CpuModule": acM1000CpuModule,
       "acM1000AnalogIfsModule": acM1000AnalogIfsModule,
       "acM1000DigitalIfsModule": acM1000DigitalIfsModule,
       "acM1000PowerSupplyModule": acM1000PowerSupplyModule,
       "acM1000FanModule": acM1000FanModule,
       "acM1000BRIModule": acM1000BRIModule,
       "acM1000IPMediaModule": acM1000IPMediaModule,
       "acM600CpuModule": acM600CpuModule,
       "acM600AnalogIfsModule": acM600AnalogIfsModule,
       "acM600DigitalIfsModule": acM600DigitalIfsModule,
       "acM600PowerSupplyModule": acM600PowerSupplyModule,
       "acM600FanModule": acM600FanModule,
       "acM600BRIModule": acM600BRIModule,
       "acM600IPMediaModule": acM600IPMediaModule,
       "acM2000KnownTypes": acM2000KnownTypes,
       "acM2000CpuSlot": acM2000CpuSlot,
       "acM2000Module1610": acM2000Module1610,
       "acM3000KnownTypes": acM3000KnownTypes,
       "acM3000Slot": acM3000Slot,
       "acM3000PowerSupplySlot": acM3000PowerSupplySlot,
       "acM3000FanSlot": acM3000FanSlot,
       "acM3000Module6310": acM3000Module6310,
       "acM3000ModuleSat": acM3000ModuleSat,
       "acM3000PowerSupplyModule": acM3000PowerSupplyModule,
       "acM3000FanModule": acM3000FanModule,
       "acM3000Module8410": acM3000Module8410,
       "acMP500KnownTypes": acMP500KnownTypes,
       "acMP500CpuSlot": acMP500CpuSlot,
       "acMP500IfsSlot": acMP500IfsSlot,
       "acMP500CpuModule": acMP500CpuModule,
       "acMP500AnalogIfsModule": acMP500AnalogIfsModule,
       "acMP500DigitalIfsModule": acMP500DigitalIfsModule,
       "acMP500BRIModule": acMP500BRIModule,
       "acMP500WANModule": acMP500WANModule,
       "acMP500WiFiModule": acMP500WiFiModule,
       "acMP500IPMediaModule": acMP500IPMediaModule,
       "acMP500EthernetModule": acMP500EthernetModule,
       "acKnownLogicalTypes": acKnownLogicalTypes,
       "acProducts": acProducts,
       "acBoardMibs": acBoardMibs,
       "acPerformance": acPerformance,
       "acExperimental": acExperimental}
)
