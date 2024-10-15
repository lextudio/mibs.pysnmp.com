# SNMP MIB module (CISCO-LWAPP-DOT11-CLIENT-TS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CLIENT-TS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:30 2024
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

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoLwappDot11ClientTsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622)
)
ciscoLwappDot11ClientTsMIB.setRevisions(
        ("2012-06-11 00:00",
         "2012-01-25 00:00",
         "2007-03-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11ClientTsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientTsMIBNotifs = _CiscoLwappDot11ClientTsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 0)
)
_CiscoLwappDot11ClientTsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientTsMIBObjects = _CiscoLwappDot11ClientTsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1)
)
_CldctClientInfo_ObjectIdentity = ObjectIdentity
cldctClientInfo = _CldctClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1)
)
_CldctClientInfoTable_Object = MibTable
cldctClientInfoTable = _CldctClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldctClientInfoTable.setStatus("current")
_CldctClientInfoEntry_Object = MibTableRow
cldctClientInfoEntry = _CldctClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1)
)
cldctClientInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoIndex"),
)
if mibBuilder.loadTexts:
    cldctClientInfoEntry.setStatus("current")


class _CldctClientInfoIndex_Type(Unsigned32):
    """Custom type cldctClientInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CldctClientInfoIndex_Type.__name__ = "Unsigned32"
_CldctClientInfoIndex_Object = MibTableColumn
cldctClientInfoIndex = _CldctClientInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 1),
    _CldctClientInfoIndex_Type()
)
cldctClientInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldctClientInfoIndex.setStatus("current")
_CldctClientInfoGeneratedTime_Type = TimeStamp
_CldctClientInfoGeneratedTime_Object = MibTableColumn
cldctClientInfoGeneratedTime = _CldctClientInfoGeneratedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 2),
    _CldctClientInfoGeneratedTime_Type()
)
cldctClientInfoGeneratedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoGeneratedTime.setStatus("current")


class _CldctClientInfoLevel_Type(Integer32):
    """Custom type cldctClientInfoLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("phase", 1),
          ("state", 2))
    )


_CldctClientInfoLevel_Type.__name__ = "Integer32"
_CldctClientInfoLevel_Object = MibTableColumn
cldctClientInfoLevel = _CldctClientInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 3),
    _CldctClientInfoLevel_Type()
)
cldctClientInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoLevel.setStatus("current")


class _CldctClientInfoSeverity_Type(Integer32):
    """Custom type cldctClientInfoSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("error", 2),
          ("info", 1))
    )


_CldctClientInfoSeverity_Type.__name__ = "Integer32"
_CldctClientInfoSeverity_Object = MibTableColumn
cldctClientInfoSeverity = _CldctClientInfoSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 4),
    _CldctClientInfoSeverity_Type()
)
cldctClientInfoSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoSeverity.setStatus("current")


class _CldctClientInfoModule_Type(Integer32):
    """Custom type cldctClientInfoModule based on Integer32"""
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
        *(("aaa", 5),
          ("dhcp", 4),
          ("dot11", 1),
          ("dot1x", 2),
          ("misc", 7),
          ("mobility", 8),
          ("pem", 3),
          ("voiceQoS", 6))
    )


_CldctClientInfoModule_Type.__name__ = "Integer32"
_CldctClientInfoModule_Object = MibTableColumn
cldctClientInfoModule = _CldctClientInfoModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 5),
    _CldctClientInfoModule_Type()
)
cldctClientInfoModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoModule.setStatus("current")
_CldctClientInfoResultCode_Type = TruthValue
_CldctClientInfoResultCode_Object = MibTableColumn
cldctClientInfoResultCode = _CldctClientInfoResultCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 6),
    _CldctClientInfoResultCode_Type()
)
cldctClientInfoResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoResultCode.setStatus("current")


class _CldctClientInfoMsgString_Type(OctetString):
    """Custom type cldctClientInfoMsgString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldctClientInfoMsgString_Type.__name__ = "OctetString"
_CldctClientInfoMsgString_Object = MibTableColumn
cldctClientInfoMsgString = _CldctClientInfoMsgString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 7),
    _CldctClientInfoMsgString_Type()
)
cldctClientInfoMsgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoMsgString.setStatus("current")


class _CldctClientInfoMessageType_Type(Unsigned32):
    """Custom type cldctClientInfoMessageType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldctClientInfoMessageType_Type.__name__ = "Unsigned32"
_CldctClientInfoMessageType_Object = MibTableColumn
cldctClientInfoMessageType = _CldctClientInfoMessageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 8),
    _CldctClientInfoMessageType_Type()
)
cldctClientInfoMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoMessageType.setStatus("current")


class _CldctClientInfoMessageSubType_Type(Unsigned32):
    """Custom type cldctClientInfoMessageSubType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldctClientInfoMessageSubType_Type.__name__ = "Unsigned32"
_CldctClientInfoMessageSubType_Object = MibTableColumn
cldctClientInfoMessageSubType = _CldctClientInfoMessageSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 1, 1, 9),
    _CldctClientInfoMessageSubType_Type()
)
cldctClientInfoMessageSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctClientInfoMessageSubType.setStatus("current")


class _CldctClientInfoMaxEntries_Type(Unsigned32):
    """Custom type cldctClientInfoMaxEntries based on Unsigned32"""
    defaultValue = 2000


_CldctClientInfoMaxEntries_Object = MibScalar
cldctClientInfoMaxEntries = _CldctClientInfoMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 1, 2),
    _CldctClientInfoMaxEntries_Type()
)
cldctClientInfoMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldctClientInfoMaxEntries.setStatus("current")
_CldctWatchList_ObjectIdentity = ObjectIdentity
cldctWatchList = _CldctWatchList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 2)
)
_CldctWatchListTable_Object = MibTable
cldctWatchListTable = _CldctWatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cldctWatchListTable.setStatus("current")
_CldctWatchListEntry_Object = MibTableRow
cldctWatchListEntry = _CldctWatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 2, 1, 1)
)
cldctWatchListEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldctWatchListEntry.setStatus("current")


class _CldctWatchListModuleList_Type(Bits):
    """Custom type cldctWatchListModuleList based on Bits"""
    namedValues = NamedValues(
        *(("aaa", 4),
          ("dhcp", 3),
          ("dot11", 0),
          ("dot1x", 1),
          ("misc", 6),
          ("mobility", 7),
          ("pem", 2),
          ("voiceQoS", 5))
    )

_CldctWatchListModuleList_Type.__name__ = "Bits"
_CldctWatchListModuleList_Object = MibTableColumn
cldctWatchListModuleList = _CldctWatchListModuleList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 2, 1, 1, 1),
    _CldctWatchListModuleList_Type()
)
cldctWatchListModuleList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldctWatchListModuleList.setStatus("current")


class _CldctWatchListTimeRemaining_Type(Unsigned32):
    """Custom type cldctWatchListTimeRemaining based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_CldctWatchListTimeRemaining_Type.__name__ = "Unsigned32"
_CldctWatchListTimeRemaining_Object = MibTableColumn
cldctWatchListTimeRemaining = _CldctWatchListTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 2, 1, 1, 2),
    _CldctWatchListTimeRemaining_Type()
)
cldctWatchListTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldctWatchListTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cldctWatchListTimeRemaining.setUnits("minutes")
_CldctWatchListRowStatus_Type = RowStatus
_CldctWatchListRowStatus_Object = MibTableColumn
cldctWatchListRowStatus = _CldctWatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 2, 1, 1, 3),
    _CldctWatchListRowStatus_Type()
)
cldctWatchListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldctWatchListRowStatus.setStatus("current")
_CldctLastPemStateInfo_ObjectIdentity = ObjectIdentity
cldctLastPemStateInfo = _CldctLastPemStateInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 3)
)
_CldctLastPemStateTable_Object = MibTable
cldctLastPemStateTable = _CldctLastPemStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cldctLastPemStateTable.setStatus("current")
_CldctLastPemStateEntry_Object = MibTableRow
cldctLastPemStateEntry = _CldctLastPemStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 3, 1, 1)
)
cldctLastPemStateEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldctLastPemStateEntry.setStatus("current")
_CldctLastPemState_Type = SnmpAdminString
_CldctLastPemState_Object = MibTableColumn
cldctLastPemState = _CldctLastPemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 1, 3, 1, 1, 1),
    _CldctLastPemState_Type()
)
cldctLastPemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldctLastPemState.setStatus("current")
_CiscoLwappDot11ClientTsMIBConfirm_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientTsMIBConfirm = _CiscoLwappDot11ClientTsMIBConfirm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2)
)
_CiscoLwappDot11ClientTsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientTsMIBCompliances = _CiscoLwappDot11ClientTsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 1)
)
_CiscoLwappDot11ClientTsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientTsMIBGroups = _CiscoLwappDot11ClientTsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 2)
)

# Managed Objects groups

ciscoLwappDot11ClientTsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 2, 1)
)
ciscoLwappDot11ClientTsConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctWatchListModuleList"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctWatchListTimeRemaining"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientTsConfigGroup.setStatus("current")

ciscoLwappDot11ClientTsStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 2, 2)
)
ciscoLwappDot11ClientTsStatusGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoGeneratedTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoLevel"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoSeverity"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoModule"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoResultCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoMsgString"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctWatchListRowStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoMaxEntries"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctLastPemState"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientTsStatusGroup.setStatus("current")

ciscoLwappDot11ClientTsStatusSupGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 2, 3)
)
ciscoLwappDot11ClientTsStatusSupGroupRev1.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoMessageType"),
        ("CISCO-LWAPP-DOT11-CLIENT-TS-MIB", "cldctClientInfoMessageSubType"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientTsStatusSupGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappDot11ClientTsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientTsMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappDot11ClientTsMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 622, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientTsMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-TS-MIB",
    **{"ciscoLwappDot11ClientTsMIB": ciscoLwappDot11ClientTsMIB,
       "ciscoLwappDot11ClientTsMIBNotifs": ciscoLwappDot11ClientTsMIBNotifs,
       "ciscoLwappDot11ClientTsMIBObjects": ciscoLwappDot11ClientTsMIBObjects,
       "cldctClientInfo": cldctClientInfo,
       "cldctClientInfoTable": cldctClientInfoTable,
       "cldctClientInfoEntry": cldctClientInfoEntry,
       "cldctClientInfoIndex": cldctClientInfoIndex,
       "cldctClientInfoGeneratedTime": cldctClientInfoGeneratedTime,
       "cldctClientInfoLevel": cldctClientInfoLevel,
       "cldctClientInfoSeverity": cldctClientInfoSeverity,
       "cldctClientInfoModule": cldctClientInfoModule,
       "cldctClientInfoResultCode": cldctClientInfoResultCode,
       "cldctClientInfoMsgString": cldctClientInfoMsgString,
       "cldctClientInfoMessageType": cldctClientInfoMessageType,
       "cldctClientInfoMessageSubType": cldctClientInfoMessageSubType,
       "cldctClientInfoMaxEntries": cldctClientInfoMaxEntries,
       "cldctWatchList": cldctWatchList,
       "cldctWatchListTable": cldctWatchListTable,
       "cldctWatchListEntry": cldctWatchListEntry,
       "cldctWatchListModuleList": cldctWatchListModuleList,
       "cldctWatchListTimeRemaining": cldctWatchListTimeRemaining,
       "cldctWatchListRowStatus": cldctWatchListRowStatus,
       "cldctLastPemStateInfo": cldctLastPemStateInfo,
       "cldctLastPemStateTable": cldctLastPemStateTable,
       "cldctLastPemStateEntry": cldctLastPemStateEntry,
       "cldctLastPemState": cldctLastPemState,
       "ciscoLwappDot11ClientTsMIBConfirm": ciscoLwappDot11ClientTsMIBConfirm,
       "ciscoLwappDot11ClientTsMIBCompliances": ciscoLwappDot11ClientTsMIBCompliances,
       "ciscoLwappDot11ClientTsMIBCompliance": ciscoLwappDot11ClientTsMIBCompliance,
       "ciscoLwappDot11ClientTsMIBComplianceRev1": ciscoLwappDot11ClientTsMIBComplianceRev1,
       "ciscoLwappDot11ClientTsMIBGroups": ciscoLwappDot11ClientTsMIBGroups,
       "ciscoLwappDot11ClientTsConfigGroup": ciscoLwappDot11ClientTsConfigGroup,
       "ciscoLwappDot11ClientTsStatusGroup": ciscoLwappDot11ClientTsStatusGroup,
       "ciscoLwappDot11ClientTsStatusSupGroupRev1": ciscoLwappDot11ClientTsStatusSupGroupRev1}
)
