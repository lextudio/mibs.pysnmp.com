# SNMP MIB module (CISCO-FCSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:27 2024
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

(FcNameId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFcspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391)
)
ciscoFcspMIB.setRevisions(
        ("2004-07-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFcspMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoFcspMIBNotifications = _CiscoFcspMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 0)
)
_CiscoFcspMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcspMIBObjects = _CiscoFcspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1)
)
_CfcspConfig_ObjectIdentity = ObjectIdentity
cfcspConfig = _CfcspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1)
)
_CfcspIfTable_Object = MibTable
cfcspIfTable = _CfcspIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfcspIfTable.setStatus("current")
_CfcspIfEntry_Object = MibTableRow
cfcspIfEntry = _CfcspIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1)
)
cfcspIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcspIfEntry.setStatus("current")


class _CfcspMode_Type(Integer32):
    """Custom type cfcspMode based on Integer32"""
    defaultValue = 2

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
        *(("autoActive", 3),
          ("autoPassive", 2),
          ("off", 1),
          ("on", 4))
    )


_CfcspMode_Type.__name__ = "Integer32"
_CfcspMode_Object = MibTableColumn
cfcspMode = _CfcspMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1, 1),
    _CfcspMode_Type()
)
cfcspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspMode.setStatus("current")


class _CfcspReauthInterval_Type(Unsigned32):
    """Custom type cfcspReauthInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CfcspReauthInterval_Type.__name__ = "Unsigned32"
_CfcspReauthInterval_Object = MibTableColumn
cfcspReauthInterval = _CfcspReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1, 2),
    _CfcspReauthInterval_Type()
)
cfcspReauthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspReauthInterval.setStatus("current")
if mibBuilder.loadTexts:
    cfcspReauthInterval.setUnits("minutes")


class _CfcspReauthenticate_Type(Integer32):
    """Custom type cfcspReauthenticate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noOp", 2))
    )


_CfcspReauthenticate_Type.__name__ = "Integer32"
_CfcspReauthenticate_Object = MibTableColumn
cfcspReauthenticate = _CfcspReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1, 3),
    _CfcspReauthenticate_Type()
)
cfcspReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspReauthenticate.setStatus("current")


class _CfcspAuthProtocols_Type(Integer32):
    """Custom type cfcspAuthProtocols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhChap", 0),
          ("fcCap", 1))
    )


_CfcspAuthProtocols_Type.__name__ = "Integer32"
_CfcspAuthProtocols_Object = MibScalar
cfcspAuthProtocols = _CfcspAuthProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 2),
    _CfcspAuthProtocols_Type()
)
cfcspAuthProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspAuthProtocols.setStatus("current")


class _CfcspTimeout_Type(Unsigned32):
    """Custom type cfcspTimeout based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_CfcspTimeout_Type.__name__ = "Unsigned32"
_CfcspTimeout_Object = MibScalar
cfcspTimeout = _CfcspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 3),
    _CfcspTimeout_Type()
)
cfcspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cfcspTimeout.setUnits("seconds")
_CfcspDhChapObjects_ObjectIdentity = ObjectIdentity
cfcspDhChapObjects = _CfcspDhChapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4)
)


class _CfcspDhChapHashList_Type(OctetString):
    """Custom type cfcspDhChapHashList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CfcspDhChapHashList_Type.__name__ = "OctetString"
_CfcspDhChapHashList_Object = MibScalar
cfcspDhChapHashList = _CfcspDhChapHashList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4, 1),
    _CfcspDhChapHashList_Type()
)
cfcspDhChapHashList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspDhChapHashList.setStatus("current")


class _CfcspDhChapGroupList_Type(OctetString):
    """Custom type cfcspDhChapGroupList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CfcspDhChapGroupList_Type.__name__ = "OctetString"
_CfcspDhChapGroupList_Object = MibScalar
cfcspDhChapGroupList = _CfcspDhChapGroupList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4, 2),
    _CfcspDhChapGroupList_Type()
)
cfcspDhChapGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspDhChapGroupList.setStatus("current")


class _CfcspDhChapGenericPasswd_Type(SnmpAdminString):
    """Custom type cfcspDhChapGenericPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfcspDhChapGenericPasswd_Type.__name__ = "SnmpAdminString"
_CfcspDhChapGenericPasswd_Object = MibScalar
cfcspDhChapGenericPasswd = _CfcspDhChapGenericPasswd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4, 3),
    _CfcspDhChapGenericPasswd_Type()
)
cfcspDhChapGenericPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcspDhChapGenericPasswd.setStatus("current")
_CfcspLocalPasswdTable_Object = MibTable
cfcspLocalPasswdTable = _CfcspLocalPasswdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfcspLocalPasswdTable.setStatus("current")
_CfcspLocalPasswdEntry_Object = MibTableRow
cfcspLocalPasswdEntry = _CfcspLocalPasswdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1)
)
cfcspLocalPasswdEntry.setIndexNames(
    (0, "CISCO-FCSP-MIB", "cfcspSwitchWwn"),
)
if mibBuilder.loadTexts:
    cfcspLocalPasswdEntry.setStatus("current")
_CfcspSwitchWwn_Type = FcNameId
_CfcspSwitchWwn_Object = MibTableColumn
cfcspSwitchWwn = _CfcspSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1, 1),
    _CfcspSwitchWwn_Type()
)
cfcspSwitchWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcspSwitchWwn.setStatus("current")


class _CfcspLocalPasswd_Type(SnmpAdminString):
    """Custom type cfcspLocalPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfcspLocalPasswd_Type.__name__ = "SnmpAdminString"
_CfcspLocalPasswd_Object = MibTableColumn
cfcspLocalPasswd = _CfcspLocalPasswd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1, 2),
    _CfcspLocalPasswd_Type()
)
cfcspLocalPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcspLocalPasswd.setStatus("current")
_CfcspLocalPassRowStatus_Type = RowStatus
_CfcspLocalPassRowStatus_Object = MibTableColumn
cfcspLocalPassRowStatus = _CfcspLocalPassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1, 3),
    _CfcspLocalPassRowStatus_Type()
)
cfcspLocalPassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcspLocalPassRowStatus.setStatus("current")
_CfcspRemotePasswdTable_Object = MibTable
cfcspRemotePasswdTable = _CfcspRemotePasswdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfcspRemotePasswdTable.setStatus("current")
_CfcspRemotePasswdEntry_Object = MibTableRow
cfcspRemotePasswdEntry = _CfcspRemotePasswdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1)
)
cfcspRemotePasswdEntry.setIndexNames(
    (0, "CISCO-FCSP-MIB", "cfcspRemoteSwitchWwn"),
)
if mibBuilder.loadTexts:
    cfcspRemotePasswdEntry.setStatus("current")
_CfcspRemoteSwitchWwn_Type = FcNameId
_CfcspRemoteSwitchWwn_Object = MibTableColumn
cfcspRemoteSwitchWwn = _CfcspRemoteSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1, 1),
    _CfcspRemoteSwitchWwn_Type()
)
cfcspRemoteSwitchWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcspRemoteSwitchWwn.setStatus("current")


class _CfcspRemotePasswd_Type(SnmpAdminString):
    """Custom type cfcspRemotePasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfcspRemotePasswd_Type.__name__ = "SnmpAdminString"
_CfcspRemotePasswd_Object = MibTableColumn
cfcspRemotePasswd = _CfcspRemotePasswd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1, 2),
    _CfcspRemotePasswd_Type()
)
cfcspRemotePasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcspRemotePasswd.setStatus("current")
_CfcspRemotePassRowStatus_Type = RowStatus
_CfcspRemotePassRowStatus_Object = MibTableColumn
cfcspRemotePassRowStatus = _CfcspRemotePassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1, 3),
    _CfcspRemotePassRowStatus_Type()
)
cfcspRemotePassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcspRemotePassRowStatus.setStatus("current")
_CfcspInfo_ObjectIdentity = ObjectIdentity
cfcspInfo = _CfcspInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 2)
)
_CfcspStatistics_ObjectIdentity = ObjectIdentity
cfcspStatistics = _CfcspStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3)
)
_CfcspIfStatsTable_Object = MibTable
cfcspIfStatsTable = _CfcspIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfcspIfStatsTable.setStatus("current")
_CfcspIfStatsEntry_Object = MibTableRow
cfcspIfStatsEntry = _CfcspIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1)
)
cfcspIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcspIfStatsEntry.setStatus("current")
_CfcspIfAuthSucceeded_Type = Counter32
_CfcspIfAuthSucceeded_Object = MibTableColumn
cfcspIfAuthSucceeded = _CfcspIfAuthSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1, 1),
    _CfcspIfAuthSucceeded_Type()
)
cfcspIfAuthSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcspIfAuthSucceeded.setStatus("current")
_CfcspIfAuthFailed_Type = Counter32
_CfcspIfAuthFailed_Object = MibTableColumn
cfcspIfAuthFailed = _CfcspIfAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1, 2),
    _CfcspIfAuthFailed_Type()
)
cfcspIfAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcspIfAuthFailed.setStatus("current")
_CfcspIfAuthByPassed_Type = Counter32
_CfcspIfAuthByPassed_Object = MibTableColumn
cfcspIfAuthByPassed = _CfcspIfAuthByPassed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1, 3),
    _CfcspIfAuthByPassed_Type()
)
cfcspIfAuthByPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcspIfAuthByPassed.setStatus("current")
_CfcspNotificationObjects_ObjectIdentity = ObjectIdentity
cfcspNotificationObjects = _CfcspNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 4)
)
_CiscoFcspMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFcspMIBConformance = _CiscoFcspMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2)
)
_CiscoFcspMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFcspMIBCompliances = _CiscoFcspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 1)
)
_CiscoFcspMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFcspMIBGroups = _CiscoFcspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2)
)

# Managed Objects groups

cfcspConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 1)
)
cfcspConfigGroup.setObjects(
      *(("CISCO-FCSP-MIB", "cfcspMode"),
        ("CISCO-FCSP-MIB", "cfcspReauthInterval"),
        ("CISCO-FCSP-MIB", "cfcspReauthenticate"),
        ("CISCO-FCSP-MIB", "cfcspAuthProtocols"),
        ("CISCO-FCSP-MIB", "cfcspTimeout"),
        ("CISCO-FCSP-MIB", "cfcspDhChapHashList"),
        ("CISCO-FCSP-MIB", "cfcspDhChapGroupList"),
        ("CISCO-FCSP-MIB", "cfcspDhChapGenericPasswd"))
)
if mibBuilder.loadTexts:
    cfcspConfigGroup.setStatus("current")

cfcspLocalPasswdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 2)
)
cfcspLocalPasswdGroup.setObjects(
      *(("CISCO-FCSP-MIB", "cfcspLocalPasswd"),
        ("CISCO-FCSP-MIB", "cfcspLocalPassRowStatus"),
        ("CISCO-FCSP-MIB", "cfcspRemotePasswd"),
        ("CISCO-FCSP-MIB", "cfcspRemotePassRowStatus"))
)
if mibBuilder.loadTexts:
    cfcspLocalPasswdGroup.setStatus("current")

cfcspIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 3)
)
cfcspIfStatsGroup.setObjects(
      *(("CISCO-FCSP-MIB", "cfcspIfAuthSucceeded"),
        ("CISCO-FCSP-MIB", "cfcspIfAuthFailed"),
        ("CISCO-FCSP-MIB", "cfcspIfAuthByPassed"))
)
if mibBuilder.loadTexts:
    cfcspIfStatsGroup.setStatus("current")


# Notification objects

cfcspAuthFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 0, 1)
)
cfcspAuthFailNotification.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    cfcspAuthFailNotification.setStatus(
        "current"
    )


# Notifications groups

cfcspNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 4)
)
cfcspNotificationGroup.setObjects(
    ("CISCO-FCSP-MIB", "cfcspAuthFailNotification")
)
if mibBuilder.loadTexts:
    cfcspNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFcspMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFcspMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCSP-MIB",
    **{"ciscoFcspMIB": ciscoFcspMIB,
       "ciscoFcspMIBNotifications": ciscoFcspMIBNotifications,
       "cfcspAuthFailNotification": cfcspAuthFailNotification,
       "ciscoFcspMIBObjects": ciscoFcspMIBObjects,
       "cfcspConfig": cfcspConfig,
       "cfcspIfTable": cfcspIfTable,
       "cfcspIfEntry": cfcspIfEntry,
       "cfcspMode": cfcspMode,
       "cfcspReauthInterval": cfcspReauthInterval,
       "cfcspReauthenticate": cfcspReauthenticate,
       "cfcspAuthProtocols": cfcspAuthProtocols,
       "cfcspTimeout": cfcspTimeout,
       "cfcspDhChapObjects": cfcspDhChapObjects,
       "cfcspDhChapHashList": cfcspDhChapHashList,
       "cfcspDhChapGroupList": cfcspDhChapGroupList,
       "cfcspDhChapGenericPasswd": cfcspDhChapGenericPasswd,
       "cfcspLocalPasswdTable": cfcspLocalPasswdTable,
       "cfcspLocalPasswdEntry": cfcspLocalPasswdEntry,
       "cfcspSwitchWwn": cfcspSwitchWwn,
       "cfcspLocalPasswd": cfcspLocalPasswd,
       "cfcspLocalPassRowStatus": cfcspLocalPassRowStatus,
       "cfcspRemotePasswdTable": cfcspRemotePasswdTable,
       "cfcspRemotePasswdEntry": cfcspRemotePasswdEntry,
       "cfcspRemoteSwitchWwn": cfcspRemoteSwitchWwn,
       "cfcspRemotePasswd": cfcspRemotePasswd,
       "cfcspRemotePassRowStatus": cfcspRemotePassRowStatus,
       "cfcspInfo": cfcspInfo,
       "cfcspStatistics": cfcspStatistics,
       "cfcspIfStatsTable": cfcspIfStatsTable,
       "cfcspIfStatsEntry": cfcspIfStatsEntry,
       "cfcspIfAuthSucceeded": cfcspIfAuthSucceeded,
       "cfcspIfAuthFailed": cfcspIfAuthFailed,
       "cfcspIfAuthByPassed": cfcspIfAuthByPassed,
       "cfcspNotificationObjects": cfcspNotificationObjects,
       "ciscoFcspMIBConformance": ciscoFcspMIBConformance,
       "ciscoFcspMIBCompliances": ciscoFcspMIBCompliances,
       "ciscoFcspMIBCompliance": ciscoFcspMIBCompliance,
       "ciscoFcspMIBGroups": ciscoFcspMIBGroups,
       "cfcspConfigGroup": cfcspConfigGroup,
       "cfcspLocalPasswdGroup": cfcspLocalPasswdGroup,
       "cfcspIfStatsGroup": cfcspIfStatsGroup,
       "cfcspNotificationGroup": cfcspNotificationGroup}
)
