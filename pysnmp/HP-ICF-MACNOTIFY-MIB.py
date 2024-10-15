# SNMP MIB module (HP-ICF-MACNOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-MACNOTIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:46 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpicfMacNotifyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66)
)
hpicfMacNotifyMIB.setRevisions(
        ("2013-07-18 00:00",
         "2011-07-21 00:00",
         "2010-02-08 00:00",
         "2009-12-11 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfMacNotifyNotificationObjects_ObjectIdentity = ObjectIdentity
hpicfMacNotifyNotificationObjects = _HpicfMacNotifyNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0)
)
_HpicfMacNotifyConfigObjects_ObjectIdentity = ObjectIdentity
hpicfMacNotifyConfigObjects = _HpicfMacNotifyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1)
)


class _HpicfMacNotifyEnable_Type(Integer32):
    """Custom type hpicfMacNotifyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfMacNotifyEnable_Type.__name__ = "Integer32"
_HpicfMacNotifyEnable_Object = MibScalar
hpicfMacNotifyEnable = _HpicfMacNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 1),
    _HpicfMacNotifyEnable_Type()
)
hpicfMacNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyEnable.setStatus("current")


class _HpicfMacNotifyTrapInterval_Type(Unsigned32):
    """Custom type hpicfMacNotifyTrapInterval based on Unsigned32"""
    defaultValue = 30


_HpicfMacNotifyTrapInterval_Object = MibScalar
hpicfMacNotifyTrapInterval = _HpicfMacNotifyTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 2),
    _HpicfMacNotifyTrapInterval_Type()
)
hpicfMacNotifyTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfMacNotifyTrapInterval.setUnits("Seconds")


class _HpicfMacNotifyMoveEnable_Type(Integer32):
    """Custom type hpicfMacNotifyMoveEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfMacNotifyMoveEnable_Type.__name__ = "Integer32"
_HpicfMacNotifyMoveEnable_Object = MibScalar
hpicfMacNotifyMoveEnable = _HpicfMacNotifyMoveEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 3),
    _HpicfMacNotifyMoveEnable_Type()
)
hpicfMacNotifyMoveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyMoveEnable.setStatus("current")
_HpicfMacNotifyLearnedPortConfig_Type = PortList
_HpicfMacNotifyLearnedPortConfig_Object = MibScalar
hpicfMacNotifyLearnedPortConfig = _HpicfMacNotifyLearnedPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 4),
    _HpicfMacNotifyLearnedPortConfig_Type()
)
hpicfMacNotifyLearnedPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyLearnedPortConfig.setStatus("current")
_HpicfMacNotifyRemovedPortConfig_Type = PortList
_HpicfMacNotifyRemovedPortConfig_Object = MibScalar
hpicfMacNotifyRemovedPortConfig = _HpicfMacNotifyRemovedPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 5),
    _HpicfMacNotifyRemovedPortConfig_Type()
)
hpicfMacNotifyRemovedPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyRemovedPortConfig.setStatus("current")


class _HpicfMacNotifyAction_Type(Integer32):
    """Custom type hpicfMacNotifyAction based on Integer32"""
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
        *(("aged", 4),
          ("learned", 1),
          ("moved", 2),
          ("removed", 3))
    )


_HpicfMacNotifyAction_Type.__name__ = "Integer32"
_HpicfMacNotifyAction_Object = MibScalar
hpicfMacNotifyAction = _HpicfMacNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 6),
    _HpicfMacNotifyAction_Type()
)
hpicfMacNotifyAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMacNotifyAction.setStatus("current")
_HpicfMacNotifyMacAddress_Type = MacAddress
_HpicfMacNotifyMacAddress_Object = MibScalar
hpicfMacNotifyMacAddress = _HpicfMacNotifyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 7),
    _HpicfMacNotifyMacAddress_Type()
)
hpicfMacNotifyMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMacNotifyMacAddress.setStatus("current")
_HpicfMacNotifyFromPortId_Type = Integer32
_HpicfMacNotifyFromPortId_Object = MibScalar
hpicfMacNotifyFromPortId = _HpicfMacNotifyFromPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 8),
    _HpicfMacNotifyFromPortId_Type()
)
hpicfMacNotifyFromPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMacNotifyFromPortId.setStatus("current")
_HpicfMacNotifyToPortId_Type = Integer32
_HpicfMacNotifyToPortId_Object = MibScalar
hpicfMacNotifyToPortId = _HpicfMacNotifyToPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 9),
    _HpicfMacNotifyToPortId_Type()
)
hpicfMacNotifyToPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMacNotifyToPortId.setStatus("current")
_HpicfMacNotifyVlanId_Type = Integer32
_HpicfMacNotifyVlanId_Object = MibScalar
hpicfMacNotifyVlanId = _HpicfMacNotifyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 10),
    _HpicfMacNotifyVlanId_Type()
)
hpicfMacNotifyVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMacNotifyVlanId.setStatus("current")
_HpicfMacNotifyAgedPortConfig_Type = PortList
_HpicfMacNotifyAgedPortConfig_Object = MibScalar
hpicfMacNotifyAgedPortConfig = _HpicfMacNotifyAgedPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 11),
    _HpicfMacNotifyAgedPortConfig_Type()
)
hpicfMacNotifyAgedPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyAgedPortConfig.setStatus("current")
_HpicfMacNotifyStats_ObjectIdentity = ObjectIdentity
hpicfMacNotifyStats = _HpicfMacNotifyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2)
)
_HpicfMacNotifyLearnedCount_Type = Counter32
_HpicfMacNotifyLearnedCount_Object = MibScalar
hpicfMacNotifyLearnedCount = _HpicfMacNotifyLearnedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 1),
    _HpicfMacNotifyLearnedCount_Type()
)
hpicfMacNotifyLearnedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMacNotifyLearnedCount.setStatus("current")
_HpicfMacNotifyRemovedCount_Type = Counter32
_HpicfMacNotifyRemovedCount_Object = MibScalar
hpicfMacNotifyRemovedCount = _HpicfMacNotifyRemovedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 2),
    _HpicfMacNotifyRemovedCount_Type()
)
hpicfMacNotifyRemovedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMacNotifyRemovedCount.setStatus("current")
_HpicfMacNotifyMoveCount_Type = Counter32
_HpicfMacNotifyMoveCount_Object = MibScalar
hpicfMacNotifyMoveCount = _HpicfMacNotifyMoveCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 3),
    _HpicfMacNotifyMoveCount_Type()
)
hpicfMacNotifyMoveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMacNotifyMoveCount.setStatus("current")
_HpicfMacNotifyCount_Type = Counter32
_HpicfMacNotifyCount_Object = MibScalar
hpicfMacNotifyCount = _HpicfMacNotifyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 4),
    _HpicfMacNotifyCount_Type()
)
hpicfMacNotifyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMacNotifyCount.setStatus("current")
_HpicfMacNotifyAgedCount_Type = Counter32
_HpicfMacNotifyAgedCount_Object = MibScalar
hpicfMacNotifyAgedCount = _HpicfMacNotifyAgedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 5),
    _HpicfMacNotifyAgedCount_Type()
)
hpicfMacNotifyAgedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMacNotifyAgedCount.setStatus("current")
_HpicfMacNotifyConformance_ObjectIdentity = ObjectIdentity
hpicfMacNotifyConformance = _HpicfMacNotifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3)
)
_HpicfMacNotifyCompliances_ObjectIdentity = ObjectIdentity
hpicfMacNotifyCompliances = _HpicfMacNotifyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1)
)
_HpicfMacNotifyGroups_ObjectIdentity = ObjectIdentity
hpicfMacNotifyGroups = _HpicfMacNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2)
)
_HpicfMacNotifyClearObjects_ObjectIdentity = ObjectIdentity
hpicfMacNotifyClearObjects = _HpicfMacNotifyClearObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4)
)
_HpicfMacNotifyClearMacTableOnPorts_Type = PortList
_HpicfMacNotifyClearMacTableOnPorts_Object = MibScalar
hpicfMacNotifyClearMacTableOnPorts = _HpicfMacNotifyClearMacTableOnPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4, 1),
    _HpicfMacNotifyClearMacTableOnPorts_Type()
)
hpicfMacNotifyClearMacTableOnPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyClearMacTableOnPorts.setStatus("current")
_HpicfMacNotifyClearMacTableOnVlan_Type = VlanId
_HpicfMacNotifyClearMacTableOnVlan_Object = MibScalar
hpicfMacNotifyClearMacTableOnVlan = _HpicfMacNotifyClearMacTableOnVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4, 2),
    _HpicfMacNotifyClearMacTableOnVlan_Type()
)
hpicfMacNotifyClearMacTableOnVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyClearMacTableOnVlan.setStatus("current")
_HpicfMacCountNotifyConfigObjects_ObjectIdentity = ObjectIdentity
hpicfMacCountNotifyConfigObjects = _HpicfMacCountNotifyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5)
)


class _HpicfMacNotifyPortLearnedCountEnable_Type(Integer32):
    """Custom type hpicfMacNotifyPortLearnedCountEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfMacNotifyPortLearnedCountEnable_Type.__name__ = "Integer32"
_HpicfMacNotifyPortLearnedCountEnable_Object = MibScalar
hpicfMacNotifyPortLearnedCountEnable = _HpicfMacNotifyPortLearnedCountEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 1),
    _HpicfMacNotifyPortLearnedCountEnable_Type()
)
hpicfMacNotifyPortLearnedCountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyPortLearnedCountEnable.setStatus("current")
_HpicfMacNotifyPortLearnedCountConfig_Type = PortList
_HpicfMacNotifyPortLearnedCountConfig_Object = MibScalar
hpicfMacNotifyPortLearnedCountConfig = _HpicfMacNotifyPortLearnedCountConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 2),
    _HpicfMacNotifyPortLearnedCountConfig_Type()
)
hpicfMacNotifyPortLearnedCountConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyPortLearnedCountConfig.setStatus("current")
_HpicfMacNotifyPortLearnedCountConfigTable_Object = MibTable
hpicfMacNotifyPortLearnedCountConfigTable = _HpicfMacNotifyPortLearnedCountConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3)
)
if mibBuilder.loadTexts:
    hpicfMacNotifyPortLearnedCountConfigTable.setStatus("current")
_HpicfMacNotifyPortLearnedCountConfigEntry_Object = MibTableRow
hpicfMacNotifyPortLearnedCountConfigEntry = _HpicfMacNotifyPortLearnedCountConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1)
)
hpicfMacNotifyPortLearnedCountConfigEntry.setIndexNames(
    (0, "HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfMacNotifyPortLearnedCountConfigEntry.setStatus("current")
_HpicfMacNotifyPortIndex_Type = InterfaceIndex
_HpicfMacNotifyPortIndex_Object = MibTableColumn
hpicfMacNotifyPortIndex = _HpicfMacNotifyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1, 1),
    _HpicfMacNotifyPortIndex_Type()
)
hpicfMacNotifyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMacNotifyPortIndex.setStatus("current")


class _HpicfMacNotifyPortLearnedCount_Type(Unsigned32):
    """Custom type hpicfMacNotifyPortLearnedCount based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HpicfMacNotifyPortLearnedCount_Type.__name__ = "Unsigned32"
_HpicfMacNotifyPortLearnedCount_Object = MibTableColumn
hpicfMacNotifyPortLearnedCount = _HpicfMacNotifyPortLearnedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1, 2),
    _HpicfMacNotifyPortLearnedCount_Type()
)
hpicfMacNotifyPortLearnedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacNotifyPortLearnedCount.setStatus("current")

# Managed Objects groups

hpicfMacNotifyGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 1)
)
hpicfMacNotifyGlobalConfigGroup.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyGlobalConfigGroup.setStatus("current")

hpicfMacNotifyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 2)
)
hpicfMacNotifyConfigGroup.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedPortConfig"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedPortConfig"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyConfigGroup.setStatus("deprecated")

hpicfMacNotifyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 3)
)
hpicfMacNotifyStatsGroup.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyCount"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyStatsGroup.setStatus("deprecated")

hpicfMacNotifyClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 5)
)
hpicfMacNotifyClearGroup.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearMacTableOnPorts"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearMacTableOnVlan"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyClearGroup.setStatus("current")

hpicfMacCountNotifyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 6)
)
hpicfMacCountNotifyConfigGroup.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCountEnable"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCountConfig"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCount"))
)
if mibBuilder.loadTexts:
    hpicfMacCountNotifyConfigGroup.setStatus("current")

hpicfMacNotifyStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 8)
)
hpicfMacNotifyStatsGroup2.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAgedCount"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyStatsGroup2.setStatus("current")

hpicfMacNotifyConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 9)
)
hpicfMacNotifyConfigGroup2.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedPortConfig"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedPortConfig"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAgedPortConfig"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyConfigGroup2.setStatus("current")


# Notification objects

hpicfMacNotifyMacAddressTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0, 1)
)
hpicfMacNotifyMacAddressTableChange.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyMacAddressTableChange.setStatus(
        "current"
    )

hpicfMacNotifyPortMacAddressCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0, 2)
)
hpicfMacNotifyPortMacAddressCount.setObjects(
      *(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCount"),
        ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"))
)
if mibBuilder.loadTexts:
    hpicfMacNotifyPortMacAddressCount.setStatus(
        "current"
    )


# Notifications groups

hpicfMacNotifyNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 4)
)
hpicfMacNotifyNotifications.setObjects(
    ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddressTableChange")
)
if mibBuilder.loadTexts:
    hpicfMacNotifyNotifications.setStatus(
        "current"
    )

hpicfMacCountNotifyNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 7)
)
hpicfMacCountNotifyNotifications.setObjects(
    ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortMacAddressCount")
)
if mibBuilder.loadTexts:
    hpicfMacCountNotifyNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfMacNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfMacNotifyCompliance.setStatus(
        "deprecated"
    )

hpicfMacCountNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfMacCountNotifyCompliance.setStatus(
        "current"
    )

hpicfMacNotifyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfMacNotifyCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-MACNOTIFY-MIB",
    **{"hpicfMacNotifyMIB": hpicfMacNotifyMIB,
       "hpicfMacNotifyNotificationObjects": hpicfMacNotifyNotificationObjects,
       "hpicfMacNotifyMacAddressTableChange": hpicfMacNotifyMacAddressTableChange,
       "hpicfMacNotifyPortMacAddressCount": hpicfMacNotifyPortMacAddressCount,
       "hpicfMacNotifyConfigObjects": hpicfMacNotifyConfigObjects,
       "hpicfMacNotifyEnable": hpicfMacNotifyEnable,
       "hpicfMacNotifyTrapInterval": hpicfMacNotifyTrapInterval,
       "hpicfMacNotifyMoveEnable": hpicfMacNotifyMoveEnable,
       "hpicfMacNotifyLearnedPortConfig": hpicfMacNotifyLearnedPortConfig,
       "hpicfMacNotifyRemovedPortConfig": hpicfMacNotifyRemovedPortConfig,
       "hpicfMacNotifyAction": hpicfMacNotifyAction,
       "hpicfMacNotifyMacAddress": hpicfMacNotifyMacAddress,
       "hpicfMacNotifyFromPortId": hpicfMacNotifyFromPortId,
       "hpicfMacNotifyToPortId": hpicfMacNotifyToPortId,
       "hpicfMacNotifyVlanId": hpicfMacNotifyVlanId,
       "hpicfMacNotifyAgedPortConfig": hpicfMacNotifyAgedPortConfig,
       "hpicfMacNotifyStats": hpicfMacNotifyStats,
       "hpicfMacNotifyLearnedCount": hpicfMacNotifyLearnedCount,
       "hpicfMacNotifyRemovedCount": hpicfMacNotifyRemovedCount,
       "hpicfMacNotifyMoveCount": hpicfMacNotifyMoveCount,
       "hpicfMacNotifyCount": hpicfMacNotifyCount,
       "hpicfMacNotifyAgedCount": hpicfMacNotifyAgedCount,
       "hpicfMacNotifyConformance": hpicfMacNotifyConformance,
       "hpicfMacNotifyCompliances": hpicfMacNotifyCompliances,
       "hpicfMacNotifyCompliance": hpicfMacNotifyCompliance,
       "hpicfMacCountNotifyCompliance": hpicfMacCountNotifyCompliance,
       "hpicfMacNotifyCompliance2": hpicfMacNotifyCompliance2,
       "hpicfMacNotifyGroups": hpicfMacNotifyGroups,
       "hpicfMacNotifyGlobalConfigGroup": hpicfMacNotifyGlobalConfigGroup,
       "hpicfMacNotifyConfigGroup": hpicfMacNotifyConfigGroup,
       "hpicfMacNotifyStatsGroup": hpicfMacNotifyStatsGroup,
       "hpicfMacNotifyNotifications": hpicfMacNotifyNotifications,
       "hpicfMacNotifyClearGroup": hpicfMacNotifyClearGroup,
       "hpicfMacCountNotifyConfigGroup": hpicfMacCountNotifyConfigGroup,
       "hpicfMacCountNotifyNotifications": hpicfMacCountNotifyNotifications,
       "hpicfMacNotifyStatsGroup2": hpicfMacNotifyStatsGroup2,
       "hpicfMacNotifyConfigGroup2": hpicfMacNotifyConfigGroup2,
       "hpicfMacNotifyClearObjects": hpicfMacNotifyClearObjects,
       "hpicfMacNotifyClearMacTableOnPorts": hpicfMacNotifyClearMacTableOnPorts,
       "hpicfMacNotifyClearMacTableOnVlan": hpicfMacNotifyClearMacTableOnVlan,
       "hpicfMacCountNotifyConfigObjects": hpicfMacCountNotifyConfigObjects,
       "hpicfMacNotifyPortLearnedCountEnable": hpicfMacNotifyPortLearnedCountEnable,
       "hpicfMacNotifyPortLearnedCountConfig": hpicfMacNotifyPortLearnedCountConfig,
       "hpicfMacNotifyPortLearnedCountConfigTable": hpicfMacNotifyPortLearnedCountConfigTable,
       "hpicfMacNotifyPortLearnedCountConfigEntry": hpicfMacNotifyPortLearnedCountConfigEntry,
       "hpicfMacNotifyPortIndex": hpicfMacNotifyPortIndex,
       "hpicfMacNotifyPortLearnedCount": hpicfMacNotifyPortLearnedCount}
)
