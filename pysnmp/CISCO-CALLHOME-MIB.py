# SNMP MIB module (CISCO-CALLHOME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALLHOME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:51 2024
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

(SyslogSeverity,) = mibBuilder.importSymbols(
    "CISCO-SYSLOG-MIB",
    "SyslogSeverity")

(CiscoURLString,
 CiscoVrfName,
 EntPhysicalIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString",
    "CiscoVrfName",
    "EntPhysicalIndexOrZero")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCallHomeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300)
)
ciscoCallHomeMIB.setRevisions(
        ("2012-04-27 00:00",
         "2010-11-08 00:00",
         "2009-05-04 00:00",
         "2009-04-09 00:00",
         "2008-07-01 00:00",
         "2007-12-19 00:00",
         "2007-03-29 00:00",
         "2006-03-30 00:00",
         "2004-08-02 00:00",
         "2004-02-11 00:00",
         "2004-02-09 00:00",
         "2003-10-30 00:00",
         "2003-05-20 00:00",
         "2002-10-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CallHomeAlert(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inventory", 3),
          ("noOp", 1),
          ("test", 2))
    )



class CallHomeMsgFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullText", 2),
          ("shortText", 3),
          ("xml", 1))
    )



class CallHomeTransportMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("email", 1),
          ("emailAndHttp", 4),
          ("ftp", 2),
          ("http", 3))
    )



class CallHomeMsgLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("catastrophic", 10),
          ("critical", 7),
          ("debug", 1),
          ("disaster", 9),
          ("fatal", 8),
          ("major", 6),
          ("minor", 5),
          ("normal", 2),
          ("notification", 3),
          ("warning", 4))
    )



class AlertGroupList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



# MIB Managed Objects in the order of their OIDs

_CcmCallHomeNotifications_ObjectIdentity = ObjectIdentity
ccmCallHomeNotifications = _CcmCallHomeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 0)
)
_CiscoCallHomeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCallHomeMIBObjects = _CiscoCallHomeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1)
)
_CcmCallHomeConfiguration_ObjectIdentity = ObjectIdentity
ccmCallHomeConfiguration = _CcmCallHomeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1)
)
_CallHomeEnable_Type = TruthValue
_CallHomeEnable_Object = MibScalar
callHomeEnable = _CallHomeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 1),
    _CallHomeEnable_Type()
)
callHomeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeEnable.setStatus("current")


class _SysContactPhoneNumber_Type(SnmpAdminString):
    """Custom type sysContactPhoneNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
        ValueSizeConstraint(13, 17),
    )


_SysContactPhoneNumber_Type.__name__ = "SnmpAdminString"
_SysContactPhoneNumber_Object = MibScalar
sysContactPhoneNumber = _SysContactPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 2),
    _SysContactPhoneNumber_Type()
)
sysContactPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContactPhoneNumber.setStatus("current")
_SysContactEmailAddress_Type = SnmpAdminString
_SysContactEmailAddress_Object = MibScalar
sysContactEmailAddress = _SysContactEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 3),
    _SysContactEmailAddress_Type()
)
sysContactEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContactEmailAddress.setStatus("current")
_SysStreetAddress_Type = SnmpAdminString
_SysStreetAddress_Object = MibScalar
sysStreetAddress = _SysStreetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 4),
    _SysStreetAddress_Type()
)
sysStreetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysStreetAddress.setStatus("current")
_CallHomeCustomerId_Type = SnmpAdminString
_CallHomeCustomerId_Object = MibScalar
callHomeCustomerId = _CallHomeCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 5),
    _CallHomeCustomerId_Type()
)
callHomeCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeCustomerId.setStatus("current")
_CallHomeContractId_Type = SnmpAdminString
_CallHomeContractId_Object = MibScalar
callHomeContractId = _CallHomeContractId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 6),
    _CallHomeContractId_Type()
)
callHomeContractId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeContractId.setStatus("current")
_CallHomeSiteId_Type = SnmpAdminString
_CallHomeSiteId_Object = MibScalar
callHomeSiteId = _CallHomeSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 7),
    _CallHomeSiteId_Type()
)
callHomeSiteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeSiteId.setStatus("current")


class _CallHomeDeviceServicePriority_Type(SyslogSeverity):
    """Custom type callHomeDeviceServicePriority based on SyslogSeverity"""


_CallHomeDeviceServicePriority_Object = MibScalar
callHomeDeviceServicePriority = _CallHomeDeviceServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 8),
    _CallHomeDeviceServicePriority_Type()
)
callHomeDeviceServicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeDeviceServicePriority.setStatus("current")
_CallHomeAlertAction_Type = CallHomeAlert
_CallHomeAlertAction_Object = MibScalar
callHomeAlertAction = _CallHomeAlertAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 9),
    _CallHomeAlertAction_Type()
)
callHomeAlertAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeAlertAction.setStatus("current")


class _CallHomeAlertActionStatus_Type(Integer32):
    """Custom type callHomeAlertActionStatus based on Integer32"""
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
        *(("failed", 4),
          ("inprogress", 3),
          ("successful", 2),
          ("unknown", 1))
    )


_CallHomeAlertActionStatus_Type.__name__ = "Integer32"
_CallHomeAlertActionStatus_Object = MibScalar
callHomeAlertActionStatus = _CallHomeAlertActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 10),
    _CallHomeAlertActionStatus_Type()
)
callHomeAlertActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeAlertActionStatus.setStatus("current")
_CallHomeAlertActionFailureCause_Type = SnmpAdminString
_CallHomeAlertActionFailureCause_Object = MibScalar
callHomeAlertActionFailureCause = _CallHomeAlertActionFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 11),
    _CallHomeAlertActionFailureCause_Type()
)
callHomeAlertActionFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeAlertActionFailureCause.setStatus("current")
_CallHomeDestProfileTable_Object = MibTable
callHomeDestProfileTable = _CallHomeDestProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12)
)
if mibBuilder.loadTexts:
    callHomeDestProfileTable.setStatus("current")
_CallHomeDestProfileEntry_Object = MibTableRow
callHomeDestProfileEntry = _CallHomeDestProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1)
)
callHomeDestProfileEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
)
if mibBuilder.loadTexts:
    callHomeDestProfileEntry.setStatus("current")


class _CallHomeDestProfileName_Type(SnmpAdminString):
    """Custom type callHomeDestProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CallHomeDestProfileName_Type.__name__ = "SnmpAdminString"
_CallHomeDestProfileName_Object = MibTableColumn
callHomeDestProfileName = _CallHomeDestProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 1),
    _CallHomeDestProfileName_Type()
)
callHomeDestProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callHomeDestProfileName.setStatus("current")


class _CallHomeDestProfileMsgFormat_Type(CallHomeMsgFormat):
    """Custom type callHomeDestProfileMsgFormat based on CallHomeMsgFormat"""


_CallHomeDestProfileMsgFormat_Object = MibTableColumn
callHomeDestProfileMsgFormat = _CallHomeDestProfileMsgFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 2),
    _CallHomeDestProfileMsgFormat_Type()
)
callHomeDestProfileMsgFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileMsgFormat.setStatus("current")


class _CallHomeDestProfileMaxMsgSize_Type(Unsigned32):
    """Custom type callHomeDestProfileMaxMsgSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CallHomeDestProfileMaxMsgSize_Type.__name__ = "Unsigned32"
_CallHomeDestProfileMaxMsgSize_Object = MibTableColumn
callHomeDestProfileMaxMsgSize = _CallHomeDestProfileMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 3),
    _CallHomeDestProfileMaxMsgSize_Type()
)
callHomeDestProfileMaxMsgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileMaxMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    callHomeDestProfileMaxMsgSize.setUnits("bytes")


class _CallHomeDestProfileTrnsprtMthd_Type(CallHomeTransportMethod):
    """Custom type callHomeDestProfileTrnsprtMthd based on CallHomeTransportMethod"""


_CallHomeDestProfileTrnsprtMthd_Object = MibTableColumn
callHomeDestProfileTrnsprtMthd = _CallHomeDestProfileTrnsprtMthd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 4),
    _CallHomeDestProfileTrnsprtMthd_Type()
)
callHomeDestProfileTrnsprtMthd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileTrnsprtMthd.setStatus("current")
_CallHomeDestProfileStatus_Type = RowStatus
_CallHomeDestProfileStatus_Object = MibTableColumn
callHomeDestProfileStatus = _CallHomeDestProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 5),
    _CallHomeDestProfileStatus_Type()
)
callHomeDestProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileStatus.setStatus("current")


class _CallHomeDestProfileMsgLevel_Type(CallHomeMsgLevel):
    """Custom type callHomeDestProfileMsgLevel based on CallHomeMsgLevel"""


_CallHomeDestProfileMsgLevel_Object = MibTableColumn
callHomeDestProfileMsgLevel = _CallHomeDestProfileMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 6),
    _CallHomeDestProfileMsgLevel_Type()
)
callHomeDestProfileMsgLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileMsgLevel.setStatus("current")
_CallHomeDestProfileAlertGroups_Type = AlertGroupList
_CallHomeDestProfileAlertGroups_Object = MibTableColumn
callHomeDestProfileAlertGroups = _CallHomeDestProfileAlertGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 7),
    _CallHomeDestProfileAlertGroups_Type()
)
callHomeDestProfileAlertGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileAlertGroups.setStatus("current")


class _CallHomeDestProfileActive_Type(TruthValue):
    """Custom type callHomeDestProfileActive based on TruthValue"""


_CallHomeDestProfileActive_Object = MibTableColumn
callHomeDestProfileActive = _CallHomeDestProfileActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 8),
    _CallHomeDestProfileActive_Type()
)
callHomeDestProfileActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileActive.setStatus("current")
_CallHomeDestProfileHiMaxMsgSize_Type = Unsigned32
_CallHomeDestProfileHiMaxMsgSize_Object = MibTableColumn
callHomeDestProfileHiMaxMsgSize = _CallHomeDestProfileHiMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 12, 1, 9),
    _CallHomeDestProfileHiMaxMsgSize_Type()
)
callHomeDestProfileHiMaxMsgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestProfileHiMaxMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    callHomeDestProfileHiMaxMsgSize.setUnits("bytes")


class _CallHomeEmailAddrTblMaxEntries_Type(Unsigned32):
    """Custom type callHomeEmailAddrTblMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CallHomeEmailAddrTblMaxEntries_Type.__name__ = "Unsigned32"
_CallHomeEmailAddrTblMaxEntries_Object = MibScalar
callHomeEmailAddrTblMaxEntries = _CallHomeEmailAddrTblMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 13),
    _CallHomeEmailAddrTblMaxEntries_Type()
)
callHomeEmailAddrTblMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeEmailAddrTblMaxEntries.setStatus("current")
_CallHomeDestEmailAddressTable_Object = MibTable
callHomeDestEmailAddressTable = _CallHomeDestEmailAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14)
)
if mibBuilder.loadTexts:
    callHomeDestEmailAddressTable.setStatus("current")
_CallHomeDestEmailAddressEntry_Object = MibTableRow
callHomeDestEmailAddressEntry = _CallHomeDestEmailAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14, 1)
)
callHomeDestEmailAddressEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
    (0, "CISCO-CALLHOME-MIB", "callHomeDestEmailAddressIndex"),
)
if mibBuilder.loadTexts:
    callHomeDestEmailAddressEntry.setStatus("current")


class _CallHomeDestEmailAddressIndex_Type(Unsigned32):
    """Custom type callHomeDestEmailAddressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CallHomeDestEmailAddressIndex_Type.__name__ = "Unsigned32"
_CallHomeDestEmailAddressIndex_Object = MibTableColumn
callHomeDestEmailAddressIndex = _CallHomeDestEmailAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14, 1, 1),
    _CallHomeDestEmailAddressIndex_Type()
)
callHomeDestEmailAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callHomeDestEmailAddressIndex.setStatus("current")
_CallHomeDestEmailAddress_Type = SnmpAdminString
_CallHomeDestEmailAddress_Object = MibTableColumn
callHomeDestEmailAddress = _CallHomeDestEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14, 1, 2),
    _CallHomeDestEmailAddress_Type()
)
callHomeDestEmailAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestEmailAddress.setStatus("current")
_CallHomeDestEmailAddressStatus_Type = RowStatus
_CallHomeDestEmailAddressStatus_Object = MibTableColumn
callHomeDestEmailAddressStatus = _CallHomeDestEmailAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14, 1, 3),
    _CallHomeDestEmailAddressStatus_Type()
)
callHomeDestEmailAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestEmailAddressStatus.setStatus("current")


class _CallHomeDestType_Type(Integer32):
    """Custom type callHomeDestType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("email", 1),
          ("http", 2))
    )


_CallHomeDestType_Type.__name__ = "Integer32"
_CallHomeDestType_Object = MibTableColumn
callHomeDestType = _CallHomeDestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14, 1, 4),
    _CallHomeDestType_Type()
)
callHomeDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestType.setStatus("current")
_CallHomeDestHttpUrl_Type = CiscoURLString
_CallHomeDestHttpUrl_Object = MibTableColumn
callHomeDestHttpUrl = _CallHomeDestHttpUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 14, 1, 5),
    _CallHomeDestHttpUrl_Type()
)
callHomeDestHttpUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeDestHttpUrl.setStatus("current")
_CallHomeEmailFrom_Type = SnmpAdminString
_CallHomeEmailFrom_Object = MibScalar
callHomeEmailFrom = _CallHomeEmailFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 15),
    _CallHomeEmailFrom_Type()
)
callHomeEmailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeEmailFrom.setStatus("current")
_CallHomeEmailReplyTo_Type = SnmpAdminString
_CallHomeEmailReplyTo_Object = MibScalar
callHomeEmailReplyTo = _CallHomeEmailReplyTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 16),
    _CallHomeEmailReplyTo_Type()
)
callHomeEmailReplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeEmailReplyTo.setStatus("current")
_CallHomeEmailMsgDispNotification_Type = SnmpAdminString
_CallHomeEmailMsgDispNotification_Object = MibScalar
callHomeEmailMsgDispNotification = _CallHomeEmailMsgDispNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 17),
    _CallHomeEmailMsgDispNotification_Type()
)
callHomeEmailMsgDispNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeEmailMsgDispNotification.setStatus("current")
_CallHomeSmtpServerAddrType_Type = InetAddressType
_CallHomeSmtpServerAddrType_Object = MibScalar
callHomeSmtpServerAddrType = _CallHomeSmtpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 18),
    _CallHomeSmtpServerAddrType_Type()
)
callHomeSmtpServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeSmtpServerAddrType.setStatus("current")
_CallHomeSmtpServerAddr_Type = InetAddress
_CallHomeSmtpServerAddr_Object = MibScalar
callHomeSmtpServerAddr = _CallHomeSmtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 19),
    _CallHomeSmtpServerAddr_Type()
)
callHomeSmtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeSmtpServerAddr.setStatus("current")


class _CallHomeSmtpServerPort_Type(Unsigned32):
    """Custom type callHomeSmtpServerPort based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CallHomeSmtpServerPort_Type.__name__ = "Unsigned32"
_CallHomeSmtpServerPort_Object = MibScalar
callHomeSmtpServerPort = _CallHomeSmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 20),
    _CallHomeSmtpServerPort_Type()
)
callHomeSmtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeSmtpServerPort.setStatus("current")


class _CcmSmtpServersTblMaxEntries_Type(Unsigned32):
    """Custom type ccmSmtpServersTblMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcmSmtpServersTblMaxEntries_Type.__name__ = "Unsigned32"
_CcmSmtpServersTblMaxEntries_Object = MibScalar
ccmSmtpServersTblMaxEntries = _CcmSmtpServersTblMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 21),
    _CcmSmtpServersTblMaxEntries_Type()
)
ccmSmtpServersTblMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSmtpServersTblMaxEntries.setStatus("current")
_CcmSmtpServersTable_Object = MibTable
ccmSmtpServersTable = _CcmSmtpServersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22)
)
if mibBuilder.loadTexts:
    ccmSmtpServersTable.setStatus("current")
_CcmSmtpServersEntry_Object = MibTableRow
ccmSmtpServersEntry = _CcmSmtpServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1)
)
ccmSmtpServersEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "ccmSmtpServersAddrType"),
    (0, "CISCO-CALLHOME-MIB", "ccmSmtpServersAddr"),
)
if mibBuilder.loadTexts:
    ccmSmtpServersEntry.setStatus("current")
_CcmSmtpServersAddrType_Type = InetAddressType
_CcmSmtpServersAddrType_Object = MibTableColumn
ccmSmtpServersAddrType = _CcmSmtpServersAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1, 1),
    _CcmSmtpServersAddrType_Type()
)
ccmSmtpServersAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmSmtpServersAddrType.setStatus("current")


class _CcmSmtpServersAddr_Type(InetAddress):
    """Custom type ccmSmtpServersAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcmSmtpServersAddr_Type.__name__ = "InetAddress"
_CcmSmtpServersAddr_Object = MibTableColumn
ccmSmtpServersAddr = _CcmSmtpServersAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1, 2),
    _CcmSmtpServersAddr_Type()
)
ccmSmtpServersAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmSmtpServersAddr.setStatus("current")


class _CcmSmtpServersPort_Type(Unsigned32):
    """Custom type ccmSmtpServersPort based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcmSmtpServersPort_Type.__name__ = "Unsigned32"
_CcmSmtpServersPort_Object = MibTableColumn
ccmSmtpServersPort = _CcmSmtpServersPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1, 3),
    _CcmSmtpServersPort_Type()
)
ccmSmtpServersPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmSmtpServersPort.setStatus("current")
_CcmSmtpServersStatus_Type = RowStatus
_CcmSmtpServersStatus_Object = MibTableColumn
ccmSmtpServersStatus = _CcmSmtpServersStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1, 4),
    _CcmSmtpServersStatus_Type()
)
ccmSmtpServersStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmSmtpServersStatus.setStatus("current")


class _CcmSmtpServersPriority_Type(Unsigned32):
    """Custom type ccmSmtpServersPriority based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcmSmtpServersPriority_Type.__name__ = "Unsigned32"
_CcmSmtpServersPriority_Object = MibTableColumn
ccmSmtpServersPriority = _CcmSmtpServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1, 5),
    _CcmSmtpServersPriority_Type()
)
ccmSmtpServersPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmSmtpServersPriority.setStatus("current")


class _CcmSmtpServersUseVrf_Type(CiscoVrfName):
    """Custom type ccmSmtpServersUseVrf based on CiscoVrfName"""
    defaultValue = OctetString("default")


_CcmSmtpServersUseVrf_Object = MibTableColumn
ccmSmtpServersUseVrf = _CcmSmtpServersUseVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 22, 1, 6),
    _CcmSmtpServersUseVrf_Type()
)
ccmSmtpServersUseVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmSmtpServersUseVrf.setStatus("current")
_CcmSysLogSeverity_Type = SyslogSeverity
_CcmSysLogSeverity_Object = MibScalar
ccmSysLogSeverity = _CcmSysLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 23),
    _CcmSysLogSeverity_Type()
)
ccmSysLogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSysLogSeverity.setStatus("current")
_CcmEnableSmtpServerNotif_Type = TruthValue
_CcmEnableSmtpServerNotif_Object = MibScalar
ccmEnableSmtpServerNotif = _CcmEnableSmtpServerNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 24),
    _CcmEnableSmtpServerNotif_Type()
)
ccmEnableSmtpServerNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmEnableSmtpServerNotif.setStatus("current")
_CallHomeAlertGroupTypeTable_Object = MibTable
callHomeAlertGroupTypeTable = _CallHomeAlertGroupTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 25)
)
if mibBuilder.loadTexts:
    callHomeAlertGroupTypeTable.setStatus("current")
_CallHomeAlertGroupTypeEntry_Object = MibTableRow
callHomeAlertGroupTypeEntry = _CallHomeAlertGroupTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 25, 1)
)
callHomeAlertGroupTypeEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeAlertGroupTypeIndex"),
)
if mibBuilder.loadTexts:
    callHomeAlertGroupTypeEntry.setStatus("current")


class _CallHomeAlertGroupTypeIndex_Type(Unsigned32):
    """Custom type callHomeAlertGroupTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CallHomeAlertGroupTypeIndex_Type.__name__ = "Unsigned32"
_CallHomeAlertGroupTypeIndex_Object = MibTableColumn
callHomeAlertGroupTypeIndex = _CallHomeAlertGroupTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 25, 1, 1),
    _CallHomeAlertGroupTypeIndex_Type()
)
callHomeAlertGroupTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callHomeAlertGroupTypeIndex.setStatus("current")


class _CallHomeAlertGroupName_Type(SnmpAdminString):
    """Custom type callHomeAlertGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CallHomeAlertGroupName_Type.__name__ = "SnmpAdminString"
_CallHomeAlertGroupName_Object = MibTableColumn
callHomeAlertGroupName = _CallHomeAlertGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 25, 1, 2),
    _CallHomeAlertGroupName_Type()
)
callHomeAlertGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeAlertGroupName.setStatus("current")
_CallHomeAlertGroupEnable_Type = TruthValue
_CallHomeAlertGroupEnable_Object = MibTableColumn
callHomeAlertGroupEnable = _CallHomeAlertGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 25, 1, 3),
    _CallHomeAlertGroupEnable_Type()
)
callHomeAlertGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeAlertGroupEnable.setStatus("current")


class _CallHomeAlertGroupCapability_Type(Bits):
    """Custom type callHomeAlertGroupCapability based on Bits"""
    namedValues = NamedValues(
        *(("callHomeMessageSeverity", 0),
          ("event", 3),
          ("onDemand", 4),
          ("onDemandPerEntity", 5),
          ("periodic", 1),
          ("periodicHourly", 6),
          ("periodicMinutes", 7),
          ("regularExpression", 2))
    )

_CallHomeAlertGroupCapability_Type.__name__ = "Bits"
_CallHomeAlertGroupCapability_Object = MibTableColumn
callHomeAlertGroupCapability = _CallHomeAlertGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 25, 1, 4),
    _CallHomeAlertGroupCapability_Type()
)
callHomeAlertGroupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeAlertGroupCapability.setStatus("current")
_CallHomeSwInventoryTable_Object = MibTable
callHomeSwInventoryTable = _CallHomeSwInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 26)
)
if mibBuilder.loadTexts:
    callHomeSwInventoryTable.setStatus("current")
_CallHomeSwInventoryEntry_Object = MibTableRow
callHomeSwInventoryEntry = _CallHomeSwInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 26, 1)
)
callHomeSwInventoryEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeSwServiceName"),
    (0, "CISCO-CALLHOME-MIB", "callHomeInventoryNVPairIndex"),
)
if mibBuilder.loadTexts:
    callHomeSwInventoryEntry.setStatus("current")


class _CallHomeSwServiceName_Type(SnmpAdminString):
    """Custom type callHomeSwServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CallHomeSwServiceName_Type.__name__ = "SnmpAdminString"
_CallHomeSwServiceName_Object = MibTableColumn
callHomeSwServiceName = _CallHomeSwServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 26, 1, 1),
    _CallHomeSwServiceName_Type()
)
callHomeSwServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callHomeSwServiceName.setStatus("current")


class _CallHomeInventoryNVPairIndex_Type(Unsigned32):
    """Custom type callHomeInventoryNVPairIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CallHomeInventoryNVPairIndex_Type.__name__ = "Unsigned32"
_CallHomeInventoryNVPairIndex_Object = MibTableColumn
callHomeInventoryNVPairIndex = _CallHomeInventoryNVPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 26, 1, 2),
    _CallHomeInventoryNVPairIndex_Type()
)
callHomeInventoryNVPairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callHomeInventoryNVPairIndex.setStatus("current")


class _CallHomeInventoryInfoName_Type(OctetString):
    """Custom type callHomeInventoryInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CallHomeInventoryInfoName_Type.__name__ = "OctetString"
_CallHomeInventoryInfoName_Object = MibTableColumn
callHomeInventoryInfoName = _CallHomeInventoryInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 26, 1, 3),
    _CallHomeInventoryInfoName_Type()
)
callHomeInventoryInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeInventoryInfoName.setStatus("current")


class _CallHomeInventoryInfoValue_Type(OctetString):
    """Custom type callHomeInventoryInfoValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CallHomeInventoryInfoValue_Type.__name__ = "OctetString"
_CallHomeInventoryInfoValue_Object = MibTableColumn
callHomeInventoryInfoValue = _CallHomeInventoryInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 26, 1, 4),
    _CallHomeInventoryInfoValue_Type()
)
callHomeInventoryInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeInventoryInfoValue.setStatus("current")


class _CcmPeriodicSwInventoryMsgEnable_Type(TruthValue):
    """Custom type ccmPeriodicSwInventoryMsgEnable based on TruthValue"""


_CcmPeriodicSwInventoryMsgEnable_Object = MibScalar
ccmPeriodicSwInventoryMsgEnable = _CcmPeriodicSwInventoryMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 27),
    _CcmPeriodicSwInventoryMsgEnable_Type()
)
ccmPeriodicSwInventoryMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicSwInventoryMsgEnable.setStatus("current")


class _CcmPeriodicSwInventoryTimeFrame_Type(Unsigned32):
    """Custom type ccmPeriodicSwInventoryTimeFrame based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CcmPeriodicSwInventoryTimeFrame_Type.__name__ = "Unsigned32"
_CcmPeriodicSwInventoryTimeFrame_Object = MibScalar
ccmPeriodicSwInventoryTimeFrame = _CcmPeriodicSwInventoryTimeFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 28),
    _CcmPeriodicSwInventoryTimeFrame_Type()
)
ccmPeriodicSwInventoryTimeFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicSwInventoryTimeFrame.setStatus("current")
if mibBuilder.loadTexts:
    ccmPeriodicSwInventoryTimeFrame.setUnits("days")


class _CcmMsgThrottlingEnable_Type(TruthValue):
    """Custom type ccmMsgThrottlingEnable based on TruthValue"""


_CcmMsgThrottlingEnable_Object = MibScalar
ccmMsgThrottlingEnable = _CcmMsgThrottlingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 29),
    _CcmMsgThrottlingEnable_Type()
)
ccmMsgThrottlingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmMsgThrottlingEnable.setStatus("current")
_CcmCallHomeAlertGroupCfg_ObjectIdentity = ObjectIdentity
ccmCallHomeAlertGroupCfg = _CcmCallHomeAlertGroupCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30)
)
_CcmSeverityAlertGroupTable_Object = MibTable
ccmSeverityAlertGroupTable = _CcmSeverityAlertGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 1)
)
if mibBuilder.loadTexts:
    ccmSeverityAlertGroupTable.setStatus("current")
_CcmSeverityAlertGroupEntry_Object = MibTableRow
ccmSeverityAlertGroupEntry = _CcmSeverityAlertGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 1, 1)
)
ccmSeverityAlertGroupEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
    (0, "CISCO-CALLHOME-MIB", "callHomeAlertGroupTypeIndex"),
)
if mibBuilder.loadTexts:
    ccmSeverityAlertGroupEntry.setStatus("current")


class _CcmAlertGroupSeverity_Type(CallHomeMsgLevel):
    """Custom type ccmAlertGroupSeverity based on CallHomeMsgLevel"""


_CcmAlertGroupSeverity_Object = MibTableColumn
ccmAlertGroupSeverity = _CcmAlertGroupSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 1, 1, 1),
    _CcmAlertGroupSeverity_Type()
)
ccmAlertGroupSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmAlertGroupSeverity.setStatus("current")
_CcmPeriodicAlertGroupTable_Object = MibTable
ccmPeriodicAlertGroupTable = _CcmPeriodicAlertGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2)
)
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupTable.setStatus("current")
_CcmPeriodicAlertGroupEntry_Object = MibTableRow
ccmPeriodicAlertGroupEntry = _CcmPeriodicAlertGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1)
)
ccmPeriodicAlertGroupEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
    (0, "CISCO-CALLHOME-MIB", "callHomeAlertGroupTypeIndex"),
)
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupEntry.setStatus("current")


class _CcmPeriodicAlertGroupInterval_Type(Integer32):
    """Custom type ccmPeriodicAlertGroupInterval based on Integer32"""
    defaultValue = 1

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
        *(("daily", 1),
          ("hourly", 4),
          ("minutes", 5),
          ("monthly", 3),
          ("weekly", 2))
    )


_CcmPeriodicAlertGroupInterval_Type.__name__ = "Integer32"
_CcmPeriodicAlertGroupInterval_Object = MibTableColumn
ccmPeriodicAlertGroupInterval = _CcmPeriodicAlertGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 1),
    _CcmPeriodicAlertGroupInterval_Type()
)
ccmPeriodicAlertGroupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupInterval.setStatus("current")


class _CcmPeriodicAlertGroupDayOfWeek_Type(Integer32):
    """Custom type ccmPeriodicAlertGroupDayOfWeek based on Integer32"""
    defaultValue = 1

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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_CcmPeriodicAlertGroupDayOfWeek_Type.__name__ = "Integer32"
_CcmPeriodicAlertGroupDayOfWeek_Object = MibTableColumn
ccmPeriodicAlertGroupDayOfWeek = _CcmPeriodicAlertGroupDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 2),
    _CcmPeriodicAlertGroupDayOfWeek_Type()
)
ccmPeriodicAlertGroupDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupDayOfWeek.setStatus("current")


class _CcmPeriodicAlertGroupDayOfMonth_Type(Unsigned32):
    """Custom type ccmPeriodicAlertGroupDayOfMonth based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcmPeriodicAlertGroupDayOfMonth_Type.__name__ = "Unsigned32"
_CcmPeriodicAlertGroupDayOfMonth_Object = MibTableColumn
ccmPeriodicAlertGroupDayOfMonth = _CcmPeriodicAlertGroupDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 3),
    _CcmPeriodicAlertGroupDayOfMonth_Type()
)
ccmPeriodicAlertGroupDayOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupDayOfMonth.setStatus("current")


class _CcmPeriodicAlertGroupHour_Type(Unsigned32):
    """Custom type ccmPeriodicAlertGroupHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmPeriodicAlertGroupHour_Type.__name__ = "Unsigned32"
_CcmPeriodicAlertGroupHour_Object = MibTableColumn
ccmPeriodicAlertGroupHour = _CcmPeriodicAlertGroupHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 4),
    _CcmPeriodicAlertGroupHour_Type()
)
ccmPeriodicAlertGroupHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupHour.setStatus("current")


class _CcmPeriodicAlertGroupMinute_Type(Unsigned32):
    """Custom type ccmPeriodicAlertGroupMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmPeriodicAlertGroupMinute_Type.__name__ = "Unsigned32"
_CcmPeriodicAlertGroupMinute_Object = MibTableColumn
ccmPeriodicAlertGroupMinute = _CcmPeriodicAlertGroupMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 5),
    _CcmPeriodicAlertGroupMinute_Type()
)
ccmPeriodicAlertGroupMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupMinute.setStatus("current")


class _CcmPeriodicAlertGroupEnable_Type(TruthValue):
    """Custom type ccmPeriodicAlertGroupEnable based on TruthValue"""


_CcmPeriodicAlertGroupEnable_Object = MibTableColumn
ccmPeriodicAlertGroupEnable = _CcmPeriodicAlertGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 6),
    _CcmPeriodicAlertGroupEnable_Type()
)
ccmPeriodicAlertGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupEnable.setStatus("current")


class _CcmPeriodicAlertGroupIntervalMinutes_Type(Unsigned32):
    """Custom type ccmPeriodicAlertGroupIntervalMinutes based on Unsigned32"""
    defaultValue = 60


_CcmPeriodicAlertGroupIntervalMinutes_Object = MibTableColumn
ccmPeriodicAlertGroupIntervalMinutes = _CcmPeriodicAlertGroupIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 2, 1, 7),
    _CcmPeriodicAlertGroupIntervalMinutes_Type()
)
ccmPeriodicAlertGroupIntervalMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupIntervalMinutes.setStatus("current")
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupIntervalMinutes.setUnits("minutes")
_CcmMaxSyslogAlertGroupPatterns_Type = Unsigned32
_CcmMaxSyslogAlertGroupPatterns_Object = MibScalar
ccmMaxSyslogAlertGroupPatterns = _CcmMaxSyslogAlertGroupPatterns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 3),
    _CcmMaxSyslogAlertGroupPatterns_Type()
)
ccmMaxSyslogAlertGroupPatterns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmMaxSyslogAlertGroupPatterns.setStatus("current")
_CcmPatternAlertGroupTable_Object = MibTable
ccmPatternAlertGroupTable = _CcmPatternAlertGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 4)
)
if mibBuilder.loadTexts:
    ccmPatternAlertGroupTable.setStatus("current")
_CcmPatternAlertGroupEntry_Object = MibTableRow
ccmPatternAlertGroupEntry = _CcmPatternAlertGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 4, 1)
)
ccmPatternAlertGroupEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
    (0, "CISCO-CALLHOME-MIB", "callHomeAlertGroupTypeIndex"),
    (1, "CISCO-CALLHOME-MIB", "ccmAlertGroupPattern"),
)
if mibBuilder.loadTexts:
    ccmPatternAlertGroupEntry.setStatus("current")


class _CcmAlertGroupPattern_Type(SnmpAdminString):
    """Custom type ccmAlertGroupPattern based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CcmAlertGroupPattern_Type.__name__ = "SnmpAdminString"
_CcmAlertGroupPattern_Object = MibTableColumn
ccmAlertGroupPattern = _CcmAlertGroupPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 4, 1, 1),
    _CcmAlertGroupPattern_Type()
)
ccmAlertGroupPattern.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmAlertGroupPattern.setStatus("current")


class _CcmPatternAlertGroupSeverity_Type(CallHomeMsgLevel):
    """Custom type ccmPatternAlertGroupSeverity based on CallHomeMsgLevel"""


_CcmPatternAlertGroupSeverity_Object = MibTableColumn
ccmPatternAlertGroupSeverity = _CcmPatternAlertGroupSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 4, 1, 2),
    _CcmPatternAlertGroupSeverity_Type()
)
ccmPatternAlertGroupSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmPatternAlertGroupSeverity.setStatus("current")


class _CcmPatternAlertGroupStorage_Type(StorageType):
    """Custom type ccmPatternAlertGroupStorage based on StorageType"""


_CcmPatternAlertGroupStorage_Object = MibTableColumn
ccmPatternAlertGroupStorage = _CcmPatternAlertGroupStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 4, 1, 3),
    _CcmPatternAlertGroupStorage_Type()
)
ccmPatternAlertGroupStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmPatternAlertGroupStorage.setStatus("current")
_CcmPatternAlertGroupStatus_Type = RowStatus
_CcmPatternAlertGroupStatus_Object = MibTableColumn
ccmPatternAlertGroupStatus = _CcmPatternAlertGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 4, 1, 4),
    _CcmPatternAlertGroupStatus_Type()
)
ccmPatternAlertGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmPatternAlertGroupStatus.setStatus("current")


class _CallHomeUserDefMaxCmds_Type(Unsigned32):
    """Custom type callHomeUserDefMaxCmds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CallHomeUserDefMaxCmds_Type.__name__ = "Unsigned32"
_CallHomeUserDefMaxCmds_Object = MibScalar
callHomeUserDefMaxCmds = _CallHomeUserDefMaxCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 5),
    _CallHomeUserDefMaxCmds_Type()
)
callHomeUserDefMaxCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeUserDefMaxCmds.setStatus("current")
_CallHomeUserDefCmdTable_Object = MibTable
callHomeUserDefCmdTable = _CallHomeUserDefCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 6)
)
if mibBuilder.loadTexts:
    callHomeUserDefCmdTable.setStatus("current")
_CallHomeUserDefCmdEntry_Object = MibTableRow
callHomeUserDefCmdEntry = _CallHomeUserDefCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 6, 1)
)
callHomeUserDefCmdEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeAlertGroupTypeIndex"),
    (0, "CISCO-CALLHOME-MIB", "callHomeUserDefCmdIndex"),
)
if mibBuilder.loadTexts:
    callHomeUserDefCmdEntry.setStatus("current")
_CallHomeUserDefCmdIndex_Type = Unsigned32
_CallHomeUserDefCmdIndex_Object = MibTableColumn
callHomeUserDefCmdIndex = _CallHomeUserDefCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 6, 1, 1),
    _CallHomeUserDefCmdIndex_Type()
)
callHomeUserDefCmdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callHomeUserDefCmdIndex.setStatus("current")


class _CallHomeUserDefCmdName_Type(SnmpAdminString):
    """Custom type callHomeUserDefCmdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CallHomeUserDefCmdName_Type.__name__ = "SnmpAdminString"
_CallHomeUserDefCmdName_Object = MibTableColumn
callHomeUserDefCmdName = _CallHomeUserDefCmdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 6, 1, 2),
    _CallHomeUserDefCmdName_Type()
)
callHomeUserDefCmdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeUserDefCmdName.setStatus("current")
_CallHomeUserDefCmdRowStatus_Type = RowStatus
_CallHomeUserDefCmdRowStatus_Object = MibTableColumn
callHomeUserDefCmdRowStatus = _CallHomeUserDefCmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 6, 1, 3),
    _CallHomeUserDefCmdRowStatus_Type()
)
callHomeUserDefCmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    callHomeUserDefCmdRowStatus.setStatus("current")
_CcmEventAlertGroupTable_Object = MibTable
ccmEventAlertGroupTable = _CcmEventAlertGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 7)
)
if mibBuilder.loadTexts:
    ccmEventAlertGroupTable.setStatus("current")
_CcmEventAlertGroupEntry_Object = MibTableRow
ccmEventAlertGroupEntry = _CcmEventAlertGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 7, 1)
)
ccmEventAlertGroupEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
    (0, "CISCO-CALLHOME-MIB", "callHomeAlertGroupTypeIndex"),
)
if mibBuilder.loadTexts:
    ccmEventAlertGroupEntry.setStatus("current")


class _CcmEventAlertGroupEnable_Type(TruthValue):
    """Custom type ccmEventAlertGroupEnable based on TruthValue"""


_CcmEventAlertGroupEnable_Object = MibTableColumn
ccmEventAlertGroupEnable = _CcmEventAlertGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 7, 1, 1),
    _CcmEventAlertGroupEnable_Type()
)
ccmEventAlertGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmEventAlertGroupEnable.setStatus("current")
_CcmEventAlertGroupOperSeverity_Type = CallHomeMsgLevel
_CcmEventAlertGroupOperSeverity_Object = MibTableColumn
ccmEventAlertGroupOperSeverity = _CcmEventAlertGroupOperSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 30, 7, 1, 2),
    _CcmEventAlertGroupOperSeverity_Type()
)
ccmEventAlertGroupOperSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventAlertGroupOperSeverity.setStatus("current")
_CcmCallHomeProfileTestControl_ObjectIdentity = ObjectIdentity
ccmCallHomeProfileTestControl = _CcmCallHomeProfileTestControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31)
)
_CcmDestProfileTestTable_Object = MibTable
ccmDestProfileTestTable = _CcmDestProfileTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    ccmDestProfileTestTable.setStatus("current")
_CcmDestProfileTestEntry_Object = MibTableRow
ccmDestProfileTestEntry = _CcmDestProfileTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31, 1, 1)
)
ccmDestProfileTestEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "callHomeDestProfileName"),
)
if mibBuilder.loadTexts:
    ccmDestProfileTestEntry.setStatus("current")
_CcmDestProfileTestTrigger_Type = TruthValue
_CcmDestProfileTestTrigger_Object = MibTableColumn
ccmDestProfileTestTrigger = _CcmDestProfileTestTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31, 1, 1, 1),
    _CcmDestProfileTestTrigger_Type()
)
ccmDestProfileTestTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmDestProfileTestTrigger.setStatus("current")
_CcmDestProfileTestMessage_Type = SnmpAdminString
_CcmDestProfileTestMessage_Object = MibTableColumn
ccmDestProfileTestMessage = _CcmDestProfileTestMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31, 1, 1, 2),
    _CcmDestProfileTestMessage_Type()
)
ccmDestProfileTestMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmDestProfileTestMessage.setStatus("current")


class _CcmDestProfileTestStatus_Type(Integer32):
    """Custom type ccmDestProfileTestStatus based on Integer32"""
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
        *(("failed", 4),
          ("inprogress", 3),
          ("successful", 2),
          ("unknown", 1))
    )


_CcmDestProfileTestStatus_Type.__name__ = "Integer32"
_CcmDestProfileTestStatus_Object = MibTableColumn
ccmDestProfileTestStatus = _CcmDestProfileTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31, 1, 1, 3),
    _CcmDestProfileTestStatus_Type()
)
ccmDestProfileTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDestProfileTestStatus.setStatus("current")
_CcmDestProfileTestFailureCause_Type = SnmpAdminString
_CcmDestProfileTestFailureCause_Object = MibTableColumn
ccmDestProfileTestFailureCause = _CcmDestProfileTestFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 31, 1, 1, 4),
    _CcmDestProfileTestFailureCause_Type()
)
ccmDestProfileTestFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmDestProfileTestFailureCause.setStatus("current")
_CcmCallHomeNotifConfig_ObjectIdentity = ObjectIdentity
ccmCallHomeNotifConfig = _CcmCallHomeNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 32)
)
_CcmSmtpMsgSendFailNotifEnable_Type = TruthValue
_CcmSmtpMsgSendFailNotifEnable_Object = MibScalar
ccmSmtpMsgSendFailNotifEnable = _CcmSmtpMsgSendFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 32, 1),
    _CcmSmtpMsgSendFailNotifEnable_Type()
)
ccmSmtpMsgSendFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmtpMsgSendFailNotifEnable.setStatus("current")
_CcmPeriodicSwInventoryCfg_ObjectIdentity = ObjectIdentity
ccmPeriodicSwInventoryCfg = _CcmPeriodicSwInventoryCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 33)
)


class _CcmPeriodicSwInventoryTimeOfDay_Type(SnmpAdminString):
    """Custom type ccmPeriodicSwInventoryTimeOfDay based on SnmpAdminString"""
    defaultValue = OctetString("08:00")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CcmPeriodicSwInventoryTimeOfDay_Type.__name__ = "SnmpAdminString"
_CcmPeriodicSwInventoryTimeOfDay_Object = MibScalar
ccmPeriodicSwInventoryTimeOfDay = _CcmPeriodicSwInventoryTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 33, 1),
    _CcmPeriodicSwInventoryTimeOfDay_Type()
)
ccmPeriodicSwInventoryTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmPeriodicSwInventoryTimeOfDay.setStatus("current")
_CcmAlertRateLimit_Type = Unsigned32
_CcmAlertRateLimit_Object = MibScalar
ccmAlertRateLimit = _CcmAlertRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 34),
    _CcmAlertRateLimit_Type()
)
ccmAlertRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmAlertRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    ccmAlertRateLimit.setUnits("alerts per minute")
_CcmHttpProxyServerAddrType_Type = InetAddressType
_CcmHttpProxyServerAddrType_Object = MibScalar
ccmHttpProxyServerAddrType = _CcmHttpProxyServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 35),
    _CcmHttpProxyServerAddrType_Type()
)
ccmHttpProxyServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmHttpProxyServerAddrType.setStatus("current")
_CcmHttpProxyServerAddr_Type = InetAddress
_CcmHttpProxyServerAddr_Object = MibScalar
ccmHttpProxyServerAddr = _CcmHttpProxyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 36),
    _CcmHttpProxyServerAddr_Type()
)
ccmHttpProxyServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmHttpProxyServerAddr.setStatus("current")


class _CcmHttpProxyServerPort_Type(Unsigned32):
    """Custom type ccmHttpProxyServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcmHttpProxyServerPort_Type.__name__ = "Unsigned32"
_CcmHttpProxyServerPort_Object = MibScalar
ccmHttpProxyServerPort = _CcmHttpProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 37),
    _CcmHttpProxyServerPort_Type()
)
ccmHttpProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmHttpProxyServerPort.setStatus("current")
_CcmHttpProxyServerUseEnable_Type = TruthValue
_CcmHttpProxyServerUseEnable_Object = MibScalar
ccmHttpProxyServerUseEnable = _CcmHttpProxyServerUseEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 38),
    _CcmHttpProxyServerUseEnable_Type()
)
ccmHttpProxyServerUseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmHttpProxyServerUseEnable.setStatus("current")


class _CallHomeSmtpServerUseVrf_Type(CiscoVrfName):
    """Custom type callHomeSmtpServerUseVrf based on CiscoVrfName"""
    defaultValue = OctetString("default")


_CallHomeSmtpServerUseVrf_Object = MibScalar
callHomeSmtpServerUseVrf = _CallHomeSmtpServerUseVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 39),
    _CallHomeSmtpServerUseVrf_Type()
)
callHomeSmtpServerUseVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHomeSmtpServerUseVrf.setStatus("current")


class _CcmHttpTransportUseVrf_Type(CiscoVrfName):
    """Custom type ccmHttpTransportUseVrf based on CiscoVrfName"""
    defaultValue = OctetString("default")


_CcmHttpTransportUseVrf_Object = MibScalar
ccmHttpTransportUseVrf = _CcmHttpTransportUseVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 1, 40),
    _CcmHttpTransportUseVrf_Type()
)
ccmHttpTransportUseVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmHttpTransportUseVrf.setStatus("current")
_CcmCallHomeStats_ObjectIdentity = ObjectIdentity
ccmCallHomeStats = _CcmCallHomeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2)
)
_CallHomeLastAlertSent_Type = TimeStamp
_CallHomeLastAlertSent_Object = MibScalar
callHomeLastAlertSent = _CallHomeLastAlertSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 1),
    _CallHomeLastAlertSent_Type()
)
callHomeLastAlertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeLastAlertSent.setStatus("current")
_CallHomeAlerts_Type = Counter32
_CallHomeAlerts_Object = MibScalar
callHomeAlerts = _CallHomeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 2),
    _CallHomeAlerts_Type()
)
callHomeAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeAlerts.setStatus("current")
_CallHomeHCAlerts_Type = Counter64
_CallHomeHCAlerts_Object = MibScalar
callHomeHCAlerts = _CallHomeHCAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 3),
    _CallHomeHCAlerts_Type()
)
callHomeHCAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHomeHCAlerts.setStatus("current")
_CcmAlertsDropped_Type = Counter64
_CcmAlertsDropped_Object = MibScalar
ccmAlertsDropped = _CcmAlertsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 4),
    _CcmAlertsDropped_Type()
)
ccmAlertsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmAlertsDropped.setStatus("current")
_CcmEventStatsTable_Object = MibTable
ccmEventStatsTable = _CcmEventStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ccmEventStatsTable.setStatus("current")
_CcmEventStatsEntry_Object = MibTableRow
ccmEventStatsEntry = _CcmEventStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1)
)
ccmEventStatsEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "ccmEventStatsTypeIndex"),
    (0, "CISCO-CALLHOME-MIB", "ccmEventStatsMsgTypeIndex"),
)
if mibBuilder.loadTexts:
    ccmEventStatsEntry.setStatus("current")


class _CcmEventStatsTypeIndex_Type(Integer32):
    """Custom type ccmEventStatsTypeIndex based on Integer32"""
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
        *(("dropped", 3),
          ("failed", 4),
          ("inQueue", 2),
          ("successful", 1))
    )


_CcmEventStatsTypeIndex_Type.__name__ = "Integer32"
_CcmEventStatsTypeIndex_Object = MibTableColumn
ccmEventStatsTypeIndex = _CcmEventStatsTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 1),
    _CcmEventStatsTypeIndex_Type()
)
ccmEventStatsTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmEventStatsTypeIndex.setStatus("current")


class _CcmEventStatsMsgTypeIndex_Type(Integer32):
    """Custom type ccmEventStatsMsgTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("email", 2),
          ("http", 3),
          ("total", 1))
    )


_CcmEventStatsMsgTypeIndex_Type.__name__ = "Integer32"
_CcmEventStatsMsgTypeIndex_Object = MibTableColumn
ccmEventStatsMsgTypeIndex = _CcmEventStatsMsgTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 2),
    _CcmEventStatsMsgTypeIndex_Type()
)
ccmEventStatsMsgTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmEventStatsMsgTypeIndex.setStatus("current")
_CcmEventStatsTotal_Type = Counter64
_CcmEventStatsTotal_Object = MibTableColumn
ccmEventStatsTotal = _CcmEventStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 3),
    _CcmEventStatsTotal_Type()
)
ccmEventStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsTotal.setStatus("current")
_CcmEventStatsConfiguration_Type = Counter64
_CcmEventStatsConfiguration_Object = MibTableColumn
ccmEventStatsConfiguration = _CcmEventStatsConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 4),
    _CcmEventStatsConfiguration_Type()
)
ccmEventStatsConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsConfiguration.setStatus("current")
_CcmEventStatsDiagnostic_Type = Counter64
_CcmEventStatsDiagnostic_Object = MibTableColumn
ccmEventStatsDiagnostic = _CcmEventStatsDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 5),
    _CcmEventStatsDiagnostic_Type()
)
ccmEventStatsDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsDiagnostic.setStatus("current")
_CcmEventStatsEnvironment_Type = Counter64
_CcmEventStatsEnvironment_Object = MibTableColumn
ccmEventStatsEnvironment = _CcmEventStatsEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 6),
    _CcmEventStatsEnvironment_Type()
)
ccmEventStatsEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsEnvironment.setStatus("current")
_CcmEventStatsInventory_Type = Counter64
_CcmEventStatsInventory_Object = MibTableColumn
ccmEventStatsInventory = _CcmEventStatsInventory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 7),
    _CcmEventStatsInventory_Type()
)
ccmEventStatsInventory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsInventory.setStatus("current")
_CcmEventStatsSystemLog_Type = Counter64
_CcmEventStatsSystemLog_Object = MibTableColumn
ccmEventStatsSystemLog = _CcmEventStatsSystemLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 8),
    _CcmEventStatsSystemLog_Type()
)
ccmEventStatsSystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsSystemLog.setStatus("current")
_CcmEventStatsTest_Type = Counter64
_CcmEventStatsTest_Object = MibTableColumn
ccmEventStatsTest = _CcmEventStatsTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 9),
    _CcmEventStatsTest_Type()
)
ccmEventStatsTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsTest.setStatus("current")
_CcmEventStatsRequest_Type = Counter64
_CcmEventStatsRequest_Object = MibTableColumn
ccmEventStatsRequest = _CcmEventStatsRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 10),
    _CcmEventStatsRequest_Type()
)
ccmEventStatsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsRequest.setStatus("current")
_CcmEventStatsSendCliOutput_Type = Counter64
_CcmEventStatsSendCliOutput_Object = MibTableColumn
ccmEventStatsSendCliOutput = _CcmEventStatsSendCliOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 2, 5, 1, 11),
    _CcmEventStatsSendCliOutput_Type()
)
ccmEventStatsSendCliOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmEventStatsSendCliOutput.setStatus("current")
_CcmCallHomeStatus_ObjectIdentity = ObjectIdentity
ccmCallHomeStatus = _CcmCallHomeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3)
)
_CcmSmtpServerStatusTimeStamp_Type = TimeStamp
_CcmSmtpServerStatusTimeStamp_Object = MibScalar
ccmSmtpServerStatusTimeStamp = _CcmSmtpServerStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 1),
    _CcmSmtpServerStatusTimeStamp_Type()
)
ccmSmtpServerStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSmtpServerStatusTimeStamp.setStatus("current")
_CcmSmtpServerStatusInitiate_Type = TruthValue
_CcmSmtpServerStatusInitiate_Object = MibScalar
ccmSmtpServerStatusInitiate = _CcmSmtpServerStatusInitiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 2),
    _CcmSmtpServerStatusInitiate_Type()
)
ccmSmtpServerStatusInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmtpServerStatusInitiate.setStatus("current")


class _CcmSmtpServerStatusResult_Type(Integer32):
    """Custom type ccmSmtpServerStatusResult based on Integer32"""
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
        *(("failed", 4),
          ("inprogress", 3),
          ("noSmtpServerConfigured", 5),
          ("successful", 2),
          ("unknown", 1))
    )


_CcmSmtpServerStatusResult_Type.__name__ = "Integer32"
_CcmSmtpServerStatusResult_Object = MibScalar
ccmSmtpServerStatusResult = _CcmSmtpServerStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 3),
    _CcmSmtpServerStatusResult_Type()
)
ccmSmtpServerStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSmtpServerStatusResult.setStatus("current")
_CcmSmtpServerStatusTable_Object = MibTable
ccmSmtpServerStatusTable = _CcmSmtpServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ccmSmtpServerStatusTable.setStatus("current")
_CcmSmtpServerStatusEntry_Object = MibTableRow
ccmSmtpServerStatusEntry = _CcmSmtpServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 4, 1)
)
ccmSmtpServerStatusEntry.setIndexNames(
    (0, "CISCO-CALLHOME-MIB", "ccmSmtpServersAddrType"),
    (0, "CISCO-CALLHOME-MIB", "ccmSmtpServersAddr"),
)
if mibBuilder.loadTexts:
    ccmSmtpServerStatusEntry.setStatus("current")


class _CcmSmtpServerStatusAvailability_Type(Integer32):
    """Custom type ccmSmtpServerStatusAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2),
          ("unknown", 3))
    )


_CcmSmtpServerStatusAvailability_Type.__name__ = "Integer32"
_CcmSmtpServerStatusAvailability_Object = MibTableColumn
ccmSmtpServerStatusAvailability = _CcmSmtpServerStatusAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 4, 1, 1),
    _CcmSmtpServerStatusAvailability_Type()
)
ccmSmtpServerStatusAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmSmtpServerStatusAvailability.setStatus("current")
_CcmOnDemandMsgServAvailable_Type = TruthValue
_CcmOnDemandMsgServAvailable_Object = MibScalar
ccmOnDemandMsgServAvailable = _CcmOnDemandMsgServAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 3, 5),
    _CcmOnDemandMsgServAvailable_Type()
)
ccmOnDemandMsgServAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmOnDemandMsgServAvailable.setStatus("current")
_CcmCallHomeOnDemandActions_ObjectIdentity = ObjectIdentity
ccmCallHomeOnDemandActions = _CcmCallHomeOnDemandActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4)
)
_CcmOnDemandMsgSendControl_ObjectIdentity = ObjectIdentity
ccmOnDemandMsgSendControl = _CcmOnDemandMsgSendControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 1)
)


class _CcmOnDemandMsgSendAlertGroup_Type(Unsigned32):
    """Custom type ccmOnDemandMsgSendAlertGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CcmOnDemandMsgSendAlertGroup_Type.__name__ = "Unsigned32"
_CcmOnDemandMsgSendAlertGroup_Object = MibScalar
ccmOnDemandMsgSendAlertGroup = _CcmOnDemandMsgSendAlertGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 1, 1),
    _CcmOnDemandMsgSendAlertGroup_Type()
)
ccmOnDemandMsgSendAlertGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandMsgSendAlertGroup.setStatus("current")


class _CcmOnDemandMsgSendProfile_Type(SnmpAdminString):
    """Custom type ccmOnDemandMsgSendProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcmOnDemandMsgSendProfile_Type.__name__ = "SnmpAdminString"
_CcmOnDemandMsgSendProfile_Object = MibScalar
ccmOnDemandMsgSendProfile = _CcmOnDemandMsgSendProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 1, 2),
    _CcmOnDemandMsgSendProfile_Type()
)
ccmOnDemandMsgSendProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandMsgSendProfile.setStatus("current")
_CcmOnDemandMsgSendEntPhyIndex_Type = EntPhysicalIndexOrZero
_CcmOnDemandMsgSendEntPhyIndex_Object = MibScalar
ccmOnDemandMsgSendEntPhyIndex = _CcmOnDemandMsgSendEntPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 1, 3),
    _CcmOnDemandMsgSendEntPhyIndex_Type()
)
ccmOnDemandMsgSendEntPhyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandMsgSendEntPhyIndex.setStatus("current")
_CcmOnDemandMsgSendTrigger_Type = TruthValue
_CcmOnDemandMsgSendTrigger_Object = MibScalar
ccmOnDemandMsgSendTrigger = _CcmOnDemandMsgSendTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 1, 4),
    _CcmOnDemandMsgSendTrigger_Type()
)
ccmOnDemandMsgSendTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandMsgSendTrigger.setStatus("current")
_CcmOnDemandCliMsgControl_ObjectIdentity = ObjectIdentity
ccmOnDemandCliMsgControl = _CcmOnDemandCliMsgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2)
)
_CcmOnDemandCliMsgCliList_Type = SnmpAdminString
_CcmOnDemandCliMsgCliList_Object = MibScalar
ccmOnDemandCliMsgCliList = _CcmOnDemandCliMsgCliList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2, 1),
    _CcmOnDemandCliMsgCliList_Type()
)
ccmOnDemandCliMsgCliList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgCliList.setStatus("current")


class _CcmOnDemandCliMsgTransport_Type(Integer32):
    """Custom type ccmOnDemandCliMsgTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("email", 1),
          ("http", 2))
    )


_CcmOnDemandCliMsgTransport_Type.__name__ = "Integer32"
_CcmOnDemandCliMsgTransport_Object = MibScalar
ccmOnDemandCliMsgTransport = _CcmOnDemandCliMsgTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2, 2),
    _CcmOnDemandCliMsgTransport_Type()
)
ccmOnDemandCliMsgTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgTransport.setStatus("current")
_CcmOnDemandCliMsgEmail_Type = SnmpAdminString
_CcmOnDemandCliMsgEmail_Object = MibScalar
ccmOnDemandCliMsgEmail = _CcmOnDemandCliMsgEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2, 3),
    _CcmOnDemandCliMsgEmail_Type()
)
ccmOnDemandCliMsgEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgEmail.setStatus("current")
_CcmOnDemandCliMsgFormat_Type = CallHomeMsgFormat
_CcmOnDemandCliMsgFormat_Object = MibScalar
ccmOnDemandCliMsgFormat = _CcmOnDemandCliMsgFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2, 4),
    _CcmOnDemandCliMsgFormat_Type()
)
ccmOnDemandCliMsgFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgFormat.setStatus("current")
_CcmOnDemandCliMsgTacServiceReqId_Type = SnmpAdminString
_CcmOnDemandCliMsgTacServiceReqId_Object = MibScalar
ccmOnDemandCliMsgTacServiceReqId = _CcmOnDemandCliMsgTacServiceReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2, 5),
    _CcmOnDemandCliMsgTacServiceReqId_Type()
)
ccmOnDemandCliMsgTacServiceReqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgTacServiceReqId.setStatus("current")
_CcmOnDemandCliMsgTrigger_Type = TruthValue
_CcmOnDemandCliMsgTrigger_Object = MibScalar
ccmOnDemandCliMsgTrigger = _CcmOnDemandCliMsgTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 4, 2, 6),
    _CcmOnDemandCliMsgTrigger_Type()
)
ccmOnDemandCliMsgTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgTrigger.setStatus("current")
_CcmSmartCallHomeActions_ObjectIdentity = ObjectIdentity
ccmSmartCallHomeActions = _CcmSmartCallHomeActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 5)
)


class _CcmSmartCallHomeProfile_Type(SnmpAdminString):
    """Custom type ccmSmartCallHomeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcmSmartCallHomeProfile_Type.__name__ = "SnmpAdminString"
_CcmSmartCallHomeProfile_Object = MibScalar
ccmSmartCallHomeProfile = _CcmSmartCallHomeProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 5, 1),
    _CcmSmartCallHomeProfile_Type()
)
ccmSmartCallHomeProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmartCallHomeProfile.setStatus("current")


class _CcmSmartCallHomeServiceType_Type(Integer32):
    """Custom type ccmSmartCallHomeServiceType based on Integer32"""
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
        *(("bugsList", 3),
          ("commandReference", 1),
          ("configSanity", 2),
          ("outputAnalysis", 4),
          ("productAdvisory", 5))
    )


_CcmSmartCallHomeServiceType_Type.__name__ = "Integer32"
_CcmSmartCallHomeServiceType_Object = MibScalar
ccmSmartCallHomeServiceType = _CcmSmartCallHomeServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 5, 2),
    _CcmSmartCallHomeServiceType_Type()
)
ccmSmartCallHomeServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmartCallHomeServiceType.setStatus("current")
_CcmSmartCallHomeAnalysisCmd_Type = SnmpAdminString
_CcmSmartCallHomeAnalysisCmd_Object = MibScalar
ccmSmartCallHomeAnalysisCmd = _CcmSmartCallHomeAnalysisCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 5, 3),
    _CcmSmartCallHomeAnalysisCmd_Type()
)
ccmSmartCallHomeAnalysisCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmartCallHomeAnalysisCmd.setStatus("current")
_CcmSmartCallHomeCcoId_Type = SnmpAdminString
_CcmSmartCallHomeCcoId_Object = MibScalar
ccmSmartCallHomeCcoId = _CcmSmartCallHomeCcoId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 5, 4),
    _CcmSmartCallHomeCcoId_Type()
)
ccmSmartCallHomeCcoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmartCallHomeCcoId.setStatus("current")
_CcmSmartCallHomeTrigger_Type = TruthValue
_CcmSmartCallHomeTrigger_Object = MibScalar
ccmSmartCallHomeTrigger = _CcmSmartCallHomeTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 5, 5),
    _CcmSmartCallHomeTrigger_Type()
)
ccmSmartCallHomeTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmSmartCallHomeTrigger.setStatus("current")
_CcmCallHomeVrf_ObjectIdentity = ObjectIdentity
ccmCallHomeVrf = _CcmCallHomeVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 6)
)
_CcmCallHomeVrfName_Type = CiscoVrfName
_CcmCallHomeVrfName_Object = MibScalar
ccmCallHomeVrfName = _CcmCallHomeVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 6, 1),
    _CcmCallHomeVrfName_Type()
)
ccmCallHomeVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCallHomeVrfName.setStatus("current")
_CcmCallHomeMessageSource_ObjectIdentity = ObjectIdentity
ccmCallHomeMessageSource = _CcmCallHomeMessageSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 7)
)
_CcmMsgSourceIpAddrType_Type = InetAddressType
_CcmMsgSourceIpAddrType_Object = MibScalar
ccmMsgSourceIpAddrType = _CcmMsgSourceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 7, 1),
    _CcmMsgSourceIpAddrType_Type()
)
ccmMsgSourceIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmMsgSourceIpAddrType.setStatus("current")
_CcmMsgSourceIpAddr_Type = InetAddress
_CcmMsgSourceIpAddr_Object = MibScalar
ccmMsgSourceIpAddr = _CcmMsgSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 7, 2),
    _CcmMsgSourceIpAddr_Type()
)
ccmMsgSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmMsgSourceIpAddr.setStatus("current")
_CcmMsgSourceInterface_Type = InterfaceIndexOrZero
_CcmMsgSourceInterface_Object = MibScalar
ccmMsgSourceInterface = _CcmMsgSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 7, 3),
    _CcmMsgSourceInterface_Type()
)
ccmMsgSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmMsgSourceInterface.setStatus("current")
_CcmCallhomeEvents_ObjectIdentity = ObjectIdentity
ccmCallhomeEvents = _CcmCallhomeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 8)
)
_CcmEventDescription_Type = SnmpAdminString
_CcmEventDescription_Object = MibScalar
ccmEventDescription = _CcmEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 8, 1),
    _CcmEventDescription_Type()
)
ccmEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmEventDescription.setStatus("current")
_CcmEventTime_Type = TimeStamp
_CcmEventTime_Object = MibScalar
ccmEventTime = _CcmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 8, 2),
    _CcmEventTime_Type()
)
ccmEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmEventTime.setStatus("current")
_CcmEventUrgencyLevel_Type = CallHomeMsgLevel
_CcmEventUrgencyLevel_Object = MibScalar
ccmEventUrgencyLevel = _CcmEventUrgencyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 8, 3),
    _CcmEventUrgencyLevel_Type()
)
ccmEventUrgencyLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccmEventUrgencyLevel.setStatus("current")
_CcmCallHomeDiagSignature_ObjectIdentity = ObjectIdentity
ccmCallHomeDiagSignature = _CcmCallHomeDiagSignature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9)
)
_CcmDiagSignatureActive_Type = TruthValue
_CcmDiagSignatureActive_Object = MibScalar
ccmDiagSignatureActive = _CcmDiagSignatureActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 1),
    _CcmDiagSignatureActive_Type()
)
ccmDiagSignatureActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmDiagSignatureActive.setStatus("current")


class _CcmDiagSignatureProfileName_Type(SnmpAdminString):
    """Custom type ccmDiagSignatureProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcmDiagSignatureProfileName_Type.__name__ = "SnmpAdminString"
_CcmDiagSignatureProfileName_Object = MibScalar
ccmDiagSignatureProfileName = _CcmDiagSignatureProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 2),
    _CcmDiagSignatureProfileName_Type()
)
ccmDiagSignatureProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmDiagSignatureProfileName.setStatus("current")
_CcmCallHomeDiagSignatureInfoTable_Object = MibTable
ccmCallHomeDiagSignatureInfoTable = _CcmCallHomeDiagSignatureInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3)
)
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureInfoTable.setStatus("current")
_CcmCallHomeDiagSignatureInfoEntry_Object = MibTableRow
ccmCallHomeDiagSignatureInfoEntry = _CcmCallHomeDiagSignatureInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1)
)
ccmCallHomeDiagSignatureInfoEntry.setIndexNames(
    (1, "CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureName"),
)
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureInfoEntry.setStatus("current")


class _CcmCallHomeDiagSignatureName_Type(SnmpAdminString):
    """Custom type ccmCallHomeDiagSignatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CcmCallHomeDiagSignatureName_Type.__name__ = "SnmpAdminString"
_CcmCallHomeDiagSignatureName_Object = MibTableColumn
ccmCallHomeDiagSignatureName = _CcmCallHomeDiagSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 1),
    _CcmCallHomeDiagSignatureName_Type()
)
ccmCallHomeDiagSignatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureName.setStatus("current")


class _CcmCallHomeDiagSignatureType_Type(Integer32):
    """Custom type ccmCallHomeDiagSignatureType based on Integer32"""
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
        *(("applet", 3),
          ("meta", 1),
          ("mixed", 4),
          ("tcl", 2))
    )


_CcmCallHomeDiagSignatureType_Type.__name__ = "Integer32"
_CcmCallHomeDiagSignatureType_Object = MibTableColumn
ccmCallHomeDiagSignatureType = _CcmCallHomeDiagSignatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 2),
    _CcmCallHomeDiagSignatureType_Type()
)
ccmCallHomeDiagSignatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureType.setStatus("current")
_CcmCallHomeDiagSignatureFuncDescr_Type = SnmpAdminString
_CcmCallHomeDiagSignatureFuncDescr_Object = MibTableColumn
ccmCallHomeDiagSignatureFuncDescr = _CcmCallHomeDiagSignatureFuncDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 3),
    _CcmCallHomeDiagSignatureFuncDescr_Type()
)
ccmCallHomeDiagSignatureFuncDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureFuncDescr.setStatus("current")
_CcmCallHomeDiagSignatureRev_Type = SnmpAdminString
_CcmCallHomeDiagSignatureRev_Object = MibTableColumn
ccmCallHomeDiagSignatureRev = _CcmCallHomeDiagSignatureRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 4),
    _CcmCallHomeDiagSignatureRev_Type()
)
ccmCallHomeDiagSignatureRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureRev.setStatus("current")


class _CcmCallHomeDiagSignatureSigner_Type(Integer32):
    """Custom type ccmCallHomeDiagSignatureSigner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cisco", 1),
          ("partner", 2),
          ("thirdParty", 3))
    )


_CcmCallHomeDiagSignatureSigner_Type.__name__ = "Integer32"
_CcmCallHomeDiagSignatureSigner_Object = MibTableColumn
ccmCallHomeDiagSignatureSigner = _CcmCallHomeDiagSignatureSigner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 5),
    _CcmCallHomeDiagSignatureSigner_Type()
)
ccmCallHomeDiagSignatureSigner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureSigner.setStatus("current")
_CcmCallHomeDiagSignatureTriggerCount_Type = Counter32
_CcmCallHomeDiagSignatureTriggerCount_Object = MibTableColumn
ccmCallHomeDiagSignatureTriggerCount = _CcmCallHomeDiagSignatureTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 6),
    _CcmCallHomeDiagSignatureTriggerCount_Type()
)
ccmCallHomeDiagSignatureTriggerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureTriggerCount.setStatus("current")
_CcmCallHomeDiagSignatureAvgRuntime_Type = Unsigned32
_CcmCallHomeDiagSignatureAvgRuntime_Object = MibTableColumn
ccmCallHomeDiagSignatureAvgRuntime = _CcmCallHomeDiagSignatureAvgRuntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 7),
    _CcmCallHomeDiagSignatureAvgRuntime_Type()
)
ccmCallHomeDiagSignatureAvgRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureAvgRuntime.setStatus("current")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureAvgRuntime.setUnits("milli seconds")
_CcmCallHomeDiagSignatureMaxRuntime_Type = Unsigned32
_CcmCallHomeDiagSignatureMaxRuntime_Object = MibTableColumn
ccmCallHomeDiagSignatureMaxRuntime = _CcmCallHomeDiagSignatureMaxRuntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 9, 3, 1, 8),
    _CcmCallHomeDiagSignatureMaxRuntime_Type()
)
ccmCallHomeDiagSignatureMaxRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureMaxRuntime.setStatus("current")
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureMaxRuntime.setUnits("milli seconds")
_CcmCallHomeSecurity_ObjectIdentity = ObjectIdentity
ccmCallHomeSecurity = _CcmCallHomeSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 10)
)


class _CcmCallHomeSecurityLevel_Type(Integer32):
    """Custom type ccmCallHomeSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_CcmCallHomeSecurityLevel_Type.__name__ = "Integer32"
_CcmCallHomeSecurityLevel_Object = MibScalar
ccmCallHomeSecurityLevel = _CcmCallHomeSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 10, 1),
    _CcmCallHomeSecurityLevel_Type()
)
ccmCallHomeSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCallHomeSecurityLevel.setStatus("current")
_CcmCallHomeReporting_ObjectIdentity = ObjectIdentity
ccmCallHomeReporting = _CcmCallHomeReporting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 11)
)
_CcmAnonymousReportingEnable_Type = TruthValue
_CcmAnonymousReportingEnable_Object = MibScalar
ccmAnonymousReportingEnable = _CcmAnonymousReportingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 11, 1),
    _CcmAnonymousReportingEnable_Type()
)
ccmAnonymousReportingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmAnonymousReportingEnable.setStatus("current")
_CcmCallHomeHttpProxy_ObjectIdentity = ObjectIdentity
ccmCallHomeHttpProxy = _CcmCallHomeHttpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 12)
)
_CcmCallHomeAaa_ObjectIdentity = ObjectIdentity
ccmCallHomeAaa = _CcmCallHomeAaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 13)
)
_CcmAaaAuthEnable_Type = TruthValue
_CcmAaaAuthEnable_Object = MibScalar
ccmAaaAuthEnable = _CcmAaaAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 13, 1),
    _CcmAaaAuthEnable_Type()
)
ccmAaaAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmAaaAuthEnable.setStatus("current")
_CcmAaaAuthUserName_Type = SnmpAdminString
_CcmAaaAuthUserName_Object = MibScalar
ccmAaaAuthUserName = _CcmAaaAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 1, 13, 2),
    _CcmAaaAuthUserName_Type()
)
ccmAaaAuthUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmAaaAuthUserName.setStatus("current")
_ChMIBConformance_ObjectIdentity = ObjectIdentity
chMIBConformance = _ChMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2)
)
_ChMIBCompliances_ObjectIdentity = ObjectIdentity
chMIBCompliances = _ChMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1)
)
_ChMIBGroups_ObjectIdentity = ObjectIdentity
chMIBGroups = _ChMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2)
)

# Managed Objects groups

chSystemInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 1)
)
chSystemInformationGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "sysContactPhoneNumber"),
        ("CISCO-CALLHOME-MIB", "sysContactEmailAddress"),
        ("CISCO-CALLHOME-MIB", "sysStreetAddress"),
        ("CISCO-CALLHOME-MIB", "callHomeCustomerId"),
        ("CISCO-CALLHOME-MIB", "callHomeContractId"),
        ("CISCO-CALLHOME-MIB", "callHomeSiteId"),
        ("CISCO-CALLHOME-MIB", "callHomeDeviceServicePriority"))
)
if mibBuilder.loadTexts:
    chSystemInformationGroup.setStatus("deprecated")

chConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 2)
)
chConfigurationGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeEnable"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertAction"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionFailureCause"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgFormat"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMaxMsgSize"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileTrnsprtMthd"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailAddrTblMaxEntries"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddress"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddressStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailFrom"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailReplyTo"))
)
if mibBuilder.loadTexts:
    chConfigurationGroup.setStatus("deprecated")

chEmailMsgDispGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 3)
)
chEmailMsgDispGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeEmailMsgDispNotification")
)
if mibBuilder.loadTexts:
    chEmailMsgDispGroup.setStatus("current")

chSingleSmtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 4)
)
chSingleSmtpServerGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeSmtpServerAddrType"),
        ("CISCO-CALLHOME-MIB", "callHomeSmtpServerAddr"),
        ("CISCO-CALLHOME-MIB", "callHomeSmtpServerPort"))
)
if mibBuilder.loadTexts:
    chSingleSmtpServerGroup.setStatus("deprecated")

chMultipleSmtpServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 5)
)
chMultipleSmtpServersGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmSmtpServersTblMaxEntries"),
        ("CISCO-CALLHOME-MIB", "ccmSmtpServersPort"),
        ("CISCO-CALLHOME-MIB", "ccmSmtpServersStatus"))
)
if mibBuilder.loadTexts:
    chMultipleSmtpServersGroup.setStatus("current")

chStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 6)
)
chStatisticsGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeLastAlertSent"),
        ("CISCO-CALLHOME-MIB", "callHomeAlerts"))
)
if mibBuilder.loadTexts:
    chStatisticsGroup.setStatus("current")

ccmSysLogSeverityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 7)
)
ccmSysLogSeverityGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSysLogSeverity")
)
if mibBuilder.loadTexts:
    ccmSysLogSeverityGroup.setStatus("current")

ccmMIBNotificationsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 8)
)
ccmMIBNotificationsConfigGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmEnableSmtpServerNotif")
)
if mibBuilder.loadTexts:
    ccmMIBNotificationsConfigGroup.setStatus("current")

chConfigurationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 10)
)
chConfigurationGroup1.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeEnable"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertAction"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionFailureCause"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgFormat"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMaxMsgSize"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileTrnsprtMthd"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgLevel"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileAlertGroups"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailAddrTblMaxEntries"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddress"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddressStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailFrom"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailReplyTo"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertGroupName"))
)
if mibBuilder.loadTexts:
    chConfigurationGroup1.setStatus("deprecated")

chConfigurationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 12)
)
chConfigurationGroup2.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeEnable"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertAction"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionFailureCause"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgFormat"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMaxMsgSize"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileTrnsprtMthd"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgLevel"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileAlertGroups"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailAddrTblMaxEntries"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddress"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddressStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailFrom"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailReplyTo"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertGroupName"),
        ("CISCO-CALLHOME-MIB", "ccmMsgThrottlingEnable"))
)
if mibBuilder.loadTexts:
    chConfigurationGroup2.setStatus("deprecated")

chSwInventoryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 13)
)
chSwInventoryInfoGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeInventoryInfoName"),
        ("CISCO-CALLHOME-MIB", "callHomeInventoryInfoValue"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicSwInventoryMsgEnable"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicSwInventoryTimeFrame"))
)
if mibBuilder.loadTexts:
    chSwInventoryInfoGroup.setStatus("deprecated")

chPeriodicSwInventoryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 14)
)
chPeriodicSwInventoryInfoGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmPeriodicSwInventoryMsgEnable"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicSwInventoryTimeFrame"))
)
if mibBuilder.loadTexts:
    chPeriodicSwInventoryInfoGroup.setStatus("current")

chSwInventoryInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 15)
)
chSwInventoryInfoGroup1.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeInventoryInfoName"),
        ("CISCO-CALLHOME-MIB", "callHomeInventoryInfoValue"))
)
if mibBuilder.loadTexts:
    chSwInventoryInfoGroup1.setStatus("current")

ccmUserDefCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 16)
)
ccmUserDefCmdGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeUserDefMaxCmds"),
        ("CISCO-CALLHOME-MIB", "callHomeUserDefCmdName"),
        ("CISCO-CALLHOME-MIB", "callHomeUserDefCmdRowStatus"))
)
if mibBuilder.loadTexts:
    ccmUserDefCmdGroup.setStatus("current")

ccmPeriodicSwInventoryInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 17)
)
ccmPeriodicSwInventoryInfoGroup1.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmPeriodicSwInventoryTimeOfDay")
)
if mibBuilder.loadTexts:
    ccmPeriodicSwInventoryInfoGroup1.setStatus("current")

ccmConfigurationGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 18)
)
ccmConfigurationGroup3.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeEnable"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgFormat"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileTrnsprtMthd"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeDestProfileMaxMsgSize"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailAddrTblMaxEntries"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddress"),
        ("CISCO-CALLHOME-MIB", "callHomeDestEmailAddressStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailFrom"),
        ("CISCO-CALLHOME-MIB", "callHomeEmailReplyTo"))
)
if mibBuilder.loadTexts:
    ccmConfigurationGroup3.setStatus("current")

ccmAlertActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 19)
)
ccmAlertActionGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeAlertAction"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionStatus"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertActionFailureCause"))
)
if mibBuilder.loadTexts:
    ccmAlertActionGroup.setStatus("current")

ccmProfileMessageLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 20)
)
ccmProfileMessageLevelGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeDestProfileMsgLevel")
)
if mibBuilder.loadTexts:
    ccmProfileMessageLevelGroup.setStatus("current")

ccmProfileActivationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 21)
)
ccmProfileActivationGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeDestProfileActive")
)
if mibBuilder.loadTexts:
    ccmProfileActivationGroup.setStatus("current")

ccmProfileTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 22)
)
ccmProfileTestGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmDestProfileTestTrigger"),
        ("CISCO-CALLHOME-MIB", "ccmDestProfileTestMessage"),
        ("CISCO-CALLHOME-MIB", "ccmDestProfileTestStatus"),
        ("CISCO-CALLHOME-MIB", "ccmDestProfileTestFailureCause"))
)
if mibBuilder.loadTexts:
    ccmProfileTestGroup.setStatus("current")

ccmProfileAlertGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 23)
)
ccmProfileAlertGroupsGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeDestProfileAlertGroups"),
        ("CISCO-CALLHOME-MIB", "callHomeAlertGroupName"))
)
if mibBuilder.loadTexts:
    ccmProfileAlertGroupsGroup.setStatus("current")

ccmProfileAlertGroupControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 24)
)
ccmProfileAlertGroupControlGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeAlertGroupEnable")
)
if mibBuilder.loadTexts:
    ccmProfileAlertGroupControlGroup.setStatus("current")

ccmThrottleConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 25)
)
ccmThrottleConfigurationGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmMsgThrottlingEnable")
)
if mibBuilder.loadTexts:
    ccmThrottleConfigurationGroup.setStatus("current")

ccmSmtpServersPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 26)
)
ccmSmtpServersPriorityGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSmtpServersPriority")
)
if mibBuilder.loadTexts:
    ccmSmtpServersPriorityGroup.setStatus("current")

ccmAlertGroupCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 27)
)
ccmAlertGroupCapabilityGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeAlertGroupCapability")
)
if mibBuilder.loadTexts:
    ccmAlertGroupCapabilityGroup.setStatus("current")

ccmHttpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 28)
)
ccmHttpCfgGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeDestType"),
        ("CISCO-CALLHOME-MIB", "callHomeDestHttpUrl"))
)
if mibBuilder.loadTexts:
    ccmHttpCfgGroup.setStatus("current")

ccmSeverityAlertGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 29)
)
ccmSeverityAlertGroupCfgGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmAlertGroupSeverity")
)
if mibBuilder.loadTexts:
    ccmSeverityAlertGroupCfgGroup.setStatus("current")

ccmPeriodicAlertGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 30)
)
ccmPeriodicAlertGroupCfgGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupInterval"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupDayOfWeek"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupDayOfMonth"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupHour"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupMinute"),
        ("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupEnable"))
)
if mibBuilder.loadTexts:
    ccmPeriodicAlertGroupCfgGroup.setStatus("current")

ccmPatternAlertGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 31)
)
ccmPatternAlertGroupCfgGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmMaxSyslogAlertGroupPatterns"),
        ("CISCO-CALLHOME-MIB", "ccmPatternAlertGroupSeverity"),
        ("CISCO-CALLHOME-MIB", "ccmPatternAlertGroupStorage"),
        ("CISCO-CALLHOME-MIB", "ccmPatternAlertGroupStatus"))
)
if mibBuilder.loadTexts:
    ccmPatternAlertGroupCfgGroup.setStatus("current")

ccmEventAlertGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 32)
)
ccmEventAlertGroupCfgGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmEventAlertGroupEnable"),
        ("CISCO-CALLHOME-MIB", "ccmEventAlertGroupOperSeverity"))
)
if mibBuilder.loadTexts:
    ccmEventAlertGroupCfgGroup.setStatus("current")

ccmSmtpMsgSendFailNotifCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 33)
)
ccmSmtpMsgSendFailNotifCtrlGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSmtpMsgSendFailNotifEnable")
)
if mibBuilder.loadTexts:
    ccmSmtpMsgSendFailNotifCtrlGroup.setStatus("current")

ccmAlertHCStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 35)
)
ccmAlertHCStatisticsGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeHCAlerts")
)
if mibBuilder.loadTexts:
    ccmAlertHCStatisticsGroup.setStatus("current")

ccmAlertRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 36)
)
ccmAlertRateLimitGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmAlertsDropped"),
        ("CISCO-CALLHOME-MIB", "ccmAlertRateLimit"))
)
if mibBuilder.loadTexts:
    ccmAlertRateLimitGroup.setStatus("current")

ccmSmtpServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 37)
)
ccmSmtpServerStatusGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmSmtpServerStatusTimeStamp"),
        ("CISCO-CALLHOME-MIB", "ccmSmtpServerStatusInitiate"),
        ("CISCO-CALLHOME-MIB", "ccmSmtpServerStatusResult"),
        ("CISCO-CALLHOME-MIB", "ccmSmtpServerStatusAvailability"))
)
if mibBuilder.loadTexts:
    ccmSmtpServerStatusGroup.setStatus("current")

ccmProfileHiMessageSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 38)
)
ccmProfileHiMessageSizeGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeDestProfileHiMaxMsgSize")
)
if mibBuilder.loadTexts:
    ccmProfileHiMessageSizeGroup.setStatus("current")

chSystemInformationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 39)
)
chSystemInformationGroup1.setObjects(
      *(("CISCO-CALLHOME-MIB", "sysContactPhoneNumber"),
        ("CISCO-CALLHOME-MIB", "sysContactEmailAddress"),
        ("CISCO-CALLHOME-MIB", "sysStreetAddress"),
        ("CISCO-CALLHOME-MIB", "callHomeCustomerId"),
        ("CISCO-CALLHOME-MIB", "callHomeContractId"),
        ("CISCO-CALLHOME-MIB", "callHomeSiteId"))
)
if mibBuilder.loadTexts:
    chSystemInformationGroup1.setStatus("current")

chSystemServicePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 40)
)
chSystemServicePriorityGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeDeviceServicePriority")
)
if mibBuilder.loadTexts:
    chSystemServicePriorityGroup.setStatus("current")

ccmOnDemandMsgSendControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 41)
)
ccmOnDemandMsgSendControlGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmOnDemandMsgSendAlertGroup"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandMsgSendProfile"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandMsgSendEntPhyIndex"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandMsgSendTrigger"))
)
if mibBuilder.loadTexts:
    ccmOnDemandMsgSendControlGroup.setStatus("current")

ccmOnDemandMsgStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 42)
)
ccmOnDemandMsgStatusGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmOnDemandMsgServAvailable")
)
if mibBuilder.loadTexts:
    ccmOnDemandMsgStatusGroup.setStatus("current")

ccmSmartCallHomeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 43)
)
ccmSmartCallHomeGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmSmartCallHomeProfile"),
        ("CISCO-CALLHOME-MIB", "ccmSmartCallHomeServiceType"),
        ("CISCO-CALLHOME-MIB", "ccmSmartCallHomeAnalysisCmd"),
        ("CISCO-CALLHOME-MIB", "ccmSmartCallHomeCcoId"),
        ("CISCO-CALLHOME-MIB", "ccmSmartCallHomeTrigger"))
)
if mibBuilder.loadTexts:
    ccmSmartCallHomeGroup.setStatus("current")

ccmEventStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 44)
)
ccmEventStatsGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmEventStatsTotal"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsConfiguration"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsDiagnostic"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsEnvironment"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsInventory"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsSystemLog"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsTest"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsRequest"),
        ("CISCO-CALLHOME-MIB", "ccmEventStatsSendCliOutput"))
)
if mibBuilder.loadTexts:
    ccmEventStatsGroup.setStatus("current")

ccmCallhomeEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 46)
)
ccmCallhomeEventsGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmEventDescription"),
        ("CISCO-CALLHOME-MIB", "ccmEventTime"),
        ("CISCO-CALLHOME-MIB", "ccmEventUrgencyLevel"))
)
if mibBuilder.loadTexts:
    ccmCallhomeEventsGroup.setStatus("current")

ccmCallHomeVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 47)
)
ccmCallHomeVrfGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmCallHomeVrfName")
)
if mibBuilder.loadTexts:
    ccmCallHomeVrfGroup.setStatus("current")

ccmSmtpServersVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 48)
)
ccmSmtpServersVrfGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSmtpServersUseVrf")
)
if mibBuilder.loadTexts:
    ccmSmtpServersVrfGroup.setStatus("current")

ccmHttpProxyServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 49)
)
ccmHttpProxyServerGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmHttpProxyServerAddrType"),
        ("CISCO-CALLHOME-MIB", "ccmHttpProxyServerAddr"),
        ("CISCO-CALLHOME-MIB", "ccmHttpProxyServerPort"),
        ("CISCO-CALLHOME-MIB", "ccmHttpProxyServerUseEnable"))
)
if mibBuilder.loadTexts:
    ccmHttpProxyServerGroup.setStatus("current")

ccmHttpTransportVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 50)
)
ccmHttpTransportVrfGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmHttpTransportUseVrf")
)
if mibBuilder.loadTexts:
    ccmHttpTransportVrfGroup.setStatus("current")

ccmSingleSmtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 51)
)
ccmSingleSmtpServerGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "callHomeSmtpServerAddrType"),
        ("CISCO-CALLHOME-MIB", "callHomeSmtpServerAddr"),
        ("CISCO-CALLHOME-MIB", "callHomeSmtpServerPort"),
        ("CISCO-CALLHOME-MIB", "callHomeSmtpServerUseVrf"))
)
if mibBuilder.loadTexts:
    ccmSingleSmtpServerGroup.setStatus("current")

ccmMessageSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 52)
)
ccmMessageSourceGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmMsgSourceIpAddrType"),
        ("CISCO-CALLHOME-MIB", "ccmMsgSourceIpAddr"),
        ("CISCO-CALLHOME-MIB", "ccmMsgSourceInterface"))
)
if mibBuilder.loadTexts:
    ccmMessageSourceGroup.setStatus("current")

ccmCallHomePeriodicMinutesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 53)
)
ccmCallHomePeriodicMinutesGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmPeriodicAlertGroupIntervalMinutes")
)
if mibBuilder.loadTexts:
    ccmCallHomePeriodicMinutesGroup.setStatus("current")

ccmOnDemandCliMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 54)
)
ccmOnDemandCliMsgGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmOnDemandCliMsgCliList"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandCliMsgTransport"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandCliMsgEmail"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandCliMsgFormat"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandCliMsgTacServiceReqId"),
        ("CISCO-CALLHOME-MIB", "ccmOnDemandCliMsgTrigger"))
)
if mibBuilder.loadTexts:
    ccmOnDemandCliMsgGroup.setStatus("current")

ccmCallHomeDiagSignatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 55)
)
ccmCallHomeDiagSignatureGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmDiagSignatureActive"),
        ("CISCO-CALLHOME-MIB", "ccmDiagSignatureProfileName"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureType"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureFuncDescr"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureRev"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureSigner"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureTriggerCount"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureAvgRuntime"),
        ("CISCO-CALLHOME-MIB", "ccmCallHomeDiagSignatureMaxRuntime"))
)
if mibBuilder.loadTexts:
    ccmCallHomeDiagSignatureGroup.setStatus("current")

ccmCallHomeSecurityLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 56)
)
ccmCallHomeSecurityLevelGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmCallHomeSecurityLevel")
)
if mibBuilder.loadTexts:
    ccmCallHomeSecurityLevelGroup.setStatus("current")

ccmCallHomeAnonymousReportingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 57)
)
ccmCallHomeAnonymousReportingGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmAnonymousReportingEnable")
)
if mibBuilder.loadTexts:
    ccmCallHomeAnonymousReportingGroup.setStatus("current")

ccmCallHomeAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 58)
)
ccmCallHomeAaaGroup.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmAaaAuthEnable"),
        ("CISCO-CALLHOME-MIB", "ccmAaaAuthUserName"))
)
if mibBuilder.loadTexts:
    ccmCallHomeAaaGroup.setStatus("current")


# Notification objects

ccmSmtpServerFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 0, 1)
)
ccmSmtpServerFailNotif.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSmtpServersPort")
)
if mibBuilder.loadTexts:
    ccmSmtpServerFailNotif.setStatus(
        "current"
    )

ccmAlertGroupTypeAddedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 0, 2)
)
ccmAlertGroupTypeAddedNotif.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeAlertGroupName")
)
if mibBuilder.loadTexts:
    ccmAlertGroupTypeAddedNotif.setStatus(
        "current"
    )

ccmAlertGroupTypeDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 0, 3)
)
ccmAlertGroupTypeDeletedNotif.setObjects(
    ("CISCO-CALLHOME-MIB", "callHomeAlertGroupName")
)
if mibBuilder.loadTexts:
    ccmAlertGroupTypeDeletedNotif.setStatus(
        "current"
    )

ccmSmtpMsgSendFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 0, 4)
)
if mibBuilder.loadTexts:
    ccmSmtpMsgSendFailNotif.setStatus(
        "current"
    )

ccmEventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 0, 5)
)
ccmEventNotif.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CISCO-CALLHOME-MIB", "ccmEventDescription"),
        ("CISCO-CALLHOME-MIB", "ccmEventTime"),
        ("CISCO-CALLHOME-MIB", "ccmEventUrgencyLevel"))
)
if mibBuilder.loadTexts:
    ccmEventNotif.setStatus(
        "current"
    )


# Notifications groups

ccmMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 9)
)
ccmMIBNotificationsGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSmtpServerFailNotif")
)
if mibBuilder.loadTexts:
    ccmMIBNotificationsGroup.setStatus(
        "deprecated"
    )

ccmMIBNotificationsGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 11)
)
ccmMIBNotificationsGroup1.setObjects(
      *(("CISCO-CALLHOME-MIB", "ccmSmtpServerFailNotif"),
        ("CISCO-CALLHOME-MIB", "ccmAlertGroupTypeAddedNotif"),
        ("CISCO-CALLHOME-MIB", "ccmAlertGroupTypeDeletedNotif"))
)
if mibBuilder.loadTexts:
    ccmMIBNotificationsGroup1.setStatus(
        "current"
    )

ccmSmtpMsgSendFailNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 34)
)
ccmSmtpMsgSendFailNotifGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmSmtpMsgSendFailNotif")
)
if mibBuilder.loadTexts:
    ccmSmtpMsgSendFailNotifGroup.setStatus(
        "current"
    )

ccmEventNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 2, 45)
)
ccmEventNotifGroup.setObjects(
    ("CISCO-CALLHOME-MIB", "ccmEventNotif")
)
if mibBuilder.loadTexts:
    ccmEventNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

chMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chMIBCompliance.setStatus(
        "deprecated"
    )

chMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 2)
)
if mibBuilder.loadTexts:
    chMIBCompliance1.setStatus(
        "deprecated"
    )

chMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 3)
)
if mibBuilder.loadTexts:
    chMIBCompliance2.setStatus(
        "deprecated"
    )

chMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 4)
)
if mibBuilder.loadTexts:
    chMIBCompliance3.setStatus(
        "deprecated"
    )

chMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 5)
)
if mibBuilder.loadTexts:
    chMIBCompliance4.setStatus(
        "deprecated"
    )

chMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 6)
)
if mibBuilder.loadTexts:
    chMIBCompliance5.setStatus(
        "deprecated"
    )

chMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 7)
)
if mibBuilder.loadTexts:
    chMIBCompliance6.setStatus(
        "deprecated"
    )

chMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 8)
)
if mibBuilder.loadTexts:
    chMIBCompliance7.setStatus(
        "deprecated"
    )

chMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 9)
)
if mibBuilder.loadTexts:
    chMIBCompliance8.setStatus(
        "deprecated"
    )

chMIBCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300, 2, 1, 10)
)
if mibBuilder.loadTexts:
    chMIBCompliance9.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALLHOME-MIB",
    **{"CallHomeAlert": CallHomeAlert,
       "CallHomeMsgFormat": CallHomeMsgFormat,
       "CallHomeTransportMethod": CallHomeTransportMethod,
       "CallHomeMsgLevel": CallHomeMsgLevel,
       "AlertGroupList": AlertGroupList,
       "ciscoCallHomeMIB": ciscoCallHomeMIB,
       "ccmCallHomeNotifications": ccmCallHomeNotifications,
       "ccmSmtpServerFailNotif": ccmSmtpServerFailNotif,
       "ccmAlertGroupTypeAddedNotif": ccmAlertGroupTypeAddedNotif,
       "ccmAlertGroupTypeDeletedNotif": ccmAlertGroupTypeDeletedNotif,
       "ccmSmtpMsgSendFailNotif": ccmSmtpMsgSendFailNotif,
       "ccmEventNotif": ccmEventNotif,
       "ciscoCallHomeMIBObjects": ciscoCallHomeMIBObjects,
       "ccmCallHomeConfiguration": ccmCallHomeConfiguration,
       "callHomeEnable": callHomeEnable,
       "sysContactPhoneNumber": sysContactPhoneNumber,
       "sysContactEmailAddress": sysContactEmailAddress,
       "sysStreetAddress": sysStreetAddress,
       "callHomeCustomerId": callHomeCustomerId,
       "callHomeContractId": callHomeContractId,
       "callHomeSiteId": callHomeSiteId,
       "callHomeDeviceServicePriority": callHomeDeviceServicePriority,
       "callHomeAlertAction": callHomeAlertAction,
       "callHomeAlertActionStatus": callHomeAlertActionStatus,
       "callHomeAlertActionFailureCause": callHomeAlertActionFailureCause,
       "callHomeDestProfileTable": callHomeDestProfileTable,
       "callHomeDestProfileEntry": callHomeDestProfileEntry,
       "callHomeDestProfileName": callHomeDestProfileName,
       "callHomeDestProfileMsgFormat": callHomeDestProfileMsgFormat,
       "callHomeDestProfileMaxMsgSize": callHomeDestProfileMaxMsgSize,
       "callHomeDestProfileTrnsprtMthd": callHomeDestProfileTrnsprtMthd,
       "callHomeDestProfileStatus": callHomeDestProfileStatus,
       "callHomeDestProfileMsgLevel": callHomeDestProfileMsgLevel,
       "callHomeDestProfileAlertGroups": callHomeDestProfileAlertGroups,
       "callHomeDestProfileActive": callHomeDestProfileActive,
       "callHomeDestProfileHiMaxMsgSize": callHomeDestProfileHiMaxMsgSize,
       "callHomeEmailAddrTblMaxEntries": callHomeEmailAddrTblMaxEntries,
       "callHomeDestEmailAddressTable": callHomeDestEmailAddressTable,
       "callHomeDestEmailAddressEntry": callHomeDestEmailAddressEntry,
       "callHomeDestEmailAddressIndex": callHomeDestEmailAddressIndex,
       "callHomeDestEmailAddress": callHomeDestEmailAddress,
       "callHomeDestEmailAddressStatus": callHomeDestEmailAddressStatus,
       "callHomeDestType": callHomeDestType,
       "callHomeDestHttpUrl": callHomeDestHttpUrl,
       "callHomeEmailFrom": callHomeEmailFrom,
       "callHomeEmailReplyTo": callHomeEmailReplyTo,
       "callHomeEmailMsgDispNotification": callHomeEmailMsgDispNotification,
       "callHomeSmtpServerAddrType": callHomeSmtpServerAddrType,
       "callHomeSmtpServerAddr": callHomeSmtpServerAddr,
       "callHomeSmtpServerPort": callHomeSmtpServerPort,
       "ccmSmtpServersTblMaxEntries": ccmSmtpServersTblMaxEntries,
       "ccmSmtpServersTable": ccmSmtpServersTable,
       "ccmSmtpServersEntry": ccmSmtpServersEntry,
       "ccmSmtpServersAddrType": ccmSmtpServersAddrType,
       "ccmSmtpServersAddr": ccmSmtpServersAddr,
       "ccmSmtpServersPort": ccmSmtpServersPort,
       "ccmSmtpServersStatus": ccmSmtpServersStatus,
       "ccmSmtpServersPriority": ccmSmtpServersPriority,
       "ccmSmtpServersUseVrf": ccmSmtpServersUseVrf,
       "ccmSysLogSeverity": ccmSysLogSeverity,
       "ccmEnableSmtpServerNotif": ccmEnableSmtpServerNotif,
       "callHomeAlertGroupTypeTable": callHomeAlertGroupTypeTable,
       "callHomeAlertGroupTypeEntry": callHomeAlertGroupTypeEntry,
       "callHomeAlertGroupTypeIndex": callHomeAlertGroupTypeIndex,
       "callHomeAlertGroupName": callHomeAlertGroupName,
       "callHomeAlertGroupEnable": callHomeAlertGroupEnable,
       "callHomeAlertGroupCapability": callHomeAlertGroupCapability,
       "callHomeSwInventoryTable": callHomeSwInventoryTable,
       "callHomeSwInventoryEntry": callHomeSwInventoryEntry,
       "callHomeSwServiceName": callHomeSwServiceName,
       "callHomeInventoryNVPairIndex": callHomeInventoryNVPairIndex,
       "callHomeInventoryInfoName": callHomeInventoryInfoName,
       "callHomeInventoryInfoValue": callHomeInventoryInfoValue,
       "ccmPeriodicSwInventoryMsgEnable": ccmPeriodicSwInventoryMsgEnable,
       "ccmPeriodicSwInventoryTimeFrame": ccmPeriodicSwInventoryTimeFrame,
       "ccmMsgThrottlingEnable": ccmMsgThrottlingEnable,
       "ccmCallHomeAlertGroupCfg": ccmCallHomeAlertGroupCfg,
       "ccmSeverityAlertGroupTable": ccmSeverityAlertGroupTable,
       "ccmSeverityAlertGroupEntry": ccmSeverityAlertGroupEntry,
       "ccmAlertGroupSeverity": ccmAlertGroupSeverity,
       "ccmPeriodicAlertGroupTable": ccmPeriodicAlertGroupTable,
       "ccmPeriodicAlertGroupEntry": ccmPeriodicAlertGroupEntry,
       "ccmPeriodicAlertGroupInterval": ccmPeriodicAlertGroupInterval,
       "ccmPeriodicAlertGroupDayOfWeek": ccmPeriodicAlertGroupDayOfWeek,
       "ccmPeriodicAlertGroupDayOfMonth": ccmPeriodicAlertGroupDayOfMonth,
       "ccmPeriodicAlertGroupHour": ccmPeriodicAlertGroupHour,
       "ccmPeriodicAlertGroupMinute": ccmPeriodicAlertGroupMinute,
       "ccmPeriodicAlertGroupEnable": ccmPeriodicAlertGroupEnable,
       "ccmPeriodicAlertGroupIntervalMinutes": ccmPeriodicAlertGroupIntervalMinutes,
       "ccmMaxSyslogAlertGroupPatterns": ccmMaxSyslogAlertGroupPatterns,
       "ccmPatternAlertGroupTable": ccmPatternAlertGroupTable,
       "ccmPatternAlertGroupEntry": ccmPatternAlertGroupEntry,
       "ccmAlertGroupPattern": ccmAlertGroupPattern,
       "ccmPatternAlertGroupSeverity": ccmPatternAlertGroupSeverity,
       "ccmPatternAlertGroupStorage": ccmPatternAlertGroupStorage,
       "ccmPatternAlertGroupStatus": ccmPatternAlertGroupStatus,
       "callHomeUserDefMaxCmds": callHomeUserDefMaxCmds,
       "callHomeUserDefCmdTable": callHomeUserDefCmdTable,
       "callHomeUserDefCmdEntry": callHomeUserDefCmdEntry,
       "callHomeUserDefCmdIndex": callHomeUserDefCmdIndex,
       "callHomeUserDefCmdName": callHomeUserDefCmdName,
       "callHomeUserDefCmdRowStatus": callHomeUserDefCmdRowStatus,
       "ccmEventAlertGroupTable": ccmEventAlertGroupTable,
       "ccmEventAlertGroupEntry": ccmEventAlertGroupEntry,
       "ccmEventAlertGroupEnable": ccmEventAlertGroupEnable,
       "ccmEventAlertGroupOperSeverity": ccmEventAlertGroupOperSeverity,
       "ccmCallHomeProfileTestControl": ccmCallHomeProfileTestControl,
       "ccmDestProfileTestTable": ccmDestProfileTestTable,
       "ccmDestProfileTestEntry": ccmDestProfileTestEntry,
       "ccmDestProfileTestTrigger": ccmDestProfileTestTrigger,
       "ccmDestProfileTestMessage": ccmDestProfileTestMessage,
       "ccmDestProfileTestStatus": ccmDestProfileTestStatus,
       "ccmDestProfileTestFailureCause": ccmDestProfileTestFailureCause,
       "ccmCallHomeNotifConfig": ccmCallHomeNotifConfig,
       "ccmSmtpMsgSendFailNotifEnable": ccmSmtpMsgSendFailNotifEnable,
       "ccmPeriodicSwInventoryCfg": ccmPeriodicSwInventoryCfg,
       "ccmPeriodicSwInventoryTimeOfDay": ccmPeriodicSwInventoryTimeOfDay,
       "ccmAlertRateLimit": ccmAlertRateLimit,
       "ccmHttpProxyServerAddrType": ccmHttpProxyServerAddrType,
       "ccmHttpProxyServerAddr": ccmHttpProxyServerAddr,
       "ccmHttpProxyServerPort": ccmHttpProxyServerPort,
       "ccmHttpProxyServerUseEnable": ccmHttpProxyServerUseEnable,
       "callHomeSmtpServerUseVrf": callHomeSmtpServerUseVrf,
       "ccmHttpTransportUseVrf": ccmHttpTransportUseVrf,
       "ccmCallHomeStats": ccmCallHomeStats,
       "callHomeLastAlertSent": callHomeLastAlertSent,
       "callHomeAlerts": callHomeAlerts,
       "callHomeHCAlerts": callHomeHCAlerts,
       "ccmAlertsDropped": ccmAlertsDropped,
       "ccmEventStatsTable": ccmEventStatsTable,
       "ccmEventStatsEntry": ccmEventStatsEntry,
       "ccmEventStatsTypeIndex": ccmEventStatsTypeIndex,
       "ccmEventStatsMsgTypeIndex": ccmEventStatsMsgTypeIndex,
       "ccmEventStatsTotal": ccmEventStatsTotal,
       "ccmEventStatsConfiguration": ccmEventStatsConfiguration,
       "ccmEventStatsDiagnostic": ccmEventStatsDiagnostic,
       "ccmEventStatsEnvironment": ccmEventStatsEnvironment,
       "ccmEventStatsInventory": ccmEventStatsInventory,
       "ccmEventStatsSystemLog": ccmEventStatsSystemLog,
       "ccmEventStatsTest": ccmEventStatsTest,
       "ccmEventStatsRequest": ccmEventStatsRequest,
       "ccmEventStatsSendCliOutput": ccmEventStatsSendCliOutput,
       "ccmCallHomeStatus": ccmCallHomeStatus,
       "ccmSmtpServerStatusTimeStamp": ccmSmtpServerStatusTimeStamp,
       "ccmSmtpServerStatusInitiate": ccmSmtpServerStatusInitiate,
       "ccmSmtpServerStatusResult": ccmSmtpServerStatusResult,
       "ccmSmtpServerStatusTable": ccmSmtpServerStatusTable,
       "ccmSmtpServerStatusEntry": ccmSmtpServerStatusEntry,
       "ccmSmtpServerStatusAvailability": ccmSmtpServerStatusAvailability,
       "ccmOnDemandMsgServAvailable": ccmOnDemandMsgServAvailable,
       "ccmCallHomeOnDemandActions": ccmCallHomeOnDemandActions,
       "ccmOnDemandMsgSendControl": ccmOnDemandMsgSendControl,
       "ccmOnDemandMsgSendAlertGroup": ccmOnDemandMsgSendAlertGroup,
       "ccmOnDemandMsgSendProfile": ccmOnDemandMsgSendProfile,
       "ccmOnDemandMsgSendEntPhyIndex": ccmOnDemandMsgSendEntPhyIndex,
       "ccmOnDemandMsgSendTrigger": ccmOnDemandMsgSendTrigger,
       "ccmOnDemandCliMsgControl": ccmOnDemandCliMsgControl,
       "ccmOnDemandCliMsgCliList": ccmOnDemandCliMsgCliList,
       "ccmOnDemandCliMsgTransport": ccmOnDemandCliMsgTransport,
       "ccmOnDemandCliMsgEmail": ccmOnDemandCliMsgEmail,
       "ccmOnDemandCliMsgFormat": ccmOnDemandCliMsgFormat,
       "ccmOnDemandCliMsgTacServiceReqId": ccmOnDemandCliMsgTacServiceReqId,
       "ccmOnDemandCliMsgTrigger": ccmOnDemandCliMsgTrigger,
       "ccmSmartCallHomeActions": ccmSmartCallHomeActions,
       "ccmSmartCallHomeProfile": ccmSmartCallHomeProfile,
       "ccmSmartCallHomeServiceType": ccmSmartCallHomeServiceType,
       "ccmSmartCallHomeAnalysisCmd": ccmSmartCallHomeAnalysisCmd,
       "ccmSmartCallHomeCcoId": ccmSmartCallHomeCcoId,
       "ccmSmartCallHomeTrigger": ccmSmartCallHomeTrigger,
       "ccmCallHomeVrf": ccmCallHomeVrf,
       "ccmCallHomeVrfName": ccmCallHomeVrfName,
       "ccmCallHomeMessageSource": ccmCallHomeMessageSource,
       "ccmMsgSourceIpAddrType": ccmMsgSourceIpAddrType,
       "ccmMsgSourceIpAddr": ccmMsgSourceIpAddr,
       "ccmMsgSourceInterface": ccmMsgSourceInterface,
       "ccmCallhomeEvents": ccmCallhomeEvents,
       "ccmEventDescription": ccmEventDescription,
       "ccmEventTime": ccmEventTime,
       "ccmEventUrgencyLevel": ccmEventUrgencyLevel,
       "ccmCallHomeDiagSignature": ccmCallHomeDiagSignature,
       "ccmDiagSignatureActive": ccmDiagSignatureActive,
       "ccmDiagSignatureProfileName": ccmDiagSignatureProfileName,
       "ccmCallHomeDiagSignatureInfoTable": ccmCallHomeDiagSignatureInfoTable,
       "ccmCallHomeDiagSignatureInfoEntry": ccmCallHomeDiagSignatureInfoEntry,
       "ccmCallHomeDiagSignatureName": ccmCallHomeDiagSignatureName,
       "ccmCallHomeDiagSignatureType": ccmCallHomeDiagSignatureType,
       "ccmCallHomeDiagSignatureFuncDescr": ccmCallHomeDiagSignatureFuncDescr,
       "ccmCallHomeDiagSignatureRev": ccmCallHomeDiagSignatureRev,
       "ccmCallHomeDiagSignatureSigner": ccmCallHomeDiagSignatureSigner,
       "ccmCallHomeDiagSignatureTriggerCount": ccmCallHomeDiagSignatureTriggerCount,
       "ccmCallHomeDiagSignatureAvgRuntime": ccmCallHomeDiagSignatureAvgRuntime,
       "ccmCallHomeDiagSignatureMaxRuntime": ccmCallHomeDiagSignatureMaxRuntime,
       "ccmCallHomeSecurity": ccmCallHomeSecurity,
       "ccmCallHomeSecurityLevel": ccmCallHomeSecurityLevel,
       "ccmCallHomeReporting": ccmCallHomeReporting,
       "ccmAnonymousReportingEnable": ccmAnonymousReportingEnable,
       "ccmCallHomeHttpProxy": ccmCallHomeHttpProxy,
       "ccmCallHomeAaa": ccmCallHomeAaa,
       "ccmAaaAuthEnable": ccmAaaAuthEnable,
       "ccmAaaAuthUserName": ccmAaaAuthUserName,
       "chMIBConformance": chMIBConformance,
       "chMIBCompliances": chMIBCompliances,
       "chMIBCompliance": chMIBCompliance,
       "chMIBCompliance1": chMIBCompliance1,
       "chMIBCompliance2": chMIBCompliance2,
       "chMIBCompliance3": chMIBCompliance3,
       "chMIBCompliance4": chMIBCompliance4,
       "chMIBCompliance5": chMIBCompliance5,
       "chMIBCompliance6": chMIBCompliance6,
       "chMIBCompliance7": chMIBCompliance7,
       "chMIBCompliance8": chMIBCompliance8,
       "chMIBCompliance9": chMIBCompliance9,
       "chMIBGroups": chMIBGroups,
       "chSystemInformationGroup": chSystemInformationGroup,
       "chConfigurationGroup": chConfigurationGroup,
       "chEmailMsgDispGroup": chEmailMsgDispGroup,
       "chSingleSmtpServerGroup": chSingleSmtpServerGroup,
       "chMultipleSmtpServersGroup": chMultipleSmtpServersGroup,
       "chStatisticsGroup": chStatisticsGroup,
       "ccmSysLogSeverityGroup": ccmSysLogSeverityGroup,
       "ccmMIBNotificationsConfigGroup": ccmMIBNotificationsConfigGroup,
       "ccmMIBNotificationsGroup": ccmMIBNotificationsGroup,
       "chConfigurationGroup1": chConfigurationGroup1,
       "ccmMIBNotificationsGroup1": ccmMIBNotificationsGroup1,
       "chConfigurationGroup2": chConfigurationGroup2,
       "chSwInventoryInfoGroup": chSwInventoryInfoGroup,
       "chPeriodicSwInventoryInfoGroup": chPeriodicSwInventoryInfoGroup,
       "chSwInventoryInfoGroup1": chSwInventoryInfoGroup1,
       "ccmUserDefCmdGroup": ccmUserDefCmdGroup,
       "ccmPeriodicSwInventoryInfoGroup1": ccmPeriodicSwInventoryInfoGroup1,
       "ccmConfigurationGroup3": ccmConfigurationGroup3,
       "ccmAlertActionGroup": ccmAlertActionGroup,
       "ccmProfileMessageLevelGroup": ccmProfileMessageLevelGroup,
       "ccmProfileActivationGroup": ccmProfileActivationGroup,
       "ccmProfileTestGroup": ccmProfileTestGroup,
       "ccmProfileAlertGroupsGroup": ccmProfileAlertGroupsGroup,
       "ccmProfileAlertGroupControlGroup": ccmProfileAlertGroupControlGroup,
       "ccmThrottleConfigurationGroup": ccmThrottleConfigurationGroup,
       "ccmSmtpServersPriorityGroup": ccmSmtpServersPriorityGroup,
       "ccmAlertGroupCapabilityGroup": ccmAlertGroupCapabilityGroup,
       "ccmHttpCfgGroup": ccmHttpCfgGroup,
       "ccmSeverityAlertGroupCfgGroup": ccmSeverityAlertGroupCfgGroup,
       "ccmPeriodicAlertGroupCfgGroup": ccmPeriodicAlertGroupCfgGroup,
       "ccmPatternAlertGroupCfgGroup": ccmPatternAlertGroupCfgGroup,
       "ccmEventAlertGroupCfgGroup": ccmEventAlertGroupCfgGroup,
       "ccmSmtpMsgSendFailNotifCtrlGroup": ccmSmtpMsgSendFailNotifCtrlGroup,
       "ccmSmtpMsgSendFailNotifGroup": ccmSmtpMsgSendFailNotifGroup,
       "ccmAlertHCStatisticsGroup": ccmAlertHCStatisticsGroup,
       "ccmAlertRateLimitGroup": ccmAlertRateLimitGroup,
       "ccmSmtpServerStatusGroup": ccmSmtpServerStatusGroup,
       "ccmProfileHiMessageSizeGroup": ccmProfileHiMessageSizeGroup,
       "chSystemInformationGroup1": chSystemInformationGroup1,
       "chSystemServicePriorityGroup": chSystemServicePriorityGroup,
       "ccmOnDemandMsgSendControlGroup": ccmOnDemandMsgSendControlGroup,
       "ccmOnDemandMsgStatusGroup": ccmOnDemandMsgStatusGroup,
       "ccmSmartCallHomeGroup": ccmSmartCallHomeGroup,
       "ccmEventStatsGroup": ccmEventStatsGroup,
       "ccmEventNotifGroup": ccmEventNotifGroup,
       "ccmCallhomeEventsGroup": ccmCallhomeEventsGroup,
       "ccmCallHomeVrfGroup": ccmCallHomeVrfGroup,
       "ccmSmtpServersVrfGroup": ccmSmtpServersVrfGroup,
       "ccmHttpProxyServerGroup": ccmHttpProxyServerGroup,
       "ccmHttpTransportVrfGroup": ccmHttpTransportVrfGroup,
       "ccmSingleSmtpServerGroup": ccmSingleSmtpServerGroup,
       "ccmMessageSourceGroup": ccmMessageSourceGroup,
       "ccmCallHomePeriodicMinutesGroup": ccmCallHomePeriodicMinutesGroup,
       "ccmOnDemandCliMsgGroup": ccmOnDemandCliMsgGroup,
       "ccmCallHomeDiagSignatureGroup": ccmCallHomeDiagSignatureGroup,
       "ccmCallHomeSecurityLevelGroup": ccmCallHomeSecurityLevelGroup,
       "ccmCallHomeAnonymousReportingGroup": ccmCallHomeAnonymousReportingGroup,
       "ccmCallHomeAaaGroup": ccmCallHomeAaaGroup}
)
