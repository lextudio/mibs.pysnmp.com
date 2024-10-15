# SNMP MIB module (DNS-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNS-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:08 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dnsServMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnsName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class DnsNameAsIndex(DnsName, TextualConvention):
    status = "current"


class DnsClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DnsType(Integer32, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DnsQClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DnsQType(Integer32, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DnsTime(Gauge32, TextualConvention):
    status = "current"
    displayHint = "4d"


class DnsOpCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class DnsRespCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



# MIB Managed Objects in the order of their OIDs

_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32)
)
if mibBuilder.loadTexts:
    dns.setStatus("current")
_DnsServMIBObjects_ObjectIdentity = ObjectIdentity
dnsServMIBObjects = _DnsServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 1)
)
_DnsServConfig_ObjectIdentity = ObjectIdentity
dnsServConfig = _DnsServConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 1)
)
_DnsServConfigImplementIdent_Type = DisplayString
_DnsServConfigImplementIdent_Object = MibScalar
dnsServConfigImplementIdent = _DnsServConfigImplementIdent_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 1),
    _DnsServConfigImplementIdent_Type()
)
dnsServConfigImplementIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServConfigImplementIdent.setStatus("current")


class _DnsServConfigRecurs_Type(Integer32):
    """Custom type dnsServConfigRecurs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("restricted", 2),
          ("unavailable", 3))
    )


_DnsServConfigRecurs_Type.__name__ = "Integer32"
_DnsServConfigRecurs_Object = MibScalar
dnsServConfigRecurs = _DnsServConfigRecurs_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 2),
    _DnsServConfigRecurs_Type()
)
dnsServConfigRecurs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServConfigRecurs.setStatus("current")
_DnsServConfigUpTime_Type = DnsTime
_DnsServConfigUpTime_Object = MibScalar
dnsServConfigUpTime = _DnsServConfigUpTime_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 3),
    _DnsServConfigUpTime_Type()
)
dnsServConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServConfigUpTime.setStatus("current")
_DnsServConfigResetTime_Type = DnsTime
_DnsServConfigResetTime_Object = MibScalar
dnsServConfigResetTime = _DnsServConfigResetTime_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 4),
    _DnsServConfigResetTime_Type()
)
dnsServConfigResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServConfigResetTime.setStatus("current")


class _DnsServConfigReset_Type(Integer32):
    """Custom type dnsServConfigReset based on Integer32"""
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
        *(("initializing", 3),
          ("other", 1),
          ("reset", 2),
          ("running", 4))
    )


_DnsServConfigReset_Type.__name__ = "Integer32"
_DnsServConfigReset_Object = MibScalar
dnsServConfigReset = _DnsServConfigReset_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 5),
    _DnsServConfigReset_Type()
)
dnsServConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServConfigReset.setStatus("current")
_DnsServCounter_ObjectIdentity = ObjectIdentity
dnsServCounter = _DnsServCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2)
)
_DnsServCounterAuthAns_Type = Counter32
_DnsServCounterAuthAns_Object = MibScalar
dnsServCounterAuthAns = _DnsServCounterAuthAns_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 2),
    _DnsServCounterAuthAns_Type()
)
dnsServCounterAuthAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterAuthAns.setStatus("current")
_DnsServCounterAuthNoNames_Type = Counter32
_DnsServCounterAuthNoNames_Object = MibScalar
dnsServCounterAuthNoNames = _DnsServCounterAuthNoNames_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 3),
    _DnsServCounterAuthNoNames_Type()
)
dnsServCounterAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterAuthNoNames.setStatus("current")
_DnsServCounterAuthNoDataResps_Type = Counter32
_DnsServCounterAuthNoDataResps_Object = MibScalar
dnsServCounterAuthNoDataResps = _DnsServCounterAuthNoDataResps_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 4),
    _DnsServCounterAuthNoDataResps_Type()
)
dnsServCounterAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterAuthNoDataResps.setStatus("current")
_DnsServCounterNonAuthDatas_Type = Counter32
_DnsServCounterNonAuthDatas_Object = MibScalar
dnsServCounterNonAuthDatas = _DnsServCounterNonAuthDatas_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 5),
    _DnsServCounterNonAuthDatas_Type()
)
dnsServCounterNonAuthDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterNonAuthDatas.setStatus("current")
_DnsServCounterNonAuthNoDatas_Type = Counter32
_DnsServCounterNonAuthNoDatas_Object = MibScalar
dnsServCounterNonAuthNoDatas = _DnsServCounterNonAuthNoDatas_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 6),
    _DnsServCounterNonAuthNoDatas_Type()
)
dnsServCounterNonAuthNoDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterNonAuthNoDatas.setStatus("current")
_DnsServCounterReferrals_Type = Counter32
_DnsServCounterReferrals_Object = MibScalar
dnsServCounterReferrals = _DnsServCounterReferrals_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 7),
    _DnsServCounterReferrals_Type()
)
dnsServCounterReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterReferrals.setStatus("current")
_DnsServCounterErrors_Type = Counter32
_DnsServCounterErrors_Object = MibScalar
dnsServCounterErrors = _DnsServCounterErrors_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 8),
    _DnsServCounterErrors_Type()
)
dnsServCounterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterErrors.setStatus("current")
_DnsServCounterRelNames_Type = Counter32
_DnsServCounterRelNames_Object = MibScalar
dnsServCounterRelNames = _DnsServCounterRelNames_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 9),
    _DnsServCounterRelNames_Type()
)
dnsServCounterRelNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterRelNames.setStatus("current")
_DnsServCounterReqRefusals_Type = Counter32
_DnsServCounterReqRefusals_Object = MibScalar
dnsServCounterReqRefusals = _DnsServCounterReqRefusals_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 10),
    _DnsServCounterReqRefusals_Type()
)
dnsServCounterReqRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterReqRefusals.setStatus("current")
_DnsServCounterReqUnparses_Type = Counter32
_DnsServCounterReqUnparses_Object = MibScalar
dnsServCounterReqUnparses = _DnsServCounterReqUnparses_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 11),
    _DnsServCounterReqUnparses_Type()
)
dnsServCounterReqUnparses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterReqUnparses.setStatus("current")
_DnsServCounterOtherErrors_Type = Counter32
_DnsServCounterOtherErrors_Object = MibScalar
dnsServCounterOtherErrors = _DnsServCounterOtherErrors_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 12),
    _DnsServCounterOtherErrors_Type()
)
dnsServCounterOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterOtherErrors.setStatus("current")
_DnsServCounterTable_Object = MibTable
dnsServCounterTable = _DnsServCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    dnsServCounterTable.setStatus("current")
_DnsServCounterEntry_Object = MibTableRow
dnsServCounterEntry = _DnsServCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1)
)
dnsServCounterEntry.setIndexNames(
    (0, "DNS-SERVER-MIB", "dnsServCounterOpCode"),
    (0, "DNS-SERVER-MIB", "dnsServCounterQClass"),
    (0, "DNS-SERVER-MIB", "dnsServCounterQType"),
    (0, "DNS-SERVER-MIB", "dnsServCounterTransport"),
)
if mibBuilder.loadTexts:
    dnsServCounterEntry.setStatus("current")
_DnsServCounterOpCode_Type = DnsOpCode
_DnsServCounterOpCode_Object = MibTableColumn
dnsServCounterOpCode = _DnsServCounterOpCode_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 1),
    _DnsServCounterOpCode_Type()
)
dnsServCounterOpCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServCounterOpCode.setStatus("current")
_DnsServCounterQClass_Type = DnsClass
_DnsServCounterQClass_Object = MibTableColumn
dnsServCounterQClass = _DnsServCounterQClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 2),
    _DnsServCounterQClass_Type()
)
dnsServCounterQClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServCounterQClass.setStatus("current")
_DnsServCounterQType_Type = DnsType
_DnsServCounterQType_Object = MibTableColumn
dnsServCounterQType = _DnsServCounterQType_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 3),
    _DnsServCounterQType_Type()
)
dnsServCounterQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServCounterQType.setStatus("current")


class _DnsServCounterTransport_Type(Integer32):
    """Custom type dnsServCounterTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("tcp", 2),
          ("udp", 1))
    )


_DnsServCounterTransport_Type.__name__ = "Integer32"
_DnsServCounterTransport_Object = MibTableColumn
dnsServCounterTransport = _DnsServCounterTransport_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 4),
    _DnsServCounterTransport_Type()
)
dnsServCounterTransport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServCounterTransport.setStatus("current")
_DnsServCounterRequests_Type = Counter32
_DnsServCounterRequests_Object = MibTableColumn
dnsServCounterRequests = _DnsServCounterRequests_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 5),
    _DnsServCounterRequests_Type()
)
dnsServCounterRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterRequests.setStatus("current")
_DnsServCounterResponses_Type = Counter32
_DnsServCounterResponses_Object = MibTableColumn
dnsServCounterResponses = _DnsServCounterResponses_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 6),
    _DnsServCounterResponses_Type()
)
dnsServCounterResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServCounterResponses.setStatus("current")
_DnsServOptCounter_ObjectIdentity = ObjectIdentity
dnsServOptCounter = _DnsServOptCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3)
)
_DnsServOptCounterSelfAuthAns_Type = Counter32
_DnsServOptCounterSelfAuthAns_Object = MibScalar
dnsServOptCounterSelfAuthAns = _DnsServOptCounterSelfAuthAns_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 1),
    _DnsServOptCounterSelfAuthAns_Type()
)
dnsServOptCounterSelfAuthAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfAuthAns.setStatus("current")
_DnsServOptCounterSelfAuthNoNames_Type = Counter32
_DnsServOptCounterSelfAuthNoNames_Object = MibScalar
dnsServOptCounterSelfAuthNoNames = _DnsServOptCounterSelfAuthNoNames_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 2),
    _DnsServOptCounterSelfAuthNoNames_Type()
)
dnsServOptCounterSelfAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfAuthNoNames.setStatus("current")
_DnsServOptCounterSelfAuthNoDataResps_Type = Counter32
_DnsServOptCounterSelfAuthNoDataResps_Object = MibScalar
dnsServOptCounterSelfAuthNoDataResps = _DnsServOptCounterSelfAuthNoDataResps_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 3),
    _DnsServOptCounterSelfAuthNoDataResps_Type()
)
dnsServOptCounterSelfAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfAuthNoDataResps.setStatus("current")
_DnsServOptCounterSelfNonAuthDatas_Type = Counter32
_DnsServOptCounterSelfNonAuthDatas_Object = MibScalar
dnsServOptCounterSelfNonAuthDatas = _DnsServOptCounterSelfNonAuthDatas_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 4),
    _DnsServOptCounterSelfNonAuthDatas_Type()
)
dnsServOptCounterSelfNonAuthDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfNonAuthDatas.setStatus("current")
_DnsServOptCounterSelfNonAuthNoDatas_Type = Counter32
_DnsServOptCounterSelfNonAuthNoDatas_Object = MibScalar
dnsServOptCounterSelfNonAuthNoDatas = _DnsServOptCounterSelfNonAuthNoDatas_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 5),
    _DnsServOptCounterSelfNonAuthNoDatas_Type()
)
dnsServOptCounterSelfNonAuthNoDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfNonAuthNoDatas.setStatus("current")
_DnsServOptCounterSelfReferrals_Type = Counter32
_DnsServOptCounterSelfReferrals_Object = MibScalar
dnsServOptCounterSelfReferrals = _DnsServOptCounterSelfReferrals_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 6),
    _DnsServOptCounterSelfReferrals_Type()
)
dnsServOptCounterSelfReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfReferrals.setStatus("current")
_DnsServOptCounterSelfErrors_Type = Counter32
_DnsServOptCounterSelfErrors_Object = MibScalar
dnsServOptCounterSelfErrors = _DnsServOptCounterSelfErrors_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 7),
    _DnsServOptCounterSelfErrors_Type()
)
dnsServOptCounterSelfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfErrors.setStatus("current")
_DnsServOptCounterSelfRelNames_Type = Counter32
_DnsServOptCounterSelfRelNames_Object = MibScalar
dnsServOptCounterSelfRelNames = _DnsServOptCounterSelfRelNames_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 8),
    _DnsServOptCounterSelfRelNames_Type()
)
dnsServOptCounterSelfRelNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfRelNames.setStatus("current")
_DnsServOptCounterSelfReqRefusals_Type = Counter32
_DnsServOptCounterSelfReqRefusals_Object = MibScalar
dnsServOptCounterSelfReqRefusals = _DnsServOptCounterSelfReqRefusals_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 9),
    _DnsServOptCounterSelfReqRefusals_Type()
)
dnsServOptCounterSelfReqRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfReqRefusals.setStatus("current")
_DnsServOptCounterSelfReqUnparses_Type = Counter32
_DnsServOptCounterSelfReqUnparses_Object = MibScalar
dnsServOptCounterSelfReqUnparses = _DnsServOptCounterSelfReqUnparses_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 10),
    _DnsServOptCounterSelfReqUnparses_Type()
)
dnsServOptCounterSelfReqUnparses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfReqUnparses.setStatus("current")
_DnsServOptCounterSelfOtherErrors_Type = Counter32
_DnsServOptCounterSelfOtherErrors_Object = MibScalar
dnsServOptCounterSelfOtherErrors = _DnsServOptCounterSelfOtherErrors_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 11),
    _DnsServOptCounterSelfOtherErrors_Type()
)
dnsServOptCounterSelfOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterSelfOtherErrors.setStatus("current")
_DnsServOptCounterFriendsAuthAns_Type = Counter32
_DnsServOptCounterFriendsAuthAns_Object = MibScalar
dnsServOptCounterFriendsAuthAns = _DnsServOptCounterFriendsAuthAns_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 12),
    _DnsServOptCounterFriendsAuthAns_Type()
)
dnsServOptCounterFriendsAuthAns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsAuthAns.setStatus("current")
_DnsServOptCounterFriendsAuthNoNames_Type = Counter32
_DnsServOptCounterFriendsAuthNoNames_Object = MibScalar
dnsServOptCounterFriendsAuthNoNames = _DnsServOptCounterFriendsAuthNoNames_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 13),
    _DnsServOptCounterFriendsAuthNoNames_Type()
)
dnsServOptCounterFriendsAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsAuthNoNames.setStatus("current")
_DnsServOptCounterFriendsAuthNoDataResps_Type = Counter32
_DnsServOptCounterFriendsAuthNoDataResps_Object = MibScalar
dnsServOptCounterFriendsAuthNoDataResps = _DnsServOptCounterFriendsAuthNoDataResps_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 14),
    _DnsServOptCounterFriendsAuthNoDataResps_Type()
)
dnsServOptCounterFriendsAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsAuthNoDataResps.setStatus("current")
_DnsServOptCounterFriendsNonAuthDatas_Type = Counter32
_DnsServOptCounterFriendsNonAuthDatas_Object = MibScalar
dnsServOptCounterFriendsNonAuthDatas = _DnsServOptCounterFriendsNonAuthDatas_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 15),
    _DnsServOptCounterFriendsNonAuthDatas_Type()
)
dnsServOptCounterFriendsNonAuthDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsNonAuthDatas.setStatus("current")
_DnsServOptCounterFriendsNonAuthNoDatas_Type = Counter32
_DnsServOptCounterFriendsNonAuthNoDatas_Object = MibScalar
dnsServOptCounterFriendsNonAuthNoDatas = _DnsServOptCounterFriendsNonAuthNoDatas_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 16),
    _DnsServOptCounterFriendsNonAuthNoDatas_Type()
)
dnsServOptCounterFriendsNonAuthNoDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsNonAuthNoDatas.setStatus("current")
_DnsServOptCounterFriendsReferrals_Type = Counter32
_DnsServOptCounterFriendsReferrals_Object = MibScalar
dnsServOptCounterFriendsReferrals = _DnsServOptCounterFriendsReferrals_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 17),
    _DnsServOptCounterFriendsReferrals_Type()
)
dnsServOptCounterFriendsReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsReferrals.setStatus("current")
_DnsServOptCounterFriendsErrors_Type = Counter32
_DnsServOptCounterFriendsErrors_Object = MibScalar
dnsServOptCounterFriendsErrors = _DnsServOptCounterFriendsErrors_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 18),
    _DnsServOptCounterFriendsErrors_Type()
)
dnsServOptCounterFriendsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsErrors.setStatus("current")
_DnsServOptCounterFriendsRelNames_Type = Counter32
_DnsServOptCounterFriendsRelNames_Object = MibScalar
dnsServOptCounterFriendsRelNames = _DnsServOptCounterFriendsRelNames_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 19),
    _DnsServOptCounterFriendsRelNames_Type()
)
dnsServOptCounterFriendsRelNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsRelNames.setStatus("current")
_DnsServOptCounterFriendsReqRefusals_Type = Counter32
_DnsServOptCounterFriendsReqRefusals_Object = MibScalar
dnsServOptCounterFriendsReqRefusals = _DnsServOptCounterFriendsReqRefusals_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 20),
    _DnsServOptCounterFriendsReqRefusals_Type()
)
dnsServOptCounterFriendsReqRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsReqRefusals.setStatus("current")
_DnsServOptCounterFriendsReqUnparses_Type = Counter32
_DnsServOptCounterFriendsReqUnparses_Object = MibScalar
dnsServOptCounterFriendsReqUnparses = _DnsServOptCounterFriendsReqUnparses_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 21),
    _DnsServOptCounterFriendsReqUnparses_Type()
)
dnsServOptCounterFriendsReqUnparses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsReqUnparses.setStatus("current")
_DnsServOptCounterFriendsOtherErrors_Type = Counter32
_DnsServOptCounterFriendsOtherErrors_Object = MibScalar
dnsServOptCounterFriendsOtherErrors = _DnsServOptCounterFriendsOtherErrors_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 22),
    _DnsServOptCounterFriendsOtherErrors_Type()
)
dnsServOptCounterFriendsOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServOptCounterFriendsOtherErrors.setStatus("current")
_DnsServZone_ObjectIdentity = ObjectIdentity
dnsServZone = _DnsServZone_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4)
)
_DnsServZoneTable_Object = MibTable
dnsServZoneTable = _DnsServZoneTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dnsServZoneTable.setStatus("current")
_DnsServZoneEntry_Object = MibTableRow
dnsServZoneEntry = _DnsServZoneEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1)
)
dnsServZoneEntry.setIndexNames(
    (0, "DNS-SERVER-MIB", "dnsServZoneName"),
    (0, "DNS-SERVER-MIB", "dnsServZoneClass"),
)
if mibBuilder.loadTexts:
    dnsServZoneEntry.setStatus("current")
_DnsServZoneName_Type = DnsNameAsIndex
_DnsServZoneName_Object = MibTableColumn
dnsServZoneName = _DnsServZoneName_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 1),
    _DnsServZoneName_Type()
)
dnsServZoneName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServZoneName.setStatus("current")
_DnsServZoneClass_Type = DnsClass
_DnsServZoneClass_Object = MibTableColumn
dnsServZoneClass = _DnsServZoneClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 2),
    _DnsServZoneClass_Type()
)
dnsServZoneClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServZoneClass.setStatus("current")
_DnsServZoneLastReloadSuccess_Type = DnsTime
_DnsServZoneLastReloadSuccess_Object = MibTableColumn
dnsServZoneLastReloadSuccess = _DnsServZoneLastReloadSuccess_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 3),
    _DnsServZoneLastReloadSuccess_Type()
)
dnsServZoneLastReloadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServZoneLastReloadSuccess.setStatus("current")
_DnsServZoneLastReloadAttempt_Type = DnsTime
_DnsServZoneLastReloadAttempt_Object = MibTableColumn
dnsServZoneLastReloadAttempt = _DnsServZoneLastReloadAttempt_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 4),
    _DnsServZoneLastReloadAttempt_Type()
)
dnsServZoneLastReloadAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServZoneLastReloadAttempt.setStatus("current")
_DnsServZoneLastSourceAttempt_Type = IpAddress
_DnsServZoneLastSourceAttempt_Object = MibTableColumn
dnsServZoneLastSourceAttempt = _DnsServZoneLastSourceAttempt_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 5),
    _DnsServZoneLastSourceAttempt_Type()
)
dnsServZoneLastSourceAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServZoneLastSourceAttempt.setStatus("current")
_DnsServZoneStatus_Type = RowStatus
_DnsServZoneStatus_Object = MibTableColumn
dnsServZoneStatus = _DnsServZoneStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 6),
    _DnsServZoneStatus_Type()
)
dnsServZoneStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsServZoneStatus.setStatus("current")
_DnsServZoneSerial_Type = Counter32
_DnsServZoneSerial_Object = MibTableColumn
dnsServZoneSerial = _DnsServZoneSerial_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 7),
    _DnsServZoneSerial_Type()
)
dnsServZoneSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServZoneSerial.setStatus("current")
_DnsServZoneCurrent_Type = TruthValue
_DnsServZoneCurrent_Object = MibTableColumn
dnsServZoneCurrent = _DnsServZoneCurrent_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 8),
    _DnsServZoneCurrent_Type()
)
dnsServZoneCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServZoneCurrent.setStatus("current")
_DnsServZoneLastSourceSuccess_Type = IpAddress
_DnsServZoneLastSourceSuccess_Object = MibTableColumn
dnsServZoneLastSourceSuccess = _DnsServZoneLastSourceSuccess_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 9),
    _DnsServZoneLastSourceSuccess_Type()
)
dnsServZoneLastSourceSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServZoneLastSourceSuccess.setStatus("current")
_DnsServZoneSrcTable_Object = MibTable
dnsServZoneSrcTable = _DnsServZoneSrcTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dnsServZoneSrcTable.setStatus("current")
_DnsServZoneSrcEntry_Object = MibTableRow
dnsServZoneSrcEntry = _DnsServZoneSrcEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1)
)
dnsServZoneSrcEntry.setIndexNames(
    (0, "DNS-SERVER-MIB", "dnsServZoneSrcName"),
    (0, "DNS-SERVER-MIB", "dnsServZoneSrcClass"),
    (0, "DNS-SERVER-MIB", "dnsServZoneSrcAddr"),
)
if mibBuilder.loadTexts:
    dnsServZoneSrcEntry.setStatus("current")
_DnsServZoneSrcName_Type = DnsNameAsIndex
_DnsServZoneSrcName_Object = MibTableColumn
dnsServZoneSrcName = _DnsServZoneSrcName_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 1),
    _DnsServZoneSrcName_Type()
)
dnsServZoneSrcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServZoneSrcName.setStatus("current")
_DnsServZoneSrcClass_Type = DnsClass
_DnsServZoneSrcClass_Object = MibTableColumn
dnsServZoneSrcClass = _DnsServZoneSrcClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 2),
    _DnsServZoneSrcClass_Type()
)
dnsServZoneSrcClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServZoneSrcClass.setStatus("current")
_DnsServZoneSrcAddr_Type = IpAddress
_DnsServZoneSrcAddr_Object = MibTableColumn
dnsServZoneSrcAddr = _DnsServZoneSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 3),
    _DnsServZoneSrcAddr_Type()
)
dnsServZoneSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsServZoneSrcAddr.setStatus("current")
_DnsServZoneSrcStatus_Type = RowStatus
_DnsServZoneSrcStatus_Object = MibTableColumn
dnsServZoneSrcStatus = _DnsServZoneSrcStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 4),
    _DnsServZoneSrcStatus_Type()
)
dnsServZoneSrcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsServZoneSrcStatus.setStatus("current")
_DnsServMIBGroups_ObjectIdentity = ObjectIdentity
dnsServMIBGroups = _DnsServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 2)
)
_DnsServMIBCompliances_ObjectIdentity = ObjectIdentity
dnsServMIBCompliances = _DnsServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 1, 3)
)

# Managed Objects groups

dnsServConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 1, 2, 1)
)
dnsServConfigGroup.setObjects(
      *(("DNS-SERVER-MIB", "dnsServConfigImplementIdent"),
        ("DNS-SERVER-MIB", "dnsServConfigRecurs"),
        ("DNS-SERVER-MIB", "dnsServConfigUpTime"),
        ("DNS-SERVER-MIB", "dnsServConfigResetTime"),
        ("DNS-SERVER-MIB", "dnsServConfigReset"))
)
if mibBuilder.loadTexts:
    dnsServConfigGroup.setStatus("current")

dnsServCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 1, 2, 2)
)
dnsServCounterGroup.setObjects(
      *(("DNS-SERVER-MIB", "dnsServCounterAuthAns"),
        ("DNS-SERVER-MIB", "dnsServCounterAuthNoNames"),
        ("DNS-SERVER-MIB", "dnsServCounterAuthNoDataResps"),
        ("DNS-SERVER-MIB", "dnsServCounterNonAuthDatas"),
        ("DNS-SERVER-MIB", "dnsServCounterNonAuthNoDatas"),
        ("DNS-SERVER-MIB", "dnsServCounterReferrals"),
        ("DNS-SERVER-MIB", "dnsServCounterErrors"),
        ("DNS-SERVER-MIB", "dnsServCounterRelNames"),
        ("DNS-SERVER-MIB", "dnsServCounterReqRefusals"),
        ("DNS-SERVER-MIB", "dnsServCounterReqUnparses"),
        ("DNS-SERVER-MIB", "dnsServCounterOtherErrors"),
        ("DNS-SERVER-MIB", "dnsServCounterOpCode"),
        ("DNS-SERVER-MIB", "dnsServCounterQClass"),
        ("DNS-SERVER-MIB", "dnsServCounterQType"),
        ("DNS-SERVER-MIB", "dnsServCounterTransport"),
        ("DNS-SERVER-MIB", "dnsServCounterRequests"),
        ("DNS-SERVER-MIB", "dnsServCounterResponses"))
)
if mibBuilder.loadTexts:
    dnsServCounterGroup.setStatus("current")

dnsServOptCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 1, 2, 3)
)
dnsServOptCounterGroup.setObjects(
      *(("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthAns"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoNames"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoDataResps"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthDatas"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthNoDatas"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfReferrals"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfErrors"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfRelNames"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqRefusals"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqUnparses"),
        ("DNS-SERVER-MIB", "dnsServOptCounterSelfOtherErrors"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthAns"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoNames"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoDataResps"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthDatas"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthNoDatas"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReferrals"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsErrors"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsRelNames"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqRefusals"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqUnparses"),
        ("DNS-SERVER-MIB", "dnsServOptCounterFriendsOtherErrors"))
)
if mibBuilder.loadTexts:
    dnsServOptCounterGroup.setStatus("current")

dnsServZoneGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 1, 2, 4)
)
dnsServZoneGroup.setObjects(
      *(("DNS-SERVER-MIB", "dnsServZoneName"),
        ("DNS-SERVER-MIB", "dnsServZoneClass"),
        ("DNS-SERVER-MIB", "dnsServZoneLastReloadSuccess"),
        ("DNS-SERVER-MIB", "dnsServZoneLastReloadAttempt"),
        ("DNS-SERVER-MIB", "dnsServZoneLastSourceAttempt"),
        ("DNS-SERVER-MIB", "dnsServZoneLastSourceSuccess"),
        ("DNS-SERVER-MIB", "dnsServZoneStatus"),
        ("DNS-SERVER-MIB", "dnsServZoneSerial"),
        ("DNS-SERVER-MIB", "dnsServZoneCurrent"),
        ("DNS-SERVER-MIB", "dnsServZoneSrcName"),
        ("DNS-SERVER-MIB", "dnsServZoneSrcClass"),
        ("DNS-SERVER-MIB", "dnsServZoneSrcAddr"),
        ("DNS-SERVER-MIB", "dnsServZoneSrcStatus"))
)
if mibBuilder.loadTexts:
    dnsServZoneGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dnsServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 32, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dnsServMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNS-SERVER-MIB",
    **{"DnsName": DnsName,
       "DnsNameAsIndex": DnsNameAsIndex,
       "DnsClass": DnsClass,
       "DnsType": DnsType,
       "DnsQClass": DnsQClass,
       "DnsQType": DnsQType,
       "DnsTime": DnsTime,
       "DnsOpCode": DnsOpCode,
       "DnsRespCode": DnsRespCode,
       "dns": dns,
       "dnsServMIB": dnsServMIB,
       "dnsServMIBObjects": dnsServMIBObjects,
       "dnsServConfig": dnsServConfig,
       "dnsServConfigImplementIdent": dnsServConfigImplementIdent,
       "dnsServConfigRecurs": dnsServConfigRecurs,
       "dnsServConfigUpTime": dnsServConfigUpTime,
       "dnsServConfigResetTime": dnsServConfigResetTime,
       "dnsServConfigReset": dnsServConfigReset,
       "dnsServCounter": dnsServCounter,
       "dnsServCounterAuthAns": dnsServCounterAuthAns,
       "dnsServCounterAuthNoNames": dnsServCounterAuthNoNames,
       "dnsServCounterAuthNoDataResps": dnsServCounterAuthNoDataResps,
       "dnsServCounterNonAuthDatas": dnsServCounterNonAuthDatas,
       "dnsServCounterNonAuthNoDatas": dnsServCounterNonAuthNoDatas,
       "dnsServCounterReferrals": dnsServCounterReferrals,
       "dnsServCounterErrors": dnsServCounterErrors,
       "dnsServCounterRelNames": dnsServCounterRelNames,
       "dnsServCounterReqRefusals": dnsServCounterReqRefusals,
       "dnsServCounterReqUnparses": dnsServCounterReqUnparses,
       "dnsServCounterOtherErrors": dnsServCounterOtherErrors,
       "dnsServCounterTable": dnsServCounterTable,
       "dnsServCounterEntry": dnsServCounterEntry,
       "dnsServCounterOpCode": dnsServCounterOpCode,
       "dnsServCounterQClass": dnsServCounterQClass,
       "dnsServCounterQType": dnsServCounterQType,
       "dnsServCounterTransport": dnsServCounterTransport,
       "dnsServCounterRequests": dnsServCounterRequests,
       "dnsServCounterResponses": dnsServCounterResponses,
       "dnsServOptCounter": dnsServOptCounter,
       "dnsServOptCounterSelfAuthAns": dnsServOptCounterSelfAuthAns,
       "dnsServOptCounterSelfAuthNoNames": dnsServOptCounterSelfAuthNoNames,
       "dnsServOptCounterSelfAuthNoDataResps": dnsServOptCounterSelfAuthNoDataResps,
       "dnsServOptCounterSelfNonAuthDatas": dnsServOptCounterSelfNonAuthDatas,
       "dnsServOptCounterSelfNonAuthNoDatas": dnsServOptCounterSelfNonAuthNoDatas,
       "dnsServOptCounterSelfReferrals": dnsServOptCounterSelfReferrals,
       "dnsServOptCounterSelfErrors": dnsServOptCounterSelfErrors,
       "dnsServOptCounterSelfRelNames": dnsServOptCounterSelfRelNames,
       "dnsServOptCounterSelfReqRefusals": dnsServOptCounterSelfReqRefusals,
       "dnsServOptCounterSelfReqUnparses": dnsServOptCounterSelfReqUnparses,
       "dnsServOptCounterSelfOtherErrors": dnsServOptCounterSelfOtherErrors,
       "dnsServOptCounterFriendsAuthAns": dnsServOptCounterFriendsAuthAns,
       "dnsServOptCounterFriendsAuthNoNames": dnsServOptCounterFriendsAuthNoNames,
       "dnsServOptCounterFriendsAuthNoDataResps": dnsServOptCounterFriendsAuthNoDataResps,
       "dnsServOptCounterFriendsNonAuthDatas": dnsServOptCounterFriendsNonAuthDatas,
       "dnsServOptCounterFriendsNonAuthNoDatas": dnsServOptCounterFriendsNonAuthNoDatas,
       "dnsServOptCounterFriendsReferrals": dnsServOptCounterFriendsReferrals,
       "dnsServOptCounterFriendsErrors": dnsServOptCounterFriendsErrors,
       "dnsServOptCounterFriendsRelNames": dnsServOptCounterFriendsRelNames,
       "dnsServOptCounterFriendsReqRefusals": dnsServOptCounterFriendsReqRefusals,
       "dnsServOptCounterFriendsReqUnparses": dnsServOptCounterFriendsReqUnparses,
       "dnsServOptCounterFriendsOtherErrors": dnsServOptCounterFriendsOtherErrors,
       "dnsServZone": dnsServZone,
       "dnsServZoneTable": dnsServZoneTable,
       "dnsServZoneEntry": dnsServZoneEntry,
       "dnsServZoneName": dnsServZoneName,
       "dnsServZoneClass": dnsServZoneClass,
       "dnsServZoneLastReloadSuccess": dnsServZoneLastReloadSuccess,
       "dnsServZoneLastReloadAttempt": dnsServZoneLastReloadAttempt,
       "dnsServZoneLastSourceAttempt": dnsServZoneLastSourceAttempt,
       "dnsServZoneStatus": dnsServZoneStatus,
       "dnsServZoneSerial": dnsServZoneSerial,
       "dnsServZoneCurrent": dnsServZoneCurrent,
       "dnsServZoneLastSourceSuccess": dnsServZoneLastSourceSuccess,
       "dnsServZoneSrcTable": dnsServZoneSrcTable,
       "dnsServZoneSrcEntry": dnsServZoneSrcEntry,
       "dnsServZoneSrcName": dnsServZoneSrcName,
       "dnsServZoneSrcClass": dnsServZoneSrcClass,
       "dnsServZoneSrcAddr": dnsServZoneSrcAddr,
       "dnsServZoneSrcStatus": dnsServZoneSrcStatus,
       "dnsServMIBGroups": dnsServMIBGroups,
       "dnsServConfigGroup": dnsServConfigGroup,
       "dnsServCounterGroup": dnsServCounterGroup,
       "dnsServOptCounterGroup": dnsServOptCounterGroup,
       "dnsServZoneGroup": dnsServZoneGroup,
       "dnsServMIBCompliances": dnsServMIBCompliances,
       "dnsServMIBCompliance": dnsServMIBCompliance}
)
