# SNMP MIB module (WWP-LEOS-TACACS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-TACACS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:13 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosTacacsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402)
)
wwpLeosTacacsClientMIB.setRevisions(
        ("2012-04-05 00:00",
         "2011-08-04 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TacacsString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 127),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosTacacsClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClientMIBObjects = _WwpLeosTacacsClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1)
)
_WwpLeosTacacsClient_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClient = _WwpLeosTacacsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1)
)


class _WwpLeosTacacsAdminState_Type(Integer32):
    """Custom type wwpLeosTacacsAdminState based on Integer32"""
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


_WwpLeosTacacsAdminState_Type.__name__ = "Integer32"
_WwpLeosTacacsAdminState_Object = MibScalar
wwpLeosTacacsAdminState = _WwpLeosTacacsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 1),
    _WwpLeosTacacsAdminState_Type()
)
wwpLeosTacacsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsAdminState.setStatus("current")


class _WwpLeosTacacsOperState_Type(Integer32):
    """Custom type wwpLeosTacacsOperState based on Integer32"""
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


_WwpLeosTacacsOperState_Type.__name__ = "Integer32"
_WwpLeosTacacsOperState_Object = MibScalar
wwpLeosTacacsOperState = _WwpLeosTacacsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 2),
    _WwpLeosTacacsOperState_Type()
)
wwpLeosTacacsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsOperState.setStatus("current")


class _WwpLeosTacacsClientTimeout_Type(Integer32):
    """Custom type wwpLeosTacacsClientTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosTacacsClientTimeout_Type.__name__ = "Integer32"
_WwpLeosTacacsClientTimeout_Object = MibScalar
wwpLeosTacacsClientTimeout = _WwpLeosTacacsClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 3),
    _WwpLeosTacacsClientTimeout_Type()
)
wwpLeosTacacsClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientTimeout.setUnits("seconds")


class _WwpLeosTacacsClientRetries_Type(Integer32):
    """Custom type wwpLeosTacacsClientRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosTacacsClientRetries_Type.__name__ = "Integer32"
_WwpLeosTacacsClientRetries_Object = MibScalar
wwpLeosTacacsClientRetries = _WwpLeosTacacsClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 4),
    _WwpLeosTacacsClientRetries_Type()
)
wwpLeosTacacsClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientRetries.setStatus("deprecated")


class _WwpLeosTacacsClientPrivilegeLevelRW_Type(Integer32):
    """Custom type wwpLeosTacacsClientPrivilegeLevelRW based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 14),
    )


_WwpLeosTacacsClientPrivilegeLevelRW_Type.__name__ = "Integer32"
_WwpLeosTacacsClientPrivilegeLevelRW_Object = MibScalar
wwpLeosTacacsClientPrivilegeLevelRW = _WwpLeosTacacsClientPrivilegeLevelRW_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 5),
    _WwpLeosTacacsClientPrivilegeLevelRW_Type()
)
wwpLeosTacacsClientPrivilegeLevelRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientPrivilegeLevelRW.setStatus("current")


class _WwpLeosTacacsClientPrivilegeLevelAdmin_Type(Integer32):
    """Custom type wwpLeosTacacsClientPrivilegeLevelAdmin based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 13),
    )


_WwpLeosTacacsClientPrivilegeLevelAdmin_Type.__name__ = "Integer32"
_WwpLeosTacacsClientPrivilegeLevelAdmin_Object = MibScalar
wwpLeosTacacsClientPrivilegeLevelAdmin = _WwpLeosTacacsClientPrivilegeLevelAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 6),
    _WwpLeosTacacsClientPrivilegeLevelAdmin_Type()
)
wwpLeosTacacsClientPrivilegeLevelAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientPrivilegeLevelAdmin.setStatus("current")


class _WwpLeosTacacsClientPrivilegeLevelDiag_Type(Integer32):
    """Custom type wwpLeosTacacsClientPrivilegeLevelDiag based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_WwpLeosTacacsClientPrivilegeLevelDiag_Type.__name__ = "Integer32"
_WwpLeosTacacsClientPrivilegeLevelDiag_Object = MibScalar
wwpLeosTacacsClientPrivilegeLevelDiag = _WwpLeosTacacsClientPrivilegeLevelDiag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 7),
    _WwpLeosTacacsClientPrivilegeLevelDiag_Type()
)
wwpLeosTacacsClientPrivilegeLevelDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientPrivilegeLevelDiag.setStatus("current")
_WwpLeosTacacsClientAuthKey_Type = TacacsString
_WwpLeosTacacsClientAuthKey_Object = MibScalar
wwpLeosTacacsClientAuthKey = _WwpLeosTacacsClientAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 8),
    _WwpLeosTacacsClientAuthKey_Type()
)
wwpLeosTacacsClientAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthKey.setStatus("current")


class _WwpLeosTacacsAuthenticationAdminState_Type(Integer32):
    """Custom type wwpLeosTacacsAuthenticationAdminState based on Integer32"""
    defaultValue = 2

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


_WwpLeosTacacsAuthenticationAdminState_Type.__name__ = "Integer32"
_WwpLeosTacacsAuthenticationAdminState_Object = MibScalar
wwpLeosTacacsAuthenticationAdminState = _WwpLeosTacacsAuthenticationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 9),
    _WwpLeosTacacsAuthenticationAdminState_Type()
)
wwpLeosTacacsAuthenticationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsAuthenticationAdminState.setStatus("current")


class _WwpLeosTacacsAuthorizationAdminState_Type(Integer32):
    """Custom type wwpLeosTacacsAuthorizationAdminState based on Integer32"""
    defaultValue = 1

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


_WwpLeosTacacsAuthorizationAdminState_Type.__name__ = "Integer32"
_WwpLeosTacacsAuthorizationAdminState_Object = MibScalar
wwpLeosTacacsAuthorizationAdminState = _WwpLeosTacacsAuthorizationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 10),
    _WwpLeosTacacsAuthorizationAdminState_Type()
)
wwpLeosTacacsAuthorizationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsAuthorizationAdminState.setStatus("current")


class _WwpLeosTacacsAccountingAdminState_Type(Integer32):
    """Custom type wwpLeosTacacsAccountingAdminState based on Integer32"""
    defaultValue = 1

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


_WwpLeosTacacsAccountingAdminState_Type.__name__ = "Integer32"
_WwpLeosTacacsAccountingAdminState_Object = MibScalar
wwpLeosTacacsAccountingAdminState = _WwpLeosTacacsAccountingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 11),
    _WwpLeosTacacsAccountingAdminState_Type()
)
wwpLeosTacacsAccountingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsAccountingAdminState.setStatus("current")


class _WwpLeosTacacsSyslogAdminState_Type(Integer32):
    """Custom type wwpLeosTacacsSyslogAdminState based on Integer32"""
    defaultValue = 1

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


_WwpLeosTacacsSyslogAdminState_Type.__name__ = "Integer32"
_WwpLeosTacacsSyslogAdminState_Object = MibScalar
wwpLeosTacacsSyslogAdminState = _WwpLeosTacacsSyslogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 12),
    _WwpLeosTacacsSyslogAdminState_Type()
)
wwpLeosTacacsSyslogAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsSyslogAdminState.setStatus("current")
_WwpLeosTacacsClientServerTable_Object = MibTable
wwpLeosTacacsClientServerTable = _WwpLeosTacacsClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13)
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerTable.setStatus("current")
_WwpLeosTacacsClientServerEntry_Object = MibTableRow
wwpLeosTacacsClientServerEntry = _WwpLeosTacacsClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1)
)
wwpLeosTacacsClientServerEntry.setIndexNames(
    (0, "WWP-LEOS-TACACS-CLIENT-MIB", "wwpLeosTacacsClientServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerEntry.setStatus("current")


class _WwpLeosTacacsClientServerIndex_Type(Integer32):
    """Custom type wwpLeosTacacsClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosTacacsClientServerIndex_Type.__name__ = "Integer32"
_WwpLeosTacacsClientServerIndex_Object = MibTableColumn
wwpLeosTacacsClientServerIndex = _WwpLeosTacacsClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 1),
    _WwpLeosTacacsClientServerIndex_Type()
)
wwpLeosTacacsClientServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerIndex.setStatus("current")


class _WwpLeosTacacsClientServerAddr_Type(DisplayString):
    """Custom type wwpLeosTacacsClientServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosTacacsClientServerAddr_Type.__name__ = "DisplayString"
_WwpLeosTacacsClientServerAddr_Object = MibTableColumn
wwpLeosTacacsClientServerAddr = _WwpLeosTacacsClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 2),
    _WwpLeosTacacsClientServerAddr_Type()
)
wwpLeosTacacsClientServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerAddr.setStatus("current")
_WwpLeosTacacsClientServerResolvedAddr_Type = IpAddress
_WwpLeosTacacsClientServerResolvedAddr_Object = MibTableColumn
wwpLeosTacacsClientServerResolvedAddr = _WwpLeosTacacsClientServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 3),
    _WwpLeosTacacsClientServerResolvedAddr_Type()
)
wwpLeosTacacsClientServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerResolvedAddr.setStatus("current")
_WwpLeosTacacsClientServerPriority_Type = Integer32
_WwpLeosTacacsClientServerPriority_Object = MibTableColumn
wwpLeosTacacsClientServerPriority = _WwpLeosTacacsClientServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 4),
    _WwpLeosTacacsClientServerPriority_Type()
)
wwpLeosTacacsClientServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerPriority.setStatus("current")


class _WwpLeosTacacsClientServerAuthPort_Type(Integer32):
    """Custom type wwpLeosTacacsClientServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTacacsClientServerAuthPort_Type.__name__ = "Integer32"
_WwpLeosTacacsClientServerAuthPort_Object = MibTableColumn
wwpLeosTacacsClientServerAuthPort = _WwpLeosTacacsClientServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 5),
    _WwpLeosTacacsClientServerAuthPort_Type()
)
wwpLeosTacacsClientServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerAuthPort.setStatus("current")
_WwpLeosTacacsClientServerAccessRequests_Type = Counter32
_WwpLeosTacacsClientServerAccessRequests_Object = MibTableColumn
wwpLeosTacacsClientServerAccessRequests = _WwpLeosTacacsClientServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 6),
    _WwpLeosTacacsClientServerAccessRequests_Type()
)
wwpLeosTacacsClientServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerAccessRequests.setStatus("current")
_WwpLeosTacacsClientServerAccessRetransmissions_Type = Counter32
_WwpLeosTacacsClientServerAccessRetransmissions_Object = MibTableColumn
wwpLeosTacacsClientServerAccessRetransmissions = _WwpLeosTacacsClientServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 7),
    _WwpLeosTacacsClientServerAccessRetransmissions_Type()
)
wwpLeosTacacsClientServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerAccessRetransmissions.setStatus("current")
_WwpLeosTacacsClientServerAccessAccepts_Type = Counter32
_WwpLeosTacacsClientServerAccessAccepts_Object = MibTableColumn
wwpLeosTacacsClientServerAccessAccepts = _WwpLeosTacacsClientServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 8),
    _WwpLeosTacacsClientServerAccessAccepts_Type()
)
wwpLeosTacacsClientServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerAccessAccepts.setStatus("current")
_WwpLeosTacacsClientServerAccessRejects_Type = Counter32
_WwpLeosTacacsClientServerAccessRejects_Object = MibTableColumn
wwpLeosTacacsClientServerAccessRejects = _WwpLeosTacacsClientServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 9),
    _WwpLeosTacacsClientServerAccessRejects_Type()
)
wwpLeosTacacsClientServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerAccessRejects.setStatus("current")
_WwpLeosTacacsClientServerMalformedAccessResponses_Type = Counter32
_WwpLeosTacacsClientServerMalformedAccessResponses_Object = MibTableColumn
wwpLeosTacacsClientServerMalformedAccessResponses = _WwpLeosTacacsClientServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 10),
    _WwpLeosTacacsClientServerMalformedAccessResponses_Type()
)
wwpLeosTacacsClientServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerMalformedAccessResponses.setStatus("current")
_WwpLeosTacacsClientServerBadAuthenticators_Type = Counter32
_WwpLeosTacacsClientServerBadAuthenticators_Object = MibTableColumn
wwpLeosTacacsClientServerBadAuthenticators = _WwpLeosTacacsClientServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 11),
    _WwpLeosTacacsClientServerBadAuthenticators_Type()
)
wwpLeosTacacsClientServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerBadAuthenticators.setStatus("current")
_WwpLeosTacacsClientServerPendingRequests_Type = Gauge32
_WwpLeosTacacsClientServerPendingRequests_Object = MibTableColumn
wwpLeosTacacsClientServerPendingRequests = _WwpLeosTacacsClientServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 12),
    _WwpLeosTacacsClientServerPendingRequests_Type()
)
wwpLeosTacacsClientServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerPendingRequests.setStatus("deprecated")
_WwpLeosTacacsClientServerTimeouts_Type = Counter32
_WwpLeosTacacsClientServerTimeouts_Object = MibTableColumn
wwpLeosTacacsClientServerTimeouts = _WwpLeosTacacsClientServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 13),
    _WwpLeosTacacsClientServerTimeouts_Type()
)
wwpLeosTacacsClientServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerTimeouts.setStatus("current")
_WwpLeosTacacsClientServerUnknownTypes_Type = Counter32
_WwpLeosTacacsClientServerUnknownTypes_Object = MibTableColumn
wwpLeosTacacsClientServerUnknownTypes = _WwpLeosTacacsClientServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 14),
    _WwpLeosTacacsClientServerUnknownTypes_Type()
)
wwpLeosTacacsClientServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerUnknownTypes.setStatus("current")
_WwpLeosTacacsClientServerBadHeaderSequence_Type = Counter32
_WwpLeosTacacsClientServerBadHeaderSequence_Object = MibTableColumn
wwpLeosTacacsClientServerBadHeaderSequence = _WwpLeosTacacsClientServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 15),
    _WwpLeosTacacsClientServerBadHeaderSequence_Type()
)
wwpLeosTacacsClientServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerBadHeaderSequence.setStatus("current")
_WwpLeosTacacsClientServerStatus_Type = RowStatus
_WwpLeosTacacsClientServerStatus_Object = MibTableColumn
wwpLeosTacacsClientServerStatus = _WwpLeosTacacsClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 16),
    _WwpLeosTacacsClientServerStatus_Type()
)
wwpLeosTacacsClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerStatus.setStatus("current")


class _WwpLeosTacacsClientServerApplication_Type(Integer32):
    """Custom type wwpLeosTacacsClientServerApplication based on Integer32"""
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
        *(("all", 3),
          ("dot1x", 2),
          ("userLogin", 1))
    )


_WwpLeosTacacsClientServerApplication_Type.__name__ = "Integer32"
_WwpLeosTacacsClientServerApplication_Object = MibTableColumn
wwpLeosTacacsClientServerApplication = _WwpLeosTacacsClientServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 17),
    _WwpLeosTacacsClientServerApplication_Type()
)
wwpLeosTacacsClientServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerApplication.setStatus("current")


class _WwpLeosTacacsClientServerClearStatistics_Type(TruthValue):
    """Custom type wwpLeosTacacsClientServerClearStatistics based on TruthValue"""


_WwpLeosTacacsClientServerClearStatistics_Object = MibTableColumn
wwpLeosTacacsClientServerClearStatistics = _WwpLeosTacacsClientServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 18),
    _WwpLeosTacacsClientServerClearStatistics_Type()
)
wwpLeosTacacsClientServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerClearStatistics.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationAccessRequests_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationAccessRequests_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationAccessRequests = _WwpLeosTacacsClientGlobalAuthorizationAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 19),
    _WwpLeosTacacsClientGlobalAuthorizationAccessRequests_Type()
)
wwpLeosTacacsClientGlobalAuthorizationAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationAccessRequests.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions = _WwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 20),
    _WwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions_Type()
)
wwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationAccessAccepts_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationAccessAccepts_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationAccessAccepts = _WwpLeosTacacsClientGlobalAuthorizationAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 21),
    _WwpLeosTacacsClientGlobalAuthorizationAccessAccepts_Type()
)
wwpLeosTacacsClientGlobalAuthorizationAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationAccessAccepts.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationAccessRejects_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationAccessRejects_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationAccessRejects = _WwpLeosTacacsClientGlobalAuthorizationAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 22),
    _WwpLeosTacacsClientGlobalAuthorizationAccessRejects_Type()
)
wwpLeosTacacsClientGlobalAuthorizationAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationAccessRejects.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses = _WwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 23),
    _WwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses_Type()
)
wwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationBadAuthenticators_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationBadAuthenticators_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationBadAuthenticators = _WwpLeosTacacsClientGlobalAuthorizationBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 24),
    _WwpLeosTacacsClientGlobalAuthorizationBadAuthenticators_Type()
)
wwpLeosTacacsClientGlobalAuthorizationBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationBadAuthenticators.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationTimeouts_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationTimeouts_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationTimeouts = _WwpLeosTacacsClientGlobalAuthorizationTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 25),
    _WwpLeosTacacsClientGlobalAuthorizationTimeouts_Type()
)
wwpLeosTacacsClientGlobalAuthorizationTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationTimeouts.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationUnknownTypes_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationUnknownTypes_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationUnknownTypes = _WwpLeosTacacsClientGlobalAuthorizationUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 26),
    _WwpLeosTacacsClientGlobalAuthorizationUnknownTypes_Type()
)
wwpLeosTacacsClientGlobalAuthorizationUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationUnknownTypes.setStatus("current")
_WwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence_Type = Counter32
_WwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence_Object = MibTableColumn
wwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence = _WwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 27),
    _WwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence_Type()
)
wwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingAccessRequests_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingAccessRequests_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingAccessRequests = _WwpLeosTacacsClientGlobalAccountingAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 28),
    _WwpLeosTacacsClientGlobalAccountingAccessRequests_Type()
)
wwpLeosTacacsClientGlobalAccountingAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingAccessRequests.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingAccessRetransmissions_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingAccessRetransmissions_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingAccessRetransmissions = _WwpLeosTacacsClientGlobalAccountingAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 29),
    _WwpLeosTacacsClientGlobalAccountingAccessRetransmissions_Type()
)
wwpLeosTacacsClientGlobalAccountingAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingAccessRetransmissions.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingAccessAccepts_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingAccessAccepts_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingAccessAccepts = _WwpLeosTacacsClientGlobalAccountingAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 30),
    _WwpLeosTacacsClientGlobalAccountingAccessAccepts_Type()
)
wwpLeosTacacsClientGlobalAccountingAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingAccessAccepts.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingAccessRejects_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingAccessRejects_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingAccessRejects = _WwpLeosTacacsClientGlobalAccountingAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 31),
    _WwpLeosTacacsClientGlobalAccountingAccessRejects_Type()
)
wwpLeosTacacsClientGlobalAccountingAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingAccessRejects.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingMalformedAccessResponses_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingMalformedAccessResponses_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingMalformedAccessResponses = _WwpLeosTacacsClientGlobalAccountingMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 32),
    _WwpLeosTacacsClientGlobalAccountingMalformedAccessResponses_Type()
)
wwpLeosTacacsClientGlobalAccountingMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingMalformedAccessResponses.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingBadAuthenticators_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingBadAuthenticators_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingBadAuthenticators = _WwpLeosTacacsClientGlobalAccountingBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 33),
    _WwpLeosTacacsClientGlobalAccountingBadAuthenticators_Type()
)
wwpLeosTacacsClientGlobalAccountingBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingBadAuthenticators.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingTimeouts_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingTimeouts_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingTimeouts = _WwpLeosTacacsClientGlobalAccountingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 34),
    _WwpLeosTacacsClientGlobalAccountingTimeouts_Type()
)
wwpLeosTacacsClientGlobalAccountingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingTimeouts.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingUnknownTypes_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingUnknownTypes_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingUnknownTypes = _WwpLeosTacacsClientGlobalAccountingUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 35),
    _WwpLeosTacacsClientGlobalAccountingUnknownTypes_Type()
)
wwpLeosTacacsClientGlobalAccountingUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingUnknownTypes.setStatus("current")
_WwpLeosTacacsClientGlobalAccountingBadHeaderSequence_Type = Counter32
_WwpLeosTacacsClientGlobalAccountingBadHeaderSequence_Object = MibTableColumn
wwpLeosTacacsClientGlobalAccountingBadHeaderSequence = _WwpLeosTacacsClientGlobalAccountingBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 36),
    _WwpLeosTacacsClientGlobalAccountingBadHeaderSequence_Type()
)
wwpLeosTacacsClientGlobalAccountingBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalAccountingBadHeaderSequence.setStatus("current")
_WwpLeosTacacsClientServerResolvedInetAddrType_Type = InetAddressType
_WwpLeosTacacsClientServerResolvedInetAddrType_Object = MibTableColumn
wwpLeosTacacsClientServerResolvedInetAddrType = _WwpLeosTacacsClientServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 37),
    _WwpLeosTacacsClientServerResolvedInetAddrType_Type()
)
wwpLeosTacacsClientServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerResolvedInetAddrType.setStatus("current")
_WwpLeosTacacsClientServerResolvedInetAddr_Type = InetAddress
_WwpLeosTacacsClientServerResolvedInetAddr_Object = MibTableColumn
wwpLeosTacacsClientServerResolvedInetAddr = _WwpLeosTacacsClientServerResolvedInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 13, 1, 38),
    _WwpLeosTacacsClientServerResolvedInetAddr_Type()
)
wwpLeosTacacsClientServerResolvedInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientServerResolvedInetAddr.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerTable_Object = MibTable
wwpLeosTacacsClientAuthenticationServerTable = _WwpLeosTacacsClientAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14)
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerTable.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerEntry_Object = MibTableRow
wwpLeosTacacsClientAuthenticationServerEntry = _WwpLeosTacacsClientAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1)
)
wwpLeosTacacsClientAuthenticationServerEntry.setIndexNames(
    (0, "WWP-LEOS-TACACS-CLIENT-MIB", "wwpLeosTacacsClientAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerEntry.setStatus("current")


class _WwpLeosTacacsClientAuthenticationServerIndex_Type(Integer32):
    """Custom type wwpLeosTacacsClientAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosTacacsClientAuthenticationServerIndex_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAuthenticationServerIndex_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerIndex = _WwpLeosTacacsClientAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 1),
    _WwpLeosTacacsClientAuthenticationServerIndex_Type()
)
wwpLeosTacacsClientAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerIndex.setStatus("current")


class _WwpLeosTacacsClientAuthenticationServerAddr_Type(DisplayString):
    """Custom type wwpLeosTacacsClientAuthenticationServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosTacacsClientAuthenticationServerAddr_Type.__name__ = "DisplayString"
_WwpLeosTacacsClientAuthenticationServerAddr_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerAddr = _WwpLeosTacacsClientAuthenticationServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 2),
    _WwpLeosTacacsClientAuthenticationServerAddr_Type()
)
wwpLeosTacacsClientAuthenticationServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerAddr.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerResolvedAddr_Type = IpAddress
_WwpLeosTacacsClientAuthenticationServerResolvedAddr_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerResolvedAddr = _WwpLeosTacacsClientAuthenticationServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 3),
    _WwpLeosTacacsClientAuthenticationServerResolvedAddr_Type()
)
wwpLeosTacacsClientAuthenticationServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerResolvedAddr.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerPriority_Type = Integer32
_WwpLeosTacacsClientAuthenticationServerPriority_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerPriority = _WwpLeosTacacsClientAuthenticationServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 4),
    _WwpLeosTacacsClientAuthenticationServerPriority_Type()
)
wwpLeosTacacsClientAuthenticationServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerPriority.setStatus("current")


class _WwpLeosTacacsClientAuthenticationServerAuthPort_Type(Integer32):
    """Custom type wwpLeosTacacsClientAuthenticationServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTacacsClientAuthenticationServerAuthPort_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAuthenticationServerAuthPort_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerAuthPort = _WwpLeosTacacsClientAuthenticationServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 5),
    _WwpLeosTacacsClientAuthenticationServerAuthPort_Type()
)
wwpLeosTacacsClientAuthenticationServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerAuthPort.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerAccessRequests_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerAccessRequests_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerAccessRequests = _WwpLeosTacacsClientAuthenticationServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 6),
    _WwpLeosTacacsClientAuthenticationServerAccessRequests_Type()
)
wwpLeosTacacsClientAuthenticationServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerAccessRequests.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerAccessRetransmissions_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerAccessRetransmissions_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerAccessRetransmissions = _WwpLeosTacacsClientAuthenticationServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 7),
    _WwpLeosTacacsClientAuthenticationServerAccessRetransmissions_Type()
)
wwpLeosTacacsClientAuthenticationServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerAccessRetransmissions.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerAccessAccepts_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerAccessAccepts_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerAccessAccepts = _WwpLeosTacacsClientAuthenticationServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 8),
    _WwpLeosTacacsClientAuthenticationServerAccessAccepts_Type()
)
wwpLeosTacacsClientAuthenticationServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerAccessAccepts.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerAccessRejects_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerAccessRejects_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerAccessRejects = _WwpLeosTacacsClientAuthenticationServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 9),
    _WwpLeosTacacsClientAuthenticationServerAccessRejects_Type()
)
wwpLeosTacacsClientAuthenticationServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerAccessRejects.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerMalformedAccessResponses_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerMalformedAccessResponses_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerMalformedAccessResponses = _WwpLeosTacacsClientAuthenticationServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 10),
    _WwpLeosTacacsClientAuthenticationServerMalformedAccessResponses_Type()
)
wwpLeosTacacsClientAuthenticationServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerMalformedAccessResponses.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerBadAuthenticators_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerBadAuthenticators_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerBadAuthenticators = _WwpLeosTacacsClientAuthenticationServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 11),
    _WwpLeosTacacsClientAuthenticationServerBadAuthenticators_Type()
)
wwpLeosTacacsClientAuthenticationServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerBadAuthenticators.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerPendingRequests_Type = Gauge32
_WwpLeosTacacsClientAuthenticationServerPendingRequests_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerPendingRequests = _WwpLeosTacacsClientAuthenticationServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 12),
    _WwpLeosTacacsClientAuthenticationServerPendingRequests_Type()
)
wwpLeosTacacsClientAuthenticationServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerPendingRequests.setStatus("deprecated")
_WwpLeosTacacsClientAuthenticationServerTimeouts_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerTimeouts_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerTimeouts = _WwpLeosTacacsClientAuthenticationServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 13),
    _WwpLeosTacacsClientAuthenticationServerTimeouts_Type()
)
wwpLeosTacacsClientAuthenticationServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerTimeouts.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerUnknownTypes_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerUnknownTypes_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerUnknownTypes = _WwpLeosTacacsClientAuthenticationServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 14),
    _WwpLeosTacacsClientAuthenticationServerUnknownTypes_Type()
)
wwpLeosTacacsClientAuthenticationServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerUnknownTypes.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerBadHeaderSequence_Type = Counter32
_WwpLeosTacacsClientAuthenticationServerBadHeaderSequence_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerBadHeaderSequence = _WwpLeosTacacsClientAuthenticationServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 15),
    _WwpLeosTacacsClientAuthenticationServerBadHeaderSequence_Type()
)
wwpLeosTacacsClientAuthenticationServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerBadHeaderSequence.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerStatus_Type = RowStatus
_WwpLeosTacacsClientAuthenticationServerStatus_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerStatus = _WwpLeosTacacsClientAuthenticationServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 16),
    _WwpLeosTacacsClientAuthenticationServerStatus_Type()
)
wwpLeosTacacsClientAuthenticationServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerStatus.setStatus("current")


class _WwpLeosTacacsClientAuthenticationServerApplication_Type(Integer32):
    """Custom type wwpLeosTacacsClientAuthenticationServerApplication based on Integer32"""
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
        *(("all", 3),
          ("dot1x", 2),
          ("userLogin", 1))
    )


_WwpLeosTacacsClientAuthenticationServerApplication_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAuthenticationServerApplication_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerApplication = _WwpLeosTacacsClientAuthenticationServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 17),
    _WwpLeosTacacsClientAuthenticationServerApplication_Type()
)
wwpLeosTacacsClientAuthenticationServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerApplication.setStatus("current")


class _WwpLeosTacacsClientAuthenticationServerClearStatistics_Type(TruthValue):
    """Custom type wwpLeosTacacsClientAuthenticationServerClearStatistics based on TruthValue"""


_WwpLeosTacacsClientAuthenticationServerClearStatistics_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerClearStatistics = _WwpLeosTacacsClientAuthenticationServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 18),
    _WwpLeosTacacsClientAuthenticationServerClearStatistics_Type()
)
wwpLeosTacacsClientAuthenticationServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerClearStatistics.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerResolvedInetAddrType_Type = InetAddressType
_WwpLeosTacacsClientAuthenticationServerResolvedInetAddrType_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerResolvedInetAddrType = _WwpLeosTacacsClientAuthenticationServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 19),
    _WwpLeosTacacsClientAuthenticationServerResolvedInetAddrType_Type()
)
wwpLeosTacacsClientAuthenticationServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerResolvedInetAddrType.setStatus("current")
_WwpLeosTacacsClientAuthenticationServerResolvedInetAddr_Type = InetAddress
_WwpLeosTacacsClientAuthenticationServerResolvedInetAddr_Object = MibTableColumn
wwpLeosTacacsClientAuthenticationServerResolvedInetAddr = _WwpLeosTacacsClientAuthenticationServerResolvedInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 14, 1, 20),
    _WwpLeosTacacsClientAuthenticationServerResolvedInetAddr_Type()
)
wwpLeosTacacsClientAuthenticationServerResolvedInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthenticationServerResolvedInetAddr.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerTable_Object = MibTable
wwpLeosTacacsClientAuthorizationServerTable = _WwpLeosTacacsClientAuthorizationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15)
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerTable.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerEntry_Object = MibTableRow
wwpLeosTacacsClientAuthorizationServerEntry = _WwpLeosTacacsClientAuthorizationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1)
)
wwpLeosTacacsClientAuthorizationServerEntry.setIndexNames(
    (0, "WWP-LEOS-TACACS-CLIENT-MIB", "wwpLeosTacacsClientAuthorizationServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerEntry.setStatus("current")


class _WwpLeosTacacsClientAuthorizationServerIndex_Type(Integer32):
    """Custom type wwpLeosTacacsClientAuthorizationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosTacacsClientAuthorizationServerIndex_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAuthorizationServerIndex_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerIndex = _WwpLeosTacacsClientAuthorizationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 1),
    _WwpLeosTacacsClientAuthorizationServerIndex_Type()
)
wwpLeosTacacsClientAuthorizationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerIndex.setStatus("current")


class _WwpLeosTacacsClientAuthorizationServerAddr_Type(DisplayString):
    """Custom type wwpLeosTacacsClientAuthorizationServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosTacacsClientAuthorizationServerAddr_Type.__name__ = "DisplayString"
_WwpLeosTacacsClientAuthorizationServerAddr_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerAddr = _WwpLeosTacacsClientAuthorizationServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 2),
    _WwpLeosTacacsClientAuthorizationServerAddr_Type()
)
wwpLeosTacacsClientAuthorizationServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerAddr.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerResolvedAddr_Type = IpAddress
_WwpLeosTacacsClientAuthorizationServerResolvedAddr_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerResolvedAddr = _WwpLeosTacacsClientAuthorizationServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 3),
    _WwpLeosTacacsClientAuthorizationServerResolvedAddr_Type()
)
wwpLeosTacacsClientAuthorizationServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerResolvedAddr.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerPriority_Type = Integer32
_WwpLeosTacacsClientAuthorizationServerPriority_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerPriority = _WwpLeosTacacsClientAuthorizationServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 4),
    _WwpLeosTacacsClientAuthorizationServerPriority_Type()
)
wwpLeosTacacsClientAuthorizationServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerPriority.setStatus("current")


class _WwpLeosTacacsClientAuthorizationServerAuthPort_Type(Integer32):
    """Custom type wwpLeosTacacsClientAuthorizationServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTacacsClientAuthorizationServerAuthPort_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAuthorizationServerAuthPort_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerAuthPort = _WwpLeosTacacsClientAuthorizationServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 5),
    _WwpLeosTacacsClientAuthorizationServerAuthPort_Type()
)
wwpLeosTacacsClientAuthorizationServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerAuthPort.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerAccessRequests_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerAccessRequests_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerAccessRequests = _WwpLeosTacacsClientAuthorizationServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 6),
    _WwpLeosTacacsClientAuthorizationServerAccessRequests_Type()
)
wwpLeosTacacsClientAuthorizationServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerAccessRequests.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerAccessRetransmissions_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerAccessRetransmissions_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerAccessRetransmissions = _WwpLeosTacacsClientAuthorizationServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 7),
    _WwpLeosTacacsClientAuthorizationServerAccessRetransmissions_Type()
)
wwpLeosTacacsClientAuthorizationServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerAccessRetransmissions.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerAccessAccepts_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerAccessAccepts_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerAccessAccepts = _WwpLeosTacacsClientAuthorizationServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 8),
    _WwpLeosTacacsClientAuthorizationServerAccessAccepts_Type()
)
wwpLeosTacacsClientAuthorizationServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerAccessAccepts.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerAccessRejects_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerAccessRejects_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerAccessRejects = _WwpLeosTacacsClientAuthorizationServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 9),
    _WwpLeosTacacsClientAuthorizationServerAccessRejects_Type()
)
wwpLeosTacacsClientAuthorizationServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerAccessRejects.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerMalformedAccessResponses_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerMalformedAccessResponses_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerMalformedAccessResponses = _WwpLeosTacacsClientAuthorizationServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 10),
    _WwpLeosTacacsClientAuthorizationServerMalformedAccessResponses_Type()
)
wwpLeosTacacsClientAuthorizationServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerMalformedAccessResponses.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerBadAuthenticators_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerBadAuthenticators_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerBadAuthenticators = _WwpLeosTacacsClientAuthorizationServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 11),
    _WwpLeosTacacsClientAuthorizationServerBadAuthenticators_Type()
)
wwpLeosTacacsClientAuthorizationServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerBadAuthenticators.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerPendingRequests_Type = Gauge32
_WwpLeosTacacsClientAuthorizationServerPendingRequests_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerPendingRequests = _WwpLeosTacacsClientAuthorizationServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 12),
    _WwpLeosTacacsClientAuthorizationServerPendingRequests_Type()
)
wwpLeosTacacsClientAuthorizationServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerPendingRequests.setStatus("deprecated")
_WwpLeosTacacsClientAuthorizationServerTimeouts_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerTimeouts_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerTimeouts = _WwpLeosTacacsClientAuthorizationServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 13),
    _WwpLeosTacacsClientAuthorizationServerTimeouts_Type()
)
wwpLeosTacacsClientAuthorizationServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerTimeouts.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerUnknownTypes_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerUnknownTypes_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerUnknownTypes = _WwpLeosTacacsClientAuthorizationServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 14),
    _WwpLeosTacacsClientAuthorizationServerUnknownTypes_Type()
)
wwpLeosTacacsClientAuthorizationServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerUnknownTypes.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerBadHeaderSequence_Type = Counter32
_WwpLeosTacacsClientAuthorizationServerBadHeaderSequence_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerBadHeaderSequence = _WwpLeosTacacsClientAuthorizationServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 15),
    _WwpLeosTacacsClientAuthorizationServerBadHeaderSequence_Type()
)
wwpLeosTacacsClientAuthorizationServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerBadHeaderSequence.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerStatus_Type = RowStatus
_WwpLeosTacacsClientAuthorizationServerStatus_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerStatus = _WwpLeosTacacsClientAuthorizationServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 16),
    _WwpLeosTacacsClientAuthorizationServerStatus_Type()
)
wwpLeosTacacsClientAuthorizationServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerStatus.setStatus("current")


class _WwpLeosTacacsClientAuthorizationServerApplication_Type(Integer32):
    """Custom type wwpLeosTacacsClientAuthorizationServerApplication based on Integer32"""
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
        *(("all", 3),
          ("dot1x", 2),
          ("userLogin", 1))
    )


_WwpLeosTacacsClientAuthorizationServerApplication_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAuthorizationServerApplication_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerApplication = _WwpLeosTacacsClientAuthorizationServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 17),
    _WwpLeosTacacsClientAuthorizationServerApplication_Type()
)
wwpLeosTacacsClientAuthorizationServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerApplication.setStatus("current")


class _WwpLeosTacacsClientAuthorizationServerClearStatistics_Type(TruthValue):
    """Custom type wwpLeosTacacsClientAuthorizationServerClearStatistics based on TruthValue"""


_WwpLeosTacacsClientAuthorizationServerClearStatistics_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerClearStatistics = _WwpLeosTacacsClientAuthorizationServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 18),
    _WwpLeosTacacsClientAuthorizationServerClearStatistics_Type()
)
wwpLeosTacacsClientAuthorizationServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerClearStatistics.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerResolvedInetAddrType_Type = InetAddressType
_WwpLeosTacacsClientAuthorizationServerResolvedInetAddrType_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerResolvedInetAddrType = _WwpLeosTacacsClientAuthorizationServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 19),
    _WwpLeosTacacsClientAuthorizationServerResolvedInetAddrType_Type()
)
wwpLeosTacacsClientAuthorizationServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerResolvedInetAddrType.setStatus("current")
_WwpLeosTacacsClientAuthorizationServerResolvedInetAddr_Type = InetAddress
_WwpLeosTacacsClientAuthorizationServerResolvedInetAddr_Object = MibTableColumn
wwpLeosTacacsClientAuthorizationServerResolvedInetAddr = _WwpLeosTacacsClientAuthorizationServerResolvedInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 15, 1, 20),
    _WwpLeosTacacsClientAuthorizationServerResolvedInetAddr_Type()
)
wwpLeosTacacsClientAuthorizationServerResolvedInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAuthorizationServerResolvedInetAddr.setStatus("current")
_WwpLeosTacacsClientAccountingServerTable_Object = MibTable
wwpLeosTacacsClientAccountingServerTable = _WwpLeosTacacsClientAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16)
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerTable.setStatus("current")
_WwpLeosTacacsClientAccountingServerEntry_Object = MibTableRow
wwpLeosTacacsClientAccountingServerEntry = _WwpLeosTacacsClientAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1)
)
wwpLeosTacacsClientAccountingServerEntry.setIndexNames(
    (0, "WWP-LEOS-TACACS-CLIENT-MIB", "wwpLeosTacacsClientAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerEntry.setStatus("current")


class _WwpLeosTacacsClientAccountingServerIndex_Type(Integer32):
    """Custom type wwpLeosTacacsClientAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosTacacsClientAccountingServerIndex_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAccountingServerIndex_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerIndex = _WwpLeosTacacsClientAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 1),
    _WwpLeosTacacsClientAccountingServerIndex_Type()
)
wwpLeosTacacsClientAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerIndex.setStatus("current")


class _WwpLeosTacacsClientAccountingServerAddr_Type(DisplayString):
    """Custom type wwpLeosTacacsClientAccountingServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosTacacsClientAccountingServerAddr_Type.__name__ = "DisplayString"
_WwpLeosTacacsClientAccountingServerAddr_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerAddr = _WwpLeosTacacsClientAccountingServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 2),
    _WwpLeosTacacsClientAccountingServerAddr_Type()
)
wwpLeosTacacsClientAccountingServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerAddr.setStatus("current")
_WwpLeosTacacsClientAccountingServerResolvedAddr_Type = IpAddress
_WwpLeosTacacsClientAccountingServerResolvedAddr_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerResolvedAddr = _WwpLeosTacacsClientAccountingServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 3),
    _WwpLeosTacacsClientAccountingServerResolvedAddr_Type()
)
wwpLeosTacacsClientAccountingServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerResolvedAddr.setStatus("current")
_WwpLeosTacacsClientAccountingServerPriority_Type = Integer32
_WwpLeosTacacsClientAccountingServerPriority_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerPriority = _WwpLeosTacacsClientAccountingServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 4),
    _WwpLeosTacacsClientAccountingServerPriority_Type()
)
wwpLeosTacacsClientAccountingServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerPriority.setStatus("current")


class _WwpLeosTacacsClientAccountingServerAuthPort_Type(Integer32):
    """Custom type wwpLeosTacacsClientAccountingServerAuthPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTacacsClientAccountingServerAuthPort_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAccountingServerAuthPort_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerAuthPort = _WwpLeosTacacsClientAccountingServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 5),
    _WwpLeosTacacsClientAccountingServerAuthPort_Type()
)
wwpLeosTacacsClientAccountingServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerAuthPort.setStatus("current")
_WwpLeosTacacsClientAccountingServerAccessRequests_Type = Counter32
_WwpLeosTacacsClientAccountingServerAccessRequests_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerAccessRequests = _WwpLeosTacacsClientAccountingServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 6),
    _WwpLeosTacacsClientAccountingServerAccessRequests_Type()
)
wwpLeosTacacsClientAccountingServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerAccessRequests.setStatus("current")
_WwpLeosTacacsClientAccountingServerAccessRetransmissions_Type = Counter32
_WwpLeosTacacsClientAccountingServerAccessRetransmissions_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerAccessRetransmissions = _WwpLeosTacacsClientAccountingServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 7),
    _WwpLeosTacacsClientAccountingServerAccessRetransmissions_Type()
)
wwpLeosTacacsClientAccountingServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerAccessRetransmissions.setStatus("current")
_WwpLeosTacacsClientAccountingServerAccessAccepts_Type = Counter32
_WwpLeosTacacsClientAccountingServerAccessAccepts_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerAccessAccepts = _WwpLeosTacacsClientAccountingServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 8),
    _WwpLeosTacacsClientAccountingServerAccessAccepts_Type()
)
wwpLeosTacacsClientAccountingServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerAccessAccepts.setStatus("current")
_WwpLeosTacacsClientAccountingServerAccessRejects_Type = Counter32
_WwpLeosTacacsClientAccountingServerAccessRejects_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerAccessRejects = _WwpLeosTacacsClientAccountingServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 9),
    _WwpLeosTacacsClientAccountingServerAccessRejects_Type()
)
wwpLeosTacacsClientAccountingServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerAccessRejects.setStatus("current")
_WwpLeosTacacsClientAccountingServerMalformedAccessResponses_Type = Counter32
_WwpLeosTacacsClientAccountingServerMalformedAccessResponses_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerMalformedAccessResponses = _WwpLeosTacacsClientAccountingServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 10),
    _WwpLeosTacacsClientAccountingServerMalformedAccessResponses_Type()
)
wwpLeosTacacsClientAccountingServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerMalformedAccessResponses.setStatus("current")
_WwpLeosTacacsClientAccountingServerBadAuthenticators_Type = Counter32
_WwpLeosTacacsClientAccountingServerBadAuthenticators_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerBadAuthenticators = _WwpLeosTacacsClientAccountingServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 11),
    _WwpLeosTacacsClientAccountingServerBadAuthenticators_Type()
)
wwpLeosTacacsClientAccountingServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerBadAuthenticators.setStatus("current")
_WwpLeosTacacsClientAccountingServerPendingRequests_Type = Gauge32
_WwpLeosTacacsClientAccountingServerPendingRequests_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerPendingRequests = _WwpLeosTacacsClientAccountingServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 12),
    _WwpLeosTacacsClientAccountingServerPendingRequests_Type()
)
wwpLeosTacacsClientAccountingServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerPendingRequests.setStatus("current")
_WwpLeosTacacsClientAccountingServerTimeouts_Type = Counter32
_WwpLeosTacacsClientAccountingServerTimeouts_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerTimeouts = _WwpLeosTacacsClientAccountingServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 13),
    _WwpLeosTacacsClientAccountingServerTimeouts_Type()
)
wwpLeosTacacsClientAccountingServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerTimeouts.setStatus("current")
_WwpLeosTacacsClientAccountingServerUnknownTypes_Type = Counter32
_WwpLeosTacacsClientAccountingServerUnknownTypes_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerUnknownTypes = _WwpLeosTacacsClientAccountingServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 14),
    _WwpLeosTacacsClientAccountingServerUnknownTypes_Type()
)
wwpLeosTacacsClientAccountingServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerUnknownTypes.setStatus("current")
_WwpLeosTacacsClientAccountingServerBadHeaderSequence_Type = Counter32
_WwpLeosTacacsClientAccountingServerBadHeaderSequence_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerBadHeaderSequence = _WwpLeosTacacsClientAccountingServerBadHeaderSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 15),
    _WwpLeosTacacsClientAccountingServerBadHeaderSequence_Type()
)
wwpLeosTacacsClientAccountingServerBadHeaderSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerBadHeaderSequence.setStatus("current")
_WwpLeosTacacsClientAccountingServerStatus_Type = RowStatus
_WwpLeosTacacsClientAccountingServerStatus_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerStatus = _WwpLeosTacacsClientAccountingServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 16),
    _WwpLeosTacacsClientAccountingServerStatus_Type()
)
wwpLeosTacacsClientAccountingServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerStatus.setStatus("current")


class _WwpLeosTacacsClientAccountingServerApplication_Type(Integer32):
    """Custom type wwpLeosTacacsClientAccountingServerApplication based on Integer32"""
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
        *(("all", 3),
          ("dot1x", 2),
          ("userLogin", 1))
    )


_WwpLeosTacacsClientAccountingServerApplication_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAccountingServerApplication_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerApplication = _WwpLeosTacacsClientAccountingServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 17),
    _WwpLeosTacacsClientAccountingServerApplication_Type()
)
wwpLeosTacacsClientAccountingServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerApplication.setStatus("current")


class _WwpLeosTacacsClientAccountingServerClearStatistics_Type(TruthValue):
    """Custom type wwpLeosTacacsClientAccountingServerClearStatistics based on TruthValue"""


_WwpLeosTacacsClientAccountingServerClearStatistics_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerClearStatistics = _WwpLeosTacacsClientAccountingServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 18),
    _WwpLeosTacacsClientAccountingServerClearStatistics_Type()
)
wwpLeosTacacsClientAccountingServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerClearStatistics.setStatus("current")
_WwpLeosTacacsClientAccountingServerResolvedInetAddrType_Type = InetAddressType
_WwpLeosTacacsClientAccountingServerResolvedInetAddrType_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerResolvedInetAddrType = _WwpLeosTacacsClientAccountingServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 19),
    _WwpLeosTacacsClientAccountingServerResolvedInetAddrType_Type()
)
wwpLeosTacacsClientAccountingServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerResolvedInetAddrType.setStatus("current")
_WwpLeosTacacsClientAccountingServerResolvedInetAddr_Type = InetAddress
_WwpLeosTacacsClientAccountingServerResolvedInetAddr_Object = MibTableColumn
wwpLeosTacacsClientAccountingServerResolvedInetAddr = _WwpLeosTacacsClientAccountingServerResolvedInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 16, 1, 20),
    _WwpLeosTacacsClientAccountingServerResolvedInetAddr_Type()
)
wwpLeosTacacsClientAccountingServerResolvedInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingServerResolvedInetAddr.setStatus("current")


class _WwpLeosTacacsClientAccountingSession_Type(Integer32):
    """Custom type wwpLeosTacacsClientAccountingSession based on Integer32"""
    defaultValue = 1

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


_WwpLeosTacacsClientAccountingSession_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAccountingSession_Object = MibScalar
wwpLeosTacacsClientAccountingSession = _WwpLeosTacacsClientAccountingSession_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 20),
    _WwpLeosTacacsClientAccountingSession_Type()
)
wwpLeosTacacsClientAccountingSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingSession.setStatus("current")


class _WwpLeosTacacsClientAccountingCommand_Type(Integer32):
    """Custom type wwpLeosTacacsClientAccountingCommand based on Integer32"""
    defaultValue = 1

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


_WwpLeosTacacsClientAccountingCommand_Type.__name__ = "Integer32"
_WwpLeosTacacsClientAccountingCommand_Object = MibScalar
wwpLeosTacacsClientAccountingCommand = _WwpLeosTacacsClientAccountingCommand_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 21),
    _WwpLeosTacacsClientAccountingCommand_Type()
)
wwpLeosTacacsClientAccountingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientAccountingCommand.setStatus("current")


class _WwpLeosTacacsClientGlobalServers_Type(Integer32):
    """Custom type wwpLeosTacacsClientGlobalServers based on Integer32"""
    defaultValue = 1

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


_WwpLeosTacacsClientGlobalServers_Type.__name__ = "Integer32"
_WwpLeosTacacsClientGlobalServers_Object = MibScalar
wwpLeosTacacsClientGlobalServers = _WwpLeosTacacsClientGlobalServers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 22),
    _WwpLeosTacacsClientGlobalServers_Type()
)
wwpLeosTacacsClientGlobalServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientGlobalServers.setStatus("deprecated")


class _WwpLeosTacacsClientSearchMethod_Type(Integer32):
    """Custom type wwpLeosTacacsClientSearchMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cached", 2),
          ("priority", 1))
    )


_WwpLeosTacacsClientSearchMethod_Type.__name__ = "Integer32"
_WwpLeosTacacsClientSearchMethod_Object = MibScalar
wwpLeosTacacsClientSearchMethod = _WwpLeosTacacsClientSearchMethod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 23),
    _WwpLeosTacacsClientSearchMethod_Type()
)
wwpLeosTacacsClientSearchMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientSearchMethod.setStatus("current")


class _WwpLeosTacacsClientKeyMinLen_Type(Integer32):
    """Custom type wwpLeosTacacsClientKeyMinLen based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_WwpLeosTacacsClientKeyMinLen_Type.__name__ = "Integer32"
_WwpLeosTacacsClientKeyMinLen_Object = MibScalar
wwpLeosTacacsClientKeyMinLen = _WwpLeosTacacsClientKeyMinLen_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 1, 1, 24),
    _WwpLeosTacacsClientKeyMinLen_Type()
)
wwpLeosTacacsClientKeyMinLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTacacsClientKeyMinLen.setStatus("current")
_WwpLeosTacacsClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClientMIBNotificationPrefix = _WwpLeosTacacsClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 2)
)
_WwpLeosTacacsClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClientMIBNotifications = _WwpLeosTacacsClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 2, 0)
)
_WwpLeosTacacsClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClientMIBConformance = _WwpLeosTacacsClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 3)
)
_WwpLeosTacacsClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClientMIBCompliances = _WwpLeosTacacsClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 3, 1)
)
_WwpLeosTacacsClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosTacacsClientMIBGroups = _WwpLeosTacacsClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 402, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-TACACS-CLIENT-MIB",
    **{"TacacsString": TacacsString,
       "wwpLeosTacacsClientMIB": wwpLeosTacacsClientMIB,
       "wwpLeosTacacsClientMIBObjects": wwpLeosTacacsClientMIBObjects,
       "wwpLeosTacacsClient": wwpLeosTacacsClient,
       "wwpLeosTacacsAdminState": wwpLeosTacacsAdminState,
       "wwpLeosTacacsOperState": wwpLeosTacacsOperState,
       "wwpLeosTacacsClientTimeout": wwpLeosTacacsClientTimeout,
       "wwpLeosTacacsClientRetries": wwpLeosTacacsClientRetries,
       "wwpLeosTacacsClientPrivilegeLevelRW": wwpLeosTacacsClientPrivilegeLevelRW,
       "wwpLeosTacacsClientPrivilegeLevelAdmin": wwpLeosTacacsClientPrivilegeLevelAdmin,
       "wwpLeosTacacsClientPrivilegeLevelDiag": wwpLeosTacacsClientPrivilegeLevelDiag,
       "wwpLeosTacacsClientAuthKey": wwpLeosTacacsClientAuthKey,
       "wwpLeosTacacsAuthenticationAdminState": wwpLeosTacacsAuthenticationAdminState,
       "wwpLeosTacacsAuthorizationAdminState": wwpLeosTacacsAuthorizationAdminState,
       "wwpLeosTacacsAccountingAdminState": wwpLeosTacacsAccountingAdminState,
       "wwpLeosTacacsSyslogAdminState": wwpLeosTacacsSyslogAdminState,
       "wwpLeosTacacsClientServerTable": wwpLeosTacacsClientServerTable,
       "wwpLeosTacacsClientServerEntry": wwpLeosTacacsClientServerEntry,
       "wwpLeosTacacsClientServerIndex": wwpLeosTacacsClientServerIndex,
       "wwpLeosTacacsClientServerAddr": wwpLeosTacacsClientServerAddr,
       "wwpLeosTacacsClientServerResolvedAddr": wwpLeosTacacsClientServerResolvedAddr,
       "wwpLeosTacacsClientServerPriority": wwpLeosTacacsClientServerPriority,
       "wwpLeosTacacsClientServerAuthPort": wwpLeosTacacsClientServerAuthPort,
       "wwpLeosTacacsClientServerAccessRequests": wwpLeosTacacsClientServerAccessRequests,
       "wwpLeosTacacsClientServerAccessRetransmissions": wwpLeosTacacsClientServerAccessRetransmissions,
       "wwpLeosTacacsClientServerAccessAccepts": wwpLeosTacacsClientServerAccessAccepts,
       "wwpLeosTacacsClientServerAccessRejects": wwpLeosTacacsClientServerAccessRejects,
       "wwpLeosTacacsClientServerMalformedAccessResponses": wwpLeosTacacsClientServerMalformedAccessResponses,
       "wwpLeosTacacsClientServerBadAuthenticators": wwpLeosTacacsClientServerBadAuthenticators,
       "wwpLeosTacacsClientServerPendingRequests": wwpLeosTacacsClientServerPendingRequests,
       "wwpLeosTacacsClientServerTimeouts": wwpLeosTacacsClientServerTimeouts,
       "wwpLeosTacacsClientServerUnknownTypes": wwpLeosTacacsClientServerUnknownTypes,
       "wwpLeosTacacsClientServerBadHeaderSequence": wwpLeosTacacsClientServerBadHeaderSequence,
       "wwpLeosTacacsClientServerStatus": wwpLeosTacacsClientServerStatus,
       "wwpLeosTacacsClientServerApplication": wwpLeosTacacsClientServerApplication,
       "wwpLeosTacacsClientServerClearStatistics": wwpLeosTacacsClientServerClearStatistics,
       "wwpLeosTacacsClientGlobalAuthorizationAccessRequests": wwpLeosTacacsClientGlobalAuthorizationAccessRequests,
       "wwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions": wwpLeosTacacsClientGlobalAuthorizationAccessRetransmissions,
       "wwpLeosTacacsClientGlobalAuthorizationAccessAccepts": wwpLeosTacacsClientGlobalAuthorizationAccessAccepts,
       "wwpLeosTacacsClientGlobalAuthorizationAccessRejects": wwpLeosTacacsClientGlobalAuthorizationAccessRejects,
       "wwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses": wwpLeosTacacsClientGlobalAuthorizationMalformedAccessResponses,
       "wwpLeosTacacsClientGlobalAuthorizationBadAuthenticators": wwpLeosTacacsClientGlobalAuthorizationBadAuthenticators,
       "wwpLeosTacacsClientGlobalAuthorizationTimeouts": wwpLeosTacacsClientGlobalAuthorizationTimeouts,
       "wwpLeosTacacsClientGlobalAuthorizationUnknownTypes": wwpLeosTacacsClientGlobalAuthorizationUnknownTypes,
       "wwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence": wwpLeosTacacsClientGlobalAuthorizationBadHeaderSequence,
       "wwpLeosTacacsClientGlobalAccountingAccessRequests": wwpLeosTacacsClientGlobalAccountingAccessRequests,
       "wwpLeosTacacsClientGlobalAccountingAccessRetransmissions": wwpLeosTacacsClientGlobalAccountingAccessRetransmissions,
       "wwpLeosTacacsClientGlobalAccountingAccessAccepts": wwpLeosTacacsClientGlobalAccountingAccessAccepts,
       "wwpLeosTacacsClientGlobalAccountingAccessRejects": wwpLeosTacacsClientGlobalAccountingAccessRejects,
       "wwpLeosTacacsClientGlobalAccountingMalformedAccessResponses": wwpLeosTacacsClientGlobalAccountingMalformedAccessResponses,
       "wwpLeosTacacsClientGlobalAccountingBadAuthenticators": wwpLeosTacacsClientGlobalAccountingBadAuthenticators,
       "wwpLeosTacacsClientGlobalAccountingTimeouts": wwpLeosTacacsClientGlobalAccountingTimeouts,
       "wwpLeosTacacsClientGlobalAccountingUnknownTypes": wwpLeosTacacsClientGlobalAccountingUnknownTypes,
       "wwpLeosTacacsClientGlobalAccountingBadHeaderSequence": wwpLeosTacacsClientGlobalAccountingBadHeaderSequence,
       "wwpLeosTacacsClientServerResolvedInetAddrType": wwpLeosTacacsClientServerResolvedInetAddrType,
       "wwpLeosTacacsClientServerResolvedInetAddr": wwpLeosTacacsClientServerResolvedInetAddr,
       "wwpLeosTacacsClientAuthenticationServerTable": wwpLeosTacacsClientAuthenticationServerTable,
       "wwpLeosTacacsClientAuthenticationServerEntry": wwpLeosTacacsClientAuthenticationServerEntry,
       "wwpLeosTacacsClientAuthenticationServerIndex": wwpLeosTacacsClientAuthenticationServerIndex,
       "wwpLeosTacacsClientAuthenticationServerAddr": wwpLeosTacacsClientAuthenticationServerAddr,
       "wwpLeosTacacsClientAuthenticationServerResolvedAddr": wwpLeosTacacsClientAuthenticationServerResolvedAddr,
       "wwpLeosTacacsClientAuthenticationServerPriority": wwpLeosTacacsClientAuthenticationServerPriority,
       "wwpLeosTacacsClientAuthenticationServerAuthPort": wwpLeosTacacsClientAuthenticationServerAuthPort,
       "wwpLeosTacacsClientAuthenticationServerAccessRequests": wwpLeosTacacsClientAuthenticationServerAccessRequests,
       "wwpLeosTacacsClientAuthenticationServerAccessRetransmissions": wwpLeosTacacsClientAuthenticationServerAccessRetransmissions,
       "wwpLeosTacacsClientAuthenticationServerAccessAccepts": wwpLeosTacacsClientAuthenticationServerAccessAccepts,
       "wwpLeosTacacsClientAuthenticationServerAccessRejects": wwpLeosTacacsClientAuthenticationServerAccessRejects,
       "wwpLeosTacacsClientAuthenticationServerMalformedAccessResponses": wwpLeosTacacsClientAuthenticationServerMalformedAccessResponses,
       "wwpLeosTacacsClientAuthenticationServerBadAuthenticators": wwpLeosTacacsClientAuthenticationServerBadAuthenticators,
       "wwpLeosTacacsClientAuthenticationServerPendingRequests": wwpLeosTacacsClientAuthenticationServerPendingRequests,
       "wwpLeosTacacsClientAuthenticationServerTimeouts": wwpLeosTacacsClientAuthenticationServerTimeouts,
       "wwpLeosTacacsClientAuthenticationServerUnknownTypes": wwpLeosTacacsClientAuthenticationServerUnknownTypes,
       "wwpLeosTacacsClientAuthenticationServerBadHeaderSequence": wwpLeosTacacsClientAuthenticationServerBadHeaderSequence,
       "wwpLeosTacacsClientAuthenticationServerStatus": wwpLeosTacacsClientAuthenticationServerStatus,
       "wwpLeosTacacsClientAuthenticationServerApplication": wwpLeosTacacsClientAuthenticationServerApplication,
       "wwpLeosTacacsClientAuthenticationServerClearStatistics": wwpLeosTacacsClientAuthenticationServerClearStatistics,
       "wwpLeosTacacsClientAuthenticationServerResolvedInetAddrType": wwpLeosTacacsClientAuthenticationServerResolvedInetAddrType,
       "wwpLeosTacacsClientAuthenticationServerResolvedInetAddr": wwpLeosTacacsClientAuthenticationServerResolvedInetAddr,
       "wwpLeosTacacsClientAuthorizationServerTable": wwpLeosTacacsClientAuthorizationServerTable,
       "wwpLeosTacacsClientAuthorizationServerEntry": wwpLeosTacacsClientAuthorizationServerEntry,
       "wwpLeosTacacsClientAuthorizationServerIndex": wwpLeosTacacsClientAuthorizationServerIndex,
       "wwpLeosTacacsClientAuthorizationServerAddr": wwpLeosTacacsClientAuthorizationServerAddr,
       "wwpLeosTacacsClientAuthorizationServerResolvedAddr": wwpLeosTacacsClientAuthorizationServerResolvedAddr,
       "wwpLeosTacacsClientAuthorizationServerPriority": wwpLeosTacacsClientAuthorizationServerPriority,
       "wwpLeosTacacsClientAuthorizationServerAuthPort": wwpLeosTacacsClientAuthorizationServerAuthPort,
       "wwpLeosTacacsClientAuthorizationServerAccessRequests": wwpLeosTacacsClientAuthorizationServerAccessRequests,
       "wwpLeosTacacsClientAuthorizationServerAccessRetransmissions": wwpLeosTacacsClientAuthorizationServerAccessRetransmissions,
       "wwpLeosTacacsClientAuthorizationServerAccessAccepts": wwpLeosTacacsClientAuthorizationServerAccessAccepts,
       "wwpLeosTacacsClientAuthorizationServerAccessRejects": wwpLeosTacacsClientAuthorizationServerAccessRejects,
       "wwpLeosTacacsClientAuthorizationServerMalformedAccessResponses": wwpLeosTacacsClientAuthorizationServerMalformedAccessResponses,
       "wwpLeosTacacsClientAuthorizationServerBadAuthenticators": wwpLeosTacacsClientAuthorizationServerBadAuthenticators,
       "wwpLeosTacacsClientAuthorizationServerPendingRequests": wwpLeosTacacsClientAuthorizationServerPendingRequests,
       "wwpLeosTacacsClientAuthorizationServerTimeouts": wwpLeosTacacsClientAuthorizationServerTimeouts,
       "wwpLeosTacacsClientAuthorizationServerUnknownTypes": wwpLeosTacacsClientAuthorizationServerUnknownTypes,
       "wwpLeosTacacsClientAuthorizationServerBadHeaderSequence": wwpLeosTacacsClientAuthorizationServerBadHeaderSequence,
       "wwpLeosTacacsClientAuthorizationServerStatus": wwpLeosTacacsClientAuthorizationServerStatus,
       "wwpLeosTacacsClientAuthorizationServerApplication": wwpLeosTacacsClientAuthorizationServerApplication,
       "wwpLeosTacacsClientAuthorizationServerClearStatistics": wwpLeosTacacsClientAuthorizationServerClearStatistics,
       "wwpLeosTacacsClientAuthorizationServerResolvedInetAddrType": wwpLeosTacacsClientAuthorizationServerResolvedInetAddrType,
       "wwpLeosTacacsClientAuthorizationServerResolvedInetAddr": wwpLeosTacacsClientAuthorizationServerResolvedInetAddr,
       "wwpLeosTacacsClientAccountingServerTable": wwpLeosTacacsClientAccountingServerTable,
       "wwpLeosTacacsClientAccountingServerEntry": wwpLeosTacacsClientAccountingServerEntry,
       "wwpLeosTacacsClientAccountingServerIndex": wwpLeosTacacsClientAccountingServerIndex,
       "wwpLeosTacacsClientAccountingServerAddr": wwpLeosTacacsClientAccountingServerAddr,
       "wwpLeosTacacsClientAccountingServerResolvedAddr": wwpLeosTacacsClientAccountingServerResolvedAddr,
       "wwpLeosTacacsClientAccountingServerPriority": wwpLeosTacacsClientAccountingServerPriority,
       "wwpLeosTacacsClientAccountingServerAuthPort": wwpLeosTacacsClientAccountingServerAuthPort,
       "wwpLeosTacacsClientAccountingServerAccessRequests": wwpLeosTacacsClientAccountingServerAccessRequests,
       "wwpLeosTacacsClientAccountingServerAccessRetransmissions": wwpLeosTacacsClientAccountingServerAccessRetransmissions,
       "wwpLeosTacacsClientAccountingServerAccessAccepts": wwpLeosTacacsClientAccountingServerAccessAccepts,
       "wwpLeosTacacsClientAccountingServerAccessRejects": wwpLeosTacacsClientAccountingServerAccessRejects,
       "wwpLeosTacacsClientAccountingServerMalformedAccessResponses": wwpLeosTacacsClientAccountingServerMalformedAccessResponses,
       "wwpLeosTacacsClientAccountingServerBadAuthenticators": wwpLeosTacacsClientAccountingServerBadAuthenticators,
       "wwpLeosTacacsClientAccountingServerPendingRequests": wwpLeosTacacsClientAccountingServerPendingRequests,
       "wwpLeosTacacsClientAccountingServerTimeouts": wwpLeosTacacsClientAccountingServerTimeouts,
       "wwpLeosTacacsClientAccountingServerUnknownTypes": wwpLeosTacacsClientAccountingServerUnknownTypes,
       "wwpLeosTacacsClientAccountingServerBadHeaderSequence": wwpLeosTacacsClientAccountingServerBadHeaderSequence,
       "wwpLeosTacacsClientAccountingServerStatus": wwpLeosTacacsClientAccountingServerStatus,
       "wwpLeosTacacsClientAccountingServerApplication": wwpLeosTacacsClientAccountingServerApplication,
       "wwpLeosTacacsClientAccountingServerClearStatistics": wwpLeosTacacsClientAccountingServerClearStatistics,
       "wwpLeosTacacsClientAccountingServerResolvedInetAddrType": wwpLeosTacacsClientAccountingServerResolvedInetAddrType,
       "wwpLeosTacacsClientAccountingServerResolvedInetAddr": wwpLeosTacacsClientAccountingServerResolvedInetAddr,
       "wwpLeosTacacsClientAccountingSession": wwpLeosTacacsClientAccountingSession,
       "wwpLeosTacacsClientAccountingCommand": wwpLeosTacacsClientAccountingCommand,
       "wwpLeosTacacsClientGlobalServers": wwpLeosTacacsClientGlobalServers,
       "wwpLeosTacacsClientSearchMethod": wwpLeosTacacsClientSearchMethod,
       "wwpLeosTacacsClientKeyMinLen": wwpLeosTacacsClientKeyMinLen,
       "wwpLeosTacacsClientMIBNotificationPrefix": wwpLeosTacacsClientMIBNotificationPrefix,
       "wwpLeosTacacsClientMIBNotifications": wwpLeosTacacsClientMIBNotifications,
       "wwpLeosTacacsClientMIBConformance": wwpLeosTacacsClientMIBConformance,
       "wwpLeosTacacsClientMIBCompliances": wwpLeosTacacsClientMIBCompliances,
       "wwpLeosTacacsClientMIBGroups": wwpLeosTacacsClientMIBGroups}
)
