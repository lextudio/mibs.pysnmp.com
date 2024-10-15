# SNMP MIB module (RSVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RSVP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(BitRate,
 BurstSize,
 MessageSize,
 Port,
 Protocol,
 QosService,
 SessionNumber,
 SessionType,
 intSrvFlowStatus) = mibBuilder.importSymbols(
    "INTEGRATED-SERVICES-MIB",
    "BitRate",
    "BurstSize",
    "MessageSize",
    "Port",
    "Protocol",
    "QosService",
    "SessionNumber",
    "SessionType",
    "intSrvFlowStatus")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rsvp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsvpEncapsulation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ip", 1),
          ("udp", 2))
    )



class RefreshInterval(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_RsvpObjects_ObjectIdentity = ObjectIdentity
rsvpObjects = _RsvpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 1)
)
_RsvpSessionTable_Object = MibTable
rsvpSessionTable = _RsvpSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1)
)
if mibBuilder.loadTexts:
    rsvpSessionTable.setStatus("current")
_RsvpSessionEntry_Object = MibTableRow
rsvpSessionEntry = _RsvpSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1)
)
rsvpSessionEntry.setIndexNames(
    (0, "RSVP-MIB", "rsvpSessionNumber"),
)
if mibBuilder.loadTexts:
    rsvpSessionEntry.setStatus("current")
_RsvpSessionNumber_Type = SessionNumber
_RsvpSessionNumber_Object = MibTableColumn
rsvpSessionNumber = _RsvpSessionNumber_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 1),
    _RsvpSessionNumber_Type()
)
rsvpSessionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsvpSessionNumber.setStatus("current")
_RsvpSessionType_Type = SessionType
_RsvpSessionType_Object = MibTableColumn
rsvpSessionType = _RsvpSessionType_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 2),
    _RsvpSessionType_Type()
)
rsvpSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionType.setStatus("current")


class _RsvpSessionDestAddr_Type(OctetString):
    """Custom type rsvpSessionDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpSessionDestAddr_Type.__name__ = "OctetString"
_RsvpSessionDestAddr_Object = MibTableColumn
rsvpSessionDestAddr = _RsvpSessionDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 3),
    _RsvpSessionDestAddr_Type()
)
rsvpSessionDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionDestAddr.setStatus("current")


class _RsvpSessionDestAddrLength_Type(Integer32):
    """Custom type rsvpSessionDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpSessionDestAddrLength_Type.__name__ = "Integer32"
_RsvpSessionDestAddrLength_Object = MibTableColumn
rsvpSessionDestAddrLength = _RsvpSessionDestAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 4),
    _RsvpSessionDestAddrLength_Type()
)
rsvpSessionDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionDestAddrLength.setStatus("current")
_RsvpSessionProtocol_Type = Protocol
_RsvpSessionProtocol_Object = MibTableColumn
rsvpSessionProtocol = _RsvpSessionProtocol_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 5),
    _RsvpSessionProtocol_Type()
)
rsvpSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionProtocol.setStatus("current")
_RsvpSessionPort_Type = Port
_RsvpSessionPort_Object = MibTableColumn
rsvpSessionPort = _RsvpSessionPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 6),
    _RsvpSessionPort_Type()
)
rsvpSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionPort.setStatus("current")
_RsvpSessionSenders_Type = Gauge32
_RsvpSessionSenders_Object = MibTableColumn
rsvpSessionSenders = _RsvpSessionSenders_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 7),
    _RsvpSessionSenders_Type()
)
rsvpSessionSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionSenders.setStatus("current")
_RsvpSessionReceivers_Type = Gauge32
_RsvpSessionReceivers_Object = MibTableColumn
rsvpSessionReceivers = _RsvpSessionReceivers_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 8),
    _RsvpSessionReceivers_Type()
)
rsvpSessionReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionReceivers.setStatus("current")
_RsvpSessionRequests_Type = Gauge32
_RsvpSessionRequests_Object = MibTableColumn
rsvpSessionRequests = _RsvpSessionRequests_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 1, 1, 9),
    _RsvpSessionRequests_Type()
)
rsvpSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSessionRequests.setStatus("current")
_RsvpSenderTable_Object = MibTable
rsvpSenderTable = _RsvpSenderTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2)
)
if mibBuilder.loadTexts:
    rsvpSenderTable.setStatus("current")
_RsvpSenderEntry_Object = MibTableRow
rsvpSenderEntry = _RsvpSenderEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1)
)
rsvpSenderEntry.setIndexNames(
    (0, "RSVP-MIB", "rsvpSessionNumber"),
    (0, "RSVP-MIB", "rsvpSenderNumber"),
)
if mibBuilder.loadTexts:
    rsvpSenderEntry.setStatus("current")
_RsvpSenderNumber_Type = SessionNumber
_RsvpSenderNumber_Object = MibTableColumn
rsvpSenderNumber = _RsvpSenderNumber_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 1),
    _RsvpSenderNumber_Type()
)
rsvpSenderNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsvpSenderNumber.setStatus("current")
_RsvpSenderType_Type = SessionType
_RsvpSenderType_Object = MibTableColumn
rsvpSenderType = _RsvpSenderType_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 2),
    _RsvpSenderType_Type()
)
rsvpSenderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderType.setStatus("current")


class _RsvpSenderDestAddr_Type(OctetString):
    """Custom type rsvpSenderDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpSenderDestAddr_Type.__name__ = "OctetString"
_RsvpSenderDestAddr_Object = MibTableColumn
rsvpSenderDestAddr = _RsvpSenderDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 3),
    _RsvpSenderDestAddr_Type()
)
rsvpSenderDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderDestAddr.setStatus("current")


class _RsvpSenderAddr_Type(OctetString):
    """Custom type rsvpSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpSenderAddr_Type.__name__ = "OctetString"
_RsvpSenderAddr_Object = MibTableColumn
rsvpSenderAddr = _RsvpSenderAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 4),
    _RsvpSenderAddr_Type()
)
rsvpSenderAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAddr.setStatus("current")


class _RsvpSenderDestAddrLength_Type(Integer32):
    """Custom type rsvpSenderDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpSenderDestAddrLength_Type.__name__ = "Integer32"
_RsvpSenderDestAddrLength_Object = MibTableColumn
rsvpSenderDestAddrLength = _RsvpSenderDestAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 5),
    _RsvpSenderDestAddrLength_Type()
)
rsvpSenderDestAddrLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderDestAddrLength.setStatus("current")


class _RsvpSenderAddrLength_Type(Integer32):
    """Custom type rsvpSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpSenderAddrLength_Type.__name__ = "Integer32"
_RsvpSenderAddrLength_Object = MibTableColumn
rsvpSenderAddrLength = _RsvpSenderAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 6),
    _RsvpSenderAddrLength_Type()
)
rsvpSenderAddrLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAddrLength.setStatus("current")
_RsvpSenderProtocol_Type = Protocol
_RsvpSenderProtocol_Object = MibTableColumn
rsvpSenderProtocol = _RsvpSenderProtocol_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 7),
    _RsvpSenderProtocol_Type()
)
rsvpSenderProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderProtocol.setStatus("current")
_RsvpSenderDestPort_Type = Port
_RsvpSenderDestPort_Object = MibTableColumn
rsvpSenderDestPort = _RsvpSenderDestPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 8),
    _RsvpSenderDestPort_Type()
)
rsvpSenderDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderDestPort.setStatus("current")
_RsvpSenderPort_Type = Port
_RsvpSenderPort_Object = MibTableColumn
rsvpSenderPort = _RsvpSenderPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 9),
    _RsvpSenderPort_Type()
)
rsvpSenderPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderPort.setStatus("current")


class _RsvpSenderFlowId_Type(Integer32):
    """Custom type rsvpSenderFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsvpSenderFlowId_Type.__name__ = "Integer32"
_RsvpSenderFlowId_Object = MibTableColumn
rsvpSenderFlowId = _RsvpSenderFlowId_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 10),
    _RsvpSenderFlowId_Type()
)
rsvpSenderFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSenderFlowId.setStatus("current")


class _RsvpSenderHopAddr_Type(OctetString):
    """Custom type rsvpSenderHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpSenderHopAddr_Type.__name__ = "OctetString"
_RsvpSenderHopAddr_Object = MibTableColumn
rsvpSenderHopAddr = _RsvpSenderHopAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 11),
    _RsvpSenderHopAddr_Type()
)
rsvpSenderHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderHopAddr.setStatus("current")
_RsvpSenderHopLih_Type = Integer32
_RsvpSenderHopLih_Object = MibTableColumn
rsvpSenderHopLih = _RsvpSenderHopLih_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 12),
    _RsvpSenderHopLih_Type()
)
rsvpSenderHopLih.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderHopLih.setStatus("current")
_RsvpSenderInterface_Type = InterfaceIndex
_RsvpSenderInterface_Object = MibTableColumn
rsvpSenderInterface = _RsvpSenderInterface_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 13),
    _RsvpSenderInterface_Type()
)
rsvpSenderInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderInterface.setStatus("current")
_RsvpSenderTSpecRate_Type = BitRate
_RsvpSenderTSpecRate_Object = MibTableColumn
rsvpSenderTSpecRate = _RsvpSenderTSpecRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 14),
    _RsvpSenderTSpecRate_Type()
)
rsvpSenderTSpecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderTSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderTSpecRate.setUnits("bits per second")
_RsvpSenderTSpecPeakRate_Type = BitRate
_RsvpSenderTSpecPeakRate_Object = MibTableColumn
rsvpSenderTSpecPeakRate = _RsvpSenderTSpecPeakRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 15),
    _RsvpSenderTSpecPeakRate_Type()
)
rsvpSenderTSpecPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderTSpecPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderTSpecPeakRate.setUnits("bits per second")
_RsvpSenderTSpecBurst_Type = BurstSize
_RsvpSenderTSpecBurst_Object = MibTableColumn
rsvpSenderTSpecBurst = _RsvpSenderTSpecBurst_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 16),
    _RsvpSenderTSpecBurst_Type()
)
rsvpSenderTSpecBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderTSpecBurst.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderTSpecBurst.setUnits("bytes")
_RsvpSenderTSpecMinTU_Type = MessageSize
_RsvpSenderTSpecMinTU_Object = MibTableColumn
rsvpSenderTSpecMinTU = _RsvpSenderTSpecMinTU_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 17),
    _RsvpSenderTSpecMinTU_Type()
)
rsvpSenderTSpecMinTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderTSpecMinTU.setStatus("current")
_RsvpSenderTSpecMaxTU_Type = MessageSize
_RsvpSenderTSpecMaxTU_Object = MibTableColumn
rsvpSenderTSpecMaxTU = _RsvpSenderTSpecMaxTU_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 18),
    _RsvpSenderTSpecMaxTU_Type()
)
rsvpSenderTSpecMaxTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderTSpecMaxTU.setStatus("current")
_RsvpSenderInterval_Type = RefreshInterval
_RsvpSenderInterval_Object = MibTableColumn
rsvpSenderInterval = _RsvpSenderInterval_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 19),
    _RsvpSenderInterval_Type()
)
rsvpSenderInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderInterval.setStatus("current")
_RsvpSenderRSVPHop_Type = TruthValue
_RsvpSenderRSVPHop_Object = MibTableColumn
rsvpSenderRSVPHop = _RsvpSenderRSVPHop_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 20),
    _RsvpSenderRSVPHop_Type()
)
rsvpSenderRSVPHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderRSVPHop.setStatus("current")
_RsvpSenderLastChange_Type = TimeStamp
_RsvpSenderLastChange_Object = MibTableColumn
rsvpSenderLastChange = _RsvpSenderLastChange_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 21),
    _RsvpSenderLastChange_Type()
)
rsvpSenderLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSenderLastChange.setStatus("current")


class _RsvpSenderPolicy_Type(OctetString):
    """Custom type rsvpSenderPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 65536),
    )


_RsvpSenderPolicy_Type.__name__ = "OctetString"
_RsvpSenderPolicy_Object = MibTableColumn
rsvpSenderPolicy = _RsvpSenderPolicy_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 22),
    _RsvpSenderPolicy_Type()
)
rsvpSenderPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderPolicy.setStatus("current")
_RsvpSenderAdspecBreak_Type = TruthValue
_RsvpSenderAdspecBreak_Object = MibTableColumn
rsvpSenderAdspecBreak = _RsvpSenderAdspecBreak_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 23),
    _RsvpSenderAdspecBreak_Type()
)
rsvpSenderAdspecBreak.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecBreak.setStatus("current")


class _RsvpSenderAdspecHopCount_Type(Integer32):
    """Custom type rsvpSenderAdspecHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsvpSenderAdspecHopCount_Type.__name__ = "Integer32"
_RsvpSenderAdspecHopCount_Object = MibTableColumn
rsvpSenderAdspecHopCount = _RsvpSenderAdspecHopCount_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 24),
    _RsvpSenderAdspecHopCount_Type()
)
rsvpSenderAdspecHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecHopCount.setStatus("current")
_RsvpSenderAdspecPathBw_Type = BitRate
_RsvpSenderAdspecPathBw_Object = MibTableColumn
rsvpSenderAdspecPathBw = _RsvpSenderAdspecPathBw_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 25),
    _RsvpSenderAdspecPathBw_Type()
)
rsvpSenderAdspecPathBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecPathBw.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecPathBw.setUnits("bits per second")
_RsvpSenderAdspecMinLatency_Type = Integer32
_RsvpSenderAdspecMinLatency_Object = MibTableColumn
rsvpSenderAdspecMinLatency = _RsvpSenderAdspecMinLatency_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 26),
    _RsvpSenderAdspecMinLatency_Type()
)
rsvpSenderAdspecMinLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecMinLatency.setUnits("microseconds")


class _RsvpSenderAdspecMtu_Type(Integer32):
    """Custom type rsvpSenderAdspecMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsvpSenderAdspecMtu_Type.__name__ = "Integer32"
_RsvpSenderAdspecMtu_Object = MibTableColumn
rsvpSenderAdspecMtu = _RsvpSenderAdspecMtu_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 27),
    _RsvpSenderAdspecMtu_Type()
)
rsvpSenderAdspecMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecMtu.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecMtu.setUnits("bytes")
_RsvpSenderAdspecGuaranteedSvc_Type = TruthValue
_RsvpSenderAdspecGuaranteedSvc_Object = MibTableColumn
rsvpSenderAdspecGuaranteedSvc = _RsvpSenderAdspecGuaranteedSvc_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 28),
    _RsvpSenderAdspecGuaranteedSvc_Type()
)
rsvpSenderAdspecGuaranteedSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedSvc.setStatus("current")
_RsvpSenderAdspecGuaranteedBreak_Type = TruthValue
_RsvpSenderAdspecGuaranteedBreak_Object = MibTableColumn
rsvpSenderAdspecGuaranteedBreak = _RsvpSenderAdspecGuaranteedBreak_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 29),
    _RsvpSenderAdspecGuaranteedBreak_Type()
)
rsvpSenderAdspecGuaranteedBreak.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedBreak.setStatus("current")
_RsvpSenderAdspecGuaranteedCtot_Type = Integer32
_RsvpSenderAdspecGuaranteedCtot_Object = MibTableColumn
rsvpSenderAdspecGuaranteedCtot = _RsvpSenderAdspecGuaranteedCtot_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 30),
    _RsvpSenderAdspecGuaranteedCtot_Type()
)
rsvpSenderAdspecGuaranteedCtot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedCtot.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedCtot.setUnits("bytes")
_RsvpSenderAdspecGuaranteedDtot_Type = Integer32
_RsvpSenderAdspecGuaranteedDtot_Object = MibTableColumn
rsvpSenderAdspecGuaranteedDtot = _RsvpSenderAdspecGuaranteedDtot_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 31),
    _RsvpSenderAdspecGuaranteedDtot_Type()
)
rsvpSenderAdspecGuaranteedDtot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedDtot.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedDtot.setUnits("microseconds")
_RsvpSenderAdspecGuaranteedCsum_Type = Integer32
_RsvpSenderAdspecGuaranteedCsum_Object = MibTableColumn
rsvpSenderAdspecGuaranteedCsum = _RsvpSenderAdspecGuaranteedCsum_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 32),
    _RsvpSenderAdspecGuaranteedCsum_Type()
)
rsvpSenderAdspecGuaranteedCsum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedCsum.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedCsum.setUnits("bytes")
_RsvpSenderAdspecGuaranteedDsum_Type = Integer32
_RsvpSenderAdspecGuaranteedDsum_Object = MibTableColumn
rsvpSenderAdspecGuaranteedDsum = _RsvpSenderAdspecGuaranteedDsum_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 33),
    _RsvpSenderAdspecGuaranteedDsum_Type()
)
rsvpSenderAdspecGuaranteedDsum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedDsum.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedDsum.setUnits("microseconds")


class _RsvpSenderAdspecGuaranteedHopCount_Type(Integer32):
    """Custom type rsvpSenderAdspecGuaranteedHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsvpSenderAdspecGuaranteedHopCount_Type.__name__ = "Integer32"
_RsvpSenderAdspecGuaranteedHopCount_Object = MibTableColumn
rsvpSenderAdspecGuaranteedHopCount = _RsvpSenderAdspecGuaranteedHopCount_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 34),
    _RsvpSenderAdspecGuaranteedHopCount_Type()
)
rsvpSenderAdspecGuaranteedHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedHopCount.setStatus("current")
_RsvpSenderAdspecGuaranteedPathBw_Type = BitRate
_RsvpSenderAdspecGuaranteedPathBw_Object = MibTableColumn
rsvpSenderAdspecGuaranteedPathBw = _RsvpSenderAdspecGuaranteedPathBw_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 35),
    _RsvpSenderAdspecGuaranteedPathBw_Type()
)
rsvpSenderAdspecGuaranteedPathBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedPathBw.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedPathBw.setUnits("bits per second")
_RsvpSenderAdspecGuaranteedMinLatency_Type = Integer32
_RsvpSenderAdspecGuaranteedMinLatency_Object = MibTableColumn
rsvpSenderAdspecGuaranteedMinLatency = _RsvpSenderAdspecGuaranteedMinLatency_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 36),
    _RsvpSenderAdspecGuaranteedMinLatency_Type()
)
rsvpSenderAdspecGuaranteedMinLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedMinLatency.setUnits("microseconds")


class _RsvpSenderAdspecGuaranteedMtu_Type(Integer32):
    """Custom type rsvpSenderAdspecGuaranteedMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsvpSenderAdspecGuaranteedMtu_Type.__name__ = "Integer32"
_RsvpSenderAdspecGuaranteedMtu_Object = MibTableColumn
rsvpSenderAdspecGuaranteedMtu = _RsvpSenderAdspecGuaranteedMtu_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 37),
    _RsvpSenderAdspecGuaranteedMtu_Type()
)
rsvpSenderAdspecGuaranteedMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedMtu.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecGuaranteedMtu.setUnits("bytes")
_RsvpSenderAdspecCtrlLoadSvc_Type = TruthValue
_RsvpSenderAdspecCtrlLoadSvc_Object = MibTableColumn
rsvpSenderAdspecCtrlLoadSvc = _RsvpSenderAdspecCtrlLoadSvc_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 38),
    _RsvpSenderAdspecCtrlLoadSvc_Type()
)
rsvpSenderAdspecCtrlLoadSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadSvc.setStatus("current")
_RsvpSenderAdspecCtrlLoadBreak_Type = TruthValue
_RsvpSenderAdspecCtrlLoadBreak_Object = MibTableColumn
rsvpSenderAdspecCtrlLoadBreak = _RsvpSenderAdspecCtrlLoadBreak_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 39),
    _RsvpSenderAdspecCtrlLoadBreak_Type()
)
rsvpSenderAdspecCtrlLoadBreak.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadBreak.setStatus("current")


class _RsvpSenderAdspecCtrlLoadHopCount_Type(Integer32):
    """Custom type rsvpSenderAdspecCtrlLoadHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsvpSenderAdspecCtrlLoadHopCount_Type.__name__ = "Integer32"
_RsvpSenderAdspecCtrlLoadHopCount_Object = MibTableColumn
rsvpSenderAdspecCtrlLoadHopCount = _RsvpSenderAdspecCtrlLoadHopCount_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 40),
    _RsvpSenderAdspecCtrlLoadHopCount_Type()
)
rsvpSenderAdspecCtrlLoadHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadHopCount.setStatus("current")
_RsvpSenderAdspecCtrlLoadPathBw_Type = BitRate
_RsvpSenderAdspecCtrlLoadPathBw_Object = MibTableColumn
rsvpSenderAdspecCtrlLoadPathBw = _RsvpSenderAdspecCtrlLoadPathBw_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 41),
    _RsvpSenderAdspecCtrlLoadPathBw_Type()
)
rsvpSenderAdspecCtrlLoadPathBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadPathBw.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadPathBw.setUnits("bits per second")
_RsvpSenderAdspecCtrlLoadMinLatency_Type = Integer32
_RsvpSenderAdspecCtrlLoadMinLatency_Object = MibTableColumn
rsvpSenderAdspecCtrlLoadMinLatency = _RsvpSenderAdspecCtrlLoadMinLatency_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 42),
    _RsvpSenderAdspecCtrlLoadMinLatency_Type()
)
rsvpSenderAdspecCtrlLoadMinLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadMinLatency.setUnits("microseconds")


class _RsvpSenderAdspecCtrlLoadMtu_Type(Integer32):
    """Custom type rsvpSenderAdspecCtrlLoadMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsvpSenderAdspecCtrlLoadMtu_Type.__name__ = "Integer32"
_RsvpSenderAdspecCtrlLoadMtu_Object = MibTableColumn
rsvpSenderAdspecCtrlLoadMtu = _RsvpSenderAdspecCtrlLoadMtu_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 43),
    _RsvpSenderAdspecCtrlLoadMtu_Type()
)
rsvpSenderAdspecCtrlLoadMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadMtu.setStatus("current")
if mibBuilder.loadTexts:
    rsvpSenderAdspecCtrlLoadMtu.setUnits("bytes")
_RsvpSenderStatus_Type = RowStatus
_RsvpSenderStatus_Object = MibTableColumn
rsvpSenderStatus = _RsvpSenderStatus_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 44),
    _RsvpSenderStatus_Type()
)
rsvpSenderStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpSenderStatus.setStatus("current")


class _RsvpSenderTTL_Type(Integer32):
    """Custom type rsvpSenderTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsvpSenderTTL_Type.__name__ = "Integer32"
_RsvpSenderTTL_Object = MibTableColumn
rsvpSenderTTL = _RsvpSenderTTL_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 2, 1, 45),
    _RsvpSenderTTL_Type()
)
rsvpSenderTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSenderTTL.setStatus("current")
_RsvpSenderOutInterfaceTable_Object = MibTable
rsvpSenderOutInterfaceTable = _RsvpSenderOutInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 3)
)
if mibBuilder.loadTexts:
    rsvpSenderOutInterfaceTable.setStatus("current")
_RsvpSenderOutInterfaceEntry_Object = MibTableRow
rsvpSenderOutInterfaceEntry = _RsvpSenderOutInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 3, 1)
)
rsvpSenderOutInterfaceEntry.setIndexNames(
    (0, "RSVP-MIB", "rsvpSessionNumber"),
    (0, "RSVP-MIB", "rsvpSenderNumber"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsvpSenderOutInterfaceEntry.setStatus("current")
_RsvpSenderOutInterfaceStatus_Type = RowStatus
_RsvpSenderOutInterfaceStatus_Object = MibTableColumn
rsvpSenderOutInterfaceStatus = _RsvpSenderOutInterfaceStatus_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 3, 1, 1),
    _RsvpSenderOutInterfaceStatus_Type()
)
rsvpSenderOutInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpSenderOutInterfaceStatus.setStatus("current")
_RsvpResvTable_Object = MibTable
rsvpResvTable = _RsvpResvTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4)
)
if mibBuilder.loadTexts:
    rsvpResvTable.setStatus("current")
_RsvpResvEntry_Object = MibTableRow
rsvpResvEntry = _RsvpResvEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1)
)
rsvpResvEntry.setIndexNames(
    (0, "RSVP-MIB", "rsvpSessionNumber"),
    (0, "RSVP-MIB", "rsvpResvNumber"),
)
if mibBuilder.loadTexts:
    rsvpResvEntry.setStatus("current")
_RsvpResvNumber_Type = SessionNumber
_RsvpResvNumber_Object = MibTableColumn
rsvpResvNumber = _RsvpResvNumber_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 1),
    _RsvpResvNumber_Type()
)
rsvpResvNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsvpResvNumber.setStatus("current")
_RsvpResvType_Type = SessionType
_RsvpResvType_Object = MibTableColumn
rsvpResvType = _RsvpResvType_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 2),
    _RsvpResvType_Type()
)
rsvpResvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvType.setStatus("current")


class _RsvpResvDestAddr_Type(OctetString):
    """Custom type rsvpResvDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpResvDestAddr_Type.__name__ = "OctetString"
_RsvpResvDestAddr_Object = MibTableColumn
rsvpResvDestAddr = _RsvpResvDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 3),
    _RsvpResvDestAddr_Type()
)
rsvpResvDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvDestAddr.setStatus("current")


class _RsvpResvSenderAddr_Type(OctetString):
    """Custom type rsvpResvSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpResvSenderAddr_Type.__name__ = "OctetString"
_RsvpResvSenderAddr_Object = MibTableColumn
rsvpResvSenderAddr = _RsvpResvSenderAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 4),
    _RsvpResvSenderAddr_Type()
)
rsvpResvSenderAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvSenderAddr.setStatus("current")


class _RsvpResvDestAddrLength_Type(Integer32):
    """Custom type rsvpResvDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpResvDestAddrLength_Type.__name__ = "Integer32"
_RsvpResvDestAddrLength_Object = MibTableColumn
rsvpResvDestAddrLength = _RsvpResvDestAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 5),
    _RsvpResvDestAddrLength_Type()
)
rsvpResvDestAddrLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvDestAddrLength.setStatus("current")


class _RsvpResvSenderAddrLength_Type(Integer32):
    """Custom type rsvpResvSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpResvSenderAddrLength_Type.__name__ = "Integer32"
_RsvpResvSenderAddrLength_Object = MibTableColumn
rsvpResvSenderAddrLength = _RsvpResvSenderAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 6),
    _RsvpResvSenderAddrLength_Type()
)
rsvpResvSenderAddrLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvSenderAddrLength.setStatus("current")
_RsvpResvProtocol_Type = Protocol
_RsvpResvProtocol_Object = MibTableColumn
rsvpResvProtocol = _RsvpResvProtocol_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 7),
    _RsvpResvProtocol_Type()
)
rsvpResvProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvProtocol.setStatus("current")
_RsvpResvDestPort_Type = Port
_RsvpResvDestPort_Object = MibTableColumn
rsvpResvDestPort = _RsvpResvDestPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 8),
    _RsvpResvDestPort_Type()
)
rsvpResvDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvDestPort.setStatus("current")
_RsvpResvPort_Type = Port
_RsvpResvPort_Object = MibTableColumn
rsvpResvPort = _RsvpResvPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 9),
    _RsvpResvPort_Type()
)
rsvpResvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvPort.setStatus("current")


class _RsvpResvHopAddr_Type(OctetString):
    """Custom type rsvpResvHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpResvHopAddr_Type.__name__ = "OctetString"
_RsvpResvHopAddr_Object = MibTableColumn
rsvpResvHopAddr = _RsvpResvHopAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 10),
    _RsvpResvHopAddr_Type()
)
rsvpResvHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvHopAddr.setStatus("current")
_RsvpResvHopLih_Type = Integer32
_RsvpResvHopLih_Object = MibTableColumn
rsvpResvHopLih = _RsvpResvHopLih_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 11),
    _RsvpResvHopLih_Type()
)
rsvpResvHopLih.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvHopLih.setStatus("current")
_RsvpResvInterface_Type = InterfaceIndex
_RsvpResvInterface_Object = MibTableColumn
rsvpResvInterface = _RsvpResvInterface_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 12),
    _RsvpResvInterface_Type()
)
rsvpResvInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvInterface.setStatus("current")
_RsvpResvService_Type = QosService
_RsvpResvService_Object = MibTableColumn
rsvpResvService = _RsvpResvService_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 13),
    _RsvpResvService_Type()
)
rsvpResvService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvService.setStatus("current")
_RsvpResvTSpecRate_Type = BitRate
_RsvpResvTSpecRate_Object = MibTableColumn
rsvpResvTSpecRate = _RsvpResvTSpecRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 14),
    _RsvpResvTSpecRate_Type()
)
rsvpResvTSpecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvTSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvTSpecRate.setUnits("bits per second")
_RsvpResvTSpecPeakRate_Type = BitRate
_RsvpResvTSpecPeakRate_Object = MibTableColumn
rsvpResvTSpecPeakRate = _RsvpResvTSpecPeakRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 15),
    _RsvpResvTSpecPeakRate_Type()
)
rsvpResvTSpecPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvTSpecPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvTSpecPeakRate.setUnits("bits per second")
_RsvpResvTSpecBurst_Type = BurstSize
_RsvpResvTSpecBurst_Object = MibTableColumn
rsvpResvTSpecBurst = _RsvpResvTSpecBurst_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 16),
    _RsvpResvTSpecBurst_Type()
)
rsvpResvTSpecBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvTSpecBurst.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvTSpecBurst.setUnits("bytes")
_RsvpResvTSpecMinTU_Type = MessageSize
_RsvpResvTSpecMinTU_Object = MibTableColumn
rsvpResvTSpecMinTU = _RsvpResvTSpecMinTU_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 17),
    _RsvpResvTSpecMinTU_Type()
)
rsvpResvTSpecMinTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvTSpecMinTU.setStatus("current")
_RsvpResvTSpecMaxTU_Type = MessageSize
_RsvpResvTSpecMaxTU_Object = MibTableColumn
rsvpResvTSpecMaxTU = _RsvpResvTSpecMaxTU_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 18),
    _RsvpResvTSpecMaxTU_Type()
)
rsvpResvTSpecMaxTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvTSpecMaxTU.setStatus("current")
_RsvpResvRSpecRate_Type = BitRate
_RsvpResvRSpecRate_Object = MibTableColumn
rsvpResvRSpecRate = _RsvpResvRSpecRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 19),
    _RsvpResvRSpecRate_Type()
)
rsvpResvRSpecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvRSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvRSpecRate.setUnits("bits per second")
_RsvpResvRSpecSlack_Type = Integer32
_RsvpResvRSpecSlack_Object = MibTableColumn
rsvpResvRSpecSlack = _RsvpResvRSpecSlack_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 20),
    _RsvpResvRSpecSlack_Type()
)
rsvpResvRSpecSlack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvRSpecSlack.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvRSpecSlack.setUnits("microseconds")
_RsvpResvInterval_Type = RefreshInterval
_RsvpResvInterval_Object = MibTableColumn
rsvpResvInterval = _RsvpResvInterval_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 21),
    _RsvpResvInterval_Type()
)
rsvpResvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvInterval.setStatus("current")


class _RsvpResvScope_Type(OctetString):
    """Custom type rsvpResvScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_RsvpResvScope_Type.__name__ = "OctetString"
_RsvpResvScope_Object = MibTableColumn
rsvpResvScope = _RsvpResvScope_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 22),
    _RsvpResvScope_Type()
)
rsvpResvScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvScope.setStatus("current")
_RsvpResvShared_Type = TruthValue
_RsvpResvShared_Object = MibTableColumn
rsvpResvShared = _RsvpResvShared_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 23),
    _RsvpResvShared_Type()
)
rsvpResvShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvShared.setStatus("current")
_RsvpResvExplicit_Type = TruthValue
_RsvpResvExplicit_Object = MibTableColumn
rsvpResvExplicit = _RsvpResvExplicit_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 24),
    _RsvpResvExplicit_Type()
)
rsvpResvExplicit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvExplicit.setStatus("current")
_RsvpResvRSVPHop_Type = TruthValue
_RsvpResvRSVPHop_Object = MibTableColumn
rsvpResvRSVPHop = _RsvpResvRSVPHop_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 25),
    _RsvpResvRSVPHop_Type()
)
rsvpResvRSVPHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvRSVPHop.setStatus("current")
_RsvpResvLastChange_Type = TimeStamp
_RsvpResvLastChange_Object = MibTableColumn
rsvpResvLastChange = _RsvpResvLastChange_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 26),
    _RsvpResvLastChange_Type()
)
rsvpResvLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvLastChange.setStatus("current")


class _RsvpResvPolicy_Type(OctetString):
    """Custom type rsvpResvPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_RsvpResvPolicy_Type.__name__ = "OctetString"
_RsvpResvPolicy_Object = MibTableColumn
rsvpResvPolicy = _RsvpResvPolicy_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 27),
    _RsvpResvPolicy_Type()
)
rsvpResvPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvPolicy.setStatus("current")
_RsvpResvStatus_Type = RowStatus
_RsvpResvStatus_Object = MibTableColumn
rsvpResvStatus = _RsvpResvStatus_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 28),
    _RsvpResvStatus_Type()
)
rsvpResvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpResvStatus.setStatus("current")


class _RsvpResvTTL_Type(Integer32):
    """Custom type rsvpResvTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsvpResvTTL_Type.__name__ = "Integer32"
_RsvpResvTTL_Object = MibTableColumn
rsvpResvTTL = _RsvpResvTTL_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 29),
    _RsvpResvTTL_Type()
)
rsvpResvTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvTTL.setStatus("current")


class _RsvpResvFlowId_Type(Integer32):
    """Custom type rsvpResvFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsvpResvFlowId_Type.__name__ = "Integer32"
_RsvpResvFlowId_Object = MibTableColumn
rsvpResvFlowId = _RsvpResvFlowId_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 4, 1, 30),
    _RsvpResvFlowId_Type()
)
rsvpResvFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFlowId.setStatus("current")
_RsvpResvFwdTable_Object = MibTable
rsvpResvFwdTable = _RsvpResvFwdTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5)
)
if mibBuilder.loadTexts:
    rsvpResvFwdTable.setStatus("current")
_RsvpResvFwdEntry_Object = MibTableRow
rsvpResvFwdEntry = _RsvpResvFwdEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1)
)
rsvpResvFwdEntry.setIndexNames(
    (0, "RSVP-MIB", "rsvpSessionNumber"),
    (0, "RSVP-MIB", "rsvpResvFwdNumber"),
)
if mibBuilder.loadTexts:
    rsvpResvFwdEntry.setStatus("current")
_RsvpResvFwdNumber_Type = SessionNumber
_RsvpResvFwdNumber_Object = MibTableColumn
rsvpResvFwdNumber = _RsvpResvFwdNumber_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 1),
    _RsvpResvFwdNumber_Type()
)
rsvpResvFwdNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsvpResvFwdNumber.setStatus("current")
_RsvpResvFwdType_Type = SessionType
_RsvpResvFwdType_Object = MibTableColumn
rsvpResvFwdType = _RsvpResvFwdType_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 2),
    _RsvpResvFwdType_Type()
)
rsvpResvFwdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdType.setStatus("current")


class _RsvpResvFwdDestAddr_Type(OctetString):
    """Custom type rsvpResvFwdDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpResvFwdDestAddr_Type.__name__ = "OctetString"
_RsvpResvFwdDestAddr_Object = MibTableColumn
rsvpResvFwdDestAddr = _RsvpResvFwdDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 3),
    _RsvpResvFwdDestAddr_Type()
)
rsvpResvFwdDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdDestAddr.setStatus("current")


class _RsvpResvFwdSenderAddr_Type(OctetString):
    """Custom type rsvpResvFwdSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpResvFwdSenderAddr_Type.__name__ = "OctetString"
_RsvpResvFwdSenderAddr_Object = MibTableColumn
rsvpResvFwdSenderAddr = _RsvpResvFwdSenderAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 4),
    _RsvpResvFwdSenderAddr_Type()
)
rsvpResvFwdSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdSenderAddr.setStatus("current")


class _RsvpResvFwdDestAddrLength_Type(Integer32):
    """Custom type rsvpResvFwdDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpResvFwdDestAddrLength_Type.__name__ = "Integer32"
_RsvpResvFwdDestAddrLength_Object = MibTableColumn
rsvpResvFwdDestAddrLength = _RsvpResvFwdDestAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 5),
    _RsvpResvFwdDestAddrLength_Type()
)
rsvpResvFwdDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdDestAddrLength.setStatus("current")


class _RsvpResvFwdSenderAddrLength_Type(Integer32):
    """Custom type rsvpResvFwdSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RsvpResvFwdSenderAddrLength_Type.__name__ = "Integer32"
_RsvpResvFwdSenderAddrLength_Object = MibTableColumn
rsvpResvFwdSenderAddrLength = _RsvpResvFwdSenderAddrLength_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 6),
    _RsvpResvFwdSenderAddrLength_Type()
)
rsvpResvFwdSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdSenderAddrLength.setStatus("current")
_RsvpResvFwdProtocol_Type = Protocol
_RsvpResvFwdProtocol_Object = MibTableColumn
rsvpResvFwdProtocol = _RsvpResvFwdProtocol_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 7),
    _RsvpResvFwdProtocol_Type()
)
rsvpResvFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdProtocol.setStatus("current")
_RsvpResvFwdDestPort_Type = Port
_RsvpResvFwdDestPort_Object = MibTableColumn
rsvpResvFwdDestPort = _RsvpResvFwdDestPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 8),
    _RsvpResvFwdDestPort_Type()
)
rsvpResvFwdDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdDestPort.setStatus("current")
_RsvpResvFwdPort_Type = Port
_RsvpResvFwdPort_Object = MibTableColumn
rsvpResvFwdPort = _RsvpResvFwdPort_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 9),
    _RsvpResvFwdPort_Type()
)
rsvpResvFwdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdPort.setStatus("current")


class _RsvpResvFwdHopAddr_Type(OctetString):
    """Custom type rsvpResvFwdHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpResvFwdHopAddr_Type.__name__ = "OctetString"
_RsvpResvFwdHopAddr_Object = MibTableColumn
rsvpResvFwdHopAddr = _RsvpResvFwdHopAddr_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 10),
    _RsvpResvFwdHopAddr_Type()
)
rsvpResvFwdHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdHopAddr.setStatus("current")
_RsvpResvFwdHopLih_Type = Integer32
_RsvpResvFwdHopLih_Object = MibTableColumn
rsvpResvFwdHopLih = _RsvpResvFwdHopLih_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 11),
    _RsvpResvFwdHopLih_Type()
)
rsvpResvFwdHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdHopLih.setStatus("current")
_RsvpResvFwdInterface_Type = InterfaceIndex
_RsvpResvFwdInterface_Object = MibTableColumn
rsvpResvFwdInterface = _RsvpResvFwdInterface_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 12),
    _RsvpResvFwdInterface_Type()
)
rsvpResvFwdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdInterface.setStatus("current")
_RsvpResvFwdService_Type = QosService
_RsvpResvFwdService_Object = MibTableColumn
rsvpResvFwdService = _RsvpResvFwdService_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 13),
    _RsvpResvFwdService_Type()
)
rsvpResvFwdService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdService.setStatus("current")
_RsvpResvFwdTSpecRate_Type = BitRate
_RsvpResvFwdTSpecRate_Object = MibTableColumn
rsvpResvFwdTSpecRate = _RsvpResvFwdTSpecRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 14),
    _RsvpResvFwdTSpecRate_Type()
)
rsvpResvFwdTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecRate.setUnits("bits per second")
_RsvpResvFwdTSpecPeakRate_Type = BitRate
_RsvpResvFwdTSpecPeakRate_Object = MibTableColumn
rsvpResvFwdTSpecPeakRate = _RsvpResvFwdTSpecPeakRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 15),
    _RsvpResvFwdTSpecPeakRate_Type()
)
rsvpResvFwdTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecPeakRate.setUnits("bits per second")
_RsvpResvFwdTSpecBurst_Type = BurstSize
_RsvpResvFwdTSpecBurst_Object = MibTableColumn
rsvpResvFwdTSpecBurst = _RsvpResvFwdTSpecBurst_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 16),
    _RsvpResvFwdTSpecBurst_Type()
)
rsvpResvFwdTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecBurst.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecBurst.setUnits("bytes")
_RsvpResvFwdTSpecMinTU_Type = MessageSize
_RsvpResvFwdTSpecMinTU_Object = MibTableColumn
rsvpResvFwdTSpecMinTU = _RsvpResvFwdTSpecMinTU_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 17),
    _RsvpResvFwdTSpecMinTU_Type()
)
rsvpResvFwdTSpecMinTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecMinTU.setStatus("current")
_RsvpResvFwdTSpecMaxTU_Type = MessageSize
_RsvpResvFwdTSpecMaxTU_Object = MibTableColumn
rsvpResvFwdTSpecMaxTU = _RsvpResvFwdTSpecMaxTU_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 18),
    _RsvpResvFwdTSpecMaxTU_Type()
)
rsvpResvFwdTSpecMaxTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdTSpecMaxTU.setStatus("current")
_RsvpResvFwdRSpecRate_Type = BitRate
_RsvpResvFwdRSpecRate_Object = MibTableColumn
rsvpResvFwdRSpecRate = _RsvpResvFwdRSpecRate_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 19),
    _RsvpResvFwdRSpecRate_Type()
)
rsvpResvFwdRSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdRSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvFwdRSpecRate.setUnits("bytes per second")
_RsvpResvFwdRSpecSlack_Type = Integer32
_RsvpResvFwdRSpecSlack_Object = MibTableColumn
rsvpResvFwdRSpecSlack = _RsvpResvFwdRSpecSlack_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 20),
    _RsvpResvFwdRSpecSlack_Type()
)
rsvpResvFwdRSpecSlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdRSpecSlack.setStatus("current")
if mibBuilder.loadTexts:
    rsvpResvFwdRSpecSlack.setUnits("microseconds")
_RsvpResvFwdInterval_Type = RefreshInterval
_RsvpResvFwdInterval_Object = MibTableColumn
rsvpResvFwdInterval = _RsvpResvFwdInterval_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 21),
    _RsvpResvFwdInterval_Type()
)
rsvpResvFwdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdInterval.setStatus("current")


class _RsvpResvFwdScope_Type(OctetString):
    """Custom type rsvpResvFwdScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_RsvpResvFwdScope_Type.__name__ = "OctetString"
_RsvpResvFwdScope_Object = MibTableColumn
rsvpResvFwdScope = _RsvpResvFwdScope_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 22),
    _RsvpResvFwdScope_Type()
)
rsvpResvFwdScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdScope.setStatus("current")
_RsvpResvFwdShared_Type = TruthValue
_RsvpResvFwdShared_Object = MibTableColumn
rsvpResvFwdShared = _RsvpResvFwdShared_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 23),
    _RsvpResvFwdShared_Type()
)
rsvpResvFwdShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdShared.setStatus("current")
_RsvpResvFwdExplicit_Type = TruthValue
_RsvpResvFwdExplicit_Object = MibTableColumn
rsvpResvFwdExplicit = _RsvpResvFwdExplicit_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 24),
    _RsvpResvFwdExplicit_Type()
)
rsvpResvFwdExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdExplicit.setStatus("current")
_RsvpResvFwdRSVPHop_Type = TruthValue
_RsvpResvFwdRSVPHop_Object = MibTableColumn
rsvpResvFwdRSVPHop = _RsvpResvFwdRSVPHop_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 25),
    _RsvpResvFwdRSVPHop_Type()
)
rsvpResvFwdRSVPHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdRSVPHop.setStatus("current")
_RsvpResvFwdLastChange_Type = TimeStamp
_RsvpResvFwdLastChange_Object = MibTableColumn
rsvpResvFwdLastChange = _RsvpResvFwdLastChange_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 26),
    _RsvpResvFwdLastChange_Type()
)
rsvpResvFwdLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdLastChange.setStatus("current")


class _RsvpResvFwdPolicy_Type(OctetString):
    """Custom type rsvpResvFwdPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_RsvpResvFwdPolicy_Type.__name__ = "OctetString"
_RsvpResvFwdPolicy_Object = MibTableColumn
rsvpResvFwdPolicy = _RsvpResvFwdPolicy_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 27),
    _RsvpResvFwdPolicy_Type()
)
rsvpResvFwdPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdPolicy.setStatus("current")
_RsvpResvFwdStatus_Type = RowStatus
_RsvpResvFwdStatus_Object = MibTableColumn
rsvpResvFwdStatus = _RsvpResvFwdStatus_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 28),
    _RsvpResvFwdStatus_Type()
)
rsvpResvFwdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsvpResvFwdStatus.setStatus("current")


class _RsvpResvFwdTTL_Type(Integer32):
    """Custom type rsvpResvFwdTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsvpResvFwdTTL_Type.__name__ = "Integer32"
_RsvpResvFwdTTL_Object = MibTableColumn
rsvpResvFwdTTL = _RsvpResvFwdTTL_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 29),
    _RsvpResvFwdTTL_Type()
)
rsvpResvFwdTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdTTL.setStatus("current")


class _RsvpResvFwdFlowId_Type(Integer32):
    """Custom type rsvpResvFwdFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsvpResvFwdFlowId_Type.__name__ = "Integer32"
_RsvpResvFwdFlowId_Object = MibTableColumn
rsvpResvFwdFlowId = _RsvpResvFwdFlowId_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 5, 1, 30),
    _RsvpResvFwdFlowId_Type()
)
rsvpResvFwdFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpResvFwdFlowId.setStatus("current")
_RsvpIfTable_Object = MibTable
rsvpIfTable = _RsvpIfTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6)
)
if mibBuilder.loadTexts:
    rsvpIfTable.setStatus("current")
_RsvpIfEntry_Object = MibTableRow
rsvpIfEntry = _RsvpIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1)
)
rsvpIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsvpIfEntry.setStatus("current")
_RsvpIfUdpNbrs_Type = Gauge32
_RsvpIfUdpNbrs_Object = MibTableColumn
rsvpIfUdpNbrs = _RsvpIfUdpNbrs_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 1),
    _RsvpIfUdpNbrs_Type()
)
rsvpIfUdpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpIfUdpNbrs.setStatus("current")
_RsvpIfIpNbrs_Type = Gauge32
_RsvpIfIpNbrs_Object = MibTableColumn
rsvpIfIpNbrs = _RsvpIfIpNbrs_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 2),
    _RsvpIfIpNbrs_Type()
)
rsvpIfIpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpIfIpNbrs.setStatus("current")
_RsvpIfNbrs_Type = Gauge32
_RsvpIfNbrs_Object = MibTableColumn
rsvpIfNbrs = _RsvpIfNbrs_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 3),
    _RsvpIfNbrs_Type()
)
rsvpIfNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpIfNbrs.setStatus("current")


class _RsvpIfRefreshBlockadeMultiple_Type(Integer32):
    """Custom type rsvpIfRefreshBlockadeMultiple based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_RsvpIfRefreshBlockadeMultiple_Type.__name__ = "Integer32"
_RsvpIfRefreshBlockadeMultiple_Object = MibTableColumn
rsvpIfRefreshBlockadeMultiple = _RsvpIfRefreshBlockadeMultiple_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 4),
    _RsvpIfRefreshBlockadeMultiple_Type()
)
rsvpIfRefreshBlockadeMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfRefreshBlockadeMultiple.setStatus("current")


class _RsvpIfRefreshMultiple_Type(Integer32):
    """Custom type rsvpIfRefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_RsvpIfRefreshMultiple_Type.__name__ = "Integer32"
_RsvpIfRefreshMultiple_Object = MibTableColumn
rsvpIfRefreshMultiple = _RsvpIfRefreshMultiple_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 5),
    _RsvpIfRefreshMultiple_Type()
)
rsvpIfRefreshMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfRefreshMultiple.setStatus("current")


class _RsvpIfTTL_Type(Integer32):
    """Custom type rsvpIfTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsvpIfTTL_Type.__name__ = "Integer32"
_RsvpIfTTL_Object = MibTableColumn
rsvpIfTTL = _RsvpIfTTL_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 6),
    _RsvpIfTTL_Type()
)
rsvpIfTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfTTL.setStatus("current")


class _RsvpIfRefreshInterval_Type(TimeInterval):
    """Custom type rsvpIfRefreshInterval based on TimeInterval"""
    defaultValue = 3000


_RsvpIfRefreshInterval_Object = MibTableColumn
rsvpIfRefreshInterval = _RsvpIfRefreshInterval_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 7),
    _RsvpIfRefreshInterval_Type()
)
rsvpIfRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsvpIfRefreshInterval.setUnits("milliseconds")


class _RsvpIfRouteDelay_Type(TimeInterval):
    """Custom type rsvpIfRouteDelay based on TimeInterval"""
    defaultValue = 200


_RsvpIfRouteDelay_Object = MibTableColumn
rsvpIfRouteDelay = _RsvpIfRouteDelay_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 8),
    _RsvpIfRouteDelay_Type()
)
rsvpIfRouteDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfRouteDelay.setStatus("current")
if mibBuilder.loadTexts:
    rsvpIfRouteDelay.setUnits("hundredths of a second")
_RsvpIfEnabled_Type = TruthValue
_RsvpIfEnabled_Object = MibTableColumn
rsvpIfEnabled = _RsvpIfEnabled_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 9),
    _RsvpIfEnabled_Type()
)
rsvpIfEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfEnabled.setStatus("current")
_RsvpIfUdpRequired_Type = TruthValue
_RsvpIfUdpRequired_Object = MibTableColumn
rsvpIfUdpRequired = _RsvpIfUdpRequired_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 10),
    _RsvpIfUdpRequired_Type()
)
rsvpIfUdpRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfUdpRequired.setStatus("current")
_RsvpIfStatus_Type = RowStatus
_RsvpIfStatus_Object = MibTableColumn
rsvpIfStatus = _RsvpIfStatus_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 6, 1, 11),
    _RsvpIfStatus_Type()
)
rsvpIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpIfStatus.setStatus("current")
_RsvpNbrTable_Object = MibTable
rsvpNbrTable = _RsvpNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 7)
)
if mibBuilder.loadTexts:
    rsvpNbrTable.setStatus("current")
_RsvpNbrEntry_Object = MibTableRow
rsvpNbrEntry = _RsvpNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 7, 1)
)
rsvpNbrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RSVP-MIB", "rsvpNbrAddress"),
)
if mibBuilder.loadTexts:
    rsvpNbrEntry.setStatus("current")


class _RsvpNbrAddress_Type(OctetString):
    """Custom type rsvpNbrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RsvpNbrAddress_Type.__name__ = "OctetString"
_RsvpNbrAddress_Object = MibTableColumn
rsvpNbrAddress = _RsvpNbrAddress_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 7, 1, 1),
    _RsvpNbrAddress_Type()
)
rsvpNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsvpNbrAddress.setStatus("current")
_RsvpNbrProtocol_Type = RsvpEncapsulation
_RsvpNbrProtocol_Object = MibTableColumn
rsvpNbrProtocol = _RsvpNbrProtocol_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 7, 1, 2),
    _RsvpNbrProtocol_Type()
)
rsvpNbrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpNbrProtocol.setStatus("current")
_RsvpNbrStatus_Type = RowStatus
_RsvpNbrStatus_Object = MibTableColumn
rsvpNbrStatus = _RsvpNbrStatus_Object(
    (1, 3, 6, 1, 2, 1, 51, 1, 7, 1, 3),
    _RsvpNbrStatus_Type()
)
rsvpNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsvpNbrStatus.setStatus("current")
_RsvpGenObjects_ObjectIdentity = ObjectIdentity
rsvpGenObjects = _RsvpGenObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 2)
)
_RsvpBadPackets_Type = Gauge32
_RsvpBadPackets_Object = MibScalar
rsvpBadPackets = _RsvpBadPackets_Object(
    (1, 3, 6, 1, 2, 1, 51, 2, 1),
    _RsvpBadPackets_Type()
)
rsvpBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsvpBadPackets.setStatus("current")
_RsvpSenderNewIndex_Type = TestAndIncr
_RsvpSenderNewIndex_Object = MibScalar
rsvpSenderNewIndex = _RsvpSenderNewIndex_Object(
    (1, 3, 6, 1, 2, 1, 51, 2, 2),
    _RsvpSenderNewIndex_Type()
)
rsvpSenderNewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsvpSenderNewIndex.setStatus("current")
_RsvpResvNewIndex_Type = TestAndIncr
_RsvpResvNewIndex_Object = MibScalar
rsvpResvNewIndex = _RsvpResvNewIndex_Object(
    (1, 3, 6, 1, 2, 1, 51, 2, 3),
    _RsvpResvNewIndex_Type()
)
rsvpResvNewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsvpResvNewIndex.setStatus("current")
_RsvpResvFwdNewIndex_Type = TestAndIncr
_RsvpResvFwdNewIndex_Object = MibScalar
rsvpResvFwdNewIndex = _RsvpResvFwdNewIndex_Object(
    (1, 3, 6, 1, 2, 1, 51, 2, 4),
    _RsvpResvFwdNewIndex_Type()
)
rsvpResvFwdNewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsvpResvFwdNewIndex.setStatus("current")
_RsvpNotificationsPrefix_ObjectIdentity = ObjectIdentity
rsvpNotificationsPrefix = _RsvpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 3)
)
_RsvpNotifications_ObjectIdentity = ObjectIdentity
rsvpNotifications = _RsvpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 3, 0)
)
_RsvpConformance_ObjectIdentity = ObjectIdentity
rsvpConformance = _RsvpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 4)
)
_RsvpGroups_ObjectIdentity = ObjectIdentity
rsvpGroups = _RsvpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 4, 1)
)
_RsvpCompliances_ObjectIdentity = ObjectIdentity
rsvpCompliances = _RsvpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 51, 4, 2)
)

# Managed Objects groups

rsvpSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 1)
)
rsvpSessionGroup.setObjects(
      *(("RSVP-MIB", "rsvpSessionType"),
        ("RSVP-MIB", "rsvpSessionDestAddr"),
        ("RSVP-MIB", "rsvpSessionDestAddrLength"),
        ("RSVP-MIB", "rsvpSessionProtocol"),
        ("RSVP-MIB", "rsvpSessionPort"),
        ("RSVP-MIB", "rsvpSessionSenders"),
        ("RSVP-MIB", "rsvpSessionReceivers"),
        ("RSVP-MIB", "rsvpSessionRequests"))
)
if mibBuilder.loadTexts:
    rsvpSessionGroup.setStatus("current")

rsvpSenderGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 2)
)
rsvpSenderGroup.setObjects(
      *(("RSVP-MIB", "rsvpSenderType"),
        ("RSVP-MIB", "rsvpSenderDestAddr"),
        ("RSVP-MIB", "rsvpSenderAddr"),
        ("RSVP-MIB", "rsvpSenderDestAddrLength"),
        ("RSVP-MIB", "rsvpSenderAddrLength"),
        ("RSVP-MIB", "rsvpSenderProtocol"),
        ("RSVP-MIB", "rsvpSenderDestPort"),
        ("RSVP-MIB", "rsvpSenderPort"),
        ("RSVP-MIB", "rsvpSenderHopAddr"),
        ("RSVP-MIB", "rsvpSenderHopLih"),
        ("RSVP-MIB", "rsvpSenderInterface"),
        ("RSVP-MIB", "rsvpSenderTSpecRate"),
        ("RSVP-MIB", "rsvpSenderTSpecPeakRate"),
        ("RSVP-MIB", "rsvpSenderTSpecBurst"),
        ("RSVP-MIB", "rsvpSenderTSpecMinTU"),
        ("RSVP-MIB", "rsvpSenderTSpecMaxTU"),
        ("RSVP-MIB", "rsvpSenderInterval"),
        ("RSVP-MIB", "rsvpSenderLastChange"),
        ("RSVP-MIB", "rsvpSenderStatus"),
        ("RSVP-MIB", "rsvpSenderRSVPHop"),
        ("RSVP-MIB", "rsvpSenderPolicy"),
        ("RSVP-MIB", "rsvpSenderAdspecBreak"),
        ("RSVP-MIB", "rsvpSenderAdspecHopCount"),
        ("RSVP-MIB", "rsvpSenderAdspecPathBw"),
        ("RSVP-MIB", "rsvpSenderAdspecMinLatency"),
        ("RSVP-MIB", "rsvpSenderAdspecMtu"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedSvc"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedBreak"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedCtot"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedDtot"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedCsum"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedDsum"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedHopCount"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedPathBw"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedMinLatency"),
        ("RSVP-MIB", "rsvpSenderAdspecGuaranteedMtu"),
        ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadSvc"),
        ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadBreak"),
        ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadHopCount"),
        ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadPathBw"),
        ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadMinLatency"),
        ("RSVP-MIB", "rsvpSenderAdspecCtrlLoadMtu"),
        ("RSVP-MIB", "rsvpSenderNewIndex"))
)
if mibBuilder.loadTexts:
    rsvpSenderGroup.setStatus("current")

rsvpResvGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 3)
)
rsvpResvGroup.setObjects(
      *(("RSVP-MIB", "rsvpResvType"),
        ("RSVP-MIB", "rsvpResvDestAddr"),
        ("RSVP-MIB", "rsvpResvSenderAddr"),
        ("RSVP-MIB", "rsvpResvDestAddrLength"),
        ("RSVP-MIB", "rsvpResvSenderAddrLength"),
        ("RSVP-MIB", "rsvpResvProtocol"),
        ("RSVP-MIB", "rsvpResvDestPort"),
        ("RSVP-MIB", "rsvpResvPort"),
        ("RSVP-MIB", "rsvpResvHopAddr"),
        ("RSVP-MIB", "rsvpResvHopLih"),
        ("RSVP-MIB", "rsvpResvInterface"),
        ("RSVP-MIB", "rsvpResvService"),
        ("RSVP-MIB", "rsvpResvTSpecRate"),
        ("RSVP-MIB", "rsvpResvTSpecBurst"),
        ("RSVP-MIB", "rsvpResvTSpecPeakRate"),
        ("RSVP-MIB", "rsvpResvTSpecMinTU"),
        ("RSVP-MIB", "rsvpResvTSpecMaxTU"),
        ("RSVP-MIB", "rsvpResvRSpecRate"),
        ("RSVP-MIB", "rsvpResvRSpecSlack"),
        ("RSVP-MIB", "rsvpResvInterval"),
        ("RSVP-MIB", "rsvpResvScope"),
        ("RSVP-MIB", "rsvpResvShared"),
        ("RSVP-MIB", "rsvpResvExplicit"),
        ("RSVP-MIB", "rsvpResvRSVPHop"),
        ("RSVP-MIB", "rsvpResvLastChange"),
        ("RSVP-MIB", "rsvpResvPolicy"),
        ("RSVP-MIB", "rsvpResvStatus"),
        ("RSVP-MIB", "rsvpResvNewIndex"))
)
if mibBuilder.loadTexts:
    rsvpResvGroup.setStatus("current")

rsvpResvFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 4)
)
rsvpResvFwdGroup.setObjects(
      *(("RSVP-MIB", "rsvpResvFwdType"),
        ("RSVP-MIB", "rsvpResvFwdDestAddr"),
        ("RSVP-MIB", "rsvpResvFwdSenderAddr"),
        ("RSVP-MIB", "rsvpResvFwdDestAddrLength"),
        ("RSVP-MIB", "rsvpResvFwdSenderAddrLength"),
        ("RSVP-MIB", "rsvpResvFwdProtocol"),
        ("RSVP-MIB", "rsvpResvFwdDestPort"),
        ("RSVP-MIB", "rsvpResvFwdPort"),
        ("RSVP-MIB", "rsvpResvFwdHopAddr"),
        ("RSVP-MIB", "rsvpResvFwdHopLih"),
        ("RSVP-MIB", "rsvpResvFwdInterface"),
        ("RSVP-MIB", "rsvpResvFwdNewIndex"),
        ("RSVP-MIB", "rsvpResvFwdService"),
        ("RSVP-MIB", "rsvpResvFwdTSpecPeakRate"),
        ("RSVP-MIB", "rsvpResvFwdTSpecMinTU"),
        ("RSVP-MIB", "rsvpResvFwdTSpecMaxTU"),
        ("RSVP-MIB", "rsvpResvFwdTSpecRate"),
        ("RSVP-MIB", "rsvpResvFwdTSpecBurst"),
        ("RSVP-MIB", "rsvpResvFwdRSpecRate"),
        ("RSVP-MIB", "rsvpResvFwdRSpecSlack"),
        ("RSVP-MIB", "rsvpResvFwdInterval"),
        ("RSVP-MIB", "rsvpResvFwdScope"),
        ("RSVP-MIB", "rsvpResvFwdShared"),
        ("RSVP-MIB", "rsvpResvFwdExplicit"),
        ("RSVP-MIB", "rsvpResvFwdRSVPHop"),
        ("RSVP-MIB", "rsvpResvFwdLastChange"),
        ("RSVP-MIB", "rsvpResvFwdPolicy"),
        ("RSVP-MIB", "rsvpResvFwdStatus"))
)
if mibBuilder.loadTexts:
    rsvpResvFwdGroup.setStatus("current")

rsvpIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 6)
)
rsvpIfGroup.setObjects(
      *(("RSVP-MIB", "rsvpIfUdpNbrs"),
        ("RSVP-MIB", "rsvpIfIpNbrs"),
        ("RSVP-MIB", "rsvpIfNbrs"),
        ("RSVP-MIB", "rsvpIfEnabled"),
        ("RSVP-MIB", "rsvpIfUdpRequired"),
        ("RSVP-MIB", "rsvpIfRefreshBlockadeMultiple"),
        ("RSVP-MIB", "rsvpIfRefreshMultiple"),
        ("RSVP-MIB", "rsvpIfRefreshInterval"),
        ("RSVP-MIB", "rsvpIfTTL"),
        ("RSVP-MIB", "rsvpIfRouteDelay"),
        ("RSVP-MIB", "rsvpIfStatus"))
)
if mibBuilder.loadTexts:
    rsvpIfGroup.setStatus("current")

rsvpNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 7)
)
rsvpNbrGroup.setObjects(
      *(("RSVP-MIB", "rsvpNbrProtocol"),
        ("RSVP-MIB", "rsvpNbrStatus"))
)
if mibBuilder.loadTexts:
    rsvpNbrGroup.setStatus("current")


# Notification objects

newFlow = NotificationType(
    (1, 3, 6, 1, 2, 1, 51, 3, 0, 1)
)
newFlow.setObjects(
      *(("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"),
        ("RSVP-MIB", "rsvpSessionDestAddr"),
        ("RSVP-MIB", "rsvpResvFwdStatus"),
        ("RSVP-MIB", "rsvpResvStatus"),
        ("RSVP-MIB", "rsvpSenderStatus"))
)
if mibBuilder.loadTexts:
    newFlow.setStatus(
        "current"
    )

lostFlow = NotificationType(
    (1, 3, 6, 1, 2, 1, 51, 3, 0, 2)
)
lostFlow.setObjects(
      *(("INTEGRATED-SERVICES-MIB", "intSrvFlowStatus"),
        ("RSVP-MIB", "rsvpSessionDestAddr"),
        ("RSVP-MIB", "rsvpResvFwdStatus"),
        ("RSVP-MIB", "rsvpResvStatus"),
        ("RSVP-MIB", "rsvpSenderStatus"))
)
if mibBuilder.loadTexts:
    lostFlow.setStatus(
        "current"
    )


# Notifications groups

rsvpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 51, 4, 1, 8)
)
rsvpNotificationGroup.setObjects(
      *(("RSVP-MIB", "newFlow"),
        ("RSVP-MIB", "lostFlow"))
)
if mibBuilder.loadTexts:
    rsvpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rsvpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 51, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rsvpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RSVP-MIB",
    **{"RsvpEncapsulation": RsvpEncapsulation,
       "RefreshInterval": RefreshInterval,
       "rsvp": rsvp,
       "rsvpObjects": rsvpObjects,
       "rsvpSessionTable": rsvpSessionTable,
       "rsvpSessionEntry": rsvpSessionEntry,
       "rsvpSessionNumber": rsvpSessionNumber,
       "rsvpSessionType": rsvpSessionType,
       "rsvpSessionDestAddr": rsvpSessionDestAddr,
       "rsvpSessionDestAddrLength": rsvpSessionDestAddrLength,
       "rsvpSessionProtocol": rsvpSessionProtocol,
       "rsvpSessionPort": rsvpSessionPort,
       "rsvpSessionSenders": rsvpSessionSenders,
       "rsvpSessionReceivers": rsvpSessionReceivers,
       "rsvpSessionRequests": rsvpSessionRequests,
       "rsvpSenderTable": rsvpSenderTable,
       "rsvpSenderEntry": rsvpSenderEntry,
       "rsvpSenderNumber": rsvpSenderNumber,
       "rsvpSenderType": rsvpSenderType,
       "rsvpSenderDestAddr": rsvpSenderDestAddr,
       "rsvpSenderAddr": rsvpSenderAddr,
       "rsvpSenderDestAddrLength": rsvpSenderDestAddrLength,
       "rsvpSenderAddrLength": rsvpSenderAddrLength,
       "rsvpSenderProtocol": rsvpSenderProtocol,
       "rsvpSenderDestPort": rsvpSenderDestPort,
       "rsvpSenderPort": rsvpSenderPort,
       "rsvpSenderFlowId": rsvpSenderFlowId,
       "rsvpSenderHopAddr": rsvpSenderHopAddr,
       "rsvpSenderHopLih": rsvpSenderHopLih,
       "rsvpSenderInterface": rsvpSenderInterface,
       "rsvpSenderTSpecRate": rsvpSenderTSpecRate,
       "rsvpSenderTSpecPeakRate": rsvpSenderTSpecPeakRate,
       "rsvpSenderTSpecBurst": rsvpSenderTSpecBurst,
       "rsvpSenderTSpecMinTU": rsvpSenderTSpecMinTU,
       "rsvpSenderTSpecMaxTU": rsvpSenderTSpecMaxTU,
       "rsvpSenderInterval": rsvpSenderInterval,
       "rsvpSenderRSVPHop": rsvpSenderRSVPHop,
       "rsvpSenderLastChange": rsvpSenderLastChange,
       "rsvpSenderPolicy": rsvpSenderPolicy,
       "rsvpSenderAdspecBreak": rsvpSenderAdspecBreak,
       "rsvpSenderAdspecHopCount": rsvpSenderAdspecHopCount,
       "rsvpSenderAdspecPathBw": rsvpSenderAdspecPathBw,
       "rsvpSenderAdspecMinLatency": rsvpSenderAdspecMinLatency,
       "rsvpSenderAdspecMtu": rsvpSenderAdspecMtu,
       "rsvpSenderAdspecGuaranteedSvc": rsvpSenderAdspecGuaranteedSvc,
       "rsvpSenderAdspecGuaranteedBreak": rsvpSenderAdspecGuaranteedBreak,
       "rsvpSenderAdspecGuaranteedCtot": rsvpSenderAdspecGuaranteedCtot,
       "rsvpSenderAdspecGuaranteedDtot": rsvpSenderAdspecGuaranteedDtot,
       "rsvpSenderAdspecGuaranteedCsum": rsvpSenderAdspecGuaranteedCsum,
       "rsvpSenderAdspecGuaranteedDsum": rsvpSenderAdspecGuaranteedDsum,
       "rsvpSenderAdspecGuaranteedHopCount": rsvpSenderAdspecGuaranteedHopCount,
       "rsvpSenderAdspecGuaranteedPathBw": rsvpSenderAdspecGuaranteedPathBw,
       "rsvpSenderAdspecGuaranteedMinLatency": rsvpSenderAdspecGuaranteedMinLatency,
       "rsvpSenderAdspecGuaranteedMtu": rsvpSenderAdspecGuaranteedMtu,
       "rsvpSenderAdspecCtrlLoadSvc": rsvpSenderAdspecCtrlLoadSvc,
       "rsvpSenderAdspecCtrlLoadBreak": rsvpSenderAdspecCtrlLoadBreak,
       "rsvpSenderAdspecCtrlLoadHopCount": rsvpSenderAdspecCtrlLoadHopCount,
       "rsvpSenderAdspecCtrlLoadPathBw": rsvpSenderAdspecCtrlLoadPathBw,
       "rsvpSenderAdspecCtrlLoadMinLatency": rsvpSenderAdspecCtrlLoadMinLatency,
       "rsvpSenderAdspecCtrlLoadMtu": rsvpSenderAdspecCtrlLoadMtu,
       "rsvpSenderStatus": rsvpSenderStatus,
       "rsvpSenderTTL": rsvpSenderTTL,
       "rsvpSenderOutInterfaceTable": rsvpSenderOutInterfaceTable,
       "rsvpSenderOutInterfaceEntry": rsvpSenderOutInterfaceEntry,
       "rsvpSenderOutInterfaceStatus": rsvpSenderOutInterfaceStatus,
       "rsvpResvTable": rsvpResvTable,
       "rsvpResvEntry": rsvpResvEntry,
       "rsvpResvNumber": rsvpResvNumber,
       "rsvpResvType": rsvpResvType,
       "rsvpResvDestAddr": rsvpResvDestAddr,
       "rsvpResvSenderAddr": rsvpResvSenderAddr,
       "rsvpResvDestAddrLength": rsvpResvDestAddrLength,
       "rsvpResvSenderAddrLength": rsvpResvSenderAddrLength,
       "rsvpResvProtocol": rsvpResvProtocol,
       "rsvpResvDestPort": rsvpResvDestPort,
       "rsvpResvPort": rsvpResvPort,
       "rsvpResvHopAddr": rsvpResvHopAddr,
       "rsvpResvHopLih": rsvpResvHopLih,
       "rsvpResvInterface": rsvpResvInterface,
       "rsvpResvService": rsvpResvService,
       "rsvpResvTSpecRate": rsvpResvTSpecRate,
       "rsvpResvTSpecPeakRate": rsvpResvTSpecPeakRate,
       "rsvpResvTSpecBurst": rsvpResvTSpecBurst,
       "rsvpResvTSpecMinTU": rsvpResvTSpecMinTU,
       "rsvpResvTSpecMaxTU": rsvpResvTSpecMaxTU,
       "rsvpResvRSpecRate": rsvpResvRSpecRate,
       "rsvpResvRSpecSlack": rsvpResvRSpecSlack,
       "rsvpResvInterval": rsvpResvInterval,
       "rsvpResvScope": rsvpResvScope,
       "rsvpResvShared": rsvpResvShared,
       "rsvpResvExplicit": rsvpResvExplicit,
       "rsvpResvRSVPHop": rsvpResvRSVPHop,
       "rsvpResvLastChange": rsvpResvLastChange,
       "rsvpResvPolicy": rsvpResvPolicy,
       "rsvpResvStatus": rsvpResvStatus,
       "rsvpResvTTL": rsvpResvTTL,
       "rsvpResvFlowId": rsvpResvFlowId,
       "rsvpResvFwdTable": rsvpResvFwdTable,
       "rsvpResvFwdEntry": rsvpResvFwdEntry,
       "rsvpResvFwdNumber": rsvpResvFwdNumber,
       "rsvpResvFwdType": rsvpResvFwdType,
       "rsvpResvFwdDestAddr": rsvpResvFwdDestAddr,
       "rsvpResvFwdSenderAddr": rsvpResvFwdSenderAddr,
       "rsvpResvFwdDestAddrLength": rsvpResvFwdDestAddrLength,
       "rsvpResvFwdSenderAddrLength": rsvpResvFwdSenderAddrLength,
       "rsvpResvFwdProtocol": rsvpResvFwdProtocol,
       "rsvpResvFwdDestPort": rsvpResvFwdDestPort,
       "rsvpResvFwdPort": rsvpResvFwdPort,
       "rsvpResvFwdHopAddr": rsvpResvFwdHopAddr,
       "rsvpResvFwdHopLih": rsvpResvFwdHopLih,
       "rsvpResvFwdInterface": rsvpResvFwdInterface,
       "rsvpResvFwdService": rsvpResvFwdService,
       "rsvpResvFwdTSpecRate": rsvpResvFwdTSpecRate,
       "rsvpResvFwdTSpecPeakRate": rsvpResvFwdTSpecPeakRate,
       "rsvpResvFwdTSpecBurst": rsvpResvFwdTSpecBurst,
       "rsvpResvFwdTSpecMinTU": rsvpResvFwdTSpecMinTU,
       "rsvpResvFwdTSpecMaxTU": rsvpResvFwdTSpecMaxTU,
       "rsvpResvFwdRSpecRate": rsvpResvFwdRSpecRate,
       "rsvpResvFwdRSpecSlack": rsvpResvFwdRSpecSlack,
       "rsvpResvFwdInterval": rsvpResvFwdInterval,
       "rsvpResvFwdScope": rsvpResvFwdScope,
       "rsvpResvFwdShared": rsvpResvFwdShared,
       "rsvpResvFwdExplicit": rsvpResvFwdExplicit,
       "rsvpResvFwdRSVPHop": rsvpResvFwdRSVPHop,
       "rsvpResvFwdLastChange": rsvpResvFwdLastChange,
       "rsvpResvFwdPolicy": rsvpResvFwdPolicy,
       "rsvpResvFwdStatus": rsvpResvFwdStatus,
       "rsvpResvFwdTTL": rsvpResvFwdTTL,
       "rsvpResvFwdFlowId": rsvpResvFwdFlowId,
       "rsvpIfTable": rsvpIfTable,
       "rsvpIfEntry": rsvpIfEntry,
       "rsvpIfUdpNbrs": rsvpIfUdpNbrs,
       "rsvpIfIpNbrs": rsvpIfIpNbrs,
       "rsvpIfNbrs": rsvpIfNbrs,
       "rsvpIfRefreshBlockadeMultiple": rsvpIfRefreshBlockadeMultiple,
       "rsvpIfRefreshMultiple": rsvpIfRefreshMultiple,
       "rsvpIfTTL": rsvpIfTTL,
       "rsvpIfRefreshInterval": rsvpIfRefreshInterval,
       "rsvpIfRouteDelay": rsvpIfRouteDelay,
       "rsvpIfEnabled": rsvpIfEnabled,
       "rsvpIfUdpRequired": rsvpIfUdpRequired,
       "rsvpIfStatus": rsvpIfStatus,
       "rsvpNbrTable": rsvpNbrTable,
       "rsvpNbrEntry": rsvpNbrEntry,
       "rsvpNbrAddress": rsvpNbrAddress,
       "rsvpNbrProtocol": rsvpNbrProtocol,
       "rsvpNbrStatus": rsvpNbrStatus,
       "rsvpGenObjects": rsvpGenObjects,
       "rsvpBadPackets": rsvpBadPackets,
       "rsvpSenderNewIndex": rsvpSenderNewIndex,
       "rsvpResvNewIndex": rsvpResvNewIndex,
       "rsvpResvFwdNewIndex": rsvpResvFwdNewIndex,
       "rsvpNotificationsPrefix": rsvpNotificationsPrefix,
       "rsvpNotifications": rsvpNotifications,
       "newFlow": newFlow,
       "lostFlow": lostFlow,
       "rsvpConformance": rsvpConformance,
       "rsvpGroups": rsvpGroups,
       "rsvpSessionGroup": rsvpSessionGroup,
       "rsvpSenderGroup": rsvpSenderGroup,
       "rsvpResvGroup": rsvpResvGroup,
       "rsvpResvFwdGroup": rsvpResvFwdGroup,
       "rsvpIfGroup": rsvpIfGroup,
       "rsvpNbrGroup": rsvpNbrGroup,
       "rsvpNotificationGroup": rsvpNotificationGroup,
       "rsvpCompliances": rsvpCompliances,
       "rsvpCompliance": rsvpCompliance}
)
