# SNMP MIB module (SMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:30 2024
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

(IbDataPort,
 IbDataPortAndInvalid,
 IbGuid,
 IbMulticastLid,
 IbSmPortList,
 IbUnicastLid,
 infinibandMIB) = mibBuilder.importSymbols(
    "IB-TC-MIB",
    "IbDataPort",
    "IbDataPortAndInvalid",
    "IbGuid",
    "IbMulticastLid",
    "IbSmPortList",
    "IbUnicastLid",
    "infinibandMIB")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ibSmaMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 117, 3)
)
ibSmaMIB.setRevisions(
        ("2003-06-06 12:00",
         "2003-01-01 12:00",
         "2002-09-16 12:00",
         "2002-07-31 12:00",
         "2002-07-18 12:00",
         "2002-05-10 12:00",
         "2002-03-01 12:00",
         "2001-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbSmaObjects_ObjectIdentity = ObjectIdentity
ibSmaObjects = _IbSmaObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1)
)
_IbSmaNodeInfo_ObjectIdentity = ObjectIdentity
ibSmaNodeInfo = _IbSmaNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 1)
)


class _IbSmaNodeString_Type(DisplayString):
    """Custom type ibSmaNodeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IbSmaNodeString_Type.__name__ = "DisplayString"
_IbSmaNodeString_Object = MibScalar
ibSmaNodeString = _IbSmaNodeString_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 1),
    _IbSmaNodeString_Type()
)
ibSmaNodeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeString.setStatus("current")


class _IbSmaNodeBaseVersion_Type(Integer32):
    """Custom type ibSmaNodeBaseVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbSmaNodeBaseVersion_Type.__name__ = "Integer32"
_IbSmaNodeBaseVersion_Object = MibScalar
ibSmaNodeBaseVersion = _IbSmaNodeBaseVersion_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 2),
    _IbSmaNodeBaseVersion_Type()
)
ibSmaNodeBaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeBaseVersion.setStatus("current")


class _IbSmaNodeClassVersion_Type(Integer32):
    """Custom type ibSmaNodeClassVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbSmaNodeClassVersion_Type.__name__ = "Integer32"
_IbSmaNodeClassVersion_Object = MibScalar
ibSmaNodeClassVersion = _IbSmaNodeClassVersion_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 3),
    _IbSmaNodeClassVersion_Type()
)
ibSmaNodeClassVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeClassVersion.setStatus("current")


class _IbSmaNodeType_Type(Integer32):
    """Custom type ibSmaNodeType based on Integer32"""
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
        *(("channelAdapter", 1),
          ("other", 4),
          ("router", 3),
          ("switch", 2))
    )


_IbSmaNodeType_Type.__name__ = "Integer32"
_IbSmaNodeType_Object = MibScalar
ibSmaNodeType = _IbSmaNodeType_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 4),
    _IbSmaNodeType_Type()
)
ibSmaNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeType.setStatus("current")


class _IbSmaNodeNumPorts_Type(Integer32):
    """Custom type ibSmaNodeNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbSmaNodeNumPorts_Type.__name__ = "Integer32"
_IbSmaNodeNumPorts_Object = MibScalar
ibSmaNodeNumPorts = _IbSmaNodeNumPorts_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 5),
    _IbSmaNodeNumPorts_Type()
)
ibSmaNodeNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeNumPorts.setStatus("current")
_IbSmaSystemImageGuid_Type = IbGuid
_IbSmaSystemImageGuid_Object = MibScalar
ibSmaSystemImageGuid = _IbSmaSystemImageGuid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 6),
    _IbSmaSystemImageGuid_Type()
)
ibSmaSystemImageGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSystemImageGuid.setStatus("current")
_IbSmaNodeGuid_Type = IbGuid
_IbSmaNodeGuid_Object = MibScalar
ibSmaNodeGuid = _IbSmaNodeGuid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 7),
    _IbSmaNodeGuid_Type()
)
ibSmaNodeGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeGuid.setStatus("current")
_IbSmaNodePortGuid_Type = IbGuid
_IbSmaNodePortGuid_Object = MibScalar
ibSmaNodePortGuid = _IbSmaNodePortGuid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 8),
    _IbSmaNodePortGuid_Type()
)
ibSmaNodePortGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodePortGuid.setStatus("current")


class _IbSmaNodePartitionTableNum_Type(Integer32):
    """Custom type ibSmaNodePartitionTableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbSmaNodePartitionTableNum_Type.__name__ = "Integer32"
_IbSmaNodePartitionTableNum_Object = MibScalar
ibSmaNodePartitionTableNum = _IbSmaNodePartitionTableNum_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 9),
    _IbSmaNodePartitionTableNum_Type()
)
ibSmaNodePartitionTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodePartitionTableNum.setStatus("current")


class _IbSmaNodeDeviceId_Type(OctetString):
    """Custom type ibSmaNodeDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbSmaNodeDeviceId_Type.__name__ = "OctetString"
_IbSmaNodeDeviceId_Object = MibScalar
ibSmaNodeDeviceId = _IbSmaNodeDeviceId_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 10),
    _IbSmaNodeDeviceId_Type()
)
ibSmaNodeDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeDeviceId.setStatus("current")


class _IbSmaNodeRevision_Type(OctetString):
    """Custom type ibSmaNodeRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbSmaNodeRevision_Type.__name__ = "OctetString"
_IbSmaNodeRevision_Object = MibScalar
ibSmaNodeRevision = _IbSmaNodeRevision_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 11),
    _IbSmaNodeRevision_Type()
)
ibSmaNodeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeRevision.setStatus("current")


class _IbSmaNodeLocalPortNumOrZero_Type(Integer32):
    """Custom type ibSmaNodeLocalPortNumOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_IbSmaNodeLocalPortNumOrZero_Type.__name__ = "Integer32"
_IbSmaNodeLocalPortNumOrZero_Object = MibScalar
ibSmaNodeLocalPortNumOrZero = _IbSmaNodeLocalPortNumOrZero_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 12),
    _IbSmaNodeLocalPortNumOrZero_Type()
)
ibSmaNodeLocalPortNumOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeLocalPortNumOrZero.setStatus("current")


class _IbSmaNodeVendorId_Type(OctetString):
    """Custom type ibSmaNodeVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbSmaNodeVendorId_Type.__name__ = "OctetString"
_IbSmaNodeVendorId_Object = MibScalar
ibSmaNodeVendorId = _IbSmaNodeVendorId_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 13),
    _IbSmaNodeVendorId_Type()
)
ibSmaNodeVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaNodeVendorId.setStatus("current")


class _IbSmaNodeLid_Type(Integer32):
    """Custom type ibSmaNodeLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaNodeLid_Type.__name__ = "Integer32"
_IbSmaNodeLid_Object = MibScalar
ibSmaNodeLid = _IbSmaNodeLid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 14),
    _IbSmaNodeLid_Type()
)
ibSmaNodeLid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeLid.setStatus("current")
_IbSmaNodePortNum_Type = IbDataPort
_IbSmaNodePortNum_Object = MibScalar
ibSmaNodePortNum = _IbSmaNodePortNum_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 15),
    _IbSmaNodePortNum_Type()
)
ibSmaNodePortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodePortNum.setStatus("current")


class _IbSmaNodeMethod_Type(Integer32):
    """Custom type ibSmaNodeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbSmaNodeMethod_Type.__name__ = "Integer32"
_IbSmaNodeMethod_Object = MibScalar
ibSmaNodeMethod = _IbSmaNodeMethod_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 16),
    _IbSmaNodeMethod_Type()
)
ibSmaNodeMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeMethod.setStatus("current")


class _IbSmaNodeAttributeId_Type(Unsigned32):
    """Custom type ibSmaNodeAttributeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaNodeAttributeId_Type.__name__ = "Unsigned32"
_IbSmaNodeAttributeId_Object = MibScalar
ibSmaNodeAttributeId = _IbSmaNodeAttributeId_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 17),
    _IbSmaNodeAttributeId_Type()
)
ibSmaNodeAttributeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeAttributeId.setStatus("current")


class _IbSmaNodeAttributeModifier_Type(Unsigned32):
    """Custom type ibSmaNodeAttributeModifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IbSmaNodeAttributeModifier_Type.__name__ = "Unsigned32"
_IbSmaNodeAttributeModifier_Object = MibScalar
ibSmaNodeAttributeModifier = _IbSmaNodeAttributeModifier_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 18),
    _IbSmaNodeAttributeModifier_Type()
)
ibSmaNodeAttributeModifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeAttributeModifier.setStatus("current")


class _IbSmaNodeKey_Type(OctetString):
    """Custom type ibSmaNodeKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbSmaNodeKey_Type.__name__ = "OctetString"
_IbSmaNodeKey_Object = MibScalar
ibSmaNodeKey = _IbSmaNodeKey_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 19),
    _IbSmaNodeKey_Type()
)
ibSmaNodeKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeKey.setStatus("current")


class _IbSmaNodeLid2_Type(Integer32):
    """Custom type ibSmaNodeLid2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaNodeLid2_Type.__name__ = "Integer32"
_IbSmaNodeLid2_Object = MibScalar
ibSmaNodeLid2 = _IbSmaNodeLid2_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 20),
    _IbSmaNodeLid2_Type()
)
ibSmaNodeLid2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeLid2.setStatus("current")


class _IbSmaNodeServiceLevel_Type(Integer32):
    """Custom type ibSmaNodeServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbSmaNodeServiceLevel_Type.__name__ = "Integer32"
_IbSmaNodeServiceLevel_Object = MibScalar
ibSmaNodeServiceLevel = _IbSmaNodeServiceLevel_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 21),
    _IbSmaNodeServiceLevel_Type()
)
ibSmaNodeServiceLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeServiceLevel.setStatus("current")


class _IbSmaNodeQueuePair1_Type(Integer32):
    """Custom type ibSmaNodeQueuePair1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IbSmaNodeQueuePair1_Type.__name__ = "Integer32"
_IbSmaNodeQueuePair1_Object = MibScalar
ibSmaNodeQueuePair1 = _IbSmaNodeQueuePair1_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 22),
    _IbSmaNodeQueuePair1_Type()
)
ibSmaNodeQueuePair1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeQueuePair1.setStatus("current")


class _IbSmaNodeQueuePair2_Type(Integer32):
    """Custom type ibSmaNodeQueuePair2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IbSmaNodeQueuePair2_Type.__name__ = "Integer32"
_IbSmaNodeQueuePair2_Object = MibScalar
ibSmaNodeQueuePair2 = _IbSmaNodeQueuePair2_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 23),
    _IbSmaNodeQueuePair2_Type()
)
ibSmaNodeQueuePair2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeQueuePair2.setStatus("current")


class _IbSmaNodeGid1_Type(OctetString):
    """Custom type ibSmaNodeGid1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbSmaNodeGid1_Type.__name__ = "OctetString"
_IbSmaNodeGid1_Object = MibScalar
ibSmaNodeGid1 = _IbSmaNodeGid1_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 24),
    _IbSmaNodeGid1_Type()
)
ibSmaNodeGid1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeGid1.setStatus("current")


class _IbSmaNodeGid2_Type(OctetString):
    """Custom type ibSmaNodeGid2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbSmaNodeGid2_Type.__name__ = "OctetString"
_IbSmaNodeGid2_Object = MibScalar
ibSmaNodeGid2 = _IbSmaNodeGid2_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 25),
    _IbSmaNodeGid2_Type()
)
ibSmaNodeGid2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeGid2.setStatus("current")


class _IbSmaNodeCapMask_Type(OctetString):
    """Custom type ibSmaNodeCapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbSmaNodeCapMask_Type.__name__ = "OctetString"
_IbSmaNodeCapMask_Object = MibScalar
ibSmaNodeCapMask = _IbSmaNodeCapMask_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 26),
    _IbSmaNodeCapMask_Type()
)
ibSmaNodeCapMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeCapMask.setStatus("current")


class _IbSmaNodeSwitchLid_Type(Integer32):
    """Custom type ibSmaNodeSwitchLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaNodeSwitchLid_Type.__name__ = "Integer32"
_IbSmaNodeSwitchLid_Object = MibScalar
ibSmaNodeSwitchLid = _IbSmaNodeSwitchLid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 27),
    _IbSmaNodeSwitchLid_Type()
)
ibSmaNodeSwitchLid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeSwitchLid.setStatus("current")


class _IbSmaNodeDataValid_Type(OctetString):
    """Custom type ibSmaNodeDataValid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbSmaNodeDataValid_Type.__name__ = "OctetString"
_IbSmaNodeDataValid_Object = MibScalar
ibSmaNodeDataValid = _IbSmaNodeDataValid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 1, 28),
    _IbSmaNodeDataValid_Type()
)
ibSmaNodeDataValid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSmaNodeDataValid.setStatus("current")
_IbSmaSwitchInfo_ObjectIdentity = ObjectIdentity
ibSmaSwitchInfo = _IbSmaSwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 2)
)


class _IbSmaSwLinearFdbTableNum_Type(Integer32):
    """Custom type ibSmaSwLinearFdbTableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_IbSmaSwLinearFdbTableNum_Type.__name__ = "Integer32"
_IbSmaSwLinearFdbTableNum_Object = MibScalar
ibSmaSwLinearFdbTableNum = _IbSmaSwLinearFdbTableNum_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 1),
    _IbSmaSwLinearFdbTableNum_Type()
)
ibSmaSwLinearFdbTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwLinearFdbTableNum.setStatus("current")


class _IbSmaSwRandomFdbTableNum_Type(Integer32):
    """Custom type ibSmaSwRandomFdbTableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_IbSmaSwRandomFdbTableNum_Type.__name__ = "Integer32"
_IbSmaSwRandomFdbTableNum_Object = MibScalar
ibSmaSwRandomFdbTableNum = _IbSmaSwRandomFdbTableNum_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 2),
    _IbSmaSwRandomFdbTableNum_Type()
)
ibSmaSwRandomFdbTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwRandomFdbTableNum.setStatus("current")


class _IbSmaSwMulticastFdbTableNum_Type(Integer32):
    """Custom type ibSmaSwMulticastFdbTableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_IbSmaSwMulticastFdbTableNum_Type.__name__ = "Integer32"
_IbSmaSwMulticastFdbTableNum_Object = MibScalar
ibSmaSwMulticastFdbTableNum = _IbSmaSwMulticastFdbTableNum_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 3),
    _IbSmaSwMulticastFdbTableNum_Type()
)
ibSmaSwMulticastFdbTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwMulticastFdbTableNum.setStatus("current")


class _IbSmaSwLinearFdbTop_Type(Integer32):
    """Custom type ibSmaSwLinearFdbTop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_IbSmaSwLinearFdbTop_Type.__name__ = "Integer32"
_IbSmaSwLinearFdbTop_Object = MibScalar
ibSmaSwLinearFdbTop = _IbSmaSwLinearFdbTop_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 4),
    _IbSmaSwLinearFdbTop_Type()
)
ibSmaSwLinearFdbTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwLinearFdbTop.setStatus("current")


class _IbSmaSwDefaultPort_Type(Integer32):
    """Custom type ibSmaSwDefaultPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_IbSmaSwDefaultPort_Type.__name__ = "Integer32"
_IbSmaSwDefaultPort_Object = MibScalar
ibSmaSwDefaultPort = _IbSmaSwDefaultPort_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 5),
    _IbSmaSwDefaultPort_Type()
)
ibSmaSwDefaultPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwDefaultPort.setStatus("current")


class _IbSmaSwDefMcastPriPort_Type(Integer32):
    """Custom type ibSmaSwDefMcastPriPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_IbSmaSwDefMcastPriPort_Type.__name__ = "Integer32"
_IbSmaSwDefMcastPriPort_Object = MibScalar
ibSmaSwDefMcastPriPort = _IbSmaSwDefMcastPriPort_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 6),
    _IbSmaSwDefMcastPriPort_Type()
)
ibSmaSwDefMcastPriPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwDefMcastPriPort.setStatus("current")


class _IbSmaSwDefMcastNotPriPort_Type(Integer32):
    """Custom type ibSmaSwDefMcastNotPriPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_IbSmaSwDefMcastNotPriPort_Type.__name__ = "Integer32"
_IbSmaSwDefMcastNotPriPort_Object = MibScalar
ibSmaSwDefMcastNotPriPort = _IbSmaSwDefMcastNotPriPort_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 7),
    _IbSmaSwDefMcastNotPriPort_Type()
)
ibSmaSwDefMcastNotPriPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwDefMcastNotPriPort.setStatus("current")


class _IbSmaSwLifeTimeValue_Type(Integer32):
    """Custom type ibSmaSwLifeTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbSmaSwLifeTimeValue_Type.__name__ = "Integer32"
_IbSmaSwLifeTimeValue_Object = MibScalar
ibSmaSwLifeTimeValue = _IbSmaSwLifeTimeValue_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 8),
    _IbSmaSwLifeTimeValue_Type()
)
ibSmaSwLifeTimeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwLifeTimeValue.setStatus("current")


class _IbSmaSwPortStateChange_Type(Integer32):
    """Custom type ibSmaSwPortStateChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IbSmaSwPortStateChange_Type.__name__ = "Integer32"
_IbSmaSwPortStateChange_Object = MibScalar
ibSmaSwPortStateChange = _IbSmaSwPortStateChange_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 9),
    _IbSmaSwPortStateChange_Type()
)
ibSmaSwPortStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwPortStateChange.setStatus("current")


class _IbSmaSwLidsPerPort_Type(Integer32):
    """Custom type ibSmaSwLidsPerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaSwLidsPerPort_Type.__name__ = "Integer32"
_IbSmaSwLidsPerPort_Object = MibScalar
ibSmaSwLidsPerPort = _IbSmaSwLidsPerPort_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 10),
    _IbSmaSwLidsPerPort_Type()
)
ibSmaSwLidsPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwLidsPerPort.setStatus("current")


class _IbSmaSwPartitionEnforceNum_Type(Integer32):
    """Custom type ibSmaSwPartitionEnforceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaSwPartitionEnforceNum_Type.__name__ = "Integer32"
_IbSmaSwPartitionEnforceNum_Object = MibScalar
ibSmaSwPartitionEnforceNum = _IbSmaSwPartitionEnforceNum_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 11),
    _IbSmaSwPartitionEnforceNum_Type()
)
ibSmaSwPartitionEnforceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwPartitionEnforceNum.setStatus("current")
_IbSmaSwInboundEnforceCap_Type = TruthValue
_IbSmaSwInboundEnforceCap_Object = MibScalar
ibSmaSwInboundEnforceCap = _IbSmaSwInboundEnforceCap_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 12),
    _IbSmaSwInboundEnforceCap_Type()
)
ibSmaSwInboundEnforceCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwInboundEnforceCap.setStatus("current")
_IbSmaSwOutboundEnforceCap_Type = TruthValue
_IbSmaSwOutboundEnforceCap_Object = MibScalar
ibSmaSwOutboundEnforceCap = _IbSmaSwOutboundEnforceCap_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 13),
    _IbSmaSwOutboundEnforceCap_Type()
)
ibSmaSwOutboundEnforceCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwOutboundEnforceCap.setStatus("current")
_IbSmaSwFilterRawPktInputCap_Type = TruthValue
_IbSmaSwFilterRawPktInputCap_Object = MibScalar
ibSmaSwFilterRawPktInputCap = _IbSmaSwFilterRawPktInputCap_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 14),
    _IbSmaSwFilterRawPktInputCap_Type()
)
ibSmaSwFilterRawPktInputCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwFilterRawPktInputCap.setStatus("current")
_IbSmaSwFilterRawPktOutputCap_Type = TruthValue
_IbSmaSwFilterRawPktOutputCap_Object = MibScalar
ibSmaSwFilterRawPktOutputCap = _IbSmaSwFilterRawPktOutputCap_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 15),
    _IbSmaSwFilterRawPktOutputCap_Type()
)
ibSmaSwFilterRawPktOutputCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwFilterRawPktOutputCap.setStatus("current")
_IbSmaSwEnhancedPort0_Type = TruthValue
_IbSmaSwEnhancedPort0_Object = MibScalar
ibSmaSwEnhancedPort0 = _IbSmaSwEnhancedPort0_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 2, 16),
    _IbSmaSwEnhancedPort0_Type()
)
ibSmaSwEnhancedPort0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSwEnhancedPort0.setStatus("current")
_IbSmaGuidInfo_ObjectIdentity = ObjectIdentity
ibSmaGuidInfo = _IbSmaGuidInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 3)
)
_IbSmaGuidInfoTable_Object = MibTable
ibSmaGuidInfoTable = _IbSmaGuidInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ibSmaGuidInfoTable.setStatus("current")
_IbGuidInfoEntry_Object = MibTableRow
ibGuidInfoEntry = _IbGuidInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 3, 1, 1)
)
ibGuidInfoEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaGuidPortIndex"),
    (0, "SMA-MIB", "ibSmaGuidIndex"),
)
if mibBuilder.loadTexts:
    ibGuidInfoEntry.setStatus("current")
_IbSmaGuidPortIndex_Type = IbDataPort
_IbSmaGuidPortIndex_Object = MibTableColumn
ibSmaGuidPortIndex = _IbSmaGuidPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 3, 1, 1, 1),
    _IbSmaGuidPortIndex_Type()
)
ibSmaGuidPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaGuidPortIndex.setStatus("current")


class _IbSmaGuidIndex_Type(Integer32):
    """Custom type ibSmaGuidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbSmaGuidIndex_Type.__name__ = "Integer32"
_IbSmaGuidIndex_Object = MibTableColumn
ibSmaGuidIndex = _IbSmaGuidIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 3, 1, 1, 2),
    _IbSmaGuidIndex_Type()
)
ibSmaGuidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaGuidIndex.setStatus("current")
_IbSmaGuidVal_Type = IbGuid
_IbSmaGuidVal_Object = MibTableColumn
ibSmaGuidVal = _IbSmaGuidVal_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 3, 1, 1, 3),
    _IbSmaGuidVal_Type()
)
ibSmaGuidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaGuidVal.setStatus("current")
_IbSmaMgmtPortInfo_ObjectIdentity = ObjectIdentity
ibSmaMgmtPortInfo = _IbSmaMgmtPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 4)
)


class _IbSmaPortMKey_Type(OctetString):
    """Custom type ibSmaPortMKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbSmaPortMKey_Type.__name__ = "OctetString"
_IbSmaPortMKey_Object = MibScalar
ibSmaPortMKey = _IbSmaPortMKey_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 1),
    _IbSmaPortMKey_Type()
)
ibSmaPortMKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMKey.setStatus("current")


class _IbSmaPortGidPrefix_Type(OctetString):
    """Custom type ibSmaPortGidPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbSmaPortGidPrefix_Type.__name__ = "OctetString"
_IbSmaPortGidPrefix_Object = MibScalar
ibSmaPortGidPrefix = _IbSmaPortGidPrefix_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 2),
    _IbSmaPortGidPrefix_Type()
)
ibSmaPortGidPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortGidPrefix.setStatus("current")


class _IbSmaPortLid_Type(Integer32):
    """Custom type ibSmaPortLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_IbSmaPortLid_Type.__name__ = "Integer32"
_IbSmaPortLid_Object = MibScalar
ibSmaPortLid = _IbSmaPortLid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 3),
    _IbSmaPortLid_Type()
)
ibSmaPortLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLid.setStatus("current")


class _IbSmaPortMasterSmLid_Type(Integer32):
    """Custom type ibSmaPortMasterSmLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_IbSmaPortMasterSmLid_Type.__name__ = "Integer32"
_IbSmaPortMasterSmLid_Object = MibScalar
ibSmaPortMasterSmLid = _IbSmaPortMasterSmLid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 4),
    _IbSmaPortMasterSmLid_Type()
)
ibSmaPortMasterSmLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMasterSmLid.setStatus("current")
_IbSmaPortIsSubnetManager_Type = TruthValue
_IbSmaPortIsSubnetManager_Object = MibScalar
ibSmaPortIsSubnetManager = _IbSmaPortIsSubnetManager_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 5),
    _IbSmaPortIsSubnetManager_Type()
)
ibSmaPortIsSubnetManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsSubnetManager.setStatus("current")
_IbSmaPortIsNoticeSupported_Type = TruthValue
_IbSmaPortIsNoticeSupported_Object = MibScalar
ibSmaPortIsNoticeSupported = _IbSmaPortIsNoticeSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 6),
    _IbSmaPortIsNoticeSupported_Type()
)
ibSmaPortIsNoticeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsNoticeSupported.setStatus("current")
_IbSmaPortIsTrapSupported_Type = TruthValue
_IbSmaPortIsTrapSupported_Object = MibScalar
ibSmaPortIsTrapSupported = _IbSmaPortIsTrapSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 7),
    _IbSmaPortIsTrapSupported_Type()
)
ibSmaPortIsTrapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsTrapSupported.setStatus("current")
_IbSmaPortIsAutoMigrateSupported_Type = TruthValue
_IbSmaPortIsAutoMigrateSupported_Object = MibScalar
ibSmaPortIsAutoMigrateSupported = _IbSmaPortIsAutoMigrateSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 8),
    _IbSmaPortIsAutoMigrateSupported_Type()
)
ibSmaPortIsAutoMigrateSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsAutoMigrateSupported.setStatus("current")
_IbSmaPortIsSlMappingSupported_Type = TruthValue
_IbSmaPortIsSlMappingSupported_Object = MibScalar
ibSmaPortIsSlMappingSupported = _IbSmaPortIsSlMappingSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 9),
    _IbSmaPortIsSlMappingSupported_Type()
)
ibSmaPortIsSlMappingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsSlMappingSupported.setStatus("current")
_IbSmaPortIsMKeyNvram_Type = TruthValue
_IbSmaPortIsMKeyNvram_Object = MibScalar
ibSmaPortIsMKeyNvram = _IbSmaPortIsMKeyNvram_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 10),
    _IbSmaPortIsMKeyNvram_Type()
)
ibSmaPortIsMKeyNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsMKeyNvram.setStatus("current")
_IbSmaPortIsPKeyNvram_Type = TruthValue
_IbSmaPortIsPKeyNvram_Object = MibScalar
ibSmaPortIsPKeyNvram = _IbSmaPortIsPKeyNvram_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 11),
    _IbSmaPortIsPKeyNvram_Type()
)
ibSmaPortIsPKeyNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsPKeyNvram.setStatus("current")
_IbSmaPortIsLedInfoSupported_Type = TruthValue
_IbSmaPortIsLedInfoSupported_Object = MibScalar
ibSmaPortIsLedInfoSupported = _IbSmaPortIsLedInfoSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 12),
    _IbSmaPortIsLedInfoSupported_Type()
)
ibSmaPortIsLedInfoSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsLedInfoSupported.setStatus("current")
_IbSmaPortIsSmDisabled_Type = TruthValue
_IbSmaPortIsSmDisabled_Object = MibScalar
ibSmaPortIsSmDisabled = _IbSmaPortIsSmDisabled_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 13),
    _IbSmaPortIsSmDisabled_Type()
)
ibSmaPortIsSmDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsSmDisabled.setStatus("current")
_IbSmaPortIsSysImgGuidSupported_Type = TruthValue
_IbSmaPortIsSysImgGuidSupported_Object = MibScalar
ibSmaPortIsSysImgGuidSupported = _IbSmaPortIsSysImgGuidSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 14),
    _IbSmaPortIsSysImgGuidSupported_Type()
)
ibSmaPortIsSysImgGuidSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsSysImgGuidSupported.setStatus("current")
_IbSmaPortIsPKeyExtPortTrapSup_Type = TruthValue
_IbSmaPortIsPKeyExtPortTrapSup_Object = MibScalar
ibSmaPortIsPKeyExtPortTrapSup = _IbSmaPortIsPKeyExtPortTrapSup_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 15),
    _IbSmaPortIsPKeyExtPortTrapSup_Type()
)
ibSmaPortIsPKeyExtPortTrapSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsPKeyExtPortTrapSup.setStatus("current")
_IbSmaPortIsCommManageSupported_Type = TruthValue
_IbSmaPortIsCommManageSupported_Object = MibScalar
ibSmaPortIsCommManageSupported = _IbSmaPortIsCommManageSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 16),
    _IbSmaPortIsCommManageSupported_Type()
)
ibSmaPortIsCommManageSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsCommManageSupported.setStatus("current")
_IbSmaPortIsSnmpTunnelSupported_Type = TruthValue
_IbSmaPortIsSnmpTunnelSupported_Object = MibScalar
ibSmaPortIsSnmpTunnelSupported = _IbSmaPortIsSnmpTunnelSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 17),
    _IbSmaPortIsSnmpTunnelSupported_Type()
)
ibSmaPortIsSnmpTunnelSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsSnmpTunnelSupported.setStatus("current")
_IbSmaPortIsReinitSupported_Type = TruthValue
_IbSmaPortIsReinitSupported_Object = MibScalar
ibSmaPortIsReinitSupported = _IbSmaPortIsReinitSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 18),
    _IbSmaPortIsReinitSupported_Type()
)
ibSmaPortIsReinitSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsReinitSupported.setStatus("current")
_IbSmaPortIsDevManageSupported_Type = TruthValue
_IbSmaPortIsDevManageSupported_Object = MibScalar
ibSmaPortIsDevManageSupported = _IbSmaPortIsDevManageSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 19),
    _IbSmaPortIsDevManageSupported_Type()
)
ibSmaPortIsDevManageSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsDevManageSupported.setStatus("current")
_IbSmaPortIsVendorClassSupported_Type = TruthValue
_IbSmaPortIsVendorClassSupported_Object = MibScalar
ibSmaPortIsVendorClassSupported = _IbSmaPortIsVendorClassSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 20),
    _IbSmaPortIsVendorClassSupported_Type()
)
ibSmaPortIsVendorClassSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsVendorClassSupported.setStatus("current")
_IbSmaPortIsDrNoticeSupported_Type = TruthValue
_IbSmaPortIsDrNoticeSupported_Object = MibScalar
ibSmaPortIsDrNoticeSupported = _IbSmaPortIsDrNoticeSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 21),
    _IbSmaPortIsDrNoticeSupported_Type()
)
ibSmaPortIsDrNoticeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsDrNoticeSupported.setStatus("current")
_IbSmaPortIsCapMaskNoticSupported_Type = TruthValue
_IbSmaPortIsCapMaskNoticSupported_Object = MibScalar
ibSmaPortIsCapMaskNoticSupported = _IbSmaPortIsCapMaskNoticSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 22),
    _IbSmaPortIsCapMaskNoticSupported_Type()
)
ibSmaPortIsCapMaskNoticSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsCapMaskNoticSupported.setStatus("current")
_IbSmaPortIsBootMgmtSupported_Type = TruthValue
_IbSmaPortIsBootMgmtSupported_Object = MibScalar
ibSmaPortIsBootMgmtSupported = _IbSmaPortIsBootMgmtSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 23),
    _IbSmaPortIsBootMgmtSupported_Type()
)
ibSmaPortIsBootMgmtSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortIsBootMgmtSupported.setStatus("current")


class _IbSmaPortMKeyLeasePeriod_Type(Integer32):
    """Custom type ibSmaPortMKeyLeasePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaPortMKeyLeasePeriod_Type.__name__ = "Integer32"
_IbSmaPortMKeyLeasePeriod_Object = MibScalar
ibSmaPortMKeyLeasePeriod = _IbSmaPortMKeyLeasePeriod_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 24),
    _IbSmaPortMKeyLeasePeriod_Type()
)
ibSmaPortMKeyLeasePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMKeyLeasePeriod.setStatus("current")
if mibBuilder.loadTexts:
    ibSmaPortMKeyLeasePeriod.setUnits("seconds")


class _IbSmaPortMKeyProtectBits_Type(Integer32):
    """Custom type ibSmaPortMKeyProtectBits based on Integer32"""
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
        *(("failOnNoMatch", 4),
          ("noMKeyProtection", 1),
          ("succeedWithReturnKey", 2),
          ("succeedWithReturnZeroes", 3))
    )


_IbSmaPortMKeyProtectBits_Type.__name__ = "Integer32"
_IbSmaPortMKeyProtectBits_Object = MibScalar
ibSmaPortMKeyProtectBits = _IbSmaPortMKeyProtectBits_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 25),
    _IbSmaPortMKeyProtectBits_Type()
)
ibSmaPortMKeyProtectBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMKeyProtectBits.setStatus("current")


class _IbSmaPortMasterSmSl_Type(Integer32):
    """Custom type ibSmaPortMasterSmSl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbSmaPortMasterSmSl_Type.__name__ = "Integer32"
_IbSmaPortMasterSmSl_Object = MibScalar
ibSmaPortMasterSmSl = _IbSmaPortMasterSmSl_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 26),
    _IbSmaPortMasterSmSl_Type()
)
ibSmaPortMasterSmSl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMasterSmSl.setStatus("current")
_IbSmaPortInitTypeLoad_Type = TruthValue
_IbSmaPortInitTypeLoad_Object = MibScalar
ibSmaPortInitTypeLoad = _IbSmaPortInitTypeLoad_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 27),
    _IbSmaPortInitTypeLoad_Type()
)
ibSmaPortInitTypeLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitTypeLoad.setStatus("current")
_IbSmaPortInitTypeContent_Type = TruthValue
_IbSmaPortInitTypeContent_Object = MibScalar
ibSmaPortInitTypeContent = _IbSmaPortInitTypeContent_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 28),
    _IbSmaPortInitTypeContent_Type()
)
ibSmaPortInitTypeContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitTypeContent.setStatus("current")
_IbSmaPortInitTypePresence_Type = TruthValue
_IbSmaPortInitTypePresence_Object = MibScalar
ibSmaPortInitTypePresence = _IbSmaPortInitTypePresence_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 29),
    _IbSmaPortInitTypePresence_Type()
)
ibSmaPortInitTypePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitTypePresence.setStatus("current")
_IbSmaPortInitTypeResuscitate_Type = TruthValue
_IbSmaPortInitTypeResuscitate_Object = MibScalar
ibSmaPortInitTypeResuscitate = _IbSmaPortInitTypeResuscitate_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 30),
    _IbSmaPortInitTypeResuscitate_Type()
)
ibSmaPortInitTypeResuscitate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitTypeResuscitate.setStatus("current")
_IbSmaPortInitNoLoadReply_Type = TruthValue
_IbSmaPortInitNoLoadReply_Object = MibScalar
ibSmaPortInitNoLoadReply = _IbSmaPortInitNoLoadReply_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 31),
    _IbSmaPortInitNoLoadReply_Type()
)
ibSmaPortInitNoLoadReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitNoLoadReply.setStatus("current")
_IbSmaPortInitPreserveContReply_Type = TruthValue
_IbSmaPortInitPreserveContReply_Object = MibScalar
ibSmaPortInitPreserveContReply = _IbSmaPortInitPreserveContReply_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 32),
    _IbSmaPortInitPreserveContReply_Type()
)
ibSmaPortInitPreserveContReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitPreserveContReply.setStatus("current")
_IbSmaPortInitPreservePresReply_Type = TruthValue
_IbSmaPortInitPreservePresReply_Object = MibScalar
ibSmaPortInitPreservePresReply = _IbSmaPortInitPreservePresReply_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 33),
    _IbSmaPortInitPreservePresReply_Type()
)
ibSmaPortInitPreservePresReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortInitPreservePresReply.setStatus("current")


class _IbSmaPortMKeyViolations_Type(Gauge32):
    """Custom type ibSmaPortMKeyViolations based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaPortMKeyViolations_Type.__name__ = "Gauge32"
_IbSmaPortMKeyViolations_Object = MibScalar
ibSmaPortMKeyViolations = _IbSmaPortMKeyViolations_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 34),
    _IbSmaPortMKeyViolations_Type()
)
ibSmaPortMKeyViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMKeyViolations.setStatus("current")


class _IbSmaPortPKeyViolations_Type(Gauge32):
    """Custom type ibSmaPortPKeyViolations based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaPortPKeyViolations_Type.__name__ = "Gauge32"
_IbSmaPortPKeyViolations_Object = MibScalar
ibSmaPortPKeyViolations = _IbSmaPortPKeyViolations_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 35),
    _IbSmaPortPKeyViolations_Type()
)
ibSmaPortPKeyViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortPKeyViolations.setStatus("current")


class _IbSmaPortQKeyViolations_Type(Gauge32):
    """Custom type ibSmaPortQKeyViolations based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbSmaPortQKeyViolations_Type.__name__ = "Gauge32"
_IbSmaPortQKeyViolations_Object = MibScalar
ibSmaPortQKeyViolations = _IbSmaPortQKeyViolations_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 36),
    _IbSmaPortQKeyViolations_Type()
)
ibSmaPortQKeyViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortQKeyViolations.setStatus("current")


class _IbSmaPortNumGuid_Type(Integer32):
    """Custom type ibSmaPortNumGuid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbSmaPortNumGuid_Type.__name__ = "Integer32"
_IbSmaPortNumGuid_Object = MibScalar
ibSmaPortNumGuid = _IbSmaPortNumGuid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 37),
    _IbSmaPortNumGuid_Type()
)
ibSmaPortNumGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortNumGuid.setStatus("current")


class _IbSmaPortSubnetTimeout_Type(Integer32):
    """Custom type ibSmaPortSubnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbSmaPortSubnetTimeout_Type.__name__ = "Integer32"
_IbSmaPortSubnetTimeout_Object = MibScalar
ibSmaPortSubnetTimeout = _IbSmaPortSubnetTimeout_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 38),
    _IbSmaPortSubnetTimeout_Type()
)
ibSmaPortSubnetTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortSubnetTimeout.setStatus("current")


class _IbSmaPortResponseTimeValue_Type(Integer32):
    """Custom type ibSmaPortResponseTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbSmaPortResponseTimeValue_Type.__name__ = "Integer32"
_IbSmaPortResponseTimeValue_Object = MibScalar
ibSmaPortResponseTimeValue = _IbSmaPortResponseTimeValue_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 4, 39),
    _IbSmaPortResponseTimeValue_Type()
)
ibSmaPortResponseTimeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortResponseTimeValue.setStatus("current")
_IbSmaDataPortInfo_ObjectIdentity = ObjectIdentity
ibSmaDataPortInfo = _IbSmaDataPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 5)
)
_IbSmaPortInfoTable_Object = MibTable
ibSmaPortInfoTable = _IbSmaPortInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ibSmaPortInfoTable.setStatus("current")
_IbSmaPortInfoEntry_Object = MibTableRow
ibSmaPortInfoEntry = _IbSmaPortInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1)
)
ibSmaPortInfoEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaPortIndex"),
)
if mibBuilder.loadTexts:
    ibSmaPortInfoEntry.setStatus("current")
_IbSmaPortIndex_Type = IbDataPort
_IbSmaPortIndex_Object = MibTableColumn
ibSmaPortIndex = _IbSmaPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 1),
    _IbSmaPortIndex_Type()
)
ibSmaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaPortIndex.setStatus("current")


class _IbSmaPortLinkWidthEnabled_Type(Integer32):
    """Custom type ibSmaPortLinkWidthEnabled based on Integer32"""
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
        *(("fourX", 3),
          ("fourXOr12X", 7),
          ("linkWidthSupported", 9),
          ("noStateChange", 1),
          ("oneX", 2),
          ("oneX4XOr12X", 8),
          ("oneXOr12X", 6),
          ("oneXOr4X", 4),
          ("other", 10),
          ("twelveX", 5))
    )


_IbSmaPortLinkWidthEnabled_Type.__name__ = "Integer32"
_IbSmaPortLinkWidthEnabled_Object = MibTableColumn
ibSmaPortLinkWidthEnabled = _IbSmaPortLinkWidthEnabled_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 2),
    _IbSmaPortLinkWidthEnabled_Type()
)
ibSmaPortLinkWidthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkWidthEnabled.setStatus("current")


class _IbSmaPortLinkWidthSupported_Type(Integer32):
    """Custom type ibSmaPortLinkWidthSupported based on Integer32"""
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
        *(("oneX", 1),
          ("oneX4XOr12X", 3),
          ("oneXOr4X", 2),
          ("other", 4))
    )


_IbSmaPortLinkWidthSupported_Type.__name__ = "Integer32"
_IbSmaPortLinkWidthSupported_Object = MibTableColumn
ibSmaPortLinkWidthSupported = _IbSmaPortLinkWidthSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 3),
    _IbSmaPortLinkWidthSupported_Type()
)
ibSmaPortLinkWidthSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkWidthSupported.setStatus("current")


class _IbSmaPortLinkWidthActive_Type(Integer32):
    """Custom type ibSmaPortLinkWidthActive based on Integer32"""
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
        *(("fourX", 2),
          ("oneX", 1),
          ("other", 4),
          ("twelveX", 3))
    )


_IbSmaPortLinkWidthActive_Type.__name__ = "Integer32"
_IbSmaPortLinkWidthActive_Object = MibTableColumn
ibSmaPortLinkWidthActive = _IbSmaPortLinkWidthActive_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 4),
    _IbSmaPortLinkWidthActive_Type()
)
ibSmaPortLinkWidthActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkWidthActive.setStatus("current")


class _IbSmaPortLinkSpeedSupported_Type(Integer32):
    """Custom type ibSmaPortLinkSpeedSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("twoPoint5Gbps", 1))
    )


_IbSmaPortLinkSpeedSupported_Type.__name__ = "Integer32"
_IbSmaPortLinkSpeedSupported_Object = MibTableColumn
ibSmaPortLinkSpeedSupported = _IbSmaPortLinkSpeedSupported_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 5),
    _IbSmaPortLinkSpeedSupported_Type()
)
ibSmaPortLinkSpeedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkSpeedSupported.setStatus("current")


class _IbSmaPortLinkState_Type(Integer32):
    """Custom type ibSmaPortLinkState based on Integer32"""
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
        *(("active", 5),
          ("armed", 4),
          ("down", 2),
          ("init", 3),
          ("noChange", 1),
          ("other", 6))
    )


_IbSmaPortLinkState_Type.__name__ = "Integer32"
_IbSmaPortLinkState_Object = MibTableColumn
ibSmaPortLinkState = _IbSmaPortLinkState_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 6),
    _IbSmaPortLinkState_Type()
)
ibSmaPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkState.setStatus("current")


class _IbSmaPortPhysState_Type(Integer32):
    """Custom type ibSmaPortPhysState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("linkErrorRecovery", 7),
          ("linkUp", 6),
          ("noChange", 1),
          ("other", 8),
          ("polling", 3),
          ("portConfigTraining", 5),
          ("sleep", 2))
    )


_IbSmaPortPhysState_Type.__name__ = "Integer32"
_IbSmaPortPhysState_Object = MibTableColumn
ibSmaPortPhysState = _IbSmaPortPhysState_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 7),
    _IbSmaPortPhysState_Type()
)
ibSmaPortPhysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortPhysState.setStatus("current")


class _IbSmaPortLinkDownDefaultState_Type(Integer32):
    """Custom type ibSmaPortLinkDownDefaultState based on Integer32"""
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
        *(("noChange", 1),
          ("other", 4),
          ("polling", 3),
          ("sleep", 2))
    )


_IbSmaPortLinkDownDefaultState_Type.__name__ = "Integer32"
_IbSmaPortLinkDownDefaultState_Object = MibTableColumn
ibSmaPortLinkDownDefaultState = _IbSmaPortLinkDownDefaultState_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 8),
    _IbSmaPortLinkDownDefaultState_Type()
)
ibSmaPortLinkDownDefaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkDownDefaultState.setStatus("current")


class _IbSmaPortLidMaskCount_Type(Integer32):
    """Custom type ibSmaPortLidMaskCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IbSmaPortLidMaskCount_Type.__name__ = "Integer32"
_IbSmaPortLidMaskCount_Object = MibTableColumn
ibSmaPortLidMaskCount = _IbSmaPortLidMaskCount_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 9),
    _IbSmaPortLidMaskCount_Type()
)
ibSmaPortLidMaskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLidMaskCount.setStatus("current")


class _IbSmaPortLinkSpeedActive_Type(Integer32):
    """Custom type ibSmaPortLinkSpeedActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("twoPoint5Gbps", 1))
    )


_IbSmaPortLinkSpeedActive_Type.__name__ = "Integer32"
_IbSmaPortLinkSpeedActive_Object = MibTableColumn
ibSmaPortLinkSpeedActive = _IbSmaPortLinkSpeedActive_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 10),
    _IbSmaPortLinkSpeedActive_Type()
)
ibSmaPortLinkSpeedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkSpeedActive.setStatus("current")


class _IbSmaPortLinkSpeedEnabled_Type(Integer32):
    """Custom type ibSmaPortLinkSpeedEnabled based on Integer32"""
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
        *(("linkSpeedSupported", 3),
          ("noStateChange", 1),
          ("other", 4),
          ("twoPoint5Gbps", 2))
    )


_IbSmaPortLinkSpeedEnabled_Type.__name__ = "Integer32"
_IbSmaPortLinkSpeedEnabled_Object = MibTableColumn
ibSmaPortLinkSpeedEnabled = _IbSmaPortLinkSpeedEnabled_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 11),
    _IbSmaPortLinkSpeedEnabled_Type()
)
ibSmaPortLinkSpeedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLinkSpeedEnabled.setStatus("current")


class _IbSmaPortNeighborMtu_Type(Integer32):
    """Custom type ibSmaPortNeighborMtu based on Integer32"""
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
        *(("mtu1024", 3),
          ("mtu2048", 4),
          ("mtu256", 1),
          ("mtu4096", 5),
          ("mtu512", 2),
          ("other", 6))
    )


_IbSmaPortNeighborMtu_Type.__name__ = "Integer32"
_IbSmaPortNeighborMtu_Object = MibTableColumn
ibSmaPortNeighborMtu = _IbSmaPortNeighborMtu_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 12),
    _IbSmaPortNeighborMtu_Type()
)
ibSmaPortNeighborMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortNeighborMtu.setStatus("current")


class _IbSmaPortVirtLaneSupport_Type(Integer32):
    """Custom type ibSmaPortVirtLaneSupport based on Integer32"""
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
        *(("other", 6),
          ("vl0", 1),
          ("vl0ToVl1", 2),
          ("vl0ToVl14", 5),
          ("vl0ToVl3", 3),
          ("vl0ToVl7", 4))
    )


_IbSmaPortVirtLaneSupport_Type.__name__ = "Integer32"
_IbSmaPortVirtLaneSupport_Object = MibTableColumn
ibSmaPortVirtLaneSupport = _IbSmaPortVirtLaneSupport_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 13),
    _IbSmaPortVirtLaneSupport_Type()
)
ibSmaPortVirtLaneSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVirtLaneSupport.setStatus("current")


class _IbSmaPortVlHighPriorityLimit_Type(Integer32):
    """Custom type ibSmaPortVlHighPriorityLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbSmaPortVlHighPriorityLimit_Type.__name__ = "Integer32"
_IbSmaPortVlHighPriorityLimit_Object = MibTableColumn
ibSmaPortVlHighPriorityLimit = _IbSmaPortVlHighPriorityLimit_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 14),
    _IbSmaPortVlHighPriorityLimit_Type()
)
ibSmaPortVlHighPriorityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVlHighPriorityLimit.setStatus("current")


class _IbSmaPortVlArbHighCapacity_Type(Integer32):
    """Custom type ibSmaPortVlArbHighCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IbSmaPortVlArbHighCapacity_Type.__name__ = "Integer32"
_IbSmaPortVlArbHighCapacity_Object = MibTableColumn
ibSmaPortVlArbHighCapacity = _IbSmaPortVlArbHighCapacity_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 15),
    _IbSmaPortVlArbHighCapacity_Type()
)
ibSmaPortVlArbHighCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVlArbHighCapacity.setStatus("current")


class _IbSmaPortVlArbLowCapacity_Type(Integer32):
    """Custom type ibSmaPortVlArbLowCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IbSmaPortVlArbLowCapacity_Type.__name__ = "Integer32"
_IbSmaPortVlArbLowCapacity_Object = MibTableColumn
ibSmaPortVlArbLowCapacity = _IbSmaPortVlArbLowCapacity_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 16),
    _IbSmaPortVlArbLowCapacity_Type()
)
ibSmaPortVlArbLowCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVlArbLowCapacity.setStatus("current")


class _IbSmaPortMtuCapacity_Type(Integer32):
    """Custom type ibSmaPortMtuCapacity based on Integer32"""
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
        *(("mtu1024", 3),
          ("mtu2048", 4),
          ("mtu256", 1),
          ("mtu4096", 5),
          ("mtu512", 2),
          ("other", 6))
    )


_IbSmaPortMtuCapacity_Type.__name__ = "Integer32"
_IbSmaPortMtuCapacity_Object = MibTableColumn
ibSmaPortMtuCapacity = _IbSmaPortMtuCapacity_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 17),
    _IbSmaPortMtuCapacity_Type()
)
ibSmaPortMtuCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortMtuCapacity.setStatus("current")


class _IbSmaPortVlStallCount_Type(Integer32):
    """Custom type ibSmaPortVlStallCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IbSmaPortVlStallCount_Type.__name__ = "Integer32"
_IbSmaPortVlStallCount_Object = MibTableColumn
ibSmaPortVlStallCount = _IbSmaPortVlStallCount_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 18),
    _IbSmaPortVlStallCount_Type()
)
ibSmaPortVlStallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVlStallCount.setStatus("current")


class _IbSmaPortHeadOfQueueLife_Type(Integer32):
    """Custom type ibSmaPortHeadOfQueueLife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbSmaPortHeadOfQueueLife_Type.__name__ = "Integer32"
_IbSmaPortHeadOfQueueLife_Object = MibTableColumn
ibSmaPortHeadOfQueueLife = _IbSmaPortHeadOfQueueLife_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 19),
    _IbSmaPortHeadOfQueueLife_Type()
)
ibSmaPortHeadOfQueueLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortHeadOfQueueLife.setStatus("current")


class _IbSmaPortOperationalVls_Type(Integer32):
    """Custom type ibSmaPortOperationalVls based on Integer32"""
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
        *(("other", 6),
          ("vl0", 1),
          ("vl0ToVl1", 2),
          ("vl0ToVl14", 5),
          ("vl0ToVl3", 3),
          ("vl0ToVl7", 4))
    )


_IbSmaPortOperationalVls_Type.__name__ = "Integer32"
_IbSmaPortOperationalVls_Object = MibTableColumn
ibSmaPortOperationalVls = _IbSmaPortOperationalVls_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 20),
    _IbSmaPortOperationalVls_Type()
)
ibSmaPortOperationalVls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortOperationalVls.setStatus("current")
_IbSmaPortPartEnforceInbound_Type = TruthValue
_IbSmaPortPartEnforceInbound_Object = MibTableColumn
ibSmaPortPartEnforceInbound = _IbSmaPortPartEnforceInbound_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 21),
    _IbSmaPortPartEnforceInbound_Type()
)
ibSmaPortPartEnforceInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortPartEnforceInbound.setStatus("current")
_IbSmaPortPartEnforceOutbound_Type = TruthValue
_IbSmaPortPartEnforceOutbound_Object = MibTableColumn
ibSmaPortPartEnforceOutbound = _IbSmaPortPartEnforceOutbound_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 22),
    _IbSmaPortPartEnforceOutbound_Type()
)
ibSmaPortPartEnforceOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortPartEnforceOutbound.setStatus("current")
_IbSmaPortFilterRawPktInbound_Type = TruthValue
_IbSmaPortFilterRawPktInbound_Object = MibTableColumn
ibSmaPortFilterRawPktInbound = _IbSmaPortFilterRawPktInbound_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 23),
    _IbSmaPortFilterRawPktInbound_Type()
)
ibSmaPortFilterRawPktInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortFilterRawPktInbound.setStatus("current")
_IbSmaPortFilterRawPktOutbound_Type = TruthValue
_IbSmaPortFilterRawPktOutbound_Object = MibTableColumn
ibSmaPortFilterRawPktOutbound = _IbSmaPortFilterRawPktOutbound_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 24),
    _IbSmaPortFilterRawPktOutbound_Type()
)
ibSmaPortFilterRawPktOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortFilterRawPktOutbound.setStatus("current")


class _IbSmaPortLocalPhysErrorThreshold_Type(Integer32):
    """Custom type ibSmaPortLocalPhysErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbSmaPortLocalPhysErrorThreshold_Type.__name__ = "Integer32"
_IbSmaPortLocalPhysErrorThreshold_Object = MibTableColumn
ibSmaPortLocalPhysErrorThreshold = _IbSmaPortLocalPhysErrorThreshold_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 25),
    _IbSmaPortLocalPhysErrorThreshold_Type()
)
ibSmaPortLocalPhysErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortLocalPhysErrorThreshold.setStatus("current")


class _IbSmaPortOverrunErrorThreshold_Type(Integer32):
    """Custom type ibSmaPortOverrunErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbSmaPortOverrunErrorThreshold_Type.__name__ = "Integer32"
_IbSmaPortOverrunErrorThreshold_Object = MibTableColumn
ibSmaPortOverrunErrorThreshold = _IbSmaPortOverrunErrorThreshold_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 5, 1, 1, 26),
    _IbSmaPortOverrunErrorThreshold_Type()
)
ibSmaPortOverrunErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortOverrunErrorThreshold.setStatus("current")
_IbSmaPKeyInfo_ObjectIdentity = ObjectIdentity
ibSmaPKeyInfo = _IbSmaPKeyInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 6)
)
_IbSmaPKeyTable_Object = MibTable
ibSmaPKeyTable = _IbSmaPKeyTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ibSmaPKeyTable.setStatus("current")
_IbSmaPKeyEntry_Object = MibTableRow
ibSmaPKeyEntry = _IbSmaPKeyEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 6, 1, 1)
)
ibSmaPKeyEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaPKeyIBAPortIndex"),
    (0, "SMA-MIB", "ibSmaPKeyIndex"),
)
if mibBuilder.loadTexts:
    ibSmaPKeyEntry.setStatus("current")
_IbSmaPKeyIBAPortIndex_Type = IbDataPortAndInvalid
_IbSmaPKeyIBAPortIndex_Object = MibTableColumn
ibSmaPKeyIBAPortIndex = _IbSmaPKeyIBAPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 6, 1, 1, 1),
    _IbSmaPKeyIBAPortIndex_Type()
)
ibSmaPKeyIBAPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaPKeyIBAPortIndex.setStatus("current")


class _IbSmaPKeyIndex_Type(Integer32):
    """Custom type ibSmaPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65505),
    )


_IbSmaPKeyIndex_Type.__name__ = "Integer32"
_IbSmaPKeyIndex_Object = MibTableColumn
ibSmaPKeyIndex = _IbSmaPKeyIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 6, 1, 1, 2),
    _IbSmaPKeyIndex_Type()
)
ibSmaPKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaPKeyIndex.setStatus("current")


class _IbSmaPKeyMembership_Type(Integer32):
    """Custom type ibSmaPKeyMembership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("limited", 2),
          ("none", 1))
    )


_IbSmaPKeyMembership_Type.__name__ = "Integer32"
_IbSmaPKeyMembership_Object = MibTableColumn
ibSmaPKeyMembership = _IbSmaPKeyMembership_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 6, 1, 1, 3),
    _IbSmaPKeyMembership_Type()
)
ibSmaPKeyMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPKeyMembership.setStatus("current")


class _IbSmaPKeyBase_Type(Integer32):
    """Custom type ibSmaPKeyBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65527),
    )


_IbSmaPKeyBase_Type.__name__ = "Integer32"
_IbSmaPKeyBase_Object = MibTableColumn
ibSmaPKeyBase = _IbSmaPKeyBase_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 6, 1, 1, 4),
    _IbSmaPKeyBase_Type()
)
ibSmaPKeyBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPKeyBase.setStatus("current")
_IbSmaSlToVlMapInfo_ObjectIdentity = ObjectIdentity
ibSmaSlToVlMapInfo = _IbSmaSlToVlMapInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 7)
)
_IbSmaSL2VLMapTable_Object = MibTable
ibSmaSL2VLMapTable = _IbSmaSL2VLMapTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ibSmaSL2VLMapTable.setStatus("current")
_IbSmaSL2VLMapEntry_Object = MibTableRow
ibSmaSL2VLMapEntry = _IbSmaSL2VLMapEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 7, 1, 1)
)
ibSmaSL2VLMapEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaIBAOutPortIndex"),
    (0, "SMA-MIB", "ibSmaIBAInPortIndex"),
    (0, "SMA-MIB", "ibSmaServiceLevelIndex"),
)
if mibBuilder.loadTexts:
    ibSmaSL2VLMapEntry.setStatus("current")
_IbSmaIBAOutPortIndex_Type = IbDataPortAndInvalid
_IbSmaIBAOutPortIndex_Object = MibTableColumn
ibSmaIBAOutPortIndex = _IbSmaIBAOutPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 7, 1, 1, 1),
    _IbSmaIBAOutPortIndex_Type()
)
ibSmaIBAOutPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaIBAOutPortIndex.setStatus("current")
_IbSmaIBAInPortIndex_Type = IbDataPortAndInvalid
_IbSmaIBAInPortIndex_Object = MibTableColumn
ibSmaIBAInPortIndex = _IbSmaIBAInPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 7, 1, 1, 2),
    _IbSmaIBAInPortIndex_Type()
)
ibSmaIBAInPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaIBAInPortIndex.setStatus("current")


class _IbSmaServiceLevelIndex_Type(Integer32):
    """Custom type ibSmaServiceLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IbSmaServiceLevelIndex_Type.__name__ = "Integer32"
_IbSmaServiceLevelIndex_Object = MibTableColumn
ibSmaServiceLevelIndex = _IbSmaServiceLevelIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 7, 1, 1, 3),
    _IbSmaServiceLevelIndex_Type()
)
ibSmaServiceLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaServiceLevelIndex.setStatus("current")


class _IbSmaVirtualLane_Type(Integer32):
    """Custom type ibSmaVirtualLane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbSmaVirtualLane_Type.__name__ = "Integer32"
_IbSmaVirtualLane_Object = MibTableColumn
ibSmaVirtualLane = _IbSmaVirtualLane_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 7, 1, 1, 4),
    _IbSmaVirtualLane_Type()
)
ibSmaVirtualLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaVirtualLane.setStatus("current")
_IbSmaVLArbitInfo_ObjectIdentity = ObjectIdentity
ibSmaVLArbitInfo = _IbSmaVLArbitInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 8)
)
_IbSmaHiPriVlArbTable_Object = MibTable
ibSmaHiPriVlArbTable = _IbSmaHiPriVlArbTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ibSmaHiPriVlArbTable.setStatus("current")
_IbSmaHiPriVlArbEntry_Object = MibTableRow
ibSmaHiPriVlArbEntry = _IbSmaHiPriVlArbEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 1, 1)
)
ibSmaHiPriVlArbEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaHiPriIBAPortIndex"),
    (0, "SMA-MIB", "ibSmaHiPriNIndex"),
)
if mibBuilder.loadTexts:
    ibSmaHiPriVlArbEntry.setStatus("current")
_IbSmaHiPriIBAPortIndex_Type = IbDataPort
_IbSmaHiPriIBAPortIndex_Object = MibTableColumn
ibSmaHiPriIBAPortIndex = _IbSmaHiPriIBAPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 1, 1, 1),
    _IbSmaHiPriIBAPortIndex_Type()
)
ibSmaHiPriIBAPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaHiPriIBAPortIndex.setStatus("current")


class _IbSmaHiPriNIndex_Type(Integer32):
    """Custom type ibSmaHiPriNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IbSmaHiPriNIndex_Type.__name__ = "Integer32"
_IbSmaHiPriNIndex_Object = MibTableColumn
ibSmaHiPriNIndex = _IbSmaHiPriNIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 1, 1, 2),
    _IbSmaHiPriNIndex_Type()
)
ibSmaHiPriNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaHiPriNIndex.setStatus("current")


class _IbSmaHiPriVirtLane_Type(Integer32):
    """Custom type ibSmaHiPriVirtLane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_IbSmaHiPriVirtLane_Type.__name__ = "Integer32"
_IbSmaHiPriVirtLane_Object = MibTableColumn
ibSmaHiPriVirtLane = _IbSmaHiPriVirtLane_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 1, 1, 3),
    _IbSmaHiPriVirtLane_Type()
)
ibSmaHiPriVirtLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaHiPriVirtLane.setStatus("current")


class _IbSmaHiPriWeight_Type(Integer32):
    """Custom type ibSmaHiPriWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbSmaHiPriWeight_Type.__name__ = "Integer32"
_IbSmaHiPriWeight_Object = MibTableColumn
ibSmaHiPriWeight = _IbSmaHiPriWeight_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 1, 1, 4),
    _IbSmaHiPriWeight_Type()
)
ibSmaHiPriWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaHiPriWeight.setStatus("current")
_IbSmaLowPriVlArbTable_Object = MibTable
ibSmaLowPriVlArbTable = _IbSmaLowPriVlArbTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ibSmaLowPriVlArbTable.setStatus("current")
_IbSmaLowPriVlArbEntry_Object = MibTableRow
ibSmaLowPriVlArbEntry = _IbSmaLowPriVlArbEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 2, 1)
)
ibSmaLowPriVlArbEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaLowPriIBAPortIndex"),
    (0, "SMA-MIB", "ibSmaLowPriNIndex"),
)
if mibBuilder.loadTexts:
    ibSmaLowPriVlArbEntry.setStatus("current")
_IbSmaLowPriIBAPortIndex_Type = IbDataPort
_IbSmaLowPriIBAPortIndex_Object = MibTableColumn
ibSmaLowPriIBAPortIndex = _IbSmaLowPriIBAPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 2, 1, 1),
    _IbSmaLowPriIBAPortIndex_Type()
)
ibSmaLowPriIBAPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaLowPriIBAPortIndex.setStatus("current")


class _IbSmaLowPriNIndex_Type(Integer32):
    """Custom type ibSmaLowPriNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IbSmaLowPriNIndex_Type.__name__ = "Integer32"
_IbSmaLowPriNIndex_Object = MibTableColumn
ibSmaLowPriNIndex = _IbSmaLowPriNIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 2, 1, 2),
    _IbSmaLowPriNIndex_Type()
)
ibSmaLowPriNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaLowPriNIndex.setStatus("current")


class _IbSmaLowPriVirtLane_Type(Integer32):
    """Custom type ibSmaLowPriVirtLane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_IbSmaLowPriVirtLane_Type.__name__ = "Integer32"
_IbSmaLowPriVirtLane_Object = MibTableColumn
ibSmaLowPriVirtLane = _IbSmaLowPriVirtLane_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 2, 1, 3),
    _IbSmaLowPriVirtLane_Type()
)
ibSmaLowPriVirtLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaLowPriVirtLane.setStatus("current")


class _IbSmaLowPriWeight_Type(Integer32):
    """Custom type ibSmaLowPriWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbSmaLowPriWeight_Type.__name__ = "Integer32"
_IbSmaLowPriWeight_Object = MibTableColumn
ibSmaLowPriWeight = _IbSmaLowPriWeight_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 8, 2, 1, 4),
    _IbSmaLowPriWeight_Type()
)
ibSmaLowPriWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaLowPriWeight.setStatus("current")
_IbSmaLFTInfo_ObjectIdentity = ObjectIdentity
ibSmaLFTInfo = _IbSmaLFTInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 9)
)
_IbSmaLinForTable_Object = MibTable
ibSmaLinForTable = _IbSmaLinForTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ibSmaLinForTable.setStatus("current")
_IbSmaLinForEntry_Object = MibTableRow
ibSmaLinForEntry = _IbSmaLinForEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 9, 1, 1)
)
ibSmaLinForEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaLinDestDLIDIndex"),
)
if mibBuilder.loadTexts:
    ibSmaLinForEntry.setStatus("current")
_IbSmaLinDestDLIDIndex_Type = IbUnicastLid
_IbSmaLinDestDLIDIndex_Object = MibTableColumn
ibSmaLinDestDLIDIndex = _IbSmaLinDestDLIDIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 9, 1, 1, 1),
    _IbSmaLinDestDLIDIndex_Type()
)
ibSmaLinDestDLIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaLinDestDLIDIndex.setStatus("current")
_IbSmaLinForwEgressPort_Type = IbDataPortAndInvalid
_IbSmaLinForwEgressPort_Object = MibTableColumn
ibSmaLinForwEgressPort = _IbSmaLinForwEgressPort_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 9, 1, 1, 2),
    _IbSmaLinForwEgressPort_Type()
)
ibSmaLinForwEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaLinForwEgressPort.setStatus("current")
_IbSmaRFTInfo_ObjectIdentity = ObjectIdentity
ibSmaRFTInfo = _IbSmaRFTInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 10)
)
_IbSmaRandomForwardingTable_Object = MibTable
ibSmaRandomForwardingTable = _IbSmaRandomForwardingTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ibSmaRandomForwardingTable.setStatus("current")
_IbSmaRandomForwardingEntry_Object = MibTableRow
ibSmaRandomForwardingEntry = _IbSmaRandomForwardingEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1, 1)
)
ibSmaRandomForwardingEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaRandomForwardingPortIndex"),
)
if mibBuilder.loadTexts:
    ibSmaRandomForwardingEntry.setStatus("current")
_IbSmaRandomForwardingPortIndex_Type = IbDataPort
_IbSmaRandomForwardingPortIndex_Object = MibTableColumn
ibSmaRandomForwardingPortIndex = _IbSmaRandomForwardingPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1, 1, 1),
    _IbSmaRandomForwardingPortIndex_Type()
)
ibSmaRandomForwardingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaRandomForwardingPortIndex.setStatus("current")


class _IbSmaRandomDestLID_Type(Integer32):
    """Custom type ibSmaRandomDestLID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49152),
    )


_IbSmaRandomDestLID_Type.__name__ = "Integer32"
_IbSmaRandomDestLID_Object = MibTableColumn
ibSmaRandomDestLID = _IbSmaRandomDestLID_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1, 1, 2),
    _IbSmaRandomDestLID_Type()
)
ibSmaRandomDestLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaRandomDestLID.setStatus("current")
_IbSmaRandomForwEgressPort_Type = IbDataPort
_IbSmaRandomForwEgressPort_Object = MibTableColumn
ibSmaRandomForwEgressPort = _IbSmaRandomForwEgressPort_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1, 1, 3),
    _IbSmaRandomForwEgressPort_Type()
)
ibSmaRandomForwEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaRandomForwEgressPort.setStatus("current")


class _IbSmaRandomLMC_Type(Integer32):
    """Custom type ibSmaRandomLMC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IbSmaRandomLMC_Type.__name__ = "Integer32"
_IbSmaRandomLMC_Object = MibTableColumn
ibSmaRandomLMC = _IbSmaRandomLMC_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1, 1, 4),
    _IbSmaRandomLMC_Type()
)
ibSmaRandomLMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaRandomLMC.setStatus("current")
_IbSmaRandomIsValid_Type = TruthValue
_IbSmaRandomIsValid_Object = MibTableColumn
ibSmaRandomIsValid = _IbSmaRandomIsValid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 10, 1, 1, 5),
    _IbSmaRandomIsValid_Type()
)
ibSmaRandomIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaRandomIsValid.setStatus("current")
_IbSmaMFTInfo_ObjectIdentity = ObjectIdentity
ibSmaMFTInfo = _IbSmaMFTInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 11)
)
_IbSmaMulForTable_Object = MibTable
ibSmaMulForTable = _IbSmaMulForTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ibSmaMulForTable.setStatus("current")
_IbSmaMulForEntry_Object = MibTableRow
ibSmaMulForEntry = _IbSmaMulForEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 11, 1, 1)
)
ibSmaMulForEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaMulDestDLIDIndex"),
)
if mibBuilder.loadTexts:
    ibSmaMulForEntry.setStatus("current")
_IbSmaMulDestDLIDIndex_Type = IbMulticastLid
_IbSmaMulDestDLIDIndex_Object = MibTableColumn
ibSmaMulDestDLIDIndex = _IbSmaMulDestDLIDIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 11, 1, 1, 1),
    _IbSmaMulDestDLIDIndex_Type()
)
ibSmaMulDestDLIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaMulDestDLIDIndex.setStatus("current")
_IbSmaMulForwMask_Type = IbSmPortList
_IbSmaMulForwMask_Object = MibTableColumn
ibSmaMulForwMask = _IbSmaMulForwMask_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 11, 1, 1, 2),
    _IbSmaMulForwMask_Type()
)
ibSmaMulForwMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaMulForwMask.setStatus("current")
_IbSmaSMInfo_ObjectIdentity = ObjectIdentity
ibSmaSMInfo = _IbSmaSMInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 12)
)
_IbSmaSubMgrInfo_ObjectIdentity = ObjectIdentity
ibSmaSubMgrInfo = _IbSmaSubMgrInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1)
)
_IbSmaSmInfoTable_Object = MibTable
ibSmaSmInfoTable = _IbSmaSmInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ibSmaSmInfoTable.setStatus("current")
_IbSmaSmInfoEntry_Object = MibTableRow
ibSmaSmInfoEntry = _IbSmaSmInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1)
)
ibSmaSmInfoEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaSmInfoPortIndex"),
)
if mibBuilder.loadTexts:
    ibSmaSmInfoEntry.setStatus("current")
_IbSmaSmInfoPortIndex_Type = IbDataPort
_IbSmaSmInfoPortIndex_Object = MibTableColumn
ibSmaSmInfoPortIndex = _IbSmaSmInfoPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1, 1),
    _IbSmaSmInfoPortIndex_Type()
)
ibSmaSmInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaSmInfoPortIndex.setStatus("current")
_IbSmaSmGuid_Type = IbGuid
_IbSmaSmGuid_Object = MibTableColumn
ibSmaSmGuid = _IbSmaSmGuid_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1, 2),
    _IbSmaSmGuid_Type()
)
ibSmaSmGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSmGuid.setStatus("current")


class _IbSmaSmSmKey_Type(OctetString):
    """Custom type ibSmaSmSmKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbSmaSmSmKey_Type.__name__ = "OctetString"
_IbSmaSmSmKey_Object = MibTableColumn
ibSmaSmSmKey = _IbSmaSmSmKey_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1, 3),
    _IbSmaSmSmKey_Type()
)
ibSmaSmSmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSmSmKey.setStatus("current")
_IbSmaSmSmpCount_Type = Counter32
_IbSmaSmSmpCount_Object = MibTableColumn
ibSmaSmSmpCount = _IbSmaSmSmpCount_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1, 4),
    _IbSmaSmSmpCount_Type()
)
ibSmaSmSmpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSmSmpCount.setStatus("current")


class _IbSmaSmPriority_Type(Integer32):
    """Custom type ibSmaSmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IbSmaSmPriority_Type.__name__ = "Integer32"
_IbSmaSmPriority_Object = MibTableColumn
ibSmaSmPriority = _IbSmaSmPriority_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1, 5),
    _IbSmaSmPriority_Type()
)
ibSmaSmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSmPriority.setStatus("current")


class _IbSmaSmState_Type(Integer32):
    """Custom type ibSmaSmState based on Integer32"""
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
        *(("discovering", 3),
          ("master", 5),
          ("notActive", 2),
          ("standby", 4),
          ("unknown", 1))
    )


_IbSmaSmState_Type.__name__ = "Integer32"
_IbSmaSmState_Object = MibTableColumn
ibSmaSmState = _IbSmaSmState_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 12, 1, 1, 1, 6),
    _IbSmaSmState_Type()
)
ibSmaSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaSmState.setStatus("current")
_IbSmaVendDiagInfo_ObjectIdentity = ObjectIdentity
ibSmaVendDiagInfo = _IbSmaVendDiagInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 13)
)
_IbSmaVendDiagInfoTable_Object = MibTable
ibSmaVendDiagInfoTable = _IbSmaVendDiagInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1)
)
if mibBuilder.loadTexts:
    ibSmaVendDiagInfoTable.setStatus("current")
_IbSmaVendDiagInfoEntry_Object = MibTableRow
ibSmaVendDiagInfoEntry = _IbSmaVendDiagInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1, 1)
)
ibSmaVendDiagInfoEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaVendDiagPortIndex"),
)
if mibBuilder.loadTexts:
    ibSmaVendDiagInfoEntry.setStatus("current")
_IbSmaVendDiagPortIndex_Type = IbDataPortAndInvalid
_IbSmaVendDiagPortIndex_Object = MibTableColumn
ibSmaVendDiagPortIndex = _IbSmaVendDiagPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1, 1, 1),
    _IbSmaVendDiagPortIndex_Type()
)
ibSmaVendDiagPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaVendDiagPortIndex.setStatus("current")


class _IbSmaPortGenericDiagCode_Type(Integer32):
    """Custom type ibSmaPortGenericDiagCode based on Integer32"""
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
        *(("hardError", 5),
          ("initializing", 3),
          ("other", 6),
          ("performingSelfTest", 2),
          ("portReady", 1),
          ("softError", 4))
    )


_IbSmaPortGenericDiagCode_Type.__name__ = "Integer32"
_IbSmaPortGenericDiagCode_Object = MibTableColumn
ibSmaPortGenericDiagCode = _IbSmaPortGenericDiagCode_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1, 1, 2),
    _IbSmaPortGenericDiagCode_Type()
)
ibSmaPortGenericDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortGenericDiagCode.setStatus("current")


class _IbSmaPortVendorDiagCode_Type(Integer32):
    """Custom type ibSmaPortVendorDiagCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_IbSmaPortVendorDiagCode_Type.__name__ = "Integer32"
_IbSmaPortVendorDiagCode_Object = MibTableColumn
ibSmaPortVendorDiagCode = _IbSmaPortVendorDiagCode_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1, 1, 3),
    _IbSmaPortVendorDiagCode_Type()
)
ibSmaPortVendorDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVendorDiagCode.setStatus("current")
_IbSmaPortVendorDiagIndexFwd_Type = TruthValue
_IbSmaPortVendorDiagIndexFwd_Object = MibTableColumn
ibSmaPortVendorDiagIndexFwd = _IbSmaPortVendorDiagIndexFwd_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1, 1, 4),
    _IbSmaPortVendorDiagIndexFwd_Type()
)
ibSmaPortVendorDiagIndexFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVendorDiagIndexFwd.setStatus("current")


class _IbSmaPortVendorDiagData_Type(OctetString):
    """Custom type ibSmaPortVendorDiagData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(124, 124),
    )


_IbSmaPortVendorDiagData_Type.__name__ = "OctetString"
_IbSmaPortVendorDiagData_Object = MibTableColumn
ibSmaPortVendorDiagData = _IbSmaPortVendorDiagData_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 13, 1, 1, 5),
    _IbSmaPortVendorDiagData_Type()
)
ibSmaPortVendorDiagData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaPortVendorDiagData.setStatus("current")
_IbSmaLedInfo_ObjectIdentity = ObjectIdentity
ibSmaLedInfo = _IbSmaLedInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 1, 14)
)
_IbSmaLedInfoTable_Object = MibTable
ibSmaLedInfoTable = _IbSmaLedInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 14, 1)
)
if mibBuilder.loadTexts:
    ibSmaLedInfoTable.setStatus("current")
_IbSmaLedInfoEntry_Object = MibTableRow
ibSmaLedInfoEntry = _IbSmaLedInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 14, 1, 1)
)
ibSmaLedInfoEntry.setIndexNames(
    (0, "SMA-MIB", "ibSmaLedIndex"),
)
if mibBuilder.loadTexts:
    ibSmaLedInfoEntry.setStatus("current")
_IbSmaLedIndex_Type = IbDataPort
_IbSmaLedIndex_Object = MibTableColumn
ibSmaLedIndex = _IbSmaLedIndex_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 14, 1, 1, 1),
    _IbSmaLedIndex_Type()
)
ibSmaLedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibSmaLedIndex.setStatus("current")


class _IbSmaLedState_Type(Integer32):
    """Custom type ibSmaLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("unknown", 1))
    )


_IbSmaLedState_Type.__name__ = "Integer32"
_IbSmaLedState_Object = MibTableColumn
ibSmaLedState = _IbSmaLedState_Object(
    (1, 3, 6, 1, 3, 117, 3, 1, 14, 1, 1, 2),
    _IbSmaLedState_Type()
)
ibSmaLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSmaLedState.setStatus("current")
_IbSmaNotifications_ObjectIdentity = ObjectIdentity
ibSmaNotifications = _IbSmaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 2)
)
_IbSmaNotificationPrefix_ObjectIdentity = ObjectIdentity
ibSmaNotificationPrefix = _IbSmaNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 2, 0)
)
_IbSmaConformance_ObjectIdentity = ObjectIdentity
ibSmaConformance = _IbSmaConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 3)
)
_IbSmaCompliances_ObjectIdentity = ObjectIdentity
ibSmaCompliances = _IbSmaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 3, 1)
)
_IbSmaGroups_ObjectIdentity = ObjectIdentity
ibSmaGroups = _IbSmaGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 3, 3, 2)
)

# Managed Objects groups

ibSmaNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 1)
)
ibSmaNodeGroup.setObjects(
      *(("SMA-MIB", "ibSmaNodeString"),
        ("SMA-MIB", "ibSmaNodeBaseVersion"),
        ("SMA-MIB", "ibSmaNodeClassVersion"),
        ("SMA-MIB", "ibSmaNodeType"),
        ("SMA-MIB", "ibSmaNodeNumPorts"),
        ("SMA-MIB", "ibSmaSystemImageGuid"),
        ("SMA-MIB", "ibSmaNodeGuid"),
        ("SMA-MIB", "ibSmaNodePortGuid"),
        ("SMA-MIB", "ibSmaNodePartitionTableNum"),
        ("SMA-MIB", "ibSmaNodeDeviceId"),
        ("SMA-MIB", "ibSmaNodeRevision"),
        ("SMA-MIB", "ibSmaNodeLocalPortNumOrZero"),
        ("SMA-MIB", "ibSmaNodeVendorId"),
        ("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodePortNum"),
        ("SMA-MIB", "ibSmaNodeMethod"),
        ("SMA-MIB", "ibSmaNodeAttributeId"),
        ("SMA-MIB", "ibSmaNodeAttributeModifier"),
        ("SMA-MIB", "ibSmaNodeKey"),
        ("SMA-MIB", "ibSmaNodeLid2"),
        ("SMA-MIB", "ibSmaNodeServiceLevel"),
        ("SMA-MIB", "ibSmaNodeQueuePair1"),
        ("SMA-MIB", "ibSmaNodeQueuePair2"),
        ("SMA-MIB", "ibSmaNodeGid1"),
        ("SMA-MIB", "ibSmaNodeGid2"),
        ("SMA-MIB", "ibSmaNodeCapMask"),
        ("SMA-MIB", "ibSmaNodeSwitchLid"),
        ("SMA-MIB", "ibSmaNodeDataValid"))
)
if mibBuilder.loadTexts:
    ibSmaNodeGroup.setStatus("current")

ibSmaSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 2)
)
ibSmaSwitchGroup.setObjects(
      *(("SMA-MIB", "ibSmaSwLinearFdbTableNum"),
        ("SMA-MIB", "ibSmaSwRandomFdbTableNum"),
        ("SMA-MIB", "ibSmaSwMulticastFdbTableNum"),
        ("SMA-MIB", "ibSmaSwLinearFdbTop"),
        ("SMA-MIB", "ibSmaSwDefaultPort"),
        ("SMA-MIB", "ibSmaSwDefMcastPriPort"),
        ("SMA-MIB", "ibSmaSwDefMcastNotPriPort"),
        ("SMA-MIB", "ibSmaSwLifeTimeValue"),
        ("SMA-MIB", "ibSmaSwPortStateChange"),
        ("SMA-MIB", "ibSmaSwLidsPerPort"),
        ("SMA-MIB", "ibSmaSwPartitionEnforceNum"),
        ("SMA-MIB", "ibSmaSwInboundEnforceCap"),
        ("SMA-MIB", "ibSmaSwOutboundEnforceCap"),
        ("SMA-MIB", "ibSmaSwFilterRawPktInputCap"),
        ("SMA-MIB", "ibSmaSwFilterRawPktOutputCap"),
        ("SMA-MIB", "ibSmaSwEnhancedPort0"))
)
if mibBuilder.loadTexts:
    ibSmaSwitchGroup.setStatus("current")

ibSmaGuidGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 3)
)
ibSmaGuidGroup.setObjects(
    ("SMA-MIB", "ibSmaGuidVal")
)
if mibBuilder.loadTexts:
    ibSmaGuidGroup.setStatus("current")

ibSmaMgmtPortGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 4)
)
ibSmaMgmtPortGroup.setObjects(
      *(("SMA-MIB", "ibSmaPortMKey"),
        ("SMA-MIB", "ibSmaPortGidPrefix"),
        ("SMA-MIB", "ibSmaPortLid"),
        ("SMA-MIB", "ibSmaPortMasterSmLid"),
        ("SMA-MIB", "ibSmaPortIsSubnetManager"),
        ("SMA-MIB", "ibSmaPortIsNoticeSupported"),
        ("SMA-MIB", "ibSmaPortIsTrapSupported"),
        ("SMA-MIB", "ibSmaPortIsAutoMigrateSupported"),
        ("SMA-MIB", "ibSmaPortIsSlMappingSupported"),
        ("SMA-MIB", "ibSmaPortIsMKeyNvram"),
        ("SMA-MIB", "ibSmaPortIsPKeyNvram"),
        ("SMA-MIB", "ibSmaPortIsLedInfoSupported"),
        ("SMA-MIB", "ibSmaPortIsSmDisabled"),
        ("SMA-MIB", "ibSmaPortIsSysImgGuidSupported"),
        ("SMA-MIB", "ibSmaPortIsPKeyExtPortTrapSup"),
        ("SMA-MIB", "ibSmaPortIsCommManageSupported"),
        ("SMA-MIB", "ibSmaPortIsSnmpTunnelSupported"),
        ("SMA-MIB", "ibSmaPortIsReinitSupported"),
        ("SMA-MIB", "ibSmaPortIsDevManageSupported"),
        ("SMA-MIB", "ibSmaPortIsVendorClassSupported"),
        ("SMA-MIB", "ibSmaPortIsDrNoticeSupported"),
        ("SMA-MIB", "ibSmaPortIsCapMaskNoticSupported"),
        ("SMA-MIB", "ibSmaPortIsBootMgmtSupported"),
        ("SMA-MIB", "ibSmaPortMKeyLeasePeriod"),
        ("SMA-MIB", "ibSmaPortMKeyProtectBits"),
        ("SMA-MIB", "ibSmaPortMasterSmSl"),
        ("SMA-MIB", "ibSmaPortInitTypeLoad"),
        ("SMA-MIB", "ibSmaPortInitTypeContent"),
        ("SMA-MIB", "ibSmaPortInitTypePresence"),
        ("SMA-MIB", "ibSmaPortInitTypeResuscitate"),
        ("SMA-MIB", "ibSmaPortInitNoLoadReply"),
        ("SMA-MIB", "ibSmaPortInitPreserveContReply"),
        ("SMA-MIB", "ibSmaPortInitPreservePresReply"),
        ("SMA-MIB", "ibSmaPortMKeyViolations"),
        ("SMA-MIB", "ibSmaPortPKeyViolations"),
        ("SMA-MIB", "ibSmaPortQKeyViolations"),
        ("SMA-MIB", "ibSmaPortNumGuid"),
        ("SMA-MIB", "ibSmaPortSubnetTimeout"),
        ("SMA-MIB", "ibSmaPortResponseTimeValue"))
)
if mibBuilder.loadTexts:
    ibSmaMgmtPortGroup.setStatus("current")

ibSmaDataPortGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 5)
)
ibSmaDataPortGroup.setObjects(
      *(("SMA-MIB", "ibSmaPortLinkWidthEnabled"),
        ("SMA-MIB", "ibSmaPortLinkWidthSupported"),
        ("SMA-MIB", "ibSmaPortLinkWidthActive"),
        ("SMA-MIB", "ibSmaPortLinkSpeedSupported"),
        ("SMA-MIB", "ibSmaPortLinkState"),
        ("SMA-MIB", "ibSmaPortPhysState"),
        ("SMA-MIB", "ibSmaPortLinkDownDefaultState"),
        ("SMA-MIB", "ibSmaPortLidMaskCount"),
        ("SMA-MIB", "ibSmaPortLinkSpeedActive"),
        ("SMA-MIB", "ibSmaPortLinkSpeedEnabled"),
        ("SMA-MIB", "ibSmaPortNeighborMtu"),
        ("SMA-MIB", "ibSmaPortVirtLaneSupport"),
        ("SMA-MIB", "ibSmaPortVlHighPriorityLimit"),
        ("SMA-MIB", "ibSmaPortVlArbHighCapacity"),
        ("SMA-MIB", "ibSmaPortVlArbLowCapacity"),
        ("SMA-MIB", "ibSmaPortMtuCapacity"),
        ("SMA-MIB", "ibSmaPortVlStallCount"),
        ("SMA-MIB", "ibSmaPortHeadOfQueueLife"),
        ("SMA-MIB", "ibSmaPortOperationalVls"),
        ("SMA-MIB", "ibSmaPortPartEnforceInbound"),
        ("SMA-MIB", "ibSmaPortPartEnforceOutbound"),
        ("SMA-MIB", "ibSmaPortFilterRawPktInbound"),
        ("SMA-MIB", "ibSmaPortFilterRawPktOutbound"),
        ("SMA-MIB", "ibSmaPortLocalPhysErrorThreshold"),
        ("SMA-MIB", "ibSmaPortOverrunErrorThreshold"))
)
if mibBuilder.loadTexts:
    ibSmaDataPortGroup.setStatus("current")

ibSmaPKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 6)
)
ibSmaPKeyGroup.setObjects(
      *(("SMA-MIB", "ibSmaPKeyMembership"),
        ("SMA-MIB", "ibSmaPKeyBase"))
)
if mibBuilder.loadTexts:
    ibSmaPKeyGroup.setStatus("current")

ibSmaSlToVlMapGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 7)
)
ibSmaSlToVlMapGroup.setObjects(
    ("SMA-MIB", "ibSmaVirtualLane")
)
if mibBuilder.loadTexts:
    ibSmaSlToVlMapGroup.setStatus("current")

ibSmaVLArbitGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 8)
)
ibSmaVLArbitGroup.setObjects(
      *(("SMA-MIB", "ibSmaHiPriVirtLane"),
        ("SMA-MIB", "ibSmaHiPriWeight"),
        ("SMA-MIB", "ibSmaLowPriVirtLane"),
        ("SMA-MIB", "ibSmaLowPriWeight"))
)
if mibBuilder.loadTexts:
    ibSmaVLArbitGroup.setStatus("current")

ibSmaLFTGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 9)
)
ibSmaLFTGroup.setObjects(
    ("SMA-MIB", "ibSmaLinForwEgressPort")
)
if mibBuilder.loadTexts:
    ibSmaLFTGroup.setStatus("current")

ibSmaRFTGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 10)
)
ibSmaRFTGroup.setObjects(
      *(("SMA-MIB", "ibSmaRandomDestLID"),
        ("SMA-MIB", "ibSmaRandomForwEgressPort"),
        ("SMA-MIB", "ibSmaRandomLMC"),
        ("SMA-MIB", "ibSmaRandomIsValid"))
)
if mibBuilder.loadTexts:
    ibSmaRFTGroup.setStatus("current")

ibSmaMFTGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 11)
)
ibSmaMFTGroup.setObjects(
    ("SMA-MIB", "ibSmaMulForwMask")
)
if mibBuilder.loadTexts:
    ibSmaMFTGroup.setStatus("current")

ibSmaSMGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 12)
)
ibSmaSMGroup.setObjects(
      *(("SMA-MIB", "ibSmaSmGuid"),
        ("SMA-MIB", "ibSmaSmSmKey"),
        ("SMA-MIB", "ibSmaSmSmpCount"),
        ("SMA-MIB", "ibSmaSmPriority"),
        ("SMA-MIB", "ibSmaSmState"))
)
if mibBuilder.loadTexts:
    ibSmaSMGroup.setStatus("current")

ibSmaVendDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 13)
)
ibSmaVendDiagGroup.setObjects(
      *(("SMA-MIB", "ibSmaPortGenericDiagCode"),
        ("SMA-MIB", "ibSmaPortVendorDiagCode"),
        ("SMA-MIB", "ibSmaPortVendorDiagIndexFwd"),
        ("SMA-MIB", "ibSmaPortVendorDiagData"))
)
if mibBuilder.loadTexts:
    ibSmaVendDiagGroup.setStatus("current")

ibSmaLedGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 14)
)
ibSmaLedGroup.setObjects(
    ("SMA-MIB", "ibSmaLedState")
)
if mibBuilder.loadTexts:
    ibSmaLedGroup.setStatus("current")


# Notification objects

ibSmaPortLinkStateChange = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 1)
)
ibSmaPortLinkStateChange.setObjects(
    ("SMA-MIB", "ibSmaNodeLid")
)
if mibBuilder.loadTexts:
    ibSmaPortLinkStateChange.setStatus(
        "current"
    )

ibSmaLinkIntegrityThresReached = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 2)
)
ibSmaLinkIntegrityThresReached.setObjects(
      *(("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodePortNum"))
)
if mibBuilder.loadTexts:
    ibSmaLinkIntegrityThresReached.setStatus(
        "current"
    )

ibSmaExcessBuffOverrunThres = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 3)
)
ibSmaExcessBuffOverrunThres.setObjects(
      *(("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodePortNum"))
)
if mibBuilder.loadTexts:
    ibSmaExcessBuffOverrunThres.setStatus(
        "current"
    )

ibSmaFlowCntrlUpdateTimerExpire = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 4)
)
ibSmaFlowCntrlUpdateTimerExpire.setObjects(
      *(("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodePortNum"))
)
if mibBuilder.loadTexts:
    ibSmaFlowCntrlUpdateTimerExpire.setStatus(
        "current"
    )

ibSmaCapabilityMaskModified = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 5)
)
ibSmaCapabilityMaskModified.setObjects(
      *(("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodeCapMask"))
)
if mibBuilder.loadTexts:
    ibSmaCapabilityMaskModified.setStatus(
        "current"
    )

ibSmaSysImageGuidModified = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 6)
)
ibSmaSysImageGuidModified.setObjects(
      *(("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaSystemImageGuid"))
)
if mibBuilder.loadTexts:
    ibSmaSysImageGuidModified.setStatus(
        "current"
    )

ibSmaBadManagementKey = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 7)
)
ibSmaBadManagementKey.setObjects(
      *(("SMA-MIB", "ibSmaNodeKey"),
        ("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodeMethod"),
        ("SMA-MIB", "ibSmaNodeAttributeId"),
        ("SMA-MIB", "ibSmaNodeAttributeModifier"))
)
if mibBuilder.loadTexts:
    ibSmaBadManagementKey.setStatus(
        "current"
    )

ibSmaBadPartitionKey = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 8)
)
ibSmaBadPartitionKey.setObjects(
      *(("SMA-MIB", "ibSmaNodeKey"),
        ("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodeGid1"),
        ("SMA-MIB", "ibSmaNodeQueuePair1"),
        ("SMA-MIB", "ibSmaNodeLid2"),
        ("SMA-MIB", "ibSmaNodeGid2"),
        ("SMA-MIB", "ibSmaNodeQueuePair2"),
        ("SMA-MIB", "ibSmaNodeServiceLevel"))
)
if mibBuilder.loadTexts:
    ibSmaBadPartitionKey.setStatus(
        "current"
    )

ibSmaBadQueueKey = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 9)
)
ibSmaBadQueueKey.setObjects(
      *(("SMA-MIB", "ibSmaNodeKey"),
        ("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodeGid1"),
        ("SMA-MIB", "ibSmaNodeQueuePair1"),
        ("SMA-MIB", "ibSmaNodeLid2"),
        ("SMA-MIB", "ibSmaNodeGid2"),
        ("SMA-MIB", "ibSmaNodeQueuePair2"),
        ("SMA-MIB", "ibSmaNodeServiceLevel"))
)
if mibBuilder.loadTexts:
    ibSmaBadQueueKey.setStatus(
        "current"
    )

ibSmaBadPKeyAtSwitchPort = NotificationType(
    (1, 3, 6, 1, 3, 117, 3, 2, 10)
)
ibSmaBadPKeyAtSwitchPort.setObjects(
      *(("SMA-MIB", "ibSmaNodeKey"),
        ("SMA-MIB", "ibSmaNodeLid"),
        ("SMA-MIB", "ibSmaNodeGid1"),
        ("SMA-MIB", "ibSmaNodeQueuePair1"),
        ("SMA-MIB", "ibSmaNodeLid2"),
        ("SMA-MIB", "ibSmaNodeGid2"),
        ("SMA-MIB", "ibSmaNodeQueuePair2"),
        ("SMA-MIB", "ibSmaNodeServiceLevel"),
        ("SMA-MIB", "ibSmaNodeSwitchLid"),
        ("SMA-MIB", "ibSmaNodeDataValid"))
)
if mibBuilder.loadTexts:
    ibSmaBadPKeyAtSwitchPort.setStatus(
        "current"
    )


# Notifications groups

ibSmaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 117, 3, 3, 2, 15)
)
ibSmaNotificationsGroup.setObjects(
      *(("SMA-MIB", "ibSmaPortLinkStateChange"),
        ("SMA-MIB", "ibSmaLinkIntegrityThresReached"),
        ("SMA-MIB", "ibSmaExcessBuffOverrunThres"),
        ("SMA-MIB", "ibSmaFlowCntrlUpdateTimerExpire"),
        ("SMA-MIB", "ibSmaCapabilityMaskModified"),
        ("SMA-MIB", "ibSmaSysImageGuidModified"),
        ("SMA-MIB", "ibSmaBadManagementKey"),
        ("SMA-MIB", "ibSmaBadPartitionKey"),
        ("SMA-MIB", "ibSmaBadQueueKey"),
        ("SMA-MIB", "ibSmaBadPKeyAtSwitchPort"))
)
if mibBuilder.loadTexts:
    ibSmaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ibSmaBasicNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibSmaBasicNodeCompliance.setStatus(
        "current"
    )

ibSmaFullSwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibSmaFullSwitchCompliance.setStatus(
        "current"
    )

ibSmaFullRouterCACompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ibSmaFullRouterCACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMA-MIB",
    **{"ibSmaMIB": ibSmaMIB,
       "ibSmaObjects": ibSmaObjects,
       "ibSmaNodeInfo": ibSmaNodeInfo,
       "ibSmaNodeString": ibSmaNodeString,
       "ibSmaNodeBaseVersion": ibSmaNodeBaseVersion,
       "ibSmaNodeClassVersion": ibSmaNodeClassVersion,
       "ibSmaNodeType": ibSmaNodeType,
       "ibSmaNodeNumPorts": ibSmaNodeNumPorts,
       "ibSmaSystemImageGuid": ibSmaSystemImageGuid,
       "ibSmaNodeGuid": ibSmaNodeGuid,
       "ibSmaNodePortGuid": ibSmaNodePortGuid,
       "ibSmaNodePartitionTableNum": ibSmaNodePartitionTableNum,
       "ibSmaNodeDeviceId": ibSmaNodeDeviceId,
       "ibSmaNodeRevision": ibSmaNodeRevision,
       "ibSmaNodeLocalPortNumOrZero": ibSmaNodeLocalPortNumOrZero,
       "ibSmaNodeVendorId": ibSmaNodeVendorId,
       "ibSmaNodeLid": ibSmaNodeLid,
       "ibSmaNodePortNum": ibSmaNodePortNum,
       "ibSmaNodeMethod": ibSmaNodeMethod,
       "ibSmaNodeAttributeId": ibSmaNodeAttributeId,
       "ibSmaNodeAttributeModifier": ibSmaNodeAttributeModifier,
       "ibSmaNodeKey": ibSmaNodeKey,
       "ibSmaNodeLid2": ibSmaNodeLid2,
       "ibSmaNodeServiceLevel": ibSmaNodeServiceLevel,
       "ibSmaNodeQueuePair1": ibSmaNodeQueuePair1,
       "ibSmaNodeQueuePair2": ibSmaNodeQueuePair2,
       "ibSmaNodeGid1": ibSmaNodeGid1,
       "ibSmaNodeGid2": ibSmaNodeGid2,
       "ibSmaNodeCapMask": ibSmaNodeCapMask,
       "ibSmaNodeSwitchLid": ibSmaNodeSwitchLid,
       "ibSmaNodeDataValid": ibSmaNodeDataValid,
       "ibSmaSwitchInfo": ibSmaSwitchInfo,
       "ibSmaSwLinearFdbTableNum": ibSmaSwLinearFdbTableNum,
       "ibSmaSwRandomFdbTableNum": ibSmaSwRandomFdbTableNum,
       "ibSmaSwMulticastFdbTableNum": ibSmaSwMulticastFdbTableNum,
       "ibSmaSwLinearFdbTop": ibSmaSwLinearFdbTop,
       "ibSmaSwDefaultPort": ibSmaSwDefaultPort,
       "ibSmaSwDefMcastPriPort": ibSmaSwDefMcastPriPort,
       "ibSmaSwDefMcastNotPriPort": ibSmaSwDefMcastNotPriPort,
       "ibSmaSwLifeTimeValue": ibSmaSwLifeTimeValue,
       "ibSmaSwPortStateChange": ibSmaSwPortStateChange,
       "ibSmaSwLidsPerPort": ibSmaSwLidsPerPort,
       "ibSmaSwPartitionEnforceNum": ibSmaSwPartitionEnforceNum,
       "ibSmaSwInboundEnforceCap": ibSmaSwInboundEnforceCap,
       "ibSmaSwOutboundEnforceCap": ibSmaSwOutboundEnforceCap,
       "ibSmaSwFilterRawPktInputCap": ibSmaSwFilterRawPktInputCap,
       "ibSmaSwFilterRawPktOutputCap": ibSmaSwFilterRawPktOutputCap,
       "ibSmaSwEnhancedPort0": ibSmaSwEnhancedPort0,
       "ibSmaGuidInfo": ibSmaGuidInfo,
       "ibSmaGuidInfoTable": ibSmaGuidInfoTable,
       "ibGuidInfoEntry": ibGuidInfoEntry,
       "ibSmaGuidPortIndex": ibSmaGuidPortIndex,
       "ibSmaGuidIndex": ibSmaGuidIndex,
       "ibSmaGuidVal": ibSmaGuidVal,
       "ibSmaMgmtPortInfo": ibSmaMgmtPortInfo,
       "ibSmaPortMKey": ibSmaPortMKey,
       "ibSmaPortGidPrefix": ibSmaPortGidPrefix,
       "ibSmaPortLid": ibSmaPortLid,
       "ibSmaPortMasterSmLid": ibSmaPortMasterSmLid,
       "ibSmaPortIsSubnetManager": ibSmaPortIsSubnetManager,
       "ibSmaPortIsNoticeSupported": ibSmaPortIsNoticeSupported,
       "ibSmaPortIsTrapSupported": ibSmaPortIsTrapSupported,
       "ibSmaPortIsAutoMigrateSupported": ibSmaPortIsAutoMigrateSupported,
       "ibSmaPortIsSlMappingSupported": ibSmaPortIsSlMappingSupported,
       "ibSmaPortIsMKeyNvram": ibSmaPortIsMKeyNvram,
       "ibSmaPortIsPKeyNvram": ibSmaPortIsPKeyNvram,
       "ibSmaPortIsLedInfoSupported": ibSmaPortIsLedInfoSupported,
       "ibSmaPortIsSmDisabled": ibSmaPortIsSmDisabled,
       "ibSmaPortIsSysImgGuidSupported": ibSmaPortIsSysImgGuidSupported,
       "ibSmaPortIsPKeyExtPortTrapSup": ibSmaPortIsPKeyExtPortTrapSup,
       "ibSmaPortIsCommManageSupported": ibSmaPortIsCommManageSupported,
       "ibSmaPortIsSnmpTunnelSupported": ibSmaPortIsSnmpTunnelSupported,
       "ibSmaPortIsReinitSupported": ibSmaPortIsReinitSupported,
       "ibSmaPortIsDevManageSupported": ibSmaPortIsDevManageSupported,
       "ibSmaPortIsVendorClassSupported": ibSmaPortIsVendorClassSupported,
       "ibSmaPortIsDrNoticeSupported": ibSmaPortIsDrNoticeSupported,
       "ibSmaPortIsCapMaskNoticSupported": ibSmaPortIsCapMaskNoticSupported,
       "ibSmaPortIsBootMgmtSupported": ibSmaPortIsBootMgmtSupported,
       "ibSmaPortMKeyLeasePeriod": ibSmaPortMKeyLeasePeriod,
       "ibSmaPortMKeyProtectBits": ibSmaPortMKeyProtectBits,
       "ibSmaPortMasterSmSl": ibSmaPortMasterSmSl,
       "ibSmaPortInitTypeLoad": ibSmaPortInitTypeLoad,
       "ibSmaPortInitTypeContent": ibSmaPortInitTypeContent,
       "ibSmaPortInitTypePresence": ibSmaPortInitTypePresence,
       "ibSmaPortInitTypeResuscitate": ibSmaPortInitTypeResuscitate,
       "ibSmaPortInitNoLoadReply": ibSmaPortInitNoLoadReply,
       "ibSmaPortInitPreserveContReply": ibSmaPortInitPreserveContReply,
       "ibSmaPortInitPreservePresReply": ibSmaPortInitPreservePresReply,
       "ibSmaPortMKeyViolations": ibSmaPortMKeyViolations,
       "ibSmaPortPKeyViolations": ibSmaPortPKeyViolations,
       "ibSmaPortQKeyViolations": ibSmaPortQKeyViolations,
       "ibSmaPortNumGuid": ibSmaPortNumGuid,
       "ibSmaPortSubnetTimeout": ibSmaPortSubnetTimeout,
       "ibSmaPortResponseTimeValue": ibSmaPortResponseTimeValue,
       "ibSmaDataPortInfo": ibSmaDataPortInfo,
       "ibSmaPortInfoTable": ibSmaPortInfoTable,
       "ibSmaPortInfoEntry": ibSmaPortInfoEntry,
       "ibSmaPortIndex": ibSmaPortIndex,
       "ibSmaPortLinkWidthEnabled": ibSmaPortLinkWidthEnabled,
       "ibSmaPortLinkWidthSupported": ibSmaPortLinkWidthSupported,
       "ibSmaPortLinkWidthActive": ibSmaPortLinkWidthActive,
       "ibSmaPortLinkSpeedSupported": ibSmaPortLinkSpeedSupported,
       "ibSmaPortLinkState": ibSmaPortLinkState,
       "ibSmaPortPhysState": ibSmaPortPhysState,
       "ibSmaPortLinkDownDefaultState": ibSmaPortLinkDownDefaultState,
       "ibSmaPortLidMaskCount": ibSmaPortLidMaskCount,
       "ibSmaPortLinkSpeedActive": ibSmaPortLinkSpeedActive,
       "ibSmaPortLinkSpeedEnabled": ibSmaPortLinkSpeedEnabled,
       "ibSmaPortNeighborMtu": ibSmaPortNeighborMtu,
       "ibSmaPortVirtLaneSupport": ibSmaPortVirtLaneSupport,
       "ibSmaPortVlHighPriorityLimit": ibSmaPortVlHighPriorityLimit,
       "ibSmaPortVlArbHighCapacity": ibSmaPortVlArbHighCapacity,
       "ibSmaPortVlArbLowCapacity": ibSmaPortVlArbLowCapacity,
       "ibSmaPortMtuCapacity": ibSmaPortMtuCapacity,
       "ibSmaPortVlStallCount": ibSmaPortVlStallCount,
       "ibSmaPortHeadOfQueueLife": ibSmaPortHeadOfQueueLife,
       "ibSmaPortOperationalVls": ibSmaPortOperationalVls,
       "ibSmaPortPartEnforceInbound": ibSmaPortPartEnforceInbound,
       "ibSmaPortPartEnforceOutbound": ibSmaPortPartEnforceOutbound,
       "ibSmaPortFilterRawPktInbound": ibSmaPortFilterRawPktInbound,
       "ibSmaPortFilterRawPktOutbound": ibSmaPortFilterRawPktOutbound,
       "ibSmaPortLocalPhysErrorThreshold": ibSmaPortLocalPhysErrorThreshold,
       "ibSmaPortOverrunErrorThreshold": ibSmaPortOverrunErrorThreshold,
       "ibSmaPKeyInfo": ibSmaPKeyInfo,
       "ibSmaPKeyTable": ibSmaPKeyTable,
       "ibSmaPKeyEntry": ibSmaPKeyEntry,
       "ibSmaPKeyIBAPortIndex": ibSmaPKeyIBAPortIndex,
       "ibSmaPKeyIndex": ibSmaPKeyIndex,
       "ibSmaPKeyMembership": ibSmaPKeyMembership,
       "ibSmaPKeyBase": ibSmaPKeyBase,
       "ibSmaSlToVlMapInfo": ibSmaSlToVlMapInfo,
       "ibSmaSL2VLMapTable": ibSmaSL2VLMapTable,
       "ibSmaSL2VLMapEntry": ibSmaSL2VLMapEntry,
       "ibSmaIBAOutPortIndex": ibSmaIBAOutPortIndex,
       "ibSmaIBAInPortIndex": ibSmaIBAInPortIndex,
       "ibSmaServiceLevelIndex": ibSmaServiceLevelIndex,
       "ibSmaVirtualLane": ibSmaVirtualLane,
       "ibSmaVLArbitInfo": ibSmaVLArbitInfo,
       "ibSmaHiPriVlArbTable": ibSmaHiPriVlArbTable,
       "ibSmaHiPriVlArbEntry": ibSmaHiPriVlArbEntry,
       "ibSmaHiPriIBAPortIndex": ibSmaHiPriIBAPortIndex,
       "ibSmaHiPriNIndex": ibSmaHiPriNIndex,
       "ibSmaHiPriVirtLane": ibSmaHiPriVirtLane,
       "ibSmaHiPriWeight": ibSmaHiPriWeight,
       "ibSmaLowPriVlArbTable": ibSmaLowPriVlArbTable,
       "ibSmaLowPriVlArbEntry": ibSmaLowPriVlArbEntry,
       "ibSmaLowPriIBAPortIndex": ibSmaLowPriIBAPortIndex,
       "ibSmaLowPriNIndex": ibSmaLowPriNIndex,
       "ibSmaLowPriVirtLane": ibSmaLowPriVirtLane,
       "ibSmaLowPriWeight": ibSmaLowPriWeight,
       "ibSmaLFTInfo": ibSmaLFTInfo,
       "ibSmaLinForTable": ibSmaLinForTable,
       "ibSmaLinForEntry": ibSmaLinForEntry,
       "ibSmaLinDestDLIDIndex": ibSmaLinDestDLIDIndex,
       "ibSmaLinForwEgressPort": ibSmaLinForwEgressPort,
       "ibSmaRFTInfo": ibSmaRFTInfo,
       "ibSmaRandomForwardingTable": ibSmaRandomForwardingTable,
       "ibSmaRandomForwardingEntry": ibSmaRandomForwardingEntry,
       "ibSmaRandomForwardingPortIndex": ibSmaRandomForwardingPortIndex,
       "ibSmaRandomDestLID": ibSmaRandomDestLID,
       "ibSmaRandomForwEgressPort": ibSmaRandomForwEgressPort,
       "ibSmaRandomLMC": ibSmaRandomLMC,
       "ibSmaRandomIsValid": ibSmaRandomIsValid,
       "ibSmaMFTInfo": ibSmaMFTInfo,
       "ibSmaMulForTable": ibSmaMulForTable,
       "ibSmaMulForEntry": ibSmaMulForEntry,
       "ibSmaMulDestDLIDIndex": ibSmaMulDestDLIDIndex,
       "ibSmaMulForwMask": ibSmaMulForwMask,
       "ibSmaSMInfo": ibSmaSMInfo,
       "ibSmaSubMgrInfo": ibSmaSubMgrInfo,
       "ibSmaSmInfoTable": ibSmaSmInfoTable,
       "ibSmaSmInfoEntry": ibSmaSmInfoEntry,
       "ibSmaSmInfoPortIndex": ibSmaSmInfoPortIndex,
       "ibSmaSmGuid": ibSmaSmGuid,
       "ibSmaSmSmKey": ibSmaSmSmKey,
       "ibSmaSmSmpCount": ibSmaSmSmpCount,
       "ibSmaSmPriority": ibSmaSmPriority,
       "ibSmaSmState": ibSmaSmState,
       "ibSmaVendDiagInfo": ibSmaVendDiagInfo,
       "ibSmaVendDiagInfoTable": ibSmaVendDiagInfoTable,
       "ibSmaVendDiagInfoEntry": ibSmaVendDiagInfoEntry,
       "ibSmaVendDiagPortIndex": ibSmaVendDiagPortIndex,
       "ibSmaPortGenericDiagCode": ibSmaPortGenericDiagCode,
       "ibSmaPortVendorDiagCode": ibSmaPortVendorDiagCode,
       "ibSmaPortVendorDiagIndexFwd": ibSmaPortVendorDiagIndexFwd,
       "ibSmaPortVendorDiagData": ibSmaPortVendorDiagData,
       "ibSmaLedInfo": ibSmaLedInfo,
       "ibSmaLedInfoTable": ibSmaLedInfoTable,
       "ibSmaLedInfoEntry": ibSmaLedInfoEntry,
       "ibSmaLedIndex": ibSmaLedIndex,
       "ibSmaLedState": ibSmaLedState,
       "ibSmaNotifications": ibSmaNotifications,
       "ibSmaNotificationPrefix": ibSmaNotificationPrefix,
       "ibSmaPortLinkStateChange": ibSmaPortLinkStateChange,
       "ibSmaLinkIntegrityThresReached": ibSmaLinkIntegrityThresReached,
       "ibSmaExcessBuffOverrunThres": ibSmaExcessBuffOverrunThres,
       "ibSmaFlowCntrlUpdateTimerExpire": ibSmaFlowCntrlUpdateTimerExpire,
       "ibSmaCapabilityMaskModified": ibSmaCapabilityMaskModified,
       "ibSmaSysImageGuidModified": ibSmaSysImageGuidModified,
       "ibSmaBadManagementKey": ibSmaBadManagementKey,
       "ibSmaBadPartitionKey": ibSmaBadPartitionKey,
       "ibSmaBadQueueKey": ibSmaBadQueueKey,
       "ibSmaBadPKeyAtSwitchPort": ibSmaBadPKeyAtSwitchPort,
       "ibSmaConformance": ibSmaConformance,
       "ibSmaCompliances": ibSmaCompliances,
       "ibSmaBasicNodeCompliance": ibSmaBasicNodeCompliance,
       "ibSmaFullSwitchCompliance": ibSmaFullSwitchCompliance,
       "ibSmaFullRouterCACompliance": ibSmaFullRouterCACompliance,
       "ibSmaGroups": ibSmaGroups,
       "ibSmaNodeGroup": ibSmaNodeGroup,
       "ibSmaSwitchGroup": ibSmaSwitchGroup,
       "ibSmaGuidGroup": ibSmaGuidGroup,
       "ibSmaMgmtPortGroup": ibSmaMgmtPortGroup,
       "ibSmaDataPortGroup": ibSmaDataPortGroup,
       "ibSmaPKeyGroup": ibSmaPKeyGroup,
       "ibSmaSlToVlMapGroup": ibSmaSlToVlMapGroup,
       "ibSmaVLArbitGroup": ibSmaVLArbitGroup,
       "ibSmaLFTGroup": ibSmaLFTGroup,
       "ibSmaRFTGroup": ibSmaRFTGroup,
       "ibSmaMFTGroup": ibSmaMFTGroup,
       "ibSmaSMGroup": ibSmaSMGroup,
       "ibSmaVendDiagGroup": ibSmaVendDiagGroup,
       "ibSmaLedGroup": ibSmaLedGroup,
       "ibSmaNotificationsGroup": ibSmaNotificationsGroup}
)
