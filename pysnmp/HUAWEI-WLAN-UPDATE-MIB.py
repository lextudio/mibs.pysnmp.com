# SNMP MIB module (HUAWEI-WLAN-UPDATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-UPDATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:45 2024
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

(hwApIndex,
 hwApMac,
 hwApRegionIndex,
 hwApType) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-DEVICE-MIB",
    "hwApIndex",
    "hwApMac",
    "hwApRegionIndex",
    "hwApType")

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwWlanUpdate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7)
)
hwWlanUpdate.setRevisions(
        ("2014-11-27 10:00",
         "2013-10-23 15:00",
         "2010-06-08 00:00",
         "2010-11-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwWlanUpdateNotifications_ObjectIdentity = ObjectIdentity
hwWlanUpdateNotifications = _HwWlanUpdateNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 1)
)
_HwWlanUpdateNotifyObjects_ObjectIdentity = ObjectIdentity
hwWlanUpdateNotifyObjects = _HwWlanUpdateNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 2)
)


class _HwApUpdateResult_Type(Integer32):
    """Custom type hwApUpdateResult based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("failureCommunicationFaultApAndAc", 11),
          ("failureDownloadFileFailure", 4),
          ("failureFileContentError", 8),
          ("failureInsufficientMemory", 3),
          ("failureInvalidFileName", 6),
          ("failureMismatchApTypeInEfs", 7),
          ("failureMismatchVersionEfsAndFileName", 5),
          ("failureTimeoutForUpgrade", 10),
          ("failureUnknownError", 2),
          ("failureWriteFlashFailure", 9),
          ("success", 1))
    )


_HwApUpdateResult_Type.__name__ = "Integer32"
_HwApUpdateResult_Object = MibScalar
hwApUpdateResult = _HwApUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 2, 1),
    _HwApUpdateResult_Type()
)
hwApUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateResult.setStatus("current")
_HwApUpdateTime_Type = OctetString
_HwApUpdateTime_Object = MibScalar
hwApUpdateTime = _HwApUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 2, 2),
    _HwApUpdateTime_Type()
)
hwApUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateTime.setStatus("current")
_HwApUpdateByFileName_Type = OctetString
_HwApUpdateByFileName_Object = MibScalar
hwApUpdateByFileName = _HwApUpdateByFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 2, 3),
    _HwApUpdateByFileName_Type()
)
hwApUpdateByFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateByFileName.setStatus("current")


class _HwApUpdateNextOper_Type(Integer32):
    """Custom type hwApUpdateNextOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReset", 1),
          ("reset", 2))
    )


_HwApUpdateNextOper_Type.__name__ = "Integer32"
_HwApUpdateNextOper_Object = MibScalar
hwApUpdateNextOper = _HwApUpdateNextOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 2, 4),
    _HwApUpdateNextOper_Type()
)
hwApUpdateNextOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateNextOper.setStatus("current")
_HwApUpdateResultStatus_Type = OctetString
_HwApUpdateResultStatus_Object = MibScalar
hwApUpdateResultStatus = _HwApUpdateResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 2, 5),
    _HwApUpdateResultStatus_Type()
)
hwApUpdateResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateResultStatus.setStatus("current")
_HwApUpdateObjects_ObjectIdentity = ObjectIdentity
hwApUpdateObjects = _HwApUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3)
)
_HwApUpdateConfig_ObjectIdentity = ObjectIdentity
hwApUpdateConfig = _HwApUpdateConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1)
)
_HwApUpdateFTPIPAddress_Type = IpAddress
_HwApUpdateFTPIPAddress_Object = MibScalar
hwApUpdateFTPIPAddress = _HwApUpdateFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 1),
    _HwApUpdateFTPIPAddress_Type()
)
hwApUpdateFTPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateFTPIPAddress.setStatus("current")
_HwApUpdateFTPUsername_Type = OctetString
_HwApUpdateFTPUsername_Object = MibScalar
hwApUpdateFTPUsername = _HwApUpdateFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 2),
    _HwApUpdateFTPUsername_Type()
)
hwApUpdateFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateFTPUsername.setStatus("current")
_HwApUpdateFTPPassword_Type = OctetString
_HwApUpdateFTPPassword_Object = MibScalar
hwApUpdateFTPPassword = _HwApUpdateFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 3),
    _HwApUpdateFTPPassword_Type()
)
hwApUpdateFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateFTPPassword.setStatus("current")


class _HwApUpdateMode_Type(Integer32):
    """Custom type hwApUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("ftp", 1),
          ("sftp", 3))
    )


_HwApUpdateMode_Type.__name__ = "Integer32"
_HwApUpdateMode_Object = MibScalar
hwApUpdateMode = _HwApUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 4),
    _HwApUpdateMode_Type()
)
hwApUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateMode.setStatus("current")
_HwApUpdateSFTPIPAddress_Type = IpAddress
_HwApUpdateSFTPIPAddress_Object = MibScalar
hwApUpdateSFTPIPAddress = _HwApUpdateSFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 5),
    _HwApUpdateSFTPIPAddress_Type()
)
hwApUpdateSFTPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateSFTPIPAddress.setStatus("current")
_HwApUpdateSFTPUsername_Type = OctetString
_HwApUpdateSFTPUsername_Object = MibScalar
hwApUpdateSFTPUsername = _HwApUpdateSFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 6),
    _HwApUpdateSFTPUsername_Type()
)
hwApUpdateSFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateSFTPUsername.setStatus("current")
_HwApUpdateSFTPPassword_Type = OctetString
_HwApUpdateSFTPPassword_Object = MibScalar
hwApUpdateSFTPPassword = _HwApUpdateSFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 7),
    _HwApUpdateSFTPPassword_Type()
)
hwApUpdateSFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateSFTPPassword.setStatus("current")
_HwApUpdateFTPMaxConnectNum_Type = Integer32
_HwApUpdateFTPMaxConnectNum_Object = MibScalar
hwApUpdateFTPMaxConnectNum = _HwApUpdateFTPMaxConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 8),
    _HwApUpdateFTPMaxConnectNum_Type()
)
hwApUpdateFTPMaxConnectNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateFTPMaxConnectNum.setStatus("current")
_HwApUpdateSFTPMaxConnectNum_Type = Integer32
_HwApUpdateSFTPMaxConnectNum_Object = MibScalar
hwApUpdateSFTPMaxConnectNum = _HwApUpdateSFTPMaxConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 9),
    _HwApUpdateSFTPMaxConnectNum_Type()
)
hwApUpdateSFTPMaxConnectNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateSFTPMaxConnectNum.setStatus("current")


class _HwApUpdateFTPIPv6Address_Type(OctetString):
    """Custom type hwApUpdateFTPIPv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApUpdateFTPIPv6Address_Type.__name__ = "OctetString"
_HwApUpdateFTPIPv6Address_Object = MibScalar
hwApUpdateFTPIPv6Address = _HwApUpdateFTPIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 10),
    _HwApUpdateFTPIPv6Address_Type()
)
hwApUpdateFTPIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateFTPIPv6Address.setStatus("current")


class _HwApUpdateSFTPIPv6Address_Type(OctetString):
    """Custom type hwApUpdateSFTPIPv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApUpdateSFTPIPv6Address_Type.__name__ = "OctetString"
_HwApUpdateSFTPIPv6Address_Object = MibScalar
hwApUpdateSFTPIPv6Address = _HwApUpdateSFTPIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 1, 11),
    _HwApUpdateSFTPIPv6Address_Type()
)
hwApUpdateSFTPIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateSFTPIPv6Address.setStatus("current")
_HwApUpdateTable_Object = MibTable
hwApUpdateTable = _HwApUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2)
)
if mibBuilder.loadTexts:
    hwApUpdateTable.setStatus("current")
_HwApUpdateEntry_Object = MibTableRow
hwApUpdateEntry = _HwApUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1)
)
hwApUpdateEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
)
if mibBuilder.loadTexts:
    hwApUpdateEntry.setStatus("current")
_HwApUpdateFilename_Type = OctetString
_HwApUpdateFilename_Object = MibTableColumn
hwApUpdateFilename = _HwApUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 1),
    _HwApUpdateFilename_Type()
)
hwApUpdateFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApUpdateFilename.setStatus("current")
_HwApUpdateResultMask_Type = OctetString
_HwApUpdateResultMask_Object = MibTableColumn
hwApUpdateResultMask = _HwApUpdateResultMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 2),
    _HwApUpdateResultMask_Type()
)
hwApUpdateResultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateResultMask.setStatus("current")


class _HwApUpdateAdminOper_Type(Integer32):
    """Custom type hwApUpdateAdminOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("reset", 2),
          ("start", 1))
    )


_HwApUpdateAdminOper_Type.__name__ = "Integer32"
_HwApUpdateAdminOper_Object = MibTableColumn
hwApUpdateAdminOper = _HwApUpdateAdminOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 3),
    _HwApUpdateAdminOper_Type()
)
hwApUpdateAdminOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApUpdateAdminOper.setStatus("current")
_HwApUpdatePercent_Type = Integer32
_HwApUpdatePercent_Object = MibTableColumn
hwApUpdatePercent = _HwApUpdatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 4),
    _HwApUpdatePercent_Type()
)
hwApUpdatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdatePercent.setStatus("current")
_HwApUpdateRowStatus_Type = RowStatus
_HwApUpdateRowStatus_Object = MibTableColumn
hwApUpdateRowStatus = _HwApUpdateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 5),
    _HwApUpdateRowStatus_Type()
)
hwApUpdateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApUpdateRowStatus.setStatus("current")
_HwApUpdateResultInfo_Type = OctetString
_HwApUpdateResultInfo_Object = MibTableColumn
hwApUpdateResultInfo = _HwApUpdateResultInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 6),
    _HwApUpdateResultInfo_Type()
)
hwApUpdateResultInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateResultInfo.setStatus("current")
_HwApUpdateApIdSetMask_Type = OctetString
_HwApUpdateApIdSetMask_Object = MibTableColumn
hwApUpdateApIdSetMask = _HwApUpdateApIdSetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 2, 1, 7),
    _HwApUpdateApIdSetMask_Type()
)
hwApUpdateApIdSetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUpdateApIdSetMask.setStatus("current")
_HwApUpdateProgressTable_Object = MibTable
hwApUpdateProgressTable = _HwApUpdateProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 3)
)
if mibBuilder.loadTexts:
    hwApUpdateProgressTable.setStatus("current")
_HwApUpdateProgressEntry_Object = MibTableRow
hwApUpdateProgressEntry = _HwApUpdateProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 3, 1)
)
hwApUpdateProgressEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
)
if mibBuilder.loadTexts:
    hwApUpdateProgressEntry.setStatus("current")


class _HwApUpdateProgressStatus_Type(Integer32):
    """Custom type hwApUpdateProgressStatus based on Integer32"""
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
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("apAcLinkDown", 11),
          ("blockFull", 27),
          ("efsAndApTypeMismatched", 7),
          ("efsAndVersionMismatched", 5),
          ("failToDownloadFile", 4),
          ("fileContentError", 8),
          ("fileLoading", 22),
          ("getFtpInfoFailed", 25),
          ("getSftpInfoFailed", 26),
          ("identifierErr", 23),
          ("insufficientApMemory", 3),
          ("invalidFileName", 6),
          ("modeChanged", 33),
          ("neitherNeedUpdateNorReset", 21),
          ("noNeedToUpdate", 12),
          ("noNeedUpdateNeedReset", 20),
          ("noResult", 18),
          ("noUpdateResult", -1),
          ("normalToStandby", 32),
          ("notInConfig", 24),
          ("readFileFailed", 31),
          ("receiveFileFailed", 15),
          ("retransferFileFailed", 16),
          ("sendFirstFileFailed", 14),
          ("succeedNeedReset", 34),
          ("updateCancel", 13),
          ("updateFailed", 2),
          ("updateOverMaxTime", 17),
          ("updateSuccessful", 1),
          ("updateTimeout", 10),
          ("updating", 0),
          ("waitForNextBatch", 19),
          ("writingMemoryError", 9))
    )


_HwApUpdateProgressStatus_Type.__name__ = "Integer32"
_HwApUpdateProgressStatus_Object = MibTableColumn
hwApUpdateProgressStatus = _HwApUpdateProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 3, 1, 1),
    _HwApUpdateProgressStatus_Type()
)
hwApUpdateProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateProgressStatus.setStatus("current")
_HwApUpdateProgress_Type = Integer32
_HwApUpdateProgress_Object = MibTableColumn
hwApUpdateProgress = _HwApUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 3, 1, 2),
    _HwApUpdateProgress_Type()
)
hwApUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpdateProgress.setStatus("current")
_HwApFlashProgress_Type = Integer32
_HwApFlashProgress_Object = MibTableColumn
hwApFlashProgress = _HwApFlashProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 3, 1, 3),
    _HwApFlashProgress_Type()
)
hwApFlashProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApFlashProgress.setStatus("current")
_HwMacApUpdateProgressTable_Object = MibTable
hwMacApUpdateProgressTable = _HwMacApUpdateProgressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 4)
)
if mibBuilder.loadTexts:
    hwMacApUpdateProgressTable.setStatus("current")
_HwMacApUpdateProgressEntry_Object = MibTableRow
hwMacApUpdateProgressEntry = _HwMacApUpdateProgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 4, 1)
)
hwMacApUpdateProgressEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
)
if mibBuilder.loadTexts:
    hwMacApUpdateProgressEntry.setStatus("current")


class _HwMacApUpdateProgressStatus_Type(Integer32):
    """Custom type hwMacApUpdateProgressStatus based on Integer32"""
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
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("apAcLinkDown", 11),
          ("blockFull", 27),
          ("efsAndApTypeMismatched", 7),
          ("efsAndVersionMismatched", 5),
          ("failToDownloadFile", 4),
          ("fileContentError", 8),
          ("fileLoading", 22),
          ("getFtpInfoFailed", 25),
          ("getSftpInfoFailed", 26),
          ("identifierErr", 23),
          ("insufficientApMemory", 3),
          ("invalidFileName", 6),
          ("modeChanged", 33),
          ("neitherNeedUpdateNorReset", 21),
          ("noNeedToUpdate", 12),
          ("noNeedUpdateNeedReset", 20),
          ("noResult", 18),
          ("noUpdateResult", -1),
          ("normalToStandby", 32),
          ("notInConfig", 24),
          ("readFileFailed", 31),
          ("receiveFileFailed", 15),
          ("retransferFileFailed", 16),
          ("sendFirstFileFailed", 14),
          ("succeedNeedReset", 34),
          ("updateCancel", 13),
          ("updateFailed", 2),
          ("updateOverMaxTime", 17),
          ("updateSuccessful", 1),
          ("updateTimeout", 10),
          ("updating", 0),
          ("waitForNextBatch", 19),
          ("writingMemoryError", 9))
    )


_HwMacApUpdateProgressStatus_Type.__name__ = "Integer32"
_HwMacApUpdateProgressStatus_Object = MibTableColumn
hwMacApUpdateProgressStatus = _HwMacApUpdateProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 4, 1, 1),
    _HwMacApUpdateProgressStatus_Type()
)
hwMacApUpdateProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpdateProgressStatus.setStatus("current")
_HwMacApUpdateProgress_Type = Integer32
_HwMacApUpdateProgress_Object = MibTableColumn
hwMacApUpdateProgress = _HwMacApUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 4, 1, 2),
    _HwMacApUpdateProgress_Type()
)
hwMacApUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpdateProgress.setStatus("current")
_HwMacApFlashProgress_Type = Integer32
_HwMacApFlashProgress_Object = MibTableColumn
hwMacApFlashProgress = _HwMacApFlashProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 4, 1, 3),
    _HwMacApFlashProgress_Type()
)
hwMacApFlashProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApFlashProgress.setStatus("current")
_HwSingleApUpdateTable_Object = MibTable
hwSingleApUpdateTable = _HwSingleApUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 5)
)
if mibBuilder.loadTexts:
    hwSingleApUpdateTable.setStatus("current")
_HwSingleApUpdateEntry_Object = MibTableRow
hwSingleApUpdateEntry = _HwSingleApUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 5, 1)
)
hwSingleApUpdateEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
)
if mibBuilder.loadTexts:
    hwSingleApUpdateEntry.setStatus("current")


class _HwSingleApUpdateAdminOper_Type(Integer32):
    """Custom type hwSingleApUpdateAdminOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("reset", 2),
          ("start", 1))
    )


_HwSingleApUpdateAdminOper_Type.__name__ = "Integer32"
_HwSingleApUpdateAdminOper_Object = MibTableColumn
hwSingleApUpdateAdminOper = _HwSingleApUpdateAdminOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 5, 1, 1),
    _HwSingleApUpdateAdminOper_Type()
)
hwSingleApUpdateAdminOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSingleApUpdateAdminOper.setStatus("current")
_HwSingleApUpdatePercent_Type = Integer32
_HwSingleApUpdatePercent_Object = MibTableColumn
hwSingleApUpdatePercent = _HwSingleApUpdatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 5, 1, 2),
    _HwSingleApUpdatePercent_Type()
)
hwSingleApUpdatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSingleApUpdatePercent.setStatus("current")


class _HwSingleApUpdateResult_Type(Integer32):
    """Custom type hwSingleApUpdateResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("success", 0))
    )


_HwSingleApUpdateResult_Type.__name__ = "Integer32"
_HwSingleApUpdateResult_Object = MibTableColumn
hwSingleApUpdateResult = _HwSingleApUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 5, 1, 3),
    _HwSingleApUpdateResult_Type()
)
hwSingleApUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSingleApUpdateResult.setStatus("current")
_HwSingleApUpdateFilename_Type = OctetString
_HwSingleApUpdateFilename_Object = MibTableColumn
hwSingleApUpdateFilename = _HwSingleApUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 5, 1, 4),
    _HwSingleApUpdateFilename_Type()
)
hwSingleApUpdateFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSingleApUpdateFilename.setStatus("current")
_HwMacSingleApUpdateTable_Object = MibTable
hwMacSingleApUpdateTable = _HwMacSingleApUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 6)
)
if mibBuilder.loadTexts:
    hwMacSingleApUpdateTable.setStatus("current")
_HwMacSingleApUpdateEntry_Object = MibTableRow
hwMacSingleApUpdateEntry = _HwMacSingleApUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 6, 1)
)
hwMacSingleApUpdateEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
)
if mibBuilder.loadTexts:
    hwMacSingleApUpdateEntry.setStatus("current")


class _HwMacSingleApUpdateAdminOper_Type(Integer32):
    """Custom type hwMacSingleApUpdateAdminOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("reset", 2),
          ("start", 1))
    )


_HwMacSingleApUpdateAdminOper_Type.__name__ = "Integer32"
_HwMacSingleApUpdateAdminOper_Object = MibTableColumn
hwMacSingleApUpdateAdminOper = _HwMacSingleApUpdateAdminOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 6, 1, 1),
    _HwMacSingleApUpdateAdminOper_Type()
)
hwMacSingleApUpdateAdminOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacSingleApUpdateAdminOper.setStatus("current")
_HwMacSingleApUpdatePercent_Type = Integer32
_HwMacSingleApUpdatePercent_Object = MibTableColumn
hwMacSingleApUpdatePercent = _HwMacSingleApUpdatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 6, 1, 2),
    _HwMacSingleApUpdatePercent_Type()
)
hwMacSingleApUpdatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSingleApUpdatePercent.setStatus("current")


class _HwMacSingleApUpdateResult_Type(Integer32):
    """Custom type hwMacSingleApUpdateResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("success", 0))
    )


_HwMacSingleApUpdateResult_Type.__name__ = "Integer32"
_HwMacSingleApUpdateResult_Object = MibTableColumn
hwMacSingleApUpdateResult = _HwMacSingleApUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 6, 1, 3),
    _HwMacSingleApUpdateResult_Type()
)
hwMacSingleApUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSingleApUpdateResult.setStatus("current")
_HwMacSingleApUpdateFilename_Type = OctetString
_HwMacSingleApUpdateFilename_Object = MibTableColumn
hwMacSingleApUpdateFilename = _HwMacSingleApUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 6, 1, 4),
    _HwMacSingleApUpdateFilename_Type()
)
hwMacSingleApUpdateFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacSingleApUpdateFilename.setStatus("current")
_HwApTypeRegionUpdateTable_Object = MibTable
hwApTypeRegionUpdateTable = _HwApTypeRegionUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7)
)
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateTable.setStatus("current")
_HwApTypeRegionUpdateEntry_Object = MibTableRow
hwApTypeRegionUpdateEntry = _HwApTypeRegionUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1)
)
hwApTypeRegionUpdateEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApRegionIndex"),
)
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateEntry.setStatus("current")
_HwApTypeRegionUpdateFilename_Type = OctetString
_HwApTypeRegionUpdateFilename_Object = MibTableColumn
hwApTypeRegionUpdateFilename = _HwApTypeRegionUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1, 1),
    _HwApTypeRegionUpdateFilename_Type()
)
hwApTypeRegionUpdateFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateFilename.setStatus("current")
_HwApTypeRegionUpdateResultMask_Type = OctetString
_HwApTypeRegionUpdateResultMask_Object = MibTableColumn
hwApTypeRegionUpdateResultMask = _HwApTypeRegionUpdateResultMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1, 2),
    _HwApTypeRegionUpdateResultMask_Type()
)
hwApTypeRegionUpdateResultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateResultMask.setStatus("current")


class _HwApTypeRegionUpdateAdminOper_Type(Integer32):
    """Custom type hwApTypeRegionUpdateAdminOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("reset", 2),
          ("start", 1))
    )


_HwApTypeRegionUpdateAdminOper_Type.__name__ = "Integer32"
_HwApTypeRegionUpdateAdminOper_Object = MibTableColumn
hwApTypeRegionUpdateAdminOper = _HwApTypeRegionUpdateAdminOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1, 3),
    _HwApTypeRegionUpdateAdminOper_Type()
)
hwApTypeRegionUpdateAdminOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateAdminOper.setStatus("current")
_HwApTypeRegionUpdatePercent_Type = Integer32
_HwApTypeRegionUpdatePercent_Object = MibTableColumn
hwApTypeRegionUpdatePercent = _HwApTypeRegionUpdatePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1, 4),
    _HwApTypeRegionUpdatePercent_Type()
)
hwApTypeRegionUpdatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApTypeRegionUpdatePercent.setStatus("current")
_HwApTypeRegionUpdateRowStatus_Type = RowStatus
_HwApTypeRegionUpdateRowStatus_Object = MibTableColumn
hwApTypeRegionUpdateRowStatus = _HwApTypeRegionUpdateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1, 5),
    _HwApTypeRegionUpdateRowStatus_Type()
)
hwApTypeRegionUpdateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateRowStatus.setStatus("current")
_HwApTypeRegionUpdateResultInfo_Type = OctetString
_HwApTypeRegionUpdateResultInfo_Object = MibTableColumn
hwApTypeRegionUpdateResultInfo = _HwApTypeRegionUpdateResultInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 3, 7, 1, 6),
    _HwApTypeRegionUpdateResultInfo_Type()
)
hwApTypeRegionUpdateResultInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApTypeRegionUpdateResultInfo.setStatus("current")
_HwWlanUpdateObjects_ObjectIdentity = ObjectIdentity
hwWlanUpdateObjects = _HwWlanUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 4)
)
_HwWlanUpdateConformance_ObjectIdentity = ObjectIdentity
hwWlanUpdateConformance = _HwWlanUpdateConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5)
)
_HwWlanUpdateCompliances_ObjectIdentity = ObjectIdentity
hwWlanUpdateCompliances = _HwWlanUpdateCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5, 1)
)
_HwWlanUpdateObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanUpdateObjectGroups = _HwWlanUpdateObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5, 2)
)

# Managed Objects groups

hwWlanUpdateNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5, 2, 2)
)
hwWlanUpdateNotifyObjectsGroup.setObjects(
      *(("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResult"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateTime"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateByFileName"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateNextOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResultStatus"))
)
if mibBuilder.loadTexts:
    hwWlanUpdateNotifyObjectsGroup.setStatus("current")

hwApUpdateObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5, 2, 3)
)
hwApUpdateObjectsGroup.setObjects(
      *(("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateSFTPIPAddress"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateSFTPUsername"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateSFTPPassword"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateFTPMaxConnectNum"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateFTPIPv6Address"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateSFTPIPv6Address"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateSFTPMaxConnectNum"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateFilename"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResultMask"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateAdminOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdatePercent"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateRowStatus"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResultInfo"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApFlashProgress"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacApFlashProgress"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateApIdSetMask"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResult"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateTime"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateByFileName"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateNextOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateFTPIPAddress"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateFTPUsername"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateFTPPassword"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateMode"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateProgressStatus"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateProgress"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacApUpdateProgressStatus"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacApUpdateProgress"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwSingleApUpdateAdminOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwSingleApUpdatePercent"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwSingleApUpdateResult"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwSingleApUpdateFilename"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacSingleApUpdateAdminOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacSingleApUpdatePercent"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacSingleApUpdateResult"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwMacSingleApUpdateFilename"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApTypeRegionUpdateFilename"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApTypeRegionUpdateResultMask"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApTypeRegionUpdateAdminOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApTypeRegionUpdatePercent"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApTypeRegionUpdateRowStatus"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApTypeRegionUpdateResultInfo"))
)
if mibBuilder.loadTexts:
    hwApUpdateObjectsGroup.setStatus("current")


# Notification objects

hwApUpdateBeginNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 1, 1)
)
hwApUpdateBeginNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApUpdateBeginNotify.setStatus(
        "current"
    )

hwApUpdateResultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 1, 2)
)
hwApUpdateResultNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResult"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateTime"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateByFileName"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateNextOper"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResultStatus"))
)
if mibBuilder.loadTexts:
    hwApUpdateResultNotify.setStatus(
        "current"
    )

hwApUpdateUbootNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 1, 3)
)
hwApUpdateUbootNotMatchNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApUpdateUbootNotMatchNotify.setStatus(
        "current"
    )


# Notifications groups

hwWlanUpdateNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5, 2, 1)
)
hwWlanUpdateNotificationsGroup.setObjects(
      *(("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateBeginNotify"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateResultNotify"),
        ("HUAWEI-WLAN-UPDATE-MIB", "hwApUpdateUbootNotMatchNotify"))
)
if mibBuilder.loadTexts:
    hwWlanUpdateNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwWlanUpdateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 7, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanUpdateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-UPDATE-MIB",
    **{"hwWlanUpdate": hwWlanUpdate,
       "hwWlanUpdateNotifications": hwWlanUpdateNotifications,
       "hwApUpdateBeginNotify": hwApUpdateBeginNotify,
       "hwApUpdateResultNotify": hwApUpdateResultNotify,
       "hwApUpdateUbootNotMatchNotify": hwApUpdateUbootNotMatchNotify,
       "hwWlanUpdateNotifyObjects": hwWlanUpdateNotifyObjects,
       "hwApUpdateResult": hwApUpdateResult,
       "hwApUpdateTime": hwApUpdateTime,
       "hwApUpdateByFileName": hwApUpdateByFileName,
       "hwApUpdateNextOper": hwApUpdateNextOper,
       "hwApUpdateResultStatus": hwApUpdateResultStatus,
       "hwApUpdateObjects": hwApUpdateObjects,
       "hwApUpdateConfig": hwApUpdateConfig,
       "hwApUpdateFTPIPAddress": hwApUpdateFTPIPAddress,
       "hwApUpdateFTPUsername": hwApUpdateFTPUsername,
       "hwApUpdateFTPPassword": hwApUpdateFTPPassword,
       "hwApUpdateMode": hwApUpdateMode,
       "hwApUpdateSFTPIPAddress": hwApUpdateSFTPIPAddress,
       "hwApUpdateSFTPUsername": hwApUpdateSFTPUsername,
       "hwApUpdateSFTPPassword": hwApUpdateSFTPPassword,
       "hwApUpdateFTPMaxConnectNum": hwApUpdateFTPMaxConnectNum,
       "hwApUpdateSFTPMaxConnectNum": hwApUpdateSFTPMaxConnectNum,
       "hwApUpdateFTPIPv6Address": hwApUpdateFTPIPv6Address,
       "hwApUpdateSFTPIPv6Address": hwApUpdateSFTPIPv6Address,
       "hwApUpdateTable": hwApUpdateTable,
       "hwApUpdateEntry": hwApUpdateEntry,
       "hwApUpdateFilename": hwApUpdateFilename,
       "hwApUpdateResultMask": hwApUpdateResultMask,
       "hwApUpdateAdminOper": hwApUpdateAdminOper,
       "hwApUpdatePercent": hwApUpdatePercent,
       "hwApUpdateRowStatus": hwApUpdateRowStatus,
       "hwApUpdateResultInfo": hwApUpdateResultInfo,
       "hwApUpdateApIdSetMask": hwApUpdateApIdSetMask,
       "hwApUpdateProgressTable": hwApUpdateProgressTable,
       "hwApUpdateProgressEntry": hwApUpdateProgressEntry,
       "hwApUpdateProgressStatus": hwApUpdateProgressStatus,
       "hwApUpdateProgress": hwApUpdateProgress,
       "hwApFlashProgress": hwApFlashProgress,
       "hwMacApUpdateProgressTable": hwMacApUpdateProgressTable,
       "hwMacApUpdateProgressEntry": hwMacApUpdateProgressEntry,
       "hwMacApUpdateProgressStatus": hwMacApUpdateProgressStatus,
       "hwMacApUpdateProgress": hwMacApUpdateProgress,
       "hwMacApFlashProgress": hwMacApFlashProgress,
       "hwSingleApUpdateTable": hwSingleApUpdateTable,
       "hwSingleApUpdateEntry": hwSingleApUpdateEntry,
       "hwSingleApUpdateAdminOper": hwSingleApUpdateAdminOper,
       "hwSingleApUpdatePercent": hwSingleApUpdatePercent,
       "hwSingleApUpdateResult": hwSingleApUpdateResult,
       "hwSingleApUpdateFilename": hwSingleApUpdateFilename,
       "hwMacSingleApUpdateTable": hwMacSingleApUpdateTable,
       "hwMacSingleApUpdateEntry": hwMacSingleApUpdateEntry,
       "hwMacSingleApUpdateAdminOper": hwMacSingleApUpdateAdminOper,
       "hwMacSingleApUpdatePercent": hwMacSingleApUpdatePercent,
       "hwMacSingleApUpdateResult": hwMacSingleApUpdateResult,
       "hwMacSingleApUpdateFilename": hwMacSingleApUpdateFilename,
       "hwApTypeRegionUpdateTable": hwApTypeRegionUpdateTable,
       "hwApTypeRegionUpdateEntry": hwApTypeRegionUpdateEntry,
       "hwApTypeRegionUpdateFilename": hwApTypeRegionUpdateFilename,
       "hwApTypeRegionUpdateResultMask": hwApTypeRegionUpdateResultMask,
       "hwApTypeRegionUpdateAdminOper": hwApTypeRegionUpdateAdminOper,
       "hwApTypeRegionUpdatePercent": hwApTypeRegionUpdatePercent,
       "hwApTypeRegionUpdateRowStatus": hwApTypeRegionUpdateRowStatus,
       "hwApTypeRegionUpdateResultInfo": hwApTypeRegionUpdateResultInfo,
       "hwWlanUpdateObjects": hwWlanUpdateObjects,
       "hwWlanUpdateConformance": hwWlanUpdateConformance,
       "hwWlanUpdateCompliances": hwWlanUpdateCompliances,
       "hwWlanUpdateCompliance": hwWlanUpdateCompliance,
       "hwWlanUpdateObjectGroups": hwWlanUpdateObjectGroups,
       "hwWlanUpdateNotificationsGroup": hwWlanUpdateNotificationsGroup,
       "hwWlanUpdateNotifyObjectsGroup": hwWlanUpdateNotifyObjectsGroup,
       "hwApUpdateObjectsGroup": hwApUpdateObjectsGroup}
)
