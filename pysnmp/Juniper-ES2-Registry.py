# SNMP MIB module (Juniper-ES2-Registry) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ES2-Registry
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:12 2024
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

(juniAdmin,) = mibBuilder.importSymbols(
    "Juniper-Registry",
    "juniAdmin")

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

juniES2Registry = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3)
)
juniES2Registry.setRevisions(
        ("2008-05-08 11:48",
         "2006-12-18 21:06",
         "2006-11-24 09:13",
         "2006-01-06 18:06",
         "2005-09-15 13:46",
         "2005-08-19 11:58",
         "2005-07-29 18:26",
         "2004-12-23 11:58",
         "2004-12-06 10:21",
         "2004-05-19 17:42",
         "2003-08-18 20:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniES2EntPhysicalType_ObjectIdentity = ObjectIdentity
juniES2EntPhysicalType = _JuniES2EntPhysicalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1)
)
_Es2Chassis_ObjectIdentity = ObjectIdentity
es2Chassis = _Es2Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    es2Chassis.setStatus("current")
_E320BaseChassis_ObjectIdentity = ObjectIdentity
e320BaseChassis = _E320BaseChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    e320BaseChassis.setStatus("current")
_E120BaseChassis_ObjectIdentity = ObjectIdentity
e120BaseChassis = _E120BaseChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    e120BaseChassis.setStatus("current")
_Es2FanAssembly_ObjectIdentity = ObjectIdentity
es2FanAssembly = _Es2FanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    es2FanAssembly.setStatus("current")
_E320PrimaryFanTray_ObjectIdentity = ObjectIdentity
e320PrimaryFanTray = _E320PrimaryFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    e320PrimaryFanTray.setStatus("current")
_E320AuxiliaryFanTray_ObjectIdentity = ObjectIdentity
e320AuxiliaryFanTray = _E320AuxiliaryFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    e320AuxiliaryFanTray.setStatus("current")
_E120PrimaryFanTray_ObjectIdentity = ObjectIdentity
e120PrimaryFanTray = _E120PrimaryFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    e120PrimaryFanTray.setStatus("current")
_Es2PowerInput_ObjectIdentity = ObjectIdentity
es2PowerInput = _Es2PowerInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    es2PowerInput.setStatus("current")
_E320DcPowerDistributionUnit_ObjectIdentity = ObjectIdentity
e320DcPowerDistributionUnit = _E320DcPowerDistributionUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    e320DcPowerDistributionUnit.setStatus("current")
_Es2Midplane_ObjectIdentity = ObjectIdentity
es2Midplane = _Es2Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    es2Midplane.setStatus("current")
_E320Midplane_ObjectIdentity = ObjectIdentity
e320Midplane = _E320Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    e320Midplane.setStatus("current")
_E120Midplane_ObjectIdentity = ObjectIdentity
e120Midplane = _E120Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    e120Midplane.setStatus("current")
_Es2SrpModule_ObjectIdentity = ObjectIdentity
es2SrpModule = _Es2SrpModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    es2SrpModule.setStatus("current")
_E320Srp100_ObjectIdentity = ObjectIdentity
e320Srp100 = _E320Srp100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    e320Srp100.setStatus("current")
_E320Srp320_ObjectIdentity = ObjectIdentity
e320Srp320 = _E320Srp320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    e320Srp320.setStatus("current")
_E120Srp120_ObjectIdentity = ObjectIdentity
e120Srp120 = _E120Srp120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    e120Srp120.setStatus("current")
_Es2SwitchFabricModule_ObjectIdentity = ObjectIdentity
es2SwitchFabricModule = _Es2SwitchFabricModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    es2SwitchFabricModule.setStatus("current")
_E320Sfm100_ObjectIdentity = ObjectIdentity
e320Sfm100 = _E320Sfm100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    e320Sfm100.setStatus("current")
_E320Sfm320_ObjectIdentity = ObjectIdentity
e320Sfm320 = _E320Sfm320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    e320Sfm320.setStatus("current")
_E120Sfm120_ObjectIdentity = ObjectIdentity
e120Sfm120 = _E120Sfm120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    e120Sfm120.setStatus("current")
_Es2SrpIoa_ObjectIdentity = ObjectIdentity
es2SrpIoa = _Es2SrpIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    es2SrpIoa.setStatus("current")
_E320SrpIoa_ObjectIdentity = ObjectIdentity
e320SrpIoa = _E320SrpIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    e320SrpIoa.setStatus("current")
_Es2ForwardingModule_ObjectIdentity = ObjectIdentity
es2ForwardingModule = _Es2ForwardingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8)
)
if mibBuilder.loadTexts:
    es2ForwardingModule.setStatus("current")
_Es2Lm4_ObjectIdentity = ObjectIdentity
es2Lm4 = _Es2Lm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 1)
)
if mibBuilder.loadTexts:
    es2Lm4.setStatus("current")
_Es2Lm10Uplink_ObjectIdentity = ObjectIdentity
es2Lm10Uplink = _Es2Lm10Uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    es2Lm10Uplink.setStatus("current")
_Es2Lm10_ObjectIdentity = ObjectIdentity
es2Lm10 = _Es2Lm10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 3)
)
if mibBuilder.loadTexts:
    es2Lm10.setStatus("current")
_Es2Lm10s_ObjectIdentity = ObjectIdentity
es2Lm10s = _Es2Lm10s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 4)
)
if mibBuilder.loadTexts:
    es2Lm10s.setStatus("current")
_Es2ForwardingIoa_ObjectIdentity = ObjectIdentity
es2ForwardingIoa = _Es2ForwardingIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9)
)
if mibBuilder.loadTexts:
    es2ForwardingIoa.setStatus("current")
_Es2Ge4S1Ioa_ObjectIdentity = ObjectIdentity
es2Ge4S1Ioa = _Es2Ge4S1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    es2Ge4S1Ioa.setStatus("current")
_Es2Oc48Stm16PosS1Ioa_ObjectIdentity = ObjectIdentity
es2Oc48Stm16PosS1Ioa = _Es2Oc48Stm16PosS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    es2Oc48Stm16PosS1Ioa.setStatus("current")
_Es2ServiceS1Ioa_ObjectIdentity = ObjectIdentity
es2ServiceS1Ioa = _Es2ServiceS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 3)
)
if mibBuilder.loadTexts:
    es2ServiceS1Ioa.setStatus("current")
_Es2Oc3Stm1x8AtmS1Ioa_ObjectIdentity = ObjectIdentity
es2Oc3Stm1x8AtmS1Ioa = _Es2Oc3Stm1x8AtmS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 4)
)
if mibBuilder.loadTexts:
    es2Oc3Stm1x8AtmS1Ioa.setStatus("current")
_Es2RedundancyS1Ioa_ObjectIdentity = ObjectIdentity
es2RedundancyS1Ioa = _Es2RedundancyS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 5)
)
if mibBuilder.loadTexts:
    es2RedundancyS1Ioa.setStatus("current")
_Es2Oc12Stm4x2PosS1Ioa_ObjectIdentity = ObjectIdentity
es2Oc12Stm4x2PosS1Ioa = _Es2Oc12Stm4x2PosS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 6)
)
if mibBuilder.loadTexts:
    es2Oc12Stm4x2PosS1Ioa.setStatus("current")
_Es2Oc12Stm4x2AtmS1Ioa_ObjectIdentity = ObjectIdentity
es2Oc12Stm4x2AtmS1Ioa = _Es2Oc12Stm4x2AtmS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 7)
)
if mibBuilder.loadTexts:
    es2Oc12Stm4x2AtmS1Ioa.setStatus("current")
_Es2dash10GeS1Ioa_ObjectIdentity = ObjectIdentity
es2dash10GeS1Ioa = _Es2dash10GeS1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 8)
)
if mibBuilder.loadTexts:
    es2dash10GeS1Ioa.setStatus("current")
_Es2Ge8S1Ioa_ObjectIdentity = ObjectIdentity
es2Ge8S1Ioa = _Es2Ge8S1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 9)
)
if mibBuilder.loadTexts:
    es2Ge8S1Ioa.setStatus("current")
_Es2dash10GePrS2Ioa_ObjectIdentity = ObjectIdentity
es2dash10GePrS2Ioa = _Es2dash10GePrS2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 10)
)
if mibBuilder.loadTexts:
    es2dash10GePrS2Ioa.setStatus("current")
_Es2Ge20S2Ioa_ObjectIdentity = ObjectIdentity
es2Ge20S2Ioa = _Es2Ge20S2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 11)
)
if mibBuilder.loadTexts:
    es2Ge20S2Ioa.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ES2-Registry",
    **{"juniES2Registry": juniES2Registry,
       "juniES2EntPhysicalType": juniES2EntPhysicalType,
       "es2Chassis": es2Chassis,
       "e320BaseChassis": e320BaseChassis,
       "e120BaseChassis": e120BaseChassis,
       "es2FanAssembly": es2FanAssembly,
       "e320PrimaryFanTray": e320PrimaryFanTray,
       "e320AuxiliaryFanTray": e320AuxiliaryFanTray,
       "e120PrimaryFanTray": e120PrimaryFanTray,
       "es2PowerInput": es2PowerInput,
       "e320DcPowerDistributionUnit": e320DcPowerDistributionUnit,
       "es2Midplane": es2Midplane,
       "e320Midplane": e320Midplane,
       "e120Midplane": e120Midplane,
       "es2SrpModule": es2SrpModule,
       "e320Srp100": e320Srp100,
       "e320Srp320": e320Srp320,
       "e120Srp120": e120Srp120,
       "es2SwitchFabricModule": es2SwitchFabricModule,
       "e320Sfm100": e320Sfm100,
       "e320Sfm320": e320Sfm320,
       "e120Sfm120": e120Sfm120,
       "es2SrpIoa": es2SrpIoa,
       "e320SrpIoa": e320SrpIoa,
       "es2ForwardingModule": es2ForwardingModule,
       "es2Lm4": es2Lm4,
       "es2Lm10Uplink": es2Lm10Uplink,
       "es2Lm10": es2Lm10,
       "es2Lm10s": es2Lm10s,
       "es2ForwardingIoa": es2ForwardingIoa,
       "es2Ge4S1Ioa": es2Ge4S1Ioa,
       "es2Oc48Stm16PosS1Ioa": es2Oc48Stm16PosS1Ioa,
       "es2ServiceS1Ioa": es2ServiceS1Ioa,
       "es2Oc3Stm1x8AtmS1Ioa": es2Oc3Stm1x8AtmS1Ioa,
       "es2RedundancyS1Ioa": es2RedundancyS1Ioa,
       "es2Oc12Stm4x2PosS1Ioa": es2Oc12Stm4x2PosS1Ioa,
       "es2Oc12Stm4x2AtmS1Ioa": es2Oc12Stm4x2AtmS1Ioa,
       "es2dash10GeS1Ioa": es2dash10GeS1Ioa,
       "es2Ge8S1Ioa": es2Ge8S1Ioa,
       "es2dash10GePrS2Ioa": es2dash10GePrS2Ioa,
       "es2Ge20S2Ioa": es2Ge20S2Ioa}
)
