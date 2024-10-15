# SNMP MIB module (DELL-NETWORKING-OPENFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-OPENFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:57 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

dellNetOpenFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DataPathIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_OfSwitchObjects_ObjectIdentity = ObjectIdentity
ofSwitchObjects = _OfSwitchObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1)
)


class _OfSwitchId_Type(Unsigned32):
    """Custom type ofSwitchId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfSwitchId_Type.__name__ = "Unsigned32"
_OfSwitchId_Object = MibScalar
ofSwitchId = _OfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 1),
    _OfSwitchId_Type()
)
ofSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofSwitchId.setStatus("current")


class _OfManufacturerDesc_Type(DisplayString):
    """Custom type ofManufacturerDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OfManufacturerDesc_Type.__name__ = "DisplayString"
_OfManufacturerDesc_Object = MibScalar
ofManufacturerDesc = _OfManufacturerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 2),
    _OfManufacturerDesc_Type()
)
ofManufacturerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofManufacturerDesc.setStatus("current")


class _OfHardwareDesc_Type(DisplayString):
    """Custom type ofHardwareDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OfHardwareDesc_Type.__name__ = "DisplayString"
_OfHardwareDesc_Object = MibScalar
ofHardwareDesc = _OfHardwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 3),
    _OfHardwareDesc_Type()
)
ofHardwareDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofHardwareDesc.setStatus("current")


class _OfSoftwareDesc_Type(DisplayString):
    """Custom type ofSoftwareDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OfSoftwareDesc_Type.__name__ = "DisplayString"
_OfSoftwareDesc_Object = MibScalar
ofSoftwareDesc = _OfSoftwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 4),
    _OfSoftwareDesc_Type()
)
ofSoftwareDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofSoftwareDesc.setStatus("current")


class _OfSwitchSerialNo_Type(OctetString):
    """Custom type ofSwitchSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OfSwitchSerialNo_Type.__name__ = "OctetString"
_OfSwitchSerialNo_Object = MibScalar
ofSwitchSerialNo = _OfSwitchSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 5),
    _OfSwitchSerialNo_Type()
)
ofSwitchSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofSwitchSerialNo.setStatus("current")


class _OfSwitchVersion_Type(OctetString):
    """Custom type ofSwitchVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OfSwitchVersion_Type.__name__ = "OctetString"
_OfSwitchVersion_Object = MibScalar
ofSwitchVersion = _OfSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 6),
    _OfSwitchVersion_Type()
)
ofSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofSwitchVersion.setStatus("current")
_OfInstTable_Object = MibTable
ofInstTable = _OfInstTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7)
)
if mibBuilder.loadTexts:
    ofInstTable.setStatus("current")
_OfInstEntry_Object = MibTableRow
ofInstEntry = _OfInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1)
)
ofInstEntry.setIndexNames(
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"),
)
if mibBuilder.loadTexts:
    ofInstEntry.setStatus("current")


class _OfInstId_Type(Unsigned32):
    """Custom type ofInstId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfInstId_Type.__name__ = "Unsigned32"
_OfInstId_Object = MibTableColumn
ofInstId = _OfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 1),
    _OfInstId_Type()
)
ofInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofInstId.setStatus("current")


class _OfInstAdminState_Type(Integer32):
    """Custom type ofInstAdminState based on Integer32"""
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


_OfInstAdminState_Type.__name__ = "Integer32"
_OfInstAdminState_Object = MibTableColumn
ofInstAdminState = _OfInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 2),
    _OfInstAdminState_Type()
)
ofInstAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstAdminState.setStatus("current")


class _OfInstIntfType_Type(Integer32):
    """Custom type ofInstIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("port", 1),
          ("vlan", 2))
    )


_OfInstIntfType_Type.__name__ = "Integer32"
_OfInstIntfType_Object = MibTableColumn
ofInstIntfType = _OfInstIntfType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 3),
    _OfInstIntfType_Type()
)
ofInstIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstIntfType.setStatus("current")
_OfInstDataPathId_Type = DataPathIdentifier
_OfInstDataPathId_Object = MibTableColumn
ofInstDataPathId = _OfInstDataPathId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 4),
    _OfInstDataPathId_Type()
)
ofInstDataPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstDataPathId.setStatus("current")


class _OfInstConnectTimeout_Type(Unsigned32):
    """Custom type ofInstConnectTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfInstConnectTimeout_Type.__name__ = "Unsigned32"
_OfInstConnectTimeout_Object = MibTableColumn
ofInstConnectTimeout = _OfInstConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 5),
    _OfInstConnectTimeout_Type()
)
ofInstConnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstConnectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ofInstConnectTimeout.setUnits("seconds")


class _OfInstEchoReplyTimeout_Type(Unsigned32):
    """Custom type ofInstEchoReplyTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfInstEchoReplyTimeout_Type.__name__ = "Unsigned32"
_OfInstEchoReplyTimeout_Object = MibTableColumn
ofInstEchoReplyTimeout = _OfInstEchoReplyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 6),
    _OfInstEchoReplyTimeout_Type()
)
ofInstEchoReplyTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstEchoReplyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ofInstEchoReplyTimeout.setUnits("seconds")


class _OfInstEchoReqInterval_Type(Unsigned32):
    """Custom type ofInstEchoReqInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfInstEchoReqInterval_Type.__name__ = "Unsigned32"
_OfInstEchoReqInterval_Object = MibTableColumn
ofInstEchoReqInterval = _OfInstEchoReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 7),
    _OfInstEchoReqInterval_Type()
)
ofInstEchoReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstEchoReqInterval.setStatus("current")
_OfInstNumFlows_Type = Unsigned32
_OfInstNumFlows_Object = MibTableColumn
ofInstNumFlows = _OfInstNumFlows_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 8),
    _OfInstNumFlows_Type()
)
ofInstNumFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstNumFlows.setStatus("current")


class _OfInstSuppCapabilities_Type(Bits):
    """Custom type ofInstSuppCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("flow", 2),
          ("port", 0),
          ("table", 1))
    )

_OfInstSuppCapabilities_Type.__name__ = "Bits"
_OfInstSuppCapabilities_Object = MibTableColumn
ofInstSuppCapabilities = _OfInstSuppCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 9),
    _OfInstSuppCapabilities_Type()
)
ofInstSuppCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstSuppCapabilities.setStatus("current")


class _OfInstSuppActions_Type(Bits):
    """Custom type ofInstSuppActions based on Bits"""
    namedValues = NamedValues(
        *(("output", 0),
          ("set-dmac", 4),
          ("set-pcp", 2),
          ("set-smac", 3),
          ("set-tos", 5),
          ("set-vlan", 1))
    )

_OfInstSuppActions_Type.__name__ = "Bits"
_OfInstSuppActions_Object = MibTableColumn
ofInstSuppActions = _OfInstSuppActions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 10),
    _OfInstSuppActions_Type()
)
ofInstSuppActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofInstSuppActions.setStatus("current")
_OfCntlrTable_Object = MibTable
ofCntlrTable = _OfCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8)
)
if mibBuilder.loadTexts:
    ofCntlrTable.setStatus("current")
_OfCntlrEntry_Object = MibTableRow
ofCntlrEntry = _OfCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1)
)
ofCntlrEntry.setIndexNames(
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrId"),
)
if mibBuilder.loadTexts:
    ofCntlrEntry.setStatus("current")


class _OfCntlrId_Type(Unsigned32):
    """Custom type ofCntlrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfCntlrId_Type.__name__ = "Unsigned32"
_OfCntlrId_Object = MibTableColumn
ofCntlrId = _OfCntlrId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 1),
    _OfCntlrId_Type()
)
ofCntlrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofCntlrId.setStatus("current")
_OfCntlrAddrType_Type = InetAddressType
_OfCntlrAddrType_Object = MibTableColumn
ofCntlrAddrType = _OfCntlrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 2),
    _OfCntlrAddrType_Type()
)
ofCntlrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofCntlrAddrType.setStatus("current")


class _OfCntlrAddr_Type(InetAddress):
    """Custom type ofCntlrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_OfCntlrAddr_Type.__name__ = "InetAddress"
_OfCntlrAddr_Object = MibTableColumn
ofCntlrAddr = _OfCntlrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 3),
    _OfCntlrAddr_Type()
)
ofCntlrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofCntlrAddr.setStatus("current")
_OfCntlrPortNumber_Type = InetPortNumber
_OfCntlrPortNumber_Object = MibTableColumn
ofCntlrPortNumber = _OfCntlrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 4),
    _OfCntlrPortNumber_Type()
)
ofCntlrPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofCntlrPortNumber.setStatus("current")


class _OfCntlrProtocol_Type(Integer32):
    """Custom type ofCntlrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("tls", 1))
    )


_OfCntlrProtocol_Type.__name__ = "Integer32"
_OfCntlrProtocol_Object = MibTableColumn
ofCntlrProtocol = _OfCntlrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 5),
    _OfCntlrProtocol_Type()
)
ofCntlrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofCntlrProtocol.setStatus("current")


class _OfCntlrConState_Type(Integer32):
    """Custom type ofCntlrConState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_OfCntlrConState_Type.__name__ = "Integer32"
_OfCntlrConState_Object = MibTableColumn
ofCntlrConState = _OfCntlrConState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 6),
    _OfCntlrConState_Type()
)
ofCntlrConState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofCntlrConState.setStatus("current")
_OfPortTable_Object = MibTable
ofPortTable = _OfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9)
)
if mibBuilder.loadTexts:
    ofPortTable.setStatus("current")
_OfPortEntry_Object = MibTableRow
ofPortEntry = _OfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9, 1)
)
ofPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofPortIfIndex"),
)
if mibBuilder.loadTexts:
    ofPortEntry.setStatus("current")
_OfPortIfIndex_Type = InterfaceIndex
_OfPortIfIndex_Object = MibTableColumn
ofPortIfIndex = _OfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9, 1, 1),
    _OfPortIfIndex_Type()
)
ofPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofPortIfIndex.setStatus("current")


class _OfPortAssociationType_Type(Integer32):
    """Custom type ofPortAssociationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("instVlanPort", 2),
          ("instancePort", 1))
    )


_OfPortAssociationType_Type.__name__ = "Integer32"
_OfPortAssociationType_Object = MibTableColumn
ofPortAssociationType = _OfPortAssociationType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9, 1, 2),
    _OfPortAssociationType_Type()
)
ofPortAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofPortAssociationType.setStatus("current")
_OfVlanTable_Object = MibTable
ofVlanTable = _OfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10)
)
if mibBuilder.loadTexts:
    ofVlanTable.setStatus("current")
_OfVlanEntry_Object = MibTableRow
ofVlanEntry = _OfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10, 1)
)
ofVlanEntry.setIndexNames(
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofVlanIfIndex"),
)
if mibBuilder.loadTexts:
    ofVlanEntry.setStatus("current")
_OfVlanIfIndex_Type = InterfaceIndex
_OfVlanIfIndex_Object = MibTableColumn
ofVlanIfIndex = _OfVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10, 1, 1),
    _OfVlanIfIndex_Type()
)
ofVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofVlanIfIndex.setStatus("current")
_OfVlanId_Type = VlanId
_OfVlanId_Object = MibTableColumn
ofVlanId = _OfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10, 1, 2),
    _OfVlanId_Type()
)
ofVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofVlanId.setStatus("current")
_OfFlowTable_Object = MibTable
ofFlowTable = _OfFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11)
)
if mibBuilder.loadTexts:
    ofFlowTable.setStatus("current")
_OfFlowEntry_Object = MibTableRow
ofFlowEntry = _OfFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1)
)
ofFlowEntry.setIndexNames(
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowTblId"),
)
if mibBuilder.loadTexts:
    ofFlowEntry.setStatus("current")
_OfFlowId_Type = Unsigned32
_OfFlowId_Object = MibTableColumn
ofFlowId = _OfFlowId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 1),
    _OfFlowId_Type()
)
ofFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofFlowId.setStatus("current")
_OfFlowTblId_Type = Unsigned32
_OfFlowTblId_Object = MibTableColumn
ofFlowTblId = _OfFlowTblId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 2),
    _OfFlowTblId_Type()
)
ofFlowTblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofFlowTblId.setStatus("current")


class _OfFlowPriority_Type(Unsigned32):
    """Custom type ofFlowPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfFlowPriority_Type.__name__ = "Unsigned32"
_OfFlowPriority_Object = MibTableColumn
ofFlowPriority = _OfFlowPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 3),
    _OfFlowPriority_Type()
)
ofFlowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowPriority.setStatus("current")


class _OfFlowIdleTime_Type(Unsigned32):
    """Custom type ofFlowIdleTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfFlowIdleTime_Type.__name__ = "Unsigned32"
_OfFlowIdleTime_Object = MibTableColumn
ofFlowIdleTime = _OfFlowIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 4),
    _OfFlowIdleTime_Type()
)
ofFlowIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    ofFlowIdleTime.setUnits("seconds")


class _OfFlowHardTime_Type(Unsigned32):
    """Custom type ofFlowHardTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfFlowHardTime_Type.__name__ = "Unsigned32"
_OfFlowHardTime_Object = MibTableColumn
ofFlowHardTime = _OfFlowHardTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 5),
    _OfFlowHardTime_Type()
)
ofFlowHardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowHardTime.setStatus("current")
if mibBuilder.loadTexts:
    ofFlowHardTime.setUnits("seconds")
_OfFlowUpTime_Type = TimeTicks
_OfFlowUpTime_Object = MibTableColumn
ofFlowUpTime = _OfFlowUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 6),
    _OfFlowUpTime_Type()
)
ofFlowUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowUpTime.setStatus("current")


class _OfFlowCookie_Type(OctetString):
    """Custom type ofFlowCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OfFlowCookie_Type.__name__ = "OctetString"
_OfFlowCookie_Object = MibTableColumn
ofFlowCookie = _OfFlowCookie_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 7),
    _OfFlowCookie_Type()
)
ofFlowCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowCookie.setStatus("current")
_OfFlowPacketCount_Type = Counter64
_OfFlowPacketCount_Object = MibTableColumn
ofFlowPacketCount = _OfFlowPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 8),
    _OfFlowPacketCount_Type()
)
ofFlowPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowPacketCount.setStatus("current")
_OfFlowByteCount_Type = Counter64
_OfFlowByteCount_Object = MibTableColumn
ofFlowByteCount = _OfFlowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 9),
    _OfFlowByteCount_Type()
)
ofFlowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowByteCount.setStatus("current")
_OfFlowMatchParamsTable_Object = MibTable
ofFlowMatchParamsTable = _OfFlowMatchParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12)
)
if mibBuilder.loadTexts:
    ofFlowMatchParamsTable.setStatus("current")
_OfFlowMatchParamsEntry_Object = MibTableRow
ofFlowMatchParamsEntry = _OfFlowMatchParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ofFlowMatchParamsEntry.setStatus("current")


class _OfFlowMatchInPort_Type(OctetString):
    """Custom type ofFlowMatchInPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OfFlowMatchInPort_Type.__name__ = "OctetString"
_OfFlowMatchInPort_Object = MibTableColumn
ofFlowMatchInPort = _OfFlowMatchInPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 1),
    _OfFlowMatchInPort_Type()
)
ofFlowMatchInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchInPort.setStatus("current")


class _OfFlowMatchEtherSrcAddr_Type(OctetString):
    """Custom type ofFlowMatchEtherSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OfFlowMatchEtherSrcAddr_Type.__name__ = "OctetString"
_OfFlowMatchEtherSrcAddr_Object = MibTableColumn
ofFlowMatchEtherSrcAddr = _OfFlowMatchEtherSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 2),
    _OfFlowMatchEtherSrcAddr_Type()
)
ofFlowMatchEtherSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchEtherSrcAddr.setStatus("current")


class _OfFlowMatchEtherDstAddr_Type(OctetString):
    """Custom type ofFlowMatchEtherDstAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OfFlowMatchEtherDstAddr_Type.__name__ = "OctetString"
_OfFlowMatchEtherDstAddr_Object = MibTableColumn
ofFlowMatchEtherDstAddr = _OfFlowMatchEtherDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 3),
    _OfFlowMatchEtherDstAddr_Type()
)
ofFlowMatchEtherDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchEtherDstAddr.setStatus("current")


class _OfFlowMatchVlanId_Type(OctetString):
    """Custom type ofFlowMatchVlanId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OfFlowMatchVlanId_Type.__name__ = "OctetString"
_OfFlowMatchVlanId_Object = MibTableColumn
ofFlowMatchVlanId = _OfFlowMatchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 4),
    _OfFlowMatchVlanId_Type()
)
ofFlowMatchVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchVlanId.setStatus("current")


class _OfFlowMatchEthType_Type(OctetString):
    """Custom type ofFlowMatchEthType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OfFlowMatchEthType_Type.__name__ = "OctetString"
_OfFlowMatchEthType_Object = MibTableColumn
ofFlowMatchEthType = _OfFlowMatchEthType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 5),
    _OfFlowMatchEthType_Type()
)
ofFlowMatchEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchEthType.setStatus("current")


class _OfFlowMatchVlanPri_Type(OctetString):
    """Custom type ofFlowMatchVlanPri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_OfFlowMatchVlanPri_Type.__name__ = "OctetString"
_OfFlowMatchVlanPri_Object = MibTableColumn
ofFlowMatchVlanPri = _OfFlowMatchVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 6),
    _OfFlowMatchVlanPri_Type()
)
ofFlowMatchVlanPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchVlanPri.setStatus("current")


class _OfFlowMatchIpTos_Type(OctetString):
    """Custom type ofFlowMatchIpTos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_OfFlowMatchIpTos_Type.__name__ = "OctetString"
_OfFlowMatchIpTos_Object = MibTableColumn
ofFlowMatchIpTos = _OfFlowMatchIpTos_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 7),
    _OfFlowMatchIpTos_Type()
)
ofFlowMatchIpTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchIpTos.setStatus("current")


class _OfFlowMatchIpProto_Type(OctetString):
    """Custom type ofFlowMatchIpProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_OfFlowMatchIpProto_Type.__name__ = "OctetString"
_OfFlowMatchIpProto_Object = MibTableColumn
ofFlowMatchIpProto = _OfFlowMatchIpProto_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 8),
    _OfFlowMatchIpProto_Type()
)
ofFlowMatchIpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchIpProto.setStatus("current")


class _OfFlowMatchIpSrcAddr_Type(OctetString):
    """Custom type ofFlowMatchIpSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OfFlowMatchIpSrcAddr_Type.__name__ = "OctetString"
_OfFlowMatchIpSrcAddr_Object = MibTableColumn
ofFlowMatchIpSrcAddr = _OfFlowMatchIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 9),
    _OfFlowMatchIpSrcAddr_Type()
)
ofFlowMatchIpSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchIpSrcAddr.setStatus("current")


class _OfFlowMatchIpDestAddr_Type(OctetString):
    """Custom type ofFlowMatchIpDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OfFlowMatchIpDestAddr_Type.__name__ = "OctetString"
_OfFlowMatchIpDestAddr_Object = MibTableColumn
ofFlowMatchIpDestAddr = _OfFlowMatchIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 10),
    _OfFlowMatchIpDestAddr_Type()
)
ofFlowMatchIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchIpDestAddr.setStatus("current")


class _OfFlowMatchTpSrcPort_Type(OctetString):
    """Custom type ofFlowMatchTpSrcPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OfFlowMatchTpSrcPort_Type.__name__ = "OctetString"
_OfFlowMatchTpSrcPort_Object = MibTableColumn
ofFlowMatchTpSrcPort = _OfFlowMatchTpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 11),
    _OfFlowMatchTpSrcPort_Type()
)
ofFlowMatchTpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchTpSrcPort.setStatus("current")


class _OfFlowMatchTpDstPort_Type(OctetString):
    """Custom type ofFlowMatchTpDstPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OfFlowMatchTpDstPort_Type.__name__ = "OctetString"
_OfFlowMatchTpDstPort_Object = MibTableColumn
ofFlowMatchTpDstPort = _OfFlowMatchTpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 12),
    _OfFlowMatchTpDstPort_Type()
)
ofFlowMatchTpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowMatchTpDstPort.setStatus("current")
_OfFlowActionTable_Object = MibTable
ofFlowActionTable = _OfFlowActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13)
)
if mibBuilder.loadTexts:
    ofFlowActionTable.setStatus("current")
_OfFlowActionEntry_Object = MibTableRow
ofFlowActionEntry = _OfFlowActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1)
)
ofFlowActionEntry.setIndexNames(
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowTblId"),
    (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionId"),
)
if mibBuilder.loadTexts:
    ofFlowActionEntry.setStatus("current")
_OfFlowActionId_Type = Unsigned32
_OfFlowActionId_Object = MibTableColumn
ofFlowActionId = _OfFlowActionId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 1),
    _OfFlowActionId_Type()
)
ofFlowActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofFlowActionId.setStatus("current")


class _OfFlowActionType_Type(Integer32):
    """Custom type ofFlowActionType based on Integer32"""
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
              65535)
        )
    )
    namedValues = NamedValues(
        *(("outToQueue", 12),
          ("outToSwitchPort", 1),
          ("setDlDst", 6),
          ("setDlSrc", 5),
          ("setNetworkDst", 8),
          ("setNetworkSrc", 7),
          ("setNetworkTos", 9),
          ("setTpDest", 11),
          ("setTpSrc", 10),
          ("setVlanPcp", 3),
          ("setVlanVid", 2),
          ("stripVlan", 4),
          ("vendor", 65535))
    )


_OfFlowActionType_Type.__name__ = "Integer32"
_OfFlowActionType_Object = MibTableColumn
ofFlowActionType = _OfFlowActionType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 2),
    _OfFlowActionType_Type()
)
ofFlowActionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionType.setStatus("current")
_OfFlowActionSrcMac_Type = MacAddress
_OfFlowActionSrcMac_Object = MibTableColumn
ofFlowActionSrcMac = _OfFlowActionSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 3),
    _OfFlowActionSrcMac_Type()
)
ofFlowActionSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionSrcMac.setStatus("current")
_OfFlowActionDstMac_Type = MacAddress
_OfFlowActionDstMac_Object = MibTableColumn
ofFlowActionDstMac = _OfFlowActionDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 4),
    _OfFlowActionDstMac_Type()
)
ofFlowActionDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionDstMac.setStatus("current")
_OfFlowActionPortIndex_Type = InterfaceIndex
_OfFlowActionPortIndex_Object = MibTableColumn
ofFlowActionPortIndex = _OfFlowActionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 5),
    _OfFlowActionPortIndex_Type()
)
ofFlowActionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionPortIndex.setStatus("current")
_OfFlowActionVlanId_Type = VlanId
_OfFlowActionVlanId_Object = MibTableColumn
ofFlowActionVlanId = _OfFlowActionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 6),
    _OfFlowActionVlanId_Type()
)
ofFlowActionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionVlanId.setStatus("current")


class _OfFlowActionMaxLen_Type(Unsigned32):
    """Custom type ofFlowActionMaxLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OfFlowActionMaxLen_Type.__name__ = "Unsigned32"
_OfFlowActionMaxLen_Object = MibTableColumn
ofFlowActionMaxLen = _OfFlowActionMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 7),
    _OfFlowActionMaxLen_Type()
)
ofFlowActionMaxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionMaxLen.setStatus("current")


class _OfFlowActionVlanPcp_Type(Unsigned32):
    """Custom type ofFlowActionVlanPcp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfFlowActionVlanPcp_Type.__name__ = "Unsigned32"
_OfFlowActionVlanPcp_Object = MibTableColumn
ofFlowActionVlanPcp = _OfFlowActionVlanPcp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 8),
    _OfFlowActionVlanPcp_Type()
)
ofFlowActionVlanPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionVlanPcp.setStatus("current")


class _OfFlowActionNWTos_Type(Unsigned32):
    """Custom type ofFlowActionNWTos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OfFlowActionNWTos_Type.__name__ = "Unsigned32"
_OfFlowActionNWTos_Object = MibTableColumn
ofFlowActionNWTos = _OfFlowActionNWTos_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 9),
    _OfFlowActionNWTos_Type()
)
ofFlowActionNWTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofFlowActionNWTos.setStatus("current")
_OfSwitchMibConformance_ObjectIdentity = ObjectIdentity
ofSwitchMibConformance = _OfSwitchMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14)
)
_OfSwitchMibCompliances_ObjectIdentity = ObjectIdentity
ofSwitchMibCompliances = _OfSwitchMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 1)
)
_OfSwitchMibGroups_ObjectIdentity = ObjectIdentity
ofSwitchMibGroups = _OfSwitchMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2)
)
_OfSwitchNotification_ObjectIdentity = ObjectIdentity
ofSwitchNotification = _OfSwitchNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 2)
)
_OfSwitchNotifications_ObjectIdentity = ObjectIdentity
ofSwitchNotifications = _OfSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 0)
)
_OfSwitchNotifyVariable_ObjectIdentity = ObjectIdentity
ofSwitchNotifyVariable = _OfSwitchNotifyVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 1)
)


class _OfSwitchFlowTableSrc_Type(Integer32):
    """Custom type ofSwitchFlowTableSrc based on Integer32"""
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
        *(("dmac", 3),
          ("ifp", 1),
          ("lb", 5),
          ("route", 4),
          ("vlan", 2))
    )


_OfSwitchFlowTableSrc_Type.__name__ = "Integer32"
_OfSwitchFlowTableSrc_Object = MibScalar
ofSwitchFlowTableSrc = _OfSwitchFlowTableSrc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 1, 1),
    _OfSwitchFlowTableSrc_Type()
)
ofSwitchFlowTableSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ofSwitchFlowTableSrc.setStatus("current")
ofFlowEntry.registerAugmentions(
    ("DELL-NETWORKING-OPENFLOW-MIB",
     "ofFlowMatchParamsEntry")
)
ofFlowMatchParamsEntry.setIndexNames(*ofFlowEntry.getIndexNames())

# Managed Objects groups

ofSwitchScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 1)
)
ofSwitchScalarGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchId"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofManufacturerDesc"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofHardwareDesc"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofSoftwareDesc"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchSerialNo"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchVersion"))
)
if mibBuilder.loadTexts:
    ofSwitchScalarGroup.setStatus("current")

ofInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 2)
)
ofInstanceGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofInstAdminState"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstIntfType"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstDataPathId"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstConnectTimeout"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstEchoReplyTimeout"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstEchoReqInterval"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstNumFlows"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstSuppCapabilities"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstSuppActions"))
)
if mibBuilder.loadTexts:
    ofInstanceGroup.setStatus("current")

ofControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 3)
)
ofControllerGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrAddrType"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrAddr"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrPortNumber"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrProtocol"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrConState"))
)
if mibBuilder.loadTexts:
    ofControllerGroup.setStatus("current")

ofPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 4)
)
ofPortGroup.setObjects(
    ("DELL-NETWORKING-OPENFLOW-MIB", "ofPortAssociationType")
)
if mibBuilder.loadTexts:
    ofPortGroup.setStatus("current")

ofVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 5)
)
ofVlanGroup.setObjects(
    ("DELL-NETWORKING-OPENFLOW-MIB", "ofVlanId")
)
if mibBuilder.loadTexts:
    ofVlanGroup.setStatus("current")

ofFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 6)
)
ofFlowGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowPriority"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowIdleTime"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowHardTime"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowUpTime"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowCookie"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowPacketCount"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowByteCount"))
)
if mibBuilder.loadTexts:
    ofFlowGroup.setStatus("current")

ofFlowMatchParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 7)
)
ofFlowMatchParamsGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchInPort"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchEtherSrcAddr"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchEtherDstAddr"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchVlanId"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchEthType"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchVlanPri"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpTos"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpProto"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpSrcAddr"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpDestAddr"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchTpSrcPort"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchTpDstPort"))
)
if mibBuilder.loadTexts:
    ofFlowMatchParamsGroup.setStatus("current")

ofFlowActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 8)
)
ofFlowActionGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionType"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionSrcMac"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionDstMac"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionPortIndex"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionVlanId"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionMaxLen"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionVlanPcp"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionNWTos"))
)
if mibBuilder.loadTexts:
    ofFlowActionGroup.setStatus("current")


# Notification objects

ofSwitchCntlrSessionStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 0, 1)
)
ofSwitchCntlrSessionStatusChanged.setObjects(
    ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrConState")
)
if mibBuilder.loadTexts:
    ofSwitchCntlrSessionStatusChanged.setStatus(
        "current"
    )

ofSwitchFlowTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 0, 2)
)
ofSwitchFlowTableFull.setObjects(
    ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchFlowTableSrc")
)
if mibBuilder.loadTexts:
    ofSwitchFlowTableFull.setStatus(
        "current"
    )


# Notifications groups

ofSwitchMibNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 9)
)
ofSwitchMibNotificationsGroup.setObjects(
      *(("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchCntlrSessionStatusChanged"),
        ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchFlowTableFull"))
)
if mibBuilder.loadTexts:
    ofSwitchMibNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ofSwitchMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ofSwitchMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-OPENFLOW-MIB",
    **{"DataPathIdentifier": DataPathIdentifier,
       "dellNetOpenFlow": dellNetOpenFlow,
       "ofSwitchObjects": ofSwitchObjects,
       "ofSwitchId": ofSwitchId,
       "ofManufacturerDesc": ofManufacturerDesc,
       "ofHardwareDesc": ofHardwareDesc,
       "ofSoftwareDesc": ofSoftwareDesc,
       "ofSwitchSerialNo": ofSwitchSerialNo,
       "ofSwitchVersion": ofSwitchVersion,
       "ofInstTable": ofInstTable,
       "ofInstEntry": ofInstEntry,
       "ofInstId": ofInstId,
       "ofInstAdminState": ofInstAdminState,
       "ofInstIntfType": ofInstIntfType,
       "ofInstDataPathId": ofInstDataPathId,
       "ofInstConnectTimeout": ofInstConnectTimeout,
       "ofInstEchoReplyTimeout": ofInstEchoReplyTimeout,
       "ofInstEchoReqInterval": ofInstEchoReqInterval,
       "ofInstNumFlows": ofInstNumFlows,
       "ofInstSuppCapabilities": ofInstSuppCapabilities,
       "ofInstSuppActions": ofInstSuppActions,
       "ofCntlrTable": ofCntlrTable,
       "ofCntlrEntry": ofCntlrEntry,
       "ofCntlrId": ofCntlrId,
       "ofCntlrAddrType": ofCntlrAddrType,
       "ofCntlrAddr": ofCntlrAddr,
       "ofCntlrPortNumber": ofCntlrPortNumber,
       "ofCntlrProtocol": ofCntlrProtocol,
       "ofCntlrConState": ofCntlrConState,
       "ofPortTable": ofPortTable,
       "ofPortEntry": ofPortEntry,
       "ofPortIfIndex": ofPortIfIndex,
       "ofPortAssociationType": ofPortAssociationType,
       "ofVlanTable": ofVlanTable,
       "ofVlanEntry": ofVlanEntry,
       "ofVlanIfIndex": ofVlanIfIndex,
       "ofVlanId": ofVlanId,
       "ofFlowTable": ofFlowTable,
       "ofFlowEntry": ofFlowEntry,
       "ofFlowId": ofFlowId,
       "ofFlowTblId": ofFlowTblId,
       "ofFlowPriority": ofFlowPriority,
       "ofFlowIdleTime": ofFlowIdleTime,
       "ofFlowHardTime": ofFlowHardTime,
       "ofFlowUpTime": ofFlowUpTime,
       "ofFlowCookie": ofFlowCookie,
       "ofFlowPacketCount": ofFlowPacketCount,
       "ofFlowByteCount": ofFlowByteCount,
       "ofFlowMatchParamsTable": ofFlowMatchParamsTable,
       "ofFlowMatchParamsEntry": ofFlowMatchParamsEntry,
       "ofFlowMatchInPort": ofFlowMatchInPort,
       "ofFlowMatchEtherSrcAddr": ofFlowMatchEtherSrcAddr,
       "ofFlowMatchEtherDstAddr": ofFlowMatchEtherDstAddr,
       "ofFlowMatchVlanId": ofFlowMatchVlanId,
       "ofFlowMatchEthType": ofFlowMatchEthType,
       "ofFlowMatchVlanPri": ofFlowMatchVlanPri,
       "ofFlowMatchIpTos": ofFlowMatchIpTos,
       "ofFlowMatchIpProto": ofFlowMatchIpProto,
       "ofFlowMatchIpSrcAddr": ofFlowMatchIpSrcAddr,
       "ofFlowMatchIpDestAddr": ofFlowMatchIpDestAddr,
       "ofFlowMatchTpSrcPort": ofFlowMatchTpSrcPort,
       "ofFlowMatchTpDstPort": ofFlowMatchTpDstPort,
       "ofFlowActionTable": ofFlowActionTable,
       "ofFlowActionEntry": ofFlowActionEntry,
       "ofFlowActionId": ofFlowActionId,
       "ofFlowActionType": ofFlowActionType,
       "ofFlowActionSrcMac": ofFlowActionSrcMac,
       "ofFlowActionDstMac": ofFlowActionDstMac,
       "ofFlowActionPortIndex": ofFlowActionPortIndex,
       "ofFlowActionVlanId": ofFlowActionVlanId,
       "ofFlowActionMaxLen": ofFlowActionMaxLen,
       "ofFlowActionVlanPcp": ofFlowActionVlanPcp,
       "ofFlowActionNWTos": ofFlowActionNWTos,
       "ofSwitchMibConformance": ofSwitchMibConformance,
       "ofSwitchMibCompliances": ofSwitchMibCompliances,
       "ofSwitchMibCompliance": ofSwitchMibCompliance,
       "ofSwitchMibGroups": ofSwitchMibGroups,
       "ofSwitchScalarGroup": ofSwitchScalarGroup,
       "ofInstanceGroup": ofInstanceGroup,
       "ofControllerGroup": ofControllerGroup,
       "ofPortGroup": ofPortGroup,
       "ofVlanGroup": ofVlanGroup,
       "ofFlowGroup": ofFlowGroup,
       "ofFlowMatchParamsGroup": ofFlowMatchParamsGroup,
       "ofFlowActionGroup": ofFlowActionGroup,
       "ofSwitchMibNotificationsGroup": ofSwitchMibNotificationsGroup,
       "ofSwitchNotification": ofSwitchNotification,
       "ofSwitchNotifications": ofSwitchNotifications,
       "ofSwitchCntlrSessionStatusChanged": ofSwitchCntlrSessionStatusChanged,
       "ofSwitchFlowTableFull": ofSwitchFlowTableFull,
       "ofSwitchNotifyVariable": ofSwitchNotifyVariable,
       "ofSwitchFlowTableSrc": ofSwitchFlowTableSrc}
)
