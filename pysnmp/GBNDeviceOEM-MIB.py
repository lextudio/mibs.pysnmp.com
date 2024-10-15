# SNMP MIB module (GBNDeviceOEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNDeviceOEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:43 2024
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

(gbnDevice,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnDevice")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

bcm5600 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3)
)
bcm5600.setRevisions(
        ("1901-05-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OemArchIface_ObjectIdentity = ObjectIdentity
oemArchIface = _OemArchIface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1)
)
_OemArchIfaceTable_Object = MibTable
oemArchIfaceTable = _OemArchIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    oemArchIfaceTable.setStatus("current")
_OemArchIfaceEntry_Object = MibTableRow
oemArchIfaceEntry = _OemArchIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1)
)
oemArchIfaceEntry.setIndexNames(
    (0, "GBNDeviceOEM-MIB", "oemArchIfaceUnit"),
    (0, "GBNDeviceOEM-MIB", "oemArchIfacePort"),
)
if mibBuilder.loadTexts:
    oemArchIfaceEntry.setStatus("current")


class _OemArchIfaceUnit_Type(Integer32):
    """Custom type oemArchIfaceUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OemArchIfaceUnit_Type.__name__ = "Integer32"
_OemArchIfaceUnit_Object = MibTableColumn
oemArchIfaceUnit = _OemArchIfaceUnit_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 1),
    _OemArchIfaceUnit_Type()
)
oemArchIfaceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceUnit.setStatus("current")
_OemArchIfacePort_Type = Integer32
_OemArchIfacePort_Object = MibTableColumn
oemArchIfacePort = _OemArchIfacePort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 2),
    _OemArchIfacePort_Type()
)
oemArchIfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfacePort.setStatus("current")


class _OemArchIfaceLLWHPort_Type(Integer32):
    """Custom type oemArchIfaceLLWHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8193, 8296),
    )


_OemArchIfaceLLWHPort_Type.__name__ = "Integer32"
_OemArchIfaceLLWHPort_Object = MibTableColumn
oemArchIfaceLLWHPort = _OemArchIfaceLLWHPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 3),
    _OemArchIfaceLLWHPort_Type()
)
oemArchIfaceLLWHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceLLWHPort.setStatus("current")
_OemArchIfaceIfIndex_Type = Integer32
_OemArchIfaceIfIndex_Object = MibTableColumn
oemArchIfaceIfIndex = _OemArchIfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 4),
    _OemArchIfaceIfIndex_Type()
)
oemArchIfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceIfIndex.setStatus("current")


class _OemArchIfaceName_Type(DisplayString):
    """Custom type oemArchIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OemArchIfaceName_Type.__name__ = "DisplayString"
_OemArchIfaceName_Object = MibTableColumn
oemArchIfaceName = _OemArchIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 5),
    _OemArchIfaceName_Type()
)
oemArchIfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfaceName.setStatus("current")


class _OemArchIfaceEnable_Type(Integer32):
    """Custom type oemArchIfaceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_OemArchIfaceEnable_Type.__name__ = "Integer32"
_OemArchIfaceEnable_Object = MibTableColumn
oemArchIfaceEnable = _OemArchIfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 6),
    _OemArchIfaceEnable_Type()
)
oemArchIfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfaceEnable.setStatus("current")
_OemArchIfaceSTPEnable_Type = TruthValue
_OemArchIfaceSTPEnable_Object = MibTableColumn
oemArchIfaceSTPEnable = _OemArchIfaceSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 7),
    _OemArchIfaceSTPEnable_Type()
)
oemArchIfaceSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfaceSTPEnable.setStatus("current")


class _OemArchIfaceLink_Type(Integer32):
    """Custom type oemArchIfaceLink based on Integer32"""
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


_OemArchIfaceLink_Type.__name__ = "Integer32"
_OemArchIfaceLink_Object = MibTableColumn
oemArchIfaceLink = _OemArchIfaceLink_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 8),
    _OemArchIfaceLink_Type()
)
oemArchIfaceLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceLink.setStatus("current")


class _OemArchIfaceDuplexSpeedSet_Type(Integer32):
    """Custom type oemArchIfaceDuplexSpeedSet based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000", 7),
          ("half-10", 2),
          ("half-100", 4),
          ("half-1000", 6),
          ("illegal", 99))
    )


_OemArchIfaceDuplexSpeedSet_Type.__name__ = "Integer32"
_OemArchIfaceDuplexSpeedSet_Object = MibTableColumn
oemArchIfaceDuplexSpeedSet = _OemArchIfaceDuplexSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 9),
    _OemArchIfaceDuplexSpeedSet_Type()
)
oemArchIfaceDuplexSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfaceDuplexSpeedSet.setStatus("current")


class _OemArchIfaceDuplexSpeedGet_Type(Integer32):
    """Custom type oemArchIfaceDuplexSpeedGet based on Integer32"""
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
              8,
              9,
              10,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto_10", 8),
          ("auto_100", 9),
          ("auto_1000", 10),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000", 7),
          ("half-10", 2),
          ("half-100", 4),
          ("half-1000", 6),
          ("illegal", 99),
          ("unknown", 1))
    )


_OemArchIfaceDuplexSpeedGet_Type.__name__ = "Integer32"
_OemArchIfaceDuplexSpeedGet_Object = MibTableColumn
oemArchIfaceDuplexSpeedGet = _OemArchIfaceDuplexSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 10),
    _OemArchIfaceDuplexSpeedGet_Type()
)
oemArchIfaceDuplexSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceDuplexSpeedGet.setStatus("current")


class _OemArchIfacePortLoop_Type(Integer32):
    """Custom type oemArchIfacePortLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("externalEnable", 2),
          ("internalEnable", 1))
    )


_OemArchIfacePortLoop_Type.__name__ = "Integer32"
_OemArchIfacePortLoop_Object = MibTableColumn
oemArchIfacePortLoop = _OemArchIfacePortLoop_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 11),
    _OemArchIfacePortLoop_Type()
)
oemArchIfacePortLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfacePortLoop.setStatus("current")


class _OemArchIfaceFlowControl_Type(Integer32):
    """Custom type oemArchIfaceFlowControl based on Integer32"""
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


_OemArchIfaceFlowControl_Type.__name__ = "Integer32"
_OemArchIfaceFlowControl_Object = MibTableColumn
oemArchIfaceFlowControl = _OemArchIfaceFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 12),
    _OemArchIfaceFlowControl_Type()
)
oemArchIfaceFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfaceFlowControl.setStatus("current")
_OemArchIfaceTxVlanTagPkts_Type = Counter64
_OemArchIfaceTxVlanTagPkts_Object = MibTableColumn
oemArchIfaceTxVlanTagPkts = _OemArchIfaceTxVlanTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 13),
    _OemArchIfaceTxVlanTagPkts_Type()
)
oemArchIfaceTxVlanTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceTxVlanTagPkts.setStatus("current")
_OemArchIfaceTxL3Pkts_Type = Counter64
_OemArchIfaceTxL3Pkts_Object = MibTableColumn
oemArchIfaceTxL3Pkts = _OemArchIfaceTxL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 14),
    _OemArchIfaceTxL3Pkts_Type()
)
oemArchIfaceTxL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceTxL3Pkts.setStatus("current")
_OemArchIfaceTxL3AbortedPkts_Type = Counter64
_OemArchIfaceTxL3AbortedPkts_Object = MibTableColumn
oemArchIfaceTxL3AbortedPkts = _OemArchIfaceTxL3AbortedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 15),
    _OemArchIfaceTxL3AbortedPkts_Type()
)
oemArchIfaceTxL3AbortedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceTxL3AbortedPkts.setStatus("current")
_OemArchIfaceRxIpInHdrErrors_Type = Counter64
_OemArchIfaceRxIpInHdrErrors_Object = MibTableColumn
oemArchIfaceRxIpInHdrErrors = _OemArchIfaceRxIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 16),
    _OemArchIfaceRxIpInHdrErrors_Type()
)
oemArchIfaceRxIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemArchIfaceRxIpInHdrErrors.setStatus("current")


class _OemArchIfaceL2Tunneling_Type(Integer32):
    """Custom type oemArchIfaceL2Tunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_OemArchIfaceL2Tunneling_Type.__name__ = "Integer32"
_OemArchIfaceL2Tunneling_Object = MibTableColumn
oemArchIfaceL2Tunneling = _OemArchIfaceL2Tunneling_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 17),
    _OemArchIfaceL2Tunneling_Type()
)
oemArchIfaceL2Tunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemArchIfaceL2Tunneling.setStatus("current")
_OemArchIfaceTrap_ObjectIdentity = ObjectIdentity
oemArchIfaceTrap = _OemArchIfaceTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2)
)
_OemChip_ObjectIdentity = ObjectIdentity
oemChip = _OemChip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 2)
)


class _OemChipStub_Type(Integer32):
    """Custom type oemChipStub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chip-value2", 2),
          ("chip-value3", 3),
          ("noop", 1))
    )


_OemChipStub_Type.__name__ = "Integer32"
_OemChipStub_Object = MibScalar
oemChipStub = _OemChipStub_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 2, 1),
    _OemChipStub_Type()
)
oemChipStub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oemChipStub.setStatus("current")
_OemProdConformance_ObjectIdentity = ObjectIdentity
oemProdConformance = _OemProdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3)
)
_OemProdGroups_ObjectIdentity = ObjectIdentity
oemProdGroups = _OemProdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 1)
)
_OemProdCompliances_ObjectIdentity = ObjectIdentity
oemProdCompliances = _OemProdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 2)
)

# Managed Objects groups

oemArchIfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 1, 1)
)
oemArchIfaceGroup.setObjects(
      *(("GBNDeviceOEM-MIB", "oemArchIfaceLLWHPort"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceIfIndex"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceName"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceEnable"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceSTPEnable"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceLink"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceDuplexSpeedSet"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceDuplexSpeedGet"),
        ("GBNDeviceOEM-MIB", "oemArchIfacePortLoop"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceFlowControl"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceTxVlanTagPkts"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceTxL3Pkts"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceTxL3AbortedPkts"),
        ("GBNDeviceOEM-MIB", "oemArchIfaceRxIpInHdrErrors"))
)
if mibBuilder.loadTexts:
    oemArchIfaceGroup.setStatus("current")

oemChipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 1, 2)
)
oemChipGroup.setObjects(
    ("GBNDeviceOEM-MIB", "oemChipStub")
)
if mibBuilder.loadTexts:
    oemChipGroup.setStatus("current")


# Notification objects

macAddrLimitOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 1)
)
macAddrLimitOn.setObjects(
    ("GBNDeviceOEM-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    macAddrLimitOn.setStatus(
        "current"
    )

macAddrLimitOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 2)
)
macAddrLimitOff.setObjects(
    ("GBNDeviceOEM-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    macAddrLimitOff.setStatus(
        "current"
    )

stormCtrlPortShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 3)
)
stormCtrlPortShutdown.setObjects(
    ("GBNDeviceOEM-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    stormCtrlPortShutdown.setStatus(
        "current"
    )

stormCtrlPortFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 4)
)
stormCtrlPortFree.setObjects(
    ("GBNDeviceOEM-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    stormCtrlPortFree.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

oemProdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oemProdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNDeviceOEM-MIB",
    **{"bcm5600": bcm5600,
       "oemArchIface": oemArchIface,
       "oemArchIfaceTable": oemArchIfaceTable,
       "oemArchIfaceEntry": oemArchIfaceEntry,
       "oemArchIfaceUnit": oemArchIfaceUnit,
       "oemArchIfacePort": oemArchIfacePort,
       "oemArchIfaceLLWHPort": oemArchIfaceLLWHPort,
       "oemArchIfaceIfIndex": oemArchIfaceIfIndex,
       "oemArchIfaceName": oemArchIfaceName,
       "oemArchIfaceEnable": oemArchIfaceEnable,
       "oemArchIfaceSTPEnable": oemArchIfaceSTPEnable,
       "oemArchIfaceLink": oemArchIfaceLink,
       "oemArchIfaceDuplexSpeedSet": oemArchIfaceDuplexSpeedSet,
       "oemArchIfaceDuplexSpeedGet": oemArchIfaceDuplexSpeedGet,
       "oemArchIfacePortLoop": oemArchIfacePortLoop,
       "oemArchIfaceFlowControl": oemArchIfaceFlowControl,
       "oemArchIfaceTxVlanTagPkts": oemArchIfaceTxVlanTagPkts,
       "oemArchIfaceTxL3Pkts": oemArchIfaceTxL3Pkts,
       "oemArchIfaceTxL3AbortedPkts": oemArchIfaceTxL3AbortedPkts,
       "oemArchIfaceRxIpInHdrErrors": oemArchIfaceRxIpInHdrErrors,
       "oemArchIfaceL2Tunneling": oemArchIfaceL2Tunneling,
       "oemArchIfaceTrap": oemArchIfaceTrap,
       "macAddrLimitOn": macAddrLimitOn,
       "macAddrLimitOff": macAddrLimitOff,
       "stormCtrlPortShutdown": stormCtrlPortShutdown,
       "stormCtrlPortFree": stormCtrlPortFree,
       "oemChip": oemChip,
       "oemChipStub": oemChipStub,
       "oemProdConformance": oemProdConformance,
       "oemProdGroups": oemProdGroups,
       "oemArchIfaceGroup": oemArchIfaceGroup,
       "oemChipGroup": oemChipGroup,
       "oemProdCompliances": oemProdCompliances,
       "oemProdCompliance": oemProdCompliance}
)
