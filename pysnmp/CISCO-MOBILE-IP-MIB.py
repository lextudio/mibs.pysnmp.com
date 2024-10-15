# SNMP MIB module (CISCO-MOBILE-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MOBILE-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:47 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(RegistrationFlags,
 faCOAEntry,
 haMobilityBindingEntry,
 mnHAEntry,
 mnRegAgentAddress,
 mnRegCOA,
 mnRegistrationEntry,
 mnState) = mibBuilder.importSymbols(
    "MIP-MIB",
    "RegistrationFlags",
    "faCOAEntry",
    "haMobilityBindingEntry",
    "mnHAEntry",
    "mnRegAgentAddress",
    "mnRegCOA",
    "mnRegistrationEntry",
    "mnState")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoMobileIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174)
)
ciscoMobileIpMIB.setRevisions(
        ("2009-06-26 00:00",
         "2009-01-22 00:00",
         "2008-12-11 00:00",
         "2005-05-31 00:00",
         "2004-05-28 00:00",
         "2004-01-23 00:00",
         "2003-11-27 00:00",
         "2003-09-05 00:00",
         "2003-06-30 00:00",
         "2003-01-23 00:00",
         "2002-11-18 00:00",
         "2002-05-17 00:00",
         "2001-07-06 00:00",
         "2001-01-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmiRegistrationFlags(Bits, TextualConvention):
    status = "current"


class CmiEntityIdentifierType(Integer32, TextualConvention):
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
        *(("ipaddress", 2),
          ("nai", 3),
          ("other", 1))
    )



class CmiEntityIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class CmiSpi(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )



class CmiMultiPathMetricType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 2),
          ("hopcount", 1))
    )



class CmiTunnelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 2),
          ("ipinip", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMobileIpMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoMobileIpMIBNotifications = _CiscoMobileIpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 0)
)
_CiscoMobileIpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMobileIpMIBObjects = _CiscoMobileIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1)
)
_CmiFa_ObjectIdentity = ObjectIdentity
cmiFa = _CmiFa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1)
)
_CmiFaReg_ObjectIdentity = ObjectIdentity
cmiFaReg = _CmiFaReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1)
)
_CmiFaRegTotalVisitors_Type = Gauge32
_CmiFaRegTotalVisitors_Object = MibScalar
cmiFaRegTotalVisitors = _CmiFaRegTotalVisitors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 1),
    _CmiFaRegTotalVisitors_Type()
)
cmiFaRegTotalVisitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegTotalVisitors.setStatus("current")
_CmiFaRegVisitorTable_Object = MibTable
cmiFaRegVisitorTable = _CmiFaRegVisitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmiFaRegVisitorTable.setStatus("current")
_CmiFaRegVisitorEntry_Object = MibTableRow
cmiFaRegVisitorEntry = _CmiFaRegVisitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1)
)
cmiFaRegVisitorEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorIdentifierType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorIdentifier"),
)
if mibBuilder.loadTexts:
    cmiFaRegVisitorEntry.setStatus("current")
_CmiFaRegVisitorIdentifierType_Type = CmiEntityIdentifierType
_CmiFaRegVisitorIdentifierType_Object = MibTableColumn
cmiFaRegVisitorIdentifierType = _CmiFaRegVisitorIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 1),
    _CmiFaRegVisitorIdentifierType_Type()
)
cmiFaRegVisitorIdentifierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiFaRegVisitorIdentifierType.setStatus("current")
_CmiFaRegVisitorIdentifier_Type = CmiEntityIdentifier
_CmiFaRegVisitorIdentifier_Object = MibTableColumn
cmiFaRegVisitorIdentifier = _CmiFaRegVisitorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 2),
    _CmiFaRegVisitorIdentifier_Type()
)
cmiFaRegVisitorIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiFaRegVisitorIdentifier.setStatus("current")
_CmiFaRegVisitorHomeAddress_Type = IpAddress
_CmiFaRegVisitorHomeAddress_Object = MibTableColumn
cmiFaRegVisitorHomeAddress = _CmiFaRegVisitorHomeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 3),
    _CmiFaRegVisitorHomeAddress_Type()
)
cmiFaRegVisitorHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorHomeAddress.setStatus("current")
_CmiFaRegVisitorHomeAgentAddress_Type = IpAddress
_CmiFaRegVisitorHomeAgentAddress_Object = MibTableColumn
cmiFaRegVisitorHomeAgentAddress = _CmiFaRegVisitorHomeAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 4),
    _CmiFaRegVisitorHomeAgentAddress_Type()
)
cmiFaRegVisitorHomeAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorHomeAgentAddress.setStatus("current")
_CmiFaRegVisitorTimeGranted_Type = TimeInterval
_CmiFaRegVisitorTimeGranted_Object = MibTableColumn
cmiFaRegVisitorTimeGranted = _CmiFaRegVisitorTimeGranted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 5),
    _CmiFaRegVisitorTimeGranted_Type()
)
cmiFaRegVisitorTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorTimeGranted.setStatus("current")
_CmiFaRegVisitorTimeRemaining_Type = TimeInterval
_CmiFaRegVisitorTimeRemaining_Object = MibTableColumn
cmiFaRegVisitorTimeRemaining = _CmiFaRegVisitorTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 6),
    _CmiFaRegVisitorTimeRemaining_Type()
)
cmiFaRegVisitorTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorTimeRemaining.setStatus("current")
_CmiFaRegVisitorRegFlags_Type = RegistrationFlags
_CmiFaRegVisitorRegFlags_Object = MibTableColumn
cmiFaRegVisitorRegFlags = _CmiFaRegVisitorRegFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 7),
    _CmiFaRegVisitorRegFlags_Type()
)
cmiFaRegVisitorRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorRegFlags.setStatus("deprecated")


class _CmiFaRegVisitorRegIDLow_Type(Unsigned32):
    """Custom type cmiFaRegVisitorRegIDLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmiFaRegVisitorRegIDLow_Type.__name__ = "Unsigned32"
_CmiFaRegVisitorRegIDLow_Object = MibTableColumn
cmiFaRegVisitorRegIDLow = _CmiFaRegVisitorRegIDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 8),
    _CmiFaRegVisitorRegIDLow_Type()
)
cmiFaRegVisitorRegIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorRegIDLow.setStatus("current")


class _CmiFaRegVisitorRegIDHigh_Type(Unsigned32):
    """Custom type cmiFaRegVisitorRegIDHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmiFaRegVisitorRegIDHigh_Type.__name__ = "Unsigned32"
_CmiFaRegVisitorRegIDHigh_Object = MibTableColumn
cmiFaRegVisitorRegIDHigh = _CmiFaRegVisitorRegIDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 9),
    _CmiFaRegVisitorRegIDHigh_Type()
)
cmiFaRegVisitorRegIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorRegIDHigh.setStatus("current")
_CmiFaRegVisitorRegIsAccepted_Type = TruthValue
_CmiFaRegVisitorRegIsAccepted_Object = MibTableColumn
cmiFaRegVisitorRegIsAccepted = _CmiFaRegVisitorRegIsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 10),
    _CmiFaRegVisitorRegIsAccepted_Type()
)
cmiFaRegVisitorRegIsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorRegIsAccepted.setStatus("current")
_CmiFaRegVisitorRegFlagsRev1_Type = CmiRegistrationFlags
_CmiFaRegVisitorRegFlagsRev1_Object = MibTableColumn
cmiFaRegVisitorRegFlagsRev1 = _CmiFaRegVisitorRegFlagsRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 11),
    _CmiFaRegVisitorRegFlagsRev1_Type()
)
cmiFaRegVisitorRegFlagsRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorRegFlagsRev1.setStatus("current")


class _CmiFaRegVisitorChallengeValue_Type(OctetString):
    """Custom type cmiFaRegVisitorChallengeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_CmiFaRegVisitorChallengeValue_Type.__name__ = "OctetString"
_CmiFaRegVisitorChallengeValue_Object = MibTableColumn
cmiFaRegVisitorChallengeValue = _CmiFaRegVisitorChallengeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 2, 1, 12),
    _CmiFaRegVisitorChallengeValue_Type()
)
cmiFaRegVisitorChallengeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRegVisitorChallengeValue.setStatus("current")
_CmiFaInitRegRequestsReceived_Type = Counter32
_CmiFaInitRegRequestsReceived_Object = MibScalar
cmiFaInitRegRequestsReceived = _CmiFaInitRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 3),
    _CmiFaInitRegRequestsReceived_Type()
)
cmiFaInitRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaInitRegRequestsReceived.setStatus("current")
_CmiFaInitRegRequestsRelayed_Type = Counter32
_CmiFaInitRegRequestsRelayed_Object = MibScalar
cmiFaInitRegRequestsRelayed = _CmiFaInitRegRequestsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 4),
    _CmiFaInitRegRequestsRelayed_Type()
)
cmiFaInitRegRequestsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaInitRegRequestsRelayed.setStatus("current")
_CmiFaInitRegRequestsDenied_Type = Counter32
_CmiFaInitRegRequestsDenied_Object = MibScalar
cmiFaInitRegRequestsDenied = _CmiFaInitRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 5),
    _CmiFaInitRegRequestsDenied_Type()
)
cmiFaInitRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaInitRegRequestsDenied.setStatus("current")
_CmiFaInitRegRequestsDiscarded_Type = Counter32
_CmiFaInitRegRequestsDiscarded_Object = MibScalar
cmiFaInitRegRequestsDiscarded = _CmiFaInitRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 6),
    _CmiFaInitRegRequestsDiscarded_Type()
)
cmiFaInitRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaInitRegRequestsDiscarded.setStatus("current")
_CmiFaInitRegRepliesValidFromHA_Type = Counter32
_CmiFaInitRegRepliesValidFromHA_Object = MibScalar
cmiFaInitRegRepliesValidFromHA = _CmiFaInitRegRepliesValidFromHA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 7),
    _CmiFaInitRegRepliesValidFromHA_Type()
)
cmiFaInitRegRepliesValidFromHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaInitRegRepliesValidFromHA.setStatus("current")
_CmiFaInitRegRepliesValidRelayMN_Type = Counter32
_CmiFaInitRegRepliesValidRelayMN_Object = MibScalar
cmiFaInitRegRepliesValidRelayMN = _CmiFaInitRegRepliesValidRelayMN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 8),
    _CmiFaInitRegRepliesValidRelayMN_Type()
)
cmiFaInitRegRepliesValidRelayMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaInitRegRepliesValidRelayMN.setStatus("current")
_CmiFaReRegRequestsReceived_Type = Counter32
_CmiFaReRegRequestsReceived_Object = MibScalar
cmiFaReRegRequestsReceived = _CmiFaReRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 9),
    _CmiFaReRegRequestsReceived_Type()
)
cmiFaReRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReRegRequestsReceived.setStatus("current")
_CmiFaReRegRequestsRelayed_Type = Counter32
_CmiFaReRegRequestsRelayed_Object = MibScalar
cmiFaReRegRequestsRelayed = _CmiFaReRegRequestsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 10),
    _CmiFaReRegRequestsRelayed_Type()
)
cmiFaReRegRequestsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReRegRequestsRelayed.setStatus("current")
_CmiFaReRegRequestsDenied_Type = Counter32
_CmiFaReRegRequestsDenied_Object = MibScalar
cmiFaReRegRequestsDenied = _CmiFaReRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 11),
    _CmiFaReRegRequestsDenied_Type()
)
cmiFaReRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReRegRequestsDenied.setStatus("current")
_CmiFaReRegRequestsDiscarded_Type = Counter32
_CmiFaReRegRequestsDiscarded_Object = MibScalar
cmiFaReRegRequestsDiscarded = _CmiFaReRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 12),
    _CmiFaReRegRequestsDiscarded_Type()
)
cmiFaReRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReRegRequestsDiscarded.setStatus("current")
_CmiFaReRegRepliesValidFromHA_Type = Counter32
_CmiFaReRegRepliesValidFromHA_Object = MibScalar
cmiFaReRegRepliesValidFromHA = _CmiFaReRegRepliesValidFromHA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 13),
    _CmiFaReRegRepliesValidFromHA_Type()
)
cmiFaReRegRepliesValidFromHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReRegRepliesValidFromHA.setStatus("current")
_CmiFaReRegRepliesValidRelayToMN_Type = Counter32
_CmiFaReRegRepliesValidRelayToMN_Object = MibScalar
cmiFaReRegRepliesValidRelayToMN = _CmiFaReRegRepliesValidRelayToMN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 14),
    _CmiFaReRegRepliesValidRelayToMN_Type()
)
cmiFaReRegRepliesValidRelayToMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReRegRepliesValidRelayToMN.setStatus("current")
_CmiFaDeRegRequestsReceived_Type = Counter32
_CmiFaDeRegRequestsReceived_Object = MibScalar
cmiFaDeRegRequestsReceived = _CmiFaDeRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 15),
    _CmiFaDeRegRequestsReceived_Type()
)
cmiFaDeRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeRegRequestsReceived.setStatus("current")
_CmiFaDeRegRequestsRelayed_Type = Counter32
_CmiFaDeRegRequestsRelayed_Object = MibScalar
cmiFaDeRegRequestsRelayed = _CmiFaDeRegRequestsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 16),
    _CmiFaDeRegRequestsRelayed_Type()
)
cmiFaDeRegRequestsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeRegRequestsRelayed.setStatus("current")
_CmiFaDeRegRequestsDenied_Type = Counter32
_CmiFaDeRegRequestsDenied_Object = MibScalar
cmiFaDeRegRequestsDenied = _CmiFaDeRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 17),
    _CmiFaDeRegRequestsDenied_Type()
)
cmiFaDeRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeRegRequestsDenied.setStatus("current")
_CmiFaDeRegRequestsDiscarded_Type = Counter32
_CmiFaDeRegRequestsDiscarded_Object = MibScalar
cmiFaDeRegRequestsDiscarded = _CmiFaDeRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 18),
    _CmiFaDeRegRequestsDiscarded_Type()
)
cmiFaDeRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeRegRequestsDiscarded.setStatus("current")
_CmiFaDeRegRepliesValidFromHA_Type = Counter32
_CmiFaDeRegRepliesValidFromHA_Object = MibScalar
cmiFaDeRegRepliesValidFromHA = _CmiFaDeRegRepliesValidFromHA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 19),
    _CmiFaDeRegRepliesValidFromHA_Type()
)
cmiFaDeRegRepliesValidFromHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeRegRepliesValidFromHA.setStatus("current")
_CmiFaDeRegRepliesValidRelayToMN_Type = Counter32
_CmiFaDeRegRepliesValidRelayToMN_Object = MibScalar
cmiFaDeRegRepliesValidRelayToMN = _CmiFaDeRegRepliesValidRelayToMN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 20),
    _CmiFaDeRegRepliesValidRelayToMN_Type()
)
cmiFaDeRegRepliesValidRelayToMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeRegRepliesValidRelayToMN.setStatus("current")
_CmiFaReverseTunnelUnavailable_Type = Counter32
_CmiFaReverseTunnelUnavailable_Object = MibScalar
cmiFaReverseTunnelUnavailable = _CmiFaReverseTunnelUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 21),
    _CmiFaReverseTunnelUnavailable_Type()
)
cmiFaReverseTunnelUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReverseTunnelUnavailable.setStatus("current")
_CmiFaReverseTunnelBitNotSet_Type = Counter32
_CmiFaReverseTunnelBitNotSet_Object = MibScalar
cmiFaReverseTunnelBitNotSet = _CmiFaReverseTunnelBitNotSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 22),
    _CmiFaReverseTunnelBitNotSet_Type()
)
cmiFaReverseTunnelBitNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaReverseTunnelBitNotSet.setStatus("current")
_CmiFaMnTooDistant_Type = Counter32
_CmiFaMnTooDistant_Object = MibScalar
cmiFaMnTooDistant = _CmiFaMnTooDistant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 23),
    _CmiFaMnTooDistant_Type()
)
cmiFaMnTooDistant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaMnTooDistant.setStatus("current")
_CmiFaDeliveryStyleUnsupported_Type = Counter32
_CmiFaDeliveryStyleUnsupported_Object = MibScalar
cmiFaDeliveryStyleUnsupported = _CmiFaDeliveryStyleUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 24),
    _CmiFaDeliveryStyleUnsupported_Type()
)
cmiFaDeliveryStyleUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaDeliveryStyleUnsupported.setStatus("current")
_CmiFaUnknownChallenge_Type = Counter32
_CmiFaUnknownChallenge_Object = MibScalar
cmiFaUnknownChallenge = _CmiFaUnknownChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 25),
    _CmiFaUnknownChallenge_Type()
)
cmiFaUnknownChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaUnknownChallenge.setStatus("current")
_CmiFaMissingChallenge_Type = Counter32
_CmiFaMissingChallenge_Object = MibScalar
cmiFaMissingChallenge = _CmiFaMissingChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 26),
    _CmiFaMissingChallenge_Type()
)
cmiFaMissingChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaMissingChallenge.setStatus("current")
_CmiFaStaleChallenge_Type = Counter32
_CmiFaStaleChallenge_Object = MibScalar
cmiFaStaleChallenge = _CmiFaStaleChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 27),
    _CmiFaStaleChallenge_Type()
)
cmiFaStaleChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaStaleChallenge.setStatus("current")
_CmiFaCvsesFromMnRejected_Type = Counter32
_CmiFaCvsesFromMnRejected_Object = MibScalar
cmiFaCvsesFromMnRejected = _CmiFaCvsesFromMnRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 28),
    _CmiFaCvsesFromMnRejected_Type()
)
cmiFaCvsesFromMnRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaCvsesFromMnRejected.setStatus("current")
_CmiFaCvsesFromHaRejected_Type = Counter32
_CmiFaCvsesFromHaRejected_Object = MibScalar
cmiFaCvsesFromHaRejected = _CmiFaCvsesFromHaRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 29),
    _CmiFaCvsesFromHaRejected_Type()
)
cmiFaCvsesFromHaRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaCvsesFromHaRejected.setStatus("current")
_CmiFaNvsesFromMnNeglected_Type = Counter32
_CmiFaNvsesFromMnNeglected_Object = MibScalar
cmiFaNvsesFromMnNeglected = _CmiFaNvsesFromMnNeglected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 30),
    _CmiFaNvsesFromMnNeglected_Type()
)
cmiFaNvsesFromMnNeglected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaNvsesFromMnNeglected.setStatus("current")
_CmiFaNvsesFromHaNeglected_Type = Counter32
_CmiFaNvsesFromHaNeglected_Object = MibScalar
cmiFaNvsesFromHaNeglected = _CmiFaNvsesFromHaNeglected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 31),
    _CmiFaNvsesFromHaNeglected_Type()
)
cmiFaNvsesFromHaNeglected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaNvsesFromHaNeglected.setStatus("current")
_CmiFaTotalRegRequests_Type = Counter32
_CmiFaTotalRegRequests_Object = MibScalar
cmiFaTotalRegRequests = _CmiFaTotalRegRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 32),
    _CmiFaTotalRegRequests_Type()
)
cmiFaTotalRegRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaTotalRegRequests.setStatus("current")
_CmiFaTotalRegReplies_Type = Counter32
_CmiFaTotalRegReplies_Object = MibScalar
cmiFaTotalRegReplies = _CmiFaTotalRegReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 33),
    _CmiFaTotalRegReplies_Type()
)
cmiFaTotalRegReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaTotalRegReplies.setStatus("current")
_CmiFaMnFaAuthFailures_Type = Counter32
_CmiFaMnFaAuthFailures_Object = MibScalar
cmiFaMnFaAuthFailures = _CmiFaMnFaAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 34),
    _CmiFaMnFaAuthFailures_Type()
)
cmiFaMnFaAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaMnFaAuthFailures.setStatus("current")
_CmiFaMnAAAAuthFailures_Type = Counter32
_CmiFaMnAAAAuthFailures_Object = MibScalar
cmiFaMnAAAAuthFailures = _CmiFaMnAAAAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 1, 35),
    _CmiFaMnAAAAuthFailures_Type()
)
cmiFaMnAAAAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaMnAAAAuthFailures.setStatus("current")
_CmiFaAdvertisement_ObjectIdentity = ObjectIdentity
cmiFaAdvertisement = _CmiFaAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2)
)
_CmiFaAdvertConfTable_Object = MibTable
cmiFaAdvertConfTable = _CmiFaAdvertConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmiFaAdvertConfTable.setStatus("current")
_CmiFaAdvertConfEntry_Object = MibTableRow
cmiFaAdvertConfEntry = _CmiFaAdvertConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 1, 1)
)
cmiFaAdvertConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmiFaAdvertConfEntry.setStatus("current")
_CmiFaAdvertIsBusy_Type = TruthValue
_CmiFaAdvertIsBusy_Object = MibTableColumn
cmiFaAdvertIsBusy = _CmiFaAdvertIsBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 1, 1, 1),
    _CmiFaAdvertIsBusy_Type()
)
cmiFaAdvertIsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaAdvertIsBusy.setStatus("current")


class _CmiFaAdvertRegRequired_Type(TruthValue):
    """Custom type cmiFaAdvertRegRequired based on TruthValue"""


_CmiFaAdvertRegRequired_Object = MibTableColumn
cmiFaAdvertRegRequired = _CmiFaAdvertRegRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 1, 1, 2),
    _CmiFaAdvertRegRequired_Type()
)
cmiFaAdvertRegRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiFaAdvertRegRequired.setStatus("current")


class _CmiFaAdvertChallengeWindow_Type(Unsigned32):
    """Custom type cmiFaAdvertChallengeWindow based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmiFaAdvertChallengeWindow_Type.__name__ = "Unsigned32"
_CmiFaAdvertChallengeWindow_Object = MibTableColumn
cmiFaAdvertChallengeWindow = _CmiFaAdvertChallengeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 1, 1, 3),
    _CmiFaAdvertChallengeWindow_Type()
)
cmiFaAdvertChallengeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiFaAdvertChallengeWindow.setStatus("current")
_CmiFaAdvertChallengeTable_Object = MibTable
cmiFaAdvertChallengeTable = _CmiFaAdvertChallengeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmiFaAdvertChallengeTable.setStatus("current")
_CmiFaAdvertChallengeEntry_Object = MibTableRow
cmiFaAdvertChallengeEntry = _CmiFaAdvertChallengeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 2, 1)
)
cmiFaAdvertChallengeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiFaAdvertChallengeIndex"),
)
if mibBuilder.loadTexts:
    cmiFaAdvertChallengeEntry.setStatus("current")


class _CmiFaAdvertChallengeIndex_Type(Unsigned32):
    """Custom type cmiFaAdvertChallengeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmiFaAdvertChallengeIndex_Type.__name__ = "Unsigned32"
_CmiFaAdvertChallengeIndex_Object = MibTableColumn
cmiFaAdvertChallengeIndex = _CmiFaAdvertChallengeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 2, 1, 1),
    _CmiFaAdvertChallengeIndex_Type()
)
cmiFaAdvertChallengeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiFaAdvertChallengeIndex.setStatus("current")


class _CmiFaAdvertChallengeValue_Type(OctetString):
    """Custom type cmiFaAdvertChallengeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_CmiFaAdvertChallengeValue_Type.__name__ = "OctetString"
_CmiFaAdvertChallengeValue_Object = MibTableColumn
cmiFaAdvertChallengeValue = _CmiFaAdvertChallengeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 2, 2, 1, 2),
    _CmiFaAdvertChallengeValue_Type()
)
cmiFaAdvertChallengeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaAdvertChallengeValue.setStatus("current")
_CmiFaSystem_ObjectIdentity = ObjectIdentity
cmiFaSystem = _CmiFaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3)
)


class _CmiFaRevTunnelSupported_Type(TruthValue):
    """Custom type cmiFaRevTunnelSupported based on TruthValue"""


_CmiFaRevTunnelSupported_Object = MibScalar
cmiFaRevTunnelSupported = _CmiFaRevTunnelSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 1),
    _CmiFaRevTunnelSupported_Type()
)
cmiFaRevTunnelSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaRevTunnelSupported.setStatus("current")


class _CmiFaChallengeSupported_Type(TruthValue):
    """Custom type cmiFaChallengeSupported based on TruthValue"""


_CmiFaChallengeSupported_Object = MibScalar
cmiFaChallengeSupported = _CmiFaChallengeSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 2),
    _CmiFaChallengeSupported_Type()
)
cmiFaChallengeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaChallengeSupported.setStatus("current")


class _CmiFaEncapDeliveryStyleSupported_Type(TruthValue):
    """Custom type cmiFaEncapDeliveryStyleSupported based on TruthValue"""


_CmiFaEncapDeliveryStyleSupported_Object = MibScalar
cmiFaEncapDeliveryStyleSupported = _CmiFaEncapDeliveryStyleSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 3),
    _CmiFaEncapDeliveryStyleSupported_Type()
)
cmiFaEncapDeliveryStyleSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaEncapDeliveryStyleSupported.setStatus("current")
_CmiFaInterfaceTable_Object = MibTable
cmiFaInterfaceTable = _CmiFaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cmiFaInterfaceTable.setStatus("current")
_CmiFaInterfaceEntry_Object = MibTableRow
cmiFaInterfaceEntry = _CmiFaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 4, 1)
)
cmiFaInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmiFaInterfaceEntry.setStatus("current")


class _CmiFaReverseTunnelEnable_Type(TruthValue):
    """Custom type cmiFaReverseTunnelEnable based on TruthValue"""


_CmiFaReverseTunnelEnable_Object = MibTableColumn
cmiFaReverseTunnelEnable = _CmiFaReverseTunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 4, 1, 1),
    _CmiFaReverseTunnelEnable_Type()
)
cmiFaReverseTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiFaReverseTunnelEnable.setStatus("current")


class _CmiFaChallengeEnable_Type(TruthValue):
    """Custom type cmiFaChallengeEnable based on TruthValue"""


_CmiFaChallengeEnable_Object = MibTableColumn
cmiFaChallengeEnable = _CmiFaChallengeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 4, 1, 2),
    _CmiFaChallengeEnable_Type()
)
cmiFaChallengeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiFaChallengeEnable.setStatus("current")


class _CmiFaAdvertChallengeChapSPI_Type(Unsigned32):
    """Custom type cmiFaAdvertChallengeChapSPI based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CmiFaAdvertChallengeChapSPI_Type.__name__ = "Unsigned32"
_CmiFaAdvertChallengeChapSPI_Object = MibTableColumn
cmiFaAdvertChallengeChapSPI = _CmiFaAdvertChallengeChapSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 4, 1, 3),
    _CmiFaAdvertChallengeChapSPI_Type()
)
cmiFaAdvertChallengeChapSPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiFaAdvertChallengeChapSPI.setStatus("current")
_CmiFaCoaTable_Object = MibTable
cmiFaCoaTable = _CmiFaCoaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cmiFaCoaTable.setStatus("current")
_CmiFaCoaEntry_Object = MibTableRow
cmiFaCoaEntry = _CmiFaCoaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cmiFaCoaEntry.setStatus("current")


class _CmiFaCoaInterfaceOnly_Type(TruthValue):
    """Custom type cmiFaCoaInterfaceOnly based on TruthValue"""


_CmiFaCoaInterfaceOnly_Object = MibTableColumn
cmiFaCoaInterfaceOnly = _CmiFaCoaInterfaceOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 5, 1, 1),
    _CmiFaCoaInterfaceOnly_Type()
)
cmiFaCoaInterfaceOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiFaCoaInterfaceOnly.setStatus("current")


class _CmiFaCoaTransmitOnly_Type(TruthValue):
    """Custom type cmiFaCoaTransmitOnly based on TruthValue"""


_CmiFaCoaTransmitOnly_Object = MibTableColumn
cmiFaCoaTransmitOnly = _CmiFaCoaTransmitOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 5, 1, 2),
    _CmiFaCoaTransmitOnly_Type()
)
cmiFaCoaTransmitOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiFaCoaTransmitOnly.setStatus("current")
_CmiFaCoaRegAsymLink_Type = ZeroBasedCounter32
_CmiFaCoaRegAsymLink_Object = MibTableColumn
cmiFaCoaRegAsymLink = _CmiFaCoaRegAsymLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 1, 3, 5, 1, 3),
    _CmiFaCoaRegAsymLink_Type()
)
cmiFaCoaRegAsymLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiFaCoaRegAsymLink.setStatus("current")
_CmiHa_ObjectIdentity = ObjectIdentity
cmiHa = _CmiHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2)
)
_CmiHaReg_ObjectIdentity = ObjectIdentity
cmiHaReg = _CmiHaReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1)
)
_CmiHaRegTotalMobilityBindings_Type = Gauge32
_CmiHaRegTotalMobilityBindings_Object = MibScalar
cmiHaRegTotalMobilityBindings = _CmiHaRegTotalMobilityBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 1),
    _CmiHaRegTotalMobilityBindings_Type()
)
cmiHaRegTotalMobilityBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTotalMobilityBindings.setStatus("current")
_CmiHaRegMobilityBindingTable_Object = MibTable
cmiHaRegMobilityBindingTable = _CmiHaRegMobilityBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cmiHaRegMobilityBindingTable.setStatus("current")
_CmiHaRegMobilityBindingEntry_Object = MibTableRow
cmiHaRegMobilityBindingEntry = _CmiHaRegMobilityBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmiHaRegMobilityBindingEntry.setStatus("current")
_CmiHaRegMnIdentifierType_Type = CmiEntityIdentifierType
_CmiHaRegMnIdentifierType_Object = MibTableColumn
cmiHaRegMnIdentifierType = _CmiHaRegMnIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 1),
    _CmiHaRegMnIdentifierType_Type()
)
cmiHaRegMnIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMnIdentifierType.setStatus("current")
_CmiHaRegMnIdentifier_Type = CmiEntityIdentifier
_CmiHaRegMnIdentifier_Object = MibTableColumn
cmiHaRegMnIdentifier = _CmiHaRegMnIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 2),
    _CmiHaRegMnIdentifier_Type()
)
cmiHaRegMnIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMnIdentifier.setStatus("current")
_CmiHaRegMobilityBindingRegFlags_Type = CmiRegistrationFlags
_CmiHaRegMobilityBindingRegFlags_Object = MibTableColumn
cmiHaRegMobilityBindingRegFlags = _CmiHaRegMobilityBindingRegFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 3),
    _CmiHaRegMobilityBindingRegFlags_Type()
)
cmiHaRegMobilityBindingRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMobilityBindingRegFlags.setStatus("current")
_CmiHaRegMnIfDescription_Type = SnmpAdminString
_CmiHaRegMnIfDescription_Object = MibTableColumn
cmiHaRegMnIfDescription = _CmiHaRegMnIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 4),
    _CmiHaRegMnIfDescription_Type()
)
cmiHaRegMnIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMnIfDescription.setStatus("current")
_CmiHaRegMnIfBandwidth_Type = Unsigned32
_CmiHaRegMnIfBandwidth_Object = MibTableColumn
cmiHaRegMnIfBandwidth = _CmiHaRegMnIfBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 5),
    _CmiHaRegMnIfBandwidth_Type()
)
cmiHaRegMnIfBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMnIfBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegMnIfBandwidth.setUnits("kilobits/second")
_CmiHaRegMnIfID_Type = Unsigned32
_CmiHaRegMnIfID_Object = MibTableColumn
cmiHaRegMnIfID = _CmiHaRegMnIfID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 6),
    _CmiHaRegMnIfID_Type()
)
cmiHaRegMnIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMnIfID.setStatus("current")
_CmiHaRegMnIfPathMetricType_Type = CmiMultiPathMetricType
_CmiHaRegMnIfPathMetricType_Object = MibTableColumn
cmiHaRegMnIfPathMetricType = _CmiHaRegMnIfPathMetricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 7),
    _CmiHaRegMnIfPathMetricType_Type()
)
cmiHaRegMnIfPathMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMnIfPathMetricType.setStatus("current")
_CmiHaRegMobilityBindingMacAddress_Type = MacAddress
_CmiHaRegMobilityBindingMacAddress_Object = MibTableColumn
cmiHaRegMobilityBindingMacAddress = _CmiHaRegMobilityBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 2, 1, 8),
    _CmiHaRegMobilityBindingMacAddress_Type()
)
cmiHaRegMobilityBindingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMobilityBindingMacAddress.setStatus("current")
_CmiHaRegCounterTable_Object = MibTable
cmiHaRegCounterTable = _CmiHaRegCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cmiHaRegCounterTable.setStatus("current")
_CmiHaRegCounterEntry_Object = MibTableRow
cmiHaRegCounterEntry = _CmiHaRegCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1)
)
cmiHaRegCounterEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaRegMnId"),
)
if mibBuilder.loadTexts:
    cmiHaRegCounterEntry.setStatus("current")
_CmiHaRegMnIdType_Type = CmiEntityIdentifierType
_CmiHaRegMnIdType_Object = MibTableColumn
cmiHaRegMnIdType = _CmiHaRegMnIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 1),
    _CmiHaRegMnIdType_Type()
)
cmiHaRegMnIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaRegMnIdType.setStatus("current")
_CmiHaRegMnId_Type = CmiEntityIdentifier
_CmiHaRegMnId_Object = MibTableColumn
cmiHaRegMnId = _CmiHaRegMnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 2),
    _CmiHaRegMnId_Type()
)
cmiHaRegMnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaRegMnId.setStatus("current")
_CmiHaRegServAcceptedRequests_Type = Counter32
_CmiHaRegServAcceptedRequests_Object = MibTableColumn
cmiHaRegServAcceptedRequests = _CmiHaRegServAcceptedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 3),
    _CmiHaRegServAcceptedRequests_Type()
)
cmiHaRegServAcceptedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegServAcceptedRequests.setStatus("current")
_CmiHaRegServDeniedRequests_Type = Counter32
_CmiHaRegServDeniedRequests_Object = MibTableColumn
cmiHaRegServDeniedRequests = _CmiHaRegServDeniedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 4),
    _CmiHaRegServDeniedRequests_Type()
)
cmiHaRegServDeniedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegServDeniedRequests.setStatus("current")
_CmiHaRegOverallServTime_Type = TimeInterval
_CmiHaRegOverallServTime_Object = MibTableColumn
cmiHaRegOverallServTime = _CmiHaRegOverallServTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 5),
    _CmiHaRegOverallServTime_Type()
)
cmiHaRegOverallServTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegOverallServTime.setStatus("current")
_CmiHaRegRecentServAcceptedTime_Type = TimeStamp
_CmiHaRegRecentServAcceptedTime_Object = MibTableColumn
cmiHaRegRecentServAcceptedTime = _CmiHaRegRecentServAcceptedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 6),
    _CmiHaRegRecentServAcceptedTime_Type()
)
cmiHaRegRecentServAcceptedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegRecentServAcceptedTime.setStatus("current")
_CmiHaRegRecentServDeniedTime_Type = TimeStamp
_CmiHaRegRecentServDeniedTime_Object = MibTableColumn
cmiHaRegRecentServDeniedTime = _CmiHaRegRecentServDeniedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 7),
    _CmiHaRegRecentServDeniedTime_Type()
)
cmiHaRegRecentServDeniedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegRecentServDeniedTime.setStatus("current")


class _CmiHaRegRecentServDeniedCode_Type(Integer32):
    """Custom type cmiHaRegRecentServDeniedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139)
        )
    )
    namedValues = NamedValues(
        *(("admProhibited", 129),
          ("encapsulationUnavailable", 139),
          ("faAuthenticationFailure", 132),
          ("idMismatch", 133),
          ("insufficientResource", 130),
          ("mnAuthenticationFailure", 131),
          ("poorlyFormedRequest", 134),
          ("reasonUnspecified", 128),
          ("reverseTunnelBitNotSet", 138),
          ("reverseTunnelUnavailable", 137),
          ("tooManyBindings", 135),
          ("unknownHA", 136))
    )


_CmiHaRegRecentServDeniedCode_Type.__name__ = "Integer32"
_CmiHaRegRecentServDeniedCode_Object = MibTableColumn
cmiHaRegRecentServDeniedCode = _CmiHaRegRecentServDeniedCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 3, 1, 8),
    _CmiHaRegRecentServDeniedCode_Type()
)
cmiHaRegRecentServDeniedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegRecentServDeniedCode.setStatus("current")
_CmiHaRegTotalProcLocRegs_Type = Counter32
_CmiHaRegTotalProcLocRegs_Object = MibScalar
cmiHaRegTotalProcLocRegs = _CmiHaRegTotalProcLocRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 4),
    _CmiHaRegTotalProcLocRegs_Type()
)
cmiHaRegTotalProcLocRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTotalProcLocRegs.setStatus("current")
_CmiHaRegMaxProcLocInMinRegs_Type = Counter32
_CmiHaRegMaxProcLocInMinRegs_Object = MibScalar
cmiHaRegMaxProcLocInMinRegs = _CmiHaRegMaxProcLocInMinRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 5),
    _CmiHaRegMaxProcLocInMinRegs_Type()
)
cmiHaRegMaxProcLocInMinRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMaxProcLocInMinRegs.setStatus("current")
_CmiHaRegDateMaxRegsProcLoc_Type = DateAndTime
_CmiHaRegDateMaxRegsProcLoc_Object = MibScalar
cmiHaRegDateMaxRegsProcLoc = _CmiHaRegDateMaxRegsProcLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 6),
    _CmiHaRegDateMaxRegsProcLoc_Type()
)
cmiHaRegDateMaxRegsProcLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegDateMaxRegsProcLoc.setStatus("current")
_CmiHaRegProcLocInLastMinRegs_Type = Counter32
_CmiHaRegProcLocInLastMinRegs_Object = MibScalar
cmiHaRegProcLocInLastMinRegs = _CmiHaRegProcLocInLastMinRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 7),
    _CmiHaRegProcLocInLastMinRegs_Type()
)
cmiHaRegProcLocInLastMinRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegProcLocInLastMinRegs.setStatus("current")
_CmiHaRegTotalProcByAAARegs_Type = Counter32
_CmiHaRegTotalProcByAAARegs_Object = MibScalar
cmiHaRegTotalProcByAAARegs = _CmiHaRegTotalProcByAAARegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 8),
    _CmiHaRegTotalProcByAAARegs_Type()
)
cmiHaRegTotalProcByAAARegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTotalProcByAAARegs.setStatus("current")
_CmiHaRegMaxProcByAAAInMinRegs_Type = Counter32
_CmiHaRegMaxProcByAAAInMinRegs_Object = MibScalar
cmiHaRegMaxProcByAAAInMinRegs = _CmiHaRegMaxProcByAAAInMinRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 9),
    _CmiHaRegMaxProcByAAAInMinRegs_Type()
)
cmiHaRegMaxProcByAAAInMinRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMaxProcByAAAInMinRegs.setStatus("current")
_CmiHaRegDateMaxRegsProcByAAA_Type = DateAndTime
_CmiHaRegDateMaxRegsProcByAAA_Object = MibScalar
cmiHaRegDateMaxRegsProcByAAA = _CmiHaRegDateMaxRegsProcByAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 10),
    _CmiHaRegDateMaxRegsProcByAAA_Type()
)
cmiHaRegDateMaxRegsProcByAAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegDateMaxRegsProcByAAA.setStatus("current")
_CmiHaRegProcAAAInLastByMinRegs_Type = Counter32
_CmiHaRegProcAAAInLastByMinRegs_Object = MibScalar
cmiHaRegProcAAAInLastByMinRegs = _CmiHaRegProcAAAInLastByMinRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 11),
    _CmiHaRegProcAAAInLastByMinRegs_Type()
)
cmiHaRegProcAAAInLastByMinRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegProcAAAInLastByMinRegs.setStatus("current")


class _CmiHaRegAvgTimeRegsProcByAAA_Type(Integer32):
    """Custom type cmiHaRegAvgTimeRegsProcByAAA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmiHaRegAvgTimeRegsProcByAAA_Type.__name__ = "Integer32"
_CmiHaRegAvgTimeRegsProcByAAA_Object = MibScalar
cmiHaRegAvgTimeRegsProcByAAA = _CmiHaRegAvgTimeRegsProcByAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 12),
    _CmiHaRegAvgTimeRegsProcByAAA_Type()
)
cmiHaRegAvgTimeRegsProcByAAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegAvgTimeRegsProcByAAA.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegAvgTimeRegsProcByAAA.setUnits("milli seconds")


class _CmiHaRegMaxTimeRegsProcByAAA_Type(Integer32):
    """Custom type cmiHaRegMaxTimeRegsProcByAAA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmiHaRegMaxTimeRegsProcByAAA_Type.__name__ = "Integer32"
_CmiHaRegMaxTimeRegsProcByAAA_Object = MibScalar
cmiHaRegMaxTimeRegsProcByAAA = _CmiHaRegMaxTimeRegsProcByAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 13),
    _CmiHaRegMaxTimeRegsProcByAAA_Type()
)
cmiHaRegMaxTimeRegsProcByAAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegMaxTimeRegsProcByAAA.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegMaxTimeRegsProcByAAA.setUnits("milli seconds")
_CmiHaRegRequestsReceived_Type = Counter32
_CmiHaRegRequestsReceived_Object = MibScalar
cmiHaRegRequestsReceived = _CmiHaRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 14),
    _CmiHaRegRequestsReceived_Type()
)
cmiHaRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegRequestsReceived.setStatus("current")
_CmiHaRegRequestsDenied_Type = Counter32
_CmiHaRegRequestsDenied_Object = MibScalar
cmiHaRegRequestsDenied = _CmiHaRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 15),
    _CmiHaRegRequestsDenied_Type()
)
cmiHaRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegRequestsDenied.setStatus("current")
_CmiHaRegRequestsDiscarded_Type = Counter32
_CmiHaRegRequestsDiscarded_Object = MibScalar
cmiHaRegRequestsDiscarded = _CmiHaRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 16),
    _CmiHaRegRequestsDiscarded_Type()
)
cmiHaRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegRequestsDiscarded.setStatus("current")
_CmiHaEncapUnavailable_Type = Counter32
_CmiHaEncapUnavailable_Object = MibScalar
cmiHaEncapUnavailable = _CmiHaEncapUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 17),
    _CmiHaEncapUnavailable_Type()
)
cmiHaEncapUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaEncapUnavailable.setStatus("current")
_CmiHaNAICheckFailures_Type = Counter32
_CmiHaNAICheckFailures_Object = MibScalar
cmiHaNAICheckFailures = _CmiHaNAICheckFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 18),
    _CmiHaNAICheckFailures_Type()
)
cmiHaNAICheckFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaNAICheckFailures.setStatus("current")
_CmiHaInitRegRequestsReceived_Type = Counter32
_CmiHaInitRegRequestsReceived_Object = MibScalar
cmiHaInitRegRequestsReceived = _CmiHaInitRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 19),
    _CmiHaInitRegRequestsReceived_Type()
)
cmiHaInitRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaInitRegRequestsReceived.setStatus("current")
_CmiHaInitRegRequestsAccepted_Type = Counter32
_CmiHaInitRegRequestsAccepted_Object = MibScalar
cmiHaInitRegRequestsAccepted = _CmiHaInitRegRequestsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 20),
    _CmiHaInitRegRequestsAccepted_Type()
)
cmiHaInitRegRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaInitRegRequestsAccepted.setStatus("current")
_CmiHaInitRegRequestsDenied_Type = Counter32
_CmiHaInitRegRequestsDenied_Object = MibScalar
cmiHaInitRegRequestsDenied = _CmiHaInitRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 21),
    _CmiHaInitRegRequestsDenied_Type()
)
cmiHaInitRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaInitRegRequestsDenied.setStatus("current")
_CmiHaInitRegRequestsDiscarded_Type = Counter32
_CmiHaInitRegRequestsDiscarded_Object = MibScalar
cmiHaInitRegRequestsDiscarded = _CmiHaInitRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 22),
    _CmiHaInitRegRequestsDiscarded_Type()
)
cmiHaInitRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaInitRegRequestsDiscarded.setStatus("current")
_CmiHaReRegRequestsReceived_Type = Counter32
_CmiHaReRegRequestsReceived_Object = MibScalar
cmiHaReRegRequestsReceived = _CmiHaReRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 23),
    _CmiHaReRegRequestsReceived_Type()
)
cmiHaReRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaReRegRequestsReceived.setStatus("current")
_CmiHaReRegRequestsAccepted_Type = Counter32
_CmiHaReRegRequestsAccepted_Object = MibScalar
cmiHaReRegRequestsAccepted = _CmiHaReRegRequestsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 24),
    _CmiHaReRegRequestsAccepted_Type()
)
cmiHaReRegRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaReRegRequestsAccepted.setStatus("current")
_CmiHaReRegRequestsDenied_Type = Counter32
_CmiHaReRegRequestsDenied_Object = MibScalar
cmiHaReRegRequestsDenied = _CmiHaReRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 25),
    _CmiHaReRegRequestsDenied_Type()
)
cmiHaReRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaReRegRequestsDenied.setStatus("current")
_CmiHaReRegRequestsDiscarded_Type = Counter32
_CmiHaReRegRequestsDiscarded_Object = MibScalar
cmiHaReRegRequestsDiscarded = _CmiHaReRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 26),
    _CmiHaReRegRequestsDiscarded_Type()
)
cmiHaReRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaReRegRequestsDiscarded.setStatus("current")
_CmiHaDeRegRequestsReceived_Type = Counter32
_CmiHaDeRegRequestsReceived_Object = MibScalar
cmiHaDeRegRequestsReceived = _CmiHaDeRegRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 27),
    _CmiHaDeRegRequestsReceived_Type()
)
cmiHaDeRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaDeRegRequestsReceived.setStatus("current")
_CmiHaDeRegRequestsAccepted_Type = Counter32
_CmiHaDeRegRequestsAccepted_Object = MibScalar
cmiHaDeRegRequestsAccepted = _CmiHaDeRegRequestsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 28),
    _CmiHaDeRegRequestsAccepted_Type()
)
cmiHaDeRegRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaDeRegRequestsAccepted.setStatus("current")
_CmiHaDeRegRequestsDenied_Type = Counter32
_CmiHaDeRegRequestsDenied_Object = MibScalar
cmiHaDeRegRequestsDenied = _CmiHaDeRegRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 29),
    _CmiHaDeRegRequestsDenied_Type()
)
cmiHaDeRegRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaDeRegRequestsDenied.setStatus("current")
_CmiHaDeRegRequestsDiscarded_Type = Counter32
_CmiHaDeRegRequestsDiscarded_Object = MibScalar
cmiHaDeRegRequestsDiscarded = _CmiHaDeRegRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 30),
    _CmiHaDeRegRequestsDiscarded_Type()
)
cmiHaDeRegRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaDeRegRequestsDiscarded.setStatus("current")
_CmiHaReverseTunnelUnavailable_Type = Counter32
_CmiHaReverseTunnelUnavailable_Object = MibScalar
cmiHaReverseTunnelUnavailable = _CmiHaReverseTunnelUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 31),
    _CmiHaReverseTunnelUnavailable_Type()
)
cmiHaReverseTunnelUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaReverseTunnelUnavailable.setStatus("current")
_CmiHaReverseTunnelBitNotSet_Type = Counter32
_CmiHaReverseTunnelBitNotSet_Object = MibScalar
cmiHaReverseTunnelBitNotSet = _CmiHaReverseTunnelBitNotSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 32),
    _CmiHaReverseTunnelBitNotSet_Type()
)
cmiHaReverseTunnelBitNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaReverseTunnelBitNotSet.setStatus("current")
_CmiHaEncapsulationUnavailable_Type = Counter32
_CmiHaEncapsulationUnavailable_Object = MibScalar
cmiHaEncapsulationUnavailable = _CmiHaEncapsulationUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 33),
    _CmiHaEncapsulationUnavailable_Type()
)
cmiHaEncapsulationUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaEncapsulationUnavailable.setStatus("current")
_CmiHaCvsesFromMnRejected_Type = Counter32
_CmiHaCvsesFromMnRejected_Object = MibScalar
cmiHaCvsesFromMnRejected = _CmiHaCvsesFromMnRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 34),
    _CmiHaCvsesFromMnRejected_Type()
)
cmiHaCvsesFromMnRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaCvsesFromMnRejected.setStatus("current")
_CmiHaCvsesFromFaRejected_Type = Counter32
_CmiHaCvsesFromFaRejected_Object = MibScalar
cmiHaCvsesFromFaRejected = _CmiHaCvsesFromFaRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 35),
    _CmiHaCvsesFromFaRejected_Type()
)
cmiHaCvsesFromFaRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaCvsesFromFaRejected.setStatus("current")
_CmiHaNvsesFromMnNeglected_Type = Counter32
_CmiHaNvsesFromMnNeglected_Object = MibScalar
cmiHaNvsesFromMnNeglected = _CmiHaNvsesFromMnNeglected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 36),
    _CmiHaNvsesFromMnNeglected_Type()
)
cmiHaNvsesFromMnNeglected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaNvsesFromMnNeglected.setStatus("current")
_CmiHaNvsesFromFaNeglected_Type = Counter32
_CmiHaNvsesFromFaNeglected_Object = MibScalar
cmiHaNvsesFromFaNeglected = _CmiHaNvsesFromFaNeglected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 37),
    _CmiHaNvsesFromFaNeglected_Type()
)
cmiHaNvsesFromFaNeglected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaNvsesFromFaNeglected.setStatus("current")
_CmiHaMnHaAuthFailures_Type = Counter32
_CmiHaMnHaAuthFailures_Object = MibScalar
cmiHaMnHaAuthFailures = _CmiHaMnHaAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 38),
    _CmiHaMnHaAuthFailures_Type()
)
cmiHaMnHaAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaMnHaAuthFailures.setStatus("current")
_CmiHaMnAAAAuthFailures_Type = Counter32
_CmiHaMnAAAAuthFailures_Object = MibScalar
cmiHaMnAAAAuthFailures = _CmiHaMnAAAAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 39),
    _CmiHaMnAAAAuthFailures_Type()
)
cmiHaMnAAAAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaMnAAAAuthFailures.setStatus("current")


class _CmiHaMaximumBindings_Type(Unsigned32):
    """Custom type cmiHaMaximumBindings based on Unsigned32"""
    defaultValue = 235000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_CmiHaMaximumBindings_Type.__name__ = "Unsigned32"
_CmiHaMaximumBindings_Object = MibScalar
cmiHaMaximumBindings = _CmiHaMaximumBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 40),
    _CmiHaMaximumBindings_Type()
)
cmiHaMaximumBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiHaMaximumBindings.setStatus("current")


class _CmiHaRegIntervalSize_Type(Unsigned32):
    """Custom type cmiHaRegIntervalSize based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_CmiHaRegIntervalSize_Type.__name__ = "Unsigned32"
_CmiHaRegIntervalSize_Object = MibScalar
cmiHaRegIntervalSize = _CmiHaRegIntervalSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 41),
    _CmiHaRegIntervalSize_Type()
)
cmiHaRegIntervalSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiHaRegIntervalSize.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegIntervalSize.setUnits("minutes")
_CmiHaRegIntervalMaxActiveBindings_Type = Gauge32
_CmiHaRegIntervalMaxActiveBindings_Object = MibScalar
cmiHaRegIntervalMaxActiveBindings = _CmiHaRegIntervalMaxActiveBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 42),
    _CmiHaRegIntervalMaxActiveBindings_Type()
)
cmiHaRegIntervalMaxActiveBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegIntervalMaxActiveBindings.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegIntervalMaxActiveBindings.setUnits("MIP call per interval")
_CmiHaRegInterval3gpp2MaxActiveBindings_Type = Gauge32
_CmiHaRegInterval3gpp2MaxActiveBindings_Object = MibScalar
cmiHaRegInterval3gpp2MaxActiveBindings = _CmiHaRegInterval3gpp2MaxActiveBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 43),
    _CmiHaRegInterval3gpp2MaxActiveBindings_Type()
)
cmiHaRegInterval3gpp2MaxActiveBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegInterval3gpp2MaxActiveBindings.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegInterval3gpp2MaxActiveBindings.setUnits("MIP call per interval")
_CmiHaRegIntervalWimaxMaxActiveBindings_Type = Gauge32
_CmiHaRegIntervalWimaxMaxActiveBindings_Object = MibScalar
cmiHaRegIntervalWimaxMaxActiveBindings = _CmiHaRegIntervalWimaxMaxActiveBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 44),
    _CmiHaRegIntervalWimaxMaxActiveBindings_Type()
)
cmiHaRegIntervalWimaxMaxActiveBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegIntervalWimaxMaxActiveBindings.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegIntervalWimaxMaxActiveBindings.setUnits("MIP call per interval")
_CmiHaRegTunnelStatsTable_Object = MibTable
cmiHaRegTunnelStatsTable = _CmiHaRegTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45)
)
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsTable.setStatus("current")
_CmiHaRegTunnelStatsEntry_Object = MibTableRow
cmiHaRegTunnelStatsEntry = _CmiHaRegTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1)
)
cmiHaRegTunnelStatsEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsSrcAddrType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsSrcAddr"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsDestAddrType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsDestAddr"),
)
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsEntry.setStatus("current")
_CmiHaRegTunnelStatsSrcAddrType_Type = InetAddressType
_CmiHaRegTunnelStatsSrcAddrType_Object = MibTableColumn
cmiHaRegTunnelStatsSrcAddrType = _CmiHaRegTunnelStatsSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 1),
    _CmiHaRegTunnelStatsSrcAddrType_Type()
)
cmiHaRegTunnelStatsSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsSrcAddrType.setStatus("current")
_CmiHaRegTunnelStatsSrcAddr_Type = InetAddress
_CmiHaRegTunnelStatsSrcAddr_Object = MibTableColumn
cmiHaRegTunnelStatsSrcAddr = _CmiHaRegTunnelStatsSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 2),
    _CmiHaRegTunnelStatsSrcAddr_Type()
)
cmiHaRegTunnelStatsSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsSrcAddr.setStatus("current")
_CmiHaRegTunnelStatsDestAddrType_Type = InetAddressType
_CmiHaRegTunnelStatsDestAddrType_Object = MibTableColumn
cmiHaRegTunnelStatsDestAddrType = _CmiHaRegTunnelStatsDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 3),
    _CmiHaRegTunnelStatsDestAddrType_Type()
)
cmiHaRegTunnelStatsDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsDestAddrType.setStatus("current")
_CmiHaRegTunnelStatsDestAddr_Type = InetAddress
_CmiHaRegTunnelStatsDestAddr_Object = MibTableColumn
cmiHaRegTunnelStatsDestAddr = _CmiHaRegTunnelStatsDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 4),
    _CmiHaRegTunnelStatsDestAddr_Type()
)
cmiHaRegTunnelStatsDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsDestAddr.setStatus("current")
_CmiHaRegTunnelStatsTunnelType_Type = CmiTunnelType
_CmiHaRegTunnelStatsTunnelType_Object = MibTableColumn
cmiHaRegTunnelStatsTunnelType = _CmiHaRegTunnelStatsTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 5),
    _CmiHaRegTunnelStatsTunnelType_Type()
)
cmiHaRegTunnelStatsTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsTunnelType.setStatus("current")
_CmiHaRegTunnelStatsNumUsers_Type = Gauge32
_CmiHaRegTunnelStatsNumUsers_Object = MibTableColumn
cmiHaRegTunnelStatsNumUsers = _CmiHaRegTunnelStatsNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 6),
    _CmiHaRegTunnelStatsNumUsers_Type()
)
cmiHaRegTunnelStatsNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsNumUsers.setStatus("current")
_CmiHaRegTunnelStatsDataRateInt_Type = Unsigned32
_CmiHaRegTunnelStatsDataRateInt_Object = MibTableColumn
cmiHaRegTunnelStatsDataRateInt = _CmiHaRegTunnelStatsDataRateInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 7),
    _CmiHaRegTunnelStatsDataRateInt_Type()
)
cmiHaRegTunnelStatsDataRateInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsDataRateInt.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsDataRateInt.setUnits("seconds")
_CmiHaRegTunnelStatsInBitRate_Type = CounterBasedGauge64
_CmiHaRegTunnelStatsInBitRate_Object = MibTableColumn
cmiHaRegTunnelStatsInBitRate = _CmiHaRegTunnelStatsInBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 8),
    _CmiHaRegTunnelStatsInBitRate_Type()
)
cmiHaRegTunnelStatsInBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsInBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsInBitRate.setUnits("bits per second")
_CmiHaRegTunnelStatsInPktRate_Type = CounterBasedGauge64
_CmiHaRegTunnelStatsInPktRate_Object = MibTableColumn
cmiHaRegTunnelStatsInPktRate = _CmiHaRegTunnelStatsInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 9),
    _CmiHaRegTunnelStatsInPktRate_Type()
)
cmiHaRegTunnelStatsInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsInPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsInPktRate.setUnits("packets per second")
_CmiHaRegTunnelStatsInBytes_Type = Counter64
_CmiHaRegTunnelStatsInBytes_Object = MibTableColumn
cmiHaRegTunnelStatsInBytes = _CmiHaRegTunnelStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 10),
    _CmiHaRegTunnelStatsInBytes_Type()
)
cmiHaRegTunnelStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsInBytes.setStatus("current")
_CmiHaRegTunnelStatsInPkts_Type = Counter64
_CmiHaRegTunnelStatsInPkts_Object = MibTableColumn
cmiHaRegTunnelStatsInPkts = _CmiHaRegTunnelStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 11),
    _CmiHaRegTunnelStatsInPkts_Type()
)
cmiHaRegTunnelStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsInPkts.setStatus("current")
_CmiHaRegTunnelStatsOutBitRate_Type = CounterBasedGauge64
_CmiHaRegTunnelStatsOutBitRate_Object = MibTableColumn
cmiHaRegTunnelStatsOutBitRate = _CmiHaRegTunnelStatsOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 12),
    _CmiHaRegTunnelStatsOutBitRate_Type()
)
cmiHaRegTunnelStatsOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsOutBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsOutBitRate.setUnits("bits per second")
_CmiHaRegTunnelStatsOutPktRate_Type = CounterBasedGauge64
_CmiHaRegTunnelStatsOutPktRate_Object = MibTableColumn
cmiHaRegTunnelStatsOutPktRate = _CmiHaRegTunnelStatsOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 13),
    _CmiHaRegTunnelStatsOutPktRate_Type()
)
cmiHaRegTunnelStatsOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsOutPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsOutPktRate.setUnits("packets per second")
_CmiHaRegTunnelStatsOutBytes_Type = Counter64
_CmiHaRegTunnelStatsOutBytes_Object = MibTableColumn
cmiHaRegTunnelStatsOutBytes = _CmiHaRegTunnelStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 14),
    _CmiHaRegTunnelStatsOutBytes_Type()
)
cmiHaRegTunnelStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsOutBytes.setStatus("current")
_CmiHaRegTunnelStatsOutPkts_Type = Counter64
_CmiHaRegTunnelStatsOutPkts_Object = MibTableColumn
cmiHaRegTunnelStatsOutPkts = _CmiHaRegTunnelStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 1, 45, 1, 15),
    _CmiHaRegTunnelStatsOutPkts_Type()
)
cmiHaRegTunnelStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRegTunnelStatsOutPkts.setStatus("current")
_CmiHaRedun_ObjectIdentity = ObjectIdentity
cmiHaRedun = _CmiHaRedun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2)
)
_CmiHaRedunSentBUs_Type = Counter32
_CmiHaRedunSentBUs_Object = MibScalar
cmiHaRedunSentBUs = _CmiHaRedunSentBUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 1),
    _CmiHaRedunSentBUs_Type()
)
cmiHaRedunSentBUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunSentBUs.setStatus("current")
_CmiHaRedunFailedBUs_Type = Counter32
_CmiHaRedunFailedBUs_Object = MibScalar
cmiHaRedunFailedBUs = _CmiHaRedunFailedBUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 2),
    _CmiHaRedunFailedBUs_Type()
)
cmiHaRedunFailedBUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunFailedBUs.setStatus("current")
_CmiHaRedunReceivedBUAcks_Type = Counter32
_CmiHaRedunReceivedBUAcks_Object = MibScalar
cmiHaRedunReceivedBUAcks = _CmiHaRedunReceivedBUAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 3),
    _CmiHaRedunReceivedBUAcks_Type()
)
cmiHaRedunReceivedBUAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunReceivedBUAcks.setStatus("current")
_CmiHaRedunTotalSentBUs_Type = Counter32
_CmiHaRedunTotalSentBUs_Object = MibScalar
cmiHaRedunTotalSentBUs = _CmiHaRedunTotalSentBUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 4),
    _CmiHaRedunTotalSentBUs_Type()
)
cmiHaRedunTotalSentBUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunTotalSentBUs.setStatus("current")
_CmiHaRedunReceivedBUs_Type = Counter32
_CmiHaRedunReceivedBUs_Object = MibScalar
cmiHaRedunReceivedBUs = _CmiHaRedunReceivedBUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 5),
    _CmiHaRedunReceivedBUs_Type()
)
cmiHaRedunReceivedBUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunReceivedBUs.setStatus("current")
_CmiHaRedunSentBUAcks_Type = Counter32
_CmiHaRedunSentBUAcks_Object = MibScalar
cmiHaRedunSentBUAcks = _CmiHaRedunSentBUAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 6),
    _CmiHaRedunSentBUAcks_Type()
)
cmiHaRedunSentBUAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunSentBUAcks.setStatus("current")
_CmiHaRedunSentBIReqs_Type = Counter32
_CmiHaRedunSentBIReqs_Object = MibScalar
cmiHaRedunSentBIReqs = _CmiHaRedunSentBIReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 7),
    _CmiHaRedunSentBIReqs_Type()
)
cmiHaRedunSentBIReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunSentBIReqs.setStatus("current")
_CmiHaRedunFailedBIReqs_Type = Counter32
_CmiHaRedunFailedBIReqs_Object = MibScalar
cmiHaRedunFailedBIReqs = _CmiHaRedunFailedBIReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 8),
    _CmiHaRedunFailedBIReqs_Type()
)
cmiHaRedunFailedBIReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunFailedBIReqs.setStatus("current")
_CmiHaRedunTotalSentBIReqs_Type = Counter32
_CmiHaRedunTotalSentBIReqs_Object = MibScalar
cmiHaRedunTotalSentBIReqs = _CmiHaRedunTotalSentBIReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 9),
    _CmiHaRedunTotalSentBIReqs_Type()
)
cmiHaRedunTotalSentBIReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunTotalSentBIReqs.setStatus("current")
_CmiHaRedunReceivedBIReps_Type = Counter32
_CmiHaRedunReceivedBIReps_Object = MibScalar
cmiHaRedunReceivedBIReps = _CmiHaRedunReceivedBIReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 10),
    _CmiHaRedunReceivedBIReps_Type()
)
cmiHaRedunReceivedBIReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunReceivedBIReps.setStatus("current")
_CmiHaRedunDroppedBIReps_Type = Counter32
_CmiHaRedunDroppedBIReps_Object = MibScalar
cmiHaRedunDroppedBIReps = _CmiHaRedunDroppedBIReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 11),
    _CmiHaRedunDroppedBIReps_Type()
)
cmiHaRedunDroppedBIReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunDroppedBIReps.setStatus("current")
_CmiHaRedunSentBIAcks_Type = Counter32
_CmiHaRedunSentBIAcks_Object = MibScalar
cmiHaRedunSentBIAcks = _CmiHaRedunSentBIAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 12),
    _CmiHaRedunSentBIAcks_Type()
)
cmiHaRedunSentBIAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunSentBIAcks.setStatus("current")
_CmiHaRedunReceivedBIReqs_Type = Counter32
_CmiHaRedunReceivedBIReqs_Object = MibScalar
cmiHaRedunReceivedBIReqs = _CmiHaRedunReceivedBIReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 13),
    _CmiHaRedunReceivedBIReqs_Type()
)
cmiHaRedunReceivedBIReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunReceivedBIReqs.setStatus("current")
_CmiHaRedunSentBIReps_Type = Counter32
_CmiHaRedunSentBIReps_Object = MibScalar
cmiHaRedunSentBIReps = _CmiHaRedunSentBIReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 14),
    _CmiHaRedunSentBIReps_Type()
)
cmiHaRedunSentBIReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunSentBIReps.setStatus("current")
_CmiHaRedunFailedBIReps_Type = Counter32
_CmiHaRedunFailedBIReps_Object = MibScalar
cmiHaRedunFailedBIReps = _CmiHaRedunFailedBIReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 15),
    _CmiHaRedunFailedBIReps_Type()
)
cmiHaRedunFailedBIReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunFailedBIReps.setStatus("current")
_CmiHaRedunTotalSentBIReps_Type = Counter32
_CmiHaRedunTotalSentBIReps_Object = MibScalar
cmiHaRedunTotalSentBIReps = _CmiHaRedunTotalSentBIReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 16),
    _CmiHaRedunTotalSentBIReps_Type()
)
cmiHaRedunTotalSentBIReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunTotalSentBIReps.setStatus("current")
_CmiHaRedunReceivedBIAcks_Type = Counter32
_CmiHaRedunReceivedBIAcks_Object = MibScalar
cmiHaRedunReceivedBIAcks = _CmiHaRedunReceivedBIAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 17),
    _CmiHaRedunReceivedBIAcks_Type()
)
cmiHaRedunReceivedBIAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunReceivedBIAcks.setStatus("current")
_CmiHaRedunDroppedBIAcks_Type = Counter32
_CmiHaRedunDroppedBIAcks_Object = MibScalar
cmiHaRedunDroppedBIAcks = _CmiHaRedunDroppedBIAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 18),
    _CmiHaRedunDroppedBIAcks_Type()
)
cmiHaRedunDroppedBIAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunDroppedBIAcks.setStatus("current")
_CmiHaRedunSecViolations_Type = Counter32
_CmiHaRedunSecViolations_Object = MibScalar
cmiHaRedunSecViolations = _CmiHaRedunSecViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 2, 19),
    _CmiHaRedunSecViolations_Type()
)
cmiHaRedunSecViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaRedunSecViolations.setStatus("current")
_CmiHaMobNet_ObjectIdentity = ObjectIdentity
cmiHaMobNet = _CmiHaMobNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3)
)
_CmiHaMrTable_Object = MibTable
cmiHaMrTable = _CmiHaMrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cmiHaMrTable.setStatus("current")
_CmiHaMrEntry_Object = MibTableRow
cmiHaMrEntry = _CmiHaMrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1)
)
cmiHaMrEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMrAddrType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMrAddr"),
)
if mibBuilder.loadTexts:
    cmiHaMrEntry.setStatus("current")
_CmiHaMrAddrType_Type = InetAddressType
_CmiHaMrAddrType_Object = MibTableColumn
cmiHaMrAddrType = _CmiHaMrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1, 1),
    _CmiHaMrAddrType_Type()
)
cmiHaMrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaMrAddrType.setStatus("current")


class _CmiHaMrAddr_Type(InetAddress):
    """Custom type cmiHaMrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmiHaMrAddr_Type.__name__ = "InetAddress"
_CmiHaMrAddr_Object = MibTableColumn
cmiHaMrAddr = _CmiHaMrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1, 2),
    _CmiHaMrAddr_Type()
)
cmiHaMrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaMrAddr.setStatus("current")


class _CmiHaMrDynamic_Type(TruthValue):
    """Custom type cmiHaMrDynamic based on TruthValue"""


_CmiHaMrDynamic_Object = MibTableColumn
cmiHaMrDynamic = _CmiHaMrDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1, 3),
    _CmiHaMrDynamic_Type()
)
cmiHaMrDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiHaMrDynamic.setStatus("current")
_CmiHaMrStatus_Type = RowStatus
_CmiHaMrStatus_Object = MibTableColumn
cmiHaMrStatus = _CmiHaMrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1, 4),
    _CmiHaMrStatus_Type()
)
cmiHaMrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiHaMrStatus.setStatus("current")


class _CmiHaMrMultiPath_Type(TruthValue):
    """Custom type cmiHaMrMultiPath based on TruthValue"""


_CmiHaMrMultiPath_Object = MibTableColumn
cmiHaMrMultiPath = _CmiHaMrMultiPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1, 5),
    _CmiHaMrMultiPath_Type()
)
cmiHaMrMultiPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiHaMrMultiPath.setStatus("current")


class _CmiHaMrMultiPathMetricType_Type(CmiMultiPathMetricType):
    """Custom type cmiHaMrMultiPathMetricType based on CmiMultiPathMetricType"""


_CmiHaMrMultiPathMetricType_Object = MibTableColumn
cmiHaMrMultiPathMetricType = _CmiHaMrMultiPathMetricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 1, 1, 6),
    _CmiHaMrMultiPathMetricType_Type()
)
cmiHaMrMultiPathMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiHaMrMultiPathMetricType.setStatus("current")
_CmiHaMobNetTable_Object = MibTable
cmiHaMobNetTable = _CmiHaMobNetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cmiHaMobNetTable.setStatus("current")
_CmiHaMobNetEntry_Object = MibTableRow
cmiHaMobNetEntry = _CmiHaMobNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2, 1)
)
cmiHaMobNetEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMrAddrType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMrAddr"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMobNetAddressType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMobNetAddress"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiHaMobNetPfxLen"),
)
if mibBuilder.loadTexts:
    cmiHaMobNetEntry.setStatus("current")
_CmiHaMobNetAddressType_Type = InetAddressType
_CmiHaMobNetAddressType_Object = MibTableColumn
cmiHaMobNetAddressType = _CmiHaMobNetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2, 1, 1),
    _CmiHaMobNetAddressType_Type()
)
cmiHaMobNetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaMobNetAddressType.setStatus("current")


class _CmiHaMobNetAddress_Type(InetAddress):
    """Custom type cmiHaMobNetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmiHaMobNetAddress_Type.__name__ = "InetAddress"
_CmiHaMobNetAddress_Object = MibTableColumn
cmiHaMobNetAddress = _CmiHaMobNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2, 1, 2),
    _CmiHaMobNetAddress_Type()
)
cmiHaMobNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaMobNetAddress.setStatus("current")
_CmiHaMobNetPfxLen_Type = InetAddressPrefixLength
_CmiHaMobNetPfxLen_Object = MibTableColumn
cmiHaMobNetPfxLen = _CmiHaMobNetPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2, 1, 3),
    _CmiHaMobNetPfxLen_Type()
)
cmiHaMobNetPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiHaMobNetPfxLen.setStatus("current")
_CmiHaMobNetDynamic_Type = TruthValue
_CmiHaMobNetDynamic_Object = MibTableColumn
cmiHaMobNetDynamic = _CmiHaMobNetDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2, 1, 4),
    _CmiHaMobNetDynamic_Type()
)
cmiHaMobNetDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaMobNetDynamic.setStatus("current")
_CmiHaMobNetStatus_Type = RowStatus
_CmiHaMobNetStatus_Object = MibTableColumn
cmiHaMobNetStatus = _CmiHaMobNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 3, 2, 1, 5),
    _CmiHaMobNetStatus_Type()
)
cmiHaMobNetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiHaMobNetStatus.setStatus("current")
_CmiHaSystem_ObjectIdentity = ObjectIdentity
cmiHaSystem = _CmiHaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 4)
)
_CmiHaSystemVersion_Type = SnmpAdminString
_CmiHaSystemVersion_Object = MibScalar
cmiHaSystemVersion = _CmiHaSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 2, 4, 1),
    _CmiHaSystemVersion_Type()
)
cmiHaSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiHaSystemVersion.setStatus("current")
_CmiSecurity_ObjectIdentity = ObjectIdentity
cmiSecurity = _CmiSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3)
)
_CmiSecAssocsCount_Type = Gauge32
_CmiSecAssocsCount_Object = MibScalar
cmiSecAssocsCount = _CmiSecAssocsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 1),
    _CmiSecAssocsCount_Type()
)
cmiSecAssocsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecAssocsCount.setStatus("current")
_CmiSecAssocTable_Object = MibTable
cmiSecAssocTable = _CmiSecAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cmiSecAssocTable.setStatus("current")
_CmiSecAssocEntry_Object = MibTableRow
cmiSecAssocEntry = _CmiSecAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1)
)
cmiSecAssocEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiSecPeerIdentifierType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiSecPeerIdentifier"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiSecSPI"),
)
if mibBuilder.loadTexts:
    cmiSecAssocEntry.setStatus("current")
_CmiSecPeerIdentifierType_Type = CmiEntityIdentifierType
_CmiSecPeerIdentifierType_Object = MibTableColumn
cmiSecPeerIdentifierType = _CmiSecPeerIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 1),
    _CmiSecPeerIdentifierType_Type()
)
cmiSecPeerIdentifierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiSecPeerIdentifierType.setStatus("current")
_CmiSecPeerIdentifier_Type = CmiEntityIdentifier
_CmiSecPeerIdentifier_Object = MibTableColumn
cmiSecPeerIdentifier = _CmiSecPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 2),
    _CmiSecPeerIdentifier_Type()
)
cmiSecPeerIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiSecPeerIdentifier.setStatus("current")
_CmiSecSPI_Type = CmiSpi
_CmiSecSPI_Object = MibTableColumn
cmiSecSPI = _CmiSecSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 3),
    _CmiSecSPI_Type()
)
cmiSecSPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiSecSPI.setStatus("current")


class _CmiSecAlgorithmType_Type(Integer32):
    """Custom type cmiSecAlgorithmType based on Integer32"""
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
        *(("hmacMD5", 3),
          ("md5", 2),
          ("other", 1))
    )


_CmiSecAlgorithmType_Type.__name__ = "Integer32"
_CmiSecAlgorithmType_Object = MibTableColumn
cmiSecAlgorithmType = _CmiSecAlgorithmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 4),
    _CmiSecAlgorithmType_Type()
)
cmiSecAlgorithmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiSecAlgorithmType.setStatus("current")


class _CmiSecAlgorithmMode_Type(Integer32):
    """Custom type cmiSecAlgorithmMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("prefixSuffix", 2))
    )


_CmiSecAlgorithmMode_Type.__name__ = "Integer32"
_CmiSecAlgorithmMode_Object = MibTableColumn
cmiSecAlgorithmMode = _CmiSecAlgorithmMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 5),
    _CmiSecAlgorithmMode_Type()
)
cmiSecAlgorithmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiSecAlgorithmMode.setStatus("current")


class _CmiSecKey_Type(OctetString):
    """Custom type cmiSecKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CmiSecKey_Type.__name__ = "OctetString"
_CmiSecKey_Object = MibTableColumn
cmiSecKey = _CmiSecKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 6),
    _CmiSecKey_Type()
)
cmiSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiSecKey.setStatus("deprecated")


class _CmiSecReplayMethod_Type(Integer32):
    """Custom type cmiSecReplayMethod based on Integer32"""
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
        *(("nonces", 3),
          ("other", 1),
          ("timestamps", 2))
    )


_CmiSecReplayMethod_Type.__name__ = "Integer32"
_CmiSecReplayMethod_Object = MibTableColumn
cmiSecReplayMethod = _CmiSecReplayMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 7),
    _CmiSecReplayMethod_Type()
)
cmiSecReplayMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiSecReplayMethod.setStatus("current")
_CmiSecStatus_Type = RowStatus
_CmiSecStatus_Object = MibTableColumn
cmiSecStatus = _CmiSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 8),
    _CmiSecStatus_Type()
)
cmiSecStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiSecStatus.setStatus("current")


class _CmiSecKey2_Type(OctetString):
    """Custom type cmiSecKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmiSecKey2_Type.__name__ = "OctetString"
_CmiSecKey2_Object = MibTableColumn
cmiSecKey2 = _CmiSecKey2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 2, 1, 9),
    _CmiSecKey2_Type()
)
cmiSecKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiSecKey2.setStatus("current")
_CmiSecViolationTable_Object = MibTable
cmiSecViolationTable = _CmiSecViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cmiSecViolationTable.setStatus("current")
_CmiSecViolationEntry_Object = MibTableRow
cmiSecViolationEntry = _CmiSecViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1)
)
cmiSecViolationEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiSecViolatorIdentifierType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiSecViolatorIdentifier"),
)
if mibBuilder.loadTexts:
    cmiSecViolationEntry.setStatus("current")
_CmiSecViolatorIdentifierType_Type = CmiEntityIdentifierType
_CmiSecViolatorIdentifierType_Object = MibTableColumn
cmiSecViolatorIdentifierType = _CmiSecViolatorIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 1),
    _CmiSecViolatorIdentifierType_Type()
)
cmiSecViolatorIdentifierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiSecViolatorIdentifierType.setStatus("current")
_CmiSecViolatorIdentifier_Type = CmiEntityIdentifier
_CmiSecViolatorIdentifier_Object = MibTableColumn
cmiSecViolatorIdentifier = _CmiSecViolatorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 2),
    _CmiSecViolatorIdentifier_Type()
)
cmiSecViolatorIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiSecViolatorIdentifier.setStatus("current")
_CmiSecTotalViolations_Type = Counter32
_CmiSecTotalViolations_Object = MibTableColumn
cmiSecTotalViolations = _CmiSecTotalViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 3),
    _CmiSecTotalViolations_Type()
)
cmiSecTotalViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecTotalViolations.setStatus("current")
_CmiSecRecentViolationSPI_Type = CmiSpi
_CmiSecRecentViolationSPI_Object = MibTableColumn
cmiSecRecentViolationSPI = _CmiSecRecentViolationSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 4),
    _CmiSecRecentViolationSPI_Type()
)
cmiSecRecentViolationSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecRecentViolationSPI.setStatus("current")
_CmiSecRecentViolationTime_Type = TimeStamp
_CmiSecRecentViolationTime_Object = MibTableColumn
cmiSecRecentViolationTime = _CmiSecRecentViolationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 5),
    _CmiSecRecentViolationTime_Type()
)
cmiSecRecentViolationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecRecentViolationTime.setStatus("current")


class _CmiSecRecentViolationIDLow_Type(Unsigned32):
    """Custom type cmiSecRecentViolationIDLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmiSecRecentViolationIDLow_Type.__name__ = "Unsigned32"
_CmiSecRecentViolationIDLow_Object = MibTableColumn
cmiSecRecentViolationIDLow = _CmiSecRecentViolationIDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 6),
    _CmiSecRecentViolationIDLow_Type()
)
cmiSecRecentViolationIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecRecentViolationIDLow.setStatus("current")


class _CmiSecRecentViolationIDHigh_Type(Unsigned32):
    """Custom type cmiSecRecentViolationIDHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmiSecRecentViolationIDHigh_Type.__name__ = "Unsigned32"
_CmiSecRecentViolationIDHigh_Object = MibTableColumn
cmiSecRecentViolationIDHigh = _CmiSecRecentViolationIDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 7),
    _CmiSecRecentViolationIDHigh_Type()
)
cmiSecRecentViolationIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecRecentViolationIDHigh.setStatus("current")


class _CmiSecRecentViolationReason_Type(Integer32):
    """Custom type cmiSecRecentViolationReason based on Integer32"""
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
        *(("badAuthenticator", 2),
          ("badIdentifier", 3),
          ("badSPI", 4),
          ("missingSecurityExtension", 5),
          ("noMobilitySecurityAssociation", 1),
          ("other", 6))
    )


_CmiSecRecentViolationReason_Type.__name__ = "Integer32"
_CmiSecRecentViolationReason_Object = MibTableColumn
cmiSecRecentViolationReason = _CmiSecRecentViolationReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 3, 3, 1, 8),
    _CmiSecRecentViolationReason_Type()
)
cmiSecRecentViolationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiSecRecentViolationReason.setStatus("current")
_CmiMa_ObjectIdentity = ObjectIdentity
cmiMa = _CmiMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4)
)
_CmiMaReg_ObjectIdentity = ObjectIdentity
cmiMaReg = _CmiMaReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 1)
)
_CmiMaRegMaxInMinuteRegs_Type = Counter32
_CmiMaRegMaxInMinuteRegs_Object = MibScalar
cmiMaRegMaxInMinuteRegs = _CmiMaRegMaxInMinuteRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 1, 1),
    _CmiMaRegMaxInMinuteRegs_Type()
)
cmiMaRegMaxInMinuteRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMaRegMaxInMinuteRegs.setStatus("current")
_CmiMaRegDateMaxRegsReceived_Type = DateAndTime
_CmiMaRegDateMaxRegsReceived_Object = MibScalar
cmiMaRegDateMaxRegsReceived = _CmiMaRegDateMaxRegsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 1, 2),
    _CmiMaRegDateMaxRegsReceived_Type()
)
cmiMaRegDateMaxRegsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMaRegDateMaxRegsReceived.setStatus("current")
_CmiMaRegInLastMinuteRegs_Type = Counter32
_CmiMaRegInLastMinuteRegs_Object = MibScalar
cmiMaRegInLastMinuteRegs = _CmiMaRegInLastMinuteRegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 1, 3),
    _CmiMaRegInLastMinuteRegs_Type()
)
cmiMaRegInLastMinuteRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMaRegInLastMinuteRegs.setStatus("current")
_CmiMaAdvertisement_ObjectIdentity = ObjectIdentity
cmiMaAdvertisement = _CmiMaAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2)
)
_CmiMaAdvConfigTable_Object = MibTable
cmiMaAdvConfigTable = _CmiMaAdvConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cmiMaAdvConfigTable.setStatus("current")
_CmiMaAdvConfigEntry_Object = MibTableRow
cmiMaAdvConfigEntry = _CmiMaAdvConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1)
)
cmiMaAdvConfigEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiMaAdvInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cmiMaAdvConfigEntry.setStatus("current")
_CmiMaAdvInterfaceIndex_Type = InterfaceIndex
_CmiMaAdvInterfaceIndex_Object = MibTableColumn
cmiMaAdvInterfaceIndex = _CmiMaAdvInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 1),
    _CmiMaAdvInterfaceIndex_Type()
)
cmiMaAdvInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiMaAdvInterfaceIndex.setStatus("current")
_CmiMaInterfaceAddressType_Type = InetAddressType
_CmiMaInterfaceAddressType_Object = MibTableColumn
cmiMaInterfaceAddressType = _CmiMaInterfaceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 2),
    _CmiMaInterfaceAddressType_Type()
)
cmiMaInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMaInterfaceAddressType.setStatus("current")
_CmiMaInterfaceAddress_Type = InetAddress
_CmiMaInterfaceAddress_Object = MibTableColumn
cmiMaInterfaceAddress = _CmiMaInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 3),
    _CmiMaInterfaceAddress_Type()
)
cmiMaInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMaInterfaceAddress.setStatus("current")


class _CmiMaAdvMaxRegLifetime_Type(Unsigned32):
    """Custom type cmiMaAdvMaxRegLifetime based on Unsigned32"""
    defaultValue = 36000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_CmiMaAdvMaxRegLifetime_Type.__name__ = "Unsigned32"
_CmiMaAdvMaxRegLifetime_Object = MibTableColumn
cmiMaAdvMaxRegLifetime = _CmiMaAdvMaxRegLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 4),
    _CmiMaAdvMaxRegLifetime_Type()
)
cmiMaAdvMaxRegLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvMaxRegLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cmiMaAdvMaxRegLifetime.setUnits("seconds")


class _CmiMaAdvPrefixLengthInclusion_Type(TruthValue):
    """Custom type cmiMaAdvPrefixLengthInclusion based on TruthValue"""


_CmiMaAdvPrefixLengthInclusion_Object = MibTableColumn
cmiMaAdvPrefixLengthInclusion = _CmiMaAdvPrefixLengthInclusion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 5),
    _CmiMaAdvPrefixLengthInclusion_Type()
)
cmiMaAdvPrefixLengthInclusion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvPrefixLengthInclusion.setStatus("current")
_CmiMaAdvAddressType_Type = InetAddressType
_CmiMaAdvAddressType_Object = MibTableColumn
cmiMaAdvAddressType = _CmiMaAdvAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 6),
    _CmiMaAdvAddressType_Type()
)
cmiMaAdvAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvAddressType.setStatus("current")
_CmiMaAdvAddress_Type = InetAddress
_CmiMaAdvAddress_Object = MibTableColumn
cmiMaAdvAddress = _CmiMaAdvAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 7),
    _CmiMaAdvAddress_Type()
)
cmiMaAdvAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvAddress.setStatus("current")


class _CmiMaAdvMaxInterval_Type(Unsigned32):
    """Custom type cmiMaAdvMaxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 1800),
    )


_CmiMaAdvMaxInterval_Type.__name__ = "Unsigned32"
_CmiMaAdvMaxInterval_Object = MibTableColumn
cmiMaAdvMaxInterval = _CmiMaAdvMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 8),
    _CmiMaAdvMaxInterval_Type()
)
cmiMaAdvMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmiMaAdvMaxInterval.setUnits("seconds")


class _CmiMaAdvMinInterval_Type(Unsigned32):
    """Custom type cmiMaAdvMinInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 1800),
    )


_CmiMaAdvMinInterval_Type.__name__ = "Unsigned32"
_CmiMaAdvMinInterval_Object = MibTableColumn
cmiMaAdvMinInterval = _CmiMaAdvMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 9),
    _CmiMaAdvMinInterval_Type()
)
cmiMaAdvMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmiMaAdvMinInterval.setUnits("seconds")


class _CmiMaAdvMaxAdvLifetime_Type(Unsigned32):
    """Custom type cmiMaAdvMaxAdvLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 9000),
    )


_CmiMaAdvMaxAdvLifetime_Type.__name__ = "Unsigned32"
_CmiMaAdvMaxAdvLifetime_Object = MibTableColumn
cmiMaAdvMaxAdvLifetime = _CmiMaAdvMaxAdvLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 10),
    _CmiMaAdvMaxAdvLifetime_Type()
)
cmiMaAdvMaxAdvLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvMaxAdvLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cmiMaAdvMaxAdvLifetime.setUnits("seconds")
_CmiMaAdvResponseSolicitationOnly_Type = TruthValue
_CmiMaAdvResponseSolicitationOnly_Object = MibTableColumn
cmiMaAdvResponseSolicitationOnly = _CmiMaAdvResponseSolicitationOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 11),
    _CmiMaAdvResponseSolicitationOnly_Type()
)
cmiMaAdvResponseSolicitationOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvResponseSolicitationOnly.setStatus("current")
_CmiMaAdvStatus_Type = RowStatus
_CmiMaAdvStatus_Object = MibTableColumn
cmiMaAdvStatus = _CmiMaAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 4, 2, 1, 1, 12),
    _CmiMaAdvStatus_Type()
)
cmiMaAdvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMaAdvStatus.setStatus("current")
_CmiMn_ObjectIdentity = ObjectIdentity
cmiMn = _CmiMn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5)
)
_CmiMnDiscovery_ObjectIdentity = ObjectIdentity
cmiMnDiscovery = _CmiMnDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 1)
)
_CmiMnRecentAdvReceived_ObjectIdentity = ObjectIdentity
cmiMnRecentAdvReceived = _CmiMnRecentAdvReceived_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 1, 1)
)


class _CmiMnAdvFlags_Type(Bits):
    """Custom type cmiMnAdvFlags based on Bits"""
    namedValues = NamedValues(
        *(("busy", 4),
          ("foreignAgent", 2),
          ("gre", 0),
          ("homeAgent", 3),
          ("minEnc", 1),
          ("regRequired", 5),
          ("reverseTunnel", 6))
    )

_CmiMnAdvFlags_Type.__name__ = "Bits"
_CmiMnAdvFlags_Object = MibScalar
cmiMnAdvFlags = _CmiMnAdvFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 1, 1, 1),
    _CmiMnAdvFlags_Type()
)
cmiMnAdvFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMnAdvFlags.setStatus("current")
_CmiMnRegistration_ObjectIdentity = ObjectIdentity
cmiMnRegistration = _CmiMnRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 2)
)
_CmiMnRegistrationTable_Object = MibTable
cmiMnRegistrationTable = _CmiMnRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cmiMnRegistrationTable.setStatus("current")
_CmiMnRegistrationEntry_Object = MibTableRow
cmiMnRegistrationEntry = _CmiMnRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmiMnRegistrationEntry.setStatus("current")
_CmiMnRegFlags_Type = CmiRegistrationFlags
_CmiMnRegFlags_Object = MibTableColumn
cmiMnRegFlags = _CmiMnRegFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 2, 1, 1, 1),
    _CmiMnRegFlags_Type()
)
cmiMnRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMnRegFlags.setStatus("current")
_CmiMrSystem_ObjectIdentity = ObjectIdentity
cmiMrSystem = _CmiMrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3)
)


class _CmiMrReverseTunnel_Type(TruthValue):
    """Custom type cmiMrReverseTunnel based on TruthValue"""


_CmiMrReverseTunnel_Object = MibScalar
cmiMrReverseTunnel = _CmiMrReverseTunnel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 1),
    _CmiMrReverseTunnel_Type()
)
cmiMrReverseTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrReverseTunnel.setStatus("current")
_CmiMrRedundancyGroup_Type = SnmpAdminString
_CmiMrRedundancyGroup_Object = MibScalar
cmiMrRedundancyGroup = _CmiMrRedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 2),
    _CmiMrRedundancyGroup_Type()
)
cmiMrRedundancyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRedundancyGroup.setStatus("current")
_CmiMrMobNetTable_Object = MibTable
cmiMrMobNetTable = _CmiMrMobNetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    cmiMrMobNetTable.setStatus("current")
_CmiMrMobNetEntry_Object = MibTableRow
cmiMrMobNetEntry = _CmiMrMobNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3, 1)
)
cmiMrMobNetEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiMrMobNetIfIndex"),
)
if mibBuilder.loadTexts:
    cmiMrMobNetEntry.setStatus("current")
_CmiMrMobNetIfIndex_Type = InterfaceIndex
_CmiMrMobNetIfIndex_Object = MibTableColumn
cmiMrMobNetIfIndex = _CmiMrMobNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3, 1, 1),
    _CmiMrMobNetIfIndex_Type()
)
cmiMrMobNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiMrMobNetIfIndex.setStatus("current")
_CmiMrMobNetAddrType_Type = InetAddressType
_CmiMrMobNetAddrType_Object = MibTableColumn
cmiMrMobNetAddrType = _CmiMrMobNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3, 1, 2),
    _CmiMrMobNetAddrType_Type()
)
cmiMrMobNetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMobNetAddrType.setStatus("current")


class _CmiMrMobNetAddr_Type(InetAddress):
    """Custom type cmiMrMobNetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmiMrMobNetAddr_Type.__name__ = "InetAddress"
_CmiMrMobNetAddr_Object = MibTableColumn
cmiMrMobNetAddr = _CmiMrMobNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3, 1, 3),
    _CmiMrMobNetAddr_Type()
)
cmiMrMobNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMobNetAddr.setStatus("current")
_CmiMrMobNetPfxLen_Type = InetAddressPrefixLength
_CmiMrMobNetPfxLen_Object = MibTableColumn
cmiMrMobNetPfxLen = _CmiMrMobNetPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3, 1, 4),
    _CmiMrMobNetPfxLen_Type()
)
cmiMrMobNetPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMobNetPfxLen.setStatus("current")
_CmiMrMobNetStatus_Type = RowStatus
_CmiMrMobNetStatus_Object = MibTableColumn
cmiMrMobNetStatus = _CmiMrMobNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 3, 1, 5),
    _CmiMrMobNetStatus_Type()
)
cmiMrMobNetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrMobNetStatus.setStatus("current")
_CmiMrHaTunnelIfIndex_Type = InterfaceIndexOrZero
_CmiMrHaTunnelIfIndex_Object = MibScalar
cmiMrHaTunnelIfIndex = _CmiMrHaTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 4),
    _CmiMrHaTunnelIfIndex_Type()
)
cmiMrHaTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrHaTunnelIfIndex.setStatus("current")
_CmiMrHATable_Object = MibTable
cmiMrHATable = _CmiMrHATable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    cmiMrHATable.setStatus("current")
_CmiMrHAEntry_Object = MibTableRow
cmiMrHAEntry = _CmiMrHAEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cmiMrHAEntry.setStatus("current")


class _CmiMrHAPriority_Type(Unsigned32):
    """Custom type cmiMrHAPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmiMrHAPriority_Type.__name__ = "Unsigned32"
_CmiMrHAPriority_Object = MibTableColumn
cmiMrHAPriority = _CmiMrHAPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 5, 1, 1),
    _CmiMrHAPriority_Type()
)
cmiMrHAPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrHAPriority.setStatus("current")
_CmiMrHABest_Type = TruthValue
_CmiMrHABest_Object = MibTableColumn
cmiMrHABest = _CmiMrHABest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 5, 1, 2),
    _CmiMrHABest_Type()
)
cmiMrHABest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrHABest.setStatus("current")
_CmiMrIfTable_Object = MibTable
cmiMrIfTable = _CmiMrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    cmiMrIfTable.setStatus("current")
_CmiMrIfEntry_Object = MibTableRow
cmiMrIfEntry = _CmiMrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1)
)
cmiMrIfEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiMrIfIndex"),
)
if mibBuilder.loadTexts:
    cmiMrIfEntry.setStatus("current")
_CmiMrIfIndex_Type = InterfaceIndex
_CmiMrIfIndex_Object = MibTableColumn
cmiMrIfIndex = _CmiMrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 1),
    _CmiMrIfIndex_Type()
)
cmiMrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiMrIfIndex.setStatus("current")
_CmiMRIfDescription_Type = SnmpAdminString
_CmiMRIfDescription_Object = MibTableColumn
cmiMRIfDescription = _CmiMRIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 2),
    _CmiMRIfDescription_Type()
)
cmiMRIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMRIfDescription.setStatus("current")


class _CmiMrIfHoldDown_Type(Unsigned32):
    """Custom type cmiMrIfHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CmiMrIfHoldDown_Type.__name__ = "Unsigned32"
_CmiMrIfHoldDown_Object = MibTableColumn
cmiMrIfHoldDown = _CmiMrIfHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 3),
    _CmiMrIfHoldDown_Type()
)
cmiMrIfHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfHoldDown.setUnits("seconds")


class _CmiMrIfRoamPriority_Type(Unsigned32):
    """Custom type cmiMrIfRoamPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmiMrIfRoamPriority_Type.__name__ = "Unsigned32"
_CmiMrIfRoamPriority_Object = MibTableColumn
cmiMrIfRoamPriority = _CmiMrIfRoamPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 4),
    _CmiMrIfRoamPriority_Type()
)
cmiMrIfRoamPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfRoamPriority.setStatus("current")


class _CmiMrIfSolicitPeriodic_Type(TruthValue):
    """Custom type cmiMrIfSolicitPeriodic based on TruthValue"""


_CmiMrIfSolicitPeriodic_Object = MibTableColumn
cmiMrIfSolicitPeriodic = _CmiMrIfSolicitPeriodic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 5),
    _CmiMrIfSolicitPeriodic_Type()
)
cmiMrIfSolicitPeriodic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfSolicitPeriodic.setStatus("current")


class _CmiMrIfSolicitInterval_Type(Unsigned32):
    """Custom type cmiMrIfSolicitInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmiMrIfSolicitInterval_Type.__name__ = "Unsigned32"
_CmiMrIfSolicitInterval_Object = MibTableColumn
cmiMrIfSolicitInterval = _CmiMrIfSolicitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 6),
    _CmiMrIfSolicitInterval_Type()
)
cmiMrIfSolicitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfSolicitInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfSolicitInterval.setUnits("seconds")


class _CmiMrIfSolicitRetransInitial_Type(Unsigned32):
    """Custom type cmiMrIfSolicitRetransInitial based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CmiMrIfSolicitRetransInitial_Type.__name__ = "Unsigned32"
_CmiMrIfSolicitRetransInitial_Object = MibTableColumn
cmiMrIfSolicitRetransInitial = _CmiMrIfSolicitRetransInitial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 7),
    _CmiMrIfSolicitRetransInitial_Type()
)
cmiMrIfSolicitRetransInitial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransInitial.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransInitial.setUnits("milliseconds")


class _CmiMrIfSolicitRetransMax_Type(Unsigned32):
    """Custom type cmiMrIfSolicitRetransMax based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CmiMrIfSolicitRetransMax_Type.__name__ = "Unsigned32"
_CmiMrIfSolicitRetransMax_Object = MibTableColumn
cmiMrIfSolicitRetransMax = _CmiMrIfSolicitRetransMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 8),
    _CmiMrIfSolicitRetransMax_Type()
)
cmiMrIfSolicitRetransMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransMax.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransMax.setUnits("milliseconds")


class _CmiMrIfSolicitRetransLimit_Type(Unsigned32):
    """Custom type cmiMrIfSolicitRetransLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CmiMrIfSolicitRetransLimit_Type.__name__ = "Unsigned32"
_CmiMrIfSolicitRetransLimit_Object = MibTableColumn
cmiMrIfSolicitRetransLimit = _CmiMrIfSolicitRetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 9),
    _CmiMrIfSolicitRetransLimit_Type()
)
cmiMrIfSolicitRetransLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransLimit.setStatus("current")


class _CmiMrIfSolicitRetransCurrent_Type(Unsigned32):
    """Custom type cmiMrIfSolicitRetransCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CmiMrIfSolicitRetransCurrent_Type.__name__ = "Unsigned32"
_CmiMrIfSolicitRetransCurrent_Object = MibTableColumn
cmiMrIfSolicitRetransCurrent = _CmiMrIfSolicitRetransCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 10),
    _CmiMrIfSolicitRetransCurrent_Type()
)
cmiMrIfSolicitRetransCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransCurrent.setUnits("milliseconds")
_CmiMrIfSolicitRetransRemaining_Type = Gauge32
_CmiMrIfSolicitRetransRemaining_Object = MibTableColumn
cmiMrIfSolicitRetransRemaining = _CmiMrIfSolicitRetransRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 11),
    _CmiMrIfSolicitRetransRemaining_Type()
)
cmiMrIfSolicitRetransRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransRemaining.setUnits("milliseconds")
_CmiMrIfSolicitRetransCount_Type = Counter32
_CmiMrIfSolicitRetransCount_Object = MibTableColumn
cmiMrIfSolicitRetransCount = _CmiMrIfSolicitRetransCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 12),
    _CmiMrIfSolicitRetransCount_Type()
)
cmiMrIfSolicitRetransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfSolicitRetransCount.setStatus("current")
_CmiMrIfCCoaAddressType_Type = InetAddressType
_CmiMrIfCCoaAddressType_Object = MibTableColumn
cmiMrIfCCoaAddressType = _CmiMrIfCCoaAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 13),
    _CmiMrIfCCoaAddressType_Type()
)
cmiMrIfCCoaAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfCCoaAddressType.setStatus("current")
_CmiMrIfCCoaAddress_Type = InetAddress
_CmiMrIfCCoaAddress_Object = MibTableColumn
cmiMrIfCCoaAddress = _CmiMrIfCCoaAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 14),
    _CmiMrIfCCoaAddress_Type()
)
cmiMrIfCCoaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfCCoaAddress.setStatus("current")
_CmiMrIfCCoaDefaultGwType_Type = InetAddressType
_CmiMrIfCCoaDefaultGwType_Object = MibTableColumn
cmiMrIfCCoaDefaultGwType = _CmiMrIfCCoaDefaultGwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 15),
    _CmiMrIfCCoaDefaultGwType_Type()
)
cmiMrIfCCoaDefaultGwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfCCoaDefaultGwType.setStatus("current")


class _CmiMrIfCCoaDefaultGw_Type(InetAddress):
    """Custom type cmiMrIfCCoaDefaultGw based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmiMrIfCCoaDefaultGw_Type.__name__ = "InetAddress"
_CmiMrIfCCoaDefaultGw_Object = MibTableColumn
cmiMrIfCCoaDefaultGw = _CmiMrIfCCoaDefaultGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 16),
    _CmiMrIfCCoaDefaultGw_Type()
)
cmiMrIfCCoaDefaultGw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfCCoaDefaultGw.setStatus("current")


class _CmiMrIfCCoaRegRetry_Type(Unsigned32):
    """Custom type cmiMrIfCCoaRegRetry based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmiMrIfCCoaRegRetry_Type.__name__ = "Unsigned32"
_CmiMrIfCCoaRegRetry_Object = MibTableColumn
cmiMrIfCCoaRegRetry = _CmiMrIfCCoaRegRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 17),
    _CmiMrIfCCoaRegRetry_Type()
)
cmiMrIfCCoaRegRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfCCoaRegRetry.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfCCoaRegRetry.setUnits("seconds")
_CmiMrIfCCoaRegRetryRemaining_Type = Gauge32
_CmiMrIfCCoaRegRetryRemaining_Object = MibTableColumn
cmiMrIfCCoaRegRetryRemaining = _CmiMrIfCCoaRegRetryRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 18),
    _CmiMrIfCCoaRegRetryRemaining_Type()
)
cmiMrIfCCoaRegRetryRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfCCoaRegRetryRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrIfCCoaRegRetryRemaining.setUnits("seconds")
_CmiMrIfStatus_Type = RowStatus
_CmiMrIfStatus_Object = MibTableColumn
cmiMrIfStatus = _CmiMrIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 19),
    _CmiMrIfStatus_Type()
)
cmiMrIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfStatus.setStatus("current")
_CmiMrIfCCoaRegistration_Type = TruthValue
_CmiMrIfCCoaRegistration_Object = MibTableColumn
cmiMrIfCCoaRegistration = _CmiMrIfCCoaRegistration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 20),
    _CmiMrIfCCoaRegistration_Type()
)
cmiMrIfCCoaRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfCCoaRegistration.setStatus("current")


class _CmiMrIfCCoaOnly_Type(TruthValue):
    """Custom type cmiMrIfCCoaOnly based on TruthValue"""


_CmiMrIfCCoaOnly_Object = MibTableColumn
cmiMrIfCCoaOnly = _CmiMrIfCCoaOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 21),
    _CmiMrIfCCoaOnly_Type()
)
cmiMrIfCCoaOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfCCoaOnly.setStatus("current")


class _CmiMrIfCCoaEnable_Type(TruthValue):
    """Custom type cmiMrIfCCoaEnable based on TruthValue"""


_CmiMrIfCCoaEnable_Object = MibTableColumn
cmiMrIfCCoaEnable = _CmiMrIfCCoaEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 22),
    _CmiMrIfCCoaEnable_Type()
)
cmiMrIfCCoaEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmiMrIfCCoaEnable.setStatus("current")
_CmiMrIfRoamStatus_Type = TruthValue
_CmiMrIfRoamStatus_Object = MibTableColumn
cmiMrIfRoamStatus = _CmiMrIfRoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 23),
    _CmiMrIfRoamStatus_Type()
)
cmiMrIfRoamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfRoamStatus.setStatus("current")
_CmiMrIfRegisteredCoAType_Type = InetAddressType
_CmiMrIfRegisteredCoAType_Object = MibTableColumn
cmiMrIfRegisteredCoAType = _CmiMrIfRegisteredCoAType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 24),
    _CmiMrIfRegisteredCoAType_Type()
)
cmiMrIfRegisteredCoAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfRegisteredCoAType.setStatus("current")
_CmiMrIfRegisteredCoA_Type = InetAddress
_CmiMrIfRegisteredCoA_Object = MibTableColumn
cmiMrIfRegisteredCoA = _CmiMrIfRegisteredCoA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 25),
    _CmiMrIfRegisteredCoA_Type()
)
cmiMrIfRegisteredCoA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfRegisteredCoA.setStatus("current")
_CmiMrIfRegisteredMaAddrType_Type = InetAddressType
_CmiMrIfRegisteredMaAddrType_Object = MibTableColumn
cmiMrIfRegisteredMaAddrType = _CmiMrIfRegisteredMaAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 26),
    _CmiMrIfRegisteredMaAddrType_Type()
)
cmiMrIfRegisteredMaAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfRegisteredMaAddrType.setStatus("current")
_CmiMrIfRegisteredMaAddr_Type = InetAddress
_CmiMrIfRegisteredMaAddr_Object = MibTableColumn
cmiMrIfRegisteredMaAddr = _CmiMrIfRegisteredMaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 27),
    _CmiMrIfRegisteredMaAddr_Type()
)
cmiMrIfRegisteredMaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfRegisteredMaAddr.setStatus("current")
_CmiMrIfHaTunnelIfIndex_Type = InterfaceIndexOrZero
_CmiMrIfHaTunnelIfIndex_Object = MibTableColumn
cmiMrIfHaTunnelIfIndex = _CmiMrIfHaTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 28),
    _CmiMrIfHaTunnelIfIndex_Type()
)
cmiMrIfHaTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfHaTunnelIfIndex.setStatus("current")
_CmiMrIfID_Type = Unsigned32
_CmiMrIfID_Object = MibTableColumn
cmiMrIfID = _CmiMrIfID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 6, 1, 29),
    _CmiMrIfID_Type()
)
cmiMrIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrIfID.setStatus("current")
_CmiMrBetterIfDetected_Type = Counter32
_CmiMrBetterIfDetected_Object = MibScalar
cmiMrBetterIfDetected = _CmiMrBetterIfDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 7),
    _CmiMrBetterIfDetected_Type()
)
cmiMrBetterIfDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrBetterIfDetected.setStatus("current")
_CmiMrTunnelPktsRcvd_Type = Counter32
_CmiMrTunnelPktsRcvd_Object = MibScalar
cmiMrTunnelPktsRcvd = _CmiMrTunnelPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 8),
    _CmiMrTunnelPktsRcvd_Type()
)
cmiMrTunnelPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrTunnelPktsRcvd.setStatus("current")
_CmiMrTunnelPktsSent_Type = Counter32
_CmiMrTunnelPktsSent_Object = MibScalar
cmiMrTunnelPktsSent = _CmiMrTunnelPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 9),
    _CmiMrTunnelPktsSent_Type()
)
cmiMrTunnelPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrTunnelPktsSent.setStatus("current")
_CmiMrTunnelBytesRcvd_Type = Counter32
_CmiMrTunnelBytesRcvd_Object = MibScalar
cmiMrTunnelBytesRcvd = _CmiMrTunnelBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 10),
    _CmiMrTunnelBytesRcvd_Type()
)
cmiMrTunnelBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrTunnelBytesRcvd.setStatus("current")
_CmiMrTunnelBytesSent_Type = Counter32
_CmiMrTunnelBytesSent_Object = MibScalar
cmiMrTunnelBytesSent = _CmiMrTunnelBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 11),
    _CmiMrTunnelBytesSent_Type()
)
cmiMrTunnelBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrTunnelBytesSent.setStatus("current")
_CmiMrRedStateActive_Type = Counter32
_CmiMrRedStateActive_Object = MibScalar
cmiMrRedStateActive = _CmiMrRedStateActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 12),
    _CmiMrRedStateActive_Type()
)
cmiMrRedStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrRedStateActive.setStatus("current")
_CmiMrRedStatePassive_Type = Counter32
_CmiMrRedStatePassive_Object = MibScalar
cmiMrRedStatePassive = _CmiMrRedStatePassive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 13),
    _CmiMrRedStatePassive_Type()
)
cmiMrRedStatePassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrRedStatePassive.setStatus("current")


class _CmiMrCollocatedTunnel_Type(Integer32):
    """Custom type cmiMrCollocatedTunnel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("double", 2),
          ("single", 1))
    )


_CmiMrCollocatedTunnel_Type.__name__ = "Integer32"
_CmiMrCollocatedTunnel_Object = MibScalar
cmiMrCollocatedTunnel = _CmiMrCollocatedTunnel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 14),
    _CmiMrCollocatedTunnel_Type()
)
cmiMrCollocatedTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrCollocatedTunnel.setStatus("current")


class _CmiMrMultiPath_Type(TruthValue):
    """Custom type cmiMrMultiPath based on TruthValue"""


_CmiMrMultiPath_Object = MibScalar
cmiMrMultiPath = _CmiMrMultiPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 15),
    _CmiMrMultiPath_Type()
)
cmiMrMultiPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrMultiPath.setStatus("current")


class _CmiMrMultiPathMetricType_Type(CmiMultiPathMetricType):
    """Custom type cmiMrMultiPathMetricType based on CmiMultiPathMetricType"""


_CmiMrMultiPathMetricType_Object = MibScalar
cmiMrMultiPathMetricType = _CmiMrMultiPathMetricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 3, 16),
    _CmiMrMultiPathMetricType_Type()
)
cmiMrMultiPathMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrMultiPathMetricType.setStatus("current")
_CmiMrDiscovery_ObjectIdentity = ObjectIdentity
cmiMrDiscovery = _CmiMrDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4)
)
_CmiMrMaAdvTable_Object = MibTable
cmiMrMaAdvTable = _CmiMrMaAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    cmiMrMaAdvTable.setStatus("current")
_CmiMrMaAdvEntry_Object = MibTableRow
cmiMrMaAdvEntry = _CmiMrMaAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1)
)
cmiMrMaAdvEntry.setIndexNames(
    (0, "CISCO-MOBILE-IP-MIB", "cmiMrMaAddressType"),
    (0, "CISCO-MOBILE-IP-MIB", "cmiMrMaAddress"),
)
if mibBuilder.loadTexts:
    cmiMrMaAdvEntry.setStatus("current")
_CmiMrMaAddressType_Type = InetAddressType
_CmiMrMaAddressType_Object = MibTableColumn
cmiMrMaAddressType = _CmiMrMaAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 1),
    _CmiMrMaAddressType_Type()
)
cmiMrMaAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiMrMaAddressType.setStatus("current")


class _CmiMrMaAddress_Type(InetAddress):
    """Custom type cmiMrMaAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmiMrMaAddress_Type.__name__ = "InetAddress"
_CmiMrMaAddress_Object = MibTableColumn
cmiMrMaAddress = _CmiMrMaAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 2),
    _CmiMrMaAddress_Type()
)
cmiMrMaAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmiMrMaAddress.setStatus("current")
_CmiMrMaIsHa_Type = TruthValue
_CmiMrMaIsHa_Object = MibTableColumn
cmiMrMaIsHa = _CmiMrMaIsHa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 3),
    _CmiMrMaIsHa_Type()
)
cmiMrMaIsHa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaIsHa.setStatus("current")
_CmiMrMaAdvRcvIf_Type = InterfaceIndex
_CmiMrMaAdvRcvIf_Object = MibTableColumn
cmiMrMaAdvRcvIf = _CmiMrMaAdvRcvIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 4),
    _CmiMrMaAdvRcvIf_Type()
)
cmiMrMaAdvRcvIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvRcvIf.setStatus("current")
_CmiMrMaIfMacAddress_Type = MacAddress
_CmiMrMaIfMacAddress_Object = MibTableColumn
cmiMrMaIfMacAddress = _CmiMrMaIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 5),
    _CmiMrMaIfMacAddress_Type()
)
cmiMrMaIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaIfMacAddress.setStatus("current")


class _CmiMrMaAdvSequence_Type(Unsigned32):
    """Custom type cmiMrMaAdvSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmiMrMaAdvSequence_Type.__name__ = "Unsigned32"
_CmiMrMaAdvSequence_Object = MibTableColumn
cmiMrMaAdvSequence = _CmiMrMaAdvSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 6),
    _CmiMrMaAdvSequence_Type()
)
cmiMrMaAdvSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvSequence.setStatus("current")


class _CmiMrMaAdvFlags_Type(Bits):
    """Custom type cmiMrMaAdvFlags based on Bits"""
    namedValues = NamedValues(
        *(("busy", 5),
          ("foreignAgent", 3),
          ("gre", 1),
          ("homeAgent", 4),
          ("minEnc", 2),
          ("regRequired", 6),
          ("reverseTunnel", 0))
    )

_CmiMrMaAdvFlags_Type.__name__ = "Bits"
_CmiMrMaAdvFlags_Object = MibTableColumn
cmiMrMaAdvFlags = _CmiMrMaAdvFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 7),
    _CmiMrMaAdvFlags_Type()
)
cmiMrMaAdvFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvFlags.setStatus("current")


class _CmiMrMaAdvMaxRegLifetime_Type(Unsigned32):
    """Custom type cmiMrMaAdvMaxRegLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmiMrMaAdvMaxRegLifetime_Type.__name__ = "Unsigned32"
_CmiMrMaAdvMaxRegLifetime_Object = MibTableColumn
cmiMrMaAdvMaxRegLifetime = _CmiMrMaAdvMaxRegLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 8),
    _CmiMrMaAdvMaxRegLifetime_Type()
)
cmiMrMaAdvMaxRegLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvMaxRegLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrMaAdvMaxRegLifetime.setUnits("seconds")


class _CmiMrMaAdvMaxLifetime_Type(Unsigned32):
    """Custom type cmiMrMaAdvMaxLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmiMrMaAdvMaxLifetime_Type.__name__ = "Unsigned32"
_CmiMrMaAdvMaxLifetime_Object = MibTableColumn
cmiMrMaAdvMaxLifetime = _CmiMrMaAdvMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 9),
    _CmiMrMaAdvMaxLifetime_Type()
)
cmiMrMaAdvMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvMaxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrMaAdvMaxLifetime.setUnits("seconds")
_CmiMrMaAdvLifetimeRemaining_Type = Gauge32
_CmiMrMaAdvLifetimeRemaining_Object = MibTableColumn
cmiMrMaAdvLifetimeRemaining = _CmiMrMaAdvLifetimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 10),
    _CmiMrMaAdvLifetimeRemaining_Type()
)
cmiMrMaAdvLifetimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvLifetimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrMaAdvLifetimeRemaining.setUnits("seconds")
_CmiMrMaAdvTimeReceived_Type = TimeStamp
_CmiMrMaAdvTimeReceived_Object = MibTableColumn
cmiMrMaAdvTimeReceived = _CmiMrMaAdvTimeReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 11),
    _CmiMrMaAdvTimeReceived_Type()
)
cmiMrMaAdvTimeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvTimeReceived.setStatus("current")
_CmiMrMaAdvTimeFirstHeard_Type = TimeStamp
_CmiMrMaAdvTimeFirstHeard_Object = MibTableColumn
cmiMrMaAdvTimeFirstHeard = _CmiMrMaAdvTimeFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 12),
    _CmiMrMaAdvTimeFirstHeard_Type()
)
cmiMrMaAdvTimeFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaAdvTimeFirstHeard.setStatus("current")
_CmiMrMaHoldDownRemaining_Type = Gauge32
_CmiMrMaHoldDownRemaining_Object = MibTableColumn
cmiMrMaHoldDownRemaining = _CmiMrMaHoldDownRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 4, 1, 1, 13),
    _CmiMrMaHoldDownRemaining_Type()
)
cmiMrMaHoldDownRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrMaHoldDownRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrMaHoldDownRemaining.setUnits("seconds")
_CmiMrRegistration_ObjectIdentity = ObjectIdentity
cmiMrRegistration = _CmiMrRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5)
)


class _CmiMrRegExtendExpire_Type(Unsigned32):
    """Custom type cmiMrRegExtendExpire based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CmiMrRegExtendExpire_Type.__name__ = "Unsigned32"
_CmiMrRegExtendExpire_Object = MibScalar
cmiMrRegExtendExpire = _CmiMrRegExtendExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 1),
    _CmiMrRegExtendExpire_Type()
)
cmiMrRegExtendExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegExtendExpire.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrRegExtendExpire.setUnits("seconds")


class _CmiMrRegExtendRetry_Type(Unsigned32):
    """Custom type cmiMrRegExtendRetry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CmiMrRegExtendRetry_Type.__name__ = "Unsigned32"
_CmiMrRegExtendRetry_Object = MibScalar
cmiMrRegExtendRetry = _CmiMrRegExtendRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 2),
    _CmiMrRegExtendRetry_Type()
)
cmiMrRegExtendRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegExtendRetry.setStatus("current")


class _CmiMrRegExtendInterval_Type(Unsigned32):
    """Custom type cmiMrRegExtendInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CmiMrRegExtendInterval_Type.__name__ = "Unsigned32"
_CmiMrRegExtendInterval_Object = MibScalar
cmiMrRegExtendInterval = _CmiMrRegExtendInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 3),
    _CmiMrRegExtendInterval_Type()
)
cmiMrRegExtendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegExtendInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrRegExtendInterval.setUnits("seconds")


class _CmiMrRegLifetime_Type(Unsigned32):
    """Custom type cmiMrRegLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_CmiMrRegLifetime_Type.__name__ = "Unsigned32"
_CmiMrRegLifetime_Object = MibScalar
cmiMrRegLifetime = _CmiMrRegLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 4),
    _CmiMrRegLifetime_Type()
)
cmiMrRegLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrRegLifetime.setUnits("seconds")


class _CmiMrRegRetransInitial_Type(Unsigned32):
    """Custom type cmiMrRegRetransInitial based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CmiMrRegRetransInitial_Type.__name__ = "Unsigned32"
_CmiMrRegRetransInitial_Object = MibScalar
cmiMrRegRetransInitial = _CmiMrRegRetransInitial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 5),
    _CmiMrRegRetransInitial_Type()
)
cmiMrRegRetransInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegRetransInitial.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrRegRetransInitial.setUnits("milli-seconds")


class _CmiMrRegRetransMax_Type(Unsigned32):
    """Custom type cmiMrRegRetransMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CmiMrRegRetransMax_Type.__name__ = "Unsigned32"
_CmiMrRegRetransMax_Object = MibScalar
cmiMrRegRetransMax = _CmiMrRegRetransMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 6),
    _CmiMrRegRetransMax_Type()
)
cmiMrRegRetransMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegRetransMax.setStatus("current")
if mibBuilder.loadTexts:
    cmiMrRegRetransMax.setUnits("milli-seconds")


class _CmiMrRegRetransLimit_Type(Unsigned32):
    """Custom type cmiMrRegRetransLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CmiMrRegRetransLimit_Type.__name__ = "Unsigned32"
_CmiMrRegRetransLimit_Object = MibScalar
cmiMrRegRetransLimit = _CmiMrRegRetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 7),
    _CmiMrRegRetransLimit_Type()
)
cmiMrRegRetransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiMrRegRetransLimit.setStatus("current")
_CmiMrRegNewHa_Type = Counter32
_CmiMrRegNewHa_Object = MibScalar
cmiMrRegNewHa = _CmiMrRegNewHa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 5, 5, 8),
    _CmiMrRegNewHa_Type()
)
cmiMrRegNewHa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiMrRegNewHa.setStatus("current")
_CmiTrapObjects_ObjectIdentity = ObjectIdentity
cmiTrapObjects = _CmiTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6)
)


class _CmiTrapControl_Type(Bits):
    """Custom type cmiTrapControl based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cmiHaMaxBindingsNotif", 4),
          ("cmiHaMnRegFailedTrap", 3),
          ("cmiMrCoaChangeTrap", 1),
          ("cmiMrNewMATrap", 2),
          ("cmiMrStateChangeTrap", 0))
    )

_CmiTrapControl_Type.__name__ = "Bits"
_CmiTrapControl_Object = MibScalar
cmiTrapControl = _CmiTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 1),
    _CmiTrapControl_Type()
)
cmiTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmiTrapControl.setStatus("current")
_CmiNtRegCOAType_Type = InetAddressType
_CmiNtRegCOAType_Object = MibScalar
cmiNtRegCOAType = _CmiNtRegCOAType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 3),
    _CmiNtRegCOAType_Type()
)
cmiNtRegCOAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegCOAType.setStatus("current")
_CmiNtRegCOA_Type = InetAddress
_CmiNtRegCOA_Object = MibScalar
cmiNtRegCOA = _CmiNtRegCOA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 4),
    _CmiNtRegCOA_Type()
)
cmiNtRegCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegCOA.setStatus("current")
_CmiNtRegHAAddrType_Type = InetAddressType
_CmiNtRegHAAddrType_Object = MibScalar
cmiNtRegHAAddrType = _CmiNtRegHAAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 5),
    _CmiNtRegHAAddrType_Type()
)
cmiNtRegHAAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegHAAddrType.setStatus("current")
_CmiNtRegHomeAgent_Type = InetAddress
_CmiNtRegHomeAgent_Object = MibScalar
cmiNtRegHomeAgent = _CmiNtRegHomeAgent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 6),
    _CmiNtRegHomeAgent_Type()
)
cmiNtRegHomeAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegHomeAgent.setStatus("current")
_CmiNtRegHomeAddressType_Type = InetAddressType
_CmiNtRegHomeAddressType_Object = MibScalar
cmiNtRegHomeAddressType = _CmiNtRegHomeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 7),
    _CmiNtRegHomeAddressType_Type()
)
cmiNtRegHomeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegHomeAddressType.setStatus("current")
_CmiNtRegHomeAddress_Type = IpAddress
_CmiNtRegHomeAddress_Object = MibScalar
cmiNtRegHomeAddress = _CmiNtRegHomeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 8),
    _CmiNtRegHomeAddress_Type()
)
cmiNtRegHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegHomeAddress.setStatus("current")


class _CmiNtRegNAI_Type(OctetString):
    """Custom type cmiNtRegNAI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CmiNtRegNAI_Type.__name__ = "OctetString"
_CmiNtRegNAI_Object = MibScalar
cmiNtRegNAI = _CmiNtRegNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 9),
    _CmiNtRegNAI_Type()
)
cmiNtRegNAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegNAI.setStatus("current")


class _CmiNtRegDeniedCode_Type(Integer32):
    """Custom type cmiNtRegDeniedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139)
        )
    )
    namedValues = NamedValues(
        *(("admProhibited", 129),
          ("encapsulationUnavailable", 139),
          ("faAuthenticationFailure", 132),
          ("idMismatch", 133),
          ("insufficientResource", 130),
          ("mnAuthenticationFailure", 131),
          ("poorlyFormedRequest", 134),
          ("reasonUnspecified", 128),
          ("reverseTunnelBitNotSet", 138),
          ("reverseTunnelUnavailable", 137),
          ("tooManyBindings", 135),
          ("unknownHA", 136))
    )


_CmiNtRegDeniedCode_Type.__name__ = "Integer32"
_CmiNtRegDeniedCode_Object = MibScalar
cmiNtRegDeniedCode = _CmiNtRegDeniedCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 1, 6, 10),
    _CmiNtRegDeniedCode_Type()
)
cmiNtRegDeniedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmiNtRegDeniedCode.setStatus("current")
_CiscoMobileIpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoMobileIpMIBConformance = _CiscoMobileIpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3)
)
_CiscoMobileIpCompliances_ObjectIdentity = ObjectIdentity
ciscoMobileIpCompliances = _CiscoMobileIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1)
)
_CiscoMobileIpGroups_ObjectIdentity = ObjectIdentity
ciscoMobileIpGroups = _CiscoMobileIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2)
)
faCOAEntry.registerAugmentions(
    ("CISCO-MOBILE-IP-MIB",
     "cmiFaCoaEntry")
)
cmiFaCoaEntry.setIndexNames(*faCOAEntry.getIndexNames())
haMobilityBindingEntry.registerAugmentions(
    ("CISCO-MOBILE-IP-MIB",
     "cmiHaRegMobilityBindingEntry")
)
cmiHaRegMobilityBindingEntry.setIndexNames(*haMobilityBindingEntry.getIndexNames())
mnRegistrationEntry.registerAugmentions(
    ("CISCO-MOBILE-IP-MIB",
     "cmiMnRegistrationEntry")
)
cmiMnRegistrationEntry.setIndexNames(*mnRegistrationEntry.getIndexNames())
mnHAEntry.registerAugmentions(
    ("CISCO-MOBILE-IP-MIB",
     "cmiMrHAEntry")
)
cmiMrHAEntry.setIndexNames(*mnHAEntry.getIndexNames())

# Managed Objects groups

ciscoMobileIpFaRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 1)
)
ciscoMobileIpFaRegGroup.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiFaRegTotalVisitors")
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaRegGroup.setStatus("obsolete")

ciscoMobileIpHaRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 2)
)
ciscoMobileIpHaRegGroup.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalMobilityBindings")
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroup.setStatus("obsolete")

ciscoMobileIpFaRegGroupV12R02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 3)
)
ciscoMobileIpFaRegGroupV12R02.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiFaRegTotalVisitors"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAgentAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeGranted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegFlags"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDLow"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDHigh"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIsAccepted"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaRegGroupV12R02.setStatus("deprecated")

ciscoMobileIpHaRegGroupV12R02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 4)
)
ciscoMobileIpHaRegGroupV12R02.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalMobilityBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifierType"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifier"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServAcceptedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServDeniedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegOverallServTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServAcceptedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedCode"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcLocRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcLocInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcLoc"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcLocInLastMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcByAAARegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcByAAAInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcAAAInLastByMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegAvgTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxTimeRegsProcByAAA"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV12R02.setStatus("deprecated")

ciscoMobileIpHaRedunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 5)
)
ciscoMobileIpHaRedunGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRedunSentBUs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunFailedBUs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunReceivedBUAcks"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunTotalSentBUs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunReceivedBUs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunSentBUAcks"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunSentBIReqs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunFailedBIReqs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunTotalSentBIReqs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunReceivedBIReps"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunDroppedBIReps"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunSentBIAcks"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunReceivedBIReqs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunSentBIReps"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunFailedBIReps"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunTotalSentBIReps"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunReceivedBIAcks"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunDroppedBIAcks"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRedunSecViolations"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRedunGroup.setStatus("current")

ciscoMobileIpSecAssocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 6)
)
ciscoMobileIpSecAssocGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiSecAssocsCount"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecAlgorithmType"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecAlgorithmMode"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecKey"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecReplayMethod"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecStatus"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpSecAssocGroup.setStatus("deprecated")

ciscoMobileIpSecViolationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 7)
)
ciscoMobileIpSecViolationGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiSecTotalViolations"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecRecentViolationSPI"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecRecentViolationTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecRecentViolationIDLow"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecRecentViolationIDHigh"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecRecentViolationReason"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpSecViolationGroup.setStatus("current")

ciscoMobileIpMaRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 8)
)
ciscoMobileIpMaRegGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMaRegMaxInMinuteRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaRegDateMaxRegsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaRegInLastMinuteRegs"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMaRegGroup.setStatus("current")

ciscoMobileIpFaRegGroupV12R03 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 9)
)
ciscoMobileIpFaRegGroupV12R03.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiFaRegTotalVisitors"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAgentAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeGranted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegFlags"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDLow"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDHigh"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRepliesValidRelayMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRepliesValidRelayToMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRepliesValidRelayToMN"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaRegGroupV12R03.setStatus("deprecated")

ciscoMobileIpHaRegGroupV12R03 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 10)
)
ciscoMobileIpHaRegGroupV12R03.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalMobilityBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifierType"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifier"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServAcceptedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServDeniedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegOverallServTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServAcceptedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedCode"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcLocRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcLocInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcLoc"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcLocInLastMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcByAAARegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcByAAAInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcAAAInLastByMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegAvgTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaEncapUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNAICheckFailures"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsDiscarded"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV12R03.setStatus("deprecated")

ciscoMobileIpFaRegGroupV12R03r1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 11)
)
ciscoMobileIpFaRegGroupV12R03r1.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiFaRegTotalVisitors"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAgentAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeGranted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDLow"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDHigh"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegFlagsRev1"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorChallengeValue"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRepliesValidRelayMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRepliesValidRelayToMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRepliesValidRelayToMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReverseTunnelUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReverseTunnelBitNotSet"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaMnTooDistant"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeliveryStyleUnsupported"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaUnknownChallenge"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaMissingChallenge"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaStaleChallenge"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCvsesFromMnRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCvsesFromHaRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaNvsesFromMnNeglected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaNvsesFromHaNeglected"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaRegGroupV12R03r1.setStatus("deprecated")

ciscoMobileIpHaRegGroupV12R03r1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 12)
)
ciscoMobileIpHaRegGroupV12R03r1.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalMobilityBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifierType"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifier"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMobilityBindingRegFlags"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServAcceptedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServDeniedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegOverallServTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServAcceptedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedCode"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcLocRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcLocInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcLoc"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcLocInLastMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcByAAARegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcByAAAInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcAAAInLastByMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegAvgTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaEncapUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNAICheckFailures"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReverseTunnelUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReverseTunnelBitNotSet"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaEncapsulationUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaCvsesFromMnRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaCvsesFromFaRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNvsesFromMnNeglected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNvsesFromFaNeglected"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV12R03r1.setStatus("deprecated")

ciscoMobileIpFaAdvertisementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 13)
)
ciscoMobileIpFaAdvertisementGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiFaAdvertIsBusy"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaAdvertRegRequired"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaAdvertChallengeWindow"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaAdvertChallengeValue"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaAdvertisementGroup.setStatus("current")

ciscoMobileIpFaSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 14)
)
ciscoMobileIpFaSystemGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiFaRevTunnelSupported"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaChallengeSupported"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaEncapDeliveryStyleSupported"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReverseTunnelEnable"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaChallengeEnable"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaAdvertChallengeChapSPI"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCoaInterfaceOnly"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCoaTransmitOnly"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCoaRegAsymLink"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaSystemGroup.setStatus("current")

ciscoMobileIpMnDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 15)
)
ciscoMobileIpMnDiscoveryGroup.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiMnAdvFlags")
)
if mibBuilder.loadTexts:
    ciscoMobileIpMnDiscoveryGroup.setStatus("current")

ciscoMobileIpMnRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 16)
)
ciscoMobileIpMnRegistrationGroup.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiMnRegFlags")
)
if mibBuilder.loadTexts:
    ciscoMobileIpMnRegistrationGroup.setStatus("current")

ciscoMobileIpHaMobNetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 17)
)
ciscoMobileIpHaMobNetGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaMrDynamic"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMrStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMobNetDynamic"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMobNetStatus"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaMobNetGroup.setStatus("current")

ciscoMobileIpMrSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 18)
)
ciscoMobileIpMrSystemGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrReverseTunnel"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedundancyGroup"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddr"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetPfxLen"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHaTunnelIfIndex"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHAPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHABest"),
        ("CISCO-MOBILE-IP-MIB", "cmiMRIfDescription"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfHoldDown"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRoamPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitPeriodic"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransInitial"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransMax"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransLimit"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCurrent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCount"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGwType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGw"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetry"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetryRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrBetterIfDetected"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStateActive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStatePassive"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrSystemGroup.setStatus("deprecated")

ciscoMobileIpMrDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 19)
)
ciscoMobileIpMrDiscoveryGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrMaIsHa"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvRcvIf"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaIfMacAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvSequence"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvFlags"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvMaxRegLifetime"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvMaxLifetime"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvLifetimeRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvTimeReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvTimeFirstHeard"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaHoldDownRemaining"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrDiscoveryGroup.setStatus("current")

ciscoMobileIpMrRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 20)
)
ciscoMobileIpMrRegistrationGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrRegExtendExpire"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegExtendRetry"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegExtendInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegLifetime"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegRetransInitial"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegRetransMax"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegRetransLimit"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRegNewHa"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrRegistrationGroup.setStatus("current")

ciscoMobileIpTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 21)
)
ciscoMobileIpTrapObjectsGroup.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiTrapControl")
)
if mibBuilder.loadTexts:
    ciscoMobileIpTrapObjectsGroup.setStatus("deprecated")

ciscoMobileIpSecAssocGroupV12R02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 23)
)
ciscoMobileIpSecAssocGroupV12R02.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiSecAssocsCount"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecAlgorithmType"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecAlgorithmMode"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecReplayMethod"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiSecKey2"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpSecAssocGroupV12R02.setStatus("current")

cmiMaAdvertisementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 24)
)
cmiMaAdvertisementGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMaInterfaceAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaInterfaceAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvMaxRegLifetime"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvPrefixLengthInclusion"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvMaxInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvMinInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvMaxAdvLifetime"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvResponseSolicitationOnly"),
        ("CISCO-MOBILE-IP-MIB", "cmiMaAdvStatus"))
)
if mibBuilder.loadTexts:
    cmiMaAdvertisementGroup.setStatus("current")

ciscoMobileIpMrSystemGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 25)
)
ciscoMobileIpMrSystemGroupV1.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrReverseTunnel"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedundancyGroup"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddr"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetPfxLen"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHaTunnelIfIndex"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHAPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHABest"),
        ("CISCO-MOBILE-IP-MIB", "cmiMRIfDescription"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfHoldDown"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRoamPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitPeriodic"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransInitial"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransMax"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransLimit"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCurrent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCount"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGwType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGw"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetry"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetryRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegistration"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaOnly"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrBetterIfDetected"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStateActive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStatePassive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrCollocatedTunnel"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrSystemGroupV1.setStatus("deprecated")

ciscoMobileIpMrSystemGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 26)
)
ciscoMobileIpMrSystemGroupV2.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrReverseTunnel"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedundancyGroup"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddr"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetPfxLen"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHaTunnelIfIndex"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHAPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHABest"),
        ("CISCO-MOBILE-IP-MIB", "cmiMRIfDescription"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfHoldDown"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRoamPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitPeriodic"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransInitial"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransMax"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransLimit"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCurrent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCount"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGwType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGw"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetry"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetryRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegistration"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaOnly"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaEnable"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrBetterIfDetected"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStateActive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStatePassive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrCollocatedTunnel"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrSystemGroupV2.setStatus("deprecated")

ciscoMobileIpFaRegGroupV12R03r2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 27)
)
ciscoMobileIpFaRegGroupV12R03r2.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiFaRegTotalVisitors"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorHomeAgentAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeGranted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorTimeRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDLow"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIDHigh"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegIsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorRegFlagsRev1"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaRegVisitorChallengeValue"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaInitRegRepliesValidRelayMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReRegRepliesValidRelayToMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsRelayed"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRepliesValidFromHA"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeRegRepliesValidRelayToMN"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReverseTunnelUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaReverseTunnelBitNotSet"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaMnTooDistant"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaDeliveryStyleUnsupported"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaUnknownChallenge"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaMissingChallenge"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaStaleChallenge"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCvsesFromMnRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaCvsesFromHaRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaNvsesFromMnNeglected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaNvsesFromHaNeglected"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaTotalRegRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaTotalRegReplies"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaMnFaAuthFailures"),
        ("CISCO-MOBILE-IP-MIB", "cmiFaMnAAAAuthFailures"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpFaRegGroupV12R03r2.setStatus("current")

ciscoMobileIpHaRegGroupV12R03r2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 28)
)
ciscoMobileIpHaRegGroupV12R03r2.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalMobilityBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifierType"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIdentifier"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMobilityBindingRegFlags"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServAcceptedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegServDeniedRequests"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegOverallServTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServAcceptedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedTime"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRecentServDeniedCode"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcLocRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcLocInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcLoc"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcLocInLastMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalProcByAAARegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxProcByAAAInMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegDateMaxRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegProcAAAInLastByMinRegs"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegAvgTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMaxTimeRegsProcByAAA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaEncapUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNAICheckFailures"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaInitRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsReceived"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsAccepted"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsDenied"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaDeRegRequestsDiscarded"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReverseTunnelUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaReverseTunnelBitNotSet"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaEncapsulationUnavailable"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaCvsesFromMnRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaCvsesFromFaRejected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNvsesFromMnNeglected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaNvsesFromFaNeglected"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMnHaAuthFailures"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMnAAAAuthFailures"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV12R03r2.setStatus("current")

ciscoMobileIpTrapObjectsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 29)
)
ciscoMobileIpTrapObjectsGroupV2.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiTrapControl"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegCOA"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegCOAType"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHAAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHomeAgent"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHomeAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHomeAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegNAI"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegDeniedCode"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpTrapObjectsGroupV2.setStatus("current")

ciscoMobileIpMrSystemGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 31)
)
ciscoMobileIpMrSystemGroupV3.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrReverseTunnel"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedundancyGroup"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetAddr"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetPfxLen"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMobNetStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHaTunnelIfIndex"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHAPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrHABest"),
        ("CISCO-MOBILE-IP-MIB", "cmiMRIfDescription"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfHoldDown"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRoamPriority"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitPeriodic"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitInterval"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransInitial"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransMax"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransLimit"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCurrent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfSolicitRetransCount"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGwType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaDefaultGw"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetry"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegRetryRemaining"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaRegistration"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaOnly"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfCCoaEnable"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRoamStatus"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRegisteredCoAType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRegisteredCoA"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRegisteredMaAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfRegisteredMaAddr"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrBetterIfDetected"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelPktsSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesRcvd"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrTunnelBytesSent"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStateActive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrRedStatePassive"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrCollocatedTunnel"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrSystemGroupV3.setStatus("current")

ciscoMobileIpHaRegGroupV12R03r2Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 32)
)
ciscoMobileIpHaRegGroupV12R03r2Sup1.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIfDescription"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIfBandwidth"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIfID"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegMnIfPathMetricType"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV12R03r2Sup1.setStatus("current")

ciscoMobileIpHaMobNetGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 33)
)
ciscoMobileIpHaMobNetGroupSup1.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaMrMultiPath"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMrMultiPathMetricType"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaMobNetGroupSup1.setStatus("current")

ciscoMobileIpMrSystemGroupV3Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 34)
)
ciscoMobileIpMrSystemGroupV3Sup1.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrIfHaTunnelIfIndex"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrIfID"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMultiPath"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMultiPathMetricType"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrSystemGroupV3Sup1.setStatus("current")

ciscoMobileIpHaRegGroupV12R03r2Sup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 35)
)
ciscoMobileIpHaRegGroupV12R03r2Sup2.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiHaRegMobilityBindingMacAddress")
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV12R03r2Sup2.setStatus("current")

ciscoMobileIpHaSystemGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 36)
)
ciscoMobileIpHaSystemGroupV1.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiHaSystemVersion")
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaSystemGroupV1.setStatus("current")

ciscoMobileIpHaRegGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 38)
)
ciscoMobileIpHaRegGroupV1.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiHaMaximumBindings")
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegGroupV1.setStatus("current")

ciscoMobileIpHaRegIntervalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 39)
)
ciscoMobileIpHaRegIntervalStatsGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegIntervalSize"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegIntervalMaxActiveBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegInterval3gpp2MaxActiveBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegIntervalWimaxMaxActiveBindings"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegIntervalStatsGroup.setStatus("current")

ciscoMobileIpHaRegTunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 40)
)
ciscoMobileIpHaRegTunnelStatsGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsTunnelType"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsNumUsers"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsDataRateInt"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsInBitRate"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsInPktRate"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsInBytes"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsInPkts"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsOutBitRate"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsOutPktRate"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsOutBytes"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaRegTunnelStatsOutPkts"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpHaRegTunnelStatsGroup.setStatus("current")


# Notification objects

cmiMrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 0, 1)
)
cmiMrStateChange.setObjects(
    ("MIP-MIB", "mnState")
)
if mibBuilder.loadTexts:
    cmiMrStateChange.setStatus(
        "current"
    )

cmiMrCoaChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 0, 2)
)
cmiMrCoaChange.setObjects(
      *(("MIP-MIB", "mnRegCOA"),
        ("MIP-MIB", "mnRegAgentAddress"))
)
if mibBuilder.loadTexts:
    cmiMrCoaChange.setStatus(
        "current"
    )

cmiMrNewMA = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 0, 3)
)
cmiMrNewMA.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrMaIsHa"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvFlags"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrMaAdvRcvIf"))
)
if mibBuilder.loadTexts:
    cmiMrNewMA.setStatus(
        "current"
    )

cmiHaMnRegReqFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 0, 4)
)
cmiHaMnRegReqFailed.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiNtRegCOAType"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegCOA"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHAAddrType"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHomeAgent"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHomeAddressType"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegHomeAddress"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegNAI"),
        ("CISCO-MOBILE-IP-MIB", "cmiNtRegDeniedCode"))
)
if mibBuilder.loadTexts:
    cmiHaMnRegReqFailed.setStatus(
        "current"
    )

cmiHaMaxBindingsNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 0, 5)
)
cmiHaMaxBindingsNotif.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiHaRegTotalMobilityBindings"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMaximumBindings"))
)
if mibBuilder.loadTexts:
    cmiHaMaxBindingsNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoMobileIpMrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 22)
)
ciscoMobileIpMrNotificationGroup.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrStateChange"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrCoaChange"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrNewMA"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrNotificationGroup.setStatus(
        "deprecated"
    )

ciscoMobileIpMrNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 30)
)
ciscoMobileIpMrNotificationGroupV2.setObjects(
      *(("CISCO-MOBILE-IP-MIB", "cmiMrStateChange"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrCoaChange"),
        ("CISCO-MOBILE-IP-MIB", "cmiMrNewMA"),
        ("CISCO-MOBILE-IP-MIB", "cmiHaMnRegReqFailed"))
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrNotificationGroupV2.setStatus(
        "current"
    )

ciscoMobileIpMrNotificationGroupV3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 2, 37)
)
ciscoMobileIpMrNotificationGroupV3.setObjects(
    ("CISCO-MOBILE-IP-MIB", "cmiHaMaxBindingsNotif")
)
if mibBuilder.loadTexts:
    ciscoMobileIpMrNotificationGroupV3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMobileIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMobileIpCompliance.setStatus(
        "obsolete"
    )

ciscoMobileIpComplianceV12R02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R02.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R03.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R03r1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R03r1.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R04 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R04.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R05 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R05.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R06 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R06.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R07 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R07.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R08 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R08.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R09 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R09.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 11)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R10.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceV12R11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 12)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceV12R11.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 13)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceRev1.setStatus(
        "deprecated"
    )

ciscoMobileIpComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 174, 3, 1, 14)
)
if mibBuilder.loadTexts:
    ciscoMobileIpComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MOBILE-IP-MIB",
    **{"CmiRegistrationFlags": CmiRegistrationFlags,
       "CmiEntityIdentifierType": CmiEntityIdentifierType,
       "CmiEntityIdentifier": CmiEntityIdentifier,
       "CmiSpi": CmiSpi,
       "CmiMultiPathMetricType": CmiMultiPathMetricType,
       "CmiTunnelType": CmiTunnelType,
       "ciscoMobileIpMIB": ciscoMobileIpMIB,
       "ciscoMobileIpMIBNotifications": ciscoMobileIpMIBNotifications,
       "cmiMrStateChange": cmiMrStateChange,
       "cmiMrCoaChange": cmiMrCoaChange,
       "cmiMrNewMA": cmiMrNewMA,
       "cmiHaMnRegReqFailed": cmiHaMnRegReqFailed,
       "cmiHaMaxBindingsNotif": cmiHaMaxBindingsNotif,
       "ciscoMobileIpMIBObjects": ciscoMobileIpMIBObjects,
       "cmiFa": cmiFa,
       "cmiFaReg": cmiFaReg,
       "cmiFaRegTotalVisitors": cmiFaRegTotalVisitors,
       "cmiFaRegVisitorTable": cmiFaRegVisitorTable,
       "cmiFaRegVisitorEntry": cmiFaRegVisitorEntry,
       "cmiFaRegVisitorIdentifierType": cmiFaRegVisitorIdentifierType,
       "cmiFaRegVisitorIdentifier": cmiFaRegVisitorIdentifier,
       "cmiFaRegVisitorHomeAddress": cmiFaRegVisitorHomeAddress,
       "cmiFaRegVisitorHomeAgentAddress": cmiFaRegVisitorHomeAgentAddress,
       "cmiFaRegVisitorTimeGranted": cmiFaRegVisitorTimeGranted,
       "cmiFaRegVisitorTimeRemaining": cmiFaRegVisitorTimeRemaining,
       "cmiFaRegVisitorRegFlags": cmiFaRegVisitorRegFlags,
       "cmiFaRegVisitorRegIDLow": cmiFaRegVisitorRegIDLow,
       "cmiFaRegVisitorRegIDHigh": cmiFaRegVisitorRegIDHigh,
       "cmiFaRegVisitorRegIsAccepted": cmiFaRegVisitorRegIsAccepted,
       "cmiFaRegVisitorRegFlagsRev1": cmiFaRegVisitorRegFlagsRev1,
       "cmiFaRegVisitorChallengeValue": cmiFaRegVisitorChallengeValue,
       "cmiFaInitRegRequestsReceived": cmiFaInitRegRequestsReceived,
       "cmiFaInitRegRequestsRelayed": cmiFaInitRegRequestsRelayed,
       "cmiFaInitRegRequestsDenied": cmiFaInitRegRequestsDenied,
       "cmiFaInitRegRequestsDiscarded": cmiFaInitRegRequestsDiscarded,
       "cmiFaInitRegRepliesValidFromHA": cmiFaInitRegRepliesValidFromHA,
       "cmiFaInitRegRepliesValidRelayMN": cmiFaInitRegRepliesValidRelayMN,
       "cmiFaReRegRequestsReceived": cmiFaReRegRequestsReceived,
       "cmiFaReRegRequestsRelayed": cmiFaReRegRequestsRelayed,
       "cmiFaReRegRequestsDenied": cmiFaReRegRequestsDenied,
       "cmiFaReRegRequestsDiscarded": cmiFaReRegRequestsDiscarded,
       "cmiFaReRegRepliesValidFromHA": cmiFaReRegRepliesValidFromHA,
       "cmiFaReRegRepliesValidRelayToMN": cmiFaReRegRepliesValidRelayToMN,
       "cmiFaDeRegRequestsReceived": cmiFaDeRegRequestsReceived,
       "cmiFaDeRegRequestsRelayed": cmiFaDeRegRequestsRelayed,
       "cmiFaDeRegRequestsDenied": cmiFaDeRegRequestsDenied,
       "cmiFaDeRegRequestsDiscarded": cmiFaDeRegRequestsDiscarded,
       "cmiFaDeRegRepliesValidFromHA": cmiFaDeRegRepliesValidFromHA,
       "cmiFaDeRegRepliesValidRelayToMN": cmiFaDeRegRepliesValidRelayToMN,
       "cmiFaReverseTunnelUnavailable": cmiFaReverseTunnelUnavailable,
       "cmiFaReverseTunnelBitNotSet": cmiFaReverseTunnelBitNotSet,
       "cmiFaMnTooDistant": cmiFaMnTooDistant,
       "cmiFaDeliveryStyleUnsupported": cmiFaDeliveryStyleUnsupported,
       "cmiFaUnknownChallenge": cmiFaUnknownChallenge,
       "cmiFaMissingChallenge": cmiFaMissingChallenge,
       "cmiFaStaleChallenge": cmiFaStaleChallenge,
       "cmiFaCvsesFromMnRejected": cmiFaCvsesFromMnRejected,
       "cmiFaCvsesFromHaRejected": cmiFaCvsesFromHaRejected,
       "cmiFaNvsesFromMnNeglected": cmiFaNvsesFromMnNeglected,
       "cmiFaNvsesFromHaNeglected": cmiFaNvsesFromHaNeglected,
       "cmiFaTotalRegRequests": cmiFaTotalRegRequests,
       "cmiFaTotalRegReplies": cmiFaTotalRegReplies,
       "cmiFaMnFaAuthFailures": cmiFaMnFaAuthFailures,
       "cmiFaMnAAAAuthFailures": cmiFaMnAAAAuthFailures,
       "cmiFaAdvertisement": cmiFaAdvertisement,
       "cmiFaAdvertConfTable": cmiFaAdvertConfTable,
       "cmiFaAdvertConfEntry": cmiFaAdvertConfEntry,
       "cmiFaAdvertIsBusy": cmiFaAdvertIsBusy,
       "cmiFaAdvertRegRequired": cmiFaAdvertRegRequired,
       "cmiFaAdvertChallengeWindow": cmiFaAdvertChallengeWindow,
       "cmiFaAdvertChallengeTable": cmiFaAdvertChallengeTable,
       "cmiFaAdvertChallengeEntry": cmiFaAdvertChallengeEntry,
       "cmiFaAdvertChallengeIndex": cmiFaAdvertChallengeIndex,
       "cmiFaAdvertChallengeValue": cmiFaAdvertChallengeValue,
       "cmiFaSystem": cmiFaSystem,
       "cmiFaRevTunnelSupported": cmiFaRevTunnelSupported,
       "cmiFaChallengeSupported": cmiFaChallengeSupported,
       "cmiFaEncapDeliveryStyleSupported": cmiFaEncapDeliveryStyleSupported,
       "cmiFaInterfaceTable": cmiFaInterfaceTable,
       "cmiFaInterfaceEntry": cmiFaInterfaceEntry,
       "cmiFaReverseTunnelEnable": cmiFaReverseTunnelEnable,
       "cmiFaChallengeEnable": cmiFaChallengeEnable,
       "cmiFaAdvertChallengeChapSPI": cmiFaAdvertChallengeChapSPI,
       "cmiFaCoaTable": cmiFaCoaTable,
       "cmiFaCoaEntry": cmiFaCoaEntry,
       "cmiFaCoaInterfaceOnly": cmiFaCoaInterfaceOnly,
       "cmiFaCoaTransmitOnly": cmiFaCoaTransmitOnly,
       "cmiFaCoaRegAsymLink": cmiFaCoaRegAsymLink,
       "cmiHa": cmiHa,
       "cmiHaReg": cmiHaReg,
       "cmiHaRegTotalMobilityBindings": cmiHaRegTotalMobilityBindings,
       "cmiHaRegMobilityBindingTable": cmiHaRegMobilityBindingTable,
       "cmiHaRegMobilityBindingEntry": cmiHaRegMobilityBindingEntry,
       "cmiHaRegMnIdentifierType": cmiHaRegMnIdentifierType,
       "cmiHaRegMnIdentifier": cmiHaRegMnIdentifier,
       "cmiHaRegMobilityBindingRegFlags": cmiHaRegMobilityBindingRegFlags,
       "cmiHaRegMnIfDescription": cmiHaRegMnIfDescription,
       "cmiHaRegMnIfBandwidth": cmiHaRegMnIfBandwidth,
       "cmiHaRegMnIfID": cmiHaRegMnIfID,
       "cmiHaRegMnIfPathMetricType": cmiHaRegMnIfPathMetricType,
       "cmiHaRegMobilityBindingMacAddress": cmiHaRegMobilityBindingMacAddress,
       "cmiHaRegCounterTable": cmiHaRegCounterTable,
       "cmiHaRegCounterEntry": cmiHaRegCounterEntry,
       "cmiHaRegMnIdType": cmiHaRegMnIdType,
       "cmiHaRegMnId": cmiHaRegMnId,
       "cmiHaRegServAcceptedRequests": cmiHaRegServAcceptedRequests,
       "cmiHaRegServDeniedRequests": cmiHaRegServDeniedRequests,
       "cmiHaRegOverallServTime": cmiHaRegOverallServTime,
       "cmiHaRegRecentServAcceptedTime": cmiHaRegRecentServAcceptedTime,
       "cmiHaRegRecentServDeniedTime": cmiHaRegRecentServDeniedTime,
       "cmiHaRegRecentServDeniedCode": cmiHaRegRecentServDeniedCode,
       "cmiHaRegTotalProcLocRegs": cmiHaRegTotalProcLocRegs,
       "cmiHaRegMaxProcLocInMinRegs": cmiHaRegMaxProcLocInMinRegs,
       "cmiHaRegDateMaxRegsProcLoc": cmiHaRegDateMaxRegsProcLoc,
       "cmiHaRegProcLocInLastMinRegs": cmiHaRegProcLocInLastMinRegs,
       "cmiHaRegTotalProcByAAARegs": cmiHaRegTotalProcByAAARegs,
       "cmiHaRegMaxProcByAAAInMinRegs": cmiHaRegMaxProcByAAAInMinRegs,
       "cmiHaRegDateMaxRegsProcByAAA": cmiHaRegDateMaxRegsProcByAAA,
       "cmiHaRegProcAAAInLastByMinRegs": cmiHaRegProcAAAInLastByMinRegs,
       "cmiHaRegAvgTimeRegsProcByAAA": cmiHaRegAvgTimeRegsProcByAAA,
       "cmiHaRegMaxTimeRegsProcByAAA": cmiHaRegMaxTimeRegsProcByAAA,
       "cmiHaRegRequestsReceived": cmiHaRegRequestsReceived,
       "cmiHaRegRequestsDenied": cmiHaRegRequestsDenied,
       "cmiHaRegRequestsDiscarded": cmiHaRegRequestsDiscarded,
       "cmiHaEncapUnavailable": cmiHaEncapUnavailable,
       "cmiHaNAICheckFailures": cmiHaNAICheckFailures,
       "cmiHaInitRegRequestsReceived": cmiHaInitRegRequestsReceived,
       "cmiHaInitRegRequestsAccepted": cmiHaInitRegRequestsAccepted,
       "cmiHaInitRegRequestsDenied": cmiHaInitRegRequestsDenied,
       "cmiHaInitRegRequestsDiscarded": cmiHaInitRegRequestsDiscarded,
       "cmiHaReRegRequestsReceived": cmiHaReRegRequestsReceived,
       "cmiHaReRegRequestsAccepted": cmiHaReRegRequestsAccepted,
       "cmiHaReRegRequestsDenied": cmiHaReRegRequestsDenied,
       "cmiHaReRegRequestsDiscarded": cmiHaReRegRequestsDiscarded,
       "cmiHaDeRegRequestsReceived": cmiHaDeRegRequestsReceived,
       "cmiHaDeRegRequestsAccepted": cmiHaDeRegRequestsAccepted,
       "cmiHaDeRegRequestsDenied": cmiHaDeRegRequestsDenied,
       "cmiHaDeRegRequestsDiscarded": cmiHaDeRegRequestsDiscarded,
       "cmiHaReverseTunnelUnavailable": cmiHaReverseTunnelUnavailable,
       "cmiHaReverseTunnelBitNotSet": cmiHaReverseTunnelBitNotSet,
       "cmiHaEncapsulationUnavailable": cmiHaEncapsulationUnavailable,
       "cmiHaCvsesFromMnRejected": cmiHaCvsesFromMnRejected,
       "cmiHaCvsesFromFaRejected": cmiHaCvsesFromFaRejected,
       "cmiHaNvsesFromMnNeglected": cmiHaNvsesFromMnNeglected,
       "cmiHaNvsesFromFaNeglected": cmiHaNvsesFromFaNeglected,
       "cmiHaMnHaAuthFailures": cmiHaMnHaAuthFailures,
       "cmiHaMnAAAAuthFailures": cmiHaMnAAAAuthFailures,
       "cmiHaMaximumBindings": cmiHaMaximumBindings,
       "cmiHaRegIntervalSize": cmiHaRegIntervalSize,
       "cmiHaRegIntervalMaxActiveBindings": cmiHaRegIntervalMaxActiveBindings,
       "cmiHaRegInterval3gpp2MaxActiveBindings": cmiHaRegInterval3gpp2MaxActiveBindings,
       "cmiHaRegIntervalWimaxMaxActiveBindings": cmiHaRegIntervalWimaxMaxActiveBindings,
       "cmiHaRegTunnelStatsTable": cmiHaRegTunnelStatsTable,
       "cmiHaRegTunnelStatsEntry": cmiHaRegTunnelStatsEntry,
       "cmiHaRegTunnelStatsSrcAddrType": cmiHaRegTunnelStatsSrcAddrType,
       "cmiHaRegTunnelStatsSrcAddr": cmiHaRegTunnelStatsSrcAddr,
       "cmiHaRegTunnelStatsDestAddrType": cmiHaRegTunnelStatsDestAddrType,
       "cmiHaRegTunnelStatsDestAddr": cmiHaRegTunnelStatsDestAddr,
       "cmiHaRegTunnelStatsTunnelType": cmiHaRegTunnelStatsTunnelType,
       "cmiHaRegTunnelStatsNumUsers": cmiHaRegTunnelStatsNumUsers,
       "cmiHaRegTunnelStatsDataRateInt": cmiHaRegTunnelStatsDataRateInt,
       "cmiHaRegTunnelStatsInBitRate": cmiHaRegTunnelStatsInBitRate,
       "cmiHaRegTunnelStatsInPktRate": cmiHaRegTunnelStatsInPktRate,
       "cmiHaRegTunnelStatsInBytes": cmiHaRegTunnelStatsInBytes,
       "cmiHaRegTunnelStatsInPkts": cmiHaRegTunnelStatsInPkts,
       "cmiHaRegTunnelStatsOutBitRate": cmiHaRegTunnelStatsOutBitRate,
       "cmiHaRegTunnelStatsOutPktRate": cmiHaRegTunnelStatsOutPktRate,
       "cmiHaRegTunnelStatsOutBytes": cmiHaRegTunnelStatsOutBytes,
       "cmiHaRegTunnelStatsOutPkts": cmiHaRegTunnelStatsOutPkts,
       "cmiHaRedun": cmiHaRedun,
       "cmiHaRedunSentBUs": cmiHaRedunSentBUs,
       "cmiHaRedunFailedBUs": cmiHaRedunFailedBUs,
       "cmiHaRedunReceivedBUAcks": cmiHaRedunReceivedBUAcks,
       "cmiHaRedunTotalSentBUs": cmiHaRedunTotalSentBUs,
       "cmiHaRedunReceivedBUs": cmiHaRedunReceivedBUs,
       "cmiHaRedunSentBUAcks": cmiHaRedunSentBUAcks,
       "cmiHaRedunSentBIReqs": cmiHaRedunSentBIReqs,
       "cmiHaRedunFailedBIReqs": cmiHaRedunFailedBIReqs,
       "cmiHaRedunTotalSentBIReqs": cmiHaRedunTotalSentBIReqs,
       "cmiHaRedunReceivedBIReps": cmiHaRedunReceivedBIReps,
       "cmiHaRedunDroppedBIReps": cmiHaRedunDroppedBIReps,
       "cmiHaRedunSentBIAcks": cmiHaRedunSentBIAcks,
       "cmiHaRedunReceivedBIReqs": cmiHaRedunReceivedBIReqs,
       "cmiHaRedunSentBIReps": cmiHaRedunSentBIReps,
       "cmiHaRedunFailedBIReps": cmiHaRedunFailedBIReps,
       "cmiHaRedunTotalSentBIReps": cmiHaRedunTotalSentBIReps,
       "cmiHaRedunReceivedBIAcks": cmiHaRedunReceivedBIAcks,
       "cmiHaRedunDroppedBIAcks": cmiHaRedunDroppedBIAcks,
       "cmiHaRedunSecViolations": cmiHaRedunSecViolations,
       "cmiHaMobNet": cmiHaMobNet,
       "cmiHaMrTable": cmiHaMrTable,
       "cmiHaMrEntry": cmiHaMrEntry,
       "cmiHaMrAddrType": cmiHaMrAddrType,
       "cmiHaMrAddr": cmiHaMrAddr,
       "cmiHaMrDynamic": cmiHaMrDynamic,
       "cmiHaMrStatus": cmiHaMrStatus,
       "cmiHaMrMultiPath": cmiHaMrMultiPath,
       "cmiHaMrMultiPathMetricType": cmiHaMrMultiPathMetricType,
       "cmiHaMobNetTable": cmiHaMobNetTable,
       "cmiHaMobNetEntry": cmiHaMobNetEntry,
       "cmiHaMobNetAddressType": cmiHaMobNetAddressType,
       "cmiHaMobNetAddress": cmiHaMobNetAddress,
       "cmiHaMobNetPfxLen": cmiHaMobNetPfxLen,
       "cmiHaMobNetDynamic": cmiHaMobNetDynamic,
       "cmiHaMobNetStatus": cmiHaMobNetStatus,
       "cmiHaSystem": cmiHaSystem,
       "cmiHaSystemVersion": cmiHaSystemVersion,
       "cmiSecurity": cmiSecurity,
       "cmiSecAssocsCount": cmiSecAssocsCount,
       "cmiSecAssocTable": cmiSecAssocTable,
       "cmiSecAssocEntry": cmiSecAssocEntry,
       "cmiSecPeerIdentifierType": cmiSecPeerIdentifierType,
       "cmiSecPeerIdentifier": cmiSecPeerIdentifier,
       "cmiSecSPI": cmiSecSPI,
       "cmiSecAlgorithmType": cmiSecAlgorithmType,
       "cmiSecAlgorithmMode": cmiSecAlgorithmMode,
       "cmiSecKey": cmiSecKey,
       "cmiSecReplayMethod": cmiSecReplayMethod,
       "cmiSecStatus": cmiSecStatus,
       "cmiSecKey2": cmiSecKey2,
       "cmiSecViolationTable": cmiSecViolationTable,
       "cmiSecViolationEntry": cmiSecViolationEntry,
       "cmiSecViolatorIdentifierType": cmiSecViolatorIdentifierType,
       "cmiSecViolatorIdentifier": cmiSecViolatorIdentifier,
       "cmiSecTotalViolations": cmiSecTotalViolations,
       "cmiSecRecentViolationSPI": cmiSecRecentViolationSPI,
       "cmiSecRecentViolationTime": cmiSecRecentViolationTime,
       "cmiSecRecentViolationIDLow": cmiSecRecentViolationIDLow,
       "cmiSecRecentViolationIDHigh": cmiSecRecentViolationIDHigh,
       "cmiSecRecentViolationReason": cmiSecRecentViolationReason,
       "cmiMa": cmiMa,
       "cmiMaReg": cmiMaReg,
       "cmiMaRegMaxInMinuteRegs": cmiMaRegMaxInMinuteRegs,
       "cmiMaRegDateMaxRegsReceived": cmiMaRegDateMaxRegsReceived,
       "cmiMaRegInLastMinuteRegs": cmiMaRegInLastMinuteRegs,
       "cmiMaAdvertisement": cmiMaAdvertisement,
       "cmiMaAdvConfigTable": cmiMaAdvConfigTable,
       "cmiMaAdvConfigEntry": cmiMaAdvConfigEntry,
       "cmiMaAdvInterfaceIndex": cmiMaAdvInterfaceIndex,
       "cmiMaInterfaceAddressType": cmiMaInterfaceAddressType,
       "cmiMaInterfaceAddress": cmiMaInterfaceAddress,
       "cmiMaAdvMaxRegLifetime": cmiMaAdvMaxRegLifetime,
       "cmiMaAdvPrefixLengthInclusion": cmiMaAdvPrefixLengthInclusion,
       "cmiMaAdvAddressType": cmiMaAdvAddressType,
       "cmiMaAdvAddress": cmiMaAdvAddress,
       "cmiMaAdvMaxInterval": cmiMaAdvMaxInterval,
       "cmiMaAdvMinInterval": cmiMaAdvMinInterval,
       "cmiMaAdvMaxAdvLifetime": cmiMaAdvMaxAdvLifetime,
       "cmiMaAdvResponseSolicitationOnly": cmiMaAdvResponseSolicitationOnly,
       "cmiMaAdvStatus": cmiMaAdvStatus,
       "cmiMn": cmiMn,
       "cmiMnDiscovery": cmiMnDiscovery,
       "cmiMnRecentAdvReceived": cmiMnRecentAdvReceived,
       "cmiMnAdvFlags": cmiMnAdvFlags,
       "cmiMnRegistration": cmiMnRegistration,
       "cmiMnRegistrationTable": cmiMnRegistrationTable,
       "cmiMnRegistrationEntry": cmiMnRegistrationEntry,
       "cmiMnRegFlags": cmiMnRegFlags,
       "cmiMrSystem": cmiMrSystem,
       "cmiMrReverseTunnel": cmiMrReverseTunnel,
       "cmiMrRedundancyGroup": cmiMrRedundancyGroup,
       "cmiMrMobNetTable": cmiMrMobNetTable,
       "cmiMrMobNetEntry": cmiMrMobNetEntry,
       "cmiMrMobNetIfIndex": cmiMrMobNetIfIndex,
       "cmiMrMobNetAddrType": cmiMrMobNetAddrType,
       "cmiMrMobNetAddr": cmiMrMobNetAddr,
       "cmiMrMobNetPfxLen": cmiMrMobNetPfxLen,
       "cmiMrMobNetStatus": cmiMrMobNetStatus,
       "cmiMrHaTunnelIfIndex": cmiMrHaTunnelIfIndex,
       "cmiMrHATable": cmiMrHATable,
       "cmiMrHAEntry": cmiMrHAEntry,
       "cmiMrHAPriority": cmiMrHAPriority,
       "cmiMrHABest": cmiMrHABest,
       "cmiMrIfTable": cmiMrIfTable,
       "cmiMrIfEntry": cmiMrIfEntry,
       "cmiMrIfIndex": cmiMrIfIndex,
       "cmiMRIfDescription": cmiMRIfDescription,
       "cmiMrIfHoldDown": cmiMrIfHoldDown,
       "cmiMrIfRoamPriority": cmiMrIfRoamPriority,
       "cmiMrIfSolicitPeriodic": cmiMrIfSolicitPeriodic,
       "cmiMrIfSolicitInterval": cmiMrIfSolicitInterval,
       "cmiMrIfSolicitRetransInitial": cmiMrIfSolicitRetransInitial,
       "cmiMrIfSolicitRetransMax": cmiMrIfSolicitRetransMax,
       "cmiMrIfSolicitRetransLimit": cmiMrIfSolicitRetransLimit,
       "cmiMrIfSolicitRetransCurrent": cmiMrIfSolicitRetransCurrent,
       "cmiMrIfSolicitRetransRemaining": cmiMrIfSolicitRetransRemaining,
       "cmiMrIfSolicitRetransCount": cmiMrIfSolicitRetransCount,
       "cmiMrIfCCoaAddressType": cmiMrIfCCoaAddressType,
       "cmiMrIfCCoaAddress": cmiMrIfCCoaAddress,
       "cmiMrIfCCoaDefaultGwType": cmiMrIfCCoaDefaultGwType,
       "cmiMrIfCCoaDefaultGw": cmiMrIfCCoaDefaultGw,
       "cmiMrIfCCoaRegRetry": cmiMrIfCCoaRegRetry,
       "cmiMrIfCCoaRegRetryRemaining": cmiMrIfCCoaRegRetryRemaining,
       "cmiMrIfStatus": cmiMrIfStatus,
       "cmiMrIfCCoaRegistration": cmiMrIfCCoaRegistration,
       "cmiMrIfCCoaOnly": cmiMrIfCCoaOnly,
       "cmiMrIfCCoaEnable": cmiMrIfCCoaEnable,
       "cmiMrIfRoamStatus": cmiMrIfRoamStatus,
       "cmiMrIfRegisteredCoAType": cmiMrIfRegisteredCoAType,
       "cmiMrIfRegisteredCoA": cmiMrIfRegisteredCoA,
       "cmiMrIfRegisteredMaAddrType": cmiMrIfRegisteredMaAddrType,
       "cmiMrIfRegisteredMaAddr": cmiMrIfRegisteredMaAddr,
       "cmiMrIfHaTunnelIfIndex": cmiMrIfHaTunnelIfIndex,
       "cmiMrIfID": cmiMrIfID,
       "cmiMrBetterIfDetected": cmiMrBetterIfDetected,
       "cmiMrTunnelPktsRcvd": cmiMrTunnelPktsRcvd,
       "cmiMrTunnelPktsSent": cmiMrTunnelPktsSent,
       "cmiMrTunnelBytesRcvd": cmiMrTunnelBytesRcvd,
       "cmiMrTunnelBytesSent": cmiMrTunnelBytesSent,
       "cmiMrRedStateActive": cmiMrRedStateActive,
       "cmiMrRedStatePassive": cmiMrRedStatePassive,
       "cmiMrCollocatedTunnel": cmiMrCollocatedTunnel,
       "cmiMrMultiPath": cmiMrMultiPath,
       "cmiMrMultiPathMetricType": cmiMrMultiPathMetricType,
       "cmiMrDiscovery": cmiMrDiscovery,
       "cmiMrMaAdvTable": cmiMrMaAdvTable,
       "cmiMrMaAdvEntry": cmiMrMaAdvEntry,
       "cmiMrMaAddressType": cmiMrMaAddressType,
       "cmiMrMaAddress": cmiMrMaAddress,
       "cmiMrMaIsHa": cmiMrMaIsHa,
       "cmiMrMaAdvRcvIf": cmiMrMaAdvRcvIf,
       "cmiMrMaIfMacAddress": cmiMrMaIfMacAddress,
       "cmiMrMaAdvSequence": cmiMrMaAdvSequence,
       "cmiMrMaAdvFlags": cmiMrMaAdvFlags,
       "cmiMrMaAdvMaxRegLifetime": cmiMrMaAdvMaxRegLifetime,
       "cmiMrMaAdvMaxLifetime": cmiMrMaAdvMaxLifetime,
       "cmiMrMaAdvLifetimeRemaining": cmiMrMaAdvLifetimeRemaining,
       "cmiMrMaAdvTimeReceived": cmiMrMaAdvTimeReceived,
       "cmiMrMaAdvTimeFirstHeard": cmiMrMaAdvTimeFirstHeard,
       "cmiMrMaHoldDownRemaining": cmiMrMaHoldDownRemaining,
       "cmiMrRegistration": cmiMrRegistration,
       "cmiMrRegExtendExpire": cmiMrRegExtendExpire,
       "cmiMrRegExtendRetry": cmiMrRegExtendRetry,
       "cmiMrRegExtendInterval": cmiMrRegExtendInterval,
       "cmiMrRegLifetime": cmiMrRegLifetime,
       "cmiMrRegRetransInitial": cmiMrRegRetransInitial,
       "cmiMrRegRetransMax": cmiMrRegRetransMax,
       "cmiMrRegRetransLimit": cmiMrRegRetransLimit,
       "cmiMrRegNewHa": cmiMrRegNewHa,
       "cmiTrapObjects": cmiTrapObjects,
       "cmiTrapControl": cmiTrapControl,
       "cmiNtRegCOAType": cmiNtRegCOAType,
       "cmiNtRegCOA": cmiNtRegCOA,
       "cmiNtRegHAAddrType": cmiNtRegHAAddrType,
       "cmiNtRegHomeAgent": cmiNtRegHomeAgent,
       "cmiNtRegHomeAddressType": cmiNtRegHomeAddressType,
       "cmiNtRegHomeAddress": cmiNtRegHomeAddress,
       "cmiNtRegNAI": cmiNtRegNAI,
       "cmiNtRegDeniedCode": cmiNtRegDeniedCode,
       "ciscoMobileIpMIBConformance": ciscoMobileIpMIBConformance,
       "ciscoMobileIpCompliances": ciscoMobileIpCompliances,
       "ciscoMobileIpCompliance": ciscoMobileIpCompliance,
       "ciscoMobileIpComplianceV12R02": ciscoMobileIpComplianceV12R02,
       "ciscoMobileIpComplianceV12R03": ciscoMobileIpComplianceV12R03,
       "ciscoMobileIpComplianceV12R03r1": ciscoMobileIpComplianceV12R03r1,
       "ciscoMobileIpComplianceV12R04": ciscoMobileIpComplianceV12R04,
       "ciscoMobileIpComplianceV12R05": ciscoMobileIpComplianceV12R05,
       "ciscoMobileIpComplianceV12R06": ciscoMobileIpComplianceV12R06,
       "ciscoMobileIpComplianceV12R07": ciscoMobileIpComplianceV12R07,
       "ciscoMobileIpComplianceV12R08": ciscoMobileIpComplianceV12R08,
       "ciscoMobileIpComplianceV12R09": ciscoMobileIpComplianceV12R09,
       "ciscoMobileIpComplianceV12R10": ciscoMobileIpComplianceV12R10,
       "ciscoMobileIpComplianceV12R11": ciscoMobileIpComplianceV12R11,
       "ciscoMobileIpComplianceRev1": ciscoMobileIpComplianceRev1,
       "ciscoMobileIpComplianceRev2": ciscoMobileIpComplianceRev2,
       "ciscoMobileIpGroups": ciscoMobileIpGroups,
       "ciscoMobileIpFaRegGroup": ciscoMobileIpFaRegGroup,
       "ciscoMobileIpHaRegGroup": ciscoMobileIpHaRegGroup,
       "ciscoMobileIpFaRegGroupV12R02": ciscoMobileIpFaRegGroupV12R02,
       "ciscoMobileIpHaRegGroupV12R02": ciscoMobileIpHaRegGroupV12R02,
       "ciscoMobileIpHaRedunGroup": ciscoMobileIpHaRedunGroup,
       "ciscoMobileIpSecAssocGroup": ciscoMobileIpSecAssocGroup,
       "ciscoMobileIpSecViolationGroup": ciscoMobileIpSecViolationGroup,
       "ciscoMobileIpMaRegGroup": ciscoMobileIpMaRegGroup,
       "ciscoMobileIpFaRegGroupV12R03": ciscoMobileIpFaRegGroupV12R03,
       "ciscoMobileIpHaRegGroupV12R03": ciscoMobileIpHaRegGroupV12R03,
       "ciscoMobileIpFaRegGroupV12R03r1": ciscoMobileIpFaRegGroupV12R03r1,
       "ciscoMobileIpHaRegGroupV12R03r1": ciscoMobileIpHaRegGroupV12R03r1,
       "ciscoMobileIpFaAdvertisementGroup": ciscoMobileIpFaAdvertisementGroup,
       "ciscoMobileIpFaSystemGroup": ciscoMobileIpFaSystemGroup,
       "ciscoMobileIpMnDiscoveryGroup": ciscoMobileIpMnDiscoveryGroup,
       "ciscoMobileIpMnRegistrationGroup": ciscoMobileIpMnRegistrationGroup,
       "ciscoMobileIpHaMobNetGroup": ciscoMobileIpHaMobNetGroup,
       "ciscoMobileIpMrSystemGroup": ciscoMobileIpMrSystemGroup,
       "ciscoMobileIpMrDiscoveryGroup": ciscoMobileIpMrDiscoveryGroup,
       "ciscoMobileIpMrRegistrationGroup": ciscoMobileIpMrRegistrationGroup,
       "ciscoMobileIpTrapObjectsGroup": ciscoMobileIpTrapObjectsGroup,
       "ciscoMobileIpMrNotificationGroup": ciscoMobileIpMrNotificationGroup,
       "ciscoMobileIpSecAssocGroupV12R02": ciscoMobileIpSecAssocGroupV12R02,
       "cmiMaAdvertisementGroup": cmiMaAdvertisementGroup,
       "ciscoMobileIpMrSystemGroupV1": ciscoMobileIpMrSystemGroupV1,
       "ciscoMobileIpMrSystemGroupV2": ciscoMobileIpMrSystemGroupV2,
       "ciscoMobileIpFaRegGroupV12R03r2": ciscoMobileIpFaRegGroupV12R03r2,
       "ciscoMobileIpHaRegGroupV12R03r2": ciscoMobileIpHaRegGroupV12R03r2,
       "ciscoMobileIpTrapObjectsGroupV2": ciscoMobileIpTrapObjectsGroupV2,
       "ciscoMobileIpMrNotificationGroupV2": ciscoMobileIpMrNotificationGroupV2,
       "ciscoMobileIpMrSystemGroupV3": ciscoMobileIpMrSystemGroupV3,
       "ciscoMobileIpHaRegGroupV12R03r2Sup1": ciscoMobileIpHaRegGroupV12R03r2Sup1,
       "ciscoMobileIpHaMobNetGroupSup1": ciscoMobileIpHaMobNetGroupSup1,
       "ciscoMobileIpMrSystemGroupV3Sup1": ciscoMobileIpMrSystemGroupV3Sup1,
       "ciscoMobileIpHaRegGroupV12R03r2Sup2": ciscoMobileIpHaRegGroupV12R03r2Sup2,
       "ciscoMobileIpHaSystemGroupV1": ciscoMobileIpHaSystemGroupV1,
       "ciscoMobileIpMrNotificationGroupV3": ciscoMobileIpMrNotificationGroupV3,
       "ciscoMobileIpHaRegGroupV1": ciscoMobileIpHaRegGroupV1,
       "ciscoMobileIpHaRegIntervalStatsGroup": ciscoMobileIpHaRegIntervalStatsGroup,
       "ciscoMobileIpHaRegTunnelStatsGroup": ciscoMobileIpHaRegTunnelStatsGroup}
)
