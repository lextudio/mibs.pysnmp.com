# SNMP MIB module (CISCO-WWNMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WWNMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:46 2024
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

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWwnmgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286)
)
ciscoWwnmgrMIB.setRevisions(
        ("2006-02-06 00:00",
         "2002-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWwnmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWwnmMIBObjects = _CiscoWwnmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1)
)
_WwnmConfigurationGroup_ObjectIdentity = ObjectIdentity
wwnmConfigurationGroup = _WwnmConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1)
)


class _WwnmSecondaryBaseMacAddress_Type(MacAddress):
    """Custom type wwnmSecondaryBaseMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_WwnmSecondaryBaseMacAddress_Object = MibScalar
wwnmSecondaryBaseMacAddress = _WwnmSecondaryBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 1),
    _WwnmSecondaryBaseMacAddress_Type()
)
wwnmSecondaryBaseMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnmSecondaryBaseMacAddress.setStatus("current")


class _WwnmSecondaryMacAddressRange_Type(Unsigned32):
    """Custom type wwnmSecondaryMacAddressRange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwnmSecondaryMacAddressRange_Type.__name__ = "Unsigned32"
_WwnmSecondaryMacAddressRange_Object = MibScalar
wwnmSecondaryMacAddressRange = _WwnmSecondaryMacAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 2),
    _WwnmSecondaryMacAddressRange_Type()
)
wwnmSecondaryMacAddressRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnmSecondaryMacAddressRange.setStatus("current")


class _WwnmType1MaxWwns_Type(Unsigned32):
    """Custom type wwnmType1MaxWwns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwnmType1MaxWwns_Type.__name__ = "Unsigned32"
_WwnmType1MaxWwns_Object = MibScalar
wwnmType1MaxWwns = _WwnmType1MaxWwns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 3),
    _WwnmType1MaxWwns_Type()
)
wwnmType1MaxWwns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmType1MaxWwns.setStatus("current")
_WwnmType1AvailableWwns_Type = Gauge32
_WwnmType1AvailableWwns_Object = MibScalar
wwnmType1AvailableWwns = _WwnmType1AvailableWwns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 4),
    _WwnmType1AvailableWwns_Type()
)
wwnmType1AvailableWwns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmType1AvailableWwns.setStatus("current")


class _WwnmTypeOtherMaxWwns_Type(Unsigned32):
    """Custom type wwnmTypeOtherMaxWwns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwnmTypeOtherMaxWwns_Type.__name__ = "Unsigned32"
_WwnmTypeOtherMaxWwns_Object = MibScalar
wwnmTypeOtherMaxWwns = _WwnmTypeOtherMaxWwns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 5),
    _WwnmTypeOtherMaxWwns_Type()
)
wwnmTypeOtherMaxWwns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmTypeOtherMaxWwns.setStatus("current")
_WwnmTypeOtherAvailableWwns_Type = Gauge32
_WwnmTypeOtherAvailableWwns_Object = MibScalar
wwnmTypeOtherAvailableWwns = _WwnmTypeOtherAvailableWwns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 6),
    _WwnmTypeOtherAvailableWwns_Type()
)
wwnmTypeOtherAvailableWwns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmTypeOtherAvailableWwns.setStatus("current")


class _WwnmType1ReservedWwns_Type(Unsigned32):
    """Custom type wwnmType1ReservedWwns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwnmType1ReservedWwns_Type.__name__ = "Unsigned32"
_WwnmType1ReservedWwns_Object = MibScalar
wwnmType1ReservedWwns = _WwnmType1ReservedWwns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 7),
    _WwnmType1ReservedWwns_Type()
)
wwnmType1ReservedWwns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmType1ReservedWwns.setStatus("current")


class _WwnmTypeOtherReservedWwns_Type(Unsigned32):
    """Custom type wwnmTypeOtherReservedWwns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwnmTypeOtherReservedWwns_Type.__name__ = "Unsigned32"
_WwnmTypeOtherReservedWwns_Object = MibScalar
wwnmTypeOtherReservedWwns = _WwnmTypeOtherReservedWwns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 8),
    _WwnmTypeOtherReservedWwns_Type()
)
wwnmTypeOtherReservedWwns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmTypeOtherReservedWwns.setStatus("current")
_WwnmVsanWwnTable_Object = MibTable
wwnmVsanWwnTable = _WwnmVsanWwnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wwnmVsanWwnTable.setStatus("current")
_WwnmVsanWwnEntry_Object = MibTableRow
wwnmVsanWwnEntry = _WwnmVsanWwnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1)
)
wwnmVsanWwnEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    wwnmVsanWwnEntry.setStatus("current")
_WwnmVsanWwn_Type = FcNameId
_WwnmVsanWwn_Object = MibTableColumn
wwnmVsanWwn = _WwnmVsanWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1, 1),
    _WwnmVsanWwn_Type()
)
wwnmVsanWwn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwnmVsanWwn.setStatus("current")


class _WwnmVsanWwnStorageType_Type(StorageType):
    """Custom type wwnmVsanWwnStorageType based on StorageType"""


_WwnmVsanWwnStorageType_Object = MibTableColumn
wwnmVsanWwnStorageType = _WwnmVsanWwnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1, 2),
    _WwnmVsanWwnStorageType_Type()
)
wwnmVsanWwnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnmVsanWwnStorageType.setStatus("current")
_WwnmVsanWwnRowStatus_Type = RowStatus
_WwnmVsanWwnRowStatus_Object = MibTableColumn
wwnmVsanWwnRowStatus = _WwnmVsanWwnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1, 3),
    _WwnmVsanWwnRowStatus_Type()
)
wwnmVsanWwnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwnmVsanWwnRowStatus.setStatus("current")
_WwnmNotificationGroup_ObjectIdentity = ObjectIdentity
wwnmNotificationGroup = _WwnmNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2)
)
_WwnmNotification_ObjectIdentity = ObjectIdentity
wwnmNotification = _WwnmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1)
)
_WwnmNotificationPrefix_ObjectIdentity = ObjectIdentity
wwnmNotificationPrefix = _WwnmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0)
)
_CiscoWwnmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWwnmMIBConformance = _CiscoWwnmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2)
)
_CiscoWwnmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWwnmMIBCompliances = _CiscoWwnmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 1)
)
_CiscoWwnmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWwnmMIBGroups = _CiscoWwnmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2)
)

# Managed Objects groups

cwmWwnmConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2, 6)
)
cwmWwnmConfigurationGroup.setObjects(
      *(("CISCO-WWNMGR-MIB", "wwnmSecondaryBaseMacAddress"),
        ("CISCO-WWNMGR-MIB", "wwnmSecondaryMacAddressRange"),
        ("CISCO-WWNMGR-MIB", "wwnmType1MaxWwns"),
        ("CISCO-WWNMGR-MIB", "wwnmType1AvailableWwns"),
        ("CISCO-WWNMGR-MIB", "wwnmTypeOtherMaxWwns"),
        ("CISCO-WWNMGR-MIB", "wwnmTypeOtherAvailableWwns"),
        ("CISCO-WWNMGR-MIB", "wwnmType1ReservedWwns"),
        ("CISCO-WWNMGR-MIB", "wwnmTypeOtherReservedWwns"))
)
if mibBuilder.loadTexts:
    cwmWwnmConfigurationGroup.setStatus("current")

cwmWwnmVsanWwnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2, 9)
)
cwmWwnmVsanWwnGroup.setObjects(
      *(("CISCO-WWNMGR-MIB", "wwnmVsanWwn"),
        ("CISCO-WWNMGR-MIB", "wwnmVsanWwnStorageType"),
        ("CISCO-WWNMGR-MIB", "wwnmVsanWwnRowStatus"))
)
if mibBuilder.loadTexts:
    cwmWwnmVsanWwnGroup.setStatus("current")


# Notification objects

wwnmType1WwnShortageNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 1)
)
wwnmType1WwnShortageNotify.setObjects(
    ("CISCO-WWNMGR-MIB", "wwnmType1AvailableWwns")
)
if mibBuilder.loadTexts:
    wwnmType1WwnShortageNotify.setStatus(
        "current"
    )

wwnmType1WwnAvailableNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 2)
)
wwnmType1WwnAvailableNotify.setObjects(
    ("CISCO-WWNMGR-MIB", "wwnmType1AvailableWwns")
)
if mibBuilder.loadTexts:
    wwnmType1WwnAvailableNotify.setStatus(
        "current"
    )

wwnmTypeOtherWwnShortageNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 3)
)
wwnmTypeOtherWwnShortageNotify.setObjects(
    ("CISCO-WWNMGR-MIB", "wwnmTypeOtherAvailableWwns")
)
if mibBuilder.loadTexts:
    wwnmTypeOtherWwnShortageNotify.setStatus(
        "current"
    )

wwnmTypeOtherWwnAvailableNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 4)
)
wwnmTypeOtherWwnAvailableNotify.setObjects(
    ("CISCO-WWNMGR-MIB", "wwnmTypeOtherAvailableWwns")
)
if mibBuilder.loadTexts:
    wwnmTypeOtherWwnAvailableNotify.setStatus(
        "current"
    )


# Notifications groups

cwmWwnmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2, 8)
)
cwmWwnmNotificationGroup.setObjects(
      *(("CISCO-WWNMGR-MIB", "wwnmType1WwnShortageNotify"),
        ("CISCO-WWNMGR-MIB", "wwnmType1WwnAvailableNotify"),
        ("CISCO-WWNMGR-MIB", "wwnmTypeOtherWwnShortageNotify"),
        ("CISCO-WWNMGR-MIB", "wwnmTypeOtherWwnAvailableNotify"))
)
if mibBuilder.loadTexts:
    cwmWwnmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWwnmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWwnmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWwnmMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWwnmMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WWNMGR-MIB",
    **{"ciscoWwnmgrMIB": ciscoWwnmgrMIB,
       "ciscoWwnmMIBObjects": ciscoWwnmMIBObjects,
       "wwnmConfigurationGroup": wwnmConfigurationGroup,
       "wwnmSecondaryBaseMacAddress": wwnmSecondaryBaseMacAddress,
       "wwnmSecondaryMacAddressRange": wwnmSecondaryMacAddressRange,
       "wwnmType1MaxWwns": wwnmType1MaxWwns,
       "wwnmType1AvailableWwns": wwnmType1AvailableWwns,
       "wwnmTypeOtherMaxWwns": wwnmTypeOtherMaxWwns,
       "wwnmTypeOtherAvailableWwns": wwnmTypeOtherAvailableWwns,
       "wwnmType1ReservedWwns": wwnmType1ReservedWwns,
       "wwnmTypeOtherReservedWwns": wwnmTypeOtherReservedWwns,
       "wwnmVsanWwnTable": wwnmVsanWwnTable,
       "wwnmVsanWwnEntry": wwnmVsanWwnEntry,
       "wwnmVsanWwn": wwnmVsanWwn,
       "wwnmVsanWwnStorageType": wwnmVsanWwnStorageType,
       "wwnmVsanWwnRowStatus": wwnmVsanWwnRowStatus,
       "wwnmNotificationGroup": wwnmNotificationGroup,
       "wwnmNotification": wwnmNotification,
       "wwnmNotificationPrefix": wwnmNotificationPrefix,
       "wwnmType1WwnShortageNotify": wwnmType1WwnShortageNotify,
       "wwnmType1WwnAvailableNotify": wwnmType1WwnAvailableNotify,
       "wwnmTypeOtherWwnShortageNotify": wwnmTypeOtherWwnShortageNotify,
       "wwnmTypeOtherWwnAvailableNotify": wwnmTypeOtherWwnAvailableNotify,
       "ciscoWwnmMIBConformance": ciscoWwnmMIBConformance,
       "ciscoWwnmMIBCompliances": ciscoWwnmMIBCompliances,
       "ciscoWwnmMIBCompliance": ciscoWwnmMIBCompliance,
       "ciscoWwnmMIBCompliance1": ciscoWwnmMIBCompliance1,
       "ciscoWwnmMIBGroups": ciscoWwnmMIBGroups,
       "cwmWwnmConfigurationGroup": cwmWwnmConfigurationGroup,
       "cwmWwnmNotificationGroup": cwmWwnmNotificationGroup,
       "cwmWwnmVsanWwnGroup": cwmWwnmVsanWwnGroup}
)
