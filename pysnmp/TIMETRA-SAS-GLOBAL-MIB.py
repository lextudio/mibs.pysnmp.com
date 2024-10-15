# SNMP MIB module (TIMETRA-SAS-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:16 2024
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

(tmnxBasedProducts,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "tmnxBasedProducts")


# MODULE-IDENTITY

timetraSASGlobalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 1)
)
timetraSASGlobalMIBModule.setRevisions(
        ("1908-01-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TimetraServiceAccessSwitches_ObjectIdentity = ObjectIdentity
timetraServiceAccessSwitches = _TimetraServiceAccessSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2)
)
_TimetraSASRegistry_ObjectIdentity = ObjectIdentity
timetraSASRegistry = _TimetraSASRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1)
)
_TimetraSASModules_ObjectIdentity = ObjectIdentity
timetraSASModules = _TimetraSASModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1)
)
_TimetraSASMIBModules_ObjectIdentity = ObjectIdentity
timetraSASMIBModules = _TimetraSASMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 3)
)
_TimetraSASCapabilityModule_ObjectIdentity = ObjectIdentity
timetraSASCapabilityModule = _TimetraSASCapabilityModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4)
)
_TimetraSASE7210CapModule_ObjectIdentity = ObjectIdentity
timetraSASE7210CapModule = _TimetraSASE7210CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 1)
)
_TimetraSASM7210CapModule_ObjectIdentity = ObjectIdentity
timetraSASM7210CapModule = _TimetraSASM7210CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 2)
)
_TimetraSASX7210CapModule_ObjectIdentity = ObjectIdentity
timetraSASX7210CapModule = _TimetraSASX7210CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 3)
)
_TimetraSASD7210CapModule_ObjectIdentity = ObjectIdentity
timetraSASD7210CapModule = _TimetraSASD7210CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 4)
)
_TimetraSAST7210CapModule_ObjectIdentity = ObjectIdentity
timetraSAST7210CapModule = _TimetraSAST7210CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 5)
)
_TimetraSASR7210CapModule_ObjectIdentity = ObjectIdentity
timetraSASR7210CapModule = _TimetraSASR7210CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 6)
)
_TimetraSAS7210ServiceAccessSwitches_ObjectIdentity = ObjectIdentity
timetraSAS7210ServiceAccessSwitches = _TimetraSAS7210ServiceAccessSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2)
)
_TimetraSASModel7210SASEReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASEReg = _TimetraSASModel7210SASEReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASEReg.setStatus("current")
_TimetraSASModel7210SASM_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASM = _TimetraSASModel7210SASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2)
)
_TimetraSASModel7210SASMReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASMReg = _TimetraSASModel7210SASMReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASMReg.setStatus("current")
_TimetraSASModel7210SASM24F2XPReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASM24F2XPReg = _TimetraSASModel7210SASM24F2XPReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASM24F2XPReg.setStatus("current")
_TimetraSASModel7210SASM24F2XPETRReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASM24F2XPETRReg = _TimetraSASModel7210SASM24F2XPETRReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASM24F2XPETRReg.setStatus("current")
_TimetraSASModel7210SASX_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASX = _TimetraSASModel7210SASX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 3)
)
_TimetraSASModel7210SASX24F2XPReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASX24F2XPReg = _TimetraSASModel7210SASX24F2XPReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASX24F2XPReg.setStatus("current")
_TimetraSASModel7210SASD_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASD = _TimetraSASModel7210SASD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 4)
)
_TimetraSASModel7210SASDReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASDReg = _TimetraSASModel7210SASDReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASDReg.setStatus("current")
_TimetraSASModel7210SASDETRReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASDETRReg = _TimetraSASModel7210SASDETRReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASDETRReg.setStatus("current")
_TimetraSASModel7210SAST_ObjectIdentity = ObjectIdentity
timetraSASModel7210SAST = _TimetraSASModel7210SAST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 5)
)
_TimetraSASModel7210SASTReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASTReg = _TimetraSASModel7210SASTReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASTReg.setStatus("current")
_TimetraSASModel7210SASTETRReg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASTETRReg = _TimetraSASModel7210SASTETRReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASTETRReg.setStatus("current")
_TimetraSASModel7210SASR_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASR = _TimetraSASModel7210SASR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 6)
)
_TimetraSASModel7210SASR6Reg_ObjectIdentity = ObjectIdentity
timetraSASModel7210SASR6Reg = _TimetraSASModel7210SASR6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    timetraSASModel7210SASR6Reg.setStatus("current")
_TimetraSASMIB_ObjectIdentity = ObjectIdentity
timetraSASMIB = _TimetraSASMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2)
)
_TimetraSASConfs_ObjectIdentity = ObjectIdentity
timetraSASConfs = _TimetraSASConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1)
)
_TimetraSASObjs_ObjectIdentity = ObjectIdentity
timetraSASObjs = _TimetraSASObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2)
)
_TimetraSASNotifyPrefix_ObjectIdentity = ObjectIdentity
timetraSASNotifyPrefix = _TimetraSASNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3)
)
_TimetraSASProductCapability_ObjectIdentity = ObjectIdentity
timetraSASProductCapability = _TimetraSASProductCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3)
)
_TimetraSAS7210Capability_ObjectIdentity = ObjectIdentity
timetraSAS7210Capability = _TimetraSAS7210Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1)
)
_TimetraSAS7210V1v0_ObjectIdentity = ObjectIdentity
timetraSAS7210V1v0 = _TimetraSAS7210V1v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 1)
)
_TimetraSAS7210V1v1_ObjectIdentity = ObjectIdentity
timetraSAS7210V1v1 = _TimetraSAS7210V1v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 2)
)
_TimetraSAS7210V2v0_ObjectIdentity = ObjectIdentity
timetraSAS7210V2v0 = _TimetraSAS7210V2v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 3)
)
_TimetraSAS7210V3v0_ObjectIdentity = ObjectIdentity
timetraSAS7210V3v0 = _TimetraSAS7210V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 4)
)
_TimetraSAS7210V4v0_ObjectIdentity = ObjectIdentity
timetraSAS7210V4v0 = _TimetraSAS7210V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 5)
)
_TimetraSAS7210V5v0_ObjectIdentity = ObjectIdentity
timetraSAS7210V5v0 = _TimetraSAS7210V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 6)
)
_TimetraSAS7210V6v0_ObjectIdentity = ObjectIdentity
timetraSAS7210V6v0 = _TimetraSAS7210V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    **{"timetraServiceAccessSwitches": timetraServiceAccessSwitches,
       "timetraSASRegistry": timetraSASRegistry,
       "timetraSASModules": timetraSASModules,
       "timetraSASGlobalMIBModule": timetraSASGlobalMIBModule,
       "timetraSASMIBModules": timetraSASMIBModules,
       "timetraSASCapabilityModule": timetraSASCapabilityModule,
       "timetraSASE7210CapModule": timetraSASE7210CapModule,
       "timetraSASM7210CapModule": timetraSASM7210CapModule,
       "timetraSASX7210CapModule": timetraSASX7210CapModule,
       "timetraSASD7210CapModule": timetraSASD7210CapModule,
       "timetraSAST7210CapModule": timetraSAST7210CapModule,
       "timetraSASR7210CapModule": timetraSASR7210CapModule,
       "timetraSAS7210ServiceAccessSwitches": timetraSAS7210ServiceAccessSwitches,
       "timetraSASModel7210SASEReg": timetraSASModel7210SASEReg,
       "timetraSASModel7210SASM": timetraSASModel7210SASM,
       "timetraSASModel7210SASMReg": timetraSASModel7210SASMReg,
       "timetraSASModel7210SASM24F2XPReg": timetraSASModel7210SASM24F2XPReg,
       "timetraSASModel7210SASM24F2XPETRReg": timetraSASModel7210SASM24F2XPETRReg,
       "timetraSASModel7210SASX": timetraSASModel7210SASX,
       "timetraSASModel7210SASX24F2XPReg": timetraSASModel7210SASX24F2XPReg,
       "timetraSASModel7210SASD": timetraSASModel7210SASD,
       "timetraSASModel7210SASDReg": timetraSASModel7210SASDReg,
       "timetraSASModel7210SASDETRReg": timetraSASModel7210SASDETRReg,
       "timetraSASModel7210SAST": timetraSASModel7210SAST,
       "timetraSASModel7210SASTReg": timetraSASModel7210SASTReg,
       "timetraSASModel7210SASTETRReg": timetraSASModel7210SASTETRReg,
       "timetraSASModel7210SASR": timetraSASModel7210SASR,
       "timetraSASModel7210SASR6Reg": timetraSASModel7210SASR6Reg,
       "timetraSASMIB": timetraSASMIB,
       "timetraSASConfs": timetraSASConfs,
       "timetraSASObjs": timetraSASObjs,
       "timetraSASNotifyPrefix": timetraSASNotifyPrefix,
       "timetraSASProductCapability": timetraSASProductCapability,
       "timetraSAS7210Capability": timetraSAS7210Capability,
       "timetraSAS7210V1v0": timetraSAS7210V1v0,
       "timetraSAS7210V1v1": timetraSAS7210V1v1,
       "timetraSAS7210V2v0": timetraSAS7210V2v0,
       "timetraSAS7210V3v0": timetraSAS7210V3v0,
       "timetraSAS7210V4v0": timetraSAS7210V4v0,
       "timetraSAS7210V5v0": timetraSAS7210V5v0,
       "timetraSAS7210V6v0": timetraSAS7210V6v0}
)
