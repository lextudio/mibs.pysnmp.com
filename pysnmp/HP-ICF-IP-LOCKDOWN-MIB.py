# SNMP MIB module (HP-ICF-IP-LOCKDOWN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-IP-LOCKDOWN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:33 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfIpLockdown = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39)
)
hpicfIpLockdown.setRevisions(
        ("2008-03-16 05:24",
         "2006-06-08 23:47")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfIpLockTraps_ObjectIdentity = ObjectIdentity
hpicfIpLockTraps = _HpicfIpLockTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0)
)
_HpicfIpLockTrapsObjects_ObjectIdentity = ObjectIdentity
hpicfIpLockTrapsObjects = _HpicfIpLockTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1)
)


class _HpicfIpLockOutOfResourceSource_Type(Integer32):
    """Custom type hpicfIpLockOutOfResourceSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpsnooping", 1),
          ("iplockdown", 2))
    )


_HpicfIpLockOutOfResourceSource_Type.__name__ = "Integer32"
_HpicfIpLockOutOfResourceSource_Object = MibScalar
hpicfIpLockOutOfResourceSource = _HpicfIpLockOutOfResourceSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 1),
    _HpicfIpLockOutOfResourceSource_Type()
)
hpicfIpLockOutOfResourceSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockOutOfResourceSource.setStatus("current")
_HpicfIpLockErrantNotifyObjects_ObjectIdentity = ObjectIdentity
hpicfIpLockErrantNotifyObjects = _HpicfIpLockErrantNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4)
)
_HpicfIpLockNotifyCount_Type = Counter32
_HpicfIpLockNotifyCount_Object = MibScalar
hpicfIpLockNotifyCount = _HpicfIpLockNotifyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 1),
    _HpicfIpLockNotifyCount_Type()
)
hpicfIpLockNotifyCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifyCount.setStatus("current")
_HpicfIpLockNotifyPort_Type = InterfaceIndex
_HpicfIpLockNotifyPort_Object = MibScalar
hpicfIpLockNotifyPort = _HpicfIpLockNotifyPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 2),
    _HpicfIpLockNotifyPort_Type()
)
hpicfIpLockNotifyPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifyPort.setStatus("current")
_HpicfIpLockNotifySrcIpType_Type = InetAddressType
_HpicfIpLockNotifySrcIpType_Object = MibScalar
hpicfIpLockNotifySrcIpType = _HpicfIpLockNotifySrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 3),
    _HpicfIpLockNotifySrcIpType_Type()
)
hpicfIpLockNotifySrcIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifySrcIpType.setStatus("current")
_HpicfIpLockNotifySrcIpAddress_Type = InetAddress
_HpicfIpLockNotifySrcIpAddress_Object = MibScalar
hpicfIpLockNotifySrcIpAddress = _HpicfIpLockNotifySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 4),
    _HpicfIpLockNotifySrcIpAddress_Type()
)
hpicfIpLockNotifySrcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifySrcIpAddress.setStatus("current")
_HpicfIpLockNotifyDstIpType_Type = InetAddressType
_HpicfIpLockNotifyDstIpType_Object = MibScalar
hpicfIpLockNotifyDstIpType = _HpicfIpLockNotifyDstIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 5),
    _HpicfIpLockNotifyDstIpType_Type()
)
hpicfIpLockNotifyDstIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifyDstIpType.setStatus("current")
_HpicfIpLockNotifyDstIpAddress_Type = InetAddress
_HpicfIpLockNotifyDstIpAddress_Object = MibScalar
hpicfIpLockNotifyDstIpAddress = _HpicfIpLockNotifyDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 6),
    _HpicfIpLockNotifyDstIpAddress_Type()
)
hpicfIpLockNotifyDstIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifyDstIpAddress.setStatus("current")
_HpicfIpLockNotifyMacAddress_Type = MacAddress
_HpicfIpLockNotifyMacAddress_Object = MibScalar
hpicfIpLockNotifyMacAddress = _HpicfIpLockNotifyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 7),
    _HpicfIpLockNotifyMacAddress_Type()
)
hpicfIpLockNotifyMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifyMacAddress.setStatus("current")
_HpicfIpLockNotifyPktCount_Type = Counter32
_HpicfIpLockNotifyPktCount_Object = MibScalar
hpicfIpLockNotifyPktCount = _HpicfIpLockNotifyPktCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 4, 8),
    _HpicfIpLockNotifyPktCount_Type()
)
hpicfIpLockNotifyPktCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfIpLockNotifyPktCount.setStatus("current")
_HpicfIpLockObjects_ObjectIdentity = ObjectIdentity
hpicfIpLockObjects = _HpicfIpLockObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1)
)
_HpicfIpLockConfig_ObjectIdentity = ObjectIdentity
hpicfIpLockConfig = _HpicfIpLockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1)
)
_HpicfIpLockEnable_Type = TruthValue
_HpicfIpLockEnable_Object = MibScalar
hpicfIpLockEnable = _HpicfIpLockEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1, 1),
    _HpicfIpLockEnable_Type()
)
hpicfIpLockEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpLockEnable.setStatus("current")
_HpicfIpLockPortTable_Object = MibTable
hpicfIpLockPortTable = _HpicfIpLockPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfIpLockPortTable.setStatus("current")
_HpicfIpLockPortEntry_Object = MibTableRow
hpicfIpLockPortEntry = _HpicfIpLockPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1, 2, 1)
)
hpicfIpLockPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfIpLockPortEntry.setStatus("current")
_HpicfIpLockPortEnable_Type = TruthValue
_HpicfIpLockPortEnable_Object = MibTableColumn
hpicfIpLockPortEnable = _HpicfIpLockPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1, 2, 1, 1),
    _HpicfIpLockPortEnable_Type()
)
hpicfIpLockPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpLockPortEnable.setStatus("current")


class _HpicfIpLockTrapCntl_Type(Bits):
    """Custom type hpicfIpLockTrapCntl based on Bits"""
    namedValues = NamedValues(
        ("outOfResource", 0)
    )

_HpicfIpLockTrapCntl_Type.__name__ = "Bits"
_HpicfIpLockTrapCntl_Object = MibScalar
hpicfIpLockTrapCntl = _HpicfIpLockTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1, 3),
    _HpicfIpLockTrapCntl_Type()
)
hpicfIpLockTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpLockTrapCntl.setStatus("obsolete")


class _HpicfIpLockTrapCtrl_Type(TruthValue):
    """Custom type hpicfIpLockTrapCtrl based on TruthValue"""


_HpicfIpLockTrapCtrl_Object = MibScalar
hpicfIpLockTrapCtrl = _HpicfIpLockTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 1, 4),
    _HpicfIpLockTrapCtrl_Type()
)
hpicfIpLockTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpLockTrapCtrl.setStatus("current")
_HpicfIpLockStatus_ObjectIdentity = ObjectIdentity
hpicfIpLockStatus = _HpicfIpLockStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2)
)
_HpicfIpLockPortStatusTable_Object = MibTable
hpicfIpLockPortStatusTable = _HpicfIpLockPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfIpLockPortStatusTable.setStatus("current")
_HpicfIpLockPortStatusEntry_Object = MibTableRow
hpicfIpLockPortStatusEntry = _HpicfIpLockPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 1, 1)
)
hpicfIpLockPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfIpLockPortStatusEntry.setStatus("current")


class _HpicfIpLockPortOperStatus_Type(Bits):
    """Custom type hpicfIpLockPortOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("active", 0),
          ("noDsnoop", 1),
          ("noSnoopingVlan", 3),
          ("trustedPort", 2))
    )

_HpicfIpLockPortOperStatus_Type.__name__ = "Bits"
_HpicfIpLockPortOperStatus_Object = MibTableColumn
hpicfIpLockPortOperStatus = _HpicfIpLockPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 1, 1, 1),
    _HpicfIpLockPortOperStatus_Type()
)
hpicfIpLockPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockPortOperStatus.setStatus("current")
_HpicfIpLockAddrTable_Object = MibTable
hpicfIpLockAddrTable = _HpicfIpLockAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfIpLockAddrTable.setStatus("current")
_HpicfIpLockAddrEntry_Object = MibTableRow
hpicfIpLockAddrEntry = _HpicfIpLockAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1)
)
hpicfIpLockAddrEntry.setIndexNames(
    (0, "HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrPort"),
    (0, "HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrType"),
    (0, "HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrIpAddress"),
)
if mibBuilder.loadTexts:
    hpicfIpLockAddrEntry.setStatus("current")
_HpicfIpLockAddrPort_Type = InterfaceIndex
_HpicfIpLockAddrPort_Object = MibTableColumn
hpicfIpLockAddrPort = _HpicfIpLockAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1, 1),
    _HpicfIpLockAddrPort_Type()
)
hpicfIpLockAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockAddrPort.setStatus("current")
_HpicfIpLockAddrType_Type = InetAddressType
_HpicfIpLockAddrType_Object = MibTableColumn
hpicfIpLockAddrType = _HpicfIpLockAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1, 2),
    _HpicfIpLockAddrType_Type()
)
hpicfIpLockAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockAddrType.setStatus("current")
_HpicfIpLockAddrIpAddress_Type = InetAddress
_HpicfIpLockAddrIpAddress_Object = MibTableColumn
hpicfIpLockAddrIpAddress = _HpicfIpLockAddrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1, 3),
    _HpicfIpLockAddrIpAddress_Type()
)
hpicfIpLockAddrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockAddrIpAddress.setStatus("current")
_HpicfIpLockAddrVlan_Type = VlanIndex
_HpicfIpLockAddrVlan_Object = MibTableColumn
hpicfIpLockAddrVlan = _HpicfIpLockAddrVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1, 4),
    _HpicfIpLockAddrVlan_Type()
)
hpicfIpLockAddrVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockAddrVlan.setStatus("current")
_HpicfIpLockAddrMacAddress_Type = MacAddress
_HpicfIpLockAddrMacAddress_Object = MibTableColumn
hpicfIpLockAddrMacAddress = _HpicfIpLockAddrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1, 5),
    _HpicfIpLockAddrMacAddress_Type()
)
hpicfIpLockAddrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockAddrMacAddress.setStatus("current")
_HpicfIpLockResourceAvailable_Type = TruthValue
_HpicfIpLockResourceAvailable_Object = MibTableColumn
hpicfIpLockResourceAvailable = _HpicfIpLockResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 1, 2, 2, 1, 6),
    _HpicfIpLockResourceAvailable_Type()
)
hpicfIpLockResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpLockResourceAvailable.setStatus("current")
_HpicfIpLockConformance_ObjectIdentity = ObjectIdentity
hpicfIpLockConformance = _HpicfIpLockConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2)
)
_HpicfIpLockGroups_ObjectIdentity = ObjectIdentity
hpicfIpLockGroups = _HpicfIpLockGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 1)
)
_HpicfIpLockCompliances_ObjectIdentity = ObjectIdentity
hpicfIpLockCompliances = _HpicfIpLockCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 2)
)

# Managed Objects groups

hpicfIpLockBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 1, 1)
)
hpicfIpLockBaseGroup.setObjects(
      *(("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockEnable"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockPortEnable"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockPortOperStatus"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrPort"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrType"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrIpAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrVlan"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrMacAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockResourceAvailable"))
)
if mibBuilder.loadTexts:
    hpicfIpLockBaseGroup.setStatus("current")

hpicfIpLockTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 1, 3)
)
hpicfIpLockTrapObjectsGroup.setObjects(
      *(("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockOutOfResourceSource"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyCount"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyPort"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifySrcIpType"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifySrcIpAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyDstIpType"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyDstIpAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyMacAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyPktCount"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockTrapCtrl"))
)
if mibBuilder.loadTexts:
    hpicfIpLockTrapObjectsGroup.setStatus("current")

hpicfIpLockObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 1, 4)
)
hpicfIpLockObsoleteGroup.setObjects(
    ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockTrapCntl")
)
if mibBuilder.loadTexts:
    hpicfIpLockObsoleteGroup.setStatus("obsolete")


# Notification objects

hpicfIpLockOutOfResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 2)
)
hpicfIpLockOutOfResources.setObjects(
      *(("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrPort"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrMacAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrIpAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockAddrVlan"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockOutOfResourceSource"))
)
if mibBuilder.loadTexts:
    hpicfIpLockOutOfResources.setStatus(
        "current"
    )

hpicfIpLockErrantNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 0, 1, 3)
)
hpicfIpLockErrantNotify.setObjects(
      *(("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyCount"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyPort"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifySrcIpType"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifySrcIpAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyDstIpType"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyDstIpAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyMacAddress"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockNotifyPktCount"))
)
if mibBuilder.loadTexts:
    hpicfIpLockErrantNotify.setStatus(
        "current"
    )


# Notifications groups

hpicfIpLockTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 1, 2)
)
hpicfIpLockTrapsGroup.setObjects(
      *(("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockOutOfResources"),
        ("HP-ICF-IP-LOCKDOWN-MIB", "hpicfIpLockErrantNotify"))
)
if mibBuilder.loadTexts:
    hpicfIpLockTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfIpLockCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfIpLockCompliance.setStatus(
        "current"
    )

hpicfIpLockTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfIpLockTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-IP-LOCKDOWN-MIB",
    **{"hpicfIpLockdown": hpicfIpLockdown,
       "hpicfIpLockTraps": hpicfIpLockTraps,
       "hpicfIpLockTrapsObjects": hpicfIpLockTrapsObjects,
       "hpicfIpLockOutOfResourceSource": hpicfIpLockOutOfResourceSource,
       "hpicfIpLockOutOfResources": hpicfIpLockOutOfResources,
       "hpicfIpLockErrantNotify": hpicfIpLockErrantNotify,
       "hpicfIpLockErrantNotifyObjects": hpicfIpLockErrantNotifyObjects,
       "hpicfIpLockNotifyCount": hpicfIpLockNotifyCount,
       "hpicfIpLockNotifyPort": hpicfIpLockNotifyPort,
       "hpicfIpLockNotifySrcIpType": hpicfIpLockNotifySrcIpType,
       "hpicfIpLockNotifySrcIpAddress": hpicfIpLockNotifySrcIpAddress,
       "hpicfIpLockNotifyDstIpType": hpicfIpLockNotifyDstIpType,
       "hpicfIpLockNotifyDstIpAddress": hpicfIpLockNotifyDstIpAddress,
       "hpicfIpLockNotifyMacAddress": hpicfIpLockNotifyMacAddress,
       "hpicfIpLockNotifyPktCount": hpicfIpLockNotifyPktCount,
       "hpicfIpLockObjects": hpicfIpLockObjects,
       "hpicfIpLockConfig": hpicfIpLockConfig,
       "hpicfIpLockEnable": hpicfIpLockEnable,
       "hpicfIpLockPortTable": hpicfIpLockPortTable,
       "hpicfIpLockPortEntry": hpicfIpLockPortEntry,
       "hpicfIpLockPortEnable": hpicfIpLockPortEnable,
       "hpicfIpLockTrapCntl": hpicfIpLockTrapCntl,
       "hpicfIpLockTrapCtrl": hpicfIpLockTrapCtrl,
       "hpicfIpLockStatus": hpicfIpLockStatus,
       "hpicfIpLockPortStatusTable": hpicfIpLockPortStatusTable,
       "hpicfIpLockPortStatusEntry": hpicfIpLockPortStatusEntry,
       "hpicfIpLockPortOperStatus": hpicfIpLockPortOperStatus,
       "hpicfIpLockAddrTable": hpicfIpLockAddrTable,
       "hpicfIpLockAddrEntry": hpicfIpLockAddrEntry,
       "hpicfIpLockAddrPort": hpicfIpLockAddrPort,
       "hpicfIpLockAddrType": hpicfIpLockAddrType,
       "hpicfIpLockAddrIpAddress": hpicfIpLockAddrIpAddress,
       "hpicfIpLockAddrVlan": hpicfIpLockAddrVlan,
       "hpicfIpLockAddrMacAddress": hpicfIpLockAddrMacAddress,
       "hpicfIpLockResourceAvailable": hpicfIpLockResourceAvailable,
       "hpicfIpLockConformance": hpicfIpLockConformance,
       "hpicfIpLockGroups": hpicfIpLockGroups,
       "hpicfIpLockBaseGroup": hpicfIpLockBaseGroup,
       "hpicfIpLockTrapsGroup": hpicfIpLockTrapsGroup,
       "hpicfIpLockTrapObjectsGroup": hpicfIpLockTrapObjectsGroup,
       "hpicfIpLockObsoleteGroup": hpicfIpLockObsoleteGroup,
       "hpicfIpLockCompliances": hpicfIpLockCompliances,
       "hpicfIpLockCompliance": hpicfIpLockCompliance,
       "hpicfIpLockTrapCompliance": hpicfIpLockTrapCompliance}
)
