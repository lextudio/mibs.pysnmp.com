# SNMP MIB module (HP-ICF-CONNECTION-RATE-FILTER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-CONNECTION-RATE-FILTER
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:12 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfConnectionRateFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24)
)
hpicfConnectionRateFilter.setRevisions(
        ("2009-05-12 01:08",
         "2004-09-07 01:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfConnectionRateFilterNotifications_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterNotifications = _HpicfConnectionRateFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 0)
)
_HpicfConnectionRateFilterNotificationControl_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterNotificationControl = _HpicfConnectionRateFilterNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 1)
)
_HpicfConnectionRateFilterNotificationControlEnable_Type = TruthValue
_HpicfConnectionRateFilterNotificationControlEnable_Object = MibScalar
hpicfConnectionRateFilterNotificationControlEnable = _HpicfConnectionRateFilterNotificationControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 1, 1),
    _HpicfConnectionRateFilterNotificationControlEnable_Type()
)
hpicfConnectionRateFilterNotificationControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterNotificationControlEnable.setStatus("current")


class _HpicfConnectionRateFilterSensitivity_Type(Integer32):
    """Custom type hpicfConnectionRateFilterSensitivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 4),
          ("high", 3),
          ("low", 1),
          ("medium", 2),
          ("none", 0))
    )


_HpicfConnectionRateFilterSensitivity_Type.__name__ = "Integer32"
_HpicfConnectionRateFilterSensitivity_Object = MibScalar
hpicfConnectionRateFilterSensitivity = _HpicfConnectionRateFilterSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 1, 2),
    _HpicfConnectionRateFilterSensitivity_Type()
)
hpicfConnectionRateFilterSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterSensitivity.setStatus("current")
_HpicfConnectionRateFilterObjects_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterObjects = _HpicfConnectionRateFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2)
)


class _HpicifConnectionRateFilterVlanId_Type(Integer32):
    """Custom type hpicifConnectionRateFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpicifConnectionRateFilterVlanId_Type.__name__ = "Integer32"
_HpicifConnectionRateFilterVlanId_Object = MibScalar
hpicifConnectionRateFilterVlanId = _HpicifConnectionRateFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 1),
    _HpicifConnectionRateFilterVlanId_Type()
)
hpicifConnectionRateFilterVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicifConnectionRateFilterVlanId.setStatus("current")
_HpicifConnectionRateFilterInetAddress_Type = InetAddress
_HpicifConnectionRateFilterInetAddress_Object = MibScalar
hpicifConnectionRateFilterInetAddress = _HpicifConnectionRateFilterInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 2),
    _HpicifConnectionRateFilterInetAddress_Type()
)
hpicifConnectionRateFilterInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicifConnectionRateFilterInetAddress.setStatus("current")
_HpicifConnectionRateFilterInetAddressType_Type = InetAddressType
_HpicifConnectionRateFilterInetAddressType_Object = MibScalar
hpicifConnectionRateFilterInetAddressType = _HpicifConnectionRateFilterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 3),
    _HpicifConnectionRateFilterInetAddressType_Type()
)
hpicifConnectionRateFilterInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicifConnectionRateFilterInetAddressType.setStatus("current")


class _HpicifConnectionRateFilterMode_Type(Integer32):
    """Custom type hpicifConnectionRateFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("inform", 0),
          ("throttle", 1))
    )


_HpicifConnectionRateFilterMode_Type.__name__ = "Integer32"
_HpicifConnectionRateFilterMode_Object = MibScalar
hpicifConnectionRateFilterMode = _HpicifConnectionRateFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 4),
    _HpicifConnectionRateFilterMode_Type()
)
hpicifConnectionRateFilterMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicifConnectionRateFilterMode.setStatus("current")
_HpicfConnectionRateFilterConformance_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterConformance = _HpicfConnectionRateFilterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3)
)
_HpicfConnectionRateFilterCompliances_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterCompliances = _HpicfConnectionRateFilterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 1)
)
_HpicfConnectionRateFilterGroups_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterGroups = _HpicfConnectionRateFilterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2)
)
_HpicfConnectionRateFilterIfModeConfig_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilterIfModeConfig = _HpicfConnectionRateFilterIfModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4)
)
_HpicfConnectionRateFilterIfModeConfigTable_Object = MibTable
hpicfConnectionRateFilterIfModeConfigTable = _HpicfConnectionRateFilterIfModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterIfModeConfigTable.setStatus("current")
_HpicfConnectionRateFilterIfModeConfigEntry_Object = MibTableRow
hpicfConnectionRateFilterIfModeConfigEntry = _HpicfConnectionRateFilterIfModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4, 1, 1)
)
hpicfConnectionRateFilterIfModeConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterIfModeConfigEntry.setStatus("current")


class _HpicfConnectionRateFilterIfModeValue_Type(Integer32):
    """Custom type hpicfConnectionRateFilterIfModeValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 3),
          ("inform", 1),
          ("none", 0),
          ("throttle", 2))
    )


_HpicfConnectionRateFilterIfModeValue_Type.__name__ = "Integer32"
_HpicfConnectionRateFilterIfModeValue_Object = MibTableColumn
hpicfConnectionRateFilterIfModeValue = _HpicfConnectionRateFilterIfModeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4, 1, 1, 1),
    _HpicfConnectionRateFilterIfModeValue_Type()
)
hpicfConnectionRateFilterIfModeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterIfModeValue.setStatus("current")

# Managed Objects groups

hpicfConnectionRateFilterObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2, 2)
)
hpicfConnectionRateFilterObjectGroup.setObjects(
      *(("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterNotificationControlEnable"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterIfModeValue"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterSensitivity"))
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterObjectGroup.setStatus("current")

hpicfConnectionRateFilterObjectGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2, 3)
)
hpicfConnectionRateFilterObjectGroup1.setObjects(
      *(("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterVlanId"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddress"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddressType"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterMode"))
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterObjectGroup1.setStatus("current")


# Notification objects

hpicfConnectionRateFilterNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 0, 1)
)
hpicfConnectionRateFilterNotification.setObjects(
      *(("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterVlanId"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddress"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddressType"),
        ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterMode"))
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterNotification.setStatus(
        "current"
    )


# Notifications groups

hpicfConnectionRateFilterNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2, 1)
)
hpicfConnectionRateFilterNotifyGroup.setObjects(
    ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterNotification")
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfConnectionRateFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterCompliance.setStatus(
        "current"
    )

hpicfConnectionRateFilterCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfConnectionRateFilterCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-CONNECTION-RATE-FILTER",
    **{"hpicfConnectionRateFilter": hpicfConnectionRateFilter,
       "hpicfConnectionRateFilterNotifications": hpicfConnectionRateFilterNotifications,
       "hpicfConnectionRateFilterNotification": hpicfConnectionRateFilterNotification,
       "hpicfConnectionRateFilterNotificationControl": hpicfConnectionRateFilterNotificationControl,
       "hpicfConnectionRateFilterNotificationControlEnable": hpicfConnectionRateFilterNotificationControlEnable,
       "hpicfConnectionRateFilterSensitivity": hpicfConnectionRateFilterSensitivity,
       "hpicfConnectionRateFilterObjects": hpicfConnectionRateFilterObjects,
       "hpicifConnectionRateFilterVlanId": hpicifConnectionRateFilterVlanId,
       "hpicifConnectionRateFilterInetAddress": hpicifConnectionRateFilterInetAddress,
       "hpicifConnectionRateFilterInetAddressType": hpicifConnectionRateFilterInetAddressType,
       "hpicifConnectionRateFilterMode": hpicifConnectionRateFilterMode,
       "hpicfConnectionRateFilterConformance": hpicfConnectionRateFilterConformance,
       "hpicfConnectionRateFilterCompliances": hpicfConnectionRateFilterCompliances,
       "hpicfConnectionRateFilterCompliance": hpicfConnectionRateFilterCompliance,
       "hpicfConnectionRateFilterCompliance1": hpicfConnectionRateFilterCompliance1,
       "hpicfConnectionRateFilterGroups": hpicfConnectionRateFilterGroups,
       "hpicfConnectionRateFilterNotifyGroup": hpicfConnectionRateFilterNotifyGroup,
       "hpicfConnectionRateFilterObjectGroup": hpicfConnectionRateFilterObjectGroup,
       "hpicfConnectionRateFilterObjectGroup1": hpicfConnectionRateFilterObjectGroup1,
       "hpicfConnectionRateFilterIfModeConfig": hpicfConnectionRateFilterIfModeConfig,
       "hpicfConnectionRateFilterIfModeConfigTable": hpicfConnectionRateFilterIfModeConfigTable,
       "hpicfConnectionRateFilterIfModeConfigEntry": hpicfConnectionRateFilterIfModeConfigEntry,
       "hpicfConnectionRateFilterIfModeValue": hpicfConnectionRateFilterIfModeValue}
)
