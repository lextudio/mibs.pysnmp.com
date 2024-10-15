# SNMP MIB module (Juniper-E2-Registry) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-E2-Registry
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:09 2024
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

juniE2Registry = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3)
)
juniE2Registry.setRevisions(
        ("2004-05-19 17:42",
         "2003-08-18 20:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniE2EntPhysicalType_ObjectIdentity = ObjectIdentity
juniE2EntPhysicalType = _JuniE2EntPhysicalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1)
)
_E2Chassis_ObjectIdentity = ObjectIdentity
e2Chassis = _E2Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    e2Chassis.setStatus("current")
_E320Chassis_ObjectIdentity = ObjectIdentity
e320Chassis = _E320Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    e320Chassis.setStatus("current")
_E2FanAssembly_ObjectIdentity = ObjectIdentity
e2FanAssembly = _E2FanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    e2FanAssembly.setStatus("current")
_E320PrimaryFanAssembly_ObjectIdentity = ObjectIdentity
e320PrimaryFanAssembly = _E320PrimaryFanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    e320PrimaryFanAssembly.setStatus("current")
_E320AuxiliaryFanAssembly_ObjectIdentity = ObjectIdentity
e320AuxiliaryFanAssembly = _E320AuxiliaryFanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    e320AuxiliaryFanAssembly.setStatus("current")
_E2PowerInput_ObjectIdentity = ObjectIdentity
e2PowerInput = _E2PowerInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    e2PowerInput.setStatus("current")
_E320PowerDistributionModule_ObjectIdentity = ObjectIdentity
e320PowerDistributionModule = _E320PowerDistributionModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    e320PowerDistributionModule.setStatus("current")
_E2Midplane_ObjectIdentity = ObjectIdentity
e2Midplane = _E2Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    e2Midplane.setStatus("current")
_E320Midplane_ObjectIdentity = ObjectIdentity
e320Midplane = _E320Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    e320Midplane.setStatus("current")
_E2SrpModule_ObjectIdentity = ObjectIdentity
e2SrpModule = _E2SrpModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    e2SrpModule.setStatus("current")
_E320Srp100Module_ObjectIdentity = ObjectIdentity
e320Srp100Module = _E320Srp100Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    e320Srp100Module.setStatus("current")
_E320Srp320Module_ObjectIdentity = ObjectIdentity
e320Srp320Module = _E320Srp320Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 99)
)
if mibBuilder.loadTexts:
    e320Srp320Module.setStatus("current")
_E2SwitchFabricModule_ObjectIdentity = ObjectIdentity
e2SwitchFabricModule = _E2SwitchFabricModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    e2SwitchFabricModule.setStatus("current")
_E320FabricSlice100Module_ObjectIdentity = ObjectIdentity
e320FabricSlice100Module = _E320FabricSlice100Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    e320FabricSlice100Module.setStatus("current")
_E320FabricSlice320Module_ObjectIdentity = ObjectIdentity
e320FabricSlice320Module = _E320FabricSlice320Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 99)
)
if mibBuilder.loadTexts:
    e320FabricSlice320Module.setStatus("current")
_E2SrpIoa_ObjectIdentity = ObjectIdentity
e2SrpIoa = _E2SrpIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    e2SrpIoa.setStatus("current")
_E320SrpIoa_ObjectIdentity = ObjectIdentity
e320SrpIoa = _E320SrpIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    e320SrpIoa.setStatus("current")
_E2ForwardingModule_ObjectIdentity = ObjectIdentity
e2ForwardingModule = _E2ForwardingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8)
)
if mibBuilder.loadTexts:
    e2ForwardingModule.setStatus("current")
_E3204gLeModule_ObjectIdentity = ObjectIdentity
e3204gLeModule = _E3204gLeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 1)
)
if mibBuilder.loadTexts:
    e3204gLeModule.setStatus("current")
_E320Ge4PortModule_ObjectIdentity = ObjectIdentity
e320Ge4PortModule = _E320Ge4PortModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    e320Ge4PortModule.setStatus("current")
_E320Oc48Pos1PortModule_ObjectIdentity = ObjectIdentity
e320Oc48Pos1PortModule = _E320Oc48Pos1PortModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 3)
)
if mibBuilder.loadTexts:
    e320Oc48Pos1PortModule.setStatus("current")
_E320Oc48RPos1PortModule_ObjectIdentity = ObjectIdentity
e320Oc48RPos1PortModule = _E320Oc48RPos1PortModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 4)
)
if mibBuilder.loadTexts:
    e320Oc48RPos1PortModule.setStatus("current")
_E320OcXModule_ObjectIdentity = ObjectIdentity
e320OcXModule = _E320OcXModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 5)
)
if mibBuilder.loadTexts:
    e320OcXModule.setStatus("current")
_E320MfgSerdesTestModule_ObjectIdentity = ObjectIdentity
e320MfgSerdesTestModule = _E320MfgSerdesTestModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 99)
)
if mibBuilder.loadTexts:
    e320MfgSerdesTestModule.setStatus("current")
_E2ForwardingIoa_ObjectIdentity = ObjectIdentity
e2ForwardingIoa = _E2ForwardingIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9)
)
if mibBuilder.loadTexts:
    e2ForwardingIoa.setStatus("current")
_E3204GeIoa_ObjectIdentity = ObjectIdentity
e3204GeIoa = _E3204GeIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    e3204GeIoa.setStatus("current")
_E320Oc48PosIoa_ObjectIdentity = ObjectIdentity
e320Oc48PosIoa = _E320Oc48PosIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    e320Oc48PosIoa.setStatus("current")
_E320Oc48RPosIoa_ObjectIdentity = ObjectIdentity
e320Oc48RPosIoa = _E320Oc48RPosIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 3)
)
if mibBuilder.loadTexts:
    e320Oc48RPosIoa.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-E2-Registry",
    **{"juniE2Registry": juniE2Registry,
       "juniE2EntPhysicalType": juniE2EntPhysicalType,
       "e2Chassis": e2Chassis,
       "e320Chassis": e320Chassis,
       "e2FanAssembly": e2FanAssembly,
       "e320PrimaryFanAssembly": e320PrimaryFanAssembly,
       "e320AuxiliaryFanAssembly": e320AuxiliaryFanAssembly,
       "e2PowerInput": e2PowerInput,
       "e320PowerDistributionModule": e320PowerDistributionModule,
       "e2Midplane": e2Midplane,
       "e320Midplane": e320Midplane,
       "e2SrpModule": e2SrpModule,
       "e320Srp100Module": e320Srp100Module,
       "e320Srp320Module": e320Srp320Module,
       "e2SwitchFabricModule": e2SwitchFabricModule,
       "e320FabricSlice100Module": e320FabricSlice100Module,
       "e320FabricSlice320Module": e320FabricSlice320Module,
       "e2SrpIoa": e2SrpIoa,
       "e320SrpIoa": e320SrpIoa,
       "e2ForwardingModule": e2ForwardingModule,
       "e3204gLeModule": e3204gLeModule,
       "e320Ge4PortModule": e320Ge4PortModule,
       "e320Oc48Pos1PortModule": e320Oc48Pos1PortModule,
       "e320Oc48RPos1PortModule": e320Oc48RPos1PortModule,
       "e320OcXModule": e320OcXModule,
       "e320MfgSerdesTestModule": e320MfgSerdesTestModule,
       "e2ForwardingIoa": e2ForwardingIoa,
       "e3204GeIoa": e3204GeIoa,
       "e320Oc48PosIoa": e320Oc48PosIoa,
       "e320Oc48RPosIoa": e320Oc48RPosIoa}
)
