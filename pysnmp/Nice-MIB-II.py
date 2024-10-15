# SNMP MIB module (Nice-MIB-II) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nice-MIB-II
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:12 2024
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



class YesNo(Integer32):
    """Custom type YesNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )





class SeverityType(Integer32):
    """Custom type SeverityType based on Integer32"""
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
        *(("criticalError", 4),
          ("error", 3),
          ("noError", 1),
          ("warning", 2))
    )





class ClsErrorType(Integer32):
    """Custom type ClsErrorType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("allCLSModulesInitFailed", 19),
          ("callServerIsDown", 1),
          ("callServerLinkIsDown", 6),
          ("callServerTableIsFull", 18),
          ("clsModuleRestartFailed", 20),
          ("communicationProblemWithLogger", 12),
          ("dBServerIsDown", 4),
          ("dBServerIsNotInitializedProperly", 10),
          ("dBSpaceIsFull", 11),
          ("dispatchIsDown", 5),
          ("failureConnectionToDB", 9),
          ("loggerIsNotInitializedProperly", 15),
          ("noAvailableResources", 14),
          ("osDiskFailure", 21),
          ("problemWithNPLUS1Loggers", 17),
          ("problematicClockDifferencesWithLogger", 13),
          ("rcmIsDown", 2),
          ("rcmIsNotInitializedProperly", 16),
          ("recordingOnDemandIsNotEnabled", 7),
          ("schedulerServerIsDown", 3),
          ("schedulerServerIsNotInitializedProperly", 8))
    )





class RecordedMediaType(Integer32):
    """Custom type RecordedMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("screen", 2),
          ("voice", 1),
          ("voiceAndScreen", 3))
    )





class LoggerInitializationStatus(Integer32):
    """Custom type LoggerInitializationStatus based on Integer32"""
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
        *(("channelWasNotInitialized", 4),
          ("noConnectionToSwitch", 3),
          ("noLoggerWasFound", 2),
          ("rcmInternalComponentsError", 1))
    )





class OsDiskFailureType(Integer32):
    """Custom type OsDiskFailureType based on Integer32"""
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
        *(("faileDisk", 1),
          ("fixStarted", 2),
          ("missingDisk", 4),
          ("shutdownDirty", 3),
          ("unknownFailure", 5))
    )





class ClsTableType(Integer32):
    """Custom type ClsTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callsTable", 2),
          ("dbRecordsTable", 1),
          ("loginTable", 3))
    )





class ApplicationErrorType(Integer32):
    """Custom type ApplicationErrorType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("applicationServerIsDown", 2),
          ("caDbConnectionIsDown", 14),
          ("clsConnectionIsDown", 10),
          ("ctiDbConnectionIsDown", 13),
          ("dataBaseConnectionIsDown", 4),
          ("hostIsDown", 1),
          ("interactionDBConnectionIsDown", 16),
          ("loggerConnectionIsDown", 11),
          ("loggerWasNotAttachedToACLS", 9),
          ("nifDBConnectionIsDown", 15),
          ("playbackServerHostConnectionIsDown", 7),
          ("queryExecuterHostConnectionIsDown", 8),
          ("ruleEngineActionExecuterFailed", 21),
          ("ruleEngineActionExecuterIdle", 22),
          ("ruleEngineConfigurationError", 23),
          ("ruleEngineEventProviderFailed", 17),
          ("ruleEngineEventProviderIdle", 18),
          ("ruleEngineRuleGeneratorFailed", 19),
          ("ruleEngineRuleGeneratorIdle", 20),
          ("scConnectionIsDown", 12),
          ("storageCenterHostConnectionIsDown", 6),
          ("sysAdminHostConnectionIsDown", 3),
          ("userAdminHostConnectionIsDown", 5))
    )





class DriverErrorType(Integer32):
    """Custom type DriverErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationFileIsMissing", 3),
          ("driverIsDown", 2),
          ("driverIsUp", 1))
    )





class CTIEventsDBServerErrorType(Integer32):
    """Custom type CTIEventsDBServerErrorType based on Integer32"""
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
        *(("ctiDBLogSpaceIsFull", 3),
          ("ctiDBServerIsNotInitializedProperly", 1),
          ("ctiDBSpaceIsFull", 2),
          ("ctiFailureConnectionToCTIDB", 4),
          ("ctiFailureInsertCTIEvent", 6),
          ("ctiInvalidMessageReceived", 7),
          ("ctiMissingLookUpTable", 5),
          ("ctiRetentionFailure", 8))
    )





class LoggingInstanceType(Integer32):
    """Custom type LoggingInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("audioManagerModule", 1),
          ("autoDeletionModule", 5),
          ("channelsModule", 4),
          ("checkSumModule", 11),
          ("dataBaseModule", 2),
          ("diskModule", 3),
          ("dliDriverModule", 8),
          ("dongleModule", 10),
          ("general", 0),
          ("hardwareDriverModule", 6),
          ("nPlus1Module", 9),
          ("voipDriverModule", 7))
    )





class LoggingErrorType(Integer32):
    """Custom type LoggingErrorType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("communicationFailure", 1),
          ("diskProblem", 4),
          ("dongleProblem", 11),
          ("highStatisticslarmOnChannels", 16),
          ("initializationFailure", 3),
          ("invalidChecksum", 12),
          ("lineErrorOnChannels", 13),
          ("loggerQueryFailure", 2),
          ("lowFreeDiskSpace", 7),
          ("lowKeptDiskSpace", 9),
          ("lowStatisticsAlarmOnChannels", 15),
          ("noFreeDiskSpace", 8),
          ("noKeptDiskSpace", 10),
          ("nplus1RobMalfunction", 5),
          ("nplus1RobPowerFailure", 6),
          ("someChannelsNotRecording", 14))
    )





class CaptureInstanceType(Integer32):
    """Custom type CaptureInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("adif3Board", 1),
          ("adifBoard", 0),
          ("ali4Board", 17),
          ("aliBoard", 16),
          ("apaBoard", 2),
          ("btai2Board", 18),
          ("dliBoard", 12),
          ("etai2Board", 5),
          ("etaiBoard", 4),
          ("isac2Board", 11),
          ("isacBoard", 10),
          ("isdnBoard", 3),
          ("lafBoard", 13),
          ("lmopBoard", 15),
          ("nati2Board", 9),
          ("natiBoard", 8),
          ("ntcmBoard", 6),
          ("tdaBoard", 7),
          ("udaBoard", 14))
    )





class CaptureErrorType(Integer32):
    """Custom type CaptureErrorType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dspProblemInAlgorithmsBoard", 2),
          ("dspProblemInInterfaceBoard", 3),
          ("dspProblemInPlaybackBoard", 4),
          ("dspProblemInRecordingBoard", 1),
          ("internalProblemInAlgorithmsBoard", 6),
          ("internalProblemInInterfaceBoard", 7),
          ("internalProblemInPlaybackBoard", 8),
          ("internalProblemInRecordingBoard", 5),
          ("lineProblemInAlgorithmsBoard", 10),
          ("lineProblemInInterfaceBoard", 11),
          ("lineProblemInPlaybackBoard", 12),
          ("lineProblemInRecordingBoard", 9))
    )





class BackupErrorType(Integer32):
    """Custom type BackupErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("archivingSuspended", 7),
          ("communicationError", 4),
          ("deviceError", 2),
          ("hardDiskError", 5),
          ("mediaError", 1),
          ("recoveryFailed", 6),
          ("retrievalError", 3))
    )





class BackupInstanceType(Integer32):
    """Custom type BackupInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              49,
              50,
              51,
              52,
              53,
              54,
              55)
        )
    )
    namedValues = NamedValues(
        *(("hitachiDVDRam1Device", 53),
          ("hitachiDVDRam2Device", 54),
          ("hpDDS4Device", 13),
          ("hpDatDDS2AutoLoaderDevice", 9),
          ("hpDatDDS2Device", 0),
          ("hpDatDDS3AutoLoaderDevice", 2),
          ("hpDatDDS3Device", 1),
          ("hpMo1Device", 7),
          ("matsushitaDVDRam1Device", 52),
          ("matsushitaDVDRam2Device", 55),
          ("seaGateDatDDS4Device", 49),
          ("sonyAit1Device", 6),
          ("sonyAit2Device", 51),
          ("sonyDatDDS2Device", 3),
          ("sonyDatDDS3AutoLoaderDevice", 10),
          ("sonyDatDDS3Device", 4),
          ("sonyDatDDS4Device", 50),
          ("sonyMo1Device", 5),
          ("sonyMo2Device", 8),
          ("sonyait1autoloaderDevice", 11),
          ("srvsonyDatDDS2sdt7000Device", 12))
    )





class BackupErrorBSRVErrorCode(Integer32):
    """Custom type BackupErrorBSRVErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3735539,
              -2818031,
              -2424816,
              -1638383,
              -1572846,
              -1507312,
              -1441780,
              -1179630,
              -1114095,
              -1048563,
              -983028,
              -917486,
              -851950,
              -786415,
              -720879,
              -655343,
              -524270,
              -458735,
              -393198,
              -327662,
              -262126,
              -196590,
              -131054,
              -65518,
              0,
              1,
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
              14,
              15,
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
              33,
              34,
              720909,
              1310732,
              1835026)
        )
    )
    namedValues = NamedValues(
        *(("bsrv-ErrCode-AccessDeniedToMedia", 26),
          ("bsrv-ErrCode-AutoloaderHardware", 27),
          ("bsrv-ErrCode-BadCassette", 22),
          ("bsrv-ErrCode-BadMediaType", 20),
          ("bsrv-ErrCode-CannotAppendToMedia", 4),
          ("bsrv-ErrCode-CannotEjectMedia", 30),
          ("bsrv-ErrCode-CleaningCartridge", 23),
          ("bsrv-ErrCode-CommToRemoteTapeErr", 28),
          ("bsrv-ErrCode-DeviceCleaningRequired", 24),
          ("bsrv-ErrCode-DeviceHasTimedOut", 6),
          ("bsrv-ErrCode-DeviceNotConnected", 11),
          ("bsrv-ErrCode-DeviceOk", 0),
          ("bsrv-ErrCode-DeviceStillWorking", 33),
          ("bsrv-ErrCode-DiskFailure", 21),
          ("bsrv-ErrCode-DiskIsFull", 2),
          ("bsrv-ErrCode-EndOfMediumWasReached-PBUEOMEarlyWarn", -2424816),
          ("bsrv-ErrCode-EndOfMediumWasReached-PBUVolOverflow", -1507312),
          ("bsrv-ErrCode-FatNotSupported", 32),
          ("bsrv-ErrCode-GeneralHardwareError-BusFail", -786415),
          ("bsrv-ErrCode-GeneralHardwareError-BusFree", -720879),
          ("bsrv-ErrCode-GeneralHardwareError-DataOverrun", -655343),
          ("bsrv-ErrCode-GeneralHardwareError-Hardware", -1114095),
          ("bsrv-ErrCode-GeneralHardwareError-NoAdapter", -458735),
          ("bsrv-ErrCode-GeneralHardwareError-PBUHostBusReset", -2818031),
          ("bsrv-ErrCode-GeneralHardwareError-PBUIOErr", -1638383),
          ("bsrv-ErrCode-InternalError-Abort", -524270),
          ("bsrv-ErrCode-InternalError-AspiErr", -196590),
          ("bsrv-ErrCode-InternalError-AspiInval", -393198),
          ("bsrv-ErrCode-InternalError-Busy", -131054),
          ("bsrv-ErrCode-InternalError-IllegalReq", -1179630),
          ("bsrv-ErrCode-InternalError-InternalError", 1835026),
          ("bsrv-ErrCode-InternalError-Miscompare", -1572846),
          ("bsrv-ErrCode-InternalError-NoAspi", -65518),
          ("bsrv-ErrCode-InternalError-NoDevice", -327662),
          ("bsrv-ErrCode-InternalError-NoMem", -262126),
          ("bsrv-ErrCode-InternalError-Reservation", -917486),
          ("bsrv-ErrCode-InternalError-TargetBusy", -851950),
          ("bsrv-ErrCode-LoadCountExceeded", 29),
          ("bsrv-ErrCode-MediaHasBadHeader", 7),
          ("bsrv-ErrCode-MediaHasNotYetExpired", 5),
          ("bsrv-ErrCode-MediaIsBlank", 15),
          ("bsrv-ErrCode-MediaIsWriteProtected", 14),
          ("bsrv-ErrCode-MediaWasManualyEjected-NoMagazine", 1310732),
          ("bsrv-ErrCode-MediaWasManualyEjected-NotReady", -983028),
          ("bsrv-ErrCode-MediaWasManualyEjected-TargetAbort", -1441780),
          ("bsrv-ErrCode-MediumError-CRCError", -3735539),
          ("bsrv-ErrCode-MediumError-Medium", -1048563),
          ("bsrv-ErrCode-MediumError-ReadFromPbuFailed", 720909),
          ("bsrv-ErrCode-NewMediaWasDetected", 34),
          ("bsrv-ErrCode-NoFreeTokens", 1),
          ("bsrv-ErrCode-NoInitHeader", 19),
          ("bsrv-ErrCode-OldVersionCassette", 25),
          ("bsrv-ErrCode-RecoveryFailed", 10),
          ("bsrv-ErrCode-TablesSizeMismatch", 31),
          ("bsrv-ErrCode-TapeHasNoData", 8),
          ("bsrv-ErrCode-WrongFileSize", 3),
          ("bsrv-ErrCode-WrongLoggerId", 9))
    )





class BackupConfig(Integer32):
    """Custom type BackupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              2,
              3,
              4,
              5,
              6,
              100,
              101,
              102,
              110,
              111,
              112,
              120,
              121,
              122)
        )
    )
    namedValues = NamedValues(
        *(("bsrv-conf-autoarch-channalization-continousmode", 120),
          ("bsrv-conf-autoarch-channalization-periodicbackupmode", 121),
          ("bsrv-conf-autoarch-channalizationperiodicejectmode", 122),
          ("bsrv-conf-autoarch-mirroring-continousmode", 110),
          ("bsrv-conf-autoarch-mirroring-periodicbackupmode", 111),
          ("bsrv-conf-autoarch-mirroring-periodicejectmode", 112),
          ("bsrv-conf-autoarch-pool-continousmode", 100),
          ("bsrv-conf-autoarch-pool-periodicbackupmode", 101),
          ("bsrv-conf-autoarch-pool-periodicejectmode", 102),
          ("bsrv-conf-erase", 5),
          ("bsrv-conf-init", 4),
          ("bsrv-conf-manual-archiving", 2),
          ("bsrv-conf-not-used", 0),
          ("bsrv-conf-null", -1),
          ("bsrv-conf-retrieval", 3),
          ("bsrv-conf-retrieve-while-archiving", 6))
    )





class BackupDeviceState(Integer32):
    """Custom type BackupDeviceState based on Integer32"""
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
              19,
              20,
              21,
              22,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("cannotAppendOldMedia", 25),
          ("deviceArchiving", 4),
          ("deviceCleaning", 13),
          ("deviceClosing", 10),
          ("deviceConnectingToRTS", 19),
          ("deviceConnectionToRTSFailed", 21),
          ("deviceEmpty", 1),
          ("deviceErasing", 15),
          ("deviceError", 6),
          ("deviceFull", 5),
          ("deviceLoadingForReading", 7),
          ("deviceLoadingForWrite", 2),
          ("deviceMagazineIsExhausted", 14),
          ("deviceMirroringSuspended", 12),
          ("deviceReadyForReading", 8),
          ("deviceReadyForWrite", 3),
          ("deviceRecovering", 11),
          ("deviceRetrieving", 9),
          ("deviceVerifyingMagazine", 16),
          ("deviceWaitingForBSRVRestart", 20),
          ("deviceWaitingForUserEject", 26),
          ("occupiedRemoteDevice", 22))
    )





class LineErrorType(Integer32):
    """Custom type LineErrorType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ais", 5),
          ("fer", 1),
          ("flos", 4),
          ("ito", 11),
          ("los", 7),
          ("lsig", 9),
          ("mfas", 10),
          ("mlos", 2),
          ("nos", 6),
          ("pra", 3),
          ("rai", 13),
          ("swf", 12),
          ("ubal", 8),
          ("voipErr", 14))
    )





class BoardType(Integer32):
    """Custom type BoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("board-type-adif", 6),
          ("board-type-ali", 9),
          ("board-type-dli", 8),
          ("board-type-etai", 7),
          ("board-type-external", 14),
          ("board-type-isac", 12),
          ("board-type-isdn", 10),
          ("board-type-nati", 13),
          ("board-type-none", -1),
          ("board-type-ntcm", 11),
          ("hc-adif3-board", 0),
          ("hc-ali4-board", 5),
          ("hc-btai2-board", 3),
          ("hc-etai2-board", 1),
          ("hc-isac2-board", 2),
          ("hc-nati2-board", 4))
    )





class RdTaskType(Integer32):
    """Custom type RdTaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("sampleCompare", 9),
          ("totalCompare", 8))
    )





class TaskState(Integer32):
    """Custom type TaskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("endingDueTime", 2),
          ("notActive", 0),
          ("stuck", 3))
    )





class RdErrorType(Integer32):
    """Custom type RdErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clsAddressingGeneralError", 5),
          ("connectionToCLSLost", 3),
          ("connectionToLoggerLost", 4),
          ("exceptionWhileProcessing", 0),
          ("failedToInitializeApplication", 1),
          ("keepAliveHearbeatFailure", 2))
    )





class RdConnStatus(Integer32):
    """Custom type RdConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectionIsActive", 1),
          ("connectionLost", 2),
          ("connectionNotActive", 0))
    )




# TEXTUAL-CONVENTIONS



class HostLocalTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "YYMMDDHHMMSS"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



# MIB Managed Objects in the order of their OIDs

_Nice_ObjectIdentity = ObjectIdentity
nice = _Nice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167)
)
_NiceMib_2_ObjectIdentity = ObjectIdentity
niceMib_2 = _NiceMib_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1)
)
_TrapsInfo_ObjectIdentity = ObjectIdentity
trapsInfo = _TrapsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1)
)
_TrapSeverity_Type = SeverityType
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 1),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")
_TrapLoggerId_Type = DisplayString
_TrapLoggerId_Object = MibScalar
trapLoggerId = _TrapLoggerId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 2),
    _TrapLoggerId_Type()
)
trapLoggerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLoggerId.setStatus("mandatory")
_TrapRecordedMedia_Type = RecordedMediaType
_TrapRecordedMedia_Object = MibScalar
trapRecordedMedia = _TrapRecordedMedia_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 3),
    _TrapRecordedMedia_Type()
)
trapRecordedMedia.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapRecordedMedia.setStatus("mandatory")
_TrapLoggerInitialization_Type = LoggerInitializationStatus
_TrapLoggerInitialization_Object = MibScalar
trapLoggerInitialization = _TrapLoggerInitialization_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 4),
    _TrapLoggerInitialization_Type()
)
trapLoggerInitialization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLoggerInitialization.setStatus("mandatory")
_TrapDBErrorCode_Type = Integer32
_TrapDBErrorCode_Object = MibScalar
trapDBErrorCode = _TrapDBErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 5),
    _TrapDBErrorCode_Type()
)
trapDBErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDBErrorCode.setStatus("mandatory")
_TrapOsDiskFailure_Type = OsDiskFailureType
_TrapOsDiskFailure_Object = MibScalar
trapOsDiskFailure = _TrapOsDiskFailure_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 6),
    _TrapOsDiskFailure_Type()
)
trapOsDiskFailure.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapOsDiskFailure.setStatus("mandatory")
_TrapClsTableType_Type = ClsTableType
_TrapClsTableType_Object = MibScalar
trapClsTableType = _TrapClsTableType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 7),
    _TrapClsTableType_Type()
)
trapClsTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapClsTableType.setStatus("mandatory")
_TrapDiskUsage_Type = Integer32
_TrapDiskUsage_Object = MibScalar
trapDiskUsage = _TrapDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 8),
    _TrapDiskUsage_Type()
)
trapDiskUsage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDiskUsage.setStatus("mandatory")
_TrapLoggerInitializationStatus_Type = LoggerInitializationStatus
_TrapLoggerInitializationStatus_Object = MibScalar
trapLoggerInitializationStatus = _TrapLoggerInitializationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 9),
    _TrapLoggerInitializationStatus_Type()
)
trapLoggerInitializationStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLoggerInitializationStatus.setStatus("mandatory")
_TrapHostTime_Type = HostLocalTime
_TrapHostTime_Object = MibScalar
trapHostTime = _TrapHostTime_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 10),
    _TrapHostTime_Type()
)
trapHostTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapHostTime.setStatus("mandatory")
_TrapCLSId_Type = DisplayString
_TrapCLSId_Object = MibScalar
trapCLSId = _TrapCLSId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 11),
    _TrapCLSId_Type()
)
trapCLSId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapCLSId.setStatus("mandatory")
_TrapSCId_Type = DisplayString
_TrapSCId_Object = MibScalar
trapSCId = _TrapSCId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 12),
    _TrapSCId_Type()
)
trapSCId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSCId.setStatus("mandatory")
_TrapDBId_Type = DisplayString
_TrapDBId_Object = MibScalar
trapDBId = _TrapDBId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 13),
    _TrapDBId_Type()
)
trapDBId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDBId.setStatus("mandatory")
_TrapFileName_Type = DisplayString
_TrapFileName_Object = MibScalar
trapFileName = _TrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 14),
    _TrapFileName_Type()
)
trapFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapFileName.setStatus("mandatory")
_TrapDeviceId_Type = DisplayString
_TrapDeviceId_Object = MibScalar
trapDeviceId = _TrapDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 15),
    _TrapDeviceId_Type()
)
trapDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDeviceId.setStatus("mandatory")
_TrapRegistryKey_Type = DisplayString
_TrapRegistryKey_Object = MibScalar
trapRegistryKey = _TrapRegistryKey_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 16),
    _TrapRegistryKey_Type()
)
trapRegistryKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapRegistryKey.setStatus("mandatory")
_TrapVLModuleName_Type = DisplayString
_TrapVLModuleName_Object = MibScalar
trapVLModuleName = _TrapVLModuleName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 17),
    _TrapVLModuleName_Type()
)
trapVLModuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapVLModuleName.setStatus("mandatory")
_TrapVLModuleStatus_Type = SeverityType
_TrapVLModuleStatus_Object = MibScalar
trapVLModuleStatus = _TrapVLModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 18),
    _TrapVLModuleStatus_Type()
)
trapVLModuleStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapVLModuleStatus.setStatus("mandatory")
_TrapDiskDrive_Type = DisplayString
_TrapDiskDrive_Object = MibScalar
trapDiskDrive = _TrapDiskDrive_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 19),
    _TrapDiskDrive_Type()
)
trapDiskDrive.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDiskDrive.setStatus("mandatory")
_TrapLoggerIdInChain_Type = Integer32
_TrapLoggerIdInChain_Object = MibScalar
trapLoggerIdInChain = _TrapLoggerIdInChain_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 20),
    _TrapLoggerIdInChain_Type()
)
trapLoggerIdInChain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLoggerIdInChain.setStatus("mandatory")
_TrapFreeSpacePercentage_Type = Integer32
_TrapFreeSpacePercentage_Object = MibScalar
trapFreeSpacePercentage = _TrapFreeSpacePercentage_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 21),
    _TrapFreeSpacePercentage_Type()
)
trapFreeSpacePercentage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapFreeSpacePercentage.setStatus("mandatory")
_TrapKeptSpacePercentage_Type = Integer32
_TrapKeptSpacePercentage_Object = MibScalar
trapKeptSpacePercentage = _TrapKeptSpacePercentage_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 22),
    _TrapKeptSpacePercentage_Type()
)
trapKeptSpacePercentage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapKeptSpacePercentage.setStatus("mandatory")
_TrapChannelNumber_Type = Integer32
_TrapChannelNumber_Object = MibScalar
trapChannelNumber = _TrapChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 23),
    _TrapChannelNumber_Type()
)
trapChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapChannelNumber.setStatus("mandatory")
_TrapBoardNumber_Type = Integer32
_TrapBoardNumber_Object = MibScalar
trapBoardNumber = _TrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 24),
    _TrapBoardNumber_Type()
)
trapBoardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapBoardNumber.setStatus("mandatory")
_TrapDspNumber_Type = Integer32
_TrapDspNumber_Object = MibScalar
trapDspNumber = _TrapDspNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 25),
    _TrapDspNumber_Type()
)
trapDspNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDspNumber.setStatus("mandatory")
_TrapLineNumber_Type = Integer32
_TrapLineNumber_Object = MibScalar
trapLineNumber = _TrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 26),
    _TrapLineNumber_Type()
)
trapLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLineNumber.setStatus("mandatory")
_TrapLineProblem_Type = DisplayString
_TrapLineProblem_Object = MibScalar
trapLineProblem = _TrapLineProblem_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 27),
    _TrapLineProblem_Type()
)
trapLineProblem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLineProblem.setStatus("mandatory")
_TrapDataLineNumber_Type = Integer32
_TrapDataLineNumber_Object = MibScalar
trapDataLineNumber = _TrapDataLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 28),
    _TrapDataLineNumber_Type()
)
trapDataLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDataLineNumber.setStatus("mandatory")
_TrapDaughterBoardNumber_Type = Integer32
_TrapDaughterBoardNumber_Object = MibScalar
trapDaughterBoardNumber = _TrapDaughterBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 29),
    _TrapDaughterBoardNumber_Type()
)
trapDaughterBoardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDaughterBoardNumber.setStatus("mandatory")
_TrapSQLTableName_Type = DisplayString
_TrapSQLTableName_Object = MibScalar
trapSQLTableName = _TrapSQLTableName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 30),
    _TrapSQLTableName_Type()
)
trapSQLTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSQLTableName.setStatus("mandatory")
_TrapEventProviderId_Type = Integer32
_TrapEventProviderId_Object = MibScalar
trapEventProviderId = _TrapEventProviderId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 31),
    _TrapEventProviderId_Type()
)
trapEventProviderId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventProviderId.setStatus("mandatory")
_TrapRuleGeneratorId_Type = Integer32
_TrapRuleGeneratorId_Object = MibScalar
trapRuleGeneratorId = _TrapRuleGeneratorId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 32),
    _TrapRuleGeneratorId_Type()
)
trapRuleGeneratorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapRuleGeneratorId.setStatus("mandatory")
_TrapActionExecuterId_Type = Integer32
_TrapActionExecuterId_Object = MibScalar
trapActionExecuterId = _TrapActionExecuterId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 33),
    _TrapActionExecuterId_Type()
)
trapActionExecuterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapActionExecuterId.setStatus("mandatory")
_TrapLineErrorType_Type = LineErrorType
_TrapLineErrorType_Object = MibScalar
trapLineErrorType = _TrapLineErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 34),
    _TrapLineErrorType_Type()
)
trapLineErrorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLineErrorType.setStatus("mandatory")
_TrapRecordingChannel_Type = Integer32
_TrapRecordingChannel_Object = MibScalar
trapRecordingChannel = _TrapRecordingChannel_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 35),
    _TrapRecordingChannel_Type()
)
trapRecordingChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapRecordingChannel.setStatus("mandatory")
_TrapRecordingStartTime_Type = HostLocalTime
_TrapRecordingStartTime_Object = MibScalar
trapRecordingStartTime = _TrapRecordingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 36),
    _TrapRecordingStartTime_Type()
)
trapRecordingStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapRecordingStartTime.setStatus("mandatory")
_TrapRecordingStopTime_Type = HostLocalTime
_TrapRecordingStopTime_Object = MibScalar
trapRecordingStopTime = _TrapRecordingStopTime_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 37),
    _TrapRecordingStopTime_Type()
)
trapRecordingStopTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapRecordingStopTime.setStatus("mandatory")
_TrapNumOfChannels_Type = Integer32
_TrapNumOfChannels_Object = MibScalar
trapNumOfChannels = _TrapNumOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 38),
    _TrapNumOfChannels_Type()
)
trapNumOfChannels.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapNumOfChannels.setStatus("mandatory")
_TrapBoardOrLogicalTrunk_Type = Integer32
_TrapBoardOrLogicalTrunk_Object = MibScalar
trapBoardOrLogicalTrunk = _TrapBoardOrLogicalTrunk_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 39),
    _TrapBoardOrLogicalTrunk_Type()
)
trapBoardOrLogicalTrunk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapBoardOrLogicalTrunk.setStatus("mandatory")
_TrapChannelOrTimeslot_Type = Integer32
_TrapChannelOrTimeslot_Object = MibScalar
trapChannelOrTimeslot = _TrapChannelOrTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 40),
    _TrapChannelOrTimeslot_Type()
)
trapChannelOrTimeslot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapChannelOrTimeslot.setStatus("mandatory")
_TrapMateLogicalTrunk_Type = Integer32
_TrapMateLogicalTrunk_Object = MibScalar
trapMateLogicalTrunk = _TrapMateLogicalTrunk_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 41),
    _TrapMateLogicalTrunk_Type()
)
trapMateLogicalTrunk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapMateLogicalTrunk.setStatus("mandatory")
_TrapMateTimeslot_Type = Integer32
_TrapMateTimeslot_Object = MibScalar
trapMateTimeslot = _TrapMateTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 42),
    _TrapMateTimeslot_Type()
)
trapMateTimeslot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapMateTimeslot.setStatus("mandatory")
_TrapBoardType_Type = BoardType
_TrapBoardType_Object = MibScalar
trapBoardType = _TrapBoardType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 43),
    _TrapBoardType_Type()
)
trapBoardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapBoardType.setStatus("mandatory")
_TrapLogicalStreamNumber_Type = Integer32
_TrapLogicalStreamNumber_Object = MibScalar
trapLogicalStreamNumber = _TrapLogicalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 44),
    _TrapLogicalStreamNumber_Type()
)
trapLogicalStreamNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLogicalStreamNumber.setStatus("mandatory")
_TrapBackupConfig_Type = BackupConfig
_TrapBackupConfig_Object = MibScalar
trapBackupConfig = _TrapBackupConfig_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 45),
    _TrapBackupConfig_Type()
)
trapBackupConfig.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapBackupConfig.setStatus("mandatory")
_TrapBackupDeviceState_Type = BackupDeviceState
_TrapBackupDeviceState_Object = MibScalar
trapBackupDeviceState = _TrapBackupDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 1, 46),
    _TrapBackupDeviceState_Type()
)
trapBackupDeviceState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapBackupDeviceState.setStatus("mandatory")
_Cls_ObjectIdentity = ObjectIdentity
cls = _Cls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2)
)
_ClsRcm_ObjectIdentity = ObjectIdentity
clsRcm = _ClsRcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1)
)
_RcmName_Type = DisplayString
_RcmName_Object = MibScalar
rcmName = _RcmName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 1),
    _RcmName_Type()
)
rcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmName.setStatus("mandatory")
_RcmStatus_Type = SeverityType
_RcmStatus_Object = MibScalar
rcmStatus = _RcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 2),
    _RcmStatus_Type()
)
rcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmStatus.setStatus("mandatory")
_RcmPendingErrorsTable_Object = MibTable
rcmPendingErrorsTable = _RcmPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rcmPendingErrorsTable.setStatus("mandatory")
_RcmPendingErrorsEntry_Object = MibTableRow
rcmPendingErrorsEntry = _RcmPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 3, 1)
)
rcmPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "rcmErrorIndex"),
)
if mibBuilder.loadTexts:
    rcmPendingErrorsEntry.setStatus("mandatory")
_RcmErrorType_Type = ClsErrorType
_RcmErrorType_Object = MibTableColumn
rcmErrorType = _RcmErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 3, 1, 1),
    _RcmErrorType_Type()
)
rcmErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmErrorType.setStatus("mandatory")
_RcmErrorReflectedStatus_Type = SeverityType
_RcmErrorReflectedStatus_Object = MibTableColumn
rcmErrorReflectedStatus = _RcmErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 3, 1, 2),
    _RcmErrorReflectedStatus_Type()
)
rcmErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmErrorReflectedStatus.setStatus("mandatory")
_RcmErrorLoggerId_Type = DisplayString
_RcmErrorLoggerId_Object = MibTableColumn
rcmErrorLoggerId = _RcmErrorLoggerId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 3, 1, 3),
    _RcmErrorLoggerId_Type()
)
rcmErrorLoggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmErrorLoggerId.setStatus("optional")
_RcmErrorIndex_Type = Integer32
_RcmErrorIndex_Object = MibTableColumn
rcmErrorIndex = _RcmErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 3, 1, 4),
    _RcmErrorIndex_Type()
)
rcmErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcmErrorIndex.setStatus("mandatory")
_ClsCallServer_ObjectIdentity = ObjectIdentity
clsCallServer = _ClsCallServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2)
)
_CallServerName_Type = DisplayString
_CallServerName_Object = MibScalar
callServerName = _CallServerName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 1),
    _CallServerName_Type()
)
callServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callServerName.setStatus("mandatory")
_CallServerStatus_Type = SeverityType
_CallServerStatus_Object = MibScalar
callServerStatus = _CallServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 2),
    _CallServerStatus_Type()
)
callServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callServerStatus.setStatus("mandatory")
_CallServerPendingErrorsTable_Object = MibTable
callServerPendingErrorsTable = _CallServerPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    callServerPendingErrorsTable.setStatus("mandatory")
_CallServerPendingErrorsEntry_Object = MibTableRow
callServerPendingErrorsEntry = _CallServerPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 3, 1)
)
callServerPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "callServerErrorIndex"),
)
if mibBuilder.loadTexts:
    callServerPendingErrorsEntry.setStatus("mandatory")
_CallServerErrorType_Type = ClsErrorType
_CallServerErrorType_Object = MibTableColumn
callServerErrorType = _CallServerErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 3, 1, 1),
    _CallServerErrorType_Type()
)
callServerErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callServerErrorType.setStatus("mandatory")
_CallServerErrorReflectedStatus_Type = SeverityType
_CallServerErrorReflectedStatus_Object = MibTableColumn
callServerErrorReflectedStatus = _CallServerErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 3, 1, 2),
    _CallServerErrorReflectedStatus_Type()
)
callServerErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callServerErrorReflectedStatus.setStatus("mandatory")
_CallServerErrorIndex_Type = Integer32
_CallServerErrorIndex_Object = MibTableColumn
callServerErrorIndex = _CallServerErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 3, 1, 3),
    _CallServerErrorIndex_Type()
)
callServerErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callServerErrorIndex.setStatus("mandatory")
_ClsSchedulerServer_ObjectIdentity = ObjectIdentity
clsSchedulerServer = _ClsSchedulerServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3)
)
_SchedulerServerName_Type = DisplayString
_SchedulerServerName_Object = MibScalar
schedulerServerName = _SchedulerServerName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 1),
    _SchedulerServerName_Type()
)
schedulerServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerServerName.setStatus("mandatory")
_SchedulerServerStatus_Type = SeverityType
_SchedulerServerStatus_Object = MibScalar
schedulerServerStatus = _SchedulerServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 2),
    _SchedulerServerStatus_Type()
)
schedulerServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerServerStatus.setStatus("mandatory")
_SchedulerServerPendingErrorsTable_Object = MibTable
schedulerServerPendingErrorsTable = _SchedulerServerPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    schedulerServerPendingErrorsTable.setStatus("mandatory")
_SchedulerServerPendingErrorsEntry_Object = MibTableRow
schedulerServerPendingErrorsEntry = _SchedulerServerPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 3, 1)
)
schedulerServerPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "schedulerServerErrorIndex"),
)
if mibBuilder.loadTexts:
    schedulerServerPendingErrorsEntry.setStatus("mandatory")
_SchedulerServerErrorType_Type = ClsErrorType
_SchedulerServerErrorType_Object = MibTableColumn
schedulerServerErrorType = _SchedulerServerErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 3, 1, 1),
    _SchedulerServerErrorType_Type()
)
schedulerServerErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerServerErrorType.setStatus("mandatory")
_SchedulerServerErrorReflectedStatus_Type = SeverityType
_SchedulerServerErrorReflectedStatus_Object = MibTableColumn
schedulerServerErrorReflectedStatus = _SchedulerServerErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 3, 1, 2),
    _SchedulerServerErrorReflectedStatus_Type()
)
schedulerServerErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerServerErrorReflectedStatus.setStatus("mandatory")
_SchedulerServerErrorIndex_Type = Integer32
_SchedulerServerErrorIndex_Object = MibTableColumn
schedulerServerErrorIndex = _SchedulerServerErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 3, 1, 3),
    _SchedulerServerErrorIndex_Type()
)
schedulerServerErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerServerErrorIndex.setStatus("mandatory")
_ClsDbServer_ObjectIdentity = ObjectIdentity
clsDbServer = _ClsDbServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4)
)
_DbServerName_Type = DisplayString
_DbServerName_Object = MibScalar
dbServerName = _DbServerName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 1),
    _DbServerName_Type()
)
dbServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbServerName.setStatus("mandatory")
_DbServerStatus_Type = SeverityType
_DbServerStatus_Object = MibScalar
dbServerStatus = _DbServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 2),
    _DbServerStatus_Type()
)
dbServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbServerStatus.setStatus("mandatory")
_DbServerPendingErrorsTable_Object = MibTable
dbServerPendingErrorsTable = _DbServerPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    dbServerPendingErrorsTable.setStatus("mandatory")
_DbServerPendingErrorsEntry_Object = MibTableRow
dbServerPendingErrorsEntry = _DbServerPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 3, 1)
)
dbServerPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "dbServerErrorIndex"),
)
if mibBuilder.loadTexts:
    dbServerPendingErrorsEntry.setStatus("mandatory")
_DbServerErrorType_Type = ClsErrorType
_DbServerErrorType_Object = MibTableColumn
dbServerErrorType = _DbServerErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 3, 1, 1),
    _DbServerErrorType_Type()
)
dbServerErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbServerErrorType.setStatus("mandatory")
_DbServerErrorReflectedStatus_Type = SeverityType
_DbServerErrorReflectedStatus_Object = MibTableColumn
dbServerErrorReflectedStatus = _DbServerErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 3, 1, 2),
    _DbServerErrorReflectedStatus_Type()
)
dbServerErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbServerErrorReflectedStatus.setStatus("mandatory")
_DbServerDBErrorCode_Type = Integer32
_DbServerDBErrorCode_Object = MibTableColumn
dbServerDBErrorCode = _DbServerDBErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 3, 1, 3),
    _DbServerDBErrorCode_Type()
)
dbServerDBErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbServerDBErrorCode.setStatus("optional")
_DbServerErrorIndex_Type = Integer32
_DbServerErrorIndex_Object = MibTableColumn
dbServerErrorIndex = _DbServerErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 3, 1, 4),
    _DbServerErrorIndex_Type()
)
dbServerErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbServerErrorIndex.setStatus("mandatory")
_ClsDispatcher_ObjectIdentity = ObjectIdentity
clsDispatcher = _ClsDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5)
)
_ClsDispatcherName_Type = DisplayString
_ClsDispatcherName_Object = MibScalar
clsDispatcherName = _ClsDispatcherName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 1),
    _ClsDispatcherName_Type()
)
clsDispatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsDispatcherName.setStatus("mandatory")
_ClsDispatcherStatus_Type = SeverityType
_ClsDispatcherStatus_Object = MibScalar
clsDispatcherStatus = _ClsDispatcherStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 2),
    _ClsDispatcherStatus_Type()
)
clsDispatcherStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsDispatcherStatus.setStatus("mandatory")
_ClsDispatcherPendingErrorsTable_Object = MibTable
clsDispatcherPendingErrorsTable = _ClsDispatcherPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    clsDispatcherPendingErrorsTable.setStatus("mandatory")
_ClsDispatcherPendingErrorsEntry_Object = MibTableRow
clsDispatcherPendingErrorsEntry = _ClsDispatcherPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 3, 1)
)
clsDispatcherPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "clsDispatcherErrorIndex"),
)
if mibBuilder.loadTexts:
    clsDispatcherPendingErrorsEntry.setStatus("mandatory")
_ClsDispatcherErrorType_Type = ClsErrorType
_ClsDispatcherErrorType_Object = MibTableColumn
clsDispatcherErrorType = _ClsDispatcherErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 3, 1, 1),
    _ClsDispatcherErrorType_Type()
)
clsDispatcherErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsDispatcherErrorType.setStatus("mandatory")
_ClsDispatcherErrorReflectedStatus_Type = SeverityType
_ClsDispatcherErrorReflectedStatus_Object = MibTableColumn
clsDispatcherErrorReflectedStatus = _ClsDispatcherErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 3, 1, 2),
    _ClsDispatcherErrorReflectedStatus_Type()
)
clsDispatcherErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsDispatcherErrorReflectedStatus.setStatus("mandatory")
_ClsDispatcherErrorIndex_Type = Integer32
_ClsDispatcherErrorIndex_Object = MibTableColumn
clsDispatcherErrorIndex = _ClsDispatcherErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 3, 1, 3),
    _ClsDispatcherErrorIndex_Type()
)
clsDispatcherErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsDispatcherErrorIndex.setStatus("mandatory")
_ClsAgentConfig_ObjectIdentity = ObjectIdentity
clsAgentConfig = _ClsAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 6)
)
_ClsAgentIsRepeatingTraps_Type = YesNo
_ClsAgentIsRepeatingTraps_Object = MibScalar
clsAgentIsRepeatingTraps = _ClsAgentIsRepeatingTraps_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 6, 1),
    _ClsAgentIsRepeatingTraps_Type()
)
clsAgentIsRepeatingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsAgentIsRepeatingTraps.setStatus("mandatory")
_ClsAgentTrapsRepeatInterval_Type = Integer32
_ClsAgentTrapsRepeatInterval_Object = MibScalar
clsAgentTrapsRepeatInterval = _ClsAgentTrapsRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 6, 2),
    _ClsAgentTrapsRepeatInterval_Type()
)
clsAgentTrapsRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsAgentTrapsRepeatInterval.setStatus("mandatory")
_ClsAgentVersion_Type = DisplayString
_ClsAgentVersion_Object = MibScalar
clsAgentVersion = _ClsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 6, 3),
    _ClsAgentVersion_Type()
)
clsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsAgentVersion.setStatus("mandatory")
_Logger_ObjectIdentity = ObjectIdentity
logger = _Logger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3)
)
_MultiMediaLogger_ObjectIdentity = ObjectIdentity
multiMediaLogger = _MultiMediaLogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1)
)
_MmlName_Type = DisplayString
_MmlName_Object = MibScalar
mmlName = _MmlName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 1),
    _MmlName_Type()
)
mmlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlName.setStatus("mandatory")
_MmlStatus_Type = SeverityType
_MmlStatus_Object = MibScalar
mmlStatus = _MmlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 2),
    _MmlStatus_Type()
)
mmlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlStatus.setStatus("mandatory")
_MmlStorageSystem_ObjectIdentity = ObjectIdentity
mmlStorageSystem = _MmlStorageSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3)
)
_MmlStorageSystemName_Type = DisplayString
_MmlStorageSystemName_Object = MibScalar
mmlStorageSystemName = _MmlStorageSystemName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 1),
    _MmlStorageSystemName_Type()
)
mmlStorageSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlStorageSystemName.setStatus("mandatory")
_MmlStorageSystemStatus_Type = SeverityType
_MmlStorageSystemStatus_Object = MibScalar
mmlStorageSystemStatus = _MmlStorageSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 2),
    _MmlStorageSystemStatus_Type()
)
mmlStorageSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlStorageSystemStatus.setStatus("mandatory")
_MmlStorageSystemDiskUsage_Type = Integer32
_MmlStorageSystemDiskUsage_Object = MibScalar
mmlStorageSystemDiskUsage = _MmlStorageSystemDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 3),
    _MmlStorageSystemDiskUsage_Type()
)
mmlStorageSystemDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlStorageSystemDiskUsage.setStatus("mandatory")
_MmlDataSystem_ObjectIdentity = ObjectIdentity
mmlDataSystem = _MmlDataSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4)
)
_MmlDataSystemName_Type = DisplayString
_MmlDataSystemName_Object = MibScalar
mmlDataSystemName = _MmlDataSystemName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 1),
    _MmlDataSystemName_Type()
)
mmlDataSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlDataSystemName.setStatus("mandatory")
_MmlDataSystemStatus_Type = SeverityType
_MmlDataSystemStatus_Object = MibScalar
mmlDataSystemStatus = _MmlDataSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 2),
    _MmlDataSystemStatus_Type()
)
mmlDataSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlDataSystemStatus.setStatus("mandatory")
_MmlAutoDeletion_ObjectIdentity = ObjectIdentity
mmlAutoDeletion = _MmlAutoDeletion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5)
)
_MmlAutoDeletionName_Type = DisplayString
_MmlAutoDeletionName_Object = MibScalar
mmlAutoDeletionName = _MmlAutoDeletionName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 1),
    _MmlAutoDeletionName_Type()
)
mmlAutoDeletionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlAutoDeletionName.setStatus("mandatory")
_MmlAutoDeletionStatus_Type = SeverityType
_MmlAutoDeletionStatus_Object = MibScalar
mmlAutoDeletionStatus = _MmlAutoDeletionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 2),
    _MmlAutoDeletionStatus_Type()
)
mmlAutoDeletionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlAutoDeletionStatus.setStatus("mandatory")
_MmlAgentConfig_ObjectIdentity = ObjectIdentity
mmlAgentConfig = _MmlAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 6)
)
_MmlAgentIsRepeatingTraps_Type = YesNo
_MmlAgentIsRepeatingTraps_Object = MibScalar
mmlAgentIsRepeatingTraps = _MmlAgentIsRepeatingTraps_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 6, 1),
    _MmlAgentIsRepeatingTraps_Type()
)
mmlAgentIsRepeatingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmlAgentIsRepeatingTraps.setStatus("mandatory")
_MmlAgentTrapsRepeatInterval_Type = Integer32
_MmlAgentTrapsRepeatInterval_Object = MibScalar
mmlAgentTrapsRepeatInterval = _MmlAgentTrapsRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 6, 2),
    _MmlAgentTrapsRepeatInterval_Type()
)
mmlAgentTrapsRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmlAgentTrapsRepeatInterval.setStatus("mandatory")
_MmlAgentVersion_Type = DisplayString
_MmlAgentVersion_Object = MibScalar
mmlAgentVersion = _MmlAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 6, 3),
    _MmlAgentVersion_Type()
)
mmlAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmlAgentVersion.setStatus("mandatory")
_VoiceLogger_ObjectIdentity = ObjectIdentity
voiceLogger = _VoiceLogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2)
)
_VoiceLoggerName_Type = DisplayString
_VoiceLoggerName_Object = MibScalar
voiceLoggerName = _VoiceLoggerName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 1),
    _VoiceLoggerName_Type()
)
voiceLoggerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceLoggerName.setStatus("mandatory")
_VoiceLoggerStatus_Type = SeverityType
_VoiceLoggerStatus_Object = MibScalar
voiceLoggerStatus = _VoiceLoggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 2),
    _VoiceLoggerStatus_Type()
)
voiceLoggerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceLoggerStatus.setStatus("mandatory")
_VoiceLoggerLogging_ObjectIdentity = ObjectIdentity
voiceLoggerLogging = _VoiceLoggerLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3)
)
_LoggingName_Type = DisplayString
_LoggingName_Object = MibScalar
loggingName = _LoggingName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 1),
    _LoggingName_Type()
)
loggingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingName.setStatus("mandatory")
_LoggingStatus_Type = SeverityType
_LoggingStatus_Object = MibScalar
loggingStatus = _LoggingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 2),
    _LoggingStatus_Type()
)
loggingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingStatus.setStatus("mandatory")
_LoggingInstanceTable_Object = MibTable
loggingInstanceTable = _LoggingInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    loggingInstanceTable.setStatus("mandatory")
_LoggingInstanceEntry_Object = MibTableRow
loggingInstanceEntry = _LoggingInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3, 1)
)
loggingInstanceEntry.setIndexNames(
    (0, "Nice-MIB-II", "loggingInstanceIndex"),
)
if mibBuilder.loadTexts:
    loggingInstanceEntry.setStatus("mandatory")
_LoggingInstanceName_Type = DisplayString
_LoggingInstanceName_Object = MibTableColumn
loggingInstanceName = _LoggingInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3, 1, 1),
    _LoggingInstanceName_Type()
)
loggingInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingInstanceName.setStatus("mandatory")
_LoggingInstanceStatus_Type = SeverityType
_LoggingInstanceStatus_Object = MibTableColumn
loggingInstanceStatus = _LoggingInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3, 1, 2),
    _LoggingInstanceStatus_Type()
)
loggingInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingInstanceStatus.setStatus("mandatory")
_LoggingInstanceType_Type = LoggingInstanceType
_LoggingInstanceType_Object = MibTableColumn
loggingInstanceType = _LoggingInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3, 1, 3),
    _LoggingInstanceType_Type()
)
loggingInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingInstanceType.setStatus("mandatory")
_LoggingInstanceNumberInType_Type = Integer32
_LoggingInstanceNumberInType_Object = MibTableColumn
loggingInstanceNumberInType = _LoggingInstanceNumberInType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3, 1, 4),
    _LoggingInstanceNumberInType_Type()
)
loggingInstanceNumberInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingInstanceNumberInType.setStatus("mandatory")
_LoggingInstanceIndex_Type = Integer32
_LoggingInstanceIndex_Object = MibTableColumn
loggingInstanceIndex = _LoggingInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 3, 1, 5),
    _LoggingInstanceIndex_Type()
)
loggingInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingInstanceIndex.setStatus("mandatory")
_LoggingPendingErrorsTable_Object = MibTable
loggingPendingErrorsTable = _LoggingPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    loggingPendingErrorsTable.setStatus("mandatory")
_LoggingPendingErrorsEntry_Object = MibTableRow
loggingPendingErrorsEntry = _LoggingPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4, 1)
)
loggingPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "loggingErrorInstanceIndex"),
    (0, "Nice-MIB-II", "loggingErrorIndex"),
)
if mibBuilder.loadTexts:
    loggingPendingErrorsEntry.setStatus("mandatory")
_LoggingErrorType_Type = LoggingErrorType
_LoggingErrorType_Object = MibTableColumn
loggingErrorType = _LoggingErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4, 1, 1),
    _LoggingErrorType_Type()
)
loggingErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingErrorType.setStatus("mandatory")
_LoggingErrorReflectedStatus_Type = SeverityType
_LoggingErrorReflectedStatus_Object = MibTableColumn
loggingErrorReflectedStatus = _LoggingErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4, 1, 2),
    _LoggingErrorReflectedStatus_Type()
)
loggingErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingErrorReflectedStatus.setStatus("mandatory")
_LoggingErrorInstanceIndex_Type = Integer32
_LoggingErrorInstanceIndex_Object = MibTableColumn
loggingErrorInstanceIndex = _LoggingErrorInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4, 1, 3),
    _LoggingErrorInstanceIndex_Type()
)
loggingErrorInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingErrorInstanceIndex.setStatus("mandatory")
_LoggingErrorIndex_Type = Integer32
_LoggingErrorIndex_Object = MibTableColumn
loggingErrorIndex = _LoggingErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4, 1, 4),
    _LoggingErrorIndex_Type()
)
loggingErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingErrorIndex.setStatus("mandatory")
_LoggingErrorCode_Type = Integer32
_LoggingErrorCode_Object = MibTableColumn
loggingErrorCode = _LoggingErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 4, 1, 5),
    _LoggingErrorCode_Type()
)
loggingErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingErrorCode.setStatus("mandatory")
_VoiceLoggerCapture_ObjectIdentity = ObjectIdentity
voiceLoggerCapture = _VoiceLoggerCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4)
)
_CaptureName_Type = DisplayString
_CaptureName_Object = MibScalar
captureName = _CaptureName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 1),
    _CaptureName_Type()
)
captureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureName.setStatus("mandatory")
_CaptureStatus_Type = SeverityType
_CaptureStatus_Object = MibScalar
captureStatus = _CaptureStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 2),
    _CaptureStatus_Type()
)
captureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureStatus.setStatus("mandatory")
_CaptureInstanceTable_Object = MibTable
captureInstanceTable = _CaptureInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    captureInstanceTable.setStatus("mandatory")
_CaptureInstanceEntry_Object = MibTableRow
captureInstanceEntry = _CaptureInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3, 1)
)
captureInstanceEntry.setIndexNames(
    (0, "Nice-MIB-II", "captureInstanceIndex"),
)
if mibBuilder.loadTexts:
    captureInstanceEntry.setStatus("mandatory")
_CaptureInstanceName_Type = DisplayString
_CaptureInstanceName_Object = MibTableColumn
captureInstanceName = _CaptureInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3, 1, 1),
    _CaptureInstanceName_Type()
)
captureInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureInstanceName.setStatus("mandatory")
_CaptureInstanceStatus_Type = SeverityType
_CaptureInstanceStatus_Object = MibTableColumn
captureInstanceStatus = _CaptureInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3, 1, 2),
    _CaptureInstanceStatus_Type()
)
captureInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureInstanceStatus.setStatus("mandatory")
_CaptureInstanceType_Type = CaptureInstanceType
_CaptureInstanceType_Object = MibTableColumn
captureInstanceType = _CaptureInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3, 1, 3),
    _CaptureInstanceType_Type()
)
captureInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureInstanceType.setStatus("mandatory")
_CaptureInstanceNumberInType_Type = Integer32
_CaptureInstanceNumberInType_Object = MibTableColumn
captureInstanceNumberInType = _CaptureInstanceNumberInType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3, 1, 4),
    _CaptureInstanceNumberInType_Type()
)
captureInstanceNumberInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureInstanceNumberInType.setStatus("mandatory")
_CaptureInstanceIndex_Type = Integer32
_CaptureInstanceIndex_Object = MibTableColumn
captureInstanceIndex = _CaptureInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 3, 1, 5),
    _CaptureInstanceIndex_Type()
)
captureInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureInstanceIndex.setStatus("mandatory")
_CapturePendingErrorsTable_Object = MibTable
capturePendingErrorsTable = _CapturePendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4)
)
if mibBuilder.loadTexts:
    capturePendingErrorsTable.setStatus("mandatory")
_CapturePendingErrorsEntry_Object = MibTableRow
capturePendingErrorsEntry = _CapturePendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4, 1)
)
capturePendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "captureErrorInstanceIndex"),
    (0, "Nice-MIB-II", "captureErrorIndex"),
)
if mibBuilder.loadTexts:
    capturePendingErrorsEntry.setStatus("mandatory")
_CaptureErrorType_Type = CaptureErrorType
_CaptureErrorType_Object = MibTableColumn
captureErrorType = _CaptureErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4, 1, 1),
    _CaptureErrorType_Type()
)
captureErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureErrorType.setStatus("mandatory")
_CaptureErrorReflectedStatus_Type = SeverityType
_CaptureErrorReflectedStatus_Object = MibTableColumn
captureErrorReflectedStatus = _CaptureErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4, 1, 2),
    _CaptureErrorReflectedStatus_Type()
)
captureErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureErrorReflectedStatus.setStatus("mandatory")
_CaptureErrorInstanceIndex_Type = Integer32
_CaptureErrorInstanceIndex_Object = MibTableColumn
captureErrorInstanceIndex = _CaptureErrorInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4, 1, 3),
    _CaptureErrorInstanceIndex_Type()
)
captureErrorInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureErrorInstanceIndex.setStatus("mandatory")
_CaptureErrorIndex_Type = Integer32
_CaptureErrorIndex_Object = MibTableColumn
captureErrorIndex = _CaptureErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4, 1, 4),
    _CaptureErrorIndex_Type()
)
captureErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureErrorIndex.setStatus("mandatory")
_CaptureErrorCode_Type = Integer32
_CaptureErrorCode_Object = MibTableColumn
captureErrorCode = _CaptureErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 4, 1, 5),
    _CaptureErrorCode_Type()
)
captureErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureErrorCode.setStatus("mandatory")
_VoiceLoggerBackup_ObjectIdentity = ObjectIdentity
voiceLoggerBackup = _VoiceLoggerBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5)
)
_BackupName_Type = DisplayString
_BackupName_Object = MibScalar
backupName = _BackupName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 1),
    _BackupName_Type()
)
backupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupName.setStatus("mandatory")
_BackupStatus_Type = SeverityType
_BackupStatus_Object = MibScalar
backupStatus = _BackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 2),
    _BackupStatus_Type()
)
backupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupStatus.setStatus("mandatory")
_BackupInstanceTable_Object = MibTable
backupInstanceTable = _BackupInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    backupInstanceTable.setStatus("mandatory")
_BackupInstanceEntry_Object = MibTableRow
backupInstanceEntry = _BackupInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3, 1)
)
backupInstanceEntry.setIndexNames(
    (0, "Nice-MIB-II", "backupInstanceNumber"),
)
if mibBuilder.loadTexts:
    backupInstanceEntry.setStatus("mandatory")
_BackupInstanceName_Type = DisplayString
_BackupInstanceName_Object = MibTableColumn
backupInstanceName = _BackupInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3, 1, 1),
    _BackupInstanceName_Type()
)
backupInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupInstanceName.setStatus("mandatory")
_BackupInstanceStatus_Type = SeverityType
_BackupInstanceStatus_Object = MibTableColumn
backupInstanceStatus = _BackupInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3, 1, 2),
    _BackupInstanceStatus_Type()
)
backupInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupInstanceStatus.setStatus("mandatory")
_BackupInstanceNumber_Type = Integer32
_BackupInstanceNumber_Object = MibTableColumn
backupInstanceNumber = _BackupInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3, 1, 3),
    _BackupInstanceNumber_Type()
)
backupInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupInstanceNumber.setStatus("mandatory")
_BackupInstanceRemoteNumber_Type = Integer32
_BackupInstanceRemoteNumber_Object = MibTableColumn
backupInstanceRemoteNumber = _BackupInstanceRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3, 1, 4),
    _BackupInstanceRemoteNumber_Type()
)
backupInstanceRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupInstanceRemoteNumber.setStatus("mandatory")
_BackupInstanceType_Type = BackupInstanceType
_BackupInstanceType_Object = MibTableColumn
backupInstanceType = _BackupInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 3, 1, 5),
    _BackupInstanceType_Type()
)
backupInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupInstanceType.setStatus("mandatory")
_BackupPendingErrorsTable_Object = MibTable
backupPendingErrorsTable = _BackupPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4)
)
if mibBuilder.loadTexts:
    backupPendingErrorsTable.setStatus("mandatory")
_BackupPendingErrorsEntry_Object = MibTableRow
backupPendingErrorsEntry = _BackupPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4, 1)
)
backupPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "backupErrorInstanceIndex"),
    (0, "Nice-MIB-II", "backupErrorIndex"),
)
if mibBuilder.loadTexts:
    backupPendingErrorsEntry.setStatus("mandatory")
_BackupErrorType_Type = BackupErrorType
_BackupErrorType_Object = MibTableColumn
backupErrorType = _BackupErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4, 1, 1),
    _BackupErrorType_Type()
)
backupErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupErrorType.setStatus("mandatory")
_BackupErrorReflectedStatus_Type = SeverityType
_BackupErrorReflectedStatus_Object = MibTableColumn
backupErrorReflectedStatus = _BackupErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4, 1, 2),
    _BackupErrorReflectedStatus_Type()
)
backupErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupErrorReflectedStatus.setStatus("mandatory")
_BackupErrorBSRVErrorCode_Type = BackupErrorBSRVErrorCode
_BackupErrorBSRVErrorCode_Object = MibTableColumn
backupErrorBSRVErrorCode = _BackupErrorBSRVErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4, 1, 3),
    _BackupErrorBSRVErrorCode_Type()
)
backupErrorBSRVErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupErrorBSRVErrorCode.setStatus("mandatory")
_BackupErrorInstanceIndex_Type = Integer32
_BackupErrorInstanceIndex_Object = MibTableColumn
backupErrorInstanceIndex = _BackupErrorInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4, 1, 4),
    _BackupErrorInstanceIndex_Type()
)
backupErrorInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupErrorInstanceIndex.setStatus("mandatory")
_BackupErrorIndex_Type = Integer32
_BackupErrorIndex_Object = MibTableColumn
backupErrorIndex = _BackupErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 4, 1, 5),
    _BackupErrorIndex_Type()
)
backupErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupErrorIndex.setStatus("mandatory")
_VoiceLoggerSnmpAgentConfig_ObjectIdentity = ObjectIdentity
voiceLoggerSnmpAgentConfig = _VoiceLoggerSnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 6)
)
_VoiceLoggerAgentIsRepeatingTraps_Type = YesNo
_VoiceLoggerAgentIsRepeatingTraps_Object = MibScalar
voiceLoggerAgentIsRepeatingTraps = _VoiceLoggerAgentIsRepeatingTraps_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 6, 1),
    _VoiceLoggerAgentIsRepeatingTraps_Type()
)
voiceLoggerAgentIsRepeatingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceLoggerAgentIsRepeatingTraps.setStatus("mandatory")
_VoiceLoggerTrapsRepeatInterval_Type = Integer32
_VoiceLoggerTrapsRepeatInterval_Object = MibScalar
voiceLoggerTrapsRepeatInterval = _VoiceLoggerTrapsRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 6, 2),
    _VoiceLoggerTrapsRepeatInterval_Type()
)
voiceLoggerTrapsRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceLoggerTrapsRepeatInterval.setStatus("mandatory")
_VoiceLoggerAgentVersion_Type = DisplayString
_VoiceLoggerAgentVersion_Object = MibScalar
voiceLoggerAgentVersion = _VoiceLoggerAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 6, 3),
    _VoiceLoggerAgentVersion_Type()
)
voiceLoggerAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceLoggerAgentVersion.setStatus("mandatory")
_Drivers_ObjectIdentity = ObjectIdentity
drivers = _Drivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4)
)
_DriversTable_Object = MibTable
driversTable = _DriversTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1)
)
if mibBuilder.loadTexts:
    driversTable.setStatus("mandatory")
_DriversEntry_Object = MibTableRow
driversEntry = _DriversEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1)
)
driversEntry.setIndexNames(
    (0, "Nice-MIB-II", "driverId"),
)
if mibBuilder.loadTexts:
    driversEntry.setStatus("mandatory")
_DriverName_Type = DisplayString
_DriverName_Object = MibTableColumn
driverName = _DriverName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1, 1),
    _DriverName_Type()
)
driverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverName.setStatus("mandatory")
_DriverStatus_Type = SeverityType
_DriverStatus_Object = MibTableColumn
driverStatus = _DriverStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1, 2),
    _DriverStatus_Type()
)
driverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverStatus.setStatus("mandatory")
_DriverId_Type = Integer32
_DriverId_Object = MibTableColumn
driverId = _DriverId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1, 3),
    _DriverId_Type()
)
driverId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverId.setStatus("mandatory")
_DriverNumberOfDevicesMonitored_Type = Integer32
_DriverNumberOfDevicesMonitored_Object = MibTableColumn
driverNumberOfDevicesMonitored = _DriverNumberOfDevicesMonitored_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1, 4),
    _DriverNumberOfDevicesMonitored_Type()
)
driverNumberOfDevicesMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverNumberOfDevicesMonitored.setStatus("mandatory")
_DriverNumberOfSegments_Type = Integer32
_DriverNumberOfSegments_Object = MibTableColumn
driverNumberOfSegments = _DriverNumberOfSegments_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1, 5),
    _DriverNumberOfSegments_Type()
)
driverNumberOfSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverNumberOfSegments.setStatus("mandatory")
_DriverNumberOfCompound_Type = Integer32
_DriverNumberOfCompound_Object = MibTableColumn
driverNumberOfCompound = _DriverNumberOfCompound_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 1, 6),
    _DriverNumberOfCompound_Type()
)
driverNumberOfCompound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverNumberOfCompound.setStatus("mandatory")
_DriverModulesTable_Object = MibTable
driverModulesTable = _DriverModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2)
)
if mibBuilder.loadTexts:
    driverModulesTable.setStatus("mandatory")
_DriverModulesEntry_Object = MibTableRow
driverModulesEntry = _DriverModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 1)
)
driverModulesEntry.setIndexNames(
    (0, "Nice-MIB-II", "driverIdInModulesTable"),
    (0, "Nice-MIB-II", "driverModuleId"),
)
if mibBuilder.loadTexts:
    driverModulesEntry.setStatus("mandatory")
_DriverModuleName_Type = DisplayString
_DriverModuleName_Object = MibTableColumn
driverModuleName = _DriverModuleName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 1, 1),
    _DriverModuleName_Type()
)
driverModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverModuleName.setStatus("mandatory")
_DriverModuleStatus_Type = SeverityType
_DriverModuleStatus_Object = MibTableColumn
driverModuleStatus = _DriverModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 1, 2),
    _DriverModuleStatus_Type()
)
driverModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverModuleStatus.setStatus("mandatory")
_DriverIdInModulesTable_Type = Integer32
_DriverIdInModulesTable_Object = MibTableColumn
driverIdInModulesTable = _DriverIdInModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 1, 3),
    _DriverIdInModulesTable_Type()
)
driverIdInModulesTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverIdInModulesTable.setStatus("mandatory")
_DriverModuleId_Type = Integer32
_DriverModuleId_Object = MibTableColumn
driverModuleId = _DriverModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 1, 4),
    _DriverModuleId_Type()
)
driverModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverModuleId.setStatus("mandatory")
_DriversPendingErrorsTable_Object = MibTable
driversPendingErrorsTable = _DriversPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 3)
)
if mibBuilder.loadTexts:
    driversPendingErrorsTable.setStatus("mandatory")
_DriversPendingErrorsEntry_Object = MibTableRow
driversPendingErrorsEntry = _DriversPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 3, 1)
)
driversPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "driverIdInDriversErrors"),
    (0, "Nice-MIB-II", "driverErrorIndex"),
)
if mibBuilder.loadTexts:
    driversPendingErrorsEntry.setStatus("mandatory")
_DriverErrorType_Type = DriverErrorType
_DriverErrorType_Object = MibTableColumn
driverErrorType = _DriverErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 3, 1, 1),
    _DriverErrorType_Type()
)
driverErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverErrorType.setStatus("mandatory")
_DriverErrorReflectedStatus_Type = SeverityType
_DriverErrorReflectedStatus_Object = MibTableColumn
driverErrorReflectedStatus = _DriverErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 3, 1, 2),
    _DriverErrorReflectedStatus_Type()
)
driverErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverErrorReflectedStatus.setStatus("mandatory")
_DriverIdInDriversErrors_Type = Integer32
_DriverIdInDriversErrors_Object = MibTableColumn
driverIdInDriversErrors = _DriverIdInDriversErrors_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 3, 1, 3),
    _DriverIdInDriversErrors_Type()
)
driverIdInDriversErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverIdInDriversErrors.setStatus("mandatory")
_DriverErrorIndex_Type = Integer32
_DriverErrorIndex_Object = MibTableColumn
driverErrorIndex = _DriverErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 3, 1, 4),
    _DriverErrorIndex_Type()
)
driverErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverErrorIndex.setStatus("mandatory")
_DriversModulePendingErrorsTable_Object = MibTable
driversModulePendingErrorsTable = _DriversModulePendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4)
)
if mibBuilder.loadTexts:
    driversModulePendingErrorsTable.setStatus("mandatory")
_DriversModulePendingErrorsEntry_Object = MibTableRow
driversModulePendingErrorsEntry = _DriversModulePendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4, 1)
)
driversModulePendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "driverIdInDriversErrors"),
    (0, "Nice-MIB-II", "driverErrorIndex"),
)
if mibBuilder.loadTexts:
    driversModulePendingErrorsEntry.setStatus("mandatory")
_DriverModuleErrorType_Type = DriverErrorType
_DriverModuleErrorType_Object = MibTableColumn
driverModuleErrorType = _DriverModuleErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4, 1, 1),
    _DriverModuleErrorType_Type()
)
driverModuleErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverModuleErrorType.setStatus("mandatory")
_DriverModuleErrorReflectedStatus_Type = SeverityType
_DriverModuleErrorReflectedStatus_Object = MibTableColumn
driverModuleErrorReflectedStatus = _DriverModuleErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4, 1, 2),
    _DriverModuleErrorReflectedStatus_Type()
)
driverModuleErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverModuleErrorReflectedStatus.setStatus("mandatory")
_DriverIdInDriverModulesErrors_Type = Integer32
_DriverIdInDriverModulesErrors_Object = MibTableColumn
driverIdInDriverModulesErrors = _DriverIdInDriverModulesErrors_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4, 1, 3),
    _DriverIdInDriverModulesErrors_Type()
)
driverIdInDriverModulesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverIdInDriverModulesErrors.setStatus("mandatory")
_ModuleIdInModulesErrors_Type = Integer32
_ModuleIdInModulesErrors_Object = MibTableColumn
moduleIdInModulesErrors = _ModuleIdInModulesErrors_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4, 1, 4),
    _ModuleIdInModulesErrors_Type()
)
moduleIdInModulesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIdInModulesErrors.setStatus("mandatory")
_DriverModuleErrorIndex_Type = Integer32
_DriverModuleErrorIndex_Object = MibTableColumn
driverModuleErrorIndex = _DriverModuleErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 4, 1, 5),
    _DriverModuleErrorIndex_Type()
)
driverModuleErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverModuleErrorIndex.setStatus("mandatory")
_DriversSnmpAgentConfig_ObjectIdentity = ObjectIdentity
driversSnmpAgentConfig = _DriversSnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 5)
)
_DriversAgentIsRepeatingTraps_Type = YesNo
_DriversAgentIsRepeatingTraps_Object = MibScalar
driversAgentIsRepeatingTraps = _DriversAgentIsRepeatingTraps_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 5, 1),
    _DriversAgentIsRepeatingTraps_Type()
)
driversAgentIsRepeatingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    driversAgentIsRepeatingTraps.setStatus("mandatory")
_DriversAgentTrapsRepeatInterval_Type = Integer32
_DriversAgentTrapsRepeatInterval_Object = MibScalar
driversAgentTrapsRepeatInterval = _DriversAgentTrapsRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 5, 2),
    _DriversAgentTrapsRepeatInterval_Type()
)
driversAgentTrapsRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    driversAgentTrapsRepeatInterval.setStatus("mandatory")
_DriversAgentVersion_Type = DisplayString
_DriversAgentVersion_Object = MibScalar
driversAgentVersion = _DriversAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 5, 3),
    _DriversAgentVersion_Type()
)
driversAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driversAgentVersion.setStatus("mandatory")
_ApplicationsServer_ObjectIdentity = ObjectIdentity
applicationsServer = _ApplicationsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5)
)
_ApplicationsTable_Object = MibTable
applicationsTable = _ApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1)
)
if mibBuilder.loadTexts:
    applicationsTable.setStatus("mandatory")
_ApplicationsEntry_Object = MibTableRow
applicationsEntry = _ApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 1)
)
applicationsEntry.setIndexNames(
    (0, "Nice-MIB-II", "applicationsTableIndex"),
)
if mibBuilder.loadTexts:
    applicationsEntry.setStatus("mandatory")
_ApplicationName_Type = DisplayString
_ApplicationName_Object = MibTableColumn
applicationName = _ApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 1, 1),
    _ApplicationName_Type()
)
applicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationName.setStatus("mandatory")
_ApplicationStatus_Type = SeverityType
_ApplicationStatus_Object = MibTableColumn
applicationStatus = _ApplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 1, 2),
    _ApplicationStatus_Type()
)
applicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationStatus.setStatus("mandatory")
_ApplicationsTableIndex_Type = Integer32
_ApplicationsTableIndex_Object = MibTableColumn
applicationsTableIndex = _ApplicationsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 1, 3),
    _ApplicationsTableIndex_Type()
)
applicationsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationsTableIndex.setStatus("mandatory")
_ApplicationsPendingErrorsTable_Object = MibTable
applicationsPendingErrorsTable = _ApplicationsPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 2)
)
if mibBuilder.loadTexts:
    applicationsPendingErrorsTable.setStatus("mandatory")
_ApplicationsPendingErrorsEntry_Object = MibTableRow
applicationsPendingErrorsEntry = _ApplicationsPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 2, 1)
)
applicationsPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "applicationsErrorsTableApplicationIndex"),
    (0, "Nice-MIB-II", "applicationsErrorsTableErrorIndex"),
)
if mibBuilder.loadTexts:
    applicationsPendingErrorsEntry.setStatus("mandatory")
_ApplicationErrorType_Type = ApplicationErrorType
_ApplicationErrorType_Object = MibTableColumn
applicationErrorType = _ApplicationErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 2, 1, 1),
    _ApplicationErrorType_Type()
)
applicationErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationErrorType.setStatus("mandatory")
_ApplicationErrorReflectedStatus_Type = SeverityType
_ApplicationErrorReflectedStatus_Object = MibTableColumn
applicationErrorReflectedStatus = _ApplicationErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 2, 1, 2),
    _ApplicationErrorReflectedStatus_Type()
)
applicationErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationErrorReflectedStatus.setStatus("mandatory")
_ApplicationsErrorsTableApplicationIndex_Type = Integer32
_ApplicationsErrorsTableApplicationIndex_Object = MibTableColumn
applicationsErrorsTableApplicationIndex = _ApplicationsErrorsTableApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 2, 1, 3),
    _ApplicationsErrorsTableApplicationIndex_Type()
)
applicationsErrorsTableApplicationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationsErrorsTableApplicationIndex.setStatus("mandatory")
_ApplicationsErrorsTableErrorIndex_Type = Integer32
_ApplicationsErrorsTableErrorIndex_Object = MibTableColumn
applicationsErrorsTableErrorIndex = _ApplicationsErrorsTableErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 2, 1, 4),
    _ApplicationsErrorsTableErrorIndex_Type()
)
applicationsErrorsTableErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationsErrorsTableErrorIndex.setStatus("mandatory")
_ApplicationsNumberLoggedInUsers_Type = Integer32
_ApplicationsNumberLoggedInUsers_Object = MibScalar
applicationsNumberLoggedInUsers = _ApplicationsNumberLoggedInUsers_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 3),
    _ApplicationsNumberLoggedInUsers_Type()
)
applicationsNumberLoggedInUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationsNumberLoggedInUsers.setStatus("mandatory")
_ApplicationsSnmpAgentConfig_ObjectIdentity = ObjectIdentity
applicationsSnmpAgentConfig = _ApplicationsSnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 4)
)
_ApplicationsAgentIsRepeatingTraps_Type = YesNo
_ApplicationsAgentIsRepeatingTraps_Object = MibScalar
applicationsAgentIsRepeatingTraps = _ApplicationsAgentIsRepeatingTraps_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 4, 1),
    _ApplicationsAgentIsRepeatingTraps_Type()
)
applicationsAgentIsRepeatingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applicationsAgentIsRepeatingTraps.setStatus("mandatory")
_ApplicationsAgentTrapsRepeatInterval_Type = Integer32
_ApplicationsAgentTrapsRepeatInterval_Object = MibScalar
applicationsAgentTrapsRepeatInterval = _ApplicationsAgentTrapsRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 4, 2),
    _ApplicationsAgentTrapsRepeatInterval_Type()
)
applicationsAgentTrapsRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applicationsAgentTrapsRepeatInterval.setStatus("mandatory")
_ApplicationsAgentVersion_Type = DisplayString
_ApplicationsAgentVersion_Object = MibScalar
applicationsAgentVersion = _ApplicationsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 4, 3),
    _ApplicationsAgentVersion_Type()
)
applicationsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationsAgentVersion.setStatus("mandatory")
_StorageCenter_ObjectIdentity = ObjectIdentity
storageCenter = _StorageCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 6)
)
_SystemTools_ObjectIdentity = ObjectIdentity
systemTools = _SystemTools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7)
)
_RecordingsDiagnostic_ObjectIdentity = ObjectIdentity
recordingsDiagnostic = _RecordingsDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1)
)
_RdName_Type = DisplayString
_RdName_Object = MibScalar
rdName = _RdName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 1),
    _RdName_Type()
)
rdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdName.setStatus("mandatory")
_RdStatus_Type = SeverityType
_RdStatus_Object = MibScalar
rdStatus = _RdStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 2),
    _RdStatus_Type()
)
rdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdStatus.setStatus("mandatory")
_RdVersion_Type = DisplayString
_RdVersion_Object = MibScalar
rdVersion = _RdVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 3),
    _RdVersion_Type()
)
rdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdVersion.setStatus("mandatory")
_RdServerName_Type = DisplayString
_RdServerName_Object = MibScalar
rdServerName = _RdServerName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 4),
    _RdServerName_Type()
)
rdServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdServerName.setStatus("mandatory")
_RdServerAddress_Type = DisplayString
_RdServerAddress_Object = MibScalar
rdServerAddress = _RdServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 5),
    _RdServerAddress_Type()
)
rdServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdServerAddress.setStatus("mandatory")
_RdCLSConnectionTable_Object = MibTable
rdCLSConnectionTable = _RdCLSConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 6)
)
if mibBuilder.loadTexts:
    rdCLSConnectionTable.setStatus("mandatory")
_RdCLSConnectionEntry_Object = MibTableRow
rdCLSConnectionEntry = _RdCLSConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 6, 1)
)
rdCLSConnectionEntry.setIndexNames(
    (0, "Nice-MIB-II", "rdCLSConnectionTableIndex"),
)
if mibBuilder.loadTexts:
    rdCLSConnectionEntry.setStatus("mandatory")
_RdCLSID_Type = Integer32
_RdCLSID_Object = MibTableColumn
rdCLSID = _RdCLSID_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 6, 1, 1),
    _RdCLSID_Type()
)
rdCLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSID.setStatus("mandatory")
_RdCLSIpAddress_Type = DisplayString
_RdCLSIpAddress_Object = MibTableColumn
rdCLSIpAddress = _RdCLSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 6, 1, 2),
    _RdCLSIpAddress_Type()
)
rdCLSIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSIpAddress.setStatus("mandatory")
_RdCLSConnectionTableIndex_Type = Integer32
_RdCLSConnectionTableIndex_Object = MibTableColumn
rdCLSConnectionTableIndex = _RdCLSConnectionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 6, 1, 3),
    _RdCLSConnectionTableIndex_Type()
)
rdCLSConnectionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSConnectionTableIndex.setStatus("mandatory")
_RdLoggerConnectionTable_Object = MibTable
rdLoggerConnectionTable = _RdLoggerConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 7)
)
if mibBuilder.loadTexts:
    rdLoggerConnectionTable.setStatus("mandatory")
_RdLoggerConnectionEntry_Object = MibTableRow
rdLoggerConnectionEntry = _RdLoggerConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 7, 1)
)
rdLoggerConnectionEntry.setIndexNames(
    (0, "Nice-MIB-II", "rdLoggerConnectionTableIndex"),
)
if mibBuilder.loadTexts:
    rdLoggerConnectionEntry.setStatus("mandatory")
_RdLoggerID_Type = Integer32
_RdLoggerID_Object = MibTableColumn
rdLoggerID = _RdLoggerID_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 7, 1, 1),
    _RdLoggerID_Type()
)
rdLoggerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerID.setStatus("mandatory")
_RdLoggerIpAddress_Type = DisplayString
_RdLoggerIpAddress_Object = MibTableColumn
rdLoggerIpAddress = _RdLoggerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 7, 1, 2),
    _RdLoggerIpAddress_Type()
)
rdLoggerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerIpAddress.setStatus("mandatory")
_RdLoggerSpareloggerID_Type = Integer32
_RdLoggerSpareloggerID_Object = MibTableColumn
rdLoggerSpareloggerID = _RdLoggerSpareloggerID_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 7, 1, 3),
    _RdLoggerSpareloggerID_Type()
)
rdLoggerSpareloggerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerSpareloggerID.setStatus("mandatory")
_RdLoggerConnectionTableIndex_Type = Integer32
_RdLoggerConnectionTableIndex_Object = MibTableColumn
rdLoggerConnectionTableIndex = _RdLoggerConnectionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 7, 1, 4),
    _RdLoggerConnectionTableIndex_Type()
)
rdLoggerConnectionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerConnectionTableIndex.setStatus("mandatory")
_RdTasksTable_Object = MibTable
rdTasksTable = _RdTasksTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8)
)
if mibBuilder.loadTexts:
    rdTasksTable.setStatus("mandatory")
_RdTasksEntry_Object = MibTableRow
rdTasksEntry = _RdTasksEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1)
)
rdTasksEntry.setIndexNames(
    (0, "Nice-MIB-II", "rdTasksTableIndex"),
)
if mibBuilder.loadTexts:
    rdTasksEntry.setStatus("mandatory")
_RdTaskType_Type = RdTaskType
_RdTaskType_Object = MibTableColumn
rdTaskType = _RdTaskType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 1),
    _RdTaskType_Type()
)
rdTaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskType.setStatus("mandatory")
_RdTaskName_Type = DisplayString
_RdTaskName_Object = MibTableColumn
rdTaskName = _RdTaskName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 2),
    _RdTaskName_Type()
)
rdTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskName.setStatus("mandatory")
_RdTaskDescription_Type = DisplayString
_RdTaskDescription_Object = MibTableColumn
rdTaskDescription = _RdTaskDescription_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 3),
    _RdTaskDescription_Type()
)
rdTaskDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskDescription.setStatus("mandatory")
_RdTaskCreationTime_Type = HostLocalTime
_RdTaskCreationTime_Object = MibTableColumn
rdTaskCreationTime = _RdTaskCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 4),
    _RdTaskCreationTime_Type()
)
rdTaskCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskCreationTime.setStatus("mandatory")
_RdTaskStartTime_Type = HostLocalTime
_RdTaskStartTime_Object = MibTableColumn
rdTaskStartTime = _RdTaskStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 5),
    _RdTaskStartTime_Type()
)
rdTaskStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskStartTime.setStatus("mandatory")
_RdTaskQuery_Type = DisplayString
_RdTaskQuery_Object = MibTableColumn
rdTaskQuery = _RdTaskQuery_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 6),
    _RdTaskQuery_Type()
)
rdTaskQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskQuery.setStatus("mandatory")
_RdTaskExecElements_Type = Integer32
_RdTaskExecElements_Object = MibTableColumn
rdTaskExecElements = _RdTaskExecElements_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 7),
    _RdTaskExecElements_Type()
)
rdTaskExecElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskExecElements.setStatus("mandatory")
_RdTaskExecFailElements_Type = Integer32
_RdTaskExecFailElements_Object = MibTableColumn
rdTaskExecFailElements = _RdTaskExecFailElements_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 8),
    _RdTaskExecFailElements_Type()
)
rdTaskExecFailElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskExecFailElements.setStatus("mandatory")
_RdTaskCurrentState_Type = TaskState
_RdTaskCurrentState_Object = MibTableColumn
rdTaskCurrentState = _RdTaskCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 9),
    _RdTaskCurrentState_Type()
)
rdTaskCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskCurrentState.setStatus("mandatory")
_RdTaskLastError_Type = DisplayString
_RdTaskLastError_Object = MibTableColumn
rdTaskLastError = _RdTaskLastError_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 10),
    _RdTaskLastError_Type()
)
rdTaskLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTaskLastError.setStatus("mandatory")
_RdTasksTableIndex_Type = Integer32
_RdTasksTableIndex_Object = MibTableColumn
rdTasksTableIndex = _RdTasksTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 8, 1, 11),
    _RdTasksTableIndex_Type()
)
rdTasksTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdTasksTableIndex.setStatus("mandatory")
_RdCLSPendingErrorsTable_Object = MibTable
rdCLSPendingErrorsTable = _RdCLSPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9)
)
if mibBuilder.loadTexts:
    rdCLSPendingErrorsTable.setStatus("mandatory")
_RdCLSPendingErrorsEntry_Object = MibTableRow
rdCLSPendingErrorsEntry = _RdCLSPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9, 1)
)
rdCLSPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "rdCLSPendingErrorsTableIndex"),
)
if mibBuilder.loadTexts:
    rdCLSPendingErrorsEntry.setStatus("mandatory")
_RdCLSErrorType_Type = RdErrorType
_RdCLSErrorType_Object = MibTableColumn
rdCLSErrorType = _RdCLSErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9, 1, 1),
    _RdCLSErrorType_Type()
)
rdCLSErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSErrorType.setStatus("mandatory")
_RdCLSErrorReflectedStatus_Type = SeverityType
_RdCLSErrorReflectedStatus_Object = MibTableColumn
rdCLSErrorReflectedStatus = _RdCLSErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9, 1, 2),
    _RdCLSErrorReflectedStatus_Type()
)
rdCLSErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSErrorReflectedStatus.setStatus("mandatory")
_RdCLSExtendedErrorinformation_Type = DisplayString
_RdCLSExtendedErrorinformation_Object = MibTableColumn
rdCLSExtendedErrorinformation = _RdCLSExtendedErrorinformation_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9, 1, 3),
    _RdCLSExtendedErrorinformation_Type()
)
rdCLSExtendedErrorinformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSExtendedErrorinformation.setStatus("mandatory")
_RdCLSErrorCLSTableIndex_Type = Integer32
_RdCLSErrorCLSTableIndex_Object = MibTableColumn
rdCLSErrorCLSTableIndex = _RdCLSErrorCLSTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9, 1, 4),
    _RdCLSErrorCLSTableIndex_Type()
)
rdCLSErrorCLSTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSErrorCLSTableIndex.setStatus("mandatory")
_RdCLSPendingErrorsTableIndex_Type = Integer32
_RdCLSPendingErrorsTableIndex_Object = MibTableColumn
rdCLSPendingErrorsTableIndex = _RdCLSPendingErrorsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 9, 1, 5),
    _RdCLSPendingErrorsTableIndex_Type()
)
rdCLSPendingErrorsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdCLSPendingErrorsTableIndex.setStatus("mandatory")
_RdLoggerPendingErrorsTable_Object = MibTable
rdLoggerPendingErrorsTable = _RdLoggerPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10)
)
if mibBuilder.loadTexts:
    rdLoggerPendingErrorsTable.setStatus("mandatory")
_RdLoggerPendingErrorsEntry_Object = MibTableRow
rdLoggerPendingErrorsEntry = _RdLoggerPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10, 1)
)
rdLoggerPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "rdLoggerPendingErrorsTableIndex"),
)
if mibBuilder.loadTexts:
    rdLoggerPendingErrorsEntry.setStatus("mandatory")
_RdLoggerErrorType_Type = RdErrorType
_RdLoggerErrorType_Object = MibTableColumn
rdLoggerErrorType = _RdLoggerErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10, 1, 1),
    _RdLoggerErrorType_Type()
)
rdLoggerErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerErrorType.setStatus("mandatory")
_RdLoggerErrorReflectedStatus_Type = SeverityType
_RdLoggerErrorReflectedStatus_Object = MibTableColumn
rdLoggerErrorReflectedStatus = _RdLoggerErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10, 1, 2),
    _RdLoggerErrorReflectedStatus_Type()
)
rdLoggerErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerErrorReflectedStatus.setStatus("mandatory")
_RdLoggerExtendedErrorinformation_Type = DisplayString
_RdLoggerExtendedErrorinformation_Object = MibTableColumn
rdLoggerExtendedErrorinformation = _RdLoggerExtendedErrorinformation_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10, 1, 3),
    _RdLoggerExtendedErrorinformation_Type()
)
rdLoggerExtendedErrorinformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerExtendedErrorinformation.setStatus("mandatory")
_RdLoggerErrorLoggerTableIndex_Type = Integer32
_RdLoggerErrorLoggerTableIndex_Object = MibTableColumn
rdLoggerErrorLoggerTableIndex = _RdLoggerErrorLoggerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10, 1, 4),
    _RdLoggerErrorLoggerTableIndex_Type()
)
rdLoggerErrorLoggerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerErrorLoggerTableIndex.setStatus("mandatory")
_RdLoggerPendingErrorsTableIndex_Type = Integer32
_RdLoggerPendingErrorsTableIndex_Object = MibTableColumn
rdLoggerPendingErrorsTableIndex = _RdLoggerPendingErrorsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 10, 1, 5),
    _RdLoggerPendingErrorsTableIndex_Type()
)
rdLoggerPendingErrorsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdLoggerPendingErrorsTableIndex.setStatus("mandatory")
_DatabaseUtilities_ObjectIdentity = ObjectIdentity
databaseUtilities = _DatabaseUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2)
)
_CtiEventsDbServer_ObjectIdentity = ObjectIdentity
ctiEventsDbServer = _CtiEventsDbServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8)
)
_CtiDBServerName_Type = DisplayString
_CtiDBServerName_Object = MibScalar
ctiDBServerName = _CtiDBServerName_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 1),
    _CtiDBServerName_Type()
)
ctiDBServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerName.setStatus("mandatory")
_CtiDBServerStatus_Type = SeverityType
_CtiDBServerStatus_Object = MibScalar
ctiDBServerStatus = _CtiDBServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 2),
    _CtiDBServerStatus_Type()
)
ctiDBServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerStatus.setStatus("mandatory")
_CtiDBServerPendingErrorsTable_Object = MibTable
ctiDBServerPendingErrorsTable = _CtiDBServerPendingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ctiDBServerPendingErrorsTable.setStatus("mandatory")
_CtiDBServerPendingErrorsEntry_Object = MibTableRow
ctiDBServerPendingErrorsEntry = _CtiDBServerPendingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 3, 1)
)
ctiDBServerPendingErrorsEntry.setIndexNames(
    (0, "Nice-MIB-II", "ctiDBServerErrorIndex"),
)
if mibBuilder.loadTexts:
    ctiDBServerPendingErrorsEntry.setStatus("mandatory")
_CtiDBServerErrorType_Type = CTIEventsDBServerErrorType
_CtiDBServerErrorType_Object = MibTableColumn
ctiDBServerErrorType = _CtiDBServerErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 3, 1, 1),
    _CtiDBServerErrorType_Type()
)
ctiDBServerErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerErrorType.setStatus("mandatory")
_CtiDBServerErrorReflectedStatus_Type = SeverityType
_CtiDBServerErrorReflectedStatus_Object = MibTableColumn
ctiDBServerErrorReflectedStatus = _CtiDBServerErrorReflectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 3, 1, 2),
    _CtiDBServerErrorReflectedStatus_Type()
)
ctiDBServerErrorReflectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerErrorReflectedStatus.setStatus("mandatory")
_CtiDBServerDBErrorCode_Type = Integer32
_CtiDBServerDBErrorCode_Object = MibTableColumn
ctiDBServerDBErrorCode = _CtiDBServerDBErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 3, 1, 3),
    _CtiDBServerDBErrorCode_Type()
)
ctiDBServerDBErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerDBErrorCode.setStatus("optional")
_CtiDBServerErrorIndex_Type = Integer32
_CtiDBServerErrorIndex_Object = MibTableColumn
ctiDBServerErrorIndex = _CtiDBServerErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 3, 1, 4),
    _CtiDBServerErrorIndex_Type()
)
ctiDBServerErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerErrorIndex.setStatus("mandatory")
_CtiDBServerSnmpAgentConfig_ObjectIdentity = ObjectIdentity
ctiDBServerSnmpAgentConfig = _CtiDBServerSnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 4)
)
_CtiDBServerAgentIsRepeatingTraps_Type = YesNo
_CtiDBServerAgentIsRepeatingTraps_Object = MibScalar
ctiDBServerAgentIsRepeatingTraps = _CtiDBServerAgentIsRepeatingTraps_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 4, 1),
    _CtiDBServerAgentIsRepeatingTraps_Type()
)
ctiDBServerAgentIsRepeatingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctiDBServerAgentIsRepeatingTraps.setStatus("mandatory")
_CtiDBServerAgentTrapsRepeatInterval_Type = Integer32
_CtiDBServerAgentTrapsRepeatInterval_Object = MibScalar
ctiDBServerAgentTrapsRepeatInterval = _CtiDBServerAgentTrapsRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 4, 2),
    _CtiDBServerAgentTrapsRepeatInterval_Type()
)
ctiDBServerAgentTrapsRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctiDBServerAgentTrapsRepeatInterval.setStatus("mandatory")
_CtiDBServerAgentVersion_Type = DisplayString
_CtiDBServerAgentVersion_Object = MibScalar
ctiDBServerAgentVersion = _CtiDBServerAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 4, 3),
    _CtiDBServerAgentVersion_Type()
)
ctiDBServerAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctiDBServerAgentVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects

clsRcmIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1001)
)
clsRcmIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRcmIsDown.setStatus(
        ""
    )

clsRcmIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1002)
)
clsRcmIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRcmIsUp.setStatus(
        ""
    )

clsRecordIsInsertedToDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1024)
)
clsRecordIsInsertedToDB.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRecordIsInsertedToDB.setStatus(
        ""
    )

clsCommunicationProblemWithLogger = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1025)
)
clsCommunicationProblemWithLogger.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerId"))
)
if mibBuilder.loadTexts:
    clsCommunicationProblemWithLogger.setStatus(
        ""
    )

clsCommunicationToLoggerIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1026)
)
clsCommunicationToLoggerIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCommunicationToLoggerIsOK.setStatus(
        ""
    )

clsProblematicClockDifferencesWithLogger = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1027)
)
clsProblematicClockDifferencesWithLogger.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerId"))
)
if mibBuilder.loadTexts:
    clsProblematicClockDifferencesWithLogger.setStatus(
        ""
    )

clsNoClockDifferencesWithLogger = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1028)
)
clsNoClockDifferencesWithLogger.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsNoClockDifferencesWithLogger.setStatus(
        ""
    )

clsNoAvailableResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1029)
)
clsNoAvailableResources.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRecordedMedia"))
)
if mibBuilder.loadTexts:
    clsNoAvailableResources.setStatus(
        ""
    )

clsResourcesAreAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1030)
)
clsResourcesAreAvailable.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsResourcesAreAvailable.setStatus(
        ""
    )

clsLoggerIsNotInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1031)
)
clsLoggerIsNotInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerInitializationStatus"))
)
if mibBuilder.loadTexts:
    clsLoggerIsNotInitializedProperly.setStatus(
        ""
    )

clsLoggerIsInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1032)
)
clsLoggerIsInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsLoggerIsInitializedProperly.setStatus(
        ""
    )

clsRCMIsNotInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1033)
)
clsRCMIsNotInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRCMIsNotInitializedProperly.setStatus(
        ""
    )

clsRCMIsInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1034)
)
clsRCMIsInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRCMIsInitializedProperly.setStatus(
        ""
    )

clsProblemWithNPLUS1Loggers = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1035)
)
clsProblemWithNPLUS1Loggers.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerId"))
)
if mibBuilder.loadTexts:
    clsProblemWithNPLUS1Loggers.setStatus(
        ""
    )

clsNPLUS1LoggersAreOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 1, 0, 1036)
)
clsNPLUS1LoggersAreOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rcmName"),
        ("Nice-MIB-II", "rcmStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsNPLUS1LoggersAreOK.setStatus(
        ""
    )

clsCallServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 0, 1003)
)
clsCallServerIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "callServerName"),
        ("Nice-MIB-II", "callServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCallServerIsDown.setStatus(
        ""
    )

clsCallServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 0, 1004)
)
clsCallServerIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "callServerName"),
        ("Nice-MIB-II", "callServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCallServerIsUp.setStatus(
        ""
    )

clsCallServerLinkIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 0, 1011)
)
clsCallServerLinkIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "callServerName"),
        ("Nice-MIB-II", "callServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCallServerLinkIsDown.setStatus(
        ""
    )

clsCallServerLinkIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 0, 1012)
)
clsCallServerLinkIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "callServerName"),
        ("Nice-MIB-II", "callServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCallServerLinkIsUp.setStatus(
        ""
    )

clsCallServerTableIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 0, 1037)
)
clsCallServerTableIsFull.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "callServerName"),
        ("Nice-MIB-II", "callServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapClsTableType"))
)
if mibBuilder.loadTexts:
    clsCallServerTableIsFull.setStatus(
        ""
    )

clsCallServerTableIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 2, 0, 1038)
)
clsCallServerTableIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "callServerName"),
        ("Nice-MIB-II", "callServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCallServerTableIsOK.setStatus(
        ""
    )

clsSchedulerServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 0, 1005)
)
clsSchedulerServerIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "schedulerServerName"),
        ("Nice-MIB-II", "schedulerServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsSchedulerServerIsDown.setStatus(
        ""
    )

clsSchedulerServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 0, 1006)
)
clsSchedulerServerIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "schedulerServerName"),
        ("Nice-MIB-II", "schedulerServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsSchedulerServerIsUp.setStatus(
        ""
    )

clsRecordingOnDemandIsNotEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 0, 1013)
)
clsRecordingOnDemandIsNotEnabled.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "schedulerServerName"),
        ("Nice-MIB-II", "schedulerServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRecordingOnDemandIsNotEnabled.setStatus(
        ""
    )

clsRecordingOnDemandIsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 0, 1014)
)
clsRecordingOnDemandIsEnabled.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "schedulerServerName"),
        ("Nice-MIB-II", "schedulerServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsRecordingOnDemandIsEnabled.setStatus(
        ""
    )

clsSchedulerServerIsNotInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 0, 1015)
)
clsSchedulerServerIsNotInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "schedulerServerName"),
        ("Nice-MIB-II", "schedulerServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsSchedulerServerIsNotInitializedProperly.setStatus(
        ""
    )

clsSchedulerServerIsInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 3, 0, 1016)
)
clsSchedulerServerIsInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "schedulerServerName"),
        ("Nice-MIB-II", "schedulerServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsSchedulerServerIsInitializedProperly.setStatus(
        ""
    )

clsDBServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1007)
)
clsDBServerIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDBServerIsDown.setStatus(
        ""
    )

clsDBServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1008)
)
clsDBServerIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDBServerIsUp.setStatus(
        ""
    )

clsFailureConnectionToDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1017)
)
clsFailureConnectionToDB.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    clsFailureConnectionToDB.setStatus(
        ""
    )

clsConnectionToDBIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1018)
)
clsConnectionToDBIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsConnectionToDBIsOK.setStatus(
        ""
    )

clsDBServerIsNotInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1019)
)
clsDBServerIsNotInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDBServerIsNotInitializedProperly.setStatus(
        ""
    )

clsDBServerIsInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1020)
)
clsDBServerIsInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDBServerIsInitializedProperly.setStatus(
        ""
    )

clsDBSpaceIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1021)
)
clsDBSpaceIsFull.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    clsDBSpaceIsFull.setStatus(
        ""
    )

clsDBSpaceIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1022)
)
clsDBSpaceIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDBSpaceIsOK.setStatus(
        ""
    )

clsRecordIsNotInsertedToDBTheRecordIsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 4, 0, 1023)
)
clsRecordIsNotInsertedToDBTheRecordIsLost.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "dbServerName"),
        ("Nice-MIB-II", "dbServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    clsRecordIsNotInsertedToDBTheRecordIsLost.setStatus(
        ""
    )

clsDispatchIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1009)
)
clsDispatchIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDispatchIsDown.setStatus(
        ""
    )

clsDispatchIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1010)
)
clsDispatchIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsDispatchIsUp.setStatus(
        ""
    )

clsALLCLSModulesInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1039)
)
clsALLCLSModulesInitFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsALLCLSModulesInitFailed.setStatus(
        ""
    )

clsALLCLSModulesInitOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1040)
)
clsALLCLSModulesInitOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsALLCLSModulesInitOK.setStatus(
        ""
    )

clsCLSModuleRestartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1041)
)
clsCLSModuleRestartFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCLSModuleRestartFailed.setStatus(
        ""
    )

clsCLSModuleRestartOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1042)
)
clsCLSModuleRestartOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsCLSModuleRestartOK.setStatus(
        ""
    )

clsOSDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1043)
)
clsOSDiskFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapOsDiskFailure"))
)
if mibBuilder.loadTexts:
    clsOSDiskFailure.setStatus(
        ""
    )

clsOSDiskOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 2, 5, 0, 1044)
)
clsOSDiskOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "clsDispatcherName"),
        ("Nice-MIB-II", "clsDispatcherStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    clsOSDiskOK.setStatus(
        ""
    )

mmlSnmpAgentConnectedToLogger = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3001)
)
mmlSnmpAgentConnectedToLogger.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlSnmpAgentConnectedToLogger.setStatus(
        ""
    )

mmlConnectionToLoggerNotEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3002)
)
mmlConnectionToLoggerNotEstablished.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlConnectionToLoggerNotEstablished.setStatus(
        ""
    )

mmlInvalidConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3100)
)
mmlInvalidConfiguration.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlInvalidConfiguration.setStatus(
        ""
    )

mmlPersistentMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3101)
)
mmlPersistentMismatch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlPersistentMismatch.setStatus(
        ""
    )

mmlAbnormalPlaybackTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3102)
)
mmlAbnormalPlaybackTermination.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlAbnormalPlaybackTermination.setStatus(
        ""
    )

mmlAbnormalRecordTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3103)
)
mmlAbnormalRecordTermination.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlAbnormalRecordTermination.setStatus(
        ""
    )

mmlUnableToReplyDueToConnectionLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3104)
)
mmlUnableToReplyDueToConnectionLoss.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlUnableToReplyDueToConnectionLoss.setStatus(
        ""
    )

mmlFailToInitializeStorageDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3105)
)
mmlFailToInitializeStorageDevice.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlFailToInitializeStorageDevice.setStatus(
        ""
    )

mmlFailToInitializeDataSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3106)
)
mmlFailToInitializeDataSystem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlFailToInitializeDataSystem.setStatus(
        ""
    )

mmlFailToInitializeMemoryManager = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3107)
)
mmlFailToInitializeMemoryManager.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlFailToInitializeMemoryManager.setStatus(
        ""
    )

mmlUnexpectedDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3108)
)
mmlUnexpectedDisconnect.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlUnexpectedDisconnect.setStatus(
        ""
    )

mmlConnectionCanNotBeEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3109)
)
mmlConnectionCanNotBeEstablished.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlConnectionCanNotBeEstablished.setStatus(
        ""
    )

mmlAllConnectionResourcesInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3110)
)
mmlAllConnectionResourcesInUse.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlAllConnectionResourcesInUse.setStatus(
        ""
    )

mmlConnectionTimeoutExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3111)
)
mmlConnectionTimeoutExceeded.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlConnectionTimeoutExceeded.setStatus(
        ""
    )

mmlMemoryManagerOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3112)
)
mmlMemoryManagerOverflow.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlMemoryManagerOverflow.setStatus(
        ""
    )

mmlAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3113)
)
mmlAllocationFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlAllocationFailure.setStatus(
        ""
    )

mmlResourceAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3114)
)
mmlResourceAllocationFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlResourceAllocationFailure.setStatus(
        ""
    )

mmlOutputChannelAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3115)
)
mmlOutputChannelAllocationFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlOutputChannelAllocationFailure.setStatus(
        ""
    )

mmlInputChannelAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3116)
)
mmlInputChannelAllocationFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlInputChannelAllocationFailure.setStatus(
        ""
    )

mmlResourceAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3117)
)
mmlResourceAccessFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlResourceAccessFailure.setStatus(
        ""
    )

mmlLoggerIsShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3118)
)
mmlLoggerIsShuttingDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlLoggerIsShuttingDown.setStatus(
        ""
    )

mmlLoggerIsReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 0, 3119)
)
mmlLoggerIsReady.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlName"),
        ("Nice-MIB-II", "mmlStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlLoggerIsReady.setStatus(
        ""
    )

mmlStorageSystemInvalidConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3200)
)
mmlStorageSystemInvalidConfiguration.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlStorageSystemInvalidConfiguration.setStatus(
        ""
    )

mmlStorageSystemPersistentMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3201)
)
mmlStorageSystemPersistentMismatch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlStorageSystemPersistentMismatch.setStatus(
        ""
    )

mmlConsistentDiskWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3202)
)
mmlConsistentDiskWriteFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlConsistentDiskWriteFailure.setStatus(
        ""
    )

mmlConsistentDiskReadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3203)
)
mmlConsistentDiskReadFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlConsistentDiskReadFailure.setStatus(
        ""
    )

mmlDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3204)
)
mmlDiskUsage.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDiskUsage"))
)
if mibBuilder.loadTexts:
    mmlDiskUsage.setStatus(
        ""
    )

mmlDiskIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3205)
)
mmlDiskIsFull.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlDiskIsFull.setStatus(
        ""
    )

mmlDiskIOFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 3, 0, 3206)
)
mmlDiskIOFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlStorageSystemName"),
        ("Nice-MIB-II", "mmlStorageSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlDiskIOFailure.setStatus(
        ""
    )

mmlDataSystemInvalidConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 0, 3300)
)
mmlDataSystemInvalidConfiguration.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlDataSystemName"),
        ("Nice-MIB-II", "mmlDataSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlDataSystemInvalidConfiguration.setStatus(
        ""
    )

mmlDataSystemPersistentMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 0, 3301)
)
mmlDataSystemPersistentMismatch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlDataSystemName"),
        ("Nice-MIB-II", "mmlDataSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlDataSystemPersistentMismatch.setStatus(
        ""
    )

mmlDataBaseConsistencyMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 0, 3302)
)
mmlDataBaseConsistencyMismatch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlDataSystemName"),
        ("Nice-MIB-II", "mmlDataSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlDataBaseConsistencyMismatch.setStatus(
        ""
    )

mmlCriticalDataSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 0, 3303)
)
mmlCriticalDataSystemError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlDataSystemName"),
        ("Nice-MIB-II", "mmlDataSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlCriticalDataSystemError.setStatus(
        ""
    )

mmlTableAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 4, 0, 3304)
)
mmlTableAccessFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlDataSystemName"),
        ("Nice-MIB-II", "mmlDataSystemStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlTableAccessFailure.setStatus(
        ""
    )

mmlAutoDeletionInvalidConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 0, 3400)
)
mmlAutoDeletionInvalidConfiguration.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlAutoDeletionName"),
        ("Nice-MIB-II", "mmlAutoDeletionStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlAutoDeletionInvalidConfiguration.setStatus(
        ""
    )

mmlAutoDeletionPersistentMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 0, 3401)
)
mmlAutoDeletionPersistentMismatch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlAutoDeletionName"),
        ("Nice-MIB-II", "mmlAutoDeletionStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlAutoDeletionPersistentMismatch.setStatus(
        ""
    )

mmlStartingAutoDeletionJob = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 0, 3402)
)
mmlStartingAutoDeletionJob.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlAutoDeletionName"),
        ("Nice-MIB-II", "mmlAutoDeletionStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlStartingAutoDeletionJob.setStatus(
        ""
    )

mmlFinishedNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 0, 3403)
)
mmlFinishedNormal.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlAutoDeletionName"),
        ("Nice-MIB-II", "mmlAutoDeletionStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlFinishedNormal.setStatus(
        ""
    )

mmlDeletionCapacityNotReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 1, 5, 0, 3404)
)
mmlDeletionCapacityNotReached.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "mmlAutoDeletionName"),
        ("Nice-MIB-II", "mmlAutoDeletionStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    mmlDeletionCapacityNotReached.setStatus(
        ""
    )

vlLoggerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 0, 6002)
)
vlLoggerNotResponding.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlLoggerNotResponding.setStatus(
        ""
    )

vlApiQueryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 0, 6003)
)
vlApiQueryError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlApiQueryError.setStatus(
        ""
    )

vlDbmConsistencyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6100)
)
vlDbmConsistencyFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDbmConsistencyFailed.setStatus(
        ""
    )

vlDbmInitPartitionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6101)
)
vlDbmInitPartitionFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDbmInitPartitionFailed.setStatus(
        ""
    )

vlKernerHWDriverInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6102)
)
vlKernerHWDriverInitFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlKernerHWDriverInitFailed.setStatus(
        ""
    )

vlVoipDriverInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6103)
)
vlVoipDriverInitFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlVoipDriverInitFailed.setStatus(
        ""
    )

vlDliDriverInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6104)
)
vlDliDriverInitFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDliDriverInitFailed.setStatus(
        ""
    )

vlAumGeneralInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6105)
)
vlAumGeneralInitFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlAumGeneralInitFailure.setStatus(
        ""
    )

vlDiskOpenPartitionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6106)
)
vlDiskOpenPartitionFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDiskDrive"))
)
if mibBuilder.loadTexts:
    vlDiskOpenPartitionFailed.setStatus(
        ""
    )

vlDiskDriveProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6107)
)
vlDiskDriveProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDiskDriveProblem.setStatus(
        ""
    )

vlNPlus1ManualSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6108)
)
vlNPlus1ManualSwitch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlNPlus1ManualSwitch.setStatus(
        ""
    )

vlNPlus1SpareIsBackingUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6109)
)
vlNPlus1SpareIsBackingUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerIdInChain"))
)
if mibBuilder.loadTexts:
    vlNPlus1SpareIsBackingUp.setStatus(
        ""
    )

vlNPlus1ROBMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6110)
)
vlNPlus1ROBMalfunction.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlNPlus1ROBMalfunction.setStatus(
        ""
    )

vlNPlus1ROBPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6111)
)
vlNPlus1ROBPowerFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlNPlus1ROBPowerFailure.setStatus(
        ""
    )

vlNPlus1SpareNeedLongUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6112)
)
vlNPlus1SpareNeedLongUpdate.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlNPlus1SpareNeedLongUpdate.setStatus(
        ""
    )

vlAutoDeleteUnder3PercSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6113)
)
vlAutoDeleteUnder3PercSpace.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapFreeSpacePercentage"))
)
if mibBuilder.loadTexts:
    vlAutoDeleteUnder3PercSpace.setStatus(
        ""
    )

vlAutoDeleteNofreeSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6114)
)
vlAutoDeleteNofreeSpace.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapFreeSpacePercentage"))
)
if mibBuilder.loadTexts:
    vlAutoDeleteNofreeSpace.setStatus(
        ""
    )

vlAutoDeleteLowKeptSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6115)
)
vlAutoDeleteLowKeptSpace.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapKeptSpacePercentage"))
)
if mibBuilder.loadTexts:
    vlAutoDeleteLowKeptSpace.setStatus(
        ""
    )

vlAutoDeleteNoKeptSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6116)
)
vlAutoDeleteNoKeptSpace.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlAutoDeleteNoKeptSpace.setStatus(
        ""
    )

vlDongleNotInitialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6117)
)
vlDongleNotInitialized.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleNotInitialized.setStatus(
        ""
    )

vlDongleAlreadyInitialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6118)
)
vlDongleAlreadyInitialized.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleAlreadyInitialized.setStatus(
        ""
    )

vlDongleDeviceNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6119)
)
vlDongleDeviceNotSupported.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleDeviceNotSupported.setStatus(
        ""
    )

vlDongleInitFailed_function = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6120)
)
vlDongleInitFailed_function.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleInitFailed_function.setStatus(
        ""
    )

vlDongleConnectFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6121)
)
vlDongleConnectFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleConnectFailed.setStatus(
        ""
    )

vlDongleInitFailed_network = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6122)
)
vlDongleInitFailed_network.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleInitFailed_network.setStatus(
        ""
    )

vlDongleNoDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6123)
)
vlDongleNoDevice.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleNoDevice.setStatus(
        ""
    )

vlDongleInitFailed_parameter = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6124)
)
vlDongleInitFailed_parameter.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleInitFailed_parameter.setStatus(
        ""
    )

vlDongleInitFailed_HLApi = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6125)
)
vlDongleInitFailed_HLApi.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleInitFailed_HLApi.setStatus(
        ""
    )

vlDongleInitFailed_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6126)
)
vlDongleInitFailed_memory.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleInitFailed_memory.setStatus(
        ""
    )

vlDongleInitFailed_HLVDD = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6127)
)
vlDongleInitFailed_HLVDD.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlDongleInitFailed_HLVDD.setStatus(
        ""
    )

vlCheckSumInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6128)
)
vlCheckSumInvalid.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlCheckSumInvalid.setStatus(
        ""
    )

vlChannelsLineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6129)
)
vlChannelsLineError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapChannelNumber"),
        ("Nice-MIB-II", "trapLineErrorType"),
        ("Nice-MIB-II", "trapBoardType"),
        ("Nice-MIB-II", "trapBoardOrLogicalTrunk"),
        ("Nice-MIB-II", "trapChannelOrTimeslot"),
        ("Nice-MIB-II", "trapMateLogicalTrunk"),
        ("Nice-MIB-II", "trapMateTimeslot"))
)
if mibBuilder.loadTexts:
    vlChannelsLineError.setStatus(
        ""
    )

vlChannelsSomeNotRecording = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6130)
)
vlChannelsSomeNotRecording.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapNumOfChannels"))
)
if mibBuilder.loadTexts:
    vlChannelsSomeNotRecording.setStatus(
        ""
    )

vlChannelsLowStatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6131)
)
vlChannelsLowStatAlarm.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapNumOfChannels"))
)
if mibBuilder.loadTexts:
    vlChannelsLowStatAlarm.setStatus(
        ""
    )

vlChannelsHighStatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 3, 0, 6132)
)
vlChannelsHighStatAlarm.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapNumOfChannels"))
)
if mibBuilder.loadTexts:
    vlChannelsHighStatAlarm.setStatus(
        ""
    )

vlAdifDspIllegalCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6300)
)
vlAdifDspIllegalCommand.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspIllegalCommand.setStatus(
        ""
    )

vlAdifDspNoSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6301)
)
vlAdifDspNoSynch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspNoSynch.setStatus(
        ""
    )

vlAdifDspSSIRXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6302)
)
vlAdifDspSSIRXError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspSSIRXError.setStatus(
        ""
    )

vlAdifDspCodecError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6303)
)
vlAdifDspCodecError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspCodecError.setStatus(
        ""
    )

vlAdifDspIllegalParameter = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6304)
)
vlAdifDspIllegalParameter.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspIllegalParameter.setStatus(
        ""
    )

vlAdifDspMPMLQError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6305)
)
vlAdifDspMPMLQError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspMPMLQError.setStatus(
        ""
    )

vlAdifDspStackOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6306)
)
vlAdifDspStackOverflow.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspStackOverflow.setStatus(
        ""
    )

vlAdifDspIllegalInstruction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6307)
)
vlAdifDspIllegalInstruction.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifDspIllegalInstruction.setStatus(
        ""
    )

vlAdifNoInterrupts = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6308)
)
vlAdifNoInterrupts.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifNoInterrupts.setStatus(
        ""
    )

vlAdifInternalBoardError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6309)
)
vlAdifInternalBoardError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifInternalBoardError.setStatus(
        ""
    )

vlAdifNoSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6310)
)
vlAdifNoSignal.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifNoSignal.setStatus(
        ""
    )

vlAdifAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6311)
)
vlAdifAlarmIndicationSignal.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifAlarmIndicationSignal.setStatus(
        ""
    )

vlAdifLossOfSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6312)
)
vlAdifLossOfSynch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifLossOfSynch.setStatus(
        ""
    )

vlAdifRemoteAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6313)
)
vlAdifRemoteAlarmIndication.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifRemoteAlarmIndication.setStatus(
        ""
    )

vlAdifFramingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6314)
)
vlAdifFramingError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdifFramingError.setStatus(
        ""
    )

vlApaInternalSelfTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6315)
)
vlApaInternalSelfTestFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlApaInternalSelfTestFailed.setStatus(
        ""
    )

vlApaCommBoardDspError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6316)
)
vlApaCommBoardDspError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlApaCommBoardDspError.setStatus(
        ""
    )

vlApaIOError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6317)
)
vlApaIOError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlApaIOError.setStatus(
        ""
    )

vlApaDspFirmwareLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6318)
)
vlApaDspFirmwareLoadFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlApaDspFirmwareLoadFailed.setStatus(
        ""
    )

vlApaDspRuntimeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6319)
)
vlApaDspRuntimeError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlApaDspRuntimeError.setStatus(
        ""
    )

vlIsdnDspCommFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6320)
)
vlIsdnDspCommFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlIsdnDspCommFailed.setStatus(
        ""
    )

vlIsdnIniterror = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6321)
)
vlIsdnIniterror.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsdnIniterror.setStatus(
        ""
    )

vlIsdnBSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6322)
)
vlIsdnBSError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsdnBSError.setStatus(
        ""
    )

vlIsdnLogicConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6323)
)
vlIsdnLogicConnectError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsdnLogicConnectError.setStatus(
        ""
    )

vlIsdnBoardSelfTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6324)
)
vlIsdnBoardSelfTestFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsdnBoardSelfTestFailed.setStatus(
        ""
    )

vlIsdnLineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6325)
)
vlIsdnLineError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsdnLineError.setStatus(
        ""
    )

vlEtaiInitBoardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6326)
)
vlEtaiInitBoardFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlEtaiInitBoardFailed.setStatus(
        ""
    )

vlEtaiLineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6327)
)
vlEtaiLineError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapLineNumber"),
        ("Nice-MIB-II", "trapLineProblem"))
)
if mibBuilder.loadTexts:
    vlEtaiLineError.setStatus(
        ""
    )

vlEtaiMatrixSwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6328)
)
vlEtaiMatrixSwitchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlEtaiMatrixSwitchError.setStatus(
        ""
    )

vlEtaiDspError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6329)
)
vlEtaiDspError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlEtaiDspError.setStatus(
        ""
    )

vlNtcmLoopError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6330)
)
vlNtcmLoopError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNtcmLoopError.setStatus(
        ""
    )

vlNtcmInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6331)
)
vlNtcmInitError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNtcmInitError.setStatus(
        ""
    )

vlNtcmMatrixSwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6332)
)
vlNtcmMatrixSwitchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNtcmMatrixSwitchError.setStatus(
        ""
    )

vlTdaMatrizSwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6333)
)
vlTdaMatrizSwitchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlTdaMatrizSwitchError.setStatus(
        ""
    )

vlTdaDspError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6334)
)
vlTdaDspError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlTdaDspError.setStatus(
        ""
    )

vlTdaGeneralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6335)
)
vlTdaGeneralError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlTdaGeneralError.setStatus(
        ""
    )

vlNatiChannelError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6336)
)
vlNatiChannelError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNatiChannelError.setStatus(
        ""
    )

vlNatiInitBoardError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6337)
)
vlNatiInitBoardError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNatiInitBoardError.setStatus(
        ""
    )

vlNatiMatrixSwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6338)
)
vlNatiMatrixSwitchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNatiMatrixSwitchError.setStatus(
        ""
    )

vlNatiDspA3mError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6339)
)
vlNatiDspA3mError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNatiDspA3mError.setStatus(
        ""
    )

vlIsacSelectedClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6340)
)
vlIsacSelectedClockError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsacSelectedClockError.setStatus(
        ""
    )

vlIsacRightClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6341)
)
vlIsacRightClockError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsacRightClockError.setStatus(
        ""
    )

vlIsacLeftClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6342)
)
vlIsacLeftClockError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsacLeftClockError.setStatus(
        ""
    )

vlIsacRightFameSynchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6343)
)
vlIsacRightFameSynchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsacRightFameSynchError.setStatus(
        ""
    )

vlIsacLeftFrameSynchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6344)
)
vlIsacLeftFrameSynchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsacLeftFrameSynchError.setStatus(
        ""
    )

vlIsacBoardError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6345)
)
vlIsacBoardError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsacBoardError.setStatus(
        ""
    )

vlIsacTestToneError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6346)
)
vlIsacTestToneError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDataLineNumber"))
)
if mibBuilder.loadTexts:
    vlIsacTestToneError.setStatus(
        ""
    )

vlIsacCriticalSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6347)
)
vlIsacCriticalSystemError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    vlIsacCriticalSystemError.setStatus(
        ""
    )

vlDliBoardCommError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6348)
)
vlDliBoardCommError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlDliBoardCommError.setStatus(
        ""
    )

vlDliChannelError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6349)
)
vlDliChannelError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlDliChannelError.setStatus(
        ""
    )

vlLafDspCommError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6350)
)
vlLafDspCommError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafDspCommError.setStatus(
        ""
    )

vlLafFirmwareLoadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6351)
)
vlLafFirmwareLoadError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafFirmwareLoadError.setStatus(
        ""
    )

vlLafinitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6352)
)
vlLafinitFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafinitFailed.setStatus(
        ""
    )

vlLafConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6353)
)
vlLafConfigError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafConfigError.setStatus(
        ""
    )

vlLafInvalidTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6354)
)
vlLafInvalidTime.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafInvalidTime.setStatus(
        ""
    )

vlLafLostSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6355)
)
vlLafLostSynch.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafLostSynch.setStatus(
        ""
    )

vlLafPowerProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6356)
)
vlLafPowerProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafPowerProblem.setStatus(
        ""
    )

vlLafMirrorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6357)
)
vlLafMirrorFault.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLafMirrorFault.setStatus(
        ""
    )

vlAdif3InitFailed_Dsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6358)
)
vlAdif3InitFailed_Dsp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlAdif3InitFailed_Dsp.setStatus(
        ""
    )

vlAdif3InitFailed_timing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6359)
)
vlAdif3InitFailed_timing.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdif3InitFailed_timing.setStatus(
        ""
    )

vlAdif3InitFailed_ADPCM = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6360)
)
vlAdif3InitFailed_ADPCM.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdif3InitFailed_ADPCM.setStatus(
        ""
    )

vlAdif3InitFailed_HW = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6361)
)
vlAdif3InitFailed_HW.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdif3InitFailed_HW.setStatus(
        ""
    )

vlAdif3ExternalClockSynchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6362)
)
vlAdif3ExternalClockSynchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAdif3ExternalClockSynchError.setStatus(
        ""
    )

vlUdaInitFailed_Dsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6363)
)
vlUdaInitFailed_Dsp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"),
        ("Nice-MIB-II", "trapDaughterBoardNumber"))
)
if mibBuilder.loadTexts:
    vlUdaInitFailed_Dsp.setStatus(
        ""
    )

vlUdaMatrixInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6364)
)
vlUdaMatrixInitFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlUdaMatrixInitFailed.setStatus(
        ""
    )

vlUdaInitBoardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6365)
)
vlUdaInitBoardFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlUdaInitBoardFailed.setStatus(
        ""
    )

vlEtai2InitFailed_Dsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6366)
)
vlEtai2InitFailed_Dsp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlEtai2InitFailed_Dsp.setStatus(
        ""
    )

vlEtai2MatrixInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6367)
)
vlEtai2MatrixInitError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlEtai2MatrixInitError.setStatus(
        ""
    )

vlEtai2InitBoardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6368)
)
vlEtai2InitBoardFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlEtai2InitBoardFailed.setStatus(
        ""
    )

vlEtai2LineProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6369)
)
vlEtai2LineProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapLineNumber"),
        ("Nice-MIB-II", "trapLineErrorType"),
        ("Nice-MIB-II", "trapLogicalStreamNumber"))
)
if mibBuilder.loadTexts:
    vlEtai2LineProblem.setStatus(
        ""
    )

vlBtai2InitFailed_Dsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6370)
)
vlBtai2InitFailed_Dsp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlBtai2InitFailed_Dsp.setStatus(
        ""
    )

vlBtai2MatrixInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6371)
)
vlBtai2MatrixInitError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlBtai2MatrixInitError.setStatus(
        ""
    )

vlBtai2InitBoardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6372)
)
vlBtai2InitBoardFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlBtai2InitBoardFailed.setStatus(
        ""
    )

vlBtai2FpgaError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6373)
)
vlBtai2FpgaError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlBtai2FpgaError.setStatus(
        ""
    )

vlBtai2LineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6374)
)
vlBtai2LineError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapLineNumber"),
        ("Nice-MIB-II", "trapLineErrorType"),
        ("Nice-MIB-II", "trapLogicalStreamNumber"))
)
if mibBuilder.loadTexts:
    vlBtai2LineError.setStatus(
        ""
    )

vlIsac2RightClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6375)
)
vlIsac2RightClockError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2RightClockError.setStatus(
        ""
    )

vlIsac2LeftClockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6376)
)
vlIsac2LeftClockError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2LeftClockError.setStatus(
        ""
    )

vlIsac2RightFrameSynchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6377)
)
vlIsac2RightFrameSynchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2RightFrameSynchError.setStatus(
        ""
    )

vlIsac2LeftFrameSynchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6378)
)
vlIsac2LeftFrameSynchError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2LeftFrameSynchError.setStatus(
        ""
    )

vlIsac2BoardProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6379)
)
vlIsac2BoardProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2BoardProblem.setStatus(
        ""
    )

vlIsac2TestToneProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6380)
)
vlIsac2TestToneProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDataLineNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2TestToneProblem.setStatus(
        ""
    )

vlIsac2SystemCriticalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6381)
)
vlIsac2SystemCriticalError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlIsac2SystemCriticalError.setStatus(
        ""
    )

vlLmopRedunPowerProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6382)
)
vlLmopRedunPowerProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLmopRedunPowerProblem.setStatus(
        ""
    )

vlLmopRedunDiskMirrorProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6383)
)
vlLmopRedunDiskMirrorProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLmopRedunDiskMirrorProblem.setStatus(
        ""
    )

vlLmopGeneralHWProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6384)
)
vlLmopGeneralHWProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlLmopGeneralHWProblem.setStatus(
        ""
    )

vlNati2A3mDspInitProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6385)
)
vlNati2A3mDspInitProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapDspNumber"))
)
if mibBuilder.loadTexts:
    vlNati2A3mDspInitProblem.setStatus(
        ""
    )

vlNati2McvpDspProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6386)
)
vlNati2McvpDspProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNati2McvpDspProblem.setStatus(
        ""
    )

vlNati2MatrixInitProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6387)
)
vlNati2MatrixInitProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNati2MatrixInitProblem.setStatus(
        ""
    )

vlNati2InitBoardProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6388)
)
vlNati2InitBoardProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNati2InitBoardProblem.setStatus(
        ""
    )

vlNati2FpgaProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6389)
)
vlNati2FpgaProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlNati2FpgaProblem.setStatus(
        ""
    )

vlNati2LineProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6390)
)
vlNati2LineProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapLineNumber"),
        ("Nice-MIB-II", "trapLineErrorType"),
        ("Nice-MIB-II", "trapLogicalStreamNumber"))
)
if mibBuilder.loadTexts:
    vlNati2LineProblem.setStatus(
        ""
    )

vlAli4DspInitProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6391)
)
vlAli4DspInitProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAli4DspInitProblem.setStatus(
        ""
    )

vlAli4MatrixInitProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6392)
)
vlAli4MatrixInitProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAli4MatrixInitProblem.setStatus(
        ""
    )

vlAli4CpldProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6393)
)
vlAli4CpldProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAli4CpldProblem.setStatus(
        ""
    )

vlAli4InitBoardProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6394)
)
vlAli4InitBoardProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAli4InitBoardProblem.setStatus(
        ""
    )

vlAli4LineProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6395)
)
vlAli4LineProblem.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"),
        ("Nice-MIB-II", "trapLineNumber"),
        ("Nice-MIB-II", "trapLineErrorType"),
        ("Nice-MIB-II", "trapLogicalStreamNumber"))
)
if mibBuilder.loadTexts:
    vlAli4LineProblem.setStatus(
        ""
    )

vlAli4ExtSqlshDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 4, 0, 6396)
)
vlAli4ExtSqlshDisconnected.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapBoardNumber"))
)
if mibBuilder.loadTexts:
    vlAli4ExtSqlshDisconnected.setStatus(
        ""
    )

vlBsvrNoMediaRetrieval = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6700)
)
vlBsvrNoMediaRetrieval.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrNoMediaRetrieval.setStatus(
        ""
    )

vlBsvrNoMediaManualArchive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6701)
)
vlBsvrNoMediaManualArchive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrNoMediaManualArchive.setStatus(
        ""
    )

vlBsvrAutoArchiveSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6702)
)
vlBsvrAutoArchiveSuspend.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrAutoArchiveSuspend.setStatus(
        ""
    )

vlBsvrRetrievalFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6703)
)
vlBsvrRetrievalFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"))
)
if mibBuilder.loadTexts:
    vlBsvrRetrievalFailed.setStatus(
        ""
    )

vlBsvrOverwMediaFailedrite = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6704)
)
vlBsvrOverwMediaFailedrite.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"))
)
if mibBuilder.loadTexts:
    vlBsvrOverwMediaFailedrite.setStatus(
        ""
    )

vlDeviceNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6705)
)
vlDeviceNotResponding.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"),
        ("Nice-MIB-II", "trapBackupConfig"),
        ("Nice-MIB-II", "trapBackupDeviceState"))
)
if mibBuilder.loadTexts:
    vlDeviceNotResponding.setStatus(
        ""
    )

vlBsvrNoMediaRecognized = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6706)
)
vlBsvrNoMediaRecognized.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"),
        ("Nice-MIB-II", "trapBackupConfig"))
)
if mibBuilder.loadTexts:
    vlBsvrNoMediaRecognized.setStatus(
        ""
    )

vlBsvrMediaError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6707)
)
vlBsvrMediaError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"),
        ("Nice-MIB-II", "trapBackupConfig"),
        ("Nice-MIB-II", "trapBackupDeviceState"))
)
if mibBuilder.loadTexts:
    vlBsvrMediaError.setStatus(
        ""
    )

vlBsvrMediaWriteProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6708)
)
vlBsvrMediaWriteProtected.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrMediaWriteProtected.setStatus(
        ""
    )

vlBsvrCannotAppend = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6709)
)
vlBsvrCannotAppend.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"))
)
if mibBuilder.loadTexts:
    vlBsvrCannotAppend.setStatus(
        ""
    )

vlBsvrNoMediaDataFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6710)
)
vlBsvrNoMediaDataFound.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrNoMediaDataFound.setStatus(
        ""
    )

vlBsvrDeviceOperationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6711)
)
vlBsvrDeviceOperationFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"),
        ("Nice-MIB-II", "trapBackupConfig"),
        ("Nice-MIB-II", "trapBackupDeviceState"))
)
if mibBuilder.loadTexts:
    vlBsvrDeviceOperationFailed.setStatus(
        ""
    )

vlBsvrRecoveryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6712)
)
vlBsvrRecoveryFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrRecoveryFailed.setStatus(
        ""
    )

vlBsvrArchivingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6713)
)
vlBsvrArchivingFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "backupErrorBSRVErrorCode"))
)
if mibBuilder.loadTexts:
    vlBsvrArchivingFailed.setStatus(
        ""
    )

vlBsvrOverwriteUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6714)
)
vlBsvrOverwriteUsageExceeded.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrOverwriteUsageExceeded.setStatus(
        ""
    )

vlBsvrMediaAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6715)
)
vlBsvrMediaAccessDenied.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"))
)
if mibBuilder.loadTexts:
    vlBsvrMediaAccessDenied.setStatus(
        ""
    )

vlBsvrDeviceShouldBeCleaned = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6716)
)
vlBsvrDeviceShouldBeCleaned.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"),
        ("Nice-MIB-II", "trapBackupDeviceState"))
)
if mibBuilder.loadTexts:
    vlBsvrDeviceShouldBeCleaned.setStatus(
        ""
    )

vlBsvrConnectRTSFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6717)
)
vlBsvrConnectRTSFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"),
        ("Nice-MIB-II", "trapBackupDeviceState"))
)
if mibBuilder.loadTexts:
    vlBsvrConnectRTSFailed.setStatus(
        ""
    )

vlBsvrAppendFailed_version = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6718)
)
vlBsvrAppendFailed_version.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsvrAppendFailed_version.setStatus(
        ""
    )

vlBsvrAutoArchiveSuspended_Retrieval = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6719)
)
vlBsvrAutoArchiveSuspended_Retrieval.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"))
)
if mibBuilder.loadTexts:
    vlBsvrAutoArchiveSuspended_Retrieval.setStatus(
        ""
    )

vlBsvrAutoArchiveSuspended_Manual = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6720)
)
vlBsvrAutoArchiveSuspended_Manual.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"))
)
if mibBuilder.loadTexts:
    vlBsvrAutoArchiveSuspended_Manual.setStatus(
        ""
    )

vlBsvrAutoArchiveSuspended_Erase = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6721)
)
vlBsvrAutoArchiveSuspended_Erase.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"))
)
if mibBuilder.loadTexts:
    vlBsvrAutoArchiveSuspended_Erase.setStatus(
        ""
    )

vlBsrvDvdArchiveCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6722)
)
vlBsrvDvdArchiveCompleted.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"))
)
if mibBuilder.loadTexts:
    vlBsrvDvdArchiveCompleted.setStatus(
        ""
    )

vlBsrvBackupServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 3, 2, 5, 0, 6723)
)
vlBsrvBackupServerError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "trapVLModuleName"),
        ("Nice-MIB-II", "trapVLModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "backupInstanceNumber"),
        ("Nice-MIB-II", "trapBackupConfig"),
        ("Nice-MIB-II", "trapBackupDeviceState"))
)
if mibBuilder.loadTexts:
    vlBsrvBackupServerError.setStatus(
        ""
    )

driverIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 0, 4001)
)
driverIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverName"),
        ("Nice-MIB-II", "driverStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverIsUp.setStatus(
        ""
    )

driverRegistryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 0, 4018)
)
driverRegistryError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRegistryKey"))
)
if mibBuilder.loadTexts:
    driverRegistryError.setStatus(
        ""
    )

driverRegistryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 0, 4019)
)
driverRegistryWarning.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRegistryKey"))
)
if mibBuilder.loadTexts:
    driverRegistryWarning.setStatus(
        ""
    )

driverIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 0, 4002)
)
driverIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverName"),
        ("Nice-MIB-II", "driverStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverIsDown.setStatus(
        ""
    )

driverConfigurationFileIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 0, 4003)
)
driverConfigurationFileIsMissing.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverName"),
        ("Nice-MIB-II", "driverStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapFileName"))
)
if mibBuilder.loadTexts:
    driverConfigurationFileIsMissing.setStatus(
        ""
    )

driverSignificantConfigurationFileDataIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 0, 4004)
)
driverSignificantConfigurationFileDataIsMissing.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverName"),
        ("Nice-MIB-II", "driverStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapFileName"))
)
if mibBuilder.loadTexts:
    driverSignificantConfigurationFileDataIsMissing.setStatus(
        ""
    )

driverConfigurationFileDataIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 1, 0, 4005)
)
driverConfigurationFileDataIsMissing.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverName"),
        ("Nice-MIB-II", "driverStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapFileName"))
)
if mibBuilder.loadTexts:
    driverConfigurationFileDataIsMissing.setStatus(
        ""
    )

driverConnectionToCapiIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4006)
)
driverConnectionToCapiIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverConnectionToCapiIsDown.setStatus(
        ""
    )

driverConnectionToCapiIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4007)
)
driverConnectionToCapiIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverConnectionToCapiIsUp.setStatus(
        ""
    )

driverConnectionToSwitchIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4008)
)
driverConnectionToSwitchIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverConnectionToSwitchIsDown.setStatus(
        ""
    )

driverConnectionToSwitchIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4009)
)
driverConnectionToSwitchIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverConnectionToSwitchIsUp.setStatus(
        ""
    )

driverInternalEngineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4010)
)
driverInternalEngineError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverInternalEngineError.setStatus(
        ""
    )

driverInternalEngineOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4011)
)
driverInternalEngineOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverInternalEngineOK.setStatus(
        ""
    )

driverCapiError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4012)
)
driverCapiError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverCapiError.setStatus(
        ""
    )

driverCapiOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4013)
)
driverCapiOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverCapiOK.setStatus(
        ""
    )

driverCTIEngineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4014)
)
driverCTIEngineError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverCTIEngineError.setStatus(
        ""
    )

driverCTIEngineWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4015)
)
driverCTIEngineWarning.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverCTIEngineWarning.setStatus(
        ""
    )

driverCTIEngineOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4016)
)
driverCTIEngineOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    driverCTIEngineOK.setStatus(
        ""
    )

driverMonitorEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 4, 2, 0, 4017)
)
driverMonitorEnd.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "driverModuleName"),
        ("Nice-MIB-II", "driverModuleStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDeviceId"))
)
if mibBuilder.loadTexts:
    driverMonitorEnd.setStatus(
        ""
    )

appsServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5001)
)
appsServerIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsServerIsDown.setStatus(
        ""
    )

appsServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5002)
)
appsServerIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsServerIsUp.setStatus(
        ""
    )

appsSystemAdminHostConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5003)
)
appsSystemAdminHostConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsSystemAdminHostConnectionIsDown.setStatus(
        ""
    )

appsSystemAdminHostConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5004)
)
appsSystemAdminHostConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsSystemAdminHostConnectionIsUp.setStatus(
        ""
    )

appsAdminDataBaseConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5005)
)
appsAdminDataBaseConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsAdminDataBaseConnectionIsDown.setStatus(
        ""
    )

appsAdminDataBaseConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5006)
)
appsAdminDataBaseConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsAdminDataBaseConnectionIsUp.setStatus(
        ""
    )

appsLoggerIsNotAttachToACLS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5007)
)
appsLoggerIsNotAttachToACLS.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerId"))
)
if mibBuilder.loadTexts:
    appsLoggerIsNotAttachToACLS.setStatus(
        ""
    )

appsCLSConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5008)
)
appsCLSConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapCLSId"))
)
if mibBuilder.loadTexts:
    appsCLSConnectionIsDown.setStatus(
        ""
    )

appsCLSConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5009)
)
appsCLSConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapCLSId"))
)
if mibBuilder.loadTexts:
    appsCLSConnectionIsUp.setStatus(
        ""
    )

appsLoggerConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5010)
)
appsLoggerConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerId"))
)
if mibBuilder.loadTexts:
    appsLoggerConnectionIsDown.setStatus(
        ""
    )

appsLoggerConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5011)
)
appsLoggerConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapLoggerId"))
)
if mibBuilder.loadTexts:
    appsLoggerConnectionIsUp.setStatus(
        ""
    )

appsSCConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5012)
)
appsSCConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapSCId"))
)
if mibBuilder.loadTexts:
    appsSCConnectionIsDown.setStatus(
        ""
    )

appsSCConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5013)
)
appsSCConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapSCId"))
)
if mibBuilder.loadTexts:
    appsSCConnectionIsUp.setStatus(
        ""
    )

appsCTIDBConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5014)
)
appsCTIDBConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsCTIDBConnectionIsDown.setStatus(
        ""
    )

appsCTIDBConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5015)
)
appsCTIDBConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsCTIDBConnectionIsUp.setStatus(
        ""
    )

appsCADBConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5016)
)
appsCADBConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsCADBConnectionIsDown.setStatus(
        ""
    )

appsCADBConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5017)
)
appsCADBConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsCADBConnectionIsUp.setStatus(
        ""
    )

appsNIFDBConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5018)
)
appsNIFDBConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsNIFDBConnectionIsDown.setStatus(
        ""
    )

appsNIFDBConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5019)
)
appsNIFDBConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsNIFDBConnectionIsUp.setStatus(
        ""
    )

appsInteractionDBConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5020)
)
appsInteractionDBConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsInteractionDBConnectionIsDown.setStatus(
        ""
    )

appsInteractionDBConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5021)
)
appsInteractionDBConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsInteractionDBConnectionIsUp.setStatus(
        ""
    )

appsUserAdminHostConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5022)
)
appsUserAdminHostConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsUserAdminHostConnectionIsDown.setStatus(
        ""
    )

appsUserAdminHostConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5023)
)
appsUserAdminHostConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    appsUserAdminHostConnectionIsUp.setStatus(
        ""
    )

appsRuleEngineEventProviderFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5024)
)
appsRuleEngineEventProviderFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapEventProviderId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineEventProviderFailed.setStatus(
        ""
    )

appsRuleEngineEventProviderSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5025)
)
appsRuleEngineEventProviderSucceeded.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapEventProviderId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineEventProviderSucceeded.setStatus(
        ""
    )

appsRuleEngineEventProviderIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5026)
)
appsRuleEngineEventProviderIdle.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapEventProviderId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineEventProviderIdle.setStatus(
        ""
    )

appsRuleEngineEventProviderActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5027)
)
appsRuleEngineEventProviderActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapEventProviderId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineEventProviderActive.setStatus(
        ""
    )

appsRuleEngineRuleGeneratorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5028)
)
appsRuleEngineRuleGeneratorFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRuleGeneratorId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineRuleGeneratorFailed.setStatus(
        ""
    )

appsRuleEngineRuleGeneratorSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5029)
)
appsRuleEngineRuleGeneratorSucceeded.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRuleGeneratorId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineRuleGeneratorSucceeded.setStatus(
        ""
    )

appsRuleEngineRuleGeneratorIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5030)
)
appsRuleEngineRuleGeneratorIdle.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRuleGeneratorId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineRuleGeneratorIdle.setStatus(
        ""
    )

appsRuleEngineRuleGeneratorActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5031)
)
appsRuleEngineRuleGeneratorActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapRuleGeneratorId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineRuleGeneratorActive.setStatus(
        ""
    )

appsRuleEngineActionExecuterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5032)
)
appsRuleEngineActionExecuterFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapActionExecuterId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineActionExecuterFailed.setStatus(
        ""
    )

appsRuleEngineActionExecuterSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5033)
)
appsRuleEngineActionExecuterSucceeded.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapActionExecuterId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineActionExecuterSucceeded.setStatus(
        ""
    )

appsRuleEngineActionExecuterIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5034)
)
appsRuleEngineActionExecuterIdle.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapActionExecuterId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineActionExecuterIdle.setStatus(
        ""
    )

appsRuleEngineActionExecuterActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5035)
)
appsRuleEngineActionExecuterActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapActionExecuterId"))
)
if mibBuilder.loadTexts:
    appsRuleEngineActionExecuterActive.setStatus(
        ""
    )

appsRuleMngrDataBaseConnectionIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5036)
)
appsRuleMngrDataBaseConnectionIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsRuleMngrDataBaseConnectionIsDown.setStatus(
        ""
    )

appsRuleMngrDataBaseConnectionIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 5, 1, 0, 5037)
)
appsRuleMngrDataBaseConnectionIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "applicationName"),
        ("Nice-MIB-II", "applicationStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBId"))
)
if mibBuilder.loadTexts:
    appsRuleMngrDataBaseConnectionIsUp.setStatus(
        ""
    )

rdExceptionWhileProcessing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8000)
)
rdExceptionWhileProcessing.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    rdExceptionWhileProcessing.setStatus(
        ""
    )

rdApplicationFailedToInitialize = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8001)
)
rdApplicationFailedToInitialize.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    rdApplicationFailedToInitialize.setStatus(
        ""
    )

rdApplicationStartUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8002)
)
rdApplicationStartUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    rdApplicationStartUp.setStatus(
        ""
    )

rdKeepAliveHeartBeatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8003)
)
rdKeepAliveHeartBeatFail.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    rdKeepAliveHeartBeatFail.setStatus(
        ""
    )

rdConnectionToCLSIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8004)
)
rdConnectionToCLSIsActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdCLSID"),
        ("Nice-MIB-II", "rdCLSIpAddress"))
)
if mibBuilder.loadTexts:
    rdConnectionToCLSIsActive.setStatus(
        ""
    )

rdConnectionToCLSIsNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8005)
)
rdConnectionToCLSIsNotActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdCLSID"),
        ("Nice-MIB-II", "rdCLSIpAddress"))
)
if mibBuilder.loadTexts:
    rdConnectionToCLSIsNotActive.setStatus(
        ""
    )

rdConnectionToCLSLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8006)
)
rdConnectionToCLSLost.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdCLSID"),
        ("Nice-MIB-II", "rdCLSIpAddress"))
)
if mibBuilder.loadTexts:
    rdConnectionToCLSLost.setStatus(
        ""
    )

rdConnectionToLoggerIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8007)
)
rdConnectionToLoggerIsActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdLoggerID"),
        ("Nice-MIB-II", "rdLoggerIpAddress"))
)
if mibBuilder.loadTexts:
    rdConnectionToLoggerIsActive.setStatus(
        ""
    )

rdConnectionToLoggerIsNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8008)
)
rdConnectionToLoggerIsNotActive.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdLoggerID"),
        ("Nice-MIB-II", "rdLoggerIpAddress"))
)
if mibBuilder.loadTexts:
    rdConnectionToLoggerIsNotActive.setStatus(
        ""
    )

rdConnectionToLoggerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8009)
)
rdConnectionToLoggerLost.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdLoggerID"),
        ("Nice-MIB-II", "rdLoggerIpAddress"))
)
if mibBuilder.loadTexts:
    rdConnectionToLoggerLost.setStatus(
        ""
    )

rdTaskStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8010)
)
rdTaskStarted.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdTaskName"),
        ("Nice-MIB-II", "rdTaskType"))
)
if mibBuilder.loadTexts:
    rdTaskStarted.setStatus(
        ""
    )

rdTaskCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8011)
)
rdTaskCompleted.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdTaskName"),
        ("Nice-MIB-II", "rdTaskType"),
        ("Nice-MIB-II", "rdTaskCurrentState"),
        ("Nice-MIB-II", "rdTaskExecElements"),
        ("Nice-MIB-II", "rdTaskExecFailElements"),
        ("Nice-MIB-II", "rdTaskLastError"))
)
if mibBuilder.loadTexts:
    rdTaskCompleted.setStatus(
        ""
    )

rdMatchingSessionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8012)
)
rdMatchingSessionFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdTaskName"),
        ("Nice-MIB-II", "trapCLSId"),
        ("Nice-MIB-II", "trapLoggerId"),
        ("Nice-MIB-II", "trapRecordingChannel"),
        ("Nice-MIB-II", "trapRecordingStartTime"),
        ("Nice-MIB-II", "trapRecordingStopTime"))
)
if mibBuilder.loadTexts:
    rdMatchingSessionFailed.setStatus(
        ""
    )

rdMatchingPerdiodFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8013)
)
rdMatchingPerdiodFailed.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdTaskName"),
        ("Nice-MIB-II", "trapCLSId"),
        ("Nice-MIB-II", "trapLoggerId"),
        ("Nice-MIB-II", "trapRecordingChannel"),
        ("Nice-MIB-II", "trapRecordingStartTime"),
        ("Nice-MIB-II", "trapRecordingStopTime"))
)
if mibBuilder.loadTexts:
    rdMatchingPerdiodFailed.setStatus(
        ""
    )

rdCLSGeneralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 1, 0, 8014)
)
rdCLSGeneralError.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "rdName"),
        ("Nice-MIB-II", "rdStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "rdCLSID"),
        ("Nice-MIB-II", "rdCLSIpAddress"))
)
if mibBuilder.loadTexts:
    rdCLSGeneralError.setStatus(
        ""
    )

dbCallsBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7001)
)
dbCallsBackupFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbCallsBackupFinished.setStatus(
        ""
    )

dbCallsBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7002)
)
dbCallsBackupFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbCallsBackupFailed.setStatus(
        ""
    )

dbAdminBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7003)
)
dbAdminBackupFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAdminBackupFinished.setStatus(
        ""
    )

dbAdminBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7004)
)
dbAdminBackupFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAdminBackupFailed.setStatus(
        ""
    )

dbAuditBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7005)
)
dbAuditBackupFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAuditBackupFinished.setStatus(
        ""
    )

dbAuditBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7006)
)
dbAuditBackupFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAuditBackupFailed.setStatus(
        ""
    )

dbReindexJobFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7007)
)
dbReindexJobFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbReindexJobFinished.setStatus(
        ""
    )

dbReindexJobFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7008)
)
dbReindexJobFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbReindexJobFailed.setStatus(
        ""
    )

dbAuditAutoDeletionFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7009)
)
dbAuditAutoDeletionFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAuditAutoDeletionFinished.setStatus(
        ""
    )

dbAuditAutoDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7010)
)
dbAuditAutoDeletionFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAuditAutoDeletionFailed.setStatus(
        ""
    )

dbCallsDbSpaceIsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7011)
)
dbCallsDbSpaceIsLow.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbCallsDbSpaceIsLow.setStatus(
        ""
    )

dbCallsDbFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7012)
)
dbCallsDbFull.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbCallsDbFull.setStatus(
        ""
    )

dbAuditDbSpaceIsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7013)
)
dbAuditDbSpaceIsLow.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAuditDbSpaceIsLow.setStatus(
        ""
    )

dbAuditDbFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7014)
)
dbAuditDbFull.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAuditDbFull.setStatus(
        ""
    )

dbAdminDbSpaceIsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7015)
)
dbAdminDbSpaceIsLow.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAdminDbSpaceIsLow.setStatus(
        ""
    )

dbAdminDbFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7016)
)
dbAdminDbFull.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbAdminDbFull.setStatus(
        ""
    )

dbInserterMissingCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7017)
)
dbInserterMissingCalls.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbInserterMissingCalls.setStatus(
        ""
    )

dbReplicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7018)
)
dbReplicationFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbReplicationFailed.setStatus(
        ""
    )

dbRuleBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7019)
)
dbRuleBackupFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbRuleBackupFinished.setStatus(
        ""
    )

dbRuleBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7020)
)
dbRuleBackupFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbRuleBackupFailed.setStatus(
        ""
    )

dbMsdbBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7021)
)
dbMsdbBackupFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbMsdbBackupFinished.setStatus(
        ""
    )

dbMsdbBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7022)
)
dbMsdbBackupFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbMsdbBackupFailed.setStatus(
        ""
    )

dbMasterBackupFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7023)
)
dbMasterBackupFinished.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbMasterBackupFinished.setStatus(
        ""
    )

dbMasterBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7024)
)
dbMasterBackupFailed.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbMasterBackupFailed.setStatus(
        ""
    )

dbRuleDBFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7025)
)
dbRuleDBFull.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbRuleDBFull.setStatus(
        ""
    )

dbRuleDBSpaceIsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 7, 2, 0, 7026)
)
dbRuleDBSpaceIsLow.setObjects(
    ("Nice-MIB-II", "trapSeverity")
)
if mibBuilder.loadTexts:
    dbRuleDBSpaceIsLow.setStatus(
        ""
    )

ctiDBServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8001)
)
ctiDBServerIsUp.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiDBServerIsUp.setStatus(
        ""
    )

ctiDBServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8002)
)
ctiDBServerIsDown.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiDBServerIsDown.setStatus(
        ""
    )

ctiDBServerIsNotInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8003)
)
ctiDBServerIsNotInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiDBServerIsNotInitializedProperly.setStatus(
        ""
    )

ctiDBServerIsInitializedProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8004)
)
ctiDBServerIsInitializedProperly.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiDBServerIsInitializedProperly.setStatus(
        ""
    )

ctiDBSpaceIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8005)
)
ctiDBSpaceIsFull.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    ctiDBSpaceIsFull.setStatus(
        ""
    )

ctiDBSpaceIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8006)
)
ctiDBSpaceIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiDBSpaceIsOK.setStatus(
        ""
    )

ctiDBLogSpaceIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8007)
)
ctiDBLogSpaceIsFull.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    ctiDBLogSpaceIsFull.setStatus(
        ""
    )

ctiDBLogSpaceIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8008)
)
ctiDBLogSpaceIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiDBLogSpaceIsOK.setStatus(
        ""
    )

ctiConnectionToDBIsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8009)
)
ctiConnectionToDBIsOK.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiConnectionToDBIsOK.setStatus(
        ""
    )

ctiFailedConnectToDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8010)
)
ctiFailedConnectToDB.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    ctiFailedConnectToDB.setStatus(
        ""
    )

ctiMissingLookUpTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8011)
)
ctiMissingLookUpTable.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapSQLTableName"))
)
if mibBuilder.loadTexts:
    ctiMissingLookUpTable.setStatus(
        ""
    )

ctiFailedToInsertCTIEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8012)
)
ctiFailedToInsertCTIEvent.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    ctiFailedToInsertCTIEvent.setStatus(
        ""
    )

ctiDBRetentionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8013)
)
ctiDBRetentionFailure.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"),
        ("Nice-MIB-II", "trapDBErrorCode"))
)
if mibBuilder.loadTexts:
    ctiDBRetentionFailure.setStatus(
        ""
    )

ctiInvalidMessageReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 3167, 1, 8, 0, 8014)
)
ctiInvalidMessageReceived.setObjects(
      *(("Nice-MIB-II", "trapSeverity"),
        ("Nice-MIB-II", "ctiDBServerName"),
        ("Nice-MIB-II", "ctiDBServerStatus"),
        ("Nice-MIB-II", "trapHostTime"))
)
if mibBuilder.loadTexts:
    ctiInvalidMessageReceived.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nice-MIB-II",
    **{"HostLocalTime": HostLocalTime,
       "YesNo": YesNo,
       "SeverityType": SeverityType,
       "ClsErrorType": ClsErrorType,
       "RecordedMediaType": RecordedMediaType,
       "LoggerInitializationStatus": LoggerInitializationStatus,
       "OsDiskFailureType": OsDiskFailureType,
       "ClsTableType": ClsTableType,
       "ApplicationErrorType": ApplicationErrorType,
       "DriverErrorType": DriverErrorType,
       "CTIEventsDBServerErrorType": CTIEventsDBServerErrorType,
       "LoggingInstanceType": LoggingInstanceType,
       "LoggingErrorType": LoggingErrorType,
       "CaptureInstanceType": CaptureInstanceType,
       "CaptureErrorType": CaptureErrorType,
       "BackupErrorType": BackupErrorType,
       "BackupInstanceType": BackupInstanceType,
       "BackupErrorBSRVErrorCode": BackupErrorBSRVErrorCode,
       "BackupConfig": BackupConfig,
       "BackupDeviceState": BackupDeviceState,
       "LineErrorType": LineErrorType,
       "BoardType": BoardType,
       "RdTaskType": RdTaskType,
       "TaskState": TaskState,
       "RdErrorType": RdErrorType,
       "RdConnStatus": RdConnStatus,
       "nice": nice,
       "niceMib-2": niceMib_2,
       "trapsInfo": trapsInfo,
       "trapSeverity": trapSeverity,
       "trapLoggerId": trapLoggerId,
       "trapRecordedMedia": trapRecordedMedia,
       "trapLoggerInitialization": trapLoggerInitialization,
       "trapDBErrorCode": trapDBErrorCode,
       "trapOsDiskFailure": trapOsDiskFailure,
       "trapClsTableType": trapClsTableType,
       "trapDiskUsage": trapDiskUsage,
       "trapLoggerInitializationStatus": trapLoggerInitializationStatus,
       "trapHostTime": trapHostTime,
       "trapCLSId": trapCLSId,
       "trapSCId": trapSCId,
       "trapDBId": trapDBId,
       "trapFileName": trapFileName,
       "trapDeviceId": trapDeviceId,
       "trapRegistryKey": trapRegistryKey,
       "trapVLModuleName": trapVLModuleName,
       "trapVLModuleStatus": trapVLModuleStatus,
       "trapDiskDrive": trapDiskDrive,
       "trapLoggerIdInChain": trapLoggerIdInChain,
       "trapFreeSpacePercentage": trapFreeSpacePercentage,
       "trapKeptSpacePercentage": trapKeptSpacePercentage,
       "trapChannelNumber": trapChannelNumber,
       "trapBoardNumber": trapBoardNumber,
       "trapDspNumber": trapDspNumber,
       "trapLineNumber": trapLineNumber,
       "trapLineProblem": trapLineProblem,
       "trapDataLineNumber": trapDataLineNumber,
       "trapDaughterBoardNumber": trapDaughterBoardNumber,
       "trapSQLTableName": trapSQLTableName,
       "trapEventProviderId": trapEventProviderId,
       "trapRuleGeneratorId": trapRuleGeneratorId,
       "trapActionExecuterId": trapActionExecuterId,
       "trapLineErrorType": trapLineErrorType,
       "trapRecordingChannel": trapRecordingChannel,
       "trapRecordingStartTime": trapRecordingStartTime,
       "trapRecordingStopTime": trapRecordingStopTime,
       "trapNumOfChannels": trapNumOfChannels,
       "trapBoardOrLogicalTrunk": trapBoardOrLogicalTrunk,
       "trapChannelOrTimeslot": trapChannelOrTimeslot,
       "trapMateLogicalTrunk": trapMateLogicalTrunk,
       "trapMateTimeslot": trapMateTimeslot,
       "trapBoardType": trapBoardType,
       "trapLogicalStreamNumber": trapLogicalStreamNumber,
       "trapBackupConfig": trapBackupConfig,
       "trapBackupDeviceState": trapBackupDeviceState,
       "cls": cls,
       "clsRcm": clsRcm,
       "clsRcmIsDown": clsRcmIsDown,
       "clsRcmIsUp": clsRcmIsUp,
       "clsRecordIsInsertedToDB": clsRecordIsInsertedToDB,
       "clsCommunicationProblemWithLogger": clsCommunicationProblemWithLogger,
       "clsCommunicationToLoggerIsOK": clsCommunicationToLoggerIsOK,
       "clsProblematicClockDifferencesWithLogger": clsProblematicClockDifferencesWithLogger,
       "clsNoClockDifferencesWithLogger": clsNoClockDifferencesWithLogger,
       "clsNoAvailableResources": clsNoAvailableResources,
       "clsResourcesAreAvailable": clsResourcesAreAvailable,
       "clsLoggerIsNotInitializedProperly": clsLoggerIsNotInitializedProperly,
       "clsLoggerIsInitializedProperly": clsLoggerIsInitializedProperly,
       "clsRCMIsNotInitializedProperly": clsRCMIsNotInitializedProperly,
       "clsRCMIsInitializedProperly": clsRCMIsInitializedProperly,
       "clsProblemWithNPLUS1Loggers": clsProblemWithNPLUS1Loggers,
       "clsNPLUS1LoggersAreOK": clsNPLUS1LoggersAreOK,
       "rcmName": rcmName,
       "rcmStatus": rcmStatus,
       "rcmPendingErrorsTable": rcmPendingErrorsTable,
       "rcmPendingErrorsEntry": rcmPendingErrorsEntry,
       "rcmErrorType": rcmErrorType,
       "rcmErrorReflectedStatus": rcmErrorReflectedStatus,
       "rcmErrorLoggerId": rcmErrorLoggerId,
       "rcmErrorIndex": rcmErrorIndex,
       "clsCallServer": clsCallServer,
       "clsCallServerIsDown": clsCallServerIsDown,
       "clsCallServerIsUp": clsCallServerIsUp,
       "clsCallServerLinkIsDown": clsCallServerLinkIsDown,
       "clsCallServerLinkIsUp": clsCallServerLinkIsUp,
       "clsCallServerTableIsFull": clsCallServerTableIsFull,
       "clsCallServerTableIsOK": clsCallServerTableIsOK,
       "callServerName": callServerName,
       "callServerStatus": callServerStatus,
       "callServerPendingErrorsTable": callServerPendingErrorsTable,
       "callServerPendingErrorsEntry": callServerPendingErrorsEntry,
       "callServerErrorType": callServerErrorType,
       "callServerErrorReflectedStatus": callServerErrorReflectedStatus,
       "callServerErrorIndex": callServerErrorIndex,
       "clsSchedulerServer": clsSchedulerServer,
       "clsSchedulerServerIsDown": clsSchedulerServerIsDown,
       "clsSchedulerServerIsUp": clsSchedulerServerIsUp,
       "clsRecordingOnDemandIsNotEnabled": clsRecordingOnDemandIsNotEnabled,
       "clsRecordingOnDemandIsEnabled": clsRecordingOnDemandIsEnabled,
       "clsSchedulerServerIsNotInitializedProperly": clsSchedulerServerIsNotInitializedProperly,
       "clsSchedulerServerIsInitializedProperly": clsSchedulerServerIsInitializedProperly,
       "schedulerServerName": schedulerServerName,
       "schedulerServerStatus": schedulerServerStatus,
       "schedulerServerPendingErrorsTable": schedulerServerPendingErrorsTable,
       "schedulerServerPendingErrorsEntry": schedulerServerPendingErrorsEntry,
       "schedulerServerErrorType": schedulerServerErrorType,
       "schedulerServerErrorReflectedStatus": schedulerServerErrorReflectedStatus,
       "schedulerServerErrorIndex": schedulerServerErrorIndex,
       "clsDbServer": clsDbServer,
       "clsDBServerIsDown": clsDBServerIsDown,
       "clsDBServerIsUp": clsDBServerIsUp,
       "clsFailureConnectionToDB": clsFailureConnectionToDB,
       "clsConnectionToDBIsOK": clsConnectionToDBIsOK,
       "clsDBServerIsNotInitializedProperly": clsDBServerIsNotInitializedProperly,
       "clsDBServerIsInitializedProperly": clsDBServerIsInitializedProperly,
       "clsDBSpaceIsFull": clsDBSpaceIsFull,
       "clsDBSpaceIsOK": clsDBSpaceIsOK,
       "clsRecordIsNotInsertedToDBTheRecordIsLost": clsRecordIsNotInsertedToDBTheRecordIsLost,
       "dbServerName": dbServerName,
       "dbServerStatus": dbServerStatus,
       "dbServerPendingErrorsTable": dbServerPendingErrorsTable,
       "dbServerPendingErrorsEntry": dbServerPendingErrorsEntry,
       "dbServerErrorType": dbServerErrorType,
       "dbServerErrorReflectedStatus": dbServerErrorReflectedStatus,
       "dbServerDBErrorCode": dbServerDBErrorCode,
       "dbServerErrorIndex": dbServerErrorIndex,
       "clsDispatcher": clsDispatcher,
       "clsDispatchIsDown": clsDispatchIsDown,
       "clsDispatchIsUp": clsDispatchIsUp,
       "clsALLCLSModulesInitFailed": clsALLCLSModulesInitFailed,
       "clsALLCLSModulesInitOK": clsALLCLSModulesInitOK,
       "clsCLSModuleRestartFailed": clsCLSModuleRestartFailed,
       "clsCLSModuleRestartOK": clsCLSModuleRestartOK,
       "clsOSDiskFailure": clsOSDiskFailure,
       "clsOSDiskOK": clsOSDiskOK,
       "clsDispatcherName": clsDispatcherName,
       "clsDispatcherStatus": clsDispatcherStatus,
       "clsDispatcherPendingErrorsTable": clsDispatcherPendingErrorsTable,
       "clsDispatcherPendingErrorsEntry": clsDispatcherPendingErrorsEntry,
       "clsDispatcherErrorType": clsDispatcherErrorType,
       "clsDispatcherErrorReflectedStatus": clsDispatcherErrorReflectedStatus,
       "clsDispatcherErrorIndex": clsDispatcherErrorIndex,
       "clsAgentConfig": clsAgentConfig,
       "clsAgentIsRepeatingTraps": clsAgentIsRepeatingTraps,
       "clsAgentTrapsRepeatInterval": clsAgentTrapsRepeatInterval,
       "clsAgentVersion": clsAgentVersion,
       "logger": logger,
       "multiMediaLogger": multiMediaLogger,
       "mmlSnmpAgentConnectedToLogger": mmlSnmpAgentConnectedToLogger,
       "mmlConnectionToLoggerNotEstablished": mmlConnectionToLoggerNotEstablished,
       "mmlInvalidConfiguration": mmlInvalidConfiguration,
       "mmlPersistentMismatch": mmlPersistentMismatch,
       "mmlAbnormalPlaybackTermination": mmlAbnormalPlaybackTermination,
       "mmlAbnormalRecordTermination": mmlAbnormalRecordTermination,
       "mmlUnableToReplyDueToConnectionLoss": mmlUnableToReplyDueToConnectionLoss,
       "mmlFailToInitializeStorageDevice": mmlFailToInitializeStorageDevice,
       "mmlFailToInitializeDataSystem": mmlFailToInitializeDataSystem,
       "mmlFailToInitializeMemoryManager": mmlFailToInitializeMemoryManager,
       "mmlUnexpectedDisconnect": mmlUnexpectedDisconnect,
       "mmlConnectionCanNotBeEstablished": mmlConnectionCanNotBeEstablished,
       "mmlAllConnectionResourcesInUse": mmlAllConnectionResourcesInUse,
       "mmlConnectionTimeoutExceeded": mmlConnectionTimeoutExceeded,
       "mmlMemoryManagerOverflow": mmlMemoryManagerOverflow,
       "mmlAllocationFailure": mmlAllocationFailure,
       "mmlResourceAllocationFailure": mmlResourceAllocationFailure,
       "mmlOutputChannelAllocationFailure": mmlOutputChannelAllocationFailure,
       "mmlInputChannelAllocationFailure": mmlInputChannelAllocationFailure,
       "mmlResourceAccessFailure": mmlResourceAccessFailure,
       "mmlLoggerIsShuttingDown": mmlLoggerIsShuttingDown,
       "mmlLoggerIsReady": mmlLoggerIsReady,
       "mmlName": mmlName,
       "mmlStatus": mmlStatus,
       "mmlStorageSystem": mmlStorageSystem,
       "mmlStorageSystemInvalidConfiguration": mmlStorageSystemInvalidConfiguration,
       "mmlStorageSystemPersistentMismatch": mmlStorageSystemPersistentMismatch,
       "mmlConsistentDiskWriteFailure": mmlConsistentDiskWriteFailure,
       "mmlConsistentDiskReadFailure": mmlConsistentDiskReadFailure,
       "mmlDiskUsage": mmlDiskUsage,
       "mmlDiskIsFull": mmlDiskIsFull,
       "mmlDiskIOFailure": mmlDiskIOFailure,
       "mmlStorageSystemName": mmlStorageSystemName,
       "mmlStorageSystemStatus": mmlStorageSystemStatus,
       "mmlStorageSystemDiskUsage": mmlStorageSystemDiskUsage,
       "mmlDataSystem": mmlDataSystem,
       "mmlDataSystemInvalidConfiguration": mmlDataSystemInvalidConfiguration,
       "mmlDataSystemPersistentMismatch": mmlDataSystemPersistentMismatch,
       "mmlDataBaseConsistencyMismatch": mmlDataBaseConsistencyMismatch,
       "mmlCriticalDataSystemError": mmlCriticalDataSystemError,
       "mmlTableAccessFailure": mmlTableAccessFailure,
       "mmlDataSystemName": mmlDataSystemName,
       "mmlDataSystemStatus": mmlDataSystemStatus,
       "mmlAutoDeletion": mmlAutoDeletion,
       "mmlAutoDeletionInvalidConfiguration": mmlAutoDeletionInvalidConfiguration,
       "mmlAutoDeletionPersistentMismatch": mmlAutoDeletionPersistentMismatch,
       "mmlStartingAutoDeletionJob": mmlStartingAutoDeletionJob,
       "mmlFinishedNormal": mmlFinishedNormal,
       "mmlDeletionCapacityNotReached": mmlDeletionCapacityNotReached,
       "mmlAutoDeletionName": mmlAutoDeletionName,
       "mmlAutoDeletionStatus": mmlAutoDeletionStatus,
       "mmlAgentConfig": mmlAgentConfig,
       "mmlAgentIsRepeatingTraps": mmlAgentIsRepeatingTraps,
       "mmlAgentTrapsRepeatInterval": mmlAgentTrapsRepeatInterval,
       "mmlAgentVersion": mmlAgentVersion,
       "voiceLogger": voiceLogger,
       "vlLoggerNotResponding": vlLoggerNotResponding,
       "vlApiQueryError": vlApiQueryError,
       "voiceLoggerName": voiceLoggerName,
       "voiceLoggerStatus": voiceLoggerStatus,
       "voiceLoggerLogging": voiceLoggerLogging,
       "vlDbmConsistencyFailed": vlDbmConsistencyFailed,
       "vlDbmInitPartitionFailed": vlDbmInitPartitionFailed,
       "vlKernerHWDriverInitFailed": vlKernerHWDriverInitFailed,
       "vlVoipDriverInitFailed": vlVoipDriverInitFailed,
       "vlDliDriverInitFailed": vlDliDriverInitFailed,
       "vlAumGeneralInitFailure": vlAumGeneralInitFailure,
       "vlDiskOpenPartitionFailed": vlDiskOpenPartitionFailed,
       "vlDiskDriveProblem": vlDiskDriveProblem,
       "vlNPlus1ManualSwitch": vlNPlus1ManualSwitch,
       "vlNPlus1SpareIsBackingUp": vlNPlus1SpareIsBackingUp,
       "vlNPlus1ROBMalfunction": vlNPlus1ROBMalfunction,
       "vlNPlus1ROBPowerFailure": vlNPlus1ROBPowerFailure,
       "vlNPlus1SpareNeedLongUpdate": vlNPlus1SpareNeedLongUpdate,
       "vlAutoDeleteUnder3PercSpace": vlAutoDeleteUnder3PercSpace,
       "vlAutoDeleteNofreeSpace": vlAutoDeleteNofreeSpace,
       "vlAutoDeleteLowKeptSpace": vlAutoDeleteLowKeptSpace,
       "vlAutoDeleteNoKeptSpace": vlAutoDeleteNoKeptSpace,
       "vlDongleNotInitialized": vlDongleNotInitialized,
       "vlDongleAlreadyInitialized": vlDongleAlreadyInitialized,
       "vlDongleDeviceNotSupported": vlDongleDeviceNotSupported,
       "vlDongleInitFailed-function": vlDongleInitFailed_function,
       "vlDongleConnectFailed": vlDongleConnectFailed,
       "vlDongleInitFailed-network": vlDongleInitFailed_network,
       "vlDongleNoDevice": vlDongleNoDevice,
       "vlDongleInitFailed-parameter": vlDongleInitFailed_parameter,
       "vlDongleInitFailed-HLApi": vlDongleInitFailed_HLApi,
       "vlDongleInitFailed-memory": vlDongleInitFailed_memory,
       "vlDongleInitFailed-HLVDD": vlDongleInitFailed_HLVDD,
       "vlCheckSumInvalid": vlCheckSumInvalid,
       "vlChannelsLineError": vlChannelsLineError,
       "vlChannelsSomeNotRecording": vlChannelsSomeNotRecording,
       "vlChannelsLowStatAlarm": vlChannelsLowStatAlarm,
       "vlChannelsHighStatAlarm": vlChannelsHighStatAlarm,
       "loggingName": loggingName,
       "loggingStatus": loggingStatus,
       "loggingInstanceTable": loggingInstanceTable,
       "loggingInstanceEntry": loggingInstanceEntry,
       "loggingInstanceName": loggingInstanceName,
       "loggingInstanceStatus": loggingInstanceStatus,
       "loggingInstanceType": loggingInstanceType,
       "loggingInstanceNumberInType": loggingInstanceNumberInType,
       "loggingInstanceIndex": loggingInstanceIndex,
       "loggingPendingErrorsTable": loggingPendingErrorsTable,
       "loggingPendingErrorsEntry": loggingPendingErrorsEntry,
       "loggingErrorType": loggingErrorType,
       "loggingErrorReflectedStatus": loggingErrorReflectedStatus,
       "loggingErrorInstanceIndex": loggingErrorInstanceIndex,
       "loggingErrorIndex": loggingErrorIndex,
       "loggingErrorCode": loggingErrorCode,
       "voiceLoggerCapture": voiceLoggerCapture,
       "vlAdifDspIllegalCommand": vlAdifDspIllegalCommand,
       "vlAdifDspNoSynch": vlAdifDspNoSynch,
       "vlAdifDspSSIRXError": vlAdifDspSSIRXError,
       "vlAdifDspCodecError": vlAdifDspCodecError,
       "vlAdifDspIllegalParameter": vlAdifDspIllegalParameter,
       "vlAdifDspMPMLQError": vlAdifDspMPMLQError,
       "vlAdifDspStackOverflow": vlAdifDspStackOverflow,
       "vlAdifDspIllegalInstruction": vlAdifDspIllegalInstruction,
       "vlAdifNoInterrupts": vlAdifNoInterrupts,
       "vlAdifInternalBoardError": vlAdifInternalBoardError,
       "vlAdifNoSignal": vlAdifNoSignal,
       "vlAdifAlarmIndicationSignal": vlAdifAlarmIndicationSignal,
       "vlAdifLossOfSynch": vlAdifLossOfSynch,
       "vlAdifRemoteAlarmIndication": vlAdifRemoteAlarmIndication,
       "vlAdifFramingError": vlAdifFramingError,
       "vlApaInternalSelfTestFailed": vlApaInternalSelfTestFailed,
       "vlApaCommBoardDspError": vlApaCommBoardDspError,
       "vlApaIOError": vlApaIOError,
       "vlApaDspFirmwareLoadFailed": vlApaDspFirmwareLoadFailed,
       "vlApaDspRuntimeError": vlApaDspRuntimeError,
       "vlIsdnDspCommFailed": vlIsdnDspCommFailed,
       "vlIsdnIniterror": vlIsdnIniterror,
       "vlIsdnBSError": vlIsdnBSError,
       "vlIsdnLogicConnectError": vlIsdnLogicConnectError,
       "vlIsdnBoardSelfTestFailed": vlIsdnBoardSelfTestFailed,
       "vlIsdnLineError": vlIsdnLineError,
       "vlEtaiInitBoardFailed": vlEtaiInitBoardFailed,
       "vlEtaiLineError": vlEtaiLineError,
       "vlEtaiMatrixSwitchError": vlEtaiMatrixSwitchError,
       "vlEtaiDspError": vlEtaiDspError,
       "vlNtcmLoopError": vlNtcmLoopError,
       "vlNtcmInitError": vlNtcmInitError,
       "vlNtcmMatrixSwitchError": vlNtcmMatrixSwitchError,
       "vlTdaMatrizSwitchError": vlTdaMatrizSwitchError,
       "vlTdaDspError": vlTdaDspError,
       "vlTdaGeneralError": vlTdaGeneralError,
       "vlNatiChannelError": vlNatiChannelError,
       "vlNatiInitBoardError": vlNatiInitBoardError,
       "vlNatiMatrixSwitchError": vlNatiMatrixSwitchError,
       "vlNatiDspA3mError": vlNatiDspA3mError,
       "vlIsacSelectedClockError": vlIsacSelectedClockError,
       "vlIsacRightClockError": vlIsacRightClockError,
       "vlIsacLeftClockError": vlIsacLeftClockError,
       "vlIsacRightFameSynchError": vlIsacRightFameSynchError,
       "vlIsacLeftFrameSynchError": vlIsacLeftFrameSynchError,
       "vlIsacBoardError": vlIsacBoardError,
       "vlIsacTestToneError": vlIsacTestToneError,
       "vlIsacCriticalSystemError": vlIsacCriticalSystemError,
       "vlDliBoardCommError": vlDliBoardCommError,
       "vlDliChannelError": vlDliChannelError,
       "vlLafDspCommError": vlLafDspCommError,
       "vlLafFirmwareLoadError": vlLafFirmwareLoadError,
       "vlLafinitFailed": vlLafinitFailed,
       "vlLafConfigError": vlLafConfigError,
       "vlLafInvalidTime": vlLafInvalidTime,
       "vlLafLostSynch": vlLafLostSynch,
       "vlLafPowerProblem": vlLafPowerProblem,
       "vlLafMirrorFault": vlLafMirrorFault,
       "vlAdif3InitFailed-Dsp": vlAdif3InitFailed_Dsp,
       "vlAdif3InitFailed-timing": vlAdif3InitFailed_timing,
       "vlAdif3InitFailed-ADPCM": vlAdif3InitFailed_ADPCM,
       "vlAdif3InitFailed-HW": vlAdif3InitFailed_HW,
       "vlAdif3ExternalClockSynchError": vlAdif3ExternalClockSynchError,
       "vlUdaInitFailed-Dsp": vlUdaInitFailed_Dsp,
       "vlUdaMatrixInitFailed": vlUdaMatrixInitFailed,
       "vlUdaInitBoardFailed": vlUdaInitBoardFailed,
       "vlEtai2InitFailed-Dsp": vlEtai2InitFailed_Dsp,
       "vlEtai2MatrixInitError": vlEtai2MatrixInitError,
       "vlEtai2InitBoardFailed": vlEtai2InitBoardFailed,
       "vlEtai2LineProblem": vlEtai2LineProblem,
       "vlBtai2InitFailed-Dsp": vlBtai2InitFailed_Dsp,
       "vlBtai2MatrixInitError": vlBtai2MatrixInitError,
       "vlBtai2InitBoardFailed": vlBtai2InitBoardFailed,
       "vlBtai2FpgaError": vlBtai2FpgaError,
       "vlBtai2LineError": vlBtai2LineError,
       "vlIsac2RightClockError": vlIsac2RightClockError,
       "vlIsac2LeftClockError": vlIsac2LeftClockError,
       "vlIsac2RightFrameSynchError": vlIsac2RightFrameSynchError,
       "vlIsac2LeftFrameSynchError": vlIsac2LeftFrameSynchError,
       "vlIsac2BoardProblem": vlIsac2BoardProblem,
       "vlIsac2TestToneProblem": vlIsac2TestToneProblem,
       "vlIsac2SystemCriticalError": vlIsac2SystemCriticalError,
       "vlLmopRedunPowerProblem": vlLmopRedunPowerProblem,
       "vlLmopRedunDiskMirrorProblem": vlLmopRedunDiskMirrorProblem,
       "vlLmopGeneralHWProblem": vlLmopGeneralHWProblem,
       "vlNati2A3mDspInitProblem": vlNati2A3mDspInitProblem,
       "vlNati2McvpDspProblem": vlNati2McvpDspProblem,
       "vlNati2MatrixInitProblem": vlNati2MatrixInitProblem,
       "vlNati2InitBoardProblem": vlNati2InitBoardProblem,
       "vlNati2FpgaProblem": vlNati2FpgaProblem,
       "vlNati2LineProblem": vlNati2LineProblem,
       "vlAli4DspInitProblem": vlAli4DspInitProblem,
       "vlAli4MatrixInitProblem": vlAli4MatrixInitProblem,
       "vlAli4CpldProblem": vlAli4CpldProblem,
       "vlAli4InitBoardProblem": vlAli4InitBoardProblem,
       "vlAli4LineProblem": vlAli4LineProblem,
       "vlAli4ExtSqlshDisconnected": vlAli4ExtSqlshDisconnected,
       "captureName": captureName,
       "captureStatus": captureStatus,
       "captureInstanceTable": captureInstanceTable,
       "captureInstanceEntry": captureInstanceEntry,
       "captureInstanceName": captureInstanceName,
       "captureInstanceStatus": captureInstanceStatus,
       "captureInstanceType": captureInstanceType,
       "captureInstanceNumberInType": captureInstanceNumberInType,
       "captureInstanceIndex": captureInstanceIndex,
       "capturePendingErrorsTable": capturePendingErrorsTable,
       "capturePendingErrorsEntry": capturePendingErrorsEntry,
       "captureErrorType": captureErrorType,
       "captureErrorReflectedStatus": captureErrorReflectedStatus,
       "captureErrorInstanceIndex": captureErrorInstanceIndex,
       "captureErrorIndex": captureErrorIndex,
       "captureErrorCode": captureErrorCode,
       "voiceLoggerBackup": voiceLoggerBackup,
       "vlBsvrNoMediaRetrieval": vlBsvrNoMediaRetrieval,
       "vlBsvrNoMediaManualArchive": vlBsvrNoMediaManualArchive,
       "vlBsvrAutoArchiveSuspend": vlBsvrAutoArchiveSuspend,
       "vlBsvrRetrievalFailed": vlBsvrRetrievalFailed,
       "vlBsvrOverwMediaFailedrite": vlBsvrOverwMediaFailedrite,
       "vlDeviceNotResponding": vlDeviceNotResponding,
       "vlBsvrNoMediaRecognized": vlBsvrNoMediaRecognized,
       "vlBsvrMediaError": vlBsvrMediaError,
       "vlBsvrMediaWriteProtected": vlBsvrMediaWriteProtected,
       "vlBsvrCannotAppend": vlBsvrCannotAppend,
       "vlBsvrNoMediaDataFound": vlBsvrNoMediaDataFound,
       "vlBsvrDeviceOperationFailed": vlBsvrDeviceOperationFailed,
       "vlBsvrRecoveryFailed": vlBsvrRecoveryFailed,
       "vlBsvrArchivingFailed": vlBsvrArchivingFailed,
       "vlBsvrOverwriteUsageExceeded": vlBsvrOverwriteUsageExceeded,
       "vlBsvrMediaAccessDenied": vlBsvrMediaAccessDenied,
       "vlBsvrDeviceShouldBeCleaned": vlBsvrDeviceShouldBeCleaned,
       "vlBsvrConnectRTSFailed": vlBsvrConnectRTSFailed,
       "vlBsvrAppendFailed-version": vlBsvrAppendFailed_version,
       "vlBsvrAutoArchiveSuspended-Retrieval": vlBsvrAutoArchiveSuspended_Retrieval,
       "vlBsvrAutoArchiveSuspended-Manual": vlBsvrAutoArchiveSuspended_Manual,
       "vlBsvrAutoArchiveSuspended-Erase": vlBsvrAutoArchiveSuspended_Erase,
       "vlBsrvDvdArchiveCompleted": vlBsrvDvdArchiveCompleted,
       "vlBsrvBackupServerError": vlBsrvBackupServerError,
       "backupName": backupName,
       "backupStatus": backupStatus,
       "backupInstanceTable": backupInstanceTable,
       "backupInstanceEntry": backupInstanceEntry,
       "backupInstanceName": backupInstanceName,
       "backupInstanceStatus": backupInstanceStatus,
       "backupInstanceNumber": backupInstanceNumber,
       "backupInstanceRemoteNumber": backupInstanceRemoteNumber,
       "backupInstanceType": backupInstanceType,
       "backupPendingErrorsTable": backupPendingErrorsTable,
       "backupPendingErrorsEntry": backupPendingErrorsEntry,
       "backupErrorType": backupErrorType,
       "backupErrorReflectedStatus": backupErrorReflectedStatus,
       "backupErrorBSRVErrorCode": backupErrorBSRVErrorCode,
       "backupErrorInstanceIndex": backupErrorInstanceIndex,
       "backupErrorIndex": backupErrorIndex,
       "voiceLoggerSnmpAgentConfig": voiceLoggerSnmpAgentConfig,
       "voiceLoggerAgentIsRepeatingTraps": voiceLoggerAgentIsRepeatingTraps,
       "voiceLoggerTrapsRepeatInterval": voiceLoggerTrapsRepeatInterval,
       "voiceLoggerAgentVersion": voiceLoggerAgentVersion,
       "drivers": drivers,
       "driverIsUp": driverIsUp,
       "driverRegistryError": driverRegistryError,
       "driverRegistryWarning": driverRegistryWarning,
       "driversTable": driversTable,
       "driverIsDown": driverIsDown,
       "driverConfigurationFileIsMissing": driverConfigurationFileIsMissing,
       "driverSignificantConfigurationFileDataIsMissing": driverSignificantConfigurationFileDataIsMissing,
       "driverConfigurationFileDataIsMissing": driverConfigurationFileDataIsMissing,
       "driversEntry": driversEntry,
       "driverName": driverName,
       "driverStatus": driverStatus,
       "driverId": driverId,
       "driverNumberOfDevicesMonitored": driverNumberOfDevicesMonitored,
       "driverNumberOfSegments": driverNumberOfSegments,
       "driverNumberOfCompound": driverNumberOfCompound,
       "driverModulesTable": driverModulesTable,
       "driverConnectionToCapiIsDown": driverConnectionToCapiIsDown,
       "driverConnectionToCapiIsUp": driverConnectionToCapiIsUp,
       "driverConnectionToSwitchIsDown": driverConnectionToSwitchIsDown,
       "driverConnectionToSwitchIsUp": driverConnectionToSwitchIsUp,
       "driverInternalEngineError": driverInternalEngineError,
       "driverInternalEngineOK": driverInternalEngineOK,
       "driverCapiError": driverCapiError,
       "driverCapiOK": driverCapiOK,
       "driverCTIEngineError": driverCTIEngineError,
       "driverCTIEngineWarning": driverCTIEngineWarning,
       "driverCTIEngineOK": driverCTIEngineOK,
       "driverMonitorEnd": driverMonitorEnd,
       "driverModulesEntry": driverModulesEntry,
       "driverModuleName": driverModuleName,
       "driverModuleStatus": driverModuleStatus,
       "driverIdInModulesTable": driverIdInModulesTable,
       "driverModuleId": driverModuleId,
       "driversPendingErrorsTable": driversPendingErrorsTable,
       "driversPendingErrorsEntry": driversPendingErrorsEntry,
       "driverErrorType": driverErrorType,
       "driverErrorReflectedStatus": driverErrorReflectedStatus,
       "driverIdInDriversErrors": driverIdInDriversErrors,
       "driverErrorIndex": driverErrorIndex,
       "driversModulePendingErrorsTable": driversModulePendingErrorsTable,
       "driversModulePendingErrorsEntry": driversModulePendingErrorsEntry,
       "driverModuleErrorType": driverModuleErrorType,
       "driverModuleErrorReflectedStatus": driverModuleErrorReflectedStatus,
       "driverIdInDriverModulesErrors": driverIdInDriverModulesErrors,
       "moduleIdInModulesErrors": moduleIdInModulesErrors,
       "driverModuleErrorIndex": driverModuleErrorIndex,
       "driversSnmpAgentConfig": driversSnmpAgentConfig,
       "driversAgentIsRepeatingTraps": driversAgentIsRepeatingTraps,
       "driversAgentTrapsRepeatInterval": driversAgentTrapsRepeatInterval,
       "driversAgentVersion": driversAgentVersion,
       "applicationsServer": applicationsServer,
       "applicationsTable": applicationsTable,
       "appsServerIsDown": appsServerIsDown,
       "appsServerIsUp": appsServerIsUp,
       "appsSystemAdminHostConnectionIsDown": appsSystemAdminHostConnectionIsDown,
       "appsSystemAdminHostConnectionIsUp": appsSystemAdminHostConnectionIsUp,
       "appsAdminDataBaseConnectionIsDown": appsAdminDataBaseConnectionIsDown,
       "appsAdminDataBaseConnectionIsUp": appsAdminDataBaseConnectionIsUp,
       "appsLoggerIsNotAttachToACLS": appsLoggerIsNotAttachToACLS,
       "appsCLSConnectionIsDown": appsCLSConnectionIsDown,
       "appsCLSConnectionIsUp": appsCLSConnectionIsUp,
       "appsLoggerConnectionIsDown": appsLoggerConnectionIsDown,
       "appsLoggerConnectionIsUp": appsLoggerConnectionIsUp,
       "appsSCConnectionIsDown": appsSCConnectionIsDown,
       "appsSCConnectionIsUp": appsSCConnectionIsUp,
       "appsCTIDBConnectionIsDown": appsCTIDBConnectionIsDown,
       "appsCTIDBConnectionIsUp": appsCTIDBConnectionIsUp,
       "appsCADBConnectionIsDown": appsCADBConnectionIsDown,
       "appsCADBConnectionIsUp": appsCADBConnectionIsUp,
       "appsNIFDBConnectionIsDown": appsNIFDBConnectionIsDown,
       "appsNIFDBConnectionIsUp": appsNIFDBConnectionIsUp,
       "appsInteractionDBConnectionIsDown": appsInteractionDBConnectionIsDown,
       "appsInteractionDBConnectionIsUp": appsInteractionDBConnectionIsUp,
       "appsUserAdminHostConnectionIsDown": appsUserAdminHostConnectionIsDown,
       "appsUserAdminHostConnectionIsUp": appsUserAdminHostConnectionIsUp,
       "appsRuleEngineEventProviderFailed": appsRuleEngineEventProviderFailed,
       "appsRuleEngineEventProviderSucceeded": appsRuleEngineEventProviderSucceeded,
       "appsRuleEngineEventProviderIdle": appsRuleEngineEventProviderIdle,
       "appsRuleEngineEventProviderActive": appsRuleEngineEventProviderActive,
       "appsRuleEngineRuleGeneratorFailed": appsRuleEngineRuleGeneratorFailed,
       "appsRuleEngineRuleGeneratorSucceeded": appsRuleEngineRuleGeneratorSucceeded,
       "appsRuleEngineRuleGeneratorIdle": appsRuleEngineRuleGeneratorIdle,
       "appsRuleEngineRuleGeneratorActive": appsRuleEngineRuleGeneratorActive,
       "appsRuleEngineActionExecuterFailed": appsRuleEngineActionExecuterFailed,
       "appsRuleEngineActionExecuterSucceeded": appsRuleEngineActionExecuterSucceeded,
       "appsRuleEngineActionExecuterIdle": appsRuleEngineActionExecuterIdle,
       "appsRuleEngineActionExecuterActive": appsRuleEngineActionExecuterActive,
       "appsRuleMngrDataBaseConnectionIsDown": appsRuleMngrDataBaseConnectionIsDown,
       "appsRuleMngrDataBaseConnectionIsUp": appsRuleMngrDataBaseConnectionIsUp,
       "applicationsEntry": applicationsEntry,
       "applicationName": applicationName,
       "applicationStatus": applicationStatus,
       "applicationsTableIndex": applicationsTableIndex,
       "applicationsPendingErrorsTable": applicationsPendingErrorsTable,
       "applicationsPendingErrorsEntry": applicationsPendingErrorsEntry,
       "applicationErrorType": applicationErrorType,
       "applicationErrorReflectedStatus": applicationErrorReflectedStatus,
       "applicationsErrorsTableApplicationIndex": applicationsErrorsTableApplicationIndex,
       "applicationsErrorsTableErrorIndex": applicationsErrorsTableErrorIndex,
       "applicationsNumberLoggedInUsers": applicationsNumberLoggedInUsers,
       "applicationsSnmpAgentConfig": applicationsSnmpAgentConfig,
       "applicationsAgentIsRepeatingTraps": applicationsAgentIsRepeatingTraps,
       "applicationsAgentTrapsRepeatInterval": applicationsAgentTrapsRepeatInterval,
       "applicationsAgentVersion": applicationsAgentVersion,
       "storageCenter": storageCenter,
       "systemTools": systemTools,
       "recordingsDiagnostic": recordingsDiagnostic,
       "rdExceptionWhileProcessing": rdExceptionWhileProcessing,
       "rdApplicationFailedToInitialize": rdApplicationFailedToInitialize,
       "rdApplicationStartUp": rdApplicationStartUp,
       "rdKeepAliveHeartBeatFail": rdKeepAliveHeartBeatFail,
       "rdConnectionToCLSIsActive": rdConnectionToCLSIsActive,
       "rdConnectionToCLSIsNotActive": rdConnectionToCLSIsNotActive,
       "rdConnectionToCLSLost": rdConnectionToCLSLost,
       "rdConnectionToLoggerIsActive": rdConnectionToLoggerIsActive,
       "rdConnectionToLoggerIsNotActive": rdConnectionToLoggerIsNotActive,
       "rdConnectionToLoggerLost": rdConnectionToLoggerLost,
       "rdTaskStarted": rdTaskStarted,
       "rdTaskCompleted": rdTaskCompleted,
       "rdMatchingSessionFailed": rdMatchingSessionFailed,
       "rdMatchingPerdiodFailed": rdMatchingPerdiodFailed,
       "rdCLSGeneralError": rdCLSGeneralError,
       "rdName": rdName,
       "rdStatus": rdStatus,
       "rdVersion": rdVersion,
       "rdServerName": rdServerName,
       "rdServerAddress": rdServerAddress,
       "rdCLSConnectionTable": rdCLSConnectionTable,
       "rdCLSConnectionEntry": rdCLSConnectionEntry,
       "rdCLSID": rdCLSID,
       "rdCLSIpAddress": rdCLSIpAddress,
       "rdCLSConnectionTableIndex": rdCLSConnectionTableIndex,
       "rdLoggerConnectionTable": rdLoggerConnectionTable,
       "rdLoggerConnectionEntry": rdLoggerConnectionEntry,
       "rdLoggerID": rdLoggerID,
       "rdLoggerIpAddress": rdLoggerIpAddress,
       "rdLoggerSpareloggerID": rdLoggerSpareloggerID,
       "rdLoggerConnectionTableIndex": rdLoggerConnectionTableIndex,
       "rdTasksTable": rdTasksTable,
       "rdTasksEntry": rdTasksEntry,
       "rdTaskType": rdTaskType,
       "rdTaskName": rdTaskName,
       "rdTaskDescription": rdTaskDescription,
       "rdTaskCreationTime": rdTaskCreationTime,
       "rdTaskStartTime": rdTaskStartTime,
       "rdTaskQuery": rdTaskQuery,
       "rdTaskExecElements": rdTaskExecElements,
       "rdTaskExecFailElements": rdTaskExecFailElements,
       "rdTaskCurrentState": rdTaskCurrentState,
       "rdTaskLastError": rdTaskLastError,
       "rdTasksTableIndex": rdTasksTableIndex,
       "rdCLSPendingErrorsTable": rdCLSPendingErrorsTable,
       "rdCLSPendingErrorsEntry": rdCLSPendingErrorsEntry,
       "rdCLSErrorType": rdCLSErrorType,
       "rdCLSErrorReflectedStatus": rdCLSErrorReflectedStatus,
       "rdCLSExtendedErrorinformation": rdCLSExtendedErrorinformation,
       "rdCLSErrorCLSTableIndex": rdCLSErrorCLSTableIndex,
       "rdCLSPendingErrorsTableIndex": rdCLSPendingErrorsTableIndex,
       "rdLoggerPendingErrorsTable": rdLoggerPendingErrorsTable,
       "rdLoggerPendingErrorsEntry": rdLoggerPendingErrorsEntry,
       "rdLoggerErrorType": rdLoggerErrorType,
       "rdLoggerErrorReflectedStatus": rdLoggerErrorReflectedStatus,
       "rdLoggerExtendedErrorinformation": rdLoggerExtendedErrorinformation,
       "rdLoggerErrorLoggerTableIndex": rdLoggerErrorLoggerTableIndex,
       "rdLoggerPendingErrorsTableIndex": rdLoggerPendingErrorsTableIndex,
       "databaseUtilities": databaseUtilities,
       "dbCallsBackupFinished": dbCallsBackupFinished,
       "dbCallsBackupFailed": dbCallsBackupFailed,
       "dbAdminBackupFinished": dbAdminBackupFinished,
       "dbAdminBackupFailed": dbAdminBackupFailed,
       "dbAuditBackupFinished": dbAuditBackupFinished,
       "dbAuditBackupFailed": dbAuditBackupFailed,
       "dbReindexJobFinished": dbReindexJobFinished,
       "dbReindexJobFailed": dbReindexJobFailed,
       "dbAuditAutoDeletionFinished": dbAuditAutoDeletionFinished,
       "dbAuditAutoDeletionFailed": dbAuditAutoDeletionFailed,
       "dbCallsDbSpaceIsLow": dbCallsDbSpaceIsLow,
       "dbCallsDbFull": dbCallsDbFull,
       "dbAuditDbSpaceIsLow": dbAuditDbSpaceIsLow,
       "dbAuditDbFull": dbAuditDbFull,
       "dbAdminDbSpaceIsLow": dbAdminDbSpaceIsLow,
       "dbAdminDbFull": dbAdminDbFull,
       "dbInserterMissingCalls": dbInserterMissingCalls,
       "dbReplicationFailed": dbReplicationFailed,
       "dbRuleBackupFinished": dbRuleBackupFinished,
       "dbRuleBackupFailed": dbRuleBackupFailed,
       "dbMsdbBackupFinished": dbMsdbBackupFinished,
       "dbMsdbBackupFailed": dbMsdbBackupFailed,
       "dbMasterBackupFinished": dbMasterBackupFinished,
       "dbMasterBackupFailed": dbMasterBackupFailed,
       "dbRuleDBFull": dbRuleDBFull,
       "dbRuleDBSpaceIsLow": dbRuleDBSpaceIsLow,
       "ctiEventsDbServer": ctiEventsDbServer,
       "ctiDBServerIsUp": ctiDBServerIsUp,
       "ctiDBServerIsDown": ctiDBServerIsDown,
       "ctiDBServerIsNotInitializedProperly": ctiDBServerIsNotInitializedProperly,
       "ctiDBServerIsInitializedProperly": ctiDBServerIsInitializedProperly,
       "ctiDBSpaceIsFull": ctiDBSpaceIsFull,
       "ctiDBSpaceIsOK": ctiDBSpaceIsOK,
       "ctiDBLogSpaceIsFull": ctiDBLogSpaceIsFull,
       "ctiDBLogSpaceIsOK": ctiDBLogSpaceIsOK,
       "ctiConnectionToDBIsOK": ctiConnectionToDBIsOK,
       "ctiFailedConnectToDB": ctiFailedConnectToDB,
       "ctiMissingLookUpTable": ctiMissingLookUpTable,
       "ctiFailedToInsertCTIEvent": ctiFailedToInsertCTIEvent,
       "ctiDBRetentionFailure": ctiDBRetentionFailure,
       "ctiInvalidMessageReceived": ctiInvalidMessageReceived,
       "ctiDBServerName": ctiDBServerName,
       "ctiDBServerStatus": ctiDBServerStatus,
       "ctiDBServerPendingErrorsTable": ctiDBServerPendingErrorsTable,
       "ctiDBServerPendingErrorsEntry": ctiDBServerPendingErrorsEntry,
       "ctiDBServerErrorType": ctiDBServerErrorType,
       "ctiDBServerErrorReflectedStatus": ctiDBServerErrorReflectedStatus,
       "ctiDBServerDBErrorCode": ctiDBServerDBErrorCode,
       "ctiDBServerErrorIndex": ctiDBServerErrorIndex,
       "ctiDBServerSnmpAgentConfig": ctiDBServerSnmpAgentConfig,
       "ctiDBServerAgentIsRepeatingTraps": ctiDBServerAgentIsRepeatingTraps,
       "ctiDBServerAgentTrapsRepeatInterval": ctiDBServerAgentTrapsRepeatInterval,
       "ctiDBServerAgentVersion": ctiDBServerAgentVersion}
)
