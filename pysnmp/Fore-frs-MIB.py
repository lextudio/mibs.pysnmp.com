# SNMP MIB module (Fore-frs-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-frs-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:23 2024
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

(frameInternetworking,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "frameInternetworking")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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


# MODULE-IDENTITY

foreFrameRelayModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrextDlcmiTable_Object = MibTable
frextDlcmiTable = _FrextDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    frextDlcmiTable.setStatus("current")
_FrextDlcmiEntry_Object = MibTableRow
frextDlcmiEntry = _FrextDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1)
)
frextDlcmiEntry.setIndexNames(
    (0, "Fore-frs-MIB", "frextDlcmiServiceIfIndex"),
)
if mibBuilder.loadTexts:
    frextDlcmiEntry.setStatus("current")
_FrextDlcmiServiceIfIndex_Type = InterfaceIndex
_FrextDlcmiServiceIfIndex_Object = MibTableColumn
frextDlcmiServiceIfIndex = _FrextDlcmiServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 1),
    _FrextDlcmiServiceIfIndex_Type()
)
frextDlcmiServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiServiceIfIndex.setStatus("current")


class _FrextDlcmiProfileLmiIndex_Type(Integer32):
    """Custom type frextDlcmiProfileLmiIndex based on Integer32"""
    defaultValue = 0


_FrextDlcmiProfileLmiIndex_Object = MibTableColumn
frextDlcmiProfileLmiIndex = _FrextDlcmiProfileLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 2),
    _FrextDlcmiProfileLmiIndex_Type()
)
frextDlcmiProfileLmiIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextDlcmiProfileLmiIndex.setStatus("current")


class _FrextDlcmiProfileServiceIndex_Type(Integer32):
    """Custom type frextDlcmiProfileServiceIndex based on Integer32"""
    defaultValue = 0


_FrextDlcmiProfileServiceIndex_Object = MibTableColumn
frextDlcmiProfileServiceIndex = _FrextDlcmiProfileServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 3),
    _FrextDlcmiProfileServiceIndex_Type()
)
frextDlcmiProfileServiceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextDlcmiProfileServiceIndex.setStatus("current")


class _FrextDlcmiStatsMonitor_Type(Integer32):
    """Custom type frextDlcmiStatsMonitor based on Integer32"""
    defaultValue = 2

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


_FrextDlcmiStatsMonitor_Type.__name__ = "Integer32"
_FrextDlcmiStatsMonitor_Object = MibTableColumn
frextDlcmiStatsMonitor = _FrextDlcmiStatsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 4),
    _FrextDlcmiStatsMonitor_Type()
)
frextDlcmiStatsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextDlcmiStatsMonitor.setStatus("current")
_FrextDlcmiStatsEnabledTimeStamp_Type = TimeTicks
_FrextDlcmiStatsEnabledTimeStamp_Object = MibTableColumn
frextDlcmiStatsEnabledTimeStamp = _FrextDlcmiStatsEnabledTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 5),
    _FrextDlcmiStatsEnabledTimeStamp_Type()
)
frextDlcmiStatsEnabledTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiStatsEnabledTimeStamp.setStatus("current")
_FrextDlcmiLmiDlci_Type = Integer32
_FrextDlcmiLmiDlci_Object = MibTableColumn
frextDlcmiLmiDlci = _FrextDlcmiLmiDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 6),
    _FrextDlcmiLmiDlci_Type()
)
frextDlcmiLmiDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiDlci.setStatus("current")


class _FrextDlcmiLmiFlowControl_Type(Integer32):
    """Custom type frextDlcmiLmiFlowControl based on Integer32"""
    defaultValue = 2

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


_FrextDlcmiLmiFlowControl_Type.__name__ = "Integer32"
_FrextDlcmiLmiFlowControl_Object = MibTableColumn
frextDlcmiLmiFlowControl = _FrextDlcmiLmiFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 7),
    _FrextDlcmiLmiFlowControl_Type()
)
frextDlcmiLmiFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextDlcmiLmiFlowControl.setStatus("current")


class _FrextDlcmiRAControl_Type(Integer32):
    """Custom type frextDlcmiRAControl based on Integer32"""
    defaultValue = 2

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


_FrextDlcmiRAControl_Type.__name__ = "Integer32"
_FrextDlcmiRAControl_Object = MibTableColumn
frextDlcmiRAControl = _FrextDlcmiRAControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 8),
    _FrextDlcmiRAControl_Type()
)
frextDlcmiRAControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextDlcmiRAControl.setStatus("current")


class _FrextDlcmiLmiBandwidthControl_Type(Integer32):
    """Custom type frextDlcmiLmiBandwidthControl based on Integer32"""
    defaultValue = 2

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


_FrextDlcmiLmiBandwidthControl_Type.__name__ = "Integer32"
_FrextDlcmiLmiBandwidthControl_Object = MibTableColumn
frextDlcmiLmiBandwidthControl = _FrextDlcmiLmiBandwidthControl_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 9),
    _FrextDlcmiLmiBandwidthControl_Type()
)
frextDlcmiLmiBandwidthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextDlcmiLmiBandwidthControl.setStatus("current")
_FrextDlcmiRxAbortedFrames_Type = Counter32
_FrextDlcmiRxAbortedFrames_Object = MibTableColumn
frextDlcmiRxAbortedFrames = _FrextDlcmiRxAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 10),
    _FrextDlcmiRxAbortedFrames_Type()
)
frextDlcmiRxAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiRxAbortedFrames.setStatus("current")
_FrextDlcmiRcvCrcErrors_Type = Counter32
_FrextDlcmiRcvCrcErrors_Object = MibTableColumn
frextDlcmiRcvCrcErrors = _FrextDlcmiRcvCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 11),
    _FrextDlcmiRcvCrcErrors_Type()
)
frextDlcmiRcvCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiRcvCrcErrors.setStatus("current")
_FrextDlcmiRcvShortFrames_Type = Counter32
_FrextDlcmiRcvShortFrames_Object = MibTableColumn
frextDlcmiRcvShortFrames = _FrextDlcmiRcvShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 12),
    _FrextDlcmiRcvShortFrames_Type()
)
frextDlcmiRcvShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiRcvShortFrames.setStatus("current")
_FrextDlcmiRcvLongFrames_Type = Counter32
_FrextDlcmiRcvLongFrames_Object = MibTableColumn
frextDlcmiRcvLongFrames = _FrextDlcmiRcvLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 13),
    _FrextDlcmiRcvLongFrames_Type()
)
frextDlcmiRcvLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiRcvLongFrames.setStatus("current")
_FrextDlcmiRcvInvalidDLCI_Type = Counter32
_FrextDlcmiRcvInvalidDLCI_Object = MibTableColumn
frextDlcmiRcvInvalidDLCI = _FrextDlcmiRcvInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 14),
    _FrextDlcmiRcvInvalidDLCI_Type()
)
frextDlcmiRcvInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiRcvInvalidDLCI.setStatus("current")
_FrextDlcmiRcvUnknownErrs_Type = Counter32
_FrextDlcmiRcvUnknownErrs_Object = MibTableColumn
frextDlcmiRcvUnknownErrs = _FrextDlcmiRcvUnknownErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 15),
    _FrextDlcmiRcvUnknownErrs_Type()
)
frextDlcmiRcvUnknownErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiRcvUnknownErrs.setStatus("current")
_FrextDlcmiLmiTxStatusResponses_Type = Counter32
_FrextDlcmiLmiTxStatusResponses_Object = MibTableColumn
frextDlcmiLmiTxStatusResponses = _FrextDlcmiLmiTxStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 16),
    _FrextDlcmiLmiTxStatusResponses_Type()
)
frextDlcmiLmiTxStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiTxStatusResponses.setStatus("current")
_FrextDlcmiLmiTxFullStatusResponses_Type = Counter32
_FrextDlcmiLmiTxFullStatusResponses_Object = MibTableColumn
frextDlcmiLmiTxFullStatusResponses = _FrextDlcmiLmiTxFullStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 17),
    _FrextDlcmiLmiTxFullStatusResponses_Type()
)
frextDlcmiLmiTxFullStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiTxFullStatusResponses.setStatus("current")
_FrextDlcmiLmiTxStatusEnquiries_Type = Counter32
_FrextDlcmiLmiTxStatusEnquiries_Object = MibTableColumn
frextDlcmiLmiTxStatusEnquiries = _FrextDlcmiLmiTxStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 18),
    _FrextDlcmiLmiTxStatusEnquiries_Type()
)
frextDlcmiLmiTxStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiTxStatusEnquiries.setStatus("current")
_FrextDlcmiLmiTxFullStatusEnquiries_Type = Counter32
_FrextDlcmiLmiTxFullStatusEnquiries_Object = MibTableColumn
frextDlcmiLmiTxFullStatusEnquiries = _FrextDlcmiLmiTxFullStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 19),
    _FrextDlcmiLmiTxFullStatusEnquiries_Type()
)
frextDlcmiLmiTxFullStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiTxFullStatusEnquiries.setStatus("current")
_FrextDlcmiLmiRxStatusResponses_Type = Counter32
_FrextDlcmiLmiRxStatusResponses_Object = MibTableColumn
frextDlcmiLmiRxStatusResponses = _FrextDlcmiLmiRxStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 20),
    _FrextDlcmiLmiRxStatusResponses_Type()
)
frextDlcmiLmiRxStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiRxStatusResponses.setStatus("current")
_FrextDlcmiLmiRxFullStatusResponses_Type = Counter32
_FrextDlcmiLmiRxFullStatusResponses_Object = MibTableColumn
frextDlcmiLmiRxFullStatusResponses = _FrextDlcmiLmiRxFullStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 21),
    _FrextDlcmiLmiRxFullStatusResponses_Type()
)
frextDlcmiLmiRxFullStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiRxFullStatusResponses.setStatus("current")
_FrextDlcmiLmiRxStatusEnquiries_Type = Counter32
_FrextDlcmiLmiRxStatusEnquiries_Object = MibTableColumn
frextDlcmiLmiRxStatusEnquiries = _FrextDlcmiLmiRxStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 22),
    _FrextDlcmiLmiRxStatusEnquiries_Type()
)
frextDlcmiLmiRxStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiRxStatusEnquiries.setStatus("current")
_FrextDlcmiLmiRxFullStatusEnquiries_Type = Counter32
_FrextDlcmiLmiRxFullStatusEnquiries_Object = MibTableColumn
frextDlcmiLmiRxFullStatusEnquiries = _FrextDlcmiLmiRxFullStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 23),
    _FrextDlcmiLmiRxFullStatusEnquiries_Type()
)
frextDlcmiLmiRxFullStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiRxFullStatusEnquiries.setStatus("current")
_FrextDlcmiLmiUnknownMessagesRcvd_Type = Counter32
_FrextDlcmiLmiUnknownMessagesRcvd_Object = MibTableColumn
frextDlcmiLmiUnknownMessagesRcvd = _FrextDlcmiLmiUnknownMessagesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 24),
    _FrextDlcmiLmiUnknownMessagesRcvd_Type()
)
frextDlcmiLmiUnknownMessagesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiUnknownMessagesRcvd.setStatus("current")
_FrextDlcmiLmiStatusLostSequences_Type = Counter32
_FrextDlcmiLmiStatusLostSequences_Object = MibTableColumn
frextDlcmiLmiStatusLostSequences = _FrextDlcmiLmiStatusLostSequences_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 25),
    _FrextDlcmiLmiStatusLostSequences_Type()
)
frextDlcmiLmiStatusLostSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiStatusLostSequences.setStatus("current")
_FrextDlcmiLmiStatusEnqLostSequences_Type = Counter32
_FrextDlcmiLmiStatusEnqLostSequences_Object = MibTableColumn
frextDlcmiLmiStatusEnqLostSequences = _FrextDlcmiLmiStatusEnqLostSequences_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 26),
    _FrextDlcmiLmiStatusEnqLostSequences_Type()
)
frextDlcmiLmiStatusEnqLostSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiStatusEnqLostSequences.setStatus("current")
_FrextDlcmiLmiMissingStatEnquiries_Type = Counter32
_FrextDlcmiLmiMissingStatEnquiries_Object = MibTableColumn
frextDlcmiLmiMissingStatEnquiries = _FrextDlcmiLmiMissingStatEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 27),
    _FrextDlcmiLmiMissingStatEnquiries_Type()
)
frextDlcmiLmiMissingStatEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiMissingStatEnquiries.setStatus("current")
_FrextDlcmiLmiUnexpectedPVCStatMsg_Type = Counter32
_FrextDlcmiLmiUnexpectedPVCStatMsg_Object = MibTableColumn
frextDlcmiLmiUnexpectedPVCStatMsg = _FrextDlcmiLmiUnexpectedPVCStatMsg_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 28),
    _FrextDlcmiLmiUnexpectedPVCStatMsg_Type()
)
frextDlcmiLmiUnexpectedPVCStatMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiUnexpectedPVCStatMsg.setStatus("current")
_FrextDlcmiLmiUnexpectedDLCI_Type = Counter32
_FrextDlcmiLmiUnexpectedDLCI_Object = MibTableColumn
frextDlcmiLmiUnexpectedDLCI = _FrextDlcmiLmiUnexpectedDLCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 29),
    _FrextDlcmiLmiUnexpectedDLCI_Type()
)
frextDlcmiLmiUnexpectedDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiUnexpectedDLCI.setStatus("current")
_FrextDlcmiLmiStatEnqRatePlus_Type = Counter32
_FrextDlcmiLmiStatEnqRatePlus_Object = MibTableColumn
frextDlcmiLmiStatEnqRatePlus = _FrextDlcmiLmiStatEnqRatePlus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 30),
    _FrextDlcmiLmiStatEnqRatePlus_Type()
)
frextDlcmiLmiStatEnqRatePlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiStatEnqRatePlus.setStatus("current")
_FrextDlcmiLmiInvInfoFrame_Type = Counter32
_FrextDlcmiLmiInvInfoFrame_Object = MibTableColumn
frextDlcmiLmiInvInfoFrame = _FrextDlcmiLmiInvInfoFrame_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 31),
    _FrextDlcmiLmiInvInfoFrame_Type()
)
frextDlcmiLmiInvInfoFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiInvInfoFrame.setStatus("current")
_FrextDlcmiLmiInvFrameHdr_Type = Counter32
_FrextDlcmiLmiInvFrameHdr_Object = MibTableColumn
frextDlcmiLmiInvFrameHdr = _FrextDlcmiLmiInvFrameHdr_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 32),
    _FrextDlcmiLmiInvFrameHdr_Type()
)
frextDlcmiLmiInvFrameHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiInvFrameHdr.setStatus("current")
_FrextDlcmiLmiNoIERepType_Type = Counter32
_FrextDlcmiLmiNoIERepType_Object = MibTableColumn
frextDlcmiLmiNoIERepType = _FrextDlcmiLmiNoIERepType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 33),
    _FrextDlcmiLmiNoIERepType_Type()
)
frextDlcmiLmiNoIERepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiNoIERepType.setStatus("current")
_FrextDlcmiLmiNoIEKeepAlive_Type = Counter32
_FrextDlcmiLmiNoIEKeepAlive_Object = MibTableColumn
frextDlcmiLmiNoIEKeepAlive = _FrextDlcmiLmiNoIEKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 34),
    _FrextDlcmiLmiNoIEKeepAlive_Type()
)
frextDlcmiLmiNoIEKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiNoIEKeepAlive.setStatus("current")
_FrextDlcmiLmiMissingResponses_Type = Counter32
_FrextDlcmiLmiMissingResponses_Object = MibTableColumn
frextDlcmiLmiMissingResponses = _FrextDlcmiLmiMissingResponses_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 35),
    _FrextDlcmiLmiMissingResponses_Type()
)
frextDlcmiLmiMissingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiMissingResponses.setStatus("current")
_FrextDlcmiLmiUnsuppIERcvd_Type = Counter32
_FrextDlcmiLmiUnsuppIERcvd_Object = MibTableColumn
frextDlcmiLmiUnsuppIERcvd = _FrextDlcmiLmiUnsuppIERcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 36),
    _FrextDlcmiLmiUnsuppIERcvd_Type()
)
frextDlcmiLmiUnsuppIERcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiLmiUnsuppIERcvd.setStatus("current")
_FrextDlcmiPvccs_Type = Gauge32
_FrextDlcmiPvccs_Object = MibTableColumn
frextDlcmiPvccs = _FrextDlcmiPvccs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 37),
    _FrextDlcmiPvccs_Type()
)
frextDlcmiPvccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextDlcmiPvccs.setStatus("current")
_FrextCircuitTable_Object = MibTable
frextCircuitTable = _FrextCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    frextCircuitTable.setStatus("current")
_FrextCircuitEntry_Object = MibTableRow
frextCircuitEntry = _FrextCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1)
)
frextCircuitEntry.setIndexNames(
    (0, "Fore-frs-MIB", "frextCircuitServiceIfIndex"),
    (0, "Fore-frs-MIB", "frextCircuitDlci"),
)
if mibBuilder.loadTexts:
    frextCircuitEntry.setStatus("current")
_FrextCircuitServiceIfIndex_Type = InterfaceIndex
_FrextCircuitServiceIfIndex_Object = MibTableColumn
frextCircuitServiceIfIndex = _FrextCircuitServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 1),
    _FrextCircuitServiceIfIndex_Type()
)
frextCircuitServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitServiceIfIndex.setStatus("current")
_FrextCircuitDlci_Type = Integer32
_FrextCircuitDlci_Object = MibTableColumn
frextCircuitDlci = _FrextCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 2),
    _FrextCircuitDlci_Type()
)
frextCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitDlci.setStatus("current")
_FrextCircuitName_Type = DisplayString
_FrextCircuitName_Object = MibTableColumn
frextCircuitName = _FrextCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 3),
    _FrextCircuitName_Type()
)
frextCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextCircuitName.setStatus("current")


class _FrextCircuitProfileFrRateIndex_Type(Integer32):
    """Custom type frextCircuitProfileFrRateIndex based on Integer32"""
    defaultValue = 0


_FrextCircuitProfileFrRateIndex_Object = MibTableColumn
frextCircuitProfileFrRateIndex = _FrextCircuitProfileFrRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 4),
    _FrextCircuitProfileFrRateIndex_Type()
)
frextCircuitProfileFrRateIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextCircuitProfileFrRateIndex.setStatus("current")


class _FrextCircuitREMonitor_Type(Integer32):
    """Custom type frextCircuitREMonitor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("standard", 2))
    )


_FrextCircuitREMonitor_Type.__name__ = "Integer32"
_FrextCircuitREMonitor_Object = MibTableColumn
frextCircuitREMonitor = _FrextCircuitREMonitor_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 5),
    _FrextCircuitREMonitor_Type()
)
frextCircuitREMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frextCircuitREMonitor.setStatus("current")
_FrextCircuitRateFallbacks_Type = Counter32
_FrextCircuitRateFallbacks_Object = MibTableColumn
frextCircuitRateFallbacks = _FrextCircuitRateFallbacks_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 6),
    _FrextCircuitRateFallbacks_Type()
)
frextCircuitRateFallbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRateFallbacks.setStatus("current")
_FrextCircuitRateFallforwards_Type = Counter32
_FrextCircuitRateFallforwards_Object = MibTableColumn
frextCircuitRateFallforwards = _FrextCircuitRateFallforwards_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 7),
    _FrextCircuitRateFallforwards_Type()
)
frextCircuitRateFallforwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRateFallforwards.setStatus("current")
_FrextCircuitEgFramesDroppedQueueFull_Type = Counter32
_FrextCircuitEgFramesDroppedQueueFull_Object = MibTableColumn
frextCircuitEgFramesDroppedQueueFull = _FrextCircuitEgFramesDroppedQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 8),
    _FrextCircuitEgFramesDroppedQueueFull_Type()
)
frextCircuitEgFramesDroppedQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitEgFramesDroppedQueueFull.setStatus("current")
_FrextCircuitNormalSentFrames_Type = Counter32
_FrextCircuitNormalSentFrames_Object = MibTableColumn
frextCircuitNormalSentFrames = _FrextCircuitNormalSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 9),
    _FrextCircuitNormalSentFrames_Type()
)
frextCircuitNormalSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitNormalSentFrames.setStatus("current")
_FrextCircuitNormalSentOctets_Type = Counter32
_FrextCircuitNormalSentOctets_Object = MibTableColumn
frextCircuitNormalSentOctets = _FrextCircuitNormalSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 10),
    _FrextCircuitNormalSentOctets_Type()
)
frextCircuitNormalSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitNormalSentOctets.setStatus("current")
_FrextCircuitExcessSentOctets_Type = Counter32
_FrextCircuitExcessSentOctets_Object = MibTableColumn
frextCircuitExcessSentOctets = _FrextCircuitExcessSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 11),
    _FrextCircuitExcessSentOctets_Type()
)
frextCircuitExcessSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitExcessSentOctets.setStatus("current")
_FrextCircuitHeldBuffers_Type = Counter32
_FrextCircuitHeldBuffers_Object = MibTableColumn
frextCircuitHeldBuffers = _FrextCircuitHeldBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 12),
    _FrextCircuitHeldBuffers_Type()
)
frextCircuitHeldBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitHeldBuffers.setStatus("current")
_FrextCircuitOctetsOnQueue_Type = Counter32
_FrextCircuitOctetsOnQueue_Object = MibTableColumn
frextCircuitOctetsOnQueue = _FrextCircuitOctetsOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 13),
    _FrextCircuitOctetsOnQueue_Type()
)
frextCircuitOctetsOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitOctetsOnQueue.setStatus("current")
_FrextCircuitBuffersOnQueue_Type = Counter32
_FrextCircuitBuffersOnQueue_Object = MibTableColumn
frextCircuitBuffersOnQueue = _FrextCircuitBuffersOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 14),
    _FrextCircuitBuffersOnQueue_Type()
)
frextCircuitBuffersOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitBuffersOnQueue.setStatus("current")
_FrextCircuitRxMonNormalFrames_Type = Counter32
_FrextCircuitRxMonNormalFrames_Object = MibTableColumn
frextCircuitRxMonNormalFrames = _FrextCircuitRxMonNormalFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 15),
    _FrextCircuitRxMonNormalFrames_Type()
)
frextCircuitRxMonNormalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonNormalFrames.setStatus("current")
_FrextCircuitRxMonNormalOctets_Type = Counter32
_FrextCircuitRxMonNormalOctets_Object = MibTableColumn
frextCircuitRxMonNormalOctets = _FrextCircuitRxMonNormalOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 16),
    _FrextCircuitRxMonNormalOctets_Type()
)
frextCircuitRxMonNormalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonNormalOctets.setStatus("current")
_FrextCircuitRxMonExcessOctets_Type = Counter32
_FrextCircuitRxMonExcessOctets_Object = MibTableColumn
frextCircuitRxMonExcessOctets = _FrextCircuitRxMonExcessOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 17),
    _FrextCircuitRxMonExcessOctets_Type()
)
frextCircuitRxMonExcessOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonExcessOctets.setStatus("current")
_FrextCircuitRxMonDroppedOctets_Type = Counter32
_FrextCircuitRxMonDroppedOctets_Object = MibTableColumn
frextCircuitRxMonDroppedOctets = _FrextCircuitRxMonDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 18),
    _FrextCircuitRxMonDroppedOctets_Type()
)
frextCircuitRxMonDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonDroppedOctets.setStatus("current")
_FrextCircuitRxMonDroppedDEFrames_Type = Counter32
_FrextCircuitRxMonDroppedDEFrames_Object = MibTableColumn
frextCircuitRxMonDroppedDEFrames = _FrextCircuitRxMonDroppedDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 19),
    _FrextCircuitRxMonDroppedDEFrames_Type()
)
frextCircuitRxMonDroppedDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonDroppedDEFrames.setStatus("current")
_FrextCircuitRxMonDroppedDEOctets_Type = Counter32
_FrextCircuitRxMonDroppedDEOctets_Object = MibTableColumn
frextCircuitRxMonDroppedDEOctets = _FrextCircuitRxMonDroppedDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 20),
    _FrextCircuitRxMonDroppedDEOctets_Type()
)
frextCircuitRxMonDroppedDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonDroppedDEOctets.setStatus("current")
_FrextCircuitRxMonDEOctets_Type = Counter32
_FrextCircuitRxMonDEOctets_Object = MibTableColumn
frextCircuitRxMonDEOctets = _FrextCircuitRxMonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 21),
    _FrextCircuitRxMonDEOctets_Type()
)
frextCircuitRxMonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonDEOctets.setStatus("current")
_FrextCircuitRxMonSetDEFrames_Type = Counter32
_FrextCircuitRxMonSetDEFrames_Object = MibTableColumn
frextCircuitRxMonSetDEFrames = _FrextCircuitRxMonSetDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 22),
    _FrextCircuitRxMonSetDEFrames_Type()
)
frextCircuitRxMonSetDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonSetDEFrames.setStatus("current")
_FrextCircuitRxMonSetDEOctets_Type = Counter32
_FrextCircuitRxMonSetDEOctets_Object = MibTableColumn
frextCircuitRxMonSetDEOctets = _FrextCircuitRxMonSetDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 23),
    _FrextCircuitRxMonSetDEOctets_Type()
)
frextCircuitRxMonSetDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRxMonSetDEOctets.setStatus("current")
_FrextCircuitRecvdBECNS_Type = Counter32
_FrextCircuitRecvdBECNS_Object = MibTableColumn
frextCircuitRecvdBECNS = _FrextCircuitRecvdBECNS_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 24),
    _FrextCircuitRecvdBECNS_Type()
)
frextCircuitRecvdBECNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRecvdBECNS.setStatus("current")
_FrextCircuitRecvdFECNS_Type = Counter32
_FrextCircuitRecvdFECNS_Object = MibTableColumn
frextCircuitRecvdFECNS = _FrextCircuitRecvdFECNS_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 25),
    _FrextCircuitRecvdFECNS_Type()
)
frextCircuitRecvdFECNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frextCircuitRecvdFECNS.setStatus("current")
_FrsOamF5Table_Object = MibTable
frsOamF5Table = _FrsOamF5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3)
)
if mibBuilder.loadTexts:
    frsOamF5Table.setStatus("current")
_FrsOamF5Entry_Object = MibTableRow
frsOamF5Entry = _FrsOamF5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1)
)
frsOamF5Entry.setIndexNames(
    (0, "Fore-frs-MIB", "frsOamF5AtmIf"),
    (0, "Fore-frs-MIB", "frsOamF5AtmVpi"),
    (0, "Fore-frs-MIB", "frsOamF5AtmVci"),
)
if mibBuilder.loadTexts:
    frsOamF5Entry.setStatus("current")
_FrsOamF5AtmIf_Type = Integer32
_FrsOamF5AtmIf_Object = MibTableColumn
frsOamF5AtmIf = _FrsOamF5AtmIf_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 1),
    _FrsOamF5AtmIf_Type()
)
frsOamF5AtmIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5AtmIf.setStatus("current")
_FrsOamF5AtmVpi_Type = Integer32
_FrsOamF5AtmVpi_Object = MibTableColumn
frsOamF5AtmVpi = _FrsOamF5AtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 2),
    _FrsOamF5AtmVpi_Type()
)
frsOamF5AtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5AtmVpi.setStatus("current")
_FrsOamF5AtmVci_Type = Integer32
_FrsOamF5AtmVci_Object = MibTableColumn
frsOamF5AtmVci = _FrsOamF5AtmVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 3),
    _FrsOamF5AtmVci_Type()
)
frsOamF5AtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5AtmVci.setStatus("current")
_FrsOamF5AISRxCounter_Type = Counter32
_FrsOamF5AISRxCounter_Object = MibTableColumn
frsOamF5AISRxCounter = _FrsOamF5AISRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 4),
    _FrsOamF5AISRxCounter_Type()
)
frsOamF5AISRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5AISRxCounter.setStatus("current")
_FrsOamF5AISTxCounter_Type = Counter32
_FrsOamF5AISTxCounter_Object = MibTableColumn
frsOamF5AISTxCounter = _FrsOamF5AISTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 5),
    _FrsOamF5AISTxCounter_Type()
)
frsOamF5AISTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5AISTxCounter.setStatus("current")
_FrsOamF5RDIRxCounter_Type = Counter32
_FrsOamF5RDIRxCounter_Object = MibTableColumn
frsOamF5RDIRxCounter = _FrsOamF5RDIRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 6),
    _FrsOamF5RDIRxCounter_Type()
)
frsOamF5RDIRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5RDIRxCounter.setStatus("current")
_FrsOamF5RDITxCounter_Type = Counter32
_FrsOamF5RDITxCounter_Object = MibTableColumn
frsOamF5RDITxCounter = _FrsOamF5RDITxCounter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 7),
    _FrsOamF5RDITxCounter_Type()
)
frsOamF5RDITxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsOamF5RDITxCounter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-frs-MIB",
    **{"foreFrameRelayModule": foreFrameRelayModule,
       "frextDlcmiTable": frextDlcmiTable,
       "frextDlcmiEntry": frextDlcmiEntry,
       "frextDlcmiServiceIfIndex": frextDlcmiServiceIfIndex,
       "frextDlcmiProfileLmiIndex": frextDlcmiProfileLmiIndex,
       "frextDlcmiProfileServiceIndex": frextDlcmiProfileServiceIndex,
       "frextDlcmiStatsMonitor": frextDlcmiStatsMonitor,
       "frextDlcmiStatsEnabledTimeStamp": frextDlcmiStatsEnabledTimeStamp,
       "frextDlcmiLmiDlci": frextDlcmiLmiDlci,
       "frextDlcmiLmiFlowControl": frextDlcmiLmiFlowControl,
       "frextDlcmiRAControl": frextDlcmiRAControl,
       "frextDlcmiLmiBandwidthControl": frextDlcmiLmiBandwidthControl,
       "frextDlcmiRxAbortedFrames": frextDlcmiRxAbortedFrames,
       "frextDlcmiRcvCrcErrors": frextDlcmiRcvCrcErrors,
       "frextDlcmiRcvShortFrames": frextDlcmiRcvShortFrames,
       "frextDlcmiRcvLongFrames": frextDlcmiRcvLongFrames,
       "frextDlcmiRcvInvalidDLCI": frextDlcmiRcvInvalidDLCI,
       "frextDlcmiRcvUnknownErrs": frextDlcmiRcvUnknownErrs,
       "frextDlcmiLmiTxStatusResponses": frextDlcmiLmiTxStatusResponses,
       "frextDlcmiLmiTxFullStatusResponses": frextDlcmiLmiTxFullStatusResponses,
       "frextDlcmiLmiTxStatusEnquiries": frextDlcmiLmiTxStatusEnquiries,
       "frextDlcmiLmiTxFullStatusEnquiries": frextDlcmiLmiTxFullStatusEnquiries,
       "frextDlcmiLmiRxStatusResponses": frextDlcmiLmiRxStatusResponses,
       "frextDlcmiLmiRxFullStatusResponses": frextDlcmiLmiRxFullStatusResponses,
       "frextDlcmiLmiRxStatusEnquiries": frextDlcmiLmiRxStatusEnquiries,
       "frextDlcmiLmiRxFullStatusEnquiries": frextDlcmiLmiRxFullStatusEnquiries,
       "frextDlcmiLmiUnknownMessagesRcvd": frextDlcmiLmiUnknownMessagesRcvd,
       "frextDlcmiLmiStatusLostSequences": frextDlcmiLmiStatusLostSequences,
       "frextDlcmiLmiStatusEnqLostSequences": frextDlcmiLmiStatusEnqLostSequences,
       "frextDlcmiLmiMissingStatEnquiries": frextDlcmiLmiMissingStatEnquiries,
       "frextDlcmiLmiUnexpectedPVCStatMsg": frextDlcmiLmiUnexpectedPVCStatMsg,
       "frextDlcmiLmiUnexpectedDLCI": frextDlcmiLmiUnexpectedDLCI,
       "frextDlcmiLmiStatEnqRatePlus": frextDlcmiLmiStatEnqRatePlus,
       "frextDlcmiLmiInvInfoFrame": frextDlcmiLmiInvInfoFrame,
       "frextDlcmiLmiInvFrameHdr": frextDlcmiLmiInvFrameHdr,
       "frextDlcmiLmiNoIERepType": frextDlcmiLmiNoIERepType,
       "frextDlcmiLmiNoIEKeepAlive": frextDlcmiLmiNoIEKeepAlive,
       "frextDlcmiLmiMissingResponses": frextDlcmiLmiMissingResponses,
       "frextDlcmiLmiUnsuppIERcvd": frextDlcmiLmiUnsuppIERcvd,
       "frextDlcmiPvccs": frextDlcmiPvccs,
       "frextCircuitTable": frextCircuitTable,
       "frextCircuitEntry": frextCircuitEntry,
       "frextCircuitServiceIfIndex": frextCircuitServiceIfIndex,
       "frextCircuitDlci": frextCircuitDlci,
       "frextCircuitName": frextCircuitName,
       "frextCircuitProfileFrRateIndex": frextCircuitProfileFrRateIndex,
       "frextCircuitREMonitor": frextCircuitREMonitor,
       "frextCircuitRateFallbacks": frextCircuitRateFallbacks,
       "frextCircuitRateFallforwards": frextCircuitRateFallforwards,
       "frextCircuitEgFramesDroppedQueueFull": frextCircuitEgFramesDroppedQueueFull,
       "frextCircuitNormalSentFrames": frextCircuitNormalSentFrames,
       "frextCircuitNormalSentOctets": frextCircuitNormalSentOctets,
       "frextCircuitExcessSentOctets": frextCircuitExcessSentOctets,
       "frextCircuitHeldBuffers": frextCircuitHeldBuffers,
       "frextCircuitOctetsOnQueue": frextCircuitOctetsOnQueue,
       "frextCircuitBuffersOnQueue": frextCircuitBuffersOnQueue,
       "frextCircuitRxMonNormalFrames": frextCircuitRxMonNormalFrames,
       "frextCircuitRxMonNormalOctets": frextCircuitRxMonNormalOctets,
       "frextCircuitRxMonExcessOctets": frextCircuitRxMonExcessOctets,
       "frextCircuitRxMonDroppedOctets": frextCircuitRxMonDroppedOctets,
       "frextCircuitRxMonDroppedDEFrames": frextCircuitRxMonDroppedDEFrames,
       "frextCircuitRxMonDroppedDEOctets": frextCircuitRxMonDroppedDEOctets,
       "frextCircuitRxMonDEOctets": frextCircuitRxMonDEOctets,
       "frextCircuitRxMonSetDEFrames": frextCircuitRxMonSetDEFrames,
       "frextCircuitRxMonSetDEOctets": frextCircuitRxMonSetDEOctets,
       "frextCircuitRecvdBECNS": frextCircuitRecvdBECNS,
       "frextCircuitRecvdFECNS": frextCircuitRecvdFECNS,
       "frsOamF5Table": frsOamF5Table,
       "frsOamF5Entry": frsOamF5Entry,
       "frsOamF5AtmIf": frsOamF5AtmIf,
       "frsOamF5AtmVpi": frsOamF5AtmVpi,
       "frsOamF5AtmVci": frsOamF5AtmVci,
       "frsOamF5AISRxCounter": frsOamF5AISRxCounter,
       "frsOamF5AISTxCounter": frsOamF5AISTxCounter,
       "frsOamF5RDIRxCounter": frsOamF5RDIRxCounter,
       "frsOamF5RDITxCounter": frsOamF5RDITxCounter}
)
