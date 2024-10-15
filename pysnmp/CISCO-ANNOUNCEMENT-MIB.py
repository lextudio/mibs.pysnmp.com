# SNMP MIB module (CISCO-ANNOUNCEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ANNOUNCEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:35 2024
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

(cmgwIndex,) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAnnouncementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888)
)
ciscoAnnouncementMIB.setRevisions(
        ("2003-03-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAnnouncementMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoAnnouncementMIBNotifs = _CiscoAnnouncementMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 0)
)
_CiscoAnnouncementMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAnnouncementMIBObjects = _CiscoAnnouncementMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1)
)
_CannoGeneric_ObjectIdentity = ObjectIdentity
cannoGeneric = _CannoGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1)
)
_CannoControlConfig_ObjectIdentity = ObjectIdentity
cannoControlConfig = _CannoControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1)
)
_CannoControlTable_Object = MibTable
cannoControlTable = _CannoControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cannoControlTable.setStatus("current")
_CannoControlEntry_Object = MibTableRow
cannoControlEntry = _CannoControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1)
)
cannoControlEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cannoControlEntry.setStatus("current")


class _CannoAudioFileServerName_Type(SnmpAdminString):
    """Custom type cannoAudioFileServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CannoAudioFileServerName_Type.__name__ = "SnmpAdminString"
_CannoAudioFileServerName_Object = MibTableColumn
cannoAudioFileServerName = _CannoAudioFileServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 1),
    _CannoAudioFileServerName_Type()
)
cannoAudioFileServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoAudioFileServerName.setStatus("current")


class _CannoDnResolution_Type(Integer32):
    """Custom type cannoDnResolution based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalOnly", 2),
          ("internalOnly", 1))
    )


_CannoDnResolution_Type.__name__ = "Integer32"
_CannoDnResolution_Object = MibTableColumn
cannoDnResolution = _CannoDnResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 2),
    _CannoDnResolution_Type()
)
cannoDnResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoDnResolution.setStatus("current")


class _CannoIpAddressType_Type(InetAddressType):
    """Custom type cannoIpAddressType based on InetAddressType"""


_CannoIpAddressType_Object = MibTableColumn
cannoIpAddressType = _CannoIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 3),
    _CannoIpAddressType_Type()
)
cannoIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoIpAddressType.setStatus("current")


class _CannoIpAddress_Type(InetAddress):
    """Custom type cannoIpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CannoIpAddress_Object = MibTableColumn
cannoIpAddress = _CannoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 4),
    _CannoIpAddress_Type()
)
cannoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoIpAddress.setStatus("current")


class _CannoAgeTime_Type(Unsigned32):
    """Custom type cannoAgeTime based on Unsigned32"""
    defaultValue = 10080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CannoAgeTime_Type.__name__ = "Unsigned32"
_CannoAgeTime_Object = MibTableColumn
cannoAgeTime = _CannoAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 5),
    _CannoAgeTime_Type()
)
cannoAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    cannoAgeTime.setUnits("minutes")


class _CannoSubDirPath_Type(SnmpAdminString):
    """Custom type cannoSubDirPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CannoSubDirPath_Type.__name__ = "SnmpAdminString"
_CannoSubDirPath_Object = MibTableColumn
cannoSubDirPath = _CannoSubDirPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 6),
    _CannoSubDirPath_Type()
)
cannoSubDirPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoSubDirPath.setStatus("current")


class _CannoReqTimeout_Type(Unsigned32):
    """Custom type cannoReqTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CannoReqTimeout_Type.__name__ = "Unsigned32"
_CannoReqTimeout_Object = MibTableColumn
cannoReqTimeout = _CannoReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 7),
    _CannoReqTimeout_Type()
)
cannoReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoReqTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cannoReqTimeout.setUnits("seconds")


class _CannoMaxPermanent_Type(Unsigned32):
    """Custom type cannoMaxPermanent based on Unsigned32"""
    defaultValue = 41

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CannoMaxPermanent_Type.__name__ = "Unsigned32"
_CannoMaxPermanent_Object = MibTableColumn
cannoMaxPermanent = _CannoMaxPermanent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 8),
    _CannoMaxPermanent_Type()
)
cannoMaxPermanent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cannoMaxPermanent.setStatus("current")
_CannoAudioFileConfig_ObjectIdentity = ObjectIdentity
cannoAudioFileConfig = _CannoAudioFileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2)
)
_CannoAudioFileTable_Object = MibTable
cannoAudioFileTable = _CannoAudioFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cannoAudioFileTable.setStatus("current")
_CannoAudioFileEntry_Object = MibTableRow
cannoAudioFileEntry = _CannoAudioFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1)
)
cannoAudioFileEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileNumber"),
)
if mibBuilder.loadTexts:
    cannoAudioFileEntry.setStatus("current")


class _CannoAudioFileNumber_Type(Unsigned32):
    """Custom type cannoAudioFileNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CannoAudioFileNumber_Type.__name__ = "Unsigned32"
_CannoAudioFileNumber_Object = MibTableColumn
cannoAudioFileNumber = _CannoAudioFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 1),
    _CannoAudioFileNumber_Type()
)
cannoAudioFileNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cannoAudioFileNumber.setStatus("current")


class _CannoAudioFileDescr_Type(SnmpAdminString):
    """Custom type cannoAudioFileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CannoAudioFileDescr_Type.__name__ = "SnmpAdminString"
_CannoAudioFileDescr_Object = MibTableColumn
cannoAudioFileDescr = _CannoAudioFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 2),
    _CannoAudioFileDescr_Type()
)
cannoAudioFileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFileDescr.setStatus("current")


class _CannoAudioFileName_Type(SnmpAdminString):
    """Custom type cannoAudioFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CannoAudioFileName_Type.__name__ = "SnmpAdminString"
_CannoAudioFileName_Object = MibTableColumn
cannoAudioFileName = _CannoAudioFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 3),
    _CannoAudioFileName_Type()
)
cannoAudioFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFileName.setStatus("current")


class _CannoAudioFileStatus_Type(Integer32):
    """Custom type cannoAudioFileStatus based on Integer32"""
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
        *(("cached", 1),
          ("invalidFile", 3),
          ("loadFailed", 4),
          ("loading", 2),
          ("notCached", 5))
    )


_CannoAudioFileStatus_Type.__name__ = "Integer32"
_CannoAudioFileStatus_Object = MibTableColumn
cannoAudioFileStatus = _CannoAudioFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 4),
    _CannoAudioFileStatus_Type()
)
cannoAudioFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cannoAudioFileStatus.setStatus("current")


class _CannoAudioFileOperStatus_Type(Integer32):
    """Custom type cannoAudioFileOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delPending", 3),
          ("inPlaying", 1),
          ("notPlaying", 2))
    )


_CannoAudioFileOperStatus_Type.__name__ = "Integer32"
_CannoAudioFileOperStatus_Object = MibTableColumn
cannoAudioFileOperStatus = _CannoAudioFileOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 5),
    _CannoAudioFileOperStatus_Type()
)
cannoAudioFileOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cannoAudioFileOperStatus.setStatus("current")


class _CannoAudioFilePlayNoc_Type(Unsigned32):
    """Custom type cannoAudioFilePlayNoc based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CannoAudioFilePlayNoc_Type.__name__ = "Unsigned32"
_CannoAudioFilePlayNoc_Object = MibTableColumn
cannoAudioFilePlayNoc = _CannoAudioFilePlayNoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 6),
    _CannoAudioFilePlayNoc_Type()
)
cannoAudioFilePlayNoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFilePlayNoc.setStatus("current")


class _CannoAudioFileDuration_Type(Unsigned32):
    """Custom type cannoAudioFileDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CannoAudioFileDuration_Type.__name__ = "Unsigned32"
_CannoAudioFileDuration_Object = MibTableColumn
cannoAudioFileDuration = _CannoAudioFileDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 7),
    _CannoAudioFileDuration_Type()
)
cannoAudioFileDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFileDuration.setStatus("current")
if mibBuilder.loadTexts:
    cannoAudioFileDuration.setUnits("10 milliseconds")


class _CannoAudioFileType_Type(Integer32):
    """Custom type cannoAudioFileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_CannoAudioFileType_Type.__name__ = "Integer32"
_CannoAudioFileType_Object = MibTableColumn
cannoAudioFileType = _CannoAudioFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 8),
    _CannoAudioFileType_Type()
)
cannoAudioFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFileType.setStatus("current")


class _CannoAudioFileAge_Type(Unsigned32):
    """Custom type cannoAudioFileAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CannoAudioFileAge_Type.__name__ = "Unsigned32"
_CannoAudioFileAge_Object = MibTableColumn
cannoAudioFileAge = _CannoAudioFileAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 9),
    _CannoAudioFileAge_Type()
)
cannoAudioFileAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cannoAudioFileAge.setStatus("current")
if mibBuilder.loadTexts:
    cannoAudioFileAge.setUnits("minutes")


class _CannoAudioFileAdminDeletion_Type(Integer32):
    """Custom type cannoAudioFileAdminDeletion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcefully", 2),
          ("gracefully", 1))
    )


_CannoAudioFileAdminDeletion_Type.__name__ = "Integer32"
_CannoAudioFileAdminDeletion_Object = MibTableColumn
cannoAudioFileAdminDeletion = _CannoAudioFileAdminDeletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 10),
    _CannoAudioFileAdminDeletion_Type()
)
cannoAudioFileAdminDeletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFileAdminDeletion.setStatus("current")
_CannoAudioFileRowStatus_Type = RowStatus
_CannoAudioFileRowStatus_Object = MibTableColumn
cannoAudioFileRowStatus = _CannoAudioFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 11),
    _CannoAudioFileRowStatus_Type()
)
cannoAudioFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cannoAudioFileRowStatus.setStatus("current")
_CiscoAnnouncementMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAnnouncementMIBConformance = _CiscoAnnouncementMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 2)
)
_CannoMIBCompliances_ObjectIdentity = ObjectIdentity
cannoMIBCompliances = _CannoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 1)
)
_CannoMIBGroups_ObjectIdentity = ObjectIdentity
cannoMIBGroups = _CannoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 2)
)

# Managed Objects groups

cannoControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 2, 1)
)
cannoControlGroup.setObjects(
      *(("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileServerName"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoDnResolution"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoIpAddressType"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoIpAddress"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAgeTime"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoSubDirPath"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoReqTimeout"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoMaxPermanent"))
)
if mibBuilder.loadTexts:
    cannoControlGroup.setStatus("current")

cannoAudioFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 2, 2)
)
cannoAudioFileGroup.setObjects(
      *(("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileDescr"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileName"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileStatus"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileOperStatus"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFilePlayNoc"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileDuration"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileType"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileAge"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileAdminDeletion"),
        ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileRowStatus"))
)
if mibBuilder.loadTexts:
    cannoAudioFileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cannoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cannoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ANNOUNCEMENT-MIB",
    **{"ciscoAnnouncementMIB": ciscoAnnouncementMIB,
       "ciscoAnnouncementMIBNotifs": ciscoAnnouncementMIBNotifs,
       "ciscoAnnouncementMIBObjects": ciscoAnnouncementMIBObjects,
       "cannoGeneric": cannoGeneric,
       "cannoControlConfig": cannoControlConfig,
       "cannoControlTable": cannoControlTable,
       "cannoControlEntry": cannoControlEntry,
       "cannoAudioFileServerName": cannoAudioFileServerName,
       "cannoDnResolution": cannoDnResolution,
       "cannoIpAddressType": cannoIpAddressType,
       "cannoIpAddress": cannoIpAddress,
       "cannoAgeTime": cannoAgeTime,
       "cannoSubDirPath": cannoSubDirPath,
       "cannoReqTimeout": cannoReqTimeout,
       "cannoMaxPermanent": cannoMaxPermanent,
       "cannoAudioFileConfig": cannoAudioFileConfig,
       "cannoAudioFileTable": cannoAudioFileTable,
       "cannoAudioFileEntry": cannoAudioFileEntry,
       "cannoAudioFileNumber": cannoAudioFileNumber,
       "cannoAudioFileDescr": cannoAudioFileDescr,
       "cannoAudioFileName": cannoAudioFileName,
       "cannoAudioFileStatus": cannoAudioFileStatus,
       "cannoAudioFileOperStatus": cannoAudioFileOperStatus,
       "cannoAudioFilePlayNoc": cannoAudioFilePlayNoc,
       "cannoAudioFileDuration": cannoAudioFileDuration,
       "cannoAudioFileType": cannoAudioFileType,
       "cannoAudioFileAge": cannoAudioFileAge,
       "cannoAudioFileAdminDeletion": cannoAudioFileAdminDeletion,
       "cannoAudioFileRowStatus": cannoAudioFileRowStatus,
       "ciscoAnnouncementMIBConformance": ciscoAnnouncementMIBConformance,
       "cannoMIBCompliances": cannoMIBCompliances,
       "cannoMIBCompliance": cannoMIBCompliance,
       "cannoMIBGroups": cannoMIBGroups,
       "cannoControlGroup": cannoControlGroup,
       "cannoAudioFileGroup": cannoAudioFileGroup}
)
