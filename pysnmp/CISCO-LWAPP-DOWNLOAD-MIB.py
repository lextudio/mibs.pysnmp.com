# SNMP MIB module (CISCO-LWAPP-DOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOWNLOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:32 2024
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

(cLApSysMacAddress,
 ciscoLwappApMIB) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress",
    "ciscoLwappApMIB")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDownloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4)
)
ciscoLwappDownloadMIB.setRevisions(
        ("2008-05-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDownloadMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBNotifs = _CiscoLwappDownloadMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0)
)
_CiscoLwappDownloadMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBObjects = _CiscoLwappDownloadMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1)
)
_CiscoLwappDLApBoot_ObjectIdentity = ObjectIdentity
ciscoLwappDLApBoot = _CiscoLwappDLApBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1)
)
_ClDLApBootTable_Object = MibTable
clDLApBootTable = _ClDLApBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clDLApBootTable.setStatus("current")
_CldlApBootEntry_Object = MibTableRow
cldlApBootEntry = _CldlApBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1)
)
cldlApBootEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cldlApBootEntry.setStatus("current")
_CldlAPName_Type = SnmpAdminString
_CldlAPName_Object = MibTableColumn
cldlAPName = _CldlAPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 1),
    _CldlAPName_Type()
)
cldlAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPName.setStatus("current")
_CldlAPPrimaryVersion_Type = SnmpAdminString
_CldlAPPrimaryVersion_Object = MibTableColumn
cldlAPPrimaryVersion = _CldlAPPrimaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 2),
    _CldlAPPrimaryVersion_Type()
)
cldlAPPrimaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPPrimaryVersion.setStatus("current")
_CldlAPBackupVersion_Type = SnmpAdminString
_CldlAPBackupVersion_Object = MibTableColumn
cldlAPBackupVersion = _CldlAPBackupVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 3),
    _CldlAPBackupVersion_Type()
)
cldlAPBackupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPBackupVersion.setStatus("current")


class _CldlAPSwapImage_Type(TruthValue):
    """Custom type cldlAPSwapImage based on TruthValue"""


_CldlAPSwapImage_Object = MibTableColumn
cldlAPSwapImage = _CldlAPSwapImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 4),
    _CldlAPSwapImage_Type()
)
cldlAPSwapImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlAPSwapImage.setStatus("current")


class _CldlApDownloadImage_Type(Integer32):
    """Custom type cldlApDownloadImage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_CldlApDownloadImage_Type.__name__ = "Integer32"
_CldlApDownloadImage_Object = MibTableColumn
cldlApDownloadImage = _CldlApDownloadImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 5),
    _CldlApDownloadImage_Type()
)
cldlApDownloadImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlApDownloadImage.setStatus("current")
_CiscoLwappDLReset_ObjectIdentity = ObjectIdentity
ciscoLwappDLReset = _CiscoLwappDLReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2)
)
_ClDLResetTable_Object = MibTable
clDLResetTable = _ClDLResetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clDLResetTable.setStatus("current")
_CldlResetEntry_Object = MibTableRow
cldlResetEntry = _CldlResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1)
)
cldlResetEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetIndex"),
)
if mibBuilder.loadTexts:
    cldlResetEntry.setStatus("current")
_CldlResetIndex_Type = Unsigned32
_CldlResetIndex_Object = MibTableColumn
cldlResetIndex = _CldlResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 1),
    _CldlResetIndex_Type()
)
cldlResetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldlResetIndex.setStatus("current")
_CldlResetDateAndTime_Type = DateAndTime
_CldlResetDateAndTime_Object = MibTableColumn
cldlResetDateAndTime = _CldlResetDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 2),
    _CldlResetDateAndTime_Type()
)
cldlResetDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetDateAndTime.setStatus("current")


class _CldlResetSwapImage_Type(TruthValue):
    """Custom type cldlResetSwapImage based on TruthValue"""


_CldlResetSwapImage_Object = MibTableColumn
cldlResetSwapImage = _CldlResetSwapImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 3),
    _CldlResetSwapImage_Type()
)
cldlResetSwapImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetSwapImage.setStatus("current")


class _CldlResetAP_Type(TruthValue):
    """Custom type cldlResetAP based on TruthValue"""


_CldlResetAP_Object = MibTableColumn
cldlResetAP = _CldlResetAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 4),
    _CldlResetAP_Type()
)
cldlResetAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetAP.setStatus("current")
_CldlResetRowStatus_Type = RowStatus
_CldlResetRowStatus_Object = MibTableColumn
cldlResetRowStatus = _CldlResetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 5),
    _CldlResetRowStatus_Type()
)
cldlResetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetRowStatus.setStatus("current")


class _CldlResetSaveConfig_Type(TruthValue):
    """Custom type cldlResetSaveConfig based on TruthValue"""


_CldlResetSaveConfig_Object = MibTableColumn
cldlResetSaveConfig = _CldlResetSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 6),
    _CldlResetSaveConfig_Type()
)
cldlResetSaveConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetSaveConfig.setStatus("current")
_CldlResetAlertTime_Type = Unsigned32
_CldlResetAlertTime_Object = MibTableColumn
cldlResetAlertTime = _CldlResetAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 7),
    _CldlResetAlertTime_Type()
)
cldlResetAlertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetAlertTime.setStatus("current")
_CiscoLwappDownloadMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBConform = _CiscoLwappDownloadMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2)
)
_CiscoLwappDownloadMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBCompliances = _CiscoLwappDownloadMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 1)
)
_CiscoLwappDownloadMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBGroups = _CiscoLwappDownloadMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2)
)

# Managed Objects groups

ciscoLwappDLApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 1)
)
ciscoLwappDLApGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPName"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPPrimaryVersion"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPBackupVersion"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPSwapImage"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlApDownloadImage"))
)
if mibBuilder.loadTexts:
    ciscoLwappDLApGroup.setStatus("current")

ciscoLwappDLResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 2)
)
ciscoLwappDLResetGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetDateAndTime"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetSwapImage"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAP"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetRowStatus"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetSaveConfig"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAlertTime"))
)
if mibBuilder.loadTexts:
    ciscoLwappDLResetGroup.setStatus("current")


# Notification objects

ciscoLwappScheduledResetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0, 1)
)
ciscoLwappScheduledResetNotif.setObjects(
    ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAlertTime")
)
if mibBuilder.loadTexts:
    ciscoLwappScheduledResetNotif.setStatus(
        "current"
    )

ciscoLwappResetFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappResetFailedNotif.setStatus(
        "current"
    )

ciscoLwappClearResetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappClearResetNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappDLNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 3)
)
ciscoLwappDLNotifsGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "ciscoLwappScheduledResetNotif"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "ciscoLwappResetFailedNotif"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "ciscoLwappClearResetNotif"))
)
if mibBuilder.loadTexts:
    ciscoLwappDLNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappDownloadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDownloadMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOWNLOAD-MIB",
    **{"ciscoLwappDownloadMIB": ciscoLwappDownloadMIB,
       "ciscoLwappDownloadMIBNotifs": ciscoLwappDownloadMIBNotifs,
       "ciscoLwappScheduledResetNotif": ciscoLwappScheduledResetNotif,
       "ciscoLwappResetFailedNotif": ciscoLwappResetFailedNotif,
       "ciscoLwappClearResetNotif": ciscoLwappClearResetNotif,
       "ciscoLwappDownloadMIBObjects": ciscoLwappDownloadMIBObjects,
       "ciscoLwappDLApBoot": ciscoLwappDLApBoot,
       "clDLApBootTable": clDLApBootTable,
       "cldlApBootEntry": cldlApBootEntry,
       "cldlAPName": cldlAPName,
       "cldlAPPrimaryVersion": cldlAPPrimaryVersion,
       "cldlAPBackupVersion": cldlAPBackupVersion,
       "cldlAPSwapImage": cldlAPSwapImage,
       "cldlApDownloadImage": cldlApDownloadImage,
       "ciscoLwappDLReset": ciscoLwappDLReset,
       "clDLResetTable": clDLResetTable,
       "cldlResetEntry": cldlResetEntry,
       "cldlResetIndex": cldlResetIndex,
       "cldlResetDateAndTime": cldlResetDateAndTime,
       "cldlResetSwapImage": cldlResetSwapImage,
       "cldlResetAP": cldlResetAP,
       "cldlResetRowStatus": cldlResetRowStatus,
       "cldlResetSaveConfig": cldlResetSaveConfig,
       "cldlResetAlertTime": cldlResetAlertTime,
       "ciscoLwappDownloadMIBConform": ciscoLwappDownloadMIBConform,
       "ciscoLwappDownloadMIBCompliances": ciscoLwappDownloadMIBCompliances,
       "ciscoLwappDownloadMIBCompliance": ciscoLwappDownloadMIBCompliance,
       "ciscoLwappDownloadMIBGroups": ciscoLwappDownloadMIBGroups,
       "ciscoLwappDLApGroup": ciscoLwappDLApGroup,
       "ciscoLwappDLResetGroup": ciscoLwappDLResetGroup,
       "ciscoLwappDLNotifsGroup": ciscoLwappDLNotifsGroup}
)
