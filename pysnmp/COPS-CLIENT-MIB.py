# SNMP MIB module (COPS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COPS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:04 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

copsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 89)
)
copsClientMIB.setRevisions(
        ("2000-09-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CopsClientState(Integer32, TextualConvention):
    status = "current"
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
        *(("copsClientAccepted", 5),
          ("copsClientAuthenticating", 3),
          ("copsClientInvalid", 1),
          ("copsClientSecAccepted", 4),
          ("copsClientTcpconnected", 2),
          ("copsClientTimingout", 6))
    )



class CopsServerEntryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copsServerRedirect", 2),
          ("copsServerStatic", 1))
    )



class CopsErrorCode(Integer32, TextualConvention):
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("errorAuthenticationFailure", 14),
          ("errorAuthenticationMissing", 15),
          ("errorBadHandle", 1),
          ("errorBadMessageFormat", 3),
          ("errorClientFailure", 8),
          ("errorCommunicationFailure", 9),
          ("errorInvalidHandleReference", 2),
          ("errorMandatoryClientSiMissing", 5),
          ("errorMandatoryCopsObjectMissing", 7),
          ("errorOther", 0),
          ("errorRedirectToPreferredServer", 12),
          ("errorShuttingDown", 11),
          ("errorUnableToProcess", 4),
          ("errorUnknownCopsObject", 13),
          ("errorUnspecified", 10),
          ("errorUnsupportedClientType", 6))
    )



class CopsTcpPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CopsAuthType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("authCopsIntegrity", 5),
          ("authIpSecAh", 2),
          ("authIpSecEsp", 3),
          ("authNone", 0),
          ("authOther", 1),
          ("authTls", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CopsClientMIBObjects_ObjectIdentity = ObjectIdentity
copsClientMIBObjects = _CopsClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 1)
)
_CopsClientCapabilitiesGroup_ObjectIdentity = ObjectIdentity
copsClientCapabilitiesGroup = _CopsClientCapabilitiesGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 1, 1)
)


class _CopsClientCapabilities_Type(Bits):
    """Custom type copsClientCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("copsClientAuthInteg", 4),
          ("copsClientAuthIpSecAh", 1),
          ("copsClientAuthIpSecEsp", 2),
          ("copsClientAuthTls", 3),
          ("copsClientVersion1", 0))
    )

_CopsClientCapabilities_Type.__name__ = "Bits"
_CopsClientCapabilities_Object = MibScalar
copsClientCapabilities = _CopsClientCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 1, 1),
    _CopsClientCapabilities_Type()
)
copsClientCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientCapabilities.setStatus("current")
_CopsClientStatusGroup_ObjectIdentity = ObjectIdentity
copsClientStatusGroup = _CopsClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 1, 2)
)
_CopsClientServerCurrentTable_Object = MibTable
copsClientServerCurrentTable = _CopsClientServerCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1)
)
if mibBuilder.loadTexts:
    copsClientServerCurrentTable.setStatus("current")
_CopsClientServerCurrentEntry_Object = MibTableRow
copsClientServerCurrentEntry = _CopsClientServerCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1)
)
copsClientServerCurrentEntry.setIndexNames(
    (0, "COPS-CLIENT-MIB", "copsClientServerAddressType"),
    (0, "COPS-CLIENT-MIB", "copsClientServerAddress"),
    (0, "COPS-CLIENT-MIB", "copsClientServerClientType"),
)
if mibBuilder.loadTexts:
    copsClientServerCurrentEntry.setStatus("current")
_CopsClientServerAddressType_Type = InetAddressType
_CopsClientServerAddressType_Object = MibTableColumn
copsClientServerAddressType = _CopsClientServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 1),
    _CopsClientServerAddressType_Type()
)
copsClientServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerAddressType.setStatus("current")
_CopsClientServerAddress_Type = InetAddress
_CopsClientServerAddress_Object = MibTableColumn
copsClientServerAddress = _CopsClientServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 2),
    _CopsClientServerAddress_Type()
)
copsClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerAddress.setStatus("current")


class _CopsClientServerClientType_Type(Integer32):
    """Custom type copsClientServerClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CopsClientServerClientType_Type.__name__ = "Integer32"
_CopsClientServerClientType_Object = MibTableColumn
copsClientServerClientType = _CopsClientServerClientType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 3),
    _CopsClientServerClientType_Type()
)
copsClientServerClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerClientType.setStatus("current")
_CopsClientServerTcpPort_Type = CopsTcpPort
_CopsClientServerTcpPort_Object = MibTableColumn
copsClientServerTcpPort = _CopsClientServerTcpPort_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 4),
    _CopsClientServerTcpPort_Type()
)
copsClientServerTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientServerTcpPort.setStatus("current")
_CopsClientServerType_Type = CopsServerEntryType
_CopsClientServerType_Object = MibTableColumn
copsClientServerType = _CopsClientServerType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 5),
    _CopsClientServerType_Type()
)
copsClientServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientServerType.setStatus("current")
_CopsClientServerAuthType_Type = CopsAuthType
_CopsClientServerAuthType_Object = MibTableColumn
copsClientServerAuthType = _CopsClientServerAuthType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 6),
    _CopsClientServerAuthType_Type()
)
copsClientServerAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientServerAuthType.setStatus("current")
_CopsClientServerLastConnAttempt_Type = TimeStamp
_CopsClientServerLastConnAttempt_Object = MibTableColumn
copsClientServerLastConnAttempt = _CopsClientServerLastConnAttempt_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 7),
    _CopsClientServerLastConnAttempt_Type()
)
copsClientServerLastConnAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientServerLastConnAttempt.setStatus("current")
_CopsClientState_Type = CopsClientState
_CopsClientState_Object = MibTableColumn
copsClientState = _CopsClientState_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 8),
    _CopsClientState_Type()
)
copsClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientState.setStatus("current")
_CopsClientServerKeepaliveTime_Type = TimeInterval
_CopsClientServerKeepaliveTime_Object = MibTableColumn
copsClientServerKeepaliveTime = _CopsClientServerKeepaliveTime_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 9),
    _CopsClientServerKeepaliveTime_Type()
)
copsClientServerKeepaliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientServerKeepaliveTime.setStatus("current")
_CopsClientServerAccountingTime_Type = TimeInterval
_CopsClientServerAccountingTime_Object = MibTableColumn
copsClientServerAccountingTime = _CopsClientServerAccountingTime_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 10),
    _CopsClientServerAccountingTime_Type()
)
copsClientServerAccountingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientServerAccountingTime.setStatus("current")
_CopsClientInPkts_Type = Counter32
_CopsClientInPkts_Object = MibTableColumn
copsClientInPkts = _CopsClientInPkts_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 11),
    _CopsClientInPkts_Type()
)
copsClientInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientInPkts.setStatus("current")
_CopsClientOutPkts_Type = Counter32
_CopsClientOutPkts_Object = MibTableColumn
copsClientOutPkts = _CopsClientOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 12),
    _CopsClientOutPkts_Type()
)
copsClientOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientOutPkts.setStatus("current")
_CopsClientInErrs_Type = Counter32
_CopsClientInErrs_Object = MibTableColumn
copsClientInErrs = _CopsClientInErrs_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 13),
    _CopsClientInErrs_Type()
)
copsClientInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientInErrs.setStatus("current")
_CopsClientLastError_Type = CopsErrorCode
_CopsClientLastError_Object = MibTableColumn
copsClientLastError = _CopsClientLastError_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 14),
    _CopsClientLastError_Type()
)
copsClientLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientLastError.setStatus("current")
_CopsClientTcpConnectAttempts_Type = Counter32
_CopsClientTcpConnectAttempts_Object = MibTableColumn
copsClientTcpConnectAttempts = _CopsClientTcpConnectAttempts_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 15),
    _CopsClientTcpConnectAttempts_Type()
)
copsClientTcpConnectAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientTcpConnectAttempts.setStatus("current")
_CopsClientTcpConnectFailures_Type = Counter32
_CopsClientTcpConnectFailures_Object = MibTableColumn
copsClientTcpConnectFailures = _CopsClientTcpConnectFailures_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 16),
    _CopsClientTcpConnectFailures_Type()
)
copsClientTcpConnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientTcpConnectFailures.setStatus("current")
_CopsClientOpenAttempts_Type = Counter32
_CopsClientOpenAttempts_Object = MibTableColumn
copsClientOpenAttempts = _CopsClientOpenAttempts_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 17),
    _CopsClientOpenAttempts_Type()
)
copsClientOpenAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientOpenAttempts.setStatus("current")
_CopsClientOpenFailures_Type = Counter32
_CopsClientOpenFailures_Object = MibTableColumn
copsClientOpenFailures = _CopsClientOpenFailures_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 18),
    _CopsClientOpenFailures_Type()
)
copsClientOpenFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientOpenFailures.setStatus("current")
_CopsClientErrUnsupportClienttype_Type = Counter32
_CopsClientErrUnsupportClienttype_Object = MibTableColumn
copsClientErrUnsupportClienttype = _CopsClientErrUnsupportClienttype_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 19),
    _CopsClientErrUnsupportClienttype_Type()
)
copsClientErrUnsupportClienttype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrUnsupportClienttype.setStatus("current")
_CopsClientErrUnsupportedVersion_Type = Counter32
_CopsClientErrUnsupportedVersion_Object = MibTableColumn
copsClientErrUnsupportedVersion = _CopsClientErrUnsupportedVersion_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 20),
    _CopsClientErrUnsupportedVersion_Type()
)
copsClientErrUnsupportedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrUnsupportedVersion.setStatus("current")
_CopsClientErrLengthMismatch_Type = Counter32
_CopsClientErrLengthMismatch_Object = MibTableColumn
copsClientErrLengthMismatch = _CopsClientErrLengthMismatch_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 21),
    _CopsClientErrLengthMismatch_Type()
)
copsClientErrLengthMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrLengthMismatch.setStatus("current")
_CopsClientErrUnknownOpcode_Type = Counter32
_CopsClientErrUnknownOpcode_Object = MibTableColumn
copsClientErrUnknownOpcode = _CopsClientErrUnknownOpcode_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 22),
    _CopsClientErrUnknownOpcode_Type()
)
copsClientErrUnknownOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrUnknownOpcode.setStatus("current")
_CopsClientErrUnknownCnum_Type = Counter32
_CopsClientErrUnknownCnum_Object = MibTableColumn
copsClientErrUnknownCnum = _CopsClientErrUnknownCnum_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 23),
    _CopsClientErrUnknownCnum_Type()
)
copsClientErrUnknownCnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrUnknownCnum.setStatus("current")
_CopsClientErrBadCtype_Type = Counter32
_CopsClientErrBadCtype_Object = MibTableColumn
copsClientErrBadCtype = _CopsClientErrBadCtype_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 24),
    _CopsClientErrBadCtype_Type()
)
copsClientErrBadCtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrBadCtype.setStatus("current")
_CopsClientErrBadSends_Type = Counter32
_CopsClientErrBadSends_Object = MibTableColumn
copsClientErrBadSends = _CopsClientErrBadSends_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 25),
    _CopsClientErrBadSends_Type()
)
copsClientErrBadSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrBadSends.setStatus("current")
_CopsClientErrWrongObjects_Type = Counter32
_CopsClientErrWrongObjects_Object = MibTableColumn
copsClientErrWrongObjects = _CopsClientErrWrongObjects_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 26),
    _CopsClientErrWrongObjects_Type()
)
copsClientErrWrongObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrWrongObjects.setStatus("current")
_CopsClientErrWrongOpcode_Type = Counter32
_CopsClientErrWrongOpcode_Object = MibTableColumn
copsClientErrWrongOpcode = _CopsClientErrWrongOpcode_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 27),
    _CopsClientErrWrongOpcode_Type()
)
copsClientErrWrongOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrWrongOpcode.setStatus("current")
_CopsClientKaTimedoutClients_Type = Counter32
_CopsClientKaTimedoutClients_Object = MibTableColumn
copsClientKaTimedoutClients = _CopsClientKaTimedoutClients_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 28),
    _CopsClientKaTimedoutClients_Type()
)
copsClientKaTimedoutClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientKaTimedoutClients.setStatus("current")
_CopsClientErrAuthFailures_Type = Counter32
_CopsClientErrAuthFailures_Object = MibTableColumn
copsClientErrAuthFailures = _CopsClientErrAuthFailures_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 29),
    _CopsClientErrAuthFailures_Type()
)
copsClientErrAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrAuthFailures.setStatus("current")
_CopsClientErrAuthMissing_Type = Counter32
_CopsClientErrAuthMissing_Object = MibTableColumn
copsClientErrAuthMissing = _CopsClientErrAuthMissing_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 30),
    _CopsClientErrAuthMissing_Type()
)
copsClientErrAuthMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copsClientErrAuthMissing.setStatus("current")
_CopsClientConfigGroup_ObjectIdentity = ObjectIdentity
copsClientConfigGroup = _CopsClientConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 1, 3)
)
_CopsClientServerConfigTable_Object = MibTable
copsClientServerConfigTable = _CopsClientServerConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1)
)
if mibBuilder.loadTexts:
    copsClientServerConfigTable.setStatus("current")
_CopsClientServerConfigEntry_Object = MibTableRow
copsClientServerConfigEntry = _CopsClientServerConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1)
)
copsClientServerConfigEntry.setIndexNames(
    (0, "COPS-CLIENT-MIB", "copsClientServerConfigAddrType"),
    (0, "COPS-CLIENT-MIB", "copsClientServerConfigAddress"),
    (0, "COPS-CLIENT-MIB", "copsClientServerConfigClientType"),
    (0, "COPS-CLIENT-MIB", "copsClientServerConfigAuthType"),
)
if mibBuilder.loadTexts:
    copsClientServerConfigEntry.setStatus("current")
_CopsClientServerConfigAddrType_Type = InetAddressType
_CopsClientServerConfigAddrType_Object = MibTableColumn
copsClientServerConfigAddrType = _CopsClientServerConfigAddrType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 1),
    _CopsClientServerConfigAddrType_Type()
)
copsClientServerConfigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerConfigAddrType.setStatus("current")
_CopsClientServerConfigAddress_Type = InetAddress
_CopsClientServerConfigAddress_Object = MibTableColumn
copsClientServerConfigAddress = _CopsClientServerConfigAddress_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 2),
    _CopsClientServerConfigAddress_Type()
)
copsClientServerConfigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerConfigAddress.setStatus("current")


class _CopsClientServerConfigClientType_Type(Integer32):
    """Custom type copsClientServerConfigClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CopsClientServerConfigClientType_Type.__name__ = "Integer32"
_CopsClientServerConfigClientType_Object = MibTableColumn
copsClientServerConfigClientType = _CopsClientServerConfigClientType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 3),
    _CopsClientServerConfigClientType_Type()
)
copsClientServerConfigClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerConfigClientType.setStatus("current")
_CopsClientServerConfigAuthType_Type = CopsAuthType
_CopsClientServerConfigAuthType_Object = MibTableColumn
copsClientServerConfigAuthType = _CopsClientServerConfigAuthType_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 4),
    _CopsClientServerConfigAuthType_Type()
)
copsClientServerConfigAuthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copsClientServerConfigAuthType.setStatus("current")
_CopsClientServerConfigTcpPort_Type = CopsTcpPort
_CopsClientServerConfigTcpPort_Object = MibTableColumn
copsClientServerConfigTcpPort = _CopsClientServerConfigTcpPort_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 5),
    _CopsClientServerConfigTcpPort_Type()
)
copsClientServerConfigTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copsClientServerConfigTcpPort.setStatus("current")
_CopsClientServerConfigPriority_Type = Integer32
_CopsClientServerConfigPriority_Object = MibTableColumn
copsClientServerConfigPriority = _CopsClientServerConfigPriority_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 6),
    _CopsClientServerConfigPriority_Type()
)
copsClientServerConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copsClientServerConfigPriority.setStatus("current")
_CopsClientServerConfigRowStatus_Type = RowStatus
_CopsClientServerConfigRowStatus_Object = MibTableColumn
copsClientServerConfigRowStatus = _CopsClientServerConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 7),
    _CopsClientServerConfigRowStatus_Type()
)
copsClientServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copsClientServerConfigRowStatus.setStatus("current")


class _CopsClientServerConfigRetryAlgrm_Type(Integer32):
    """Custom type copsClientServerConfigRetryAlgrm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("roundRobin", 3),
          ("sequential", 2))
    )


_CopsClientServerConfigRetryAlgrm_Type.__name__ = "Integer32"
_CopsClientServerConfigRetryAlgrm_Object = MibScalar
copsClientServerConfigRetryAlgrm = _CopsClientServerConfigRetryAlgrm_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 2),
    _CopsClientServerConfigRetryAlgrm_Type()
)
copsClientServerConfigRetryAlgrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copsClientServerConfigRetryAlgrm.setStatus("current")


class _CopsClientServerConfigRetryCount_Type(Unsigned32):
    """Custom type copsClientServerConfigRetryCount based on Unsigned32"""
    defaultValue = 1


_CopsClientServerConfigRetryCount_Object = MibScalar
copsClientServerConfigRetryCount = _CopsClientServerConfigRetryCount_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 3),
    _CopsClientServerConfigRetryCount_Type()
)
copsClientServerConfigRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copsClientServerConfigRetryCount.setStatus("current")


class _CopsClientServerConfigRetryIntvl_Type(TimeInterval):
    """Custom type copsClientServerConfigRetryIntvl based on TimeInterval"""
    defaultValue = 1000


_CopsClientServerConfigRetryIntvl_Object = MibScalar
copsClientServerConfigRetryIntvl = _CopsClientServerConfigRetryIntvl_Object(
    (1, 3, 6, 1, 2, 1, 89, 1, 3, 4),
    _CopsClientServerConfigRetryIntvl_Type()
)
copsClientServerConfigRetryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copsClientServerConfigRetryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    copsClientServerConfigRetryIntvl.setUnits("centi-seconds")
_CopsClientConformance_ObjectIdentity = ObjectIdentity
copsClientConformance = _CopsClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 2)
)
_CopsClientGroups_ObjectIdentity = ObjectIdentity
copsClientGroups = _CopsClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 2, 1)
)
_CopsClientCompliances_ObjectIdentity = ObjectIdentity
copsClientCompliances = _CopsClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 89, 2, 2)
)

# Managed Objects groups

copsDeviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 89, 2, 1, 1)
)
copsDeviceStatusGroup.setObjects(
      *(("COPS-CLIENT-MIB", "copsClientCapabilities"),
        ("COPS-CLIENT-MIB", "copsClientServerTcpPort"),
        ("COPS-CLIENT-MIB", "copsClientServerType"),
        ("COPS-CLIENT-MIB", "copsClientServerAuthType"),
        ("COPS-CLIENT-MIB", "copsClientServerLastConnAttempt"),
        ("COPS-CLIENT-MIB", "copsClientState"),
        ("COPS-CLIENT-MIB", "copsClientServerKeepaliveTime"),
        ("COPS-CLIENT-MIB", "copsClientServerAccountingTime"),
        ("COPS-CLIENT-MIB", "copsClientInPkts"),
        ("COPS-CLIENT-MIB", "copsClientOutPkts"),
        ("COPS-CLIENT-MIB", "copsClientInErrs"),
        ("COPS-CLIENT-MIB", "copsClientLastError"),
        ("COPS-CLIENT-MIB", "copsClientTcpConnectAttempts"),
        ("COPS-CLIENT-MIB", "copsClientTcpConnectFailures"),
        ("COPS-CLIENT-MIB", "copsClientOpenAttempts"),
        ("COPS-CLIENT-MIB", "copsClientOpenFailures"),
        ("COPS-CLIENT-MIB", "copsClientErrUnsupportClienttype"),
        ("COPS-CLIENT-MIB", "copsClientErrUnsupportedVersion"),
        ("COPS-CLIENT-MIB", "copsClientErrLengthMismatch"),
        ("COPS-CLIENT-MIB", "copsClientErrUnknownOpcode"),
        ("COPS-CLIENT-MIB", "copsClientErrUnknownCnum"),
        ("COPS-CLIENT-MIB", "copsClientErrBadCtype"),
        ("COPS-CLIENT-MIB", "copsClientErrBadSends"),
        ("COPS-CLIENT-MIB", "copsClientErrWrongObjects"),
        ("COPS-CLIENT-MIB", "copsClientErrWrongOpcode"),
        ("COPS-CLIENT-MIB", "copsClientKaTimedoutClients"),
        ("COPS-CLIENT-MIB", "copsClientErrAuthFailures"),
        ("COPS-CLIENT-MIB", "copsClientErrAuthMissing"))
)
if mibBuilder.loadTexts:
    copsDeviceStatusGroup.setStatus("current")

copsDeviceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 89, 2, 1, 2)
)
copsDeviceConfigGroup.setObjects(
      *(("COPS-CLIENT-MIB", "copsClientServerConfigTcpPort"),
        ("COPS-CLIENT-MIB", "copsClientServerConfigPriority"),
        ("COPS-CLIENT-MIB", "copsClientServerConfigRowStatus"),
        ("COPS-CLIENT-MIB", "copsClientServerConfigRetryAlgrm"),
        ("COPS-CLIENT-MIB", "copsClientServerConfigRetryCount"),
        ("COPS-CLIENT-MIB", "copsClientServerConfigRetryIntvl"))
)
if mibBuilder.loadTexts:
    copsDeviceConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

copsClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 89, 2, 2, 1)
)
if mibBuilder.loadTexts:
    copsClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COPS-CLIENT-MIB",
    **{"CopsClientState": CopsClientState,
       "CopsServerEntryType": CopsServerEntryType,
       "CopsErrorCode": CopsErrorCode,
       "CopsTcpPort": CopsTcpPort,
       "CopsAuthType": CopsAuthType,
       "copsClientMIB": copsClientMIB,
       "copsClientMIBObjects": copsClientMIBObjects,
       "copsClientCapabilitiesGroup": copsClientCapabilitiesGroup,
       "copsClientCapabilities": copsClientCapabilities,
       "copsClientStatusGroup": copsClientStatusGroup,
       "copsClientServerCurrentTable": copsClientServerCurrentTable,
       "copsClientServerCurrentEntry": copsClientServerCurrentEntry,
       "copsClientServerAddressType": copsClientServerAddressType,
       "copsClientServerAddress": copsClientServerAddress,
       "copsClientServerClientType": copsClientServerClientType,
       "copsClientServerTcpPort": copsClientServerTcpPort,
       "copsClientServerType": copsClientServerType,
       "copsClientServerAuthType": copsClientServerAuthType,
       "copsClientServerLastConnAttempt": copsClientServerLastConnAttempt,
       "copsClientState": copsClientState,
       "copsClientServerKeepaliveTime": copsClientServerKeepaliveTime,
       "copsClientServerAccountingTime": copsClientServerAccountingTime,
       "copsClientInPkts": copsClientInPkts,
       "copsClientOutPkts": copsClientOutPkts,
       "copsClientInErrs": copsClientInErrs,
       "copsClientLastError": copsClientLastError,
       "copsClientTcpConnectAttempts": copsClientTcpConnectAttempts,
       "copsClientTcpConnectFailures": copsClientTcpConnectFailures,
       "copsClientOpenAttempts": copsClientOpenAttempts,
       "copsClientOpenFailures": copsClientOpenFailures,
       "copsClientErrUnsupportClienttype": copsClientErrUnsupportClienttype,
       "copsClientErrUnsupportedVersion": copsClientErrUnsupportedVersion,
       "copsClientErrLengthMismatch": copsClientErrLengthMismatch,
       "copsClientErrUnknownOpcode": copsClientErrUnknownOpcode,
       "copsClientErrUnknownCnum": copsClientErrUnknownCnum,
       "copsClientErrBadCtype": copsClientErrBadCtype,
       "copsClientErrBadSends": copsClientErrBadSends,
       "copsClientErrWrongObjects": copsClientErrWrongObjects,
       "copsClientErrWrongOpcode": copsClientErrWrongOpcode,
       "copsClientKaTimedoutClients": copsClientKaTimedoutClients,
       "copsClientErrAuthFailures": copsClientErrAuthFailures,
       "copsClientErrAuthMissing": copsClientErrAuthMissing,
       "copsClientConfigGroup": copsClientConfigGroup,
       "copsClientServerConfigTable": copsClientServerConfigTable,
       "copsClientServerConfigEntry": copsClientServerConfigEntry,
       "copsClientServerConfigAddrType": copsClientServerConfigAddrType,
       "copsClientServerConfigAddress": copsClientServerConfigAddress,
       "copsClientServerConfigClientType": copsClientServerConfigClientType,
       "copsClientServerConfigAuthType": copsClientServerConfigAuthType,
       "copsClientServerConfigTcpPort": copsClientServerConfigTcpPort,
       "copsClientServerConfigPriority": copsClientServerConfigPriority,
       "copsClientServerConfigRowStatus": copsClientServerConfigRowStatus,
       "copsClientServerConfigRetryAlgrm": copsClientServerConfigRetryAlgrm,
       "copsClientServerConfigRetryCount": copsClientServerConfigRetryCount,
       "copsClientServerConfigRetryIntvl": copsClientServerConfigRetryIntvl,
       "copsClientConformance": copsClientConformance,
       "copsClientGroups": copsClientGroups,
       "copsDeviceStatusGroup": copsDeviceStatusGroup,
       "copsDeviceConfigGroup": copsDeviceConfigGroup,
       "copsClientCompliances": copsClientCompliances,
       "copsClientCompliance": copsClientCompliance}
)
