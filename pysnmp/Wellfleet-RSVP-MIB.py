# SNMP MIB module (Wellfleet-RSVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RSVP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:02 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfReservationProtocolGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfReservationProtocolGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRsvpGroup_ObjectIdentity = ObjectIdentity
wfRsvpGroup = _WfRsvpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1)
)
_WfRsvp_ObjectIdentity = ObjectIdentity
wfRsvp = _WfRsvp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1)
)


class _WfRsvpDelete_Type(Integer32):
    """Custom type wfRsvpDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRsvpDelete_Type.__name__ = "Integer32"
_WfRsvpDelete_Object = MibScalar
wfRsvpDelete = _WfRsvpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 1),
    _WfRsvpDelete_Type()
)
wfRsvpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpDelete.setStatus("mandatory")


class _WfRsvpDisable_Type(Integer32):
    """Custom type wfRsvpDisable based on Integer32"""
    defaultValue = 1

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


_WfRsvpDisable_Type.__name__ = "Integer32"
_WfRsvpDisable_Object = MibScalar
wfRsvpDisable = _WfRsvpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 2),
    _WfRsvpDisable_Type()
)
wfRsvpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpDisable.setStatus("mandatory")


class _WfRsvpState_Type(Integer32):
    """Custom type wfRsvpState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfRsvpState_Type.__name__ = "Integer32"
_WfRsvpState_Object = MibScalar
wfRsvpState = _WfRsvpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 3),
    _WfRsvpState_Type()
)
wfRsvpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpState.setStatus("mandatory")


class _WfRsvpSoloistSlots_Type(Gauge32):
    """Custom type wfRsvpSoloistSlots based on Gauge32"""
    defaultValue = 4294705152

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpSoloistSlots_Type.__name__ = "Gauge32"
_WfRsvpSoloistSlots_Object = MibScalar
wfRsvpSoloistSlots = _WfRsvpSoloistSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 4),
    _WfRsvpSoloistSlots_Type()
)
wfRsvpSoloistSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpSoloistSlots.setStatus("mandatory")


class _WfRsvpInfoLogFilter_Type(Integer32):
    """Custom type wfRsvpInfoLogFilter based on Integer32"""
    defaultValue = 0


_WfRsvpInfoLogFilter_Object = MibScalar
wfRsvpInfoLogFilter = _WfRsvpInfoLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 5),
    _WfRsvpInfoLogFilter_Type()
)
wfRsvpInfoLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpInfoLogFilter.setStatus("mandatory")


class _WfRsvpDebugLogFilter_Type(Integer32):
    """Custom type wfRsvpDebugLogFilter based on Integer32"""
    defaultValue = 0


_WfRsvpDebugLogFilter_Object = MibScalar
wfRsvpDebugLogFilter = _WfRsvpDebugLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 6),
    _WfRsvpDebugLogFilter_Type()
)
wfRsvpDebugLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpDebugLogFilter.setStatus("mandatory")


class _WfRsvpTraceLogFilter_Type(Integer32):
    """Custom type wfRsvpTraceLogFilter based on Integer32"""
    defaultValue = 0


_WfRsvpTraceLogFilter_Object = MibScalar
wfRsvpTraceLogFilter = _WfRsvpTraceLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 7),
    _WfRsvpTraceLogFilter_Type()
)
wfRsvpTraceLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpTraceLogFilter.setStatus("mandatory")


class _WfRsvpTotalSenders_Type(Gauge32):
    """Custom type wfRsvpTotalSenders based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpTotalSenders_Type.__name__ = "Gauge32"
_WfRsvpTotalSenders_Object = MibScalar
wfRsvpTotalSenders = _WfRsvpTotalSenders_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 8),
    _WfRsvpTotalSenders_Type()
)
wfRsvpTotalSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpTotalSenders.setStatus("mandatory")


class _WfRsvpTotalReservations_Type(Gauge32):
    """Custom type wfRsvpTotalReservations based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpTotalReservations_Type.__name__ = "Gauge32"
_WfRsvpTotalReservations_Object = MibScalar
wfRsvpTotalReservations = _WfRsvpTotalReservations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 9),
    _WfRsvpTotalReservations_Type()
)
wfRsvpTotalReservations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpTotalReservations.setStatus("mandatory")


class _WfRsvpTotalReserved_Type(Gauge32):
    """Custom type wfRsvpTotalReserved based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpTotalReserved_Type.__name__ = "Gauge32"
_WfRsvpTotalReserved_Object = MibScalar
wfRsvpTotalReserved = _WfRsvpTotalReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 10),
    _WfRsvpTotalReserved_Type()
)
wfRsvpTotalReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpTotalReserved.setStatus("mandatory")


class _WfRsvpCurrentSoloistSlot_Type(Integer32):
    """Custom type wfRsvpCurrentSoloistSlot based on Integer32"""
    defaultValue = 0


_WfRsvpCurrentSoloistSlot_Object = MibScalar
wfRsvpCurrentSoloistSlot = _WfRsvpCurrentSoloistSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 1, 11),
    _WfRsvpCurrentSoloistSlot_Type()
)
wfRsvpCurrentSoloistSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpCurrentSoloistSlot.setStatus("mandatory")
_WfRsvpSessionTable_Object = MibTable
wfRsvpSessionTable = _WfRsvpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wfRsvpSessionTable.setStatus("mandatory")
_WfRsvpSessionEntry_Object = MibTableRow
wfRsvpSessionEntry = _WfRsvpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1)
)
wfRsvpSessionEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSessionDestAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSessionProtocol"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSessionPort"),
)
if mibBuilder.loadTexts:
    wfRsvpSessionEntry.setStatus("mandatory")
_WfRsvpSessionDestAddr_Type = IpAddress
_WfRsvpSessionDestAddr_Object = MibTableColumn
wfRsvpSessionDestAddr = _WfRsvpSessionDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 1),
    _WfRsvpSessionDestAddr_Type()
)
wfRsvpSessionDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionDestAddr.setStatus("mandatory")


class _WfRsvpSessionDestAddrLength_Type(Integer32):
    """Custom type wfRsvpSessionDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpSessionDestAddrLength_Type.__name__ = "Integer32"
_WfRsvpSessionDestAddrLength_Object = MibTableColumn
wfRsvpSessionDestAddrLength = _WfRsvpSessionDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 2),
    _WfRsvpSessionDestAddrLength_Type()
)
wfRsvpSessionDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionDestAddrLength.setStatus("mandatory")


class _WfRsvpSessionProtocol_Type(Integer32):
    """Custom type wfRsvpSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfRsvpSessionProtocol_Type.__name__ = "Integer32"
_WfRsvpSessionProtocol_Object = MibTableColumn
wfRsvpSessionProtocol = _WfRsvpSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 3),
    _WfRsvpSessionProtocol_Type()
)
wfRsvpSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionProtocol.setStatus("mandatory")


class _WfRsvpSessionPort_Type(Integer32):
    """Custom type wfRsvpSessionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSessionPort_Type.__name__ = "Integer32"
_WfRsvpSessionPort_Object = MibTableColumn
wfRsvpSessionPort = _WfRsvpSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 4),
    _WfRsvpSessionPort_Type()
)
wfRsvpSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionPort.setStatus("mandatory")


class _WfRsvpSessionSenders_Type(Gauge32):
    """Custom type wfRsvpSessionSenders based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpSessionSenders_Type.__name__ = "Gauge32"
_WfRsvpSessionSenders_Object = MibTableColumn
wfRsvpSessionSenders = _WfRsvpSessionSenders_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 5),
    _WfRsvpSessionSenders_Type()
)
wfRsvpSessionSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionSenders.setStatus("mandatory")


class _WfRsvpSessionReceivers_Type(Gauge32):
    """Custom type wfRsvpSessionReceivers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpSessionReceivers_Type.__name__ = "Gauge32"
_WfRsvpSessionReceivers_Object = MibTableColumn
wfRsvpSessionReceivers = _WfRsvpSessionReceivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 6),
    _WfRsvpSessionReceivers_Type()
)
wfRsvpSessionReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionReceivers.setStatus("mandatory")


class _WfRsvpSessionRequests_Type(Gauge32):
    """Custom type wfRsvpSessionRequests based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpSessionRequests_Type.__name__ = "Gauge32"
_WfRsvpSessionRequests_Object = MibTableColumn
wfRsvpSessionRequests = _WfRsvpSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 2, 1, 7),
    _WfRsvpSessionRequests_Type()
)
wfRsvpSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSessionRequests.setStatus("mandatory")
_WfRsvpSenderTable_Object = MibTable
wfRsvpSenderTable = _WfRsvpSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wfRsvpSenderTable.setStatus("mandatory")
_WfRsvpSenderEntry_Object = MibTableRow
wfRsvpSenderEntry = _WfRsvpSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1)
)
wfRsvpSenderEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSenderDestAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSenderProtocol"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSenderDestPort"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSenderAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpSenderPort"),
)
if mibBuilder.loadTexts:
    wfRsvpSenderEntry.setStatus("mandatory")
_WfRsvpSenderDestAddr_Type = IpAddress
_WfRsvpSenderDestAddr_Object = MibTableColumn
wfRsvpSenderDestAddr = _WfRsvpSenderDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 1),
    _WfRsvpSenderDestAddr_Type()
)
wfRsvpSenderDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderDestAddr.setStatus("mandatory")
_WfRsvpSenderAddr_Type = IpAddress
_WfRsvpSenderAddr_Object = MibTableColumn
wfRsvpSenderAddr = _WfRsvpSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 2),
    _WfRsvpSenderAddr_Type()
)
wfRsvpSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAddr.setStatus("mandatory")


class _WfRsvpSenderDestAddrLength_Type(Integer32):
    """Custom type wfRsvpSenderDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpSenderDestAddrLength_Type.__name__ = "Integer32"
_WfRsvpSenderDestAddrLength_Object = MibTableColumn
wfRsvpSenderDestAddrLength = _WfRsvpSenderDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 3),
    _WfRsvpSenderDestAddrLength_Type()
)
wfRsvpSenderDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderDestAddrLength.setStatus("mandatory")


class _WfRsvpSenderAddrLength_Type(Integer32):
    """Custom type wfRsvpSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpSenderAddrLength_Type.__name__ = "Integer32"
_WfRsvpSenderAddrLength_Object = MibTableColumn
wfRsvpSenderAddrLength = _WfRsvpSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 4),
    _WfRsvpSenderAddrLength_Type()
)
wfRsvpSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAddrLength.setStatus("mandatory")


class _WfRsvpSenderProtocol_Type(Integer32):
    """Custom type wfRsvpSenderProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfRsvpSenderProtocol_Type.__name__ = "Integer32"
_WfRsvpSenderProtocol_Object = MibTableColumn
wfRsvpSenderProtocol = _WfRsvpSenderProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 5),
    _WfRsvpSenderProtocol_Type()
)
wfRsvpSenderProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderProtocol.setStatus("mandatory")


class _WfRsvpSenderDestPort_Type(Integer32):
    """Custom type wfRsvpSenderDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderDestPort_Type.__name__ = "Integer32"
_WfRsvpSenderDestPort_Object = MibTableColumn
wfRsvpSenderDestPort = _WfRsvpSenderDestPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 6),
    _WfRsvpSenderDestPort_Type()
)
wfRsvpSenderDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderDestPort.setStatus("mandatory")


class _WfRsvpSenderPort_Type(Integer32):
    """Custom type wfRsvpSenderPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderPort_Type.__name__ = "Integer32"
_WfRsvpSenderPort_Object = MibTableColumn
wfRsvpSenderPort = _WfRsvpSenderPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 7),
    _WfRsvpSenderPort_Type()
)
wfRsvpSenderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderPort.setStatus("mandatory")
_WfRsvpSenderHopAddr_Type = IpAddress
_WfRsvpSenderHopAddr_Object = MibTableColumn
wfRsvpSenderHopAddr = _WfRsvpSenderHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 8),
    _WfRsvpSenderHopAddr_Type()
)
wfRsvpSenderHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderHopAddr.setStatus("mandatory")
_WfRsvpSenderHopLih_Type = Integer32
_WfRsvpSenderHopLih_Object = MibTableColumn
wfRsvpSenderHopLih = _WfRsvpSenderHopLih_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 9),
    _WfRsvpSenderHopLih_Type()
)
wfRsvpSenderHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderHopLih.setStatus("mandatory")
_WfRsvpSenderInterface_Type = Integer32
_WfRsvpSenderInterface_Object = MibTableColumn
wfRsvpSenderInterface = _WfRsvpSenderInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 10),
    _WfRsvpSenderInterface_Type()
)
wfRsvpSenderInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderInterface.setStatus("mandatory")


class _WfRsvpSenderTSpecRate_Type(Integer32):
    """Custom type wfRsvpSenderTSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderTSpecRate_Type.__name__ = "Integer32"
_WfRsvpSenderTSpecRate_Object = MibTableColumn
wfRsvpSenderTSpecRate = _WfRsvpSenderTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 11),
    _WfRsvpSenderTSpecRate_Type()
)
wfRsvpSenderTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderTSpecRate.setStatus("mandatory")


class _WfRsvpSenderTSpecPeakRate_Type(Integer32):
    """Custom type wfRsvpSenderTSpecPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderTSpecPeakRate_Type.__name__ = "Integer32"
_WfRsvpSenderTSpecPeakRate_Object = MibTableColumn
wfRsvpSenderTSpecPeakRate = _WfRsvpSenderTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 12),
    _WfRsvpSenderTSpecPeakRate_Type()
)
wfRsvpSenderTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderTSpecPeakRate.setStatus("mandatory")


class _WfRsvpSenderTSpecBurst_Type(Integer32):
    """Custom type wfRsvpSenderTSpecBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderTSpecBurst_Type.__name__ = "Integer32"
_WfRsvpSenderTSpecBurst_Object = MibTableColumn
wfRsvpSenderTSpecBurst = _WfRsvpSenderTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 13),
    _WfRsvpSenderTSpecBurst_Type()
)
wfRsvpSenderTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderTSpecBurst.setStatus("mandatory")


class _WfRsvpSenderTSpecMinTU_Type(Integer32):
    """Custom type wfRsvpSenderTSpecMinTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderTSpecMinTU_Type.__name__ = "Integer32"
_WfRsvpSenderTSpecMinTU_Object = MibTableColumn
wfRsvpSenderTSpecMinTU = _WfRsvpSenderTSpecMinTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 14),
    _WfRsvpSenderTSpecMinTU_Type()
)
wfRsvpSenderTSpecMinTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderTSpecMinTU.setStatus("mandatory")


class _WfRsvpSenderTSpecMaxTU_Type(Integer32):
    """Custom type wfRsvpSenderTSpecMaxTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderTSpecMaxTU_Type.__name__ = "Integer32"
_WfRsvpSenderTSpecMaxTU_Object = MibTableColumn
wfRsvpSenderTSpecMaxTU = _WfRsvpSenderTSpecMaxTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 15),
    _WfRsvpSenderTSpecMaxTU_Type()
)
wfRsvpSenderTSpecMaxTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderTSpecMaxTU.setStatus("mandatory")


class _WfRsvpSenderInterval_Type(Integer32):
    """Custom type wfRsvpSenderInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderInterval_Type.__name__ = "Integer32"
_WfRsvpSenderInterval_Object = MibTableColumn
wfRsvpSenderInterval = _WfRsvpSenderInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 16),
    _WfRsvpSenderInterval_Type()
)
wfRsvpSenderInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderInterval.setStatus("mandatory")


class _WfRsvpSenderRSVPHop_Type(Integer32):
    """Custom type wfRsvpSenderRSVPHop based on Integer32"""
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


_WfRsvpSenderRSVPHop_Type.__name__ = "Integer32"
_WfRsvpSenderRSVPHop_Object = MibTableColumn
wfRsvpSenderRSVPHop = _WfRsvpSenderRSVPHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 17),
    _WfRsvpSenderRSVPHop_Type()
)
wfRsvpSenderRSVPHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderRSVPHop.setStatus("mandatory")
_WfRsvpSenderLastChange_Type = Integer32
_WfRsvpSenderLastChange_Object = MibTableColumn
wfRsvpSenderLastChange = _WfRsvpSenderLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 18),
    _WfRsvpSenderLastChange_Type()
)
wfRsvpSenderLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderLastChange.setStatus("mandatory")
_WfRsvpSenderPSBTimeout_Type = Integer32
_WfRsvpSenderPSBTimeout_Object = MibTableColumn
wfRsvpSenderPSBTimeout = _WfRsvpSenderPSBTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 19),
    _WfRsvpSenderPSBTimeout_Type()
)
wfRsvpSenderPSBTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderPSBTimeout.setStatus("mandatory")


class _WfRsvpSenderPolicy_Type(OctetString):
    """Custom type wfRsvpSenderPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 65536),
    )


_WfRsvpSenderPolicy_Type.__name__ = "OctetString"
_WfRsvpSenderPolicy_Object = MibTableColumn
wfRsvpSenderPolicy = _WfRsvpSenderPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 20),
    _WfRsvpSenderPolicy_Type()
)
wfRsvpSenderPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderPolicy.setStatus("mandatory")


class _WfRsvpSenderAdspecBreak_Type(Integer32):
    """Custom type wfRsvpSenderAdspecBreak based on Integer32"""
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


_WfRsvpSenderAdspecBreak_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecBreak_Object = MibTableColumn
wfRsvpSenderAdspecBreak = _WfRsvpSenderAdspecBreak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 21),
    _WfRsvpSenderAdspecBreak_Type()
)
wfRsvpSenderAdspecBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecBreak.setStatus("mandatory")


class _WfRsvpSenderAdspecHopCount_Type(Integer32):
    """Custom type wfRsvpSenderAdspecHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderAdspecHopCount_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecHopCount_Object = MibTableColumn
wfRsvpSenderAdspecHopCount = _WfRsvpSenderAdspecHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 22),
    _WfRsvpSenderAdspecHopCount_Type()
)
wfRsvpSenderAdspecHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecHopCount.setStatus("mandatory")


class _WfRsvpSenderAdspecPathBw_Type(Integer32):
    """Custom type wfRsvpSenderAdspecPathBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderAdspecPathBw_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecPathBw_Object = MibTableColumn
wfRsvpSenderAdspecPathBw = _WfRsvpSenderAdspecPathBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 23),
    _WfRsvpSenderAdspecPathBw_Type()
)
wfRsvpSenderAdspecPathBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecPathBw.setStatus("mandatory")
_WfRsvpSenderAdspecMinLatency_Type = Integer32
_WfRsvpSenderAdspecMinLatency_Object = MibTableColumn
wfRsvpSenderAdspecMinLatency = _WfRsvpSenderAdspecMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 24),
    _WfRsvpSenderAdspecMinLatency_Type()
)
wfRsvpSenderAdspecMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecMinLatency.setStatus("mandatory")


class _WfRsvpSenderAdspecMtu_Type(Integer32):
    """Custom type wfRsvpSenderAdspecMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderAdspecMtu_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecMtu_Object = MibTableColumn
wfRsvpSenderAdspecMtu = _WfRsvpSenderAdspecMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 25),
    _WfRsvpSenderAdspecMtu_Type()
)
wfRsvpSenderAdspecMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecMtu.setStatus("mandatory")


class _WfRsvpSenderAdspecGSSvc_Type(Integer32):
    """Custom type wfRsvpSenderAdspecGSSvc based on Integer32"""
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


_WfRsvpSenderAdspecGSSvc_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecGSSvc_Object = MibTableColumn
wfRsvpSenderAdspecGSSvc = _WfRsvpSenderAdspecGSSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 26),
    _WfRsvpSenderAdspecGSSvc_Type()
)
wfRsvpSenderAdspecGSSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSSvc.setStatus("mandatory")


class _WfRsvpSenderAdspecGSBreak_Type(Integer32):
    """Custom type wfRsvpSenderAdspecGSBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flase", 2),
          ("true", 1))
    )


_WfRsvpSenderAdspecGSBreak_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecGSBreak_Object = MibTableColumn
wfRsvpSenderAdspecGSBreak = _WfRsvpSenderAdspecGSBreak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 27),
    _WfRsvpSenderAdspecGSBreak_Type()
)
wfRsvpSenderAdspecGSBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSBreak.setStatus("mandatory")
_WfRsvpSenderAdspecGSCtot_Type = Integer32
_WfRsvpSenderAdspecGSCtot_Object = MibTableColumn
wfRsvpSenderAdspecGSCtot = _WfRsvpSenderAdspecGSCtot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 28),
    _WfRsvpSenderAdspecGSCtot_Type()
)
wfRsvpSenderAdspecGSCtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSCtot.setStatus("mandatory")
_WfRsvpSenderAdspecGSDtot_Type = Integer32
_WfRsvpSenderAdspecGSDtot_Object = MibTableColumn
wfRsvpSenderAdspecGSDtot = _WfRsvpSenderAdspecGSDtot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 29),
    _WfRsvpSenderAdspecGSDtot_Type()
)
wfRsvpSenderAdspecGSDtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSDtot.setStatus("mandatory")
_WfRsvpSenderAdspecGSCsum_Type = Integer32
_WfRsvpSenderAdspecGSCsum_Object = MibTableColumn
wfRsvpSenderAdspecGSCsum = _WfRsvpSenderAdspecGSCsum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 30),
    _WfRsvpSenderAdspecGSCsum_Type()
)
wfRsvpSenderAdspecGSCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSCsum.setStatus("mandatory")
_WfRsvpSenderAdspecGSDsum_Type = Integer32
_WfRsvpSenderAdspecGSDsum_Object = MibTableColumn
wfRsvpSenderAdspecGSDsum = _WfRsvpSenderAdspecGSDsum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 31),
    _WfRsvpSenderAdspecGSDsum_Type()
)
wfRsvpSenderAdspecGSDsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSDsum.setStatus("mandatory")


class _WfRsvpSenderAdspecGSHopCount_Type(Integer32):
    """Custom type wfRsvpSenderAdspecGSHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderAdspecGSHopCount_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecGSHopCount_Object = MibTableColumn
wfRsvpSenderAdspecGSHopCount = _WfRsvpSenderAdspecGSHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 32),
    _WfRsvpSenderAdspecGSHopCount_Type()
)
wfRsvpSenderAdspecGSHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSHopCount.setStatus("mandatory")


class _WfRsvpSenderAdspecGSPathBw_Type(Integer32):
    """Custom type wfRsvpSenderAdspecGSPathBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderAdspecGSPathBw_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecGSPathBw_Object = MibTableColumn
wfRsvpSenderAdspecGSPathBw = _WfRsvpSenderAdspecGSPathBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 33),
    _WfRsvpSenderAdspecGSPathBw_Type()
)
wfRsvpSenderAdspecGSPathBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSPathBw.setStatus("mandatory")
_WfRsvpSenderAdspecGSMinLatency_Type = Integer32
_WfRsvpSenderAdspecGSMinLatency_Object = MibTableColumn
wfRsvpSenderAdspecGSMinLatency = _WfRsvpSenderAdspecGSMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 34),
    _WfRsvpSenderAdspecGSMinLatency_Type()
)
wfRsvpSenderAdspecGSMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSMinLatency.setStatus("mandatory")


class _WfRsvpSenderAdspecGSMtu_Type(Integer32):
    """Custom type wfRsvpSenderAdspecGSMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderAdspecGSMtu_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecGSMtu_Object = MibTableColumn
wfRsvpSenderAdspecGSMtu = _WfRsvpSenderAdspecGSMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 35),
    _WfRsvpSenderAdspecGSMtu_Type()
)
wfRsvpSenderAdspecGSMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecGSMtu.setStatus("mandatory")


class _WfRsvpSenderAdspecCLSvc_Type(Integer32):
    """Custom type wfRsvpSenderAdspecCLSvc based on Integer32"""
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


_WfRsvpSenderAdspecCLSvc_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecCLSvc_Object = MibTableColumn
wfRsvpSenderAdspecCLSvc = _WfRsvpSenderAdspecCLSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 36),
    _WfRsvpSenderAdspecCLSvc_Type()
)
wfRsvpSenderAdspecCLSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecCLSvc.setStatus("mandatory")


class _WfRsvpSenderAdspecCLBreak_Type(Integer32):
    """Custom type wfRsvpSenderAdspecCLBreak based on Integer32"""
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


_WfRsvpSenderAdspecCLBreak_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecCLBreak_Object = MibTableColumn
wfRsvpSenderAdspecCLBreak = _WfRsvpSenderAdspecCLBreak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 37),
    _WfRsvpSenderAdspecCLBreak_Type()
)
wfRsvpSenderAdspecCLBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecCLBreak.setStatus("mandatory")


class _WfRsvpSenderAdspecCLHopCount_Type(Integer32):
    """Custom type wfRsvpSenderAdspecCLHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderAdspecCLHopCount_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecCLHopCount_Object = MibTableColumn
wfRsvpSenderAdspecCLHopCount = _WfRsvpSenderAdspecCLHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 38),
    _WfRsvpSenderAdspecCLHopCount_Type()
)
wfRsvpSenderAdspecCLHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecCLHopCount.setStatus("mandatory")


class _WfRsvpSenderAdspecCLPathBw_Type(Integer32):
    """Custom type wfRsvpSenderAdspecCLPathBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpSenderAdspecCLPathBw_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecCLPathBw_Object = MibTableColumn
wfRsvpSenderAdspecCLPathBw = _WfRsvpSenderAdspecCLPathBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 39),
    _WfRsvpSenderAdspecCLPathBw_Type()
)
wfRsvpSenderAdspecCLPathBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecCLPathBw.setStatus("mandatory")
_WfRsvpSenderAdspecCLMinLatency_Type = Integer32
_WfRsvpSenderAdspecCLMinLatency_Object = MibTableColumn
wfRsvpSenderAdspecCLMinLatency = _WfRsvpSenderAdspecCLMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 40),
    _WfRsvpSenderAdspecCLMinLatency_Type()
)
wfRsvpSenderAdspecCLMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecCLMinLatency.setStatus("mandatory")


class _WfRsvpSenderAdspecCLMtu_Type(Integer32):
    """Custom type wfRsvpSenderAdspecCLMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpSenderAdspecCLMtu_Type.__name__ = "Integer32"
_WfRsvpSenderAdspecCLMtu_Object = MibTableColumn
wfRsvpSenderAdspecCLMtu = _WfRsvpSenderAdspecCLMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 41),
    _WfRsvpSenderAdspecCLMtu_Type()
)
wfRsvpSenderAdspecCLMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderAdspecCLMtu.setStatus("mandatory")


class _WfRsvpSenderStatus_Type(Integer32):
    """Custom type wfRsvpSenderStatus based on Integer32"""
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


_WfRsvpSenderStatus_Type.__name__ = "Integer32"
_WfRsvpSenderStatus_Object = MibTableColumn
wfRsvpSenderStatus = _WfRsvpSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 3, 1, 42),
    _WfRsvpSenderStatus_Type()
)
wfRsvpSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpSenderStatus.setStatus("mandatory")
_WfRsvpResvTable_Object = MibTable
wfRsvpResvTable = _WfRsvpResvTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wfRsvpResvTable.setStatus("mandatory")
_WfRsvpResvEntry_Object = MibTableRow
wfRsvpResvEntry = _WfRsvpResvEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1)
)
wfRsvpResvEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvDestAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvProtocol"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvDestPort"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvSenderAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvPort"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvInterface"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvHopAddr"),
)
if mibBuilder.loadTexts:
    wfRsvpResvEntry.setStatus("mandatory")
_WfRsvpResvDestAddr_Type = IpAddress
_WfRsvpResvDestAddr_Object = MibTableColumn
wfRsvpResvDestAddr = _WfRsvpResvDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 1),
    _WfRsvpResvDestAddr_Type()
)
wfRsvpResvDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvDestAddr.setStatus("mandatory")
_WfRsvpResvSenderAddr_Type = IpAddress
_WfRsvpResvSenderAddr_Object = MibTableColumn
wfRsvpResvSenderAddr = _WfRsvpResvSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 2),
    _WfRsvpResvSenderAddr_Type()
)
wfRsvpResvSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvSenderAddr.setStatus("mandatory")


class _WfRsvpResvDestAddrLength_Type(Integer32):
    """Custom type wfRsvpResvDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpResvDestAddrLength_Type.__name__ = "Integer32"
_WfRsvpResvDestAddrLength_Object = MibTableColumn
wfRsvpResvDestAddrLength = _WfRsvpResvDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 3),
    _WfRsvpResvDestAddrLength_Type()
)
wfRsvpResvDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvDestAddrLength.setStatus("mandatory")


class _WfRsvpResvSenderAddrLength_Type(Integer32):
    """Custom type wfRsvpResvSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpResvSenderAddrLength_Type.__name__ = "Integer32"
_WfRsvpResvSenderAddrLength_Object = MibTableColumn
wfRsvpResvSenderAddrLength = _WfRsvpResvSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 4),
    _WfRsvpResvSenderAddrLength_Type()
)
wfRsvpResvSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvSenderAddrLength.setStatus("mandatory")


class _WfRsvpResvProtocol_Type(Integer32):
    """Custom type wfRsvpResvProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfRsvpResvProtocol_Type.__name__ = "Integer32"
_WfRsvpResvProtocol_Object = MibTableColumn
wfRsvpResvProtocol = _WfRsvpResvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 5),
    _WfRsvpResvProtocol_Type()
)
wfRsvpResvProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvProtocol.setStatus("mandatory")


class _WfRsvpResvDestPort_Type(Integer32):
    """Custom type wfRsvpResvDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpResvDestPort_Type.__name__ = "Integer32"
_WfRsvpResvDestPort_Object = MibTableColumn
wfRsvpResvDestPort = _WfRsvpResvDestPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 6),
    _WfRsvpResvDestPort_Type()
)
wfRsvpResvDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvDestPort.setStatus("mandatory")


class _WfRsvpResvPort_Type(Integer32):
    """Custom type wfRsvpResvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpResvPort_Type.__name__ = "Integer32"
_WfRsvpResvPort_Object = MibTableColumn
wfRsvpResvPort = _WfRsvpResvPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 7),
    _WfRsvpResvPort_Type()
)
wfRsvpResvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvPort.setStatus("mandatory")
_WfRsvpResvHopAddr_Type = IpAddress
_WfRsvpResvHopAddr_Object = MibTableColumn
wfRsvpResvHopAddr = _WfRsvpResvHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 8),
    _WfRsvpResvHopAddr_Type()
)
wfRsvpResvHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvHopAddr.setStatus("mandatory")
_WfRsvpResvHopLih_Type = Integer32
_WfRsvpResvHopLih_Object = MibTableColumn
wfRsvpResvHopLih = _WfRsvpResvHopLih_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 9),
    _WfRsvpResvHopLih_Type()
)
wfRsvpResvHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvHopLih.setStatus("mandatory")
_WfRsvpResvInterface_Type = Integer32
_WfRsvpResvInterface_Object = MibTableColumn
wfRsvpResvInterface = _WfRsvpResvInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 10),
    _WfRsvpResvInterface_Type()
)
wfRsvpResvInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvInterface.setStatus("mandatory")


class _WfRsvpResvService_Type(Integer32):
    """Custom type wfRsvpResvService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("controlledDelay", 1),
          ("controlledLoad", 5),
          ("guaranteedDelay", 2),
          ("predictive", 3))
    )


_WfRsvpResvService_Type.__name__ = "Integer32"
_WfRsvpResvService_Object = MibTableColumn
wfRsvpResvService = _WfRsvpResvService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 11),
    _WfRsvpResvService_Type()
)
wfRsvpResvService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvService.setStatus("mandatory")


class _WfRsvpResvTSpecRate_Type(Integer32):
    """Custom type wfRsvpResvTSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvTSpecRate_Type.__name__ = "Integer32"
_WfRsvpResvTSpecRate_Object = MibTableColumn
wfRsvpResvTSpecRate = _WfRsvpResvTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 12),
    _WfRsvpResvTSpecRate_Type()
)
wfRsvpResvTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvTSpecRate.setStatus("mandatory")


class _WfRsvpResvTSpecPeakRate_Type(Integer32):
    """Custom type wfRsvpResvTSpecPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvTSpecPeakRate_Type.__name__ = "Integer32"
_WfRsvpResvTSpecPeakRate_Object = MibTableColumn
wfRsvpResvTSpecPeakRate = _WfRsvpResvTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 13),
    _WfRsvpResvTSpecPeakRate_Type()
)
wfRsvpResvTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvTSpecPeakRate.setStatus("mandatory")


class _WfRsvpResvTSpecBurst_Type(Integer32):
    """Custom type wfRsvpResvTSpecBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvTSpecBurst_Type.__name__ = "Integer32"
_WfRsvpResvTSpecBurst_Object = MibTableColumn
wfRsvpResvTSpecBurst = _WfRsvpResvTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 14),
    _WfRsvpResvTSpecBurst_Type()
)
wfRsvpResvTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvTSpecBurst.setStatus("mandatory")


class _WfRsvpResvTSpecMinTU_Type(Integer32):
    """Custom type wfRsvpResvTSpecMinTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvTSpecMinTU_Type.__name__ = "Integer32"
_WfRsvpResvTSpecMinTU_Object = MibTableColumn
wfRsvpResvTSpecMinTU = _WfRsvpResvTSpecMinTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 15),
    _WfRsvpResvTSpecMinTU_Type()
)
wfRsvpResvTSpecMinTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvTSpecMinTU.setStatus("mandatory")


class _WfRsvpResvTSpecMaxTU_Type(Integer32):
    """Custom type wfRsvpResvTSpecMaxTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvTSpecMaxTU_Type.__name__ = "Integer32"
_WfRsvpResvTSpecMaxTU_Object = MibTableColumn
wfRsvpResvTSpecMaxTU = _WfRsvpResvTSpecMaxTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 16),
    _WfRsvpResvTSpecMaxTU_Type()
)
wfRsvpResvTSpecMaxTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvTSpecMaxTU.setStatus("mandatory")


class _WfRsvpResvTSpecLevel_Type(Integer32):
    """Custom type wfRsvpResvTSpecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WfRsvpResvTSpecLevel_Type.__name__ = "Integer32"
_WfRsvpResvTSpecLevel_Object = MibTableColumn
wfRsvpResvTSpecLevel = _WfRsvpResvTSpecLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 17),
    _WfRsvpResvTSpecLevel_Type()
)
wfRsvpResvTSpecLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvTSpecLevel.setStatus("mandatory")


class _WfRsvpResvRSpecRate_Type(Integer32):
    """Custom type wfRsvpResvRSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvRSpecRate_Type.__name__ = "Integer32"
_WfRsvpResvRSpecRate_Object = MibTableColumn
wfRsvpResvRSpecRate = _WfRsvpResvRSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 18),
    _WfRsvpResvRSpecRate_Type()
)
wfRsvpResvRSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvRSpecRate.setStatus("mandatory")
_WfRsvpResvRSpecSlack_Type = Integer32
_WfRsvpResvRSpecSlack_Object = MibTableColumn
wfRsvpResvRSpecSlack = _WfRsvpResvRSpecSlack_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 19),
    _WfRsvpResvRSpecSlack_Type()
)
wfRsvpResvRSpecSlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvRSpecSlack.setStatus("mandatory")


class _WfRsvpResvInterval_Type(Integer32):
    """Custom type wfRsvpResvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvInterval_Type.__name__ = "Integer32"
_WfRsvpResvInterval_Object = MibTableColumn
wfRsvpResvInterval = _WfRsvpResvInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 20),
    _WfRsvpResvInterval_Type()
)
wfRsvpResvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvInterval.setStatus("mandatory")


class _WfRsvpResvScope_Type(OctetString):
    """Custom type wfRsvpResvScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfRsvpResvScope_Type.__name__ = "OctetString"
_WfRsvpResvScope_Object = MibTableColumn
wfRsvpResvScope = _WfRsvpResvScope_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 21),
    _WfRsvpResvScope_Type()
)
wfRsvpResvScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvScope.setStatus("mandatory")


class _WfRsvpResvShared_Type(Integer32):
    """Custom type wfRsvpResvShared based on Integer32"""
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


_WfRsvpResvShared_Type.__name__ = "Integer32"
_WfRsvpResvShared_Object = MibTableColumn
wfRsvpResvShared = _WfRsvpResvShared_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 22),
    _WfRsvpResvShared_Type()
)
wfRsvpResvShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvShared.setStatus("mandatory")


class _WfRsvpResvExplicit_Type(Integer32):
    """Custom type wfRsvpResvExplicit based on Integer32"""
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


_WfRsvpResvExplicit_Type.__name__ = "Integer32"
_WfRsvpResvExplicit_Object = MibTableColumn
wfRsvpResvExplicit = _WfRsvpResvExplicit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 23),
    _WfRsvpResvExplicit_Type()
)
wfRsvpResvExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvExplicit.setStatus("mandatory")


class _WfRsvpResvRSVPHop_Type(Integer32):
    """Custom type wfRsvpResvRSVPHop based on Integer32"""
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


_WfRsvpResvRSVPHop_Type.__name__ = "Integer32"
_WfRsvpResvRSVPHop_Object = MibTableColumn
wfRsvpResvRSVPHop = _WfRsvpResvRSVPHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 24),
    _WfRsvpResvRSVPHop_Type()
)
wfRsvpResvRSVPHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvRSVPHop.setStatus("mandatory")
_WfRsvpResvLastChange_Type = Integer32
_WfRsvpResvLastChange_Object = MibTableColumn
wfRsvpResvLastChange = _WfRsvpResvLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 25),
    _WfRsvpResvLastChange_Type()
)
wfRsvpResvLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvLastChange.setStatus("mandatory")
_WfRsvpResvRSBTimeout_Type = Integer32
_WfRsvpResvRSBTimeout_Object = MibTableColumn
wfRsvpResvRSBTimeout = _WfRsvpResvRSBTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 26),
    _WfRsvpResvRSBTimeout_Type()
)
wfRsvpResvRSBTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvRSBTimeout.setStatus("mandatory")


class _WfRsvpResvPolicy_Type(OctetString):
    """Custom type wfRsvpResvPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfRsvpResvPolicy_Type.__name__ = "OctetString"
_WfRsvpResvPolicy_Object = MibTableColumn
wfRsvpResvPolicy = _WfRsvpResvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 27),
    _WfRsvpResvPolicy_Type()
)
wfRsvpResvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvPolicy.setStatus("mandatory")


class _WfRsvpResvStatus_Type(Integer32):
    """Custom type wfRsvpResvStatus based on Integer32"""
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


_WfRsvpResvStatus_Type.__name__ = "Integer32"
_WfRsvpResvStatus_Object = MibTableColumn
wfRsvpResvStatus = _WfRsvpResvStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 4, 1, 28),
    _WfRsvpResvStatus_Type()
)
wfRsvpResvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvStatus.setStatus("mandatory")
_WfRsvpResvFwdTable_Object = MibTable
wfRsvpResvFwdTable = _WfRsvpResvFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wfRsvpResvFwdTable.setStatus("mandatory")
_WfRsvpResvFwdEntry_Object = MibTableRow
wfRsvpResvFwdEntry = _WfRsvpResvFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1)
)
wfRsvpResvFwdEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdDestAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdProtocol"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdDestPort"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdSenderAddr"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdPort"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdInterface"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpResvFwdHopAddr"),
)
if mibBuilder.loadTexts:
    wfRsvpResvFwdEntry.setStatus("mandatory")
_WfRsvpResvFwdDestAddr_Type = IpAddress
_WfRsvpResvFwdDestAddr_Object = MibTableColumn
wfRsvpResvFwdDestAddr = _WfRsvpResvFwdDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 1),
    _WfRsvpResvFwdDestAddr_Type()
)
wfRsvpResvFwdDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdDestAddr.setStatus("mandatory")
_WfRsvpResvFwdSenderAddr_Type = IpAddress
_WfRsvpResvFwdSenderAddr_Object = MibTableColumn
wfRsvpResvFwdSenderAddr = _WfRsvpResvFwdSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 2),
    _WfRsvpResvFwdSenderAddr_Type()
)
wfRsvpResvFwdSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdSenderAddr.setStatus("mandatory")


class _WfRsvpResvFwdDestAddrLength_Type(Integer32):
    """Custom type wfRsvpResvFwdDestAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpResvFwdDestAddrLength_Type.__name__ = "Integer32"
_WfRsvpResvFwdDestAddrLength_Object = MibTableColumn
wfRsvpResvFwdDestAddrLength = _WfRsvpResvFwdDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 3),
    _WfRsvpResvFwdDestAddrLength_Type()
)
wfRsvpResvFwdDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdDestAddrLength.setStatus("mandatory")


class _WfRsvpResvFwdSenderAddrLength_Type(Integer32):
    """Custom type wfRsvpResvFwdSenderAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfRsvpResvFwdSenderAddrLength_Type.__name__ = "Integer32"
_WfRsvpResvFwdSenderAddrLength_Object = MibTableColumn
wfRsvpResvFwdSenderAddrLength = _WfRsvpResvFwdSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 4),
    _WfRsvpResvFwdSenderAddrLength_Type()
)
wfRsvpResvFwdSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdSenderAddrLength.setStatus("mandatory")


class _WfRsvpResvFwdProtocol_Type(Integer32):
    """Custom type wfRsvpResvFwdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfRsvpResvFwdProtocol_Type.__name__ = "Integer32"
_WfRsvpResvFwdProtocol_Object = MibTableColumn
wfRsvpResvFwdProtocol = _WfRsvpResvFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 5),
    _WfRsvpResvFwdProtocol_Type()
)
wfRsvpResvFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdProtocol.setStatus("mandatory")


class _WfRsvpResvFwdDestPort_Type(Integer32):
    """Custom type wfRsvpResvFwdDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpResvFwdDestPort_Type.__name__ = "Integer32"
_WfRsvpResvFwdDestPort_Object = MibTableColumn
wfRsvpResvFwdDestPort = _WfRsvpResvFwdDestPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 6),
    _WfRsvpResvFwdDestPort_Type()
)
wfRsvpResvFwdDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdDestPort.setStatus("mandatory")


class _WfRsvpResvFwdPort_Type(Integer32):
    """Custom type wfRsvpResvFwdPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfRsvpResvFwdPort_Type.__name__ = "Integer32"
_WfRsvpResvFwdPort_Object = MibTableColumn
wfRsvpResvFwdPort = _WfRsvpResvFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 7),
    _WfRsvpResvFwdPort_Type()
)
wfRsvpResvFwdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdPort.setStatus("mandatory")
_WfRsvpResvFwdHopAddr_Type = IpAddress
_WfRsvpResvFwdHopAddr_Object = MibTableColumn
wfRsvpResvFwdHopAddr = _WfRsvpResvFwdHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 8),
    _WfRsvpResvFwdHopAddr_Type()
)
wfRsvpResvFwdHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdHopAddr.setStatus("mandatory")
_WfRsvpResvFwdHopLih_Type = Integer32
_WfRsvpResvFwdHopLih_Object = MibTableColumn
wfRsvpResvFwdHopLih = _WfRsvpResvFwdHopLih_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 9),
    _WfRsvpResvFwdHopLih_Type()
)
wfRsvpResvFwdHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdHopLih.setStatus("mandatory")
_WfRsvpResvFwdInterface_Type = Integer32
_WfRsvpResvFwdInterface_Object = MibTableColumn
wfRsvpResvFwdInterface = _WfRsvpResvFwdInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 10),
    _WfRsvpResvFwdInterface_Type()
)
wfRsvpResvFwdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdInterface.setStatus("mandatory")


class _WfRsvpResvFwdService_Type(Integer32):
    """Custom type wfRsvpResvFwdService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("controlledDelay", 1),
          ("controlledLoad", 5),
          ("guaranteedDelay", 2),
          ("predictive", 3))
    )


_WfRsvpResvFwdService_Type.__name__ = "Integer32"
_WfRsvpResvFwdService_Object = MibTableColumn
wfRsvpResvFwdService = _WfRsvpResvFwdService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 11),
    _WfRsvpResvFwdService_Type()
)
wfRsvpResvFwdService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdService.setStatus("mandatory")


class _WfRsvpResvFwdTSpecRate_Type(Integer32):
    """Custom type wfRsvpResvFwdTSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdTSpecRate_Type.__name__ = "Integer32"
_WfRsvpResvFwdTSpecRate_Object = MibTableColumn
wfRsvpResvFwdTSpecRate = _WfRsvpResvFwdTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 12),
    _WfRsvpResvFwdTSpecRate_Type()
)
wfRsvpResvFwdTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdTSpecRate.setStatus("mandatory")


class _WfRsvpResvFwdTSpecPeakRate_Type(Integer32):
    """Custom type wfRsvpResvFwdTSpecPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdTSpecPeakRate_Type.__name__ = "Integer32"
_WfRsvpResvFwdTSpecPeakRate_Object = MibTableColumn
wfRsvpResvFwdTSpecPeakRate = _WfRsvpResvFwdTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 13),
    _WfRsvpResvFwdTSpecPeakRate_Type()
)
wfRsvpResvFwdTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdTSpecPeakRate.setStatus("mandatory")


class _WfRsvpResvFwdTSpecBurst_Type(Integer32):
    """Custom type wfRsvpResvFwdTSpecBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdTSpecBurst_Type.__name__ = "Integer32"
_WfRsvpResvFwdTSpecBurst_Object = MibTableColumn
wfRsvpResvFwdTSpecBurst = _WfRsvpResvFwdTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 14),
    _WfRsvpResvFwdTSpecBurst_Type()
)
wfRsvpResvFwdTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdTSpecBurst.setStatus("mandatory")


class _WfRsvpResvFwdTSpecMinTU_Type(Integer32):
    """Custom type wfRsvpResvFwdTSpecMinTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdTSpecMinTU_Type.__name__ = "Integer32"
_WfRsvpResvFwdTSpecMinTU_Object = MibTableColumn
wfRsvpResvFwdTSpecMinTU = _WfRsvpResvFwdTSpecMinTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 15),
    _WfRsvpResvFwdTSpecMinTU_Type()
)
wfRsvpResvFwdTSpecMinTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdTSpecMinTU.setStatus("mandatory")


class _WfRsvpResvFwdTSpecMaxTU_Type(Integer32):
    """Custom type wfRsvpResvFwdTSpecMaxTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdTSpecMaxTU_Type.__name__ = "Integer32"
_WfRsvpResvFwdTSpecMaxTU_Object = MibTableColumn
wfRsvpResvFwdTSpecMaxTU = _WfRsvpResvFwdTSpecMaxTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 16),
    _WfRsvpResvFwdTSpecMaxTU_Type()
)
wfRsvpResvFwdTSpecMaxTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdTSpecMaxTU.setStatus("mandatory")


class _WfRsvpResvFwdTSpecLevel_Type(Integer32):
    """Custom type wfRsvpResvFwdTSpecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WfRsvpResvFwdTSpecLevel_Type.__name__ = "Integer32"
_WfRsvpResvFwdTSpecLevel_Object = MibTableColumn
wfRsvpResvFwdTSpecLevel = _WfRsvpResvFwdTSpecLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 17),
    _WfRsvpResvFwdTSpecLevel_Type()
)
wfRsvpResvFwdTSpecLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdTSpecLevel.setStatus("mandatory")


class _WfRsvpResvFwdRSpecRate_Type(Integer32):
    """Custom type wfRsvpResvFwdRSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdRSpecRate_Type.__name__ = "Integer32"
_WfRsvpResvFwdRSpecRate_Object = MibTableColumn
wfRsvpResvFwdRSpecRate = _WfRsvpResvFwdRSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 18),
    _WfRsvpResvFwdRSpecRate_Type()
)
wfRsvpResvFwdRSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdRSpecRate.setStatus("mandatory")
_WfRsvpResvFwdRSpecSlack_Type = Integer32
_WfRsvpResvFwdRSpecSlack_Object = MibTableColumn
wfRsvpResvFwdRSpecSlack = _WfRsvpResvFwdRSpecSlack_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 19),
    _WfRsvpResvFwdRSpecSlack_Type()
)
wfRsvpResvFwdRSpecSlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdRSpecSlack.setStatus("mandatory")


class _WfRsvpResvFwdInterval_Type(Integer32):
    """Custom type wfRsvpResvFwdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfRsvpResvFwdInterval_Type.__name__ = "Integer32"
_WfRsvpResvFwdInterval_Object = MibTableColumn
wfRsvpResvFwdInterval = _WfRsvpResvFwdInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 20),
    _WfRsvpResvFwdInterval_Type()
)
wfRsvpResvFwdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdInterval.setStatus("mandatory")


class _WfRsvpResvFwdScope_Type(OctetString):
    """Custom type wfRsvpResvFwdScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfRsvpResvFwdScope_Type.__name__ = "OctetString"
_WfRsvpResvFwdScope_Object = MibTableColumn
wfRsvpResvFwdScope = _WfRsvpResvFwdScope_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 21),
    _WfRsvpResvFwdScope_Type()
)
wfRsvpResvFwdScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdScope.setStatus("mandatory")


class _WfRsvpResvFwdShared_Type(Integer32):
    """Custom type wfRsvpResvFwdShared based on Integer32"""
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


_WfRsvpResvFwdShared_Type.__name__ = "Integer32"
_WfRsvpResvFwdShared_Object = MibTableColumn
wfRsvpResvFwdShared = _WfRsvpResvFwdShared_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 22),
    _WfRsvpResvFwdShared_Type()
)
wfRsvpResvFwdShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdShared.setStatus("mandatory")


class _WfRsvpResvFwdExplicit_Type(Integer32):
    """Custom type wfRsvpResvFwdExplicit based on Integer32"""
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


_WfRsvpResvFwdExplicit_Type.__name__ = "Integer32"
_WfRsvpResvFwdExplicit_Object = MibTableColumn
wfRsvpResvFwdExplicit = _WfRsvpResvFwdExplicit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 23),
    _WfRsvpResvFwdExplicit_Type()
)
wfRsvpResvFwdExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdExplicit.setStatus("mandatory")


class _WfRsvpResvFwdRSVPHop_Type(Integer32):
    """Custom type wfRsvpResvFwdRSVPHop based on Integer32"""
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


_WfRsvpResvFwdRSVPHop_Type.__name__ = "Integer32"
_WfRsvpResvFwdRSVPHop_Object = MibTableColumn
wfRsvpResvFwdRSVPHop = _WfRsvpResvFwdRSVPHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 24),
    _WfRsvpResvFwdRSVPHop_Type()
)
wfRsvpResvFwdRSVPHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdRSVPHop.setStatus("mandatory")
_WfRsvpResvFwdLastChange_Type = Integer32
_WfRsvpResvFwdLastChange_Object = MibTableColumn
wfRsvpResvFwdLastChange = _WfRsvpResvFwdLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 25),
    _WfRsvpResvFwdLastChange_Type()
)
wfRsvpResvFwdLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdLastChange.setStatus("mandatory")


class _WfRsvpResvFwdPolicy_Type(OctetString):
    """Custom type wfRsvpResvFwdPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfRsvpResvFwdPolicy_Type.__name__ = "OctetString"
_WfRsvpResvFwdPolicy_Object = MibTableColumn
wfRsvpResvFwdPolicy = _WfRsvpResvFwdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 26),
    _WfRsvpResvFwdPolicy_Type()
)
wfRsvpResvFwdPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdPolicy.setStatus("mandatory")


class _WfRsvpResvFwdStatus_Type(Integer32):
    """Custom type wfRsvpResvFwdStatus based on Integer32"""
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


_WfRsvpResvFwdStatus_Type.__name__ = "Integer32"
_WfRsvpResvFwdStatus_Object = MibTableColumn
wfRsvpResvFwdStatus = _WfRsvpResvFwdStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 5, 1, 27),
    _WfRsvpResvFwdStatus_Type()
)
wfRsvpResvFwdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpResvFwdStatus.setStatus("mandatory")
_WfRsvpIfTable_Object = MibTable
wfRsvpIfTable = _WfRsvpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wfRsvpIfTable.setStatus("mandatory")
_WfRsvpIfEntry_Object = MibTableRow
wfRsvpIfEntry = _WfRsvpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1)
)
wfRsvpIfEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfRsvpIfCct"),
)
if mibBuilder.loadTexts:
    wfRsvpIfEntry.setStatus("mandatory")


class _WfRsvpIfDelete_Type(Integer32):
    """Custom type wfRsvpIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRsvpIfDelete_Type.__name__ = "Integer32"
_WfRsvpIfDelete_Object = MibTableColumn
wfRsvpIfDelete = _WfRsvpIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 1),
    _WfRsvpIfDelete_Type()
)
wfRsvpIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfDelete.setStatus("mandatory")


class _WfRsvpIfEnable_Type(Integer32):
    """Custom type wfRsvpIfEnable based on Integer32"""
    defaultValue = 1

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


_WfRsvpIfEnable_Type.__name__ = "Integer32"
_WfRsvpIfEnable_Object = MibTableColumn
wfRsvpIfEnable = _WfRsvpIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 2),
    _WfRsvpIfEnable_Type()
)
wfRsvpIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfEnable.setStatus("mandatory")


class _WfRsvpIfState_Type(Integer32):
    """Custom type wfRsvpIfState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfRsvpIfState_Type.__name__ = "Integer32"
_WfRsvpIfState_Object = MibTableColumn
wfRsvpIfState = _WfRsvpIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 3),
    _WfRsvpIfState_Type()
)
wfRsvpIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpIfState.setStatus("mandatory")
_WfRsvpIfCct_Type = Integer32
_WfRsvpIfCct_Object = MibTableColumn
wfRsvpIfCct = _WfRsvpIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 4),
    _WfRsvpIfCct_Type()
)
wfRsvpIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpIfCct.setStatus("mandatory")


class _WfRsvpIfUdpNbrs_Type(Gauge32):
    """Custom type wfRsvpIfUdpNbrs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpIfUdpNbrs_Type.__name__ = "Gauge32"
_WfRsvpIfUdpNbrs_Object = MibTableColumn
wfRsvpIfUdpNbrs = _WfRsvpIfUdpNbrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 5),
    _WfRsvpIfUdpNbrs_Type()
)
wfRsvpIfUdpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpIfUdpNbrs.setStatus("mandatory")


class _WfRsvpIfIpNbrs_Type(Gauge32):
    """Custom type wfRsvpIfIpNbrs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpIfIpNbrs_Type.__name__ = "Gauge32"
_WfRsvpIfIpNbrs_Object = MibTableColumn
wfRsvpIfIpNbrs = _WfRsvpIfIpNbrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 6),
    _WfRsvpIfIpNbrs_Type()
)
wfRsvpIfIpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpIfIpNbrs.setStatus("mandatory")


class _WfRsvpIfNbrs_Type(Gauge32):
    """Custom type wfRsvpIfNbrs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfRsvpIfNbrs_Type.__name__ = "Gauge32"
_WfRsvpIfNbrs_Object = MibTableColumn
wfRsvpIfNbrs = _WfRsvpIfNbrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 7),
    _WfRsvpIfNbrs_Type()
)
wfRsvpIfNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpIfNbrs.setStatus("mandatory")


class _WfRsvpIfRefreshBlockadeMultiple_Type(Integer32):
    """Custom type wfRsvpIfRefreshBlockadeMultiple based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_WfRsvpIfRefreshBlockadeMultiple_Type.__name__ = "Integer32"
_WfRsvpIfRefreshBlockadeMultiple_Object = MibTableColumn
wfRsvpIfRefreshBlockadeMultiple = _WfRsvpIfRefreshBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 8),
    _WfRsvpIfRefreshBlockadeMultiple_Type()
)
wfRsvpIfRefreshBlockadeMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfRefreshBlockadeMultiple.setStatus("mandatory")


class _WfRsvpIfRefreshMultiple_Type(Integer32):
    """Custom type wfRsvpIfRefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_WfRsvpIfRefreshMultiple_Type.__name__ = "Integer32"
_WfRsvpIfRefreshMultiple_Object = MibTableColumn
wfRsvpIfRefreshMultiple = _WfRsvpIfRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 9),
    _WfRsvpIfRefreshMultiple_Type()
)
wfRsvpIfRefreshMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfRefreshMultiple.setStatus("mandatory")


class _WfRsvpIfTTL_Type(Integer32):
    """Custom type wfRsvpIfTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfRsvpIfTTL_Type.__name__ = "Integer32"
_WfRsvpIfTTL_Object = MibTableColumn
wfRsvpIfTTL = _WfRsvpIfTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 10),
    _WfRsvpIfTTL_Type()
)
wfRsvpIfTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfTTL.setStatus("mandatory")


class _WfRsvpIfRefreshInterval_Type(Integer32):
    """Custom type wfRsvpIfRefreshInterval based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2147483647),
    )


_WfRsvpIfRefreshInterval_Type.__name__ = "Integer32"
_WfRsvpIfRefreshInterval_Object = MibTableColumn
wfRsvpIfRefreshInterval = _WfRsvpIfRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 11),
    _WfRsvpIfRefreshInterval_Type()
)
wfRsvpIfRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfRefreshInterval.setStatus("mandatory")


class _WfRsvpIfRouteDelay_Type(Integer32):
    """Custom type wfRsvpIfRouteDelay based on Integer32"""
    defaultValue = 200


_WfRsvpIfRouteDelay_Object = MibTableColumn
wfRsvpIfRouteDelay = _WfRsvpIfRouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 12),
    _WfRsvpIfRouteDelay_Type()
)
wfRsvpIfRouteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfRouteDelay.setStatus("mandatory")


class _WfRsvpIfUdpRequired_Type(Integer32):
    """Custom type wfRsvpIfUdpRequired based on Integer32"""
    defaultValue = 2

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


_WfRsvpIfUdpRequired_Type.__name__ = "Integer32"
_WfRsvpIfUdpRequired_Object = MibTableColumn
wfRsvpIfUdpRequired = _WfRsvpIfUdpRequired_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 6, 1, 13),
    _WfRsvpIfUdpRequired_Type()
)
wfRsvpIfUdpRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRsvpIfUdpRequired.setStatus("mandatory")
_WfRsvpNbrTable_Object = MibTable
wfRsvpNbrTable = _WfRsvpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wfRsvpNbrTable.setStatus("mandatory")
_WfRsvpNbrEntry_Object = MibTableRow
wfRsvpNbrEntry = _WfRsvpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 7, 1)
)
wfRsvpNbrEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfRsvpNbrCct"),
    (0, "Wellfleet-RSVP-MIB", "wfRsvpNbrAddress"),
)
if mibBuilder.loadTexts:
    wfRsvpNbrEntry.setStatus("mandatory")
_WfRsvpNbrAddress_Type = IpAddress
_WfRsvpNbrAddress_Object = MibTableColumn
wfRsvpNbrAddress = _WfRsvpNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 7, 1, 1),
    _WfRsvpNbrAddress_Type()
)
wfRsvpNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpNbrAddress.setStatus("mandatory")


class _WfRsvpNbrProtocol_Type(Integer32):
    """Custom type wfRsvpNbrProtocol based on Integer32"""
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


_WfRsvpNbrProtocol_Type.__name__ = "Integer32"
_WfRsvpNbrProtocol_Object = MibTableColumn
wfRsvpNbrProtocol = _WfRsvpNbrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 7, 1, 2),
    _WfRsvpNbrProtocol_Type()
)
wfRsvpNbrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpNbrProtocol.setStatus("mandatory")
_WfRsvpNbrCct_Type = Integer32
_WfRsvpNbrCct_Object = MibTableColumn
wfRsvpNbrCct = _WfRsvpNbrCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 7, 1, 3),
    _WfRsvpNbrCct_Type()
)
wfRsvpNbrCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpNbrCct.setStatus("mandatory")


class _WfRsvpNbrStatus_Type(Integer32):
    """Custom type wfRsvpNbrStatus based on Integer32"""
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


_WfRsvpNbrStatus_Type.__name__ = "Integer32"
_WfRsvpNbrStatus_Object = MibTableColumn
wfRsvpNbrStatus = _WfRsvpNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 7, 1, 4),
    _WfRsvpNbrStatus_Type()
)
wfRsvpNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRsvpNbrStatus.setStatus("mandatory")
_WfSRsvp_ObjectIdentity = ObjectIdentity
wfSRsvp = _WfSRsvp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8)
)


class _WfSRsvpDelete_Type(Integer32):
    """Custom type wfSRsvpDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSRsvpDelete_Type.__name__ = "Integer32"
_WfSRsvpDelete_Object = MibScalar
wfSRsvpDelete = _WfSRsvpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 1),
    _WfSRsvpDelete_Type()
)
wfSRsvpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpDelete.setStatus("mandatory")


class _WfSRsvpDisable_Type(Integer32):
    """Custom type wfSRsvpDisable based on Integer32"""
    defaultValue = 1

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


_WfSRsvpDisable_Type.__name__ = "Integer32"
_WfSRsvpDisable_Object = MibScalar
wfSRsvpDisable = _WfSRsvpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 2),
    _WfSRsvpDisable_Type()
)
wfSRsvpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpDisable.setStatus("mandatory")


class _WfSRsvpState_Type(Integer32):
    """Custom type wfSRsvpState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfSRsvpState_Type.__name__ = "Integer32"
_WfSRsvpState_Object = MibScalar
wfSRsvpState = _WfSRsvpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 3),
    _WfSRsvpState_Type()
)
wfSRsvpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpState.setStatus("mandatory")


class _WfSRsvpSoloistSlot_Type(Integer32):
    """Custom type wfSRsvpSoloistSlot based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfSRsvpSoloistSlot_Type.__name__ = "Integer32"
_WfSRsvpSoloistSlot_Object = MibScalar
wfSRsvpSoloistSlot = _WfSRsvpSoloistSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 4),
    _WfSRsvpSoloistSlot_Type()
)
wfSRsvpSoloistSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSoloistSlot.setStatus("mandatory")


class _WfSRsvpInfoLogFilter_Type(Integer32):
    """Custom type wfSRsvpInfoLogFilter based on Integer32"""
    defaultValue = 0


_WfSRsvpInfoLogFilter_Object = MibScalar
wfSRsvpInfoLogFilter = _WfSRsvpInfoLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 5),
    _WfSRsvpInfoLogFilter_Type()
)
wfSRsvpInfoLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpInfoLogFilter.setStatus("mandatory")


class _WfSRsvpDebugLogFilter_Type(Integer32):
    """Custom type wfSRsvpDebugLogFilter based on Integer32"""
    defaultValue = 0


_WfSRsvpDebugLogFilter_Object = MibScalar
wfSRsvpDebugLogFilter = _WfSRsvpDebugLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 6),
    _WfSRsvpDebugLogFilter_Type()
)
wfSRsvpDebugLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpDebugLogFilter.setStatus("mandatory")


class _WfSRsvpTraceLogFilter_Type(Integer32):
    """Custom type wfSRsvpTraceLogFilter based on Integer32"""
    defaultValue = 0


_WfSRsvpTraceLogFilter_Object = MibScalar
wfSRsvpTraceLogFilter = _WfSRsvpTraceLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 7),
    _WfSRsvpTraceLogFilter_Type()
)
wfSRsvpTraceLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpTraceLogFilter.setStatus("mandatory")


class _WfSRsvpRefreshInterval_Type(Integer32):
    """Custom type wfSRsvpRefreshInterval based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2147483647),
    )


_WfSRsvpRefreshInterval_Type.__name__ = "Integer32"
_WfSRsvpRefreshInterval_Object = MibScalar
wfSRsvpRefreshInterval = _WfSRsvpRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 8),
    _WfSRsvpRefreshInterval_Type()
)
wfSRsvpRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpRefreshInterval.setStatus("mandatory")


class _WfSRsvpTotalSenders_Type(Gauge32):
    """Custom type wfSRsvpTotalSenders based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfSRsvpTotalSenders_Type.__name__ = "Gauge32"
_WfSRsvpTotalSenders_Object = MibScalar
wfSRsvpTotalSenders = _WfSRsvpTotalSenders_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 9),
    _WfSRsvpTotalSenders_Type()
)
wfSRsvpTotalSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpTotalSenders.setStatus("mandatory")


class _WfSRsvpTotalReservations_Type(Gauge32):
    """Custom type wfSRsvpTotalReservations based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfSRsvpTotalReservations_Type.__name__ = "Gauge32"
_WfSRsvpTotalReservations_Object = MibScalar
wfSRsvpTotalReservations = _WfSRsvpTotalReservations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 8, 10),
    _WfSRsvpTotalReservations_Type()
)
wfSRsvpTotalReservations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpTotalReservations.setStatus("mandatory")
_WfSRsvpSenderTable_Object = MibTable
wfSRsvpSenderTable = _WfSRsvpSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wfSRsvpSenderTable.setStatus("mandatory")
_WfSRsvpSenderEntry_Object = MibTableRow
wfSRsvpSenderEntry = _WfSRsvpSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1)
)
wfSRsvpSenderEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfSRsvpSenderNumber"),
)
if mibBuilder.loadTexts:
    wfSRsvpSenderEntry.setStatus("mandatory")


class _WfSRsvpSenderCreate_Type(Integer32):
    """Custom type wfSRsvpSenderCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSRsvpSenderCreate_Type.__name__ = "Integer32"
_WfSRsvpSenderCreate_Object = MibTableColumn
wfSRsvpSenderCreate = _WfSRsvpSenderCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 1),
    _WfSRsvpSenderCreate_Type()
)
wfSRsvpSenderCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderCreate.setStatus("mandatory")


class _WfSRsvpSenderEnable_Type(Integer32):
    """Custom type wfSRsvpSenderEnable based on Integer32"""
    defaultValue = 1

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


_WfSRsvpSenderEnable_Type.__name__ = "Integer32"
_WfSRsvpSenderEnable_Object = MibTableColumn
wfSRsvpSenderEnable = _WfSRsvpSenderEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 2),
    _WfSRsvpSenderEnable_Type()
)
wfSRsvpSenderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderEnable.setStatus("mandatory")


class _WfSRsvpSenderStatus_Type(Integer32):
    """Custom type wfSRsvpSenderStatus based on Integer32"""
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
        *(("invalid", 2),
          ("notpres", 3),
          ("valid", 1))
    )


_WfSRsvpSenderStatus_Type.__name__ = "Integer32"
_WfSRsvpSenderStatus_Object = MibTableColumn
wfSRsvpSenderStatus = _WfSRsvpSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 3),
    _WfSRsvpSenderStatus_Type()
)
wfSRsvpSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpSenderStatus.setStatus("mandatory")
_WfSRsvpSenderNumber_Type = Integer32
_WfSRsvpSenderNumber_Object = MibTableColumn
wfSRsvpSenderNumber = _WfSRsvpSenderNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 4),
    _WfSRsvpSenderNumber_Type()
)
wfSRsvpSenderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpSenderNumber.setStatus("mandatory")


class _WfSRsvpSenderDestReplicate_Type(Integer32):
    """Custom type wfSRsvpSenderDestReplicate based on Integer32"""
    defaultValue = 0


_WfSRsvpSenderDestReplicate_Object = MibTableColumn
wfSRsvpSenderDestReplicate = _WfSRsvpSenderDestReplicate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 5),
    _WfSRsvpSenderDestReplicate_Type()
)
wfSRsvpSenderDestReplicate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderDestReplicate.setStatus("mandatory")


class _WfSRsvpSenderReplicate_Type(Integer32):
    """Custom type wfSRsvpSenderReplicate based on Integer32"""
    defaultValue = 0


_WfSRsvpSenderReplicate_Object = MibTableColumn
wfSRsvpSenderReplicate = _WfSRsvpSenderReplicate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 6),
    _WfSRsvpSenderReplicate_Type()
)
wfSRsvpSenderReplicate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderReplicate.setStatus("mandatory")


class _WfSRsvpSenderIntegrity_Type(OctetString):
    """Custom type wfSRsvpSenderIntegrity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfSRsvpSenderIntegrity_Type.__name__ = "OctetString"
_WfSRsvpSenderIntegrity_Object = MibTableColumn
wfSRsvpSenderIntegrity = _WfSRsvpSenderIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 7),
    _WfSRsvpSenderIntegrity_Type()
)
wfSRsvpSenderIntegrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderIntegrity.setStatus("mandatory")
_WfSRsvpSenderDestAddr_Type = IpAddress
_WfSRsvpSenderDestAddr_Object = MibTableColumn
wfSRsvpSenderDestAddr = _WfSRsvpSenderDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 8),
    _WfSRsvpSenderDestAddr_Type()
)
wfSRsvpSenderDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderDestAddr.setStatus("mandatory")
_WfSRsvpSenderAddr_Type = IpAddress
_WfSRsvpSenderAddr_Object = MibTableColumn
wfSRsvpSenderAddr = _WfSRsvpSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 9),
    _WfSRsvpSenderAddr_Type()
)
wfSRsvpSenderAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAddr.setStatus("mandatory")


class _WfSRsvpSenderDestAddrLength_Type(Integer32):
    """Custom type wfSRsvpSenderDestAddrLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfSRsvpSenderDestAddrLength_Type.__name__ = "Integer32"
_WfSRsvpSenderDestAddrLength_Object = MibTableColumn
wfSRsvpSenderDestAddrLength = _WfSRsvpSenderDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 10),
    _WfSRsvpSenderDestAddrLength_Type()
)
wfSRsvpSenderDestAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderDestAddrLength.setStatus("mandatory")


class _WfSRsvpSenderAddrLength_Type(Integer32):
    """Custom type wfSRsvpSenderAddrLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfSRsvpSenderAddrLength_Type.__name__ = "Integer32"
_WfSRsvpSenderAddrLength_Object = MibTableColumn
wfSRsvpSenderAddrLength = _WfSRsvpSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 11),
    _WfSRsvpSenderAddrLength_Type()
)
wfSRsvpSenderAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAddrLength.setStatus("mandatory")


class _WfSRsvpSenderProtocol_Type(Integer32):
    """Custom type wfSRsvpSenderProtocol based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSRsvpSenderProtocol_Type.__name__ = "Integer32"
_WfSRsvpSenderProtocol_Object = MibTableColumn
wfSRsvpSenderProtocol = _WfSRsvpSenderProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 12),
    _WfSRsvpSenderProtocol_Type()
)
wfSRsvpSenderProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderProtocol.setStatus("mandatory")


class _WfSRsvpSenderDestPort_Type(Integer32):
    """Custom type wfSRsvpSenderDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfSRsvpSenderDestPort_Type.__name__ = "Integer32"
_WfSRsvpSenderDestPort_Object = MibTableColumn
wfSRsvpSenderDestPort = _WfSRsvpSenderDestPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 13),
    _WfSRsvpSenderDestPort_Type()
)
wfSRsvpSenderDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderDestPort.setStatus("mandatory")


class _WfSRsvpSenderPort_Type(Integer32):
    """Custom type wfSRsvpSenderPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfSRsvpSenderPort_Type.__name__ = "Integer32"
_WfSRsvpSenderPort_Object = MibTableColumn
wfSRsvpSenderPort = _WfSRsvpSenderPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 14),
    _WfSRsvpSenderPort_Type()
)
wfSRsvpSenderPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderPort.setStatus("mandatory")
_WfSRsvpSenderHopAddr_Type = IpAddress
_WfSRsvpSenderHopAddr_Object = MibTableColumn
wfSRsvpSenderHopAddr = _WfSRsvpSenderHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 15),
    _WfSRsvpSenderHopAddr_Type()
)
wfSRsvpSenderHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderHopAddr.setStatus("mandatory")
_WfSRsvpSenderHopLih_Type = Integer32
_WfSRsvpSenderHopLih_Object = MibTableColumn
wfSRsvpSenderHopLih = _WfSRsvpSenderHopLih_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 16),
    _WfSRsvpSenderHopLih_Type()
)
wfSRsvpSenderHopLih.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderHopLih.setStatus("mandatory")
_WfSRsvpSenderInterface_Type = Integer32
_WfSRsvpSenderInterface_Object = MibTableColumn
wfSRsvpSenderInterface = _WfSRsvpSenderInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 17),
    _WfSRsvpSenderInterface_Type()
)
wfSRsvpSenderInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderInterface.setStatus("mandatory")


class _WfSRsvpSenderTimeValue_Type(Integer32):
    """Custom type wfSRsvpSenderTimeValue based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderTimeValue_Type.__name__ = "Integer32"
_WfSRsvpSenderTimeValue_Object = MibTableColumn
wfSRsvpSenderTimeValue = _WfSRsvpSenderTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 18),
    _WfSRsvpSenderTimeValue_Type()
)
wfSRsvpSenderTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderTimeValue.setStatus("mandatory")


class _WfSRsvpSenderTSpecRate_Type(Integer32):
    """Custom type wfSRsvpSenderTSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderTSpecRate_Type.__name__ = "Integer32"
_WfSRsvpSenderTSpecRate_Object = MibTableColumn
wfSRsvpSenderTSpecRate = _WfSRsvpSenderTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 19),
    _WfSRsvpSenderTSpecRate_Type()
)
wfSRsvpSenderTSpecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderTSpecRate.setStatus("mandatory")


class _WfSRsvpSenderTSpecPeakRate_Type(Integer32):
    """Custom type wfSRsvpSenderTSpecPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderTSpecPeakRate_Type.__name__ = "Integer32"
_WfSRsvpSenderTSpecPeakRate_Object = MibTableColumn
wfSRsvpSenderTSpecPeakRate = _WfSRsvpSenderTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 20),
    _WfSRsvpSenderTSpecPeakRate_Type()
)
wfSRsvpSenderTSpecPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderTSpecPeakRate.setStatus("mandatory")


class _WfSRsvpSenderTSpecBurst_Type(Integer32):
    """Custom type wfSRsvpSenderTSpecBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderTSpecBurst_Type.__name__ = "Integer32"
_WfSRsvpSenderTSpecBurst_Object = MibTableColumn
wfSRsvpSenderTSpecBurst = _WfSRsvpSenderTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 21),
    _WfSRsvpSenderTSpecBurst_Type()
)
wfSRsvpSenderTSpecBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderTSpecBurst.setStatus("mandatory")


class _WfSRsvpSenderTSpecMinTU_Type(Integer32):
    """Custom type wfSRsvpSenderTSpecMinTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderTSpecMinTU_Type.__name__ = "Integer32"
_WfSRsvpSenderTSpecMinTU_Object = MibTableColumn
wfSRsvpSenderTSpecMinTU = _WfSRsvpSenderTSpecMinTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 22),
    _WfSRsvpSenderTSpecMinTU_Type()
)
wfSRsvpSenderTSpecMinTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderTSpecMinTU.setStatus("mandatory")


class _WfSRsvpSenderTSpecMaxTU_Type(Integer32):
    """Custom type wfSRsvpSenderTSpecMaxTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderTSpecMaxTU_Type.__name__ = "Integer32"
_WfSRsvpSenderTSpecMaxTU_Object = MibTableColumn
wfSRsvpSenderTSpecMaxTU = _WfSRsvpSenderTSpecMaxTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 23),
    _WfSRsvpSenderTSpecMaxTU_Type()
)
wfSRsvpSenderTSpecMaxTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderTSpecMaxTU.setStatus("mandatory")


class _WfSRsvpSenderPolicy_Type(OctetString):
    """Custom type wfSRsvpSenderPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfSRsvpSenderPolicy_Type.__name__ = "OctetString"
_WfSRsvpSenderPolicy_Object = MibTableColumn
wfSRsvpSenderPolicy = _WfSRsvpSenderPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 24),
    _WfSRsvpSenderPolicy_Type()
)
wfSRsvpSenderPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderPolicy.setStatus("mandatory")


class _WfSRsvpSenderAdspec_Type(Integer32):
    """Custom type wfSRsvpSenderAdspec based on Integer32"""
    defaultValue = 1

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


_WfSRsvpSenderAdspec_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspec_Object = MibTableColumn
wfSRsvpSenderAdspec = _WfSRsvpSenderAdspec_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 25),
    _WfSRsvpSenderAdspec_Type()
)
wfSRsvpSenderAdspec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspec.setStatus("mandatory")


class _WfSRsvpSenderAdspecBreak_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecBreak based on Integer32"""
    defaultValue = 2

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


_WfSRsvpSenderAdspecBreak_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecBreak_Object = MibTableColumn
wfSRsvpSenderAdspecBreak = _WfSRsvpSenderAdspecBreak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 26),
    _WfSRsvpSenderAdspecBreak_Type()
)
wfSRsvpSenderAdspecBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecBreak.setStatus("mandatory")


class _WfSRsvpSenderAdspecHopCount_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecHopCount_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecHopCount_Object = MibTableColumn
wfSRsvpSenderAdspecHopCount = _WfSRsvpSenderAdspecHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 27),
    _WfSRsvpSenderAdspecHopCount_Type()
)
wfSRsvpSenderAdspecHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecHopCount.setStatus("mandatory")


class _WfSRsvpSenderAdspecPathBw_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecPathBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecPathBw_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecPathBw_Object = MibTableColumn
wfSRsvpSenderAdspecPathBw = _WfSRsvpSenderAdspecPathBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 28),
    _WfSRsvpSenderAdspecPathBw_Type()
)
wfSRsvpSenderAdspecPathBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecPathBw.setStatus("mandatory")


class _WfSRsvpSenderAdspecMinLatency_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecMinLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecMinLatency_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecMinLatency_Object = MibTableColumn
wfSRsvpSenderAdspecMinLatency = _WfSRsvpSenderAdspecMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 29),
    _WfSRsvpSenderAdspecMinLatency_Type()
)
wfSRsvpSenderAdspecMinLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecMinLatency.setStatus("mandatory")


class _WfSRsvpSenderAdspecMtu_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecMtu_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecMtu_Object = MibTableColumn
wfSRsvpSenderAdspecMtu = _WfSRsvpSenderAdspecMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 30),
    _WfSRsvpSenderAdspecMtu_Type()
)
wfSRsvpSenderAdspecMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecMtu.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSSvc_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSSvc based on Integer32"""
    defaultValue = 2

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


_WfSRsvpSenderAdspecGSSvc_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSSvc_Object = MibTableColumn
wfSRsvpSenderAdspecGSSvc = _WfSRsvpSenderAdspecGSSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 31),
    _WfSRsvpSenderAdspecGSSvc_Type()
)
wfSRsvpSenderAdspecGSSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSSvc.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSBreak_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSBreak based on Integer32"""
    defaultValue = 1

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


_WfSRsvpSenderAdspecGSBreak_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSBreak_Object = MibTableColumn
wfSRsvpSenderAdspecGSBreak = _WfSRsvpSenderAdspecGSBreak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 32),
    _WfSRsvpSenderAdspecGSBreak_Type()
)
wfSRsvpSenderAdspecGSBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSBreak.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSCtot_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSCtot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSCtot_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSCtot_Object = MibTableColumn
wfSRsvpSenderAdspecGSCtot = _WfSRsvpSenderAdspecGSCtot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 33),
    _WfSRsvpSenderAdspecGSCtot_Type()
)
wfSRsvpSenderAdspecGSCtot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSCtot.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSDtot_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSDtot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSDtot_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSDtot_Object = MibTableColumn
wfSRsvpSenderAdspecGSDtot = _WfSRsvpSenderAdspecGSDtot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 34),
    _WfSRsvpSenderAdspecGSDtot_Type()
)
wfSRsvpSenderAdspecGSDtot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSDtot.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSCsum_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSCsum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSCsum_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSCsum_Object = MibTableColumn
wfSRsvpSenderAdspecGSCsum = _WfSRsvpSenderAdspecGSCsum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 35),
    _WfSRsvpSenderAdspecGSCsum_Type()
)
wfSRsvpSenderAdspecGSCsum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSCsum.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSDsum_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSDsum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSDsum_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSDsum_Object = MibTableColumn
wfSRsvpSenderAdspecGSDsum = _WfSRsvpSenderAdspecGSDsum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 36),
    _WfSRsvpSenderAdspecGSDsum_Type()
)
wfSRsvpSenderAdspecGSDsum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSDsum.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSOverrides_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSOverrides based on Integer32"""
    defaultValue = 2

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


_WfSRsvpSenderAdspecGSOverrides_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSOverrides_Object = MibTableColumn
wfSRsvpSenderAdspecGSOverrides = _WfSRsvpSenderAdspecGSOverrides_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 37),
    _WfSRsvpSenderAdspecGSOverrides_Type()
)
wfSRsvpSenderAdspecGSOverrides.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSOverrides.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSHopCount_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSHopCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSHopCount_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSHopCount_Object = MibTableColumn
wfSRsvpSenderAdspecGSHopCount = _WfSRsvpSenderAdspecGSHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 38),
    _WfSRsvpSenderAdspecGSHopCount_Type()
)
wfSRsvpSenderAdspecGSHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSHopCount.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSPathBw_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSPathBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSPathBw_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSPathBw_Object = MibTableColumn
wfSRsvpSenderAdspecGSPathBw = _WfSRsvpSenderAdspecGSPathBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 39),
    _WfSRsvpSenderAdspecGSPathBw_Type()
)
wfSRsvpSenderAdspecGSPathBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSPathBw.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSMinLatency_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSMinLatency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSMinLatency_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSMinLatency_Object = MibTableColumn
wfSRsvpSenderAdspecGSMinLatency = _WfSRsvpSenderAdspecGSMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 40),
    _WfSRsvpSenderAdspecGSMinLatency_Type()
)
wfSRsvpSenderAdspecGSMinLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSMinLatency.setStatus("mandatory")


class _WfSRsvpSenderAdspecGSMtu_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecGSMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecGSMtu_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecGSMtu_Object = MibTableColumn
wfSRsvpSenderAdspecGSMtu = _WfSRsvpSenderAdspecGSMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 41),
    _WfSRsvpSenderAdspecGSMtu_Type()
)
wfSRsvpSenderAdspecGSMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecGSMtu.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLSvc_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLSvc based on Integer32"""
    defaultValue = 1

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


_WfSRsvpSenderAdspecCLSvc_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLSvc_Object = MibTableColumn
wfSRsvpSenderAdspecCLSvc = _WfSRsvpSenderAdspecCLSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 42),
    _WfSRsvpSenderAdspecCLSvc_Type()
)
wfSRsvpSenderAdspecCLSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLSvc.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLBreak_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLBreak based on Integer32"""
    defaultValue = 2

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


_WfSRsvpSenderAdspecCLBreak_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLBreak_Object = MibTableColumn
wfSRsvpSenderAdspecCLBreak = _WfSRsvpSenderAdspecCLBreak_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 43),
    _WfSRsvpSenderAdspecCLBreak_Type()
)
wfSRsvpSenderAdspecCLBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLBreak.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLOverrides_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLOverrides based on Integer32"""
    defaultValue = 2

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


_WfSRsvpSenderAdspecCLOverrides_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLOverrides_Object = MibTableColumn
wfSRsvpSenderAdspecCLOverrides = _WfSRsvpSenderAdspecCLOverrides_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 44),
    _WfSRsvpSenderAdspecCLOverrides_Type()
)
wfSRsvpSenderAdspecCLOverrides.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLOverrides.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLHopCount_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLHopCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecCLHopCount_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLHopCount_Object = MibTableColumn
wfSRsvpSenderAdspecCLHopCount = _WfSRsvpSenderAdspecCLHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 45),
    _WfSRsvpSenderAdspecCLHopCount_Type()
)
wfSRsvpSenderAdspecCLHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLHopCount.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLPathBw_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLPathBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecCLPathBw_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLPathBw_Object = MibTableColumn
wfSRsvpSenderAdspecCLPathBw = _WfSRsvpSenderAdspecCLPathBw_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 46),
    _WfSRsvpSenderAdspecCLPathBw_Type()
)
wfSRsvpSenderAdspecCLPathBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLPathBw.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLMinLatency_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLMinLatency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecCLMinLatency_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLMinLatency_Object = MibTableColumn
wfSRsvpSenderAdspecCLMinLatency = _WfSRsvpSenderAdspecCLMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 47),
    _WfSRsvpSenderAdspecCLMinLatency_Type()
)
wfSRsvpSenderAdspecCLMinLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLMinLatency.setStatus("mandatory")


class _WfSRsvpSenderAdspecCLMtu_Type(Integer32):
    """Custom type wfSRsvpSenderAdspecCLMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpSenderAdspecCLMtu_Type.__name__ = "Integer32"
_WfSRsvpSenderAdspecCLMtu_Object = MibTableColumn
wfSRsvpSenderAdspecCLMtu = _WfSRsvpSenderAdspecCLMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 9, 1, 48),
    _WfSRsvpSenderAdspecCLMtu_Type()
)
wfSRsvpSenderAdspecCLMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpSenderAdspecCLMtu.setStatus("mandatory")
_WfSRsvpResvTable_Object = MibTable
wfSRsvpResvTable = _WfSRsvpResvTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wfSRsvpResvTable.setStatus("mandatory")
_WfSRsvpResvEntry_Object = MibTableRow
wfSRsvpResvEntry = _WfSRsvpResvEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1)
)
wfSRsvpResvEntry.setIndexNames(
    (0, "Wellfleet-RSVP-MIB", "wfSRsvpResvNumber"),
)
if mibBuilder.loadTexts:
    wfSRsvpResvEntry.setStatus("mandatory")


class _WfSRsvpResvCreate_Type(Integer32):
    """Custom type wfSRsvpResvCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSRsvpResvCreate_Type.__name__ = "Integer32"
_WfSRsvpResvCreate_Object = MibTableColumn
wfSRsvpResvCreate = _WfSRsvpResvCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 1),
    _WfSRsvpResvCreate_Type()
)
wfSRsvpResvCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvCreate.setStatus("mandatory")


class _WfSRsvpResvEnable_Type(Integer32):
    """Custom type wfSRsvpResvEnable based on Integer32"""
    defaultValue = 1

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


_WfSRsvpResvEnable_Type.__name__ = "Integer32"
_WfSRsvpResvEnable_Object = MibTableColumn
wfSRsvpResvEnable = _WfSRsvpResvEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 2),
    _WfSRsvpResvEnable_Type()
)
wfSRsvpResvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvEnable.setStatus("mandatory")


class _WfSRsvpResvStatus_Type(Integer32):
    """Custom type wfSRsvpResvStatus based on Integer32"""
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
        *(("invalid", 2),
          ("notpres", 3),
          ("valid", 1))
    )


_WfSRsvpResvStatus_Type.__name__ = "Integer32"
_WfSRsvpResvStatus_Object = MibTableColumn
wfSRsvpResvStatus = _WfSRsvpResvStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 3),
    _WfSRsvpResvStatus_Type()
)
wfSRsvpResvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpResvStatus.setStatus("mandatory")
_WfSRsvpResvNumber_Type = Integer32
_WfSRsvpResvNumber_Object = MibTableColumn
wfSRsvpResvNumber = _WfSRsvpResvNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 4),
    _WfSRsvpResvNumber_Type()
)
wfSRsvpResvNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSRsvpResvNumber.setStatus("mandatory")


class _WfSRsvpResvDestReplicate_Type(Integer32):
    """Custom type wfSRsvpResvDestReplicate based on Integer32"""
    defaultValue = 0


_WfSRsvpResvDestReplicate_Object = MibTableColumn
wfSRsvpResvDestReplicate = _WfSRsvpResvDestReplicate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 5),
    _WfSRsvpResvDestReplicate_Type()
)
wfSRsvpResvDestReplicate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvDestReplicate.setStatus("mandatory")


class _WfSRsvpResvReplicate_Type(Integer32):
    """Custom type wfSRsvpResvReplicate based on Integer32"""
    defaultValue = 0


_WfSRsvpResvReplicate_Object = MibTableColumn
wfSRsvpResvReplicate = _WfSRsvpResvReplicate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 6),
    _WfSRsvpResvReplicate_Type()
)
wfSRsvpResvReplicate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvReplicate.setStatus("mandatory")


class _WfSRsvpResvIntegrity_Type(OctetString):
    """Custom type wfSRsvpResvIntegrity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfSRsvpResvIntegrity_Type.__name__ = "OctetString"
_WfSRsvpResvIntegrity_Object = MibTableColumn
wfSRsvpResvIntegrity = _WfSRsvpResvIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 7),
    _WfSRsvpResvIntegrity_Type()
)
wfSRsvpResvIntegrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvIntegrity.setStatus("mandatory")
_WfSRsvpResvDestAddr_Type = IpAddress
_WfSRsvpResvDestAddr_Object = MibTableColumn
wfSRsvpResvDestAddr = _WfSRsvpResvDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 8),
    _WfSRsvpResvDestAddr_Type()
)
wfSRsvpResvDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvDestAddr.setStatus("mandatory")
_WfSRsvpResvSenderAddr_Type = IpAddress
_WfSRsvpResvSenderAddr_Object = MibTableColumn
wfSRsvpResvSenderAddr = _WfSRsvpResvSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 9),
    _WfSRsvpResvSenderAddr_Type()
)
wfSRsvpResvSenderAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvSenderAddr.setStatus("mandatory")


class _WfSRsvpResvDestAddrLength_Type(Integer32):
    """Custom type wfSRsvpResvDestAddrLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfSRsvpResvDestAddrLength_Type.__name__ = "Integer32"
_WfSRsvpResvDestAddrLength_Object = MibTableColumn
wfSRsvpResvDestAddrLength = _WfSRsvpResvDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 10),
    _WfSRsvpResvDestAddrLength_Type()
)
wfSRsvpResvDestAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvDestAddrLength.setStatus("mandatory")


class _WfSRsvpResvSenderAddrLength_Type(Integer32):
    """Custom type wfSRsvpResvSenderAddrLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfSRsvpResvSenderAddrLength_Type.__name__ = "Integer32"
_WfSRsvpResvSenderAddrLength_Object = MibTableColumn
wfSRsvpResvSenderAddrLength = _WfSRsvpResvSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 11),
    _WfSRsvpResvSenderAddrLength_Type()
)
wfSRsvpResvSenderAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvSenderAddrLength.setStatus("mandatory")


class _WfSRsvpResvProtocol_Type(Integer32):
    """Custom type wfSRsvpResvProtocol based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSRsvpResvProtocol_Type.__name__ = "Integer32"
_WfSRsvpResvProtocol_Object = MibTableColumn
wfSRsvpResvProtocol = _WfSRsvpResvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 12),
    _WfSRsvpResvProtocol_Type()
)
wfSRsvpResvProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvProtocol.setStatus("mandatory")


class _WfSRsvpResvDestPort_Type(Integer32):
    """Custom type wfSRsvpResvDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfSRsvpResvDestPort_Type.__name__ = "Integer32"
_WfSRsvpResvDestPort_Object = MibTableColumn
wfSRsvpResvDestPort = _WfSRsvpResvDestPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 13),
    _WfSRsvpResvDestPort_Type()
)
wfSRsvpResvDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvDestPort.setStatus("mandatory")


class _WfSRsvpResvPort_Type(Integer32):
    """Custom type wfSRsvpResvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfSRsvpResvPort_Type.__name__ = "Integer32"
_WfSRsvpResvPort_Object = MibTableColumn
wfSRsvpResvPort = _WfSRsvpResvPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 14),
    _WfSRsvpResvPort_Type()
)
wfSRsvpResvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvPort.setStatus("mandatory")


class _WfSRsvpResvFilterSpecNum_Type(Integer32):
    """Custom type wfSRsvpResvFilterSpecNum based on Integer32"""
    defaultValue = 0


_WfSRsvpResvFilterSpecNum_Object = MibTableColumn
wfSRsvpResvFilterSpecNum = _WfSRsvpResvFilterSpecNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 15),
    _WfSRsvpResvFilterSpecNum_Type()
)
wfSRsvpResvFilterSpecNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvFilterSpecNum.setStatus("mandatory")
_WfSRsvpResvHopAddr_Type = IpAddress
_WfSRsvpResvHopAddr_Object = MibTableColumn
wfSRsvpResvHopAddr = _WfSRsvpResvHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 16),
    _WfSRsvpResvHopAddr_Type()
)
wfSRsvpResvHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvHopAddr.setStatus("mandatory")
_WfSRsvpResvHopLih_Type = Integer32
_WfSRsvpResvHopLih_Object = MibTableColumn
wfSRsvpResvHopLih = _WfSRsvpResvHopLih_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 17),
    _WfSRsvpResvHopLih_Type()
)
wfSRsvpResvHopLih.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvHopLih.setStatus("mandatory")
_WfSRsvpResvInterface_Type = Integer32
_WfSRsvpResvInterface_Object = MibTableColumn
wfSRsvpResvInterface = _WfSRsvpResvInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 18),
    _WfSRsvpResvInterface_Type()
)
wfSRsvpResvInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvInterface.setStatus("mandatory")


class _WfSRsvpResvTimeValue_Type(Integer32):
    """Custom type wfSRsvpResvTimeValue based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvTimeValue_Type.__name__ = "Integer32"
_WfSRsvpResvTimeValue_Object = MibTableColumn
wfSRsvpResvTimeValue = _WfSRsvpResvTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 19),
    _WfSRsvpResvTimeValue_Type()
)
wfSRsvpResvTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTimeValue.setStatus("mandatory")


class _WfSRsvpResvService_Type(Integer32):
    """Custom type wfSRsvpResvService based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("controlledDelay", 1),
          ("controlledLoad", 5),
          ("guaranteedDelay", 2),
          ("predictive", 3))
    )


_WfSRsvpResvService_Type.__name__ = "Integer32"
_WfSRsvpResvService_Object = MibTableColumn
wfSRsvpResvService = _WfSRsvpResvService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 20),
    _WfSRsvpResvService_Type()
)
wfSRsvpResvService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvService.setStatus("mandatory")


class _WfSRsvpResvTSpecRate_Type(Integer32):
    """Custom type wfSRsvpResvTSpecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvTSpecRate_Type.__name__ = "Integer32"
_WfSRsvpResvTSpecRate_Object = MibTableColumn
wfSRsvpResvTSpecRate = _WfSRsvpResvTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 21),
    _WfSRsvpResvTSpecRate_Type()
)
wfSRsvpResvTSpecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTSpecRate.setStatus("mandatory")


class _WfSRsvpResvTSpecPeakRate_Type(Integer32):
    """Custom type wfSRsvpResvTSpecPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvTSpecPeakRate_Type.__name__ = "Integer32"
_WfSRsvpResvTSpecPeakRate_Object = MibTableColumn
wfSRsvpResvTSpecPeakRate = _WfSRsvpResvTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 22),
    _WfSRsvpResvTSpecPeakRate_Type()
)
wfSRsvpResvTSpecPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTSpecPeakRate.setStatus("mandatory")


class _WfSRsvpResvTSpecBurst_Type(Integer32):
    """Custom type wfSRsvpResvTSpecBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvTSpecBurst_Type.__name__ = "Integer32"
_WfSRsvpResvTSpecBurst_Object = MibTableColumn
wfSRsvpResvTSpecBurst = _WfSRsvpResvTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 23),
    _WfSRsvpResvTSpecBurst_Type()
)
wfSRsvpResvTSpecBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTSpecBurst.setStatus("mandatory")


class _WfSRsvpResvTSpecMinTU_Type(Integer32):
    """Custom type wfSRsvpResvTSpecMinTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvTSpecMinTU_Type.__name__ = "Integer32"
_WfSRsvpResvTSpecMinTU_Object = MibTableColumn
wfSRsvpResvTSpecMinTU = _WfSRsvpResvTSpecMinTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 24),
    _WfSRsvpResvTSpecMinTU_Type()
)
wfSRsvpResvTSpecMinTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTSpecMinTU.setStatus("mandatory")


class _WfSRsvpResvTSpecMaxTU_Type(Integer32):
    """Custom type wfSRsvpResvTSpecMaxTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvTSpecMaxTU_Type.__name__ = "Integer32"
_WfSRsvpResvTSpecMaxTU_Object = MibTableColumn
wfSRsvpResvTSpecMaxTU = _WfSRsvpResvTSpecMaxTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 25),
    _WfSRsvpResvTSpecMaxTU_Type()
)
wfSRsvpResvTSpecMaxTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTSpecMaxTU.setStatus("mandatory")


class _WfSRsvpResvTSpecLevel_Type(Integer32):
    """Custom type wfSRsvpResvTSpecLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WfSRsvpResvTSpecLevel_Type.__name__ = "Integer32"
_WfSRsvpResvTSpecLevel_Object = MibTableColumn
wfSRsvpResvTSpecLevel = _WfSRsvpResvTSpecLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 26),
    _WfSRsvpResvTSpecLevel_Type()
)
wfSRsvpResvTSpecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvTSpecLevel.setStatus("mandatory")


class _WfSRsvpResvRSpecRate_Type(Integer32):
    """Custom type wfSRsvpResvRSpecRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfSRsvpResvRSpecRate_Type.__name__ = "Integer32"
_WfSRsvpResvRSpecRate_Object = MibTableColumn
wfSRsvpResvRSpecRate = _WfSRsvpResvRSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 27),
    _WfSRsvpResvRSpecRate_Type()
)
wfSRsvpResvRSpecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvRSpecRate.setStatus("mandatory")


class _WfSRsvpResvRSpecSlack_Type(Integer32):
    """Custom type wfSRsvpResvRSpecSlack based on Integer32"""
    defaultValue = 0


_WfSRsvpResvRSpecSlack_Object = MibTableColumn
wfSRsvpResvRSpecSlack = _WfSRsvpResvRSpecSlack_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 28),
    _WfSRsvpResvRSpecSlack_Type()
)
wfSRsvpResvRSpecSlack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvRSpecSlack.setStatus("mandatory")


class _WfSRsvpResvScopeNum_Type(Integer32):
    """Custom type wfSRsvpResvScopeNum based on Integer32"""
    defaultValue = 0


_WfSRsvpResvScopeNum_Object = MibTableColumn
wfSRsvpResvScopeNum = _WfSRsvpResvScopeNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 29),
    _WfSRsvpResvScopeNum_Type()
)
wfSRsvpResvScopeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvScopeNum.setStatus("mandatory")


class _WfSRsvpResvScope_Type(OctetString):
    """Custom type wfSRsvpResvScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfSRsvpResvScope_Type.__name__ = "OctetString"
_WfSRsvpResvScope_Object = MibTableColumn
wfSRsvpResvScope = _WfSRsvpResvScope_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 30),
    _WfSRsvpResvScope_Type()
)
wfSRsvpResvScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvScope.setStatus("mandatory")


class _WfSRsvpResvShared_Type(Integer32):
    """Custom type wfSRsvpResvShared based on Integer32"""
    defaultValue = 2

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


_WfSRsvpResvShared_Type.__name__ = "Integer32"
_WfSRsvpResvShared_Object = MibTableColumn
wfSRsvpResvShared = _WfSRsvpResvShared_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 31),
    _WfSRsvpResvShared_Type()
)
wfSRsvpResvShared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvShared.setStatus("mandatory")


class _WfSRsvpResvExplicit_Type(Integer32):
    """Custom type wfSRsvpResvExplicit based on Integer32"""
    defaultValue = 1

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


_WfSRsvpResvExplicit_Type.__name__ = "Integer32"
_WfSRsvpResvExplicit_Object = MibTableColumn
wfSRsvpResvExplicit = _WfSRsvpResvExplicit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 32),
    _WfSRsvpResvExplicit_Type()
)
wfSRsvpResvExplicit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvExplicit.setStatus("mandatory")


class _WfSRsvpResvPolicy_Type(OctetString):
    """Custom type wfSRsvpResvPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_WfSRsvpResvPolicy_Type.__name__ = "OctetString"
_WfSRsvpResvPolicy_Object = MibTableColumn
wfSRsvpResvPolicy = _WfSRsvpResvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 1, 10, 1, 33),
    _WfSRsvpResvPolicy_Type()
)
wfSRsvpResvPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSRsvpResvPolicy.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RSVP-MIB",
    **{"wfRsvpGroup": wfRsvpGroup,
       "wfRsvp": wfRsvp,
       "wfRsvpDelete": wfRsvpDelete,
       "wfRsvpDisable": wfRsvpDisable,
       "wfRsvpState": wfRsvpState,
       "wfRsvpSoloistSlots": wfRsvpSoloistSlots,
       "wfRsvpInfoLogFilter": wfRsvpInfoLogFilter,
       "wfRsvpDebugLogFilter": wfRsvpDebugLogFilter,
       "wfRsvpTraceLogFilter": wfRsvpTraceLogFilter,
       "wfRsvpTotalSenders": wfRsvpTotalSenders,
       "wfRsvpTotalReservations": wfRsvpTotalReservations,
       "wfRsvpTotalReserved": wfRsvpTotalReserved,
       "wfRsvpCurrentSoloistSlot": wfRsvpCurrentSoloistSlot,
       "wfRsvpSessionTable": wfRsvpSessionTable,
       "wfRsvpSessionEntry": wfRsvpSessionEntry,
       "wfRsvpSessionDestAddr": wfRsvpSessionDestAddr,
       "wfRsvpSessionDestAddrLength": wfRsvpSessionDestAddrLength,
       "wfRsvpSessionProtocol": wfRsvpSessionProtocol,
       "wfRsvpSessionPort": wfRsvpSessionPort,
       "wfRsvpSessionSenders": wfRsvpSessionSenders,
       "wfRsvpSessionReceivers": wfRsvpSessionReceivers,
       "wfRsvpSessionRequests": wfRsvpSessionRequests,
       "wfRsvpSenderTable": wfRsvpSenderTable,
       "wfRsvpSenderEntry": wfRsvpSenderEntry,
       "wfRsvpSenderDestAddr": wfRsvpSenderDestAddr,
       "wfRsvpSenderAddr": wfRsvpSenderAddr,
       "wfRsvpSenderDestAddrLength": wfRsvpSenderDestAddrLength,
       "wfRsvpSenderAddrLength": wfRsvpSenderAddrLength,
       "wfRsvpSenderProtocol": wfRsvpSenderProtocol,
       "wfRsvpSenderDestPort": wfRsvpSenderDestPort,
       "wfRsvpSenderPort": wfRsvpSenderPort,
       "wfRsvpSenderHopAddr": wfRsvpSenderHopAddr,
       "wfRsvpSenderHopLih": wfRsvpSenderHopLih,
       "wfRsvpSenderInterface": wfRsvpSenderInterface,
       "wfRsvpSenderTSpecRate": wfRsvpSenderTSpecRate,
       "wfRsvpSenderTSpecPeakRate": wfRsvpSenderTSpecPeakRate,
       "wfRsvpSenderTSpecBurst": wfRsvpSenderTSpecBurst,
       "wfRsvpSenderTSpecMinTU": wfRsvpSenderTSpecMinTU,
       "wfRsvpSenderTSpecMaxTU": wfRsvpSenderTSpecMaxTU,
       "wfRsvpSenderInterval": wfRsvpSenderInterval,
       "wfRsvpSenderRSVPHop": wfRsvpSenderRSVPHop,
       "wfRsvpSenderLastChange": wfRsvpSenderLastChange,
       "wfRsvpSenderPSBTimeout": wfRsvpSenderPSBTimeout,
       "wfRsvpSenderPolicy": wfRsvpSenderPolicy,
       "wfRsvpSenderAdspecBreak": wfRsvpSenderAdspecBreak,
       "wfRsvpSenderAdspecHopCount": wfRsvpSenderAdspecHopCount,
       "wfRsvpSenderAdspecPathBw": wfRsvpSenderAdspecPathBw,
       "wfRsvpSenderAdspecMinLatency": wfRsvpSenderAdspecMinLatency,
       "wfRsvpSenderAdspecMtu": wfRsvpSenderAdspecMtu,
       "wfRsvpSenderAdspecGSSvc": wfRsvpSenderAdspecGSSvc,
       "wfRsvpSenderAdspecGSBreak": wfRsvpSenderAdspecGSBreak,
       "wfRsvpSenderAdspecGSCtot": wfRsvpSenderAdspecGSCtot,
       "wfRsvpSenderAdspecGSDtot": wfRsvpSenderAdspecGSDtot,
       "wfRsvpSenderAdspecGSCsum": wfRsvpSenderAdspecGSCsum,
       "wfRsvpSenderAdspecGSDsum": wfRsvpSenderAdspecGSDsum,
       "wfRsvpSenderAdspecGSHopCount": wfRsvpSenderAdspecGSHopCount,
       "wfRsvpSenderAdspecGSPathBw": wfRsvpSenderAdspecGSPathBw,
       "wfRsvpSenderAdspecGSMinLatency": wfRsvpSenderAdspecGSMinLatency,
       "wfRsvpSenderAdspecGSMtu": wfRsvpSenderAdspecGSMtu,
       "wfRsvpSenderAdspecCLSvc": wfRsvpSenderAdspecCLSvc,
       "wfRsvpSenderAdspecCLBreak": wfRsvpSenderAdspecCLBreak,
       "wfRsvpSenderAdspecCLHopCount": wfRsvpSenderAdspecCLHopCount,
       "wfRsvpSenderAdspecCLPathBw": wfRsvpSenderAdspecCLPathBw,
       "wfRsvpSenderAdspecCLMinLatency": wfRsvpSenderAdspecCLMinLatency,
       "wfRsvpSenderAdspecCLMtu": wfRsvpSenderAdspecCLMtu,
       "wfRsvpSenderStatus": wfRsvpSenderStatus,
       "wfRsvpResvTable": wfRsvpResvTable,
       "wfRsvpResvEntry": wfRsvpResvEntry,
       "wfRsvpResvDestAddr": wfRsvpResvDestAddr,
       "wfRsvpResvSenderAddr": wfRsvpResvSenderAddr,
       "wfRsvpResvDestAddrLength": wfRsvpResvDestAddrLength,
       "wfRsvpResvSenderAddrLength": wfRsvpResvSenderAddrLength,
       "wfRsvpResvProtocol": wfRsvpResvProtocol,
       "wfRsvpResvDestPort": wfRsvpResvDestPort,
       "wfRsvpResvPort": wfRsvpResvPort,
       "wfRsvpResvHopAddr": wfRsvpResvHopAddr,
       "wfRsvpResvHopLih": wfRsvpResvHopLih,
       "wfRsvpResvInterface": wfRsvpResvInterface,
       "wfRsvpResvService": wfRsvpResvService,
       "wfRsvpResvTSpecRate": wfRsvpResvTSpecRate,
       "wfRsvpResvTSpecPeakRate": wfRsvpResvTSpecPeakRate,
       "wfRsvpResvTSpecBurst": wfRsvpResvTSpecBurst,
       "wfRsvpResvTSpecMinTU": wfRsvpResvTSpecMinTU,
       "wfRsvpResvTSpecMaxTU": wfRsvpResvTSpecMaxTU,
       "wfRsvpResvTSpecLevel": wfRsvpResvTSpecLevel,
       "wfRsvpResvRSpecRate": wfRsvpResvRSpecRate,
       "wfRsvpResvRSpecSlack": wfRsvpResvRSpecSlack,
       "wfRsvpResvInterval": wfRsvpResvInterval,
       "wfRsvpResvScope": wfRsvpResvScope,
       "wfRsvpResvShared": wfRsvpResvShared,
       "wfRsvpResvExplicit": wfRsvpResvExplicit,
       "wfRsvpResvRSVPHop": wfRsvpResvRSVPHop,
       "wfRsvpResvLastChange": wfRsvpResvLastChange,
       "wfRsvpResvRSBTimeout": wfRsvpResvRSBTimeout,
       "wfRsvpResvPolicy": wfRsvpResvPolicy,
       "wfRsvpResvStatus": wfRsvpResvStatus,
       "wfRsvpResvFwdTable": wfRsvpResvFwdTable,
       "wfRsvpResvFwdEntry": wfRsvpResvFwdEntry,
       "wfRsvpResvFwdDestAddr": wfRsvpResvFwdDestAddr,
       "wfRsvpResvFwdSenderAddr": wfRsvpResvFwdSenderAddr,
       "wfRsvpResvFwdDestAddrLength": wfRsvpResvFwdDestAddrLength,
       "wfRsvpResvFwdSenderAddrLength": wfRsvpResvFwdSenderAddrLength,
       "wfRsvpResvFwdProtocol": wfRsvpResvFwdProtocol,
       "wfRsvpResvFwdDestPort": wfRsvpResvFwdDestPort,
       "wfRsvpResvFwdPort": wfRsvpResvFwdPort,
       "wfRsvpResvFwdHopAddr": wfRsvpResvFwdHopAddr,
       "wfRsvpResvFwdHopLih": wfRsvpResvFwdHopLih,
       "wfRsvpResvFwdInterface": wfRsvpResvFwdInterface,
       "wfRsvpResvFwdService": wfRsvpResvFwdService,
       "wfRsvpResvFwdTSpecRate": wfRsvpResvFwdTSpecRate,
       "wfRsvpResvFwdTSpecPeakRate": wfRsvpResvFwdTSpecPeakRate,
       "wfRsvpResvFwdTSpecBurst": wfRsvpResvFwdTSpecBurst,
       "wfRsvpResvFwdTSpecMinTU": wfRsvpResvFwdTSpecMinTU,
       "wfRsvpResvFwdTSpecMaxTU": wfRsvpResvFwdTSpecMaxTU,
       "wfRsvpResvFwdTSpecLevel": wfRsvpResvFwdTSpecLevel,
       "wfRsvpResvFwdRSpecRate": wfRsvpResvFwdRSpecRate,
       "wfRsvpResvFwdRSpecSlack": wfRsvpResvFwdRSpecSlack,
       "wfRsvpResvFwdInterval": wfRsvpResvFwdInterval,
       "wfRsvpResvFwdScope": wfRsvpResvFwdScope,
       "wfRsvpResvFwdShared": wfRsvpResvFwdShared,
       "wfRsvpResvFwdExplicit": wfRsvpResvFwdExplicit,
       "wfRsvpResvFwdRSVPHop": wfRsvpResvFwdRSVPHop,
       "wfRsvpResvFwdLastChange": wfRsvpResvFwdLastChange,
       "wfRsvpResvFwdPolicy": wfRsvpResvFwdPolicy,
       "wfRsvpResvFwdStatus": wfRsvpResvFwdStatus,
       "wfRsvpIfTable": wfRsvpIfTable,
       "wfRsvpIfEntry": wfRsvpIfEntry,
       "wfRsvpIfDelete": wfRsvpIfDelete,
       "wfRsvpIfEnable": wfRsvpIfEnable,
       "wfRsvpIfState": wfRsvpIfState,
       "wfRsvpIfCct": wfRsvpIfCct,
       "wfRsvpIfUdpNbrs": wfRsvpIfUdpNbrs,
       "wfRsvpIfIpNbrs": wfRsvpIfIpNbrs,
       "wfRsvpIfNbrs": wfRsvpIfNbrs,
       "wfRsvpIfRefreshBlockadeMultiple": wfRsvpIfRefreshBlockadeMultiple,
       "wfRsvpIfRefreshMultiple": wfRsvpIfRefreshMultiple,
       "wfRsvpIfTTL": wfRsvpIfTTL,
       "wfRsvpIfRefreshInterval": wfRsvpIfRefreshInterval,
       "wfRsvpIfRouteDelay": wfRsvpIfRouteDelay,
       "wfRsvpIfUdpRequired": wfRsvpIfUdpRequired,
       "wfRsvpNbrTable": wfRsvpNbrTable,
       "wfRsvpNbrEntry": wfRsvpNbrEntry,
       "wfRsvpNbrAddress": wfRsvpNbrAddress,
       "wfRsvpNbrProtocol": wfRsvpNbrProtocol,
       "wfRsvpNbrCct": wfRsvpNbrCct,
       "wfRsvpNbrStatus": wfRsvpNbrStatus,
       "wfSRsvp": wfSRsvp,
       "wfSRsvpDelete": wfSRsvpDelete,
       "wfSRsvpDisable": wfSRsvpDisable,
       "wfSRsvpState": wfSRsvpState,
       "wfSRsvpSoloistSlot": wfSRsvpSoloistSlot,
       "wfSRsvpInfoLogFilter": wfSRsvpInfoLogFilter,
       "wfSRsvpDebugLogFilter": wfSRsvpDebugLogFilter,
       "wfSRsvpTraceLogFilter": wfSRsvpTraceLogFilter,
       "wfSRsvpRefreshInterval": wfSRsvpRefreshInterval,
       "wfSRsvpTotalSenders": wfSRsvpTotalSenders,
       "wfSRsvpTotalReservations": wfSRsvpTotalReservations,
       "wfSRsvpSenderTable": wfSRsvpSenderTable,
       "wfSRsvpSenderEntry": wfSRsvpSenderEntry,
       "wfSRsvpSenderCreate": wfSRsvpSenderCreate,
       "wfSRsvpSenderEnable": wfSRsvpSenderEnable,
       "wfSRsvpSenderStatus": wfSRsvpSenderStatus,
       "wfSRsvpSenderNumber": wfSRsvpSenderNumber,
       "wfSRsvpSenderDestReplicate": wfSRsvpSenderDestReplicate,
       "wfSRsvpSenderReplicate": wfSRsvpSenderReplicate,
       "wfSRsvpSenderIntegrity": wfSRsvpSenderIntegrity,
       "wfSRsvpSenderDestAddr": wfSRsvpSenderDestAddr,
       "wfSRsvpSenderAddr": wfSRsvpSenderAddr,
       "wfSRsvpSenderDestAddrLength": wfSRsvpSenderDestAddrLength,
       "wfSRsvpSenderAddrLength": wfSRsvpSenderAddrLength,
       "wfSRsvpSenderProtocol": wfSRsvpSenderProtocol,
       "wfSRsvpSenderDestPort": wfSRsvpSenderDestPort,
       "wfSRsvpSenderPort": wfSRsvpSenderPort,
       "wfSRsvpSenderHopAddr": wfSRsvpSenderHopAddr,
       "wfSRsvpSenderHopLih": wfSRsvpSenderHopLih,
       "wfSRsvpSenderInterface": wfSRsvpSenderInterface,
       "wfSRsvpSenderTimeValue": wfSRsvpSenderTimeValue,
       "wfSRsvpSenderTSpecRate": wfSRsvpSenderTSpecRate,
       "wfSRsvpSenderTSpecPeakRate": wfSRsvpSenderTSpecPeakRate,
       "wfSRsvpSenderTSpecBurst": wfSRsvpSenderTSpecBurst,
       "wfSRsvpSenderTSpecMinTU": wfSRsvpSenderTSpecMinTU,
       "wfSRsvpSenderTSpecMaxTU": wfSRsvpSenderTSpecMaxTU,
       "wfSRsvpSenderPolicy": wfSRsvpSenderPolicy,
       "wfSRsvpSenderAdspec": wfSRsvpSenderAdspec,
       "wfSRsvpSenderAdspecBreak": wfSRsvpSenderAdspecBreak,
       "wfSRsvpSenderAdspecHopCount": wfSRsvpSenderAdspecHopCount,
       "wfSRsvpSenderAdspecPathBw": wfSRsvpSenderAdspecPathBw,
       "wfSRsvpSenderAdspecMinLatency": wfSRsvpSenderAdspecMinLatency,
       "wfSRsvpSenderAdspecMtu": wfSRsvpSenderAdspecMtu,
       "wfSRsvpSenderAdspecGSSvc": wfSRsvpSenderAdspecGSSvc,
       "wfSRsvpSenderAdspecGSBreak": wfSRsvpSenderAdspecGSBreak,
       "wfSRsvpSenderAdspecGSCtot": wfSRsvpSenderAdspecGSCtot,
       "wfSRsvpSenderAdspecGSDtot": wfSRsvpSenderAdspecGSDtot,
       "wfSRsvpSenderAdspecGSCsum": wfSRsvpSenderAdspecGSCsum,
       "wfSRsvpSenderAdspecGSDsum": wfSRsvpSenderAdspecGSDsum,
       "wfSRsvpSenderAdspecGSOverrides": wfSRsvpSenderAdspecGSOverrides,
       "wfSRsvpSenderAdspecGSHopCount": wfSRsvpSenderAdspecGSHopCount,
       "wfSRsvpSenderAdspecGSPathBw": wfSRsvpSenderAdspecGSPathBw,
       "wfSRsvpSenderAdspecGSMinLatency": wfSRsvpSenderAdspecGSMinLatency,
       "wfSRsvpSenderAdspecGSMtu": wfSRsvpSenderAdspecGSMtu,
       "wfSRsvpSenderAdspecCLSvc": wfSRsvpSenderAdspecCLSvc,
       "wfSRsvpSenderAdspecCLBreak": wfSRsvpSenderAdspecCLBreak,
       "wfSRsvpSenderAdspecCLOverrides": wfSRsvpSenderAdspecCLOverrides,
       "wfSRsvpSenderAdspecCLHopCount": wfSRsvpSenderAdspecCLHopCount,
       "wfSRsvpSenderAdspecCLPathBw": wfSRsvpSenderAdspecCLPathBw,
       "wfSRsvpSenderAdspecCLMinLatency": wfSRsvpSenderAdspecCLMinLatency,
       "wfSRsvpSenderAdspecCLMtu": wfSRsvpSenderAdspecCLMtu,
       "wfSRsvpResvTable": wfSRsvpResvTable,
       "wfSRsvpResvEntry": wfSRsvpResvEntry,
       "wfSRsvpResvCreate": wfSRsvpResvCreate,
       "wfSRsvpResvEnable": wfSRsvpResvEnable,
       "wfSRsvpResvStatus": wfSRsvpResvStatus,
       "wfSRsvpResvNumber": wfSRsvpResvNumber,
       "wfSRsvpResvDestReplicate": wfSRsvpResvDestReplicate,
       "wfSRsvpResvReplicate": wfSRsvpResvReplicate,
       "wfSRsvpResvIntegrity": wfSRsvpResvIntegrity,
       "wfSRsvpResvDestAddr": wfSRsvpResvDestAddr,
       "wfSRsvpResvSenderAddr": wfSRsvpResvSenderAddr,
       "wfSRsvpResvDestAddrLength": wfSRsvpResvDestAddrLength,
       "wfSRsvpResvSenderAddrLength": wfSRsvpResvSenderAddrLength,
       "wfSRsvpResvProtocol": wfSRsvpResvProtocol,
       "wfSRsvpResvDestPort": wfSRsvpResvDestPort,
       "wfSRsvpResvPort": wfSRsvpResvPort,
       "wfSRsvpResvFilterSpecNum": wfSRsvpResvFilterSpecNum,
       "wfSRsvpResvHopAddr": wfSRsvpResvHopAddr,
       "wfSRsvpResvHopLih": wfSRsvpResvHopLih,
       "wfSRsvpResvInterface": wfSRsvpResvInterface,
       "wfSRsvpResvTimeValue": wfSRsvpResvTimeValue,
       "wfSRsvpResvService": wfSRsvpResvService,
       "wfSRsvpResvTSpecRate": wfSRsvpResvTSpecRate,
       "wfSRsvpResvTSpecPeakRate": wfSRsvpResvTSpecPeakRate,
       "wfSRsvpResvTSpecBurst": wfSRsvpResvTSpecBurst,
       "wfSRsvpResvTSpecMinTU": wfSRsvpResvTSpecMinTU,
       "wfSRsvpResvTSpecMaxTU": wfSRsvpResvTSpecMaxTU,
       "wfSRsvpResvTSpecLevel": wfSRsvpResvTSpecLevel,
       "wfSRsvpResvRSpecRate": wfSRsvpResvRSpecRate,
       "wfSRsvpResvRSpecSlack": wfSRsvpResvRSpecSlack,
       "wfSRsvpResvScopeNum": wfSRsvpResvScopeNum,
       "wfSRsvpResvScope": wfSRsvpResvScope,
       "wfSRsvpResvShared": wfSRsvpResvShared,
       "wfSRsvpResvExplicit": wfSRsvpResvExplicit,
       "wfSRsvpResvPolicy": wfSRsvpResvPolicy}
)
