# SNMP MIB module (INTEGRATED-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEGRATED-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:21 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

intSrv = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SessionNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Protocol(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class SessionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class Port(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )



class MessageSize(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class BitRate(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class BurstSize(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class QosService(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("controlledLoad", 5),
          ("guaranteedDelay", 2))
    )



# MIB Managed Objects in the order of their OIDs

_IntSrvObjects_ObjectIdentity = ObjectIdentity
intSrvObjects = _IntSrvObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 1)
)
_IntSrvIfAttribTable_Object = MibTable
intSrvIfAttribTable = _IntSrvIfAttribTable_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1)
)
if mibBuilder.loadTexts:
    intSrvIfAttribTable.setStatus("current")
_IntSrvIfAttribEntry_Object = MibTableRow
intSrvIfAttribEntry = _IntSrvIfAttribEntry_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1)
)
intSrvIfAttribEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    intSrvIfAttribEntry.setStatus("current")
_IntSrvIfAttribAllocatedBits_Type = BitRate
_IntSrvIfAttribAllocatedBits_Object = MibTableColumn
intSrvIfAttribAllocatedBits = _IntSrvIfAttribAllocatedBits_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 1),
    _IntSrvIfAttribAllocatedBits_Type()
)
intSrvIfAttribAllocatedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvIfAttribAllocatedBits.setStatus("current")
if mibBuilder.loadTexts:
    intSrvIfAttribAllocatedBits.setUnits("Bits per second")
_IntSrvIfAttribMaxAllocatedBits_Type = BitRate
_IntSrvIfAttribMaxAllocatedBits_Object = MibTableColumn
intSrvIfAttribMaxAllocatedBits = _IntSrvIfAttribMaxAllocatedBits_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 2),
    _IntSrvIfAttribMaxAllocatedBits_Type()
)
intSrvIfAttribMaxAllocatedBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvIfAttribMaxAllocatedBits.setStatus("current")
if mibBuilder.loadTexts:
    intSrvIfAttribMaxAllocatedBits.setUnits("Bits per second")
_IntSrvIfAttribAllocatedBuffer_Type = BurstSize
_IntSrvIfAttribAllocatedBuffer_Object = MibTableColumn
intSrvIfAttribAllocatedBuffer = _IntSrvIfAttribAllocatedBuffer_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 3),
    _IntSrvIfAttribAllocatedBuffer_Type()
)
intSrvIfAttribAllocatedBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvIfAttribAllocatedBuffer.setStatus("current")
if mibBuilder.loadTexts:
    intSrvIfAttribAllocatedBuffer.setUnits("Bytes")
_IntSrvIfAttribFlows_Type = Gauge32
_IntSrvIfAttribFlows_Object = MibTableColumn
intSrvIfAttribFlows = _IntSrvIfAttribFlows_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 4),
    _IntSrvIfAttribFlows_Type()
)
intSrvIfAttribFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvIfAttribFlows.setStatus("current")


class _IntSrvIfAttribPropagationDelay_Type(Integer32):
    """Custom type intSrvIfAttribPropagationDelay based on Integer32"""
    defaultValue = 0


_IntSrvIfAttribPropagationDelay_Object = MibTableColumn
intSrvIfAttribPropagationDelay = _IntSrvIfAttribPropagationDelay_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 5),
    _IntSrvIfAttribPropagationDelay_Type()
)
intSrvIfAttribPropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvIfAttribPropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    intSrvIfAttribPropagationDelay.setUnits("microseconds")
_IntSrvIfAttribStatus_Type = RowStatus
_IntSrvIfAttribStatus_Object = MibTableColumn
intSrvIfAttribStatus = _IntSrvIfAttribStatus_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 6),
    _IntSrvIfAttribStatus_Type()
)
intSrvIfAttribStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvIfAttribStatus.setStatus("current")
_IntSrvFlowTable_Object = MibTable
intSrvFlowTable = _IntSrvFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2)
)
if mibBuilder.loadTexts:
    intSrvFlowTable.setStatus("current")
_IntSrvFlowEntry_Object = MibTableRow
intSrvFlowEntry = _IntSrvFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1)
)
intSrvFlowEntry.setIndexNames(
    (0, "INTEGRATED-SERVICES-MIB", "intSrvFlowNumber"),
)
if mibBuilder.loadTexts:
    intSrvFlowEntry.setStatus("current")
_IntSrvFlowNumber_Type = SessionNumber
_IntSrvFlowNumber_Object = MibTableColumn
intSrvFlowNumber = _IntSrvFlowNumber_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 1),
    _IntSrvFlowNumber_Type()
)
intSrvFlowNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intSrvFlowNumber.setStatus("current")
_IntSrvFlowType_Type = SessionType
_IntSrvFlowType_Object = MibTableColumn
intSrvFlowType = _IntSrvFlowType_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 2),
    _IntSrvFlowType_Type()
)
intSrvFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowType.setStatus("current")


class _IntSrvFlowOwner_Type(Integer32):
    """Custom type intSrvFlowOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("management", 3),
          ("other", 1),
          ("rsvp", 2))
    )


_IntSrvFlowOwner_Type.__name__ = "Integer32"
_IntSrvFlowOwner_Object = MibTableColumn
intSrvFlowOwner = _IntSrvFlowOwner_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 3),
    _IntSrvFlowOwner_Type()
)
intSrvFlowOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowOwner.setStatus("current")


class _IntSrvFlowDestAddr_Type(OctetString):
    """Custom type intSrvFlowDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_IntSrvFlowDestAddr_Type.__name__ = "OctetString"
_IntSrvFlowDestAddr_Object = MibTableColumn
intSrvFlowDestAddr = _IntSrvFlowDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 4),
    _IntSrvFlowDestAddr_Type()
)
intSrvFlowDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowDestAddr.setStatus("current")


class _IntSrvFlowSenderAddr_Type(OctetString):
    """Custom type intSrvFlowSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_IntSrvFlowSenderAddr_Type.__name__ = "OctetString"
_IntSrvFlowSenderAddr_Object = MibTableColumn
intSrvFlowSenderAddr = _IntSrvFlowSenderAddr_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 5),
    _IntSrvFlowSenderAddr_Type()
)
intSrvFlowSenderAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowSenderAddr.setStatus("current")


class _IntSrvFlowDestAddrLength_Type(Integer32):
    """Custom type intSrvFlowDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IntSrvFlowDestAddrLength_Type.__name__ = "Integer32"
_IntSrvFlowDestAddrLength_Object = MibTableColumn
intSrvFlowDestAddrLength = _IntSrvFlowDestAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 6),
    _IntSrvFlowDestAddrLength_Type()
)
intSrvFlowDestAddrLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowDestAddrLength.setStatus("current")


class _IntSrvFlowSenderAddrLength_Type(Integer32):
    """Custom type intSrvFlowSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IntSrvFlowSenderAddrLength_Type.__name__ = "Integer32"
_IntSrvFlowSenderAddrLength_Object = MibTableColumn
intSrvFlowSenderAddrLength = _IntSrvFlowSenderAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 7),
    _IntSrvFlowSenderAddrLength_Type()
)
intSrvFlowSenderAddrLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowSenderAddrLength.setStatus("current")
_IntSrvFlowProtocol_Type = Protocol
_IntSrvFlowProtocol_Object = MibTableColumn
intSrvFlowProtocol = _IntSrvFlowProtocol_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 8),
    _IntSrvFlowProtocol_Type()
)
intSrvFlowProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowProtocol.setStatus("current")
_IntSrvFlowDestPort_Type = Port
_IntSrvFlowDestPort_Object = MibTableColumn
intSrvFlowDestPort = _IntSrvFlowDestPort_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 9),
    _IntSrvFlowDestPort_Type()
)
intSrvFlowDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowDestPort.setStatus("current")
_IntSrvFlowPort_Type = Port
_IntSrvFlowPort_Object = MibTableColumn
intSrvFlowPort = _IntSrvFlowPort_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 10),
    _IntSrvFlowPort_Type()
)
intSrvFlowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowPort.setStatus("current")


class _IntSrvFlowFlowId_Type(Integer32):
    """Custom type intSrvFlowFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IntSrvFlowFlowId_Type.__name__ = "Integer32"
_IntSrvFlowFlowId_Object = MibTableColumn
intSrvFlowFlowId = _IntSrvFlowFlowId_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 11),
    _IntSrvFlowFlowId_Type()
)
intSrvFlowFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvFlowFlowId.setStatus("current")
_IntSrvFlowInterface_Type = InterfaceIndex
_IntSrvFlowInterface_Object = MibTableColumn
intSrvFlowInterface = _IntSrvFlowInterface_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 12),
    _IntSrvFlowInterface_Type()
)
intSrvFlowInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowInterface.setStatus("current")


class _IntSrvFlowIfAddr_Type(OctetString):
    """Custom type intSrvFlowIfAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_IntSrvFlowIfAddr_Type.__name__ = "OctetString"
_IntSrvFlowIfAddr_Object = MibTableColumn
intSrvFlowIfAddr = _IntSrvFlowIfAddr_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 13),
    _IntSrvFlowIfAddr_Type()
)
intSrvFlowIfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowIfAddr.setStatus("current")
_IntSrvFlowRate_Type = BitRate
_IntSrvFlowRate_Object = MibTableColumn
intSrvFlowRate = _IntSrvFlowRate_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 14),
    _IntSrvFlowRate_Type()
)
intSrvFlowRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowRate.setStatus("current")
if mibBuilder.loadTexts:
    intSrvFlowRate.setUnits("bits per second")
_IntSrvFlowBurst_Type = BurstSize
_IntSrvFlowBurst_Object = MibTableColumn
intSrvFlowBurst = _IntSrvFlowBurst_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 15),
    _IntSrvFlowBurst_Type()
)
intSrvFlowBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowBurst.setStatus("current")
if mibBuilder.loadTexts:
    intSrvFlowBurst.setUnits("bytes")
_IntSrvFlowWeight_Type = Integer32
_IntSrvFlowWeight_Object = MibTableColumn
intSrvFlowWeight = _IntSrvFlowWeight_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 16),
    _IntSrvFlowWeight_Type()
)
intSrvFlowWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowWeight.setStatus("current")
_IntSrvFlowQueue_Type = Integer32
_IntSrvFlowQueue_Object = MibTableColumn
intSrvFlowQueue = _IntSrvFlowQueue_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 17),
    _IntSrvFlowQueue_Type()
)
intSrvFlowQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowQueue.setStatus("current")
_IntSrvFlowMinTU_Type = MessageSize
_IntSrvFlowMinTU_Object = MibTableColumn
intSrvFlowMinTU = _IntSrvFlowMinTU_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 18),
    _IntSrvFlowMinTU_Type()
)
intSrvFlowMinTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowMinTU.setStatus("current")
_IntSrvFlowMaxTU_Type = MessageSize
_IntSrvFlowMaxTU_Object = MibTableColumn
intSrvFlowMaxTU = _IntSrvFlowMaxTU_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 19),
    _IntSrvFlowMaxTU_Type()
)
intSrvFlowMaxTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowMaxTU.setStatus("current")
_IntSrvFlowBestEffort_Type = Counter32
_IntSrvFlowBestEffort_Object = MibTableColumn
intSrvFlowBestEffort = _IntSrvFlowBestEffort_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 20),
    _IntSrvFlowBestEffort_Type()
)
intSrvFlowBestEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvFlowBestEffort.setStatus("current")
_IntSrvFlowPoliced_Type = Counter32
_IntSrvFlowPoliced_Object = MibTableColumn
intSrvFlowPoliced = _IntSrvFlowPoliced_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 21),
    _IntSrvFlowPoliced_Type()
)
intSrvFlowPoliced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvFlowPoliced.setStatus("current")


class _IntSrvFlowDiscard_Type(TruthValue):
    """Custom type intSrvFlowDiscard based on TruthValue"""


_IntSrvFlowDiscard_Object = MibTableColumn
intSrvFlowDiscard = _IntSrvFlowDiscard_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 22),
    _IntSrvFlowDiscard_Type()
)
intSrvFlowDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowDiscard.setStatus("current")
_IntSrvFlowService_Type = QosService
_IntSrvFlowService_Object = MibTableColumn
intSrvFlowService = _IntSrvFlowService_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 23),
    _IntSrvFlowService_Type()
)
intSrvFlowService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSrvFlowService.setStatus("current")


class _IntSrvFlowOrder_Type(Integer32):
    """Custom type intSrvFlowOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IntSrvFlowOrder_Type.__name__ = "Integer32"
_IntSrvFlowOrder_Object = MibTableColumn
intSrvFlowOrder = _IntSrvFlowOrder_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 24),
    _IntSrvFlowOrder_Type()
)
intSrvFlowOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowOrder.setStatus("current")
_IntSrvFlowStatus_Type = RowStatus
_IntSrvFlowStatus_Object = MibTableColumn
intSrvFlowStatus = _IntSrvFlowStatus_Object(
    (1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 25),
    _IntSrvFlowStatus_Type()
)
intSrvFlowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvFlowStatus.setStatus("current")
_IntSrvGenObjects_ObjectIdentity = ObjectIdentity
intSrvGenObjects = _IntSrvGenObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 2)
)
_IntSrvFlowNewIndex_Type = TestAndIncr
_IntSrvFlowNewIndex_Object = MibScalar
intSrvFlowNewIndex = _IntSrvFlowNewIndex_Object(
    (1, 3, 6, 1, 2, 1, 52, 2, 1),
    _IntSrvFlowNewIndex_Type()
)
intSrvFlowNewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intSrvFlowNewIndex.setStatus("current")
_IntSrvNotifications_ObjectIdentity = ObjectIdentity
intSrvNotifications = _IntSrvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 3)
)
_IntSrvConformance_ObjectIdentity = ObjectIdentity
intSrvConformance = _IntSrvConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 4)
)
_IntSrvGroups_ObjectIdentity = ObjectIdentity
intSrvGroups = _IntSrvGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 4, 1)
)
_IntSrvCompliances_ObjectIdentity = ObjectIdentity
intSrvCompliances = _IntSrvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 4, 2)
)

# Managed Objects groups

intSrvIfAttribGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 52, 4, 1, 1)
)
intSrvIfAttribGroup.setObjects(
      *(("INTEGRATED-SERVICES-MIB", "intSrvIfAttribAllocatedBits"),
        ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribMaxAllocatedBits"),
        ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribAllocatedBuffer"),
        ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribFlows"),
        ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribPropagationDelay"),
        ("INTEGRATED-SERVICES-MIB", "intSrvIfAttribStatus"))
)
if mibBuilder.loadTexts:
    intSrvIfAttribGroup.setStatus("current")

intSrvFlowsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 52, 4, 1, 2)
)
intSrvFlowsGroup.setObjects(
      *(("INTEGRATED-SERVICES-MIB", "intSrvFlowType"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowOwner"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestAddr"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowSenderAddr"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestAddrLength"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowSenderAddrLength"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowProtocol"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowDestPort"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowPort"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowInterface"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowBestEffort"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowRate"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowBurst"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowWeight"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowQueue"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowMinTU"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowDiscard"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowPoliced"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowService"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowIfAddr"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowOrder"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowFlowId"),
        ("INTEGRATED-SERVICES-MIB", "intSrvFlowMaxTU"))
)
if mibBuilder.loadTexts:
    intSrvFlowsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

intSrvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 52, 4, 2, 1)
)
if mibBuilder.loadTexts:
    intSrvCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEGRATED-SERVICES-MIB",
    **{"SessionNumber": SessionNumber,
       "Protocol": Protocol,
       "SessionType": SessionType,
       "Port": Port,
       "MessageSize": MessageSize,
       "BitRate": BitRate,
       "BurstSize": BurstSize,
       "QosService": QosService,
       "intSrv": intSrv,
       "intSrvObjects": intSrvObjects,
       "intSrvIfAttribTable": intSrvIfAttribTable,
       "intSrvIfAttribEntry": intSrvIfAttribEntry,
       "intSrvIfAttribAllocatedBits": intSrvIfAttribAllocatedBits,
       "intSrvIfAttribMaxAllocatedBits": intSrvIfAttribMaxAllocatedBits,
       "intSrvIfAttribAllocatedBuffer": intSrvIfAttribAllocatedBuffer,
       "intSrvIfAttribFlows": intSrvIfAttribFlows,
       "intSrvIfAttribPropagationDelay": intSrvIfAttribPropagationDelay,
       "intSrvIfAttribStatus": intSrvIfAttribStatus,
       "intSrvFlowTable": intSrvFlowTable,
       "intSrvFlowEntry": intSrvFlowEntry,
       "intSrvFlowNumber": intSrvFlowNumber,
       "intSrvFlowType": intSrvFlowType,
       "intSrvFlowOwner": intSrvFlowOwner,
       "intSrvFlowDestAddr": intSrvFlowDestAddr,
       "intSrvFlowSenderAddr": intSrvFlowSenderAddr,
       "intSrvFlowDestAddrLength": intSrvFlowDestAddrLength,
       "intSrvFlowSenderAddrLength": intSrvFlowSenderAddrLength,
       "intSrvFlowProtocol": intSrvFlowProtocol,
       "intSrvFlowDestPort": intSrvFlowDestPort,
       "intSrvFlowPort": intSrvFlowPort,
       "intSrvFlowFlowId": intSrvFlowFlowId,
       "intSrvFlowInterface": intSrvFlowInterface,
       "intSrvFlowIfAddr": intSrvFlowIfAddr,
       "intSrvFlowRate": intSrvFlowRate,
       "intSrvFlowBurst": intSrvFlowBurst,
       "intSrvFlowWeight": intSrvFlowWeight,
       "intSrvFlowQueue": intSrvFlowQueue,
       "intSrvFlowMinTU": intSrvFlowMinTU,
       "intSrvFlowMaxTU": intSrvFlowMaxTU,
       "intSrvFlowBestEffort": intSrvFlowBestEffort,
       "intSrvFlowPoliced": intSrvFlowPoliced,
       "intSrvFlowDiscard": intSrvFlowDiscard,
       "intSrvFlowService": intSrvFlowService,
       "intSrvFlowOrder": intSrvFlowOrder,
       "intSrvFlowStatus": intSrvFlowStatus,
       "intSrvGenObjects": intSrvGenObjects,
       "intSrvFlowNewIndex": intSrvFlowNewIndex,
       "intSrvNotifications": intSrvNotifications,
       "intSrvConformance": intSrvConformance,
       "intSrvGroups": intSrvGroups,
       "intSrvIfAttribGroup": intSrvIfAttribGroup,
       "intSrvFlowsGroup": intSrvFlowsGroup,
       "intSrvCompliances": intSrvCompliances,
       "intSrvCompliance": intSrvCompliance}
)
