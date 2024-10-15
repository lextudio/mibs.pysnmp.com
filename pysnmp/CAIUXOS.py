# SNMP MIB module (CAIUXOS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAIUXOS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:21 2024
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
 NotificationType,
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
    "NotificationType",
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

_Cai_ObjectIdentity = ObjectIdentity
cai = _Cai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791)
)
_CaiSysMgr_ObjectIdentity = ObjectIdentity
caiSysMgr = _CaiSysMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2)
)
_AgentWorks_ObjectIdentity = ObjectIdentity
agentWorks = _AgentWorks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9)
)
_Unix_ObjectIdentity = ObjectIdentity
unix = _Unix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4)
)
_CaiUxOs_ObjectIdentity = ObjectIdentity
caiUxOs = _CaiUxOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5)
)
_UxsConfigGroup_ObjectIdentity = ObjectIdentity
uxsConfigGroup = _UxsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1)
)
_UxsConfigGeneralGroup_ObjectIdentity = ObjectIdentity
uxsConfigGeneralGroup = _UxsConfigGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1)
)
_UxsConfigGeneralAgentVersion_Type = DisplayString
_UxsConfigGeneralAgentVersion_Object = MibScalar
uxsConfigGeneralAgentVersion = _UxsConfigGeneralAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 1),
    _UxsConfigGeneralAgentVersion_Type()
)
uxsConfigGeneralAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralAgentVersion.setStatus("mandatory")
_UxsConfigGeneralColdStartTime_Type = DisplayString
_UxsConfigGeneralColdStartTime_Object = MibScalar
uxsConfigGeneralColdStartTime = _UxsConfigGeneralColdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 2),
    _UxsConfigGeneralColdStartTime_Type()
)
uxsConfigGeneralColdStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralColdStartTime.setStatus("mandatory")
_UxsConfigGeneralWarmStartTime_Type = DisplayString
_UxsConfigGeneralWarmStartTime_Object = MibScalar
uxsConfigGeneralWarmStartTime = _UxsConfigGeneralWarmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 3),
    _UxsConfigGeneralWarmStartTime_Type()
)
uxsConfigGeneralWarmStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralWarmStartTime.setStatus("mandatory")
_UxsConfigGeneralCPUPollTime_Type = DisplayString
_UxsConfigGeneralCPUPollTime_Object = MibScalar
uxsConfigGeneralCPUPollTime = _UxsConfigGeneralCPUPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 4),
    _UxsConfigGeneralCPUPollTime_Type()
)
uxsConfigGeneralCPUPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralCPUPollTime.setStatus("mandatory")
_UxsConfigGeneralLoadPollTime_Type = DisplayString
_UxsConfigGeneralLoadPollTime_Object = MibScalar
uxsConfigGeneralLoadPollTime = _UxsConfigGeneralLoadPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 5),
    _UxsConfigGeneralLoadPollTime_Type()
)
uxsConfigGeneralLoadPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralLoadPollTime.setStatus("mandatory")
_UxsConfigGeneralMemPollTime_Type = DisplayString
_UxsConfigGeneralMemPollTime_Object = MibScalar
uxsConfigGeneralMemPollTime = _UxsConfigGeneralMemPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 6),
    _UxsConfigGeneralMemPollTime_Type()
)
uxsConfigGeneralMemPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralMemPollTime.setStatus("mandatory")
_UxsConfigGeneralSwapPollTime_Type = DisplayString
_UxsConfigGeneralSwapPollTime_Object = MibScalar
uxsConfigGeneralSwapPollTime = _UxsConfigGeneralSwapPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 7),
    _UxsConfigGeneralSwapPollTime_Type()
)
uxsConfigGeneralSwapPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralSwapPollTime.setStatus("mandatory")
_UxsConfigGeneralFSysPollTime_Type = DisplayString
_UxsConfigGeneralFSysPollTime_Object = MibScalar
uxsConfigGeneralFSysPollTime = _UxsConfigGeneralFSysPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 8),
    _UxsConfigGeneralFSysPollTime_Type()
)
uxsConfigGeneralFSysPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralFSysPollTime.setStatus("mandatory")
_UxsConfigGeneralDiskPollTime_Type = DisplayString
_UxsConfigGeneralDiskPollTime_Object = MibScalar
uxsConfigGeneralDiskPollTime = _UxsConfigGeneralDiskPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 9),
    _UxsConfigGeneralDiskPollTime_Type()
)
uxsConfigGeneralDiskPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralDiskPollTime.setStatus("mandatory")
_UxsConfigGeneralFilePollTime_Type = DisplayString
_UxsConfigGeneralFilePollTime_Object = MibScalar
uxsConfigGeneralFilePollTime = _UxsConfigGeneralFilePollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 10),
    _UxsConfigGeneralFilePollTime_Type()
)
uxsConfigGeneralFilePollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralFilePollTime.setStatus("mandatory")
_UxsConfigGeneralProcPollTime_Type = DisplayString
_UxsConfigGeneralProcPollTime_Object = MibScalar
uxsConfigGeneralProcPollTime = _UxsConfigGeneralProcPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 11),
    _UxsConfigGeneralProcPollTime_Type()
)
uxsConfigGeneralProcPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralProcPollTime.setStatus("mandatory")
_UxsConfigGeneralPrnPollTime_Type = DisplayString
_UxsConfigGeneralPrnPollTime_Object = MibScalar
uxsConfigGeneralPrnPollTime = _UxsConfigGeneralPrnPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 12),
    _UxsConfigGeneralPrnPollTime_Type()
)
uxsConfigGeneralPrnPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralPrnPollTime.setStatus("mandatory")
_UxsConfigGeneralNetPollTime_Type = DisplayString
_UxsConfigGeneralNetPollTime_Object = MibScalar
uxsConfigGeneralNetPollTime = _UxsConfigGeneralNetPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 13),
    _UxsConfigGeneralNetPollTime_Type()
)
uxsConfigGeneralNetPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralNetPollTime.setStatus("mandatory")
_UxsConfigGeneralIPCPollTime_Type = DisplayString
_UxsConfigGeneralIPCPollTime_Object = MibScalar
uxsConfigGeneralIPCPollTime = _UxsConfigGeneralIPCPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 1, 14),
    _UxsConfigGeneralIPCPollTime_Type()
)
uxsConfigGeneralIPCPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigGeneralIPCPollTime.setStatus("mandatory")
_UxsConfigSysGroup_ObjectIdentity = ObjectIdentity
uxsConfigSysGroup = _UxsConfigSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2)
)
_UxsConfigSysNodeName_Type = DisplayString
_UxsConfigSysNodeName_Object = MibScalar
uxsConfigSysNodeName = _UxsConfigSysNodeName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 1),
    _UxsConfigSysNodeName_Type()
)
uxsConfigSysNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysNodeName.setStatus("mandatory")
_UxsConfigSysSystemName_Type = DisplayString
_UxsConfigSysSystemName_Object = MibScalar
uxsConfigSysSystemName = _UxsConfigSysSystemName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 2),
    _UxsConfigSysSystemName_Type()
)
uxsConfigSysSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysSystemName.setStatus("mandatory")
_UxsConfigSysRelease_Type = DisplayString
_UxsConfigSysRelease_Object = MibScalar
uxsConfigSysRelease = _UxsConfigSysRelease_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 3),
    _UxsConfigSysRelease_Type()
)
uxsConfigSysRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysRelease.setStatus("mandatory")
_UxsConfigSysVersion_Type = DisplayString
_UxsConfigSysVersion_Object = MibScalar
uxsConfigSysVersion = _UxsConfigSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 4),
    _UxsConfigSysVersion_Type()
)
uxsConfigSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysVersion.setStatus("mandatory")
_UxsConfigSysHardware_Type = DisplayString
_UxsConfigSysHardware_Object = MibScalar
uxsConfigSysHardware = _UxsConfigSysHardware_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 5),
    _UxsConfigSysHardware_Type()
)
uxsConfigSysHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysHardware.setStatus("mandatory")
_UxsConfigSysBootTime_Type = DisplayString
_UxsConfigSysBootTime_Object = MibScalar
uxsConfigSysBootTime = _UxsConfigSysBootTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 6),
    _UxsConfigSysBootTime_Type()
)
uxsConfigSysBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysBootTime.setStatus("mandatory")
_UxsConfigSysRunLevel_Type = DisplayString
_UxsConfigSysRunLevel_Object = MibScalar
uxsConfigSysRunLevel = _UxsConfigSysRunLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 2, 7),
    _UxsConfigSysRunLevel_Type()
)
uxsConfigSysRunLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigSysRunLevel.setStatus("mandatory")
_UxsConfigCPUGroup_ObjectIdentity = ObjectIdentity
uxsConfigCPUGroup = _UxsConfigCPUGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3)
)
_UxsConfigCPUPollInterval_Type = Integer32
_UxsConfigCPUPollInterval_Object = MibScalar
uxsConfigCPUPollInterval = _UxsConfigCPUPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 1),
    _UxsConfigCPUPollInterval_Type()
)
uxsConfigCPUPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPUPollInterval.setStatus("mandatory")


class _UxsConfigCPUPollMethod_Type(Integer32):
    """Custom type uxsConfigCPUPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigCPUPollMethod_Type.__name__ = "Integer32"
_UxsConfigCPUPollMethod_Object = MibScalar
uxsConfigCPUPollMethod = _UxsConfigCPUPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 2),
    _UxsConfigCPUPollMethod_Type()
)
uxsConfigCPUPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPUPollMethod.setStatus("mandatory")
_UxsConfigCPULag_Type = Integer32
_UxsConfigCPULag_Object = MibScalar
uxsConfigCPULag = _UxsConfigCPULag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 3),
    _UxsConfigCPULag_Type()
)
uxsConfigCPULag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPULag.setStatus("mandatory")
_UxsConfigCPUWarn_Type = DisplayString
_UxsConfigCPUWarn_Object = MibScalar
uxsConfigCPUWarn = _UxsConfigCPUWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 4),
    _UxsConfigCPUWarn_Type()
)
uxsConfigCPUWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPUWarn.setStatus("mandatory")
_UxsConfigCPUCrit_Type = DisplayString
_UxsConfigCPUCrit_Object = MibScalar
uxsConfigCPUCrit = _UxsConfigCPUCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 5),
    _UxsConfigCPUCrit_Type()
)
uxsConfigCPUCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPUCrit.setStatus("mandatory")


class _UxsConfigCPUMonitor_Type(Integer32):
    """Custom type uxsConfigCPUMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigCPUMonitor_Type.__name__ = "Integer32"
_UxsConfigCPUMonitor_Object = MibScalar
uxsConfigCPUMonitor = _UxsConfigCPUMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 6),
    _UxsConfigCPUMonitor_Type()
)
uxsConfigCPUMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPUMonitor.setStatus("mandatory")


class _UxsConfigCPULossAction_Type(Integer32):
    """Custom type uxsConfigCPULossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsConfigCPULossAction_Type.__name__ = "Integer32"
_UxsConfigCPULossAction_Object = MibScalar
uxsConfigCPULossAction = _UxsConfigCPULossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 3, 7),
    _UxsConfigCPULossAction_Type()
)
uxsConfigCPULossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigCPULossAction.setStatus("mandatory")
_UxsConfigLoadGroup_ObjectIdentity = ObjectIdentity
uxsConfigLoadGroup = _UxsConfigLoadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 4)
)
_UxsConfigLoadPollInterval_Type = Integer32
_UxsConfigLoadPollInterval_Object = MibScalar
uxsConfigLoadPollInterval = _UxsConfigLoadPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 4, 1),
    _UxsConfigLoadPollInterval_Type()
)
uxsConfigLoadPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigLoadPollInterval.setStatus("mandatory")


class _UxsConfigLoadPollMethod_Type(Integer32):
    """Custom type uxsConfigLoadPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigLoadPollMethod_Type.__name__ = "Integer32"
_UxsConfigLoadPollMethod_Object = MibScalar
uxsConfigLoadPollMethod = _UxsConfigLoadPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 4, 2),
    _UxsConfigLoadPollMethod_Type()
)
uxsConfigLoadPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigLoadPollMethod.setStatus("mandatory")
_UxsConfigMemGroup_ObjectIdentity = ObjectIdentity
uxsConfigMemGroup = _UxsConfigMemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 5)
)
_UxsConfigMemPollInterval_Type = Integer32
_UxsConfigMemPollInterval_Object = MibScalar
uxsConfigMemPollInterval = _UxsConfigMemPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 5, 1),
    _UxsConfigMemPollInterval_Type()
)
uxsConfigMemPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigMemPollInterval.setStatus("mandatory")


class _UxsConfigMemPollMethod_Type(Integer32):
    """Custom type uxsConfigMemPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigMemPollMethod_Type.__name__ = "Integer32"
_UxsConfigMemPollMethod_Object = MibScalar
uxsConfigMemPollMethod = _UxsConfigMemPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 5, 2),
    _UxsConfigMemPollMethod_Type()
)
uxsConfigMemPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigMemPollMethod.setStatus("mandatory")
_UxsConfigSwapGroup_ObjectIdentity = ObjectIdentity
uxsConfigSwapGroup = _UxsConfigSwapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6)
)
_UxsConfigSwapPollInterval_Type = Integer32
_UxsConfigSwapPollInterval_Object = MibScalar
uxsConfigSwapPollInterval = _UxsConfigSwapPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 1),
    _UxsConfigSwapPollInterval_Type()
)
uxsConfigSwapPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapPollInterval.setStatus("mandatory")


class _UxsConfigSwapPollMethod_Type(Integer32):
    """Custom type uxsConfigSwapPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigSwapPollMethod_Type.__name__ = "Integer32"
_UxsConfigSwapPollMethod_Object = MibScalar
uxsConfigSwapPollMethod = _UxsConfigSwapPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 2),
    _UxsConfigSwapPollMethod_Type()
)
uxsConfigSwapPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapPollMethod.setStatus("mandatory")
_UxsConfigSwapLag_Type = Integer32
_UxsConfigSwapLag_Object = MibScalar
uxsConfigSwapLag = _UxsConfigSwapLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 3),
    _UxsConfigSwapLag_Type()
)
uxsConfigSwapLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapLag.setStatus("mandatory")
_UxsConfigSwapWarn_Type = DisplayString
_UxsConfigSwapWarn_Object = MibScalar
uxsConfigSwapWarn = _UxsConfigSwapWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 4),
    _UxsConfigSwapWarn_Type()
)
uxsConfigSwapWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapWarn.setStatus("mandatory")
_UxsConfigSwapCrit_Type = DisplayString
_UxsConfigSwapCrit_Object = MibScalar
uxsConfigSwapCrit = _UxsConfigSwapCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 5),
    _UxsConfigSwapCrit_Type()
)
uxsConfigSwapCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapCrit.setStatus("mandatory")


class _UxsConfigSwapMonitor_Type(Integer32):
    """Custom type uxsConfigSwapMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigSwapMonitor_Type.__name__ = "Integer32"
_UxsConfigSwapMonitor_Object = MibScalar
uxsConfigSwapMonitor = _UxsConfigSwapMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 6),
    _UxsConfigSwapMonitor_Type()
)
uxsConfigSwapMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapMonitor.setStatus("mandatory")


class _UxsConfigSwapLossAction_Type(Integer32):
    """Custom type uxsConfigSwapLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsConfigSwapLossAction_Type.__name__ = "Integer32"
_UxsConfigSwapLossAction_Object = MibScalar
uxsConfigSwapLossAction = _UxsConfigSwapLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 6, 7),
    _UxsConfigSwapLossAction_Type()
)
uxsConfigSwapLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigSwapLossAction.setStatus("mandatory")
_UxsConfigFSysGroup_ObjectIdentity = ObjectIdentity
uxsConfigFSysGroup = _UxsConfigFSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7)
)
_UxsConfigFSysPollInterval_Type = Integer32
_UxsConfigFSysPollInterval_Object = MibScalar
uxsConfigFSysPollInterval = _UxsConfigFSysPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 1),
    _UxsConfigFSysPollInterval_Type()
)
uxsConfigFSysPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysPollInterval.setStatus("mandatory")


class _UxsConfigFSysPollMethod_Type(Integer32):
    """Custom type uxsConfigFSysPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigFSysPollMethod_Type.__name__ = "Integer32"
_UxsConfigFSysPollMethod_Object = MibScalar
uxsConfigFSysPollMethod = _UxsConfigFSysPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 2),
    _UxsConfigFSysPollMethod_Type()
)
uxsConfigFSysPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysPollMethod.setStatus("mandatory")
_UxsConfigFSysSpaceWarn_Type = DisplayString
_UxsConfigFSysSpaceWarn_Object = MibScalar
uxsConfigFSysSpaceWarn = _UxsConfigFSysSpaceWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 3),
    _UxsConfigFSysSpaceWarn_Type()
)
uxsConfigFSysSpaceWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysSpaceWarn.setStatus("mandatory")
_UxsConfigFSysSpaceCrit_Type = DisplayString
_UxsConfigFSysSpaceCrit_Object = MibScalar
uxsConfigFSysSpaceCrit = _UxsConfigFSysSpaceCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 4),
    _UxsConfigFSysSpaceCrit_Type()
)
uxsConfigFSysSpaceCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysSpaceCrit.setStatus("mandatory")


class _UxsConfigFSysSpaceMonitor_Type(Integer32):
    """Custom type uxsConfigFSysSpaceMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigFSysSpaceMonitor_Type.__name__ = "Integer32"
_UxsConfigFSysSpaceMonitor_Object = MibScalar
uxsConfigFSysSpaceMonitor = _UxsConfigFSysSpaceMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 5),
    _UxsConfigFSysSpaceMonitor_Type()
)
uxsConfigFSysSpaceMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysSpaceMonitor.setStatus("mandatory")
_UxsConfigFSysSpaceDWarn_Type = DisplayString
_UxsConfigFSysSpaceDWarn_Object = MibScalar
uxsConfigFSysSpaceDWarn = _UxsConfigFSysSpaceDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 6),
    _UxsConfigFSysSpaceDWarn_Type()
)
uxsConfigFSysSpaceDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysSpaceDWarn.setStatus("mandatory")
_UxsConfigFSysSpaceDCrit_Type = DisplayString
_UxsConfigFSysSpaceDCrit_Object = MibScalar
uxsConfigFSysSpaceDCrit = _UxsConfigFSysSpaceDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 7),
    _UxsConfigFSysSpaceDCrit_Type()
)
uxsConfigFSysSpaceDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysSpaceDCrit.setStatus("mandatory")


class _UxsConfigFSysSpaceDMonitor_Type(Integer32):
    """Custom type uxsConfigFSysSpaceDMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigFSysSpaceDMonitor_Type.__name__ = "Integer32"
_UxsConfigFSysSpaceDMonitor_Object = MibScalar
uxsConfigFSysSpaceDMonitor = _UxsConfigFSysSpaceDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 8),
    _UxsConfigFSysSpaceDMonitor_Type()
)
uxsConfigFSysSpaceDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysSpaceDMonitor.setStatus("mandatory")
_UxsConfigFSysInodesWarn_Type = DisplayString
_UxsConfigFSysInodesWarn_Object = MibScalar
uxsConfigFSysInodesWarn = _UxsConfigFSysInodesWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 9),
    _UxsConfigFSysInodesWarn_Type()
)
uxsConfigFSysInodesWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysInodesWarn.setStatus("mandatory")
_UxsConfigFSysInodesCrit_Type = DisplayString
_UxsConfigFSysInodesCrit_Object = MibScalar
uxsConfigFSysInodesCrit = _UxsConfigFSysInodesCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 10),
    _UxsConfigFSysInodesCrit_Type()
)
uxsConfigFSysInodesCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysInodesCrit.setStatus("mandatory")


class _UxsConfigFSysInodesMonitor_Type(Integer32):
    """Custom type uxsConfigFSysInodesMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigFSysInodesMonitor_Type.__name__ = "Integer32"
_UxsConfigFSysInodesMonitor_Object = MibScalar
uxsConfigFSysInodesMonitor = _UxsConfigFSysInodesMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 11),
    _UxsConfigFSysInodesMonitor_Type()
)
uxsConfigFSysInodesMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysInodesMonitor.setStatus("mandatory")
_UxsConfigFSysInodesDWarn_Type = DisplayString
_UxsConfigFSysInodesDWarn_Object = MibScalar
uxsConfigFSysInodesDWarn = _UxsConfigFSysInodesDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 12),
    _UxsConfigFSysInodesDWarn_Type()
)
uxsConfigFSysInodesDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysInodesDWarn.setStatus("mandatory")
_UxsConfigFSysInodesDCrit_Type = DisplayString
_UxsConfigFSysInodesDCrit_Object = MibScalar
uxsConfigFSysInodesDCrit = _UxsConfigFSysInodesDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 13),
    _UxsConfigFSysInodesDCrit_Type()
)
uxsConfigFSysInodesDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysInodesDCrit.setStatus("mandatory")


class _UxsConfigFSysInodesDMonitor_Type(Integer32):
    """Custom type uxsConfigFSysInodesDMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigFSysInodesDMonitor_Type.__name__ = "Integer32"
_UxsConfigFSysInodesDMonitor_Object = MibScalar
uxsConfigFSysInodesDMonitor = _UxsConfigFSysInodesDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 14),
    _UxsConfigFSysInodesDMonitor_Type()
)
uxsConfigFSysInodesDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysInodesDMonitor.setStatus("mandatory")


class _UxsConfigFSysMountedMonitor_Type(Integer32):
    """Custom type uxsConfigFSysMountedMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsConfigFSysMountedMonitor_Type.__name__ = "Integer32"
_UxsConfigFSysMountedMonitor_Object = MibScalar
uxsConfigFSysMountedMonitor = _UxsConfigFSysMountedMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 15),
    _UxsConfigFSysMountedMonitor_Type()
)
uxsConfigFSysMountedMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysMountedMonitor.setStatus("mandatory")


class _UxsConfigFSysLossAction_Type(Integer32):
    """Custom type uxsConfigFSysLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsConfigFSysLossAction_Type.__name__ = "Integer32"
_UxsConfigFSysLossAction_Object = MibScalar
uxsConfigFSysLossAction = _UxsConfigFSysLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 16),
    _UxsConfigFSysLossAction_Type()
)
uxsConfigFSysLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysLossAction.setStatus("mandatory")
_UxsConfigFSysNameAdd_Type = DisplayString
_UxsConfigFSysNameAdd_Object = MibScalar
uxsConfigFSysNameAdd = _UxsConfigFSysNameAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 17),
    _UxsConfigFSysNameAdd_Type()
)
uxsConfigFSysNameAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysNameAdd.setStatus("mandatory")
_UxsConfigFSysNameRemove_Type = DisplayString
_UxsConfigFSysNameRemove_Object = MibScalar
uxsConfigFSysNameRemove = _UxsConfigFSysNameRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 7, 18),
    _UxsConfigFSysNameRemove_Type()
)
uxsConfigFSysNameRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFSysNameRemove.setStatus("mandatory")
_UxsConfigDiskGroup_ObjectIdentity = ObjectIdentity
uxsConfigDiskGroup = _UxsConfigDiskGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8)
)
_UxsConfigDiskPollInterval_Type = Integer32
_UxsConfigDiskPollInterval_Object = MibScalar
uxsConfigDiskPollInterval = _UxsConfigDiskPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 1),
    _UxsConfigDiskPollInterval_Type()
)
uxsConfigDiskPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskPollInterval.setStatus("mandatory")


class _UxsConfigDiskPollMethod_Type(Integer32):
    """Custom type uxsConfigDiskPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigDiskPollMethod_Type.__name__ = "Integer32"
_UxsConfigDiskPollMethod_Object = MibScalar
uxsConfigDiskPollMethod = _UxsConfigDiskPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 2),
    _UxsConfigDiskPollMethod_Type()
)
uxsConfigDiskPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskPollMethod.setStatus("mandatory")
_UxsConfigDiskTPutWarn_Type = Integer32
_UxsConfigDiskTPutWarn_Object = MibScalar
uxsConfigDiskTPutWarn = _UxsConfigDiskTPutWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 3),
    _UxsConfigDiskTPutWarn_Type()
)
uxsConfigDiskTPutWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskTPutWarn.setStatus("mandatory")
_UxsConfigDiskTPutCrit_Type = Integer32
_UxsConfigDiskTPutCrit_Object = MibScalar
uxsConfigDiskTPutCrit = _UxsConfigDiskTPutCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 4),
    _UxsConfigDiskTPutCrit_Type()
)
uxsConfigDiskTPutCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskTPutCrit.setStatus("mandatory")


class _UxsConfigDiskTPutMonitor_Type(Integer32):
    """Custom type uxsConfigDiskTPutMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigDiskTPutMonitor_Type.__name__ = "Integer32"
_UxsConfigDiskTPutMonitor_Object = MibScalar
uxsConfigDiskTPutMonitor = _UxsConfigDiskTPutMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 5),
    _UxsConfigDiskTPutMonitor_Type()
)
uxsConfigDiskTPutMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskTPutMonitor.setStatus("mandatory")


class _UxsConfigDiskLossAction_Type(Integer32):
    """Custom type uxsConfigDiskLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsConfigDiskLossAction_Type.__name__ = "Integer32"
_UxsConfigDiskLossAction_Object = MibScalar
uxsConfigDiskLossAction = _UxsConfigDiskLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 6),
    _UxsConfigDiskLossAction_Type()
)
uxsConfigDiskLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskLossAction.setStatus("mandatory")
_UxsConfigDiskNameAdd_Type = DisplayString
_UxsConfigDiskNameAdd_Object = MibScalar
uxsConfigDiskNameAdd = _UxsConfigDiskNameAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 7),
    _UxsConfigDiskNameAdd_Type()
)
uxsConfigDiskNameAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskNameAdd.setStatus("mandatory")
_UxsConfigDiskNameRemove_Type = DisplayString
_UxsConfigDiskNameRemove_Object = MibScalar
uxsConfigDiskNameRemove = _UxsConfigDiskNameRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 8, 8),
    _UxsConfigDiskNameRemove_Type()
)
uxsConfigDiskNameRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigDiskNameRemove.setStatus("mandatory")
_UxsConfigFileGroup_ObjectIdentity = ObjectIdentity
uxsConfigFileGroup = _UxsConfigFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9)
)
_UxsConfigFilePollInterval_Type = Integer32
_UxsConfigFilePollInterval_Object = MibScalar
uxsConfigFilePollInterval = _UxsConfigFilePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 1),
    _UxsConfigFilePollInterval_Type()
)
uxsConfigFilePollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFilePollInterval.setStatus("mandatory")


class _UxsConfigFilePollMethod_Type(Integer32):
    """Custom type uxsConfigFilePollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigFilePollMethod_Type.__name__ = "Integer32"
_UxsConfigFilePollMethod_Object = MibScalar
uxsConfigFilePollMethod = _UxsConfigFilePollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 2),
    _UxsConfigFilePollMethod_Type()
)
uxsConfigFilePollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFilePollMethod.setStatus("mandatory")
_UxsConfigFileDesc_Type = DisplayString
_UxsConfigFileDesc_Object = MibScalar
uxsConfigFileDesc = _UxsConfigFileDesc_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 3),
    _UxsConfigFileDesc_Type()
)
uxsConfigFileDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileDesc.setStatus("mandatory")


class _UxsConfigFileExist_Type(Integer32):
    """Custom type uxsConfigFileExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_UxsConfigFileExist_Type.__name__ = "Integer32"
_UxsConfigFileExist_Object = MibScalar
uxsConfigFileExist = _UxsConfigFileExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 4),
    _UxsConfigFileExist_Type()
)
uxsConfigFileExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileExist.setStatus("mandatory")


class _UxsConfigFileExistMonitor_Type(Integer32):
    """Custom type uxsConfigFileExistMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsConfigFileExistMonitor_Type.__name__ = "Integer32"
_UxsConfigFileExistMonitor_Object = MibScalar
uxsConfigFileExistMonitor = _UxsConfigFileExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 5),
    _UxsConfigFileExistMonitor_Type()
)
uxsConfigFileExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileExistMonitor.setStatus("mandatory")


class _UxsConfigFileModTimeMonitor_Type(Integer32):
    """Custom type uxsConfigFileModTimeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsConfigFileModTimeMonitor_Type.__name__ = "Integer32"
_UxsConfigFileModTimeMonitor_Object = MibScalar
uxsConfigFileModTimeMonitor = _UxsConfigFileModTimeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 6),
    _UxsConfigFileModTimeMonitor_Type()
)
uxsConfigFileModTimeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileModTimeMonitor.setStatus("mandatory")
_UxsConfigFileSizeWarn_Type = DisplayString
_UxsConfigFileSizeWarn_Object = MibScalar
uxsConfigFileSizeWarn = _UxsConfigFileSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 7),
    _UxsConfigFileSizeWarn_Type()
)
uxsConfigFileSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileSizeWarn.setStatus("mandatory")
_UxsConfigFileSizeCrit_Type = DisplayString
_UxsConfigFileSizeCrit_Object = MibScalar
uxsConfigFileSizeCrit = _UxsConfigFileSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 8),
    _UxsConfigFileSizeCrit_Type()
)
uxsConfigFileSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileSizeCrit.setStatus("mandatory")


class _UxsConfigFileSizeMonitor_Type(Integer32):
    """Custom type uxsConfigFileSizeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigFileSizeMonitor_Type.__name__ = "Integer32"
_UxsConfigFileSizeMonitor_Object = MibScalar
uxsConfigFileSizeMonitor = _UxsConfigFileSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 9),
    _UxsConfigFileSizeMonitor_Type()
)
uxsConfigFileSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileSizeMonitor.setStatus("mandatory")
_UxsConfigFileSizeDWarn_Type = DisplayString
_UxsConfigFileSizeDWarn_Object = MibScalar
uxsConfigFileSizeDWarn = _UxsConfigFileSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 10),
    _UxsConfigFileSizeDWarn_Type()
)
uxsConfigFileSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileSizeDWarn.setStatus("mandatory")
_UxsConfigFileSizeDCrit_Type = DisplayString
_UxsConfigFileSizeDCrit_Object = MibScalar
uxsConfigFileSizeDCrit = _UxsConfigFileSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 11),
    _UxsConfigFileSizeDCrit_Type()
)
uxsConfigFileSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileSizeDCrit.setStatus("mandatory")


class _UxsConfigFileSizeDMonitor_Type(Integer32):
    """Custom type uxsConfigFileSizeDMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigFileSizeDMonitor_Type.__name__ = "Integer32"
_UxsConfigFileSizeDMonitor_Object = MibScalar
uxsConfigFileSizeDMonitor = _UxsConfigFileSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 12),
    _UxsConfigFileSizeDMonitor_Type()
)
uxsConfigFileSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileSizeDMonitor.setStatus("mandatory")
_UxsConfigFileNameAdd_Type = DisplayString
_UxsConfigFileNameAdd_Object = MibScalar
uxsConfigFileNameAdd = _UxsConfigFileNameAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 13),
    _UxsConfigFileNameAdd_Type()
)
uxsConfigFileNameAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileNameAdd.setStatus("mandatory")
_UxsConfigFileNameRemove_Type = DisplayString
_UxsConfigFileNameRemove_Object = MibScalar
uxsConfigFileNameRemove = _UxsConfigFileNameRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 9, 14),
    _UxsConfigFileNameRemove_Type()
)
uxsConfigFileNameRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigFileNameRemove.setStatus("mandatory")
_UxsConfigProcGroup_ObjectIdentity = ObjectIdentity
uxsConfigProcGroup = _UxsConfigProcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10)
)
_UxsConfigProcPollInterval_Type = Integer32
_UxsConfigProcPollInterval_Object = MibScalar
uxsConfigProcPollInterval = _UxsConfigProcPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 1),
    _UxsConfigProcPollInterval_Type()
)
uxsConfigProcPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcPollInterval.setStatus("mandatory")


class _UxsConfigProcPollMethod_Type(Integer32):
    """Custom type uxsConfigProcPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigProcPollMethod_Type.__name__ = "Integer32"
_UxsConfigProcPollMethod_Object = MibScalar
uxsConfigProcPollMethod = _UxsConfigProcPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 2),
    _UxsConfigProcPollMethod_Type()
)
uxsConfigProcPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcPollMethod.setStatus("mandatory")
_UxsConfigProcPath_Type = DisplayString
_UxsConfigProcPath_Object = MibScalar
uxsConfigProcPath = _UxsConfigProcPath_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 3),
    _UxsConfigProcPath_Type()
)
uxsConfigProcPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcPath.setStatus("mandatory")
_UxsConfigProcArgs_Type = DisplayString
_UxsConfigProcArgs_Object = MibScalar
uxsConfigProcArgs = _UxsConfigProcArgs_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 4),
    _UxsConfigProcArgs_Type()
)
uxsConfigProcArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcArgs.setStatus("mandatory")
_UxsConfigProcUsers_Type = DisplayString
_UxsConfigProcUsers_Object = MibScalar
uxsConfigProcUsers = _UxsConfigProcUsers_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 5),
    _UxsConfigProcUsers_Type()
)
uxsConfigProcUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcUsers.setStatus("mandatory")
_UxsConfigProcInstMin_Type = Integer32
_UxsConfigProcInstMin_Object = MibScalar
uxsConfigProcInstMin = _UxsConfigProcInstMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 6),
    _UxsConfigProcInstMin_Type()
)
uxsConfigProcInstMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcInstMin.setStatus("mandatory")
_UxsConfigProcInstMax_Type = Integer32
_UxsConfigProcInstMax_Object = MibScalar
uxsConfigProcInstMax = _UxsConfigProcInstMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 7),
    _UxsConfigProcInstMax_Type()
)
uxsConfigProcInstMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcInstMax.setStatus("mandatory")


class _UxsConfigProcInstMonitor_Type(Integer32):
    """Custom type uxsConfigProcInstMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsConfigProcInstMonitor_Type.__name__ = "Integer32"
_UxsConfigProcInstMonitor_Object = MibScalar
uxsConfigProcInstMonitor = _UxsConfigProcInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 8),
    _UxsConfigProcInstMonitor_Type()
)
uxsConfigProcInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcInstMonitor.setStatus("mandatory")
_UxsConfigProcChldMin_Type = Integer32
_UxsConfigProcChldMin_Object = MibScalar
uxsConfigProcChldMin = _UxsConfigProcChldMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 9),
    _UxsConfigProcChldMin_Type()
)
uxsConfigProcChldMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcChldMin.setStatus("mandatory")
_UxsConfigProcChldMax_Type = Integer32
_UxsConfigProcChldMax_Object = MibScalar
uxsConfigProcChldMax = _UxsConfigProcChldMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 10),
    _UxsConfigProcChldMax_Type()
)
uxsConfigProcChldMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcChldMax.setStatus("mandatory")


class _UxsConfigProcChldMonitor_Type(Integer32):
    """Custom type uxsConfigProcChldMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsConfigProcChldMonitor_Type.__name__ = "Integer32"
_UxsConfigProcChldMonitor_Object = MibScalar
uxsConfigProcChldMonitor = _UxsConfigProcChldMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 11),
    _UxsConfigProcChldMonitor_Type()
)
uxsConfigProcChldMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcChldMonitor.setStatus("mandatory")
_UxsConfigProcSizeMin_Type = Integer32
_UxsConfigProcSizeMin_Object = MibScalar
uxsConfigProcSizeMin = _UxsConfigProcSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 12),
    _UxsConfigProcSizeMin_Type()
)
uxsConfigProcSizeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcSizeMin.setStatus("mandatory")
_UxsConfigProcSizeMax_Type = Integer32
_UxsConfigProcSizeMax_Object = MibScalar
uxsConfigProcSizeMax = _UxsConfigProcSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 13),
    _UxsConfigProcSizeMax_Type()
)
uxsConfigProcSizeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcSizeMax.setStatus("mandatory")


class _UxsConfigProcSizeMonitor_Type(Integer32):
    """Custom type uxsConfigProcSizeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsConfigProcSizeMonitor_Type.__name__ = "Integer32"
_UxsConfigProcSizeMonitor_Object = MibScalar
uxsConfigProcSizeMonitor = _UxsConfigProcSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 14),
    _UxsConfigProcSizeMonitor_Type()
)
uxsConfigProcSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcSizeMonitor.setStatus("mandatory")
_UxsConfigProcCPUWarn_Type = Integer32
_UxsConfigProcCPUWarn_Object = MibScalar
uxsConfigProcCPUWarn = _UxsConfigProcCPUWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 15),
    _UxsConfigProcCPUWarn_Type()
)
uxsConfigProcCPUWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcCPUWarn.setStatus("mandatory")
_UxsConfigProcCPUCrit_Type = Integer32
_UxsConfigProcCPUCrit_Object = MibScalar
uxsConfigProcCPUCrit = _UxsConfigProcCPUCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 16),
    _UxsConfigProcCPUCrit_Type()
)
uxsConfigProcCPUCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcCPUCrit.setStatus("mandatory")


class _UxsConfigProcCPUMonitor_Type(Integer32):
    """Custom type uxsConfigProcCPUMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigProcCPUMonitor_Type.__name__ = "Integer32"
_UxsConfigProcCPUMonitor_Object = MibScalar
uxsConfigProcCPUMonitor = _UxsConfigProcCPUMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 17),
    _UxsConfigProcCPUMonitor_Type()
)
uxsConfigProcCPUMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcCPUMonitor.setStatus("mandatory")
_UxsConfigProcNameAdd_Type = DisplayString
_UxsConfigProcNameAdd_Object = MibScalar
uxsConfigProcNameAdd = _UxsConfigProcNameAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 18),
    _UxsConfigProcNameAdd_Type()
)
uxsConfigProcNameAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcNameAdd.setStatus("mandatory")
_UxsConfigProcNameRemove_Type = DisplayString
_UxsConfigProcNameRemove_Object = MibScalar
uxsConfigProcNameRemove = _UxsConfigProcNameRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 19),
    _UxsConfigProcNameRemove_Type()
)
uxsConfigProcNameRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigProcNameRemove.setStatus("mandatory")
_UxsConfigProcNameSig_Type = Integer32
_UxsConfigProcNameSig_Object = MibScalar
uxsConfigProcNameSig = _UxsConfigProcNameSig_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 20),
    _UxsConfigProcNameSig_Type()
)
uxsConfigProcNameSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigProcNameSig.setStatus("mandatory")
_UxsConfigProcPathSig_Type = Integer32
_UxsConfigProcPathSig_Object = MibScalar
uxsConfigProcPathSig = _UxsConfigProcPathSig_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 21),
    _UxsConfigProcPathSig_Type()
)
uxsConfigProcPathSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigProcPathSig.setStatus("mandatory")
_UxsConfigProcArgsSig_Type = Integer32
_UxsConfigProcArgsSig_Object = MibScalar
uxsConfigProcArgsSig = _UxsConfigProcArgsSig_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 10, 22),
    _UxsConfigProcArgsSig_Type()
)
uxsConfigProcArgsSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsConfigProcArgsSig.setStatus("mandatory")
_UxsConfigPrnGroup_ObjectIdentity = ObjectIdentity
uxsConfigPrnGroup = _UxsConfigPrnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11)
)
_UxsConfigPrnPollInterval_Type = Integer32
_UxsConfigPrnPollInterval_Object = MibScalar
uxsConfigPrnPollInterval = _UxsConfigPrnPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 1),
    _UxsConfigPrnPollInterval_Type()
)
uxsConfigPrnPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnPollInterval.setStatus("mandatory")


class _UxsConfigPrnPollMethod_Type(Integer32):
    """Custom type uxsConfigPrnPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigPrnPollMethod_Type.__name__ = "Integer32"
_UxsConfigPrnPollMethod_Object = MibScalar
uxsConfigPrnPollMethod = _UxsConfigPrnPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 2),
    _UxsConfigPrnPollMethod_Type()
)
uxsConfigPrnPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnPollMethod.setStatus("mandatory")
_UxsConfigPrnDesc_Type = DisplayString
_UxsConfigPrnDesc_Object = MibScalar
uxsConfigPrnDesc = _UxsConfigPrnDesc_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 3),
    _UxsConfigPrnDesc_Type()
)
uxsConfigPrnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnDesc.setStatus("mandatory")
_UxsConfigPrnItemsWarn_Type = Integer32
_UxsConfigPrnItemsWarn_Object = MibScalar
uxsConfigPrnItemsWarn = _UxsConfigPrnItemsWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 4),
    _UxsConfigPrnItemsWarn_Type()
)
uxsConfigPrnItemsWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnItemsWarn.setStatus("mandatory")
_UxsConfigPrnItemsCrit_Type = Integer32
_UxsConfigPrnItemsCrit_Object = MibScalar
uxsConfigPrnItemsCrit = _UxsConfigPrnItemsCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 5),
    _UxsConfigPrnItemsCrit_Type()
)
uxsConfigPrnItemsCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnItemsCrit.setStatus("mandatory")


class _UxsConfigPrnItemsMonitor_Type(Integer32):
    """Custom type uxsConfigPrnItemsMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigPrnItemsMonitor_Type.__name__ = "Integer32"
_UxsConfigPrnItemsMonitor_Object = MibScalar
uxsConfigPrnItemsMonitor = _UxsConfigPrnItemsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 6),
    _UxsConfigPrnItemsMonitor_Type()
)
uxsConfigPrnItemsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnItemsMonitor.setStatus("mandatory")


class _UxsConfigPrnLossAction_Type(Integer32):
    """Custom type uxsConfigPrnLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsConfigPrnLossAction_Type.__name__ = "Integer32"
_UxsConfigPrnLossAction_Object = MibScalar
uxsConfigPrnLossAction = _UxsConfigPrnLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 7),
    _UxsConfigPrnLossAction_Type()
)
uxsConfigPrnLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnLossAction.setStatus("mandatory")
_UxsConfigPrnNameAdd_Type = DisplayString
_UxsConfigPrnNameAdd_Object = MibScalar
uxsConfigPrnNameAdd = _UxsConfigPrnNameAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 8),
    _UxsConfigPrnNameAdd_Type()
)
uxsConfigPrnNameAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnNameAdd.setStatus("mandatory")
_UxsConfigPrnNameRemove_Type = DisplayString
_UxsConfigPrnNameRemove_Object = MibScalar
uxsConfigPrnNameRemove = _UxsConfigPrnNameRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 11, 9),
    _UxsConfigPrnNameRemove_Type()
)
uxsConfigPrnNameRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigPrnNameRemove.setStatus("mandatory")
_UxsConfigNetGroup_ObjectIdentity = ObjectIdentity
uxsConfigNetGroup = _UxsConfigNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12)
)
_UxsConfigNetPollInterval_Type = Integer32
_UxsConfigNetPollInterval_Object = MibScalar
uxsConfigNetPollInterval = _UxsConfigNetPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 1),
    _UxsConfigNetPollInterval_Type()
)
uxsConfigNetPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetPollInterval.setStatus("mandatory")


class _UxsConfigNetPollMethod_Type(Integer32):
    """Custom type uxsConfigNetPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigNetPollMethod_Type.__name__ = "Integer32"
_UxsConfigNetPollMethod_Object = MibScalar
uxsConfigNetPollMethod = _UxsConfigNetPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 2),
    _UxsConfigNetPollMethod_Type()
)
uxsConfigNetPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetPollMethod.setStatus("mandatory")
_UxsConfigNetIPktWarn_Type = Integer32
_UxsConfigNetIPktWarn_Object = MibScalar
uxsConfigNetIPktWarn = _UxsConfigNetIPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 3),
    _UxsConfigNetIPktWarn_Type()
)
uxsConfigNetIPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetIPktWarn.setStatus("mandatory")
_UxsConfigNetIPktCrit_Type = Integer32
_UxsConfigNetIPktCrit_Object = MibScalar
uxsConfigNetIPktCrit = _UxsConfigNetIPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 4),
    _UxsConfigNetIPktCrit_Type()
)
uxsConfigNetIPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetIPktCrit.setStatus("mandatory")


class _UxsConfigNetIPktMonitor_Type(Integer32):
    """Custom type uxsConfigNetIPktMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigNetIPktMonitor_Type.__name__ = "Integer32"
_UxsConfigNetIPktMonitor_Object = MibScalar
uxsConfigNetIPktMonitor = _UxsConfigNetIPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 5),
    _UxsConfigNetIPktMonitor_Type()
)
uxsConfigNetIPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetIPktMonitor.setStatus("mandatory")
_UxsConfigNetIErrWarn_Type = Integer32
_UxsConfigNetIErrWarn_Object = MibScalar
uxsConfigNetIErrWarn = _UxsConfigNetIErrWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 6),
    _UxsConfigNetIErrWarn_Type()
)
uxsConfigNetIErrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetIErrWarn.setStatus("mandatory")
_UxsConfigNetIErrCrit_Type = Integer32
_UxsConfigNetIErrCrit_Object = MibScalar
uxsConfigNetIErrCrit = _UxsConfigNetIErrCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 7),
    _UxsConfigNetIErrCrit_Type()
)
uxsConfigNetIErrCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetIErrCrit.setStatus("mandatory")


class _UxsConfigNetIErrMonitor_Type(Integer32):
    """Custom type uxsConfigNetIErrMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigNetIErrMonitor_Type.__name__ = "Integer32"
_UxsConfigNetIErrMonitor_Object = MibScalar
uxsConfigNetIErrMonitor = _UxsConfigNetIErrMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 8),
    _UxsConfigNetIErrMonitor_Type()
)
uxsConfigNetIErrMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetIErrMonitor.setStatus("mandatory")
_UxsConfigNetOPktWarn_Type = Integer32
_UxsConfigNetOPktWarn_Object = MibScalar
uxsConfigNetOPktWarn = _UxsConfigNetOPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 9),
    _UxsConfigNetOPktWarn_Type()
)
uxsConfigNetOPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetOPktWarn.setStatus("mandatory")
_UxsConfigNetOPktCrit_Type = Integer32
_UxsConfigNetOPktCrit_Object = MibScalar
uxsConfigNetOPktCrit = _UxsConfigNetOPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 10),
    _UxsConfigNetOPktCrit_Type()
)
uxsConfigNetOPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetOPktCrit.setStatus("mandatory")


class _UxsConfigNetOPktMonitor_Type(Integer32):
    """Custom type uxsConfigNetOPktMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigNetOPktMonitor_Type.__name__ = "Integer32"
_UxsConfigNetOPktMonitor_Object = MibScalar
uxsConfigNetOPktMonitor = _UxsConfigNetOPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 11),
    _UxsConfigNetOPktMonitor_Type()
)
uxsConfigNetOPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetOPktMonitor.setStatus("mandatory")
_UxsConfigNetOErrWarn_Type = Integer32
_UxsConfigNetOErrWarn_Object = MibScalar
uxsConfigNetOErrWarn = _UxsConfigNetOErrWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 12),
    _UxsConfigNetOErrWarn_Type()
)
uxsConfigNetOErrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetOErrWarn.setStatus("mandatory")
_UxsConfigNetOErrCrit_Type = Integer32
_UxsConfigNetOErrCrit_Object = MibScalar
uxsConfigNetOErrCrit = _UxsConfigNetOErrCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 13),
    _UxsConfigNetOErrCrit_Type()
)
uxsConfigNetOErrCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetOErrCrit.setStatus("mandatory")


class _UxsConfigNetOErrMonitor_Type(Integer32):
    """Custom type uxsConfigNetOErrMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigNetOErrMonitor_Type.__name__ = "Integer32"
_UxsConfigNetOErrMonitor_Object = MibScalar
uxsConfigNetOErrMonitor = _UxsConfigNetOErrMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 14),
    _UxsConfigNetOErrMonitor_Type()
)
uxsConfigNetOErrMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetOErrMonitor.setStatus("mandatory")
_UxsConfigNetCollWarn_Type = Integer32
_UxsConfigNetCollWarn_Object = MibScalar
uxsConfigNetCollWarn = _UxsConfigNetCollWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 15),
    _UxsConfigNetCollWarn_Type()
)
uxsConfigNetCollWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetCollWarn.setStatus("mandatory")
_UxsConfigNetCollCrit_Type = Integer32
_UxsConfigNetCollCrit_Object = MibScalar
uxsConfigNetCollCrit = _UxsConfigNetCollCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 16),
    _UxsConfigNetCollCrit_Type()
)
uxsConfigNetCollCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetCollCrit.setStatus("mandatory")


class _UxsConfigNetCollMonitor_Type(Integer32):
    """Custom type uxsConfigNetCollMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigNetCollMonitor_Type.__name__ = "Integer32"
_UxsConfigNetCollMonitor_Object = MibScalar
uxsConfigNetCollMonitor = _UxsConfigNetCollMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 17),
    _UxsConfigNetCollMonitor_Type()
)
uxsConfigNetCollMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetCollMonitor.setStatus("mandatory")


class _UxsConfigNetLossAction_Type(Integer32):
    """Custom type uxsConfigNetLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsConfigNetLossAction_Type.__name__ = "Integer32"
_UxsConfigNetLossAction_Object = MibScalar
uxsConfigNetLossAction = _UxsConfigNetLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 12, 18),
    _UxsConfigNetLossAction_Type()
)
uxsConfigNetLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigNetLossAction.setStatus("mandatory")
_UxsConfigIPCGroup_ObjectIdentity = ObjectIdentity
uxsConfigIPCGroup = _UxsConfigIPCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13)
)
_UxsConfigIPCPollInterval_Type = Integer32
_UxsConfigIPCPollInterval_Object = MibScalar
uxsConfigIPCPollInterval = _UxsConfigIPCPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13, 1),
    _UxsConfigIPCPollInterval_Type()
)
uxsConfigIPCPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigIPCPollInterval.setStatus("mandatory")


class _UxsConfigIPCPollMethod_Type(Integer32):
    """Custom type uxsConfigIPCPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("use-polling-period", 2))
    )


_UxsConfigIPCPollMethod_Type.__name__ = "Integer32"
_UxsConfigIPCPollMethod_Object = MibScalar
uxsConfigIPCPollMethod = _UxsConfigIPCPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13, 2),
    _UxsConfigIPCPollMethod_Type()
)
uxsConfigIPCPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigIPCPollMethod.setStatus("mandatory")
_UxsConfigIPCMQBytesLag_Type = Integer32
_UxsConfigIPCMQBytesLag_Object = MibScalar
uxsConfigIPCMQBytesLag = _UxsConfigIPCMQBytesLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13, 3),
    _UxsConfigIPCMQBytesLag_Type()
)
uxsConfigIPCMQBytesLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigIPCMQBytesLag.setStatus("mandatory")
_UxsConfigIPCMQBytesWarn_Type = DisplayString
_UxsConfigIPCMQBytesWarn_Object = MibScalar
uxsConfigIPCMQBytesWarn = _UxsConfigIPCMQBytesWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13, 4),
    _UxsConfigIPCMQBytesWarn_Type()
)
uxsConfigIPCMQBytesWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigIPCMQBytesWarn.setStatus("mandatory")
_UxsConfigIPCMQBytesCrit_Type = DisplayString
_UxsConfigIPCMQBytesCrit_Object = MibScalar
uxsConfigIPCMQBytesCrit = _UxsConfigIPCMQBytesCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13, 5),
    _UxsConfigIPCMQBytesCrit_Type()
)
uxsConfigIPCMQBytesCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigIPCMQBytesCrit.setStatus("mandatory")


class _UxsConfigIPCMQBytesMonitor_Type(Integer32):
    """Custom type uxsConfigIPCMQBytesMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsConfigIPCMQBytesMonitor_Type.__name__ = "Integer32"
_UxsConfigIPCMQBytesMonitor_Object = MibScalar
uxsConfigIPCMQBytesMonitor = _UxsConfigIPCMQBytesMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 1, 13, 6),
    _UxsConfigIPCMQBytesMonitor_Type()
)
uxsConfigIPCMQBytesMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsConfigIPCMQBytesMonitor.setStatus("mandatory")
_UxsStatusGroup_ObjectIdentity = ObjectIdentity
uxsStatusGroup = _UxsStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2)
)
_UxsStatusGeneralGroup_ObjectIdentity = ObjectIdentity
uxsStatusGeneralGroup = _UxsStatusGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1)
)
_UxsStatusGeneralTotalCount_Type = Integer32
_UxsStatusGeneralTotalCount_Object = MibScalar
uxsStatusGeneralTotalCount = _UxsStatusGeneralTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 1),
    _UxsStatusGeneralTotalCount_Type()
)
uxsStatusGeneralTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralTotalCount.setStatus("mandatory")
_UxsStatusGeneralTotalWarning_Type = Integer32
_UxsStatusGeneralTotalWarning_Object = MibScalar
uxsStatusGeneralTotalWarning = _UxsStatusGeneralTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 2),
    _UxsStatusGeneralTotalWarning_Type()
)
uxsStatusGeneralTotalWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralTotalWarning.setStatus("mandatory")
_UxsStatusGeneralTotalCritical_Type = Integer32
_UxsStatusGeneralTotalCritical_Object = MibScalar
uxsStatusGeneralTotalCritical = _UxsStatusGeneralTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 3),
    _UxsStatusGeneralTotalCritical_Type()
)
uxsStatusGeneralTotalCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralTotalCritical.setStatus("mandatory")
_UxsStatusGeneralCPUCount_Type = Integer32
_UxsStatusGeneralCPUCount_Object = MibScalar
uxsStatusGeneralCPUCount = _UxsStatusGeneralCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 4),
    _UxsStatusGeneralCPUCount_Type()
)
uxsStatusGeneralCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralCPUCount.setStatus("mandatory")
_UxsStatusGeneralCPUWarning_Type = Integer32
_UxsStatusGeneralCPUWarning_Object = MibScalar
uxsStatusGeneralCPUWarning = _UxsStatusGeneralCPUWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 5),
    _UxsStatusGeneralCPUWarning_Type()
)
uxsStatusGeneralCPUWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralCPUWarning.setStatus("mandatory")
_UxsStatusGeneralCPUCritical_Type = Integer32
_UxsStatusGeneralCPUCritical_Object = MibScalar
uxsStatusGeneralCPUCritical = _UxsStatusGeneralCPUCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 6),
    _UxsStatusGeneralCPUCritical_Type()
)
uxsStatusGeneralCPUCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralCPUCritical.setStatus("mandatory")
_UxsStatusGeneralLoadCount_Type = Integer32
_UxsStatusGeneralLoadCount_Object = MibScalar
uxsStatusGeneralLoadCount = _UxsStatusGeneralLoadCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 7),
    _UxsStatusGeneralLoadCount_Type()
)
uxsStatusGeneralLoadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralLoadCount.setStatus("mandatory")
_UxsStatusGeneralLoadWarning_Type = Integer32
_UxsStatusGeneralLoadWarning_Object = MibScalar
uxsStatusGeneralLoadWarning = _UxsStatusGeneralLoadWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 8),
    _UxsStatusGeneralLoadWarning_Type()
)
uxsStatusGeneralLoadWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralLoadWarning.setStatus("mandatory")
_UxsStatusGeneralLoadCritical_Type = Integer32
_UxsStatusGeneralLoadCritical_Object = MibScalar
uxsStatusGeneralLoadCritical = _UxsStatusGeneralLoadCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 9),
    _UxsStatusGeneralLoadCritical_Type()
)
uxsStatusGeneralLoadCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralLoadCritical.setStatus("mandatory")
_UxsStatusGeneralMemCount_Type = Integer32
_UxsStatusGeneralMemCount_Object = MibScalar
uxsStatusGeneralMemCount = _UxsStatusGeneralMemCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 10),
    _UxsStatusGeneralMemCount_Type()
)
uxsStatusGeneralMemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralMemCount.setStatus("mandatory")
_UxsStatusGeneralMemWarning_Type = Integer32
_UxsStatusGeneralMemWarning_Object = MibScalar
uxsStatusGeneralMemWarning = _UxsStatusGeneralMemWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 11),
    _UxsStatusGeneralMemWarning_Type()
)
uxsStatusGeneralMemWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralMemWarning.setStatus("mandatory")
_UxsStatusGeneralMemCritical_Type = Integer32
_UxsStatusGeneralMemCritical_Object = MibScalar
uxsStatusGeneralMemCritical = _UxsStatusGeneralMemCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 12),
    _UxsStatusGeneralMemCritical_Type()
)
uxsStatusGeneralMemCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralMemCritical.setStatus("mandatory")
_UxsStatusGeneralSwapCount_Type = Integer32
_UxsStatusGeneralSwapCount_Object = MibScalar
uxsStatusGeneralSwapCount = _UxsStatusGeneralSwapCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 13),
    _UxsStatusGeneralSwapCount_Type()
)
uxsStatusGeneralSwapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralSwapCount.setStatus("mandatory")
_UxsStatusGeneralSwapWarning_Type = Integer32
_UxsStatusGeneralSwapWarning_Object = MibScalar
uxsStatusGeneralSwapWarning = _UxsStatusGeneralSwapWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 14),
    _UxsStatusGeneralSwapWarning_Type()
)
uxsStatusGeneralSwapWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralSwapWarning.setStatus("mandatory")
_UxsStatusGeneralSwapCritical_Type = Integer32
_UxsStatusGeneralSwapCritical_Object = MibScalar
uxsStatusGeneralSwapCritical = _UxsStatusGeneralSwapCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 15),
    _UxsStatusGeneralSwapCritical_Type()
)
uxsStatusGeneralSwapCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralSwapCritical.setStatus("mandatory")
_UxsStatusGeneralFSysCount_Type = Integer32
_UxsStatusGeneralFSysCount_Object = MibScalar
uxsStatusGeneralFSysCount = _UxsStatusGeneralFSysCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 16),
    _UxsStatusGeneralFSysCount_Type()
)
uxsStatusGeneralFSysCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralFSysCount.setStatus("mandatory")
_UxsStatusGeneralFSysWarning_Type = Integer32
_UxsStatusGeneralFSysWarning_Object = MibScalar
uxsStatusGeneralFSysWarning = _UxsStatusGeneralFSysWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 17),
    _UxsStatusGeneralFSysWarning_Type()
)
uxsStatusGeneralFSysWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralFSysWarning.setStatus("mandatory")
_UxsStatusGeneralFSysCritical_Type = Integer32
_UxsStatusGeneralFSysCritical_Object = MibScalar
uxsStatusGeneralFSysCritical = _UxsStatusGeneralFSysCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 18),
    _UxsStatusGeneralFSysCritical_Type()
)
uxsStatusGeneralFSysCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralFSysCritical.setStatus("mandatory")
_UxsStatusGeneralDiskCount_Type = Integer32
_UxsStatusGeneralDiskCount_Object = MibScalar
uxsStatusGeneralDiskCount = _UxsStatusGeneralDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 19),
    _UxsStatusGeneralDiskCount_Type()
)
uxsStatusGeneralDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralDiskCount.setStatus("mandatory")
_UxsStatusGeneralDiskWarning_Type = Integer32
_UxsStatusGeneralDiskWarning_Object = MibScalar
uxsStatusGeneralDiskWarning = _UxsStatusGeneralDiskWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 20),
    _UxsStatusGeneralDiskWarning_Type()
)
uxsStatusGeneralDiskWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralDiskWarning.setStatus("mandatory")
_UxsStatusGeneralDiskCritical_Type = Integer32
_UxsStatusGeneralDiskCritical_Object = MibScalar
uxsStatusGeneralDiskCritical = _UxsStatusGeneralDiskCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 21),
    _UxsStatusGeneralDiskCritical_Type()
)
uxsStatusGeneralDiskCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralDiskCritical.setStatus("mandatory")
_UxsStatusGeneralFileCount_Type = Integer32
_UxsStatusGeneralFileCount_Object = MibScalar
uxsStatusGeneralFileCount = _UxsStatusGeneralFileCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 22),
    _UxsStatusGeneralFileCount_Type()
)
uxsStatusGeneralFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralFileCount.setStatus("mandatory")
_UxsStatusGeneralFileWarning_Type = Integer32
_UxsStatusGeneralFileWarning_Object = MibScalar
uxsStatusGeneralFileWarning = _UxsStatusGeneralFileWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 23),
    _UxsStatusGeneralFileWarning_Type()
)
uxsStatusGeneralFileWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralFileWarning.setStatus("mandatory")
_UxsStatusGeneralFileCritical_Type = Integer32
_UxsStatusGeneralFileCritical_Object = MibScalar
uxsStatusGeneralFileCritical = _UxsStatusGeneralFileCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 24),
    _UxsStatusGeneralFileCritical_Type()
)
uxsStatusGeneralFileCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralFileCritical.setStatus("mandatory")
_UxsStatusGeneralProcCount_Type = Integer32
_UxsStatusGeneralProcCount_Object = MibScalar
uxsStatusGeneralProcCount = _UxsStatusGeneralProcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 25),
    _UxsStatusGeneralProcCount_Type()
)
uxsStatusGeneralProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralProcCount.setStatus("mandatory")
_UxsStatusGeneralProcWarning_Type = Integer32
_UxsStatusGeneralProcWarning_Object = MibScalar
uxsStatusGeneralProcWarning = _UxsStatusGeneralProcWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 26),
    _UxsStatusGeneralProcWarning_Type()
)
uxsStatusGeneralProcWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralProcWarning.setStatus("mandatory")
_UxsStatusGeneralProcCritical_Type = Integer32
_UxsStatusGeneralProcCritical_Object = MibScalar
uxsStatusGeneralProcCritical = _UxsStatusGeneralProcCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 27),
    _UxsStatusGeneralProcCritical_Type()
)
uxsStatusGeneralProcCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralProcCritical.setStatus("mandatory")
_UxsStatusGeneralPrnCount_Type = Integer32
_UxsStatusGeneralPrnCount_Object = MibScalar
uxsStatusGeneralPrnCount = _UxsStatusGeneralPrnCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 28),
    _UxsStatusGeneralPrnCount_Type()
)
uxsStatusGeneralPrnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralPrnCount.setStatus("mandatory")
_UxsStatusGeneralPrnWarning_Type = Integer32
_UxsStatusGeneralPrnWarning_Object = MibScalar
uxsStatusGeneralPrnWarning = _UxsStatusGeneralPrnWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 29),
    _UxsStatusGeneralPrnWarning_Type()
)
uxsStatusGeneralPrnWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralPrnWarning.setStatus("mandatory")
_UxsStatusGeneralPrnCritical_Type = Integer32
_UxsStatusGeneralPrnCritical_Object = MibScalar
uxsStatusGeneralPrnCritical = _UxsStatusGeneralPrnCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 30),
    _UxsStatusGeneralPrnCritical_Type()
)
uxsStatusGeneralPrnCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralPrnCritical.setStatus("mandatory")
_UxsStatusGeneralNetCount_Type = Integer32
_UxsStatusGeneralNetCount_Object = MibScalar
uxsStatusGeneralNetCount = _UxsStatusGeneralNetCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 31),
    _UxsStatusGeneralNetCount_Type()
)
uxsStatusGeneralNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralNetCount.setStatus("mandatory")
_UxsStatusGeneralNetWarning_Type = Integer32
_UxsStatusGeneralNetWarning_Object = MibScalar
uxsStatusGeneralNetWarning = _UxsStatusGeneralNetWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 32),
    _UxsStatusGeneralNetWarning_Type()
)
uxsStatusGeneralNetWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralNetWarning.setStatus("mandatory")
_UxsStatusGeneralNetCritical_Type = Integer32
_UxsStatusGeneralNetCritical_Object = MibScalar
uxsStatusGeneralNetCritical = _UxsStatusGeneralNetCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 33),
    _UxsStatusGeneralNetCritical_Type()
)
uxsStatusGeneralNetCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralNetCritical.setStatus("mandatory")
_UxsStatusGeneralIPCCount_Type = Integer32
_UxsStatusGeneralIPCCount_Object = MibScalar
uxsStatusGeneralIPCCount = _UxsStatusGeneralIPCCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 34),
    _UxsStatusGeneralIPCCount_Type()
)
uxsStatusGeneralIPCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralIPCCount.setStatus("mandatory")
_UxsStatusGeneralIPCWarning_Type = Integer32
_UxsStatusGeneralIPCWarning_Object = MibScalar
uxsStatusGeneralIPCWarning = _UxsStatusGeneralIPCWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 35),
    _UxsStatusGeneralIPCWarning_Type()
)
uxsStatusGeneralIPCWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralIPCWarning.setStatus("mandatory")
_UxsStatusGeneralIPCCritical_Type = Integer32
_UxsStatusGeneralIPCCritical_Object = MibScalar
uxsStatusGeneralIPCCritical = _UxsStatusGeneralIPCCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 1, 36),
    _UxsStatusGeneralIPCCritical_Type()
)
uxsStatusGeneralIPCCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusGeneralIPCCritical.setStatus("mandatory")
_UxsStatusCPUGroup_ObjectIdentity = ObjectIdentity
uxsStatusCPUGroup = _UxsStatusCPUGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2)
)
_UxsStatusCPUTotalName_Type = DisplayString
_UxsStatusCPUTotalName_Object = MibScalar
uxsStatusCPUTotalName = _UxsStatusCPUTotalName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 1),
    _UxsStatusCPUTotalName_Type()
)
uxsStatusCPUTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalName.setStatus("mandatory")
_UxsStatusCPUTotalUser_Type = Integer32
_UxsStatusCPUTotalUser_Object = MibScalar
uxsStatusCPUTotalUser = _UxsStatusCPUTotalUser_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 2),
    _UxsStatusCPUTotalUser_Type()
)
uxsStatusCPUTotalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalUser.setStatus("mandatory")
_UxsStatusCPUTotalSys_Type = Integer32
_UxsStatusCPUTotalSys_Object = MibScalar
uxsStatusCPUTotalSys = _UxsStatusCPUTotalSys_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 3),
    _UxsStatusCPUTotalSys_Type()
)
uxsStatusCPUTotalSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalSys.setStatus("mandatory")
_UxsStatusCPUTotalIdle_Type = Integer32
_UxsStatusCPUTotalIdle_Object = MibScalar
uxsStatusCPUTotalIdle = _UxsStatusCPUTotalIdle_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 4),
    _UxsStatusCPUTotalIdle_Type()
)
uxsStatusCPUTotalIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalIdle.setStatus("mandatory")
_UxsStatusCPUTotalWIO_Type = Integer32
_UxsStatusCPUTotalWIO_Object = MibScalar
uxsStatusCPUTotalWIO = _UxsStatusCPUTotalWIO_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 5),
    _UxsStatusCPUTotalWIO_Type()
)
uxsStatusCPUTotalWIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalWIO.setStatus("mandatory")
_UxsStatusCPUTotalUsedValue_Type = Integer32
_UxsStatusCPUTotalUsedValue_Object = MibScalar
uxsStatusCPUTotalUsedValue = _UxsStatusCPUTotalUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 6),
    _UxsStatusCPUTotalUsedValue_Type()
)
uxsStatusCPUTotalUsedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalUsedValue.setStatus("mandatory")
_UxsStatusCPUTotalLagValue_Type = Integer32
_UxsStatusCPUTotalLagValue_Object = MibScalar
uxsStatusCPUTotalLagValue = _UxsStatusCPUTotalLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 7),
    _UxsStatusCPUTotalLagValue_Type()
)
uxsStatusCPUTotalLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalLagValue.setStatus("mandatory")
_UxsStatusCPUTotalLag_Type = Integer32
_UxsStatusCPUTotalLag_Object = MibScalar
uxsStatusCPUTotalLag = _UxsStatusCPUTotalLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 8),
    _UxsStatusCPUTotalLag_Type()
)
uxsStatusCPUTotalLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalLag.setStatus("mandatory")
_UxsStatusCPUTotalWarn_Type = DisplayString
_UxsStatusCPUTotalWarn_Object = MibScalar
uxsStatusCPUTotalWarn = _UxsStatusCPUTotalWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 9),
    _UxsStatusCPUTotalWarn_Type()
)
uxsStatusCPUTotalWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalWarn.setStatus("mandatory")
_UxsStatusCPUTotalCrit_Type = DisplayString
_UxsStatusCPUTotalCrit_Object = MibScalar
uxsStatusCPUTotalCrit = _UxsStatusCPUTotalCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 10),
    _UxsStatusCPUTotalCrit_Type()
)
uxsStatusCPUTotalCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalCrit.setStatus("mandatory")


class _UxsStatusCPUTotalMonitor_Type(Integer32):
    """Custom type uxsStatusCPUTotalMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusCPUTotalMonitor_Type.__name__ = "Integer32"
_UxsStatusCPUTotalMonitor_Object = MibScalar
uxsStatusCPUTotalMonitor = _UxsStatusCPUTotalMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 11),
    _UxsStatusCPUTotalMonitor_Type()
)
uxsStatusCPUTotalMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalMonitor.setStatus("mandatory")


class _UxsStatusCPUTotalStatus_Type(Integer32):
    """Custom type uxsStatusCPUTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusCPUTotalStatus_Type.__name__ = "Integer32"
_UxsStatusCPUTotalStatus_Object = MibScalar
uxsStatusCPUTotalStatus = _UxsStatusCPUTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 12),
    _UxsStatusCPUTotalStatus_Type()
)
uxsStatusCPUTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUTotalStatus.setStatus("mandatory")
_UxsStatusCPUCount_Type = Integer32
_UxsStatusCPUCount_Object = MibScalar
uxsStatusCPUCount = _UxsStatusCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 13),
    _UxsStatusCPUCount_Type()
)
uxsStatusCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUCount.setStatus("mandatory")
_UxsStatusCPUTable_Object = MibTable
uxsStatusCPUTable = _UxsStatusCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14)
)
if mibBuilder.loadTexts:
    uxsStatusCPUTable.setStatus("mandatory")
_UxsStatusCPUEntry_Object = MibTableRow
uxsStatusCPUEntry = _UxsStatusCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1)
)
uxsStatusCPUEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusCPUName"),
)
if mibBuilder.loadTexts:
    uxsStatusCPUEntry.setStatus("mandatory")
_UxsStatusCPUName_Type = DisplayString
_UxsStatusCPUName_Object = MibTableColumn
uxsStatusCPUName = _UxsStatusCPUName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 1),
    _UxsStatusCPUName_Type()
)
uxsStatusCPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUName.setStatus("mandatory")
_UxsStatusCPUUser_Type = Integer32
_UxsStatusCPUUser_Object = MibTableColumn
uxsStatusCPUUser = _UxsStatusCPUUser_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 2),
    _UxsStatusCPUUser_Type()
)
uxsStatusCPUUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUUser.setStatus("mandatory")
_UxsStatusCPUSys_Type = Integer32
_UxsStatusCPUSys_Object = MibTableColumn
uxsStatusCPUSys = _UxsStatusCPUSys_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 3),
    _UxsStatusCPUSys_Type()
)
uxsStatusCPUSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUSys.setStatus("mandatory")
_UxsStatusCPUIdle_Type = Integer32
_UxsStatusCPUIdle_Object = MibTableColumn
uxsStatusCPUIdle = _UxsStatusCPUIdle_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 4),
    _UxsStatusCPUIdle_Type()
)
uxsStatusCPUIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUIdle.setStatus("mandatory")
_UxsStatusCPUWIO_Type = Integer32
_UxsStatusCPUWIO_Object = MibTableColumn
uxsStatusCPUWIO = _UxsStatusCPUWIO_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 5),
    _UxsStatusCPUWIO_Type()
)
uxsStatusCPUWIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUWIO.setStatus("mandatory")


class _UxsStatusCPUAggStatus_Type(Integer32):
    """Custom type uxsStatusCPUAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusCPUAggStatus_Type.__name__ = "Integer32"
_UxsStatusCPUAggStatus_Object = MibTableColumn
uxsStatusCPUAggStatus = _UxsStatusCPUAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 6),
    _UxsStatusCPUAggStatus_Type()
)
uxsStatusCPUAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUAggStatus.setStatus("mandatory")
_UxsStatusCPUUsedValue_Type = Integer32
_UxsStatusCPUUsedValue_Object = MibTableColumn
uxsStatusCPUUsedValue = _UxsStatusCPUUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 7),
    _UxsStatusCPUUsedValue_Type()
)
uxsStatusCPUUsedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUUsedValue.setStatus("mandatory")
_UxsStatusCPULagValue_Type = Integer32
_UxsStatusCPULagValue_Object = MibTableColumn
uxsStatusCPULagValue = _UxsStatusCPULagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 8),
    _UxsStatusCPULagValue_Type()
)
uxsStatusCPULagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPULagValue.setStatus("mandatory")
_UxsStatusCPULag_Type = Integer32
_UxsStatusCPULag_Object = MibTableColumn
uxsStatusCPULag = _UxsStatusCPULag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 9),
    _UxsStatusCPULag_Type()
)
uxsStatusCPULag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPULag.setStatus("mandatory")
_UxsStatusCPUWarn_Type = DisplayString
_UxsStatusCPUWarn_Object = MibTableColumn
uxsStatusCPUWarn = _UxsStatusCPUWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 10),
    _UxsStatusCPUWarn_Type()
)
uxsStatusCPUWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUWarn.setStatus("mandatory")
_UxsStatusCPUCrit_Type = DisplayString
_UxsStatusCPUCrit_Object = MibTableColumn
uxsStatusCPUCrit = _UxsStatusCPUCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 11),
    _UxsStatusCPUCrit_Type()
)
uxsStatusCPUCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUCrit.setStatus("mandatory")


class _UxsStatusCPUMonitor_Type(Integer32):
    """Custom type uxsStatusCPUMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusCPUMonitor_Type.__name__ = "Integer32"
_UxsStatusCPUMonitor_Object = MibTableColumn
uxsStatusCPUMonitor = _UxsStatusCPUMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 12),
    _UxsStatusCPUMonitor_Type()
)
uxsStatusCPUMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPUMonitor.setStatus("mandatory")


class _UxsStatusCPUStatus_Type(Integer32):
    """Custom type uxsStatusCPUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusCPUStatus_Type.__name__ = "Integer32"
_UxsStatusCPUStatus_Object = MibTableColumn
uxsStatusCPUStatus = _UxsStatusCPUStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 13),
    _UxsStatusCPUStatus_Type()
)
uxsStatusCPUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPUStatus.setStatus("mandatory")


class _UxsStatusCPULossAction_Type(Integer32):
    """Custom type uxsStatusCPULossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsStatusCPULossAction_Type.__name__ = "Integer32"
_UxsStatusCPULossAction_Object = MibTableColumn
uxsStatusCPULossAction = _UxsStatusCPULossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 14),
    _UxsStatusCPULossAction_Type()
)
uxsStatusCPULossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusCPULossAction.setStatus("mandatory")


class _UxsStatusCPULossStatus_Type(Integer32):
    """Custom type uxsStatusCPULossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusCPULossStatus_Type.__name__ = "Integer32"
_UxsStatusCPULossStatus_Object = MibTableColumn
uxsStatusCPULossStatus = _UxsStatusCPULossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 2, 14, 1, 15),
    _UxsStatusCPULossStatus_Type()
)
uxsStatusCPULossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusCPULossStatus.setStatus("mandatory")
_UxsStatusLoadGroup_ObjectIdentity = ObjectIdentity
uxsStatusLoadGroup = _UxsStatusLoadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3)
)
_UxsStatusLoad1MinValue_Type = DisplayString
_UxsStatusLoad1MinValue_Object = MibScalar
uxsStatusLoad1MinValue = _UxsStatusLoad1MinValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 1),
    _UxsStatusLoad1MinValue_Type()
)
uxsStatusLoad1MinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusLoad1MinValue.setStatus("mandatory")
_UxsStatusLoad1MinWarn_Type = DisplayString
_UxsStatusLoad1MinWarn_Object = MibScalar
uxsStatusLoad1MinWarn = _UxsStatusLoad1MinWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 2),
    _UxsStatusLoad1MinWarn_Type()
)
uxsStatusLoad1MinWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad1MinWarn.setStatus("mandatory")
_UxsStatusLoad1MinCrit_Type = DisplayString
_UxsStatusLoad1MinCrit_Object = MibScalar
uxsStatusLoad1MinCrit = _UxsStatusLoad1MinCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 3),
    _UxsStatusLoad1MinCrit_Type()
)
uxsStatusLoad1MinCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad1MinCrit.setStatus("mandatory")


class _UxsStatusLoad1MinMonitor_Type(Integer32):
    """Custom type uxsStatusLoad1MinMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusLoad1MinMonitor_Type.__name__ = "Integer32"
_UxsStatusLoad1MinMonitor_Object = MibScalar
uxsStatusLoad1MinMonitor = _UxsStatusLoad1MinMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 4),
    _UxsStatusLoad1MinMonitor_Type()
)
uxsStatusLoad1MinMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad1MinMonitor.setStatus("mandatory")


class _UxsStatusLoad1MinStatus_Type(Integer32):
    """Custom type uxsStatusLoad1MinStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusLoad1MinStatus_Type.__name__ = "Integer32"
_UxsStatusLoad1MinStatus_Object = MibScalar
uxsStatusLoad1MinStatus = _UxsStatusLoad1MinStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 5),
    _UxsStatusLoad1MinStatus_Type()
)
uxsStatusLoad1MinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusLoad1MinStatus.setStatus("mandatory")
_UxsStatusLoad5MinValue_Type = DisplayString
_UxsStatusLoad5MinValue_Object = MibScalar
uxsStatusLoad5MinValue = _UxsStatusLoad5MinValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 6),
    _UxsStatusLoad5MinValue_Type()
)
uxsStatusLoad5MinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusLoad5MinValue.setStatus("mandatory")
_UxsStatusLoad5MinWarn_Type = DisplayString
_UxsStatusLoad5MinWarn_Object = MibScalar
uxsStatusLoad5MinWarn = _UxsStatusLoad5MinWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 7),
    _UxsStatusLoad5MinWarn_Type()
)
uxsStatusLoad5MinWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad5MinWarn.setStatus("mandatory")
_UxsStatusLoad5MinCrit_Type = DisplayString
_UxsStatusLoad5MinCrit_Object = MibScalar
uxsStatusLoad5MinCrit = _UxsStatusLoad5MinCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 8),
    _UxsStatusLoad5MinCrit_Type()
)
uxsStatusLoad5MinCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad5MinCrit.setStatus("mandatory")


class _UxsStatusLoad5MinMonitor_Type(Integer32):
    """Custom type uxsStatusLoad5MinMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusLoad5MinMonitor_Type.__name__ = "Integer32"
_UxsStatusLoad5MinMonitor_Object = MibScalar
uxsStatusLoad5MinMonitor = _UxsStatusLoad5MinMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 9),
    _UxsStatusLoad5MinMonitor_Type()
)
uxsStatusLoad5MinMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad5MinMonitor.setStatus("mandatory")


class _UxsStatusLoad5MinStatus_Type(Integer32):
    """Custom type uxsStatusLoad5MinStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusLoad5MinStatus_Type.__name__ = "Integer32"
_UxsStatusLoad5MinStatus_Object = MibScalar
uxsStatusLoad5MinStatus = _UxsStatusLoad5MinStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 10),
    _UxsStatusLoad5MinStatus_Type()
)
uxsStatusLoad5MinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusLoad5MinStatus.setStatus("mandatory")
_UxsStatusLoad15MinValue_Type = DisplayString
_UxsStatusLoad15MinValue_Object = MibScalar
uxsStatusLoad15MinValue = _UxsStatusLoad15MinValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 11),
    _UxsStatusLoad15MinValue_Type()
)
uxsStatusLoad15MinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusLoad15MinValue.setStatus("mandatory")
_UxsStatusLoad15MinWarn_Type = DisplayString
_UxsStatusLoad15MinWarn_Object = MibScalar
uxsStatusLoad15MinWarn = _UxsStatusLoad15MinWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 12),
    _UxsStatusLoad15MinWarn_Type()
)
uxsStatusLoad15MinWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad15MinWarn.setStatus("mandatory")
_UxsStatusLoad15MinCrit_Type = DisplayString
_UxsStatusLoad15MinCrit_Object = MibScalar
uxsStatusLoad15MinCrit = _UxsStatusLoad15MinCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 13),
    _UxsStatusLoad15MinCrit_Type()
)
uxsStatusLoad15MinCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad15MinCrit.setStatus("mandatory")


class _UxsStatusLoad15MinMonitor_Type(Integer32):
    """Custom type uxsStatusLoad15MinMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusLoad15MinMonitor_Type.__name__ = "Integer32"
_UxsStatusLoad15MinMonitor_Object = MibScalar
uxsStatusLoad15MinMonitor = _UxsStatusLoad15MinMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 14),
    _UxsStatusLoad15MinMonitor_Type()
)
uxsStatusLoad15MinMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusLoad15MinMonitor.setStatus("mandatory")


class _UxsStatusLoad15MinStatus_Type(Integer32):
    """Custom type uxsStatusLoad15MinStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusLoad15MinStatus_Type.__name__ = "Integer32"
_UxsStatusLoad15MinStatus_Object = MibScalar
uxsStatusLoad15MinStatus = _UxsStatusLoad15MinStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 3, 15),
    _UxsStatusLoad15MinStatus_Type()
)
uxsStatusLoad15MinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusLoad15MinStatus.setStatus("mandatory")
_UxsStatusMemGroup_ObjectIdentity = ObjectIdentity
uxsStatusMemGroup = _UxsStatusMemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4)
)
_UxsStatusMemTotal_Type = Integer32
_UxsStatusMemTotal_Object = MibScalar
uxsStatusMemTotal = _UxsStatusMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 1),
    _UxsStatusMemTotal_Type()
)
uxsStatusMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusMemTotal.setStatus("mandatory")
_UxsStatusMemValue_Type = Integer32
_UxsStatusMemValue_Object = MibScalar
uxsStatusMemValue = _UxsStatusMemValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 2),
    _UxsStatusMemValue_Type()
)
uxsStatusMemValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusMemValue.setStatus("mandatory")
_UxsStatusMemLagValue_Type = Integer32
_UxsStatusMemLagValue_Object = MibScalar
uxsStatusMemLagValue = _UxsStatusMemLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 3),
    _UxsStatusMemLagValue_Type()
)
uxsStatusMemLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusMemLagValue.setStatus("mandatory")
_UxsStatusMemLag_Type = Integer32
_UxsStatusMemLag_Object = MibScalar
uxsStatusMemLag = _UxsStatusMemLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 4),
    _UxsStatusMemLag_Type()
)
uxsStatusMemLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusMemLag.setStatus("mandatory")
_UxsStatusMemWarnValue_Type = DisplayString
_UxsStatusMemWarnValue_Object = MibScalar
uxsStatusMemWarnValue = _UxsStatusMemWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 5),
    _UxsStatusMemWarnValue_Type()
)
uxsStatusMemWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusMemWarnValue.setStatus("mandatory")
_UxsStatusMemCritValue_Type = DisplayString
_UxsStatusMemCritValue_Object = MibScalar
uxsStatusMemCritValue = _UxsStatusMemCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 6),
    _UxsStatusMemCritValue_Type()
)
uxsStatusMemCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusMemCritValue.setStatus("mandatory")
_UxsStatusMemWarn_Type = DisplayString
_UxsStatusMemWarn_Object = MibScalar
uxsStatusMemWarn = _UxsStatusMemWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 7),
    _UxsStatusMemWarn_Type()
)
uxsStatusMemWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusMemWarn.setStatus("mandatory")
_UxsStatusMemCrit_Type = DisplayString
_UxsStatusMemCrit_Object = MibScalar
uxsStatusMemCrit = _UxsStatusMemCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 8),
    _UxsStatusMemCrit_Type()
)
uxsStatusMemCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusMemCrit.setStatus("mandatory")


class _UxsStatusMemMonitor_Type(Integer32):
    """Custom type uxsStatusMemMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusMemMonitor_Type.__name__ = "Integer32"
_UxsStatusMemMonitor_Object = MibScalar
uxsStatusMemMonitor = _UxsStatusMemMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 9),
    _UxsStatusMemMonitor_Type()
)
uxsStatusMemMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusMemMonitor.setStatus("mandatory")


class _UxsStatusMemStatus_Type(Integer32):
    """Custom type uxsStatusMemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusMemStatus_Type.__name__ = "Integer32"
_UxsStatusMemStatus_Object = MibScalar
uxsStatusMemStatus = _UxsStatusMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 4, 10),
    _UxsStatusMemStatus_Type()
)
uxsStatusMemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusMemStatus.setStatus("mandatory")
_UxsStatusSwapGroup_ObjectIdentity = ObjectIdentity
uxsStatusSwapGroup = _UxsStatusSwapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5)
)
_UxsStatusSwapTotalName_Type = DisplayString
_UxsStatusSwapTotalName_Object = MibScalar
uxsStatusSwapTotalName = _UxsStatusSwapTotalName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 1),
    _UxsStatusSwapTotalName_Type()
)
uxsStatusSwapTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalName.setStatus("mandatory")
_UxsStatusSwapTotalAvailable_Type = Integer32
_UxsStatusSwapTotalAvailable_Object = MibScalar
uxsStatusSwapTotalAvailable = _UxsStatusSwapTotalAvailable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 2),
    _UxsStatusSwapTotalAvailable_Type()
)
uxsStatusSwapTotalAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalAvailable.setStatus("mandatory")
_UxsStatusSwapTotalUsedValue_Type = Integer32
_UxsStatusSwapTotalUsedValue_Object = MibScalar
uxsStatusSwapTotalUsedValue = _UxsStatusSwapTotalUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 3),
    _UxsStatusSwapTotalUsedValue_Type()
)
uxsStatusSwapTotalUsedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalUsedValue.setStatus("mandatory")
_UxsStatusSwapTotalLagValue_Type = Integer32
_UxsStatusSwapTotalLagValue_Object = MibScalar
uxsStatusSwapTotalLagValue = _UxsStatusSwapTotalLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 4),
    _UxsStatusSwapTotalLagValue_Type()
)
uxsStatusSwapTotalLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalLagValue.setStatus("mandatory")
_UxsStatusSwapTotalLag_Type = Integer32
_UxsStatusSwapTotalLag_Object = MibScalar
uxsStatusSwapTotalLag = _UxsStatusSwapTotalLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 5),
    _UxsStatusSwapTotalLag_Type()
)
uxsStatusSwapTotalLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalLag.setStatus("mandatory")
_UxsStatusSwapTotalWarnValue_Type = DisplayString
_UxsStatusSwapTotalWarnValue_Object = MibScalar
uxsStatusSwapTotalWarnValue = _UxsStatusSwapTotalWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 6),
    _UxsStatusSwapTotalWarnValue_Type()
)
uxsStatusSwapTotalWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalWarnValue.setStatus("mandatory")
_UxsStatusSwapTotalCritValue_Type = DisplayString
_UxsStatusSwapTotalCritValue_Object = MibScalar
uxsStatusSwapTotalCritValue = _UxsStatusSwapTotalCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 7),
    _UxsStatusSwapTotalCritValue_Type()
)
uxsStatusSwapTotalCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalCritValue.setStatus("mandatory")
_UxsStatusSwapTotalWarn_Type = DisplayString
_UxsStatusSwapTotalWarn_Object = MibScalar
uxsStatusSwapTotalWarn = _UxsStatusSwapTotalWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 8),
    _UxsStatusSwapTotalWarn_Type()
)
uxsStatusSwapTotalWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalWarn.setStatus("mandatory")
_UxsStatusSwapTotalCrit_Type = DisplayString
_UxsStatusSwapTotalCrit_Object = MibScalar
uxsStatusSwapTotalCrit = _UxsStatusSwapTotalCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 9),
    _UxsStatusSwapTotalCrit_Type()
)
uxsStatusSwapTotalCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalCrit.setStatus("mandatory")


class _UxsStatusSwapTotalMonitor_Type(Integer32):
    """Custom type uxsStatusSwapTotalMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusSwapTotalMonitor_Type.__name__ = "Integer32"
_UxsStatusSwapTotalMonitor_Object = MibScalar
uxsStatusSwapTotalMonitor = _UxsStatusSwapTotalMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 10),
    _UxsStatusSwapTotalMonitor_Type()
)
uxsStatusSwapTotalMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalMonitor.setStatus("mandatory")


class _UxsStatusSwapTotalStatus_Type(Integer32):
    """Custom type uxsStatusSwapTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusSwapTotalStatus_Type.__name__ = "Integer32"
_UxsStatusSwapTotalStatus_Object = MibScalar
uxsStatusSwapTotalStatus = _UxsStatusSwapTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 11),
    _UxsStatusSwapTotalStatus_Type()
)
uxsStatusSwapTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapTotalStatus.setStatus("mandatory")
_UxsStatusSwapCount_Type = Integer32
_UxsStatusSwapCount_Object = MibScalar
uxsStatusSwapCount = _UxsStatusSwapCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 12),
    _UxsStatusSwapCount_Type()
)
uxsStatusSwapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapCount.setStatus("mandatory")
_UxsStatusSwapTable_Object = MibTable
uxsStatusSwapTable = _UxsStatusSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13)
)
if mibBuilder.loadTexts:
    uxsStatusSwapTable.setStatus("mandatory")
_UxsStatusSwapEntry_Object = MibTableRow
uxsStatusSwapEntry = _UxsStatusSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1)
)
uxsStatusSwapEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusSwapName"),
)
if mibBuilder.loadTexts:
    uxsStatusSwapEntry.setStatus("mandatory")
_UxsStatusSwapName_Type = DisplayString
_UxsStatusSwapName_Object = MibTableColumn
uxsStatusSwapName = _UxsStatusSwapName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 1),
    _UxsStatusSwapName_Type()
)
uxsStatusSwapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapName.setStatus("mandatory")


class _UxsStatusSwapAggStatus_Type(Integer32):
    """Custom type uxsStatusSwapAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusSwapAggStatus_Type.__name__ = "Integer32"
_UxsStatusSwapAggStatus_Object = MibTableColumn
uxsStatusSwapAggStatus = _UxsStatusSwapAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 2),
    _UxsStatusSwapAggStatus_Type()
)
uxsStatusSwapAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapAggStatus.setStatus("mandatory")
_UxsStatusSwapAvailable_Type = Integer32
_UxsStatusSwapAvailable_Object = MibTableColumn
uxsStatusSwapAvailable = _UxsStatusSwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 3),
    _UxsStatusSwapAvailable_Type()
)
uxsStatusSwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapAvailable.setStatus("mandatory")
_UxsStatusSwapUsedValue_Type = Integer32
_UxsStatusSwapUsedValue_Object = MibTableColumn
uxsStatusSwapUsedValue = _UxsStatusSwapUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 4),
    _UxsStatusSwapUsedValue_Type()
)
uxsStatusSwapUsedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapUsedValue.setStatus("mandatory")
_UxsStatusSwapLagValue_Type = Integer32
_UxsStatusSwapLagValue_Object = MibTableColumn
uxsStatusSwapLagValue = _UxsStatusSwapLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 5),
    _UxsStatusSwapLagValue_Type()
)
uxsStatusSwapLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapLagValue.setStatus("mandatory")
_UxsStatusSwapLag_Type = Integer32
_UxsStatusSwapLag_Object = MibTableColumn
uxsStatusSwapLag = _UxsStatusSwapLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 6),
    _UxsStatusSwapLag_Type()
)
uxsStatusSwapLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapLag.setStatus("mandatory")
_UxsStatusSwapWarnValue_Type = DisplayString
_UxsStatusSwapWarnValue_Object = MibTableColumn
uxsStatusSwapWarnValue = _UxsStatusSwapWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 7),
    _UxsStatusSwapWarnValue_Type()
)
uxsStatusSwapWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapWarnValue.setStatus("mandatory")
_UxsStatusSwapCritValue_Type = DisplayString
_UxsStatusSwapCritValue_Object = MibTableColumn
uxsStatusSwapCritValue = _UxsStatusSwapCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 8),
    _UxsStatusSwapCritValue_Type()
)
uxsStatusSwapCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapCritValue.setStatus("mandatory")
_UxsStatusSwapWarn_Type = DisplayString
_UxsStatusSwapWarn_Object = MibTableColumn
uxsStatusSwapWarn = _UxsStatusSwapWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 9),
    _UxsStatusSwapWarn_Type()
)
uxsStatusSwapWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapWarn.setStatus("mandatory")
_UxsStatusSwapCrit_Type = DisplayString
_UxsStatusSwapCrit_Object = MibTableColumn
uxsStatusSwapCrit = _UxsStatusSwapCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 10),
    _UxsStatusSwapCrit_Type()
)
uxsStatusSwapCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapCrit.setStatus("mandatory")


class _UxsStatusSwapMonitor_Type(Integer32):
    """Custom type uxsStatusSwapMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusSwapMonitor_Type.__name__ = "Integer32"
_UxsStatusSwapMonitor_Object = MibTableColumn
uxsStatusSwapMonitor = _UxsStatusSwapMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 11),
    _UxsStatusSwapMonitor_Type()
)
uxsStatusSwapMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapMonitor.setStatus("mandatory")


class _UxsStatusSwapStatus_Type(Integer32):
    """Custom type uxsStatusSwapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusSwapStatus_Type.__name__ = "Integer32"
_UxsStatusSwapStatus_Object = MibTableColumn
uxsStatusSwapStatus = _UxsStatusSwapStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 12),
    _UxsStatusSwapStatus_Type()
)
uxsStatusSwapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapStatus.setStatus("mandatory")


class _UxsStatusSwapLossAction_Type(Integer32):
    """Custom type uxsStatusSwapLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsStatusSwapLossAction_Type.__name__ = "Integer32"
_UxsStatusSwapLossAction_Object = MibTableColumn
uxsStatusSwapLossAction = _UxsStatusSwapLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 13),
    _UxsStatusSwapLossAction_Type()
)
uxsStatusSwapLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusSwapLossAction.setStatus("mandatory")


class _UxsStatusSwapLossStatus_Type(Integer32):
    """Custom type uxsStatusSwapLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusSwapLossStatus_Type.__name__ = "Integer32"
_UxsStatusSwapLossStatus_Object = MibTableColumn
uxsStatusSwapLossStatus = _UxsStatusSwapLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 5, 13, 1, 14),
    _UxsStatusSwapLossStatus_Type()
)
uxsStatusSwapLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusSwapLossStatus.setStatus("mandatory")
_UxsStatusFSysGroup_ObjectIdentity = ObjectIdentity
uxsStatusFSysGroup = _UxsStatusFSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6)
)
_UxsStatusFSysCount_Type = Integer32
_UxsStatusFSysCount_Object = MibScalar
uxsStatusFSysCount = _UxsStatusFSysCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 1),
    _UxsStatusFSysCount_Type()
)
uxsStatusFSysCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysCount.setStatus("mandatory")
_UxsStatusFSysTable_Object = MibTable
uxsStatusFSysTable = _UxsStatusFSysTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    uxsStatusFSysTable.setStatus("mandatory")
_UxsStatusFSysEntry_Object = MibTableRow
uxsStatusFSysEntry = _UxsStatusFSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1)
)
uxsStatusFSysEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusFSysName"),
)
if mibBuilder.loadTexts:
    uxsStatusFSysEntry.setStatus("mandatory")
_UxsStatusFSysName_Type = DisplayString
_UxsStatusFSysName_Object = MibTableColumn
uxsStatusFSysName = _UxsStatusFSysName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 1),
    _UxsStatusFSysName_Type()
)
uxsStatusFSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysName.setStatus("mandatory")
_UxsStatusFSysRelatedTo_Type = DisplayString
_UxsStatusFSysRelatedTo_Object = MibTableColumn
uxsStatusFSysRelatedTo = _UxsStatusFSysRelatedTo_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 2),
    _UxsStatusFSysRelatedTo_Type()
)
uxsStatusFSysRelatedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysRelatedTo.setStatus("mandatory")
_UxsStatusFSysType_Type = DisplayString
_UxsStatusFSysType_Object = MibTableColumn
uxsStatusFSysType = _UxsStatusFSysType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 3),
    _UxsStatusFSysType_Type()
)
uxsStatusFSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysType.setStatus("mandatory")


class _UxsStatusFSysStatus_Type(Integer32):
    """Custom type uxsStatusFSysStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFSysStatus_Type.__name__ = "Integer32"
_UxsStatusFSysStatus_Object = MibTableColumn
uxsStatusFSysStatus = _UxsStatusFSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 4),
    _UxsStatusFSysStatus_Type()
)
uxsStatusFSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysStatus.setStatus("mandatory")
_UxsStatusFSysSpaceTotal_Type = Integer32
_UxsStatusFSysSpaceTotal_Object = MibTableColumn
uxsStatusFSysSpaceTotal = _UxsStatusFSysSpaceTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 5),
    _UxsStatusFSysSpaceTotal_Type()
)
uxsStatusFSysSpaceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceTotal.setStatus("mandatory")
_UxsStatusFSysSpaceValue_Type = Integer32
_UxsStatusFSysSpaceValue_Object = MibTableColumn
uxsStatusFSysSpaceValue = _UxsStatusFSysSpaceValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 6),
    _UxsStatusFSysSpaceValue_Type()
)
uxsStatusFSysSpaceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceValue.setStatus("mandatory")
_UxsStatusFSysSpaceWarnValue_Type = DisplayString
_UxsStatusFSysSpaceWarnValue_Object = MibTableColumn
uxsStatusFSysSpaceWarnValue = _UxsStatusFSysSpaceWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 7),
    _UxsStatusFSysSpaceWarnValue_Type()
)
uxsStatusFSysSpaceWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceWarnValue.setStatus("mandatory")
_UxsStatusFSysSpaceCritValue_Type = DisplayString
_UxsStatusFSysSpaceCritValue_Object = MibTableColumn
uxsStatusFSysSpaceCritValue = _UxsStatusFSysSpaceCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 8),
    _UxsStatusFSysSpaceCritValue_Type()
)
uxsStatusFSysSpaceCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceCritValue.setStatus("mandatory")
_UxsStatusFSysSpaceWarn_Type = DisplayString
_UxsStatusFSysSpaceWarn_Object = MibTableColumn
uxsStatusFSysSpaceWarn = _UxsStatusFSysSpaceWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 9),
    _UxsStatusFSysSpaceWarn_Type()
)
uxsStatusFSysSpaceWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceWarn.setStatus("mandatory")
_UxsStatusFSysSpaceCrit_Type = DisplayString
_UxsStatusFSysSpaceCrit_Object = MibTableColumn
uxsStatusFSysSpaceCrit = _UxsStatusFSysSpaceCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 10),
    _UxsStatusFSysSpaceCrit_Type()
)
uxsStatusFSysSpaceCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceCrit.setStatus("mandatory")


class _UxsStatusFSysSpaceMonitor_Type(Integer32):
    """Custom type uxsStatusFSysSpaceMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusFSysSpaceMonitor_Type.__name__ = "Integer32"
_UxsStatusFSysSpaceMonitor_Object = MibTableColumn
uxsStatusFSysSpaceMonitor = _UxsStatusFSysSpaceMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 11),
    _UxsStatusFSysSpaceMonitor_Type()
)
uxsStatusFSysSpaceMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceMonitor.setStatus("mandatory")


class _UxsStatusFSysSpaceStatus_Type(Integer32):
    """Custom type uxsStatusFSysSpaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFSysSpaceStatus_Type.__name__ = "Integer32"
_UxsStatusFSysSpaceStatus_Object = MibTableColumn
uxsStatusFSysSpaceStatus = _UxsStatusFSysSpaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 12),
    _UxsStatusFSysSpaceStatus_Type()
)
uxsStatusFSysSpaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceStatus.setStatus("mandatory")
_UxsStatusFSysSpaceDValue_Type = Integer32
_UxsStatusFSysSpaceDValue_Object = MibTableColumn
uxsStatusFSysSpaceDValue = _UxsStatusFSysSpaceDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 13),
    _UxsStatusFSysSpaceDValue_Type()
)
uxsStatusFSysSpaceDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDValue.setStatus("mandatory")
_UxsStatusFSysSpaceDWarnValue_Type = DisplayString
_UxsStatusFSysSpaceDWarnValue_Object = MibTableColumn
uxsStatusFSysSpaceDWarnValue = _UxsStatusFSysSpaceDWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 14),
    _UxsStatusFSysSpaceDWarnValue_Type()
)
uxsStatusFSysSpaceDWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDWarnValue.setStatus("mandatory")
_UxsStatusFSysSpaceDCritValue_Type = DisplayString
_UxsStatusFSysSpaceDCritValue_Object = MibTableColumn
uxsStatusFSysSpaceDCritValue = _UxsStatusFSysSpaceDCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 15),
    _UxsStatusFSysSpaceDCritValue_Type()
)
uxsStatusFSysSpaceDCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDCritValue.setStatus("mandatory")
_UxsStatusFSysSpaceDWarn_Type = DisplayString
_UxsStatusFSysSpaceDWarn_Object = MibTableColumn
uxsStatusFSysSpaceDWarn = _UxsStatusFSysSpaceDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 16),
    _UxsStatusFSysSpaceDWarn_Type()
)
uxsStatusFSysSpaceDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDWarn.setStatus("mandatory")
_UxsStatusFSysSpaceDCrit_Type = DisplayString
_UxsStatusFSysSpaceDCrit_Object = MibTableColumn
uxsStatusFSysSpaceDCrit = _UxsStatusFSysSpaceDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 17),
    _UxsStatusFSysSpaceDCrit_Type()
)
uxsStatusFSysSpaceDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDCrit.setStatus("mandatory")


class _UxsStatusFSysSpaceDMonitor_Type(Integer32):
    """Custom type uxsStatusFSysSpaceDMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusFSysSpaceDMonitor_Type.__name__ = "Integer32"
_UxsStatusFSysSpaceDMonitor_Object = MibTableColumn
uxsStatusFSysSpaceDMonitor = _UxsStatusFSysSpaceDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 18),
    _UxsStatusFSysSpaceDMonitor_Type()
)
uxsStatusFSysSpaceDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDMonitor.setStatus("mandatory")


class _UxsStatusFSysSpaceDStatus_Type(Integer32):
    """Custom type uxsStatusFSysSpaceDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFSysSpaceDStatus_Type.__name__ = "Integer32"
_UxsStatusFSysSpaceDStatus_Object = MibTableColumn
uxsStatusFSysSpaceDStatus = _UxsStatusFSysSpaceDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 19),
    _UxsStatusFSysSpaceDStatus_Type()
)
uxsStatusFSysSpaceDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysSpaceDStatus.setStatus("mandatory")
_UxsStatusFSysInodesTotal_Type = Integer32
_UxsStatusFSysInodesTotal_Object = MibTableColumn
uxsStatusFSysInodesTotal = _UxsStatusFSysInodesTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 20),
    _UxsStatusFSysInodesTotal_Type()
)
uxsStatusFSysInodesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesTotal.setStatus("mandatory")
_UxsStatusFSysInodesValue_Type = Integer32
_UxsStatusFSysInodesValue_Object = MibTableColumn
uxsStatusFSysInodesValue = _UxsStatusFSysInodesValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 21),
    _UxsStatusFSysInodesValue_Type()
)
uxsStatusFSysInodesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesValue.setStatus("mandatory")
_UxsStatusFSysInodesWarnValue_Type = DisplayString
_UxsStatusFSysInodesWarnValue_Object = MibTableColumn
uxsStatusFSysInodesWarnValue = _UxsStatusFSysInodesWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 22),
    _UxsStatusFSysInodesWarnValue_Type()
)
uxsStatusFSysInodesWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesWarnValue.setStatus("mandatory")
_UxsStatusFSysInodesCritValue_Type = DisplayString
_UxsStatusFSysInodesCritValue_Object = MibTableColumn
uxsStatusFSysInodesCritValue = _UxsStatusFSysInodesCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 23),
    _UxsStatusFSysInodesCritValue_Type()
)
uxsStatusFSysInodesCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesCritValue.setStatus("mandatory")
_UxsStatusFSysInodesWarn_Type = DisplayString
_UxsStatusFSysInodesWarn_Object = MibTableColumn
uxsStatusFSysInodesWarn = _UxsStatusFSysInodesWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 24),
    _UxsStatusFSysInodesWarn_Type()
)
uxsStatusFSysInodesWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesWarn.setStatus("mandatory")
_UxsStatusFSysInodesCrit_Type = DisplayString
_UxsStatusFSysInodesCrit_Object = MibTableColumn
uxsStatusFSysInodesCrit = _UxsStatusFSysInodesCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 25),
    _UxsStatusFSysInodesCrit_Type()
)
uxsStatusFSysInodesCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesCrit.setStatus("mandatory")


class _UxsStatusFSysInodesMonitor_Type(Integer32):
    """Custom type uxsStatusFSysInodesMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusFSysInodesMonitor_Type.__name__ = "Integer32"
_UxsStatusFSysInodesMonitor_Object = MibTableColumn
uxsStatusFSysInodesMonitor = _UxsStatusFSysInodesMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 26),
    _UxsStatusFSysInodesMonitor_Type()
)
uxsStatusFSysInodesMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesMonitor.setStatus("mandatory")


class _UxsStatusFSysInodesStatus_Type(Integer32):
    """Custom type uxsStatusFSysInodesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFSysInodesStatus_Type.__name__ = "Integer32"
_UxsStatusFSysInodesStatus_Object = MibTableColumn
uxsStatusFSysInodesStatus = _UxsStatusFSysInodesStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 27),
    _UxsStatusFSysInodesStatus_Type()
)
uxsStatusFSysInodesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesStatus.setStatus("mandatory")
_UxsStatusFSysInodesDValue_Type = Integer32
_UxsStatusFSysInodesDValue_Object = MibTableColumn
uxsStatusFSysInodesDValue = _UxsStatusFSysInodesDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 28),
    _UxsStatusFSysInodesDValue_Type()
)
uxsStatusFSysInodesDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDValue.setStatus("mandatory")
_UxsStatusFSysInodesDWarnValue_Type = DisplayString
_UxsStatusFSysInodesDWarnValue_Object = MibTableColumn
uxsStatusFSysInodesDWarnValue = _UxsStatusFSysInodesDWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 29),
    _UxsStatusFSysInodesDWarnValue_Type()
)
uxsStatusFSysInodesDWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDWarnValue.setStatus("mandatory")
_UxsStatusFSysInodesDCritValue_Type = DisplayString
_UxsStatusFSysInodesDCritValue_Object = MibTableColumn
uxsStatusFSysInodesDCritValue = _UxsStatusFSysInodesDCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 30),
    _UxsStatusFSysInodesDCritValue_Type()
)
uxsStatusFSysInodesDCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDCritValue.setStatus("mandatory")
_UxsStatusFSysInodesDWarn_Type = DisplayString
_UxsStatusFSysInodesDWarn_Object = MibTableColumn
uxsStatusFSysInodesDWarn = _UxsStatusFSysInodesDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 31),
    _UxsStatusFSysInodesDWarn_Type()
)
uxsStatusFSysInodesDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDWarn.setStatus("mandatory")
_UxsStatusFSysInodesDCrit_Type = DisplayString
_UxsStatusFSysInodesDCrit_Object = MibTableColumn
uxsStatusFSysInodesDCrit = _UxsStatusFSysInodesDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 32),
    _UxsStatusFSysInodesDCrit_Type()
)
uxsStatusFSysInodesDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDCrit.setStatus("mandatory")


class _UxsStatusFSysInodesDMonitor_Type(Integer32):
    """Custom type uxsStatusFSysInodesDMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusFSysInodesDMonitor_Type.__name__ = "Integer32"
_UxsStatusFSysInodesDMonitor_Object = MibTableColumn
uxsStatusFSysInodesDMonitor = _UxsStatusFSysInodesDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 33),
    _UxsStatusFSysInodesDMonitor_Type()
)
uxsStatusFSysInodesDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDMonitor.setStatus("mandatory")


class _UxsStatusFSysInodesDStatus_Type(Integer32):
    """Custom type uxsStatusFSysInodesDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFSysInodesDStatus_Type.__name__ = "Integer32"
_UxsStatusFSysInodesDStatus_Object = MibTableColumn
uxsStatusFSysInodesDStatus = _UxsStatusFSysInodesDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 34),
    _UxsStatusFSysInodesDStatus_Type()
)
uxsStatusFSysInodesDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysInodesDStatus.setStatus("mandatory")


class _UxsStatusFSysMountedMonitor_Type(Integer32):
    """Custom type uxsStatusFSysMountedMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusFSysMountedMonitor_Type.__name__ = "Integer32"
_UxsStatusFSysMountedMonitor_Object = MibTableColumn
uxsStatusFSysMountedMonitor = _UxsStatusFSysMountedMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 35),
    _UxsStatusFSysMountedMonitor_Type()
)
uxsStatusFSysMountedMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysMountedMonitor.setStatus("mandatory")


class _UxsStatusFSysMountedStatus_Type(Integer32):
    """Custom type uxsStatusFSysMountedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusFSysMountedStatus_Type.__name__ = "Integer32"
_UxsStatusFSysMountedStatus_Object = MibTableColumn
uxsStatusFSysMountedStatus = _UxsStatusFSysMountedStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 36),
    _UxsStatusFSysMountedStatus_Type()
)
uxsStatusFSysMountedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysMountedStatus.setStatus("mandatory")


class _UxsStatusFSysLossAction_Type(Integer32):
    """Custom type uxsStatusFSysLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsStatusFSysLossAction_Type.__name__ = "Integer32"
_UxsStatusFSysLossAction_Object = MibTableColumn
uxsStatusFSysLossAction = _UxsStatusFSysLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 37),
    _UxsStatusFSysLossAction_Type()
)
uxsStatusFSysLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysLossAction.setStatus("mandatory")


class _UxsStatusFSysLossStatus_Type(Integer32):
    """Custom type uxsStatusFSysLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusFSysLossStatus_Type.__name__ = "Integer32"
_UxsStatusFSysLossStatus_Object = MibTableColumn
uxsStatusFSysLossStatus = _UxsStatusFSysLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 38),
    _UxsStatusFSysLossStatus_Type()
)
uxsStatusFSysLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFSysLossStatus.setStatus("mandatory")


class _UxsStatusFSysRemove_Type(Integer32):
    """Custom type uxsStatusFSysRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_UxsStatusFSysRemove_Type.__name__ = "Integer32"
_UxsStatusFSysRemove_Object = MibTableColumn
uxsStatusFSysRemove = _UxsStatusFSysRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 6, 2, 1, 39),
    _UxsStatusFSysRemove_Type()
)
uxsStatusFSysRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFSysRemove.setStatus("mandatory")
_UxsStatusDiskGroup_ObjectIdentity = ObjectIdentity
uxsStatusDiskGroup = _UxsStatusDiskGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7)
)
_UxsStatusDiskCount_Type = Integer32
_UxsStatusDiskCount_Object = MibScalar
uxsStatusDiskCount = _UxsStatusDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 1),
    _UxsStatusDiskCount_Type()
)
uxsStatusDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusDiskCount.setStatus("mandatory")
_UxsStatusDiskTable_Object = MibTable
uxsStatusDiskTable = _UxsStatusDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2)
)
if mibBuilder.loadTexts:
    uxsStatusDiskTable.setStatus("mandatory")
_UxsStatusDiskEntry_Object = MibTableRow
uxsStatusDiskEntry = _UxsStatusDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1)
)
uxsStatusDiskEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusDiskName"),
)
if mibBuilder.loadTexts:
    uxsStatusDiskEntry.setStatus("mandatory")
_UxsStatusDiskName_Type = DisplayString
_UxsStatusDiskName_Object = MibTableColumn
uxsStatusDiskName = _UxsStatusDiskName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 1),
    _UxsStatusDiskName_Type()
)
uxsStatusDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusDiskName.setStatus("mandatory")


class _UxsStatusDiskAggStatus_Type(Integer32):
    """Custom type uxsStatusDiskAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusDiskAggStatus_Type.__name__ = "Integer32"
_UxsStatusDiskAggStatus_Object = MibTableColumn
uxsStatusDiskAggStatus = _UxsStatusDiskAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 2),
    _UxsStatusDiskAggStatus_Type()
)
uxsStatusDiskAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusDiskAggStatus.setStatus("mandatory")
_UxsStatusDiskTPutValue_Type = Integer32
_UxsStatusDiskTPutValue_Object = MibTableColumn
uxsStatusDiskTPutValue = _UxsStatusDiskTPutValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 3),
    _UxsStatusDiskTPutValue_Type()
)
uxsStatusDiskTPutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusDiskTPutValue.setStatus("mandatory")
_UxsStatusDiskTPutWarn_Type = Integer32
_UxsStatusDiskTPutWarn_Object = MibTableColumn
uxsStatusDiskTPutWarn = _UxsStatusDiskTPutWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 4),
    _UxsStatusDiskTPutWarn_Type()
)
uxsStatusDiskTPutWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusDiskTPutWarn.setStatus("mandatory")
_UxsStatusDiskTPutCrit_Type = Integer32
_UxsStatusDiskTPutCrit_Object = MibTableColumn
uxsStatusDiskTPutCrit = _UxsStatusDiskTPutCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 5),
    _UxsStatusDiskTPutCrit_Type()
)
uxsStatusDiskTPutCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusDiskTPutCrit.setStatus("mandatory")


class _UxsStatusDiskTPutMonitor_Type(Integer32):
    """Custom type uxsStatusDiskTPutMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusDiskTPutMonitor_Type.__name__ = "Integer32"
_UxsStatusDiskTPutMonitor_Object = MibTableColumn
uxsStatusDiskTPutMonitor = _UxsStatusDiskTPutMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 6),
    _UxsStatusDiskTPutMonitor_Type()
)
uxsStatusDiskTPutMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusDiskTPutMonitor.setStatus("mandatory")


class _UxsStatusDiskTPutStatus_Type(Integer32):
    """Custom type uxsStatusDiskTPutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusDiskTPutStatus_Type.__name__ = "Integer32"
_UxsStatusDiskTPutStatus_Object = MibTableColumn
uxsStatusDiskTPutStatus = _UxsStatusDiskTPutStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 7),
    _UxsStatusDiskTPutStatus_Type()
)
uxsStatusDiskTPutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusDiskTPutStatus.setStatus("mandatory")


class _UxsStatusDiskLossAction_Type(Integer32):
    """Custom type uxsStatusDiskLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsStatusDiskLossAction_Type.__name__ = "Integer32"
_UxsStatusDiskLossAction_Object = MibTableColumn
uxsStatusDiskLossAction = _UxsStatusDiskLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 8),
    _UxsStatusDiskLossAction_Type()
)
uxsStatusDiskLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusDiskLossAction.setStatus("mandatory")


class _UxsStatusDiskLossStatus_Type(Integer32):
    """Custom type uxsStatusDiskLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusDiskLossStatus_Type.__name__ = "Integer32"
_UxsStatusDiskLossStatus_Object = MibTableColumn
uxsStatusDiskLossStatus = _UxsStatusDiskLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 9),
    _UxsStatusDiskLossStatus_Type()
)
uxsStatusDiskLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusDiskLossStatus.setStatus("mandatory")


class _UxsStatusDiskRemove_Type(Integer32):
    """Custom type uxsStatusDiskRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_UxsStatusDiskRemove_Type.__name__ = "Integer32"
_UxsStatusDiskRemove_Object = MibTableColumn
uxsStatusDiskRemove = _UxsStatusDiskRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 7, 2, 1, 10),
    _UxsStatusDiskRemove_Type()
)
uxsStatusDiskRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusDiskRemove.setStatus("mandatory")
_UxsStatusFileGroup_ObjectIdentity = ObjectIdentity
uxsStatusFileGroup = _UxsStatusFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8)
)
_UxsStatusFileCount_Type = Integer32
_UxsStatusFileCount_Object = MibScalar
uxsStatusFileCount = _UxsStatusFileCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 1),
    _UxsStatusFileCount_Type()
)
uxsStatusFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileCount.setStatus("mandatory")
_UxsStatusFileTable_Object = MibTable
uxsStatusFileTable = _UxsStatusFileTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2)
)
if mibBuilder.loadTexts:
    uxsStatusFileTable.setStatus("mandatory")
_UxsStatusFileEntry_Object = MibTableRow
uxsStatusFileEntry = _UxsStatusFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1)
)
uxsStatusFileEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusFileName"),
)
if mibBuilder.loadTexts:
    uxsStatusFileEntry.setStatus("mandatory")
_UxsStatusFileName_Type = DisplayString
_UxsStatusFileName_Object = MibTableColumn
uxsStatusFileName = _UxsStatusFileName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 1),
    _UxsStatusFileName_Type()
)
uxsStatusFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileName.setStatus("mandatory")
_UxsStatusFileDesc_Type = DisplayString
_UxsStatusFileDesc_Object = MibTableColumn
uxsStatusFileDesc = _UxsStatusFileDesc_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 2),
    _UxsStatusFileDesc_Type()
)
uxsStatusFileDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileDesc.setStatus("mandatory")


class _UxsStatusFileStatus_Type(Integer32):
    """Custom type uxsStatusFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFileStatus_Type.__name__ = "Integer32"
_UxsStatusFileStatus_Object = MibTableColumn
uxsStatusFileStatus = _UxsStatusFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 3),
    _UxsStatusFileStatus_Type()
)
uxsStatusFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileStatus.setStatus("mandatory")


class _UxsStatusFileExist_Type(Integer32):
    """Custom type uxsStatusFileExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_UxsStatusFileExist_Type.__name__ = "Integer32"
_UxsStatusFileExist_Object = MibTableColumn
uxsStatusFileExist = _UxsStatusFileExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 4),
    _UxsStatusFileExist_Type()
)
uxsStatusFileExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileExist.setStatus("mandatory")


class _UxsStatusFileExistMonitor_Type(Integer32):
    """Custom type uxsStatusFileExistMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusFileExistMonitor_Type.__name__ = "Integer32"
_UxsStatusFileExistMonitor_Object = MibTableColumn
uxsStatusFileExistMonitor = _UxsStatusFileExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 5),
    _UxsStatusFileExistMonitor_Type()
)
uxsStatusFileExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileExistMonitor.setStatus("mandatory")


class _UxsStatusFileExistStatus_Type(Integer32):
    """Custom type uxsStatusFileExistStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusFileExistStatus_Type.__name__ = "Integer32"
_UxsStatusFileExistStatus_Object = MibTableColumn
uxsStatusFileExistStatus = _UxsStatusFileExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 6),
    _UxsStatusFileExistStatus_Type()
)
uxsStatusFileExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileExistStatus.setStatus("mandatory")
_UxsStatusFileModTime_Type = DisplayString
_UxsStatusFileModTime_Object = MibTableColumn
uxsStatusFileModTime = _UxsStatusFileModTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 7),
    _UxsStatusFileModTime_Type()
)
uxsStatusFileModTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileModTime.setStatus("mandatory")
_UxsStatusFileModTimeValue_Type = DisplayString
_UxsStatusFileModTimeValue_Object = MibTableColumn
uxsStatusFileModTimeValue = _UxsStatusFileModTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 8),
    _UxsStatusFileModTimeValue_Type()
)
uxsStatusFileModTimeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileModTimeValue.setStatus("mandatory")


class _UxsStatusFileModTimeMonitor_Type(Integer32):
    """Custom type uxsStatusFileModTimeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusFileModTimeMonitor_Type.__name__ = "Integer32"
_UxsStatusFileModTimeMonitor_Object = MibTableColumn
uxsStatusFileModTimeMonitor = _UxsStatusFileModTimeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 9),
    _UxsStatusFileModTimeMonitor_Type()
)
uxsStatusFileModTimeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileModTimeMonitor.setStatus("mandatory")


class _UxsStatusFileModTimeStatus_Type(Integer32):
    """Custom type uxsStatusFileModTimeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("reset", 4),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusFileModTimeStatus_Type.__name__ = "Integer32"
_UxsStatusFileModTimeStatus_Object = MibTableColumn
uxsStatusFileModTimeStatus = _UxsStatusFileModTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 10),
    _UxsStatusFileModTimeStatus_Type()
)
uxsStatusFileModTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileModTimeStatus.setStatus("mandatory")
_UxsStatusFileSizeValue_Type = Integer32
_UxsStatusFileSizeValue_Object = MibTableColumn
uxsStatusFileSizeValue = _UxsStatusFileSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 11),
    _UxsStatusFileSizeValue_Type()
)
uxsStatusFileSizeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileSizeValue.setStatus("mandatory")
_UxsStatusFileSizeWarn_Type = Integer32
_UxsStatusFileSizeWarn_Object = MibTableColumn
uxsStatusFileSizeWarn = _UxsStatusFileSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 12),
    _UxsStatusFileSizeWarn_Type()
)
uxsStatusFileSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileSizeWarn.setStatus("mandatory")
_UxsStatusFileSizeCrit_Type = Integer32
_UxsStatusFileSizeCrit_Object = MibTableColumn
uxsStatusFileSizeCrit = _UxsStatusFileSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 13),
    _UxsStatusFileSizeCrit_Type()
)
uxsStatusFileSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileSizeCrit.setStatus("mandatory")


class _UxsStatusFileSizeMonitor_Type(Integer32):
    """Custom type uxsStatusFileSizeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusFileSizeMonitor_Type.__name__ = "Integer32"
_UxsStatusFileSizeMonitor_Object = MibTableColumn
uxsStatusFileSizeMonitor = _UxsStatusFileSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 14),
    _UxsStatusFileSizeMonitor_Type()
)
uxsStatusFileSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileSizeMonitor.setStatus("mandatory")


class _UxsStatusFileSizeStatus_Type(Integer32):
    """Custom type uxsStatusFileSizeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFileSizeStatus_Type.__name__ = "Integer32"
_UxsStatusFileSizeStatus_Object = MibTableColumn
uxsStatusFileSizeStatus = _UxsStatusFileSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 15),
    _UxsStatusFileSizeStatus_Type()
)
uxsStatusFileSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileSizeStatus.setStatus("mandatory")
_UxsStatusFileSizeDValue_Type = Integer32
_UxsStatusFileSizeDValue_Object = MibTableColumn
uxsStatusFileSizeDValue = _UxsStatusFileSizeDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 16),
    _UxsStatusFileSizeDValue_Type()
)
uxsStatusFileSizeDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileSizeDValue.setStatus("mandatory")
_UxsStatusFileSizeDWarn_Type = Integer32
_UxsStatusFileSizeDWarn_Object = MibTableColumn
uxsStatusFileSizeDWarn = _UxsStatusFileSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 17),
    _UxsStatusFileSizeDWarn_Type()
)
uxsStatusFileSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileSizeDWarn.setStatus("mandatory")
_UxsStatusFileSizeDCrit_Type = Integer32
_UxsStatusFileSizeDCrit_Object = MibTableColumn
uxsStatusFileSizeDCrit = _UxsStatusFileSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 18),
    _UxsStatusFileSizeDCrit_Type()
)
uxsStatusFileSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileSizeDCrit.setStatus("mandatory")


class _UxsStatusFileSizeDMonitor_Type(Integer32):
    """Custom type uxsStatusFileSizeDMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusFileSizeDMonitor_Type.__name__ = "Integer32"
_UxsStatusFileSizeDMonitor_Object = MibTableColumn
uxsStatusFileSizeDMonitor = _UxsStatusFileSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 19),
    _UxsStatusFileSizeDMonitor_Type()
)
uxsStatusFileSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileSizeDMonitor.setStatus("mandatory")


class _UxsStatusFileSizeDStatus_Type(Integer32):
    """Custom type uxsStatusFileSizeDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusFileSizeDStatus_Type.__name__ = "Integer32"
_UxsStatusFileSizeDStatus_Object = MibTableColumn
uxsStatusFileSizeDStatus = _UxsStatusFileSizeDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 20),
    _UxsStatusFileSizeDStatus_Type()
)
uxsStatusFileSizeDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusFileSizeDStatus.setStatus("mandatory")


class _UxsStatusFileRemove_Type(Integer32):
    """Custom type uxsStatusFileRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_UxsStatusFileRemove_Type.__name__ = "Integer32"
_UxsStatusFileRemove_Object = MibTableColumn
uxsStatusFileRemove = _UxsStatusFileRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 8, 2, 1, 21),
    _UxsStatusFileRemove_Type()
)
uxsStatusFileRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusFileRemove.setStatus("mandatory")
_UxsStatusProcGroup_ObjectIdentity = ObjectIdentity
uxsStatusProcGroup = _UxsStatusProcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9)
)
_UxsStatusProcCount_Type = Integer32
_UxsStatusProcCount_Object = MibScalar
uxsStatusProcCount = _UxsStatusProcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 1),
    _UxsStatusProcCount_Type()
)
uxsStatusProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcCount.setStatus("mandatory")
_UxsStatusProcTable_Object = MibTable
uxsStatusProcTable = _UxsStatusProcTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2)
)
if mibBuilder.loadTexts:
    uxsStatusProcTable.setStatus("mandatory")
_UxsStatusProcEntry_Object = MibTableRow
uxsStatusProcEntry = _UxsStatusProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1)
)
uxsStatusProcEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusProcName"),
    (0, "CAIUXOS", "uxsStatusProcPath"),
    (0, "CAIUXOS", "uxsStatusProcArgs"),
    (0, "CAIUXOS", "uxsStatusProcUsers"),
)
if mibBuilder.loadTexts:
    uxsStatusProcEntry.setStatus("mandatory")
_UxsStatusProcName_Type = DisplayString
_UxsStatusProcName_Object = MibTableColumn
uxsStatusProcName = _UxsStatusProcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 1),
    _UxsStatusProcName_Type()
)
uxsStatusProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcName.setStatus("mandatory")
_UxsStatusProcPath_Type = DisplayString
_UxsStatusProcPath_Object = MibTableColumn
uxsStatusProcPath = _UxsStatusProcPath_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 2),
    _UxsStatusProcPath_Type()
)
uxsStatusProcPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcPath.setStatus("mandatory")
_UxsStatusProcArgs_Type = DisplayString
_UxsStatusProcArgs_Object = MibTableColumn
uxsStatusProcArgs = _UxsStatusProcArgs_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 3),
    _UxsStatusProcArgs_Type()
)
uxsStatusProcArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcArgs.setStatus("mandatory")
_UxsStatusProcUsers_Type = DisplayString
_UxsStatusProcUsers_Object = MibTableColumn
uxsStatusProcUsers = _UxsStatusProcUsers_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 4),
    _UxsStatusProcUsers_Type()
)
uxsStatusProcUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcUsers.setStatus("mandatory")


class _UxsStatusProcStatus_Type(Integer32):
    """Custom type uxsStatusProcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusProcStatus_Type.__name__ = "Integer32"
_UxsStatusProcStatus_Object = MibTableColumn
uxsStatusProcStatus = _UxsStatusProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 5),
    _UxsStatusProcStatus_Type()
)
uxsStatusProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcStatus.setStatus("mandatory")
_UxsStatusProcPIDs_Type = DisplayString
_UxsStatusProcPIDs_Object = MibTableColumn
uxsStatusProcPIDs = _UxsStatusProcPIDs_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 6),
    _UxsStatusProcPIDs_Type()
)
uxsStatusProcPIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcPIDs.setStatus("mandatory")
_UxsStatusProcInstValue_Type = Integer32
_UxsStatusProcInstValue_Object = MibTableColumn
uxsStatusProcInstValue = _UxsStatusProcInstValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 7),
    _UxsStatusProcInstValue_Type()
)
uxsStatusProcInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcInstValue.setStatus("mandatory")
_UxsStatusProcInstMin_Type = Integer32
_UxsStatusProcInstMin_Object = MibTableColumn
uxsStatusProcInstMin = _UxsStatusProcInstMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 8),
    _UxsStatusProcInstMin_Type()
)
uxsStatusProcInstMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcInstMin.setStatus("mandatory")
_UxsStatusProcInstMax_Type = Integer32
_UxsStatusProcInstMax_Object = MibTableColumn
uxsStatusProcInstMax = _UxsStatusProcInstMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 9),
    _UxsStatusProcInstMax_Type()
)
uxsStatusProcInstMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcInstMax.setStatus("mandatory")


class _UxsStatusProcInstMonitor_Type(Integer32):
    """Custom type uxsStatusProcInstMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusProcInstMonitor_Type.__name__ = "Integer32"
_UxsStatusProcInstMonitor_Object = MibTableColumn
uxsStatusProcInstMonitor = _UxsStatusProcInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 10),
    _UxsStatusProcInstMonitor_Type()
)
uxsStatusProcInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcInstMonitor.setStatus("mandatory")


class _UxsStatusProcInstStatus_Type(Integer32):
    """Custom type uxsStatusProcInstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusProcInstStatus_Type.__name__ = "Integer32"
_UxsStatusProcInstStatus_Object = MibTableColumn
uxsStatusProcInstStatus = _UxsStatusProcInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 11),
    _UxsStatusProcInstStatus_Type()
)
uxsStatusProcInstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcInstStatus.setStatus("mandatory")
_UxsStatusProcChldValue_Type = Integer32
_UxsStatusProcChldValue_Object = MibTableColumn
uxsStatusProcChldValue = _UxsStatusProcChldValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 12),
    _UxsStatusProcChldValue_Type()
)
uxsStatusProcChldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcChldValue.setStatus("mandatory")
_UxsStatusProcChldMin_Type = Integer32
_UxsStatusProcChldMin_Object = MibTableColumn
uxsStatusProcChldMin = _UxsStatusProcChldMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 13),
    _UxsStatusProcChldMin_Type()
)
uxsStatusProcChldMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcChldMin.setStatus("mandatory")
_UxsStatusProcChldMax_Type = Integer32
_UxsStatusProcChldMax_Object = MibTableColumn
uxsStatusProcChldMax = _UxsStatusProcChldMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 14),
    _UxsStatusProcChldMax_Type()
)
uxsStatusProcChldMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcChldMax.setStatus("mandatory")


class _UxsStatusProcChldMonitor_Type(Integer32):
    """Custom type uxsStatusProcChldMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusProcChldMonitor_Type.__name__ = "Integer32"
_UxsStatusProcChldMonitor_Object = MibTableColumn
uxsStatusProcChldMonitor = _UxsStatusProcChldMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 15),
    _UxsStatusProcChldMonitor_Type()
)
uxsStatusProcChldMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcChldMonitor.setStatus("mandatory")


class _UxsStatusProcChldStatus_Type(Integer32):
    """Custom type uxsStatusProcChldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusProcChldStatus_Type.__name__ = "Integer32"
_UxsStatusProcChldStatus_Object = MibTableColumn
uxsStatusProcChldStatus = _UxsStatusProcChldStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 16),
    _UxsStatusProcChldStatus_Type()
)
uxsStatusProcChldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcChldStatus.setStatus("mandatory")
_UxsStatusProcSizeValue_Type = Integer32
_UxsStatusProcSizeValue_Object = MibTableColumn
uxsStatusProcSizeValue = _UxsStatusProcSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 17),
    _UxsStatusProcSizeValue_Type()
)
uxsStatusProcSizeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcSizeValue.setStatus("mandatory")
_UxsStatusProcSizeMin_Type = Integer32
_UxsStatusProcSizeMin_Object = MibTableColumn
uxsStatusProcSizeMin = _UxsStatusProcSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 18),
    _UxsStatusProcSizeMin_Type()
)
uxsStatusProcSizeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcSizeMin.setStatus("mandatory")
_UxsStatusProcSizeMax_Type = Integer32
_UxsStatusProcSizeMax_Object = MibTableColumn
uxsStatusProcSizeMax = _UxsStatusProcSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 19),
    _UxsStatusProcSizeMax_Type()
)
uxsStatusProcSizeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcSizeMax.setStatus("mandatory")


class _UxsStatusProcSizeMonitor_Type(Integer32):
    """Custom type uxsStatusProcSizeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusProcSizeMonitor_Type.__name__ = "Integer32"
_UxsStatusProcSizeMonitor_Object = MibTableColumn
uxsStatusProcSizeMonitor = _UxsStatusProcSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 20),
    _UxsStatusProcSizeMonitor_Type()
)
uxsStatusProcSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcSizeMonitor.setStatus("mandatory")


class _UxsStatusProcSizeStatus_Type(Integer32):
    """Custom type uxsStatusProcSizeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusProcSizeStatus_Type.__name__ = "Integer32"
_UxsStatusProcSizeStatus_Object = MibTableColumn
uxsStatusProcSizeStatus = _UxsStatusProcSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 21),
    _UxsStatusProcSizeStatus_Type()
)
uxsStatusProcSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcSizeStatus.setStatus("mandatory")
_UxsStatusProcCPUValue_Type = Integer32
_UxsStatusProcCPUValue_Object = MibTableColumn
uxsStatusProcCPUValue = _UxsStatusProcCPUValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 22),
    _UxsStatusProcCPUValue_Type()
)
uxsStatusProcCPUValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcCPUValue.setStatus("mandatory")
_UxsStatusProcCPUWarn_Type = Integer32
_UxsStatusProcCPUWarn_Object = MibTableColumn
uxsStatusProcCPUWarn = _UxsStatusProcCPUWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 23),
    _UxsStatusProcCPUWarn_Type()
)
uxsStatusProcCPUWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcCPUWarn.setStatus("mandatory")
_UxsStatusProcCPUCrit_Type = Integer32
_UxsStatusProcCPUCrit_Object = MibTableColumn
uxsStatusProcCPUCrit = _UxsStatusProcCPUCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 24),
    _UxsStatusProcCPUCrit_Type()
)
uxsStatusProcCPUCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcCPUCrit.setStatus("mandatory")


class _UxsStatusProcCPUMonitor_Type(Integer32):
    """Custom type uxsStatusProcCPUMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusProcCPUMonitor_Type.__name__ = "Integer32"
_UxsStatusProcCPUMonitor_Object = MibTableColumn
uxsStatusProcCPUMonitor = _UxsStatusProcCPUMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 25),
    _UxsStatusProcCPUMonitor_Type()
)
uxsStatusProcCPUMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcCPUMonitor.setStatus("mandatory")


class _UxsStatusProcCPUStatus_Type(Integer32):
    """Custom type uxsStatusProcCPUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusProcCPUStatus_Type.__name__ = "Integer32"
_UxsStatusProcCPUStatus_Object = MibTableColumn
uxsStatusProcCPUStatus = _UxsStatusProcCPUStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 26),
    _UxsStatusProcCPUStatus_Type()
)
uxsStatusProcCPUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusProcCPUStatus.setStatus("mandatory")


class _UxsStatusProcRemove_Type(Integer32):
    """Custom type uxsStatusProcRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_UxsStatusProcRemove_Type.__name__ = "Integer32"
_UxsStatusProcRemove_Object = MibTableColumn
uxsStatusProcRemove = _UxsStatusProcRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 9, 2, 1, 27),
    _UxsStatusProcRemove_Type()
)
uxsStatusProcRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusProcRemove.setStatus("mandatory")
_UxsStatusPrnGroup_ObjectIdentity = ObjectIdentity
uxsStatusPrnGroup = _UxsStatusPrnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10)
)
_UxsStatusPrnCount_Type = Integer32
_UxsStatusPrnCount_Object = MibScalar
uxsStatusPrnCount = _UxsStatusPrnCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 1),
    _UxsStatusPrnCount_Type()
)
uxsStatusPrnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusPrnCount.setStatus("mandatory")
_UxsStatusPrnTable_Object = MibTable
uxsStatusPrnTable = _UxsStatusPrnTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    uxsStatusPrnTable.setStatus("mandatory")
_UxsStatusPrnEntry_Object = MibTableRow
uxsStatusPrnEntry = _UxsStatusPrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1)
)
uxsStatusPrnEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusPrnName"),
)
if mibBuilder.loadTexts:
    uxsStatusPrnEntry.setStatus("mandatory")
_UxsStatusPrnName_Type = DisplayString
_UxsStatusPrnName_Object = MibTableColumn
uxsStatusPrnName = _UxsStatusPrnName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 1),
    _UxsStatusPrnName_Type()
)
uxsStatusPrnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusPrnName.setStatus("mandatory")


class _UxsStatusPrnAggStatus_Type(Integer32):
    """Custom type uxsStatusPrnAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("down", 5),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusPrnAggStatus_Type.__name__ = "Integer32"
_UxsStatusPrnAggStatus_Object = MibTableColumn
uxsStatusPrnAggStatus = _UxsStatusPrnAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 2),
    _UxsStatusPrnAggStatus_Type()
)
uxsStatusPrnAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusPrnAggStatus.setStatus("mandatory")
_UxsStatusPrnDesc_Type = DisplayString
_UxsStatusPrnDesc_Object = MibTableColumn
uxsStatusPrnDesc = _UxsStatusPrnDesc_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 3),
    _UxsStatusPrnDesc_Type()
)
uxsStatusPrnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusPrnDesc.setStatus("mandatory")
_UxsStatusPrnItemsValue_Type = Integer32
_UxsStatusPrnItemsValue_Object = MibTableColumn
uxsStatusPrnItemsValue = _UxsStatusPrnItemsValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 4),
    _UxsStatusPrnItemsValue_Type()
)
uxsStatusPrnItemsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusPrnItemsValue.setStatus("mandatory")
_UxsStatusPrnItemsWarn_Type = Integer32
_UxsStatusPrnItemsWarn_Object = MibTableColumn
uxsStatusPrnItemsWarn = _UxsStatusPrnItemsWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 5),
    _UxsStatusPrnItemsWarn_Type()
)
uxsStatusPrnItemsWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusPrnItemsWarn.setStatus("mandatory")
_UxsStatusPrnItemsCrit_Type = Integer32
_UxsStatusPrnItemsCrit_Object = MibTableColumn
uxsStatusPrnItemsCrit = _UxsStatusPrnItemsCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 6),
    _UxsStatusPrnItemsCrit_Type()
)
uxsStatusPrnItemsCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusPrnItemsCrit.setStatus("mandatory")


class _UxsStatusPrnItemsMonitor_Type(Integer32):
    """Custom type uxsStatusPrnItemsMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusPrnItemsMonitor_Type.__name__ = "Integer32"
_UxsStatusPrnItemsMonitor_Object = MibTableColumn
uxsStatusPrnItemsMonitor = _UxsStatusPrnItemsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 7),
    _UxsStatusPrnItemsMonitor_Type()
)
uxsStatusPrnItemsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusPrnItemsMonitor.setStatus("mandatory")


class _UxsStatusPrnItemsStatus_Type(Integer32):
    """Custom type uxsStatusPrnItemsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusPrnItemsStatus_Type.__name__ = "Integer32"
_UxsStatusPrnItemsStatus_Object = MibTableColumn
uxsStatusPrnItemsStatus = _UxsStatusPrnItemsStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 8),
    _UxsStatusPrnItemsStatus_Type()
)
uxsStatusPrnItemsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusPrnItemsStatus.setStatus("mandatory")


class _UxsStatusPrnLossAction_Type(Integer32):
    """Custom type uxsStatusPrnLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsStatusPrnLossAction_Type.__name__ = "Integer32"
_UxsStatusPrnLossAction_Object = MibTableColumn
uxsStatusPrnLossAction = _UxsStatusPrnLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 9),
    _UxsStatusPrnLossAction_Type()
)
uxsStatusPrnLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusPrnLossAction.setStatus("mandatory")


class _UxsStatusPrnLossStatus_Type(Integer32):
    """Custom type uxsStatusPrnLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusPrnLossStatus_Type.__name__ = "Integer32"
_UxsStatusPrnLossStatus_Object = MibTableColumn
uxsStatusPrnLossStatus = _UxsStatusPrnLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 10),
    _UxsStatusPrnLossStatus_Type()
)
uxsStatusPrnLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusPrnLossStatus.setStatus("mandatory")


class _UxsStatusPrnRemove_Type(Integer32):
    """Custom type uxsStatusPrnRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_UxsStatusPrnRemove_Type.__name__ = "Integer32"
_UxsStatusPrnRemove_Object = MibTableColumn
uxsStatusPrnRemove = _UxsStatusPrnRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 10, 2, 1, 11),
    _UxsStatusPrnRemove_Type()
)
uxsStatusPrnRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusPrnRemove.setStatus("mandatory")
_UxsStatusNetGroup_ObjectIdentity = ObjectIdentity
uxsStatusNetGroup = _UxsStatusNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11)
)


class _UxsStatusNetTotalStatus_Type(Integer32):
    """Custom type uxsStatusNetTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetTotalStatus_Type.__name__ = "Integer32"
_UxsStatusNetTotalStatus_Object = MibScalar
uxsStatusNetTotalStatus = _UxsStatusNetTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 1),
    _UxsStatusNetTotalStatus_Type()
)
uxsStatusNetTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalStatus.setStatus("mandatory")
_UxsStatusNetTotalIPktValue_Type = Integer32
_UxsStatusNetTotalIPktValue_Object = MibScalar
uxsStatusNetTotalIPktValue = _UxsStatusNetTotalIPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 2),
    _UxsStatusNetTotalIPktValue_Type()
)
uxsStatusNetTotalIPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIPktValue.setStatus("mandatory")
_UxsStatusNetTotalIPktWarn_Type = Integer32
_UxsStatusNetTotalIPktWarn_Object = MibScalar
uxsStatusNetTotalIPktWarn = _UxsStatusNetTotalIPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 3),
    _UxsStatusNetTotalIPktWarn_Type()
)
uxsStatusNetTotalIPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIPktWarn.setStatus("mandatory")
_UxsStatusNetTotalIPktCrit_Type = Integer32
_UxsStatusNetTotalIPktCrit_Object = MibScalar
uxsStatusNetTotalIPktCrit = _UxsStatusNetTotalIPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 4),
    _UxsStatusNetTotalIPktCrit_Type()
)
uxsStatusNetTotalIPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIPktCrit.setStatus("mandatory")


class _UxsStatusNetTotalIPktMonitor_Type(Integer32):
    """Custom type uxsStatusNetTotalIPktMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetTotalIPktMonitor_Type.__name__ = "Integer32"
_UxsStatusNetTotalIPktMonitor_Object = MibScalar
uxsStatusNetTotalIPktMonitor = _UxsStatusNetTotalIPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 5),
    _UxsStatusNetTotalIPktMonitor_Type()
)
uxsStatusNetTotalIPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIPktMonitor.setStatus("mandatory")


class _UxsStatusNetTotalIPktStatus_Type(Integer32):
    """Custom type uxsStatusNetTotalIPktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetTotalIPktStatus_Type.__name__ = "Integer32"
_UxsStatusNetTotalIPktStatus_Object = MibScalar
uxsStatusNetTotalIPktStatus = _UxsStatusNetTotalIPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 6),
    _UxsStatusNetTotalIPktStatus_Type()
)
uxsStatusNetTotalIPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIPktStatus.setStatus("mandatory")
_UxsStatusNetTotalIErrValue_Type = Integer32
_UxsStatusNetTotalIErrValue_Object = MibScalar
uxsStatusNetTotalIErrValue = _UxsStatusNetTotalIErrValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 7),
    _UxsStatusNetTotalIErrValue_Type()
)
uxsStatusNetTotalIErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIErrValue.setStatus("mandatory")
_UxsStatusNetTotalIErrWarn_Type = Integer32
_UxsStatusNetTotalIErrWarn_Object = MibScalar
uxsStatusNetTotalIErrWarn = _UxsStatusNetTotalIErrWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 8),
    _UxsStatusNetTotalIErrWarn_Type()
)
uxsStatusNetTotalIErrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIErrWarn.setStatus("mandatory")
_UxsStatusNetTotalIErrCrit_Type = Integer32
_UxsStatusNetTotalIErrCrit_Object = MibScalar
uxsStatusNetTotalIErrCrit = _UxsStatusNetTotalIErrCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 9),
    _UxsStatusNetTotalIErrCrit_Type()
)
uxsStatusNetTotalIErrCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIErrCrit.setStatus("mandatory")


class _UxsStatusNetTotalIErrMonitor_Type(Integer32):
    """Custom type uxsStatusNetTotalIErrMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetTotalIErrMonitor_Type.__name__ = "Integer32"
_UxsStatusNetTotalIErrMonitor_Object = MibScalar
uxsStatusNetTotalIErrMonitor = _UxsStatusNetTotalIErrMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 10),
    _UxsStatusNetTotalIErrMonitor_Type()
)
uxsStatusNetTotalIErrMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIErrMonitor.setStatus("mandatory")


class _UxsStatusNetTotalIErrStatus_Type(Integer32):
    """Custom type uxsStatusNetTotalIErrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetTotalIErrStatus_Type.__name__ = "Integer32"
_UxsStatusNetTotalIErrStatus_Object = MibScalar
uxsStatusNetTotalIErrStatus = _UxsStatusNetTotalIErrStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 11),
    _UxsStatusNetTotalIErrStatus_Type()
)
uxsStatusNetTotalIErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalIErrStatus.setStatus("mandatory")
_UxsStatusNetTotalOPktValue_Type = Integer32
_UxsStatusNetTotalOPktValue_Object = MibScalar
uxsStatusNetTotalOPktValue = _UxsStatusNetTotalOPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 12),
    _UxsStatusNetTotalOPktValue_Type()
)
uxsStatusNetTotalOPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOPktValue.setStatus("mandatory")
_UxsStatusNetTotalOPktWarn_Type = Integer32
_UxsStatusNetTotalOPktWarn_Object = MibScalar
uxsStatusNetTotalOPktWarn = _UxsStatusNetTotalOPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 13),
    _UxsStatusNetTotalOPktWarn_Type()
)
uxsStatusNetTotalOPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOPktWarn.setStatus("mandatory")
_UxsStatusNetTotalOPktCrit_Type = Integer32
_UxsStatusNetTotalOPktCrit_Object = MibScalar
uxsStatusNetTotalOPktCrit = _UxsStatusNetTotalOPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 14),
    _UxsStatusNetTotalOPktCrit_Type()
)
uxsStatusNetTotalOPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOPktCrit.setStatus("mandatory")


class _UxsStatusNetTotalOPktMonitor_Type(Integer32):
    """Custom type uxsStatusNetTotalOPktMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetTotalOPktMonitor_Type.__name__ = "Integer32"
_UxsStatusNetTotalOPktMonitor_Object = MibScalar
uxsStatusNetTotalOPktMonitor = _UxsStatusNetTotalOPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 15),
    _UxsStatusNetTotalOPktMonitor_Type()
)
uxsStatusNetTotalOPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOPktMonitor.setStatus("mandatory")


class _UxsStatusNetTotalOPktStatus_Type(Integer32):
    """Custom type uxsStatusNetTotalOPktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetTotalOPktStatus_Type.__name__ = "Integer32"
_UxsStatusNetTotalOPktStatus_Object = MibScalar
uxsStatusNetTotalOPktStatus = _UxsStatusNetTotalOPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 16),
    _UxsStatusNetTotalOPktStatus_Type()
)
uxsStatusNetTotalOPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOPktStatus.setStatus("mandatory")
_UxsStatusNetTotalOErrValue_Type = Integer32
_UxsStatusNetTotalOErrValue_Object = MibScalar
uxsStatusNetTotalOErrValue = _UxsStatusNetTotalOErrValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 17),
    _UxsStatusNetTotalOErrValue_Type()
)
uxsStatusNetTotalOErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOErrValue.setStatus("mandatory")
_UxsStatusNetTotalOErrWarn_Type = Integer32
_UxsStatusNetTotalOErrWarn_Object = MibScalar
uxsStatusNetTotalOErrWarn = _UxsStatusNetTotalOErrWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 18),
    _UxsStatusNetTotalOErrWarn_Type()
)
uxsStatusNetTotalOErrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOErrWarn.setStatus("mandatory")
_UxsStatusNetTotalOErrCrit_Type = Integer32
_UxsStatusNetTotalOErrCrit_Object = MibScalar
uxsStatusNetTotalOErrCrit = _UxsStatusNetTotalOErrCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 19),
    _UxsStatusNetTotalOErrCrit_Type()
)
uxsStatusNetTotalOErrCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOErrCrit.setStatus("mandatory")


class _UxsStatusNetTotalOErrMonitor_Type(Integer32):
    """Custom type uxsStatusNetTotalOErrMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetTotalOErrMonitor_Type.__name__ = "Integer32"
_UxsStatusNetTotalOErrMonitor_Object = MibScalar
uxsStatusNetTotalOErrMonitor = _UxsStatusNetTotalOErrMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 20),
    _UxsStatusNetTotalOErrMonitor_Type()
)
uxsStatusNetTotalOErrMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOErrMonitor.setStatus("mandatory")


class _UxsStatusNetTotalOErrStatus_Type(Integer32):
    """Custom type uxsStatusNetTotalOErrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetTotalOErrStatus_Type.__name__ = "Integer32"
_UxsStatusNetTotalOErrStatus_Object = MibScalar
uxsStatusNetTotalOErrStatus = _UxsStatusNetTotalOErrStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 21),
    _UxsStatusNetTotalOErrStatus_Type()
)
uxsStatusNetTotalOErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalOErrStatus.setStatus("mandatory")
_UxsStatusNetTotalCollValue_Type = Integer32
_UxsStatusNetTotalCollValue_Object = MibScalar
uxsStatusNetTotalCollValue = _UxsStatusNetTotalCollValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 22),
    _UxsStatusNetTotalCollValue_Type()
)
uxsStatusNetTotalCollValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalCollValue.setStatus("mandatory")
_UxsStatusNetTotalCollWarn_Type = Integer32
_UxsStatusNetTotalCollWarn_Object = MibScalar
uxsStatusNetTotalCollWarn = _UxsStatusNetTotalCollWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 23),
    _UxsStatusNetTotalCollWarn_Type()
)
uxsStatusNetTotalCollWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalCollWarn.setStatus("mandatory")
_UxsStatusNetTotalCollCrit_Type = Integer32
_UxsStatusNetTotalCollCrit_Object = MibScalar
uxsStatusNetTotalCollCrit = _UxsStatusNetTotalCollCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 24),
    _UxsStatusNetTotalCollCrit_Type()
)
uxsStatusNetTotalCollCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalCollCrit.setStatus("mandatory")


class _UxsStatusNetTotalCollMonitor_Type(Integer32):
    """Custom type uxsStatusNetTotalCollMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetTotalCollMonitor_Type.__name__ = "Integer32"
_UxsStatusNetTotalCollMonitor_Object = MibScalar
uxsStatusNetTotalCollMonitor = _UxsStatusNetTotalCollMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 25),
    _UxsStatusNetTotalCollMonitor_Type()
)
uxsStatusNetTotalCollMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetTotalCollMonitor.setStatus("mandatory")


class _UxsStatusNetTotalCollStatus_Type(Integer32):
    """Custom type uxsStatusNetTotalCollStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetTotalCollStatus_Type.__name__ = "Integer32"
_UxsStatusNetTotalCollStatus_Object = MibScalar
uxsStatusNetTotalCollStatus = _UxsStatusNetTotalCollStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 26),
    _UxsStatusNetTotalCollStatus_Type()
)
uxsStatusNetTotalCollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetTotalCollStatus.setStatus("mandatory")
_UxsStatusNetCount_Type = Integer32
_UxsStatusNetCount_Object = MibScalar
uxsStatusNetCount = _UxsStatusNetCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 27),
    _UxsStatusNetCount_Type()
)
uxsStatusNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetCount.setStatus("mandatory")
_UxsStatusNetTable_Object = MibTable
uxsStatusNetTable = _UxsStatusNetTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28)
)
if mibBuilder.loadTexts:
    uxsStatusNetTable.setStatus("mandatory")
_UxsStatusNetEntry_Object = MibTableRow
uxsStatusNetEntry = _UxsStatusNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1)
)
uxsStatusNetEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusNetName"),
)
if mibBuilder.loadTexts:
    uxsStatusNetEntry.setStatus("mandatory")
_UxsStatusNetName_Type = DisplayString
_UxsStatusNetName_Object = MibTableColumn
uxsStatusNetName = _UxsStatusNetName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 1),
    _UxsStatusNetName_Type()
)
uxsStatusNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetName.setStatus("mandatory")
_UxsStatusNetIP_Type = DisplayString
_UxsStatusNetIP_Object = MibTableColumn
uxsStatusNetIP = _UxsStatusNetIP_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 2),
    _UxsStatusNetIP_Type()
)
uxsStatusNetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetIP.setStatus("mandatory")


class _UxsStatusNetStatus_Type(Integer32):
    """Custom type uxsStatusNetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetStatus_Type.__name__ = "Integer32"
_UxsStatusNetStatus_Object = MibTableColumn
uxsStatusNetStatus = _UxsStatusNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 3),
    _UxsStatusNetStatus_Type()
)
uxsStatusNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetStatus.setStatus("mandatory")
_UxsStatusNetIPktValue_Type = Integer32
_UxsStatusNetIPktValue_Object = MibTableColumn
uxsStatusNetIPktValue = _UxsStatusNetIPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 4),
    _UxsStatusNetIPktValue_Type()
)
uxsStatusNetIPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetIPktValue.setStatus("mandatory")
_UxsStatusNetIPktWarn_Type = Integer32
_UxsStatusNetIPktWarn_Object = MibTableColumn
uxsStatusNetIPktWarn = _UxsStatusNetIPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 5),
    _UxsStatusNetIPktWarn_Type()
)
uxsStatusNetIPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetIPktWarn.setStatus("mandatory")
_UxsStatusNetIPktCrit_Type = Integer32
_UxsStatusNetIPktCrit_Object = MibTableColumn
uxsStatusNetIPktCrit = _UxsStatusNetIPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 6),
    _UxsStatusNetIPktCrit_Type()
)
uxsStatusNetIPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetIPktCrit.setStatus("mandatory")


class _UxsStatusNetIPktMonitor_Type(Integer32):
    """Custom type uxsStatusNetIPktMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetIPktMonitor_Type.__name__ = "Integer32"
_UxsStatusNetIPktMonitor_Object = MibTableColumn
uxsStatusNetIPktMonitor = _UxsStatusNetIPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 7),
    _UxsStatusNetIPktMonitor_Type()
)
uxsStatusNetIPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetIPktMonitor.setStatus("mandatory")


class _UxsStatusNetIPktStatus_Type(Integer32):
    """Custom type uxsStatusNetIPktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetIPktStatus_Type.__name__ = "Integer32"
_UxsStatusNetIPktStatus_Object = MibTableColumn
uxsStatusNetIPktStatus = _UxsStatusNetIPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 8),
    _UxsStatusNetIPktStatus_Type()
)
uxsStatusNetIPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetIPktStatus.setStatus("mandatory")
_UxsStatusNetIErrValue_Type = Integer32
_UxsStatusNetIErrValue_Object = MibTableColumn
uxsStatusNetIErrValue = _UxsStatusNetIErrValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 9),
    _UxsStatusNetIErrValue_Type()
)
uxsStatusNetIErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetIErrValue.setStatus("mandatory")
_UxsStatusNetIErrWarn_Type = Integer32
_UxsStatusNetIErrWarn_Object = MibTableColumn
uxsStatusNetIErrWarn = _UxsStatusNetIErrWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 10),
    _UxsStatusNetIErrWarn_Type()
)
uxsStatusNetIErrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetIErrWarn.setStatus("mandatory")
_UxsStatusNetIErrCrit_Type = Integer32
_UxsStatusNetIErrCrit_Object = MibTableColumn
uxsStatusNetIErrCrit = _UxsStatusNetIErrCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 11),
    _UxsStatusNetIErrCrit_Type()
)
uxsStatusNetIErrCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetIErrCrit.setStatus("mandatory")


class _UxsStatusNetIErrMonitor_Type(Integer32):
    """Custom type uxsStatusNetIErrMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetIErrMonitor_Type.__name__ = "Integer32"
_UxsStatusNetIErrMonitor_Object = MibTableColumn
uxsStatusNetIErrMonitor = _UxsStatusNetIErrMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 12),
    _UxsStatusNetIErrMonitor_Type()
)
uxsStatusNetIErrMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetIErrMonitor.setStatus("mandatory")


class _UxsStatusNetIErrStatus_Type(Integer32):
    """Custom type uxsStatusNetIErrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetIErrStatus_Type.__name__ = "Integer32"
_UxsStatusNetIErrStatus_Object = MibTableColumn
uxsStatusNetIErrStatus = _UxsStatusNetIErrStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 13),
    _UxsStatusNetIErrStatus_Type()
)
uxsStatusNetIErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetIErrStatus.setStatus("mandatory")
_UxsStatusNetOPktValue_Type = Integer32
_UxsStatusNetOPktValue_Object = MibTableColumn
uxsStatusNetOPktValue = _UxsStatusNetOPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 14),
    _UxsStatusNetOPktValue_Type()
)
uxsStatusNetOPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetOPktValue.setStatus("mandatory")
_UxsStatusNetOPktWarn_Type = Integer32
_UxsStatusNetOPktWarn_Object = MibTableColumn
uxsStatusNetOPktWarn = _UxsStatusNetOPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 15),
    _UxsStatusNetOPktWarn_Type()
)
uxsStatusNetOPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetOPktWarn.setStatus("mandatory")
_UxsStatusNetOPktCrit_Type = Integer32
_UxsStatusNetOPktCrit_Object = MibTableColumn
uxsStatusNetOPktCrit = _UxsStatusNetOPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 16),
    _UxsStatusNetOPktCrit_Type()
)
uxsStatusNetOPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetOPktCrit.setStatus("mandatory")


class _UxsStatusNetOPktMonitor_Type(Integer32):
    """Custom type uxsStatusNetOPktMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetOPktMonitor_Type.__name__ = "Integer32"
_UxsStatusNetOPktMonitor_Object = MibTableColumn
uxsStatusNetOPktMonitor = _UxsStatusNetOPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 17),
    _UxsStatusNetOPktMonitor_Type()
)
uxsStatusNetOPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetOPktMonitor.setStatus("mandatory")


class _UxsStatusNetOPktStatus_Type(Integer32):
    """Custom type uxsStatusNetOPktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetOPktStatus_Type.__name__ = "Integer32"
_UxsStatusNetOPktStatus_Object = MibTableColumn
uxsStatusNetOPktStatus = _UxsStatusNetOPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 18),
    _UxsStatusNetOPktStatus_Type()
)
uxsStatusNetOPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetOPktStatus.setStatus("mandatory")
_UxsStatusNetOErrValue_Type = Integer32
_UxsStatusNetOErrValue_Object = MibTableColumn
uxsStatusNetOErrValue = _UxsStatusNetOErrValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 19),
    _UxsStatusNetOErrValue_Type()
)
uxsStatusNetOErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetOErrValue.setStatus("mandatory")
_UxsStatusNetOErrWarn_Type = Integer32
_UxsStatusNetOErrWarn_Object = MibTableColumn
uxsStatusNetOErrWarn = _UxsStatusNetOErrWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 20),
    _UxsStatusNetOErrWarn_Type()
)
uxsStatusNetOErrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetOErrWarn.setStatus("mandatory")
_UxsStatusNetOErrCrit_Type = Integer32
_UxsStatusNetOErrCrit_Object = MibTableColumn
uxsStatusNetOErrCrit = _UxsStatusNetOErrCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 21),
    _UxsStatusNetOErrCrit_Type()
)
uxsStatusNetOErrCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetOErrCrit.setStatus("mandatory")


class _UxsStatusNetOErrMonitor_Type(Integer32):
    """Custom type uxsStatusNetOErrMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetOErrMonitor_Type.__name__ = "Integer32"
_UxsStatusNetOErrMonitor_Object = MibTableColumn
uxsStatusNetOErrMonitor = _UxsStatusNetOErrMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 22),
    _UxsStatusNetOErrMonitor_Type()
)
uxsStatusNetOErrMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetOErrMonitor.setStatus("mandatory")


class _UxsStatusNetOErrStatus_Type(Integer32):
    """Custom type uxsStatusNetOErrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetOErrStatus_Type.__name__ = "Integer32"
_UxsStatusNetOErrStatus_Object = MibTableColumn
uxsStatusNetOErrStatus = _UxsStatusNetOErrStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 23),
    _UxsStatusNetOErrStatus_Type()
)
uxsStatusNetOErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetOErrStatus.setStatus("mandatory")
_UxsStatusNetCollValue_Type = Integer32
_UxsStatusNetCollValue_Object = MibTableColumn
uxsStatusNetCollValue = _UxsStatusNetCollValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 24),
    _UxsStatusNetCollValue_Type()
)
uxsStatusNetCollValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetCollValue.setStatus("mandatory")
_UxsStatusNetCollWarn_Type = Integer32
_UxsStatusNetCollWarn_Object = MibTableColumn
uxsStatusNetCollWarn = _UxsStatusNetCollWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 25),
    _UxsStatusNetCollWarn_Type()
)
uxsStatusNetCollWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetCollWarn.setStatus("mandatory")
_UxsStatusNetCollCrit_Type = Integer32
_UxsStatusNetCollCrit_Object = MibTableColumn
uxsStatusNetCollCrit = _UxsStatusNetCollCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 26),
    _UxsStatusNetCollCrit_Type()
)
uxsStatusNetCollCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetCollCrit.setStatus("mandatory")


class _UxsStatusNetCollMonitor_Type(Integer32):
    """Custom type uxsStatusNetCollMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusNetCollMonitor_Type.__name__ = "Integer32"
_UxsStatusNetCollMonitor_Object = MibTableColumn
uxsStatusNetCollMonitor = _UxsStatusNetCollMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 27),
    _UxsStatusNetCollMonitor_Type()
)
uxsStatusNetCollMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetCollMonitor.setStatus("mandatory")


class _UxsStatusNetCollStatus_Type(Integer32):
    """Custom type uxsStatusNetCollStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusNetCollStatus_Type.__name__ = "Integer32"
_UxsStatusNetCollStatus_Object = MibTableColumn
uxsStatusNetCollStatus = _UxsStatusNetCollStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 28),
    _UxsStatusNetCollStatus_Type()
)
uxsStatusNetCollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetCollStatus.setStatus("mandatory")


class _UxsStatusNetLossAction_Type(Integer32):
    """Custom type uxsStatusNetLossAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("remove", 1),
          ("up", 2))
    )


_UxsStatusNetLossAction_Type.__name__ = "Integer32"
_UxsStatusNetLossAction_Object = MibTableColumn
uxsStatusNetLossAction = _UxsStatusNetLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 29),
    _UxsStatusNetLossAction_Type()
)
uxsStatusNetLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusNetLossAction.setStatus("mandatory")


class _UxsStatusNetLossStatus_Type(Integer32):
    """Custom type uxsStatusNetLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_UxsStatusNetLossStatus_Type.__name__ = "Integer32"
_UxsStatusNetLossStatus_Object = MibTableColumn
uxsStatusNetLossStatus = _UxsStatusNetLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 11, 28, 1, 30),
    _UxsStatusNetLossStatus_Type()
)
uxsStatusNetLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusNetLossStatus.setStatus("mandatory")
_UxsStatusIPCGroup_ObjectIdentity = ObjectIdentity
uxsStatusIPCGroup = _UxsStatusIPCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12)
)
_UxsStatusIPCSHMIDSAvailable_Type = Integer32
_UxsStatusIPCSHMIDSAvailable_Object = MibScalar
uxsStatusIPCSHMIDSAvailable = _UxsStatusIPCSHMIDSAvailable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 1),
    _UxsStatusIPCSHMIDSAvailable_Type()
)
uxsStatusIPCSHMIDSAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSAvailable.setStatus("mandatory")
_UxsStatusIPCSHMIDSValue_Type = Integer32
_UxsStatusIPCSHMIDSValue_Object = MibScalar
uxsStatusIPCSHMIDSValue = _UxsStatusIPCSHMIDSValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 2),
    _UxsStatusIPCSHMIDSValue_Type()
)
uxsStatusIPCSHMIDSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSValue.setStatus("mandatory")
_UxsStatusIPCSHMIDSLagValue_Type = Integer32
_UxsStatusIPCSHMIDSLagValue_Object = MibScalar
uxsStatusIPCSHMIDSLagValue = _UxsStatusIPCSHMIDSLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 3),
    _UxsStatusIPCSHMIDSLagValue_Type()
)
uxsStatusIPCSHMIDSLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSLagValue.setStatus("mandatory")
_UxsStatusIPCSHMIDSLag_Type = Integer32
_UxsStatusIPCSHMIDSLag_Object = MibScalar
uxsStatusIPCSHMIDSLag = _UxsStatusIPCSHMIDSLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 4),
    _UxsStatusIPCSHMIDSLag_Type()
)
uxsStatusIPCSHMIDSLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSLag.setStatus("mandatory")
_UxsStatusIPCSHMIDSWarnValue_Type = DisplayString
_UxsStatusIPCSHMIDSWarnValue_Object = MibScalar
uxsStatusIPCSHMIDSWarnValue = _UxsStatusIPCSHMIDSWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 5),
    _UxsStatusIPCSHMIDSWarnValue_Type()
)
uxsStatusIPCSHMIDSWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSWarnValue.setStatus("mandatory")
_UxsStatusIPCSHMIDSCritValue_Type = DisplayString
_UxsStatusIPCSHMIDSCritValue_Object = MibScalar
uxsStatusIPCSHMIDSCritValue = _UxsStatusIPCSHMIDSCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 6),
    _UxsStatusIPCSHMIDSCritValue_Type()
)
uxsStatusIPCSHMIDSCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSCritValue.setStatus("mandatory")
_UxsStatusIPCSHMIDSWarn_Type = DisplayString
_UxsStatusIPCSHMIDSWarn_Object = MibScalar
uxsStatusIPCSHMIDSWarn = _UxsStatusIPCSHMIDSWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 7),
    _UxsStatusIPCSHMIDSWarn_Type()
)
uxsStatusIPCSHMIDSWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSWarn.setStatus("mandatory")
_UxsStatusIPCSHMIDSCrit_Type = DisplayString
_UxsStatusIPCSHMIDSCrit_Object = MibScalar
uxsStatusIPCSHMIDSCrit = _UxsStatusIPCSHMIDSCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 8),
    _UxsStatusIPCSHMIDSCrit_Type()
)
uxsStatusIPCSHMIDSCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSCrit.setStatus("mandatory")


class _UxsStatusIPCSHMIDSMonitor_Type(Integer32):
    """Custom type uxsStatusIPCSHMIDSMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusIPCSHMIDSMonitor_Type.__name__ = "Integer32"
_UxsStatusIPCSHMIDSMonitor_Object = MibScalar
uxsStatusIPCSHMIDSMonitor = _UxsStatusIPCSHMIDSMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 9),
    _UxsStatusIPCSHMIDSMonitor_Type()
)
uxsStatusIPCSHMIDSMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSMonitor.setStatus("mandatory")


class _UxsStatusIPCSHMIDSStatus_Type(Integer32):
    """Custom type uxsStatusIPCSHMIDSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusIPCSHMIDSStatus_Type.__name__ = "Integer32"
_UxsStatusIPCSHMIDSStatus_Object = MibScalar
uxsStatusIPCSHMIDSStatus = _UxsStatusIPCSHMIDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 10),
    _UxsStatusIPCSHMIDSStatus_Type()
)
uxsStatusIPCSHMIDSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSHMIDSStatus.setStatus("mandatory")
_UxsStatusIPCSEMIDSAvailable_Type = Integer32
_UxsStatusIPCSEMIDSAvailable_Object = MibScalar
uxsStatusIPCSEMIDSAvailable = _UxsStatusIPCSEMIDSAvailable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 11),
    _UxsStatusIPCSEMIDSAvailable_Type()
)
uxsStatusIPCSEMIDSAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSAvailable.setStatus("mandatory")
_UxsStatusIPCSEMIDSValue_Type = Integer32
_UxsStatusIPCSEMIDSValue_Object = MibScalar
uxsStatusIPCSEMIDSValue = _UxsStatusIPCSEMIDSValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 12),
    _UxsStatusIPCSEMIDSValue_Type()
)
uxsStatusIPCSEMIDSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSValue.setStatus("mandatory")
_UxsStatusIPCSEMIDSLagValue_Type = Integer32
_UxsStatusIPCSEMIDSLagValue_Object = MibScalar
uxsStatusIPCSEMIDSLagValue = _UxsStatusIPCSEMIDSLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 13),
    _UxsStatusIPCSEMIDSLagValue_Type()
)
uxsStatusIPCSEMIDSLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSLagValue.setStatus("mandatory")
_UxsStatusIPCSEMIDSLag_Type = Integer32
_UxsStatusIPCSEMIDSLag_Object = MibScalar
uxsStatusIPCSEMIDSLag = _UxsStatusIPCSEMIDSLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 14),
    _UxsStatusIPCSEMIDSLag_Type()
)
uxsStatusIPCSEMIDSLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSLag.setStatus("mandatory")
_UxsStatusIPCSEMIDSWarnValue_Type = DisplayString
_UxsStatusIPCSEMIDSWarnValue_Object = MibScalar
uxsStatusIPCSEMIDSWarnValue = _UxsStatusIPCSEMIDSWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 15),
    _UxsStatusIPCSEMIDSWarnValue_Type()
)
uxsStatusIPCSEMIDSWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSWarnValue.setStatus("mandatory")
_UxsStatusIPCSEMIDSCritValue_Type = DisplayString
_UxsStatusIPCSEMIDSCritValue_Object = MibScalar
uxsStatusIPCSEMIDSCritValue = _UxsStatusIPCSEMIDSCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 16),
    _UxsStatusIPCSEMIDSCritValue_Type()
)
uxsStatusIPCSEMIDSCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSCritValue.setStatus("mandatory")
_UxsStatusIPCSEMIDSWarn_Type = DisplayString
_UxsStatusIPCSEMIDSWarn_Object = MibScalar
uxsStatusIPCSEMIDSWarn = _UxsStatusIPCSEMIDSWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 17),
    _UxsStatusIPCSEMIDSWarn_Type()
)
uxsStatusIPCSEMIDSWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSWarn.setStatus("mandatory")
_UxsStatusIPCSEMIDSCrit_Type = DisplayString
_UxsStatusIPCSEMIDSCrit_Object = MibScalar
uxsStatusIPCSEMIDSCrit = _UxsStatusIPCSEMIDSCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 18),
    _UxsStatusIPCSEMIDSCrit_Type()
)
uxsStatusIPCSEMIDSCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSCrit.setStatus("mandatory")


class _UxsStatusIPCSEMIDSMonitor_Type(Integer32):
    """Custom type uxsStatusIPCSEMIDSMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusIPCSEMIDSMonitor_Type.__name__ = "Integer32"
_UxsStatusIPCSEMIDSMonitor_Object = MibScalar
uxsStatusIPCSEMIDSMonitor = _UxsStatusIPCSEMIDSMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 19),
    _UxsStatusIPCSEMIDSMonitor_Type()
)
uxsStatusIPCSEMIDSMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSMonitor.setStatus("mandatory")


class _UxsStatusIPCSEMIDSStatus_Type(Integer32):
    """Custom type uxsStatusIPCSEMIDSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusIPCSEMIDSStatus_Type.__name__ = "Integer32"
_UxsStatusIPCSEMIDSStatus_Object = MibScalar
uxsStatusIPCSEMIDSStatus = _UxsStatusIPCSEMIDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 20),
    _UxsStatusIPCSEMIDSStatus_Type()
)
uxsStatusIPCSEMIDSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCSEMIDSStatus.setStatus("mandatory")
_UxsStatusIPCMQIDSAvailable_Type = Integer32
_UxsStatusIPCMQIDSAvailable_Object = MibScalar
uxsStatusIPCMQIDSAvailable = _UxsStatusIPCMQIDSAvailable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 21),
    _UxsStatusIPCMQIDSAvailable_Type()
)
uxsStatusIPCMQIDSAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSAvailable.setStatus("mandatory")
_UxsStatusIPCMQIDSValue_Type = Integer32
_UxsStatusIPCMQIDSValue_Object = MibScalar
uxsStatusIPCMQIDSValue = _UxsStatusIPCMQIDSValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 22),
    _UxsStatusIPCMQIDSValue_Type()
)
uxsStatusIPCMQIDSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSValue.setStatus("mandatory")
_UxsStatusIPCMQIDSLagValue_Type = Integer32
_UxsStatusIPCMQIDSLagValue_Object = MibScalar
uxsStatusIPCMQIDSLagValue = _UxsStatusIPCMQIDSLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 23),
    _UxsStatusIPCMQIDSLagValue_Type()
)
uxsStatusIPCMQIDSLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSLagValue.setStatus("mandatory")
_UxsStatusIPCMQIDSLag_Type = Integer32
_UxsStatusIPCMQIDSLag_Object = MibScalar
uxsStatusIPCMQIDSLag = _UxsStatusIPCMQIDSLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 24),
    _UxsStatusIPCMQIDSLag_Type()
)
uxsStatusIPCMQIDSLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSLag.setStatus("mandatory")
_UxsStatusIPCMQIDSWarnValue_Type = DisplayString
_UxsStatusIPCMQIDSWarnValue_Object = MibScalar
uxsStatusIPCMQIDSWarnValue = _UxsStatusIPCMQIDSWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 25),
    _UxsStatusIPCMQIDSWarnValue_Type()
)
uxsStatusIPCMQIDSWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSWarnValue.setStatus("mandatory")
_UxsStatusIPCMQIDSCritValue_Type = DisplayString
_UxsStatusIPCMQIDSCritValue_Object = MibScalar
uxsStatusIPCMQIDSCritValue = _UxsStatusIPCMQIDSCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 26),
    _UxsStatusIPCMQIDSCritValue_Type()
)
uxsStatusIPCMQIDSCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSCritValue.setStatus("mandatory")
_UxsStatusIPCMQIDSWarn_Type = DisplayString
_UxsStatusIPCMQIDSWarn_Object = MibScalar
uxsStatusIPCMQIDSWarn = _UxsStatusIPCMQIDSWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 27),
    _UxsStatusIPCMQIDSWarn_Type()
)
uxsStatusIPCMQIDSWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSWarn.setStatus("mandatory")
_UxsStatusIPCMQIDSCrit_Type = DisplayString
_UxsStatusIPCMQIDSCrit_Object = MibScalar
uxsStatusIPCMQIDSCrit = _UxsStatusIPCMQIDSCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 28),
    _UxsStatusIPCMQIDSCrit_Type()
)
uxsStatusIPCMQIDSCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSCrit.setStatus("mandatory")


class _UxsStatusIPCMQIDSMonitor_Type(Integer32):
    """Custom type uxsStatusIPCMQIDSMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusIPCMQIDSMonitor_Type.__name__ = "Integer32"
_UxsStatusIPCMQIDSMonitor_Object = MibScalar
uxsStatusIPCMQIDSMonitor = _UxsStatusIPCMQIDSMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 29),
    _UxsStatusIPCMQIDSMonitor_Type()
)
uxsStatusIPCMQIDSMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSMonitor.setStatus("mandatory")


class _UxsStatusIPCMQIDSStatus_Type(Integer32):
    """Custom type uxsStatusIPCMQIDSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusIPCMQIDSStatus_Type.__name__ = "Integer32"
_UxsStatusIPCMQIDSStatus_Object = MibScalar
uxsStatusIPCMQIDSStatus = _UxsStatusIPCMQIDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 30),
    _UxsStatusIPCMQIDSStatus_Type()
)
uxsStatusIPCMQIDSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQIDSStatus.setStatus("mandatory")


class _UxsStatusIPCMQMonitor_Type(Integer32):
    """Custom type uxsStatusIPCMQMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsStatusIPCMQMonitor_Type.__name__ = "Integer32"
_UxsStatusIPCMQMonitor_Object = MibScalar
uxsStatusIPCMQMonitor = _UxsStatusIPCMQMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 31),
    _UxsStatusIPCMQMonitor_Type()
)
uxsStatusIPCMQMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQMonitor.setStatus("mandatory")
_UxsStatusIPCMQCount_Type = Integer32
_UxsStatusIPCMQCount_Object = MibScalar
uxsStatusIPCMQCount = _UxsStatusIPCMQCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 32),
    _UxsStatusIPCMQCount_Type()
)
uxsStatusIPCMQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQCount.setStatus("mandatory")
_UxsStatusIPCMQTable_Object = MibTable
uxsStatusIPCMQTable = _UxsStatusIPCMQTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33)
)
if mibBuilder.loadTexts:
    uxsStatusIPCMQTable.setStatus("mandatory")
_UxsStatusIPCMQEntry_Object = MibTableRow
uxsStatusIPCMQEntry = _UxsStatusIPCMQEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1)
)
uxsStatusIPCMQEntry.setIndexNames(
    (0, "CAIUXOS", "uxsStatusIPCMQID"),
)
if mibBuilder.loadTexts:
    uxsStatusIPCMQEntry.setStatus("mandatory")
_UxsStatusIPCMQID_Type = DisplayString
_UxsStatusIPCMQID_Object = MibTableColumn
uxsStatusIPCMQID = _UxsStatusIPCMQID_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 1),
    _UxsStatusIPCMQID_Type()
)
uxsStatusIPCMQID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQID.setStatus("mandatory")
_UxsStatusIPCMQKey_Type = DisplayString
_UxsStatusIPCMQKey_Object = MibTableColumn
uxsStatusIPCMQKey = _UxsStatusIPCMQKey_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 2),
    _UxsStatusIPCMQKey_Type()
)
uxsStatusIPCMQKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQKey.setStatus("mandatory")
_UxsStatusIPCMQMode_Type = DisplayString
_UxsStatusIPCMQMode_Object = MibTableColumn
uxsStatusIPCMQMode = _UxsStatusIPCMQMode_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 3),
    _UxsStatusIPCMQMode_Type()
)
uxsStatusIPCMQMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQMode.setStatus("mandatory")
_UxsStatusIPCMQOwner_Type = DisplayString
_UxsStatusIPCMQOwner_Object = MibTableColumn
uxsStatusIPCMQOwner = _UxsStatusIPCMQOwner_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 4),
    _UxsStatusIPCMQOwner_Type()
)
uxsStatusIPCMQOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQOwner.setStatus("mandatory")
_UxsStatusIPCMQGroup_Type = DisplayString
_UxsStatusIPCMQGroup_Object = MibTableColumn
uxsStatusIPCMQGroup = _UxsStatusIPCMQGroup_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 5),
    _UxsStatusIPCMQGroup_Type()
)
uxsStatusIPCMQGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQGroup.setStatus("mandatory")
_UxsStatusIPCMQBytesAvailable_Type = Integer32
_UxsStatusIPCMQBytesAvailable_Object = MibTableColumn
uxsStatusIPCMQBytesAvailable = _UxsStatusIPCMQBytesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 6),
    _UxsStatusIPCMQBytesAvailable_Type()
)
uxsStatusIPCMQBytesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesAvailable.setStatus("mandatory")
_UxsStatusIPCMQBytesValue_Type = Integer32
_UxsStatusIPCMQBytesValue_Object = MibTableColumn
uxsStatusIPCMQBytesValue = _UxsStatusIPCMQBytesValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 7),
    _UxsStatusIPCMQBytesValue_Type()
)
uxsStatusIPCMQBytesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesValue.setStatus("mandatory")
_UxsStatusIPCMQBytesLagValue_Type = Integer32
_UxsStatusIPCMQBytesLagValue_Object = MibTableColumn
uxsStatusIPCMQBytesLagValue = _UxsStatusIPCMQBytesLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 8),
    _UxsStatusIPCMQBytesLagValue_Type()
)
uxsStatusIPCMQBytesLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesLagValue.setStatus("mandatory")
_UxsStatusIPCMQBytesLag_Type = Integer32
_UxsStatusIPCMQBytesLag_Object = MibTableColumn
uxsStatusIPCMQBytesLag = _UxsStatusIPCMQBytesLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 9),
    _UxsStatusIPCMQBytesLag_Type()
)
uxsStatusIPCMQBytesLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesLag.setStatus("mandatory")
_UxsStatusIPCMQBytesWarnValue_Type = DisplayString
_UxsStatusIPCMQBytesWarnValue_Object = MibTableColumn
uxsStatusIPCMQBytesWarnValue = _UxsStatusIPCMQBytesWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 10),
    _UxsStatusIPCMQBytesWarnValue_Type()
)
uxsStatusIPCMQBytesWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesWarnValue.setStatus("mandatory")
_UxsStatusIPCMQBytesCritValue_Type = DisplayString
_UxsStatusIPCMQBytesCritValue_Object = MibTableColumn
uxsStatusIPCMQBytesCritValue = _UxsStatusIPCMQBytesCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 12),
    _UxsStatusIPCMQBytesCritValue_Type()
)
uxsStatusIPCMQBytesCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesCritValue.setStatus("mandatory")
_UxsStatusIPCMQBytesWarn_Type = DisplayString
_UxsStatusIPCMQBytesWarn_Object = MibTableColumn
uxsStatusIPCMQBytesWarn = _UxsStatusIPCMQBytesWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 13),
    _UxsStatusIPCMQBytesWarn_Type()
)
uxsStatusIPCMQBytesWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesWarn.setStatus("mandatory")
_UxsStatusIPCMQBytesCrit_Type = DisplayString
_UxsStatusIPCMQBytesCrit_Object = MibTableColumn
uxsStatusIPCMQBytesCrit = _UxsStatusIPCMQBytesCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 14),
    _UxsStatusIPCMQBytesCrit_Type()
)
uxsStatusIPCMQBytesCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesCrit.setStatus("mandatory")


class _UxsStatusIPCMQBytesMonitor_Type(Integer32):
    """Custom type uxsStatusIPCMQBytesMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_UxsStatusIPCMQBytesMonitor_Type.__name__ = "Integer32"
_UxsStatusIPCMQBytesMonitor_Object = MibTableColumn
uxsStatusIPCMQBytesMonitor = _UxsStatusIPCMQBytesMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 15),
    _UxsStatusIPCMQBytesMonitor_Type()
)
uxsStatusIPCMQBytesMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesMonitor.setStatus("mandatory")


class _UxsStatusIPCMQBytesStatus_Type(Integer32):
    """Custom type uxsStatusIPCMQBytesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UxsStatusIPCMQBytesStatus_Type.__name__ = "Integer32"
_UxsStatusIPCMQBytesStatus_Object = MibTableColumn
uxsStatusIPCMQBytesStatus = _UxsStatusIPCMQBytesStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 2, 12, 33, 1, 16),
    _UxsStatusIPCMQBytesStatus_Type()
)
uxsStatusIPCMQBytesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsStatusIPCMQBytesStatus.setStatus("mandatory")
_UxsAvailableGroup_ObjectIdentity = ObjectIdentity
uxsAvailableGroup = _UxsAvailableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3)
)


class _UxsAvailFSysRefresh_Type(Integer32):
    """Custom type uxsAvailFSysRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_UxsAvailFSysRefresh_Type.__name__ = "Integer32"
_UxsAvailFSysRefresh_Object = MibScalar
uxsAvailFSysRefresh = _UxsAvailFSysRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 1),
    _UxsAvailFSysRefresh_Type()
)
uxsAvailFSysRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsAvailFSysRefresh.setStatus("mandatory")
_UxsAvailFSysTable_Object = MibTable
uxsAvailFSysTable = _UxsAvailFSysTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 2)
)
if mibBuilder.loadTexts:
    uxsAvailFSysTable.setStatus("mandatory")
_UxsAvailFSysEntry_Object = MibTableRow
uxsAvailFSysEntry = _UxsAvailFSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 2, 1)
)
uxsAvailFSysEntry.setIndexNames(
    (0, "CAIUXOS", "uxsAvailFSysName"),
)
if mibBuilder.loadTexts:
    uxsAvailFSysEntry.setStatus("mandatory")
_UxsAvailFSysName_Type = DisplayString
_UxsAvailFSysName_Object = MibTableColumn
uxsAvailFSysName = _UxsAvailFSysName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 2, 1, 1),
    _UxsAvailFSysName_Type()
)
uxsAvailFSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsAvailFSysName.setStatus("mandatory")
_UxsAvailFSysRelatedTo_Type = DisplayString
_UxsAvailFSysRelatedTo_Object = MibTableColumn
uxsAvailFSysRelatedTo = _UxsAvailFSysRelatedTo_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 2, 1, 2),
    _UxsAvailFSysRelatedTo_Type()
)
uxsAvailFSysRelatedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsAvailFSysRelatedTo.setStatus("mandatory")
_UxsAvailFSysType_Type = DisplayString
_UxsAvailFSysType_Object = MibTableColumn
uxsAvailFSysType = _UxsAvailFSysType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 2, 1, 3),
    _UxsAvailFSysType_Type()
)
uxsAvailFSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsAvailFSysType.setStatus("mandatory")


class _UxsAvailDiskRefresh_Type(Integer32):
    """Custom type uxsAvailDiskRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_UxsAvailDiskRefresh_Type.__name__ = "Integer32"
_UxsAvailDiskRefresh_Object = MibScalar
uxsAvailDiskRefresh = _UxsAvailDiskRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 3),
    _UxsAvailDiskRefresh_Type()
)
uxsAvailDiskRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsAvailDiskRefresh.setStatus("mandatory")
_UxsAvailDiskTable_Object = MibTable
uxsAvailDiskTable = _UxsAvailDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 4)
)
if mibBuilder.loadTexts:
    uxsAvailDiskTable.setStatus("mandatory")
_UxsAvailDiskEntry_Object = MibTableRow
uxsAvailDiskEntry = _UxsAvailDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 4, 1)
)
uxsAvailDiskEntry.setIndexNames(
    (0, "CAIUXOS", "uxsAvailDiskName"),
)
if mibBuilder.loadTexts:
    uxsAvailDiskEntry.setStatus("mandatory")
_UxsAvailDiskName_Type = DisplayString
_UxsAvailDiskName_Object = MibTableColumn
uxsAvailDiskName = _UxsAvailDiskName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 4, 1, 1),
    _UxsAvailDiskName_Type()
)
uxsAvailDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsAvailDiskName.setStatus("mandatory")


class _UxsAvailPrnRefresh_Type(Integer32):
    """Custom type uxsAvailPrnRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_UxsAvailPrnRefresh_Type.__name__ = "Integer32"
_UxsAvailPrnRefresh_Object = MibScalar
uxsAvailPrnRefresh = _UxsAvailPrnRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 5),
    _UxsAvailPrnRefresh_Type()
)
uxsAvailPrnRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsAvailPrnRefresh.setStatus("mandatory")
_UxsAvailPrnTable_Object = MibTable
uxsAvailPrnTable = _UxsAvailPrnTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 6)
)
if mibBuilder.loadTexts:
    uxsAvailPrnTable.setStatus("mandatory")
_UxsAvailPrnEntry_Object = MibTableRow
uxsAvailPrnEntry = _UxsAvailPrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 6, 1)
)
uxsAvailPrnEntry.setIndexNames(
    (0, "CAIUXOS", "uxsAvailPrnName"),
)
if mibBuilder.loadTexts:
    uxsAvailPrnEntry.setStatus("mandatory")
_UxsAvailPrnName_Type = DisplayString
_UxsAvailPrnName_Object = MibTableColumn
uxsAvailPrnName = _UxsAvailPrnName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 3, 6, 1, 1),
    _UxsAvailPrnName_Type()
)
uxsAvailPrnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsAvailPrnName.setStatus("mandatory")
_UxsPollGroup_ObjectIdentity = ObjectIdentity
uxsPollGroup = _UxsPollGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4)
)
_UxsPollNetGroup_ObjectIdentity = ObjectIdentity
uxsPollNetGroup = _UxsPollNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1)
)
_UxsPollNetTable_Object = MibTable
uxsPollNetTable = _UxsPollNetTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    uxsPollNetTable.setStatus("mandatory")
_UxsPollNetEntry_Object = MibTableRow
uxsPollNetEntry = _UxsPollNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1)
)
uxsPollNetEntry.setIndexNames(
    (0, "CAIUXOS", "uxsPollNetName"),
)
if mibBuilder.loadTexts:
    uxsPollNetEntry.setStatus("mandatory")
_UxsPollNetName_Type = DisplayString
_UxsPollNetName_Object = MibTableColumn
uxsPollNetName = _UxsPollNetName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 1),
    _UxsPollNetName_Type()
)
uxsPollNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetName.setStatus("mandatory")
_UxsPollNetIP_Type = DisplayString
_UxsPollNetIP_Object = MibTableColumn
uxsPollNetIP = _UxsPollNetIP_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 2),
    _UxsPollNetIP_Type()
)
uxsPollNetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetIP.setStatus("mandatory")
_UxsPollNetIPktValue_Type = Integer32
_UxsPollNetIPktValue_Object = MibTableColumn
uxsPollNetIPktValue = _UxsPollNetIPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 3),
    _UxsPollNetIPktValue_Type()
)
uxsPollNetIPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetIPktValue.setStatus("mandatory")
_UxsPollNetIErrValue_Type = Integer32
_UxsPollNetIErrValue_Object = MibTableColumn
uxsPollNetIErrValue = _UxsPollNetIErrValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 4),
    _UxsPollNetIErrValue_Type()
)
uxsPollNetIErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetIErrValue.setStatus("mandatory")
_UxsPollNetOPktValue_Type = Integer32
_UxsPollNetOPktValue_Object = MibTableColumn
uxsPollNetOPktValue = _UxsPollNetOPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 5),
    _UxsPollNetOPktValue_Type()
)
uxsPollNetOPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetOPktValue.setStatus("mandatory")
_UxsPollNetOErrValue_Type = Integer32
_UxsPollNetOErrValue_Object = MibTableColumn
uxsPollNetOErrValue = _UxsPollNetOErrValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 6),
    _UxsPollNetOErrValue_Type()
)
uxsPollNetOErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetOErrValue.setStatus("mandatory")
_UxsPollNetCollValue_Type = Integer32
_UxsPollNetCollValue_Object = MibTableColumn
uxsPollNetCollValue = _UxsPollNetCollValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 1, 1, 1, 7),
    _UxsPollNetCollValue_Type()
)
uxsPollNetCollValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollNetCollValue.setStatus("mandatory")
_UxsPollIPCGroup_ObjectIdentity = ObjectIdentity
uxsPollIPCGroup = _UxsPollIPCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2)
)


class _UxsPollIPCSHMMonitor_Type(Integer32):
    """Custom type uxsPollIPCSHMMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsPollIPCSHMMonitor_Type.__name__ = "Integer32"
_UxsPollIPCSHMMonitor_Object = MibScalar
uxsPollIPCSHMMonitor = _UxsPollIPCSHMMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 1),
    _UxsPollIPCSHMMonitor_Type()
)
uxsPollIPCSHMMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsPollIPCSHMMonitor.setStatus("mandatory")
_UxsPollIPCSHMCount_Type = Integer32
_UxsPollIPCSHMCount_Object = MibScalar
uxsPollIPCSHMCount = _UxsPollIPCSHMCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 2),
    _UxsPollIPCSHMCount_Type()
)
uxsPollIPCSHMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMCount.setStatus("mandatory")
_UxsPollIPCSHMTable_Object = MibTable
uxsPollIPCSHMTable = _UxsPollIPCSHMTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    uxsPollIPCSHMTable.setStatus("mandatory")
_UxsPollIPCSHMEntry_Object = MibTableRow
uxsPollIPCSHMEntry = _UxsPollIPCSHMEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1)
)
uxsPollIPCSHMEntry.setIndexNames(
    (0, "CAIUXOS", "uxsPollIPCSHMID"),
)
if mibBuilder.loadTexts:
    uxsPollIPCSHMEntry.setStatus("mandatory")
_UxsPollIPCSHMID_Type = DisplayString
_UxsPollIPCSHMID_Object = MibTableColumn
uxsPollIPCSHMID = _UxsPollIPCSHMID_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 1),
    _UxsPollIPCSHMID_Type()
)
uxsPollIPCSHMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMID.setStatus("mandatory")
_UxsPollIPCSHMKey_Type = DisplayString
_UxsPollIPCSHMKey_Object = MibTableColumn
uxsPollIPCSHMKey = _UxsPollIPCSHMKey_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 2),
    _UxsPollIPCSHMKey_Type()
)
uxsPollIPCSHMKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMKey.setStatus("mandatory")
_UxsPollIPCSHMMode_Type = DisplayString
_UxsPollIPCSHMMode_Object = MibTableColumn
uxsPollIPCSHMMode = _UxsPollIPCSHMMode_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 3),
    _UxsPollIPCSHMMode_Type()
)
uxsPollIPCSHMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMMode.setStatus("mandatory")
_UxsPollIPCSHMOwner_Type = DisplayString
_UxsPollIPCSHMOwner_Object = MibTableColumn
uxsPollIPCSHMOwner = _UxsPollIPCSHMOwner_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 4),
    _UxsPollIPCSHMOwner_Type()
)
uxsPollIPCSHMOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMOwner.setStatus("mandatory")
_UxsPollIPCSHMGroup_Type = DisplayString
_UxsPollIPCSHMGroup_Object = MibTableColumn
uxsPollIPCSHMGroup = _UxsPollIPCSHMGroup_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 5),
    _UxsPollIPCSHMGroup_Type()
)
uxsPollIPCSHMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMGroup.setStatus("mandatory")
_UxsPollIPCSHMMaxSize_Type = Integer32
_UxsPollIPCSHMMaxSize_Object = MibTableColumn
uxsPollIPCSHMMaxSize = _UxsPollIPCSHMMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 6),
    _UxsPollIPCSHMMaxSize_Type()
)
uxsPollIPCSHMMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMMaxSize.setStatus("mandatory")
_UxsPollIPCSHMAttached_Type = Integer32
_UxsPollIPCSHMAttached_Object = MibTableColumn
uxsPollIPCSHMAttached = _UxsPollIPCSHMAttached_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 3, 1, 7),
    _UxsPollIPCSHMAttached_Type()
)
uxsPollIPCSHMAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSHMAttached.setStatus("mandatory")


class _UxsPollIPCSEMMonitor_Type(Integer32):
    """Custom type uxsPollIPCSEMMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("monitor", 2))
    )


_UxsPollIPCSEMMonitor_Type.__name__ = "Integer32"
_UxsPollIPCSEMMonitor_Object = MibScalar
uxsPollIPCSEMMonitor = _UxsPollIPCSEMMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 4),
    _UxsPollIPCSEMMonitor_Type()
)
uxsPollIPCSEMMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uxsPollIPCSEMMonitor.setStatus("mandatory")
_UxsPollIPCSEMCount_Type = Integer32
_UxsPollIPCSEMCount_Object = MibScalar
uxsPollIPCSEMCount = _UxsPollIPCSEMCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 5),
    _UxsPollIPCSEMCount_Type()
)
uxsPollIPCSEMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMCount.setStatus("mandatory")
_UxsPollIPCSEMTable_Object = MibTable
uxsPollIPCSEMTable = _UxsPollIPCSEMTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6)
)
if mibBuilder.loadTexts:
    uxsPollIPCSEMTable.setStatus("mandatory")
_UxsPollIPCSEMEntry_Object = MibTableRow
uxsPollIPCSEMEntry = _UxsPollIPCSEMEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1)
)
uxsPollIPCSEMEntry.setIndexNames(
    (0, "CAIUXOS", "uxsPollIPCSEMID"),
)
if mibBuilder.loadTexts:
    uxsPollIPCSEMEntry.setStatus("mandatory")
_UxsPollIPCSEMID_Type = DisplayString
_UxsPollIPCSEMID_Object = MibTableColumn
uxsPollIPCSEMID = _UxsPollIPCSEMID_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1, 1),
    _UxsPollIPCSEMID_Type()
)
uxsPollIPCSEMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMID.setStatus("mandatory")
_UxsPollIPCSEMKey_Type = DisplayString
_UxsPollIPCSEMKey_Object = MibTableColumn
uxsPollIPCSEMKey = _UxsPollIPCSEMKey_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1, 2),
    _UxsPollIPCSEMKey_Type()
)
uxsPollIPCSEMKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMKey.setStatus("mandatory")
_UxsPollIPCSEMMode_Type = DisplayString
_UxsPollIPCSEMMode_Object = MibTableColumn
uxsPollIPCSEMMode = _UxsPollIPCSEMMode_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1, 3),
    _UxsPollIPCSEMMode_Type()
)
uxsPollIPCSEMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMMode.setStatus("mandatory")
_UxsPollIPCSEMOwner_Type = DisplayString
_UxsPollIPCSEMOwner_Object = MibTableColumn
uxsPollIPCSEMOwner = _UxsPollIPCSEMOwner_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1, 4),
    _UxsPollIPCSEMOwner_Type()
)
uxsPollIPCSEMOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMOwner.setStatus("mandatory")
_UxsPollIPCSEMGroup_Type = DisplayString
_UxsPollIPCSEMGroup_Object = MibTableColumn
uxsPollIPCSEMGroup = _UxsPollIPCSEMGroup_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1, 5),
    _UxsPollIPCSEMGroup_Type()
)
uxsPollIPCSEMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMGroup.setStatus("mandatory")
_UxsPollIPCSEMMaxNums_Type = Integer32
_UxsPollIPCSEMMaxNums_Object = MibTableColumn
uxsPollIPCSEMMaxNums = _UxsPollIPCSEMMaxNums_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 4, 2, 6, 1, 6),
    _UxsPollIPCSEMMaxNums_Type()
)
uxsPollIPCSEMMaxNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxsPollIPCSEMMaxNums.setStatus("mandatory")

# Managed Objects groups


# Notification objects

uxsCPUTotalUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10000)
)
if mibBuilder.loadTexts:
    uxsCPUTotalUnknown.setStatus(
        ""
    )

uxsCPUTotalOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10001)
)
if mibBuilder.loadTexts:
    uxsCPUTotalOK.setStatus(
        ""
    )

uxsCPUTotalWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10002)
)
if mibBuilder.loadTexts:
    uxsCPUTotalWarning.setStatus(
        ""
    )

uxsCPUTotalCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10003)
)
if mibBuilder.loadTexts:
    uxsCPUTotalCritical.setStatus(
        ""
    )

uxsCPUUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10990)
)
if mibBuilder.loadTexts:
    uxsCPUUnknown.setStatus(
        ""
    )

uxsCPUOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10991)
)
if mibBuilder.loadTexts:
    uxsCPUOK.setStatus(
        ""
    )

uxsCPUWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10992)
)
if mibBuilder.loadTexts:
    uxsCPUWarning.setStatus(
        ""
    )

uxsCPUCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10993)
)
if mibBuilder.loadTexts:
    uxsCPUCritical.setStatus(
        ""
    )

uxsCPUDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10995)
)
if mibBuilder.loadTexts:
    uxsCPUDown.setStatus(
        ""
    )

uxsCPUAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10996)
)
if mibBuilder.loadTexts:
    uxsCPUAdded.setStatus(
        ""
    )

uxsCPUDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 10997)
)
if mibBuilder.loadTexts:
    uxsCPUDeleted.setStatus(
        ""
    )

uxsLoad1Unknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11010)
)
if mibBuilder.loadTexts:
    uxsLoad1Unknown.setStatus(
        ""
    )

uxsLoad1OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11011)
)
if mibBuilder.loadTexts:
    uxsLoad1OK.setStatus(
        ""
    )

uxsLoad1Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11012)
)
if mibBuilder.loadTexts:
    uxsLoad1Warning.setStatus(
        ""
    )

uxsLoad1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11013)
)
if mibBuilder.loadTexts:
    uxsLoad1Critical.setStatus(
        ""
    )

uxsLoad5Unknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11050)
)
if mibBuilder.loadTexts:
    uxsLoad5Unknown.setStatus(
        ""
    )

uxsLoad5OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11051)
)
if mibBuilder.loadTexts:
    uxsLoad5OK.setStatus(
        ""
    )

uxsLoad5Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11052)
)
if mibBuilder.loadTexts:
    uxsLoad5Warning.setStatus(
        ""
    )

uxsLoad5Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11053)
)
if mibBuilder.loadTexts:
    uxsLoad5Critical.setStatus(
        ""
    )

uxsLoad15Unknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11150)
)
if mibBuilder.loadTexts:
    uxsLoad15Unknown.setStatus(
        ""
    )

uxsLoad15OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11151)
)
if mibBuilder.loadTexts:
    uxsLoad15OK.setStatus(
        ""
    )

uxsLoad15Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11152)
)
if mibBuilder.loadTexts:
    uxsLoad15Warning.setStatus(
        ""
    )

uxsLoad15Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 11153)
)
if mibBuilder.loadTexts:
    uxsLoad15Critical.setStatus(
        ""
    )

uxsMemUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 12010)
)
if mibBuilder.loadTexts:
    uxsMemUnknown.setStatus(
        ""
    )

uxsMemOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 12011)
)
if mibBuilder.loadTexts:
    uxsMemOK.setStatus(
        ""
    )

uxsMemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 12012)
)
if mibBuilder.loadTexts:
    uxsMemWarning.setStatus(
        ""
    )

uxsMemCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 12013)
)
if mibBuilder.loadTexts:
    uxsMemCritical.setStatus(
        ""
    )

uxsSwapTotalUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13000)
)
if mibBuilder.loadTexts:
    uxsSwapTotalUnknown.setStatus(
        ""
    )

uxsSwapTotalOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13001)
)
if mibBuilder.loadTexts:
    uxsSwapTotalOK.setStatus(
        ""
    )

uxsSwapTotalWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13002)
)
if mibBuilder.loadTexts:
    uxsSwapTotalWarning.setStatus(
        ""
    )

uxsSwapTotalCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13003)
)
if mibBuilder.loadTexts:
    uxsSwapTotalCritical.setStatus(
        ""
    )

uxsSwapUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13990)
)
if mibBuilder.loadTexts:
    uxsSwapUnknown.setStatus(
        ""
    )

uxsSwapOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13991)
)
if mibBuilder.loadTexts:
    uxsSwapOK.setStatus(
        ""
    )

uxsSwapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13992)
)
if mibBuilder.loadTexts:
    uxsSwapWarning.setStatus(
        ""
    )

uxsSwapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13993)
)
if mibBuilder.loadTexts:
    uxsSwapCritical.setStatus(
        ""
    )

uxsSwapDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13995)
)
if mibBuilder.loadTexts:
    uxsSwapDown.setStatus(
        ""
    )

uxsSwapAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13996)
)
if mibBuilder.loadTexts:
    uxsSwapAdded.setStatus(
        ""
    )

uxsSwapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 13997)
)
if mibBuilder.loadTexts:
    uxsSwapDeleted.setStatus(
        ""
    )

uxsFSysUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14980)
)
if mibBuilder.loadTexts:
    uxsFSysUnknown.setStatus(
        ""
    )

uxsFSysOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14981)
)
if mibBuilder.loadTexts:
    uxsFSysOK.setStatus(
        ""
    )

uxsFSysWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14982)
)
if mibBuilder.loadTexts:
    uxsFSysWarning.setStatus(
        ""
    )

uxsFSysCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14983)
)
if mibBuilder.loadTexts:
    uxsFSysCritical.setStatus(
        ""
    )

uxsFSysDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14985)
)
if mibBuilder.loadTexts:
    uxsFSysDown.setStatus(
        ""
    )

uxsFSysAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14986)
)
if mibBuilder.loadTexts:
    uxsFSysAdded.setStatus(
        ""
    )

uxsFSysDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 14987)
)
if mibBuilder.loadTexts:
    uxsFSysDeleted.setStatus(
        ""
    )

uxsDiskUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15980)
)
if mibBuilder.loadTexts:
    uxsDiskUnknown.setStatus(
        ""
    )

uxsDiskOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15981)
)
if mibBuilder.loadTexts:
    uxsDiskOK.setStatus(
        ""
    )

uxsDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15982)
)
if mibBuilder.loadTexts:
    uxsDiskWarning.setStatus(
        ""
    )

uxsDiskCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15983)
)
if mibBuilder.loadTexts:
    uxsDiskCritical.setStatus(
        ""
    )

uxsDiskDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15985)
)
if mibBuilder.loadTexts:
    uxsDiskDown.setStatus(
        ""
    )

uxsDiskAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15986)
)
if mibBuilder.loadTexts:
    uxsDiskAdded.setStatus(
        ""
    )

uxsDiskDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 15987)
)
if mibBuilder.loadTexts:
    uxsDiskDeleted.setStatus(
        ""
    )

uxsProcUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16980)
)
if mibBuilder.loadTexts:
    uxsProcUnknown.setStatus(
        ""
    )

uxsProcOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16981)
)
if mibBuilder.loadTexts:
    uxsProcOK.setStatus(
        ""
    )

uxsProcWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16982)
)
if mibBuilder.loadTexts:
    uxsProcWarning.setStatus(
        ""
    )

uxsProcCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16983)
)
if mibBuilder.loadTexts:
    uxsProcCritical.setStatus(
        ""
    )

uxsProcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16985)
)
if mibBuilder.loadTexts:
    uxsProcDown.setStatus(
        ""
    )

uxsProcAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16986)
)
if mibBuilder.loadTexts:
    uxsProcAdded.setStatus(
        ""
    )

uxsProcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 16987)
)
if mibBuilder.loadTexts:
    uxsProcDeleted.setStatus(
        ""
    )

uxsFilesUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17980)
)
if mibBuilder.loadTexts:
    uxsFilesUnknown.setStatus(
        ""
    )

uxsFilesOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17981)
)
if mibBuilder.loadTexts:
    uxsFilesOK.setStatus(
        ""
    )

uxsFilesWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17982)
)
if mibBuilder.loadTexts:
    uxsFilesWarning.setStatus(
        ""
    )

uxsFilesCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17983)
)
if mibBuilder.loadTexts:
    uxsFilesCritical.setStatus(
        ""
    )

uxsFilesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17985)
)
if mibBuilder.loadTexts:
    uxsFilesDown.setStatus(
        ""
    )

uxsFilesAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17986)
)
if mibBuilder.loadTexts:
    uxsFilesAdded.setStatus(
        ""
    )

uxsFilesDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 17987)
)
if mibBuilder.loadTexts:
    uxsFilesDeleted.setStatus(
        ""
    )

uxsPrnUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18980)
)
if mibBuilder.loadTexts:
    uxsPrnUnknown.setStatus(
        ""
    )

uxsPrnOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18981)
)
if mibBuilder.loadTexts:
    uxsPrnOK.setStatus(
        ""
    )

uxsPrnWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18982)
)
if mibBuilder.loadTexts:
    uxsPrnWarning.setStatus(
        ""
    )

uxsPrnCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18983)
)
if mibBuilder.loadTexts:
    uxsPrnCritical.setStatus(
        ""
    )

uxsPrnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18985)
)
if mibBuilder.loadTexts:
    uxsPrnDown.setStatus(
        ""
    )

uxsPrnAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18986)
)
if mibBuilder.loadTexts:
    uxsPrnAdded.setStatus(
        ""
    )

uxsPrnDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 18987)
)
if mibBuilder.loadTexts:
    uxsPrnDeleted.setStatus(
        ""
    )

uxsNetTotalUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19000)
)
if mibBuilder.loadTexts:
    uxsNetTotalUnknown.setStatus(
        ""
    )

uxsNetTotalOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19001)
)
if mibBuilder.loadTexts:
    uxsNetTotalOK.setStatus(
        ""
    )

uxsNetTotalWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19002)
)
if mibBuilder.loadTexts:
    uxsNetTotalWarning.setStatus(
        ""
    )

uxsNetTotalCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19003)
)
if mibBuilder.loadTexts:
    uxsNetTotalCritical.setStatus(
        ""
    )

uxsNetUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19990)
)
if mibBuilder.loadTexts:
    uxsNetUnknown.setStatus(
        ""
    )

uxsNetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19991)
)
if mibBuilder.loadTexts:
    uxsNetOK.setStatus(
        ""
    )

uxsNetWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19992)
)
if mibBuilder.loadTexts:
    uxsNetWarning.setStatus(
        ""
    )

uxsNetCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19993)
)
if mibBuilder.loadTexts:
    uxsNetCritical.setStatus(
        ""
    )

uxsNetDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19995)
)
if mibBuilder.loadTexts:
    uxsNetDown.setStatus(
        ""
    )

uxsNetAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19996)
)
if mibBuilder.loadTexts:
    uxsNetAdded.setStatus(
        ""
    )

uxsNetDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 19997)
)
if mibBuilder.loadTexts:
    uxsNetDeleted.setStatus(
        ""
    )

uxsIPCSHMUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20010)
)
if mibBuilder.loadTexts:
    uxsIPCSHMUnknown.setStatus(
        ""
    )

uxsIPCSHMOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20011)
)
if mibBuilder.loadTexts:
    uxsIPCSHMOK.setStatus(
        ""
    )

uxsIPCSHMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20012)
)
if mibBuilder.loadTexts:
    uxsIPCSHMWarning.setStatus(
        ""
    )

uxsIPCSHMCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20013)
)
if mibBuilder.loadTexts:
    uxsIPCSHMCritical.setStatus(
        ""
    )

uxsIPCSEMUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20020)
)
if mibBuilder.loadTexts:
    uxsIPCSEMUnknown.setStatus(
        ""
    )

uxsIPCSEMOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20021)
)
if mibBuilder.loadTexts:
    uxsIPCSEMOK.setStatus(
        ""
    )

uxsIPCSEMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20022)
)
if mibBuilder.loadTexts:
    uxsIPCSEMWarning.setStatus(
        ""
    )

uxsIPCSEMCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20023)
)
if mibBuilder.loadTexts:
    uxsIPCSEMCritical.setStatus(
        ""
    )

uxsIPCMQUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20030)
)
if mibBuilder.loadTexts:
    uxsIPCMQUnknown.setStatus(
        ""
    )

uxsIPCMQOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20031)
)
if mibBuilder.loadTexts:
    uxsIPCMQOK.setStatus(
        ""
    )

uxsIPCMQWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20032)
)
if mibBuilder.loadTexts:
    uxsIPCMQWarning.setStatus(
        ""
    )

uxsIPCMQCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20033)
)
if mibBuilder.loadTexts:
    uxsIPCMQCritical.setStatus(
        ""
    )

uxsIPCMQSUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20980)
)
if mibBuilder.loadTexts:
    uxsIPCMQSUnknown.setStatus(
        ""
    )

uxsIPCMQSOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20981)
)
if mibBuilder.loadTexts:
    uxsIPCMQSOK.setStatus(
        ""
    )

uxsIPCMQSWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20982)
)
if mibBuilder.loadTexts:
    uxsIPCMQSWarning.setStatus(
        ""
    )

uxsIPCMQSCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20983)
)
if mibBuilder.loadTexts:
    uxsIPCMQSCritical.setStatus(
        ""
    )

uxsIPCMQSDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20985)
)
if mibBuilder.loadTexts:
    uxsIPCMQSDown.setStatus(
        ""
    )

uxsIPCMQSAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20986)
)
if mibBuilder.loadTexts:
    uxsIPCMQSAdded.setStatus(
        ""
    )

uxsIPCMQSDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 4, 5, 0, 20987)
)
if mibBuilder.loadTexts:
    uxsIPCMQSDeleted.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAIUXOS",
    **{"cai": cai,
       "caiSysMgr": caiSysMgr,
       "agentWorks": agentWorks,
       "unix": unix,
       "caiUxOs": caiUxOs,
       "uxsCPUTotalUnknown": uxsCPUTotalUnknown,
       "uxsCPUTotalOK": uxsCPUTotalOK,
       "uxsCPUTotalWarning": uxsCPUTotalWarning,
       "uxsCPUTotalCritical": uxsCPUTotalCritical,
       "uxsCPUUnknown": uxsCPUUnknown,
       "uxsCPUOK": uxsCPUOK,
       "uxsCPUWarning": uxsCPUWarning,
       "uxsCPUCritical": uxsCPUCritical,
       "uxsCPUDown": uxsCPUDown,
       "uxsCPUAdded": uxsCPUAdded,
       "uxsCPUDeleted": uxsCPUDeleted,
       "uxsLoad1Unknown": uxsLoad1Unknown,
       "uxsLoad1OK": uxsLoad1OK,
       "uxsLoad1Warning": uxsLoad1Warning,
       "uxsLoad1Critical": uxsLoad1Critical,
       "uxsLoad5Unknown": uxsLoad5Unknown,
       "uxsLoad5OK": uxsLoad5OK,
       "uxsLoad5Warning": uxsLoad5Warning,
       "uxsLoad5Critical": uxsLoad5Critical,
       "uxsLoad15Unknown": uxsLoad15Unknown,
       "uxsLoad15OK": uxsLoad15OK,
       "uxsLoad15Warning": uxsLoad15Warning,
       "uxsLoad15Critical": uxsLoad15Critical,
       "uxsMemUnknown": uxsMemUnknown,
       "uxsMemOK": uxsMemOK,
       "uxsMemWarning": uxsMemWarning,
       "uxsMemCritical": uxsMemCritical,
       "uxsSwapTotalUnknown": uxsSwapTotalUnknown,
       "uxsSwapTotalOK": uxsSwapTotalOK,
       "uxsSwapTotalWarning": uxsSwapTotalWarning,
       "uxsSwapTotalCritical": uxsSwapTotalCritical,
       "uxsSwapUnknown": uxsSwapUnknown,
       "uxsSwapOK": uxsSwapOK,
       "uxsSwapWarning": uxsSwapWarning,
       "uxsSwapCritical": uxsSwapCritical,
       "uxsSwapDown": uxsSwapDown,
       "uxsSwapAdded": uxsSwapAdded,
       "uxsSwapDeleted": uxsSwapDeleted,
       "uxsFSysUnknown": uxsFSysUnknown,
       "uxsFSysOK": uxsFSysOK,
       "uxsFSysWarning": uxsFSysWarning,
       "uxsFSysCritical": uxsFSysCritical,
       "uxsFSysDown": uxsFSysDown,
       "uxsFSysAdded": uxsFSysAdded,
       "uxsFSysDeleted": uxsFSysDeleted,
       "uxsDiskUnknown": uxsDiskUnknown,
       "uxsDiskOK": uxsDiskOK,
       "uxsDiskWarning": uxsDiskWarning,
       "uxsDiskCritical": uxsDiskCritical,
       "uxsDiskDown": uxsDiskDown,
       "uxsDiskAdded": uxsDiskAdded,
       "uxsDiskDeleted": uxsDiskDeleted,
       "uxsProcUnknown": uxsProcUnknown,
       "uxsProcOK": uxsProcOK,
       "uxsProcWarning": uxsProcWarning,
       "uxsProcCritical": uxsProcCritical,
       "uxsProcDown": uxsProcDown,
       "uxsProcAdded": uxsProcAdded,
       "uxsProcDeleted": uxsProcDeleted,
       "uxsFilesUnknown": uxsFilesUnknown,
       "uxsFilesOK": uxsFilesOK,
       "uxsFilesWarning": uxsFilesWarning,
       "uxsFilesCritical": uxsFilesCritical,
       "uxsFilesDown": uxsFilesDown,
       "uxsFilesAdded": uxsFilesAdded,
       "uxsFilesDeleted": uxsFilesDeleted,
       "uxsPrnUnknown": uxsPrnUnknown,
       "uxsPrnOK": uxsPrnOK,
       "uxsPrnWarning": uxsPrnWarning,
       "uxsPrnCritical": uxsPrnCritical,
       "uxsPrnDown": uxsPrnDown,
       "uxsPrnAdded": uxsPrnAdded,
       "uxsPrnDeleted": uxsPrnDeleted,
       "uxsNetTotalUnknown": uxsNetTotalUnknown,
       "uxsNetTotalOK": uxsNetTotalOK,
       "uxsNetTotalWarning": uxsNetTotalWarning,
       "uxsNetTotalCritical": uxsNetTotalCritical,
       "uxsNetUnknown": uxsNetUnknown,
       "uxsNetOK": uxsNetOK,
       "uxsNetWarning": uxsNetWarning,
       "uxsNetCritical": uxsNetCritical,
       "uxsNetDown": uxsNetDown,
       "uxsNetAdded": uxsNetAdded,
       "uxsNetDeleted": uxsNetDeleted,
       "uxsIPCSHMUnknown": uxsIPCSHMUnknown,
       "uxsIPCSHMOK": uxsIPCSHMOK,
       "uxsIPCSHMWarning": uxsIPCSHMWarning,
       "uxsIPCSHMCritical": uxsIPCSHMCritical,
       "uxsIPCSEMUnknown": uxsIPCSEMUnknown,
       "uxsIPCSEMOK": uxsIPCSEMOK,
       "uxsIPCSEMWarning": uxsIPCSEMWarning,
       "uxsIPCSEMCritical": uxsIPCSEMCritical,
       "uxsIPCMQUnknown": uxsIPCMQUnknown,
       "uxsIPCMQOK": uxsIPCMQOK,
       "uxsIPCMQWarning": uxsIPCMQWarning,
       "uxsIPCMQCritical": uxsIPCMQCritical,
       "uxsIPCMQSUnknown": uxsIPCMQSUnknown,
       "uxsIPCMQSOK": uxsIPCMQSOK,
       "uxsIPCMQSWarning": uxsIPCMQSWarning,
       "uxsIPCMQSCritical": uxsIPCMQSCritical,
       "uxsIPCMQSDown": uxsIPCMQSDown,
       "uxsIPCMQSAdded": uxsIPCMQSAdded,
       "uxsIPCMQSDeleted": uxsIPCMQSDeleted,
       "uxsConfigGroup": uxsConfigGroup,
       "uxsConfigGeneralGroup": uxsConfigGeneralGroup,
       "uxsConfigGeneralAgentVersion": uxsConfigGeneralAgentVersion,
       "uxsConfigGeneralColdStartTime": uxsConfigGeneralColdStartTime,
       "uxsConfigGeneralWarmStartTime": uxsConfigGeneralWarmStartTime,
       "uxsConfigGeneralCPUPollTime": uxsConfigGeneralCPUPollTime,
       "uxsConfigGeneralLoadPollTime": uxsConfigGeneralLoadPollTime,
       "uxsConfigGeneralMemPollTime": uxsConfigGeneralMemPollTime,
       "uxsConfigGeneralSwapPollTime": uxsConfigGeneralSwapPollTime,
       "uxsConfigGeneralFSysPollTime": uxsConfigGeneralFSysPollTime,
       "uxsConfigGeneralDiskPollTime": uxsConfigGeneralDiskPollTime,
       "uxsConfigGeneralFilePollTime": uxsConfigGeneralFilePollTime,
       "uxsConfigGeneralProcPollTime": uxsConfigGeneralProcPollTime,
       "uxsConfigGeneralPrnPollTime": uxsConfigGeneralPrnPollTime,
       "uxsConfigGeneralNetPollTime": uxsConfigGeneralNetPollTime,
       "uxsConfigGeneralIPCPollTime": uxsConfigGeneralIPCPollTime,
       "uxsConfigSysGroup": uxsConfigSysGroup,
       "uxsConfigSysNodeName": uxsConfigSysNodeName,
       "uxsConfigSysSystemName": uxsConfigSysSystemName,
       "uxsConfigSysRelease": uxsConfigSysRelease,
       "uxsConfigSysVersion": uxsConfigSysVersion,
       "uxsConfigSysHardware": uxsConfigSysHardware,
       "uxsConfigSysBootTime": uxsConfigSysBootTime,
       "uxsConfigSysRunLevel": uxsConfigSysRunLevel,
       "uxsConfigCPUGroup": uxsConfigCPUGroup,
       "uxsConfigCPUPollInterval": uxsConfigCPUPollInterval,
       "uxsConfigCPUPollMethod": uxsConfigCPUPollMethod,
       "uxsConfigCPULag": uxsConfigCPULag,
       "uxsConfigCPUWarn": uxsConfigCPUWarn,
       "uxsConfigCPUCrit": uxsConfigCPUCrit,
       "uxsConfigCPUMonitor": uxsConfigCPUMonitor,
       "uxsConfigCPULossAction": uxsConfigCPULossAction,
       "uxsConfigLoadGroup": uxsConfigLoadGroup,
       "uxsConfigLoadPollInterval": uxsConfigLoadPollInterval,
       "uxsConfigLoadPollMethod": uxsConfigLoadPollMethod,
       "uxsConfigMemGroup": uxsConfigMemGroup,
       "uxsConfigMemPollInterval": uxsConfigMemPollInterval,
       "uxsConfigMemPollMethod": uxsConfigMemPollMethod,
       "uxsConfigSwapGroup": uxsConfigSwapGroup,
       "uxsConfigSwapPollInterval": uxsConfigSwapPollInterval,
       "uxsConfigSwapPollMethod": uxsConfigSwapPollMethod,
       "uxsConfigSwapLag": uxsConfigSwapLag,
       "uxsConfigSwapWarn": uxsConfigSwapWarn,
       "uxsConfigSwapCrit": uxsConfigSwapCrit,
       "uxsConfigSwapMonitor": uxsConfigSwapMonitor,
       "uxsConfigSwapLossAction": uxsConfigSwapLossAction,
       "uxsConfigFSysGroup": uxsConfigFSysGroup,
       "uxsConfigFSysPollInterval": uxsConfigFSysPollInterval,
       "uxsConfigFSysPollMethod": uxsConfigFSysPollMethod,
       "uxsConfigFSysSpaceWarn": uxsConfigFSysSpaceWarn,
       "uxsConfigFSysSpaceCrit": uxsConfigFSysSpaceCrit,
       "uxsConfigFSysSpaceMonitor": uxsConfigFSysSpaceMonitor,
       "uxsConfigFSysSpaceDWarn": uxsConfigFSysSpaceDWarn,
       "uxsConfigFSysSpaceDCrit": uxsConfigFSysSpaceDCrit,
       "uxsConfigFSysSpaceDMonitor": uxsConfigFSysSpaceDMonitor,
       "uxsConfigFSysInodesWarn": uxsConfigFSysInodesWarn,
       "uxsConfigFSysInodesCrit": uxsConfigFSysInodesCrit,
       "uxsConfigFSysInodesMonitor": uxsConfigFSysInodesMonitor,
       "uxsConfigFSysInodesDWarn": uxsConfigFSysInodesDWarn,
       "uxsConfigFSysInodesDCrit": uxsConfigFSysInodesDCrit,
       "uxsConfigFSysInodesDMonitor": uxsConfigFSysInodesDMonitor,
       "uxsConfigFSysMountedMonitor": uxsConfigFSysMountedMonitor,
       "uxsConfigFSysLossAction": uxsConfigFSysLossAction,
       "uxsConfigFSysNameAdd": uxsConfigFSysNameAdd,
       "uxsConfigFSysNameRemove": uxsConfigFSysNameRemove,
       "uxsConfigDiskGroup": uxsConfigDiskGroup,
       "uxsConfigDiskPollInterval": uxsConfigDiskPollInterval,
       "uxsConfigDiskPollMethod": uxsConfigDiskPollMethod,
       "uxsConfigDiskTPutWarn": uxsConfigDiskTPutWarn,
       "uxsConfigDiskTPutCrit": uxsConfigDiskTPutCrit,
       "uxsConfigDiskTPutMonitor": uxsConfigDiskTPutMonitor,
       "uxsConfigDiskLossAction": uxsConfigDiskLossAction,
       "uxsConfigDiskNameAdd": uxsConfigDiskNameAdd,
       "uxsConfigDiskNameRemove": uxsConfigDiskNameRemove,
       "uxsConfigFileGroup": uxsConfigFileGroup,
       "uxsConfigFilePollInterval": uxsConfigFilePollInterval,
       "uxsConfigFilePollMethod": uxsConfigFilePollMethod,
       "uxsConfigFileDesc": uxsConfigFileDesc,
       "uxsConfigFileExist": uxsConfigFileExist,
       "uxsConfigFileExistMonitor": uxsConfigFileExistMonitor,
       "uxsConfigFileModTimeMonitor": uxsConfigFileModTimeMonitor,
       "uxsConfigFileSizeWarn": uxsConfigFileSizeWarn,
       "uxsConfigFileSizeCrit": uxsConfigFileSizeCrit,
       "uxsConfigFileSizeMonitor": uxsConfigFileSizeMonitor,
       "uxsConfigFileSizeDWarn": uxsConfigFileSizeDWarn,
       "uxsConfigFileSizeDCrit": uxsConfigFileSizeDCrit,
       "uxsConfigFileSizeDMonitor": uxsConfigFileSizeDMonitor,
       "uxsConfigFileNameAdd": uxsConfigFileNameAdd,
       "uxsConfigFileNameRemove": uxsConfigFileNameRemove,
       "uxsConfigProcGroup": uxsConfigProcGroup,
       "uxsConfigProcPollInterval": uxsConfigProcPollInterval,
       "uxsConfigProcPollMethod": uxsConfigProcPollMethod,
       "uxsConfigProcPath": uxsConfigProcPath,
       "uxsConfigProcArgs": uxsConfigProcArgs,
       "uxsConfigProcUsers": uxsConfigProcUsers,
       "uxsConfigProcInstMin": uxsConfigProcInstMin,
       "uxsConfigProcInstMax": uxsConfigProcInstMax,
       "uxsConfigProcInstMonitor": uxsConfigProcInstMonitor,
       "uxsConfigProcChldMin": uxsConfigProcChldMin,
       "uxsConfigProcChldMax": uxsConfigProcChldMax,
       "uxsConfigProcChldMonitor": uxsConfigProcChldMonitor,
       "uxsConfigProcSizeMin": uxsConfigProcSizeMin,
       "uxsConfigProcSizeMax": uxsConfigProcSizeMax,
       "uxsConfigProcSizeMonitor": uxsConfigProcSizeMonitor,
       "uxsConfigProcCPUWarn": uxsConfigProcCPUWarn,
       "uxsConfigProcCPUCrit": uxsConfigProcCPUCrit,
       "uxsConfigProcCPUMonitor": uxsConfigProcCPUMonitor,
       "uxsConfigProcNameAdd": uxsConfigProcNameAdd,
       "uxsConfigProcNameRemove": uxsConfigProcNameRemove,
       "uxsConfigProcNameSig": uxsConfigProcNameSig,
       "uxsConfigProcPathSig": uxsConfigProcPathSig,
       "uxsConfigProcArgsSig": uxsConfigProcArgsSig,
       "uxsConfigPrnGroup": uxsConfigPrnGroup,
       "uxsConfigPrnPollInterval": uxsConfigPrnPollInterval,
       "uxsConfigPrnPollMethod": uxsConfigPrnPollMethod,
       "uxsConfigPrnDesc": uxsConfigPrnDesc,
       "uxsConfigPrnItemsWarn": uxsConfigPrnItemsWarn,
       "uxsConfigPrnItemsCrit": uxsConfigPrnItemsCrit,
       "uxsConfigPrnItemsMonitor": uxsConfigPrnItemsMonitor,
       "uxsConfigPrnLossAction": uxsConfigPrnLossAction,
       "uxsConfigPrnNameAdd": uxsConfigPrnNameAdd,
       "uxsConfigPrnNameRemove": uxsConfigPrnNameRemove,
       "uxsConfigNetGroup": uxsConfigNetGroup,
       "uxsConfigNetPollInterval": uxsConfigNetPollInterval,
       "uxsConfigNetPollMethod": uxsConfigNetPollMethod,
       "uxsConfigNetIPktWarn": uxsConfigNetIPktWarn,
       "uxsConfigNetIPktCrit": uxsConfigNetIPktCrit,
       "uxsConfigNetIPktMonitor": uxsConfigNetIPktMonitor,
       "uxsConfigNetIErrWarn": uxsConfigNetIErrWarn,
       "uxsConfigNetIErrCrit": uxsConfigNetIErrCrit,
       "uxsConfigNetIErrMonitor": uxsConfigNetIErrMonitor,
       "uxsConfigNetOPktWarn": uxsConfigNetOPktWarn,
       "uxsConfigNetOPktCrit": uxsConfigNetOPktCrit,
       "uxsConfigNetOPktMonitor": uxsConfigNetOPktMonitor,
       "uxsConfigNetOErrWarn": uxsConfigNetOErrWarn,
       "uxsConfigNetOErrCrit": uxsConfigNetOErrCrit,
       "uxsConfigNetOErrMonitor": uxsConfigNetOErrMonitor,
       "uxsConfigNetCollWarn": uxsConfigNetCollWarn,
       "uxsConfigNetCollCrit": uxsConfigNetCollCrit,
       "uxsConfigNetCollMonitor": uxsConfigNetCollMonitor,
       "uxsConfigNetLossAction": uxsConfigNetLossAction,
       "uxsConfigIPCGroup": uxsConfigIPCGroup,
       "uxsConfigIPCPollInterval": uxsConfigIPCPollInterval,
       "uxsConfigIPCPollMethod": uxsConfigIPCPollMethod,
       "uxsConfigIPCMQBytesLag": uxsConfigIPCMQBytesLag,
       "uxsConfigIPCMQBytesWarn": uxsConfigIPCMQBytesWarn,
       "uxsConfigIPCMQBytesCrit": uxsConfigIPCMQBytesCrit,
       "uxsConfigIPCMQBytesMonitor": uxsConfigIPCMQBytesMonitor,
       "uxsStatusGroup": uxsStatusGroup,
       "uxsStatusGeneralGroup": uxsStatusGeneralGroup,
       "uxsStatusGeneralTotalCount": uxsStatusGeneralTotalCount,
       "uxsStatusGeneralTotalWarning": uxsStatusGeneralTotalWarning,
       "uxsStatusGeneralTotalCritical": uxsStatusGeneralTotalCritical,
       "uxsStatusGeneralCPUCount": uxsStatusGeneralCPUCount,
       "uxsStatusGeneralCPUWarning": uxsStatusGeneralCPUWarning,
       "uxsStatusGeneralCPUCritical": uxsStatusGeneralCPUCritical,
       "uxsStatusGeneralLoadCount": uxsStatusGeneralLoadCount,
       "uxsStatusGeneralLoadWarning": uxsStatusGeneralLoadWarning,
       "uxsStatusGeneralLoadCritical": uxsStatusGeneralLoadCritical,
       "uxsStatusGeneralMemCount": uxsStatusGeneralMemCount,
       "uxsStatusGeneralMemWarning": uxsStatusGeneralMemWarning,
       "uxsStatusGeneralMemCritical": uxsStatusGeneralMemCritical,
       "uxsStatusGeneralSwapCount": uxsStatusGeneralSwapCount,
       "uxsStatusGeneralSwapWarning": uxsStatusGeneralSwapWarning,
       "uxsStatusGeneralSwapCritical": uxsStatusGeneralSwapCritical,
       "uxsStatusGeneralFSysCount": uxsStatusGeneralFSysCount,
       "uxsStatusGeneralFSysWarning": uxsStatusGeneralFSysWarning,
       "uxsStatusGeneralFSysCritical": uxsStatusGeneralFSysCritical,
       "uxsStatusGeneralDiskCount": uxsStatusGeneralDiskCount,
       "uxsStatusGeneralDiskWarning": uxsStatusGeneralDiskWarning,
       "uxsStatusGeneralDiskCritical": uxsStatusGeneralDiskCritical,
       "uxsStatusGeneralFileCount": uxsStatusGeneralFileCount,
       "uxsStatusGeneralFileWarning": uxsStatusGeneralFileWarning,
       "uxsStatusGeneralFileCritical": uxsStatusGeneralFileCritical,
       "uxsStatusGeneralProcCount": uxsStatusGeneralProcCount,
       "uxsStatusGeneralProcWarning": uxsStatusGeneralProcWarning,
       "uxsStatusGeneralProcCritical": uxsStatusGeneralProcCritical,
       "uxsStatusGeneralPrnCount": uxsStatusGeneralPrnCount,
       "uxsStatusGeneralPrnWarning": uxsStatusGeneralPrnWarning,
       "uxsStatusGeneralPrnCritical": uxsStatusGeneralPrnCritical,
       "uxsStatusGeneralNetCount": uxsStatusGeneralNetCount,
       "uxsStatusGeneralNetWarning": uxsStatusGeneralNetWarning,
       "uxsStatusGeneralNetCritical": uxsStatusGeneralNetCritical,
       "uxsStatusGeneralIPCCount": uxsStatusGeneralIPCCount,
       "uxsStatusGeneralIPCWarning": uxsStatusGeneralIPCWarning,
       "uxsStatusGeneralIPCCritical": uxsStatusGeneralIPCCritical,
       "uxsStatusCPUGroup": uxsStatusCPUGroup,
       "uxsStatusCPUTotalName": uxsStatusCPUTotalName,
       "uxsStatusCPUTotalUser": uxsStatusCPUTotalUser,
       "uxsStatusCPUTotalSys": uxsStatusCPUTotalSys,
       "uxsStatusCPUTotalIdle": uxsStatusCPUTotalIdle,
       "uxsStatusCPUTotalWIO": uxsStatusCPUTotalWIO,
       "uxsStatusCPUTotalUsedValue": uxsStatusCPUTotalUsedValue,
       "uxsStatusCPUTotalLagValue": uxsStatusCPUTotalLagValue,
       "uxsStatusCPUTotalLag": uxsStatusCPUTotalLag,
       "uxsStatusCPUTotalWarn": uxsStatusCPUTotalWarn,
       "uxsStatusCPUTotalCrit": uxsStatusCPUTotalCrit,
       "uxsStatusCPUTotalMonitor": uxsStatusCPUTotalMonitor,
       "uxsStatusCPUTotalStatus": uxsStatusCPUTotalStatus,
       "uxsStatusCPUCount": uxsStatusCPUCount,
       "uxsStatusCPUTable": uxsStatusCPUTable,
       "uxsStatusCPUEntry": uxsStatusCPUEntry,
       "uxsStatusCPUName": uxsStatusCPUName,
       "uxsStatusCPUUser": uxsStatusCPUUser,
       "uxsStatusCPUSys": uxsStatusCPUSys,
       "uxsStatusCPUIdle": uxsStatusCPUIdle,
       "uxsStatusCPUWIO": uxsStatusCPUWIO,
       "uxsStatusCPUAggStatus": uxsStatusCPUAggStatus,
       "uxsStatusCPUUsedValue": uxsStatusCPUUsedValue,
       "uxsStatusCPULagValue": uxsStatusCPULagValue,
       "uxsStatusCPULag": uxsStatusCPULag,
       "uxsStatusCPUWarn": uxsStatusCPUWarn,
       "uxsStatusCPUCrit": uxsStatusCPUCrit,
       "uxsStatusCPUMonitor": uxsStatusCPUMonitor,
       "uxsStatusCPUStatus": uxsStatusCPUStatus,
       "uxsStatusCPULossAction": uxsStatusCPULossAction,
       "uxsStatusCPULossStatus": uxsStatusCPULossStatus,
       "uxsStatusLoadGroup": uxsStatusLoadGroup,
       "uxsStatusLoad1MinValue": uxsStatusLoad1MinValue,
       "uxsStatusLoad1MinWarn": uxsStatusLoad1MinWarn,
       "uxsStatusLoad1MinCrit": uxsStatusLoad1MinCrit,
       "uxsStatusLoad1MinMonitor": uxsStatusLoad1MinMonitor,
       "uxsStatusLoad1MinStatus": uxsStatusLoad1MinStatus,
       "uxsStatusLoad5MinValue": uxsStatusLoad5MinValue,
       "uxsStatusLoad5MinWarn": uxsStatusLoad5MinWarn,
       "uxsStatusLoad5MinCrit": uxsStatusLoad5MinCrit,
       "uxsStatusLoad5MinMonitor": uxsStatusLoad5MinMonitor,
       "uxsStatusLoad5MinStatus": uxsStatusLoad5MinStatus,
       "uxsStatusLoad15MinValue": uxsStatusLoad15MinValue,
       "uxsStatusLoad15MinWarn": uxsStatusLoad15MinWarn,
       "uxsStatusLoad15MinCrit": uxsStatusLoad15MinCrit,
       "uxsStatusLoad15MinMonitor": uxsStatusLoad15MinMonitor,
       "uxsStatusLoad15MinStatus": uxsStatusLoad15MinStatus,
       "uxsStatusMemGroup": uxsStatusMemGroup,
       "uxsStatusMemTotal": uxsStatusMemTotal,
       "uxsStatusMemValue": uxsStatusMemValue,
       "uxsStatusMemLagValue": uxsStatusMemLagValue,
       "uxsStatusMemLag": uxsStatusMemLag,
       "uxsStatusMemWarnValue": uxsStatusMemWarnValue,
       "uxsStatusMemCritValue": uxsStatusMemCritValue,
       "uxsStatusMemWarn": uxsStatusMemWarn,
       "uxsStatusMemCrit": uxsStatusMemCrit,
       "uxsStatusMemMonitor": uxsStatusMemMonitor,
       "uxsStatusMemStatus": uxsStatusMemStatus,
       "uxsStatusSwapGroup": uxsStatusSwapGroup,
       "uxsStatusSwapTotalName": uxsStatusSwapTotalName,
       "uxsStatusSwapTotalAvailable": uxsStatusSwapTotalAvailable,
       "uxsStatusSwapTotalUsedValue": uxsStatusSwapTotalUsedValue,
       "uxsStatusSwapTotalLagValue": uxsStatusSwapTotalLagValue,
       "uxsStatusSwapTotalLag": uxsStatusSwapTotalLag,
       "uxsStatusSwapTotalWarnValue": uxsStatusSwapTotalWarnValue,
       "uxsStatusSwapTotalCritValue": uxsStatusSwapTotalCritValue,
       "uxsStatusSwapTotalWarn": uxsStatusSwapTotalWarn,
       "uxsStatusSwapTotalCrit": uxsStatusSwapTotalCrit,
       "uxsStatusSwapTotalMonitor": uxsStatusSwapTotalMonitor,
       "uxsStatusSwapTotalStatus": uxsStatusSwapTotalStatus,
       "uxsStatusSwapCount": uxsStatusSwapCount,
       "uxsStatusSwapTable": uxsStatusSwapTable,
       "uxsStatusSwapEntry": uxsStatusSwapEntry,
       "uxsStatusSwapName": uxsStatusSwapName,
       "uxsStatusSwapAggStatus": uxsStatusSwapAggStatus,
       "uxsStatusSwapAvailable": uxsStatusSwapAvailable,
       "uxsStatusSwapUsedValue": uxsStatusSwapUsedValue,
       "uxsStatusSwapLagValue": uxsStatusSwapLagValue,
       "uxsStatusSwapLag": uxsStatusSwapLag,
       "uxsStatusSwapWarnValue": uxsStatusSwapWarnValue,
       "uxsStatusSwapCritValue": uxsStatusSwapCritValue,
       "uxsStatusSwapWarn": uxsStatusSwapWarn,
       "uxsStatusSwapCrit": uxsStatusSwapCrit,
       "uxsStatusSwapMonitor": uxsStatusSwapMonitor,
       "uxsStatusSwapStatus": uxsStatusSwapStatus,
       "uxsStatusSwapLossAction": uxsStatusSwapLossAction,
       "uxsStatusSwapLossStatus": uxsStatusSwapLossStatus,
       "uxsStatusFSysGroup": uxsStatusFSysGroup,
       "uxsStatusFSysCount": uxsStatusFSysCount,
       "uxsStatusFSysTable": uxsStatusFSysTable,
       "uxsStatusFSysEntry": uxsStatusFSysEntry,
       "uxsStatusFSysName": uxsStatusFSysName,
       "uxsStatusFSysRelatedTo": uxsStatusFSysRelatedTo,
       "uxsStatusFSysType": uxsStatusFSysType,
       "uxsStatusFSysStatus": uxsStatusFSysStatus,
       "uxsStatusFSysSpaceTotal": uxsStatusFSysSpaceTotal,
       "uxsStatusFSysSpaceValue": uxsStatusFSysSpaceValue,
       "uxsStatusFSysSpaceWarnValue": uxsStatusFSysSpaceWarnValue,
       "uxsStatusFSysSpaceCritValue": uxsStatusFSysSpaceCritValue,
       "uxsStatusFSysSpaceWarn": uxsStatusFSysSpaceWarn,
       "uxsStatusFSysSpaceCrit": uxsStatusFSysSpaceCrit,
       "uxsStatusFSysSpaceMonitor": uxsStatusFSysSpaceMonitor,
       "uxsStatusFSysSpaceStatus": uxsStatusFSysSpaceStatus,
       "uxsStatusFSysSpaceDValue": uxsStatusFSysSpaceDValue,
       "uxsStatusFSysSpaceDWarnValue": uxsStatusFSysSpaceDWarnValue,
       "uxsStatusFSysSpaceDCritValue": uxsStatusFSysSpaceDCritValue,
       "uxsStatusFSysSpaceDWarn": uxsStatusFSysSpaceDWarn,
       "uxsStatusFSysSpaceDCrit": uxsStatusFSysSpaceDCrit,
       "uxsStatusFSysSpaceDMonitor": uxsStatusFSysSpaceDMonitor,
       "uxsStatusFSysSpaceDStatus": uxsStatusFSysSpaceDStatus,
       "uxsStatusFSysInodesTotal": uxsStatusFSysInodesTotal,
       "uxsStatusFSysInodesValue": uxsStatusFSysInodesValue,
       "uxsStatusFSysInodesWarnValue": uxsStatusFSysInodesWarnValue,
       "uxsStatusFSysInodesCritValue": uxsStatusFSysInodesCritValue,
       "uxsStatusFSysInodesWarn": uxsStatusFSysInodesWarn,
       "uxsStatusFSysInodesCrit": uxsStatusFSysInodesCrit,
       "uxsStatusFSysInodesMonitor": uxsStatusFSysInodesMonitor,
       "uxsStatusFSysInodesStatus": uxsStatusFSysInodesStatus,
       "uxsStatusFSysInodesDValue": uxsStatusFSysInodesDValue,
       "uxsStatusFSysInodesDWarnValue": uxsStatusFSysInodesDWarnValue,
       "uxsStatusFSysInodesDCritValue": uxsStatusFSysInodesDCritValue,
       "uxsStatusFSysInodesDWarn": uxsStatusFSysInodesDWarn,
       "uxsStatusFSysInodesDCrit": uxsStatusFSysInodesDCrit,
       "uxsStatusFSysInodesDMonitor": uxsStatusFSysInodesDMonitor,
       "uxsStatusFSysInodesDStatus": uxsStatusFSysInodesDStatus,
       "uxsStatusFSysMountedMonitor": uxsStatusFSysMountedMonitor,
       "uxsStatusFSysMountedStatus": uxsStatusFSysMountedStatus,
       "uxsStatusFSysLossAction": uxsStatusFSysLossAction,
       "uxsStatusFSysLossStatus": uxsStatusFSysLossStatus,
       "uxsStatusFSysRemove": uxsStatusFSysRemove,
       "uxsStatusDiskGroup": uxsStatusDiskGroup,
       "uxsStatusDiskCount": uxsStatusDiskCount,
       "uxsStatusDiskTable": uxsStatusDiskTable,
       "uxsStatusDiskEntry": uxsStatusDiskEntry,
       "uxsStatusDiskName": uxsStatusDiskName,
       "uxsStatusDiskAggStatus": uxsStatusDiskAggStatus,
       "uxsStatusDiskTPutValue": uxsStatusDiskTPutValue,
       "uxsStatusDiskTPutWarn": uxsStatusDiskTPutWarn,
       "uxsStatusDiskTPutCrit": uxsStatusDiskTPutCrit,
       "uxsStatusDiskTPutMonitor": uxsStatusDiskTPutMonitor,
       "uxsStatusDiskTPutStatus": uxsStatusDiskTPutStatus,
       "uxsStatusDiskLossAction": uxsStatusDiskLossAction,
       "uxsStatusDiskLossStatus": uxsStatusDiskLossStatus,
       "uxsStatusDiskRemove": uxsStatusDiskRemove,
       "uxsStatusFileGroup": uxsStatusFileGroup,
       "uxsStatusFileCount": uxsStatusFileCount,
       "uxsStatusFileTable": uxsStatusFileTable,
       "uxsStatusFileEntry": uxsStatusFileEntry,
       "uxsStatusFileName": uxsStatusFileName,
       "uxsStatusFileDesc": uxsStatusFileDesc,
       "uxsStatusFileStatus": uxsStatusFileStatus,
       "uxsStatusFileExist": uxsStatusFileExist,
       "uxsStatusFileExistMonitor": uxsStatusFileExistMonitor,
       "uxsStatusFileExistStatus": uxsStatusFileExistStatus,
       "uxsStatusFileModTime": uxsStatusFileModTime,
       "uxsStatusFileModTimeValue": uxsStatusFileModTimeValue,
       "uxsStatusFileModTimeMonitor": uxsStatusFileModTimeMonitor,
       "uxsStatusFileModTimeStatus": uxsStatusFileModTimeStatus,
       "uxsStatusFileSizeValue": uxsStatusFileSizeValue,
       "uxsStatusFileSizeWarn": uxsStatusFileSizeWarn,
       "uxsStatusFileSizeCrit": uxsStatusFileSizeCrit,
       "uxsStatusFileSizeMonitor": uxsStatusFileSizeMonitor,
       "uxsStatusFileSizeStatus": uxsStatusFileSizeStatus,
       "uxsStatusFileSizeDValue": uxsStatusFileSizeDValue,
       "uxsStatusFileSizeDWarn": uxsStatusFileSizeDWarn,
       "uxsStatusFileSizeDCrit": uxsStatusFileSizeDCrit,
       "uxsStatusFileSizeDMonitor": uxsStatusFileSizeDMonitor,
       "uxsStatusFileSizeDStatus": uxsStatusFileSizeDStatus,
       "uxsStatusFileRemove": uxsStatusFileRemove,
       "uxsStatusProcGroup": uxsStatusProcGroup,
       "uxsStatusProcCount": uxsStatusProcCount,
       "uxsStatusProcTable": uxsStatusProcTable,
       "uxsStatusProcEntry": uxsStatusProcEntry,
       "uxsStatusProcName": uxsStatusProcName,
       "uxsStatusProcPath": uxsStatusProcPath,
       "uxsStatusProcArgs": uxsStatusProcArgs,
       "uxsStatusProcUsers": uxsStatusProcUsers,
       "uxsStatusProcStatus": uxsStatusProcStatus,
       "uxsStatusProcPIDs": uxsStatusProcPIDs,
       "uxsStatusProcInstValue": uxsStatusProcInstValue,
       "uxsStatusProcInstMin": uxsStatusProcInstMin,
       "uxsStatusProcInstMax": uxsStatusProcInstMax,
       "uxsStatusProcInstMonitor": uxsStatusProcInstMonitor,
       "uxsStatusProcInstStatus": uxsStatusProcInstStatus,
       "uxsStatusProcChldValue": uxsStatusProcChldValue,
       "uxsStatusProcChldMin": uxsStatusProcChldMin,
       "uxsStatusProcChldMax": uxsStatusProcChldMax,
       "uxsStatusProcChldMonitor": uxsStatusProcChldMonitor,
       "uxsStatusProcChldStatus": uxsStatusProcChldStatus,
       "uxsStatusProcSizeValue": uxsStatusProcSizeValue,
       "uxsStatusProcSizeMin": uxsStatusProcSizeMin,
       "uxsStatusProcSizeMax": uxsStatusProcSizeMax,
       "uxsStatusProcSizeMonitor": uxsStatusProcSizeMonitor,
       "uxsStatusProcSizeStatus": uxsStatusProcSizeStatus,
       "uxsStatusProcCPUValue": uxsStatusProcCPUValue,
       "uxsStatusProcCPUWarn": uxsStatusProcCPUWarn,
       "uxsStatusProcCPUCrit": uxsStatusProcCPUCrit,
       "uxsStatusProcCPUMonitor": uxsStatusProcCPUMonitor,
       "uxsStatusProcCPUStatus": uxsStatusProcCPUStatus,
       "uxsStatusProcRemove": uxsStatusProcRemove,
       "uxsStatusPrnGroup": uxsStatusPrnGroup,
       "uxsStatusPrnCount": uxsStatusPrnCount,
       "uxsStatusPrnTable": uxsStatusPrnTable,
       "uxsStatusPrnEntry": uxsStatusPrnEntry,
       "uxsStatusPrnName": uxsStatusPrnName,
       "uxsStatusPrnAggStatus": uxsStatusPrnAggStatus,
       "uxsStatusPrnDesc": uxsStatusPrnDesc,
       "uxsStatusPrnItemsValue": uxsStatusPrnItemsValue,
       "uxsStatusPrnItemsWarn": uxsStatusPrnItemsWarn,
       "uxsStatusPrnItemsCrit": uxsStatusPrnItemsCrit,
       "uxsStatusPrnItemsMonitor": uxsStatusPrnItemsMonitor,
       "uxsStatusPrnItemsStatus": uxsStatusPrnItemsStatus,
       "uxsStatusPrnLossAction": uxsStatusPrnLossAction,
       "uxsStatusPrnLossStatus": uxsStatusPrnLossStatus,
       "uxsStatusPrnRemove": uxsStatusPrnRemove,
       "uxsStatusNetGroup": uxsStatusNetGroup,
       "uxsStatusNetTotalStatus": uxsStatusNetTotalStatus,
       "uxsStatusNetTotalIPktValue": uxsStatusNetTotalIPktValue,
       "uxsStatusNetTotalIPktWarn": uxsStatusNetTotalIPktWarn,
       "uxsStatusNetTotalIPktCrit": uxsStatusNetTotalIPktCrit,
       "uxsStatusNetTotalIPktMonitor": uxsStatusNetTotalIPktMonitor,
       "uxsStatusNetTotalIPktStatus": uxsStatusNetTotalIPktStatus,
       "uxsStatusNetTotalIErrValue": uxsStatusNetTotalIErrValue,
       "uxsStatusNetTotalIErrWarn": uxsStatusNetTotalIErrWarn,
       "uxsStatusNetTotalIErrCrit": uxsStatusNetTotalIErrCrit,
       "uxsStatusNetTotalIErrMonitor": uxsStatusNetTotalIErrMonitor,
       "uxsStatusNetTotalIErrStatus": uxsStatusNetTotalIErrStatus,
       "uxsStatusNetTotalOPktValue": uxsStatusNetTotalOPktValue,
       "uxsStatusNetTotalOPktWarn": uxsStatusNetTotalOPktWarn,
       "uxsStatusNetTotalOPktCrit": uxsStatusNetTotalOPktCrit,
       "uxsStatusNetTotalOPktMonitor": uxsStatusNetTotalOPktMonitor,
       "uxsStatusNetTotalOPktStatus": uxsStatusNetTotalOPktStatus,
       "uxsStatusNetTotalOErrValue": uxsStatusNetTotalOErrValue,
       "uxsStatusNetTotalOErrWarn": uxsStatusNetTotalOErrWarn,
       "uxsStatusNetTotalOErrCrit": uxsStatusNetTotalOErrCrit,
       "uxsStatusNetTotalOErrMonitor": uxsStatusNetTotalOErrMonitor,
       "uxsStatusNetTotalOErrStatus": uxsStatusNetTotalOErrStatus,
       "uxsStatusNetTotalCollValue": uxsStatusNetTotalCollValue,
       "uxsStatusNetTotalCollWarn": uxsStatusNetTotalCollWarn,
       "uxsStatusNetTotalCollCrit": uxsStatusNetTotalCollCrit,
       "uxsStatusNetTotalCollMonitor": uxsStatusNetTotalCollMonitor,
       "uxsStatusNetTotalCollStatus": uxsStatusNetTotalCollStatus,
       "uxsStatusNetCount": uxsStatusNetCount,
       "uxsStatusNetTable": uxsStatusNetTable,
       "uxsStatusNetEntry": uxsStatusNetEntry,
       "uxsStatusNetName": uxsStatusNetName,
       "uxsStatusNetIP": uxsStatusNetIP,
       "uxsStatusNetStatus": uxsStatusNetStatus,
       "uxsStatusNetIPktValue": uxsStatusNetIPktValue,
       "uxsStatusNetIPktWarn": uxsStatusNetIPktWarn,
       "uxsStatusNetIPktCrit": uxsStatusNetIPktCrit,
       "uxsStatusNetIPktMonitor": uxsStatusNetIPktMonitor,
       "uxsStatusNetIPktStatus": uxsStatusNetIPktStatus,
       "uxsStatusNetIErrValue": uxsStatusNetIErrValue,
       "uxsStatusNetIErrWarn": uxsStatusNetIErrWarn,
       "uxsStatusNetIErrCrit": uxsStatusNetIErrCrit,
       "uxsStatusNetIErrMonitor": uxsStatusNetIErrMonitor,
       "uxsStatusNetIErrStatus": uxsStatusNetIErrStatus,
       "uxsStatusNetOPktValue": uxsStatusNetOPktValue,
       "uxsStatusNetOPktWarn": uxsStatusNetOPktWarn,
       "uxsStatusNetOPktCrit": uxsStatusNetOPktCrit,
       "uxsStatusNetOPktMonitor": uxsStatusNetOPktMonitor,
       "uxsStatusNetOPktStatus": uxsStatusNetOPktStatus,
       "uxsStatusNetOErrValue": uxsStatusNetOErrValue,
       "uxsStatusNetOErrWarn": uxsStatusNetOErrWarn,
       "uxsStatusNetOErrCrit": uxsStatusNetOErrCrit,
       "uxsStatusNetOErrMonitor": uxsStatusNetOErrMonitor,
       "uxsStatusNetOErrStatus": uxsStatusNetOErrStatus,
       "uxsStatusNetCollValue": uxsStatusNetCollValue,
       "uxsStatusNetCollWarn": uxsStatusNetCollWarn,
       "uxsStatusNetCollCrit": uxsStatusNetCollCrit,
       "uxsStatusNetCollMonitor": uxsStatusNetCollMonitor,
       "uxsStatusNetCollStatus": uxsStatusNetCollStatus,
       "uxsStatusNetLossAction": uxsStatusNetLossAction,
       "uxsStatusNetLossStatus": uxsStatusNetLossStatus,
       "uxsStatusIPCGroup": uxsStatusIPCGroup,
       "uxsStatusIPCSHMIDSAvailable": uxsStatusIPCSHMIDSAvailable,
       "uxsStatusIPCSHMIDSValue": uxsStatusIPCSHMIDSValue,
       "uxsStatusIPCSHMIDSLagValue": uxsStatusIPCSHMIDSLagValue,
       "uxsStatusIPCSHMIDSLag": uxsStatusIPCSHMIDSLag,
       "uxsStatusIPCSHMIDSWarnValue": uxsStatusIPCSHMIDSWarnValue,
       "uxsStatusIPCSHMIDSCritValue": uxsStatusIPCSHMIDSCritValue,
       "uxsStatusIPCSHMIDSWarn": uxsStatusIPCSHMIDSWarn,
       "uxsStatusIPCSHMIDSCrit": uxsStatusIPCSHMIDSCrit,
       "uxsStatusIPCSHMIDSMonitor": uxsStatusIPCSHMIDSMonitor,
       "uxsStatusIPCSHMIDSStatus": uxsStatusIPCSHMIDSStatus,
       "uxsStatusIPCSEMIDSAvailable": uxsStatusIPCSEMIDSAvailable,
       "uxsStatusIPCSEMIDSValue": uxsStatusIPCSEMIDSValue,
       "uxsStatusIPCSEMIDSLagValue": uxsStatusIPCSEMIDSLagValue,
       "uxsStatusIPCSEMIDSLag": uxsStatusIPCSEMIDSLag,
       "uxsStatusIPCSEMIDSWarnValue": uxsStatusIPCSEMIDSWarnValue,
       "uxsStatusIPCSEMIDSCritValue": uxsStatusIPCSEMIDSCritValue,
       "uxsStatusIPCSEMIDSWarn": uxsStatusIPCSEMIDSWarn,
       "uxsStatusIPCSEMIDSCrit": uxsStatusIPCSEMIDSCrit,
       "uxsStatusIPCSEMIDSMonitor": uxsStatusIPCSEMIDSMonitor,
       "uxsStatusIPCSEMIDSStatus": uxsStatusIPCSEMIDSStatus,
       "uxsStatusIPCMQIDSAvailable": uxsStatusIPCMQIDSAvailable,
       "uxsStatusIPCMQIDSValue": uxsStatusIPCMQIDSValue,
       "uxsStatusIPCMQIDSLagValue": uxsStatusIPCMQIDSLagValue,
       "uxsStatusIPCMQIDSLag": uxsStatusIPCMQIDSLag,
       "uxsStatusIPCMQIDSWarnValue": uxsStatusIPCMQIDSWarnValue,
       "uxsStatusIPCMQIDSCritValue": uxsStatusIPCMQIDSCritValue,
       "uxsStatusIPCMQIDSWarn": uxsStatusIPCMQIDSWarn,
       "uxsStatusIPCMQIDSCrit": uxsStatusIPCMQIDSCrit,
       "uxsStatusIPCMQIDSMonitor": uxsStatusIPCMQIDSMonitor,
       "uxsStatusIPCMQIDSStatus": uxsStatusIPCMQIDSStatus,
       "uxsStatusIPCMQMonitor": uxsStatusIPCMQMonitor,
       "uxsStatusIPCMQCount": uxsStatusIPCMQCount,
       "uxsStatusIPCMQTable": uxsStatusIPCMQTable,
       "uxsStatusIPCMQEntry": uxsStatusIPCMQEntry,
       "uxsStatusIPCMQID": uxsStatusIPCMQID,
       "uxsStatusIPCMQKey": uxsStatusIPCMQKey,
       "uxsStatusIPCMQMode": uxsStatusIPCMQMode,
       "uxsStatusIPCMQOwner": uxsStatusIPCMQOwner,
       "uxsStatusIPCMQGroup": uxsStatusIPCMQGroup,
       "uxsStatusIPCMQBytesAvailable": uxsStatusIPCMQBytesAvailable,
       "uxsStatusIPCMQBytesValue": uxsStatusIPCMQBytesValue,
       "uxsStatusIPCMQBytesLagValue": uxsStatusIPCMQBytesLagValue,
       "uxsStatusIPCMQBytesLag": uxsStatusIPCMQBytesLag,
       "uxsStatusIPCMQBytesWarnValue": uxsStatusIPCMQBytesWarnValue,
       "uxsStatusIPCMQBytesCritValue": uxsStatusIPCMQBytesCritValue,
       "uxsStatusIPCMQBytesWarn": uxsStatusIPCMQBytesWarn,
       "uxsStatusIPCMQBytesCrit": uxsStatusIPCMQBytesCrit,
       "uxsStatusIPCMQBytesMonitor": uxsStatusIPCMQBytesMonitor,
       "uxsStatusIPCMQBytesStatus": uxsStatusIPCMQBytesStatus,
       "uxsAvailableGroup": uxsAvailableGroup,
       "uxsAvailFSysRefresh": uxsAvailFSysRefresh,
       "uxsAvailFSysTable": uxsAvailFSysTable,
       "uxsAvailFSysEntry": uxsAvailFSysEntry,
       "uxsAvailFSysName": uxsAvailFSysName,
       "uxsAvailFSysRelatedTo": uxsAvailFSysRelatedTo,
       "uxsAvailFSysType": uxsAvailFSysType,
       "uxsAvailDiskRefresh": uxsAvailDiskRefresh,
       "uxsAvailDiskTable": uxsAvailDiskTable,
       "uxsAvailDiskEntry": uxsAvailDiskEntry,
       "uxsAvailDiskName": uxsAvailDiskName,
       "uxsAvailPrnRefresh": uxsAvailPrnRefresh,
       "uxsAvailPrnTable": uxsAvailPrnTable,
       "uxsAvailPrnEntry": uxsAvailPrnEntry,
       "uxsAvailPrnName": uxsAvailPrnName,
       "uxsPollGroup": uxsPollGroup,
       "uxsPollNetGroup": uxsPollNetGroup,
       "uxsPollNetTable": uxsPollNetTable,
       "uxsPollNetEntry": uxsPollNetEntry,
       "uxsPollNetName": uxsPollNetName,
       "uxsPollNetIP": uxsPollNetIP,
       "uxsPollNetIPktValue": uxsPollNetIPktValue,
       "uxsPollNetIErrValue": uxsPollNetIErrValue,
       "uxsPollNetOPktValue": uxsPollNetOPktValue,
       "uxsPollNetOErrValue": uxsPollNetOErrValue,
       "uxsPollNetCollValue": uxsPollNetCollValue,
       "uxsPollIPCGroup": uxsPollIPCGroup,
       "uxsPollIPCSHMMonitor": uxsPollIPCSHMMonitor,
       "uxsPollIPCSHMCount": uxsPollIPCSHMCount,
       "uxsPollIPCSHMTable": uxsPollIPCSHMTable,
       "uxsPollIPCSHMEntry": uxsPollIPCSHMEntry,
       "uxsPollIPCSHMID": uxsPollIPCSHMID,
       "uxsPollIPCSHMKey": uxsPollIPCSHMKey,
       "uxsPollIPCSHMMode": uxsPollIPCSHMMode,
       "uxsPollIPCSHMOwner": uxsPollIPCSHMOwner,
       "uxsPollIPCSHMGroup": uxsPollIPCSHMGroup,
       "uxsPollIPCSHMMaxSize": uxsPollIPCSHMMaxSize,
       "uxsPollIPCSHMAttached": uxsPollIPCSHMAttached,
       "uxsPollIPCSEMMonitor": uxsPollIPCSEMMonitor,
       "uxsPollIPCSEMCount": uxsPollIPCSEMCount,
       "uxsPollIPCSEMTable": uxsPollIPCSEMTable,
       "uxsPollIPCSEMEntry": uxsPollIPCSEMEntry,
       "uxsPollIPCSEMID": uxsPollIPCSEMID,
       "uxsPollIPCSEMKey": uxsPollIPCSEMKey,
       "uxsPollIPCSEMMode": uxsPollIPCSEMMode,
       "uxsPollIPCSEMOwner": uxsPollIPCSEMOwner,
       "uxsPollIPCSEMGroup": uxsPollIPCSEMGroup,
       "uxsPollIPCSEMMaxNums": uxsPollIPCSEMMaxNums}
)
