# SNMP MIB module (CISCO-FTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FTP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:45 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoFtpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 80)
)
ciscoFtpClientMIB.setRevisions(
        ("2006-03-31 00:00",
         "1997-10-09 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFtpClientMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFtpClientMIBObjects = _CiscoFtpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1)
)
_CfcRequest_ObjectIdentity = ObjectIdentity
cfcRequest = _CfcRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1)
)


class _CfcRequestMaximum_Type(Unsigned32):
    """Custom type cfcRequestMaximum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfcRequestMaximum_Type.__name__ = "Unsigned32"
_CfcRequestMaximum_Object = MibScalar
cfcRequestMaximum = _CfcRequestMaximum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 1),
    _CfcRequestMaximum_Type()
)
cfcRequestMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcRequestMaximum.setStatus("current")
_CfcRequests_Type = Gauge32
_CfcRequests_Object = MibScalar
cfcRequests = _CfcRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 2),
    _CfcRequests_Type()
)
cfcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcRequests.setStatus("current")
_CfcRequestsHigh_Type = Gauge32
_CfcRequestsHigh_Object = MibScalar
cfcRequestsHigh = _CfcRequestsHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 3),
    _CfcRequestsHigh_Type()
)
cfcRequestsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcRequestsHigh.setStatus("current")
_CfcRequestsBumped_Type = Counter32
_CfcRequestsBumped_Object = MibScalar
cfcRequestsBumped = _CfcRequestsBumped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 4),
    _CfcRequestsBumped_Type()
)
cfcRequestsBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcRequestsBumped.setStatus("current")
_CfcRequestTable_Object = MibTable
cfcRequestTable = _CfcRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfcRequestTable.setStatus("current")
_CfcRequestEntry_Object = MibTableRow
cfcRequestEntry = _CfcRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1)
)
cfcRequestEntry.setIndexNames(
    (0, "CISCO-FTP-CLIENT-MIB", "cfcRequestIndex"),
)
if mibBuilder.loadTexts:
    cfcRequestEntry.setStatus("current")


class _CfcRequestIndex_Type(Unsigned32):
    """Custom type cfcRequestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfcRequestIndex_Type.__name__ = "Unsigned32"
_CfcRequestIndex_Object = MibTableColumn
cfcRequestIndex = _CfcRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 1),
    _CfcRequestIndex_Type()
)
cfcRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcRequestIndex.setStatus("current")


class _CfcRequestOperation_Type(Integer32):
    """Custom type cfcRequestOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("putASCII", 2),
          ("putBinary", 1))
    )


_CfcRequestOperation_Type.__name__ = "Integer32"
_CfcRequestOperation_Object = MibTableColumn
cfcRequestOperation = _CfcRequestOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 2),
    _CfcRequestOperation_Type()
)
cfcRequestOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestOperation.setStatus("current")


class _CfcRequestLocalFile_Type(DisplayString):
    """Custom type cfcRequestLocalFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfcRequestLocalFile_Type.__name__ = "DisplayString"
_CfcRequestLocalFile_Object = MibTableColumn
cfcRequestLocalFile = _CfcRequestLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 3),
    _CfcRequestLocalFile_Type()
)
cfcRequestLocalFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestLocalFile.setStatus("current")


class _CfcRequestRemoteFile_Type(DisplayString):
    """Custom type cfcRequestRemoteFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfcRequestRemoteFile_Type.__name__ = "DisplayString"
_CfcRequestRemoteFile_Object = MibTableColumn
cfcRequestRemoteFile = _CfcRequestRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 4),
    _CfcRequestRemoteFile_Type()
)
cfcRequestRemoteFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestRemoteFile.setStatus("current")


class _CfcRequestServer_Type(DisplayString):
    """Custom type cfcRequestServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfcRequestServer_Type.__name__ = "DisplayString"
_CfcRequestServer_Object = MibTableColumn
cfcRequestServer = _CfcRequestServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 5),
    _CfcRequestServer_Type()
)
cfcRequestServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestServer.setStatus("current")


class _CfcRequestUser_Type(DisplayString):
    """Custom type cfcRequestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CfcRequestUser_Type.__name__ = "DisplayString"
_CfcRequestUser_Object = MibTableColumn
cfcRequestUser = _CfcRequestUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 6),
    _CfcRequestUser_Type()
)
cfcRequestUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestUser.setStatus("current")


class _CfcRequestPassword_Type(DisplayString):
    """Custom type cfcRequestPassword based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CfcRequestPassword_Type.__name__ = "DisplayString"
_CfcRequestPassword_Object = MibTableColumn
cfcRequestPassword = _CfcRequestPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 7),
    _CfcRequestPassword_Type()
)
cfcRequestPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestPassword.setStatus("current")


class _CfcRequestResult_Type(Integer32):
    """Custom type cfcRequestResult based on Integer32"""
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
        *(("aborted", 3),
          ("badDomainName", 6),
          ("fileOpenFailLocal", 4),
          ("fileOpenFailRemote", 5),
          ("fileReadFailed", 9),
          ("fileWriteFailed", 10),
          ("linkFailed", 8),
          ("pending", 1),
          ("success", 2),
          ("unreachableIpAddress", 7))
    )


_CfcRequestResult_Type.__name__ = "Integer32"
_CfcRequestResult_Object = MibTableColumn
cfcRequestResult = _CfcRequestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 8),
    _CfcRequestResult_Type()
)
cfcRequestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcRequestResult.setStatus("current")
_CfcRequestCompletionTime_Type = TimeStamp
_CfcRequestCompletionTime_Object = MibTableColumn
cfcRequestCompletionTime = _CfcRequestCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 9),
    _CfcRequestCompletionTime_Type()
)
cfcRequestCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcRequestCompletionTime.setStatus("current")


class _CfcRequestStop_Type(Integer32):
    """Custom type cfcRequestStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("stop", 2))
    )


_CfcRequestStop_Type.__name__ = "Integer32"
_CfcRequestStop_Object = MibTableColumn
cfcRequestStop = _CfcRequestStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 10),
    _CfcRequestStop_Type()
)
cfcRequestStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestStop.setStatus("current")


class _CfcRequestOperationState_Type(Integer32):
    """Custom type cfcRequestOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 3),
          ("stopping", 2))
    )


_CfcRequestOperationState_Type.__name__ = "Integer32"
_CfcRequestOperationState_Object = MibTableColumn
cfcRequestOperationState = _CfcRequestOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 11),
    _CfcRequestOperationState_Type()
)
cfcRequestOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcRequestOperationState.setStatus("current")
_CfcRequestEntryStatus_Type = RowStatus
_CfcRequestEntryStatus_Object = MibTableColumn
cfcRequestEntryStatus = _CfcRequestEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 1, 1, 5, 1, 12),
    _CfcRequestEntryStatus_Type()
)
cfcRequestEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcRequestEntryStatus.setStatus("current")
_CiscoFtpClientMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFtpClientMIBConformance = _CiscoFtpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 3)
)
_CiscoFtpClientMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFtpClientMIBCompliances = _CiscoFtpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 3, 1)
)
_CiscoFtpClientMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFtpClientMIBGroups = _CiscoFtpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 3, 2)
)

# Managed Objects groups

ciscoFtpClientRequestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 3, 2, 1)
)
ciscoFtpClientRequestGroup.setObjects(
      *(("CISCO-FTP-CLIENT-MIB", "cfcRequestMaximum"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequests"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestsHigh"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestsBumped"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestOperation"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestLocalFile"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestRemoteFile"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestServer"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestUser"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestPassword"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestResult"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestCompletionTime"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestStop"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestOperationState"),
        ("CISCO-FTP-CLIENT-MIB", "cfcRequestEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoFtpClientRequestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFtpClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 80, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFtpClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FTP-CLIENT-MIB",
    **{"ciscoFtpClientMIB": ciscoFtpClientMIB,
       "ciscoFtpClientMIBObjects": ciscoFtpClientMIBObjects,
       "cfcRequest": cfcRequest,
       "cfcRequestMaximum": cfcRequestMaximum,
       "cfcRequests": cfcRequests,
       "cfcRequestsHigh": cfcRequestsHigh,
       "cfcRequestsBumped": cfcRequestsBumped,
       "cfcRequestTable": cfcRequestTable,
       "cfcRequestEntry": cfcRequestEntry,
       "cfcRequestIndex": cfcRequestIndex,
       "cfcRequestOperation": cfcRequestOperation,
       "cfcRequestLocalFile": cfcRequestLocalFile,
       "cfcRequestRemoteFile": cfcRequestRemoteFile,
       "cfcRequestServer": cfcRequestServer,
       "cfcRequestUser": cfcRequestUser,
       "cfcRequestPassword": cfcRequestPassword,
       "cfcRequestResult": cfcRequestResult,
       "cfcRequestCompletionTime": cfcRequestCompletionTime,
       "cfcRequestStop": cfcRequestStop,
       "cfcRequestOperationState": cfcRequestOperationState,
       "cfcRequestEntryStatus": cfcRequestEntryStatus,
       "ciscoFtpClientMIBConformance": ciscoFtpClientMIBConformance,
       "ciscoFtpClientMIBCompliances": ciscoFtpClientMIBCompliances,
       "ciscoFtpClientMIBCompliance": ciscoFtpClientMIBCompliance,
       "ciscoFtpClientMIBGroups": ciscoFtpClientMIBGroups,
       "ciscoFtpClientRequestGroup": ciscoFtpClientRequestGroup}
)
