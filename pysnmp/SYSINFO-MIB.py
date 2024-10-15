# SNMP MIB module (SYSINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:11 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_SystemsMonitor6000_ObjectIdentity = ObjectIdentity
systemsMonitor6000 = _SystemsMonitor6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12)
)
_SmProgramInformation_ObjectIdentity = ObjectIdentity
smProgramInformation = _SmProgramInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1)
)
_SmSiaProgramData_ObjectIdentity = ObjectIdentity
smSiaProgramData = _SmSiaProgramData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10)
)
_SmSiaProgramDescription_ObjectIdentity = ObjectIdentity
smSiaProgramDescription = _SmSiaProgramDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1)
)
_SmSiaProgramName_Type = DisplayString
_SmSiaProgramName_Object = MibScalar
smSiaProgramName = _SmSiaProgramName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1, 1),
    _SmSiaProgramName_Type()
)
smSiaProgramName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramName.setStatus("mandatory")
_SmSiaProgramNumber_Type = DisplayString
_SmSiaProgramNumber_Object = MibScalar
smSiaProgramNumber = _SmSiaProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1, 2),
    _SmSiaProgramNumber_Type()
)
smSiaProgramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramNumber.setStatus("mandatory")
_SmSiaProgramVersion_Type = DisplayString
_SmSiaProgramVersion_Object = MibScalar
smSiaProgramVersion = _SmSiaProgramVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1, 3),
    _SmSiaProgramVersion_Type()
)
smSiaProgramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramVersion.setStatus("mandatory")
_SmSiaProgramCompilationDate_Type = DisplayString
_SmSiaProgramCompilationDate_Object = MibScalar
smSiaProgramCompilationDate = _SmSiaProgramCompilationDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1, 4),
    _SmSiaProgramCompilationDate_Type()
)
smSiaProgramCompilationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramCompilationDate.setStatus("mandatory")
_SmSiaProgramUpTime_Type = TimeTicks
_SmSiaProgramUpTime_Object = MibScalar
smSiaProgramUpTime = _SmSiaProgramUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1, 5),
    _SmSiaProgramUpTime_Type()
)
smSiaProgramUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramUpTime.setStatus("mandatory")
_SmSiaProgramContact_Type = DisplayString
_SmSiaProgramContact_Object = MibScalar
smSiaProgramContact = _SmSiaProgramContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 1, 6),
    _SmSiaProgramContact_Type()
)
smSiaProgramContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramContact.setStatus("mandatory")
_SmSiaProgramControl_ObjectIdentity = ObjectIdentity
smSiaProgramControl = _SmSiaProgramControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2)
)
_SmSiaProgramControlLocalConfigurationFile_Type = DisplayString
_SmSiaProgramControlLocalConfigurationFile_Object = MibScalar
smSiaProgramControlLocalConfigurationFile = _SmSiaProgramControlLocalConfigurationFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 1),
    _SmSiaProgramControlLocalConfigurationFile_Type()
)
smSiaProgramControlLocalConfigurationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlLocalConfigurationFile.setStatus("mandatory")
_SmSiaProgramControlSavedFlags_Type = DisplayString
_SmSiaProgramControlSavedFlags_Object = MibScalar
smSiaProgramControlSavedFlags = _SmSiaProgramControlSavedFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 2),
    _SmSiaProgramControlSavedFlags_Type()
)
smSiaProgramControlSavedFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSavedFlags.setStatus("mandatory")
_SmSiaProgramControlAgentAddress_Type = IpAddress
_SmSiaProgramControlAgentAddress_Object = MibScalar
smSiaProgramControlAgentAddress = _SmSiaProgramControlAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 3),
    _SmSiaProgramControlAgentAddress_Type()
)
smSiaProgramControlAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlAgentAddress.setStatus("mandatory")
_SmSiaProgramControlReserved1_Type = Integer32
_SmSiaProgramControlReserved1_Object = MibScalar
smSiaProgramControlReserved1 = _SmSiaProgramControlReserved1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 4),
    _SmSiaProgramControlReserved1_Type()
)
smSiaProgramControlReserved1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlReserved1.setStatus("mandatory")
_SmSiaProgramControlPercentMultiplier_Type = Integer32
_SmSiaProgramControlPercentMultiplier_Object = MibScalar
smSiaProgramControlPercentMultiplier = _SmSiaProgramControlPercentMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 5),
    _SmSiaProgramControlPercentMultiplier_Type()
)
smSiaProgramControlPercentMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlPercentMultiplier.setStatus("mandatory")
_SmSiaProgramControlPollTime_Type = Integer32
_SmSiaProgramControlPollTime_Object = MibScalar
smSiaProgramControlPollTime = _SmSiaProgramControlPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 6),
    _SmSiaProgramControlPollTime_Type()
)
smSiaProgramControlPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlPollTime.setStatus("mandatory")
_SmSiaProgramControlFlags_Type = Integer32
_SmSiaProgramControlFlags_Object = MibScalar
smSiaProgramControlFlags = _SmSiaProgramControlFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 7),
    _SmSiaProgramControlFlags_Type()
)
smSiaProgramControlFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlFlags.setStatus("mandatory")
_SmSiaProgramControlRetryCount_Type = Integer32
_SmSiaProgramControlRetryCount_Object = MibScalar
smSiaProgramControlRetryCount = _SmSiaProgramControlRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 8),
    _SmSiaProgramControlRetryCount_Type()
)
smSiaProgramControlRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlRetryCount.setStatus("mandatory")
_SmSiaProgramControlTimeout_Type = TimeTicks
_SmSiaProgramControlTimeout_Object = MibScalar
smSiaProgramControlTimeout = _SmSiaProgramControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 9),
    _SmSiaProgramControlTimeout_Type()
)
smSiaProgramControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlTimeout.setStatus("mandatory")
_SmSiaProgramControlCurrentFlags_Type = DisplayString
_SmSiaProgramControlCurrentFlags_Object = MibScalar
smSiaProgramControlCurrentFlags = _SmSiaProgramControlCurrentFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 10),
    _SmSiaProgramControlCurrentFlags_Type()
)
smSiaProgramControlCurrentFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramControlCurrentFlags.setStatus("mandatory")
_SmSiaProgramControlReinitFlags_Type = DisplayString
_SmSiaProgramControlReinitFlags_Object = MibScalar
smSiaProgramControlReinitFlags = _SmSiaProgramControlReinitFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 11),
    _SmSiaProgramControlReinitFlags_Type()
)
smSiaProgramControlReinitFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlReinitFlags.setStatus("mandatory")


class _SmSiaProgramControlReInitializeMonitor_Type(Integer32):
    """Custom type smSiaProgramControlReInitializeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("trueReinit", 2),
          ("trueSaved", 3))
    )


_SmSiaProgramControlReInitializeMonitor_Type.__name__ = "Integer32"
_SmSiaProgramControlReInitializeMonitor_Object = MibScalar
smSiaProgramControlReInitializeMonitor = _SmSiaProgramControlReInitializeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 12),
    _SmSiaProgramControlReInitializeMonitor_Type()
)
smSiaProgramControlReInitializeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlReInitializeMonitor.setStatus("mandatory")


class _SmSiaProgramControlSaveConfiguration_Type(Integer32):
    """Custom type smSiaProgramControlSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SmSiaProgramControlSaveConfiguration_Type.__name__ = "Integer32"
_SmSiaProgramControlSaveConfiguration_Object = MibScalar
smSiaProgramControlSaveConfiguration = _SmSiaProgramControlSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 2, 13),
    _SmSiaProgramControlSaveConfiguration_Type()
)
smSiaProgramControlSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSaveConfiguration.setStatus("mandatory")
_SmSiaProgramLog_ObjectIdentity = ObjectIdentity
smSiaProgramLog = _SmSiaProgramLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3)
)
_SmSiaProgramLogFileName_Type = DisplayString
_SmSiaProgramLogFileName_Object = MibScalar
smSiaProgramLogFileName = _SmSiaProgramLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3, 1),
    _SmSiaProgramLogFileName_Type()
)
smSiaProgramLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramLogFileName.setStatus("mandatory")
_SmSiaProgramLogFileSize_Type = Integer32
_SmSiaProgramLogFileSize_Object = MibScalar
smSiaProgramLogFileSize = _SmSiaProgramLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3, 2),
    _SmSiaProgramLogFileSize_Type()
)
smSiaProgramLogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramLogFileSize.setStatus("mandatory")
_SmSiaProgramLogMaxFileSize_Type = Integer32
_SmSiaProgramLogMaxFileSize_Object = MibScalar
smSiaProgramLogMaxFileSize = _SmSiaProgramLogMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3, 3),
    _SmSiaProgramLogMaxFileSize_Type()
)
smSiaProgramLogMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramLogMaxFileSize.setStatus("mandatory")
_SmSiaProgramLogNumFiles_Type = Integer32
_SmSiaProgramLogNumFiles_Object = MibScalar
smSiaProgramLogNumFiles = _SmSiaProgramLogNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3, 4),
    _SmSiaProgramLogNumFiles_Type()
)
smSiaProgramLogNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramLogNumFiles.setStatus("mandatory")


class _SmSiaProgramLogFileBehavior_Type(Integer32):
    """Custom type smSiaProgramLogFileBehavior based on Integer32"""
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
        *(("nowrapFlush", 3),
          ("nowrapNoflush", 4),
          ("wrapFlush", 1),
          ("wrapNoflush", 2))
    )


_SmSiaProgramLogFileBehavior_Type.__name__ = "Integer32"
_SmSiaProgramLogFileBehavior_Object = MibScalar
smSiaProgramLogFileBehavior = _SmSiaProgramLogFileBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3, 5),
    _SmSiaProgramLogFileBehavior_Type()
)
smSiaProgramLogFileBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramLogFileBehavior.setStatus("mandatory")
_SmSiaProgramLogMask_Type = DisplayString
_SmSiaProgramLogMask_Object = MibScalar
smSiaProgramLogMask = _SmSiaProgramLogMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 3, 6),
    _SmSiaProgramLogMask_Type()
)
smSiaProgramLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramLogMask.setStatus("mandatory")
_SmSiaProgramSetableTestObjects_ObjectIdentity = ObjectIdentity
smSiaProgramSetableTestObjects = _SmSiaProgramSetableTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5)
)
_SmSiaProgramControlSetableInteger_Type = Integer32
_SmSiaProgramControlSetableInteger_Object = MibScalar
smSiaProgramControlSetableInteger = _SmSiaProgramControlSetableInteger_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5, 1),
    _SmSiaProgramControlSetableInteger_Type()
)
smSiaProgramControlSetableInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSetableInteger.setStatus("mandatory")
_SmSiaProgramControlSetableCounter_Type = Counter32
_SmSiaProgramControlSetableCounter_Object = MibScalar
smSiaProgramControlSetableCounter = _SmSiaProgramControlSetableCounter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5, 2),
    _SmSiaProgramControlSetableCounter_Type()
)
smSiaProgramControlSetableCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSetableCounter.setStatus("mandatory")
_SmSiaProgramControlSetableGauge_Type = Gauge32
_SmSiaProgramControlSetableGauge_Object = MibScalar
smSiaProgramControlSetableGauge = _SmSiaProgramControlSetableGauge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5, 3),
    _SmSiaProgramControlSetableGauge_Type()
)
smSiaProgramControlSetableGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSetableGauge.setStatus("mandatory")
_SmSiaProgramControlSetableIpAddress_Type = IpAddress
_SmSiaProgramControlSetableIpAddress_Object = MibScalar
smSiaProgramControlSetableIpAddress = _SmSiaProgramControlSetableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5, 4),
    _SmSiaProgramControlSetableIpAddress_Type()
)
smSiaProgramControlSetableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSetableIpAddress.setStatus("mandatory")
_SmSiaProgramControlSetableTimeTicks_Type = TimeTicks
_SmSiaProgramControlSetableTimeTicks_Object = MibScalar
smSiaProgramControlSetableTimeTicks = _SmSiaProgramControlSetableTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5, 5),
    _SmSiaProgramControlSetableTimeTicks_Type()
)
smSiaProgramControlSetableTimeTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSetableTimeTicks.setStatus("mandatory")
_SmSiaProgramControlSetableOctetString_Type = DisplayString
_SmSiaProgramControlSetableOctetString_Object = MibScalar
smSiaProgramControlSetableOctetString = _SmSiaProgramControlSetableOctetString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 10, 5, 6),
    _SmSiaProgramControlSetableOctetString_Type()
)
smSiaProgramControlSetableOctetString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaProgramControlSetableOctetString.setStatus("mandatory")
_SmSiaResourceUsage_ObjectIdentity = ObjectIdentity
smSiaResourceUsage = _SmSiaResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11)
)
_SmSiaResourceUsageTable_Object = MibTable
smSiaResourceUsageTable = _SmSiaResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1)
)
if mibBuilder.loadTexts:
    smSiaResourceUsageTable.setStatus("mandatory")
_SmSiaResourceUsageEntry_Object = MibTableRow
smSiaResourceUsageEntry = _SmSiaResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1)
)
smSiaResourceUsageEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaResourceUsageName"),
)
if mibBuilder.loadTexts:
    smSiaResourceUsageEntry.setStatus("mandatory")
_SmSiaResourceUsageName_Type = DisplayString
_SmSiaResourceUsageName_Object = MibTableColumn
smSiaResourceUsageName = _SmSiaResourceUsageName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 1),
    _SmSiaResourceUsageName_Type()
)
smSiaResourceUsageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageName.setStatus("mandatory")
_SmSiaResourceUsageUserTime_Type = TimeTicks
_SmSiaResourceUsageUserTime_Object = MibTableColumn
smSiaResourceUsageUserTime = _SmSiaResourceUsageUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 2),
    _SmSiaResourceUsageUserTime_Type()
)
smSiaResourceUsageUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageUserTime.setStatus("mandatory")
_SmSiaResourceUsageSystemTime_Type = TimeTicks
_SmSiaResourceUsageSystemTime_Object = MibTableColumn
smSiaResourceUsageSystemTime = _SmSiaResourceUsageSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 3),
    _SmSiaResourceUsageSystemTime_Type()
)
smSiaResourceUsageSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageSystemTime.setStatus("mandatory")
_SmSiaResourceUsageTotalTime_Type = TimeTicks
_SmSiaResourceUsageTotalTime_Object = MibTableColumn
smSiaResourceUsageTotalTime = _SmSiaResourceUsageTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 4),
    _SmSiaResourceUsageTotalTime_Type()
)
smSiaResourceUsageTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageTotalTime.setStatus("mandatory")
_SmSiaResourceUsageMaxrss_Type = Counter32
_SmSiaResourceUsageMaxrss_Object = MibTableColumn
smSiaResourceUsageMaxrss = _SmSiaResourceUsageMaxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 5),
    _SmSiaResourceUsageMaxrss_Type()
)
smSiaResourceUsageMaxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageMaxrss.setStatus("mandatory")
_SmSiaResourceUsageIxrss_Type = Counter32
_SmSiaResourceUsageIxrss_Object = MibTableColumn
smSiaResourceUsageIxrss = _SmSiaResourceUsageIxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 6),
    _SmSiaResourceUsageIxrss_Type()
)
smSiaResourceUsageIxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageIxrss.setStatus("mandatory")
_SmSiaResourceUsageIdrss_Type = Counter32
_SmSiaResourceUsageIdrss_Object = MibTableColumn
smSiaResourceUsageIdrss = _SmSiaResourceUsageIdrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 7),
    _SmSiaResourceUsageIdrss_Type()
)
smSiaResourceUsageIdrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageIdrss.setStatus("mandatory")
_SmSiaResourceUsageIsrss_Type = Counter32
_SmSiaResourceUsageIsrss_Object = MibTableColumn
smSiaResourceUsageIsrss = _SmSiaResourceUsageIsrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 8),
    _SmSiaResourceUsageIsrss_Type()
)
smSiaResourceUsageIsrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageIsrss.setStatus("mandatory")
_SmSiaResourceUsageMinflt_Type = Counter32
_SmSiaResourceUsageMinflt_Object = MibTableColumn
smSiaResourceUsageMinflt = _SmSiaResourceUsageMinflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 9),
    _SmSiaResourceUsageMinflt_Type()
)
smSiaResourceUsageMinflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageMinflt.setStatus("mandatory")
_SmSiaResourceUsageMajflt_Type = Counter32
_SmSiaResourceUsageMajflt_Object = MibTableColumn
smSiaResourceUsageMajflt = _SmSiaResourceUsageMajflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 10),
    _SmSiaResourceUsageMajflt_Type()
)
smSiaResourceUsageMajflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageMajflt.setStatus("mandatory")
_SmSiaResourceUsageNSwap_Type = Counter32
_SmSiaResourceUsageNSwap_Object = MibTableColumn
smSiaResourceUsageNSwap = _SmSiaResourceUsageNSwap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 11),
    _SmSiaResourceUsageNSwap_Type()
)
smSiaResourceUsageNSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageNSwap.setStatus("mandatory")
_SmSiaResourceUsageInBlock_Type = Counter32
_SmSiaResourceUsageInBlock_Object = MibTableColumn
smSiaResourceUsageInBlock = _SmSiaResourceUsageInBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 12),
    _SmSiaResourceUsageInBlock_Type()
)
smSiaResourceUsageInBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageInBlock.setStatus("mandatory")
_SmSiaResourceUsageOutBlock_Type = Counter32
_SmSiaResourceUsageOutBlock_Object = MibTableColumn
smSiaResourceUsageOutBlock = _SmSiaResourceUsageOutBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 13),
    _SmSiaResourceUsageOutBlock_Type()
)
smSiaResourceUsageOutBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageOutBlock.setStatus("mandatory")
_SmSiaResourceUsageMsgsnd_Type = Counter32
_SmSiaResourceUsageMsgsnd_Object = MibTableColumn
smSiaResourceUsageMsgsnd = _SmSiaResourceUsageMsgsnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 14),
    _SmSiaResourceUsageMsgsnd_Type()
)
smSiaResourceUsageMsgsnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageMsgsnd.setStatus("mandatory")
_SmSiaResourceUsageMsgrcv_Type = Counter32
_SmSiaResourceUsageMsgrcv_Object = MibTableColumn
smSiaResourceUsageMsgrcv = _SmSiaResourceUsageMsgrcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 15),
    _SmSiaResourceUsageMsgrcv_Type()
)
smSiaResourceUsageMsgrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageMsgrcv.setStatus("mandatory")
_SmSiaResourceUsageNSignals_Type = Counter32
_SmSiaResourceUsageNSignals_Object = MibTableColumn
smSiaResourceUsageNSignals = _SmSiaResourceUsageNSignals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 16),
    _SmSiaResourceUsageNSignals_Type()
)
smSiaResourceUsageNSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageNSignals.setStatus("mandatory")
_SmSiaResourceUsageVcsw_Type = Counter32
_SmSiaResourceUsageVcsw_Object = MibTableColumn
smSiaResourceUsageVcsw = _SmSiaResourceUsageVcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 17),
    _SmSiaResourceUsageVcsw_Type()
)
smSiaResourceUsageVcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageVcsw.setStatus("mandatory")
_SmSiaResourceUsageIcsw_Type = Counter32
_SmSiaResourceUsageIcsw_Object = MibTableColumn
smSiaResourceUsageIcsw = _SmSiaResourceUsageIcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 11, 1, 1, 18),
    _SmSiaResourceUsageIcsw_Type()
)
smSiaResourceUsageIcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaResourceUsageIcsw.setStatus("mandatory")
_SmSiaProgramMessages_ObjectIdentity = ObjectIdentity
smSiaProgramMessages = _SmSiaProgramMessages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12)
)
_SmSiaProgramMessagesTable_Object = MibTable
smSiaProgramMessagesTable = _SmSiaProgramMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12, 1)
)
if mibBuilder.loadTexts:
    smSiaProgramMessagesTable.setStatus("mandatory")
_SmSiaProgramMessagesEntry_Object = MibTableRow
smSiaProgramMessagesEntry = _SmSiaProgramMessagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12, 1, 1)
)
smSiaProgramMessagesEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaProgramMessagesRowNumber"),
)
if mibBuilder.loadTexts:
    smSiaProgramMessagesEntry.setStatus("mandatory")
_SmSiaProgramMessagesRowNumber_Type = Integer32
_SmSiaProgramMessagesRowNumber_Object = MibTableColumn
smSiaProgramMessagesRowNumber = _SmSiaProgramMessagesRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12, 1, 1, 1),
    _SmSiaProgramMessagesRowNumber_Type()
)
smSiaProgramMessagesRowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramMessagesRowNumber.setStatus("mandatory")
_SmSiaProgramMessagesTime_Type = DisplayString
_SmSiaProgramMessagesTime_Object = MibTableColumn
smSiaProgramMessagesTime = _SmSiaProgramMessagesTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12, 1, 1, 2),
    _SmSiaProgramMessagesTime_Type()
)
smSiaProgramMessagesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramMessagesTime.setStatus("mandatory")
_SmSiaProgramMessagesText_Type = DisplayString
_SmSiaProgramMessagesText_Object = MibTableColumn
smSiaProgramMessagesText = _SmSiaProgramMessagesText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12, 1, 1, 3),
    _SmSiaProgramMessagesText_Type()
)
smSiaProgramMessagesText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramMessagesText.setStatus("mandatory")
_SmSiaProgramMessagesTimeStamp_Type = Integer32
_SmSiaProgramMessagesTimeStamp_Object = MibTableColumn
smSiaProgramMessagesTimeStamp = _SmSiaProgramMessagesTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 12, 1, 1, 4),
    _SmSiaProgramMessagesTimeStamp_Type()
)
smSiaProgramMessagesTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaProgramMessagesTimeStamp.setStatus("mandatory")
_SmSiaSystemInformation_ObjectIdentity = ObjectIdentity
smSiaSystemInformation = _SmSiaSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2)
)
_SmSiaSystemDescription_ObjectIdentity = ObjectIdentity
smSiaSystemDescription = _SmSiaSystemDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1)
)
_SmSiaSystemNodeName_Type = DisplayString
_SmSiaSystemNodeName_Object = MibScalar
smSiaSystemNodeName = _SmSiaSystemNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 1),
    _SmSiaSystemNodeName_Type()
)
smSiaSystemNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemNodeName.setStatus("mandatory")
_SmSiaSystemSysName_Type = DisplayString
_SmSiaSystemSysName_Object = MibScalar
smSiaSystemSysName = _SmSiaSystemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 2),
    _SmSiaSystemSysName_Type()
)
smSiaSystemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSysName.setStatus("mandatory")
_SmSiaSystemVersion_Type = DisplayString
_SmSiaSystemVersion_Object = MibScalar
smSiaSystemVersion = _SmSiaSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 3),
    _SmSiaSystemVersion_Type()
)
smSiaSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemVersion.setStatus("mandatory")
_SmSiaSystemRelease_Type = DisplayString
_SmSiaSystemRelease_Object = MibScalar
smSiaSystemRelease = _SmSiaSystemRelease_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 4),
    _SmSiaSystemRelease_Type()
)
smSiaSystemRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemRelease.setStatus("mandatory")
_SmSiaSystemMachine_Type = DisplayString
_SmSiaSystemMachine_Object = MibScalar
smSiaSystemMachine = _SmSiaSystemMachine_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 5),
    _SmSiaSystemMachine_Type()
)
smSiaSystemMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMachine.setStatus("mandatory")
_SmSiaSystemTime_Type = DisplayString
_SmSiaSystemTime_Object = MibScalar
smSiaSystemTime = _SmSiaSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 6),
    _SmSiaSystemTime_Type()
)
smSiaSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemTime.setStatus("mandatory")
_SmSiaSystemConfiguration_ObjectIdentity = ObjectIdentity
smSiaSystemConfiguration = _SmSiaSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2)
)
_SmSiaSystemBufferPoolMark_Type = Integer32
_SmSiaSystemBufferPoolMark_Object = MibScalar
smSiaSystemBufferPoolMark = _SmSiaSystemBufferPoolMark_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 1),
    _SmSiaSystemBufferPoolMark_Type()
)
smSiaSystemBufferPoolMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemBufferPoolMark.setStatus("mandatory")
_SmSiaSystemMaxMbufs_Type = Integer32
_SmSiaSystemMaxMbufs_Object = MibScalar
smSiaSystemMaxMbufs = _SmSiaSystemMaxMbufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 2),
    _SmSiaSystemMaxMbufs_Type()
)
smSiaSystemMaxMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMaxMbufs.setStatus("mandatory")
_SmSiaSystemMaxUserProcesses_Type = Integer32
_SmSiaSystemMaxUserProcesses_Object = MibScalar
smSiaSystemMaxUserProcesses = _SmSiaSystemMaxUserProcesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 3),
    _SmSiaSystemMaxUserProcesses_Type()
)
smSiaSystemMaxUserProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMaxUserProcesses.setStatus("mandatory")
_SmSiaSystemMaxSystemProcesses_Type = Integer32
_SmSiaSystemMaxSystemProcesses_Object = MibScalar
smSiaSystemMaxSystemProcesses = _SmSiaSystemMaxSystemProcesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 4),
    _SmSiaSystemMaxSystemProcesses_Type()
)
smSiaSystemMaxSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMaxSystemProcesses.setStatus("mandatory")
_SmSiaSystemRecordLockTableSize_Type = Integer32
_SmSiaSystemRecordLockTableSize_Object = MibScalar
smSiaSystemRecordLockTableSize = _SmSiaSystemRecordLockTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 5),
    _SmSiaSystemRecordLockTableSize_Type()
)
smSiaSystemRecordLockTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemRecordLockTableSize.setStatus("mandatory")
_SmSiaSystemOpenFileTableSize_Type = Integer32
_SmSiaSystemOpenFileTableSize_Object = MibScalar
smSiaSystemOpenFileTableSize = _SmSiaSystemOpenFileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 6),
    _SmSiaSystemOpenFileTableSize_Type()
)
smSiaSystemOpenFileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemOpenFileTableSize.setStatus("mandatory")
_SmSiaSystemCBlockArraySize_Type = Integer32
_SmSiaSystemCBlockArraySize_Object = MibScalar
smSiaSystemCBlockArraySize = _SmSiaSystemCBlockArraySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 7),
    _SmSiaSystemCBlockArraySize_Type()
)
smSiaSystemCBlockArraySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemCBlockArraySize.setStatus("mandatory")


class _SmSiaSystemDiskIOHistory_Type(Integer32):
    """Custom type smSiaSystemDiskIOHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SmSiaSystemDiskIOHistory_Type.__name__ = "Integer32"
_SmSiaSystemDiskIOHistory_Object = MibScalar
smSiaSystemDiskIOHistory = _SmSiaSystemDiskIOHistory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 8),
    _SmSiaSystemDiskIOHistory_Type()
)
smSiaSystemDiskIOHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDiskIOHistory.setStatus("mandatory")


class _SmSiaSystemAutomaticBootAfterHalt_Type(Integer32):
    """Custom type smSiaSystemAutomaticBootAfterHalt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SmSiaSystemAutomaticBootAfterHalt_Type.__name__ = "Integer32"
_SmSiaSystemAutomaticBootAfterHalt_Object = MibScalar
smSiaSystemAutomaticBootAfterHalt = _SmSiaSystemAutomaticBootAfterHalt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 9),
    _SmSiaSystemAutomaticBootAfterHalt_Type()
)
smSiaSystemAutomaticBootAfterHalt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemAutomaticBootAfterHalt.setStatus("mandatory")


class _SmSiaSystemMemScrub_Type(Integer32):
    """Custom type smSiaSystemMemScrub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SmSiaSystemMemScrub_Type.__name__ = "Integer32"
_SmSiaSystemMemScrub_Object = MibScalar
smSiaSystemMemScrub = _SmSiaSystemMemScrub_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 10),
    _SmSiaSystemMemScrub_Type()
)
smSiaSystemMemScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMemScrub.setStatus("mandatory")
_SmSiaSystemLeastPriv_Type = Integer32
_SmSiaSystemLeastPriv_Object = MibScalar
smSiaSystemLeastPriv = _SmSiaSystemLeastPriv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 11),
    _SmSiaSystemLeastPriv_Type()
)
smSiaSystemLeastPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemLeastPriv.setStatus("mandatory")
_SmSiaSystemMaxPout_Type = Integer32
_SmSiaSystemMaxPout_Object = MibScalar
smSiaSystemMaxPout = _SmSiaSystemMaxPout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 12),
    _SmSiaSystemMaxPout_Type()
)
smSiaSystemMaxPout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMaxPout.setStatus("mandatory")
_SmSiaSystemMinPout_Type = Integer32
_SmSiaSystemMinPout_Object = MibScalar
smSiaSystemMinPout = _SmSiaSystemMinPout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 13),
    _SmSiaSystemMinPout_Type()
)
smSiaSystemMinPout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMinPout.setStatus("mandatory")
_SmSiaSystemPageSize_Type = Integer32
_SmSiaSystemPageSize_Object = MibScalar
smSiaSystemPageSize = _SmSiaSystemPageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 14),
    _SmSiaSystemPageSize_Type()
)
smSiaSystemPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPageSize.setStatus("mandatory")
_SmSiaSystemProcessMaxOpenFiles_Type = Integer32
_SmSiaSystemProcessMaxOpenFiles_Object = MibScalar
smSiaSystemProcessMaxOpenFiles = _SmSiaSystemProcessMaxOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 15),
    _SmSiaSystemProcessMaxOpenFiles_Type()
)
smSiaSystemProcessMaxOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessMaxOpenFiles.setStatus("mandatory")
_SmSiaSystemProcessMaxOpenStreams_Type = Integer32
_SmSiaSystemProcessMaxOpenStreams_Object = MibScalar
smSiaSystemProcessMaxOpenStreams = _SmSiaSystemProcessMaxOpenStreams_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 16),
    _SmSiaSystemProcessMaxOpenStreams_Type()
)
smSiaSystemProcessMaxOpenStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessMaxOpenStreams.setStatus("mandatory")
_SmSiaSystemProcessDescriptorTableSize_Type = Integer32
_SmSiaSystemProcessDescriptorTableSize_Object = MibScalar
smSiaSystemProcessDescriptorTableSize = _SmSiaSystemProcessDescriptorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 17),
    _SmSiaSystemProcessDescriptorTableSize_Type()
)
smSiaSystemProcessDescriptorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessDescriptorTableSize.setStatus("mandatory")
_SmSiaSystemPhysicalMemorySize_Type = Integer32
_SmSiaSystemPhysicalMemorySize_Object = MibScalar
smSiaSystemPhysicalMemorySize = _SmSiaSystemPhysicalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 18),
    _SmSiaSystemPhysicalMemorySize_Type()
)
smSiaSystemPhysicalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPhysicalMemorySize.setStatus("mandatory")
_SmSiaSystemDevice_ObjectIdentity = ObjectIdentity
smSiaSystemDevice = _SmSiaSystemDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3)
)
_SmSiaSystemDeviceList_ObjectIdentity = ObjectIdentity
smSiaSystemDeviceList = _SmSiaSystemDeviceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1)
)
_SmSiaSystemDeviceListInstalled_Type = Integer32
_SmSiaSystemDeviceListInstalled_Object = MibScalar
smSiaSystemDeviceListInstalled = _SmSiaSystemDeviceListInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 1),
    _SmSiaSystemDeviceListInstalled_Type()
)
smSiaSystemDeviceListInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListInstalled.setStatus("mandatory")
_SmSiaSystemDeviceListTable_Object = MibTable
smSiaSystemDeviceListTable = _SmSiaSystemDeviceListTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceListTable.setStatus("mandatory")
_SmSiaSystemDeviceListEntry_Object = MibTableRow
smSiaSystemDeviceListEntry = _SmSiaSystemDeviceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1)
)
smSiaSystemDeviceListEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemDeviceListName"),
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceListEntry.setStatus("mandatory")
_SmSiaSystemDeviceListName_Type = DisplayString
_SmSiaSystemDeviceListName_Object = MibTableColumn
smSiaSystemDeviceListName = _SmSiaSystemDeviceListName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 1),
    _SmSiaSystemDeviceListName_Type()
)
smSiaSystemDeviceListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListName.setStatus("mandatory")
_SmSiaSystemDeviceListDescription_Type = DisplayString
_SmSiaSystemDeviceListDescription_Object = MibTableColumn
smSiaSystemDeviceListDescription = _SmSiaSystemDeviceListDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 2),
    _SmSiaSystemDeviceListDescription_Type()
)
smSiaSystemDeviceListDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListDescription.setStatus("mandatory")
_SmSiaSystemDeviceListLocation_Type = DisplayString
_SmSiaSystemDeviceListLocation_Object = MibTableColumn
smSiaSystemDeviceListLocation = _SmSiaSystemDeviceListLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 3),
    _SmSiaSystemDeviceListLocation_Type()
)
smSiaSystemDeviceListLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListLocation.setStatus("mandatory")
_SmSiaSystemDeviceListVPD_Type = DisplayString
_SmSiaSystemDeviceListVPD_Object = MibTableColumn
smSiaSystemDeviceListVPD = _SmSiaSystemDeviceListVPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 4),
    _SmSiaSystemDeviceListVPD_Type()
)
smSiaSystemDeviceListVPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListVPD.setStatus("mandatory")
_SmSiaSystemDeviceListAttributes_Type = DisplayString
_SmSiaSystemDeviceListAttributes_Object = MibTableColumn
smSiaSystemDeviceListAttributes = _SmSiaSystemDeviceListAttributes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 5),
    _SmSiaSystemDeviceListAttributes_Type()
)
smSiaSystemDeviceListAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListAttributes.setStatus("mandatory")
_SmSiaSystemDeviceListDiagnostics_Type = DisplayString
_SmSiaSystemDeviceListDiagnostics_Object = MibTableColumn
smSiaSystemDeviceListDiagnostics = _SmSiaSystemDeviceListDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 6),
    _SmSiaSystemDeviceListDiagnostics_Type()
)
smSiaSystemDeviceListDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceListDiagnostics.setStatus("mandatory")
_SmSiaSystemDeviceTokenRing_ObjectIdentity = ObjectIdentity
smSiaSystemDeviceTokenRing = _SmSiaSystemDeviceTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2)
)
_SmSiaSystemDeviceTokenRingInstalled_Type = Integer32
_SmSiaSystemDeviceTokenRingInstalled_Object = MibScalar
smSiaSystemDeviceTokenRingInstalled = _SmSiaSystemDeviceTokenRingInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 1),
    _SmSiaSystemDeviceTokenRingInstalled_Type()
)
smSiaSystemDeviceTokenRingInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingInstalled.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTable_Object = MibTable
smSiaSystemDeviceTokenRingTable = _SmSiaSystemDeviceTokenRingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTable.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingEntry_Object = MibTableRow
smSiaSystemDeviceTokenRingEntry = _SmSiaSystemDeviceTokenRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1)
)
smSiaSystemDeviceTokenRingEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemDeviceTokenRingNumber"),
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingEntry.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingNumber_Type = Integer32
_SmSiaSystemDeviceTokenRingNumber_Object = MibTableColumn
smSiaSystemDeviceTokenRingNumber = _SmSiaSystemDeviceTokenRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 1),
    _SmSiaSystemDeviceTokenRingNumber_Type()
)
smSiaSystemDeviceTokenRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingNumber.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingHardwareAddress_Type = PhysAddress
_SmSiaSystemDeviceTokenRingHardwareAddress_Object = MibTableColumn
smSiaSystemDeviceTokenRingHardwareAddress = _SmSiaSystemDeviceTokenRingHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 2),
    _SmSiaSystemDeviceTokenRingHardwareAddress_Type()
)
smSiaSystemDeviceTokenRingHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingHardwareAddress.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingCurrentAddress_Type = PhysAddress
_SmSiaSystemDeviceTokenRingCurrentAddress_Object = MibTableColumn
smSiaSystemDeviceTokenRingCurrentAddress = _SmSiaSystemDeviceTokenRingCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 3),
    _SmSiaSystemDeviceTokenRingCurrentAddress_Type()
)
smSiaSystemDeviceTokenRingCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingCurrentAddress.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingReceiveDataOffset_Type = Integer32
_SmSiaSystemDeviceTokenRingReceiveDataOffset_Object = MibTableColumn
smSiaSystemDeviceTokenRingReceiveDataOffset = _SmSiaSystemDeviceTokenRingReceiveDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 4),
    _SmSiaSystemDeviceTokenRingReceiveDataOffset_Type()
)
smSiaSystemDeviceTokenRingReceiveDataOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingReceiveDataOffset.setStatus("mandatory")


class _SmSiaSystemDeviceTokenRingBroadwrap_Type(Integer32):
    """Custom type smSiaSystemDeviceTokenRingBroadwrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SmSiaSystemDeviceTokenRingBroadwrap_Type.__name__ = "Integer32"
_SmSiaSystemDeviceTokenRingBroadwrap_Object = MibTableColumn
smSiaSystemDeviceTokenRingBroadwrap = _SmSiaSystemDeviceTokenRingBroadwrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 5),
    _SmSiaSystemDeviceTokenRingBroadwrap_Type()
)
smSiaSystemDeviceTokenRingBroadwrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingBroadwrap.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxByteMcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingTxByteMcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxByteMcnt = _SmSiaSystemDeviceTokenRingTxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 6),
    _SmSiaSystemDeviceTokenRingTxByteMcnt_Type()
)
smSiaSystemDeviceTokenRingTxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxByteMcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxByteLcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingTxByteLcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxByteLcnt = _SmSiaSystemDeviceTokenRingTxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 7),
    _SmSiaSystemDeviceTokenRingTxByteLcnt_Type()
)
smSiaSystemDeviceTokenRingTxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxByteLcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxByteMcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxByteMcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxByteMcnt = _SmSiaSystemDeviceTokenRingRxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 8),
    _SmSiaSystemDeviceTokenRingRxByteMcnt_Type()
)
smSiaSystemDeviceTokenRingRxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxByteMcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxByteLcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxByteLcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxByteLcnt = _SmSiaSystemDeviceTokenRingRxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 9),
    _SmSiaSystemDeviceTokenRingRxByteLcnt_Type()
)
smSiaSystemDeviceTokenRingRxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxByteLcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxFrameMcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingTxFrameMcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxFrameMcnt = _SmSiaSystemDeviceTokenRingTxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 10),
    _SmSiaSystemDeviceTokenRingTxFrameMcnt_Type()
)
smSiaSystemDeviceTokenRingTxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxFrameMcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxFrameLcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingTxFrameLcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxFrameLcnt = _SmSiaSystemDeviceTokenRingTxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 11),
    _SmSiaSystemDeviceTokenRingTxFrameLcnt_Type()
)
smSiaSystemDeviceTokenRingTxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxFrameLcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxFrameMcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxFrameMcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxFrameMcnt = _SmSiaSystemDeviceTokenRingRxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 12),
    _SmSiaSystemDeviceTokenRingRxFrameMcnt_Type()
)
smSiaSystemDeviceTokenRingRxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxFrameMcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxFrameLcnt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxFrameLcnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxFrameLcnt = _SmSiaSystemDeviceTokenRingRxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 13),
    _SmSiaSystemDeviceTokenRingRxFrameLcnt_Type()
)
smSiaSystemDeviceTokenRingRxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxFrameLcnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxErrCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingTxErrCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxErrCnt = _SmSiaSystemDeviceTokenRingTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 14),
    _SmSiaSystemDeviceTokenRingTxErrCnt_Type()
)
smSiaSystemDeviceTokenRingTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxErrCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxErrCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxErrCnt = _SmSiaSystemDeviceTokenRingRxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 15),
    _SmSiaSystemDeviceTokenRingRxErrCnt_Type()
)
smSiaSystemDeviceTokenRingRxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingNidTblHigh_Type = Integer32
_SmSiaSystemDeviceTokenRingNidTblHigh_Object = MibTableColumn
smSiaSystemDeviceTokenRingNidTblHigh = _SmSiaSystemDeviceTokenRingNidTblHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 16),
    _SmSiaSystemDeviceTokenRingNidTblHigh_Type()
)
smSiaSystemDeviceTokenRingNidTblHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingNidTblHigh.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxQueHigh_Type = Gauge32
_SmSiaSystemDeviceTokenRingTxQueHigh_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxQueHigh = _SmSiaSystemDeviceTokenRingTxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 17),
    _SmSiaSystemDeviceTokenRingTxQueHigh_Type()
)
smSiaSystemDeviceTokenRingTxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxQueHigh_Type = Gauge32
_SmSiaSystemDeviceTokenRingRxQueHigh_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxQueHigh = _SmSiaSystemDeviceTokenRingRxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 18),
    _SmSiaSystemDeviceTokenRingRxQueHigh_Type()
)
smSiaSystemDeviceTokenRingRxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingStaQueHigh_Type = Gauge32
_SmSiaSystemDeviceTokenRingStaQueHigh_Object = MibTableColumn
smSiaSystemDeviceTokenRingStaQueHigh = _SmSiaSystemDeviceTokenRingStaQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 19),
    _SmSiaSystemDeviceTokenRingStaQueHigh_Type()
)
smSiaSystemDeviceTokenRingStaQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingStaQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingIntrLost_Type = Counter32
_SmSiaSystemDeviceTokenRingIntrLost_Object = MibTableColumn
smSiaSystemDeviceTokenRingIntrLost = _SmSiaSystemDeviceTokenRingIntrLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 20),
    _SmSiaSystemDeviceTokenRingIntrLost_Type()
)
smSiaSystemDeviceTokenRingIntrLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingIntrLost.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingWdtLost_Type = Counter32
_SmSiaSystemDeviceTokenRingWdtLost_Object = MibTableColumn
smSiaSystemDeviceTokenRingWdtLost = _SmSiaSystemDeviceTokenRingWdtLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 21),
    _SmSiaSystemDeviceTokenRingWdtLost_Type()
)
smSiaSystemDeviceTokenRingWdtLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingWdtLost.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTimoLost_Type = Counter32
_SmSiaSystemDeviceTokenRingTimoLost_Object = MibTableColumn
smSiaSystemDeviceTokenRingTimoLost = _SmSiaSystemDeviceTokenRingTimoLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 22),
    _SmSiaSystemDeviceTokenRingTimoLost_Type()
)
smSiaSystemDeviceTokenRingTimoLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTimoLost.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingStaQueOverflow_Type = Counter32
_SmSiaSystemDeviceTokenRingStaQueOverflow_Object = MibTableColumn
smSiaSystemDeviceTokenRingStaQueOverflow = _SmSiaSystemDeviceTokenRingStaQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 23),
    _SmSiaSystemDeviceTokenRingStaQueOverflow_Type()
)
smSiaSystemDeviceTokenRingStaQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingStaQueOverflow.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxQueOverflow_Type = Counter32
_SmSiaSystemDeviceTokenRingRxQueOverflow_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxQueOverflow = _SmSiaSystemDeviceTokenRingRxQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 24),
    _SmSiaSystemDeviceTokenRingRxQueOverflow_Type()
)
smSiaSystemDeviceTokenRingRxQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxQueOverflow.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxQueNoMbuf_Type = Counter32
_SmSiaSystemDeviceTokenRingRxQueNoMbuf_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxQueNoMbuf = _SmSiaSystemDeviceTokenRingRxQueNoMbuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 25),
    _SmSiaSystemDeviceTokenRingRxQueNoMbuf_Type()
)
smSiaSystemDeviceTokenRingRxQueNoMbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxQueNoMbuf.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxQueNoMbufExt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxQueNoMbufExt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxQueNoMbufExt = _SmSiaSystemDeviceTokenRingRxQueNoMbufExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 26),
    _SmSiaSystemDeviceTokenRingRxQueNoMbufExt_Type()
)
smSiaSystemDeviceTokenRingRxQueNoMbufExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxQueNoMbufExt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxIntrCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingTxIntrCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxIntrCnt = _SmSiaSystemDeviceTokenRingTxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 27),
    _SmSiaSystemDeviceTokenRingTxIntrCnt_Type()
)
smSiaSystemDeviceTokenRingTxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxIntrCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRxIntrCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingRxIntrCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingRxIntrCnt = _SmSiaSystemDeviceTokenRingRxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 28),
    _SmSiaSystemDeviceTokenRingRxIntrCnt_Type()
)
smSiaSystemDeviceTokenRingRxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRxIntrCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingPktRejCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingPktRejCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingPktRejCnt = _SmSiaSystemDeviceTokenRingPktRejCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 29),
    _SmSiaSystemDeviceTokenRingPktRejCnt_Type()
)
smSiaSystemDeviceTokenRingPktRejCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingPktRejCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingPktAccCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingPktAccCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingPktAccCnt = _SmSiaSystemDeviceTokenRingPktAccCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 30),
    _SmSiaSystemDeviceTokenRingPktAccCnt_Type()
)
smSiaSystemDeviceTokenRingPktAccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingPktAccCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingPktTxCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingPktTxCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingPktTxCnt = _SmSiaSystemDeviceTokenRingPktTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 31),
    _SmSiaSystemDeviceTokenRingPktTxCnt_Type()
)
smSiaSystemDeviceTokenRingPktTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingPktTxCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingOvfloPktCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingOvfloPktCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingOvfloPktCnt = _SmSiaSystemDeviceTokenRingOvfloPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 32),
    _SmSiaSystemDeviceTokenRingOvfloPktCnt_Type()
)
smSiaSystemDeviceTokenRingOvfloPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingOvfloPktCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingPktTxErrCnt_Type = Counter32
_SmSiaSystemDeviceTokenRingPktTxErrCnt_Object = MibTableColumn
smSiaSystemDeviceTokenRingPktTxErrCnt = _SmSiaSystemDeviceTokenRingPktTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 33),
    _SmSiaSystemDeviceTokenRingPktTxErrCnt_Type()
)
smSiaSystemDeviceTokenRingPktTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingPktTxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingSpeed_Type = Integer32
_SmSiaSystemDeviceTokenRingSpeed_Object = MibTableColumn
smSiaSystemDeviceTokenRingSpeed = _SmSiaSystemDeviceTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 34),
    _SmSiaSystemDeviceTokenRingSpeed_Type()
)
smSiaSystemDeviceTokenRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingSpeed.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingVPD_Type = DisplayString
_SmSiaSystemDeviceTokenRingVPD_Object = MibTableColumn
smSiaSystemDeviceTokenRingVPD = _SmSiaSystemDeviceTokenRingVPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 35),
    _SmSiaSystemDeviceTokenRingVPD_Type()
)
smSiaSystemDeviceTokenRingVPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingVPD.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingAdapPhysAddr_Type = PhysAddress
_SmSiaSystemDeviceTokenRingAdapPhysAddr_Object = MibTableColumn
smSiaSystemDeviceTokenRingAdapPhysAddr = _SmSiaSystemDeviceTokenRingAdapPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 36),
    _SmSiaSystemDeviceTokenRingAdapPhysAddr_Type()
)
smSiaSystemDeviceTokenRingAdapPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingAdapPhysAddr.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingUpstreamNodeAddr_Type = PhysAddress
_SmSiaSystemDeviceTokenRingUpstreamNodeAddr_Object = MibTableColumn
smSiaSystemDeviceTokenRingUpstreamNodeAddr = _SmSiaSystemDeviceTokenRingUpstreamNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 37),
    _SmSiaSystemDeviceTokenRingUpstreamNodeAddr_Type()
)
smSiaSystemDeviceTokenRingUpstreamNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingUpstreamNodeAddr.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingUpstreamPhysAddr_Type = PhysAddress
_SmSiaSystemDeviceTokenRingUpstreamPhysAddr_Object = MibTableColumn
smSiaSystemDeviceTokenRingUpstreamPhysAddr = _SmSiaSystemDeviceTokenRingUpstreamPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 38),
    _SmSiaSystemDeviceTokenRingUpstreamPhysAddr_Type()
)
smSiaSystemDeviceTokenRingUpstreamPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingUpstreamPhysAddr.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingLastPollAddr_Type = PhysAddress
_SmSiaSystemDeviceTokenRingLastPollAddr_Object = MibTableColumn
smSiaSystemDeviceTokenRingLastPollAddr = _SmSiaSystemDeviceTokenRingLastPollAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 39),
    _SmSiaSystemDeviceTokenRingLastPollAddr_Type()
)
smSiaSystemDeviceTokenRingLastPollAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingLastPollAddr.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingAuthorEnv_Type = Integer32
_SmSiaSystemDeviceTokenRingAuthorEnv_Object = MibTableColumn
smSiaSystemDeviceTokenRingAuthorEnv = _SmSiaSystemDeviceTokenRingAuthorEnv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 40),
    _SmSiaSystemDeviceTokenRingAuthorEnv_Type()
)
smSiaSystemDeviceTokenRingAuthorEnv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingAuthorEnv.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingTxAccessPriority_Type = Integer32
_SmSiaSystemDeviceTokenRingTxAccessPriority_Object = MibTableColumn
smSiaSystemDeviceTokenRingTxAccessPriority = _SmSiaSystemDeviceTokenRingTxAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 41),
    _SmSiaSystemDeviceTokenRingTxAccessPriority_Type()
)
smSiaSystemDeviceTokenRingTxAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingTxAccessPriority.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingSrcClassAuthor_Type = Integer32
_SmSiaSystemDeviceTokenRingSrcClassAuthor_Object = MibTableColumn
smSiaSystemDeviceTokenRingSrcClassAuthor = _SmSiaSystemDeviceTokenRingSrcClassAuthor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 42),
    _SmSiaSystemDeviceTokenRingSrcClassAuthor_Type()
)
smSiaSystemDeviceTokenRingSrcClassAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingSrcClassAuthor.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingLastAttenCode_Type = Integer32
_SmSiaSystemDeviceTokenRingLastAttenCode_Object = MibTableColumn
smSiaSystemDeviceTokenRingLastAttenCode = _SmSiaSystemDeviceTokenRingLastAttenCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 43),
    _SmSiaSystemDeviceTokenRingLastAttenCode_Type()
)
smSiaSystemDeviceTokenRingLastAttenCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingLastAttenCode.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingLastSrcAddr_Type = PhysAddress
_SmSiaSystemDeviceTokenRingLastSrcAddr_Object = MibTableColumn
smSiaSystemDeviceTokenRingLastSrcAddr = _SmSiaSystemDeviceTokenRingLastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 44),
    _SmSiaSystemDeviceTokenRingLastSrcAddr_Type()
)
smSiaSystemDeviceTokenRingLastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingLastSrcAddr.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingLastBeaconType_Type = Integer32
_SmSiaSystemDeviceTokenRingLastBeaconType_Object = MibTableColumn
smSiaSystemDeviceTokenRingLastBeaconType = _SmSiaSystemDeviceTokenRingLastBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 45),
    _SmSiaSystemDeviceTokenRingLastBeaconType_Type()
)
smSiaSystemDeviceTokenRingLastBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingLastBeaconType.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingLastMajorVector_Type = Integer32
_SmSiaSystemDeviceTokenRingLastMajorVector_Object = MibTableColumn
smSiaSystemDeviceTokenRingLastMajorVector = _SmSiaSystemDeviceTokenRingLastMajorVector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 46),
    _SmSiaSystemDeviceTokenRingLastMajorVector_Type()
)
smSiaSystemDeviceTokenRingLastMajorVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingLastMajorVector.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingRingStatus_Type = Integer32
_SmSiaSystemDeviceTokenRingRingStatus_Object = MibTableColumn
smSiaSystemDeviceTokenRingRingStatus = _SmSiaSystemDeviceTokenRingRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 47),
    _SmSiaSystemDeviceTokenRingRingStatus_Type()
)
smSiaSystemDeviceTokenRingRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingRingStatus.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingSoftErrorTimerVal_Type = Integer32
_SmSiaSystemDeviceTokenRingSoftErrorTimerVal_Object = MibTableColumn
smSiaSystemDeviceTokenRingSoftErrorTimerVal = _SmSiaSystemDeviceTokenRingSoftErrorTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 48),
    _SmSiaSystemDeviceTokenRingSoftErrorTimerVal_Type()
)
smSiaSystemDeviceTokenRingSoftErrorTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingSoftErrorTimerVal.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingFrontEndTimerVal_Type = Integer32
_SmSiaSystemDeviceTokenRingFrontEndTimerVal_Object = MibTableColumn
smSiaSystemDeviceTokenRingFrontEndTimerVal = _SmSiaSystemDeviceTokenRingFrontEndTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 49),
    _SmSiaSystemDeviceTokenRingFrontEndTimerVal_Type()
)
smSiaSystemDeviceTokenRingFrontEndTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingFrontEndTimerVal.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingMonitorErrorCode_Type = Integer32
_SmSiaSystemDeviceTokenRingMonitorErrorCode_Object = MibTableColumn
smSiaSystemDeviceTokenRingMonitorErrorCode = _SmSiaSystemDeviceTokenRingMonitorErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 50),
    _SmSiaSystemDeviceTokenRingMonitorErrorCode_Type()
)
smSiaSystemDeviceTokenRingMonitorErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingMonitorErrorCode.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingBeaconTxType_Type = Integer32
_SmSiaSystemDeviceTokenRingBeaconTxType_Object = MibTableColumn
smSiaSystemDeviceTokenRingBeaconTxType = _SmSiaSystemDeviceTokenRingBeaconTxType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 51),
    _SmSiaSystemDeviceTokenRingBeaconTxType_Type()
)
smSiaSystemDeviceTokenRingBeaconTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingBeaconTxType.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingBeaconRxType_Type = Integer32
_SmSiaSystemDeviceTokenRingBeaconRxType_Object = MibTableColumn
smSiaSystemDeviceTokenRingBeaconRxType = _SmSiaSystemDeviceTokenRingBeaconRxType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 52),
    _SmSiaSystemDeviceTokenRingBeaconRxType_Type()
)
smSiaSystemDeviceTokenRingBeaconRxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingBeaconRxType.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingFrameCorrSave_Type = Integer32
_SmSiaSystemDeviceTokenRingFrameCorrSave_Object = MibTableColumn
smSiaSystemDeviceTokenRingFrameCorrSave = _SmSiaSystemDeviceTokenRingFrameCorrSave_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 53),
    _SmSiaSystemDeviceTokenRingFrameCorrSave_Type()
)
smSiaSystemDeviceTokenRingFrameCorrSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingFrameCorrSave.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingBeaconStationNAUN_Type = PhysAddress
_SmSiaSystemDeviceTokenRingBeaconStationNAUN_Object = MibTableColumn
smSiaSystemDeviceTokenRingBeaconStationNAUN = _SmSiaSystemDeviceTokenRingBeaconStationNAUN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 54),
    _SmSiaSystemDeviceTokenRingBeaconStationNAUN_Type()
)
smSiaSystemDeviceTokenRingBeaconStationNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingBeaconStationNAUN.setStatus("mandatory")
_SmSiaSystemDeviceTokenRingBeaconStationPhysAddr_Type = PhysAddress
_SmSiaSystemDeviceTokenRingBeaconStationPhysAddr_Object = MibTableColumn
smSiaSystemDeviceTokenRingBeaconStationPhysAddr = _SmSiaSystemDeviceTokenRingBeaconStationPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 55),
    _SmSiaSystemDeviceTokenRingBeaconStationPhysAddr_Type()
)
smSiaSystemDeviceTokenRingBeaconStationPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingBeaconStationPhysAddr.setStatus("mandatory")


class _SmSiaSystemDeviceTokenRingClear_Type(Integer32):
    """Custom type smSiaSystemDeviceTokenRingClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("normal", 1))
    )


_SmSiaSystemDeviceTokenRingClear_Type.__name__ = "Integer32"
_SmSiaSystemDeviceTokenRingClear_Object = MibTableColumn
smSiaSystemDeviceTokenRingClear = _SmSiaSystemDeviceTokenRingClear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 56),
    _SmSiaSystemDeviceTokenRingClear_Type()
)
smSiaSystemDeviceTokenRingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaSystemDeviceTokenRingClear.setStatus("mandatory")
_SmSiaSystemDeviceEthernet_ObjectIdentity = ObjectIdentity
smSiaSystemDeviceEthernet = _SmSiaSystemDeviceEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3)
)
_SmSiaSystemDeviceEthernetInstalled_Type = Integer32
_SmSiaSystemDeviceEthernetInstalled_Object = MibScalar
smSiaSystemDeviceEthernetInstalled = _SmSiaSystemDeviceEthernetInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 1),
    _SmSiaSystemDeviceEthernetInstalled_Type()
)
smSiaSystemDeviceEthernetInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetInstalled.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTable_Object = MibTable
smSiaSystemDeviceEthernetTable = _SmSiaSystemDeviceEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTable.setStatus("mandatory")
_SmSiaSystemDeviceEthernetEntry_Object = MibTableRow
smSiaSystemDeviceEthernetEntry = _SmSiaSystemDeviceEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1)
)
smSiaSystemDeviceEthernetEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemDeviceEthernetNumber"),
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetEntry.setStatus("mandatory")
_SmSiaSystemDeviceEthernetNumber_Type = Integer32
_SmSiaSystemDeviceEthernetNumber_Object = MibTableColumn
smSiaSystemDeviceEthernetNumber = _SmSiaSystemDeviceEthernetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 1),
    _SmSiaSystemDeviceEthernetNumber_Type()
)
smSiaSystemDeviceEthernetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetNumber.setStatus("mandatory")
_SmSiaSystemDeviceEthernetHardwareAddress_Type = PhysAddress
_SmSiaSystemDeviceEthernetHardwareAddress_Object = MibTableColumn
smSiaSystemDeviceEthernetHardwareAddress = _SmSiaSystemDeviceEthernetHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 2),
    _SmSiaSystemDeviceEthernetHardwareAddress_Type()
)
smSiaSystemDeviceEthernetHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetHardwareAddress.setStatus("mandatory")
_SmSiaSystemDeviceEthernetCurrentAddress_Type = PhysAddress
_SmSiaSystemDeviceEthernetCurrentAddress_Object = MibTableColumn
smSiaSystemDeviceEthernetCurrentAddress = _SmSiaSystemDeviceEthernetCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 3),
    _SmSiaSystemDeviceEthernetCurrentAddress_Type()
)
smSiaSystemDeviceEthernetCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetCurrentAddress.setStatus("mandatory")
_SmSiaSystemDeviceEthernetReceiveDataOffset_Type = Integer32
_SmSiaSystemDeviceEthernetReceiveDataOffset_Object = MibTableColumn
smSiaSystemDeviceEthernetReceiveDataOffset = _SmSiaSystemDeviceEthernetReceiveDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 4),
    _SmSiaSystemDeviceEthernetReceiveDataOffset_Type()
)
smSiaSystemDeviceEthernetReceiveDataOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetReceiveDataOffset.setStatus("mandatory")


class _SmSiaSystemDeviceEthernetBroadwrap_Type(Integer32):
    """Custom type smSiaSystemDeviceEthernetBroadwrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SmSiaSystemDeviceEthernetBroadwrap_Type.__name__ = "Integer32"
_SmSiaSystemDeviceEthernetBroadwrap_Object = MibTableColumn
smSiaSystemDeviceEthernetBroadwrap = _SmSiaSystemDeviceEthernetBroadwrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 5),
    _SmSiaSystemDeviceEthernetBroadwrap_Type()
)
smSiaSystemDeviceEthernetBroadwrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetBroadwrap.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxByteMcnt_Type = Counter32
_SmSiaSystemDeviceEthernetTxByteMcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetTxByteMcnt = _SmSiaSystemDeviceEthernetTxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 6),
    _SmSiaSystemDeviceEthernetTxByteMcnt_Type()
)
smSiaSystemDeviceEthernetTxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxByteMcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxByteLcnt_Type = Counter32
_SmSiaSystemDeviceEthernetTxByteLcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetTxByteLcnt = _SmSiaSystemDeviceEthernetTxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 7),
    _SmSiaSystemDeviceEthernetTxByteLcnt_Type()
)
smSiaSystemDeviceEthernetTxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxByteLcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxByteMcnt_Type = Counter32
_SmSiaSystemDeviceEthernetRxByteMcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxByteMcnt = _SmSiaSystemDeviceEthernetRxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 8),
    _SmSiaSystemDeviceEthernetRxByteMcnt_Type()
)
smSiaSystemDeviceEthernetRxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxByteMcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxByteLcnt_Type = Counter32
_SmSiaSystemDeviceEthernetRxByteLcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxByteLcnt = _SmSiaSystemDeviceEthernetRxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 9),
    _SmSiaSystemDeviceEthernetRxByteLcnt_Type()
)
smSiaSystemDeviceEthernetRxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxByteLcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxFrameMcnt_Type = Counter32
_SmSiaSystemDeviceEthernetTxFrameMcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetTxFrameMcnt = _SmSiaSystemDeviceEthernetTxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 10),
    _SmSiaSystemDeviceEthernetTxFrameMcnt_Type()
)
smSiaSystemDeviceEthernetTxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxFrameMcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxFrameLcnt_Type = Counter32
_SmSiaSystemDeviceEthernetTxFrameLcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetTxFrameLcnt = _SmSiaSystemDeviceEthernetTxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 11),
    _SmSiaSystemDeviceEthernetTxFrameLcnt_Type()
)
smSiaSystemDeviceEthernetTxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxFrameLcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxFrameMcnt_Type = Counter32
_SmSiaSystemDeviceEthernetRxFrameMcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxFrameMcnt = _SmSiaSystemDeviceEthernetRxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 12),
    _SmSiaSystemDeviceEthernetRxFrameMcnt_Type()
)
smSiaSystemDeviceEthernetRxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxFrameMcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxFrameLcnt_Type = Counter32
_SmSiaSystemDeviceEthernetRxFrameLcnt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxFrameLcnt = _SmSiaSystemDeviceEthernetRxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 13),
    _SmSiaSystemDeviceEthernetRxFrameLcnt_Type()
)
smSiaSystemDeviceEthernetRxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxFrameLcnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxErrCnt_Type = Counter32
_SmSiaSystemDeviceEthernetTxErrCnt_Object = MibTableColumn
smSiaSystemDeviceEthernetTxErrCnt = _SmSiaSystemDeviceEthernetTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 14),
    _SmSiaSystemDeviceEthernetTxErrCnt_Type()
)
smSiaSystemDeviceEthernetTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxErrCnt_Type = Counter32
_SmSiaSystemDeviceEthernetRxErrCnt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxErrCnt = _SmSiaSystemDeviceEthernetRxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 15),
    _SmSiaSystemDeviceEthernetRxErrCnt_Type()
)
smSiaSystemDeviceEthernetRxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetNidTblHigh_Type = Integer32
_SmSiaSystemDeviceEthernetNidTblHigh_Object = MibTableColumn
smSiaSystemDeviceEthernetNidTblHigh = _SmSiaSystemDeviceEthernetNidTblHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 16),
    _SmSiaSystemDeviceEthernetNidTblHigh_Type()
)
smSiaSystemDeviceEthernetNidTblHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetNidTblHigh.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxQueHigh_Type = Gauge32
_SmSiaSystemDeviceEthernetTxQueHigh_Object = MibTableColumn
smSiaSystemDeviceEthernetTxQueHigh = _SmSiaSystemDeviceEthernetTxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 17),
    _SmSiaSystemDeviceEthernetTxQueHigh_Type()
)
smSiaSystemDeviceEthernetTxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxQueHigh_Type = Gauge32
_SmSiaSystemDeviceEthernetRxQueHigh_Object = MibTableColumn
smSiaSystemDeviceEthernetRxQueHigh = _SmSiaSystemDeviceEthernetRxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 18),
    _SmSiaSystemDeviceEthernetRxQueHigh_Type()
)
smSiaSystemDeviceEthernetRxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceEthernetStaQueHigh_Type = Gauge32
_SmSiaSystemDeviceEthernetStaQueHigh_Object = MibTableColumn
smSiaSystemDeviceEthernetStaQueHigh = _SmSiaSystemDeviceEthernetStaQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 19),
    _SmSiaSystemDeviceEthernetStaQueHigh_Type()
)
smSiaSystemDeviceEthernetStaQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetStaQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceEthernetIntrLost_Type = Counter32
_SmSiaSystemDeviceEthernetIntrLost_Object = MibTableColumn
smSiaSystemDeviceEthernetIntrLost = _SmSiaSystemDeviceEthernetIntrLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 20),
    _SmSiaSystemDeviceEthernetIntrLost_Type()
)
smSiaSystemDeviceEthernetIntrLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetIntrLost.setStatus("mandatory")
_SmSiaSystemDeviceEthernetWdtLost_Type = Counter32
_SmSiaSystemDeviceEthernetWdtLost_Object = MibTableColumn
smSiaSystemDeviceEthernetWdtLost = _SmSiaSystemDeviceEthernetWdtLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 21),
    _SmSiaSystemDeviceEthernetWdtLost_Type()
)
smSiaSystemDeviceEthernetWdtLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetWdtLost.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTimoLost_Type = Counter32
_SmSiaSystemDeviceEthernetTimoLost_Object = MibTableColumn
smSiaSystemDeviceEthernetTimoLost = _SmSiaSystemDeviceEthernetTimoLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 22),
    _SmSiaSystemDeviceEthernetTimoLost_Type()
)
smSiaSystemDeviceEthernetTimoLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTimoLost.setStatus("mandatory")
_SmSiaSystemDeviceEthernetStaQueOverflow_Type = Counter32
_SmSiaSystemDeviceEthernetStaQueOverflow_Object = MibTableColumn
smSiaSystemDeviceEthernetStaQueOverflow = _SmSiaSystemDeviceEthernetStaQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 23),
    _SmSiaSystemDeviceEthernetStaQueOverflow_Type()
)
smSiaSystemDeviceEthernetStaQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetStaQueOverflow.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxQueOverflow_Type = Counter32
_SmSiaSystemDeviceEthernetRxQueOverflow_Object = MibTableColumn
smSiaSystemDeviceEthernetRxQueOverflow = _SmSiaSystemDeviceEthernetRxQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 24),
    _SmSiaSystemDeviceEthernetRxQueOverflow_Type()
)
smSiaSystemDeviceEthernetRxQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxQueOverflow.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxQueNoMbuf_Type = Counter32
_SmSiaSystemDeviceEthernetRxQueNoMbuf_Object = MibTableColumn
smSiaSystemDeviceEthernetRxQueNoMbuf = _SmSiaSystemDeviceEthernetRxQueNoMbuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 25),
    _SmSiaSystemDeviceEthernetRxQueNoMbuf_Type()
)
smSiaSystemDeviceEthernetRxQueNoMbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxQueNoMbuf.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxQueNoMbufExt_Type = Counter32
_SmSiaSystemDeviceEthernetRxQueNoMbufExt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxQueNoMbufExt = _SmSiaSystemDeviceEthernetRxQueNoMbufExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 26),
    _SmSiaSystemDeviceEthernetRxQueNoMbufExt_Type()
)
smSiaSystemDeviceEthernetRxQueNoMbufExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxQueNoMbufExt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxIntrCnt_Type = Counter32
_SmSiaSystemDeviceEthernetTxIntrCnt_Object = MibTableColumn
smSiaSystemDeviceEthernetTxIntrCnt = _SmSiaSystemDeviceEthernetTxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 27),
    _SmSiaSystemDeviceEthernetTxIntrCnt_Type()
)
smSiaSystemDeviceEthernetTxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxIntrCnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetRxIntrCnt_Type = Counter32
_SmSiaSystemDeviceEthernetRxIntrCnt_Object = MibTableColumn
smSiaSystemDeviceEthernetRxIntrCnt = _SmSiaSystemDeviceEthernetRxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 28),
    _SmSiaSystemDeviceEthernetRxIntrCnt_Type()
)
smSiaSystemDeviceEthernetRxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetRxIntrCnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetCRCErr_Type = Counter32
_SmSiaSystemDeviceEthernetCRCErr_Object = MibTableColumn
smSiaSystemDeviceEthernetCRCErr = _SmSiaSystemDeviceEthernetCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 29),
    _SmSiaSystemDeviceEthernetCRCErr_Type()
)
smSiaSystemDeviceEthernetCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetCRCErr.setStatus("mandatory")
_SmSiaSystemDeviceEthernetAlignErr_Type = Counter32
_SmSiaSystemDeviceEthernetAlignErr_Object = MibTableColumn
smSiaSystemDeviceEthernetAlignErr = _SmSiaSystemDeviceEthernetAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 30),
    _SmSiaSystemDeviceEthernetAlignErr_Type()
)
smSiaSystemDeviceEthernetAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetAlignErr.setStatus("mandatory")
_SmSiaSystemDeviceEthernetOverrun_Type = Counter32
_SmSiaSystemDeviceEthernetOverrun_Object = MibTableColumn
smSiaSystemDeviceEthernetOverrun = _SmSiaSystemDeviceEthernetOverrun_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 31),
    _SmSiaSystemDeviceEthernetOverrun_Type()
)
smSiaSystemDeviceEthernetOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetOverrun.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTooShort_Type = Counter32
_SmSiaSystemDeviceEthernetTooShort_Object = MibTableColumn
smSiaSystemDeviceEthernetTooShort = _SmSiaSystemDeviceEthernetTooShort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 32),
    _SmSiaSystemDeviceEthernetTooShort_Type()
)
smSiaSystemDeviceEthernetTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTooShort.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTooLong_Type = Counter32
_SmSiaSystemDeviceEthernetTooLong_Object = MibTableColumn
smSiaSystemDeviceEthernetTooLong = _SmSiaSystemDeviceEthernetTooLong_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 33),
    _SmSiaSystemDeviceEthernetTooLong_Type()
)
smSiaSystemDeviceEthernetTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTooLong.setStatus("mandatory")
_SmSiaSystemDeviceEthernetNoResources_Type = Counter32
_SmSiaSystemDeviceEthernetNoResources_Object = MibTableColumn
smSiaSystemDeviceEthernetNoResources = _SmSiaSystemDeviceEthernetNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 34),
    _SmSiaSystemDeviceEthernetNoResources_Type()
)
smSiaSystemDeviceEthernetNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetNoResources.setStatus("mandatory")
_SmSiaSystemDeviceEthernetPktDiscard_Type = Counter32
_SmSiaSystemDeviceEthernetPktDiscard_Object = MibTableColumn
smSiaSystemDeviceEthernetPktDiscard = _SmSiaSystemDeviceEthernetPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 35),
    _SmSiaSystemDeviceEthernetPktDiscard_Type()
)
smSiaSystemDeviceEthernetPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetPktDiscard.setStatus("mandatory")
_SmSiaSystemDeviceEthernetMaxCollision_Type = Counter32
_SmSiaSystemDeviceEthernetMaxCollision_Object = MibTableColumn
smSiaSystemDeviceEthernetMaxCollision = _SmSiaSystemDeviceEthernetMaxCollision_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 36),
    _SmSiaSystemDeviceEthernetMaxCollision_Type()
)
smSiaSystemDeviceEthernetMaxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetMaxCollision.setStatus("mandatory")
_SmSiaSystemDeviceEthernetLateCollision_Type = Counter32
_SmSiaSystemDeviceEthernetLateCollision_Object = MibTableColumn
smSiaSystemDeviceEthernetLateCollision = _SmSiaSystemDeviceEthernetLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 37),
    _SmSiaSystemDeviceEthernetLateCollision_Type()
)
smSiaSystemDeviceEthernetLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetLateCollision.setStatus("mandatory")
_SmSiaSystemDeviceEthernetCarrierLost_Type = Counter32
_SmSiaSystemDeviceEthernetCarrierLost_Object = MibTableColumn
smSiaSystemDeviceEthernetCarrierLost = _SmSiaSystemDeviceEthernetCarrierLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 38),
    _SmSiaSystemDeviceEthernetCarrierLost_Type()
)
smSiaSystemDeviceEthernetCarrierLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetCarrierLost.setStatus("mandatory")
_SmSiaSystemDeviceEthernetUnderrun_Type = Counter32
_SmSiaSystemDeviceEthernetUnderrun_Object = MibTableColumn
smSiaSystemDeviceEthernetUnderrun = _SmSiaSystemDeviceEthernetUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 39),
    _SmSiaSystemDeviceEthernetUnderrun_Type()
)
smSiaSystemDeviceEthernetUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetUnderrun.setStatus("mandatory")
_SmSiaSystemDeviceEthernetCTSLost_Type = Counter32
_SmSiaSystemDeviceEthernetCTSLost_Object = MibTableColumn
smSiaSystemDeviceEthernetCTSLost = _SmSiaSystemDeviceEthernetCTSLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 40),
    _SmSiaSystemDeviceEthernetCTSLost_Type()
)
smSiaSystemDeviceEthernetCTSLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetCTSLost.setStatus("mandatory")
_SmSiaSystemDeviceEthernetTxTimeouts_Type = Counter32
_SmSiaSystemDeviceEthernetTxTimeouts_Object = MibTableColumn
smSiaSystemDeviceEthernetTxTimeouts = _SmSiaSystemDeviceEthernetTxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 41),
    _SmSiaSystemDeviceEthernetTxTimeouts_Type()
)
smSiaSystemDeviceEthernetTxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetTxTimeouts.setStatus("mandatory")
_SmSiaSystemDeviceEthernetParErrCnt_Type = Counter32
_SmSiaSystemDeviceEthernetParErrCnt_Object = MibTableColumn
smSiaSystemDeviceEthernetParErrCnt = _SmSiaSystemDeviceEthernetParErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 42),
    _SmSiaSystemDeviceEthernetParErrCnt_Type()
)
smSiaSystemDeviceEthernetParErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetParErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetDiagOverflow_Type = Counter32
_SmSiaSystemDeviceEthernetDiagOverflow_Object = MibTableColumn
smSiaSystemDeviceEthernetDiagOverflow = _SmSiaSystemDeviceEthernetDiagOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 43),
    _SmSiaSystemDeviceEthernetDiagOverflow_Type()
)
smSiaSystemDeviceEthernetDiagOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetDiagOverflow.setStatus("mandatory")
_SmSiaSystemDeviceEthernetExecOverflow_Type = Counter32
_SmSiaSystemDeviceEthernetExecOverflow_Object = MibTableColumn
smSiaSystemDeviceEthernetExecOverflow = _SmSiaSystemDeviceEthernetExecOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 44),
    _SmSiaSystemDeviceEthernetExecOverflow_Type()
)
smSiaSystemDeviceEthernetExecOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetExecOverflow.setStatus("mandatory")
_SmSiaSystemDeviceEthernetExecCmdErrors_Type = Counter32
_SmSiaSystemDeviceEthernetExecCmdErrors_Object = MibTableColumn
smSiaSystemDeviceEthernetExecCmdErrors = _SmSiaSystemDeviceEthernetExecCmdErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 45),
    _SmSiaSystemDeviceEthernetExecCmdErrors_Type()
)
smSiaSystemDeviceEthernetExecCmdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetExecCmdErrors.setStatus("mandatory")
_SmSiaSystemDeviceEthernetHostRecEol_Type = Counter32
_SmSiaSystemDeviceEthernetHostRecEol_Object = MibTableColumn
smSiaSystemDeviceEthernetHostRecEol = _SmSiaSystemDeviceEthernetHostRecEol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 46),
    _SmSiaSystemDeviceEthernetHostRecEol_Type()
)
smSiaSystemDeviceEthernetHostRecEol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetHostRecEol.setStatus("mandatory")
_SmSiaSystemDeviceEthernetAdptRecEol_Type = Counter32
_SmSiaSystemDeviceEthernetAdptRecEol_Object = MibTableColumn
smSiaSystemDeviceEthernetAdptRecEol = _SmSiaSystemDeviceEthernetAdptRecEol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 47),
    _SmSiaSystemDeviceEthernetAdptRecEol_Type()
)
smSiaSystemDeviceEthernetAdptRecEol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetAdptRecEol.setStatus("mandatory")
_SmSiaSystemDeviceEthernetHostRecPkt_Type = Counter32
_SmSiaSystemDeviceEthernetHostRecPkt_Object = MibTableColumn
smSiaSystemDeviceEthernetHostRecPkt = _SmSiaSystemDeviceEthernetHostRecPkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 48),
    _SmSiaSystemDeviceEthernetHostRecPkt_Type()
)
smSiaSystemDeviceEthernetHostRecPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetHostRecPkt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetAdptRecPkt_Type = Counter32
_SmSiaSystemDeviceEthernetAdptRecPkt_Object = MibTableColumn
smSiaSystemDeviceEthernetAdptRecPkt = _SmSiaSystemDeviceEthernetAdptRecPkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 49),
    _SmSiaSystemDeviceEthernetAdptRecPkt_Type()
)
smSiaSystemDeviceEthernetAdptRecPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetAdptRecPkt.setStatus("mandatory")
_SmSiaSystemDeviceEthernetStartRxCmd_Type = Counter32
_SmSiaSystemDeviceEthernetStartRxCmd_Object = MibTableColumn
smSiaSystemDeviceEthernetStartRxCmd = _SmSiaSystemDeviceEthernetStartRxCmd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 50),
    _SmSiaSystemDeviceEthernetStartRxCmd_Type()
)
smSiaSystemDeviceEthernetStartRxCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetStartRxCmd.setStatus("mandatory")
_SmSiaSystemDeviceEthernetStartRxDmaTimeouts_Type = Counter32
_SmSiaSystemDeviceEthernetStartRxDmaTimeouts_Object = MibTableColumn
smSiaSystemDeviceEthernetStartRxDmaTimeouts = _SmSiaSystemDeviceEthernetStartRxDmaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 51),
    _SmSiaSystemDeviceEthernetStartRxDmaTimeouts_Type()
)
smSiaSystemDeviceEthernetStartRxDmaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetStartRxDmaTimeouts.setStatus("mandatory")
_SmSiaSystemDeviceEthernetVPD_Type = DisplayString
_SmSiaSystemDeviceEthernetVPD_Object = MibTableColumn
smSiaSystemDeviceEthernetVPD = _SmSiaSystemDeviceEthernetVPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 52),
    _SmSiaSystemDeviceEthernetVPD_Type()
)
smSiaSystemDeviceEthernetVPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetVPD.setStatus("mandatory")


class _SmSiaSystemDeviceEthernetClear_Type(Integer32):
    """Custom type smSiaSystemDeviceEthernetClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("normal", 1))
    )


_SmSiaSystemDeviceEthernetClear_Type.__name__ = "Integer32"
_SmSiaSystemDeviceEthernetClear_Object = MibTableColumn
smSiaSystemDeviceEthernetClear = _SmSiaSystemDeviceEthernetClear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 53),
    _SmSiaSystemDeviceEthernetClear_Type()
)
smSiaSystemDeviceEthernetClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaSystemDeviceEthernetClear.setStatus("mandatory")
_SmSiaSystemDeviceX25_ObjectIdentity = ObjectIdentity
smSiaSystemDeviceX25 = _SmSiaSystemDeviceX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4)
)
_SmSiaSystemDeviceX25Installed_Type = Integer32
_SmSiaSystemDeviceX25Installed_Object = MibScalar
smSiaSystemDeviceX25Installed = _SmSiaSystemDeviceX25Installed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 1),
    _SmSiaSystemDeviceX25Installed_Type()
)
smSiaSystemDeviceX25Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Installed.setStatus("mandatory")
_SmSiaSystemDeviceX25Table_Object = MibTable
smSiaSystemDeviceX25Table = _SmSiaSystemDeviceX25Table_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Table.setStatus("mandatory")
_SmSiaSystemDeviceX25Entry_Object = MibTableRow
smSiaSystemDeviceX25Entry = _SmSiaSystemDeviceX25Entry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1)
)
smSiaSystemDeviceX25Entry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemDeviceX25Number"),
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Entry.setStatus("mandatory")
_SmSiaSystemDeviceX25Number_Type = Integer32
_SmSiaSystemDeviceX25Number_Object = MibTableColumn
smSiaSystemDeviceX25Number = _SmSiaSystemDeviceX25Number_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 1),
    _SmSiaSystemDeviceX25Number_Type()
)
smSiaSystemDeviceX25Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Number.setStatus("mandatory")
_SmSiaSystemDeviceX25Address_Type = DisplayString
_SmSiaSystemDeviceX25Address_Object = MibTableColumn
smSiaSystemDeviceX25Address = _SmSiaSystemDeviceX25Address_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 2),
    _SmSiaSystemDeviceX25Address_Type()
)
smSiaSystemDeviceX25Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Address.setStatus("mandatory")
_SmSiaSystemDeviceX25SupportLevel_Type = Integer32
_SmSiaSystemDeviceX25SupportLevel_Object = MibTableColumn
smSiaSystemDeviceX25SupportLevel = _SmSiaSystemDeviceX25SupportLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 3),
    _SmSiaSystemDeviceX25SupportLevel_Type()
)
smSiaSystemDeviceX25SupportLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25SupportLevel.setStatus("mandatory")
_SmSiaSystemDeviceX25SupportedFacilities_Type = Integer32
_SmSiaSystemDeviceX25SupportedFacilities_Object = MibTableColumn
smSiaSystemDeviceX25SupportedFacilities = _SmSiaSystemDeviceX25SupportedFacilities_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 4),
    _SmSiaSystemDeviceX25SupportedFacilities_Type()
)
smSiaSystemDeviceX25SupportedFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25SupportedFacilities.setStatus("mandatory")
_SmSiaSystemDeviceX25NetworkId_Type = PhysAddress
_SmSiaSystemDeviceX25NetworkId_Object = MibTableColumn
smSiaSystemDeviceX25NetworkId = _SmSiaSystemDeviceX25NetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 5),
    _SmSiaSystemDeviceX25NetworkId_Type()
)
smSiaSystemDeviceX25NetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25NetworkId.setStatus("mandatory")
_SmSiaSystemDeviceX25MaxTxPacketSize_Type = Integer32
_SmSiaSystemDeviceX25MaxTxPacketSize_Object = MibTableColumn
smSiaSystemDeviceX25MaxTxPacketSize = _SmSiaSystemDeviceX25MaxTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 6),
    _SmSiaSystemDeviceX25MaxTxPacketSize_Type()
)
smSiaSystemDeviceX25MaxTxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25MaxTxPacketSize.setStatus("mandatory")
_SmSiaSystemDeviceX25MaxRxPacketSize_Type = Integer32
_SmSiaSystemDeviceX25MaxRxPacketSize_Object = MibTableColumn
smSiaSystemDeviceX25MaxRxPacketSize = _SmSiaSystemDeviceX25MaxRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 7),
    _SmSiaSystemDeviceX25MaxRxPacketSize_Type()
)
smSiaSystemDeviceX25MaxRxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25MaxRxPacketSize.setStatus("mandatory")
_SmSiaSystemDeviceX25DefaultSvcTxPacketSize_Type = Integer32
_SmSiaSystemDeviceX25DefaultSvcTxPacketSize_Object = MibTableColumn
smSiaSystemDeviceX25DefaultSvcTxPacketSize = _SmSiaSystemDeviceX25DefaultSvcTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 8),
    _SmSiaSystemDeviceX25DefaultSvcTxPacketSize_Type()
)
smSiaSystemDeviceX25DefaultSvcTxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DefaultSvcTxPacketSize.setStatus("mandatory")
_SmSiaSystemDeviceX25DefaultSvcRxPacketSize_Type = Integer32
_SmSiaSystemDeviceX25DefaultSvcRxPacketSize_Object = MibTableColumn
smSiaSystemDeviceX25DefaultSvcRxPacketSize = _SmSiaSystemDeviceX25DefaultSvcRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 9),
    _SmSiaSystemDeviceX25DefaultSvcRxPacketSize_Type()
)
smSiaSystemDeviceX25DefaultSvcRxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DefaultSvcRxPacketSize.setStatus("mandatory")
_SmSiaSystemDeviceX25ReceiveDataTransferOffset_Type = Integer32
_SmSiaSystemDeviceX25ReceiveDataTransferOffset_Object = MibTableColumn
smSiaSystemDeviceX25ReceiveDataTransferOffset = _SmSiaSystemDeviceX25ReceiveDataTransferOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 10),
    _SmSiaSystemDeviceX25ReceiveDataTransferOffset_Type()
)
smSiaSystemDeviceX25ReceiveDataTransferOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ReceiveDataTransferOffset.setStatus("mandatory")
_SmSiaSystemDeviceX25MemoryWindowSize_Type = Integer32
_SmSiaSystemDeviceX25MemoryWindowSize_Object = MibTableColumn
smSiaSystemDeviceX25MemoryWindowSize = _SmSiaSystemDeviceX25MemoryWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 11),
    _SmSiaSystemDeviceX25MemoryWindowSize_Type()
)
smSiaSystemDeviceX25MemoryWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25MemoryWindowSize.setStatus("mandatory")
_SmSiaSystemDeviceX25TxByteMcnt_Type = Counter32
_SmSiaSystemDeviceX25TxByteMcnt_Object = MibTableColumn
smSiaSystemDeviceX25TxByteMcnt = _SmSiaSystemDeviceX25TxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 12),
    _SmSiaSystemDeviceX25TxByteMcnt_Type()
)
smSiaSystemDeviceX25TxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxByteMcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25TxByteLcnt_Type = Counter32
_SmSiaSystemDeviceX25TxByteLcnt_Object = MibTableColumn
smSiaSystemDeviceX25TxByteLcnt = _SmSiaSystemDeviceX25TxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 13),
    _SmSiaSystemDeviceX25TxByteLcnt_Type()
)
smSiaSystemDeviceX25TxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxByteLcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25RxByteMcnt_Type = Counter32
_SmSiaSystemDeviceX25RxByteMcnt_Object = MibTableColumn
smSiaSystemDeviceX25RxByteMcnt = _SmSiaSystemDeviceX25RxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 14),
    _SmSiaSystemDeviceX25RxByteMcnt_Type()
)
smSiaSystemDeviceX25RxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxByteMcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25RxByteLcnt_Type = Counter32
_SmSiaSystemDeviceX25RxByteLcnt_Object = MibTableColumn
smSiaSystemDeviceX25RxByteLcnt = _SmSiaSystemDeviceX25RxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 15),
    _SmSiaSystemDeviceX25RxByteLcnt_Type()
)
smSiaSystemDeviceX25RxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxByteLcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25TxFrameMcnt_Type = Counter32
_SmSiaSystemDeviceX25TxFrameMcnt_Object = MibTableColumn
smSiaSystemDeviceX25TxFrameMcnt = _SmSiaSystemDeviceX25TxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 16),
    _SmSiaSystemDeviceX25TxFrameMcnt_Type()
)
smSiaSystemDeviceX25TxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxFrameMcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25TxFrameLcnt_Type = Counter32
_SmSiaSystemDeviceX25TxFrameLcnt_Object = MibTableColumn
smSiaSystemDeviceX25TxFrameLcnt = _SmSiaSystemDeviceX25TxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 17),
    _SmSiaSystemDeviceX25TxFrameLcnt_Type()
)
smSiaSystemDeviceX25TxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxFrameLcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25RxFrameMcnt_Type = Counter32
_SmSiaSystemDeviceX25RxFrameMcnt_Object = MibTableColumn
smSiaSystemDeviceX25RxFrameMcnt = _SmSiaSystemDeviceX25RxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 18),
    _SmSiaSystemDeviceX25RxFrameMcnt_Type()
)
smSiaSystemDeviceX25RxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxFrameMcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25RxFrameLcnt_Type = Counter32
_SmSiaSystemDeviceX25RxFrameLcnt_Object = MibTableColumn
smSiaSystemDeviceX25RxFrameLcnt = _SmSiaSystemDeviceX25RxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 19),
    _SmSiaSystemDeviceX25RxFrameLcnt_Type()
)
smSiaSystemDeviceX25RxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxFrameLcnt.setStatus("mandatory")
_SmSiaSystemDeviceX25TxErrCnt_Type = Counter32
_SmSiaSystemDeviceX25TxErrCnt_Object = MibTableColumn
smSiaSystemDeviceX25TxErrCnt = _SmSiaSystemDeviceX25TxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 20),
    _SmSiaSystemDeviceX25TxErrCnt_Type()
)
smSiaSystemDeviceX25TxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceX25RxErrCnt_Type = Counter32
_SmSiaSystemDeviceX25RxErrCnt_Object = MibTableColumn
smSiaSystemDeviceX25RxErrCnt = _SmSiaSystemDeviceX25RxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 21),
    _SmSiaSystemDeviceX25RxErrCnt_Type()
)
smSiaSystemDeviceX25RxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxErrCnt.setStatus("mandatory")
_SmSiaSystemDeviceX25NidTblHigh_Type = Integer32
_SmSiaSystemDeviceX25NidTblHigh_Object = MibTableColumn
smSiaSystemDeviceX25NidTblHigh = _SmSiaSystemDeviceX25NidTblHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 22),
    _SmSiaSystemDeviceX25NidTblHigh_Type()
)
smSiaSystemDeviceX25NidTblHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25NidTblHigh.setStatus("mandatory")
_SmSiaSystemDeviceX25TxQueHigh_Type = Gauge32
_SmSiaSystemDeviceX25TxQueHigh_Object = MibTableColumn
smSiaSystemDeviceX25TxQueHigh = _SmSiaSystemDeviceX25TxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 23),
    _SmSiaSystemDeviceX25TxQueHigh_Type()
)
smSiaSystemDeviceX25TxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceX25RxQueHigh_Type = Gauge32
_SmSiaSystemDeviceX25RxQueHigh_Object = MibTableColumn
smSiaSystemDeviceX25RxQueHigh = _SmSiaSystemDeviceX25RxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 24),
    _SmSiaSystemDeviceX25RxQueHigh_Type()
)
smSiaSystemDeviceX25RxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceX25StaQueHigh_Type = Gauge32
_SmSiaSystemDeviceX25StaQueHigh_Object = MibTableColumn
smSiaSystemDeviceX25StaQueHigh = _SmSiaSystemDeviceX25StaQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 25),
    _SmSiaSystemDeviceX25StaQueHigh_Type()
)
smSiaSystemDeviceX25StaQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25StaQueHigh.setStatus("mandatory")
_SmSiaSystemDeviceX25IgnoredFTx_Type = Counter32
_SmSiaSystemDeviceX25IgnoredFTx_Object = MibTableColumn
smSiaSystemDeviceX25IgnoredFTx = _SmSiaSystemDeviceX25IgnoredFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 26),
    _SmSiaSystemDeviceX25IgnoredFTx_Type()
)
smSiaSystemDeviceX25IgnoredFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25IgnoredFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RrFTx_Type = Counter32
_SmSiaSystemDeviceX25RrFTx_Object = MibTableColumn
smSiaSystemDeviceX25RrFTx = _SmSiaSystemDeviceX25RrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 27),
    _SmSiaSystemDeviceX25RrFTx_Type()
)
smSiaSystemDeviceX25RrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RrFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RnrFTx_Type = Counter32
_SmSiaSystemDeviceX25RnrFTx_Object = MibTableColumn
smSiaSystemDeviceX25RnrFTx = _SmSiaSystemDeviceX25RnrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 28),
    _SmSiaSystemDeviceX25RnrFTx_Type()
)
smSiaSystemDeviceX25RnrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RnrFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RejFTx_Type = Counter32
_SmSiaSystemDeviceX25RejFTx_Object = MibTableColumn
smSiaSystemDeviceX25RejFTx = _SmSiaSystemDeviceX25RejFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 29),
    _SmSiaSystemDeviceX25RejFTx_Type()
)
smSiaSystemDeviceX25RejFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RejFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25InfoFTx_Type = Counter32
_SmSiaSystemDeviceX25InfoFTx_Object = MibTableColumn
smSiaSystemDeviceX25InfoFTx = _SmSiaSystemDeviceX25InfoFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 30),
    _SmSiaSystemDeviceX25InfoFTx_Type()
)
smSiaSystemDeviceX25InfoFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25InfoFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25SabmFTx_Type = Counter32
_SmSiaSystemDeviceX25SabmFTx_Object = MibTableColumn
smSiaSystemDeviceX25SabmFTx = _SmSiaSystemDeviceX25SabmFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 31),
    _SmSiaSystemDeviceX25SabmFTx_Type()
)
smSiaSystemDeviceX25SabmFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25SabmFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25SarmDmFTx_Type = Counter32
_SmSiaSystemDeviceX25SarmDmFTx_Object = MibTableColumn
smSiaSystemDeviceX25SarmDmFTx = _SmSiaSystemDeviceX25SarmDmFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 32),
    _SmSiaSystemDeviceX25SarmDmFTx_Type()
)
smSiaSystemDeviceX25SarmDmFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25SarmDmFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25DiscFTx_Type = Counter32
_SmSiaSystemDeviceX25DiscFTx_Object = MibTableColumn
smSiaSystemDeviceX25DiscFTx = _SmSiaSystemDeviceX25DiscFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 33),
    _SmSiaSystemDeviceX25DiscFTx_Type()
)
smSiaSystemDeviceX25DiscFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DiscFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25UaFTx_Type = Counter32
_SmSiaSystemDeviceX25UaFTx_Object = MibTableColumn
smSiaSystemDeviceX25UaFTx = _SmSiaSystemDeviceX25UaFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 34),
    _SmSiaSystemDeviceX25UaFTx_Type()
)
smSiaSystemDeviceX25UaFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25UaFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25FrmrFTx_Type = Counter32
_SmSiaSystemDeviceX25FrmrFTx_Object = MibTableColumn
smSiaSystemDeviceX25FrmrFTx = _SmSiaSystemDeviceX25FrmrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 35),
    _SmSiaSystemDeviceX25FrmrFTx_Type()
)
smSiaSystemDeviceX25FrmrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25FrmrFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25BadNrFTx_Type = Counter32
_SmSiaSystemDeviceX25BadNrFTx_Object = MibTableColumn
smSiaSystemDeviceX25BadNrFTx = _SmSiaSystemDeviceX25BadNrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 36),
    _SmSiaSystemDeviceX25BadNrFTx_Type()
)
smSiaSystemDeviceX25BadNrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25BadNrFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25UnknownFTx_Type = Counter32
_SmSiaSystemDeviceX25UnknownFTx_Object = MibTableColumn
smSiaSystemDeviceX25UnknownFTx = _SmSiaSystemDeviceX25UnknownFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 37),
    _SmSiaSystemDeviceX25UnknownFTx_Type()
)
smSiaSystemDeviceX25UnknownFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25UnknownFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25XidFTx_Type = Counter32
_SmSiaSystemDeviceX25XidFTx_Object = MibTableColumn
smSiaSystemDeviceX25XidFTx = _SmSiaSystemDeviceX25XidFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 38),
    _SmSiaSystemDeviceX25XidFTx_Type()
)
smSiaSystemDeviceX25XidFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25XidFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25BadLengthFTx_Type = Counter32
_SmSiaSystemDeviceX25BadLengthFTx_Object = MibTableColumn
smSiaSystemDeviceX25BadLengthFTx = _SmSiaSystemDeviceX25BadLengthFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 39),
    _SmSiaSystemDeviceX25BadLengthFTx_Type()
)
smSiaSystemDeviceX25BadLengthFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25BadLengthFTx.setStatus("mandatory")
_SmSiaSystemDeviceX25T1Expirations_Type = Counter32
_SmSiaSystemDeviceX25T1Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T1Expirations = _SmSiaSystemDeviceX25T1Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 40),
    _SmSiaSystemDeviceX25T1Expirations_Type()
)
smSiaSystemDeviceX25T1Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T1Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25Lvl2Connects_Type = Counter32
_SmSiaSystemDeviceX25Lvl2Connects_Object = MibTableColumn
smSiaSystemDeviceX25Lvl2Connects = _SmSiaSystemDeviceX25Lvl2Connects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 41),
    _SmSiaSystemDeviceX25Lvl2Connects_Type()
)
smSiaSystemDeviceX25Lvl2Connects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Lvl2Connects.setStatus("mandatory")
_SmSiaSystemDeviceX25Lvl2Disconnects_Type = Counter32
_SmSiaSystemDeviceX25Lvl2Disconnects_Object = MibTableColumn
smSiaSystemDeviceX25Lvl2Disconnects = _SmSiaSystemDeviceX25Lvl2Disconnects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 42),
    _SmSiaSystemDeviceX25Lvl2Disconnects_Type()
)
smSiaSystemDeviceX25Lvl2Disconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Lvl2Disconnects.setStatus("mandatory")
_SmSiaSystemDeviceX25CarrierLoss_Type = Counter32
_SmSiaSystemDeviceX25CarrierLoss_Object = MibTableColumn
smSiaSystemDeviceX25CarrierLoss = _SmSiaSystemDeviceX25CarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 43),
    _SmSiaSystemDeviceX25CarrierLoss_Type()
)
smSiaSystemDeviceX25CarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25CarrierLoss.setStatus("mandatory")
_SmSiaSystemDeviceX25ConnectTime_Type = TimeTicks
_SmSiaSystemDeviceX25ConnectTime_Object = MibTableColumn
smSiaSystemDeviceX25ConnectTime = _SmSiaSystemDeviceX25ConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 44),
    _SmSiaSystemDeviceX25ConnectTime_Type()
)
smSiaSystemDeviceX25ConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ConnectTime.setStatus("mandatory")
_SmSiaSystemDeviceX25T4Expirations_Type = Counter32
_SmSiaSystemDeviceX25T4Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T4Expirations = _SmSiaSystemDeviceX25T4Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 45),
    _SmSiaSystemDeviceX25T4Expirations_Type()
)
smSiaSystemDeviceX25T4Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T4Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T4N2Times_Type = Counter32
_SmSiaSystemDeviceX25T4N2Times_Object = MibTableColumn
smSiaSystemDeviceX25T4N2Times = _SmSiaSystemDeviceX25T4N2Times_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 46),
    _SmSiaSystemDeviceX25T4N2Times_Type()
)
smSiaSystemDeviceX25T4N2Times.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T4N2Times.setStatus("mandatory")
_SmSiaSystemDeviceX25IgnoredFRx_Type = Counter32
_SmSiaSystemDeviceX25IgnoredFRx_Object = MibTableColumn
smSiaSystemDeviceX25IgnoredFRx = _SmSiaSystemDeviceX25IgnoredFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 47),
    _SmSiaSystemDeviceX25IgnoredFRx_Type()
)
smSiaSystemDeviceX25IgnoredFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25IgnoredFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RrFRx_Type = Counter32
_SmSiaSystemDeviceX25RrFRx_Object = MibTableColumn
smSiaSystemDeviceX25RrFRx = _SmSiaSystemDeviceX25RrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 48),
    _SmSiaSystemDeviceX25RrFRx_Type()
)
smSiaSystemDeviceX25RrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RrFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RnrFRx_Type = Counter32
_SmSiaSystemDeviceX25RnrFRx_Object = MibTableColumn
smSiaSystemDeviceX25RnrFRx = _SmSiaSystemDeviceX25RnrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 49),
    _SmSiaSystemDeviceX25RnrFRx_Type()
)
smSiaSystemDeviceX25RnrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RnrFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RejFRx_Type = Counter32
_SmSiaSystemDeviceX25RejFRx_Object = MibTableColumn
smSiaSystemDeviceX25RejFRx = _SmSiaSystemDeviceX25RejFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 50),
    _SmSiaSystemDeviceX25RejFRx_Type()
)
smSiaSystemDeviceX25RejFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RejFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25InfoFRx_Type = Counter32
_SmSiaSystemDeviceX25InfoFRx_Object = MibTableColumn
smSiaSystemDeviceX25InfoFRx = _SmSiaSystemDeviceX25InfoFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 51),
    _SmSiaSystemDeviceX25InfoFRx_Type()
)
smSiaSystemDeviceX25InfoFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25InfoFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25SabmFRx_Type = Counter32
_SmSiaSystemDeviceX25SabmFRx_Object = MibTableColumn
smSiaSystemDeviceX25SabmFRx = _SmSiaSystemDeviceX25SabmFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 52),
    _SmSiaSystemDeviceX25SabmFRx_Type()
)
smSiaSystemDeviceX25SabmFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25SabmFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25SarmDmFRx_Type = Counter32
_SmSiaSystemDeviceX25SarmDmFRx_Object = MibTableColumn
smSiaSystemDeviceX25SarmDmFRx = _SmSiaSystemDeviceX25SarmDmFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 53),
    _SmSiaSystemDeviceX25SarmDmFRx_Type()
)
smSiaSystemDeviceX25SarmDmFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25SarmDmFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25DiscFRx_Type = Counter32
_SmSiaSystemDeviceX25DiscFRx_Object = MibTableColumn
smSiaSystemDeviceX25DiscFRx = _SmSiaSystemDeviceX25DiscFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 54),
    _SmSiaSystemDeviceX25DiscFRx_Type()
)
smSiaSystemDeviceX25DiscFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DiscFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25UaFRx_Type = Counter32
_SmSiaSystemDeviceX25UaFRx_Object = MibTableColumn
smSiaSystemDeviceX25UaFRx = _SmSiaSystemDeviceX25UaFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 55),
    _SmSiaSystemDeviceX25UaFRx_Type()
)
smSiaSystemDeviceX25UaFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25UaFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25FrmrFRx_Type = Counter32
_SmSiaSystemDeviceX25FrmrFRx_Object = MibTableColumn
smSiaSystemDeviceX25FrmrFRx = _SmSiaSystemDeviceX25FrmrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 56),
    _SmSiaSystemDeviceX25FrmrFRx_Type()
)
smSiaSystemDeviceX25FrmrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25FrmrFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25BadNrFRx_Type = Counter32
_SmSiaSystemDeviceX25BadNrFRx_Object = MibTableColumn
smSiaSystemDeviceX25BadNrFRx = _SmSiaSystemDeviceX25BadNrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 57),
    _SmSiaSystemDeviceX25BadNrFRx_Type()
)
smSiaSystemDeviceX25BadNrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25BadNrFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25UnknownFRx_Type = Counter32
_SmSiaSystemDeviceX25UnknownFRx_Object = MibTableColumn
smSiaSystemDeviceX25UnknownFRx = _SmSiaSystemDeviceX25UnknownFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 58),
    _SmSiaSystemDeviceX25UnknownFRx_Type()
)
smSiaSystemDeviceX25UnknownFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25UnknownFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25XidFRx_Type = Counter32
_SmSiaSystemDeviceX25XidFRx_Object = MibTableColumn
smSiaSystemDeviceX25XidFRx = _SmSiaSystemDeviceX25XidFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 59),
    _SmSiaSystemDeviceX25XidFRx_Type()
)
smSiaSystemDeviceX25XidFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25XidFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25BadLengthFRx_Type = Counter32
_SmSiaSystemDeviceX25BadLengthFRx_Object = MibTableColumn
smSiaSystemDeviceX25BadLengthFRx = _SmSiaSystemDeviceX25BadLengthFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 60),
    _SmSiaSystemDeviceX25BadLengthFRx_Type()
)
smSiaSystemDeviceX25BadLengthFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25BadLengthFRx.setStatus("mandatory")
_SmSiaSystemDeviceX25DataPTx_Type = Counter32
_SmSiaSystemDeviceX25DataPTx_Object = MibTableColumn
smSiaSystemDeviceX25DataPTx = _SmSiaSystemDeviceX25DataPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 61),
    _SmSiaSystemDeviceX25DataPTx_Type()
)
smSiaSystemDeviceX25DataPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DataPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RrPTx_Type = Counter32
_SmSiaSystemDeviceX25RrPTx_Object = MibTableColumn
smSiaSystemDeviceX25RrPTx = _SmSiaSystemDeviceX25RrPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 62),
    _SmSiaSystemDeviceX25RrPTx_Type()
)
smSiaSystemDeviceX25RrPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RrPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RnrPTx_Type = Counter32
_SmSiaSystemDeviceX25RnrPTx_Object = MibTableColumn
smSiaSystemDeviceX25RnrPTx = _SmSiaSystemDeviceX25RnrPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 63),
    _SmSiaSystemDeviceX25RnrPTx_Type()
)
smSiaSystemDeviceX25RnrPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RnrPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25InterruptPTx_Type = Counter32
_SmSiaSystemDeviceX25InterruptPTx_Object = MibTableColumn
smSiaSystemDeviceX25InterruptPTx = _SmSiaSystemDeviceX25InterruptPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 64),
    _SmSiaSystemDeviceX25InterruptPTx_Type()
)
smSiaSystemDeviceX25InterruptPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25InterruptPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25InterruptConfirmPTx_Type = Counter32
_SmSiaSystemDeviceX25InterruptConfirmPTx_Object = MibTableColumn
smSiaSystemDeviceX25InterruptConfirmPTx = _SmSiaSystemDeviceX25InterruptConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 65),
    _SmSiaSystemDeviceX25InterruptConfirmPTx_Type()
)
smSiaSystemDeviceX25InterruptConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25InterruptConfirmPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25CallRequestPTx_Type = Counter32
_SmSiaSystemDeviceX25CallRequestPTx_Object = MibTableColumn
smSiaSystemDeviceX25CallRequestPTx = _SmSiaSystemDeviceX25CallRequestPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 66),
    _SmSiaSystemDeviceX25CallRequestPTx_Type()
)
smSiaSystemDeviceX25CallRequestPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25CallRequestPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25CallAcceptPTx_Type = Counter32
_SmSiaSystemDeviceX25CallAcceptPTx_Object = MibTableColumn
smSiaSystemDeviceX25CallAcceptPTx = _SmSiaSystemDeviceX25CallAcceptPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 67),
    _SmSiaSystemDeviceX25CallAcceptPTx_Type()
)
smSiaSystemDeviceX25CallAcceptPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25CallAcceptPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25ClearRequestPTx_Type = Counter32
_SmSiaSystemDeviceX25ClearRequestPTx_Object = MibTableColumn
smSiaSystemDeviceX25ClearRequestPTx = _SmSiaSystemDeviceX25ClearRequestPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 68),
    _SmSiaSystemDeviceX25ClearRequestPTx_Type()
)
smSiaSystemDeviceX25ClearRequestPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ClearRequestPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25ClearConfirmPTx_Type = Counter32
_SmSiaSystemDeviceX25ClearConfirmPTx_Object = MibTableColumn
smSiaSystemDeviceX25ClearConfirmPTx = _SmSiaSystemDeviceX25ClearConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 69),
    _SmSiaSystemDeviceX25ClearConfirmPTx_Type()
)
smSiaSystemDeviceX25ClearConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ClearConfirmPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25ResetRequestPTx_Type = Counter32
_SmSiaSystemDeviceX25ResetRequestPTx_Object = MibTableColumn
smSiaSystemDeviceX25ResetRequestPTx = _SmSiaSystemDeviceX25ResetRequestPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 70),
    _SmSiaSystemDeviceX25ResetRequestPTx_Type()
)
smSiaSystemDeviceX25ResetRequestPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ResetRequestPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25ResetConfirmPTx_Type = Counter32
_SmSiaSystemDeviceX25ResetConfirmPTx_Object = MibTableColumn
smSiaSystemDeviceX25ResetConfirmPTx = _SmSiaSystemDeviceX25ResetConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 71),
    _SmSiaSystemDeviceX25ResetConfirmPTx_Type()
)
smSiaSystemDeviceX25ResetConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ResetConfirmPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25DiagnosticPTx_Type = Counter32
_SmSiaSystemDeviceX25DiagnosticPTx_Object = MibTableColumn
smSiaSystemDeviceX25DiagnosticPTx = _SmSiaSystemDeviceX25DiagnosticPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 72),
    _SmSiaSystemDeviceX25DiagnosticPTx_Type()
)
smSiaSystemDeviceX25DiagnosticPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DiagnosticPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RegistrationPTx_Type = Counter32
_SmSiaSystemDeviceX25RegistrationPTx_Object = MibTableColumn
smSiaSystemDeviceX25RegistrationPTx = _SmSiaSystemDeviceX25RegistrationPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 73),
    _SmSiaSystemDeviceX25RegistrationPTx_Type()
)
smSiaSystemDeviceX25RegistrationPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RegistrationPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RegistrationConfirmPTx_Type = Counter32
_SmSiaSystemDeviceX25RegistrationConfirmPTx_Object = MibTableColumn
smSiaSystemDeviceX25RegistrationConfirmPTx = _SmSiaSystemDeviceX25RegistrationConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 74),
    _SmSiaSystemDeviceX25RegistrationConfirmPTx_Type()
)
smSiaSystemDeviceX25RegistrationConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RegistrationConfirmPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RestartPTx_Type = Counter32
_SmSiaSystemDeviceX25RestartPTx_Object = MibTableColumn
smSiaSystemDeviceX25RestartPTx = _SmSiaSystemDeviceX25RestartPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 75),
    _SmSiaSystemDeviceX25RestartPTx_Type()
)
smSiaSystemDeviceX25RestartPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RestartPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25RestartConfirmPTx_Type = Counter32
_SmSiaSystemDeviceX25RestartConfirmPTx_Object = MibTableColumn
smSiaSystemDeviceX25RestartConfirmPTx = _SmSiaSystemDeviceX25RestartConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 76),
    _SmSiaSystemDeviceX25RestartConfirmPTx_Type()
)
smSiaSystemDeviceX25RestartConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RestartConfirmPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25ErrorPTx_Type = Counter32
_SmSiaSystemDeviceX25ErrorPTx_Object = MibTableColumn
smSiaSystemDeviceX25ErrorPTx = _SmSiaSystemDeviceX25ErrorPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 77),
    _SmSiaSystemDeviceX25ErrorPTx_Type()
)
smSiaSystemDeviceX25ErrorPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ErrorPTx.setStatus("mandatory")
_SmSiaSystemDeviceX25T20Expirations_Type = Counter32
_SmSiaSystemDeviceX25T20Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T20Expirations = _SmSiaSystemDeviceX25T20Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 78),
    _SmSiaSystemDeviceX25T20Expirations_Type()
)
smSiaSystemDeviceX25T20Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T20Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T21Expirations_Type = Counter32
_SmSiaSystemDeviceX25T21Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T21Expirations = _SmSiaSystemDeviceX25T21Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 79),
    _SmSiaSystemDeviceX25T21Expirations_Type()
)
smSiaSystemDeviceX25T21Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T21Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T22Expirations_Type = Counter32
_SmSiaSystemDeviceX25T22Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T22Expirations = _SmSiaSystemDeviceX25T22Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 80),
    _SmSiaSystemDeviceX25T22Expirations_Type()
)
smSiaSystemDeviceX25T22Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T22Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T23Expirations_Type = Counter32
_SmSiaSystemDeviceX25T23Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T23Expirations = _SmSiaSystemDeviceX25T23Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 81),
    _SmSiaSystemDeviceX25T23Expirations_Type()
)
smSiaSystemDeviceX25T23Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T23Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25VcEstablishments_Type = Counter32
_SmSiaSystemDeviceX25VcEstablishments_Object = MibTableColumn
smSiaSystemDeviceX25VcEstablishments = _SmSiaSystemDeviceX25VcEstablishments_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 82),
    _SmSiaSystemDeviceX25VcEstablishments_Type()
)
smSiaSystemDeviceX25VcEstablishments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25VcEstablishments.setStatus("mandatory")
_SmSiaSystemDeviceX25T24Expirations_Type = Counter32
_SmSiaSystemDeviceX25T24Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T24Expirations = _SmSiaSystemDeviceX25T24Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 83),
    _SmSiaSystemDeviceX25T24Expirations_Type()
)
smSiaSystemDeviceX25T24Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T24Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T25Expirations_Type = Counter32
_SmSiaSystemDeviceX25T25Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T25Expirations = _SmSiaSystemDeviceX25T25Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 84),
    _SmSiaSystemDeviceX25T25Expirations_Type()
)
smSiaSystemDeviceX25T25Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T25Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T26Expirations_Type = Counter32
_SmSiaSystemDeviceX25T26Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T26Expirations = _SmSiaSystemDeviceX25T26Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 85),
    _SmSiaSystemDeviceX25T26Expirations_Type()
)
smSiaSystemDeviceX25T26Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T26Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25T28Expirations_Type = Counter32
_SmSiaSystemDeviceX25T28Expirations_Object = MibTableColumn
smSiaSystemDeviceX25T28Expirations = _SmSiaSystemDeviceX25T28Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 86),
    _SmSiaSystemDeviceX25T28Expirations_Type()
)
smSiaSystemDeviceX25T28Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25T28Expirations.setStatus("mandatory")
_SmSiaSystemDeviceX25DataPRx_Type = Counter32
_SmSiaSystemDeviceX25DataPRx_Object = MibTableColumn
smSiaSystemDeviceX25DataPRx = _SmSiaSystemDeviceX25DataPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 87),
    _SmSiaSystemDeviceX25DataPRx_Type()
)
smSiaSystemDeviceX25DataPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DataPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RrPRx_Type = Counter32
_SmSiaSystemDeviceX25RrPRx_Object = MibTableColumn
smSiaSystemDeviceX25RrPRx = _SmSiaSystemDeviceX25RrPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 88),
    _SmSiaSystemDeviceX25RrPRx_Type()
)
smSiaSystemDeviceX25RrPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RrPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RnrPRx_Type = Counter32
_SmSiaSystemDeviceX25RnrPRx_Object = MibTableColumn
smSiaSystemDeviceX25RnrPRx = _SmSiaSystemDeviceX25RnrPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 89),
    _SmSiaSystemDeviceX25RnrPRx_Type()
)
smSiaSystemDeviceX25RnrPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RnrPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25InterruptPRx_Type = Counter32
_SmSiaSystemDeviceX25InterruptPRx_Object = MibTableColumn
smSiaSystemDeviceX25InterruptPRx = _SmSiaSystemDeviceX25InterruptPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 90),
    _SmSiaSystemDeviceX25InterruptPRx_Type()
)
smSiaSystemDeviceX25InterruptPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25InterruptPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25InterruptConfirmPRx_Type = Counter32
_SmSiaSystemDeviceX25InterruptConfirmPRx_Object = MibTableColumn
smSiaSystemDeviceX25InterruptConfirmPRx = _SmSiaSystemDeviceX25InterruptConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 91),
    _SmSiaSystemDeviceX25InterruptConfirmPRx_Type()
)
smSiaSystemDeviceX25InterruptConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25InterruptConfirmPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25IncomingCallPRx_Type = Counter32
_SmSiaSystemDeviceX25IncomingCallPRx_Object = MibTableColumn
smSiaSystemDeviceX25IncomingCallPRx = _SmSiaSystemDeviceX25IncomingCallPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 92),
    _SmSiaSystemDeviceX25IncomingCallPRx_Type()
)
smSiaSystemDeviceX25IncomingCallPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25IncomingCallPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25CallConnectedPRx_Type = Counter32
_SmSiaSystemDeviceX25CallConnectedPRx_Object = MibTableColumn
smSiaSystemDeviceX25CallConnectedPRx = _SmSiaSystemDeviceX25CallConnectedPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 93),
    _SmSiaSystemDeviceX25CallConnectedPRx_Type()
)
smSiaSystemDeviceX25CallConnectedPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25CallConnectedPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25ClearIndicationPRx_Type = Counter32
_SmSiaSystemDeviceX25ClearIndicationPRx_Object = MibTableColumn
smSiaSystemDeviceX25ClearIndicationPRx = _SmSiaSystemDeviceX25ClearIndicationPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 94),
    _SmSiaSystemDeviceX25ClearIndicationPRx_Type()
)
smSiaSystemDeviceX25ClearIndicationPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ClearIndicationPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25ClearConfirmPRx_Type = Counter32
_SmSiaSystemDeviceX25ClearConfirmPRx_Object = MibTableColumn
smSiaSystemDeviceX25ClearConfirmPRx = _SmSiaSystemDeviceX25ClearConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 95),
    _SmSiaSystemDeviceX25ClearConfirmPRx_Type()
)
smSiaSystemDeviceX25ClearConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ClearConfirmPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25ResetIndicationPRx_Type = Counter32
_SmSiaSystemDeviceX25ResetIndicationPRx_Object = MibTableColumn
smSiaSystemDeviceX25ResetIndicationPRx = _SmSiaSystemDeviceX25ResetIndicationPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 96),
    _SmSiaSystemDeviceX25ResetIndicationPRx_Type()
)
smSiaSystemDeviceX25ResetIndicationPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ResetIndicationPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25ResetConfirmPRx_Type = Counter32
_SmSiaSystemDeviceX25ResetConfirmPRx_Object = MibTableColumn
smSiaSystemDeviceX25ResetConfirmPRx = _SmSiaSystemDeviceX25ResetConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 97),
    _SmSiaSystemDeviceX25ResetConfirmPRx_Type()
)
smSiaSystemDeviceX25ResetConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25ResetConfirmPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25DiagnosticPRx_Type = Counter32
_SmSiaSystemDeviceX25DiagnosticPRx_Object = MibTableColumn
smSiaSystemDeviceX25DiagnosticPRx = _SmSiaSystemDeviceX25DiagnosticPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 98),
    _SmSiaSystemDeviceX25DiagnosticPRx_Type()
)
smSiaSystemDeviceX25DiagnosticPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25DiagnosticPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RegistrationPRx_Type = Counter32
_SmSiaSystemDeviceX25RegistrationPRx_Object = MibTableColumn
smSiaSystemDeviceX25RegistrationPRx = _SmSiaSystemDeviceX25RegistrationPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 99),
    _SmSiaSystemDeviceX25RegistrationPRx_Type()
)
smSiaSystemDeviceX25RegistrationPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RegistrationPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RegistrationConfirmPRx_Type = Counter32
_SmSiaSystemDeviceX25RegistrationConfirmPRx_Object = MibTableColumn
smSiaSystemDeviceX25RegistrationConfirmPRx = _SmSiaSystemDeviceX25RegistrationConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 100),
    _SmSiaSystemDeviceX25RegistrationConfirmPRx_Type()
)
smSiaSystemDeviceX25RegistrationConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RegistrationConfirmPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RestartPRx_Type = Counter32
_SmSiaSystemDeviceX25RestartPRx_Object = MibTableColumn
smSiaSystemDeviceX25RestartPRx = _SmSiaSystemDeviceX25RestartPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 101),
    _SmSiaSystemDeviceX25RestartPRx_Type()
)
smSiaSystemDeviceX25RestartPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RestartPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25RestartConfirmPRx_Type = Counter32
_SmSiaSystemDeviceX25RestartConfirmPRx_Object = MibTableColumn
smSiaSystemDeviceX25RestartConfirmPRx = _SmSiaSystemDeviceX25RestartConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 102),
    _SmSiaSystemDeviceX25RestartConfirmPRx_Type()
)
smSiaSystemDeviceX25RestartConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RestartConfirmPRx.setStatus("mandatory")
_SmSiaSystemDeviceX25TxUnknownSize_Type = Counter32
_SmSiaSystemDeviceX25TxUnknownSize_Object = MibTableColumn
smSiaSystemDeviceX25TxUnknownSize = _SmSiaSystemDeviceX25TxUnknownSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 103),
    _SmSiaSystemDeviceX25TxUnknownSize_Type()
)
smSiaSystemDeviceX25TxUnknownSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxUnknownSize.setStatus("mandatory")
_SmSiaSystemDeviceX25TxReserved1_Type = Counter32
_SmSiaSystemDeviceX25TxReserved1_Object = MibTableColumn
smSiaSystemDeviceX25TxReserved1 = _SmSiaSystemDeviceX25TxReserved1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 104),
    _SmSiaSystemDeviceX25TxReserved1_Type()
)
smSiaSystemDeviceX25TxReserved1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxReserved1.setStatus("mandatory")
_SmSiaSystemDeviceX25TxReserved2_Type = Counter32
_SmSiaSystemDeviceX25TxReserved2_Object = MibTableColumn
smSiaSystemDeviceX25TxReserved2 = _SmSiaSystemDeviceX25TxReserved2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 105),
    _SmSiaSystemDeviceX25TxReserved2_Type()
)
smSiaSystemDeviceX25TxReserved2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxReserved2.setStatus("mandatory")
_SmSiaSystemDeviceX25TxReserved3_Type = Counter32
_SmSiaSystemDeviceX25TxReserved3_Object = MibTableColumn
smSiaSystemDeviceX25TxReserved3 = _SmSiaSystemDeviceX25TxReserved3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 106),
    _SmSiaSystemDeviceX25TxReserved3_Type()
)
smSiaSystemDeviceX25TxReserved3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxReserved3.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx0x15_Type = Counter32
_SmSiaSystemDeviceX25Tx0x15_Object = MibTableColumn
smSiaSystemDeviceX25Tx0x15 = _SmSiaSystemDeviceX25Tx0x15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 107),
    _SmSiaSystemDeviceX25Tx0x15_Type()
)
smSiaSystemDeviceX25Tx0x15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx0x15.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx16x31_Type = Counter32
_SmSiaSystemDeviceX25Tx16x31_Object = MibTableColumn
smSiaSystemDeviceX25Tx16x31 = _SmSiaSystemDeviceX25Tx16x31_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 108),
    _SmSiaSystemDeviceX25Tx16x31_Type()
)
smSiaSystemDeviceX25Tx16x31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx16x31.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx32x63_Type = Counter32
_SmSiaSystemDeviceX25Tx32x63_Object = MibTableColumn
smSiaSystemDeviceX25Tx32x63 = _SmSiaSystemDeviceX25Tx32x63_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 109),
    _SmSiaSystemDeviceX25Tx32x63_Type()
)
smSiaSystemDeviceX25Tx32x63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx32x63.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx64x127_Type = Counter32
_SmSiaSystemDeviceX25Tx64x127_Object = MibTableColumn
smSiaSystemDeviceX25Tx64x127 = _SmSiaSystemDeviceX25Tx64x127_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 110),
    _SmSiaSystemDeviceX25Tx64x127_Type()
)
smSiaSystemDeviceX25Tx64x127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx64x127.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx128x255_Type = Counter32
_SmSiaSystemDeviceX25Tx128x255_Object = MibTableColumn
smSiaSystemDeviceX25Tx128x255 = _SmSiaSystemDeviceX25Tx128x255_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 111),
    _SmSiaSystemDeviceX25Tx128x255_Type()
)
smSiaSystemDeviceX25Tx128x255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx128x255.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx256x511_Type = Counter32
_SmSiaSystemDeviceX25Tx256x511_Object = MibTableColumn
smSiaSystemDeviceX25Tx256x511 = _SmSiaSystemDeviceX25Tx256x511_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 112),
    _SmSiaSystemDeviceX25Tx256x511_Type()
)
smSiaSystemDeviceX25Tx256x511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx256x511.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx512x1023_Type = Counter32
_SmSiaSystemDeviceX25Tx512x1023_Object = MibTableColumn
smSiaSystemDeviceX25Tx512x1023 = _SmSiaSystemDeviceX25Tx512x1023_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 113),
    _SmSiaSystemDeviceX25Tx512x1023_Type()
)
smSiaSystemDeviceX25Tx512x1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx512x1023.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx1024x2047_Type = Counter32
_SmSiaSystemDeviceX25Tx1024x2047_Object = MibTableColumn
smSiaSystemDeviceX25Tx1024x2047 = _SmSiaSystemDeviceX25Tx1024x2047_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 114),
    _SmSiaSystemDeviceX25Tx1024x2047_Type()
)
smSiaSystemDeviceX25Tx1024x2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx1024x2047.setStatus("mandatory")
_SmSiaSystemDeviceX25Tx2048x4095_Type = Counter32
_SmSiaSystemDeviceX25Tx2048x4095_Object = MibTableColumn
smSiaSystemDeviceX25Tx2048x4095 = _SmSiaSystemDeviceX25Tx2048x4095_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 115),
    _SmSiaSystemDeviceX25Tx2048x4095_Type()
)
smSiaSystemDeviceX25Tx2048x4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Tx2048x4095.setStatus("mandatory")
_SmSiaSystemDeviceX25TxReserved13_Type = Counter32
_SmSiaSystemDeviceX25TxReserved13_Object = MibTableColumn
smSiaSystemDeviceX25TxReserved13 = _SmSiaSystemDeviceX25TxReserved13_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 116),
    _SmSiaSystemDeviceX25TxReserved13_Type()
)
smSiaSystemDeviceX25TxReserved13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxReserved13.setStatus("mandatory")
_SmSiaSystemDeviceX25TxReserved14_Type = Counter32
_SmSiaSystemDeviceX25TxReserved14_Object = MibTableColumn
smSiaSystemDeviceX25TxReserved14 = _SmSiaSystemDeviceX25TxReserved14_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 117),
    _SmSiaSystemDeviceX25TxReserved14_Type()
)
smSiaSystemDeviceX25TxReserved14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxReserved14.setStatus("mandatory")
_SmSiaSystemDeviceX25TxReserved15_Type = Counter32
_SmSiaSystemDeviceX25TxReserved15_Object = MibTableColumn
smSiaSystemDeviceX25TxReserved15 = _SmSiaSystemDeviceX25TxReserved15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 118),
    _SmSiaSystemDeviceX25TxReserved15_Type()
)
smSiaSystemDeviceX25TxReserved15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxReserved15.setStatus("mandatory")
_SmSiaSystemDeviceX25TxTotalPackets_Type = Counter32
_SmSiaSystemDeviceX25TxTotalPackets_Object = MibTableColumn
smSiaSystemDeviceX25TxTotalPackets = _SmSiaSystemDeviceX25TxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 119),
    _SmSiaSystemDeviceX25TxTotalPackets_Type()
)
smSiaSystemDeviceX25TxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25TxTotalPackets.setStatus("mandatory")
_SmSiaSystemDeviceX25RxUnknownSize_Type = Counter32
_SmSiaSystemDeviceX25RxUnknownSize_Object = MibTableColumn
smSiaSystemDeviceX25RxUnknownSize = _SmSiaSystemDeviceX25RxUnknownSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 120),
    _SmSiaSystemDeviceX25RxUnknownSize_Type()
)
smSiaSystemDeviceX25RxUnknownSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxUnknownSize.setStatus("mandatory")
_SmSiaSystemDeviceX25RxReserved1_Type = Counter32
_SmSiaSystemDeviceX25RxReserved1_Object = MibTableColumn
smSiaSystemDeviceX25RxReserved1 = _SmSiaSystemDeviceX25RxReserved1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 121),
    _SmSiaSystemDeviceX25RxReserved1_Type()
)
smSiaSystemDeviceX25RxReserved1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxReserved1.setStatus("mandatory")
_SmSiaSystemDeviceX25RxReserved2_Type = Counter32
_SmSiaSystemDeviceX25RxReserved2_Object = MibTableColumn
smSiaSystemDeviceX25RxReserved2 = _SmSiaSystemDeviceX25RxReserved2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 122),
    _SmSiaSystemDeviceX25RxReserved2_Type()
)
smSiaSystemDeviceX25RxReserved2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxReserved2.setStatus("mandatory")
_SmSiaSystemDeviceX25RxReserved3_Type = Counter32
_SmSiaSystemDeviceX25RxReserved3_Object = MibTableColumn
smSiaSystemDeviceX25RxReserved3 = _SmSiaSystemDeviceX25RxReserved3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 123),
    _SmSiaSystemDeviceX25RxReserved3_Type()
)
smSiaSystemDeviceX25RxReserved3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxReserved3.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx0x15_Type = Counter32
_SmSiaSystemDeviceX25Rx0x15_Object = MibTableColumn
smSiaSystemDeviceX25Rx0x15 = _SmSiaSystemDeviceX25Rx0x15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 124),
    _SmSiaSystemDeviceX25Rx0x15_Type()
)
smSiaSystemDeviceX25Rx0x15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx0x15.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx16x31_Type = Counter32
_SmSiaSystemDeviceX25Rx16x31_Object = MibTableColumn
smSiaSystemDeviceX25Rx16x31 = _SmSiaSystemDeviceX25Rx16x31_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 125),
    _SmSiaSystemDeviceX25Rx16x31_Type()
)
smSiaSystemDeviceX25Rx16x31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx16x31.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx32x63_Type = Counter32
_SmSiaSystemDeviceX25Rx32x63_Object = MibTableColumn
smSiaSystemDeviceX25Rx32x63 = _SmSiaSystemDeviceX25Rx32x63_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 126),
    _SmSiaSystemDeviceX25Rx32x63_Type()
)
smSiaSystemDeviceX25Rx32x63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx32x63.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx64x127_Type = Counter32
_SmSiaSystemDeviceX25Rx64x127_Object = MibTableColumn
smSiaSystemDeviceX25Rx64x127 = _SmSiaSystemDeviceX25Rx64x127_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 127),
    _SmSiaSystemDeviceX25Rx64x127_Type()
)
smSiaSystemDeviceX25Rx64x127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx64x127.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx128x255_Type = Counter32
_SmSiaSystemDeviceX25Rx128x255_Object = MibTableColumn
smSiaSystemDeviceX25Rx128x255 = _SmSiaSystemDeviceX25Rx128x255_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 128),
    _SmSiaSystemDeviceX25Rx128x255_Type()
)
smSiaSystemDeviceX25Rx128x255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx128x255.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx256x511_Type = Counter32
_SmSiaSystemDeviceX25Rx256x511_Object = MibTableColumn
smSiaSystemDeviceX25Rx256x511 = _SmSiaSystemDeviceX25Rx256x511_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 129),
    _SmSiaSystemDeviceX25Rx256x511_Type()
)
smSiaSystemDeviceX25Rx256x511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx256x511.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx512x1023_Type = Counter32
_SmSiaSystemDeviceX25Rx512x1023_Object = MibTableColumn
smSiaSystemDeviceX25Rx512x1023 = _SmSiaSystemDeviceX25Rx512x1023_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 130),
    _SmSiaSystemDeviceX25Rx512x1023_Type()
)
smSiaSystemDeviceX25Rx512x1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx512x1023.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx1024x2047_Type = Counter32
_SmSiaSystemDeviceX25Rx1024x2047_Object = MibTableColumn
smSiaSystemDeviceX25Rx1024x2047 = _SmSiaSystemDeviceX25Rx1024x2047_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 131),
    _SmSiaSystemDeviceX25Rx1024x2047_Type()
)
smSiaSystemDeviceX25Rx1024x2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx1024x2047.setStatus("mandatory")
_SmSiaSystemDeviceX25Rx2048x4095_Type = Counter32
_SmSiaSystemDeviceX25Rx2048x4095_Object = MibTableColumn
smSiaSystemDeviceX25Rx2048x4095 = _SmSiaSystemDeviceX25Rx2048x4095_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 132),
    _SmSiaSystemDeviceX25Rx2048x4095_Type()
)
smSiaSystemDeviceX25Rx2048x4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Rx2048x4095.setStatus("mandatory")
_SmSiaSystemDeviceX25RxReserved13_Type = Counter32
_SmSiaSystemDeviceX25RxReserved13_Object = MibTableColumn
smSiaSystemDeviceX25RxReserved13 = _SmSiaSystemDeviceX25RxReserved13_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 133),
    _SmSiaSystemDeviceX25RxReserved13_Type()
)
smSiaSystemDeviceX25RxReserved13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxReserved13.setStatus("mandatory")
_SmSiaSystemDeviceX25RxReserved14_Type = Counter32
_SmSiaSystemDeviceX25RxReserved14_Object = MibTableColumn
smSiaSystemDeviceX25RxReserved14 = _SmSiaSystemDeviceX25RxReserved14_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 134),
    _SmSiaSystemDeviceX25RxReserved14_Type()
)
smSiaSystemDeviceX25RxReserved14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxReserved14.setStatus("mandatory")
_SmSiaSystemDeviceX25RxReserved15_Type = Counter32
_SmSiaSystemDeviceX25RxReserved15_Object = MibTableColumn
smSiaSystemDeviceX25RxReserved15 = _SmSiaSystemDeviceX25RxReserved15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 135),
    _SmSiaSystemDeviceX25RxReserved15_Type()
)
smSiaSystemDeviceX25RxReserved15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxReserved15.setStatus("mandatory")
_SmSiaSystemDeviceX25RxTotalPackets_Type = Counter32
_SmSiaSystemDeviceX25RxTotalPackets_Object = MibTableColumn
smSiaSystemDeviceX25RxTotalPackets = _SmSiaSystemDeviceX25RxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 136),
    _SmSiaSystemDeviceX25RxTotalPackets_Type()
)
smSiaSystemDeviceX25RxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RxTotalPackets.setStatus("mandatory")


class _SmSiaSystemDeviceX25Clear_Type(Integer32):
    """Custom type smSiaSystemDeviceX25Clear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("normal", 1))
    )


_SmSiaSystemDeviceX25Clear_Type.__name__ = "Integer32"
_SmSiaSystemDeviceX25Clear_Object = MibTableColumn
smSiaSystemDeviceX25Clear = _SmSiaSystemDeviceX25Clear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 137),
    _SmSiaSystemDeviceX25Clear_Type()
)
smSiaSystemDeviceX25Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25Clear.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteCount_Type = Integer32
_SmSiaSystemDeviceX25RouteCount_Object = MibScalar
smSiaSystemDeviceX25RouteCount = _SmSiaSystemDeviceX25RouteCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 3),
    _SmSiaSystemDeviceX25RouteCount_Type()
)
smSiaSystemDeviceX25RouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteCount.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteTable_Object = MibTable
smSiaSystemDeviceX25RouteTable = _SmSiaSystemDeviceX25RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4)
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteTable.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteEntry_Object = MibTableRow
smSiaSystemDeviceX25RouteEntry = _SmSiaSystemDeviceX25RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1)
)
smSiaSystemDeviceX25RouteEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemDeviceX25RouteNumber"),
)
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteEntry.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteNumber_Type = Integer32
_SmSiaSystemDeviceX25RouteNumber_Object = MibTableColumn
smSiaSystemDeviceX25RouteNumber = _SmSiaSystemDeviceX25RouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 1),
    _SmSiaSystemDeviceX25RouteNumber_Type()
)
smSiaSystemDeviceX25RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteNumber.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteEntryName_Type = DisplayString
_SmSiaSystemDeviceX25RouteEntryName_Object = MibTableColumn
smSiaSystemDeviceX25RouteEntryName = _SmSiaSystemDeviceX25RouteEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 2),
    _SmSiaSystemDeviceX25RouteEntryName_Type()
)
smSiaSystemDeviceX25RouteEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteEntryName.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteUserName_Type = DisplayString
_SmSiaSystemDeviceX25RouteUserName_Object = MibTableColumn
smSiaSystemDeviceX25RouteUserName = _SmSiaSystemDeviceX25RouteUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 3),
    _SmSiaSystemDeviceX25RouteUserName_Type()
)
smSiaSystemDeviceX25RouteUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteUserName.setStatus("mandatory")
_SmSiaSystemDeviceX25RoutePort_Type = DisplayString
_SmSiaSystemDeviceX25RoutePort_Object = MibTableColumn
smSiaSystemDeviceX25RoutePort = _SmSiaSystemDeviceX25RoutePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 4),
    _SmSiaSystemDeviceX25RoutePort_Type()
)
smSiaSystemDeviceX25RoutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RoutePort.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteCallingAddress_Type = DisplayString
_SmSiaSystemDeviceX25RouteCallingAddress_Object = MibTableColumn
smSiaSystemDeviceX25RouteCallingAddress = _SmSiaSystemDeviceX25RouteCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 5),
    _SmSiaSystemDeviceX25RouteCallingAddress_Type()
)
smSiaSystemDeviceX25RouteCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteCallingAddress.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteCalledSubaddress_Type = DisplayString
_SmSiaSystemDeviceX25RouteCalledSubaddress_Object = MibTableColumn
smSiaSystemDeviceX25RouteCalledSubaddress = _SmSiaSystemDeviceX25RouteCalledSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 6),
    _SmSiaSystemDeviceX25RouteCalledSubaddress_Type()
)
smSiaSystemDeviceX25RouteCalledSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteCalledSubaddress.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteCallingAddressExt_Type = DisplayString
_SmSiaSystemDeviceX25RouteCallingAddressExt_Object = MibTableColumn
smSiaSystemDeviceX25RouteCallingAddressExt = _SmSiaSystemDeviceX25RouteCallingAddressExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 7),
    _SmSiaSystemDeviceX25RouteCallingAddressExt_Type()
)
smSiaSystemDeviceX25RouteCallingAddressExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteCallingAddressExt.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteCalledAddressExt_Type = DisplayString
_SmSiaSystemDeviceX25RouteCalledAddressExt_Object = MibTableColumn
smSiaSystemDeviceX25RouteCalledAddressExt = _SmSiaSystemDeviceX25RouteCalledAddressExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 8),
    _SmSiaSystemDeviceX25RouteCalledAddressExt_Type()
)
smSiaSystemDeviceX25RouteCalledAddressExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteCalledAddressExt.setStatus("mandatory")
_SmSiaSystemDeviceX25RouteCalledUserData_Type = DisplayString
_SmSiaSystemDeviceX25RouteCalledUserData_Object = MibTableColumn
smSiaSystemDeviceX25RouteCalledUserData = _SmSiaSystemDeviceX25RouteCalledUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 9),
    _SmSiaSystemDeviceX25RouteCalledUserData_Type()
)
smSiaSystemDeviceX25RouteCalledUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteCalledUserData.setStatus("mandatory")
_SmSiaSystemDeviceX25RoutePriority_Type = Integer32
_SmSiaSystemDeviceX25RoutePriority_Object = MibTableColumn
smSiaSystemDeviceX25RoutePriority = _SmSiaSystemDeviceX25RoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 10),
    _SmSiaSystemDeviceX25RoutePriority_Type()
)
smSiaSystemDeviceX25RoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RoutePriority.setStatus("mandatory")


class _SmSiaSystemDeviceX25RouteAction_Type(Integer32):
    """Custom type smSiaSystemDeviceX25RouteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reject", 2))
    )


_SmSiaSystemDeviceX25RouteAction_Type.__name__ = "Integer32"
_SmSiaSystemDeviceX25RouteAction_Object = MibTableColumn
smSiaSystemDeviceX25RouteAction = _SmSiaSystemDeviceX25RouteAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 11),
    _SmSiaSystemDeviceX25RouteAction_Type()
)
smSiaSystemDeviceX25RouteAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemDeviceX25RouteAction.setStatus("mandatory")
_SmSiaSystemPagingInformation_ObjectIdentity = ObjectIdentity
smSiaSystemPagingInformation = _SmSiaSystemPagingInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4)
)
_SmSiaSystemFreePagingSpace_Type = Integer32
_SmSiaSystemFreePagingSpace_Object = MibScalar
smSiaSystemFreePagingSpace = _SmSiaSystemFreePagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 1),
    _SmSiaSystemFreePagingSpace_Type()
)
smSiaSystemFreePagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFreePagingSpace.setStatus("mandatory")
_SmSiaSystemFreePagingSpaceUntilKill_Type = Integer32
_SmSiaSystemFreePagingSpaceUntilKill_Object = MibScalar
smSiaSystemFreePagingSpaceUntilKill = _SmSiaSystemFreePagingSpaceUntilKill_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 2),
    _SmSiaSystemFreePagingSpaceUntilKill_Type()
)
smSiaSystemFreePagingSpaceUntilKill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFreePagingSpaceUntilKill.setStatus("mandatory")
_SmSiaSystemKillThresholdToFreePagingSpacePercent_Type = Integer32
_SmSiaSystemKillThresholdToFreePagingSpacePercent_Object = MibScalar
smSiaSystemKillThresholdToFreePagingSpacePercent = _SmSiaSystemKillThresholdToFreePagingSpacePercent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 3),
    _SmSiaSystemKillThresholdToFreePagingSpacePercent_Type()
)
smSiaSystemKillThresholdToFreePagingSpacePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemKillThresholdToFreePagingSpacePercent.setStatus("mandatory")
_SmSiaSystemPagingSpace_ObjectIdentity = ObjectIdentity
smSiaSystemPagingSpace = _SmSiaSystemPagingSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4)
)
_SmSiaSystemPagingSpaceCount_Type = Gauge32
_SmSiaSystemPagingSpaceCount_Object = MibScalar
smSiaSystemPagingSpaceCount = _SmSiaSystemPagingSpaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 1),
    _SmSiaSystemPagingSpaceCount_Type()
)
smSiaSystemPagingSpaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceCount.setStatus("mandatory")
_SmSiaSystemPagingSpaceTable_Object = MibTable
smSiaSystemPagingSpaceTable = _SmSiaSystemPagingSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceTable.setStatus("mandatory")
_SmSiaSystemPagingSpaceEntry_Object = MibTableRow
smSiaSystemPagingSpaceEntry = _SmSiaSystemPagingSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1)
)
smSiaSystemPagingSpaceEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemPagingSpaceName"),
)
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceEntry.setStatus("mandatory")
_SmSiaSystemPagingSpaceName_Type = DisplayString
_SmSiaSystemPagingSpaceName_Object = MibTableColumn
smSiaSystemPagingSpaceName = _SmSiaSystemPagingSpaceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 1),
    _SmSiaSystemPagingSpaceName_Type()
)
smSiaSystemPagingSpaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceName.setStatus("mandatory")
_SmSiaSystemPagingSpacePhysicalVolume_Type = DisplayString
_SmSiaSystemPagingSpacePhysicalVolume_Object = MibTableColumn
smSiaSystemPagingSpacePhysicalVolume = _SmSiaSystemPagingSpacePhysicalVolume_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 2),
    _SmSiaSystemPagingSpacePhysicalVolume_Type()
)
smSiaSystemPagingSpacePhysicalVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpacePhysicalVolume.setStatus("mandatory")
_SmSiaSystemPagingSpaceVolumeGroup_Type = DisplayString
_SmSiaSystemPagingSpaceVolumeGroup_Object = MibTableColumn
smSiaSystemPagingSpaceVolumeGroup = _SmSiaSystemPagingSpaceVolumeGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 3),
    _SmSiaSystemPagingSpaceVolumeGroup_Type()
)
smSiaSystemPagingSpaceVolumeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceVolumeGroup.setStatus("mandatory")
_SmSiaSystemPagingSpaceSize_Type = Integer32
_SmSiaSystemPagingSpaceSize_Object = MibTableColumn
smSiaSystemPagingSpaceSize = _SmSiaSystemPagingSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 4),
    _SmSiaSystemPagingSpaceSize_Type()
)
smSiaSystemPagingSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceSize.setStatus("mandatory")
_SmSiaSystemPagingSpacePercentUsed_Type = Gauge32
_SmSiaSystemPagingSpacePercentUsed_Object = MibTableColumn
smSiaSystemPagingSpacePercentUsed = _SmSiaSystemPagingSpacePercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 5),
    _SmSiaSystemPagingSpacePercentUsed_Type()
)
smSiaSystemPagingSpacePercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpacePercentUsed.setStatus("mandatory")
_SmSiaSystemPagingSpaceActive_Type = DisplayString
_SmSiaSystemPagingSpaceActive_Object = MibTableColumn
smSiaSystemPagingSpaceActive = _SmSiaSystemPagingSpaceActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 6),
    _SmSiaSystemPagingSpaceActive_Type()
)
smSiaSystemPagingSpaceActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceActive.setStatus("mandatory")
_SmSiaSystemPagingSpaceAuto_Type = DisplayString
_SmSiaSystemPagingSpaceAuto_Object = MibTableColumn
smSiaSystemPagingSpaceAuto = _SmSiaSystemPagingSpaceAuto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 7),
    _SmSiaSystemPagingSpaceAuto_Type()
)
smSiaSystemPagingSpaceAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceAuto.setStatus("mandatory")
_SmSiaSystemPagingSpaceType_Type = DisplayString
_SmSiaSystemPagingSpaceType_Object = MibTableColumn
smSiaSystemPagingSpaceType = _SmSiaSystemPagingSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 8),
    _SmSiaSystemPagingSpaceType_Type()
)
smSiaSystemPagingSpaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingSpaceType.setStatus("mandatory")
_SmSiaSystemPagingStatistics_ObjectIdentity = ObjectIdentity
smSiaSystemPagingStatistics = _SmSiaSystemPagingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5)
)
_SmSiaSystemPagingStatisticsPollingInterval_Type = Integer32
_SmSiaSystemPagingStatisticsPollingInterval_Object = MibScalar
smSiaSystemPagingStatisticsPollingInterval = _SmSiaSystemPagingStatisticsPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 1),
    _SmSiaSystemPagingStatisticsPollingInterval_Type()
)
smSiaSystemPagingStatisticsPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPollingInterval.setStatus("mandatory")
_SmSiaSystemPagingStatisticsTable_Object = MibTable
smSiaSystemPagingStatisticsTable = _SmSiaSystemPagingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsTable.setStatus("mandatory")
_SmSiaSystemPagingStatisticsEntry_Object = MibTableRow
smSiaSystemPagingStatisticsEntry = _SmSiaSystemPagingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1)
)
smSiaSystemPagingStatisticsEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemPagingStatisticsName"),
)
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsEntry.setStatus("mandatory")
_SmSiaSystemPagingStatisticsName_Type = DisplayString
_SmSiaSystemPagingStatisticsName_Object = MibTableColumn
smSiaSystemPagingStatisticsName = _SmSiaSystemPagingStatisticsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 1),
    _SmSiaSystemPagingStatisticsName_Type()
)
smSiaSystemPagingStatisticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsName.setStatus("mandatory")
_SmSiaSystemPagingStatisticsIntervalStartTime_Type = DisplayString
_SmSiaSystemPagingStatisticsIntervalStartTime_Object = MibTableColumn
smSiaSystemPagingStatisticsIntervalStartTime = _SmSiaSystemPagingStatisticsIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 2),
    _SmSiaSystemPagingStatisticsIntervalStartTime_Type()
)
smSiaSystemPagingStatisticsIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsIntervalStartTime.setStatus("mandatory")
_SmSiaSystemPagingStatisticsIntervalLength_Type = TimeTicks
_SmSiaSystemPagingStatisticsIntervalLength_Object = MibTableColumn
smSiaSystemPagingStatisticsIntervalLength = _SmSiaSystemPagingStatisticsIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 3),
    _SmSiaSystemPagingStatisticsIntervalLength_Type()
)
smSiaSystemPagingStatisticsIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsIntervalLength.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageFaults_Type = Integer32
_SmSiaSystemPagingStatisticsPageFaults_Object = MibTableColumn
smSiaSystemPagingStatisticsPageFaults = _SmSiaSystemPagingStatisticsPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 4),
    _SmSiaSystemPagingStatisticsPageFaults_Type()
)
smSiaSystemPagingStatisticsPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageFaults.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageReclaims_Type = Integer32
_SmSiaSystemPagingStatisticsPageReclaims_Object = MibTableColumn
smSiaSystemPagingStatisticsPageReclaims = _SmSiaSystemPagingStatisticsPageReclaims_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 5),
    _SmSiaSystemPagingStatisticsPageReclaims_Type()
)
smSiaSystemPagingStatisticsPageReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageReclaims.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPagesPagedIn_Type = Integer32
_SmSiaSystemPagingStatisticsPagesPagedIn_Object = MibTableColumn
smSiaSystemPagingStatisticsPagesPagedIn = _SmSiaSystemPagingStatisticsPagesPagedIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 6),
    _SmSiaSystemPagingStatisticsPagesPagedIn_Type()
)
smSiaSystemPagingStatisticsPagesPagedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPagesPagedIn.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPagesPagedOut_Type = Integer32
_SmSiaSystemPagingStatisticsPagesPagedOut_Object = MibTableColumn
smSiaSystemPagingStatisticsPagesPagedOut = _SmSiaSystemPagingStatisticsPagesPagedOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 7),
    _SmSiaSystemPagingStatisticsPagesPagedOut_Type()
)
smSiaSystemPagingStatisticsPagesPagedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPagesPagedOut.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageInsFromPagingSpace_Type = Integer32
_SmSiaSystemPagingStatisticsPageInsFromPagingSpace_Object = MibTableColumn
smSiaSystemPagingStatisticsPageInsFromPagingSpace = _SmSiaSystemPagingStatisticsPageInsFromPagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 8),
    _SmSiaSystemPagingStatisticsPageInsFromPagingSpace_Type()
)
smSiaSystemPagingStatisticsPageInsFromPagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageInsFromPagingSpace.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageOutsFromPagingSpace_Type = Integer32
_SmSiaSystemPagingStatisticsPageOutsFromPagingSpace_Object = MibTableColumn
smSiaSystemPagingStatisticsPageOutsFromPagingSpace = _SmSiaSystemPagingStatisticsPageOutsFromPagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 9),
    _SmSiaSystemPagingStatisticsPageOutsFromPagingSpace_Type()
)
smSiaSystemPagingStatisticsPageOutsFromPagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageOutsFromPagingSpace.setStatus("mandatory")
_SmSiaSystemPagingStatisticsStartIOs_Type = Integer32
_SmSiaSystemPagingStatisticsStartIOs_Object = MibTableColumn
smSiaSystemPagingStatisticsStartIOs = _SmSiaSystemPagingStatisticsStartIOs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 10),
    _SmSiaSystemPagingStatisticsStartIOs_Type()
)
smSiaSystemPagingStatisticsStartIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsStartIOs.setStatus("mandatory")
_SmSiaSystemPagingStatisticsDoneIOs_Type = Integer32
_SmSiaSystemPagingStatisticsDoneIOs_Object = MibTableColumn
smSiaSystemPagingStatisticsDoneIOs = _SmSiaSystemPagingStatisticsDoneIOs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 11),
    _SmSiaSystemPagingStatisticsDoneIOs_Type()
)
smSiaSystemPagingStatisticsDoneIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsDoneIOs.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageScans_Type = Integer32
_SmSiaSystemPagingStatisticsPageScans_Object = MibTableColumn
smSiaSystemPagingStatisticsPageScans = _SmSiaSystemPagingStatisticsPageScans_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 12),
    _SmSiaSystemPagingStatisticsPageScans_Type()
)
smSiaSystemPagingStatisticsPageScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageScans.setStatus("mandatory")
_SmSiaSystemPagingStatisticsScanClockCycles_Type = Integer32
_SmSiaSystemPagingStatisticsScanClockCycles_Object = MibTableColumn
smSiaSystemPagingStatisticsScanClockCycles = _SmSiaSystemPagingStatisticsScanClockCycles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 13),
    _SmSiaSystemPagingStatisticsScanClockCycles_Type()
)
smSiaSystemPagingStatisticsScanClockCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsScanClockCycles.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageSteals_Type = Integer32
_SmSiaSystemPagingStatisticsPageSteals_Object = MibTableColumn
smSiaSystemPagingStatisticsPageSteals = _SmSiaSystemPagingStatisticsPageSteals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 14),
    _SmSiaSystemPagingStatisticsPageSteals_Type()
)
smSiaSystemPagingStatisticsPageSteals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageSteals.setStatus("mandatory")
_SmSiaSystemPagingStatisticsFreeFrameWaits_Type = Integer32
_SmSiaSystemPagingStatisticsFreeFrameWaits_Object = MibTableColumn
smSiaSystemPagingStatisticsFreeFrameWaits = _SmSiaSystemPagingStatisticsFreeFrameWaits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 15),
    _SmSiaSystemPagingStatisticsFreeFrameWaits_Type()
)
smSiaSystemPagingStatisticsFreeFrameWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsFreeFrameWaits.setStatus("mandatory")
_SmSiaSystemPagingStatisticsExtendXPTWaits_Type = Integer32
_SmSiaSystemPagingStatisticsExtendXPTWaits_Object = MibTableColumn
smSiaSystemPagingStatisticsExtendXPTWaits = _SmSiaSystemPagingStatisticsExtendXPTWaits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 16),
    _SmSiaSystemPagingStatisticsExtendXPTWaits_Type()
)
smSiaSystemPagingStatisticsExtendXPTWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsExtendXPTWaits.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPendingIOWaits_Type = Integer32
_SmSiaSystemPagingStatisticsPendingIOWaits_Object = MibTableColumn
smSiaSystemPagingStatisticsPendingIOWaits = _SmSiaSystemPagingStatisticsPendingIOWaits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 17),
    _SmSiaSystemPagingStatisticsPendingIOWaits_Type()
)
smSiaSystemPagingStatisticsPendingIOWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPendingIOWaits.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageFaultsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPageFaultsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageFaultsMinimum = _SmSiaSystemPagingStatisticsPageFaultsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 18),
    _SmSiaSystemPagingStatisticsPageFaultsMinimum_Type()
)
smSiaSystemPagingStatisticsPageFaultsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageFaultsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageReclaimsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPageReclaimsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageReclaimsMinimum = _SmSiaSystemPagingStatisticsPageReclaimsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 19),
    _SmSiaSystemPagingStatisticsPageReclaimsMinimum_Type()
)
smSiaSystemPagingStatisticsPageReclaimsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageReclaimsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPagesPagedInMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPagesPagedInMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPagesPagedInMinimum = _SmSiaSystemPagingStatisticsPagesPagedInMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 20),
    _SmSiaSystemPagingStatisticsPagesPagedInMinimum_Type()
)
smSiaSystemPagingStatisticsPagesPagedInMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPagesPagedInMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPagesPagedOutMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPagesPagedOutMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPagesPagedOutMinimum = _SmSiaSystemPagingStatisticsPagesPagedOutMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 21),
    _SmSiaSystemPagingStatisticsPagesPagedOutMinimum_Type()
)
smSiaSystemPagingStatisticsPagesPagedOutMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPagesPagedOutMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum = _SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 22),
    _SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Type()
)
smSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum = _SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 23),
    _SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Type()
)
smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsStartIOsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsStartIOsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsStartIOsMinimum = _SmSiaSystemPagingStatisticsStartIOsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 24),
    _SmSiaSystemPagingStatisticsStartIOsMinimum_Type()
)
smSiaSystemPagingStatisticsStartIOsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsStartIOsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsDoneIOsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsDoneIOsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsDoneIOsMinimum = _SmSiaSystemPagingStatisticsDoneIOsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 25),
    _SmSiaSystemPagingStatisticsDoneIOsMinimum_Type()
)
smSiaSystemPagingStatisticsDoneIOsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsDoneIOsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageScansMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPageScansMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageScansMinimum = _SmSiaSystemPagingStatisticsPageScansMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 26),
    _SmSiaSystemPagingStatisticsPageScansMinimum_Type()
)
smSiaSystemPagingStatisticsPageScansMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageScansMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsScanClockCyclesMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsScanClockCyclesMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsScanClockCyclesMinimum = _SmSiaSystemPagingStatisticsScanClockCyclesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 27),
    _SmSiaSystemPagingStatisticsScanClockCyclesMinimum_Type()
)
smSiaSystemPagingStatisticsScanClockCyclesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsScanClockCyclesMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageStealsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPageStealsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageStealsMinimum = _SmSiaSystemPagingStatisticsPageStealsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 28),
    _SmSiaSystemPagingStatisticsPageStealsMinimum_Type()
)
smSiaSystemPagingStatisticsPageStealsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageStealsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsFreeFrameWaitsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsFreeFrameWaitsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsFreeFrameWaitsMinimum = _SmSiaSystemPagingStatisticsFreeFrameWaitsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 29),
    _SmSiaSystemPagingStatisticsFreeFrameWaitsMinimum_Type()
)
smSiaSystemPagingStatisticsFreeFrameWaitsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsFreeFrameWaitsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsExtendXPTWaitsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsExtendXPTWaitsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsExtendXPTWaitsMinimum = _SmSiaSystemPagingStatisticsExtendXPTWaitsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 30),
    _SmSiaSystemPagingStatisticsExtendXPTWaitsMinimum_Type()
)
smSiaSystemPagingStatisticsExtendXPTWaitsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsExtendXPTWaitsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPendingIOWaitsMinimum_Type = Integer32
_SmSiaSystemPagingStatisticsPendingIOWaitsMinimum_Object = MibTableColumn
smSiaSystemPagingStatisticsPendingIOWaitsMinimum = _SmSiaSystemPagingStatisticsPendingIOWaitsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 31),
    _SmSiaSystemPagingStatisticsPendingIOWaitsMinimum_Type()
)
smSiaSystemPagingStatisticsPendingIOWaitsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPendingIOWaitsMinimum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageFaultsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPageFaultsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageFaultsMaximum = _SmSiaSystemPagingStatisticsPageFaultsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 32),
    _SmSiaSystemPagingStatisticsPageFaultsMaximum_Type()
)
smSiaSystemPagingStatisticsPageFaultsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageFaultsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageReclaimsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPageReclaimsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageReclaimsMaximum = _SmSiaSystemPagingStatisticsPageReclaimsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 33),
    _SmSiaSystemPagingStatisticsPageReclaimsMaximum_Type()
)
smSiaSystemPagingStatisticsPageReclaimsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageReclaimsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPagesPagedInMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPagesPagedInMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPagesPagedInMaximum = _SmSiaSystemPagingStatisticsPagesPagedInMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 34),
    _SmSiaSystemPagingStatisticsPagesPagedInMaximum_Type()
)
smSiaSystemPagingStatisticsPagesPagedInMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPagesPagedInMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPagesPagedOutMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPagesPagedOutMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPagesPagedOutMaximum = _SmSiaSystemPagingStatisticsPagesPagedOutMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 35),
    _SmSiaSystemPagingStatisticsPagesPagedOutMaximum_Type()
)
smSiaSystemPagingStatisticsPagesPagedOutMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPagesPagedOutMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum = _SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 36),
    _SmSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Type()
)
smSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum = _SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 37),
    _SmSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Type()
)
smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsStartIOsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsStartIOsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsStartIOsMaximum = _SmSiaSystemPagingStatisticsStartIOsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 38),
    _SmSiaSystemPagingStatisticsStartIOsMaximum_Type()
)
smSiaSystemPagingStatisticsStartIOsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsStartIOsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsDoneIOsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsDoneIOsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsDoneIOsMaximum = _SmSiaSystemPagingStatisticsDoneIOsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 39),
    _SmSiaSystemPagingStatisticsDoneIOsMaximum_Type()
)
smSiaSystemPagingStatisticsDoneIOsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsDoneIOsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageScansMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPageScansMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageScansMaximum = _SmSiaSystemPagingStatisticsPageScansMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 40),
    _SmSiaSystemPagingStatisticsPageScansMaximum_Type()
)
smSiaSystemPagingStatisticsPageScansMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageScansMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsScanClockCyclesMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsScanClockCyclesMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsScanClockCyclesMaximum = _SmSiaSystemPagingStatisticsScanClockCyclesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 41),
    _SmSiaSystemPagingStatisticsScanClockCyclesMaximum_Type()
)
smSiaSystemPagingStatisticsScanClockCyclesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsScanClockCyclesMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPageStealsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPageStealsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPageStealsMaximum = _SmSiaSystemPagingStatisticsPageStealsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 42),
    _SmSiaSystemPagingStatisticsPageStealsMaximum_Type()
)
smSiaSystemPagingStatisticsPageStealsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPageStealsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsFreeFrameWaitsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsFreeFrameWaitsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsFreeFrameWaitsMaximum = _SmSiaSystemPagingStatisticsFreeFrameWaitsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 43),
    _SmSiaSystemPagingStatisticsFreeFrameWaitsMaximum_Type()
)
smSiaSystemPagingStatisticsFreeFrameWaitsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsFreeFrameWaitsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsExtendXPTWaitsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsExtendXPTWaitsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsExtendXPTWaitsMaximum = _SmSiaSystemPagingStatisticsExtendXPTWaitsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 44),
    _SmSiaSystemPagingStatisticsExtendXPTWaitsMaximum_Type()
)
smSiaSystemPagingStatisticsExtendXPTWaitsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsExtendXPTWaitsMaximum.setStatus("mandatory")
_SmSiaSystemPagingStatisticsPendingIOWaitsMaximum_Type = Integer32
_SmSiaSystemPagingStatisticsPendingIOWaitsMaximum_Object = MibTableColumn
smSiaSystemPagingStatisticsPendingIOWaitsMaximum = _SmSiaSystemPagingStatisticsPendingIOWaitsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 45),
    _SmSiaSystemPagingStatisticsPendingIOWaitsMaximum_Type()
)
smSiaSystemPagingStatisticsPendingIOWaitsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemPagingStatisticsPendingIOWaitsMaximum.setStatus("mandatory")
_SmSiaSystemFileSystem_ObjectIdentity = ObjectIdentity
smSiaSystemFileSystem = _SmSiaSystemFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5)
)
_SmSiaSystemFileSystemMounted_Type = Gauge32
_SmSiaSystemFileSystemMounted_Object = MibScalar
smSiaSystemFileSystemMounted = _SmSiaSystemFileSystemMounted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 1),
    _SmSiaSystemFileSystemMounted_Type()
)
smSiaSystemFileSystemMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemMounted.setStatus("mandatory")
_SmSiaSystemFileSystemTable_Object = MibTable
smSiaSystemFileSystemTable = _SmSiaSystemFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemFileSystemTable.setStatus("mandatory")
_SmSiaSystemFileSystemEntry_Object = MibTableRow
smSiaSystemFileSystemEntry = _SmSiaSystemFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1)
)
smSiaSystemFileSystemEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemFileSystemName"),
)
if mibBuilder.loadTexts:
    smSiaSystemFileSystemEntry.setStatus("mandatory")
_SmSiaSystemFileSystemName_Type = DisplayString
_SmSiaSystemFileSystemName_Object = MibTableColumn
smSiaSystemFileSystemName = _SmSiaSystemFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 1),
    _SmSiaSystemFileSystemName_Type()
)
smSiaSystemFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemName.setStatus("mandatory")
_SmSiaSystemFileSystemSize_Type = Gauge32
_SmSiaSystemFileSystemSize_Object = MibTableColumn
smSiaSystemFileSystemSize = _SmSiaSystemFileSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 2),
    _SmSiaSystemFileSystemSize_Type()
)
smSiaSystemFileSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemSize.setStatus("mandatory")
_SmSiaSystemFileSystemFree_Type = Gauge32
_SmSiaSystemFileSystemFree_Object = MibTableColumn
smSiaSystemFileSystemFree = _SmSiaSystemFileSystemFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 3),
    _SmSiaSystemFileSystemFree_Type()
)
smSiaSystemFileSystemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemFree.setStatus("mandatory")
_SmSiaSystemFileSystemPercentUsed_Type = Gauge32
_SmSiaSystemFileSystemPercentUsed_Object = MibTableColumn
smSiaSystemFileSystemPercentUsed = _SmSiaSystemFileSystemPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 4),
    _SmSiaSystemFileSystemPercentUsed_Type()
)
smSiaSystemFileSystemPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemPercentUsed.setStatus("mandatory")
_SmSiaSystemFileSystemInodesUsed_Type = Gauge32
_SmSiaSystemFileSystemInodesUsed_Object = MibTableColumn
smSiaSystemFileSystemInodesUsed = _SmSiaSystemFileSystemInodesUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 5),
    _SmSiaSystemFileSystemInodesUsed_Type()
)
smSiaSystemFileSystemInodesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemInodesUsed.setStatus("mandatory")
_SmSiaSystemFileSystemInodesPercentUsed_Type = Gauge32
_SmSiaSystemFileSystemInodesPercentUsed_Object = MibTableColumn
smSiaSystemFileSystemInodesPercentUsed = _SmSiaSystemFileSystemInodesPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 6),
    _SmSiaSystemFileSystemInodesPercentUsed_Type()
)
smSiaSystemFileSystemInodesPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemInodesPercentUsed.setStatus("mandatory")
_SmSiaSystemFileSystemInodeCount_Type = Gauge32
_SmSiaSystemFileSystemInodeCount_Object = MibTableColumn
smSiaSystemFileSystemInodeCount = _SmSiaSystemFileSystemInodeCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 7),
    _SmSiaSystemFileSystemInodeCount_Type()
)
smSiaSystemFileSystemInodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemInodeCount.setStatus("mandatory")
_SmSiaSystemFileSystemFileSystem_Type = DisplayString
_SmSiaSystemFileSystemFileSystem_Object = MibTableColumn
smSiaSystemFileSystemFileSystem = _SmSiaSystemFileSystemFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 8),
    _SmSiaSystemFileSystemFileSystem_Type()
)
smSiaSystemFileSystemFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemFileSystem.setStatus("mandatory")
_SmSiaSystemFileSystemRemote_Type = DisplayString
_SmSiaSystemFileSystemRemote_Object = MibTableColumn
smSiaSystemFileSystemRemote = _SmSiaSystemFileSystemRemote_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 9),
    _SmSiaSystemFileSystemRemote_Type()
)
smSiaSystemFileSystemRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemFileSystemRemote.setStatus("mandatory")
_SmSiaSystemSubSystems_ObjectIdentity = ObjectIdentity
smSiaSystemSubSystems = _SmSiaSystemSubSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6)
)
_SmSiaSystemSubSystemsCount_Type = Gauge32
_SmSiaSystemSubSystemsCount_Object = MibScalar
smSiaSystemSubSystemsCount = _SmSiaSystemSubSystemsCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 1),
    _SmSiaSystemSubSystemsCount_Type()
)
smSiaSystemSubSystemsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsCount.setStatus("mandatory")
_SmSiaSystemSubSystemsTable_Object = MibTable
smSiaSystemSubSystemsTable = _SmSiaSystemSubSystemsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsTable.setStatus("mandatory")
_SmSiaSystemSubSystemsEntry_Object = MibTableRow
smSiaSystemSubSystemsEntry = _SmSiaSystemSubSystemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1)
)
smSiaSystemSubSystemsEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemSubSystemsName"),
)
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsEntry.setStatus("mandatory")
_SmSiaSystemSubSystemsName_Type = DisplayString
_SmSiaSystemSubSystemsName_Object = MibTableColumn
smSiaSystemSubSystemsName = _SmSiaSystemSubSystemsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 1),
    _SmSiaSystemSubSystemsName_Type()
)
smSiaSystemSubSystemsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsName.setStatus("mandatory")
_SmSiaSystemSubSystemsPID_Type = Integer32
_SmSiaSystemSubSystemsPID_Object = MibTableColumn
smSiaSystemSubSystemsPID = _SmSiaSystemSubSystemsPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 2),
    _SmSiaSystemSubSystemsPID_Type()
)
smSiaSystemSubSystemsPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsPID.setStatus("mandatory")
_SmSiaSystemSubSystemsStatusDescription_Type = DisplayString
_SmSiaSystemSubSystemsStatusDescription_Object = MibTableColumn
smSiaSystemSubSystemsStatusDescription = _SmSiaSystemSubSystemsStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 3),
    _SmSiaSystemSubSystemsStatusDescription_Type()
)
smSiaSystemSubSystemsStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsStatusDescription.setStatus("mandatory")
_SmSiaSystemSubSystemsStatusText_Type = DisplayString
_SmSiaSystemSubSystemsStatusText_Object = MibTableColumn
smSiaSystemSubSystemsStatusText = _SmSiaSystemSubSystemsStatusText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 4),
    _SmSiaSystemSubSystemsStatusText_Type()
)
smSiaSystemSubSystemsStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsStatusText.setStatus("mandatory")
_SmSiaSystemSubSystemsStatusCode_Type = Integer32
_SmSiaSystemSubSystemsStatusCode_Object = MibTableColumn
smSiaSystemSubSystemsStatusCode = _SmSiaSystemSubSystemsStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 5),
    _SmSiaSystemSubSystemsStatusCode_Type()
)
smSiaSystemSubSystemsStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemSubSystemsStatusCode.setStatus("mandatory")
_SmSiaSystemProcess_ObjectIdentity = ObjectIdentity
smSiaSystemProcess = _SmSiaSystemProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7)
)
_SmSiaSystemProcessCount_Type = Gauge32
_SmSiaSystemProcessCount_Object = MibScalar
smSiaSystemProcessCount = _SmSiaSystemProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 1),
    _SmSiaSystemProcessCount_Type()
)
smSiaSystemProcessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessCount.setStatus("mandatory")
_SmSiaSystemProcessTable_Object = MibTable
smSiaSystemProcessTable = _SmSiaSystemProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemProcessTable.setStatus("mandatory")
_SmSiaSystemProcessEntry_Object = MibTableRow
smSiaSystemProcessEntry = _SmSiaSystemProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1)
)
smSiaSystemProcessEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemProcessCommand"),
    (0, "SYSINFO-MIB", "smSiaSystemProcessPID"),
)
if mibBuilder.loadTexts:
    smSiaSystemProcessEntry.setStatus("mandatory")
_SmSiaSystemProcessLoginUser_Type = DisplayString
_SmSiaSystemProcessLoginUser_Object = MibTableColumn
smSiaSystemProcessLoginUser = _SmSiaSystemProcessLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 1),
    _SmSiaSystemProcessLoginUser_Type()
)
smSiaSystemProcessLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessLoginUser.setStatus("mandatory")
_SmSiaSystemProcessPID_Type = Integer32
_SmSiaSystemProcessPID_Object = MibTableColumn
smSiaSystemProcessPID = _SmSiaSystemProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 2),
    _SmSiaSystemProcessPID_Type()
)
smSiaSystemProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPID.setStatus("mandatory")
_SmSiaSystemProcessParentPID_Type = Integer32
_SmSiaSystemProcessParentPID_Object = MibTableColumn
smSiaSystemProcessParentPID = _SmSiaSystemProcessParentPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 3),
    _SmSiaSystemProcessParentPID_Type()
)
smSiaSystemProcessParentPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessParentPID.setStatus("mandatory")
_SmSiaSystemProcessCPUTime_Type = TimeTicks
_SmSiaSystemProcessCPUTime_Object = MibTableColumn
smSiaSystemProcessCPUTime = _SmSiaSystemProcessCPUTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 4),
    _SmSiaSystemProcessCPUTime_Type()
)
smSiaSystemProcessCPUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessCPUTime.setStatus("mandatory")
_SmSiaSystemProcessUserTime_Type = TimeTicks
_SmSiaSystemProcessUserTime_Object = MibTableColumn
smSiaSystemProcessUserTime = _SmSiaSystemProcessUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 5),
    _SmSiaSystemProcessUserTime_Type()
)
smSiaSystemProcessUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessUserTime.setStatus("mandatory")
_SmSiaSystemProcessSystemTime_Type = TimeTicks
_SmSiaSystemProcessSystemTime_Object = MibTableColumn
smSiaSystemProcessSystemTime = _SmSiaSystemProcessSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 6),
    _SmSiaSystemProcessSystemTime_Type()
)
smSiaSystemProcessSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessSystemTime.setStatus("mandatory")
_SmSiaSystemProcessPageFaultsIO_Type = Counter32
_SmSiaSystemProcessPageFaultsIO_Object = MibTableColumn
smSiaSystemProcessPageFaultsIO = _SmSiaSystemProcessPageFaultsIO_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 7),
    _SmSiaSystemProcessPageFaultsIO_Type()
)
smSiaSystemProcessPageFaultsIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPageFaultsIO.setStatus("mandatory")
_SmSiaSystemProcessPageFaultsNoIO_Type = Counter32
_SmSiaSystemProcessPageFaultsNoIO_Object = MibTableColumn
smSiaSystemProcessPageFaultsNoIO = _SmSiaSystemProcessPageFaultsNoIO_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 8),
    _SmSiaSystemProcessPageFaultsNoIO_Type()
)
smSiaSystemProcessPageFaultsNoIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPageFaultsNoIO.setStatus("mandatory")
_SmSiaSystemProcessPriority_Type = Integer32
_SmSiaSystemProcessPriority_Object = MibTableColumn
smSiaSystemProcessPriority = _SmSiaSystemProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 9),
    _SmSiaSystemProcessPriority_Type()
)
smSiaSystemProcessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPriority.setStatus("mandatory")
_SmSiaSystemProcessNice_Type = Integer32
_SmSiaSystemProcessNice_Object = MibTableColumn
smSiaSystemProcessNice = _SmSiaSystemProcessNice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 10),
    _SmSiaSystemProcessNice_Type()
)
smSiaSystemProcessNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessNice.setStatus("mandatory")


class _SmSiaSystemProcessState_Type(Integer32):
    """Custom type smSiaSystemProcessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              666)
        )
    )
    namedValues = NamedValues(
        *(("iDL", 4),
          ("none", 666),
          ("run", 3),
          ("sleep", 1),
          ("stop", 6),
          ("zombie", 5))
    )


_SmSiaSystemProcessState_Type.__name__ = "Integer32"
_SmSiaSystemProcessState_Object = MibTableColumn
smSiaSystemProcessState = _SmSiaSystemProcessState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 11),
    _SmSiaSystemProcessState_Type()
)
smSiaSystemProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessState.setStatus("mandatory")


class _SmSiaSystemProcessWait_Type(Integer32):
    """Custom type smSiaSystemProcessWait based on Integer32"""
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
              8,
              9,
              666)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 4),
          ("event", 1),
          ("lock", 2),
          ("memory", 9),
          ("none", 666),
          ("pLock", 7),
          ("pageFree", 8),
          ("pageIn", 5),
          ("pageOut", 6),
          ("timer", 3))
    )


_SmSiaSystemProcessWait_Type.__name__ = "Integer32"
_SmSiaSystemProcessWait_Object = MibTableColumn
smSiaSystemProcessWait = _SmSiaSystemProcessWait_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 12),
    _SmSiaSystemProcessWait_Type()
)
smSiaSystemProcessWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessWait.setStatus("mandatory")
_SmSiaSystemProcessDataResidentSetSize_Type = Integer32
_SmSiaSystemProcessDataResidentSetSize_Object = MibTableColumn
smSiaSystemProcessDataResidentSetSize = _SmSiaSystemProcessDataResidentSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 13),
    _SmSiaSystemProcessDataResidentSetSize_Type()
)
smSiaSystemProcessDataResidentSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessDataResidentSetSize.setStatus("mandatory")
_SmSiaSystemProcessTextResidentSetSize_Type = Integer32
_SmSiaSystemProcessTextResidentSetSize_Object = MibTableColumn
smSiaSystemProcessTextResidentSetSize = _SmSiaSystemProcessTextResidentSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 14),
    _SmSiaSystemProcessTextResidentSetSize_Type()
)
smSiaSystemProcessTextResidentSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessTextResidentSetSize.setStatus("mandatory")
_SmSiaSystemProcessImageSize_Type = Integer32
_SmSiaSystemProcessImageSize_Object = MibTableColumn
smSiaSystemProcessImageSize = _SmSiaSystemProcessImageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 15),
    _SmSiaSystemProcessImageSize_Type()
)
smSiaSystemProcessImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessImageSize.setStatus("mandatory")
_SmSiaSystemProcessDataVirtualMemorySize_Type = Integer32
_SmSiaSystemProcessDataVirtualMemorySize_Object = MibTableColumn
smSiaSystemProcessDataVirtualMemorySize = _SmSiaSystemProcessDataVirtualMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 16),
    _SmSiaSystemProcessDataVirtualMemorySize_Type()
)
smSiaSystemProcessDataVirtualMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessDataVirtualMemorySize.setStatus("mandatory")
_SmSiaSystemProcessPercentMemory_Type = Integer32
_SmSiaSystemProcessPercentMemory_Object = MibTableColumn
smSiaSystemProcessPercentMemory = _SmSiaSystemProcessPercentMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 17),
    _SmSiaSystemProcessPercentMemory_Type()
)
smSiaSystemProcessPercentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPercentMemory.setStatus("mandatory")
_SmSiaSystemProcessCPU_Type = Integer32
_SmSiaSystemProcessCPU_Object = MibTableColumn
smSiaSystemProcessCPU = _SmSiaSystemProcessCPU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 18),
    _SmSiaSystemProcessCPU_Type()
)
smSiaSystemProcessCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessCPU.setStatus("mandatory")
_SmSiaSystemProcessStartTime_Type = DisplayString
_SmSiaSystemProcessStartTime_Object = MibTableColumn
smSiaSystemProcessStartTime = _SmSiaSystemProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 19),
    _SmSiaSystemProcessStartTime_Type()
)
smSiaSystemProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessStartTime.setStatus("mandatory")
_SmSiaSystemProcessCommand_Type = DisplayString
_SmSiaSystemProcessCommand_Object = MibTableColumn
smSiaSystemProcessCommand = _SmSiaSystemProcessCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 20),
    _SmSiaSystemProcessCommand_Type()
)
smSiaSystemProcessCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessCommand.setStatus("mandatory")
_SmSiaSystemProcessLoginUID_Type = Integer32
_SmSiaSystemProcessLoginUID_Object = MibTableColumn
smSiaSystemProcessLoginUID = _SmSiaSystemProcessLoginUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 21),
    _SmSiaSystemProcessLoginUID_Type()
)
smSiaSystemProcessLoginUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessLoginUID.setStatus("mandatory")
_SmSiaSystemProcessEffectiveUID_Type = Integer32
_SmSiaSystemProcessEffectiveUID_Object = MibTableColumn
smSiaSystemProcessEffectiveUID = _SmSiaSystemProcessEffectiveUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 22),
    _SmSiaSystemProcessEffectiveUID_Type()
)
smSiaSystemProcessEffectiveUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessEffectiveUID.setStatus("mandatory")
_SmSiaSystemProcessEffectiveGID_Type = Integer32
_SmSiaSystemProcessEffectiveGID_Object = MibTableColumn
smSiaSystemProcessEffectiveGID = _SmSiaSystemProcessEffectiveGID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 23),
    _SmSiaSystemProcessEffectiveGID_Type()
)
smSiaSystemProcessEffectiveGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessEffectiveGID.setStatus("mandatory")
_SmSiaSystemProcessEffectiveGroupName_Type = DisplayString
_SmSiaSystemProcessEffectiveGroupName_Object = MibTableColumn
smSiaSystemProcessEffectiveGroupName = _SmSiaSystemProcessEffectiveGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 24),
    _SmSiaSystemProcessEffectiveGroupName_Type()
)
smSiaSystemProcessEffectiveGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessEffectiveGroupName.setStatus("mandatory")
_SmSiaSystemProcessSUID_Type = Integer32
_SmSiaSystemProcessSUID_Object = MibTableColumn
smSiaSystemProcessSUID = _SmSiaSystemProcessSUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 25),
    _SmSiaSystemProcessSUID_Type()
)
smSiaSystemProcessSUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessSUID.setStatus("mandatory")
_SmSiaSystemProcessPgrp_Type = Integer32
_SmSiaSystemProcessPgrp_Object = MibTableColumn
smSiaSystemProcessPgrp = _SmSiaSystemProcessPgrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 26),
    _SmSiaSystemProcessPgrp_Type()
)
smSiaSystemProcessPgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPgrp.setStatus("mandatory")
_SmSiaSystemProcessPFlags_Type = Integer32
_SmSiaSystemProcessPFlags_Object = MibTableColumn
smSiaSystemProcessPFlags = _SmSiaSystemProcessPFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 27),
    _SmSiaSystemProcessPFlags_Type()
)
smSiaSystemProcessPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessPFlags.setStatus("mandatory")
_SmSiaSystemProcessAdspace_Type = Gauge32
_SmSiaSystemProcessAdspace_Object = MibTableColumn
smSiaSystemProcessAdspace = _SmSiaSystemProcessAdspace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 28),
    _SmSiaSystemProcessAdspace_Type()
)
smSiaSystemProcessAdspace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessAdspace.setStatus("mandatory")
_SmSiaSystemProcessTTYp_Type = Integer32
_SmSiaSystemProcessTTYp_Object = MibTableColumn
smSiaSystemProcessTTYp = _SmSiaSystemProcessTTYp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 29),
    _SmSiaSystemProcessTTYp_Type()
)
smSiaSystemProcessTTYp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessTTYp.setStatus("mandatory")
_SmSiaSystemProcessTTYd_Type = Integer32
_SmSiaSystemProcessTTYd_Object = MibTableColumn
smSiaSystemProcessTTYd = _SmSiaSystemProcessTTYd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 30),
    _SmSiaSystemProcessTTYd_Type()
)
smSiaSystemProcessTTYd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessTTYd.setStatus("mandatory")
_SmSiaSystemProcessNSwap_Type = Counter32
_SmSiaSystemProcessNSwap_Object = MibTableColumn
smSiaSystemProcessNSwap = _SmSiaSystemProcessNSwap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 31),
    _SmSiaSystemProcessNSwap_Type()
)
smSiaSystemProcessNSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessNSwap.setStatus("mandatory")
_SmSiaSystemProcessInblocks_Type = Counter32
_SmSiaSystemProcessInblocks_Object = MibTableColumn
smSiaSystemProcessInblocks = _SmSiaSystemProcessInblocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 32),
    _SmSiaSystemProcessInblocks_Type()
)
smSiaSystemProcessInblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessInblocks.setStatus("mandatory")
_SmSiaSystemProcessOutblocks_Type = Counter32
_SmSiaSystemProcessOutblocks_Object = MibTableColumn
smSiaSystemProcessOutblocks = _SmSiaSystemProcessOutblocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 33),
    _SmSiaSystemProcessOutblocks_Type()
)
smSiaSystemProcessOutblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessOutblocks.setStatus("mandatory")
_SmSiaSystemProcessMsgsnd_Type = Counter32
_SmSiaSystemProcessMsgsnd_Object = MibTableColumn
smSiaSystemProcessMsgsnd = _SmSiaSystemProcessMsgsnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 34),
    _SmSiaSystemProcessMsgsnd_Type()
)
smSiaSystemProcessMsgsnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessMsgsnd.setStatus("mandatory")
_SmSiaSystemProcessMsgrcv_Type = Counter32
_SmSiaSystemProcessMsgrcv_Object = MibTableColumn
smSiaSystemProcessMsgrcv = _SmSiaSystemProcessMsgrcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 35),
    _SmSiaSystemProcessMsgrcv_Type()
)
smSiaSystemProcessMsgrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessMsgrcv.setStatus("mandatory")
_SmSiaSystemProcessNsignals_Type = Counter32
_SmSiaSystemProcessNsignals_Object = MibTableColumn
smSiaSystemProcessNsignals = _SmSiaSystemProcessNsignals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 36),
    _SmSiaSystemProcessNsignals_Type()
)
smSiaSystemProcessNsignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessNsignals.setStatus("mandatory")
_SmSiaSystemProcessNVcsw_Type = Counter32
_SmSiaSystemProcessNVcsw_Object = MibTableColumn
smSiaSystemProcessNVcsw = _SmSiaSystemProcessNVcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 37),
    _SmSiaSystemProcessNVcsw_Type()
)
smSiaSystemProcessNVcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessNVcsw.setStatus("mandatory")
_SmSiaSystemProcessNIvcsw_Type = Counter32
_SmSiaSystemProcessNIvcsw_Object = MibTableColumn
smSiaSystemProcessNIvcsw = _SmSiaSystemProcessNIvcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 38),
    _SmSiaSystemProcessNIvcsw_Type()
)
smSiaSystemProcessNIvcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessNIvcsw.setStatus("mandatory")
_SmSiaSystemProcessArguments_Type = DisplayString
_SmSiaSystemProcessArguments_Object = MibTableColumn
smSiaSystemProcessArguments = _SmSiaSystemProcessArguments_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 39),
    _SmSiaSystemProcessArguments_Type()
)
smSiaSystemProcessArguments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemProcessArguments.setStatus("mandatory")


class _SmSiaSystemProcessSignal_Type(Integer32):
    """Custom type smSiaSystemProcessSignal based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("sigabrt", 6),
          ("sigalrm", 14),
          ("sigbus", 10),
          ("sigchld", 20),
          ("sigcont", 19),
          ("sigdanger", 33),
          ("sigemt", 7),
          ("sigfpe", 8),
          ("siggrant", 60),
          ("sighup", 1),
          ("sigill", 4),
          ("sigint", 2),
          ("sigio", 23),
          ("sigkill", 9),
          ("sigmigrate", 35),
          ("sigmsg", 27),
          ("sigpipe", 13),
          ("sigpre", 36),
          ("sigprof", 32),
          ("sigpwr", 29),
          ("sigquit", 3),
          ("sigretract", 61),
          ("sigsak", 63),
          ("sigsegv", 11),
          ("sigsound", 62),
          ("sigstop", 17),
          ("sigsys", 12),
          ("sigterm", 15),
          ("sigtrap", 5),
          ("sigtstp", 18),
          ("sigttin", 21),
          ("sigttou", 22),
          ("sigurg", 16),
          ("sigusr1", 30),
          ("sigusr2", 31),
          ("sigvirt", 37),
          ("sigvtalrm", 34),
          ("sigwinch", 28),
          ("sigxcpu", 24),
          ("sigxfsz", 25))
    )


_SmSiaSystemProcessSignal_Type.__name__ = "Integer32"
_SmSiaSystemProcessSignal_Object = MibTableColumn
smSiaSystemProcessSignal = _SmSiaSystemProcessSignal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 40),
    _SmSiaSystemProcessSignal_Type()
)
smSiaSystemProcessSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaSystemProcessSignal.setStatus("mandatory")
_SmSiaSystemUsers_ObjectIdentity = ObjectIdentity
smSiaSystemUsers = _SmSiaSystemUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8)
)
_SmSiaSystemUsersLoggedIn_Type = Gauge32
_SmSiaSystemUsersLoggedIn_Object = MibScalar
smSiaSystemUsersLoggedIn = _SmSiaSystemUsersLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 1),
    _SmSiaSystemUsersLoggedIn_Type()
)
smSiaSystemUsersLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUsersLoggedIn.setStatus("mandatory")
_SmSiaSystemUsersTable_Object = MibTable
smSiaSystemUsersTable = _SmSiaSystemUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemUsersTable.setStatus("mandatory")
_SmSiaSystemUsersEntry_Object = MibTableRow
smSiaSystemUsersEntry = _SmSiaSystemUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1)
)
smSiaSystemUsersEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemUsersName"),
    (0, "SYSINFO-MIB", "smSiaSystemUsersPID"),
)
if mibBuilder.loadTexts:
    smSiaSystemUsersEntry.setStatus("mandatory")
_SmSiaSystemUsersName_Type = DisplayString
_SmSiaSystemUsersName_Object = MibTableColumn
smSiaSystemUsersName = _SmSiaSystemUsersName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 1),
    _SmSiaSystemUsersName_Type()
)
smSiaSystemUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUsersName.setStatus("mandatory")
_SmSiaSystemUsersLine_Type = DisplayString
_SmSiaSystemUsersLine_Object = MibTableColumn
smSiaSystemUsersLine = _SmSiaSystemUsersLine_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 2),
    _SmSiaSystemUsersLine_Type()
)
smSiaSystemUsersLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUsersLine.setStatus("mandatory")
_SmSiaSystemUsersTime_Type = DisplayString
_SmSiaSystemUsersTime_Object = MibTableColumn
smSiaSystemUsersTime = _SmSiaSystemUsersTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 3),
    _SmSiaSystemUsersTime_Type()
)
smSiaSystemUsersTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUsersTime.setStatus("mandatory")
_SmSiaSystemUsersPID_Type = Integer32
_SmSiaSystemUsersPID_Object = MibTableColumn
smSiaSystemUsersPID = _SmSiaSystemUsersPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 4),
    _SmSiaSystemUsersPID_Type()
)
smSiaSystemUsersPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUsersPID.setStatus("mandatory")
_SmSiaSystemUsersRemoteHost_Type = DisplayString
_SmSiaSystemUsersRemoteHost_Object = MibTableColumn
smSiaSystemUsersRemoteHost = _SmSiaSystemUsersRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 5),
    _SmSiaSystemUsersRemoteHost_Type()
)
smSiaSystemUsersRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUsersRemoteHost.setStatus("mandatory")
_SmSiaSystemUtilization_ObjectIdentity = ObjectIdentity
smSiaSystemUtilization = _SmSiaSystemUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9)
)
_SmSiaSystemUtilizationCPU_ObjectIdentity = ObjectIdentity
smSiaSystemUtilizationCPU = _SmSiaSystemUtilizationCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1)
)
_SmSiaSystemUtilizationCPUPollingInterval_Type = Integer32
_SmSiaSystemUtilizationCPUPollingInterval_Object = MibScalar
smSiaSystemUtilizationCPUPollingInterval = _SmSiaSystemUtilizationCPUPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 1),
    _SmSiaSystemUtilizationCPUPollingInterval_Type()
)
smSiaSystemUtilizationCPUPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUPollingInterval.setStatus("mandatory")
_SmSiaSystemUtilizationCPUCount_Type = Integer32
_SmSiaSystemUtilizationCPUCount_Object = MibScalar
smSiaSystemUtilizationCPUCount = _SmSiaSystemUtilizationCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 2),
    _SmSiaSystemUtilizationCPUCount_Type()
)
smSiaSystemUtilizationCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUCount.setStatus("mandatory")
_SmSiaSystemUtilizationCPUTable_Object = MibTable
smSiaSystemUtilizationCPUTable = _SmSiaSystemUtilizationCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUTable.setStatus("mandatory")
_SmSiaSystemUtilizationCPUEntry_Object = MibTableRow
smSiaSystemUtilizationCPUEntry = _SmSiaSystemUtilizationCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1)
)
smSiaSystemUtilizationCPUEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemUtilizationCPUIntervalName"),
)
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUEntry.setStatus("mandatory")
_SmSiaSystemUtilizationCPUIntervalName_Type = DisplayString
_SmSiaSystemUtilizationCPUIntervalName_Object = MibTableColumn
smSiaSystemUtilizationCPUIntervalName = _SmSiaSystemUtilizationCPUIntervalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 1),
    _SmSiaSystemUtilizationCPUIntervalName_Type()
)
smSiaSystemUtilizationCPUIntervalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUIntervalName.setStatus("mandatory")
_SmSiaSystemUtilizationCPUIntervalStartTime_Type = DisplayString
_SmSiaSystemUtilizationCPUIntervalStartTime_Object = MibTableColumn
smSiaSystemUtilizationCPUIntervalStartTime = _SmSiaSystemUtilizationCPUIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 2),
    _SmSiaSystemUtilizationCPUIntervalStartTime_Type()
)
smSiaSystemUtilizationCPUIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUIntervalStartTime.setStatus("mandatory")
_SmSiaSystemUtilizationCPUIntervalLength_Type = TimeTicks
_SmSiaSystemUtilizationCPUIntervalLength_Object = MibTableColumn
smSiaSystemUtilizationCPUIntervalLength = _SmSiaSystemUtilizationCPUIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 3),
    _SmSiaSystemUtilizationCPUIntervalLength_Type()
)
smSiaSystemUtilizationCPUIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUIntervalLength.setStatus("mandatory")
_SmSiaSystemUtilizationCPUUser_Type = Integer32
_SmSiaSystemUtilizationCPUUser_Object = MibTableColumn
smSiaSystemUtilizationCPUUser = _SmSiaSystemUtilizationCPUUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 4),
    _SmSiaSystemUtilizationCPUUser_Type()
)
smSiaSystemUtilizationCPUUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUUser.setStatus("mandatory")
_SmSiaSystemUtilizationCPUSystem_Type = Integer32
_SmSiaSystemUtilizationCPUSystem_Object = MibTableColumn
smSiaSystemUtilizationCPUSystem = _SmSiaSystemUtilizationCPUSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 5),
    _SmSiaSystemUtilizationCPUSystem_Type()
)
smSiaSystemUtilizationCPUSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUSystem.setStatus("mandatory")
_SmSiaSystemUtilizationCPUIdle_Type = Integer32
_SmSiaSystemUtilizationCPUIdle_Object = MibTableColumn
smSiaSystemUtilizationCPUIdle = _SmSiaSystemUtilizationCPUIdle_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 6),
    _SmSiaSystemUtilizationCPUIdle_Type()
)
smSiaSystemUtilizationCPUIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUIdle.setStatus("mandatory")
_SmSiaSystemUtilizationCPUWait_Type = Integer32
_SmSiaSystemUtilizationCPUWait_Object = MibTableColumn
smSiaSystemUtilizationCPUWait = _SmSiaSystemUtilizationCPUWait_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 7),
    _SmSiaSystemUtilizationCPUWait_Type()
)
smSiaSystemUtilizationCPUWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUWait.setStatus("mandatory")
_SmSiaSystemUtilizationCPUBusy_Type = Integer32
_SmSiaSystemUtilizationCPUBusy_Object = MibTableColumn
smSiaSystemUtilizationCPUBusy = _SmSiaSystemUtilizationCPUBusy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 8),
    _SmSiaSystemUtilizationCPUBusy_Type()
)
smSiaSystemUtilizationCPUBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUBusy.setStatus("mandatory")
_SmSiaSystemUtilizationCPUUserMinimum_Type = Integer32
_SmSiaSystemUtilizationCPUUserMinimum_Object = MibTableColumn
smSiaSystemUtilizationCPUUserMinimum = _SmSiaSystemUtilizationCPUUserMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 9),
    _SmSiaSystemUtilizationCPUUserMinimum_Type()
)
smSiaSystemUtilizationCPUUserMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUUserMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUSystemMinimum_Type = Integer32
_SmSiaSystemUtilizationCPUSystemMinimum_Object = MibTableColumn
smSiaSystemUtilizationCPUSystemMinimum = _SmSiaSystemUtilizationCPUSystemMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 10),
    _SmSiaSystemUtilizationCPUSystemMinimum_Type()
)
smSiaSystemUtilizationCPUSystemMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUSystemMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUIdleMinimum_Type = Integer32
_SmSiaSystemUtilizationCPUIdleMinimum_Object = MibTableColumn
smSiaSystemUtilizationCPUIdleMinimum = _SmSiaSystemUtilizationCPUIdleMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 11),
    _SmSiaSystemUtilizationCPUIdleMinimum_Type()
)
smSiaSystemUtilizationCPUIdleMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUIdleMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUWaitMinimum_Type = Integer32
_SmSiaSystemUtilizationCPUWaitMinimum_Object = MibTableColumn
smSiaSystemUtilizationCPUWaitMinimum = _SmSiaSystemUtilizationCPUWaitMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 12),
    _SmSiaSystemUtilizationCPUWaitMinimum_Type()
)
smSiaSystemUtilizationCPUWaitMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUWaitMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUBusyMinimum_Type = Integer32
_SmSiaSystemUtilizationCPUBusyMinimum_Object = MibTableColumn
smSiaSystemUtilizationCPUBusyMinimum = _SmSiaSystemUtilizationCPUBusyMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 13),
    _SmSiaSystemUtilizationCPUBusyMinimum_Type()
)
smSiaSystemUtilizationCPUBusyMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUBusyMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUUserMaximum_Type = Integer32
_SmSiaSystemUtilizationCPUUserMaximum_Object = MibTableColumn
smSiaSystemUtilizationCPUUserMaximum = _SmSiaSystemUtilizationCPUUserMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 14),
    _SmSiaSystemUtilizationCPUUserMaximum_Type()
)
smSiaSystemUtilizationCPUUserMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUUserMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUSystemMaximum_Type = Integer32
_SmSiaSystemUtilizationCPUSystemMaximum_Object = MibTableColumn
smSiaSystemUtilizationCPUSystemMaximum = _SmSiaSystemUtilizationCPUSystemMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 15),
    _SmSiaSystemUtilizationCPUSystemMaximum_Type()
)
smSiaSystemUtilizationCPUSystemMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUSystemMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUIdleMaximum_Type = Integer32
_SmSiaSystemUtilizationCPUIdleMaximum_Object = MibTableColumn
smSiaSystemUtilizationCPUIdleMaximum = _SmSiaSystemUtilizationCPUIdleMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 16),
    _SmSiaSystemUtilizationCPUIdleMaximum_Type()
)
smSiaSystemUtilizationCPUIdleMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUIdleMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUWaitMaximum_Type = Integer32
_SmSiaSystemUtilizationCPUWaitMaximum_Object = MibTableColumn
smSiaSystemUtilizationCPUWaitMaximum = _SmSiaSystemUtilizationCPUWaitMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 17),
    _SmSiaSystemUtilizationCPUWaitMaximum_Type()
)
smSiaSystemUtilizationCPUWaitMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUWaitMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUBusyMaximum_Type = Integer32
_SmSiaSystemUtilizationCPUBusyMaximum_Object = MibTableColumn
smSiaSystemUtilizationCPUBusyMaximum = _SmSiaSystemUtilizationCPUBusyMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 18),
    _SmSiaSystemUtilizationCPUBusyMaximum_Type()
)
smSiaSystemUtilizationCPUBusyMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUBusyMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationCPUNumber_Type = Integer32
_SmSiaSystemUtilizationCPUNumber_Object = MibTableColumn
smSiaSystemUtilizationCPUNumber = _SmSiaSystemUtilizationCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 19),
    _SmSiaSystemUtilizationCPUNumber_Type()
)
smSiaSystemUtilizationCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationCPUNumber.setStatus("mandatory")
_SmSiaSystemUtilizationKernel_ObjectIdentity = ObjectIdentity
smSiaSystemUtilizationKernel = _SmSiaSystemUtilizationKernel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2)
)
_SmSiaSystemUtilizationKernelPollingInterval_Type = Integer32
_SmSiaSystemUtilizationKernelPollingInterval_Object = MibScalar
smSiaSystemUtilizationKernelPollingInterval = _SmSiaSystemUtilizationKernelPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 1),
    _SmSiaSystemUtilizationKernelPollingInterval_Type()
)
smSiaSystemUtilizationKernelPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelPollingInterval.setStatus("mandatory")
_SmSiaSystemUtilizationKernelTable_Object = MibTable
smSiaSystemUtilizationKernelTable = _SmSiaSystemUtilizationKernelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelTable.setStatus("mandatory")
_SmSiaSystemUtilizationKernelEntry_Object = MibTableRow
smSiaSystemUtilizationKernelEntry = _SmSiaSystemUtilizationKernelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1)
)
smSiaSystemUtilizationKernelEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemUtilizationKernelName"),
)
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelEntry.setStatus("mandatory")
_SmSiaSystemUtilizationKernelName_Type = DisplayString
_SmSiaSystemUtilizationKernelName_Object = MibTableColumn
smSiaSystemUtilizationKernelName = _SmSiaSystemUtilizationKernelName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 1),
    _SmSiaSystemUtilizationKernelName_Type()
)
smSiaSystemUtilizationKernelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelName.setStatus("mandatory")
_SmSiaSystemUtilizationKernelIntervalStartTime_Type = DisplayString
_SmSiaSystemUtilizationKernelIntervalStartTime_Object = MibTableColumn
smSiaSystemUtilizationKernelIntervalStartTime = _SmSiaSystemUtilizationKernelIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 2),
    _SmSiaSystemUtilizationKernelIntervalStartTime_Type()
)
smSiaSystemUtilizationKernelIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelIntervalStartTime.setStatus("mandatory")
_SmSiaSystemUtilizationKernelIntervalLength_Type = TimeTicks
_SmSiaSystemUtilizationKernelIntervalLength_Object = MibTableColumn
smSiaSystemUtilizationKernelIntervalLength = _SmSiaSystemUtilizationKernelIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 3),
    _SmSiaSystemUtilizationKernelIntervalLength_Type()
)
smSiaSystemUtilizationKernelIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelIntervalLength.setStatus("mandatory")
_SmSiaSystemUtilizationKernelContextSwitches_Type = Integer32
_SmSiaSystemUtilizationKernelContextSwitches_Object = MibTableColumn
smSiaSystemUtilizationKernelContextSwitches = _SmSiaSystemUtilizationKernelContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 4),
    _SmSiaSystemUtilizationKernelContextSwitches_Type()
)
smSiaSystemUtilizationKernelContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelContextSwitches.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemCalls_Type = Integer32
_SmSiaSystemUtilizationKernelSystemCalls_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemCalls = _SmSiaSystemUtilizationKernelSystemCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 5),
    _SmSiaSystemUtilizationKernelSystemCalls_Type()
)
smSiaSystemUtilizationKernelSystemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemCalls.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemReads_Type = Integer32
_SmSiaSystemUtilizationKernelSystemReads_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemReads = _SmSiaSystemUtilizationKernelSystemReads_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 6),
    _SmSiaSystemUtilizationKernelSystemReads_Type()
)
smSiaSystemUtilizationKernelSystemReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemReads.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemWrites_Type = Integer32
_SmSiaSystemUtilizationKernelSystemWrites_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemWrites = _SmSiaSystemUtilizationKernelSystemWrites_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 7),
    _SmSiaSystemUtilizationKernelSystemWrites_Type()
)
smSiaSystemUtilizationKernelSystemWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemWrites.setStatus("mandatory")
_SmSiaSystemUtilizationKernelForks_Type = Integer32
_SmSiaSystemUtilizationKernelForks_Object = MibTableColumn
smSiaSystemUtilizationKernelForks = _SmSiaSystemUtilizationKernelForks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 8),
    _SmSiaSystemUtilizationKernelForks_Type()
)
smSiaSystemUtilizationKernelForks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelForks.setStatus("mandatory")
_SmSiaSystemUtilizationKernelExecs_Type = Integer32
_SmSiaSystemUtilizationKernelExecs_Object = MibTableColumn
smSiaSystemUtilizationKernelExecs = _SmSiaSystemUtilizationKernelExecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 9),
    _SmSiaSystemUtilizationKernelExecs_Type()
)
smSiaSystemUtilizationKernelExecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelExecs.setStatus("mandatory")
_SmSiaSystemUtilizationKernelRunQueue_Type = Integer32
_SmSiaSystemUtilizationKernelRunQueue_Object = MibTableColumn
smSiaSystemUtilizationKernelRunQueue = _SmSiaSystemUtilizationKernelRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 10),
    _SmSiaSystemUtilizationKernelRunQueue_Type()
)
smSiaSystemUtilizationKernelRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelRunQueue.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSwapQueue_Type = Integer32
_SmSiaSystemUtilizationKernelSwapQueue_Object = MibTableColumn
smSiaSystemUtilizationKernelSwapQueue = _SmSiaSystemUtilizationKernelSwapQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 11),
    _SmSiaSystemUtilizationKernelSwapQueue_Type()
)
smSiaSystemUtilizationKernelSwapQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSwapQueue.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSemaphores_Type = Integer32
_SmSiaSystemUtilizationKernelSemaphores_Object = MibTableColumn
smSiaSystemUtilizationKernelSemaphores = _SmSiaSystemUtilizationKernelSemaphores_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 12),
    _SmSiaSystemUtilizationKernelSemaphores_Type()
)
smSiaSystemUtilizationKernelSemaphores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSemaphores.setStatus("mandatory")
_SmSiaSystemUtilizationKernelMessages_Type = Integer32
_SmSiaSystemUtilizationKernelMessages_Object = MibTableColumn
smSiaSystemUtilizationKernelMessages = _SmSiaSystemUtilizationKernelMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 13),
    _SmSiaSystemUtilizationKernelMessages_Type()
)
smSiaSystemUtilizationKernelMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelMessages.setStatus("mandatory")
_SmSiaSystemUtilizationKernelProcessOverflow_Type = Integer32
_SmSiaSystemUtilizationKernelProcessOverflow_Object = MibTableColumn
smSiaSystemUtilizationKernelProcessOverflow = _SmSiaSystemUtilizationKernelProcessOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 14),
    _SmSiaSystemUtilizationKernelProcessOverflow_Type()
)
smSiaSystemUtilizationKernelProcessOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelProcessOverflow.setStatus("mandatory")
_SmSiaSystemUtilizationKernelBytesRead_Type = Integer32
_SmSiaSystemUtilizationKernelBytesRead_Object = MibTableColumn
smSiaSystemUtilizationKernelBytesRead = _SmSiaSystemUtilizationKernelBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 15),
    _SmSiaSystemUtilizationKernelBytesRead_Type()
)
smSiaSystemUtilizationKernelBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelBytesRead.setStatus("mandatory")
_SmSiaSystemUtilizationKernelBytesWritten_Type = Integer32
_SmSiaSystemUtilizationKernelBytesWritten_Object = MibTableColumn
smSiaSystemUtilizationKernelBytesWritten = _SmSiaSystemUtilizationKernelBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 16),
    _SmSiaSystemUtilizationKernelBytesWritten_Type()
)
smSiaSystemUtilizationKernelBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelBytesWritten.setStatus("mandatory")
_SmSiaSystemUtilizationKernelRawTTYOut_Type = Integer32
_SmSiaSystemUtilizationKernelRawTTYOut_Object = MibTableColumn
smSiaSystemUtilizationKernelRawTTYOut = _SmSiaSystemUtilizationKernelRawTTYOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 17),
    _SmSiaSystemUtilizationKernelRawTTYOut_Type()
)
smSiaSystemUtilizationKernelRawTTYOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelRawTTYOut.setStatus("mandatory")
_SmSiaSystemUtilizationKernelContextSwitchesMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelContextSwitchesMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelContextSwitchesMinimum = _SmSiaSystemUtilizationKernelContextSwitchesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 18),
    _SmSiaSystemUtilizationKernelContextSwitchesMinimum_Type()
)
smSiaSystemUtilizationKernelContextSwitchesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelContextSwitchesMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemCallsMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelSystemCallsMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemCallsMinimum = _SmSiaSystemUtilizationKernelSystemCallsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 19),
    _SmSiaSystemUtilizationKernelSystemCallsMinimum_Type()
)
smSiaSystemUtilizationKernelSystemCallsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemCallsMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemReadsMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelSystemReadsMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemReadsMinimum = _SmSiaSystemUtilizationKernelSystemReadsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 20),
    _SmSiaSystemUtilizationKernelSystemReadsMinimum_Type()
)
smSiaSystemUtilizationKernelSystemReadsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemReadsMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemWritesMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelSystemWritesMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemWritesMinimum = _SmSiaSystemUtilizationKernelSystemWritesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 21),
    _SmSiaSystemUtilizationKernelSystemWritesMinimum_Type()
)
smSiaSystemUtilizationKernelSystemWritesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemWritesMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelForksMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelForksMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelForksMinimum = _SmSiaSystemUtilizationKernelForksMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 22),
    _SmSiaSystemUtilizationKernelForksMinimum_Type()
)
smSiaSystemUtilizationKernelForksMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelForksMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelExecsMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelExecsMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelExecsMinimum = _SmSiaSystemUtilizationKernelExecsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 23),
    _SmSiaSystemUtilizationKernelExecsMinimum_Type()
)
smSiaSystemUtilizationKernelExecsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelExecsMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelRunQueueMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelRunQueueMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelRunQueueMinimum = _SmSiaSystemUtilizationKernelRunQueueMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 24),
    _SmSiaSystemUtilizationKernelRunQueueMinimum_Type()
)
smSiaSystemUtilizationKernelRunQueueMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelRunQueueMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSwapQueueMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelSwapQueueMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelSwapQueueMinimum = _SmSiaSystemUtilizationKernelSwapQueueMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 25),
    _SmSiaSystemUtilizationKernelSwapQueueMinimum_Type()
)
smSiaSystemUtilizationKernelSwapQueueMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSwapQueueMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSemaphoresMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelSemaphoresMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelSemaphoresMinimum = _SmSiaSystemUtilizationKernelSemaphoresMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 26),
    _SmSiaSystemUtilizationKernelSemaphoresMinimum_Type()
)
smSiaSystemUtilizationKernelSemaphoresMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSemaphoresMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelMessagesMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelMessagesMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelMessagesMinimum = _SmSiaSystemUtilizationKernelMessagesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 27),
    _SmSiaSystemUtilizationKernelMessagesMinimum_Type()
)
smSiaSystemUtilizationKernelMessagesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelMessagesMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelProcessOverflowMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelProcessOverflowMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelProcessOverflowMinimum = _SmSiaSystemUtilizationKernelProcessOverflowMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 28),
    _SmSiaSystemUtilizationKernelProcessOverflowMinimum_Type()
)
smSiaSystemUtilizationKernelProcessOverflowMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelProcessOverflowMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelBytesReadMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelBytesReadMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelBytesReadMinimum = _SmSiaSystemUtilizationKernelBytesReadMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 29),
    _SmSiaSystemUtilizationKernelBytesReadMinimum_Type()
)
smSiaSystemUtilizationKernelBytesReadMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelBytesReadMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelBytesWrittenMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelBytesWrittenMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelBytesWrittenMinimum = _SmSiaSystemUtilizationKernelBytesWrittenMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 30),
    _SmSiaSystemUtilizationKernelBytesWrittenMinimum_Type()
)
smSiaSystemUtilizationKernelBytesWrittenMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelBytesWrittenMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelRawTTYOutMinimum_Type = Integer32
_SmSiaSystemUtilizationKernelRawTTYOutMinimum_Object = MibTableColumn
smSiaSystemUtilizationKernelRawTTYOutMinimum = _SmSiaSystemUtilizationKernelRawTTYOutMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 31),
    _SmSiaSystemUtilizationKernelRawTTYOutMinimum_Type()
)
smSiaSystemUtilizationKernelRawTTYOutMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelRawTTYOutMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelContextSwitchesMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelContextSwitchesMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelContextSwitchesMaximum = _SmSiaSystemUtilizationKernelContextSwitchesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 32),
    _SmSiaSystemUtilizationKernelContextSwitchesMaximum_Type()
)
smSiaSystemUtilizationKernelContextSwitchesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelContextSwitchesMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemCallsMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelSystemCallsMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemCallsMaximum = _SmSiaSystemUtilizationKernelSystemCallsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 33),
    _SmSiaSystemUtilizationKernelSystemCallsMaximum_Type()
)
smSiaSystemUtilizationKernelSystemCallsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemCallsMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemReadsMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelSystemReadsMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemReadsMaximum = _SmSiaSystemUtilizationKernelSystemReadsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 34),
    _SmSiaSystemUtilizationKernelSystemReadsMaximum_Type()
)
smSiaSystemUtilizationKernelSystemReadsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemReadsMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSystemWritesMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelSystemWritesMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelSystemWritesMaximum = _SmSiaSystemUtilizationKernelSystemWritesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 35),
    _SmSiaSystemUtilizationKernelSystemWritesMaximum_Type()
)
smSiaSystemUtilizationKernelSystemWritesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSystemWritesMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelForksMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelForksMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelForksMaximum = _SmSiaSystemUtilizationKernelForksMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 36),
    _SmSiaSystemUtilizationKernelForksMaximum_Type()
)
smSiaSystemUtilizationKernelForksMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelForksMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelExecsMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelExecsMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelExecsMaximum = _SmSiaSystemUtilizationKernelExecsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 37),
    _SmSiaSystemUtilizationKernelExecsMaximum_Type()
)
smSiaSystemUtilizationKernelExecsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelExecsMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelRunQueueMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelRunQueueMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelRunQueueMaximum = _SmSiaSystemUtilizationKernelRunQueueMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 38),
    _SmSiaSystemUtilizationKernelRunQueueMaximum_Type()
)
smSiaSystemUtilizationKernelRunQueueMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelRunQueueMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSwapQueueMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelSwapQueueMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelSwapQueueMaximum = _SmSiaSystemUtilizationKernelSwapQueueMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 39),
    _SmSiaSystemUtilizationKernelSwapQueueMaximum_Type()
)
smSiaSystemUtilizationKernelSwapQueueMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSwapQueueMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelSemaphoresMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelSemaphoresMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelSemaphoresMaximum = _SmSiaSystemUtilizationKernelSemaphoresMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 40),
    _SmSiaSystemUtilizationKernelSemaphoresMaximum_Type()
)
smSiaSystemUtilizationKernelSemaphoresMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelSemaphoresMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelMessagesMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelMessagesMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelMessagesMaximum = _SmSiaSystemUtilizationKernelMessagesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 41),
    _SmSiaSystemUtilizationKernelMessagesMaximum_Type()
)
smSiaSystemUtilizationKernelMessagesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelMessagesMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelProcessOverflowMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelProcessOverflowMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelProcessOverflowMaximum = _SmSiaSystemUtilizationKernelProcessOverflowMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 42),
    _SmSiaSystemUtilizationKernelProcessOverflowMaximum_Type()
)
smSiaSystemUtilizationKernelProcessOverflowMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelProcessOverflowMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelBytesReadMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelBytesReadMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelBytesReadMaximum = _SmSiaSystemUtilizationKernelBytesReadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 43),
    _SmSiaSystemUtilizationKernelBytesReadMaximum_Type()
)
smSiaSystemUtilizationKernelBytesReadMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelBytesReadMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelBytesWrittenMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelBytesWrittenMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelBytesWrittenMaximum = _SmSiaSystemUtilizationKernelBytesWrittenMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 44),
    _SmSiaSystemUtilizationKernelBytesWrittenMaximum_Type()
)
smSiaSystemUtilizationKernelBytesWrittenMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelBytesWrittenMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationKernelRawTTYOutMaximum_Type = Integer32
_SmSiaSystemUtilizationKernelRawTTYOutMaximum_Object = MibTableColumn
smSiaSystemUtilizationKernelRawTTYOutMaximum = _SmSiaSystemUtilizationKernelRawTTYOutMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 45),
    _SmSiaSystemUtilizationKernelRawTTYOutMaximum_Type()
)
smSiaSystemUtilizationKernelRawTTYOutMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationKernelRawTTYOutMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationIostat_ObjectIdentity = ObjectIdentity
smSiaSystemUtilizationIostat = _SmSiaSystemUtilizationIostat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3)
)
_SmSiaSystemUtilizationIostatPollingInterval_Type = Integer32
_SmSiaSystemUtilizationIostatPollingInterval_Object = MibScalar
smSiaSystemUtilizationIostatPollingInterval = _SmSiaSystemUtilizationIostatPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 1),
    _SmSiaSystemUtilizationIostatPollingInterval_Type()
)
smSiaSystemUtilizationIostatPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatPollingInterval.setStatus("mandatory")
_SmSiaSystemUtilizationIostatTable_Object = MibTable
smSiaSystemUtilizationIostatTable = _SmSiaSystemUtilizationIostatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatTable.setStatus("mandatory")
_SmSiaSystemUtilizationIostatEntry_Object = MibTableRow
smSiaSystemUtilizationIostatEntry = _SmSiaSystemUtilizationIostatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1)
)
smSiaSystemUtilizationIostatEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaSystemUtilizationIostatName"),
)
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatEntry.setStatus("mandatory")
_SmSiaSystemUtilizationIostatName_Type = DisplayString
_SmSiaSystemUtilizationIostatName_Object = MibTableColumn
smSiaSystemUtilizationIostatName = _SmSiaSystemUtilizationIostatName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 1),
    _SmSiaSystemUtilizationIostatName_Type()
)
smSiaSystemUtilizationIostatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatName.setStatus("mandatory")
_SmSiaSystemUtilizationIostatIntervalStartTime_Type = DisplayString
_SmSiaSystemUtilizationIostatIntervalStartTime_Object = MibTableColumn
smSiaSystemUtilizationIostatIntervalStartTime = _SmSiaSystemUtilizationIostatIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 2),
    _SmSiaSystemUtilizationIostatIntervalStartTime_Type()
)
smSiaSystemUtilizationIostatIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatIntervalStartTime.setStatus("mandatory")
_SmSiaSystemUtilizationIostatIntervalLength_Type = TimeTicks
_SmSiaSystemUtilizationIostatIntervalLength_Object = MibTableColumn
smSiaSystemUtilizationIostatIntervalLength = _SmSiaSystemUtilizationIostatIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 3),
    _SmSiaSystemUtilizationIostatIntervalLength_Type()
)
smSiaSystemUtilizationIostatIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatIntervalLength.setStatus("mandatory")
_SmSiaSystemUtilizationIostatPercentTimeActive_Type = Integer32
_SmSiaSystemUtilizationIostatPercentTimeActive_Object = MibTableColumn
smSiaSystemUtilizationIostatPercentTimeActive = _SmSiaSystemUtilizationIostatPercentTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 4),
    _SmSiaSystemUtilizationIostatPercentTimeActive_Type()
)
smSiaSystemUtilizationIostatPercentTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatPercentTimeActive.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesTransferRate_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesTransferRate_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesTransferRate = _SmSiaSystemUtilizationIostatKilobytesTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 5),
    _SmSiaSystemUtilizationIostatKilobytesTransferRate_Type()
)
smSiaSystemUtilizationIostatKilobytesTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesTransferRate.setStatus("mandatory")
_SmSiaSystemUtilizationIostatTransfers_Type = Integer32
_SmSiaSystemUtilizationIostatTransfers_Object = MibTableColumn
smSiaSystemUtilizationIostatTransfers = _SmSiaSystemUtilizationIostatTransfers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 6),
    _SmSiaSystemUtilizationIostatTransfers_Type()
)
smSiaSystemUtilizationIostatTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatTransfers.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesRead_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesRead_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesRead = _SmSiaSystemUtilizationIostatKilobytesRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 7),
    _SmSiaSystemUtilizationIostatKilobytesRead_Type()
)
smSiaSystemUtilizationIostatKilobytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesRead.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesWritten_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesWritten_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesWritten = _SmSiaSystemUtilizationIostatKilobytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 8),
    _SmSiaSystemUtilizationIostatKilobytesWritten_Type()
)
smSiaSystemUtilizationIostatKilobytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesWritten.setStatus("mandatory")
_SmSiaSystemUtilizationIostatPercentTimeActiveMinimum_Type = Integer32
_SmSiaSystemUtilizationIostatPercentTimeActiveMinimum_Object = MibTableColumn
smSiaSystemUtilizationIostatPercentTimeActiveMinimum = _SmSiaSystemUtilizationIostatPercentTimeActiveMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 9),
    _SmSiaSystemUtilizationIostatPercentTimeActiveMinimum_Type()
)
smSiaSystemUtilizationIostatPercentTimeActiveMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatPercentTimeActiveMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesTransferRateMinimum_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesTransferRateMinimum_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesTransferRateMinimum = _SmSiaSystemUtilizationIostatKilobytesTransferRateMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 10),
    _SmSiaSystemUtilizationIostatKilobytesTransferRateMinimum_Type()
)
smSiaSystemUtilizationIostatKilobytesTransferRateMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesTransferRateMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatTransfersMinimum_Type = Integer32
_SmSiaSystemUtilizationIostatTransfersMinimum_Object = MibTableColumn
smSiaSystemUtilizationIostatTransfersMinimum = _SmSiaSystemUtilizationIostatTransfersMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 11),
    _SmSiaSystemUtilizationIostatTransfersMinimum_Type()
)
smSiaSystemUtilizationIostatTransfersMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatTransfersMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesReadMinimum_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesReadMinimum_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesReadMinimum = _SmSiaSystemUtilizationIostatKilobytesReadMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 12),
    _SmSiaSystemUtilizationIostatKilobytesReadMinimum_Type()
)
smSiaSystemUtilizationIostatKilobytesReadMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesReadMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesWrittenMinimum_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesWrittenMinimum_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesWrittenMinimum = _SmSiaSystemUtilizationIostatKilobytesWrittenMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 13),
    _SmSiaSystemUtilizationIostatKilobytesWrittenMinimum_Type()
)
smSiaSystemUtilizationIostatKilobytesWrittenMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesWrittenMinimum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatPercentTimeActiveMaximum_Type = Integer32
_SmSiaSystemUtilizationIostatPercentTimeActiveMaximum_Object = MibTableColumn
smSiaSystemUtilizationIostatPercentTimeActiveMaximum = _SmSiaSystemUtilizationIostatPercentTimeActiveMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 14),
    _SmSiaSystemUtilizationIostatPercentTimeActiveMaximum_Type()
)
smSiaSystemUtilizationIostatPercentTimeActiveMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatPercentTimeActiveMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesTransferRateMaximum_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesTransferRateMaximum_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesTransferRateMaximum = _SmSiaSystemUtilizationIostatKilobytesTransferRateMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 15),
    _SmSiaSystemUtilizationIostatKilobytesTransferRateMaximum_Type()
)
smSiaSystemUtilizationIostatKilobytesTransferRateMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesTransferRateMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatTransfersMaximum_Type = Integer32
_SmSiaSystemUtilizationIostatTransfersMaximum_Object = MibTableColumn
smSiaSystemUtilizationIostatTransfersMaximum = _SmSiaSystemUtilizationIostatTransfersMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 16),
    _SmSiaSystemUtilizationIostatTransfersMaximum_Type()
)
smSiaSystemUtilizationIostatTransfersMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatTransfersMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesReadMaximum_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesReadMaximum_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesReadMaximum = _SmSiaSystemUtilizationIostatKilobytesReadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 17),
    _SmSiaSystemUtilizationIostatKilobytesReadMaximum_Type()
)
smSiaSystemUtilizationIostatKilobytesReadMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesReadMaximum.setStatus("mandatory")
_SmSiaSystemUtilizationIostatKilobytesWrittenMaximum_Type = Integer32
_SmSiaSystemUtilizationIostatKilobytesWrittenMaximum_Object = MibTableColumn
smSiaSystemUtilizationIostatKilobytesWrittenMaximum = _SmSiaSystemUtilizationIostatKilobytesWrittenMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 18),
    _SmSiaSystemUtilizationIostatKilobytesWrittenMaximum_Type()
)
smSiaSystemUtilizationIostatKilobytesWrittenMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemUtilizationIostatKilobytesWrittenMaximum.setStatus("mandatory")
_SmSiaSystemMiscellaneous_ObjectIdentity = ObjectIdentity
smSiaSystemMiscellaneous = _SmSiaSystemMiscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11)
)
_SmSiaSystemMiscellaneousTimeText_Type = DisplayString
_SmSiaSystemMiscellaneousTimeText_Object = MibScalar
smSiaSystemMiscellaneousTimeText = _SmSiaSystemMiscellaneousTimeText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 1),
    _SmSiaSystemMiscellaneousTimeText_Type()
)
smSiaSystemMiscellaneousTimeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMiscellaneousTimeText.setStatus("mandatory")
_SmSiaSystemMiscellaneousTime_Type = Counter32
_SmSiaSystemMiscellaneousTime_Object = MibScalar
smSiaSystemMiscellaneousTime = _SmSiaSystemMiscellaneousTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 2),
    _SmSiaSystemMiscellaneousTime_Type()
)
smSiaSystemMiscellaneousTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMiscellaneousTime.setStatus("mandatory")
_SmSiaSystemMiscellaneousRandom_Type = Integer32
_SmSiaSystemMiscellaneousRandom_Object = MibScalar
smSiaSystemMiscellaneousRandom = _SmSiaSystemMiscellaneousRandom_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 3),
    _SmSiaSystemMiscellaneousRandom_Type()
)
smSiaSystemMiscellaneousRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMiscellaneousRandom.setStatus("mandatory")
_SmSiaSystemMiscellaneousFreeSpace_Type = Integer32
_SmSiaSystemMiscellaneousFreeSpace_Object = MibScalar
smSiaSystemMiscellaneousFreeSpace = _SmSiaSystemMiscellaneousFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 4),
    _SmSiaSystemMiscellaneousFreeSpace_Type()
)
smSiaSystemMiscellaneousFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMiscellaneousFreeSpace.setStatus("mandatory")
_SmSiaSystemMiscellaneousPublicKey_Type = DisplayString
_SmSiaSystemMiscellaneousPublicKey_Object = MibScalar
smSiaSystemMiscellaneousPublicKey = _SmSiaSystemMiscellaneousPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 5),
    _SmSiaSystemMiscellaneousPublicKey_Type()
)
smSiaSystemMiscellaneousPublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaSystemMiscellaneousPublicKey.setStatus("mandatory")
_SmSiaSystemMiscellaneousLocalSocket_Type = Integer32
_SmSiaSystemMiscellaneousLocalSocket_Object = MibScalar
smSiaSystemMiscellaneousLocalSocket = _SmSiaSystemMiscellaneousLocalSocket_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 6),
    _SmSiaSystemMiscellaneousLocalSocket_Type()
)
smSiaSystemMiscellaneousLocalSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaSystemMiscellaneousLocalSocket.setStatus("mandatory")
_SmSiaCommand_ObjectIdentity = ObjectIdentity
smSiaCommand = _SmSiaCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4)
)
_SmSiaCommandTable_Object = MibTable
smSiaCommandTable = _SmSiaCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1)
)
if mibBuilder.loadTexts:
    smSiaCommandTable.setStatus("mandatory")
_SmSiaCommandEntry_Object = MibTableRow
smSiaCommandEntry = _SmSiaCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1)
)
smSiaCommandEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaCommandName"),
)
if mibBuilder.loadTexts:
    smSiaCommandEntry.setStatus("mandatory")


class _SmSiaCommandState_Type(Integer32):
    """Custom type smSiaCommandState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 3),
          ("invalid", 2))
    )


_SmSiaCommandState_Type.__name__ = "Integer32"
_SmSiaCommandState_Object = MibTableColumn
smSiaCommandState = _SmSiaCommandState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 1),
    _SmSiaCommandState_Type()
)
smSiaCommandState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandState.setStatus("mandatory")
_SmSiaCommandName_Type = DisplayString
_SmSiaCommandName_Object = MibTableColumn
smSiaCommandName = _SmSiaCommandName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 2),
    _SmSiaCommandName_Type()
)
smSiaCommandName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandName.setStatus("mandatory")
_SmSiaCommandDescription_Type = DisplayString
_SmSiaCommandDescription_Object = MibTableColumn
smSiaCommandDescription = _SmSiaCommandDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 3),
    _SmSiaCommandDescription_Type()
)
smSiaCommandDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandDescription.setStatus("mandatory")
_SmSiaCommandOwnerID_Type = DisplayString
_SmSiaCommandOwnerID_Object = MibTableColumn
smSiaCommandOwnerID = _SmSiaCommandOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 4),
    _SmSiaCommandOwnerID_Type()
)
smSiaCommandOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandOwnerID.setStatus("mandatory")
_SmSiaCommandGetStringAndParameters_Type = DisplayString
_SmSiaCommandGetStringAndParameters_Object = MibTableColumn
smSiaCommandGetStringAndParameters = _SmSiaCommandGetStringAndParameters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 5),
    _SmSiaCommandGetStringAndParameters_Type()
)
smSiaCommandGetStringAndParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandGetStringAndParameters.setStatus("mandatory")
_SmSiaCommandSetStringAndParameters_Type = DisplayString
_SmSiaCommandSetStringAndParameters_Object = MibTableColumn
smSiaCommandSetStringAndParameters = _SmSiaCommandSetStringAndParameters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 6),
    _SmSiaCommandSetStringAndParameters_Type()
)
smSiaCommandSetStringAndParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandSetStringAndParameters.setStatus("mandatory")


class _SmSiaCommandTimeOutValue_Type(Integer32):
    """Custom type smSiaCommandTimeOutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaCommandTimeOutValue_Type.__name__ = "Integer32"
_SmSiaCommandTimeOutValue_Object = MibTableColumn
smSiaCommandTimeOutValue = _SmSiaCommandTimeOutValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 7),
    _SmSiaCommandTimeOutValue_Type()
)
smSiaCommandTimeOutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandTimeOutValue.setStatus("mandatory")


class _SmSiaCommandCountToLive_Type(Integer32):
    """Custom type smSiaCommandCountToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaCommandCountToLive_Type.__name__ = "Integer32"
_SmSiaCommandCountToLive_Object = MibTableColumn
smSiaCommandCountToLive = _SmSiaCommandCountToLive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 8),
    _SmSiaCommandCountToLive_Type()
)
smSiaCommandCountToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaCommandCountToLive.setStatus("mandatory")


class _SmSiaCommandTimeToLive_Type(Integer32):
    """Custom type smSiaCommandTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaCommandTimeToLive_Type.__name__ = "Integer32"
_SmSiaCommandTimeToLive_Object = MibTableColumn
smSiaCommandTimeToLive = _SmSiaCommandTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 9),
    _SmSiaCommandTimeToLive_Type()
)
smSiaCommandTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandTimeToLive.setStatus("mandatory")


class _SmSiaCommandOutputResultIndex_Type(Integer32):
    """Custom type smSiaCommandOutputResultIndex based on Integer32"""
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
        *(("counter", 3),
          ("displaystring", 1),
          ("gauge", 4),
          ("integer", 2))
    )


_SmSiaCommandOutputResultIndex_Type.__name__ = "Integer32"
_SmSiaCommandOutputResultIndex_Object = MibTableColumn
smSiaCommandOutputResultIndex = _SmSiaCommandOutputResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 10),
    _SmSiaCommandOutputResultIndex_Type()
)
smSiaCommandOutputResultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandOutputResultIndex.setStatus("mandatory")


class _SmSiaCommandOutputRowIndex_Type(Integer32):
    """Custom type smSiaCommandOutputRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaCommandOutputRowIndex_Type.__name__ = "Integer32"
_SmSiaCommandOutputRowIndex_Object = MibTableColumn
smSiaCommandOutputRowIndex = _SmSiaCommandOutputRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 11),
    _SmSiaCommandOutputRowIndex_Type()
)
smSiaCommandOutputRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandOutputRowIndex.setStatus("mandatory")


class _SmSiaCommandOutputColumnIndex_Type(Integer32):
    """Custom type smSiaCommandOutputColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaCommandOutputColumnIndex_Type.__name__ = "Integer32"
_SmSiaCommandOutputColumnIndex_Object = MibTableColumn
smSiaCommandOutputColumnIndex = _SmSiaCommandOutputColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 12),
    _SmSiaCommandOutputColumnIndex_Type()
)
smSiaCommandOutputColumnIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandOutputColumnIndex.setStatus("mandatory")
_SmSiaCommandDisplayStringResult_Type = DisplayString
_SmSiaCommandDisplayStringResult_Object = MibTableColumn
smSiaCommandDisplayStringResult = _SmSiaCommandDisplayStringResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 13),
    _SmSiaCommandDisplayStringResult_Type()
)
smSiaCommandDisplayStringResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandDisplayStringResult.setStatus("mandatory")
_SmSiaCommandIntegerResult_Type = Integer32
_SmSiaCommandIntegerResult_Object = MibTableColumn
smSiaCommandIntegerResult = _SmSiaCommandIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 14),
    _SmSiaCommandIntegerResult_Type()
)
smSiaCommandIntegerResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandIntegerResult.setStatus("mandatory")
_SmSiaCommandCounterResult_Type = Counter32
_SmSiaCommandCounterResult_Object = MibTableColumn
smSiaCommandCounterResult = _SmSiaCommandCounterResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 15),
    _SmSiaCommandCounterResult_Type()
)
smSiaCommandCounterResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandCounterResult.setStatus("mandatory")
_SmSiaCommandGaugeResult_Type = Gauge32
_SmSiaCommandGaugeResult_Object = MibTableColumn
smSiaCommandGaugeResult = _SmSiaCommandGaugeResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 16),
    _SmSiaCommandGaugeResult_Type()
)
smSiaCommandGaugeResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaCommandGaugeResult.setStatus("mandatory")
_SmSiaCommandExecutionReturnCode_Type = Integer32
_SmSiaCommandExecutionReturnCode_Object = MibTableColumn
smSiaCommandExecutionReturnCode = _SmSiaCommandExecutionReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 17),
    _SmSiaCommandExecutionReturnCode_Type()
)
smSiaCommandExecutionReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaCommandExecutionReturnCode.setStatus("mandatory")
_SmSiaCommandStandardError_Type = DisplayString
_SmSiaCommandStandardError_Object = MibTableColumn
smSiaCommandStandardError = _SmSiaCommandStandardError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 18),
    _SmSiaCommandStandardError_Type()
)
smSiaCommandStandardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaCommandStandardError.setStatus("mandatory")
_SmSiaAdministration_ObjectIdentity = ObjectIdentity
smSiaAdministration = _SmSiaAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20)
)
_SmSiaAdministrationTable_Object = MibTable
smSiaAdministrationTable = _SmSiaAdministrationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1)
)
if mibBuilder.loadTexts:
    smSiaAdministrationTable.setStatus("mandatory")
_SmSiaAdministrationEntry_Object = MibTableRow
smSiaAdministrationEntry = _SmSiaAdministrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1, 1)
)
smSiaAdministrationEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaAdministrationFieldName"),
)
if mibBuilder.loadTexts:
    smSiaAdministrationEntry.setStatus("mandatory")


class _SmSiaAdministrationFieldState_Type(Integer32):
    """Custom type smSiaAdministrationFieldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("outDated", 3),
          ("valid", 1))
    )


_SmSiaAdministrationFieldState_Type.__name__ = "Integer32"
_SmSiaAdministrationFieldState_Object = MibTableColumn
smSiaAdministrationFieldState = _SmSiaAdministrationFieldState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1, 1, 1),
    _SmSiaAdministrationFieldState_Type()
)
smSiaAdministrationFieldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaAdministrationFieldState.setStatus("mandatory")
_SmSiaAdministrationFieldName_Type = DisplayString
_SmSiaAdministrationFieldName_Object = MibTableColumn
smSiaAdministrationFieldName = _SmSiaAdministrationFieldName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1, 1, 2),
    _SmSiaAdministrationFieldName_Type()
)
smSiaAdministrationFieldName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaAdministrationFieldName.setStatus("mandatory")
_SmSiaAdministrationFieldOwner_Type = DisplayString
_SmSiaAdministrationFieldOwner_Object = MibTableColumn
smSiaAdministrationFieldOwner = _SmSiaAdministrationFieldOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1, 1, 3),
    _SmSiaAdministrationFieldOwner_Type()
)
smSiaAdministrationFieldOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaAdministrationFieldOwner.setStatus("mandatory")
_SmSiaAdministrationFieldDescription_Type = DisplayString
_SmSiaAdministrationFieldDescription_Object = MibTableColumn
smSiaAdministrationFieldDescription = _SmSiaAdministrationFieldDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1, 1, 4),
    _SmSiaAdministrationFieldDescription_Type()
)
smSiaAdministrationFieldDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaAdministrationFieldDescription.setStatus("mandatory")
_SmSiaAdministrationFieldValue_Type = DisplayString
_SmSiaAdministrationFieldValue_Object = MibTableColumn
smSiaAdministrationFieldValue = _SmSiaAdministrationFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 20, 1, 1, 5),
    _SmSiaAdministrationFieldValue_Type()
)
smSiaAdministrationFieldValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaAdministrationFieldValue.setStatus("mandatory")
_SmSiaFileMonitor_ObjectIdentity = ObjectIdentity
smSiaFileMonitor = _SmSiaFileMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21)
)
_SmSiaFileMonitorTable_Object = MibTable
smSiaFileMonitorTable = _SmSiaFileMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1)
)
if mibBuilder.loadTexts:
    smSiaFileMonitorTable.setStatus("mandatory")
_SmSiaFileMonitorEntry_Object = MibTableRow
smSiaFileMonitorEntry = _SmSiaFileMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1)
)
smSiaFileMonitorEntry.setIndexNames(
    (0, "SYSINFO-MIB", "smSiaFileMonitorName"),
)
if mibBuilder.loadTexts:
    smSiaFileMonitorEntry.setStatus("mandatory")


class _SmSiaFileMonitorState_Type(Integer32):
    """Custom type smSiaFileMonitorState based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 3),
          ("enabledFromBegin", 4),
          ("invalid", 2))
    )


_SmSiaFileMonitorState_Type.__name__ = "Integer32"
_SmSiaFileMonitorState_Object = MibTableColumn
smSiaFileMonitorState = _SmSiaFileMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 1),
    _SmSiaFileMonitorState_Type()
)
smSiaFileMonitorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorState.setStatus("mandatory")
_SmSiaFileMonitorName_Type = DisplayString
_SmSiaFileMonitorName_Object = MibTableColumn
smSiaFileMonitorName = _SmSiaFileMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 2),
    _SmSiaFileMonitorName_Type()
)
smSiaFileMonitorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorName.setStatus("mandatory")


class _SmSiaFileMonitorType_Type(Integer32):
    """Custom type smSiaFileMonitorType based on Integer32"""
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
        *(("all", 7),
          ("dataChange", 2),
          ("exist", 6),
          ("notExist", 5),
          ("notString", 8),
          ("statusChange", 3),
          ("strDataStatus", 4),
          ("string", 1))
    )


_SmSiaFileMonitorType_Type.__name__ = "Integer32"
_SmSiaFileMonitorType_Object = MibTableColumn
smSiaFileMonitorType = _SmSiaFileMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 3),
    _SmSiaFileMonitorType_Type()
)
smSiaFileMonitorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorType.setStatus("mandatory")


class _SmSiaFileMonitorTrapState_Type(Integer32):
    """Custom type smSiaFileMonitorTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSend", 2),
          ("send", 1))
    )


_SmSiaFileMonitorTrapState_Type.__name__ = "Integer32"
_SmSiaFileMonitorTrapState_Object = MibTableColumn
smSiaFileMonitorTrapState = _SmSiaFileMonitorTrapState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 4),
    _SmSiaFileMonitorTrapState_Type()
)
smSiaFileMonitorTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorTrapState.setStatus("mandatory")


class _SmSiaFileMonitorCaseState_Type(Integer32):
    """Custom type smSiaFileMonitorCaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("case", 1),
          ("ignoreCase", 2))
    )


_SmSiaFileMonitorCaseState_Type.__name__ = "Integer32"
_SmSiaFileMonitorCaseState_Object = MibTableColumn
smSiaFileMonitorCaseState = _SmSiaFileMonitorCaseState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 5),
    _SmSiaFileMonitorCaseState_Type()
)
smSiaFileMonitorCaseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorCaseState.setStatus("mandatory")
_SmSiaFileMonitorDescription_Type = DisplayString
_SmSiaFileMonitorDescription_Object = MibTableColumn
smSiaFileMonitorDescription = _SmSiaFileMonitorDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 6),
    _SmSiaFileMonitorDescription_Type()
)
smSiaFileMonitorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorDescription.setStatus("mandatory")
_SmSiaFileMonitorOwnerID_Type = DisplayString
_SmSiaFileMonitorOwnerID_Object = MibTableColumn
smSiaFileMonitorOwnerID = _SmSiaFileMonitorOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 7),
    _SmSiaFileMonitorOwnerID_Type()
)
smSiaFileMonitorOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorOwnerID.setStatus("mandatory")
_SmSiaFileMonitorFullPathName_Type = DisplayString
_SmSiaFileMonitorFullPathName_Object = MibTableColumn
smSiaFileMonitorFullPathName = _SmSiaFileMonitorFullPathName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 8),
    _SmSiaFileMonitorFullPathName_Type()
)
smSiaFileMonitorFullPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorFullPathName.setStatus("mandatory")
_SmSiaFileMonitorForString_Type = DisplayString
_SmSiaFileMonitorForString_Object = MibTableColumn
smSiaFileMonitorForString = _SmSiaFileMonitorForString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 9),
    _SmSiaFileMonitorForString_Type()
)
smSiaFileMonitorForString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorForString.setStatus("mandatory")


class _SmSiaFileMonitorActivationState_Type(Integer32):
    """Custom type smSiaFileMonitorActivationState based on Integer32"""
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
          ("inactive", 3),
          ("notEnabled", 1))
    )


_SmSiaFileMonitorActivationState_Type.__name__ = "Integer32"
_SmSiaFileMonitorActivationState_Object = MibTableColumn
smSiaFileMonitorActivationState = _SmSiaFileMonitorActivationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 10),
    _SmSiaFileMonitorActivationState_Type()
)
smSiaFileMonitorActivationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorActivationState.setStatus("mandatory")
_SmSiaFileMonitorActivationTime_Type = DisplayString
_SmSiaFileMonitorActivationTime_Object = MibTableColumn
smSiaFileMonitorActivationTime = _SmSiaFileMonitorActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 11),
    _SmSiaFileMonitorActivationTime_Type()
)
smSiaFileMonitorActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorActivationTime.setStatus("mandatory")
_SmSiaFileMonitorActivationDayOfWeek_Type = DisplayString
_SmSiaFileMonitorActivationDayOfWeek_Object = MibTableColumn
smSiaFileMonitorActivationDayOfWeek = _SmSiaFileMonitorActivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 12),
    _SmSiaFileMonitorActivationDayOfWeek_Type()
)
smSiaFileMonitorActivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorActivationDayOfWeek.setStatus("mandatory")
_SmSiaFileMonitorDeactivationTime_Type = DisplayString
_SmSiaFileMonitorDeactivationTime_Object = MibTableColumn
smSiaFileMonitorDeactivationTime = _SmSiaFileMonitorDeactivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 13),
    _SmSiaFileMonitorDeactivationTime_Type()
)
smSiaFileMonitorDeactivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorDeactivationTime.setStatus("mandatory")
_SmSiaFileMonitorDeactivationDayOfWeek_Type = DisplayString
_SmSiaFileMonitorDeactivationDayOfWeek_Object = MibTableColumn
smSiaFileMonitorDeactivationDayOfWeek = _SmSiaFileMonitorDeactivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 14),
    _SmSiaFileMonitorDeactivationDayOfWeek_Type()
)
smSiaFileMonitorDeactivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorDeactivationDayOfWeek.setStatus("mandatory")
_SmSiaFileMonitorPollTime_Type = DisplayString
_SmSiaFileMonitorPollTime_Object = MibTableColumn
smSiaFileMonitorPollTime = _SmSiaFileMonitorPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 15),
    _SmSiaFileMonitorPollTime_Type()
)
smSiaFileMonitorPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorPollTime.setStatus("mandatory")


class _SmSiaFileMonitorResetToStartOfFile_Type(Integer32):
    """Custom type smSiaFileMonitorResetToStartOfFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SmSiaFileMonitorResetToStartOfFile_Type.__name__ = "Integer32"
_SmSiaFileMonitorResetToStartOfFile_Object = MibTableColumn
smSiaFileMonitorResetToStartOfFile = _SmSiaFileMonitorResetToStartOfFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 16),
    _SmSiaFileMonitorResetToStartOfFile_Type()
)
smSiaFileMonitorResetToStartOfFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorResetToStartOfFile.setStatus("mandatory")


class _SmSiaFileMonitorCurrentLineCountOfFile_Type(Integer32):
    """Custom type smSiaFileMonitorCurrentLineCountOfFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaFileMonitorCurrentLineCountOfFile_Type.__name__ = "Integer32"
_SmSiaFileMonitorCurrentLineCountOfFile_Object = MibTableColumn
smSiaFileMonitorCurrentLineCountOfFile = _SmSiaFileMonitorCurrentLineCountOfFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 17),
    _SmSiaFileMonitorCurrentLineCountOfFile_Type()
)
smSiaFileMonitorCurrentLineCountOfFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorCurrentLineCountOfFile.setStatus("mandatory")


class _SmSiaFileMonitorFoundStringCount_Type(Integer32):
    """Custom type smSiaFileMonitorFoundStringCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaFileMonitorFoundStringCount_Type.__name__ = "Integer32"
_SmSiaFileMonitorFoundStringCount_Object = MibTableColumn
smSiaFileMonitorFoundStringCount = _SmSiaFileMonitorFoundStringCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 18),
    _SmSiaFileMonitorFoundStringCount_Type()
)
smSiaFileMonitorFoundStringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorFoundStringCount.setStatus("mandatory")
_SmSiaFileMonitorStringFound_Type = DisplayString
_SmSiaFileMonitorStringFound_Object = MibTableColumn
smSiaFileMonitorStringFound = _SmSiaFileMonitorStringFound_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 19),
    _SmSiaFileMonitorStringFound_Type()
)
smSiaFileMonitorStringFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorStringFound.setStatus("mandatory")


class _SmSiaFileMonitorFoundStringAtLineNumber_Type(Integer32):
    """Custom type smSiaFileMonitorFoundStringAtLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaFileMonitorFoundStringAtLineNumber_Type.__name__ = "Integer32"
_SmSiaFileMonitorFoundStringAtLineNumber_Object = MibTableColumn
smSiaFileMonitorFoundStringAtLineNumber = _SmSiaFileMonitorFoundStringAtLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 20),
    _SmSiaFileMonitorFoundStringAtLineNumber_Type()
)
smSiaFileMonitorFoundStringAtLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorFoundStringAtLineNumber.setStatus("mandatory")


class _SmSiaFileMonitorBytePositionWithinLine_Type(Integer32):
    """Custom type smSiaFileMonitorBytePositionWithinLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaFileMonitorBytePositionWithinLine_Type.__name__ = "Integer32"
_SmSiaFileMonitorBytePositionWithinLine_Object = MibTableColumn
smSiaFileMonitorBytePositionWithinLine = _SmSiaFileMonitorBytePositionWithinLine_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 21),
    _SmSiaFileMonitorBytePositionWithinLine_Type()
)
smSiaFileMonitorBytePositionWithinLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorBytePositionWithinLine.setStatus("mandatory")
_SmSiaFileMonitorCompleteLineStringFound_Type = DisplayString
_SmSiaFileMonitorCompleteLineStringFound_Object = MibTableColumn
smSiaFileMonitorCompleteLineStringFound = _SmSiaFileMonitorCompleteLineStringFound_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 22),
    _SmSiaFileMonitorCompleteLineStringFound_Type()
)
smSiaFileMonitorCompleteLineStringFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorCompleteLineStringFound.setStatus("mandatory")


class _SmSiaFileMonitorFoundStringBytePositionWithinFile_Type(Integer32):
    """Custom type smSiaFileMonitorFoundStringBytePositionWithinFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaFileMonitorFoundStringBytePositionWithinFile_Type.__name__ = "Integer32"
_SmSiaFileMonitorFoundStringBytePositionWithinFile_Object = MibTableColumn
smSiaFileMonitorFoundStringBytePositionWithinFile = _SmSiaFileMonitorFoundStringBytePositionWithinFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 23),
    _SmSiaFileMonitorFoundStringBytePositionWithinFile_Type()
)
smSiaFileMonitorFoundStringBytePositionWithinFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorFoundStringBytePositionWithinFile.setStatus("mandatory")
_SmSiaFileMonitorTimeLastFound_Type = DisplayString
_SmSiaFileMonitorTimeLastFound_Object = MibTableColumn
smSiaFileMonitorTimeLastFound = _SmSiaFileMonitorTimeLastFound_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 24),
    _SmSiaFileMonitorTimeLastFound_Type()
)
smSiaFileMonitorTimeLastFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorTimeLastFound.setStatus("mandatory")
_SmSiaFileMonitorCommandToExecuteTypeMet_Type = DisplayString
_SmSiaFileMonitorCommandToExecuteTypeMet_Object = MibTableColumn
smSiaFileMonitorCommandToExecuteTypeMet = _SmSiaFileMonitorCommandToExecuteTypeMet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 25),
    _SmSiaFileMonitorCommandToExecuteTypeMet_Type()
)
smSiaFileMonitorCommandToExecuteTypeMet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorCommandToExecuteTypeMet.setStatus("mandatory")
_SmSiaFileMonitorCommandToExecuteBeforeMonitor_Type = DisplayString
_SmSiaFileMonitorCommandToExecuteBeforeMonitor_Object = MibTableColumn
smSiaFileMonitorCommandToExecuteBeforeMonitor = _SmSiaFileMonitorCommandToExecuteBeforeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 26),
    _SmSiaFileMonitorCommandToExecuteBeforeMonitor_Type()
)
smSiaFileMonitorCommandToExecuteBeforeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorCommandToExecuteBeforeMonitor.setStatus("mandatory")
_SmSiaFileMonitorMode_Type = DisplayString
_SmSiaFileMonitorMode_Object = MibTableColumn
smSiaFileMonitorMode = _SmSiaFileMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 27),
    _SmSiaFileMonitorMode_Type()
)
smSiaFileMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorMode.setStatus("mandatory")
_SmSiaFileMonitorUserID_Type = DisplayString
_SmSiaFileMonitorUserID_Object = MibTableColumn
smSiaFileMonitorUserID = _SmSiaFileMonitorUserID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 28),
    _SmSiaFileMonitorUserID_Type()
)
smSiaFileMonitorUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorUserID.setStatus("mandatory")
_SmSiaFileMonitorGroupID_Type = DisplayString
_SmSiaFileMonitorGroupID_Object = MibTableColumn
smSiaFileMonitorGroupID = _SmSiaFileMonitorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 29),
    _SmSiaFileMonitorGroupID_Type()
)
smSiaFileMonitorGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSiaFileMonitorGroupID.setStatus("mandatory")


class _SmSiaFileMonitorSize_Type(Integer32):
    """Custom type smSiaFileMonitorSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmSiaFileMonitorSize_Type.__name__ = "Integer32"
_SmSiaFileMonitorSize_Object = MibTableColumn
smSiaFileMonitorSize = _SmSiaFileMonitorSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 30),
    _SmSiaFileMonitorSize_Type()
)
smSiaFileMonitorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorSize.setStatus("mandatory")
_SmSiaFileMonitorTimeLastDataModification_Type = DisplayString
_SmSiaFileMonitorTimeLastDataModification_Object = MibTableColumn
smSiaFileMonitorTimeLastDataModification = _SmSiaFileMonitorTimeLastDataModification_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 31),
    _SmSiaFileMonitorTimeLastDataModification_Type()
)
smSiaFileMonitorTimeLastDataModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorTimeLastDataModification.setStatus("mandatory")
_SmSiaFileMonitorTimeLastFileStatusChange_Type = DisplayString
_SmSiaFileMonitorTimeLastFileStatusChange_Object = MibTableColumn
smSiaFileMonitorTimeLastFileStatusChange = _SmSiaFileMonitorTimeLastFileStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 32),
    _SmSiaFileMonitorTimeLastFileStatusChange_Type()
)
smSiaFileMonitorTimeLastFileStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorTimeLastFileStatusChange.setStatus("mandatory")
_SmSiaFileMonitorReturnCode_Type = Integer32
_SmSiaFileMonitorReturnCode_Object = MibTableColumn
smSiaFileMonitorReturnCode = _SmSiaFileMonitorReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 33),
    _SmSiaFileMonitorReturnCode_Type()
)
smSiaFileMonitorReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorReturnCode.setStatus("mandatory")
_SmSiaFileMonitorMessages_Type = DisplayString
_SmSiaFileMonitorMessages_Object = MibTableColumn
smSiaFileMonitorMessages = _SmSiaFileMonitorMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 21, 1, 1, 34),
    _SmSiaFileMonitorMessages_Type()
)
smSiaFileMonitorMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSiaFileMonitorMessages.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSINFO-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "systemsMonitor6000": systemsMonitor6000,
       "smProgramInformation": smProgramInformation,
       "smSiaProgramData": smSiaProgramData,
       "smSiaProgramDescription": smSiaProgramDescription,
       "smSiaProgramName": smSiaProgramName,
       "smSiaProgramNumber": smSiaProgramNumber,
       "smSiaProgramVersion": smSiaProgramVersion,
       "smSiaProgramCompilationDate": smSiaProgramCompilationDate,
       "smSiaProgramUpTime": smSiaProgramUpTime,
       "smSiaProgramContact": smSiaProgramContact,
       "smSiaProgramControl": smSiaProgramControl,
       "smSiaProgramControlLocalConfigurationFile": smSiaProgramControlLocalConfigurationFile,
       "smSiaProgramControlSavedFlags": smSiaProgramControlSavedFlags,
       "smSiaProgramControlAgentAddress": smSiaProgramControlAgentAddress,
       "smSiaProgramControlReserved1": smSiaProgramControlReserved1,
       "smSiaProgramControlPercentMultiplier": smSiaProgramControlPercentMultiplier,
       "smSiaProgramControlPollTime": smSiaProgramControlPollTime,
       "smSiaProgramControlFlags": smSiaProgramControlFlags,
       "smSiaProgramControlRetryCount": smSiaProgramControlRetryCount,
       "smSiaProgramControlTimeout": smSiaProgramControlTimeout,
       "smSiaProgramControlCurrentFlags": smSiaProgramControlCurrentFlags,
       "smSiaProgramControlReinitFlags": smSiaProgramControlReinitFlags,
       "smSiaProgramControlReInitializeMonitor": smSiaProgramControlReInitializeMonitor,
       "smSiaProgramControlSaveConfiguration": smSiaProgramControlSaveConfiguration,
       "smSiaProgramLog": smSiaProgramLog,
       "smSiaProgramLogFileName": smSiaProgramLogFileName,
       "smSiaProgramLogFileSize": smSiaProgramLogFileSize,
       "smSiaProgramLogMaxFileSize": smSiaProgramLogMaxFileSize,
       "smSiaProgramLogNumFiles": smSiaProgramLogNumFiles,
       "smSiaProgramLogFileBehavior": smSiaProgramLogFileBehavior,
       "smSiaProgramLogMask": smSiaProgramLogMask,
       "smSiaProgramSetableTestObjects": smSiaProgramSetableTestObjects,
       "smSiaProgramControlSetableInteger": smSiaProgramControlSetableInteger,
       "smSiaProgramControlSetableCounter": smSiaProgramControlSetableCounter,
       "smSiaProgramControlSetableGauge": smSiaProgramControlSetableGauge,
       "smSiaProgramControlSetableIpAddress": smSiaProgramControlSetableIpAddress,
       "smSiaProgramControlSetableTimeTicks": smSiaProgramControlSetableTimeTicks,
       "smSiaProgramControlSetableOctetString": smSiaProgramControlSetableOctetString,
       "smSiaResourceUsage": smSiaResourceUsage,
       "smSiaResourceUsageTable": smSiaResourceUsageTable,
       "smSiaResourceUsageEntry": smSiaResourceUsageEntry,
       "smSiaResourceUsageName": smSiaResourceUsageName,
       "smSiaResourceUsageUserTime": smSiaResourceUsageUserTime,
       "smSiaResourceUsageSystemTime": smSiaResourceUsageSystemTime,
       "smSiaResourceUsageTotalTime": smSiaResourceUsageTotalTime,
       "smSiaResourceUsageMaxrss": smSiaResourceUsageMaxrss,
       "smSiaResourceUsageIxrss": smSiaResourceUsageIxrss,
       "smSiaResourceUsageIdrss": smSiaResourceUsageIdrss,
       "smSiaResourceUsageIsrss": smSiaResourceUsageIsrss,
       "smSiaResourceUsageMinflt": smSiaResourceUsageMinflt,
       "smSiaResourceUsageMajflt": smSiaResourceUsageMajflt,
       "smSiaResourceUsageNSwap": smSiaResourceUsageNSwap,
       "smSiaResourceUsageInBlock": smSiaResourceUsageInBlock,
       "smSiaResourceUsageOutBlock": smSiaResourceUsageOutBlock,
       "smSiaResourceUsageMsgsnd": smSiaResourceUsageMsgsnd,
       "smSiaResourceUsageMsgrcv": smSiaResourceUsageMsgrcv,
       "smSiaResourceUsageNSignals": smSiaResourceUsageNSignals,
       "smSiaResourceUsageVcsw": smSiaResourceUsageVcsw,
       "smSiaResourceUsageIcsw": smSiaResourceUsageIcsw,
       "smSiaProgramMessages": smSiaProgramMessages,
       "smSiaProgramMessagesTable": smSiaProgramMessagesTable,
       "smSiaProgramMessagesEntry": smSiaProgramMessagesEntry,
       "smSiaProgramMessagesRowNumber": smSiaProgramMessagesRowNumber,
       "smSiaProgramMessagesTime": smSiaProgramMessagesTime,
       "smSiaProgramMessagesText": smSiaProgramMessagesText,
       "smSiaProgramMessagesTimeStamp": smSiaProgramMessagesTimeStamp,
       "smSiaSystemInformation": smSiaSystemInformation,
       "smSiaSystemDescription": smSiaSystemDescription,
       "smSiaSystemNodeName": smSiaSystemNodeName,
       "smSiaSystemSysName": smSiaSystemSysName,
       "smSiaSystemVersion": smSiaSystemVersion,
       "smSiaSystemRelease": smSiaSystemRelease,
       "smSiaSystemMachine": smSiaSystemMachine,
       "smSiaSystemTime": smSiaSystemTime,
       "smSiaSystemConfiguration": smSiaSystemConfiguration,
       "smSiaSystemBufferPoolMark": smSiaSystemBufferPoolMark,
       "smSiaSystemMaxMbufs": smSiaSystemMaxMbufs,
       "smSiaSystemMaxUserProcesses": smSiaSystemMaxUserProcesses,
       "smSiaSystemMaxSystemProcesses": smSiaSystemMaxSystemProcesses,
       "smSiaSystemRecordLockTableSize": smSiaSystemRecordLockTableSize,
       "smSiaSystemOpenFileTableSize": smSiaSystemOpenFileTableSize,
       "smSiaSystemCBlockArraySize": smSiaSystemCBlockArraySize,
       "smSiaSystemDiskIOHistory": smSiaSystemDiskIOHistory,
       "smSiaSystemAutomaticBootAfterHalt": smSiaSystemAutomaticBootAfterHalt,
       "smSiaSystemMemScrub": smSiaSystemMemScrub,
       "smSiaSystemLeastPriv": smSiaSystemLeastPriv,
       "smSiaSystemMaxPout": smSiaSystemMaxPout,
       "smSiaSystemMinPout": smSiaSystemMinPout,
       "smSiaSystemPageSize": smSiaSystemPageSize,
       "smSiaSystemProcessMaxOpenFiles": smSiaSystemProcessMaxOpenFiles,
       "smSiaSystemProcessMaxOpenStreams": smSiaSystemProcessMaxOpenStreams,
       "smSiaSystemProcessDescriptorTableSize": smSiaSystemProcessDescriptorTableSize,
       "smSiaSystemPhysicalMemorySize": smSiaSystemPhysicalMemorySize,
       "smSiaSystemDevice": smSiaSystemDevice,
       "smSiaSystemDeviceList": smSiaSystemDeviceList,
       "smSiaSystemDeviceListInstalled": smSiaSystemDeviceListInstalled,
       "smSiaSystemDeviceListTable": smSiaSystemDeviceListTable,
       "smSiaSystemDeviceListEntry": smSiaSystemDeviceListEntry,
       "smSiaSystemDeviceListName": smSiaSystemDeviceListName,
       "smSiaSystemDeviceListDescription": smSiaSystemDeviceListDescription,
       "smSiaSystemDeviceListLocation": smSiaSystemDeviceListLocation,
       "smSiaSystemDeviceListVPD": smSiaSystemDeviceListVPD,
       "smSiaSystemDeviceListAttributes": smSiaSystemDeviceListAttributes,
       "smSiaSystemDeviceListDiagnostics": smSiaSystemDeviceListDiagnostics,
       "smSiaSystemDeviceTokenRing": smSiaSystemDeviceTokenRing,
       "smSiaSystemDeviceTokenRingInstalled": smSiaSystemDeviceTokenRingInstalled,
       "smSiaSystemDeviceTokenRingTable": smSiaSystemDeviceTokenRingTable,
       "smSiaSystemDeviceTokenRingEntry": smSiaSystemDeviceTokenRingEntry,
       "smSiaSystemDeviceTokenRingNumber": smSiaSystemDeviceTokenRingNumber,
       "smSiaSystemDeviceTokenRingHardwareAddress": smSiaSystemDeviceTokenRingHardwareAddress,
       "smSiaSystemDeviceTokenRingCurrentAddress": smSiaSystemDeviceTokenRingCurrentAddress,
       "smSiaSystemDeviceTokenRingReceiveDataOffset": smSiaSystemDeviceTokenRingReceiveDataOffset,
       "smSiaSystemDeviceTokenRingBroadwrap": smSiaSystemDeviceTokenRingBroadwrap,
       "smSiaSystemDeviceTokenRingTxByteMcnt": smSiaSystemDeviceTokenRingTxByteMcnt,
       "smSiaSystemDeviceTokenRingTxByteLcnt": smSiaSystemDeviceTokenRingTxByteLcnt,
       "smSiaSystemDeviceTokenRingRxByteMcnt": smSiaSystemDeviceTokenRingRxByteMcnt,
       "smSiaSystemDeviceTokenRingRxByteLcnt": smSiaSystemDeviceTokenRingRxByteLcnt,
       "smSiaSystemDeviceTokenRingTxFrameMcnt": smSiaSystemDeviceTokenRingTxFrameMcnt,
       "smSiaSystemDeviceTokenRingTxFrameLcnt": smSiaSystemDeviceTokenRingTxFrameLcnt,
       "smSiaSystemDeviceTokenRingRxFrameMcnt": smSiaSystemDeviceTokenRingRxFrameMcnt,
       "smSiaSystemDeviceTokenRingRxFrameLcnt": smSiaSystemDeviceTokenRingRxFrameLcnt,
       "smSiaSystemDeviceTokenRingTxErrCnt": smSiaSystemDeviceTokenRingTxErrCnt,
       "smSiaSystemDeviceTokenRingRxErrCnt": smSiaSystemDeviceTokenRingRxErrCnt,
       "smSiaSystemDeviceTokenRingNidTblHigh": smSiaSystemDeviceTokenRingNidTblHigh,
       "smSiaSystemDeviceTokenRingTxQueHigh": smSiaSystemDeviceTokenRingTxQueHigh,
       "smSiaSystemDeviceTokenRingRxQueHigh": smSiaSystemDeviceTokenRingRxQueHigh,
       "smSiaSystemDeviceTokenRingStaQueHigh": smSiaSystemDeviceTokenRingStaQueHigh,
       "smSiaSystemDeviceTokenRingIntrLost": smSiaSystemDeviceTokenRingIntrLost,
       "smSiaSystemDeviceTokenRingWdtLost": smSiaSystemDeviceTokenRingWdtLost,
       "smSiaSystemDeviceTokenRingTimoLost": smSiaSystemDeviceTokenRingTimoLost,
       "smSiaSystemDeviceTokenRingStaQueOverflow": smSiaSystemDeviceTokenRingStaQueOverflow,
       "smSiaSystemDeviceTokenRingRxQueOverflow": smSiaSystemDeviceTokenRingRxQueOverflow,
       "smSiaSystemDeviceTokenRingRxQueNoMbuf": smSiaSystemDeviceTokenRingRxQueNoMbuf,
       "smSiaSystemDeviceTokenRingRxQueNoMbufExt": smSiaSystemDeviceTokenRingRxQueNoMbufExt,
       "smSiaSystemDeviceTokenRingTxIntrCnt": smSiaSystemDeviceTokenRingTxIntrCnt,
       "smSiaSystemDeviceTokenRingRxIntrCnt": smSiaSystemDeviceTokenRingRxIntrCnt,
       "smSiaSystemDeviceTokenRingPktRejCnt": smSiaSystemDeviceTokenRingPktRejCnt,
       "smSiaSystemDeviceTokenRingPktAccCnt": smSiaSystemDeviceTokenRingPktAccCnt,
       "smSiaSystemDeviceTokenRingPktTxCnt": smSiaSystemDeviceTokenRingPktTxCnt,
       "smSiaSystemDeviceTokenRingOvfloPktCnt": smSiaSystemDeviceTokenRingOvfloPktCnt,
       "smSiaSystemDeviceTokenRingPktTxErrCnt": smSiaSystemDeviceTokenRingPktTxErrCnt,
       "smSiaSystemDeviceTokenRingSpeed": smSiaSystemDeviceTokenRingSpeed,
       "smSiaSystemDeviceTokenRingVPD": smSiaSystemDeviceTokenRingVPD,
       "smSiaSystemDeviceTokenRingAdapPhysAddr": smSiaSystemDeviceTokenRingAdapPhysAddr,
       "smSiaSystemDeviceTokenRingUpstreamNodeAddr": smSiaSystemDeviceTokenRingUpstreamNodeAddr,
       "smSiaSystemDeviceTokenRingUpstreamPhysAddr": smSiaSystemDeviceTokenRingUpstreamPhysAddr,
       "smSiaSystemDeviceTokenRingLastPollAddr": smSiaSystemDeviceTokenRingLastPollAddr,
       "smSiaSystemDeviceTokenRingAuthorEnv": smSiaSystemDeviceTokenRingAuthorEnv,
       "smSiaSystemDeviceTokenRingTxAccessPriority": smSiaSystemDeviceTokenRingTxAccessPriority,
       "smSiaSystemDeviceTokenRingSrcClassAuthor": smSiaSystemDeviceTokenRingSrcClassAuthor,
       "smSiaSystemDeviceTokenRingLastAttenCode": smSiaSystemDeviceTokenRingLastAttenCode,
       "smSiaSystemDeviceTokenRingLastSrcAddr": smSiaSystemDeviceTokenRingLastSrcAddr,
       "smSiaSystemDeviceTokenRingLastBeaconType": smSiaSystemDeviceTokenRingLastBeaconType,
       "smSiaSystemDeviceTokenRingLastMajorVector": smSiaSystemDeviceTokenRingLastMajorVector,
       "smSiaSystemDeviceTokenRingRingStatus": smSiaSystemDeviceTokenRingRingStatus,
       "smSiaSystemDeviceTokenRingSoftErrorTimerVal": smSiaSystemDeviceTokenRingSoftErrorTimerVal,
       "smSiaSystemDeviceTokenRingFrontEndTimerVal": smSiaSystemDeviceTokenRingFrontEndTimerVal,
       "smSiaSystemDeviceTokenRingMonitorErrorCode": smSiaSystemDeviceTokenRingMonitorErrorCode,
       "smSiaSystemDeviceTokenRingBeaconTxType": smSiaSystemDeviceTokenRingBeaconTxType,
       "smSiaSystemDeviceTokenRingBeaconRxType": smSiaSystemDeviceTokenRingBeaconRxType,
       "smSiaSystemDeviceTokenRingFrameCorrSave": smSiaSystemDeviceTokenRingFrameCorrSave,
       "smSiaSystemDeviceTokenRingBeaconStationNAUN": smSiaSystemDeviceTokenRingBeaconStationNAUN,
       "smSiaSystemDeviceTokenRingBeaconStationPhysAddr": smSiaSystemDeviceTokenRingBeaconStationPhysAddr,
       "smSiaSystemDeviceTokenRingClear": smSiaSystemDeviceTokenRingClear,
       "smSiaSystemDeviceEthernet": smSiaSystemDeviceEthernet,
       "smSiaSystemDeviceEthernetInstalled": smSiaSystemDeviceEthernetInstalled,
       "smSiaSystemDeviceEthernetTable": smSiaSystemDeviceEthernetTable,
       "smSiaSystemDeviceEthernetEntry": smSiaSystemDeviceEthernetEntry,
       "smSiaSystemDeviceEthernetNumber": smSiaSystemDeviceEthernetNumber,
       "smSiaSystemDeviceEthernetHardwareAddress": smSiaSystemDeviceEthernetHardwareAddress,
       "smSiaSystemDeviceEthernetCurrentAddress": smSiaSystemDeviceEthernetCurrentAddress,
       "smSiaSystemDeviceEthernetReceiveDataOffset": smSiaSystemDeviceEthernetReceiveDataOffset,
       "smSiaSystemDeviceEthernetBroadwrap": smSiaSystemDeviceEthernetBroadwrap,
       "smSiaSystemDeviceEthernetTxByteMcnt": smSiaSystemDeviceEthernetTxByteMcnt,
       "smSiaSystemDeviceEthernetTxByteLcnt": smSiaSystemDeviceEthernetTxByteLcnt,
       "smSiaSystemDeviceEthernetRxByteMcnt": smSiaSystemDeviceEthernetRxByteMcnt,
       "smSiaSystemDeviceEthernetRxByteLcnt": smSiaSystemDeviceEthernetRxByteLcnt,
       "smSiaSystemDeviceEthernetTxFrameMcnt": smSiaSystemDeviceEthernetTxFrameMcnt,
       "smSiaSystemDeviceEthernetTxFrameLcnt": smSiaSystemDeviceEthernetTxFrameLcnt,
       "smSiaSystemDeviceEthernetRxFrameMcnt": smSiaSystemDeviceEthernetRxFrameMcnt,
       "smSiaSystemDeviceEthernetRxFrameLcnt": smSiaSystemDeviceEthernetRxFrameLcnt,
       "smSiaSystemDeviceEthernetTxErrCnt": smSiaSystemDeviceEthernetTxErrCnt,
       "smSiaSystemDeviceEthernetRxErrCnt": smSiaSystemDeviceEthernetRxErrCnt,
       "smSiaSystemDeviceEthernetNidTblHigh": smSiaSystemDeviceEthernetNidTblHigh,
       "smSiaSystemDeviceEthernetTxQueHigh": smSiaSystemDeviceEthernetTxQueHigh,
       "smSiaSystemDeviceEthernetRxQueHigh": smSiaSystemDeviceEthernetRxQueHigh,
       "smSiaSystemDeviceEthernetStaQueHigh": smSiaSystemDeviceEthernetStaQueHigh,
       "smSiaSystemDeviceEthernetIntrLost": smSiaSystemDeviceEthernetIntrLost,
       "smSiaSystemDeviceEthernetWdtLost": smSiaSystemDeviceEthernetWdtLost,
       "smSiaSystemDeviceEthernetTimoLost": smSiaSystemDeviceEthernetTimoLost,
       "smSiaSystemDeviceEthernetStaQueOverflow": smSiaSystemDeviceEthernetStaQueOverflow,
       "smSiaSystemDeviceEthernetRxQueOverflow": smSiaSystemDeviceEthernetRxQueOverflow,
       "smSiaSystemDeviceEthernetRxQueNoMbuf": smSiaSystemDeviceEthernetRxQueNoMbuf,
       "smSiaSystemDeviceEthernetRxQueNoMbufExt": smSiaSystemDeviceEthernetRxQueNoMbufExt,
       "smSiaSystemDeviceEthernetTxIntrCnt": smSiaSystemDeviceEthernetTxIntrCnt,
       "smSiaSystemDeviceEthernetRxIntrCnt": smSiaSystemDeviceEthernetRxIntrCnt,
       "smSiaSystemDeviceEthernetCRCErr": smSiaSystemDeviceEthernetCRCErr,
       "smSiaSystemDeviceEthernetAlignErr": smSiaSystemDeviceEthernetAlignErr,
       "smSiaSystemDeviceEthernetOverrun": smSiaSystemDeviceEthernetOverrun,
       "smSiaSystemDeviceEthernetTooShort": smSiaSystemDeviceEthernetTooShort,
       "smSiaSystemDeviceEthernetTooLong": smSiaSystemDeviceEthernetTooLong,
       "smSiaSystemDeviceEthernetNoResources": smSiaSystemDeviceEthernetNoResources,
       "smSiaSystemDeviceEthernetPktDiscard": smSiaSystemDeviceEthernetPktDiscard,
       "smSiaSystemDeviceEthernetMaxCollision": smSiaSystemDeviceEthernetMaxCollision,
       "smSiaSystemDeviceEthernetLateCollision": smSiaSystemDeviceEthernetLateCollision,
       "smSiaSystemDeviceEthernetCarrierLost": smSiaSystemDeviceEthernetCarrierLost,
       "smSiaSystemDeviceEthernetUnderrun": smSiaSystemDeviceEthernetUnderrun,
       "smSiaSystemDeviceEthernetCTSLost": smSiaSystemDeviceEthernetCTSLost,
       "smSiaSystemDeviceEthernetTxTimeouts": smSiaSystemDeviceEthernetTxTimeouts,
       "smSiaSystemDeviceEthernetParErrCnt": smSiaSystemDeviceEthernetParErrCnt,
       "smSiaSystemDeviceEthernetDiagOverflow": smSiaSystemDeviceEthernetDiagOverflow,
       "smSiaSystemDeviceEthernetExecOverflow": smSiaSystemDeviceEthernetExecOverflow,
       "smSiaSystemDeviceEthernetExecCmdErrors": smSiaSystemDeviceEthernetExecCmdErrors,
       "smSiaSystemDeviceEthernetHostRecEol": smSiaSystemDeviceEthernetHostRecEol,
       "smSiaSystemDeviceEthernetAdptRecEol": smSiaSystemDeviceEthernetAdptRecEol,
       "smSiaSystemDeviceEthernetHostRecPkt": smSiaSystemDeviceEthernetHostRecPkt,
       "smSiaSystemDeviceEthernetAdptRecPkt": smSiaSystemDeviceEthernetAdptRecPkt,
       "smSiaSystemDeviceEthernetStartRxCmd": smSiaSystemDeviceEthernetStartRxCmd,
       "smSiaSystemDeviceEthernetStartRxDmaTimeouts": smSiaSystemDeviceEthernetStartRxDmaTimeouts,
       "smSiaSystemDeviceEthernetVPD": smSiaSystemDeviceEthernetVPD,
       "smSiaSystemDeviceEthernetClear": smSiaSystemDeviceEthernetClear,
       "smSiaSystemDeviceX25": smSiaSystemDeviceX25,
       "smSiaSystemDeviceX25Installed": smSiaSystemDeviceX25Installed,
       "smSiaSystemDeviceX25Table": smSiaSystemDeviceX25Table,
       "smSiaSystemDeviceX25Entry": smSiaSystemDeviceX25Entry,
       "smSiaSystemDeviceX25Number": smSiaSystemDeviceX25Number,
       "smSiaSystemDeviceX25Address": smSiaSystemDeviceX25Address,
       "smSiaSystemDeviceX25SupportLevel": smSiaSystemDeviceX25SupportLevel,
       "smSiaSystemDeviceX25SupportedFacilities": smSiaSystemDeviceX25SupportedFacilities,
       "smSiaSystemDeviceX25NetworkId": smSiaSystemDeviceX25NetworkId,
       "smSiaSystemDeviceX25MaxTxPacketSize": smSiaSystemDeviceX25MaxTxPacketSize,
       "smSiaSystemDeviceX25MaxRxPacketSize": smSiaSystemDeviceX25MaxRxPacketSize,
       "smSiaSystemDeviceX25DefaultSvcTxPacketSize": smSiaSystemDeviceX25DefaultSvcTxPacketSize,
       "smSiaSystemDeviceX25DefaultSvcRxPacketSize": smSiaSystemDeviceX25DefaultSvcRxPacketSize,
       "smSiaSystemDeviceX25ReceiveDataTransferOffset": smSiaSystemDeviceX25ReceiveDataTransferOffset,
       "smSiaSystemDeviceX25MemoryWindowSize": smSiaSystemDeviceX25MemoryWindowSize,
       "smSiaSystemDeviceX25TxByteMcnt": smSiaSystemDeviceX25TxByteMcnt,
       "smSiaSystemDeviceX25TxByteLcnt": smSiaSystemDeviceX25TxByteLcnt,
       "smSiaSystemDeviceX25RxByteMcnt": smSiaSystemDeviceX25RxByteMcnt,
       "smSiaSystemDeviceX25RxByteLcnt": smSiaSystemDeviceX25RxByteLcnt,
       "smSiaSystemDeviceX25TxFrameMcnt": smSiaSystemDeviceX25TxFrameMcnt,
       "smSiaSystemDeviceX25TxFrameLcnt": smSiaSystemDeviceX25TxFrameLcnt,
       "smSiaSystemDeviceX25RxFrameMcnt": smSiaSystemDeviceX25RxFrameMcnt,
       "smSiaSystemDeviceX25RxFrameLcnt": smSiaSystemDeviceX25RxFrameLcnt,
       "smSiaSystemDeviceX25TxErrCnt": smSiaSystemDeviceX25TxErrCnt,
       "smSiaSystemDeviceX25RxErrCnt": smSiaSystemDeviceX25RxErrCnt,
       "smSiaSystemDeviceX25NidTblHigh": smSiaSystemDeviceX25NidTblHigh,
       "smSiaSystemDeviceX25TxQueHigh": smSiaSystemDeviceX25TxQueHigh,
       "smSiaSystemDeviceX25RxQueHigh": smSiaSystemDeviceX25RxQueHigh,
       "smSiaSystemDeviceX25StaQueHigh": smSiaSystemDeviceX25StaQueHigh,
       "smSiaSystemDeviceX25IgnoredFTx": smSiaSystemDeviceX25IgnoredFTx,
       "smSiaSystemDeviceX25RrFTx": smSiaSystemDeviceX25RrFTx,
       "smSiaSystemDeviceX25RnrFTx": smSiaSystemDeviceX25RnrFTx,
       "smSiaSystemDeviceX25RejFTx": smSiaSystemDeviceX25RejFTx,
       "smSiaSystemDeviceX25InfoFTx": smSiaSystemDeviceX25InfoFTx,
       "smSiaSystemDeviceX25SabmFTx": smSiaSystemDeviceX25SabmFTx,
       "smSiaSystemDeviceX25SarmDmFTx": smSiaSystemDeviceX25SarmDmFTx,
       "smSiaSystemDeviceX25DiscFTx": smSiaSystemDeviceX25DiscFTx,
       "smSiaSystemDeviceX25UaFTx": smSiaSystemDeviceX25UaFTx,
       "smSiaSystemDeviceX25FrmrFTx": smSiaSystemDeviceX25FrmrFTx,
       "smSiaSystemDeviceX25BadNrFTx": smSiaSystemDeviceX25BadNrFTx,
       "smSiaSystemDeviceX25UnknownFTx": smSiaSystemDeviceX25UnknownFTx,
       "smSiaSystemDeviceX25XidFTx": smSiaSystemDeviceX25XidFTx,
       "smSiaSystemDeviceX25BadLengthFTx": smSiaSystemDeviceX25BadLengthFTx,
       "smSiaSystemDeviceX25T1Expirations": smSiaSystemDeviceX25T1Expirations,
       "smSiaSystemDeviceX25Lvl2Connects": smSiaSystemDeviceX25Lvl2Connects,
       "smSiaSystemDeviceX25Lvl2Disconnects": smSiaSystemDeviceX25Lvl2Disconnects,
       "smSiaSystemDeviceX25CarrierLoss": smSiaSystemDeviceX25CarrierLoss,
       "smSiaSystemDeviceX25ConnectTime": smSiaSystemDeviceX25ConnectTime,
       "smSiaSystemDeviceX25T4Expirations": smSiaSystemDeviceX25T4Expirations,
       "smSiaSystemDeviceX25T4N2Times": smSiaSystemDeviceX25T4N2Times,
       "smSiaSystemDeviceX25IgnoredFRx": smSiaSystemDeviceX25IgnoredFRx,
       "smSiaSystemDeviceX25RrFRx": smSiaSystemDeviceX25RrFRx,
       "smSiaSystemDeviceX25RnrFRx": smSiaSystemDeviceX25RnrFRx,
       "smSiaSystemDeviceX25RejFRx": smSiaSystemDeviceX25RejFRx,
       "smSiaSystemDeviceX25InfoFRx": smSiaSystemDeviceX25InfoFRx,
       "smSiaSystemDeviceX25SabmFRx": smSiaSystemDeviceX25SabmFRx,
       "smSiaSystemDeviceX25SarmDmFRx": smSiaSystemDeviceX25SarmDmFRx,
       "smSiaSystemDeviceX25DiscFRx": smSiaSystemDeviceX25DiscFRx,
       "smSiaSystemDeviceX25UaFRx": smSiaSystemDeviceX25UaFRx,
       "smSiaSystemDeviceX25FrmrFRx": smSiaSystemDeviceX25FrmrFRx,
       "smSiaSystemDeviceX25BadNrFRx": smSiaSystemDeviceX25BadNrFRx,
       "smSiaSystemDeviceX25UnknownFRx": smSiaSystemDeviceX25UnknownFRx,
       "smSiaSystemDeviceX25XidFRx": smSiaSystemDeviceX25XidFRx,
       "smSiaSystemDeviceX25BadLengthFRx": smSiaSystemDeviceX25BadLengthFRx,
       "smSiaSystemDeviceX25DataPTx": smSiaSystemDeviceX25DataPTx,
       "smSiaSystemDeviceX25RrPTx": smSiaSystemDeviceX25RrPTx,
       "smSiaSystemDeviceX25RnrPTx": smSiaSystemDeviceX25RnrPTx,
       "smSiaSystemDeviceX25InterruptPTx": smSiaSystemDeviceX25InterruptPTx,
       "smSiaSystemDeviceX25InterruptConfirmPTx": smSiaSystemDeviceX25InterruptConfirmPTx,
       "smSiaSystemDeviceX25CallRequestPTx": smSiaSystemDeviceX25CallRequestPTx,
       "smSiaSystemDeviceX25CallAcceptPTx": smSiaSystemDeviceX25CallAcceptPTx,
       "smSiaSystemDeviceX25ClearRequestPTx": smSiaSystemDeviceX25ClearRequestPTx,
       "smSiaSystemDeviceX25ClearConfirmPTx": smSiaSystemDeviceX25ClearConfirmPTx,
       "smSiaSystemDeviceX25ResetRequestPTx": smSiaSystemDeviceX25ResetRequestPTx,
       "smSiaSystemDeviceX25ResetConfirmPTx": smSiaSystemDeviceX25ResetConfirmPTx,
       "smSiaSystemDeviceX25DiagnosticPTx": smSiaSystemDeviceX25DiagnosticPTx,
       "smSiaSystemDeviceX25RegistrationPTx": smSiaSystemDeviceX25RegistrationPTx,
       "smSiaSystemDeviceX25RegistrationConfirmPTx": smSiaSystemDeviceX25RegistrationConfirmPTx,
       "smSiaSystemDeviceX25RestartPTx": smSiaSystemDeviceX25RestartPTx,
       "smSiaSystemDeviceX25RestartConfirmPTx": smSiaSystemDeviceX25RestartConfirmPTx,
       "smSiaSystemDeviceX25ErrorPTx": smSiaSystemDeviceX25ErrorPTx,
       "smSiaSystemDeviceX25T20Expirations": smSiaSystemDeviceX25T20Expirations,
       "smSiaSystemDeviceX25T21Expirations": smSiaSystemDeviceX25T21Expirations,
       "smSiaSystemDeviceX25T22Expirations": smSiaSystemDeviceX25T22Expirations,
       "smSiaSystemDeviceX25T23Expirations": smSiaSystemDeviceX25T23Expirations,
       "smSiaSystemDeviceX25VcEstablishments": smSiaSystemDeviceX25VcEstablishments,
       "smSiaSystemDeviceX25T24Expirations": smSiaSystemDeviceX25T24Expirations,
       "smSiaSystemDeviceX25T25Expirations": smSiaSystemDeviceX25T25Expirations,
       "smSiaSystemDeviceX25T26Expirations": smSiaSystemDeviceX25T26Expirations,
       "smSiaSystemDeviceX25T28Expirations": smSiaSystemDeviceX25T28Expirations,
       "smSiaSystemDeviceX25DataPRx": smSiaSystemDeviceX25DataPRx,
       "smSiaSystemDeviceX25RrPRx": smSiaSystemDeviceX25RrPRx,
       "smSiaSystemDeviceX25RnrPRx": smSiaSystemDeviceX25RnrPRx,
       "smSiaSystemDeviceX25InterruptPRx": smSiaSystemDeviceX25InterruptPRx,
       "smSiaSystemDeviceX25InterruptConfirmPRx": smSiaSystemDeviceX25InterruptConfirmPRx,
       "smSiaSystemDeviceX25IncomingCallPRx": smSiaSystemDeviceX25IncomingCallPRx,
       "smSiaSystemDeviceX25CallConnectedPRx": smSiaSystemDeviceX25CallConnectedPRx,
       "smSiaSystemDeviceX25ClearIndicationPRx": smSiaSystemDeviceX25ClearIndicationPRx,
       "smSiaSystemDeviceX25ClearConfirmPRx": smSiaSystemDeviceX25ClearConfirmPRx,
       "smSiaSystemDeviceX25ResetIndicationPRx": smSiaSystemDeviceX25ResetIndicationPRx,
       "smSiaSystemDeviceX25ResetConfirmPRx": smSiaSystemDeviceX25ResetConfirmPRx,
       "smSiaSystemDeviceX25DiagnosticPRx": smSiaSystemDeviceX25DiagnosticPRx,
       "smSiaSystemDeviceX25RegistrationPRx": smSiaSystemDeviceX25RegistrationPRx,
       "smSiaSystemDeviceX25RegistrationConfirmPRx": smSiaSystemDeviceX25RegistrationConfirmPRx,
       "smSiaSystemDeviceX25RestartPRx": smSiaSystemDeviceX25RestartPRx,
       "smSiaSystemDeviceX25RestartConfirmPRx": smSiaSystemDeviceX25RestartConfirmPRx,
       "smSiaSystemDeviceX25TxUnknownSize": smSiaSystemDeviceX25TxUnknownSize,
       "smSiaSystemDeviceX25TxReserved1": smSiaSystemDeviceX25TxReserved1,
       "smSiaSystemDeviceX25TxReserved2": smSiaSystemDeviceX25TxReserved2,
       "smSiaSystemDeviceX25TxReserved3": smSiaSystemDeviceX25TxReserved3,
       "smSiaSystemDeviceX25Tx0x15": smSiaSystemDeviceX25Tx0x15,
       "smSiaSystemDeviceX25Tx16x31": smSiaSystemDeviceX25Tx16x31,
       "smSiaSystemDeviceX25Tx32x63": smSiaSystemDeviceX25Tx32x63,
       "smSiaSystemDeviceX25Tx64x127": smSiaSystemDeviceX25Tx64x127,
       "smSiaSystemDeviceX25Tx128x255": smSiaSystemDeviceX25Tx128x255,
       "smSiaSystemDeviceX25Tx256x511": smSiaSystemDeviceX25Tx256x511,
       "smSiaSystemDeviceX25Tx512x1023": smSiaSystemDeviceX25Tx512x1023,
       "smSiaSystemDeviceX25Tx1024x2047": smSiaSystemDeviceX25Tx1024x2047,
       "smSiaSystemDeviceX25Tx2048x4095": smSiaSystemDeviceX25Tx2048x4095,
       "smSiaSystemDeviceX25TxReserved13": smSiaSystemDeviceX25TxReserved13,
       "smSiaSystemDeviceX25TxReserved14": smSiaSystemDeviceX25TxReserved14,
       "smSiaSystemDeviceX25TxReserved15": smSiaSystemDeviceX25TxReserved15,
       "smSiaSystemDeviceX25TxTotalPackets": smSiaSystemDeviceX25TxTotalPackets,
       "smSiaSystemDeviceX25RxUnknownSize": smSiaSystemDeviceX25RxUnknownSize,
       "smSiaSystemDeviceX25RxReserved1": smSiaSystemDeviceX25RxReserved1,
       "smSiaSystemDeviceX25RxReserved2": smSiaSystemDeviceX25RxReserved2,
       "smSiaSystemDeviceX25RxReserved3": smSiaSystemDeviceX25RxReserved3,
       "smSiaSystemDeviceX25Rx0x15": smSiaSystemDeviceX25Rx0x15,
       "smSiaSystemDeviceX25Rx16x31": smSiaSystemDeviceX25Rx16x31,
       "smSiaSystemDeviceX25Rx32x63": smSiaSystemDeviceX25Rx32x63,
       "smSiaSystemDeviceX25Rx64x127": smSiaSystemDeviceX25Rx64x127,
       "smSiaSystemDeviceX25Rx128x255": smSiaSystemDeviceX25Rx128x255,
       "smSiaSystemDeviceX25Rx256x511": smSiaSystemDeviceX25Rx256x511,
       "smSiaSystemDeviceX25Rx512x1023": smSiaSystemDeviceX25Rx512x1023,
       "smSiaSystemDeviceX25Rx1024x2047": smSiaSystemDeviceX25Rx1024x2047,
       "smSiaSystemDeviceX25Rx2048x4095": smSiaSystemDeviceX25Rx2048x4095,
       "smSiaSystemDeviceX25RxReserved13": smSiaSystemDeviceX25RxReserved13,
       "smSiaSystemDeviceX25RxReserved14": smSiaSystemDeviceX25RxReserved14,
       "smSiaSystemDeviceX25RxReserved15": smSiaSystemDeviceX25RxReserved15,
       "smSiaSystemDeviceX25RxTotalPackets": smSiaSystemDeviceX25RxTotalPackets,
       "smSiaSystemDeviceX25Clear": smSiaSystemDeviceX25Clear,
       "smSiaSystemDeviceX25RouteCount": smSiaSystemDeviceX25RouteCount,
       "smSiaSystemDeviceX25RouteTable": smSiaSystemDeviceX25RouteTable,
       "smSiaSystemDeviceX25RouteEntry": smSiaSystemDeviceX25RouteEntry,
       "smSiaSystemDeviceX25RouteNumber": smSiaSystemDeviceX25RouteNumber,
       "smSiaSystemDeviceX25RouteEntryName": smSiaSystemDeviceX25RouteEntryName,
       "smSiaSystemDeviceX25RouteUserName": smSiaSystemDeviceX25RouteUserName,
       "smSiaSystemDeviceX25RoutePort": smSiaSystemDeviceX25RoutePort,
       "smSiaSystemDeviceX25RouteCallingAddress": smSiaSystemDeviceX25RouteCallingAddress,
       "smSiaSystemDeviceX25RouteCalledSubaddress": smSiaSystemDeviceX25RouteCalledSubaddress,
       "smSiaSystemDeviceX25RouteCallingAddressExt": smSiaSystemDeviceX25RouteCallingAddressExt,
       "smSiaSystemDeviceX25RouteCalledAddressExt": smSiaSystemDeviceX25RouteCalledAddressExt,
       "smSiaSystemDeviceX25RouteCalledUserData": smSiaSystemDeviceX25RouteCalledUserData,
       "smSiaSystemDeviceX25RoutePriority": smSiaSystemDeviceX25RoutePriority,
       "smSiaSystemDeviceX25RouteAction": smSiaSystemDeviceX25RouteAction,
       "smSiaSystemPagingInformation": smSiaSystemPagingInformation,
       "smSiaSystemFreePagingSpace": smSiaSystemFreePagingSpace,
       "smSiaSystemFreePagingSpaceUntilKill": smSiaSystemFreePagingSpaceUntilKill,
       "smSiaSystemKillThresholdToFreePagingSpacePercent": smSiaSystemKillThresholdToFreePagingSpacePercent,
       "smSiaSystemPagingSpace": smSiaSystemPagingSpace,
       "smSiaSystemPagingSpaceCount": smSiaSystemPagingSpaceCount,
       "smSiaSystemPagingSpaceTable": smSiaSystemPagingSpaceTable,
       "smSiaSystemPagingSpaceEntry": smSiaSystemPagingSpaceEntry,
       "smSiaSystemPagingSpaceName": smSiaSystemPagingSpaceName,
       "smSiaSystemPagingSpacePhysicalVolume": smSiaSystemPagingSpacePhysicalVolume,
       "smSiaSystemPagingSpaceVolumeGroup": smSiaSystemPagingSpaceVolumeGroup,
       "smSiaSystemPagingSpaceSize": smSiaSystemPagingSpaceSize,
       "smSiaSystemPagingSpacePercentUsed": smSiaSystemPagingSpacePercentUsed,
       "smSiaSystemPagingSpaceActive": smSiaSystemPagingSpaceActive,
       "smSiaSystemPagingSpaceAuto": smSiaSystemPagingSpaceAuto,
       "smSiaSystemPagingSpaceType": smSiaSystemPagingSpaceType,
       "smSiaSystemPagingStatistics": smSiaSystemPagingStatistics,
       "smSiaSystemPagingStatisticsPollingInterval": smSiaSystemPagingStatisticsPollingInterval,
       "smSiaSystemPagingStatisticsTable": smSiaSystemPagingStatisticsTable,
       "smSiaSystemPagingStatisticsEntry": smSiaSystemPagingStatisticsEntry,
       "smSiaSystemPagingStatisticsName": smSiaSystemPagingStatisticsName,
       "smSiaSystemPagingStatisticsIntervalStartTime": smSiaSystemPagingStatisticsIntervalStartTime,
       "smSiaSystemPagingStatisticsIntervalLength": smSiaSystemPagingStatisticsIntervalLength,
       "smSiaSystemPagingStatisticsPageFaults": smSiaSystemPagingStatisticsPageFaults,
       "smSiaSystemPagingStatisticsPageReclaims": smSiaSystemPagingStatisticsPageReclaims,
       "smSiaSystemPagingStatisticsPagesPagedIn": smSiaSystemPagingStatisticsPagesPagedIn,
       "smSiaSystemPagingStatisticsPagesPagedOut": smSiaSystemPagingStatisticsPagesPagedOut,
       "smSiaSystemPagingStatisticsPageInsFromPagingSpace": smSiaSystemPagingStatisticsPageInsFromPagingSpace,
       "smSiaSystemPagingStatisticsPageOutsFromPagingSpace": smSiaSystemPagingStatisticsPageOutsFromPagingSpace,
       "smSiaSystemPagingStatisticsStartIOs": smSiaSystemPagingStatisticsStartIOs,
       "smSiaSystemPagingStatisticsDoneIOs": smSiaSystemPagingStatisticsDoneIOs,
       "smSiaSystemPagingStatisticsPageScans": smSiaSystemPagingStatisticsPageScans,
       "smSiaSystemPagingStatisticsScanClockCycles": smSiaSystemPagingStatisticsScanClockCycles,
       "smSiaSystemPagingStatisticsPageSteals": smSiaSystemPagingStatisticsPageSteals,
       "smSiaSystemPagingStatisticsFreeFrameWaits": smSiaSystemPagingStatisticsFreeFrameWaits,
       "smSiaSystemPagingStatisticsExtendXPTWaits": smSiaSystemPagingStatisticsExtendXPTWaits,
       "smSiaSystemPagingStatisticsPendingIOWaits": smSiaSystemPagingStatisticsPendingIOWaits,
       "smSiaSystemPagingStatisticsPageFaultsMinimum": smSiaSystemPagingStatisticsPageFaultsMinimum,
       "smSiaSystemPagingStatisticsPageReclaimsMinimum": smSiaSystemPagingStatisticsPageReclaimsMinimum,
       "smSiaSystemPagingStatisticsPagesPagedInMinimum": smSiaSystemPagingStatisticsPagesPagedInMinimum,
       "smSiaSystemPagingStatisticsPagesPagedOutMinimum": smSiaSystemPagingStatisticsPagesPagedOutMinimum,
       "smSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum": smSiaSystemPagingStatisticsPageInsFromPagingSpaceMinimum,
       "smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum": smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMinimum,
       "smSiaSystemPagingStatisticsStartIOsMinimum": smSiaSystemPagingStatisticsStartIOsMinimum,
       "smSiaSystemPagingStatisticsDoneIOsMinimum": smSiaSystemPagingStatisticsDoneIOsMinimum,
       "smSiaSystemPagingStatisticsPageScansMinimum": smSiaSystemPagingStatisticsPageScansMinimum,
       "smSiaSystemPagingStatisticsScanClockCyclesMinimum": smSiaSystemPagingStatisticsScanClockCyclesMinimum,
       "smSiaSystemPagingStatisticsPageStealsMinimum": smSiaSystemPagingStatisticsPageStealsMinimum,
       "smSiaSystemPagingStatisticsFreeFrameWaitsMinimum": smSiaSystemPagingStatisticsFreeFrameWaitsMinimum,
       "smSiaSystemPagingStatisticsExtendXPTWaitsMinimum": smSiaSystemPagingStatisticsExtendXPTWaitsMinimum,
       "smSiaSystemPagingStatisticsPendingIOWaitsMinimum": smSiaSystemPagingStatisticsPendingIOWaitsMinimum,
       "smSiaSystemPagingStatisticsPageFaultsMaximum": smSiaSystemPagingStatisticsPageFaultsMaximum,
       "smSiaSystemPagingStatisticsPageReclaimsMaximum": smSiaSystemPagingStatisticsPageReclaimsMaximum,
       "smSiaSystemPagingStatisticsPagesPagedInMaximum": smSiaSystemPagingStatisticsPagesPagedInMaximum,
       "smSiaSystemPagingStatisticsPagesPagedOutMaximum": smSiaSystemPagingStatisticsPagesPagedOutMaximum,
       "smSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum": smSiaSystemPagingStatisticsPageInsFromPagingSpaceMaximum,
       "smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum": smSiaSystemPagingStatisticsPageOutsFromPagingSpaceMaximum,
       "smSiaSystemPagingStatisticsStartIOsMaximum": smSiaSystemPagingStatisticsStartIOsMaximum,
       "smSiaSystemPagingStatisticsDoneIOsMaximum": smSiaSystemPagingStatisticsDoneIOsMaximum,
       "smSiaSystemPagingStatisticsPageScansMaximum": smSiaSystemPagingStatisticsPageScansMaximum,
       "smSiaSystemPagingStatisticsScanClockCyclesMaximum": smSiaSystemPagingStatisticsScanClockCyclesMaximum,
       "smSiaSystemPagingStatisticsPageStealsMaximum": smSiaSystemPagingStatisticsPageStealsMaximum,
       "smSiaSystemPagingStatisticsFreeFrameWaitsMaximum": smSiaSystemPagingStatisticsFreeFrameWaitsMaximum,
       "smSiaSystemPagingStatisticsExtendXPTWaitsMaximum": smSiaSystemPagingStatisticsExtendXPTWaitsMaximum,
       "smSiaSystemPagingStatisticsPendingIOWaitsMaximum": smSiaSystemPagingStatisticsPendingIOWaitsMaximum,
       "smSiaSystemFileSystem": smSiaSystemFileSystem,
       "smSiaSystemFileSystemMounted": smSiaSystemFileSystemMounted,
       "smSiaSystemFileSystemTable": smSiaSystemFileSystemTable,
       "smSiaSystemFileSystemEntry": smSiaSystemFileSystemEntry,
       "smSiaSystemFileSystemName": smSiaSystemFileSystemName,
       "smSiaSystemFileSystemSize": smSiaSystemFileSystemSize,
       "smSiaSystemFileSystemFree": smSiaSystemFileSystemFree,
       "smSiaSystemFileSystemPercentUsed": smSiaSystemFileSystemPercentUsed,
       "smSiaSystemFileSystemInodesUsed": smSiaSystemFileSystemInodesUsed,
       "smSiaSystemFileSystemInodesPercentUsed": smSiaSystemFileSystemInodesPercentUsed,
       "smSiaSystemFileSystemInodeCount": smSiaSystemFileSystemInodeCount,
       "smSiaSystemFileSystemFileSystem": smSiaSystemFileSystemFileSystem,
       "smSiaSystemFileSystemRemote": smSiaSystemFileSystemRemote,
       "smSiaSystemSubSystems": smSiaSystemSubSystems,
       "smSiaSystemSubSystemsCount": smSiaSystemSubSystemsCount,
       "smSiaSystemSubSystemsTable": smSiaSystemSubSystemsTable,
       "smSiaSystemSubSystemsEntry": smSiaSystemSubSystemsEntry,
       "smSiaSystemSubSystemsName": smSiaSystemSubSystemsName,
       "smSiaSystemSubSystemsPID": smSiaSystemSubSystemsPID,
       "smSiaSystemSubSystemsStatusDescription": smSiaSystemSubSystemsStatusDescription,
       "smSiaSystemSubSystemsStatusText": smSiaSystemSubSystemsStatusText,
       "smSiaSystemSubSystemsStatusCode": smSiaSystemSubSystemsStatusCode,
       "smSiaSystemProcess": smSiaSystemProcess,
       "smSiaSystemProcessCount": smSiaSystemProcessCount,
       "smSiaSystemProcessTable": smSiaSystemProcessTable,
       "smSiaSystemProcessEntry": smSiaSystemProcessEntry,
       "smSiaSystemProcessLoginUser": smSiaSystemProcessLoginUser,
       "smSiaSystemProcessPID": smSiaSystemProcessPID,
       "smSiaSystemProcessParentPID": smSiaSystemProcessParentPID,
       "smSiaSystemProcessCPUTime": smSiaSystemProcessCPUTime,
       "smSiaSystemProcessUserTime": smSiaSystemProcessUserTime,
       "smSiaSystemProcessSystemTime": smSiaSystemProcessSystemTime,
       "smSiaSystemProcessPageFaultsIO": smSiaSystemProcessPageFaultsIO,
       "smSiaSystemProcessPageFaultsNoIO": smSiaSystemProcessPageFaultsNoIO,
       "smSiaSystemProcessPriority": smSiaSystemProcessPriority,
       "smSiaSystemProcessNice": smSiaSystemProcessNice,
       "smSiaSystemProcessState": smSiaSystemProcessState,
       "smSiaSystemProcessWait": smSiaSystemProcessWait,
       "smSiaSystemProcessDataResidentSetSize": smSiaSystemProcessDataResidentSetSize,
       "smSiaSystemProcessTextResidentSetSize": smSiaSystemProcessTextResidentSetSize,
       "smSiaSystemProcessImageSize": smSiaSystemProcessImageSize,
       "smSiaSystemProcessDataVirtualMemorySize": smSiaSystemProcessDataVirtualMemorySize,
       "smSiaSystemProcessPercentMemory": smSiaSystemProcessPercentMemory,
       "smSiaSystemProcessCPU": smSiaSystemProcessCPU,
       "smSiaSystemProcessStartTime": smSiaSystemProcessStartTime,
       "smSiaSystemProcessCommand": smSiaSystemProcessCommand,
       "smSiaSystemProcessLoginUID": smSiaSystemProcessLoginUID,
       "smSiaSystemProcessEffectiveUID": smSiaSystemProcessEffectiveUID,
       "smSiaSystemProcessEffectiveGID": smSiaSystemProcessEffectiveGID,
       "smSiaSystemProcessEffectiveGroupName": smSiaSystemProcessEffectiveGroupName,
       "smSiaSystemProcessSUID": smSiaSystemProcessSUID,
       "smSiaSystemProcessPgrp": smSiaSystemProcessPgrp,
       "smSiaSystemProcessPFlags": smSiaSystemProcessPFlags,
       "smSiaSystemProcessAdspace": smSiaSystemProcessAdspace,
       "smSiaSystemProcessTTYp": smSiaSystemProcessTTYp,
       "smSiaSystemProcessTTYd": smSiaSystemProcessTTYd,
       "smSiaSystemProcessNSwap": smSiaSystemProcessNSwap,
       "smSiaSystemProcessInblocks": smSiaSystemProcessInblocks,
       "smSiaSystemProcessOutblocks": smSiaSystemProcessOutblocks,
       "smSiaSystemProcessMsgsnd": smSiaSystemProcessMsgsnd,
       "smSiaSystemProcessMsgrcv": smSiaSystemProcessMsgrcv,
       "smSiaSystemProcessNsignals": smSiaSystemProcessNsignals,
       "smSiaSystemProcessNVcsw": smSiaSystemProcessNVcsw,
       "smSiaSystemProcessNIvcsw": smSiaSystemProcessNIvcsw,
       "smSiaSystemProcessArguments": smSiaSystemProcessArguments,
       "smSiaSystemProcessSignal": smSiaSystemProcessSignal,
       "smSiaSystemUsers": smSiaSystemUsers,
       "smSiaSystemUsersLoggedIn": smSiaSystemUsersLoggedIn,
       "smSiaSystemUsersTable": smSiaSystemUsersTable,
       "smSiaSystemUsersEntry": smSiaSystemUsersEntry,
       "smSiaSystemUsersName": smSiaSystemUsersName,
       "smSiaSystemUsersLine": smSiaSystemUsersLine,
       "smSiaSystemUsersTime": smSiaSystemUsersTime,
       "smSiaSystemUsersPID": smSiaSystemUsersPID,
       "smSiaSystemUsersRemoteHost": smSiaSystemUsersRemoteHost,
       "smSiaSystemUtilization": smSiaSystemUtilization,
       "smSiaSystemUtilizationCPU": smSiaSystemUtilizationCPU,
       "smSiaSystemUtilizationCPUPollingInterval": smSiaSystemUtilizationCPUPollingInterval,
       "smSiaSystemUtilizationCPUCount": smSiaSystemUtilizationCPUCount,
       "smSiaSystemUtilizationCPUTable": smSiaSystemUtilizationCPUTable,
       "smSiaSystemUtilizationCPUEntry": smSiaSystemUtilizationCPUEntry,
       "smSiaSystemUtilizationCPUIntervalName": smSiaSystemUtilizationCPUIntervalName,
       "smSiaSystemUtilizationCPUIntervalStartTime": smSiaSystemUtilizationCPUIntervalStartTime,
       "smSiaSystemUtilizationCPUIntervalLength": smSiaSystemUtilizationCPUIntervalLength,
       "smSiaSystemUtilizationCPUUser": smSiaSystemUtilizationCPUUser,
       "smSiaSystemUtilizationCPUSystem": smSiaSystemUtilizationCPUSystem,
       "smSiaSystemUtilizationCPUIdle": smSiaSystemUtilizationCPUIdle,
       "smSiaSystemUtilizationCPUWait": smSiaSystemUtilizationCPUWait,
       "smSiaSystemUtilizationCPUBusy": smSiaSystemUtilizationCPUBusy,
       "smSiaSystemUtilizationCPUUserMinimum": smSiaSystemUtilizationCPUUserMinimum,
       "smSiaSystemUtilizationCPUSystemMinimum": smSiaSystemUtilizationCPUSystemMinimum,
       "smSiaSystemUtilizationCPUIdleMinimum": smSiaSystemUtilizationCPUIdleMinimum,
       "smSiaSystemUtilizationCPUWaitMinimum": smSiaSystemUtilizationCPUWaitMinimum,
       "smSiaSystemUtilizationCPUBusyMinimum": smSiaSystemUtilizationCPUBusyMinimum,
       "smSiaSystemUtilizationCPUUserMaximum": smSiaSystemUtilizationCPUUserMaximum,
       "smSiaSystemUtilizationCPUSystemMaximum": smSiaSystemUtilizationCPUSystemMaximum,
       "smSiaSystemUtilizationCPUIdleMaximum": smSiaSystemUtilizationCPUIdleMaximum,
       "smSiaSystemUtilizationCPUWaitMaximum": smSiaSystemUtilizationCPUWaitMaximum,
       "smSiaSystemUtilizationCPUBusyMaximum": smSiaSystemUtilizationCPUBusyMaximum,
       "smSiaSystemUtilizationCPUNumber": smSiaSystemUtilizationCPUNumber,
       "smSiaSystemUtilizationKernel": smSiaSystemUtilizationKernel,
       "smSiaSystemUtilizationKernelPollingInterval": smSiaSystemUtilizationKernelPollingInterval,
       "smSiaSystemUtilizationKernelTable": smSiaSystemUtilizationKernelTable,
       "smSiaSystemUtilizationKernelEntry": smSiaSystemUtilizationKernelEntry,
       "smSiaSystemUtilizationKernelName": smSiaSystemUtilizationKernelName,
       "smSiaSystemUtilizationKernelIntervalStartTime": smSiaSystemUtilizationKernelIntervalStartTime,
       "smSiaSystemUtilizationKernelIntervalLength": smSiaSystemUtilizationKernelIntervalLength,
       "smSiaSystemUtilizationKernelContextSwitches": smSiaSystemUtilizationKernelContextSwitches,
       "smSiaSystemUtilizationKernelSystemCalls": smSiaSystemUtilizationKernelSystemCalls,
       "smSiaSystemUtilizationKernelSystemReads": smSiaSystemUtilizationKernelSystemReads,
       "smSiaSystemUtilizationKernelSystemWrites": smSiaSystemUtilizationKernelSystemWrites,
       "smSiaSystemUtilizationKernelForks": smSiaSystemUtilizationKernelForks,
       "smSiaSystemUtilizationKernelExecs": smSiaSystemUtilizationKernelExecs,
       "smSiaSystemUtilizationKernelRunQueue": smSiaSystemUtilizationKernelRunQueue,
       "smSiaSystemUtilizationKernelSwapQueue": smSiaSystemUtilizationKernelSwapQueue,
       "smSiaSystemUtilizationKernelSemaphores": smSiaSystemUtilizationKernelSemaphores,
       "smSiaSystemUtilizationKernelMessages": smSiaSystemUtilizationKernelMessages,
       "smSiaSystemUtilizationKernelProcessOverflow": smSiaSystemUtilizationKernelProcessOverflow,
       "smSiaSystemUtilizationKernelBytesRead": smSiaSystemUtilizationKernelBytesRead,
       "smSiaSystemUtilizationKernelBytesWritten": smSiaSystemUtilizationKernelBytesWritten,
       "smSiaSystemUtilizationKernelRawTTYOut": smSiaSystemUtilizationKernelRawTTYOut,
       "smSiaSystemUtilizationKernelContextSwitchesMinimum": smSiaSystemUtilizationKernelContextSwitchesMinimum,
       "smSiaSystemUtilizationKernelSystemCallsMinimum": smSiaSystemUtilizationKernelSystemCallsMinimum,
       "smSiaSystemUtilizationKernelSystemReadsMinimum": smSiaSystemUtilizationKernelSystemReadsMinimum,
       "smSiaSystemUtilizationKernelSystemWritesMinimum": smSiaSystemUtilizationKernelSystemWritesMinimum,
       "smSiaSystemUtilizationKernelForksMinimum": smSiaSystemUtilizationKernelForksMinimum,
       "smSiaSystemUtilizationKernelExecsMinimum": smSiaSystemUtilizationKernelExecsMinimum,
       "smSiaSystemUtilizationKernelRunQueueMinimum": smSiaSystemUtilizationKernelRunQueueMinimum,
       "smSiaSystemUtilizationKernelSwapQueueMinimum": smSiaSystemUtilizationKernelSwapQueueMinimum,
       "smSiaSystemUtilizationKernelSemaphoresMinimum": smSiaSystemUtilizationKernelSemaphoresMinimum,
       "smSiaSystemUtilizationKernelMessagesMinimum": smSiaSystemUtilizationKernelMessagesMinimum,
       "smSiaSystemUtilizationKernelProcessOverflowMinimum": smSiaSystemUtilizationKernelProcessOverflowMinimum,
       "smSiaSystemUtilizationKernelBytesReadMinimum": smSiaSystemUtilizationKernelBytesReadMinimum,
       "smSiaSystemUtilizationKernelBytesWrittenMinimum": smSiaSystemUtilizationKernelBytesWrittenMinimum,
       "smSiaSystemUtilizationKernelRawTTYOutMinimum": smSiaSystemUtilizationKernelRawTTYOutMinimum,
       "smSiaSystemUtilizationKernelContextSwitchesMaximum": smSiaSystemUtilizationKernelContextSwitchesMaximum,
       "smSiaSystemUtilizationKernelSystemCallsMaximum": smSiaSystemUtilizationKernelSystemCallsMaximum,
       "smSiaSystemUtilizationKernelSystemReadsMaximum": smSiaSystemUtilizationKernelSystemReadsMaximum,
       "smSiaSystemUtilizationKernelSystemWritesMaximum": smSiaSystemUtilizationKernelSystemWritesMaximum,
       "smSiaSystemUtilizationKernelForksMaximum": smSiaSystemUtilizationKernelForksMaximum,
       "smSiaSystemUtilizationKernelExecsMaximum": smSiaSystemUtilizationKernelExecsMaximum,
       "smSiaSystemUtilizationKernelRunQueueMaximum": smSiaSystemUtilizationKernelRunQueueMaximum,
       "smSiaSystemUtilizationKernelSwapQueueMaximum": smSiaSystemUtilizationKernelSwapQueueMaximum,
       "smSiaSystemUtilizationKernelSemaphoresMaximum": smSiaSystemUtilizationKernelSemaphoresMaximum,
       "smSiaSystemUtilizationKernelMessagesMaximum": smSiaSystemUtilizationKernelMessagesMaximum,
       "smSiaSystemUtilizationKernelProcessOverflowMaximum": smSiaSystemUtilizationKernelProcessOverflowMaximum,
       "smSiaSystemUtilizationKernelBytesReadMaximum": smSiaSystemUtilizationKernelBytesReadMaximum,
       "smSiaSystemUtilizationKernelBytesWrittenMaximum": smSiaSystemUtilizationKernelBytesWrittenMaximum,
       "smSiaSystemUtilizationKernelRawTTYOutMaximum": smSiaSystemUtilizationKernelRawTTYOutMaximum,
       "smSiaSystemUtilizationIostat": smSiaSystemUtilizationIostat,
       "smSiaSystemUtilizationIostatPollingInterval": smSiaSystemUtilizationIostatPollingInterval,
       "smSiaSystemUtilizationIostatTable": smSiaSystemUtilizationIostatTable,
       "smSiaSystemUtilizationIostatEntry": smSiaSystemUtilizationIostatEntry,
       "smSiaSystemUtilizationIostatName": smSiaSystemUtilizationIostatName,
       "smSiaSystemUtilizationIostatIntervalStartTime": smSiaSystemUtilizationIostatIntervalStartTime,
       "smSiaSystemUtilizationIostatIntervalLength": smSiaSystemUtilizationIostatIntervalLength,
       "smSiaSystemUtilizationIostatPercentTimeActive": smSiaSystemUtilizationIostatPercentTimeActive,
       "smSiaSystemUtilizationIostatKilobytesTransferRate": smSiaSystemUtilizationIostatKilobytesTransferRate,
       "smSiaSystemUtilizationIostatTransfers": smSiaSystemUtilizationIostatTransfers,
       "smSiaSystemUtilizationIostatKilobytesRead": smSiaSystemUtilizationIostatKilobytesRead,
       "smSiaSystemUtilizationIostatKilobytesWritten": smSiaSystemUtilizationIostatKilobytesWritten,
       "smSiaSystemUtilizationIostatPercentTimeActiveMinimum": smSiaSystemUtilizationIostatPercentTimeActiveMinimum,
       "smSiaSystemUtilizationIostatKilobytesTransferRateMinimum": smSiaSystemUtilizationIostatKilobytesTransferRateMinimum,
       "smSiaSystemUtilizationIostatTransfersMinimum": smSiaSystemUtilizationIostatTransfersMinimum,
       "smSiaSystemUtilizationIostatKilobytesReadMinimum": smSiaSystemUtilizationIostatKilobytesReadMinimum,
       "smSiaSystemUtilizationIostatKilobytesWrittenMinimum": smSiaSystemUtilizationIostatKilobytesWrittenMinimum,
       "smSiaSystemUtilizationIostatPercentTimeActiveMaximum": smSiaSystemUtilizationIostatPercentTimeActiveMaximum,
       "smSiaSystemUtilizationIostatKilobytesTransferRateMaximum": smSiaSystemUtilizationIostatKilobytesTransferRateMaximum,
       "smSiaSystemUtilizationIostatTransfersMaximum": smSiaSystemUtilizationIostatTransfersMaximum,
       "smSiaSystemUtilizationIostatKilobytesReadMaximum": smSiaSystemUtilizationIostatKilobytesReadMaximum,
       "smSiaSystemUtilizationIostatKilobytesWrittenMaximum": smSiaSystemUtilizationIostatKilobytesWrittenMaximum,
       "smSiaSystemMiscellaneous": smSiaSystemMiscellaneous,
       "smSiaSystemMiscellaneousTimeText": smSiaSystemMiscellaneousTimeText,
       "smSiaSystemMiscellaneousTime": smSiaSystemMiscellaneousTime,
       "smSiaSystemMiscellaneousRandom": smSiaSystemMiscellaneousRandom,
       "smSiaSystemMiscellaneousFreeSpace": smSiaSystemMiscellaneousFreeSpace,
       "smSiaSystemMiscellaneousPublicKey": smSiaSystemMiscellaneousPublicKey,
       "smSiaSystemMiscellaneousLocalSocket": smSiaSystemMiscellaneousLocalSocket,
       "smSiaCommand": smSiaCommand,
       "smSiaCommandTable": smSiaCommandTable,
       "smSiaCommandEntry": smSiaCommandEntry,
       "smSiaCommandState": smSiaCommandState,
       "smSiaCommandName": smSiaCommandName,
       "smSiaCommandDescription": smSiaCommandDescription,
       "smSiaCommandOwnerID": smSiaCommandOwnerID,
       "smSiaCommandGetStringAndParameters": smSiaCommandGetStringAndParameters,
       "smSiaCommandSetStringAndParameters": smSiaCommandSetStringAndParameters,
       "smSiaCommandTimeOutValue": smSiaCommandTimeOutValue,
       "smSiaCommandCountToLive": smSiaCommandCountToLive,
       "smSiaCommandTimeToLive": smSiaCommandTimeToLive,
       "smSiaCommandOutputResultIndex": smSiaCommandOutputResultIndex,
       "smSiaCommandOutputRowIndex": smSiaCommandOutputRowIndex,
       "smSiaCommandOutputColumnIndex": smSiaCommandOutputColumnIndex,
       "smSiaCommandDisplayStringResult": smSiaCommandDisplayStringResult,
       "smSiaCommandIntegerResult": smSiaCommandIntegerResult,
       "smSiaCommandCounterResult": smSiaCommandCounterResult,
       "smSiaCommandGaugeResult": smSiaCommandGaugeResult,
       "smSiaCommandExecutionReturnCode": smSiaCommandExecutionReturnCode,
       "smSiaCommandStandardError": smSiaCommandStandardError,
       "smSiaAdministration": smSiaAdministration,
       "smSiaAdministrationTable": smSiaAdministrationTable,
       "smSiaAdministrationEntry": smSiaAdministrationEntry,
       "smSiaAdministrationFieldState": smSiaAdministrationFieldState,
       "smSiaAdministrationFieldName": smSiaAdministrationFieldName,
       "smSiaAdministrationFieldOwner": smSiaAdministrationFieldOwner,
       "smSiaAdministrationFieldDescription": smSiaAdministrationFieldDescription,
       "smSiaAdministrationFieldValue": smSiaAdministrationFieldValue,
       "smSiaFileMonitor": smSiaFileMonitor,
       "smSiaFileMonitorTable": smSiaFileMonitorTable,
       "smSiaFileMonitorEntry": smSiaFileMonitorEntry,
       "smSiaFileMonitorState": smSiaFileMonitorState,
       "smSiaFileMonitorName": smSiaFileMonitorName,
       "smSiaFileMonitorType": smSiaFileMonitorType,
       "smSiaFileMonitorTrapState": smSiaFileMonitorTrapState,
       "smSiaFileMonitorCaseState": smSiaFileMonitorCaseState,
       "smSiaFileMonitorDescription": smSiaFileMonitorDescription,
       "smSiaFileMonitorOwnerID": smSiaFileMonitorOwnerID,
       "smSiaFileMonitorFullPathName": smSiaFileMonitorFullPathName,
       "smSiaFileMonitorForString": smSiaFileMonitorForString,
       "smSiaFileMonitorActivationState": smSiaFileMonitorActivationState,
       "smSiaFileMonitorActivationTime": smSiaFileMonitorActivationTime,
       "smSiaFileMonitorActivationDayOfWeek": smSiaFileMonitorActivationDayOfWeek,
       "smSiaFileMonitorDeactivationTime": smSiaFileMonitorDeactivationTime,
       "smSiaFileMonitorDeactivationDayOfWeek": smSiaFileMonitorDeactivationDayOfWeek,
       "smSiaFileMonitorPollTime": smSiaFileMonitorPollTime,
       "smSiaFileMonitorResetToStartOfFile": smSiaFileMonitorResetToStartOfFile,
       "smSiaFileMonitorCurrentLineCountOfFile": smSiaFileMonitorCurrentLineCountOfFile,
       "smSiaFileMonitorFoundStringCount": smSiaFileMonitorFoundStringCount,
       "smSiaFileMonitorStringFound": smSiaFileMonitorStringFound,
       "smSiaFileMonitorFoundStringAtLineNumber": smSiaFileMonitorFoundStringAtLineNumber,
       "smSiaFileMonitorBytePositionWithinLine": smSiaFileMonitorBytePositionWithinLine,
       "smSiaFileMonitorCompleteLineStringFound": smSiaFileMonitorCompleteLineStringFound,
       "smSiaFileMonitorFoundStringBytePositionWithinFile": smSiaFileMonitorFoundStringBytePositionWithinFile,
       "smSiaFileMonitorTimeLastFound": smSiaFileMonitorTimeLastFound,
       "smSiaFileMonitorCommandToExecuteTypeMet": smSiaFileMonitorCommandToExecuteTypeMet,
       "smSiaFileMonitorCommandToExecuteBeforeMonitor": smSiaFileMonitorCommandToExecuteBeforeMonitor,
       "smSiaFileMonitorMode": smSiaFileMonitorMode,
       "smSiaFileMonitorUserID": smSiaFileMonitorUserID,
       "smSiaFileMonitorGroupID": smSiaFileMonitorGroupID,
       "smSiaFileMonitorSize": smSiaFileMonitorSize,
       "smSiaFileMonitorTimeLastDataModification": smSiaFileMonitorTimeLastDataModification,
       "smSiaFileMonitorTimeLastFileStatusChange": smSiaFileMonitorTimeLastFileStatusChange,
       "smSiaFileMonitorReturnCode": smSiaFileMonitorReturnCode,
       "smSiaFileMonitorMessages": smSiaFileMonitorMessages}
)
