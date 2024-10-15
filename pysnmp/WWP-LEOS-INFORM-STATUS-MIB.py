# SNMP MIB module (WWP-LEOS-INFORM-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-INFORM-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:54 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosInformStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42)
)
wwpLeosInformStatusMIB.setRevisions(
        ("2012-03-19 00:00",
         "2010-09-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosInformStatusMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusMIBObjects = _WwpLeosInformStatusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1)
)
_WwpLeosInformStatus_ObjectIdentity = ObjectIdentity
wwpLeosInformStatus = _WwpLeosInformStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1)
)
_WwpLeosInformStatusGlobal_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusGlobal = _WwpLeosInformStatusGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 1)
)


class _WwpLeosInformStatusReliableTrapState_Type(Integer32):
    """Custom type wwpLeosInformStatusReliableTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosInformStatusReliableTrapState_Type.__name__ = "Integer32"
_WwpLeosInformStatusReliableTrapState_Object = MibScalar
wwpLeosInformStatusReliableTrapState = _WwpLeosInformStatusReliableTrapState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 1, 1),
    _WwpLeosInformStatusReliableTrapState_Type()
)
wwpLeosInformStatusReliableTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosInformStatusReliableTrapState.setStatus("current")


class _WwpLeosInformStatusReliableTrapStatsClear_Type(Integer32):
    """Custom type wwpLeosInformStatusReliableTrapStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 0))
    )


_WwpLeosInformStatusReliableTrapStatsClear_Type.__name__ = "Integer32"
_WwpLeosInformStatusReliableTrapStatsClear_Object = MibScalar
wwpLeosInformStatusReliableTrapStatsClear = _WwpLeosInformStatusReliableTrapStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 1, 2),
    _WwpLeosInformStatusReliableTrapStatsClear_Type()
)
wwpLeosInformStatusReliableTrapStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosInformStatusReliableTrapStatsClear.setStatus("current")
_WwpLeosInformStatusTable_Object = MibTable
wwpLeosInformStatusTable = _WwpLeosInformStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosInformStatusTable.setStatus("current")
_WwpLeosInformStatusEntry_Object = MibTableRow
wwpLeosInformStatusEntry = _WwpLeosInformStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1)
)
wwpLeosInformStatusEntry.setIndexNames(
    (0, "WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInformStatusTargetIp"),
    (0, "WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInformStatusTargetPort"),
)
if mibBuilder.loadTexts:
    wwpLeosInformStatusEntry.setStatus("current")
_WwpLeosInformStatusTargetIp_Type = IpAddress
_WwpLeosInformStatusTargetIp_Object = MibTableColumn
wwpLeosInformStatusTargetIp = _WwpLeosInformStatusTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 1),
    _WwpLeosInformStatusTargetIp_Type()
)
wwpLeosInformStatusTargetIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosInformStatusTargetIp.setStatus("current")
_WwpLeosInformStatusTargetPort_Type = Unsigned32
_WwpLeosInformStatusTargetPort_Object = MibTableColumn
wwpLeosInformStatusTargetPort = _WwpLeosInformStatusTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 2),
    _WwpLeosInformStatusTargetPort_Type()
)
wwpLeosInformStatusTargetPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosInformStatusTargetPort.setStatus("current")
_WwpLeosInformStatusPendingInforms_Type = Unsigned32
_WwpLeosInformStatusPendingInforms_Object = MibTableColumn
wwpLeosInformStatusPendingInforms = _WwpLeosInformStatusPendingInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 3),
    _WwpLeosInformStatusPendingInforms_Type()
)
wwpLeosInformStatusPendingInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusPendingInforms.setStatus("current")
_WwpLeosInformStatusLostInforms_Type = Unsigned32
_WwpLeosInformStatusLostInforms_Object = MibTableColumn
wwpLeosInformStatusLostInforms = _WwpLeosInformStatusLostInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 4),
    _WwpLeosInformStatusLostInforms_Type()
)
wwpLeosInformStatusLostInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusLostInforms.setStatus("current")
_WwpLeosInformStatusDroppedInforms_Type = Unsigned32
_WwpLeosInformStatusDroppedInforms_Object = MibTableColumn
wwpLeosInformStatusDroppedInforms = _WwpLeosInformStatusDroppedInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 5),
    _WwpLeosInformStatusDroppedInforms_Type()
)
wwpLeosInformStatusDroppedInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusDroppedInforms.setStatus("current")
_WwpLeosInformStatusTimeout_Type = Unsigned32
_WwpLeosInformStatusTimeout_Object = MibTableColumn
wwpLeosInformStatusTimeout = _WwpLeosInformStatusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 6),
    _WwpLeosInformStatusTimeout_Type()
)
wwpLeosInformStatusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosInformStatusTimeout.setUnits("centi-seconds")
_WwpLeosInformStatusRetries_Type = Unsigned32
_WwpLeosInformStatusRetries_Object = MibTableColumn
wwpLeosInformStatusRetries = _WwpLeosInformStatusRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 7),
    _WwpLeosInformStatusRetries_Type()
)
wwpLeosInformStatusRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusRetries.setStatus("current")
_WwpLeosInformStatusCurrentTimeoutValue_Type = Unsigned32
_WwpLeosInformStatusCurrentTimeoutValue_Object = MibTableColumn
wwpLeosInformStatusCurrentTimeoutValue = _WwpLeosInformStatusCurrentTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 8),
    _WwpLeosInformStatusCurrentTimeoutValue_Type()
)
wwpLeosInformStatusCurrentTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusCurrentTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosInformStatusCurrentTimeoutValue.setUnits("centi-seconds")
_WwpLeosInformStatusCurrentRetries_Type = Unsigned32
_WwpLeosInformStatusCurrentRetries_Object = MibTableColumn
wwpLeosInformStatusCurrentRetries = _WwpLeosInformStatusCurrentRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 9),
    _WwpLeosInformStatusCurrentRetries_Type()
)
wwpLeosInformStatusCurrentRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusCurrentRetries.setStatus("current")
_WwpLeosInformStatusTotalTimeouts_Type = Unsigned32
_WwpLeosInformStatusTotalTimeouts_Object = MibTableColumn
wwpLeosInformStatusTotalTimeouts = _WwpLeosInformStatusTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 10),
    _WwpLeosInformStatusTotalTimeouts_Type()
)
wwpLeosInformStatusTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusTotalTimeouts.setStatus("current")
_WwpLeosInformStatusTotalAcknowledgedInforms_Type = Unsigned32
_WwpLeosInformStatusTotalAcknowledgedInforms_Object = MibTableColumn
wwpLeosInformStatusTotalAcknowledgedInforms = _WwpLeosInformStatusTotalAcknowledgedInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 11),
    _WwpLeosInformStatusTotalAcknowledgedInforms_Type()
)
wwpLeosInformStatusTotalAcknowledgedInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusTotalAcknowledgedInforms.setStatus("current")
_WwpLeosInformStatusMaxTransmissions_Type = Unsigned32
_WwpLeosInformStatusMaxTransmissions_Object = MibTableColumn
wwpLeosInformStatusMaxTransmissions = _WwpLeosInformStatusMaxTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 12),
    _WwpLeosInformStatusMaxTransmissions_Type()
)
wwpLeosInformStatusMaxTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusMaxTransmissions.setStatus("current")
_WwpLeosInformStatusMaxDelayToAcknowledgeInform_Type = Unsigned32
_WwpLeosInformStatusMaxDelayToAcknowledgeInform_Object = MibTableColumn
wwpLeosInformStatusMaxDelayToAcknowledgeInform = _WwpLeosInformStatusMaxDelayToAcknowledgeInform_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 13),
    _WwpLeosInformStatusMaxDelayToAcknowledgeInform_Type()
)
wwpLeosInformStatusMaxDelayToAcknowledgeInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusMaxDelayToAcknowledgeInform.setStatus("current")
_WwpLeosInformStatusLastDiscardedInformTimeStamp_Type = TimeTicks
_WwpLeosInformStatusLastDiscardedInformTimeStamp_Object = MibTableColumn
wwpLeosInformStatusLastDiscardedInformTimeStamp = _WwpLeosInformStatusLastDiscardedInformTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 14),
    _WwpLeosInformStatusLastDiscardedInformTimeStamp_Type()
)
wwpLeosInformStatusLastDiscardedInformTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInformStatusLastDiscardedInformTimeStamp.setStatus("current")


class _WwpLeosInformStatusResend_Type(Integer32):
    """Custom type wwpLeosInformStatusResend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("send", 1))
    )


_WwpLeosInformStatusResend_Type.__name__ = "Integer32"
_WwpLeosInformStatusResend_Object = MibTableColumn
wwpLeosInformStatusResend = _WwpLeosInformStatusResend_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 15),
    _WwpLeosInformStatusResend_Type()
)
wwpLeosInformStatusResend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosInformStatusResend.setStatus("current")


class _WwpLeosInformStatusClearStats_Type(Integer32):
    """Custom type wwpLeosInformStatusClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 0))
    )


_WwpLeosInformStatusClearStats_Type.__name__ = "Integer32"
_WwpLeosInformStatusClearStats_Object = MibTableColumn
wwpLeosInformStatusClearStats = _WwpLeosInformStatusClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 2, 1, 16),
    _WwpLeosInformStatusClearStats_Type()
)
wwpLeosInformStatusClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosInformStatusClearStats.setStatus("current")
_WwpLeosInetTargetInformStatusTable_Object = MibTable
wwpLeosInetTargetInformStatusTable = _WwpLeosInetTargetInformStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusTable.setStatus("current")
_WwpLeosInetTargetInformStatusEntry_Object = MibTableRow
wwpLeosInetTargetInformStatusEntry = _WwpLeosInetTargetInformStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1)
)
wwpLeosInetTargetInformStatusEntry.setIndexNames(
    (0, "WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusInetAddrType"),
    (0, "WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusInetAddr"),
    (0, "WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusTargetPort"),
)
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusEntry.setStatus("current")
_WwpLeosInetTargetInformStatusInetAddrType_Type = InetAddressType
_WwpLeosInetTargetInformStatusInetAddrType_Object = MibTableColumn
wwpLeosInetTargetInformStatusInetAddrType = _WwpLeosInetTargetInformStatusInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 1),
    _WwpLeosInetTargetInformStatusInetAddrType_Type()
)
wwpLeosInetTargetInformStatusInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusInetAddrType.setStatus("current")
_WwpLeosInetTargetInformStatusInetAddr_Type = InetAddress
_WwpLeosInetTargetInformStatusInetAddr_Object = MibTableColumn
wwpLeosInetTargetInformStatusInetAddr = _WwpLeosInetTargetInformStatusInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 2),
    _WwpLeosInetTargetInformStatusInetAddr_Type()
)
wwpLeosInetTargetInformStatusInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusInetAddr.setStatus("current")
_WwpLeosInetTargetInformStatusTargetPort_Type = Unsigned32
_WwpLeosInetTargetInformStatusTargetPort_Object = MibTableColumn
wwpLeosInetTargetInformStatusTargetPort = _WwpLeosInetTargetInformStatusTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 3),
    _WwpLeosInetTargetInformStatusTargetPort_Type()
)
wwpLeosInetTargetInformStatusTargetPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusTargetPort.setStatus("current")
_WwpLeosInetTargetInformStatusPendingInforms_Type = Unsigned32
_WwpLeosInetTargetInformStatusPendingInforms_Object = MibTableColumn
wwpLeosInetTargetInformStatusPendingInforms = _WwpLeosInetTargetInformStatusPendingInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 4),
    _WwpLeosInetTargetInformStatusPendingInforms_Type()
)
wwpLeosInetTargetInformStatusPendingInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusPendingInforms.setStatus("current")
_WwpLeosInetTargetInformStatusLostInforms_Type = Unsigned32
_WwpLeosInetTargetInformStatusLostInforms_Object = MibTableColumn
wwpLeosInetTargetInformStatusLostInforms = _WwpLeosInetTargetInformStatusLostInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 5),
    _WwpLeosInetTargetInformStatusLostInforms_Type()
)
wwpLeosInetTargetInformStatusLostInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusLostInforms.setStatus("current")
_WwpLeosInetTargetInformStatusDroppedInforms_Type = Unsigned32
_WwpLeosInetTargetInformStatusDroppedInforms_Object = MibTableColumn
wwpLeosInetTargetInformStatusDroppedInforms = _WwpLeosInetTargetInformStatusDroppedInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 6),
    _WwpLeosInetTargetInformStatusDroppedInforms_Type()
)
wwpLeosInetTargetInformStatusDroppedInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusDroppedInforms.setStatus("current")
_WwpLeosInetTargetInformStatusTimeout_Type = Unsigned32
_WwpLeosInetTargetInformStatusTimeout_Object = MibTableColumn
wwpLeosInetTargetInformStatusTimeout = _WwpLeosInetTargetInformStatusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 7),
    _WwpLeosInetTargetInformStatusTimeout_Type()
)
wwpLeosInetTargetInformStatusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusTimeout.setUnits("centi-seconds")
_WwpLeosInetTargetInformStatusRetries_Type = Unsigned32
_WwpLeosInetTargetInformStatusRetries_Object = MibTableColumn
wwpLeosInetTargetInformStatusRetries = _WwpLeosInetTargetInformStatusRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 8),
    _WwpLeosInetTargetInformStatusRetries_Type()
)
wwpLeosInetTargetInformStatusRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusRetries.setStatus("current")
_WwpLeosInetTargetInformStatusCurrentTimeoutValue_Type = Unsigned32
_WwpLeosInetTargetInformStatusCurrentTimeoutValue_Object = MibTableColumn
wwpLeosInetTargetInformStatusCurrentTimeoutValue = _WwpLeosInetTargetInformStatusCurrentTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 9),
    _WwpLeosInetTargetInformStatusCurrentTimeoutValue_Type()
)
wwpLeosInetTargetInformStatusCurrentTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusCurrentTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusCurrentTimeoutValue.setUnits("centi-seconds")
_WwpLeosInetTargetInformStatusCurrentRetries_Type = Unsigned32
_WwpLeosInetTargetInformStatusCurrentRetries_Object = MibTableColumn
wwpLeosInetTargetInformStatusCurrentRetries = _WwpLeosInetTargetInformStatusCurrentRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 10),
    _WwpLeosInetTargetInformStatusCurrentRetries_Type()
)
wwpLeosInetTargetInformStatusCurrentRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusCurrentRetries.setStatus("current")
_WwpLeosInetTargetInformStatusTotalTimeouts_Type = Unsigned32
_WwpLeosInetTargetInformStatusTotalTimeouts_Object = MibTableColumn
wwpLeosInetTargetInformStatusTotalTimeouts = _WwpLeosInetTargetInformStatusTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 11),
    _WwpLeosInetTargetInformStatusTotalTimeouts_Type()
)
wwpLeosInetTargetInformStatusTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusTotalTimeouts.setStatus("current")
_WwpLeosInetTargetInformStatusTotalAcknowledgedInforms_Type = Unsigned32
_WwpLeosInetTargetInformStatusTotalAcknowledgedInforms_Object = MibTableColumn
wwpLeosInetTargetInformStatusTotalAcknowledgedInforms = _WwpLeosInetTargetInformStatusTotalAcknowledgedInforms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 12),
    _WwpLeosInetTargetInformStatusTotalAcknowledgedInforms_Type()
)
wwpLeosInetTargetInformStatusTotalAcknowledgedInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusTotalAcknowledgedInforms.setStatus("current")
_WwpLeosInetTargetInformStatusMaxTransmissions_Type = Unsigned32
_WwpLeosInetTargetInformStatusMaxTransmissions_Object = MibTableColumn
wwpLeosInetTargetInformStatusMaxTransmissions = _WwpLeosInetTargetInformStatusMaxTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 13),
    _WwpLeosInetTargetInformStatusMaxTransmissions_Type()
)
wwpLeosInetTargetInformStatusMaxTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusMaxTransmissions.setStatus("current")
_WwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform_Type = Unsigned32
_WwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform_Object = MibTableColumn
wwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform = _WwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 14),
    _WwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform_Type()
)
wwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform.setStatus("current")
_WwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp_Type = TimeTicks
_WwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp_Object = MibTableColumn
wwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp = _WwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 15),
    _WwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp_Type()
)
wwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp.setStatus("current")


class _WwpLeosInetTargetInformStatusResend_Type(Integer32):
    """Custom type wwpLeosInetTargetInformStatusResend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("send", 1))
    )


_WwpLeosInetTargetInformStatusResend_Type.__name__ = "Integer32"
_WwpLeosInetTargetInformStatusResend_Object = MibTableColumn
wwpLeosInetTargetInformStatusResend = _WwpLeosInetTargetInformStatusResend_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 16),
    _WwpLeosInetTargetInformStatusResend_Type()
)
wwpLeosInetTargetInformStatusResend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusResend.setStatus("current")


class _WwpLeosInetTargetInformStatusClearStats_Type(Integer32):
    """Custom type wwpLeosInetTargetInformStatusClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 0))
    )


_WwpLeosInetTargetInformStatusClearStats_Type.__name__ = "Integer32"
_WwpLeosInetTargetInformStatusClearStats_Object = MibTableColumn
wwpLeosInetTargetInformStatusClearStats = _WwpLeosInetTargetInformStatusClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 1, 1, 3, 1, 17),
    _WwpLeosInetTargetInformStatusClearStats_Type()
)
wwpLeosInetTargetInformStatusClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusClearStats.setStatus("current")
_WwpLeosInformStatusMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusMIBNotificationPrefix = _WwpLeosInformStatusMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 2)
)
_WwpLeosInformStatusMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusMIBNotifications = _WwpLeosInformStatusMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 2, 0)
)
_WwpLeosInformStatusMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusMIBConformance = _WwpLeosInformStatusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 3)
)
_WwpLeosInformStatusMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusMIBCompliances = _WwpLeosInformStatusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 3, 1)
)
_WwpLeosInformStatusMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosInformStatusMIBGroups = _WwpLeosInformStatusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 3, 2)
)

# Managed Objects groups

wwpLeosInetTargetInformStatusIPv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 3, 2, 1)
)
wwpLeosInetTargetInformStatusIPv6Group.setObjects(
      *(("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusInetAddrType"),
        ("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusInetAddr"))
)
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusIPv6Group.setStatus("current")


# Notification objects

wwpLeosInformDiscardNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 2, 0, 1)
)
wwpLeosInformDiscardNotification.setObjects(
      *(("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInformStatusTargetIp"),
        ("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInformStatusLostInforms"),
        ("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInformStatusLastDiscardedInformTimeStamp"))
)
if mibBuilder.loadTexts:
    wwpLeosInformDiscardNotification.setStatus(
        "current"
    )

wwpLeosInetTargetInformDiscardNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 2, 0, 2)
)
wwpLeosInetTargetInformDiscardNotification.setObjects(
      *(("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusInetAddr"),
        ("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusInetAddrType"),
        ("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusLostInforms"),
        ("WWP-LEOS-INFORM-STATUS-MIB", "wwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp"))
)
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformDiscardNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

wwpLeosInetTargetInformStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 42, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosInetTargetInformStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-INFORM-STATUS-MIB",
    **{"wwpLeosInformStatusMIB": wwpLeosInformStatusMIB,
       "wwpLeosInformStatusMIBObjects": wwpLeosInformStatusMIBObjects,
       "wwpLeosInformStatus": wwpLeosInformStatus,
       "wwpLeosInformStatusGlobal": wwpLeosInformStatusGlobal,
       "wwpLeosInformStatusReliableTrapState": wwpLeosInformStatusReliableTrapState,
       "wwpLeosInformStatusReliableTrapStatsClear": wwpLeosInformStatusReliableTrapStatsClear,
       "wwpLeosInformStatusTable": wwpLeosInformStatusTable,
       "wwpLeosInformStatusEntry": wwpLeosInformStatusEntry,
       "wwpLeosInformStatusTargetIp": wwpLeosInformStatusTargetIp,
       "wwpLeosInformStatusTargetPort": wwpLeosInformStatusTargetPort,
       "wwpLeosInformStatusPendingInforms": wwpLeosInformStatusPendingInforms,
       "wwpLeosInformStatusLostInforms": wwpLeosInformStatusLostInforms,
       "wwpLeosInformStatusDroppedInforms": wwpLeosInformStatusDroppedInforms,
       "wwpLeosInformStatusTimeout": wwpLeosInformStatusTimeout,
       "wwpLeosInformStatusRetries": wwpLeosInformStatusRetries,
       "wwpLeosInformStatusCurrentTimeoutValue": wwpLeosInformStatusCurrentTimeoutValue,
       "wwpLeosInformStatusCurrentRetries": wwpLeosInformStatusCurrentRetries,
       "wwpLeosInformStatusTotalTimeouts": wwpLeosInformStatusTotalTimeouts,
       "wwpLeosInformStatusTotalAcknowledgedInforms": wwpLeosInformStatusTotalAcknowledgedInforms,
       "wwpLeosInformStatusMaxTransmissions": wwpLeosInformStatusMaxTransmissions,
       "wwpLeosInformStatusMaxDelayToAcknowledgeInform": wwpLeosInformStatusMaxDelayToAcknowledgeInform,
       "wwpLeosInformStatusLastDiscardedInformTimeStamp": wwpLeosInformStatusLastDiscardedInformTimeStamp,
       "wwpLeosInformStatusResend": wwpLeosInformStatusResend,
       "wwpLeosInformStatusClearStats": wwpLeosInformStatusClearStats,
       "wwpLeosInetTargetInformStatusTable": wwpLeosInetTargetInformStatusTable,
       "wwpLeosInetTargetInformStatusEntry": wwpLeosInetTargetInformStatusEntry,
       "wwpLeosInetTargetInformStatusInetAddrType": wwpLeosInetTargetInformStatusInetAddrType,
       "wwpLeosInetTargetInformStatusInetAddr": wwpLeosInetTargetInformStatusInetAddr,
       "wwpLeosInetTargetInformStatusTargetPort": wwpLeosInetTargetInformStatusTargetPort,
       "wwpLeosInetTargetInformStatusPendingInforms": wwpLeosInetTargetInformStatusPendingInforms,
       "wwpLeosInetTargetInformStatusLostInforms": wwpLeosInetTargetInformStatusLostInforms,
       "wwpLeosInetTargetInformStatusDroppedInforms": wwpLeosInetTargetInformStatusDroppedInforms,
       "wwpLeosInetTargetInformStatusTimeout": wwpLeosInetTargetInformStatusTimeout,
       "wwpLeosInetTargetInformStatusRetries": wwpLeosInetTargetInformStatusRetries,
       "wwpLeosInetTargetInformStatusCurrentTimeoutValue": wwpLeosInetTargetInformStatusCurrentTimeoutValue,
       "wwpLeosInetTargetInformStatusCurrentRetries": wwpLeosInetTargetInformStatusCurrentRetries,
       "wwpLeosInetTargetInformStatusTotalTimeouts": wwpLeosInetTargetInformStatusTotalTimeouts,
       "wwpLeosInetTargetInformStatusTotalAcknowledgedInforms": wwpLeosInetTargetInformStatusTotalAcknowledgedInforms,
       "wwpLeosInetTargetInformStatusMaxTransmissions": wwpLeosInetTargetInformStatusMaxTransmissions,
       "wwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform": wwpLeosInetTargetInformStatusMaxDelayToAcknowledgeInform,
       "wwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp": wwpLeosInetTargetInformStatusLastDiscardedInformTimeStamp,
       "wwpLeosInetTargetInformStatusResend": wwpLeosInetTargetInformStatusResend,
       "wwpLeosInetTargetInformStatusClearStats": wwpLeosInetTargetInformStatusClearStats,
       "wwpLeosInformStatusMIBNotificationPrefix": wwpLeosInformStatusMIBNotificationPrefix,
       "wwpLeosInformStatusMIBNotifications": wwpLeosInformStatusMIBNotifications,
       "wwpLeosInformDiscardNotification": wwpLeosInformDiscardNotification,
       "wwpLeosInetTargetInformDiscardNotification": wwpLeosInetTargetInformDiscardNotification,
       "wwpLeosInformStatusMIBConformance": wwpLeosInformStatusMIBConformance,
       "wwpLeosInformStatusMIBCompliances": wwpLeosInformStatusMIBCompliances,
       "wwpLeosInetTargetInformStatusCompliance": wwpLeosInetTargetInformStatusCompliance,
       "wwpLeosInformStatusMIBGroups": wwpLeosInformStatusMIBGroups,
       "wwpLeosInetTargetInformStatusIPv6Group": wwpLeosInetTargetInformStatusIPv6Group}
)
