# SNMP MIB module (NETI-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-ETH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:33 2024
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

(Dsti,) = mibBuilder.importSymbols(
    "NETI-CHMGR-MIB",
    "Dsti")

(netiGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiGeneric")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netiEthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2)
)
netiEthMIB.setRevisions(
        ("2014-03-20 10:00",
         "2013-02-28 10:00",
         "2012-09-12 10:00",
         "2012-01-27 15:00",
         "2011-10-26 09:00",
         "2011-09-05 11:00",
         "2010-10-20 16:00",
         "2009-07-08 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrafficClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class VLANSet(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )



class AdvertisedSpeed(Bits, TextualConvention):
    status = "current"


class AdvertisedDuplex(Bits, TextualConvention):
    status = "current"


class AdvertisedFlowControl(Bits, TextualConvention):
    status = "current"


class BridgeIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class EthInterfaceType(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("b1000baseLX", 5),
          ("b1000baseSX", 4),
          ("b1000baseT", 6),
          ("b100baseTX", 3),
          ("b10GbaseER", 11),
          ("b10GbaseLR", 9),
          ("b10GbaseLRM", 10),
          ("b10GbaseSR", 8),
          ("b10GbaseZR", 12),
          ("bETS", 2),
          ("bETSGroup", 7),
          ("unknown", 1))
    )



class PortIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class FrameProcess(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("notSupported", 0))
    )



class InterfaceIndexList(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d,"


class IfgProtectionStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("hitlessCapable", 4),
          ("hitlessProtected", 5),
          ("standbyProtected", 3),
          ("unavailable", 1),
          ("unprotected", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EthObjects_ObjectIdentity = ObjectIdentity
ethObjects = _EthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1)
)
_EthDeviceGroup_ObjectIdentity = ObjectIdentity
ethDeviceGroup = _EthDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1)
)
_EthDeviceTable_Object = MibTable
ethDeviceTable = _EthDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ethDeviceTable.setStatus("current")
_EthDeviceEntry_Object = MibTableRow
ethDeviceEntry = _EthDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1)
)
ethDeviceEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
)
if mibBuilder.loadTexts:
    ethDeviceEntry.setStatus("current")
_EthDevIndex_Type = Unsigned32
_EthDevIndex_Object = MibTableColumn
ethDevIndex = _EthDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 1),
    _EthDevIndex_Type()
)
ethDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethDevIndex.setStatus("current")
_EthDevRowStatus_Type = RowStatus
_EthDevRowStatus_Object = MibTableColumn
ethDevRowStatus = _EthDevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 2),
    _EthDevRowStatus_Type()
)
ethDevRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDevRowStatus.setStatus("current")
_EthDevName_Type = SnmpAdminString
_EthDevName_Object = MibTableColumn
ethDevName = _EthDevName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 3),
    _EthDevName_Type()
)
ethDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevName.setStatus("current")
_EthDevContainerName_Type = SnmpAdminString
_EthDevContainerName_Object = MibTableColumn
ethDevContainerName = _EthDevContainerName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 4),
    _EthDevContainerName_Type()
)
ethDevContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevContainerName.setStatus("current")
_EthDevProductName_Type = SnmpAdminString
_EthDevProductName_Object = MibTableColumn
ethDevProductName = _EthDevProductName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 5),
    _EthDevProductName_Type()
)
ethDevProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevProductName.setStatus("current")


class _EthDevStatus_Type(Integer32):
    """Custom type ethDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("mismatch", 3),
          ("present", 1))
    )


_EthDevStatus_Type.__name__ = "Integer32"
_EthDevStatus_Object = MibTableColumn
ethDevStatus = _EthDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 6),
    _EthDevStatus_Type()
)
ethDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevStatus.setStatus("current")


class _EthDevCapJumboFrames_Type(Bits):
    """Custom type ethDevCapJumboFrames based on Bits"""
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )

_EthDevCapJumboFrames_Type.__name__ = "Bits"
_EthDevCapJumboFrames_Object = MibTableColumn
ethDevCapJumboFrames = _EthDevCapJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 7),
    _EthDevCapJumboFrames_Type()
)
ethDevCapJumboFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapJumboFrames.setStatus("current")
_EthDevCapMaxAgingTime_Type = Unsigned32
_EthDevCapMaxAgingTime_Object = MibTableColumn
ethDevCapMaxAgingTime = _EthDevCapMaxAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 8),
    _EthDevCapMaxAgingTime_Type()
)
ethDevCapMaxAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapMaxAgingTime.setStatus("current")


class _EthDevCapMACMode_Type(Bits):
    """Custom type ethDevCapMACMode based on Bits"""
    namedValues = NamedValues(
        *(("auto", 0),
          ("mac", 1),
          ("nomac", 2))
    )

_EthDevCapMACMode_Type.__name__ = "Bits"
_EthDevCapMACMode_Object = MibTableColumn
ethDevCapMACMode = _EthDevCapMACMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 9),
    _EthDevCapMACMode_Type()
)
ethDevCapMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapMACMode.setStatus("current")


class _EthDevCapSpanningTree_Type(Bits):
    """Custom type ethDevCapSpanningTree based on Bits"""
    namedValues = NamedValues(
        *(("auto", 0),
          ("drop", 2),
          ("forward", 1),
          ("process", 3))
    )

_EthDevCapSpanningTree_Type.__name__ = "Bits"
_EthDevCapSpanningTree_Object = MibTableColumn
ethDevCapSpanningTree = _EthDevCapSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 10),
    _EthDevCapSpanningTree_Type()
)
ethDevCapSpanningTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapSpanningTree.setStatus("current")


class _EthDevCapVLANMode_Type(Bits):
    """Custom type ethDevCapVLANMode based on Bits"""
    namedValues = NamedValues(
        *(("customer", 1),
          ("provider", 2),
          ("transparent", 0))
    )

_EthDevCapVLANMode_Type.__name__ = "Bits"
_EthDevCapVLANMode_Object = MibTableColumn
ethDevCapVLANMode = _EthDevCapVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 11),
    _EthDevCapVLANMode_Type()
)
ethDevCapVLANMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapVLANMode.setStatus("current")
_EthDevCapAdvertisedDuplex_Type = AdvertisedDuplex
_EthDevCapAdvertisedDuplex_Object = MibTableColumn
ethDevCapAdvertisedDuplex = _EthDevCapAdvertisedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 12),
    _EthDevCapAdvertisedDuplex_Type()
)
ethDevCapAdvertisedDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapAdvertisedDuplex.setStatus("current")
_EthDevCapAdvertisedFlowControl_Type = AdvertisedFlowControl
_EthDevCapAdvertisedFlowControl_Object = MibTableColumn
ethDevCapAdvertisedFlowControl = _EthDevCapAdvertisedFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 13),
    _EthDevCapAdvertisedFlowControl_Type()
)
ethDevCapAdvertisedFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapAdvertisedFlowControl.setStatus("current")


class _EthDevCapAcceptableFrameType_Type(Bits):
    """Custom type ethDevCapAcceptableFrameType based on Bits"""
    namedValues = NamedValues(
        *(("all", 0),
          ("untagged", 2),
          ("vlanTagged", 1))
    )

_EthDevCapAcceptableFrameType_Type.__name__ = "Bits"
_EthDevCapAcceptableFrameType_Object = MibTableColumn
ethDevCapAcceptableFrameType = _EthDevCapAcceptableFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 14),
    _EthDevCapAcceptableFrameType_Type()
)
ethDevCapAcceptableFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapAcceptableFrameType.setStatus("current")


class _EthDevCapDefaultEthernetPriority_Type(OctetString):
    """Custom type ethDevCapDefaultEthernetPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EthDevCapDefaultEthernetPriority_Type.__name__ = "OctetString"
_EthDevCapDefaultEthernetPriority_Object = MibTableColumn
ethDevCapDefaultEthernetPriority = _EthDevCapDefaultEthernetPriority_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 15),
    _EthDevCapDefaultEthernetPriority_Type()
)
ethDevCapDefaultEthernetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapDefaultEthernetPriority.setStatus("current")


class _EthDevCapLearning_Type(Bits):
    """Custom type ethDevCapLearning based on Bits"""
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )

_EthDevCapLearning_Type.__name__ = "Bits"
_EthDevCapLearning_Object = MibTableColumn
ethDevCapLearning = _EthDevCapLearning_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 16),
    _EthDevCapLearning_Type()
)
ethDevCapLearning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapLearning.setStatus("current")


class _EthDevCapTransmittedFrameTypeETS_Type(Bits):
    """Custom type ethDevCapTransmittedFrameTypeETS based on Bits"""
    namedValues = NamedValues(
        *(("legacy", 3),
          ("untagged", 2),
          ("vlanTagged", 1))
    )

_EthDevCapTransmittedFrameTypeETS_Type.__name__ = "Bits"
_EthDevCapTransmittedFrameTypeETS_Object = MibTableColumn
ethDevCapTransmittedFrameTypeETS = _EthDevCapTransmittedFrameTypeETS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 17),
    _EthDevCapTransmittedFrameTypeETS_Type()
)
ethDevCapTransmittedFrameTypeETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapTransmittedFrameTypeETS.setStatus("current")


class _EthDevCapTransmittedFrameTypeDot3_Type(Bits):
    """Custom type ethDevCapTransmittedFrameTypeDot3 based on Bits"""
    namedValues = NamedValues(
        *(("untagged", 2),
          ("vlanTagged", 1))
    )

_EthDevCapTransmittedFrameTypeDot3_Type.__name__ = "Bits"
_EthDevCapTransmittedFrameTypeDot3_Object = MibTableColumn
ethDevCapTransmittedFrameTypeDot3 = _EthDevCapTransmittedFrameTypeDot3_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 18),
    _EthDevCapTransmittedFrameTypeDot3_Type()
)
ethDevCapTransmittedFrameTypeDot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapTransmittedFrameTypeDot3.setStatus("current")
_EthDevCapMaxMaxQueueOctets_Type = Unsigned32
_EthDevCapMaxMaxQueueOctets_Object = MibTableColumn
ethDevCapMaxMaxQueueOctets = _EthDevCapMaxMaxQueueOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 19),
    _EthDevCapMaxMaxQueueOctets_Type()
)
ethDevCapMaxMaxQueueOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapMaxMaxQueueOctets.setStatus("current")
_EthDevCapMaxMaxQueueFrames_Type = Unsigned32
_EthDevCapMaxMaxQueueFrames_Object = MibTableColumn
ethDevCapMaxMaxQueueFrames = _EthDevCapMaxMaxQueueFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 20),
    _EthDevCapMaxMaxQueueFrames_Type()
)
ethDevCapMaxMaxQueueFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapMaxMaxQueueFrames.setStatus("deprecated")
_EthDevCapMaxTrafficClass_Type = TrafficClass
_EthDevCapMaxTrafficClass_Object = MibTableColumn
ethDevCapMaxTrafficClass = _EthDevCapMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 21),
    _EthDevCapMaxTrafficClass_Type()
)
ethDevCapMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapMaxTrafficClass.setStatus("current")
_EthDevEtsNextIndex_Type = Unsigned32
_EthDevEtsNextIndex_Object = MibTableColumn
ethDevEtsNextIndex = _EthDevEtsNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 22),
    _EthDevEtsNextIndex_Type()
)
ethDevEtsNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevEtsNextIndex.setStatus("current")
_EthDevFwdFuncNextIndex_Type = Unsigned32
_EthDevFwdFuncNextIndex_Object = MibTableColumn
ethDevFwdFuncNextIndex = _EthDevFwdFuncNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 23),
    _EthDevFwdFuncNextIndex_Type()
)
ethDevFwdFuncNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevFwdFuncNextIndex.setStatus("current")


class _EthDevCapPerformanceMonitoring_Type(Integer32):
    """Custom type ethDevCapPerformanceMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EthDevCapPerformanceMonitoring_Type.__name__ = "Integer32"
_EthDevCapPerformanceMonitoring_Object = MibTableColumn
ethDevCapPerformanceMonitoring = _EthDevCapPerformanceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 24),
    _EthDevCapPerformanceMonitoring_Type()
)
ethDevCapPerformanceMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapPerformanceMonitoring.setStatus("current")


class _EthDevCapConfigurableFaultMgmt_Type(Integer32):
    """Custom type ethDevCapConfigurableFaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EthDevCapConfigurableFaultMgmt_Type.__name__ = "Integer32"
_EthDevCapConfigurableFaultMgmt_Object = MibTableColumn
ethDevCapConfigurableFaultMgmt = _EthDevCapConfigurableFaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 25),
    _EthDevCapConfigurableFaultMgmt_Type()
)
ethDevCapConfigurableFaultMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapConfigurableFaultMgmt.setStatus("current")
_EthDevIfgFirstIndex_Type = Unsigned32
_EthDevIfgFirstIndex_Object = MibTableColumn
ethDevIfgFirstIndex = _EthDevIfgFirstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 26),
    _EthDevIfgFirstIndex_Type()
)
ethDevIfgFirstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevIfgFirstIndex.setStatus("current")
_EthDevIfgNextIndex_Type = Unsigned32
_EthDevIfgNextIndex_Object = MibTableColumn
ethDevIfgNextIndex = _EthDevIfgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 27),
    _EthDevIfgNextIndex_Type()
)
ethDevIfgNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevIfgNextIndex.setStatus("current")
_EthDevCapDropPrecedenceLevels_Type = Unsigned32
_EthDevCapDropPrecedenceLevels_Object = MibTableColumn
ethDevCapDropPrecedenceLevels = _EthDevCapDropPrecedenceLevels_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 28),
    _EthDevCapDropPrecedenceLevels_Type()
)
ethDevCapDropPrecedenceLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapDropPrecedenceLevels.setStatus("current")


class _EthDevCapDropProbabilityFunctions_Type(Bits):
    """Custom type ethDevCapDropProbabilityFunctions based on Bits"""
    namedValues = NamedValues(
        *(("taildrop", 0),
          ("wred", 1))
    )

_EthDevCapDropProbabilityFunctions_Type.__name__ = "Bits"
_EthDevCapDropProbabilityFunctions_Object = MibTableColumn
ethDevCapDropProbabilityFunctions = _EthDevCapDropProbabilityFunctions_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 29),
    _EthDevCapDropProbabilityFunctions_Type()
)
ethDevCapDropProbabilityFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevCapDropProbabilityFunctions.setStatus("current")
_EthDevFailure_Type = SnmpAdminString
_EthDevFailure_Object = MibTableColumn
ethDevFailure = _EthDevFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 1, 1, 1, 30),
    _EthDevFailure_Type()
)
ethDevFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDevFailure.setStatus("current")
_EthFwdFuncGroup_ObjectIdentity = ObjectIdentity
ethFwdFuncGroup = _EthFwdFuncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2)
)
_EthFwdFuncLastChange_Type = TimeStamp
_EthFwdFuncLastChange_Object = MibScalar
ethFwdFuncLastChange = _EthFwdFuncLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 1),
    _EthFwdFuncLastChange_Type()
)
ethFwdFuncLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdFuncLastChange.setStatus("current")
_EthFwdFuncTable_Object = MibTable
ethFwdFuncTable = _EthFwdFuncTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ethFwdFuncTable.setStatus("current")
_EthFwdFuncEntry_Object = MibTableRow
ethFwdFuncEntry = _EthFwdFuncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1)
)
ethFwdFuncEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethFwdIndex"),
)
if mibBuilder.loadTexts:
    ethFwdFuncEntry.setStatus("current")


class _EthFwdIndex_Type(Integer32):
    """Custom type ethFwdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EthFwdIndex_Type.__name__ = "Integer32"
_EthFwdIndex_Object = MibTableColumn
ethFwdIndex = _EthFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 1),
    _EthFwdIndex_Type()
)
ethFwdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethFwdIndex.setStatus("current")
_EthFwdRowStatus_Type = RowStatus
_EthFwdRowStatus_Object = MibTableColumn
ethFwdRowStatus = _EthFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 2),
    _EthFwdRowStatus_Type()
)
ethFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethFwdRowStatus.setStatus("current")
_EthFwdName_Type = SnmpAdminString
_EthFwdName_Object = MibTableColumn
ethFwdName = _EthFwdName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 3),
    _EthFwdName_Type()
)
ethFwdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdName.setStatus("current")


class _EthFwdCustomerId_Type(Unsigned32):
    """Custom type ethFwdCustomerId based on Unsigned32"""
    defaultValue = 0


_EthFwdCustomerId_Object = MibTableColumn
ethFwdCustomerId = _EthFwdCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 4),
    _EthFwdCustomerId_Type()
)
ethFwdCustomerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethFwdCustomerId.setStatus("current")


class _EthFwdPurpose_Type(SnmpAdminString):
    """Custom type ethFwdPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_EthFwdPurpose_Object = MibTableColumn
ethFwdPurpose = _EthFwdPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 5),
    _EthFwdPurpose_Type()
)
ethFwdPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethFwdPurpose.setStatus("current")


class _EthFwdJumboFrames_Type(Integer32):
    """Custom type ethFwdJumboFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EthFwdJumboFrames_Type.__name__ = "Integer32"
_EthFwdJumboFrames_Object = MibTableColumn
ethFwdJumboFrames = _EthFwdJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 6),
    _EthFwdJumboFrames_Type()
)
ethFwdJumboFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdJumboFrames.setStatus("current")


class _EthFwdMACMode_Type(Integer32):
    """Custom type ethFwdMACMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mac", 2),
          ("nomac", 3))
    )


_EthFwdMACMode_Type.__name__ = "Integer32"
_EthFwdMACMode_Object = MibTableColumn
ethFwdMACMode = _EthFwdMACMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 7),
    _EthFwdMACMode_Type()
)
ethFwdMACMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMACMode.setStatus("current")


class _EthFwdCurrentMACMode_Type(Integer32):
    """Custom type ethFwdCurrentMACMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 2),
          ("nomac", 3))
    )


_EthFwdCurrentMACMode_Type.__name__ = "Integer32"
_EthFwdCurrentMACMode_Object = MibTableColumn
ethFwdCurrentMACMode = _EthFwdCurrentMACMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 8),
    _EthFwdCurrentMACMode_Type()
)
ethFwdCurrentMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdCurrentMACMode.setStatus("current")


class _EthFwdSpanningTree_Type(Integer32):
    """Custom type ethFwdSpanningTree based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("drop", 3),
          ("forward", 2),
          ("process", 4))
    )


_EthFwdSpanningTree_Type.__name__ = "Integer32"
_EthFwdSpanningTree_Object = MibTableColumn
ethFwdSpanningTree = _EthFwdSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 9),
    _EthFwdSpanningTree_Type()
)
ethFwdSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdSpanningTree.setStatus("current")


class _EthFwdVLANMode_Type(Integer32):
    """Custom type ethFwdVLANMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customer", 2),
          ("provider", 3),
          ("transparent", 1))
    )


_EthFwdVLANMode_Type.__name__ = "Integer32"
_EthFwdVLANMode_Object = MibTableColumn
ethFwdVLANMode = _EthFwdVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 10),
    _EthFwdVLANMode_Type()
)
ethFwdVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdVLANMode.setStatus("current")


class _EthFwdAgingTime_Type(Unsigned32):
    """Custom type ethFwdAgingTime based on Unsigned32"""
    defaultValue = 300


_EthFwdAgingTime_Object = MibTableColumn
ethFwdAgingTime = _EthFwdAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 11),
    _EthFwdAgingTime_Type()
)
ethFwdAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdAgingTime.setUnits("seconds")
_EthFwdFailure_Type = SnmpAdminString
_EthFwdFailure_Object = MibTableColumn
ethFwdFailure = _EthFwdFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 12),
    _EthFwdFailure_Type()
)
ethFwdFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdFailure.setStatus("current")
_EthFwdLastChange_Type = TimeTicks
_EthFwdLastChange_Object = MibTableColumn
ethFwdLastChange = _EthFwdLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 13),
    _EthFwdLastChange_Type()
)
ethFwdLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdLastChange.setStatus("current")


class _EthFwdPropagateFaults_Type(TruthValue):
    """Custom type ethFwdPropagateFaults based on TruthValue"""


_EthFwdPropagateFaults_Object = MibTableColumn
ethFwdPropagateFaults = _EthFwdPropagateFaults_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 14),
    _EthFwdPropagateFaults_Type()
)
ethFwdPropagateFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdPropagateFaults.setStatus("current")


class _EthFwdReservedAddr0180C2000002_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000002 based on FrameProcess"""


_EthFwdReservedAddr0180C2000002_Object = MibTableColumn
ethFwdReservedAddr0180C2000002 = _EthFwdReservedAddr0180C2000002_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 15),
    _EthFwdReservedAddr0180C2000002_Type()
)
ethFwdReservedAddr0180C2000002.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000002.setStatus("current")


class _EthFwdReservedAddr0180C2000003_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000003 based on FrameProcess"""


_EthFwdReservedAddr0180C2000003_Object = MibTableColumn
ethFwdReservedAddr0180C2000003 = _EthFwdReservedAddr0180C2000003_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 16),
    _EthFwdReservedAddr0180C2000003_Type()
)
ethFwdReservedAddr0180C2000003.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000003.setStatus("current")


class _EthFwdReservedAddr0180C2000004_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000004 based on FrameProcess"""


_EthFwdReservedAddr0180C2000004_Object = MibTableColumn
ethFwdReservedAddr0180C2000004 = _EthFwdReservedAddr0180C2000004_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 17),
    _EthFwdReservedAddr0180C2000004_Type()
)
ethFwdReservedAddr0180C2000004.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000004.setStatus("current")


class _EthFwdReservedAddr0180C2000005_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000005 based on FrameProcess"""


_EthFwdReservedAddr0180C2000005_Object = MibTableColumn
ethFwdReservedAddr0180C2000005 = _EthFwdReservedAddr0180C2000005_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 18),
    _EthFwdReservedAddr0180C2000005_Type()
)
ethFwdReservedAddr0180C2000005.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000005.setStatus("current")


class _EthFwdReservedAddr0180C2000006_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000006 based on FrameProcess"""


_EthFwdReservedAddr0180C2000006_Object = MibTableColumn
ethFwdReservedAddr0180C2000006 = _EthFwdReservedAddr0180C2000006_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 19),
    _EthFwdReservedAddr0180C2000006_Type()
)
ethFwdReservedAddr0180C2000006.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000006.setStatus("current")


class _EthFwdReservedAddr0180C2000007_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000007 based on FrameProcess"""


_EthFwdReservedAddr0180C2000007_Object = MibTableColumn
ethFwdReservedAddr0180C2000007 = _EthFwdReservedAddr0180C2000007_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 20),
    _EthFwdReservedAddr0180C2000007_Type()
)
ethFwdReservedAddr0180C2000007.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000007.setStatus("current")


class _EthFwdReservedAddr0180C2000008_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000008 based on FrameProcess"""


_EthFwdReservedAddr0180C2000008_Object = MibTableColumn
ethFwdReservedAddr0180C2000008 = _EthFwdReservedAddr0180C2000008_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 21),
    _EthFwdReservedAddr0180C2000008_Type()
)
ethFwdReservedAddr0180C2000008.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000008.setStatus("current")


class _EthFwdReservedAddr0180C2000009_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C2000009 based on FrameProcess"""


_EthFwdReservedAddr0180C2000009_Object = MibTableColumn
ethFwdReservedAddr0180C2000009 = _EthFwdReservedAddr0180C2000009_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 22),
    _EthFwdReservedAddr0180C2000009_Type()
)
ethFwdReservedAddr0180C2000009.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C2000009.setStatus("current")


class _EthFwdReservedAddr0180C200000A_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C200000A based on FrameProcess"""


_EthFwdReservedAddr0180C200000A_Object = MibTableColumn
ethFwdReservedAddr0180C200000A = _EthFwdReservedAddr0180C200000A_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 23),
    _EthFwdReservedAddr0180C200000A_Type()
)
ethFwdReservedAddr0180C200000A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C200000A.setStatus("current")


class _EthFwdReservedAddr0180C200000B_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C200000B based on FrameProcess"""


_EthFwdReservedAddr0180C200000B_Object = MibTableColumn
ethFwdReservedAddr0180C200000B = _EthFwdReservedAddr0180C200000B_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 24),
    _EthFwdReservedAddr0180C200000B_Type()
)
ethFwdReservedAddr0180C200000B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C200000B.setStatus("current")


class _EthFwdReservedAddr0180C200000C_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C200000C based on FrameProcess"""


_EthFwdReservedAddr0180C200000C_Object = MibTableColumn
ethFwdReservedAddr0180C200000C = _EthFwdReservedAddr0180C200000C_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 25),
    _EthFwdReservedAddr0180C200000C_Type()
)
ethFwdReservedAddr0180C200000C.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C200000C.setStatus("current")


class _EthFwdReservedAddr0180C200000D_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C200000D based on FrameProcess"""


_EthFwdReservedAddr0180C200000D_Object = MibTableColumn
ethFwdReservedAddr0180C200000D = _EthFwdReservedAddr0180C200000D_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 26),
    _EthFwdReservedAddr0180C200000D_Type()
)
ethFwdReservedAddr0180C200000D.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C200000D.setStatus("current")


class _EthFwdReservedAddr0180C200000E_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C200000E based on FrameProcess"""


_EthFwdReservedAddr0180C200000E_Object = MibTableColumn
ethFwdReservedAddr0180C200000E = _EthFwdReservedAddr0180C200000E_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 27),
    _EthFwdReservedAddr0180C200000E_Type()
)
ethFwdReservedAddr0180C200000E.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C200000E.setStatus("current")


class _EthFwdReservedAddr0180C200000F_Type(FrameProcess):
    """Custom type ethFwdReservedAddr0180C200000F based on FrameProcess"""


_EthFwdReservedAddr0180C200000F_Object = MibTableColumn
ethFwdReservedAddr0180C200000F = _EthFwdReservedAddr0180C200000F_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 28),
    _EthFwdReservedAddr0180C200000F_Type()
)
ethFwdReservedAddr0180C200000F.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdReservedAddr0180C200000F.setStatus("current")


class _EthFwdCurrentStpMode_Type(Integer32):
    """Custom type ethFwdCurrentStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("forward", 2),
          ("process", 4))
    )


_EthFwdCurrentStpMode_Type.__name__ = "Integer32"
_EthFwdCurrentStpMode_Object = MibTableColumn
ethFwdCurrentStpMode = _EthFwdCurrentStpMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 29),
    _EthFwdCurrentStpMode_Type()
)
ethFwdCurrentStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdCurrentStpMode.setStatus("current")


class _EthFwdMrpAddr0180C2000020_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000020 based on FrameProcess"""


_EthFwdMrpAddr0180C2000020_Object = MibTableColumn
ethFwdMrpAddr0180C2000020 = _EthFwdMrpAddr0180C2000020_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 30),
    _EthFwdMrpAddr0180C2000020_Type()
)
ethFwdMrpAddr0180C2000020.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000020.setStatus("current")


class _EthFwdMrpAddr0180C2000021_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000021 based on FrameProcess"""


_EthFwdMrpAddr0180C2000021_Object = MibTableColumn
ethFwdMrpAddr0180C2000021 = _EthFwdMrpAddr0180C2000021_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 31),
    _EthFwdMrpAddr0180C2000021_Type()
)
ethFwdMrpAddr0180C2000021.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000021.setStatus("current")


class _EthFwdMrpAddr0180C2000022_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000022 based on FrameProcess"""


_EthFwdMrpAddr0180C2000022_Object = MibTableColumn
ethFwdMrpAddr0180C2000022 = _EthFwdMrpAddr0180C2000022_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 32),
    _EthFwdMrpAddr0180C2000022_Type()
)
ethFwdMrpAddr0180C2000022.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000022.setStatus("current")


class _EthFwdMrpAddr0180C2000023_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000023 based on FrameProcess"""


_EthFwdMrpAddr0180C2000023_Object = MibTableColumn
ethFwdMrpAddr0180C2000023 = _EthFwdMrpAddr0180C2000023_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 33),
    _EthFwdMrpAddr0180C2000023_Type()
)
ethFwdMrpAddr0180C2000023.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000023.setStatus("current")


class _EthFwdMrpAddr0180C2000024_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000024 based on FrameProcess"""


_EthFwdMrpAddr0180C2000024_Object = MibTableColumn
ethFwdMrpAddr0180C2000024 = _EthFwdMrpAddr0180C2000024_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 34),
    _EthFwdMrpAddr0180C2000024_Type()
)
ethFwdMrpAddr0180C2000024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000024.setStatus("current")


class _EthFwdMrpAddr0180C2000025_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000025 based on FrameProcess"""


_EthFwdMrpAddr0180C2000025_Object = MibTableColumn
ethFwdMrpAddr0180C2000025 = _EthFwdMrpAddr0180C2000025_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 35),
    _EthFwdMrpAddr0180C2000025_Type()
)
ethFwdMrpAddr0180C2000025.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000025.setStatus("current")


class _EthFwdMrpAddr0180C2000026_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000026 based on FrameProcess"""


_EthFwdMrpAddr0180C2000026_Object = MibTableColumn
ethFwdMrpAddr0180C2000026 = _EthFwdMrpAddr0180C2000026_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 36),
    _EthFwdMrpAddr0180C2000026_Type()
)
ethFwdMrpAddr0180C2000026.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000026.setStatus("current")


class _EthFwdMrpAddr0180C2000027_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000027 based on FrameProcess"""


_EthFwdMrpAddr0180C2000027_Object = MibTableColumn
ethFwdMrpAddr0180C2000027 = _EthFwdMrpAddr0180C2000027_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 37),
    _EthFwdMrpAddr0180C2000027_Type()
)
ethFwdMrpAddr0180C2000027.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000027.setStatus("current")


class _EthFwdMrpAddr0180C2000028_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000028 based on FrameProcess"""


_EthFwdMrpAddr0180C2000028_Object = MibTableColumn
ethFwdMrpAddr0180C2000028 = _EthFwdMrpAddr0180C2000028_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 38),
    _EthFwdMrpAddr0180C2000028_Type()
)
ethFwdMrpAddr0180C2000028.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000028.setStatus("current")


class _EthFwdMrpAddr0180C2000029_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C2000029 based on FrameProcess"""


_EthFwdMrpAddr0180C2000029_Object = MibTableColumn
ethFwdMrpAddr0180C2000029 = _EthFwdMrpAddr0180C2000029_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 39),
    _EthFwdMrpAddr0180C2000029_Type()
)
ethFwdMrpAddr0180C2000029.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C2000029.setStatus("current")


class _EthFwdMrpAddr0180C200002A_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C200002A based on FrameProcess"""


_EthFwdMrpAddr0180C200002A_Object = MibTableColumn
ethFwdMrpAddr0180C200002A = _EthFwdMrpAddr0180C200002A_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 40),
    _EthFwdMrpAddr0180C200002A_Type()
)
ethFwdMrpAddr0180C200002A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C200002A.setStatus("current")


class _EthFwdMrpAddr0180C200002B_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C200002B based on FrameProcess"""


_EthFwdMrpAddr0180C200002B_Object = MibTableColumn
ethFwdMrpAddr0180C200002B = _EthFwdMrpAddr0180C200002B_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 41),
    _EthFwdMrpAddr0180C200002B_Type()
)
ethFwdMrpAddr0180C200002B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C200002B.setStatus("current")


class _EthFwdMrpAddr0180C200002C_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C200002C based on FrameProcess"""


_EthFwdMrpAddr0180C200002C_Object = MibTableColumn
ethFwdMrpAddr0180C200002C = _EthFwdMrpAddr0180C200002C_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 42),
    _EthFwdMrpAddr0180C200002C_Type()
)
ethFwdMrpAddr0180C200002C.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C200002C.setStatus("current")


class _EthFwdMrpAddr0180C200002D_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C200002D based on FrameProcess"""


_EthFwdMrpAddr0180C200002D_Object = MibTableColumn
ethFwdMrpAddr0180C200002D = _EthFwdMrpAddr0180C200002D_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 43),
    _EthFwdMrpAddr0180C200002D_Type()
)
ethFwdMrpAddr0180C200002D.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C200002D.setStatus("current")


class _EthFwdMrpAddr0180C200002E_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C200002E based on FrameProcess"""


_EthFwdMrpAddr0180C200002E_Object = MibTableColumn
ethFwdMrpAddr0180C200002E = _EthFwdMrpAddr0180C200002E_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 44),
    _EthFwdMrpAddr0180C200002E_Type()
)
ethFwdMrpAddr0180C200002E.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C200002E.setStatus("current")


class _EthFwdMrpAddr0180C200002F_Type(FrameProcess):
    """Custom type ethFwdMrpAddr0180C200002F based on FrameProcess"""


_EthFwdMrpAddr0180C200002F_Object = MibTableColumn
ethFwdMrpAddr0180C200002F = _EthFwdMrpAddr0180C200002F_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 2, 1, 45),
    _EthFwdMrpAddr0180C200002F_Type()
)
ethFwdMrpAddr0180C200002F.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdMrpAddr0180C200002F.setStatus("current")
_EthFwdDiffservTable_Object = MibTable
ethFwdDiffservTable = _EthFwdDiffservTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ethFwdDiffservTable.setStatus("current")
_EthFwdDiffservEntry_Object = MibTableRow
ethFwdDiffservEntry = _EthFwdDiffservEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 3, 1)
)
ethFwdDiffservEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethFwdIndex"),
    (0, "NETI-ETH-MIB", "ethFwdDiffservIndex"),
)
if mibBuilder.loadTexts:
    ethFwdDiffservEntry.setStatus("current")


class _EthFwdDiffservIndex_Type(Integer32):
    """Custom type ethFwdDiffservIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EthFwdDiffservIndex_Type.__name__ = "Integer32"
_EthFwdDiffservIndex_Object = MibTableColumn
ethFwdDiffservIndex = _EthFwdDiffservIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 3, 1, 1),
    _EthFwdDiffservIndex_Type()
)
ethFwdDiffservIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethFwdDiffservIndex.setStatus("current")


class _EthFwdDiffservFlowGroup_Type(Integer32):
    """Custom type ethFwdDiffservFlowGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EthFwdDiffservFlowGroup_Type.__name__ = "Integer32"
_EthFwdDiffservFlowGroup_Object = MibTableColumn
ethFwdDiffservFlowGroup = _EthFwdDiffservFlowGroup_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 3, 1, 2),
    _EthFwdDiffservFlowGroup_Type()
)
ethFwdDiffservFlowGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdDiffservFlowGroup.setStatus("current")
_EthFwdRstpTable_Object = MibTable
ethFwdRstpTable = _EthFwdRstpTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ethFwdRstpTable.setStatus("current")
_EthFwdRstpEntry_Object = MibTableRow
ethFwdRstpEntry = _EthFwdRstpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1)
)
ethFwdRstpEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethFwdIndex"),
)
if mibBuilder.loadTexts:
    ethFwdRstpEntry.setStatus("current")
_EthFwdRstpBridgeIdentifier_Type = BridgeIdentifier
_EthFwdRstpBridgeIdentifier_Object = MibTableColumn
ethFwdRstpBridgeIdentifier = _EthFwdRstpBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 1),
    _EthFwdRstpBridgeIdentifier_Type()
)
ethFwdRstpBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpBridgeIdentifier.setStatus("current")


class _EthFwdRstpPriority_Type(Integer32):
    """Custom type ethFwdRstpPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_EthFwdRstpPriority_Type.__name__ = "Integer32"
_EthFwdRstpPriority_Object = MibTableColumn
ethFwdRstpPriority = _EthFwdRstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 2),
    _EthFwdRstpPriority_Type()
)
ethFwdRstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdRstpPriority.setStatus("current")
_EthFwdRstpTimeSinceTopologyChange_Type = Timeout
_EthFwdRstpTimeSinceTopologyChange_Object = MibTableColumn
ethFwdRstpTimeSinceTopologyChange = _EthFwdRstpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 3),
    _EthFwdRstpTimeSinceTopologyChange_Type()
)
ethFwdRstpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdRstpTimeSinceTopologyChange.setUnits("centi-seconds")
_EthFwdRstpTopologyChangeCount_Type = Counter32
_EthFwdRstpTopologyChangeCount_Object = MibTableColumn
ethFwdRstpTopologyChangeCount = _EthFwdRstpTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 4),
    _EthFwdRstpTopologyChangeCount_Type()
)
ethFwdRstpTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpTopologyChangeCount.setStatus("current")
_EthFwdRstpTopologyChange_Type = TruthValue
_EthFwdRstpTopologyChange_Object = MibTableColumn
ethFwdRstpTopologyChange = _EthFwdRstpTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 5),
    _EthFwdRstpTopologyChange_Type()
)
ethFwdRstpTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpTopologyChange.setStatus("current")
_EthFwdRstpDesignatedRoot_Type = BridgeIdentifier
_EthFwdRstpDesignatedRoot_Object = MibTableColumn
ethFwdRstpDesignatedRoot = _EthFwdRstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 6),
    _EthFwdRstpDesignatedRoot_Type()
)
ethFwdRstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpDesignatedRoot.setStatus("current")
_EthFwdRstpRootPathCost_Type = Integer32
_EthFwdRstpRootPathCost_Object = MibTableColumn
ethFwdRstpRootPathCost = _EthFwdRstpRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 7),
    _EthFwdRstpRootPathCost_Type()
)
ethFwdRstpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpRootPathCost.setStatus("current")
_EthFwdRstpRootPortName_Type = SnmpAdminString
_EthFwdRstpRootPortName_Object = MibTableColumn
ethFwdRstpRootPortName = _EthFwdRstpRootPortName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 8),
    _EthFwdRstpRootPortName_Type()
)
ethFwdRstpRootPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpRootPortName.setStatus("current")
_EthFwdRstpMaxAge_Type = Timeout
_EthFwdRstpMaxAge_Object = MibTableColumn
ethFwdRstpMaxAge = _EthFwdRstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 9),
    _EthFwdRstpMaxAge_Type()
)
ethFwdRstpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdRstpMaxAge.setUnits("centi-seconds")
_EthFwdRstpHelloTime_Type = Timeout
_EthFwdRstpHelloTime_Object = MibTableColumn
ethFwdRstpHelloTime = _EthFwdRstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 10),
    _EthFwdRstpHelloTime_Type()
)
ethFwdRstpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdRstpHelloTime.setUnits("centi-seconds")
_EthFwdRstpForwardDelay_Type = Timeout
_EthFwdRstpForwardDelay_Object = MibTableColumn
ethFwdRstpForwardDelay = _EthFwdRstpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 11),
    _EthFwdRstpForwardDelay_Type()
)
ethFwdRstpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFwdRstpForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdRstpForwardDelay.setUnits("centi-seconds")


class _EthFwdRstpBridgeMaxAge_Type(Timeout):
    """Custom type ethFwdRstpBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_EthFwdRstpBridgeMaxAge_Type.__name__ = "Timeout"
_EthFwdRstpBridgeMaxAge_Object = MibTableColumn
ethFwdRstpBridgeMaxAge = _EthFwdRstpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 12),
    _EthFwdRstpBridgeMaxAge_Type()
)
ethFwdRstpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdRstpBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdRstpBridgeMaxAge.setUnits("centi-seconds")


class _EthFwdRstpBridgeHelloTime_Type(Timeout):
    """Custom type ethFwdRstpBridgeHelloTime based on Timeout"""
    defaultValue = 200

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_EthFwdRstpBridgeHelloTime_Type.__name__ = "Timeout"
_EthFwdRstpBridgeHelloTime_Object = MibTableColumn
ethFwdRstpBridgeHelloTime = _EthFwdRstpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 13),
    _EthFwdRstpBridgeHelloTime_Type()
)
ethFwdRstpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdRstpBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    ethFwdRstpBridgeHelloTime.setUnits("centi-seconds")


class _EthFwdRstpBridgeForwardDelay_Type(Timeout):
    """Custom type ethFwdRstpBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_EthFwdRstpBridgeForwardDelay_Type.__name__ = "Timeout"
_EthFwdRstpBridgeForwardDelay_Object = MibTableColumn
ethFwdRstpBridgeForwardDelay = _EthFwdRstpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 14),
    _EthFwdRstpBridgeForwardDelay_Type()
)
ethFwdRstpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdRstpBridgeForwardDelay.setStatus("current")


class _EthFwdRstpTxHoldCount_Type(Integer32):
    """Custom type ethFwdRstpTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EthFwdRstpTxHoldCount_Type.__name__ = "Integer32"
_EthFwdRstpTxHoldCount_Object = MibTableColumn
ethFwdRstpTxHoldCount = _EthFwdRstpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 15),
    _EthFwdRstpTxHoldCount_Type()
)
ethFwdRstpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdRstpTxHoldCount.setStatus("current")


class _EthFwdRstpForceVersion_Type(Integer32):
    """Custom type ethFwdRstpForceVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stp", 1))
    )


_EthFwdRstpForceVersion_Type.__name__ = "Integer32"
_EthFwdRstpForceVersion_Object = MibTableColumn
ethFwdRstpForceVersion = _EthFwdRstpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 2, 4, 1, 16),
    _EthFwdRstpForceVersion_Type()
)
ethFwdRstpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethFwdRstpForceVersion.setStatus("current")
_EthInterfaceGroup_ObjectIdentity = ObjectIdentity
ethInterfaceGroup = _EthInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3)
)
_EthIfGroupLastChange_Type = TimeStamp
_EthIfGroupLastChange_Object = MibScalar
ethIfGroupLastChange = _EthIfGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 1),
    _EthIfGroupLastChange_Type()
)
ethIfGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfGroupLastChange.setStatus("current")
_EthIfTable_Object = MibTable
ethIfTable = _EthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ethIfTable.setStatus("current")
_EthIfEntry_Object = MibTableRow
ethIfEntry = _EthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1)
)
ethIfEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethIfEntry.setStatus("current")
_EthIfIndex_Type = Unsigned32
_EthIfIndex_Object = MibTableColumn
ethIfIndex = _EthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 1),
    _EthIfIndex_Type()
)
ethIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfIndex.setStatus("current")


class _EthIfIfIndex_Type(Integer32):
    """Custom type ethIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EthIfIfIndex_Type.__name__ = "Integer32"
_EthIfIfIndex_Object = MibTableColumn
ethIfIfIndex = _EthIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 2),
    _EthIfIfIndex_Type()
)
ethIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIfIndex.setStatus("current")
_EthIfName_Type = SnmpAdminString
_EthIfName_Object = MibTableColumn
ethIfName = _EthIfName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 3),
    _EthIfName_Type()
)
ethIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfName.setStatus("current")
_EthIfType_Type = EthInterfaceType
_EthIfType_Object = MibTableColumn
ethIfType = _EthIfType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 4),
    _EthIfType_Type()
)
ethIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfType.setStatus("current")


class _EthIfCustomerId_Type(Unsigned32):
    """Custom type ethIfCustomerId based on Unsigned32"""
    defaultValue = 0


_EthIfCustomerId_Object = MibTableColumn
ethIfCustomerId = _EthIfCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 5),
    _EthIfCustomerId_Type()
)
ethIfCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfCustomerId.setStatus("current")


class _EthIfPurpose_Type(SnmpAdminString):
    """Custom type ethIfPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_EthIfPurpose_Object = MibTableColumn
ethIfPurpose = _EthIfPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 6),
    _EthIfPurpose_Type()
)
ethIfPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfPurpose.setStatus("current")


class _EthIfAdminStatus_Type(Integer32):
    """Custom type ethIfAdminStatus based on Integer32"""
    defaultValue = 2

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


_EthIfAdminStatus_Type.__name__ = "Integer32"
_EthIfAdminStatus_Object = MibTableColumn
ethIfAdminStatus = _EthIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 7),
    _EthIfAdminStatus_Type()
)
ethIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfAdminStatus.setStatus("current")


class _EthIfOperStatus_Type(Integer32):
    """Custom type ethIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("notPresent", 6),
          ("partial", 9),
          ("up", 1))
    )


_EthIfOperStatus_Type.__name__ = "Integer32"
_EthIfOperStatus_Object = MibTableColumn
ethIfOperStatus = _EthIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 8),
    _EthIfOperStatus_Type()
)
ethIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfOperStatus.setStatus("current")
_EthIfFailure_Type = SnmpAdminString
_EthIfFailure_Object = MibTableColumn
ethIfFailure = _EthIfFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 9),
    _EthIfFailure_Type()
)
ethIfFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfFailure.setStatus("current")


class _EthIfForwardingFunction_Type(Integer32):
    """Custom type ethIfForwardingFunction based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_EthIfForwardingFunction_Type.__name__ = "Integer32"
_EthIfForwardingFunction_Object = MibTableColumn
ethIfForwardingFunction = _EthIfForwardingFunction_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 10),
    _EthIfForwardingFunction_Type()
)
ethIfForwardingFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfForwardingFunction.setStatus("current")


class _EthIfAcceptableFrameTypes_Type(Integer32):
    """Custom type ethIfAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("untagged", 3),
          ("vlanTagged", 2))
    )


_EthIfAcceptableFrameTypes_Type.__name__ = "Integer32"
_EthIfAcceptableFrameTypes_Object = MibTableColumn
ethIfAcceptableFrameTypes = _EthIfAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 11),
    _EthIfAcceptableFrameTypes_Type()
)
ethIfAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfAcceptableFrameTypes.setStatus("current")


class _EthIfTransmittedFrameType_Type(Integer32):
    """Custom type ethIfTransmittedFrameType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 4),
          ("untagged", 3),
          ("vlanTagged", 2))
    )


_EthIfTransmittedFrameType_Type.__name__ = "Integer32"
_EthIfTransmittedFrameType_Object = MibTableColumn
ethIfTransmittedFrameType = _EthIfTransmittedFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 12),
    _EthIfTransmittedFrameType_Type()
)
ethIfTransmittedFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfTransmittedFrameType.setStatus("current")


class _EthIfDefaultVLAN_Type(Integer32):
    """Custom type ethIfDefaultVLAN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EthIfDefaultVLAN_Type.__name__ = "Integer32"
_EthIfDefaultVLAN_Object = MibTableColumn
ethIfDefaultVLAN = _EthIfDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 13),
    _EthIfDefaultVLAN_Type()
)
ethIfDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfDefaultVLAN.setStatus("current")


class _EthIfDefaultEthernetPriority_Type(Integer32):
    """Custom type ethIfDefaultEthernetPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EthIfDefaultEthernetPriority_Type.__name__ = "Integer32"
_EthIfDefaultEthernetPriority_Object = MibTableColumn
ethIfDefaultEthernetPriority = _EthIfDefaultEthernetPriority_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 14),
    _EthIfDefaultEthernetPriority_Type()
)
ethIfDefaultEthernetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfDefaultEthernetPriority.setStatus("current")


class _EthIfPriorityMode_Type(Integer32):
    """Custom type ethIfPriorityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diffserv", 2),
          ("ethernet", 1))
    )


_EthIfPriorityMode_Type.__name__ = "Integer32"
_EthIfPriorityMode_Object = MibTableColumn
ethIfPriorityMode = _EthIfPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 15),
    _EthIfPriorityMode_Type()
)
ethIfPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfPriorityMode.setStatus("current")


class _EthIfDefaultTrafficClass_Type(TrafficClass):
    """Custom type ethIfDefaultTrafficClass based on TrafficClass"""
    defaultValue = 0


_EthIfDefaultTrafficClass_Object = MibTableColumn
ethIfDefaultTrafficClass = _EthIfDefaultTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 16),
    _EthIfDefaultTrafficClass_Type()
)
ethIfDefaultTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfDefaultTrafficClass.setStatus("current")


class _EthIfFlowGroupMap_Type(OctetString):
    """Custom type ethIfFlowGroupMap based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EthIfFlowGroupMap_Type.__name__ = "OctetString"
_EthIfFlowGroupMap_Object = MibTableColumn
ethIfFlowGroupMap = _EthIfFlowGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 17),
    _EthIfFlowGroupMap_Type()
)
ethIfFlowGroupMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfFlowGroupMap.setStatus("current")


class _EthIfLearning_Type(Integer32):
    """Custom type ethIfLearning based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EthIfLearning_Type.__name__ = "Integer32"
_EthIfLearning_Object = MibTableColumn
ethIfLearning = _EthIfLearning_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 18),
    _EthIfLearning_Type()
)
ethIfLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfLearning.setStatus("current")
_EthIfInSpeed_Type = Gauge32
_EthIfInSpeed_Object = MibTableColumn
ethIfInSpeed = _EthIfInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 19),
    _EthIfInSpeed_Type()
)
ethIfInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfInSpeed.setStatus("current")
_EthIfInHighSpeed_Type = Gauge32
_EthIfInHighSpeed_Object = MibTableColumn
ethIfInHighSpeed = _EthIfInHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 20),
    _EthIfInHighSpeed_Type()
)
ethIfInHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfInHighSpeed.setStatus("current")
_EthIfOutSpeed_Type = Gauge32
_EthIfOutSpeed_Object = MibTableColumn
ethIfOutSpeed = _EthIfOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 21),
    _EthIfOutSpeed_Type()
)
ethIfOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfOutSpeed.setStatus("current")
_EthIfOutHighSpeed_Type = Gauge32
_EthIfOutHighSpeed_Object = MibTableColumn
ethIfOutHighSpeed = _EthIfOutHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 22),
    _EthIfOutHighSpeed_Type()
)
ethIfOutHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfOutHighSpeed.setStatus("current")
_EthIfVLANNextIndex_Type = Unsigned32
_EthIfVLANNextIndex_Object = MibTableColumn
ethIfVLANNextIndex = _EthIfVLANNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 23),
    _EthIfVLANNextIndex_Type()
)
ethIfVLANNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfVLANNextIndex.setStatus("current")
_EthIfLastChange_Type = TimeTicks
_EthIfLastChange_Object = MibTableColumn
ethIfLastChange = _EthIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 24),
    _EthIfLastChange_Type()
)
ethIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfLastChange.setStatus("current")
_EthIfSrcPmReference_Type = RowPointer
_EthIfSrcPmReference_Object = MibTableColumn
ethIfSrcPmReference = _EthIfSrcPmReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 25),
    _EthIfSrcPmReference_Type()
)
ethIfSrcPmReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSrcPmReference.setStatus("current")
_EthIfSnkPmReference_Type = RowPointer
_EthIfSnkPmReference_Object = MibTableColumn
ethIfSnkPmReference = _EthIfSnkPmReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 26),
    _EthIfSnkPmReference_Type()
)
ethIfSnkPmReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSnkPmReference.setStatus("current")


class _EthIfSrcDegThreshold_Type(Unsigned32):
    """Custom type ethIfSrcDegThreshold based on Unsigned32"""
    defaultValue = 100


_EthIfSrcDegThreshold_Object = MibTableColumn
ethIfSrcDegThreshold = _EthIfSrcDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 27),
    _EthIfSrcDegThreshold_Type()
)
ethIfSrcDegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcDegThreshold.setStatus("current")


class _EthIfSnkDegThreshold_Type(Unsigned32):
    """Custom type ethIfSnkDegThreshold based on Unsigned32"""
    defaultValue = 100


_EthIfSnkDegThreshold_Object = MibTableColumn
ethIfSnkDegThreshold = _EthIfSnkDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 28),
    _EthIfSnkDegThreshold_Type()
)
ethIfSnkDegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkDegThreshold.setStatus("current")


class _EthIfSrcDegPeriod_Type(Unsigned32):
    """Custom type ethIfSrcDegPeriod based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_EthIfSrcDegPeriod_Type.__name__ = "Unsigned32"
_EthIfSrcDegPeriod_Object = MibTableColumn
ethIfSrcDegPeriod = _EthIfSrcDegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 29),
    _EthIfSrcDegPeriod_Type()
)
ethIfSrcDegPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcDegPeriod.setStatus("current")


class _EthIfSnkDegPeriod_Type(Unsigned32):
    """Custom type ethIfSnkDegPeriod based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_EthIfSnkDegPeriod_Type.__name__ = "Unsigned32"
_EthIfSnkDegPeriod_Object = MibTableColumn
ethIfSnkDegPeriod = _EthIfSnkDegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 30),
    _EthIfSnkDegPeriod_Type()
)
ethIfSnkDegPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkDegPeriod.setStatus("current")


class _EthIfSrcReducedBitRateThreshold_Type(Unsigned32):
    """Custom type ethIfSrcReducedBitRateThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSrcReducedBitRateThreshold_Object = MibTableColumn
ethIfSrcReducedBitRateThreshold = _EthIfSrcReducedBitRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 31),
    _EthIfSrcReducedBitRateThreshold_Type()
)
ethIfSrcReducedBitRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcReducedBitRateThreshold.setStatus("current")


class _EthIfSnkReducedBitRateThreshold_Type(Unsigned32):
    """Custom type ethIfSnkReducedBitRateThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSnkReducedBitRateThreshold_Object = MibTableColumn
ethIfSnkReducedBitRateThreshold = _EthIfSnkReducedBitRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 32),
    _EthIfSnkReducedBitRateThreshold_Type()
)
ethIfSnkReducedBitRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkReducedBitRateThreshold.setStatus("current")


class _EthIfSrcReducedBitRateHighThreshold_Type(Unsigned32):
    """Custom type ethIfSrcReducedBitRateHighThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSrcReducedBitRateHighThreshold_Object = MibTableColumn
ethIfSrcReducedBitRateHighThreshold = _EthIfSrcReducedBitRateHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 33),
    _EthIfSrcReducedBitRateHighThreshold_Type()
)
ethIfSrcReducedBitRateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcReducedBitRateHighThreshold.setStatus("current")


class _EthIfSnkReducedBitRateHighThreshold_Type(Unsigned32):
    """Custom type ethIfSnkReducedBitRateHighThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSnkReducedBitRateHighThreshold_Object = MibTableColumn
ethIfSnkReducedBitRateHighThreshold = _EthIfSnkReducedBitRateHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 34),
    _EthIfSnkReducedBitRateHighThreshold_Type()
)
ethIfSnkReducedBitRateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkReducedBitRateHighThreshold.setStatus("current")


class _EthIfSrcReducedBitRateAIS_Type(TruthValue):
    """Custom type ethIfSrcReducedBitRateAIS based on TruthValue"""


_EthIfSrcReducedBitRateAIS_Object = MibTableColumn
ethIfSrcReducedBitRateAIS = _EthIfSrcReducedBitRateAIS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 35),
    _EthIfSrcReducedBitRateAIS_Type()
)
ethIfSrcReducedBitRateAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcReducedBitRateAIS.setStatus("current")


class _EthIfSnkReducedBitRateAIS_Type(TruthValue):
    """Custom type ethIfSnkReducedBitRateAIS based on TruthValue"""


_EthIfSnkReducedBitRateAIS_Object = MibTableColumn
ethIfSnkReducedBitRateAIS = _EthIfSnkReducedBitRateAIS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 36),
    _EthIfSnkReducedBitRateAIS_Type()
)
ethIfSnkReducedBitRateAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkReducedBitRateAIS.setStatus("current")


class _EthIfSnkDegAIS_Type(TruthValue):
    """Custom type ethIfSnkDegAIS based on TruthValue"""


_EthIfSnkDegAIS_Object = MibTableColumn
ethIfSnkDegAIS = _EthIfSnkDegAIS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 37),
    _EthIfSnkDegAIS_Type()
)
ethIfSnkDegAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkDegAIS.setStatus("current")


class _EthIfSrcMinorReducedBitRateThreshold_Type(Unsigned32):
    """Custom type ethIfSrcMinorReducedBitRateThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSrcMinorReducedBitRateThreshold_Object = MibTableColumn
ethIfSrcMinorReducedBitRateThreshold = _EthIfSrcMinorReducedBitRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 38),
    _EthIfSrcMinorReducedBitRateThreshold_Type()
)
ethIfSrcMinorReducedBitRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMinorReducedBitRateThreshold.setStatus("current")


class _EthIfSnkMinorReducedBitRateThreshold_Type(Unsigned32):
    """Custom type ethIfSnkMinorReducedBitRateThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSnkMinorReducedBitRateThreshold_Object = MibTableColumn
ethIfSnkMinorReducedBitRateThreshold = _EthIfSnkMinorReducedBitRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 39),
    _EthIfSnkMinorReducedBitRateThreshold_Type()
)
ethIfSnkMinorReducedBitRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkMinorReducedBitRateThreshold.setStatus("current")


class _EthIfSrcMinorReducedBitRateHighThreshold_Type(Unsigned32):
    """Custom type ethIfSrcMinorReducedBitRateHighThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSrcMinorReducedBitRateHighThreshold_Object = MibTableColumn
ethIfSrcMinorReducedBitRateHighThreshold = _EthIfSrcMinorReducedBitRateHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 40),
    _EthIfSrcMinorReducedBitRateHighThreshold_Type()
)
ethIfSrcMinorReducedBitRateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSrcMinorReducedBitRateHighThreshold.setStatus("current")


class _EthIfSnkMinorReducedBitRateHighThreshold_Type(Unsigned32):
    """Custom type ethIfSnkMinorReducedBitRateHighThreshold based on Unsigned32"""
    defaultValue = 0


_EthIfSnkMinorReducedBitRateHighThreshold_Object = MibTableColumn
ethIfSnkMinorReducedBitRateHighThreshold = _EthIfSnkMinorReducedBitRateHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 41),
    _EthIfSnkMinorReducedBitRateHighThreshold_Type()
)
ethIfSnkMinorReducedBitRateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfSnkMinorReducedBitRateHighThreshold.setStatus("current")
_EthIfSrcFailure_Type = SnmpAdminString
_EthIfSrcFailure_Object = MibTableColumn
ethIfSrcFailure = _EthIfSrcFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 42),
    _EthIfSrcFailure_Type()
)
ethIfSrcFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSrcFailure.setStatus("current")
_EthIfSnkFailure_Type = SnmpAdminString
_EthIfSnkFailure_Object = MibTableColumn
ethIfSnkFailure = _EthIfSnkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 43),
    _EthIfSnkFailure_Type()
)
ethIfSnkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfSnkFailure.setStatus("current")
_EthIfInterfaceGroup_Type = Integer32
_EthIfInterfaceGroup_Object = MibTableColumn
ethIfInterfaceGroup = _EthIfInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 44),
    _EthIfInterfaceGroup_Type()
)
ethIfInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfInterfaceGroup.setStatus("current")
_EthIfMaxMaxQueueFrames_Type = Unsigned32
_EthIfMaxMaxQueueFrames_Object = MibTableColumn
ethIfMaxMaxQueueFrames = _EthIfMaxMaxQueueFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 45),
    _EthIfMaxMaxQueueFrames_Type()
)
ethIfMaxMaxQueueFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfMaxMaxQueueFrames.setStatus("current")


class _EthIfDefaultDropPrecedence_Type(Unsigned32):
    """Custom type ethIfDefaultDropPrecedence based on Unsigned32"""
    defaultValue = 0


_EthIfDefaultDropPrecedence_Object = MibTableColumn
ethIfDefaultDropPrecedence = _EthIfDefaultDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 46),
    _EthIfDefaultDropPrecedence_Type()
)
ethIfDefaultDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfDefaultDropPrecedence.setStatus("current")


class _EthIfDropPrecedenceMap_Type(OctetString):
    """Custom type ethIfDropPrecedenceMap based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EthIfDropPrecedenceMap_Type.__name__ = "OctetString"
_EthIfDropPrecedenceMap_Object = MibTableColumn
ethIfDropPrecedenceMap = _EthIfDropPrecedenceMap_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 2, 1, 47),
    _EthIfDropPrecedenceMap_Type()
)
ethIfDropPrecedenceMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfDropPrecedenceMap.setStatus("current")
_EthIfQueueTable_Object = MibTable
ethIfQueueTable = _EthIfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ethIfQueueTable.setStatus("current")
_EthIfQueueEntry_Object = MibTableRow
ethIfQueueEntry = _EthIfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 3, 1)
)
ethIfQueueEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
    (0, "NETI-ETH-MIB", "ethIfQueueTrafficClass"),
)
if mibBuilder.loadTexts:
    ethIfQueueEntry.setStatus("current")
_EthIfQueueTrafficClass_Type = TrafficClass
_EthIfQueueTrafficClass_Object = MibTableColumn
ethIfQueueTrafficClass = _EthIfQueueTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 3, 1, 1),
    _EthIfQueueTrafficClass_Type()
)
ethIfQueueTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfQueueTrafficClass.setStatus("current")


class _EthIfQueueMaxOctets_Type(Integer32):
    """Custom type ethIfQueueMaxOctets based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_EthIfQueueMaxOctets_Type.__name__ = "Integer32"
_EthIfQueueMaxOctets_Object = MibTableColumn
ethIfQueueMaxOctets = _EthIfQueueMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 3, 1, 2),
    _EthIfQueueMaxOctets_Type()
)
ethIfQueueMaxOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfQueueMaxOctets.setStatus("current")


class _EthIfQueueMaxFrames_Type(Integer32):
    """Custom type ethIfQueueMaxFrames based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_EthIfQueueMaxFrames_Type.__name__ = "Integer32"
_EthIfQueueMaxFrames_Object = MibTableColumn
ethIfQueueMaxFrames = _EthIfQueueMaxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 3, 1, 3),
    _EthIfQueueMaxFrames_Type()
)
ethIfQueueMaxFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfQueueMaxFrames.setStatus("current")
_EthIfVLANSetsTable_Object = MibTable
ethIfVLANSetsTable = _EthIfVLANSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ethIfVLANSetsTable.setStatus("current")
_EthIfVLANSetsEntry_Object = MibTableRow
ethIfVLANSetsEntry = _EthIfVLANSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4, 1)
)
ethIfVLANSetsEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
    (0, "NETI-ETH-MIB", "ethIfVLANSetIndex"),
)
if mibBuilder.loadTexts:
    ethIfVLANSetsEntry.setStatus("current")
_EthIfVLANSetIndex_Type = Unsigned32
_EthIfVLANSetIndex_Object = MibTableColumn
ethIfVLANSetIndex = _EthIfVLANSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4, 1, 1),
    _EthIfVLANSetIndex_Type()
)
ethIfVLANSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfVLANSetIndex.setStatus("current")
_EthIfVLANRowStatus_Type = RowStatus
_EthIfVLANRowStatus_Object = MibTableColumn
ethIfVLANRowStatus = _EthIfVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4, 1, 2),
    _EthIfVLANRowStatus_Type()
)
ethIfVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfVLANRowStatus.setStatus("current")


class _EthIfVLANSet_Type(VLANSet):
    """Custom type ethIfVLANSet based on VLANSet"""
    defaultHexValue = ""


_EthIfVLANSet_Object = MibTableColumn
ethIfVLANSet = _EthIfVLANSet_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4, 1, 3),
    _EthIfVLANSet_Type()
)
ethIfVLANSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfVLANSet.setStatus("current")


class _EthIfVLANCustomerId_Type(Unsigned32):
    """Custom type ethIfVLANCustomerId based on Unsigned32"""
    defaultValue = 0


_EthIfVLANCustomerId_Object = MibTableColumn
ethIfVLANCustomerId = _EthIfVLANCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4, 1, 4),
    _EthIfVLANCustomerId_Type()
)
ethIfVLANCustomerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfVLANCustomerId.setStatus("current")


class _EthIfVLANPurpose_Type(SnmpAdminString):
    """Custom type ethIfVLANPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_EthIfVLANPurpose_Object = MibTableColumn
ethIfVLANPurpose = _EthIfVLANPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 4, 1, 5),
    _EthIfVLANPurpose_Type()
)
ethIfVLANPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfVLANPurpose.setStatus("current")
_EthDot3Table_Object = MibTable
ethDot3Table = _EthDot3Table_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ethDot3Table.setStatus("current")
_EthDot3Entry_Object = MibTableRow
ethDot3Entry = _EthDot3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1)
)
ethDot3Entry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethDot3Entry.setStatus("current")


class _EthDot3AutoNegotiate_Type(TruthValue):
    """Custom type ethDot3AutoNegotiate based on TruthValue"""


_EthDot3AutoNegotiate_Object = MibTableColumn
ethDot3AutoNegotiate = _EthDot3AutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 1),
    _EthDot3AutoNegotiate_Type()
)
ethDot3AutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3AutoNegotiate.setStatus("current")


class _EthDot3AdvertisedSpeed_Type(AdvertisedSpeed):
    """Custom type ethDot3AdvertisedSpeed based on AdvertisedSpeed"""
    defaultBinValue = "1"


_EthDot3AdvertisedSpeed_Object = MibTableColumn
ethDot3AdvertisedSpeed = _EthDot3AdvertisedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 2),
    _EthDot3AdvertisedSpeed_Type()
)
ethDot3AdvertisedSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3AdvertisedSpeed.setStatus("current")


class _EthDot3AdvertisedDuplex_Type(AdvertisedDuplex):
    """Custom type ethDot3AdvertisedDuplex based on AdvertisedDuplex"""
    defaultBinValue = "1"


_EthDot3AdvertisedDuplex_Object = MibTableColumn
ethDot3AdvertisedDuplex = _EthDot3AdvertisedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 3),
    _EthDot3AdvertisedDuplex_Type()
)
ethDot3AdvertisedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3AdvertisedDuplex.setStatus("current")


class _EthDot3AdvertisedFlowControl_Type(AdvertisedFlowControl):
    """Custom type ethDot3AdvertisedFlowControl based on AdvertisedFlowControl"""
    defaultBinValue = "1"


_EthDot3AdvertisedFlowControl_Object = MibTableColumn
ethDot3AdvertisedFlowControl = _EthDot3AdvertisedFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 4),
    _EthDot3AdvertisedFlowControl_Type()
)
ethDot3AdvertisedFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3AdvertisedFlowControl.setStatus("current")


class _EthDot3ActiveSpeed_Type(Unsigned32):
    """Custom type ethDot3ActiveSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_EthDot3ActiveSpeed_Type.__name__ = "Unsigned32"
_EthDot3ActiveSpeed_Object = MibTableColumn
ethDot3ActiveSpeed = _EthDot3ActiveSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 5),
    _EthDot3ActiveSpeed_Type()
)
ethDot3ActiveSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3ActiveSpeed.setStatus("current")


class _EthDot3ActiveDuplex_Type(Integer32):
    """Custom type ethDot3ActiveDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 3))
    )


_EthDot3ActiveDuplex_Type.__name__ = "Integer32"
_EthDot3ActiveDuplex_Object = MibTableColumn
ethDot3ActiveDuplex = _EthDot3ActiveDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 6),
    _EthDot3ActiveDuplex_Type()
)
ethDot3ActiveDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3ActiveDuplex.setStatus("current")


class _EthDot3ActiveFlowControl_Type(Integer32):
    """Custom type ethDot3ActiveFlowControl based on Integer32"""
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
        *(("all", 1),
          ("none", 4),
          ("notApplicable", 5),
          ("receive", 2),
          ("transmit", 3))
    )


_EthDot3ActiveFlowControl_Type.__name__ = "Integer32"
_EthDot3ActiveFlowControl_Object = MibTableColumn
ethDot3ActiveFlowControl = _EthDot3ActiveFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 7),
    _EthDot3ActiveFlowControl_Type()
)
ethDot3ActiveFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3ActiveFlowControl.setStatus("current")


class _EthDot3ForceVLANTagged_Type(VLANSet):
    """Custom type ethDot3ForceVLANTagged based on VLANSet"""
    defaultHexValue = ""


_EthDot3ForceVLANTagged_Object = MibTableColumn
ethDot3ForceVLANTagged = _EthDot3ForceVLANTagged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 8),
    _EthDot3ForceVLANTagged_Type()
)
ethDot3ForceVLANTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3ForceVLANTagged.setStatus("current")


class _EthDot3ForceVLANUntagged_Type(VLANSet):
    """Custom type ethDot3ForceVLANUntagged based on VLANSet"""
    defaultHexValue = ""


_EthDot3ForceVLANUntagged_Object = MibTableColumn
ethDot3ForceVLANUntagged = _EthDot3ForceVLANUntagged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 9),
    _EthDot3ForceVLANUntagged_Type()
)
ethDot3ForceVLANUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3ForceVLANUntagged.setStatus("current")
_EthDot3SupportedSpeeds_Type = AdvertisedSpeed
_EthDot3SupportedSpeeds_Object = MibTableColumn
ethDot3SupportedSpeeds = _EthDot3SupportedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 10),
    _EthDot3SupportedSpeeds_Type()
)
ethDot3SupportedSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3SupportedSpeeds.setStatus("current")


class _EthDot3ResetToDefaults_Type(Integer32):
    """Custom type ethDot3ResetToDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_EthDot3ResetToDefaults_Type.__name__ = "Integer32"
_EthDot3ResetToDefaults_Object = MibTableColumn
ethDot3ResetToDefaults = _EthDot3ResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 11),
    _EthDot3ResetToDefaults_Type()
)
ethDot3ResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3ResetToDefaults.setStatus("current")
_EthDot3AutoNegotiateStatus_Type = TruthValue
_EthDot3AutoNegotiateStatus_Object = MibTableColumn
ethDot3AutoNegotiateStatus = _EthDot3AutoNegotiateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 12),
    _EthDot3AutoNegotiateStatus_Type()
)
ethDot3AutoNegotiateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3AutoNegotiateStatus.setStatus("current")
_EthDot3AutoNegotiateAllowed_Type = TruthValue
_EthDot3AutoNegotiateAllowed_Object = MibTableColumn
ethDot3AutoNegotiateAllowed = _EthDot3AutoNegotiateAllowed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 13),
    _EthDot3AutoNegotiateAllowed_Type()
)
ethDot3AutoNegotiateAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3AutoNegotiateAllowed.setStatus("current")
_EthDot3AutoNegotiateMandatory_Type = TruthValue
_EthDot3AutoNegotiateMandatory_Object = MibTableColumn
ethDot3AutoNegotiateMandatory = _EthDot3AutoNegotiateMandatory_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 14),
    _EthDot3AutoNegotiateMandatory_Type()
)
ethDot3AutoNegotiateMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3AutoNegotiateMandatory.setStatus("current")


class _EthDot3SupportedIfType_Type(Bits):
    """Custom type ethDot3SupportedIfType based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseLX", 5),
          ("b1000baseSX", 4),
          ("b1000baseT", 6),
          ("b100baseTX", 3),
          ("b10GbaseER", 11),
          ("b10GbaseLR", 9),
          ("b10GbaseLRM", 10),
          ("b10GbaseSR", 8),
          ("b10GbaseZR", 12))
    )

_EthDot3SupportedIfType_Type.__name__ = "Bits"
_EthDot3SupportedIfType_Object = MibTableColumn
ethDot3SupportedIfType = _EthDot3SupportedIfType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 15),
    _EthDot3SupportedIfType_Type()
)
ethDot3SupportedIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDot3SupportedIfType.setStatus("current")
_EthDot3SelectedIfType_Type = EthInterfaceType
_EthDot3SelectedIfType_Object = MibTableColumn
ethDot3SelectedIfType = _EthDot3SelectedIfType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 5, 1, 16),
    _EthDot3SelectedIfType_Type()
)
ethDot3SelectedIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDot3SelectedIfType.setStatus("current")
_EthEtsTable_Object = MibTable
ethEtsTable = _EthEtsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ethEtsTable.setStatus("current")
_EthEtsEntry_Object = MibTableRow
ethEtsEntry = _EthEtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1)
)
ethEtsEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethEtsEntry.setStatus("current")
_EthEtsRowStatus_Type = RowStatus
_EthEtsRowStatus_Object = MibTableColumn
ethEtsRowStatus = _EthEtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1, 1),
    _EthEtsRowStatus_Type()
)
ethEtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethEtsRowStatus.setStatus("current")


class _EthEtsMode_Type(Integer32):
    """Custom type ethEtsMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1),
          ("unspecified", 3))
    )


_EthEtsMode_Type.__name__ = "Integer32"
_EthEtsMode_Object = MibTableColumn
ethEtsMode = _EthEtsMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1, 2),
    _EthEtsMode_Type()
)
ethEtsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethEtsMode.setStatus("current")
_EthEtsLocalDsti_Type = Dsti
_EthEtsLocalDsti_Object = MibTableColumn
ethEtsLocalDsti = _EthEtsLocalDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1, 3),
    _EthEtsLocalDsti_Type()
)
ethEtsLocalDsti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethEtsLocalDsti.setStatus("current")


class _EthEtsODescription_Type(Unsigned32):
    """Custom type ethEtsODescription based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EthEtsODescription_Type.__name__ = "Unsigned32"
_EthEtsODescription_Object = MibTableColumn
ethEtsODescription = _EthEtsODescription_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1, 4),
    _EthEtsODescription_Type()
)
ethEtsODescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethEtsODescription.setStatus("current")
_EthEtsOConnection_Type = Unsigned32
_EthEtsOConnection_Object = MibTableColumn
ethEtsOConnection = _EthEtsOConnection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1, 5),
    _EthEtsOConnection_Type()
)
ethEtsOConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethEtsOConnection.setStatus("current")


class _EthEtsSnkExpectChannel_Type(TruthValue):
    """Custom type ethEtsSnkExpectChannel based on TruthValue"""


_EthEtsSnkExpectChannel_Object = MibTableColumn
ethEtsSnkExpectChannel = _EthEtsSnkExpectChannel_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 6, 1, 6),
    _EthEtsSnkExpectChannel_Type()
)
ethEtsSnkExpectChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethEtsSnkExpectChannel.setStatus("current")
_EthEtsTConnectionTable_Object = MibTable
ethEtsTConnectionTable = _EthEtsTConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ethEtsTConnectionTable.setStatus("current")
_EthEtsTConnectionEntry_Object = MibTableRow
ethEtsTConnectionEntry = _EthEtsTConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 7, 1)
)
ethEtsTConnectionEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
    (0, "NETI-ETH-MIB", "ethEtsTConnectionIndex"),
)
if mibBuilder.loadTexts:
    ethEtsTConnectionEntry.setStatus("current")
_EthEtsTConnectionIndex_Type = Unsigned32
_EthEtsTConnectionIndex_Object = MibTableColumn
ethEtsTConnectionIndex = _EthEtsTConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 7, 1, 1),
    _EthEtsTConnectionIndex_Type()
)
ethEtsTConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethEtsTConnectionIndex.setStatus("current")
_EthEtsTConnectionRowStatus_Type = RowStatus
_EthEtsTConnectionRowStatus_Object = MibTableColumn
ethEtsTConnectionRowStatus = _EthEtsTConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 7, 1, 2),
    _EthEtsTConnectionRowStatus_Type()
)
ethEtsTConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethEtsTConnectionRowStatus.setStatus("current")
_EthEtsTConnection_Type = Unsigned32
_EthEtsTConnection_Object = MibTableColumn
ethEtsTConnection = _EthEtsTConnection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 7, 1, 3),
    _EthEtsTConnection_Type()
)
ethEtsTConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethEtsTConnection.setStatus("current")
_EthEtsIndexLookupTable_Object = MibTable
ethEtsIndexLookupTable = _EthEtsIndexLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    ethEtsIndexLookupTable.setStatus("current")
_EthEtsIndexLookupEntry_Object = MibTableRow
ethEtsIndexLookupEntry = _EthEtsIndexLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 8, 1)
)
ethEtsIndexLookupEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethEtsLocalDsti"),
)
if mibBuilder.loadTexts:
    ethEtsIndexLookupEntry.setStatus("current")
_EthEtsIndexLookupDevIndex_Type = Unsigned32
_EthEtsIndexLookupDevIndex_Object = MibTableColumn
ethEtsIndexLookupDevIndex = _EthEtsIndexLookupDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 8, 1, 1),
    _EthEtsIndexLookupDevIndex_Type()
)
ethEtsIndexLookupDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethEtsIndexLookupDevIndex.setStatus("current")
_EthEtsIndexLookupIfIndex_Type = Unsigned32
_EthEtsIndexLookupIfIndex_Object = MibTableColumn
ethEtsIndexLookupIfIndex = _EthEtsIndexLookupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 8, 1, 2),
    _EthEtsIndexLookupIfIndex_Type()
)
ethEtsIndexLookupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethEtsIndexLookupIfIndex.setStatus("current")
_EthIfRstpTable_Object = MibTable
ethIfRstpTable = _EthIfRstpTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9)
)
if mibBuilder.loadTexts:
    ethIfRstpTable.setStatus("current")
_EthIfRstpEntry_Object = MibTableRow
ethIfRstpEntry = _EthIfRstpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1)
)
ethIfRstpEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethIfRstpEntry.setStatus("current")
_EthIfRstpPortIdentifier_Type = PortIdentifier
_EthIfRstpPortIdentifier_Object = MibTableColumn
ethIfRstpPortIdentifier = _EthIfRstpPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 1),
    _EthIfRstpPortIdentifier_Type()
)
ethIfRstpPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpPortIdentifier.setStatus("current")


class _EthIfRstpPriority_Type(Integer32):
    """Custom type ethIfRstpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_EthIfRstpPriority_Type.__name__ = "Integer32"
_EthIfRstpPriority_Object = MibTableColumn
ethIfRstpPriority = _EthIfRstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 2),
    _EthIfRstpPriority_Type()
)
ethIfRstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRstpPriority.setStatus("current")


class _EthIfRstpState_Type(Integer32):
    """Custom type ethIfRstpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 3),
          ("learning", 2))
    )


_EthIfRstpState_Type.__name__ = "Integer32"
_EthIfRstpState_Object = MibTableColumn
ethIfRstpState = _EthIfRstpState_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 3),
    _EthIfRstpState_Type()
)
ethIfRstpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpState.setStatus("current")
_EthIfRstpTopologyChangeAcknowledge_Type = TruthValue
_EthIfRstpTopologyChangeAcknowledge_Object = MibTableColumn
ethIfRstpTopologyChangeAcknowledge = _EthIfRstpTopologyChangeAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 4),
    _EthIfRstpTopologyChangeAcknowledge_Type()
)
ethIfRstpTopologyChangeAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpTopologyChangeAcknowledge.setStatus("current")


class _EthIfRstpPathCost_Type(Integer32):
    """Custom type ethIfRstpPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_EthIfRstpPathCost_Type.__name__ = "Integer32"
_EthIfRstpPathCost_Object = MibTableColumn
ethIfRstpPathCost = _EthIfRstpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 5),
    _EthIfRstpPathCost_Type()
)
ethIfRstpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRstpPathCost.setStatus("current")
_EthIfRstpDesignatedRoot_Type = BridgeIdentifier
_EthIfRstpDesignatedRoot_Object = MibTableColumn
ethIfRstpDesignatedRoot = _EthIfRstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 6),
    _EthIfRstpDesignatedRoot_Type()
)
ethIfRstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpDesignatedRoot.setStatus("current")
_EthIfRstpDesignatedCost_Type = Integer32
_EthIfRstpDesignatedCost_Object = MibTableColumn
ethIfRstpDesignatedCost = _EthIfRstpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 7),
    _EthIfRstpDesignatedCost_Type()
)
ethIfRstpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpDesignatedCost.setStatus("current")
_EthIfRstpDesignatedBridge_Type = BridgeIdentifier
_EthIfRstpDesignatedBridge_Object = MibTableColumn
ethIfRstpDesignatedBridge = _EthIfRstpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 8),
    _EthIfRstpDesignatedBridge_Type()
)
ethIfRstpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpDesignatedBridge.setStatus("current")
_EthIfRstpDesignatedPort_Type = PortIdentifier
_EthIfRstpDesignatedPort_Object = MibTableColumn
ethIfRstpDesignatedPort = _EthIfRstpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 9),
    _EthIfRstpDesignatedPort_Type()
)
ethIfRstpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpDesignatedPort.setStatus("current")


class _EthIfRstpAdminEdgePort_Type(Integer32):
    """Custom type ethIfRstpAdminEdgePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("false", 2),
          ("true", 1))
    )


_EthIfRstpAdminEdgePort_Type.__name__ = "Integer32"
_EthIfRstpAdminEdgePort_Object = MibTableColumn
ethIfRstpAdminEdgePort = _EthIfRstpAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 10),
    _EthIfRstpAdminEdgePort_Type()
)
ethIfRstpAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRstpAdminEdgePort.setStatus("current")
_EthIfRstpOperEdgePort_Type = TruthValue
_EthIfRstpOperEdgePort_Object = MibTableColumn
ethIfRstpOperEdgePort = _EthIfRstpOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 11),
    _EthIfRstpOperEdgePort_Type()
)
ethIfRstpOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpOperEdgePort.setStatus("current")


class _EthIfRstpAdminPointToPointMAC_Type(Integer32):
    """Custom type ethIfRstpAdminPointToPointMAC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("false", 2),
          ("true", 1))
    )


_EthIfRstpAdminPointToPointMAC_Type.__name__ = "Integer32"
_EthIfRstpAdminPointToPointMAC_Object = MibTableColumn
ethIfRstpAdminPointToPointMAC = _EthIfRstpAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 12),
    _EthIfRstpAdminPointToPointMAC_Type()
)
ethIfRstpAdminPointToPointMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfRstpAdminPointToPointMAC.setStatus("current")
_EthIfRstpOperPointToPointMAC_Type = TruthValue
_EthIfRstpOperPointToPointMAC_Object = MibTableColumn
ethIfRstpOperPointToPointMAC = _EthIfRstpOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 13),
    _EthIfRstpOperPointToPointMAC_Type()
)
ethIfRstpOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpOperPointToPointMAC.setStatus("current")


class _EthIfRstpCurrentPathCost_Type(Integer32):
    """Custom type ethIfRstpCurrentPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_EthIfRstpCurrentPathCost_Type.__name__ = "Integer32"
_EthIfRstpCurrentPathCost_Object = MibTableColumn
ethIfRstpCurrentPathCost = _EthIfRstpCurrentPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 9, 1, 14),
    _EthIfRstpCurrentPathCost_Type()
)
ethIfRstpCurrentPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfRstpCurrentPathCost.setStatus("current")
_EthIfgTable_Object = MibTable
ethIfgTable = _EthIfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10)
)
if mibBuilder.loadTexts:
    ethIfgTable.setStatus("current")
_EthIfgEntry_Object = MibTableRow
ethIfgEntry = _EthIfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1)
)
ethIfgEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethIfgEntry.setStatus("current")
_EthIfgRowStatus_Type = RowStatus
_EthIfgRowStatus_Object = MibTableColumn
ethIfgRowStatus = _EthIfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 1),
    _EthIfgRowStatus_Type()
)
ethIfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfgRowStatus.setStatus("current")
_EthIfgMembers_Type = InterfaceIndexList
_EthIfgMembers_Object = MibTableColumn
ethIfgMembers = _EthIfgMembers_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 2),
    _EthIfgMembers_Type()
)
ethIfgMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfgMembers.setStatus("current")
_EthIfgDifferentialDelay_Type = Unsigned32
_EthIfgDifferentialDelay_Object = MibTableColumn
ethIfgDifferentialDelay = _EthIfgDifferentialDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 3),
    _EthIfgDifferentialDelay_Type()
)
ethIfgDifferentialDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfgDifferentialDelay.setStatus("current")
_EthIfgDifferentialDelayValid_Type = TruthValue
_EthIfgDifferentialDelayValid_Object = MibTableColumn
ethIfgDifferentialDelayValid = _EthIfgDifferentialDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 4),
    _EthIfgDifferentialDelayValid_Type()
)
ethIfgDifferentialDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfgDifferentialDelayValid.setStatus("current")
_EthIfgAheadInterface_Type = Unsigned32
_EthIfgAheadInterface_Object = MibTableColumn
ethIfgAheadInterface = _EthIfgAheadInterface_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 5),
    _EthIfgAheadInterface_Type()
)
ethIfgAheadInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfgAheadInterface.setStatus("current")


class _EthIfgHitlessProtection_Type(TruthValue):
    """Custom type ethIfgHitlessProtection based on TruthValue"""


_EthIfgHitlessProtection_Object = MibTableColumn
ethIfgHitlessProtection = _EthIfgHitlessProtection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 6),
    _EthIfgHitlessProtection_Type()
)
ethIfgHitlessProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfgHitlessProtection.setStatus("current")
_EthIfgProtectionStatus_Type = IfgProtectionStatus
_EthIfgProtectionStatus_Object = MibTableColumn
ethIfgProtectionStatus = _EthIfgProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 7),
    _EthIfgProtectionStatus_Type()
)
ethIfgProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfgProtectionStatus.setStatus("current")


class _EthIfgExpectedProtectionStatus_Type(IfgProtectionStatus):
    """Custom type ethIfgExpectedProtectionStatus based on IfgProtectionStatus"""


_EthIfgExpectedProtectionStatus_Object = MibTableColumn
ethIfgExpectedProtectionStatus = _EthIfgExpectedProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 8),
    _EthIfgExpectedProtectionStatus_Type()
)
ethIfgExpectedProtectionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfgExpectedProtectionStatus.setStatus("current")


class _EthIfgForceHit_Type(Unsigned32):
    """Custom type ethIfgForceHit based on Unsigned32"""
    defaultValue = 0


_EthIfgForceHit_Object = MibTableColumn
ethIfgForceHit = _EthIfgForceHit_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 9),
    _EthIfgForceHit_Type()
)
ethIfgForceHit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfgForceHit.setStatus("current")
_EthIfgActiveInterface_Type = Unsigned32
_EthIfgActiveInterface_Object = MibTableColumn
ethIfgActiveInterface = _EthIfgActiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 10),
    _EthIfgActiveInterface_Type()
)
ethIfgActiveInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfgActiveInterface.setStatus("current")
_EthIfgExpectChannel_Type = TruthValue
_EthIfgExpectChannel_Object = MibTableColumn
ethIfgExpectChannel = _EthIfgExpectChannel_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 10, 1, 11),
    _EthIfgExpectChannel_Type()
)
ethIfgExpectChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfgExpectChannel.setStatus("current")
_EthIfQDropThresholdTable_Object = MibTable
ethIfQDropThresholdTable = _EthIfQDropThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 11)
)
if mibBuilder.loadTexts:
    ethIfQDropThresholdTable.setStatus("current")
_EthIfQDropThresholdEntry_Object = MibTableRow
ethIfQDropThresholdEntry = _EthIfQDropThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 11, 1)
)
ethIfQDropThresholdEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
    (0, "NETI-ETH-MIB", "ethIfQueueTrafficClass"),
    (0, "NETI-ETH-MIB", "ethIfQDropThresDropPrecedence"),
)
if mibBuilder.loadTexts:
    ethIfQDropThresholdEntry.setStatus("current")
_EthIfQDropThresDropPrecedence_Type = Unsigned32
_EthIfQDropThresDropPrecedence_Object = MibTableColumn
ethIfQDropThresDropPrecedence = _EthIfQDropThresDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 11, 1, 1),
    _EthIfQDropThresDropPrecedence_Type()
)
ethIfQDropThresDropPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfQDropThresDropPrecedence.setStatus("current")


class _EthIfQDropThresMaxFrames_Type(Integer32):
    """Custom type ethIfQDropThresMaxFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_EthIfQDropThresMaxFrames_Type.__name__ = "Integer32"
_EthIfQDropThresMaxFrames_Object = MibTableColumn
ethIfQDropThresMaxFrames = _EthIfQDropThresMaxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 11, 1, 2),
    _EthIfQDropThresMaxFrames_Type()
)
ethIfQDropThresMaxFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfQDropThresMaxFrames.setStatus("current")


class _EthIfQDropThresCurrentMaxFrames_Type(Integer32):
    """Custom type ethIfQDropThresCurrentMaxFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EthIfQDropThresCurrentMaxFrames_Type.__name__ = "Integer32"
_EthIfQDropThresCurrentMaxFrames_Object = MibTableColumn
ethIfQDropThresCurrentMaxFrames = _EthIfQDropThresCurrentMaxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 11, 1, 3),
    _EthIfQDropThresCurrentMaxFrames_Type()
)
ethIfQDropThresCurrentMaxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfQDropThresCurrentMaxFrames.setStatus("current")


class _EthIfQDropThresDropProbabilityFunction_Type(Integer32):
    """Custom type ethIfQDropThresDropProbabilityFunction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("taildrop", 0),
          ("wred", 1))
    )


_EthIfQDropThresDropProbabilityFunction_Type.__name__ = "Integer32"
_EthIfQDropThresDropProbabilityFunction_Object = MibTableColumn
ethIfQDropThresDropProbabilityFunction = _EthIfQDropThresDropProbabilityFunction_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 3, 11, 1, 4),
    _EthIfQDropThresDropProbabilityFunction_Type()
)
ethIfQDropThresDropProbabilityFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfQDropThresDropProbabilityFunction.setStatus("current")
_EthStatisticsGroup_ObjectIdentity = ObjectIdentity
ethStatisticsGroup = _EthStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4)
)
_EthStatDcap1Table_Object = MibTable
ethStatDcap1Table = _EthStatDcap1Table_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ethStatDcap1Table.setStatus("current")
_EthStatDcap1Entry_Object = MibTableRow
ethStatDcap1Entry = _EthStatDcap1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1)
)
ethStatDcap1Entry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethStatDcap1Entry.setStatus("current")


class _EthStatDcap1Reset_Type(Integer32):
    """Custom type ethStatDcap1Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_EthStatDcap1Reset_Type.__name__ = "Integer32"
_EthStatDcap1Reset_Object = MibTableColumn
ethStatDcap1Reset = _EthStatDcap1Reset_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 1),
    _EthStatDcap1Reset_Type()
)
ethStatDcap1Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethStatDcap1Reset.setStatus("current")
_EthStatDcap1TxOctets_Type = Counter64
_EthStatDcap1TxOctets_Object = MibTableColumn
ethStatDcap1TxOctets = _EthStatDcap1TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 2),
    _EthStatDcap1TxOctets_Type()
)
ethStatDcap1TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1TxOctets.setStatus("current")
_EthStatDcap1TxPackets_Type = Counter64
_EthStatDcap1TxPackets_Object = MibTableColumn
ethStatDcap1TxPackets = _EthStatDcap1TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 3),
    _EthStatDcap1TxPackets_Type()
)
ethStatDcap1TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1TxPackets.setStatus("current")
_EthStatDcap1TxDiscardOctets_Type = Counter64
_EthStatDcap1TxDiscardOctets_Object = MibTableColumn
ethStatDcap1TxDiscardOctets = _EthStatDcap1TxDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 4),
    _EthStatDcap1TxDiscardOctets_Type()
)
ethStatDcap1TxDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1TxDiscardOctets.setStatus("current")
_EthStatDcap1TxDiscardPackets_Type = Counter64
_EthStatDcap1TxDiscardPackets_Object = MibTableColumn
ethStatDcap1TxDiscardPackets = _EthStatDcap1TxDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 5),
    _EthStatDcap1TxDiscardPackets_Type()
)
ethStatDcap1TxDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1TxDiscardPackets.setStatus("current")
_EthStatDcap1TxBitrate_Type = Counter64
_EthStatDcap1TxBitrate_Object = MibTableColumn
ethStatDcap1TxBitrate = _EthStatDcap1TxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 6),
    _EthStatDcap1TxBitrate_Type()
)
ethStatDcap1TxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1TxBitrate.setStatus("current")


class _EthStatDcap1TxLoad_Type(Unsigned32):
    """Custom type ethStatDcap1TxLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EthStatDcap1TxLoad_Type.__name__ = "Unsigned32"
_EthStatDcap1TxLoad_Object = MibTableColumn
ethStatDcap1TxLoad = _EthStatDcap1TxLoad_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 7),
    _EthStatDcap1TxLoad_Type()
)
ethStatDcap1TxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1TxLoad.setStatus("current")
_EthStatDcap1RxOctets_Type = Counter64
_EthStatDcap1RxOctets_Object = MibTableColumn
ethStatDcap1RxOctets = _EthStatDcap1RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 8),
    _EthStatDcap1RxOctets_Type()
)
ethStatDcap1RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxOctets.setStatus("current")
_EthStatDcap1RxPackets_Type = Counter64
_EthStatDcap1RxPackets_Object = MibTableColumn
ethStatDcap1RxPackets = _EthStatDcap1RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 9),
    _EthStatDcap1RxPackets_Type()
)
ethStatDcap1RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxPackets.setStatus("current")
_EthStatDcap1RxDiscardOctets_Type = Counter64
_EthStatDcap1RxDiscardOctets_Object = MibTableColumn
ethStatDcap1RxDiscardOctets = _EthStatDcap1RxDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 10),
    _EthStatDcap1RxDiscardOctets_Type()
)
ethStatDcap1RxDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxDiscardOctets.setStatus("current")
_EthStatDcap1RxDiscardPackets_Type = Counter64
_EthStatDcap1RxDiscardPackets_Object = MibTableColumn
ethStatDcap1RxDiscardPackets = _EthStatDcap1RxDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 11),
    _EthStatDcap1RxDiscardPackets_Type()
)
ethStatDcap1RxDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxDiscardPackets.setStatus("current")
_EthStatDcap1RxErrorCRC_Type = Counter64
_EthStatDcap1RxErrorCRC_Object = MibTableColumn
ethStatDcap1RxErrorCRC = _EthStatDcap1RxErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 12),
    _EthStatDcap1RxErrorCRC_Type()
)
ethStatDcap1RxErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxErrorCRC.setStatus("current")
_EthStatDcap1RxBitrate_Type = Counter64
_EthStatDcap1RxBitrate_Object = MibTableColumn
ethStatDcap1RxBitrate = _EthStatDcap1RxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 13),
    _EthStatDcap1RxBitrate_Type()
)
ethStatDcap1RxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxBitrate.setStatus("current")


class _EthStatDcap1RxLoad_Type(Unsigned32):
    """Custom type ethStatDcap1RxLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EthStatDcap1RxLoad_Type.__name__ = "Unsigned32"
_EthStatDcap1RxLoad_Object = MibTableColumn
ethStatDcap1RxLoad = _EthStatDcap1RxLoad_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 1, 1, 14),
    _EthStatDcap1RxLoad_Type()
)
ethStatDcap1RxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatDcap1RxLoad.setStatus("current")
_EthIfStatTable_Object = MibTable
ethIfStatTable = _EthIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ethIfStatTable.setStatus("current")
_EthIfStatEntry_Object = MibTableRow
ethIfStatEntry = _EthIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2, 1)
)
ethIfStatEntry.setIndexNames(
    (0, "NETI-ETH-MIB", "ethDevIndex"),
    (0, "NETI-ETH-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethIfStatEntry.setStatus("current")
_EthIfStatReset_Type = Integer32
_EthIfStatReset_Object = MibTableColumn
ethIfStatReset = _EthIfStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2, 1, 1),
    _EthIfStatReset_Type()
)
ethIfStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfStatReset.setStatus("current")
_EthIfStatTxBitrate_Type = Counter64
_EthIfStatTxBitrate_Object = MibTableColumn
ethIfStatTxBitrate = _EthIfStatTxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2, 1, 2),
    _EthIfStatTxBitrate_Type()
)
ethIfStatTxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatTxBitrate.setStatus("current")


class _EthIfStatTxLoad_Type(Unsigned32):
    """Custom type ethIfStatTxLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EthIfStatTxLoad_Type.__name__ = "Unsigned32"
_EthIfStatTxLoad_Object = MibTableColumn
ethIfStatTxLoad = _EthIfStatTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2, 1, 3),
    _EthIfStatTxLoad_Type()
)
ethIfStatTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatTxLoad.setStatus("current")
_EthIfStatRxBitrate_Type = Counter64
_EthIfStatRxBitrate_Object = MibTableColumn
ethIfStatRxBitrate = _EthIfStatRxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2, 1, 4),
    _EthIfStatRxBitrate_Type()
)
ethIfStatRxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatRxBitrate.setStatus("current")


class _EthIfStatRxLoad_Type(Unsigned32):
    """Custom type ethIfStatRxLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EthIfStatRxLoad_Type.__name__ = "Unsigned32"
_EthIfStatRxLoad_Object = MibTableColumn
ethIfStatRxLoad = _EthIfStatRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 2, 1, 4, 2, 1, 5),
    _EthIfStatRxLoad_Type()
)
ethIfStatRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfStatRxLoad.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-ETH-MIB",
    **{"TrafficClass": TrafficClass,
       "VLANSet": VLANSet,
       "AdvertisedSpeed": AdvertisedSpeed,
       "AdvertisedDuplex": AdvertisedDuplex,
       "AdvertisedFlowControl": AdvertisedFlowControl,
       "BridgeIdentifier": BridgeIdentifier,
       "EthInterfaceType": EthInterfaceType,
       "PortIdentifier": PortIdentifier,
       "Timeout": Timeout,
       "FrameProcess": FrameProcess,
       "InterfaceIndexList": InterfaceIndexList,
       "IfgProtectionStatus": IfgProtectionStatus,
       "netiEthMIB": netiEthMIB,
       "ethObjects": ethObjects,
       "ethDeviceGroup": ethDeviceGroup,
       "ethDeviceTable": ethDeviceTable,
       "ethDeviceEntry": ethDeviceEntry,
       "ethDevIndex": ethDevIndex,
       "ethDevRowStatus": ethDevRowStatus,
       "ethDevName": ethDevName,
       "ethDevContainerName": ethDevContainerName,
       "ethDevProductName": ethDevProductName,
       "ethDevStatus": ethDevStatus,
       "ethDevCapJumboFrames": ethDevCapJumboFrames,
       "ethDevCapMaxAgingTime": ethDevCapMaxAgingTime,
       "ethDevCapMACMode": ethDevCapMACMode,
       "ethDevCapSpanningTree": ethDevCapSpanningTree,
       "ethDevCapVLANMode": ethDevCapVLANMode,
       "ethDevCapAdvertisedDuplex": ethDevCapAdvertisedDuplex,
       "ethDevCapAdvertisedFlowControl": ethDevCapAdvertisedFlowControl,
       "ethDevCapAcceptableFrameType": ethDevCapAcceptableFrameType,
       "ethDevCapDefaultEthernetPriority": ethDevCapDefaultEthernetPriority,
       "ethDevCapLearning": ethDevCapLearning,
       "ethDevCapTransmittedFrameTypeETS": ethDevCapTransmittedFrameTypeETS,
       "ethDevCapTransmittedFrameTypeDot3": ethDevCapTransmittedFrameTypeDot3,
       "ethDevCapMaxMaxQueueOctets": ethDevCapMaxMaxQueueOctets,
       "ethDevCapMaxMaxQueueFrames": ethDevCapMaxMaxQueueFrames,
       "ethDevCapMaxTrafficClass": ethDevCapMaxTrafficClass,
       "ethDevEtsNextIndex": ethDevEtsNextIndex,
       "ethDevFwdFuncNextIndex": ethDevFwdFuncNextIndex,
       "ethDevCapPerformanceMonitoring": ethDevCapPerformanceMonitoring,
       "ethDevCapConfigurableFaultMgmt": ethDevCapConfigurableFaultMgmt,
       "ethDevIfgFirstIndex": ethDevIfgFirstIndex,
       "ethDevIfgNextIndex": ethDevIfgNextIndex,
       "ethDevCapDropPrecedenceLevels": ethDevCapDropPrecedenceLevels,
       "ethDevCapDropProbabilityFunctions": ethDevCapDropProbabilityFunctions,
       "ethDevFailure": ethDevFailure,
       "ethFwdFuncGroup": ethFwdFuncGroup,
       "ethFwdFuncLastChange": ethFwdFuncLastChange,
       "ethFwdFuncTable": ethFwdFuncTable,
       "ethFwdFuncEntry": ethFwdFuncEntry,
       "ethFwdIndex": ethFwdIndex,
       "ethFwdRowStatus": ethFwdRowStatus,
       "ethFwdName": ethFwdName,
       "ethFwdCustomerId": ethFwdCustomerId,
       "ethFwdPurpose": ethFwdPurpose,
       "ethFwdJumboFrames": ethFwdJumboFrames,
       "ethFwdMACMode": ethFwdMACMode,
       "ethFwdCurrentMACMode": ethFwdCurrentMACMode,
       "ethFwdSpanningTree": ethFwdSpanningTree,
       "ethFwdVLANMode": ethFwdVLANMode,
       "ethFwdAgingTime": ethFwdAgingTime,
       "ethFwdFailure": ethFwdFailure,
       "ethFwdLastChange": ethFwdLastChange,
       "ethFwdPropagateFaults": ethFwdPropagateFaults,
       "ethFwdReservedAddr0180C2000002": ethFwdReservedAddr0180C2000002,
       "ethFwdReservedAddr0180C2000003": ethFwdReservedAddr0180C2000003,
       "ethFwdReservedAddr0180C2000004": ethFwdReservedAddr0180C2000004,
       "ethFwdReservedAddr0180C2000005": ethFwdReservedAddr0180C2000005,
       "ethFwdReservedAddr0180C2000006": ethFwdReservedAddr0180C2000006,
       "ethFwdReservedAddr0180C2000007": ethFwdReservedAddr0180C2000007,
       "ethFwdReservedAddr0180C2000008": ethFwdReservedAddr0180C2000008,
       "ethFwdReservedAddr0180C2000009": ethFwdReservedAddr0180C2000009,
       "ethFwdReservedAddr0180C200000A": ethFwdReservedAddr0180C200000A,
       "ethFwdReservedAddr0180C200000B": ethFwdReservedAddr0180C200000B,
       "ethFwdReservedAddr0180C200000C": ethFwdReservedAddr0180C200000C,
       "ethFwdReservedAddr0180C200000D": ethFwdReservedAddr0180C200000D,
       "ethFwdReservedAddr0180C200000E": ethFwdReservedAddr0180C200000E,
       "ethFwdReservedAddr0180C200000F": ethFwdReservedAddr0180C200000F,
       "ethFwdCurrentStpMode": ethFwdCurrentStpMode,
       "ethFwdMrpAddr0180C2000020": ethFwdMrpAddr0180C2000020,
       "ethFwdMrpAddr0180C2000021": ethFwdMrpAddr0180C2000021,
       "ethFwdMrpAddr0180C2000022": ethFwdMrpAddr0180C2000022,
       "ethFwdMrpAddr0180C2000023": ethFwdMrpAddr0180C2000023,
       "ethFwdMrpAddr0180C2000024": ethFwdMrpAddr0180C2000024,
       "ethFwdMrpAddr0180C2000025": ethFwdMrpAddr0180C2000025,
       "ethFwdMrpAddr0180C2000026": ethFwdMrpAddr0180C2000026,
       "ethFwdMrpAddr0180C2000027": ethFwdMrpAddr0180C2000027,
       "ethFwdMrpAddr0180C2000028": ethFwdMrpAddr0180C2000028,
       "ethFwdMrpAddr0180C2000029": ethFwdMrpAddr0180C2000029,
       "ethFwdMrpAddr0180C200002A": ethFwdMrpAddr0180C200002A,
       "ethFwdMrpAddr0180C200002B": ethFwdMrpAddr0180C200002B,
       "ethFwdMrpAddr0180C200002C": ethFwdMrpAddr0180C200002C,
       "ethFwdMrpAddr0180C200002D": ethFwdMrpAddr0180C200002D,
       "ethFwdMrpAddr0180C200002E": ethFwdMrpAddr0180C200002E,
       "ethFwdMrpAddr0180C200002F": ethFwdMrpAddr0180C200002F,
       "ethFwdDiffservTable": ethFwdDiffservTable,
       "ethFwdDiffservEntry": ethFwdDiffservEntry,
       "ethFwdDiffservIndex": ethFwdDiffservIndex,
       "ethFwdDiffservFlowGroup": ethFwdDiffservFlowGroup,
       "ethFwdRstpTable": ethFwdRstpTable,
       "ethFwdRstpEntry": ethFwdRstpEntry,
       "ethFwdRstpBridgeIdentifier": ethFwdRstpBridgeIdentifier,
       "ethFwdRstpPriority": ethFwdRstpPriority,
       "ethFwdRstpTimeSinceTopologyChange": ethFwdRstpTimeSinceTopologyChange,
       "ethFwdRstpTopologyChangeCount": ethFwdRstpTopologyChangeCount,
       "ethFwdRstpTopologyChange": ethFwdRstpTopologyChange,
       "ethFwdRstpDesignatedRoot": ethFwdRstpDesignatedRoot,
       "ethFwdRstpRootPathCost": ethFwdRstpRootPathCost,
       "ethFwdRstpRootPortName": ethFwdRstpRootPortName,
       "ethFwdRstpMaxAge": ethFwdRstpMaxAge,
       "ethFwdRstpHelloTime": ethFwdRstpHelloTime,
       "ethFwdRstpForwardDelay": ethFwdRstpForwardDelay,
       "ethFwdRstpBridgeMaxAge": ethFwdRstpBridgeMaxAge,
       "ethFwdRstpBridgeHelloTime": ethFwdRstpBridgeHelloTime,
       "ethFwdRstpBridgeForwardDelay": ethFwdRstpBridgeForwardDelay,
       "ethFwdRstpTxHoldCount": ethFwdRstpTxHoldCount,
       "ethFwdRstpForceVersion": ethFwdRstpForceVersion,
       "ethInterfaceGroup": ethInterfaceGroup,
       "ethIfGroupLastChange": ethIfGroupLastChange,
       "ethIfTable": ethIfTable,
       "ethIfEntry": ethIfEntry,
       "ethIfIndex": ethIfIndex,
       "ethIfIfIndex": ethIfIfIndex,
       "ethIfName": ethIfName,
       "ethIfType": ethIfType,
       "ethIfCustomerId": ethIfCustomerId,
       "ethIfPurpose": ethIfPurpose,
       "ethIfAdminStatus": ethIfAdminStatus,
       "ethIfOperStatus": ethIfOperStatus,
       "ethIfFailure": ethIfFailure,
       "ethIfForwardingFunction": ethIfForwardingFunction,
       "ethIfAcceptableFrameTypes": ethIfAcceptableFrameTypes,
       "ethIfTransmittedFrameType": ethIfTransmittedFrameType,
       "ethIfDefaultVLAN": ethIfDefaultVLAN,
       "ethIfDefaultEthernetPriority": ethIfDefaultEthernetPriority,
       "ethIfPriorityMode": ethIfPriorityMode,
       "ethIfDefaultTrafficClass": ethIfDefaultTrafficClass,
       "ethIfFlowGroupMap": ethIfFlowGroupMap,
       "ethIfLearning": ethIfLearning,
       "ethIfInSpeed": ethIfInSpeed,
       "ethIfInHighSpeed": ethIfInHighSpeed,
       "ethIfOutSpeed": ethIfOutSpeed,
       "ethIfOutHighSpeed": ethIfOutHighSpeed,
       "ethIfVLANNextIndex": ethIfVLANNextIndex,
       "ethIfLastChange": ethIfLastChange,
       "ethIfSrcPmReference": ethIfSrcPmReference,
       "ethIfSnkPmReference": ethIfSnkPmReference,
       "ethIfSrcDegThreshold": ethIfSrcDegThreshold,
       "ethIfSnkDegThreshold": ethIfSnkDegThreshold,
       "ethIfSrcDegPeriod": ethIfSrcDegPeriod,
       "ethIfSnkDegPeriod": ethIfSnkDegPeriod,
       "ethIfSrcReducedBitRateThreshold": ethIfSrcReducedBitRateThreshold,
       "ethIfSnkReducedBitRateThreshold": ethIfSnkReducedBitRateThreshold,
       "ethIfSrcReducedBitRateHighThreshold": ethIfSrcReducedBitRateHighThreshold,
       "ethIfSnkReducedBitRateHighThreshold": ethIfSnkReducedBitRateHighThreshold,
       "ethIfSrcReducedBitRateAIS": ethIfSrcReducedBitRateAIS,
       "ethIfSnkReducedBitRateAIS": ethIfSnkReducedBitRateAIS,
       "ethIfSnkDegAIS": ethIfSnkDegAIS,
       "ethIfSrcMinorReducedBitRateThreshold": ethIfSrcMinorReducedBitRateThreshold,
       "ethIfSnkMinorReducedBitRateThreshold": ethIfSnkMinorReducedBitRateThreshold,
       "ethIfSrcMinorReducedBitRateHighThreshold": ethIfSrcMinorReducedBitRateHighThreshold,
       "ethIfSnkMinorReducedBitRateHighThreshold": ethIfSnkMinorReducedBitRateHighThreshold,
       "ethIfSrcFailure": ethIfSrcFailure,
       "ethIfSnkFailure": ethIfSnkFailure,
       "ethIfInterfaceGroup": ethIfInterfaceGroup,
       "ethIfMaxMaxQueueFrames": ethIfMaxMaxQueueFrames,
       "ethIfDefaultDropPrecedence": ethIfDefaultDropPrecedence,
       "ethIfDropPrecedenceMap": ethIfDropPrecedenceMap,
       "ethIfQueueTable": ethIfQueueTable,
       "ethIfQueueEntry": ethIfQueueEntry,
       "ethIfQueueTrafficClass": ethIfQueueTrafficClass,
       "ethIfQueueMaxOctets": ethIfQueueMaxOctets,
       "ethIfQueueMaxFrames": ethIfQueueMaxFrames,
       "ethIfVLANSetsTable": ethIfVLANSetsTable,
       "ethIfVLANSetsEntry": ethIfVLANSetsEntry,
       "ethIfVLANSetIndex": ethIfVLANSetIndex,
       "ethIfVLANRowStatus": ethIfVLANRowStatus,
       "ethIfVLANSet": ethIfVLANSet,
       "ethIfVLANCustomerId": ethIfVLANCustomerId,
       "ethIfVLANPurpose": ethIfVLANPurpose,
       "ethDot3Table": ethDot3Table,
       "ethDot3Entry": ethDot3Entry,
       "ethDot3AutoNegotiate": ethDot3AutoNegotiate,
       "ethDot3AdvertisedSpeed": ethDot3AdvertisedSpeed,
       "ethDot3AdvertisedDuplex": ethDot3AdvertisedDuplex,
       "ethDot3AdvertisedFlowControl": ethDot3AdvertisedFlowControl,
       "ethDot3ActiveSpeed": ethDot3ActiveSpeed,
       "ethDot3ActiveDuplex": ethDot3ActiveDuplex,
       "ethDot3ActiveFlowControl": ethDot3ActiveFlowControl,
       "ethDot3ForceVLANTagged": ethDot3ForceVLANTagged,
       "ethDot3ForceVLANUntagged": ethDot3ForceVLANUntagged,
       "ethDot3SupportedSpeeds": ethDot3SupportedSpeeds,
       "ethDot3ResetToDefaults": ethDot3ResetToDefaults,
       "ethDot3AutoNegotiateStatus": ethDot3AutoNegotiateStatus,
       "ethDot3AutoNegotiateAllowed": ethDot3AutoNegotiateAllowed,
       "ethDot3AutoNegotiateMandatory": ethDot3AutoNegotiateMandatory,
       "ethDot3SupportedIfType": ethDot3SupportedIfType,
       "ethDot3SelectedIfType": ethDot3SelectedIfType,
       "ethEtsTable": ethEtsTable,
       "ethEtsEntry": ethEtsEntry,
       "ethEtsRowStatus": ethEtsRowStatus,
       "ethEtsMode": ethEtsMode,
       "ethEtsLocalDsti": ethEtsLocalDsti,
       "ethEtsODescription": ethEtsODescription,
       "ethEtsOConnection": ethEtsOConnection,
       "ethEtsSnkExpectChannel": ethEtsSnkExpectChannel,
       "ethEtsTConnectionTable": ethEtsTConnectionTable,
       "ethEtsTConnectionEntry": ethEtsTConnectionEntry,
       "ethEtsTConnectionIndex": ethEtsTConnectionIndex,
       "ethEtsTConnectionRowStatus": ethEtsTConnectionRowStatus,
       "ethEtsTConnection": ethEtsTConnection,
       "ethEtsIndexLookupTable": ethEtsIndexLookupTable,
       "ethEtsIndexLookupEntry": ethEtsIndexLookupEntry,
       "ethEtsIndexLookupDevIndex": ethEtsIndexLookupDevIndex,
       "ethEtsIndexLookupIfIndex": ethEtsIndexLookupIfIndex,
       "ethIfRstpTable": ethIfRstpTable,
       "ethIfRstpEntry": ethIfRstpEntry,
       "ethIfRstpPortIdentifier": ethIfRstpPortIdentifier,
       "ethIfRstpPriority": ethIfRstpPriority,
       "ethIfRstpState": ethIfRstpState,
       "ethIfRstpTopologyChangeAcknowledge": ethIfRstpTopologyChangeAcknowledge,
       "ethIfRstpPathCost": ethIfRstpPathCost,
       "ethIfRstpDesignatedRoot": ethIfRstpDesignatedRoot,
       "ethIfRstpDesignatedCost": ethIfRstpDesignatedCost,
       "ethIfRstpDesignatedBridge": ethIfRstpDesignatedBridge,
       "ethIfRstpDesignatedPort": ethIfRstpDesignatedPort,
       "ethIfRstpAdminEdgePort": ethIfRstpAdminEdgePort,
       "ethIfRstpOperEdgePort": ethIfRstpOperEdgePort,
       "ethIfRstpAdminPointToPointMAC": ethIfRstpAdminPointToPointMAC,
       "ethIfRstpOperPointToPointMAC": ethIfRstpOperPointToPointMAC,
       "ethIfRstpCurrentPathCost": ethIfRstpCurrentPathCost,
       "ethIfgTable": ethIfgTable,
       "ethIfgEntry": ethIfgEntry,
       "ethIfgRowStatus": ethIfgRowStatus,
       "ethIfgMembers": ethIfgMembers,
       "ethIfgDifferentialDelay": ethIfgDifferentialDelay,
       "ethIfgDifferentialDelayValid": ethIfgDifferentialDelayValid,
       "ethIfgAheadInterface": ethIfgAheadInterface,
       "ethIfgHitlessProtection": ethIfgHitlessProtection,
       "ethIfgProtectionStatus": ethIfgProtectionStatus,
       "ethIfgExpectedProtectionStatus": ethIfgExpectedProtectionStatus,
       "ethIfgForceHit": ethIfgForceHit,
       "ethIfgActiveInterface": ethIfgActiveInterface,
       "ethIfgExpectChannel": ethIfgExpectChannel,
       "ethIfQDropThresholdTable": ethIfQDropThresholdTable,
       "ethIfQDropThresholdEntry": ethIfQDropThresholdEntry,
       "ethIfQDropThresDropPrecedence": ethIfQDropThresDropPrecedence,
       "ethIfQDropThresMaxFrames": ethIfQDropThresMaxFrames,
       "ethIfQDropThresCurrentMaxFrames": ethIfQDropThresCurrentMaxFrames,
       "ethIfQDropThresDropProbabilityFunction": ethIfQDropThresDropProbabilityFunction,
       "ethStatisticsGroup": ethStatisticsGroup,
       "ethStatDcap1Table": ethStatDcap1Table,
       "ethStatDcap1Entry": ethStatDcap1Entry,
       "ethStatDcap1Reset": ethStatDcap1Reset,
       "ethStatDcap1TxOctets": ethStatDcap1TxOctets,
       "ethStatDcap1TxPackets": ethStatDcap1TxPackets,
       "ethStatDcap1TxDiscardOctets": ethStatDcap1TxDiscardOctets,
       "ethStatDcap1TxDiscardPackets": ethStatDcap1TxDiscardPackets,
       "ethStatDcap1TxBitrate": ethStatDcap1TxBitrate,
       "ethStatDcap1TxLoad": ethStatDcap1TxLoad,
       "ethStatDcap1RxOctets": ethStatDcap1RxOctets,
       "ethStatDcap1RxPackets": ethStatDcap1RxPackets,
       "ethStatDcap1RxDiscardOctets": ethStatDcap1RxDiscardOctets,
       "ethStatDcap1RxDiscardPackets": ethStatDcap1RxDiscardPackets,
       "ethStatDcap1RxErrorCRC": ethStatDcap1RxErrorCRC,
       "ethStatDcap1RxBitrate": ethStatDcap1RxBitrate,
       "ethStatDcap1RxLoad": ethStatDcap1RxLoad,
       "ethIfStatTable": ethIfStatTable,
       "ethIfStatEntry": ethIfStatEntry,
       "ethIfStatReset": ethIfStatReset,
       "ethIfStatTxBitrate": ethIfStatTxBitrate,
       "ethIfStatTxLoad": ethIfStatTxLoad,
       "ethIfStatRxBitrate": ethIfStatRxBitrate,
       "ethIfStatRxLoad": ethIfStatRxLoad}
)
