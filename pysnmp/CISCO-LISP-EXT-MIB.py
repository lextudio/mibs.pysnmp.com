# SNMP MIB module (CISCO-LISP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LISP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:04 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(LispAddressType,
 lispEidRegistrationSiteName,
 lispFeaturesEntry,
 lispFeaturesMapCacheLimit,
 lispGlobalStatsEntry,
 lispMappingDatabaseTimeStamp,
 lispUseMapResolverState,
 lispUseMapServerState,
 lispUseProxyEtrState) = mibBuilder.importSymbols(
    "LISP-MIB",
    "LispAddressType",
    "lispEidRegistrationSiteName",
    "lispFeaturesEntry",
    "lispFeaturesMapCacheLimit",
    "lispGlobalStatsEntry",
    "lispMappingDatabaseTimeStamp",
    "lispUseMapResolverState",
    "lispUseMapServerState",
    "lispUseProxyEtrState")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLispExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825)
)
ciscoLispExtMIB.setRevisions(
        ("2015-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLispExtNotifications_ObjectIdentity = ObjectIdentity
ciscoLispExtNotifications = _CiscoLispExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0)
)
_CiscoLispExtObjects_ObjectIdentity = ObjectIdentity
ciscoLispExtObjects = _CiscoLispExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1)
)
_ClispExtEidRegRlocMembershipTable_Object = MibTable
clispExtEidRegRlocMembershipTable = _ClispExtEidRegRlocMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1)
)
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipTable.setStatus("current")
_ClispExtEidRegRlocMembershipEntry_Object = MibTableRow
clispExtEidRegRlocMembershipEntry = _ClispExtEidRegRlocMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1)
)
clispExtEidRegRlocMembershipEntry.setIndexNames(
    (0, "CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipInstanceID"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipEidAfi"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipRlocLength"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipRloc"),
)
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipEntry.setStatus("current")


class _ClispExtEidRegRlocMembershipInstanceID_Type(Unsigned32):
    """Custom type clispExtEidRegRlocMembershipInstanceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ClispExtEidRegRlocMembershipInstanceID_Type.__name__ = "Unsigned32"
_ClispExtEidRegRlocMembershipInstanceID_Object = MibTableColumn
clispExtEidRegRlocMembershipInstanceID = _ClispExtEidRegRlocMembershipInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 1),
    _ClispExtEidRegRlocMembershipInstanceID_Type()
)
clispExtEidRegRlocMembershipInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipInstanceID.setStatus("current")
_ClispExtEidRegRlocMembershipEidAfi_Type = AddressFamilyNumbers
_ClispExtEidRegRlocMembershipEidAfi_Object = MibTableColumn
clispExtEidRegRlocMembershipEidAfi = _ClispExtEidRegRlocMembershipEidAfi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 2),
    _ClispExtEidRegRlocMembershipEidAfi_Type()
)
clispExtEidRegRlocMembershipEidAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipEidAfi.setStatus("current")


class _ClispExtEidRegRlocMembershipRlocLength_Type(Integer32):
    """Custom type clispExtEidRegRlocMembershipRlocLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_ClispExtEidRegRlocMembershipRlocLength_Type.__name__ = "Integer32"
_ClispExtEidRegRlocMembershipRlocLength_Object = MibTableColumn
clispExtEidRegRlocMembershipRlocLength = _ClispExtEidRegRlocMembershipRlocLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 3),
    _ClispExtEidRegRlocMembershipRlocLength_Type()
)
clispExtEidRegRlocMembershipRlocLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipRlocLength.setStatus("current")
_ClispExtEidRegRlocMembershipRloc_Type = LispAddressType
_ClispExtEidRegRlocMembershipRloc_Object = MibTableColumn
clispExtEidRegRlocMembershipRloc = _ClispExtEidRegRlocMembershipRloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 4),
    _ClispExtEidRegRlocMembershipRloc_Type()
)
clispExtEidRegRlocMembershipRloc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipRloc.setStatus("current")


class _ClispExtEidRegRlocMembershipMemberSince_Type(TimeStamp):
    """Custom type clispExtEidRegRlocMembershipMemberSince based on TimeStamp"""
    defaultValue = 0


_ClispExtEidRegRlocMembershipMemberSince_Object = MibTableColumn
clispExtEidRegRlocMembershipMemberSince = _ClispExtEidRegRlocMembershipMemberSince_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 5),
    _ClispExtEidRegRlocMembershipMemberSince_Type()
)
clispExtEidRegRlocMembershipMemberSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipMemberSince.setStatus("current")
_ClispExtEidRegRlocMembershipGleaned_Type = TruthValue
_ClispExtEidRegRlocMembershipGleaned_Object = MibTableColumn
clispExtEidRegRlocMembershipGleaned = _ClispExtEidRegRlocMembershipGleaned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 6),
    _ClispExtEidRegRlocMembershipGleaned_Type()
)
clispExtEidRegRlocMembershipGleaned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipGleaned.setStatus("current")
_ClispExtEidRegRlocMembershipConfigured_Type = TruthValue
_ClispExtEidRegRlocMembershipConfigured_Object = MibTableColumn
clispExtEidRegRlocMembershipConfigured = _ClispExtEidRegRlocMembershipConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 1, 1, 7),
    _ClispExtEidRegRlocMembershipConfigured_Type()
)
clispExtEidRegRlocMembershipConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipConfigured.setStatus("current")
_ClispExtRlocMembershipTable_Object = MibTable
clispExtRlocMembershipTable = _ClispExtRlocMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2)
)
if mibBuilder.loadTexts:
    clispExtRlocMembershipTable.setStatus("current")
_ClispExtRlocMembershipEntry_Object = MibTableRow
clispExtRlocMembershipEntry = _ClispExtRlocMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1)
)
clispExtRlocMembershipEntry.setIndexNames(
    (0, "CISCO-LISP-EXT-MIB", "clispExtRlocMembershipInstanceID"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtRlocMembershipEidAfi"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtRlocMembershipRlocLength"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtRlocMembershipRloc"),
)
if mibBuilder.loadTexts:
    clispExtRlocMembershipEntry.setStatus("current")


class _ClispExtRlocMembershipInstanceID_Type(Unsigned32):
    """Custom type clispExtRlocMembershipInstanceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ClispExtRlocMembershipInstanceID_Type.__name__ = "Unsigned32"
_ClispExtRlocMembershipInstanceID_Object = MibTableColumn
clispExtRlocMembershipInstanceID = _ClispExtRlocMembershipInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 1),
    _ClispExtRlocMembershipInstanceID_Type()
)
clispExtRlocMembershipInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtRlocMembershipInstanceID.setStatus("current")
_ClispExtRlocMembershipEidAfi_Type = AddressFamilyNumbers
_ClispExtRlocMembershipEidAfi_Object = MibTableColumn
clispExtRlocMembershipEidAfi = _ClispExtRlocMembershipEidAfi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 2),
    _ClispExtRlocMembershipEidAfi_Type()
)
clispExtRlocMembershipEidAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtRlocMembershipEidAfi.setStatus("current")


class _ClispExtRlocMembershipRlocLength_Type(Integer32):
    """Custom type clispExtRlocMembershipRlocLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_ClispExtRlocMembershipRlocLength_Type.__name__ = "Integer32"
_ClispExtRlocMembershipRlocLength_Object = MibTableColumn
clispExtRlocMembershipRlocLength = _ClispExtRlocMembershipRlocLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 3),
    _ClispExtRlocMembershipRlocLength_Type()
)
clispExtRlocMembershipRlocLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtRlocMembershipRlocLength.setStatus("current")
_ClispExtRlocMembershipRloc_Type = LispAddressType
_ClispExtRlocMembershipRloc_Object = MibTableColumn
clispExtRlocMembershipRloc = _ClispExtRlocMembershipRloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 4),
    _ClispExtRlocMembershipRloc_Type()
)
clispExtRlocMembershipRloc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtRlocMembershipRloc.setStatus("current")


class _ClispExtRlocMembershipMemberSince_Type(TimeStamp):
    """Custom type clispExtRlocMembershipMemberSince based on TimeStamp"""
    defaultValue = 0


_ClispExtRlocMembershipMemberSince_Object = MibTableColumn
clispExtRlocMembershipMemberSince = _ClispExtRlocMembershipMemberSince_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 5),
    _ClispExtRlocMembershipMemberSince_Type()
)
clispExtRlocMembershipMemberSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtRlocMembershipMemberSince.setStatus("current")
_ClispExtRlocMembershipDiscovered_Type = TruthValue
_ClispExtRlocMembershipDiscovered_Object = MibTableColumn
clispExtRlocMembershipDiscovered = _ClispExtRlocMembershipDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 6),
    _ClispExtRlocMembershipDiscovered_Type()
)
clispExtRlocMembershipDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtRlocMembershipDiscovered.setStatus("current")
_ClispExtRlocMembershipConfigured_Type = TruthValue
_ClispExtRlocMembershipConfigured_Object = MibTableColumn
clispExtRlocMembershipConfigured = _ClispExtRlocMembershipConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 2, 1, 7),
    _ClispExtRlocMembershipConfigured_Type()
)
clispExtRlocMembershipConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtRlocMembershipConfigured.setStatus("current")
_ClispExtReliableTransportSessionTable_Object = MibTable
clispExtReliableTransportSessionTable = _ClispExtReliableTransportSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3)
)
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionTable.setStatus("current")
_ClispExtReliableTransportSessionEntry_Object = MibTableRow
clispExtReliableTransportSessionEntry = _ClispExtReliableTransportSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1)
)
clispExtReliableTransportSessionEntry.setIndexNames(
    (0, "CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionPeerAddressLength"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionPeerAddress"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionPeerPort"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionLocalAddressLength"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionLocalAddress"),
    (0, "CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionLocalPort"),
)
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionEntry.setStatus("current")


class _ClispExtReliableTransportSessionPeerAddressLength_Type(Integer32):
    """Custom type clispExtReliableTransportSessionPeerAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_ClispExtReliableTransportSessionPeerAddressLength_Type.__name__ = "Integer32"
_ClispExtReliableTransportSessionPeerAddressLength_Object = MibTableColumn
clispExtReliableTransportSessionPeerAddressLength = _ClispExtReliableTransportSessionPeerAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 1),
    _ClispExtReliableTransportSessionPeerAddressLength_Type()
)
clispExtReliableTransportSessionPeerAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionPeerAddressLength.setStatus("current")
_ClispExtReliableTransportSessionPeerAddress_Type = LispAddressType
_ClispExtReliableTransportSessionPeerAddress_Object = MibTableColumn
clispExtReliableTransportSessionPeerAddress = _ClispExtReliableTransportSessionPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 2),
    _ClispExtReliableTransportSessionPeerAddress_Type()
)
clispExtReliableTransportSessionPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionPeerAddress.setStatus("current")
_ClispExtReliableTransportSessionPeerPort_Type = InetPortNumber
_ClispExtReliableTransportSessionPeerPort_Object = MibTableColumn
clispExtReliableTransportSessionPeerPort = _ClispExtReliableTransportSessionPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 3),
    _ClispExtReliableTransportSessionPeerPort_Type()
)
clispExtReliableTransportSessionPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionPeerPort.setStatus("current")


class _ClispExtReliableTransportSessionLocalAddressLength_Type(Integer32):
    """Custom type clispExtReliableTransportSessionLocalAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_ClispExtReliableTransportSessionLocalAddressLength_Type.__name__ = "Integer32"
_ClispExtReliableTransportSessionLocalAddressLength_Object = MibTableColumn
clispExtReliableTransportSessionLocalAddressLength = _ClispExtReliableTransportSessionLocalAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 4),
    _ClispExtReliableTransportSessionLocalAddressLength_Type()
)
clispExtReliableTransportSessionLocalAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionLocalAddressLength.setStatus("current")
_ClispExtReliableTransportSessionLocalAddress_Type = LispAddressType
_ClispExtReliableTransportSessionLocalAddress_Object = MibTableColumn
clispExtReliableTransportSessionLocalAddress = _ClispExtReliableTransportSessionLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 5),
    _ClispExtReliableTransportSessionLocalAddress_Type()
)
clispExtReliableTransportSessionLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionLocalAddress.setStatus("current")
_ClispExtReliableTransportSessionLocalPort_Type = InetPortNumber
_ClispExtReliableTransportSessionLocalPort_Object = MibTableColumn
clispExtReliableTransportSessionLocalPort = _ClispExtReliableTransportSessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 6),
    _ClispExtReliableTransportSessionLocalPort_Type()
)
clispExtReliableTransportSessionLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionLocalPort.setStatus("current")


class _ClispExtReliableTransportSessionState_Type(Integer32):
    """Custom type clispExtReliableTransportSessionState based on Integer32"""
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


_ClispExtReliableTransportSessionState_Type.__name__ = "Integer32"
_ClispExtReliableTransportSessionState_Object = MibTableColumn
clispExtReliableTransportSessionState = _ClispExtReliableTransportSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 7),
    _ClispExtReliableTransportSessionState_Type()
)
clispExtReliableTransportSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionState.setStatus("current")


class _ClispExtReliableTransportSessionLastStateChangeTime_Type(TimeStamp):
    """Custom type clispExtReliableTransportSessionLastStateChangeTime based on TimeStamp"""
    defaultValue = 0


_ClispExtReliableTransportSessionLastStateChangeTime_Object = MibTableColumn
clispExtReliableTransportSessionLastStateChangeTime = _ClispExtReliableTransportSessionLastStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 8),
    _ClispExtReliableTransportSessionLastStateChangeTime_Type()
)
clispExtReliableTransportSessionLastStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionLastStateChangeTime.setStatus("current")


class _ClispExtReliableTransportSessionEstablishmentRole_Type(Integer32):
    """Custom type clispExtReliableTransportSessionEstablishmentRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_ClispExtReliableTransportSessionEstablishmentRole_Type.__name__ = "Integer32"
_ClispExtReliableTransportSessionEstablishmentRole_Object = MibTableColumn
clispExtReliableTransportSessionEstablishmentRole = _ClispExtReliableTransportSessionEstablishmentRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 9),
    _ClispExtReliableTransportSessionEstablishmentRole_Type()
)
clispExtReliableTransportSessionEstablishmentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionEstablishmentRole.setStatus("current")
_ClispExtReliableTransportSessionMessagesIn_Type = Counter64
_ClispExtReliableTransportSessionMessagesIn_Object = MibTableColumn
clispExtReliableTransportSessionMessagesIn = _ClispExtReliableTransportSessionMessagesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 10),
    _ClispExtReliableTransportSessionMessagesIn_Type()
)
clispExtReliableTransportSessionMessagesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionMessagesIn.setStatus("current")
_ClispExtReliableTransportSessionMessagesOut_Type = Counter64
_ClispExtReliableTransportSessionMessagesOut_Object = MibTableColumn
clispExtReliableTransportSessionMessagesOut = _ClispExtReliableTransportSessionMessagesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 11),
    _ClispExtReliableTransportSessionMessagesOut_Type()
)
clispExtReliableTransportSessionMessagesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionMessagesOut.setStatus("current")
_ClispExtReliableTransportSessionBytesIn_Type = Counter64
_ClispExtReliableTransportSessionBytesIn_Object = MibTableColumn
clispExtReliableTransportSessionBytesIn = _ClispExtReliableTransportSessionBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 12),
    _ClispExtReliableTransportSessionBytesIn_Type()
)
clispExtReliableTransportSessionBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionBytesIn.setStatus("current")
_ClispExtReliableTransportSessionBytesOut_Type = Counter64
_ClispExtReliableTransportSessionBytesOut_Object = MibTableColumn
clispExtReliableTransportSessionBytesOut = _ClispExtReliableTransportSessionBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 3, 1, 13),
    _ClispExtReliableTransportSessionBytesOut_Type()
)
clispExtReliableTransportSessionBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionBytesOut.setStatus("current")
_ClispExtGlobalStatsTable_Object = MibTable
clispExtGlobalStatsTable = _ClispExtGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 4)
)
if mibBuilder.loadTexts:
    clispExtGlobalStatsTable.setStatus("current")
_ClispExtGlobalStatsEntry_Object = MibTableRow
clispExtGlobalStatsEntry = _ClispExtGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clispExtGlobalStatsEntry.setStatus("current")
_ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Type = Unsigned32
_ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Object = MibTableColumn
clispExtGlobalStatsEidRegMoreSpecificEntryCount = _ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 4, 1, 1),
    _ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Type()
)
clispExtGlobalStatsEidRegMoreSpecificEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtGlobalStatsEidRegMoreSpecificEntryCount.setStatus("current")
_ClispExtFeaturesTable_Object = MibTable
clispExtFeaturesTable = _ClispExtFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 5)
)
if mibBuilder.loadTexts:
    clispExtFeaturesTable.setStatus("current")
_ClispExtFeaturesEntry_Object = MibTableRow
clispExtFeaturesEntry = _ClispExtFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clispExtFeaturesEntry.setStatus("current")
_ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Type = Unsigned32
_ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Object = MibTableColumn
clispExtFeaturesEidRegMoreSpecificWarningThreshold = _ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 5, 1, 1),
    _ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Type()
)
clispExtFeaturesEidRegMoreSpecificWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtFeaturesEidRegMoreSpecificWarningThreshold.setStatus("current")
_ClispExtFeaturesEidRegMoreSpecificLimit_Type = Unsigned32
_ClispExtFeaturesEidRegMoreSpecificLimit_Object = MibTableColumn
clispExtFeaturesEidRegMoreSpecificLimit = _ClispExtFeaturesEidRegMoreSpecificLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 5, 1, 2),
    _ClispExtFeaturesEidRegMoreSpecificLimit_Type()
)
clispExtFeaturesEidRegMoreSpecificLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtFeaturesEidRegMoreSpecificLimit.setStatus("current")
_ClispExtFeaturesMapCacheWarningThreshold_Type = Unsigned32
_ClispExtFeaturesMapCacheWarningThreshold_Object = MibTableColumn
clispExtFeaturesMapCacheWarningThreshold = _ClispExtFeaturesMapCacheWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 5, 1, 3),
    _ClispExtFeaturesMapCacheWarningThreshold_Type()
)
clispExtFeaturesMapCacheWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtFeaturesMapCacheWarningThreshold.setStatus("current")
_ClispExtNotificationObjects_ObjectIdentity = ObjectIdentity
clispExtNotificationObjects = _ClispExtNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 6)
)


class _ClispExtEidRegFailureCause_Type(Integer32):
    """Custom type clispExtEidRegFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowedLocatorMismatch", 3),
          ("authenticationFailure", 2),
          ("noEidPrefixConfiguration", 1))
    )


_ClispExtEidRegFailureCause_Type.__name__ = "Integer32"
_ClispExtEidRegFailureCause_Object = MibScalar
clispExtEidRegFailureCause = _ClispExtEidRegFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 6, 1),
    _ClispExtEidRegFailureCause_Type()
)
clispExtEidRegFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clispExtEidRegFailureCause.setStatus("current")


class _ClispExtEidRegMapRequestDroppedCause_Type(Integer32):
    """Custom type clispExtEidRegMapRequestDroppedCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowedLocatorPolicyViolation", 3),
          ("malformedRequest", 1),
          ("noMatchingEidRegistration", 2))
    )


_ClispExtEidRegMapRequestDroppedCause_Type.__name__ = "Integer32"
_ClispExtEidRegMapRequestDroppedCause_Object = MibScalar
clispExtEidRegMapRequestDroppedCause = _ClispExtEidRegMapRequestDroppedCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 6, 2),
    _ClispExtEidRegMapRequestDroppedCause_Type()
)
clispExtEidRegMapRequestDroppedCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clispExtEidRegMapRequestDroppedCause.setStatus("current")
_ClispExtGlobalObjects_ObjectIdentity = ObjectIdentity
clispExtGlobalObjects = _ClispExtGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 7)
)
_ClispExtEidRegMoreSpecificWarningThreshold_Type = Unsigned32
_ClispExtEidRegMoreSpecificWarningThreshold_Object = MibScalar
clispExtEidRegMoreSpecificWarningThreshold = _ClispExtEidRegMoreSpecificWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 7, 1),
    _ClispExtEidRegMoreSpecificWarningThreshold_Type()
)
clispExtEidRegMoreSpecificWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtEidRegMoreSpecificWarningThreshold.setStatus("current")
_ClispExtEidRegMoreSpecificLimit_Type = Unsigned32
_ClispExtEidRegMoreSpecificLimit_Object = MibScalar
clispExtEidRegMoreSpecificLimit = _ClispExtEidRegMoreSpecificLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 7, 2),
    _ClispExtEidRegMoreSpecificLimit_Type()
)
clispExtEidRegMoreSpecificLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtEidRegMoreSpecificLimit.setStatus("current")
_ClispExtEidRegMoreSpecificCount_Type = Unsigned32
_ClispExtEidRegMoreSpecificCount_Object = MibScalar
clispExtEidRegMoreSpecificCount = _ClispExtEidRegMoreSpecificCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 1, 7, 3),
    _ClispExtEidRegMoreSpecificCount_Type()
)
clispExtEidRegMoreSpecificCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clispExtEidRegMoreSpecificCount.setStatus("current")
_CiscoLispExtConformance_ObjectIdentity = ObjectIdentity
ciscoLispExtConformance = _CiscoLispExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2)
)
_CiscoLispExtCompliances_ObjectIdentity = ObjectIdentity
ciscoLispExtCompliances = _CiscoLispExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 1)
)
_CiscoLispExtGroups_ObjectIdentity = ObjectIdentity
ciscoLispExtGroups = _CiscoLispExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2)
)
lispGlobalStatsEntry.registerAugmentions(
    ("CISCO-LISP-EXT-MIB",
     "clispExtGlobalStatsEntry")
)
clispExtGlobalStatsEntry.setIndexNames(*lispGlobalStatsEntry.getIndexNames())
lispFeaturesEntry.registerAugmentions(
    ("CISCO-LISP-EXT-MIB",
     "clispExtFeaturesEntry")
)
clispExtFeaturesEntry.setIndexNames(*lispFeaturesEntry.getIndexNames())

# Managed Objects groups

clispExtEidRegRlocMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 2)
)
clispExtEidRegRlocMembershipGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipMemberSince"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipGleaned"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegRlocMembershipConfigured"))
)
if mibBuilder.loadTexts:
    clispExtEidRegRlocMembershipGroup.setStatus("current")

clispExtRlocMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 3)
)
clispExtRlocMembershipGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtRlocMembershipMemberSince"),
        ("CISCO-LISP-EXT-MIB", "clispExtRlocMembershipDiscovered"),
        ("CISCO-LISP-EXT-MIB", "clispExtRlocMembershipConfigured"))
)
if mibBuilder.loadTexts:
    clispExtRlocMembershipGroup.setStatus("current")

clispExtReliableTransportSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 4)
)
clispExtReliableTransportSessionGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionState"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionLastStateChangeTime"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionEstablishmentRole"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionMessagesIn"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionMessagesOut"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionBytesIn"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionBytesOut"))
)
if mibBuilder.loadTexts:
    clispExtReliableTransportSessionGroup.setStatus("current")

clispExtGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 5)
)
clispExtGlobalStatsGroup.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtGlobalStatsEidRegMoreSpecificEntryCount")
)
if mibBuilder.loadTexts:
    clispExtGlobalStatsGroup.setStatus("current")

clispExtFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 6)
)
clispExtFeaturesGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtFeaturesEidRegMoreSpecificWarningThreshold"),
        ("CISCO-LISP-EXT-MIB", "clispExtFeaturesEidRegMoreSpecificLimit"),
        ("CISCO-LISP-EXT-MIB", "clispExtFeaturesMapCacheWarningThreshold"))
)
if mibBuilder.loadTexts:
    clispExtFeaturesGroup.setStatus("current")

clispExtNotificationSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 7)
)
clispExtNotificationSupportGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtEidRegFailureCause"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMapRequestDroppedCause"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificWarningThreshold"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificLimit"))
)
if mibBuilder.loadTexts:
    clispExtNotificationSupportGroup.setStatus("current")

clispExtEidRegMoreSpecificValuesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 8)
)
clispExtEidRegMoreSpecificValuesGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificWarningThreshold"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificLimit"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificCount"))
)
if mibBuilder.loadTexts:
    clispExtEidRegMoreSpecificValuesGroup.setStatus("current")


# Notification objects

clispExtUseMapResolverStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 1)
)
clispExtUseMapResolverStateChange.setObjects(
    ("LISP-MIB", "lispUseMapResolverState")
)
if mibBuilder.loadTexts:
    clispExtUseMapResolverStateChange.setStatus(
        "current"
    )

clispExtReliableTransportStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 2)
)
clispExtReliableTransportStateChange.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportSessionState")
)
if mibBuilder.loadTexts:
    clispExtReliableTransportStateChange.setStatus(
        "current"
    )

clispExtMappingDatabaseEidRegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 3)
)
clispExtMappingDatabaseEidRegFailure.setObjects(
      *(("LISP-MIB", "lispMappingDatabaseTimeStamp"),
        ("LISP-MIB", "lispUseMapServerState"))
)
if mibBuilder.loadTexts:
    clispExtMappingDatabaseEidRegFailure.setStatus(
        "current"
    )

clispExtUseMapServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 4)
)
clispExtUseMapServerStateChange.setObjects(
    ("LISP-MIB", "lispUseMapServerState")
)
if mibBuilder.loadTexts:
    clispExtUseMapServerStateChange.setStatus(
        "current"
    )

clispExtUseProxyEtrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 5)
)
clispExtUseProxyEtrStateChange.setObjects(
    ("LISP-MIB", "lispUseProxyEtrState")
)
if mibBuilder.loadTexts:
    clispExtUseProxyEtrStateChange.setStatus(
        "current"
    )

clispExtEidRegSiteAllRegistrationsExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 6)
)
clispExtEidRegSiteAllRegistrationsExpired.setObjects(
    ("LISP-MIB", "lispEidRegistrationSiteName")
)
if mibBuilder.loadTexts:
    clispExtEidRegSiteAllRegistrationsExpired.setStatus(
        "current"
    )

clispExtEidRegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 7)
)
clispExtEidRegFailure.setObjects(
      *(("LISP-MIB", "lispEidRegistrationSiteName"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegFailureCause"))
)
if mibBuilder.loadTexts:
    clispExtEidRegFailure.setStatus(
        "current"
    )

clispExtFeaturesEidRegMoreSpecificLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 8)
)
clispExtFeaturesEidRegMoreSpecificLimitReached.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtFeaturesEidRegMoreSpecificLimit")
)
if mibBuilder.loadTexts:
    clispExtFeaturesEidRegMoreSpecificLimitReached.setStatus(
        "current"
    )

clispExtFeaturesEidRegMoreSpecificWarningThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 9)
)
clispExtFeaturesEidRegMoreSpecificWarningThresholdReached.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtFeaturesEidRegMoreSpecificWarningThreshold")
)
if mibBuilder.loadTexts:
    clispExtFeaturesEidRegMoreSpecificWarningThresholdReached.setStatus(
        "current"
    )

clispExtEidRegMapRequestDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 10)
)
clispExtEidRegMapRequestDropped.setObjects(
      *(("LISP-MIB", "lispEidRegistrationSiteName"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMapRequestDroppedCause"))
)
if mibBuilder.loadTexts:
    clispExtEidRegMapRequestDropped.setStatus(
        "current"
    )

clispExtEidRegMoreSpecificLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 11)
)
clispExtEidRegMoreSpecificLimitReached.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificLimit")
)
if mibBuilder.loadTexts:
    clispExtEidRegMoreSpecificLimitReached.setStatus(
        "current"
    )

clispExtEidRegMoreSpecificWarningThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 12)
)
clispExtEidRegMoreSpecificWarningThresholdReached.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificWarningThreshold")
)
if mibBuilder.loadTexts:
    clispExtEidRegMoreSpecificWarningThresholdReached.setStatus(
        "current"
    )

clispExtFeaturesMapCacheLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 13)
)
clispExtFeaturesMapCacheLimitReached.setObjects(
    ("LISP-MIB", "lispFeaturesMapCacheLimit")
)
if mibBuilder.loadTexts:
    clispExtFeaturesMapCacheLimitReached.setStatus(
        "current"
    )

clispExtFeaturesMapCacheWarningThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 0, 14)
)
clispExtFeaturesMapCacheWarningThresholdReached.setObjects(
    ("CISCO-LISP-EXT-MIB", "clispExtFeaturesMapCacheWarningThreshold")
)
if mibBuilder.loadTexts:
    clispExtFeaturesMapCacheWarningThresholdReached.setStatus(
        "current"
    )


# Notifications groups

clispExtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 2, 1)
)
clispExtNotificationsGroup.setObjects(
      *(("CISCO-LISP-EXT-MIB", "clispExtUseMapResolverStateChange"),
        ("CISCO-LISP-EXT-MIB", "clispExtReliableTransportStateChange"),
        ("CISCO-LISP-EXT-MIB", "clispExtMappingDatabaseEidRegFailure"),
        ("CISCO-LISP-EXT-MIB", "clispExtUseMapServerStateChange"),
        ("CISCO-LISP-EXT-MIB", "clispExtUseProxyEtrStateChange"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegSiteAllRegistrationsExpired"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegFailure"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificLimitReached"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMoreSpecificWarningThresholdReached"),
        ("CISCO-LISP-EXT-MIB", "clispExtEidRegMapRequestDropped"),
        ("CISCO-LISP-EXT-MIB", "clispExtFeaturesEidRegMoreSpecificLimitReached"),
        ("CISCO-LISP-EXT-MIB", "clispExtFeaturesEidRegMoreSpecificWarningThresholdReached"),
        ("CISCO-LISP-EXT-MIB", "clispExtFeaturesMapCacheLimitReached"),
        ("CISCO-LISP-EXT-MIB", "clispExtFeaturesMapCacheWarningThresholdReached"))
)
if mibBuilder.loadTexts:
    clispExtNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLispExtMIBComplianceAll = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLispExtMIBComplianceAll.setStatus(
        "current"
    )

ciscoLispExtMIBComplianceMapServer = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 825, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLispExtMIBComplianceMapServer.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LISP-EXT-MIB",
    **{"ciscoLispExtMIB": ciscoLispExtMIB,
       "ciscoLispExtNotifications": ciscoLispExtNotifications,
       "clispExtUseMapResolverStateChange": clispExtUseMapResolverStateChange,
       "clispExtReliableTransportStateChange": clispExtReliableTransportStateChange,
       "clispExtMappingDatabaseEidRegFailure": clispExtMappingDatabaseEidRegFailure,
       "clispExtUseMapServerStateChange": clispExtUseMapServerStateChange,
       "clispExtUseProxyEtrStateChange": clispExtUseProxyEtrStateChange,
       "clispExtEidRegSiteAllRegistrationsExpired": clispExtEidRegSiteAllRegistrationsExpired,
       "clispExtEidRegFailure": clispExtEidRegFailure,
       "clispExtFeaturesEidRegMoreSpecificLimitReached": clispExtFeaturesEidRegMoreSpecificLimitReached,
       "clispExtFeaturesEidRegMoreSpecificWarningThresholdReached": clispExtFeaturesEidRegMoreSpecificWarningThresholdReached,
       "clispExtEidRegMapRequestDropped": clispExtEidRegMapRequestDropped,
       "clispExtEidRegMoreSpecificLimitReached": clispExtEidRegMoreSpecificLimitReached,
       "clispExtEidRegMoreSpecificWarningThresholdReached": clispExtEidRegMoreSpecificWarningThresholdReached,
       "clispExtFeaturesMapCacheLimitReached": clispExtFeaturesMapCacheLimitReached,
       "clispExtFeaturesMapCacheWarningThresholdReached": clispExtFeaturesMapCacheWarningThresholdReached,
       "ciscoLispExtObjects": ciscoLispExtObjects,
       "clispExtEidRegRlocMembershipTable": clispExtEidRegRlocMembershipTable,
       "clispExtEidRegRlocMembershipEntry": clispExtEidRegRlocMembershipEntry,
       "clispExtEidRegRlocMembershipInstanceID": clispExtEidRegRlocMembershipInstanceID,
       "clispExtEidRegRlocMembershipEidAfi": clispExtEidRegRlocMembershipEidAfi,
       "clispExtEidRegRlocMembershipRlocLength": clispExtEidRegRlocMembershipRlocLength,
       "clispExtEidRegRlocMembershipRloc": clispExtEidRegRlocMembershipRloc,
       "clispExtEidRegRlocMembershipMemberSince": clispExtEidRegRlocMembershipMemberSince,
       "clispExtEidRegRlocMembershipGleaned": clispExtEidRegRlocMembershipGleaned,
       "clispExtEidRegRlocMembershipConfigured": clispExtEidRegRlocMembershipConfigured,
       "clispExtRlocMembershipTable": clispExtRlocMembershipTable,
       "clispExtRlocMembershipEntry": clispExtRlocMembershipEntry,
       "clispExtRlocMembershipInstanceID": clispExtRlocMembershipInstanceID,
       "clispExtRlocMembershipEidAfi": clispExtRlocMembershipEidAfi,
       "clispExtRlocMembershipRlocLength": clispExtRlocMembershipRlocLength,
       "clispExtRlocMembershipRloc": clispExtRlocMembershipRloc,
       "clispExtRlocMembershipMemberSince": clispExtRlocMembershipMemberSince,
       "clispExtRlocMembershipDiscovered": clispExtRlocMembershipDiscovered,
       "clispExtRlocMembershipConfigured": clispExtRlocMembershipConfigured,
       "clispExtReliableTransportSessionTable": clispExtReliableTransportSessionTable,
       "clispExtReliableTransportSessionEntry": clispExtReliableTransportSessionEntry,
       "clispExtReliableTransportSessionPeerAddressLength": clispExtReliableTransportSessionPeerAddressLength,
       "clispExtReliableTransportSessionPeerAddress": clispExtReliableTransportSessionPeerAddress,
       "clispExtReliableTransportSessionPeerPort": clispExtReliableTransportSessionPeerPort,
       "clispExtReliableTransportSessionLocalAddressLength": clispExtReliableTransportSessionLocalAddressLength,
       "clispExtReliableTransportSessionLocalAddress": clispExtReliableTransportSessionLocalAddress,
       "clispExtReliableTransportSessionLocalPort": clispExtReliableTransportSessionLocalPort,
       "clispExtReliableTransportSessionState": clispExtReliableTransportSessionState,
       "clispExtReliableTransportSessionLastStateChangeTime": clispExtReliableTransportSessionLastStateChangeTime,
       "clispExtReliableTransportSessionEstablishmentRole": clispExtReliableTransportSessionEstablishmentRole,
       "clispExtReliableTransportSessionMessagesIn": clispExtReliableTransportSessionMessagesIn,
       "clispExtReliableTransportSessionMessagesOut": clispExtReliableTransportSessionMessagesOut,
       "clispExtReliableTransportSessionBytesIn": clispExtReliableTransportSessionBytesIn,
       "clispExtReliableTransportSessionBytesOut": clispExtReliableTransportSessionBytesOut,
       "clispExtGlobalStatsTable": clispExtGlobalStatsTable,
       "clispExtGlobalStatsEntry": clispExtGlobalStatsEntry,
       "clispExtGlobalStatsEidRegMoreSpecificEntryCount": clispExtGlobalStatsEidRegMoreSpecificEntryCount,
       "clispExtFeaturesTable": clispExtFeaturesTable,
       "clispExtFeaturesEntry": clispExtFeaturesEntry,
       "clispExtFeaturesEidRegMoreSpecificWarningThreshold": clispExtFeaturesEidRegMoreSpecificWarningThreshold,
       "clispExtFeaturesEidRegMoreSpecificLimit": clispExtFeaturesEidRegMoreSpecificLimit,
       "clispExtFeaturesMapCacheWarningThreshold": clispExtFeaturesMapCacheWarningThreshold,
       "clispExtNotificationObjects": clispExtNotificationObjects,
       "clispExtEidRegFailureCause": clispExtEidRegFailureCause,
       "clispExtEidRegMapRequestDroppedCause": clispExtEidRegMapRequestDroppedCause,
       "clispExtGlobalObjects": clispExtGlobalObjects,
       "clispExtEidRegMoreSpecificWarningThreshold": clispExtEidRegMoreSpecificWarningThreshold,
       "clispExtEidRegMoreSpecificLimit": clispExtEidRegMoreSpecificLimit,
       "clispExtEidRegMoreSpecificCount": clispExtEidRegMoreSpecificCount,
       "ciscoLispExtConformance": ciscoLispExtConformance,
       "ciscoLispExtCompliances": ciscoLispExtCompliances,
       "ciscoLispExtMIBComplianceAll": ciscoLispExtMIBComplianceAll,
       "ciscoLispExtMIBComplianceMapServer": ciscoLispExtMIBComplianceMapServer,
       "ciscoLispExtGroups": ciscoLispExtGroups,
       "clispExtNotificationsGroup": clispExtNotificationsGroup,
       "clispExtEidRegRlocMembershipGroup": clispExtEidRegRlocMembershipGroup,
       "clispExtRlocMembershipGroup": clispExtRlocMembershipGroup,
       "clispExtReliableTransportSessionGroup": clispExtReliableTransportSessionGroup,
       "clispExtGlobalStatsGroup": clispExtGlobalStatsGroup,
       "clispExtFeaturesGroup": clispExtFeaturesGroup,
       "clispExtNotificationSupportGroup": clispExtNotificationSupportGroup,
       "clispExtEidRegMoreSpecificValuesGroup": clispExtEidRegMoreSpecificValuesGroup}
)
