# SNMP MIB module (IB-CA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-CA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:13 2024
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

(IbPhysPort,
 infinibandMIB) = mibBuilder.importSymbols(
    "IB-TC-MIB",
    "IbPhysPort",
    "infinibandMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ibCaMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 117, 4)
)
ibCaMIB.setRevisions(
        ("2006-10-10 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbCaObjects_ObjectIdentity = ObjectIdentity
ibCaObjects = _IbCaObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 1)
)
_IbCaGeneralInfo_ObjectIdentity = ObjectIdentity
ibCaGeneralInfo = _IbCaGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 1, 1)
)
_IbCaGeneralInfoTable_Object = MibTable
ibCaGeneralInfoTable = _IbCaGeneralInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ibCaGeneralInfoTable.setStatus("current")
_IbCaGeneralInfoEntry_Object = MibTableRow
ibCaGeneralInfoEntry = _IbCaGeneralInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1)
)
ibCaGeneralInfoEntry.setIndexNames(
    (0, "IB-CA-MIB", "ibCaIndex"),
)
if mibBuilder.loadTexts:
    ibCaGeneralInfoEntry.setStatus("current")


class _IbCaIndex_Type(Unsigned32):
    """Custom type ibCaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbCaIndex_Type.__name__ = "Unsigned32"
_IbCaIndex_Object = MibTableColumn
ibCaIndex = _IbCaIndex_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 1),
    _IbCaIndex_Type()
)
ibCaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibCaIndex.setStatus("current")


class _IbCaType_Type(Integer32):
    """Custom type ibCaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hca", 2),
          ("tca", 3),
          ("unknown", 1))
    )


_IbCaType_Type.__name__ = "Integer32"
_IbCaType_Object = MibTableColumn
ibCaType = _IbCaType_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 2),
    _IbCaType_Type()
)
ibCaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaType.setStatus("current")


class _IbCaNodeGuid_Type(OctetString):
    """Custom type ibCaNodeGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbCaNodeGuid_Type.__name__ = "OctetString"
_IbCaNodeGuid_Object = MibTableColumn
ibCaNodeGuid = _IbCaNodeGuid_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 3),
    _IbCaNodeGuid_Type()
)
ibCaNodeGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaNodeGuid.setStatus("current")


class _IbCaNumPorts_Type(Unsigned32):
    """Custom type ibCaNumPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbCaNumPorts_Type.__name__ = "Unsigned32"
_IbCaNumPorts_Object = MibTableColumn
ibCaNumPorts = _IbCaNumPorts_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 4),
    _IbCaNumPorts_Type()
)
ibCaNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaNumPorts.setStatus("current")
_IbCaAttrInfo_ObjectIdentity = ObjectIdentity
ibCaAttrInfo = _IbCaAttrInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 1, 2)
)
_IbCaAttributeTable_Object = MibTable
ibCaAttributeTable = _IbCaAttributeTable_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ibCaAttributeTable.setStatus("current")
_IbCaAttributeEntry_Object = MibTableRow
ibCaAttributeEntry = _IbCaAttributeEntry_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1)
)
ibCaAttributeEntry.setIndexNames(
    (0, "IB-CA-MIB", "ibCaIndex"),
)
if mibBuilder.loadTexts:
    ibCaAttributeEntry.setStatus("current")
_IbCaHasReliableConnection_Type = TruthValue
_IbCaHasReliableConnection_Object = MibTableColumn
ibCaHasReliableConnection = _IbCaHasReliableConnection_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 1),
    _IbCaHasReliableConnection_Type()
)
ibCaHasReliableConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaHasReliableConnection.setStatus("current")
_IbCaHasUnreliableConnection_Type = TruthValue
_IbCaHasUnreliableConnection_Object = MibTableColumn
ibCaHasUnreliableConnection = _IbCaHasUnreliableConnection_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 2),
    _IbCaHasUnreliableConnection_Type()
)
ibCaHasUnreliableConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaHasUnreliableConnection.setStatus("current")
_IbCaHasReliableDatagram_Type = TruthValue
_IbCaHasReliableDatagram_Object = MibTableColumn
ibCaHasReliableDatagram = _IbCaHasReliableDatagram_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 3),
    _IbCaHasReliableDatagram_Type()
)
ibCaHasReliableDatagram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaHasReliableDatagram.setStatus("current")
_IbCaHasUnreliableDatagram_Type = TruthValue
_IbCaHasUnreliableDatagram_Object = MibTableColumn
ibCaHasUnreliableDatagram = _IbCaHasUnreliableDatagram_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 4),
    _IbCaHasUnreliableDatagram_Type()
)
ibCaHasUnreliableDatagram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaHasUnreliableDatagram.setStatus("current")
_IbCaSupportsAtomicOperations_Type = TruthValue
_IbCaSupportsAtomicOperations_Object = MibTableColumn
ibCaSupportsAtomicOperations = _IbCaSupportsAtomicOperations_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 5),
    _IbCaSupportsAtomicOperations_Type()
)
ibCaSupportsAtomicOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsAtomicOperations.setStatus("current")
_IbCaSupportsOtherOperations_Type = TruthValue
_IbCaSupportsOtherOperations_Object = MibTableColumn
ibCaSupportsOtherOperations = _IbCaSupportsOtherOperations_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 6),
    _IbCaSupportsOtherOperations_Type()
)
ibCaSupportsOtherOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsOtherOperations.setStatus("current")
_IbCaSupportsSolicitedEvents_Type = TruthValue
_IbCaSupportsSolicitedEvents_Object = MibTableColumn
ibCaSupportsSolicitedEvents = _IbCaSupportsSolicitedEvents_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 7),
    _IbCaSupportsSolicitedEvents_Type()
)
ibCaSupportsSolicitedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsSolicitedEvents.setStatus("current")


class _IbCaPathMtuSetSupport_Type(Integer32):
    """Custom type ibCaPathMtuSetSupport based on Integer32"""
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
        *(("mtu256", 1),
          ("mtu256n512", 2),
          ("mtu256n512n1024", 3),
          ("mtu256n512n1024n2048", 4),
          ("mtu256n512n1024n2048n4096", 5))
    )


_IbCaPathMtuSetSupport_Type.__name__ = "Integer32"
_IbCaPathMtuSetSupport_Object = MibTableColumn
ibCaPathMtuSetSupport = _IbCaPathMtuSetSupport_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 8),
    _IbCaPathMtuSetSupport_Type()
)
ibCaPathMtuSetSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaPathMtuSetSupport.setStatus("current")
_IbCaGenEndToEndFlowControl_Type = TruthValue
_IbCaGenEndToEndFlowControl_Object = MibTableColumn
ibCaGenEndToEndFlowControl = _IbCaGenEndToEndFlowControl_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 9),
    _IbCaGenEndToEndFlowControl_Type()
)
ibCaGenEndToEndFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaGenEndToEndFlowControl.setStatus("current")
_IbCaSupportsMulticast_Type = TruthValue
_IbCaSupportsMulticast_Object = MibTableColumn
ibCaSupportsMulticast = _IbCaSupportsMulticast_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 10),
    _IbCaSupportsMulticast_Type()
)
ibCaSupportsMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsMulticast.setStatus("current")
_IbCaSupportsAutoPathMigration_Type = TruthValue
_IbCaSupportsAutoPathMigration_Object = MibTableColumn
ibCaSupportsAutoPathMigration = _IbCaSupportsAutoPathMigration_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 11),
    _IbCaSupportsAutoPathMigration_Type()
)
ibCaSupportsAutoPathMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsAutoPathMigration.setStatus("current")
_IbCaSupportsMemoryProtection_Type = TruthValue
_IbCaSupportsMemoryProtection_Object = MibTableColumn
ibCaSupportsMemoryProtection = _IbCaSupportsMemoryProtection_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 12),
    _IbCaSupportsMemoryProtection_Type()
)
ibCaSupportsMemoryProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsMemoryProtection.setStatus("current")
_IbCaSupportsLoopback_Type = TruthValue
_IbCaSupportsLoopback_Object = MibTableColumn
ibCaSupportsLoopback = _IbCaSupportsLoopback_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 13),
    _IbCaSupportsLoopback_Type()
)
ibCaSupportsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsLoopback.setStatus("current")
_IbCaSupportsSubnetManager_Type = TruthValue
_IbCaSupportsSubnetManager_Object = MibTableColumn
ibCaSupportsSubnetManager = _IbCaSupportsSubnetManager_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 14),
    _IbCaSupportsSubnetManager_Type()
)
ibCaSupportsSubnetManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsSubnetManager.setStatus("current")
_IbCaPortAttrInfo_ObjectIdentity = ObjectIdentity
ibCaPortAttrInfo = _IbCaPortAttrInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 1, 3)
)
_IbCaPortAttributeTable_Object = MibTable
ibCaPortAttributeTable = _IbCaPortAttributeTable_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ibCaPortAttributeTable.setStatus("current")
_IbCaPortAttributeEntry_Object = MibTableRow
ibCaPortAttributeEntry = _IbCaPortAttributeEntry_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1)
)
ibCaPortAttributeEntry.setIndexNames(
    (0, "IB-CA-MIB", "ibCaIndex"),
    (0, "IB-CA-MIB", "ibCaPortIndex"),
)
if mibBuilder.loadTexts:
    ibCaPortAttributeEntry.setStatus("current")
_IbCaPortIndex_Type = IbPhysPort
_IbCaPortIndex_Object = MibTableColumn
ibCaPortIndex = _IbCaPortIndex_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 1),
    _IbCaPortIndex_Type()
)
ibCaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibCaPortIndex.setStatus("current")


class _IbCaPortGuid_Type(OctetString):
    """Custom type ibCaPortGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbCaPortGuid_Type.__name__ = "OctetString"
_IbCaPortGuid_Object = MibTableColumn
ibCaPortGuid = _IbCaPortGuid_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 2),
    _IbCaPortGuid_Type()
)
ibCaPortGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaPortGuid.setStatus("current")


class _IbCaPhysicalInterface_Type(Integer32):
    """Custom type ibCaPhysicalInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 3),
          ("cable", 1),
          ("fiber", 2))
    )


_IbCaPhysicalInterface_Type.__name__ = "Integer32"
_IbCaPhysicalInterface_Object = MibTableColumn
ibCaPhysicalInterface = _IbCaPhysicalInterface_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 3),
    _IbCaPhysicalInterface_Type()
)
ibCaPhysicalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaPhysicalInterface.setStatus("current")
_IbCaSupportsStaticRateControl_Type = TruthValue
_IbCaSupportsStaticRateControl_Object = MibTableColumn
ibCaSupportsStaticRateControl = _IbCaSupportsStaticRateControl_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 4),
    _IbCaSupportsStaticRateControl_Type()
)
ibCaSupportsStaticRateControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsStaticRateControl.setStatus("current")


class _IbCaInterpacketDelayValue_Type(Unsigned32):
    """Custom type ibCaInterpacketDelayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbCaInterpacketDelayValue_Type.__name__ = "Unsigned32"
_IbCaInterpacketDelayValue_Object = MibTableColumn
ibCaInterpacketDelayValue = _IbCaInterpacketDelayValue_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 5),
    _IbCaInterpacketDelayValue_Type()
)
ibCaInterpacketDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaInterpacketDelayValue.setStatus("current")
_IbCaSupportsMultipathing_Type = TruthValue
_IbCaSupportsMultipathing_Object = MibTableColumn
ibCaSupportsMultipathing = _IbCaSupportsMultipathing_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 6),
    _IbCaSupportsMultipathing_Type()
)
ibCaSupportsMultipathing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaSupportsMultipathing.setStatus("current")
_IbCaValidatesInPktDlid_Type = TruthValue
_IbCaValidatesInPktDlid_Object = MibTableColumn
ibCaValidatesInPktDlid = _IbCaValidatesInPktDlid_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 7),
    _IbCaValidatesInPktDlid_Type()
)
ibCaValidatesInPktDlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaValidatesInPktDlid.setStatus("current")


class _IbCaMaxGidsPerPort_Type(Unsigned32):
    """Custom type ibCaMaxGidsPerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbCaMaxGidsPerPort_Type.__name__ = "Unsigned32"
_IbCaMaxGidsPerPort_Object = MibTableColumn
ibCaMaxGidsPerPort = _IbCaMaxGidsPerPort_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 8),
    _IbCaMaxGidsPerPort_Type()
)
ibCaMaxGidsPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaMaxGidsPerPort.setStatus("current")
_IbCaPortGidTable_Object = MibTable
ibCaPortGidTable = _IbCaPortGidTable_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ibCaPortGidTable.setStatus("current")
_IbCaPortGidEntry_Object = MibTableRow
ibCaPortGidEntry = _IbCaPortGidEntry_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 2, 1)
)
ibCaPortGidEntry.setIndexNames(
    (0, "IB-CA-MIB", "ibCaIndex"),
    (0, "IB-CA-MIB", "ibCaPortIndex"),
    (0, "IB-CA-MIB", "ibCaPortGidIndex"),
)
if mibBuilder.loadTexts:
    ibCaPortGidEntry.setStatus("current")


class _IbCaPortGidIndex_Type(Unsigned32):
    """Custom type ibCaPortGidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbCaPortGidIndex_Type.__name__ = "Unsigned32"
_IbCaPortGidIndex_Object = MibTableColumn
ibCaPortGidIndex = _IbCaPortGidIndex_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 2, 1, 1),
    _IbCaPortGidIndex_Type()
)
ibCaPortGidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibCaPortGidIndex.setStatus("current")


class _IbCaPortGidValue_Type(OctetString):
    """Custom type ibCaPortGidValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbCaPortGidValue_Type.__name__ = "OctetString"
_IbCaPortGidValue_Object = MibTableColumn
ibCaPortGidValue = _IbCaPortGidValue_Object(
    (1, 3, 6, 1, 3, 117, 4, 1, 3, 2, 1, 2),
    _IbCaPortGidValue_Type()
)
ibCaPortGidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCaPortGidValue.setStatus("current")
_IbCaConformance_ObjectIdentity = ObjectIdentity
ibCaConformance = _IbCaConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 2)
)
_IbCaCompliances_ObjectIdentity = ObjectIdentity
ibCaCompliances = _IbCaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 2, 1)
)
_IbCaGroups_ObjectIdentity = ObjectIdentity
ibCaGroups = _IbCaGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 4, 2, 2)
)

# Managed Objects groups

ibCaGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 4, 2, 2, 1)
)
ibCaGeneralGroup.setObjects(
      *(("IB-CA-MIB", "ibCaType"),
        ("IB-CA-MIB", "ibCaNodeGuid"),
        ("IB-CA-MIB", "ibCaNumPorts"))
)
if mibBuilder.loadTexts:
    ibCaGeneralGroup.setStatus("current")

ibCaAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 4, 2, 2, 2)
)
ibCaAttrGroup.setObjects(
      *(("IB-CA-MIB", "ibCaHasReliableConnection"),
        ("IB-CA-MIB", "ibCaHasUnreliableConnection"),
        ("IB-CA-MIB", "ibCaHasReliableDatagram"),
        ("IB-CA-MIB", "ibCaHasUnreliableDatagram"),
        ("IB-CA-MIB", "ibCaSupportsAtomicOperations"),
        ("IB-CA-MIB", "ibCaSupportsOtherOperations"),
        ("IB-CA-MIB", "ibCaSupportsSolicitedEvents"),
        ("IB-CA-MIB", "ibCaPathMtuSetSupport"),
        ("IB-CA-MIB", "ibCaGenEndToEndFlowControl"),
        ("IB-CA-MIB", "ibCaSupportsMulticast"),
        ("IB-CA-MIB", "ibCaSupportsAutoPathMigration"),
        ("IB-CA-MIB", "ibCaSupportsMemoryProtection"),
        ("IB-CA-MIB", "ibCaSupportsLoopback"),
        ("IB-CA-MIB", "ibCaSupportsSubnetManager"))
)
if mibBuilder.loadTexts:
    ibCaAttrGroup.setStatus("current")

ibCaPortAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 4, 2, 2, 3)
)
ibCaPortAttrGroup.setObjects(
      *(("IB-CA-MIB", "ibCaPortGuid"),
        ("IB-CA-MIB", "ibCaPhysicalInterface"),
        ("IB-CA-MIB", "ibCaSupportsStaticRateControl"),
        ("IB-CA-MIB", "ibCaInterpacketDelayValue"),
        ("IB-CA-MIB", "ibCaSupportsMultipathing"),
        ("IB-CA-MIB", "ibCaValidatesInPktDlid"),
        ("IB-CA-MIB", "ibCaMaxGidsPerPort"))
)
if mibBuilder.loadTexts:
    ibCaPortAttrGroup.setStatus("current")

ibCaPortGidGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 4, 2, 2, 4)
)
ibCaPortGidGroup.setObjects(
    ("IB-CA-MIB", "ibCaPortGidValue")
)
if mibBuilder.loadTexts:
    ibCaPortGidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ibCaBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibCaBasicCompliance.setStatus(
        "current"
    )

ibCaFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibCaFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-CA-MIB",
    **{"ibCaMIB": ibCaMIB,
       "ibCaObjects": ibCaObjects,
       "ibCaGeneralInfo": ibCaGeneralInfo,
       "ibCaGeneralInfoTable": ibCaGeneralInfoTable,
       "ibCaGeneralInfoEntry": ibCaGeneralInfoEntry,
       "ibCaIndex": ibCaIndex,
       "ibCaType": ibCaType,
       "ibCaNodeGuid": ibCaNodeGuid,
       "ibCaNumPorts": ibCaNumPorts,
       "ibCaAttrInfo": ibCaAttrInfo,
       "ibCaAttributeTable": ibCaAttributeTable,
       "ibCaAttributeEntry": ibCaAttributeEntry,
       "ibCaHasReliableConnection": ibCaHasReliableConnection,
       "ibCaHasUnreliableConnection": ibCaHasUnreliableConnection,
       "ibCaHasReliableDatagram": ibCaHasReliableDatagram,
       "ibCaHasUnreliableDatagram": ibCaHasUnreliableDatagram,
       "ibCaSupportsAtomicOperations": ibCaSupportsAtomicOperations,
       "ibCaSupportsOtherOperations": ibCaSupportsOtherOperations,
       "ibCaSupportsSolicitedEvents": ibCaSupportsSolicitedEvents,
       "ibCaPathMtuSetSupport": ibCaPathMtuSetSupport,
       "ibCaGenEndToEndFlowControl": ibCaGenEndToEndFlowControl,
       "ibCaSupportsMulticast": ibCaSupportsMulticast,
       "ibCaSupportsAutoPathMigration": ibCaSupportsAutoPathMigration,
       "ibCaSupportsMemoryProtection": ibCaSupportsMemoryProtection,
       "ibCaSupportsLoopback": ibCaSupportsLoopback,
       "ibCaSupportsSubnetManager": ibCaSupportsSubnetManager,
       "ibCaPortAttrInfo": ibCaPortAttrInfo,
       "ibCaPortAttributeTable": ibCaPortAttributeTable,
       "ibCaPortAttributeEntry": ibCaPortAttributeEntry,
       "ibCaPortIndex": ibCaPortIndex,
       "ibCaPortGuid": ibCaPortGuid,
       "ibCaPhysicalInterface": ibCaPhysicalInterface,
       "ibCaSupportsStaticRateControl": ibCaSupportsStaticRateControl,
       "ibCaInterpacketDelayValue": ibCaInterpacketDelayValue,
       "ibCaSupportsMultipathing": ibCaSupportsMultipathing,
       "ibCaValidatesInPktDlid": ibCaValidatesInPktDlid,
       "ibCaMaxGidsPerPort": ibCaMaxGidsPerPort,
       "ibCaPortGidTable": ibCaPortGidTable,
       "ibCaPortGidEntry": ibCaPortGidEntry,
       "ibCaPortGidIndex": ibCaPortGidIndex,
       "ibCaPortGidValue": ibCaPortGidValue,
       "ibCaConformance": ibCaConformance,
       "ibCaCompliances": ibCaCompliances,
       "ibCaBasicCompliance": ibCaBasicCompliance,
       "ibCaFullCompliance": ibCaFullCompliance,
       "ibCaGroups": ibCaGroups,
       "ibCaGeneralGroup": ibCaGeneralGroup,
       "ibCaAttrGroup": ibCaAttrGroup,
       "ibCaPortAttrGroup": ibCaPortAttrGroup,
       "ibCaPortGidGroup": ibCaPortGidGroup}
)
