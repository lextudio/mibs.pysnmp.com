# SNMP MIB module (HUAWEI-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:00 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifAdminStatus,
 ifDescr,
 ifIndex,
 ifName,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifName",
    "ifOperStatus")

(ipAdEntNetMask,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntNetMask")

(PortList,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwIFExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class SnmpPasswdString(OctetString, TextualConvention):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class HWDirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class HwIpAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("sub", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwIFExtObjects_ObjectIdentity = ObjectIdentity
hwIFExtObjects = _HwIFExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1)
)
_HwIFExtBase_ObjectIdentity = ObjectIdentity
hwIFExtBase = _HwIFExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1)
)
_HwIFExtTable_Object = MibTable
hwIFExtTable = _HwIFExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwIFExtTable.setStatus("current")
_HwIFExtEntry_Object = MibTableRow
hwIFExtEntry = _HwIFExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1)
)
hwIFExtEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIFExtIndex"),
)
if mibBuilder.loadTexts:
    hwIFExtEntry.setStatus("current")
_HwIFExtIndex_Type = InterfaceIndex
_HwIFExtIndex_Object = MibTableColumn
hwIFExtIndex = _HwIFExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 1),
    _HwIFExtIndex_Type()
)
hwIFExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIFExtIndex.setStatus("current")


class _HwIFExtLayer_Type(Integer32):
    """Custom type hwIFExtLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )


_HwIFExtLayer_Type.__name__ = "Integer32"
_HwIFExtLayer_Object = MibTableColumn
hwIFExtLayer = _HwIFExtLayer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 2),
    _HwIFExtLayer_Type()
)
hwIFExtLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtLayer.setStatus("current")


class _HwIFExtFrameType_Type(Integer32):
    """Custom type hwIFExtFrameType based on Integer32"""
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
        *(("ethernet8022", 3),
          ("ethernet8023", 4),
          ("ethernetII", 1),
          ("ethernetSnap", 2),
          ("other", 5))
    )


_HwIFExtFrameType_Type.__name__ = "Integer32"
_HwIFExtFrameType_Object = MibTableColumn
hwIFExtFrameType = _HwIFExtFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 3),
    _HwIFExtFrameType_Type()
)
hwIFExtFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIFExtFrameType.setStatus("current")


class _HwIFExtFlowStatInterval_Type(Integer32):
    """Custom type hwIFExtFlowStatInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_HwIFExtFlowStatInterval_Type.__name__ = "Integer32"
_HwIFExtFlowStatInterval_Object = MibTableColumn
hwIFExtFlowStatInterval = _HwIFExtFlowStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 4),
    _HwIFExtFlowStatInterval_Type()
)
hwIFExtFlowStatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtFlowStatInterval.setStatus("current")


class _HwIFExtFlushReceiveEnable_Type(EnabledStatus):
    """Custom type hwIFExtFlushReceiveEnable based on EnabledStatus"""


_HwIFExtFlushReceiveEnable_Object = MibTableColumn
hwIFExtFlushReceiveEnable = _HwIFExtFlushReceiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 5),
    _HwIFExtFlushReceiveEnable_Type()
)
hwIFExtFlushReceiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtFlushReceiveEnable.setStatus("current")


class _HwIFExtFlushVlanId_Type(VlanIdOrNone):
    """Custom type hwIFExtFlushVlanId based on VlanIdOrNone"""
    defaultValue = 0


_HwIFExtFlushVlanId_Object = MibTableColumn
hwIFExtFlushVlanId = _HwIFExtFlushVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 6),
    _HwIFExtFlushVlanId_Type()
)
hwIFExtFlushVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtFlushVlanId.setStatus("current")


class _HwIFExtFlushPasswd_Type(SnmpPasswdString):
    """Custom type hwIFExtFlushPasswd based on SnmpPasswdString"""
    defaultHexValue = "00"


_HwIFExtFlushPasswd_Object = MibTableColumn
hwIFExtFlushPasswd = _HwIFExtFlushPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 7),
    _HwIFExtFlushPasswd_Type()
)
hwIFExtFlushPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtFlushPasswd.setStatus("current")


class _HwIFExtFlowStatus_Type(Integer32):
    """Custom type hwIFExtFlowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowDown", 2),
          ("flowUp", 1))
    )


_HwIFExtFlowStatus_Type.__name__ = "Integer32"
_HwIFExtFlowStatus_Object = MibTableColumn
hwIFExtFlowStatus = _HwIFExtFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 8),
    _HwIFExtFlowStatus_Type()
)
hwIFExtFlowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIFExtFlowStatus.setStatus("current")
_HwIFExtMtu_Type = Integer32
_HwIFExtMtu_Object = MibTableColumn
hwIFExtMtu = _HwIFExtMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 9),
    _HwIFExtMtu_Type()
)
hwIFExtMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtMtu.setStatus("current")
_HwIFExtMacAddr_Type = PhysAddress
_HwIFExtMacAddr_Object = MibTableColumn
hwIFExtMacAddr = _HwIFExtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 10),
    _HwIFExtMacAddr_Type()
)
hwIFExtMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtMacAddr.setStatus("current")


class _HwIFExtBlockPriority_Type(Integer32):
    """Custom type hwIFExtBlockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIFExtBlockPriority_Type.__name__ = "Integer32"
_HwIFExtBlockPriority_Object = MibTableColumn
hwIFExtBlockPriority = _HwIFExtBlockPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 11),
    _HwIFExtBlockPriority_Type()
)
hwIFExtBlockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtBlockPriority.setStatus("current")


class _HwIFExtMacShift_Type(Integer32):
    """Custom type hwIFExtMacShift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macShift", 2),
          ("normal", 1))
    )


_HwIFExtMacShift_Type.__name__ = "Integer32"
_HwIFExtMacShift_Object = MibTableColumn
hwIFExtMacShift = _HwIFExtMacShift_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 12),
    _HwIFExtMacShift_Type()
)
hwIFExtMacShift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFExtMacShift.setStatus("current")


class _HwIFExtSuppressStatus_Type(Integer32):
    """Custom type hwIFExtSuppressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("suppress", 1),
          ("unsuppress", 0))
    )


_HwIFExtSuppressStatus_Type.__name__ = "Integer32"
_HwIFExtSuppressStatus_Object = MibTableColumn
hwIFExtSuppressStatus = _HwIFExtSuppressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 1, 1, 13),
    _HwIFExtSuppressStatus_Type()
)
hwIFExtSuppressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIFExtSuppressStatus.setStatus("current")


class _HwIFExtPhyStatus_Type(Integer32):
    """Custom type hwIFExtPhyStatus based on Integer32"""
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


_HwIFExtPhyStatus_Type.__name__ = "Integer32"
_HwIFExtPhyStatus_Object = MibScalar
hwIFExtPhyStatus = _HwIFExtPhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 2),
    _HwIFExtPhyStatus_Type()
)
hwIFExtPhyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIFExtPhyStatus.setStatus("current")
_HwIFExtMemberOf_Type = DisplayString
_HwIFExtMemberOf_Object = MibScalar
hwIFExtMemberOf = _HwIFExtMemberOf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 3),
    _HwIFExtMemberOf_Type()
)
hwIFExtMemberOf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIFExtMemberOf.setStatus("current")
_HwLinkModeChangeAutoCreateIfTable_Object = MibTable
hwLinkModeChangeAutoCreateIfTable = _HwLinkModeChangeAutoCreateIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwLinkModeChangeAutoCreateIfTable.setStatus("current")
_HwLinkModeChangeAutoCreateIfEntry_Object = MibTableRow
hwLinkModeChangeAutoCreateIfEntry = _HwLinkModeChangeAutoCreateIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 4, 1)
)
hwLinkModeChangeAutoCreateIfEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwAutoIfIndex"),
)
if mibBuilder.loadTexts:
    hwLinkModeChangeAutoCreateIfEntry.setStatus("current")
_HwAutoIfIndex_Type = InterfaceIndex
_HwAutoIfIndex_Object = MibTableColumn
hwAutoIfIndex = _HwAutoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 4, 1, 1),
    _HwAutoIfIndex_Type()
)
hwAutoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAutoIfIndex.setStatus("current")


class _HwNewIfTimeslot_Type(Bits):
    """Custom type hwNewIfTimeslot based on Bits"""
    namedValues = NamedValues(
        *(("timeslot0", 0),
          ("timeslot1", 1),
          ("timeslot10", 10),
          ("timeslot11", 11),
          ("timeslot12", 12),
          ("timeslot13", 13),
          ("timeslot14", 14),
          ("timeslot15", 15),
          ("timeslot16", 16),
          ("timeslot17", 17),
          ("timeslot18", 18),
          ("timeslot19", 19),
          ("timeslot2", 2),
          ("timeslot20", 20),
          ("timeslot21", 21),
          ("timeslot22", 22),
          ("timeslot23", 23),
          ("timeslot24", 24),
          ("timeslot25", 25),
          ("timeslot26", 26),
          ("timeslot27", 27),
          ("timeslot28", 28),
          ("timeslot29", 29),
          ("timeslot3", 3),
          ("timeslot30", 30),
          ("timeslot31", 31),
          ("timeslot4", 4),
          ("timeslot5", 5),
          ("timeslot6", 6),
          ("timeslot7", 7),
          ("timeslot8", 8),
          ("timeslot9", 9))
    )

_HwNewIfTimeslot_Type.__name__ = "Bits"
_HwNewIfTimeslot_Object = MibTableColumn
hwNewIfTimeslot = _HwNewIfTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 4, 1, 2),
    _HwNewIfTimeslot_Type()
)
hwNewIfTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNewIfTimeslot.setStatus("current")
_HwIFExtPhyNumber_Type = Integer32
_HwIFExtPhyNumber_Object = MibScalar
hwIFExtPhyNumber = _HwIFExtPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 1, 5),
    _HwIFExtPhyNumber_Type()
)
hwIFExtPhyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIFExtPhyNumber.setStatus("current")
_HwInterfaceIp_ObjectIdentity = ObjectIdentity
hwInterfaceIp = _HwInterfaceIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2)
)
_HwIfIpTable_Object = MibTable
hwIfIpTable = _HwIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwIfIpTable.setStatus("current")
_HwIfIpEntry_Object = MibTableRow
hwIfIpEntry = _HwIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1)
)
hwIfIpEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    hwIfIpEntry.setStatus("current")
_HwIpAdEntAddr_Type = IpAddress
_HwIpAdEntAddr_Object = MibTableColumn
hwIpAdEntAddr = _HwIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 1),
    _HwIpAdEntAddr_Type()
)
hwIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpAdEntAddr.setStatus("current")
_HwIpAdEntIfIndex_Type = Integer32
_HwIpAdEntIfIndex_Object = MibTableColumn
hwIpAdEntIfIndex = _HwIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 2),
    _HwIpAdEntIfIndex_Type()
)
hwIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpAdEntIfIndex.setStatus("current")
_HwIpAdEntNetMask_Type = IpAddress
_HwIpAdEntNetMask_Object = MibTableColumn
hwIpAdEntNetMask = _HwIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 3),
    _HwIpAdEntNetMask_Type()
)
hwIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpAdEntNetMask.setStatus("current")
_HwIpAdEntBcastAddr_Type = Integer32
_HwIpAdEntBcastAddr_Object = MibTableColumn
hwIpAdEntBcastAddr = _HwIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 4),
    _HwIpAdEntBcastAddr_Type()
)
hwIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpAdEntBcastAddr.setStatus("current")


class _HwIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type hwIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_HwIpAdEntReasmMaxSize_Object = MibTableColumn
hwIpAdEntReasmMaxSize = _HwIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 5),
    _HwIpAdEntReasmMaxSize_Type()
)
hwIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpAdEntReasmMaxSize.setStatus("current")
_HwIpAdEntAddressType_Type = HwIpAddressType
_HwIpAdEntAddressType_Object = MibTableColumn
hwIpAdEntAddressType = _HwIpAdEntAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 6),
    _HwIpAdEntAddressType_Type()
)
hwIpAdEntAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpAdEntAddressType.setStatus("current")


class _HwIfIpMethod_Type(Integer32):
    """Custom type hwIfIpMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("assignedIp", 1),
          ("bootpIp", 3),
          ("dhcpIp", 2),
          ("linklayer", 5),
          ("other", 4),
          ("random", 6))
    )


_HwIfIpMethod_Type.__name__ = "Integer32"
_HwIfIpMethod_Object = MibTableColumn
hwIfIpMethod = _HwIfIpMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 7),
    _HwIfIpMethod_Type()
)
hwIfIpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfIpMethod.setStatus("current")
_HwIpAdEntAddrStatus_Type = RowStatus
_HwIpAdEntAddrStatus_Object = MibTableColumn
hwIpAdEntAddrStatus = _HwIpAdEntAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 1, 1, 8),
    _HwIpAdEntAddrStatus_Type()
)
hwIpAdEntAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpAdEntAddrStatus.setStatus("current")
_HwIfIpUnnumberedTable_Object = MibTable
hwIfIpUnnumberedTable = _HwIfIpUnnumberedTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwIfIpUnnumberedTable.setStatus("current")
_HwIfIpUnnumberedEntry_Object = MibTableRow
hwIfIpUnnumberedEntry = _HwIfIpUnnumberedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2, 1)
)
hwIfIpUnnumberedEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwUnnumberedIfIndex"),
)
if mibBuilder.loadTexts:
    hwIfIpUnnumberedEntry.setStatus("current")
_HwUnnumberedIfIndex_Type = InterfaceIndex
_HwUnnumberedIfIndex_Object = MibTableColumn
hwUnnumberedIfIndex = _HwUnnumberedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2, 1, 1),
    _HwUnnumberedIfIndex_Type()
)
hwUnnumberedIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwUnnumberedIfIndex.setStatus("current")
_HwLendIfIndex_Type = InterfaceIndex
_HwLendIfIndex_Object = MibTableColumn
hwLendIfIndex = _HwLendIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2, 1, 11),
    _HwLendIfIndex_Type()
)
hwLendIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLendIfIndex.setStatus("current")
_HwLendIpAddr_Type = IpAddress
_HwLendIpAddr_Object = MibTableColumn
hwLendIpAddr = _HwLendIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2, 1, 12),
    _HwLendIpAddr_Type()
)
hwLendIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLendIpAddr.setStatus("current")
_HwLendIpAddrNetMask_Type = IpAddress
_HwLendIpAddrNetMask_Object = MibTableColumn
hwLendIpAddrNetMask = _HwLendIpAddrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2, 1, 13),
    _HwLendIpAddrNetMask_Type()
)
hwLendIpAddrNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLendIpAddrNetMask.setStatus("current")
_HwUnnumberedRowStatus_Type = RowStatus
_HwUnnumberedRowStatus_Object = MibTableColumn
hwUnnumberedRowStatus = _HwUnnumberedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 2, 2, 1, 51),
    _HwUnnumberedRowStatus_Type()
)
hwUnnumberedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUnnumberedRowStatus.setStatus("current")
_HwTrunkAttr_ObjectIdentity = ObjectIdentity
hwTrunkAttr = _HwTrunkAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3)
)
_HwTrunkIfMax_Type = Integer32
_HwTrunkIfMax_Object = MibScalar
hwTrunkIfMax = _HwTrunkIfMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 1),
    _HwTrunkIfMax_Type()
)
hwTrunkIfMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkIfMax.setStatus("current")
_HwTrunkNextIndex_Type = Integer32
_HwTrunkNextIndex_Object = MibScalar
hwTrunkNextIndex = _HwTrunkNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 2),
    _HwTrunkNextIndex_Type()
)
hwTrunkNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkNextIndex.setStatus("current")
_HwTrunkIfTable_Object = MibTable
hwTrunkIfTable = _HwTrunkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwTrunkIfTable.setStatus("current")
_HwTrunkIfEntry_Object = MibTableRow
hwTrunkIfEntry = _HwTrunkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1)
)
hwTrunkIfEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwTrunkIndex"),
)
if mibBuilder.loadTexts:
    hwTrunkIfEntry.setStatus("current")
_HwTrunkIndex_Type = Integer32
_HwTrunkIndex_Object = MibTableColumn
hwTrunkIndex = _HwTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 1),
    _HwTrunkIndex_Type()
)
hwTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrunkIndex.setStatus("current")
_HwTrunkIfID_Type = Integer32
_HwTrunkIfID_Object = MibTableColumn
hwTrunkIfID = _HwTrunkIfID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 2),
    _HwTrunkIfID_Type()
)
hwTrunkIfID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfID.setStatus("current")


class _HwTrunkIfType_Type(Integer32):
    """Custom type hwTrunkIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethTrunk", 1),
          ("ipTrunk", 2))
    )


_HwTrunkIfType_Type.__name__ = "Integer32"
_HwTrunkIfType_Object = MibTableColumn
hwTrunkIfType = _HwTrunkIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 3),
    _HwTrunkIfType_Type()
)
hwTrunkIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfType.setStatus("current")
_HwTrunkIfIndex_Type = InterfaceIndex
_HwTrunkIfIndex_Object = MibTableColumn
hwTrunkIfIndex = _HwTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 4),
    _HwTrunkIfIndex_Type()
)
hwTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkIfIndex.setStatus("current")


class _HwTrunkIfModel_Type(Integer32):
    """Custom type hwTrunkIfModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("desIp", 9),
          ("desMac", 11),
          ("desPort", 13),
          ("fwdType", 15),
          ("invalid", -1),
          ("label", 18),
          ("labelNum", 17),
          ("packetAll", 1),
          ("packetTcp", 4),
          ("packetUdp", 3),
          ("qos", 16),
          ("sourceDesIp", 5),
          ("sourceDesMac", 2),
          ("sourceDesPort", 14),
          ("sourceIp", 8),
          ("sourceIpIpv6", 7),
          ("sourceMac", 10),
          ("sourceMacIpv6", 6),
          ("sourcePort", 12))
    )


_HwTrunkIfModel_Type.__name__ = "Integer32"
_HwTrunkIfModel_Object = MibTableColumn
hwTrunkIfModel = _HwTrunkIfModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 5),
    _HwTrunkIfModel_Type()
)
hwTrunkIfModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfModel.setStatus("current")
_HwTrunkIfBandWidthAffectLinkNum_Type = Integer32
_HwTrunkIfBandWidthAffectLinkNum_Object = MibTableColumn
hwTrunkIfBandWidthAffectLinkNum = _HwTrunkIfBandWidthAffectLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 6),
    _HwTrunkIfBandWidthAffectLinkNum_Type()
)
hwTrunkIfBandWidthAffectLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfBandWidthAffectLinkNum.setStatus("current")
_HwTrunkIfMinLinkNum_Type = Integer32
_HwTrunkIfMinLinkNum_Object = MibTableColumn
hwTrunkIfMinLinkNum = _HwTrunkIfMinLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 7),
    _HwTrunkIfMinLinkNum_Type()
)
hwTrunkIfMinLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfMinLinkNum.setStatus("current")
_HwTrunkIfRowStatus_Type = RowStatus
_HwTrunkIfRowStatus_Object = MibTableColumn
hwTrunkIfRowStatus = _HwTrunkIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 8),
    _HwTrunkIfRowStatus_Type()
)
hwTrunkIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfRowStatus.setStatus("current")


class _HwTrunkIfWorkingMode_Type(Integer32):
    """Custom type hwTrunkIfWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("lacpStaticMode", 3),
          ("masterBackup", 1),
          ("normalMode", 2))
    )


_HwTrunkIfWorkingMode_Type.__name__ = "Integer32"
_HwTrunkIfWorkingMode_Object = MibTableColumn
hwTrunkIfWorkingMode = _HwTrunkIfWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 9),
    _HwTrunkIfWorkingMode_Type()
)
hwTrunkIfWorkingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfWorkingMode.setStatus("current")


class _HwTrunkIfWorkingState_Type(Integer32):
    """Custom type hwTrunkIfWorkingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backupWorking", 4),
          ("generalMode", 1),
          ("initialization", 2),
          ("invalid", -1),
          ("masterWorking", 3))
    )


_HwTrunkIfWorkingState_Type.__name__ = "Integer32"
_HwTrunkIfWorkingState_Object = MibTableColumn
hwTrunkIfWorkingState = _HwTrunkIfWorkingState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 10),
    _HwTrunkIfWorkingState_Type()
)
hwTrunkIfWorkingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkIfWorkingState.setStatus("current")


class _HwTrunkIfAutoRecover_Type(Integer32):
    """Custom type hwTrunkIfAutoRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoRecover", 2),
          ("generalMode", 1),
          ("invalid", -1))
    )


_HwTrunkIfAutoRecover_Type.__name__ = "Integer32"
_HwTrunkIfAutoRecover_Object = MibTableColumn
hwTrunkIfAutoRecover = _HwTrunkIfAutoRecover_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 11),
    _HwTrunkIfAutoRecover_Type()
)
hwTrunkIfAutoRecover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfAutoRecover.setStatus("current")


class _HwTrunkIfPreemptEnable_Type(Integer32):
    """Custom type hwTrunkIfPreemptEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", -1))
    )


_HwTrunkIfPreemptEnable_Type.__name__ = "Integer32"
_HwTrunkIfPreemptEnable_Object = MibTableColumn
hwTrunkIfPreemptEnable = _HwTrunkIfPreemptEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 12),
    _HwTrunkIfPreemptEnable_Type()
)
hwTrunkIfPreemptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfPreemptEnable.setStatus("current")


class _HwTrunkIfPreemptDelay_Type(Integer32):
    """Custom type hwTrunkIfPreemptDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
        ValueRangeConstraint(-1, -1),
    )


_HwTrunkIfPreemptDelay_Type.__name__ = "Integer32"
_HwTrunkIfPreemptDelay_Object = MibTableColumn
hwTrunkIfPreemptDelay = _HwTrunkIfPreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 13),
    _HwTrunkIfPreemptDelay_Type()
)
hwTrunkIfPreemptDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfPreemptDelay.setStatus("current")


class _HwTrunkIfTimeoutReceive_Type(Integer32):
    """Custom type hwTrunkIfTimeoutReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("invalid", -1),
          ("slow", 2))
    )


_HwTrunkIfTimeoutReceive_Type.__name__ = "Integer32"
_HwTrunkIfTimeoutReceive_Object = MibTableColumn
hwTrunkIfTimeoutReceive = _HwTrunkIfTimeoutReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 14),
    _HwTrunkIfTimeoutReceive_Type()
)
hwTrunkIfTimeoutReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfTimeoutReceive.setStatus("current")


class _HwTrunkIfFlushSendEnable_Type(Integer32):
    """Custom type hwTrunkIfFlushSendEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", -1))
    )


_HwTrunkIfFlushSendEnable_Type.__name__ = "Integer32"
_HwTrunkIfFlushSendEnable_Object = MibTableColumn
hwTrunkIfFlushSendEnable = _HwTrunkIfFlushSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 15),
    _HwTrunkIfFlushSendEnable_Type()
)
hwTrunkIfFlushSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfFlushSendEnable.setStatus("current")


class _HwTrunkIfFlushVlanId_Type(Integer32):
    """Custom type hwTrunkIfFlushVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(-1, -1),
    )


_HwTrunkIfFlushVlanId_Type.__name__ = "Integer32"
_HwTrunkIfFlushVlanId_Object = MibTableColumn
hwTrunkIfFlushVlanId = _HwTrunkIfFlushVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 16),
    _HwTrunkIfFlushVlanId_Type()
)
hwTrunkIfFlushVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfFlushVlanId.setStatus("current")


class _HwTrunkIfFlushPasswd_Type(SnmpPasswdString):
    """Custom type hwTrunkIfFlushPasswd based on SnmpPasswdString"""
    defaultHexValue = "00"


_HwTrunkIfFlushPasswd_Object = MibTableColumn
hwTrunkIfFlushPasswd = _HwTrunkIfFlushPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 17),
    _HwTrunkIfFlushPasswd_Type()
)
hwTrunkIfFlushPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfFlushPasswd.setStatus("current")


class _HwTrunkIfForceSwitchEnable_Type(Integer32):
    """Custom type hwTrunkIfForceSwitchEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("invalid", -1))
    )


_HwTrunkIfForceSwitchEnable_Type.__name__ = "Integer32"
_HwTrunkIfForceSwitchEnable_Object = MibTableColumn
hwTrunkIfForceSwitchEnable = _HwTrunkIfForceSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 18),
    _HwTrunkIfForceSwitchEnable_Type()
)
hwTrunkIfForceSwitchEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfForceSwitchEnable.setStatus("current")


class _HwTrunkIfStatReset_Type(Integer32):
    """Custom type hwTrunkIfStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("ready", 2),
          ("reset", 1))
    )


_HwTrunkIfStatReset_Type.__name__ = "Integer32"
_HwTrunkIfStatReset_Object = MibTableColumn
hwTrunkIfStatReset = _HwTrunkIfStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 19),
    _HwTrunkIfStatReset_Type()
)
hwTrunkIfStatReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfStatReset.setStatus("current")
_HwTrunkBandwidth_Type = Integer32
_HwTrunkBandwidth_Object = MibTableColumn
hwTrunkBandwidth = _HwTrunkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 20),
    _HwTrunkBandwidth_Type()
)
hwTrunkBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkBandwidth.setStatus("current")


class _HwTrunkIfArpSendSpeed_Type(Integer32):
    """Custom type hwTrunkIfArpSendSpeed based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 3000),
        ValueRangeConstraint(-1, -1),
    )


_HwTrunkIfArpSendSpeed_Type.__name__ = "Integer32"
_HwTrunkIfArpSendSpeed_Object = MibTableColumn
hwTrunkIfArpSendSpeed = _HwTrunkIfArpSendSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 21),
    _HwTrunkIfArpSendSpeed_Type()
)
hwTrunkIfArpSendSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfArpSendSpeed.setStatus("current")


class _HwTrunkIfLagSelectedPortStd_Type(Integer32):
    """Custom type hwTrunkIfLagSelectedPortStd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("priority", 2),
          ("speed", 1))
    )


_HwTrunkIfLagSelectedPortStd_Type.__name__ = "Integer32"
_HwTrunkIfLagSelectedPortStd_Object = MibTableColumn
hwTrunkIfLagSelectedPortStd = _HwTrunkIfLagSelectedPortStd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 22),
    _HwTrunkIfLagSelectedPortStd_Type()
)
hwTrunkIfLagSelectedPortStd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfLagSelectedPortStd.setStatus("current")
_HwTrunkIfLagMaxActiveLinkNum_Type = Integer32
_HwTrunkIfLagMaxActiveLinkNum_Object = MibTableColumn
hwTrunkIfLagMaxActiveLinkNum = _HwTrunkIfLagMaxActiveLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 23),
    _HwTrunkIfLagMaxActiveLinkNum_Type()
)
hwTrunkIfLagMaxActiveLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkIfLagMaxActiveLinkNum.setStatus("current")


class _HwTrunkETrunkPriority_Type(Integer32):
    """Custom type hwTrunkETrunkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(-1, -1),
    )


_HwTrunkETrunkPriority_Type.__name__ = "Integer32"
_HwTrunkETrunkPriority_Object = MibTableColumn
hwTrunkETrunkPriority = _HwTrunkETrunkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 24),
    _HwTrunkETrunkPriority_Type()
)
hwTrunkETrunkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkETrunkPriority.setStatus("current")
_HwTrunkETrunkSysID_Type = PhysAddress
_HwTrunkETrunkSysID_Object = MibTableColumn
hwTrunkETrunkSysID = _HwTrunkETrunkSysID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 25),
    _HwTrunkETrunkSysID_Type()
)
hwTrunkETrunkSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkETrunkSysID.setStatus("current")


class _HwTrunkETrunkPriorityReset_Type(Integer32):
    """Custom type hwTrunkETrunkPriorityReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("no", 2),
          ("yes", 1))
    )


_HwTrunkETrunkPriorityReset_Type.__name__ = "Integer32"
_HwTrunkETrunkPriorityReset_Object = MibTableColumn
hwTrunkETrunkPriorityReset = _HwTrunkETrunkPriorityReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 26),
    _HwTrunkETrunkPriorityReset_Type()
)
hwTrunkETrunkPriorityReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkETrunkPriorityReset.setStatus("current")


class _HwTrunkETrunkSysIDReset_Type(Integer32):
    """Custom type hwTrunkETrunkSysIDReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("no", 2),
          ("yes", 1))
    )


_HwTrunkETrunkSysIDReset_Type.__name__ = "Integer32"
_HwTrunkETrunkSysIDReset_Object = MibTableColumn
hwTrunkETrunkSysIDReset = _HwTrunkETrunkSysIDReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 27),
    _HwTrunkETrunkSysIDReset_Type()
)
hwTrunkETrunkSysIDReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkETrunkSysIDReset.setStatus("current")


class _HwTrunkLocalPrefMode_Type(Integer32):
    """Custom type hwTrunkLocalPrefMode based on Integer32"""
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


_HwTrunkLocalPrefMode_Type.__name__ = "Integer32"
_HwTrunkLocalPrefMode_Object = MibTableColumn
hwTrunkLocalPrefMode = _HwTrunkLocalPrefMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 28),
    _HwTrunkLocalPrefMode_Type()
)
hwTrunkLocalPrefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkLocalPrefMode.setStatus("current")
_HwTrunkIfTrackVrrpVrid_Type = Integer32
_HwTrunkIfTrackVrrpVrid_Object = MibTableColumn
hwTrunkIfTrackVrrpVrid = _HwTrunkIfTrackVrrpVrid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 29),
    _HwTrunkIfTrackVrrpVrid_Type()
)
hwTrunkIfTrackVrrpVrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkIfTrackVrrpVrid.setStatus("current")
_HwTrunkIfTrackVrrpIfIndex_Type = InterfaceIndex
_HwTrunkIfTrackVrrpIfIndex_Object = MibTableColumn
hwTrunkIfTrackVrrpIfIndex = _HwTrunkIfTrackVrrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 30),
    _HwTrunkIfTrackVrrpIfIndex_Type()
)
hwTrunkIfTrackVrrpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkIfTrackVrrpIfIndex.setStatus("current")


class _HwTrunkIfTrackVrrpReset_Type(Integer32):
    """Custom type hwTrunkIfTrackVrrpReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("no", 2),
          ("yes", 1))
    )


_HwTrunkIfTrackVrrpReset_Type.__name__ = "Integer32"
_HwTrunkIfTrackVrrpReset_Object = MibTableColumn
hwTrunkIfTrackVrrpReset = _HwTrunkIfTrackVrrpReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 31),
    _HwTrunkIfTrackVrrpReset_Type()
)
hwTrunkIfTrackVrrpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkIfTrackVrrpReset.setStatus("current")


class _HwTrunkIfBackupPreemptEnable_Type(EnabledStatus):
    """Custom type hwTrunkIfBackupPreemptEnable based on EnabledStatus"""


_HwTrunkIfBackupPreemptEnable_Object = MibTableColumn
hwTrunkIfBackupPreemptEnable = _HwTrunkIfBackupPreemptEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 32),
    _HwTrunkIfBackupPreemptEnable_Type()
)
hwTrunkIfBackupPreemptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkIfBackupPreemptEnable.setStatus("current")


class _HwTrunkIfBackupPreemptDelay_Type(Integer32):
    """Custom type hwTrunkIfBackupPreemptDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
        ValueRangeConstraint(-1, -1),
    )


_HwTrunkIfBackupPreemptDelay_Type.__name__ = "Integer32"
_HwTrunkIfBackupPreemptDelay_Object = MibTableColumn
hwTrunkIfBackupPreemptDelay = _HwTrunkIfBackupPreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 3, 1, 33),
    _HwTrunkIfBackupPreemptDelay_Type()
)
hwTrunkIfBackupPreemptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkIfBackupPreemptDelay.setStatus("current")


class _HwTrunkSystemPriority_Type(Integer32):
    """Custom type hwTrunkSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwTrunkSystemPriority_Type.__name__ = "Integer32"
_HwTrunkSystemPriority_Object = MibScalar
hwTrunkSystemPriority = _HwTrunkSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 4),
    _HwTrunkSystemPriority_Type()
)
hwTrunkSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkSystemPriority.setStatus("current")


class _HwTrunkUnknownUnicastIfModel_Type(Integer32):
    """Custom type hwTrunkUnknownUnicastIfModel based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("desIp", 9),
          ("desMac", 11),
          ("desPort", 13),
          ("ipOrLabel", 16),
          ("label", 15),
          ("packetAll", 1),
          ("packetTcp", 4),
          ("packetUdp", 3),
          ("sourceDesIp", 5),
          ("sourceDesMac", 2),
          ("sourceDesPort", 14),
          ("sourceIp", 8),
          ("sourceIpIpv6", 7),
          ("sourceMac", 10),
          ("sourceMacIpv6", 6),
          ("sourcePort", 12))
    )


_HwTrunkUnknownUnicastIfModel_Type.__name__ = "Integer32"
_HwTrunkUnknownUnicastIfModel_Object = MibScalar
hwTrunkUnknownUnicastIfModel = _HwTrunkUnknownUnicastIfModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 5),
    _HwTrunkUnknownUnicastIfModel_Type()
)
hwTrunkUnknownUnicastIfModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkUnknownUnicastIfModel.setStatus("current")


class _HwTrunkETrunkSystemPriority_Type(Integer32):
    """Custom type hwTrunkETrunkSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwTrunkETrunkSystemPriority_Type.__name__ = "Integer32"
_HwTrunkETrunkSystemPriority_Object = MibScalar
hwTrunkETrunkSystemPriority = _HwTrunkETrunkSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 6),
    _HwTrunkETrunkSystemPriority_Type()
)
hwTrunkETrunkSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkETrunkSystemPriority.setStatus("current")
_HwTrunkETrunkSystemID_Type = PhysAddress
_HwTrunkETrunkSystemID_Object = MibScalar
hwTrunkETrunkSystemID = _HwTrunkETrunkSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 3, 7),
    _HwTrunkETrunkSystemID_Type()
)
hwTrunkETrunkSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrunkETrunkSystemID.setStatus("current")
_HwTrunkMemAttr_ObjectIdentity = ObjectIdentity
hwTrunkMemAttr = _HwTrunkMemAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4)
)
_HwTrunkMemTable_Object = MibTable
hwTrunkMemTable = _HwTrunkMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwTrunkMemTable.setStatus("current")
_HwTrunkMemEntry_Object = MibTableRow
hwTrunkMemEntry = _HwTrunkMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1)
)
hwTrunkMemEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwTrunkIndex"),
    (0, "HUAWEI-IF-EXT-MIB", "hwTrunkMemifIndex"),
)
if mibBuilder.loadTexts:
    hwTrunkMemEntry.setStatus("current")
_HwTrunkMemifIndex_Type = Integer32
_HwTrunkMemifIndex_Object = MibTableColumn
hwTrunkMemifIndex = _HwTrunkMemifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 1),
    _HwTrunkMemifIndex_Type()
)
hwTrunkMemifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrunkMemifIndex.setStatus("current")


class _HwTrunkValidEntry_Type(Integer32):
    """Custom type hwTrunkValidEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwTrunkValidEntry_Type.__name__ = "Integer32"
_HwTrunkValidEntry_Object = MibTableColumn
hwTrunkValidEntry = _HwTrunkValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 2),
    _HwTrunkValidEntry_Type()
)
hwTrunkValidEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkValidEntry.setStatus("current")


class _HwTrunkSelectStatus_Type(Integer32):
    """Custom type hwTrunkSelectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("trunkDeselected", 2),
          ("trunkSelected", 1))
    )


_HwTrunkSelectStatus_Type.__name__ = "Integer32"
_HwTrunkSelectStatus_Object = MibTableColumn
hwTrunkSelectStatus = _HwTrunkSelectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 3),
    _HwTrunkSelectStatus_Type()
)
hwTrunkSelectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkSelectStatus.setStatus("current")
_HwTrunkLacpStatus_Type = EnabledStatus
_HwTrunkLacpStatus_Object = MibTableColumn
hwTrunkLacpStatus = _HwTrunkLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 4),
    _HwTrunkLacpStatus_Type()
)
hwTrunkLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkLacpStatus.setStatus("current")
_HwTrunkDeleteFlag_Type = EnabledStatus
_HwTrunkDeleteFlag_Object = MibTableColumn
hwTrunkDeleteFlag = _HwTrunkDeleteFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 5),
    _HwTrunkDeleteFlag_Type()
)
hwTrunkDeleteFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkDeleteFlag.setStatus("current")


class _HwTrunkOperstatus_Type(Integer32):
    """Custom type hwTrunkOperstatus based on Integer32"""
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


_HwTrunkOperstatus_Type.__name__ = "Integer32"
_HwTrunkOperstatus_Object = MibTableColumn
hwTrunkOperstatus = _HwTrunkOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 6),
    _HwTrunkOperstatus_Type()
)
hwTrunkOperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkOperstatus.setStatus("current")
_HwTrunkIsDefaultLagRecv_Type = TruthValue
_HwTrunkIsDefaultLagRecv_Object = MibTableColumn
hwTrunkIsDefaultLagRecv = _HwTrunkIsDefaultLagRecv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 7),
    _HwTrunkIsDefaultLagRecv_Type()
)
hwTrunkIsDefaultLagRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrunkIsDefaultLagRecv.setStatus("current")
_HwTrunkPortWeight_Type = Unsigned32
_HwTrunkPortWeight_Object = MibTableColumn
hwTrunkPortWeight = _HwTrunkPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 8),
    _HwTrunkPortWeight_Type()
)
hwTrunkPortWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkPortWeight.setStatus("current")
_HwTrunkPortStandby_Type = Unsigned32
_HwTrunkPortStandby_Object = MibTableColumn
hwTrunkPortStandby = _HwTrunkPortStandby_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 9),
    _HwTrunkPortStandby_Type()
)
hwTrunkPortStandby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkPortStandby.setStatus("current")
_HwTrunkRowStatus_Type = RowStatus
_HwTrunkRowStatus_Object = MibTableColumn
hwTrunkRowStatus = _HwTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 10),
    _HwTrunkRowStatus_Type()
)
hwTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkRowStatus.setStatus("current")


class _HwTrunkPortMaster_Type(Integer32):
    """Custom type hwTrunkPortMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("portMaster", 2),
          ("portSlave", 1))
    )


_HwTrunkPortMaster_Type.__name__ = "Integer32"
_HwTrunkPortMaster_Object = MibTableColumn
hwTrunkPortMaster = _HwTrunkPortMaster_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 11),
    _HwTrunkPortMaster_Type()
)
hwTrunkPortMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkPortMaster.setStatus("current")


class _HwTrunkPortPriority_Type(Integer32):
    """Custom type hwTrunkPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(-1, -1),
    )


_HwTrunkPortPriority_Type.__name__ = "Integer32"
_HwTrunkPortPriority_Object = MibTableColumn
hwTrunkPortPriority = _HwTrunkPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 12),
    _HwTrunkPortPriority_Type()
)
hwTrunkPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkPortPriority.setStatus("current")


class _HwTrunkPortStatReset_Type(Integer32):
    """Custom type hwTrunkPortStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("ready", 2),
          ("reset", 1))
    )


_HwTrunkPortStatReset_Type.__name__ = "Integer32"
_HwTrunkPortStatReset_Object = MibTableColumn
hwTrunkPortStatReset = _HwTrunkPortStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 4, 1, 1, 13),
    _HwTrunkPortStatReset_Type()
)
hwTrunkPortStatReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrunkPortStatReset.setStatus("current")
_HwIFFlowStat_ObjectIdentity = ObjectIdentity
hwIFFlowStat = _HwIFFlowStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 5)
)


class _HwIFFlowStatGlobalInterval_Type(Integer32):
    """Custom type hwIFFlowStatGlobalInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_HwIFFlowStatGlobalInterval_Type.__name__ = "Integer32"
_HwIFFlowStatGlobalInterval_Object = MibScalar
hwIFFlowStatGlobalInterval = _HwIFFlowStatGlobalInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 5, 1),
    _HwIFFlowStatGlobalInterval_Type()
)
hwIFFlowStatGlobalInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIFFlowStatGlobalInterval.setStatus("current")
_HwIfStatistics_ObjectIdentity = ObjectIdentity
hwIfStatistics = _HwIfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6)
)
_HwIfEtherStatTable_Object = MibTable
hwIfEtherStatTable = _HwIfEtherStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwIfEtherStatTable.setStatus("current")
_HwIfEtherStatEntry_Object = MibTableRow
hwIfEtherStatEntry = _HwIfEtherStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1)
)
hwIfEtherStatEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfEtherStatIfIndex"),
)
if mibBuilder.loadTexts:
    hwIfEtherStatEntry.setStatus("current")
_HwIfEtherStatIfIndex_Type = InterfaceIndex
_HwIfEtherStatIfIndex_Object = MibTableColumn
hwIfEtherStatIfIndex = _HwIfEtherStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 1),
    _HwIfEtherStatIfIndex_Type()
)
hwIfEtherStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfEtherStatIfIndex.setStatus("current")
_HwIfEtherStatInPkts64Octets_Type = Counter64
_HwIfEtherStatInPkts64Octets_Object = MibTableColumn
hwIfEtherStatInPkts64Octets = _HwIfEtherStatInPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 5),
    _HwIfEtherStatInPkts64Octets_Type()
)
hwIfEtherStatInPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPkts64Octets.setStatus("current")
_HwIfEtherStatInPkts65to127Octets_Type = Counter64
_HwIfEtherStatInPkts65to127Octets_Object = MibTableColumn
hwIfEtherStatInPkts65to127Octets = _HwIfEtherStatInPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 6),
    _HwIfEtherStatInPkts65to127Octets_Type()
)
hwIfEtherStatInPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPkts65to127Octets.setStatus("current")
_HwIfEtherStatInPkts128to255Octets_Type = Counter64
_HwIfEtherStatInPkts128to255Octets_Object = MibTableColumn
hwIfEtherStatInPkts128to255Octets = _HwIfEtherStatInPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 7),
    _HwIfEtherStatInPkts128to255Octets_Type()
)
hwIfEtherStatInPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPkts128to255Octets.setStatus("current")
_HwIfEtherStatInPkts256to511Octets_Type = Counter64
_HwIfEtherStatInPkts256to511Octets_Object = MibTableColumn
hwIfEtherStatInPkts256to511Octets = _HwIfEtherStatInPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 8),
    _HwIfEtherStatInPkts256to511Octets_Type()
)
hwIfEtherStatInPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPkts256to511Octets.setStatus("current")
_HwIfEtherStatInPkts512to1023Octets_Type = Counter64
_HwIfEtherStatInPkts512to1023Octets_Object = MibTableColumn
hwIfEtherStatInPkts512to1023Octets = _HwIfEtherStatInPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 9),
    _HwIfEtherStatInPkts512to1023Octets_Type()
)
hwIfEtherStatInPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPkts512to1023Octets.setStatus("current")
_HwIfEtherStatInPkts1024to1518Octets_Type = Counter64
_HwIfEtherStatInPkts1024to1518Octets_Object = MibTableColumn
hwIfEtherStatInPkts1024to1518Octets = _HwIfEtherStatInPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 10),
    _HwIfEtherStatInPkts1024to1518Octets_Type()
)
hwIfEtherStatInPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPkts1024to1518Octets.setStatus("current")
_HwIfEtherStatInJumboPkts_Type = Counter64
_HwIfEtherStatInJumboPkts_Object = MibTableColumn
hwIfEtherStatInJumboPkts = _HwIfEtherStatInJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 11),
    _HwIfEtherStatInJumboPkts_Type()
)
hwIfEtherStatInJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInJumboPkts.setStatus("current")
_HwIfEtherStatInCRCPkts_Type = Counter64
_HwIfEtherStatInCRCPkts_Object = MibTableColumn
hwIfEtherStatInCRCPkts = _HwIfEtherStatInCRCPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 12),
    _HwIfEtherStatInCRCPkts_Type()
)
hwIfEtherStatInCRCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInCRCPkts.setStatus("current")
_HwIfEtherStatInLongPkts_Type = Counter64
_HwIfEtherStatInLongPkts_Object = MibTableColumn
hwIfEtherStatInLongPkts = _HwIfEtherStatInLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 13),
    _HwIfEtherStatInLongPkts_Type()
)
hwIfEtherStatInLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInLongPkts.setStatus("current")
_HwIfEtherStatInJabberPkts_Type = Counter64
_HwIfEtherStatInJabberPkts_Object = MibTableColumn
hwIfEtherStatInJabberPkts = _HwIfEtherStatInJabberPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 14),
    _HwIfEtherStatInJabberPkts_Type()
)
hwIfEtherStatInJabberPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInJabberPkts.setStatus("current")
_HwIfEtherStatInFragmentPkts_Type = Counter64
_HwIfEtherStatInFragmentPkts_Object = MibTableColumn
hwIfEtherStatInFragmentPkts = _HwIfEtherStatInFragmentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 15),
    _HwIfEtherStatInFragmentPkts_Type()
)
hwIfEtherStatInFragmentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInFragmentPkts.setStatus("current")
_HwIfEtherStatInUnderSizePkts_Type = Counter64
_HwIfEtherStatInUnderSizePkts_Object = MibTableColumn
hwIfEtherStatInUnderSizePkts = _HwIfEtherStatInUnderSizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 16),
    _HwIfEtherStatInUnderSizePkts_Type()
)
hwIfEtherStatInUnderSizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInUnderSizePkts.setStatus("current")
_HwIfEtherStatInOverRunPkts_Type = Counter64
_HwIfEtherStatInOverRunPkts_Object = MibTableColumn
hwIfEtherStatInOverRunPkts = _HwIfEtherStatInOverRunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 17),
    _HwIfEtherStatInOverRunPkts_Type()
)
hwIfEtherStatInOverRunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInOverRunPkts.setStatus("current")
_HwIfEtherStatInPausePkts_Type = Counter64
_HwIfEtherStatInPausePkts_Object = MibTableColumn
hwIfEtherStatInPausePkts = _HwIfEtherStatInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 18),
    _HwIfEtherStatInPausePkts_Type()
)
hwIfEtherStatInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInPausePkts.setStatus("current")
_HwIfEtherStatOutJumboPkts_Type = Counter64
_HwIfEtherStatOutJumboPkts_Object = MibTableColumn
hwIfEtherStatOutJumboPkts = _HwIfEtherStatOutJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 19),
    _HwIfEtherStatOutJumboPkts_Type()
)
hwIfEtherStatOutJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutJumboPkts.setStatus("current")
_HwIfEtherStatOutOverflowPkts_Type = Counter64
_HwIfEtherStatOutOverflowPkts_Object = MibTableColumn
hwIfEtherStatOutOverflowPkts = _HwIfEtherStatOutOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 20),
    _HwIfEtherStatOutOverflowPkts_Type()
)
hwIfEtherStatOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutOverflowPkts.setStatus("current")
_HwIfEtherStatOutUnderRunPkts_Type = Counter64
_HwIfEtherStatOutUnderRunPkts_Object = MibTableColumn
hwIfEtherStatOutUnderRunPkts = _HwIfEtherStatOutUnderRunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 21),
    _HwIfEtherStatOutUnderRunPkts_Type()
)
hwIfEtherStatOutUnderRunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutUnderRunPkts.setStatus("current")
_HwIfEtherStatOutPausePkts_Type = Counter64
_HwIfEtherStatOutPausePkts_Object = MibTableColumn
hwIfEtherStatOutPausePkts = _HwIfEtherStatOutPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 22),
    _HwIfEtherStatOutPausePkts_Type()
)
hwIfEtherStatOutPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutPausePkts.setStatus("current")


class _HwIfEthIfStatReset_Type(Integer32):
    """Custom type hwIfEthIfStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("reset", 1))
    )


_HwIfEthIfStatReset_Type.__name__ = "Integer32"
_HwIfEthIfStatReset_Object = MibTableColumn
hwIfEthIfStatReset = _HwIfEthIfStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 23),
    _HwIfEthIfStatReset_Type()
)
hwIfEthIfStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfEthIfStatReset.setStatus("current")
_HwIfEtherStatInDropEventPkts_Type = Counter64
_HwIfEtherStatInDropEventPkts_Object = MibTableColumn
hwIfEtherStatInDropEventPkts = _HwIfEtherStatInDropEventPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 24),
    _HwIfEtherStatInDropEventPkts_Type()
)
hwIfEtherStatInDropEventPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInDropEventPkts.setStatus("current")
_HwIfEtherStatInAlignmentPkts_Type = Counter64
_HwIfEtherStatInAlignmentPkts_Object = MibTableColumn
hwIfEtherStatInAlignmentPkts = _HwIfEtherStatInAlignmentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 25),
    _HwIfEtherStatInAlignmentPkts_Type()
)
hwIfEtherStatInAlignmentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInAlignmentPkts.setStatus("current")
_HwIfEtherStatInSymbolPkts_Type = Counter64
_HwIfEtherStatInSymbolPkts_Object = MibTableColumn
hwIfEtherStatInSymbolPkts = _HwIfEtherStatInSymbolPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 26),
    _HwIfEtherStatInSymbolPkts_Type()
)
hwIfEtherStatInSymbolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInSymbolPkts.setStatus("current")
_HwIfEtherStatInIgnoredPkts_Type = Counter64
_HwIfEtherStatInIgnoredPkts_Object = MibTableColumn
hwIfEtherStatInIgnoredPkts = _HwIfEtherStatInIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 27),
    _HwIfEtherStatInIgnoredPkts_Type()
)
hwIfEtherStatInIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInIgnoredPkts.setStatus("current")
_HwIfEtherStatInFramePkts_Type = Counter64
_HwIfEtherStatInFramePkts_Object = MibTableColumn
hwIfEtherStatInFramePkts = _HwIfEtherStatInFramePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 28),
    _HwIfEtherStatInFramePkts_Type()
)
hwIfEtherStatInFramePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatInFramePkts.setStatus("current")
_HwIfEtherStatOutCollisionPkts_Type = Counter64
_HwIfEtherStatOutCollisionPkts_Object = MibTableColumn
hwIfEtherStatOutCollisionPkts = _HwIfEtherStatOutCollisionPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 29),
    _HwIfEtherStatOutCollisionPkts_Type()
)
hwIfEtherStatOutCollisionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutCollisionPkts.setStatus("current")
_HwIfEtherStatOutDeferredPkts_Type = Counter64
_HwIfEtherStatOutDeferredPkts_Object = MibTableColumn
hwIfEtherStatOutDeferredPkts = _HwIfEtherStatOutDeferredPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 30),
    _HwIfEtherStatOutDeferredPkts_Type()
)
hwIfEtherStatOutDeferredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutDeferredPkts.setStatus("current")
_HwIfEtherStatOutLateCollisionPkts_Type = Counter64
_HwIfEtherStatOutLateCollisionPkts_Object = MibTableColumn
hwIfEtherStatOutLateCollisionPkts = _HwIfEtherStatOutLateCollisionPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 31),
    _HwIfEtherStatOutLateCollisionPkts_Type()
)
hwIfEtherStatOutLateCollisionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutLateCollisionPkts.setStatus("current")
_HwIfEtherStatOutExcessiveCollisionPkts_Type = Counter64
_HwIfEtherStatOutExcessiveCollisionPkts_Object = MibTableColumn
hwIfEtherStatOutExcessiveCollisionPkts = _HwIfEtherStatOutExcessiveCollisionPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 32),
    _HwIfEtherStatOutExcessiveCollisionPkts_Type()
)
hwIfEtherStatOutExcessiveCollisionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutExcessiveCollisionPkts.setStatus("current")
_HwIfEtherStatOutBufferPurgationPkts_Type = Counter64
_HwIfEtherStatOutBufferPurgationPkts_Object = MibTableColumn
hwIfEtherStatOutBufferPurgationPkts = _HwIfEtherStatOutBufferPurgationPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 1, 1, 33),
    _HwIfEtherStatOutBufferPurgationPkts_Type()
)
hwIfEtherStatOutBufferPurgationPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfEtherStatOutBufferPurgationPkts.setStatus("current")
_HwIfSdhStatTable_Object = MibTable
hwIfSdhStatTable = _HwIfSdhStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hwIfSdhStatTable.setStatus("current")
_HwIfSdhStatEntry_Object = MibTableRow
hwIfSdhStatEntry = _HwIfSdhStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1)
)
hwIfSdhStatEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfSdhStatIfIndex"),
)
if mibBuilder.loadTexts:
    hwIfSdhStatEntry.setStatus("current")
_HwIfSdhStatIfIndex_Type = InterfaceIndex
_HwIfSdhStatIfIndex_Object = MibTableColumn
hwIfSdhStatIfIndex = _HwIfSdhStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 1),
    _HwIfSdhStatIfIndex_Type()
)
hwIfSdhStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfSdhStatIfIndex.setStatus("current")
_HwIfSdhStatInCRCPkts_Type = Counter64
_HwIfSdhStatInCRCPkts_Object = MibTableColumn
hwIfSdhStatInCRCPkts = _HwIfSdhStatInCRCPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 2),
    _HwIfSdhStatInCRCPkts_Type()
)
hwIfSdhStatInCRCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfSdhStatInCRCPkts.setStatus("current")
_HwIfSdhStatInShortPkts_Type = Counter64
_HwIfSdhStatInShortPkts_Object = MibTableColumn
hwIfSdhStatInShortPkts = _HwIfSdhStatInShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 3),
    _HwIfSdhStatInShortPkts_Type()
)
hwIfSdhStatInShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfSdhStatInShortPkts.setStatus("current")
_HwIfSdhStatInLongPkts_Type = Counter64
_HwIfSdhStatInLongPkts_Object = MibTableColumn
hwIfSdhStatInLongPkts = _HwIfSdhStatInLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 4),
    _HwIfSdhStatInLongPkts_Type()
)
hwIfSdhStatInLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfSdhStatInLongPkts.setStatus("current")
_HwIfSdhStatOutOverRunPkts_Type = Counter64
_HwIfSdhStatOutOverRunPkts_Object = MibTableColumn
hwIfSdhStatOutOverRunPkts = _HwIfSdhStatOutOverRunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 5),
    _HwIfSdhStatOutOverRunPkts_Type()
)
hwIfSdhStatOutOverRunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfSdhStatOutOverRunPkts.setStatus("current")
_HwIfSdhStatOutUnderRunPkts_Type = Counter64
_HwIfSdhStatOutUnderRunPkts_Object = MibTableColumn
hwIfSdhStatOutUnderRunPkts = _HwIfSdhStatOutUnderRunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 6),
    _HwIfSdhStatOutUnderRunPkts_Type()
)
hwIfSdhStatOutUnderRunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfSdhStatOutUnderRunPkts.setStatus("current")


class _HwIfSdhIfStatReset_Type(Integer32):
    """Custom type hwIfSdhIfStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("reset", 1))
    )


_HwIfSdhIfStatReset_Type.__name__ = "Integer32"
_HwIfSdhIfStatReset_Object = MibTableColumn
hwIfSdhIfStatReset = _HwIfSdhIfStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 2, 1, 7),
    _HwIfSdhIfStatReset_Type()
)
hwIfSdhIfStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfSdhIfStatReset.setStatus("current")
_HwIfAtmStatTable_Object = MibTable
hwIfAtmStatTable = _HwIfAtmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hwIfAtmStatTable.setStatus("current")
_HwIfAtmStatEntry_Object = MibTableRow
hwIfAtmStatEntry = _HwIfAtmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1)
)
hwIfAtmStatEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfAtmStatIfIndex"),
)
if mibBuilder.loadTexts:
    hwIfAtmStatEntry.setStatus("current")
_HwIfAtmStatIfIndex_Type = InterfaceIndex
_HwIfAtmStatIfIndex_Object = MibTableColumn
hwIfAtmStatIfIndex = _HwIfAtmStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 1),
    _HwIfAtmStatIfIndex_Type()
)
hwIfAtmStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfAtmStatIfIndex.setStatus("current")
_HwIfAtmStatInGoodCells_Type = Counter64
_HwIfAtmStatInGoodCells_Object = MibTableColumn
hwIfAtmStatInGoodCells = _HwIfAtmStatInGoodCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 2),
    _HwIfAtmStatInGoodCells_Type()
)
hwIfAtmStatInGoodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfAtmStatInGoodCells.setStatus("current")
_HwIfAtmStatInIdleCells_Type = Counter64
_HwIfAtmStatInIdleCells_Object = MibTableColumn
hwIfAtmStatInIdleCells = _HwIfAtmStatInIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 3),
    _HwIfAtmStatInIdleCells_Type()
)
hwIfAtmStatInIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfAtmStatInIdleCells.setStatus("current")
_HwIfAtmStatInCorrectedCells_Type = Counter64
_HwIfAtmStatInCorrectedCells_Object = MibTableColumn
hwIfAtmStatInCorrectedCells = _HwIfAtmStatInCorrectedCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 4),
    _HwIfAtmStatInCorrectedCells_Type()
)
hwIfAtmStatInCorrectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfAtmStatInCorrectedCells.setStatus("current")
_HwIfAtmStatInUncorrectedCells_Type = Counter64
_HwIfAtmStatInUncorrectedCells_Object = MibTableColumn
hwIfAtmStatInUncorrectedCells = _HwIfAtmStatInUncorrectedCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 5),
    _HwIfAtmStatInUncorrectedCells_Type()
)
hwIfAtmStatInUncorrectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfAtmStatInUncorrectedCells.setStatus("current")
_HwIfAtmStatOutGoodCells_Type = Counter64
_HwIfAtmStatOutGoodCells_Object = MibTableColumn
hwIfAtmStatOutGoodCells = _HwIfAtmStatOutGoodCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 6),
    _HwIfAtmStatOutGoodCells_Type()
)
hwIfAtmStatOutGoodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfAtmStatOutGoodCells.setStatus("current")
_HwIfAtmStatOutIdleCells_Type = Counter64
_HwIfAtmStatOutIdleCells_Object = MibTableColumn
hwIfAtmStatOutIdleCells = _HwIfAtmStatOutIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 7),
    _HwIfAtmStatOutIdleCells_Type()
)
hwIfAtmStatOutIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfAtmStatOutIdleCells.setStatus("current")


class _HwIfAtmIfStatReset_Type(Integer32):
    """Custom type hwIfAtmIfStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("reset", 1))
    )


_HwIfAtmIfStatReset_Type.__name__ = "Integer32"
_HwIfAtmIfStatReset_Object = MibTableColumn
hwIfAtmIfStatReset = _HwIfAtmIfStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 6, 3, 1, 8),
    _HwIfAtmIfStatReset_Type()
)
hwIfAtmIfStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfAtmIfStatReset.setStatus("current")
_HwIfMonitorObject_ObjectIdentity = ObjectIdentity
hwIfMonitorObject = _HwIfMonitorObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7)
)
_HwIfMonitorThresholdTable_Object = MibTable
hwIfMonitorThresholdTable = _HwIfMonitorThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwIfMonitorThresholdTable.setStatus("current")
_HwIfMonitorThresholdEntry_Object = MibTableRow
hwIfMonitorThresholdEntry = _HwIfMonitorThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1)
)
hwIfMonitorThresholdEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfMonitorIndex"),
)
if mibBuilder.loadTexts:
    hwIfMonitorThresholdEntry.setStatus("current")
_HwIfMonitorIndex_Type = InterfaceIndex
_HwIfMonitorIndex_Object = MibTableColumn
hwIfMonitorIndex = _HwIfMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 1),
    _HwIfMonitorIndex_Type()
)
hwIfMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfMonitorIndex.setStatus("current")
_HwIfMonitorCrcErrorStatistics_Type = Counter64
_HwIfMonitorCrcErrorStatistics_Object = MibTableColumn
hwIfMonitorCrcErrorStatistics = _HwIfMonitorCrcErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 2),
    _HwIfMonitorCrcErrorStatistics_Type()
)
hwIfMonitorCrcErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorCrcErrorStatistics.setStatus("current")


class _HwIfMonitorCrcErrorThreshold_Type(Integer32):
    """Custom type hwIfMonitorCrcErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIfMonitorCrcErrorThreshold_Type.__name__ = "Integer32"
_HwIfMonitorCrcErrorThreshold_Object = MibTableColumn
hwIfMonitorCrcErrorThreshold = _HwIfMonitorCrcErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 3),
    _HwIfMonitorCrcErrorThreshold_Type()
)
hwIfMonitorCrcErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorCrcErrorThreshold.setStatus("current")


class _HwIfMonitorCrcErrorInterval_Type(Integer32):
    """Custom type hwIfMonitorCrcErrorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIfMonitorCrcErrorInterval_Type.__name__ = "Integer32"
_HwIfMonitorCrcErrorInterval_Object = MibTableColumn
hwIfMonitorCrcErrorInterval = _HwIfMonitorCrcErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 4),
    _HwIfMonitorCrcErrorInterval_Type()
)
hwIfMonitorCrcErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorCrcErrorInterval.setStatus("current")
_HwIfMonitorSdhErrorStatistics_Type = Counter64
_HwIfMonitorSdhErrorStatistics_Object = MibTableColumn
hwIfMonitorSdhErrorStatistics = _HwIfMonitorSdhErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 5),
    _HwIfMonitorSdhErrorStatistics_Type()
)
hwIfMonitorSdhErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorSdhErrorStatistics.setStatus("current")


class _HwIfMonitorSdhErrorThreshold_Type(Integer32):
    """Custom type hwIfMonitorSdhErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIfMonitorSdhErrorThreshold_Type.__name__ = "Integer32"
_HwIfMonitorSdhErrorThreshold_Object = MibTableColumn
hwIfMonitorSdhErrorThreshold = _HwIfMonitorSdhErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 6),
    _HwIfMonitorSdhErrorThreshold_Type()
)
hwIfMonitorSdhErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhErrorThreshold.setStatus("current")


class _HwIfMonitorSdhErrorInterval_Type(Integer32):
    """Custom type hwIfMonitorSdhErrorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIfMonitorSdhErrorInterval_Type.__name__ = "Integer32"
_HwIfMonitorSdhErrorInterval_Object = MibTableColumn
hwIfMonitorSdhErrorInterval = _HwIfMonitorSdhErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 7),
    _HwIfMonitorSdhErrorInterval_Type()
)
hwIfMonitorSdhErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhErrorInterval.setStatus("current")


class _HwIfMonitorInputRatePercentage_Type(Integer32):
    """Custom type hwIfMonitorInputRatePercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwIfMonitorInputRatePercentage_Type.__name__ = "Integer32"
_HwIfMonitorInputRatePercentage_Object = MibTableColumn
hwIfMonitorInputRatePercentage = _HwIfMonitorInputRatePercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 8),
    _HwIfMonitorInputRatePercentage_Type()
)
hwIfMonitorInputRatePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorInputRatePercentage.setStatus("current")


class _HwIfMonitorInputRateThreshold_Type(Integer32):
    """Custom type hwIfMonitorInputRateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIfMonitorInputRateThreshold_Type.__name__ = "Integer32"
_HwIfMonitorInputRateThreshold_Object = MibTableColumn
hwIfMonitorInputRateThreshold = _HwIfMonitorInputRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 9),
    _HwIfMonitorInputRateThreshold_Type()
)
hwIfMonitorInputRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorInputRateThreshold.setStatus("current")


class _HwIfMonitorOutputRatePercentage_Type(Integer32):
    """Custom type hwIfMonitorOutputRatePercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwIfMonitorOutputRatePercentage_Type.__name__ = "Integer32"
_HwIfMonitorOutputRatePercentage_Object = MibTableColumn
hwIfMonitorOutputRatePercentage = _HwIfMonitorOutputRatePercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 10),
    _HwIfMonitorOutputRatePercentage_Type()
)
hwIfMonitorOutputRatePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorOutputRatePercentage.setStatus("current")


class _HwIfMonitorOutputRateThreshold_Type(Integer32):
    """Custom type hwIfMonitorOutputRateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIfMonitorOutputRateThreshold_Type.__name__ = "Integer32"
_HwIfMonitorOutputRateThreshold_Object = MibTableColumn
hwIfMonitorOutputRateThreshold = _HwIfMonitorOutputRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 11),
    _HwIfMonitorOutputRateThreshold_Type()
)
hwIfMonitorOutputRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorOutputRateThreshold.setStatus("current")
_HwIfMonitorPauseFrameStatistics_Type = Counter64
_HwIfMonitorPauseFrameStatistics_Object = MibTableColumn
hwIfMonitorPauseFrameStatistics = _HwIfMonitorPauseFrameStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 12),
    _HwIfMonitorPauseFrameStatistics_Type()
)
hwIfMonitorPauseFrameStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorPauseFrameStatistics.setStatus("current")


class _HwIfMonitorPauseFrameThreshold_Type(Integer32):
    """Custom type hwIfMonitorPauseFrameThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIfMonitorPauseFrameThreshold_Type.__name__ = "Integer32"
_HwIfMonitorPauseFrameThreshold_Object = MibTableColumn
hwIfMonitorPauseFrameThreshold = _HwIfMonitorPauseFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 13),
    _HwIfMonitorPauseFrameThreshold_Type()
)
hwIfMonitorPauseFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorPauseFrameThreshold.setStatus("current")


class _HwIfMonitorPauseFrameInterval_Type(Integer32):
    """Custom type hwIfMonitorPauseFrameInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIfMonitorPauseFrameInterval_Type.__name__ = "Integer32"
_HwIfMonitorPauseFrameInterval_Object = MibTableColumn
hwIfMonitorPauseFrameInterval = _HwIfMonitorPauseFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 14),
    _HwIfMonitorPauseFrameInterval_Type()
)
hwIfMonitorPauseFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorPauseFrameInterval.setStatus("current")


class _HwIfMonitorDelayValue_Type(Integer32):
    """Custom type hwIfMonitorDelayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorDelayValue_Type.__name__ = "Integer32"
_HwIfMonitorDelayValue_Object = MibTableColumn
hwIfMonitorDelayValue = _HwIfMonitorDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 15),
    _HwIfMonitorDelayValue_Type()
)
hwIfMonitorDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorDelayValue.setStatus("current")


class _HwIfMonitorDelayThreshold_Type(Integer32):
    """Custom type hwIfMonitorDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorDelayThreshold_Type.__name__ = "Integer32"
_HwIfMonitorDelayThreshold_Object = MibTableColumn
hwIfMonitorDelayThreshold = _HwIfMonitorDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 16),
    _HwIfMonitorDelayThreshold_Type()
)
hwIfMonitorDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorDelayThreshold.setStatus("current")


class _HwIfMonitorJitterValue_Type(Integer32):
    """Custom type hwIfMonitorJitterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorJitterValue_Type.__name__ = "Integer32"
_HwIfMonitorJitterValue_Object = MibTableColumn
hwIfMonitorJitterValue = _HwIfMonitorJitterValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 17),
    _HwIfMonitorJitterValue_Type()
)
hwIfMonitorJitterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorJitterValue.setStatus("current")


class _HwIfMonitorJitterThreshold_Type(Integer32):
    """Custom type hwIfMonitorJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorJitterThreshold_Type.__name__ = "Integer32"
_HwIfMonitorJitterThreshold_Object = MibTableColumn
hwIfMonitorJitterThreshold = _HwIfMonitorJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 18),
    _HwIfMonitorJitterThreshold_Type()
)
hwIfMonitorJitterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorJitterThreshold.setStatus("current")
_HwIfMonitorName_Type = DisplayString
_HwIfMonitorName_Object = MibTableColumn
hwIfMonitorName = _HwIfMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 19),
    _HwIfMonitorName_Type()
)
hwIfMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorName.setStatus("current")
_HwIfMonitorSdhB1ErrorStatistics_Type = Counter64
_HwIfMonitorSdhB1ErrorStatistics_Object = MibTableColumn
hwIfMonitorSdhB1ErrorStatistics = _HwIfMonitorSdhB1ErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 20),
    _HwIfMonitorSdhB1ErrorStatistics_Type()
)
hwIfMonitorSdhB1ErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorSdhB1ErrorStatistics.setStatus("current")


class _HwIfMonitorSdhB1ErrorThreshold_Type(Integer32):
    """Custom type hwIfMonitorSdhB1ErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorSdhB1ErrorThreshold_Type.__name__ = "Integer32"
_HwIfMonitorSdhB1ErrorThreshold_Object = MibTableColumn
hwIfMonitorSdhB1ErrorThreshold = _HwIfMonitorSdhB1ErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 21),
    _HwIfMonitorSdhB1ErrorThreshold_Type()
)
hwIfMonitorSdhB1ErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhB1ErrorThreshold.setStatus("current")


class _HwIfMonitorSdhB1ErrorInterval_Type(Integer32):
    """Custom type hwIfMonitorSdhB1ErrorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorSdhB1ErrorInterval_Type.__name__ = "Integer32"
_HwIfMonitorSdhB1ErrorInterval_Object = MibTableColumn
hwIfMonitorSdhB1ErrorInterval = _HwIfMonitorSdhB1ErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 22),
    _HwIfMonitorSdhB1ErrorInterval_Type()
)
hwIfMonitorSdhB1ErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhB1ErrorInterval.setStatus("current")
_HwIfMonitorSdhB2ErrorStatistics_Type = Counter64
_HwIfMonitorSdhB2ErrorStatistics_Object = MibTableColumn
hwIfMonitorSdhB2ErrorStatistics = _HwIfMonitorSdhB2ErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 23),
    _HwIfMonitorSdhB2ErrorStatistics_Type()
)
hwIfMonitorSdhB2ErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorSdhB2ErrorStatistics.setStatus("current")


class _HwIfMonitorSdhB2ErrorThreshold_Type(Integer32):
    """Custom type hwIfMonitorSdhB2ErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorSdhB2ErrorThreshold_Type.__name__ = "Integer32"
_HwIfMonitorSdhB2ErrorThreshold_Object = MibTableColumn
hwIfMonitorSdhB2ErrorThreshold = _HwIfMonitorSdhB2ErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 24),
    _HwIfMonitorSdhB2ErrorThreshold_Type()
)
hwIfMonitorSdhB2ErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhB2ErrorThreshold.setStatus("current")


class _HwIfMonitorSdhB2ErrorInterval_Type(Integer32):
    """Custom type hwIfMonitorSdhB2ErrorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorSdhB2ErrorInterval_Type.__name__ = "Integer32"
_HwIfMonitorSdhB2ErrorInterval_Object = MibTableColumn
hwIfMonitorSdhB2ErrorInterval = _HwIfMonitorSdhB2ErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 25),
    _HwIfMonitorSdhB2ErrorInterval_Type()
)
hwIfMonitorSdhB2ErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhB2ErrorInterval.setStatus("current")
_HwIfMonitorSymbolErrorStatistics_Type = Counter64
_HwIfMonitorSymbolErrorStatistics_Object = MibTableColumn
hwIfMonitorSymbolErrorStatistics = _HwIfMonitorSymbolErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 26),
    _HwIfMonitorSymbolErrorStatistics_Type()
)
hwIfMonitorSymbolErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorSymbolErrorStatistics.setStatus("current")


class _HwIfMonitorSymbolErrorThreshold_Type(Integer32):
    """Custom type hwIfMonitorSymbolErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorSymbolErrorThreshold_Type.__name__ = "Integer32"
_HwIfMonitorSymbolErrorThreshold_Object = MibTableColumn
hwIfMonitorSymbolErrorThreshold = _HwIfMonitorSymbolErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 27),
    _HwIfMonitorSymbolErrorThreshold_Type()
)
hwIfMonitorSymbolErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSymbolErrorThreshold.setStatus("current")


class _HwIfMonitorSymbolErrorInterval_Type(Integer32):
    """Custom type hwIfMonitorSymbolErrorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIfMonitorSymbolErrorInterval_Type.__name__ = "Integer32"
_HwIfMonitorSymbolErrorInterval_Object = MibTableColumn
hwIfMonitorSymbolErrorInterval = _HwIfMonitorSymbolErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 28),
    _HwIfMonitorSymbolErrorInterval_Type()
)
hwIfMonitorSymbolErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSymbolErrorInterval.setStatus("current")
_HwIfMonitorBadBytesErrorStatistics_Type = Counter64
_HwIfMonitorBadBytesErrorStatistics_Object = MibTableColumn
hwIfMonitorBadBytesErrorStatistics = _HwIfMonitorBadBytesErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 40),
    _HwIfMonitorBadBytesErrorStatistics_Type()
)
hwIfMonitorBadBytesErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfMonitorBadBytesErrorStatistics.setStatus("current")
_HwIfMonitorBadBytesErrorThreshold_Type = Integer32
_HwIfMonitorBadBytesErrorThreshold_Object = MibTableColumn
hwIfMonitorBadBytesErrorThreshold = _HwIfMonitorBadBytesErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 41),
    _HwIfMonitorBadBytesErrorThreshold_Type()
)
hwIfMonitorBadBytesErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorBadBytesErrorThreshold.setStatus("current")
_HwIfMonitorBadBytesErrorInterval_Type = Integer32
_HwIfMonitorBadBytesErrorInterval_Object = MibTableColumn
hwIfMonitorBadBytesErrorInterval = _HwIfMonitorBadBytesErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 7, 1, 1, 42),
    _HwIfMonitorBadBytesErrorInterval_Type()
)
hwIfMonitorBadBytesErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorBadBytesErrorInterval.setStatus("current")
_HwIfMonitorGeneral_ObjectIdentity = ObjectIdentity
hwIfMonitorGeneral = _HwIfMonitorGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8)
)
_HwIfMonitorCrcEnabledStatus_Type = EnabledStatus
_HwIfMonitorCrcEnabledStatus_Object = MibScalar
hwIfMonitorCrcEnabledStatus = _HwIfMonitorCrcEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 1),
    _HwIfMonitorCrcEnabledStatus_Type()
)
hwIfMonitorCrcEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorCrcEnabledStatus.setStatus("current")
_HwIfMonitorSdhEnabledStatus_Type = EnabledStatus
_HwIfMonitorSdhEnabledStatus_Object = MibScalar
hwIfMonitorSdhEnabledStatus = _HwIfMonitorSdhEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 2),
    _HwIfMonitorSdhEnabledStatus_Type()
)
hwIfMonitorSdhEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorSdhEnabledStatus.setStatus("current")
_HwIfMonitorInputRateEnabledStatus_Type = EnabledStatus
_HwIfMonitorInputRateEnabledStatus_Object = MibScalar
hwIfMonitorInputRateEnabledStatus = _HwIfMonitorInputRateEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 3),
    _HwIfMonitorInputRateEnabledStatus_Type()
)
hwIfMonitorInputRateEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorInputRateEnabledStatus.setStatus("current")
_HwIfMonitorOutputRateEnabledStatus_Type = EnabledStatus
_HwIfMonitorOutputRateEnabledStatus_Object = MibScalar
hwIfMonitorOutputRateEnabledStatus = _HwIfMonitorOutputRateEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 4),
    _HwIfMonitorOutputRateEnabledStatus_Type()
)
hwIfMonitorOutputRateEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorOutputRateEnabledStatus.setStatus("current")
_HwIfMonitorHalfDuplexEnabledStatus_Type = EnabledStatus
_HwIfMonitorHalfDuplexEnabledStatus_Object = MibScalar
hwIfMonitorHalfDuplexEnabledStatus = _HwIfMonitorHalfDuplexEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 5),
    _HwIfMonitorHalfDuplexEnabledStatus_Type()
)
hwIfMonitorHalfDuplexEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorHalfDuplexEnabledStatus.setStatus("current")
_HwIfMonitorPauseRisingEnabledStatus_Type = EnabledStatus
_HwIfMonitorPauseRisingEnabledStatus_Object = MibScalar
hwIfMonitorPauseRisingEnabledStatus = _HwIfMonitorPauseRisingEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 6),
    _HwIfMonitorPauseRisingEnabledStatus_Type()
)
hwIfMonitorPauseRisingEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorPauseRisingEnabledStatus.setStatus("current")
_HwIfMonitorPauseContinuingEnabledStatus_Type = EnabledStatus
_HwIfMonitorPauseContinuingEnabledStatus_Object = MibScalar
hwIfMonitorPauseContinuingEnabledStatus = _HwIfMonitorPauseContinuingEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 7),
    _HwIfMonitorPauseContinuingEnabledStatus_Type()
)
hwIfMonitorPauseContinuingEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMonitorPauseContinuingEnabledStatus.setStatus("current")
_HwifMonitorBadBytesEnabledStatus_Type = EnabledStatus
_HwifMonitorBadBytesEnabledStatus_Object = MibScalar
hwifMonitorBadBytesEnabledStatus = _HwifMonitorBadBytesEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 8, 8),
    _HwifMonitorBadBytesEnabledStatus_Type()
)
hwifMonitorBadBytesEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifMonitorBadBytesEnabledStatus.setStatus("current")
_HwAdminVrrpMemberIf_ObjectIdentity = ObjectIdentity
hwAdminVrrpMemberIf = _HwAdminVrrpMemberIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9)
)
_HwIfFlowChangeTime_Type = Integer32
_HwIfFlowChangeTime_Object = MibScalar
hwIfFlowChangeTime = _HwIfFlowChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 1),
    _HwIfFlowChangeTime_Type()
)
hwIfFlowChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIfFlowChangeTime.setStatus("obsolete")
_HwAdminVrrpMemberIfTable_Object = MibTable
hwAdminVrrpMemberIfTable = _HwAdminVrrpMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfTable.setStatus("obsolete")
_HwAdminVrrpMemberIfEntry_Object = MibTableRow
hwAdminVrrpMemberIfEntry = _HwAdminVrrpMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2, 1)
)
hwAdminVrrpMemberIfEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwAdminVrrpMemberIfIndex"),
)
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfEntry.setStatus("obsolete")
_HwAdminVrrpMemberIfIndex_Type = InterfaceIndex
_HwAdminVrrpMemberIfIndex_Object = MibTableColumn
hwAdminVrrpMemberIfIndex = _HwAdminVrrpMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2, 1, 1),
    _HwAdminVrrpMemberIfIndex_Type()
)
hwAdminVrrpMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfIndex.setStatus("obsolete")
_HwAdminVrrpVrid_Type = Integer32
_HwAdminVrrpVrid_Object = MibTableColumn
hwAdminVrrpVrid = _HwAdminVrrpVrid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2, 1, 2),
    _HwAdminVrrpVrid_Type()
)
hwAdminVrrpVrid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpVrid.setStatus("obsolete")
_HwAdminVrrpIfIndex_Type = InterfaceIndex
_HwAdminVrrpIfIndex_Object = MibTableColumn
hwAdminVrrpIfIndex = _HwAdminVrrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2, 1, 3),
    _HwAdminVrrpIfIndex_Type()
)
hwAdminVrrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpIfIndex.setStatus("obsolete")


class _HwAdminVrrpMemberIfFlowStatus_Type(Integer32):
    """Custom type hwAdminVrrpMemberIfFlowStatus based on Integer32"""
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


_HwAdminVrrpMemberIfFlowStatus_Type.__name__ = "Integer32"
_HwAdminVrrpMemberIfFlowStatus_Object = MibTableColumn
hwAdminVrrpMemberIfFlowStatus = _HwAdminVrrpMemberIfFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2, 1, 4),
    _HwAdminVrrpMemberIfFlowStatus_Type()
)
hwAdminVrrpMemberIfFlowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfFlowStatus.setStatus("obsolete")
_HwAdminVrrpMemberIfRowStatus_Type = RowStatus
_HwAdminVrrpMemberIfRowStatus_Object = MibTableColumn
hwAdminVrrpMemberIfRowStatus = _HwAdminVrrpMemberIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 9, 2, 1, 5),
    _HwAdminVrrpMemberIfRowStatus_Type()
)
hwAdminVrrpMemberIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfRowStatus.setStatus("obsolete")
_HwIfFluxLimit_ObjectIdentity = ObjectIdentity
hwIfFluxLimit = _HwIfFluxLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10)
)
_HwIfFluxLimitTable_Object = MibTable
hwIfFluxLimitTable = _HwIfFluxLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hwIfFluxLimitTable.setStatus("current")
_HwIfFluxLimitEntry_Object = MibTableRow
hwIfFluxLimitEntry = _HwIfFluxLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1)
)
hwIfFluxLimitEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfFluxIfIndex"),
    (0, "HUAWEI-IF-EXT-MIB", "hwIfFluxVlanId"),
)
if mibBuilder.loadTexts:
    hwIfFluxLimitEntry.setStatus("current")
_HwIfFluxIfIndex_Type = InterfaceIndex
_HwIfFluxIfIndex_Object = MibTableColumn
hwIfFluxIfIndex = _HwIfFluxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 1),
    _HwIfFluxIfIndex_Type()
)
hwIfFluxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfFluxIfIndex.setStatus("current")
_HwIfFluxVlanId_Type = VlanIdOrNone
_HwIfFluxVlanId_Object = MibTableColumn
hwIfFluxVlanId = _HwIfFluxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 2),
    _HwIfFluxVlanId_Type()
)
hwIfFluxVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfFluxVlanId.setStatus("current")
_HwIfFluxDirection_Type = HWDirectionType
_HwIfFluxDirection_Object = MibTableColumn
hwIfFluxDirection = _HwIfFluxDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 3),
    _HwIfFluxDirection_Type()
)
hwIfFluxDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfFluxDirection.setStatus("current")


class _HwIfFluxLimitType_Type(Integer32):
    """Custom type hwIfFluxLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcastSuppression", 1),
          ("multicastSuppression", 2),
          ("unknownUnicastSuppression", 3))
    )


_HwIfFluxLimitType_Type.__name__ = "Integer32"
_HwIfFluxLimitType_Object = MibTableColumn
hwIfFluxLimitType = _HwIfFluxLimitType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 4),
    _HwIfFluxLimitType_Type()
)
hwIfFluxLimitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfFluxLimitType.setStatus("current")
_HwIfFluxCir_Type = Integer32
_HwIfFluxCir_Object = MibTableColumn
hwIfFluxCir = _HwIfFluxCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 5),
    _HwIfFluxCir_Type()
)
hwIfFluxCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfFluxCir.setStatus("current")
_HwIfFluxCbs_Type = Integer32
_HwIfFluxCbs_Object = MibTableColumn
hwIfFluxCbs = _HwIfFluxCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 6),
    _HwIfFluxCbs_Type()
)
hwIfFluxCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfFluxCbs.setStatus("current")
_HwIfFluxRowStatus_Type = RowStatus
_HwIfFluxRowStatus_Object = MibTableColumn
hwIfFluxRowStatus = _HwIfFluxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 10, 1, 1, 7),
    _HwIfFluxRowStatus_Type()
)
hwIfFluxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfFluxRowStatus.setStatus("current")
_HwIfDiffServ_ObjectIdentity = ObjectIdentity
hwIfDiffServ = _HwIfDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11)
)
_HwIfDiffServTable_Object = MibTable
hwIfDiffServTable = _HwIfDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hwIfDiffServTable.setStatus("current")
_HwIfDiffServEntry_Object = MibTableRow
hwIfDiffServEntry = _HwIfDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11, 1, 1)
)
hwIfDiffServEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfDiffServIndex"),
)
if mibBuilder.loadTexts:
    hwIfDiffServEntry.setStatus("current")
_HwIfDiffServIndex_Type = InterfaceIndex
_HwIfDiffServIndex_Object = MibTableColumn
hwIfDiffServIndex = _HwIfDiffServIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11, 1, 1, 1),
    _HwIfDiffServIndex_Type()
)
hwIfDiffServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfDiffServIndex.setStatus("current")


class _HwIfDiffServMode_Type(Integer32):
    """Custom type hwIfDiffServMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 1),
          ("shortpipe", 3),
          ("uniform", 2))
    )


_HwIfDiffServMode_Type.__name__ = "Integer32"
_HwIfDiffServMode_Object = MibTableColumn
hwIfDiffServMode = _HwIfDiffServMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11, 1, 1, 2),
    _HwIfDiffServMode_Type()
)
hwIfDiffServMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfDiffServMode.setStatus("current")


class _HwIfDiffServServiceClass_Type(Integer32):
    """Custom type hwIfDiffServServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("default", 0),
          ("ef", 6))
    )


_HwIfDiffServServiceClass_Type.__name__ = "Integer32"
_HwIfDiffServServiceClass_Object = MibTableColumn
hwIfDiffServServiceClass = _HwIfDiffServServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11, 1, 1, 3),
    _HwIfDiffServServiceClass_Type()
)
hwIfDiffServServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfDiffServServiceClass.setStatus("current")


class _HwIfDiffServColor_Type(Integer32):
    """Custom type hwIfDiffServColor based on Integer32"""
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
        *(("default", 0),
          ("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwIfDiffServColor_Type.__name__ = "Integer32"
_HwIfDiffServColor_Object = MibTableColumn
hwIfDiffServColor = _HwIfDiffServColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 11, 1, 1, 4),
    _HwIfDiffServColor_Type()
)
hwIfDiffServColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfDiffServColor.setStatus("current")
_HwIfQuery_ObjectIdentity = ObjectIdentity
hwIfQuery = _HwIfQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 12)
)
_HwIfQueryTable_Object = MibTable
hwIfQueryTable = _HwIfQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 12, 1)
)
if mibBuilder.loadTexts:
    hwIfQueryTable.setStatus("current")
_HwIfQueryEntry_Object = MibTableRow
hwIfQueryEntry = _HwIfQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 12, 1, 1)
)
hwIfQueryEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwIfName"),
)
if mibBuilder.loadTexts:
    hwIfQueryEntry.setStatus("current")


class _HwIfName_Type(OctetString):
    """Custom type hwIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwIfName_Type.__name__ = "OctetString"
_HwIfName_Object = MibTableColumn
hwIfName = _HwIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 12, 1, 1, 1),
    _HwIfName_Type()
)
hwIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIfName.setStatus("current")
_HwIfIndex_Type = InterfaceIndex
_HwIfIndex_Object = MibTableColumn
hwIfIndex = _HwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 12, 1, 1, 2),
    _HwIfIndex_Type()
)
hwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfIndex.setStatus("current")
_HwLogicIfAttrib_ObjectIdentity = ObjectIdentity
hwLogicIfAttrib = _HwLogicIfAttrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13)
)
_HwLogicIfTable_Object = MibTable
hwLogicIfTable = _HwLogicIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwLogicIfTable.setStatus("current")
_HwLogicIfEntry_Object = MibTableRow
hwLogicIfEntry = _HwLogicIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1)
)
hwLogicIfEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwLogicIfIndex"),
)
if mibBuilder.loadTexts:
    hwLogicIfEntry.setStatus("current")
_HwLogicIfIndex_Type = InterfaceIndexOrZero
_HwLogicIfIndex_Object = MibTableColumn
hwLogicIfIndex = _HwLogicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1, 1),
    _HwLogicIfIndex_Type()
)
hwLogicIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLogicIfIndex.setStatus("current")
_HwLogicIfMainIndex_Type = InterfaceIndexOrZero
_HwLogicIfMainIndex_Object = MibTableColumn
hwLogicIfMainIndex = _HwLogicIfMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1, 11),
    _HwLogicIfMainIndex_Type()
)
hwLogicIfMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfMainIndex.setStatus("current")


class _HwLogicIfType_Type(Integer32):
    """Custom type hwLogicIfType based on Integer32"""
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
              11,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bridgeIf", 14),
          ("dslGroup", 16),
          ("imaGroup", 8),
          ("loopback", 2),
          ("mpGroup", 13),
          ("stackPort", 18),
          ("subAtm", 7),
          ("subAtmTrunk", 15),
          ("subEthTrunk", 5),
          ("subEthernet", 6),
          ("subImaGroup", 9),
          ("subSerial", 10),
          ("subVe", 4),
          ("tunnel", 11),
          ("ve", 1),
          ("vlanif", 3),
          ("wlanEss", 17))
    )


_HwLogicIfType_Type.__name__ = "Integer32"
_HwLogicIfType_Object = MibTableColumn
hwLogicIfType = _HwLogicIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1, 12),
    _HwLogicIfType_Type()
)
hwLogicIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLogicIfType.setStatus("current")


class _HwLogicIfName_Type(DisplayString):
    """Custom type hwLogicIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLogicIfName_Type.__name__ = "DisplayString"
_HwLogicIfName_Object = MibTableColumn
hwLogicIfName = _HwLogicIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1, 13),
    _HwLogicIfName_Type()
)
hwLogicIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLogicIfName.setStatus("current")


class _HwLogicIfParaOne_Type(Integer32):
    """Custom type hwLogicIfParaOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 255),
          ("p2mp", 2),
          ("p2p", 1))
    )


_HwLogicIfParaOne_Type.__name__ = "Integer32"
_HwLogicIfParaOne_Object = MibTableColumn
hwLogicIfParaOne = _HwLogicIfParaOne_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1, 14),
    _HwLogicIfParaOne_Type()
)
hwLogicIfParaOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLogicIfParaOne.setStatus("current")
_HwLogicIfRowStatus_Type = RowStatus
_HwLogicIfRowStatus_Object = MibTableColumn
hwLogicIfRowStatus = _HwLogicIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 1, 1, 51),
    _HwLogicIfRowStatus_Type()
)
hwLogicIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLogicIfRowStatus.setStatus("current")
_HwLogicIfHelpTable_Object = MibTable
hwLogicIfHelpTable = _HwLogicIfHelpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2)
)
if mibBuilder.loadTexts:
    hwLogicIfHelpTable.setStatus("current")
_HwLogicIfHelpEntry_Object = MibTableRow
hwLogicIfHelpEntry = _HwLogicIfHelpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1)
)
hwLogicIfHelpEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwLogicIfhelpType"),
)
if mibBuilder.loadTexts:
    hwLogicIfHelpEntry.setStatus("current")


class _HwLogicIfhelpType_Type(Integer32):
    """Custom type hwLogicIfhelpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              11,
              13,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dslGroup", 16),
          ("ima-Group", 8),
          ("mp-group", 13),
          ("tunnel", 11),
          ("ve", 1))
    )


_HwLogicIfhelpType_Type.__name__ = "Integer32"
_HwLogicIfhelpType_Object = MibTableColumn
hwLogicIfhelpType = _HwLogicIfhelpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 1),
    _HwLogicIfhelpType_Type()
)
hwLogicIfhelpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfhelpType.setStatus("current")


class _HwLogicIfChassisNumber_Type(OctetString):
    """Custom type hwLogicIfChassisNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_HwLogicIfChassisNumber_Type.__name__ = "OctetString"
_HwLogicIfChassisNumber_Object = MibTableColumn
hwLogicIfChassisNumber = _HwLogicIfChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 2),
    _HwLogicIfChassisNumber_Type()
)
hwLogicIfChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfChassisNumber.setStatus("current")


class _HwLogicIfSlotNumber_Type(OctetString):
    """Custom type hwLogicIfSlotNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwLogicIfSlotNumber_Type.__name__ = "OctetString"
_HwLogicIfSlotNumber_Object = MibTableColumn
hwLogicIfSlotNumber = _HwLogicIfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 3),
    _HwLogicIfSlotNumber_Type()
)
hwLogicIfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfSlotNumber.setStatus("current")


class _HwLogicIfCardNumber_Type(OctetString):
    """Custom type hwLogicIfCardNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_HwLogicIfCardNumber_Type.__name__ = "OctetString"
_HwLogicIfCardNumber_Object = MibTableColumn
hwLogicIfCardNumber = _HwLogicIfCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 4),
    _HwLogicIfCardNumber_Type()
)
hwLogicIfCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfCardNumber.setStatus("current")
_HwLogicIfMin_Type = Integer32
_HwLogicIfMin_Object = MibTableColumn
hwLogicIfMin = _HwLogicIfMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 5),
    _HwLogicIfMin_Type()
)
hwLogicIfMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfMin.setStatus("current")
_HwLogicIfMax_Type = Integer32
_HwLogicIfMax_Object = MibTableColumn
hwLogicIfMax = _HwLogicIfMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 6),
    _HwLogicIfMax_Type()
)
hwLogicIfMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfMax.setStatus("current")
_HwLogicIfTotal_Type = Integer32
_HwLogicIfTotal_Object = MibTableColumn
hwLogicIfTotal = _HwLogicIfTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 2, 1, 7),
    _HwLogicIfTotal_Type()
)
hwLogicIfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicIfTotal.setStatus("current")
_HwLogicIfDynamicHelpTable_Object = MibTable
hwLogicIfDynamicHelpTable = _HwLogicIfDynamicHelpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3)
)
if mibBuilder.loadTexts:
    hwLogicIfDynamicHelpTable.setStatus("current")
_HwLogicIfDynamicHelpEntry_Object = MibTableRow
hwLogicIfDynamicHelpEntry = _HwLogicIfDynamicHelpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1)
)
hwLogicIfDynamicHelpEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfhelpType"),
    (0, "HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfChassisNumber"),
    (0, "HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfSlotNumber"),
    (0, "HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfCardNumber"),
)
if mibBuilder.loadTexts:
    hwLogicIfDynamicHelpEntry.setStatus("current")


class _HwLogicDynamicIfhelpType_Type(Integer32):
    """Custom type hwLogicDynamicIfhelpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              11,
              13,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dslGroup", 16),
          ("ima-Group", 8),
          ("mp-group", 13),
          ("tunnel", 11),
          ("ve", 1))
    )


_HwLogicDynamicIfhelpType_Type.__name__ = "Integer32"
_HwLogicDynamicIfhelpType_Object = MibTableColumn
hwLogicDynamicIfhelpType = _HwLogicDynamicIfhelpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 1),
    _HwLogicDynamicIfhelpType_Type()
)
hwLogicDynamicIfhelpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfhelpType.setStatus("current")
_HwLogicDynamicIfChassisNumber_Type = Integer32
_HwLogicDynamicIfChassisNumber_Object = MibTableColumn
hwLogicDynamicIfChassisNumber = _HwLogicDynamicIfChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 2),
    _HwLogicDynamicIfChassisNumber_Type()
)
hwLogicDynamicIfChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfChassisNumber.setStatus("current")
_HwLogicDynamicIfSlotNumber_Type = Integer32
_HwLogicDynamicIfSlotNumber_Object = MibTableColumn
hwLogicDynamicIfSlotNumber = _HwLogicDynamicIfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 3),
    _HwLogicDynamicIfSlotNumber_Type()
)
hwLogicDynamicIfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfSlotNumber.setStatus("current")
_HwLogicDynamicIfCardNumber_Type = Integer32
_HwLogicDynamicIfCardNumber_Object = MibTableColumn
hwLogicDynamicIfCardNumber = _HwLogicDynamicIfCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 4),
    _HwLogicDynamicIfCardNumber_Type()
)
hwLogicDynamicIfCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfCardNumber.setStatus("current")
_HwLogicDynamicIfMin_Type = Integer32
_HwLogicDynamicIfMin_Object = MibTableColumn
hwLogicDynamicIfMin = _HwLogicDynamicIfMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 5),
    _HwLogicDynamicIfMin_Type()
)
hwLogicDynamicIfMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfMin.setStatus("current")
_HwLogicDynamicIfMax_Type = Integer32
_HwLogicDynamicIfMax_Object = MibTableColumn
hwLogicDynamicIfMax = _HwLogicDynamicIfMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 6),
    _HwLogicDynamicIfMax_Type()
)
hwLogicDynamicIfMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfMax.setStatus("current")
_HwLogicDynamicIfTotal_Type = Integer32
_HwLogicDynamicIfTotal_Object = MibTableColumn
hwLogicDynamicIfTotal = _HwLogicDynamicIfTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 13, 3, 1, 7),
    _HwLogicDynamicIfTotal_Type()
)
hwLogicDynamicIfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLogicDynamicIfTotal.setStatus("current")
_HwCppsObjects_ObjectIdentity = ObjectIdentity
hwCppsObjects = _HwCppsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14)
)
_HwCppsGlobalEnable_Type = EnabledStatus
_HwCppsGlobalEnable_Object = MibScalar
hwCppsGlobalEnable = _HwCppsGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 1),
    _HwCppsGlobalEnable_Type()
)
hwCppsGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCppsGlobalEnable.setStatus("current")
_HwCppsInterfaceTable_Object = MibTable
hwCppsInterfaceTable = _HwCppsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 2)
)
if mibBuilder.loadTexts:
    hwCppsInterfaceTable.setStatus("current")
_HwCppsInterfaceEntry_Object = MibTableRow
hwCppsInterfaceEntry = _HwCppsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 2, 1)
)
hwCppsInterfaceEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwCppsInterfaceEntry.setStatus("current")
_HwCppsInterfaceIndex_Type = InterfaceIndex
_HwCppsInterfaceIndex_Object = MibTableColumn
hwCppsInterfaceIndex = _HwCppsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 2, 1, 1),
    _HwCppsInterfaceIndex_Type()
)
hwCppsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsInterfaceIndex.setStatus("current")


class _HwCppsPortPvcEnable_Type(EnabledStatus):
    """Custom type hwCppsPortPvcEnable based on EnabledStatus"""


_HwCppsPortPvcEnable_Object = MibTableColumn
hwCppsPortPvcEnable = _HwCppsPortPvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 2, 1, 2),
    _HwCppsPortPvcEnable_Type()
)
hwCppsPortPvcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCppsPortPvcEnable.setStatus("current")


class _HwCppsPortVlanEnable_Type(EnabledStatus):
    """Custom type hwCppsPortVlanEnable based on EnabledStatus"""


_HwCppsPortVlanEnable_Object = MibTableColumn
hwCppsPortVlanEnable = _HwCppsPortVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 2, 1, 3),
    _HwCppsPortVlanEnable_Type()
)
hwCppsPortVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCppsPortVlanEnable.setStatus("current")
_HwCppsIfStatisticsTable_Object = MibTable
hwCppsIfStatisticsTable = _HwCppsIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 3)
)
if mibBuilder.loadTexts:
    hwCppsIfStatisticsTable.setStatus("current")
_HwCppsIfStatisticsEntry_Object = MibTableRow
hwCppsIfStatisticsEntry = _HwCppsIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 3, 1)
)
hwCppsIfStatisticsEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsIfStatisticsIndex"),
)
if mibBuilder.loadTexts:
    hwCppsIfStatisticsEntry.setStatus("current")
_HwCppsIfStatisticsIndex_Type = InterfaceIndex
_HwCppsIfStatisticsIndex_Object = MibTableColumn
hwCppsIfStatisticsIndex = _HwCppsIfStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 3, 1, 1),
    _HwCppsIfStatisticsIndex_Type()
)
hwCppsIfStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsIfStatisticsIndex.setStatus("current")
_HwCppsInterfacePktStatisic_Type = Counter64
_HwCppsInterfacePktStatisic_Object = MibTableColumn
hwCppsInterfacePktStatisic = _HwCppsInterfacePktStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 3, 1, 2),
    _HwCppsInterfacePktStatisic_Type()
)
hwCppsInterfacePktStatisic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCppsInterfacePktStatisic.setStatus("current")
_HwCppsInterfaceByteStatisic_Type = Counter64
_HwCppsInterfaceByteStatisic_Object = MibTableColumn
hwCppsInterfaceByteStatisic = _HwCppsInterfaceByteStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 3, 1, 3),
    _HwCppsInterfaceByteStatisic_Type()
)
hwCppsInterfaceByteStatisic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCppsInterfaceByteStatisic.setStatus("current")


class _HwCppsResetInterfaceStatisic_Type(Integer32):
    """Custom type hwCppsResetInterfaceStatisic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_HwCppsResetInterfaceStatisic_Type.__name__ = "Integer32"
_HwCppsResetInterfaceStatisic_Object = MibTableColumn
hwCppsResetInterfaceStatisic = _HwCppsResetInterfaceStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 3, 1, 4),
    _HwCppsResetInterfaceStatisic_Type()
)
hwCppsResetInterfaceStatisic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCppsResetInterfaceStatisic.setStatus("current")
_HwCppsAtmPvcTable_Object = MibTable
hwCppsAtmPvcTable = _HwCppsAtmPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4)
)
if mibBuilder.loadTexts:
    hwCppsAtmPvcTable.setStatus("current")
_HwCppsAtmPvcEntry_Object = MibTableRow
hwCppsAtmPvcEntry = _HwCppsAtmPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1)
)
hwCppsAtmPvcEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsAtmIfIndex"),
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsAtmVpi"),
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsAtmVci"),
)
if mibBuilder.loadTexts:
    hwCppsAtmPvcEntry.setStatus("current")
_HwCppsAtmIfIndex_Type = InterfaceIndex
_HwCppsAtmIfIndex_Object = MibTableColumn
hwCppsAtmIfIndex = _HwCppsAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1, 1),
    _HwCppsAtmIfIndex_Type()
)
hwCppsAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsAtmIfIndex.setStatus("current")
_HwCppsAtmVpi_Type = AtmVpIdentifier
_HwCppsAtmVpi_Object = MibTableColumn
hwCppsAtmVpi = _HwCppsAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1, 2),
    _HwCppsAtmVpi_Type()
)
hwCppsAtmVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsAtmVpi.setStatus("current")
_HwCppsAtmVci_Type = AtmVcIdentifier
_HwCppsAtmVci_Object = MibTableColumn
hwCppsAtmVci = _HwCppsAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1, 3),
    _HwCppsAtmVci_Type()
)
hwCppsAtmVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsAtmVci.setStatus("current")
_HwCppsAtmPvcPktStatisic_Type = Counter64
_HwCppsAtmPvcPktStatisic_Object = MibTableColumn
hwCppsAtmPvcPktStatisic = _HwCppsAtmPvcPktStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1, 4),
    _HwCppsAtmPvcPktStatisic_Type()
)
hwCppsAtmPvcPktStatisic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCppsAtmPvcPktStatisic.setStatus("current")
_HwCppsAtmPvcByteStatisic_Type = Counter64
_HwCppsAtmPvcByteStatisic_Object = MibTableColumn
hwCppsAtmPvcByteStatisic = _HwCppsAtmPvcByteStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1, 5),
    _HwCppsAtmPvcByteStatisic_Type()
)
hwCppsAtmPvcByteStatisic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCppsAtmPvcByteStatisic.setStatus("current")


class _HwCppsResetAtmPvcStatisic_Type(Integer32):
    """Custom type hwCppsResetAtmPvcStatisic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_HwCppsResetAtmPvcStatisic_Type.__name__ = "Integer32"
_HwCppsResetAtmPvcStatisic_Object = MibTableColumn
hwCppsResetAtmPvcStatisic = _HwCppsResetAtmPvcStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 4, 1, 6),
    _HwCppsResetAtmPvcStatisic_Type()
)
hwCppsResetAtmPvcStatisic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCppsResetAtmPvcStatisic.setStatus("current")
_HwCppsPortVlanTable_Object = MibTable
hwCppsPortVlanTable = _HwCppsPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5)
)
if mibBuilder.loadTexts:
    hwCppsPortVlanTable.setStatus("current")
_HwCppsPortVlanEntry_Object = MibTableRow
hwCppsPortVlanEntry = _HwCppsPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5, 1)
)
hwCppsPortVlanEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsPortIndex"),
    (0, "HUAWEI-IF-EXT-MIB", "hwCppsVlanId"),
)
if mibBuilder.loadTexts:
    hwCppsPortVlanEntry.setStatus("current")
_HwCppsPortIndex_Type = InterfaceIndex
_HwCppsPortIndex_Object = MibTableColumn
hwCppsPortIndex = _HwCppsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5, 1, 1),
    _HwCppsPortIndex_Type()
)
hwCppsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsPortIndex.setStatus("current")
_HwCppsVlanId_Type = VlanIdOrNone
_HwCppsVlanId_Object = MibTableColumn
hwCppsVlanId = _HwCppsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5, 1, 2),
    _HwCppsVlanId_Type()
)
hwCppsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCppsVlanId.setStatus("current")
_HwCppsPortVlanPktStatisic_Type = Counter64
_HwCppsPortVlanPktStatisic_Object = MibTableColumn
hwCppsPortVlanPktStatisic = _HwCppsPortVlanPktStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5, 1, 3),
    _HwCppsPortVlanPktStatisic_Type()
)
hwCppsPortVlanPktStatisic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCppsPortVlanPktStatisic.setStatus("current")
_HwCppsPortVlanByteStatisic_Type = Counter64
_HwCppsPortVlanByteStatisic_Object = MibTableColumn
hwCppsPortVlanByteStatisic = _HwCppsPortVlanByteStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5, 1, 4),
    _HwCppsPortVlanByteStatisic_Type()
)
hwCppsPortVlanByteStatisic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCppsPortVlanByteStatisic.setStatus("current")


class _HwCppsResetPortVlanStatisic_Type(Integer32):
    """Custom type hwCppsResetPortVlanStatisic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_HwCppsResetPortVlanStatisic_Type.__name__ = "Integer32"
_HwCppsResetPortVlanStatisic_Object = MibTableColumn
hwCppsResetPortVlanStatisic = _HwCppsResetPortVlanStatisic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 14, 5, 1, 5),
    _HwCppsResetPortVlanStatisic_Type()
)
hwCppsResetPortVlanStatisic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCppsResetPortVlanStatisic.setStatus("current")
_HwPortIsolationGroupAttrib_ObjectIdentity = ObjectIdentity
hwPortIsolationGroupAttrib = _HwPortIsolationGroupAttrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 15)
)
_HwPortIsolationGroupTable_Object = MibTable
hwPortIsolationGroupTable = _HwPortIsolationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 15, 1)
)
if mibBuilder.loadTexts:
    hwPortIsolationGroupTable.setStatus("current")
_HwPortIsolationGroupEntry_Object = MibTableRow
hwPortIsolationGroupEntry = _HwPortIsolationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 15, 1, 1)
)
hwPortIsolationGroupEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwPortIsolationGroupIndex"),
)
if mibBuilder.loadTexts:
    hwPortIsolationGroupEntry.setStatus("current")


class _HwPortIsolationGroupIndex_Type(Integer32):
    """Custom type hwPortIsolationGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwPortIsolationGroupIndex_Type.__name__ = "Integer32"
_HwPortIsolationGroupIndex_Object = MibTableColumn
hwPortIsolationGroupIndex = _HwPortIsolationGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 15, 1, 1, 1),
    _HwPortIsolationGroupIndex_Type()
)
hwPortIsolationGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortIsolationGroupIndex.setStatus("current")
_HwPortIsolationGroupPortList_Type = PortList
_HwPortIsolationGroupPortList_Object = MibTableColumn
hwPortIsolationGroupPortList = _HwPortIsolationGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 15, 1, 1, 2),
    _HwPortIsolationGroupPortList_Type()
)
hwPortIsolationGroupPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortIsolationGroupPortList.setStatus("current")
_HwPortIsolationGroupRowStatus_Type = RowStatus
_HwPortIsolationGroupRowStatus_Object = MibTableColumn
hwPortIsolationGroupRowStatus = _HwPortIsolationGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 15, 1, 1, 3),
    _HwPortIsolationGroupRowStatus_Type()
)
hwPortIsolationGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortIsolationGroupRowStatus.setStatus("current")
_HwVTrunkAttr_ObjectIdentity = ObjectIdentity
hwVTrunkAttr = _HwVTrunkAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16)
)
_HwVTrunkIfTable_Object = MibTable
hwVTrunkIfTable = _HwVTrunkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16, 1)
)
if mibBuilder.loadTexts:
    hwVTrunkIfTable.setStatus("current")
_HwVTrunkIfEntry_Object = MibTableRow
hwVTrunkIfEntry = _HwVTrunkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16, 1, 1)
)
hwVTrunkIfEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwVTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    hwVTrunkIfEntry.setStatus("current")
_HwVTrunkIfIndex_Type = InterfaceIndex
_HwVTrunkIfIndex_Object = MibTableColumn
hwVTrunkIfIndex = _HwVTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16, 1, 1, 1),
    _HwVTrunkIfIndex_Type()
)
hwVTrunkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVTrunkIfIndex.setStatus("current")


class _HwVTrunkIfID_Type(Integer32):
    """Custom type hwVTrunkIfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_HwVTrunkIfID_Type.__name__ = "Integer32"
_HwVTrunkIfID_Object = MibTableColumn
hwVTrunkIfID = _HwVTrunkIfID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16, 1, 1, 2),
    _HwVTrunkIfID_Type()
)
hwVTrunkIfID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVTrunkIfID.setStatus("current")


class _HwVTrunkIfType_Type(Integer32):
    """Custom type hwVTrunkIfType based on Integer32"""
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
        *(("atm-Trunk", 3),
          ("atm-bundle", 4),
          ("cpos-Trunk", 2),
          ("pos-Trunk", 1))
    )


_HwVTrunkIfType_Type.__name__ = "Integer32"
_HwVTrunkIfType_Object = MibTableColumn
hwVTrunkIfType = _HwVTrunkIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16, 1, 1, 3),
    _HwVTrunkIfType_Type()
)
hwVTrunkIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVTrunkIfType.setStatus("current")
_HwVTrunkIfRowStatus_Type = RowStatus
_HwVTrunkIfRowStatus_Object = MibTableColumn
hwVTrunkIfRowStatus = _HwVTrunkIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 16, 1, 1, 50),
    _HwVTrunkIfRowStatus_Type()
)
hwVTrunkIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVTrunkIfRowStatus.setStatus("current")
_HwVTrunkMemAttr_ObjectIdentity = ObjectIdentity
hwVTrunkMemAttr = _HwVTrunkMemAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17)
)
_HwVTrunkMemTable_Object = MibTable
hwVTrunkMemTable = _HwVTrunkMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1)
)
if mibBuilder.loadTexts:
    hwVTrunkMemTable.setStatus("current")
_HwVTrunkMemEntry_Object = MibTableRow
hwVTrunkMemEntry = _HwVTrunkMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1)
)
hwVTrunkMemEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwVTrunkMemIfIndex"),
)
if mibBuilder.loadTexts:
    hwVTrunkMemEntry.setStatus("current")
_HwVTrunkMemIfIndex_Type = Integer32
_HwVTrunkMemIfIndex_Object = MibTableColumn
hwVTrunkMemIfIndex = _HwVTrunkMemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1, 1),
    _HwVTrunkMemIfIndex_Type()
)
hwVTrunkMemIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVTrunkMemIfIndex.setStatus("current")
_HwVTrunkIfnetIndex_Type = Integer32
_HwVTrunkIfnetIndex_Object = MibTableColumn
hwVTrunkIfnetIndex = _HwVTrunkIfnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1, 2),
    _HwVTrunkIfnetIndex_Type()
)
hwVTrunkIfnetIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVTrunkIfnetIndex.setStatus("current")


class _HwVTrunkValidEntry_Type(Integer32):
    """Custom type hwVTrunkValidEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwVTrunkValidEntry_Type.__name__ = "Integer32"
_HwVTrunkValidEntry_Object = MibTableColumn
hwVTrunkValidEntry = _HwVTrunkValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1, 3),
    _HwVTrunkValidEntry_Type()
)
hwVTrunkValidEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVTrunkValidEntry.setStatus("current")


class _HwVTrunkOperstatus_Type(Integer32):
    """Custom type hwVTrunkOperstatus based on Integer32"""
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


_HwVTrunkOperstatus_Type.__name__ = "Integer32"
_HwVTrunkOperstatus_Object = MibTableColumn
hwVTrunkOperstatus = _HwVTrunkOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1, 4),
    _HwVTrunkOperstatus_Type()
)
hwVTrunkOperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVTrunkOperstatus.setStatus("current")


class _HwVTrunkPortActive_Type(Integer32):
    """Custom type hwVTrunkPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portActive", 2),
          ("portInactive", 1))
    )


_HwVTrunkPortActive_Type.__name__ = "Integer32"
_HwVTrunkPortActive_Object = MibTableColumn
hwVTrunkPortActive = _HwVTrunkPortActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1, 5),
    _HwVTrunkPortActive_Type()
)
hwVTrunkPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVTrunkPortActive.setStatus("current")
_HwVTrunkRowStatus_Type = RowStatus
_HwVTrunkRowStatus_Object = MibTableColumn
hwVTrunkRowStatus = _HwVTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 17, 1, 1, 50),
    _HwVTrunkRowStatus_Type()
)
hwVTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVTrunkRowStatus.setStatus("current")
_HwMasterBackupTrunkSubinterfaceAttr_ObjectIdentity = ObjectIdentity
hwMasterBackupTrunkSubinterfaceAttr = _HwMasterBackupTrunkSubinterfaceAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18)
)
_HwMasterBackupTrunkSubinterfaceTable_Object = MibTable
hwMasterBackupTrunkSubinterfaceTable = _HwMasterBackupTrunkSubinterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1)
)
if mibBuilder.loadTexts:
    hwMasterBackupTrunkSubinterfaceTable.setStatus("current")
_HwMasterBackupTrunkSubinterfaceEntry_Object = MibTableRow
hwMasterBackupTrunkSubinterfaceEntry = _HwMasterBackupTrunkSubinterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1, 1)
)
hwMasterBackupTrunkSubinterfaceEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwBackupTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    hwMasterBackupTrunkSubinterfaceEntry.setStatus("current")
_HwBackupTrunkIfIndex_Type = InterfaceIndex
_HwBackupTrunkIfIndex_Object = MibTableColumn
hwBackupTrunkIfIndex = _HwBackupTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1, 1, 1),
    _HwBackupTrunkIfIndex_Type()
)
hwBackupTrunkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBackupTrunkIfIndex.setStatus("current")


class _HwBackupStatus_Type(Integer32):
    """Custom type hwBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("init", 1),
          ("master", 2))
    )


_HwBackupStatus_Type.__name__ = "Integer32"
_HwBackupStatus_Object = MibTableColumn
hwBackupStatus = _HwBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1, 1, 2),
    _HwBackupStatus_Type()
)
hwBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupStatus.setStatus("current")


class _HwRevertiveMode_Type(Integer32):
    """Custom type hwRevertiveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-revertive", 2),
          ("revertive", 1))
    )


_HwRevertiveMode_Type.__name__ = "Integer32"
_HwRevertiveMode_Object = MibTableColumn
hwRevertiveMode = _HwRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1, 1, 3),
    _HwRevertiveMode_Type()
)
hwRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRevertiveMode.setStatus("current")


class _HwWtrTime_Type(Integer32):
    """Custom type hwWtrTime based on Integer32"""
    defaultValue = 0


_HwWtrTime_Object = MibTableColumn
hwWtrTime = _HwWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1, 1, 4),
    _HwWtrTime_Type()
)
hwWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWtrTime.setStatus("current")


class _HwFlushVlanId_Type(VlanIdOrNone):
    """Custom type hwFlushVlanId based on VlanIdOrNone"""
    defaultValue = 0


_HwFlushVlanId_Object = MibTableColumn
hwFlushVlanId = _HwFlushVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 18, 1, 1, 5),
    _HwFlushVlanId_Type()
)
hwFlushVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFlushVlanId.setStatus("current")
_HwVaspPort_ObjectIdentity = ObjectIdentity
hwVaspPort = _HwVaspPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 19)
)
_HwVaspPortPeerMacTable_Object = MibTable
hwVaspPortPeerMacTable = _HwVaspPortPeerMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 19, 1)
)
if mibBuilder.loadTexts:
    hwVaspPortPeerMacTable.setStatus("current")
_HwVaspPortPeerMacEntry_Object = MibTableRow
hwVaspPortPeerMacEntry = _HwVaspPortPeerMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 19, 1, 1)
)
hwVaspPortPeerMacEntry.setIndexNames(
    (0, "HUAWEI-IF-EXT-MIB", "hwVaspPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwVaspPortPeerMacEntry.setStatus("current")
_HwVaspPortIfIndex_Type = InterfaceIndex
_HwVaspPortIfIndex_Object = MibTableColumn
hwVaspPortIfIndex = _HwVaspPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 19, 1, 1, 1),
    _HwVaspPortIfIndex_Type()
)
hwVaspPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVaspPortIfIndex.setStatus("current")
_HwVaspPortName_Type = DisplayString
_HwVaspPortName_Object = MibTableColumn
hwVaspPortName = _HwVaspPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 19, 1, 1, 2),
    _HwVaspPortName_Type()
)
hwVaspPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVaspPortName.setStatus("current")
_HwVaspPortPeerMac_Type = PhysAddress
_HwVaspPortPeerMac_Object = MibTableColumn
hwVaspPortPeerMac = _HwVaspPortPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 19, 1, 1, 3),
    _HwVaspPortPeerMac_Type()
)
hwVaspPortPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVaspPortPeerMac.setStatus("current")
_HwIFExtTrapObjects_ObjectIdentity = ObjectIdentity
hwIFExtTrapObjects = _HwIFExtTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 20)
)


class _HwLinkDownReason_Type(Integer32):
    """Custom type hwLinkDownReason based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 16),
          ("adminup", 18),
          ("bfdSessionDown", 26),
          ("bfdSessionUp", 27),
          ("chapAuthenticationFailed", 10),
          ("conditionsForActivationAreMet", 23),
          ("conditionsForActivationNotMet", 22),
          ("dldpIsDown", 30),
          ("dldpIsUp", 31),
          ("efmSessionFailed", 14),
          ("efmSessionUp", 28),
          ("interfaceIsDeleted", 25),
          ("keepaliveOutOfTime", 12),
          ("lacpNegotiationFailed", 2),
          ("mainifdown", 20),
          ("papAuthenticationFailed", 11),
          ("physicalLinkDown", 1),
          ("physicalLinkIsUp", 21),
          ("portAlarmDown", 29),
          ("protocoldown", 17),
          ("protocolup", 19),
          ("pvcDown", 13),
          ("receiveCodeRejPacket", 8),
          ("receiveConfAckPacket", 4),
          ("receiveConfReqPacket", 3),
          ("receiveNakPacket", 5),
          ("receiveProtoRejPacket", 9),
          ("receiveTermAckPacket", 7),
          ("receiveTermPacket", 6),
          ("tunnelDownOrInexist", 15),
          ("tunnelIsUp", 24),
          ("vrrpFlowDown", 32),
          ("vrrpFlowUp", 33))
    )


_HwLinkDownReason_Type.__name__ = "Integer32"
_HwLinkDownReason_Object = MibScalar
hwLinkDownReason = _HwLinkDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 20, 1),
    _HwLinkDownReason_Type()
)
hwLinkDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLinkDownReason.setStatus("current")
_HwMainIfName_Type = DisplayString
_HwMainIfName_Object = MibScalar
hwMainIfName = _HwMainIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 20, 2),
    _HwMainIfName_Type()
)
hwMainIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMainIfName.setStatus("current")
_HwCfmOverPhysicalName_Type = DisplayString
_HwCfmOverPhysicalName_Object = MibScalar
hwCfmOverPhysicalName = _HwCfmOverPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 1, 20, 3),
    _HwCfmOverPhysicalName_Type()
)
hwCfmOverPhysicalName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfmOverPhysicalName.setStatus("current")
_HwIFExtConformance_ObjectIdentity = ObjectIdentity
hwIFExtConformance = _HwIFExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2)
)
_HwIFExtGroups_ObjectIdentity = ObjectIdentity
hwIFExtGroups = _HwIFExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1)
)
_HwIFExtCompliances_ObjectIdentity = ObjectIdentity
hwIFExtCompliances = _HwIFExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 2)
)
_HwIFExtTraps_ObjectIdentity = ObjectIdentity
hwIFExtTraps = _HwIFExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3)
)
_HwMonitorNotifications_ObjectIdentity = ObjectIdentity
hwMonitorNotifications = _HwMonitorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4)
)
_HwIFExtTrapConformance_ObjectIdentity = ObjectIdentity
hwIFExtTrapConformance = _HwIFExtTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 5)
)
_HwIFExtTrapGroups_ObjectIdentity = ObjectIdentity
hwIFExtTrapGroups = _HwIFExtTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 5, 1)
)
_HwIFIpNotifications_ObjectIdentity = ObjectIdentity
hwIFIpNotifications = _HwIFIpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 6)
)

# Managed Objects groups

hwTrunkIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 1)
)
hwTrunkIfGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIFExtPhyStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtMemberOf"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfMax"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkNextIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfType"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfModel"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfBandWidthAffectLinkNum"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfMinLinkNum"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfRowStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfWorkingMode"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfWorkingState"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfAutoRecover"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfPreemptEnable"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfPreemptDelay"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfTimeoutReceive"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkBandwidth"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfFlushSendEnable"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfFlushVlanId"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfFlushPasswd"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfForceSwitchEnable"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfStatReset"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfLagSelectedPortStd"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfLagMaxActiveLinkNum"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkETrunkPriority"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkETrunkSysID"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkETrunkPriorityReset"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkETrunkSysIDReset"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkLocalPrefMode"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfTrackVrrpVrid"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfTrackVrrpIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfTrackVrrpReset"))
)
if mibBuilder.loadTexts:
    hwTrunkIfGroup.setStatus("current")

hwIfIpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 2)
)
hwIfIpAddressGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIpAdEntAddr"),
        ("HUAWEI-IF-EXT-MIB", "hwIpAdEntIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwIpAdEntNetMask"),
        ("HUAWEI-IF-EXT-MIB", "hwIpAdEntBcastAddr"),
        ("HUAWEI-IF-EXT-MIB", "hwIpAdEntReasmMaxSize"),
        ("HUAWEI-IF-EXT-MIB", "hwIpAdEntAddressType"),
        ("HUAWEI-IF-EXT-MIB", "hwIfIpMethod"),
        ("HUAWEI-IF-EXT-MIB", "hwIpAdEntAddrStatus"))
)
if mibBuilder.loadTexts:
    hwIfIpAddressGroup.setStatus("current")

hwIFExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 3)
)
hwIFExtGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIFExtLayer"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFrameType"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlowStatInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlushReceiveEnable"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlushVlanId"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlushPasswd"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkSystemPriority"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkUnknownUnicastIfModel"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkETrunkSystemPriority"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkETrunkSystemID"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlowStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtMtu"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtMacAddr"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtBlockPriority"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtMacShift"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtSuppressStatus"))
)
if mibBuilder.loadTexts:
    hwIFExtGroup.setStatus("current")

hwTrunkMemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 4)
)
hwTrunkMemGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkMemifIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkValidEntry"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkSelectStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkLacpStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkDeleteFlag"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkOperstatus"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIsDefaultLagRecv"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkPortWeight"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkPortStandby"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkPortMaster"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkPortPriority"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkPortStatReset"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkRowStatus"))
)
if mibBuilder.loadTexts:
    hwTrunkMemGroup.setStatus("current")

hwIFFlowStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 5)
)
hwIFFlowStatGroup.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwIFFlowStatGlobalInterval")
)
if mibBuilder.loadTexts:
    hwIFFlowStatGroup.setStatus("current")

hwAdminVrrpMemberIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 6)
)
hwAdminVrrpMemberIfGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfFlowChangeTime"),
        ("HUAWEI-IF-EXT-MIB", "hwAdminVrrpVrid"),
        ("HUAWEI-IF-EXT-MIB", "hwAdminVrrpIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwAdminVrrpMemberIfFlowStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwAdminVrrpMemberIfRowStatus"))
)
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfGroup.setStatus("obsolete")

hwIfEtherStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 7)
)
hwIfEtherStatGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPkts64Octets"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPkts65to127Octets"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPkts128to255Octets"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPkts256to511Octets"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPkts512to1023Octets"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPkts1024to1518Octets"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInJumboPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInCRCPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInLongPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInJabberPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInFragmentPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInUnderSizePkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInOverRunPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInPausePkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutJumboPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutOverflowPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutUnderRunPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutPausePkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEthIfStatReset"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInDropEventPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInAlignmentPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInSymbolPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInIgnoredPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatInFramePkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutCollisionPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutDeferredPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutLateCollisionPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutExcessiveCollisionPkts"),
        ("HUAWEI-IF-EXT-MIB", "hwIfEtherStatOutBufferPurgationPkts"))
)
if mibBuilder.loadTexts:
    hwIfEtherStatGroup.setStatus("current")

hwIfMonitorThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 8)
)
hwIfMonitorThresholdGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRatePercentage"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRateThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRatePercentage"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRateThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorDelayValue"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorDelayThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorJitterValue"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorJitterThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorInterval"))
)
if mibBuilder.loadTexts:
    hwIfMonitorThresholdGroup.setStatus("current")

hwIfMonitorGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 9)
)
hwIfMonitorGeneralGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRateEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRateEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorHalfDuplexEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseRisingEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseContinuingEnabledStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwifMonitorBadBytesEnabledStatus"))
)
if mibBuilder.loadTexts:
    hwIfMonitorGeneralGroup.setStatus("current")

hwIfFluxLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 10)
)
hwIfFluxLimitGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfFluxDirection"),
        ("HUAWEI-IF-EXT-MIB", "hwIfFluxLimitType"),
        ("HUAWEI-IF-EXT-MIB", "hwIfFluxCir"),
        ("HUAWEI-IF-EXT-MIB", "hwIfFluxCbs"),
        ("HUAWEI-IF-EXT-MIB", "hwIfFluxRowStatus"))
)
if mibBuilder.loadTexts:
    hwIfFluxLimitGroup.setStatus("current")

hwIfDiffServGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 11)
)
hwIfDiffServGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfDiffServMode"),
        ("HUAWEI-IF-EXT-MIB", "hwIfDiffServServiceClass"),
        ("HUAWEI-IF-EXT-MIB", "hwIfDiffServColor"))
)
if mibBuilder.loadTexts:
    hwIfDiffServGroup.setStatus("current")

hwIfQueryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 12)
)
hwIfQueryGroup.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwIfIndex")
)
if mibBuilder.loadTexts:
    hwIfQueryGroup.setStatus("current")

hwLogicIfAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 13)
)
hwLogicIfAttrGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwLogicIfMainIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfType"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfName"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfParaOne"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfRowStatus"))
)
if mibBuilder.loadTexts:
    hwLogicIfAttrGroup.setStatus("current")

hwIfIpUnnumberedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 14)
)
hwIfIpUnnumberedGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwLendIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwLendIpAddr"),
        ("HUAWEI-IF-EXT-MIB", "hwLendIpAddrNetMask"),
        ("HUAWEI-IF-EXT-MIB", "hwUnnumberedRowStatus"))
)
if mibBuilder.loadTexts:
    hwIfIpUnnumberedGroup.setStatus("current")

hwLinkModeChangeAutoCreateIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 15)
)
hwLinkModeChangeAutoCreateIfGroup.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwNewIfTimeslot")
)
if mibBuilder.loadTexts:
    hwLinkModeChangeAutoCreateIfGroup.setStatus("current")

hwCppsGlobalEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 16)
)
hwCppsGlobalEnableGroup.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwCppsGlobalEnable")
)
if mibBuilder.loadTexts:
    hwCppsGlobalEnableGroup.setStatus("current")

hwCppsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 17)
)
hwCppsInterfaceGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwCppsPortPvcEnable"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsPortVlanEnable"))
)
if mibBuilder.loadTexts:
    hwCppsInterfaceGroup.setStatus("current")

hwCppsIfStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 18)
)
hwCppsIfStatisticsGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwCppsInterfacePktStatisic"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsInterfaceByteStatisic"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsResetInterfaceStatisic"))
)
if mibBuilder.loadTexts:
    hwCppsIfStatisticsGroup.setStatus("current")

hwCppsAtmPvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 19)
)
hwCppsAtmPvcGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwCppsAtmPvcPktStatisic"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsAtmPvcByteStatisic"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsResetAtmPvcStatisic"))
)
if mibBuilder.loadTexts:
    hwCppsAtmPvcGroup.setStatus("current")

hwCppsPortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 20)
)
hwCppsPortVlanGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwCppsPortVlanPktStatisic"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsPortVlanByteStatisic"),
        ("HUAWEI-IF-EXT-MIB", "hwCppsResetPortVlanStatisic"))
)
if mibBuilder.loadTexts:
    hwCppsPortVlanGroup.setStatus("current")

hwPortIsolationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 21)
)
hwPortIsolationGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwPortIsolationGroupPortList"),
        ("HUAWEI-IF-EXT-MIB", "hwPortIsolationGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwPortIsolationGroup.setStatus("current")

hwVTrunkIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 22)
)
hwVTrunkIfGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwVTrunkIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkIfID"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkIfType"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkIfRowStatus"))
)
if mibBuilder.loadTexts:
    hwVTrunkIfGroup.setStatus("current")

hwVTrunkMemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 23)
)
hwVTrunkMemGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwVTrunkMemIfIndex"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkValidEntry"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkOperstatus"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkPortActive"),
        ("HUAWEI-IF-EXT-MIB", "hwVTrunkRowStatus"))
)
if mibBuilder.loadTexts:
    hwVTrunkMemGroup.setStatus("current")

hwLogicIfHelpTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 24)
)
hwLogicIfHelpTableGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwLogicIfhelpType"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfChassisNumber"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfSlotNumber"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfCardNumber"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfMin"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfMax"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicIfTotal"))
)
if mibBuilder.loadTexts:
    hwLogicIfHelpTableGroup.setStatus("current")

hwSubInterfaceBackupTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 25)
)
hwSubInterfaceBackupTrunkGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwBackupStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwRevertiveMode"),
        ("HUAWEI-IF-EXT-MIB", "hwWtrTime"),
        ("HUAWEI-IF-EXT-MIB", "hwFlushVlanId"))
)
if mibBuilder.loadTexts:
    hwSubInterfaceBackupTrunkGroup.setStatus("current")

hwVaspPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 26)
)
hwVaspPortGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwVaspPortName"),
        ("HUAWEI-IF-EXT-MIB", "hwVaspPortPeerMac"))
)
if mibBuilder.loadTexts:
    hwVaspPortGroup.setStatus("current")

hwLogicIfDynamicHelpTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 1, 27)
)
hwLogicIfDynamicHelpTableGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfhelpType"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfChassisNumber"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfSlotNumber"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfCardNumber"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfMin"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfMax"),
        ("HUAWEI-IF-EXT-MIB", "hwLogicDynamicIfTotal"))
)
if mibBuilder.loadTexts:
    hwLogicIfDynamicHelpTableGroup.setStatus("current")


# Notification objects

hwTrunkWorkingSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 1)
)
hwTrunkWorkingSwitch.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("HUAWEI-IF-EXT-MIB", "hwTrunkIfWorkingState"))
)
if mibBuilder.loadTexts:
    hwTrunkWorkingSwitch.setStatus(
        "current"
    )

hwLacpNegotiateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 2)
)
hwLacpNegotiateFailed.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwLacpNegotiateFailed.setStatus(
        "current"
    )

hwLacpTotalLinkLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 3)
)
hwLacpTotalLinkLoss.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwLacpTotalLinkLoss.setStatus(
        "current"
    )

hwLacpPartialLinkLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 4)
)
hwLacpPartialLinkLoss.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwLacpPartialLinkLoss.setStatus(
        "current"
    )

hwIfFlowDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 5)
)
hwIfFlowDown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlowStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwIfFlowDown.setStatus(
        "current"
    )

hwIfFlowUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 6)
)
hwIfFlowUp.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtFlowStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwIfFlowUp.setStatus(
        "current"
    )

hwIfNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 7)
)
if mibBuilder.loadTexts:
    hwIfNameChange.setStatus(
        "current"
    )

hwIfNameChangeResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 8)
)
if mibBuilder.loadTexts:
    hwIfNameChangeResume.setStatus(
        "current"
    )

hwExtLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 9)
)
hwExtLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifDescr"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtPhyStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtMemberOf"))
)
if mibBuilder.loadTexts:
    hwExtLinkDown.setStatus(
        "deprecated"
    )

hwExtLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 10)
)
hwExtLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifDescr"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtPhyStatus"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtMemberOf"))
)
if mibBuilder.loadTexts:
    hwExtLinkUp.setStatus(
        "deprecated"
    )

hwLoopbackBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 11)
)
hwLoopbackBlock.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwIfName")
)
if mibBuilder.loadTexts:
    hwLoopbackBlock.setStatus(
        "current"
    )

hwLoopbackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 12)
)
hwLoopbackResume.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwIfName")
)
if mibBuilder.loadTexts:
    hwLoopbackResume.setStatus(
        "current"
    )

hwLacpNegotiateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 13)
)
hwLacpNegotiateResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwLacpNegotiateResume.setStatus(
        "current"
    )

hwLacpTotalLinkLossResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 14)
)
hwLacpTotalLinkLossResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwLacpTotalLinkLossResume.setStatus(
        "current"
    )

hwLacpPartialLinkLossResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 15)
)
hwLacpPartialLinkLossResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkIfID"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwLacpPartialLinkLossResume.setStatus(
        "current"
    )

hwTrunkSubIfStateToMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 24)
)
hwTrunkSubIfStateToMaster.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfName"),
        ("HUAWEI-IF-EXT-MIB", "hwBackupStatus"))
)
if mibBuilder.loadTexts:
    hwTrunkSubIfStateToMaster.setStatus(
        "current"
    )

hwTrunkSubIfStateToSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 25)
)
hwTrunkSubIfStateToSlave.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfName"),
        ("HUAWEI-IF-EXT-MIB", "hwBackupStatus"))
)
if mibBuilder.loadTexts:
    hwTrunkSubIfStateToSlave.setStatus(
        "current"
    )

hwEntityExtCfmOverSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 26)
)
hwEntityExtCfmOverSlot.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwCfmOverPhysicalName")
)
if mibBuilder.loadTexts:
    hwEntityExtCfmOverSlot.setStatus(
        "current"
    )

hwEntityExtCfmOverCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 27)
)
hwEntityExtCfmOverCard.setObjects(
    ("HUAWEI-IF-EXT-MIB", "hwCfmOverPhysicalName")
)
if mibBuilder.loadTexts:
    hwEntityExtCfmOverCard.setStatus(
        "current"
    )

hwExtAllMemberDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 28)
)
hwExtAllMemberDownNotify.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwExtAllMemberDownNotify.setStatus(
        "current"
    )

hwExtAllMemberDownResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 29)
)
hwExtAllMemberDownResume.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwExtAllMemberDownResume.setStatus(
        "current"
    )

hwIfControlFlapSuppress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 31)
)
hwIfControlFlapSuppress.setObjects(
      *(("IF-MIB", "ifName"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtSuppressStatus"))
)
if mibBuilder.loadTexts:
    hwIfControlFlapSuppress.setStatus(
        "current"
    )

hwIfControlFlapResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 32)
)
hwIfControlFlapResume.setObjects(
      *(("IF-MIB", "ifName"),
        ("HUAWEI-IF-EXT-MIB", "hwIFExtSuppressStatus"))
)
if mibBuilder.loadTexts:
    hwIfControlFlapResume.setStatus(
        "current"
    )

hwExtInterfaceDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 3, 33)
)
hwExtInterfaceDelete.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hwExtInterfaceDelete.setStatus(
        "current"
    )

hwIfMonitorCrcErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 1)
)
hwIfMonitorCrcErrorRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorCrcErrorRising.setStatus(
        "current"
    )

hwIfMonitorCrcErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 2)
)
hwIfMonitorCrcErrorResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorCrcErrorResume.setStatus(
        "current"
    )

hwIfMonitorSdhErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 3)
)
hwIfMonitorSdhErrorRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSdhErrorRising.setStatus(
        "current"
    )

hwIfMonitorSdhErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 4)
)
hwIfMonitorSdhErrorResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSdhErrorResume.setStatus(
        "current"
    )

hwIfMonitorInputRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 5)
)
hwIfMonitorInputRateRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRatePercentage"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRateThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorInputRateRising.setStatus(
        "current"
    )

hwIfMonitorInputRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 6)
)
hwIfMonitorInputRateResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRatePercentage"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRateThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorInputRateResume.setStatus(
        "current"
    )

hwIfMonitorOutputRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 7)
)
hwIfMonitorOutputRateRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRatePercentage"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRateThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorOutputRateRising.setStatus(
        "current"
    )

hwIfMonitorOutputRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 8)
)
hwIfMonitorOutputRateResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRatePercentage"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRateThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorOutputRateResume.setStatus(
        "current"
    )

hwIfMonitorHalfDuplexRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 9)
)
hwIfMonitorHalfDuplexRising.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    hwIfMonitorHalfDuplexRising.setStatus(
        "current"
    )

hwIfMonitorPauseFrameRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 10)
)
hwIfMonitorPauseFrameRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    hwIfMonitorPauseFrameRising.setStatus(
        "current"
    )

hwIfMonitorPauseFrameRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 11)
)
hwIfMonitorPauseFrameRisingResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    hwIfMonitorPauseFrameRisingResume.setStatus(
        "current"
    )

hwIfPortControlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 12)
)
hwIfPortControlUp.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwIfPortControlUp.setStatus(
        "current"
    )

hwIfPortControlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 13)
)
hwIfPortControlDown.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwIfPortControlDown.setStatus(
        "current"
    )

hwIfMonitorSdhB1ErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 14)
)
hwIfMonitorSdhB1ErrorRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSdhB1ErrorRising.setStatus(
        "current"
    )

hwIfMonitorSdhB1ErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 15)
)
hwIfMonitorSdhB1ErrorResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSdhB1ErrorResume.setStatus(
        "current"
    )

hwIfMonitorSdhB2ErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 16)
)
hwIfMonitorSdhB2ErrorRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSdhB2ErrorRising.setStatus(
        "current"
    )

hwIfMonitorSdhB2ErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 17)
)
hwIfMonitorSdhB2ErrorResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSdhB2ErrorResume.setStatus(
        "current"
    )

hwIfMonitorSymbolErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 18)
)
hwIfMonitorSymbolErrorRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSymbolErrorRising.setStatus(
        "current"
    )

hwIfMonitorSymbolErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 19)
)
hwIfMonitorSymbolErrorResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorInterval"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorName"))
)
if mibBuilder.loadTexts:
    hwIfMonitorSymbolErrorResume.setStatus(
        "current"
    )

hwIfMonitorBadBytesErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 40)
)
hwIfMonitorBadBytesErrorRising.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorInterval"))
)
if mibBuilder.loadTexts:
    hwIfMonitorBadBytesErrorRising.setStatus(
        "current"
    )

hwIfMonitorBadBytesErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 4, 41)
)
hwIfMonitorBadBytesErrorResume.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorStatistics"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorThreshold"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorInterval"))
)
if mibBuilder.loadTexts:
    hwIfMonitorBadBytesErrorResume.setStatus(
        "current"
    )

hwIfIpAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 6, 1)
)
hwIfIpAddressChange.setObjects(
      *(("IP-MIB", "ipAdEntNetMask"),
        ("IP-MIB", "ipAdEntNetMask"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwIfIpAddressChange.setStatus(
        "current"
    )


# Notifications groups

hwIFExtTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 5, 1, 1)
)
hwIFExtTrapGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwTrunkWorkingSwitch"),
        ("HUAWEI-IF-EXT-MIB", "hwLacpNegotiateFailed"),
        ("HUAWEI-IF-EXT-MIB", "hwLacpTotalLinkLoss"),
        ("HUAWEI-IF-EXT-MIB", "hwLacpPartialLinkLoss"),
        ("HUAWEI-IF-EXT-MIB", "hwIfFlowDown"),
        ("HUAWEI-IF-EXT-MIB", "hwIfFlowUp"),
        ("HUAWEI-IF-EXT-MIB", "hwIfNameChange"),
        ("HUAWEI-IF-EXT-MIB", "hwIfNameChangeResume"),
        ("HUAWEI-IF-EXT-MIB", "hwExtLinkDown"),
        ("HUAWEI-IF-EXT-MIB", "hwExtLinkUp"),
        ("HUAWEI-IF-EXT-MIB", "hwLoopbackBlock"),
        ("HUAWEI-IF-EXT-MIB", "hwLoopbackResume"),
        ("HUAWEI-IF-EXT-MIB", "hwLacpNegotiateResume"),
        ("HUAWEI-IF-EXT-MIB", "hwLacpTotalLinkLossResume"),
        ("HUAWEI-IF-EXT-MIB", "hwLacpPartialLinkLossResume"),
        ("HUAWEI-IF-EXT-MIB", "hwExtAllMemberDownNotify"),
        ("HUAWEI-IF-EXT-MIB", "hwExtAllMemberDownResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfControlFlapSuppress"),
        ("HUAWEI-IF-EXT-MIB", "hwIfControlFlapResume"),
        ("HUAWEI-IF-EXT-MIB", "hwExtInterfaceDelete"))
)
if mibBuilder.loadTexts:
    hwIFExtTrapGroup.setStatus(
        "current"
    )

hwMonitorTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 5, 1, 2)
)
hwMonitorTrapGroup.setObjects(
      *(("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorCrcErrorResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhErrorResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRateRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorInputRateResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRateRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorOutputRateResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorHalfDuplexRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorPauseFrameRisingResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfPortControlUp"),
        ("HUAWEI-IF-EXT-MIB", "hwIfPortControlDown"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB1ErrorResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSdhB2ErrorResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorSymbolErrorResume"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorRising"),
        ("HUAWEI-IF-EXT-MIB", "hwIfMonitorBadBytesErrorResume"))
)
if mibBuilder.loadTexts:
    hwMonitorTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIFExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 41, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwIFExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IF-EXT-MIB",
    **{"EnabledStatus": EnabledStatus,
       "SnmpPasswdString": SnmpPasswdString,
       "HWDirectionType": HWDirectionType,
       "HwIpAddressType": HwIpAddressType,
       "hwIFExtMib": hwIFExtMib,
       "hwIFExtObjects": hwIFExtObjects,
       "hwIFExtBase": hwIFExtBase,
       "hwIFExtTable": hwIFExtTable,
       "hwIFExtEntry": hwIFExtEntry,
       "hwIFExtIndex": hwIFExtIndex,
       "hwIFExtLayer": hwIFExtLayer,
       "hwIFExtFrameType": hwIFExtFrameType,
       "hwIFExtFlowStatInterval": hwIFExtFlowStatInterval,
       "hwIFExtFlushReceiveEnable": hwIFExtFlushReceiveEnable,
       "hwIFExtFlushVlanId": hwIFExtFlushVlanId,
       "hwIFExtFlushPasswd": hwIFExtFlushPasswd,
       "hwIFExtFlowStatus": hwIFExtFlowStatus,
       "hwIFExtMtu": hwIFExtMtu,
       "hwIFExtMacAddr": hwIFExtMacAddr,
       "hwIFExtBlockPriority": hwIFExtBlockPriority,
       "hwIFExtMacShift": hwIFExtMacShift,
       "hwIFExtSuppressStatus": hwIFExtSuppressStatus,
       "hwIFExtPhyStatus": hwIFExtPhyStatus,
       "hwIFExtMemberOf": hwIFExtMemberOf,
       "hwLinkModeChangeAutoCreateIfTable": hwLinkModeChangeAutoCreateIfTable,
       "hwLinkModeChangeAutoCreateIfEntry": hwLinkModeChangeAutoCreateIfEntry,
       "hwAutoIfIndex": hwAutoIfIndex,
       "hwNewIfTimeslot": hwNewIfTimeslot,
       "hwIFExtPhyNumber": hwIFExtPhyNumber,
       "hwInterfaceIp": hwInterfaceIp,
       "hwIfIpTable": hwIfIpTable,
       "hwIfIpEntry": hwIfIpEntry,
       "hwIpAdEntAddr": hwIpAdEntAddr,
       "hwIpAdEntIfIndex": hwIpAdEntIfIndex,
       "hwIpAdEntNetMask": hwIpAdEntNetMask,
       "hwIpAdEntBcastAddr": hwIpAdEntBcastAddr,
       "hwIpAdEntReasmMaxSize": hwIpAdEntReasmMaxSize,
       "hwIpAdEntAddressType": hwIpAdEntAddressType,
       "hwIfIpMethod": hwIfIpMethod,
       "hwIpAdEntAddrStatus": hwIpAdEntAddrStatus,
       "hwIfIpUnnumberedTable": hwIfIpUnnumberedTable,
       "hwIfIpUnnumberedEntry": hwIfIpUnnumberedEntry,
       "hwUnnumberedIfIndex": hwUnnumberedIfIndex,
       "hwLendIfIndex": hwLendIfIndex,
       "hwLendIpAddr": hwLendIpAddr,
       "hwLendIpAddrNetMask": hwLendIpAddrNetMask,
       "hwUnnumberedRowStatus": hwUnnumberedRowStatus,
       "hwTrunkAttr": hwTrunkAttr,
       "hwTrunkIfMax": hwTrunkIfMax,
       "hwTrunkNextIndex": hwTrunkNextIndex,
       "hwTrunkIfTable": hwTrunkIfTable,
       "hwTrunkIfEntry": hwTrunkIfEntry,
       "hwTrunkIndex": hwTrunkIndex,
       "hwTrunkIfID": hwTrunkIfID,
       "hwTrunkIfType": hwTrunkIfType,
       "hwTrunkIfIndex": hwTrunkIfIndex,
       "hwTrunkIfModel": hwTrunkIfModel,
       "hwTrunkIfBandWidthAffectLinkNum": hwTrunkIfBandWidthAffectLinkNum,
       "hwTrunkIfMinLinkNum": hwTrunkIfMinLinkNum,
       "hwTrunkIfRowStatus": hwTrunkIfRowStatus,
       "hwTrunkIfWorkingMode": hwTrunkIfWorkingMode,
       "hwTrunkIfWorkingState": hwTrunkIfWorkingState,
       "hwTrunkIfAutoRecover": hwTrunkIfAutoRecover,
       "hwTrunkIfPreemptEnable": hwTrunkIfPreemptEnable,
       "hwTrunkIfPreemptDelay": hwTrunkIfPreemptDelay,
       "hwTrunkIfTimeoutReceive": hwTrunkIfTimeoutReceive,
       "hwTrunkIfFlushSendEnable": hwTrunkIfFlushSendEnable,
       "hwTrunkIfFlushVlanId": hwTrunkIfFlushVlanId,
       "hwTrunkIfFlushPasswd": hwTrunkIfFlushPasswd,
       "hwTrunkIfForceSwitchEnable": hwTrunkIfForceSwitchEnable,
       "hwTrunkIfStatReset": hwTrunkIfStatReset,
       "hwTrunkBandwidth": hwTrunkBandwidth,
       "hwTrunkIfArpSendSpeed": hwTrunkIfArpSendSpeed,
       "hwTrunkIfLagSelectedPortStd": hwTrunkIfLagSelectedPortStd,
       "hwTrunkIfLagMaxActiveLinkNum": hwTrunkIfLagMaxActiveLinkNum,
       "hwTrunkETrunkPriority": hwTrunkETrunkPriority,
       "hwTrunkETrunkSysID": hwTrunkETrunkSysID,
       "hwTrunkETrunkPriorityReset": hwTrunkETrunkPriorityReset,
       "hwTrunkETrunkSysIDReset": hwTrunkETrunkSysIDReset,
       "hwTrunkLocalPrefMode": hwTrunkLocalPrefMode,
       "hwTrunkIfTrackVrrpVrid": hwTrunkIfTrackVrrpVrid,
       "hwTrunkIfTrackVrrpIfIndex": hwTrunkIfTrackVrrpIfIndex,
       "hwTrunkIfTrackVrrpReset": hwTrunkIfTrackVrrpReset,
       "hwTrunkIfBackupPreemptEnable": hwTrunkIfBackupPreemptEnable,
       "hwTrunkIfBackupPreemptDelay": hwTrunkIfBackupPreemptDelay,
       "hwTrunkSystemPriority": hwTrunkSystemPriority,
       "hwTrunkUnknownUnicastIfModel": hwTrunkUnknownUnicastIfModel,
       "hwTrunkETrunkSystemPriority": hwTrunkETrunkSystemPriority,
       "hwTrunkETrunkSystemID": hwTrunkETrunkSystemID,
       "hwTrunkMemAttr": hwTrunkMemAttr,
       "hwTrunkMemTable": hwTrunkMemTable,
       "hwTrunkMemEntry": hwTrunkMemEntry,
       "hwTrunkMemifIndex": hwTrunkMemifIndex,
       "hwTrunkValidEntry": hwTrunkValidEntry,
       "hwTrunkSelectStatus": hwTrunkSelectStatus,
       "hwTrunkLacpStatus": hwTrunkLacpStatus,
       "hwTrunkDeleteFlag": hwTrunkDeleteFlag,
       "hwTrunkOperstatus": hwTrunkOperstatus,
       "hwTrunkIsDefaultLagRecv": hwTrunkIsDefaultLagRecv,
       "hwTrunkPortWeight": hwTrunkPortWeight,
       "hwTrunkPortStandby": hwTrunkPortStandby,
       "hwTrunkRowStatus": hwTrunkRowStatus,
       "hwTrunkPortMaster": hwTrunkPortMaster,
       "hwTrunkPortPriority": hwTrunkPortPriority,
       "hwTrunkPortStatReset": hwTrunkPortStatReset,
       "hwIFFlowStat": hwIFFlowStat,
       "hwIFFlowStatGlobalInterval": hwIFFlowStatGlobalInterval,
       "hwIfStatistics": hwIfStatistics,
       "hwIfEtherStatTable": hwIfEtherStatTable,
       "hwIfEtherStatEntry": hwIfEtherStatEntry,
       "hwIfEtherStatIfIndex": hwIfEtherStatIfIndex,
       "hwIfEtherStatInPkts64Octets": hwIfEtherStatInPkts64Octets,
       "hwIfEtherStatInPkts65to127Octets": hwIfEtherStatInPkts65to127Octets,
       "hwIfEtherStatInPkts128to255Octets": hwIfEtherStatInPkts128to255Octets,
       "hwIfEtherStatInPkts256to511Octets": hwIfEtherStatInPkts256to511Octets,
       "hwIfEtherStatInPkts512to1023Octets": hwIfEtherStatInPkts512to1023Octets,
       "hwIfEtherStatInPkts1024to1518Octets": hwIfEtherStatInPkts1024to1518Octets,
       "hwIfEtherStatInJumboPkts": hwIfEtherStatInJumboPkts,
       "hwIfEtherStatInCRCPkts": hwIfEtherStatInCRCPkts,
       "hwIfEtherStatInLongPkts": hwIfEtherStatInLongPkts,
       "hwIfEtherStatInJabberPkts": hwIfEtherStatInJabberPkts,
       "hwIfEtherStatInFragmentPkts": hwIfEtherStatInFragmentPkts,
       "hwIfEtherStatInUnderSizePkts": hwIfEtherStatInUnderSizePkts,
       "hwIfEtherStatInOverRunPkts": hwIfEtherStatInOverRunPkts,
       "hwIfEtherStatInPausePkts": hwIfEtherStatInPausePkts,
       "hwIfEtherStatOutJumboPkts": hwIfEtherStatOutJumboPkts,
       "hwIfEtherStatOutOverflowPkts": hwIfEtherStatOutOverflowPkts,
       "hwIfEtherStatOutUnderRunPkts": hwIfEtherStatOutUnderRunPkts,
       "hwIfEtherStatOutPausePkts": hwIfEtherStatOutPausePkts,
       "hwIfEthIfStatReset": hwIfEthIfStatReset,
       "hwIfEtherStatInDropEventPkts": hwIfEtherStatInDropEventPkts,
       "hwIfEtherStatInAlignmentPkts": hwIfEtherStatInAlignmentPkts,
       "hwIfEtherStatInSymbolPkts": hwIfEtherStatInSymbolPkts,
       "hwIfEtherStatInIgnoredPkts": hwIfEtherStatInIgnoredPkts,
       "hwIfEtherStatInFramePkts": hwIfEtherStatInFramePkts,
       "hwIfEtherStatOutCollisionPkts": hwIfEtherStatOutCollisionPkts,
       "hwIfEtherStatOutDeferredPkts": hwIfEtherStatOutDeferredPkts,
       "hwIfEtherStatOutLateCollisionPkts": hwIfEtherStatOutLateCollisionPkts,
       "hwIfEtherStatOutExcessiveCollisionPkts": hwIfEtherStatOutExcessiveCollisionPkts,
       "hwIfEtherStatOutBufferPurgationPkts": hwIfEtherStatOutBufferPurgationPkts,
       "hwIfSdhStatTable": hwIfSdhStatTable,
       "hwIfSdhStatEntry": hwIfSdhStatEntry,
       "hwIfSdhStatIfIndex": hwIfSdhStatIfIndex,
       "hwIfSdhStatInCRCPkts": hwIfSdhStatInCRCPkts,
       "hwIfSdhStatInShortPkts": hwIfSdhStatInShortPkts,
       "hwIfSdhStatInLongPkts": hwIfSdhStatInLongPkts,
       "hwIfSdhStatOutOverRunPkts": hwIfSdhStatOutOverRunPkts,
       "hwIfSdhStatOutUnderRunPkts": hwIfSdhStatOutUnderRunPkts,
       "hwIfSdhIfStatReset": hwIfSdhIfStatReset,
       "hwIfAtmStatTable": hwIfAtmStatTable,
       "hwIfAtmStatEntry": hwIfAtmStatEntry,
       "hwIfAtmStatIfIndex": hwIfAtmStatIfIndex,
       "hwIfAtmStatInGoodCells": hwIfAtmStatInGoodCells,
       "hwIfAtmStatInIdleCells": hwIfAtmStatInIdleCells,
       "hwIfAtmStatInCorrectedCells": hwIfAtmStatInCorrectedCells,
       "hwIfAtmStatInUncorrectedCells": hwIfAtmStatInUncorrectedCells,
       "hwIfAtmStatOutGoodCells": hwIfAtmStatOutGoodCells,
       "hwIfAtmStatOutIdleCells": hwIfAtmStatOutIdleCells,
       "hwIfAtmIfStatReset": hwIfAtmIfStatReset,
       "hwIfMonitorObject": hwIfMonitorObject,
       "hwIfMonitorThresholdTable": hwIfMonitorThresholdTable,
       "hwIfMonitorThresholdEntry": hwIfMonitorThresholdEntry,
       "hwIfMonitorIndex": hwIfMonitorIndex,
       "hwIfMonitorCrcErrorStatistics": hwIfMonitorCrcErrorStatistics,
       "hwIfMonitorCrcErrorThreshold": hwIfMonitorCrcErrorThreshold,
       "hwIfMonitorCrcErrorInterval": hwIfMonitorCrcErrorInterval,
       "hwIfMonitorSdhErrorStatistics": hwIfMonitorSdhErrorStatistics,
       "hwIfMonitorSdhErrorThreshold": hwIfMonitorSdhErrorThreshold,
       "hwIfMonitorSdhErrorInterval": hwIfMonitorSdhErrorInterval,
       "hwIfMonitorInputRatePercentage": hwIfMonitorInputRatePercentage,
       "hwIfMonitorInputRateThreshold": hwIfMonitorInputRateThreshold,
       "hwIfMonitorOutputRatePercentage": hwIfMonitorOutputRatePercentage,
       "hwIfMonitorOutputRateThreshold": hwIfMonitorOutputRateThreshold,
       "hwIfMonitorPauseFrameStatistics": hwIfMonitorPauseFrameStatistics,
       "hwIfMonitorPauseFrameThreshold": hwIfMonitorPauseFrameThreshold,
       "hwIfMonitorPauseFrameInterval": hwIfMonitorPauseFrameInterval,
       "hwIfMonitorDelayValue": hwIfMonitorDelayValue,
       "hwIfMonitorDelayThreshold": hwIfMonitorDelayThreshold,
       "hwIfMonitorJitterValue": hwIfMonitorJitterValue,
       "hwIfMonitorJitterThreshold": hwIfMonitorJitterThreshold,
       "hwIfMonitorName": hwIfMonitorName,
       "hwIfMonitorSdhB1ErrorStatistics": hwIfMonitorSdhB1ErrorStatistics,
       "hwIfMonitorSdhB1ErrorThreshold": hwIfMonitorSdhB1ErrorThreshold,
       "hwIfMonitorSdhB1ErrorInterval": hwIfMonitorSdhB1ErrorInterval,
       "hwIfMonitorSdhB2ErrorStatistics": hwIfMonitorSdhB2ErrorStatistics,
       "hwIfMonitorSdhB2ErrorThreshold": hwIfMonitorSdhB2ErrorThreshold,
       "hwIfMonitorSdhB2ErrorInterval": hwIfMonitorSdhB2ErrorInterval,
       "hwIfMonitorSymbolErrorStatistics": hwIfMonitorSymbolErrorStatistics,
       "hwIfMonitorSymbolErrorThreshold": hwIfMonitorSymbolErrorThreshold,
       "hwIfMonitorSymbolErrorInterval": hwIfMonitorSymbolErrorInterval,
       "hwIfMonitorBadBytesErrorStatistics": hwIfMonitorBadBytesErrorStatistics,
       "hwIfMonitorBadBytesErrorThreshold": hwIfMonitorBadBytesErrorThreshold,
       "hwIfMonitorBadBytesErrorInterval": hwIfMonitorBadBytesErrorInterval,
       "hwIfMonitorGeneral": hwIfMonitorGeneral,
       "hwIfMonitorCrcEnabledStatus": hwIfMonitorCrcEnabledStatus,
       "hwIfMonitorSdhEnabledStatus": hwIfMonitorSdhEnabledStatus,
       "hwIfMonitorInputRateEnabledStatus": hwIfMonitorInputRateEnabledStatus,
       "hwIfMonitorOutputRateEnabledStatus": hwIfMonitorOutputRateEnabledStatus,
       "hwIfMonitorHalfDuplexEnabledStatus": hwIfMonitorHalfDuplexEnabledStatus,
       "hwIfMonitorPauseRisingEnabledStatus": hwIfMonitorPauseRisingEnabledStatus,
       "hwIfMonitorPauseContinuingEnabledStatus": hwIfMonitorPauseContinuingEnabledStatus,
       "hwifMonitorBadBytesEnabledStatus": hwifMonitorBadBytesEnabledStatus,
       "hwAdminVrrpMemberIf": hwAdminVrrpMemberIf,
       "hwIfFlowChangeTime": hwIfFlowChangeTime,
       "hwAdminVrrpMemberIfTable": hwAdminVrrpMemberIfTable,
       "hwAdminVrrpMemberIfEntry": hwAdminVrrpMemberIfEntry,
       "hwAdminVrrpMemberIfIndex": hwAdminVrrpMemberIfIndex,
       "hwAdminVrrpVrid": hwAdminVrrpVrid,
       "hwAdminVrrpIfIndex": hwAdminVrrpIfIndex,
       "hwAdminVrrpMemberIfFlowStatus": hwAdminVrrpMemberIfFlowStatus,
       "hwAdminVrrpMemberIfRowStatus": hwAdminVrrpMemberIfRowStatus,
       "hwIfFluxLimit": hwIfFluxLimit,
       "hwIfFluxLimitTable": hwIfFluxLimitTable,
       "hwIfFluxLimitEntry": hwIfFluxLimitEntry,
       "hwIfFluxIfIndex": hwIfFluxIfIndex,
       "hwIfFluxVlanId": hwIfFluxVlanId,
       "hwIfFluxDirection": hwIfFluxDirection,
       "hwIfFluxLimitType": hwIfFluxLimitType,
       "hwIfFluxCir": hwIfFluxCir,
       "hwIfFluxCbs": hwIfFluxCbs,
       "hwIfFluxRowStatus": hwIfFluxRowStatus,
       "hwIfDiffServ": hwIfDiffServ,
       "hwIfDiffServTable": hwIfDiffServTable,
       "hwIfDiffServEntry": hwIfDiffServEntry,
       "hwIfDiffServIndex": hwIfDiffServIndex,
       "hwIfDiffServMode": hwIfDiffServMode,
       "hwIfDiffServServiceClass": hwIfDiffServServiceClass,
       "hwIfDiffServColor": hwIfDiffServColor,
       "hwIfQuery": hwIfQuery,
       "hwIfQueryTable": hwIfQueryTable,
       "hwIfQueryEntry": hwIfQueryEntry,
       "hwIfName": hwIfName,
       "hwIfIndex": hwIfIndex,
       "hwLogicIfAttrib": hwLogicIfAttrib,
       "hwLogicIfTable": hwLogicIfTable,
       "hwLogicIfEntry": hwLogicIfEntry,
       "hwLogicIfIndex": hwLogicIfIndex,
       "hwLogicIfMainIndex": hwLogicIfMainIndex,
       "hwLogicIfType": hwLogicIfType,
       "hwLogicIfName": hwLogicIfName,
       "hwLogicIfParaOne": hwLogicIfParaOne,
       "hwLogicIfRowStatus": hwLogicIfRowStatus,
       "hwLogicIfHelpTable": hwLogicIfHelpTable,
       "hwLogicIfHelpEntry": hwLogicIfHelpEntry,
       "hwLogicIfhelpType": hwLogicIfhelpType,
       "hwLogicIfChassisNumber": hwLogicIfChassisNumber,
       "hwLogicIfSlotNumber": hwLogicIfSlotNumber,
       "hwLogicIfCardNumber": hwLogicIfCardNumber,
       "hwLogicIfMin": hwLogicIfMin,
       "hwLogicIfMax": hwLogicIfMax,
       "hwLogicIfTotal": hwLogicIfTotal,
       "hwLogicIfDynamicHelpTable": hwLogicIfDynamicHelpTable,
       "hwLogicIfDynamicHelpEntry": hwLogicIfDynamicHelpEntry,
       "hwLogicDynamicIfhelpType": hwLogicDynamicIfhelpType,
       "hwLogicDynamicIfChassisNumber": hwLogicDynamicIfChassisNumber,
       "hwLogicDynamicIfSlotNumber": hwLogicDynamicIfSlotNumber,
       "hwLogicDynamicIfCardNumber": hwLogicDynamicIfCardNumber,
       "hwLogicDynamicIfMin": hwLogicDynamicIfMin,
       "hwLogicDynamicIfMax": hwLogicDynamicIfMax,
       "hwLogicDynamicIfTotal": hwLogicDynamicIfTotal,
       "hwCppsObjects": hwCppsObjects,
       "hwCppsGlobalEnable": hwCppsGlobalEnable,
       "hwCppsInterfaceTable": hwCppsInterfaceTable,
       "hwCppsInterfaceEntry": hwCppsInterfaceEntry,
       "hwCppsInterfaceIndex": hwCppsInterfaceIndex,
       "hwCppsPortPvcEnable": hwCppsPortPvcEnable,
       "hwCppsPortVlanEnable": hwCppsPortVlanEnable,
       "hwCppsIfStatisticsTable": hwCppsIfStatisticsTable,
       "hwCppsIfStatisticsEntry": hwCppsIfStatisticsEntry,
       "hwCppsIfStatisticsIndex": hwCppsIfStatisticsIndex,
       "hwCppsInterfacePktStatisic": hwCppsInterfacePktStatisic,
       "hwCppsInterfaceByteStatisic": hwCppsInterfaceByteStatisic,
       "hwCppsResetInterfaceStatisic": hwCppsResetInterfaceStatisic,
       "hwCppsAtmPvcTable": hwCppsAtmPvcTable,
       "hwCppsAtmPvcEntry": hwCppsAtmPvcEntry,
       "hwCppsAtmIfIndex": hwCppsAtmIfIndex,
       "hwCppsAtmVpi": hwCppsAtmVpi,
       "hwCppsAtmVci": hwCppsAtmVci,
       "hwCppsAtmPvcPktStatisic": hwCppsAtmPvcPktStatisic,
       "hwCppsAtmPvcByteStatisic": hwCppsAtmPvcByteStatisic,
       "hwCppsResetAtmPvcStatisic": hwCppsResetAtmPvcStatisic,
       "hwCppsPortVlanTable": hwCppsPortVlanTable,
       "hwCppsPortVlanEntry": hwCppsPortVlanEntry,
       "hwCppsPortIndex": hwCppsPortIndex,
       "hwCppsVlanId": hwCppsVlanId,
       "hwCppsPortVlanPktStatisic": hwCppsPortVlanPktStatisic,
       "hwCppsPortVlanByteStatisic": hwCppsPortVlanByteStatisic,
       "hwCppsResetPortVlanStatisic": hwCppsResetPortVlanStatisic,
       "hwPortIsolationGroupAttrib": hwPortIsolationGroupAttrib,
       "hwPortIsolationGroupTable": hwPortIsolationGroupTable,
       "hwPortIsolationGroupEntry": hwPortIsolationGroupEntry,
       "hwPortIsolationGroupIndex": hwPortIsolationGroupIndex,
       "hwPortIsolationGroupPortList": hwPortIsolationGroupPortList,
       "hwPortIsolationGroupRowStatus": hwPortIsolationGroupRowStatus,
       "hwVTrunkAttr": hwVTrunkAttr,
       "hwVTrunkIfTable": hwVTrunkIfTable,
       "hwVTrunkIfEntry": hwVTrunkIfEntry,
       "hwVTrunkIfIndex": hwVTrunkIfIndex,
       "hwVTrunkIfID": hwVTrunkIfID,
       "hwVTrunkIfType": hwVTrunkIfType,
       "hwVTrunkIfRowStatus": hwVTrunkIfRowStatus,
       "hwVTrunkMemAttr": hwVTrunkMemAttr,
       "hwVTrunkMemTable": hwVTrunkMemTable,
       "hwVTrunkMemEntry": hwVTrunkMemEntry,
       "hwVTrunkMemIfIndex": hwVTrunkMemIfIndex,
       "hwVTrunkIfnetIndex": hwVTrunkIfnetIndex,
       "hwVTrunkValidEntry": hwVTrunkValidEntry,
       "hwVTrunkOperstatus": hwVTrunkOperstatus,
       "hwVTrunkPortActive": hwVTrunkPortActive,
       "hwVTrunkRowStatus": hwVTrunkRowStatus,
       "hwMasterBackupTrunkSubinterfaceAttr": hwMasterBackupTrunkSubinterfaceAttr,
       "hwMasterBackupTrunkSubinterfaceTable": hwMasterBackupTrunkSubinterfaceTable,
       "hwMasterBackupTrunkSubinterfaceEntry": hwMasterBackupTrunkSubinterfaceEntry,
       "hwBackupTrunkIfIndex": hwBackupTrunkIfIndex,
       "hwBackupStatus": hwBackupStatus,
       "hwRevertiveMode": hwRevertiveMode,
       "hwWtrTime": hwWtrTime,
       "hwFlushVlanId": hwFlushVlanId,
       "hwVaspPort": hwVaspPort,
       "hwVaspPortPeerMacTable": hwVaspPortPeerMacTable,
       "hwVaspPortPeerMacEntry": hwVaspPortPeerMacEntry,
       "hwVaspPortIfIndex": hwVaspPortIfIndex,
       "hwVaspPortName": hwVaspPortName,
       "hwVaspPortPeerMac": hwVaspPortPeerMac,
       "hwIFExtTrapObjects": hwIFExtTrapObjects,
       "hwLinkDownReason": hwLinkDownReason,
       "hwMainIfName": hwMainIfName,
       "hwCfmOverPhysicalName": hwCfmOverPhysicalName,
       "hwIFExtConformance": hwIFExtConformance,
       "hwIFExtGroups": hwIFExtGroups,
       "hwTrunkIfGroup": hwTrunkIfGroup,
       "hwIfIpAddressGroup": hwIfIpAddressGroup,
       "hwIFExtGroup": hwIFExtGroup,
       "hwTrunkMemGroup": hwTrunkMemGroup,
       "hwIFFlowStatGroup": hwIFFlowStatGroup,
       "hwAdminVrrpMemberIfGroup": hwAdminVrrpMemberIfGroup,
       "hwIfEtherStatGroup": hwIfEtherStatGroup,
       "hwIfMonitorThresholdGroup": hwIfMonitorThresholdGroup,
       "hwIfMonitorGeneralGroup": hwIfMonitorGeneralGroup,
       "hwIfFluxLimitGroup": hwIfFluxLimitGroup,
       "hwIfDiffServGroup": hwIfDiffServGroup,
       "hwIfQueryGroup": hwIfQueryGroup,
       "hwLogicIfAttrGroup": hwLogicIfAttrGroup,
       "hwIfIpUnnumberedGroup": hwIfIpUnnumberedGroup,
       "hwLinkModeChangeAutoCreateIfGroup": hwLinkModeChangeAutoCreateIfGroup,
       "hwCppsGlobalEnableGroup": hwCppsGlobalEnableGroup,
       "hwCppsInterfaceGroup": hwCppsInterfaceGroup,
       "hwCppsIfStatisticsGroup": hwCppsIfStatisticsGroup,
       "hwCppsAtmPvcGroup": hwCppsAtmPvcGroup,
       "hwCppsPortVlanGroup": hwCppsPortVlanGroup,
       "hwPortIsolationGroup": hwPortIsolationGroup,
       "hwVTrunkIfGroup": hwVTrunkIfGroup,
       "hwVTrunkMemGroup": hwVTrunkMemGroup,
       "hwLogicIfHelpTableGroup": hwLogicIfHelpTableGroup,
       "hwSubInterfaceBackupTrunkGroup": hwSubInterfaceBackupTrunkGroup,
       "hwVaspPortGroup": hwVaspPortGroup,
       "hwLogicIfDynamicHelpTableGroup": hwLogicIfDynamicHelpTableGroup,
       "hwIFExtCompliances": hwIFExtCompliances,
       "hwIFExtCompliance": hwIFExtCompliance,
       "hwIFExtTraps": hwIFExtTraps,
       "hwTrunkWorkingSwitch": hwTrunkWorkingSwitch,
       "hwLacpNegotiateFailed": hwLacpNegotiateFailed,
       "hwLacpTotalLinkLoss": hwLacpTotalLinkLoss,
       "hwLacpPartialLinkLoss": hwLacpPartialLinkLoss,
       "hwIfFlowDown": hwIfFlowDown,
       "hwIfFlowUp": hwIfFlowUp,
       "hwIfNameChange": hwIfNameChange,
       "hwIfNameChangeResume": hwIfNameChangeResume,
       "hwExtLinkDown": hwExtLinkDown,
       "hwExtLinkUp": hwExtLinkUp,
       "hwLoopbackBlock": hwLoopbackBlock,
       "hwLoopbackResume": hwLoopbackResume,
       "hwLacpNegotiateResume": hwLacpNegotiateResume,
       "hwLacpTotalLinkLossResume": hwLacpTotalLinkLossResume,
       "hwLacpPartialLinkLossResume": hwLacpPartialLinkLossResume,
       "hwTrunkSubIfStateToMaster": hwTrunkSubIfStateToMaster,
       "hwTrunkSubIfStateToSlave": hwTrunkSubIfStateToSlave,
       "hwEntityExtCfmOverSlot": hwEntityExtCfmOverSlot,
       "hwEntityExtCfmOverCard": hwEntityExtCfmOverCard,
       "hwExtAllMemberDownNotify": hwExtAllMemberDownNotify,
       "hwExtAllMemberDownResume": hwExtAllMemberDownResume,
       "hwIfControlFlapSuppress": hwIfControlFlapSuppress,
       "hwIfControlFlapResume": hwIfControlFlapResume,
       "hwExtInterfaceDelete": hwExtInterfaceDelete,
       "hwMonitorNotifications": hwMonitorNotifications,
       "hwIfMonitorCrcErrorRising": hwIfMonitorCrcErrorRising,
       "hwIfMonitorCrcErrorResume": hwIfMonitorCrcErrorResume,
       "hwIfMonitorSdhErrorRising": hwIfMonitorSdhErrorRising,
       "hwIfMonitorSdhErrorResume": hwIfMonitorSdhErrorResume,
       "hwIfMonitorInputRateRising": hwIfMonitorInputRateRising,
       "hwIfMonitorInputRateResume": hwIfMonitorInputRateResume,
       "hwIfMonitorOutputRateRising": hwIfMonitorOutputRateRising,
       "hwIfMonitorOutputRateResume": hwIfMonitorOutputRateResume,
       "hwIfMonitorHalfDuplexRising": hwIfMonitorHalfDuplexRising,
       "hwIfMonitorPauseFrameRising": hwIfMonitorPauseFrameRising,
       "hwIfMonitorPauseFrameRisingResume": hwIfMonitorPauseFrameRisingResume,
       "hwIfPortControlUp": hwIfPortControlUp,
       "hwIfPortControlDown": hwIfPortControlDown,
       "hwIfMonitorSdhB1ErrorRising": hwIfMonitorSdhB1ErrorRising,
       "hwIfMonitorSdhB1ErrorResume": hwIfMonitorSdhB1ErrorResume,
       "hwIfMonitorSdhB2ErrorRising": hwIfMonitorSdhB2ErrorRising,
       "hwIfMonitorSdhB2ErrorResume": hwIfMonitorSdhB2ErrorResume,
       "hwIfMonitorSymbolErrorRising": hwIfMonitorSymbolErrorRising,
       "hwIfMonitorSymbolErrorResume": hwIfMonitorSymbolErrorResume,
       "hwIfMonitorBadBytesErrorRising": hwIfMonitorBadBytesErrorRising,
       "hwIfMonitorBadBytesErrorResume": hwIfMonitorBadBytesErrorResume,
       "hwIFExtTrapConformance": hwIFExtTrapConformance,
       "hwIFExtTrapGroups": hwIFExtTrapGroups,
       "hwIFExtTrapGroup": hwIFExtTrapGroup,
       "hwMonitorTrapGroup": hwMonitorTrapGroup,
       "hwIFIpNotifications": hwIFIpNotifications,
       "hwIfIpAddressChange": hwIfIpAddressChange}
)
