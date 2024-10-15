# SNMP MIB module (CISCO-CONFIG-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONFIG-COPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:38 2024
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

(FcNameIdOrZero,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameIdOrZero")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoConfigCopyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96)
)
ciscoConfigCopyMIB.setRevisions(
        ("2009-02-27 00:00",
         "2005-04-06 00:00",
         "2004-03-17 00:00",
         "2002-12-17 00:00",
         "2002-05-30 00:00",
         "2002-05-07 00:00",
         "2002-03-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigCopyProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("ftp", 2),
          ("rcp", 3),
          ("scp", 4),
          ("sftp", 5),
          ("tftp", 1))
    )



class ConfigCopyState(Integer32, TextualConvention):
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
        *(("failed", 4),
          ("running", 2),
          ("successful", 3),
          ("waiting", 1))
    )



class ConfigCopyFailCause(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("badFileName", 2),
          ("noConfig", 5),
          ("noMem", 4),
          ("requestAborted", 9),
          ("someConfigApplyFailed", 7),
          ("systemNotReady", 8),
          ("timeout", 3),
          ("unknown", 1),
          ("unsupportedProtocol", 6))
    )



class ConfigFileType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fabricStartupConfig", 6),
          ("iosFile", 2),
          ("networkFile", 1),
          ("runningConfig", 4),
          ("startupConfig", 3),
          ("terminal", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoConfigCopyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoConfigCopyMIBObjects = _CiscoConfigCopyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1)
)
_CcCopy_ObjectIdentity = ObjectIdentity
ccCopy = _CcCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1)
)
_CcCopyTable_Object = MibTable
ccCopyTable = _CcCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccCopyTable.setStatus("current")
_CcCopyEntry_Object = MibTableRow
ccCopyEntry = _CcCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1)
)
ccCopyEntry.setIndexNames(
    (0, "CISCO-CONFIG-COPY-MIB", "ccCopyIndex"),
)
if mibBuilder.loadTexts:
    ccCopyEntry.setStatus("current")


class _CcCopyIndex_Type(Unsigned32):
    """Custom type ccCopyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcCopyIndex_Type.__name__ = "Unsigned32"
_CcCopyIndex_Object = MibTableColumn
ccCopyIndex = _CcCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 1),
    _CcCopyIndex_Type()
)
ccCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCopyIndex.setStatus("current")


class _CcCopyProtocol_Type(ConfigCopyProtocol):
    """Custom type ccCopyProtocol based on ConfigCopyProtocol"""


_CcCopyProtocol_Object = MibTableColumn
ccCopyProtocol = _CcCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 2),
    _CcCopyProtocol_Type()
)
ccCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyProtocol.setStatus("current")
_CcCopySourceFileType_Type = ConfigFileType
_CcCopySourceFileType_Object = MibTableColumn
ccCopySourceFileType = _CcCopySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 3),
    _CcCopySourceFileType_Type()
)
ccCopySourceFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopySourceFileType.setStatus("current")
_CcCopyDestFileType_Type = ConfigFileType
_CcCopyDestFileType_Object = MibTableColumn
ccCopyDestFileType = _CcCopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 4),
    _CcCopyDestFileType_Type()
)
ccCopyDestFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyDestFileType.setStatus("current")
_CcCopyServerAddress_Type = IpAddress
_CcCopyServerAddress_Object = MibTableColumn
ccCopyServerAddress = _CcCopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 5),
    _CcCopyServerAddress_Type()
)
ccCopyServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyServerAddress.setStatus("deprecated")
_CcCopyFileName_Type = DisplayString
_CcCopyFileName_Object = MibTableColumn
ccCopyFileName = _CcCopyFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 6),
    _CcCopyFileName_Type()
)
ccCopyFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyFileName.setStatus("current")


class _CcCopyUserName_Type(DisplayString):
    """Custom type ccCopyUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CcCopyUserName_Type.__name__ = "DisplayString"
_CcCopyUserName_Object = MibTableColumn
ccCopyUserName = _CcCopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 7),
    _CcCopyUserName_Type()
)
ccCopyUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyUserName.setStatus("current")


class _CcCopyUserPassword_Type(DisplayString):
    """Custom type ccCopyUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CcCopyUserPassword_Type.__name__ = "DisplayString"
_CcCopyUserPassword_Object = MibTableColumn
ccCopyUserPassword = _CcCopyUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 8),
    _CcCopyUserPassword_Type()
)
ccCopyUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyUserPassword.setStatus("current")


class _CcCopyNotificationOnCompletion_Type(TruthValue):
    """Custom type ccCopyNotificationOnCompletion based on TruthValue"""


_CcCopyNotificationOnCompletion_Object = MibTableColumn
ccCopyNotificationOnCompletion = _CcCopyNotificationOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 9),
    _CcCopyNotificationOnCompletion_Type()
)
ccCopyNotificationOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyNotificationOnCompletion.setStatus("current")
_CcCopyState_Type = ConfigCopyState
_CcCopyState_Object = MibTableColumn
ccCopyState = _CcCopyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 10),
    _CcCopyState_Type()
)
ccCopyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyState.setStatus("current")
_CcCopyTimeStarted_Type = TimeStamp
_CcCopyTimeStarted_Object = MibTableColumn
ccCopyTimeStarted = _CcCopyTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 11),
    _CcCopyTimeStarted_Type()
)
ccCopyTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyTimeStarted.setStatus("current")
_CcCopyTimeCompleted_Type = TimeStamp
_CcCopyTimeCompleted_Object = MibTableColumn
ccCopyTimeCompleted = _CcCopyTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 12),
    _CcCopyTimeCompleted_Type()
)
ccCopyTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyTimeCompleted.setStatus("current")
_CcCopyFailCause_Type = ConfigCopyFailCause
_CcCopyFailCause_Object = MibTableColumn
ccCopyFailCause = _CcCopyFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 13),
    _CcCopyFailCause_Type()
)
ccCopyFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyFailCause.setStatus("current")
_CcCopyEntryRowStatus_Type = RowStatus
_CcCopyEntryRowStatus_Object = MibTableColumn
ccCopyEntryRowStatus = _CcCopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 14),
    _CcCopyEntryRowStatus_Type()
)
ccCopyEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyEntryRowStatus.setStatus("current")
_CcCopyServerAddressType_Type = InetAddressType
_CcCopyServerAddressType_Object = MibTableColumn
ccCopyServerAddressType = _CcCopyServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 15),
    _CcCopyServerAddressType_Type()
)
ccCopyServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyServerAddressType.setStatus("current")
_CcCopyServerAddressRev1_Type = InetAddress
_CcCopyServerAddressRev1_Object = MibTableColumn
ccCopyServerAddressRev1 = _CcCopyServerAddressRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 16),
    _CcCopyServerAddressRev1_Type()
)
ccCopyServerAddressRev1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyServerAddressRev1.setStatus("current")


class _CcCopyVrfName_Type(OctetString):
    """Custom type ccCopyVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcCopyVrfName_Type.__name__ = "OctetString"
_CcCopyVrfName_Object = MibTableColumn
ccCopyVrfName = _CcCopyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 17),
    _CcCopyVrfName_Type()
)
ccCopyVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccCopyVrfName.setStatus("current")
_CcCopyErrorTable_Object = MibTable
ccCopyErrorTable = _CcCopyErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ccCopyErrorTable.setStatus("current")
_CcCopyErrorEntry_Object = MibTableRow
ccCopyErrorEntry = _CcCopyErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1)
)
ccCopyErrorEntry.setIndexNames(
    (0, "CISCO-CONFIG-COPY-MIB", "ccCopyIndex"),
    (0, "CISCO-CONFIG-COPY-MIB", "ccCopyErrorIndex"),
)
if mibBuilder.loadTexts:
    ccCopyErrorEntry.setStatus("current")
_CcCopyErrorIndex_Type = Unsigned32
_CcCopyErrorIndex_Object = MibTableColumn
ccCopyErrorIndex = _CcCopyErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 1),
    _CcCopyErrorIndex_Type()
)
ccCopyErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccCopyErrorIndex.setStatus("current")
_CcCopyErrorDeviceIpAddressType_Type = InetAddressType
_CcCopyErrorDeviceIpAddressType_Object = MibTableColumn
ccCopyErrorDeviceIpAddressType = _CcCopyErrorDeviceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 2),
    _CcCopyErrorDeviceIpAddressType_Type()
)
ccCopyErrorDeviceIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyErrorDeviceIpAddressType.setStatus("current")
_CcCopyErrorDeviceIpAddress_Type = InetAddress
_CcCopyErrorDeviceIpAddress_Object = MibTableColumn
ccCopyErrorDeviceIpAddress = _CcCopyErrorDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 3),
    _CcCopyErrorDeviceIpAddress_Type()
)
ccCopyErrorDeviceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyErrorDeviceIpAddress.setStatus("current")
_CcCopyErrorDeviceWWN_Type = FcNameIdOrZero
_CcCopyErrorDeviceWWN_Object = MibTableColumn
ccCopyErrorDeviceWWN = _CcCopyErrorDeviceWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 4),
    _CcCopyErrorDeviceWWN_Type()
)
ccCopyErrorDeviceWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyErrorDeviceWWN.setStatus("current")
_CcCopyErrorDescription_Type = SnmpAdminString
_CcCopyErrorDescription_Object = MibTableColumn
ccCopyErrorDescription = _CcCopyErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 5),
    _CcCopyErrorDescription_Type()
)
ccCopyErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCopyErrorDescription.setStatus("current")
_CiscoConfigCopyMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoConfigCopyMIBTrapPrefix = _CiscoConfigCopyMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 2)
)
_CcCopyMIBTraps_ObjectIdentity = ObjectIdentity
ccCopyMIBTraps = _CcCopyMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 2, 1)
)
_CiscoConfigCopyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoConfigCopyMIBConformance = _CiscoConfigCopyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3)
)
_CcCopyMIBCompliances_ObjectIdentity = ObjectIdentity
ccCopyMIBCompliances = _CcCopyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1)
)
_CcCopyMIBGroups_ObjectIdentity = ObjectIdentity
ccCopyMIBGroups = _CcCopyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2)
)

# Managed Objects groups

ccCopyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 1)
)
ccCopyGroup.setObjects(
      *(("CISCO-CONFIG-COPY-MIB", "ccCopyProtocol"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopySourceFileType"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyDestFileType"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddress"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyUserName"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyUserPassword"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationOnCompletion"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyState"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ccCopyGroup.setStatus("deprecated")

ccCopyGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 3)
)
ccCopyGroupRev1.setObjects(
      *(("CISCO-CONFIG-COPY-MIB", "ccCopyProtocol"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopySourceFileType"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyDestFileType"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddressType"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddressRev1"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyUserName"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyUserPassword"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationOnCompletion"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyState"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ccCopyGroupRev1.setStatus("current")

ccCopyErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 4)
)
ccCopyErrorGroup.setObjects(
      *(("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceIpAddressType"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceIpAddress"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceWWN"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDescription"))
)
if mibBuilder.loadTexts:
    ccCopyErrorGroup.setStatus("current")

ccCopyGroupVpn = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 5)
)
ccCopyGroupVpn.setObjects(
    ("CISCO-CONFIG-COPY-MIB", "ccCopyVrfName")
)
if mibBuilder.loadTexts:
    ccCopyGroupVpn.setStatus("current")


# Notification objects

ccCopyCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 2, 1, 1)
)
ccCopyCompletion.setObjects(
      *(("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddress"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyState"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"),
        ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"))
)
if mibBuilder.loadTexts:
    ccCopyCompletion.setStatus(
        "current"
    )


# Notifications groups

ccCopyNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 2)
)
ccCopyNotificationsGroup.setObjects(
    ("CISCO-CONFIG-COPY-MIB", "ccCopyCompletion")
)
if mibBuilder.loadTexts:
    ccCopyNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ccCopyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccCopyMIBCompliance.setStatus(
        "deprecated"
    )

ccCopyMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccCopyMIBComplianceRev1.setStatus(
        "deprecated"
    )

ccCopyMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ccCopyMIBComplianceRev2.setStatus(
        "deprecated"
    )

ccCopyMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ccCopyMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONFIG-COPY-MIB",
    **{"ConfigCopyProtocol": ConfigCopyProtocol,
       "ConfigCopyState": ConfigCopyState,
       "ConfigCopyFailCause": ConfigCopyFailCause,
       "ConfigFileType": ConfigFileType,
       "ciscoConfigCopyMIB": ciscoConfigCopyMIB,
       "ciscoConfigCopyMIBObjects": ciscoConfigCopyMIBObjects,
       "ccCopy": ccCopy,
       "ccCopyTable": ccCopyTable,
       "ccCopyEntry": ccCopyEntry,
       "ccCopyIndex": ccCopyIndex,
       "ccCopyProtocol": ccCopyProtocol,
       "ccCopySourceFileType": ccCopySourceFileType,
       "ccCopyDestFileType": ccCopyDestFileType,
       "ccCopyServerAddress": ccCopyServerAddress,
       "ccCopyFileName": ccCopyFileName,
       "ccCopyUserName": ccCopyUserName,
       "ccCopyUserPassword": ccCopyUserPassword,
       "ccCopyNotificationOnCompletion": ccCopyNotificationOnCompletion,
       "ccCopyState": ccCopyState,
       "ccCopyTimeStarted": ccCopyTimeStarted,
       "ccCopyTimeCompleted": ccCopyTimeCompleted,
       "ccCopyFailCause": ccCopyFailCause,
       "ccCopyEntryRowStatus": ccCopyEntryRowStatus,
       "ccCopyServerAddressType": ccCopyServerAddressType,
       "ccCopyServerAddressRev1": ccCopyServerAddressRev1,
       "ccCopyVrfName": ccCopyVrfName,
       "ccCopyErrorTable": ccCopyErrorTable,
       "ccCopyErrorEntry": ccCopyErrorEntry,
       "ccCopyErrorIndex": ccCopyErrorIndex,
       "ccCopyErrorDeviceIpAddressType": ccCopyErrorDeviceIpAddressType,
       "ccCopyErrorDeviceIpAddress": ccCopyErrorDeviceIpAddress,
       "ccCopyErrorDeviceWWN": ccCopyErrorDeviceWWN,
       "ccCopyErrorDescription": ccCopyErrorDescription,
       "ciscoConfigCopyMIBTrapPrefix": ciscoConfigCopyMIBTrapPrefix,
       "ccCopyMIBTraps": ccCopyMIBTraps,
       "ccCopyCompletion": ccCopyCompletion,
       "ciscoConfigCopyMIBConformance": ciscoConfigCopyMIBConformance,
       "ccCopyMIBCompliances": ccCopyMIBCompliances,
       "ccCopyMIBCompliance": ccCopyMIBCompliance,
       "ccCopyMIBComplianceRev1": ccCopyMIBComplianceRev1,
       "ccCopyMIBComplianceRev2": ccCopyMIBComplianceRev2,
       "ccCopyMIBComplianceRev3": ccCopyMIBComplianceRev3,
       "ccCopyMIBGroups": ccCopyMIBGroups,
       "ccCopyGroup": ccCopyGroup,
       "ccCopyNotificationsGroup": ccCopyNotificationsGroup,
       "ccCopyGroupRev1": ccCopyGroupRev1,
       "ccCopyErrorGroup": ccCopyErrorGroup,
       "ccCopyGroupVpn": ccCopyGroupVpn}
)
