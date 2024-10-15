# SNMP MIB module (SYSMON6K-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSMON6K-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:14 2024
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
_Sm6kProgramInformation_ObjectIdentity = ObjectIdentity
sm6kProgramInformation = _Sm6kProgramInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1)
)
_Sm6kProgramData_ObjectIdentity = ObjectIdentity
sm6kProgramData = _Sm6kProgramData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1)
)
_Sm6kProgramDescription_ObjectIdentity = ObjectIdentity
sm6kProgramDescription = _Sm6kProgramDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1)
)
_Sm6kProgramName_Type = DisplayString
_Sm6kProgramName_Object = MibScalar
sm6kProgramName = _Sm6kProgramName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 1),
    _Sm6kProgramName_Type()
)
sm6kProgramName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramName.setStatus("mandatory")
_Sm6kProgramNumber_Type = DisplayString
_Sm6kProgramNumber_Object = MibScalar
sm6kProgramNumber = _Sm6kProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 2),
    _Sm6kProgramNumber_Type()
)
sm6kProgramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramNumber.setStatus("mandatory")
_Sm6kProgramVersion_Type = DisplayString
_Sm6kProgramVersion_Object = MibScalar
sm6kProgramVersion = _Sm6kProgramVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 3),
    _Sm6kProgramVersion_Type()
)
sm6kProgramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramVersion.setStatus("mandatory")
_Sm6kProgramCompilationDate_Type = DisplayString
_Sm6kProgramCompilationDate_Object = MibScalar
sm6kProgramCompilationDate = _Sm6kProgramCompilationDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 4),
    _Sm6kProgramCompilationDate_Type()
)
sm6kProgramCompilationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramCompilationDate.setStatus("mandatory")
_Sm6kProgramUpTime_Type = TimeTicks
_Sm6kProgramUpTime_Object = MibScalar
sm6kProgramUpTime = _Sm6kProgramUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 5),
    _Sm6kProgramUpTime_Type()
)
sm6kProgramUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramUpTime.setStatus("mandatory")


class _Sm6kProgramContact_Type(DisplayString):
    """Custom type sm6kProgramContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Sm6kProgramContact_Type.__name__ = "DisplayString"
_Sm6kProgramContact_Object = MibScalar
sm6kProgramContact = _Sm6kProgramContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 6),
    _Sm6kProgramContact_Type()
)
sm6kProgramContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramContact.setStatus("mandatory")
_Sm6kProgramControl_ObjectIdentity = ObjectIdentity
sm6kProgramControl = _Sm6kProgramControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2)
)
_Sm6kProgramControlLocalConfigurationFile_Type = DisplayString
_Sm6kProgramControlLocalConfigurationFile_Object = MibScalar
sm6kProgramControlLocalConfigurationFile = _Sm6kProgramControlLocalConfigurationFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 1),
    _Sm6kProgramControlLocalConfigurationFile_Type()
)
sm6kProgramControlLocalConfigurationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlLocalConfigurationFile.setStatus("mandatory")
_Sm6kProgramControlReInitializeMonitor_Type = DisplayString
_Sm6kProgramControlReInitializeMonitor_Object = MibScalar
sm6kProgramControlReInitializeMonitor = _Sm6kProgramControlReInitializeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 2),
    _Sm6kProgramControlReInitializeMonitor_Type()
)
sm6kProgramControlReInitializeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlReInitializeMonitor.setStatus("mandatory")
_Sm6kProgramControlNonForkCacheTime_Type = Integer32
_Sm6kProgramControlNonForkCacheTime_Object = MibScalar
sm6kProgramControlNonForkCacheTime = _Sm6kProgramControlNonForkCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 3),
    _Sm6kProgramControlNonForkCacheTime_Type()
)
sm6kProgramControlNonForkCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlNonForkCacheTime.setStatus("mandatory")
_Sm6kProgramControlForkCacheTime_Type = Integer32
_Sm6kProgramControlForkCacheTime_Object = MibScalar
sm6kProgramControlForkCacheTime = _Sm6kProgramControlForkCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 4),
    _Sm6kProgramControlForkCacheTime_Type()
)
sm6kProgramControlForkCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlForkCacheTime.setStatus("mandatory")
_Sm6kProgramControlPercentMultiplier_Type = Integer32
_Sm6kProgramControlPercentMultiplier_Object = MibScalar
sm6kProgramControlPercentMultiplier = _Sm6kProgramControlPercentMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 5),
    _Sm6kProgramControlPercentMultiplier_Type()
)
sm6kProgramControlPercentMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlPercentMultiplier.setStatus("mandatory")
_Sm6kProgramControlPollTime_Type = Integer32
_Sm6kProgramControlPollTime_Object = MibScalar
sm6kProgramControlPollTime = _Sm6kProgramControlPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 6),
    _Sm6kProgramControlPollTime_Type()
)
sm6kProgramControlPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlPollTime.setStatus("mandatory")
_Sm6kProgramControlFlags_Type = Integer32
_Sm6kProgramControlFlags_Object = MibScalar
sm6kProgramControlFlags = _Sm6kProgramControlFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 7),
    _Sm6kProgramControlFlags_Type()
)
sm6kProgramControlFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlFlags.setStatus("mandatory")
_Sm6kProgramRetryCount_Type = Integer32
_Sm6kProgramRetryCount_Object = MibScalar
sm6kProgramRetryCount = _Sm6kProgramRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 8),
    _Sm6kProgramRetryCount_Type()
)
sm6kProgramRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramRetryCount.setStatus("mandatory")
_Sm6kProgramTimeout_Type = TimeTicks
_Sm6kProgramTimeout_Object = MibScalar
sm6kProgramTimeout = _Sm6kProgramTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 9),
    _Sm6kProgramTimeout_Type()
)
sm6kProgramTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramTimeout.setStatus("mandatory")
_Sm6kProgramLog_ObjectIdentity = ObjectIdentity
sm6kProgramLog = _Sm6kProgramLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3)
)
_Sm6kProgramLogFileName_Type = DisplayString
_Sm6kProgramLogFileName_Object = MibScalar
sm6kProgramLogFileName = _Sm6kProgramLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 1),
    _Sm6kProgramLogFileName_Type()
)
sm6kProgramLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramLogFileName.setStatus("mandatory")
_Sm6kProgramLogFileSize_Type = Integer32
_Sm6kProgramLogFileSize_Object = MibScalar
sm6kProgramLogFileSize = _Sm6kProgramLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 2),
    _Sm6kProgramLogFileSize_Type()
)
sm6kProgramLogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramLogFileSize.setStatus("mandatory")
_Sm6kProgramLogMaxFileSize_Type = Integer32
_Sm6kProgramLogMaxFileSize_Object = MibScalar
sm6kProgramLogMaxFileSize = _Sm6kProgramLogMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 3),
    _Sm6kProgramLogMaxFileSize_Type()
)
sm6kProgramLogMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramLogMaxFileSize.setStatus("mandatory")
_Sm6kProgramLogNumFiles_Type = Integer32
_Sm6kProgramLogNumFiles_Object = MibScalar
sm6kProgramLogNumFiles = _Sm6kProgramLogNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 4),
    _Sm6kProgramLogNumFiles_Type()
)
sm6kProgramLogNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramLogNumFiles.setStatus("mandatory")


class _Sm6kProgramLogFileBehavior_Type(Integer32):
    """Custom type sm6kProgramLogFileBehavior based on Integer32"""
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


_Sm6kProgramLogFileBehavior_Type.__name__ = "Integer32"
_Sm6kProgramLogFileBehavior_Object = MibScalar
sm6kProgramLogFileBehavior = _Sm6kProgramLogFileBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 5),
    _Sm6kProgramLogFileBehavior_Type()
)
sm6kProgramLogFileBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramLogFileBehavior.setStatus("mandatory")
_Sm6kProgramLogMask_Type = DisplayString
_Sm6kProgramLogMask_Object = MibScalar
sm6kProgramLogMask = _Sm6kProgramLogMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 6),
    _Sm6kProgramLogMask_Type()
)
sm6kProgramLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramLogMask.setStatus("mandatory")
_Sm6kProgramDataCollection_ObjectIdentity = ObjectIdentity
sm6kProgramDataCollection = _Sm6kProgramDataCollection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4)
)
_Sm6kProgramDataCollectionFileName_Type = DisplayString
_Sm6kProgramDataCollectionFileName_Object = MibScalar
sm6kProgramDataCollectionFileName = _Sm6kProgramDataCollectionFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 1),
    _Sm6kProgramDataCollectionFileName_Type()
)
sm6kProgramDataCollectionFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramDataCollectionFileName.setStatus("mandatory")
_Sm6kProgramDataCollectionFileSize_Type = Integer32
_Sm6kProgramDataCollectionFileSize_Object = MibScalar
sm6kProgramDataCollectionFileSize = _Sm6kProgramDataCollectionFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 2),
    _Sm6kProgramDataCollectionFileSize_Type()
)
sm6kProgramDataCollectionFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramDataCollectionFileSize.setStatus("mandatory")
_Sm6kProgramDataCollectionMaxFileSize_Type = Integer32
_Sm6kProgramDataCollectionMaxFileSize_Object = MibScalar
sm6kProgramDataCollectionMaxFileSize = _Sm6kProgramDataCollectionMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 3),
    _Sm6kProgramDataCollectionMaxFileSize_Type()
)
sm6kProgramDataCollectionMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramDataCollectionMaxFileSize.setStatus("mandatory")
_Sm6kProgramDataCollectionNumFiles_Type = Integer32
_Sm6kProgramDataCollectionNumFiles_Object = MibScalar
sm6kProgramDataCollectionNumFiles = _Sm6kProgramDataCollectionNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 4),
    _Sm6kProgramDataCollectionNumFiles_Type()
)
sm6kProgramDataCollectionNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramDataCollectionNumFiles.setStatus("mandatory")


class _Sm6kProgramDataCollectionFileBehavior_Type(Integer32):
    """Custom type sm6kProgramDataCollectionFileBehavior based on Integer32"""
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


_Sm6kProgramDataCollectionFileBehavior_Type.__name__ = "Integer32"
_Sm6kProgramDataCollectionFileBehavior_Object = MibScalar
sm6kProgramDataCollectionFileBehavior = _Sm6kProgramDataCollectionFileBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 5),
    _Sm6kProgramDataCollectionFileBehavior_Type()
)
sm6kProgramDataCollectionFileBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramDataCollectionFileBehavior.setStatus("mandatory")
_Sm6kProgramSetableTestObjects_ObjectIdentity = ObjectIdentity
sm6kProgramSetableTestObjects = _Sm6kProgramSetableTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5)
)
_Sm6kProgramControlSetableInteger_Type = Integer32
_Sm6kProgramControlSetableInteger_Object = MibScalar
sm6kProgramControlSetableInteger = _Sm6kProgramControlSetableInteger_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 1),
    _Sm6kProgramControlSetableInteger_Type()
)
sm6kProgramControlSetableInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlSetableInteger.setStatus("mandatory")
_Sm6kProgramControlSetableCounter_Type = Counter32
_Sm6kProgramControlSetableCounter_Object = MibScalar
sm6kProgramControlSetableCounter = _Sm6kProgramControlSetableCounter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 2),
    _Sm6kProgramControlSetableCounter_Type()
)
sm6kProgramControlSetableCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlSetableCounter.setStatus("mandatory")
_Sm6kProgramControlSetableGauge_Type = Gauge32
_Sm6kProgramControlSetableGauge_Object = MibScalar
sm6kProgramControlSetableGauge = _Sm6kProgramControlSetableGauge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 3),
    _Sm6kProgramControlSetableGauge_Type()
)
sm6kProgramControlSetableGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlSetableGauge.setStatus("mandatory")
_Sm6kProgramControlSetableIpAddress_Type = IpAddress
_Sm6kProgramControlSetableIpAddress_Object = MibScalar
sm6kProgramControlSetableIpAddress = _Sm6kProgramControlSetableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 4),
    _Sm6kProgramControlSetableIpAddress_Type()
)
sm6kProgramControlSetableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlSetableIpAddress.setStatus("mandatory")
_Sm6kProgramControlSetableTimeTicks_Type = TimeTicks
_Sm6kProgramControlSetableTimeTicks_Object = MibScalar
sm6kProgramControlSetableTimeTicks = _Sm6kProgramControlSetableTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 5),
    _Sm6kProgramControlSetableTimeTicks_Type()
)
sm6kProgramControlSetableTimeTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlSetableTimeTicks.setStatus("mandatory")
_Sm6kProgramControlSetableOctetString_Type = DisplayString
_Sm6kProgramControlSetableOctetString_Object = MibScalar
sm6kProgramControlSetableOctetString = _Sm6kProgramControlSetableOctetString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 6),
    _Sm6kProgramControlSetableOctetString_Type()
)
sm6kProgramControlSetableOctetString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kProgramControlSetableOctetString.setStatus("mandatory")
_Sm6kResourceUsage_ObjectIdentity = ObjectIdentity
sm6kResourceUsage = _Sm6kResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2)
)
_Sm6kResourceUsageTable_Object = MibTable
sm6kResourceUsageTable = _Sm6kResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sm6kResourceUsageTable.setStatus("mandatory")
_Sm6kResourceUsageEntry_Object = MibTableRow
sm6kResourceUsageEntry = _Sm6kResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1)
)
sm6kResourceUsageEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kResourceUsageName"),
)
if mibBuilder.loadTexts:
    sm6kResourceUsageEntry.setStatus("mandatory")
_Sm6kResourceUsageName_Type = DisplayString
_Sm6kResourceUsageName_Object = MibTableColumn
sm6kResourceUsageName = _Sm6kResourceUsageName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 1),
    _Sm6kResourceUsageName_Type()
)
sm6kResourceUsageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageName.setStatus("mandatory")
_Sm6kResourceUsageUserTime_Type = TimeTicks
_Sm6kResourceUsageUserTime_Object = MibTableColumn
sm6kResourceUsageUserTime = _Sm6kResourceUsageUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 2),
    _Sm6kResourceUsageUserTime_Type()
)
sm6kResourceUsageUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageUserTime.setStatus("mandatory")
_Sm6kResourceUsageSystemTime_Type = TimeTicks
_Sm6kResourceUsageSystemTime_Object = MibTableColumn
sm6kResourceUsageSystemTime = _Sm6kResourceUsageSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 3),
    _Sm6kResourceUsageSystemTime_Type()
)
sm6kResourceUsageSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageSystemTime.setStatus("mandatory")
_Sm6kResourceUsageTotalTime_Type = TimeTicks
_Sm6kResourceUsageTotalTime_Object = MibTableColumn
sm6kResourceUsageTotalTime = _Sm6kResourceUsageTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 4),
    _Sm6kResourceUsageTotalTime_Type()
)
sm6kResourceUsageTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageTotalTime.setStatus("mandatory")
_Sm6kResourceUsageMaxrss_Type = Counter32
_Sm6kResourceUsageMaxrss_Object = MibTableColumn
sm6kResourceUsageMaxrss = _Sm6kResourceUsageMaxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 5),
    _Sm6kResourceUsageMaxrss_Type()
)
sm6kResourceUsageMaxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageMaxrss.setStatus("mandatory")
_Sm6kResourceUsageIxrss_Type = Counter32
_Sm6kResourceUsageIxrss_Object = MibTableColumn
sm6kResourceUsageIxrss = _Sm6kResourceUsageIxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 6),
    _Sm6kResourceUsageIxrss_Type()
)
sm6kResourceUsageIxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageIxrss.setStatus("mandatory")
_Sm6kResourceUsageIdrss_Type = Counter32
_Sm6kResourceUsageIdrss_Object = MibTableColumn
sm6kResourceUsageIdrss = _Sm6kResourceUsageIdrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 7),
    _Sm6kResourceUsageIdrss_Type()
)
sm6kResourceUsageIdrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageIdrss.setStatus("mandatory")
_Sm6kResourceUsageIsrss_Type = Counter32
_Sm6kResourceUsageIsrss_Object = MibTableColumn
sm6kResourceUsageIsrss = _Sm6kResourceUsageIsrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 8),
    _Sm6kResourceUsageIsrss_Type()
)
sm6kResourceUsageIsrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageIsrss.setStatus("mandatory")
_Sm6kResourceUsageMinflt_Type = Counter32
_Sm6kResourceUsageMinflt_Object = MibTableColumn
sm6kResourceUsageMinflt = _Sm6kResourceUsageMinflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 9),
    _Sm6kResourceUsageMinflt_Type()
)
sm6kResourceUsageMinflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageMinflt.setStatus("mandatory")
_Sm6kResourceUsageMajflt_Type = Counter32
_Sm6kResourceUsageMajflt_Object = MibTableColumn
sm6kResourceUsageMajflt = _Sm6kResourceUsageMajflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 10),
    _Sm6kResourceUsageMajflt_Type()
)
sm6kResourceUsageMajflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageMajflt.setStatus("mandatory")
_Sm6kResourceUsageNSwap_Type = Counter32
_Sm6kResourceUsageNSwap_Object = MibTableColumn
sm6kResourceUsageNSwap = _Sm6kResourceUsageNSwap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 11),
    _Sm6kResourceUsageNSwap_Type()
)
sm6kResourceUsageNSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageNSwap.setStatus("mandatory")
_Sm6kResourceUsageInBlock_Type = Counter32
_Sm6kResourceUsageInBlock_Object = MibTableColumn
sm6kResourceUsageInBlock = _Sm6kResourceUsageInBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 12),
    _Sm6kResourceUsageInBlock_Type()
)
sm6kResourceUsageInBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageInBlock.setStatus("mandatory")
_Sm6kResourceUsageOutBlock_Type = Counter32
_Sm6kResourceUsageOutBlock_Object = MibTableColumn
sm6kResourceUsageOutBlock = _Sm6kResourceUsageOutBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 13),
    _Sm6kResourceUsageOutBlock_Type()
)
sm6kResourceUsageOutBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageOutBlock.setStatus("mandatory")
_Sm6kResourceUsageMsgsnd_Type = Counter32
_Sm6kResourceUsageMsgsnd_Object = MibTableColumn
sm6kResourceUsageMsgsnd = _Sm6kResourceUsageMsgsnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 14),
    _Sm6kResourceUsageMsgsnd_Type()
)
sm6kResourceUsageMsgsnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageMsgsnd.setStatus("mandatory")
_Sm6kResourceUsageMsgrcv_Type = Counter32
_Sm6kResourceUsageMsgrcv_Object = MibTableColumn
sm6kResourceUsageMsgrcv = _Sm6kResourceUsageMsgrcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 15),
    _Sm6kResourceUsageMsgrcv_Type()
)
sm6kResourceUsageMsgrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageMsgrcv.setStatus("mandatory")
_Sm6kResourceUsageNSignals_Type = Counter32
_Sm6kResourceUsageNSignals_Object = MibTableColumn
sm6kResourceUsageNSignals = _Sm6kResourceUsageNSignals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 16),
    _Sm6kResourceUsageNSignals_Type()
)
sm6kResourceUsageNSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageNSignals.setStatus("mandatory")
_Sm6kResourceUsageVcsw_Type = Counter32
_Sm6kResourceUsageVcsw_Object = MibTableColumn
sm6kResourceUsageVcsw = _Sm6kResourceUsageVcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 17),
    _Sm6kResourceUsageVcsw_Type()
)
sm6kResourceUsageVcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageVcsw.setStatus("mandatory")
_Sm6kResourceUsageIcsw_Type = Counter32
_Sm6kResourceUsageIcsw_Object = MibTableColumn
sm6kResourceUsageIcsw = _Sm6kResourceUsageIcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 18),
    _Sm6kResourceUsageIcsw_Type()
)
sm6kResourceUsageIcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kResourceUsageIcsw.setStatus("mandatory")
_Sm6kProgramMessages_ObjectIdentity = ObjectIdentity
sm6kProgramMessages = _Sm6kProgramMessages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3)
)
_Sm6kProgramMessagesTable_Object = MibTable
sm6kProgramMessagesTable = _Sm6kProgramMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sm6kProgramMessagesTable.setStatus("mandatory")
_Sm6kProgramMessagesEntry_Object = MibTableRow
sm6kProgramMessagesEntry = _Sm6kProgramMessagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1)
)
sm6kProgramMessagesEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kProgramMessagesRowNumber"),
)
if mibBuilder.loadTexts:
    sm6kProgramMessagesEntry.setStatus("mandatory")
_Sm6kProgramMessagesRowNumber_Type = Integer32
_Sm6kProgramMessagesRowNumber_Object = MibTableColumn
sm6kProgramMessagesRowNumber = _Sm6kProgramMessagesRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 1),
    _Sm6kProgramMessagesRowNumber_Type()
)
sm6kProgramMessagesRowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramMessagesRowNumber.setStatus("mandatory")
_Sm6kProgramMessagesTime_Type = DisplayString
_Sm6kProgramMessagesTime_Object = MibTableColumn
sm6kProgramMessagesTime = _Sm6kProgramMessagesTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 2),
    _Sm6kProgramMessagesTime_Type()
)
sm6kProgramMessagesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramMessagesTime.setStatus("mandatory")
_Sm6kProgramMessagesText_Type = DisplayString
_Sm6kProgramMessagesText_Object = MibTableColumn
sm6kProgramMessagesText = _Sm6kProgramMessagesText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 3),
    _Sm6kProgramMessagesText_Type()
)
sm6kProgramMessagesText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramMessagesText.setStatus("mandatory")
_Sm6kProgramMessagesTimeStamp_Type = Integer32
_Sm6kProgramMessagesTimeStamp_Object = MibTableColumn
sm6kProgramMessagesTimeStamp = _Sm6kProgramMessagesTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 4),
    _Sm6kProgramMessagesTimeStamp_Type()
)
sm6kProgramMessagesTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kProgramMessagesTimeStamp.setStatus("mandatory")
_Sm6kSystemInformation_ObjectIdentity = ObjectIdentity
sm6kSystemInformation = _Sm6kSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2)
)
_Sm6kSystemDescription_ObjectIdentity = ObjectIdentity
sm6kSystemDescription = _Sm6kSystemDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1)
)
_Sm6kSystemNodeName_Type = DisplayString
_Sm6kSystemNodeName_Object = MibScalar
sm6kSystemNodeName = _Sm6kSystemNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 1),
    _Sm6kSystemNodeName_Type()
)
sm6kSystemNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemNodeName.setStatus("mandatory")
_Sm6kSystemSysName_Type = DisplayString
_Sm6kSystemSysName_Object = MibScalar
sm6kSystemSysName = _Sm6kSystemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 2),
    _Sm6kSystemSysName_Type()
)
sm6kSystemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSysName.setStatus("mandatory")
_Sm6kSystemVersion_Type = DisplayString
_Sm6kSystemVersion_Object = MibScalar
sm6kSystemVersion = _Sm6kSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 3),
    _Sm6kSystemVersion_Type()
)
sm6kSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemVersion.setStatus("mandatory")
_Sm6kSystemRelease_Type = DisplayString
_Sm6kSystemRelease_Object = MibScalar
sm6kSystemRelease = _Sm6kSystemRelease_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 4),
    _Sm6kSystemRelease_Type()
)
sm6kSystemRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemRelease.setStatus("mandatory")
_Sm6kSystemMachine_Type = DisplayString
_Sm6kSystemMachine_Object = MibScalar
sm6kSystemMachine = _Sm6kSystemMachine_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 1, 5),
    _Sm6kSystemMachine_Type()
)
sm6kSystemMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMachine.setStatus("mandatory")
_Sm6kSystemConfiguration_ObjectIdentity = ObjectIdentity
sm6kSystemConfiguration = _Sm6kSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2)
)
_Sm6kSystemBufferPoolMark_Type = Integer32
_Sm6kSystemBufferPoolMark_Object = MibScalar
sm6kSystemBufferPoolMark = _Sm6kSystemBufferPoolMark_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 1),
    _Sm6kSystemBufferPoolMark_Type()
)
sm6kSystemBufferPoolMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemBufferPoolMark.setStatus("mandatory")
_Sm6kSystemMaxMbufs_Type = Integer32
_Sm6kSystemMaxMbufs_Object = MibScalar
sm6kSystemMaxMbufs = _Sm6kSystemMaxMbufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 2),
    _Sm6kSystemMaxMbufs_Type()
)
sm6kSystemMaxMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMaxMbufs.setStatus("mandatory")
_Sm6kSystemMaxUserProcesses_Type = Integer32
_Sm6kSystemMaxUserProcesses_Object = MibScalar
sm6kSystemMaxUserProcesses = _Sm6kSystemMaxUserProcesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 3),
    _Sm6kSystemMaxUserProcesses_Type()
)
sm6kSystemMaxUserProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMaxUserProcesses.setStatus("mandatory")
_Sm6kSystemMaxSystemProcesses_Type = Integer32
_Sm6kSystemMaxSystemProcesses_Object = MibScalar
sm6kSystemMaxSystemProcesses = _Sm6kSystemMaxSystemProcesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 4),
    _Sm6kSystemMaxSystemProcesses_Type()
)
sm6kSystemMaxSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMaxSystemProcesses.setStatus("mandatory")
_Sm6kSystemRecordLockTableSize_Type = Integer32
_Sm6kSystemRecordLockTableSize_Object = MibScalar
sm6kSystemRecordLockTableSize = _Sm6kSystemRecordLockTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 5),
    _Sm6kSystemRecordLockTableSize_Type()
)
sm6kSystemRecordLockTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemRecordLockTableSize.setStatus("mandatory")
_Sm6kSystemOpenFileTableSize_Type = Integer32
_Sm6kSystemOpenFileTableSize_Object = MibScalar
sm6kSystemOpenFileTableSize = _Sm6kSystemOpenFileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 6),
    _Sm6kSystemOpenFileTableSize_Type()
)
sm6kSystemOpenFileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemOpenFileTableSize.setStatus("mandatory")
_Sm6kSystemCBlockArraySize_Type = Integer32
_Sm6kSystemCBlockArraySize_Object = MibScalar
sm6kSystemCBlockArraySize = _Sm6kSystemCBlockArraySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 7),
    _Sm6kSystemCBlockArraySize_Type()
)
sm6kSystemCBlockArraySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemCBlockArraySize.setStatus("mandatory")


class _Sm6kSystemDiskIOHistory_Type(Integer32):
    """Custom type sm6kSystemDiskIOHistory based on Integer32"""
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


_Sm6kSystemDiskIOHistory_Type.__name__ = "Integer32"
_Sm6kSystemDiskIOHistory_Object = MibScalar
sm6kSystemDiskIOHistory = _Sm6kSystemDiskIOHistory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 8),
    _Sm6kSystemDiskIOHistory_Type()
)
sm6kSystemDiskIOHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDiskIOHistory.setStatus("mandatory")


class _Sm6kSystemAutomaticBootAfterHalt_Type(Integer32):
    """Custom type sm6kSystemAutomaticBootAfterHalt based on Integer32"""
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


_Sm6kSystemAutomaticBootAfterHalt_Type.__name__ = "Integer32"
_Sm6kSystemAutomaticBootAfterHalt_Object = MibScalar
sm6kSystemAutomaticBootAfterHalt = _Sm6kSystemAutomaticBootAfterHalt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 9),
    _Sm6kSystemAutomaticBootAfterHalt_Type()
)
sm6kSystemAutomaticBootAfterHalt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemAutomaticBootAfterHalt.setStatus("mandatory")


class _Sm6kSystemMemScrub_Type(Integer32):
    """Custom type sm6kSystemMemScrub based on Integer32"""
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


_Sm6kSystemMemScrub_Type.__name__ = "Integer32"
_Sm6kSystemMemScrub_Object = MibScalar
sm6kSystemMemScrub = _Sm6kSystemMemScrub_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 10),
    _Sm6kSystemMemScrub_Type()
)
sm6kSystemMemScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMemScrub.setStatus("mandatory")
_Sm6kSystemLeastPriv_Type = Integer32
_Sm6kSystemLeastPriv_Object = MibScalar
sm6kSystemLeastPriv = _Sm6kSystemLeastPriv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 11),
    _Sm6kSystemLeastPriv_Type()
)
sm6kSystemLeastPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemLeastPriv.setStatus("mandatory")
_Sm6kSystemMaxPout_Type = Integer32
_Sm6kSystemMaxPout_Object = MibScalar
sm6kSystemMaxPout = _Sm6kSystemMaxPout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 12),
    _Sm6kSystemMaxPout_Type()
)
sm6kSystemMaxPout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMaxPout.setStatus("mandatory")
_Sm6kSystemMinPout_Type = Integer32
_Sm6kSystemMinPout_Object = MibScalar
sm6kSystemMinPout = _Sm6kSystemMinPout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 13),
    _Sm6kSystemMinPout_Type()
)
sm6kSystemMinPout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMinPout.setStatus("mandatory")
_Sm6kSystemPageSize_Type = Integer32
_Sm6kSystemPageSize_Object = MibScalar
sm6kSystemPageSize = _Sm6kSystemPageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 14),
    _Sm6kSystemPageSize_Type()
)
sm6kSystemPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPageSize.setStatus("mandatory")
_Sm6kSystemProcessMaxOpenFiles_Type = Integer32
_Sm6kSystemProcessMaxOpenFiles_Object = MibScalar
sm6kSystemProcessMaxOpenFiles = _Sm6kSystemProcessMaxOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 15),
    _Sm6kSystemProcessMaxOpenFiles_Type()
)
sm6kSystemProcessMaxOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessMaxOpenFiles.setStatus("mandatory")
_Sm6kSystemProcessMaxOpenStreams_Type = Integer32
_Sm6kSystemProcessMaxOpenStreams_Object = MibScalar
sm6kSystemProcessMaxOpenStreams = _Sm6kSystemProcessMaxOpenStreams_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 16),
    _Sm6kSystemProcessMaxOpenStreams_Type()
)
sm6kSystemProcessMaxOpenStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessMaxOpenStreams.setStatus("mandatory")
_Sm6kSystemProcessDescriptorTableSize_Type = Integer32
_Sm6kSystemProcessDescriptorTableSize_Object = MibScalar
sm6kSystemProcessDescriptorTableSize = _Sm6kSystemProcessDescriptorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 2, 17),
    _Sm6kSystemProcessDescriptorTableSize_Type()
)
sm6kSystemProcessDescriptorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessDescriptorTableSize.setStatus("mandatory")
_Sm6kSystemDevice_ObjectIdentity = ObjectIdentity
sm6kSystemDevice = _Sm6kSystemDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3)
)
_Sm6kSystemDeviceList_ObjectIdentity = ObjectIdentity
sm6kSystemDeviceList = _Sm6kSystemDeviceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1)
)
_Sm6kSystemDeviceListInstalled_Type = Integer32
_Sm6kSystemDeviceListInstalled_Object = MibScalar
sm6kSystemDeviceListInstalled = _Sm6kSystemDeviceListInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 1),
    _Sm6kSystemDeviceListInstalled_Type()
)
sm6kSystemDeviceListInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListInstalled.setStatus("mandatory")
_Sm6kSystemDeviceListTable_Object = MibTable
sm6kSystemDeviceListTable = _Sm6kSystemDeviceListTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceListTable.setStatus("mandatory")
_Sm6kSystemDeviceListEntry_Object = MibTableRow
sm6kSystemDeviceListEntry = _Sm6kSystemDeviceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1)
)
sm6kSystemDeviceListEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemDeviceListName"),
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceListEntry.setStatus("mandatory")
_Sm6kSystemDeviceListName_Type = DisplayString
_Sm6kSystemDeviceListName_Object = MibTableColumn
sm6kSystemDeviceListName = _Sm6kSystemDeviceListName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 1),
    _Sm6kSystemDeviceListName_Type()
)
sm6kSystemDeviceListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListName.setStatus("mandatory")
_Sm6kSystemDeviceListDescription_Type = DisplayString
_Sm6kSystemDeviceListDescription_Object = MibTableColumn
sm6kSystemDeviceListDescription = _Sm6kSystemDeviceListDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 2),
    _Sm6kSystemDeviceListDescription_Type()
)
sm6kSystemDeviceListDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListDescription.setStatus("mandatory")
_Sm6kSystemDeviceListLocation_Type = DisplayString
_Sm6kSystemDeviceListLocation_Object = MibTableColumn
sm6kSystemDeviceListLocation = _Sm6kSystemDeviceListLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 3),
    _Sm6kSystemDeviceListLocation_Type()
)
sm6kSystemDeviceListLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListLocation.setStatus("mandatory")
_Sm6kSystemDeviceListVPD_Type = DisplayString
_Sm6kSystemDeviceListVPD_Object = MibTableColumn
sm6kSystemDeviceListVPD = _Sm6kSystemDeviceListVPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 4),
    _Sm6kSystemDeviceListVPD_Type()
)
sm6kSystemDeviceListVPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListVPD.setStatus("mandatory")
_Sm6kSystemDeviceListAttributes_Type = DisplayString
_Sm6kSystemDeviceListAttributes_Object = MibTableColumn
sm6kSystemDeviceListAttributes = _Sm6kSystemDeviceListAttributes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 5),
    _Sm6kSystemDeviceListAttributes_Type()
)
sm6kSystemDeviceListAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListAttributes.setStatus("mandatory")
_Sm6kSystemDeviceListDiagnostics_Type = DisplayString
_Sm6kSystemDeviceListDiagnostics_Object = MibTableColumn
sm6kSystemDeviceListDiagnostics = _Sm6kSystemDeviceListDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 1, 2, 1, 6),
    _Sm6kSystemDeviceListDiagnostics_Type()
)
sm6kSystemDeviceListDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceListDiagnostics.setStatus("mandatory")
_Sm6kSystemDeviceTokenRing_ObjectIdentity = ObjectIdentity
sm6kSystemDeviceTokenRing = _Sm6kSystemDeviceTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2)
)
_Sm6kSystemDeviceTokenRingInstalled_Type = Integer32
_Sm6kSystemDeviceTokenRingInstalled_Object = MibScalar
sm6kSystemDeviceTokenRingInstalled = _Sm6kSystemDeviceTokenRingInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 1),
    _Sm6kSystemDeviceTokenRingInstalled_Type()
)
sm6kSystemDeviceTokenRingInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingInstalled.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTable_Object = MibTable
sm6kSystemDeviceTokenRingTable = _Sm6kSystemDeviceTokenRingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTable.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingEntry_Object = MibTableRow
sm6kSystemDeviceTokenRingEntry = _Sm6kSystemDeviceTokenRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1)
)
sm6kSystemDeviceTokenRingEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemDeviceTokenRingNumber"),
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingEntry.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingNumber_Type = Integer32
_Sm6kSystemDeviceTokenRingNumber_Object = MibTableColumn
sm6kSystemDeviceTokenRingNumber = _Sm6kSystemDeviceTokenRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 1),
    _Sm6kSystemDeviceTokenRingNumber_Type()
)
sm6kSystemDeviceTokenRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingNumber.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingHardwareAddress_Type = PhysAddress
_Sm6kSystemDeviceTokenRingHardwareAddress_Object = MibTableColumn
sm6kSystemDeviceTokenRingHardwareAddress = _Sm6kSystemDeviceTokenRingHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 2),
    _Sm6kSystemDeviceTokenRingHardwareAddress_Type()
)
sm6kSystemDeviceTokenRingHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingHardwareAddress.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingCurrentAddress_Type = PhysAddress
_Sm6kSystemDeviceTokenRingCurrentAddress_Object = MibTableColumn
sm6kSystemDeviceTokenRingCurrentAddress = _Sm6kSystemDeviceTokenRingCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 3),
    _Sm6kSystemDeviceTokenRingCurrentAddress_Type()
)
sm6kSystemDeviceTokenRingCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingCurrentAddress.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingReceiveDataOffset_Type = Integer32
_Sm6kSystemDeviceTokenRingReceiveDataOffset_Object = MibTableColumn
sm6kSystemDeviceTokenRingReceiveDataOffset = _Sm6kSystemDeviceTokenRingReceiveDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 4),
    _Sm6kSystemDeviceTokenRingReceiveDataOffset_Type()
)
sm6kSystemDeviceTokenRingReceiveDataOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingReceiveDataOffset.setStatus("mandatory")


class _Sm6kSystemDeviceTokenRingBroadwrap_Type(Integer32):
    """Custom type sm6kSystemDeviceTokenRingBroadwrap based on Integer32"""
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


_Sm6kSystemDeviceTokenRingBroadwrap_Type.__name__ = "Integer32"
_Sm6kSystemDeviceTokenRingBroadwrap_Object = MibTableColumn
sm6kSystemDeviceTokenRingBroadwrap = _Sm6kSystemDeviceTokenRingBroadwrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 5),
    _Sm6kSystemDeviceTokenRingBroadwrap_Type()
)
sm6kSystemDeviceTokenRingBroadwrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingBroadwrap.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxByteMcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingTxByteMcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxByteMcnt = _Sm6kSystemDeviceTokenRingTxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 6),
    _Sm6kSystemDeviceTokenRingTxByteMcnt_Type()
)
sm6kSystemDeviceTokenRingTxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxByteMcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxByteLcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingTxByteLcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxByteLcnt = _Sm6kSystemDeviceTokenRingTxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 7),
    _Sm6kSystemDeviceTokenRingTxByteLcnt_Type()
)
sm6kSystemDeviceTokenRingTxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxByteLcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxByteMcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxByteMcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxByteMcnt = _Sm6kSystemDeviceTokenRingRxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 8),
    _Sm6kSystemDeviceTokenRingRxByteMcnt_Type()
)
sm6kSystemDeviceTokenRingRxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxByteMcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxByteLcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxByteLcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxByteLcnt = _Sm6kSystemDeviceTokenRingRxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 9),
    _Sm6kSystemDeviceTokenRingRxByteLcnt_Type()
)
sm6kSystemDeviceTokenRingRxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxByteLcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxFrameMcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingTxFrameMcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxFrameMcnt = _Sm6kSystemDeviceTokenRingTxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 10),
    _Sm6kSystemDeviceTokenRingTxFrameMcnt_Type()
)
sm6kSystemDeviceTokenRingTxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxFrameMcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxFrameLcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingTxFrameLcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxFrameLcnt = _Sm6kSystemDeviceTokenRingTxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 11),
    _Sm6kSystemDeviceTokenRingTxFrameLcnt_Type()
)
sm6kSystemDeviceTokenRingTxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxFrameLcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxFrameMcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxFrameMcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxFrameMcnt = _Sm6kSystemDeviceTokenRingRxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 12),
    _Sm6kSystemDeviceTokenRingRxFrameMcnt_Type()
)
sm6kSystemDeviceTokenRingRxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxFrameMcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxFrameLcnt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxFrameLcnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxFrameLcnt = _Sm6kSystemDeviceTokenRingRxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 13),
    _Sm6kSystemDeviceTokenRingRxFrameLcnt_Type()
)
sm6kSystemDeviceTokenRingRxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxFrameLcnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxErrCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingTxErrCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxErrCnt = _Sm6kSystemDeviceTokenRingTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 14),
    _Sm6kSystemDeviceTokenRingTxErrCnt_Type()
)
sm6kSystemDeviceTokenRingTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxErrCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxErrCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxErrCnt = _Sm6kSystemDeviceTokenRingRxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 15),
    _Sm6kSystemDeviceTokenRingRxErrCnt_Type()
)
sm6kSystemDeviceTokenRingRxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingNidTblHigh_Type = Integer32
_Sm6kSystemDeviceTokenRingNidTblHigh_Object = MibTableColumn
sm6kSystemDeviceTokenRingNidTblHigh = _Sm6kSystemDeviceTokenRingNidTblHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 16),
    _Sm6kSystemDeviceTokenRingNidTblHigh_Type()
)
sm6kSystemDeviceTokenRingNidTblHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingNidTblHigh.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxQueHigh_Type = Gauge32
_Sm6kSystemDeviceTokenRingTxQueHigh_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxQueHigh = _Sm6kSystemDeviceTokenRingTxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 17),
    _Sm6kSystemDeviceTokenRingTxQueHigh_Type()
)
sm6kSystemDeviceTokenRingTxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxQueHigh_Type = Gauge32
_Sm6kSystemDeviceTokenRingRxQueHigh_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxQueHigh = _Sm6kSystemDeviceTokenRingRxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 18),
    _Sm6kSystemDeviceTokenRingRxQueHigh_Type()
)
sm6kSystemDeviceTokenRingRxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingStaQueHigh_Type = Gauge32
_Sm6kSystemDeviceTokenRingStaQueHigh_Object = MibTableColumn
sm6kSystemDeviceTokenRingStaQueHigh = _Sm6kSystemDeviceTokenRingStaQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 19),
    _Sm6kSystemDeviceTokenRingStaQueHigh_Type()
)
sm6kSystemDeviceTokenRingStaQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingStaQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingIntrLost_Type = Counter32
_Sm6kSystemDeviceTokenRingIntrLost_Object = MibTableColumn
sm6kSystemDeviceTokenRingIntrLost = _Sm6kSystemDeviceTokenRingIntrLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 20),
    _Sm6kSystemDeviceTokenRingIntrLost_Type()
)
sm6kSystemDeviceTokenRingIntrLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingIntrLost.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingWdtLost_Type = Counter32
_Sm6kSystemDeviceTokenRingWdtLost_Object = MibTableColumn
sm6kSystemDeviceTokenRingWdtLost = _Sm6kSystemDeviceTokenRingWdtLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 21),
    _Sm6kSystemDeviceTokenRingWdtLost_Type()
)
sm6kSystemDeviceTokenRingWdtLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingWdtLost.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTimoLost_Type = Counter32
_Sm6kSystemDeviceTokenRingTimoLost_Object = MibTableColumn
sm6kSystemDeviceTokenRingTimoLost = _Sm6kSystemDeviceTokenRingTimoLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 22),
    _Sm6kSystemDeviceTokenRingTimoLost_Type()
)
sm6kSystemDeviceTokenRingTimoLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTimoLost.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingStaQueOverflow_Type = Counter32
_Sm6kSystemDeviceTokenRingStaQueOverflow_Object = MibTableColumn
sm6kSystemDeviceTokenRingStaQueOverflow = _Sm6kSystemDeviceTokenRingStaQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 23),
    _Sm6kSystemDeviceTokenRingStaQueOverflow_Type()
)
sm6kSystemDeviceTokenRingStaQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingStaQueOverflow.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxQueOverflow_Type = Counter32
_Sm6kSystemDeviceTokenRingRxQueOverflow_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxQueOverflow = _Sm6kSystemDeviceTokenRingRxQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 24),
    _Sm6kSystemDeviceTokenRingRxQueOverflow_Type()
)
sm6kSystemDeviceTokenRingRxQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxQueOverflow.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxQueNoMbuf_Type = Counter32
_Sm6kSystemDeviceTokenRingRxQueNoMbuf_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxQueNoMbuf = _Sm6kSystemDeviceTokenRingRxQueNoMbuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 25),
    _Sm6kSystemDeviceTokenRingRxQueNoMbuf_Type()
)
sm6kSystemDeviceTokenRingRxQueNoMbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxQueNoMbuf.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxQueNoMbufExt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxQueNoMbufExt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxQueNoMbufExt = _Sm6kSystemDeviceTokenRingRxQueNoMbufExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 26),
    _Sm6kSystemDeviceTokenRingRxQueNoMbufExt_Type()
)
sm6kSystemDeviceTokenRingRxQueNoMbufExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxQueNoMbufExt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxIntrCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingTxIntrCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxIntrCnt = _Sm6kSystemDeviceTokenRingTxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 27),
    _Sm6kSystemDeviceTokenRingTxIntrCnt_Type()
)
sm6kSystemDeviceTokenRingTxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxIntrCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRxIntrCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingRxIntrCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingRxIntrCnt = _Sm6kSystemDeviceTokenRingRxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 28),
    _Sm6kSystemDeviceTokenRingRxIntrCnt_Type()
)
sm6kSystemDeviceTokenRingRxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRxIntrCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingPktRejCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingPktRejCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingPktRejCnt = _Sm6kSystemDeviceTokenRingPktRejCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 29),
    _Sm6kSystemDeviceTokenRingPktRejCnt_Type()
)
sm6kSystemDeviceTokenRingPktRejCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingPktRejCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingPktAccCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingPktAccCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingPktAccCnt = _Sm6kSystemDeviceTokenRingPktAccCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 30),
    _Sm6kSystemDeviceTokenRingPktAccCnt_Type()
)
sm6kSystemDeviceTokenRingPktAccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingPktAccCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingPktTxCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingPktTxCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingPktTxCnt = _Sm6kSystemDeviceTokenRingPktTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 31),
    _Sm6kSystemDeviceTokenRingPktTxCnt_Type()
)
sm6kSystemDeviceTokenRingPktTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingPktTxCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingOvfloPktCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingOvfloPktCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingOvfloPktCnt = _Sm6kSystemDeviceTokenRingOvfloPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 32),
    _Sm6kSystemDeviceTokenRingOvfloPktCnt_Type()
)
sm6kSystemDeviceTokenRingOvfloPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingOvfloPktCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingPktTxErrCnt_Type = Counter32
_Sm6kSystemDeviceTokenRingPktTxErrCnt_Object = MibTableColumn
sm6kSystemDeviceTokenRingPktTxErrCnt = _Sm6kSystemDeviceTokenRingPktTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 33),
    _Sm6kSystemDeviceTokenRingPktTxErrCnt_Type()
)
sm6kSystemDeviceTokenRingPktTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingPktTxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingSpeed_Type = Integer32
_Sm6kSystemDeviceTokenRingSpeed_Object = MibTableColumn
sm6kSystemDeviceTokenRingSpeed = _Sm6kSystemDeviceTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 34),
    _Sm6kSystemDeviceTokenRingSpeed_Type()
)
sm6kSystemDeviceTokenRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingSpeed.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingVPD_Type = DisplayString
_Sm6kSystemDeviceTokenRingVPD_Object = MibTableColumn
sm6kSystemDeviceTokenRingVPD = _Sm6kSystemDeviceTokenRingVPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 35),
    _Sm6kSystemDeviceTokenRingVPD_Type()
)
sm6kSystemDeviceTokenRingVPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingVPD.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingAdapPhysAddr_Type = PhysAddress
_Sm6kSystemDeviceTokenRingAdapPhysAddr_Object = MibTableColumn
sm6kSystemDeviceTokenRingAdapPhysAddr = _Sm6kSystemDeviceTokenRingAdapPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 36),
    _Sm6kSystemDeviceTokenRingAdapPhysAddr_Type()
)
sm6kSystemDeviceTokenRingAdapPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingAdapPhysAddr.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingUpstreamNodeAddr_Type = PhysAddress
_Sm6kSystemDeviceTokenRingUpstreamNodeAddr_Object = MibTableColumn
sm6kSystemDeviceTokenRingUpstreamNodeAddr = _Sm6kSystemDeviceTokenRingUpstreamNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 37),
    _Sm6kSystemDeviceTokenRingUpstreamNodeAddr_Type()
)
sm6kSystemDeviceTokenRingUpstreamNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingUpstreamNodeAddr.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingUpstreamPhysAddr_Type = PhysAddress
_Sm6kSystemDeviceTokenRingUpstreamPhysAddr_Object = MibTableColumn
sm6kSystemDeviceTokenRingUpstreamPhysAddr = _Sm6kSystemDeviceTokenRingUpstreamPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 38),
    _Sm6kSystemDeviceTokenRingUpstreamPhysAddr_Type()
)
sm6kSystemDeviceTokenRingUpstreamPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingUpstreamPhysAddr.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingLastPollAddr_Type = PhysAddress
_Sm6kSystemDeviceTokenRingLastPollAddr_Object = MibTableColumn
sm6kSystemDeviceTokenRingLastPollAddr = _Sm6kSystemDeviceTokenRingLastPollAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 39),
    _Sm6kSystemDeviceTokenRingLastPollAddr_Type()
)
sm6kSystemDeviceTokenRingLastPollAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingLastPollAddr.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingAuthorEnv_Type = Integer32
_Sm6kSystemDeviceTokenRingAuthorEnv_Object = MibTableColumn
sm6kSystemDeviceTokenRingAuthorEnv = _Sm6kSystemDeviceTokenRingAuthorEnv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 40),
    _Sm6kSystemDeviceTokenRingAuthorEnv_Type()
)
sm6kSystemDeviceTokenRingAuthorEnv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingAuthorEnv.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingTxAccessPriority_Type = Integer32
_Sm6kSystemDeviceTokenRingTxAccessPriority_Object = MibTableColumn
sm6kSystemDeviceTokenRingTxAccessPriority = _Sm6kSystemDeviceTokenRingTxAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 41),
    _Sm6kSystemDeviceTokenRingTxAccessPriority_Type()
)
sm6kSystemDeviceTokenRingTxAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingTxAccessPriority.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingSrcClassAuthor_Type = Integer32
_Sm6kSystemDeviceTokenRingSrcClassAuthor_Object = MibTableColumn
sm6kSystemDeviceTokenRingSrcClassAuthor = _Sm6kSystemDeviceTokenRingSrcClassAuthor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 42),
    _Sm6kSystemDeviceTokenRingSrcClassAuthor_Type()
)
sm6kSystemDeviceTokenRingSrcClassAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingSrcClassAuthor.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingLastAttenCode_Type = Integer32
_Sm6kSystemDeviceTokenRingLastAttenCode_Object = MibTableColumn
sm6kSystemDeviceTokenRingLastAttenCode = _Sm6kSystemDeviceTokenRingLastAttenCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 43),
    _Sm6kSystemDeviceTokenRingLastAttenCode_Type()
)
sm6kSystemDeviceTokenRingLastAttenCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingLastAttenCode.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingLastSrcAddr_Type = PhysAddress
_Sm6kSystemDeviceTokenRingLastSrcAddr_Object = MibTableColumn
sm6kSystemDeviceTokenRingLastSrcAddr = _Sm6kSystemDeviceTokenRingLastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 44),
    _Sm6kSystemDeviceTokenRingLastSrcAddr_Type()
)
sm6kSystemDeviceTokenRingLastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingLastSrcAddr.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingLastBeaconType_Type = Integer32
_Sm6kSystemDeviceTokenRingLastBeaconType_Object = MibTableColumn
sm6kSystemDeviceTokenRingLastBeaconType = _Sm6kSystemDeviceTokenRingLastBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 45),
    _Sm6kSystemDeviceTokenRingLastBeaconType_Type()
)
sm6kSystemDeviceTokenRingLastBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingLastBeaconType.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingLastMajorVector_Type = Integer32
_Sm6kSystemDeviceTokenRingLastMajorVector_Object = MibTableColumn
sm6kSystemDeviceTokenRingLastMajorVector = _Sm6kSystemDeviceTokenRingLastMajorVector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 46),
    _Sm6kSystemDeviceTokenRingLastMajorVector_Type()
)
sm6kSystemDeviceTokenRingLastMajorVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingLastMajorVector.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingRingStatus_Type = Integer32
_Sm6kSystemDeviceTokenRingRingStatus_Object = MibTableColumn
sm6kSystemDeviceTokenRingRingStatus = _Sm6kSystemDeviceTokenRingRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 47),
    _Sm6kSystemDeviceTokenRingRingStatus_Type()
)
sm6kSystemDeviceTokenRingRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingRingStatus.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingSoftErrorTimerVal_Type = Integer32
_Sm6kSystemDeviceTokenRingSoftErrorTimerVal_Object = MibTableColumn
sm6kSystemDeviceTokenRingSoftErrorTimerVal = _Sm6kSystemDeviceTokenRingSoftErrorTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 48),
    _Sm6kSystemDeviceTokenRingSoftErrorTimerVal_Type()
)
sm6kSystemDeviceTokenRingSoftErrorTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingSoftErrorTimerVal.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingFrontEndTimerVal_Type = Integer32
_Sm6kSystemDeviceTokenRingFrontEndTimerVal_Object = MibTableColumn
sm6kSystemDeviceTokenRingFrontEndTimerVal = _Sm6kSystemDeviceTokenRingFrontEndTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 49),
    _Sm6kSystemDeviceTokenRingFrontEndTimerVal_Type()
)
sm6kSystemDeviceTokenRingFrontEndTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingFrontEndTimerVal.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingMonitorErrorCode_Type = Integer32
_Sm6kSystemDeviceTokenRingMonitorErrorCode_Object = MibTableColumn
sm6kSystemDeviceTokenRingMonitorErrorCode = _Sm6kSystemDeviceTokenRingMonitorErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 50),
    _Sm6kSystemDeviceTokenRingMonitorErrorCode_Type()
)
sm6kSystemDeviceTokenRingMonitorErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingMonitorErrorCode.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingBeaconTxType_Type = Integer32
_Sm6kSystemDeviceTokenRingBeaconTxType_Object = MibTableColumn
sm6kSystemDeviceTokenRingBeaconTxType = _Sm6kSystemDeviceTokenRingBeaconTxType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 51),
    _Sm6kSystemDeviceTokenRingBeaconTxType_Type()
)
sm6kSystemDeviceTokenRingBeaconTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingBeaconTxType.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingBeaconRxType_Type = Integer32
_Sm6kSystemDeviceTokenRingBeaconRxType_Object = MibTableColumn
sm6kSystemDeviceTokenRingBeaconRxType = _Sm6kSystemDeviceTokenRingBeaconRxType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 52),
    _Sm6kSystemDeviceTokenRingBeaconRxType_Type()
)
sm6kSystemDeviceTokenRingBeaconRxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingBeaconRxType.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingFrameCorrSave_Type = Integer32
_Sm6kSystemDeviceTokenRingFrameCorrSave_Object = MibTableColumn
sm6kSystemDeviceTokenRingFrameCorrSave = _Sm6kSystemDeviceTokenRingFrameCorrSave_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 53),
    _Sm6kSystemDeviceTokenRingFrameCorrSave_Type()
)
sm6kSystemDeviceTokenRingFrameCorrSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingFrameCorrSave.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingBeaconStationNAUN_Type = PhysAddress
_Sm6kSystemDeviceTokenRingBeaconStationNAUN_Object = MibTableColumn
sm6kSystemDeviceTokenRingBeaconStationNAUN = _Sm6kSystemDeviceTokenRingBeaconStationNAUN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 54),
    _Sm6kSystemDeviceTokenRingBeaconStationNAUN_Type()
)
sm6kSystemDeviceTokenRingBeaconStationNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingBeaconStationNAUN.setStatus("mandatory")
_Sm6kSystemDeviceTokenRingBeaconStationPhysAddr_Type = PhysAddress
_Sm6kSystemDeviceTokenRingBeaconStationPhysAddr_Object = MibTableColumn
sm6kSystemDeviceTokenRingBeaconStationPhysAddr = _Sm6kSystemDeviceTokenRingBeaconStationPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 55),
    _Sm6kSystemDeviceTokenRingBeaconStationPhysAddr_Type()
)
sm6kSystemDeviceTokenRingBeaconStationPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingBeaconStationPhysAddr.setStatus("mandatory")


class _Sm6kSystemDeviceTokenRingClear_Type(Integer32):
    """Custom type sm6kSystemDeviceTokenRingClear based on Integer32"""
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


_Sm6kSystemDeviceTokenRingClear_Type.__name__ = "Integer32"
_Sm6kSystemDeviceTokenRingClear_Object = MibTableColumn
sm6kSystemDeviceTokenRingClear = _Sm6kSystemDeviceTokenRingClear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 2, 2, 1, 56),
    _Sm6kSystemDeviceTokenRingClear_Type()
)
sm6kSystemDeviceTokenRingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kSystemDeviceTokenRingClear.setStatus("mandatory")
_Sm6kSystemDeviceEthernet_ObjectIdentity = ObjectIdentity
sm6kSystemDeviceEthernet = _Sm6kSystemDeviceEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3)
)
_Sm6kSystemDeviceEthernetInstalled_Type = Integer32
_Sm6kSystemDeviceEthernetInstalled_Object = MibScalar
sm6kSystemDeviceEthernetInstalled = _Sm6kSystemDeviceEthernetInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 1),
    _Sm6kSystemDeviceEthernetInstalled_Type()
)
sm6kSystemDeviceEthernetInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetInstalled.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTable_Object = MibTable
sm6kSystemDeviceEthernetTable = _Sm6kSystemDeviceEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTable.setStatus("mandatory")
_Sm6kSystemDeviceEthernetEntry_Object = MibTableRow
sm6kSystemDeviceEthernetEntry = _Sm6kSystemDeviceEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1)
)
sm6kSystemDeviceEthernetEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemDeviceEthernetNumber"),
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetEntry.setStatus("mandatory")
_Sm6kSystemDeviceEthernetNumber_Type = Integer32
_Sm6kSystemDeviceEthernetNumber_Object = MibTableColumn
sm6kSystemDeviceEthernetNumber = _Sm6kSystemDeviceEthernetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 1),
    _Sm6kSystemDeviceEthernetNumber_Type()
)
sm6kSystemDeviceEthernetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetNumber.setStatus("mandatory")
_Sm6kSystemDeviceEthernetHardwareAddress_Type = PhysAddress
_Sm6kSystemDeviceEthernetHardwareAddress_Object = MibTableColumn
sm6kSystemDeviceEthernetHardwareAddress = _Sm6kSystemDeviceEthernetHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 2),
    _Sm6kSystemDeviceEthernetHardwareAddress_Type()
)
sm6kSystemDeviceEthernetHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetHardwareAddress.setStatus("mandatory")
_Sm6kSystemDeviceEthernetCurrentAddress_Type = PhysAddress
_Sm6kSystemDeviceEthernetCurrentAddress_Object = MibTableColumn
sm6kSystemDeviceEthernetCurrentAddress = _Sm6kSystemDeviceEthernetCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 3),
    _Sm6kSystemDeviceEthernetCurrentAddress_Type()
)
sm6kSystemDeviceEthernetCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetCurrentAddress.setStatus("mandatory")
_Sm6kSystemDeviceEthernetReceiveDataOffset_Type = Integer32
_Sm6kSystemDeviceEthernetReceiveDataOffset_Object = MibTableColumn
sm6kSystemDeviceEthernetReceiveDataOffset = _Sm6kSystemDeviceEthernetReceiveDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 4),
    _Sm6kSystemDeviceEthernetReceiveDataOffset_Type()
)
sm6kSystemDeviceEthernetReceiveDataOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetReceiveDataOffset.setStatus("mandatory")


class _Sm6kSystemDeviceEthernetBroadwrap_Type(Integer32):
    """Custom type sm6kSystemDeviceEthernetBroadwrap based on Integer32"""
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


_Sm6kSystemDeviceEthernetBroadwrap_Type.__name__ = "Integer32"
_Sm6kSystemDeviceEthernetBroadwrap_Object = MibTableColumn
sm6kSystemDeviceEthernetBroadwrap = _Sm6kSystemDeviceEthernetBroadwrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 5),
    _Sm6kSystemDeviceEthernetBroadwrap_Type()
)
sm6kSystemDeviceEthernetBroadwrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetBroadwrap.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxByteMcnt_Type = Counter32
_Sm6kSystemDeviceEthernetTxByteMcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetTxByteMcnt = _Sm6kSystemDeviceEthernetTxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 6),
    _Sm6kSystemDeviceEthernetTxByteMcnt_Type()
)
sm6kSystemDeviceEthernetTxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxByteMcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxByteLcnt_Type = Counter32
_Sm6kSystemDeviceEthernetTxByteLcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetTxByteLcnt = _Sm6kSystemDeviceEthernetTxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 7),
    _Sm6kSystemDeviceEthernetTxByteLcnt_Type()
)
sm6kSystemDeviceEthernetTxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxByteLcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxByteMcnt_Type = Counter32
_Sm6kSystemDeviceEthernetRxByteMcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxByteMcnt = _Sm6kSystemDeviceEthernetRxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 8),
    _Sm6kSystemDeviceEthernetRxByteMcnt_Type()
)
sm6kSystemDeviceEthernetRxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxByteMcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxByteLcnt_Type = Counter32
_Sm6kSystemDeviceEthernetRxByteLcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxByteLcnt = _Sm6kSystemDeviceEthernetRxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 9),
    _Sm6kSystemDeviceEthernetRxByteLcnt_Type()
)
sm6kSystemDeviceEthernetRxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxByteLcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxFrameMcnt_Type = Counter32
_Sm6kSystemDeviceEthernetTxFrameMcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetTxFrameMcnt = _Sm6kSystemDeviceEthernetTxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 10),
    _Sm6kSystemDeviceEthernetTxFrameMcnt_Type()
)
sm6kSystemDeviceEthernetTxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxFrameMcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxFrameLcnt_Type = Counter32
_Sm6kSystemDeviceEthernetTxFrameLcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetTxFrameLcnt = _Sm6kSystemDeviceEthernetTxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 11),
    _Sm6kSystemDeviceEthernetTxFrameLcnt_Type()
)
sm6kSystemDeviceEthernetTxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxFrameLcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxFrameMcnt_Type = Counter32
_Sm6kSystemDeviceEthernetRxFrameMcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxFrameMcnt = _Sm6kSystemDeviceEthernetRxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 12),
    _Sm6kSystemDeviceEthernetRxFrameMcnt_Type()
)
sm6kSystemDeviceEthernetRxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxFrameMcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxFrameLcnt_Type = Counter32
_Sm6kSystemDeviceEthernetRxFrameLcnt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxFrameLcnt = _Sm6kSystemDeviceEthernetRxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 13),
    _Sm6kSystemDeviceEthernetRxFrameLcnt_Type()
)
sm6kSystemDeviceEthernetRxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxFrameLcnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxErrCnt_Type = Counter32
_Sm6kSystemDeviceEthernetTxErrCnt_Object = MibTableColumn
sm6kSystemDeviceEthernetTxErrCnt = _Sm6kSystemDeviceEthernetTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 14),
    _Sm6kSystemDeviceEthernetTxErrCnt_Type()
)
sm6kSystemDeviceEthernetTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxErrCnt_Type = Counter32
_Sm6kSystemDeviceEthernetRxErrCnt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxErrCnt = _Sm6kSystemDeviceEthernetRxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 15),
    _Sm6kSystemDeviceEthernetRxErrCnt_Type()
)
sm6kSystemDeviceEthernetRxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetNidTblHigh_Type = Integer32
_Sm6kSystemDeviceEthernetNidTblHigh_Object = MibTableColumn
sm6kSystemDeviceEthernetNidTblHigh = _Sm6kSystemDeviceEthernetNidTblHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 16),
    _Sm6kSystemDeviceEthernetNidTblHigh_Type()
)
sm6kSystemDeviceEthernetNidTblHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetNidTblHigh.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxQueHigh_Type = Gauge32
_Sm6kSystemDeviceEthernetTxQueHigh_Object = MibTableColumn
sm6kSystemDeviceEthernetTxQueHigh = _Sm6kSystemDeviceEthernetTxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 17),
    _Sm6kSystemDeviceEthernetTxQueHigh_Type()
)
sm6kSystemDeviceEthernetTxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxQueHigh_Type = Gauge32
_Sm6kSystemDeviceEthernetRxQueHigh_Object = MibTableColumn
sm6kSystemDeviceEthernetRxQueHigh = _Sm6kSystemDeviceEthernetRxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 18),
    _Sm6kSystemDeviceEthernetRxQueHigh_Type()
)
sm6kSystemDeviceEthernetRxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceEthernetStaQueHigh_Type = Gauge32
_Sm6kSystemDeviceEthernetStaQueHigh_Object = MibTableColumn
sm6kSystemDeviceEthernetStaQueHigh = _Sm6kSystemDeviceEthernetStaQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 19),
    _Sm6kSystemDeviceEthernetStaQueHigh_Type()
)
sm6kSystemDeviceEthernetStaQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetStaQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceEthernetIntrLost_Type = Counter32
_Sm6kSystemDeviceEthernetIntrLost_Object = MibTableColumn
sm6kSystemDeviceEthernetIntrLost = _Sm6kSystemDeviceEthernetIntrLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 20),
    _Sm6kSystemDeviceEthernetIntrLost_Type()
)
sm6kSystemDeviceEthernetIntrLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetIntrLost.setStatus("mandatory")
_Sm6kSystemDeviceEthernetWdtLost_Type = Counter32
_Sm6kSystemDeviceEthernetWdtLost_Object = MibTableColumn
sm6kSystemDeviceEthernetWdtLost = _Sm6kSystemDeviceEthernetWdtLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 21),
    _Sm6kSystemDeviceEthernetWdtLost_Type()
)
sm6kSystemDeviceEthernetWdtLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetWdtLost.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTimoLost_Type = Counter32
_Sm6kSystemDeviceEthernetTimoLost_Object = MibTableColumn
sm6kSystemDeviceEthernetTimoLost = _Sm6kSystemDeviceEthernetTimoLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 22),
    _Sm6kSystemDeviceEthernetTimoLost_Type()
)
sm6kSystemDeviceEthernetTimoLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTimoLost.setStatus("mandatory")
_Sm6kSystemDeviceEthernetStaQueOverflow_Type = Counter32
_Sm6kSystemDeviceEthernetStaQueOverflow_Object = MibTableColumn
sm6kSystemDeviceEthernetStaQueOverflow = _Sm6kSystemDeviceEthernetStaQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 23),
    _Sm6kSystemDeviceEthernetStaQueOverflow_Type()
)
sm6kSystemDeviceEthernetStaQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetStaQueOverflow.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxQueOverflow_Type = Counter32
_Sm6kSystemDeviceEthernetRxQueOverflow_Object = MibTableColumn
sm6kSystemDeviceEthernetRxQueOverflow = _Sm6kSystemDeviceEthernetRxQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 24),
    _Sm6kSystemDeviceEthernetRxQueOverflow_Type()
)
sm6kSystemDeviceEthernetRxQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxQueOverflow.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxQueNoMbuf_Type = Counter32
_Sm6kSystemDeviceEthernetRxQueNoMbuf_Object = MibTableColumn
sm6kSystemDeviceEthernetRxQueNoMbuf = _Sm6kSystemDeviceEthernetRxQueNoMbuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 25),
    _Sm6kSystemDeviceEthernetRxQueNoMbuf_Type()
)
sm6kSystemDeviceEthernetRxQueNoMbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxQueNoMbuf.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxQueNoMbufExt_Type = Counter32
_Sm6kSystemDeviceEthernetRxQueNoMbufExt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxQueNoMbufExt = _Sm6kSystemDeviceEthernetRxQueNoMbufExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 26),
    _Sm6kSystemDeviceEthernetRxQueNoMbufExt_Type()
)
sm6kSystemDeviceEthernetRxQueNoMbufExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxQueNoMbufExt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxIntrCnt_Type = Counter32
_Sm6kSystemDeviceEthernetTxIntrCnt_Object = MibTableColumn
sm6kSystemDeviceEthernetTxIntrCnt = _Sm6kSystemDeviceEthernetTxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 27),
    _Sm6kSystemDeviceEthernetTxIntrCnt_Type()
)
sm6kSystemDeviceEthernetTxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxIntrCnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetRxIntrCnt_Type = Counter32
_Sm6kSystemDeviceEthernetRxIntrCnt_Object = MibTableColumn
sm6kSystemDeviceEthernetRxIntrCnt = _Sm6kSystemDeviceEthernetRxIntrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 28),
    _Sm6kSystemDeviceEthernetRxIntrCnt_Type()
)
sm6kSystemDeviceEthernetRxIntrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetRxIntrCnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetCRCErr_Type = Counter32
_Sm6kSystemDeviceEthernetCRCErr_Object = MibTableColumn
sm6kSystemDeviceEthernetCRCErr = _Sm6kSystemDeviceEthernetCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 29),
    _Sm6kSystemDeviceEthernetCRCErr_Type()
)
sm6kSystemDeviceEthernetCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetCRCErr.setStatus("mandatory")
_Sm6kSystemDeviceEthernetAlignErr_Type = Counter32
_Sm6kSystemDeviceEthernetAlignErr_Object = MibTableColumn
sm6kSystemDeviceEthernetAlignErr = _Sm6kSystemDeviceEthernetAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 30),
    _Sm6kSystemDeviceEthernetAlignErr_Type()
)
sm6kSystemDeviceEthernetAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetAlignErr.setStatus("mandatory")
_Sm6kSystemDeviceEthernetOverrun_Type = Counter32
_Sm6kSystemDeviceEthernetOverrun_Object = MibTableColumn
sm6kSystemDeviceEthernetOverrun = _Sm6kSystemDeviceEthernetOverrun_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 31),
    _Sm6kSystemDeviceEthernetOverrun_Type()
)
sm6kSystemDeviceEthernetOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetOverrun.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTooShort_Type = Counter32
_Sm6kSystemDeviceEthernetTooShort_Object = MibTableColumn
sm6kSystemDeviceEthernetTooShort = _Sm6kSystemDeviceEthernetTooShort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 32),
    _Sm6kSystemDeviceEthernetTooShort_Type()
)
sm6kSystemDeviceEthernetTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTooShort.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTooLong_Type = Counter32
_Sm6kSystemDeviceEthernetTooLong_Object = MibTableColumn
sm6kSystemDeviceEthernetTooLong = _Sm6kSystemDeviceEthernetTooLong_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 33),
    _Sm6kSystemDeviceEthernetTooLong_Type()
)
sm6kSystemDeviceEthernetTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTooLong.setStatus("mandatory")
_Sm6kSystemDeviceEthernetNoResources_Type = Counter32
_Sm6kSystemDeviceEthernetNoResources_Object = MibTableColumn
sm6kSystemDeviceEthernetNoResources = _Sm6kSystemDeviceEthernetNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 34),
    _Sm6kSystemDeviceEthernetNoResources_Type()
)
sm6kSystemDeviceEthernetNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetNoResources.setStatus("mandatory")
_Sm6kSystemDeviceEthernetPktDiscard_Type = Counter32
_Sm6kSystemDeviceEthernetPktDiscard_Object = MibTableColumn
sm6kSystemDeviceEthernetPktDiscard = _Sm6kSystemDeviceEthernetPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 35),
    _Sm6kSystemDeviceEthernetPktDiscard_Type()
)
sm6kSystemDeviceEthernetPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetPktDiscard.setStatus("mandatory")
_Sm6kSystemDeviceEthernetMaxCollision_Type = Counter32
_Sm6kSystemDeviceEthernetMaxCollision_Object = MibTableColumn
sm6kSystemDeviceEthernetMaxCollision = _Sm6kSystemDeviceEthernetMaxCollision_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 36),
    _Sm6kSystemDeviceEthernetMaxCollision_Type()
)
sm6kSystemDeviceEthernetMaxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetMaxCollision.setStatus("mandatory")
_Sm6kSystemDeviceEthernetLateCollision_Type = Counter32
_Sm6kSystemDeviceEthernetLateCollision_Object = MibTableColumn
sm6kSystemDeviceEthernetLateCollision = _Sm6kSystemDeviceEthernetLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 37),
    _Sm6kSystemDeviceEthernetLateCollision_Type()
)
sm6kSystemDeviceEthernetLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetLateCollision.setStatus("mandatory")
_Sm6kSystemDeviceEthernetCarrierLost_Type = Counter32
_Sm6kSystemDeviceEthernetCarrierLost_Object = MibTableColumn
sm6kSystemDeviceEthernetCarrierLost = _Sm6kSystemDeviceEthernetCarrierLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 38),
    _Sm6kSystemDeviceEthernetCarrierLost_Type()
)
sm6kSystemDeviceEthernetCarrierLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetCarrierLost.setStatus("mandatory")
_Sm6kSystemDeviceEthernetUnderrun_Type = Counter32
_Sm6kSystemDeviceEthernetUnderrun_Object = MibTableColumn
sm6kSystemDeviceEthernetUnderrun = _Sm6kSystemDeviceEthernetUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 39),
    _Sm6kSystemDeviceEthernetUnderrun_Type()
)
sm6kSystemDeviceEthernetUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetUnderrun.setStatus("mandatory")
_Sm6kSystemDeviceEthernetCTSLost_Type = Counter32
_Sm6kSystemDeviceEthernetCTSLost_Object = MibTableColumn
sm6kSystemDeviceEthernetCTSLost = _Sm6kSystemDeviceEthernetCTSLost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 40),
    _Sm6kSystemDeviceEthernetCTSLost_Type()
)
sm6kSystemDeviceEthernetCTSLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetCTSLost.setStatus("mandatory")
_Sm6kSystemDeviceEthernetTxTimeouts_Type = Counter32
_Sm6kSystemDeviceEthernetTxTimeouts_Object = MibTableColumn
sm6kSystemDeviceEthernetTxTimeouts = _Sm6kSystemDeviceEthernetTxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 41),
    _Sm6kSystemDeviceEthernetTxTimeouts_Type()
)
sm6kSystemDeviceEthernetTxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetTxTimeouts.setStatus("mandatory")
_Sm6kSystemDeviceEthernetParErrCnt_Type = Counter32
_Sm6kSystemDeviceEthernetParErrCnt_Object = MibTableColumn
sm6kSystemDeviceEthernetParErrCnt = _Sm6kSystemDeviceEthernetParErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 42),
    _Sm6kSystemDeviceEthernetParErrCnt_Type()
)
sm6kSystemDeviceEthernetParErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetParErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetDiagOverflow_Type = Counter32
_Sm6kSystemDeviceEthernetDiagOverflow_Object = MibTableColumn
sm6kSystemDeviceEthernetDiagOverflow = _Sm6kSystemDeviceEthernetDiagOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 43),
    _Sm6kSystemDeviceEthernetDiagOverflow_Type()
)
sm6kSystemDeviceEthernetDiagOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetDiagOverflow.setStatus("mandatory")
_Sm6kSystemDeviceEthernetExecOverflow_Type = Counter32
_Sm6kSystemDeviceEthernetExecOverflow_Object = MibTableColumn
sm6kSystemDeviceEthernetExecOverflow = _Sm6kSystemDeviceEthernetExecOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 44),
    _Sm6kSystemDeviceEthernetExecOverflow_Type()
)
sm6kSystemDeviceEthernetExecOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetExecOverflow.setStatus("mandatory")
_Sm6kSystemDeviceEthernetExecCmdErrors_Type = Counter32
_Sm6kSystemDeviceEthernetExecCmdErrors_Object = MibTableColumn
sm6kSystemDeviceEthernetExecCmdErrors = _Sm6kSystemDeviceEthernetExecCmdErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 45),
    _Sm6kSystemDeviceEthernetExecCmdErrors_Type()
)
sm6kSystemDeviceEthernetExecCmdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetExecCmdErrors.setStatus("mandatory")
_Sm6kSystemDeviceEthernetHostRecEol_Type = Counter32
_Sm6kSystemDeviceEthernetHostRecEol_Object = MibTableColumn
sm6kSystemDeviceEthernetHostRecEol = _Sm6kSystemDeviceEthernetHostRecEol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 46),
    _Sm6kSystemDeviceEthernetHostRecEol_Type()
)
sm6kSystemDeviceEthernetHostRecEol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetHostRecEol.setStatus("mandatory")
_Sm6kSystemDeviceEthernetAdptRecEol_Type = Counter32
_Sm6kSystemDeviceEthernetAdptRecEol_Object = MibTableColumn
sm6kSystemDeviceEthernetAdptRecEol = _Sm6kSystemDeviceEthernetAdptRecEol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 47),
    _Sm6kSystemDeviceEthernetAdptRecEol_Type()
)
sm6kSystemDeviceEthernetAdptRecEol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetAdptRecEol.setStatus("mandatory")
_Sm6kSystemDeviceEthernetHostRecPkt_Type = Counter32
_Sm6kSystemDeviceEthernetHostRecPkt_Object = MibTableColumn
sm6kSystemDeviceEthernetHostRecPkt = _Sm6kSystemDeviceEthernetHostRecPkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 48),
    _Sm6kSystemDeviceEthernetHostRecPkt_Type()
)
sm6kSystemDeviceEthernetHostRecPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetHostRecPkt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetAdptRecPkt_Type = Counter32
_Sm6kSystemDeviceEthernetAdptRecPkt_Object = MibTableColumn
sm6kSystemDeviceEthernetAdptRecPkt = _Sm6kSystemDeviceEthernetAdptRecPkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 49),
    _Sm6kSystemDeviceEthernetAdptRecPkt_Type()
)
sm6kSystemDeviceEthernetAdptRecPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetAdptRecPkt.setStatus("mandatory")
_Sm6kSystemDeviceEthernetStartRxCmd_Type = Counter32
_Sm6kSystemDeviceEthernetStartRxCmd_Object = MibTableColumn
sm6kSystemDeviceEthernetStartRxCmd = _Sm6kSystemDeviceEthernetStartRxCmd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 50),
    _Sm6kSystemDeviceEthernetStartRxCmd_Type()
)
sm6kSystemDeviceEthernetStartRxCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetStartRxCmd.setStatus("mandatory")
_Sm6kSystemDeviceEthernetStartRxDmaTimeouts_Type = Counter32
_Sm6kSystemDeviceEthernetStartRxDmaTimeouts_Object = MibTableColumn
sm6kSystemDeviceEthernetStartRxDmaTimeouts = _Sm6kSystemDeviceEthernetStartRxDmaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 51),
    _Sm6kSystemDeviceEthernetStartRxDmaTimeouts_Type()
)
sm6kSystemDeviceEthernetStartRxDmaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetStartRxDmaTimeouts.setStatus("mandatory")
_Sm6kSystemDeviceEthernetVPD_Type = DisplayString
_Sm6kSystemDeviceEthernetVPD_Object = MibTableColumn
sm6kSystemDeviceEthernetVPD = _Sm6kSystemDeviceEthernetVPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 52),
    _Sm6kSystemDeviceEthernetVPD_Type()
)
sm6kSystemDeviceEthernetVPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetVPD.setStatus("mandatory")


class _Sm6kSystemDeviceEthernetClear_Type(Integer32):
    """Custom type sm6kSystemDeviceEthernetClear based on Integer32"""
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


_Sm6kSystemDeviceEthernetClear_Type.__name__ = "Integer32"
_Sm6kSystemDeviceEthernetClear_Object = MibTableColumn
sm6kSystemDeviceEthernetClear = _Sm6kSystemDeviceEthernetClear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 3, 2, 1, 53),
    _Sm6kSystemDeviceEthernetClear_Type()
)
sm6kSystemDeviceEthernetClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kSystemDeviceEthernetClear.setStatus("mandatory")
_Sm6kSystemDeviceX25_ObjectIdentity = ObjectIdentity
sm6kSystemDeviceX25 = _Sm6kSystemDeviceX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4)
)
_Sm6kSystemDeviceX25Installed_Type = Integer32
_Sm6kSystemDeviceX25Installed_Object = MibScalar
sm6kSystemDeviceX25Installed = _Sm6kSystemDeviceX25Installed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 1),
    _Sm6kSystemDeviceX25Installed_Type()
)
sm6kSystemDeviceX25Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Installed.setStatus("mandatory")
_Sm6kSystemDeviceX25Table_Object = MibTable
sm6kSystemDeviceX25Table = _Sm6kSystemDeviceX25Table_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Table.setStatus("mandatory")
_Sm6kSystemDeviceX25Entry_Object = MibTableRow
sm6kSystemDeviceX25Entry = _Sm6kSystemDeviceX25Entry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1)
)
sm6kSystemDeviceX25Entry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemDeviceX25Number"),
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Entry.setStatus("mandatory")
_Sm6kSystemDeviceX25Number_Type = Integer32
_Sm6kSystemDeviceX25Number_Object = MibTableColumn
sm6kSystemDeviceX25Number = _Sm6kSystemDeviceX25Number_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 1),
    _Sm6kSystemDeviceX25Number_Type()
)
sm6kSystemDeviceX25Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Number.setStatus("mandatory")
_Sm6kSystemDeviceX25Address_Type = DisplayString
_Sm6kSystemDeviceX25Address_Object = MibTableColumn
sm6kSystemDeviceX25Address = _Sm6kSystemDeviceX25Address_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 2),
    _Sm6kSystemDeviceX25Address_Type()
)
sm6kSystemDeviceX25Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Address.setStatus("mandatory")
_Sm6kSystemDeviceX25SupportLevel_Type = Integer32
_Sm6kSystemDeviceX25SupportLevel_Object = MibTableColumn
sm6kSystemDeviceX25SupportLevel = _Sm6kSystemDeviceX25SupportLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 3),
    _Sm6kSystemDeviceX25SupportLevel_Type()
)
sm6kSystemDeviceX25SupportLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25SupportLevel.setStatus("mandatory")
_Sm6kSystemDeviceX25SupportedFacilities_Type = Integer32
_Sm6kSystemDeviceX25SupportedFacilities_Object = MibTableColumn
sm6kSystemDeviceX25SupportedFacilities = _Sm6kSystemDeviceX25SupportedFacilities_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 4),
    _Sm6kSystemDeviceX25SupportedFacilities_Type()
)
sm6kSystemDeviceX25SupportedFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25SupportedFacilities.setStatus("mandatory")
_Sm6kSystemDeviceX25NetworkId_Type = PhysAddress
_Sm6kSystemDeviceX25NetworkId_Object = MibTableColumn
sm6kSystemDeviceX25NetworkId = _Sm6kSystemDeviceX25NetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 5),
    _Sm6kSystemDeviceX25NetworkId_Type()
)
sm6kSystemDeviceX25NetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25NetworkId.setStatus("mandatory")
_Sm6kSystemDeviceX25MaxTxPacketSize_Type = Integer32
_Sm6kSystemDeviceX25MaxTxPacketSize_Object = MibTableColumn
sm6kSystemDeviceX25MaxTxPacketSize = _Sm6kSystemDeviceX25MaxTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 6),
    _Sm6kSystemDeviceX25MaxTxPacketSize_Type()
)
sm6kSystemDeviceX25MaxTxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25MaxTxPacketSize.setStatus("mandatory")
_Sm6kSystemDeviceX25MaxRxPacketSize_Type = Integer32
_Sm6kSystemDeviceX25MaxRxPacketSize_Object = MibTableColumn
sm6kSystemDeviceX25MaxRxPacketSize = _Sm6kSystemDeviceX25MaxRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 7),
    _Sm6kSystemDeviceX25MaxRxPacketSize_Type()
)
sm6kSystemDeviceX25MaxRxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25MaxRxPacketSize.setStatus("mandatory")
_Sm6kSystemDeviceX25DefaultSvcTxPacketSize_Type = Integer32
_Sm6kSystemDeviceX25DefaultSvcTxPacketSize_Object = MibTableColumn
sm6kSystemDeviceX25DefaultSvcTxPacketSize = _Sm6kSystemDeviceX25DefaultSvcTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 8),
    _Sm6kSystemDeviceX25DefaultSvcTxPacketSize_Type()
)
sm6kSystemDeviceX25DefaultSvcTxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DefaultSvcTxPacketSize.setStatus("mandatory")
_Sm6kSystemDeviceX25DefaultSvcRxPacketSize_Type = Integer32
_Sm6kSystemDeviceX25DefaultSvcRxPacketSize_Object = MibTableColumn
sm6kSystemDeviceX25DefaultSvcRxPacketSize = _Sm6kSystemDeviceX25DefaultSvcRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 9),
    _Sm6kSystemDeviceX25DefaultSvcRxPacketSize_Type()
)
sm6kSystemDeviceX25DefaultSvcRxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DefaultSvcRxPacketSize.setStatus("mandatory")
_Sm6kSystemDeviceX25ReceiveDataTransferOffset_Type = Integer32
_Sm6kSystemDeviceX25ReceiveDataTransferOffset_Object = MibTableColumn
sm6kSystemDeviceX25ReceiveDataTransferOffset = _Sm6kSystemDeviceX25ReceiveDataTransferOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 10),
    _Sm6kSystemDeviceX25ReceiveDataTransferOffset_Type()
)
sm6kSystemDeviceX25ReceiveDataTransferOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ReceiveDataTransferOffset.setStatus("mandatory")
_Sm6kSystemDeviceX25MemoryWindowSize_Type = Integer32
_Sm6kSystemDeviceX25MemoryWindowSize_Object = MibTableColumn
sm6kSystemDeviceX25MemoryWindowSize = _Sm6kSystemDeviceX25MemoryWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 11),
    _Sm6kSystemDeviceX25MemoryWindowSize_Type()
)
sm6kSystemDeviceX25MemoryWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25MemoryWindowSize.setStatus("mandatory")
_Sm6kSystemDeviceX25TxByteMcnt_Type = Counter32
_Sm6kSystemDeviceX25TxByteMcnt_Object = MibTableColumn
sm6kSystemDeviceX25TxByteMcnt = _Sm6kSystemDeviceX25TxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 12),
    _Sm6kSystemDeviceX25TxByteMcnt_Type()
)
sm6kSystemDeviceX25TxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxByteMcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25TxByteLcnt_Type = Counter32
_Sm6kSystemDeviceX25TxByteLcnt_Object = MibTableColumn
sm6kSystemDeviceX25TxByteLcnt = _Sm6kSystemDeviceX25TxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 13),
    _Sm6kSystemDeviceX25TxByteLcnt_Type()
)
sm6kSystemDeviceX25TxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxByteLcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25RxByteMcnt_Type = Counter32
_Sm6kSystemDeviceX25RxByteMcnt_Object = MibTableColumn
sm6kSystemDeviceX25RxByteMcnt = _Sm6kSystemDeviceX25RxByteMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 14),
    _Sm6kSystemDeviceX25RxByteMcnt_Type()
)
sm6kSystemDeviceX25RxByteMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxByteMcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25RxByteLcnt_Type = Counter32
_Sm6kSystemDeviceX25RxByteLcnt_Object = MibTableColumn
sm6kSystemDeviceX25RxByteLcnt = _Sm6kSystemDeviceX25RxByteLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 15),
    _Sm6kSystemDeviceX25RxByteLcnt_Type()
)
sm6kSystemDeviceX25RxByteLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxByteLcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25TxFrameMcnt_Type = Counter32
_Sm6kSystemDeviceX25TxFrameMcnt_Object = MibTableColumn
sm6kSystemDeviceX25TxFrameMcnt = _Sm6kSystemDeviceX25TxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 16),
    _Sm6kSystemDeviceX25TxFrameMcnt_Type()
)
sm6kSystemDeviceX25TxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxFrameMcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25TxFrameLcnt_Type = Counter32
_Sm6kSystemDeviceX25TxFrameLcnt_Object = MibTableColumn
sm6kSystemDeviceX25TxFrameLcnt = _Sm6kSystemDeviceX25TxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 17),
    _Sm6kSystemDeviceX25TxFrameLcnt_Type()
)
sm6kSystemDeviceX25TxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxFrameLcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25RxFrameMcnt_Type = Counter32
_Sm6kSystemDeviceX25RxFrameMcnt_Object = MibTableColumn
sm6kSystemDeviceX25RxFrameMcnt = _Sm6kSystemDeviceX25RxFrameMcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 18),
    _Sm6kSystemDeviceX25RxFrameMcnt_Type()
)
sm6kSystemDeviceX25RxFrameMcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxFrameMcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25RxFrameLcnt_Type = Counter32
_Sm6kSystemDeviceX25RxFrameLcnt_Object = MibTableColumn
sm6kSystemDeviceX25RxFrameLcnt = _Sm6kSystemDeviceX25RxFrameLcnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 19),
    _Sm6kSystemDeviceX25RxFrameLcnt_Type()
)
sm6kSystemDeviceX25RxFrameLcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxFrameLcnt.setStatus("mandatory")
_Sm6kSystemDeviceX25TxErrCnt_Type = Counter32
_Sm6kSystemDeviceX25TxErrCnt_Object = MibTableColumn
sm6kSystemDeviceX25TxErrCnt = _Sm6kSystemDeviceX25TxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 20),
    _Sm6kSystemDeviceX25TxErrCnt_Type()
)
sm6kSystemDeviceX25TxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceX25RxErrCnt_Type = Counter32
_Sm6kSystemDeviceX25RxErrCnt_Object = MibTableColumn
sm6kSystemDeviceX25RxErrCnt = _Sm6kSystemDeviceX25RxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 21),
    _Sm6kSystemDeviceX25RxErrCnt_Type()
)
sm6kSystemDeviceX25RxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxErrCnt.setStatus("mandatory")
_Sm6kSystemDeviceX25NidTblHigh_Type = Integer32
_Sm6kSystemDeviceX25NidTblHigh_Object = MibTableColumn
sm6kSystemDeviceX25NidTblHigh = _Sm6kSystemDeviceX25NidTblHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 22),
    _Sm6kSystemDeviceX25NidTblHigh_Type()
)
sm6kSystemDeviceX25NidTblHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25NidTblHigh.setStatus("mandatory")
_Sm6kSystemDeviceX25TxQueHigh_Type = Gauge32
_Sm6kSystemDeviceX25TxQueHigh_Object = MibTableColumn
sm6kSystemDeviceX25TxQueHigh = _Sm6kSystemDeviceX25TxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 23),
    _Sm6kSystemDeviceX25TxQueHigh_Type()
)
sm6kSystemDeviceX25TxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceX25RxQueHigh_Type = Gauge32
_Sm6kSystemDeviceX25RxQueHigh_Object = MibTableColumn
sm6kSystemDeviceX25RxQueHigh = _Sm6kSystemDeviceX25RxQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 24),
    _Sm6kSystemDeviceX25RxQueHigh_Type()
)
sm6kSystemDeviceX25RxQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceX25StaQueHigh_Type = Gauge32
_Sm6kSystemDeviceX25StaQueHigh_Object = MibTableColumn
sm6kSystemDeviceX25StaQueHigh = _Sm6kSystemDeviceX25StaQueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 25),
    _Sm6kSystemDeviceX25StaQueHigh_Type()
)
sm6kSystemDeviceX25StaQueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25StaQueHigh.setStatus("mandatory")
_Sm6kSystemDeviceX25IgnoredFTx_Type = Counter32
_Sm6kSystemDeviceX25IgnoredFTx_Object = MibTableColumn
sm6kSystemDeviceX25IgnoredFTx = _Sm6kSystemDeviceX25IgnoredFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 26),
    _Sm6kSystemDeviceX25IgnoredFTx_Type()
)
sm6kSystemDeviceX25IgnoredFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25IgnoredFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RrFTx_Type = Counter32
_Sm6kSystemDeviceX25RrFTx_Object = MibTableColumn
sm6kSystemDeviceX25RrFTx = _Sm6kSystemDeviceX25RrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 27),
    _Sm6kSystemDeviceX25RrFTx_Type()
)
sm6kSystemDeviceX25RrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RrFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RnrFTx_Type = Counter32
_Sm6kSystemDeviceX25RnrFTx_Object = MibTableColumn
sm6kSystemDeviceX25RnrFTx = _Sm6kSystemDeviceX25RnrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 28),
    _Sm6kSystemDeviceX25RnrFTx_Type()
)
sm6kSystemDeviceX25RnrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RnrFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RejFTx_Type = Counter32
_Sm6kSystemDeviceX25RejFTx_Object = MibTableColumn
sm6kSystemDeviceX25RejFTx = _Sm6kSystemDeviceX25RejFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 29),
    _Sm6kSystemDeviceX25RejFTx_Type()
)
sm6kSystemDeviceX25RejFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RejFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25InfoFTx_Type = Counter32
_Sm6kSystemDeviceX25InfoFTx_Object = MibTableColumn
sm6kSystemDeviceX25InfoFTx = _Sm6kSystemDeviceX25InfoFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 30),
    _Sm6kSystemDeviceX25InfoFTx_Type()
)
sm6kSystemDeviceX25InfoFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25InfoFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25SabmFTx_Type = Counter32
_Sm6kSystemDeviceX25SabmFTx_Object = MibTableColumn
sm6kSystemDeviceX25SabmFTx = _Sm6kSystemDeviceX25SabmFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 31),
    _Sm6kSystemDeviceX25SabmFTx_Type()
)
sm6kSystemDeviceX25SabmFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25SabmFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25SarmDmFTx_Type = Counter32
_Sm6kSystemDeviceX25SarmDmFTx_Object = MibTableColumn
sm6kSystemDeviceX25SarmDmFTx = _Sm6kSystemDeviceX25SarmDmFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 32),
    _Sm6kSystemDeviceX25SarmDmFTx_Type()
)
sm6kSystemDeviceX25SarmDmFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25SarmDmFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25DiscFTx_Type = Counter32
_Sm6kSystemDeviceX25DiscFTx_Object = MibTableColumn
sm6kSystemDeviceX25DiscFTx = _Sm6kSystemDeviceX25DiscFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 33),
    _Sm6kSystemDeviceX25DiscFTx_Type()
)
sm6kSystemDeviceX25DiscFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DiscFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25UaFTx_Type = Counter32
_Sm6kSystemDeviceX25UaFTx_Object = MibTableColumn
sm6kSystemDeviceX25UaFTx = _Sm6kSystemDeviceX25UaFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 34),
    _Sm6kSystemDeviceX25UaFTx_Type()
)
sm6kSystemDeviceX25UaFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25UaFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25FrmrFTx_Type = Counter32
_Sm6kSystemDeviceX25FrmrFTx_Object = MibTableColumn
sm6kSystemDeviceX25FrmrFTx = _Sm6kSystemDeviceX25FrmrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 35),
    _Sm6kSystemDeviceX25FrmrFTx_Type()
)
sm6kSystemDeviceX25FrmrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25FrmrFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25BadNrFTx_Type = Counter32
_Sm6kSystemDeviceX25BadNrFTx_Object = MibTableColumn
sm6kSystemDeviceX25BadNrFTx = _Sm6kSystemDeviceX25BadNrFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 36),
    _Sm6kSystemDeviceX25BadNrFTx_Type()
)
sm6kSystemDeviceX25BadNrFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25BadNrFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25UnknownFTx_Type = Counter32
_Sm6kSystemDeviceX25UnknownFTx_Object = MibTableColumn
sm6kSystemDeviceX25UnknownFTx = _Sm6kSystemDeviceX25UnknownFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 37),
    _Sm6kSystemDeviceX25UnknownFTx_Type()
)
sm6kSystemDeviceX25UnknownFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25UnknownFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25XidFTx_Type = Counter32
_Sm6kSystemDeviceX25XidFTx_Object = MibTableColumn
sm6kSystemDeviceX25XidFTx = _Sm6kSystemDeviceX25XidFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 38),
    _Sm6kSystemDeviceX25XidFTx_Type()
)
sm6kSystemDeviceX25XidFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25XidFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25BadLengthFTx_Type = Counter32
_Sm6kSystemDeviceX25BadLengthFTx_Object = MibTableColumn
sm6kSystemDeviceX25BadLengthFTx = _Sm6kSystemDeviceX25BadLengthFTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 39),
    _Sm6kSystemDeviceX25BadLengthFTx_Type()
)
sm6kSystemDeviceX25BadLengthFTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25BadLengthFTx.setStatus("mandatory")
_Sm6kSystemDeviceX25T1Expirations_Type = Counter32
_Sm6kSystemDeviceX25T1Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T1Expirations = _Sm6kSystemDeviceX25T1Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 40),
    _Sm6kSystemDeviceX25T1Expirations_Type()
)
sm6kSystemDeviceX25T1Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T1Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25Lvl2Connects_Type = Counter32
_Sm6kSystemDeviceX25Lvl2Connects_Object = MibTableColumn
sm6kSystemDeviceX25Lvl2Connects = _Sm6kSystemDeviceX25Lvl2Connects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 41),
    _Sm6kSystemDeviceX25Lvl2Connects_Type()
)
sm6kSystemDeviceX25Lvl2Connects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Lvl2Connects.setStatus("mandatory")
_Sm6kSystemDeviceX25Lvl2Disconnects_Type = Counter32
_Sm6kSystemDeviceX25Lvl2Disconnects_Object = MibTableColumn
sm6kSystemDeviceX25Lvl2Disconnects = _Sm6kSystemDeviceX25Lvl2Disconnects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 42),
    _Sm6kSystemDeviceX25Lvl2Disconnects_Type()
)
sm6kSystemDeviceX25Lvl2Disconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Lvl2Disconnects.setStatus("mandatory")
_Sm6kSystemDeviceX25CarrierLoss_Type = Counter32
_Sm6kSystemDeviceX25CarrierLoss_Object = MibTableColumn
sm6kSystemDeviceX25CarrierLoss = _Sm6kSystemDeviceX25CarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 43),
    _Sm6kSystemDeviceX25CarrierLoss_Type()
)
sm6kSystemDeviceX25CarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25CarrierLoss.setStatus("mandatory")
_Sm6kSystemDeviceX25ConnectTime_Type = TimeTicks
_Sm6kSystemDeviceX25ConnectTime_Object = MibTableColumn
sm6kSystemDeviceX25ConnectTime = _Sm6kSystemDeviceX25ConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 44),
    _Sm6kSystemDeviceX25ConnectTime_Type()
)
sm6kSystemDeviceX25ConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ConnectTime.setStatus("mandatory")
_Sm6kSystemDeviceX25T4Expirations_Type = Counter32
_Sm6kSystemDeviceX25T4Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T4Expirations = _Sm6kSystemDeviceX25T4Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 45),
    _Sm6kSystemDeviceX25T4Expirations_Type()
)
sm6kSystemDeviceX25T4Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T4Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T4N2Times_Type = Counter32
_Sm6kSystemDeviceX25T4N2Times_Object = MibTableColumn
sm6kSystemDeviceX25T4N2Times = _Sm6kSystemDeviceX25T4N2Times_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 46),
    _Sm6kSystemDeviceX25T4N2Times_Type()
)
sm6kSystemDeviceX25T4N2Times.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T4N2Times.setStatus("mandatory")
_Sm6kSystemDeviceX25IgnoredFRx_Type = Counter32
_Sm6kSystemDeviceX25IgnoredFRx_Object = MibTableColumn
sm6kSystemDeviceX25IgnoredFRx = _Sm6kSystemDeviceX25IgnoredFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 47),
    _Sm6kSystemDeviceX25IgnoredFRx_Type()
)
sm6kSystemDeviceX25IgnoredFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25IgnoredFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RrFRx_Type = Counter32
_Sm6kSystemDeviceX25RrFRx_Object = MibTableColumn
sm6kSystemDeviceX25RrFRx = _Sm6kSystemDeviceX25RrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 48),
    _Sm6kSystemDeviceX25RrFRx_Type()
)
sm6kSystemDeviceX25RrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RrFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RnrFRx_Type = Counter32
_Sm6kSystemDeviceX25RnrFRx_Object = MibTableColumn
sm6kSystemDeviceX25RnrFRx = _Sm6kSystemDeviceX25RnrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 49),
    _Sm6kSystemDeviceX25RnrFRx_Type()
)
sm6kSystemDeviceX25RnrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RnrFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RejFRx_Type = Counter32
_Sm6kSystemDeviceX25RejFRx_Object = MibTableColumn
sm6kSystemDeviceX25RejFRx = _Sm6kSystemDeviceX25RejFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 50),
    _Sm6kSystemDeviceX25RejFRx_Type()
)
sm6kSystemDeviceX25RejFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RejFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25InfoFRx_Type = Counter32
_Sm6kSystemDeviceX25InfoFRx_Object = MibTableColumn
sm6kSystemDeviceX25InfoFRx = _Sm6kSystemDeviceX25InfoFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 51),
    _Sm6kSystemDeviceX25InfoFRx_Type()
)
sm6kSystemDeviceX25InfoFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25InfoFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25SabmFRx_Type = Counter32
_Sm6kSystemDeviceX25SabmFRx_Object = MibTableColumn
sm6kSystemDeviceX25SabmFRx = _Sm6kSystemDeviceX25SabmFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 52),
    _Sm6kSystemDeviceX25SabmFRx_Type()
)
sm6kSystemDeviceX25SabmFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25SabmFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25SarmDmFRx_Type = Counter32
_Sm6kSystemDeviceX25SarmDmFRx_Object = MibTableColumn
sm6kSystemDeviceX25SarmDmFRx = _Sm6kSystemDeviceX25SarmDmFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 53),
    _Sm6kSystemDeviceX25SarmDmFRx_Type()
)
sm6kSystemDeviceX25SarmDmFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25SarmDmFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25DiscFRx_Type = Counter32
_Sm6kSystemDeviceX25DiscFRx_Object = MibTableColumn
sm6kSystemDeviceX25DiscFRx = _Sm6kSystemDeviceX25DiscFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 54),
    _Sm6kSystemDeviceX25DiscFRx_Type()
)
sm6kSystemDeviceX25DiscFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DiscFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25UaFRx_Type = Counter32
_Sm6kSystemDeviceX25UaFRx_Object = MibTableColumn
sm6kSystemDeviceX25UaFRx = _Sm6kSystemDeviceX25UaFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 55),
    _Sm6kSystemDeviceX25UaFRx_Type()
)
sm6kSystemDeviceX25UaFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25UaFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25FrmrFRx_Type = Counter32
_Sm6kSystemDeviceX25FrmrFRx_Object = MibTableColumn
sm6kSystemDeviceX25FrmrFRx = _Sm6kSystemDeviceX25FrmrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 56),
    _Sm6kSystemDeviceX25FrmrFRx_Type()
)
sm6kSystemDeviceX25FrmrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25FrmrFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25BadNrFRx_Type = Counter32
_Sm6kSystemDeviceX25BadNrFRx_Object = MibTableColumn
sm6kSystemDeviceX25BadNrFRx = _Sm6kSystemDeviceX25BadNrFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 57),
    _Sm6kSystemDeviceX25BadNrFRx_Type()
)
sm6kSystemDeviceX25BadNrFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25BadNrFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25UnknownFRx_Type = Counter32
_Sm6kSystemDeviceX25UnknownFRx_Object = MibTableColumn
sm6kSystemDeviceX25UnknownFRx = _Sm6kSystemDeviceX25UnknownFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 58),
    _Sm6kSystemDeviceX25UnknownFRx_Type()
)
sm6kSystemDeviceX25UnknownFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25UnknownFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25XidFRx_Type = Counter32
_Sm6kSystemDeviceX25XidFRx_Object = MibTableColumn
sm6kSystemDeviceX25XidFRx = _Sm6kSystemDeviceX25XidFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 59),
    _Sm6kSystemDeviceX25XidFRx_Type()
)
sm6kSystemDeviceX25XidFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25XidFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25BadLengthFRx_Type = Counter32
_Sm6kSystemDeviceX25BadLengthFRx_Object = MibTableColumn
sm6kSystemDeviceX25BadLengthFRx = _Sm6kSystemDeviceX25BadLengthFRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 60),
    _Sm6kSystemDeviceX25BadLengthFRx_Type()
)
sm6kSystemDeviceX25BadLengthFRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25BadLengthFRx.setStatus("mandatory")
_Sm6kSystemDeviceX25DataPTx_Type = Counter32
_Sm6kSystemDeviceX25DataPTx_Object = MibTableColumn
sm6kSystemDeviceX25DataPTx = _Sm6kSystemDeviceX25DataPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 61),
    _Sm6kSystemDeviceX25DataPTx_Type()
)
sm6kSystemDeviceX25DataPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DataPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RrPTx_Type = Counter32
_Sm6kSystemDeviceX25RrPTx_Object = MibTableColumn
sm6kSystemDeviceX25RrPTx = _Sm6kSystemDeviceX25RrPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 62),
    _Sm6kSystemDeviceX25RrPTx_Type()
)
sm6kSystemDeviceX25RrPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RrPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RnrPTx_Type = Counter32
_Sm6kSystemDeviceX25RnrPTx_Object = MibTableColumn
sm6kSystemDeviceX25RnrPTx = _Sm6kSystemDeviceX25RnrPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 63),
    _Sm6kSystemDeviceX25RnrPTx_Type()
)
sm6kSystemDeviceX25RnrPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RnrPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25InterruptPTx_Type = Counter32
_Sm6kSystemDeviceX25InterruptPTx_Object = MibTableColumn
sm6kSystemDeviceX25InterruptPTx = _Sm6kSystemDeviceX25InterruptPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 64),
    _Sm6kSystemDeviceX25InterruptPTx_Type()
)
sm6kSystemDeviceX25InterruptPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25InterruptPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25InterruptConfirmPTx_Type = Counter32
_Sm6kSystemDeviceX25InterruptConfirmPTx_Object = MibTableColumn
sm6kSystemDeviceX25InterruptConfirmPTx = _Sm6kSystemDeviceX25InterruptConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 65),
    _Sm6kSystemDeviceX25InterruptConfirmPTx_Type()
)
sm6kSystemDeviceX25InterruptConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25InterruptConfirmPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25CallRequestPTx_Type = Counter32
_Sm6kSystemDeviceX25CallRequestPTx_Object = MibTableColumn
sm6kSystemDeviceX25CallRequestPTx = _Sm6kSystemDeviceX25CallRequestPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 66),
    _Sm6kSystemDeviceX25CallRequestPTx_Type()
)
sm6kSystemDeviceX25CallRequestPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25CallRequestPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25CallAcceptPTx_Type = Counter32
_Sm6kSystemDeviceX25CallAcceptPTx_Object = MibTableColumn
sm6kSystemDeviceX25CallAcceptPTx = _Sm6kSystemDeviceX25CallAcceptPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 67),
    _Sm6kSystemDeviceX25CallAcceptPTx_Type()
)
sm6kSystemDeviceX25CallAcceptPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25CallAcceptPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25ClearRequestPTx_Type = Counter32
_Sm6kSystemDeviceX25ClearRequestPTx_Object = MibTableColumn
sm6kSystemDeviceX25ClearRequestPTx = _Sm6kSystemDeviceX25ClearRequestPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 68),
    _Sm6kSystemDeviceX25ClearRequestPTx_Type()
)
sm6kSystemDeviceX25ClearRequestPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ClearRequestPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25ClearConfirmPTx_Type = Counter32
_Sm6kSystemDeviceX25ClearConfirmPTx_Object = MibTableColumn
sm6kSystemDeviceX25ClearConfirmPTx = _Sm6kSystemDeviceX25ClearConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 69),
    _Sm6kSystemDeviceX25ClearConfirmPTx_Type()
)
sm6kSystemDeviceX25ClearConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ClearConfirmPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25ResetRequestPTx_Type = Counter32
_Sm6kSystemDeviceX25ResetRequestPTx_Object = MibTableColumn
sm6kSystemDeviceX25ResetRequestPTx = _Sm6kSystemDeviceX25ResetRequestPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 70),
    _Sm6kSystemDeviceX25ResetRequestPTx_Type()
)
sm6kSystemDeviceX25ResetRequestPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ResetRequestPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25ResetConfirmPTx_Type = Counter32
_Sm6kSystemDeviceX25ResetConfirmPTx_Object = MibTableColumn
sm6kSystemDeviceX25ResetConfirmPTx = _Sm6kSystemDeviceX25ResetConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 71),
    _Sm6kSystemDeviceX25ResetConfirmPTx_Type()
)
sm6kSystemDeviceX25ResetConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ResetConfirmPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25DiagnosticPTx_Type = Counter32
_Sm6kSystemDeviceX25DiagnosticPTx_Object = MibTableColumn
sm6kSystemDeviceX25DiagnosticPTx = _Sm6kSystemDeviceX25DiagnosticPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 72),
    _Sm6kSystemDeviceX25DiagnosticPTx_Type()
)
sm6kSystemDeviceX25DiagnosticPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DiagnosticPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RegistrationPTx_Type = Counter32
_Sm6kSystemDeviceX25RegistrationPTx_Object = MibTableColumn
sm6kSystemDeviceX25RegistrationPTx = _Sm6kSystemDeviceX25RegistrationPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 73),
    _Sm6kSystemDeviceX25RegistrationPTx_Type()
)
sm6kSystemDeviceX25RegistrationPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RegistrationPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RegistrationConfirmPTx_Type = Counter32
_Sm6kSystemDeviceX25RegistrationConfirmPTx_Object = MibTableColumn
sm6kSystemDeviceX25RegistrationConfirmPTx = _Sm6kSystemDeviceX25RegistrationConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 74),
    _Sm6kSystemDeviceX25RegistrationConfirmPTx_Type()
)
sm6kSystemDeviceX25RegistrationConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RegistrationConfirmPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RestartPTx_Type = Counter32
_Sm6kSystemDeviceX25RestartPTx_Object = MibTableColumn
sm6kSystemDeviceX25RestartPTx = _Sm6kSystemDeviceX25RestartPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 75),
    _Sm6kSystemDeviceX25RestartPTx_Type()
)
sm6kSystemDeviceX25RestartPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RestartPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25RestartConfirmPTx_Type = Counter32
_Sm6kSystemDeviceX25RestartConfirmPTx_Object = MibTableColumn
sm6kSystemDeviceX25RestartConfirmPTx = _Sm6kSystemDeviceX25RestartConfirmPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 76),
    _Sm6kSystemDeviceX25RestartConfirmPTx_Type()
)
sm6kSystemDeviceX25RestartConfirmPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RestartConfirmPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25ErrorPTx_Type = Counter32
_Sm6kSystemDeviceX25ErrorPTx_Object = MibTableColumn
sm6kSystemDeviceX25ErrorPTx = _Sm6kSystemDeviceX25ErrorPTx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 77),
    _Sm6kSystemDeviceX25ErrorPTx_Type()
)
sm6kSystemDeviceX25ErrorPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ErrorPTx.setStatus("mandatory")
_Sm6kSystemDeviceX25T20Expirations_Type = Counter32
_Sm6kSystemDeviceX25T20Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T20Expirations = _Sm6kSystemDeviceX25T20Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 78),
    _Sm6kSystemDeviceX25T20Expirations_Type()
)
sm6kSystemDeviceX25T20Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T20Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T21Expirations_Type = Counter32
_Sm6kSystemDeviceX25T21Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T21Expirations = _Sm6kSystemDeviceX25T21Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 79),
    _Sm6kSystemDeviceX25T21Expirations_Type()
)
sm6kSystemDeviceX25T21Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T21Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T22Expirations_Type = Counter32
_Sm6kSystemDeviceX25T22Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T22Expirations = _Sm6kSystemDeviceX25T22Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 80),
    _Sm6kSystemDeviceX25T22Expirations_Type()
)
sm6kSystemDeviceX25T22Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T22Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T23Expirations_Type = Counter32
_Sm6kSystemDeviceX25T23Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T23Expirations = _Sm6kSystemDeviceX25T23Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 81),
    _Sm6kSystemDeviceX25T23Expirations_Type()
)
sm6kSystemDeviceX25T23Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T23Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25VcEstablishments_Type = Counter32
_Sm6kSystemDeviceX25VcEstablishments_Object = MibTableColumn
sm6kSystemDeviceX25VcEstablishments = _Sm6kSystemDeviceX25VcEstablishments_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 82),
    _Sm6kSystemDeviceX25VcEstablishments_Type()
)
sm6kSystemDeviceX25VcEstablishments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25VcEstablishments.setStatus("mandatory")
_Sm6kSystemDeviceX25T24Expirations_Type = Counter32
_Sm6kSystemDeviceX25T24Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T24Expirations = _Sm6kSystemDeviceX25T24Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 83),
    _Sm6kSystemDeviceX25T24Expirations_Type()
)
sm6kSystemDeviceX25T24Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T24Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T25Expirations_Type = Counter32
_Sm6kSystemDeviceX25T25Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T25Expirations = _Sm6kSystemDeviceX25T25Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 84),
    _Sm6kSystemDeviceX25T25Expirations_Type()
)
sm6kSystemDeviceX25T25Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T25Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T26Expirations_Type = Counter32
_Sm6kSystemDeviceX25T26Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T26Expirations = _Sm6kSystemDeviceX25T26Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 85),
    _Sm6kSystemDeviceX25T26Expirations_Type()
)
sm6kSystemDeviceX25T26Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T26Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25T28Expirations_Type = Counter32
_Sm6kSystemDeviceX25T28Expirations_Object = MibTableColumn
sm6kSystemDeviceX25T28Expirations = _Sm6kSystemDeviceX25T28Expirations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 86),
    _Sm6kSystemDeviceX25T28Expirations_Type()
)
sm6kSystemDeviceX25T28Expirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25T28Expirations.setStatus("mandatory")
_Sm6kSystemDeviceX25DataPRx_Type = Counter32
_Sm6kSystemDeviceX25DataPRx_Object = MibTableColumn
sm6kSystemDeviceX25DataPRx = _Sm6kSystemDeviceX25DataPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 87),
    _Sm6kSystemDeviceX25DataPRx_Type()
)
sm6kSystemDeviceX25DataPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DataPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RrPRx_Type = Counter32
_Sm6kSystemDeviceX25RrPRx_Object = MibTableColumn
sm6kSystemDeviceX25RrPRx = _Sm6kSystemDeviceX25RrPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 88),
    _Sm6kSystemDeviceX25RrPRx_Type()
)
sm6kSystemDeviceX25RrPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RrPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RnrPRx_Type = Counter32
_Sm6kSystemDeviceX25RnrPRx_Object = MibTableColumn
sm6kSystemDeviceX25RnrPRx = _Sm6kSystemDeviceX25RnrPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 89),
    _Sm6kSystemDeviceX25RnrPRx_Type()
)
sm6kSystemDeviceX25RnrPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RnrPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25InterruptPRx_Type = Counter32
_Sm6kSystemDeviceX25InterruptPRx_Object = MibTableColumn
sm6kSystemDeviceX25InterruptPRx = _Sm6kSystemDeviceX25InterruptPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 90),
    _Sm6kSystemDeviceX25InterruptPRx_Type()
)
sm6kSystemDeviceX25InterruptPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25InterruptPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25InterruptConfirmPRx_Type = Counter32
_Sm6kSystemDeviceX25InterruptConfirmPRx_Object = MibTableColumn
sm6kSystemDeviceX25InterruptConfirmPRx = _Sm6kSystemDeviceX25InterruptConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 91),
    _Sm6kSystemDeviceX25InterruptConfirmPRx_Type()
)
sm6kSystemDeviceX25InterruptConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25InterruptConfirmPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25IncomingCallPRx_Type = Counter32
_Sm6kSystemDeviceX25IncomingCallPRx_Object = MibTableColumn
sm6kSystemDeviceX25IncomingCallPRx = _Sm6kSystemDeviceX25IncomingCallPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 92),
    _Sm6kSystemDeviceX25IncomingCallPRx_Type()
)
sm6kSystemDeviceX25IncomingCallPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25IncomingCallPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25CallConnectedPRx_Type = Counter32
_Sm6kSystemDeviceX25CallConnectedPRx_Object = MibTableColumn
sm6kSystemDeviceX25CallConnectedPRx = _Sm6kSystemDeviceX25CallConnectedPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 93),
    _Sm6kSystemDeviceX25CallConnectedPRx_Type()
)
sm6kSystemDeviceX25CallConnectedPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25CallConnectedPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25ClearIndicationPRx_Type = Counter32
_Sm6kSystemDeviceX25ClearIndicationPRx_Object = MibTableColumn
sm6kSystemDeviceX25ClearIndicationPRx = _Sm6kSystemDeviceX25ClearIndicationPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 94),
    _Sm6kSystemDeviceX25ClearIndicationPRx_Type()
)
sm6kSystemDeviceX25ClearIndicationPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ClearIndicationPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25ClearConfirmPRx_Type = Counter32
_Sm6kSystemDeviceX25ClearConfirmPRx_Object = MibTableColumn
sm6kSystemDeviceX25ClearConfirmPRx = _Sm6kSystemDeviceX25ClearConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 95),
    _Sm6kSystemDeviceX25ClearConfirmPRx_Type()
)
sm6kSystemDeviceX25ClearConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ClearConfirmPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25ResetIndicationPRx_Type = Counter32
_Sm6kSystemDeviceX25ResetIndicationPRx_Object = MibTableColumn
sm6kSystemDeviceX25ResetIndicationPRx = _Sm6kSystemDeviceX25ResetIndicationPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 96),
    _Sm6kSystemDeviceX25ResetIndicationPRx_Type()
)
sm6kSystemDeviceX25ResetIndicationPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ResetIndicationPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25ResetConfirmPRx_Type = Counter32
_Sm6kSystemDeviceX25ResetConfirmPRx_Object = MibTableColumn
sm6kSystemDeviceX25ResetConfirmPRx = _Sm6kSystemDeviceX25ResetConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 97),
    _Sm6kSystemDeviceX25ResetConfirmPRx_Type()
)
sm6kSystemDeviceX25ResetConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25ResetConfirmPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25DiagnosticPRx_Type = Counter32
_Sm6kSystemDeviceX25DiagnosticPRx_Object = MibTableColumn
sm6kSystemDeviceX25DiagnosticPRx = _Sm6kSystemDeviceX25DiagnosticPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 98),
    _Sm6kSystemDeviceX25DiagnosticPRx_Type()
)
sm6kSystemDeviceX25DiagnosticPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25DiagnosticPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RegistrationPRx_Type = Counter32
_Sm6kSystemDeviceX25RegistrationPRx_Object = MibTableColumn
sm6kSystemDeviceX25RegistrationPRx = _Sm6kSystemDeviceX25RegistrationPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 99),
    _Sm6kSystemDeviceX25RegistrationPRx_Type()
)
sm6kSystemDeviceX25RegistrationPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RegistrationPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RegistrationConfirmPRx_Type = Counter32
_Sm6kSystemDeviceX25RegistrationConfirmPRx_Object = MibTableColumn
sm6kSystemDeviceX25RegistrationConfirmPRx = _Sm6kSystemDeviceX25RegistrationConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 100),
    _Sm6kSystemDeviceX25RegistrationConfirmPRx_Type()
)
sm6kSystemDeviceX25RegistrationConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RegistrationConfirmPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RestartPRx_Type = Counter32
_Sm6kSystemDeviceX25RestartPRx_Object = MibTableColumn
sm6kSystemDeviceX25RestartPRx = _Sm6kSystemDeviceX25RestartPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 101),
    _Sm6kSystemDeviceX25RestartPRx_Type()
)
sm6kSystemDeviceX25RestartPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RestartPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25RestartConfirmPRx_Type = Counter32
_Sm6kSystemDeviceX25RestartConfirmPRx_Object = MibTableColumn
sm6kSystemDeviceX25RestartConfirmPRx = _Sm6kSystemDeviceX25RestartConfirmPRx_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 102),
    _Sm6kSystemDeviceX25RestartConfirmPRx_Type()
)
sm6kSystemDeviceX25RestartConfirmPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RestartConfirmPRx.setStatus("mandatory")
_Sm6kSystemDeviceX25TxUnknownSize_Type = Counter32
_Sm6kSystemDeviceX25TxUnknownSize_Object = MibTableColumn
sm6kSystemDeviceX25TxUnknownSize = _Sm6kSystemDeviceX25TxUnknownSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 103),
    _Sm6kSystemDeviceX25TxUnknownSize_Type()
)
sm6kSystemDeviceX25TxUnknownSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxUnknownSize.setStatus("mandatory")
_Sm6kSystemDeviceX25TxReserved1_Type = Counter32
_Sm6kSystemDeviceX25TxReserved1_Object = MibTableColumn
sm6kSystemDeviceX25TxReserved1 = _Sm6kSystemDeviceX25TxReserved1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 104),
    _Sm6kSystemDeviceX25TxReserved1_Type()
)
sm6kSystemDeviceX25TxReserved1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxReserved1.setStatus("mandatory")
_Sm6kSystemDeviceX25TxReserved2_Type = Counter32
_Sm6kSystemDeviceX25TxReserved2_Object = MibTableColumn
sm6kSystemDeviceX25TxReserved2 = _Sm6kSystemDeviceX25TxReserved2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 105),
    _Sm6kSystemDeviceX25TxReserved2_Type()
)
sm6kSystemDeviceX25TxReserved2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxReserved2.setStatus("mandatory")
_Sm6kSystemDeviceX25TxReserved3_Type = Counter32
_Sm6kSystemDeviceX25TxReserved3_Object = MibTableColumn
sm6kSystemDeviceX25TxReserved3 = _Sm6kSystemDeviceX25TxReserved3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 106),
    _Sm6kSystemDeviceX25TxReserved3_Type()
)
sm6kSystemDeviceX25TxReserved3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxReserved3.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx0x15_Type = Counter32
_Sm6kSystemDeviceX25Tx0x15_Object = MibTableColumn
sm6kSystemDeviceX25Tx0x15 = _Sm6kSystemDeviceX25Tx0x15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 107),
    _Sm6kSystemDeviceX25Tx0x15_Type()
)
sm6kSystemDeviceX25Tx0x15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx0x15.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx16x31_Type = Counter32
_Sm6kSystemDeviceX25Tx16x31_Object = MibTableColumn
sm6kSystemDeviceX25Tx16x31 = _Sm6kSystemDeviceX25Tx16x31_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 108),
    _Sm6kSystemDeviceX25Tx16x31_Type()
)
sm6kSystemDeviceX25Tx16x31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx16x31.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx32x63_Type = Counter32
_Sm6kSystemDeviceX25Tx32x63_Object = MibTableColumn
sm6kSystemDeviceX25Tx32x63 = _Sm6kSystemDeviceX25Tx32x63_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 109),
    _Sm6kSystemDeviceX25Tx32x63_Type()
)
sm6kSystemDeviceX25Tx32x63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx32x63.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx64x127_Type = Counter32
_Sm6kSystemDeviceX25Tx64x127_Object = MibTableColumn
sm6kSystemDeviceX25Tx64x127 = _Sm6kSystemDeviceX25Tx64x127_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 110),
    _Sm6kSystemDeviceX25Tx64x127_Type()
)
sm6kSystemDeviceX25Tx64x127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx64x127.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx128x255_Type = Counter32
_Sm6kSystemDeviceX25Tx128x255_Object = MibTableColumn
sm6kSystemDeviceX25Tx128x255 = _Sm6kSystemDeviceX25Tx128x255_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 111),
    _Sm6kSystemDeviceX25Tx128x255_Type()
)
sm6kSystemDeviceX25Tx128x255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx128x255.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx256x511_Type = Counter32
_Sm6kSystemDeviceX25Tx256x511_Object = MibTableColumn
sm6kSystemDeviceX25Tx256x511 = _Sm6kSystemDeviceX25Tx256x511_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 112),
    _Sm6kSystemDeviceX25Tx256x511_Type()
)
sm6kSystemDeviceX25Tx256x511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx256x511.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx512x1023_Type = Counter32
_Sm6kSystemDeviceX25Tx512x1023_Object = MibTableColumn
sm6kSystemDeviceX25Tx512x1023 = _Sm6kSystemDeviceX25Tx512x1023_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 113),
    _Sm6kSystemDeviceX25Tx512x1023_Type()
)
sm6kSystemDeviceX25Tx512x1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx512x1023.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx1024x2047_Type = Counter32
_Sm6kSystemDeviceX25Tx1024x2047_Object = MibTableColumn
sm6kSystemDeviceX25Tx1024x2047 = _Sm6kSystemDeviceX25Tx1024x2047_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 114),
    _Sm6kSystemDeviceX25Tx1024x2047_Type()
)
sm6kSystemDeviceX25Tx1024x2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx1024x2047.setStatus("mandatory")
_Sm6kSystemDeviceX25Tx2048x4095_Type = Counter32
_Sm6kSystemDeviceX25Tx2048x4095_Object = MibTableColumn
sm6kSystemDeviceX25Tx2048x4095 = _Sm6kSystemDeviceX25Tx2048x4095_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 115),
    _Sm6kSystemDeviceX25Tx2048x4095_Type()
)
sm6kSystemDeviceX25Tx2048x4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Tx2048x4095.setStatus("mandatory")
_Sm6kSystemDeviceX25TxReserved13_Type = Counter32
_Sm6kSystemDeviceX25TxReserved13_Object = MibTableColumn
sm6kSystemDeviceX25TxReserved13 = _Sm6kSystemDeviceX25TxReserved13_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 116),
    _Sm6kSystemDeviceX25TxReserved13_Type()
)
sm6kSystemDeviceX25TxReserved13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxReserved13.setStatus("mandatory")
_Sm6kSystemDeviceX25TxReserved14_Type = Counter32
_Sm6kSystemDeviceX25TxReserved14_Object = MibTableColumn
sm6kSystemDeviceX25TxReserved14 = _Sm6kSystemDeviceX25TxReserved14_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 117),
    _Sm6kSystemDeviceX25TxReserved14_Type()
)
sm6kSystemDeviceX25TxReserved14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxReserved14.setStatus("mandatory")
_Sm6kSystemDeviceX25TxReserved15_Type = Counter32
_Sm6kSystemDeviceX25TxReserved15_Object = MibTableColumn
sm6kSystemDeviceX25TxReserved15 = _Sm6kSystemDeviceX25TxReserved15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 118),
    _Sm6kSystemDeviceX25TxReserved15_Type()
)
sm6kSystemDeviceX25TxReserved15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxReserved15.setStatus("mandatory")
_Sm6kSystemDeviceX25TxTotalPackets_Type = Counter32
_Sm6kSystemDeviceX25TxTotalPackets_Object = MibTableColumn
sm6kSystemDeviceX25TxTotalPackets = _Sm6kSystemDeviceX25TxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 119),
    _Sm6kSystemDeviceX25TxTotalPackets_Type()
)
sm6kSystemDeviceX25TxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25TxTotalPackets.setStatus("mandatory")
_Sm6kSystemDeviceX25RxUnknownSize_Type = Counter32
_Sm6kSystemDeviceX25RxUnknownSize_Object = MibTableColumn
sm6kSystemDeviceX25RxUnknownSize = _Sm6kSystemDeviceX25RxUnknownSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 120),
    _Sm6kSystemDeviceX25RxUnknownSize_Type()
)
sm6kSystemDeviceX25RxUnknownSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxUnknownSize.setStatus("mandatory")
_Sm6kSystemDeviceX25RxReserved1_Type = Counter32
_Sm6kSystemDeviceX25RxReserved1_Object = MibTableColumn
sm6kSystemDeviceX25RxReserved1 = _Sm6kSystemDeviceX25RxReserved1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 121),
    _Sm6kSystemDeviceX25RxReserved1_Type()
)
sm6kSystemDeviceX25RxReserved1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxReserved1.setStatus("mandatory")
_Sm6kSystemDeviceX25RxReserved2_Type = Counter32
_Sm6kSystemDeviceX25RxReserved2_Object = MibTableColumn
sm6kSystemDeviceX25RxReserved2 = _Sm6kSystemDeviceX25RxReserved2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 122),
    _Sm6kSystemDeviceX25RxReserved2_Type()
)
sm6kSystemDeviceX25RxReserved2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxReserved2.setStatus("mandatory")
_Sm6kSystemDeviceX25RxReserved3_Type = Counter32
_Sm6kSystemDeviceX25RxReserved3_Object = MibTableColumn
sm6kSystemDeviceX25RxReserved3 = _Sm6kSystemDeviceX25RxReserved3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 123),
    _Sm6kSystemDeviceX25RxReserved3_Type()
)
sm6kSystemDeviceX25RxReserved3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxReserved3.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx0x15_Type = Counter32
_Sm6kSystemDeviceX25Rx0x15_Object = MibTableColumn
sm6kSystemDeviceX25Rx0x15 = _Sm6kSystemDeviceX25Rx0x15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 124),
    _Sm6kSystemDeviceX25Rx0x15_Type()
)
sm6kSystemDeviceX25Rx0x15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx0x15.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx16x31_Type = Counter32
_Sm6kSystemDeviceX25Rx16x31_Object = MibTableColumn
sm6kSystemDeviceX25Rx16x31 = _Sm6kSystemDeviceX25Rx16x31_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 125),
    _Sm6kSystemDeviceX25Rx16x31_Type()
)
sm6kSystemDeviceX25Rx16x31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx16x31.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx32x63_Type = Counter32
_Sm6kSystemDeviceX25Rx32x63_Object = MibTableColumn
sm6kSystemDeviceX25Rx32x63 = _Sm6kSystemDeviceX25Rx32x63_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 126),
    _Sm6kSystemDeviceX25Rx32x63_Type()
)
sm6kSystemDeviceX25Rx32x63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx32x63.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx64x127_Type = Counter32
_Sm6kSystemDeviceX25Rx64x127_Object = MibTableColumn
sm6kSystemDeviceX25Rx64x127 = _Sm6kSystemDeviceX25Rx64x127_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 127),
    _Sm6kSystemDeviceX25Rx64x127_Type()
)
sm6kSystemDeviceX25Rx64x127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx64x127.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx128x255_Type = Counter32
_Sm6kSystemDeviceX25Rx128x255_Object = MibTableColumn
sm6kSystemDeviceX25Rx128x255 = _Sm6kSystemDeviceX25Rx128x255_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 128),
    _Sm6kSystemDeviceX25Rx128x255_Type()
)
sm6kSystemDeviceX25Rx128x255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx128x255.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx256x511_Type = Counter32
_Sm6kSystemDeviceX25Rx256x511_Object = MibTableColumn
sm6kSystemDeviceX25Rx256x511 = _Sm6kSystemDeviceX25Rx256x511_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 129),
    _Sm6kSystemDeviceX25Rx256x511_Type()
)
sm6kSystemDeviceX25Rx256x511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx256x511.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx512x1023_Type = Counter32
_Sm6kSystemDeviceX25Rx512x1023_Object = MibTableColumn
sm6kSystemDeviceX25Rx512x1023 = _Sm6kSystemDeviceX25Rx512x1023_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 130),
    _Sm6kSystemDeviceX25Rx512x1023_Type()
)
sm6kSystemDeviceX25Rx512x1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx512x1023.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx1024x2047_Type = Counter32
_Sm6kSystemDeviceX25Rx1024x2047_Object = MibTableColumn
sm6kSystemDeviceX25Rx1024x2047 = _Sm6kSystemDeviceX25Rx1024x2047_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 131),
    _Sm6kSystemDeviceX25Rx1024x2047_Type()
)
sm6kSystemDeviceX25Rx1024x2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx1024x2047.setStatus("mandatory")
_Sm6kSystemDeviceX25Rx2048x4095_Type = Counter32
_Sm6kSystemDeviceX25Rx2048x4095_Object = MibTableColumn
sm6kSystemDeviceX25Rx2048x4095 = _Sm6kSystemDeviceX25Rx2048x4095_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 132),
    _Sm6kSystemDeviceX25Rx2048x4095_Type()
)
sm6kSystemDeviceX25Rx2048x4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Rx2048x4095.setStatus("mandatory")
_Sm6kSystemDeviceX25RxReserved13_Type = Counter32
_Sm6kSystemDeviceX25RxReserved13_Object = MibTableColumn
sm6kSystemDeviceX25RxReserved13 = _Sm6kSystemDeviceX25RxReserved13_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 133),
    _Sm6kSystemDeviceX25RxReserved13_Type()
)
sm6kSystemDeviceX25RxReserved13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxReserved13.setStatus("mandatory")
_Sm6kSystemDeviceX25RxReserved14_Type = Counter32
_Sm6kSystemDeviceX25RxReserved14_Object = MibTableColumn
sm6kSystemDeviceX25RxReserved14 = _Sm6kSystemDeviceX25RxReserved14_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 134),
    _Sm6kSystemDeviceX25RxReserved14_Type()
)
sm6kSystemDeviceX25RxReserved14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxReserved14.setStatus("mandatory")
_Sm6kSystemDeviceX25RxReserved15_Type = Counter32
_Sm6kSystemDeviceX25RxReserved15_Object = MibTableColumn
sm6kSystemDeviceX25RxReserved15 = _Sm6kSystemDeviceX25RxReserved15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 135),
    _Sm6kSystemDeviceX25RxReserved15_Type()
)
sm6kSystemDeviceX25RxReserved15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxReserved15.setStatus("mandatory")
_Sm6kSystemDeviceX25RxTotalPackets_Type = Counter32
_Sm6kSystemDeviceX25RxTotalPackets_Object = MibTableColumn
sm6kSystemDeviceX25RxTotalPackets = _Sm6kSystemDeviceX25RxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 136),
    _Sm6kSystemDeviceX25RxTotalPackets_Type()
)
sm6kSystemDeviceX25RxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RxTotalPackets.setStatus("mandatory")


class _Sm6kSystemDeviceX25Clear_Type(Integer32):
    """Custom type sm6kSystemDeviceX25Clear based on Integer32"""
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


_Sm6kSystemDeviceX25Clear_Type.__name__ = "Integer32"
_Sm6kSystemDeviceX25Clear_Object = MibTableColumn
sm6kSystemDeviceX25Clear = _Sm6kSystemDeviceX25Clear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 2, 1, 137),
    _Sm6kSystemDeviceX25Clear_Type()
)
sm6kSystemDeviceX25Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25Clear.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteCount_Type = Integer32
_Sm6kSystemDeviceX25RouteCount_Object = MibScalar
sm6kSystemDeviceX25RouteCount = _Sm6kSystemDeviceX25RouteCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 3),
    _Sm6kSystemDeviceX25RouteCount_Type()
)
sm6kSystemDeviceX25RouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteCount.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteTable_Object = MibTable
sm6kSystemDeviceX25RouteTable = _Sm6kSystemDeviceX25RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4)
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteTable.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteEntry_Object = MibTableRow
sm6kSystemDeviceX25RouteEntry = _Sm6kSystemDeviceX25RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1)
)
sm6kSystemDeviceX25RouteEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemDeviceX25RouteNumber"),
)
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteEntry.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteNumber_Type = Integer32
_Sm6kSystemDeviceX25RouteNumber_Object = MibTableColumn
sm6kSystemDeviceX25RouteNumber = _Sm6kSystemDeviceX25RouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 1),
    _Sm6kSystemDeviceX25RouteNumber_Type()
)
sm6kSystemDeviceX25RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteNumber.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteEntryName_Type = DisplayString
_Sm6kSystemDeviceX25RouteEntryName_Object = MibTableColumn
sm6kSystemDeviceX25RouteEntryName = _Sm6kSystemDeviceX25RouteEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 2),
    _Sm6kSystemDeviceX25RouteEntryName_Type()
)
sm6kSystemDeviceX25RouteEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteEntryName.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteUserName_Type = DisplayString
_Sm6kSystemDeviceX25RouteUserName_Object = MibTableColumn
sm6kSystemDeviceX25RouteUserName = _Sm6kSystemDeviceX25RouteUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 3),
    _Sm6kSystemDeviceX25RouteUserName_Type()
)
sm6kSystemDeviceX25RouteUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteUserName.setStatus("mandatory")
_Sm6kSystemDeviceX25RoutePort_Type = DisplayString
_Sm6kSystemDeviceX25RoutePort_Object = MibTableColumn
sm6kSystemDeviceX25RoutePort = _Sm6kSystemDeviceX25RoutePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 4),
    _Sm6kSystemDeviceX25RoutePort_Type()
)
sm6kSystemDeviceX25RoutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RoutePort.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteCallingAddress_Type = DisplayString
_Sm6kSystemDeviceX25RouteCallingAddress_Object = MibTableColumn
sm6kSystemDeviceX25RouteCallingAddress = _Sm6kSystemDeviceX25RouteCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 5),
    _Sm6kSystemDeviceX25RouteCallingAddress_Type()
)
sm6kSystemDeviceX25RouteCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteCallingAddress.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteCalledSubaddress_Type = DisplayString
_Sm6kSystemDeviceX25RouteCalledSubaddress_Object = MibTableColumn
sm6kSystemDeviceX25RouteCalledSubaddress = _Sm6kSystemDeviceX25RouteCalledSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 6),
    _Sm6kSystemDeviceX25RouteCalledSubaddress_Type()
)
sm6kSystemDeviceX25RouteCalledSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteCalledSubaddress.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteCallingAddressExt_Type = DisplayString
_Sm6kSystemDeviceX25RouteCallingAddressExt_Object = MibTableColumn
sm6kSystemDeviceX25RouteCallingAddressExt = _Sm6kSystemDeviceX25RouteCallingAddressExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 7),
    _Sm6kSystemDeviceX25RouteCallingAddressExt_Type()
)
sm6kSystemDeviceX25RouteCallingAddressExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteCallingAddressExt.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteCalledAddressExt_Type = DisplayString
_Sm6kSystemDeviceX25RouteCalledAddressExt_Object = MibTableColumn
sm6kSystemDeviceX25RouteCalledAddressExt = _Sm6kSystemDeviceX25RouteCalledAddressExt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 8),
    _Sm6kSystemDeviceX25RouteCalledAddressExt_Type()
)
sm6kSystemDeviceX25RouteCalledAddressExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteCalledAddressExt.setStatus("mandatory")
_Sm6kSystemDeviceX25RouteCalledUserData_Type = DisplayString
_Sm6kSystemDeviceX25RouteCalledUserData_Object = MibTableColumn
sm6kSystemDeviceX25RouteCalledUserData = _Sm6kSystemDeviceX25RouteCalledUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 9),
    _Sm6kSystemDeviceX25RouteCalledUserData_Type()
)
sm6kSystemDeviceX25RouteCalledUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteCalledUserData.setStatus("mandatory")
_Sm6kSystemDeviceX25RoutePriority_Type = Integer32
_Sm6kSystemDeviceX25RoutePriority_Object = MibTableColumn
sm6kSystemDeviceX25RoutePriority = _Sm6kSystemDeviceX25RoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 10),
    _Sm6kSystemDeviceX25RoutePriority_Type()
)
sm6kSystemDeviceX25RoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RoutePriority.setStatus("mandatory")


class _Sm6kSystemDeviceX25RouteAction_Type(Integer32):
    """Custom type sm6kSystemDeviceX25RouteAction based on Integer32"""
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


_Sm6kSystemDeviceX25RouteAction_Type.__name__ = "Integer32"
_Sm6kSystemDeviceX25RouteAction_Object = MibTableColumn
sm6kSystemDeviceX25RouteAction = _Sm6kSystemDeviceX25RouteAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 3, 4, 4, 1, 11),
    _Sm6kSystemDeviceX25RouteAction_Type()
)
sm6kSystemDeviceX25RouteAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemDeviceX25RouteAction.setStatus("mandatory")
_Sm6kSystemPagingInformation_ObjectIdentity = ObjectIdentity
sm6kSystemPagingInformation = _Sm6kSystemPagingInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4)
)
_Sm6kSystemFreePagingSpace_Type = Integer32
_Sm6kSystemFreePagingSpace_Object = MibScalar
sm6kSystemFreePagingSpace = _Sm6kSystemFreePagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 1),
    _Sm6kSystemFreePagingSpace_Type()
)
sm6kSystemFreePagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFreePagingSpace.setStatus("mandatory")
_Sm6kSystemFreePagingSpaceUntilKill_Type = Integer32
_Sm6kSystemFreePagingSpaceUntilKill_Object = MibScalar
sm6kSystemFreePagingSpaceUntilKill = _Sm6kSystemFreePagingSpaceUntilKill_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 2),
    _Sm6kSystemFreePagingSpaceUntilKill_Type()
)
sm6kSystemFreePagingSpaceUntilKill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFreePagingSpaceUntilKill.setStatus("mandatory")
_Sm6kSystemFreePagingSpaceUntilKillPercent_Type = Integer32
_Sm6kSystemFreePagingSpaceUntilKillPercent_Object = MibScalar
sm6kSystemFreePagingSpaceUntilKillPercent = _Sm6kSystemFreePagingSpaceUntilKillPercent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 3),
    _Sm6kSystemFreePagingSpaceUntilKillPercent_Type()
)
sm6kSystemFreePagingSpaceUntilKillPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFreePagingSpaceUntilKillPercent.setStatus("mandatory")
_Sm6kSystemPagingSpace_ObjectIdentity = ObjectIdentity
sm6kSystemPagingSpace = _Sm6kSystemPagingSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4)
)
_Sm6kSystemPagingSpaceCount_Type = Gauge32
_Sm6kSystemPagingSpaceCount_Object = MibScalar
sm6kSystemPagingSpaceCount = _Sm6kSystemPagingSpaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 1),
    _Sm6kSystemPagingSpaceCount_Type()
)
sm6kSystemPagingSpaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceCount.setStatus("mandatory")
_Sm6kSystemPagingSpaceTable_Object = MibTable
sm6kSystemPagingSpaceTable = _Sm6kSystemPagingSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceTable.setStatus("mandatory")
_Sm6kSystemPagingSpaceEntry_Object = MibTableRow
sm6kSystemPagingSpaceEntry = _Sm6kSystemPagingSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1)
)
sm6kSystemPagingSpaceEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemPagingSpaceName"),
)
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceEntry.setStatus("mandatory")
_Sm6kSystemPagingSpaceName_Type = DisplayString
_Sm6kSystemPagingSpaceName_Object = MibTableColumn
sm6kSystemPagingSpaceName = _Sm6kSystemPagingSpaceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 1),
    _Sm6kSystemPagingSpaceName_Type()
)
sm6kSystemPagingSpaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceName.setStatus("mandatory")
_Sm6kSystemPagingSpacePhysicalVolume_Type = DisplayString
_Sm6kSystemPagingSpacePhysicalVolume_Object = MibTableColumn
sm6kSystemPagingSpacePhysicalVolume = _Sm6kSystemPagingSpacePhysicalVolume_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 2),
    _Sm6kSystemPagingSpacePhysicalVolume_Type()
)
sm6kSystemPagingSpacePhysicalVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpacePhysicalVolume.setStatus("mandatory")
_Sm6kSystemPagingSpaceVolumeGroup_Type = DisplayString
_Sm6kSystemPagingSpaceVolumeGroup_Object = MibTableColumn
sm6kSystemPagingSpaceVolumeGroup = _Sm6kSystemPagingSpaceVolumeGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 3),
    _Sm6kSystemPagingSpaceVolumeGroup_Type()
)
sm6kSystemPagingSpaceVolumeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceVolumeGroup.setStatus("mandatory")
_Sm6kSystemPagingSpaceSize_Type = Integer32
_Sm6kSystemPagingSpaceSize_Object = MibTableColumn
sm6kSystemPagingSpaceSize = _Sm6kSystemPagingSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 4),
    _Sm6kSystemPagingSpaceSize_Type()
)
sm6kSystemPagingSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceSize.setStatus("mandatory")
_Sm6kSystemPagingSpacePercentUsed_Type = Gauge32
_Sm6kSystemPagingSpacePercentUsed_Object = MibTableColumn
sm6kSystemPagingSpacePercentUsed = _Sm6kSystemPagingSpacePercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 5),
    _Sm6kSystemPagingSpacePercentUsed_Type()
)
sm6kSystemPagingSpacePercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpacePercentUsed.setStatus("mandatory")
_Sm6kSystemPagingSpaceActive_Type = DisplayString
_Sm6kSystemPagingSpaceActive_Object = MibTableColumn
sm6kSystemPagingSpaceActive = _Sm6kSystemPagingSpaceActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 6),
    _Sm6kSystemPagingSpaceActive_Type()
)
sm6kSystemPagingSpaceActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceActive.setStatus("mandatory")
_Sm6kSystemPagingSpaceAuto_Type = DisplayString
_Sm6kSystemPagingSpaceAuto_Object = MibTableColumn
sm6kSystemPagingSpaceAuto = _Sm6kSystemPagingSpaceAuto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 7),
    _Sm6kSystemPagingSpaceAuto_Type()
)
sm6kSystemPagingSpaceAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceAuto.setStatus("mandatory")
_Sm6kSystemPagingSpaceType_Type = DisplayString
_Sm6kSystemPagingSpaceType_Object = MibTableColumn
sm6kSystemPagingSpaceType = _Sm6kSystemPagingSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 4, 2, 1, 8),
    _Sm6kSystemPagingSpaceType_Type()
)
sm6kSystemPagingSpaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingSpaceType.setStatus("mandatory")
_Sm6kSystemPagingStatistics_ObjectIdentity = ObjectIdentity
sm6kSystemPagingStatistics = _Sm6kSystemPagingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5)
)
_Sm6kSystemPagingStatisticsPollingInterval_Type = Integer32
_Sm6kSystemPagingStatisticsPollingInterval_Object = MibScalar
sm6kSystemPagingStatisticsPollingInterval = _Sm6kSystemPagingStatisticsPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 1),
    _Sm6kSystemPagingStatisticsPollingInterval_Type()
)
sm6kSystemPagingStatisticsPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPollingInterval.setStatus("mandatory")
_Sm6kSystemPagingStatisticsTable_Object = MibTable
sm6kSystemPagingStatisticsTable = _Sm6kSystemPagingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsTable.setStatus("mandatory")
_Sm6kSystemPagingStatisticsEntry_Object = MibTableRow
sm6kSystemPagingStatisticsEntry = _Sm6kSystemPagingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1)
)
sm6kSystemPagingStatisticsEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemPagingStatisticsName"),
)
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsEntry.setStatus("mandatory")
_Sm6kSystemPagingStatisticsName_Type = DisplayString
_Sm6kSystemPagingStatisticsName_Object = MibTableColumn
sm6kSystemPagingStatisticsName = _Sm6kSystemPagingStatisticsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 1),
    _Sm6kSystemPagingStatisticsName_Type()
)
sm6kSystemPagingStatisticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsName.setStatus("mandatory")
_Sm6kSystemPagingStatisticsIntervalStartTime_Type = DisplayString
_Sm6kSystemPagingStatisticsIntervalStartTime_Object = MibTableColumn
sm6kSystemPagingStatisticsIntervalStartTime = _Sm6kSystemPagingStatisticsIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 2),
    _Sm6kSystemPagingStatisticsIntervalStartTime_Type()
)
sm6kSystemPagingStatisticsIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsIntervalStartTime.setStatus("mandatory")
_Sm6kSystemPagingStatisticsIntervalLength_Type = TimeTicks
_Sm6kSystemPagingStatisticsIntervalLength_Object = MibTableColumn
sm6kSystemPagingStatisticsIntervalLength = _Sm6kSystemPagingStatisticsIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 3),
    _Sm6kSystemPagingStatisticsIntervalLength_Type()
)
sm6kSystemPagingStatisticsIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsIntervalLength.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageFaults_Type = Integer32
_Sm6kSystemPagingStatisticsPageFaults_Object = MibTableColumn
sm6kSystemPagingStatisticsPageFaults = _Sm6kSystemPagingStatisticsPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 4),
    _Sm6kSystemPagingStatisticsPageFaults_Type()
)
sm6kSystemPagingStatisticsPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageFaults.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageReclaims_Type = Integer32
_Sm6kSystemPagingStatisticsPageReclaims_Object = MibTableColumn
sm6kSystemPagingStatisticsPageReclaims = _Sm6kSystemPagingStatisticsPageReclaims_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 5),
    _Sm6kSystemPagingStatisticsPageReclaims_Type()
)
sm6kSystemPagingStatisticsPageReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageReclaims.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPagesPagedIn_Type = Integer32
_Sm6kSystemPagingStatisticsPagesPagedIn_Object = MibTableColumn
sm6kSystemPagingStatisticsPagesPagedIn = _Sm6kSystemPagingStatisticsPagesPagedIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 6),
    _Sm6kSystemPagingStatisticsPagesPagedIn_Type()
)
sm6kSystemPagingStatisticsPagesPagedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPagesPagedIn.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPagesPagedOut_Type = Integer32
_Sm6kSystemPagingStatisticsPagesPagedOut_Object = MibTableColumn
sm6kSystemPagingStatisticsPagesPagedOut = _Sm6kSystemPagingStatisticsPagesPagedOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 7),
    _Sm6kSystemPagingStatisticsPagesPagedOut_Type()
)
sm6kSystemPagingStatisticsPagesPagedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPagesPagedOut.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageInsFromPagingSpace_Type = Integer32
_Sm6kSystemPagingStatisticsPageInsFromPagingSpace_Object = MibTableColumn
sm6kSystemPagingStatisticsPageInsFromPagingSpace = _Sm6kSystemPagingStatisticsPageInsFromPagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 8),
    _Sm6kSystemPagingStatisticsPageInsFromPagingSpace_Type()
)
sm6kSystemPagingStatisticsPageInsFromPagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageInsFromPagingSpace.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageOutsFromPagingSpace_Type = Integer32
_Sm6kSystemPagingStatisticsPageOutsFromPagingSpace_Object = MibTableColumn
sm6kSystemPagingStatisticsPageOutsFromPagingSpace = _Sm6kSystemPagingStatisticsPageOutsFromPagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 9),
    _Sm6kSystemPagingStatisticsPageOutsFromPagingSpace_Type()
)
sm6kSystemPagingStatisticsPageOutsFromPagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageOutsFromPagingSpace.setStatus("mandatory")
_Sm6kSystemPagingStatisticsStartIOs_Type = Integer32
_Sm6kSystemPagingStatisticsStartIOs_Object = MibTableColumn
sm6kSystemPagingStatisticsStartIOs = _Sm6kSystemPagingStatisticsStartIOs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 10),
    _Sm6kSystemPagingStatisticsStartIOs_Type()
)
sm6kSystemPagingStatisticsStartIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsStartIOs.setStatus("mandatory")
_Sm6kSystemPagingStatisticsDoneIOs_Type = Integer32
_Sm6kSystemPagingStatisticsDoneIOs_Object = MibTableColumn
sm6kSystemPagingStatisticsDoneIOs = _Sm6kSystemPagingStatisticsDoneIOs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 11),
    _Sm6kSystemPagingStatisticsDoneIOs_Type()
)
sm6kSystemPagingStatisticsDoneIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsDoneIOs.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageScans_Type = Integer32
_Sm6kSystemPagingStatisticsPageScans_Object = MibTableColumn
sm6kSystemPagingStatisticsPageScans = _Sm6kSystemPagingStatisticsPageScans_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 12),
    _Sm6kSystemPagingStatisticsPageScans_Type()
)
sm6kSystemPagingStatisticsPageScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageScans.setStatus("mandatory")
_Sm6kSystemPagingStatisticsScanClockCycles_Type = Integer32
_Sm6kSystemPagingStatisticsScanClockCycles_Object = MibTableColumn
sm6kSystemPagingStatisticsScanClockCycles = _Sm6kSystemPagingStatisticsScanClockCycles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 13),
    _Sm6kSystemPagingStatisticsScanClockCycles_Type()
)
sm6kSystemPagingStatisticsScanClockCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsScanClockCycles.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageSteals_Type = Integer32
_Sm6kSystemPagingStatisticsPageSteals_Object = MibTableColumn
sm6kSystemPagingStatisticsPageSteals = _Sm6kSystemPagingStatisticsPageSteals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 14),
    _Sm6kSystemPagingStatisticsPageSteals_Type()
)
sm6kSystemPagingStatisticsPageSteals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageSteals.setStatus("mandatory")
_Sm6kSystemPagingStatisticsFreeFrameWaits_Type = Integer32
_Sm6kSystemPagingStatisticsFreeFrameWaits_Object = MibTableColumn
sm6kSystemPagingStatisticsFreeFrameWaits = _Sm6kSystemPagingStatisticsFreeFrameWaits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 15),
    _Sm6kSystemPagingStatisticsFreeFrameWaits_Type()
)
sm6kSystemPagingStatisticsFreeFrameWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsFreeFrameWaits.setStatus("mandatory")
_Sm6kSystemPagingStatisticsExtendXPTWaits_Type = Integer32
_Sm6kSystemPagingStatisticsExtendXPTWaits_Object = MibTableColumn
sm6kSystemPagingStatisticsExtendXPTWaits = _Sm6kSystemPagingStatisticsExtendXPTWaits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 16),
    _Sm6kSystemPagingStatisticsExtendXPTWaits_Type()
)
sm6kSystemPagingStatisticsExtendXPTWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsExtendXPTWaits.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPendingIOWaits_Type = Integer32
_Sm6kSystemPagingStatisticsPendingIOWaits_Object = MibTableColumn
sm6kSystemPagingStatisticsPendingIOWaits = _Sm6kSystemPagingStatisticsPendingIOWaits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 17),
    _Sm6kSystemPagingStatisticsPendingIOWaits_Type()
)
sm6kSystemPagingStatisticsPendingIOWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPendingIOWaits.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageFaultsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPageFaultsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageFaultsMinimum = _Sm6kSystemPagingStatisticsPageFaultsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 18),
    _Sm6kSystemPagingStatisticsPageFaultsMinimum_Type()
)
sm6kSystemPagingStatisticsPageFaultsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageFaultsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageReclaimsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPageReclaimsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageReclaimsMinimum = _Sm6kSystemPagingStatisticsPageReclaimsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 19),
    _Sm6kSystemPagingStatisticsPageReclaimsMinimum_Type()
)
sm6kSystemPagingStatisticsPageReclaimsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageReclaimsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPagesPagedInMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPagesPagedInMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPagesPagedInMinimum = _Sm6kSystemPagingStatisticsPagesPagedInMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 20),
    _Sm6kSystemPagingStatisticsPagesPagedInMinimum_Type()
)
sm6kSystemPagingStatisticsPagesPagedInMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPagesPagedInMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPagesPagedOutMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPagesPagedOutMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPagesPagedOutMinimum = _Sm6kSystemPagingStatisticsPagesPagedOutMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 21),
    _Sm6kSystemPagingStatisticsPagesPagedOutMinimum_Type()
)
sm6kSystemPagingStatisticsPagesPagedOutMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPagesPagedOutMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum = _Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 22),
    _Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum_Type()
)
sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum = _Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 23),
    _Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum_Type()
)
sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsStartIOsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsStartIOsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsStartIOsMinimum = _Sm6kSystemPagingStatisticsStartIOsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 24),
    _Sm6kSystemPagingStatisticsStartIOsMinimum_Type()
)
sm6kSystemPagingStatisticsStartIOsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsStartIOsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsDoneIOsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsDoneIOsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsDoneIOsMinimum = _Sm6kSystemPagingStatisticsDoneIOsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 25),
    _Sm6kSystemPagingStatisticsDoneIOsMinimum_Type()
)
sm6kSystemPagingStatisticsDoneIOsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsDoneIOsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageScansMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPageScansMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageScansMinimum = _Sm6kSystemPagingStatisticsPageScansMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 26),
    _Sm6kSystemPagingStatisticsPageScansMinimum_Type()
)
sm6kSystemPagingStatisticsPageScansMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageScansMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsScanClockCyclesMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsScanClockCyclesMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsScanClockCyclesMinimum = _Sm6kSystemPagingStatisticsScanClockCyclesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 27),
    _Sm6kSystemPagingStatisticsScanClockCyclesMinimum_Type()
)
sm6kSystemPagingStatisticsScanClockCyclesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsScanClockCyclesMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageStealsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPageStealsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageStealsMinimum = _Sm6kSystemPagingStatisticsPageStealsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 28),
    _Sm6kSystemPagingStatisticsPageStealsMinimum_Type()
)
sm6kSystemPagingStatisticsPageStealsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageStealsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsFreeFrameWaitsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsFreeFrameWaitsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsFreeFrameWaitsMinimum = _Sm6kSystemPagingStatisticsFreeFrameWaitsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 29),
    _Sm6kSystemPagingStatisticsFreeFrameWaitsMinimum_Type()
)
sm6kSystemPagingStatisticsFreeFrameWaitsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsFreeFrameWaitsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsExtendXPTWaitsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsExtendXPTWaitsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsExtendXPTWaitsMinimum = _Sm6kSystemPagingStatisticsExtendXPTWaitsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 30),
    _Sm6kSystemPagingStatisticsExtendXPTWaitsMinimum_Type()
)
sm6kSystemPagingStatisticsExtendXPTWaitsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsExtendXPTWaitsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPendingIOWaitsMinimum_Type = Integer32
_Sm6kSystemPagingStatisticsPendingIOWaitsMinimum_Object = MibTableColumn
sm6kSystemPagingStatisticsPendingIOWaitsMinimum = _Sm6kSystemPagingStatisticsPendingIOWaitsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 31),
    _Sm6kSystemPagingStatisticsPendingIOWaitsMinimum_Type()
)
sm6kSystemPagingStatisticsPendingIOWaitsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPendingIOWaitsMinimum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageFaultsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPageFaultsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageFaultsMaximum = _Sm6kSystemPagingStatisticsPageFaultsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 32),
    _Sm6kSystemPagingStatisticsPageFaultsMaximum_Type()
)
sm6kSystemPagingStatisticsPageFaultsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageFaultsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageReclaimsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPageReclaimsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageReclaimsMaximum = _Sm6kSystemPagingStatisticsPageReclaimsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 33),
    _Sm6kSystemPagingStatisticsPageReclaimsMaximum_Type()
)
sm6kSystemPagingStatisticsPageReclaimsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageReclaimsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPagesPagedInMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPagesPagedInMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPagesPagedInMaximum = _Sm6kSystemPagingStatisticsPagesPagedInMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 34),
    _Sm6kSystemPagingStatisticsPagesPagedInMaximum_Type()
)
sm6kSystemPagingStatisticsPagesPagedInMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPagesPagedInMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPagesPagedOutMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPagesPagedOutMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPagesPagedOutMaximum = _Sm6kSystemPagingStatisticsPagesPagedOutMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 35),
    _Sm6kSystemPagingStatisticsPagesPagedOutMaximum_Type()
)
sm6kSystemPagingStatisticsPagesPagedOutMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPagesPagedOutMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum = _Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 36),
    _Sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum_Type()
)
sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum = _Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 37),
    _Sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum_Type()
)
sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsStartIOsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsStartIOsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsStartIOsMaximum = _Sm6kSystemPagingStatisticsStartIOsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 38),
    _Sm6kSystemPagingStatisticsStartIOsMaximum_Type()
)
sm6kSystemPagingStatisticsStartIOsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsStartIOsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsDoneIOsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsDoneIOsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsDoneIOsMaximum = _Sm6kSystemPagingStatisticsDoneIOsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 39),
    _Sm6kSystemPagingStatisticsDoneIOsMaximum_Type()
)
sm6kSystemPagingStatisticsDoneIOsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsDoneIOsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageScansMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPageScansMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageScansMaximum = _Sm6kSystemPagingStatisticsPageScansMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 40),
    _Sm6kSystemPagingStatisticsPageScansMaximum_Type()
)
sm6kSystemPagingStatisticsPageScansMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageScansMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsScanClockCyclesMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsScanClockCyclesMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsScanClockCyclesMaximum = _Sm6kSystemPagingStatisticsScanClockCyclesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 41),
    _Sm6kSystemPagingStatisticsScanClockCyclesMaximum_Type()
)
sm6kSystemPagingStatisticsScanClockCyclesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsScanClockCyclesMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPageStealsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPageStealsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPageStealsMaximum = _Sm6kSystemPagingStatisticsPageStealsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 42),
    _Sm6kSystemPagingStatisticsPageStealsMaximum_Type()
)
sm6kSystemPagingStatisticsPageStealsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPageStealsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsFreeFrameWaitsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsFreeFrameWaitsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsFreeFrameWaitsMaximum = _Sm6kSystemPagingStatisticsFreeFrameWaitsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 43),
    _Sm6kSystemPagingStatisticsFreeFrameWaitsMaximum_Type()
)
sm6kSystemPagingStatisticsFreeFrameWaitsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsFreeFrameWaitsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsExtendXPTWaitsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsExtendXPTWaitsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsExtendXPTWaitsMaximum = _Sm6kSystemPagingStatisticsExtendXPTWaitsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 44),
    _Sm6kSystemPagingStatisticsExtendXPTWaitsMaximum_Type()
)
sm6kSystemPagingStatisticsExtendXPTWaitsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsExtendXPTWaitsMaximum.setStatus("mandatory")
_Sm6kSystemPagingStatisticsPendingIOWaitsMaximum_Type = Integer32
_Sm6kSystemPagingStatisticsPendingIOWaitsMaximum_Object = MibTableColumn
sm6kSystemPagingStatisticsPendingIOWaitsMaximum = _Sm6kSystemPagingStatisticsPendingIOWaitsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 4, 5, 2, 1, 45),
    _Sm6kSystemPagingStatisticsPendingIOWaitsMaximum_Type()
)
sm6kSystemPagingStatisticsPendingIOWaitsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemPagingStatisticsPendingIOWaitsMaximum.setStatus("mandatory")
_Sm6kSystemFileSystem_ObjectIdentity = ObjectIdentity
sm6kSystemFileSystem = _Sm6kSystemFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5)
)
_Sm6kSystemFileSystemMounted_Type = Gauge32
_Sm6kSystemFileSystemMounted_Object = MibScalar
sm6kSystemFileSystemMounted = _Sm6kSystemFileSystemMounted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 1),
    _Sm6kSystemFileSystemMounted_Type()
)
sm6kSystemFileSystemMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemMounted.setStatus("mandatory")
_Sm6kSystemFileSystemTable_Object = MibTable
sm6kSystemFileSystemTable = _Sm6kSystemFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemFileSystemTable.setStatus("mandatory")
_Sm6kSystemFileSystemEntry_Object = MibTableRow
sm6kSystemFileSystemEntry = _Sm6kSystemFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1)
)
sm6kSystemFileSystemEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemFileSystemName"),
)
if mibBuilder.loadTexts:
    sm6kSystemFileSystemEntry.setStatus("mandatory")
_Sm6kSystemFileSystemName_Type = DisplayString
_Sm6kSystemFileSystemName_Object = MibTableColumn
sm6kSystemFileSystemName = _Sm6kSystemFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 1),
    _Sm6kSystemFileSystemName_Type()
)
sm6kSystemFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemName.setStatus("mandatory")
_Sm6kSystemFileSystemSize_Type = Gauge32
_Sm6kSystemFileSystemSize_Object = MibTableColumn
sm6kSystemFileSystemSize = _Sm6kSystemFileSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 2),
    _Sm6kSystemFileSystemSize_Type()
)
sm6kSystemFileSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemSize.setStatus("mandatory")
_Sm6kSystemFileSystemFree_Type = Gauge32
_Sm6kSystemFileSystemFree_Object = MibTableColumn
sm6kSystemFileSystemFree = _Sm6kSystemFileSystemFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 3),
    _Sm6kSystemFileSystemFree_Type()
)
sm6kSystemFileSystemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemFree.setStatus("mandatory")
_Sm6kSystemFileSystemPercentUsed_Type = Gauge32
_Sm6kSystemFileSystemPercentUsed_Object = MibTableColumn
sm6kSystemFileSystemPercentUsed = _Sm6kSystemFileSystemPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 4),
    _Sm6kSystemFileSystemPercentUsed_Type()
)
sm6kSystemFileSystemPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemPercentUsed.setStatus("mandatory")
_Sm6kSystemFileSystemInodesUsed_Type = Gauge32
_Sm6kSystemFileSystemInodesUsed_Object = MibTableColumn
sm6kSystemFileSystemInodesUsed = _Sm6kSystemFileSystemInodesUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 5),
    _Sm6kSystemFileSystemInodesUsed_Type()
)
sm6kSystemFileSystemInodesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemInodesUsed.setStatus("mandatory")
_Sm6kSystemFileSystemInodesPercentUsed_Type = Gauge32
_Sm6kSystemFileSystemInodesPercentUsed_Object = MibTableColumn
sm6kSystemFileSystemInodesPercentUsed = _Sm6kSystemFileSystemInodesPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 6),
    _Sm6kSystemFileSystemInodesPercentUsed_Type()
)
sm6kSystemFileSystemInodesPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemInodesPercentUsed.setStatus("mandatory")
_Sm6kSystemFileSystemInodeCount_Type = Gauge32
_Sm6kSystemFileSystemInodeCount_Object = MibTableColumn
sm6kSystemFileSystemInodeCount = _Sm6kSystemFileSystemInodeCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 7),
    _Sm6kSystemFileSystemInodeCount_Type()
)
sm6kSystemFileSystemInodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemInodeCount.setStatus("mandatory")
_Sm6kSystemFileSystemFileSystem_Type = DisplayString
_Sm6kSystemFileSystemFileSystem_Object = MibTableColumn
sm6kSystemFileSystemFileSystem = _Sm6kSystemFileSystemFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 8),
    _Sm6kSystemFileSystemFileSystem_Type()
)
sm6kSystemFileSystemFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemFileSystem.setStatus("mandatory")
_Sm6kSystemFileSystemRemote_Type = DisplayString
_Sm6kSystemFileSystemRemote_Object = MibTableColumn
sm6kSystemFileSystemRemote = _Sm6kSystemFileSystemRemote_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 5, 2, 1, 9),
    _Sm6kSystemFileSystemRemote_Type()
)
sm6kSystemFileSystemRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemFileSystemRemote.setStatus("mandatory")
_Sm6kSystemSubSystems_ObjectIdentity = ObjectIdentity
sm6kSystemSubSystems = _Sm6kSystemSubSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6)
)
_Sm6kSystemSubSystemsCount_Type = Gauge32
_Sm6kSystemSubSystemsCount_Object = MibScalar
sm6kSystemSubSystemsCount = _Sm6kSystemSubSystemsCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 1),
    _Sm6kSystemSubSystemsCount_Type()
)
sm6kSystemSubSystemsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsCount.setStatus("mandatory")
_Sm6kSystemSubSystemsTable_Object = MibTable
sm6kSystemSubSystemsTable = _Sm6kSystemSubSystemsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsTable.setStatus("mandatory")
_Sm6kSystemSubSystemsEntry_Object = MibTableRow
sm6kSystemSubSystemsEntry = _Sm6kSystemSubSystemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1)
)
sm6kSystemSubSystemsEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemSubSystemsName"),
)
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsEntry.setStatus("mandatory")
_Sm6kSystemSubSystemsName_Type = DisplayString
_Sm6kSystemSubSystemsName_Object = MibTableColumn
sm6kSystemSubSystemsName = _Sm6kSystemSubSystemsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 1),
    _Sm6kSystemSubSystemsName_Type()
)
sm6kSystemSubSystemsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsName.setStatus("mandatory")
_Sm6kSystemSubSystemsPID_Type = Integer32
_Sm6kSystemSubSystemsPID_Object = MibTableColumn
sm6kSystemSubSystemsPID = _Sm6kSystemSubSystemsPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 2),
    _Sm6kSystemSubSystemsPID_Type()
)
sm6kSystemSubSystemsPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsPID.setStatus("mandatory")
_Sm6kSystemSubSystemsStatusDescription_Type = DisplayString
_Sm6kSystemSubSystemsStatusDescription_Object = MibTableColumn
sm6kSystemSubSystemsStatusDescription = _Sm6kSystemSubSystemsStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 3),
    _Sm6kSystemSubSystemsStatusDescription_Type()
)
sm6kSystemSubSystemsStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsStatusDescription.setStatus("mandatory")
_Sm6kSystemSubSystemsStatusText_Type = DisplayString
_Sm6kSystemSubSystemsStatusText_Object = MibTableColumn
sm6kSystemSubSystemsStatusText = _Sm6kSystemSubSystemsStatusText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 4),
    _Sm6kSystemSubSystemsStatusText_Type()
)
sm6kSystemSubSystemsStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsStatusText.setStatus("mandatory")
_Sm6kSystemSubSystemsStatusCode_Type = Integer32
_Sm6kSystemSubSystemsStatusCode_Object = MibTableColumn
sm6kSystemSubSystemsStatusCode = _Sm6kSystemSubSystemsStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 6, 2, 1, 5),
    _Sm6kSystemSubSystemsStatusCode_Type()
)
sm6kSystemSubSystemsStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemSubSystemsStatusCode.setStatus("mandatory")
_Sm6kSystemProcess_ObjectIdentity = ObjectIdentity
sm6kSystemProcess = _Sm6kSystemProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7)
)
_Sm6kSystemProcessCount_Type = Gauge32
_Sm6kSystemProcessCount_Object = MibScalar
sm6kSystemProcessCount = _Sm6kSystemProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 1),
    _Sm6kSystemProcessCount_Type()
)
sm6kSystemProcessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessCount.setStatus("mandatory")
_Sm6kSystemProcessTable_Object = MibTable
sm6kSystemProcessTable = _Sm6kSystemProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemProcessTable.setStatus("mandatory")
_Sm6kSystemProcessEntry_Object = MibTableRow
sm6kSystemProcessEntry = _Sm6kSystemProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1)
)
sm6kSystemProcessEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemProcessCommand"),
    (0, "SYSMON6K-MIB", "sm6kSystemProcessPID"),
)
if mibBuilder.loadTexts:
    sm6kSystemProcessEntry.setStatus("mandatory")
_Sm6kSystemProcessLoginUser_Type = DisplayString
_Sm6kSystemProcessLoginUser_Object = MibTableColumn
sm6kSystemProcessLoginUser = _Sm6kSystemProcessLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 1),
    _Sm6kSystemProcessLoginUser_Type()
)
sm6kSystemProcessLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessLoginUser.setStatus("mandatory")
_Sm6kSystemProcessPID_Type = Integer32
_Sm6kSystemProcessPID_Object = MibTableColumn
sm6kSystemProcessPID = _Sm6kSystemProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 2),
    _Sm6kSystemProcessPID_Type()
)
sm6kSystemProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPID.setStatus("mandatory")
_Sm6kSystemProcessParentPID_Type = Integer32
_Sm6kSystemProcessParentPID_Object = MibTableColumn
sm6kSystemProcessParentPID = _Sm6kSystemProcessParentPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 3),
    _Sm6kSystemProcessParentPID_Type()
)
sm6kSystemProcessParentPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessParentPID.setStatus("mandatory")
_Sm6kSystemProcessCPUTime_Type = TimeTicks
_Sm6kSystemProcessCPUTime_Object = MibTableColumn
sm6kSystemProcessCPUTime = _Sm6kSystemProcessCPUTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 4),
    _Sm6kSystemProcessCPUTime_Type()
)
sm6kSystemProcessCPUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessCPUTime.setStatus("mandatory")
_Sm6kSystemProcessUserTime_Type = TimeTicks
_Sm6kSystemProcessUserTime_Object = MibTableColumn
sm6kSystemProcessUserTime = _Sm6kSystemProcessUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 5),
    _Sm6kSystemProcessUserTime_Type()
)
sm6kSystemProcessUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessUserTime.setStatus("mandatory")
_Sm6kSystemProcessSystemTime_Type = TimeTicks
_Sm6kSystemProcessSystemTime_Object = MibTableColumn
sm6kSystemProcessSystemTime = _Sm6kSystemProcessSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 6),
    _Sm6kSystemProcessSystemTime_Type()
)
sm6kSystemProcessSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessSystemTime.setStatus("mandatory")
_Sm6kSystemProcessPageFaultsIO_Type = Counter32
_Sm6kSystemProcessPageFaultsIO_Object = MibTableColumn
sm6kSystemProcessPageFaultsIO = _Sm6kSystemProcessPageFaultsIO_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 7),
    _Sm6kSystemProcessPageFaultsIO_Type()
)
sm6kSystemProcessPageFaultsIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPageFaultsIO.setStatus("mandatory")
_Sm6kSystemProcessPageFaultsNoIO_Type = Counter32
_Sm6kSystemProcessPageFaultsNoIO_Object = MibTableColumn
sm6kSystemProcessPageFaultsNoIO = _Sm6kSystemProcessPageFaultsNoIO_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 8),
    _Sm6kSystemProcessPageFaultsNoIO_Type()
)
sm6kSystemProcessPageFaultsNoIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPageFaultsNoIO.setStatus("mandatory")
_Sm6kSystemProcessPriority_Type = Integer32
_Sm6kSystemProcessPriority_Object = MibTableColumn
sm6kSystemProcessPriority = _Sm6kSystemProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 9),
    _Sm6kSystemProcessPriority_Type()
)
sm6kSystemProcessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPriority.setStatus("mandatory")
_Sm6kSystemProcessNice_Type = Integer32
_Sm6kSystemProcessNice_Object = MibTableColumn
sm6kSystemProcessNice = _Sm6kSystemProcessNice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 10),
    _Sm6kSystemProcessNice_Type()
)
sm6kSystemProcessNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessNice.setStatus("mandatory")


class _Sm6kSystemProcessState_Type(Integer32):
    """Custom type sm6kSystemProcessState based on Integer32"""
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


_Sm6kSystemProcessState_Type.__name__ = "Integer32"
_Sm6kSystemProcessState_Object = MibTableColumn
sm6kSystemProcessState = _Sm6kSystemProcessState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 11),
    _Sm6kSystemProcessState_Type()
)
sm6kSystemProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessState.setStatus("mandatory")


class _Sm6kSystemProcessWait_Type(Integer32):
    """Custom type sm6kSystemProcessWait based on Integer32"""
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


_Sm6kSystemProcessWait_Type.__name__ = "Integer32"
_Sm6kSystemProcessWait_Object = MibTableColumn
sm6kSystemProcessWait = _Sm6kSystemProcessWait_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 12),
    _Sm6kSystemProcessWait_Type()
)
sm6kSystemProcessWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessWait.setStatus("mandatory")
_Sm6kSystemProcessDataResidentSetSize_Type = Integer32
_Sm6kSystemProcessDataResidentSetSize_Object = MibTableColumn
sm6kSystemProcessDataResidentSetSize = _Sm6kSystemProcessDataResidentSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 13),
    _Sm6kSystemProcessDataResidentSetSize_Type()
)
sm6kSystemProcessDataResidentSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessDataResidentSetSize.setStatus("mandatory")
_Sm6kSystemProcessTextResidentSetSize_Type = Integer32
_Sm6kSystemProcessTextResidentSetSize_Object = MibTableColumn
sm6kSystemProcessTextResidentSetSize = _Sm6kSystemProcessTextResidentSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 14),
    _Sm6kSystemProcessTextResidentSetSize_Type()
)
sm6kSystemProcessTextResidentSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessTextResidentSetSize.setStatus("mandatory")
_Sm6kSystemProcessImageSize_Type = Integer32
_Sm6kSystemProcessImageSize_Object = MibTableColumn
sm6kSystemProcessImageSize = _Sm6kSystemProcessImageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 15),
    _Sm6kSystemProcessImageSize_Type()
)
sm6kSystemProcessImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessImageSize.setStatus("mandatory")
_Sm6kSystemProcessDataVirtualMemorySize_Type = Integer32
_Sm6kSystemProcessDataVirtualMemorySize_Object = MibTableColumn
sm6kSystemProcessDataVirtualMemorySize = _Sm6kSystemProcessDataVirtualMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 16),
    _Sm6kSystemProcessDataVirtualMemorySize_Type()
)
sm6kSystemProcessDataVirtualMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessDataVirtualMemorySize.setStatus("mandatory")
_Sm6kSystemProcessPercentMemory_Type = Integer32
_Sm6kSystemProcessPercentMemory_Object = MibTableColumn
sm6kSystemProcessPercentMemory = _Sm6kSystemProcessPercentMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 17),
    _Sm6kSystemProcessPercentMemory_Type()
)
sm6kSystemProcessPercentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPercentMemory.setStatus("mandatory")
_Sm6kSystemProcessCPU_Type = Integer32
_Sm6kSystemProcessCPU_Object = MibTableColumn
sm6kSystemProcessCPU = _Sm6kSystemProcessCPU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 18),
    _Sm6kSystemProcessCPU_Type()
)
sm6kSystemProcessCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessCPU.setStatus("mandatory")
_Sm6kSystemProcessStartTime_Type = DisplayString
_Sm6kSystemProcessStartTime_Object = MibTableColumn
sm6kSystemProcessStartTime = _Sm6kSystemProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 19),
    _Sm6kSystemProcessStartTime_Type()
)
sm6kSystemProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessStartTime.setStatus("mandatory")
_Sm6kSystemProcessCommand_Type = DisplayString
_Sm6kSystemProcessCommand_Object = MibTableColumn
sm6kSystemProcessCommand = _Sm6kSystemProcessCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 20),
    _Sm6kSystemProcessCommand_Type()
)
sm6kSystemProcessCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessCommand.setStatus("mandatory")
_Sm6kSystemProcessLoginUID_Type = Integer32
_Sm6kSystemProcessLoginUID_Object = MibTableColumn
sm6kSystemProcessLoginUID = _Sm6kSystemProcessLoginUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 21),
    _Sm6kSystemProcessLoginUID_Type()
)
sm6kSystemProcessLoginUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessLoginUID.setStatus("mandatory")
_Sm6kSystemProcessEffectiveUID_Type = Integer32
_Sm6kSystemProcessEffectiveUID_Object = MibTableColumn
sm6kSystemProcessEffectiveUID = _Sm6kSystemProcessEffectiveUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 22),
    _Sm6kSystemProcessEffectiveUID_Type()
)
sm6kSystemProcessEffectiveUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessEffectiveUID.setStatus("mandatory")
_Sm6kSystemProcessEffectiveGID_Type = Integer32
_Sm6kSystemProcessEffectiveGID_Object = MibTableColumn
sm6kSystemProcessEffectiveGID = _Sm6kSystemProcessEffectiveGID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 23),
    _Sm6kSystemProcessEffectiveGID_Type()
)
sm6kSystemProcessEffectiveGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessEffectiveGID.setStatus("mandatory")
_Sm6kSystemProcessEffectiveGroupName_Type = DisplayString
_Sm6kSystemProcessEffectiveGroupName_Object = MibTableColumn
sm6kSystemProcessEffectiveGroupName = _Sm6kSystemProcessEffectiveGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 24),
    _Sm6kSystemProcessEffectiveGroupName_Type()
)
sm6kSystemProcessEffectiveGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessEffectiveGroupName.setStatus("mandatory")
_Sm6kSystemProcessSUID_Type = Integer32
_Sm6kSystemProcessSUID_Object = MibTableColumn
sm6kSystemProcessSUID = _Sm6kSystemProcessSUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 25),
    _Sm6kSystemProcessSUID_Type()
)
sm6kSystemProcessSUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessSUID.setStatus("mandatory")
_Sm6kSystemProcessPgrp_Type = Integer32
_Sm6kSystemProcessPgrp_Object = MibTableColumn
sm6kSystemProcessPgrp = _Sm6kSystemProcessPgrp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 26),
    _Sm6kSystemProcessPgrp_Type()
)
sm6kSystemProcessPgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPgrp.setStatus("mandatory")
_Sm6kSystemProcessPFlags_Type = Integer32
_Sm6kSystemProcessPFlags_Object = MibTableColumn
sm6kSystemProcessPFlags = _Sm6kSystemProcessPFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 27),
    _Sm6kSystemProcessPFlags_Type()
)
sm6kSystemProcessPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessPFlags.setStatus("mandatory")
_Sm6kSystemProcessAdspace_Type = Integer32
_Sm6kSystemProcessAdspace_Object = MibTableColumn
sm6kSystemProcessAdspace = _Sm6kSystemProcessAdspace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 28),
    _Sm6kSystemProcessAdspace_Type()
)
sm6kSystemProcessAdspace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessAdspace.setStatus("mandatory")
_Sm6kSystemProcessTTYp_Type = Integer32
_Sm6kSystemProcessTTYp_Object = MibTableColumn
sm6kSystemProcessTTYp = _Sm6kSystemProcessTTYp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 29),
    _Sm6kSystemProcessTTYp_Type()
)
sm6kSystemProcessTTYp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessTTYp.setStatus("mandatory")
_Sm6kSystemProcessTTYd_Type = Integer32
_Sm6kSystemProcessTTYd_Object = MibTableColumn
sm6kSystemProcessTTYd = _Sm6kSystemProcessTTYd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 30),
    _Sm6kSystemProcessTTYd_Type()
)
sm6kSystemProcessTTYd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessTTYd.setStatus("mandatory")
_Sm6kSystemProcessNSwap_Type = Counter32
_Sm6kSystemProcessNSwap_Object = MibTableColumn
sm6kSystemProcessNSwap = _Sm6kSystemProcessNSwap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 31),
    _Sm6kSystemProcessNSwap_Type()
)
sm6kSystemProcessNSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessNSwap.setStatus("mandatory")
_Sm6kSystemProcessInblocks_Type = Counter32
_Sm6kSystemProcessInblocks_Object = MibTableColumn
sm6kSystemProcessInblocks = _Sm6kSystemProcessInblocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 32),
    _Sm6kSystemProcessInblocks_Type()
)
sm6kSystemProcessInblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessInblocks.setStatus("mandatory")
_Sm6kSystemProcessOutblocks_Type = Counter32
_Sm6kSystemProcessOutblocks_Object = MibTableColumn
sm6kSystemProcessOutblocks = _Sm6kSystemProcessOutblocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 33),
    _Sm6kSystemProcessOutblocks_Type()
)
sm6kSystemProcessOutblocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessOutblocks.setStatus("mandatory")
_Sm6kSystemProcessMsgsnd_Type = Counter32
_Sm6kSystemProcessMsgsnd_Object = MibTableColumn
sm6kSystemProcessMsgsnd = _Sm6kSystemProcessMsgsnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 34),
    _Sm6kSystemProcessMsgsnd_Type()
)
sm6kSystemProcessMsgsnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessMsgsnd.setStatus("mandatory")
_Sm6kSystemProcessMsgrcv_Type = Counter32
_Sm6kSystemProcessMsgrcv_Object = MibTableColumn
sm6kSystemProcessMsgrcv = _Sm6kSystemProcessMsgrcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 35),
    _Sm6kSystemProcessMsgrcv_Type()
)
sm6kSystemProcessMsgrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessMsgrcv.setStatus("mandatory")
_Sm6kSystemProcessNsignals_Type = Counter32
_Sm6kSystemProcessNsignals_Object = MibTableColumn
sm6kSystemProcessNsignals = _Sm6kSystemProcessNsignals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 36),
    _Sm6kSystemProcessNsignals_Type()
)
sm6kSystemProcessNsignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessNsignals.setStatus("mandatory")
_Sm6kSystemProcessNVcsw_Type = Counter32
_Sm6kSystemProcessNVcsw_Object = MibTableColumn
sm6kSystemProcessNVcsw = _Sm6kSystemProcessNVcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 37),
    _Sm6kSystemProcessNVcsw_Type()
)
sm6kSystemProcessNVcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessNVcsw.setStatus("mandatory")
_Sm6kSystemProcessNIvcsw_Type = Counter32
_Sm6kSystemProcessNIvcsw_Object = MibTableColumn
sm6kSystemProcessNIvcsw = _Sm6kSystemProcessNIvcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 38),
    _Sm6kSystemProcessNIvcsw_Type()
)
sm6kSystemProcessNIvcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessNIvcsw.setStatus("mandatory")
_Sm6kSystemProcessArguments_Type = DisplayString
_Sm6kSystemProcessArguments_Object = MibTableColumn
sm6kSystemProcessArguments = _Sm6kSystemProcessArguments_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 39),
    _Sm6kSystemProcessArguments_Type()
)
sm6kSystemProcessArguments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessArguments.setStatus("mandatory")


class _Sm6kSystemProcessSignal_Type(Integer32):
    """Custom type sm6kSystemProcessSignal based on Integer32"""
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


_Sm6kSystemProcessSignal_Type.__name__ = "Integer32"
_Sm6kSystemProcessSignal_Object = MibTableColumn
sm6kSystemProcessSignal = _Sm6kSystemProcessSignal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 7, 2, 1, 40),
    _Sm6kSystemProcessSignal_Type()
)
sm6kSystemProcessSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemProcessSignal.setStatus("mandatory")
_Sm6kSystemUsers_ObjectIdentity = ObjectIdentity
sm6kSystemUsers = _Sm6kSystemUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8)
)
_Sm6kSystemUsersLoggedIn_Type = Gauge32
_Sm6kSystemUsersLoggedIn_Object = MibScalar
sm6kSystemUsersLoggedIn = _Sm6kSystemUsersLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 1),
    _Sm6kSystemUsersLoggedIn_Type()
)
sm6kSystemUsersLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUsersLoggedIn.setStatus("mandatory")
_Sm6kSystemUsersTable_Object = MibTable
sm6kSystemUsersTable = _Sm6kSystemUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemUsersTable.setStatus("mandatory")
_Sm6kSystemUsersEntry_Object = MibTableRow
sm6kSystemUsersEntry = _Sm6kSystemUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1)
)
sm6kSystemUsersEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemUsersName"),
)
if mibBuilder.loadTexts:
    sm6kSystemUsersEntry.setStatus("mandatory")
_Sm6kSystemUsersName_Type = DisplayString
_Sm6kSystemUsersName_Object = MibTableColumn
sm6kSystemUsersName = _Sm6kSystemUsersName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 1),
    _Sm6kSystemUsersName_Type()
)
sm6kSystemUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUsersName.setStatus("mandatory")
_Sm6kSystemUsersLine_Type = DisplayString
_Sm6kSystemUsersLine_Object = MibTableColumn
sm6kSystemUsersLine = _Sm6kSystemUsersLine_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 2),
    _Sm6kSystemUsersLine_Type()
)
sm6kSystemUsersLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUsersLine.setStatus("mandatory")
_Sm6kSystemUsersTime_Type = DisplayString
_Sm6kSystemUsersTime_Object = MibTableColumn
sm6kSystemUsersTime = _Sm6kSystemUsersTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 3),
    _Sm6kSystemUsersTime_Type()
)
sm6kSystemUsersTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUsersTime.setStatus("mandatory")
_Sm6kSystemUsersPID_Type = Integer32
_Sm6kSystemUsersPID_Object = MibTableColumn
sm6kSystemUsersPID = _Sm6kSystemUsersPID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 4),
    _Sm6kSystemUsersPID_Type()
)
sm6kSystemUsersPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUsersPID.setStatus("mandatory")
_Sm6kSystemUsersRemoteHost_Type = DisplayString
_Sm6kSystemUsersRemoteHost_Object = MibTableColumn
sm6kSystemUsersRemoteHost = _Sm6kSystemUsersRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 8, 2, 1, 5),
    _Sm6kSystemUsersRemoteHost_Type()
)
sm6kSystemUsersRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUsersRemoteHost.setStatus("mandatory")
_Sm6kSystemUtilization_ObjectIdentity = ObjectIdentity
sm6kSystemUtilization = _Sm6kSystemUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9)
)
_Sm6kSystemUtilizationCPU_ObjectIdentity = ObjectIdentity
sm6kSystemUtilizationCPU = _Sm6kSystemUtilizationCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1)
)
_Sm6kSystemUtilizationCPUPollingInterval_Type = Integer32
_Sm6kSystemUtilizationCPUPollingInterval_Object = MibScalar
sm6kSystemUtilizationCPUPollingInterval = _Sm6kSystemUtilizationCPUPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 1),
    _Sm6kSystemUtilizationCPUPollingInterval_Type()
)
sm6kSystemUtilizationCPUPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUPollingInterval.setStatus("mandatory")
_Sm6kSystemUtilizationCPUCount_Type = Integer32
_Sm6kSystemUtilizationCPUCount_Object = MibScalar
sm6kSystemUtilizationCPUCount = _Sm6kSystemUtilizationCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 2),
    _Sm6kSystemUtilizationCPUCount_Type()
)
sm6kSystemUtilizationCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUCount.setStatus("mandatory")
_Sm6kSystemUtilizationCPUTable_Object = MibTable
sm6kSystemUtilizationCPUTable = _Sm6kSystemUtilizationCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUTable.setStatus("mandatory")
_Sm6kSystemUtilizationCPUEntry_Object = MibTableRow
sm6kSystemUtilizationCPUEntry = _Sm6kSystemUtilizationCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1)
)
sm6kSystemUtilizationCPUEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemUtilizationCPUIntervalName"),
)
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUEntry.setStatus("mandatory")
_Sm6kSystemUtilizationCPUIntervalName_Type = DisplayString
_Sm6kSystemUtilizationCPUIntervalName_Object = MibTableColumn
sm6kSystemUtilizationCPUIntervalName = _Sm6kSystemUtilizationCPUIntervalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 1),
    _Sm6kSystemUtilizationCPUIntervalName_Type()
)
sm6kSystemUtilizationCPUIntervalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUIntervalName.setStatus("mandatory")
_Sm6kSystemUtilizationCPUIntervalStartTime_Type = DisplayString
_Sm6kSystemUtilizationCPUIntervalStartTime_Object = MibTableColumn
sm6kSystemUtilizationCPUIntervalStartTime = _Sm6kSystemUtilizationCPUIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 2),
    _Sm6kSystemUtilizationCPUIntervalStartTime_Type()
)
sm6kSystemUtilizationCPUIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUIntervalStartTime.setStatus("mandatory")
_Sm6kSystemUtilizationCPUIntervalLength_Type = TimeTicks
_Sm6kSystemUtilizationCPUIntervalLength_Object = MibTableColumn
sm6kSystemUtilizationCPUIntervalLength = _Sm6kSystemUtilizationCPUIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 3),
    _Sm6kSystemUtilizationCPUIntervalLength_Type()
)
sm6kSystemUtilizationCPUIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUIntervalLength.setStatus("mandatory")
_Sm6kSystemUtilizationCPUUser_Type = Integer32
_Sm6kSystemUtilizationCPUUser_Object = MibTableColumn
sm6kSystemUtilizationCPUUser = _Sm6kSystemUtilizationCPUUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 4),
    _Sm6kSystemUtilizationCPUUser_Type()
)
sm6kSystemUtilizationCPUUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUUser.setStatus("mandatory")
_Sm6kSystemUtilizationCPUSystem_Type = Integer32
_Sm6kSystemUtilizationCPUSystem_Object = MibTableColumn
sm6kSystemUtilizationCPUSystem = _Sm6kSystemUtilizationCPUSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 5),
    _Sm6kSystemUtilizationCPUSystem_Type()
)
sm6kSystemUtilizationCPUSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUSystem.setStatus("mandatory")
_Sm6kSystemUtilizationCPUIdle_Type = Integer32
_Sm6kSystemUtilizationCPUIdle_Object = MibTableColumn
sm6kSystemUtilizationCPUIdle = _Sm6kSystemUtilizationCPUIdle_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 6),
    _Sm6kSystemUtilizationCPUIdle_Type()
)
sm6kSystemUtilizationCPUIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUIdle.setStatus("mandatory")
_Sm6kSystemUtilizationCPUWait_Type = Integer32
_Sm6kSystemUtilizationCPUWait_Object = MibTableColumn
sm6kSystemUtilizationCPUWait = _Sm6kSystemUtilizationCPUWait_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 7),
    _Sm6kSystemUtilizationCPUWait_Type()
)
sm6kSystemUtilizationCPUWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUWait.setStatus("mandatory")
_Sm6kSystemUtilizationCPUBusy_Type = Integer32
_Sm6kSystemUtilizationCPUBusy_Object = MibTableColumn
sm6kSystemUtilizationCPUBusy = _Sm6kSystemUtilizationCPUBusy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 8),
    _Sm6kSystemUtilizationCPUBusy_Type()
)
sm6kSystemUtilizationCPUBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUBusy.setStatus("mandatory")
_Sm6kSystemUtilizationCPUUserMinimum_Type = Integer32
_Sm6kSystemUtilizationCPUUserMinimum_Object = MibTableColumn
sm6kSystemUtilizationCPUUserMinimum = _Sm6kSystemUtilizationCPUUserMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 9),
    _Sm6kSystemUtilizationCPUUserMinimum_Type()
)
sm6kSystemUtilizationCPUUserMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUUserMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUSystemMinimum_Type = Integer32
_Sm6kSystemUtilizationCPUSystemMinimum_Object = MibTableColumn
sm6kSystemUtilizationCPUSystemMinimum = _Sm6kSystemUtilizationCPUSystemMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 10),
    _Sm6kSystemUtilizationCPUSystemMinimum_Type()
)
sm6kSystemUtilizationCPUSystemMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUSystemMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUIdleMinimum_Type = Integer32
_Sm6kSystemUtilizationCPUIdleMinimum_Object = MibTableColumn
sm6kSystemUtilizationCPUIdleMinimum = _Sm6kSystemUtilizationCPUIdleMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 11),
    _Sm6kSystemUtilizationCPUIdleMinimum_Type()
)
sm6kSystemUtilizationCPUIdleMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUIdleMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUWaitMinimum_Type = Integer32
_Sm6kSystemUtilizationCPUWaitMinimum_Object = MibTableColumn
sm6kSystemUtilizationCPUWaitMinimum = _Sm6kSystemUtilizationCPUWaitMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 12),
    _Sm6kSystemUtilizationCPUWaitMinimum_Type()
)
sm6kSystemUtilizationCPUWaitMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUWaitMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUBusyMinimum_Type = Integer32
_Sm6kSystemUtilizationCPUBusyMinimum_Object = MibTableColumn
sm6kSystemUtilizationCPUBusyMinimum = _Sm6kSystemUtilizationCPUBusyMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 13),
    _Sm6kSystemUtilizationCPUBusyMinimum_Type()
)
sm6kSystemUtilizationCPUBusyMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUBusyMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUUserMaximum_Type = Integer32
_Sm6kSystemUtilizationCPUUserMaximum_Object = MibTableColumn
sm6kSystemUtilizationCPUUserMaximum = _Sm6kSystemUtilizationCPUUserMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 14),
    _Sm6kSystemUtilizationCPUUserMaximum_Type()
)
sm6kSystemUtilizationCPUUserMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUUserMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUSystemMaximum_Type = Integer32
_Sm6kSystemUtilizationCPUSystemMaximum_Object = MibTableColumn
sm6kSystemUtilizationCPUSystemMaximum = _Sm6kSystemUtilizationCPUSystemMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 15),
    _Sm6kSystemUtilizationCPUSystemMaximum_Type()
)
sm6kSystemUtilizationCPUSystemMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUSystemMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUIdleMaximum_Type = Integer32
_Sm6kSystemUtilizationCPUIdleMaximum_Object = MibTableColumn
sm6kSystemUtilizationCPUIdleMaximum = _Sm6kSystemUtilizationCPUIdleMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 16),
    _Sm6kSystemUtilizationCPUIdleMaximum_Type()
)
sm6kSystemUtilizationCPUIdleMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUIdleMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUWaitMaximum_Type = Integer32
_Sm6kSystemUtilizationCPUWaitMaximum_Object = MibTableColumn
sm6kSystemUtilizationCPUWaitMaximum = _Sm6kSystemUtilizationCPUWaitMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 17),
    _Sm6kSystemUtilizationCPUWaitMaximum_Type()
)
sm6kSystemUtilizationCPUWaitMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUWaitMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUBusyMaximum_Type = Integer32
_Sm6kSystemUtilizationCPUBusyMaximum_Object = MibTableColumn
sm6kSystemUtilizationCPUBusyMaximum = _Sm6kSystemUtilizationCPUBusyMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 18),
    _Sm6kSystemUtilizationCPUBusyMaximum_Type()
)
sm6kSystemUtilizationCPUBusyMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUBusyMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationCPUNumber_Type = Integer32
_Sm6kSystemUtilizationCPUNumber_Object = MibTableColumn
sm6kSystemUtilizationCPUNumber = _Sm6kSystemUtilizationCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 1, 3, 1, 19),
    _Sm6kSystemUtilizationCPUNumber_Type()
)
sm6kSystemUtilizationCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationCPUNumber.setStatus("mandatory")
_Sm6kSystemUtilizationKernel_ObjectIdentity = ObjectIdentity
sm6kSystemUtilizationKernel = _Sm6kSystemUtilizationKernel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2)
)
_Sm6kSystemUtilizationKernelPollingInterval_Type = Integer32
_Sm6kSystemUtilizationKernelPollingInterval_Object = MibScalar
sm6kSystemUtilizationKernelPollingInterval = _Sm6kSystemUtilizationKernelPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 1),
    _Sm6kSystemUtilizationKernelPollingInterval_Type()
)
sm6kSystemUtilizationKernelPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelPollingInterval.setStatus("mandatory")
_Sm6kSystemUtilizationKernelTable_Object = MibTable
sm6kSystemUtilizationKernelTable = _Sm6kSystemUtilizationKernelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelTable.setStatus("mandatory")
_Sm6kSystemUtilizationKernelEntry_Object = MibTableRow
sm6kSystemUtilizationKernelEntry = _Sm6kSystemUtilizationKernelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1)
)
sm6kSystemUtilizationKernelEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemUtilizationKernelName"),
)
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelEntry.setStatus("mandatory")
_Sm6kSystemUtilizationKernelName_Type = DisplayString
_Sm6kSystemUtilizationKernelName_Object = MibTableColumn
sm6kSystemUtilizationKernelName = _Sm6kSystemUtilizationKernelName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 1),
    _Sm6kSystemUtilizationKernelName_Type()
)
sm6kSystemUtilizationKernelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelName.setStatus("mandatory")
_Sm6kSystemUtilizationKernelIntervalStartTime_Type = DisplayString
_Sm6kSystemUtilizationKernelIntervalStartTime_Object = MibTableColumn
sm6kSystemUtilizationKernelIntervalStartTime = _Sm6kSystemUtilizationKernelIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 2),
    _Sm6kSystemUtilizationKernelIntervalStartTime_Type()
)
sm6kSystemUtilizationKernelIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelIntervalStartTime.setStatus("mandatory")
_Sm6kSystemUtilizationKernelIntervalLength_Type = TimeTicks
_Sm6kSystemUtilizationKernelIntervalLength_Object = MibTableColumn
sm6kSystemUtilizationKernelIntervalLength = _Sm6kSystemUtilizationKernelIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 3),
    _Sm6kSystemUtilizationKernelIntervalLength_Type()
)
sm6kSystemUtilizationKernelIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelIntervalLength.setStatus("mandatory")
_Sm6kSystemUtilizationKernelContextSwitches_Type = Integer32
_Sm6kSystemUtilizationKernelContextSwitches_Object = MibTableColumn
sm6kSystemUtilizationKernelContextSwitches = _Sm6kSystemUtilizationKernelContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 4),
    _Sm6kSystemUtilizationKernelContextSwitches_Type()
)
sm6kSystemUtilizationKernelContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelContextSwitches.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemCalls_Type = Integer32
_Sm6kSystemUtilizationKernelSystemCalls_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemCalls = _Sm6kSystemUtilizationKernelSystemCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 5),
    _Sm6kSystemUtilizationKernelSystemCalls_Type()
)
sm6kSystemUtilizationKernelSystemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemCalls.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemReads_Type = Integer32
_Sm6kSystemUtilizationKernelSystemReads_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemReads = _Sm6kSystemUtilizationKernelSystemReads_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 6),
    _Sm6kSystemUtilizationKernelSystemReads_Type()
)
sm6kSystemUtilizationKernelSystemReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemReads.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemWrites_Type = Integer32
_Sm6kSystemUtilizationKernelSystemWrites_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemWrites = _Sm6kSystemUtilizationKernelSystemWrites_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 7),
    _Sm6kSystemUtilizationKernelSystemWrites_Type()
)
sm6kSystemUtilizationKernelSystemWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemWrites.setStatus("mandatory")
_Sm6kSystemUtilizationKernelForks_Type = Integer32
_Sm6kSystemUtilizationKernelForks_Object = MibTableColumn
sm6kSystemUtilizationKernelForks = _Sm6kSystemUtilizationKernelForks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 8),
    _Sm6kSystemUtilizationKernelForks_Type()
)
sm6kSystemUtilizationKernelForks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelForks.setStatus("mandatory")
_Sm6kSystemUtilizationKernelExecs_Type = Integer32
_Sm6kSystemUtilizationKernelExecs_Object = MibTableColumn
sm6kSystemUtilizationKernelExecs = _Sm6kSystemUtilizationKernelExecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 9),
    _Sm6kSystemUtilizationKernelExecs_Type()
)
sm6kSystemUtilizationKernelExecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelExecs.setStatus("mandatory")
_Sm6kSystemUtilizationKernelRunQueue_Type = Integer32
_Sm6kSystemUtilizationKernelRunQueue_Object = MibTableColumn
sm6kSystemUtilizationKernelRunQueue = _Sm6kSystemUtilizationKernelRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 10),
    _Sm6kSystemUtilizationKernelRunQueue_Type()
)
sm6kSystemUtilizationKernelRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelRunQueue.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSwapQueue_Type = Integer32
_Sm6kSystemUtilizationKernelSwapQueue_Object = MibTableColumn
sm6kSystemUtilizationKernelSwapQueue = _Sm6kSystemUtilizationKernelSwapQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 11),
    _Sm6kSystemUtilizationKernelSwapQueue_Type()
)
sm6kSystemUtilizationKernelSwapQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSwapQueue.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSemaphores_Type = Integer32
_Sm6kSystemUtilizationKernelSemaphores_Object = MibTableColumn
sm6kSystemUtilizationKernelSemaphores = _Sm6kSystemUtilizationKernelSemaphores_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 12),
    _Sm6kSystemUtilizationKernelSemaphores_Type()
)
sm6kSystemUtilizationKernelSemaphores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSemaphores.setStatus("mandatory")
_Sm6kSystemUtilizationKernelMessages_Type = Integer32
_Sm6kSystemUtilizationKernelMessages_Object = MibTableColumn
sm6kSystemUtilizationKernelMessages = _Sm6kSystemUtilizationKernelMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 13),
    _Sm6kSystemUtilizationKernelMessages_Type()
)
sm6kSystemUtilizationKernelMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelMessages.setStatus("mandatory")
_Sm6kSystemUtilizationKernelProcessOverflow_Type = Integer32
_Sm6kSystemUtilizationKernelProcessOverflow_Object = MibTableColumn
sm6kSystemUtilizationKernelProcessOverflow = _Sm6kSystemUtilizationKernelProcessOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 14),
    _Sm6kSystemUtilizationKernelProcessOverflow_Type()
)
sm6kSystemUtilizationKernelProcessOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelProcessOverflow.setStatus("mandatory")
_Sm6kSystemUtilizationKernelBytesRead_Type = Integer32
_Sm6kSystemUtilizationKernelBytesRead_Object = MibTableColumn
sm6kSystemUtilizationKernelBytesRead = _Sm6kSystemUtilizationKernelBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 15),
    _Sm6kSystemUtilizationKernelBytesRead_Type()
)
sm6kSystemUtilizationKernelBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelBytesRead.setStatus("mandatory")
_Sm6kSystemUtilizationKernelBytesWritten_Type = Integer32
_Sm6kSystemUtilizationKernelBytesWritten_Object = MibTableColumn
sm6kSystemUtilizationKernelBytesWritten = _Sm6kSystemUtilizationKernelBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 16),
    _Sm6kSystemUtilizationKernelBytesWritten_Type()
)
sm6kSystemUtilizationKernelBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelBytesWritten.setStatus("mandatory")
_Sm6kSystemUtilizationKernelRawTTYOut_Type = Integer32
_Sm6kSystemUtilizationKernelRawTTYOut_Object = MibTableColumn
sm6kSystemUtilizationKernelRawTTYOut = _Sm6kSystemUtilizationKernelRawTTYOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 17),
    _Sm6kSystemUtilizationKernelRawTTYOut_Type()
)
sm6kSystemUtilizationKernelRawTTYOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelRawTTYOut.setStatus("mandatory")
_Sm6kSystemUtilizationKernelContextSwitchesMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelContextSwitchesMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelContextSwitchesMinimum = _Sm6kSystemUtilizationKernelContextSwitchesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 18),
    _Sm6kSystemUtilizationKernelContextSwitchesMinimum_Type()
)
sm6kSystemUtilizationKernelContextSwitchesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelContextSwitchesMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemCallsMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelSystemCallsMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemCallsMinimum = _Sm6kSystemUtilizationKernelSystemCallsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 19),
    _Sm6kSystemUtilizationKernelSystemCallsMinimum_Type()
)
sm6kSystemUtilizationKernelSystemCallsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemCallsMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemReadsMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelSystemReadsMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemReadsMinimum = _Sm6kSystemUtilizationKernelSystemReadsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 20),
    _Sm6kSystemUtilizationKernelSystemReadsMinimum_Type()
)
sm6kSystemUtilizationKernelSystemReadsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemReadsMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemWritesMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelSystemWritesMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemWritesMinimum = _Sm6kSystemUtilizationKernelSystemWritesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 21),
    _Sm6kSystemUtilizationKernelSystemWritesMinimum_Type()
)
sm6kSystemUtilizationKernelSystemWritesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemWritesMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelForksMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelForksMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelForksMinimum = _Sm6kSystemUtilizationKernelForksMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 22),
    _Sm6kSystemUtilizationKernelForksMinimum_Type()
)
sm6kSystemUtilizationKernelForksMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelForksMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelExecsMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelExecsMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelExecsMinimum = _Sm6kSystemUtilizationKernelExecsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 23),
    _Sm6kSystemUtilizationKernelExecsMinimum_Type()
)
sm6kSystemUtilizationKernelExecsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelExecsMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelRunQueueMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelRunQueueMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelRunQueueMinimum = _Sm6kSystemUtilizationKernelRunQueueMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 24),
    _Sm6kSystemUtilizationKernelRunQueueMinimum_Type()
)
sm6kSystemUtilizationKernelRunQueueMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelRunQueueMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSwapQueueMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelSwapQueueMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelSwapQueueMinimum = _Sm6kSystemUtilizationKernelSwapQueueMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 25),
    _Sm6kSystemUtilizationKernelSwapQueueMinimum_Type()
)
sm6kSystemUtilizationKernelSwapQueueMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSwapQueueMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSemaphoresMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelSemaphoresMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelSemaphoresMinimum = _Sm6kSystemUtilizationKernelSemaphoresMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 26),
    _Sm6kSystemUtilizationKernelSemaphoresMinimum_Type()
)
sm6kSystemUtilizationKernelSemaphoresMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSemaphoresMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelMessagesMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelMessagesMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelMessagesMinimum = _Sm6kSystemUtilizationKernelMessagesMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 27),
    _Sm6kSystemUtilizationKernelMessagesMinimum_Type()
)
sm6kSystemUtilizationKernelMessagesMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelMessagesMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelProcessOverflowMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelProcessOverflowMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelProcessOverflowMinimum = _Sm6kSystemUtilizationKernelProcessOverflowMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 28),
    _Sm6kSystemUtilizationKernelProcessOverflowMinimum_Type()
)
sm6kSystemUtilizationKernelProcessOverflowMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelProcessOverflowMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelBytesReadMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelBytesReadMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelBytesReadMinimum = _Sm6kSystemUtilizationKernelBytesReadMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 29),
    _Sm6kSystemUtilizationKernelBytesReadMinimum_Type()
)
sm6kSystemUtilizationKernelBytesReadMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelBytesReadMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelBytesWrittenMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelBytesWrittenMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelBytesWrittenMinimum = _Sm6kSystemUtilizationKernelBytesWrittenMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 30),
    _Sm6kSystemUtilizationKernelBytesWrittenMinimum_Type()
)
sm6kSystemUtilizationKernelBytesWrittenMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelBytesWrittenMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelRawTTYOutMinimum_Type = Integer32
_Sm6kSystemUtilizationKernelRawTTYOutMinimum_Object = MibTableColumn
sm6kSystemUtilizationKernelRawTTYOutMinimum = _Sm6kSystemUtilizationKernelRawTTYOutMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 31),
    _Sm6kSystemUtilizationKernelRawTTYOutMinimum_Type()
)
sm6kSystemUtilizationKernelRawTTYOutMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelRawTTYOutMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelContextSwitchesMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelContextSwitchesMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelContextSwitchesMaximum = _Sm6kSystemUtilizationKernelContextSwitchesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 32),
    _Sm6kSystemUtilizationKernelContextSwitchesMaximum_Type()
)
sm6kSystemUtilizationKernelContextSwitchesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelContextSwitchesMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemCallsMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelSystemCallsMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemCallsMaximum = _Sm6kSystemUtilizationKernelSystemCallsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 33),
    _Sm6kSystemUtilizationKernelSystemCallsMaximum_Type()
)
sm6kSystemUtilizationKernelSystemCallsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemCallsMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemReadsMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelSystemReadsMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemReadsMaximum = _Sm6kSystemUtilizationKernelSystemReadsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 34),
    _Sm6kSystemUtilizationKernelSystemReadsMaximum_Type()
)
sm6kSystemUtilizationKernelSystemReadsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemReadsMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSystemWritesMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelSystemWritesMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelSystemWritesMaximum = _Sm6kSystemUtilizationKernelSystemWritesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 35),
    _Sm6kSystemUtilizationKernelSystemWritesMaximum_Type()
)
sm6kSystemUtilizationKernelSystemWritesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSystemWritesMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelForksMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelForksMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelForksMaximum = _Sm6kSystemUtilizationKernelForksMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 36),
    _Sm6kSystemUtilizationKernelForksMaximum_Type()
)
sm6kSystemUtilizationKernelForksMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelForksMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelExecsMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelExecsMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelExecsMaximum = _Sm6kSystemUtilizationKernelExecsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 37),
    _Sm6kSystemUtilizationKernelExecsMaximum_Type()
)
sm6kSystemUtilizationKernelExecsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelExecsMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelRunQueueMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelRunQueueMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelRunQueueMaximum = _Sm6kSystemUtilizationKernelRunQueueMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 38),
    _Sm6kSystemUtilizationKernelRunQueueMaximum_Type()
)
sm6kSystemUtilizationKernelRunQueueMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelRunQueueMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSwapQueueMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelSwapQueueMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelSwapQueueMaximum = _Sm6kSystemUtilizationKernelSwapQueueMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 39),
    _Sm6kSystemUtilizationKernelSwapQueueMaximum_Type()
)
sm6kSystemUtilizationKernelSwapQueueMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSwapQueueMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelSemaphoresMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelSemaphoresMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelSemaphoresMaximum = _Sm6kSystemUtilizationKernelSemaphoresMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 40),
    _Sm6kSystemUtilizationKernelSemaphoresMaximum_Type()
)
sm6kSystemUtilizationKernelSemaphoresMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelSemaphoresMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelMessagesMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelMessagesMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelMessagesMaximum = _Sm6kSystemUtilizationKernelMessagesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 41),
    _Sm6kSystemUtilizationKernelMessagesMaximum_Type()
)
sm6kSystemUtilizationKernelMessagesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelMessagesMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelProcessOverflowMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelProcessOverflowMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelProcessOverflowMaximum = _Sm6kSystemUtilizationKernelProcessOverflowMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 42),
    _Sm6kSystemUtilizationKernelProcessOverflowMaximum_Type()
)
sm6kSystemUtilizationKernelProcessOverflowMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelProcessOverflowMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelBytesReadMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelBytesReadMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelBytesReadMaximum = _Sm6kSystemUtilizationKernelBytesReadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 43),
    _Sm6kSystemUtilizationKernelBytesReadMaximum_Type()
)
sm6kSystemUtilizationKernelBytesReadMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelBytesReadMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelBytesWrittenMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelBytesWrittenMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelBytesWrittenMaximum = _Sm6kSystemUtilizationKernelBytesWrittenMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 44),
    _Sm6kSystemUtilizationKernelBytesWrittenMaximum_Type()
)
sm6kSystemUtilizationKernelBytesWrittenMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelBytesWrittenMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationKernelRawTTYOutMaximum_Type = Integer32
_Sm6kSystemUtilizationKernelRawTTYOutMaximum_Object = MibTableColumn
sm6kSystemUtilizationKernelRawTTYOutMaximum = _Sm6kSystemUtilizationKernelRawTTYOutMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 2, 2, 1, 45),
    _Sm6kSystemUtilizationKernelRawTTYOutMaximum_Type()
)
sm6kSystemUtilizationKernelRawTTYOutMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationKernelRawTTYOutMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationIostat_ObjectIdentity = ObjectIdentity
sm6kSystemUtilizationIostat = _Sm6kSystemUtilizationIostat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3)
)
_Sm6kSystemUtilizationIostatPollingInterval_Type = Integer32
_Sm6kSystemUtilizationIostatPollingInterval_Object = MibScalar
sm6kSystemUtilizationIostatPollingInterval = _Sm6kSystemUtilizationIostatPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 1),
    _Sm6kSystemUtilizationIostatPollingInterval_Type()
)
sm6kSystemUtilizationIostatPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatPollingInterval.setStatus("mandatory")
_Sm6kSystemUtilizationIostatTable_Object = MibTable
sm6kSystemUtilizationIostatTable = _Sm6kSystemUtilizationIostatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatTable.setStatus("mandatory")
_Sm6kSystemUtilizationIostatEntry_Object = MibTableRow
sm6kSystemUtilizationIostatEntry = _Sm6kSystemUtilizationIostatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1)
)
sm6kSystemUtilizationIostatEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kSystemUtilizationIostatName"),
)
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatEntry.setStatus("mandatory")
_Sm6kSystemUtilizationIostatName_Type = DisplayString
_Sm6kSystemUtilizationIostatName_Object = MibTableColumn
sm6kSystemUtilizationIostatName = _Sm6kSystemUtilizationIostatName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 1),
    _Sm6kSystemUtilizationIostatName_Type()
)
sm6kSystemUtilizationIostatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatName.setStatus("mandatory")
_Sm6kSystemUtilizationIostatIntervalStartTime_Type = DisplayString
_Sm6kSystemUtilizationIostatIntervalStartTime_Object = MibTableColumn
sm6kSystemUtilizationIostatIntervalStartTime = _Sm6kSystemUtilizationIostatIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 2),
    _Sm6kSystemUtilizationIostatIntervalStartTime_Type()
)
sm6kSystemUtilizationIostatIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatIntervalStartTime.setStatus("mandatory")
_Sm6kSystemUtilizationIostatIntervalLength_Type = TimeTicks
_Sm6kSystemUtilizationIostatIntervalLength_Object = MibTableColumn
sm6kSystemUtilizationIostatIntervalLength = _Sm6kSystemUtilizationIostatIntervalLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 3),
    _Sm6kSystemUtilizationIostatIntervalLength_Type()
)
sm6kSystemUtilizationIostatIntervalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatIntervalLength.setStatus("mandatory")
_Sm6kSystemUtilizationIostatPercentTimeActive_Type = Integer32
_Sm6kSystemUtilizationIostatPercentTimeActive_Object = MibTableColumn
sm6kSystemUtilizationIostatPercentTimeActive = _Sm6kSystemUtilizationIostatPercentTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 4),
    _Sm6kSystemUtilizationIostatPercentTimeActive_Type()
)
sm6kSystemUtilizationIostatPercentTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatPercentTimeActive.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesTransferRate_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesTransferRate_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesTransferRate = _Sm6kSystemUtilizationIostatKilobytesTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 5),
    _Sm6kSystemUtilizationIostatKilobytesTransferRate_Type()
)
sm6kSystemUtilizationIostatKilobytesTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesTransferRate.setStatus("mandatory")
_Sm6kSystemUtilizationIostatTransfers_Type = Integer32
_Sm6kSystemUtilizationIostatTransfers_Object = MibTableColumn
sm6kSystemUtilizationIostatTransfers = _Sm6kSystemUtilizationIostatTransfers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 6),
    _Sm6kSystemUtilizationIostatTransfers_Type()
)
sm6kSystemUtilizationIostatTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatTransfers.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesRead_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesRead_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesRead = _Sm6kSystemUtilizationIostatKilobytesRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 7),
    _Sm6kSystemUtilizationIostatKilobytesRead_Type()
)
sm6kSystemUtilizationIostatKilobytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesRead.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesWritten_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesWritten_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesWritten = _Sm6kSystemUtilizationIostatKilobytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 8),
    _Sm6kSystemUtilizationIostatKilobytesWritten_Type()
)
sm6kSystemUtilizationIostatKilobytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesWritten.setStatus("mandatory")
_Sm6kSystemUtilizationIostatPercentTimeActiveMinimum_Type = Integer32
_Sm6kSystemUtilizationIostatPercentTimeActiveMinimum_Object = MibTableColumn
sm6kSystemUtilizationIostatPercentTimeActiveMinimum = _Sm6kSystemUtilizationIostatPercentTimeActiveMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 9),
    _Sm6kSystemUtilizationIostatPercentTimeActiveMinimum_Type()
)
sm6kSystemUtilizationIostatPercentTimeActiveMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatPercentTimeActiveMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesTransferRateMinimum_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesTransferRateMinimum_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesTransferRateMinimum = _Sm6kSystemUtilizationIostatKilobytesTransferRateMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 10),
    _Sm6kSystemUtilizationIostatKilobytesTransferRateMinimum_Type()
)
sm6kSystemUtilizationIostatKilobytesTransferRateMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesTransferRateMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatTransfersMinimum_Type = Integer32
_Sm6kSystemUtilizationIostatTransfersMinimum_Object = MibTableColumn
sm6kSystemUtilizationIostatTransfersMinimum = _Sm6kSystemUtilizationIostatTransfersMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 11),
    _Sm6kSystemUtilizationIostatTransfersMinimum_Type()
)
sm6kSystemUtilizationIostatTransfersMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatTransfersMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesReadMinimum_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesReadMinimum_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesReadMinimum = _Sm6kSystemUtilizationIostatKilobytesReadMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 12),
    _Sm6kSystemUtilizationIostatKilobytesReadMinimum_Type()
)
sm6kSystemUtilizationIostatKilobytesReadMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesReadMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesWrittenMinimum_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesWrittenMinimum_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesWrittenMinimum = _Sm6kSystemUtilizationIostatKilobytesWrittenMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 13),
    _Sm6kSystemUtilizationIostatKilobytesWrittenMinimum_Type()
)
sm6kSystemUtilizationIostatKilobytesWrittenMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesWrittenMinimum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatPercentTimeActiveMaximum_Type = Integer32
_Sm6kSystemUtilizationIostatPercentTimeActiveMaximum_Object = MibTableColumn
sm6kSystemUtilizationIostatPercentTimeActiveMaximum = _Sm6kSystemUtilizationIostatPercentTimeActiveMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 14),
    _Sm6kSystemUtilizationIostatPercentTimeActiveMaximum_Type()
)
sm6kSystemUtilizationIostatPercentTimeActiveMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatPercentTimeActiveMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesTransferRateMaximum_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesTransferRateMaximum_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesTransferRateMaximum = _Sm6kSystemUtilizationIostatKilobytesTransferRateMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 15),
    _Sm6kSystemUtilizationIostatKilobytesTransferRateMaximum_Type()
)
sm6kSystemUtilizationIostatKilobytesTransferRateMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesTransferRateMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatTransfersMaximum_Type = Integer32
_Sm6kSystemUtilizationIostatTransfersMaximum_Object = MibTableColumn
sm6kSystemUtilizationIostatTransfersMaximum = _Sm6kSystemUtilizationIostatTransfersMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 16),
    _Sm6kSystemUtilizationIostatTransfersMaximum_Type()
)
sm6kSystemUtilizationIostatTransfersMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatTransfersMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesReadMaximum_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesReadMaximum_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesReadMaximum = _Sm6kSystemUtilizationIostatKilobytesReadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 17),
    _Sm6kSystemUtilizationIostatKilobytesReadMaximum_Type()
)
sm6kSystemUtilizationIostatKilobytesReadMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesReadMaximum.setStatus("mandatory")
_Sm6kSystemUtilizationIostatKilobytesWrittenMaximum_Type = Integer32
_Sm6kSystemUtilizationIostatKilobytesWrittenMaximum_Object = MibTableColumn
sm6kSystemUtilizationIostatKilobytesWrittenMaximum = _Sm6kSystemUtilizationIostatKilobytesWrittenMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 9, 3, 2, 1, 18),
    _Sm6kSystemUtilizationIostatKilobytesWrittenMaximum_Type()
)
sm6kSystemUtilizationIostatKilobytesWrittenMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemUtilizationIostatKilobytesWrittenMaximum.setStatus("mandatory")
_Sm6kSystemReboot_ObjectIdentity = ObjectIdentity
sm6kSystemReboot = _Sm6kSystemReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 10)
)
_Sm6kSystemRebootTimer_Type = Integer32
_Sm6kSystemRebootTimer_Object = MibScalar
sm6kSystemRebootTimer = _Sm6kSystemRebootTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 10, 1),
    _Sm6kSystemRebootTimer_Type()
)
sm6kSystemRebootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kSystemRebootTimer.setStatus("mandatory")
_Sm6kSystemMiscellaneous_ObjectIdentity = ObjectIdentity
sm6kSystemMiscellaneous = _Sm6kSystemMiscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11)
)
_Sm6kSystemMiscellaneousTimeText_Type = DisplayString
_Sm6kSystemMiscellaneousTimeText_Object = MibScalar
sm6kSystemMiscellaneousTimeText = _Sm6kSystemMiscellaneousTimeText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 1),
    _Sm6kSystemMiscellaneousTimeText_Type()
)
sm6kSystemMiscellaneousTimeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMiscellaneousTimeText.setStatus("mandatory")
_Sm6kSystemMiscellaneousTime_Type = Counter32
_Sm6kSystemMiscellaneousTime_Object = MibScalar
sm6kSystemMiscellaneousTime = _Sm6kSystemMiscellaneousTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 2),
    _Sm6kSystemMiscellaneousTime_Type()
)
sm6kSystemMiscellaneousTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMiscellaneousTime.setStatus("mandatory")
_Sm6kSystemMiscellaneousRandom_Type = Integer32
_Sm6kSystemMiscellaneousRandom_Object = MibScalar
sm6kSystemMiscellaneousRandom = _Sm6kSystemMiscellaneousRandom_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 3),
    _Sm6kSystemMiscellaneousRandom_Type()
)
sm6kSystemMiscellaneousRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMiscellaneousRandom.setStatus("mandatory")
_Sm6kSystemMiscellaneousFreeSpace_Type = Integer32
_Sm6kSystemMiscellaneousFreeSpace_Object = MibScalar
sm6kSystemMiscellaneousFreeSpace = _Sm6kSystemMiscellaneousFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 4),
    _Sm6kSystemMiscellaneousFreeSpace_Type()
)
sm6kSystemMiscellaneousFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMiscellaneousFreeSpace.setStatus("mandatory")
_Sm6kSystemMiscellaneousPublicKey_Type = DisplayString
_Sm6kSystemMiscellaneousPublicKey_Object = MibScalar
sm6kSystemMiscellaneousPublicKey = _Sm6kSystemMiscellaneousPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 5),
    _Sm6kSystemMiscellaneousPublicKey_Type()
)
sm6kSystemMiscellaneousPublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kSystemMiscellaneousPublicKey.setStatus("mandatory")
_Sm6kSystemMiscellaneousLocalSocket_Type = Integer32
_Sm6kSystemMiscellaneousLocalSocket_Object = MibScalar
sm6kSystemMiscellaneousLocalSocket = _Sm6kSystemMiscellaneousLocalSocket_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 2, 11, 6),
    _Sm6kSystemMiscellaneousLocalSocket_Type()
)
sm6kSystemMiscellaneousLocalSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kSystemMiscellaneousLocalSocket.setStatus("mandatory")
_Sm6kNetworkInformation_ObjectIdentity = ObjectIdentity
sm6kNetworkInformation = _Sm6kNetworkInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3)
)
_Sm6kNetworkSessionInformation_ObjectIdentity = ObjectIdentity
sm6kNetworkSessionInformation = _Sm6kNetworkSessionInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1)
)
_Sm6kNetworkSessionCount_Type = Integer32
_Sm6kNetworkSessionCount_Object = MibScalar
sm6kNetworkSessionCount = _Sm6kNetworkSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 1),
    _Sm6kNetworkSessionCount_Type()
)
sm6kNetworkSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionCount.setStatus("mandatory")
_Sm6kNetworkSessionTable_Object = MibTable
sm6kNetworkSessionTable = _Sm6kNetworkSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sm6kNetworkSessionTable.setStatus("mandatory")
_Sm6kNetworkSessionEntry_Object = MibTableRow
sm6kNetworkSessionEntry = _Sm6kNetworkSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1)
)
sm6kNetworkSessionEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kNetworkSessionName"),
)
if mibBuilder.loadTexts:
    sm6kNetworkSessionEntry.setStatus("mandatory")
_Sm6kNetworkSessionName_Type = DisplayString
_Sm6kNetworkSessionName_Object = MibTableColumn
sm6kNetworkSessionName = _Sm6kNetworkSessionName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 1),
    _Sm6kNetworkSessionName_Type()
)
sm6kNetworkSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionName.setStatus("mandatory")


class _Sm6kNetworkSessionCurrentState_Type(Integer32):
    """Custom type sm6kNetworkSessionCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_Sm6kNetworkSessionCurrentState_Type.__name__ = "Integer32"
_Sm6kNetworkSessionCurrentState_Object = MibTableColumn
sm6kNetworkSessionCurrentState = _Sm6kNetworkSessionCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 2),
    _Sm6kNetworkSessionCurrentState_Type()
)
sm6kNetworkSessionCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionCurrentState.setStatus("mandatory")
_Sm6kNetworkSessionLastStateChange_Type = DisplayString
_Sm6kNetworkSessionLastStateChange_Object = MibTableColumn
sm6kNetworkSessionLastStateChange = _Sm6kNetworkSessionLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 3),
    _Sm6kNetworkSessionLastStateChange_Type()
)
sm6kNetworkSessionLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionLastStateChange.setStatus("mandatory")
_Sm6kNetworkSessionLastPollAttempt_Type = DisplayString
_Sm6kNetworkSessionLastPollAttempt_Object = MibTableColumn
sm6kNetworkSessionLastPollAttempt = _Sm6kNetworkSessionLastPollAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 4),
    _Sm6kNetworkSessionLastPollAttempt_Type()
)
sm6kNetworkSessionLastPollAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionLastPollAttempt.setStatus("mandatory")


class _Sm6kNetworkSessionAddressFamily_Type(Integer32):
    """Custom type sm6kNetworkSessionAddressFamily based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 16),
          ("ccitt", 10),
          ("chaos", 5),
          ("datakit", 9),
          ("decnet", 12),
          ("dli", 13),
          ("ecma", 8),
          ("hylink", 15),
          ("implink", 3),
          ("inet", 2),
          ("intf", 20),
          ("lat", 14),
          ("link", 18),
          ("netware", 22),
          ("ns", 6),
          ("osi", 7),
          ("pup", 4),
          ("reserved23", 23),
          ("reserved24", 24),
          ("reserved25", 25),
          ("reserved26", 26),
          ("reserved27", 27),
          ("reserved28", 28),
          ("reserved29", 29),
          ("reserved30", 30),
          ("reserved31", 31),
          ("reserved32", 32),
          ("rif", 21),
          ("route", 17),
          ("sna", 11),
          ("unix", 1),
          ("unknown", 65535),
          ("xtpPseudo", 19))
    )


_Sm6kNetworkSessionAddressFamily_Type.__name__ = "Integer32"
_Sm6kNetworkSessionAddressFamily_Object = MibTableColumn
sm6kNetworkSessionAddressFamily = _Sm6kNetworkSessionAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 5),
    _Sm6kNetworkSessionAddressFamily_Type()
)
sm6kNetworkSessionAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionAddressFamily.setStatus("mandatory")
_Sm6kNetworkSessionNetAddress_Type = DisplayString
_Sm6kNetworkSessionNetAddress_Object = MibTableColumn
sm6kNetworkSessionNetAddress = _Sm6kNetworkSessionNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 6),
    _Sm6kNetworkSessionNetAddress_Type()
)
sm6kNetworkSessionNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionNetAddress.setStatus("mandatory")
_Sm6kNetworkSessionTransmitAttempts_Type = Counter32
_Sm6kNetworkSessionTransmitAttempts_Object = MibTableColumn
sm6kNetworkSessionTransmitAttempts = _Sm6kNetworkSessionTransmitAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 7),
    _Sm6kNetworkSessionTransmitAttempts_Type()
)
sm6kNetworkSessionTransmitAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionTransmitAttempts.setStatus("mandatory")
_Sm6kNetworkSessionPacketsReceived_Type = Counter32
_Sm6kNetworkSessionPacketsReceived_Object = MibTableColumn
sm6kNetworkSessionPacketsReceived = _Sm6kNetworkSessionPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 8),
    _Sm6kNetworkSessionPacketsReceived_Type()
)
sm6kNetworkSessionPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionPacketsReceived.setStatus("mandatory")
_Sm6kNetworkSessionLastTransmitTime_Type = DisplayString
_Sm6kNetworkSessionLastTransmitTime_Object = MibTableColumn
sm6kNetworkSessionLastTransmitTime = _Sm6kNetworkSessionLastTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 9),
    _Sm6kNetworkSessionLastTransmitTime_Type()
)
sm6kNetworkSessionLastTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionLastTransmitTime.setStatus("mandatory")
_Sm6kNetworkSessionLastReceiveTime_Type = DisplayString
_Sm6kNetworkSessionLastReceiveTime_Object = MibTableColumn
sm6kNetworkSessionLastReceiveTime = _Sm6kNetworkSessionLastReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 10),
    _Sm6kNetworkSessionLastReceiveTime_Type()
)
sm6kNetworkSessionLastReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionLastReceiveTime.setStatus("mandatory")
_Sm6kNetworkSessionMinimumResponseTime_Type = Integer32
_Sm6kNetworkSessionMinimumResponseTime_Object = MibTableColumn
sm6kNetworkSessionMinimumResponseTime = _Sm6kNetworkSessionMinimumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 11),
    _Sm6kNetworkSessionMinimumResponseTime_Type()
)
sm6kNetworkSessionMinimumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionMinimumResponseTime.setStatus("mandatory")
_Sm6kNetworkSessionRecentAverageResponseTime_Type = Integer32
_Sm6kNetworkSessionRecentAverageResponseTime_Object = MibTableColumn
sm6kNetworkSessionRecentAverageResponseTime = _Sm6kNetworkSessionRecentAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 12),
    _Sm6kNetworkSessionRecentAverageResponseTime_Type()
)
sm6kNetworkSessionRecentAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionRecentAverageResponseTime.setStatus("mandatory")
_Sm6kNetworkSessionLifeTimeAverageResponseTime_Type = Integer32
_Sm6kNetworkSessionLifeTimeAverageResponseTime_Object = MibTableColumn
sm6kNetworkSessionLifeTimeAverageResponseTime = _Sm6kNetworkSessionLifeTimeAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 13),
    _Sm6kNetworkSessionLifeTimeAverageResponseTime_Type()
)
sm6kNetworkSessionLifeTimeAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionLifeTimeAverageResponseTime.setStatus("mandatory")
_Sm6kNetworkSessionMaximumResponseTime_Type = Integer32
_Sm6kNetworkSessionMaximumResponseTime_Object = MibTableColumn
sm6kNetworkSessionMaximumResponseTime = _Sm6kNetworkSessionMaximumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 14),
    _Sm6kNetworkSessionMaximumResponseTime_Type()
)
sm6kNetworkSessionMaximumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kNetworkSessionMaximumResponseTime.setStatus("mandatory")
_Sm6kCommand_ObjectIdentity = ObjectIdentity
sm6kCommand = _Sm6kCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4)
)
_Sm6kCommandTable_Object = MibTable
sm6kCommandTable = _Sm6kCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1)
)
if mibBuilder.loadTexts:
    sm6kCommandTable.setStatus("mandatory")
_Sm6kCommandEntry_Object = MibTableRow
sm6kCommandEntry = _Sm6kCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1)
)
sm6kCommandEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kCommandName"),
)
if mibBuilder.loadTexts:
    sm6kCommandEntry.setStatus("mandatory")


class _Sm6kCommandState_Type(Integer32):
    """Custom type sm6kCommandState based on Integer32"""
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


_Sm6kCommandState_Type.__name__ = "Integer32"
_Sm6kCommandState_Object = MibTableColumn
sm6kCommandState = _Sm6kCommandState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 1),
    _Sm6kCommandState_Type()
)
sm6kCommandState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandState.setStatus("mandatory")
_Sm6kCommandName_Type = DisplayString
_Sm6kCommandName_Object = MibTableColumn
sm6kCommandName = _Sm6kCommandName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 2),
    _Sm6kCommandName_Type()
)
sm6kCommandName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandName.setStatus("mandatory")
_Sm6kCommandDescription_Type = DisplayString
_Sm6kCommandDescription_Object = MibTableColumn
sm6kCommandDescription = _Sm6kCommandDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 3),
    _Sm6kCommandDescription_Type()
)
sm6kCommandDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandDescription.setStatus("mandatory")
_Sm6kCommandOwnerID_Type = DisplayString
_Sm6kCommandOwnerID_Object = MibTableColumn
sm6kCommandOwnerID = _Sm6kCommandOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 4),
    _Sm6kCommandOwnerID_Type()
)
sm6kCommandOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandOwnerID.setStatus("mandatory")
_Sm6kCommandGetStringAndParameters_Type = DisplayString
_Sm6kCommandGetStringAndParameters_Object = MibTableColumn
sm6kCommandGetStringAndParameters = _Sm6kCommandGetStringAndParameters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 5),
    _Sm6kCommandGetStringAndParameters_Type()
)
sm6kCommandGetStringAndParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandGetStringAndParameters.setStatus("mandatory")
_Sm6kCommandSetStringAndParameters_Type = DisplayString
_Sm6kCommandSetStringAndParameters_Object = MibTableColumn
sm6kCommandSetStringAndParameters = _Sm6kCommandSetStringAndParameters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 6),
    _Sm6kCommandSetStringAndParameters_Type()
)
sm6kCommandSetStringAndParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandSetStringAndParameters.setStatus("mandatory")


class _Sm6kCommandTimeOutValue_Type(Integer32):
    """Custom type sm6kCommandTimeOutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Sm6kCommandTimeOutValue_Type.__name__ = "Integer32"
_Sm6kCommandTimeOutValue_Object = MibTableColumn
sm6kCommandTimeOutValue = _Sm6kCommandTimeOutValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 7),
    _Sm6kCommandTimeOutValue_Type()
)
sm6kCommandTimeOutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandTimeOutValue.setStatus("mandatory")


class _Sm6kCommandCountToLive_Type(Integer32):
    """Custom type sm6kCommandCountToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sm6kCommandCountToLive_Type.__name__ = "Integer32"
_Sm6kCommandCountToLive_Object = MibTableColumn
sm6kCommandCountToLive = _Sm6kCommandCountToLive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 8),
    _Sm6kCommandCountToLive_Type()
)
sm6kCommandCountToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kCommandCountToLive.setStatus("mandatory")


class _Sm6kCommandTimeToLive_Type(Integer32):
    """Custom type sm6kCommandTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sm6kCommandTimeToLive_Type.__name__ = "Integer32"
_Sm6kCommandTimeToLive_Object = MibTableColumn
sm6kCommandTimeToLive = _Sm6kCommandTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 9),
    _Sm6kCommandTimeToLive_Type()
)
sm6kCommandTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandTimeToLive.setStatus("mandatory")


class _Sm6kCommandOutputResultIndex_Type(Integer32):
    """Custom type sm6kCommandOutputResultIndex based on Integer32"""
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


_Sm6kCommandOutputResultIndex_Type.__name__ = "Integer32"
_Sm6kCommandOutputResultIndex_Object = MibTableColumn
sm6kCommandOutputResultIndex = _Sm6kCommandOutputResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 10),
    _Sm6kCommandOutputResultIndex_Type()
)
sm6kCommandOutputResultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandOutputResultIndex.setStatus("mandatory")


class _Sm6kCommandOutputRowIndex_Type(Integer32):
    """Custom type sm6kCommandOutputRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sm6kCommandOutputRowIndex_Type.__name__ = "Integer32"
_Sm6kCommandOutputRowIndex_Object = MibTableColumn
sm6kCommandOutputRowIndex = _Sm6kCommandOutputRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 11),
    _Sm6kCommandOutputRowIndex_Type()
)
sm6kCommandOutputRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandOutputRowIndex.setStatus("mandatory")


class _Sm6kCommandOutputColumnIndex_Type(Integer32):
    """Custom type sm6kCommandOutputColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sm6kCommandOutputColumnIndex_Type.__name__ = "Integer32"
_Sm6kCommandOutputColumnIndex_Object = MibTableColumn
sm6kCommandOutputColumnIndex = _Sm6kCommandOutputColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 12),
    _Sm6kCommandOutputColumnIndex_Type()
)
sm6kCommandOutputColumnIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandOutputColumnIndex.setStatus("mandatory")
_Sm6kCommandDisplayStringResult_Type = DisplayString
_Sm6kCommandDisplayStringResult_Object = MibTableColumn
sm6kCommandDisplayStringResult = _Sm6kCommandDisplayStringResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 13),
    _Sm6kCommandDisplayStringResult_Type()
)
sm6kCommandDisplayStringResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandDisplayStringResult.setStatus("mandatory")
_Sm6kCommandIntegerResult_Type = Integer32
_Sm6kCommandIntegerResult_Object = MibTableColumn
sm6kCommandIntegerResult = _Sm6kCommandIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 14),
    _Sm6kCommandIntegerResult_Type()
)
sm6kCommandIntegerResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandIntegerResult.setStatus("mandatory")
_Sm6kCommandCounterResult_Type = Counter32
_Sm6kCommandCounterResult_Object = MibTableColumn
sm6kCommandCounterResult = _Sm6kCommandCounterResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 15),
    _Sm6kCommandCounterResult_Type()
)
sm6kCommandCounterResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandCounterResult.setStatus("mandatory")
_Sm6kCommandGaugeResult_Type = Gauge32
_Sm6kCommandGaugeResult_Object = MibTableColumn
sm6kCommandGaugeResult = _Sm6kCommandGaugeResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 16),
    _Sm6kCommandGaugeResult_Type()
)
sm6kCommandGaugeResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kCommandGaugeResult.setStatus("mandatory")
_Sm6kCommandExecutionReturnCode_Type = Integer32
_Sm6kCommandExecutionReturnCode_Object = MibTableColumn
sm6kCommandExecutionReturnCode = _Sm6kCommandExecutionReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 17),
    _Sm6kCommandExecutionReturnCode_Type()
)
sm6kCommandExecutionReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kCommandExecutionReturnCode.setStatus("mandatory")
_Sm6kCommandStandardError_Type = DisplayString
_Sm6kCommandStandardError_Object = MibTableColumn
sm6kCommandStandardError = _Sm6kCommandStandardError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 4, 1, 1, 18),
    _Sm6kCommandStandardError_Type()
)
sm6kCommandStandardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kCommandStandardError.setStatus("mandatory")
_Sm6kThreshold_ObjectIdentity = ObjectIdentity
sm6kThreshold = _Sm6kThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5)
)
_Sm6kThresholdTable_Object = MibTable
sm6kThresholdTable = _Sm6kThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1)
)
if mibBuilder.loadTexts:
    sm6kThresholdTable.setStatus("mandatory")
_Sm6kThresholdEntry_Object = MibTableRow
sm6kThresholdEntry = _Sm6kThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1)
)
sm6kThresholdEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kThresholdName"),
)
if mibBuilder.loadTexts:
    sm6kThresholdEntry.setStatus("mandatory")


class _Sm6kThresholdState_Type(Integer32):
    """Custom type sm6kThresholdState based on Integer32"""
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
        *(("disabled", 1),
          ("enabledStoreOnly", 4),
          ("enabledThresholdOnly", 3),
          ("enabledThresholdStore", 5),
          ("invalid", 2))
    )


_Sm6kThresholdState_Type.__name__ = "Integer32"
_Sm6kThresholdState_Object = MibTableColumn
sm6kThresholdState = _Sm6kThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 1),
    _Sm6kThresholdState_Type()
)
sm6kThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdState.setStatus("mandatory")
_Sm6kThresholdName_Type = DisplayString
_Sm6kThresholdName_Object = MibTableColumn
sm6kThresholdName = _Sm6kThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 2),
    _Sm6kThresholdName_Type()
)
sm6kThresholdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdName.setStatus("mandatory")
_Sm6kThresholdDescription_Type = DisplayString
_Sm6kThresholdDescription_Object = MibTableColumn
sm6kThresholdDescription = _Sm6kThresholdDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 3),
    _Sm6kThresholdDescription_Type()
)
sm6kThresholdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdDescription.setStatus("mandatory")
_Sm6kThresholdOwnerID_Type = DisplayString
_Sm6kThresholdOwnerID_Object = MibTableColumn
sm6kThresholdOwnerID = _Sm6kThresholdOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 4),
    _Sm6kThresholdOwnerID_Type()
)
sm6kThresholdOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdOwnerID.setStatus("mandatory")
_Sm6kThresholdLocalRemoteMIBVariable_Type = DisplayString
_Sm6kThresholdLocalRemoteMIBVariable_Object = MibTableColumn
sm6kThresholdLocalRemoteMIBVariable = _Sm6kThresholdLocalRemoteMIBVariable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 5),
    _Sm6kThresholdLocalRemoteMIBVariable_Type()
)
sm6kThresholdLocalRemoteMIBVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdLocalRemoteMIBVariable.setStatus("mandatory")
_Sm6kThresholdCondition_Type = DisplayString
_Sm6kThresholdCondition_Object = MibTableColumn
sm6kThresholdCondition = _Sm6kThresholdCondition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 6),
    _Sm6kThresholdCondition_Type()
)
sm6kThresholdCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdCondition.setStatus("mandatory")
_Sm6kThresholdValue_Type = DisplayString
_Sm6kThresholdValue_Object = MibTableColumn
sm6kThresholdValue = _Sm6kThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 7),
    _Sm6kThresholdValue_Type()
)
sm6kThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdValue.setStatus("mandatory")
_Sm6kThresholdPollTime_Type = DisplayString
_Sm6kThresholdPollTime_Object = MibTableColumn
sm6kThresholdPollTime = _Sm6kThresholdPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 8),
    _Sm6kThresholdPollTime_Type()
)
sm6kThresholdPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdPollTime.setStatus("mandatory")
_Sm6kThresholdLastValue_Type = DisplayString
_Sm6kThresholdLastValue_Object = MibTableColumn
sm6kThresholdLastValue = _Sm6kThresholdLastValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 9),
    _Sm6kThresholdLastValue_Type()
)
sm6kThresholdLastValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdLastValue.setStatus("mandatory")
_Sm6kThresholdIntegerDataMax_Type = Integer32
_Sm6kThresholdIntegerDataMax_Object = MibTableColumn
sm6kThresholdIntegerDataMax = _Sm6kThresholdIntegerDataMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 10),
    _Sm6kThresholdIntegerDataMax_Type()
)
sm6kThresholdIntegerDataMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdIntegerDataMax.setStatus("mandatory")
_Sm6kThresholdIntegerDataMin_Type = Integer32
_Sm6kThresholdIntegerDataMin_Object = MibTableColumn
sm6kThresholdIntegerDataMin = _Sm6kThresholdIntegerDataMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 11),
    _Sm6kThresholdIntegerDataMin_Type()
)
sm6kThresholdIntegerDataMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdIntegerDataMin.setStatus("mandatory")
_Sm6kThresholdIntegerDataAvg_Type = Integer32
_Sm6kThresholdIntegerDataAvg_Object = MibTableColumn
sm6kThresholdIntegerDataAvg = _Sm6kThresholdIntegerDataAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 12),
    _Sm6kThresholdIntegerDataAvg_Type()
)
sm6kThresholdIntegerDataAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdIntegerDataAvg.setStatus("mandatory")
_Sm6kThresholdCounterGaugeDataMax_Type = Gauge32
_Sm6kThresholdCounterGaugeDataMax_Object = MibTableColumn
sm6kThresholdCounterGaugeDataMax = _Sm6kThresholdCounterGaugeDataMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 13),
    _Sm6kThresholdCounterGaugeDataMax_Type()
)
sm6kThresholdCounterGaugeDataMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdCounterGaugeDataMax.setStatus("mandatory")
_Sm6kThresholdCounterGaugeDataMin_Type = Gauge32
_Sm6kThresholdCounterGaugeDataMin_Object = MibTableColumn
sm6kThresholdCounterGaugeDataMin = _Sm6kThresholdCounterGaugeDataMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 14),
    _Sm6kThresholdCounterGaugeDataMin_Type()
)
sm6kThresholdCounterGaugeDataMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdCounterGaugeDataMin.setStatus("mandatory")
_Sm6kThresholdCounterGaugeDataAvg_Type = Gauge32
_Sm6kThresholdCounterGaugeDataAvg_Object = MibTableColumn
sm6kThresholdCounterGaugeDataAvg = _Sm6kThresholdCounterGaugeDataAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 15),
    _Sm6kThresholdCounterGaugeDataAvg_Type()
)
sm6kThresholdCounterGaugeDataAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdCounterGaugeDataAvg.setStatus("mandatory")
_Sm6kThresholdDataSamples_Type = Counter32
_Sm6kThresholdDataSamples_Object = MibTableColumn
sm6kThresholdDataSamples = _Sm6kThresholdDataSamples_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 16),
    _Sm6kThresholdDataSamples_Type()
)
sm6kThresholdDataSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdDataSamples.setStatus("mandatory")
_Sm6kThresholdTrapDescription_Type = DisplayString
_Sm6kThresholdTrapDescription_Object = MibTableColumn
sm6kThresholdTrapDescription = _Sm6kThresholdTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 17),
    _Sm6kThresholdTrapDescription_Type()
)
sm6kThresholdTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdTrapDescription.setStatus("mandatory")
_Sm6kThresholdArmEnterprise_Type = DisplayString
_Sm6kThresholdArmEnterprise_Object = MibTableColumn
sm6kThresholdArmEnterprise = _Sm6kThresholdArmEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 18),
    _Sm6kThresholdArmEnterprise_Type()
)
sm6kThresholdArmEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdArmEnterprise.setStatus("mandatory")
_Sm6kThresholdSpecificTrap_Type = Integer32
_Sm6kThresholdSpecificTrap_Object = MibTableColumn
sm6kThresholdSpecificTrap = _Sm6kThresholdSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 19),
    _Sm6kThresholdSpecificTrap_Type()
)
sm6kThresholdSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdSpecificTrap.setStatus("mandatory")
_Sm6kThresholdCommandToExecute_Type = DisplayString
_Sm6kThresholdCommandToExecute_Object = MibTableColumn
sm6kThresholdCommandToExecute = _Sm6kThresholdCommandToExecute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 20),
    _Sm6kThresholdCommandToExecute_Type()
)
sm6kThresholdCommandToExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdCommandToExecute.setStatus("mandatory")
_Sm6kThresholdReArmCondition_Type = DisplayString
_Sm6kThresholdReArmCondition_Object = MibTableColumn
sm6kThresholdReArmCondition = _Sm6kThresholdReArmCondition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 21),
    _Sm6kThresholdReArmCondition_Type()
)
sm6kThresholdReArmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdReArmCondition.setStatus("mandatory")
_Sm6kThresholdReArmValue_Type = DisplayString
_Sm6kThresholdReArmValue_Object = MibTableColumn
sm6kThresholdReArmValue = _Sm6kThresholdReArmValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 22),
    _Sm6kThresholdReArmValue_Type()
)
sm6kThresholdReArmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdReArmValue.setStatus("mandatory")
_Sm6kThresholdReArmTrapDescription_Type = DisplayString
_Sm6kThresholdReArmTrapDescription_Object = MibTableColumn
sm6kThresholdReArmTrapDescription = _Sm6kThresholdReArmTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 23),
    _Sm6kThresholdReArmTrapDescription_Type()
)
sm6kThresholdReArmTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdReArmTrapDescription.setStatus("mandatory")
_Sm6kThresholdReArmEnterprise_Type = DisplayString
_Sm6kThresholdReArmEnterprise_Object = MibTableColumn
sm6kThresholdReArmEnterprise = _Sm6kThresholdReArmEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 24),
    _Sm6kThresholdReArmEnterprise_Type()
)
sm6kThresholdReArmEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdReArmEnterprise.setStatus("mandatory")
_Sm6kThresholdReArmSpecificTrap_Type = Integer32
_Sm6kThresholdReArmSpecificTrap_Object = MibTableColumn
sm6kThresholdReArmSpecificTrap = _Sm6kThresholdReArmSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 25),
    _Sm6kThresholdReArmSpecificTrap_Type()
)
sm6kThresholdReArmSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdReArmSpecificTrap.setStatus("mandatory")
_Sm6kThresholdReArmCommandToExecute_Type = DisplayString
_Sm6kThresholdReArmCommandToExecute_Object = MibTableColumn
sm6kThresholdReArmCommandToExecute = _Sm6kThresholdReArmCommandToExecute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 26),
    _Sm6kThresholdReArmCommandToExecute_Type()
)
sm6kThresholdReArmCommandToExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdReArmCommandToExecute.setStatus("mandatory")
_Sm6kThresholdLastChangedSession_Type = DisplayString
_Sm6kThresholdLastChangedSession_Object = MibTableColumn
sm6kThresholdLastChangedSession = _Sm6kThresholdLastChangedSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 27),
    _Sm6kThresholdLastChangedSession_Type()
)
sm6kThresholdLastChangedSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdLastChangedSession.setStatus("mandatory")
_Sm6kThresholdStandardError_Type = DisplayString
_Sm6kThresholdStandardError_Object = MibTableColumn
sm6kThresholdStandardError = _Sm6kThresholdStandardError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 28),
    _Sm6kThresholdStandardError_Type()
)
sm6kThresholdStandardError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdStandardError.setStatus("mandatory")
_Sm6kThresholdLastResponseTime_Type = DisplayString
_Sm6kThresholdLastResponseTime_Object = MibTableColumn
sm6kThresholdLastResponseTime = _Sm6kThresholdLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 29),
    _Sm6kThresholdLastResponseTime_Type()
)
sm6kThresholdLastResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kThresholdLastResponseTime.setStatus("mandatory")
_Sm6kThresholdResponseCount_Type = Counter32
_Sm6kThresholdResponseCount_Object = MibTableColumn
sm6kThresholdResponseCount = _Sm6kThresholdResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 30),
    _Sm6kThresholdResponseCount_Type()
)
sm6kThresholdResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdResponseCount.setStatus("mandatory")
_Sm6kThresholdTimeoutCount_Type = Counter32
_Sm6kThresholdTimeoutCount_Object = MibTableColumn
sm6kThresholdTimeoutCount = _Sm6kThresholdTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 31),
    _Sm6kThresholdTimeoutCount_Type()
)
sm6kThresholdTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdTimeoutCount.setStatus("mandatory")
_Sm6kThresholdNoValueCount_Type = Counter32
_Sm6kThresholdNoValueCount_Object = MibTableColumn
sm6kThresholdNoValueCount = _Sm6kThresholdNoValueCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 32),
    _Sm6kThresholdNoValueCount_Type()
)
sm6kThresholdNoValueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kThresholdNoValueCount.setStatus("mandatory")
_Sm6kAnalysis_ObjectIdentity = ObjectIdentity
sm6kAnalysis = _Sm6kAnalysis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6)
)
_Sm6kAnalysisTable_Object = MibTable
sm6kAnalysisTable = _Sm6kAnalysisTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1)
)
if mibBuilder.loadTexts:
    sm6kAnalysisTable.setStatus("mandatory")
_Sm6kAnalysisEntry_Object = MibTableRow
sm6kAnalysisEntry = _Sm6kAnalysisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1)
)
sm6kAnalysisEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kAnalysisName"),
)
if mibBuilder.loadTexts:
    sm6kAnalysisEntry.setStatus("mandatory")


class _Sm6kAnalysisState_Type(Integer32):
    """Custom type sm6kAnalysisState based on Integer32"""
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


_Sm6kAnalysisState_Type.__name__ = "Integer32"
_Sm6kAnalysisState_Object = MibTableColumn
sm6kAnalysisState = _Sm6kAnalysisState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 1),
    _Sm6kAnalysisState_Type()
)
sm6kAnalysisState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisState.setStatus("mandatory")
_Sm6kAnalysisName_Type = DisplayString
_Sm6kAnalysisName_Object = MibTableColumn
sm6kAnalysisName = _Sm6kAnalysisName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 2),
    _Sm6kAnalysisName_Type()
)
sm6kAnalysisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisName.setStatus("mandatory")
_Sm6kAnalysisDescription_Type = DisplayString
_Sm6kAnalysisDescription_Object = MibTableColumn
sm6kAnalysisDescription = _Sm6kAnalysisDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 3),
    _Sm6kAnalysisDescription_Type()
)
sm6kAnalysisDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisDescription.setStatus("mandatory")
_Sm6kAnalysisOwnerID_Type = DisplayString
_Sm6kAnalysisOwnerID_Object = MibTableColumn
sm6kAnalysisOwnerID = _Sm6kAnalysisOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 4),
    _Sm6kAnalysisOwnerID_Type()
)
sm6kAnalysisOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisOwnerID.setStatus("mandatory")
_Sm6kAnalysisLocalRemoteMIBVariableExpression_Type = DisplayString
_Sm6kAnalysisLocalRemoteMIBVariableExpression_Object = MibTableColumn
sm6kAnalysisLocalRemoteMIBVariableExpression = _Sm6kAnalysisLocalRemoteMIBVariableExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 5),
    _Sm6kAnalysisLocalRemoteMIBVariableExpression_Type()
)
sm6kAnalysisLocalRemoteMIBVariableExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisLocalRemoteMIBVariableExpression.setStatus("mandatory")
_Sm6kAnalysisPollTime_Type = DisplayString
_Sm6kAnalysisPollTime_Object = MibTableColumn
sm6kAnalysisPollTime = _Sm6kAnalysisPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 6),
    _Sm6kAnalysisPollTime_Type()
)
sm6kAnalysisPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisPollTime.setStatus("mandatory")


class _Sm6kAnalysisResultIndex_Type(Integer32):
    """Custom type sm6kAnalysisResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("counter", 3),
          ("gauge", 4),
          ("integer", 2))
    )


_Sm6kAnalysisResultIndex_Type.__name__ = "Integer32"
_Sm6kAnalysisResultIndex_Object = MibTableColumn
sm6kAnalysisResultIndex = _Sm6kAnalysisResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 7),
    _Sm6kAnalysisResultIndex_Type()
)
sm6kAnalysisResultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAnalysisResultIndex.setStatus("mandatory")
_Sm6kAnalysisIntegerResult_Type = Integer32
_Sm6kAnalysisIntegerResult_Object = MibTableColumn
sm6kAnalysisIntegerResult = _Sm6kAnalysisIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 8),
    _Sm6kAnalysisIntegerResult_Type()
)
sm6kAnalysisIntegerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAnalysisIntegerResult.setStatus("mandatory")
_Sm6kAnalysisCounterResult_Type = Counter32
_Sm6kAnalysisCounterResult_Object = MibTableColumn
sm6kAnalysisCounterResult = _Sm6kAnalysisCounterResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 9),
    _Sm6kAnalysisCounterResult_Type()
)
sm6kAnalysisCounterResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAnalysisCounterResult.setStatus("mandatory")
_Sm6kAnalysisGaugeResult_Type = Gauge32
_Sm6kAnalysisGaugeResult_Object = MibTableColumn
sm6kAnalysisGaugeResult = _Sm6kAnalysisGaugeResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 10),
    _Sm6kAnalysisGaugeResult_Type()
)
sm6kAnalysisGaugeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAnalysisGaugeResult.setStatus("mandatory")
_Sm6kAnalysisDisplayStringResult_Type = DisplayString
_Sm6kAnalysisDisplayStringResult_Object = MibTableColumn
sm6kAnalysisDisplayStringResult = _Sm6kAnalysisDisplayStringResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 11),
    _Sm6kAnalysisDisplayStringResult_Type()
)
sm6kAnalysisDisplayStringResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAnalysisDisplayStringResult.setStatus("mandatory")
_Sm6kAnalysisReturnCode_Type = Integer32
_Sm6kAnalysisReturnCode_Object = MibTableColumn
sm6kAnalysisReturnCode = _Sm6kAnalysisReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 12),
    _Sm6kAnalysisReturnCode_Type()
)
sm6kAnalysisReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAnalysisReturnCode.setStatus("mandatory")
_Sm6kAnalysisStandardError_Type = DisplayString
_Sm6kAnalysisStandardError_Object = MibTableColumn
sm6kAnalysisStandardError = _Sm6kAnalysisStandardError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 13),
    _Sm6kAnalysisStandardError_Type()
)
sm6kAnalysisStandardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAnalysisStandardError.setStatus("mandatory")
_Sm6kFilter_ObjectIdentity = ObjectIdentity
sm6kFilter = _Sm6kFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7)
)


class _Sm6kFilterDefaultAction_Type(Integer32):
    """Custom type sm6kFilterDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockTraps", 2),
          ("sendTraps", 1))
    )


_Sm6kFilterDefaultAction_Type.__name__ = "Integer32"
_Sm6kFilterDefaultAction_Object = MibScalar
sm6kFilterDefaultAction = _Sm6kFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 1),
    _Sm6kFilterDefaultAction_Type()
)
sm6kFilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterDefaultAction.setStatus("mandatory")


class _Sm6kFilterTrapReception_Type(Integer32):
    """Custom type sm6kFilterTrapReception based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sm6kFilterTrapReception_Type.__name__ = "Integer32"
_Sm6kFilterTrapReception_Object = MibScalar
sm6kFilterTrapReception = _Sm6kFilterTrapReception_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 2),
    _Sm6kFilterTrapReception_Type()
)
sm6kFilterTrapReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterTrapReception.setStatus("mandatory")
_Sm6kFilterTotalTrapsReceived_Type = Counter32
_Sm6kFilterTotalTrapsReceived_Object = MibScalar
sm6kFilterTotalTrapsReceived = _Sm6kFilterTotalTrapsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 3),
    _Sm6kFilterTotalTrapsReceived_Type()
)
sm6kFilterTotalTrapsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kFilterTotalTrapsReceived.setStatus("mandatory")
_Sm6kFilterTable_Object = MibTable
sm6kFilterTable = _Sm6kFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4)
)
if mibBuilder.loadTexts:
    sm6kFilterTable.setStatus("mandatory")
_Sm6kFilterEntry_Object = MibTableRow
sm6kFilterEntry = _Sm6kFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1)
)
sm6kFilterEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kFilterName"),
)
if mibBuilder.loadTexts:
    sm6kFilterEntry.setStatus("mandatory")


class _Sm6kFilterState_Type(Integer32):
    """Custom type sm6kFilterState based on Integer32"""
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


_Sm6kFilterState_Type.__name__ = "Integer32"
_Sm6kFilterState_Object = MibTableColumn
sm6kFilterState = _Sm6kFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 1),
    _Sm6kFilterState_Type()
)
sm6kFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterState.setStatus("mandatory")


class _Sm6kFilterParticipationState_Type(Integer32):
    """Custom type sm6kFilterParticipationState based on Integer32"""
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


_Sm6kFilterParticipationState_Type.__name__ = "Integer32"
_Sm6kFilterParticipationState_Object = MibTableColumn
sm6kFilterParticipationState = _Sm6kFilterParticipationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 2),
    _Sm6kFilterParticipationState_Type()
)
sm6kFilterParticipationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kFilterParticipationState.setStatus("mandatory")
_Sm6kFilterName_Type = DisplayString
_Sm6kFilterName_Object = MibTableColumn
sm6kFilterName = _Sm6kFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 3),
    _Sm6kFilterName_Type()
)
sm6kFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterName.setStatus("mandatory")
_Sm6kFilterDescription_Type = DisplayString
_Sm6kFilterDescription_Object = MibTableColumn
sm6kFilterDescription = _Sm6kFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 4),
    _Sm6kFilterDescription_Type()
)
sm6kFilterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterDescription.setStatus("mandatory")


class _Sm6kFilterAction_Type(Integer32):
    """Custom type sm6kFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockTraps", 2),
          ("sendTraps", 1),
          ("throttleTraps", 3))
    )


_Sm6kFilterAction_Type.__name__ = "Integer32"
_Sm6kFilterAction_Object = MibTableColumn
sm6kFilterAction = _Sm6kFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 5),
    _Sm6kFilterAction_Type()
)
sm6kFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterAction.setStatus("mandatory")
_Sm6kFilterEntryEnterpriseExpression_Type = DisplayString
_Sm6kFilterEntryEnterpriseExpression_Object = MibTableColumn
sm6kFilterEntryEnterpriseExpression = _Sm6kFilterEntryEnterpriseExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 6),
    _Sm6kFilterEntryEnterpriseExpression_Type()
)
sm6kFilterEntryEnterpriseExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterEntryEnterpriseExpression.setStatus("mandatory")
_Sm6kFilterAgentAddrExpression_Type = DisplayString
_Sm6kFilterAgentAddrExpression_Object = MibTableColumn
sm6kFilterAgentAddrExpression = _Sm6kFilterAgentAddrExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 7),
    _Sm6kFilterAgentAddrExpression_Type()
)
sm6kFilterAgentAddrExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterAgentAddrExpression.setStatus("mandatory")
_Sm6kFilterGenericExpression_Type = DisplayString
_Sm6kFilterGenericExpression_Object = MibTableColumn
sm6kFilterGenericExpression = _Sm6kFilterGenericExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 8),
    _Sm6kFilterGenericExpression_Type()
)
sm6kFilterGenericExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterGenericExpression.setStatus("mandatory")
_Sm6kFilterSpecificExpression_Type = DisplayString
_Sm6kFilterSpecificExpression_Object = MibTableColumn
sm6kFilterSpecificExpression = _Sm6kFilterSpecificExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 9),
    _Sm6kFilterSpecificExpression_Type()
)
sm6kFilterSpecificExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterSpecificExpression.setStatus("mandatory")
_Sm6kFilterVariableExpression_Type = DisplayString
_Sm6kFilterVariableExpression_Object = MibTableColumn
sm6kFilterVariableExpression = _Sm6kFilterVariableExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 10),
    _Sm6kFilterVariableExpression_Type()
)
sm6kFilterVariableExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterVariableExpression.setStatus("mandatory")
_Sm6kFilterTotalTrapsMatched_Type = Counter32
_Sm6kFilterTotalTrapsMatched_Object = MibTableColumn
sm6kFilterTotalTrapsMatched = _Sm6kFilterTotalTrapsMatched_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 11),
    _Sm6kFilterTotalTrapsMatched_Type()
)
sm6kFilterTotalTrapsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kFilterTotalTrapsMatched.setStatus("mandatory")
_Sm6kFilterActivationTime_Type = DisplayString
_Sm6kFilterActivationTime_Object = MibTableColumn
sm6kFilterActivationTime = _Sm6kFilterActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 12),
    _Sm6kFilterActivationTime_Type()
)
sm6kFilterActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterActivationTime.setStatus("mandatory")
_Sm6kFilterActivationDayOfWeek_Type = DisplayString
_Sm6kFilterActivationDayOfWeek_Object = MibTableColumn
sm6kFilterActivationDayOfWeek = _Sm6kFilterActivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 13),
    _Sm6kFilterActivationDayOfWeek_Type()
)
sm6kFilterActivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterActivationDayOfWeek.setStatus("mandatory")
_Sm6kFilterDeactivationTime_Type = DisplayString
_Sm6kFilterDeactivationTime_Object = MibTableColumn
sm6kFilterDeactivationTime = _Sm6kFilterDeactivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 14),
    _Sm6kFilterDeactivationTime_Type()
)
sm6kFilterDeactivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterDeactivationTime.setStatus("mandatory")
_Sm6kFilterDeactivationDayOfWeek_Type = DisplayString
_Sm6kFilterDeactivationDayOfWeek_Object = MibTableColumn
sm6kFilterDeactivationDayOfWeek = _Sm6kFilterDeactivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 15),
    _Sm6kFilterDeactivationDayOfWeek_Type()
)
sm6kFilterDeactivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterDeactivationDayOfWeek.setStatus("mandatory")
_Sm6kFilterTrapDestinations_Type = DisplayString
_Sm6kFilterTrapDestinations_Object = MibTableColumn
sm6kFilterTrapDestinations = _Sm6kFilterTrapDestinations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 16),
    _Sm6kFilterTrapDestinations_Type()
)
sm6kFilterTrapDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterTrapDestinations.setStatus("mandatory")
_Sm6kFilterMatchedCommand_Type = DisplayString
_Sm6kFilterMatchedCommand_Object = MibTableColumn
sm6kFilterMatchedCommand = _Sm6kFilterMatchedCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 17),
    _Sm6kFilterMatchedCommand_Type()
)
sm6kFilterMatchedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterMatchedCommand.setStatus("mandatory")
_Sm6kFilterMatchedTrapDescription_Type = DisplayString
_Sm6kFilterMatchedTrapDescription_Object = MibTableColumn
sm6kFilterMatchedTrapDescription = _Sm6kFilterMatchedTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 18),
    _Sm6kFilterMatchedTrapDescription_Type()
)
sm6kFilterMatchedTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterMatchedTrapDescription.setStatus("mandatory")
_Sm6kFilterMatchedTrapEnterprise_Type = DisplayString
_Sm6kFilterMatchedTrapEnterprise_Object = MibTableColumn
sm6kFilterMatchedTrapEnterprise = _Sm6kFilterMatchedTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 19),
    _Sm6kFilterMatchedTrapEnterprise_Type()
)
sm6kFilterMatchedTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterMatchedTrapEnterprise.setStatus("mandatory")
_Sm6kFilterMatchedSpecificTrap_Type = Integer32
_Sm6kFilterMatchedSpecificTrap_Object = MibTableColumn
sm6kFilterMatchedSpecificTrap = _Sm6kFilterMatchedSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 20),
    _Sm6kFilterMatchedSpecificTrap_Type()
)
sm6kFilterMatchedSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterMatchedSpecificTrap.setStatus("mandatory")


class _Sm6kFilterThrottleType_Type(Integer32):
    """Custom type sm6kFilterThrottleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendAfterN", 2),
          ("sendFirstN", 1))
    )


_Sm6kFilterThrottleType_Type.__name__ = "Integer32"
_Sm6kFilterThrottleType_Object = MibTableColumn
sm6kFilterThrottleType = _Sm6kFilterThrottleType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 21),
    _Sm6kFilterThrottleType_Type()
)
sm6kFilterThrottleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleType.setStatus("mandatory")
_Sm6kFilterThrottleArmTrapCount_Type = Integer32
_Sm6kFilterThrottleArmTrapCount_Object = MibTableColumn
sm6kFilterThrottleArmTrapCount = _Sm6kFilterThrottleArmTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 22),
    _Sm6kFilterThrottleArmTrapCount_Type()
)
sm6kFilterThrottleArmTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleArmTrapCount.setStatus("mandatory")
_Sm6kFilterThrottleArmedCommand_Type = DisplayString
_Sm6kFilterThrottleArmedCommand_Object = MibTableColumn
sm6kFilterThrottleArmedCommand = _Sm6kFilterThrottleArmedCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 23),
    _Sm6kFilterThrottleArmedCommand_Type()
)
sm6kFilterThrottleArmedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleArmedCommand.setStatus("mandatory")
_Sm6kFilterThrottleArmedTrapDescription_Type = DisplayString
_Sm6kFilterThrottleArmedTrapDescription_Object = MibTableColumn
sm6kFilterThrottleArmedTrapDescription = _Sm6kFilterThrottleArmedTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 24),
    _Sm6kFilterThrottleArmedTrapDescription_Type()
)
sm6kFilterThrottleArmedTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleArmedTrapDescription.setStatus("mandatory")
_Sm6kFilterThrottleArmedTrapEnterprise_Type = DisplayString
_Sm6kFilterThrottleArmedTrapEnterprise_Object = MibTableColumn
sm6kFilterThrottleArmedTrapEnterprise = _Sm6kFilterThrottleArmedTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 25),
    _Sm6kFilterThrottleArmedTrapEnterprise_Type()
)
sm6kFilterThrottleArmedTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleArmedTrapEnterprise.setStatus("mandatory")
_Sm6kFilterThrottleArmedSpecificTrap_Type = Integer32
_Sm6kFilterThrottleArmedSpecificTrap_Object = MibTableColumn
sm6kFilterThrottleArmedSpecificTrap = _Sm6kFilterThrottleArmedSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 26),
    _Sm6kFilterThrottleArmedSpecificTrap_Type()
)
sm6kFilterThrottleArmedSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleArmedSpecificTrap.setStatus("mandatory")
_Sm6kFilterThrottleDisarmTimer_Type = DisplayString
_Sm6kFilterThrottleDisarmTimer_Object = MibTableColumn
sm6kFilterThrottleDisarmTimer = _Sm6kFilterThrottleDisarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 27),
    _Sm6kFilterThrottleDisarmTimer_Type()
)
sm6kFilterThrottleDisarmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleDisarmTimer.setStatus("mandatory")
_Sm6kFilterThrottleDisarmTrapCount_Type = Integer32
_Sm6kFilterThrottleDisarmTrapCount_Object = MibTableColumn
sm6kFilterThrottleDisarmTrapCount = _Sm6kFilterThrottleDisarmTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 28),
    _Sm6kFilterThrottleDisarmTrapCount_Type()
)
sm6kFilterThrottleDisarmTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleDisarmTrapCount.setStatus("mandatory")
_Sm6kFilterThrottleDisarmedCommand_Type = DisplayString
_Sm6kFilterThrottleDisarmedCommand_Object = MibTableColumn
sm6kFilterThrottleDisarmedCommand = _Sm6kFilterThrottleDisarmedCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 29),
    _Sm6kFilterThrottleDisarmedCommand_Type()
)
sm6kFilterThrottleDisarmedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleDisarmedCommand.setStatus("mandatory")
_Sm6kFilterThrottleDisarmedTrapDescription_Type = DisplayString
_Sm6kFilterThrottleDisarmedTrapDescription_Object = MibTableColumn
sm6kFilterThrottleDisarmedTrapDescription = _Sm6kFilterThrottleDisarmedTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 30),
    _Sm6kFilterThrottleDisarmedTrapDescription_Type()
)
sm6kFilterThrottleDisarmedTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleDisarmedTrapDescription.setStatus("mandatory")
_Sm6kFilterThrottleDisarmedTrapEnterprise_Type = DisplayString
_Sm6kFilterThrottleDisarmedTrapEnterprise_Object = MibTableColumn
sm6kFilterThrottleDisarmedTrapEnterprise = _Sm6kFilterThrottleDisarmedTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 31),
    _Sm6kFilterThrottleDisarmedTrapEnterprise_Type()
)
sm6kFilterThrottleDisarmedTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleDisarmedTrapEnterprise.setStatus("mandatory")
_Sm6kFilterThrottleDisarmedSpecificTrap_Type = Integer32
_Sm6kFilterThrottleDisarmedSpecificTrap_Object = MibTableColumn
sm6kFilterThrottleDisarmedSpecificTrap = _Sm6kFilterThrottleDisarmedSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 32),
    _Sm6kFilterThrottleDisarmedSpecificTrap_Type()
)
sm6kFilterThrottleDisarmedSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kFilterThrottleDisarmedSpecificTrap.setStatus("mandatory")


class _Sm6kFilterThrottleState_Type(Integer32):
    """Custom type sm6kFilterThrottleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("armed", 2),
          ("disarmed", 1))
    )


_Sm6kFilterThrottleState_Type.__name__ = "Integer32"
_Sm6kFilterThrottleState_Object = MibTableColumn
sm6kFilterThrottleState = _Sm6kFilterThrottleState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 33),
    _Sm6kFilterThrottleState_Type()
)
sm6kFilterThrottleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kFilterThrottleState.setStatus("mandatory")
_Sm6kFilterThrottleTimeStarted_Type = DisplayString
_Sm6kFilterThrottleTimeStarted_Object = MibTableColumn
sm6kFilterThrottleTimeStarted = _Sm6kFilterThrottleTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 34),
    _Sm6kFilterThrottleTimeStarted_Type()
)
sm6kFilterThrottleTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kFilterThrottleTimeStarted.setStatus("mandatory")
_Sm6kFilterThrottleTrapCount_Type = Integer32
_Sm6kFilterThrottleTrapCount_Object = MibTableColumn
sm6kFilterThrottleTrapCount = _Sm6kFilterThrottleTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 35),
    _Sm6kFilterThrottleTrapCount_Type()
)
sm6kFilterThrottleTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kFilterThrottleTrapCount.setStatus("mandatory")
_Sm6kAlias_ObjectIdentity = ObjectIdentity
sm6kAlias = _Sm6kAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8)
)
_Sm6kAliasTable_Object = MibTable
sm6kAliasTable = _Sm6kAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1)
)
if mibBuilder.loadTexts:
    sm6kAliasTable.setStatus("mandatory")
_Sm6kAliasEntry_Object = MibTableRow
sm6kAliasEntry = _Sm6kAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1)
)
sm6kAliasEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kAliasName"),
)
if mibBuilder.loadTexts:
    sm6kAliasEntry.setStatus("mandatory")


class _Sm6kAliasState_Type(Integer32):
    """Custom type sm6kAliasState based on Integer32"""
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


_Sm6kAliasState_Type.__name__ = "Integer32"
_Sm6kAliasState_Object = MibTableColumn
sm6kAliasState = _Sm6kAliasState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 1),
    _Sm6kAliasState_Type()
)
sm6kAliasState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAliasState.setStatus("mandatory")
_Sm6kAliasName_Type = DisplayString
_Sm6kAliasName_Object = MibTableColumn
sm6kAliasName = _Sm6kAliasName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 2),
    _Sm6kAliasName_Type()
)
sm6kAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAliasName.setStatus("mandatory")
_Sm6kAliasList_Type = DisplayString
_Sm6kAliasList_Object = MibTableColumn
sm6kAliasList = _Sm6kAliasList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 3),
    _Sm6kAliasList_Type()
)
sm6kAliasList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAliasList.setStatus("mandatory")
_Sm6kAliasResolvedList_Type = DisplayString
_Sm6kAliasResolvedList_Object = MibTableColumn
sm6kAliasResolvedList = _Sm6kAliasResolvedList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 4),
    _Sm6kAliasResolvedList_Type()
)
sm6kAliasResolvedList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm6kAliasResolvedList.setStatus("mandatory")
_Sm6kTrapDestination_ObjectIdentity = ObjectIdentity
sm6kTrapDestination = _Sm6kTrapDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9)
)
_Sm6kTrapDestinationTable_Object = MibTable
sm6kTrapDestinationTable = _Sm6kTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1)
)
if mibBuilder.loadTexts:
    sm6kTrapDestinationTable.setStatus("mandatory")
_Sm6kTrapDestinationEntry_Object = MibTableRow
sm6kTrapDestinationEntry = _Sm6kTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1)
)
sm6kTrapDestinationEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kTrapDestinationName"),
)
if mibBuilder.loadTexts:
    sm6kTrapDestinationEntry.setStatus("mandatory")


class _Sm6kTrapDestinationState_Type(Integer32):
    """Custom type sm6kTrapDestinationState based on Integer32"""
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


_Sm6kTrapDestinationState_Type.__name__ = "Integer32"
_Sm6kTrapDestinationState_Object = MibTableColumn
sm6kTrapDestinationState = _Sm6kTrapDestinationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 1),
    _Sm6kTrapDestinationState_Type()
)
sm6kTrapDestinationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kTrapDestinationState.setStatus("mandatory")
_Sm6kTrapDestinationName_Type = DisplayString
_Sm6kTrapDestinationName_Object = MibTableColumn
sm6kTrapDestinationName = _Sm6kTrapDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 2),
    _Sm6kTrapDestinationName_Type()
)
sm6kTrapDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kTrapDestinationName.setStatus("mandatory")
_Sm6kTrapDestinationHost_Type = DisplayString
_Sm6kTrapDestinationHost_Object = MibTableColumn
sm6kTrapDestinationHost = _Sm6kTrapDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 3),
    _Sm6kTrapDestinationHost_Type()
)
sm6kTrapDestinationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kTrapDestinationHost.setStatus("mandatory")
_Sm6kTrapDestinationMask_Type = Integer32
_Sm6kTrapDestinationMask_Object = MibTableColumn
sm6kTrapDestinationMask = _Sm6kTrapDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 4),
    _Sm6kTrapDestinationMask_Type()
)
sm6kTrapDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kTrapDestinationMask.setStatus("mandatory")
_Sm6kAdministration_ObjectIdentity = ObjectIdentity
sm6kAdministration = _Sm6kAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10)
)
_Sm6kAdministrationTable_Object = MibTable
sm6kAdministrationTable = _Sm6kAdministrationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1)
)
if mibBuilder.loadTexts:
    sm6kAdministrationTable.setStatus("mandatory")
_Sm6kAdministrationEntry_Object = MibTableRow
sm6kAdministrationEntry = _Sm6kAdministrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1)
)
sm6kAdministrationEntry.setIndexNames(
    (0, "SYSMON6K-MIB", "sm6kAdministrationFieldName"),
)
if mibBuilder.loadTexts:
    sm6kAdministrationEntry.setStatus("mandatory")


class _Sm6kAdministrationFieldState_Type(Integer32):
    """Custom type sm6kAdministrationFieldState based on Integer32"""
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


_Sm6kAdministrationFieldState_Type.__name__ = "Integer32"
_Sm6kAdministrationFieldState_Object = MibTableColumn
sm6kAdministrationFieldState = _Sm6kAdministrationFieldState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 1),
    _Sm6kAdministrationFieldState_Type()
)
sm6kAdministrationFieldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAdministrationFieldState.setStatus("mandatory")
_Sm6kAdministrationFieldName_Type = DisplayString
_Sm6kAdministrationFieldName_Object = MibTableColumn
sm6kAdministrationFieldName = _Sm6kAdministrationFieldName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 2),
    _Sm6kAdministrationFieldName_Type()
)
sm6kAdministrationFieldName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAdministrationFieldName.setStatus("mandatory")
_Sm6kAdministrationFieldOwner_Type = DisplayString
_Sm6kAdministrationFieldOwner_Object = MibTableColumn
sm6kAdministrationFieldOwner = _Sm6kAdministrationFieldOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 3),
    _Sm6kAdministrationFieldOwner_Type()
)
sm6kAdministrationFieldOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAdministrationFieldOwner.setStatus("mandatory")
_Sm6kAdministrationFieldDescription_Type = DisplayString
_Sm6kAdministrationFieldDescription_Object = MibTableColumn
sm6kAdministrationFieldDescription = _Sm6kAdministrationFieldDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 4),
    _Sm6kAdministrationFieldDescription_Type()
)
sm6kAdministrationFieldDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAdministrationFieldDescription.setStatus("mandatory")
_Sm6kAdministrationFieldValue_Type = DisplayString
_Sm6kAdministrationFieldValue_Object = MibTableColumn
sm6kAdministrationFieldValue = _Sm6kAdministrationFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 5),
    _Sm6kAdministrationFieldValue_Type()
)
sm6kAdministrationFieldValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm6kAdministrationFieldValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSMON6K-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "systemsMonitor6000": systemsMonitor6000,
       "sm6kProgramInformation": sm6kProgramInformation,
       "sm6kProgramData": sm6kProgramData,
       "sm6kProgramDescription": sm6kProgramDescription,
       "sm6kProgramName": sm6kProgramName,
       "sm6kProgramNumber": sm6kProgramNumber,
       "sm6kProgramVersion": sm6kProgramVersion,
       "sm6kProgramCompilationDate": sm6kProgramCompilationDate,
       "sm6kProgramUpTime": sm6kProgramUpTime,
       "sm6kProgramContact": sm6kProgramContact,
       "sm6kProgramControl": sm6kProgramControl,
       "sm6kProgramControlLocalConfigurationFile": sm6kProgramControlLocalConfigurationFile,
       "sm6kProgramControlReInitializeMonitor": sm6kProgramControlReInitializeMonitor,
       "sm6kProgramControlNonForkCacheTime": sm6kProgramControlNonForkCacheTime,
       "sm6kProgramControlForkCacheTime": sm6kProgramControlForkCacheTime,
       "sm6kProgramControlPercentMultiplier": sm6kProgramControlPercentMultiplier,
       "sm6kProgramControlPollTime": sm6kProgramControlPollTime,
       "sm6kProgramControlFlags": sm6kProgramControlFlags,
       "sm6kProgramRetryCount": sm6kProgramRetryCount,
       "sm6kProgramTimeout": sm6kProgramTimeout,
       "sm6kProgramLog": sm6kProgramLog,
       "sm6kProgramLogFileName": sm6kProgramLogFileName,
       "sm6kProgramLogFileSize": sm6kProgramLogFileSize,
       "sm6kProgramLogMaxFileSize": sm6kProgramLogMaxFileSize,
       "sm6kProgramLogNumFiles": sm6kProgramLogNumFiles,
       "sm6kProgramLogFileBehavior": sm6kProgramLogFileBehavior,
       "sm6kProgramLogMask": sm6kProgramLogMask,
       "sm6kProgramDataCollection": sm6kProgramDataCollection,
       "sm6kProgramDataCollectionFileName": sm6kProgramDataCollectionFileName,
       "sm6kProgramDataCollectionFileSize": sm6kProgramDataCollectionFileSize,
       "sm6kProgramDataCollectionMaxFileSize": sm6kProgramDataCollectionMaxFileSize,
       "sm6kProgramDataCollectionNumFiles": sm6kProgramDataCollectionNumFiles,
       "sm6kProgramDataCollectionFileBehavior": sm6kProgramDataCollectionFileBehavior,
       "sm6kProgramSetableTestObjects": sm6kProgramSetableTestObjects,
       "sm6kProgramControlSetableInteger": sm6kProgramControlSetableInteger,
       "sm6kProgramControlSetableCounter": sm6kProgramControlSetableCounter,
       "sm6kProgramControlSetableGauge": sm6kProgramControlSetableGauge,
       "sm6kProgramControlSetableIpAddress": sm6kProgramControlSetableIpAddress,
       "sm6kProgramControlSetableTimeTicks": sm6kProgramControlSetableTimeTicks,
       "sm6kProgramControlSetableOctetString": sm6kProgramControlSetableOctetString,
       "sm6kResourceUsage": sm6kResourceUsage,
       "sm6kResourceUsageTable": sm6kResourceUsageTable,
       "sm6kResourceUsageEntry": sm6kResourceUsageEntry,
       "sm6kResourceUsageName": sm6kResourceUsageName,
       "sm6kResourceUsageUserTime": sm6kResourceUsageUserTime,
       "sm6kResourceUsageSystemTime": sm6kResourceUsageSystemTime,
       "sm6kResourceUsageTotalTime": sm6kResourceUsageTotalTime,
       "sm6kResourceUsageMaxrss": sm6kResourceUsageMaxrss,
       "sm6kResourceUsageIxrss": sm6kResourceUsageIxrss,
       "sm6kResourceUsageIdrss": sm6kResourceUsageIdrss,
       "sm6kResourceUsageIsrss": sm6kResourceUsageIsrss,
       "sm6kResourceUsageMinflt": sm6kResourceUsageMinflt,
       "sm6kResourceUsageMajflt": sm6kResourceUsageMajflt,
       "sm6kResourceUsageNSwap": sm6kResourceUsageNSwap,
       "sm6kResourceUsageInBlock": sm6kResourceUsageInBlock,
       "sm6kResourceUsageOutBlock": sm6kResourceUsageOutBlock,
       "sm6kResourceUsageMsgsnd": sm6kResourceUsageMsgsnd,
       "sm6kResourceUsageMsgrcv": sm6kResourceUsageMsgrcv,
       "sm6kResourceUsageNSignals": sm6kResourceUsageNSignals,
       "sm6kResourceUsageVcsw": sm6kResourceUsageVcsw,
       "sm6kResourceUsageIcsw": sm6kResourceUsageIcsw,
       "sm6kProgramMessages": sm6kProgramMessages,
       "sm6kProgramMessagesTable": sm6kProgramMessagesTable,
       "sm6kProgramMessagesEntry": sm6kProgramMessagesEntry,
       "sm6kProgramMessagesRowNumber": sm6kProgramMessagesRowNumber,
       "sm6kProgramMessagesTime": sm6kProgramMessagesTime,
       "sm6kProgramMessagesText": sm6kProgramMessagesText,
       "sm6kProgramMessagesTimeStamp": sm6kProgramMessagesTimeStamp,
       "sm6kSystemInformation": sm6kSystemInformation,
       "sm6kSystemDescription": sm6kSystemDescription,
       "sm6kSystemNodeName": sm6kSystemNodeName,
       "sm6kSystemSysName": sm6kSystemSysName,
       "sm6kSystemVersion": sm6kSystemVersion,
       "sm6kSystemRelease": sm6kSystemRelease,
       "sm6kSystemMachine": sm6kSystemMachine,
       "sm6kSystemConfiguration": sm6kSystemConfiguration,
       "sm6kSystemBufferPoolMark": sm6kSystemBufferPoolMark,
       "sm6kSystemMaxMbufs": sm6kSystemMaxMbufs,
       "sm6kSystemMaxUserProcesses": sm6kSystemMaxUserProcesses,
       "sm6kSystemMaxSystemProcesses": sm6kSystemMaxSystemProcesses,
       "sm6kSystemRecordLockTableSize": sm6kSystemRecordLockTableSize,
       "sm6kSystemOpenFileTableSize": sm6kSystemOpenFileTableSize,
       "sm6kSystemCBlockArraySize": sm6kSystemCBlockArraySize,
       "sm6kSystemDiskIOHistory": sm6kSystemDiskIOHistory,
       "sm6kSystemAutomaticBootAfterHalt": sm6kSystemAutomaticBootAfterHalt,
       "sm6kSystemMemScrub": sm6kSystemMemScrub,
       "sm6kSystemLeastPriv": sm6kSystemLeastPriv,
       "sm6kSystemMaxPout": sm6kSystemMaxPout,
       "sm6kSystemMinPout": sm6kSystemMinPout,
       "sm6kSystemPageSize": sm6kSystemPageSize,
       "sm6kSystemProcessMaxOpenFiles": sm6kSystemProcessMaxOpenFiles,
       "sm6kSystemProcessMaxOpenStreams": sm6kSystemProcessMaxOpenStreams,
       "sm6kSystemProcessDescriptorTableSize": sm6kSystemProcessDescriptorTableSize,
       "sm6kSystemDevice": sm6kSystemDevice,
       "sm6kSystemDeviceList": sm6kSystemDeviceList,
       "sm6kSystemDeviceListInstalled": sm6kSystemDeviceListInstalled,
       "sm6kSystemDeviceListTable": sm6kSystemDeviceListTable,
       "sm6kSystemDeviceListEntry": sm6kSystemDeviceListEntry,
       "sm6kSystemDeviceListName": sm6kSystemDeviceListName,
       "sm6kSystemDeviceListDescription": sm6kSystemDeviceListDescription,
       "sm6kSystemDeviceListLocation": sm6kSystemDeviceListLocation,
       "sm6kSystemDeviceListVPD": sm6kSystemDeviceListVPD,
       "sm6kSystemDeviceListAttributes": sm6kSystemDeviceListAttributes,
       "sm6kSystemDeviceListDiagnostics": sm6kSystemDeviceListDiagnostics,
       "sm6kSystemDeviceTokenRing": sm6kSystemDeviceTokenRing,
       "sm6kSystemDeviceTokenRingInstalled": sm6kSystemDeviceTokenRingInstalled,
       "sm6kSystemDeviceTokenRingTable": sm6kSystemDeviceTokenRingTable,
       "sm6kSystemDeviceTokenRingEntry": sm6kSystemDeviceTokenRingEntry,
       "sm6kSystemDeviceTokenRingNumber": sm6kSystemDeviceTokenRingNumber,
       "sm6kSystemDeviceTokenRingHardwareAddress": sm6kSystemDeviceTokenRingHardwareAddress,
       "sm6kSystemDeviceTokenRingCurrentAddress": sm6kSystemDeviceTokenRingCurrentAddress,
       "sm6kSystemDeviceTokenRingReceiveDataOffset": sm6kSystemDeviceTokenRingReceiveDataOffset,
       "sm6kSystemDeviceTokenRingBroadwrap": sm6kSystemDeviceTokenRingBroadwrap,
       "sm6kSystemDeviceTokenRingTxByteMcnt": sm6kSystemDeviceTokenRingTxByteMcnt,
       "sm6kSystemDeviceTokenRingTxByteLcnt": sm6kSystemDeviceTokenRingTxByteLcnt,
       "sm6kSystemDeviceTokenRingRxByteMcnt": sm6kSystemDeviceTokenRingRxByteMcnt,
       "sm6kSystemDeviceTokenRingRxByteLcnt": sm6kSystemDeviceTokenRingRxByteLcnt,
       "sm6kSystemDeviceTokenRingTxFrameMcnt": sm6kSystemDeviceTokenRingTxFrameMcnt,
       "sm6kSystemDeviceTokenRingTxFrameLcnt": sm6kSystemDeviceTokenRingTxFrameLcnt,
       "sm6kSystemDeviceTokenRingRxFrameMcnt": sm6kSystemDeviceTokenRingRxFrameMcnt,
       "sm6kSystemDeviceTokenRingRxFrameLcnt": sm6kSystemDeviceTokenRingRxFrameLcnt,
       "sm6kSystemDeviceTokenRingTxErrCnt": sm6kSystemDeviceTokenRingTxErrCnt,
       "sm6kSystemDeviceTokenRingRxErrCnt": sm6kSystemDeviceTokenRingRxErrCnt,
       "sm6kSystemDeviceTokenRingNidTblHigh": sm6kSystemDeviceTokenRingNidTblHigh,
       "sm6kSystemDeviceTokenRingTxQueHigh": sm6kSystemDeviceTokenRingTxQueHigh,
       "sm6kSystemDeviceTokenRingRxQueHigh": sm6kSystemDeviceTokenRingRxQueHigh,
       "sm6kSystemDeviceTokenRingStaQueHigh": sm6kSystemDeviceTokenRingStaQueHigh,
       "sm6kSystemDeviceTokenRingIntrLost": sm6kSystemDeviceTokenRingIntrLost,
       "sm6kSystemDeviceTokenRingWdtLost": sm6kSystemDeviceTokenRingWdtLost,
       "sm6kSystemDeviceTokenRingTimoLost": sm6kSystemDeviceTokenRingTimoLost,
       "sm6kSystemDeviceTokenRingStaQueOverflow": sm6kSystemDeviceTokenRingStaQueOverflow,
       "sm6kSystemDeviceTokenRingRxQueOverflow": sm6kSystemDeviceTokenRingRxQueOverflow,
       "sm6kSystemDeviceTokenRingRxQueNoMbuf": sm6kSystemDeviceTokenRingRxQueNoMbuf,
       "sm6kSystemDeviceTokenRingRxQueNoMbufExt": sm6kSystemDeviceTokenRingRxQueNoMbufExt,
       "sm6kSystemDeviceTokenRingTxIntrCnt": sm6kSystemDeviceTokenRingTxIntrCnt,
       "sm6kSystemDeviceTokenRingRxIntrCnt": sm6kSystemDeviceTokenRingRxIntrCnt,
       "sm6kSystemDeviceTokenRingPktRejCnt": sm6kSystemDeviceTokenRingPktRejCnt,
       "sm6kSystemDeviceTokenRingPktAccCnt": sm6kSystemDeviceTokenRingPktAccCnt,
       "sm6kSystemDeviceTokenRingPktTxCnt": sm6kSystemDeviceTokenRingPktTxCnt,
       "sm6kSystemDeviceTokenRingOvfloPktCnt": sm6kSystemDeviceTokenRingOvfloPktCnt,
       "sm6kSystemDeviceTokenRingPktTxErrCnt": sm6kSystemDeviceTokenRingPktTxErrCnt,
       "sm6kSystemDeviceTokenRingSpeed": sm6kSystemDeviceTokenRingSpeed,
       "sm6kSystemDeviceTokenRingVPD": sm6kSystemDeviceTokenRingVPD,
       "sm6kSystemDeviceTokenRingAdapPhysAddr": sm6kSystemDeviceTokenRingAdapPhysAddr,
       "sm6kSystemDeviceTokenRingUpstreamNodeAddr": sm6kSystemDeviceTokenRingUpstreamNodeAddr,
       "sm6kSystemDeviceTokenRingUpstreamPhysAddr": sm6kSystemDeviceTokenRingUpstreamPhysAddr,
       "sm6kSystemDeviceTokenRingLastPollAddr": sm6kSystemDeviceTokenRingLastPollAddr,
       "sm6kSystemDeviceTokenRingAuthorEnv": sm6kSystemDeviceTokenRingAuthorEnv,
       "sm6kSystemDeviceTokenRingTxAccessPriority": sm6kSystemDeviceTokenRingTxAccessPriority,
       "sm6kSystemDeviceTokenRingSrcClassAuthor": sm6kSystemDeviceTokenRingSrcClassAuthor,
       "sm6kSystemDeviceTokenRingLastAttenCode": sm6kSystemDeviceTokenRingLastAttenCode,
       "sm6kSystemDeviceTokenRingLastSrcAddr": sm6kSystemDeviceTokenRingLastSrcAddr,
       "sm6kSystemDeviceTokenRingLastBeaconType": sm6kSystemDeviceTokenRingLastBeaconType,
       "sm6kSystemDeviceTokenRingLastMajorVector": sm6kSystemDeviceTokenRingLastMajorVector,
       "sm6kSystemDeviceTokenRingRingStatus": sm6kSystemDeviceTokenRingRingStatus,
       "sm6kSystemDeviceTokenRingSoftErrorTimerVal": sm6kSystemDeviceTokenRingSoftErrorTimerVal,
       "sm6kSystemDeviceTokenRingFrontEndTimerVal": sm6kSystemDeviceTokenRingFrontEndTimerVal,
       "sm6kSystemDeviceTokenRingMonitorErrorCode": sm6kSystemDeviceTokenRingMonitorErrorCode,
       "sm6kSystemDeviceTokenRingBeaconTxType": sm6kSystemDeviceTokenRingBeaconTxType,
       "sm6kSystemDeviceTokenRingBeaconRxType": sm6kSystemDeviceTokenRingBeaconRxType,
       "sm6kSystemDeviceTokenRingFrameCorrSave": sm6kSystemDeviceTokenRingFrameCorrSave,
       "sm6kSystemDeviceTokenRingBeaconStationNAUN": sm6kSystemDeviceTokenRingBeaconStationNAUN,
       "sm6kSystemDeviceTokenRingBeaconStationPhysAddr": sm6kSystemDeviceTokenRingBeaconStationPhysAddr,
       "sm6kSystemDeviceTokenRingClear": sm6kSystemDeviceTokenRingClear,
       "sm6kSystemDeviceEthernet": sm6kSystemDeviceEthernet,
       "sm6kSystemDeviceEthernetInstalled": sm6kSystemDeviceEthernetInstalled,
       "sm6kSystemDeviceEthernetTable": sm6kSystemDeviceEthernetTable,
       "sm6kSystemDeviceEthernetEntry": sm6kSystemDeviceEthernetEntry,
       "sm6kSystemDeviceEthernetNumber": sm6kSystemDeviceEthernetNumber,
       "sm6kSystemDeviceEthernetHardwareAddress": sm6kSystemDeviceEthernetHardwareAddress,
       "sm6kSystemDeviceEthernetCurrentAddress": sm6kSystemDeviceEthernetCurrentAddress,
       "sm6kSystemDeviceEthernetReceiveDataOffset": sm6kSystemDeviceEthernetReceiveDataOffset,
       "sm6kSystemDeviceEthernetBroadwrap": sm6kSystemDeviceEthernetBroadwrap,
       "sm6kSystemDeviceEthernetTxByteMcnt": sm6kSystemDeviceEthernetTxByteMcnt,
       "sm6kSystemDeviceEthernetTxByteLcnt": sm6kSystemDeviceEthernetTxByteLcnt,
       "sm6kSystemDeviceEthernetRxByteMcnt": sm6kSystemDeviceEthernetRxByteMcnt,
       "sm6kSystemDeviceEthernetRxByteLcnt": sm6kSystemDeviceEthernetRxByteLcnt,
       "sm6kSystemDeviceEthernetTxFrameMcnt": sm6kSystemDeviceEthernetTxFrameMcnt,
       "sm6kSystemDeviceEthernetTxFrameLcnt": sm6kSystemDeviceEthernetTxFrameLcnt,
       "sm6kSystemDeviceEthernetRxFrameMcnt": sm6kSystemDeviceEthernetRxFrameMcnt,
       "sm6kSystemDeviceEthernetRxFrameLcnt": sm6kSystemDeviceEthernetRxFrameLcnt,
       "sm6kSystemDeviceEthernetTxErrCnt": sm6kSystemDeviceEthernetTxErrCnt,
       "sm6kSystemDeviceEthernetRxErrCnt": sm6kSystemDeviceEthernetRxErrCnt,
       "sm6kSystemDeviceEthernetNidTblHigh": sm6kSystemDeviceEthernetNidTblHigh,
       "sm6kSystemDeviceEthernetTxQueHigh": sm6kSystemDeviceEthernetTxQueHigh,
       "sm6kSystemDeviceEthernetRxQueHigh": sm6kSystemDeviceEthernetRxQueHigh,
       "sm6kSystemDeviceEthernetStaQueHigh": sm6kSystemDeviceEthernetStaQueHigh,
       "sm6kSystemDeviceEthernetIntrLost": sm6kSystemDeviceEthernetIntrLost,
       "sm6kSystemDeviceEthernetWdtLost": sm6kSystemDeviceEthernetWdtLost,
       "sm6kSystemDeviceEthernetTimoLost": sm6kSystemDeviceEthernetTimoLost,
       "sm6kSystemDeviceEthernetStaQueOverflow": sm6kSystemDeviceEthernetStaQueOverflow,
       "sm6kSystemDeviceEthernetRxQueOverflow": sm6kSystemDeviceEthernetRxQueOverflow,
       "sm6kSystemDeviceEthernetRxQueNoMbuf": sm6kSystemDeviceEthernetRxQueNoMbuf,
       "sm6kSystemDeviceEthernetRxQueNoMbufExt": sm6kSystemDeviceEthernetRxQueNoMbufExt,
       "sm6kSystemDeviceEthernetTxIntrCnt": sm6kSystemDeviceEthernetTxIntrCnt,
       "sm6kSystemDeviceEthernetRxIntrCnt": sm6kSystemDeviceEthernetRxIntrCnt,
       "sm6kSystemDeviceEthernetCRCErr": sm6kSystemDeviceEthernetCRCErr,
       "sm6kSystemDeviceEthernetAlignErr": sm6kSystemDeviceEthernetAlignErr,
       "sm6kSystemDeviceEthernetOverrun": sm6kSystemDeviceEthernetOverrun,
       "sm6kSystemDeviceEthernetTooShort": sm6kSystemDeviceEthernetTooShort,
       "sm6kSystemDeviceEthernetTooLong": sm6kSystemDeviceEthernetTooLong,
       "sm6kSystemDeviceEthernetNoResources": sm6kSystemDeviceEthernetNoResources,
       "sm6kSystemDeviceEthernetPktDiscard": sm6kSystemDeviceEthernetPktDiscard,
       "sm6kSystemDeviceEthernetMaxCollision": sm6kSystemDeviceEthernetMaxCollision,
       "sm6kSystemDeviceEthernetLateCollision": sm6kSystemDeviceEthernetLateCollision,
       "sm6kSystemDeviceEthernetCarrierLost": sm6kSystemDeviceEthernetCarrierLost,
       "sm6kSystemDeviceEthernetUnderrun": sm6kSystemDeviceEthernetUnderrun,
       "sm6kSystemDeviceEthernetCTSLost": sm6kSystemDeviceEthernetCTSLost,
       "sm6kSystemDeviceEthernetTxTimeouts": sm6kSystemDeviceEthernetTxTimeouts,
       "sm6kSystemDeviceEthernetParErrCnt": sm6kSystemDeviceEthernetParErrCnt,
       "sm6kSystemDeviceEthernetDiagOverflow": sm6kSystemDeviceEthernetDiagOverflow,
       "sm6kSystemDeviceEthernetExecOverflow": sm6kSystemDeviceEthernetExecOverflow,
       "sm6kSystemDeviceEthernetExecCmdErrors": sm6kSystemDeviceEthernetExecCmdErrors,
       "sm6kSystemDeviceEthernetHostRecEol": sm6kSystemDeviceEthernetHostRecEol,
       "sm6kSystemDeviceEthernetAdptRecEol": sm6kSystemDeviceEthernetAdptRecEol,
       "sm6kSystemDeviceEthernetHostRecPkt": sm6kSystemDeviceEthernetHostRecPkt,
       "sm6kSystemDeviceEthernetAdptRecPkt": sm6kSystemDeviceEthernetAdptRecPkt,
       "sm6kSystemDeviceEthernetStartRxCmd": sm6kSystemDeviceEthernetStartRxCmd,
       "sm6kSystemDeviceEthernetStartRxDmaTimeouts": sm6kSystemDeviceEthernetStartRxDmaTimeouts,
       "sm6kSystemDeviceEthernetVPD": sm6kSystemDeviceEthernetVPD,
       "sm6kSystemDeviceEthernetClear": sm6kSystemDeviceEthernetClear,
       "sm6kSystemDeviceX25": sm6kSystemDeviceX25,
       "sm6kSystemDeviceX25Installed": sm6kSystemDeviceX25Installed,
       "sm6kSystemDeviceX25Table": sm6kSystemDeviceX25Table,
       "sm6kSystemDeviceX25Entry": sm6kSystemDeviceX25Entry,
       "sm6kSystemDeviceX25Number": sm6kSystemDeviceX25Number,
       "sm6kSystemDeviceX25Address": sm6kSystemDeviceX25Address,
       "sm6kSystemDeviceX25SupportLevel": sm6kSystemDeviceX25SupportLevel,
       "sm6kSystemDeviceX25SupportedFacilities": sm6kSystemDeviceX25SupportedFacilities,
       "sm6kSystemDeviceX25NetworkId": sm6kSystemDeviceX25NetworkId,
       "sm6kSystemDeviceX25MaxTxPacketSize": sm6kSystemDeviceX25MaxTxPacketSize,
       "sm6kSystemDeviceX25MaxRxPacketSize": sm6kSystemDeviceX25MaxRxPacketSize,
       "sm6kSystemDeviceX25DefaultSvcTxPacketSize": sm6kSystemDeviceX25DefaultSvcTxPacketSize,
       "sm6kSystemDeviceX25DefaultSvcRxPacketSize": sm6kSystemDeviceX25DefaultSvcRxPacketSize,
       "sm6kSystemDeviceX25ReceiveDataTransferOffset": sm6kSystemDeviceX25ReceiveDataTransferOffset,
       "sm6kSystemDeviceX25MemoryWindowSize": sm6kSystemDeviceX25MemoryWindowSize,
       "sm6kSystemDeviceX25TxByteMcnt": sm6kSystemDeviceX25TxByteMcnt,
       "sm6kSystemDeviceX25TxByteLcnt": sm6kSystemDeviceX25TxByteLcnt,
       "sm6kSystemDeviceX25RxByteMcnt": sm6kSystemDeviceX25RxByteMcnt,
       "sm6kSystemDeviceX25RxByteLcnt": sm6kSystemDeviceX25RxByteLcnt,
       "sm6kSystemDeviceX25TxFrameMcnt": sm6kSystemDeviceX25TxFrameMcnt,
       "sm6kSystemDeviceX25TxFrameLcnt": sm6kSystemDeviceX25TxFrameLcnt,
       "sm6kSystemDeviceX25RxFrameMcnt": sm6kSystemDeviceX25RxFrameMcnt,
       "sm6kSystemDeviceX25RxFrameLcnt": sm6kSystemDeviceX25RxFrameLcnt,
       "sm6kSystemDeviceX25TxErrCnt": sm6kSystemDeviceX25TxErrCnt,
       "sm6kSystemDeviceX25RxErrCnt": sm6kSystemDeviceX25RxErrCnt,
       "sm6kSystemDeviceX25NidTblHigh": sm6kSystemDeviceX25NidTblHigh,
       "sm6kSystemDeviceX25TxQueHigh": sm6kSystemDeviceX25TxQueHigh,
       "sm6kSystemDeviceX25RxQueHigh": sm6kSystemDeviceX25RxQueHigh,
       "sm6kSystemDeviceX25StaQueHigh": sm6kSystemDeviceX25StaQueHigh,
       "sm6kSystemDeviceX25IgnoredFTx": sm6kSystemDeviceX25IgnoredFTx,
       "sm6kSystemDeviceX25RrFTx": sm6kSystemDeviceX25RrFTx,
       "sm6kSystemDeviceX25RnrFTx": sm6kSystemDeviceX25RnrFTx,
       "sm6kSystemDeviceX25RejFTx": sm6kSystemDeviceX25RejFTx,
       "sm6kSystemDeviceX25InfoFTx": sm6kSystemDeviceX25InfoFTx,
       "sm6kSystemDeviceX25SabmFTx": sm6kSystemDeviceX25SabmFTx,
       "sm6kSystemDeviceX25SarmDmFTx": sm6kSystemDeviceX25SarmDmFTx,
       "sm6kSystemDeviceX25DiscFTx": sm6kSystemDeviceX25DiscFTx,
       "sm6kSystemDeviceX25UaFTx": sm6kSystemDeviceX25UaFTx,
       "sm6kSystemDeviceX25FrmrFTx": sm6kSystemDeviceX25FrmrFTx,
       "sm6kSystemDeviceX25BadNrFTx": sm6kSystemDeviceX25BadNrFTx,
       "sm6kSystemDeviceX25UnknownFTx": sm6kSystemDeviceX25UnknownFTx,
       "sm6kSystemDeviceX25XidFTx": sm6kSystemDeviceX25XidFTx,
       "sm6kSystemDeviceX25BadLengthFTx": sm6kSystemDeviceX25BadLengthFTx,
       "sm6kSystemDeviceX25T1Expirations": sm6kSystemDeviceX25T1Expirations,
       "sm6kSystemDeviceX25Lvl2Connects": sm6kSystemDeviceX25Lvl2Connects,
       "sm6kSystemDeviceX25Lvl2Disconnects": sm6kSystemDeviceX25Lvl2Disconnects,
       "sm6kSystemDeviceX25CarrierLoss": sm6kSystemDeviceX25CarrierLoss,
       "sm6kSystemDeviceX25ConnectTime": sm6kSystemDeviceX25ConnectTime,
       "sm6kSystemDeviceX25T4Expirations": sm6kSystemDeviceX25T4Expirations,
       "sm6kSystemDeviceX25T4N2Times": sm6kSystemDeviceX25T4N2Times,
       "sm6kSystemDeviceX25IgnoredFRx": sm6kSystemDeviceX25IgnoredFRx,
       "sm6kSystemDeviceX25RrFRx": sm6kSystemDeviceX25RrFRx,
       "sm6kSystemDeviceX25RnrFRx": sm6kSystemDeviceX25RnrFRx,
       "sm6kSystemDeviceX25RejFRx": sm6kSystemDeviceX25RejFRx,
       "sm6kSystemDeviceX25InfoFRx": sm6kSystemDeviceX25InfoFRx,
       "sm6kSystemDeviceX25SabmFRx": sm6kSystemDeviceX25SabmFRx,
       "sm6kSystemDeviceX25SarmDmFRx": sm6kSystemDeviceX25SarmDmFRx,
       "sm6kSystemDeviceX25DiscFRx": sm6kSystemDeviceX25DiscFRx,
       "sm6kSystemDeviceX25UaFRx": sm6kSystemDeviceX25UaFRx,
       "sm6kSystemDeviceX25FrmrFRx": sm6kSystemDeviceX25FrmrFRx,
       "sm6kSystemDeviceX25BadNrFRx": sm6kSystemDeviceX25BadNrFRx,
       "sm6kSystemDeviceX25UnknownFRx": sm6kSystemDeviceX25UnknownFRx,
       "sm6kSystemDeviceX25XidFRx": sm6kSystemDeviceX25XidFRx,
       "sm6kSystemDeviceX25BadLengthFRx": sm6kSystemDeviceX25BadLengthFRx,
       "sm6kSystemDeviceX25DataPTx": sm6kSystemDeviceX25DataPTx,
       "sm6kSystemDeviceX25RrPTx": sm6kSystemDeviceX25RrPTx,
       "sm6kSystemDeviceX25RnrPTx": sm6kSystemDeviceX25RnrPTx,
       "sm6kSystemDeviceX25InterruptPTx": sm6kSystemDeviceX25InterruptPTx,
       "sm6kSystemDeviceX25InterruptConfirmPTx": sm6kSystemDeviceX25InterruptConfirmPTx,
       "sm6kSystemDeviceX25CallRequestPTx": sm6kSystemDeviceX25CallRequestPTx,
       "sm6kSystemDeviceX25CallAcceptPTx": sm6kSystemDeviceX25CallAcceptPTx,
       "sm6kSystemDeviceX25ClearRequestPTx": sm6kSystemDeviceX25ClearRequestPTx,
       "sm6kSystemDeviceX25ClearConfirmPTx": sm6kSystemDeviceX25ClearConfirmPTx,
       "sm6kSystemDeviceX25ResetRequestPTx": sm6kSystemDeviceX25ResetRequestPTx,
       "sm6kSystemDeviceX25ResetConfirmPTx": sm6kSystemDeviceX25ResetConfirmPTx,
       "sm6kSystemDeviceX25DiagnosticPTx": sm6kSystemDeviceX25DiagnosticPTx,
       "sm6kSystemDeviceX25RegistrationPTx": sm6kSystemDeviceX25RegistrationPTx,
       "sm6kSystemDeviceX25RegistrationConfirmPTx": sm6kSystemDeviceX25RegistrationConfirmPTx,
       "sm6kSystemDeviceX25RestartPTx": sm6kSystemDeviceX25RestartPTx,
       "sm6kSystemDeviceX25RestartConfirmPTx": sm6kSystemDeviceX25RestartConfirmPTx,
       "sm6kSystemDeviceX25ErrorPTx": sm6kSystemDeviceX25ErrorPTx,
       "sm6kSystemDeviceX25T20Expirations": sm6kSystemDeviceX25T20Expirations,
       "sm6kSystemDeviceX25T21Expirations": sm6kSystemDeviceX25T21Expirations,
       "sm6kSystemDeviceX25T22Expirations": sm6kSystemDeviceX25T22Expirations,
       "sm6kSystemDeviceX25T23Expirations": sm6kSystemDeviceX25T23Expirations,
       "sm6kSystemDeviceX25VcEstablishments": sm6kSystemDeviceX25VcEstablishments,
       "sm6kSystemDeviceX25T24Expirations": sm6kSystemDeviceX25T24Expirations,
       "sm6kSystemDeviceX25T25Expirations": sm6kSystemDeviceX25T25Expirations,
       "sm6kSystemDeviceX25T26Expirations": sm6kSystemDeviceX25T26Expirations,
       "sm6kSystemDeviceX25T28Expirations": sm6kSystemDeviceX25T28Expirations,
       "sm6kSystemDeviceX25DataPRx": sm6kSystemDeviceX25DataPRx,
       "sm6kSystemDeviceX25RrPRx": sm6kSystemDeviceX25RrPRx,
       "sm6kSystemDeviceX25RnrPRx": sm6kSystemDeviceX25RnrPRx,
       "sm6kSystemDeviceX25InterruptPRx": sm6kSystemDeviceX25InterruptPRx,
       "sm6kSystemDeviceX25InterruptConfirmPRx": sm6kSystemDeviceX25InterruptConfirmPRx,
       "sm6kSystemDeviceX25IncomingCallPRx": sm6kSystemDeviceX25IncomingCallPRx,
       "sm6kSystemDeviceX25CallConnectedPRx": sm6kSystemDeviceX25CallConnectedPRx,
       "sm6kSystemDeviceX25ClearIndicationPRx": sm6kSystemDeviceX25ClearIndicationPRx,
       "sm6kSystemDeviceX25ClearConfirmPRx": sm6kSystemDeviceX25ClearConfirmPRx,
       "sm6kSystemDeviceX25ResetIndicationPRx": sm6kSystemDeviceX25ResetIndicationPRx,
       "sm6kSystemDeviceX25ResetConfirmPRx": sm6kSystemDeviceX25ResetConfirmPRx,
       "sm6kSystemDeviceX25DiagnosticPRx": sm6kSystemDeviceX25DiagnosticPRx,
       "sm6kSystemDeviceX25RegistrationPRx": sm6kSystemDeviceX25RegistrationPRx,
       "sm6kSystemDeviceX25RegistrationConfirmPRx": sm6kSystemDeviceX25RegistrationConfirmPRx,
       "sm6kSystemDeviceX25RestartPRx": sm6kSystemDeviceX25RestartPRx,
       "sm6kSystemDeviceX25RestartConfirmPRx": sm6kSystemDeviceX25RestartConfirmPRx,
       "sm6kSystemDeviceX25TxUnknownSize": sm6kSystemDeviceX25TxUnknownSize,
       "sm6kSystemDeviceX25TxReserved1": sm6kSystemDeviceX25TxReserved1,
       "sm6kSystemDeviceX25TxReserved2": sm6kSystemDeviceX25TxReserved2,
       "sm6kSystemDeviceX25TxReserved3": sm6kSystemDeviceX25TxReserved3,
       "sm6kSystemDeviceX25Tx0x15": sm6kSystemDeviceX25Tx0x15,
       "sm6kSystemDeviceX25Tx16x31": sm6kSystemDeviceX25Tx16x31,
       "sm6kSystemDeviceX25Tx32x63": sm6kSystemDeviceX25Tx32x63,
       "sm6kSystemDeviceX25Tx64x127": sm6kSystemDeviceX25Tx64x127,
       "sm6kSystemDeviceX25Tx128x255": sm6kSystemDeviceX25Tx128x255,
       "sm6kSystemDeviceX25Tx256x511": sm6kSystemDeviceX25Tx256x511,
       "sm6kSystemDeviceX25Tx512x1023": sm6kSystemDeviceX25Tx512x1023,
       "sm6kSystemDeviceX25Tx1024x2047": sm6kSystemDeviceX25Tx1024x2047,
       "sm6kSystemDeviceX25Tx2048x4095": sm6kSystemDeviceX25Tx2048x4095,
       "sm6kSystemDeviceX25TxReserved13": sm6kSystemDeviceX25TxReserved13,
       "sm6kSystemDeviceX25TxReserved14": sm6kSystemDeviceX25TxReserved14,
       "sm6kSystemDeviceX25TxReserved15": sm6kSystemDeviceX25TxReserved15,
       "sm6kSystemDeviceX25TxTotalPackets": sm6kSystemDeviceX25TxTotalPackets,
       "sm6kSystemDeviceX25RxUnknownSize": sm6kSystemDeviceX25RxUnknownSize,
       "sm6kSystemDeviceX25RxReserved1": sm6kSystemDeviceX25RxReserved1,
       "sm6kSystemDeviceX25RxReserved2": sm6kSystemDeviceX25RxReserved2,
       "sm6kSystemDeviceX25RxReserved3": sm6kSystemDeviceX25RxReserved3,
       "sm6kSystemDeviceX25Rx0x15": sm6kSystemDeviceX25Rx0x15,
       "sm6kSystemDeviceX25Rx16x31": sm6kSystemDeviceX25Rx16x31,
       "sm6kSystemDeviceX25Rx32x63": sm6kSystemDeviceX25Rx32x63,
       "sm6kSystemDeviceX25Rx64x127": sm6kSystemDeviceX25Rx64x127,
       "sm6kSystemDeviceX25Rx128x255": sm6kSystemDeviceX25Rx128x255,
       "sm6kSystemDeviceX25Rx256x511": sm6kSystemDeviceX25Rx256x511,
       "sm6kSystemDeviceX25Rx512x1023": sm6kSystemDeviceX25Rx512x1023,
       "sm6kSystemDeviceX25Rx1024x2047": sm6kSystemDeviceX25Rx1024x2047,
       "sm6kSystemDeviceX25Rx2048x4095": sm6kSystemDeviceX25Rx2048x4095,
       "sm6kSystemDeviceX25RxReserved13": sm6kSystemDeviceX25RxReserved13,
       "sm6kSystemDeviceX25RxReserved14": sm6kSystemDeviceX25RxReserved14,
       "sm6kSystemDeviceX25RxReserved15": sm6kSystemDeviceX25RxReserved15,
       "sm6kSystemDeviceX25RxTotalPackets": sm6kSystemDeviceX25RxTotalPackets,
       "sm6kSystemDeviceX25Clear": sm6kSystemDeviceX25Clear,
       "sm6kSystemDeviceX25RouteCount": sm6kSystemDeviceX25RouteCount,
       "sm6kSystemDeviceX25RouteTable": sm6kSystemDeviceX25RouteTable,
       "sm6kSystemDeviceX25RouteEntry": sm6kSystemDeviceX25RouteEntry,
       "sm6kSystemDeviceX25RouteNumber": sm6kSystemDeviceX25RouteNumber,
       "sm6kSystemDeviceX25RouteEntryName": sm6kSystemDeviceX25RouteEntryName,
       "sm6kSystemDeviceX25RouteUserName": sm6kSystemDeviceX25RouteUserName,
       "sm6kSystemDeviceX25RoutePort": sm6kSystemDeviceX25RoutePort,
       "sm6kSystemDeviceX25RouteCallingAddress": sm6kSystemDeviceX25RouteCallingAddress,
       "sm6kSystemDeviceX25RouteCalledSubaddress": sm6kSystemDeviceX25RouteCalledSubaddress,
       "sm6kSystemDeviceX25RouteCallingAddressExt": sm6kSystemDeviceX25RouteCallingAddressExt,
       "sm6kSystemDeviceX25RouteCalledAddressExt": sm6kSystemDeviceX25RouteCalledAddressExt,
       "sm6kSystemDeviceX25RouteCalledUserData": sm6kSystemDeviceX25RouteCalledUserData,
       "sm6kSystemDeviceX25RoutePriority": sm6kSystemDeviceX25RoutePriority,
       "sm6kSystemDeviceX25RouteAction": sm6kSystemDeviceX25RouteAction,
       "sm6kSystemPagingInformation": sm6kSystemPagingInformation,
       "sm6kSystemFreePagingSpace": sm6kSystemFreePagingSpace,
       "sm6kSystemFreePagingSpaceUntilKill": sm6kSystemFreePagingSpaceUntilKill,
       "sm6kSystemFreePagingSpaceUntilKillPercent": sm6kSystemFreePagingSpaceUntilKillPercent,
       "sm6kSystemPagingSpace": sm6kSystemPagingSpace,
       "sm6kSystemPagingSpaceCount": sm6kSystemPagingSpaceCount,
       "sm6kSystemPagingSpaceTable": sm6kSystemPagingSpaceTable,
       "sm6kSystemPagingSpaceEntry": sm6kSystemPagingSpaceEntry,
       "sm6kSystemPagingSpaceName": sm6kSystemPagingSpaceName,
       "sm6kSystemPagingSpacePhysicalVolume": sm6kSystemPagingSpacePhysicalVolume,
       "sm6kSystemPagingSpaceVolumeGroup": sm6kSystemPagingSpaceVolumeGroup,
       "sm6kSystemPagingSpaceSize": sm6kSystemPagingSpaceSize,
       "sm6kSystemPagingSpacePercentUsed": sm6kSystemPagingSpacePercentUsed,
       "sm6kSystemPagingSpaceActive": sm6kSystemPagingSpaceActive,
       "sm6kSystemPagingSpaceAuto": sm6kSystemPagingSpaceAuto,
       "sm6kSystemPagingSpaceType": sm6kSystemPagingSpaceType,
       "sm6kSystemPagingStatistics": sm6kSystemPagingStatistics,
       "sm6kSystemPagingStatisticsPollingInterval": sm6kSystemPagingStatisticsPollingInterval,
       "sm6kSystemPagingStatisticsTable": sm6kSystemPagingStatisticsTable,
       "sm6kSystemPagingStatisticsEntry": sm6kSystemPagingStatisticsEntry,
       "sm6kSystemPagingStatisticsName": sm6kSystemPagingStatisticsName,
       "sm6kSystemPagingStatisticsIntervalStartTime": sm6kSystemPagingStatisticsIntervalStartTime,
       "sm6kSystemPagingStatisticsIntervalLength": sm6kSystemPagingStatisticsIntervalLength,
       "sm6kSystemPagingStatisticsPageFaults": sm6kSystemPagingStatisticsPageFaults,
       "sm6kSystemPagingStatisticsPageReclaims": sm6kSystemPagingStatisticsPageReclaims,
       "sm6kSystemPagingStatisticsPagesPagedIn": sm6kSystemPagingStatisticsPagesPagedIn,
       "sm6kSystemPagingStatisticsPagesPagedOut": sm6kSystemPagingStatisticsPagesPagedOut,
       "sm6kSystemPagingStatisticsPageInsFromPagingSpace": sm6kSystemPagingStatisticsPageInsFromPagingSpace,
       "sm6kSystemPagingStatisticsPageOutsFromPagingSpace": sm6kSystemPagingStatisticsPageOutsFromPagingSpace,
       "sm6kSystemPagingStatisticsStartIOs": sm6kSystemPagingStatisticsStartIOs,
       "sm6kSystemPagingStatisticsDoneIOs": sm6kSystemPagingStatisticsDoneIOs,
       "sm6kSystemPagingStatisticsPageScans": sm6kSystemPagingStatisticsPageScans,
       "sm6kSystemPagingStatisticsScanClockCycles": sm6kSystemPagingStatisticsScanClockCycles,
       "sm6kSystemPagingStatisticsPageSteals": sm6kSystemPagingStatisticsPageSteals,
       "sm6kSystemPagingStatisticsFreeFrameWaits": sm6kSystemPagingStatisticsFreeFrameWaits,
       "sm6kSystemPagingStatisticsExtendXPTWaits": sm6kSystemPagingStatisticsExtendXPTWaits,
       "sm6kSystemPagingStatisticsPendingIOWaits": sm6kSystemPagingStatisticsPendingIOWaits,
       "sm6kSystemPagingStatisticsPageFaultsMinimum": sm6kSystemPagingStatisticsPageFaultsMinimum,
       "sm6kSystemPagingStatisticsPageReclaimsMinimum": sm6kSystemPagingStatisticsPageReclaimsMinimum,
       "sm6kSystemPagingStatisticsPagesPagedInMinimum": sm6kSystemPagingStatisticsPagesPagedInMinimum,
       "sm6kSystemPagingStatisticsPagesPagedOutMinimum": sm6kSystemPagingStatisticsPagesPagedOutMinimum,
       "sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum": sm6kSystemPagingStatisticsPageInsFromPagingSpaceMinimum,
       "sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum": sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMinimum,
       "sm6kSystemPagingStatisticsStartIOsMinimum": sm6kSystemPagingStatisticsStartIOsMinimum,
       "sm6kSystemPagingStatisticsDoneIOsMinimum": sm6kSystemPagingStatisticsDoneIOsMinimum,
       "sm6kSystemPagingStatisticsPageScansMinimum": sm6kSystemPagingStatisticsPageScansMinimum,
       "sm6kSystemPagingStatisticsScanClockCyclesMinimum": sm6kSystemPagingStatisticsScanClockCyclesMinimum,
       "sm6kSystemPagingStatisticsPageStealsMinimum": sm6kSystemPagingStatisticsPageStealsMinimum,
       "sm6kSystemPagingStatisticsFreeFrameWaitsMinimum": sm6kSystemPagingStatisticsFreeFrameWaitsMinimum,
       "sm6kSystemPagingStatisticsExtendXPTWaitsMinimum": sm6kSystemPagingStatisticsExtendXPTWaitsMinimum,
       "sm6kSystemPagingStatisticsPendingIOWaitsMinimum": sm6kSystemPagingStatisticsPendingIOWaitsMinimum,
       "sm6kSystemPagingStatisticsPageFaultsMaximum": sm6kSystemPagingStatisticsPageFaultsMaximum,
       "sm6kSystemPagingStatisticsPageReclaimsMaximum": sm6kSystemPagingStatisticsPageReclaimsMaximum,
       "sm6kSystemPagingStatisticsPagesPagedInMaximum": sm6kSystemPagingStatisticsPagesPagedInMaximum,
       "sm6kSystemPagingStatisticsPagesPagedOutMaximum": sm6kSystemPagingStatisticsPagesPagedOutMaximum,
       "sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum": sm6kSystemPagingStatisticsPageInsFromPagingSpaceMaximum,
       "sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum": sm6kSystemPagingStatisticsPageOutsFromPagingSpaceMaximum,
       "sm6kSystemPagingStatisticsStartIOsMaximum": sm6kSystemPagingStatisticsStartIOsMaximum,
       "sm6kSystemPagingStatisticsDoneIOsMaximum": sm6kSystemPagingStatisticsDoneIOsMaximum,
       "sm6kSystemPagingStatisticsPageScansMaximum": sm6kSystemPagingStatisticsPageScansMaximum,
       "sm6kSystemPagingStatisticsScanClockCyclesMaximum": sm6kSystemPagingStatisticsScanClockCyclesMaximum,
       "sm6kSystemPagingStatisticsPageStealsMaximum": sm6kSystemPagingStatisticsPageStealsMaximum,
       "sm6kSystemPagingStatisticsFreeFrameWaitsMaximum": sm6kSystemPagingStatisticsFreeFrameWaitsMaximum,
       "sm6kSystemPagingStatisticsExtendXPTWaitsMaximum": sm6kSystemPagingStatisticsExtendXPTWaitsMaximum,
       "sm6kSystemPagingStatisticsPendingIOWaitsMaximum": sm6kSystemPagingStatisticsPendingIOWaitsMaximum,
       "sm6kSystemFileSystem": sm6kSystemFileSystem,
       "sm6kSystemFileSystemMounted": sm6kSystemFileSystemMounted,
       "sm6kSystemFileSystemTable": sm6kSystemFileSystemTable,
       "sm6kSystemFileSystemEntry": sm6kSystemFileSystemEntry,
       "sm6kSystemFileSystemName": sm6kSystemFileSystemName,
       "sm6kSystemFileSystemSize": sm6kSystemFileSystemSize,
       "sm6kSystemFileSystemFree": sm6kSystemFileSystemFree,
       "sm6kSystemFileSystemPercentUsed": sm6kSystemFileSystemPercentUsed,
       "sm6kSystemFileSystemInodesUsed": sm6kSystemFileSystemInodesUsed,
       "sm6kSystemFileSystemInodesPercentUsed": sm6kSystemFileSystemInodesPercentUsed,
       "sm6kSystemFileSystemInodeCount": sm6kSystemFileSystemInodeCount,
       "sm6kSystemFileSystemFileSystem": sm6kSystemFileSystemFileSystem,
       "sm6kSystemFileSystemRemote": sm6kSystemFileSystemRemote,
       "sm6kSystemSubSystems": sm6kSystemSubSystems,
       "sm6kSystemSubSystemsCount": sm6kSystemSubSystemsCount,
       "sm6kSystemSubSystemsTable": sm6kSystemSubSystemsTable,
       "sm6kSystemSubSystemsEntry": sm6kSystemSubSystemsEntry,
       "sm6kSystemSubSystemsName": sm6kSystemSubSystemsName,
       "sm6kSystemSubSystemsPID": sm6kSystemSubSystemsPID,
       "sm6kSystemSubSystemsStatusDescription": sm6kSystemSubSystemsStatusDescription,
       "sm6kSystemSubSystemsStatusText": sm6kSystemSubSystemsStatusText,
       "sm6kSystemSubSystemsStatusCode": sm6kSystemSubSystemsStatusCode,
       "sm6kSystemProcess": sm6kSystemProcess,
       "sm6kSystemProcessCount": sm6kSystemProcessCount,
       "sm6kSystemProcessTable": sm6kSystemProcessTable,
       "sm6kSystemProcessEntry": sm6kSystemProcessEntry,
       "sm6kSystemProcessLoginUser": sm6kSystemProcessLoginUser,
       "sm6kSystemProcessPID": sm6kSystemProcessPID,
       "sm6kSystemProcessParentPID": sm6kSystemProcessParentPID,
       "sm6kSystemProcessCPUTime": sm6kSystemProcessCPUTime,
       "sm6kSystemProcessUserTime": sm6kSystemProcessUserTime,
       "sm6kSystemProcessSystemTime": sm6kSystemProcessSystemTime,
       "sm6kSystemProcessPageFaultsIO": sm6kSystemProcessPageFaultsIO,
       "sm6kSystemProcessPageFaultsNoIO": sm6kSystemProcessPageFaultsNoIO,
       "sm6kSystemProcessPriority": sm6kSystemProcessPriority,
       "sm6kSystemProcessNice": sm6kSystemProcessNice,
       "sm6kSystemProcessState": sm6kSystemProcessState,
       "sm6kSystemProcessWait": sm6kSystemProcessWait,
       "sm6kSystemProcessDataResidentSetSize": sm6kSystemProcessDataResidentSetSize,
       "sm6kSystemProcessTextResidentSetSize": sm6kSystemProcessTextResidentSetSize,
       "sm6kSystemProcessImageSize": sm6kSystemProcessImageSize,
       "sm6kSystemProcessDataVirtualMemorySize": sm6kSystemProcessDataVirtualMemorySize,
       "sm6kSystemProcessPercentMemory": sm6kSystemProcessPercentMemory,
       "sm6kSystemProcessCPU": sm6kSystemProcessCPU,
       "sm6kSystemProcessStartTime": sm6kSystemProcessStartTime,
       "sm6kSystemProcessCommand": sm6kSystemProcessCommand,
       "sm6kSystemProcessLoginUID": sm6kSystemProcessLoginUID,
       "sm6kSystemProcessEffectiveUID": sm6kSystemProcessEffectiveUID,
       "sm6kSystemProcessEffectiveGID": sm6kSystemProcessEffectiveGID,
       "sm6kSystemProcessEffectiveGroupName": sm6kSystemProcessEffectiveGroupName,
       "sm6kSystemProcessSUID": sm6kSystemProcessSUID,
       "sm6kSystemProcessPgrp": sm6kSystemProcessPgrp,
       "sm6kSystemProcessPFlags": sm6kSystemProcessPFlags,
       "sm6kSystemProcessAdspace": sm6kSystemProcessAdspace,
       "sm6kSystemProcessTTYp": sm6kSystemProcessTTYp,
       "sm6kSystemProcessTTYd": sm6kSystemProcessTTYd,
       "sm6kSystemProcessNSwap": sm6kSystemProcessNSwap,
       "sm6kSystemProcessInblocks": sm6kSystemProcessInblocks,
       "sm6kSystemProcessOutblocks": sm6kSystemProcessOutblocks,
       "sm6kSystemProcessMsgsnd": sm6kSystemProcessMsgsnd,
       "sm6kSystemProcessMsgrcv": sm6kSystemProcessMsgrcv,
       "sm6kSystemProcessNsignals": sm6kSystemProcessNsignals,
       "sm6kSystemProcessNVcsw": sm6kSystemProcessNVcsw,
       "sm6kSystemProcessNIvcsw": sm6kSystemProcessNIvcsw,
       "sm6kSystemProcessArguments": sm6kSystemProcessArguments,
       "sm6kSystemProcessSignal": sm6kSystemProcessSignal,
       "sm6kSystemUsers": sm6kSystemUsers,
       "sm6kSystemUsersLoggedIn": sm6kSystemUsersLoggedIn,
       "sm6kSystemUsersTable": sm6kSystemUsersTable,
       "sm6kSystemUsersEntry": sm6kSystemUsersEntry,
       "sm6kSystemUsersName": sm6kSystemUsersName,
       "sm6kSystemUsersLine": sm6kSystemUsersLine,
       "sm6kSystemUsersTime": sm6kSystemUsersTime,
       "sm6kSystemUsersPID": sm6kSystemUsersPID,
       "sm6kSystemUsersRemoteHost": sm6kSystemUsersRemoteHost,
       "sm6kSystemUtilization": sm6kSystemUtilization,
       "sm6kSystemUtilizationCPU": sm6kSystemUtilizationCPU,
       "sm6kSystemUtilizationCPUPollingInterval": sm6kSystemUtilizationCPUPollingInterval,
       "sm6kSystemUtilizationCPUCount": sm6kSystemUtilizationCPUCount,
       "sm6kSystemUtilizationCPUTable": sm6kSystemUtilizationCPUTable,
       "sm6kSystemUtilizationCPUEntry": sm6kSystemUtilizationCPUEntry,
       "sm6kSystemUtilizationCPUIntervalName": sm6kSystemUtilizationCPUIntervalName,
       "sm6kSystemUtilizationCPUIntervalStartTime": sm6kSystemUtilizationCPUIntervalStartTime,
       "sm6kSystemUtilizationCPUIntervalLength": sm6kSystemUtilizationCPUIntervalLength,
       "sm6kSystemUtilizationCPUUser": sm6kSystemUtilizationCPUUser,
       "sm6kSystemUtilizationCPUSystem": sm6kSystemUtilizationCPUSystem,
       "sm6kSystemUtilizationCPUIdle": sm6kSystemUtilizationCPUIdle,
       "sm6kSystemUtilizationCPUWait": sm6kSystemUtilizationCPUWait,
       "sm6kSystemUtilizationCPUBusy": sm6kSystemUtilizationCPUBusy,
       "sm6kSystemUtilizationCPUUserMinimum": sm6kSystemUtilizationCPUUserMinimum,
       "sm6kSystemUtilizationCPUSystemMinimum": sm6kSystemUtilizationCPUSystemMinimum,
       "sm6kSystemUtilizationCPUIdleMinimum": sm6kSystemUtilizationCPUIdleMinimum,
       "sm6kSystemUtilizationCPUWaitMinimum": sm6kSystemUtilizationCPUWaitMinimum,
       "sm6kSystemUtilizationCPUBusyMinimum": sm6kSystemUtilizationCPUBusyMinimum,
       "sm6kSystemUtilizationCPUUserMaximum": sm6kSystemUtilizationCPUUserMaximum,
       "sm6kSystemUtilizationCPUSystemMaximum": sm6kSystemUtilizationCPUSystemMaximum,
       "sm6kSystemUtilizationCPUIdleMaximum": sm6kSystemUtilizationCPUIdleMaximum,
       "sm6kSystemUtilizationCPUWaitMaximum": sm6kSystemUtilizationCPUWaitMaximum,
       "sm6kSystemUtilizationCPUBusyMaximum": sm6kSystemUtilizationCPUBusyMaximum,
       "sm6kSystemUtilizationCPUNumber": sm6kSystemUtilizationCPUNumber,
       "sm6kSystemUtilizationKernel": sm6kSystemUtilizationKernel,
       "sm6kSystemUtilizationKernelPollingInterval": sm6kSystemUtilizationKernelPollingInterval,
       "sm6kSystemUtilizationKernelTable": sm6kSystemUtilizationKernelTable,
       "sm6kSystemUtilizationKernelEntry": sm6kSystemUtilizationKernelEntry,
       "sm6kSystemUtilizationKernelName": sm6kSystemUtilizationKernelName,
       "sm6kSystemUtilizationKernelIntervalStartTime": sm6kSystemUtilizationKernelIntervalStartTime,
       "sm6kSystemUtilizationKernelIntervalLength": sm6kSystemUtilizationKernelIntervalLength,
       "sm6kSystemUtilizationKernelContextSwitches": sm6kSystemUtilizationKernelContextSwitches,
       "sm6kSystemUtilizationKernelSystemCalls": sm6kSystemUtilizationKernelSystemCalls,
       "sm6kSystemUtilizationKernelSystemReads": sm6kSystemUtilizationKernelSystemReads,
       "sm6kSystemUtilizationKernelSystemWrites": sm6kSystemUtilizationKernelSystemWrites,
       "sm6kSystemUtilizationKernelForks": sm6kSystemUtilizationKernelForks,
       "sm6kSystemUtilizationKernelExecs": sm6kSystemUtilizationKernelExecs,
       "sm6kSystemUtilizationKernelRunQueue": sm6kSystemUtilizationKernelRunQueue,
       "sm6kSystemUtilizationKernelSwapQueue": sm6kSystemUtilizationKernelSwapQueue,
       "sm6kSystemUtilizationKernelSemaphores": sm6kSystemUtilizationKernelSemaphores,
       "sm6kSystemUtilizationKernelMessages": sm6kSystemUtilizationKernelMessages,
       "sm6kSystemUtilizationKernelProcessOverflow": sm6kSystemUtilizationKernelProcessOverflow,
       "sm6kSystemUtilizationKernelBytesRead": sm6kSystemUtilizationKernelBytesRead,
       "sm6kSystemUtilizationKernelBytesWritten": sm6kSystemUtilizationKernelBytesWritten,
       "sm6kSystemUtilizationKernelRawTTYOut": sm6kSystemUtilizationKernelRawTTYOut,
       "sm6kSystemUtilizationKernelContextSwitchesMinimum": sm6kSystemUtilizationKernelContextSwitchesMinimum,
       "sm6kSystemUtilizationKernelSystemCallsMinimum": sm6kSystemUtilizationKernelSystemCallsMinimum,
       "sm6kSystemUtilizationKernelSystemReadsMinimum": sm6kSystemUtilizationKernelSystemReadsMinimum,
       "sm6kSystemUtilizationKernelSystemWritesMinimum": sm6kSystemUtilizationKernelSystemWritesMinimum,
       "sm6kSystemUtilizationKernelForksMinimum": sm6kSystemUtilizationKernelForksMinimum,
       "sm6kSystemUtilizationKernelExecsMinimum": sm6kSystemUtilizationKernelExecsMinimum,
       "sm6kSystemUtilizationKernelRunQueueMinimum": sm6kSystemUtilizationKernelRunQueueMinimum,
       "sm6kSystemUtilizationKernelSwapQueueMinimum": sm6kSystemUtilizationKernelSwapQueueMinimum,
       "sm6kSystemUtilizationKernelSemaphoresMinimum": sm6kSystemUtilizationKernelSemaphoresMinimum,
       "sm6kSystemUtilizationKernelMessagesMinimum": sm6kSystemUtilizationKernelMessagesMinimum,
       "sm6kSystemUtilizationKernelProcessOverflowMinimum": sm6kSystemUtilizationKernelProcessOverflowMinimum,
       "sm6kSystemUtilizationKernelBytesReadMinimum": sm6kSystemUtilizationKernelBytesReadMinimum,
       "sm6kSystemUtilizationKernelBytesWrittenMinimum": sm6kSystemUtilizationKernelBytesWrittenMinimum,
       "sm6kSystemUtilizationKernelRawTTYOutMinimum": sm6kSystemUtilizationKernelRawTTYOutMinimum,
       "sm6kSystemUtilizationKernelContextSwitchesMaximum": sm6kSystemUtilizationKernelContextSwitchesMaximum,
       "sm6kSystemUtilizationKernelSystemCallsMaximum": sm6kSystemUtilizationKernelSystemCallsMaximum,
       "sm6kSystemUtilizationKernelSystemReadsMaximum": sm6kSystemUtilizationKernelSystemReadsMaximum,
       "sm6kSystemUtilizationKernelSystemWritesMaximum": sm6kSystemUtilizationKernelSystemWritesMaximum,
       "sm6kSystemUtilizationKernelForksMaximum": sm6kSystemUtilizationKernelForksMaximum,
       "sm6kSystemUtilizationKernelExecsMaximum": sm6kSystemUtilizationKernelExecsMaximum,
       "sm6kSystemUtilizationKernelRunQueueMaximum": sm6kSystemUtilizationKernelRunQueueMaximum,
       "sm6kSystemUtilizationKernelSwapQueueMaximum": sm6kSystemUtilizationKernelSwapQueueMaximum,
       "sm6kSystemUtilizationKernelSemaphoresMaximum": sm6kSystemUtilizationKernelSemaphoresMaximum,
       "sm6kSystemUtilizationKernelMessagesMaximum": sm6kSystemUtilizationKernelMessagesMaximum,
       "sm6kSystemUtilizationKernelProcessOverflowMaximum": sm6kSystemUtilizationKernelProcessOverflowMaximum,
       "sm6kSystemUtilizationKernelBytesReadMaximum": sm6kSystemUtilizationKernelBytesReadMaximum,
       "sm6kSystemUtilizationKernelBytesWrittenMaximum": sm6kSystemUtilizationKernelBytesWrittenMaximum,
       "sm6kSystemUtilizationKernelRawTTYOutMaximum": sm6kSystemUtilizationKernelRawTTYOutMaximum,
       "sm6kSystemUtilizationIostat": sm6kSystemUtilizationIostat,
       "sm6kSystemUtilizationIostatPollingInterval": sm6kSystemUtilizationIostatPollingInterval,
       "sm6kSystemUtilizationIostatTable": sm6kSystemUtilizationIostatTable,
       "sm6kSystemUtilizationIostatEntry": sm6kSystemUtilizationIostatEntry,
       "sm6kSystemUtilizationIostatName": sm6kSystemUtilizationIostatName,
       "sm6kSystemUtilizationIostatIntervalStartTime": sm6kSystemUtilizationIostatIntervalStartTime,
       "sm6kSystemUtilizationIostatIntervalLength": sm6kSystemUtilizationIostatIntervalLength,
       "sm6kSystemUtilizationIostatPercentTimeActive": sm6kSystemUtilizationIostatPercentTimeActive,
       "sm6kSystemUtilizationIostatKilobytesTransferRate": sm6kSystemUtilizationIostatKilobytesTransferRate,
       "sm6kSystemUtilizationIostatTransfers": sm6kSystemUtilizationIostatTransfers,
       "sm6kSystemUtilizationIostatKilobytesRead": sm6kSystemUtilizationIostatKilobytesRead,
       "sm6kSystemUtilizationIostatKilobytesWritten": sm6kSystemUtilizationIostatKilobytesWritten,
       "sm6kSystemUtilizationIostatPercentTimeActiveMinimum": sm6kSystemUtilizationIostatPercentTimeActiveMinimum,
       "sm6kSystemUtilizationIostatKilobytesTransferRateMinimum": sm6kSystemUtilizationIostatKilobytesTransferRateMinimum,
       "sm6kSystemUtilizationIostatTransfersMinimum": sm6kSystemUtilizationIostatTransfersMinimum,
       "sm6kSystemUtilizationIostatKilobytesReadMinimum": sm6kSystemUtilizationIostatKilobytesReadMinimum,
       "sm6kSystemUtilizationIostatKilobytesWrittenMinimum": sm6kSystemUtilizationIostatKilobytesWrittenMinimum,
       "sm6kSystemUtilizationIostatPercentTimeActiveMaximum": sm6kSystemUtilizationIostatPercentTimeActiveMaximum,
       "sm6kSystemUtilizationIostatKilobytesTransferRateMaximum": sm6kSystemUtilizationIostatKilobytesTransferRateMaximum,
       "sm6kSystemUtilizationIostatTransfersMaximum": sm6kSystemUtilizationIostatTransfersMaximum,
       "sm6kSystemUtilizationIostatKilobytesReadMaximum": sm6kSystemUtilizationIostatKilobytesReadMaximum,
       "sm6kSystemUtilizationIostatKilobytesWrittenMaximum": sm6kSystemUtilizationIostatKilobytesWrittenMaximum,
       "sm6kSystemReboot": sm6kSystemReboot,
       "sm6kSystemRebootTimer": sm6kSystemRebootTimer,
       "sm6kSystemMiscellaneous": sm6kSystemMiscellaneous,
       "sm6kSystemMiscellaneousTimeText": sm6kSystemMiscellaneousTimeText,
       "sm6kSystemMiscellaneousTime": sm6kSystemMiscellaneousTime,
       "sm6kSystemMiscellaneousRandom": sm6kSystemMiscellaneousRandom,
       "sm6kSystemMiscellaneousFreeSpace": sm6kSystemMiscellaneousFreeSpace,
       "sm6kSystemMiscellaneousPublicKey": sm6kSystemMiscellaneousPublicKey,
       "sm6kSystemMiscellaneousLocalSocket": sm6kSystemMiscellaneousLocalSocket,
       "sm6kNetworkInformation": sm6kNetworkInformation,
       "sm6kNetworkSessionInformation": sm6kNetworkSessionInformation,
       "sm6kNetworkSessionCount": sm6kNetworkSessionCount,
       "sm6kNetworkSessionTable": sm6kNetworkSessionTable,
       "sm6kNetworkSessionEntry": sm6kNetworkSessionEntry,
       "sm6kNetworkSessionName": sm6kNetworkSessionName,
       "sm6kNetworkSessionCurrentState": sm6kNetworkSessionCurrentState,
       "sm6kNetworkSessionLastStateChange": sm6kNetworkSessionLastStateChange,
       "sm6kNetworkSessionLastPollAttempt": sm6kNetworkSessionLastPollAttempt,
       "sm6kNetworkSessionAddressFamily": sm6kNetworkSessionAddressFamily,
       "sm6kNetworkSessionNetAddress": sm6kNetworkSessionNetAddress,
       "sm6kNetworkSessionTransmitAttempts": sm6kNetworkSessionTransmitAttempts,
       "sm6kNetworkSessionPacketsReceived": sm6kNetworkSessionPacketsReceived,
       "sm6kNetworkSessionLastTransmitTime": sm6kNetworkSessionLastTransmitTime,
       "sm6kNetworkSessionLastReceiveTime": sm6kNetworkSessionLastReceiveTime,
       "sm6kNetworkSessionMinimumResponseTime": sm6kNetworkSessionMinimumResponseTime,
       "sm6kNetworkSessionRecentAverageResponseTime": sm6kNetworkSessionRecentAverageResponseTime,
       "sm6kNetworkSessionLifeTimeAverageResponseTime": sm6kNetworkSessionLifeTimeAverageResponseTime,
       "sm6kNetworkSessionMaximumResponseTime": sm6kNetworkSessionMaximumResponseTime,
       "sm6kCommand": sm6kCommand,
       "sm6kCommandTable": sm6kCommandTable,
       "sm6kCommandEntry": sm6kCommandEntry,
       "sm6kCommandState": sm6kCommandState,
       "sm6kCommandName": sm6kCommandName,
       "sm6kCommandDescription": sm6kCommandDescription,
       "sm6kCommandOwnerID": sm6kCommandOwnerID,
       "sm6kCommandGetStringAndParameters": sm6kCommandGetStringAndParameters,
       "sm6kCommandSetStringAndParameters": sm6kCommandSetStringAndParameters,
       "sm6kCommandTimeOutValue": sm6kCommandTimeOutValue,
       "sm6kCommandCountToLive": sm6kCommandCountToLive,
       "sm6kCommandTimeToLive": sm6kCommandTimeToLive,
       "sm6kCommandOutputResultIndex": sm6kCommandOutputResultIndex,
       "sm6kCommandOutputRowIndex": sm6kCommandOutputRowIndex,
       "sm6kCommandOutputColumnIndex": sm6kCommandOutputColumnIndex,
       "sm6kCommandDisplayStringResult": sm6kCommandDisplayStringResult,
       "sm6kCommandIntegerResult": sm6kCommandIntegerResult,
       "sm6kCommandCounterResult": sm6kCommandCounterResult,
       "sm6kCommandGaugeResult": sm6kCommandGaugeResult,
       "sm6kCommandExecutionReturnCode": sm6kCommandExecutionReturnCode,
       "sm6kCommandStandardError": sm6kCommandStandardError,
       "sm6kThreshold": sm6kThreshold,
       "sm6kThresholdTable": sm6kThresholdTable,
       "sm6kThresholdEntry": sm6kThresholdEntry,
       "sm6kThresholdState": sm6kThresholdState,
       "sm6kThresholdName": sm6kThresholdName,
       "sm6kThresholdDescription": sm6kThresholdDescription,
       "sm6kThresholdOwnerID": sm6kThresholdOwnerID,
       "sm6kThresholdLocalRemoteMIBVariable": sm6kThresholdLocalRemoteMIBVariable,
       "sm6kThresholdCondition": sm6kThresholdCondition,
       "sm6kThresholdValue": sm6kThresholdValue,
       "sm6kThresholdPollTime": sm6kThresholdPollTime,
       "sm6kThresholdLastValue": sm6kThresholdLastValue,
       "sm6kThresholdIntegerDataMax": sm6kThresholdIntegerDataMax,
       "sm6kThresholdIntegerDataMin": sm6kThresholdIntegerDataMin,
       "sm6kThresholdIntegerDataAvg": sm6kThresholdIntegerDataAvg,
       "sm6kThresholdCounterGaugeDataMax": sm6kThresholdCounterGaugeDataMax,
       "sm6kThresholdCounterGaugeDataMin": sm6kThresholdCounterGaugeDataMin,
       "sm6kThresholdCounterGaugeDataAvg": sm6kThresholdCounterGaugeDataAvg,
       "sm6kThresholdDataSamples": sm6kThresholdDataSamples,
       "sm6kThresholdTrapDescription": sm6kThresholdTrapDescription,
       "sm6kThresholdArmEnterprise": sm6kThresholdArmEnterprise,
       "sm6kThresholdSpecificTrap": sm6kThresholdSpecificTrap,
       "sm6kThresholdCommandToExecute": sm6kThresholdCommandToExecute,
       "sm6kThresholdReArmCondition": sm6kThresholdReArmCondition,
       "sm6kThresholdReArmValue": sm6kThresholdReArmValue,
       "sm6kThresholdReArmTrapDescription": sm6kThresholdReArmTrapDescription,
       "sm6kThresholdReArmEnterprise": sm6kThresholdReArmEnterprise,
       "sm6kThresholdReArmSpecificTrap": sm6kThresholdReArmSpecificTrap,
       "sm6kThresholdReArmCommandToExecute": sm6kThresholdReArmCommandToExecute,
       "sm6kThresholdLastChangedSession": sm6kThresholdLastChangedSession,
       "sm6kThresholdStandardError": sm6kThresholdStandardError,
       "sm6kThresholdLastResponseTime": sm6kThresholdLastResponseTime,
       "sm6kThresholdResponseCount": sm6kThresholdResponseCount,
       "sm6kThresholdTimeoutCount": sm6kThresholdTimeoutCount,
       "sm6kThresholdNoValueCount": sm6kThresholdNoValueCount,
       "sm6kAnalysis": sm6kAnalysis,
       "sm6kAnalysisTable": sm6kAnalysisTable,
       "sm6kAnalysisEntry": sm6kAnalysisEntry,
       "sm6kAnalysisState": sm6kAnalysisState,
       "sm6kAnalysisName": sm6kAnalysisName,
       "sm6kAnalysisDescription": sm6kAnalysisDescription,
       "sm6kAnalysisOwnerID": sm6kAnalysisOwnerID,
       "sm6kAnalysisLocalRemoteMIBVariableExpression": sm6kAnalysisLocalRemoteMIBVariableExpression,
       "sm6kAnalysisPollTime": sm6kAnalysisPollTime,
       "sm6kAnalysisResultIndex": sm6kAnalysisResultIndex,
       "sm6kAnalysisIntegerResult": sm6kAnalysisIntegerResult,
       "sm6kAnalysisCounterResult": sm6kAnalysisCounterResult,
       "sm6kAnalysisGaugeResult": sm6kAnalysisGaugeResult,
       "sm6kAnalysisDisplayStringResult": sm6kAnalysisDisplayStringResult,
       "sm6kAnalysisReturnCode": sm6kAnalysisReturnCode,
       "sm6kAnalysisStandardError": sm6kAnalysisStandardError,
       "sm6kFilter": sm6kFilter,
       "sm6kFilterDefaultAction": sm6kFilterDefaultAction,
       "sm6kFilterTrapReception": sm6kFilterTrapReception,
       "sm6kFilterTotalTrapsReceived": sm6kFilterTotalTrapsReceived,
       "sm6kFilterTable": sm6kFilterTable,
       "sm6kFilterEntry": sm6kFilterEntry,
       "sm6kFilterState": sm6kFilterState,
       "sm6kFilterParticipationState": sm6kFilterParticipationState,
       "sm6kFilterName": sm6kFilterName,
       "sm6kFilterDescription": sm6kFilterDescription,
       "sm6kFilterAction": sm6kFilterAction,
       "sm6kFilterEntryEnterpriseExpression": sm6kFilterEntryEnterpriseExpression,
       "sm6kFilterAgentAddrExpression": sm6kFilterAgentAddrExpression,
       "sm6kFilterGenericExpression": sm6kFilterGenericExpression,
       "sm6kFilterSpecificExpression": sm6kFilterSpecificExpression,
       "sm6kFilterVariableExpression": sm6kFilterVariableExpression,
       "sm6kFilterTotalTrapsMatched": sm6kFilterTotalTrapsMatched,
       "sm6kFilterActivationTime": sm6kFilterActivationTime,
       "sm6kFilterActivationDayOfWeek": sm6kFilterActivationDayOfWeek,
       "sm6kFilterDeactivationTime": sm6kFilterDeactivationTime,
       "sm6kFilterDeactivationDayOfWeek": sm6kFilterDeactivationDayOfWeek,
       "sm6kFilterTrapDestinations": sm6kFilterTrapDestinations,
       "sm6kFilterMatchedCommand": sm6kFilterMatchedCommand,
       "sm6kFilterMatchedTrapDescription": sm6kFilterMatchedTrapDescription,
       "sm6kFilterMatchedTrapEnterprise": sm6kFilterMatchedTrapEnterprise,
       "sm6kFilterMatchedSpecificTrap": sm6kFilterMatchedSpecificTrap,
       "sm6kFilterThrottleType": sm6kFilterThrottleType,
       "sm6kFilterThrottleArmTrapCount": sm6kFilterThrottleArmTrapCount,
       "sm6kFilterThrottleArmedCommand": sm6kFilterThrottleArmedCommand,
       "sm6kFilterThrottleArmedTrapDescription": sm6kFilterThrottleArmedTrapDescription,
       "sm6kFilterThrottleArmedTrapEnterprise": sm6kFilterThrottleArmedTrapEnterprise,
       "sm6kFilterThrottleArmedSpecificTrap": sm6kFilterThrottleArmedSpecificTrap,
       "sm6kFilterThrottleDisarmTimer": sm6kFilterThrottleDisarmTimer,
       "sm6kFilterThrottleDisarmTrapCount": sm6kFilterThrottleDisarmTrapCount,
       "sm6kFilterThrottleDisarmedCommand": sm6kFilterThrottleDisarmedCommand,
       "sm6kFilterThrottleDisarmedTrapDescription": sm6kFilterThrottleDisarmedTrapDescription,
       "sm6kFilterThrottleDisarmedTrapEnterprise": sm6kFilterThrottleDisarmedTrapEnterprise,
       "sm6kFilterThrottleDisarmedSpecificTrap": sm6kFilterThrottleDisarmedSpecificTrap,
       "sm6kFilterThrottleState": sm6kFilterThrottleState,
       "sm6kFilterThrottleTimeStarted": sm6kFilterThrottleTimeStarted,
       "sm6kFilterThrottleTrapCount": sm6kFilterThrottleTrapCount,
       "sm6kAlias": sm6kAlias,
       "sm6kAliasTable": sm6kAliasTable,
       "sm6kAliasEntry": sm6kAliasEntry,
       "sm6kAliasState": sm6kAliasState,
       "sm6kAliasName": sm6kAliasName,
       "sm6kAliasList": sm6kAliasList,
       "sm6kAliasResolvedList": sm6kAliasResolvedList,
       "sm6kTrapDestination": sm6kTrapDestination,
       "sm6kTrapDestinationTable": sm6kTrapDestinationTable,
       "sm6kTrapDestinationEntry": sm6kTrapDestinationEntry,
       "sm6kTrapDestinationState": sm6kTrapDestinationState,
       "sm6kTrapDestinationName": sm6kTrapDestinationName,
       "sm6kTrapDestinationHost": sm6kTrapDestinationHost,
       "sm6kTrapDestinationMask": sm6kTrapDestinationMask,
       "sm6kAdministration": sm6kAdministration,
       "sm6kAdministrationTable": sm6kAdministrationTable,
       "sm6kAdministrationEntry": sm6kAdministrationEntry,
       "sm6kAdministrationFieldState": sm6kAdministrationFieldState,
       "sm6kAdministrationFieldName": sm6kAdministrationFieldName,
       "sm6kAdministrationFieldOwner": sm6kAdministrationFieldOwner,
       "sm6kAdministrationFieldDescription": sm6kAdministrationFieldDescription,
       "sm6kAdministrationFieldValue": sm6kAdministrationFieldValue}
)
