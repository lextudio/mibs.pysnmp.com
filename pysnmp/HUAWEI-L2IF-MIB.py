# SNMP MIB module (HUAWEI-L2IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:17 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwL2IfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HwL2Mgmt_ObjectIdentity = ObjectIdentity
hwL2Mgmt = _HwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42)
)
_HwL2IfObjects_ObjectIdentity = ObjectIdentity
hwL2IfObjects = _HwL2IfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1)
)
_HwL2Interface_ObjectIdentity = ObjectIdentity
hwL2Interface = _HwL2Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1)
)
_HwL2IfPortMax_Type = Integer32
_HwL2IfPortMax_Object = MibScalar
hwL2IfPortMax = _HwL2IfPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 1),
    _HwL2IfPortMax_Type()
)
hwL2IfPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfPortMax.setStatus("current")
_HwL2TopologyDetect_Type = EnabledStatus
_HwL2TopologyDetect_Object = MibScalar
hwL2TopologyDetect = _HwL2TopologyDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 2),
    _HwL2TopologyDetect_Type()
)
hwL2TopologyDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2TopologyDetect.setStatus("current")
_HwL2IfTable_Object = MibTable
hwL2IfTable = _HwL2IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwL2IfTable.setStatus("current")
_HwL2IfEntry_Object = MibTableRow
hwL2IfEntry = _HwL2IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1)
)
hwL2IfEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPortNum"),
)
if mibBuilder.loadTexts:
    hwL2IfEntry.setStatus("current")


class _HwL2IfPortNum_Type(Integer32):
    """Custom type hwL2IfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2IfPortNum_Type.__name__ = "Integer32"
_HwL2IfPortNum_Object = MibTableColumn
hwL2IfPortNum = _HwL2IfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 1),
    _HwL2IfPortNum_Type()
)
hwL2IfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPortNum.setStatus("current")
_HwL2IfPortIfIndex_Type = InterfaceIndex
_HwL2IfPortIfIndex_Object = MibTableColumn
hwL2IfPortIfIndex = _HwL2IfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 2),
    _HwL2IfPortIfIndex_Type()
)
hwL2IfPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfPortIfIndex.setStatus("current")


class _HwL2IfPortType_Type(Integer32):
    """Custom type hwL2IfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("fabric", 4),
          ("hybrid", 3),
          ("invalid", 0),
          ("qinq", 5),
          ("trunk", 1))
    )


_HwL2IfPortType_Type.__name__ = "Integer32"
_HwL2IfPortType_Object = MibTableColumn
hwL2IfPortType = _HwL2IfPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 3),
    _HwL2IfPortType_Type()
)
hwL2IfPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPortType.setStatus("current")
_HwL2IfPVID_Type = Integer32
_HwL2IfPVID_Object = MibTableColumn
hwL2IfPVID = _HwL2IfPVID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 4),
    _HwL2IfPVID_Type()
)
hwL2IfPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPVID.setStatus("current")
_HwL2IfIsSrcMacFilter_Type = TruthValue
_HwL2IfIsSrcMacFilter_Object = MibTableColumn
hwL2IfIsSrcMacFilter = _HwL2IfIsSrcMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 5),
    _HwL2IfIsSrcMacFilter_Type()
)
hwL2IfIsSrcMacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfIsSrcMacFilter.setStatus("current")


class _HwL2IfMacAddrLearnMode_Type(Integer32):
    """Custom type hwL2IfMacAddrLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iVL", 1),
          ("sVL", 2))
    )


_HwL2IfMacAddrLearnMode_Type.__name__ = "Integer32"
_HwL2IfMacAddrLearnMode_Object = MibTableColumn
hwL2IfMacAddrLearnMode = _HwL2IfMacAddrLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 6),
    _HwL2IfMacAddrLearnMode_Type()
)
hwL2IfMacAddrLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfMacAddrLearnMode.setStatus("current")


class _HwL2IfMacAddressLearn_Type(Integer32):
    """Custom type hwL2IfMacAddressLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("discard", 3),
          ("enabled", 1))
    )


_HwL2IfMacAddressLearn_Type.__name__ = "Integer32"
_HwL2IfMacAddressLearn_Object = MibTableColumn
hwL2IfMacAddressLearn = _HwL2IfMacAddressLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 7),
    _HwL2IfMacAddressLearn_Type()
)
hwL2IfMacAddressLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfMacAddressLearn.setStatus("current")


class _HwL2IfBcastRatio_Type(Integer32):
    """Custom type hwL2IfBcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwL2IfBcastRatio_Type.__name__ = "Integer32"
_HwL2IfBcastRatio_Object = MibTableColumn
hwL2IfBcastRatio = _HwL2IfBcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 8),
    _HwL2IfBcastRatio_Type()
)
hwL2IfBcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfBcastRatio.setStatus("current")


class _HwL2IfMcastRatio_Type(Integer32):
    """Custom type hwL2IfMcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwL2IfMcastRatio_Type.__name__ = "Integer32"
_HwL2IfMcastRatio_Object = MibTableColumn
hwL2IfMcastRatio = _HwL2IfMcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 9),
    _HwL2IfMcastRatio_Type()
)
hwL2IfMcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfMcastRatio.setStatus("current")


class _HwL2IfUcastRatio_Type(Integer32):
    """Custom type hwL2IfUcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwL2IfUcastRatio_Type.__name__ = "Integer32"
_HwL2IfUcastRatio_Object = MibTableColumn
hwL2IfUcastRatio = _HwL2IfUcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 10),
    _HwL2IfUcastRatio_Type()
)
hwL2IfUcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfUcastRatio.setStatus("current")


class _HwL2IfOutBcastRatio_Type(Integer32):
    """Custom type hwL2IfOutBcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwL2IfOutBcastRatio_Type.__name__ = "Integer32"
_HwL2IfOutBcastRatio_Object = MibTableColumn
hwL2IfOutBcastRatio = _HwL2IfOutBcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 11),
    _HwL2IfOutBcastRatio_Type()
)
hwL2IfOutBcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfOutBcastRatio.setStatus("current")


class _HwL2IfOutMcastRatio_Type(Integer32):
    """Custom type hwL2IfOutMcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwL2IfOutMcastRatio_Type.__name__ = "Integer32"
_HwL2IfOutMcastRatio_Object = MibTableColumn
hwL2IfOutMcastRatio = _HwL2IfOutMcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 12),
    _HwL2IfOutMcastRatio_Type()
)
hwL2IfOutMcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfOutMcastRatio.setStatus("current")


class _HwL2IfOutUcastRatio_Type(Integer32):
    """Custom type hwL2IfOutUcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwL2IfOutUcastRatio_Type.__name__ = "Integer32"
_HwL2IfOutUcastRatio_Object = MibTableColumn
hwL2IfOutUcastRatio = _HwL2IfOutUcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 13),
    _HwL2IfOutUcastRatio_Type()
)
hwL2IfOutUcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfOutUcastRatio.setStatus("current")
_HwL2IfDiscardBcast_Type = EnabledStatus
_HwL2IfDiscardBcast_Object = MibTableColumn
hwL2IfDiscardBcast = _HwL2IfDiscardBcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 14),
    _HwL2IfDiscardBcast_Type()
)
hwL2IfDiscardBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfDiscardBcast.setStatus("current")
_HwL2IfDiscardUnknownMcast_Type = EnabledStatus
_HwL2IfDiscardUnknownMcast_Object = MibTableColumn
hwL2IfDiscardUnknownMcast = _HwL2IfDiscardUnknownMcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 15),
    _HwL2IfDiscardUnknownMcast_Type()
)
hwL2IfDiscardUnknownMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfDiscardUnknownMcast.setStatus("current")
_HwL2IfDiscardUnknownUcast_Type = EnabledStatus
_HwL2IfDiscardUnknownUcast_Object = MibTableColumn
hwL2IfDiscardUnknownUcast = _HwL2IfDiscardUnknownUcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 16),
    _HwL2IfDiscardUnknownUcast_Type()
)
hwL2IfDiscardUnknownUcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfDiscardUnknownUcast.setStatus("current")
_HwL2IfBpdu_Type = EnabledStatus
_HwL2IfBpdu_Object = MibTableColumn
hwL2IfBpdu = _HwL2IfBpdu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 17),
    _HwL2IfBpdu_Type()
)
hwL2IfBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfBpdu.setStatus("current")


class _HwL2IfPortPriority_Type(Integer32):
    """Custom type hwL2IfPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2IfPortPriority_Type.__name__ = "Integer32"
_HwL2IfPortPriority_Object = MibTableColumn
hwL2IfPortPriority = _HwL2IfPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 18),
    _HwL2IfPortPriority_Type()
)
hwL2IfPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPortPriority.setStatus("current")


class _HwL2IfPortName_Type(OctetString):
    """Custom type hwL2IfPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwL2IfPortName_Type.__name__ = "OctetString"
_HwL2IfPortName_Object = MibTableColumn
hwL2IfPortName = _HwL2IfPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 19),
    _HwL2IfPortName_Type()
)
hwL2IfPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfPortName.setStatus("current")
_HwL2IfInInvalidVlanPkts_Type = Counter64
_HwL2IfInInvalidVlanPkts_Object = MibTableColumn
hwL2IfInInvalidVlanPkts = _HwL2IfInInvalidVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 20),
    _HwL2IfInInvalidVlanPkts_Type()
)
hwL2IfInInvalidVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfInInvalidVlanPkts.setStatus("current")
_HwL2IfFlushEnable_Type = EnabledStatus
_HwL2IfFlushEnable_Object = MibTableColumn
hwL2IfFlushEnable = _HwL2IfFlushEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 21),
    _HwL2IfFlushEnable_Type()
)
hwL2IfFlushEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfFlushEnable.setStatus("current")


class _HwL2IfFlushControlVlan_Type(Integer32):
    """Custom type hwL2IfFlushControlVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HwL2IfFlushControlVlan_Type.__name__ = "Integer32"
_HwL2IfFlushControlVlan_Object = MibTableColumn
hwL2IfFlushControlVlan = _HwL2IfFlushControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 22),
    _HwL2IfFlushControlVlan_Type()
)
hwL2IfFlushControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfFlushControlVlan.setStatus("current")
_HwL2IfCurrentInBcastPercent_Type = EnabledStatus
_HwL2IfCurrentInBcastPercent_Object = MibTableColumn
hwL2IfCurrentInBcastPercent = _HwL2IfCurrentInBcastPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 23),
    _HwL2IfCurrentInBcastPercent_Type()
)
hwL2IfCurrentInBcastPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfCurrentInBcastPercent.setStatus("current")
_HwL2IfCurrentOutBcastPercent_Type = EnabledStatus
_HwL2IfCurrentOutBcastPercent_Object = MibTableColumn
hwL2IfCurrentOutBcastPercent = _HwL2IfCurrentOutBcastPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 24),
    _HwL2IfCurrentOutBcastPercent_Type()
)
hwL2IfCurrentOutBcastPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfCurrentOutBcastPercent.setStatus("current")
_HwL2IfQinqVlanTransEnable_Type = EnabledStatus
_HwL2IfQinqVlanTransEnable_Object = MibTableColumn
hwL2IfQinqVlanTransEnable = _HwL2IfQinqVlanTransEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 25),
    _HwL2IfQinqVlanTransEnable_Type()
)
hwL2IfQinqVlanTransEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfQinqVlanTransEnable.setStatus("current")


class _HwL2IfQinqVlanTransMissDrop_Type(Integer32):
    """Custom type hwL2IfQinqVlanTransMissDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("noDrop", 1))
    )


_HwL2IfQinqVlanTransMissDrop_Type.__name__ = "Integer32"
_HwL2IfQinqVlanTransMissDrop_Object = MibTableColumn
hwL2IfQinqVlanTransMissDrop = _HwL2IfQinqVlanTransMissDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 26),
    _HwL2IfQinqVlanTransMissDrop_Type()
)
hwL2IfQinqVlanTransMissDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfQinqVlanTransMissDrop.setStatus("current")
_HwL2IfIpSubnetVlanEnable_Type = EnabledStatus
_HwL2IfIpSubnetVlanEnable_Object = MibTableColumn
hwL2IfIpSubnetVlanEnable = _HwL2IfIpSubnetVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 27),
    _HwL2IfIpSubnetVlanEnable_Type()
)
hwL2IfIpSubnetVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfIpSubnetVlanEnable.setStatus("current")
_HwL2IfMacVlanEnable_Type = EnabledStatus
_HwL2IfMacVlanEnable_Object = MibTableColumn
hwL2IfMacVlanEnable = _HwL2IfMacVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 28),
    _HwL2IfMacVlanEnable_Type()
)
hwL2IfMacVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfMacVlanEnable.setStatus("current")
_HwL2IfPolicyVlanEnable_Type = EnabledStatus
_HwL2IfPolicyVlanEnable_Object = MibTableColumn
hwL2IfPolicyVlanEnable = _HwL2IfPolicyVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 29),
    _HwL2IfPolicyVlanEnable_Type()
)
hwL2IfPolicyVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPolicyVlanEnable.setStatus("current")
_HwL2IfVlanPrecedence_Type = Integer32
_HwL2IfVlanPrecedence_Object = MibTableColumn
hwL2IfVlanPrecedence = _HwL2IfVlanPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 30),
    _HwL2IfVlanPrecedence_Type()
)
hwL2IfVlanPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfVlanPrecedence.setStatus("current")


class _HwL2IfIsolateGroupEnable_Type(EnabledStatus):
    """Custom type hwL2IfIsolateGroupEnable based on EnabledStatus"""
    defaultValue = 2


_HwL2IfIsolateGroupEnable_Object = MibTableColumn
hwL2IfIsolateGroupEnable = _HwL2IfIsolateGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 3, 1, 31),
    _HwL2IfIsolateGroupEnable_Type()
)
hwL2IfIsolateGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfIsolateGroupEnable.setStatus("current")
_HwL2IfHybridPortTable_Object = MibTable
hwL2IfHybridPortTable = _HwL2IfHybridPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwL2IfHybridPortTable.setStatus("current")
_HwL2IfHybridPortEntry_Object = MibTableRow
hwL2IfHybridPortEntry = _HwL2IfHybridPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9, 1)
)
hwL2IfHybridPortEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfHybridPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2IfHybridPortEntry.setStatus("current")


class _HwL2IfHybridPortIndex_Type(Integer32):
    """Custom type hwL2IfHybridPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2IfHybridPortIndex_Type.__name__ = "Integer32"
_HwL2IfHybridPortIndex_Object = MibTableColumn
hwL2IfHybridPortIndex = _HwL2IfHybridPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9, 1, 1),
    _HwL2IfHybridPortIndex_Type()
)
hwL2IfHybridPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfHybridPortIndex.setStatus("current")


class _HwL2IfHybridTaggedVlanListLow_Type(VlanList):
    """Custom type hwL2IfHybridTaggedVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfHybridTaggedVlanListLow_Type.__name__ = "VlanList"
_HwL2IfHybridTaggedVlanListLow_Object = MibTableColumn
hwL2IfHybridTaggedVlanListLow = _HwL2IfHybridTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9, 1, 2),
    _HwL2IfHybridTaggedVlanListLow_Type()
)
hwL2IfHybridTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfHybridTaggedVlanListLow.setStatus("current")


class _HwL2IfHybridTaggedVlanListHigh_Type(VlanList):
    """Custom type hwL2IfHybridTaggedVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfHybridTaggedVlanListHigh_Type.__name__ = "VlanList"
_HwL2IfHybridTaggedVlanListHigh_Object = MibTableColumn
hwL2IfHybridTaggedVlanListHigh = _HwL2IfHybridTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9, 1, 3),
    _HwL2IfHybridTaggedVlanListHigh_Type()
)
hwL2IfHybridTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfHybridTaggedVlanListHigh.setStatus("current")


class _HwL2IfHybridUnTaggedVlanListLow_Type(VlanList):
    """Custom type hwL2IfHybridUnTaggedVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfHybridUnTaggedVlanListLow_Type.__name__ = "VlanList"
_HwL2IfHybridUnTaggedVlanListLow_Object = MibTableColumn
hwL2IfHybridUnTaggedVlanListLow = _HwL2IfHybridUnTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9, 1, 4),
    _HwL2IfHybridUnTaggedVlanListLow_Type()
)
hwL2IfHybridUnTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfHybridUnTaggedVlanListLow.setStatus("current")


class _HwL2IfHybridUnTaggedVlanListHigh_Type(VlanList):
    """Custom type hwL2IfHybridUnTaggedVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfHybridUnTaggedVlanListHigh_Type.__name__ = "VlanList"
_HwL2IfHybridUnTaggedVlanListHigh_Object = MibTableColumn
hwL2IfHybridUnTaggedVlanListHigh = _HwL2IfHybridUnTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 9, 1, 5),
    _HwL2IfHybridUnTaggedVlanListHigh_Type()
)
hwL2IfHybridUnTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfHybridUnTaggedVlanListHigh.setStatus("current")
_HwL2IfTrunkPortTable_Object = MibTable
hwL2IfTrunkPortTable = _HwL2IfTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hwL2IfTrunkPortTable.setStatus("current")
_HwL2IfTrunkPortEntry_Object = MibTableRow
hwL2IfTrunkPortEntry = _HwL2IfTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 10, 1)
)
hwL2IfTrunkPortEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2IfTrunkPortEntry.setStatus("current")


class _HwL2IfTrunkPortIndex_Type(Integer32):
    """Custom type hwL2IfTrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2IfTrunkPortIndex_Type.__name__ = "Integer32"
_HwL2IfTrunkPortIndex_Object = MibTableColumn
hwL2IfTrunkPortIndex = _HwL2IfTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 10, 1, 1),
    _HwL2IfTrunkPortIndex_Type()
)
hwL2IfTrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfTrunkPortIndex.setStatus("current")


class _HwL2IfTrunkAllowPassVlanListLow_Type(VlanList):
    """Custom type hwL2IfTrunkAllowPassVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwL2IfTrunkAllowPassVlanListLow_Type.__name__ = "VlanList"
_HwL2IfTrunkAllowPassVlanListLow_Object = MibTableColumn
hwL2IfTrunkAllowPassVlanListLow = _HwL2IfTrunkAllowPassVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 10, 1, 2),
    _HwL2IfTrunkAllowPassVlanListLow_Type()
)
hwL2IfTrunkAllowPassVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfTrunkAllowPassVlanListLow.setStatus("current")


class _HwL2IfTrunkAllowPassVlanListHigh_Type(VlanList):
    """Custom type hwL2IfTrunkAllowPassVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwL2IfTrunkAllowPassVlanListHigh_Type.__name__ = "VlanList"
_HwL2IfTrunkAllowPassVlanListHigh_Object = MibTableColumn
hwL2IfTrunkAllowPassVlanListHigh = _HwL2IfTrunkAllowPassVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 10, 1, 3),
    _HwL2IfTrunkAllowPassVlanListHigh_Type()
)
hwL2IfTrunkAllowPassVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfTrunkAllowPassVlanListHigh.setStatus("current")
_HwL2IfPortIsolateTable_Object = MibTable
hwL2IfPortIsolateTable = _HwL2IfPortIsolateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hwL2IfPortIsolateTable.setStatus("current")
_HwL2IfPortIsolateEntry_Object = MibTableRow
hwL2IfPortIsolateEntry = _HwL2IfPortIsolateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 11, 1)
)
hwL2IfPortIsolateEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPortIsolatePortIndex"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPortIsolateSIName"),
)
if mibBuilder.loadTexts:
    hwL2IfPortIsolateEntry.setStatus("current")


class _HwL2IfPortIsolatePortIndex_Type(Integer32):
    """Custom type hwL2IfPortIsolatePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2IfPortIsolatePortIndex_Type.__name__ = "Integer32"
_HwL2IfPortIsolatePortIndex_Object = MibTableColumn
hwL2IfPortIsolatePortIndex = _HwL2IfPortIsolatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 11, 1, 1),
    _HwL2IfPortIsolatePortIndex_Type()
)
hwL2IfPortIsolatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPortIsolatePortIndex.setStatus("current")


class _HwL2IfPortIsolateSIName_Type(OctetString):
    """Custom type hwL2IfPortIsolateSIName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2IfPortIsolateSIName_Type.__name__ = "OctetString"
_HwL2IfPortIsolateSIName_Object = MibTableColumn
hwL2IfPortIsolateSIName = _HwL2IfPortIsolateSIName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 11, 1, 2),
    _HwL2IfPortIsolateSIName_Type()
)
hwL2IfPortIsolateSIName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPortIsolateSIName.setStatus("current")
_HwL2IfPortIsolateRowStatus_Type = RowStatus
_HwL2IfPortIsolateRowStatus_Object = MibTableColumn
hwL2IfPortIsolateRowStatus = _HwL2IfPortIsolateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 11, 1, 3),
    _HwL2IfPortIsolateRowStatus_Type()
)
hwL2IfPortIsolateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPortIsolateRowStatus.setStatus("current")
_HwL2IfSuppressionTable_Object = MibTable
hwL2IfSuppressionTable = _HwL2IfSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hwL2IfSuppressionTable.setStatus("current")
_HwL2IfSuppressionEntry_Object = MibTableRow
hwL2IfSuppressionEntry = _HwL2IfSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12, 1)
)
hwL2IfSuppressionEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfSuppressionPortIndex"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfSuppressionType"),
)
if mibBuilder.loadTexts:
    hwL2IfSuppressionEntry.setStatus("current")


class _HwL2IfSuppressionPortIndex_Type(Integer32):
    """Custom type hwL2IfSuppressionPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfSuppressionPortIndex_Type.__name__ = "Integer32"
_HwL2IfSuppressionPortIndex_Object = MibTableColumn
hwL2IfSuppressionPortIndex = _HwL2IfSuppressionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12, 1, 1),
    _HwL2IfSuppressionPortIndex_Type()
)
hwL2IfSuppressionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfSuppressionPortIndex.setStatus("current")


class _HwL2IfSuppressionType_Type(Integer32):
    """Custom type hwL2IfSuppressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_HwL2IfSuppressionType_Type.__name__ = "Integer32"
_HwL2IfSuppressionType_Object = MibTableColumn
hwL2IfSuppressionType = _HwL2IfSuppressionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12, 1, 2),
    _HwL2IfSuppressionType_Type()
)
hwL2IfSuppressionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfSuppressionType.setStatus("current")


class _HwL2IfSuppressionCir_Type(Integer32):
    """Custom type hwL2IfSuppressionCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwL2IfSuppressionCir_Type.__name__ = "Integer32"
_HwL2IfSuppressionCir_Object = MibTableColumn
hwL2IfSuppressionCir = _HwL2IfSuppressionCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12, 1, 3),
    _HwL2IfSuppressionCir_Type()
)
hwL2IfSuppressionCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfSuppressionCir.setStatus("current")


class _HwL2IfSuppressionCbs_Type(Integer32):
    """Custom type hwL2IfSuppressionCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 64000000),
    )


_HwL2IfSuppressionCbs_Type.__name__ = "Integer32"
_HwL2IfSuppressionCbs_Object = MibTableColumn
hwL2IfSuppressionCbs = _HwL2IfSuppressionCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12, 1, 4),
    _HwL2IfSuppressionCbs_Type()
)
hwL2IfSuppressionCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfSuppressionCbs.setStatus("current")
_HwL2IfSuppressionRowStatus_Type = RowStatus
_HwL2IfSuppressionRowStatus_Object = MibTableColumn
hwL2IfSuppressionRowStatus = _HwL2IfSuppressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 12, 1, 5),
    _HwL2IfSuppressionRowStatus_Type()
)
hwL2IfSuppressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfSuppressionRowStatus.setStatus("current")
_HwL2IfVlanSuppressionTable_Object = MibTable
hwL2IfVlanSuppressionTable = _HwL2IfVlanSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionTable.setStatus("current")
_HwL2IfVlanSuppressionEntry_Object = MibTableRow
hwL2IfVlanSuppressionEntry = _HwL2IfVlanSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1)
)
hwL2IfVlanSuppressionEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfVlanSuppressionPortIndex"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfVlanSuppressionStartVlan"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfVlanSuppressionEndVlan"),
)
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionEntry.setStatus("current")


class _HwL2IfVlanSuppressionPortIndex_Type(Integer32):
    """Custom type hwL2IfVlanSuppressionPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfVlanSuppressionPortIndex_Type.__name__ = "Integer32"
_HwL2IfVlanSuppressionPortIndex_Object = MibTableColumn
hwL2IfVlanSuppressionPortIndex = _HwL2IfVlanSuppressionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1, 1),
    _HwL2IfVlanSuppressionPortIndex_Type()
)
hwL2IfVlanSuppressionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionPortIndex.setStatus("current")


class _HwL2IfVlanSuppressionStartVlan_Type(Integer32):
    """Custom type hwL2IfVlanSuppressionStartVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwL2IfVlanSuppressionStartVlan_Type.__name__ = "Integer32"
_HwL2IfVlanSuppressionStartVlan_Object = MibTableColumn
hwL2IfVlanSuppressionStartVlan = _HwL2IfVlanSuppressionStartVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1, 2),
    _HwL2IfVlanSuppressionStartVlan_Type()
)
hwL2IfVlanSuppressionStartVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionStartVlan.setStatus("current")


class _HwL2IfVlanSuppressionEndVlan_Type(Integer32):
    """Custom type hwL2IfVlanSuppressionEndVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwL2IfVlanSuppressionEndVlan_Type.__name__ = "Integer32"
_HwL2IfVlanSuppressionEndVlan_Object = MibTableColumn
hwL2IfVlanSuppressionEndVlan = _HwL2IfVlanSuppressionEndVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1, 3),
    _HwL2IfVlanSuppressionEndVlan_Type()
)
hwL2IfVlanSuppressionEndVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionEndVlan.setStatus("current")


class _HwL2IfVlanSuppressionCir_Type(Integer32):
    """Custom type hwL2IfVlanSuppressionCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwL2IfVlanSuppressionCir_Type.__name__ = "Integer32"
_HwL2IfVlanSuppressionCir_Object = MibTableColumn
hwL2IfVlanSuppressionCir = _HwL2IfVlanSuppressionCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1, 4),
    _HwL2IfVlanSuppressionCir_Type()
)
hwL2IfVlanSuppressionCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionCir.setStatus("current")


class _HwL2IfVlanSuppressionCbs_Type(Integer32):
    """Custom type hwL2IfVlanSuppressionCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 64000000),
    )


_HwL2IfVlanSuppressionCbs_Type.__name__ = "Integer32"
_HwL2IfVlanSuppressionCbs_Object = MibTableColumn
hwL2IfVlanSuppressionCbs = _HwL2IfVlanSuppressionCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1, 5),
    _HwL2IfVlanSuppressionCbs_Type()
)
hwL2IfVlanSuppressionCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionCbs.setStatus("current")
_HwL2IfVlanSuppressionRowStatus_Type = RowStatus
_HwL2IfVlanSuppressionRowStatus_Object = MibTableColumn
hwL2IfVlanSuppressionRowStatus = _HwL2IfVlanSuppressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 13, 1, 6),
    _HwL2IfVlanSuppressionRowStatus_Type()
)
hwL2IfVlanSuppressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionRowStatus.setStatus("current")
_HwL2IfPortTcnTable_Object = MibTable
hwL2IfPortTcnTable = _HwL2IfPortTcnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hwL2IfPortTcnTable.setStatus("current")
_HwL2IfPortTcnEntry_Object = MibTableRow
hwL2IfPortTcnEntry = _HwL2IfPortTcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14, 1)
)
hwL2IfPortTcnEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfTcnPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2IfPortTcnEntry.setStatus("current")


class _HwL2IfTcnPortIndex_Type(Integer32):
    """Custom type hwL2IfTcnPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2IfTcnPortIndex_Type.__name__ = "Integer32"
_HwL2IfTcnPortIndex_Object = MibTableColumn
hwL2IfTcnPortIndex = _HwL2IfTcnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14, 1, 1),
    _HwL2IfTcnPortIndex_Type()
)
hwL2IfTcnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfTcnPortIndex.setStatus("current")
_HwL2IfTcnStp_Type = EnabledStatus
_HwL2IfTcnStp_Object = MibTableColumn
hwL2IfTcnStp = _HwL2IfTcnStp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14, 1, 2),
    _HwL2IfTcnStp_Type()
)
hwL2IfTcnStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfTcnStp.setStatus("current")
_HwL2IfTcnSmartLink_Type = EnabledStatus
_HwL2IfTcnSmartLink_Object = MibTableColumn
hwL2IfTcnSmartLink = _HwL2IfTcnSmartLink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14, 1, 3),
    _HwL2IfTcnSmartLink_Type()
)
hwL2IfTcnSmartLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfTcnSmartLink.setStatus("current")


class _HwL2IfTcnVlanListLow_Type(OctetString):
    """Custom type hwL2IfTcnVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2IfTcnVlanListLow_Type.__name__ = "OctetString"
_HwL2IfTcnVlanListLow_Object = MibTableColumn
hwL2IfTcnVlanListLow = _HwL2IfTcnVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14, 1, 4),
    _HwL2IfTcnVlanListLow_Type()
)
hwL2IfTcnVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfTcnVlanListLow.setStatus("current")


class _HwL2IfTcnVlanListHigh_Type(OctetString):
    """Custom type hwL2IfTcnVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2IfTcnVlanListHigh_Type.__name__ = "OctetString"
_HwL2IfTcnVlanListHigh_Object = MibTableColumn
hwL2IfTcnVlanListHigh = _HwL2IfTcnVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 14, 1, 5),
    _HwL2IfTcnVlanListHigh_Type()
)
hwL2IfTcnVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfTcnVlanListHigh.setStatus("current")
_HwL2IfPortLoopDetectTable_Object = MibTable
hwL2IfPortLoopDetectTable = _HwL2IfPortLoopDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectTable.setStatus("current")
_HwL2IfPortLoopDetectEntry_Object = MibTableRow
hwL2IfPortLoopDetectEntry = _HwL2IfPortLoopDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1)
)
hwL2IfPortLoopDetectEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectPort"),
)
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectEntry.setStatus("current")
_HwL2IfPortLoopDetectPort_Type = Integer32
_HwL2IfPortLoopDetectPort_Object = MibTableColumn
hwL2IfPortLoopDetectPort = _HwL2IfPortLoopDetectPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1, 1),
    _HwL2IfPortLoopDetectPort_Type()
)
hwL2IfPortLoopDetectPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectPort.setStatus("current")
_HwL2IfPortLoopDetectEnabled_Type = EnabledStatus
_HwL2IfPortLoopDetectEnabled_Object = MibTableColumn
hwL2IfPortLoopDetectEnabled = _HwL2IfPortLoopDetectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1, 2),
    _HwL2IfPortLoopDetectEnabled_Type()
)
hwL2IfPortLoopDetectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectEnabled.setStatus("current")
_HwL2IfPortLoopDetectInterval_Type = Integer32
_HwL2IfPortLoopDetectInterval_Object = MibTableColumn
hwL2IfPortLoopDetectInterval = _HwL2IfPortLoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1, 3),
    _HwL2IfPortLoopDetectInterval_Type()
)
hwL2IfPortLoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectInterval.setStatus("current")


class _HwL2IfPortLoopDetectAction_Type(Integer32):
    """Custom type hwL2IfPortLoopDetectAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("shutdown", 1),
          ("trap", 3))
    )


_HwL2IfPortLoopDetectAction_Type.__name__ = "Integer32"
_HwL2IfPortLoopDetectAction_Object = MibTableColumn
hwL2IfPortLoopDetectAction = _HwL2IfPortLoopDetectAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1, 4),
    _HwL2IfPortLoopDetectAction_Type()
)
hwL2IfPortLoopDetectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectAction.setStatus("current")


class _HwL2IfPortLoopDetectStatus_Type(Integer32):
    """Custom type hwL2IfPortLoopDetectStatus based on Integer32"""
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
        *(("block", 2),
          ("normal", 1),
          ("shutdown", 3),
          ("trap", 4))
    )


_HwL2IfPortLoopDetectStatus_Type.__name__ = "Integer32"
_HwL2IfPortLoopDetectStatus_Object = MibTableColumn
hwL2IfPortLoopDetectStatus = _HwL2IfPortLoopDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1, 5),
    _HwL2IfPortLoopDetectStatus_Type()
)
hwL2IfPortLoopDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectStatus.setStatus("current")


class _HwL2IfPortLoopDetectProtocol_Type(OctetString):
    """Custom type hwL2IfPortLoopDetectProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwL2IfPortLoopDetectProtocol_Type.__name__ = "OctetString"
_HwL2IfPortLoopDetectProtocol_Object = MibTableColumn
hwL2IfPortLoopDetectProtocol = _HwL2IfPortLoopDetectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 15, 1, 6),
    _HwL2IfPortLoopDetectProtocol_Type()
)
hwL2IfPortLoopDetectProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectProtocol.setStatus("current")
_HwL2IfPortProtocolVlanDataTable_Object = MibTable
hwL2IfPortProtocolVlanDataTable = _HwL2IfPortProtocolVlanDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataTable.setStatus("current")
_HwL2IfPortProtocolVlanDataEntry_Object = MibTableRow
hwL2IfPortProtocolVlanDataEntry = _HwL2IfPortProtocolVlanDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 16, 1)
)
hwL2IfPortProtocolVlanDataEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPortProtocolVlanDataPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataEntry.setStatus("current")


class _HwL2IfPortProtocolVlanDataPortIndex_Type(Integer32):
    """Custom type hwL2IfPortProtocolVlanDataPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 479),
    )


_HwL2IfPortProtocolVlanDataPortIndex_Type.__name__ = "Integer32"
_HwL2IfPortProtocolVlanDataPortIndex_Object = MibTableColumn
hwL2IfPortProtocolVlanDataPortIndex = _HwL2IfPortProtocolVlanDataPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 16, 1, 1),
    _HwL2IfPortProtocolVlanDataPortIndex_Type()
)
hwL2IfPortProtocolVlanDataPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataPortIndex.setStatus("current")
_HwL2IfPortProtocolVlanDataVlan_Type = Integer32
_HwL2IfPortProtocolVlanDataVlan_Object = MibTableColumn
hwL2IfPortProtocolVlanDataVlan = _HwL2IfPortProtocolVlanDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 16, 1, 2),
    _HwL2IfPortProtocolVlanDataVlan_Type()
)
hwL2IfPortProtocolVlanDataVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataVlan.setStatus("current")
_HwL2IfPortProtocolVlanDataPri_Type = Integer32
_HwL2IfPortProtocolVlanDataPri_Object = MibTableColumn
hwL2IfPortProtocolVlanDataPri = _HwL2IfPortProtocolVlanDataPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 16, 1, 3),
    _HwL2IfPortProtocolVlanDataPri_Type()
)
hwL2IfPortProtocolVlanDataPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataPri.setStatus("current")
_HwL2IfPortProtocolVlanDataRowStatus_Type = RowStatus
_HwL2IfPortProtocolVlanDataRowStatus_Object = MibTableColumn
hwL2IfPortProtocolVlanDataRowStatus = _HwL2IfPortProtocolVlanDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 16, 1, 4),
    _HwL2IfPortProtocolVlanDataRowStatus_Type()
)
hwL2IfPortProtocolVlanDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataRowStatus.setStatus("current")
_HwL2IfPwSuppressionTable_Object = MibTable
hwL2IfPwSuppressionTable = _HwL2IfPwSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionTable.setStatus("current")
_HwL2IfPwSuppressionEntry_Object = MibTableRow
hwL2IfPwSuppressionEntry = _HwL2IfPwSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1)
)
hwL2IfPwSuppressionEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPwSuppressionVsiName"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPwSuppressionPwName"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfPwSuppressionType"),
)
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionEntry.setStatus("current")


class _HwL2IfPwSuppressionVsiName_Type(OctetString):
    """Custom type hwL2IfPwSuppressionVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwL2IfPwSuppressionVsiName_Type.__name__ = "OctetString"
_HwL2IfPwSuppressionVsiName_Object = MibTableColumn
hwL2IfPwSuppressionVsiName = _HwL2IfPwSuppressionVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1, 1),
    _HwL2IfPwSuppressionVsiName_Type()
)
hwL2IfPwSuppressionVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionVsiName.setStatus("current")


class _HwL2IfPwSuppressionPwName_Type(OctetString):
    """Custom type hwL2IfPwSuppressionPwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwL2IfPwSuppressionPwName_Type.__name__ = "OctetString"
_HwL2IfPwSuppressionPwName_Object = MibTableColumn
hwL2IfPwSuppressionPwName = _HwL2IfPwSuppressionPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1, 2),
    _HwL2IfPwSuppressionPwName_Type()
)
hwL2IfPwSuppressionPwName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionPwName.setStatus("current")


class _HwL2IfPwSuppressionType_Type(Integer32):
    """Custom type hwL2IfPwSuppressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_HwL2IfPwSuppressionType_Type.__name__ = "Integer32"
_HwL2IfPwSuppressionType_Object = MibTableColumn
hwL2IfPwSuppressionType = _HwL2IfPwSuppressionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1, 3),
    _HwL2IfPwSuppressionType_Type()
)
hwL2IfPwSuppressionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionType.setStatus("current")


class _HwL2IfPwSuppressionCir_Type(Integer32):
    """Custom type hwL2IfPwSuppressionCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_HwL2IfPwSuppressionCir_Type.__name__ = "Integer32"
_HwL2IfPwSuppressionCir_Object = MibTableColumn
hwL2IfPwSuppressionCir = _HwL2IfPwSuppressionCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1, 4),
    _HwL2IfPwSuppressionCir_Type()
)
hwL2IfPwSuppressionCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionCir.setStatus("current")


class _HwL2IfPwSuppressionCbs_Type(Integer32):
    """Custom type hwL2IfPwSuppressionCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 33554432),
    )


_HwL2IfPwSuppressionCbs_Type.__name__ = "Integer32"
_HwL2IfPwSuppressionCbs_Object = MibTableColumn
hwL2IfPwSuppressionCbs = _HwL2IfPwSuppressionCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1, 5),
    _HwL2IfPwSuppressionCbs_Type()
)
hwL2IfPwSuppressionCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionCbs.setStatus("current")
_HwL2IfPwSuppressionRowStatus_Type = RowStatus
_HwL2IfPwSuppressionRowStatus_Object = MibTableColumn
hwL2IfPwSuppressionRowStatus = _HwL2IfPwSuppressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 17, 1, 50),
    _HwL2IfPwSuppressionRowStatus_Type()
)
hwL2IfPwSuppressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionRowStatus.setStatus("current")


class _HwL2IfLoopDetectInterval_Type(Integer32):
    """Custom type hwL2IfLoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HwL2IfLoopDetectInterval_Type.__name__ = "Integer32"
_HwL2IfLoopDetectInterval_Object = MibScalar
hwL2IfLoopDetectInterval = _HwL2IfLoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 18),
    _HwL2IfLoopDetectInterval_Type()
)
hwL2IfLoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfLoopDetectInterval.setStatus("current")
_HwL2IfDynamicPortVlanTable_Object = MibTable
hwL2IfDynamicPortVlanTable = _HwL2IfDynamicPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanTable.setStatus("current")
_HwL2IfDynamicPortVlanEntry_Object = MibTableRow
hwL2IfDynamicPortVlanEntry = _HwL2IfDynamicPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1)
)
hwL2IfDynamicPortVlanEntry.setIndexNames(
    (0, "HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanPortIndex"),
    (0, "HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanServiceType"),
)
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanEntry.setStatus("current")


class _HwL2IfDynamicPortVlanPortIndex_Type(Integer32):
    """Custom type hwL2IfDynamicPortVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2IfDynamicPortVlanPortIndex_Type.__name__ = "Integer32"
_HwL2IfDynamicPortVlanPortIndex_Object = MibTableColumn
hwL2IfDynamicPortVlanPortIndex = _HwL2IfDynamicPortVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 1),
    _HwL2IfDynamicPortVlanPortIndex_Type()
)
hwL2IfDynamicPortVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanPortIndex.setStatus("current")


class _HwL2IfDynamicPortVlanServiceType_Type(Integer32):
    """Custom type hwL2IfDynamicPortVlanServiceType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("dynAuthenVLAN", 5),
          ("elmi", 7),
          ("gvrp", 2),
          ("hvrp", 6),
          ("loopDetection", 10),
          ("loopbackDetect", 9),
          ("macFlapping", 8),
          ("unAuthenUserVLAN", 4),
          ("voiceVLAN", 3))
    )


_HwL2IfDynamicPortVlanServiceType_Type.__name__ = "Integer32"
_HwL2IfDynamicPortVlanServiceType_Object = MibTableColumn
hwL2IfDynamicPortVlanServiceType = _HwL2IfDynamicPortVlanServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 2),
    _HwL2IfDynamicPortVlanServiceType_Type()
)
hwL2IfDynamicPortVlanServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanServiceType.setStatus("current")
_HwL2IfDynamicPortVlanPvid_Type = VlanIdOrNone
_HwL2IfDynamicPortVlanPvid_Object = MibTableColumn
hwL2IfDynamicPortVlanPvid = _HwL2IfDynamicPortVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 3),
    _HwL2IfDynamicPortVlanPvid_Type()
)
hwL2IfDynamicPortVlanPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanPvid.setStatus("current")


class _HwL2IfDynamicPortVlanUntaggedVlanListLow_Type(VlanList):
    """Custom type hwL2IfDynamicPortVlanUntaggedVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfDynamicPortVlanUntaggedVlanListLow_Type.__name__ = "VlanList"
_HwL2IfDynamicPortVlanUntaggedVlanListLow_Object = MibTableColumn
hwL2IfDynamicPortVlanUntaggedVlanListLow = _HwL2IfDynamicPortVlanUntaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 4),
    _HwL2IfDynamicPortVlanUntaggedVlanListLow_Type()
)
hwL2IfDynamicPortVlanUntaggedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanUntaggedVlanListLow.setStatus("current")


class _HwL2IfDynamicPortVlanUntaggedVlanListHigh_Type(VlanList):
    """Custom type hwL2IfDynamicPortVlanUntaggedVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfDynamicPortVlanUntaggedVlanListHigh_Type.__name__ = "VlanList"
_HwL2IfDynamicPortVlanUntaggedVlanListHigh_Object = MibTableColumn
hwL2IfDynamicPortVlanUntaggedVlanListHigh = _HwL2IfDynamicPortVlanUntaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 5),
    _HwL2IfDynamicPortVlanUntaggedVlanListHigh_Type()
)
hwL2IfDynamicPortVlanUntaggedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanUntaggedVlanListHigh.setStatus("current")


class _HwL2IfDynamicPortVlanTaggedVlanListLow_Type(VlanList):
    """Custom type hwL2IfDynamicPortVlanTaggedVlanListLow based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfDynamicPortVlanTaggedVlanListLow_Type.__name__ = "VlanList"
_HwL2IfDynamicPortVlanTaggedVlanListLow_Object = MibTableColumn
hwL2IfDynamicPortVlanTaggedVlanListLow = _HwL2IfDynamicPortVlanTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 6),
    _HwL2IfDynamicPortVlanTaggedVlanListLow_Type()
)
hwL2IfDynamicPortVlanTaggedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanTaggedVlanListLow.setStatus("current")


class _HwL2IfDynamicPortVlanTaggedVlanListHigh_Type(VlanList):
    """Custom type hwL2IfDynamicPortVlanTaggedVlanListHigh based on VlanList"""
    subtypeSpec = VlanList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IfDynamicPortVlanTaggedVlanListHigh_Type.__name__ = "VlanList"
_HwL2IfDynamicPortVlanTaggedVlanListHigh_Object = MibTableColumn
hwL2IfDynamicPortVlanTaggedVlanListHigh = _HwL2IfDynamicPortVlanTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 1, 19, 1, 7),
    _HwL2IfDynamicPortVlanTaggedVlanListHigh_Type()
)
hwL2IfDynamicPortVlanTaggedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanTaggedVlanListHigh.setStatus("current")
_HwL2IfTraps_ObjectIdentity = ObjectIdentity
hwL2IfTraps = _HwL2IfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 2)
)
_HwL2IfConformance_ObjectIdentity = ObjectIdentity
hwL2IfConformance = _HwL2IfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2)
)
_HwL2IfCompliances_ObjectIdentity = ObjectIdentity
hwL2IfCompliances = _HwL2IfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 1)
)
_HwL2IfGroups_ObjectIdentity = ObjectIdentity
hwL2IfGroups = _HwL2IfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2)
)

# Managed Objects groups

hwL2IfMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 1)
)
hwL2IfMacAddrGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfMacAddrLearnMode"),
        ("HUAWEI-L2IF-MIB", "hwL2IfMacAddressLearn"))
)
if mibBuilder.loadTexts:
    hwL2IfMacAddrGroup.setStatus("current")

hwL2IfBroadcastRatioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 2)
)
hwL2IfBroadcastRatioGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfBcastRatio"),
        ("HUAWEI-L2IF-MIB", "hwL2IfMcastRatio"),
        ("HUAWEI-L2IF-MIB", "hwL2IfUcastRatio"),
        ("HUAWEI-L2IF-MIB", "hwL2IfOutBcastRatio"),
        ("HUAWEI-L2IF-MIB", "hwL2IfOutMcastRatio"),
        ("HUAWEI-L2IF-MIB", "hwL2IfOutUcastRatio"))
)
if mibBuilder.loadTexts:
    hwL2IfBroadcastRatioGroup.setStatus("current")

hwL2IfHybridTaggedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 3)
)
hwL2IfHybridTaggedVlanGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfHybridTaggedVlanListLow"),
        ("HUAWEI-L2IF-MIB", "hwL2IfHybridTaggedVlanListHigh"),
        ("HUAWEI-L2IF-MIB", "hwL2IfHybridUnTaggedVlanListLow"),
        ("HUAWEI-L2IF-MIB", "hwL2IfHybridUnTaggedVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwL2IfHybridTaggedVlanGroup.setStatus("current")

hwL2IfTrunkAllowPassVlanListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 4)
)
hwL2IfTrunkAllowPassVlanListGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfTrunkAllowPassVlanListLow"),
        ("HUAWEI-L2IF-MIB", "hwL2IfTrunkAllowPassVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwL2IfTrunkAllowPassVlanListGroup.setStatus("current")

hwL2IfPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 5)
)
hwL2IfPortGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfPortIfIndex"),
        ("HUAWEI-L2IF-MIB", "hwL2IfIsSrcMacFilter"))
)
if mibBuilder.loadTexts:
    hwL2IfPortGroup.setStatus("current")

hwL2IfPVIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 6)
)
hwL2IfPVIDGroup.setObjects(
    ("HUAWEI-L2IF-MIB", "hwL2IfPVID")
)
if mibBuilder.loadTexts:
    hwL2IfPVIDGroup.setStatus("current")

hwL2IfPortTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 7)
)
hwL2IfPortTypeGroup.setObjects(
    ("HUAWEI-L2IF-MIB", "hwL2IfPortType")
)
if mibBuilder.loadTexts:
    hwL2IfPortTypeGroup.setStatus("current")

hwL2IfPortMaxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 8)
)
hwL2IfPortMaxGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfPortMax"),
        ("HUAWEI-L2IF-MIB", "hwL2TopologyDetect"))
)
if mibBuilder.loadTexts:
    hwL2IfPortMaxGroup.setStatus("current")

hwL2IfPortExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 9)
)
hwL2IfPortExtGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfBpdu"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDiscardBcast"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDiscardUnknownMcast"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDiscardUnknownUcast"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortPriority"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"),
        ("HUAWEI-L2IF-MIB", "hwL2IfInInvalidVlanPkts"),
        ("HUAWEI-L2IF-MIB", "hwL2IfFlushEnable"),
        ("HUAWEI-L2IF-MIB", "hwL2IfFlushControlVlan"),
        ("HUAWEI-L2IF-MIB", "hwL2IfCurrentInBcastPercent"),
        ("HUAWEI-L2IF-MIB", "hwL2IfCurrentOutBcastPercent"),
        ("HUAWEI-L2IF-MIB", "hwL2IfQinqVlanTransEnable"),
        ("HUAWEI-L2IF-MIB", "hwL2IfQinqVlanTransMissDrop"),
        ("HUAWEI-L2IF-MIB", "hwL2IfIpSubnetVlanEnable"),
        ("HUAWEI-L2IF-MIB", "hwL2IfMacVlanEnable"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPolicyVlanEnable"),
        ("HUAWEI-L2IF-MIB", "hwL2IfVlanPrecedence"),
        ("HUAWEI-L2IF-MIB", "hwL2IfIsolateGroupEnable"))
)
if mibBuilder.loadTexts:
    hwL2IfPortExtGroup.setStatus("current")

hwL2IfPortIsolateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 10)
)
hwL2IfPortIsolateGroup.setObjects(
    ("HUAWEI-L2IF-MIB", "hwL2IfPortIsolateRowStatus")
)
if mibBuilder.loadTexts:
    hwL2IfPortIsolateGroup.setStatus("current")

hwL2IfSuppressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 12)
)
hwL2IfSuppressionGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfSuppressionCir"),
        ("HUAWEI-L2IF-MIB", "hwL2IfSuppressionCbs"),
        ("HUAWEI-L2IF-MIB", "hwL2IfSuppressionRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfSuppressionGroup.setStatus("current")

hwL2IfVlanSuppressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 13)
)
hwL2IfVlanSuppressionGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfVlanSuppressionCir"),
        ("HUAWEI-L2IF-MIB", "hwL2IfVlanSuppressionCbs"),
        ("HUAWEI-L2IF-MIB", "hwL2IfVlanSuppressionRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfVlanSuppressionGroup.setStatus("current")

hwL2IfPortTcnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 14)
)
hwL2IfPortTcnGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfTcnStp"),
        ("HUAWEI-L2IF-MIB", "hwL2IfTcnSmartLink"),
        ("HUAWEI-L2IF-MIB", "hwL2IfTcnVlanListLow"),
        ("HUAWEI-L2IF-MIB", "hwL2IfTcnVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwL2IfPortTcnGroup.setStatus("current")

hwL2IfPortLoopDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 15)
)
hwL2IfPortLoopDetectGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectEnabled"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectInterval"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectAction"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectStatus"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectProtocol"),
        ("HUAWEI-L2IF-MIB", "hwL2IfLoopDetectInterval"))
)
if mibBuilder.loadTexts:
    hwL2IfPortLoopDetectGroup.setStatus("current")

hwL2IfPortProtocolVlanDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 16)
)
hwL2IfPortProtocolVlanDataGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfPortProtocolVlanDataVlan"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortProtocolVlanDataPri"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortProtocolVlanDataRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfPortProtocolVlanDataGroup.setStatus("current")

hwL2IfPwSuppressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 17)
)
hwL2IfPwSuppressionGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfPwSuppressionCir"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPwSuppressionCbs"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPwSuppressionRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfPwSuppressionGroup.setStatus("current")

hwL2IfDynamicPortVlanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 19)
)
hwL2IfDynamicPortVlanTableGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanPvid"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanUntaggedVlanListLow"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanUntaggedVlanListHigh"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanTaggedVlanListLow"),
        ("HUAWEI-L2IF-MIB", "hwL2IfDynamicPortVlanTaggedVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwL2IfDynamicPortVlanTableGroup.setStatus("current")


# Notification objects

hwL2IfInvalidVlanPacketAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 2, 1)
)
hwL2IfInvalidVlanPacketAlarm.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfPortName"),
        ("HUAWEI-L2IF-MIB", "hwL2IfInInvalidVlanPkts"))
)
if mibBuilder.loadTexts:
    hwL2IfInvalidVlanPacketAlarm.setStatus(
        "current"
    )

hwInBcastRisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 1, 2, 2)
)
hwInBcastRisingThreshold.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortLoopDetectStatus"))
)
if mibBuilder.loadTexts:
    hwInBcastRisingThreshold.setStatus(
        "current"
    )


# Notifications groups

hwL2IfAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 2, 11)
)
hwL2IfAlarmGroup.setObjects(
      *(("HUAWEI-L2IF-MIB", "hwL2IfInvalidVlanPacketAlarm"),
        ("HUAWEI-L2IF-MIB", "hwInBcastRisingThreshold"))
)
if mibBuilder.loadTexts:
    hwL2IfAlarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwL2IfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwL2IfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2IF-MIB",
    **{"VlanList": VlanList,
       "hwL2Mgmt": hwL2Mgmt,
       "hwL2IfMib": hwL2IfMib,
       "hwL2IfObjects": hwL2IfObjects,
       "hwL2Interface": hwL2Interface,
       "hwL2IfPortMax": hwL2IfPortMax,
       "hwL2TopologyDetect": hwL2TopologyDetect,
       "hwL2IfTable": hwL2IfTable,
       "hwL2IfEntry": hwL2IfEntry,
       "hwL2IfPortNum": hwL2IfPortNum,
       "hwL2IfPortIfIndex": hwL2IfPortIfIndex,
       "hwL2IfPortType": hwL2IfPortType,
       "hwL2IfPVID": hwL2IfPVID,
       "hwL2IfIsSrcMacFilter": hwL2IfIsSrcMacFilter,
       "hwL2IfMacAddrLearnMode": hwL2IfMacAddrLearnMode,
       "hwL2IfMacAddressLearn": hwL2IfMacAddressLearn,
       "hwL2IfBcastRatio": hwL2IfBcastRatio,
       "hwL2IfMcastRatio": hwL2IfMcastRatio,
       "hwL2IfUcastRatio": hwL2IfUcastRatio,
       "hwL2IfOutBcastRatio": hwL2IfOutBcastRatio,
       "hwL2IfOutMcastRatio": hwL2IfOutMcastRatio,
       "hwL2IfOutUcastRatio": hwL2IfOutUcastRatio,
       "hwL2IfDiscardBcast": hwL2IfDiscardBcast,
       "hwL2IfDiscardUnknownMcast": hwL2IfDiscardUnknownMcast,
       "hwL2IfDiscardUnknownUcast": hwL2IfDiscardUnknownUcast,
       "hwL2IfBpdu": hwL2IfBpdu,
       "hwL2IfPortPriority": hwL2IfPortPriority,
       "hwL2IfPortName": hwL2IfPortName,
       "hwL2IfInInvalidVlanPkts": hwL2IfInInvalidVlanPkts,
       "hwL2IfFlushEnable": hwL2IfFlushEnable,
       "hwL2IfFlushControlVlan": hwL2IfFlushControlVlan,
       "hwL2IfCurrentInBcastPercent": hwL2IfCurrentInBcastPercent,
       "hwL2IfCurrentOutBcastPercent": hwL2IfCurrentOutBcastPercent,
       "hwL2IfQinqVlanTransEnable": hwL2IfQinqVlanTransEnable,
       "hwL2IfQinqVlanTransMissDrop": hwL2IfQinqVlanTransMissDrop,
       "hwL2IfIpSubnetVlanEnable": hwL2IfIpSubnetVlanEnable,
       "hwL2IfMacVlanEnable": hwL2IfMacVlanEnable,
       "hwL2IfPolicyVlanEnable": hwL2IfPolicyVlanEnable,
       "hwL2IfVlanPrecedence": hwL2IfVlanPrecedence,
       "hwL2IfIsolateGroupEnable": hwL2IfIsolateGroupEnable,
       "hwL2IfHybridPortTable": hwL2IfHybridPortTable,
       "hwL2IfHybridPortEntry": hwL2IfHybridPortEntry,
       "hwL2IfHybridPortIndex": hwL2IfHybridPortIndex,
       "hwL2IfHybridTaggedVlanListLow": hwL2IfHybridTaggedVlanListLow,
       "hwL2IfHybridTaggedVlanListHigh": hwL2IfHybridTaggedVlanListHigh,
       "hwL2IfHybridUnTaggedVlanListLow": hwL2IfHybridUnTaggedVlanListLow,
       "hwL2IfHybridUnTaggedVlanListHigh": hwL2IfHybridUnTaggedVlanListHigh,
       "hwL2IfTrunkPortTable": hwL2IfTrunkPortTable,
       "hwL2IfTrunkPortEntry": hwL2IfTrunkPortEntry,
       "hwL2IfTrunkPortIndex": hwL2IfTrunkPortIndex,
       "hwL2IfTrunkAllowPassVlanListLow": hwL2IfTrunkAllowPassVlanListLow,
       "hwL2IfTrunkAllowPassVlanListHigh": hwL2IfTrunkAllowPassVlanListHigh,
       "hwL2IfPortIsolateTable": hwL2IfPortIsolateTable,
       "hwL2IfPortIsolateEntry": hwL2IfPortIsolateEntry,
       "hwL2IfPortIsolatePortIndex": hwL2IfPortIsolatePortIndex,
       "hwL2IfPortIsolateSIName": hwL2IfPortIsolateSIName,
       "hwL2IfPortIsolateRowStatus": hwL2IfPortIsolateRowStatus,
       "hwL2IfSuppressionTable": hwL2IfSuppressionTable,
       "hwL2IfSuppressionEntry": hwL2IfSuppressionEntry,
       "hwL2IfSuppressionPortIndex": hwL2IfSuppressionPortIndex,
       "hwL2IfSuppressionType": hwL2IfSuppressionType,
       "hwL2IfSuppressionCir": hwL2IfSuppressionCir,
       "hwL2IfSuppressionCbs": hwL2IfSuppressionCbs,
       "hwL2IfSuppressionRowStatus": hwL2IfSuppressionRowStatus,
       "hwL2IfVlanSuppressionTable": hwL2IfVlanSuppressionTable,
       "hwL2IfVlanSuppressionEntry": hwL2IfVlanSuppressionEntry,
       "hwL2IfVlanSuppressionPortIndex": hwL2IfVlanSuppressionPortIndex,
       "hwL2IfVlanSuppressionStartVlan": hwL2IfVlanSuppressionStartVlan,
       "hwL2IfVlanSuppressionEndVlan": hwL2IfVlanSuppressionEndVlan,
       "hwL2IfVlanSuppressionCir": hwL2IfVlanSuppressionCir,
       "hwL2IfVlanSuppressionCbs": hwL2IfVlanSuppressionCbs,
       "hwL2IfVlanSuppressionRowStatus": hwL2IfVlanSuppressionRowStatus,
       "hwL2IfPortTcnTable": hwL2IfPortTcnTable,
       "hwL2IfPortTcnEntry": hwL2IfPortTcnEntry,
       "hwL2IfTcnPortIndex": hwL2IfTcnPortIndex,
       "hwL2IfTcnStp": hwL2IfTcnStp,
       "hwL2IfTcnSmartLink": hwL2IfTcnSmartLink,
       "hwL2IfTcnVlanListLow": hwL2IfTcnVlanListLow,
       "hwL2IfTcnVlanListHigh": hwL2IfTcnVlanListHigh,
       "hwL2IfPortLoopDetectTable": hwL2IfPortLoopDetectTable,
       "hwL2IfPortLoopDetectEntry": hwL2IfPortLoopDetectEntry,
       "hwL2IfPortLoopDetectPort": hwL2IfPortLoopDetectPort,
       "hwL2IfPortLoopDetectEnabled": hwL2IfPortLoopDetectEnabled,
       "hwL2IfPortLoopDetectInterval": hwL2IfPortLoopDetectInterval,
       "hwL2IfPortLoopDetectAction": hwL2IfPortLoopDetectAction,
       "hwL2IfPortLoopDetectStatus": hwL2IfPortLoopDetectStatus,
       "hwL2IfPortLoopDetectProtocol": hwL2IfPortLoopDetectProtocol,
       "hwL2IfPortProtocolVlanDataTable": hwL2IfPortProtocolVlanDataTable,
       "hwL2IfPortProtocolVlanDataEntry": hwL2IfPortProtocolVlanDataEntry,
       "hwL2IfPortProtocolVlanDataPortIndex": hwL2IfPortProtocolVlanDataPortIndex,
       "hwL2IfPortProtocolVlanDataVlan": hwL2IfPortProtocolVlanDataVlan,
       "hwL2IfPortProtocolVlanDataPri": hwL2IfPortProtocolVlanDataPri,
       "hwL2IfPortProtocolVlanDataRowStatus": hwL2IfPortProtocolVlanDataRowStatus,
       "hwL2IfPwSuppressionTable": hwL2IfPwSuppressionTable,
       "hwL2IfPwSuppressionEntry": hwL2IfPwSuppressionEntry,
       "hwL2IfPwSuppressionVsiName": hwL2IfPwSuppressionVsiName,
       "hwL2IfPwSuppressionPwName": hwL2IfPwSuppressionPwName,
       "hwL2IfPwSuppressionType": hwL2IfPwSuppressionType,
       "hwL2IfPwSuppressionCir": hwL2IfPwSuppressionCir,
       "hwL2IfPwSuppressionCbs": hwL2IfPwSuppressionCbs,
       "hwL2IfPwSuppressionRowStatus": hwL2IfPwSuppressionRowStatus,
       "hwL2IfLoopDetectInterval": hwL2IfLoopDetectInterval,
       "hwL2IfDynamicPortVlanTable": hwL2IfDynamicPortVlanTable,
       "hwL2IfDynamicPortVlanEntry": hwL2IfDynamicPortVlanEntry,
       "hwL2IfDynamicPortVlanPortIndex": hwL2IfDynamicPortVlanPortIndex,
       "hwL2IfDynamicPortVlanServiceType": hwL2IfDynamicPortVlanServiceType,
       "hwL2IfDynamicPortVlanPvid": hwL2IfDynamicPortVlanPvid,
       "hwL2IfDynamicPortVlanUntaggedVlanListLow": hwL2IfDynamicPortVlanUntaggedVlanListLow,
       "hwL2IfDynamicPortVlanUntaggedVlanListHigh": hwL2IfDynamicPortVlanUntaggedVlanListHigh,
       "hwL2IfDynamicPortVlanTaggedVlanListLow": hwL2IfDynamicPortVlanTaggedVlanListLow,
       "hwL2IfDynamicPortVlanTaggedVlanListHigh": hwL2IfDynamicPortVlanTaggedVlanListHigh,
       "hwL2IfTraps": hwL2IfTraps,
       "hwL2IfInvalidVlanPacketAlarm": hwL2IfInvalidVlanPacketAlarm,
       "hwInBcastRisingThreshold": hwInBcastRisingThreshold,
       "hwL2IfConformance": hwL2IfConformance,
       "hwL2IfCompliances": hwL2IfCompliances,
       "hwL2IfCompliance": hwL2IfCompliance,
       "hwL2IfGroups": hwL2IfGroups,
       "hwL2IfMacAddrGroup": hwL2IfMacAddrGroup,
       "hwL2IfBroadcastRatioGroup": hwL2IfBroadcastRatioGroup,
       "hwL2IfHybridTaggedVlanGroup": hwL2IfHybridTaggedVlanGroup,
       "hwL2IfTrunkAllowPassVlanListGroup": hwL2IfTrunkAllowPassVlanListGroup,
       "hwL2IfPortGroup": hwL2IfPortGroup,
       "hwL2IfPVIDGroup": hwL2IfPVIDGroup,
       "hwL2IfPortTypeGroup": hwL2IfPortTypeGroup,
       "hwL2IfPortMaxGroup": hwL2IfPortMaxGroup,
       "hwL2IfPortExtGroup": hwL2IfPortExtGroup,
       "hwL2IfPortIsolateGroup": hwL2IfPortIsolateGroup,
       "hwL2IfAlarmGroup": hwL2IfAlarmGroup,
       "hwL2IfSuppressionGroup": hwL2IfSuppressionGroup,
       "hwL2IfVlanSuppressionGroup": hwL2IfVlanSuppressionGroup,
       "hwL2IfPortTcnGroup": hwL2IfPortTcnGroup,
       "hwL2IfPortLoopDetectGroup": hwL2IfPortLoopDetectGroup,
       "hwL2IfPortProtocolVlanDataGroup": hwL2IfPortProtocolVlanDataGroup,
       "hwL2IfPwSuppressionGroup": hwL2IfPwSuppressionGroup,
       "hwL2IfDynamicPortVlanTableGroup": hwL2IfDynamicPortVlanTableGroup}
)
