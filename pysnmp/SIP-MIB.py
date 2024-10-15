# SNMP MIB module (SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:22 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sipMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 9998)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SipServerActions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 2),
          ("redirect", 1))
    )



# MIB Managed Objects in the order of their OIDs

_SipMIBObjects_ObjectIdentity = ObjectIdentity
sipMIBObjects = _SipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1)
)
_SipCommon_ObjectIdentity = ObjectIdentity
sipCommon = _SipCommon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1)
)
_SipCommonCfg_ObjectIdentity = ObjectIdentity
sipCommonCfg = _SipCommonCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1)
)
_SipProtocolVersion_Type = SnmpAdminString
_SipProtocolVersion_Object = MibScalar
sipProtocolVersion = _SipProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 1),
    _SipProtocolVersion_Type()
)
sipProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProtocolVersion.setStatus("current")


class _SipServiceOperStatus_Type(Integer32):
    """Custom type sipServiceOperStatus based on Integer32"""
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
        *(("down", 2),
          ("halted", 5),
          ("restarting", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_SipServiceOperStatus_Type.__name__ = "Integer32"
_SipServiceOperStatus_Object = MibScalar
sipServiceOperStatus = _SipServiceOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 2),
    _SipServiceOperStatus_Type()
)
sipServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServiceOperStatus.setStatus("current")


class _SipServiceAdminStatus_Type(Integer32):
    """Custom type sipServiceAdminStatus based on Integer32"""
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
        *(("reset", 2),
          ("restart", 3),
          ("rts", 5),
          ("shutdown", 1),
          ("stop", 4))
    )


_SipServiceAdminStatus_Type.__name__ = "Integer32"
_SipServiceAdminStatus_Object = MibScalar
sipServiceAdminStatus = _SipServiceAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 3),
    _SipServiceAdminStatus_Type()
)
sipServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipServiceAdminStatus.setStatus("current")
_SipServiceStartTime_Type = TimeTicks
_SipServiceStartTime_Object = MibScalar
sipServiceStartTime = _SipServiceStartTime_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 4),
    _SipServiceStartTime_Type()
)
sipServiceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServiceStartTime.setStatus("current")
_SipServiceLastChange_Type = TimeTicks
_SipServiceLastChange_Object = MibScalar
sipServiceLastChange = _SipServiceLastChange_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 5),
    _SipServiceLastChange_Type()
)
sipServiceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServiceLastChange.setStatus("current")
_SipPortTable_Object = MibTable
sipPortTable = _SipPortTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sipPortTable.setStatus("current")
_SipPortEntry_Object = MibTableRow
sipPortEntry = _SipPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 6, 1)
)
sipPortEntry.setIndexNames(
    (0, "SIP-MIB", "sipPort"),
)
if mibBuilder.loadTexts:
    sipPortEntry.setStatus("current")


class _SipPort_Type(Integer32):
    """Custom type sipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipPort_Type.__name__ = "Integer32"
_SipPort_Object = MibTableColumn
sipPort = _SipPort_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 6, 1, 1),
    _SipPort_Type()
)
sipPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipPort.setStatus("current")


class _SipTransport_Type(Integer32):
    """Custom type sipTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1),
          ("udpAndTcp", 3))
    )


_SipTransport_Type.__name__ = "Integer32"
_SipTransport_Object = MibTableColumn
sipTransport = _SipTransport_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 6, 1, 2),
    _SipTransport_Type()
)
sipTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipTransport.setStatus("current")
_SipPortStatus_Type = RowStatus
_SipPortStatus_Object = MibTableColumn
sipPortStatus = _SipPortStatus_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 6, 1, 3),
    _SipPortStatus_Type()
)
sipPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipPortStatus.setStatus("current")
_SipUriSupportedTable_Object = MibTable
sipUriSupportedTable = _SipUriSupportedTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sipUriSupportedTable.setStatus("current")
_SipUriSupportedEntry_Object = MibTableRow
sipUriSupportedEntry = _SipUriSupportedEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 7, 1)
)
sipUriSupportedEntry.setIndexNames(
    (0, "SIP-MIB", "sipUriSupportedIndex"),
)
if mibBuilder.loadTexts:
    sipUriSupportedEntry.setStatus("current")


class _SipUriSupportedIndex_Type(Unsigned32):
    """Custom type sipUriSupportedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipUriSupportedIndex_Type.__name__ = "Unsigned32"
_SipUriSupportedIndex_Object = MibTableColumn
sipUriSupportedIndex = _SipUriSupportedIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 7, 1, 1),
    _SipUriSupportedIndex_Type()
)
sipUriSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipUriSupportedIndex.setStatus("current")
_SipUriSupported_Type = SnmpAdminString
_SipUriSupported_Object = MibTableColumn
sipUriSupported = _SipUriSupported_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 7, 1, 2),
    _SipUriSupported_Type()
)
sipUriSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUriSupported.setStatus("current")
_SipFtrSupportedTable_Object = MibTable
sipFtrSupportedTable = _SipFtrSupportedTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    sipFtrSupportedTable.setStatus("current")
_SipFtrSupportedEntry_Object = MibTableRow
sipFtrSupportedEntry = _SipFtrSupportedEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 8, 1)
)
sipFtrSupportedEntry.setIndexNames(
    (0, "SIP-MIB", "sipFtrSupportedIndex"),
)
if mibBuilder.loadTexts:
    sipFtrSupportedEntry.setStatus("current")


class _SipFtrSupportedIndex_Type(Unsigned32):
    """Custom type sipFtrSupportedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipFtrSupportedIndex_Type.__name__ = "Unsigned32"
_SipFtrSupportedIndex_Object = MibTableColumn
sipFtrSupportedIndex = _SipFtrSupportedIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 8, 1, 1),
    _SipFtrSupportedIndex_Type()
)
sipFtrSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipFtrSupportedIndex.setStatus("current")
_SipFtrSupported_Type = SnmpAdminString
_SipFtrSupported_Object = MibTableColumn
sipFtrSupported = _SipFtrSupported_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 8, 1, 2),
    _SipFtrSupported_Type()
)
sipFtrSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipFtrSupported.setStatus("current")
_SipOrganization_Type = SnmpAdminString
_SipOrganization_Object = MibScalar
sipOrganization = _SipOrganization_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 9),
    _SipOrganization_Type()
)
sipOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOrganization.setStatus("current")


class _SipMaxTransactions_Type(Unsigned32):
    """Custom type sipMaxTransactions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipMaxTransactions_Type.__name__ = "Unsigned32"
_SipMaxTransactions_Object = MibScalar
sipMaxTransactions = _SipMaxTransactions_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 10),
    _SipMaxTransactions_Type()
)
sipMaxTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipMaxTransactions.setStatus("current")


class _SipRequestDfltExpires_Type(Unsigned32):
    """Custom type sipRequestDfltExpires based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipRequestDfltExpires_Type.__name__ = "Unsigned32"
_SipRequestDfltExpires_Object = MibScalar
sipRequestDfltExpires = _SipRequestDfltExpires_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 11),
    _SipRequestDfltExpires_Type()
)
sipRequestDfltExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRequestDfltExpires.setStatus("current")
if mibBuilder.loadTexts:
    sipRequestDfltExpires.setUnits("seconds")


class _SipHideOperation_Type(Integer32):
    """Custom type sipHideOperation based on Integer32"""
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
        *(("hop", 2),
          ("none", 1),
          ("route", 3))
    )


_SipHideOperation_Type.__name__ = "Integer32"
_SipHideOperation_Object = MibScalar
sipHideOperation = _SipHideOperation_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 12),
    _SipHideOperation_Type()
)
sipHideOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHideOperation.setStatus("current")
_SipUserLocationServerAddr_Type = SnmpAdminString
_SipUserLocationServerAddr_Object = MibScalar
sipUserLocationServerAddr = _SipUserLocationServerAddr_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 1, 13),
    _SipUserLocationServerAddr_Type()
)
sipUserLocationServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUserLocationServerAddr.setStatus("current")
_SipCommonStats_ObjectIdentity = ObjectIdentity
sipCommonStats = _SipCommonStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2)
)
_SipCommonStatsSummary_ObjectIdentity = ObjectIdentity
sipCommonStatsSummary = _SipCommonStatsSummary_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 1)
)
_SipSummaryInRequests_Type = Counter32
_SipSummaryInRequests_Object = MibScalar
sipSummaryInRequests = _SipSummaryInRequests_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 1, 1),
    _SipSummaryInRequests_Type()
)
sipSummaryInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipSummaryInRequests.setStatus("current")
_SipSummaryOutRequests_Type = Counter32
_SipSummaryOutRequests_Object = MibScalar
sipSummaryOutRequests = _SipSummaryOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 1, 2),
    _SipSummaryOutRequests_Type()
)
sipSummaryOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipSummaryOutRequests.setStatus("current")
_SipSummaryInResponses_Type = Counter32
_SipSummaryInResponses_Object = MibScalar
sipSummaryInResponses = _SipSummaryInResponses_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 1, 3),
    _SipSummaryInResponses_Type()
)
sipSummaryInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipSummaryInResponses.setStatus("current")
_SipSummaryOutResponses_Type = Counter32
_SipSummaryOutResponses_Object = MibScalar
sipSummaryOutResponses = _SipSummaryOutResponses_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 1, 4),
    _SipSummaryOutResponses_Type()
)
sipSummaryOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipSummaryOutResponses.setStatus("current")
_SipSummaryTotalTransactions_Type = Counter32
_SipSummaryTotalTransactions_Object = MibScalar
sipSummaryTotalTransactions = _SipSummaryTotalTransactions_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 1, 5),
    _SipSummaryTotalTransactions_Type()
)
sipSummaryTotalTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipSummaryTotalTransactions.setStatus("current")
_SipCommonStatsMethod_ObjectIdentity = ObjectIdentity
sipCommonStatsMethod = _SipCommonStatsMethod_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2)
)
_SipStatsInviteIns_Type = Counter32
_SipStatsInviteIns_Object = MibScalar
sipStatsInviteIns = _SipStatsInviteIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 1),
    _SipStatsInviteIns_Type()
)
sipStatsInviteIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInviteIns.setStatus("current")
_SipStatsInviteOuts_Type = Counter32
_SipStatsInviteOuts_Object = MibScalar
sipStatsInviteOuts = _SipStatsInviteOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 2),
    _SipStatsInviteOuts_Type()
)
sipStatsInviteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInviteOuts.setStatus("current")
_SipStatsAckIns_Type = Counter32
_SipStatsAckIns_Object = MibScalar
sipStatsAckIns = _SipStatsAckIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 3),
    _SipStatsAckIns_Type()
)
sipStatsAckIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsAckIns.setStatus("current")
_SipStatsAckOuts_Type = Counter32
_SipStatsAckOuts_Object = MibScalar
sipStatsAckOuts = _SipStatsAckOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 4),
    _SipStatsAckOuts_Type()
)
sipStatsAckOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsAckOuts.setStatus("current")
_SipStatsByeIns_Type = Counter32
_SipStatsByeIns_Object = MibScalar
sipStatsByeIns = _SipStatsByeIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 5),
    _SipStatsByeIns_Type()
)
sipStatsByeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsByeIns.setStatus("current")
_SipStatsByeOuts_Type = Counter32
_SipStatsByeOuts_Object = MibScalar
sipStatsByeOuts = _SipStatsByeOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 6),
    _SipStatsByeOuts_Type()
)
sipStatsByeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsByeOuts.setStatus("current")
_SipStatsCancelIns_Type = Counter32
_SipStatsCancelIns_Object = MibScalar
sipStatsCancelIns = _SipStatsCancelIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 7),
    _SipStatsCancelIns_Type()
)
sipStatsCancelIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsCancelIns.setStatus("current")
_SipStatsCancelOuts_Type = Counter32
_SipStatsCancelOuts_Object = MibScalar
sipStatsCancelOuts = _SipStatsCancelOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 8),
    _SipStatsCancelOuts_Type()
)
sipStatsCancelOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsCancelOuts.setStatus("current")
_SipStatsOptionsIns_Type = Counter32
_SipStatsOptionsIns_Object = MibScalar
sipStatsOptionsIns = _SipStatsOptionsIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 9),
    _SipStatsOptionsIns_Type()
)
sipStatsOptionsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsOptionsIns.setStatus("current")
_SipStatsOptionsOuts_Type = Counter32
_SipStatsOptionsOuts_Object = MibScalar
sipStatsOptionsOuts = _SipStatsOptionsOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 10),
    _SipStatsOptionsOuts_Type()
)
sipStatsOptionsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsOptionsOuts.setStatus("current")
_SipStatsRegisterIns_Type = Counter32
_SipStatsRegisterIns_Object = MibScalar
sipStatsRegisterIns = _SipStatsRegisterIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 11),
    _SipStatsRegisterIns_Type()
)
sipStatsRegisterIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRegisterIns.setStatus("current")
_SipStatsRegisterOuts_Type = Counter32
_SipStatsRegisterOuts_Object = MibScalar
sipStatsRegisterOuts = _SipStatsRegisterOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 12),
    _SipStatsRegisterOuts_Type()
)
sipStatsRegisterOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRegisterOuts.setStatus("current")
_SipStatsInfoIns_Type = Counter32
_SipStatsInfoIns_Object = MibScalar
sipStatsInfoIns = _SipStatsInfoIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 13),
    _SipStatsInfoIns_Type()
)
sipStatsInfoIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoIns.setStatus("current")
_SipStatsInfoOuts_Type = Counter32
_SipStatsInfoOuts_Object = MibScalar
sipStatsInfoOuts = _SipStatsInfoOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 2, 14),
    _SipStatsInfoOuts_Type()
)
sipStatsInfoOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoOuts.setStatus("current")
_SipCommonStatsInfo_ObjectIdentity = ObjectIdentity
sipCommonStatsInfo = _SipCommonStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3)
)
_SipStatsInfoTryingIns_Type = Counter32
_SipStatsInfoTryingIns_Object = MibScalar
sipStatsInfoTryingIns = _SipStatsInfoTryingIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 1),
    _SipStatsInfoTryingIns_Type()
)
sipStatsInfoTryingIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoTryingIns.setStatus("current")
_SipStatsInfoTryingOuts_Type = Counter32
_SipStatsInfoTryingOuts_Object = MibScalar
sipStatsInfoTryingOuts = _SipStatsInfoTryingOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 2),
    _SipStatsInfoTryingOuts_Type()
)
sipStatsInfoTryingOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoTryingOuts.setStatus("current")
_SipStatsInfoRingingIns_Type = Counter32
_SipStatsInfoRingingIns_Object = MibScalar
sipStatsInfoRingingIns = _SipStatsInfoRingingIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 3),
    _SipStatsInfoRingingIns_Type()
)
sipStatsInfoRingingIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoRingingIns.setStatus("current")
_SipStatsInfoRingingOuts_Type = Counter32
_SipStatsInfoRingingOuts_Object = MibScalar
sipStatsInfoRingingOuts = _SipStatsInfoRingingOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 4),
    _SipStatsInfoRingingOuts_Type()
)
sipStatsInfoRingingOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoRingingOuts.setStatus("current")
_SipStatsInfoForwardedIns_Type = Counter32
_SipStatsInfoForwardedIns_Object = MibScalar
sipStatsInfoForwardedIns = _SipStatsInfoForwardedIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 5),
    _SipStatsInfoForwardedIns_Type()
)
sipStatsInfoForwardedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoForwardedIns.setStatus("current")
_SipStatsInfoForwardedOuts_Type = Counter32
_SipStatsInfoForwardedOuts_Object = MibScalar
sipStatsInfoForwardedOuts = _SipStatsInfoForwardedOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 6),
    _SipStatsInfoForwardedOuts_Type()
)
sipStatsInfoForwardedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoForwardedOuts.setStatus("current")
_SipStatsInfoQueuedIns_Type = Counter32
_SipStatsInfoQueuedIns_Object = MibScalar
sipStatsInfoQueuedIns = _SipStatsInfoQueuedIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 7),
    _SipStatsInfoQueuedIns_Type()
)
sipStatsInfoQueuedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoQueuedIns.setStatus("current")
_SipStatsInfoQueuedOuts_Type = Counter32
_SipStatsInfoQueuedOuts_Object = MibScalar
sipStatsInfoQueuedOuts = _SipStatsInfoQueuedOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 8),
    _SipStatsInfoQueuedOuts_Type()
)
sipStatsInfoQueuedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoQueuedOuts.setStatus("current")
_SipStatsInfoSessionProgIns_Type = Counter32
_SipStatsInfoSessionProgIns_Object = MibScalar
sipStatsInfoSessionProgIns = _SipStatsInfoSessionProgIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 9),
    _SipStatsInfoSessionProgIns_Type()
)
sipStatsInfoSessionProgIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoSessionProgIns.setStatus("current")
_SipStatsInfoSessionProgOuts_Type = Counter32
_SipStatsInfoSessionProgOuts_Object = MibScalar
sipStatsInfoSessionProgOuts = _SipStatsInfoSessionProgOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 3, 10),
    _SipStatsInfoSessionProgOuts_Type()
)
sipStatsInfoSessionProgOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsInfoSessionProgOuts.setStatus("current")
_SipCommonStatsSuccess_ObjectIdentity = ObjectIdentity
sipCommonStatsSuccess = _SipCommonStatsSuccess_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 4)
)
_SipStatsSuccessOkIns_Type = Counter32
_SipStatsSuccessOkIns_Object = MibScalar
sipStatsSuccessOkIns = _SipStatsSuccessOkIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 4, 1),
    _SipStatsSuccessOkIns_Type()
)
sipStatsSuccessOkIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsSuccessOkIns.setStatus("current")
_SipStatsSuccessOkOuts_Type = Counter32
_SipStatsSuccessOkOuts_Object = MibScalar
sipStatsSuccessOkOuts = _SipStatsSuccessOkOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 4, 2),
    _SipStatsSuccessOkOuts_Type()
)
sipStatsSuccessOkOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsSuccessOkOuts.setStatus("current")
_SipCommonStatsRedirect_ObjectIdentity = ObjectIdentity
sipCommonStatsRedirect = _SipCommonStatsRedirect_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5)
)
_SipStatsRedirMultipleChoiceIns_Type = Counter32
_SipStatsRedirMultipleChoiceIns_Object = MibScalar
sipStatsRedirMultipleChoiceIns = _SipStatsRedirMultipleChoiceIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 1),
    _SipStatsRedirMultipleChoiceIns_Type()
)
sipStatsRedirMultipleChoiceIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirMultipleChoiceIns.setStatus("current")
_SipStatsRedirMultipleChoiceOuts_Type = Counter32
_SipStatsRedirMultipleChoiceOuts_Object = MibScalar
sipStatsRedirMultipleChoiceOuts = _SipStatsRedirMultipleChoiceOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 2),
    _SipStatsRedirMultipleChoiceOuts_Type()
)
sipStatsRedirMultipleChoiceOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirMultipleChoiceOuts.setStatus("current")
_SipStatsRedirMovedPermIns_Type = Counter32
_SipStatsRedirMovedPermIns_Object = MibScalar
sipStatsRedirMovedPermIns = _SipStatsRedirMovedPermIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 3),
    _SipStatsRedirMovedPermIns_Type()
)
sipStatsRedirMovedPermIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirMovedPermIns.setStatus("current")
_SipStatsRedirMovedPermOuts_Type = Counter32
_SipStatsRedirMovedPermOuts_Object = MibScalar
sipStatsRedirMovedPermOuts = _SipStatsRedirMovedPermOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 4),
    _SipStatsRedirMovedPermOuts_Type()
)
sipStatsRedirMovedPermOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirMovedPermOuts.setStatus("current")
_SipStatsRedirMovedTempIns_Type = Counter32
_SipStatsRedirMovedTempIns_Object = MibScalar
sipStatsRedirMovedTempIns = _SipStatsRedirMovedTempIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 5),
    _SipStatsRedirMovedTempIns_Type()
)
sipStatsRedirMovedTempIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirMovedTempIns.setStatus("current")
_SipStatsRedirMovedTempOuts_Type = Counter32
_SipStatsRedirMovedTempOuts_Object = MibScalar
sipStatsRedirMovedTempOuts = _SipStatsRedirMovedTempOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 6),
    _SipStatsRedirMovedTempOuts_Type()
)
sipStatsRedirMovedTempOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirMovedTempOuts.setStatus("current")
_SipStatsRedirSeeOtherIns_Type = Counter32
_SipStatsRedirSeeOtherIns_Object = MibScalar
sipStatsRedirSeeOtherIns = _SipStatsRedirSeeOtherIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 7),
    _SipStatsRedirSeeOtherIns_Type()
)
sipStatsRedirSeeOtherIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirSeeOtherIns.setStatus("current")
_SipStatsRedirSeeOtherOuts_Type = Counter32
_SipStatsRedirSeeOtherOuts_Object = MibScalar
sipStatsRedirSeeOtherOuts = _SipStatsRedirSeeOtherOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 8),
    _SipStatsRedirSeeOtherOuts_Type()
)
sipStatsRedirSeeOtherOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirSeeOtherOuts.setStatus("current")
_SipStatsRedirUseProxyIns_Type = Counter32
_SipStatsRedirUseProxyIns_Object = MibScalar
sipStatsRedirUseProxyIns = _SipStatsRedirUseProxyIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 9),
    _SipStatsRedirUseProxyIns_Type()
)
sipStatsRedirUseProxyIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirUseProxyIns.setStatus("current")
_SipStatsRedirUseProxyOuts_Type = Counter32
_SipStatsRedirUseProxyOuts_Object = MibScalar
sipStatsRedirUseProxyOuts = _SipStatsRedirUseProxyOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 10),
    _SipStatsRedirUseProxyOuts_Type()
)
sipStatsRedirUseProxyOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirUseProxyOuts.setStatus("current")
_SipStatsRedirAltServiceIns_Type = Counter32
_SipStatsRedirAltServiceIns_Object = MibScalar
sipStatsRedirAltServiceIns = _SipStatsRedirAltServiceIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 11),
    _SipStatsRedirAltServiceIns_Type()
)
sipStatsRedirAltServiceIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirAltServiceIns.setStatus("current")
_SipStatsRedirAltServiceOuts_Type = Counter32
_SipStatsRedirAltServiceOuts_Object = MibScalar
sipStatsRedirAltServiceOuts = _SipStatsRedirAltServiceOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 5, 12),
    _SipStatsRedirAltServiceOuts_Type()
)
sipStatsRedirAltServiceOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRedirAltServiceOuts.setStatus("current")
_SipCommonStatsErrClient_ObjectIdentity = ObjectIdentity
sipCommonStatsErrClient = _SipCommonStatsErrClient_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6)
)
_SipStatsClientBadRequestIns_Type = Counter32
_SipStatsClientBadRequestIns_Object = MibScalar
sipStatsClientBadRequestIns = _SipStatsClientBadRequestIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 1),
    _SipStatsClientBadRequestIns_Type()
)
sipStatsClientBadRequestIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientBadRequestIns.setStatus("current")
_SipStatsClientBadRequestOuts_Type = Counter32
_SipStatsClientBadRequestOuts_Object = MibScalar
sipStatsClientBadRequestOuts = _SipStatsClientBadRequestOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 2),
    _SipStatsClientBadRequestOuts_Type()
)
sipStatsClientBadRequestOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientBadRequestOuts.setStatus("current")
_SipStatsClientUnauthorizedIns_Type = Counter32
_SipStatsClientUnauthorizedIns_Object = MibScalar
sipStatsClientUnauthorizedIns = _SipStatsClientUnauthorizedIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 3),
    _SipStatsClientUnauthorizedIns_Type()
)
sipStatsClientUnauthorizedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientUnauthorizedIns.setStatus("current")
_SipStatsClientUnauthorizedOuts_Type = Counter32
_SipStatsClientUnauthorizedOuts_Object = MibScalar
sipStatsClientUnauthorizedOuts = _SipStatsClientUnauthorizedOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 4),
    _SipStatsClientUnauthorizedOuts_Type()
)
sipStatsClientUnauthorizedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientUnauthorizedOuts.setStatus("current")
_SipStatsClientPaymentReqdIns_Type = Counter32
_SipStatsClientPaymentReqdIns_Object = MibScalar
sipStatsClientPaymentReqdIns = _SipStatsClientPaymentReqdIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 5),
    _SipStatsClientPaymentReqdIns_Type()
)
sipStatsClientPaymentReqdIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientPaymentReqdIns.setStatus("current")
_SipStatsClientPaymentReqdOuts_Type = Counter32
_SipStatsClientPaymentReqdOuts_Object = MibScalar
sipStatsClientPaymentReqdOuts = _SipStatsClientPaymentReqdOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 6),
    _SipStatsClientPaymentReqdOuts_Type()
)
sipStatsClientPaymentReqdOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientPaymentReqdOuts.setStatus("current")
_SipStatsClientForbiddenIns_Type = Counter32
_SipStatsClientForbiddenIns_Object = MibScalar
sipStatsClientForbiddenIns = _SipStatsClientForbiddenIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 7),
    _SipStatsClientForbiddenIns_Type()
)
sipStatsClientForbiddenIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientForbiddenIns.setStatus("current")
_SipStatsClientForbiddenOuts_Type = Counter32
_SipStatsClientForbiddenOuts_Object = MibScalar
sipStatsClientForbiddenOuts = _SipStatsClientForbiddenOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 8),
    _SipStatsClientForbiddenOuts_Type()
)
sipStatsClientForbiddenOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientForbiddenOuts.setStatus("current")
_SipStatsClientNotFoundIns_Type = Counter32
_SipStatsClientNotFoundIns_Object = MibScalar
sipStatsClientNotFoundIns = _SipStatsClientNotFoundIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 9),
    _SipStatsClientNotFoundIns_Type()
)
sipStatsClientNotFoundIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientNotFoundIns.setStatus("current")
_SipStatsClientNotFoundOuts_Type = Counter32
_SipStatsClientNotFoundOuts_Object = MibScalar
sipStatsClientNotFoundOuts = _SipStatsClientNotFoundOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 10),
    _SipStatsClientNotFoundOuts_Type()
)
sipStatsClientNotFoundOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientNotFoundOuts.setStatus("current")
_SipStatsClientMethNotAllowedIns_Type = Counter32
_SipStatsClientMethNotAllowedIns_Object = MibScalar
sipStatsClientMethNotAllowedIns = _SipStatsClientMethNotAllowedIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 11),
    _SipStatsClientMethNotAllowedIns_Type()
)
sipStatsClientMethNotAllowedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientMethNotAllowedIns.setStatus("current")
_SipStatsClientMethNotAllowedOuts_Type = Counter32
_SipStatsClientMethNotAllowedOuts_Object = MibScalar
sipStatsClientMethNotAllowedOuts = _SipStatsClientMethNotAllowedOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 12),
    _SipStatsClientMethNotAllowedOuts_Type()
)
sipStatsClientMethNotAllowedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientMethNotAllowedOuts.setStatus("current")
_SipStatsClientNotAcceptableIns_Type = Counter32
_SipStatsClientNotAcceptableIns_Object = MibScalar
sipStatsClientNotAcceptableIns = _SipStatsClientNotAcceptableIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 13),
    _SipStatsClientNotAcceptableIns_Type()
)
sipStatsClientNotAcceptableIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientNotAcceptableIns.setStatus("current")
_SipStatsClientNotAcceptableOuts_Type = Counter32
_SipStatsClientNotAcceptableOuts_Object = MibScalar
sipStatsClientNotAcceptableOuts = _SipStatsClientNotAcceptableOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 14),
    _SipStatsClientNotAcceptableOuts_Type()
)
sipStatsClientNotAcceptableOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientNotAcceptableOuts.setStatus("current")
_SipStatsClientProxyAuthReqdIns_Type = Counter32
_SipStatsClientProxyAuthReqdIns_Object = MibScalar
sipStatsClientProxyAuthReqdIns = _SipStatsClientProxyAuthReqdIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 15),
    _SipStatsClientProxyAuthReqdIns_Type()
)
sipStatsClientProxyAuthReqdIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientProxyAuthReqdIns.setStatus("current")
_SipStatsClientProxyAuthReqdOuts_Type = Counter32
_SipStatsClientProxyAuthReqdOuts_Object = MibScalar
sipStatsClientProxyAuthReqdOuts = _SipStatsClientProxyAuthReqdOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 16),
    _SipStatsClientProxyAuthReqdOuts_Type()
)
sipStatsClientProxyAuthReqdOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientProxyAuthReqdOuts.setStatus("current")
_SipStatsClientReqTimeoutIns_Type = Counter32
_SipStatsClientReqTimeoutIns_Object = MibScalar
sipStatsClientReqTimeoutIns = _SipStatsClientReqTimeoutIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 17),
    _SipStatsClientReqTimeoutIns_Type()
)
sipStatsClientReqTimeoutIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientReqTimeoutIns.setStatus("current")
_SipStatsClientReqTimeoutOuts_Type = Counter32
_SipStatsClientReqTimeoutOuts_Object = MibScalar
sipStatsClientReqTimeoutOuts = _SipStatsClientReqTimeoutOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 18),
    _SipStatsClientReqTimeoutOuts_Type()
)
sipStatsClientReqTimeoutOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientReqTimeoutOuts.setStatus("current")
_SipStatsClientConflictIns_Type = Counter32
_SipStatsClientConflictIns_Object = MibScalar
sipStatsClientConflictIns = _SipStatsClientConflictIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 19),
    _SipStatsClientConflictIns_Type()
)
sipStatsClientConflictIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientConflictIns.setStatus("current")
_SipStatsClientConflictOuts_Type = Counter32
_SipStatsClientConflictOuts_Object = MibScalar
sipStatsClientConflictOuts = _SipStatsClientConflictOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 20),
    _SipStatsClientConflictOuts_Type()
)
sipStatsClientConflictOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientConflictOuts.setStatus("current")
_SipStatsClientGoneIns_Type = Counter32
_SipStatsClientGoneIns_Object = MibScalar
sipStatsClientGoneIns = _SipStatsClientGoneIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 21),
    _SipStatsClientGoneIns_Type()
)
sipStatsClientGoneIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientGoneIns.setStatus("current")
_SipStatsClientGoneOuts_Type = Counter32
_SipStatsClientGoneOuts_Object = MibScalar
sipStatsClientGoneOuts = _SipStatsClientGoneOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 22),
    _SipStatsClientGoneOuts_Type()
)
sipStatsClientGoneOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientGoneOuts.setStatus("current")
_SipStatsClientLengthRequiredIns_Type = Counter32
_SipStatsClientLengthRequiredIns_Object = MibScalar
sipStatsClientLengthRequiredIns = _SipStatsClientLengthRequiredIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 23),
    _SipStatsClientLengthRequiredIns_Type()
)
sipStatsClientLengthRequiredIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientLengthRequiredIns.setStatus("current")
_SipStatsClientLengthRequiredOuts_Type = Counter32
_SipStatsClientLengthRequiredOuts_Object = MibScalar
sipStatsClientLengthRequiredOuts = _SipStatsClientLengthRequiredOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 24),
    _SipStatsClientLengthRequiredOuts_Type()
)
sipStatsClientLengthRequiredOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientLengthRequiredOuts.setStatus("current")
_SipStatsClientReqEntTooLargeIns_Type = Counter32
_SipStatsClientReqEntTooLargeIns_Object = MibScalar
sipStatsClientReqEntTooLargeIns = _SipStatsClientReqEntTooLargeIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 25),
    _SipStatsClientReqEntTooLargeIns_Type()
)
sipStatsClientReqEntTooLargeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientReqEntTooLargeIns.setStatus("current")
_SipStatsClientReqEntTooLargeOuts_Type = Counter32
_SipStatsClientReqEntTooLargeOuts_Object = MibScalar
sipStatsClientReqEntTooLargeOuts = _SipStatsClientReqEntTooLargeOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 26),
    _SipStatsClientReqEntTooLargeOuts_Type()
)
sipStatsClientReqEntTooLargeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientReqEntTooLargeOuts.setStatus("current")
_SipStatsClientReqURITooLargeIns_Type = Counter32
_SipStatsClientReqURITooLargeIns_Object = MibScalar
sipStatsClientReqURITooLargeIns = _SipStatsClientReqURITooLargeIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 27),
    _SipStatsClientReqURITooLargeIns_Type()
)
sipStatsClientReqURITooLargeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientReqURITooLargeIns.setStatus("current")
_SipStatsClientReqURITooLargeOuts_Type = Counter32
_SipStatsClientReqURITooLargeOuts_Object = MibScalar
sipStatsClientReqURITooLargeOuts = _SipStatsClientReqURITooLargeOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 28),
    _SipStatsClientReqURITooLargeOuts_Type()
)
sipStatsClientReqURITooLargeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientReqURITooLargeOuts.setStatus("current")
_SipStatsClientNoSupMediaTypeIns_Type = Counter32
_SipStatsClientNoSupMediaTypeIns_Object = MibScalar
sipStatsClientNoSupMediaTypeIns = _SipStatsClientNoSupMediaTypeIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 29),
    _SipStatsClientNoSupMediaTypeIns_Type()
)
sipStatsClientNoSupMediaTypeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientNoSupMediaTypeIns.setStatus("current")
_SipStatsClientNoSupMediaTypeOuts_Type = Counter32
_SipStatsClientNoSupMediaTypeOuts_Object = MibScalar
sipStatsClientNoSupMediaTypeOuts = _SipStatsClientNoSupMediaTypeOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 30),
    _SipStatsClientNoSupMediaTypeOuts_Type()
)
sipStatsClientNoSupMediaTypeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientNoSupMediaTypeOuts.setStatus("current")
_SipStatsClientBadExtensionIns_Type = Counter32
_SipStatsClientBadExtensionIns_Object = MibScalar
sipStatsClientBadExtensionIns = _SipStatsClientBadExtensionIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 31),
    _SipStatsClientBadExtensionIns_Type()
)
sipStatsClientBadExtensionIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientBadExtensionIns.setStatus("current")
_SipStatsClientBadExtensionOuts_Type = Counter32
_SipStatsClientBadExtensionOuts_Object = MibScalar
sipStatsClientBadExtensionOuts = _SipStatsClientBadExtensionOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 32),
    _SipStatsClientBadExtensionOuts_Type()
)
sipStatsClientBadExtensionOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientBadExtensionOuts.setStatus("current")
_SipStatsClientTempNotAvailIns_Type = Counter32
_SipStatsClientTempNotAvailIns_Object = MibScalar
sipStatsClientTempNotAvailIns = _SipStatsClientTempNotAvailIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 33),
    _SipStatsClientTempNotAvailIns_Type()
)
sipStatsClientTempNotAvailIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientTempNotAvailIns.setStatus("current")
_SipStatsClientTempNotAvailOuts_Type = Counter32
_SipStatsClientTempNotAvailOuts_Object = MibScalar
sipStatsClientTempNotAvailOuts = _SipStatsClientTempNotAvailOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 34),
    _SipStatsClientTempNotAvailOuts_Type()
)
sipStatsClientTempNotAvailOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientTempNotAvailOuts.setStatus("current")
_SipStatsClientCallLegNoExistIns_Type = Counter32
_SipStatsClientCallLegNoExistIns_Object = MibScalar
sipStatsClientCallLegNoExistIns = _SipStatsClientCallLegNoExistIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 35),
    _SipStatsClientCallLegNoExistIns_Type()
)
sipStatsClientCallLegNoExistIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientCallLegNoExistIns.setStatus("current")
_SipStatsClientCallLegNoExistOuts_Type = Counter32
_SipStatsClientCallLegNoExistOuts_Object = MibScalar
sipStatsClientCallLegNoExistOuts = _SipStatsClientCallLegNoExistOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 36),
    _SipStatsClientCallLegNoExistOuts_Type()
)
sipStatsClientCallLegNoExistOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientCallLegNoExistOuts.setStatus("current")
_SipStatsClientLoopDetectedIns_Type = Counter32
_SipStatsClientLoopDetectedIns_Object = MibScalar
sipStatsClientLoopDetectedIns = _SipStatsClientLoopDetectedIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 37),
    _SipStatsClientLoopDetectedIns_Type()
)
sipStatsClientLoopDetectedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientLoopDetectedIns.setStatus("current")
_SipStatsClientLoopDetectedOuts_Type = Counter32
_SipStatsClientLoopDetectedOuts_Object = MibScalar
sipStatsClientLoopDetectedOuts = _SipStatsClientLoopDetectedOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 38),
    _SipStatsClientLoopDetectedOuts_Type()
)
sipStatsClientLoopDetectedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientLoopDetectedOuts.setStatus("current")
_SipStatsClientTooManyHopsIns_Type = Counter32
_SipStatsClientTooManyHopsIns_Object = MibScalar
sipStatsClientTooManyHopsIns = _SipStatsClientTooManyHopsIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 39),
    _SipStatsClientTooManyHopsIns_Type()
)
sipStatsClientTooManyHopsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientTooManyHopsIns.setStatus("current")
_SipStatsClientTooManyHopsOuts_Type = Counter32
_SipStatsClientTooManyHopsOuts_Object = MibScalar
sipStatsClientTooManyHopsOuts = _SipStatsClientTooManyHopsOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 40),
    _SipStatsClientTooManyHopsOuts_Type()
)
sipStatsClientTooManyHopsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientTooManyHopsOuts.setStatus("current")
_SipStatsClientAddrIncompleteIns_Type = Counter32
_SipStatsClientAddrIncompleteIns_Object = MibScalar
sipStatsClientAddrIncompleteIns = _SipStatsClientAddrIncompleteIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 41),
    _SipStatsClientAddrIncompleteIns_Type()
)
sipStatsClientAddrIncompleteIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientAddrIncompleteIns.setStatus("current")
_SipStatsClientAddrIncompleteOuts_Type = Counter32
_SipStatsClientAddrIncompleteOuts_Object = MibScalar
sipStatsClientAddrIncompleteOuts = _SipStatsClientAddrIncompleteOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 42),
    _SipStatsClientAddrIncompleteOuts_Type()
)
sipStatsClientAddrIncompleteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientAddrIncompleteOuts.setStatus("current")
_SipStatsClientAmbiguousIns_Type = Counter32
_SipStatsClientAmbiguousIns_Object = MibScalar
sipStatsClientAmbiguousIns = _SipStatsClientAmbiguousIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 43),
    _SipStatsClientAmbiguousIns_Type()
)
sipStatsClientAmbiguousIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientAmbiguousIns.setStatus("current")
_SipStatsClientAmbiguousOuts_Type = Counter32
_SipStatsClientAmbiguousOuts_Object = MibScalar
sipStatsClientAmbiguousOuts = _SipStatsClientAmbiguousOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 44),
    _SipStatsClientAmbiguousOuts_Type()
)
sipStatsClientAmbiguousOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientAmbiguousOuts.setStatus("current")
_SipStatsClientBusyHereIns_Type = Counter32
_SipStatsClientBusyHereIns_Object = MibScalar
sipStatsClientBusyHereIns = _SipStatsClientBusyHereIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 45),
    _SipStatsClientBusyHereIns_Type()
)
sipStatsClientBusyHereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientBusyHereIns.setStatus("current")
_SipStatsClientBusyHereOuts_Type = Counter32
_SipStatsClientBusyHereOuts_Object = MibScalar
sipStatsClientBusyHereOuts = _SipStatsClientBusyHereOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 6, 46),
    _SipStatsClientBusyHereOuts_Type()
)
sipStatsClientBusyHereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsClientBusyHereOuts.setStatus("current")
_SipCommonStatsErrServer_ObjectIdentity = ObjectIdentity
sipCommonStatsErrServer = _SipCommonStatsErrServer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7)
)
_SipStatsServerIntErrorIns_Type = Counter32
_SipStatsServerIntErrorIns_Object = MibScalar
sipStatsServerIntErrorIns = _SipStatsServerIntErrorIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 1),
    _SipStatsServerIntErrorIns_Type()
)
sipStatsServerIntErrorIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerIntErrorIns.setStatus("current")
_SipStatsServerIntErrorOuts_Type = Counter32
_SipStatsServerIntErrorOuts_Object = MibScalar
sipStatsServerIntErrorOuts = _SipStatsServerIntErrorOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 2),
    _SipStatsServerIntErrorOuts_Type()
)
sipStatsServerIntErrorOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerIntErrorOuts.setStatus("current")
_SipStatsServerNotImplementedIns_Type = Counter32
_SipStatsServerNotImplementedIns_Object = MibScalar
sipStatsServerNotImplementedIns = _SipStatsServerNotImplementedIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 3),
    _SipStatsServerNotImplementedIns_Type()
)
sipStatsServerNotImplementedIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerNotImplementedIns.setStatus("current")
_SipStatsServerNotImplementedOuts_Type = Counter32
_SipStatsServerNotImplementedOuts_Object = MibScalar
sipStatsServerNotImplementedOuts = _SipStatsServerNotImplementedOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 4),
    _SipStatsServerNotImplementedOuts_Type()
)
sipStatsServerNotImplementedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerNotImplementedOuts.setStatus("current")
_SipStatsServerBadGatewayIns_Type = Counter32
_SipStatsServerBadGatewayIns_Object = MibScalar
sipStatsServerBadGatewayIns = _SipStatsServerBadGatewayIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 5),
    _SipStatsServerBadGatewayIns_Type()
)
sipStatsServerBadGatewayIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerBadGatewayIns.setStatus("current")
_SipStatsServerBadGatewayOuts_Type = Counter32
_SipStatsServerBadGatewayOuts_Object = MibScalar
sipStatsServerBadGatewayOuts = _SipStatsServerBadGatewayOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 6),
    _SipStatsServerBadGatewayOuts_Type()
)
sipStatsServerBadGatewayOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerBadGatewayOuts.setStatus("current")
_SipStatsServerServiceUnavailIns_Type = Counter32
_SipStatsServerServiceUnavailIns_Object = MibScalar
sipStatsServerServiceUnavailIns = _SipStatsServerServiceUnavailIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 7),
    _SipStatsServerServiceUnavailIns_Type()
)
sipStatsServerServiceUnavailIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerServiceUnavailIns.setStatus("current")
_SipStatsServerServiceUnavailOuts_Type = Counter32
_SipStatsServerServiceUnavailOuts_Object = MibScalar
sipStatsServerServiceUnavailOuts = _SipStatsServerServiceUnavailOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 8),
    _SipStatsServerServiceUnavailOuts_Type()
)
sipStatsServerServiceUnavailOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerServiceUnavailOuts.setStatus("current")
_SipStatsServerGatewayTimeoutIns_Type = Counter32
_SipStatsServerGatewayTimeoutIns_Object = MibScalar
sipStatsServerGatewayTimeoutIns = _SipStatsServerGatewayTimeoutIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 9),
    _SipStatsServerGatewayTimeoutIns_Type()
)
sipStatsServerGatewayTimeoutIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerGatewayTimeoutIns.setStatus("current")
_SipStatsServerGatewayTimeoutOuts_Type = Counter32
_SipStatsServerGatewayTimeoutOuts_Object = MibScalar
sipStatsServerGatewayTimeoutOuts = _SipStatsServerGatewayTimeoutOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 10),
    _SipStatsServerGatewayTimeoutOuts_Type()
)
sipStatsServerGatewayTimeoutOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerGatewayTimeoutOuts.setStatus("current")
_SipStatsServerBadSipVersionIns_Type = Counter32
_SipStatsServerBadSipVersionIns_Object = MibScalar
sipStatsServerBadSipVersionIns = _SipStatsServerBadSipVersionIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 11),
    _SipStatsServerBadSipVersionIns_Type()
)
sipStatsServerBadSipVersionIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerBadSipVersionIns.setStatus("current")
_SipStatsServerBadSipVersionOuts_Type = Counter32
_SipStatsServerBadSipVersionOuts_Object = MibScalar
sipStatsServerBadSipVersionOuts = _SipStatsServerBadSipVersionOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 7, 12),
    _SipStatsServerBadSipVersionOuts_Type()
)
sipStatsServerBadSipVersionOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsServerBadSipVersionOuts.setStatus("current")
_SipCommonStatsGlobalFail_ObjectIdentity = ObjectIdentity
sipCommonStatsGlobalFail = _SipCommonStatsGlobalFail_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8)
)
_SipStatsGlobalBusyEverywhereIns_Type = Counter32
_SipStatsGlobalBusyEverywhereIns_Object = MibScalar
sipStatsGlobalBusyEverywhereIns = _SipStatsGlobalBusyEverywhereIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 1),
    _SipStatsGlobalBusyEverywhereIns_Type()
)
sipStatsGlobalBusyEverywhereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalBusyEverywhereIns.setStatus("current")
_SipStatsGlobalBusyEverywhereOuts_Type = Counter32
_SipStatsGlobalBusyEverywhereOuts_Object = MibScalar
sipStatsGlobalBusyEverywhereOuts = _SipStatsGlobalBusyEverywhereOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 2),
    _SipStatsGlobalBusyEverywhereOuts_Type()
)
sipStatsGlobalBusyEverywhereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalBusyEverywhereOuts.setStatus("current")
_SipStatsGlobalDeclineIns_Type = Counter32
_SipStatsGlobalDeclineIns_Object = MibScalar
sipStatsGlobalDeclineIns = _SipStatsGlobalDeclineIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 3),
    _SipStatsGlobalDeclineIns_Type()
)
sipStatsGlobalDeclineIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalDeclineIns.setStatus("current")
_SipStatsGlobalDeclineOuts_Type = Counter32
_SipStatsGlobalDeclineOuts_Object = MibScalar
sipStatsGlobalDeclineOuts = _SipStatsGlobalDeclineOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 4),
    _SipStatsGlobalDeclineOuts_Type()
)
sipStatsGlobalDeclineOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalDeclineOuts.setStatus("current")
_SipStatsGlobalNotAnywhereIns_Type = Counter32
_SipStatsGlobalNotAnywhereIns_Object = MibScalar
sipStatsGlobalNotAnywhereIns = _SipStatsGlobalNotAnywhereIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 5),
    _SipStatsGlobalNotAnywhereIns_Type()
)
sipStatsGlobalNotAnywhereIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalNotAnywhereIns.setStatus("current")
_SipStatsGlobalNotAnywhereOuts_Type = Counter32
_SipStatsGlobalNotAnywhereOuts_Object = MibScalar
sipStatsGlobalNotAnywhereOuts = _SipStatsGlobalNotAnywhereOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 6),
    _SipStatsGlobalNotAnywhereOuts_Type()
)
sipStatsGlobalNotAnywhereOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalNotAnywhereOuts.setStatus("current")
_SipStatsGlobalNotAcceptableIns_Type = Counter32
_SipStatsGlobalNotAcceptableIns_Object = MibScalar
sipStatsGlobalNotAcceptableIns = _SipStatsGlobalNotAcceptableIns_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 7),
    _SipStatsGlobalNotAcceptableIns_Type()
)
sipStatsGlobalNotAcceptableIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalNotAcceptableIns.setStatus("current")
_SipStatsGlobalNotAcceptableOuts_Type = Counter32
_SipStatsGlobalNotAcceptableOuts_Object = MibScalar
sipStatsGlobalNotAcceptableOuts = _SipStatsGlobalNotAcceptableOuts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 8, 8),
    _SipStatsGlobalNotAcceptableOuts_Type()
)
sipStatsGlobalNotAcceptableOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsGlobalNotAcceptableOuts.setStatus("current")
_SipCommonStatsTrans_ObjectIdentity = ObjectIdentity
sipCommonStatsTrans = _SipCommonStatsTrans_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9)
)


class _SipCurrentTransactions_Type(Gauge32):
    """Custom type sipCurrentTransactions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipCurrentTransactions_Type.__name__ = "Gauge32"
_SipCurrentTransactions_Object = MibScalar
sipCurrentTransactions = _SipCurrentTransactions_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 1),
    _SipCurrentTransactions_Type()
)
sipCurrentTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCurrentTransactions.setStatus("current")
_SipTransactionTable_Object = MibTable
sipTransactionTable = _SipTransactionTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    sipTransactionTable.setStatus("current")
_SipTransactionEntry_Object = MibTableRow
sipTransactionEntry = _SipTransactionEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1)
)
sipTransactionEntry.setIndexNames(
    (0, "SIP-MIB", "sipTransIndex"),
)
if mibBuilder.loadTexts:
    sipTransactionEntry.setStatus("current")


class _SipTransIndex_Type(Unsigned32):
    """Custom type sipTransIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipTransIndex_Type.__name__ = "Unsigned32"
_SipTransIndex_Object = MibTableColumn
sipTransIndex = _SipTransIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 1),
    _SipTransIndex_Type()
)
sipTransIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipTransIndex.setStatus("current")
_SipTransTo_Type = SnmpAdminString
_SipTransTo_Object = MibTableColumn
sipTransTo = _SipTransTo_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 2),
    _SipTransTo_Type()
)
sipTransTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransTo.setStatus("current")
_SipTransFrom_Type = SnmpAdminString
_SipTransFrom_Object = MibTableColumn
sipTransFrom = _SipTransFrom_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 3),
    _SipTransFrom_Type()
)
sipTransFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransFrom.setStatus("current")
_SipTransCallId_Type = SnmpAdminString
_SipTransCallId_Object = MibTableColumn
sipTransCallId = _SipTransCallId_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 4),
    _SipTransCallId_Type()
)
sipTransCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransCallId.setStatus("current")
_SipTransCSeq_Type = Unsigned32
_SipTransCSeq_Object = MibTableColumn
sipTransCSeq = _SipTransCSeq_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 5),
    _SipTransCSeq_Type()
)
sipTransCSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransCSeq.setStatus("current")


class _SipTransState_Type(Integer32):
    """Custom type sipTransState based on Integer32"""
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
        *(("callProceeding", 6),
          ("calling", 3),
          ("completed", 5),
          ("confirmed", 9),
          ("failure", 7),
          ("initial", 2),
          ("null", 1),
          ("ringing", 4),
          ("success", 8))
    )


_SipTransState_Type.__name__ = "Integer32"
_SipTransState_Object = MibTableColumn
sipTransState = _SipTransState_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 6),
    _SipTransState_Type()
)
sipTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransState.setStatus("current")


class _SipTransOutstandingBranches_Type(Integer32):
    """Custom type sipTransOutstandingBranches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SipTransOutstandingBranches_Type.__name__ = "Integer32"
_SipTransOutstandingBranches_Object = MibTableColumn
sipTransOutstandingBranches = _SipTransOutstandingBranches_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 7),
    _SipTransOutstandingBranches_Type()
)
sipTransOutstandingBranches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransOutstandingBranches.setStatus("current")
_SipTransExpiry_Type = DateAndTime
_SipTransExpiry_Object = MibTableColumn
sipTransExpiry = _SipTransExpiry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 8),
    _SipTransExpiry_Type()
)
sipTransExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransExpiry.setStatus("current")
_SipTransCallingPartyContentType_Type = SnmpAdminString
_SipTransCallingPartyContentType_Object = MibTableColumn
sipTransCallingPartyContentType = _SipTransCallingPartyContentType_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 9),
    _SipTransCallingPartyContentType_Type()
)
sipTransCallingPartyContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransCallingPartyContentType.setStatus("current")
_SipTransCalledPartyContentType_Type = SnmpAdminString
_SipTransCalledPartyContentType_Object = MibTableColumn
sipTransCalledPartyContentType = _SipTransCalledPartyContentType_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 9, 2, 1, 10),
    _SipTransCalledPartyContentType_Type()
)
sipTransCalledPartyContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTransCalledPartyContentType.setStatus("current")
_SipNumUnsupportedUris_Type = Counter32
_SipNumUnsupportedUris_Object = MibScalar
sipNumUnsupportedUris = _SipNumUnsupportedUris_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 1, 2, 10),
    _SipNumUnsupportedUris_Type()
)
sipNumUnsupportedUris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipNumUnsupportedUris.setStatus("current")
_SipUA_ObjectIdentity = ObjectIdentity
sipUA = _SipUA_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2)
)
_SipUACfg_ObjectIdentity = ObjectIdentity
sipUACfg = _SipUACfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1)
)
_SipUACfgTimer_ObjectIdentity = ObjectIdentity
sipUACfgTimer = _SipUACfgTimer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 1)
)


class _SipUACfgTimerTrying_Type(Integer32):
    """Custom type sipUACfgTimerTrying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipUACfgTimerTrying_Type.__name__ = "Integer32"
_SipUACfgTimerTrying_Object = MibScalar
sipUACfgTimerTrying = _SipUACfgTimerTrying_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 1, 1),
    _SipUACfgTimerTrying_Type()
)
sipUACfgTimerTrying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerTrying.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerTrying.setUnits("milliseconds")


class _SipUACfgTimerExpires_Type(Integer32):
    """Custom type sipUACfgTimerExpires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60000, 300000),
    )


_SipUACfgTimerExpires_Type.__name__ = "Integer32"
_SipUACfgTimerExpires_Object = MibScalar
sipUACfgTimerExpires = _SipUACfgTimerExpires_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 1, 2),
    _SipUACfgTimerExpires_Type()
)
sipUACfgTimerExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerExpires.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerExpires.setUnits("milliseconds")


class _SipUACfgTimerConnect_Type(Integer32):
    """Custom type sipUACfgTimerConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipUACfgTimerConnect_Type.__name__ = "Integer32"
_SipUACfgTimerConnect_Object = MibScalar
sipUACfgTimerConnect = _SipUACfgTimerConnect_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 1, 3),
    _SipUACfgTimerConnect_Type()
)
sipUACfgTimerConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerConnect.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerConnect.setUnits("milliseconds")


class _SipUACfgTimerDisconnect_Type(Integer32):
    """Custom type sipUACfgTimerDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipUACfgTimerDisconnect_Type.__name__ = "Integer32"
_SipUACfgTimerDisconnect_Object = MibScalar
sipUACfgTimerDisconnect = _SipUACfgTimerDisconnect_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 1, 4),
    _SipUACfgTimerDisconnect_Type()
)
sipUACfgTimerDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerDisconnect.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerDisconnect.setUnits("milliseconds")
_SipUACfgRetry_ObjectIdentity = ObjectIdentity
sipUACfgRetry = _SipUACfgRetry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 2)
)


class _SipUACfgRetryInvite_Type(Integer32):
    """Custom type sipUACfgRetryInvite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryInvite_Type.__name__ = "Integer32"
_SipUACfgRetryInvite_Object = MibScalar
sipUACfgRetryInvite = _SipUACfgRetryInvite_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 2, 1),
    _SipUACfgRetryInvite_Type()
)
sipUACfgRetryInvite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryInvite.setStatus("current")


class _SipUACfgRetryBye_Type(Integer32):
    """Custom type sipUACfgRetryBye based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryBye_Type.__name__ = "Integer32"
_SipUACfgRetryBye_Object = MibScalar
sipUACfgRetryBye = _SipUACfgRetryBye_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 2, 2),
    _SipUACfgRetryBye_Type()
)
sipUACfgRetryBye.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryBye.setStatus("current")


class _SipUACfgRetryCancel_Type(Integer32):
    """Custom type sipUACfgRetryCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryCancel_Type.__name__ = "Integer32"
_SipUACfgRetryCancel_Object = MibScalar
sipUACfgRetryCancel = _SipUACfgRetryCancel_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 2, 3),
    _SipUACfgRetryCancel_Type()
)
sipUACfgRetryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryCancel.setStatus("current")


class _SipUACfgRetryRegister_Type(Integer32):
    """Custom type sipUACfgRetryRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryRegister_Type.__name__ = "Integer32"
_SipUACfgRetryRegister_Object = MibScalar
sipUACfgRetryRegister = _SipUACfgRetryRegister_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 2, 4),
    _SipUACfgRetryRegister_Type()
)
sipUACfgRetryRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryRegister.setStatus("current")


class _SipUACfgRetryResponse_Type(Integer32):
    """Custom type sipUACfgRetryResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryResponse_Type.__name__ = "Integer32"
_SipUACfgRetryResponse_Object = MibScalar
sipUACfgRetryResponse = _SipUACfgRetryResponse_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 1, 2, 5),
    _SipUACfgRetryResponse_Type()
)
sipUACfgRetryResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryResponse.setStatus("current")
_SipUAStats_ObjectIdentity = ObjectIdentity
sipUAStats = _SipUAStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2)
)
_SipUAStatsRetry_ObjectIdentity = ObjectIdentity
sipUAStatsRetry = _SipUAStatsRetry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2, 1)
)
_SipStatsRetryInvites_Type = Counter32
_SipStatsRetryInvites_Object = MibScalar
sipStatsRetryInvites = _SipStatsRetryInvites_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2, 1, 1),
    _SipStatsRetryInvites_Type()
)
sipStatsRetryInvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryInvites.setStatus("current")
_SipStatsRetryByes_Type = Counter32
_SipStatsRetryByes_Object = MibScalar
sipStatsRetryByes = _SipStatsRetryByes_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2, 1, 2),
    _SipStatsRetryByes_Type()
)
sipStatsRetryByes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryByes.setStatus("current")
_SipStatsRetryCancels_Type = Counter32
_SipStatsRetryCancels_Object = MibScalar
sipStatsRetryCancels = _SipStatsRetryCancels_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2, 1, 3),
    _SipStatsRetryCancels_Type()
)
sipStatsRetryCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryCancels.setStatus("current")
_SipStatsRetryRegisters_Type = Counter32
_SipStatsRetryRegisters_Object = MibScalar
sipStatsRetryRegisters = _SipStatsRetryRegisters_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2, 1, 4),
    _SipStatsRetryRegisters_Type()
)
sipStatsRetryRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryRegisters.setStatus("current")
_SipStatsRetryResponses_Type = Counter32
_SipStatsRetryResponses_Object = MibScalar
sipStatsRetryResponses = _SipStatsRetryResponses_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 2, 2, 1, 5),
    _SipStatsRetryResponses_Type()
)
sipStatsRetryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryResponses.setStatus("current")
_SipServer_ObjectIdentity = ObjectIdentity
sipServer = _SipServer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3)
)
_SipServerCfg_ObjectIdentity = ObjectIdentity
sipServerCfg = _SipServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1)
)
_SipServerHost_Type = SnmpAdminString
_SipServerHost_Object = MibScalar
sipServerHost = _SipServerHost_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 1),
    _SipServerHost_Type()
)
sipServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipServerHost.setStatus("current")
_SipInformationTryingInitial_Type = TruthValue
_SipInformationTryingInitial_Object = MibScalar
sipInformationTryingInitial = _SipInformationTryingInitial_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 2),
    _SipInformationTryingInitial_Type()
)
sipInformationTryingInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInformationTryingInitial.setStatus("current")


class _SipInformationTryingInterval_Type(Integer32):
    """Custom type sipInformationTryingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SipInformationTryingInterval_Type.__name__ = "Integer32"
_SipInformationTryingInterval_Object = MibScalar
sipInformationTryingInterval = _SipInformationTryingInterval_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 3),
    _SipInformationTryingInterval_Type()
)
sipInformationTryingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInformationTryingInterval.setStatus("current")
if mibBuilder.loadTexts:
    sipInformationTryingInterval.setUnits("milliseconds")
_SipPgpVersion_Type = SnmpAdminString
_SipPgpVersion_Object = MibScalar
sipPgpVersion = _SipPgpVersion_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 4),
    _SipPgpVersion_Type()
)
sipPgpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipPgpVersion.setStatus("current")
_SipServerDfltAction_Type = SipServerActions
_SipServerDfltAction_Object = MibScalar
sipServerDfltAction = _SipServerDfltAction_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 5),
    _SipServerDfltAction_Type()
)
sipServerDfltAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipServerDfltAction.setStatus("current")
_SipServerRespectUAAction_Type = TruthValue
_SipServerRespectUAAction_Object = MibScalar
sipServerRespectUAAction = _SipServerRespectUAAction_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 6),
    _SipServerRespectUAAction_Type()
)
sipServerRespectUAAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipServerRespectUAAction.setStatus("current")
_SipRequestUriHostMatching_Type = TruthValue
_SipRequestUriHostMatching_Object = MibScalar
sipRequestUriHostMatching = _SipRequestUriHostMatching_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 1, 7),
    _SipRequestUriHostMatching_Type()
)
sipRequestUriHostMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRequestUriHostMatching.setStatus("current")
_SipServerStats_ObjectIdentity = ObjectIdentity
sipServerStats = _SipServerStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 3, 2)
)
_SipProxy_ObjectIdentity = ObjectIdentity
sipProxy = _SipProxy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4)
)
_SipProxyCfg_ObjectIdentity = ObjectIdentity
sipProxyCfg = _SipProxyCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1)
)


class _SipRequestMaxExpires_Type(Unsigned32):
    """Custom type sipRequestMaxExpires based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipRequestMaxExpires_Type.__name__ = "Unsigned32"
_SipRequestMaxExpires_Object = MibScalar
sipRequestMaxExpires = _SipRequestMaxExpires_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 1),
    _SipRequestMaxExpires_Type()
)
sipRequestMaxExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRequestMaxExpires.setStatus("current")
if mibBuilder.loadTexts:
    sipRequestMaxExpires.setUnits("seconds")
_SipProxyStateful_Type = TruthValue
_SipProxyStateful_Object = MibScalar
sipProxyStateful = _SipProxyStateful_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 2),
    _SipProxyStateful_Type()
)
sipProxyStateful.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyStateful.setStatus("current")
_SipProxySendsCancel_Type = TruthValue
_SipProxySendsCancel_Object = MibScalar
sipProxySendsCancel = _SipProxySendsCancel_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 3),
    _SipProxySendsCancel_Type()
)
sipProxySendsCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxySendsCancel.setStatus("current")
_SipProxyForwardAll1xx_Type = TruthValue
_SipProxyForwardAll1xx_Object = MibScalar
sipProxyForwardAll1xx = _SipProxyForwardAll1xx_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 4),
    _SipProxyForwardAll1xx_Type()
)
sipProxyForwardAll1xx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyForwardAll1xx.setStatus("current")
_SipProxyRecursion_Type = TruthValue
_SipProxyRecursion_Object = MibScalar
sipProxyRecursion = _SipProxyRecursion_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 5),
    _SipProxyRecursion_Type()
)
sipProxyRecursion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyRecursion.setStatus("current")


class _SipProxyProvideAlternatives_Type(TruthValue):
    """Custom type sipProxyProvideAlternatives based on TruthValue"""


_SipProxyProvideAlternatives_Object = MibScalar
sipProxyProvideAlternatives = _SipProxyProvideAlternatives_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 6),
    _SipProxyProvideAlternatives_Type()
)
sipProxyProvideAlternatives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyProvideAlternatives.setStatus("current")
_SipProxyRecordRoute_Type = TruthValue
_SipProxyRecordRoute_Object = MibScalar
sipProxyRecordRoute = _SipProxyRecordRoute_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 7),
    _SipProxyRecordRoute_Type()
)
sipProxyRecordRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyRecordRoute.setStatus("current")
_SipProxyUseCompact_Type = TruthValue
_SipProxyUseCompact_Object = MibScalar
sipProxyUseCompact = _SipProxyUseCompact_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 8),
    _SipProxyUseCompact_Type()
)
sipProxyUseCompact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyUseCompact.setStatus("current")


class _SipProxyRetransmissionBuffer_Type(Integer32):
    """Custom type sipProxyRetransmissionBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SipProxyRetransmissionBuffer_Type.__name__ = "Integer32"
_SipProxyRetransmissionBuffer_Object = MibScalar
sipProxyRetransmissionBuffer = _SipProxyRetransmissionBuffer_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 9),
    _SipProxyRetransmissionBuffer_Type()
)
sipProxyRetransmissionBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyRetransmissionBuffer.setStatus("current")
if mibBuilder.loadTexts:
    sipProxyRetransmissionBuffer.setUnits("seconds")


class _SipProxyAuthMethod_Type(Integer32):
    """Custom type sipProxyAuthMethod based on Integer32"""
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
        *(("basic", 2),
          ("digest", 3),
          ("none", 1),
          ("pgp", 4))
    )


_SipProxyAuthMethod_Type.__name__ = "Integer32"
_SipProxyAuthMethod_Object = MibScalar
sipProxyAuthMethod = _SipProxyAuthMethod_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 10),
    _SipProxyAuthMethod_Type()
)
sipProxyAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyAuthMethod.setStatus("current")


class _SipProxyAuthPgpAlgorithm_Type(Integer32):
    """Custom type sipProxyAuthPgpAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("other", 1),
          ("sha1", 3))
    )


_SipProxyAuthPgpAlgorithm_Type.__name__ = "Integer32"
_SipProxyAuthPgpAlgorithm_Object = MibScalar
sipProxyAuthPgpAlgorithm = _SipProxyAuthPgpAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 11),
    _SipProxyAuthPgpAlgorithm_Type()
)
sipProxyAuthPgpAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyAuthPgpAlgorithm.setStatus("current")
_SipProxyAuthRealm_Type = SnmpAdminString
_SipProxyAuthRealm_Object = MibScalar
sipProxyAuthRealm = _SipProxyAuthRealm_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 12),
    _SipProxyAuthRealm_Type()
)
sipProxyAuthRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyAuthRealm.setStatus("current")


class _SipProxyNonceLifeTime_Type(Integer32):
    """Custom type sipProxyNonceLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipProxyNonceLifeTime_Type.__name__ = "Integer32"
_SipProxyNonceLifeTime_Object = MibScalar
sipProxyNonceLifeTime = _SipProxyNonceLifeTime_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 13),
    _SipProxyNonceLifeTime_Type()
)
sipProxyNonceLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyNonceLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    sipProxyNonceLifeTime.setUnits("milliseconds")


class _SipPgpPrivateKey_Type(OctetString):
    """Custom type sipPgpPrivateKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipPgpPrivateKey_Type.__name__ = "OctetString"
_SipPgpPrivateKey_Object = MibScalar
sipPgpPrivateKey = _SipPgpPrivateKey_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 14),
    _SipPgpPrivateKey_Type()
)
sipPgpPrivateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPgpPrivateKey.setStatus("current")
_SipRxProxyAuthTable_Object = MibTable
sipRxProxyAuthTable = _SipRxProxyAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 15)
)
if mibBuilder.loadTexts:
    sipRxProxyAuthTable.setStatus("current")
_SipRxProxyAuthEntry_Object = MibTableRow
sipRxProxyAuthEntry = _SipRxProxyAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 15, 1)
)
sipRxProxyAuthEntry.setIndexNames(
    (0, "SIP-MIB", "sipRxProxyAuthIndex"),
)
if mibBuilder.loadTexts:
    sipRxProxyAuthEntry.setStatus("current")


class _SipRxProxyAuthIndex_Type(Unsigned32):
    """Custom type sipRxProxyAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipRxProxyAuthIndex_Type.__name__ = "Unsigned32"
_SipRxProxyAuthIndex_Object = MibTableColumn
sipRxProxyAuthIndex = _SipRxProxyAuthIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 15, 1, 1),
    _SipRxProxyAuthIndex_Type()
)
sipRxProxyAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipRxProxyAuthIndex.setStatus("current")
_SipRxProxyAuthRealm_Type = SnmpAdminString
_SipRxProxyAuthRealm_Object = MibTableColumn
sipRxProxyAuthRealm = _SipRxProxyAuthRealm_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 15, 1, 2),
    _SipRxProxyAuthRealm_Type()
)
sipRxProxyAuthRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipRxProxyAuthRealm.setStatus("current")


class _SipRxProxyAuthPassword_Type(OctetString):
    """Custom type sipRxProxyAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4095),
    )


_SipRxProxyAuthPassword_Type.__name__ = "OctetString"
_SipRxProxyAuthPassword_Object = MibTableColumn
sipRxProxyAuthPassword = _SipRxProxyAuthPassword_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 15, 1, 3),
    _SipRxProxyAuthPassword_Type()
)
sipRxProxyAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipRxProxyAuthPassword.setStatus("current")
_SipRxProxyAuthStatus_Type = RowStatus
_SipRxProxyAuthStatus_Object = MibTableColumn
sipRxProxyAuthStatus = _SipRxProxyAuthStatus_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 15, 1, 4),
    _SipRxProxyAuthStatus_Type()
)
sipRxProxyAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipRxProxyAuthStatus.setStatus("current")
_SipHideRespect_Type = TruthValue
_SipHideRespect_Object = MibScalar
sipHideRespect = _SipHideRespect_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 1, 16),
    _SipHideRespect_Type()
)
sipHideRespect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHideRespect.setStatus("current")
_SipProxyStats_ObjectIdentity = ObjectIdentity
sipProxyStats = _SipProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 2)
)
_SipNumProxyRequireFailures_Type = Counter32
_SipNumProxyRequireFailures_Object = MibScalar
sipNumProxyRequireFailures = _SipNumProxyRequireFailures_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 4, 2, 1),
    _SipNumProxyRequireFailures_Type()
)
sipNumProxyRequireFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipNumProxyRequireFailures.setStatus("current")
_SipRedir_ObjectIdentity = ObjectIdentity
sipRedir = _SipRedir_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 5)
)
_SipRedirCfg_ObjectIdentity = ObjectIdentity
sipRedirCfg = _SipRedirCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 5, 1)
)
_SipRedirStats_ObjectIdentity = ObjectIdentity
sipRedirStats = _SipRedirStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 5, 2)
)
_SipReg_ObjectIdentity = ObjectIdentity
sipReg = _SipReg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6)
)
_SipRegCfg_ObjectIdentity = ObjectIdentity
sipRegCfg = _SipRegCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1)
)
_SipRegAllowThirdParty_Type = TruthValue
_SipRegAllowThirdParty_Object = MibScalar
sipRegAllowThirdParty = _SipRegAllowThirdParty_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 1),
    _SipRegAllowThirdParty_Type()
)
sipRegAllowThirdParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegAllowThirdParty.setStatus("current")


class _SipRegContactDfltExpiryDuration_Type(Unsigned32):
    """Custom type sipRegContactDfltExpiryDuration based on Unsigned32"""
    defaultValue = 3600


_SipRegContactDfltExpiryDuration_Object = MibScalar
sipRegContactDfltExpiryDuration = _SipRegContactDfltExpiryDuration_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 2),
    _SipRegContactDfltExpiryDuration_Type()
)
sipRegContactDfltExpiryDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegContactDfltExpiryDuration.setStatus("current")
if mibBuilder.loadTexts:
    sipRegContactDfltExpiryDuration.setUnits("seconds")
_SipRegContactDfltExpiryDate_Type = DateAndTime
_SipRegContactDfltExpiryDate_Object = MibScalar
sipRegContactDfltExpiryDate = _SipRegContactDfltExpiryDate_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 3),
    _SipRegContactDfltExpiryDate_Type()
)
sipRegContactDfltExpiryDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegContactDfltExpiryDate.setStatus("current")


class _SipRegMaxContactExpiryDate_Type(Unsigned32):
    """Custom type sipRegMaxContactExpiryDate based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipRegMaxContactExpiryDate_Type.__name__ = "Unsigned32"
_SipRegMaxContactExpiryDate_Object = MibScalar
sipRegMaxContactExpiryDate = _SipRegMaxContactExpiryDate_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 4),
    _SipRegMaxContactExpiryDate_Type()
)
sipRegMaxContactExpiryDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegMaxContactExpiryDate.setStatus("current")
if mibBuilder.loadTexts:
    sipRegMaxContactExpiryDate.setUnits("seconds")
_SipRegRespHasContacts_Type = TruthValue
_SipRegRespHasContacts_Object = MibScalar
sipRegRespHasContacts = _SipRegRespHasContacts_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 5),
    _SipRegRespHasContacts_Type()
)
sipRegRespHasContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegRespHasContacts.setStatus("current")


class _SipRegMaxUsers_Type(Unsigned32):
    """Custom type sipRegMaxUsers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipRegMaxUsers_Type.__name__ = "Unsigned32"
_SipRegMaxUsers_Object = MibScalar
sipRegMaxUsers = _SipRegMaxUsers_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 6),
    _SipRegMaxUsers_Type()
)
sipRegMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegMaxUsers.setStatus("current")


class _SipRegCurrentUsers_Type(Gauge32):
    """Custom type sipRegCurrentUsers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipRegCurrentUsers_Type.__name__ = "Gauge32"
_SipRegCurrentUsers_Object = MibScalar
sipRegCurrentUsers = _SipRegCurrentUsers_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 7),
    _SipRegCurrentUsers_Type()
)
sipRegCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegCurrentUsers.setStatus("current")
_SipRegUserTable_Object = MibTable
sipRegUserTable = _SipRegUserTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8)
)
if mibBuilder.loadTexts:
    sipRegUserTable.setStatus("current")
_SipRegUserEntry_Object = MibTableRow
sipRegUserEntry = _SipRegUserEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8, 1)
)
sipRegUserEntry.setIndexNames(
    (0, "SIP-MIB", "sipUserIndex"),
)
if mibBuilder.loadTexts:
    sipRegUserEntry.setStatus("current")


class _SipUserIndex_Type(Unsigned32):
    """Custom type sipUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipUserIndex_Type.__name__ = "Unsigned32"
_SipUserIndex_Object = MibTableColumn
sipUserIndex = _SipUserIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8, 1, 1),
    _SipUserIndex_Type()
)
sipUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipUserIndex.setStatus("current")
_SipUserUri_Type = SnmpAdminString
_SipUserUri_Object = MibTableColumn
sipUserUri = _SipUserUri_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8, 1, 2),
    _SipUserUri_Type()
)
sipUserUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipUserUri.setStatus("current")


class _SipUserPassword_Type(OctetString):
    """Custom type sipUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipUserPassword_Type.__name__ = "OctetString"
_SipUserPassword_Object = MibTableColumn
sipUserPassword = _SipUserPassword_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8, 1, 3),
    _SipUserPassword_Type()
)
sipUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipUserPassword.setStatus("current")
_SipUserAuthenticationFailures_Type = Counter32
_SipUserAuthenticationFailures_Object = MibTableColumn
sipUserAuthenticationFailures = _SipUserAuthenticationFailures_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8, 1, 4),
    _SipUserAuthenticationFailures_Type()
)
sipUserAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUserAuthenticationFailures.setStatus("current")
_SipUserTableRowStatus_Type = RowStatus
_SipUserTableRowStatus_Object = MibTableColumn
sipUserTableRowStatus = _SipUserTableRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 8, 1, 5),
    _SipUserTableRowStatus_Type()
)
sipUserTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipUserTableRowStatus.setStatus("current")
_SipContactTable_Object = MibTable
sipContactTable = _SipContactTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9)
)
if mibBuilder.loadTexts:
    sipContactTable.setStatus("current")
_SipContactEntry_Object = MibTableRow
sipContactEntry = _SipContactEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1)
)
sipContactEntry.setIndexNames(
    (0, "SIP-MIB", "sipUserIndex"),
    (0, "SIP-MIB", "sipContactIndex"),
)
if mibBuilder.loadTexts:
    sipContactEntry.setStatus("current")


class _SipContactIndex_Type(Unsigned32):
    """Custom type sipContactIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipContactIndex_Type.__name__ = "Unsigned32"
_SipContactIndex_Object = MibTableColumn
sipContactIndex = _SipContactIndex_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 1),
    _SipContactIndex_Type()
)
sipContactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipContactIndex.setStatus("current")
_SipContactDisplayName_Type = SnmpAdminString
_SipContactDisplayName_Object = MibTableColumn
sipContactDisplayName = _SipContactDisplayName_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 2),
    _SipContactDisplayName_Type()
)
sipContactDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactDisplayName.setStatus("current")
_SipContactURI_Type = SnmpAdminString
_SipContactURI_Object = MibTableColumn
sipContactURI = _SipContactURI_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 3),
    _SipContactURI_Type()
)
sipContactURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactURI.setStatus("current")
_SipContactLastUpdated_Type = TimeStamp
_SipContactLastUpdated_Object = MibTableColumn
sipContactLastUpdated = _SipContactLastUpdated_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 4),
    _SipContactLastUpdated_Type()
)
sipContactLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactLastUpdated.setStatus("current")
_SipContactExpiry_Type = DateAndTime
_SipContactExpiry_Object = MibTableColumn
sipContactExpiry = _SipContactExpiry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 5),
    _SipContactExpiry_Type()
)
sipContactExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactExpiry.setStatus("current")


class _SipContactPreference_Type(OctetString):
    """Custom type sipContactPreference based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipContactPreference_Type.__name__ = "OctetString"
_SipContactPreference_Object = MibTableColumn
sipContactPreference = _SipContactPreference_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 6),
    _SipContactPreference_Type()
)
sipContactPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactPreference.setStatus("current")
_SipContactAction_Type = SipServerActions
_SipContactAction_Object = MibTableColumn
sipContactAction = _SipContactAction_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 7),
    _SipContactAction_Type()
)
sipContactAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactAction.setStatus("current")
_SipContactRetryAfter_Type = DateAndTime
_SipContactRetryAfter_Object = MibTableColumn
sipContactRetryAfter = _SipContactRetryAfter_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 1, 9, 1, 8),
    _SipContactRetryAfter_Type()
)
sipContactRetryAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipContactRetryAfter.setStatus("current")
_SipRegStats_ObjectIdentity = ObjectIdentity
sipRegStats = _SipRegStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 2)
)
_SipRegAcceptedRegistrations_Type = Counter32
_SipRegAcceptedRegistrations_Object = MibScalar
sipRegAcceptedRegistrations = _SipRegAcceptedRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 2, 1),
    _SipRegAcceptedRegistrations_Type()
)
sipRegAcceptedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegAcceptedRegistrations.setStatus("current")
_SipRegRejectedRegistrations_Type = Counter32
_SipRegRejectedRegistrations_Object = MibScalar
sipRegRejectedRegistrations = _SipRegRejectedRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 9998, 1, 6, 2, 2),
    _SipRegRejectedRegistrations_Type()
)
sipRegRejectedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegRejectedRegistrations.setStatus("current")
_SipMIBNotifPrefix_ObjectIdentity = ObjectIdentity
sipMIBNotifPrefix = _SipMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2)
)
_SipMIBNotif_ObjectIdentity = ObjectIdentity
sipMIBNotif = _SipMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2, 0)
)
_SipNotif_ObjectIdentity = ObjectIdentity
sipNotif = _SipNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2, 0, 1)
)
_SipUANotif_ObjectIdentity = ObjectIdentity
sipUANotif = _SipUANotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2, 0, 2)
)
_SipProxyNotif_ObjectIdentity = ObjectIdentity
sipProxyNotif = _SipProxyNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2, 0, 3)
)
_SipRedirNotif_ObjectIdentity = ObjectIdentity
sipRedirNotif = _SipRedirNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2, 0, 4)
)
_SipRegNotif_ObjectIdentity = ObjectIdentity
sipRegNotif = _SipRegNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 2, 0, 5)
)
_SipMIBConformance_ObjectIdentity = ObjectIdentity
sipMIBConformance = _SipMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3)
)
_SipMIBCompliances_ObjectIdentity = ObjectIdentity
sipMIBCompliances = _SipMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1)
)
_SipMIBGroups_ObjectIdentity = ObjectIdentity
sipMIBGroups = _SipMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2)
)

# Managed Objects groups

sipCommonConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1)
)
sipCommonConfigGroup.setObjects(
      *(("SIP-MIB", "sipProtocolVersion"),
        ("SIP-MIB", "sipServiceOperStatus"),
        ("SIP-MIB", "sipServiceAdminStatus"),
        ("SIP-MIB", "sipServiceStartTime"),
        ("SIP-MIB", "sipServiceLastChange"),
        ("SIP-MIB", "sipTransport"),
        ("SIP-MIB", "sipPortStatus"),
        ("SIP-MIB", "sipUriSupported"),
        ("SIP-MIB", "sipFtrSupported"),
        ("SIP-MIB", "sipOrganization"),
        ("SIP-MIB", "sipMaxTransactions"),
        ("SIP-MIB", "sipRequestDfltExpires"),
        ("SIP-MIB", "sipHideOperation"),
        ("SIP-MIB", "sipUserLocationServerAddr"))
)
if mibBuilder.loadTexts:
    sipCommonConfigGroup.setStatus("current")

sipCommonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 2)
)
sipCommonStatsGroup.setObjects(
      *(("SIP-MIB", "sipSummaryInRequests"),
        ("SIP-MIB", "sipSummaryOutRequests"),
        ("SIP-MIB", "sipSummaryInResponses"),
        ("SIP-MIB", "sipSummaryOutResponses"),
        ("SIP-MIB", "sipSummaryTotalTransactions"),
        ("SIP-MIB", "sipStatsInviteIns"),
        ("SIP-MIB", "sipStatsInviteOuts"),
        ("SIP-MIB", "sipStatsAckIns"),
        ("SIP-MIB", "sipStatsAckOuts"),
        ("SIP-MIB", "sipStatsByeIns"),
        ("SIP-MIB", "sipStatsByeOuts"),
        ("SIP-MIB", "sipStatsCancelIns"),
        ("SIP-MIB", "sipStatsCancelOuts"),
        ("SIP-MIB", "sipStatsOptionsIns"),
        ("SIP-MIB", "sipStatsOptionsOuts"),
        ("SIP-MIB", "sipStatsRegisterIns"),
        ("SIP-MIB", "sipStatsRegisterOuts"),
        ("SIP-MIB", "sipStatsInfoIns"),
        ("SIP-MIB", "sipStatsInfoOuts"),
        ("SIP-MIB", "sipStatsInfoTryingIns"),
        ("SIP-MIB", "sipStatsInfoTryingOuts"),
        ("SIP-MIB", "sipStatsInfoRingingIns"),
        ("SIP-MIB", "sipStatsInfoRingingOuts"),
        ("SIP-MIB", "sipStatsInfoForwardedIns"),
        ("SIP-MIB", "sipStatsInfoForwardedOuts"),
        ("SIP-MIB", "sipStatsInfoQueuedIns"),
        ("SIP-MIB", "sipStatsInfoQueuedOuts"),
        ("SIP-MIB", "sipStatsInfoSessionProgIns"),
        ("SIP-MIB", "sipStatsInfoSessionProgOuts"),
        ("SIP-MIB", "sipStatsSuccessOkIns"),
        ("SIP-MIB", "sipStatsSuccessOkOuts"),
        ("SIP-MIB", "sipStatsRedirMultipleChoiceIns"),
        ("SIP-MIB", "sipStatsRedirMultipleChoiceOuts"),
        ("SIP-MIB", "sipStatsRedirMovedPermIns"),
        ("SIP-MIB", "sipStatsRedirMovedPermOuts"),
        ("SIP-MIB", "sipStatsRedirMovedTempIns"),
        ("SIP-MIB", "sipStatsRedirMovedTempOuts"),
        ("SIP-MIB", "sipStatsRedirSeeOtherIns"),
        ("SIP-MIB", "sipStatsRedirSeeOtherOuts"),
        ("SIP-MIB", "sipStatsRedirUseProxyIns"),
        ("SIP-MIB", "sipStatsRedirUseProxyOuts"),
        ("SIP-MIB", "sipStatsRedirAltServiceIns"),
        ("SIP-MIB", "sipStatsRedirAltServiceOuts"),
        ("SIP-MIB", "sipStatsClientBadRequestIns"),
        ("SIP-MIB", "sipStatsClientBadRequestOuts"),
        ("SIP-MIB", "sipStatsClientUnauthorizedIns"),
        ("SIP-MIB", "sipStatsClientUnauthorizedOuts"),
        ("SIP-MIB", "sipStatsClientPaymentReqdIns"),
        ("SIP-MIB", "sipStatsClientPaymentReqdOuts"),
        ("SIP-MIB", "sipStatsClientForbiddenIns"),
        ("SIP-MIB", "sipStatsClientForbiddenOuts"),
        ("SIP-MIB", "sipStatsClientNotFoundIns"),
        ("SIP-MIB", "sipStatsClientNotFoundOuts"),
        ("SIP-MIB", "sipStatsClientMethNotAllowedIns"),
        ("SIP-MIB", "sipStatsClientMethNotAllowedOuts"),
        ("SIP-MIB", "sipStatsClientNotAcceptableIns"),
        ("SIP-MIB", "sipStatsClientNotAcceptableOuts"),
        ("SIP-MIB", "sipStatsClientProxyAuthReqdIns"),
        ("SIP-MIB", "sipStatsClientProxyAuthReqdOuts"),
        ("SIP-MIB", "sipStatsClientReqTimeoutIns"),
        ("SIP-MIB", "sipStatsClientReqTimeoutOuts"),
        ("SIP-MIB", "sipStatsClientConflictIns"),
        ("SIP-MIB", "sipStatsClientConflictOuts"),
        ("SIP-MIB", "sipStatsClientGoneIns"),
        ("SIP-MIB", "sipStatsClientGoneOuts"),
        ("SIP-MIB", "sipStatsClientLengthRequiredIns"),
        ("SIP-MIB", "sipStatsClientLengthRequiredOuts"),
        ("SIP-MIB", "sipStatsClientReqEntTooLargeIns"),
        ("SIP-MIB", "sipStatsClientReqEntTooLargeOuts"),
        ("SIP-MIB", "sipStatsClientReqURITooLargeIns"),
        ("SIP-MIB", "sipStatsClientReqURITooLargeOuts"),
        ("SIP-MIB", "sipStatsClientNoSupMediaTypeIns"),
        ("SIP-MIB", "sipStatsClientNoSupMediaTypeOuts"),
        ("SIP-MIB", "sipStatsClientBadExtensionIns"),
        ("SIP-MIB", "sipStatsClientBadExtensionOuts"),
        ("SIP-MIB", "sipStatsClientTempNotAvailIns"),
        ("SIP-MIB", "sipStatsClientTempNotAvailOuts"),
        ("SIP-MIB", "sipStatsClientCallLegNoExistIns"),
        ("SIP-MIB", "sipStatsClientCallLegNoExistOuts"),
        ("SIP-MIB", "sipStatsClientLoopDetectedIns"),
        ("SIP-MIB", "sipStatsClientLoopDetectedOuts"),
        ("SIP-MIB", "sipStatsClientTooManyHopsIns"),
        ("SIP-MIB", "sipStatsClientTooManyHopsOuts"),
        ("SIP-MIB", "sipStatsClientAddrIncompleteIns"),
        ("SIP-MIB", "sipStatsClientAddrIncompleteOuts"),
        ("SIP-MIB", "sipStatsClientAmbiguousIns"),
        ("SIP-MIB", "sipStatsClientAmbiguousOuts"),
        ("SIP-MIB", "sipStatsClientBusyHereIns"),
        ("SIP-MIB", "sipStatsClientBusyHereOuts"),
        ("SIP-MIB", "sipStatsServerIntErrorIns"),
        ("SIP-MIB", "sipStatsServerIntErrorOuts"),
        ("SIP-MIB", "sipStatsServerNotImplementedIns"),
        ("SIP-MIB", "sipStatsServerNotImplementedOuts"),
        ("SIP-MIB", "sipStatsServerBadGatewayIns"),
        ("SIP-MIB", "sipStatsServerBadGatewayOuts"),
        ("SIP-MIB", "sipStatsServerServiceUnavailIns"),
        ("SIP-MIB", "sipStatsServerServiceUnavailOuts"),
        ("SIP-MIB", "sipStatsServerGatewayTimeoutIns"),
        ("SIP-MIB", "sipStatsServerGatewayTimeoutOuts"),
        ("SIP-MIB", "sipStatsServerBadSipVersionIns"),
        ("SIP-MIB", "sipStatsServerBadSipVersionOuts"),
        ("SIP-MIB", "sipStatsGlobalBusyEverywhereIns"),
        ("SIP-MIB", "sipStatsGlobalBusyEverywhereOuts"),
        ("SIP-MIB", "sipStatsGlobalDeclineIns"),
        ("SIP-MIB", "sipStatsGlobalDeclineOuts"),
        ("SIP-MIB", "sipStatsGlobalNotAnywhereIns"),
        ("SIP-MIB", "sipStatsGlobalNotAnywhereOuts"),
        ("SIP-MIB", "sipStatsGlobalNotAcceptableIns"),
        ("SIP-MIB", "sipStatsGlobalNotAcceptableOuts"),
        ("SIP-MIB", "sipCurrentTransactions"),
        ("SIP-MIB", "sipTransTo"),
        ("SIP-MIB", "sipTransFrom"),
        ("SIP-MIB", "sipTransCallId"),
        ("SIP-MIB", "sipTransCSeq"),
        ("SIP-MIB", "sipTransState"),
        ("SIP-MIB", "sipTransOutstandingBranches"),
        ("SIP-MIB", "sipTransExpiry"),
        ("SIP-MIB", "sipTransCallingPartyContentType"),
        ("SIP-MIB", "sipTransCalledPartyContentType"),
        ("SIP-MIB", "sipNumUnsupportedUris"))
)
if mibBuilder.loadTexts:
    sipCommonStatsGroup.setStatus("current")

sipUAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 4)
)
sipUAConfigGroup.setObjects(
      *(("SIP-MIB", "sipUACfgTimerTrying"),
        ("SIP-MIB", "sipUACfgTimerExpires"),
        ("SIP-MIB", "sipUACfgTimerConnect"),
        ("SIP-MIB", "sipUACfgTimerDisconnect"),
        ("SIP-MIB", "sipUACfgRetryInvite"),
        ("SIP-MIB", "sipUACfgRetryBye"),
        ("SIP-MIB", "sipUACfgRetryCancel"),
        ("SIP-MIB", "sipUACfgRetryRegister"),
        ("SIP-MIB", "sipUACfgRetryResponse"))
)
if mibBuilder.loadTexts:
    sipUAConfigGroup.setStatus("current")

sipUAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 5)
)
sipUAStatsGroup.setObjects(
      *(("SIP-MIB", "sipStatsRetryInvites"),
        ("SIP-MIB", "sipStatsRetryByes"),
        ("SIP-MIB", "sipStatsRetryCancels"),
        ("SIP-MIB", "sipStatsRetryRegisters"),
        ("SIP-MIB", "sipStatsRetryResponses"))
)
if mibBuilder.loadTexts:
    sipUAStatsGroup.setStatus("current")

sipServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 7)
)
sipServerConfigGroup.setObjects(
      *(("SIP-MIB", "sipServerHost"),
        ("SIP-MIB", "sipInformationTryingInitial"),
        ("SIP-MIB", "sipInformationTryingInterval"),
        ("SIP-MIB", "sipPgpVersion"),
        ("SIP-MIB", "sipServerDfltAction"),
        ("SIP-MIB", "sipServerRespectUAAction"),
        ("SIP-MIB", "sipRequestUriHostMatching"))
)
if mibBuilder.loadTexts:
    sipServerConfigGroup.setStatus("current")

sipProxyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 9)
)
sipProxyConfigGroup.setObjects(
      *(("SIP-MIB", "sipRequestMaxExpires"),
        ("SIP-MIB", "sipProxyStateful"),
        ("SIP-MIB", "sipProxySendsCancel"),
        ("SIP-MIB", "sipProxyForwardAll1xx"),
        ("SIP-MIB", "sipProxyRecursion"),
        ("SIP-MIB", "sipProxyProvideAlternatives"),
        ("SIP-MIB", "sipProxyRecordRoute"),
        ("SIP-MIB", "sipProxyUseCompact"),
        ("SIP-MIB", "sipProxyRetransmissionBuffer"),
        ("SIP-MIB", "sipProxyAuthMethod"),
        ("SIP-MIB", "sipProxyAuthPgpAlgorithm"),
        ("SIP-MIB", "sipProxyAuthRealm"),
        ("SIP-MIB", "sipProxyNonceLifeTime"),
        ("SIP-MIB", "sipPgpPrivateKey"),
        ("SIP-MIB", "sipRxProxyAuthRealm"),
        ("SIP-MIB", "sipRxProxyAuthPassword"),
        ("SIP-MIB", "sipRxProxyAuthStatus"),
        ("SIP-MIB", "sipHideRespect"))
)
if mibBuilder.loadTexts:
    sipProxyConfigGroup.setStatus("current")

sipProxyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 10)
)
sipProxyStatsGroup.setObjects(
    ("SIP-MIB", "sipNumProxyRequireFailures")
)
if mibBuilder.loadTexts:
    sipProxyStatsGroup.setStatus("current")

sipRegistrarConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 15)
)
sipRegistrarConfigGroup.setObjects(
      *(("SIP-MIB", "sipRegAllowThirdParty"),
        ("SIP-MIB", "sipRegContactDfltExpiryDuration"),
        ("SIP-MIB", "sipRegContactDfltExpiryDate"),
        ("SIP-MIB", "sipRegMaxContactExpiryDate"),
        ("SIP-MIB", "sipRegRespHasContacts"),
        ("SIP-MIB", "sipRegMaxUsers"),
        ("SIP-MIB", "sipRegCurrentUsers"),
        ("SIP-MIB", "sipUserUri"),
        ("SIP-MIB", "sipUserPassword"),
        ("SIP-MIB", "sipUserAuthenticationFailures"),
        ("SIP-MIB", "sipUserTableRowStatus"),
        ("SIP-MIB", "sipContactDisplayName"),
        ("SIP-MIB", "sipContactURI"),
        ("SIP-MIB", "sipContactLastUpdated"),
        ("SIP-MIB", "sipContactExpiry"),
        ("SIP-MIB", "sipContactPreference"),
        ("SIP-MIB", "sipContactAction"),
        ("SIP-MIB", "sipContactRetryAfter"))
)
if mibBuilder.loadTexts:
    sipRegistrarConfigGroup.setStatus("current")

sipRegistrarStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 16)
)
sipRegistrarStatsGroup.setObjects(
      *(("SIP-MIB", "sipRegAcceptedRegistrations"),
        ("SIP-MIB", "sipRegRejectedRegistrations"))
)
if mibBuilder.loadTexts:
    sipRegistrarStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-MIB",
    **{"SipServerActions": SipServerActions,
       "sipMIB": sipMIB,
       "sipMIBObjects": sipMIBObjects,
       "sipCommon": sipCommon,
       "sipCommonCfg": sipCommonCfg,
       "sipProtocolVersion": sipProtocolVersion,
       "sipServiceOperStatus": sipServiceOperStatus,
       "sipServiceAdminStatus": sipServiceAdminStatus,
       "sipServiceStartTime": sipServiceStartTime,
       "sipServiceLastChange": sipServiceLastChange,
       "sipPortTable": sipPortTable,
       "sipPortEntry": sipPortEntry,
       "sipPort": sipPort,
       "sipTransport": sipTransport,
       "sipPortStatus": sipPortStatus,
       "sipUriSupportedTable": sipUriSupportedTable,
       "sipUriSupportedEntry": sipUriSupportedEntry,
       "sipUriSupportedIndex": sipUriSupportedIndex,
       "sipUriSupported": sipUriSupported,
       "sipFtrSupportedTable": sipFtrSupportedTable,
       "sipFtrSupportedEntry": sipFtrSupportedEntry,
       "sipFtrSupportedIndex": sipFtrSupportedIndex,
       "sipFtrSupported": sipFtrSupported,
       "sipOrganization": sipOrganization,
       "sipMaxTransactions": sipMaxTransactions,
       "sipRequestDfltExpires": sipRequestDfltExpires,
       "sipHideOperation": sipHideOperation,
       "sipUserLocationServerAddr": sipUserLocationServerAddr,
       "sipCommonStats": sipCommonStats,
       "sipCommonStatsSummary": sipCommonStatsSummary,
       "sipSummaryInRequests": sipSummaryInRequests,
       "sipSummaryOutRequests": sipSummaryOutRequests,
       "sipSummaryInResponses": sipSummaryInResponses,
       "sipSummaryOutResponses": sipSummaryOutResponses,
       "sipSummaryTotalTransactions": sipSummaryTotalTransactions,
       "sipCommonStatsMethod": sipCommonStatsMethod,
       "sipStatsInviteIns": sipStatsInviteIns,
       "sipStatsInviteOuts": sipStatsInviteOuts,
       "sipStatsAckIns": sipStatsAckIns,
       "sipStatsAckOuts": sipStatsAckOuts,
       "sipStatsByeIns": sipStatsByeIns,
       "sipStatsByeOuts": sipStatsByeOuts,
       "sipStatsCancelIns": sipStatsCancelIns,
       "sipStatsCancelOuts": sipStatsCancelOuts,
       "sipStatsOptionsIns": sipStatsOptionsIns,
       "sipStatsOptionsOuts": sipStatsOptionsOuts,
       "sipStatsRegisterIns": sipStatsRegisterIns,
       "sipStatsRegisterOuts": sipStatsRegisterOuts,
       "sipStatsInfoIns": sipStatsInfoIns,
       "sipStatsInfoOuts": sipStatsInfoOuts,
       "sipCommonStatsInfo": sipCommonStatsInfo,
       "sipStatsInfoTryingIns": sipStatsInfoTryingIns,
       "sipStatsInfoTryingOuts": sipStatsInfoTryingOuts,
       "sipStatsInfoRingingIns": sipStatsInfoRingingIns,
       "sipStatsInfoRingingOuts": sipStatsInfoRingingOuts,
       "sipStatsInfoForwardedIns": sipStatsInfoForwardedIns,
       "sipStatsInfoForwardedOuts": sipStatsInfoForwardedOuts,
       "sipStatsInfoQueuedIns": sipStatsInfoQueuedIns,
       "sipStatsInfoQueuedOuts": sipStatsInfoQueuedOuts,
       "sipStatsInfoSessionProgIns": sipStatsInfoSessionProgIns,
       "sipStatsInfoSessionProgOuts": sipStatsInfoSessionProgOuts,
       "sipCommonStatsSuccess": sipCommonStatsSuccess,
       "sipStatsSuccessOkIns": sipStatsSuccessOkIns,
       "sipStatsSuccessOkOuts": sipStatsSuccessOkOuts,
       "sipCommonStatsRedirect": sipCommonStatsRedirect,
       "sipStatsRedirMultipleChoiceIns": sipStatsRedirMultipleChoiceIns,
       "sipStatsRedirMultipleChoiceOuts": sipStatsRedirMultipleChoiceOuts,
       "sipStatsRedirMovedPermIns": sipStatsRedirMovedPermIns,
       "sipStatsRedirMovedPermOuts": sipStatsRedirMovedPermOuts,
       "sipStatsRedirMovedTempIns": sipStatsRedirMovedTempIns,
       "sipStatsRedirMovedTempOuts": sipStatsRedirMovedTempOuts,
       "sipStatsRedirSeeOtherIns": sipStatsRedirSeeOtherIns,
       "sipStatsRedirSeeOtherOuts": sipStatsRedirSeeOtherOuts,
       "sipStatsRedirUseProxyIns": sipStatsRedirUseProxyIns,
       "sipStatsRedirUseProxyOuts": sipStatsRedirUseProxyOuts,
       "sipStatsRedirAltServiceIns": sipStatsRedirAltServiceIns,
       "sipStatsRedirAltServiceOuts": sipStatsRedirAltServiceOuts,
       "sipCommonStatsErrClient": sipCommonStatsErrClient,
       "sipStatsClientBadRequestIns": sipStatsClientBadRequestIns,
       "sipStatsClientBadRequestOuts": sipStatsClientBadRequestOuts,
       "sipStatsClientUnauthorizedIns": sipStatsClientUnauthorizedIns,
       "sipStatsClientUnauthorizedOuts": sipStatsClientUnauthorizedOuts,
       "sipStatsClientPaymentReqdIns": sipStatsClientPaymentReqdIns,
       "sipStatsClientPaymentReqdOuts": sipStatsClientPaymentReqdOuts,
       "sipStatsClientForbiddenIns": sipStatsClientForbiddenIns,
       "sipStatsClientForbiddenOuts": sipStatsClientForbiddenOuts,
       "sipStatsClientNotFoundIns": sipStatsClientNotFoundIns,
       "sipStatsClientNotFoundOuts": sipStatsClientNotFoundOuts,
       "sipStatsClientMethNotAllowedIns": sipStatsClientMethNotAllowedIns,
       "sipStatsClientMethNotAllowedOuts": sipStatsClientMethNotAllowedOuts,
       "sipStatsClientNotAcceptableIns": sipStatsClientNotAcceptableIns,
       "sipStatsClientNotAcceptableOuts": sipStatsClientNotAcceptableOuts,
       "sipStatsClientProxyAuthReqdIns": sipStatsClientProxyAuthReqdIns,
       "sipStatsClientProxyAuthReqdOuts": sipStatsClientProxyAuthReqdOuts,
       "sipStatsClientReqTimeoutIns": sipStatsClientReqTimeoutIns,
       "sipStatsClientReqTimeoutOuts": sipStatsClientReqTimeoutOuts,
       "sipStatsClientConflictIns": sipStatsClientConflictIns,
       "sipStatsClientConflictOuts": sipStatsClientConflictOuts,
       "sipStatsClientGoneIns": sipStatsClientGoneIns,
       "sipStatsClientGoneOuts": sipStatsClientGoneOuts,
       "sipStatsClientLengthRequiredIns": sipStatsClientLengthRequiredIns,
       "sipStatsClientLengthRequiredOuts": sipStatsClientLengthRequiredOuts,
       "sipStatsClientReqEntTooLargeIns": sipStatsClientReqEntTooLargeIns,
       "sipStatsClientReqEntTooLargeOuts": sipStatsClientReqEntTooLargeOuts,
       "sipStatsClientReqURITooLargeIns": sipStatsClientReqURITooLargeIns,
       "sipStatsClientReqURITooLargeOuts": sipStatsClientReqURITooLargeOuts,
       "sipStatsClientNoSupMediaTypeIns": sipStatsClientNoSupMediaTypeIns,
       "sipStatsClientNoSupMediaTypeOuts": sipStatsClientNoSupMediaTypeOuts,
       "sipStatsClientBadExtensionIns": sipStatsClientBadExtensionIns,
       "sipStatsClientBadExtensionOuts": sipStatsClientBadExtensionOuts,
       "sipStatsClientTempNotAvailIns": sipStatsClientTempNotAvailIns,
       "sipStatsClientTempNotAvailOuts": sipStatsClientTempNotAvailOuts,
       "sipStatsClientCallLegNoExistIns": sipStatsClientCallLegNoExistIns,
       "sipStatsClientCallLegNoExistOuts": sipStatsClientCallLegNoExistOuts,
       "sipStatsClientLoopDetectedIns": sipStatsClientLoopDetectedIns,
       "sipStatsClientLoopDetectedOuts": sipStatsClientLoopDetectedOuts,
       "sipStatsClientTooManyHopsIns": sipStatsClientTooManyHopsIns,
       "sipStatsClientTooManyHopsOuts": sipStatsClientTooManyHopsOuts,
       "sipStatsClientAddrIncompleteIns": sipStatsClientAddrIncompleteIns,
       "sipStatsClientAddrIncompleteOuts": sipStatsClientAddrIncompleteOuts,
       "sipStatsClientAmbiguousIns": sipStatsClientAmbiguousIns,
       "sipStatsClientAmbiguousOuts": sipStatsClientAmbiguousOuts,
       "sipStatsClientBusyHereIns": sipStatsClientBusyHereIns,
       "sipStatsClientBusyHereOuts": sipStatsClientBusyHereOuts,
       "sipCommonStatsErrServer": sipCommonStatsErrServer,
       "sipStatsServerIntErrorIns": sipStatsServerIntErrorIns,
       "sipStatsServerIntErrorOuts": sipStatsServerIntErrorOuts,
       "sipStatsServerNotImplementedIns": sipStatsServerNotImplementedIns,
       "sipStatsServerNotImplementedOuts": sipStatsServerNotImplementedOuts,
       "sipStatsServerBadGatewayIns": sipStatsServerBadGatewayIns,
       "sipStatsServerBadGatewayOuts": sipStatsServerBadGatewayOuts,
       "sipStatsServerServiceUnavailIns": sipStatsServerServiceUnavailIns,
       "sipStatsServerServiceUnavailOuts": sipStatsServerServiceUnavailOuts,
       "sipStatsServerGatewayTimeoutIns": sipStatsServerGatewayTimeoutIns,
       "sipStatsServerGatewayTimeoutOuts": sipStatsServerGatewayTimeoutOuts,
       "sipStatsServerBadSipVersionIns": sipStatsServerBadSipVersionIns,
       "sipStatsServerBadSipVersionOuts": sipStatsServerBadSipVersionOuts,
       "sipCommonStatsGlobalFail": sipCommonStatsGlobalFail,
       "sipStatsGlobalBusyEverywhereIns": sipStatsGlobalBusyEverywhereIns,
       "sipStatsGlobalBusyEverywhereOuts": sipStatsGlobalBusyEverywhereOuts,
       "sipStatsGlobalDeclineIns": sipStatsGlobalDeclineIns,
       "sipStatsGlobalDeclineOuts": sipStatsGlobalDeclineOuts,
       "sipStatsGlobalNotAnywhereIns": sipStatsGlobalNotAnywhereIns,
       "sipStatsGlobalNotAnywhereOuts": sipStatsGlobalNotAnywhereOuts,
       "sipStatsGlobalNotAcceptableIns": sipStatsGlobalNotAcceptableIns,
       "sipStatsGlobalNotAcceptableOuts": sipStatsGlobalNotAcceptableOuts,
       "sipCommonStatsTrans": sipCommonStatsTrans,
       "sipCurrentTransactions": sipCurrentTransactions,
       "sipTransactionTable": sipTransactionTable,
       "sipTransactionEntry": sipTransactionEntry,
       "sipTransIndex": sipTransIndex,
       "sipTransTo": sipTransTo,
       "sipTransFrom": sipTransFrom,
       "sipTransCallId": sipTransCallId,
       "sipTransCSeq": sipTransCSeq,
       "sipTransState": sipTransState,
       "sipTransOutstandingBranches": sipTransOutstandingBranches,
       "sipTransExpiry": sipTransExpiry,
       "sipTransCallingPartyContentType": sipTransCallingPartyContentType,
       "sipTransCalledPartyContentType": sipTransCalledPartyContentType,
       "sipNumUnsupportedUris": sipNumUnsupportedUris,
       "sipUA": sipUA,
       "sipUACfg": sipUACfg,
       "sipUACfgTimer": sipUACfgTimer,
       "sipUACfgTimerTrying": sipUACfgTimerTrying,
       "sipUACfgTimerExpires": sipUACfgTimerExpires,
       "sipUACfgTimerConnect": sipUACfgTimerConnect,
       "sipUACfgTimerDisconnect": sipUACfgTimerDisconnect,
       "sipUACfgRetry": sipUACfgRetry,
       "sipUACfgRetryInvite": sipUACfgRetryInvite,
       "sipUACfgRetryBye": sipUACfgRetryBye,
       "sipUACfgRetryCancel": sipUACfgRetryCancel,
       "sipUACfgRetryRegister": sipUACfgRetryRegister,
       "sipUACfgRetryResponse": sipUACfgRetryResponse,
       "sipUAStats": sipUAStats,
       "sipUAStatsRetry": sipUAStatsRetry,
       "sipStatsRetryInvites": sipStatsRetryInvites,
       "sipStatsRetryByes": sipStatsRetryByes,
       "sipStatsRetryCancels": sipStatsRetryCancels,
       "sipStatsRetryRegisters": sipStatsRetryRegisters,
       "sipStatsRetryResponses": sipStatsRetryResponses,
       "sipServer": sipServer,
       "sipServerCfg": sipServerCfg,
       "sipServerHost": sipServerHost,
       "sipInformationTryingInitial": sipInformationTryingInitial,
       "sipInformationTryingInterval": sipInformationTryingInterval,
       "sipPgpVersion": sipPgpVersion,
       "sipServerDfltAction": sipServerDfltAction,
       "sipServerRespectUAAction": sipServerRespectUAAction,
       "sipRequestUriHostMatching": sipRequestUriHostMatching,
       "sipServerStats": sipServerStats,
       "sipProxy": sipProxy,
       "sipProxyCfg": sipProxyCfg,
       "sipRequestMaxExpires": sipRequestMaxExpires,
       "sipProxyStateful": sipProxyStateful,
       "sipProxySendsCancel": sipProxySendsCancel,
       "sipProxyForwardAll1xx": sipProxyForwardAll1xx,
       "sipProxyRecursion": sipProxyRecursion,
       "sipProxyProvideAlternatives": sipProxyProvideAlternatives,
       "sipProxyRecordRoute": sipProxyRecordRoute,
       "sipProxyUseCompact": sipProxyUseCompact,
       "sipProxyRetransmissionBuffer": sipProxyRetransmissionBuffer,
       "sipProxyAuthMethod": sipProxyAuthMethod,
       "sipProxyAuthPgpAlgorithm": sipProxyAuthPgpAlgorithm,
       "sipProxyAuthRealm": sipProxyAuthRealm,
       "sipProxyNonceLifeTime": sipProxyNonceLifeTime,
       "sipPgpPrivateKey": sipPgpPrivateKey,
       "sipRxProxyAuthTable": sipRxProxyAuthTable,
       "sipRxProxyAuthEntry": sipRxProxyAuthEntry,
       "sipRxProxyAuthIndex": sipRxProxyAuthIndex,
       "sipRxProxyAuthRealm": sipRxProxyAuthRealm,
       "sipRxProxyAuthPassword": sipRxProxyAuthPassword,
       "sipRxProxyAuthStatus": sipRxProxyAuthStatus,
       "sipHideRespect": sipHideRespect,
       "sipProxyStats": sipProxyStats,
       "sipNumProxyRequireFailures": sipNumProxyRequireFailures,
       "sipRedir": sipRedir,
       "sipRedirCfg": sipRedirCfg,
       "sipRedirStats": sipRedirStats,
       "sipReg": sipReg,
       "sipRegCfg": sipRegCfg,
       "sipRegAllowThirdParty": sipRegAllowThirdParty,
       "sipRegContactDfltExpiryDuration": sipRegContactDfltExpiryDuration,
       "sipRegContactDfltExpiryDate": sipRegContactDfltExpiryDate,
       "sipRegMaxContactExpiryDate": sipRegMaxContactExpiryDate,
       "sipRegRespHasContacts": sipRegRespHasContacts,
       "sipRegMaxUsers": sipRegMaxUsers,
       "sipRegCurrentUsers": sipRegCurrentUsers,
       "sipRegUserTable": sipRegUserTable,
       "sipRegUserEntry": sipRegUserEntry,
       "sipUserIndex": sipUserIndex,
       "sipUserUri": sipUserUri,
       "sipUserPassword": sipUserPassword,
       "sipUserAuthenticationFailures": sipUserAuthenticationFailures,
       "sipUserTableRowStatus": sipUserTableRowStatus,
       "sipContactTable": sipContactTable,
       "sipContactEntry": sipContactEntry,
       "sipContactIndex": sipContactIndex,
       "sipContactDisplayName": sipContactDisplayName,
       "sipContactURI": sipContactURI,
       "sipContactLastUpdated": sipContactLastUpdated,
       "sipContactExpiry": sipContactExpiry,
       "sipContactPreference": sipContactPreference,
       "sipContactAction": sipContactAction,
       "sipContactRetryAfter": sipContactRetryAfter,
       "sipRegStats": sipRegStats,
       "sipRegAcceptedRegistrations": sipRegAcceptedRegistrations,
       "sipRegRejectedRegistrations": sipRegRejectedRegistrations,
       "sipMIBNotifPrefix": sipMIBNotifPrefix,
       "sipMIBNotif": sipMIBNotif,
       "sipNotif": sipNotif,
       "sipUANotif": sipUANotif,
       "sipProxyNotif": sipProxyNotif,
       "sipRedirNotif": sipRedirNotif,
       "sipRegNotif": sipRegNotif,
       "sipMIBConformance": sipMIBConformance,
       "sipMIBCompliances": sipMIBCompliances,
       "sipCompliance": sipCompliance,
       "sipMIBGroups": sipMIBGroups,
       "sipCommonConfigGroup": sipCommonConfigGroup,
       "sipCommonStatsGroup": sipCommonStatsGroup,
       "sipUAConfigGroup": sipUAConfigGroup,
       "sipUAStatsGroup": sipUAStatsGroup,
       "sipServerConfigGroup": sipServerConfigGroup,
       "sipProxyConfigGroup": sipProxyConfigGroup,
       "sipProxyStatsGroup": sipProxyStatsGroup,
       "sipRegistrarConfigGroup": sipRegistrarConfigGroup,
       "sipRegistrarStatsGroup": sipRegistrarStatsGroup}
)
