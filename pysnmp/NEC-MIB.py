# SNMP MIB module (NEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:19 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DateAndTime,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DateAndTime",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class LinfFilterMaskVpi(Integer32):
    """Custom type LinfFilterMaskVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 12),
    )





class LinfFilterMaskVci(Integer32):
    """Custom type LinfFilterMaskVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 14),
    )





class LinfCellMappingMode(Integer32):
    """Custom type LinfCellMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("plcp", 2))
    )





class LinfScramble(Integer32):
    """Custom type LinfScramble based on Integer32"""
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





class LinfLBO(Integer32):
    """Custom type LinfLBO based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("hi", 2),
          ("length-0-110", 3),
          ("length-110-220", 4),
          ("length-220-330", 5),
          ("length-330-440", 6),
          ("length-440-550", 7),
          ("length-550-660", 8),
          ("length-over660", 9),
          ("low", 1))
    )





class LinfFrameMode(Integer32):
    """Custom type LinfFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("c-bit", 1),
          ("esf", 6),
          ("g751", 4),
          ("g832-g804", 3),
          ("m13", 5),
          ("m23", 2),
          ("sf", 7))
    )





class LinfMinVci(Integer32):
    """Custom type LinfMinVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )





class LinfMaxVci(Integer32):
    """Custom type LinfMaxVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )





class LinfService(Integer32):
    """Custom type LinfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 2),
          ("unstructured", 1))
    )





class LinfInterWorking(Integer32):
    """Custom type LinfInterWorking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("service", 2))
    )





class LinfVendor(Integer32):
    """Custom type LinfVendor based on Integer32"""
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
        *(("cisco-systems", 5),
          ("digital-equipment", 3),
          ("northan-telecom", 4),
          ("notApplicable", 1),
          ("stratacom", 2))
    )





class LinfFractionalType(Integer32):
    """Custom type LinfFractionalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fractional", 2),
          ("unstructured", 1))
    )





class LinfFractionalSet(Integer32):
    """Custom type LinfFractionalSet based on Integer32"""




class LinfCasMode(Integer32):
    """Custom type LinfCasMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 2),
          ("cas", 3),
          ("notApplicable", 1))
    )





class LinfCodingMode(Integer32):
    """Custom type LinfCodingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("hdb3", 1))
    )





class LinfUnUsedParam(Integer32):
    """Custom type LinfUnUsedParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("unused", -1)
    )





class DstAtmAddressFormat(Integer32):
    """Custom type DstAtmAddressFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-164", 1),
          ("noWriting", -1),
          ("nsap", 2))
    )





class DstAtmAddressLength(Integer32):
    """Custom type DstAtmAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 160),
        ValueRangeConstraint(-1, -1),
    )





class DstAtmAddress(OctetString):
    """Custom type DstAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )





class DstPrimaryIfIndex(Integer32):
    """Custom type DstPrimaryIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
        ValueRangeConstraint(-1, -1),
    )





class DstPrimaryVPI(Integer32):
    """Custom type DstPrimaryVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(-1, -1),
    )





class DstSecondaryIfIndex(Integer32):
    """Custom type DstSecondaryIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
        ValueRangeConstraint(-1, -1),
    )





class DstSecondaryVPI(Integer32):
    """Custom type DstSecondaryVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(-1, -1),
    )





class ConnRouteOpeFailureCause(Integer32):
    """Custom type ConnRouteOpeFailureCause based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("allocateSucceed", 2),
          ("noWriting", -1),
          ("other", 1),
          ("parameterIsNotEnough", 4),
          ("specifiedAddressIsAlreadyExisting", 6),
          ("specifiedAddressIsIllegal", 5),
          ("specifiedAddressIsNotExisting", 7),
          ("tableIsFull", 3))
    )





class ConnSoftPvcSrcAtmAddressFormat(Integer32):
    """Custom type ConnSoftPvcSrcAtmAddressFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-164", 1),
          ("noWriting", -1),
          ("nsap", 2))
    )





class ConnSoftPvcDstAtmAddressFormat(Integer32):
    """Custom type ConnSoftPvcDstAtmAddressFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-164", 1),
          ("noWriting", -1),
          ("nsap", 2))
    )





class ConnSoftPvcEstSrcInfIndex(Integer32):
    """Custom type ConnSoftPvcEstSrcInfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )





class ConnProfileIndex(Integer32):
    """Custom type ConnProfileIndex based on Integer32"""




class ConnFrProfileIndex(Integer32):
    """Custom type ConnFrProfileIndex based on Integer32"""




class ClockSlaveLineStatus(Integer32):
    """Custom type ClockSlaveLineStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("adminDown", 5),
          ("frequencyOutOfRange", 13),
          ("hardError", 4),
          ("linfDown", 7),
          ("lossOf64kClock", 11),
          ("lossOf8kClock", 12),
          ("notApplicable", 1),
          ("notExist", 6),
          ("notSupported", 9),
          ("standby", 3),
          ("syncronizedFailure", 10),
          ("testing", 8))
    )





class PnniAtmAddr(OctetString):
    """Custom type PnniAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )





class PnniNodeId(OctetString):
    """Custom type PnniNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )





class PnniPeerGroupId(OctetString):
    """Custom type PnniPeerGroupId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )





class PnniLevel(Integer32):
    """Custom type PnniLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_NecProduct_ObjectIdentity = ObjectIdentity
necProduct = _NecProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1)
)
_Atomis_ObjectIdentity = ObjectIdentity
atomis = _Atomis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 14)
)
_M7_phase2_ObjectIdentity = ObjectIdentity
m7_phase2 = _M7_phase2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 14, 9)
)
_M7_corporate_ObjectIdentity = ObjectIdentity
m7_corporate = _M7_corporate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 14, 12)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_Atomis_mib_ObjectIdentity = ObjectIdentity
atomis_mib = _Atomis_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14)
)
_M7_phase2_mib_ObjectIdentity = ObjectIdentity
m7_phase2_mib = _M7_phase2_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9)
)
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1)
)
_NodeStatus_ObjectIdentity = ObjectIdentity
nodeStatus = _NodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1)
)


class _NodeStatusOperStatus_Type(Integer32):
    """Custom type nodeStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("down", 1),
          ("installing", 3))
    )


_NodeStatusOperStatus_Type.__name__ = "Integer32"
_NodeStatusOperStatus_Object = MibScalar
nodeStatusOperStatus = _NodeStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 1),
    _NodeStatusOperStatus_Type()
)
nodeStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusOperStatus.setStatus("mandatory")
_NodeStatusStartTime_Type = DateAndTime
_NodeStatusStartTime_Object = MibScalar
nodeStatusStartTime = _NodeStatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 2),
    _NodeStatusStartTime_Type()
)
nodeStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusStartTime.setStatus("mandatory")
_NodeStatusNodeId_Type = OctetString
_NodeStatusNodeId_Object = MibScalar
nodeStatusNodeId = _NodeStatusNodeId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 3),
    _NodeStatusNodeId_Type()
)
nodeStatusNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusNodeId.setStatus("mandatory")


class _NodeStatusSelfSystem_Type(Integer32):
    """Custom type nodeStatusSelfSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system-0", 1),
          ("system-1", 2))
    )


_NodeStatusSelfSystem_Type.__name__ = "Integer32"
_NodeStatusSelfSystem_Object = MibScalar
nodeStatusSelfSystem = _NodeStatusSelfSystem_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 4),
    _NodeStatusSelfSystem_Type()
)
nodeStatusSelfSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusSelfSystem.setStatus("mandatory")


class _NodeStatusSwitchType_Type(Integer32):
    """Custom type nodeStatusSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sw-Engine-10G", 2),
          ("sw-Engine-5G", 1))
    )


_NodeStatusSwitchType_Type.__name__ = "Integer32"
_NodeStatusSwitchType_Object = MibScalar
nodeStatusSwitchType = _NodeStatusSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 5),
    _NodeStatusSwitchType_Type()
)
nodeStatusSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusSwitchType.setStatus("mandatory")


class _NodeStatusFan_Type(Integer32):
    """Custom type nodeStatusFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 1))
    )


_NodeStatusFan_Type.__name__ = "Integer32"
_NodeStatusFan_Object = MibScalar
nodeStatusFan = _NodeStatusFan_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 6),
    _NodeStatusFan_Type()
)
nodeStatusFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusFan.setStatus("mandatory")


class _NodeStatusEnvironment_Type(Integer32):
    """Custom type nodeStatusEnvironment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("noGood", 2))
    )


_NodeStatusEnvironment_Type.__name__ = "Integer32"
_NodeStatusEnvironment_Object = MibScalar
nodeStatusEnvironment = _NodeStatusEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 1, 7),
    _NodeStatusEnvironment_Type()
)
nodeStatusEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusEnvironment.setStatus("mandatory")
_NodeStatusTable_Object = MibTable
nodeStatusTable = _NodeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 2)
)
if mibBuilder.loadTexts:
    nodeStatusTable.setStatus("mandatory")
_NodeStatusEntry_Object = MibTableRow
nodeStatusEntry = _NodeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 2, 1)
)
nodeStatusEntry.setIndexNames(
    (0, "NEC-MIB", "nodeStatusIndex"),
)
if mibBuilder.loadTexts:
    nodeStatusEntry.setStatus("mandatory")
_NodeStatusIndex_Type = Integer32
_NodeStatusIndex_Object = MibTableColumn
nodeStatusIndex = _NodeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 2, 1, 1),
    _NodeStatusIndex_Type()
)
nodeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeStatusIndex.setStatus("mandatory")


class _NodeStatusPower_Type(Integer32):
    """Custom type nodeStatusPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 1),
          ("notInstalled", 99))
    )


_NodeStatusPower_Type.__name__ = "Integer32"
_NodeStatusPower_Object = MibTableColumn
nodeStatusPower = _NodeStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 2, 1, 2),
    _NodeStatusPower_Type()
)
nodeStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusPower.setStatus("mandatory")


class _NodeStatusSwitchMode_Type(Integer32):
    """Custom type nodeStatusSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("notInstalled", 99),
          ("sby", 2))
    )


_NodeStatusSwitchMode_Type.__name__ = "Integer32"
_NodeStatusSwitchMode_Object = MibTableColumn
nodeStatusSwitchMode = _NodeStatusSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 2, 1, 3),
    _NodeStatusSwitchMode_Type()
)
nodeStatusSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusSwitchMode.setStatus("mandatory")


class _NodeStatusSwitch_Type(Integer32):
    """Custom type nodeStatusSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("diagnosis-status-NG", 4),
          ("diagnostics", 3),
          ("failure", 2),
          ("initializing", 5),
          ("normal", 1),
          ("notInstalled", 99))
    )


_NodeStatusSwitch_Type.__name__ = "Integer32"
_NodeStatusSwitch_Object = MibTableColumn
nodeStatusSwitch = _NodeStatusSwitch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 2, 1, 4),
    _NodeStatusSwitch_Type()
)
nodeStatusSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatusSwitch.setStatus("mandatory")
_NodePCMCIATable_Object = MibTable
nodePCMCIATable = _NodePCMCIATable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 3)
)
if mibBuilder.loadTexts:
    nodePCMCIATable.setStatus("mandatory")
_NodePCMCIAEntry_Object = MibTableRow
nodePCMCIAEntry = _NodePCMCIAEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 3, 1)
)
nodePCMCIAEntry.setIndexNames(
    (0, "NEC-MIB", "nodeStatusIndex"),
    (0, "NEC-MIB", "nodePCMCIAIndex"),
)
if mibBuilder.loadTexts:
    nodePCMCIAEntry.setStatus("mandatory")


class _NodePCMCIAIndex_Type(Integer32):
    """Custom type nodePCMCIAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NodePCMCIAIndex_Type.__name__ = "Integer32"
_NodePCMCIAIndex_Object = MibTableColumn
nodePCMCIAIndex = _NodePCMCIAIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 3, 1, 1),
    _NodePCMCIAIndex_Type()
)
nodePCMCIAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodePCMCIAIndex.setStatus("mandatory")


class _NodePCMCIAStatus_Type(Integer32):
    """Custom type nodePCMCIAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("busy", 4),
          ("failure", 2),
          ("initializing", 3),
          ("normal", 1),
          ("notInstalled", 99),
          ("unknown", 5))
    )


_NodePCMCIAStatus_Type.__name__ = "Integer32"
_NodePCMCIAStatus_Object = MibTableColumn
nodePCMCIAStatus = _NodePCMCIAStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 3, 1, 2),
    _NodePCMCIAStatus_Type()
)
nodePCMCIAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePCMCIAStatus.setStatus("mandatory")


class _NodePCMCIAType_Type(Integer32):
    """Custom type nodePCMCIAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ata-card", 2),
          ("lan-card", 1),
          ("notInstalled", 99),
          ("unknown", 3))
    )


_NodePCMCIAType_Type.__name__ = "Integer32"
_NodePCMCIAType_Object = MibTableColumn
nodePCMCIAType = _NodePCMCIAType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 3, 1, 3),
    _NodePCMCIAType_Type()
)
nodePCMCIAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePCMCIAType.setStatus("mandatory")
_NodeOpe_ObjectIdentity = ObjectIdentity
nodeOpe = _NodeOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 4)
)


class _NodeOpeSave_Type(Integer32):
    """Custom type nodeOpeSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("save", 2))
    )


_NodeOpeSave_Type.__name__ = "Integer32"
_NodeOpeSave_Object = MibScalar
nodeOpeSave = _NodeOpeSave_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 4, 1),
    _NodeOpeSave_Type()
)
nodeOpeSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeOpeSave.setStatus("mandatory")


class _NodeOpeSaveResult_Type(Integer32):
    """Custom type nodeOpeSaveResult based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("nearend", 5),
          ("nearend-0", 6),
          ("nearend-0-failure-1", 7),
          ("nearend-1", 8),
          ("nearend-1-failure-0", 9),
          ("notReady", 10),
          ("ready", 11),
          ("succeed", 1),
          ("succeed-0", 2),
          ("succeed-1", 3),
          ("temporaryFailure", 4))
    )


_NodeOpeSaveResult_Type.__name__ = "Integer32"
_NodeOpeSaveResult_Object = MibScalar
nodeOpeSaveResult = _NodeOpeSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 4, 2),
    _NodeOpeSaveResult_Type()
)
nodeOpeSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOpeSaveResult.setStatus("mandatory")


class _NodeOpeCopy_Type(Integer32):
    """Custom type nodeOpeCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copy-all-from-act", 2),
          ("copy-all-from-sby", 3),
          ("copy-config-from-act", 4),
          ("copy-config-from-sby", 5),
          ("copy-system-from-act", 6),
          ("copy-system-from-sby", 7),
          ("noOperation", 1))
    )


_NodeOpeCopy_Type.__name__ = "Integer32"
_NodeOpeCopy_Object = MibScalar
nodeOpeCopy = _NodeOpeCopy_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 4, 3),
    _NodeOpeCopy_Type()
)
nodeOpeCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeOpeCopy.setStatus("mandatory")


class _NodeOpeCopyResult_Type(Integer32):
    """Custom type nodeOpeCopyResult based on Integer32"""
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
        *(("nearend", 3),
          ("notReady", 4),
          ("ready", 5),
          ("succeed", 1),
          ("temporaryFailure", 2))
    )


_NodeOpeCopyResult_Type.__name__ = "Integer32"
_NodeOpeCopyResult_Object = MibScalar
nodeOpeCopyResult = _NodeOpeCopyResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 4, 4),
    _NodeOpeCopyResult_Type()
)
nodeOpeCopyResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOpeCopyResult.setStatus("mandatory")


class _NodeOpeReset_Type(Integer32):
    """Custom type nodeOpeReset based on Integer32"""
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
        *(("ach", 4),
          ("noOperation", 1),
          ("reset-act", 2),
          ("reset-sby", 3))
    )


_NodeOpeReset_Type.__name__ = "Integer32"
_NodeOpeReset_Object = MibScalar
nodeOpeReset = _NodeOpeReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 1, 4, 5),
    _NodeOpeReset_Type()
)
nodeOpeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeOpeReset.setStatus("mandatory")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2)
)
_SlotIfConfTable_Object = MibTable
slotIfConfTable = _SlotIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1)
)
if mibBuilder.loadTexts:
    slotIfConfTable.setStatus("mandatory")
_SlotIfConfEntry_Object = MibTableRow
slotIfConfEntry = _SlotIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1)
)
slotIfConfEntry.setIndexNames(
    (0, "NEC-MIB", "slotIfConfIndex"),
)
if mibBuilder.loadTexts:
    slotIfConfEntry.setStatus("mandatory")


class _SlotIfConfIndex_Type(Integer32):
    """Custom type slotIfConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SlotIfConfIndex_Type.__name__ = "Integer32"
_SlotIfConfIndex_Object = MibTableColumn
slotIfConfIndex = _SlotIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 1),
    _SlotIfConfIndex_Type()
)
slotIfConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfIndex.setStatus("mandatory")


class _SlotIfConfPhysType_Type(Integer32):
    """Custom type slotIfConfPhysType based on Integer32"""
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
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bts-1", 13),
          ("bts-4", 14),
          ("ce-J2", 59),
          ("ce-ds1", 57),
          ("ce-ds3", 56),
          ("ce-e1", 58),
          ("dcs", 55),
          ("ds1", 16),
          ("ds3", 11),
          ("e1", 17),
          ("e3", 12),
          ("fr-ds1", 53),
          ("fr-e1", 54),
          ("j2-6M-4M-3M", 7),
          ("notInstalled", 99),
          ("oc12c-SMF-Type-A", 9),
          ("oc12c-SMF-Type-B", 10),
          ("oc3c-MMF", 5),
          ("oc3c-POF", 18),
          ("oc3c-SMF-Long", 3),
          ("oc3c-SMF-Short", 4),
          ("other", 1),
          ("primary-1536K-1152K-768K-512K-384K-256K-192K", 15),
          ("relay-6Mcel", 6),
          ("sts3c-COAXIAL", 19),
          ("svr", 52),
          ("svr2", 60),
          ("taxi-100M", 2),
          ("utp-5", 8),
          ("vod-RxHFC4M", 50),
          ("vod-TxHFC27M", 51))
    )


_SlotIfConfPhysType_Type.__name__ = "Integer32"
_SlotIfConfPhysType_Object = MibTableColumn
slotIfConfPhysType = _SlotIfConfPhysType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 2),
    _SlotIfConfPhysType_Type()
)
slotIfConfPhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfPhysType.setStatus("mandatory")
_SlotIfConfRev_Type = DisplayString
_SlotIfConfRev_Object = MibTableColumn
slotIfConfRev = _SlotIfConfRev_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 3),
    _SlotIfConfRev_Type()
)
slotIfConfRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfRev.setStatus("mandatory")


class _SlotIfConfStatus_Type(Integer32):
    """Custom type slotIfConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("initializing", 5),
          ("installing", 6),
          ("notInstalled", 99),
          ("other", 1),
          ("outOfService", 3),
          ("testing", 4))
    )


_SlotIfConfStatus_Type.__name__ = "Integer32"
_SlotIfConfStatus_Object = MibTableColumn
slotIfConfStatus = _SlotIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 4),
    _SlotIfConfStatus_Type()
)
slotIfConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfStatus.setStatus("mandatory")


class _SlotIfConfBufferType_Type(Integer32):
    """Custom type slotIfConfBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("fr-buffer", 4),
          ("fr-buffer2", 5),
          ("notInstalled", 99),
          ("other", 1),
          ("ph1-buffer", 2),
          ("ph2-buffer", 3))
    )


_SlotIfConfBufferType_Type.__name__ = "Integer32"
_SlotIfConfBufferType_Object = MibTableColumn
slotIfConfBufferType = _SlotIfConfBufferType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 5),
    _SlotIfConfBufferType_Type()
)
slotIfConfBufferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfBufferType.setStatus("mandatory")
_SlotIfConfBufferRev_Type = DisplayString
_SlotIfConfBufferRev_Object = MibTableColumn
slotIfConfBufferRev = _SlotIfConfBufferRev_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 6),
    _SlotIfConfBufferRev_Type()
)
slotIfConfBufferRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfBufferRev.setStatus("mandatory")


class _SlotIfConfReset_Type(Integer32):
    """Custom type slotIfConfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("notInstalled", 99),
          ("reset", 2))
    )


_SlotIfConfReset_Type.__name__ = "Integer32"
_SlotIfConfReset_Object = MibTableColumn
slotIfConfReset = _SlotIfConfReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 7),
    _SlotIfConfReset_Type()
)
slotIfConfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotIfConfReset.setStatus("mandatory")


class _SlotIfConfResetResult_Type(Integer32):
    """Custom type slotIfConfResetResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("diagnostics", 3),
          ("notInstalled", 99),
          ("other", 2),
          ("succeed", 1),
          ("unchangeableSlaveLine", 4))
    )


_SlotIfConfResetResult_Type.__name__ = "Integer32"
_SlotIfConfResetResult_Object = MibTableColumn
slotIfConfResetResult = _SlotIfConfResetResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 2, 1, 1, 8),
    _SlotIfConfResetResult_Type()
)
slotIfConfResetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfConfResetResult.setStatus("mandatory")
_Linf_ObjectIdentity = ObjectIdentity
linf = _Linf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3)
)
_LinfStatusTable_Object = MibTable
linfStatusTable = _LinfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1)
)
if mibBuilder.loadTexts:
    linfStatusTable.setStatus("mandatory")
_LinfStatusEntry_Object = MibTableRow
linfStatusEntry = _LinfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1)
)
linfStatusEntry.setIndexNames(
    (0, "NEC-MIB", "linfIndex"),
)
if mibBuilder.loadTexts:
    linfStatusEntry.setStatus("mandatory")


class _LinfIndex_Type(Integer32):
    """Custom type linfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_LinfIndex_Type.__name__ = "Integer32"
_LinfIndex_Object = MibTableColumn
linfIndex = _LinfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 1),
    _LinfIndex_Type()
)
linfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfIndex.setStatus("mandatory")


class _LinfStatus_Type(Integer32):
    """Custom type linfStatus based on Integer32"""
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
              80,
              81,
              82,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("administratively-down", 98),
          ("ais", 10),
          ("ais-path", 5),
          ("ais-section", 6),
          ("failure", 97),
          ("frequency-out-of-range", 82),
          ("idle", 14),
          ("loc", 4),
          ("lof", 3),
          ("lop", 9),
          ("los", 2),
          ("loss-of-64K-clock", 80),
          ("loss-of-8K-clock", 81),
          ("normal", 1),
          ("notInstalled", 99),
          ("oof", 13),
          ("payload-all-one", 11),
          ("plcp-lof", 17),
          ("plcp-oof", 16),
          ("plcp-yellow", 18),
          ("rai", 12),
          ("rdi", 15),
          ("red", 19),
          ("yellow-path", 8),
          ("yellow-section", 7))
    )


_LinfStatus_Type.__name__ = "Integer32"
_LinfStatus_Object = MibTableColumn
linfStatus = _LinfStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 2),
    _LinfStatus_Type()
)
linfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfStatus.setStatus("mandatory")


class _LinfLoopBack_Type(Integer32):
    """Custom type linfLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("localLoopBack", 3),
          ("normal", 2),
          ("notInstalled", 99),
          ("others", 1),
          ("remoteLoopBack", 4))
    )


_LinfLoopBack_Type.__name__ = "Integer32"
_LinfLoopBack_Object = MibTableColumn
linfLoopBack = _LinfLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 3),
    _LinfLoopBack_Type()
)
linfLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linfLoopBack.setStatus("mandatory")


class _LinfConf_Type(Integer32):
    """Custom type linfConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("nni", 7),
          ("notInstalled", 99),
          ("others", 1),
          ("private-NNI", 3),
          ("private-UNI", 2),
          ("public-UNI", 4),
          ("uni", 6))
    )


_LinfConf_Type.__name__ = "Integer32"
_LinfConf_Object = MibTableColumn
linfConf = _LinfConf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 4),
    _LinfConf_Type()
)
linfConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfConf.setStatus("mandatory")
_LinfFwdAvailableBandWidth_Type = Integer32
_LinfFwdAvailableBandWidth_Object = MibTableColumn
linfFwdAvailableBandWidth = _LinfFwdAvailableBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 5),
    _LinfFwdAvailableBandWidth_Type()
)
linfFwdAvailableBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfFwdAvailableBandWidth.setStatus("mandatory")
_LinfBkwdAvailableBandWidth_Type = Integer32
_LinfBkwdAvailableBandWidth_Object = MibTableColumn
linfBkwdAvailableBandWidth = _LinfBkwdAvailableBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 6),
    _LinfBkwdAvailableBandWidth_Type()
)
linfBkwdAvailableBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfBkwdAvailableBandWidth.setStatus("mandatory")


class _LinfJ2Rate_Type(Integer32):
    """Custom type linfJ2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("not-leased-line", 1),
          ("notInstalled", 99),
          ("type-3-Mbps", 2),
          ("type-4point5-Mbps", 3),
          ("type-6point3-Mbps", 4))
    )


_LinfJ2Rate_Type.__name__ = "Integer32"
_LinfJ2Rate_Object = MibTableColumn
linfJ2Rate = _LinfJ2Rate_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 7),
    _LinfJ2Rate_Type()
)
linfJ2Rate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfJ2Rate.setStatus("mandatory")


class _LinfCacFactor_Type(Integer32):
    """Custom type linfCacFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000),
    )


_LinfCacFactor_Type.__name__ = "Integer32"
_LinfCacFactor_Object = MibTableColumn
linfCacFactor = _LinfCacFactor_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 8),
    _LinfCacFactor_Type()
)
linfCacFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linfCacFactor.setStatus("mandatory")


class _LinfLoopBackCause_Type(Integer32):
    """Custom type linfLoopBackCause based on Integer32"""
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
        *(("adminDown", 6),
          ("alreadyRegistered", 5),
          ("diagnosis", 2),
          ("failure", 3),
          ("initializing", 7),
          ("notInstalled", 99),
          ("notSupportedByPkg", 4),
          ("succeed", 1))
    )


_LinfLoopBackCause_Type.__name__ = "Integer32"
_LinfLoopBackCause_Object = MibTableColumn
linfLoopBackCause = _LinfLoopBackCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 9),
    _LinfLoopBackCause_Type()
)
linfLoopBackCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfLoopBackCause.setStatus("mandatory")
_LinfBandWidth_Type = Integer32
_LinfBandWidth_Object = MibTableColumn
linfBandWidth = _LinfBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 10),
    _LinfBandWidth_Type()
)
linfBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfBandWidth.setStatus("mandatory")


class _LinfRecommendation_Type(Integer32):
    """Custom type linfRecommendation based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 7),
          ("atmForum", 2),
          ("fourVendor", 8),
          ("frameRelayForum", 5),
          ("itu", 3),
          ("itu-t", 6),
          ("notInstalled", 99),
          ("other", 1),
          ("ttc", 4))
    )


_LinfRecommendation_Type.__name__ = "Integer32"
_LinfRecommendation_Object = MibTableColumn
linfRecommendation = _LinfRecommendation_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 11),
    _LinfRecommendation_Type()
)
linfRecommendation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfRecommendation.setStatus("mandatory")


class _LinfUnassignedIdle_Type(Integer32):
    """Custom type linfUnassignedIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("idle", 3),
          ("notApplicable", 1),
          ("notInstalled", 99),
          ("unAssigned", 2))
    )


_LinfUnassignedIdle_Type.__name__ = "Integer32"
_LinfUnassignedIdle_Object = MibTableColumn
linfUnassignedIdle = _LinfUnassignedIdle_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 12),
    _LinfUnassignedIdle_Type()
)
linfUnassignedIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfUnassignedIdle.setStatus("mandatory")


class _LinfMaxActiveVpiBits_Type(Integer32):
    """Custom type linfMaxActiveVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LinfMaxActiveVpiBits_Type.__name__ = "Integer32"
_LinfMaxActiveVpiBits_Object = MibTableColumn
linfMaxActiveVpiBits = _LinfMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 13),
    _LinfMaxActiveVpiBits_Type()
)
linfMaxActiveVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfMaxActiveVpiBits.setStatus("mandatory")


class _LinfMaxActiveVciBits_Type(Integer32):
    """Custom type linfMaxActiveVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_LinfMaxActiveVciBits_Type.__name__ = "Integer32"
_LinfMaxActiveVciBits_Object = MibTableColumn
linfMaxActiveVciBits = _LinfMaxActiveVciBits_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 14),
    _LinfMaxActiveVciBits_Type()
)
linfMaxActiveVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfMaxActiveVciBits.setStatus("mandatory")
_LinfPhysType_Type = Integer32
_LinfPhysType_Object = MibTableColumn
linfPhysType = _LinfPhysType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 15),
    _LinfPhysType_Type()
)
linfPhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfPhysType.setStatus("mandatory")
_LinfParam1_Type = Integer32
_LinfParam1_Object = MibTableColumn
linfParam1 = _LinfParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 16),
    _LinfParam1_Type()
)
linfParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam1.setStatus("mandatory")
_LinfParam2_Type = Integer32
_LinfParam2_Object = MibTableColumn
linfParam2 = _LinfParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 17),
    _LinfParam2_Type()
)
linfParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam2.setStatus("mandatory")
_LinfParam3_Type = Integer32
_LinfParam3_Object = MibTableColumn
linfParam3 = _LinfParam3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 18),
    _LinfParam3_Type()
)
linfParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam3.setStatus("mandatory")
_LinfParam4_Type = Integer32
_LinfParam4_Object = MibTableColumn
linfParam4 = _LinfParam4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 19),
    _LinfParam4_Type()
)
linfParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam4.setStatus("mandatory")
_LinfParam5_Type = Integer32
_LinfParam5_Object = MibTableColumn
linfParam5 = _LinfParam5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 20),
    _LinfParam5_Type()
)
linfParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam5.setStatus("mandatory")
_LinfParam6_Type = Integer32
_LinfParam6_Object = MibTableColumn
linfParam6 = _LinfParam6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 21),
    _LinfParam6_Type()
)
linfParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam6.setStatus("mandatory")
_LinfParam7_Type = Integer32
_LinfParam7_Object = MibTableColumn
linfParam7 = _LinfParam7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 1, 1, 22),
    _LinfParam7_Type()
)
linfParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfParam7.setStatus("mandatory")
_LinfFifoConfTable_Object = MibTable
linfFifoConfTable = _LinfFifoConfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2)
)
if mibBuilder.loadTexts:
    linfFifoConfTable.setStatus("mandatory")
_LinfFifoConfEntry_Object = MibTableRow
linfFifoConfEntry = _LinfFifoConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1)
)
linfFifoConfEntry.setIndexNames(
    (0, "NEC-MIB", "linfFifoConfifIndex"),
    (0, "NEC-MIB", "linfFifoConfIndex"),
)
if mibBuilder.loadTexts:
    linfFifoConfEntry.setStatus("mandatory")
_LinfFifoConfifIndex_Type = Integer32
_LinfFifoConfifIndex_Object = MibTableColumn
linfFifoConfifIndex = _LinfFifoConfifIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 1),
    _LinfFifoConfifIndex_Type()
)
linfFifoConfifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfifIndex.setStatus("mandatory")
_LinfFifoConfIndex_Type = Integer32
_LinfFifoConfIndex_Object = MibTableColumn
linfFifoConfIndex = _LinfFifoConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 2),
    _LinfFifoConfIndex_Type()
)
linfFifoConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfIndex.setStatus("mandatory")


class _LinfFifoConfStatus_Type(Integer32):
    """Custom type linfFifoConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overflow", 2))
    )


_LinfFifoConfStatus_Type.__name__ = "Integer32"
_LinfFifoConfStatus_Object = MibTableColumn
linfFifoConfStatus = _LinfFifoConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 3),
    _LinfFifoConfStatus_Type()
)
linfFifoConfStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfStatus.setStatus("mandatory")


class _LinfFifoConfPeekRate_Type(Integer32):
    """Custom type linfFifoConfPeekRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1412830),
    )


_LinfFifoConfPeekRate_Type.__name__ = "Integer32"
_LinfFifoConfPeekRate_Object = MibTableColumn
linfFifoConfPeekRate = _LinfFifoConfPeekRate_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 4),
    _LinfFifoConfPeekRate_Type()
)
linfFifoConfPeekRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfPeekRate.setStatus("mandatory")


class _LinfFifoConfSustainRate_Type(Integer32):
    """Custom type linfFifoConfSustainRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1412830),
    )


_LinfFifoConfSustainRate_Type.__name__ = "Integer32"
_LinfFifoConfSustainRate_Object = MibTableColumn
linfFifoConfSustainRate = _LinfFifoConfSustainRate_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 5),
    _LinfFifoConfSustainRate_Type()
)
linfFifoConfSustainRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfSustainRate.setStatus("mandatory")


class _LinfFifoConfMaxBurstSize_Type(Integer32):
    """Custom type linfFifoConfMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1412830),
    )


_LinfFifoConfMaxBurstSize_Type.__name__ = "Integer32"
_LinfFifoConfMaxBurstSize_Object = MibTableColumn
linfFifoConfMaxBurstSize = _LinfFifoConfMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 6),
    _LinfFifoConfMaxBurstSize_Type()
)
linfFifoConfMaxBurstSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfMaxBurstSize.setStatus("mandatory")


class _LinfFifoConfRowStatus_Type(Integer32):
    """Custom type linfFifoConfRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_LinfFifoConfRowStatus_Type.__name__ = "Integer32"
_LinfFifoConfRowStatus_Object = MibTableColumn
linfFifoConfRowStatus = _LinfFifoConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 3, 2, 1, 7),
    _LinfFifoConfRowStatus_Type()
)
linfFifoConfRowStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linfFifoConfRowStatus.setStatus("mandatory")
_Conn_ObjectIdentity = ObjectIdentity
conn = _Conn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4)
)
_ConnPvc_ObjectIdentity = ObjectIdentity
connPvc = _ConnPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1)
)
_ConnPvcOpe_ObjectIdentity = ObjectIdentity
connPvcOpe = _ConnPvcOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1)
)


class _ConnPvcOpeLowPort_Type(Integer32):
    """Custom type connPvcOpeLowPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
        ValueRangeConstraint(-1, -1),
    )


_ConnPvcOpeLowPort_Type.__name__ = "Integer32"
_ConnPvcOpeLowPort_Object = MibScalar
connPvcOpeLowPort = _ConnPvcOpeLowPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 1),
    _ConnPvcOpeLowPort_Type()
)
connPvcOpeLowPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeLowPort.setStatus("mandatory")


class _ConnPvcOpeLowVpi_Type(Integer32):
    """Custom type connPvcOpeLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(-1, -1),
    )


_ConnPvcOpeLowVpi_Type.__name__ = "Integer32"
_ConnPvcOpeLowVpi_Object = MibScalar
connPvcOpeLowVpi = _ConnPvcOpeLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 2),
    _ConnPvcOpeLowVpi_Type()
)
connPvcOpeLowVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeLowVpi.setStatus("mandatory")


class _ConnPvcOpeLowVci_Type(Integer32):
    """Custom type connPvcOpeLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(-1, -1),
    )


_ConnPvcOpeLowVci_Type.__name__ = "Integer32"
_ConnPvcOpeLowVci_Object = MibScalar
connPvcOpeLowVci = _ConnPvcOpeLowVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 3),
    _ConnPvcOpeLowVci_Type()
)
connPvcOpeLowVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeLowVci.setStatus("mandatory")


class _ConnPvcOpeHighPort_Type(Integer32):
    """Custom type connPvcOpeHighPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
        ValueRangeConstraint(-1, -1),
    )


_ConnPvcOpeHighPort_Type.__name__ = "Integer32"
_ConnPvcOpeHighPort_Object = MibScalar
connPvcOpeHighPort = _ConnPvcOpeHighPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 4),
    _ConnPvcOpeHighPort_Type()
)
connPvcOpeHighPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeHighPort.setStatus("mandatory")


class _ConnPvcOpeHighVpi_Type(Integer32):
    """Custom type connPvcOpeHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(-1, -1),
    )


_ConnPvcOpeHighVpi_Type.__name__ = "Integer32"
_ConnPvcOpeHighVpi_Object = MibScalar
connPvcOpeHighVpi = _ConnPvcOpeHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 5),
    _ConnPvcOpeHighVpi_Type()
)
connPvcOpeHighVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeHighVpi.setStatus("mandatory")


class _ConnPvcOpeHighVci_Type(Integer32):
    """Custom type connPvcOpeHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(-1, -1),
    )


_ConnPvcOpeHighVci_Type.__name__ = "Integer32"
_ConnPvcOpeHighVci_Object = MibScalar
connPvcOpeHighVci = _ConnPvcOpeHighVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 6),
    _ConnPvcOpeHighVci_Type()
)
connPvcOpeHighVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeHighVci.setStatus("mandatory")


class _ConnPvcOpeTopology_Type(Integer32):
    """Custom type connPvcOpeTopology based on Integer32"""
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
        *(("bi-directional-VCC", 2),
          ("bi-directional-VPC", 4),
          ("broadcast-VCC", 6),
          ("broadcast-VPC", 5),
          ("uni-directional-VCC", 1),
          ("uni-directional-VPC", 3))
    )


_ConnPvcOpeTopology_Type.__name__ = "Integer32"
_ConnPvcOpeTopology_Object = MibScalar
connPvcOpeTopology = _ConnPvcOpeTopology_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 7),
    _ConnPvcOpeTopology_Type()
)
connPvcOpeTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeTopology.setStatus("mandatory")


class _ConnPvcOpeTrafficType_Type(Integer32):
    """Custom type connPvcOpeTrafficType based on Integer32"""
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
        *(("traffic-ABR", 4),
          ("traffic-CBR", 1),
          ("traffic-UBR", 5),
          ("traffic-nrt-VBR", 3),
          ("traffic-rt-VBR", 2))
    )


_ConnPvcOpeTrafficType_Type.__name__ = "Integer32"
_ConnPvcOpeTrafficType_Object = MibScalar
connPvcOpeTrafficType = _ConnPvcOpeTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 8),
    _ConnPvcOpeTrafficType_Type()
)
connPvcOpeTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeTrafficType.setStatus("mandatory")


class _ConnPvcOpeStatus_Type(Integer32):
    """Custom type connPvcOpeStatus based on Integer32"""
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
        *(("add", 3),
          ("allocate", 1),
          ("delete", 4),
          ("establish", 2),
          ("free", 6),
          ("remove", 5))
    )


_ConnPvcOpeStatus_Type.__name__ = "Integer32"
_ConnPvcOpeStatus_Object = MibScalar
connPvcOpeStatus = _ConnPvcOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 9),
    _ConnPvcOpeStatus_Type()
)
connPvcOpeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeStatus.setStatus("mandatory")


class _ConnPvcOpeCause_Type(Integer32):
    """Custom type connPvcOpeCause based on Integer32"""
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
        *(("allocateSucceed", 2),
          ("broadcastTableFull", 8),
          ("diagnostics", 18),
          ("illegalHighFileName", 13),
          ("illegalHighRateForUPC", 21),
          ("illegalHighShaper", 15),
          ("illegalLowFileName", 12),
          ("illegalLowRateForUPC", 20),
          ("illegalLowShaper", 14),
          ("illegalOperation", 16),
          ("illegalTopology", 25),
          ("inconsistentVPVC", 9),
          ("insusfficientPCRofProfile", 33),
          ("leafSetAnotherLine", 32),
          ("lineDiagnosis", 10),
          ("missMatchTrfType", 11),
          ("missMatchTrfTypeHighShaperForGateway", 31),
          ("missMatchTrfTypeLowShaperForGateway", 30),
          ("noCevc", 23),
          ("noDlci", 24),
          ("noHighShaperForGateway", 27),
          ("noLowShaperForGateway", 26),
          ("noPvcHighShaperForGateway", 29),
          ("noPvcLowShaperForGateway", 28),
          ("noSpecifiedConnection", 22),
          ("otherFailure", 19),
          ("parameterIsNotEnough", 17),
          ("rateHighOverFlow", 7),
          ("rateLowOverFlow", 6),
          ("rowExisting", 1),
          ("vpivciHighBusy", 4),
          ("vpivciLowBusy", 3),
          ("vpivciOutOfRange", 5))
    )


_ConnPvcOpeCause_Type.__name__ = "Integer32"
_ConnPvcOpeCause_Object = MibScalar
connPvcOpeCause = _ConnPvcOpeCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 10),
    _ConnPvcOpeCause_Type()
)
connPvcOpeCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcOpeCause.setStatus("mandatory")


class _ConnPvcOpeLowFifoIndex_Type(Integer32):
    """Custom type connPvcOpeLowFifoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ConnPvcOpeLowFifoIndex_Type.__name__ = "Integer32"
_ConnPvcOpeLowFifoIndex_Object = MibScalar
connPvcOpeLowFifoIndex = _ConnPvcOpeLowFifoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 11),
    _ConnPvcOpeLowFifoIndex_Type()
)
connPvcOpeLowFifoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeLowFifoIndex.setStatus("mandatory")


class _ConnPvcOpeHighFifoIndex_Type(Integer32):
    """Custom type connPvcOpeHighFifoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ConnPvcOpeHighFifoIndex_Type.__name__ = "Integer32"
_ConnPvcOpeHighFifoIndex_Object = MibScalar
connPvcOpeHighFifoIndex = _ConnPvcOpeHighFifoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 12),
    _ConnPvcOpeHighFifoIndex_Type()
)
connPvcOpeHighFifoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeHighFifoIndex.setStatus("mandatory")


class _ConnPvcOpeLowParam1_Type(Integer32):
    """Custom type connPvcOpeLowParam1 based on Integer32"""
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
        *(("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("mode4", 5),
          ("mode5", 6),
          ("off", 1))
    )


_ConnPvcOpeLowParam1_Type.__name__ = "Integer32"
_ConnPvcOpeLowParam1_Object = MibScalar
connPvcOpeLowParam1 = _ConnPvcOpeLowParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 13),
    _ConnPvcOpeLowParam1_Type()
)
connPvcOpeLowParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeLowParam1.setStatus("mandatory")


class _ConnPvcOpeHighParam1_Type(Integer32):
    """Custom type connPvcOpeHighParam1 based on Integer32"""
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
        *(("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("mode4", 5),
          ("mode5", 6),
          ("off", 1))
    )


_ConnPvcOpeHighParam1_Type.__name__ = "Integer32"
_ConnPvcOpeHighParam1_Object = MibScalar
connPvcOpeHighParam1 = _ConnPvcOpeHighParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 14),
    _ConnPvcOpeHighParam1_Type()
)
connPvcOpeHighParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeHighParam1.setStatus("mandatory")


class _ConnPvcOpeLowParam2_Type(DisplayString):
    """Custom type connPvcOpeLowParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
        ValueSizeConstraint(0, 0),
    )


_ConnPvcOpeLowParam2_Type.__name__ = "DisplayString"
_ConnPvcOpeLowParam2_Object = MibScalar
connPvcOpeLowParam2 = _ConnPvcOpeLowParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 15),
    _ConnPvcOpeLowParam2_Type()
)
connPvcOpeLowParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeLowParam2.setStatus("mandatory")


class _ConnPvcOpeHighParam2_Type(DisplayString):
    """Custom type connPvcOpeHighParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
        ValueSizeConstraint(0, 0),
    )


_ConnPvcOpeHighParam2_Type.__name__ = "DisplayString"
_ConnPvcOpeHighParam2_Object = MibScalar
connPvcOpeHighParam2 = _ConnPvcOpeHighParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 1, 16),
    _ConnPvcOpeHighParam2_Type()
)
connPvcOpeHighParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcOpeHighParam2.setStatus("mandatory")
_ConnPvcTable_Object = MibTable
connPvcTable = _ConnPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2)
)
if mibBuilder.loadTexts:
    connPvcTable.setStatus("mandatory")
_ConnPvcEntry_Object = MibTableRow
connPvcEntry = _ConnPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1)
)
connPvcEntry.setIndexNames(
    (0, "NEC-MIB", "connPvcPort"),
    (0, "NEC-MIB", "connPvcVpi"),
    (0, "NEC-MIB", "connPvcVci"),
    (0, "NEC-MIB", "connPvcDirection"),
    (0, "NEC-MIB", "connPvcIndex"),
)
if mibBuilder.loadTexts:
    connPvcEntry.setStatus("mandatory")
_ConnPvcPort_Type = Integer32
_ConnPvcPort_Object = MibTableColumn
connPvcPort = _ConnPvcPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 1),
    _ConnPvcPort_Type()
)
connPvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcPort.setStatus("mandatory")
_ConnPvcVpi_Type = Integer32
_ConnPvcVpi_Object = MibTableColumn
connPvcVpi = _ConnPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 2),
    _ConnPvcVpi_Type()
)
connPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcVpi.setStatus("mandatory")
_ConnPvcVci_Type = Integer32
_ConnPvcVci_Object = MibTableColumn
connPvcVci = _ConnPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 3),
    _ConnPvcVci_Type()
)
connPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcVci.setStatus("mandatory")


class _ConnPvcDirection_Type(Integer32):
    """Custom type connPvcDirection based on Integer32"""
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
        *(("in", 1),
          ("in-out", 3),
          ("multi-in", 5),
          ("multi-out", 4),
          ("out", 2))
    )


_ConnPvcDirection_Type.__name__ = "Integer32"
_ConnPvcDirection_Object = MibTableColumn
connPvcDirection = _ConnPvcDirection_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 4),
    _ConnPvcDirection_Type()
)
connPvcDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcDirection.setStatus("mandatory")
_ConnPvcIndex_Type = Integer32
_ConnPvcIndex_Object = MibTableColumn
connPvcIndex = _ConnPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 5),
    _ConnPvcIndex_Type()
)
connPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcIndex.setStatus("mandatory")
_ConnPvcContrastPort_Type = Integer32
_ConnPvcContrastPort_Object = MibTableColumn
connPvcContrastPort = _ConnPvcContrastPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 6),
    _ConnPvcContrastPort_Type()
)
connPvcContrastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastPort.setStatus("mandatory")
_ConnPvcContrastVpi_Type = Integer32
_ConnPvcContrastVpi_Object = MibTableColumn
connPvcContrastVpi = _ConnPvcContrastVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 7),
    _ConnPvcContrastVpi_Type()
)
connPvcContrastVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastVpi.setStatus("mandatory")
_ConnPvcContrastVci_Type = Integer32
_ConnPvcContrastVci_Object = MibTableColumn
connPvcContrastVci = _ConnPvcContrastVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 8),
    _ConnPvcContrastVci_Type()
)
connPvcContrastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastVci.setStatus("mandatory")


class _ConnPvcTopology_Type(Integer32):
    """Custom type connPvcTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bi-directional-VCC", 2),
          ("bi-directional-VPC", 4),
          ("broadcast-VCC", 6),
          ("broadcast-VPC", 5),
          ("gateway", 7),
          ("uni-directional-VCC", 1),
          ("uni-directional-VPC", 3))
    )


_ConnPvcTopology_Type.__name__ = "Integer32"
_ConnPvcTopology_Object = MibTableColumn
connPvcTopology = _ConnPvcTopology_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 9),
    _ConnPvcTopology_Type()
)
connPvcTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTopology.setStatus("mandatory")


class _ConnPvcTrafficType_Type(Integer32):
    """Custom type connPvcTrafficType based on Integer32"""
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
        *(("traffic-ABR", 4),
          ("traffic-CBR", 1),
          ("traffic-UBR", 5),
          ("traffic-nrt-VBR", 3),
          ("traffic-rt-VBR", 2))
    )


_ConnPvcTrafficType_Type.__name__ = "Integer32"
_ConnPvcTrafficType_Object = MibTableColumn
connPvcTrafficType = _ConnPvcTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 10),
    _ConnPvcTrafficType_Type()
)
connPvcTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrafficType.setStatus("mandatory")


class _ConnPvcFifoIndex_Type(Integer32):
    """Custom type connPvcFifoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ConnPvcFifoIndex_Type.__name__ = "Integer32"
_ConnPvcFifoIndex_Object = MibTableColumn
connPvcFifoIndex = _ConnPvcFifoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 11),
    _ConnPvcFifoIndex_Type()
)
connPvcFifoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcFifoIndex.setStatus("mandatory")


class _ConnPvcContrastFifoIndex_Type(Integer32):
    """Custom type connPvcContrastFifoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ConnPvcContrastFifoIndex_Type.__name__ = "Integer32"
_ConnPvcContrastFifoIndex_Object = MibTableColumn
connPvcContrastFifoIndex = _ConnPvcContrastFifoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 12),
    _ConnPvcContrastFifoIndex_Type()
)
connPvcContrastFifoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastFifoIndex.setStatus("mandatory")


class _ConnPvcTrfConf_Type(Integer32):
    """Custom type connPvcTrfConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("entry", 1),
          ("remove", 2))
    )


_ConnPvcTrfConf_Type.__name__ = "Integer32"
_ConnPvcTrfConf_Object = MibTableColumn
connPvcTrfConf = _ConnPvcTrfConf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 13),
    _ConnPvcTrfConf_Type()
)
connPvcTrfConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcTrfConf.setStatus("mandatory")


class _ConnPvcTrfResult_Type(Integer32):
    """Custom type connPvcTrfResult based on Integer32"""
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
        *(("alreadyEntry", 3),
          ("entrySucceed", 2),
          ("notEntry", 6),
          ("other", 1),
          ("removeSucceed", 5),
          ("tableOverflow", 4))
    )


_ConnPvcTrfResult_Type.__name__ = "Integer32"
_ConnPvcTrfResult_Object = MibTableColumn
connPvcTrfResult = _ConnPvcTrfResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 14),
    _ConnPvcTrfResult_Type()
)
connPvcTrfResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfResult.setStatus("mandatory")


class _ConnPvcParam1_Type(Integer32):
    """Custom type connPvcParam1 based on Integer32"""
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
        *(("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("mode4", 5),
          ("mode5", 6),
          ("off", 1))
    )


_ConnPvcParam1_Type.__name__ = "Integer32"
_ConnPvcParam1_Object = MibTableColumn
connPvcParam1 = _ConnPvcParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 15),
    _ConnPvcParam1_Type()
)
connPvcParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcParam1.setStatus("mandatory")


class _ConnPvcContrastParam1_Type(Integer32):
    """Custom type connPvcContrastParam1 based on Integer32"""
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
        *(("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("mode4", 5),
          ("mode5", 6),
          ("off", 1))
    )


_ConnPvcContrastParam1_Type.__name__ = "Integer32"
_ConnPvcContrastParam1_Object = MibTableColumn
connPvcContrastParam1 = _ConnPvcContrastParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 16),
    _ConnPvcContrastParam1_Type()
)
connPvcContrastParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastParam1.setStatus("mandatory")


class _ConnPvcParam2_Type(DisplayString):
    """Custom type connPvcParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
        ValueSizeConstraint(0, 0),
    )


_ConnPvcParam2_Type.__name__ = "DisplayString"
_ConnPvcParam2_Object = MibTableColumn
connPvcParam2 = _ConnPvcParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 17),
    _ConnPvcParam2_Type()
)
connPvcParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcParam2.setStatus("mandatory")


class _ConnPvcContrastParam2_Type(DisplayString):
    """Custom type connPvcContrastParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
        ValueSizeConstraint(0, 0),
    )


_ConnPvcContrastParam2_Type.__name__ = "DisplayString"
_ConnPvcContrastParam2_Object = MibTableColumn
connPvcContrastParam2 = _ConnPvcContrastParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 18),
    _ConnPvcContrastParam2_Type()
)
connPvcContrastParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastParam2.setStatus("mandatory")
_ConnPvcParam3_Type = Integer32
_ConnPvcParam3_Object = MibTableColumn
connPvcParam3 = _ConnPvcParam3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 19),
    _ConnPvcParam3_Type()
)
connPvcParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcParam3.setStatus("mandatory")
_ConnPvcContrastParam3_Type = Integer32
_ConnPvcContrastParam3_Object = MibTableColumn
connPvcContrastParam3 = _ConnPvcContrastParam3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 20),
    _ConnPvcContrastParam3_Type()
)
connPvcContrastParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastParam3.setStatus("mandatory")
_ConnPvcParam4_Type = Integer32
_ConnPvcParam4_Object = MibTableColumn
connPvcParam4 = _ConnPvcParam4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 21),
    _ConnPvcParam4_Type()
)
connPvcParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcParam4.setStatus("mandatory")
_ConnPvcContrastParam4_Type = Integer32
_ConnPvcContrastParam4_Object = MibTableColumn
connPvcContrastParam4 = _ConnPvcContrastParam4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 22),
    _ConnPvcContrastParam4_Type()
)
connPvcContrastParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastParam4.setStatus("mandatory")
_ConnPvcParam5_Type = Integer32
_ConnPvcParam5_Object = MibTableColumn
connPvcParam5 = _ConnPvcParam5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 23),
    _ConnPvcParam5_Type()
)
connPvcParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcParam5.setStatus("mandatory")
_ConnPvcContrastParam5_Type = Integer32
_ConnPvcContrastParam5_Object = MibTableColumn
connPvcContrastParam5 = _ConnPvcContrastParam5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 24),
    _ConnPvcContrastParam5_Type()
)
connPvcContrastParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastParam5.setStatus("mandatory")


class _ConnPvcParam6_Type(Integer32):
    """Custom type connPvcParam6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ConnPvcParam6_Type.__name__ = "Integer32"
_ConnPvcParam6_Object = MibTableColumn
connPvcParam6 = _ConnPvcParam6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 25),
    _ConnPvcParam6_Type()
)
connPvcParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcParam6.setStatus("mandatory")


class _ConnPvcContrastParam6_Type(Integer32):
    """Custom type connPvcContrastParam6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ConnPvcContrastParam6_Type.__name__ = "Integer32"
_ConnPvcContrastParam6_Object = MibTableColumn
connPvcContrastParam6 = _ConnPvcContrastParam6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 26),
    _ConnPvcContrastParam6_Type()
)
connPvcContrastParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcContrastParam6.setStatus("mandatory")
_ConnPvcParam7_Type = Integer32
_ConnPvcParam7_Object = MibTableColumn
connPvcParam7 = _ConnPvcParam7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 27),
    _ConnPvcParam7_Type()
)
connPvcParam7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcParam7.setStatus("mandatory")
_ConnPvcContrastParam7_Type = Integer32
_ConnPvcContrastParam7_Object = MibTableColumn
connPvcContrastParam7 = _ConnPvcContrastParam7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 2, 1, 28),
    _ConnPvcContrastParam7_Type()
)
connPvcContrastParam7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connPvcContrastParam7.setStatus("mandatory")
_ConnPvcTrfTable_Object = MibTable
connPvcTrfTable = _ConnPvcTrfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3)
)
if mibBuilder.loadTexts:
    connPvcTrfTable.setStatus("mandatory")
_ConnPvcTrfEntry_Object = MibTableRow
connPvcTrfEntry = _ConnPvcTrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1)
)
connPvcTrfEntry.setIndexNames(
    (0, "NEC-MIB", "connPvcPort"),
    (0, "NEC-MIB", "connPvcVpi"),
    (0, "NEC-MIB", "connPvcVci"),
    (0, "NEC-MIB", "connPvcDirection"),
    (0, "NEC-MIB", "connPvcIndex"),
)
if mibBuilder.loadTexts:
    connPvcTrfEntry.setStatus("mandatory")
_ConnPvcTrfInCells_Type = OctetString
_ConnPvcTrfInCells_Object = MibTableColumn
connPvcTrfInCells = _ConnPvcTrfInCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1, 1),
    _ConnPvcTrfInCells_Type()
)
connPvcTrfInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfInCells.setStatus("mandatory")
_ConnPvcTrfInCellsCounters_Type = Counter32
_ConnPvcTrfInCellsCounters_Object = MibTableColumn
connPvcTrfInCellsCounters = _ConnPvcTrfInCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1, 2),
    _ConnPvcTrfInCellsCounters_Type()
)
connPvcTrfInCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfInCellsCounters.setStatus("mandatory")
_ConnPvcTrfOutCells_Type = OctetString
_ConnPvcTrfOutCells_Object = MibTableColumn
connPvcTrfOutCells = _ConnPvcTrfOutCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1, 3),
    _ConnPvcTrfOutCells_Type()
)
connPvcTrfOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfOutCells.setStatus("mandatory")
_ConnPvcTrfOutCellsCounters_Type = Counter32
_ConnPvcTrfOutCellsCounters_Object = MibTableColumn
connPvcTrfOutCellsCounters = _ConnPvcTrfOutCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1, 4),
    _ConnPvcTrfOutCellsCounters_Type()
)
connPvcTrfOutCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfOutCellsCounters.setStatus("mandatory")
_ConnPvcTrfInDropCells_Type = OctetString
_ConnPvcTrfInDropCells_Object = MibTableColumn
connPvcTrfInDropCells = _ConnPvcTrfInDropCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1, 5),
    _ConnPvcTrfInDropCells_Type()
)
connPvcTrfInDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfInDropCells.setStatus("mandatory")
_ConnPvcTrfInDropCellsCounters_Type = Counter32
_ConnPvcTrfInDropCellsCounters_Object = MibTableColumn
connPvcTrfInDropCellsCounters = _ConnPvcTrfInDropCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 1, 3, 1, 6),
    _ConnPvcTrfInDropCellsCounters_Type()
)
connPvcTrfInDropCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcTrfInDropCellsCounters.setStatus("mandatory")
_ConnConf_ObjectIdentity = ObjectIdentity
connConf = _ConnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2)
)
_ConnConfNode_ObjectIdentity = ObjectIdentity
connConfNode = _ConnConfNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1)
)


class _ConnConfNodePvcs_Type(Integer32):
    """Custom type connConfNodePvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_ConnConfNodePvcs_Type.__name__ = "Integer32"
_ConnConfNodePvcs_Object = MibScalar
connConfNodePvcs = _ConnConfNodePvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 1),
    _ConnConfNodePvcs_Type()
)
connConfNodePvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfNodePvcs.setStatus("mandatory")


class _ConnConfNodeSvcs_Type(Integer32):
    """Custom type connConfNodeSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConnConfNodeSvcs_Type.__name__ = "Integer32"
_ConnConfNodeSvcs_Object = MibScalar
connConfNodeSvcs = _ConnConfNodeSvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 2),
    _ConnConfNodeSvcs_Type()
)
connConfNodeSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfNodeSvcs.setStatus("mandatory")


class _ConnConfNodeSoftPvcs_Type(Integer32):
    """Custom type connConfNodeSoftPvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConnConfNodeSoftPvcs_Type.__name__ = "Integer32"
_ConnConfNodeSoftPvcs_Object = MibScalar
connConfNodeSoftPvcs = _ConnConfNodeSoftPvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 3),
    _ConnConfNodeSoftPvcs_Type()
)
connConfNodeSoftPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfNodeSoftPvcs.setStatus("mandatory")


class _ConnConfNodeTrafClear_Type(Integer32):
    """Custom type connConfNodeTrafClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allClear", 1),
          ("noOperation", 2))
    )


_ConnConfNodeTrafClear_Type.__name__ = "Integer32"
_ConnConfNodeTrafClear_Object = MibScalar
connConfNodeTrafClear = _ConnConfNodeTrafClear_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 4),
    _ConnConfNodeTrafClear_Type()
)
connConfNodeTrafClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connConfNodeTrafClear.setStatus("mandatory")


class _ConnConfNodeTrafs_Type(Integer32):
    """Custom type connConfNodeTrafs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ConnConfNodeTrafs_Type.__name__ = "Integer32"
_ConnConfNodeTrafs_Object = MibScalar
connConfNodeTrafs = _ConnConfNodeTrafs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 5),
    _ConnConfNodeTrafs_Type()
)
connConfNodeTrafs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfNodeTrafs.setStatus("mandatory")
_ConnConfNodeCompleteSvcs_Type = Counter32
_ConnConfNodeCompleteSvcs_Object = MibScalar
connConfNodeCompleteSvcs = _ConnConfNodeCompleteSvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 6),
    _ConnConfNodeCompleteSvcs_Type()
)
connConfNodeCompleteSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfNodeCompleteSvcs.setStatus("mandatory")
_ConnConfNodeUnCompleteSvcs_Type = Counter32
_ConnConfNodeUnCompleteSvcs_Object = MibScalar
connConfNodeUnCompleteSvcs = _ConnConfNodeUnCompleteSvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 1, 7),
    _ConnConfNodeUnCompleteSvcs_Type()
)
connConfNodeUnCompleteSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfNodeUnCompleteSvcs.setStatus("mandatory")
_ConnConfIfTable_Object = MibTable
connConfIfTable = _ConnConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 2)
)
if mibBuilder.loadTexts:
    connConfIfTable.setStatus("mandatory")
_ConnConfIfEntry_Object = MibTableRow
connConfIfEntry = _ConnConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 2, 1)
)
connConfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    connConfIfEntry.setStatus("mandatory")


class _ConnConfIfPvcs_Type(Integer32):
    """Custom type connConfIfPvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_ConnConfIfPvcs_Type.__name__ = "Integer32"
_ConnConfIfPvcs_Object = MibTableColumn
connConfIfPvcs = _ConnConfIfPvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 2, 1, 1),
    _ConnConfIfPvcs_Type()
)
connConfIfPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfIfPvcs.setStatus("mandatory")


class _ConnConfIfSvcs_Type(Integer32):
    """Custom type connConfIfSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConnConfIfSvcs_Type.__name__ = "Integer32"
_ConnConfIfSvcs_Object = MibTableColumn
connConfIfSvcs = _ConnConfIfSvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 2, 1, 2),
    _ConnConfIfSvcs_Type()
)
connConfIfSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfIfSvcs.setStatus("mandatory")


class _ConnConfIfSoftPvcs_Type(Integer32):
    """Custom type connConfIfSoftPvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ConnConfIfSoftPvcs_Type.__name__ = "Integer32"
_ConnConfIfSoftPvcs_Object = MibTableColumn
connConfIfSoftPvcs = _ConnConfIfSoftPvcs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 2, 2, 1, 3),
    _ConnConfIfSoftPvcs_Type()
)
connConfIfSoftPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConfIfSoftPvcs.setStatus("mandatory")
_ConnRoute_ObjectIdentity = ObjectIdentity
connRoute = _ConnRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3)
)
_ConnRouteOpe_ObjectIdentity = ObjectIdentity
connRouteOpe = _ConnRouteOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1)
)


class _ConnRouteOpeStatus_Type(Integer32):
    """Custom type connRouteOpeStatus based on Integer32"""
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
        *(("add", 2),
          ("allocate", 1),
          ("delete", 3),
          ("free", 4))
    )


_ConnRouteOpeStatus_Type.__name__ = "Integer32"
_ConnRouteOpeStatus_Object = MibScalar
connRouteOpeStatus = _ConnRouteOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 1),
    _ConnRouteOpeStatus_Type()
)
connRouteOpeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeStatus.setStatus("mandatory")
_ConnRouteOpeFailureCause_Type = ConnRouteOpeFailureCause
_ConnRouteOpeFailureCause_Object = MibScalar
connRouteOpeFailureCause = _ConnRouteOpeFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 2),
    _ConnRouteOpeFailureCause_Type()
)
connRouteOpeFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteOpeFailureCause.setStatus("mandatory")
_ConnRouteOpeAddressFormat_Type = DstAtmAddressFormat
_ConnRouteOpeAddressFormat_Object = MibScalar
connRouteOpeAddressFormat = _ConnRouteOpeAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 3),
    _ConnRouteOpeAddressFormat_Type()
)
connRouteOpeAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeAddressFormat.setStatus("mandatory")
_ConnRouteOpeAddressLength_Type = DstAtmAddressLength
_ConnRouteOpeAddressLength_Object = MibScalar
connRouteOpeAddressLength = _ConnRouteOpeAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 4),
    _ConnRouteOpeAddressLength_Type()
)
connRouteOpeAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeAddressLength.setStatus("mandatory")
_ConnRouteOpeAddress_Type = DstAtmAddress
_ConnRouteOpeAddress_Object = MibScalar
connRouteOpeAddress = _ConnRouteOpeAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 5),
    _ConnRouteOpeAddress_Type()
)
connRouteOpeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeAddress.setStatus("mandatory")
_ConnRouteOpePrimaryIfIndex_Type = DstPrimaryIfIndex
_ConnRouteOpePrimaryIfIndex_Object = MibScalar
connRouteOpePrimaryIfIndex = _ConnRouteOpePrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 6),
    _ConnRouteOpePrimaryIfIndex_Type()
)
connRouteOpePrimaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpePrimaryIfIndex.setStatus("mandatory")
_ConnRouteOpePrimaryVPI_Type = DstPrimaryVPI
_ConnRouteOpePrimaryVPI_Object = MibScalar
connRouteOpePrimaryVPI = _ConnRouteOpePrimaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 7),
    _ConnRouteOpePrimaryVPI_Type()
)
connRouteOpePrimaryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpePrimaryVPI.setStatus("mandatory")
_ConnRouteOpeSecondaryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteOpeSecondaryIfIndex_Object = MibScalar
connRouteOpeSecondaryIfIndex = _ConnRouteOpeSecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 8),
    _ConnRouteOpeSecondaryIfIndex_Type()
)
connRouteOpeSecondaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeSecondaryIfIndex.setStatus("mandatory")
_ConnRouteOpeSecondaryVPI_Type = DstSecondaryVPI
_ConnRouteOpeSecondaryVPI_Object = MibScalar
connRouteOpeSecondaryVPI = _ConnRouteOpeSecondaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 9),
    _ConnRouteOpeSecondaryVPI_Type()
)
connRouteOpeSecondaryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeSecondaryVPI.setStatus("mandatory")
_ConnRouteOpeTertiaryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteOpeTertiaryIfIndex_Object = MibScalar
connRouteOpeTertiaryIfIndex = _ConnRouteOpeTertiaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 10),
    _ConnRouteOpeTertiaryIfIndex_Type()
)
connRouteOpeTertiaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeTertiaryIfIndex.setStatus("mandatory")
_ConnRouteOpeTertiaryVPI_Type = DstSecondaryVPI
_ConnRouteOpeTertiaryVPI_Object = MibScalar
connRouteOpeTertiaryVPI = _ConnRouteOpeTertiaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 11),
    _ConnRouteOpeTertiaryVPI_Type()
)
connRouteOpeTertiaryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeTertiaryVPI.setStatus("mandatory")
_ConnRouteOpeFourthryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteOpeFourthryIfIndex_Object = MibScalar
connRouteOpeFourthryIfIndex = _ConnRouteOpeFourthryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 12),
    _ConnRouteOpeFourthryIfIndex_Type()
)
connRouteOpeFourthryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeFourthryIfIndex.setStatus("mandatory")
_ConnRouteOpeFourthryVPI_Type = DstSecondaryVPI
_ConnRouteOpeFourthryVPI_Object = MibScalar
connRouteOpeFourthryVPI = _ConnRouteOpeFourthryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 13),
    _ConnRouteOpeFourthryVPI_Type()
)
connRouteOpeFourthryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeFourthryVPI.setStatus("mandatory")
_ConnRouteOpeFifthryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteOpeFifthryIfIndex_Object = MibScalar
connRouteOpeFifthryIfIndex = _ConnRouteOpeFifthryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 14),
    _ConnRouteOpeFifthryIfIndex_Type()
)
connRouteOpeFifthryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeFifthryIfIndex.setStatus("mandatory")
_ConnRouteOpeFifthryVPI_Type = DstSecondaryVPI
_ConnRouteOpeFifthryVPI_Object = MibScalar
connRouteOpeFifthryVPI = _ConnRouteOpeFifthryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 15),
    _ConnRouteOpeFifthryVPI_Type()
)
connRouteOpeFifthryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeFifthryVPI.setStatus("mandatory")
_ConnRouteOpeSixthryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteOpeSixthryIfIndex_Object = MibScalar
connRouteOpeSixthryIfIndex = _ConnRouteOpeSixthryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 16),
    _ConnRouteOpeSixthryIfIndex_Type()
)
connRouteOpeSixthryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeSixthryIfIndex.setStatus("mandatory")
_ConnRouteOpeSixthryVPI_Type = DstSecondaryVPI
_ConnRouteOpeSixthryVPI_Object = MibScalar
connRouteOpeSixthryVPI = _ConnRouteOpeSixthryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 17),
    _ConnRouteOpeSixthryVPI_Type()
)
connRouteOpeSixthryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeSixthryVPI.setStatus("mandatory")
_ConnRouteOpeSeventhryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteOpeSeventhryIfIndex_Object = MibScalar
connRouteOpeSeventhryIfIndex = _ConnRouteOpeSeventhryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 18),
    _ConnRouteOpeSeventhryIfIndex_Type()
)
connRouteOpeSeventhryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeSeventhryIfIndex.setStatus("mandatory")
_ConnRouteOpeSeventhryVPI_Type = DstSecondaryVPI
_ConnRouteOpeSeventhryVPI_Object = MibScalar
connRouteOpeSeventhryVPI = _ConnRouteOpeSeventhryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 1, 19),
    _ConnRouteOpeSeventhryVPI_Type()
)
connRouteOpeSeventhryVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRouteOpeSeventhryVPI.setStatus("mandatory")
_ConnRouteTable_Object = MibTable
connRouteTable = _ConnRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2)
)
if mibBuilder.loadTexts:
    connRouteTable.setStatus("mandatory")
_ConnRouteEntry_Object = MibTableRow
connRouteEntry = _ConnRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1)
)
connRouteEntry.setIndexNames(
    (0, "NEC-MIB", "connRouteAtmAddressFormat"),
    (0, "NEC-MIB", "connRouteAtmAddressLength"),
    (0, "NEC-MIB", "connRouteAtmAddress"),
)
if mibBuilder.loadTexts:
    connRouteEntry.setStatus("mandatory")


class _ConnRouteType_Type(Integer32):
    """Custom type connRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ConnRouteType_Type.__name__ = "Integer32"
_ConnRouteType_Object = MibTableColumn
connRouteType = _ConnRouteType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 1),
    _ConnRouteType_Type()
)
connRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteType.setStatus("mandatory")
_ConnRoutePrimaryIfIndex_Type = DstPrimaryIfIndex
_ConnRoutePrimaryIfIndex_Object = MibTableColumn
connRoutePrimaryIfIndex = _ConnRoutePrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 2),
    _ConnRoutePrimaryIfIndex_Type()
)
connRoutePrimaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRoutePrimaryIfIndex.setStatus("mandatory")
_ConnRoutePrimaryVPI_Type = DstPrimaryVPI
_ConnRoutePrimaryVPI_Object = MibTableColumn
connRoutePrimaryVPI = _ConnRoutePrimaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 3),
    _ConnRoutePrimaryVPI_Type()
)
connRoutePrimaryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRoutePrimaryVPI.setStatus("mandatory")
_ConnRouteSecondaryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteSecondaryIfIndex_Object = MibTableColumn
connRouteSecondaryIfIndex = _ConnRouteSecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 4),
    _ConnRouteSecondaryIfIndex_Type()
)
connRouteSecondaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteSecondaryIfIndex.setStatus("mandatory")
_ConnRouteSecondaryVPI_Type = DstSecondaryVPI
_ConnRouteSecondaryVPI_Object = MibTableColumn
connRouteSecondaryVPI = _ConnRouteSecondaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 5),
    _ConnRouteSecondaryVPI_Type()
)
connRouteSecondaryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteSecondaryVPI.setStatus("mandatory")
_ConnRouteTertiaryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteTertiaryIfIndex_Object = MibTableColumn
connRouteTertiaryIfIndex = _ConnRouteTertiaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 6),
    _ConnRouteTertiaryIfIndex_Type()
)
connRouteTertiaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteTertiaryIfIndex.setStatus("mandatory")
_ConnRouteTertiaryVPI_Type = DstSecondaryVPI
_ConnRouteTertiaryVPI_Object = MibTableColumn
connRouteTertiaryVPI = _ConnRouteTertiaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 7),
    _ConnRouteTertiaryVPI_Type()
)
connRouteTertiaryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteTertiaryVPI.setStatus("mandatory")
_ConnRouteFourthryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteFourthryIfIndex_Object = MibTableColumn
connRouteFourthryIfIndex = _ConnRouteFourthryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 8),
    _ConnRouteFourthryIfIndex_Type()
)
connRouteFourthryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteFourthryIfIndex.setStatus("mandatory")
_ConnRouteFourthryVPI_Type = DstSecondaryVPI
_ConnRouteFourthryVPI_Object = MibTableColumn
connRouteFourthryVPI = _ConnRouteFourthryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 9),
    _ConnRouteFourthryVPI_Type()
)
connRouteFourthryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteFourthryVPI.setStatus("mandatory")
_ConnRouteFifthryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteFifthryIfIndex_Object = MibTableColumn
connRouteFifthryIfIndex = _ConnRouteFifthryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 10),
    _ConnRouteFifthryIfIndex_Type()
)
connRouteFifthryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteFifthryIfIndex.setStatus("mandatory")
_ConnRouteFifthryVPI_Type = DstSecondaryVPI
_ConnRouteFifthryVPI_Object = MibTableColumn
connRouteFifthryVPI = _ConnRouteFifthryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 11),
    _ConnRouteFifthryVPI_Type()
)
connRouteFifthryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteFifthryVPI.setStatus("mandatory")
_ConnRouteSixthryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteSixthryIfIndex_Object = MibTableColumn
connRouteSixthryIfIndex = _ConnRouteSixthryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 12),
    _ConnRouteSixthryIfIndex_Type()
)
connRouteSixthryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteSixthryIfIndex.setStatus("mandatory")
_ConnRouteSixthryVPI_Type = DstSecondaryVPI
_ConnRouteSixthryVPI_Object = MibTableColumn
connRouteSixthryVPI = _ConnRouteSixthryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 13),
    _ConnRouteSixthryVPI_Type()
)
connRouteSixthryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteSixthryVPI.setStatus("mandatory")
_ConnRouteSeventhryIfIndex_Type = DstSecondaryIfIndex
_ConnRouteSeventhryIfIndex_Object = MibTableColumn
connRouteSeventhryIfIndex = _ConnRouteSeventhryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 14),
    _ConnRouteSeventhryIfIndex_Type()
)
connRouteSeventhryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteSeventhryIfIndex.setStatus("mandatory")
_ConnRouteSeventhryVPI_Type = DstSecondaryVPI
_ConnRouteSeventhryVPI_Object = MibTableColumn
connRouteSeventhryVPI = _ConnRouteSeventhryVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 15),
    _ConnRouteSeventhryVPI_Type()
)
connRouteSeventhryVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteSeventhryVPI.setStatus("mandatory")


class _ConnRoutePrimaryStatus_Type(Integer32):
    """Custom type connRoutePrimaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ConnRoutePrimaryStatus_Type.__name__ = "Integer32"
_ConnRoutePrimaryStatus_Object = MibTableColumn
connRoutePrimaryStatus = _ConnRoutePrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 16),
    _ConnRoutePrimaryStatus_Type()
)
connRoutePrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRoutePrimaryStatus.setStatus("mandatory")


class _ConnRoutePrimaryCause_Type(Integer32):
    """Custom type connRoutePrimaryCause based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("lineInterface-Down", 4),
          ("lineInterface-Failure", 5),
          ("normal", 0),
          ("notInstalled", 99),
          ("other", 1),
          ("outOfService", 2),
          ("sw-Engine-Failure", 6),
          ("sw-Engine-SwapOUT", 7),
          ("testing", 3))
    )


_ConnRoutePrimaryCause_Type.__name__ = "Integer32"
_ConnRoutePrimaryCause_Object = MibTableColumn
connRoutePrimaryCause = _ConnRoutePrimaryCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 17),
    _ConnRoutePrimaryCause_Type()
)
connRoutePrimaryCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRoutePrimaryCause.setStatus("mandatory")
_ConnRouteAtmAddressFormat_Type = DstAtmAddressFormat
_ConnRouteAtmAddressFormat_Object = MibTableColumn
connRouteAtmAddressFormat = _ConnRouteAtmAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 18),
    _ConnRouteAtmAddressFormat_Type()
)
connRouteAtmAddressFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connRouteAtmAddressFormat.setStatus("mandatory")
_ConnRouteAtmAddressLength_Type = DstAtmAddressLength
_ConnRouteAtmAddressLength_Object = MibTableColumn
connRouteAtmAddressLength = _ConnRouteAtmAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 19),
    _ConnRouteAtmAddressLength_Type()
)
connRouteAtmAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connRouteAtmAddressLength.setStatus("mandatory")
_ConnRouteAtmAddress_Type = DstAtmAddress
_ConnRouteAtmAddress_Object = MibTableColumn
connRouteAtmAddress = _ConnRouteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 3, 2, 1, 20),
    _ConnRouteAtmAddress_Type()
)
connRouteAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connRouteAtmAddress.setStatus("mandatory")


class _ConnSoftPvcIndexNext_Type(Integer32):
    """Custom type connSoftPvcIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ConnSoftPvcIndexNext_Type.__name__ = "Integer32"
_ConnSoftPvcIndexNext_Object = MibScalar
connSoftPvcIndexNext = _ConnSoftPvcIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 4),
    _ConnSoftPvcIndexNext_Type()
)
connSoftPvcIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcIndexNext.setStatus("mandatory")
_ConnSoftPvcTable_Object = MibTable
connSoftPvcTable = _ConnSoftPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5)
)
if mibBuilder.loadTexts:
    connSoftPvcTable.setStatus("mandatory")
_ConnSoftPvcEntry_Object = MibTableRow
connSoftPvcEntry = _ConnSoftPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1)
)
connSoftPvcEntry.setIndexNames(
    (0, "NEC-MIB", "connSoftPvcIndex"),
)
if mibBuilder.loadTexts:
    connSoftPvcEntry.setStatus("mandatory")


class _ConnSoftPvcIndex_Type(Integer32):
    """Custom type connSoftPvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ConnSoftPvcIndex_Type.__name__ = "Integer32"
_ConnSoftPvcIndex_Object = MibTableColumn
connSoftPvcIndex = _ConnSoftPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 1),
    _ConnSoftPvcIndex_Type()
)
connSoftPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcIndex.setStatus("mandatory")


class _ConnSoftPvcTopology_Type(Integer32):
    """Custom type connSoftPvcTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bi-directional-VCC", 2),
          ("bi-directional-VPC", 4))
    )


_ConnSoftPvcTopology_Type.__name__ = "Integer32"
_ConnSoftPvcTopology_Object = MibTableColumn
connSoftPvcTopology = _ConnSoftPvcTopology_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 2),
    _ConnSoftPvcTopology_Type()
)
connSoftPvcTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcTopology.setStatus("mandatory")


class _ConnSoftPvcTrafficType_Type(Integer32):
    """Custom type connSoftPvcTrafficType based on Integer32"""
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
        *(("traffic-ABR", 4),
          ("traffic-CBR", 1),
          ("traffic-UBR", 5),
          ("traffic-nrt-VBR", 3),
          ("traffic-rt-VBR", 2))
    )


_ConnSoftPvcTrafficType_Type.__name__ = "Integer32"
_ConnSoftPvcTrafficType_Object = MibTableColumn
connSoftPvcTrafficType = _ConnSoftPvcTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 3),
    _ConnSoftPvcTrafficType_Type()
)
connSoftPvcTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcTrafficType.setStatus("mandatory")


class _ConnSoftPvcEndpointType_Type(Integer32):
    """Custom type connSoftPvcEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 2),
          ("calling", 1))
    )


_ConnSoftPvcEndpointType_Type.__name__ = "Integer32"
_ConnSoftPvcEndpointType_Object = MibTableColumn
connSoftPvcEndpointType = _ConnSoftPvcEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 4),
    _ConnSoftPvcEndpointType_Type()
)
connSoftPvcEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcEndpointType.setStatus("mandatory")


class _ConnSoftPvcRetry_Type(Integer32):
    """Custom type connSoftPvcRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(-1, -1),
    )


_ConnSoftPvcRetry_Type.__name__ = "Integer32"
_ConnSoftPvcRetry_Object = MibTableColumn
connSoftPvcRetry = _ConnSoftPvcRetry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 5),
    _ConnSoftPvcRetry_Type()
)
connSoftPvcRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcRetry.setStatus("mandatory")
_ConnSoftPvcSrcAtmAddressFormat_Type = ConnSoftPvcSrcAtmAddressFormat
_ConnSoftPvcSrcAtmAddressFormat_Object = MibTableColumn
connSoftPvcSrcAtmAddressFormat = _ConnSoftPvcSrcAtmAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 6),
    _ConnSoftPvcSrcAtmAddressFormat_Type()
)
connSoftPvcSrcAtmAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcAtmAddressFormat.setStatus("mandatory")


class _ConnSoftPvcSrcAtmAddressLength_Type(Integer32):
    """Custom type connSoftPvcSrcAtmAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 160),
        ValueRangeConstraint(-1, -1),
    )


_ConnSoftPvcSrcAtmAddressLength_Type.__name__ = "Integer32"
_ConnSoftPvcSrcAtmAddressLength_Object = MibTableColumn
connSoftPvcSrcAtmAddressLength = _ConnSoftPvcSrcAtmAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 7),
    _ConnSoftPvcSrcAtmAddressLength_Type()
)
connSoftPvcSrcAtmAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcAtmAddressLength.setStatus("mandatory")


class _ConnSoftPvcSrcAtmAddress_Type(OctetString):
    """Custom type connSoftPvcSrcAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnSoftPvcSrcAtmAddress_Type.__name__ = "OctetString"
_ConnSoftPvcSrcAtmAddress_Object = MibTableColumn
connSoftPvcSrcAtmAddress = _ConnSoftPvcSrcAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 8),
    _ConnSoftPvcSrcAtmAddress_Type()
)
connSoftPvcSrcAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcAtmAddress.setStatus("mandatory")


class _ConnSoftPvcSrcIfIndex_Type(Integer32):
    """Custom type connSoftPvcSrcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
        ValueRangeConstraint(-1, -1),
    )


_ConnSoftPvcSrcIfIndex_Type.__name__ = "Integer32"
_ConnSoftPvcSrcIfIndex_Object = MibTableColumn
connSoftPvcSrcIfIndex = _ConnSoftPvcSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 9),
    _ConnSoftPvcSrcIfIndex_Type()
)
connSoftPvcSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcIfIndex.setStatus("mandatory")
_ConnSoftPvcSrcVPI_Type = Integer32
_ConnSoftPvcSrcVPI_Object = MibTableColumn
connSoftPvcSrcVPI = _ConnSoftPvcSrcVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 10),
    _ConnSoftPvcSrcVPI_Type()
)
connSoftPvcSrcVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcVPI.setStatus("mandatory")
_ConnSoftPvcSrcVCI_Type = Integer32
_ConnSoftPvcSrcVCI_Object = MibTableColumn
connSoftPvcSrcVCI = _ConnSoftPvcSrcVCI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 11),
    _ConnSoftPvcSrcVCI_Type()
)
connSoftPvcSrcVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcVCI.setStatus("mandatory")
_ConnSoftPvcDstAtmAddressFormat_Type = ConnSoftPvcDstAtmAddressFormat
_ConnSoftPvcDstAtmAddressFormat_Object = MibTableColumn
connSoftPvcDstAtmAddressFormat = _ConnSoftPvcDstAtmAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 12),
    _ConnSoftPvcDstAtmAddressFormat_Type()
)
connSoftPvcDstAtmAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstAtmAddressFormat.setStatus("mandatory")


class _ConnSoftPvcDstAtmAddressLength_Type(Integer32):
    """Custom type connSoftPvcDstAtmAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 160),
        ValueRangeConstraint(-1, -1),
    )


_ConnSoftPvcDstAtmAddressLength_Type.__name__ = "Integer32"
_ConnSoftPvcDstAtmAddressLength_Object = MibTableColumn
connSoftPvcDstAtmAddressLength = _ConnSoftPvcDstAtmAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 13),
    _ConnSoftPvcDstAtmAddressLength_Type()
)
connSoftPvcDstAtmAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstAtmAddressLength.setStatus("mandatory")


class _ConnSoftPvcDstAtmAddress_Type(OctetString):
    """Custom type connSoftPvcDstAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnSoftPvcDstAtmAddress_Type.__name__ = "OctetString"
_ConnSoftPvcDstAtmAddress_Object = MibTableColumn
connSoftPvcDstAtmAddress = _ConnSoftPvcDstAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 14),
    _ConnSoftPvcDstAtmAddress_Type()
)
connSoftPvcDstAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstAtmAddress.setStatus("mandatory")


class _ConnSoftPvcDstIfIndex_Type(Integer32):
    """Custom type connSoftPvcDstIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
        ValueRangeConstraint(-1, -1),
    )


_ConnSoftPvcDstIfIndex_Type.__name__ = "Integer32"
_ConnSoftPvcDstIfIndex_Object = MibTableColumn
connSoftPvcDstIfIndex = _ConnSoftPvcDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 15),
    _ConnSoftPvcDstIfIndex_Type()
)
connSoftPvcDstIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstIfIndex.setStatus("mandatory")
_ConnSoftPvcDstVPI_Type = Integer32
_ConnSoftPvcDstVPI_Object = MibTableColumn
connSoftPvcDstVPI = _ConnSoftPvcDstVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 16),
    _ConnSoftPvcDstVPI_Type()
)
connSoftPvcDstVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstVPI.setStatus("mandatory")
_ConnSoftPvcDstVCI_Type = Integer32
_ConnSoftPvcDstVCI_Object = MibTableColumn
connSoftPvcDstVCI = _ConnSoftPvcDstVCI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 17),
    _ConnSoftPvcDstVCI_Type()
)
connSoftPvcDstVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstVCI.setStatus("mandatory")


class _ConnSoftPvcRowStatus_Type(Integer32):
    """Custom type connSoftPvcRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConnSoftPvcRowStatus_Type.__name__ = "Integer32"
_ConnSoftPvcRowStatus_Object = MibTableColumn
connSoftPvcRowStatus = _ConnSoftPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 18),
    _ConnSoftPvcRowStatus_Type()
)
connSoftPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcRowStatus.setStatus("mandatory")


class _ConnSoftPvcCause_Type(Integer32):
    """Custom type connSoftPvcCause based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("dataTableFull", 7),
          ("diagnostics", 17),
          ("illegalDstFileName", 12),
          ("illegalOperation", 15),
          ("illegalSrcFileName", 11),
          ("illegalSrcRateForUPC", 19),
          ("illegalSrcShaper", 14),
          ("inconsistentVPVC", 8),
          ("insusfficientPCRofProfile", 25),
          ("lineDiagnosis", 9),
          ("lineOutOfOrder", 13),
          ("missMatchTrfType", 10),
          ("missMatchTrfTypeSrcShaperForGateway", 24),
          ("noCevc", 20),
          ("noDlci", 21),
          ("noPvcSrcShaperForGateway", 23),
          ("noSrcShaperForGateway", 22),
          ("otherFailure", 18),
          ("parameterIsNotEnough", 16),
          ("rateDstOverFlow", 6),
          ("rateSrcOverFlow", 5),
          ("rowExisting", 1),
          ("vpivciDstBusy", 3),
          ("vpivciOutOfRange", 4),
          ("vpivciSrcBusy", 2))
    )


_ConnSoftPvcCause_Type.__name__ = "Integer32"
_ConnSoftPvcCause_Object = MibTableColumn
connSoftPvcCause = _ConnSoftPvcCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 19),
    _ConnSoftPvcCause_Type()
)
connSoftPvcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcCause.setStatus("mandatory")


class _ConnSoftPvcRestRetry_Type(Integer32):
    """Custom type connSoftPvcRestRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(-1, -1),
    )


_ConnSoftPvcRestRetry_Type.__name__ = "Integer32"
_ConnSoftPvcRestRetry_Object = MibTableColumn
connSoftPvcRestRetry = _ConnSoftPvcRestRetry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 20),
    _ConnSoftPvcRestRetry_Type()
)
connSoftPvcRestRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcRestRetry.setStatus("mandatory")


class _ConnSoftPvcSrcFifoIndex_Type(Integer32):
    """Custom type connSoftPvcSrcFifoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ConnSoftPvcSrcFifoIndex_Type.__name__ = "Integer32"
_ConnSoftPvcSrcFifoIndex_Object = MibTableColumn
connSoftPvcSrcFifoIndex = _ConnSoftPvcSrcFifoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 21),
    _ConnSoftPvcSrcFifoIndex_Type()
)
connSoftPvcSrcFifoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcFifoIndex.setStatus("mandatory")


class _ConnSoftPvcDstFifoIndex_Type(Integer32):
    """Custom type connSoftPvcDstFifoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ConnSoftPvcDstFifoIndex_Type.__name__ = "Integer32"
_ConnSoftPvcDstFifoIndex_Object = MibTableColumn
connSoftPvcDstFifoIndex = _ConnSoftPvcDstFifoIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 22),
    _ConnSoftPvcDstFifoIndex_Type()
)
connSoftPvcDstFifoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstFifoIndex.setStatus("mandatory")


class _ConnSoftPvcNodeKind_Type(Integer32):
    """Custom type connSoftPvcNodeKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("model5", 1),
          ("model5E", 3),
          ("model7", 2))
    )


_ConnSoftPvcNodeKind_Type.__name__ = "Integer32"
_ConnSoftPvcNodeKind_Object = MibTableColumn
connSoftPvcNodeKind = _ConnSoftPvcNodeKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 23),
    _ConnSoftPvcNodeKind_Type()
)
connSoftPvcNodeKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcNodeKind.setStatus("mandatory")


class _ConnSoftPvcSrcParam1_Type(Integer32):
    """Custom type connSoftPvcSrcParam1 based on Integer32"""
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
        *(("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("mode4", 5),
          ("mode5", 6),
          ("off", 1))
    )


_ConnSoftPvcSrcParam1_Type.__name__ = "Integer32"
_ConnSoftPvcSrcParam1_Object = MibTableColumn
connSoftPvcSrcParam1 = _ConnSoftPvcSrcParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 24),
    _ConnSoftPvcSrcParam1_Type()
)
connSoftPvcSrcParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam1.setStatus("mandatory")


class _ConnSoftPvcDstParam1_Type(Integer32):
    """Custom type connSoftPvcDstParam1 based on Integer32"""
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
        *(("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("mode4", 5),
          ("mode5", 6),
          ("off", 1))
    )


_ConnSoftPvcDstParam1_Type.__name__ = "Integer32"
_ConnSoftPvcDstParam1_Object = MibTableColumn
connSoftPvcDstParam1 = _ConnSoftPvcDstParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 25),
    _ConnSoftPvcDstParam1_Type()
)
connSoftPvcDstParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstParam1.setStatus("mandatory")


class _ConnSoftPvcSrcParam2_Type(DisplayString):
    """Custom type connSoftPvcSrcParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
        ValueSizeConstraint(0, 0),
    )


_ConnSoftPvcSrcParam2_Type.__name__ = "DisplayString"
_ConnSoftPvcSrcParam2_Object = MibTableColumn
connSoftPvcSrcParam2 = _ConnSoftPvcSrcParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 26),
    _ConnSoftPvcSrcParam2_Type()
)
connSoftPvcSrcParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam2.setStatus("mandatory")


class _ConnSoftPvcDstParam2_Type(DisplayString):
    """Custom type connSoftPvcDstParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
        ValueSizeConstraint(0, 0),
    )


_ConnSoftPvcDstParam2_Type.__name__ = "DisplayString"
_ConnSoftPvcDstParam2_Object = MibTableColumn
connSoftPvcDstParam2 = _ConnSoftPvcDstParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 27),
    _ConnSoftPvcDstParam2_Type()
)
connSoftPvcDstParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connSoftPvcDstParam2.setStatus("mandatory")
_ConnSoftPvcSrcParam3_Type = Integer32
_ConnSoftPvcSrcParam3_Object = MibTableColumn
connSoftPvcSrcParam3 = _ConnSoftPvcSrcParam3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 28),
    _ConnSoftPvcSrcParam3_Type()
)
connSoftPvcSrcParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam3.setStatus("mandatory")
_ConnSoftPvcDstParam3_Type = Integer32
_ConnSoftPvcDstParam3_Object = MibTableColumn
connSoftPvcDstParam3 = _ConnSoftPvcDstParam3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 29),
    _ConnSoftPvcDstParam3_Type()
)
connSoftPvcDstParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcDstParam3.setStatus("mandatory")
_ConnSoftPvcSrcParam4_Type = Integer32
_ConnSoftPvcSrcParam4_Object = MibTableColumn
connSoftPvcSrcParam4 = _ConnSoftPvcSrcParam4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 30),
    _ConnSoftPvcSrcParam4_Type()
)
connSoftPvcSrcParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam4.setStatus("mandatory")
_ConnSoftPvcDstParam4_Type = Integer32
_ConnSoftPvcDstParam4_Object = MibTableColumn
connSoftPvcDstParam4 = _ConnSoftPvcDstParam4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 31),
    _ConnSoftPvcDstParam4_Type()
)
connSoftPvcDstParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcDstParam4.setStatus("mandatory")
_ConnSoftPvcSrcParam5_Type = Integer32
_ConnSoftPvcSrcParam5_Object = MibTableColumn
connSoftPvcSrcParam5 = _ConnSoftPvcSrcParam5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 32),
    _ConnSoftPvcSrcParam5_Type()
)
connSoftPvcSrcParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam5.setStatus("mandatory")
_ConnSoftPvcDstParam5_Type = Integer32
_ConnSoftPvcDstParam5_Object = MibTableColumn
connSoftPvcDstParam5 = _ConnSoftPvcDstParam5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 33),
    _ConnSoftPvcDstParam5_Type()
)
connSoftPvcDstParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcDstParam5.setStatus("mandatory")


class _ConnSoftPvcSrcParam6_Type(Integer32):
    """Custom type connSoftPvcSrcParam6 based on Integer32"""
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


_ConnSoftPvcSrcParam6_Type.__name__ = "Integer32"
_ConnSoftPvcSrcParam6_Object = MibTableColumn
connSoftPvcSrcParam6 = _ConnSoftPvcSrcParam6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 34),
    _ConnSoftPvcSrcParam6_Type()
)
connSoftPvcSrcParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam6.setStatus("mandatory")


class _ConnSoftPvcDstParam6_Type(Integer32):
    """Custom type connSoftPvcDstParam6 based on Integer32"""
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


_ConnSoftPvcDstParam6_Type.__name__ = "Integer32"
_ConnSoftPvcDstParam6_Object = MibTableColumn
connSoftPvcDstParam6 = _ConnSoftPvcDstParam6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 35),
    _ConnSoftPvcDstParam6_Type()
)
connSoftPvcDstParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcDstParam6.setStatus("mandatory")
_ConnSoftPvcSrcParam7_Type = Integer32
_ConnSoftPvcSrcParam7_Object = MibTableColumn
connSoftPvcSrcParam7 = _ConnSoftPvcSrcParam7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 36),
    _ConnSoftPvcSrcParam7_Type()
)
connSoftPvcSrcParam7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connSoftPvcSrcParam7.setStatus("mandatory")
_ConnSoftPvcDstParam7_Type = Integer32
_ConnSoftPvcDstParam7_Object = MibTableColumn
connSoftPvcDstParam7 = _ConnSoftPvcDstParam7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 5, 1, 37),
    _ConnSoftPvcDstParam7_Type()
)
connSoftPvcDstParam7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connSoftPvcDstParam7.setStatus("mandatory")
_ConnSoftPvcEstablishedSrcInfTable_Object = MibTable
connSoftPvcEstablishedSrcInfTable = _ConnSoftPvcEstablishedSrcInfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 6)
)
if mibBuilder.loadTexts:
    connSoftPvcEstablishedSrcInfTable.setStatus("mandatory")
_ConnSoftPvcEstablishedSrcInfEntry_Object = MibTableRow
connSoftPvcEstablishedSrcInfEntry = _ConnSoftPvcEstablishedSrcInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 6, 1)
)
connSoftPvcEstablishedSrcInfEntry.setIndexNames(
    (0, "NEC-MIB", "connSoftPvcEstSrcInfIndex"),
)
if mibBuilder.loadTexts:
    connSoftPvcEstablishedSrcInfEntry.setStatus("mandatory")
_ConnSoftPvcEstablishedSrcInf_Type = Opaque
_ConnSoftPvcEstablishedSrcInf_Object = MibTableColumn
connSoftPvcEstablishedSrcInf = _ConnSoftPvcEstablishedSrcInf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 6, 1, 1),
    _ConnSoftPvcEstablishedSrcInf_Type()
)
connSoftPvcEstablishedSrcInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSoftPvcEstablishedSrcInf.setStatus("mandatory")
_ConnSoftPvcEstSrcInfIndex_Type = ConnSoftPvcEstSrcInfIndex
_ConnSoftPvcEstSrcInfIndex_Object = MibTableColumn
connSoftPvcEstSrcInfIndex = _ConnSoftPvcEstSrcInfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 6, 1, 2),
    _ConnSoftPvcEstSrcInfIndex_Type()
)
connSoftPvcEstSrcInfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connSoftPvcEstSrcInfIndex.setStatus("mandatory")
_ConnOam_ObjectIdentity = ObjectIdentity
connOam = _ConnOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7)
)
_ConnOamOpe_ObjectIdentity = ObjectIdentity
connOamOpe = _ConnOamOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1)
)


class _ConnOamOpeStatus_Type(Integer32):
    """Custom type connOamOpeStatus based on Integer32"""
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
        *(("add", 2),
          ("allocate", 1),
          ("delete", 3),
          ("free", 4))
    )


_ConnOamOpeStatus_Type.__name__ = "Integer32"
_ConnOamOpeStatus_Object = MibScalar
connOamOpeStatus = _ConnOamOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 1),
    _ConnOamOpeStatus_Type()
)
connOamOpeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeStatus.setStatus("mandatory")


class _ConnOamOpeCause_Type(Integer32):
    """Custom type connOamOpeCause based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("alreadyRegistered", 12),
          ("illegalMode", 6),
          ("illegalPoint", 5),
          ("illegalPort", 8),
          ("illegalSection", 7),
          ("illegalVpiVci", 9),
          ("invalidBufferType", 10),
          ("noSuchConnection", 11),
          ("notExisting", 13),
          ("other", 1),
          ("parameterIsNotEnough", 3),
          ("succeed", 2),
          ("tableIsFull", 4))
    )


_ConnOamOpeCause_Type.__name__ = "Integer32"
_ConnOamOpeCause_Object = MibScalar
connOamOpeCause = _ConnOamOpeCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 2),
    _ConnOamOpeCause_Type()
)
connOamOpeCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamOpeCause.setStatus("mandatory")


class _ConnOamOpePoint_Type(Integer32):
    """Custom type connOamOpePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connecting-point", 2),
          ("end-point", 1))
    )


_ConnOamOpePoint_Type.__name__ = "Integer32"
_ConnOamOpePoint_Object = MibScalar
connOamOpePoint = _ConnOamOpePoint_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 3),
    _ConnOamOpePoint_Type()
)
connOamOpePoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpePoint.setStatus("mandatory")


class _ConnOamOpeMode_Type(Integer32):
    """Custom type connOamOpeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f4", 1),
          ("f5", 2))
    )


_ConnOamOpeMode_Type.__name__ = "Integer32"
_ConnOamOpeMode_Object = MibScalar
connOamOpeMode = _ConnOamOpeMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 4),
    _ConnOamOpeMode_Type()
)
connOamOpeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeMode.setStatus("mandatory")


class _ConnOamOpeSection_Type(Integer32):
    """Custom type connOamOpeSection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end-to-end", 2),
          ("segment", 1))
    )


_ConnOamOpeSection_Type.__name__ = "Integer32"
_ConnOamOpeSection_Object = MibScalar
connOamOpeSection = _ConnOamOpeSection_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 5),
    _ConnOamOpeSection_Type()
)
connOamOpeSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeSection.setStatus("mandatory")
_ConnOamOpePort1_Type = Integer32
_ConnOamOpePort1_Object = MibScalar
connOamOpePort1 = _ConnOamOpePort1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 6),
    _ConnOamOpePort1_Type()
)
connOamOpePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpePort1.setStatus("mandatory")
_ConnOamOpePort2_Type = Integer32
_ConnOamOpePort2_Object = MibScalar
connOamOpePort2 = _ConnOamOpePort2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 7),
    _ConnOamOpePort2_Type()
)
connOamOpePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpePort2.setStatus("mandatory")
_ConnOamOpeVpi1_Type = Integer32
_ConnOamOpeVpi1_Object = MibScalar
connOamOpeVpi1 = _ConnOamOpeVpi1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 8),
    _ConnOamOpeVpi1_Type()
)
connOamOpeVpi1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeVpi1.setStatus("mandatory")
_ConnOamOpeVpi2_Type = Integer32
_ConnOamOpeVpi2_Object = MibScalar
connOamOpeVpi2 = _ConnOamOpeVpi2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 9),
    _ConnOamOpeVpi2_Type()
)
connOamOpeVpi2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeVpi2.setStatus("mandatory")
_ConnOamOpeVci1_Type = Integer32
_ConnOamOpeVci1_Object = MibScalar
connOamOpeVci1 = _ConnOamOpeVci1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 10),
    _ConnOamOpeVci1_Type()
)
connOamOpeVci1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeVci1.setStatus("mandatory")
_ConnOamOpeVci2_Type = Integer32
_ConnOamOpeVci2_Object = MibScalar
connOamOpeVci2 = _ConnOamOpeVci2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 1, 11),
    _ConnOamOpeVci2_Type()
)
connOamOpeVci2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connOamOpeVci2.setStatus("mandatory")
_ConnOamTable_Object = MibTable
connOamTable = _ConnOamTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2)
)
if mibBuilder.loadTexts:
    connOamTable.setStatus("mandatory")
_ConnOamEntry_Object = MibTableRow
connOamEntry = _ConnOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1)
)
connOamEntry.setIndexNames(
    (0, "NEC-MIB", "connOamPort"),
    (0, "NEC-MIB", "connOamIndex"),
)
if mibBuilder.loadTexts:
    connOamEntry.setStatus("mandatory")
_ConnOamPort_Type = Integer32
_ConnOamPort_Object = MibTableColumn
connOamPort = _ConnOamPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 1),
    _ConnOamPort_Type()
)
connOamPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connOamPort.setStatus("mandatory")


class _ConnOamIndex_Type(Integer32):
    """Custom type connOamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 144),
    )


_ConnOamIndex_Type.__name__ = "Integer32"
_ConnOamIndex_Object = MibTableColumn
connOamIndex = _ConnOamIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 2),
    _ConnOamIndex_Type()
)
connOamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connOamIndex.setStatus("mandatory")
_ConnOamContrastPort_Type = Integer32
_ConnOamContrastPort_Object = MibTableColumn
connOamContrastPort = _ConnOamContrastPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 3),
    _ConnOamContrastPort_Type()
)
connOamContrastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamContrastPort.setStatus("mandatory")
_ConnOamVpi_Type = Integer32
_ConnOamVpi_Object = MibTableColumn
connOamVpi = _ConnOamVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 4),
    _ConnOamVpi_Type()
)
connOamVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamVpi.setStatus("mandatory")
_ConnOamContrastVpi_Type = Integer32
_ConnOamContrastVpi_Object = MibTableColumn
connOamContrastVpi = _ConnOamContrastVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 5),
    _ConnOamContrastVpi_Type()
)
connOamContrastVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamContrastVpi.setStatus("mandatory")
_ConnOamVci_Type = Integer32
_ConnOamVci_Object = MibTableColumn
connOamVci = _ConnOamVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 6),
    _ConnOamVci_Type()
)
connOamVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamVci.setStatus("mandatory")
_ConnOamContrastVci_Type = Integer32
_ConnOamContrastVci_Object = MibTableColumn
connOamContrastVci = _ConnOamContrastVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 7),
    _ConnOamContrastVci_Type()
)
connOamContrastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamContrastVci.setStatus("mandatory")


class _ConnOamPoint_Type(Integer32):
    """Custom type connOamPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connecting-point", 2),
          ("end-point", 1))
    )


_ConnOamPoint_Type.__name__ = "Integer32"
_ConnOamPoint_Object = MibTableColumn
connOamPoint = _ConnOamPoint_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 8),
    _ConnOamPoint_Type()
)
connOamPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamPoint.setStatus("mandatory")


class _ConnOamMode_Type(Integer32):
    """Custom type connOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f4", 1),
          ("f5", 2))
    )


_ConnOamMode_Type.__name__ = "Integer32"
_ConnOamMode_Object = MibTableColumn
connOamMode = _ConnOamMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 9),
    _ConnOamMode_Type()
)
connOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamMode.setStatus("mandatory")


class _ConnOamSection_Type(Integer32):
    """Custom type connOamSection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end-to-end", 2),
          ("segment", 1))
    )


_ConnOamSection_Type.__name__ = "Integer32"
_ConnOamSection_Object = MibTableColumn
connOamSection = _ConnOamSection_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 10),
    _ConnOamSection_Type()
)
connOamSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamSection.setStatus("mandatory")


class _ConnOamStatus_Type(Integer32):
    """Custom type connOamStatus based on Integer32"""
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
        *(("failure", 5),
          ("normal", 2),
          ("other", 1),
          ("receive-AIS", 3),
          ("receive-RDI", 4))
    )


_ConnOamStatus_Type.__name__ = "Integer32"
_ConnOamStatus_Object = MibTableColumn
connOamStatus = _ConnOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 11),
    _ConnOamStatus_Type()
)
connOamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamStatus.setStatus("mandatory")


class _ConnOamDefectType_Type(Integer32):
    """Custom type connOamDefectType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("ais", 10),
          ("ais-path", 5),
          ("ais-section", 6),
          ("idle", 14),
          ("loc", 4),
          ("lof", 3),
          ("lop", 9),
          ("los", 2),
          ("normal", 1),
          ("oof", 13),
          ("payload-all-one", 11),
          ("plcp-lof", 17),
          ("plcp-oof", 16),
          ("plcp-yellow", 18),
          ("rai", 12),
          ("rdi", 15),
          ("red", 19),
          ("yellow-path", 8),
          ("yellow-section", 7))
    )


_ConnOamDefectType_Type.__name__ = "Integer32"
_ConnOamDefectType_Object = MibTableColumn
connOamDefectType = _ConnOamDefectType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 12),
    _ConnOamDefectType_Type()
)
connOamDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamDefectType.setStatus("mandatory")


class _ConnOamDefectNodeID_Type(OctetString):
    """Custom type connOamDefectNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ConnOamDefectNodeID_Type.__name__ = "OctetString"
_ConnOamDefectNodeID_Object = MibTableColumn
connOamDefectNodeID = _ConnOamDefectNodeID_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 7, 2, 1, 13),
    _ConnOamDefectNodeID_Type()
)
connOamDefectNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOamDefectNodeID.setStatus("mandatory")
_ConnLoop_ObjectIdentity = ObjectIdentity
connLoop = _ConnLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8)
)
_ConnLoopOpe_ObjectIdentity = ObjectIdentity
connLoopOpe = _ConnLoopOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1)
)


class _ConnLoopOpeStatus_Type(Integer32):
    """Custom type connLoopOpeStatus based on Integer32"""
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
        *(("action", 2),
          ("allocate", 1),
          ("endtest", 3),
          ("free", 4))
    )


_ConnLoopOpeStatus_Type.__name__ = "Integer32"
_ConnLoopOpeStatus_Object = MibScalar
connLoopOpeStatus = _ConnLoopOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 1),
    _ConnLoopOpeStatus_Type()
)
connLoopOpeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeStatus.setStatus("mandatory")


class _ConnLoopOpeCause_Type(Integer32):
    """Custom type connLoopOpeCause based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("admindown", 6),
          ("execute", 12),
          ("lineLoopback", 9),
          ("noneBuffer2", 8),
          ("noneLoopBackId", 11),
          ("nonePkg", 7),
          ("other", 3),
          ("parameterFailed", 5),
          ("resetSlot", 10),
          ("succeed", 1),
          ("vpivciOutOfRange", 4))
    )


_ConnLoopOpeCause_Type.__name__ = "Integer32"
_ConnLoopOpeCause_Object = MibScalar
connLoopOpeCause = _ConnLoopOpeCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 2),
    _ConnLoopOpeCause_Type()
)
connLoopOpeCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLoopOpeCause.setStatus("mandatory")


class _ConnLoopOpeMode_Type(Integer32):
    """Custom type connLoopOpeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f4", 1),
          ("f5", 2))
    )


_ConnLoopOpeMode_Type.__name__ = "Integer32"
_ConnLoopOpeMode_Object = MibScalar
connLoopOpeMode = _ConnLoopOpeMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 3),
    _ConnLoopOpeMode_Type()
)
connLoopOpeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeMode.setStatus("mandatory")


class _ConnLoopOpeBase_Type(Integer32):
    """Custom type connLoopOpeBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end-end", 2),
          ("segment", 1))
    )


_ConnLoopOpeBase_Type.__name__ = "Integer32"
_ConnLoopOpeBase_Object = MibScalar
connLoopOpeBase = _ConnLoopOpeBase_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 4),
    _ConnLoopOpeBase_Type()
)
connLoopOpeBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeBase.setStatus("mandatory")


class _ConnLoopOpeLoopBackPointNodeId_Type(OctetString):
    """Custom type connLoopOpeLoopBackPointNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnLoopOpeLoopBackPointNodeId_Type.__name__ = "OctetString"
_ConnLoopOpeLoopBackPointNodeId_Object = MibScalar
connLoopOpeLoopBackPointNodeId = _ConnLoopOpeLoopBackPointNodeId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 5),
    _ConnLoopOpeLoopBackPointNodeId_Type()
)
connLoopOpeLoopBackPointNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeLoopBackPointNodeId.setStatus("mandatory")


class _ConnLoopOpeCorrelationTag_Type(OctetString):
    """Custom type connLoopOpeCorrelationTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ConnLoopOpeCorrelationTag_Type.__name__ = "OctetString"
_ConnLoopOpeCorrelationTag_Object = MibScalar
connLoopOpeCorrelationTag = _ConnLoopOpeCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 6),
    _ConnLoopOpeCorrelationTag_Type()
)
connLoopOpeCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeCorrelationTag.setStatus("mandatory")


class _ConnLoopOpeCount_Type(Integer32):
    """Custom type connLoopOpeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ConnLoopOpeCount_Type.__name__ = "Integer32"
_ConnLoopOpeCount_Object = MibScalar
connLoopOpeCount = _ConnLoopOpeCount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 7),
    _ConnLoopOpeCount_Type()
)
connLoopOpeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeCount.setStatus("mandatory")
_ConnLoopOpePort_Type = Integer32
_ConnLoopOpePort_Object = MibScalar
connLoopOpePort = _ConnLoopOpePort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 8),
    _ConnLoopOpePort_Type()
)
connLoopOpePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpePort.setStatus("mandatory")
_ConnLoopOpeVpi_Type = Integer32
_ConnLoopOpeVpi_Object = MibScalar
connLoopOpeVpi = _ConnLoopOpeVpi_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 9),
    _ConnLoopOpeVpi_Type()
)
connLoopOpeVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeVpi.setStatus("mandatory")
_ConnLoopOpeVci_Type = Integer32
_ConnLoopOpeVci_Object = MibScalar
connLoopOpeVci = _ConnLoopOpeVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 10),
    _ConnLoopOpeVci_Type()
)
connLoopOpeVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeVci.setStatus("mandatory")
_ConnLoopOpeNormalEndCount_Type = Integer32
_ConnLoopOpeNormalEndCount_Object = MibScalar
connLoopOpeNormalEndCount = _ConnLoopOpeNormalEndCount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 11),
    _ConnLoopOpeNormalEndCount_Type()
)
connLoopOpeNormalEndCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLoopOpeNormalEndCount.setStatus("mandatory")
_ConnLoopOpeAbnormalEndCount_Type = Integer32
_ConnLoopOpeAbnormalEndCount_Object = MibScalar
connLoopOpeAbnormalEndCount = _ConnLoopOpeAbnormalEndCount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 12),
    _ConnLoopOpeAbnormalEndCount_Type()
)
connLoopOpeAbnormalEndCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLoopOpeAbnormalEndCount.setStatus("mandatory")
_ConnLoopOpeAbortCount_Type = Integer32
_ConnLoopOpeAbortCount_Object = MibScalar
connLoopOpeAbortCount = _ConnLoopOpeAbortCount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 13),
    _ConnLoopOpeAbortCount_Type()
)
connLoopOpeAbortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLoopOpeAbortCount.setStatus("mandatory")
_ConnLoopOpeLoopBackPointIdLength_Type = Integer32
_ConnLoopOpeLoopBackPointIdLength_Object = MibScalar
connLoopOpeLoopBackPointIdLength = _ConnLoopOpeLoopBackPointIdLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 8, 1, 14),
    _ConnLoopOpeLoopBackPointIdLength_Type()
)
connLoopOpeLoopBackPointIdLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLoopOpeLoopBackPointIdLength.setStatus("mandatory")
_ConnProfile_ObjectIdentity = ObjectIdentity
connProfile = _ConnProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9)
)
_ConnProfileIndexNext_Type = ConnProfileIndex
_ConnProfileIndexNext_Object = MibScalar
connProfileIndexNext = _ConnProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 1),
    _ConnProfileIndexNext_Type()
)
connProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connProfileIndexNext.setStatus("mandatory")
_ConnProfileTable_Object = MibTable
connProfileTable = _ConnProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2)
)
if mibBuilder.loadTexts:
    connProfileTable.setStatus("mandatory")
_ConnProfileEntry_Object = MibTableRow
connProfileEntry = _ConnProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1)
)
connProfileEntry.setIndexNames(
    (0, "NEC-MIB", "connProfileIndex"),
)
if mibBuilder.loadTexts:
    connProfileEntry.setStatus("mandatory")
_ConnProfileIndex_Type = ConnProfileIndex
_ConnProfileIndex_Object = MibTableColumn
connProfileIndex = _ConnProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 1),
    _ConnProfileIndex_Type()
)
connProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connProfileIndex.setStatus("mandatory")


class _ConnProfileRowStatus_Type(Integer32):
    """Custom type connProfileRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConnProfileRowStatus_Type.__name__ = "Integer32"
_ConnProfileRowStatus_Object = MibTableColumn
connProfileRowStatus = _ConnProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 2),
    _ConnProfileRowStatus_Type()
)
connProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileRowStatus.setStatus("mandatory")


class _ConnProfileCause_Type(Integer32):
    """Custom type connProfileCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alreadyExist", 5),
          ("duplicateName", 6),
          ("inconsistentEpd", 3),
          ("inconsistentRate", 7),
          ("otherFailure", 2),
          ("parameterNotEnough", 4),
          ("rowExisting", 1))
    )


_ConnProfileCause_Type.__name__ = "Integer32"
_ConnProfileCause_Object = MibTableColumn
connProfileCause = _ConnProfileCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 3),
    _ConnProfileCause_Type()
)
connProfileCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connProfileCause.setStatus("mandatory")


class _ConnProfileTrafficType_Type(Integer32):
    """Custom type connProfileTrafficType based on Integer32"""
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
        *(("traffic-ABR", 4),
          ("traffic-CBR", 1),
          ("traffic-UBR", 5),
          ("traffic-nrt-VBR", 3),
          ("traffic-rt-VBR", 2))
    )


_ConnProfileTrafficType_Type.__name__ = "Integer32"
_ConnProfileTrafficType_Object = MibTableColumn
connProfileTrafficType = _ConnProfileTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 4),
    _ConnProfileTrafficType_Type()
)
connProfileTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileTrafficType.setStatus("mandatory")


class _ConnProfileName_Type(DisplayString):
    """Custom type connProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 10),
    )


_ConnProfileName_Type.__name__ = "DisplayString"
_ConnProfileName_Object = MibTableColumn
connProfileName = _ConnProfileName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 5),
    _ConnProfileName_Type()
)
connProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileName.setStatus("mandatory")


class _ConnProfileParam1_Type(Integer32):
    """Custom type connProfileParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1412830),
    )


_ConnProfileParam1_Type.__name__ = "Integer32"
_ConnProfileParam1_Object = MibTableColumn
connProfileParam1 = _ConnProfileParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 6),
    _ConnProfileParam1_Type()
)
connProfileParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileParam1.setStatus("mandatory")


class _ConnProfileParam2_Type(Integer32):
    """Custom type connProfileParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1412830),
    )


_ConnProfileParam2_Type.__name__ = "Integer32"
_ConnProfileParam2_Object = MibTableColumn
connProfileParam2 = _ConnProfileParam2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 7),
    _ConnProfileParam2_Type()
)
connProfileParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileParam2.setStatus("mandatory")


class _ConnProfileParam3_Type(Integer32):
    """Custom type connProfileParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1412830),
    )


_ConnProfileParam3_Type.__name__ = "Integer32"
_ConnProfileParam3_Object = MibTableColumn
connProfileParam3 = _ConnProfileParam3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 8),
    _ConnProfileParam3_Type()
)
connProfileParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileParam3.setStatus("mandatory")


class _ConnProfileParam4_Type(Integer32):
    """Custom type connProfileParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ConnProfileParam4_Type.__name__ = "Integer32"
_ConnProfileParam4_Object = MibTableColumn
connProfileParam4 = _ConnProfileParam4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 2, 1, 9),
    _ConnProfileParam4_Type()
)
connProfileParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileParam4.setStatus("mandatory")


class _ConnProfileName2Index_Type(DisplayString):
    """Custom type connProfileName2Index based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 10),
    )


_ConnProfileName2Index_Type.__name__ = "DisplayString"
_ConnProfileName2Index_Object = MibScalar
connProfileName2Index = _ConnProfileName2Index_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 3),
    _ConnProfileName2Index_Type()
)
connProfileName2Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfileName2Index.setStatus("mandatory")
_ConnProfileName2IndexResult_Type = ConnProfileIndex
_ConnProfileName2IndexResult_Object = MibScalar
connProfileName2IndexResult = _ConnProfileName2IndexResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 9, 4),
    _ConnProfileName2IndexResult_Type()
)
connProfileName2IndexResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connProfileName2IndexResult.setStatus("mandatory")
_ConnSvcTable_Object = MibTable
connSvcTable = _ConnSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 10)
)
if mibBuilder.loadTexts:
    connSvcTable.setStatus("mandatory")
_ConnSvcEntry_Object = MibTableRow
connSvcEntry = _ConnSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 10, 1)
)
connSvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NEC-MIB", "connSvcIndex"),
)
if mibBuilder.loadTexts:
    connSvcEntry.setStatus("mandatory")
_ConnSvcIndex_Type = Integer32
_ConnSvcIndex_Object = MibTableColumn
connSvcIndex = _ConnSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 10, 1, 1),
    _ConnSvcIndex_Type()
)
connSvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connSvcIndex.setStatus("mandatory")
_ConnSvcInf_Type = Opaque
_ConnSvcInf_Object = MibTableColumn
connSvcInf = _ConnSvcInf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 10, 1, 2),
    _ConnSvcInf_Type()
)
connSvcInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSvcInf.setStatus("mandatory")
_ConnCe_ObjectIdentity = ObjectIdentity
connCe = _ConnCe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11)
)
_ConnCeVc_ObjectIdentity = ObjectIdentity
connCeVc = _ConnCeVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1)
)
_ConnCeVcTable_Object = MibTable
connCeVcTable = _ConnCeVcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1)
)
if mibBuilder.loadTexts:
    connCeVcTable.setStatus("mandatory")
_ConnCeVcEntry_Object = MibTableRow
connCeVcEntry = _ConnCeVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1)
)
connCeVcEntry.setIndexNames(
    (0, "NEC-MIB", "connCeVcPort"),
    (0, "NEC-MIB", "connCeVcVci"),
)
if mibBuilder.loadTexts:
    connCeVcEntry.setStatus("mandatory")
_ConnCeVcPort_Type = Integer32
_ConnCeVcPort_Object = MibTableColumn
connCeVcPort = _ConnCeVcPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 1),
    _ConnCeVcPort_Type()
)
connCeVcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connCeVcPort.setStatus("mandatory")


class _ConnCeVcVci_Type(Integer32):
    """Custom type connCeVcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 383),
    )


_ConnCeVcVci_Type.__name__ = "Integer32"
_ConnCeVcVci_Object = MibTableColumn
connCeVcVci = _ConnCeVcVci_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 2),
    _ConnCeVcVci_Type()
)
connCeVcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connCeVcVci.setStatus("mandatory")


class _ConnCeVcRowStatus_Type(Integer32):
    """Custom type connCeVcRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConnCeVcRowStatus_Type.__name__ = "Integer32"
_ConnCeVcRowStatus_Object = MibTableColumn
connCeVcRowStatus = _ConnCeVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 3),
    _ConnCeVcRowStatus_Type()
)
connCeVcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcRowStatus.setStatus("mandatory")


class _ConnCeVcCause_Type(Integer32):
    """Custom type connCeVcCause based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("alreadyAssignedTs", 7),
          ("illegalCdvt", 14),
          ("illegalDownPartialFillSize", 13),
          ("illegalPort", 10),
          ("illegalTimeslot", 9),
          ("illegalUpPartialFillSize", 12),
          ("illegalVci", 11),
          ("illegalpkg", 4),
          ("inconsistentTss", 8),
          ("otherFailure", 2),
          ("parameterNotEnough", 3),
          ("rowExisting", 1),
          ("tssOverFllow", 6),
          ("vcsOverFllow", 5))
    )


_ConnCeVcCause_Type.__name__ = "Integer32"
_ConnCeVcCause_Object = MibTableColumn
connCeVcCause = _ConnCeVcCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 4),
    _ConnCeVcCause_Type()
)
connCeVcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCeVcCause.setStatus("mandatory")


class _ConnCeVcDirection_Type(Integer32):
    """Custom type connCeVcDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bi", 1),
          ("down", 3),
          ("up", 2))
    )


_ConnCeVcDirection_Type.__name__ = "Integer32"
_ConnCeVcDirection_Object = MibTableColumn
connCeVcDirection = _ConnCeVcDirection_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 5),
    _ConnCeVcDirection_Type()
)
connCeVcDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcDirection.setStatus("mandatory")


class _ConnCeVcUpPartialFillSize_Type(Integer32):
    """Custom type connCeVcUpPartialFillSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 47),
    )


_ConnCeVcUpPartialFillSize_Type.__name__ = "Integer32"
_ConnCeVcUpPartialFillSize_Object = MibTableColumn
connCeVcUpPartialFillSize = _ConnCeVcUpPartialFillSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 6),
    _ConnCeVcUpPartialFillSize_Type()
)
connCeVcUpPartialFillSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcUpPartialFillSize.setStatus("mandatory")


class _ConnCeVcDownPartialFillSize_Type(Integer32):
    """Custom type connCeVcDownPartialFillSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 47),
    )


_ConnCeVcDownPartialFillSize_Type.__name__ = "Integer32"
_ConnCeVcDownPartialFillSize_Object = MibTableColumn
connCeVcDownPartialFillSize = _ConnCeVcDownPartialFillSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 7),
    _ConnCeVcDownPartialFillSize_Type()
)
connCeVcDownPartialFillSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcDownPartialFillSize.setStatus("mandatory")


class _ConnCeVcCondition_Type(Integer32):
    """Custom type connCeVcCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_ConnCeVcCondition_Type.__name__ = "Integer32"
_ConnCeVcCondition_Object = MibTableColumn
connCeVcCondition = _ConnCeVcCondition_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 8),
    _ConnCeVcCondition_Type()
)
connCeVcCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcCondition.setStatus("mandatory")


class _ConnCeVcCDVT_Type(Integer32):
    """Custom type connCeVcCDVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 7218),
    )


_ConnCeVcCDVT_Type.__name__ = "Integer32"
_ConnCeVcCDVT_Object = MibTableColumn
connCeVcCDVT = _ConnCeVcCDVT_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 9),
    _ConnCeVcCDVT_Type()
)
connCeVcCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcCDVT.setStatus("mandatory")


class _ConnCeVcUpPCR_Type(Integer32):
    """Custom type connCeVcUpPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 118979),
    )


_ConnCeVcUpPCR_Type.__name__ = "Integer32"
_ConnCeVcUpPCR_Object = MibTableColumn
connCeVcUpPCR = _ConnCeVcUpPCR_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 10),
    _ConnCeVcUpPCR_Type()
)
connCeVcUpPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCeVcUpPCR.setStatus("mandatory")


class _ConnCeVcDownPCR_Type(Integer32):
    """Custom type connCeVcDownPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 118979),
    )


_ConnCeVcDownPCR_Type.__name__ = "Integer32"
_ConnCeVcDownPCR_Object = MibTableColumn
connCeVcDownPCR = _ConnCeVcDownPCR_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 11),
    _ConnCeVcDownPCR_Type()
)
connCeVcDownPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCeVcDownPCR.setStatus("mandatory")
_ConnCeVcUpTimeSlot1_Type = Integer32
_ConnCeVcUpTimeSlot1_Object = MibTableColumn
connCeVcUpTimeSlot1 = _ConnCeVcUpTimeSlot1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 12),
    _ConnCeVcUpTimeSlot1_Type()
)
connCeVcUpTimeSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcUpTimeSlot1.setStatus("mandatory")
_ConnCeVcDownTimeSlot1_Type = Integer32
_ConnCeVcDownTimeSlot1_Object = MibTableColumn
connCeVcDownTimeSlot1 = _ConnCeVcDownTimeSlot1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 13),
    _ConnCeVcDownTimeSlot1_Type()
)
connCeVcDownTimeSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcDownTimeSlot1.setStatus("mandatory")
_ConnCeVcUpTimeSlot2_Type = Integer32
_ConnCeVcUpTimeSlot2_Object = MibTableColumn
connCeVcUpTimeSlot2 = _ConnCeVcUpTimeSlot2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 14),
    _ConnCeVcUpTimeSlot2_Type()
)
connCeVcUpTimeSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcUpTimeSlot2.setStatus("mandatory")
_ConnCeVcDownTimeSlot2_Type = Integer32
_ConnCeVcDownTimeSlot2_Object = MibTableColumn
connCeVcDownTimeSlot2 = _ConnCeVcDownTimeSlot2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 15),
    _ConnCeVcDownTimeSlot2_Type()
)
connCeVcDownTimeSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcDownTimeSlot2.setStatus("mandatory")
_ConnCeVcUpTimeSlot3_Type = Integer32
_ConnCeVcUpTimeSlot3_Object = MibTableColumn
connCeVcUpTimeSlot3 = _ConnCeVcUpTimeSlot3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 16),
    _ConnCeVcUpTimeSlot3_Type()
)
connCeVcUpTimeSlot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcUpTimeSlot3.setStatus("mandatory")
_ConnCeVcDownTimeSlot3_Type = Integer32
_ConnCeVcDownTimeSlot3_Object = MibTableColumn
connCeVcDownTimeSlot3 = _ConnCeVcDownTimeSlot3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 11, 1, 1, 1, 17),
    _ConnCeVcDownTimeSlot3_Type()
)
connCeVcDownTimeSlot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connCeVcDownTimeSlot3.setStatus("mandatory")
_ConnFr_ObjectIdentity = ObjectIdentity
connFr = _ConnFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12)
)
_ConnFrDlci_ObjectIdentity = ObjectIdentity
connFrDlci = _ConnFrDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1)
)
_ConnFrDlciTable_Object = MibTable
connFrDlciTable = _ConnFrDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1)
)
if mibBuilder.loadTexts:
    connFrDlciTable.setStatus("mandatory")
_ConnFrDlciEntry_Object = MibTableRow
connFrDlciEntry = _ConnFrDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1)
)
connFrDlciEntry.setIndexNames(
    (0, "NEC-MIB", "connFrDlciPort"),
    (0, "NEC-MIB", "connFrDlciIndex"),
)
if mibBuilder.loadTexts:
    connFrDlciEntry.setStatus("mandatory")


class _ConnFrDlciPort_Type(Integer32):
    """Custom type connFrDlciPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ConnFrDlciPort_Type.__name__ = "Integer32"
_ConnFrDlciPort_Object = MibTableColumn
connFrDlciPort = _ConnFrDlciPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 1),
    _ConnFrDlciPort_Type()
)
connFrDlciPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connFrDlciPort.setStatus("mandatory")


class _ConnFrDlciIndex_Type(Integer32):
    """Custom type connFrDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_ConnFrDlciIndex_Type.__name__ = "Integer32"
_ConnFrDlciIndex_Object = MibTableColumn
connFrDlciIndex = _ConnFrDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 2),
    _ConnFrDlciIndex_Type()
)
connFrDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connFrDlciIndex.setStatus("mandatory")


class _ConnFrDlciRowStatus_Type(Integer32):
    """Custom type connFrDlciRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConnFrDlciRowStatus_Type.__name__ = "Integer32"
_ConnFrDlciRowStatus_Object = MibTableColumn
connFrDlciRowStatus = _ConnFrDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 3),
    _ConnFrDlciRowStatus_Type()
)
connFrDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrDlciRowStatus.setStatus("mandatory")


class _ConnFrDlciCause_Type(Integer32):
    """Custom type connFrDlciCause based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("illegalDlci", 8),
          ("illegalPort", 7),
          ("inconsistentInterWorking", 4),
          ("lineDiagnosticsFailure", 6),
          ("noFrProfile", 3),
          ("otherFailure", 2),
          ("pvcsOverFlow", 9),
          ("rowExisting", 1),
          ("totalCIROverFlow", 5))
    )


_ConnFrDlciCause_Type.__name__ = "Integer32"
_ConnFrDlciCause_Object = MibTableColumn
connFrDlciCause = _ConnFrDlciCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 4),
    _ConnFrDlciCause_Type()
)
connFrDlciCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrDlciCause.setStatus("mandatory")


class _ConnFrDlciFrProfile_Type(DisplayString):
    """Custom type connFrDlciFrProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 10),
    )


_ConnFrDlciFrProfile_Type.__name__ = "DisplayString"
_ConnFrDlciFrProfile_Object = MibTableColumn
connFrDlciFrProfile = _ConnFrDlciFrProfile_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 5),
    _ConnFrDlciFrProfile_Type()
)
connFrDlciFrProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrDlciFrProfile.setStatus("mandatory")
_ConnFrDlciPCR_Type = Integer32
_ConnFrDlciPCR_Object = MibTableColumn
connFrDlciPCR = _ConnFrDlciPCR_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 6),
    _ConnFrDlciPCR_Type()
)
connFrDlciPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrDlciPCR.setStatus("mandatory")
_ConnFrDlciSCR_Type = Integer32
_ConnFrDlciSCR_Object = MibTableColumn
connFrDlciSCR = _ConnFrDlciSCR_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 7),
    _ConnFrDlciSCR_Type()
)
connFrDlciSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrDlciSCR.setStatus("mandatory")
_ConnFrDlciMBS_Type = Integer32
_ConnFrDlciMBS_Object = MibTableColumn
connFrDlciMBS = _ConnFrDlciMBS_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 1, 1, 1, 8),
    _ConnFrDlciMBS_Type()
)
connFrDlciMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrDlciMBS.setStatus("mandatory")
_ConnFrProfile_ObjectIdentity = ObjectIdentity
connFrProfile = _ConnFrProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2)
)
_ConnFrProfileIndexNext_Type = ConnFrProfileIndex
_ConnFrProfileIndexNext_Object = MibScalar
connFrProfileIndexNext = _ConnFrProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 1),
    _ConnFrProfileIndexNext_Type()
)
connFrProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrProfileIndexNext.setStatus("mandatory")
_ConnFrProfileTable_Object = MibTable
connFrProfileTable = _ConnFrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2)
)
if mibBuilder.loadTexts:
    connFrProfileTable.setStatus("mandatory")
_ConnFrProfileEntry_Object = MibTableRow
connFrProfileEntry = _ConnFrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1)
)
connFrProfileEntry.setIndexNames(
    (0, "NEC-MIB", "connFrProfileIndex"),
)
if mibBuilder.loadTexts:
    connFrProfileEntry.setStatus("mandatory")
_ConnFrProfileIndex_Type = ConnFrProfileIndex
_ConnFrProfileIndex_Object = MibTableColumn
connFrProfileIndex = _ConnFrProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 1),
    _ConnFrProfileIndex_Type()
)
connFrProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connFrProfileIndex.setStatus("mandatory")


class _ConnFrProfileRowStatus_Type(Integer32):
    """Custom type connFrProfileRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConnFrProfileRowStatus_Type.__name__ = "Integer32"
_ConnFrProfileRowStatus_Object = MibTableColumn
connFrProfileRowStatus = _ConnFrProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 2),
    _ConnFrProfileRowStatus_Type()
)
connFrProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileRowStatus.setStatus("mandatory")


class _ConnFrProfileCause_Type(Integer32):
    """Custom type connFrProfileCause based on Integer32"""
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
        *(("alreadyExist", 4),
          ("duplicateName", 5),
          ("otherFailure", 2),
          ("parameterNotEnough", 3),
          ("rowExisting", 1))
    )


_ConnFrProfileCause_Type.__name__ = "Integer32"
_ConnFrProfileCause_Object = MibTableColumn
connFrProfileCause = _ConnFrProfileCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 3),
    _ConnFrProfileCause_Type()
)
connFrProfileCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrProfileCause.setStatus("mandatory")


class _ConnFrProfileName_Type(DisplayString):
    """Custom type connFrProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 10),
    )


_ConnFrProfileName_Type.__name__ = "DisplayString"
_ConnFrProfileName_Object = MibTableColumn
connFrProfileName = _ConnFrProfileName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 4),
    _ConnFrProfileName_Type()
)
connFrProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileName.setStatus("mandatory")


class _ConnFrProfileInterworkingType_Type(Integer32):
    """Custom type connFrProfileInterworkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("service", 2))
    )


_ConnFrProfileInterworkingType_Type.__name__ = "Integer32"
_ConnFrProfileInterworkingType_Object = MibTableColumn
connFrProfileInterworkingType = _ConnFrProfileInterworkingType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 5),
    _ConnFrProfileInterworkingType_Type()
)
connFrProfileInterworkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileInterworkingType.setStatus("mandatory")


class _ConnFrProfileCIR_Type(Integer32):
    """Custom type connFrProfileCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1984),
    )


_ConnFrProfileCIR_Type.__name__ = "Integer32"
_ConnFrProfileCIR_Object = MibTableColumn
connFrProfileCIR = _ConnFrProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 6),
    _ConnFrProfileCIR_Type()
)
connFrProfileCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileCIR.setStatus("mandatory")


class _ConnFrProfileDEtoCLP_Type(Integer32):
    """Custom type connFrProfileDEtoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_ConnFrProfileDEtoCLP_Type.__name__ = "Integer32"
_ConnFrProfileDEtoCLP_Object = MibTableColumn
connFrProfileDEtoCLP = _ConnFrProfileDEtoCLP_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 7),
    _ConnFrProfileDEtoCLP_Type()
)
connFrProfileDEtoCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileDEtoCLP.setStatus("mandatory")


class _ConnFrProfileCLPValue_Type(Integer32):
    """Custom type connFrProfileCLPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 3),
          ("on", 2))
    )


_ConnFrProfileCLPValue_Type.__name__ = "Integer32"
_ConnFrProfileCLPValue_Object = MibTableColumn
connFrProfileCLPValue = _ConnFrProfileCLPValue_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 8),
    _ConnFrProfileCLPValue_Type()
)
connFrProfileCLPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileCLPValue.setStatus("mandatory")


class _ConnFrProfileCLPtoDE_Type(Integer32):
    """Custom type connFrProfileCLPtoDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_ConnFrProfileCLPtoDE_Type.__name__ = "Integer32"
_ConnFrProfileCLPtoDE_Object = MibTableColumn
connFrProfileCLPtoDE = _ConnFrProfileCLPtoDE_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 9),
    _ConnFrProfileCLPtoDE_Type()
)
connFrProfileCLPtoDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileCLPtoDE.setStatus("mandatory")


class _ConnFrProfileDEValue_Type(Integer32):
    """Custom type connFrProfileDEValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 3),
          ("on", 2))
    )


_ConnFrProfileDEValue_Type.__name__ = "Integer32"
_ConnFrProfileDEValue_Object = MibTableColumn
connFrProfileDEValue = _ConnFrProfileDEValue_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 10),
    _ConnFrProfileDEValue_Type()
)
connFrProfileDEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileDEValue.setStatus("mandatory")


class _ConnFrProfileCapsulationMode_Type(Integer32):
    """Custom type connFrProfileCapsulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("translation", 3),
          ("transparent", 2))
    )


_ConnFrProfileCapsulationMode_Type.__name__ = "Integer32"
_ConnFrProfileCapsulationMode_Object = MibTableColumn
connFrProfileCapsulationMode = _ConnFrProfileCapsulationMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 11),
    _ConnFrProfileCapsulationMode_Type()
)
connFrProfileCapsulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileCapsulationMode.setStatus("mandatory")


class _ConnFrProfileCongestionMode_Type(Integer32):
    """Custom type connFrProfileCongestionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 2),
          ("mode2", 3),
          ("notApplicable", 1))
    )


_ConnFrProfileCongestionMode_Type.__name__ = "Integer32"
_ConnFrProfileCongestionMode_Object = MibTableColumn
connFrProfileCongestionMode = _ConnFrProfileCongestionMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 2, 1, 12),
    _ConnFrProfileCongestionMode_Type()
)
connFrProfileCongestionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileCongestionMode.setStatus("mandatory")


class _ConnFrProfileName2Index_Type(DisplayString):
    """Custom type connFrProfileName2Index based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 10),
    )


_ConnFrProfileName2Index_Type.__name__ = "DisplayString"
_ConnFrProfileName2Index_Object = MibScalar
connFrProfileName2Index = _ConnFrProfileName2Index_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 3),
    _ConnFrProfileName2Index_Type()
)
connFrProfileName2Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connFrProfileName2Index.setStatus("mandatory")
_ConnFrProfileName2IndexResult_Type = ConnFrProfileIndex
_ConnFrProfileName2IndexResult_Object = MibScalar
connFrProfileName2IndexResult = _ConnFrProfileName2IndexResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 4, 12, 2, 4),
    _ConnFrProfileName2IndexResult_Type()
)
connFrProfileName2IndexResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFrProfileName2IndexResult.setStatus("mandatory")
_Perf_ObjectIdentity = ObjectIdentity
perf = _Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5)
)


class _PerfTrapEnable_Type(Integer32):
    """Custom type perfTrapEnable based on Integer32"""
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


_PerfTrapEnable_Type.__name__ = "Integer32"
_PerfTrapEnable_Object = MibScalar
perfTrapEnable = _PerfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 1),
    _PerfTrapEnable_Type()
)
perfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfTrapEnable.setStatus("mandatory")
_PerfIfTable_Object = MibTable
perfIfTable = _PerfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2)
)
if mibBuilder.loadTexts:
    perfIfTable.setStatus("mandatory")
_PerfIfEntry_Object = MibTableRow
perfIfEntry = _PerfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1)
)
perfIfEntry.setIndexNames(
    (0, "NEC-MIB", "perfIfIndex"),
)
if mibBuilder.loadTexts:
    perfIfEntry.setStatus("mandatory")
_PerfIfIndex_Type = Integer32
_PerfIfIndex_Object = MibTableColumn
perfIfIndex = _PerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 1),
    _PerfIfIndex_Type()
)
perfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfIfIndex.setStatus("mandatory")


class _PerfIfReceivedCells_Type(OctetString):
    """Custom type perfIfReceivedCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfReceivedCells_Type.__name__ = "OctetString"
_PerfIfReceivedCells_Object = MibTableColumn
perfIfReceivedCells = _PerfIfReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 2),
    _PerfIfReceivedCells_Type()
)
perfIfReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfReceivedCells.setStatus("mandatory")
_PerfIfReceivedCellsCounters_Type = Counter32
_PerfIfReceivedCellsCounters_Object = MibTableColumn
perfIfReceivedCellsCounters = _PerfIfReceivedCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 3),
    _PerfIfReceivedCellsCounters_Type()
)
perfIfReceivedCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfReceivedCellsCounters.setStatus("mandatory")


class _PerfIfTransmittedCells_Type(OctetString):
    """Custom type perfIfTransmittedCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfTransmittedCells_Type.__name__ = "OctetString"
_PerfIfTransmittedCells_Object = MibTableColumn
perfIfTransmittedCells = _PerfIfTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 4),
    _PerfIfTransmittedCells_Type()
)
perfIfTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfTransmittedCells.setStatus("mandatory")
_PerfIfTransmittedCellsCounters_Type = Counter32
_PerfIfTransmittedCellsCounters_Object = MibTableColumn
perfIfTransmittedCellsCounters = _PerfIfTransmittedCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 5),
    _PerfIfTransmittedCellsCounters_Type()
)
perfIfTransmittedCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfTransmittedCellsCounters.setStatus("mandatory")


class _PerfIfMisDelivdCells_Type(OctetString):
    """Custom type perfIfMisDelivdCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfMisDelivdCells_Type.__name__ = "OctetString"
_PerfIfMisDelivdCells_Object = MibTableColumn
perfIfMisDelivdCells = _PerfIfMisDelivdCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 8),
    _PerfIfMisDelivdCells_Type()
)
perfIfMisDelivdCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfMisDelivdCells.setStatus("mandatory")
_PerfIfMisDelivdCellsCounters_Type = Counter32
_PerfIfMisDelivdCellsCounters_Object = MibTableColumn
perfIfMisDelivdCellsCounters = _PerfIfMisDelivdCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 9),
    _PerfIfMisDelivdCellsCounters_Type()
)
perfIfMisDelivdCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfMisDelivdCellsCounters.setStatus("mandatory")


class _PerfIfThresholdExcessCells_Type(OctetString):
    """Custom type perfIfThresholdExcessCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfThresholdExcessCells_Type.__name__ = "OctetString"
_PerfIfThresholdExcessCells_Object = MibTableColumn
perfIfThresholdExcessCells = _PerfIfThresholdExcessCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 10),
    _PerfIfThresholdExcessCells_Type()
)
perfIfThresholdExcessCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfThresholdExcessCells.setStatus("mandatory")
_PerfIfThresholdExcessCellsCounters_Type = Counter32
_PerfIfThresholdExcessCellsCounters_Object = MibTableColumn
perfIfThresholdExcessCellsCounters = _PerfIfThresholdExcessCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 11),
    _PerfIfThresholdExcessCellsCounters_Type()
)
perfIfThresholdExcessCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfThresholdExcessCellsCounters.setStatus("mandatory")


class _PerfIfUpcErrorCells_Type(OctetString):
    """Custom type perfIfUpcErrorCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfUpcErrorCells_Type.__name__ = "OctetString"
_PerfIfUpcErrorCells_Object = MibTableColumn
perfIfUpcErrorCells = _PerfIfUpcErrorCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 12),
    _PerfIfUpcErrorCells_Type()
)
perfIfUpcErrorCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfUpcErrorCells.setStatus("mandatory")
_PerfIfUpcErrorCellsCounters_Type = Counter32
_PerfIfUpcErrorCellsCounters_Object = MibTableColumn
perfIfUpcErrorCellsCounters = _PerfIfUpcErrorCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 2, 1, 13),
    _PerfIfUpcErrorCellsCounters_Type()
)
perfIfUpcErrorCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfUpcErrorCellsCounters.setStatus("mandatory")
_PerfIfSlotTable_Object = MibTable
perfIfSlotTable = _PerfIfSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3)
)
if mibBuilder.loadTexts:
    perfIfSlotTable.setStatus("mandatory")
_PerfIfSlotEntry_Object = MibTableRow
perfIfSlotEntry = _PerfIfSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1)
)
perfIfSlotEntry.setIndexNames(
    (0, "NEC-MIB", "slotIfConfIndex"),
)
if mibBuilder.loadTexts:
    perfIfSlotEntry.setStatus("mandatory")


class _PerfIfSlotReceivedCells_Type(OctetString):
    """Custom type perfIfSlotReceivedCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfSlotReceivedCells_Type.__name__ = "OctetString"
_PerfIfSlotReceivedCells_Object = MibTableColumn
perfIfSlotReceivedCells = _PerfIfSlotReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 1),
    _PerfIfSlotReceivedCells_Type()
)
perfIfSlotReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotReceivedCells.setStatus("mandatory")


class _PerfIfSlotTransmittedCells_Type(OctetString):
    """Custom type perfIfSlotTransmittedCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfSlotTransmittedCells_Type.__name__ = "OctetString"
_PerfIfSlotTransmittedCells_Object = MibTableColumn
perfIfSlotTransmittedCells = _PerfIfSlotTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 2),
    _PerfIfSlotTransmittedCells_Type()
)
perfIfSlotTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotTransmittedCells.setStatus("mandatory")


class _PerfIfSlotInDropCells_Type(OctetString):
    """Custom type perfIfSlotInDropCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfSlotInDropCells_Type.__name__ = "OctetString"
_PerfIfSlotInDropCells_Object = MibTableColumn
perfIfSlotInDropCells = _PerfIfSlotInDropCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 3),
    _PerfIfSlotInDropCells_Type()
)
perfIfSlotInDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotInDropCells.setStatus("mandatory")
_PerfIfSlotReceivedCellsCounters_Type = Counter32
_PerfIfSlotReceivedCellsCounters_Object = MibTableColumn
perfIfSlotReceivedCellsCounters = _PerfIfSlotReceivedCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 5),
    _PerfIfSlotReceivedCellsCounters_Type()
)
perfIfSlotReceivedCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotReceivedCellsCounters.setStatus("mandatory")
_PerfIfSlotTransmittedCellsCounters_Type = Counter32
_PerfIfSlotTransmittedCellsCounters_Object = MibTableColumn
perfIfSlotTransmittedCellsCounters = _PerfIfSlotTransmittedCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 6),
    _PerfIfSlotTransmittedCellsCounters_Type()
)
perfIfSlotTransmittedCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotTransmittedCellsCounters.setStatus("mandatory")
_PerfIfSlotInDropCellsCounters_Type = Counter32
_PerfIfSlotInDropCellsCounters_Object = MibTableColumn
perfIfSlotInDropCellsCounters = _PerfIfSlotInDropCellsCounters_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 7),
    _PerfIfSlotInDropCellsCounters_Type()
)
perfIfSlotInDropCellsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotInDropCellsCounters.setStatus("mandatory")


class _PerfIfSlotHCThresholdExcessCells_Type(OctetString):
    """Custom type perfIfSlotHCThresholdExcessCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfSlotHCThresholdExcessCells_Type.__name__ = "OctetString"
_PerfIfSlotHCThresholdExcessCells_Object = MibTableColumn
perfIfSlotHCThresholdExcessCells = _PerfIfSlotHCThresholdExcessCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 9),
    _PerfIfSlotHCThresholdExcessCells_Type()
)
perfIfSlotHCThresholdExcessCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotHCThresholdExcessCells.setStatus("mandatory")
_PerfIfSlotThresholdExcessCells_Type = Counter32
_PerfIfSlotThresholdExcessCells_Object = MibTableColumn
perfIfSlotThresholdExcessCells = _PerfIfSlotThresholdExcessCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 10),
    _PerfIfSlotThresholdExcessCells_Type()
)
perfIfSlotThresholdExcessCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotThresholdExcessCells.setStatus("mandatory")


class _PerfIfSlotHCUpcErrorCells_Type(OctetString):
    """Custom type perfIfSlotHCUpcErrorCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfIfSlotHCUpcErrorCells_Type.__name__ = "OctetString"
_PerfIfSlotHCUpcErrorCells_Object = MibTableColumn
perfIfSlotHCUpcErrorCells = _PerfIfSlotHCUpcErrorCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 11),
    _PerfIfSlotHCUpcErrorCells_Type()
)
perfIfSlotHCUpcErrorCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotHCUpcErrorCells.setStatus("mandatory")
_PerfIfSlotUpcErrorCells_Type = Counter32
_PerfIfSlotUpcErrorCells_Object = MibTableColumn
perfIfSlotUpcErrorCells = _PerfIfSlotUpcErrorCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 3, 1, 12),
    _PerfIfSlotUpcErrorCells_Type()
)
perfIfSlotUpcErrorCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfSlotUpcErrorCells.setStatus("mandatory")
_PerfIfPhysTable_Object = MibTable
perfIfPhysTable = _PerfIfPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4)
)
if mibBuilder.loadTexts:
    perfIfPhysTable.setStatus("mandatory")
_PerfIfPhysEntry_Object = MibTableRow
perfIfPhysEntry = _PerfIfPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1)
)
perfIfPhysEntry.setIndexNames(
    (0, "NEC-MIB", "perfIfPhysPort"),
)
if mibBuilder.loadTexts:
    perfIfPhysEntry.setStatus("mandatory")
_PerfIfPhysPort_Type = Integer32
_PerfIfPhysPort_Object = MibTableColumn
perfIfPhysPort = _PerfIfPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 1),
    _PerfIfPhysPort_Type()
)
perfIfPhysPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfIfPhysPort.setStatus("mandatory")
_PerfIfPhysHCHecErorrs_Type = OctetString
_PerfIfPhysHCHecErorrs_Object = MibTableColumn
perfIfPhysHCHecErorrs = _PerfIfPhysHCHecErorrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 2),
    _PerfIfPhysHCHecErorrs_Type()
)
perfIfPhysHCHecErorrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCHecErorrs.setStatus("mandatory")
_PerfIfPhysHecErorrs_Type = Integer32
_PerfIfPhysHecErorrs_Object = MibTableColumn
perfIfPhysHecErorrs = _PerfIfPhysHecErorrs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 3),
    _PerfIfPhysHecErorrs_Type()
)
perfIfPhysHecErorrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHecErorrs.setStatus("mandatory")
_PerfIfPhysHCHecDropCells_Type = OctetString
_PerfIfPhysHCHecDropCells_Object = MibTableColumn
perfIfPhysHCHecDropCells = _PerfIfPhysHCHecDropCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 4),
    _PerfIfPhysHCHecDropCells_Type()
)
perfIfPhysHCHecDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCHecDropCells.setStatus("mandatory")
_PerfIfPhysHecDropCells_Type = Integer32
_PerfIfPhysHecDropCells_Object = MibTableColumn
perfIfPhysHecDropCells = _PerfIfPhysHecDropCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 5),
    _PerfIfPhysHecDropCells_Type()
)
perfIfPhysHecDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHecDropCells.setStatus("mandatory")
_PerfIfPhysHCB1Errors_Type = OctetString
_PerfIfPhysHCB1Errors_Object = MibTableColumn
perfIfPhysHCB1Errors = _PerfIfPhysHCB1Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 6),
    _PerfIfPhysHCB1Errors_Type()
)
perfIfPhysHCB1Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCB1Errors.setStatus("mandatory")
_PerfIfPhysB1Errors_Type = Integer32
_PerfIfPhysB1Errors_Object = MibTableColumn
perfIfPhysB1Errors = _PerfIfPhysB1Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 7),
    _PerfIfPhysB1Errors_Type()
)
perfIfPhysB1Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysB1Errors.setStatus("mandatory")
_PerfIfPhysHCB2Errors_Type = OctetString
_PerfIfPhysHCB2Errors_Object = MibTableColumn
perfIfPhysHCB2Errors = _PerfIfPhysHCB2Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 8),
    _PerfIfPhysHCB2Errors_Type()
)
perfIfPhysHCB2Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCB2Errors.setStatus("mandatory")
_PerfIfPhysB2Errors_Type = Integer32
_PerfIfPhysB2Errors_Object = MibTableColumn
perfIfPhysB2Errors = _PerfIfPhysB2Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 9),
    _PerfIfPhysB2Errors_Type()
)
perfIfPhysB2Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysB2Errors.setStatus("mandatory")
_PerfIfPhysHCB3Errors_Type = OctetString
_PerfIfPhysHCB3Errors_Object = MibTableColumn
perfIfPhysHCB3Errors = _PerfIfPhysHCB3Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 10),
    _PerfIfPhysHCB3Errors_Type()
)
perfIfPhysHCB3Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCB3Errors.setStatus("mandatory")
_PerfIfPhysB3Errors_Type = Integer32
_PerfIfPhysB3Errors_Object = MibScalar
perfIfPhysB3Errors = _PerfIfPhysB3Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 11),
    _PerfIfPhysB3Errors_Type()
)
perfIfPhysB3Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysB3Errors.setStatus("mandatory")
_PerfIfPhysHCPathFEBEs_Type = OctetString
_PerfIfPhysHCPathFEBEs_Object = MibTableColumn
perfIfPhysHCPathFEBEs = _PerfIfPhysHCPathFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 12),
    _PerfIfPhysHCPathFEBEs_Type()
)
perfIfPhysHCPathFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCPathFEBEs.setStatus("mandatory")
_PerfIfPhysPathFEBEs_Type = Integer32
_PerfIfPhysPathFEBEs_Object = MibTableColumn
perfIfPhysPathFEBEs = _PerfIfPhysPathFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 13),
    _PerfIfPhysPathFEBEs_Type()
)
perfIfPhysPathFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysPathFEBEs.setStatus("mandatory")
_PerfIfPhysHCLineFEBEs_Type = OctetString
_PerfIfPhysHCLineFEBEs_Object = MibTableColumn
perfIfPhysHCLineFEBEs = _PerfIfPhysHCLineFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 14),
    _PerfIfPhysHCLineFEBEs_Type()
)
perfIfPhysHCLineFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCLineFEBEs.setStatus("mandatory")
_PerfIfPhysLineFEBEs_Type = Integer32
_PerfIfPhysLineFEBEs_Object = MibTableColumn
perfIfPhysLineFEBEs = _PerfIfPhysLineFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 15),
    _PerfIfPhysLineFEBEs_Type()
)
perfIfPhysLineFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysLineFEBEs.setStatus("mandatory")
_PerfIfPhysHCFramingErrors_Type = OctetString
_PerfIfPhysHCFramingErrors_Object = MibTableColumn
perfIfPhysHCFramingErrors = _PerfIfPhysHCFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 16),
    _PerfIfPhysHCFramingErrors_Type()
)
perfIfPhysHCFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCFramingErrors.setStatus("mandatory")
_PerfIfPhysFramingErrors_Type = Integer32
_PerfIfPhysFramingErrors_Object = MibTableColumn
perfIfPhysFramingErrors = _PerfIfPhysFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 17),
    _PerfIfPhysFramingErrors_Type()
)
perfIfPhysFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysFramingErrors.setStatus("mandatory")
_PerfIfPhysHCReceivedCells_Type = OctetString
_PerfIfPhysHCReceivedCells_Object = MibTableColumn
perfIfPhysHCReceivedCells = _PerfIfPhysHCReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 18),
    _PerfIfPhysHCReceivedCells_Type()
)
perfIfPhysHCReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCReceivedCells.setStatus("mandatory")
_PerfIfPhysReceivedCells_Type = Integer32
_PerfIfPhysReceivedCells_Object = MibTableColumn
perfIfPhysReceivedCells = _PerfIfPhysReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 19),
    _PerfIfPhysReceivedCells_Type()
)
perfIfPhysReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysReceivedCells.setStatus("mandatory")
_PerfIfPhysHCTransmittedCells_Type = OctetString
_PerfIfPhysHCTransmittedCells_Object = MibTableColumn
perfIfPhysHCTransmittedCells = _PerfIfPhysHCTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 20),
    _PerfIfPhysHCTransmittedCells_Type()
)
perfIfPhysHCTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCTransmittedCells.setStatus("mandatory")
_PerfIfPhysTransmittedCells_Type = Integer32
_PerfIfPhysTransmittedCells_Object = MibTableColumn
perfIfPhysTransmittedCells = _PerfIfPhysTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 21),
    _PerfIfPhysTransmittedCells_Type()
)
perfIfPhysTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysTransmittedCells.setStatus("mandatory")
_PerfIfPhysHCIdelUnassignedCells_Type = OctetString
_PerfIfPhysHCIdelUnassignedCells_Object = MibTableColumn
perfIfPhysHCIdelUnassignedCells = _PerfIfPhysHCIdelUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 22),
    _PerfIfPhysHCIdelUnassignedCells_Type()
)
perfIfPhysHCIdelUnassignedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCIdelUnassignedCells.setStatus("mandatory")
_PerfIfPhysIdelUnassignedCells_Type = Integer32
_PerfIfPhysIdelUnassignedCells_Object = MibTableColumn
perfIfPhysIdelUnassignedCells = _PerfIfPhysIdelUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 23),
    _PerfIfPhysIdelUnassignedCells_Type()
)
perfIfPhysIdelUnassignedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysIdelUnassignedCells.setStatus("mandatory")
_PerfIfPhysHCFEBEErrors_Type = OctetString
_PerfIfPhysHCFEBEErrors_Object = MibTableColumn
perfIfPhysHCFEBEErrors = _PerfIfPhysHCFEBEErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 24),
    _PerfIfPhysHCFEBEErrors_Type()
)
perfIfPhysHCFEBEErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCFEBEErrors.setStatus("mandatory")
_PerfIfPhysFEBEErrors_Type = Integer32
_PerfIfPhysFEBEErrors_Object = MibTableColumn
perfIfPhysFEBEErrors = _PerfIfPhysFEBEErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 25),
    _PerfIfPhysFEBEErrors_Type()
)
perfIfPhysFEBEErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysFEBEErrors.setStatus("mandatory")
_PerfIfPhysHCFEBEs_Type = OctetString
_PerfIfPhysHCFEBEs_Object = MibTableColumn
perfIfPhysHCFEBEs = _PerfIfPhysHCFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 26),
    _PerfIfPhysHCFEBEs_Type()
)
perfIfPhysHCFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCFEBEs.setStatus("mandatory")
_PerfIfPhysFEBEs_Type = Integer32
_PerfIfPhysFEBEs_Object = MibTableColumn
perfIfPhysFEBEs = _PerfIfPhysFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 27),
    _PerfIfPhysFEBEs_Type()
)
perfIfPhysFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysFEBEs.setStatus("mandatory")
_PerfIfPhysHCPathParityErrors_Type = OctetString
_PerfIfPhysHCPathParityErrors_Object = MibTableColumn
perfIfPhysHCPathParityErrors = _PerfIfPhysHCPathParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 28),
    _PerfIfPhysHCPathParityErrors_Type()
)
perfIfPhysHCPathParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCPathParityErrors.setStatus("mandatory")
_PerfIfPhysPathParityErrors_Type = Integer32
_PerfIfPhysPathParityErrors_Object = MibTableColumn
perfIfPhysPathParityErrors = _PerfIfPhysPathParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 29),
    _PerfIfPhysPathParityErrors_Type()
)
perfIfPhysPathParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysPathParityErrors.setStatus("mandatory")
_PerfIfPhysHCParityErrors_Type = OctetString
_PerfIfPhysHCParityErrors_Object = MibTableColumn
perfIfPhysHCParityErrors = _PerfIfPhysHCParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 30),
    _PerfIfPhysHCParityErrors_Type()
)
perfIfPhysHCParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCParityErrors.setStatus("mandatory")
_PerfIfPhysParityErrors_Type = Integer32
_PerfIfPhysParityErrors_Object = MibTableColumn
perfIfPhysParityErrors = _PerfIfPhysParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 31),
    _PerfIfPhysParityErrors_Type()
)
perfIfPhysParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysParityErrors.setStatus("mandatory")
_PerfIfPhysHCSEZs_Type = OctetString
_PerfIfPhysHCSEZs_Object = MibTableColumn
perfIfPhysHCSEZs = _PerfIfPhysHCSEZs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 32),
    _PerfIfPhysHCSEZs_Type()
)
perfIfPhysHCSEZs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCSEZs.setStatus("mandatory")
_PerfIfPhysSEZs_Type = Integer32
_PerfIfPhysSEZs_Object = MibTableColumn
perfIfPhysSEZs = _PerfIfPhysSEZs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 33),
    _PerfIfPhysSEZs_Type()
)
perfIfPhysSEZs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysSEZs.setStatus("mandatory")
_PerfIfPhysHCBitErrors_Type = OctetString
_PerfIfPhysHCBitErrors_Object = MibTableColumn
perfIfPhysHCBitErrors = _PerfIfPhysHCBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 34),
    _PerfIfPhysHCBitErrors_Type()
)
perfIfPhysHCBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCBitErrors.setStatus("mandatory")
_PerfIfPhysBitErrors_Type = Integer32
_PerfIfPhysBitErrors_Object = MibTableColumn
perfIfPhysBitErrors = _PerfIfPhysBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 35),
    _PerfIfPhysBitErrors_Type()
)
perfIfPhysBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysBitErrors.setStatus("mandatory")
_PerfIfPhysHCLcvErrors_Type = OctetString
_PerfIfPhysHCLcvErrors_Object = MibTableColumn
perfIfPhysHCLcvErrors = _PerfIfPhysHCLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 36),
    _PerfIfPhysHCLcvErrors_Type()
)
perfIfPhysHCLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCLcvErrors.setStatus("mandatory")
_PerfIfPhysLcvErrors_Type = Integer32
_PerfIfPhysLcvErrors_Object = MibTableColumn
perfIfPhysLcvErrors = _PerfIfPhysLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 37),
    _PerfIfPhysLcvErrors_Type()
)
perfIfPhysLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysLcvErrors.setStatus("mandatory")
_PerfIfPhysHCBip8Errors_Type = OctetString
_PerfIfPhysHCBip8Errors_Object = MibTableColumn
perfIfPhysHCBip8Errors = _PerfIfPhysHCBip8Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 38),
    _PerfIfPhysHCBip8Errors_Type()
)
perfIfPhysHCBip8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCBip8Errors.setStatus("mandatory")
_PerfIfPhysBip8Errors_Type = Integer32
_PerfIfPhysBip8Errors_Object = MibTableColumn
perfIfPhysBip8Errors = _PerfIfPhysBip8Errors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 39),
    _PerfIfPhysBip8Errors_Type()
)
perfIfPhysBip8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysBip8Errors.setStatus("mandatory")
_PerfIfPhysHCIecErrors_Type = OctetString
_PerfIfPhysHCIecErrors_Object = MibTableColumn
perfIfPhysHCIecErrors = _PerfIfPhysHCIecErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 40),
    _PerfIfPhysHCIecErrors_Type()
)
perfIfPhysHCIecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCIecErrors.setStatus("mandatory")
_PerfIfPhysIecErrors_Type = Integer32
_PerfIfPhysIecErrors_Object = MibTableColumn
perfIfPhysIecErrors = _PerfIfPhysIecErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 41),
    _PerfIfPhysIecErrors_Type()
)
perfIfPhysIecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysIecErrors.setStatus("mandatory")
_PerfIfPhysHCFramingPatternErrors_Type = OctetString
_PerfIfPhysHCFramingPatternErrors_Object = MibTableColumn
perfIfPhysHCFramingPatternErrors = _PerfIfPhysHCFramingPatternErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 42),
    _PerfIfPhysHCFramingPatternErrors_Type()
)
perfIfPhysHCFramingPatternErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCFramingPatternErrors.setStatus("mandatory")
_PerfIfPhysFramingPatternErrors_Type = Integer32
_PerfIfPhysFramingPatternErrors_Object = MibTableColumn
perfIfPhysFramingPatternErrors = _PerfIfPhysFramingPatternErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 43),
    _PerfIfPhysFramingPatternErrors_Type()
)
perfIfPhysFramingPatternErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysFramingPatternErrors.setStatus("mandatory")
_PerfIfPhysHCFramingBitErrors_Type = OctetString
_PerfIfPhysHCFramingBitErrors_Object = MibTableColumn
perfIfPhysHCFramingBitErrors = _PerfIfPhysHCFramingBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 44),
    _PerfIfPhysHCFramingBitErrors_Type()
)
perfIfPhysHCFramingBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCFramingBitErrors.setStatus("mandatory")
_PerfIfPhysFramingBitErrors_Type = Integer32
_PerfIfPhysFramingBitErrors_Object = MibTableColumn
perfIfPhysFramingBitErrors = _PerfIfPhysFramingBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 45),
    _PerfIfPhysFramingBitErrors_Type()
)
perfIfPhysFramingBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysFramingBitErrors.setStatus("mandatory")
_PerfIfPhysHCCrcErrors_Type = OctetString
_PerfIfPhysHCCrcErrors_Object = MibTableColumn
perfIfPhysHCCrcErrors = _PerfIfPhysHCCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 46),
    _PerfIfPhysHCCrcErrors_Type()
)
perfIfPhysHCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysHCCrcErrors.setStatus("mandatory")
_PerfIfPhysCrcErrors_Type = Integer32
_PerfIfPhysCrcErrors_Object = MibTableColumn
perfIfPhysCrcErrors = _PerfIfPhysCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 5, 4, 1, 47),
    _PerfIfPhysCrcErrors_Type()
)
perfIfPhysCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfPhysCrcErrors.setStatus("mandatory")
_Scale_ObjectIdentity = ObjectIdentity
scale = _Scale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6)
)


class _ScaleStatus_Type(Integer32):
    """Custom type scaleStatus based on Integer32"""
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
        *(("allocate", 1),
          ("backup", 3),
          ("free", 4),
          ("install", 2))
    )


_ScaleStatus_Type.__name__ = "Integer32"
_ScaleStatus_Object = MibScalar
scaleStatus = _ScaleStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6, 1),
    _ScaleStatus_Type()
)
scaleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scaleStatus.setStatus("mandatory")


class _ScaleCause_Type(Integer32):
    """Custom type scaleCause based on Integer32"""
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
        *(("accessViolate", 7),
          ("checksumError", 8),
          ("fileNotFound", 6),
          ("nearend", 4),
          ("noData", 9),
          ("other", 1),
          ("sbyAccessError", 10),
          ("start", 2),
          ("succeed", 3),
          ("timeOut", 5))
    )


_ScaleCause_Type.__name__ = "Integer32"
_ScaleCause_Object = MibScalar
scaleCause = _ScaleCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6, 2),
    _ScaleCause_Type()
)
scaleCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scaleCause.setStatus("mandatory")


class _ScaleDataType_Type(Integer32):
    """Custom type scaleDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bill-cdr", 3),
          ("config", 2),
          ("system", 1))
    )


_ScaleDataType_Type.__name__ = "Integer32"
_ScaleDataType_Object = MibScalar
scaleDataType = _ScaleDataType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6, 3),
    _ScaleDataType_Type()
)
scaleDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scaleDataType.setStatus("mandatory")
_ScaleTarget_Type = IpAddress
_ScaleTarget_Object = MibScalar
scaleTarget = _ScaleTarget_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6, 4),
    _ScaleTarget_Type()
)
scaleTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scaleTarget.setStatus("mandatory")
_ScaleFileName_Type = DisplayString
_ScaleFileName_Object = MibScalar
scaleFileName = _ScaleFileName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6, 5),
    _ScaleFileName_Type()
)
scaleFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scaleFileName.setStatus("mandatory")


class _ScaleSwSide_Type(Integer32):
    """Custom type scaleSwSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("sby", 2))
    )


_ScaleSwSide_Type.__name__ = "Integer32"
_ScaleSwSide_Object = MibScalar
scaleSwSide = _ScaleSwSide_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 6, 6),
    _ScaleSwSide_Type()
)
scaleSwSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scaleSwSide.setStatus("mandatory")
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7)
)
_CardStatusTable_Object = MibTable
cardStatusTable = _CardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1)
)
if mibBuilder.loadTexts:
    cardStatusTable.setStatus("mandatory")
_CardStatusEntry_Object = MibTableRow
cardStatusEntry = _CardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1)
)
cardStatusEntry.setIndexNames(
    (0, "NEC-MIB", "slotIfConfIndex"),
)
if mibBuilder.loadTexts:
    cardStatusEntry.setStatus("mandatory")
_CardStatusServerType_Type = Integer32
_CardStatusServerType_Object = MibTableColumn
cardStatusServerType = _CardStatusServerType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 1),
    _CardStatusServerType_Type()
)
cardStatusServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusServerType.setStatus("mandatory")
_CardStatusRevision_Type = DisplayString
_CardStatusRevision_Object = MibTableColumn
cardStatusRevision = _CardStatusRevision_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 2),
    _CardStatusRevision_Type()
)
cardStatusRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusRevision.setStatus("mandatory")


class _CardStatusMateSlotNumber_Type(Integer32):
    """Custom type cardStatusMateSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CardStatusMateSlotNumber_Type.__name__ = "Integer32"
_CardStatusMateSlotNumber_Object = MibTableColumn
cardStatusMateSlotNumber = _CardStatusMateSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 3),
    _CardStatusMateSlotNumber_Type()
)
cardStatusMateSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusMateSlotNumber.setStatus("mandatory")


class _CardStatusMode_Type(Integer32):
    """Custom type cardStatusMode based on Integer32"""
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
        *(("act", 1),
          ("other", 4),
          ("sby", 2),
          ("single", 3))
    )


_CardStatusMode_Type.__name__ = "Integer32"
_CardStatusMode_Object = MibTableColumn
cardStatusMode = _CardStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 4),
    _CardStatusMode_Type()
)
cardStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusMode.setStatus("mandatory")


class _CardStatusPriority_Type(Integer32):
    """Custom type cardStatusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remotePrimary", 2),
          ("remoteSecoundary", 3))
    )


_CardStatusPriority_Type.__name__ = "Integer32"
_CardStatusPriority_Object = MibTableColumn
cardStatusPriority = _CardStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 5),
    _CardStatusPriority_Type()
)
cardStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusPriority.setStatus("mandatory")


class _CardStatusAtmAddr_Type(OctetString):
    """Custom type cardStatusAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_CardStatusAtmAddr_Type.__name__ = "OctetString"
_CardStatusAtmAddr_Object = MibTableColumn
cardStatusAtmAddr = _CardStatusAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 6),
    _CardStatusAtmAddr_Type()
)
cardStatusAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusAtmAddr.setStatus("mandatory")


class _CardStatusMateAtmAddr_Type(OctetString):
    """Custom type cardStatusMateAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_CardStatusMateAtmAddr_Type.__name__ = "OctetString"
_CardStatusMateAtmAddr_Object = MibTableColumn
cardStatusMateAtmAddr = _CardStatusMateAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 1, 1, 7),
    _CardStatusMateAtmAddr_Type()
)
cardStatusMateAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusMateAtmAddr.setStatus("mandatory")
_CardOpeTable_Object = MibTable
cardOpeTable = _CardOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2)
)
if mibBuilder.loadTexts:
    cardOpeTable.setStatus("mandatory")
_CardOpeEntry_Object = MibTableRow
cardOpeEntry = _CardOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1)
)
cardOpeEntry.setIndexNames(
    (0, "NEC-MIB", "slotIfConfIndex"),
)
if mibBuilder.loadTexts:
    cardOpeEntry.setStatus("mandatory")


class _CardOpeReset_Type(Integer32):
    """Custom type cardOpeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ach", 3),
          ("noOperation", 1),
          ("reset", 2))
    )


_CardOpeReset_Type.__name__ = "Integer32"
_CardOpeReset_Object = MibTableColumn
cardOpeReset = _CardOpeReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1, 1),
    _CardOpeReset_Type()
)
cardOpeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardOpeReset.setStatus("mandatory")


class _CardOpeDiagnosis_Type(Integer32):
    """Custom type cardOpeDiagnosis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diagnosis", 2),
          ("noOperation", 1))
    )


_CardOpeDiagnosis_Type.__name__ = "Integer32"
_CardOpeDiagnosis_Object = MibTableColumn
cardOpeDiagnosis = _CardOpeDiagnosis_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1, 2),
    _CardOpeDiagnosis_Type()
)
cardOpeDiagnosis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cardOpeDiagnosis.setStatus("mandatory")


class _CardOpeSave_Type(Integer32):
    """Custom type cardOpeSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("save", 2))
    )


_CardOpeSave_Type.__name__ = "Integer32"
_CardOpeSave_Object = MibTableColumn
cardOpeSave = _CardOpeSave_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1, 3),
    _CardOpeSave_Type()
)
cardOpeSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardOpeSave.setStatus("mandatory")


class _CardOpeSaveResult_Type(Integer32):
    """Custom type cardOpeSaveResult based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("nearend", 5),
          ("nearend-act", 6),
          ("nearend-act-failure-sby", 7),
          ("nearend-sby", 8),
          ("nearend-sby-failure-act", 9),
          ("notReady", 10),
          ("ready", 11),
          ("succeed", 1),
          ("succeed-act", 2),
          ("succeed-sby", 3),
          ("temporaryFailure", 4))
    )


_CardOpeSaveResult_Type.__name__ = "Integer32"
_CardOpeSaveResult_Object = MibTableColumn
cardOpeSaveResult = _CardOpeSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1, 4),
    _CardOpeSaveResult_Type()
)
cardOpeSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOpeSaveResult.setStatus("mandatory")


class _CardOpeCopy_Type(Integer32):
    """Custom type cardOpeCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copy-all-from-act", 2),
          ("copy-all-from-sby", 3),
          ("copy-config-from-act", 4),
          ("copy-config-from-sby", 5),
          ("copy-system-from-act", 6),
          ("copy-system-from-sby", 7),
          ("noOperation", 1))
    )


_CardOpeCopy_Type.__name__ = "Integer32"
_CardOpeCopy_Object = MibTableColumn
cardOpeCopy = _CardOpeCopy_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1, 5),
    _CardOpeCopy_Type()
)
cardOpeCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardOpeCopy.setStatus("mandatory")


class _CardOpeCopyResult_Type(Integer32):
    """Custom type cardOpeCopyResult based on Integer32"""
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
        *(("nearend", 3),
          ("notReady", 4),
          ("ready", 5),
          ("succeed", 1),
          ("temporaryFailure", 2))
    )


_CardOpeCopyResult_Type.__name__ = "Integer32"
_CardOpeCopyResult_Object = MibTableColumn
cardOpeCopyResult = _CardOpeCopyResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 7, 2, 1, 6),
    _CardOpeCopyResult_Type()
)
cardOpeCopyResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOpeCopyResult.setStatus("mandatory")
_Clock_ObjectIdentity = ObjectIdentity
clock = _Clock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8)
)
_ClockOpe_ObjectIdentity = ObjectIdentity
clockOpe = _ClockOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1)
)


class _ClockOpeStatus_Type(Integer32):
    """Custom type clockOpeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allocate", 1),
          ("free", 3),
          ("set", 2))
    )


_ClockOpeStatus_Type.__name__ = "Integer32"
_ClockOpeStatus_Object = MibScalar
clockOpeStatus = _ClockOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 1),
    _ClockOpeStatus_Type()
)
clockOpeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeStatus.setStatus("mandatory")


class _ClockOpeCause_Type(Integer32):
    """Custom type clockOpeCause based on Integer32"""
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
        *(("allPortFailure", 8),
          ("noWriting", 1),
          ("other", 2),
          ("parameterNotEnough", 5),
          ("portNotExist", 6),
          ("portOutOfRange", 7),
          ("setWarning", 4),
          ("succeed", 3))
    )


_ClockOpeCause_Type.__name__ = "Integer32"
_ClockOpeCause_Object = MibScalar
clockOpeCause = _ClockOpeCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 2),
    _ClockOpeCause_Type()
)
clockOpeCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockOpeCause.setStatus("mandatory")


class _ClockOpeMode_Type(Integer32):
    """Custom type clockOpeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ClockOpeMode_Type.__name__ = "Integer32"
_ClockOpeMode_Object = MibScalar
clockOpeMode = _ClockOpeMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 3),
    _ClockOpeMode_Type()
)
clockOpeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeMode.setStatus("mandatory")


class _ClockOpeAccuracy_Type(Integer32):
    """Custom type clockOpeAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(-1, -1),
    )


_ClockOpeAccuracy_Type.__name__ = "Integer32"
_ClockOpeAccuracy_Object = MibScalar
clockOpeAccuracy = _ClockOpeAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 4),
    _ClockOpeAccuracy_Type()
)
clockOpeAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeAccuracy.setStatus("mandatory")


class _ClockOpeSlaveLine1_Type(Integer32):
    """Custom type clockOpeSlaveLine1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(-1, -1),
    )


_ClockOpeSlaveLine1_Type.__name__ = "Integer32"
_ClockOpeSlaveLine1_Object = MibScalar
clockOpeSlaveLine1 = _ClockOpeSlaveLine1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 5),
    _ClockOpeSlaveLine1_Type()
)
clockOpeSlaveLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeSlaveLine1.setStatus("mandatory")


class _ClockOpeSlaveLine2_Type(Integer32):
    """Custom type clockOpeSlaveLine2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(-1, -1),
    )


_ClockOpeSlaveLine2_Type.__name__ = "Integer32"
_ClockOpeSlaveLine2_Object = MibScalar
clockOpeSlaveLine2 = _ClockOpeSlaveLine2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 6),
    _ClockOpeSlaveLine2_Type()
)
clockOpeSlaveLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeSlaveLine2.setStatus("mandatory")


class _ClockOpeSlaveLine3_Type(Integer32):
    """Custom type clockOpeSlaveLine3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(-1, -1),
    )


_ClockOpeSlaveLine3_Type.__name__ = "Integer32"
_ClockOpeSlaveLine3_Object = MibScalar
clockOpeSlaveLine3 = _ClockOpeSlaveLine3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 7),
    _ClockOpeSlaveLine3_Type()
)
clockOpeSlaveLine3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeSlaveLine3.setStatus("mandatory")


class _ClockOpeSlaveLine4_Type(Integer32):
    """Custom type clockOpeSlaveLine4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(-1, -1),
    )


_ClockOpeSlaveLine4_Type.__name__ = "Integer32"
_ClockOpeSlaveLine4_Object = MibScalar
clockOpeSlaveLine4 = _ClockOpeSlaveLine4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 1, 8),
    _ClockOpeSlaveLine4_Type()
)
clockOpeSlaveLine4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockOpeSlaveLine4.setStatus("mandatory")


class _ClockMode_Type(Integer32):
    """Custom type clockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ClockMode_Type.__name__ = "Integer32"
_ClockMode_Object = MibScalar
clockMode = _ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 2),
    _ClockMode_Type()
)
clockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockMode.setStatus("mandatory")


class _ClockAccuracy_Type(Integer32):
    """Custom type clockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(-1, -1),
    )


_ClockAccuracy_Type.__name__ = "Integer32"
_ClockAccuracy_Object = MibScalar
clockAccuracy = _ClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 3),
    _ClockAccuracy_Type()
)
clockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockAccuracy.setStatus("mandatory")
_ClockSlaveLine_Type = Integer32
_ClockSlaveLine_Object = MibScalar
clockSlaveLine = _ClockSlaveLine_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 4),
    _ClockSlaveLine_Type()
)
clockSlaveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine.setStatus("mandatory")
_ClockSlaveLine1_Type = Integer32
_ClockSlaveLine1_Object = MibScalar
clockSlaveLine1 = _ClockSlaveLine1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 5),
    _ClockSlaveLine1_Type()
)
clockSlaveLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine1.setStatus("mandatory")
_ClockSlaveLine1Status_Type = ClockSlaveLineStatus
_ClockSlaveLine1Status_Object = MibScalar
clockSlaveLine1Status = _ClockSlaveLine1Status_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 6),
    _ClockSlaveLine1Status_Type()
)
clockSlaveLine1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine1Status.setStatus("mandatory")
_ClockSlaveLine2_Type = Integer32
_ClockSlaveLine2_Object = MibScalar
clockSlaveLine2 = _ClockSlaveLine2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 7),
    _ClockSlaveLine2_Type()
)
clockSlaveLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine2.setStatus("mandatory")
_ClockSlaveLine2Status_Type = ClockSlaveLineStatus
_ClockSlaveLine2Status_Object = MibScalar
clockSlaveLine2Status = _ClockSlaveLine2Status_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 8),
    _ClockSlaveLine2Status_Type()
)
clockSlaveLine2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine2Status.setStatus("mandatory")
_ClockSlaveLine3_Type = Integer32
_ClockSlaveLine3_Object = MibScalar
clockSlaveLine3 = _ClockSlaveLine3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 9),
    _ClockSlaveLine3_Type()
)
clockSlaveLine3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine3.setStatus("mandatory")
_ClockSlaveLine3Status_Type = ClockSlaveLineStatus
_ClockSlaveLine3Status_Object = MibScalar
clockSlaveLine3Status = _ClockSlaveLine3Status_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 10),
    _ClockSlaveLine3Status_Type()
)
clockSlaveLine3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine3Status.setStatus("mandatory")
_ClockSlaveLine4_Type = Integer32
_ClockSlaveLine4_Object = MibScalar
clockSlaveLine4 = _ClockSlaveLine4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 11),
    _ClockSlaveLine4_Type()
)
clockSlaveLine4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine4.setStatus("mandatory")
_ClockSlaveLine4Status_Type = ClockSlaveLineStatus
_ClockSlaveLine4Status_Object = MibScalar
clockSlaveLine4Status = _ClockSlaveLine4Status_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 8, 12),
    _ClockSlaveLine4Status_Type()
)
clockSlaveLine4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSlaveLine4Status.setStatus("mandatory")
_Diag_ObjectIdentity = ObjectIdentity
diag = _Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 9)
)


class _DiagActionStatus_Type(Integer32):
    """Custom type diagActionStatus based on Integer32"""
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
        *(("allocate", 1),
          ("end", 4),
          ("execute", 3),
          ("free", 5),
          ("start", 2))
    )


_DiagActionStatus_Type.__name__ = "Integer32"
_DiagActionStatus_Object = MibScalar
diagActionStatus = _DiagActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 9, 1),
    _DiagActionStatus_Type()
)
diagActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagActionStatus.setStatus("mandatory")


class _DiagActionKind_Type(Integer32):
    """Custom type diagActionKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("slot", 3),
          ("switch", 1))
    )


_DiagActionKind_Type.__name__ = "Integer32"
_DiagActionKind_Object = MibScalar
diagActionKind = _DiagActionKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 9, 2),
    _DiagActionKind_Type()
)
diagActionKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagActionKind.setStatus("mandatory")


class _DiagPreCause_Type(Integer32):
    """Custom type diagPreCause based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("clkChgError", 7),
          ("diagnostics", 6),
          ("initializing", 8),
          ("notInstalled", 4),
          ("notSupport", 5),
          ("other", 1),
          ("parameterNotEnough", 3),
          ("sbyAccessError", 9),
          ("succeed", 2))
    )


_DiagPreCause_Type.__name__ = "Integer32"
_DiagPreCause_Object = MibScalar
diagPreCause = _DiagPreCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 9, 3),
    _DiagPreCause_Type()
)
diagPreCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagPreCause.setStatus("mandatory")


class _DiagCause_Type(Integer32):
    """Custom type diagCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1020004,
              1030004,
              1040007,
              1040107,
              1050005,
              1060010,
              1070002,
              1600201,
              1600202,
              1600203,
              1600204,
              1600205,
              1600206,
              1600207,
              1600208,
              1600301,
              1600302,
              1600303,
              1600304,
              1600401,
              1600402,
              1600403,
              1600501,
              1600502,
              1600503,
              1600504,
              1600505,
              1600601,
              1600602,
              1600603,
              1600604,
              1600605,
              1600606,
              1600607,
              1600608,
              1600609,
              1600701,
              1600702,
              1600703,
              1600704,
              1600705,
              1600706,
              1601101,
              2010002,
              2020003,
              2030003,
              2040008,
              2040009,
              2040010,
              2040011,
              2040012,
              2040013,
              2040014,
              2040015,
              2090006,
              3010002,
              3010102,
              3010202,
              3010302,
              3020012,
              3030002,
              3040003,
              3050003,
              3060003,
              3070004,
              3080004,
              3080104,
              3120004,
              3130001,
              3130101,
              3130201,
              3130301,
              3140005,
              3140105,
              3140205,
              3140305,
              3150001,
              3150002,
              3160001,
              3170001,
              3170101,
              3170201,
              3170301,
              3180001,
              3180101,
              3180201,
              3180301,
              3190001,
              3190002,
              3190003,
              3190004,
              3200001,
              3210003,
              3220004,
              3230003,
              3240001,
              3250001,
              3250002)
        )
    )
    namedValues = NamedValues(
        *(("diagNG-AAL1-SAR", 3200001),
          ("diagNG-ALARM", 3190001),
          ("diagNG-ASW-Register", 1600401),
          ("diagNG-ATOM-Buffer-OVF", 1600607),
          ("diagNG-BF", 1030004),
          ("diagNG-BMT", 1600402),
          ("diagNG-BackPressure", 1600608),
          ("diagNG-CFAD", 3050003),
          ("diagNG-CPU", 1070002),
          ("diagNG-CPU-BSN-Parity", 1600207),
          ("diagNG-CPU-Cash-Test", 1600206),
          ("diagNG-CPU-DRAM", 3250001),
          ("diagNG-CPU-DRAM-Partial-Write", 1600204),
          ("diagNG-CPU-LANCE-LoopBack", 1600208),
          ("diagNG-CPU-MM-Test", 1600203),
          ("diagNG-CPU-Memory-Machining", 1600205),
          ("diagNG-CPU-Register", 1600201),
          ("diagNG-CPU-Timer-Test", 1600202),
          ("diagNG-CPU-Tout", 3250002),
          ("diagNG-CU2INF", 3030002),
          ("diagNG-DCS-LCA", 3230003),
          ("diagNG-DI", 1060010),
          ("diagNG-DI-LoopBack", 1600702),
          ("diagNG-DI-Memory", 1600505),
          ("diagNG-DI-Register", 1600504),
          ("diagNG-DMAC-Register", 1600302),
          ("diagNG-ES-LoopBack", 1600601),
          ("diagNG-ES-Nto1-Test", 1600606),
          ("diagNG-ES-Other-Broadcast-LoopBack", 1600605),
          ("diagNG-ES-Other-LoopBack", 1600603),
          ("diagNG-ES-Own-Broadcast-LoopBack", 1600604),
          ("diagNG-ES-Own-LoopBack", 1600602),
          ("diagNG-ES0", 1040007),
          ("diagNG-ES1", 1040107),
          ("diagNG-FIFO-CTL", 3190004),
          ("diagNG-FPGA", 3070004),
          ("diagNG-FPGA-CE-DS1", 3210003),
          ("diagNG-FPGA-CE-E1", 3220004),
          ("diagNG-FR-SDRAM", 2090006),
          ("diagNG-FRAME", 3190002),
          ("diagNG-FRM0", 3080004),
          ("diagNG-FRM1", 3080104),
          ("diagNG-Failer-Detect", 1600403),
          ("diagNG-IBC-HT-i-SGRAM", 2040010),
          ("diagNG-IBC-RIRO-SGRAM", 2040009),
          ("diagNG-IBC-RIRO-SRAM", 2040011),
          ("diagNG-IBC-Register", 2040008),
          ("diagNG-IXB-Register", 2010002),
          ("diagNG-Illegal-Cell-Detect", 1600705),
          ("diagNG-LCA-Common", 3150001),
          ("diagNG-LCA-Separate", 3150002),
          ("diagNG-Local-Memory", 1600301),
          ("diagNG-MISCEMA-Register", 1600303),
          ("diagNG-MUX", 3020012),
          ("diagNG-OBC-BCI-BMT", 2040015),
          ("diagNG-OBC-CellBuffer", 2040013),
          ("diagNG-OBC-HT-o", 2040014),
          ("diagNG-OBC-Register", 2040012),
          ("diagNG-OXB-Register", 2020003),
          ("diagNG-PCMCIA-Register", 1601101),
          ("diagNG-PHY0", 3010002),
          ("diagNG-PHY1", 3010102),
          ("diagNG-PHY2", 3010202),
          ("diagNG-PHY3", 3010302),
          ("diagNG-PLD", 3060003),
          ("diagNG-PM4341A-0", 3170001),
          ("diagNG-PM4341A-1", 3170101),
          ("diagNG-PM4341A-2", 3170201),
          ("diagNG-PM4341A-3", 3170301),
          ("diagNG-PM6341-0", 3180001),
          ("diagNG-PM6341-1", 3180101),
          ("diagNG-PM6341-2", 3180201),
          ("diagNG-PM6341-3", 3180301),
          ("diagNG-PM7345-0", 3140005),
          ("diagNG-PM7345-1", 3140105),
          ("diagNG-PM7345-2", 3140205),
          ("diagNG-PM7345-3", 3140305),
          ("diagNG-RICEtoCell-Compete", 1600609),
          ("diagNG-S-UNI622", 3120004),
          ("diagNG-SAR", 1050005),
          ("diagNG-SAR-Control-Memory", 1600502),
          ("diagNG-SAR-LoopBack", 1600701),
          ("diagNG-SAR-Packet-Memory", 1600503),
          ("diagNG-SAR-Register", 1600501),
          ("diagNG-SARtoPacket-Compete", 1600706),
          ("diagNG-SC", 1020004),
          ("diagNG-SW-Other-LoopBack", 1600704),
          ("diagNG-SW-Own-LoopBack", 1600703),
          ("diagNG-TAC0", 3130001),
          ("diagNG-TAC1", 3130101),
          ("diagNG-TAC2", 3130201),
          ("diagNG-TAC3", 3130301),
          ("diagNG-TS-CTL", 3190003),
          ("diagNG-UCFAD2", 3160001),
          ("diagNG-UHT-Register", 2030003),
          ("diagNG-UNIC", 3040003),
          ("diagNG-WAC-021", 3240001),
          ("diagNG-XACK-Interrupt", 1600304),
          ("normal", 1))
    )


_DiagCause_Type.__name__ = "Integer32"
_DiagCause_Object = MibScalar
diagCause = _DiagCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 9, 4),
    _DiagCause_Type()
)
diagCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagCause.setStatus("mandatory")
_DiagParam1_Type = Integer32
_DiagParam1_Object = MibScalar
diagParam1 = _DiagParam1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 9, 5),
    _DiagParam1_Type()
)
diagParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagParam1.setStatus("mandatory")
_Pnni_ObjectIdentity = ObjectIdentity
pnni = _Pnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10)
)
_PnniNode_ObjectIdentity = ObjectIdentity
pnniNode = _PnniNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1)
)
_PnniNodeOpe_ObjectIdentity = ObjectIdentity
pnniNodeOpe = _PnniNodeOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 1)
)
_PnniNodeTable_Object = MibTable
pnniNodeTable = _PnniNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2)
)
if mibBuilder.loadTexts:
    pnniNodeTable.setStatus("mandatory")
_PnniNodeEntry_Object = MibTableRow
pnniNodeEntry = _PnniNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1)
)
pnniNodeEntry.setIndexNames(
    (0, "NEC-MIB", "pnniNodeLevel"),
)
if mibBuilder.loadTexts:
    pnniNodeEntry.setStatus("mandatory")
_PnniNodeLevel_Type = PnniLevel
_PnniNodeLevel_Object = MibTableColumn
pnniNodeLevel = _PnniNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 1),
    _PnniNodeLevel_Type()
)
pnniNodeLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniNodeLevel.setStatus("mandatory")
_PnniNodeId_Type = PnniNodeId
_PnniNodeId_Object = MibTableColumn
pnniNodeId = _PnniNodeId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 2),
    _PnniNodeId_Type()
)
pnniNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeId.setStatus("mandatory")
_PnniNodeAtmAddress_Type = PnniAtmAddr
_PnniNodeAtmAddress_Object = MibTableColumn
pnniNodeAtmAddress = _PnniNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 3),
    _PnniNodeAtmAddress_Type()
)
pnniNodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeAtmAddress.setStatus("mandatory")
_PnniNodePeerGroupId_Type = PnniPeerGroupId
_PnniNodePeerGroupId_Object = MibTableColumn
pnniNodePeerGroupId = _PnniNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 4),
    _PnniNodePeerGroupId_Type()
)
pnniNodePeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodePeerGroupId.setStatus("mandatory")
_PnniNodeRestrictedTransit_Type = TruthValue
_PnniNodeRestrictedTransit_Object = MibTableColumn
pnniNodeRestrictedTransit = _PnniNodeRestrictedTransit_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 5),
    _PnniNodeRestrictedTransit_Type()
)
pnniNodeRestrictedTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeRestrictedTransit.setStatus("mandatory")
_PnniNodeRestrictedBranching_Type = TruthValue
_PnniNodeRestrictedBranching_Object = MibTableColumn
pnniNodeRestrictedBranching = _PnniNodeRestrictedBranching_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 6),
    _PnniNodeRestrictedBranching_Type()
)
pnniNodeRestrictedBranching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeRestrictedBranching.setStatus("mandatory")


class _PnniNodeLeadershipPriority_Type(Integer32):
    """Custom type pnniNodeLeadershipPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PnniNodeLeadershipPriority_Type.__name__ = "Integer32"
_PnniNodeLeadershipPriority_Object = MibTableColumn
pnniNodeLeadershipPriority = _PnniNodeLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 10, 1, 2, 1, 7),
    _PnniNodeLeadershipPriority_Type()
)
pnniNodeLeadershipPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeLeadershipPriority.setStatus("mandatory")
_MatCmd_ObjectIdentity = ObjectIdentity
matCmd = _MatCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11)
)


class _MatCmdStatus_Type(Integer32):
    """Custom type matCmdStatus based on Integer32"""
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
        *(("active", 3),
          ("allocate", 1),
          ("free", 4),
          ("inActive", 2))
    )


_MatCmdStatus_Type.__name__ = "Integer32"
_MatCmdStatus_Object = MibScalar
matCmdStatus = _MatCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11, 1),
    _MatCmdStatus_Type()
)
matCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matCmdStatus.setStatus("mandatory")
_MatCmdInput_Type = DisplayString
_MatCmdInput_Object = MibScalar
matCmdInput = _MatCmdInput_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11, 2),
    _MatCmdInput_Type()
)
matCmdInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matCmdInput.setStatus("mandatory")
_MatCmdOutput_Type = DisplayString
_MatCmdOutput_Object = MibScalar
matCmdOutput = _MatCmdOutput_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11, 3),
    _MatCmdOutput_Type()
)
matCmdOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matCmdOutput.setStatus("mandatory")


class _MatCmdOutputType_Type(Integer32):
    """Custom type matCmdOutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continued", 2),
          ("interactive", 3),
          ("normal", 1))
    )


_MatCmdOutputType_Type.__name__ = "Integer32"
_MatCmdOutputType_Object = MibScalar
matCmdOutputType = _MatCmdOutputType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11, 4),
    _MatCmdOutputType_Type()
)
matCmdOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matCmdOutputType.setStatus("mandatory")


class _MatCmdStop_Type(Integer32):
    """Custom type matCmdStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("stop", 2))
    )


_MatCmdStop_Type.__name__ = "Integer32"
_MatCmdStop_Object = MibScalar
matCmdStop = _MatCmdStop_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11, 5),
    _MatCmdStop_Type()
)
matCmdStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matCmdStop.setStatus("mandatory")


class _MatCmdTimeOut_Type(Integer32):
    """Custom type matCmdTimeOut based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_MatCmdTimeOut_Type.__name__ = "Integer32"
_MatCmdTimeOut_Object = MibScalar
matCmdTimeOut = _MatCmdTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 9, 11, 6),
    _MatCmdTimeOut_Type()
)
matCmdTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matCmdTimeOut.setStatus("mandatory")
_M7_corporate_mib_ObjectIdentity = ObjectIdentity
m7_corporate_mib = _M7_corporate_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEC-MIB",
    **{"LinfFilterMaskVpi": LinfFilterMaskVpi,
       "LinfFilterMaskVci": LinfFilterMaskVci,
       "LinfCellMappingMode": LinfCellMappingMode,
       "LinfScramble": LinfScramble,
       "LinfLBO": LinfLBO,
       "LinfFrameMode": LinfFrameMode,
       "LinfMinVci": LinfMinVci,
       "LinfMaxVci": LinfMaxVci,
       "LinfService": LinfService,
       "LinfInterWorking": LinfInterWorking,
       "LinfVendor": LinfVendor,
       "LinfFractionalType": LinfFractionalType,
       "LinfFractionalSet": LinfFractionalSet,
       "LinfCasMode": LinfCasMode,
       "LinfCodingMode": LinfCodingMode,
       "LinfUnUsedParam": LinfUnUsedParam,
       "DstAtmAddressFormat": DstAtmAddressFormat,
       "DstAtmAddressLength": DstAtmAddressLength,
       "DstAtmAddress": DstAtmAddress,
       "DstPrimaryIfIndex": DstPrimaryIfIndex,
       "DstPrimaryVPI": DstPrimaryVPI,
       "DstSecondaryIfIndex": DstSecondaryIfIndex,
       "DstSecondaryVPI": DstSecondaryVPI,
       "ConnRouteOpeFailureCause": ConnRouteOpeFailureCause,
       "ConnSoftPvcSrcAtmAddressFormat": ConnSoftPvcSrcAtmAddressFormat,
       "ConnSoftPvcDstAtmAddressFormat": ConnSoftPvcDstAtmAddressFormat,
       "ConnSoftPvcEstSrcInfIndex": ConnSoftPvcEstSrcInfIndex,
       "ConnProfileIndex": ConnProfileIndex,
       "ConnFrProfileIndex": ConnFrProfileIndex,
       "ClockSlaveLineStatus": ClockSlaveLineStatus,
       "PnniAtmAddr": PnniAtmAddr,
       "PnniNodeId": PnniNodeId,
       "PnniPeerGroupId": PnniPeerGroupId,
       "PnniLevel": PnniLevel,
       "nec": nec,
       "necProduct": necProduct,
       "atomis": atomis,
       "m7-phase2": m7_phase2,
       "m7-corporate": m7_corporate,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "atomis-mib": atomis_mib,
       "m7-phase2-mib": m7_phase2_mib,
       "node": node,
       "nodeStatus": nodeStatus,
       "nodeStatusOperStatus": nodeStatusOperStatus,
       "nodeStatusStartTime": nodeStatusStartTime,
       "nodeStatusNodeId": nodeStatusNodeId,
       "nodeStatusSelfSystem": nodeStatusSelfSystem,
       "nodeStatusSwitchType": nodeStatusSwitchType,
       "nodeStatusFan": nodeStatusFan,
       "nodeStatusEnvironment": nodeStatusEnvironment,
       "nodeStatusTable": nodeStatusTable,
       "nodeStatusEntry": nodeStatusEntry,
       "nodeStatusIndex": nodeStatusIndex,
       "nodeStatusPower": nodeStatusPower,
       "nodeStatusSwitchMode": nodeStatusSwitchMode,
       "nodeStatusSwitch": nodeStatusSwitch,
       "nodePCMCIATable": nodePCMCIATable,
       "nodePCMCIAEntry": nodePCMCIAEntry,
       "nodePCMCIAIndex": nodePCMCIAIndex,
       "nodePCMCIAStatus": nodePCMCIAStatus,
       "nodePCMCIAType": nodePCMCIAType,
       "nodeOpe": nodeOpe,
       "nodeOpeSave": nodeOpeSave,
       "nodeOpeSaveResult": nodeOpeSaveResult,
       "nodeOpeCopy": nodeOpeCopy,
       "nodeOpeCopyResult": nodeOpeCopyResult,
       "nodeOpeReset": nodeOpeReset,
       "slot": slot,
       "slotIfConfTable": slotIfConfTable,
       "slotIfConfEntry": slotIfConfEntry,
       "slotIfConfIndex": slotIfConfIndex,
       "slotIfConfPhysType": slotIfConfPhysType,
       "slotIfConfRev": slotIfConfRev,
       "slotIfConfStatus": slotIfConfStatus,
       "slotIfConfBufferType": slotIfConfBufferType,
       "slotIfConfBufferRev": slotIfConfBufferRev,
       "slotIfConfReset": slotIfConfReset,
       "slotIfConfResetResult": slotIfConfResetResult,
       "linf": linf,
       "linfStatusTable": linfStatusTable,
       "linfStatusEntry": linfStatusEntry,
       "linfIndex": linfIndex,
       "linfStatus": linfStatus,
       "linfLoopBack": linfLoopBack,
       "linfConf": linfConf,
       "linfFwdAvailableBandWidth": linfFwdAvailableBandWidth,
       "linfBkwdAvailableBandWidth": linfBkwdAvailableBandWidth,
       "linfJ2Rate": linfJ2Rate,
       "linfCacFactor": linfCacFactor,
       "linfLoopBackCause": linfLoopBackCause,
       "linfBandWidth": linfBandWidth,
       "linfRecommendation": linfRecommendation,
       "linfUnassignedIdle": linfUnassignedIdle,
       "linfMaxActiveVpiBits": linfMaxActiveVpiBits,
       "linfMaxActiveVciBits": linfMaxActiveVciBits,
       "linfPhysType": linfPhysType,
       "linfParam1": linfParam1,
       "linfParam2": linfParam2,
       "linfParam3": linfParam3,
       "linfParam4": linfParam4,
       "linfParam5": linfParam5,
       "linfParam6": linfParam6,
       "linfParam7": linfParam7,
       "linfFifoConfTable": linfFifoConfTable,
       "linfFifoConfEntry": linfFifoConfEntry,
       "linfFifoConfifIndex": linfFifoConfifIndex,
       "linfFifoConfIndex": linfFifoConfIndex,
       "linfFifoConfStatus": linfFifoConfStatus,
       "linfFifoConfPeekRate": linfFifoConfPeekRate,
       "linfFifoConfSustainRate": linfFifoConfSustainRate,
       "linfFifoConfMaxBurstSize": linfFifoConfMaxBurstSize,
       "linfFifoConfRowStatus": linfFifoConfRowStatus,
       "conn": conn,
       "connPvc": connPvc,
       "connPvcOpe": connPvcOpe,
       "connPvcOpeLowPort": connPvcOpeLowPort,
       "connPvcOpeLowVpi": connPvcOpeLowVpi,
       "connPvcOpeLowVci": connPvcOpeLowVci,
       "connPvcOpeHighPort": connPvcOpeHighPort,
       "connPvcOpeHighVpi": connPvcOpeHighVpi,
       "connPvcOpeHighVci": connPvcOpeHighVci,
       "connPvcOpeTopology": connPvcOpeTopology,
       "connPvcOpeTrafficType": connPvcOpeTrafficType,
       "connPvcOpeStatus": connPvcOpeStatus,
       "connPvcOpeCause": connPvcOpeCause,
       "connPvcOpeLowFifoIndex": connPvcOpeLowFifoIndex,
       "connPvcOpeHighFifoIndex": connPvcOpeHighFifoIndex,
       "connPvcOpeLowParam1": connPvcOpeLowParam1,
       "connPvcOpeHighParam1": connPvcOpeHighParam1,
       "connPvcOpeLowParam2": connPvcOpeLowParam2,
       "connPvcOpeHighParam2": connPvcOpeHighParam2,
       "connPvcTable": connPvcTable,
       "connPvcEntry": connPvcEntry,
       "connPvcPort": connPvcPort,
       "connPvcVpi": connPvcVpi,
       "connPvcVci": connPvcVci,
       "connPvcDirection": connPvcDirection,
       "connPvcIndex": connPvcIndex,
       "connPvcContrastPort": connPvcContrastPort,
       "connPvcContrastVpi": connPvcContrastVpi,
       "connPvcContrastVci": connPvcContrastVci,
       "connPvcTopology": connPvcTopology,
       "connPvcTrafficType": connPvcTrafficType,
       "connPvcFifoIndex": connPvcFifoIndex,
       "connPvcContrastFifoIndex": connPvcContrastFifoIndex,
       "connPvcTrfConf": connPvcTrfConf,
       "connPvcTrfResult": connPvcTrfResult,
       "connPvcParam1": connPvcParam1,
       "connPvcContrastParam1": connPvcContrastParam1,
       "connPvcParam2": connPvcParam2,
       "connPvcContrastParam2": connPvcContrastParam2,
       "connPvcParam3": connPvcParam3,
       "connPvcContrastParam3": connPvcContrastParam3,
       "connPvcParam4": connPvcParam4,
       "connPvcContrastParam4": connPvcContrastParam4,
       "connPvcParam5": connPvcParam5,
       "connPvcContrastParam5": connPvcContrastParam5,
       "connPvcParam6": connPvcParam6,
       "connPvcContrastParam6": connPvcContrastParam6,
       "connPvcParam7": connPvcParam7,
       "connPvcContrastParam7": connPvcContrastParam7,
       "connPvcTrfTable": connPvcTrfTable,
       "connPvcTrfEntry": connPvcTrfEntry,
       "connPvcTrfInCells": connPvcTrfInCells,
       "connPvcTrfInCellsCounters": connPvcTrfInCellsCounters,
       "connPvcTrfOutCells": connPvcTrfOutCells,
       "connPvcTrfOutCellsCounters": connPvcTrfOutCellsCounters,
       "connPvcTrfInDropCells": connPvcTrfInDropCells,
       "connPvcTrfInDropCellsCounters": connPvcTrfInDropCellsCounters,
       "connConf": connConf,
       "connConfNode": connConfNode,
       "connConfNodePvcs": connConfNodePvcs,
       "connConfNodeSvcs": connConfNodeSvcs,
       "connConfNodeSoftPvcs": connConfNodeSoftPvcs,
       "connConfNodeTrafClear": connConfNodeTrafClear,
       "connConfNodeTrafs": connConfNodeTrafs,
       "connConfNodeCompleteSvcs": connConfNodeCompleteSvcs,
       "connConfNodeUnCompleteSvcs": connConfNodeUnCompleteSvcs,
       "connConfIfTable": connConfIfTable,
       "connConfIfEntry": connConfIfEntry,
       "connConfIfPvcs": connConfIfPvcs,
       "connConfIfSvcs": connConfIfSvcs,
       "connConfIfSoftPvcs": connConfIfSoftPvcs,
       "connRoute": connRoute,
       "connRouteOpe": connRouteOpe,
       "connRouteOpeStatus": connRouteOpeStatus,
       "connRouteOpeFailureCause": connRouteOpeFailureCause,
       "connRouteOpeAddressFormat": connRouteOpeAddressFormat,
       "connRouteOpeAddressLength": connRouteOpeAddressLength,
       "connRouteOpeAddress": connRouteOpeAddress,
       "connRouteOpePrimaryIfIndex": connRouteOpePrimaryIfIndex,
       "connRouteOpePrimaryVPI": connRouteOpePrimaryVPI,
       "connRouteOpeSecondaryIfIndex": connRouteOpeSecondaryIfIndex,
       "connRouteOpeSecondaryVPI": connRouteOpeSecondaryVPI,
       "connRouteOpeTertiaryIfIndex": connRouteOpeTertiaryIfIndex,
       "connRouteOpeTertiaryVPI": connRouteOpeTertiaryVPI,
       "connRouteOpeFourthryIfIndex": connRouteOpeFourthryIfIndex,
       "connRouteOpeFourthryVPI": connRouteOpeFourthryVPI,
       "connRouteOpeFifthryIfIndex": connRouteOpeFifthryIfIndex,
       "connRouteOpeFifthryVPI": connRouteOpeFifthryVPI,
       "connRouteOpeSixthryIfIndex": connRouteOpeSixthryIfIndex,
       "connRouteOpeSixthryVPI": connRouteOpeSixthryVPI,
       "connRouteOpeSeventhryIfIndex": connRouteOpeSeventhryIfIndex,
       "connRouteOpeSeventhryVPI": connRouteOpeSeventhryVPI,
       "connRouteTable": connRouteTable,
       "connRouteEntry": connRouteEntry,
       "connRouteType": connRouteType,
       "connRoutePrimaryIfIndex": connRoutePrimaryIfIndex,
       "connRoutePrimaryVPI": connRoutePrimaryVPI,
       "connRouteSecondaryIfIndex": connRouteSecondaryIfIndex,
       "connRouteSecondaryVPI": connRouteSecondaryVPI,
       "connRouteTertiaryIfIndex": connRouteTertiaryIfIndex,
       "connRouteTertiaryVPI": connRouteTertiaryVPI,
       "connRouteFourthryIfIndex": connRouteFourthryIfIndex,
       "connRouteFourthryVPI": connRouteFourthryVPI,
       "connRouteFifthryIfIndex": connRouteFifthryIfIndex,
       "connRouteFifthryVPI": connRouteFifthryVPI,
       "connRouteSixthryIfIndex": connRouteSixthryIfIndex,
       "connRouteSixthryVPI": connRouteSixthryVPI,
       "connRouteSeventhryIfIndex": connRouteSeventhryIfIndex,
       "connRouteSeventhryVPI": connRouteSeventhryVPI,
       "connRoutePrimaryStatus": connRoutePrimaryStatus,
       "connRoutePrimaryCause": connRoutePrimaryCause,
       "connRouteAtmAddressFormat": connRouteAtmAddressFormat,
       "connRouteAtmAddressLength": connRouteAtmAddressLength,
       "connRouteAtmAddress": connRouteAtmAddress,
       "connSoftPvcIndexNext": connSoftPvcIndexNext,
       "connSoftPvcTable": connSoftPvcTable,
       "connSoftPvcEntry": connSoftPvcEntry,
       "connSoftPvcIndex": connSoftPvcIndex,
       "connSoftPvcTopology": connSoftPvcTopology,
       "connSoftPvcTrafficType": connSoftPvcTrafficType,
       "connSoftPvcEndpointType": connSoftPvcEndpointType,
       "connSoftPvcRetry": connSoftPvcRetry,
       "connSoftPvcSrcAtmAddressFormat": connSoftPvcSrcAtmAddressFormat,
       "connSoftPvcSrcAtmAddressLength": connSoftPvcSrcAtmAddressLength,
       "connSoftPvcSrcAtmAddress": connSoftPvcSrcAtmAddress,
       "connSoftPvcSrcIfIndex": connSoftPvcSrcIfIndex,
       "connSoftPvcSrcVPI": connSoftPvcSrcVPI,
       "connSoftPvcSrcVCI": connSoftPvcSrcVCI,
       "connSoftPvcDstAtmAddressFormat": connSoftPvcDstAtmAddressFormat,
       "connSoftPvcDstAtmAddressLength": connSoftPvcDstAtmAddressLength,
       "connSoftPvcDstAtmAddress": connSoftPvcDstAtmAddress,
       "connSoftPvcDstIfIndex": connSoftPvcDstIfIndex,
       "connSoftPvcDstVPI": connSoftPvcDstVPI,
       "connSoftPvcDstVCI": connSoftPvcDstVCI,
       "connSoftPvcRowStatus": connSoftPvcRowStatus,
       "connSoftPvcCause": connSoftPvcCause,
       "connSoftPvcRestRetry": connSoftPvcRestRetry,
       "connSoftPvcSrcFifoIndex": connSoftPvcSrcFifoIndex,
       "connSoftPvcDstFifoIndex": connSoftPvcDstFifoIndex,
       "connSoftPvcNodeKind": connSoftPvcNodeKind,
       "connSoftPvcSrcParam1": connSoftPvcSrcParam1,
       "connSoftPvcDstParam1": connSoftPvcDstParam1,
       "connSoftPvcSrcParam2": connSoftPvcSrcParam2,
       "connSoftPvcDstParam2": connSoftPvcDstParam2,
       "connSoftPvcSrcParam3": connSoftPvcSrcParam3,
       "connSoftPvcDstParam3": connSoftPvcDstParam3,
       "connSoftPvcSrcParam4": connSoftPvcSrcParam4,
       "connSoftPvcDstParam4": connSoftPvcDstParam4,
       "connSoftPvcSrcParam5": connSoftPvcSrcParam5,
       "connSoftPvcDstParam5": connSoftPvcDstParam5,
       "connSoftPvcSrcParam6": connSoftPvcSrcParam6,
       "connSoftPvcDstParam6": connSoftPvcDstParam6,
       "connSoftPvcSrcParam7": connSoftPvcSrcParam7,
       "connSoftPvcDstParam7": connSoftPvcDstParam7,
       "connSoftPvcEstablishedSrcInfTable": connSoftPvcEstablishedSrcInfTable,
       "connSoftPvcEstablishedSrcInfEntry": connSoftPvcEstablishedSrcInfEntry,
       "connSoftPvcEstablishedSrcInf": connSoftPvcEstablishedSrcInf,
       "connSoftPvcEstSrcInfIndex": connSoftPvcEstSrcInfIndex,
       "connOam": connOam,
       "connOamOpe": connOamOpe,
       "connOamOpeStatus": connOamOpeStatus,
       "connOamOpeCause": connOamOpeCause,
       "connOamOpePoint": connOamOpePoint,
       "connOamOpeMode": connOamOpeMode,
       "connOamOpeSection": connOamOpeSection,
       "connOamOpePort1": connOamOpePort1,
       "connOamOpePort2": connOamOpePort2,
       "connOamOpeVpi1": connOamOpeVpi1,
       "connOamOpeVpi2": connOamOpeVpi2,
       "connOamOpeVci1": connOamOpeVci1,
       "connOamOpeVci2": connOamOpeVci2,
       "connOamTable": connOamTable,
       "connOamEntry": connOamEntry,
       "connOamPort": connOamPort,
       "connOamIndex": connOamIndex,
       "connOamContrastPort": connOamContrastPort,
       "connOamVpi": connOamVpi,
       "connOamContrastVpi": connOamContrastVpi,
       "connOamVci": connOamVci,
       "connOamContrastVci": connOamContrastVci,
       "connOamPoint": connOamPoint,
       "connOamMode": connOamMode,
       "connOamSection": connOamSection,
       "connOamStatus": connOamStatus,
       "connOamDefectType": connOamDefectType,
       "connOamDefectNodeID": connOamDefectNodeID,
       "connLoop": connLoop,
       "connLoopOpe": connLoopOpe,
       "connLoopOpeStatus": connLoopOpeStatus,
       "connLoopOpeCause": connLoopOpeCause,
       "connLoopOpeMode": connLoopOpeMode,
       "connLoopOpeBase": connLoopOpeBase,
       "connLoopOpeLoopBackPointNodeId": connLoopOpeLoopBackPointNodeId,
       "connLoopOpeCorrelationTag": connLoopOpeCorrelationTag,
       "connLoopOpeCount": connLoopOpeCount,
       "connLoopOpePort": connLoopOpePort,
       "connLoopOpeVpi": connLoopOpeVpi,
       "connLoopOpeVci": connLoopOpeVci,
       "connLoopOpeNormalEndCount": connLoopOpeNormalEndCount,
       "connLoopOpeAbnormalEndCount": connLoopOpeAbnormalEndCount,
       "connLoopOpeAbortCount": connLoopOpeAbortCount,
       "connLoopOpeLoopBackPointIdLength": connLoopOpeLoopBackPointIdLength,
       "connProfile": connProfile,
       "connProfileIndexNext": connProfileIndexNext,
       "connProfileTable": connProfileTable,
       "connProfileEntry": connProfileEntry,
       "connProfileIndex": connProfileIndex,
       "connProfileRowStatus": connProfileRowStatus,
       "connProfileCause": connProfileCause,
       "connProfileTrafficType": connProfileTrafficType,
       "connProfileName": connProfileName,
       "connProfileParam1": connProfileParam1,
       "connProfileParam2": connProfileParam2,
       "connProfileParam3": connProfileParam3,
       "connProfileParam4": connProfileParam4,
       "connProfileName2Index": connProfileName2Index,
       "connProfileName2IndexResult": connProfileName2IndexResult,
       "connSvcTable": connSvcTable,
       "connSvcEntry": connSvcEntry,
       "connSvcIndex": connSvcIndex,
       "connSvcInf": connSvcInf,
       "connCe": connCe,
       "connCeVc": connCeVc,
       "connCeVcTable": connCeVcTable,
       "connCeVcEntry": connCeVcEntry,
       "connCeVcPort": connCeVcPort,
       "connCeVcVci": connCeVcVci,
       "connCeVcRowStatus": connCeVcRowStatus,
       "connCeVcCause": connCeVcCause,
       "connCeVcDirection": connCeVcDirection,
       "connCeVcUpPartialFillSize": connCeVcUpPartialFillSize,
       "connCeVcDownPartialFillSize": connCeVcDownPartialFillSize,
       "connCeVcCondition": connCeVcCondition,
       "connCeVcCDVT": connCeVcCDVT,
       "connCeVcUpPCR": connCeVcUpPCR,
       "connCeVcDownPCR": connCeVcDownPCR,
       "connCeVcUpTimeSlot1": connCeVcUpTimeSlot1,
       "connCeVcDownTimeSlot1": connCeVcDownTimeSlot1,
       "connCeVcUpTimeSlot2": connCeVcUpTimeSlot2,
       "connCeVcDownTimeSlot2": connCeVcDownTimeSlot2,
       "connCeVcUpTimeSlot3": connCeVcUpTimeSlot3,
       "connCeVcDownTimeSlot3": connCeVcDownTimeSlot3,
       "connFr": connFr,
       "connFrDlci": connFrDlci,
       "connFrDlciTable": connFrDlciTable,
       "connFrDlciEntry": connFrDlciEntry,
       "connFrDlciPort": connFrDlciPort,
       "connFrDlciIndex": connFrDlciIndex,
       "connFrDlciRowStatus": connFrDlciRowStatus,
       "connFrDlciCause": connFrDlciCause,
       "connFrDlciFrProfile": connFrDlciFrProfile,
       "connFrDlciPCR": connFrDlciPCR,
       "connFrDlciSCR": connFrDlciSCR,
       "connFrDlciMBS": connFrDlciMBS,
       "connFrProfile": connFrProfile,
       "connFrProfileIndexNext": connFrProfileIndexNext,
       "connFrProfileTable": connFrProfileTable,
       "connFrProfileEntry": connFrProfileEntry,
       "connFrProfileIndex": connFrProfileIndex,
       "connFrProfileRowStatus": connFrProfileRowStatus,
       "connFrProfileCause": connFrProfileCause,
       "connFrProfileName": connFrProfileName,
       "connFrProfileInterworkingType": connFrProfileInterworkingType,
       "connFrProfileCIR": connFrProfileCIR,
       "connFrProfileDEtoCLP": connFrProfileDEtoCLP,
       "connFrProfileCLPValue": connFrProfileCLPValue,
       "connFrProfileCLPtoDE": connFrProfileCLPtoDE,
       "connFrProfileDEValue": connFrProfileDEValue,
       "connFrProfileCapsulationMode": connFrProfileCapsulationMode,
       "connFrProfileCongestionMode": connFrProfileCongestionMode,
       "connFrProfileName2Index": connFrProfileName2Index,
       "connFrProfileName2IndexResult": connFrProfileName2IndexResult,
       "perf": perf,
       "perfTrapEnable": perfTrapEnable,
       "perfIfTable": perfIfTable,
       "perfIfEntry": perfIfEntry,
       "perfIfIndex": perfIfIndex,
       "perfIfReceivedCells": perfIfReceivedCells,
       "perfIfReceivedCellsCounters": perfIfReceivedCellsCounters,
       "perfIfTransmittedCells": perfIfTransmittedCells,
       "perfIfTransmittedCellsCounters": perfIfTransmittedCellsCounters,
       "perfIfMisDelivdCells": perfIfMisDelivdCells,
       "perfIfMisDelivdCellsCounters": perfIfMisDelivdCellsCounters,
       "perfIfThresholdExcessCells": perfIfThresholdExcessCells,
       "perfIfThresholdExcessCellsCounters": perfIfThresholdExcessCellsCounters,
       "perfIfUpcErrorCells": perfIfUpcErrorCells,
       "perfIfUpcErrorCellsCounters": perfIfUpcErrorCellsCounters,
       "perfIfSlotTable": perfIfSlotTable,
       "perfIfSlotEntry": perfIfSlotEntry,
       "perfIfSlotReceivedCells": perfIfSlotReceivedCells,
       "perfIfSlotTransmittedCells": perfIfSlotTransmittedCells,
       "perfIfSlotInDropCells": perfIfSlotInDropCells,
       "perfIfSlotReceivedCellsCounters": perfIfSlotReceivedCellsCounters,
       "perfIfSlotTransmittedCellsCounters": perfIfSlotTransmittedCellsCounters,
       "perfIfSlotInDropCellsCounters": perfIfSlotInDropCellsCounters,
       "perfIfSlotHCThresholdExcessCells": perfIfSlotHCThresholdExcessCells,
       "perfIfSlotThresholdExcessCells": perfIfSlotThresholdExcessCells,
       "perfIfSlotHCUpcErrorCells": perfIfSlotHCUpcErrorCells,
       "perfIfSlotUpcErrorCells": perfIfSlotUpcErrorCells,
       "perfIfPhysTable": perfIfPhysTable,
       "perfIfPhysEntry": perfIfPhysEntry,
       "perfIfPhysPort": perfIfPhysPort,
       "perfIfPhysHCHecErorrs": perfIfPhysHCHecErorrs,
       "perfIfPhysHecErorrs": perfIfPhysHecErorrs,
       "perfIfPhysHCHecDropCells": perfIfPhysHCHecDropCells,
       "perfIfPhysHecDropCells": perfIfPhysHecDropCells,
       "perfIfPhysHCB1Errors": perfIfPhysHCB1Errors,
       "perfIfPhysB1Errors": perfIfPhysB1Errors,
       "perfIfPhysHCB2Errors": perfIfPhysHCB2Errors,
       "perfIfPhysB2Errors": perfIfPhysB2Errors,
       "perfIfPhysHCB3Errors": perfIfPhysHCB3Errors,
       "perfIfPhysB3Errors": perfIfPhysB3Errors,
       "perfIfPhysHCPathFEBEs": perfIfPhysHCPathFEBEs,
       "perfIfPhysPathFEBEs": perfIfPhysPathFEBEs,
       "perfIfPhysHCLineFEBEs": perfIfPhysHCLineFEBEs,
       "perfIfPhysLineFEBEs": perfIfPhysLineFEBEs,
       "perfIfPhysHCFramingErrors": perfIfPhysHCFramingErrors,
       "perfIfPhysFramingErrors": perfIfPhysFramingErrors,
       "perfIfPhysHCReceivedCells": perfIfPhysHCReceivedCells,
       "perfIfPhysReceivedCells": perfIfPhysReceivedCells,
       "perfIfPhysHCTransmittedCells": perfIfPhysHCTransmittedCells,
       "perfIfPhysTransmittedCells": perfIfPhysTransmittedCells,
       "perfIfPhysHCIdelUnassignedCells": perfIfPhysHCIdelUnassignedCells,
       "perfIfPhysIdelUnassignedCells": perfIfPhysIdelUnassignedCells,
       "perfIfPhysHCFEBEErrors": perfIfPhysHCFEBEErrors,
       "perfIfPhysFEBEErrors": perfIfPhysFEBEErrors,
       "perfIfPhysHCFEBEs": perfIfPhysHCFEBEs,
       "perfIfPhysFEBEs": perfIfPhysFEBEs,
       "perfIfPhysHCPathParityErrors": perfIfPhysHCPathParityErrors,
       "perfIfPhysPathParityErrors": perfIfPhysPathParityErrors,
       "perfIfPhysHCParityErrors": perfIfPhysHCParityErrors,
       "perfIfPhysParityErrors": perfIfPhysParityErrors,
       "perfIfPhysHCSEZs": perfIfPhysHCSEZs,
       "perfIfPhysSEZs": perfIfPhysSEZs,
       "perfIfPhysHCBitErrors": perfIfPhysHCBitErrors,
       "perfIfPhysBitErrors": perfIfPhysBitErrors,
       "perfIfPhysHCLcvErrors": perfIfPhysHCLcvErrors,
       "perfIfPhysLcvErrors": perfIfPhysLcvErrors,
       "perfIfPhysHCBip8Errors": perfIfPhysHCBip8Errors,
       "perfIfPhysBip8Errors": perfIfPhysBip8Errors,
       "perfIfPhysHCIecErrors": perfIfPhysHCIecErrors,
       "perfIfPhysIecErrors": perfIfPhysIecErrors,
       "perfIfPhysHCFramingPatternErrors": perfIfPhysHCFramingPatternErrors,
       "perfIfPhysFramingPatternErrors": perfIfPhysFramingPatternErrors,
       "perfIfPhysHCFramingBitErrors": perfIfPhysHCFramingBitErrors,
       "perfIfPhysFramingBitErrors": perfIfPhysFramingBitErrors,
       "perfIfPhysHCCrcErrors": perfIfPhysHCCrcErrors,
       "perfIfPhysCrcErrors": perfIfPhysCrcErrors,
       "scale": scale,
       "scaleStatus": scaleStatus,
       "scaleCause": scaleCause,
       "scaleDataType": scaleDataType,
       "scaleTarget": scaleTarget,
       "scaleFileName": scaleFileName,
       "scaleSwSide": scaleSwSide,
       "card": card,
       "cardStatusTable": cardStatusTable,
       "cardStatusEntry": cardStatusEntry,
       "cardStatusServerType": cardStatusServerType,
       "cardStatusRevision": cardStatusRevision,
       "cardStatusMateSlotNumber": cardStatusMateSlotNumber,
       "cardStatusMode": cardStatusMode,
       "cardStatusPriority": cardStatusPriority,
       "cardStatusAtmAddr": cardStatusAtmAddr,
       "cardStatusMateAtmAddr": cardStatusMateAtmAddr,
       "cardOpeTable": cardOpeTable,
       "cardOpeEntry": cardOpeEntry,
       "cardOpeReset": cardOpeReset,
       "cardOpeDiagnosis": cardOpeDiagnosis,
       "cardOpeSave": cardOpeSave,
       "cardOpeSaveResult": cardOpeSaveResult,
       "cardOpeCopy": cardOpeCopy,
       "cardOpeCopyResult": cardOpeCopyResult,
       "clock": clock,
       "clockOpe": clockOpe,
       "clockOpeStatus": clockOpeStatus,
       "clockOpeCause": clockOpeCause,
       "clockOpeMode": clockOpeMode,
       "clockOpeAccuracy": clockOpeAccuracy,
       "clockOpeSlaveLine1": clockOpeSlaveLine1,
       "clockOpeSlaveLine2": clockOpeSlaveLine2,
       "clockOpeSlaveLine3": clockOpeSlaveLine3,
       "clockOpeSlaveLine4": clockOpeSlaveLine4,
       "clockMode": clockMode,
       "clockAccuracy": clockAccuracy,
       "clockSlaveLine": clockSlaveLine,
       "clockSlaveLine1": clockSlaveLine1,
       "clockSlaveLine1Status": clockSlaveLine1Status,
       "clockSlaveLine2": clockSlaveLine2,
       "clockSlaveLine2Status": clockSlaveLine2Status,
       "clockSlaveLine3": clockSlaveLine3,
       "clockSlaveLine3Status": clockSlaveLine3Status,
       "clockSlaveLine4": clockSlaveLine4,
       "clockSlaveLine4Status": clockSlaveLine4Status,
       "diag": diag,
       "diagActionStatus": diagActionStatus,
       "diagActionKind": diagActionKind,
       "diagPreCause": diagPreCause,
       "diagCause": diagCause,
       "diagParam1": diagParam1,
       "pnni": pnni,
       "pnniNode": pnniNode,
       "pnniNodeOpe": pnniNodeOpe,
       "pnniNodeTable": pnniNodeTable,
       "pnniNodeEntry": pnniNodeEntry,
       "pnniNodeLevel": pnniNodeLevel,
       "pnniNodeId": pnniNodeId,
       "pnniNodeAtmAddress": pnniNodeAtmAddress,
       "pnniNodePeerGroupId": pnniNodePeerGroupId,
       "pnniNodeRestrictedTransit": pnniNodeRestrictedTransit,
       "pnniNodeRestrictedBranching": pnniNodeRestrictedBranching,
       "pnniNodeLeadershipPriority": pnniNodeLeadershipPriority,
       "matCmd": matCmd,
       "matCmdStatus": matCmdStatus,
       "matCmdInput": matCmdInput,
       "matCmdOutput": matCmdOutput,
       "matCmdOutputType": matCmdOutputType,
       "matCmdStop": matCmdStop,
       "matCmdTimeOut": matCmdTimeOut,
       "m7-corporate-mib": m7_corporate_mib}
)
