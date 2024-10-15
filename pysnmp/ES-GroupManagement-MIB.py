# SNMP MIB module (ES-GroupManagement-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ES-GroupManagement-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:39 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddress(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_EthernetSwitch_ObjectIdentity = ObjectIdentity
ethernetSwitch = _EthernetSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15)
)
_GroupManagement_ObjectIdentity = ObjectIdentity
groupManagement = _GroupManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4)
)
_GroupParam_ObjectIdentity = ObjectIdentity
groupParam = _GroupParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1)
)


class _GmHandtime_Type(Integer32):
    """Custom type gmHandtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_GmHandtime_Type.__name__ = "Integer32"
_GmHandtime_Object = MibScalar
gmHandtime = _GmHandtime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 1),
    _GmHandtime_Type()
)
gmHandtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmHandtime.setStatus("current")


class _GmHoldtime_Type(Integer32):
    """Custom type gmHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_GmHoldtime_Type.__name__ = "Integer32"
_GmHoldtime_Object = MibScalar
gmHoldtime = _GmHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 2),
    _GmHoldtime_Type()
)
gmHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmHoldtime.setStatus("current")
_GmName_Type = OctetString
_GmName_Object = MibScalar
gmName = _GmName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 3),
    _GmName_Type()
)
gmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmName.setStatus("current")


class _GmSwitchRole_Type(Integer32):
    """Custom type gmSwitchRole based on Integer32"""
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
        *(("candidateSwitch", 3),
          ("commandSwitch", 1),
          ("independentSwitch", 4),
          ("memberSwitch", 2))
    )


_GmSwitchRole_Type.__name__ = "Integer32"
_GmSwitchRole_Object = MibScalar
gmSwitchRole = _GmSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 4),
    _GmSwitchRole_Type()
)
gmSwitchRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmSwitchRole.setStatus("current")
_GmIpPool_Type = OctetString
_GmIpPool_Object = MibScalar
gmIpPool = _GmIpPool_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 5),
    _GmIpPool_Type()
)
gmIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmIpPool.setStatus("current")
_TftpServerIpAddr_Type = IpAddress
_TftpServerIpAddr_Object = MibScalar
tftpServerIpAddr = _TftpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 6),
    _TftpServerIpAddr_Type()
)
tftpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIpAddr.setStatus("current")
_BelongedCmdMac_Type = MacAddress
_BelongedCmdMac_Object = MibScalar
belongedCmdMac = _BelongedCmdMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 1, 7),
    _BelongedCmdMac_Type()
)
belongedCmdMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belongedCmdMac.setStatus("current")
_NeighborDiscovery_ObjectIdentity = ObjectIdentity
neighborDiscovery = _NeighborDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2)
)


class _DpAdminStatus_Type(Integer32):
    """Custom type dpAdminStatus based on Integer32"""
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


_DpAdminStatus_Type.__name__ = "Integer32"
_DpAdminStatus_Object = MibScalar
dpAdminStatus = _DpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 1),
    _DpAdminStatus_Type()
)
dpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpAdminStatus.setStatus("current")


class _DpTimer_Type(Integer32):
    """Custom type dpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_DpTimer_Type.__name__ = "Integer32"
_DpTimer_Object = MibScalar
dpTimer = _DpTimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 2),
    _DpTimer_Type()
)
dpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimer.setStatus("current")


class _DpHoldtime_Type(Integer32):
    """Custom type dpHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_DpHoldtime_Type.__name__ = "Integer32"
_DpHoldtime_Object = MibScalar
dpHoldtime = _DpHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 3),
    _DpHoldtime_Type()
)
dpHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpHoldtime.setStatus("current")
_DpPortTable_Object = MibTable
dpPortTable = _DpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4)
)
if mibBuilder.loadTexts:
    dpPortTable.setStatus("current")
_DpPortEntry_Object = MibTableRow
dpPortEntry = _DpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4, 1)
)
dpPortEntry.setIndexNames(
    (0, "ES-GroupManagement-MIB", "dpPortId"),
)
if mibBuilder.loadTexts:
    dpPortEntry.setStatus("current")
_DpPortId_Type = Integer32
_DpPortId_Object = MibTableColumn
dpPortId = _DpPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4, 1, 1),
    _DpPortId_Type()
)
dpPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpPortId.setStatus("current")


class _DpPortAdminStatus_Type(Integer32):
    """Custom type dpPortAdminStatus based on Integer32"""
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


_DpPortAdminStatus_Type.__name__ = "Integer32"
_DpPortAdminStatus_Object = MibTableColumn
dpPortAdminStatus = _DpPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 4, 1, 2),
    _DpPortAdminStatus_Type()
)
dpPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPortAdminStatus.setStatus("current")
_DpTrunkTable_Object = MibTable
dpTrunkTable = _DpTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5)
)
if mibBuilder.loadTexts:
    dpTrunkTable.setStatus("current")
_DpTrunkEntry_Object = MibTableRow
dpTrunkEntry = _DpTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5, 1)
)
dpTrunkEntry.setIndexNames(
    (0, "ES-GroupManagement-MIB", "dpTrunkId"),
)
if mibBuilder.loadTexts:
    dpTrunkEntry.setStatus("current")
_DpTrunkId_Type = Integer32
_DpTrunkId_Object = MibTableColumn
dpTrunkId = _DpTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5, 1, 1),
    _DpTrunkId_Type()
)
dpTrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTrunkId.setStatus("current")


class _DpTrunkAdminStatus_Type(Integer32):
    """Custom type dpTrunkAdminStatus based on Integer32"""
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


_DpTrunkAdminStatus_Type.__name__ = "Integer32"
_DpTrunkAdminStatus_Object = MibTableColumn
dpTrunkAdminStatus = _DpTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 2, 5, 1, 2),
    _DpTrunkAdminStatus_Type()
)
dpTrunkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTrunkAdminStatus.setStatus("current")
_TopologyCollect_ObjectIdentity = ObjectIdentity
topologyCollect = _TopologyCollect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3)
)


class _TpAdminStatus_Type(Integer32):
    """Custom type tpAdminStatus based on Integer32"""
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


_TpAdminStatus_Type.__name__ = "Integer32"
_TpAdminStatus_Object = MibScalar
tpAdminStatus = _TpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 1),
    _TpAdminStatus_Type()
)
tpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpAdminStatus.setStatus("current")


class _TpVlan_Type(Integer32):
    """Custom type tpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpVlan_Type.__name__ = "Integer32"
_TpVlan_Object = MibScalar
tpVlan = _TpVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 2),
    _TpVlan_Type()
)
tpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpVlan.setStatus("current")


class _TpHop_Type(Integer32):
    """Custom type tpHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TpHop_Type.__name__ = "Integer32"
_TpHop_Object = MibScalar
tpHop = _TpHop_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 3),
    _TpHop_Type()
)
tpHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHop.setStatus("current")


class _TpTimer_Type(Integer32):
    """Custom type tpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpTimer_Type.__name__ = "Integer32"
_TpTimer_Object = MibScalar
tpTimer = _TpTimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 4),
    _TpTimer_Type()
)
tpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTimer.setStatus("current")


class _TpHopDelay_Type(Integer32):
    """Custom type tpHopDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TpHopDelay_Type.__name__ = "Integer32"
_TpHopDelay_Object = MibScalar
tpHopDelay = _TpHopDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 5),
    _TpHopDelay_Type()
)
tpHopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHopDelay.setStatus("current")


class _TpPortDelay_Type(Integer32):
    """Custom type tpPortDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TpPortDelay_Type.__name__ = "Integer32"
_TpPortDelay_Object = MibScalar
tpPortDelay = _TpPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 6),
    _TpPortDelay_Type()
)
tpPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortDelay.setStatus("current")


class _TpStart_Type(Integer32):
    """Custom type tpStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_TpStart_Type.__name__ = "Integer32"
_TpStart_Object = MibScalar
tpStart = _TpStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 7),
    _TpStart_Type()
)
tpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStart.setStatus("current")
_TpPortTable_Object = MibTable
tpPortTable = _TpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8)
)
if mibBuilder.loadTexts:
    tpPortTable.setStatus("current")
_TpPortEntry_Object = MibTableRow
tpPortEntry = _TpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8, 1)
)
tpPortEntry.setIndexNames(
    (0, "ES-GroupManagement-MIB", "tpPortId"),
)
if mibBuilder.loadTexts:
    tpPortEntry.setStatus("current")
_TpPortId_Type = Integer32
_TpPortId_Object = MibTableColumn
tpPortId = _TpPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8, 1, 1),
    _TpPortId_Type()
)
tpPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpPortId.setStatus("current")


class _TpPortAdminStatus_Type(Integer32):
    """Custom type tpPortAdminStatus based on Integer32"""
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


_TpPortAdminStatus_Type.__name__ = "Integer32"
_TpPortAdminStatus_Object = MibTableColumn
tpPortAdminStatus = _TpPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 8, 1, 2),
    _TpPortAdminStatus_Type()
)
tpPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortAdminStatus.setStatus("current")
_TpTrunkTable_Object = MibTable
tpTrunkTable = _TpTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9)
)
if mibBuilder.loadTexts:
    tpTrunkTable.setStatus("current")
_TpTrunkEntry_Object = MibTableRow
tpTrunkEntry = _TpTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9, 1)
)
tpTrunkEntry.setIndexNames(
    (0, "ES-GroupManagement-MIB", "tpTrunkId"),
)
if mibBuilder.loadTexts:
    tpTrunkEntry.setStatus("current")
_TpTrunkId_Type = Integer32
_TpTrunkId_Object = MibTableColumn
tpTrunkId = _TpTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9, 1, 1),
    _TpTrunkId_Type()
)
tpTrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpTrunkId.setStatus("current")


class _TpTrunkAdminStatus_Type(Integer32):
    """Custom type tpTrunkAdminStatus based on Integer32"""
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


_TpTrunkAdminStatus_Type.__name__ = "Integer32"
_TpTrunkAdminStatus_Object = MibTableColumn
tpTrunkAdminStatus = _TpTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 9, 1, 2),
    _TpTrunkAdminStatus_Type()
)
tpTrunkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpTrunkAdminStatus.setStatus("current")
_TpDeviceTable_Object = MibTable
tpDeviceTable = _TpDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10)
)
if mibBuilder.loadTexts:
    tpDeviceTable.setStatus("current")
_TpDeviceEntry_Object = MibTableRow
tpDeviceEntry = _TpDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1)
)
tpDeviceEntry.setIndexNames(
    (0, "ES-GroupManagement-MIB", "deviceMac"),
)
if mibBuilder.loadTexts:
    tpDeviceEntry.setStatus("current")
_DeviceMac_Type = MacAddress
_DeviceMac_Object = MibTableColumn
deviceMac = _DeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 1),
    _DeviceMac_Type()
)
deviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMac.setStatus("current")


class _DeviceId_Type(Integer32):
    """Custom type deviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DeviceId_Type.__name__ = "Integer32"
_DeviceId_Object = MibTableColumn
deviceId = _DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 2),
    _DeviceId_Type()
)
deviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceId.setStatus("current")
_DeviceIpAddr_Type = IpAddress
_DeviceIpAddr_Object = MibTableColumn
deviceIpAddr = _DeviceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 3),
    _DeviceIpAddr_Type()
)
deviceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIpAddr.setStatus("current")
_DeviceHop_Type = Integer32
_DeviceHop_Object = MibTableColumn
deviceHop = _DeviceHop_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 4),
    _DeviceHop_Type()
)
deviceHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHop.setStatus("current")
_DevicePlatform_Type = OctetString
_DevicePlatform_Object = MibTableColumn
devicePlatform = _DevicePlatform_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 5),
    _DevicePlatform_Type()
)
devicePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePlatform.setStatus("current")


class _DeviceRole_Type(Integer32):
    """Custom type deviceRole based on Integer32"""
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
        *(("candidateSwitch", 3),
          ("commandSwitch", 1),
          ("independentSwitch", 4),
          ("memberSwitch", 2))
    )


_DeviceRole_Type.__name__ = "Integer32"
_DeviceRole_Object = MibTableColumn
deviceRole = _DeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 6),
    _DeviceRole_Type()
)
deviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRole.setStatus("current")
_DevicePeerPort_Type = OctetString
_DevicePeerPort_Object = MibTableColumn
devicePeerPort = _DevicePeerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 7),
    _DevicePeerPort_Type()
)
devicePeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePeerPort.setStatus("current")
_DeviceBelongedMac_Type = MacAddress
_DeviceBelongedMac_Object = MibTableColumn
deviceBelongedMac = _DeviceBelongedMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 8),
    _DeviceBelongedMac_Type()
)
deviceBelongedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBelongedMac.setStatus("current")
_DeviceBelongedIpAddr_Type = IpAddress
_DeviceBelongedIpAddr_Object = MibTableColumn
deviceBelongedIpAddr = _DeviceBelongedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 3, 10, 1, 9),
    _DeviceBelongedIpAddr_Type()
)
deviceBelongedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBelongedIpAddr.setStatus("current")
_MemberManage_ObjectIdentity = ObjectIdentity
memberManage = _MemberManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4)
)
_MemberTable_Object = MibTable
memberTable = _MemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1)
)
if mibBuilder.loadTexts:
    memberTable.setStatus("current")
_MemberEntry_Object = MibTableRow
memberEntry = _MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1)
)
memberEntry.setIndexNames(
    (0, "ES-GroupManagement-MIB", "memMac"),
)
if mibBuilder.loadTexts:
    memberEntry.setStatus("current")
_MemMac_Type = MacAddress
_MemMac_Object = MibTableColumn
memMac = _MemMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 1),
    _MemMac_Type()
)
memMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMac.setStatus("current")
_MemId_Type = Integer32
_MemId_Object = MibTableColumn
memId = _MemId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 2),
    _MemId_Type()
)
memId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memId.setStatus("current")
_MemIpAddr_Type = IpAddress
_MemIpAddr_Object = MibTableColumn
memIpAddr = _MemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 3),
    _MemIpAddr_Type()
)
memIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIpAddr.setStatus("current")
_MemMask_Type = IpAddress
_MemMask_Object = MibTableColumn
memMask = _MemMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 4),
    _MemMask_Type()
)
memMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMask.setStatus("current")


class _MemStatus_Type(Integer32):
    """Custom type memStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MemStatus_Type.__name__ = "Integer32"
_MemStatus_Object = MibTableColumn
memStatus = _MemStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 5),
    _MemStatus_Type()
)
memStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStatus.setStatus("current")


class _MemRole_Type(Integer32):
    """Custom type memRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("candidateSwitch", 2),
          ("memberSwitch", 1))
    )


_MemRole_Type.__name__ = "Integer32"
_MemRole_Object = MibTableColumn
memRole = _MemRole_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 6),
    _MemRole_Type()
)
memRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memRole.setStatus("current")
_SnmpPortMap_Type = Unsigned32
_SnmpPortMap_Object = MibTableColumn
snmpPortMap = _SnmpPortMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 7),
    _SnmpPortMap_Type()
)
snmpPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPortMap.setStatus("current")


class _HttpPortMap_Type(Integer32):
    """Custom type httpPortMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_HttpPortMap_Type.__name__ = "Integer32"
_HttpPortMap_Object = MibTableColumn
httpPortMap = _HttpPortMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 8),
    _HttpPortMap_Type()
)
httpPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpPortMap.setStatus("current")


class _FtpPortMap_Type(Integer32):
    """Custom type ftpPortMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FtpPortMap_Type.__name__ = "Integer32"
_FtpPortMap_Object = MibTableColumn
ftpPortMap = _FtpPortMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 9),
    _FtpPortMap_Type()
)
ftpPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPortMap.setStatus("current")


class _TftpPortMap_Type(Integer32):
    """Custom type tftpPortMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_TftpPortMap_Type.__name__ = "Integer32"
_TftpPortMap_Object = MibTableColumn
tftpPortMap = _TftpPortMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 10),
    _TftpPortMap_Type()
)
tftpPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpPortMap.setStatus("current")
_TelnetPortMap_Type = Integer32
_TelnetPortMap_Object = MibTableColumn
telnetPortMap = _TelnetPortMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 11),
    _TelnetPortMap_Type()
)
telnetPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetPortMap.setStatus("current")
_SshPortMap_Type = Integer32
_SshPortMap_Object = MibTableColumn
sshPortMap = _SshPortMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 4, 1, 1, 12),
    _SshPortMap_Type()
)
sshPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshPortMap.setStatus("current")
_GmEnterpriseTrap_ObjectIdentity = ObjectIdentity
gmEnterpriseTrap = _GmEnterpriseTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 5)
)

# Managed Objects groups


# Notification objects

gmTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 5, 1)
)
if mibBuilder.loadTexts:
    gmTopologyChange.setStatus(
        "current"
    )

gmMemberUpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 4, 5, 2)
)
gmMemberUpDown.setObjects(
      *(("ES-GroupManagement-MIB", "memMac"),
        ("ES-GroupManagement-MIB", "memId"),
        ("ES-GroupManagement-MIB", "memIpAddr"),
        ("ES-GroupManagement-MIB", "memStatus"))
)
if mibBuilder.loadTexts:
    gmMemberUpDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES-GroupManagement-MIB",
    **{"MacAddress": MacAddress,
       "zte": zte,
       "ethernetSwitch": ethernetSwitch,
       "groupManagement": groupManagement,
       "groupParam": groupParam,
       "gmHandtime": gmHandtime,
       "gmHoldtime": gmHoldtime,
       "gmName": gmName,
       "gmSwitchRole": gmSwitchRole,
       "gmIpPool": gmIpPool,
       "tftpServerIpAddr": tftpServerIpAddr,
       "belongedCmdMac": belongedCmdMac,
       "neighborDiscovery": neighborDiscovery,
       "dpAdminStatus": dpAdminStatus,
       "dpTimer": dpTimer,
       "dpHoldtime": dpHoldtime,
       "dpPortTable": dpPortTable,
       "dpPortEntry": dpPortEntry,
       "dpPortId": dpPortId,
       "dpPortAdminStatus": dpPortAdminStatus,
       "dpTrunkTable": dpTrunkTable,
       "dpTrunkEntry": dpTrunkEntry,
       "dpTrunkId": dpTrunkId,
       "dpTrunkAdminStatus": dpTrunkAdminStatus,
       "topologyCollect": topologyCollect,
       "tpAdminStatus": tpAdminStatus,
       "tpVlan": tpVlan,
       "tpHop": tpHop,
       "tpTimer": tpTimer,
       "tpHopDelay": tpHopDelay,
       "tpPortDelay": tpPortDelay,
       "tpStart": tpStart,
       "tpPortTable": tpPortTable,
       "tpPortEntry": tpPortEntry,
       "tpPortId": tpPortId,
       "tpPortAdminStatus": tpPortAdminStatus,
       "tpTrunkTable": tpTrunkTable,
       "tpTrunkEntry": tpTrunkEntry,
       "tpTrunkId": tpTrunkId,
       "tpTrunkAdminStatus": tpTrunkAdminStatus,
       "tpDeviceTable": tpDeviceTable,
       "tpDeviceEntry": tpDeviceEntry,
       "deviceMac": deviceMac,
       "deviceId": deviceId,
       "deviceIpAddr": deviceIpAddr,
       "deviceHop": deviceHop,
       "devicePlatform": devicePlatform,
       "deviceRole": deviceRole,
       "devicePeerPort": devicePeerPort,
       "deviceBelongedMac": deviceBelongedMac,
       "deviceBelongedIpAddr": deviceBelongedIpAddr,
       "memberManage": memberManage,
       "memberTable": memberTable,
       "memberEntry": memberEntry,
       "memMac": memMac,
       "memId": memId,
       "memIpAddr": memIpAddr,
       "memMask": memMask,
       "memStatus": memStatus,
       "memRole": memRole,
       "snmpPortMap": snmpPortMap,
       "httpPortMap": httpPortMap,
       "ftpPortMap": ftpPortMap,
       "tftpPortMap": tftpPortMap,
       "telnetPortMap": telnetPortMap,
       "sshPortMap": sshPortMap,
       "gmEnterpriseTrap": gmEnterpriseTrap,
       "gmTopologyChange": gmTopologyChange,
       "gmMemberUpDown": gmMemberUpDown}
)
