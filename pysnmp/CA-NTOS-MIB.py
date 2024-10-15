# SNMP MIB module (CA-NTOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CA-NTOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:51:56 2024
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
_Nt_ObjectIdentity = ObjectIdentity
nt = _Nt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2)
)
_CaiNtOs_ObjectIdentity = ObjectIdentity
caiNtOs = _CaiNtOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2)
)
_NtConfigGroup_ObjectIdentity = ObjectIdentity
ntConfigGroup = _NtConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2)
)
_NtGeneralConfig_ObjectIdentity = ObjectIdentity
ntGeneralConfig = _NtGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2)
)
_NtAgentVersion_Type = DisplayString
_NtAgentVersion_Object = MibScalar
ntAgentVersion = _NtAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 2),
    _NtAgentVersion_Type()
)
ntAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAgentVersion.setStatus("mandatory")
_NtAgentColdStartTimestamp_Type = DisplayString
_NtAgentColdStartTimestamp_Object = MibScalar
ntAgentColdStartTimestamp = _NtAgentColdStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 3),
    _NtAgentColdStartTimestamp_Type()
)
ntAgentColdStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAgentColdStartTimestamp.setStatus("mandatory")
_NtAgentWarmStartTimestamp_Type = DisplayString
_NtAgentWarmStartTimestamp_Object = MibScalar
ntAgentWarmStartTimestamp = _NtAgentWarmStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 4),
    _NtAgentWarmStartTimestamp_Type()
)
ntAgentWarmStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAgentWarmStartTimestamp.setStatus("mandatory")
_NtFilesystemPollTimestamp_Type = DisplayString
_NtFilesystemPollTimestamp_Object = MibScalar
ntFilesystemPollTimestamp = _NtFilesystemPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 5),
    _NtFilesystemPollTimestamp_Type()
)
ntFilesystemPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFilesystemPollTimestamp.setStatus("mandatory")
_NtFilePollTimestamp_Type = DisplayString
_NtFilePollTimestamp_Object = MibScalar
ntFilePollTimestamp = _NtFilePollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 6),
    _NtFilePollTimestamp_Type()
)
ntFilePollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFilePollTimestamp.setStatus("mandatory")
_NtProcessPollTimestamp_Type = DisplayString
_NtProcessPollTimestamp_Object = MibScalar
ntProcessPollTimestamp = _NtProcessPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 7),
    _NtProcessPollTimestamp_Type()
)
ntProcessPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessPollTimestamp.setStatus("mandatory")
_NtServicePollTimestamp_Type = DisplayString
_NtServicePollTimestamp_Object = MibScalar
ntServicePollTimestamp = _NtServicePollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 8),
    _NtServicePollTimestamp_Type()
)
ntServicePollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServicePollTimestamp.setStatus("mandatory")
_NtPrinterPollTimestamp_Type = DisplayString
_NtPrinterPollTimestamp_Object = MibScalar
ntPrinterPollTimestamp = _NtPrinterPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 9),
    _NtPrinterPollTimestamp_Type()
)
ntPrinterPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPrinterPollTimestamp.setStatus("mandatory")
_NtMemoryPollTimestamp_Type = DisplayString
_NtMemoryPollTimestamp_Object = MibScalar
ntMemoryPollTimestamp = _NtMemoryPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 10),
    _NtMemoryPollTimestamp_Type()
)
ntMemoryPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntMemoryPollTimestamp.setStatus("mandatory")
_NtProcessorPollTimestamp_Type = DisplayString
_NtProcessorPollTimestamp_Object = MibScalar
ntProcessorPollTimestamp = _NtProcessorPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 11),
    _NtProcessorPollTimestamp_Type()
)
ntProcessorPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessorPollTimestamp.setStatus("mandatory")
_NtRegistryPollTimestamp_Type = DisplayString
_NtRegistryPollTimestamp_Object = MibScalar
ntRegistryPollTimestamp = _NtRegistryPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 12),
    _NtRegistryPollTimestamp_Type()
)
ntRegistryPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegistryPollTimestamp.setStatus("mandatory")
_NtLogPollTimestamp_Type = DisplayString
_NtLogPollTimestamp_Object = MibScalar
ntLogPollTimestamp = _NtLogPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 2, 13),
    _NtLogPollTimestamp_Type()
)
ntLogPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogPollTimestamp.setStatus("mandatory")
_NtFileSystemConfig_ObjectIdentity = ObjectIdentity
ntFileSystemConfig = _NtFileSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3)
)
_NtFSPollInterval_Type = Integer32
_NtFSPollInterval_Object = MibScalar
ntFSPollInterval = _NtFSPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 2),
    _NtFSPollInterval_Type()
)
ntFSPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntFSPollInterval.setStatus("mandatory")
_NtDefFSWarnThresh_Type = Integer32
_NtDefFSWarnThresh_Object = MibScalar
ntDefFSWarnThresh = _NtDefFSWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 3),
    _NtDefFSWarnThresh_Type()
)
ntDefFSWarnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFSWarnThresh.setStatus("mandatory")
_NtDefFSCriticalThresh_Type = Integer32
_NtDefFSCriticalThresh_Object = MibScalar
ntDefFSCriticalThresh = _NtDefFSCriticalThresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 4),
    _NtDefFSCriticalThresh_Type()
)
ntDefFSCriticalThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFSCriticalThresh.setStatus("mandatory")
_NtDefFSDelta_Type = Integer32
_NtDefFSDelta_Object = MibScalar
ntDefFSDelta = _NtDefFSDelta_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 5),
    _NtDefFSDelta_Type()
)
ntDefFSDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFSDelta.setStatus("mandatory")
_NtFSMonitored_Type = Integer32
_NtFSMonitored_Object = MibScalar
ntFSMonitored = _NtFSMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 6),
    _NtFSMonitored_Type()
)
ntFSMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFSMonitored.setStatus("mandatory")
_NtFSAdd_Type = DisplayString
_NtFSAdd_Object = MibScalar
ntFSAdd = _NtFSAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 7),
    _NtFSAdd_Type()
)
ntFSAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntFSAdd.setStatus("mandatory")
_NtFSRemove_Type = DisplayString
_NtFSRemove_Object = MibScalar
ntFSRemove = _NtFSRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 3, 8),
    _NtFSRemove_Type()
)
ntFSRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntFSRemove.setStatus("mandatory")
_NtFileConfig_ObjectIdentity = ObjectIdentity
ntFileConfig = _NtFileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4)
)
_NtFilePollInterval_Type = Integer32
_NtFilePollInterval_Object = MibScalar
ntFilePollInterval = _NtFilePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 2),
    _NtFilePollInterval_Type()
)
ntFilePollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntFilePollInterval.setStatus("mandatory")
_NtDefFileSizeWarning_Type = Integer32
_NtDefFileSizeWarning_Object = MibScalar
ntDefFileSizeWarning = _NtDefFileSizeWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 3),
    _NtDefFileSizeWarning_Type()
)
ntDefFileSizeWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFileSizeWarning.setStatus("mandatory")
_NtDefFileSizeCritical_Type = Integer32
_NtDefFileSizeCritical_Object = MibScalar
ntDefFileSizeCritical = _NtDefFileSizeCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 4),
    _NtDefFileSizeCritical_Type()
)
ntDefFileSizeCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFileSizeCritical.setStatus("mandatory")


class _NtDefFileSizeChangeFlag_Type(Integer32):
    """Custom type ntDefFileSizeChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtDefFileSizeChangeFlag_Type.__name__ = "Integer32"
_NtDefFileSizeChangeFlag_Object = MibScalar
ntDefFileSizeChangeFlag = _NtDefFileSizeChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 5),
    _NtDefFileSizeChangeFlag_Type()
)
ntDefFileSizeChangeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFileSizeChangeFlag.setStatus("mandatory")
_NtDefFileSizeChange_Type = Integer32
_NtDefFileSizeChange_Object = MibScalar
ntDefFileSizeChange = _NtDefFileSizeChange_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 6),
    _NtDefFileSizeChange_Type()
)
ntDefFileSizeChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFileSizeChange.setStatus("mandatory")


class _NtDefFileTimestampFlag_Type(Integer32):
    """Custom type ntDefFileTimestampFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtDefFileTimestampFlag_Type.__name__ = "Integer32"
_NtDefFileTimestampFlag_Object = MibScalar
ntDefFileTimestampFlag = _NtDefFileTimestampFlag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 7),
    _NtDefFileTimestampFlag_Type()
)
ntDefFileTimestampFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefFileTimestampFlag.setStatus("mandatory")
_NtFilesMonitored_Type = Integer32
_NtFilesMonitored_Object = MibScalar
ntFilesMonitored = _NtFilesMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 8),
    _NtFilesMonitored_Type()
)
ntFilesMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFilesMonitored.setStatus("mandatory")
_NtFileAdd_Type = DisplayString
_NtFileAdd_Object = MibScalar
ntFileAdd = _NtFileAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 9),
    _NtFileAdd_Type()
)
ntFileAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntFileAdd.setStatus("mandatory")
_NtFileRemove_Type = DisplayString
_NtFileRemove_Object = MibScalar
ntFileRemove = _NtFileRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 4, 10),
    _NtFileRemove_Type()
)
ntFileRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntFileRemove.setStatus("mandatory")
_NtProcessConfig_ObjectIdentity = ObjectIdentity
ntProcessConfig = _NtProcessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5)
)
_NtProcPollInterval_Type = Integer32
_NtProcPollInterval_Object = MibScalar
ntProcPollInterval = _NtProcPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 2),
    _NtProcPollInterval_Type()
)
ntProcPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntProcPollInterval.setStatus("mandatory")


class _NtDefProcAlertLevel_Type(Integer32):
    """Custom type ntDefProcAlertLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("not-monitored", 1),
          ("warning", 2))
    )


_NtDefProcAlertLevel_Type.__name__ = "Integer32"
_NtDefProcAlertLevel_Object = MibScalar
ntDefProcAlertLevel = _NtDefProcAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 3),
    _NtDefProcAlertLevel_Type()
)
ntDefProcAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefProcAlertLevel.setStatus("mandatory")


class _NtDefProcExist_Type(Integer32):
    """Custom type ntDefProcExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alert-if-exist", 1),
          ("alert-if-not-exist", 2))
    )


_NtDefProcExist_Type.__name__ = "Integer32"
_NtDefProcExist_Object = MibScalar
ntDefProcExist = _NtDefProcExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 4),
    _NtDefProcExist_Type()
)
ntDefProcExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefProcExist.setStatus("mandatory")


class _NtDefProcInstanceAlert_Type(Integer32):
    """Custom type ntDefProcInstanceAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_NtDefProcInstanceAlert_Type.__name__ = "Integer32"
_NtDefProcInstanceAlert_Object = MibScalar
ntDefProcInstanceAlert = _NtDefProcInstanceAlert_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 5),
    _NtDefProcInstanceAlert_Type()
)
ntDefProcInstanceAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefProcInstanceAlert.setStatus("mandatory")


class _NtDefProcThreadAlert_Type(Integer32):
    """Custom type ntDefProcThreadAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("above", 2),
          ("below", 3),
          ("do-not-monitor", 1))
    )


_NtDefProcThreadAlert_Type.__name__ = "Integer32"
_NtDefProcThreadAlert_Object = MibScalar
ntDefProcThreadAlert = _NtDefProcThreadAlert_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 6),
    _NtDefProcThreadAlert_Type()
)
ntDefProcThreadAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefProcThreadAlert.setStatus("mandatory")
_NtProcessesMonitored_Type = Integer32
_NtProcessesMonitored_Object = MibScalar
ntProcessesMonitored = _NtProcessesMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 7),
    _NtProcessesMonitored_Type()
)
ntProcessesMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessesMonitored.setStatus("mandatory")
_NtProcAdd_Type = DisplayString
_NtProcAdd_Object = MibScalar
ntProcAdd = _NtProcAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 8),
    _NtProcAdd_Type()
)
ntProcAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntProcAdd.setStatus("mandatory")
_NtProcRemove_Type = DisplayString
_NtProcRemove_Object = MibScalar
ntProcRemove = _NtProcRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 5, 9),
    _NtProcRemove_Type()
)
ntProcRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntProcRemove.setStatus("mandatory")
_NtServiceConfig_ObjectIdentity = ObjectIdentity
ntServiceConfig = _NtServiceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 6)
)
_NtServPollInterval_Type = Integer32
_NtServPollInterval_Object = MibScalar
ntServPollInterval = _NtServPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 6, 2),
    _NtServPollInterval_Type()
)
ntServPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntServPollInterval.setStatus("mandatory")


class _NtDefServAlertOn_Type(Integer32):
    """Custom type ntDefServAlertOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("do-not-monitor", 1),
          ("inactive", 3))
    )


_NtDefServAlertOn_Type.__name__ = "Integer32"
_NtDefServAlertOn_Object = MibScalar
ntDefServAlertOn = _NtDefServAlertOn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 6, 3),
    _NtDefServAlertOn_Type()
)
ntDefServAlertOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefServAlertOn.setStatus("mandatory")
_NtServicesMonitored_Type = Integer32
_NtServicesMonitored_Object = MibScalar
ntServicesMonitored = _NtServicesMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 6, 4),
    _NtServicesMonitored_Type()
)
ntServicesMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServicesMonitored.setStatus("mandatory")
_NtServiceAdd_Type = DisplayString
_NtServiceAdd_Object = MibScalar
ntServiceAdd = _NtServiceAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 6, 5),
    _NtServiceAdd_Type()
)
ntServiceAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntServiceAdd.setStatus("mandatory")
_NtServiceRemove_Type = DisplayString
_NtServiceRemove_Object = MibScalar
ntServiceRemove = _NtServiceRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 6, 6),
    _NtServiceRemove_Type()
)
ntServiceRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntServiceRemove.setStatus("mandatory")
_NtPrinterConfig_ObjectIdentity = ObjectIdentity
ntPrinterConfig = _NtPrinterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7)
)
_NtPrinterPollInterval_Type = Integer32
_NtPrinterPollInterval_Object = MibScalar
ntPrinterPollInterval = _NtPrinterPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 2),
    _NtPrinterPollInterval_Type()
)
ntPrinterPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntPrinterPollInterval.setStatus("mandatory")


class _NtDefPrintEventMonitor_Type(Integer32):
    """Custom type ntDefPrintEventMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtDefPrintEventMonitor_Type.__name__ = "Integer32"
_NtDefPrintEventMonitor_Object = MibScalar
ntDefPrintEventMonitor = _NtDefPrintEventMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 3),
    _NtDefPrintEventMonitor_Type()
)
ntDefPrintEventMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefPrintEventMonitor.setStatus("mandatory")


class _NtDefPrinterQFlag_Type(Integer32):
    """Custom type ntDefPrinterQFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_NtDefPrinterQFlag_Type.__name__ = "Integer32"
_NtDefPrinterQFlag_Object = MibScalar
ntDefPrinterQFlag = _NtDefPrinterQFlag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 4),
    _NtDefPrinterQFlag_Type()
)
ntDefPrinterQFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefPrinterQFlag.setStatus("mandatory")
_NtDefPrinterQWarning_Type = Integer32
_NtDefPrinterQWarning_Object = MibScalar
ntDefPrinterQWarning = _NtDefPrinterQWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 5),
    _NtDefPrinterQWarning_Type()
)
ntDefPrinterQWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefPrinterQWarning.setStatus("mandatory")
_NtDefPrinterQCritical_Type = Integer32
_NtDefPrinterQCritical_Object = MibScalar
ntDefPrinterQCritical = _NtDefPrinterQCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 6),
    _NtDefPrinterQCritical_Type()
)
ntDefPrinterQCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefPrinterQCritical.setStatus("mandatory")
_NtPrintersMonitored_Type = Integer32
_NtPrintersMonitored_Object = MibScalar
ntPrintersMonitored = _NtPrintersMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 7),
    _NtPrintersMonitored_Type()
)
ntPrintersMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPrintersMonitored.setStatus("mandatory")
_NtPrinterAdd_Type = DisplayString
_NtPrinterAdd_Object = MibScalar
ntPrinterAdd = _NtPrinterAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 8),
    _NtPrinterAdd_Type()
)
ntPrinterAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntPrinterAdd.setStatus("mandatory")
_NtPrinterRemove_Type = DisplayString
_NtPrinterRemove_Object = MibScalar
ntPrinterRemove = _NtPrinterRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 7, 9),
    _NtPrinterRemove_Type()
)
ntPrinterRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntPrinterRemove.setStatus("mandatory")
_NtMemoryConfig_ObjectIdentity = ObjectIdentity
ntMemoryConfig = _NtMemoryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8)
)
_NtMemPollInterval_Type = Integer32
_NtMemPollInterval_Object = MibScalar
ntMemPollInterval = _NtMemPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 2),
    _NtMemPollInterval_Type()
)
ntMemPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntMemPollInterval.setStatus("mandatory")
_NtDefMemLoadWarning_Type = Integer32
_NtDefMemLoadWarning_Object = MibScalar
ntDefMemLoadWarning = _NtDefMemLoadWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 3),
    _NtDefMemLoadWarning_Type()
)
ntDefMemLoadWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemLoadWarning.setStatus("mandatory")
_NtDefMemLoadCritical_Type = Integer32
_NtDefMemLoadCritical_Object = MibScalar
ntDefMemLoadCritical = _NtDefMemLoadCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 4),
    _NtDefMemLoadCritical_Type()
)
ntDefMemLoadCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemLoadCritical.setStatus("mandatory")
_NtDefMemLoadCount_Type = Integer32
_NtDefMemLoadCount_Object = MibScalar
ntDefMemLoadCount = _NtDefMemLoadCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 5),
    _NtDefMemLoadCount_Type()
)
ntDefMemLoadCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemLoadCount.setStatus("mandatory")
_NtDefMemPhysWarning_Type = Integer32
_NtDefMemPhysWarning_Object = MibScalar
ntDefMemPhysWarning = _NtDefMemPhysWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 6),
    _NtDefMemPhysWarning_Type()
)
ntDefMemPhysWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemPhysWarning.setStatus("mandatory")
_NtDefMemPhysCritical_Type = Integer32
_NtDefMemPhysCritical_Object = MibScalar
ntDefMemPhysCritical = _NtDefMemPhysCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 7),
    _NtDefMemPhysCritical_Type()
)
ntDefMemPhysCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemPhysCritical.setStatus("mandatory")
_NtDefMemPhysCount_Type = Integer32
_NtDefMemPhysCount_Object = MibScalar
ntDefMemPhysCount = _NtDefMemPhysCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 8),
    _NtDefMemPhysCount_Type()
)
ntDefMemPhysCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemPhysCount.setStatus("mandatory")
_NtDefMemSwapWarning_Type = Integer32
_NtDefMemSwapWarning_Object = MibScalar
ntDefMemSwapWarning = _NtDefMemSwapWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 9),
    _NtDefMemSwapWarning_Type()
)
ntDefMemSwapWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemSwapWarning.setStatus("mandatory")
_NtDefMemSwapCritical_Type = Integer32
_NtDefMemSwapCritical_Object = MibScalar
ntDefMemSwapCritical = _NtDefMemSwapCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 10),
    _NtDefMemSwapCritical_Type()
)
ntDefMemSwapCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemSwapCritical.setStatus("mandatory")
_NtDefMemSwapCount_Type = Integer32
_NtDefMemSwapCount_Object = MibScalar
ntDefMemSwapCount = _NtDefMemSwapCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 8, 11),
    _NtDefMemSwapCount_Type()
)
ntDefMemSwapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefMemSwapCount.setStatus("mandatory")
_NtProcessorConfig_ObjectIdentity = ObjectIdentity
ntProcessorConfig = _NtProcessorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 9)
)
_NtCPUPollInterval_Type = Integer32
_NtCPUPollInterval_Object = MibScalar
ntCPUPollInterval = _NtCPUPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 9, 2),
    _NtCPUPollInterval_Type()
)
ntCPUPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntCPUPollInterval.setStatus("mandatory")
_NtDefCPUWarning_Type = Integer32
_NtDefCPUWarning_Object = MibScalar
ntDefCPUWarning = _NtDefCPUWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 9, 3),
    _NtDefCPUWarning_Type()
)
ntDefCPUWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefCPUWarning.setStatus("mandatory")
_NtDefCPUCritical_Type = Integer32
_NtDefCPUCritical_Object = MibScalar
ntDefCPUCritical = _NtDefCPUCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 9, 4),
    _NtDefCPUCritical_Type()
)
ntDefCPUCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefCPUCritical.setStatus("mandatory")
_NtDefCPUCount_Type = Integer32
_NtDefCPUCount_Object = MibScalar
ntDefCPUCount = _NtDefCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 9, 5),
    _NtDefCPUCount_Type()
)
ntDefCPUCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefCPUCount.setStatus("mandatory")
_NtCPUsMonitored_Type = Integer32
_NtCPUsMonitored_Object = MibScalar
ntCPUsMonitored = _NtCPUsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 9, 6),
    _NtCPUsMonitored_Type()
)
ntCPUsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUsMonitored.setStatus("mandatory")
_NtRegistryConfig_ObjectIdentity = ObjectIdentity
ntRegistryConfig = _NtRegistryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10)
)
_NtRegPollInterval_Type = Integer32
_NtRegPollInterval_Object = MibScalar
ntRegPollInterval = _NtRegPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 2),
    _NtRegPollInterval_Type()
)
ntRegPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntRegPollInterval.setStatus("mandatory")


class _NtDefRegMonitorLevel_Type(Integer32):
    """Custom type ntDefRegMonitorLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("change", 2),
          ("do-not-monitor", 1),
          ("thresholds", 3))
    )


_NtDefRegMonitorLevel_Type.__name__ = "Integer32"
_NtDefRegMonitorLevel_Object = MibScalar
ntDefRegMonitorLevel = _NtDefRegMonitorLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 3),
    _NtDefRegMonitorLevel_Type()
)
ntDefRegMonitorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefRegMonitorLevel.setStatus("mandatory")
_NtDefRegWarning_Type = Integer32
_NtDefRegWarning_Object = MibScalar
ntDefRegWarning = _NtDefRegWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 4),
    _NtDefRegWarning_Type()
)
ntDefRegWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefRegWarning.setStatus("mandatory")
_NtDefRegCritical_Type = Integer32
_NtDefRegCritical_Object = MibScalar
ntDefRegCritical = _NtDefRegCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 5),
    _NtDefRegCritical_Type()
)
ntDefRegCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefRegCritical.setStatus("mandatory")
_NtRegLeavesMonitored_Type = Integer32
_NtRegLeavesMonitored_Object = MibScalar
ntRegLeavesMonitored = _NtRegLeavesMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 6),
    _NtRegLeavesMonitored_Type()
)
ntRegLeavesMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegLeavesMonitored.setStatus("mandatory")
_NtRegistryLeafAdd_Type = DisplayString
_NtRegistryLeafAdd_Object = MibScalar
ntRegistryLeafAdd = _NtRegistryLeafAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 7),
    _NtRegistryLeafAdd_Type()
)
ntRegistryLeafAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntRegistryLeafAdd.setStatus("mandatory")
_NtRegistryLeafRemove_Type = DisplayString
_NtRegistryLeafRemove_Object = MibScalar
ntRegistryLeafRemove = _NtRegistryLeafRemove_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 10, 8),
    _NtRegistryLeafRemove_Type()
)
ntRegistryLeafRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntRegistryLeafRemove.setStatus("mandatory")
_NtEventLogConfig_ObjectIdentity = ObjectIdentity
ntEventLogConfig = _NtEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11)
)
_NtLogPollInterval_Type = Integer32
_NtLogPollInterval_Object = MibScalar
ntLogPollInterval = _NtLogPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 1),
    _NtLogPollInterval_Type()
)
ntLogPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntLogPollInterval.setStatus("mandatory")
_NtLogApplicationCount_Type = Integer32
_NtLogApplicationCount_Object = MibScalar
ntLogApplicationCount = _NtLogApplicationCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 2),
    _NtLogApplicationCount_Type()
)
ntLogApplicationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogApplicationCount.setStatus("mandatory")
_NtLogSecurityCount_Type = Integer32
_NtLogSecurityCount_Object = MibScalar
ntLogSecurityCount = _NtLogSecurityCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 3),
    _NtLogSecurityCount_Type()
)
ntLogSecurityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogSecurityCount.setStatus("mandatory")
_NtLogSystemCount_Type = Integer32
_NtLogSystemCount_Object = MibScalar
ntLogSystemCount = _NtLogSystemCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 4),
    _NtLogSystemCount_Type()
)
ntLogSystemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogSystemCount.setStatus("mandatory")


class _NtDefLogMonitorLevel_Type(Integer32):
    """Custom type ntDefLogMonitorLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtDefLogMonitorLevel_Type.__name__ = "Integer32"
_NtDefLogMonitorLevel_Object = MibScalar
ntDefLogMonitorLevel = _NtDefLogMonitorLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 5),
    _NtDefLogMonitorLevel_Type()
)
ntDefLogMonitorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntDefLogMonitorLevel.setStatus("mandatory")
_NtLogsMonitored_Type = Integer32
_NtLogsMonitored_Object = MibScalar
ntLogsMonitored = _NtLogsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 6),
    _NtLogsMonitored_Type()
)
ntLogsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogsMonitored.setStatus("mandatory")
_NtLogAdd_Type = DisplayString
_NtLogAdd_Object = MibScalar
ntLogAdd = _NtLogAdd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 2, 11, 7),
    _NtLogAdd_Type()
)
ntLogAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntLogAdd.setStatus("mandatory")
_NtStatusGroup_ObjectIdentity = ObjectIdentity
ntStatusGroup = _NtStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3)
)
_NtStatusSummary_ObjectIdentity = ObjectIdentity
ntStatusSummary = _NtStatusSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2)
)


class _NtStatus_Type(Integer32):
    """Custom type ntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatus_Type.__name__ = "Integer32"
_NtStatus_Object = MibScalar
ntStatus = _NtStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 2),
    _NtStatus_Type()
)
ntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatus.setStatus("mandatory")
_NtTotalWarning_Type = Integer32
_NtTotalWarning_Object = MibScalar
ntTotalWarning = _NtTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 3),
    _NtTotalWarning_Type()
)
ntTotalWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTotalWarning.setStatus("mandatory")
_NtTotalCritical_Type = Integer32
_NtTotalCritical_Object = MibScalar
ntTotalCritical = _NtTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 4),
    _NtTotalCritical_Type()
)
ntTotalCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTotalCritical.setStatus("mandatory")
_NtFSWarnStatus_Type = Integer32
_NtFSWarnStatus_Object = MibScalar
ntFSWarnStatus = _NtFSWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 5),
    _NtFSWarnStatus_Type()
)
ntFSWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFSWarnStatus.setStatus("mandatory")
_NtFSCriticalStatus_Type = Integer32
_NtFSCriticalStatus_Object = MibScalar
ntFSCriticalStatus = _NtFSCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 6),
    _NtFSCriticalStatus_Type()
)
ntFSCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFSCriticalStatus.setStatus("mandatory")
_NtFileWarnStatus_Type = Integer32
_NtFileWarnStatus_Object = MibScalar
ntFileWarnStatus = _NtFileWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 7),
    _NtFileWarnStatus_Type()
)
ntFileWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileWarnStatus.setStatus("mandatory")
_NtFileCriticalStatus_Type = Integer32
_NtFileCriticalStatus_Object = MibScalar
ntFileCriticalStatus = _NtFileCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 8),
    _NtFileCriticalStatus_Type()
)
ntFileCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileCriticalStatus.setStatus("mandatory")
_NtProcessWarnStatus_Type = Integer32
_NtProcessWarnStatus_Object = MibScalar
ntProcessWarnStatus = _NtProcessWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 9),
    _NtProcessWarnStatus_Type()
)
ntProcessWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessWarnStatus.setStatus("mandatory")
_NtProcessCriticalStatus_Type = Integer32
_NtProcessCriticalStatus_Object = MibScalar
ntProcessCriticalStatus = _NtProcessCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 10),
    _NtProcessCriticalStatus_Type()
)
ntProcessCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessCriticalStatus.setStatus("mandatory")
_NtServicesWarnStatus_Type = Integer32
_NtServicesWarnStatus_Object = MibScalar
ntServicesWarnStatus = _NtServicesWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 11),
    _NtServicesWarnStatus_Type()
)
ntServicesWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServicesWarnStatus.setStatus("mandatory")
_NtServicesCriticalStatus_Type = Integer32
_NtServicesCriticalStatus_Object = MibScalar
ntServicesCriticalStatus = _NtServicesCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 12),
    _NtServicesCriticalStatus_Type()
)
ntServicesCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServicesCriticalStatus.setStatus("mandatory")
_NtPrintWarnStatus_Type = Integer32
_NtPrintWarnStatus_Object = MibScalar
ntPrintWarnStatus = _NtPrintWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 13),
    _NtPrintWarnStatus_Type()
)
ntPrintWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPrintWarnStatus.setStatus("mandatory")
_NtPrintCriticalStatus_Type = Integer32
_NtPrintCriticalStatus_Object = MibScalar
ntPrintCriticalStatus = _NtPrintCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 14),
    _NtPrintCriticalStatus_Type()
)
ntPrintCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPrintCriticalStatus.setStatus("mandatory")
_NtMemoryWarnStatus_Type = Integer32
_NtMemoryWarnStatus_Object = MibScalar
ntMemoryWarnStatus = _NtMemoryWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 15),
    _NtMemoryWarnStatus_Type()
)
ntMemoryWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntMemoryWarnStatus.setStatus("mandatory")
_NtMemoryCriticalStatus_Type = Integer32
_NtMemoryCriticalStatus_Object = MibScalar
ntMemoryCriticalStatus = _NtMemoryCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 16),
    _NtMemoryCriticalStatus_Type()
)
ntMemoryCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntMemoryCriticalStatus.setStatus("mandatory")
_NtProcessorWarnStatus_Type = Integer32
_NtProcessorWarnStatus_Object = MibScalar
ntProcessorWarnStatus = _NtProcessorWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 17),
    _NtProcessorWarnStatus_Type()
)
ntProcessorWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessorWarnStatus.setStatus("mandatory")
_NtProcessorCriticalStatus_Type = Integer32
_NtProcessorCriticalStatus_Object = MibScalar
ntProcessorCriticalStatus = _NtProcessorCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 18),
    _NtProcessorCriticalStatus_Type()
)
ntProcessorCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessorCriticalStatus.setStatus("mandatory")
_NtRegistryWarnStatus_Type = Integer32
_NtRegistryWarnStatus_Object = MibScalar
ntRegistryWarnStatus = _NtRegistryWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 19),
    _NtRegistryWarnStatus_Type()
)
ntRegistryWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegistryWarnStatus.setStatus("mandatory")
_NtRegistryCriticalStatus_Type = Integer32
_NtRegistryCriticalStatus_Object = MibScalar
ntRegistryCriticalStatus = _NtRegistryCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 20),
    _NtRegistryCriticalStatus_Type()
)
ntRegistryCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegistryCriticalStatus.setStatus("mandatory")
_NtEventLogWarnStatus_Type = Integer32
_NtEventLogWarnStatus_Object = MibScalar
ntEventLogWarnStatus = _NtEventLogWarnStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 21),
    _NtEventLogWarnStatus_Type()
)
ntEventLogWarnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventLogWarnStatus.setStatus("mandatory")
_NtEventLogCriticalStatus_Type = Integer32
_NtEventLogCriticalStatus_Object = MibScalar
ntEventLogCriticalStatus = _NtEventLogCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 2, 22),
    _NtEventLogCriticalStatus_Type()
)
ntEventLogCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventLogCriticalStatus.setStatus("mandatory")
_NtFilesystemStTable_Object = MibTable
ntFilesystemStTable = _NtFilesystemStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ntFilesystemStTable.setStatus("mandatory")
_NtFilesystemStTableEntry_Object = MibTableRow
ntFilesystemStTableEntry = _NtFilesystemStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2)
)
ntFilesystemStTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusFSDriveLetter"),
)
if mibBuilder.loadTexts:
    ntFilesystemStTableEntry.setStatus("mandatory")
_NtStatusFSDriveLetter_Type = DisplayString
_NtStatusFSDriveLetter_Object = MibTableColumn
ntStatusFSDriveLetter = _NtStatusFSDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 2),
    _NtStatusFSDriveLetter_Type()
)
ntStatusFSDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSDriveLetter.setStatus("mandatory")
_NtStatusFSDriveLabel_Type = DisplayString
_NtStatusFSDriveLabel_Object = MibTableColumn
ntStatusFSDriveLabel = _NtStatusFSDriveLabel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 3),
    _NtStatusFSDriveLabel_Type()
)
ntStatusFSDriveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSDriveLabel.setStatus("mandatory")
_NtStatusFSDriveType_Type = DisplayString
_NtStatusFSDriveType_Object = MibTableColumn
ntStatusFSDriveType = _NtStatusFSDriveType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 4),
    _NtStatusFSDriveType_Type()
)
ntStatusFSDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSDriveType.setStatus("mandatory")
_NtStatusFSDriveFormat_Type = DisplayString
_NtStatusFSDriveFormat_Object = MibTableColumn
ntStatusFSDriveFormat = _NtStatusFSDriveFormat_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 5),
    _NtStatusFSDriveFormat_Type()
)
ntStatusFSDriveFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSDriveFormat.setStatus("mandatory")
_NtStatusFSTotalCapacity_Type = Integer32
_NtStatusFSTotalCapacity_Object = MibTableColumn
ntStatusFSTotalCapacity = _NtStatusFSTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 6),
    _NtStatusFSTotalCapacity_Type()
)
ntStatusFSTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSTotalCapacity.setStatus("mandatory")
_NtStatusFSUtilization_Type = Integer32
_NtStatusFSUtilization_Object = MibTableColumn
ntStatusFSUtilization = _NtStatusFSUtilization_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 7),
    _NtStatusFSUtilization_Type()
)
ntStatusFSUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSUtilization.setStatus("mandatory")
_NtStatusFSFree_Type = Integer32
_NtStatusFSFree_Object = MibTableColumn
ntStatusFSFree = _NtStatusFSFree_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 8),
    _NtStatusFSFree_Type()
)
ntStatusFSFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSFree.setStatus("mandatory")


class _NtStatusFSStatus_Type(Integer32):
    """Custom type ntStatusFSStatus based on Integer32"""
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
        *(("critical", 3),
          ("down", 4),
          ("ok", 1),
          ("unknown", 5),
          ("warning", 2))
    )


_NtStatusFSStatus_Type.__name__ = "Integer32"
_NtStatusFSStatus_Object = MibTableColumn
ntStatusFSStatus = _NtStatusFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 9),
    _NtStatusFSStatus_Type()
)
ntStatusFSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSStatus.setStatus("mandatory")
_NtStatusFSPcntWarn_Type = Integer32
_NtStatusFSPcntWarn_Object = MibTableColumn
ntStatusFSPcntWarn = _NtStatusFSPcntWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 10),
    _NtStatusFSPcntWarn_Type()
)
ntStatusFSPcntWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSPcntWarn.setStatus("mandatory")
_NtStatusFSPcntCritical_Type = Integer32
_NtStatusFSPcntCritical_Object = MibTableColumn
ntStatusFSPcntCritical = _NtStatusFSPcntCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 11),
    _NtStatusFSPcntCritical_Type()
)
ntStatusFSPcntCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSPcntCritical.setStatus("mandatory")
_NtStatusFSKByteWarn_Type = Integer32
_NtStatusFSKByteWarn_Object = MibTableColumn
ntStatusFSKByteWarn = _NtStatusFSKByteWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 12),
    _NtStatusFSKByteWarn_Type()
)
ntStatusFSKByteWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSKByteWarn.setStatus("mandatory")
_NtStatusFSKByteCritical_Type = Integer32
_NtStatusFSKByteCritical_Object = MibTableColumn
ntStatusFSKByteCritical = _NtStatusFSKByteCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 13),
    _NtStatusFSKByteCritical_Type()
)
ntStatusFSKByteCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSKByteCritical.setStatus("mandatory")
_NtStatusFSAvgUtil_Type = Integer32
_NtStatusFSAvgUtil_Object = MibTableColumn
ntStatusFSAvgUtil = _NtStatusFSAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 14),
    _NtStatusFSAvgUtil_Type()
)
ntStatusFSAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSAvgUtil.setStatus("mandatory")
_NtStatusFSMinUtil_Type = Integer32
_NtStatusFSMinUtil_Object = MibTableColumn
ntStatusFSMinUtil = _NtStatusFSMinUtil_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 15),
    _NtStatusFSMinUtil_Type()
)
ntStatusFSMinUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSMinUtil.setStatus("mandatory")
_NtStatusFSMaxUtil_Type = Integer32
_NtStatusFSMaxUtil_Object = MibTableColumn
ntStatusFSMaxUtil = _NtStatusFSMaxUtil_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 16),
    _NtStatusFSMaxUtil_Type()
)
ntStatusFSMaxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSMaxUtil.setStatus("mandatory")
_NtStatusFSUtilDelta_Type = Integer32
_NtStatusFSUtilDelta_Object = MibTableColumn
ntStatusFSUtilDelta = _NtStatusFSUtilDelta_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 17),
    _NtStatusFSUtilDelta_Type()
)
ntStatusFSUtilDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFSUtilDelta.setStatus("mandatory")


class _NtStatusFSDeltaLevel_Type(Integer32):
    """Custom type ntStatusFSDeltaLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtStatusFSDeltaLevel_Type.__name__ = "Integer32"
_NtStatusFSDeltaLevel_Object = MibTableColumn
ntStatusFSDeltaLevel = _NtStatusFSDeltaLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 18),
    _NtStatusFSDeltaLevel_Type()
)
ntStatusFSDeltaLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSDeltaLevel.setStatus("mandatory")
_NtStatusFSDeltaThreshold_Type = Integer32
_NtStatusFSDeltaThreshold_Object = MibTableColumn
ntStatusFSDeltaThreshold = _NtStatusFSDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 19),
    _NtStatusFSDeltaThreshold_Type()
)
ntStatusFSDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSDeltaThreshold.setStatus("mandatory")
_NtStatusFSDescription_Type = DisplayString
_NtStatusFSDescription_Object = MibTableColumn
ntStatusFSDescription = _NtStatusFSDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 3, 2, 20),
    _NtStatusFSDescription_Type()
)
ntStatusFSDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFSDescription.setStatus("mandatory")
_NtFileStTable_Object = MibTable
ntFileStTable = _NtFileStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    ntFileStTable.setStatus("mandatory")
_NtFileStTableEntry_Object = MibTableRow
ntFileStTableEntry = _NtFileStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2)
)
ntFileStTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusFileName"),
)
if mibBuilder.loadTexts:
    ntFileStTableEntry.setStatus("mandatory")
_NtStatusFileName_Type = DisplayString
_NtStatusFileName_Object = MibTableColumn
ntStatusFileName = _NtStatusFileName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 2),
    _NtStatusFileName_Type()
)
ntStatusFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileName.setStatus("mandatory")


class _NtStatusFileStatus_Type(Integer32):
    """Custom type ntStatusFileStatus based on Integer32"""
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
        *(("critical", 3),
          ("ok", 1),
          ("unknown", 4),
          ("warning", 2))
    )


_NtStatusFileStatus_Type.__name__ = "Integer32"
_NtStatusFileStatus_Object = MibTableColumn
ntStatusFileStatus = _NtStatusFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 3),
    _NtStatusFileStatus_Type()
)
ntStatusFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileStatus.setStatus("mandatory")
_NtStatusFileSize_Type = Integer32
_NtStatusFileSize_Object = MibTableColumn
ntStatusFileSize = _NtStatusFileSize_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 4),
    _NtStatusFileSize_Type()
)
ntStatusFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileSize.setStatus("mandatory")


class _NtStatusFileSizeStatus_Type(Integer32):
    """Custom type ntStatusFileSizeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusFileSizeStatus_Type.__name__ = "Integer32"
_NtStatusFileSizeStatus_Object = MibTableColumn
ntStatusFileSizeStatus = _NtStatusFileSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 5),
    _NtStatusFileSizeStatus_Type()
)
ntStatusFileSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileSizeStatus.setStatus("mandatory")
_NtStatusFileSizeWarning_Type = Integer32
_NtStatusFileSizeWarning_Object = MibTableColumn
ntStatusFileSizeWarning = _NtStatusFileSizeWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 6),
    _NtStatusFileSizeWarning_Type()
)
ntStatusFileSizeWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileSizeWarning.setStatus("mandatory")
_NtStatusFileSizeCritical_Type = Integer32
_NtStatusFileSizeCritical_Object = MibTableColumn
ntStatusFileSizeCritical = _NtStatusFileSizeCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 7),
    _NtStatusFileSizeCritical_Type()
)
ntStatusFileSizeCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileSizeCritical.setStatus("mandatory")
_NtStatusFileTimestamp_Type = DisplayString
_NtStatusFileTimestamp_Object = MibTableColumn
ntStatusFileTimestamp = _NtStatusFileTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 8),
    _NtStatusFileTimestamp_Type()
)
ntStatusFileTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileTimestamp.setStatus("mandatory")


class _NtStatusFileTimestampFlag_Type(Integer32):
    """Custom type ntStatusFileTimestampFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtStatusFileTimestampFlag_Type.__name__ = "Integer32"
_NtStatusFileTimestampFlag_Object = MibTableColumn
ntStatusFileTimestampFlag = _NtStatusFileTimestampFlag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 9),
    _NtStatusFileTimestampFlag_Type()
)
ntStatusFileTimestampFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileTimestampFlag.setStatus("mandatory")


class _NtStatusFileTimestampStatus_Type(Integer32):
    """Custom type ntStatusFileTimestampStatus based on Integer32"""
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
        *(("critical", 3),
          ("not-monitored", 4),
          ("ok", 1),
          ("reset", 5),
          ("warning", 2))
    )


_NtStatusFileTimestampStatus_Type.__name__ = "Integer32"
_NtStatusFileTimestampStatus_Object = MibTableColumn
ntStatusFileTimestampStatus = _NtStatusFileTimestampStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 10),
    _NtStatusFileTimestampStatus_Type()
)
ntStatusFileTimestampStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileTimestampStatus.setStatus("mandatory")


class _NtStatusFileSizeChFlag_Type(Integer32):
    """Custom type ntStatusFileSizeChFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtStatusFileSizeChFlag_Type.__name__ = "Integer32"
_NtStatusFileSizeChFlag_Object = MibTableColumn
ntStatusFileSizeChFlag = _NtStatusFileSizeChFlag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 11),
    _NtStatusFileSizeChFlag_Type()
)
ntStatusFileSizeChFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileSizeChFlag.setStatus("mandatory")
_NtStatusFileSizeCh_Type = Integer32
_NtStatusFileSizeCh_Object = MibTableColumn
ntStatusFileSizeCh = _NtStatusFileSizeCh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 12),
    _NtStatusFileSizeCh_Type()
)
ntStatusFileSizeCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileSizeCh.setStatus("mandatory")


class _NtStatusFileSizeChState_Type(Integer32):
    """Custom type ntStatusFileSizeChState based on Integer32"""
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
        *(("critical", 3),
          ("not-monitored", 4),
          ("ok", 1),
          ("reset", 5),
          ("warning", 2))
    )


_NtStatusFileSizeChState_Type.__name__ = "Integer32"
_NtStatusFileSizeChState_Object = MibTableColumn
ntStatusFileSizeChState = _NtStatusFileSizeChState_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 13),
    _NtStatusFileSizeChState_Type()
)
ntStatusFileSizeChState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileSizeChState.setStatus("mandatory")
_NtStatusFileSizeChBytes_Type = Integer32
_NtStatusFileSizeChBytes_Object = MibTableColumn
ntStatusFileSizeChBytes = _NtStatusFileSizeChBytes_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 14),
    _NtStatusFileSizeChBytes_Type()
)
ntStatusFileSizeChBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileSizeChBytes.setStatus("mandatory")
_NtStatusFileMinSize_Type = Integer32
_NtStatusFileMinSize_Object = MibTableColumn
ntStatusFileMinSize = _NtStatusFileMinSize_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 15),
    _NtStatusFileMinSize_Type()
)
ntStatusFileMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileMinSize.setStatus("mandatory")
_NtStatusFileMaxSize_Type = Integer32
_NtStatusFileMaxSize_Object = MibTableColumn
ntStatusFileMaxSize = _NtStatusFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 16),
    _NtStatusFileMaxSize_Type()
)
ntStatusFileMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileMaxSize.setStatus("mandatory")
_NtStatusFileAvgSize_Type = Integer32
_NtStatusFileAvgSize_Object = MibTableColumn
ntStatusFileAvgSize = _NtStatusFileAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 17),
    _NtStatusFileAvgSize_Type()
)
ntStatusFileAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileAvgSize.setStatus("mandatory")
_NtStatusFileDescription_Type = DisplayString
_NtStatusFileDescription_Object = MibTableColumn
ntStatusFileDescription = _NtStatusFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 18),
    _NtStatusFileDescription_Type()
)
ntStatusFileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusFileDescription.setStatus("mandatory")
_NtStatusFileSizeBase_Type = Integer32
_NtStatusFileSizeBase_Object = MibTableColumn
ntStatusFileSizeBase = _NtStatusFileSizeBase_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 4, 2, 19),
    _NtStatusFileSizeBase_Type()
)
ntStatusFileSizeBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusFileSizeBase.setStatus("mandatory")
_NtProcessStTable_Object = MibTable
ntProcessStTable = _NtProcessStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    ntProcessStTable.setStatus("mandatory")
_NtProcessStTableEntry_Object = MibTableRow
ntProcessStTableEntry = _NtProcessStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2)
)
ntProcessStTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusProcName"),
)
if mibBuilder.loadTexts:
    ntProcessStTableEntry.setStatus("mandatory")
_NtStatusProcName_Type = DisplayString
_NtStatusProcName_Object = MibTableColumn
ntStatusProcName = _NtStatusProcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 2),
    _NtStatusProcName_Type()
)
ntStatusProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusProcName.setStatus("mandatory")


class _NtStatusProcStatus_Type(Integer32):
    """Custom type ntStatusProcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusProcStatus_Type.__name__ = "Integer32"
_NtStatusProcStatus_Object = MibTableColumn
ntStatusProcStatus = _NtStatusProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 3),
    _NtStatusProcStatus_Type()
)
ntStatusProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusProcStatus.setStatus("mandatory")


class _NtStatusProcAlertLevel_Type(Integer32):
    """Custom type ntStatusProcAlertLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtStatusProcAlertLevel_Type.__name__ = "Integer32"
_NtStatusProcAlertLevel_Object = MibTableColumn
ntStatusProcAlertLevel = _NtStatusProcAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 4),
    _NtStatusProcAlertLevel_Type()
)
ntStatusProcAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcAlertLevel.setStatus("mandatory")


class _NtStatusProcExist_Type(Integer32):
    """Custom type ntStatusProcExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alert-if-exist", 1),
          ("alert-if-not-exist", 2))
    )


_NtStatusProcExist_Type.__name__ = "Integer32"
_NtStatusProcExist_Object = MibTableColumn
ntStatusProcExist = _NtStatusProcExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 5),
    _NtStatusProcExist_Type()
)
ntStatusProcExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcExist.setStatus("mandatory")
_NtStatusProcInst_Type = Integer32
_NtStatusProcInst_Object = MibTableColumn
ntStatusProcInst = _NtStatusProcInst_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 6),
    _NtStatusProcInst_Type()
)
ntStatusProcInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusProcInst.setStatus("mandatory")


class _NtStatusProcInstMonitor_Type(Integer32):
    """Custom type ntStatusProcInstMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_NtStatusProcInstMonitor_Type.__name__ = "Integer32"
_NtStatusProcInstMonitor_Object = MibTableColumn
ntStatusProcInstMonitor = _NtStatusProcInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 7),
    _NtStatusProcInstMonitor_Type()
)
ntStatusProcInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcInstMonitor.setStatus("mandatory")
_NtStatusProcInstWarning_Type = Integer32
_NtStatusProcInstWarning_Object = MibTableColumn
ntStatusProcInstWarning = _NtStatusProcInstWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 8),
    _NtStatusProcInstWarning_Type()
)
ntStatusProcInstWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcInstWarning.setStatus("mandatory")
_NtStatusProcInstCritical_Type = Integer32
_NtStatusProcInstCritical_Object = MibTableColumn
ntStatusProcInstCritical = _NtStatusProcInstCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 9),
    _NtStatusProcInstCritical_Type()
)
ntStatusProcInstCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcInstCritical.setStatus("mandatory")
_NtStatusProcThd_Type = Integer32
_NtStatusProcThd_Object = MibTableColumn
ntStatusProcThd = _NtStatusProcThd_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 10),
    _NtStatusProcThd_Type()
)
ntStatusProcThd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusProcThd.setStatus("mandatory")


class _NtStatusProcThdMonitor_Type(Integer32):
    """Custom type ntStatusProcThdMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("above", 2),
          ("below", 3),
          ("do-not-monitor", 1))
    )


_NtStatusProcThdMonitor_Type.__name__ = "Integer32"
_NtStatusProcThdMonitor_Object = MibTableColumn
ntStatusProcThdMonitor = _NtStatusProcThdMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 11),
    _NtStatusProcThdMonitor_Type()
)
ntStatusProcThdMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcThdMonitor.setStatus("mandatory")
_NtStatusProcThdRef_Type = Integer32
_NtStatusProcThdRef_Object = MibTableColumn
ntStatusProcThdRef = _NtStatusProcThdRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 12),
    _NtStatusProcThdRef_Type()
)
ntStatusProcThdRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcThdRef.setStatus("mandatory")
_NtStatusProcThdMax_Type = Integer32
_NtStatusProcThdMax_Object = MibTableColumn
ntStatusProcThdMax = _NtStatusProcThdMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 13),
    _NtStatusProcThdMax_Type()
)
ntStatusProcThdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusProcThdMax.setStatus("mandatory")
_NtStatusProcThdMin_Type = Integer32
_NtStatusProcThdMin_Object = MibTableColumn
ntStatusProcThdMin = _NtStatusProcThdMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 14),
    _NtStatusProcThdMin_Type()
)
ntStatusProcThdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusProcThdMin.setStatus("mandatory")
_NtStatusProcDescription_Type = DisplayString
_NtStatusProcDescription_Object = MibTableColumn
ntStatusProcDescription = _NtStatusProcDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 5, 2, 17),
    _NtStatusProcDescription_Type()
)
ntStatusProcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusProcDescription.setStatus("mandatory")
_NtServiceStTable_Object = MibTable
ntServiceStTable = _NtServiceStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    ntServiceStTable.setStatus("mandatory")
_NtServiceStTableEntry_Object = MibTableRow
ntServiceStTableEntry = _NtServiceStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6, 2)
)
ntServiceStTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusServName"),
)
if mibBuilder.loadTexts:
    ntServiceStTableEntry.setStatus("mandatory")
_NtStatusServName_Type = DisplayString
_NtStatusServName_Object = MibTableColumn
ntStatusServName = _NtStatusServName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6, 2, 2),
    _NtStatusServName_Type()
)
ntStatusServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusServName.setStatus("mandatory")
_NtStatusServDescription_Type = DisplayString
_NtStatusServDescription_Object = MibTableColumn
ntStatusServDescription = _NtStatusServDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6, 2, 3),
    _NtStatusServDescription_Type()
)
ntStatusServDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusServDescription.setStatus("mandatory")


class _NtStatusServState_Type(Integer32):
    """Custom type ntStatusServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("continue-pending", 5),
          ("pause-pending", 6),
          ("paused", 7),
          ("running", 4),
          ("start-pending", 2),
          ("stop-pending", 3),
          ("stopped", 1),
          ("unknown", 8))
    )


_NtStatusServState_Type.__name__ = "Integer32"
_NtStatusServState_Object = MibTableColumn
ntStatusServState = _NtStatusServState_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6, 2, 4),
    _NtStatusServState_Type()
)
ntStatusServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusServState.setStatus("mandatory")


class _NtStatusServStatus_Type(Integer32):
    """Custom type ntStatusServStatus based on Integer32"""
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
        *(("critical", 3),
          ("down", 4),
          ("ok", 1),
          ("unknown", 5),
          ("warning", 2))
    )


_NtStatusServStatus_Type.__name__ = "Integer32"
_NtStatusServStatus_Object = MibTableColumn
ntStatusServStatus = _NtStatusServStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6, 2, 5),
    _NtStatusServStatus_Type()
)
ntStatusServStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusServStatus.setStatus("mandatory")


class _NtStatusServAlertOn_Type(Integer32):
    """Custom type ntStatusServAlertOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("do-not-monitor", 1),
          ("inactive", 3))
    )


_NtStatusServAlertOn_Type.__name__ = "Integer32"
_NtStatusServAlertOn_Object = MibTableColumn
ntStatusServAlertOn = _NtStatusServAlertOn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 6, 2, 6),
    _NtStatusServAlertOn_Type()
)
ntStatusServAlertOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusServAlertOn.setStatus("mandatory")
_NtPrinterStTable_Object = MibTable
ntPrinterStTable = _NtPrinterStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    ntPrinterStTable.setStatus("mandatory")
_NtStatusPrintTableEntry_Object = MibTableRow
ntStatusPrintTableEntry = _NtStatusPrintTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2)
)
ntStatusPrintTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusPrintName"),
)
if mibBuilder.loadTexts:
    ntStatusPrintTableEntry.setStatus("mandatory")
_NtStatusPrintName_Type = DisplayString
_NtStatusPrintName_Object = MibTableColumn
ntStatusPrintName = _NtStatusPrintName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 2),
    _NtStatusPrintName_Type()
)
ntStatusPrintName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintName.setStatus("mandatory")


class _NtStatusPrintStatus_Type(Integer32):
    """Custom type ntStatusPrintStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusPrintStatus_Type.__name__ = "Integer32"
_NtStatusPrintStatus_Object = MibTableColumn
ntStatusPrintStatus = _NtStatusPrintStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 3),
    _NtStatusPrintStatus_Type()
)
ntStatusPrintStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintStatus.setStatus("mandatory")


class _NtStatusPrintEventMonitor_Type(Integer32):
    """Custom type ntStatusPrintEventMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("warning", 2))
    )


_NtStatusPrintEventMonitor_Type.__name__ = "Integer32"
_NtStatusPrintEventMonitor_Object = MibTableColumn
ntStatusPrintEventMonitor = _NtStatusPrintEventMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 4),
    _NtStatusPrintEventMonitor_Type()
)
ntStatusPrintEventMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusPrintEventMonitor.setStatus("mandatory")


class _NtStatusPrintEventStatus_Type(Integer32):
    """Custom type ntStatusPrintEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusPrintEventStatus_Type.__name__ = "Integer32"
_NtStatusPrintEventStatus_Object = MibTableColumn
ntStatusPrintEventStatus = _NtStatusPrintEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 5),
    _NtStatusPrintEventStatus_Type()
)
ntStatusPrintEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintEventStatus.setStatus("mandatory")
_NtStatusPrintEventDescription_Type = DisplayString
_NtStatusPrintEventDescription_Object = MibTableColumn
ntStatusPrintEventDescription = _NtStatusPrintEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 6),
    _NtStatusPrintEventDescription_Type()
)
ntStatusPrintEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintEventDescription.setStatus("mandatory")


class _NtStatusPrintQFlag_Type(Integer32):
    """Custom type ntStatusPrintQFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_NtStatusPrintQFlag_Type.__name__ = "Integer32"
_NtStatusPrintQFlag_Object = MibTableColumn
ntStatusPrintQFlag = _NtStatusPrintQFlag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 7),
    _NtStatusPrintQFlag_Type()
)
ntStatusPrintQFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusPrintQFlag.setStatus("mandatory")
_NtStatusPrintQueue_Type = Integer32
_NtStatusPrintQueue_Object = MibTableColumn
ntStatusPrintQueue = _NtStatusPrintQueue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 8),
    _NtStatusPrintQueue_Type()
)
ntStatusPrintQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintQueue.setStatus("mandatory")


class _NtStatusPrintQStatus_Type(Integer32):
    """Custom type ntStatusPrintQStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusPrintQStatus_Type.__name__ = "Integer32"
_NtStatusPrintQStatus_Object = MibTableColumn
ntStatusPrintQStatus = _NtStatusPrintQStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 9),
    _NtStatusPrintQStatus_Type()
)
ntStatusPrintQStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintQStatus.setStatus("mandatory")
_NtStatusPrintQWarning_Type = Integer32
_NtStatusPrintQWarning_Object = MibTableColumn
ntStatusPrintQWarning = _NtStatusPrintQWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 10),
    _NtStatusPrintQWarning_Type()
)
ntStatusPrintQWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusPrintQWarning.setStatus("mandatory")
_NtStatusPrintQCritical_Type = Integer32
_NtStatusPrintQCritical_Object = MibTableColumn
ntStatusPrintQCritical = _NtStatusPrintQCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 11),
    _NtStatusPrintQCritical_Type()
)
ntStatusPrintQCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusPrintQCritical.setStatus("mandatory")
_NtStatusPrintQMax_Type = Integer32
_NtStatusPrintQMax_Object = MibTableColumn
ntStatusPrintQMax = _NtStatusPrintQMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 12),
    _NtStatusPrintQMax_Type()
)
ntStatusPrintQMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusPrintQMax.setStatus("mandatory")
_NtStatusPrintDescription_Type = DisplayString
_NtStatusPrintDescription_Object = MibTableColumn
ntStatusPrintDescription = _NtStatusPrintDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 7, 2, 13),
    _NtStatusPrintDescription_Type()
)
ntStatusPrintDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusPrintDescription.setStatus("mandatory")
_NtMemorySt_ObjectIdentity = ObjectIdentity
ntMemorySt = _NtMemorySt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8)
)
_NtStatusMemLoad_Type = Integer32
_NtStatusMemLoad_Object = MibScalar
ntStatusMemLoad = _NtStatusMemLoad_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 2),
    _NtStatusMemLoad_Type()
)
ntStatusMemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemLoad.setStatus("mandatory")


class _NtStatusMemLoadStatus_Type(Integer32):
    """Custom type ntStatusMemLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusMemLoadStatus_Type.__name__ = "Integer32"
_NtStatusMemLoadStatus_Object = MibScalar
ntStatusMemLoadStatus = _NtStatusMemLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 3),
    _NtStatusMemLoadStatus_Type()
)
ntStatusMemLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemLoadStatus.setStatus("mandatory")
_NtStatusMemLoadAvg_Type = Integer32
_NtStatusMemLoadAvg_Object = MibScalar
ntStatusMemLoadAvg = _NtStatusMemLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 4),
    _NtStatusMemLoadAvg_Type()
)
ntStatusMemLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemLoadAvg.setStatus("mandatory")
_NtStatusMemLoadMax_Type = Integer32
_NtStatusMemLoadMax_Object = MibScalar
ntStatusMemLoadMax = _NtStatusMemLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 5),
    _NtStatusMemLoadMax_Type()
)
ntStatusMemLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemLoadMax.setStatus("mandatory")
_NtStatusMemLoadMin_Type = Integer32
_NtStatusMemLoadMin_Object = MibScalar
ntStatusMemLoadMin = _NtStatusMemLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 6),
    _NtStatusMemLoadMin_Type()
)
ntStatusMemLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemLoadMin.setStatus("mandatory")
_NtStatusMemPhysTotal_Type = Integer32
_NtStatusMemPhysTotal_Object = MibScalar
ntStatusMemPhysTotal = _NtStatusMemPhysTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 7),
    _NtStatusMemPhysTotal_Type()
)
ntStatusMemPhysTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemPhysTotal.setStatus("mandatory")
_NtStatusMemPhys_Type = Integer32
_NtStatusMemPhys_Object = MibScalar
ntStatusMemPhys = _NtStatusMemPhys_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 8),
    _NtStatusMemPhys_Type()
)
ntStatusMemPhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemPhys.setStatus("mandatory")


class _NtStatusMemPhysStatus_Type(Integer32):
    """Custom type ntStatusMemPhysStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusMemPhysStatus_Type.__name__ = "Integer32"
_NtStatusMemPhysStatus_Object = MibScalar
ntStatusMemPhysStatus = _NtStatusMemPhysStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 9),
    _NtStatusMemPhysStatus_Type()
)
ntStatusMemPhysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemPhysStatus.setStatus("mandatory")
_NtStatusMemPhysAvg_Type = Integer32
_NtStatusMemPhysAvg_Object = MibScalar
ntStatusMemPhysAvg = _NtStatusMemPhysAvg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 10),
    _NtStatusMemPhysAvg_Type()
)
ntStatusMemPhysAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemPhysAvg.setStatus("mandatory")
_NtStatusMemPhysMax_Type = Integer32
_NtStatusMemPhysMax_Object = MibScalar
ntStatusMemPhysMax = _NtStatusMemPhysMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 11),
    _NtStatusMemPhysMax_Type()
)
ntStatusMemPhysMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemPhysMax.setStatus("mandatory")
_NtStatusMemPhysMin_Type = Integer32
_NtStatusMemPhysMin_Object = MibScalar
ntStatusMemPhysMin = _NtStatusMemPhysMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 12),
    _NtStatusMemPhysMin_Type()
)
ntStatusMemPhysMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemPhysMin.setStatus("mandatory")
_NtStatusMemSwapTotal_Type = Integer32
_NtStatusMemSwapTotal_Object = MibScalar
ntStatusMemSwapTotal = _NtStatusMemSwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 13),
    _NtStatusMemSwapTotal_Type()
)
ntStatusMemSwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemSwapTotal.setStatus("mandatory")
_NtStatusMemSwap_Type = Integer32
_NtStatusMemSwap_Object = MibScalar
ntStatusMemSwap = _NtStatusMemSwap_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 14),
    _NtStatusMemSwap_Type()
)
ntStatusMemSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemSwap.setStatus("mandatory")


class _NtStatusMemSwapStatus_Type(Integer32):
    """Custom type ntStatusMemSwapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusMemSwapStatus_Type.__name__ = "Integer32"
_NtStatusMemSwapStatus_Object = MibScalar
ntStatusMemSwapStatus = _NtStatusMemSwapStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 15),
    _NtStatusMemSwapStatus_Type()
)
ntStatusMemSwapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemSwapStatus.setStatus("mandatory")
_NtStatusMemSwapAvg_Type = Integer32
_NtStatusMemSwapAvg_Object = MibScalar
ntStatusMemSwapAvg = _NtStatusMemSwapAvg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 16),
    _NtStatusMemSwapAvg_Type()
)
ntStatusMemSwapAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemSwapAvg.setStatus("mandatory")
_NtStatusMemSwapMax_Type = Integer32
_NtStatusMemSwapMax_Object = MibScalar
ntStatusMemSwapMax = _NtStatusMemSwapMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 17),
    _NtStatusMemSwapMax_Type()
)
ntStatusMemSwapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemSwapMax.setStatus("mandatory")
_NtStatusMemSwapMin_Type = Integer32
_NtStatusMemSwapMin_Object = MibScalar
ntStatusMemSwapMin = _NtStatusMemSwapMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 8, 18),
    _NtStatusMemSwapMin_Type()
)
ntStatusMemSwapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusMemSwapMin.setStatus("mandatory")
_NtProcessorStTable_Object = MibTable
ntProcessorStTable = _NtProcessorStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9)
)
if mibBuilder.loadTexts:
    ntProcessorStTable.setStatus("mandatory")
_NtProcessorStTableEntry_Object = MibTableRow
ntProcessorStTableEntry = _NtProcessorStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2)
)
ntProcessorStTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusCPUNumber"),
)
if mibBuilder.loadTexts:
    ntProcessorStTableEntry.setStatus("mandatory")
_NtStatusCPUNumber_Type = DisplayString
_NtStatusCPUNumber_Object = MibTableColumn
ntStatusCPUNumber = _NtStatusCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 2),
    _NtStatusCPUNumber_Type()
)
ntStatusCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUNumber.setStatus("mandatory")


class _NtStatusCPUStatus_Type(Integer32):
    """Custom type ntStatusCPUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("warning", 2))
    )


_NtStatusCPUStatus_Type.__name__ = "Integer32"
_NtStatusCPUStatus_Object = MibTableColumn
ntStatusCPUStatus = _NtStatusCPUStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 3),
    _NtStatusCPUStatus_Type()
)
ntStatusCPUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUStatus.setStatus("mandatory")
_NtStatusCPUTotal_Type = Integer32
_NtStatusCPUTotal_Object = MibTableColumn
ntStatusCPUTotal = _NtStatusCPUTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 4),
    _NtStatusCPUTotal_Type()
)
ntStatusCPUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUTotal.setStatus("mandatory")
_NtStatusCPUWarning_Type = Integer32
_NtStatusCPUWarning_Object = MibTableColumn
ntStatusCPUWarning = _NtStatusCPUWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 5),
    _NtStatusCPUWarning_Type()
)
ntStatusCPUWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusCPUWarning.setStatus("mandatory")
_NtStatusCPUCritical_Type = Integer32
_NtStatusCPUCritical_Object = MibTableColumn
ntStatusCPUCritical = _NtStatusCPUCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 6),
    _NtStatusCPUCritical_Type()
)
ntStatusCPUCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusCPUCritical.setStatus("mandatory")
_NtStatusCPUCount_Type = Integer32
_NtStatusCPUCount_Object = MibTableColumn
ntStatusCPUCount = _NtStatusCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 7),
    _NtStatusCPUCount_Type()
)
ntStatusCPUCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusCPUCount.setStatus("mandatory")
_NtStatusCPUAvg_Type = Integer32
_NtStatusCPUAvg_Object = MibTableColumn
ntStatusCPUAvg = _NtStatusCPUAvg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 8),
    _NtStatusCPUAvg_Type()
)
ntStatusCPUAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUAvg.setStatus("mandatory")
_NtStatusCPUMax_Type = Integer32
_NtStatusCPUMax_Object = MibTableColumn
ntStatusCPUMax = _NtStatusCPUMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 9),
    _NtStatusCPUMax_Type()
)
ntStatusCPUMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUMax.setStatus("mandatory")
_NtStatusCPUMin_Type = Integer32
_NtStatusCPUMin_Object = MibTableColumn
ntStatusCPUMin = _NtStatusCPUMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 10),
    _NtStatusCPUMin_Type()
)
ntStatusCPUMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUMin.setStatus("mandatory")
_NtStatusCPUDelta_Type = Integer32
_NtStatusCPUDelta_Object = MibTableColumn
ntStatusCPUDelta = _NtStatusCPUDelta_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 11),
    _NtStatusCPUDelta_Type()
)
ntStatusCPUDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusCPUDelta.setStatus("mandatory")
_NtStatusCPUDescription_Type = DisplayString
_NtStatusCPUDescription_Object = MibTableColumn
ntStatusCPUDescription = _NtStatusCPUDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 9, 2, 12),
    _NtStatusCPUDescription_Type()
)
ntStatusCPUDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusCPUDescription.setStatus("mandatory")
_NtRegistryStTable_Object = MibTable
ntRegistryStTable = _NtRegistryStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    ntRegistryStTable.setStatus("mandatory")
_NtRegistryStTableEntry_Object = MibTableRow
ntRegistryStTableEntry = _NtRegistryStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2)
)
ntRegistryStTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntStatusRegHandle"),
    (0, "CA-NTOS-MIB", "ntStatusRegKey"),
    (0, "CA-NTOS-MIB", "ntStatusRegLeaf"),
)
if mibBuilder.loadTexts:
    ntRegistryStTableEntry.setStatus("mandatory")


class _NtStatusRegHandle_Type(Integer32):
    """Custom type ntStatusRegHandle based on Integer32"""
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
        *(("hkey-classes-root", 4),
          ("hkey-current-user", 2),
          ("hkey-local-machine", 1),
          ("hkey-users", 3))
    )


_NtStatusRegHandle_Type.__name__ = "Integer32"
_NtStatusRegHandle_Object = MibTableColumn
ntStatusRegHandle = _NtStatusRegHandle_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 1),
    _NtStatusRegHandle_Type()
)
ntStatusRegHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegHandle.setStatus("mandatory")
_NtStatusRegKey_Type = DisplayString
_NtStatusRegKey_Object = MibTableColumn
ntStatusRegKey = _NtStatusRegKey_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 2),
    _NtStatusRegKey_Type()
)
ntStatusRegKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegKey.setStatus("mandatory")
_NtStatusRegLeaf_Type = DisplayString
_NtStatusRegLeaf_Object = MibTableColumn
ntStatusRegLeaf = _NtStatusRegLeaf_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 3),
    _NtStatusRegLeaf_Type()
)
ntStatusRegLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegLeaf.setStatus("mandatory")


class _NtStatusRegDataType_Type(Integer32):
    """Custom type ntStatusRegDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("integer", 1),
          ("string", 2))
    )


_NtStatusRegDataType_Type.__name__ = "Integer32"
_NtStatusRegDataType_Object = MibTableColumn
ntStatusRegDataType = _NtStatusRegDataType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 4),
    _NtStatusRegDataType_Type()
)
ntStatusRegDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegDataType.setStatus("mandatory")
_NtStatusRegValue_Type = DisplayString
_NtStatusRegValue_Object = MibTableColumn
ntStatusRegValue = _NtStatusRegValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 5),
    _NtStatusRegValue_Type()
)
ntStatusRegValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegValue.setStatus("mandatory")
_NtStatusRegPrevValue_Type = DisplayString
_NtStatusRegPrevValue_Object = MibTableColumn
ntStatusRegPrevValue = _NtStatusRegPrevValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 6),
    _NtStatusRegPrevValue_Type()
)
ntStatusRegPrevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegPrevValue.setStatus("mandatory")


class _NtStatusRegStatus_Type(Integer32):
    """Custom type ntStatusRegStatus based on Integer32"""
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
        *(("critical", 3),
          ("ok", 1),
          ("reset", 4),
          ("warning", 2))
    )


_NtStatusRegStatus_Type.__name__ = "Integer32"
_NtStatusRegStatus_Object = MibTableColumn
ntStatusRegStatus = _NtStatusRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 7),
    _NtStatusRegStatus_Type()
)
ntStatusRegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusRegStatus.setStatus("mandatory")
_NtStatusRegAvgTicks_Type = Integer32
_NtStatusRegAvgTicks_Object = MibTableColumn
ntStatusRegAvgTicks = _NtStatusRegAvgTicks_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 8),
    _NtStatusRegAvgTicks_Type()
)
ntStatusRegAvgTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegAvgTicks.setStatus("optional")
_NtStatusRegAvg_Type = Integer32
_NtStatusRegAvg_Object = MibTableColumn
ntStatusRegAvg = _NtStatusRegAvg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 9),
    _NtStatusRegAvg_Type()
)
ntStatusRegAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegAvg.setStatus("optional")
_NtStatusRegMax_Type = Integer32
_NtStatusRegMax_Object = MibTableColumn
ntStatusRegMax = _NtStatusRegMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 10),
    _NtStatusRegMax_Type()
)
ntStatusRegMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegMax.setStatus("optional")
_NtStatusRegMin_Type = Integer32
_NtStatusRegMin_Object = MibTableColumn
ntStatusRegMin = _NtStatusRegMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 11),
    _NtStatusRegMin_Type()
)
ntStatusRegMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusRegMin.setStatus("optional")


class _NtStatusRegMonitorLevel_Type(Integer32):
    """Custom type ntStatusRegMonitorLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("change", 2),
          ("do-not-monitor", 1),
          ("thresholds", 3))
    )


_NtStatusRegMonitorLevel_Type.__name__ = "Integer32"
_NtStatusRegMonitorLevel_Object = MibTableColumn
ntStatusRegMonitorLevel = _NtStatusRegMonitorLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 12),
    _NtStatusRegMonitorLevel_Type()
)
ntStatusRegMonitorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusRegMonitorLevel.setStatus("mandatory")
_NtStatusRegWarning_Type = Integer32
_NtStatusRegWarning_Object = MibScalar
ntStatusRegWarning = _NtStatusRegWarning_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 13),
    _NtStatusRegWarning_Type()
)
ntStatusRegWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusRegWarning.setStatus("mandatory")
_NtStatusRegCritical_Type = Integer32
_NtStatusRegCritical_Object = MibScalar
ntStatusRegCritical = _NtStatusRegCritical_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 10, 2, 14),
    _NtStatusRegCritical_Type()
)
ntStatusRegCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusRegCritical.setStatus("mandatory")
_NtEventLogStTable_Object = MibTable
ntEventLogStTable = _NtEventLogStTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    ntEventLogStTable.setStatus("mandatory")
_NtEventLogStTableEntry_Object = MibTableRow
ntEventLogStTableEntry = _NtEventLogStTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2)
)
if mibBuilder.loadTexts:
    ntEventLogStTableEntry.setStatus("mandatory")
_NtStatusLogLogs_Type = DisplayString
_NtStatusLogLogs_Object = MibTableColumn
ntStatusLogLogs = _NtStatusLogLogs_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 1),
    _NtStatusLogLogs_Type()
)
ntStatusLogLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogLogs.setStatus("mandatory")
_NtStatusLogSeverity_Type = DisplayString
_NtStatusLogSeverity_Object = MibTableColumn
ntStatusLogSeverity = _NtStatusLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 2),
    _NtStatusLogSeverity_Type()
)
ntStatusLogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogSeverity.setStatus("mandatory")
_NtStatusLogSource_Type = DisplayString
_NtStatusLogSource_Object = MibTableColumn
ntStatusLogSource = _NtStatusLogSource_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 3),
    _NtStatusLogSource_Type()
)
ntStatusLogSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogSource.setStatus("mandatory")
_NtStatusLogEventID_Type = DisplayString
_NtStatusLogEventID_Object = MibTableColumn
ntStatusLogEventID = _NtStatusLogEventID_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 4),
    _NtStatusLogEventID_Type()
)
ntStatusLogEventID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogEventID.setStatus("mandatory")
_NtStatusLogUser_Type = DisplayString
_NtStatusLogUser_Object = MibTableColumn
ntStatusLogUser = _NtStatusLogUser_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 5),
    _NtStatusLogUser_Type()
)
ntStatusLogUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogUser.setStatus("mandatory")
_NtStatusLogComputer_Type = DisplayString
_NtStatusLogComputer_Object = MibTableColumn
ntStatusLogComputer = _NtStatusLogComputer_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 6),
    _NtStatusLogComputer_Type()
)
ntStatusLogComputer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogComputer.setStatus("mandatory")


class _NtStatusLogStatus_Type(Integer32):
    """Custom type ntStatusLogStatus based on Integer32"""
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
        *(("critical", 3),
          ("ok", 1),
          ("reset", 4),
          ("warning", 2))
    )


_NtStatusLogStatus_Type.__name__ = "Integer32"
_NtStatusLogStatus_Object = MibTableColumn
ntStatusLogStatus = _NtStatusLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 7),
    _NtStatusLogStatus_Type()
)
ntStatusLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogStatus.setStatus("mandatory")


class _NtStatusLogAlertOn_Type(Integer32):
    """Custom type ntStatusLogAlertOn based on Integer32"""
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
        *(("critical", 3),
          ("do-not-monitor", 1),
          ("remove-watcher", 4),
          ("warning", 2))
    )


_NtStatusLogAlertOn_Type.__name__ = "Integer32"
_NtStatusLogAlertOn_Object = MibTableColumn
ntStatusLogAlertOn = _NtStatusLogAlertOn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 8),
    _NtStatusLogAlertOn_Type()
)
ntStatusLogAlertOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogAlertOn.setStatus("mandatory")
_NtStatusLogStartTime_Type = Integer32
_NtStatusLogStartTime_Object = MibTableColumn
ntStatusLogStartTime = _NtStatusLogStartTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 9),
    _NtStatusLogStartTime_Type()
)
ntStatusLogStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogStartTime.setStatus("mandatory")
_NtStatusLogStartTimeInText_Type = DisplayString
_NtStatusLogStartTimeInText_Object = MibTableColumn
ntStatusLogStartTimeInText = _NtStatusLogStartTimeInText_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 10),
    _NtStatusLogStartTimeInText_Type()
)
ntStatusLogStartTimeInText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogStartTimeInText.setStatus("mandatory")
_NtStatusLogAppLogMatches_Type = Integer32
_NtStatusLogAppLogMatches_Object = MibTableColumn
ntStatusLogAppLogMatches = _NtStatusLogAppLogMatches_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 11),
    _NtStatusLogAppLogMatches_Type()
)
ntStatusLogAppLogMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogAppLogMatches.setStatus("mandatory")
_NtStatusLogAppLogLastMatch_Type = DisplayString
_NtStatusLogAppLogLastMatch_Object = MibTableColumn
ntStatusLogAppLogLastMatch = _NtStatusLogAppLogLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 12),
    _NtStatusLogAppLogLastMatch_Type()
)
ntStatusLogAppLogLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogAppLogLastMatch.setStatus("mandatory")
_NtStatusLogSecLogMatches_Type = Integer32
_NtStatusLogSecLogMatches_Object = MibTableColumn
ntStatusLogSecLogMatches = _NtStatusLogSecLogMatches_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 13),
    _NtStatusLogSecLogMatches_Type()
)
ntStatusLogSecLogMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogSecLogMatches.setStatus("mandatory")
_NtStatusLogSecLogLastMatch_Type = DisplayString
_NtStatusLogSecLogLastMatch_Object = MibTableColumn
ntStatusLogSecLogLastMatch = _NtStatusLogSecLogLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 14),
    _NtStatusLogSecLogLastMatch_Type()
)
ntStatusLogSecLogLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogSecLogLastMatch.setStatus("mandatory")
_NtStatusLogSysLogMatches_Type = DisplayString
_NtStatusLogSysLogMatches_Object = MibTableColumn
ntStatusLogSysLogMatches = _NtStatusLogSysLogMatches_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 15),
    _NtStatusLogSysLogMatches_Type()
)
ntStatusLogSysLogMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogSysLogMatches.setStatus("mandatory")
_NtStatusLogSysLogLastMatch_Type = DisplayString
_NtStatusLogSysLogLastMatch_Object = MibTableColumn
ntStatusLogSysLogLastMatch = _NtStatusLogSysLogLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 16),
    _NtStatusLogSysLogLastMatch_Type()
)
ntStatusLogSysLogLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogSysLogLastMatch.setStatus("mandatory")
_NtStatusLogWatcherIndex_Type = Integer32
_NtStatusLogWatcherIndex_Object = MibTableColumn
ntStatusLogWatcherIndex = _NtStatusLogWatcherIndex_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 17),
    _NtStatusLogWatcherIndex_Type()
)
ntStatusLogWatcherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntStatusLogWatcherIndex.setStatus("mandatory")
_NtStatusLogDescription_Type = DisplayString
_NtStatusLogDescription_Object = MibTableColumn
ntStatusLogDescription = _NtStatusLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 3, 11, 2, 18),
    _NtStatusLogDescription_Type()
)
ntStatusLogDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntStatusLogDescription.setStatus("mandatory")
_NtPollGroup_ObjectIdentity = ObjectIdentity
ntPollGroup = _NtPollGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4)
)
_NtFilesystemPollTable_Object = MibTable
ntFilesystemPollTable = _NtFilesystemPollTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ntFilesystemPollTable.setStatus("mandatory")
_NtFilesystemPollTableEntry_Object = MibTableRow
ntFilesystemPollTableEntry = _NtFilesystemPollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2)
)
ntFilesystemPollTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntFsysDriveLetter"),
)
if mibBuilder.loadTexts:
    ntFilesystemPollTableEntry.setStatus("mandatory")
_NtFsysDriveLetter_Type = DisplayString
_NtFsysDriveLetter_Object = MibTableColumn
ntFsysDriveLetter = _NtFsysDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 2),
    _NtFsysDriveLetter_Type()
)
ntFsysDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysDriveLetter.setStatus("mandatory")
_NtFsysTotalCapacity_Type = Integer32
_NtFsysTotalCapacity_Object = MibTableColumn
ntFsysTotalCapacity = _NtFsysTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 3),
    _NtFsysTotalCapacity_Type()
)
ntFsysTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysTotalCapacity.setStatus("mandatory")
_NtFsysFree_Type = Integer32
_NtFsysFree_Object = MibTableColumn
ntFsysFree = _NtFsysFree_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 4),
    _NtFsysFree_Type()
)
ntFsysFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysFree.setStatus("mandatory")
_NtFsysUtilization_Type = Integer32
_NtFsysUtilization_Object = MibTableColumn
ntFsysUtilization = _NtFsysUtilization_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 5),
    _NtFsysUtilization_Type()
)
ntFsysUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysUtilization.setStatus("mandatory")
_NtFsysLastUtilization_Type = Integer32
_NtFsysLastUtilization_Object = MibTableColumn
ntFsysLastUtilization = _NtFsysLastUtilization_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 6),
    _NtFsysLastUtilization_Type()
)
ntFsysLastUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysLastUtilization.setStatus("mandatory")
_NtFsysAverage_Type = Integer32
_NtFsysAverage_Object = MibTableColumn
ntFsysAverage = _NtFsysAverage_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 7),
    _NtFsysAverage_Type()
)
ntFsysAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysAverage.setStatus("mandatory")
_NtFsysAvgTicks_Type = Integer32
_NtFsysAvgTicks_Object = MibTableColumn
ntFsysAvgTicks = _NtFsysAvgTicks_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 2, 2, 8),
    _NtFsysAvgTicks_Type()
)
ntFsysAvgTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFsysAvgTicks.setStatus("mandatory")
_NtFilePollTable_Object = MibTable
ntFilePollTable = _NtFilePollTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    ntFilePollTable.setStatus("mandatory")
_NtFilePollTableEntry_Object = MibTableRow
ntFilePollTableEntry = _NtFilePollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2)
)
ntFilePollTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntFileName"),
)
if mibBuilder.loadTexts:
    ntFilePollTableEntry.setStatus("mandatory")
_NtFileName_Type = DisplayString
_NtFileName_Object = MibTableColumn
ntFileName = _NtFileName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 2),
    _NtFileName_Type()
)
ntFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileName.setStatus("mandatory")
_NtFileTimestamp_Type = DisplayString
_NtFileTimestamp_Object = MibTableColumn
ntFileTimestamp = _NtFileTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 3),
    _NtFileTimestamp_Type()
)
ntFileTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileTimestamp.setStatus("mandatory")
_NtFileRefTimestamp_Type = DisplayString
_NtFileRefTimestamp_Object = MibTableColumn
ntFileRefTimestamp = _NtFileRefTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 4),
    _NtFileRefTimestamp_Type()
)
ntFileRefTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileRefTimestamp.setStatus("mandatory")
_NtFileSize_Type = Integer32
_NtFileSize_Object = MibTableColumn
ntFileSize = _NtFileSize_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 5),
    _NtFileSize_Type()
)
ntFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileSize.setStatus("mandatory")
_NtFileSizeChangeReference_Type = Integer32
_NtFileSizeChangeReference_Object = MibTableColumn
ntFileSizeChangeReference = _NtFileSizeChangeReference_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 6),
    _NtFileSizeChangeReference_Type()
)
ntFileSizeChangeReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileSizeChangeReference.setStatus("mandatory")
_NtFileSizeChangeCount_Type = Integer32
_NtFileSizeChangeCount_Object = MibTableColumn
ntFileSizeChangeCount = _NtFileSizeChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 7),
    _NtFileSizeChangeCount_Type()
)
ntFileSizeChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileSizeChangeCount.setStatus("mandatory")
_NtFileSizeAvgTicks_Type = Integer32
_NtFileSizeAvgTicks_Object = MibTableColumn
ntFileSizeAvgTicks = _NtFileSizeAvgTicks_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 3, 2, 8),
    _NtFileSizeAvgTicks_Type()
)
ntFileSizeAvgTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileSizeAvgTicks.setStatus("mandatory")
_NtProcessPollTable_Object = MibTable
ntProcessPollTable = _NtProcessPollTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    ntProcessPollTable.setStatus("mandatory")
_NtProcessPollTableEntry_Object = MibTableRow
ntProcessPollTableEntry = _NtProcessPollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 4, 2)
)
ntProcessPollTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntProcessName"),
)
if mibBuilder.loadTexts:
    ntProcessPollTableEntry.setStatus("mandatory")
_NtProcessName_Type = DisplayString
_NtProcessName_Object = MibTableColumn
ntProcessName = _NtProcessName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 4, 2, 2),
    _NtProcessName_Type()
)
ntProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessName.setStatus("mandatory")
_NtProcessInstCount_Type = Integer32
_NtProcessInstCount_Object = MibTableColumn
ntProcessInstCount = _NtProcessInstCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 4, 2, 3),
    _NtProcessInstCount_Type()
)
ntProcessInstCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessInstCount.setStatus("mandatory")
_NtProcessMaxThread_Type = Integer32
_NtProcessMaxThread_Object = MibTableColumn
ntProcessMaxThread = _NtProcessMaxThread_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 4, 2, 4),
    _NtProcessMaxThread_Type()
)
ntProcessMaxThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessMaxThread.setStatus("mandatory")
_NtProcessMinThread_Type = Integer32
_NtProcessMinThread_Object = MibTableColumn
ntProcessMinThread = _NtProcessMinThread_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 4, 2, 5),
    _NtProcessMinThread_Type()
)
ntProcessMinThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntProcessMinThread.setStatus("mandatory")
_NtProcessorPollTable_Object = MibTable
ntProcessorPollTable = _NtProcessorPollTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    ntProcessorPollTable.setStatus("mandatory")
_NtProcessorPollTableEntry_Object = MibTableRow
ntProcessorPollTableEntry = _NtProcessorPollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2)
)
ntProcessorPollTableEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntCPUNumber"),
)
if mibBuilder.loadTexts:
    ntProcessorPollTableEntry.setStatus("mandatory")
_NtCPUNumber_Type = DisplayString
_NtCPUNumber_Object = MibTableColumn
ntCPUNumber = _NtCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 3),
    _NtCPUNumber_Type()
)
ntCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUNumber.setStatus("mandatory")
_NtCPUDPCTime_Type = Integer32
_NtCPUDPCTime_Object = MibTableColumn
ntCPUDPCTime = _NtCPUDPCTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 4),
    _NtCPUDPCTime_Type()
)
ntCPUDPCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUDPCTime.setStatus("mandatory")
_NtCPUInterruptTime_Type = Integer32
_NtCPUInterruptTime_Object = MibTableColumn
ntCPUInterruptTime = _NtCPUInterruptTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 5),
    _NtCPUInterruptTime_Type()
)
ntCPUInterruptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUInterruptTime.setStatus("mandatory")
_NtCPUPrivilegedTime_Type = Integer32
_NtCPUPrivilegedTime_Object = MibTableColumn
ntCPUPrivilegedTime = _NtCPUPrivilegedTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 6),
    _NtCPUPrivilegedTime_Type()
)
ntCPUPrivilegedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUPrivilegedTime.setStatus("mandatory")
_NtCPUProcessorTime_Type = Integer32
_NtCPUProcessorTime_Object = MibTableColumn
ntCPUProcessorTime = _NtCPUProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 7),
    _NtCPUProcessorTime_Type()
)
ntCPUProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUProcessorTime.setStatus("mandatory")
_NtCPUUserTime_Type = Integer32
_NtCPUUserTime_Object = MibTableColumn
ntCPUUserTime = _NtCPUUserTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 8),
    _NtCPUUserTime_Type()
)
ntCPUUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUUserTime.setStatus("mandatory")
_NtCPUTicks_Type = Integer32
_NtCPUTicks_Object = MibTableColumn
ntCPUTicks = _NtCPUTicks_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 9),
    _NtCPUTicks_Type()
)
ntCPUTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUTicks.setStatus("mandatory")
_NtCPUCountsSoFar_Type = Integer32
_NtCPUCountsSoFar_Object = MibTableColumn
ntCPUCountsSoFar = _NtCPUCountsSoFar_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 5, 2, 10),
    _NtCPUCountsSoFar_Type()
)
ntCPUCountsSoFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCPUCountsSoFar.setStatus("mandatory")
_NtLogPollTable_Object = MibTable
ntLogPollTable = _NtLogPollTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    ntLogPollTable.setStatus("mandatory")
_NtLogPollTableEntry_Object = MibTableRow
ntLogPollTableEntry = _NtLogPollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ntLogPollTableEntry.setStatus("mandatory")
_NtLogAppStart_Type = Integer32
_NtLogAppStart_Object = MibTableColumn
ntLogAppStart = _NtLogAppStart_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1, 1),
    _NtLogAppStart_Type()
)
ntLogAppStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogAppStart.setStatus("mandatory")
_NtLogSecStart_Type = Integer32
_NtLogSecStart_Object = MibTableColumn
ntLogSecStart = _NtLogSecStart_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1, 2),
    _NtLogSecStart_Type()
)
ntLogSecStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogSecStart.setStatus("mandatory")
_NtLogSysStart_Type = Integer32
_NtLogSysStart_Object = MibTableColumn
ntLogSysStart = _NtLogSysStart_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1, 3),
    _NtLogSysStart_Type()
)
ntLogSysStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogSysStart.setStatus("mandatory")
_NtLogAppLast_Type = Integer32
_NtLogAppLast_Object = MibTableColumn
ntLogAppLast = _NtLogAppLast_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1, 4),
    _NtLogAppLast_Type()
)
ntLogAppLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogAppLast.setStatus("mandatory")
_NtLogSecLast_Type = Integer32
_NtLogSecLast_Object = MibTableColumn
ntLogSecLast = _NtLogSecLast_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1, 5),
    _NtLogSecLast_Type()
)
ntLogSecLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogSecLast.setStatus("mandatory")
_NtLogSysLast_Type = Integer32
_NtLogSysLast_Object = MibTableColumn
ntLogSysLast = _NtLogSysLast_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 4, 6, 1, 6),
    _NtLogSysLast_Type()
)
ntLogSysLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogSysLast.setStatus("mandatory")
_NtAvailableGroup_ObjectIdentity = ObjectIdentity
ntAvailableGroup = _NtAvailableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5)
)
_NtAvailConfig_ObjectIdentity = ObjectIdentity
ntAvailConfig = _NtAvailConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1)
)
_NtAvailFSPeriod_Type = DisplayString
_NtAvailFSPeriod_Object = MibScalar
ntAvailFSPeriod = _NtAvailFSPeriod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 1),
    _NtAvailFSPeriod_Type()
)
ntAvailFSPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntAvailFSPeriod.setStatus("mandatory")
_NtAvailFSPollTimestamp_Type = DisplayString
_NtAvailFSPollTimestamp_Object = MibScalar
ntAvailFSPollTimestamp = _NtAvailFSPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 2),
    _NtAvailFSPollTimestamp_Type()
)
ntAvailFSPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailFSPollTimestamp.setStatus("mandatory")
_NtAvailProcPeriod_Type = DisplayString
_NtAvailProcPeriod_Object = MibScalar
ntAvailProcPeriod = _NtAvailProcPeriod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 3),
    _NtAvailProcPeriod_Type()
)
ntAvailProcPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntAvailProcPeriod.setStatus("mandatory")
_NtAvailProcTimestamp_Type = DisplayString
_NtAvailProcTimestamp_Object = MibScalar
ntAvailProcTimestamp = _NtAvailProcTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 4),
    _NtAvailProcTimestamp_Type()
)
ntAvailProcTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailProcTimestamp.setStatus("mandatory")
_NtAvailServPeriod_Type = DisplayString
_NtAvailServPeriod_Object = MibScalar
ntAvailServPeriod = _NtAvailServPeriod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 5),
    _NtAvailServPeriod_Type()
)
ntAvailServPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntAvailServPeriod.setStatus("mandatory")
_NtAvailServPollTimestamp_Type = DisplayString
_NtAvailServPollTimestamp_Object = MibScalar
ntAvailServPollTimestamp = _NtAvailServPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 6),
    _NtAvailServPollTimestamp_Type()
)
ntAvailServPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailServPollTimestamp.setStatus("mandatory")
_NtAvailPrinterPeriod_Type = DisplayString
_NtAvailPrinterPeriod_Object = MibScalar
ntAvailPrinterPeriod = _NtAvailPrinterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 7),
    _NtAvailPrinterPeriod_Type()
)
ntAvailPrinterPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntAvailPrinterPeriod.setStatus("mandatory")
_NtAvailPrinterPollTimestamp_Type = DisplayString
_NtAvailPrinterPollTimestamp_Object = MibScalar
ntAvailPrinterPollTimestamp = _NtAvailPrinterPollTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 1, 8),
    _NtAvailPrinterPollTimestamp_Type()
)
ntAvailPrinterPollTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailPrinterPollTimestamp.setStatus("mandatory")
_NtAvailFSTable_Object = MibTable
ntAvailFSTable = _NtAvailFSTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ntAvailFSTable.setStatus("mandatory")
_NtAvailFSEntry_Object = MibTableRow
ntAvailFSEntry = _NtAvailFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 2, 1)
)
ntAvailFSEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntAvailFSDriveLetter"),
)
if mibBuilder.loadTexts:
    ntAvailFSEntry.setStatus("mandatory")
_NtAvailFSDriveLetter_Type = DisplayString
_NtAvailFSDriveLetter_Object = MibTableColumn
ntAvailFSDriveLetter = _NtAvailFSDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 2, 1, 1),
    _NtAvailFSDriveLetter_Type()
)
ntAvailFSDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailFSDriveLetter.setStatus("mandatory")
_NtAvailFSDriveLabel_Type = DisplayString
_NtAvailFSDriveLabel_Object = MibTableColumn
ntAvailFSDriveLabel = _NtAvailFSDriveLabel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 2, 1, 2),
    _NtAvailFSDriveLabel_Type()
)
ntAvailFSDriveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailFSDriveLabel.setStatus("mandatory")
_NtAvailFSDriveType_Type = DisplayString
_NtAvailFSDriveType_Object = MibTableColumn
ntAvailFSDriveType = _NtAvailFSDriveType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 2, 1, 3),
    _NtAvailFSDriveType_Type()
)
ntAvailFSDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailFSDriveType.setStatus("mandatory")
_NtAvailProcTable_Object = MibTable
ntAvailProcTable = _NtAvailProcTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    ntAvailProcTable.setStatus("mandatory")
_NtAvailProcEntry_Object = MibTableRow
ntAvailProcEntry = _NtAvailProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 3, 1)
)
ntAvailProcEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntAvailProcessName"),
)
if mibBuilder.loadTexts:
    ntAvailProcEntry.setStatus("mandatory")
_NtAvailProcessName_Type = DisplayString
_NtAvailProcessName_Object = MibTableColumn
ntAvailProcessName = _NtAvailProcessName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 3, 1, 1),
    _NtAvailProcessName_Type()
)
ntAvailProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailProcessName.setStatus("mandatory")
_NtAvailServiceTable_Object = MibTable
ntAvailServiceTable = _NtAvailServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    ntAvailServiceTable.setStatus("mandatory")
_NtAvailServiceEntry_Object = MibTableRow
ntAvailServiceEntry = _NtAvailServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 4, 1)
)
ntAvailServiceEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntAvailServiceName"),
)
if mibBuilder.loadTexts:
    ntAvailServiceEntry.setStatus("mandatory")
_NtAvailServiceName_Type = DisplayString
_NtAvailServiceName_Object = MibTableColumn
ntAvailServiceName = _NtAvailServiceName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 4, 1, 1),
    _NtAvailServiceName_Type()
)
ntAvailServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailServiceName.setStatus("mandatory")
_NtAvailServiceDescr_Type = DisplayString
_NtAvailServiceDescr_Object = MibTableColumn
ntAvailServiceDescr = _NtAvailServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 4, 1, 2),
    _NtAvailServiceDescr_Type()
)
ntAvailServiceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailServiceDescr.setStatus("mandatory")


class _NtAvailServiceStatus_Type(Integer32):
    """Custom type ntAvailServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("continue-pending", 5),
          ("pause-pending", 6),
          ("paused", 7),
          ("running", 4),
          ("start-pending", 2),
          ("stop-pending", 3),
          ("stopped", 1),
          ("unknown", 8))
    )


_NtAvailServiceStatus_Type.__name__ = "Integer32"
_NtAvailServiceStatus_Object = MibTableColumn
ntAvailServiceStatus = _NtAvailServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 4, 1, 3),
    _NtAvailServiceStatus_Type()
)
ntAvailServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailServiceStatus.setStatus("mandatory")
_NtAvailPrinterTable_Object = MibTable
ntAvailPrinterTable = _NtAvailPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 5)
)
if mibBuilder.loadTexts:
    ntAvailPrinterTable.setStatus("mandatory")
_NtAvailPrinterEntry_Object = MibTableRow
ntAvailPrinterEntry = _NtAvailPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 5, 1)
)
ntAvailPrinterEntry.setIndexNames(
    (0, "CA-NTOS-MIB", "ntAvailPrinterName"),
)
if mibBuilder.loadTexts:
    ntAvailPrinterEntry.setStatus("mandatory")
_NtAvailPrinterName_Type = DisplayString
_NtAvailPrinterName_Object = MibTableColumn
ntAvailPrinterName = _NtAvailPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 5, 1, 1),
    _NtAvailPrinterName_Type()
)
ntAvailPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailPrinterName.setStatus("mandatory")
_NtAvailPrinterDescr_Type = DisplayString
_NtAvailPrinterDescr_Object = MibTableColumn
ntAvailPrinterDescr = _NtAvailPrinterDescr_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 5, 1, 2),
    _NtAvailPrinterDescr_Type()
)
ntAvailPrinterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailPrinterDescr.setStatus("mandatory")
_NtAvailPrinterType_Type = DisplayString
_NtAvailPrinterType_Object = MibTableColumn
ntAvailPrinterType = _NtAvailPrinterType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 5, 1, 3),
    _NtAvailPrinterType_Type()
)
ntAvailPrinterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailPrinterType.setStatus("mandatory")
_NtAvailPrinterLocation_Type = DisplayString
_NtAvailPrinterLocation_Object = MibTableColumn
ntAvailPrinterLocation = _NtAvailPrinterLocation_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 5, 5, 1, 4),
    _NtAvailPrinterLocation_Type()
)
ntAvailPrinterLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailPrinterLocation.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ntFSUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 1)
)
if mibBuilder.loadTexts:
    ntFSUnknown.setStatus(
        ""
    )

ntFSok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 2)
)
if mibBuilder.loadTexts:
    ntFSok.setStatus(
        ""
    )

ntFSwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 3)
)
if mibBuilder.loadTexts:
    ntFSwarning.setStatus(
        ""
    )

ntFScritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 4)
)
if mibBuilder.loadTexts:
    ntFScritical.setStatus(
        ""
    )

ntFileUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 5)
)
if mibBuilder.loadTexts:
    ntFileUnknown.setStatus(
        ""
    )

ntFileok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 6)
)
if mibBuilder.loadTexts:
    ntFileok.setStatus(
        ""
    )

ntFilewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 7)
)
if mibBuilder.loadTexts:
    ntFilewarning.setStatus(
        ""
    )

ntFilecritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 8)
)
if mibBuilder.loadTexts:
    ntFilecritical.setStatus(
        ""
    )

ntProcessUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 9)
)
if mibBuilder.loadTexts:
    ntProcessUnknown.setStatus(
        ""
    )

ntProcessok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 10)
)
if mibBuilder.loadTexts:
    ntProcessok.setStatus(
        ""
    )

ntProcesswarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 11)
)
if mibBuilder.loadTexts:
    ntProcesswarning.setStatus(
        ""
    )

ntProcesscritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 12)
)
if mibBuilder.loadTexts:
    ntProcesscritical.setStatus(
        ""
    )

ntServiceUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 13)
)
if mibBuilder.loadTexts:
    ntServiceUnknown.setStatus(
        ""
    )

ntServiceok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 14)
)
if mibBuilder.loadTexts:
    ntServiceok.setStatus(
        ""
    )

ntServicewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 15)
)
if mibBuilder.loadTexts:
    ntServicewarning.setStatus(
        ""
    )

ntServicecritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 16)
)
if mibBuilder.loadTexts:
    ntServicecritical.setStatus(
        ""
    )

ntPrinterUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 17)
)
if mibBuilder.loadTexts:
    ntPrinterUnknown.setStatus(
        ""
    )

ntPrinterok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 18)
)
if mibBuilder.loadTexts:
    ntPrinterok.setStatus(
        ""
    )

ntPrinterwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 19)
)
if mibBuilder.loadTexts:
    ntPrinterwarning.setStatus(
        ""
    )

ntPrintercritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 20)
)
if mibBuilder.loadTexts:
    ntPrintercritical.setStatus(
        ""
    )

ntCPUUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 21)
)
if mibBuilder.loadTexts:
    ntCPUUnknown.setStatus(
        ""
    )

ntCPUok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 22)
)
if mibBuilder.loadTexts:
    ntCPUok.setStatus(
        ""
    )

ntCPUwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 23)
)
if mibBuilder.loadTexts:
    ntCPUwarning.setStatus(
        ""
    )

ntCPUcritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 24)
)
if mibBuilder.loadTexts:
    ntCPUcritical.setStatus(
        ""
    )

ntMemLoadok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 25)
)
if mibBuilder.loadTexts:
    ntMemLoadok.setStatus(
        ""
    )

ntMemLoadwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 26)
)
if mibBuilder.loadTexts:
    ntMemLoadwarning.setStatus(
        ""
    )

ntMemLoadcritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 27)
)
if mibBuilder.loadTexts:
    ntMemLoadcritical.setStatus(
        ""
    )

ntMemPhysok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 28)
)
if mibBuilder.loadTexts:
    ntMemPhysok.setStatus(
        ""
    )

ntMemPhyswarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 29)
)
if mibBuilder.loadTexts:
    ntMemPhyswarning.setStatus(
        ""
    )

ntMemPhyscritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 30)
)
if mibBuilder.loadTexts:
    ntMemPhyscritical.setStatus(
        ""
    )

ntMemSwapok = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 31)
)
if mibBuilder.loadTexts:
    ntMemSwapok.setStatus(
        ""
    )

ntMemSwapwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 32)
)
if mibBuilder.loadTexts:
    ntMemSwapwarning.setStatus(
        ""
    )

ntMemSwapcritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 33)
)
if mibBuilder.loadTexts:
    ntMemSwapcritical.setStatus(
        ""
    )

ntRegUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 34)
)
if mibBuilder.loadTexts:
    ntRegUnknown.setStatus(
        ""
    )

ntRegOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 35)
)
if mibBuilder.loadTexts:
    ntRegOK.setStatus(
        ""
    )

ntRegwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 36)
)
if mibBuilder.loadTexts:
    ntRegwarning.setStatus(
        ""
    )

ntRegcritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 37)
)
if mibBuilder.loadTexts:
    ntRegcritical.setStatus(
        ""
    )

ntLogOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 38)
)
if mibBuilder.loadTexts:
    ntLogOK.setStatus(
        ""
    )

ntLogwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 39)
)
if mibBuilder.loadTexts:
    ntLogwarning.setStatus(
        ""
    )

ntLogcritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 40)
)
if mibBuilder.loadTexts:
    ntLogcritical.setStatus(
        ""
    )

ntAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 41)
)
if mibBuilder.loadTexts:
    ntAdd.setStatus(
        ""
    )

ntRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 9, 2, 2, 0, 42)
)
if mibBuilder.loadTexts:
    ntRemove.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CA-NTOS-MIB",
    **{"cai": cai,
       "caiSysMgr": caiSysMgr,
       "agentWorks": agentWorks,
       "nt": nt,
       "caiNtOs": caiNtOs,
       "ntFSUnknown": ntFSUnknown,
       "ntFSok": ntFSok,
       "ntFSwarning": ntFSwarning,
       "ntFScritical": ntFScritical,
       "ntFileUnknown": ntFileUnknown,
       "ntFileok": ntFileok,
       "ntFilewarning": ntFilewarning,
       "ntFilecritical": ntFilecritical,
       "ntProcessUnknown": ntProcessUnknown,
       "ntProcessok": ntProcessok,
       "ntProcesswarning": ntProcesswarning,
       "ntProcesscritical": ntProcesscritical,
       "ntServiceUnknown": ntServiceUnknown,
       "ntServiceok": ntServiceok,
       "ntServicewarning": ntServicewarning,
       "ntServicecritical": ntServicecritical,
       "ntPrinterUnknown": ntPrinterUnknown,
       "ntPrinterok": ntPrinterok,
       "ntPrinterwarning": ntPrinterwarning,
       "ntPrintercritical": ntPrintercritical,
       "ntCPUUnknown": ntCPUUnknown,
       "ntCPUok": ntCPUok,
       "ntCPUwarning": ntCPUwarning,
       "ntCPUcritical": ntCPUcritical,
       "ntMemLoadok": ntMemLoadok,
       "ntMemLoadwarning": ntMemLoadwarning,
       "ntMemLoadcritical": ntMemLoadcritical,
       "ntMemPhysok": ntMemPhysok,
       "ntMemPhyswarning": ntMemPhyswarning,
       "ntMemPhyscritical": ntMemPhyscritical,
       "ntMemSwapok": ntMemSwapok,
       "ntMemSwapwarning": ntMemSwapwarning,
       "ntMemSwapcritical": ntMemSwapcritical,
       "ntRegUnknown": ntRegUnknown,
       "ntRegOK": ntRegOK,
       "ntRegwarning": ntRegwarning,
       "ntRegcritical": ntRegcritical,
       "ntLogOK": ntLogOK,
       "ntLogwarning": ntLogwarning,
       "ntLogcritical": ntLogcritical,
       "ntAdd": ntAdd,
       "ntRemove": ntRemove,
       "ntConfigGroup": ntConfigGroup,
       "ntGeneralConfig": ntGeneralConfig,
       "ntAgentVersion": ntAgentVersion,
       "ntAgentColdStartTimestamp": ntAgentColdStartTimestamp,
       "ntAgentWarmStartTimestamp": ntAgentWarmStartTimestamp,
       "ntFilesystemPollTimestamp": ntFilesystemPollTimestamp,
       "ntFilePollTimestamp": ntFilePollTimestamp,
       "ntProcessPollTimestamp": ntProcessPollTimestamp,
       "ntServicePollTimestamp": ntServicePollTimestamp,
       "ntPrinterPollTimestamp": ntPrinterPollTimestamp,
       "ntMemoryPollTimestamp": ntMemoryPollTimestamp,
       "ntProcessorPollTimestamp": ntProcessorPollTimestamp,
       "ntRegistryPollTimestamp": ntRegistryPollTimestamp,
       "ntLogPollTimestamp": ntLogPollTimestamp,
       "ntFileSystemConfig": ntFileSystemConfig,
       "ntFSPollInterval": ntFSPollInterval,
       "ntDefFSWarnThresh": ntDefFSWarnThresh,
       "ntDefFSCriticalThresh": ntDefFSCriticalThresh,
       "ntDefFSDelta": ntDefFSDelta,
       "ntFSMonitored": ntFSMonitored,
       "ntFSAdd": ntFSAdd,
       "ntFSRemove": ntFSRemove,
       "ntFileConfig": ntFileConfig,
       "ntFilePollInterval": ntFilePollInterval,
       "ntDefFileSizeWarning": ntDefFileSizeWarning,
       "ntDefFileSizeCritical": ntDefFileSizeCritical,
       "ntDefFileSizeChangeFlag": ntDefFileSizeChangeFlag,
       "ntDefFileSizeChange": ntDefFileSizeChange,
       "ntDefFileTimestampFlag": ntDefFileTimestampFlag,
       "ntFilesMonitored": ntFilesMonitored,
       "ntFileAdd": ntFileAdd,
       "ntFileRemove": ntFileRemove,
       "ntProcessConfig": ntProcessConfig,
       "ntProcPollInterval": ntProcPollInterval,
       "ntDefProcAlertLevel": ntDefProcAlertLevel,
       "ntDefProcExist": ntDefProcExist,
       "ntDefProcInstanceAlert": ntDefProcInstanceAlert,
       "ntDefProcThreadAlert": ntDefProcThreadAlert,
       "ntProcessesMonitored": ntProcessesMonitored,
       "ntProcAdd": ntProcAdd,
       "ntProcRemove": ntProcRemove,
       "ntServiceConfig": ntServiceConfig,
       "ntServPollInterval": ntServPollInterval,
       "ntDefServAlertOn": ntDefServAlertOn,
       "ntServicesMonitored": ntServicesMonitored,
       "ntServiceAdd": ntServiceAdd,
       "ntServiceRemove": ntServiceRemove,
       "ntPrinterConfig": ntPrinterConfig,
       "ntPrinterPollInterval": ntPrinterPollInterval,
       "ntDefPrintEventMonitor": ntDefPrintEventMonitor,
       "ntDefPrinterQFlag": ntDefPrinterQFlag,
       "ntDefPrinterQWarning": ntDefPrinterQWarning,
       "ntDefPrinterQCritical": ntDefPrinterQCritical,
       "ntPrintersMonitored": ntPrintersMonitored,
       "ntPrinterAdd": ntPrinterAdd,
       "ntPrinterRemove": ntPrinterRemove,
       "ntMemoryConfig": ntMemoryConfig,
       "ntMemPollInterval": ntMemPollInterval,
       "ntDefMemLoadWarning": ntDefMemLoadWarning,
       "ntDefMemLoadCritical": ntDefMemLoadCritical,
       "ntDefMemLoadCount": ntDefMemLoadCount,
       "ntDefMemPhysWarning": ntDefMemPhysWarning,
       "ntDefMemPhysCritical": ntDefMemPhysCritical,
       "ntDefMemPhysCount": ntDefMemPhysCount,
       "ntDefMemSwapWarning": ntDefMemSwapWarning,
       "ntDefMemSwapCritical": ntDefMemSwapCritical,
       "ntDefMemSwapCount": ntDefMemSwapCount,
       "ntProcessorConfig": ntProcessorConfig,
       "ntCPUPollInterval": ntCPUPollInterval,
       "ntDefCPUWarning": ntDefCPUWarning,
       "ntDefCPUCritical": ntDefCPUCritical,
       "ntDefCPUCount": ntDefCPUCount,
       "ntCPUsMonitored": ntCPUsMonitored,
       "ntRegistryConfig": ntRegistryConfig,
       "ntRegPollInterval": ntRegPollInterval,
       "ntDefRegMonitorLevel": ntDefRegMonitorLevel,
       "ntDefRegWarning": ntDefRegWarning,
       "ntDefRegCritical": ntDefRegCritical,
       "ntRegLeavesMonitored": ntRegLeavesMonitored,
       "ntRegistryLeafAdd": ntRegistryLeafAdd,
       "ntRegistryLeafRemove": ntRegistryLeafRemove,
       "ntEventLogConfig": ntEventLogConfig,
       "ntLogPollInterval": ntLogPollInterval,
       "ntLogApplicationCount": ntLogApplicationCount,
       "ntLogSecurityCount": ntLogSecurityCount,
       "ntLogSystemCount": ntLogSystemCount,
       "ntDefLogMonitorLevel": ntDefLogMonitorLevel,
       "ntLogsMonitored": ntLogsMonitored,
       "ntLogAdd": ntLogAdd,
       "ntStatusGroup": ntStatusGroup,
       "ntStatusSummary": ntStatusSummary,
       "ntStatus": ntStatus,
       "ntTotalWarning": ntTotalWarning,
       "ntTotalCritical": ntTotalCritical,
       "ntFSWarnStatus": ntFSWarnStatus,
       "ntFSCriticalStatus": ntFSCriticalStatus,
       "ntFileWarnStatus": ntFileWarnStatus,
       "ntFileCriticalStatus": ntFileCriticalStatus,
       "ntProcessWarnStatus": ntProcessWarnStatus,
       "ntProcessCriticalStatus": ntProcessCriticalStatus,
       "ntServicesWarnStatus": ntServicesWarnStatus,
       "ntServicesCriticalStatus": ntServicesCriticalStatus,
       "ntPrintWarnStatus": ntPrintWarnStatus,
       "ntPrintCriticalStatus": ntPrintCriticalStatus,
       "ntMemoryWarnStatus": ntMemoryWarnStatus,
       "ntMemoryCriticalStatus": ntMemoryCriticalStatus,
       "ntProcessorWarnStatus": ntProcessorWarnStatus,
       "ntProcessorCriticalStatus": ntProcessorCriticalStatus,
       "ntRegistryWarnStatus": ntRegistryWarnStatus,
       "ntRegistryCriticalStatus": ntRegistryCriticalStatus,
       "ntEventLogWarnStatus": ntEventLogWarnStatus,
       "ntEventLogCriticalStatus": ntEventLogCriticalStatus,
       "ntFilesystemStTable": ntFilesystemStTable,
       "ntFilesystemStTableEntry": ntFilesystemStTableEntry,
       "ntStatusFSDriveLetter": ntStatusFSDriveLetter,
       "ntStatusFSDriveLabel": ntStatusFSDriveLabel,
       "ntStatusFSDriveType": ntStatusFSDriveType,
       "ntStatusFSDriveFormat": ntStatusFSDriveFormat,
       "ntStatusFSTotalCapacity": ntStatusFSTotalCapacity,
       "ntStatusFSUtilization": ntStatusFSUtilization,
       "ntStatusFSFree": ntStatusFSFree,
       "ntStatusFSStatus": ntStatusFSStatus,
       "ntStatusFSPcntWarn": ntStatusFSPcntWarn,
       "ntStatusFSPcntCritical": ntStatusFSPcntCritical,
       "ntStatusFSKByteWarn": ntStatusFSKByteWarn,
       "ntStatusFSKByteCritical": ntStatusFSKByteCritical,
       "ntStatusFSAvgUtil": ntStatusFSAvgUtil,
       "ntStatusFSMinUtil": ntStatusFSMinUtil,
       "ntStatusFSMaxUtil": ntStatusFSMaxUtil,
       "ntStatusFSUtilDelta": ntStatusFSUtilDelta,
       "ntStatusFSDeltaLevel": ntStatusFSDeltaLevel,
       "ntStatusFSDeltaThreshold": ntStatusFSDeltaThreshold,
       "ntStatusFSDescription": ntStatusFSDescription,
       "ntFileStTable": ntFileStTable,
       "ntFileStTableEntry": ntFileStTableEntry,
       "ntStatusFileName": ntStatusFileName,
       "ntStatusFileStatus": ntStatusFileStatus,
       "ntStatusFileSize": ntStatusFileSize,
       "ntStatusFileSizeStatus": ntStatusFileSizeStatus,
       "ntStatusFileSizeWarning": ntStatusFileSizeWarning,
       "ntStatusFileSizeCritical": ntStatusFileSizeCritical,
       "ntStatusFileTimestamp": ntStatusFileTimestamp,
       "ntStatusFileTimestampFlag": ntStatusFileTimestampFlag,
       "ntStatusFileTimestampStatus": ntStatusFileTimestampStatus,
       "ntStatusFileSizeChFlag": ntStatusFileSizeChFlag,
       "ntStatusFileSizeCh": ntStatusFileSizeCh,
       "ntStatusFileSizeChState": ntStatusFileSizeChState,
       "ntStatusFileSizeChBytes": ntStatusFileSizeChBytes,
       "ntStatusFileMinSize": ntStatusFileMinSize,
       "ntStatusFileMaxSize": ntStatusFileMaxSize,
       "ntStatusFileAvgSize": ntStatusFileAvgSize,
       "ntStatusFileDescription": ntStatusFileDescription,
       "ntStatusFileSizeBase": ntStatusFileSizeBase,
       "ntProcessStTable": ntProcessStTable,
       "ntProcessStTableEntry": ntProcessStTableEntry,
       "ntStatusProcName": ntStatusProcName,
       "ntStatusProcStatus": ntStatusProcStatus,
       "ntStatusProcAlertLevel": ntStatusProcAlertLevel,
       "ntStatusProcExist": ntStatusProcExist,
       "ntStatusProcInst": ntStatusProcInst,
       "ntStatusProcInstMonitor": ntStatusProcInstMonitor,
       "ntStatusProcInstWarning": ntStatusProcInstWarning,
       "ntStatusProcInstCritical": ntStatusProcInstCritical,
       "ntStatusProcThd": ntStatusProcThd,
       "ntStatusProcThdMonitor": ntStatusProcThdMonitor,
       "ntStatusProcThdRef": ntStatusProcThdRef,
       "ntStatusProcThdMax": ntStatusProcThdMax,
       "ntStatusProcThdMin": ntStatusProcThdMin,
       "ntStatusProcDescription": ntStatusProcDescription,
       "ntServiceStTable": ntServiceStTable,
       "ntServiceStTableEntry": ntServiceStTableEntry,
       "ntStatusServName": ntStatusServName,
       "ntStatusServDescription": ntStatusServDescription,
       "ntStatusServState": ntStatusServState,
       "ntStatusServStatus": ntStatusServStatus,
       "ntStatusServAlertOn": ntStatusServAlertOn,
       "ntPrinterStTable": ntPrinterStTable,
       "ntStatusPrintTableEntry": ntStatusPrintTableEntry,
       "ntStatusPrintName": ntStatusPrintName,
       "ntStatusPrintStatus": ntStatusPrintStatus,
       "ntStatusPrintEventMonitor": ntStatusPrintEventMonitor,
       "ntStatusPrintEventStatus": ntStatusPrintEventStatus,
       "ntStatusPrintEventDescription": ntStatusPrintEventDescription,
       "ntStatusPrintQFlag": ntStatusPrintQFlag,
       "ntStatusPrintQueue": ntStatusPrintQueue,
       "ntStatusPrintQStatus": ntStatusPrintQStatus,
       "ntStatusPrintQWarning": ntStatusPrintQWarning,
       "ntStatusPrintQCritical": ntStatusPrintQCritical,
       "ntStatusPrintQMax": ntStatusPrintQMax,
       "ntStatusPrintDescription": ntStatusPrintDescription,
       "ntMemorySt": ntMemorySt,
       "ntStatusMemLoad": ntStatusMemLoad,
       "ntStatusMemLoadStatus": ntStatusMemLoadStatus,
       "ntStatusMemLoadAvg": ntStatusMemLoadAvg,
       "ntStatusMemLoadMax": ntStatusMemLoadMax,
       "ntStatusMemLoadMin": ntStatusMemLoadMin,
       "ntStatusMemPhysTotal": ntStatusMemPhysTotal,
       "ntStatusMemPhys": ntStatusMemPhys,
       "ntStatusMemPhysStatus": ntStatusMemPhysStatus,
       "ntStatusMemPhysAvg": ntStatusMemPhysAvg,
       "ntStatusMemPhysMax": ntStatusMemPhysMax,
       "ntStatusMemPhysMin": ntStatusMemPhysMin,
       "ntStatusMemSwapTotal": ntStatusMemSwapTotal,
       "ntStatusMemSwap": ntStatusMemSwap,
       "ntStatusMemSwapStatus": ntStatusMemSwapStatus,
       "ntStatusMemSwapAvg": ntStatusMemSwapAvg,
       "ntStatusMemSwapMax": ntStatusMemSwapMax,
       "ntStatusMemSwapMin": ntStatusMemSwapMin,
       "ntProcessorStTable": ntProcessorStTable,
       "ntProcessorStTableEntry": ntProcessorStTableEntry,
       "ntStatusCPUNumber": ntStatusCPUNumber,
       "ntStatusCPUStatus": ntStatusCPUStatus,
       "ntStatusCPUTotal": ntStatusCPUTotal,
       "ntStatusCPUWarning": ntStatusCPUWarning,
       "ntStatusCPUCritical": ntStatusCPUCritical,
       "ntStatusCPUCount": ntStatusCPUCount,
       "ntStatusCPUAvg": ntStatusCPUAvg,
       "ntStatusCPUMax": ntStatusCPUMax,
       "ntStatusCPUMin": ntStatusCPUMin,
       "ntStatusCPUDelta": ntStatusCPUDelta,
       "ntStatusCPUDescription": ntStatusCPUDescription,
       "ntRegistryStTable": ntRegistryStTable,
       "ntRegistryStTableEntry": ntRegistryStTableEntry,
       "ntStatusRegHandle": ntStatusRegHandle,
       "ntStatusRegKey": ntStatusRegKey,
       "ntStatusRegLeaf": ntStatusRegLeaf,
       "ntStatusRegDataType": ntStatusRegDataType,
       "ntStatusRegValue": ntStatusRegValue,
       "ntStatusRegPrevValue": ntStatusRegPrevValue,
       "ntStatusRegStatus": ntStatusRegStatus,
       "ntStatusRegAvgTicks": ntStatusRegAvgTicks,
       "ntStatusRegAvg": ntStatusRegAvg,
       "ntStatusRegMax": ntStatusRegMax,
       "ntStatusRegMin": ntStatusRegMin,
       "ntStatusRegMonitorLevel": ntStatusRegMonitorLevel,
       "ntStatusRegWarning": ntStatusRegWarning,
       "ntStatusRegCritical": ntStatusRegCritical,
       "ntEventLogStTable": ntEventLogStTable,
       "ntEventLogStTableEntry": ntEventLogStTableEntry,
       "ntStatusLogLogs": ntStatusLogLogs,
       "ntStatusLogSeverity": ntStatusLogSeverity,
       "ntStatusLogSource": ntStatusLogSource,
       "ntStatusLogEventID": ntStatusLogEventID,
       "ntStatusLogUser": ntStatusLogUser,
       "ntStatusLogComputer": ntStatusLogComputer,
       "ntStatusLogStatus": ntStatusLogStatus,
       "ntStatusLogAlertOn": ntStatusLogAlertOn,
       "ntStatusLogStartTime": ntStatusLogStartTime,
       "ntStatusLogStartTimeInText": ntStatusLogStartTimeInText,
       "ntStatusLogAppLogMatches": ntStatusLogAppLogMatches,
       "ntStatusLogAppLogLastMatch": ntStatusLogAppLogLastMatch,
       "ntStatusLogSecLogMatches": ntStatusLogSecLogMatches,
       "ntStatusLogSecLogLastMatch": ntStatusLogSecLogLastMatch,
       "ntStatusLogSysLogMatches": ntStatusLogSysLogMatches,
       "ntStatusLogSysLogLastMatch": ntStatusLogSysLogLastMatch,
       "ntStatusLogWatcherIndex": ntStatusLogWatcherIndex,
       "ntStatusLogDescription": ntStatusLogDescription,
       "ntPollGroup": ntPollGroup,
       "ntFilesystemPollTable": ntFilesystemPollTable,
       "ntFilesystemPollTableEntry": ntFilesystemPollTableEntry,
       "ntFsysDriveLetter": ntFsysDriveLetter,
       "ntFsysTotalCapacity": ntFsysTotalCapacity,
       "ntFsysFree": ntFsysFree,
       "ntFsysUtilization": ntFsysUtilization,
       "ntFsysLastUtilization": ntFsysLastUtilization,
       "ntFsysAverage": ntFsysAverage,
       "ntFsysAvgTicks": ntFsysAvgTicks,
       "ntFilePollTable": ntFilePollTable,
       "ntFilePollTableEntry": ntFilePollTableEntry,
       "ntFileName": ntFileName,
       "ntFileTimestamp": ntFileTimestamp,
       "ntFileRefTimestamp": ntFileRefTimestamp,
       "ntFileSize": ntFileSize,
       "ntFileSizeChangeReference": ntFileSizeChangeReference,
       "ntFileSizeChangeCount": ntFileSizeChangeCount,
       "ntFileSizeAvgTicks": ntFileSizeAvgTicks,
       "ntProcessPollTable": ntProcessPollTable,
       "ntProcessPollTableEntry": ntProcessPollTableEntry,
       "ntProcessName": ntProcessName,
       "ntProcessInstCount": ntProcessInstCount,
       "ntProcessMaxThread": ntProcessMaxThread,
       "ntProcessMinThread": ntProcessMinThread,
       "ntProcessorPollTable": ntProcessorPollTable,
       "ntProcessorPollTableEntry": ntProcessorPollTableEntry,
       "ntCPUNumber": ntCPUNumber,
       "ntCPUDPCTime": ntCPUDPCTime,
       "ntCPUInterruptTime": ntCPUInterruptTime,
       "ntCPUPrivilegedTime": ntCPUPrivilegedTime,
       "ntCPUProcessorTime": ntCPUProcessorTime,
       "ntCPUUserTime": ntCPUUserTime,
       "ntCPUTicks": ntCPUTicks,
       "ntCPUCountsSoFar": ntCPUCountsSoFar,
       "ntLogPollTable": ntLogPollTable,
       "ntLogPollTableEntry": ntLogPollTableEntry,
       "ntLogAppStart": ntLogAppStart,
       "ntLogSecStart": ntLogSecStart,
       "ntLogSysStart": ntLogSysStart,
       "ntLogAppLast": ntLogAppLast,
       "ntLogSecLast": ntLogSecLast,
       "ntLogSysLast": ntLogSysLast,
       "ntAvailableGroup": ntAvailableGroup,
       "ntAvailConfig": ntAvailConfig,
       "ntAvailFSPeriod": ntAvailFSPeriod,
       "ntAvailFSPollTimestamp": ntAvailFSPollTimestamp,
       "ntAvailProcPeriod": ntAvailProcPeriod,
       "ntAvailProcTimestamp": ntAvailProcTimestamp,
       "ntAvailServPeriod": ntAvailServPeriod,
       "ntAvailServPollTimestamp": ntAvailServPollTimestamp,
       "ntAvailPrinterPeriod": ntAvailPrinterPeriod,
       "ntAvailPrinterPollTimestamp": ntAvailPrinterPollTimestamp,
       "ntAvailFSTable": ntAvailFSTable,
       "ntAvailFSEntry": ntAvailFSEntry,
       "ntAvailFSDriveLetter": ntAvailFSDriveLetter,
       "ntAvailFSDriveLabel": ntAvailFSDriveLabel,
       "ntAvailFSDriveType": ntAvailFSDriveType,
       "ntAvailProcTable": ntAvailProcTable,
       "ntAvailProcEntry": ntAvailProcEntry,
       "ntAvailProcessName": ntAvailProcessName,
       "ntAvailServiceTable": ntAvailServiceTable,
       "ntAvailServiceEntry": ntAvailServiceEntry,
       "ntAvailServiceName": ntAvailServiceName,
       "ntAvailServiceDescr": ntAvailServiceDescr,
       "ntAvailServiceStatus": ntAvailServiceStatus,
       "ntAvailPrinterTable": ntAvailPrinterTable,
       "ntAvailPrinterEntry": ntAvailPrinterEntry,
       "ntAvailPrinterName": ntAvailPrinterName,
       "ntAvailPrinterDescr": ntAvailPrinterDescr,
       "ntAvailPrinterType": ntAvailPrinterType,
       "ntAvailPrinterLocation": ntAvailPrinterLocation}
)
