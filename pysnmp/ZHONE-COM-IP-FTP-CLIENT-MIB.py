# SNMP MIB module (ZHONE-COM-IP-FTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-FTP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:14 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneFileName,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneFileName",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpFtpClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 68)
)
comIpFtpClient.setRevisions(
        ("2001-01-11 15:59",
         "2000-09-18 11:13")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FtpClient_ObjectIdentity = ObjectIdentity
ftpClient = _FtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18)
)
if mibBuilder.loadTexts:
    ftpClient.setStatus("current")


class _FtpClientNextIndex_Type(Integer32):
    """Custom type ftpClientNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FtpClientNextIndex_Type.__name__ = "Integer32"
_FtpClientNextIndex_Object = MibScalar
ftpClientNextIndex = _FtpClientNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 1),
    _FtpClientNextIndex_Type()
)
ftpClientNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientNextIndex.setStatus("current")
_FtpClientHighRequests_Type = Integer32
_FtpClientHighRequests_Object = MibScalar
ftpClientHighRequests = _FtpClientHighRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 2),
    _FtpClientHighRequests_Type()
)
ftpClientHighRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientHighRequests.setStatus("current")
_FtpClientAutoRemovals_Type = Integer32
_FtpClientAutoRemovals_Object = MibScalar
ftpClientAutoRemovals = _FtpClientAutoRemovals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 3),
    _FtpClientAutoRemovals_Type()
)
ftpClientAutoRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientAutoRemovals.setStatus("current")
_FtpClientIndexFailures_Type = Integer32
_FtpClientIndexFailures_Object = MibScalar
ftpClientIndexFailures = _FtpClientIndexFailures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 4),
    _FtpClientIndexFailures_Type()
)
ftpClientIndexFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientIndexFailures.setStatus("current")
_FtpClientRequestTable_Object = MibTable
ftpClientRequestTable = _FtpClientRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5)
)
if mibBuilder.loadTexts:
    ftpClientRequestTable.setStatus("current")
_FtpClientRequestEntry_Object = MibTableRow
ftpClientRequestEntry = _FtpClientRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1)
)
ftpClientRequestEntry.setIndexNames(
    (0, "ZHONE-COM-IP-FTP-CLIENT-MIB", "ftpClientRequestIndex"),
)
if mibBuilder.loadTexts:
    ftpClientRequestEntry.setStatus("current")


class _FtpClientRequestIndex_Type(Integer32):
    """Custom type ftpClientRequestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FtpClientRequestIndex_Type.__name__ = "Integer32"
_FtpClientRequestIndex_Object = MibTableColumn
ftpClientRequestIndex = _FtpClientRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 1),
    _FtpClientRequestIndex_Type()
)
ftpClientRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftpClientRequestIndex.setStatus("current")


class _FtpClientRequestCode_Type(Integer32):
    """Custom type ftpClientRequestCode based on Integer32"""
    defaultValue = 1

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
        *(("getAscii", 4),
          ("getBinary", 3),
          ("putAscii", 2),
          ("putBinary", 1))
    )


_FtpClientRequestCode_Type.__name__ = "Integer32"
_FtpClientRequestCode_Object = MibTableColumn
ftpClientRequestCode = _FtpClientRequestCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 2),
    _FtpClientRequestCode_Type()
)
ftpClientRequestCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestCode.setStatus("current")
_FtpClientRequestLocalFileName_Type = ZhoneFileName
_FtpClientRequestLocalFileName_Object = MibTableColumn
ftpClientRequestLocalFileName = _FtpClientRequestLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 3),
    _FtpClientRequestLocalFileName_Type()
)
ftpClientRequestLocalFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestLocalFileName.setStatus("current")
_FtpClientRequestRemoteFileName_Type = ZhoneFileName
_FtpClientRequestRemoteFileName_Object = MibTableColumn
ftpClientRequestRemoteFileName = _FtpClientRequestRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 4),
    _FtpClientRequestRemoteFileName_Type()
)
ftpClientRequestRemoteFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestRemoteFileName.setStatus("current")
_FtpClientRequestServerAddress_Type = ZhoneAdminString
_FtpClientRequestServerAddress_Object = MibTableColumn
ftpClientRequestServerAddress = _FtpClientRequestServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 5),
    _FtpClientRequestServerAddress_Type()
)
ftpClientRequestServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestServerAddress.setStatus("current")
_FtpClientRequestUserName_Type = ZhoneAdminString
_FtpClientRequestUserName_Object = MibTableColumn
ftpClientRequestUserName = _FtpClientRequestUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 6),
    _FtpClientRequestUserName_Type()
)
ftpClientRequestUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestUserName.setStatus("current")
_FtpClientRequestPassword_Type = ZhoneAdminString
_FtpClientRequestPassword_Object = MibTableColumn
ftpClientRequestPassword = _FtpClientRequestPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 7),
    _FtpClientRequestPassword_Type()
)
ftpClientRequestPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestPassword.setStatus("current")


class _FtpClientRequestResult_Type(Integer32):
    """Custom type ftpClientRequestResult based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("invalidUserNamePassword", 7),
          ("localFileNameError", 4),
          ("readError", 9),
          ("remoteFileNameError", 5),
          ("stoppedByUser", 3),
          ("success", 2),
          ("tooManyOpenFiles", 8),
          ("unreachableDestination", 6),
          ("writeError", 10))
    )


_FtpClientRequestResult_Type.__name__ = "Integer32"
_FtpClientRequestResult_Object = MibTableColumn
ftpClientRequestResult = _FtpClientRequestResult_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 8),
    _FtpClientRequestResult_Type()
)
ftpClientRequestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientRequestResult.setStatus("current")


class _FtpClientRequestAction_Type(Integer32):
    """Custom type ftpClientRequestAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_FtpClientRequestAction_Type.__name__ = "Integer32"
_FtpClientRequestAction_Object = MibTableColumn
ftpClientRequestAction = _FtpClientRequestAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 9),
    _FtpClientRequestAction_Type()
)
ftpClientRequestAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestAction.setStatus("current")
_FtpClientRequestCompletionTime_Type = TimeStamp
_FtpClientRequestCompletionTime_Object = MibTableColumn
ftpClientRequestCompletionTime = _FtpClientRequestCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 10),
    _FtpClientRequestCompletionTime_Type()
)
ftpClientRequestCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientRequestCompletionTime.setStatus("current")
_FtpClientRequestRowStatus_Type = ZhoneRowStatus
_FtpClientRequestRowStatus_Object = MibTableColumn
ftpClientRequestRowStatus = _FtpClientRequestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 11),
    _FtpClientRequestRowStatus_Type()
)
ftpClientRequestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftpClientRequestRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-FTP-CLIENT-MIB",
    **{"ftpClient": ftpClient,
       "ftpClientNextIndex": ftpClientNextIndex,
       "ftpClientHighRequests": ftpClientHighRequests,
       "ftpClientAutoRemovals": ftpClientAutoRemovals,
       "ftpClientIndexFailures": ftpClientIndexFailures,
       "ftpClientRequestTable": ftpClientRequestTable,
       "ftpClientRequestEntry": ftpClientRequestEntry,
       "ftpClientRequestIndex": ftpClientRequestIndex,
       "ftpClientRequestCode": ftpClientRequestCode,
       "ftpClientRequestLocalFileName": ftpClientRequestLocalFileName,
       "ftpClientRequestRemoteFileName": ftpClientRequestRemoteFileName,
       "ftpClientRequestServerAddress": ftpClientRequestServerAddress,
       "ftpClientRequestUserName": ftpClientRequestUserName,
       "ftpClientRequestPassword": ftpClientRequestPassword,
       "ftpClientRequestResult": ftpClientRequestResult,
       "ftpClientRequestAction": ftpClientRequestAction,
       "ftpClientRequestCompletionTime": ftpClientRequestCompletionTime,
       "ftpClientRequestRowStatus": ftpClientRequestRowStatus,
       "comIpFtpClient": comIpFtpClient}
)
