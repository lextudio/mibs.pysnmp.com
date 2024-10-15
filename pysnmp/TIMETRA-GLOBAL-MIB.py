# SNMP MIB module (TIMETRA-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:33 2024
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

timetraGlobalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 1)
)
timetraGlobalMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1910-02-28 00:00",
         "1909-02-28 00:00",
         "1909-02-01 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Timetra_ObjectIdentity = ObjectIdentity
timetra = _Timetra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527)
)
_TimetraReg_ObjectIdentity = ObjectIdentity
timetraReg = _TimetraReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1)
)
_TimetraModules_ObjectIdentity = ObjectIdentity
timetraModules = _TimetraModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1)
)
_TimetraSRMIBModules_ObjectIdentity = ObjectIdentity
timetraSRMIBModules = _TimetraSRMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3)
)
_TimetraCapabilityModule_ObjectIdentity = ObjectIdentity
timetraCapabilityModule = _TimetraCapabilityModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4)
)
_Timetra7750CapModule_ObjectIdentity = ObjectIdentity
timetra7750CapModule = _Timetra7750CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 1)
)
_Timetra7450CapModule_ObjectIdentity = ObjectIdentity
timetra7450CapModule = _Timetra7450CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 2)
)
_Timetra7710CapModule_ObjectIdentity = ObjectIdentity
timetra7710CapModule = _Timetra7710CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 3)
)
_Timetra7750MGCapModule_ObjectIdentity = ObjectIdentity
timetra7750MGCapModule = _Timetra7750MGCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 4)
)
_TimetraSROSCapModule_ObjectIdentity = ObjectIdentity
timetraSROSCapModule = _TimetraSROSCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 5)
)
_AlcatelCommonMIBModules_ObjectIdentity = ObjectIdentity
alcatelCommonMIBModules = _AlcatelCommonMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 5)
)
_TimetraServiceRouters_ObjectIdentity = ObjectIdentity
timetraServiceRouters = _TimetraServiceRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3)
)
_TmnxModelSR1Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR1Reg = _TmnxModelSR1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxModelSR1Reg.setStatus("current")
_TmnxModelSR4Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR4Reg = _TmnxModelSR4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxModelSR4Reg.setStatus("current")
_TmnxModelSR12Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR12Reg = _TmnxModelSR12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxModelSR12Reg.setStatus("current")
_TmnxModelSR7Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR7Reg = _TmnxModelSR7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxModelSR7Reg.setStatus("current")
_TmnxModelSR6Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR6Reg = _TmnxModelSR6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxModelSR6Reg.setStatus("current")
_TmnxModelSRc12Reg_ObjectIdentity = ObjectIdentity
tmnxModelSRc12Reg = _TmnxModelSRc12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxModelSRc12Reg.setStatus("current")
_TmnxModelSRc4Reg_ObjectIdentity = ObjectIdentity
tmnxModelSRc4Reg = _TmnxModelSRc4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxModelSRc4Reg.setStatus("current")
_TimetraServiceSwitches_ObjectIdentity = ObjectIdentity
timetraServiceSwitches = _TimetraServiceSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6)
)
_TmnxModelESS1Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS1Reg = _TmnxModelESS1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxModelESS1Reg.setStatus("current")
_TmnxModelESS4Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS4Reg = _TmnxModelESS4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxModelESS4Reg.setStatus("current")
_TmnxModelESS7Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS7Reg = _TmnxModelESS7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxModelESS7Reg.setStatus("current")
_TmnxModelESS12Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS12Reg = _TmnxModelESS12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxModelESS12Reg.setStatus("current")
_TmnxModelESS6Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS6Reg = _TmnxModelESS6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxModelESS6Reg.setStatus("current")
_TmnxModelESS6vReg_ObjectIdentity = ObjectIdentity
tmnxModelESS6vReg = _TmnxModelESS6vReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 6)
)
if mibBuilder.loadTexts:
    tmnxModelESS6vReg.setStatus("current")
_Alcatel7710ServiceRouters_ObjectIdentity = ObjectIdentity
alcatel7710ServiceRouters = _Alcatel7710ServiceRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 9)
)
_TmnxModel7710SRc12Reg_ObjectIdentity = ObjectIdentity
tmnxModel7710SRc12Reg = _TmnxModel7710SRc12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxModel7710SRc12Reg.setStatus("current")
_TmnxModel7710SRc4Reg_ObjectIdentity = ObjectIdentity
tmnxModel7710SRc4Reg = _TmnxModel7710SRc4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxModel7710SRc4Reg.setStatus("current")
_Alcatel7750MobileGateways_ObjectIdentity = ObjectIdentity
alcatel7750MobileGateways = _Alcatel7750MobileGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 12)
)
_TmnxModel7750MGSR7Reg_ObjectIdentity = ObjectIdentity
tmnxModel7750MGSR7Reg = _TmnxModel7750MGSR7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxModel7750MGSR7Reg.setStatus("current")
_TmnxModel7750MGSR12Reg_ObjectIdentity = ObjectIdentity
tmnxModel7750MGSR12Reg = _TmnxModel7750MGSR12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 12, 2)
)
if mibBuilder.loadTexts:
    tmnxModel7750MGSR12Reg.setStatus("current")
_Alcatel7950ExtServiceRouters_ObjectIdentity = ObjectIdentity
alcatel7950ExtServiceRouters = _Alcatel7950ExtServiceRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15)
)
_TmnxModel7950XRS20Reg_ObjectIdentity = ObjectIdentity
tmnxModel7950XRS20Reg = _TmnxModel7950XRS20Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxModel7950XRS20Reg.setStatus("current")
_TmnxModel7950XRS16Reg_ObjectIdentity = ObjectIdentity
tmnxModel7950XRS16Reg = _TmnxModel7950XRS16Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15, 2)
)
if mibBuilder.loadTexts:
    tmnxModel7950XRS16Reg.setStatus("current")
_TimetraGeneric_ObjectIdentity = ObjectIdentity
timetraGeneric = _TimetraGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 2)
)
_TimetraProducts_ObjectIdentity = ObjectIdentity
timetraProducts = _TimetraProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3)
)
_TmnxSRMIB_ObjectIdentity = ObjectIdentity
tmnxSRMIB = _TmnxSRMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1)
)
_TmnxSRConfs_ObjectIdentity = ObjectIdentity
tmnxSRConfs = _TmnxSRConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1)
)
_TmnxSRObjs_ObjectIdentity = ObjectIdentity
tmnxSRObjs = _TmnxSRObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2)
)
_TmnxSRNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSRNotifyPrefix = _TmnxSRNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3)
)
_TmnxESSMIB_ObjectIdentity = ObjectIdentity
tmnxESSMIB = _TmnxESSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2)
)
_TmnxESSConfs_ObjectIdentity = ObjectIdentity
tmnxESSConfs = _TmnxESSConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 1)
)
_TmnxESSObjs_ObjectIdentity = ObjectIdentity
tmnxESSObjs = _TmnxESSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 2)
)
_TmnxESSNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxESSNotifyPrefix = _TmnxESSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 3)
)
_AlcatelCommonMIB_ObjectIdentity = ObjectIdentity
alcatelCommonMIB = _AlcatelCommonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3)
)
_AlcatelConformance_ObjectIdentity = ObjectIdentity
alcatelConformance = _AlcatelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1)
)
_AlcatelObjects_ObjectIdentity = ObjectIdentity
alcatelObjects = _AlcatelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2)
)
_AlcatelNotifyPrefix_ObjectIdentity = ObjectIdentity
alcatelNotifyPrefix = _AlcatelNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3)
)
_TmnxMGMIB_ObjectIdentity = ObjectIdentity
tmnxMGMIB = _TmnxMGMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4)
)
_TmnxMGConfs_ObjectIdentity = ObjectIdentity
tmnxMGConfs = _TmnxMGConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4, 1)
)
_TmnxMGObjs_ObjectIdentity = ObjectIdentity
tmnxMGObjs = _TmnxMGObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4, 2)
)
_TmnxMGNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMGNotifyPrefix = _TmnxMGNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4, 3)
)
_TmnxAgentCapability_ObjectIdentity = ObjectIdentity
tmnxAgentCapability = _TmnxAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4)
)
_Tmnx7750AgentCapability_ObjectIdentity = ObjectIdentity
tmnx7750AgentCapability = _Tmnx7750AgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4, 1)
)
_Tmnx7450AgentCapability_ObjectIdentity = ObjectIdentity
tmnx7450AgentCapability = _Tmnx7450AgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4, 2)
)
_Tmnx7710AgentCapability_ObjectIdentity = ObjectIdentity
tmnx7710AgentCapability = _Tmnx7710AgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4, 3)
)
_TmnxProductCapability_ObjectIdentity = ObjectIdentity
tmnxProductCapability = _TmnxProductCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5)
)
_Tmnx7750Capability_ObjectIdentity = ObjectIdentity
tmnx7750Capability = _Tmnx7750Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1)
)
_Tmnx7750V3v0_ObjectIdentity = ObjectIdentity
tmnx7750V3v0 = _Tmnx7750V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 1)
)
_Tmnx7750V4v0_ObjectIdentity = ObjectIdentity
tmnx7750V4v0 = _Tmnx7750V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 2)
)
_Tmnx7750V5v0_ObjectIdentity = ObjectIdentity
tmnx7750V5v0 = _Tmnx7750V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 3)
)
_Tmnx7750V6v0_ObjectIdentity = ObjectIdentity
tmnx7750V6v0 = _Tmnx7750V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 4)
)
_Tmnx7750V6v1_ObjectIdentity = ObjectIdentity
tmnx7750V6v1 = _Tmnx7750V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 5)
)
_Tmnx7750V7v0_ObjectIdentity = ObjectIdentity
tmnx7750V7v0 = _Tmnx7750V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 6)
)
_Tmnx7750V8v0_ObjectIdentity = ObjectIdentity
tmnx7750V8v0 = _Tmnx7750V8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 7)
)
_Tmnx7450Capability_ObjectIdentity = ObjectIdentity
tmnx7450Capability = _Tmnx7450Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2)
)
_Tmnx7450V3v0_ObjectIdentity = ObjectIdentity
tmnx7450V3v0 = _Tmnx7450V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 1)
)
_Tmnx7450V4v0_ObjectIdentity = ObjectIdentity
tmnx7450V4v0 = _Tmnx7450V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 2)
)
_Tmnx7450V5v0_ObjectIdentity = ObjectIdentity
tmnx7450V5v0 = _Tmnx7450V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 3)
)
_Tmnx7450V6v0_ObjectIdentity = ObjectIdentity
tmnx7450V6v0 = _Tmnx7450V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 4)
)
_Tmnx7450V6v1_ObjectIdentity = ObjectIdentity
tmnx7450V6v1 = _Tmnx7450V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 5)
)
_Tmnx7450V7v0_ObjectIdentity = ObjectIdentity
tmnx7450V7v0 = _Tmnx7450V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 6)
)
_Tmnx7450V8v0_ObjectIdentity = ObjectIdentity
tmnx7450V8v0 = _Tmnx7450V8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 7)
)
_Tmnx7710Capability_ObjectIdentity = ObjectIdentity
tmnx7710Capability = _Tmnx7710Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3)
)
_Tmnx7710V3v0_ObjectIdentity = ObjectIdentity
tmnx7710V3v0 = _Tmnx7710V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 1)
)
_Tmnx7710V4v0_ObjectIdentity = ObjectIdentity
tmnx7710V4v0 = _Tmnx7710V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 2)
)
_Tmnx7710V5v0_ObjectIdentity = ObjectIdentity
tmnx7710V5v0 = _Tmnx7710V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 3)
)
_Tmnx7710V6v0_ObjectIdentity = ObjectIdentity
tmnx7710V6v0 = _Tmnx7710V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 4)
)
_Tmnx7710V6v1_ObjectIdentity = ObjectIdentity
tmnx7710V6v1 = _Tmnx7710V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 5)
)
_Tmnx7710V7v0_ObjectIdentity = ObjectIdentity
tmnx7710V7v0 = _Tmnx7710V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 6)
)
_Tmnx7710V8v0_ObjectIdentity = ObjectIdentity
tmnx7710V8v0 = _Tmnx7710V8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 7)
)
_Tmnx7750MGCapability_ObjectIdentity = ObjectIdentity
tmnx7750MGCapability = _Tmnx7750MGCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4)
)
_Tmnx7750MGV1v0_ObjectIdentity = ObjectIdentity
tmnx7750MGV1v0 = _Tmnx7750MGV1v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4, 1)
)
_TmnxSROSCapability_ObjectIdentity = ObjectIdentity
tmnxSROSCapability = _TmnxSROSCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5)
)
_TmnxSROSV8v0_ObjectIdentity = ObjectIdentity
tmnxSROSV8v0 = _TmnxSROSV8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5, 1)
)
_TmnxSROSV9v0_ObjectIdentity = ObjectIdentity
tmnxSROSV9v0 = _TmnxSROSV9v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5, 2)
)
_TmnxSROSV10v0_ObjectIdentity = ObjectIdentity
tmnxSROSV10v0 = _TmnxSROSV10v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5, 3)
)
_TmnxBasedProducts_ObjectIdentity = ObjectIdentity
tmnxBasedProducts = _TmnxBasedProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-GLOBAL-MIB",
    **{"timetra": timetra,
       "timetraReg": timetraReg,
       "timetraModules": timetraModules,
       "timetraGlobalMIBModule": timetraGlobalMIBModule,
       "timetraSRMIBModules": timetraSRMIBModules,
       "timetraCapabilityModule": timetraCapabilityModule,
       "timetra7750CapModule": timetra7750CapModule,
       "timetra7450CapModule": timetra7450CapModule,
       "timetra7710CapModule": timetra7710CapModule,
       "timetra7750MGCapModule": timetra7750MGCapModule,
       "timetraSROSCapModule": timetraSROSCapModule,
       "alcatelCommonMIBModules": alcatelCommonMIBModules,
       "timetraServiceRouters": timetraServiceRouters,
       "tmnxModelSR1Reg": tmnxModelSR1Reg,
       "tmnxModelSR4Reg": tmnxModelSR4Reg,
       "tmnxModelSR12Reg": tmnxModelSR12Reg,
       "tmnxModelSR7Reg": tmnxModelSR7Reg,
       "tmnxModelSR6Reg": tmnxModelSR6Reg,
       "tmnxModelSRc12Reg": tmnxModelSRc12Reg,
       "tmnxModelSRc4Reg": tmnxModelSRc4Reg,
       "timetraServiceSwitches": timetraServiceSwitches,
       "tmnxModelESS1Reg": tmnxModelESS1Reg,
       "tmnxModelESS4Reg": tmnxModelESS4Reg,
       "tmnxModelESS7Reg": tmnxModelESS7Reg,
       "tmnxModelESS12Reg": tmnxModelESS12Reg,
       "tmnxModelESS6Reg": tmnxModelESS6Reg,
       "tmnxModelESS6vReg": tmnxModelESS6vReg,
       "alcatel7710ServiceRouters": alcatel7710ServiceRouters,
       "tmnxModel7710SRc12Reg": tmnxModel7710SRc12Reg,
       "tmnxModel7710SRc4Reg": tmnxModel7710SRc4Reg,
       "alcatel7750MobileGateways": alcatel7750MobileGateways,
       "tmnxModel7750MGSR7Reg": tmnxModel7750MGSR7Reg,
       "tmnxModel7750MGSR12Reg": tmnxModel7750MGSR12Reg,
       "alcatel7950ExtServiceRouters": alcatel7950ExtServiceRouters,
       "tmnxModel7950XRS20Reg": tmnxModel7950XRS20Reg,
       "tmnxModel7950XRS16Reg": tmnxModel7950XRS16Reg,
       "timetraGeneric": timetraGeneric,
       "timetraProducts": timetraProducts,
       "tmnxSRMIB": tmnxSRMIB,
       "tmnxSRConfs": tmnxSRConfs,
       "tmnxSRObjs": tmnxSRObjs,
       "tmnxSRNotifyPrefix": tmnxSRNotifyPrefix,
       "tmnxESSMIB": tmnxESSMIB,
       "tmnxESSConfs": tmnxESSConfs,
       "tmnxESSObjs": tmnxESSObjs,
       "tmnxESSNotifyPrefix": tmnxESSNotifyPrefix,
       "alcatelCommonMIB": alcatelCommonMIB,
       "alcatelConformance": alcatelConformance,
       "alcatelObjects": alcatelObjects,
       "alcatelNotifyPrefix": alcatelNotifyPrefix,
       "tmnxMGMIB": tmnxMGMIB,
       "tmnxMGConfs": tmnxMGConfs,
       "tmnxMGObjs": tmnxMGObjs,
       "tmnxMGNotifyPrefix": tmnxMGNotifyPrefix,
       "tmnxAgentCapability": tmnxAgentCapability,
       "tmnx7750AgentCapability": tmnx7750AgentCapability,
       "tmnx7450AgentCapability": tmnx7450AgentCapability,
       "tmnx7710AgentCapability": tmnx7710AgentCapability,
       "tmnxProductCapability": tmnxProductCapability,
       "tmnx7750Capability": tmnx7750Capability,
       "tmnx7750V3v0": tmnx7750V3v0,
       "tmnx7750V4v0": tmnx7750V4v0,
       "tmnx7750V5v0": tmnx7750V5v0,
       "tmnx7750V6v0": tmnx7750V6v0,
       "tmnx7750V6v1": tmnx7750V6v1,
       "tmnx7750V7v0": tmnx7750V7v0,
       "tmnx7750V8v0": tmnx7750V8v0,
       "tmnx7450Capability": tmnx7450Capability,
       "tmnx7450V3v0": tmnx7450V3v0,
       "tmnx7450V4v0": tmnx7450V4v0,
       "tmnx7450V5v0": tmnx7450V5v0,
       "tmnx7450V6v0": tmnx7450V6v0,
       "tmnx7450V6v1": tmnx7450V6v1,
       "tmnx7450V7v0": tmnx7450V7v0,
       "tmnx7450V8v0": tmnx7450V8v0,
       "tmnx7710Capability": tmnx7710Capability,
       "tmnx7710V3v0": tmnx7710V3v0,
       "tmnx7710V4v0": tmnx7710V4v0,
       "tmnx7710V5v0": tmnx7710V5v0,
       "tmnx7710V6v0": tmnx7710V6v0,
       "tmnx7710V6v1": tmnx7710V6v1,
       "tmnx7710V7v0": tmnx7710V7v0,
       "tmnx7710V8v0": tmnx7710V8v0,
       "tmnx7750MGCapability": tmnx7750MGCapability,
       "tmnx7750MGV1v0": tmnx7750MGV1v0,
       "tmnxSROSCapability": tmnxSROSCapability,
       "tmnxSROSV8v0": tmnxSROSV8v0,
       "tmnxSROSV9v0": tmnxSROSV9v0,
       "tmnxSROSV10v0": tmnxSROSV10v0,
       "tmnxBasedProducts": tmnxBasedProducts}
)
