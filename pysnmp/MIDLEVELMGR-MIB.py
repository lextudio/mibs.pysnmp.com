# SNMP MIB module (MIDLEVELMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIDLEVELMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:01 2024
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
_SmMlmProgramData_ObjectIdentity = ObjectIdentity
smMlmProgramData = _SmMlmProgramData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1)
)
_SmMlmProgramDescription_ObjectIdentity = ObjectIdentity
smMlmProgramDescription = _SmMlmProgramDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1)
)
_SmMlmProgramName_Type = DisplayString
_SmMlmProgramName_Object = MibScalar
smMlmProgramName = _SmMlmProgramName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 1),
    _SmMlmProgramName_Type()
)
smMlmProgramName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramName.setStatus("mandatory")
_SmMlmProgramNumber_Type = DisplayString
_SmMlmProgramNumber_Object = MibScalar
smMlmProgramNumber = _SmMlmProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 2),
    _SmMlmProgramNumber_Type()
)
smMlmProgramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramNumber.setStatus("mandatory")
_SmMlmProgramVersion_Type = DisplayString
_SmMlmProgramVersion_Object = MibScalar
smMlmProgramVersion = _SmMlmProgramVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 3),
    _SmMlmProgramVersion_Type()
)
smMlmProgramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramVersion.setStatus("mandatory")
_SmMlmProgramCompilationDate_Type = DisplayString
_SmMlmProgramCompilationDate_Object = MibScalar
smMlmProgramCompilationDate = _SmMlmProgramCompilationDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 4),
    _SmMlmProgramCompilationDate_Type()
)
smMlmProgramCompilationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramCompilationDate.setStatus("mandatory")
_SmMlmProgramUpTime_Type = TimeTicks
_SmMlmProgramUpTime_Object = MibScalar
smMlmProgramUpTime = _SmMlmProgramUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 5),
    _SmMlmProgramUpTime_Type()
)
smMlmProgramUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramUpTime.setStatus("mandatory")
_SmMlmProgramContact_Type = DisplayString
_SmMlmProgramContact_Object = MibScalar
smMlmProgramContact = _SmMlmProgramContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 1, 6),
    _SmMlmProgramContact_Type()
)
smMlmProgramContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramContact.setStatus("mandatory")
_SmMlmProgramControl_ObjectIdentity = ObjectIdentity
smMlmProgramControl = _SmMlmProgramControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2)
)
_SmMlmProgramControlLocalConfigurationFile_Type = DisplayString
_SmMlmProgramControlLocalConfigurationFile_Object = MibScalar
smMlmProgramControlLocalConfigurationFile = _SmMlmProgramControlLocalConfigurationFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 1),
    _SmMlmProgramControlLocalConfigurationFile_Type()
)
smMlmProgramControlLocalConfigurationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlLocalConfigurationFile.setStatus("mandatory")
_SmMlmProgramControlSavedFlags_Type = DisplayString
_SmMlmProgramControlSavedFlags_Object = MibScalar
smMlmProgramControlSavedFlags = _SmMlmProgramControlSavedFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 2),
    _SmMlmProgramControlSavedFlags_Type()
)
smMlmProgramControlSavedFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSavedFlags.setStatus("mandatory")
_SmMlmProgramControlAgentAddress_Type = IpAddress
_SmMlmProgramControlAgentAddress_Object = MibScalar
smMlmProgramControlAgentAddress = _SmMlmProgramControlAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 3),
    _SmMlmProgramControlAgentAddress_Type()
)
smMlmProgramControlAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlAgentAddress.setStatus("mandatory")


class _SmMlmProgramControlMaxTcpTrapQueue_Type(Integer32):
    """Custom type smMlmProgramControlMaxTcpTrapQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmProgramControlMaxTcpTrapQueue_Type.__name__ = "Integer32"
_SmMlmProgramControlMaxTcpTrapQueue_Object = MibScalar
smMlmProgramControlMaxTcpTrapQueue = _SmMlmProgramControlMaxTcpTrapQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 4),
    _SmMlmProgramControlMaxTcpTrapQueue_Type()
)
smMlmProgramControlMaxTcpTrapQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlMaxTcpTrapQueue.setStatus("mandatory")
_SmMlmProgramControlPercentMultiplier_Type = Integer32
_SmMlmProgramControlPercentMultiplier_Object = MibScalar
smMlmProgramControlPercentMultiplier = _SmMlmProgramControlPercentMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 5),
    _SmMlmProgramControlPercentMultiplier_Type()
)
smMlmProgramControlPercentMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlPercentMultiplier.setStatus("mandatory")


class _SmMlmProgramControlSamplesPerInterval_Type(Integer32):
    """Custom type smMlmProgramControlSamplesPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SmMlmProgramControlSamplesPerInterval_Type.__name__ = "Integer32"
_SmMlmProgramControlSamplesPerInterval_Object = MibScalar
smMlmProgramControlSamplesPerInterval = _SmMlmProgramControlSamplesPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 6),
    _SmMlmProgramControlSamplesPerInterval_Type()
)
smMlmProgramControlSamplesPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSamplesPerInterval.setStatus("mandatory")


class _SmMlmProgramControlMaxOutstandingPingRequests_Type(Integer32):
    """Custom type smMlmProgramControlMaxOutstandingPingRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SmMlmProgramControlMaxOutstandingPingRequests_Type.__name__ = "Integer32"
_SmMlmProgramControlMaxOutstandingPingRequests_Object = MibScalar
smMlmProgramControlMaxOutstandingPingRequests = _SmMlmProgramControlMaxOutstandingPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 7),
    _SmMlmProgramControlMaxOutstandingPingRequests_Type()
)
smMlmProgramControlMaxOutstandingPingRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlMaxOutstandingPingRequests.setStatus("mandatory")
_SmMlmProgramControlRetryCount_Type = Integer32
_SmMlmProgramControlRetryCount_Object = MibScalar
smMlmProgramControlRetryCount = _SmMlmProgramControlRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 8),
    _SmMlmProgramControlRetryCount_Type()
)
smMlmProgramControlRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlRetryCount.setStatus("mandatory")
_SmMlmProgramControlTimeout_Type = TimeTicks
_SmMlmProgramControlTimeout_Object = MibScalar
smMlmProgramControlTimeout = _SmMlmProgramControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 9),
    _SmMlmProgramControlTimeout_Type()
)
smMlmProgramControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlTimeout.setStatus("mandatory")
_SmMlmProgramControlCurrentFlags_Type = DisplayString
_SmMlmProgramControlCurrentFlags_Object = MibScalar
smMlmProgramControlCurrentFlags = _SmMlmProgramControlCurrentFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 10),
    _SmMlmProgramControlCurrentFlags_Type()
)
smMlmProgramControlCurrentFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramControlCurrentFlags.setStatus("mandatory")
_SmMlmProgramControlReinitFlags_Type = DisplayString
_SmMlmProgramControlReinitFlags_Object = MibScalar
smMlmProgramControlReinitFlags = _SmMlmProgramControlReinitFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 11),
    _SmMlmProgramControlReinitFlags_Type()
)
smMlmProgramControlReinitFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlReinitFlags.setStatus("mandatory")


class _SmMlmProgramControlReInitializeMonitor_Type(Integer32):
    """Custom type smMlmProgramControlReInitializeMonitor based on Integer32"""
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


_SmMlmProgramControlReInitializeMonitor_Type.__name__ = "Integer32"
_SmMlmProgramControlReInitializeMonitor_Object = MibScalar
smMlmProgramControlReInitializeMonitor = _SmMlmProgramControlReInitializeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 12),
    _SmMlmProgramControlReInitializeMonitor_Type()
)
smMlmProgramControlReInitializeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlReInitializeMonitor.setStatus("mandatory")


class _SmMlmProgramControlSaveConfiguration_Type(Integer32):
    """Custom type smMlmProgramControlSaveConfiguration based on Integer32"""
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


_SmMlmProgramControlSaveConfiguration_Type.__name__ = "Integer32"
_SmMlmProgramControlSaveConfiguration_Object = MibScalar
smMlmProgramControlSaveConfiguration = _SmMlmProgramControlSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 2, 13),
    _SmMlmProgramControlSaveConfiguration_Type()
)
smMlmProgramControlSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSaveConfiguration.setStatus("mandatory")
_SmMlmProgramLog_ObjectIdentity = ObjectIdentity
smMlmProgramLog = _SmMlmProgramLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3)
)
_SmMlmProgramLogFileName_Type = DisplayString
_SmMlmProgramLogFileName_Object = MibScalar
smMlmProgramLogFileName = _SmMlmProgramLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 1),
    _SmMlmProgramLogFileName_Type()
)
smMlmProgramLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramLogFileName.setStatus("mandatory")
_SmMlmProgramLogFileSize_Type = Integer32
_SmMlmProgramLogFileSize_Object = MibScalar
smMlmProgramLogFileSize = _SmMlmProgramLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 2),
    _SmMlmProgramLogFileSize_Type()
)
smMlmProgramLogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramLogFileSize.setStatus("mandatory")
_SmMlmProgramLogMaxFileSize_Type = Integer32
_SmMlmProgramLogMaxFileSize_Object = MibScalar
smMlmProgramLogMaxFileSize = _SmMlmProgramLogMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 3),
    _SmMlmProgramLogMaxFileSize_Type()
)
smMlmProgramLogMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramLogMaxFileSize.setStatus("mandatory")
_SmMlmProgramLogNumFiles_Type = Integer32
_SmMlmProgramLogNumFiles_Object = MibScalar
smMlmProgramLogNumFiles = _SmMlmProgramLogNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 4),
    _SmMlmProgramLogNumFiles_Type()
)
smMlmProgramLogNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramLogNumFiles.setStatus("mandatory")


class _SmMlmProgramLogFileBehavior_Type(Integer32):
    """Custom type smMlmProgramLogFileBehavior based on Integer32"""
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


_SmMlmProgramLogFileBehavior_Type.__name__ = "Integer32"
_SmMlmProgramLogFileBehavior_Object = MibScalar
smMlmProgramLogFileBehavior = _SmMlmProgramLogFileBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 5),
    _SmMlmProgramLogFileBehavior_Type()
)
smMlmProgramLogFileBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramLogFileBehavior.setStatus("mandatory")
_SmMlmProgramLogMask_Type = DisplayString
_SmMlmProgramLogMask_Object = MibScalar
smMlmProgramLogMask = _SmMlmProgramLogMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 3, 6),
    _SmMlmProgramLogMask_Type()
)
smMlmProgramLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramLogMask.setStatus("mandatory")
_SmMlmProgramDataCollection_ObjectIdentity = ObjectIdentity
smMlmProgramDataCollection = _SmMlmProgramDataCollection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4)
)
_SmMlmProgramDataCollectionFileName_Type = DisplayString
_SmMlmProgramDataCollectionFileName_Object = MibScalar
smMlmProgramDataCollectionFileName = _SmMlmProgramDataCollectionFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 1),
    _SmMlmProgramDataCollectionFileName_Type()
)
smMlmProgramDataCollectionFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectionFileName.setStatus("mandatory")
_SmMlmProgramDataCollectionFileSize_Type = Integer32
_SmMlmProgramDataCollectionFileSize_Object = MibScalar
smMlmProgramDataCollectionFileSize = _SmMlmProgramDataCollectionFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 2),
    _SmMlmProgramDataCollectionFileSize_Type()
)
smMlmProgramDataCollectionFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectionFileSize.setStatus("mandatory")
_SmMlmProgramDataCollectionMaxFileSize_Type = Integer32
_SmMlmProgramDataCollectionMaxFileSize_Object = MibScalar
smMlmProgramDataCollectionMaxFileSize = _SmMlmProgramDataCollectionMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 3),
    _SmMlmProgramDataCollectionMaxFileSize_Type()
)
smMlmProgramDataCollectionMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectionMaxFileSize.setStatus("mandatory")
_SmMlmProgramDataCollectionNumFiles_Type = Integer32
_SmMlmProgramDataCollectionNumFiles_Object = MibScalar
smMlmProgramDataCollectionNumFiles = _SmMlmProgramDataCollectionNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 4),
    _SmMlmProgramDataCollectionNumFiles_Type()
)
smMlmProgramDataCollectionNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectionNumFiles.setStatus("mandatory")


class _SmMlmProgramDataCollectionFileBehavior_Type(Integer32):
    """Custom type smMlmProgramDataCollectionFileBehavior based on Integer32"""
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


_SmMlmProgramDataCollectionFileBehavior_Type.__name__ = "Integer32"
_SmMlmProgramDataCollectionFileBehavior_Object = MibScalar
smMlmProgramDataCollectionFileBehavior = _SmMlmProgramDataCollectionFileBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 4, 5),
    _SmMlmProgramDataCollectionFileBehavior_Type()
)
smMlmProgramDataCollectionFileBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectionFileBehavior.setStatus("mandatory")
_SmMlmProgramSetableTestObjects_ObjectIdentity = ObjectIdentity
smMlmProgramSetableTestObjects = _SmMlmProgramSetableTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5)
)
_SmMlmProgramControlSetableInteger_Type = Integer32
_SmMlmProgramControlSetableInteger_Object = MibScalar
smMlmProgramControlSetableInteger = _SmMlmProgramControlSetableInteger_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 1),
    _SmMlmProgramControlSetableInteger_Type()
)
smMlmProgramControlSetableInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSetableInteger.setStatus("mandatory")
_SmMlmProgramControlSetableCounter_Type = Counter32
_SmMlmProgramControlSetableCounter_Object = MibScalar
smMlmProgramControlSetableCounter = _SmMlmProgramControlSetableCounter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 2),
    _SmMlmProgramControlSetableCounter_Type()
)
smMlmProgramControlSetableCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSetableCounter.setStatus("mandatory")
_SmMlmProgramControlSetableGauge_Type = Gauge32
_SmMlmProgramControlSetableGauge_Object = MibScalar
smMlmProgramControlSetableGauge = _SmMlmProgramControlSetableGauge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 3),
    _SmMlmProgramControlSetableGauge_Type()
)
smMlmProgramControlSetableGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSetableGauge.setStatus("mandatory")
_SmMlmProgramControlSetableIpAddress_Type = IpAddress
_SmMlmProgramControlSetableIpAddress_Object = MibScalar
smMlmProgramControlSetableIpAddress = _SmMlmProgramControlSetableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 4),
    _SmMlmProgramControlSetableIpAddress_Type()
)
smMlmProgramControlSetableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSetableIpAddress.setStatus("mandatory")
_SmMlmProgramControlSetableTimeTicks_Type = TimeTicks
_SmMlmProgramControlSetableTimeTicks_Object = MibScalar
smMlmProgramControlSetableTimeTicks = _SmMlmProgramControlSetableTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 5),
    _SmMlmProgramControlSetableTimeTicks_Type()
)
smMlmProgramControlSetableTimeTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSetableTimeTicks.setStatus("mandatory")
_SmMlmProgramControlSetableOctetString_Type = DisplayString
_SmMlmProgramControlSetableOctetString_Object = MibScalar
smMlmProgramControlSetableOctetString = _SmMlmProgramControlSetableOctetString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 5, 6),
    _SmMlmProgramControlSetableOctetString_Type()
)
smMlmProgramControlSetableOctetString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramControlSetableOctetString.setStatus("mandatory")
_SmMlmProgramTrapLog_ObjectIdentity = ObjectIdentity
smMlmProgramTrapLog = _SmMlmProgramTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6)
)
_SmMlmProgramTrapLogFileName_Type = DisplayString
_SmMlmProgramTrapLogFileName_Object = MibScalar
smMlmProgramTrapLogFileName = _SmMlmProgramTrapLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6, 1),
    _SmMlmProgramTrapLogFileName_Type()
)
smMlmProgramTrapLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramTrapLogFileName.setStatus("mandatory")
_SmMlmProgramTrapLogFileSize_Type = Integer32
_SmMlmProgramTrapLogFileSize_Object = MibScalar
smMlmProgramTrapLogFileSize = _SmMlmProgramTrapLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6, 2),
    _SmMlmProgramTrapLogFileSize_Type()
)
smMlmProgramTrapLogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramTrapLogFileSize.setStatus("mandatory")
_SmMlmProgramTrapLogMaxFileSize_Type = Integer32
_SmMlmProgramTrapLogMaxFileSize_Object = MibScalar
smMlmProgramTrapLogMaxFileSize = _SmMlmProgramTrapLogMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6, 3),
    _SmMlmProgramTrapLogMaxFileSize_Type()
)
smMlmProgramTrapLogMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramTrapLogMaxFileSize.setStatus("mandatory")
_SmMlmProgramTrapLogNumFiles_Type = Integer32
_SmMlmProgramTrapLogNumFiles_Object = MibScalar
smMlmProgramTrapLogNumFiles = _SmMlmProgramTrapLogNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6, 4),
    _SmMlmProgramTrapLogNumFiles_Type()
)
smMlmProgramTrapLogNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramTrapLogNumFiles.setStatus("mandatory")


class _SmMlmProgramTrapLogFileBehavior_Type(Integer32):
    """Custom type smMlmProgramTrapLogFileBehavior based on Integer32"""
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


_SmMlmProgramTrapLogFileBehavior_Type.__name__ = "Integer32"
_SmMlmProgramTrapLogFileBehavior_Object = MibScalar
smMlmProgramTrapLogFileBehavior = _SmMlmProgramTrapLogFileBehavior_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6, 5),
    _SmMlmProgramTrapLogFileBehavior_Type()
)
smMlmProgramTrapLogFileBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramTrapLogFileBehavior.setStatus("mandatory")
_SmMlmProgramTrapLogMask_Type = DisplayString
_SmMlmProgramTrapLogMask_Object = MibScalar
smMlmProgramTrapLogMask = _SmMlmProgramTrapLogMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 1, 6, 6),
    _SmMlmProgramTrapLogMask_Type()
)
smMlmProgramTrapLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmProgramTrapLogMask.setStatus("mandatory")
_SmMlmResourceUsage_ObjectIdentity = ObjectIdentity
smMlmResourceUsage = _SmMlmResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2)
)
_SmMlmResourceUsageTable_Object = MibTable
smMlmResourceUsageTable = _SmMlmResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    smMlmResourceUsageTable.setStatus("mandatory")
_SmMlmResourceUsageEntry_Object = MibTableRow
smMlmResourceUsageEntry = _SmMlmResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1)
)
smMlmResourceUsageEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmResourceUsageName"),
)
if mibBuilder.loadTexts:
    smMlmResourceUsageEntry.setStatus("mandatory")
_SmMlmResourceUsageName_Type = DisplayString
_SmMlmResourceUsageName_Object = MibTableColumn
smMlmResourceUsageName = _SmMlmResourceUsageName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 1),
    _SmMlmResourceUsageName_Type()
)
smMlmResourceUsageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageName.setStatus("mandatory")
_SmMlmResourceUsageUserTime_Type = TimeTicks
_SmMlmResourceUsageUserTime_Object = MibTableColumn
smMlmResourceUsageUserTime = _SmMlmResourceUsageUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 2),
    _SmMlmResourceUsageUserTime_Type()
)
smMlmResourceUsageUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageUserTime.setStatus("mandatory")
_SmMlmResourceUsageSystemTime_Type = TimeTicks
_SmMlmResourceUsageSystemTime_Object = MibTableColumn
smMlmResourceUsageSystemTime = _SmMlmResourceUsageSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 3),
    _SmMlmResourceUsageSystemTime_Type()
)
smMlmResourceUsageSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageSystemTime.setStatus("mandatory")
_SmMlmResourceUsageTotalTime_Type = TimeTicks
_SmMlmResourceUsageTotalTime_Object = MibTableColumn
smMlmResourceUsageTotalTime = _SmMlmResourceUsageTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 4),
    _SmMlmResourceUsageTotalTime_Type()
)
smMlmResourceUsageTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageTotalTime.setStatus("mandatory")
_SmMlmResourceUsageMaxrss_Type = Counter32
_SmMlmResourceUsageMaxrss_Object = MibTableColumn
smMlmResourceUsageMaxrss = _SmMlmResourceUsageMaxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 5),
    _SmMlmResourceUsageMaxrss_Type()
)
smMlmResourceUsageMaxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageMaxrss.setStatus("mandatory")
_SmMlmResourceUsageIxrss_Type = Counter32
_SmMlmResourceUsageIxrss_Object = MibTableColumn
smMlmResourceUsageIxrss = _SmMlmResourceUsageIxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 6),
    _SmMlmResourceUsageIxrss_Type()
)
smMlmResourceUsageIxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageIxrss.setStatus("mandatory")
_SmMlmResourceUsageIdrss_Type = Counter32
_SmMlmResourceUsageIdrss_Object = MibTableColumn
smMlmResourceUsageIdrss = _SmMlmResourceUsageIdrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 7),
    _SmMlmResourceUsageIdrss_Type()
)
smMlmResourceUsageIdrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageIdrss.setStatus("mandatory")
_SmMlmResourceUsageIsrss_Type = Counter32
_SmMlmResourceUsageIsrss_Object = MibTableColumn
smMlmResourceUsageIsrss = _SmMlmResourceUsageIsrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 8),
    _SmMlmResourceUsageIsrss_Type()
)
smMlmResourceUsageIsrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageIsrss.setStatus("mandatory")
_SmMlmResourceUsageMinflt_Type = Counter32
_SmMlmResourceUsageMinflt_Object = MibTableColumn
smMlmResourceUsageMinflt = _SmMlmResourceUsageMinflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 9),
    _SmMlmResourceUsageMinflt_Type()
)
smMlmResourceUsageMinflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageMinflt.setStatus("mandatory")
_SmMlmResourceUsageMajflt_Type = Counter32
_SmMlmResourceUsageMajflt_Object = MibTableColumn
smMlmResourceUsageMajflt = _SmMlmResourceUsageMajflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 10),
    _SmMlmResourceUsageMajflt_Type()
)
smMlmResourceUsageMajflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageMajflt.setStatus("mandatory")
_SmMlmResourceUsageNSwap_Type = Counter32
_SmMlmResourceUsageNSwap_Object = MibTableColumn
smMlmResourceUsageNSwap = _SmMlmResourceUsageNSwap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 11),
    _SmMlmResourceUsageNSwap_Type()
)
smMlmResourceUsageNSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageNSwap.setStatus("mandatory")
_SmMlmResourceUsageInBlock_Type = Counter32
_SmMlmResourceUsageInBlock_Object = MibTableColumn
smMlmResourceUsageInBlock = _SmMlmResourceUsageInBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 12),
    _SmMlmResourceUsageInBlock_Type()
)
smMlmResourceUsageInBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageInBlock.setStatus("mandatory")
_SmMlmResourceUsageOutBlock_Type = Counter32
_SmMlmResourceUsageOutBlock_Object = MibTableColumn
smMlmResourceUsageOutBlock = _SmMlmResourceUsageOutBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 13),
    _SmMlmResourceUsageOutBlock_Type()
)
smMlmResourceUsageOutBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageOutBlock.setStatus("mandatory")
_SmMlmResourceUsageMsgsnd_Type = Counter32
_SmMlmResourceUsageMsgsnd_Object = MibTableColumn
smMlmResourceUsageMsgsnd = _SmMlmResourceUsageMsgsnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 14),
    _SmMlmResourceUsageMsgsnd_Type()
)
smMlmResourceUsageMsgsnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageMsgsnd.setStatus("mandatory")
_SmMlmResourceUsageMsgrcv_Type = Counter32
_SmMlmResourceUsageMsgrcv_Object = MibTableColumn
smMlmResourceUsageMsgrcv = _SmMlmResourceUsageMsgrcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 15),
    _SmMlmResourceUsageMsgrcv_Type()
)
smMlmResourceUsageMsgrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageMsgrcv.setStatus("mandatory")
_SmMlmResourceUsageNSignals_Type = Counter32
_SmMlmResourceUsageNSignals_Object = MibTableColumn
smMlmResourceUsageNSignals = _SmMlmResourceUsageNSignals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 16),
    _SmMlmResourceUsageNSignals_Type()
)
smMlmResourceUsageNSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageNSignals.setStatus("mandatory")
_SmMlmResourceUsageVcsw_Type = Counter32
_SmMlmResourceUsageVcsw_Object = MibTableColumn
smMlmResourceUsageVcsw = _SmMlmResourceUsageVcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 17),
    _SmMlmResourceUsageVcsw_Type()
)
smMlmResourceUsageVcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageVcsw.setStatus("mandatory")
_SmMlmResourceUsageIcsw_Type = Counter32
_SmMlmResourceUsageIcsw_Object = MibTableColumn
smMlmResourceUsageIcsw = _SmMlmResourceUsageIcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 2, 1, 1, 18),
    _SmMlmResourceUsageIcsw_Type()
)
smMlmResourceUsageIcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmResourceUsageIcsw.setStatus("mandatory")
_SmMlmProgramMessages_ObjectIdentity = ObjectIdentity
smMlmProgramMessages = _SmMlmProgramMessages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3)
)
_SmMlmProgramMessagesTable_Object = MibTable
smMlmProgramMessagesTable = _SmMlmProgramMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    smMlmProgramMessagesTable.setStatus("mandatory")
_SmMlmProgramMessagesEntry_Object = MibTableRow
smMlmProgramMessagesEntry = _SmMlmProgramMessagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1)
)
smMlmProgramMessagesEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmProgramMessagesRowNumber"),
)
if mibBuilder.loadTexts:
    smMlmProgramMessagesEntry.setStatus("mandatory")
_SmMlmProgramMessagesRowNumber_Type = Integer32
_SmMlmProgramMessagesRowNumber_Object = MibTableColumn
smMlmProgramMessagesRowNumber = _SmMlmProgramMessagesRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 1),
    _SmMlmProgramMessagesRowNumber_Type()
)
smMlmProgramMessagesRowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramMessagesRowNumber.setStatus("mandatory")
_SmMlmProgramMessagesTime_Type = DisplayString
_SmMlmProgramMessagesTime_Object = MibTableColumn
smMlmProgramMessagesTime = _SmMlmProgramMessagesTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 2),
    _SmMlmProgramMessagesTime_Type()
)
smMlmProgramMessagesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramMessagesTime.setStatus("mandatory")
_SmMlmProgramMessagesText_Type = DisplayString
_SmMlmProgramMessagesText_Object = MibTableColumn
smMlmProgramMessagesText = _SmMlmProgramMessagesText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 3),
    _SmMlmProgramMessagesText_Type()
)
smMlmProgramMessagesText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramMessagesText.setStatus("mandatory")
_SmMlmProgramMessagesTimeStamp_Type = Integer32
_SmMlmProgramMessagesTimeStamp_Object = MibTableColumn
smMlmProgramMessagesTimeStamp = _SmMlmProgramMessagesTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 1, 1, 4),
    _SmMlmProgramMessagesTimeStamp_Type()
)
smMlmProgramMessagesTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramMessagesTimeStamp.setStatus("mandatory")
_SmMlmProgramDataCollectTable_Object = MibTable
smMlmProgramDataCollectTable = _SmMlmProgramDataCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    smMlmProgramDataCollectTable.setStatus("mandatory")
_SmMlmProgramDataCollectEntry_Object = MibTableRow
smMlmProgramDataCollectEntry = _SmMlmProgramDataCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 2, 1)
)
smMlmProgramDataCollectEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmProgramDataCollectRowNumber"),
)
if mibBuilder.loadTexts:
    smMlmProgramDataCollectEntry.setStatus("mandatory")
_SmMlmProgramDataCollectRowNumber_Type = Integer32
_SmMlmProgramDataCollectRowNumber_Object = MibTableColumn
smMlmProgramDataCollectRowNumber = _SmMlmProgramDataCollectRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 2, 1, 1),
    _SmMlmProgramDataCollectRowNumber_Type()
)
smMlmProgramDataCollectRowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectRowNumber.setStatus("mandatory")
_SmMlmProgramDataCollectTime_Type = DisplayString
_SmMlmProgramDataCollectTime_Object = MibTableColumn
smMlmProgramDataCollectTime = _SmMlmProgramDataCollectTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 2, 1, 2),
    _SmMlmProgramDataCollectTime_Type()
)
smMlmProgramDataCollectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectTime.setStatus("mandatory")
_SmMlmProgramDataCollectText_Type = DisplayString
_SmMlmProgramDataCollectText_Object = MibTableColumn
smMlmProgramDataCollectText = _SmMlmProgramDataCollectText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 2, 1, 3),
    _SmMlmProgramDataCollectText_Type()
)
smMlmProgramDataCollectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectText.setStatus("mandatory")
_SmMlmProgramDataCollectTimeStamp_Type = Integer32
_SmMlmProgramDataCollectTimeStamp_Object = MibTableColumn
smMlmProgramDataCollectTimeStamp = _SmMlmProgramDataCollectTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 2, 1, 4),
    _SmMlmProgramDataCollectTimeStamp_Type()
)
smMlmProgramDataCollectTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramDataCollectTimeStamp.setStatus("mandatory")
_SmMlmProgramTrapTable_Object = MibTable
smMlmProgramTrapTable = _SmMlmProgramTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    smMlmProgramTrapTable.setStatus("mandatory")
_SmMlmProgramTrapEntry_Object = MibTableRow
smMlmProgramTrapEntry = _SmMlmProgramTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 3, 1)
)
smMlmProgramTrapEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmProgramTrapRowNumber"),
)
if mibBuilder.loadTexts:
    smMlmProgramTrapEntry.setStatus("mandatory")
_SmMlmProgramTrapRowNumber_Type = Integer32
_SmMlmProgramTrapRowNumber_Object = MibTableColumn
smMlmProgramTrapRowNumber = _SmMlmProgramTrapRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 3, 1, 1),
    _SmMlmProgramTrapRowNumber_Type()
)
smMlmProgramTrapRowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramTrapRowNumber.setStatus("mandatory")
_SmMlmProgramTrapTime_Type = DisplayString
_SmMlmProgramTrapTime_Object = MibTableColumn
smMlmProgramTrapTime = _SmMlmProgramTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 3, 1, 2),
    _SmMlmProgramTrapTime_Type()
)
smMlmProgramTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramTrapTime.setStatus("mandatory")
_SmMlmProgramTrapText_Type = DisplayString
_SmMlmProgramTrapText_Object = MibTableColumn
smMlmProgramTrapText = _SmMlmProgramTrapText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 3, 1, 3),
    _SmMlmProgramTrapText_Type()
)
smMlmProgramTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramTrapText.setStatus("mandatory")
_SmMlmProgramTrapTimeStamp_Type = Integer32
_SmMlmProgramTrapTimeStamp_Object = MibTableColumn
smMlmProgramTrapTimeStamp = _SmMlmProgramTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 3, 3, 1, 4),
    _SmMlmProgramTrapTimeStamp_Type()
)
smMlmProgramTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmProgramTrapTimeStamp.setStatus("mandatory")
_SmMlmProgramEnvironmentVars_ObjectIdentity = ObjectIdentity
smMlmProgramEnvironmentVars = _SmMlmProgramEnvironmentVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4)
)
_SmMlmProgramEnvHostAddress_Type = DisplayString
_SmMlmProgramEnvHostAddress_Object = MibScalar
smMlmProgramEnvHostAddress = _SmMlmProgramEnvHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 1),
    _SmMlmProgramEnvHostAddress_Type()
)
smMlmProgramEnvHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvHostAddress.setStatus("mandatory")
_SmMlmProgramEnvHostName_Type = DisplayString
_SmMlmProgramEnvHostName_Object = MibScalar
smMlmProgramEnvHostName = _SmMlmProgramEnvHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 2),
    _SmMlmProgramEnvHostName_Type()
)
smMlmProgramEnvHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvHostName.setStatus("mandatory")
_SmMlmProgramEnvHostDomainName_Type = DisplayString
_SmMlmProgramEnvHostDomainName_Object = MibScalar
smMlmProgramEnvHostDomainName = _SmMlmProgramEnvHostDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 3),
    _SmMlmProgramEnvHostDomainName_Type()
)
smMlmProgramEnvHostDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvHostDomainName.setStatus("mandatory")
_SmMlmProgramEnvTableVars_ObjectIdentity = ObjectIdentity
smMlmProgramEnvTableVars = _SmMlmProgramEnvTableVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4)
)
_SmMlmProgramEnvThresholdTableVars_ObjectIdentity = ObjectIdentity
smMlmProgramEnvThresholdTableVars = _SmMlmProgramEnvThresholdTableVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5)
)
_SmMlmProgramEnvThresholdName_Type = DisplayString
_SmMlmProgramEnvThresholdName_Object = MibScalar
smMlmProgramEnvThresholdName = _SmMlmProgramEnvThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 1),
    _SmMlmProgramEnvThresholdName_Type()
)
smMlmProgramEnvThresholdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdName.setStatus("mandatory")
_SmMlmProgramEnvThresholdArmState_Type = DisplayString
_SmMlmProgramEnvThresholdArmState_Object = MibScalar
smMlmProgramEnvThresholdArmState = _SmMlmProgramEnvThresholdArmState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 2),
    _SmMlmProgramEnvThresholdArmState_Type()
)
smMlmProgramEnvThresholdArmState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdArmState.setStatus("mandatory")
_SmMlmProgramEnvThresholdCondition_Type = DisplayString
_SmMlmProgramEnvThresholdCondition_Object = MibScalar
smMlmProgramEnvThresholdCondition = _SmMlmProgramEnvThresholdCondition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 3),
    _SmMlmProgramEnvThresholdCondition_Type()
)
smMlmProgramEnvThresholdCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdCondition.setStatus("mandatory")
_SmMlmProgramEnvThresholdValue_Type = DisplayString
_SmMlmProgramEnvThresholdValue_Object = MibScalar
smMlmProgramEnvThresholdValue = _SmMlmProgramEnvThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 4),
    _SmMlmProgramEnvThresholdValue_Type()
)
smMlmProgramEnvThresholdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdValue.setStatus("mandatory")
_SmMlmProgramEnvThresholdNode_Type = DisplayString
_SmMlmProgramEnvThresholdNode_Object = MibScalar
smMlmProgramEnvThresholdNode = _SmMlmProgramEnvThresholdNode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 5),
    _SmMlmProgramEnvThresholdNode_Type()
)
smMlmProgramEnvThresholdNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdNode.setStatus("mandatory")
_SmMlmProgramEnvThresholdProxy_Type = DisplayString
_SmMlmProgramEnvThresholdProxy_Object = MibScalar
smMlmProgramEnvThresholdProxy = _SmMlmProgramEnvThresholdProxy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 6),
    _SmMlmProgramEnvThresholdProxy_Type()
)
smMlmProgramEnvThresholdProxy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdProxy.setStatus("mandatory")
_SmMlmProgramEnvThresholdAddressNode_Type = DisplayString
_SmMlmProgramEnvThresholdAddressNode_Object = MibScalar
smMlmProgramEnvThresholdAddressNode = _SmMlmProgramEnvThresholdAddressNode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 7),
    _SmMlmProgramEnvThresholdAddressNode_Type()
)
smMlmProgramEnvThresholdAddressNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdAddressNode.setStatus("mandatory")
_SmMlmProgramEnvThresholdDomainName_Type = DisplayString
_SmMlmProgramEnvThresholdDomainName_Object = MibScalar
smMlmProgramEnvThresholdDomainName = _SmMlmProgramEnvThresholdDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 8),
    _SmMlmProgramEnvThresholdDomainName_Type()
)
smMlmProgramEnvThresholdDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdDomainName.setStatus("mandatory")
_SmMlmProgramEnvThresholdPort_Type = Integer32
_SmMlmProgramEnvThresholdPort_Object = MibScalar
smMlmProgramEnvThresholdPort = _SmMlmProgramEnvThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 9),
    _SmMlmProgramEnvThresholdPort_Type()
)
smMlmProgramEnvThresholdPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdPort.setStatus("mandatory")
_SmMlmProgramEnvThresholdVarId_Type = DisplayString
_SmMlmProgramEnvThresholdVarId_Object = MibScalar
smMlmProgramEnvThresholdVarId = _SmMlmProgramEnvThresholdVarId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 10),
    _SmMlmProgramEnvThresholdVarId_Type()
)
smMlmProgramEnvThresholdVarId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdVarId.setStatus("mandatory")
_SmMlmProgramEnvThresholdVarType_Type = DisplayString
_SmMlmProgramEnvThresholdVarType_Object = MibScalar
smMlmProgramEnvThresholdVarType = _SmMlmProgramEnvThresholdVarType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 11),
    _SmMlmProgramEnvThresholdVarType_Type()
)
smMlmProgramEnvThresholdVarType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdVarType.setStatus("mandatory")
_SmMlmProgramEnvThresholdVarValue_Type = DisplayString
_SmMlmProgramEnvThresholdVarValue_Object = MibScalar
smMlmProgramEnvThresholdVarValue = _SmMlmProgramEnvThresholdVarValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 12),
    _SmMlmProgramEnvThresholdVarValue_Type()
)
smMlmProgramEnvThresholdVarValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdVarValue.setStatus("mandatory")
_SmMlmProgramEnvThresholdSeverity_Type = DisplayString
_SmMlmProgramEnvThresholdSeverity_Object = MibScalar
smMlmProgramEnvThresholdSeverity = _SmMlmProgramEnvThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 13),
    _SmMlmProgramEnvThresholdSeverity_Type()
)
smMlmProgramEnvThresholdSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdSeverity.setStatus("mandatory")
_SmMlmProgramEnvThresholdVarInstance_Type = DisplayString
_SmMlmProgramEnvThresholdVarInstance_Object = MibScalar
smMlmProgramEnvThresholdVarInstance = _SmMlmProgramEnvThresholdVarInstance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 1, 4, 4, 5, 14),
    _SmMlmProgramEnvThresholdVarInstance_Type()
)
smMlmProgramEnvThresholdVarInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smMlmProgramEnvThresholdVarInstance.setStatus("mandatory")
_SmMlmNetworkInformation_ObjectIdentity = ObjectIdentity
smMlmNetworkInformation = _SmMlmNetworkInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3)
)
_SmMlmNetworkSessionInformation_ObjectIdentity = ObjectIdentity
smMlmNetworkSessionInformation = _SmMlmNetworkSessionInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1)
)
_SmMlmNetworkSessionCount_Type = Integer32
_SmMlmNetworkSessionCount_Object = MibScalar
smMlmNetworkSessionCount = _SmMlmNetworkSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 1),
    _SmMlmNetworkSessionCount_Type()
)
smMlmNetworkSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionCount.setStatus("mandatory")
_SmMlmNetworkSessionTable_Object = MibTable
smMlmNetworkSessionTable = _SmMlmNetworkSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2)
)
if mibBuilder.loadTexts:
    smMlmNetworkSessionTable.setStatus("mandatory")
_SmMlmNetworkSessionEntry_Object = MibTableRow
smMlmNetworkSessionEntry = _SmMlmNetworkSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1)
)
smMlmNetworkSessionEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmNetworkSessionName"),
)
if mibBuilder.loadTexts:
    smMlmNetworkSessionEntry.setStatus("mandatory")
_SmMlmNetworkSessionName_Type = DisplayString
_SmMlmNetworkSessionName_Object = MibTableColumn
smMlmNetworkSessionName = _SmMlmNetworkSessionName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 1),
    _SmMlmNetworkSessionName_Type()
)
smMlmNetworkSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionName.setStatus("mandatory")


class _SmMlmNetworkSessionCurrentState_Type(Integer32):
    """Custom type smMlmNetworkSessionCurrentState based on Integer32"""
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


_SmMlmNetworkSessionCurrentState_Type.__name__ = "Integer32"
_SmMlmNetworkSessionCurrentState_Object = MibTableColumn
smMlmNetworkSessionCurrentState = _SmMlmNetworkSessionCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 2),
    _SmMlmNetworkSessionCurrentState_Type()
)
smMlmNetworkSessionCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionCurrentState.setStatus("mandatory")
_SmMlmNetworkSessionLastStateChange_Type = DisplayString
_SmMlmNetworkSessionLastStateChange_Object = MibTableColumn
smMlmNetworkSessionLastStateChange = _SmMlmNetworkSessionLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 3),
    _SmMlmNetworkSessionLastStateChange_Type()
)
smMlmNetworkSessionLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionLastStateChange.setStatus("mandatory")
_SmMlmNetworkSessionLastPollAttempt_Type = DisplayString
_SmMlmNetworkSessionLastPollAttempt_Object = MibTableColumn
smMlmNetworkSessionLastPollAttempt = _SmMlmNetworkSessionLastPollAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 4),
    _SmMlmNetworkSessionLastPollAttempt_Type()
)
smMlmNetworkSessionLastPollAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionLastPollAttempt.setStatus("mandatory")


class _SmMlmNetworkSessionAddressFamily_Type(Integer32):
    """Custom type smMlmNetworkSessionAddressFamily based on Integer32"""
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


_SmMlmNetworkSessionAddressFamily_Type.__name__ = "Integer32"
_SmMlmNetworkSessionAddressFamily_Object = MibTableColumn
smMlmNetworkSessionAddressFamily = _SmMlmNetworkSessionAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 5),
    _SmMlmNetworkSessionAddressFamily_Type()
)
smMlmNetworkSessionAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionAddressFamily.setStatus("mandatory")
_SmMlmNetworkSessionNetAddress_Type = DisplayString
_SmMlmNetworkSessionNetAddress_Object = MibTableColumn
smMlmNetworkSessionNetAddress = _SmMlmNetworkSessionNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 6),
    _SmMlmNetworkSessionNetAddress_Type()
)
smMlmNetworkSessionNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionNetAddress.setStatus("mandatory")
_SmMlmNetworkSessionTransmitAttempts_Type = Counter32
_SmMlmNetworkSessionTransmitAttempts_Object = MibTableColumn
smMlmNetworkSessionTransmitAttempts = _SmMlmNetworkSessionTransmitAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 7),
    _SmMlmNetworkSessionTransmitAttempts_Type()
)
smMlmNetworkSessionTransmitAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionTransmitAttempts.setStatus("mandatory")
_SmMlmNetworkSessionPacketsReceived_Type = Counter32
_SmMlmNetworkSessionPacketsReceived_Object = MibTableColumn
smMlmNetworkSessionPacketsReceived = _SmMlmNetworkSessionPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 8),
    _SmMlmNetworkSessionPacketsReceived_Type()
)
smMlmNetworkSessionPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionPacketsReceived.setStatus("mandatory")
_SmMlmNetworkSessionLastTransmitTime_Type = DisplayString
_SmMlmNetworkSessionLastTransmitTime_Object = MibTableColumn
smMlmNetworkSessionLastTransmitTime = _SmMlmNetworkSessionLastTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 9),
    _SmMlmNetworkSessionLastTransmitTime_Type()
)
smMlmNetworkSessionLastTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionLastTransmitTime.setStatus("mandatory")
_SmMlmNetworkSessionLastReceiveTime_Type = DisplayString
_SmMlmNetworkSessionLastReceiveTime_Object = MibTableColumn
smMlmNetworkSessionLastReceiveTime = _SmMlmNetworkSessionLastReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 10),
    _SmMlmNetworkSessionLastReceiveTime_Type()
)
smMlmNetworkSessionLastReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionLastReceiveTime.setStatus("mandatory")
_SmMlmNetworkSessionMinimumResponseTime_Type = Integer32
_SmMlmNetworkSessionMinimumResponseTime_Object = MibTableColumn
smMlmNetworkSessionMinimumResponseTime = _SmMlmNetworkSessionMinimumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 11),
    _SmMlmNetworkSessionMinimumResponseTime_Type()
)
smMlmNetworkSessionMinimumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionMinimumResponseTime.setStatus("mandatory")
_SmMlmNetworkSessionRecentAverageResponseTime_Type = Integer32
_SmMlmNetworkSessionRecentAverageResponseTime_Object = MibTableColumn
smMlmNetworkSessionRecentAverageResponseTime = _SmMlmNetworkSessionRecentAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 12),
    _SmMlmNetworkSessionRecentAverageResponseTime_Type()
)
smMlmNetworkSessionRecentAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionRecentAverageResponseTime.setStatus("mandatory")
_SmMlmNetworkSessionLifeTimeAverageResponseTime_Type = Integer32
_SmMlmNetworkSessionLifeTimeAverageResponseTime_Object = MibTableColumn
smMlmNetworkSessionLifeTimeAverageResponseTime = _SmMlmNetworkSessionLifeTimeAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 13),
    _SmMlmNetworkSessionLifeTimeAverageResponseTime_Type()
)
smMlmNetworkSessionLifeTimeAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionLifeTimeAverageResponseTime.setStatus("mandatory")
_SmMlmNetworkSessionMaximumResponseTime_Type = Integer32
_SmMlmNetworkSessionMaximumResponseTime_Object = MibTableColumn
smMlmNetworkSessionMaximumResponseTime = _SmMlmNetworkSessionMaximumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 14),
    _SmMlmNetworkSessionMaximumResponseTime_Type()
)
smMlmNetworkSessionMaximumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionMaximumResponseTime.setStatus("mandatory")
_SmMlmNetworkSessionMinimumResponseTimeStamp_Type = DisplayString
_SmMlmNetworkSessionMinimumResponseTimeStamp_Object = MibTableColumn
smMlmNetworkSessionMinimumResponseTimeStamp = _SmMlmNetworkSessionMinimumResponseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 15),
    _SmMlmNetworkSessionMinimumResponseTimeStamp_Type()
)
smMlmNetworkSessionMinimumResponseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionMinimumResponseTimeStamp.setStatus("mandatory")
_SmMlmNetworkSessionMaximumResponseTimeStamp_Type = DisplayString
_SmMlmNetworkSessionMaximumResponseTimeStamp_Object = MibTableColumn
smMlmNetworkSessionMaximumResponseTimeStamp = _SmMlmNetworkSessionMaximumResponseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 16),
    _SmMlmNetworkSessionMaximumResponseTimeStamp_Type()
)
smMlmNetworkSessionMaximumResponseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionMaximumResponseTimeStamp.setStatus("mandatory")
_SmMlmNetworkSessionProxyAddress_Type = DisplayString
_SmMlmNetworkSessionProxyAddress_Object = MibTableColumn
smMlmNetworkSessionProxyAddress = _SmMlmNetworkSessionProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 17),
    _SmMlmNetworkSessionProxyAddress_Type()
)
smMlmNetworkSessionProxyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionProxyAddress.setStatus("mandatory")
_SmMlmNetworkSessionPort_Type = Integer32
_SmMlmNetworkSessionPort_Object = MibTableColumn
smMlmNetworkSessionPort = _SmMlmNetworkSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 18),
    _SmMlmNetworkSessionPort_Type()
)
smMlmNetworkSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionPort.setStatus("mandatory")
_SmMlmNetworkSessionDomainName_Type = DisplayString
_SmMlmNetworkSessionDomainName_Object = MibTableColumn
smMlmNetworkSessionDomainName = _SmMlmNetworkSessionDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 1, 2, 1, 19),
    _SmMlmNetworkSessionDomainName_Type()
)
smMlmNetworkSessionDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkSessionDomainName.setStatus("mandatory")
_SmMlmNetworkIfStatusInformation_ObjectIdentity = ObjectIdentity
smMlmNetworkIfStatusInformation = _SmMlmNetworkIfStatusInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2)
)
_SmMlmNetworkIfStatusTable_Object = MibTable
smMlmNetworkIfStatusTable = _SmMlmNetworkIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusTable.setStatus("mandatory")
_SmMlmNetworkIfStatusEntry_Object = MibTableRow
smMlmNetworkIfStatusEntry = _SmMlmNetworkIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1)
)
smMlmNetworkIfStatusEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmNetworkIfStatusAddressFamily"),
    (0, "MIDLEVELMGR-MIB", "smMlmNetworkIfStatusRawNetAddress"),
)
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusEntry.setStatus("mandatory")


class _SmMlmNetworkIfStatusAddressFamily_Type(Integer32):
    """Custom type smMlmNetworkIfStatusAddressFamily based on Integer32"""
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


_SmMlmNetworkIfStatusAddressFamily_Type.__name__ = "Integer32"
_SmMlmNetworkIfStatusAddressFamily_Object = MibTableColumn
smMlmNetworkIfStatusAddressFamily = _SmMlmNetworkIfStatusAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 1),
    _SmMlmNetworkIfStatusAddressFamily_Type()
)
smMlmNetworkIfStatusAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusAddressFamily.setStatus("mandatory")
_SmMlmNetworkIfStatusRawNetAddress_Type = OctetString
_SmMlmNetworkIfStatusRawNetAddress_Object = MibTableColumn
smMlmNetworkIfStatusRawNetAddress = _SmMlmNetworkIfStatusRawNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 2),
    _SmMlmNetworkIfStatusRawNetAddress_Type()
)
smMlmNetworkIfStatusRawNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusRawNetAddress.setStatus("mandatory")
_SmMlmNetworkIfStatusNetAddress_Type = DisplayString
_SmMlmNetworkIfStatusNetAddress_Object = MibTableColumn
smMlmNetworkIfStatusNetAddress = _SmMlmNetworkIfStatusNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 3),
    _SmMlmNetworkIfStatusNetAddress_Type()
)
smMlmNetworkIfStatusNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusNetAddress.setStatus("mandatory")
_SmMlmNetworkIfStatusHostName_Type = DisplayString
_SmMlmNetworkIfStatusHostName_Object = MibTableColumn
smMlmNetworkIfStatusHostName = _SmMlmNetworkIfStatusHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 4),
    _SmMlmNetworkIfStatusHostName_Type()
)
smMlmNetworkIfStatusHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusHostName.setStatus("mandatory")
_SmMlmNetworkIfStatusMonitorEntryName_Type = DisplayString
_SmMlmNetworkIfStatusMonitorEntryName_Object = MibTableColumn
smMlmNetworkIfStatusMonitorEntryName = _SmMlmNetworkIfStatusMonitorEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 5),
    _SmMlmNetworkIfStatusMonitorEntryName_Type()
)
smMlmNetworkIfStatusMonitorEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusMonitorEntryName.setStatus("mandatory")
_SmMlmNetworkIfStatusMonitorFrequency_Type = DisplayString
_SmMlmNetworkIfStatusMonitorFrequency_Object = MibTableColumn
smMlmNetworkIfStatusMonitorFrequency = _SmMlmNetworkIfStatusMonitorFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 6),
    _SmMlmNetworkIfStatusMonitorFrequency_Type()
)
smMlmNetworkIfStatusMonitorFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusMonitorFrequency.setStatus("mandatory")


class _SmMlmNetworkIfStatusCurrentState_Type(Integer32):
    """Custom type smMlmNetworkIfStatusCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 1),
          ("up", 3))
    )


_SmMlmNetworkIfStatusCurrentState_Type.__name__ = "Integer32"
_SmMlmNetworkIfStatusCurrentState_Object = MibTableColumn
smMlmNetworkIfStatusCurrentState = _SmMlmNetworkIfStatusCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 7),
    _SmMlmNetworkIfStatusCurrentState_Type()
)
smMlmNetworkIfStatusCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusCurrentState.setStatus("mandatory")
_SmMlmNetworkIfStatusLastStateChange_Type = DisplayString
_SmMlmNetworkIfStatusLastStateChange_Object = MibTableColumn
smMlmNetworkIfStatusLastStateChange = _SmMlmNetworkIfStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 8),
    _SmMlmNetworkIfStatusLastStateChange_Type()
)
smMlmNetworkIfStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusLastStateChange.setStatus("mandatory")
_SmMlmNetworkIfStatusLastStatusCheck_Type = DisplayString
_SmMlmNetworkIfStatusLastStatusCheck_Object = MibTableColumn
smMlmNetworkIfStatusLastStatusCheck = _SmMlmNetworkIfStatusLastStatusCheck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 9),
    _SmMlmNetworkIfStatusLastStatusCheck_Type()
)
smMlmNetworkIfStatusLastStatusCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusLastStatusCheck.setStatus("mandatory")
_SmMlmNetworkIfStatusLastResponseTime_Type = DisplayString
_SmMlmNetworkIfStatusLastResponseTime_Object = MibTableColumn
smMlmNetworkIfStatusLastResponseTime = _SmMlmNetworkIfStatusLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 10),
    _SmMlmNetworkIfStatusLastResponseTime_Type()
)
smMlmNetworkIfStatusLastResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusLastResponseTime.setStatus("mandatory")


class _SmMlmNetworkIfStatusResetRoundTripStats_Type(Integer32):
    """Custom type smMlmNetworkIfStatusResetRoundTripStats based on Integer32"""
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


_SmMlmNetworkIfStatusResetRoundTripStats_Type.__name__ = "Integer32"
_SmMlmNetworkIfStatusResetRoundTripStats_Object = MibTableColumn
smMlmNetworkIfStatusResetRoundTripStats = _SmMlmNetworkIfStatusResetRoundTripStats_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 11),
    _SmMlmNetworkIfStatusResetRoundTripStats_Type()
)
smMlmNetworkIfStatusResetRoundTripStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusResetRoundTripStats.setStatus("mandatory")
_SmMlmNetworkIfStatusNumRequestsTransmitted_Type = Counter32
_SmMlmNetworkIfStatusNumRequestsTransmitted_Object = MibTableColumn
smMlmNetworkIfStatusNumRequestsTransmitted = _SmMlmNetworkIfStatusNumRequestsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 12),
    _SmMlmNetworkIfStatusNumRequestsTransmitted_Type()
)
smMlmNetworkIfStatusNumRequestsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusNumRequestsTransmitted.setStatus("mandatory")
_SmMlmNetworkIfStatusNumResponsesReceived_Type = Counter32
_SmMlmNetworkIfStatusNumResponsesReceived_Object = MibTableColumn
smMlmNetworkIfStatusNumResponsesReceived = _SmMlmNetworkIfStatusNumResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 13),
    _SmMlmNetworkIfStatusNumResponsesReceived_Type()
)
smMlmNetworkIfStatusNumResponsesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusNumResponsesReceived.setStatus("mandatory")
_SmMlmNetworkIfStatusLastRoundTripTime_Type = TimeTicks
_SmMlmNetworkIfStatusLastRoundTripTime_Object = MibTableColumn
smMlmNetworkIfStatusLastRoundTripTime = _SmMlmNetworkIfStatusLastRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 14),
    _SmMlmNetworkIfStatusLastRoundTripTime_Type()
)
smMlmNetworkIfStatusLastRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusLastRoundTripTime.setStatus("mandatory")
_SmMlmNetworkIfStatusAvgRoundTripTime_Type = TimeTicks
_SmMlmNetworkIfStatusAvgRoundTripTime_Object = MibTableColumn
smMlmNetworkIfStatusAvgRoundTripTime = _SmMlmNetworkIfStatusAvgRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 15),
    _SmMlmNetworkIfStatusAvgRoundTripTime_Type()
)
smMlmNetworkIfStatusAvgRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusAvgRoundTripTime.setStatus("mandatory")
_SmMlmNetworkIfStatusMinRoundTripTime_Type = TimeTicks
_SmMlmNetworkIfStatusMinRoundTripTime_Object = MibTableColumn
smMlmNetworkIfStatusMinRoundTripTime = _SmMlmNetworkIfStatusMinRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 16),
    _SmMlmNetworkIfStatusMinRoundTripTime_Type()
)
smMlmNetworkIfStatusMinRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusMinRoundTripTime.setStatus("mandatory")
_SmMlmNetworkIfStatusMinRoundTripTimeStamp_Type = DisplayString
_SmMlmNetworkIfStatusMinRoundTripTimeStamp_Object = MibTableColumn
smMlmNetworkIfStatusMinRoundTripTimeStamp = _SmMlmNetworkIfStatusMinRoundTripTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 17),
    _SmMlmNetworkIfStatusMinRoundTripTimeStamp_Type()
)
smMlmNetworkIfStatusMinRoundTripTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusMinRoundTripTimeStamp.setStatus("mandatory")
_SmMlmNetworkIfStatusMaxRoundTripTime_Type = TimeTicks
_SmMlmNetworkIfStatusMaxRoundTripTime_Object = MibTableColumn
smMlmNetworkIfStatusMaxRoundTripTime = _SmMlmNetworkIfStatusMaxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 18),
    _SmMlmNetworkIfStatusMaxRoundTripTime_Type()
)
smMlmNetworkIfStatusMaxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusMaxRoundTripTime.setStatus("mandatory")
_SmMlmNetworkIfStatusMaxRoundTripTimeStamp_Type = DisplayString
_SmMlmNetworkIfStatusMaxRoundTripTimeStamp_Object = MibTableColumn
smMlmNetworkIfStatusMaxRoundTripTimeStamp = _SmMlmNetworkIfStatusMaxRoundTripTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 19),
    _SmMlmNetworkIfStatusMaxRoundTripTimeStamp_Type()
)
smMlmNetworkIfStatusMaxRoundTripTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusMaxRoundTripTimeStamp.setStatus("mandatory")
_SmMlmNetworkIfStatusLastUp_Type = DisplayString
_SmMlmNetworkIfStatusLastUp_Object = MibTableColumn
smMlmNetworkIfStatusLastUp = _SmMlmNetworkIfStatusLastUp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 20),
    _SmMlmNetworkIfStatusLastUp_Type()
)
smMlmNetworkIfStatusLastUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusLastUp.setStatus("mandatory")
_SmMlmNetworkIfStatusLastDown_Type = DisplayString
_SmMlmNetworkIfStatusLastDown_Object = MibTableColumn
smMlmNetworkIfStatusLastDown = _SmMlmNetworkIfStatusLastDown_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 3, 2, 1, 1, 21),
    _SmMlmNetworkIfStatusLastDown_Type()
)
smMlmNetworkIfStatusLastDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmNetworkIfStatusLastDown.setStatus("mandatory")
_SmMlmThreshold_ObjectIdentity = ObjectIdentity
smMlmThreshold = _SmMlmThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5)
)
_SmMlmThresholdTable_Object = MibTable
smMlmThresholdTable = _SmMlmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1)
)
if mibBuilder.loadTexts:
    smMlmThresholdTable.setStatus("mandatory")
_SmMlmThresholdEntry_Object = MibTableRow
smMlmThresholdEntry = _SmMlmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1)
)
smMlmThresholdEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdName"),
)
if mibBuilder.loadTexts:
    smMlmThresholdEntry.setStatus("mandatory")


class _SmMlmThresholdState_Type(Integer32):
    """Custom type smMlmThresholdState based on Integer32"""
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


_SmMlmThresholdState_Type.__name__ = "Integer32"
_SmMlmThresholdState_Object = MibTableColumn
smMlmThresholdState = _SmMlmThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 1),
    _SmMlmThresholdState_Type()
)
smMlmThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdState.setStatus("mandatory")
_SmMlmThresholdName_Type = DisplayString
_SmMlmThresholdName_Object = MibTableColumn
smMlmThresholdName = _SmMlmThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 2),
    _SmMlmThresholdName_Type()
)
smMlmThresholdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdName.setStatus("mandatory")
_SmMlmThresholdDescription_Type = DisplayString
_SmMlmThresholdDescription_Object = MibTableColumn
smMlmThresholdDescription = _SmMlmThresholdDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 3),
    _SmMlmThresholdDescription_Type()
)
smMlmThresholdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdDescription.setStatus("mandatory")
_SmMlmThresholdOwnerID_Type = DisplayString
_SmMlmThresholdOwnerID_Object = MibTableColumn
smMlmThresholdOwnerID = _SmMlmThresholdOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 4),
    _SmMlmThresholdOwnerID_Type()
)
smMlmThresholdOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdOwnerID.setStatus("mandatory")
_SmMlmThresholdLocalRemoteMIBVariable_Type = DisplayString
_SmMlmThresholdLocalRemoteMIBVariable_Object = MibTableColumn
smMlmThresholdLocalRemoteMIBVariable = _SmMlmThresholdLocalRemoteMIBVariable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 5),
    _SmMlmThresholdLocalRemoteMIBVariable_Type()
)
smMlmThresholdLocalRemoteMIBVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdLocalRemoteMIBVariable.setStatus("mandatory")
_SmMlmThresholdCondition_Type = DisplayString
_SmMlmThresholdCondition_Object = MibTableColumn
smMlmThresholdCondition = _SmMlmThresholdCondition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 6),
    _SmMlmThresholdCondition_Type()
)
smMlmThresholdCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdCondition.setStatus("mandatory")
_SmMlmThresholdValue_Type = DisplayString
_SmMlmThresholdValue_Object = MibTableColumn
smMlmThresholdValue = _SmMlmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 7),
    _SmMlmThresholdValue_Type()
)
smMlmThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdValue.setStatus("mandatory")
_SmMlmThresholdPollTime_Type = DisplayString
_SmMlmThresholdPollTime_Object = MibTableColumn
smMlmThresholdPollTime = _SmMlmThresholdPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 8),
    _SmMlmThresholdPollTime_Type()
)
smMlmThresholdPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdPollTime.setStatus("mandatory")
_SmMlmThresholdLastValue_Type = DisplayString
_SmMlmThresholdLastValue_Object = MibTableColumn
smMlmThresholdLastValue = _SmMlmThresholdLastValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 9),
    _SmMlmThresholdLastValue_Type()
)
smMlmThresholdLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdLastValue.setStatus("mandatory")
_SmMlmThresholdIntegerDataMax_Type = Integer32
_SmMlmThresholdIntegerDataMax_Object = MibTableColumn
smMlmThresholdIntegerDataMax = _SmMlmThresholdIntegerDataMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 10),
    _SmMlmThresholdIntegerDataMax_Type()
)
smMlmThresholdIntegerDataMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdIntegerDataMax.setStatus("obsolete")
_SmMlmThresholdIntegerDataMin_Type = Integer32
_SmMlmThresholdIntegerDataMin_Object = MibTableColumn
smMlmThresholdIntegerDataMin = _SmMlmThresholdIntegerDataMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 11),
    _SmMlmThresholdIntegerDataMin_Type()
)
smMlmThresholdIntegerDataMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdIntegerDataMin.setStatus("obsolete")
_SmMlmThresholdIntegerDataAvg_Type = Integer32
_SmMlmThresholdIntegerDataAvg_Object = MibTableColumn
smMlmThresholdIntegerDataAvg = _SmMlmThresholdIntegerDataAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 12),
    _SmMlmThresholdIntegerDataAvg_Type()
)
smMlmThresholdIntegerDataAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdIntegerDataAvg.setStatus("obsolete")


class _SmMlmThresholdArmSeverity_Type(Integer32):
    """Custom type smMlmThresholdArmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmThresholdArmSeverity_Type.__name__ = "Integer32"
_SmMlmThresholdArmSeverity_Object = MibTableColumn
smMlmThresholdArmSeverity = _SmMlmThresholdArmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 13),
    _SmMlmThresholdArmSeverity_Type()
)
smMlmThresholdArmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdArmSeverity.setStatus("mandatory")


class _SmMlmThresholdReArmSeverity_Type(Integer32):
    """Custom type smMlmThresholdReArmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmThresholdReArmSeverity_Type.__name__ = "Integer32"
_SmMlmThresholdReArmSeverity_Object = MibTableColumn
smMlmThresholdReArmSeverity = _SmMlmThresholdReArmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 14),
    _SmMlmThresholdReArmSeverity_Type()
)
smMlmThresholdReArmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmSeverity.setStatus("mandatory")


class _SmMlmThresholdResultIndex_Type(Integer32):
    """Custom type smMlmThresholdResultIndex based on Integer32"""
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


_SmMlmThresholdResultIndex_Type.__name__ = "Integer32"
_SmMlmThresholdResultIndex_Object = MibTableColumn
smMlmThresholdResultIndex = _SmMlmThresholdResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 15),
    _SmMlmThresholdResultIndex_Type()
)
smMlmThresholdResultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdResultIndex.setStatus("mandatory")


class _SmMlmThresholdResultsTableState_Type(Integer32):
    """Custom type smMlmThresholdResultsTableState based on Integer32"""
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


_SmMlmThresholdResultsTableState_Type.__name__ = "Integer32"
_SmMlmThresholdResultsTableState_Object = MibTableColumn
smMlmThresholdResultsTableState = _SmMlmThresholdResultsTableState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 16),
    _SmMlmThresholdResultsTableState_Type()
)
smMlmThresholdResultsTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdResultsTableState.setStatus("mandatory")
_SmMlmThresholdTrapDescription_Type = DisplayString
_SmMlmThresholdTrapDescription_Object = MibTableColumn
smMlmThresholdTrapDescription = _SmMlmThresholdTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 17),
    _SmMlmThresholdTrapDescription_Type()
)
smMlmThresholdTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdTrapDescription.setStatus("mandatory")
_SmMlmThresholdArmEnterprise_Type = DisplayString
_SmMlmThresholdArmEnterprise_Object = MibTableColumn
smMlmThresholdArmEnterprise = _SmMlmThresholdArmEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 18),
    _SmMlmThresholdArmEnterprise_Type()
)
smMlmThresholdArmEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdArmEnterprise.setStatus("mandatory")
_SmMlmThresholdSpecificTrap_Type = Integer32
_SmMlmThresholdSpecificTrap_Object = MibTableColumn
smMlmThresholdSpecificTrap = _SmMlmThresholdSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 19),
    _SmMlmThresholdSpecificTrap_Type()
)
smMlmThresholdSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdSpecificTrap.setStatus("mandatory")
_SmMlmThresholdCommandToExecute_Type = DisplayString
_SmMlmThresholdCommandToExecute_Object = MibTableColumn
smMlmThresholdCommandToExecute = _SmMlmThresholdCommandToExecute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 20),
    _SmMlmThresholdCommandToExecute_Type()
)
smMlmThresholdCommandToExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdCommandToExecute.setStatus("mandatory")
_SmMlmThresholdReArmCondition_Type = DisplayString
_SmMlmThresholdReArmCondition_Object = MibTableColumn
smMlmThresholdReArmCondition = _SmMlmThresholdReArmCondition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 21),
    _SmMlmThresholdReArmCondition_Type()
)
smMlmThresholdReArmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmCondition.setStatus("mandatory")
_SmMlmThresholdReArmValue_Type = DisplayString
_SmMlmThresholdReArmValue_Object = MibTableColumn
smMlmThresholdReArmValue = _SmMlmThresholdReArmValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 22),
    _SmMlmThresholdReArmValue_Type()
)
smMlmThresholdReArmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmValue.setStatus("mandatory")
_SmMlmThresholdReArmTrapDescription_Type = DisplayString
_SmMlmThresholdReArmTrapDescription_Object = MibTableColumn
smMlmThresholdReArmTrapDescription = _SmMlmThresholdReArmTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 23),
    _SmMlmThresholdReArmTrapDescription_Type()
)
smMlmThresholdReArmTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmTrapDescription.setStatus("mandatory")
_SmMlmThresholdReArmEnterprise_Type = DisplayString
_SmMlmThresholdReArmEnterprise_Object = MibTableColumn
smMlmThresholdReArmEnterprise = _SmMlmThresholdReArmEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 24),
    _SmMlmThresholdReArmEnterprise_Type()
)
smMlmThresholdReArmEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmEnterprise.setStatus("mandatory")
_SmMlmThresholdReArmSpecificTrap_Type = Integer32
_SmMlmThresholdReArmSpecificTrap_Object = MibTableColumn
smMlmThresholdReArmSpecificTrap = _SmMlmThresholdReArmSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 25),
    _SmMlmThresholdReArmSpecificTrap_Type()
)
smMlmThresholdReArmSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmSpecificTrap.setStatus("mandatory")
_SmMlmThresholdReArmCommandToExecute_Type = DisplayString
_SmMlmThresholdReArmCommandToExecute_Object = MibTableColumn
smMlmThresholdReArmCommandToExecute = _SmMlmThresholdReArmCommandToExecute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 26),
    _SmMlmThresholdReArmCommandToExecute_Type()
)
smMlmThresholdReArmCommandToExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdReArmCommandToExecute.setStatus("mandatory")
_SmMlmThresholdLastChangedSession_Type = DisplayString
_SmMlmThresholdLastChangedSession_Object = MibTableColumn
smMlmThresholdLastChangedSession = _SmMlmThresholdLastChangedSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 27),
    _SmMlmThresholdLastChangedSession_Type()
)
smMlmThresholdLastChangedSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdLastChangedSession.setStatus("mandatory")
_SmMlmThresholdStandardError_Type = DisplayString
_SmMlmThresholdStandardError_Object = MibTableColumn
smMlmThresholdStandardError = _SmMlmThresholdStandardError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 28),
    _SmMlmThresholdStandardError_Type()
)
smMlmThresholdStandardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdStandardError.setStatus("mandatory")
_SmMlmThresholdLastResponseTime_Type = DisplayString
_SmMlmThresholdLastResponseTime_Object = MibTableColumn
smMlmThresholdLastResponseTime = _SmMlmThresholdLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 29),
    _SmMlmThresholdLastResponseTime_Type()
)
smMlmThresholdLastResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdLastResponseTime.setStatus("mandatory")
_SmMlmThresholdResponseCount_Type = Counter32
_SmMlmThresholdResponseCount_Object = MibTableColumn
smMlmThresholdResponseCount = _SmMlmThresholdResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 30),
    _SmMlmThresholdResponseCount_Type()
)
smMlmThresholdResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResponseCount.setStatus("mandatory")
_SmMlmThresholdTimeoutCount_Type = Counter32
_SmMlmThresholdTimeoutCount_Object = MibTableColumn
smMlmThresholdTimeoutCount = _SmMlmThresholdTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 31),
    _SmMlmThresholdTimeoutCount_Type()
)
smMlmThresholdTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdTimeoutCount.setStatus("mandatory")
_SmMlmThresholdNoValueCount_Type = Counter32
_SmMlmThresholdNoValueCount_Object = MibTableColumn
smMlmThresholdNoValueCount = _SmMlmThresholdNoValueCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 32),
    _SmMlmThresholdNoValueCount_Type()
)
smMlmThresholdNoValueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdNoValueCount.setStatus("mandatory")
_SmMlmThresholdArmConditionMetCount_Type = Counter32
_SmMlmThresholdArmConditionMetCount_Object = MibTableColumn
smMlmThresholdArmConditionMetCount = _SmMlmThresholdArmConditionMetCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 33),
    _SmMlmThresholdArmConditionMetCount_Type()
)
smMlmThresholdArmConditionMetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdArmConditionMetCount.setStatus("mandatory")
_SmMlmThresholdReArmConditionMetCount_Type = Counter32
_SmMlmThresholdReArmConditionMetCount_Object = MibTableColumn
smMlmThresholdReArmConditionMetCount = _SmMlmThresholdReArmConditionMetCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 34),
    _SmMlmThresholdReArmConditionMetCount_Type()
)
smMlmThresholdReArmConditionMetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdReArmConditionMetCount.setStatus("mandatory")


class _SmMlmThresholdThrottleArmCount_Type(Integer32):
    """Custom type smMlmThresholdThrottleArmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmThresholdThrottleArmCount_Type.__name__ = "Integer32"
_SmMlmThresholdThrottleArmCount_Object = MibTableColumn
smMlmThresholdThrottleArmCount = _SmMlmThresholdThrottleArmCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 35),
    _SmMlmThresholdThrottleArmCount_Type()
)
smMlmThresholdThrottleArmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdThrottleArmCount.setStatus("mandatory")


class _SmMlmThresholdThrottleReArmCount_Type(Integer32):
    """Custom type smMlmThresholdThrottleReArmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmThresholdThrottleReArmCount_Type.__name__ = "Integer32"
_SmMlmThresholdThrottleReArmCount_Object = MibTableColumn
smMlmThresholdThrottleReArmCount = _SmMlmThresholdThrottleReArmCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 36),
    _SmMlmThresholdThrottleReArmCount_Type()
)
smMlmThresholdThrottleReArmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdThrottleReArmCount.setStatus("mandatory")


class _SmMlmThresholdParticipationState_Type(Integer32):
    """Custom type smMlmThresholdParticipationState based on Integer32"""
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


_SmMlmThresholdParticipationState_Type.__name__ = "Integer32"
_SmMlmThresholdParticipationState_Object = MibTableColumn
smMlmThresholdParticipationState = _SmMlmThresholdParticipationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 37),
    _SmMlmThresholdParticipationState_Type()
)
smMlmThresholdParticipationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdParticipationState.setStatus("mandatory")
_SmMlmThresholdActivationTime_Type = DisplayString
_SmMlmThresholdActivationTime_Object = MibTableColumn
smMlmThresholdActivationTime = _SmMlmThresholdActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 38),
    _SmMlmThresholdActivationTime_Type()
)
smMlmThresholdActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdActivationTime.setStatus("mandatory")
_SmMlmThresholdActivationDayOfWeek_Type = DisplayString
_SmMlmThresholdActivationDayOfWeek_Object = MibTableColumn
smMlmThresholdActivationDayOfWeek = _SmMlmThresholdActivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 39),
    _SmMlmThresholdActivationDayOfWeek_Type()
)
smMlmThresholdActivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdActivationDayOfWeek.setStatus("mandatory")
_SmMlmThresholdDeactivationTime_Type = DisplayString
_SmMlmThresholdDeactivationTime_Object = MibTableColumn
smMlmThresholdDeactivationTime = _SmMlmThresholdDeactivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 40),
    _SmMlmThresholdDeactivationTime_Type()
)
smMlmThresholdDeactivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdDeactivationTime.setStatus("mandatory")
_SmMlmThresholdDeactivationDayOfWeek_Type = DisplayString
_SmMlmThresholdDeactivationDayOfWeek_Object = MibTableColumn
smMlmThresholdDeactivationDayOfWeek = _SmMlmThresholdDeactivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 1, 1, 41),
    _SmMlmThresholdDeactivationDayOfWeek_Type()
)
smMlmThresholdDeactivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdDeactivationDayOfWeek.setStatus("mandatory")
_SmMlmThresholdArmInfoTable_Object = MibTable
smMlmThresholdArmInfoTable = _SmMlmThresholdArmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 2)
)
if mibBuilder.loadTexts:
    smMlmThresholdArmInfoTable.setStatus("mandatory")
_SmMlmThresholdArmInfoEntry_Object = MibTableRow
smMlmThresholdArmInfoEntry = _SmMlmThresholdArmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 2, 1)
)
smMlmThresholdArmInfoEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdArmInfoName"),
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdArmInfoIpAddress"),
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdArmInfoIndex"),
)
if mibBuilder.loadTexts:
    smMlmThresholdArmInfoEntry.setStatus("mandatory")
_SmMlmThresholdArmInfoName_Type = DisplayString
_SmMlmThresholdArmInfoName_Object = MibTableColumn
smMlmThresholdArmInfoName = _SmMlmThresholdArmInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 2, 1, 1),
    _SmMlmThresholdArmInfoName_Type()
)
smMlmThresholdArmInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdArmInfoName.setStatus("mandatory")
_SmMlmThresholdArmInfoIpAddress_Type = IpAddress
_SmMlmThresholdArmInfoIpAddress_Object = MibTableColumn
smMlmThresholdArmInfoIpAddress = _SmMlmThresholdArmInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 2, 1, 2),
    _SmMlmThresholdArmInfoIpAddress_Type()
)
smMlmThresholdArmInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdArmInfoIpAddress.setStatus("mandatory")
_SmMlmThresholdArmInfoObjectID_Type = ObjectIdentifier
_SmMlmThresholdArmInfoObjectID_Object = MibTableColumn
smMlmThresholdArmInfoObjectID = _SmMlmThresholdArmInfoObjectID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 2, 1, 3),
    _SmMlmThresholdArmInfoObjectID_Type()
)
smMlmThresholdArmInfoObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdArmInfoObjectID.setStatus("mandatory")


class _SmMlmThresholdArmInfoIndex_Type(Integer32):
    """Custom type smMlmThresholdArmInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmThresholdArmInfoIndex_Type.__name__ = "Integer32"
_SmMlmThresholdArmInfoIndex_Object = MibTableColumn
smMlmThresholdArmInfoIndex = _SmMlmThresholdArmInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 2, 1, 4),
    _SmMlmThresholdArmInfoIndex_Type()
)
smMlmThresholdArmInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdArmInfoIndex.setStatus("mandatory")
_SmMlmThresholdResultsTable_Object = MibTable
smMlmThresholdResultsTable = _SmMlmThresholdResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3)
)
if mibBuilder.loadTexts:
    smMlmThresholdResultsTable.setStatus("mandatory")
_SmMlmThresholdResultsEntry_Object = MibTableRow
smMlmThresholdResultsEntry = _SmMlmThresholdResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1)
)
smMlmThresholdResultsEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdResultsName"),
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdResultsIpAddress"),
    (0, "MIDLEVELMGR-MIB", "smMlmThresholdResultsIndex"),
)
if mibBuilder.loadTexts:
    smMlmThresholdResultsEntry.setStatus("mandatory")
_SmMlmThresholdResultsName_Type = DisplayString
_SmMlmThresholdResultsName_Object = MibTableColumn
smMlmThresholdResultsName = _SmMlmThresholdResultsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 1),
    _SmMlmThresholdResultsName_Type()
)
smMlmThresholdResultsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsName.setStatus("mandatory")
_SmMlmThresholdResultsIpAddress_Type = IpAddress
_SmMlmThresholdResultsIpAddress_Object = MibTableColumn
smMlmThresholdResultsIpAddress = _SmMlmThresholdResultsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 2),
    _SmMlmThresholdResultsIpAddress_Type()
)
smMlmThresholdResultsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIpAddress.setStatus("mandatory")
_SmMlmThresholdResultsInstanceID_Type = DisplayString
_SmMlmThresholdResultsInstanceID_Object = MibTableColumn
smMlmThresholdResultsInstanceID = _SmMlmThresholdResultsInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 3),
    _SmMlmThresholdResultsInstanceID_Type()
)
smMlmThresholdResultsInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsInstanceID.setStatus("mandatory")


class _SmMlmThresholdResultsIndex_Type(Integer32):
    """Custom type smMlmThresholdResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmThresholdResultsIndex_Type.__name__ = "Integer32"
_SmMlmThresholdResultsIndex_Object = MibTableColumn
smMlmThresholdResultsIndex = _SmMlmThresholdResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 4),
    _SmMlmThresholdResultsIndex_Type()
)
smMlmThresholdResultsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIndex.setStatus("mandatory")
_SmMlmThresholdResultsResultTimeStamp_Type = DisplayString
_SmMlmThresholdResultsResultTimeStamp_Object = MibTableColumn
smMlmThresholdResultsResultTimeStamp = _SmMlmThresholdResultsResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 5),
    _SmMlmThresholdResultsResultTimeStamp_Type()
)
smMlmThresholdResultsResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsResultTimeStamp.setStatus("mandatory")


class _SmMlmThresholdResultsResultIndex_Type(Integer32):
    """Custom type smMlmThresholdResultsResultIndex based on Integer32"""
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


_SmMlmThresholdResultsResultIndex_Type.__name__ = "Integer32"
_SmMlmThresholdResultsResultIndex_Object = MibTableColumn
smMlmThresholdResultsResultIndex = _SmMlmThresholdResultsResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 6),
    _SmMlmThresholdResultsResultIndex_Type()
)
smMlmThresholdResultsResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsResultIndex.setStatus("mandatory")
_SmMlmThresholdResultsIntegerResult_Type = Integer32
_SmMlmThresholdResultsIntegerResult_Object = MibTableColumn
smMlmThresholdResultsIntegerResult = _SmMlmThresholdResultsIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 7),
    _SmMlmThresholdResultsIntegerResult_Type()
)
smMlmThresholdResultsIntegerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntegerResult.setStatus("mandatory")
_SmMlmThresholdResultsCounterResult_Type = Counter32
_SmMlmThresholdResultsCounterResult_Object = MibTableColumn
smMlmThresholdResultsCounterResult = _SmMlmThresholdResultsCounterResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 8),
    _SmMlmThresholdResultsCounterResult_Type()
)
smMlmThresholdResultsCounterResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsCounterResult.setStatus("mandatory")
_SmMlmThresholdResultsGaugeResult_Type = Gauge32
_SmMlmThresholdResultsGaugeResult_Object = MibTableColumn
smMlmThresholdResultsGaugeResult = _SmMlmThresholdResultsGaugeResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 9),
    _SmMlmThresholdResultsGaugeResult_Type()
)
smMlmThresholdResultsGaugeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsGaugeResult.setStatus("mandatory")
_SmMlmThresholdResultsDisplayStringResult_Type = DisplayString
_SmMlmThresholdResultsDisplayStringResult_Object = MibTableColumn
smMlmThresholdResultsDisplayStringResult = _SmMlmThresholdResultsDisplayStringResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 10),
    _SmMlmThresholdResultsDisplayStringResult_Type()
)
smMlmThresholdResultsDisplayStringResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsDisplayStringResult.setStatus("mandatory")


class _SmMlmThresholdResultsResetStats_Type(Integer32):
    """Custom type smMlmThresholdResultsResetStats based on Integer32"""
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


_SmMlmThresholdResultsResetStats_Type.__name__ = "Integer32"
_SmMlmThresholdResultsResetStats_Object = MibTableColumn
smMlmThresholdResultsResetStats = _SmMlmThresholdResultsResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 11),
    _SmMlmThresholdResultsResetStats_Type()
)
smMlmThresholdResultsResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmThresholdResultsResetStats.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeIntegerMin_Type = Integer32
_SmMlmThresholdResultsLifeTimeIntegerMin_Object = MibTableColumn
smMlmThresholdResultsLifeTimeIntegerMin = _SmMlmThresholdResultsLifeTimeIntegerMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 12),
    _SmMlmThresholdResultsLifeTimeIntegerMin_Type()
)
smMlmThresholdResultsLifeTimeIntegerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeIntegerMin.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeIntegerMax_Type = Integer32
_SmMlmThresholdResultsLifeTimeIntegerMax_Object = MibTableColumn
smMlmThresholdResultsLifeTimeIntegerMax = _SmMlmThresholdResultsLifeTimeIntegerMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 13),
    _SmMlmThresholdResultsLifeTimeIntegerMax_Type()
)
smMlmThresholdResultsLifeTimeIntegerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeIntegerMax.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeIntegerAvg_Type = Integer32
_SmMlmThresholdResultsLifeTimeIntegerAvg_Object = MibTableColumn
smMlmThresholdResultsLifeTimeIntegerAvg = _SmMlmThresholdResultsLifeTimeIntegerAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 14),
    _SmMlmThresholdResultsLifeTimeIntegerAvg_Type()
)
smMlmThresholdResultsLifeTimeIntegerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeIntegerAvg.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeIntegerStdDeviation_Type = Integer32
_SmMlmThresholdResultsLifeTimeIntegerStdDeviation_Object = MibTableColumn
smMlmThresholdResultsLifeTimeIntegerStdDeviation = _SmMlmThresholdResultsLifeTimeIntegerStdDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 15),
    _SmMlmThresholdResultsLifeTimeIntegerStdDeviation_Type()
)
smMlmThresholdResultsLifeTimeIntegerStdDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeIntegerStdDeviation.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeCounterGaugeMin_Type = Gauge32
_SmMlmThresholdResultsLifeTimeCounterGaugeMin_Object = MibTableColumn
smMlmThresholdResultsLifeTimeCounterGaugeMin = _SmMlmThresholdResultsLifeTimeCounterGaugeMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 16),
    _SmMlmThresholdResultsLifeTimeCounterGaugeMin_Type()
)
smMlmThresholdResultsLifeTimeCounterGaugeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeCounterGaugeMin.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeCounterGaugeMax_Type = Gauge32
_SmMlmThresholdResultsLifeTimeCounterGaugeMax_Object = MibTableColumn
smMlmThresholdResultsLifeTimeCounterGaugeMax = _SmMlmThresholdResultsLifeTimeCounterGaugeMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 17),
    _SmMlmThresholdResultsLifeTimeCounterGaugeMax_Type()
)
smMlmThresholdResultsLifeTimeCounterGaugeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeCounterGaugeMax.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeCounterGaugeAvg_Type = Gauge32
_SmMlmThresholdResultsLifeTimeCounterGaugeAvg_Object = MibTableColumn
smMlmThresholdResultsLifeTimeCounterGaugeAvg = _SmMlmThresholdResultsLifeTimeCounterGaugeAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 18),
    _SmMlmThresholdResultsLifeTimeCounterGaugeAvg_Type()
)
smMlmThresholdResultsLifeTimeCounterGaugeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeCounterGaugeAvg.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeCounterGaugeStdDeviation_Type = Integer32
_SmMlmThresholdResultsLifeTimeCounterGaugeStdDeviation_Object = MibTableColumn
smMlmThresholdResultsLifeTimeCounterGaugeStdDeviation = _SmMlmThresholdResultsLifeTimeCounterGaugeStdDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 19),
    _SmMlmThresholdResultsLifeTimeCounterGaugeStdDeviation_Type()
)
smMlmThresholdResultsLifeTimeCounterGaugeStdDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeCounterGaugeStdDeviation.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeSamples_Type = Counter32
_SmMlmThresholdResultsLifeTimeSamples_Object = MibTableColumn
smMlmThresholdResultsLifeTimeSamples = _SmMlmThresholdResultsLifeTimeSamples_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 20),
    _SmMlmThresholdResultsLifeTimeSamples_Type()
)
smMlmThresholdResultsLifeTimeSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeSamples.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeSeconds_Type = Counter32
_SmMlmThresholdResultsLifeTimeSeconds_Object = MibTableColumn
smMlmThresholdResultsLifeTimeSeconds = _SmMlmThresholdResultsLifeTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 21),
    _SmMlmThresholdResultsLifeTimeSeconds_Type()
)
smMlmThresholdResultsLifeTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeSeconds.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeMinTimeStamp_Type = DisplayString
_SmMlmThresholdResultsLifeTimeMinTimeStamp_Object = MibTableColumn
smMlmThresholdResultsLifeTimeMinTimeStamp = _SmMlmThresholdResultsLifeTimeMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 22),
    _SmMlmThresholdResultsLifeTimeMinTimeStamp_Type()
)
smMlmThresholdResultsLifeTimeMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeMinTimeStamp.setStatus("mandatory")
_SmMlmThresholdResultsLifeTimeMaxTimeStamp_Type = DisplayString
_SmMlmThresholdResultsLifeTimeMaxTimeStamp_Object = MibTableColumn
smMlmThresholdResultsLifeTimeMaxTimeStamp = _SmMlmThresholdResultsLifeTimeMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 23),
    _SmMlmThresholdResultsLifeTimeMaxTimeStamp_Type()
)
smMlmThresholdResultsLifeTimeMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsLifeTimeMaxTimeStamp.setStatus("mandatory")
_SmMlmThresholdResultsIntervalIntegerMin_Type = Integer32
_SmMlmThresholdResultsIntervalIntegerMin_Object = MibTableColumn
smMlmThresholdResultsIntervalIntegerMin = _SmMlmThresholdResultsIntervalIntegerMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 24),
    _SmMlmThresholdResultsIntervalIntegerMin_Type()
)
smMlmThresholdResultsIntervalIntegerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalIntegerMin.setStatus("mandatory")
_SmMlmThresholdResultsIntervalIntegerMax_Type = Integer32
_SmMlmThresholdResultsIntervalIntegerMax_Object = MibTableColumn
smMlmThresholdResultsIntervalIntegerMax = _SmMlmThresholdResultsIntervalIntegerMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 25),
    _SmMlmThresholdResultsIntervalIntegerMax_Type()
)
smMlmThresholdResultsIntervalIntegerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalIntegerMax.setStatus("mandatory")
_SmMlmThresholdResultsIntervalIntegerAvg_Type = Integer32
_SmMlmThresholdResultsIntervalIntegerAvg_Object = MibTableColumn
smMlmThresholdResultsIntervalIntegerAvg = _SmMlmThresholdResultsIntervalIntegerAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 26),
    _SmMlmThresholdResultsIntervalIntegerAvg_Type()
)
smMlmThresholdResultsIntervalIntegerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalIntegerAvg.setStatus("mandatory")
_SmMlmThresholdResultsIntervalIntegerStdDeviation_Type = Integer32
_SmMlmThresholdResultsIntervalIntegerStdDeviation_Object = MibTableColumn
smMlmThresholdResultsIntervalIntegerStdDeviation = _SmMlmThresholdResultsIntervalIntegerStdDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 27),
    _SmMlmThresholdResultsIntervalIntegerStdDeviation_Type()
)
smMlmThresholdResultsIntervalIntegerStdDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalIntegerStdDeviation.setStatus("mandatory")
_SmMlmThresholdResultsIntervalCounterGaugeMin_Type = Gauge32
_SmMlmThresholdResultsIntervalCounterGaugeMin_Object = MibTableColumn
smMlmThresholdResultsIntervalCounterGaugeMin = _SmMlmThresholdResultsIntervalCounterGaugeMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 28),
    _SmMlmThresholdResultsIntervalCounterGaugeMin_Type()
)
smMlmThresholdResultsIntervalCounterGaugeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalCounterGaugeMin.setStatus("mandatory")
_SmMlmThresholdResultsIntervalCounterGaugeMax_Type = Gauge32
_SmMlmThresholdResultsIntervalCounterGaugeMax_Object = MibTableColumn
smMlmThresholdResultsIntervalCounterGaugeMax = _SmMlmThresholdResultsIntervalCounterGaugeMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 29),
    _SmMlmThresholdResultsIntervalCounterGaugeMax_Type()
)
smMlmThresholdResultsIntervalCounterGaugeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalCounterGaugeMax.setStatus("mandatory")
_SmMlmThresholdResultsIntervalCounterGaugeAvg_Type = Gauge32
_SmMlmThresholdResultsIntervalCounterGaugeAvg_Object = MibTableColumn
smMlmThresholdResultsIntervalCounterGaugeAvg = _SmMlmThresholdResultsIntervalCounterGaugeAvg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 30),
    _SmMlmThresholdResultsIntervalCounterGaugeAvg_Type()
)
smMlmThresholdResultsIntervalCounterGaugeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalCounterGaugeAvg.setStatus("mandatory")
_SmMlmThresholdResultsIntervalCounterGaugeStdDeviation_Type = Integer32
_SmMlmThresholdResultsIntervalCounterGaugeStdDeviation_Object = MibTableColumn
smMlmThresholdResultsIntervalCounterGaugeStdDeviation = _SmMlmThresholdResultsIntervalCounterGaugeStdDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 31),
    _SmMlmThresholdResultsIntervalCounterGaugeStdDeviation_Type()
)
smMlmThresholdResultsIntervalCounterGaugeStdDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalCounterGaugeStdDeviation.setStatus("mandatory")
_SmMlmThresholdResultsIntervalSamples_Type = Counter32
_SmMlmThresholdResultsIntervalSamples_Object = MibTableColumn
smMlmThresholdResultsIntervalSamples = _SmMlmThresholdResultsIntervalSamples_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 32),
    _SmMlmThresholdResultsIntervalSamples_Type()
)
smMlmThresholdResultsIntervalSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalSamples.setStatus("mandatory")
_SmMlmThresholdResultsIntervalSeconds_Type = Counter32
_SmMlmThresholdResultsIntervalSeconds_Object = MibTableColumn
smMlmThresholdResultsIntervalSeconds = _SmMlmThresholdResultsIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 33),
    _SmMlmThresholdResultsIntervalSeconds_Type()
)
smMlmThresholdResultsIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalSeconds.setStatus("mandatory")
_SmMlmThresholdResultsIntervalRate_Type = Gauge32
_SmMlmThresholdResultsIntervalRate_Object = MibTableColumn
smMlmThresholdResultsIntervalRate = _SmMlmThresholdResultsIntervalRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 5, 3, 1, 34),
    _SmMlmThresholdResultsIntervalRate_Type()
)
smMlmThresholdResultsIntervalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmThresholdResultsIntervalRate.setStatus("mandatory")
_SmMlmAnalysis_ObjectIdentity = ObjectIdentity
smMlmAnalysis = _SmMlmAnalysis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6)
)
_SmMlmAnalysisTable_Object = MibTable
smMlmAnalysisTable = _SmMlmAnalysisTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1)
)
if mibBuilder.loadTexts:
    smMlmAnalysisTable.setStatus("obsolete")
_SmMlmAnalysisEntry_Object = MibTableRow
smMlmAnalysisEntry = _SmMlmAnalysisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1)
)
smMlmAnalysisEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmAnalysisName"),
)
if mibBuilder.loadTexts:
    smMlmAnalysisEntry.setStatus("obsolete")


class _SmMlmAnalysisState_Type(Integer32):
    """Custom type smMlmAnalysisState based on Integer32"""
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


_SmMlmAnalysisState_Type.__name__ = "Integer32"
_SmMlmAnalysisState_Object = MibTableColumn
smMlmAnalysisState = _SmMlmAnalysisState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 1),
    _SmMlmAnalysisState_Type()
)
smMlmAnalysisState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisState.setStatus("obsolete")
_SmMlmAnalysisName_Type = DisplayString
_SmMlmAnalysisName_Object = MibTableColumn
smMlmAnalysisName = _SmMlmAnalysisName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 2),
    _SmMlmAnalysisName_Type()
)
smMlmAnalysisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisName.setStatus("obsolete")
_SmMlmAnalysisDescription_Type = DisplayString
_SmMlmAnalysisDescription_Object = MibTableColumn
smMlmAnalysisDescription = _SmMlmAnalysisDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 3),
    _SmMlmAnalysisDescription_Type()
)
smMlmAnalysisDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisDescription.setStatus("obsolete")
_SmMlmAnalysisOwnerID_Type = DisplayString
_SmMlmAnalysisOwnerID_Object = MibTableColumn
smMlmAnalysisOwnerID = _SmMlmAnalysisOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 4),
    _SmMlmAnalysisOwnerID_Type()
)
smMlmAnalysisOwnerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisOwnerID.setStatus("obsolete")
_SmMlmAnalysisLocalRemoteMIBVariableExpression_Type = DisplayString
_SmMlmAnalysisLocalRemoteMIBVariableExpression_Object = MibTableColumn
smMlmAnalysisLocalRemoteMIBVariableExpression = _SmMlmAnalysisLocalRemoteMIBVariableExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 5),
    _SmMlmAnalysisLocalRemoteMIBVariableExpression_Type()
)
smMlmAnalysisLocalRemoteMIBVariableExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisLocalRemoteMIBVariableExpression.setStatus("obsolete")
_SmMlmAnalysisPollTime_Type = DisplayString
_SmMlmAnalysisPollTime_Object = MibTableColumn
smMlmAnalysisPollTime = _SmMlmAnalysisPollTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 6),
    _SmMlmAnalysisPollTime_Type()
)
smMlmAnalysisPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisPollTime.setStatus("obsolete")


class _SmMlmAnalysisResultIndex_Type(Integer32):
    """Custom type smMlmAnalysisResultIndex based on Integer32"""
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


_SmMlmAnalysisResultIndex_Type.__name__ = "Integer32"
_SmMlmAnalysisResultIndex_Object = MibTableColumn
smMlmAnalysisResultIndex = _SmMlmAnalysisResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 7),
    _SmMlmAnalysisResultIndex_Type()
)
smMlmAnalysisResultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAnalysisResultIndex.setStatus("obsolete")
_SmMlmAnalysisIntegerResult_Type = Integer32
_SmMlmAnalysisIntegerResult_Object = MibTableColumn
smMlmAnalysisIntegerResult = _SmMlmAnalysisIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 8),
    _SmMlmAnalysisIntegerResult_Type()
)
smMlmAnalysisIntegerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAnalysisIntegerResult.setStatus("obsolete")
_SmMlmAnalysisCounterResult_Type = Counter32
_SmMlmAnalysisCounterResult_Object = MibTableColumn
smMlmAnalysisCounterResult = _SmMlmAnalysisCounterResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 9),
    _SmMlmAnalysisCounterResult_Type()
)
smMlmAnalysisCounterResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAnalysisCounterResult.setStatus("obsolete")
_SmMlmAnalysisGaugeResult_Type = Gauge32
_SmMlmAnalysisGaugeResult_Object = MibTableColumn
smMlmAnalysisGaugeResult = _SmMlmAnalysisGaugeResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 10),
    _SmMlmAnalysisGaugeResult_Type()
)
smMlmAnalysisGaugeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAnalysisGaugeResult.setStatus("obsolete")
_SmMlmAnalysisDisplayStringResult_Type = DisplayString
_SmMlmAnalysisDisplayStringResult_Object = MibTableColumn
smMlmAnalysisDisplayStringResult = _SmMlmAnalysisDisplayStringResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 11),
    _SmMlmAnalysisDisplayStringResult_Type()
)
smMlmAnalysisDisplayStringResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAnalysisDisplayStringResult.setStatus("obsolete")
_SmMlmAnalysisReturnCode_Type = Integer32
_SmMlmAnalysisReturnCode_Object = MibTableColumn
smMlmAnalysisReturnCode = _SmMlmAnalysisReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 12),
    _SmMlmAnalysisReturnCode_Type()
)
smMlmAnalysisReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAnalysisReturnCode.setStatus("obsolete")
_SmMlmAnalysisStandardError_Type = DisplayString
_SmMlmAnalysisStandardError_Object = MibTableColumn
smMlmAnalysisStandardError = _SmMlmAnalysisStandardError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 6, 1, 1, 13),
    _SmMlmAnalysisStandardError_Type()
)
smMlmAnalysisStandardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAnalysisStandardError.setStatus("obsolete")
_SmMlmFilter_ObjectIdentity = ObjectIdentity
smMlmFilter = _SmMlmFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7)
)


class _SmMlmFilterDefaultAction_Type(Integer32):
    """Custom type smMlmFilterDefaultAction based on Integer32"""
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


_SmMlmFilterDefaultAction_Type.__name__ = "Integer32"
_SmMlmFilterDefaultAction_Object = MibScalar
smMlmFilterDefaultAction = _SmMlmFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 1),
    _SmMlmFilterDefaultAction_Type()
)
smMlmFilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterDefaultAction.setStatus("mandatory")


class _SmMlmFilterUdpTrapReception_Type(Integer32):
    """Custom type smMlmFilterUdpTrapReception based on Integer32"""
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


_SmMlmFilterUdpTrapReception_Type.__name__ = "Integer32"
_SmMlmFilterUdpTrapReception_Object = MibScalar
smMlmFilterUdpTrapReception = _SmMlmFilterUdpTrapReception_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 2),
    _SmMlmFilterUdpTrapReception_Type()
)
smMlmFilterUdpTrapReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterUdpTrapReception.setStatus("mandatory")
_SmMlmFilterTotalTrapsReceived_Type = Counter32
_SmMlmFilterTotalTrapsReceived_Object = MibScalar
smMlmFilterTotalTrapsReceived = _SmMlmFilterTotalTrapsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 3),
    _SmMlmFilterTotalTrapsReceived_Type()
)
smMlmFilterTotalTrapsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterTotalTrapsReceived.setStatus("mandatory")
_SmMlmFilterTable_Object = MibTable
smMlmFilterTable = _SmMlmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4)
)
if mibBuilder.loadTexts:
    smMlmFilterTable.setStatus("mandatory")
_SmMlmFilterEntry_Object = MibTableRow
smMlmFilterEntry = _SmMlmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1)
)
smMlmFilterEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmFilterName"),
)
if mibBuilder.loadTexts:
    smMlmFilterEntry.setStatus("mandatory")


class _SmMlmFilterState_Type(Integer32):
    """Custom type smMlmFilterState based on Integer32"""
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


_SmMlmFilterState_Type.__name__ = "Integer32"
_SmMlmFilterState_Object = MibTableColumn
smMlmFilterState = _SmMlmFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 1),
    _SmMlmFilterState_Type()
)
smMlmFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterState.setStatus("mandatory")


class _SmMlmFilterParticipationState_Type(Integer32):
    """Custom type smMlmFilterParticipationState based on Integer32"""
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


_SmMlmFilterParticipationState_Type.__name__ = "Integer32"
_SmMlmFilterParticipationState_Object = MibTableColumn
smMlmFilterParticipationState = _SmMlmFilterParticipationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 2),
    _SmMlmFilterParticipationState_Type()
)
smMlmFilterParticipationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterParticipationState.setStatus("mandatory")
_SmMlmFilterName_Type = DisplayString
_SmMlmFilterName_Object = MibTableColumn
smMlmFilterName = _SmMlmFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 3),
    _SmMlmFilterName_Type()
)
smMlmFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterName.setStatus("mandatory")
_SmMlmFilterDescription_Type = DisplayString
_SmMlmFilterDescription_Object = MibTableColumn
smMlmFilterDescription = _SmMlmFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 4),
    _SmMlmFilterDescription_Type()
)
smMlmFilterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterDescription.setStatus("mandatory")


class _SmMlmFilterAction_Type(Integer32):
    """Custom type smMlmFilterAction based on Integer32"""
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


_SmMlmFilterAction_Type.__name__ = "Integer32"
_SmMlmFilterAction_Object = MibTableColumn
smMlmFilterAction = _SmMlmFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 5),
    _SmMlmFilterAction_Type()
)
smMlmFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterAction.setStatus("mandatory")
_SmMlmFilterEntryEnterpriseExpression_Type = DisplayString
_SmMlmFilterEntryEnterpriseExpression_Object = MibTableColumn
smMlmFilterEntryEnterpriseExpression = _SmMlmFilterEntryEnterpriseExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 6),
    _SmMlmFilterEntryEnterpriseExpression_Type()
)
smMlmFilterEntryEnterpriseExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterEntryEnterpriseExpression.setStatus("mandatory")
_SmMlmFilterAgentAddrExpression_Type = DisplayString
_SmMlmFilterAgentAddrExpression_Object = MibTableColumn
smMlmFilterAgentAddrExpression = _SmMlmFilterAgentAddrExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 7),
    _SmMlmFilterAgentAddrExpression_Type()
)
smMlmFilterAgentAddrExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterAgentAddrExpression.setStatus("mandatory")
_SmMlmFilterGenericExpression_Type = DisplayString
_SmMlmFilterGenericExpression_Object = MibTableColumn
smMlmFilterGenericExpression = _SmMlmFilterGenericExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 8),
    _SmMlmFilterGenericExpression_Type()
)
smMlmFilterGenericExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterGenericExpression.setStatus("mandatory")
_SmMlmFilterSpecificExpression_Type = DisplayString
_SmMlmFilterSpecificExpression_Object = MibTableColumn
smMlmFilterSpecificExpression = _SmMlmFilterSpecificExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 9),
    _SmMlmFilterSpecificExpression_Type()
)
smMlmFilterSpecificExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterSpecificExpression.setStatus("mandatory")
_SmMlmFilterVariableExpression_Type = DisplayString
_SmMlmFilterVariableExpression_Object = MibTableColumn
smMlmFilterVariableExpression = _SmMlmFilterVariableExpression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 10),
    _SmMlmFilterVariableExpression_Type()
)
smMlmFilterVariableExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterVariableExpression.setStatus("mandatory")
_SmMlmFilterTotalTrapsMatched_Type = Counter32
_SmMlmFilterTotalTrapsMatched_Object = MibTableColumn
smMlmFilterTotalTrapsMatched = _SmMlmFilterTotalTrapsMatched_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 11),
    _SmMlmFilterTotalTrapsMatched_Type()
)
smMlmFilterTotalTrapsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterTotalTrapsMatched.setStatus("mandatory")
_SmMlmFilterActivationTime_Type = DisplayString
_SmMlmFilterActivationTime_Object = MibTableColumn
smMlmFilterActivationTime = _SmMlmFilterActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 12),
    _SmMlmFilterActivationTime_Type()
)
smMlmFilterActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterActivationTime.setStatus("mandatory")
_SmMlmFilterActivationDayOfWeek_Type = DisplayString
_SmMlmFilterActivationDayOfWeek_Object = MibTableColumn
smMlmFilterActivationDayOfWeek = _SmMlmFilterActivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 13),
    _SmMlmFilterActivationDayOfWeek_Type()
)
smMlmFilterActivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterActivationDayOfWeek.setStatus("mandatory")
_SmMlmFilterDeactivationTime_Type = DisplayString
_SmMlmFilterDeactivationTime_Object = MibTableColumn
smMlmFilterDeactivationTime = _SmMlmFilterDeactivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 14),
    _SmMlmFilterDeactivationTime_Type()
)
smMlmFilterDeactivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterDeactivationTime.setStatus("mandatory")
_SmMlmFilterDeactivationDayOfWeek_Type = DisplayString
_SmMlmFilterDeactivationDayOfWeek_Object = MibTableColumn
smMlmFilterDeactivationDayOfWeek = _SmMlmFilterDeactivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 15),
    _SmMlmFilterDeactivationDayOfWeek_Type()
)
smMlmFilterDeactivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterDeactivationDayOfWeek.setStatus("mandatory")
_SmMlmFilterTrapDestinations_Type = DisplayString
_SmMlmFilterTrapDestinations_Object = MibTableColumn
smMlmFilterTrapDestinations = _SmMlmFilterTrapDestinations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 16),
    _SmMlmFilterTrapDestinations_Type()
)
smMlmFilterTrapDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterTrapDestinations.setStatus("mandatory")
_SmMlmFilterMatchedCommand_Type = DisplayString
_SmMlmFilterMatchedCommand_Object = MibTableColumn
smMlmFilterMatchedCommand = _SmMlmFilterMatchedCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 17),
    _SmMlmFilterMatchedCommand_Type()
)
smMlmFilterMatchedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterMatchedCommand.setStatus("mandatory")
_SmMlmFilterMatchedTrapDescription_Type = DisplayString
_SmMlmFilterMatchedTrapDescription_Object = MibTableColumn
smMlmFilterMatchedTrapDescription = _SmMlmFilterMatchedTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 18),
    _SmMlmFilterMatchedTrapDescription_Type()
)
smMlmFilterMatchedTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterMatchedTrapDescription.setStatus("mandatory")
_SmMlmFilterMatchedTrapEnterprise_Type = DisplayString
_SmMlmFilterMatchedTrapEnterprise_Object = MibTableColumn
smMlmFilterMatchedTrapEnterprise = _SmMlmFilterMatchedTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 19),
    _SmMlmFilterMatchedTrapEnterprise_Type()
)
smMlmFilterMatchedTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterMatchedTrapEnterprise.setStatus("mandatory")
_SmMlmFilterMatchedSpecificTrap_Type = Integer32
_SmMlmFilterMatchedSpecificTrap_Object = MibTableColumn
smMlmFilterMatchedSpecificTrap = _SmMlmFilterMatchedSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 20),
    _SmMlmFilterMatchedSpecificTrap_Type()
)
smMlmFilterMatchedSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterMatchedSpecificTrap.setStatus("mandatory")


class _SmMlmFilterThrottleType_Type(Integer32):
    """Custom type smMlmFilterThrottleType based on Integer32"""
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


_SmMlmFilterThrottleType_Type.__name__ = "Integer32"
_SmMlmFilterThrottleType_Object = MibTableColumn
smMlmFilterThrottleType = _SmMlmFilterThrottleType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 21),
    _SmMlmFilterThrottleType_Type()
)
smMlmFilterThrottleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleType.setStatus("mandatory")
_SmMlmFilterThrottleArmTrapCount_Type = Integer32
_SmMlmFilterThrottleArmTrapCount_Object = MibTableColumn
smMlmFilterThrottleArmTrapCount = _SmMlmFilterThrottleArmTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 22),
    _SmMlmFilterThrottleArmTrapCount_Type()
)
smMlmFilterThrottleArmTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleArmTrapCount.setStatus("mandatory")
_SmMlmFilterThrottleArmedCommand_Type = DisplayString
_SmMlmFilterThrottleArmedCommand_Object = MibTableColumn
smMlmFilterThrottleArmedCommand = _SmMlmFilterThrottleArmedCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 23),
    _SmMlmFilterThrottleArmedCommand_Type()
)
smMlmFilterThrottleArmedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleArmedCommand.setStatus("mandatory")
_SmMlmFilterThrottleArmedTrapDescription_Type = DisplayString
_SmMlmFilterThrottleArmedTrapDescription_Object = MibTableColumn
smMlmFilterThrottleArmedTrapDescription = _SmMlmFilterThrottleArmedTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 24),
    _SmMlmFilterThrottleArmedTrapDescription_Type()
)
smMlmFilterThrottleArmedTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleArmedTrapDescription.setStatus("mandatory")
_SmMlmFilterThrottleArmedTrapEnterprise_Type = DisplayString
_SmMlmFilterThrottleArmedTrapEnterprise_Object = MibTableColumn
smMlmFilterThrottleArmedTrapEnterprise = _SmMlmFilterThrottleArmedTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 25),
    _SmMlmFilterThrottleArmedTrapEnterprise_Type()
)
smMlmFilterThrottleArmedTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleArmedTrapEnterprise.setStatus("mandatory")
_SmMlmFilterThrottleArmedSpecificTrap_Type = Integer32
_SmMlmFilterThrottleArmedSpecificTrap_Object = MibTableColumn
smMlmFilterThrottleArmedSpecificTrap = _SmMlmFilterThrottleArmedSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 26),
    _SmMlmFilterThrottleArmedSpecificTrap_Type()
)
smMlmFilterThrottleArmedSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleArmedSpecificTrap.setStatus("mandatory")
_SmMlmFilterThrottleDisarmTimer_Type = DisplayString
_SmMlmFilterThrottleDisarmTimer_Object = MibTableColumn
smMlmFilterThrottleDisarmTimer = _SmMlmFilterThrottleDisarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 27),
    _SmMlmFilterThrottleDisarmTimer_Type()
)
smMlmFilterThrottleDisarmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleDisarmTimer.setStatus("mandatory")
_SmMlmFilterThrottleDisarmTrapCount_Type = Integer32
_SmMlmFilterThrottleDisarmTrapCount_Object = MibTableColumn
smMlmFilterThrottleDisarmTrapCount = _SmMlmFilterThrottleDisarmTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 28),
    _SmMlmFilterThrottleDisarmTrapCount_Type()
)
smMlmFilterThrottleDisarmTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleDisarmTrapCount.setStatus("mandatory")
_SmMlmFilterThrottleDisarmedCommand_Type = DisplayString
_SmMlmFilterThrottleDisarmedCommand_Object = MibTableColumn
smMlmFilterThrottleDisarmedCommand = _SmMlmFilterThrottleDisarmedCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 29),
    _SmMlmFilterThrottleDisarmedCommand_Type()
)
smMlmFilterThrottleDisarmedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleDisarmedCommand.setStatus("mandatory")
_SmMlmFilterThrottleDisarmedTrapDescription_Type = DisplayString
_SmMlmFilterThrottleDisarmedTrapDescription_Object = MibTableColumn
smMlmFilterThrottleDisarmedTrapDescription = _SmMlmFilterThrottleDisarmedTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 30),
    _SmMlmFilterThrottleDisarmedTrapDescription_Type()
)
smMlmFilterThrottleDisarmedTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleDisarmedTrapDescription.setStatus("mandatory")
_SmMlmFilterThrottleDisarmedTrapEnterprise_Type = DisplayString
_SmMlmFilterThrottleDisarmedTrapEnterprise_Object = MibTableColumn
smMlmFilterThrottleDisarmedTrapEnterprise = _SmMlmFilterThrottleDisarmedTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 31),
    _SmMlmFilterThrottleDisarmedTrapEnterprise_Type()
)
smMlmFilterThrottleDisarmedTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleDisarmedTrapEnterprise.setStatus("mandatory")
_SmMlmFilterThrottleDisarmedSpecificTrap_Type = Integer32
_SmMlmFilterThrottleDisarmedSpecificTrap_Object = MibTableColumn
smMlmFilterThrottleDisarmedSpecificTrap = _SmMlmFilterThrottleDisarmedSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 32),
    _SmMlmFilterThrottleDisarmedSpecificTrap_Type()
)
smMlmFilterThrottleDisarmedSpecificTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleDisarmedSpecificTrap.setStatus("mandatory")


class _SmMlmFilterThrottleState_Type(Integer32):
    """Custom type smMlmFilterThrottleState based on Integer32"""
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


_SmMlmFilterThrottleState_Type.__name__ = "Integer32"
_SmMlmFilterThrottleState_Object = MibTableColumn
smMlmFilterThrottleState = _SmMlmFilterThrottleState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 33),
    _SmMlmFilterThrottleState_Type()
)
smMlmFilterThrottleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterThrottleState.setStatus("mandatory")
_SmMlmFilterThrottleTimeStarted_Type = DisplayString
_SmMlmFilterThrottleTimeStarted_Object = MibTableColumn
smMlmFilterThrottleTimeStarted = _SmMlmFilterThrottleTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 34),
    _SmMlmFilterThrottleTimeStarted_Type()
)
smMlmFilterThrottleTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterThrottleTimeStarted.setStatus("mandatory")
_SmMlmFilterThrottleTrapCount_Type = Integer32
_SmMlmFilterThrottleTrapCount_Object = MibTableColumn
smMlmFilterThrottleTrapCount = _SmMlmFilterThrottleTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 35),
    _SmMlmFilterThrottleTrapCount_Type()
)
smMlmFilterThrottleTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterThrottleTrapCount.setStatus("mandatory")
_SmMlmFilterMessages_Type = DisplayString
_SmMlmFilterMessages_Object = MibTableColumn
smMlmFilterMessages = _SmMlmFilterMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 36),
    _SmMlmFilterMessages_Type()
)
smMlmFilterMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterMessages.setStatus("mandatory")


class _SmMlmFilterThrottleCriteria_Type(Integer32):
    """Custom type smMlmFilterThrottleCriteria based on Integer32"""
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
        *(("byNode", 2),
          ("byNodeAndTrapType", 1),
          ("byNone", 4),
          ("byTrapType", 3))
    )


_SmMlmFilterThrottleCriteria_Type.__name__ = "Integer32"
_SmMlmFilterThrottleCriteria_Object = MibTableColumn
smMlmFilterThrottleCriteria = _SmMlmFilterThrottleCriteria_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 37),
    _SmMlmFilterThrottleCriteria_Type()
)
smMlmFilterThrottleCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleCriteria.setStatus("mandatory")
_SmMlmFilterThrottleVariables_Type = DisplayString
_SmMlmFilterThrottleVariables_Object = MibTableColumn
smMlmFilterThrottleVariables = _SmMlmFilterThrottleVariables_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 4, 1, 38),
    _SmMlmFilterThrottleVariables_Type()
)
smMlmFilterThrottleVariables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterThrottleVariables.setStatus("mandatory")


class _SmMlmFilterTcpTrapReception_Type(Integer32):
    """Custom type smMlmFilterTcpTrapReception based on Integer32"""
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


_SmMlmFilterTcpTrapReception_Type.__name__ = "Integer32"
_SmMlmFilterTcpTrapReception_Object = MibScalar
smMlmFilterTcpTrapReception = _SmMlmFilterTcpTrapReception_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 5),
    _SmMlmFilterTcpTrapReception_Type()
)
smMlmFilterTcpTrapReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterTcpTrapReception.setStatus("mandatory")


class _SmMlmFilterTcpReceptionStatus_Type(Integer32):
    """Custom type smMlmFilterTcpReceptionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("portBusy", 3))
    )


_SmMlmFilterTcpReceptionStatus_Type.__name__ = "Integer32"
_SmMlmFilterTcpReceptionStatus_Object = MibScalar
smMlmFilterTcpReceptionStatus = _SmMlmFilterTcpReceptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 6),
    _SmMlmFilterTcpReceptionStatus_Type()
)
smMlmFilterTcpReceptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterTcpReceptionStatus.setStatus("mandatory")


class _SmMlmFilterUdpReceptionStatus_Type(Integer32):
    """Custom type smMlmFilterUdpReceptionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("portBusy", 3))
    )


_SmMlmFilterUdpReceptionStatus_Type.__name__ = "Integer32"
_SmMlmFilterUdpReceptionStatus_Object = MibScalar
smMlmFilterUdpReceptionStatus = _SmMlmFilterUdpReceptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 7),
    _SmMlmFilterUdpReceptionStatus_Type()
)
smMlmFilterUdpReceptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterUdpReceptionStatus.setStatus("mandatory")
_SmMlmFilterUdpTrapReceptionPort_Type = Integer32
_SmMlmFilterUdpTrapReceptionPort_Object = MibScalar
smMlmFilterUdpTrapReceptionPort = _SmMlmFilterUdpTrapReceptionPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 8),
    _SmMlmFilterUdpTrapReceptionPort_Type()
)
smMlmFilterUdpTrapReceptionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterUdpTrapReceptionPort.setStatus("mandatory")
_SmMlmFilterTcpTrapReceptionPort_Type = Integer32
_SmMlmFilterTcpTrapReceptionPort_Object = MibScalar
smMlmFilterTcpTrapReceptionPort = _SmMlmFilterTcpTrapReceptionPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 9),
    _SmMlmFilterTcpTrapReceptionPort_Type()
)
smMlmFilterTcpTrapReceptionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmFilterTcpTrapReceptionPort.setStatus("mandatory")
_SmMlmFilterTrapReceptionMessages_Type = DisplayString
_SmMlmFilterTrapReceptionMessages_Object = MibScalar
smMlmFilterTrapReceptionMessages = _SmMlmFilterTrapReceptionMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 7, 10),
    _SmMlmFilterTrapReceptionMessages_Type()
)
smMlmFilterTrapReceptionMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmFilterTrapReceptionMessages.setStatus("mandatory")
_SmMlmAlias_ObjectIdentity = ObjectIdentity
smMlmAlias = _SmMlmAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8)
)
_SmMlmAliasTable_Object = MibTable
smMlmAliasTable = _SmMlmAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1)
)
if mibBuilder.loadTexts:
    smMlmAliasTable.setStatus("mandatory")
_SmMlmAliasEntry_Object = MibTableRow
smMlmAliasEntry = _SmMlmAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1)
)
smMlmAliasEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmAliasName"),
)
if mibBuilder.loadTexts:
    smMlmAliasEntry.setStatus("mandatory")


class _SmMlmAliasState_Type(Integer32):
    """Custom type smMlmAliasState based on Integer32"""
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


_SmMlmAliasState_Type.__name__ = "Integer32"
_SmMlmAliasState_Object = MibTableColumn
smMlmAliasState = _SmMlmAliasState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 1),
    _SmMlmAliasState_Type()
)
smMlmAliasState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAliasState.setStatus("mandatory")
_SmMlmAliasName_Type = DisplayString
_SmMlmAliasName_Object = MibTableColumn
smMlmAliasName = _SmMlmAliasName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 2),
    _SmMlmAliasName_Type()
)
smMlmAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAliasName.setStatus("mandatory")
_SmMlmAliasList_Type = DisplayString
_SmMlmAliasList_Object = MibTableColumn
smMlmAliasList = _SmMlmAliasList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 3),
    _SmMlmAliasList_Type()
)
smMlmAliasList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAliasList.setStatus("mandatory")
_SmMlmAliasResolvedList_Type = DisplayString
_SmMlmAliasResolvedList_Object = MibTableColumn
smMlmAliasResolvedList = _SmMlmAliasResolvedList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 8, 1, 1, 4),
    _SmMlmAliasResolvedList_Type()
)
smMlmAliasResolvedList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmAliasResolvedList.setStatus("mandatory")
_SmMlmTrapDestination_ObjectIdentity = ObjectIdentity
smMlmTrapDestination = _SmMlmTrapDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9)
)
_SmMlmTrapDestinationTable_Object = MibTable
smMlmTrapDestinationTable = _SmMlmTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1)
)
if mibBuilder.loadTexts:
    smMlmTrapDestinationTable.setStatus("mandatory")
_SmMlmTrapDestinationEntry_Object = MibTableRow
smMlmTrapDestinationEntry = _SmMlmTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1)
)
smMlmTrapDestinationEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmTrapDestinationName"),
)
if mibBuilder.loadTexts:
    smMlmTrapDestinationEntry.setStatus("mandatory")


class _SmMlmTrapDestinationState_Type(Integer32):
    """Custom type smMlmTrapDestinationState based on Integer32"""
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


_SmMlmTrapDestinationState_Type.__name__ = "Integer32"
_SmMlmTrapDestinationState_Object = MibTableColumn
smMlmTrapDestinationState = _SmMlmTrapDestinationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 1),
    _SmMlmTrapDestinationState_Type()
)
smMlmTrapDestinationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationState.setStatus("mandatory")
_SmMlmTrapDestinationName_Type = DisplayString
_SmMlmTrapDestinationName_Object = MibTableColumn
smMlmTrapDestinationName = _SmMlmTrapDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 2),
    _SmMlmTrapDestinationName_Type()
)
smMlmTrapDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationName.setStatus("mandatory")
_SmMlmTrapDestinationHost_Type = DisplayString
_SmMlmTrapDestinationHost_Object = MibTableColumn
smMlmTrapDestinationHost = _SmMlmTrapDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 3),
    _SmMlmTrapDestinationHost_Type()
)
smMlmTrapDestinationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationHost.setStatus("mandatory")
_SmMlmTrapDestinationMask_Type = Integer32
_SmMlmTrapDestinationMask_Object = MibTableColumn
smMlmTrapDestinationMask = _SmMlmTrapDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 4),
    _SmMlmTrapDestinationMask_Type()
)
smMlmTrapDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationMask.setStatus("mandatory")


class _SmMlmTrapDestinationParticipationState_Type(Integer32):
    """Custom type smMlmTrapDestinationParticipationState based on Integer32"""
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


_SmMlmTrapDestinationParticipationState_Type.__name__ = "Integer32"
_SmMlmTrapDestinationParticipationState_Object = MibTableColumn
smMlmTrapDestinationParticipationState = _SmMlmTrapDestinationParticipationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 5),
    _SmMlmTrapDestinationParticipationState_Type()
)
smMlmTrapDestinationParticipationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmTrapDestinationParticipationState.setStatus("mandatory")
_SmMlmTrapDestinationActivationTime_Type = DisplayString
_SmMlmTrapDestinationActivationTime_Object = MibTableColumn
smMlmTrapDestinationActivationTime = _SmMlmTrapDestinationActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 6),
    _SmMlmTrapDestinationActivationTime_Type()
)
smMlmTrapDestinationActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationActivationTime.setStatus("mandatory")
_SmMlmTrapDestinationActivationDayOfWeek_Type = DisplayString
_SmMlmTrapDestinationActivationDayOfWeek_Object = MibTableColumn
smMlmTrapDestinationActivationDayOfWeek = _SmMlmTrapDestinationActivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 7),
    _SmMlmTrapDestinationActivationDayOfWeek_Type()
)
smMlmTrapDestinationActivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationActivationDayOfWeek.setStatus("mandatory")
_SmMlmTrapDestinationDeactivationTime_Type = DisplayString
_SmMlmTrapDestinationDeactivationTime_Object = MibTableColumn
smMlmTrapDestinationDeactivationTime = _SmMlmTrapDestinationDeactivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 8),
    _SmMlmTrapDestinationDeactivationTime_Type()
)
smMlmTrapDestinationDeactivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationDeactivationTime.setStatus("mandatory")
_SmMlmTrapDestinationDeactivationDayOfWeek_Type = DisplayString
_SmMlmTrapDestinationDeactivationDayOfWeek_Object = MibTableColumn
smMlmTrapDestinationDeactivationDayOfWeek = _SmMlmTrapDestinationDeactivationDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 9),
    _SmMlmTrapDestinationDeactivationDayOfWeek_Type()
)
smMlmTrapDestinationDeactivationDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmTrapDestinationDeactivationDayOfWeek.setStatus("mandatory")
_SmMlmTrapDestinationMessages_Type = DisplayString
_SmMlmTrapDestinationMessages_Object = MibTableColumn
smMlmTrapDestinationMessages = _SmMlmTrapDestinationMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 9, 1, 1, 10),
    _SmMlmTrapDestinationMessages_Type()
)
smMlmTrapDestinationMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmTrapDestinationMessages.setStatus("mandatory")
_SmMlmAdministration_ObjectIdentity = ObjectIdentity
smMlmAdministration = _SmMlmAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10)
)
_SmMlmAdministrationTable_Object = MibTable
smMlmAdministrationTable = _SmMlmAdministrationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1)
)
if mibBuilder.loadTexts:
    smMlmAdministrationTable.setStatus("mandatory")
_SmMlmAdministrationEntry_Object = MibTableRow
smMlmAdministrationEntry = _SmMlmAdministrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1)
)
smMlmAdministrationEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmAdministrationFieldName"),
)
if mibBuilder.loadTexts:
    smMlmAdministrationEntry.setStatus("mandatory")


class _SmMlmAdministrationFieldState_Type(Integer32):
    """Custom type smMlmAdministrationFieldState based on Integer32"""
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


_SmMlmAdministrationFieldState_Type.__name__ = "Integer32"
_SmMlmAdministrationFieldState_Object = MibTableColumn
smMlmAdministrationFieldState = _SmMlmAdministrationFieldState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 1),
    _SmMlmAdministrationFieldState_Type()
)
smMlmAdministrationFieldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAdministrationFieldState.setStatus("mandatory")
_SmMlmAdministrationFieldName_Type = DisplayString
_SmMlmAdministrationFieldName_Object = MibTableColumn
smMlmAdministrationFieldName = _SmMlmAdministrationFieldName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 2),
    _SmMlmAdministrationFieldName_Type()
)
smMlmAdministrationFieldName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAdministrationFieldName.setStatus("mandatory")
_SmMlmAdministrationFieldOwner_Type = DisplayString
_SmMlmAdministrationFieldOwner_Object = MibTableColumn
smMlmAdministrationFieldOwner = _SmMlmAdministrationFieldOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 3),
    _SmMlmAdministrationFieldOwner_Type()
)
smMlmAdministrationFieldOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAdministrationFieldOwner.setStatus("mandatory")
_SmMlmAdministrationFieldDescription_Type = DisplayString
_SmMlmAdministrationFieldDescription_Object = MibTableColumn
smMlmAdministrationFieldDescription = _SmMlmAdministrationFieldDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 4),
    _SmMlmAdministrationFieldDescription_Type()
)
smMlmAdministrationFieldDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAdministrationFieldDescription.setStatus("mandatory")
_SmMlmAdministrationFieldValue_Type = DisplayString
_SmMlmAdministrationFieldValue_Object = MibTableColumn
smMlmAdministrationFieldValue = _SmMlmAdministrationFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 10, 1, 1, 5),
    _SmMlmAdministrationFieldValue_Type()
)
smMlmAdministrationFieldValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmAdministrationFieldValue.setStatus("mandatory")
_SmMlmStatusMonitor_ObjectIdentity = ObjectIdentity
smMlmStatusMonitor = _SmMlmStatusMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12)
)
_SmMlmStatusMonitorTable_Object = MibTable
smMlmStatusMonitorTable = _SmMlmStatusMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1)
)
if mibBuilder.loadTexts:
    smMlmStatusMonitorTable.setStatus("mandatory")
_SmMlmStatusMonitorEntry_Object = MibTableRow
smMlmStatusMonitorEntry = _SmMlmStatusMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1)
)
smMlmStatusMonitorEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmStatusMonitorName"),
)
if mibBuilder.loadTexts:
    smMlmStatusMonitorEntry.setStatus("mandatory")


class _SmMlmStatusMonitorState_Type(Integer32):
    """Custom type smMlmStatusMonitorState based on Integer32"""
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


_SmMlmStatusMonitorState_Type.__name__ = "Integer32"
_SmMlmStatusMonitorState_Object = MibTableColumn
smMlmStatusMonitorState = _SmMlmStatusMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 1),
    _SmMlmStatusMonitorState_Type()
)
smMlmStatusMonitorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorState.setStatus("mandatory")
_SmMlmStatusMonitorName_Type = DisplayString
_SmMlmStatusMonitorName_Object = MibTableColumn
smMlmStatusMonitorName = _SmMlmStatusMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 2),
    _SmMlmStatusMonitorName_Type()
)
smMlmStatusMonitorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorName.setStatus("mandatory")
_SmMlmStatusMonitorDescription_Type = DisplayString
_SmMlmStatusMonitorDescription_Object = MibTableColumn
smMlmStatusMonitorDescription = _SmMlmStatusMonitorDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 3),
    _SmMlmStatusMonitorDescription_Type()
)
smMlmStatusMonitorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorDescription.setStatus("mandatory")


class _SmMlmStatusMonitorAddressFamily_Type(Integer32):
    """Custom type smMlmStatusMonitorAddressFamily based on Integer32"""
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


_SmMlmStatusMonitorAddressFamily_Type.__name__ = "Integer32"
_SmMlmStatusMonitorAddressFamily_Object = MibTableColumn
smMlmStatusMonitorAddressFamily = _SmMlmStatusMonitorAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 4),
    _SmMlmStatusMonitorAddressFamily_Type()
)
smMlmStatusMonitorAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmStatusMonitorAddressFamily.setStatus("mandatory")
_SmMlmStatusMonitorGroup_Type = DisplayString
_SmMlmStatusMonitorGroup_Object = MibTableColumn
smMlmStatusMonitorGroup = _SmMlmStatusMonitorGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 5),
    _SmMlmStatusMonitorGroup_Type()
)
smMlmStatusMonitorGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorGroup.setStatus("mandatory")
_SmMlmStatusMonitorResolvedGroup_Type = DisplayString
_SmMlmStatusMonitorResolvedGroup_Object = MibTableColumn
smMlmStatusMonitorResolvedGroup = _SmMlmStatusMonitorResolvedGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 6),
    _SmMlmStatusMonitorResolvedGroup_Type()
)
smMlmStatusMonitorResolvedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmStatusMonitorResolvedGroup.setStatus("mandatory")
_SmMlmStatusMonitorUnresolvedGroup_Type = DisplayString
_SmMlmStatusMonitorUnresolvedGroup_Object = MibTableColumn
smMlmStatusMonitorUnresolvedGroup = _SmMlmStatusMonitorUnresolvedGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 7),
    _SmMlmStatusMonitorUnresolvedGroup_Type()
)
smMlmStatusMonitorUnresolvedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmStatusMonitorUnresolvedGroup.setStatus("mandatory")
_SmMlmStatusMonitorFrequency_Type = DisplayString
_SmMlmStatusMonitorFrequency_Object = MibTableColumn
smMlmStatusMonitorFrequency = _SmMlmStatusMonitorFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 8),
    _SmMlmStatusMonitorFrequency_Type()
)
smMlmStatusMonitorFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorFrequency.setStatus("mandatory")
_SmMlmStatusMonitorTimeout_Type = DisplayString
_SmMlmStatusMonitorTimeout_Object = MibTableColumn
smMlmStatusMonitorTimeout = _SmMlmStatusMonitorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 9),
    _SmMlmStatusMonitorTimeout_Type()
)
smMlmStatusMonitorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorTimeout.setStatus("mandatory")


class _SmMlmStatusMonitorMaxAttempts_Type(Integer32):
    """Custom type smMlmStatusMonitorMaxAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SmMlmStatusMonitorMaxAttempts_Type.__name__ = "Integer32"
_SmMlmStatusMonitorMaxAttempts_Object = MibTableColumn
smMlmStatusMonitorMaxAttempts = _SmMlmStatusMonitorMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 10),
    _SmMlmStatusMonitorMaxAttempts_Type()
)
smMlmStatusMonitorMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmStatusMonitorMaxAttempts.setStatus("mandatory")
_SmMlmStatusMonitorMessages_Type = DisplayString
_SmMlmStatusMonitorMessages_Object = MibTableColumn
smMlmStatusMonitorMessages = _SmMlmStatusMonitorMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 12, 1, 1, 11),
    _SmMlmStatusMonitorMessages_Type()
)
smMlmStatusMonitorMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmStatusMonitorMessages.setStatus("mandatory")
_SmMlmDiscovery_ObjectIdentity = ObjectIdentity
smMlmDiscovery = _SmMlmDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13)
)


class _SmMlmDiscoveryState_Type(Integer32):
    """Custom type smMlmDiscoveryState based on Integer32"""
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


_SmMlmDiscoveryState_Type.__name__ = "Integer32"
_SmMlmDiscoveryState_Object = MibScalar
smMlmDiscoveryState = _SmMlmDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 1),
    _SmMlmDiscoveryState_Type()
)
smMlmDiscoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryState.setStatus("mandatory")


class _SmMlmDiscoverySensor_Type(Integer32):
    """Custom type smMlmDiscoverySensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeSensing", 3),
          ("disabled", 1),
          ("passiveSensing", 2))
    )


_SmMlmDiscoverySensor_Type.__name__ = "Integer32"
_SmMlmDiscoverySensor_Object = MibScalar
smMlmDiscoverySensor = _SmMlmDiscoverySensor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 2),
    _SmMlmDiscoverySensor_Type()
)
smMlmDiscoverySensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoverySensor.setStatus("mandatory")


class _SmMlmDiscoverySensorMaxReads_Type(Integer32):
    """Custom type smMlmDiscoverySensorMaxReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 512),
    )


_SmMlmDiscoverySensorMaxReads_Type.__name__ = "Integer32"
_SmMlmDiscoverySensorMaxReads_Object = MibScalar
smMlmDiscoverySensorMaxReads = _SmMlmDiscoverySensorMaxReads_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 3),
    _SmMlmDiscoverySensorMaxReads_Type()
)
smMlmDiscoverySensorMaxReads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoverySensorMaxReads.setStatus("mandatory")
_SmMlmDiscoverySensorMaxInterval_Type = DisplayString
_SmMlmDiscoverySensorMaxInterval_Object = MibScalar
smMlmDiscoverySensorMaxInterval = _SmMlmDiscoverySensorMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 4),
    _SmMlmDiscoverySensorMaxInterval_Type()
)
smMlmDiscoverySensorMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoverySensorMaxInterval.setStatus("mandatory")


class _SmMlmDiscoveryBroadcastSearch_Type(Integer32):
    """Custom type smMlmDiscoveryBroadcastSearch based on Integer32"""
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
          ("enabledOnce", 2),
          ("enabledRepeated", 3))
    )


_SmMlmDiscoveryBroadcastSearch_Type.__name__ = "Integer32"
_SmMlmDiscoveryBroadcastSearch_Object = MibScalar
smMlmDiscoveryBroadcastSearch = _SmMlmDiscoveryBroadcastSearch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 5),
    _SmMlmDiscoveryBroadcastSearch_Type()
)
smMlmDiscoveryBroadcastSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryBroadcastSearch.setStatus("mandatory")
_SmMlmDiscoveryBroadcastSearchTime_Type = DisplayString
_SmMlmDiscoveryBroadcastSearchTime_Object = MibScalar
smMlmDiscoveryBroadcastSearchTime = _SmMlmDiscoveryBroadcastSearchTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 6),
    _SmMlmDiscoveryBroadcastSearchTime_Type()
)
smMlmDiscoveryBroadcastSearchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryBroadcastSearchTime.setStatus("mandatory")
_SmMlmDiscoveryBroadcastSearchDays_Type = DisplayString
_SmMlmDiscoveryBroadcastSearchDays_Object = MibScalar
smMlmDiscoveryBroadcastSearchDays = _SmMlmDiscoveryBroadcastSearchDays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 7),
    _SmMlmDiscoveryBroadcastSearchDays_Type()
)
smMlmDiscoveryBroadcastSearchDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryBroadcastSearchDays.setStatus("mandatory")


class _SmMlmDiscoveryBroadcastSearchNow_Type(Integer32):
    """Custom type smMlmDiscoveryBroadcastSearchNow based on Integer32"""
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


_SmMlmDiscoveryBroadcastSearchNow_Type.__name__ = "Integer32"
_SmMlmDiscoveryBroadcastSearchNow_Object = MibScalar
smMlmDiscoveryBroadcastSearchNow = _SmMlmDiscoveryBroadcastSearchNow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 8),
    _SmMlmDiscoveryBroadcastSearchNow_Type()
)
smMlmDiscoveryBroadcastSearchNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryBroadcastSearchNow.setStatus("mandatory")
_SmMlmDiscoveryNodeExpirationPeriod_Type = DisplayString
_SmMlmDiscoveryNodeExpirationPeriod_Object = MibScalar
smMlmDiscoveryNodeExpirationPeriod = _SmMlmDiscoveryNodeExpirationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 9),
    _SmMlmDiscoveryNodeExpirationPeriod_Type()
)
smMlmDiscoveryNodeExpirationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryNodeExpirationPeriod.setStatus("mandatory")
_SmMlmDiscoveryNotificationFrequency_Type = DisplayString
_SmMlmDiscoveryNotificationFrequency_Object = MibScalar
smMlmDiscoveryNotificationFrequency = _SmMlmDiscoveryNotificationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 10),
    _SmMlmDiscoveryNotificationFrequency_Type()
)
smMlmDiscoveryNotificationFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryNotificationFrequency.setStatus("mandatory")
_SmMlmDiscoveryNumberOfAddresses_Type = Integer32
_SmMlmDiscoveryNumberOfAddresses_Object = MibScalar
smMlmDiscoveryNumberOfAddresses = _SmMlmDiscoveryNumberOfAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 11),
    _SmMlmDiscoveryNumberOfAddresses_Type()
)
smMlmDiscoveryNumberOfAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryNumberOfAddresses.setStatus("mandatory")
_SmMlmDiscoveryMaxBridges_Type = Integer32
_SmMlmDiscoveryMaxBridges_Object = MibScalar
smMlmDiscoveryMaxBridges = _SmMlmDiscoveryMaxBridges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 12),
    _SmMlmDiscoveryMaxBridges_Type()
)
smMlmDiscoveryMaxBridges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smMlmDiscoveryMaxBridges.setStatus("mandatory")
_SmMlmDiscoveryMessages_Type = DisplayString
_SmMlmDiscoveryMessages_Object = MibScalar
smMlmDiscoveryMessages = _SmMlmDiscoveryMessages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 13),
    _SmMlmDiscoveryMessages_Type()
)
smMlmDiscoveryMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryMessages.setStatus("mandatory")
_SmMlmDiscoveryTable_Object = MibTable
smMlmDiscoveryTable = _SmMlmDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50)
)
if mibBuilder.loadTexts:
    smMlmDiscoveryTable.setStatus("mandatory")
_SmMlmDiscoveryEntry_Object = MibTableRow
smMlmDiscoveryEntry = _SmMlmDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1)
)
smMlmDiscoveryEntry.setIndexNames(
    (0, "MIDLEVELMGR-MIB", "smMlmDiscoveryAddressFamily"),
    (0, "MIDLEVELMGR-MIB", "smMlmDiscoveryRawNetAddress"),
)
if mibBuilder.loadTexts:
    smMlmDiscoveryEntry.setStatus("mandatory")


class _SmMlmDiscoveryAddressFamily_Type(Integer32):
    """Custom type smMlmDiscoveryAddressFamily based on Integer32"""
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


_SmMlmDiscoveryAddressFamily_Type.__name__ = "Integer32"
_SmMlmDiscoveryAddressFamily_Object = MibTableColumn
smMlmDiscoveryAddressFamily = _SmMlmDiscoveryAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 1),
    _SmMlmDiscoveryAddressFamily_Type()
)
smMlmDiscoveryAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryAddressFamily.setStatus("mandatory")
_SmMlmDiscoveryRawNetAddress_Type = OctetString
_SmMlmDiscoveryRawNetAddress_Object = MibTableColumn
smMlmDiscoveryRawNetAddress = _SmMlmDiscoveryRawNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 2),
    _SmMlmDiscoveryRawNetAddress_Type()
)
smMlmDiscoveryRawNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryRawNetAddress.setStatus("mandatory")
_SmMlmDiscoveryNetAddress_Type = DisplayString
_SmMlmDiscoveryNetAddress_Object = MibTableColumn
smMlmDiscoveryNetAddress = _SmMlmDiscoveryNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 3),
    _SmMlmDiscoveryNetAddress_Type()
)
smMlmDiscoveryNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryNetAddress.setStatus("mandatory")
_SmMlmDiscoveryRawMACAddress_Type = OctetString
_SmMlmDiscoveryRawMACAddress_Object = MibTableColumn
smMlmDiscoveryRawMACAddress = _SmMlmDiscoveryRawMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 4),
    _SmMlmDiscoveryRawMACAddress_Type()
)
smMlmDiscoveryRawMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryRawMACAddress.setStatus("mandatory")
_SmMlmDiscoveryMACAddress_Type = DisplayString
_SmMlmDiscoveryMACAddress_Object = MibTableColumn
smMlmDiscoveryMACAddress = _SmMlmDiscoveryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 5),
    _SmMlmDiscoveryMACAddress_Type()
)
smMlmDiscoveryMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryMACAddress.setStatus("mandatory")
_SmMlmDiscoveryRawTransposedMACAddress_Type = OctetString
_SmMlmDiscoveryRawTransposedMACAddress_Object = MibTableColumn
smMlmDiscoveryRawTransposedMACAddress = _SmMlmDiscoveryRawTransposedMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 6),
    _SmMlmDiscoveryRawTransposedMACAddress_Type()
)
smMlmDiscoveryRawTransposedMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryRawTransposedMACAddress.setStatus("mandatory")
_SmMlmDiscoveryTransposedMACAddress_Type = DisplayString
_SmMlmDiscoveryTransposedMACAddress_Object = MibTableColumn
smMlmDiscoveryTransposedMACAddress = _SmMlmDiscoveryTransposedMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 7),
    _SmMlmDiscoveryTransposedMACAddress_Type()
)
smMlmDiscoveryTransposedMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryTransposedMACAddress.setStatus("mandatory")
_SmMlmDiscoveryTimeLastSeen_Type = DisplayString
_SmMlmDiscoveryTimeLastSeen_Object = MibTableColumn
smMlmDiscoveryTimeLastSeen = _SmMlmDiscoveryTimeLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 8),
    _SmMlmDiscoveryTimeLastSeen_Type()
)
smMlmDiscoveryTimeLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryTimeLastSeen.setStatus("mandatory")
_SmMlmDiscoveryRawRoutingInformation_Type = OctetString
_SmMlmDiscoveryRawRoutingInformation_Object = MibTableColumn
smMlmDiscoveryRawRoutingInformation = _SmMlmDiscoveryRawRoutingInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 9),
    _SmMlmDiscoveryRawRoutingInformation_Type()
)
smMlmDiscoveryRawRoutingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryRawRoutingInformation.setStatus("mandatory")
_SmMlmDiscoveryRoutingInformation_Type = DisplayString
_SmMlmDiscoveryRoutingInformation_Object = MibTableColumn
smMlmDiscoveryRoutingInformation = _SmMlmDiscoveryRoutingInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 12, 13, 50, 1, 10),
    _SmMlmDiscoveryRoutingInformation_Type()
)
smMlmDiscoveryRoutingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMlmDiscoveryRoutingInformation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIDLEVELMGR-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "systemsMonitor6000": systemsMonitor6000,
       "smProgramInformation": smProgramInformation,
       "smMlmProgramData": smMlmProgramData,
       "smMlmProgramDescription": smMlmProgramDescription,
       "smMlmProgramName": smMlmProgramName,
       "smMlmProgramNumber": smMlmProgramNumber,
       "smMlmProgramVersion": smMlmProgramVersion,
       "smMlmProgramCompilationDate": smMlmProgramCompilationDate,
       "smMlmProgramUpTime": smMlmProgramUpTime,
       "smMlmProgramContact": smMlmProgramContact,
       "smMlmProgramControl": smMlmProgramControl,
       "smMlmProgramControlLocalConfigurationFile": smMlmProgramControlLocalConfigurationFile,
       "smMlmProgramControlSavedFlags": smMlmProgramControlSavedFlags,
       "smMlmProgramControlAgentAddress": smMlmProgramControlAgentAddress,
       "smMlmProgramControlMaxTcpTrapQueue": smMlmProgramControlMaxTcpTrapQueue,
       "smMlmProgramControlPercentMultiplier": smMlmProgramControlPercentMultiplier,
       "smMlmProgramControlSamplesPerInterval": smMlmProgramControlSamplesPerInterval,
       "smMlmProgramControlMaxOutstandingPingRequests": smMlmProgramControlMaxOutstandingPingRequests,
       "smMlmProgramControlRetryCount": smMlmProgramControlRetryCount,
       "smMlmProgramControlTimeout": smMlmProgramControlTimeout,
       "smMlmProgramControlCurrentFlags": smMlmProgramControlCurrentFlags,
       "smMlmProgramControlReinitFlags": smMlmProgramControlReinitFlags,
       "smMlmProgramControlReInitializeMonitor": smMlmProgramControlReInitializeMonitor,
       "smMlmProgramControlSaveConfiguration": smMlmProgramControlSaveConfiguration,
       "smMlmProgramLog": smMlmProgramLog,
       "smMlmProgramLogFileName": smMlmProgramLogFileName,
       "smMlmProgramLogFileSize": smMlmProgramLogFileSize,
       "smMlmProgramLogMaxFileSize": smMlmProgramLogMaxFileSize,
       "smMlmProgramLogNumFiles": smMlmProgramLogNumFiles,
       "smMlmProgramLogFileBehavior": smMlmProgramLogFileBehavior,
       "smMlmProgramLogMask": smMlmProgramLogMask,
       "smMlmProgramDataCollection": smMlmProgramDataCollection,
       "smMlmProgramDataCollectionFileName": smMlmProgramDataCollectionFileName,
       "smMlmProgramDataCollectionFileSize": smMlmProgramDataCollectionFileSize,
       "smMlmProgramDataCollectionMaxFileSize": smMlmProgramDataCollectionMaxFileSize,
       "smMlmProgramDataCollectionNumFiles": smMlmProgramDataCollectionNumFiles,
       "smMlmProgramDataCollectionFileBehavior": smMlmProgramDataCollectionFileBehavior,
       "smMlmProgramSetableTestObjects": smMlmProgramSetableTestObjects,
       "smMlmProgramControlSetableInteger": smMlmProgramControlSetableInteger,
       "smMlmProgramControlSetableCounter": smMlmProgramControlSetableCounter,
       "smMlmProgramControlSetableGauge": smMlmProgramControlSetableGauge,
       "smMlmProgramControlSetableIpAddress": smMlmProgramControlSetableIpAddress,
       "smMlmProgramControlSetableTimeTicks": smMlmProgramControlSetableTimeTicks,
       "smMlmProgramControlSetableOctetString": smMlmProgramControlSetableOctetString,
       "smMlmProgramTrapLog": smMlmProgramTrapLog,
       "smMlmProgramTrapLogFileName": smMlmProgramTrapLogFileName,
       "smMlmProgramTrapLogFileSize": smMlmProgramTrapLogFileSize,
       "smMlmProgramTrapLogMaxFileSize": smMlmProgramTrapLogMaxFileSize,
       "smMlmProgramTrapLogNumFiles": smMlmProgramTrapLogNumFiles,
       "smMlmProgramTrapLogFileBehavior": smMlmProgramTrapLogFileBehavior,
       "smMlmProgramTrapLogMask": smMlmProgramTrapLogMask,
       "smMlmResourceUsage": smMlmResourceUsage,
       "smMlmResourceUsageTable": smMlmResourceUsageTable,
       "smMlmResourceUsageEntry": smMlmResourceUsageEntry,
       "smMlmResourceUsageName": smMlmResourceUsageName,
       "smMlmResourceUsageUserTime": smMlmResourceUsageUserTime,
       "smMlmResourceUsageSystemTime": smMlmResourceUsageSystemTime,
       "smMlmResourceUsageTotalTime": smMlmResourceUsageTotalTime,
       "smMlmResourceUsageMaxrss": smMlmResourceUsageMaxrss,
       "smMlmResourceUsageIxrss": smMlmResourceUsageIxrss,
       "smMlmResourceUsageIdrss": smMlmResourceUsageIdrss,
       "smMlmResourceUsageIsrss": smMlmResourceUsageIsrss,
       "smMlmResourceUsageMinflt": smMlmResourceUsageMinflt,
       "smMlmResourceUsageMajflt": smMlmResourceUsageMajflt,
       "smMlmResourceUsageNSwap": smMlmResourceUsageNSwap,
       "smMlmResourceUsageInBlock": smMlmResourceUsageInBlock,
       "smMlmResourceUsageOutBlock": smMlmResourceUsageOutBlock,
       "smMlmResourceUsageMsgsnd": smMlmResourceUsageMsgsnd,
       "smMlmResourceUsageMsgrcv": smMlmResourceUsageMsgrcv,
       "smMlmResourceUsageNSignals": smMlmResourceUsageNSignals,
       "smMlmResourceUsageVcsw": smMlmResourceUsageVcsw,
       "smMlmResourceUsageIcsw": smMlmResourceUsageIcsw,
       "smMlmProgramMessages": smMlmProgramMessages,
       "smMlmProgramMessagesTable": smMlmProgramMessagesTable,
       "smMlmProgramMessagesEntry": smMlmProgramMessagesEntry,
       "smMlmProgramMessagesRowNumber": smMlmProgramMessagesRowNumber,
       "smMlmProgramMessagesTime": smMlmProgramMessagesTime,
       "smMlmProgramMessagesText": smMlmProgramMessagesText,
       "smMlmProgramMessagesTimeStamp": smMlmProgramMessagesTimeStamp,
       "smMlmProgramDataCollectTable": smMlmProgramDataCollectTable,
       "smMlmProgramDataCollectEntry": smMlmProgramDataCollectEntry,
       "smMlmProgramDataCollectRowNumber": smMlmProgramDataCollectRowNumber,
       "smMlmProgramDataCollectTime": smMlmProgramDataCollectTime,
       "smMlmProgramDataCollectText": smMlmProgramDataCollectText,
       "smMlmProgramDataCollectTimeStamp": smMlmProgramDataCollectTimeStamp,
       "smMlmProgramTrapTable": smMlmProgramTrapTable,
       "smMlmProgramTrapEntry": smMlmProgramTrapEntry,
       "smMlmProgramTrapRowNumber": smMlmProgramTrapRowNumber,
       "smMlmProgramTrapTime": smMlmProgramTrapTime,
       "smMlmProgramTrapText": smMlmProgramTrapText,
       "smMlmProgramTrapTimeStamp": smMlmProgramTrapTimeStamp,
       "smMlmProgramEnvironmentVars": smMlmProgramEnvironmentVars,
       "smMlmProgramEnvHostAddress": smMlmProgramEnvHostAddress,
       "smMlmProgramEnvHostName": smMlmProgramEnvHostName,
       "smMlmProgramEnvHostDomainName": smMlmProgramEnvHostDomainName,
       "smMlmProgramEnvTableVars": smMlmProgramEnvTableVars,
       "smMlmProgramEnvThresholdTableVars": smMlmProgramEnvThresholdTableVars,
       "smMlmProgramEnvThresholdName": smMlmProgramEnvThresholdName,
       "smMlmProgramEnvThresholdArmState": smMlmProgramEnvThresholdArmState,
       "smMlmProgramEnvThresholdCondition": smMlmProgramEnvThresholdCondition,
       "smMlmProgramEnvThresholdValue": smMlmProgramEnvThresholdValue,
       "smMlmProgramEnvThresholdNode": smMlmProgramEnvThresholdNode,
       "smMlmProgramEnvThresholdProxy": smMlmProgramEnvThresholdProxy,
       "smMlmProgramEnvThresholdAddressNode": smMlmProgramEnvThresholdAddressNode,
       "smMlmProgramEnvThresholdDomainName": smMlmProgramEnvThresholdDomainName,
       "smMlmProgramEnvThresholdPort": smMlmProgramEnvThresholdPort,
       "smMlmProgramEnvThresholdVarId": smMlmProgramEnvThresholdVarId,
       "smMlmProgramEnvThresholdVarType": smMlmProgramEnvThresholdVarType,
       "smMlmProgramEnvThresholdVarValue": smMlmProgramEnvThresholdVarValue,
       "smMlmProgramEnvThresholdSeverity": smMlmProgramEnvThresholdSeverity,
       "smMlmProgramEnvThresholdVarInstance": smMlmProgramEnvThresholdVarInstance,
       "smMlmNetworkInformation": smMlmNetworkInformation,
       "smMlmNetworkSessionInformation": smMlmNetworkSessionInformation,
       "smMlmNetworkSessionCount": smMlmNetworkSessionCount,
       "smMlmNetworkSessionTable": smMlmNetworkSessionTable,
       "smMlmNetworkSessionEntry": smMlmNetworkSessionEntry,
       "smMlmNetworkSessionName": smMlmNetworkSessionName,
       "smMlmNetworkSessionCurrentState": smMlmNetworkSessionCurrentState,
       "smMlmNetworkSessionLastStateChange": smMlmNetworkSessionLastStateChange,
       "smMlmNetworkSessionLastPollAttempt": smMlmNetworkSessionLastPollAttempt,
       "smMlmNetworkSessionAddressFamily": smMlmNetworkSessionAddressFamily,
       "smMlmNetworkSessionNetAddress": smMlmNetworkSessionNetAddress,
       "smMlmNetworkSessionTransmitAttempts": smMlmNetworkSessionTransmitAttempts,
       "smMlmNetworkSessionPacketsReceived": smMlmNetworkSessionPacketsReceived,
       "smMlmNetworkSessionLastTransmitTime": smMlmNetworkSessionLastTransmitTime,
       "smMlmNetworkSessionLastReceiveTime": smMlmNetworkSessionLastReceiveTime,
       "smMlmNetworkSessionMinimumResponseTime": smMlmNetworkSessionMinimumResponseTime,
       "smMlmNetworkSessionRecentAverageResponseTime": smMlmNetworkSessionRecentAverageResponseTime,
       "smMlmNetworkSessionLifeTimeAverageResponseTime": smMlmNetworkSessionLifeTimeAverageResponseTime,
       "smMlmNetworkSessionMaximumResponseTime": smMlmNetworkSessionMaximumResponseTime,
       "smMlmNetworkSessionMinimumResponseTimeStamp": smMlmNetworkSessionMinimumResponseTimeStamp,
       "smMlmNetworkSessionMaximumResponseTimeStamp": smMlmNetworkSessionMaximumResponseTimeStamp,
       "smMlmNetworkSessionProxyAddress": smMlmNetworkSessionProxyAddress,
       "smMlmNetworkSessionPort": smMlmNetworkSessionPort,
       "smMlmNetworkSessionDomainName": smMlmNetworkSessionDomainName,
       "smMlmNetworkIfStatusInformation": smMlmNetworkIfStatusInformation,
       "smMlmNetworkIfStatusTable": smMlmNetworkIfStatusTable,
       "smMlmNetworkIfStatusEntry": smMlmNetworkIfStatusEntry,
       "smMlmNetworkIfStatusAddressFamily": smMlmNetworkIfStatusAddressFamily,
       "smMlmNetworkIfStatusRawNetAddress": smMlmNetworkIfStatusRawNetAddress,
       "smMlmNetworkIfStatusNetAddress": smMlmNetworkIfStatusNetAddress,
       "smMlmNetworkIfStatusHostName": smMlmNetworkIfStatusHostName,
       "smMlmNetworkIfStatusMonitorEntryName": smMlmNetworkIfStatusMonitorEntryName,
       "smMlmNetworkIfStatusMonitorFrequency": smMlmNetworkIfStatusMonitorFrequency,
       "smMlmNetworkIfStatusCurrentState": smMlmNetworkIfStatusCurrentState,
       "smMlmNetworkIfStatusLastStateChange": smMlmNetworkIfStatusLastStateChange,
       "smMlmNetworkIfStatusLastStatusCheck": smMlmNetworkIfStatusLastStatusCheck,
       "smMlmNetworkIfStatusLastResponseTime": smMlmNetworkIfStatusLastResponseTime,
       "smMlmNetworkIfStatusResetRoundTripStats": smMlmNetworkIfStatusResetRoundTripStats,
       "smMlmNetworkIfStatusNumRequestsTransmitted": smMlmNetworkIfStatusNumRequestsTransmitted,
       "smMlmNetworkIfStatusNumResponsesReceived": smMlmNetworkIfStatusNumResponsesReceived,
       "smMlmNetworkIfStatusLastRoundTripTime": smMlmNetworkIfStatusLastRoundTripTime,
       "smMlmNetworkIfStatusAvgRoundTripTime": smMlmNetworkIfStatusAvgRoundTripTime,
       "smMlmNetworkIfStatusMinRoundTripTime": smMlmNetworkIfStatusMinRoundTripTime,
       "smMlmNetworkIfStatusMinRoundTripTimeStamp": smMlmNetworkIfStatusMinRoundTripTimeStamp,
       "smMlmNetworkIfStatusMaxRoundTripTime": smMlmNetworkIfStatusMaxRoundTripTime,
       "smMlmNetworkIfStatusMaxRoundTripTimeStamp": smMlmNetworkIfStatusMaxRoundTripTimeStamp,
       "smMlmNetworkIfStatusLastUp": smMlmNetworkIfStatusLastUp,
       "smMlmNetworkIfStatusLastDown": smMlmNetworkIfStatusLastDown,
       "smMlmThreshold": smMlmThreshold,
       "smMlmThresholdTable": smMlmThresholdTable,
       "smMlmThresholdEntry": smMlmThresholdEntry,
       "smMlmThresholdState": smMlmThresholdState,
       "smMlmThresholdName": smMlmThresholdName,
       "smMlmThresholdDescription": smMlmThresholdDescription,
       "smMlmThresholdOwnerID": smMlmThresholdOwnerID,
       "smMlmThresholdLocalRemoteMIBVariable": smMlmThresholdLocalRemoteMIBVariable,
       "smMlmThresholdCondition": smMlmThresholdCondition,
       "smMlmThresholdValue": smMlmThresholdValue,
       "smMlmThresholdPollTime": smMlmThresholdPollTime,
       "smMlmThresholdLastValue": smMlmThresholdLastValue,
       "smMlmThresholdIntegerDataMax": smMlmThresholdIntegerDataMax,
       "smMlmThresholdIntegerDataMin": smMlmThresholdIntegerDataMin,
       "smMlmThresholdIntegerDataAvg": smMlmThresholdIntegerDataAvg,
       "smMlmThresholdArmSeverity": smMlmThresholdArmSeverity,
       "smMlmThresholdReArmSeverity": smMlmThresholdReArmSeverity,
       "smMlmThresholdResultIndex": smMlmThresholdResultIndex,
       "smMlmThresholdResultsTableState": smMlmThresholdResultsTableState,
       "smMlmThresholdTrapDescription": smMlmThresholdTrapDescription,
       "smMlmThresholdArmEnterprise": smMlmThresholdArmEnterprise,
       "smMlmThresholdSpecificTrap": smMlmThresholdSpecificTrap,
       "smMlmThresholdCommandToExecute": smMlmThresholdCommandToExecute,
       "smMlmThresholdReArmCondition": smMlmThresholdReArmCondition,
       "smMlmThresholdReArmValue": smMlmThresholdReArmValue,
       "smMlmThresholdReArmTrapDescription": smMlmThresholdReArmTrapDescription,
       "smMlmThresholdReArmEnterprise": smMlmThresholdReArmEnterprise,
       "smMlmThresholdReArmSpecificTrap": smMlmThresholdReArmSpecificTrap,
       "smMlmThresholdReArmCommandToExecute": smMlmThresholdReArmCommandToExecute,
       "smMlmThresholdLastChangedSession": smMlmThresholdLastChangedSession,
       "smMlmThresholdStandardError": smMlmThresholdStandardError,
       "smMlmThresholdLastResponseTime": smMlmThresholdLastResponseTime,
       "smMlmThresholdResponseCount": smMlmThresholdResponseCount,
       "smMlmThresholdTimeoutCount": smMlmThresholdTimeoutCount,
       "smMlmThresholdNoValueCount": smMlmThresholdNoValueCount,
       "smMlmThresholdArmConditionMetCount": smMlmThresholdArmConditionMetCount,
       "smMlmThresholdReArmConditionMetCount": smMlmThresholdReArmConditionMetCount,
       "smMlmThresholdThrottleArmCount": smMlmThresholdThrottleArmCount,
       "smMlmThresholdThrottleReArmCount": smMlmThresholdThrottleReArmCount,
       "smMlmThresholdParticipationState": smMlmThresholdParticipationState,
       "smMlmThresholdActivationTime": smMlmThresholdActivationTime,
       "smMlmThresholdActivationDayOfWeek": smMlmThresholdActivationDayOfWeek,
       "smMlmThresholdDeactivationTime": smMlmThresholdDeactivationTime,
       "smMlmThresholdDeactivationDayOfWeek": smMlmThresholdDeactivationDayOfWeek,
       "smMlmThresholdArmInfoTable": smMlmThresholdArmInfoTable,
       "smMlmThresholdArmInfoEntry": smMlmThresholdArmInfoEntry,
       "smMlmThresholdArmInfoName": smMlmThresholdArmInfoName,
       "smMlmThresholdArmInfoIpAddress": smMlmThresholdArmInfoIpAddress,
       "smMlmThresholdArmInfoObjectID": smMlmThresholdArmInfoObjectID,
       "smMlmThresholdArmInfoIndex": smMlmThresholdArmInfoIndex,
       "smMlmThresholdResultsTable": smMlmThresholdResultsTable,
       "smMlmThresholdResultsEntry": smMlmThresholdResultsEntry,
       "smMlmThresholdResultsName": smMlmThresholdResultsName,
       "smMlmThresholdResultsIpAddress": smMlmThresholdResultsIpAddress,
       "smMlmThresholdResultsInstanceID": smMlmThresholdResultsInstanceID,
       "smMlmThresholdResultsIndex": smMlmThresholdResultsIndex,
       "smMlmThresholdResultsResultTimeStamp": smMlmThresholdResultsResultTimeStamp,
       "smMlmThresholdResultsResultIndex": smMlmThresholdResultsResultIndex,
       "smMlmThresholdResultsIntegerResult": smMlmThresholdResultsIntegerResult,
       "smMlmThresholdResultsCounterResult": smMlmThresholdResultsCounterResult,
       "smMlmThresholdResultsGaugeResult": smMlmThresholdResultsGaugeResult,
       "smMlmThresholdResultsDisplayStringResult": smMlmThresholdResultsDisplayStringResult,
       "smMlmThresholdResultsResetStats": smMlmThresholdResultsResetStats,
       "smMlmThresholdResultsLifeTimeIntegerMin": smMlmThresholdResultsLifeTimeIntegerMin,
       "smMlmThresholdResultsLifeTimeIntegerMax": smMlmThresholdResultsLifeTimeIntegerMax,
       "smMlmThresholdResultsLifeTimeIntegerAvg": smMlmThresholdResultsLifeTimeIntegerAvg,
       "smMlmThresholdResultsLifeTimeIntegerStdDeviation": smMlmThresholdResultsLifeTimeIntegerStdDeviation,
       "smMlmThresholdResultsLifeTimeCounterGaugeMin": smMlmThresholdResultsLifeTimeCounterGaugeMin,
       "smMlmThresholdResultsLifeTimeCounterGaugeMax": smMlmThresholdResultsLifeTimeCounterGaugeMax,
       "smMlmThresholdResultsLifeTimeCounterGaugeAvg": smMlmThresholdResultsLifeTimeCounterGaugeAvg,
       "smMlmThresholdResultsLifeTimeCounterGaugeStdDeviation": smMlmThresholdResultsLifeTimeCounterGaugeStdDeviation,
       "smMlmThresholdResultsLifeTimeSamples": smMlmThresholdResultsLifeTimeSamples,
       "smMlmThresholdResultsLifeTimeSeconds": smMlmThresholdResultsLifeTimeSeconds,
       "smMlmThresholdResultsLifeTimeMinTimeStamp": smMlmThresholdResultsLifeTimeMinTimeStamp,
       "smMlmThresholdResultsLifeTimeMaxTimeStamp": smMlmThresholdResultsLifeTimeMaxTimeStamp,
       "smMlmThresholdResultsIntervalIntegerMin": smMlmThresholdResultsIntervalIntegerMin,
       "smMlmThresholdResultsIntervalIntegerMax": smMlmThresholdResultsIntervalIntegerMax,
       "smMlmThresholdResultsIntervalIntegerAvg": smMlmThresholdResultsIntervalIntegerAvg,
       "smMlmThresholdResultsIntervalIntegerStdDeviation": smMlmThresholdResultsIntervalIntegerStdDeviation,
       "smMlmThresholdResultsIntervalCounterGaugeMin": smMlmThresholdResultsIntervalCounterGaugeMin,
       "smMlmThresholdResultsIntervalCounterGaugeMax": smMlmThresholdResultsIntervalCounterGaugeMax,
       "smMlmThresholdResultsIntervalCounterGaugeAvg": smMlmThresholdResultsIntervalCounterGaugeAvg,
       "smMlmThresholdResultsIntervalCounterGaugeStdDeviation": smMlmThresholdResultsIntervalCounterGaugeStdDeviation,
       "smMlmThresholdResultsIntervalSamples": smMlmThresholdResultsIntervalSamples,
       "smMlmThresholdResultsIntervalSeconds": smMlmThresholdResultsIntervalSeconds,
       "smMlmThresholdResultsIntervalRate": smMlmThresholdResultsIntervalRate,
       "smMlmAnalysis": smMlmAnalysis,
       "smMlmAnalysisTable": smMlmAnalysisTable,
       "smMlmAnalysisEntry": smMlmAnalysisEntry,
       "smMlmAnalysisState": smMlmAnalysisState,
       "smMlmAnalysisName": smMlmAnalysisName,
       "smMlmAnalysisDescription": smMlmAnalysisDescription,
       "smMlmAnalysisOwnerID": smMlmAnalysisOwnerID,
       "smMlmAnalysisLocalRemoteMIBVariableExpression": smMlmAnalysisLocalRemoteMIBVariableExpression,
       "smMlmAnalysisPollTime": smMlmAnalysisPollTime,
       "smMlmAnalysisResultIndex": smMlmAnalysisResultIndex,
       "smMlmAnalysisIntegerResult": smMlmAnalysisIntegerResult,
       "smMlmAnalysisCounterResult": smMlmAnalysisCounterResult,
       "smMlmAnalysisGaugeResult": smMlmAnalysisGaugeResult,
       "smMlmAnalysisDisplayStringResult": smMlmAnalysisDisplayStringResult,
       "smMlmAnalysisReturnCode": smMlmAnalysisReturnCode,
       "smMlmAnalysisStandardError": smMlmAnalysisStandardError,
       "smMlmFilter": smMlmFilter,
       "smMlmFilterDefaultAction": smMlmFilterDefaultAction,
       "smMlmFilterUdpTrapReception": smMlmFilterUdpTrapReception,
       "smMlmFilterTotalTrapsReceived": smMlmFilterTotalTrapsReceived,
       "smMlmFilterTable": smMlmFilterTable,
       "smMlmFilterEntry": smMlmFilterEntry,
       "smMlmFilterState": smMlmFilterState,
       "smMlmFilterParticipationState": smMlmFilterParticipationState,
       "smMlmFilterName": smMlmFilterName,
       "smMlmFilterDescription": smMlmFilterDescription,
       "smMlmFilterAction": smMlmFilterAction,
       "smMlmFilterEntryEnterpriseExpression": smMlmFilterEntryEnterpriseExpression,
       "smMlmFilterAgentAddrExpression": smMlmFilterAgentAddrExpression,
       "smMlmFilterGenericExpression": smMlmFilterGenericExpression,
       "smMlmFilterSpecificExpression": smMlmFilterSpecificExpression,
       "smMlmFilterVariableExpression": smMlmFilterVariableExpression,
       "smMlmFilterTotalTrapsMatched": smMlmFilterTotalTrapsMatched,
       "smMlmFilterActivationTime": smMlmFilterActivationTime,
       "smMlmFilterActivationDayOfWeek": smMlmFilterActivationDayOfWeek,
       "smMlmFilterDeactivationTime": smMlmFilterDeactivationTime,
       "smMlmFilterDeactivationDayOfWeek": smMlmFilterDeactivationDayOfWeek,
       "smMlmFilterTrapDestinations": smMlmFilterTrapDestinations,
       "smMlmFilterMatchedCommand": smMlmFilterMatchedCommand,
       "smMlmFilterMatchedTrapDescription": smMlmFilterMatchedTrapDescription,
       "smMlmFilterMatchedTrapEnterprise": smMlmFilterMatchedTrapEnterprise,
       "smMlmFilterMatchedSpecificTrap": smMlmFilterMatchedSpecificTrap,
       "smMlmFilterThrottleType": smMlmFilterThrottleType,
       "smMlmFilterThrottleArmTrapCount": smMlmFilterThrottleArmTrapCount,
       "smMlmFilterThrottleArmedCommand": smMlmFilterThrottleArmedCommand,
       "smMlmFilterThrottleArmedTrapDescription": smMlmFilterThrottleArmedTrapDescription,
       "smMlmFilterThrottleArmedTrapEnterprise": smMlmFilterThrottleArmedTrapEnterprise,
       "smMlmFilterThrottleArmedSpecificTrap": smMlmFilterThrottleArmedSpecificTrap,
       "smMlmFilterThrottleDisarmTimer": smMlmFilterThrottleDisarmTimer,
       "smMlmFilterThrottleDisarmTrapCount": smMlmFilterThrottleDisarmTrapCount,
       "smMlmFilterThrottleDisarmedCommand": smMlmFilterThrottleDisarmedCommand,
       "smMlmFilterThrottleDisarmedTrapDescription": smMlmFilterThrottleDisarmedTrapDescription,
       "smMlmFilterThrottleDisarmedTrapEnterprise": smMlmFilterThrottleDisarmedTrapEnterprise,
       "smMlmFilterThrottleDisarmedSpecificTrap": smMlmFilterThrottleDisarmedSpecificTrap,
       "smMlmFilterThrottleState": smMlmFilterThrottleState,
       "smMlmFilterThrottleTimeStarted": smMlmFilterThrottleTimeStarted,
       "smMlmFilterThrottleTrapCount": smMlmFilterThrottleTrapCount,
       "smMlmFilterMessages": smMlmFilterMessages,
       "smMlmFilterThrottleCriteria": smMlmFilterThrottleCriteria,
       "smMlmFilterThrottleVariables": smMlmFilterThrottleVariables,
       "smMlmFilterTcpTrapReception": smMlmFilterTcpTrapReception,
       "smMlmFilterTcpReceptionStatus": smMlmFilterTcpReceptionStatus,
       "smMlmFilterUdpReceptionStatus": smMlmFilterUdpReceptionStatus,
       "smMlmFilterUdpTrapReceptionPort": smMlmFilterUdpTrapReceptionPort,
       "smMlmFilterTcpTrapReceptionPort": smMlmFilterTcpTrapReceptionPort,
       "smMlmFilterTrapReceptionMessages": smMlmFilterTrapReceptionMessages,
       "smMlmAlias": smMlmAlias,
       "smMlmAliasTable": smMlmAliasTable,
       "smMlmAliasEntry": smMlmAliasEntry,
       "smMlmAliasState": smMlmAliasState,
       "smMlmAliasName": smMlmAliasName,
       "smMlmAliasList": smMlmAliasList,
       "smMlmAliasResolvedList": smMlmAliasResolvedList,
       "smMlmTrapDestination": smMlmTrapDestination,
       "smMlmTrapDestinationTable": smMlmTrapDestinationTable,
       "smMlmTrapDestinationEntry": smMlmTrapDestinationEntry,
       "smMlmTrapDestinationState": smMlmTrapDestinationState,
       "smMlmTrapDestinationName": smMlmTrapDestinationName,
       "smMlmTrapDestinationHost": smMlmTrapDestinationHost,
       "smMlmTrapDestinationMask": smMlmTrapDestinationMask,
       "smMlmTrapDestinationParticipationState": smMlmTrapDestinationParticipationState,
       "smMlmTrapDestinationActivationTime": smMlmTrapDestinationActivationTime,
       "smMlmTrapDestinationActivationDayOfWeek": smMlmTrapDestinationActivationDayOfWeek,
       "smMlmTrapDestinationDeactivationTime": smMlmTrapDestinationDeactivationTime,
       "smMlmTrapDestinationDeactivationDayOfWeek": smMlmTrapDestinationDeactivationDayOfWeek,
       "smMlmTrapDestinationMessages": smMlmTrapDestinationMessages,
       "smMlmAdministration": smMlmAdministration,
       "smMlmAdministrationTable": smMlmAdministrationTable,
       "smMlmAdministrationEntry": smMlmAdministrationEntry,
       "smMlmAdministrationFieldState": smMlmAdministrationFieldState,
       "smMlmAdministrationFieldName": smMlmAdministrationFieldName,
       "smMlmAdministrationFieldOwner": smMlmAdministrationFieldOwner,
       "smMlmAdministrationFieldDescription": smMlmAdministrationFieldDescription,
       "smMlmAdministrationFieldValue": smMlmAdministrationFieldValue,
       "smMlmStatusMonitor": smMlmStatusMonitor,
       "smMlmStatusMonitorTable": smMlmStatusMonitorTable,
       "smMlmStatusMonitorEntry": smMlmStatusMonitorEntry,
       "smMlmStatusMonitorState": smMlmStatusMonitorState,
       "smMlmStatusMonitorName": smMlmStatusMonitorName,
       "smMlmStatusMonitorDescription": smMlmStatusMonitorDescription,
       "smMlmStatusMonitorAddressFamily": smMlmStatusMonitorAddressFamily,
       "smMlmStatusMonitorGroup": smMlmStatusMonitorGroup,
       "smMlmStatusMonitorResolvedGroup": smMlmStatusMonitorResolvedGroup,
       "smMlmStatusMonitorUnresolvedGroup": smMlmStatusMonitorUnresolvedGroup,
       "smMlmStatusMonitorFrequency": smMlmStatusMonitorFrequency,
       "smMlmStatusMonitorTimeout": smMlmStatusMonitorTimeout,
       "smMlmStatusMonitorMaxAttempts": smMlmStatusMonitorMaxAttempts,
       "smMlmStatusMonitorMessages": smMlmStatusMonitorMessages,
       "smMlmDiscovery": smMlmDiscovery,
       "smMlmDiscoveryState": smMlmDiscoveryState,
       "smMlmDiscoverySensor": smMlmDiscoverySensor,
       "smMlmDiscoverySensorMaxReads": smMlmDiscoverySensorMaxReads,
       "smMlmDiscoverySensorMaxInterval": smMlmDiscoverySensorMaxInterval,
       "smMlmDiscoveryBroadcastSearch": smMlmDiscoveryBroadcastSearch,
       "smMlmDiscoveryBroadcastSearchTime": smMlmDiscoveryBroadcastSearchTime,
       "smMlmDiscoveryBroadcastSearchDays": smMlmDiscoveryBroadcastSearchDays,
       "smMlmDiscoveryBroadcastSearchNow": smMlmDiscoveryBroadcastSearchNow,
       "smMlmDiscoveryNodeExpirationPeriod": smMlmDiscoveryNodeExpirationPeriod,
       "smMlmDiscoveryNotificationFrequency": smMlmDiscoveryNotificationFrequency,
       "smMlmDiscoveryNumberOfAddresses": smMlmDiscoveryNumberOfAddresses,
       "smMlmDiscoveryMaxBridges": smMlmDiscoveryMaxBridges,
       "smMlmDiscoveryMessages": smMlmDiscoveryMessages,
       "smMlmDiscoveryTable": smMlmDiscoveryTable,
       "smMlmDiscoveryEntry": smMlmDiscoveryEntry,
       "smMlmDiscoveryAddressFamily": smMlmDiscoveryAddressFamily,
       "smMlmDiscoveryRawNetAddress": smMlmDiscoveryRawNetAddress,
       "smMlmDiscoveryNetAddress": smMlmDiscoveryNetAddress,
       "smMlmDiscoveryRawMACAddress": smMlmDiscoveryRawMACAddress,
       "smMlmDiscoveryMACAddress": smMlmDiscoveryMACAddress,
       "smMlmDiscoveryRawTransposedMACAddress": smMlmDiscoveryRawTransposedMACAddress,
       "smMlmDiscoveryTransposedMACAddress": smMlmDiscoveryTransposedMACAddress,
       "smMlmDiscoveryTimeLastSeen": smMlmDiscoveryTimeLastSeen,
       "smMlmDiscoveryRawRoutingInformation": smMlmDiscoveryRawRoutingInformation,
       "smMlmDiscoveryRoutingInformation": smMlmDiscoveryRoutingInformation}
)
