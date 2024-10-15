# SNMP MIB module (CISCO-FC-SDV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-SDV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:18 2024
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

(DomainIdOrZero,
 FcAddressId,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainIdOrZero",
    "FcAddressId",
    "FcNameIdOrZero")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(FcList,) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFcSdvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593)
)
ciscoFcSdvMIB.setRevisions(
        ("2006-09-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoFcSdvDevIdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleDevDevAlias", 2),
          ("singleDevPWWN", 1))
    )



class CiscoFcSdvDevId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class CiscoFcSdvRealDevMapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryDevMap", 1),
          ("secondaryDevMap", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFcSdvMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFcSdvMIBNotifs = _CiscoFcSdvMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 0)
)
_CiscoFcSdvMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcSdvMIBObjects = _CiscoFcSdvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1)
)
_CFcSdvConfig_ObjectIdentity = ObjectIdentity
cFcSdvConfig = _CFcSdvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1)
)
_CFcSdvVirtDeviceTable_Object = MibTable
cFcSdvVirtDeviceTable = _CFcSdvVirtDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cFcSdvVirtDeviceTable.setStatus("current")
_CFcSdvVirtDeviceEntry_Object = MibTableRow
cFcSdvVirtDeviceEntry = _CFcSdvVirtDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1)
)
cFcSdvVirtDeviceEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FC-SDV-MIB", "cFcSdvVdIndex"),
)
if mibBuilder.loadTexts:
    cFcSdvVirtDeviceEntry.setStatus("current")


class _CFcSdvVdIndex_Type(Unsigned32):
    """Custom type cFcSdvVdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CFcSdvVdIndex_Type.__name__ = "Unsigned32"
_CFcSdvVdIndex_Object = MibTableColumn
cFcSdvVdIndex = _CFcSdvVdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 1),
    _CFcSdvVdIndex_Type()
)
cFcSdvVdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cFcSdvVdIndex.setStatus("current")


class _CFcSdvVdName_Type(SnmpAdminString):
    """Custom type cFcSdvVdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CFcSdvVdName_Type.__name__ = "SnmpAdminString"
_CFcSdvVdName_Object = MibTableColumn
cFcSdvVdName = _CFcSdvVdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 2),
    _CFcSdvVdName_Type()
)
cFcSdvVdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVdName.setStatus("current")


class _CFcSdvVdVirtDomain_Type(DomainIdOrZero):
    """Custom type cFcSdvVdVirtDomain based on DomainIdOrZero"""
    defaultValue = 0


_CFcSdvVdVirtDomain_Object = MibTableColumn
cFcSdvVdVirtDomain = _CFcSdvVdVirtDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 3),
    _CFcSdvVdVirtDomain_Type()
)
cFcSdvVdVirtDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVdVirtDomain.setStatus("current")


class _CFcSdvVdFcId_Type(FcAddressId):
    """Custom type cFcSdvVdFcId based on FcAddressId"""
    defaultHexValue = "000000"


_CFcSdvVdFcId_Object = MibTableColumn
cFcSdvVdFcId = _CFcSdvVdFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 4),
    _CFcSdvVdFcId_Type()
)
cFcSdvVdFcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVdFcId.setStatus("current")
_CFcSdvVdPwwn_Type = FcNameIdOrZero
_CFcSdvVdPwwn_Object = MibTableColumn
cFcSdvVdPwwn = _CFcSdvVdPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 5),
    _CFcSdvVdPwwn_Type()
)
cFcSdvVdPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcSdvVdPwwn.setStatus("current")
_CFcSdvVdNwwn_Type = FcNameIdOrZero
_CFcSdvVdNwwn_Object = MibTableColumn
cFcSdvVdNwwn = _CFcSdvVdNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 6),
    _CFcSdvVdNwwn_Type()
)
cFcSdvVdNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcSdvVdNwwn.setStatus("current")
_CFcSdvVdAssignedFcId_Type = FcAddressId
_CFcSdvVdAssignedFcId_Object = MibTableColumn
cFcSdvVdAssignedFcId = _CFcSdvVdAssignedFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 7),
    _CFcSdvVdAssignedFcId_Type()
)
cFcSdvVdAssignedFcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcSdvVdAssignedFcId.setStatus("current")


class _CFcSdvVdRealDevMapList_Type(FcList):
    """Custom type cFcSdvVdRealDevMapList based on FcList"""
    defaultHexValue = ""

    subtypeSpec = FcList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CFcSdvVdRealDevMapList_Type.__name__ = "FcList"
_CFcSdvVdRealDevMapList_Object = MibTableColumn
cFcSdvVdRealDevMapList = _CFcSdvVdRealDevMapList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 8),
    _CFcSdvVdRealDevMapList_Type()
)
cFcSdvVdRealDevMapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcSdvVdRealDevMapList.setStatus("current")


class _CFcSdvVdStorageType_Type(StorageType):
    """Custom type cFcSdvVdStorageType based on StorageType"""


_CFcSdvVdStorageType_Object = MibTableColumn
cFcSdvVdStorageType = _CFcSdvVdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 9),
    _CFcSdvVdStorageType_Type()
)
cFcSdvVdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVdStorageType.setStatus("current")
_CFcSdvVdRowStatus_Type = RowStatus
_CFcSdvVdRowStatus_Object = MibTableColumn
cFcSdvVdRowStatus = _CFcSdvVdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 10),
    _CFcSdvVdRowStatus_Type()
)
cFcSdvVdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVdRowStatus.setStatus("current")
_CFcSdvVirtRealDevMapTable_Object = MibTable
cFcSdvVirtRealDevMapTable = _CFcSdvVirtRealDevMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cFcSdvVirtRealDevMapTable.setStatus("current")
_CFcSdvVirtRealDevMapEntry_Object = MibTableRow
cFcSdvVirtRealDevMapEntry = _CFcSdvVirtRealDevMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1)
)
cFcSdvVirtRealDevMapEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FC-SDV-MIB", "cFcSdvVdIndex"),
    (0, "CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapIndex"),
)
if mibBuilder.loadTexts:
    cFcSdvVirtRealDevMapEntry.setStatus("current")


class _CFcSdvVirtRealDevMapIndex_Type(Unsigned32):
    """Custom type cFcSdvVirtRealDevMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CFcSdvVirtRealDevMapIndex_Type.__name__ = "Unsigned32"
_CFcSdvVirtRealDevMapIndex_Object = MibTableColumn
cFcSdvVirtRealDevMapIndex = _CFcSdvVirtRealDevMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 1),
    _CFcSdvVirtRealDevMapIndex_Type()
)
cFcSdvVirtRealDevMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cFcSdvVirtRealDevMapIndex.setStatus("current")


class _CFcSdvVirtRealDeviceIdType_Type(CiscoFcSdvDevIdType):
    """Custom type cFcSdvVirtRealDeviceIdType based on CiscoFcSdvDevIdType"""


_CFcSdvVirtRealDeviceIdType_Object = MibTableColumn
cFcSdvVirtRealDeviceIdType = _CFcSdvVirtRealDeviceIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 2),
    _CFcSdvVirtRealDeviceIdType_Type()
)
cFcSdvVirtRealDeviceIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVirtRealDeviceIdType.setStatus("current")


class _CFcSdvVirtRealDeviceId_Type(CiscoFcSdvDevId):
    """Custom type cFcSdvVirtRealDeviceId based on CiscoFcSdvDevId"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = CiscoFcSdvDevId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CFcSdvVirtRealDeviceId_Type.__name__ = "CiscoFcSdvDevId"
_CFcSdvVirtRealDeviceId_Object = MibTableColumn
cFcSdvVirtRealDeviceId = _CFcSdvVirtRealDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 3),
    _CFcSdvVirtRealDeviceId_Type()
)
cFcSdvVirtRealDeviceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVirtRealDeviceId.setStatus("current")


class _CFcSdvVirtRealDevMapType_Type(CiscoFcSdvRealDevMapType):
    """Custom type cFcSdvVirtRealDevMapType based on CiscoFcSdvRealDevMapType"""


_CFcSdvVirtRealDevMapType_Object = MibTableColumn
cFcSdvVirtRealDevMapType = _CFcSdvVirtRealDevMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 4),
    _CFcSdvVirtRealDevMapType_Type()
)
cFcSdvVirtRealDevMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVirtRealDevMapType.setStatus("current")


class _CFcSdvVirtRealDevMapStorageType_Type(StorageType):
    """Custom type cFcSdvVirtRealDevMapStorageType based on StorageType"""


_CFcSdvVirtRealDevMapStorageType_Object = MibTableColumn
cFcSdvVirtRealDevMapStorageType = _CFcSdvVirtRealDevMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 5),
    _CFcSdvVirtRealDevMapStorageType_Type()
)
cFcSdvVirtRealDevMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVirtRealDevMapStorageType.setStatus("current")
_CFcSdvVirtRealDevMapRowStatus_Type = RowStatus
_CFcSdvVirtRealDevMapRowStatus_Object = MibTableColumn
cFcSdvVirtRealDevMapRowStatus = _CFcSdvVirtRealDevMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 6),
    _CFcSdvVirtRealDevMapRowStatus_Type()
)
cFcSdvVirtRealDevMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cFcSdvVirtRealDevMapRowStatus.setStatus("current")
_CiscoFcSdvMIBConform_ObjectIdentity = ObjectIdentity
ciscoFcSdvMIBConform = _CiscoFcSdvMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 2)
)
_CiscoFcSdvMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFcSdvMIBCompliances = _CiscoFcSdvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 1)
)
_CiscoFcSdvMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFcSdvMIBGroups = _CiscoFcSdvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 2)
)

# Managed Objects groups

ciscoFcSdvConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 2, 1)
)
ciscoFcSdvConfigGroup.setObjects(
      *(("CISCO-FC-SDV-MIB", "cFcSdvVdName"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdVirtDomain"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdFcId"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdPwwn"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdNwwn"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdAssignedFcId"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdStorageType"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdRealDevMapList"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVdRowStatus"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDeviceIdType"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDeviceId"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapType"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapStorageType"),
        ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFcSdvConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFcSdvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFcSdvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-SDV-MIB",
    **{"CiscoFcSdvDevIdType": CiscoFcSdvDevIdType,
       "CiscoFcSdvDevId": CiscoFcSdvDevId,
       "CiscoFcSdvRealDevMapType": CiscoFcSdvRealDevMapType,
       "ciscoFcSdvMIB": ciscoFcSdvMIB,
       "ciscoFcSdvMIBNotifs": ciscoFcSdvMIBNotifs,
       "ciscoFcSdvMIBObjects": ciscoFcSdvMIBObjects,
       "cFcSdvConfig": cFcSdvConfig,
       "cFcSdvVirtDeviceTable": cFcSdvVirtDeviceTable,
       "cFcSdvVirtDeviceEntry": cFcSdvVirtDeviceEntry,
       "cFcSdvVdIndex": cFcSdvVdIndex,
       "cFcSdvVdName": cFcSdvVdName,
       "cFcSdvVdVirtDomain": cFcSdvVdVirtDomain,
       "cFcSdvVdFcId": cFcSdvVdFcId,
       "cFcSdvVdPwwn": cFcSdvVdPwwn,
       "cFcSdvVdNwwn": cFcSdvVdNwwn,
       "cFcSdvVdAssignedFcId": cFcSdvVdAssignedFcId,
       "cFcSdvVdRealDevMapList": cFcSdvVdRealDevMapList,
       "cFcSdvVdStorageType": cFcSdvVdStorageType,
       "cFcSdvVdRowStatus": cFcSdvVdRowStatus,
       "cFcSdvVirtRealDevMapTable": cFcSdvVirtRealDevMapTable,
       "cFcSdvVirtRealDevMapEntry": cFcSdvVirtRealDevMapEntry,
       "cFcSdvVirtRealDevMapIndex": cFcSdvVirtRealDevMapIndex,
       "cFcSdvVirtRealDeviceIdType": cFcSdvVirtRealDeviceIdType,
       "cFcSdvVirtRealDeviceId": cFcSdvVirtRealDeviceId,
       "cFcSdvVirtRealDevMapType": cFcSdvVirtRealDevMapType,
       "cFcSdvVirtRealDevMapStorageType": cFcSdvVirtRealDevMapStorageType,
       "cFcSdvVirtRealDevMapRowStatus": cFcSdvVirtRealDevMapRowStatus,
       "ciscoFcSdvMIBConform": ciscoFcSdvMIBConform,
       "ciscoFcSdvMIBCompliances": ciscoFcSdvMIBCompliances,
       "ciscoFcSdvMIBCompliance": ciscoFcSdvMIBCompliance,
       "ciscoFcSdvMIBGroups": ciscoFcSdvMIBGroups,
       "ciscoFcSdvConfigGroup": ciscoFcSdvConfigGroup}
)
