# SNMP MIB module (TPT-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:58 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_policy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1)
)
tpt_policy.setRevisions(
        ("2016-05-25 18:54",
         "2015-06-19 18:30",
         "2015-05-28 13:30",
         "2014-12-15 11:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyProtocol(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("arp", 5),
          ("icmp", 1),
          ("icmpv6", 7),
          ("other-eth", 6),
          ("other-ip", 4),
          ("other-ipv6", 8),
          ("tcp", 3),
          ("udp", 2))
    )



class PolicyFrameSize(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("fs1024toMaxB", 6),
          ("fs128to255B", 3),
          ("fs256to511B", 4),
          ("fs4096to9216B", 8),
          ("fs512to1023B", 5),
          ("fs64B", 1),
          ("fs65to127B", 2),
          ("fs9217to16383", 11),
          ("fsMaxto4095B", 7),
          ("fsOver", 10),
          ("fsUnder", 9))
    )



class PolicyFrameType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alignError", 6),
          ("broadcast", 2),
          ("fcsError", 5),
          ("macControl", 4),
          ("multicast", 3),
          ("symbolError", 7),
          ("unicast", 1))
    )



class PolicySeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("warning", 1))
    )



class PolicyAction(Integer32, TextualConvention):
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
        *(("allow", 2),
          ("deny", 1),
          ("ratelimit", 3))
    )



class PolicyComponent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("alert", 7),
          ("allow", 2),
          ("block", 8),
          ("deny", 1),
          ("invalid", 0),
          ("peer", 9))
    )



class SslInspectedFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )



class SslProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("sslv3", 2),
          ("tls10", 3),
          ("tls11", 4),
          ("tls12", 5),
          ("unknown", 1))
    )



class SslInspEventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class SslInspAction(Integer32, TextualConvention):
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
        *(("blocked", 3),
          ("decrypted", 1),
          ("notDecrypted", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PolicyPacketsDropped_Type = Counter32
_PolicyPacketsDropped_Object = MibScalar
policyPacketsDropped = _PolicyPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 1),
    _PolicyPacketsDropped_Type()
)
policyPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsDropped.setStatus("current")
_PolicyPacketsBlocked_Type = Counter32
_PolicyPacketsBlocked_Object = MibScalar
policyPacketsBlocked = _PolicyPacketsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 2),
    _PolicyPacketsBlocked_Type()
)
policyPacketsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsBlocked.setStatus("current")
_PolicyPacketsIncoming_Type = Counter32
_PolicyPacketsIncoming_Object = MibScalar
policyPacketsIncoming = _PolicyPacketsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 3),
    _PolicyPacketsIncoming_Type()
)
policyPacketsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsIncoming.setStatus("current")
_PolicyPacketsOutgoing_Type = Counter32
_PolicyPacketsOutgoing_Object = MibScalar
policyPacketsOutgoing = _PolicyPacketsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 4),
    _PolicyPacketsOutgoing_Type()
)
policyPacketsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsOutgoing.setStatus("current")
_PolicyCounterTable_Object = MibTable
policyCounterTable = _PolicyCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    policyCounterTable.setStatus("obsolete")
_PolicyCounterEntry_Object = MibTableRow
policyCounterEntry = _PolicyCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5, 1)
)
policyCounterEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "policyGlobalID"),
)
if mibBuilder.loadTexts:
    policyCounterEntry.setStatus("obsolete")


class _PolicyGlobalID_Type(OctetString):
    """Custom type policyGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PolicyGlobalID_Type.__name__ = "OctetString"
_PolicyGlobalID_Object = MibTableColumn
policyGlobalID = _PolicyGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5, 1, 1),
    _PolicyGlobalID_Type()
)
policyGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyGlobalID.setStatus("obsolete")


class _PolicyDescriptiveName_Type(OctetString):
    """Custom type policyDescriptiveName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PolicyDescriptiveName_Type.__name__ = "OctetString"
_PolicyDescriptiveName_Object = MibTableColumn
policyDescriptiveName = _PolicyDescriptiveName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5, 1, 2),
    _PolicyDescriptiveName_Type()
)
policyDescriptiveName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDescriptiveName.setStatus("obsolete")
_PolicyCountBytes_Type = Counter64
_PolicyCountBytes_Object = MibTableColumn
policyCountBytes = _PolicyCountBytes_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5, 1, 3),
    _PolicyCountBytes_Type()
)
policyCountBytes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyCountBytes.setStatus("obsolete")
_PolicyCountPackets_Type = Counter64
_PolicyCountPackets_Object = MibTableColumn
policyCountPackets = _PolicyCountPackets_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5, 1, 4),
    _PolicyCountPackets_Type()
)
policyCountPackets.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyCountPackets.setStatus("obsolete")
_PolicyCreationTime_Type = Unsigned32
_PolicyCreationTime_Object = MibTableColumn
policyCreationTime = _PolicyCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 5, 1, 5),
    _PolicyCreationTime_Type()
)
policyCreationTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyCreationTime.setStatus("obsolete")
_PolicyPacketsInvalid_Type = Counter32
_PolicyPacketsInvalid_Object = MibScalar
policyPacketsInvalid = _PolicyPacketsInvalid_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 6),
    _PolicyPacketsInvalid_Type()
)
policyPacketsInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsInvalid.setStatus("current")
_PolicyPacketsPermitted_Type = Counter32
_PolicyPacketsPermitted_Object = MibScalar
policyPacketsPermitted = _PolicyPacketsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 7),
    _PolicyPacketsPermitted_Type()
)
policyPacketsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsPermitted.setStatus("current")
_PolicyDVObjs_ObjectIdentity = ObjectIdentity
policyDVObjs = _PolicyDVObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10)
)
if mibBuilder.loadTexts:
    policyDVObjs.setStatus("current")


class _PolicyDVVersion_Type(OctetString):
    """Custom type policyDVVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PolicyDVVersion_Type.__name__ = "OctetString"
_PolicyDVVersion_Object = MibScalar
policyDVVersion = _PolicyDVVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 1),
    _PolicyDVVersion_Type()
)
policyDVVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDVVersion.setStatus("current")
_TopTenHitsByPolicyTable_Object = MibTable
topTenHitsByPolicyTable = _TopTenHitsByPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 11)
)
if mibBuilder.loadTexts:
    topTenHitsByPolicyTable.setStatus("current")
_TopTenHitsByPolicyEntry_Object = MibTableRow
topTenHitsByPolicyEntry = _TopTenHitsByPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 11, 1)
)
topTenHitsByPolicyEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "topTenRank"),
)
if mibBuilder.loadTexts:
    topTenHitsByPolicyEntry.setStatus("current")


class _TopTenRank_Type(Unsigned32):
    """Custom type topTenRank based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TopTenRank_Type.__name__ = "Unsigned32"
_TopTenRank_Object = MibTableColumn
topTenRank = _TopTenRank_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 11, 1, 1),
    _TopTenRank_Type()
)
topTenRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topTenRank.setStatus("current")
_PolicyHitCount_Type = Unsigned32
_PolicyHitCount_Object = MibTableColumn
policyHitCount = _PolicyHitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 11, 1, 2),
    _PolicyHitCount_Type()
)
policyHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyHitCount.setStatus("current")


class _PolicyName_Type(OctetString):
    """Custom type policyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PolicyName_Type.__name__ = "OctetString"
_PolicyName_Object = MibTableColumn
policyName = _PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 11, 1, 3),
    _PolicyName_Type()
)
policyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyName.setStatus("current")


class _PolicyUUID_Type(OctetString):
    """Custom type policyUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PolicyUUID_Type.__name__ = "OctetString"
_PolicyUUID_Object = MibTableColumn
policyUUID = _PolicyUUID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 11, 1, 4),
    _PolicyUUID_Type()
)
policyUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyUUID.setStatus("current")
_AlertsBySeverityTable_Object = MibTable
alertsBySeverityTable = _AlertsBySeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 12)
)
if mibBuilder.loadTexts:
    alertsBySeverityTable.setStatus("current")
_AlertsBySeverityEntry_Object = MibTableRow
alertsBySeverityEntry = _AlertsBySeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 12, 1)
)
alertsBySeverityEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "alertSeverity"),
)
if mibBuilder.loadTexts:
    alertsBySeverityEntry.setStatus("current")
_AlertSeverity_Type = PolicySeverity
_AlertSeverity_Object = MibTableColumn
alertSeverity = _AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 12, 1, 1),
    _AlertSeverity_Type()
)
alertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSeverity.setStatus("current")
_SeverityAlertCount_Type = Unsigned32
_SeverityAlertCount_Object = MibTableColumn
severityAlertCount = _SeverityAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 12, 1, 2),
    _SeverityAlertCount_Type()
)
severityAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityAlertCount.setStatus("current")
_AlertsByProtocolTable_Object = MibTable
alertsByProtocolTable = _AlertsByProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 13)
)
if mibBuilder.loadTexts:
    alertsByProtocolTable.setStatus("current")
_AlertsByProtocolEntry_Object = MibTableRow
alertsByProtocolEntry = _AlertsByProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 13, 1)
)
alertsByProtocolEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "alertProtocol"),
)
if mibBuilder.loadTexts:
    alertsByProtocolEntry.setStatus("current")
_AlertProtocol_Type = PolicyProtocol
_AlertProtocol_Object = MibTableColumn
alertProtocol = _AlertProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 13, 1, 1),
    _AlertProtocol_Type()
)
alertProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertProtocol.setStatus("current")
_ProtocolAlertCount_Type = Unsigned32
_ProtocolAlertCount_Object = MibTableColumn
protocolAlertCount = _ProtocolAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 13, 1, 2),
    _ProtocolAlertCount_Type()
)
protocolAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolAlertCount.setStatus("current")
_AlertsByZoneTable_Object = MibTable
alertsByZoneTable = _AlertsByZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 14)
)
if mibBuilder.loadTexts:
    alertsByZoneTable.setStatus("obsolete")
_AlertsByZoneEntry_Object = MibTableRow
alertsByZoneEntry = _AlertsByZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 14, 1)
)
alertsByZoneEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "alertSlot"),
    (0, "TPT-POLICY-MIB", "alertPort"),
)
if mibBuilder.loadTexts:
    alertsByZoneEntry.setStatus("obsolete")
_AlertSlot_Type = Unsigned32
_AlertSlot_Object = MibTableColumn
alertSlot = _AlertSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 14, 1, 1),
    _AlertSlot_Type()
)
alertSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alertSlot.setStatus("obsolete")
_AlertPort_Type = Unsigned32
_AlertPort_Object = MibTableColumn
alertPort = _AlertPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 14, 1, 2),
    _AlertPort_Type()
)
alertPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alertPort.setStatus("obsolete")
_ZoneAlertCount_Type = Unsigned32
_ZoneAlertCount_Object = MibTableColumn
zoneAlertCount = _ZoneAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 14, 1, 3),
    _ZoneAlertCount_Type()
)
zoneAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneAlertCount.setStatus("obsolete")
_PermitsByZoneTable_Object = MibTable
permitsByZoneTable = _PermitsByZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 15)
)
if mibBuilder.loadTexts:
    permitsByZoneTable.setStatus("obsolete")
_PermitsByZoneEntry_Object = MibTableRow
permitsByZoneEntry = _PermitsByZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 15, 1)
)
permitsByZoneEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "permitSlot"),
    (0, "TPT-POLICY-MIB", "permitPort"),
)
if mibBuilder.loadTexts:
    permitsByZoneEntry.setStatus("obsolete")
_PermitSlot_Type = Unsigned32
_PermitSlot_Object = MibTableColumn
permitSlot = _PermitSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 15, 1, 1),
    _PermitSlot_Type()
)
permitSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    permitSlot.setStatus("obsolete")
_PermitPort_Type = Unsigned32
_PermitPort_Object = MibTableColumn
permitPort = _PermitPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 15, 1, 2),
    _PermitPort_Type()
)
permitPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    permitPort.setStatus("obsolete")
_ZonePermitCount_Type = Unsigned32
_ZonePermitCount_Object = MibTableColumn
zonePermitCount = _ZonePermitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 15, 1, 3),
    _ZonePermitCount_Type()
)
zonePermitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonePermitCount.setStatus("obsolete")
_BlocksByZoneTable_Object = MibTable
blocksByZoneTable = _BlocksByZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 16)
)
if mibBuilder.loadTexts:
    blocksByZoneTable.setStatus("obsolete")
_BlocksByZoneEntry_Object = MibTableRow
blocksByZoneEntry = _BlocksByZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 16, 1)
)
blocksByZoneEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "blockSlot"),
    (0, "TPT-POLICY-MIB", "blockPort"),
)
if mibBuilder.loadTexts:
    blocksByZoneEntry.setStatus("obsolete")
_BlockSlot_Type = Unsigned32
_BlockSlot_Object = MibTableColumn
blockSlot = _BlockSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 16, 1, 1),
    _BlockSlot_Type()
)
blockSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockSlot.setStatus("obsolete")
_BlockPort_Type = Unsigned32
_BlockPort_Object = MibTableColumn
blockPort = _BlockPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 16, 1, 2),
    _BlockPort_Type()
)
blockPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockPort.setStatus("obsolete")
_ZoneBlockCount_Type = Unsigned32
_ZoneBlockCount_Object = MibTableColumn
zoneBlockCount = _ZoneBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 16, 1, 3),
    _ZoneBlockCount_Type()
)
zoneBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBlockCount.setStatus("obsolete")
_P2psByZoneTable_Object = MibTable
p2psByZoneTable = _P2psByZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 17)
)
if mibBuilder.loadTexts:
    p2psByZoneTable.setStatus("obsolete")
_P2psByZoneEntry_Object = MibTableRow
p2psByZoneEntry = _P2psByZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 17, 1)
)
p2psByZoneEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "p2pSlot"),
    (0, "TPT-POLICY-MIB", "p2pPort"),
)
if mibBuilder.loadTexts:
    p2psByZoneEntry.setStatus("obsolete")
_P2pSlot_Type = Unsigned32
_P2pSlot_Object = MibTableColumn
p2pSlot = _P2pSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 17, 1, 1),
    _P2pSlot_Type()
)
p2pSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2pSlot.setStatus("obsolete")
_P2pPort_Type = Unsigned32
_P2pPort_Object = MibTableColumn
p2pPort = _P2pPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 17, 1, 2),
    _P2pPort_Type()
)
p2pPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2pPort.setStatus("obsolete")
_ZoneP2pCount_Type = Unsigned32
_ZoneP2pCount_Object = MibTableColumn
zoneP2pCount = _ZoneP2pCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 17, 1, 3),
    _ZoneP2pCount_Type()
)
zoneP2pCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneP2pCount.setStatus("obsolete")
_FramesBySizeTable_Object = MibTable
framesBySizeTable = _FramesBySizeTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 18)
)
if mibBuilder.loadTexts:
    framesBySizeTable.setStatus("current")
_FramesBySizeEntry_Object = MibTableRow
framesBySizeEntry = _FramesBySizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 18, 1)
)
framesBySizeEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "frameSize"),
)
if mibBuilder.loadTexts:
    framesBySizeEntry.setStatus("current")
_FrameSize_Type = PolicyFrameSize
_FrameSize_Object = MibTableColumn
frameSize = _FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 18, 1, 1),
    _FrameSize_Type()
)
frameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameSize.setStatus("current")
_SizeFrameCount_Type = Unsigned32
_SizeFrameCount_Object = MibTableColumn
sizeFrameCount = _SizeFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 18, 1, 2),
    _SizeFrameCount_Type()
)
sizeFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeFrameCount.setStatus("current")
_FramesByTypeTable_Object = MibTable
framesByTypeTable = _FramesByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 19)
)
if mibBuilder.loadTexts:
    framesByTypeTable.setStatus("current")
_FramesByTypeEntry_Object = MibTableRow
framesByTypeEntry = _FramesByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 19, 1)
)
framesByTypeEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "frameType"),
)
if mibBuilder.loadTexts:
    framesByTypeEntry.setStatus("current")
_FrameType_Type = PolicyFrameType
_FrameType_Object = MibTableColumn
frameType = _FrameType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 19, 1, 1),
    _FrameType_Type()
)
frameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameType.setStatus("current")
_TypeFrameCount_Type = Unsigned32
_TypeFrameCount_Object = MibTableColumn
typeFrameCount = _TypeFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 19, 1, 2),
    _TypeFrameCount_Type()
)
typeFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    typeFrameCount.setStatus("current")
_PacketsByProtocolTable_Object = MibTable
packetsByProtocolTable = _PacketsByProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 20)
)
if mibBuilder.loadTexts:
    packetsByProtocolTable.setStatus("current")
_PacketsByProtocolEntry_Object = MibTableRow
packetsByProtocolEntry = _PacketsByProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 20, 1)
)
packetsByProtocolEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "packetProtocol"),
)
if mibBuilder.loadTexts:
    packetsByProtocolEntry.setStatus("current")
_PacketProtocol_Type = PolicyProtocol
_PacketProtocol_Object = MibTableColumn
packetProtocol = _PacketProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 20, 1, 1),
    _PacketProtocol_Type()
)
packetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetProtocol.setStatus("current")
_ProtocolPacketCount_Type = Unsigned32
_ProtocolPacketCount_Object = MibTableColumn
protocolPacketCount = _ProtocolPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 20, 1, 2),
    _ProtocolPacketCount_Type()
)
protocolPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolPacketCount.setStatus("current")
_PolicyByNumberTable_Object = MibTable
policyByNumberTable = _PolicyByNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 21)
)
if mibBuilder.loadTexts:
    policyByNumberTable.setStatus("current")
_PolicyByNumberEntry_Object = MibTableRow
policyByNumberEntry = _PolicyByNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 21, 1)
)
policyByNumberEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "policyNumber"),
)
if mibBuilder.loadTexts:
    policyByNumberEntry.setStatus("current")
_PolicyNumber_Type = Unsigned32
_PolicyNumber_Object = MibTableColumn
policyNumber = _PolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 21, 1, 1),
    _PolicyNumber_Type()
)
policyNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyNumber.setStatus("current")


class _NumberName_Type(OctetString):
    """Custom type numberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_NumberName_Type.__name__ = "OctetString"
_NumberName_Object = MibTableColumn
numberName = _NumberName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 21, 1, 2),
    _NumberName_Type()
)
numberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberName.setStatus("current")


class _NumberDesc_Type(OctetString):
    """Custom type numberDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3000),
    )


_NumberDesc_Type.__name__ = "OctetString"
_NumberDesc_Object = MibTableColumn
numberDesc = _NumberDesc_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 21, 1, 3),
    _NumberDesc_Type()
)
numberDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDesc.setStatus("current")
_SecurityZonePairTable_Object = MibTable
securityZonePairTable = _SecurityZonePairTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22)
)
if mibBuilder.loadTexts:
    securityZonePairTable.setStatus("current")
_SecurityZonePairEntry_Object = MibTableRow
securityZonePairEntry = _SecurityZonePairEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1)
)
securityZonePairEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "szpUUID"),
)
if mibBuilder.loadTexts:
    securityZonePairEntry.setStatus("current")


class _SzpName_Type(OctetString):
    """Custom type szpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SzpName_Type.__name__ = "OctetString"
_SzpName_Object = MibTableColumn
szpName = _SzpName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 1),
    _SzpName_Type()
)
szpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpName.setStatus("current")


class _SzpInZoneName_Type(OctetString):
    """Custom type szpInZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SzpInZoneName_Type.__name__ = "OctetString"
_SzpInZoneName_Object = MibTableColumn
szpInZoneName = _SzpInZoneName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 2),
    _SzpInZoneName_Type()
)
szpInZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpInZoneName.setStatus("current")


class _SzpOutZoneName_Type(OctetString):
    """Custom type szpOutZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SzpOutZoneName_Type.__name__ = "OctetString"
_SzpOutZoneName_Object = MibTableColumn
szpOutZoneName = _SzpOutZoneName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 3),
    _SzpOutZoneName_Type()
)
szpOutZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpOutZoneName.setStatus("current")


class _SzpUUID_Type(OctetString):
    """Custom type szpUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SzpUUID_Type.__name__ = "OctetString"
_SzpUUID_Object = MibTableColumn
szpUUID = _SzpUUID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 4),
    _SzpUUID_Type()
)
szpUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpUUID.setStatus("current")


class _SzpInZoneUUID_Type(OctetString):
    """Custom type szpInZoneUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SzpInZoneUUID_Type.__name__ = "OctetString"
_SzpInZoneUUID_Object = MibTableColumn
szpInZoneUUID = _SzpInZoneUUID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 5),
    _SzpInZoneUUID_Type()
)
szpInZoneUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpInZoneUUID.setStatus("current")


class _SzpOutZoneUUID_Type(OctetString):
    """Custom type szpOutZoneUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SzpOutZoneUUID_Type.__name__ = "OctetString"
_SzpOutZoneUUID_Object = MibTableColumn
szpOutZoneUUID = _SzpOutZoneUUID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 6),
    _SzpOutZoneUUID_Type()
)
szpOutZoneUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpOutZoneUUID.setStatus("current")
_SzpInPackets_Type = Counter64
_SzpInPackets_Object = MibTableColumn
szpInPackets = _SzpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 7),
    _SzpInPackets_Type()
)
szpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpInPackets.setStatus("current")
_SzpInOctets_Type = Counter64
_SzpInOctets_Object = MibTableColumn
szpInOctets = _SzpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 8),
    _SzpInOctets_Type()
)
szpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpInOctets.setStatus("current")
_SzpAlerts_Type = Counter64
_SzpAlerts_Object = MibTableColumn
szpAlerts = _SzpAlerts_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 9),
    _SzpAlerts_Type()
)
szpAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpAlerts.setStatus("current")
_SzpBlocks_Type = Counter64
_SzpBlocks_Object = MibTableColumn
szpBlocks = _SzpBlocks_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 10),
    _SzpBlocks_Type()
)
szpBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpBlocks.setStatus("current")
_SzpPermits_Type = Counter64
_SzpPermits_Object = MibTableColumn
szpPermits = _SzpPermits_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 11),
    _SzpPermits_Type()
)
szpPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpPermits.setStatus("current")
_SzpPrecedence_Type = Unsigned32
_SzpPrecedence_Object = MibTableColumn
szpPrecedence = _SzpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 22, 1, 12),
    _SzpPrecedence_Type()
)
szpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    szpPrecedence.setStatus("current")
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 23)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("current")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 23, 1)
)
portStatsEntry.setIndexNames(
    (0, "TPT-POLICY-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("current")
_PortNumber_Type = Unsigned32
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 23, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _PortName_Type(OctetString):
    """Custom type portName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortName_Type.__name__ = "OctetString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 23, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_PortVlanTranslations_Type = Counter64
_PortVlanTranslations_Object = MibTableColumn
portVlanTranslations = _PortVlanTranslations_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 23, 1, 3),
    _PortVlanTranslations_Type()
)
portVlanTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanTranslations.setStatus("current")
_PolicyPacketsDropped64_Type = Counter64
_PolicyPacketsDropped64_Object = MibScalar
policyPacketsDropped64 = _PolicyPacketsDropped64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 31),
    _PolicyPacketsDropped64_Type()
)
policyPacketsDropped64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsDropped64.setStatus("current")
_PolicyPacketsBlocked64_Type = Counter64
_PolicyPacketsBlocked64_Object = MibScalar
policyPacketsBlocked64 = _PolicyPacketsBlocked64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 32),
    _PolicyPacketsBlocked64_Type()
)
policyPacketsBlocked64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsBlocked64.setStatus("current")
_PolicyPacketsIncoming64_Type = Counter64
_PolicyPacketsIncoming64_Object = MibScalar
policyPacketsIncoming64 = _PolicyPacketsIncoming64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 33),
    _PolicyPacketsIncoming64_Type()
)
policyPacketsIncoming64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsIncoming64.setStatus("current")
_PolicyPacketsOutgoing64_Type = Counter64
_PolicyPacketsOutgoing64_Object = MibScalar
policyPacketsOutgoing64 = _PolicyPacketsOutgoing64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 34),
    _PolicyPacketsOutgoing64_Type()
)
policyPacketsOutgoing64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsOutgoing64.setStatus("current")
_PolicyPacketsInvalid64_Type = Counter64
_PolicyPacketsInvalid64_Object = MibScalar
policyPacketsInvalid64 = _PolicyPacketsInvalid64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 36),
    _PolicyPacketsInvalid64_Type()
)
policyPacketsInvalid64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsInvalid64.setStatus("current")
_PolicyPacketsPermitted64_Type = Counter64
_PolicyPacketsPermitted64_Object = MibScalar
policyPacketsPermitted64 = _PolicyPacketsPermitted64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 37),
    _PolicyPacketsPermitted64_Type()
)
policyPacketsPermitted64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsPermitted64.setStatus("current")
_PolicyPacketsRateLimited64_Type = Counter64
_PolicyPacketsRateLimited64_Object = MibScalar
policyPacketsRateLimited64 = _PolicyPacketsRateLimited64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 38),
    _PolicyPacketsRateLimited64_Type()
)
policyPacketsRateLimited64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsRateLimited64.setStatus("current")
_PolicyPacketsTrusted64_Type = Counter64
_PolicyPacketsTrusted64_Object = MibScalar
policyPacketsTrusted64 = _PolicyPacketsTrusted64_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 39),
    _PolicyPacketsTrusted64_Type()
)
policyPacketsTrusted64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPacketsTrusted64.setStatus("current")


class _TptPolicyNotifyDeviceID_Type(OctetString):
    """Custom type tptPolicyNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifyDeviceID_Type.__name__ = "OctetString"
_TptPolicyNotifyDeviceID_Object = MibScalar
tptPolicyNotifyDeviceID = _TptPolicyNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 11),
    _TptPolicyNotifyDeviceID_Type()
)
tptPolicyNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyDeviceID.setStatus("current")


class _TptPolicyNotifyPolicyID_Type(OctetString):
    """Custom type tptPolicyNotifyPolicyID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifyPolicyID_Type.__name__ = "OctetString"
_TptPolicyNotifyPolicyID_Object = MibScalar
tptPolicyNotifyPolicyID = _TptPolicyNotifyPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 12),
    _TptPolicyNotifyPolicyID_Type()
)
tptPolicyNotifyPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyPolicyID.setStatus("current")


class _TptPolicyNotifySignatureID_Type(OctetString):
    """Custom type tptPolicyNotifySignatureID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifySignatureID_Type.__name__ = "OctetString"
_TptPolicyNotifySignatureID_Object = MibScalar
tptPolicyNotifySignatureID = _TptPolicyNotifySignatureID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 13),
    _TptPolicyNotifySignatureID_Type()
)
tptPolicyNotifySignatureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySignatureID.setStatus("current")


class _TptPolicyNotifySegmentName_Type(OctetString):
    """Custom type tptPolicyNotifySegmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptPolicyNotifySegmentName_Type.__name__ = "OctetString"
_TptPolicyNotifySegmentName_Object = MibScalar
tptPolicyNotifySegmentName = _TptPolicyNotifySegmentName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 14),
    _TptPolicyNotifySegmentName_Type()
)
tptPolicyNotifySegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySegmentName.setStatus("obsolete")
_TptPolicyNotifySrcNetAddr_Type = IpAddress
_TptPolicyNotifySrcNetAddr_Object = MibScalar
tptPolicyNotifySrcNetAddr = _TptPolicyNotifySrcNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 15),
    _TptPolicyNotifySrcNetAddr_Type()
)
tptPolicyNotifySrcNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySrcNetAddr.setStatus("current")
_TptPolicyNotifySrcNetPort_Type = Unsigned32
_TptPolicyNotifySrcNetPort_Object = MibScalar
tptPolicyNotifySrcNetPort = _TptPolicyNotifySrcNetPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 16),
    _TptPolicyNotifySrcNetPort_Type()
)
tptPolicyNotifySrcNetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySrcNetPort.setStatus("current")
_TptPolicyNotifyDestNetAddr_Type = IpAddress
_TptPolicyNotifyDestNetAddr_Object = MibScalar
tptPolicyNotifyDestNetAddr = _TptPolicyNotifyDestNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 17),
    _TptPolicyNotifyDestNetAddr_Type()
)
tptPolicyNotifyDestNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyDestNetAddr.setStatus("current")
_TptPolicyNotifyDestNetPort_Type = Unsigned32
_TptPolicyNotifyDestNetPort_Object = MibScalar
tptPolicyNotifyDestNetPort = _TptPolicyNotifyDestNetPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 18),
    _TptPolicyNotifyDestNetPort_Type()
)
tptPolicyNotifyDestNetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyDestNetPort.setStatus("current")
_TptPolicyNotifyStartTimeSec_Type = Unsigned32
_TptPolicyNotifyStartTimeSec_Object = MibScalar
tptPolicyNotifyStartTimeSec = _TptPolicyNotifyStartTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 19),
    _TptPolicyNotifyStartTimeSec_Type()
)
tptPolicyNotifyStartTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyStartTimeSec.setStatus("current")
_TptPolicyNotifyAlertAction_Type = PolicyAction
_TptPolicyNotifyAlertAction_Object = MibScalar
tptPolicyNotifyAlertAction = _TptPolicyNotifyAlertAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 20),
    _TptPolicyNotifyAlertAction_Type()
)
tptPolicyNotifyAlertAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyAlertAction.setStatus("current")
_TptPolicyNotifyConfigAction_Type = PolicyAction
_TptPolicyNotifyConfigAction_Object = MibScalar
tptPolicyNotifyConfigAction = _TptPolicyNotifyConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 21),
    _TptPolicyNotifyConfigAction_Type()
)
tptPolicyNotifyConfigAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyConfigAction.setStatus("current")
_TptPolicyNotifyComponentID_Type = PolicyComponent
_TptPolicyNotifyComponentID_Object = MibScalar
tptPolicyNotifyComponentID = _TptPolicyNotifyComponentID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 22),
    _TptPolicyNotifyComponentID_Type()
)
tptPolicyNotifyComponentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyComponentID.setStatus("current")
_TptPolicyNotifyHitCount_Type = Unsigned32
_TptPolicyNotifyHitCount_Object = MibScalar
tptPolicyNotifyHitCount = _TptPolicyNotifyHitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 23),
    _TptPolicyNotifyHitCount_Type()
)
tptPolicyNotifyHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyHitCount.setStatus("current")
_TptPolicyNotifyAggregationPeriod_Type = Unsigned32
_TptPolicyNotifyAggregationPeriod_Object = MibScalar
tptPolicyNotifyAggregationPeriod = _TptPolicyNotifyAggregationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 24),
    _TptPolicyNotifyAggregationPeriod_Type()
)
tptPolicyNotifyAggregationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyAggregationPeriod.setStatus("current")
_TptPolicyNotifySeverity_Type = PolicySeverity
_TptPolicyNotifySeverity_Object = MibScalar
tptPolicyNotifySeverity = _TptPolicyNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 25),
    _TptPolicyNotifySeverity_Type()
)
tptPolicyNotifySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySeverity.setStatus("current")


class _TptPolicyNotifyProtocol_Type(OctetString):
    """Custom type tptPolicyNotifyProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TptPolicyNotifyProtocol_Type.__name__ = "OctetString"
_TptPolicyNotifyProtocol_Object = MibScalar
tptPolicyNotifyProtocol = _TptPolicyNotifyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 26),
    _TptPolicyNotifyProtocol_Type()
)
tptPolicyNotifyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyProtocol.setStatus("current")
_TptPolicyNotifyAlertTimeSec_Type = Unsigned32
_TptPolicyNotifyAlertTimeSec_Object = MibScalar
tptPolicyNotifyAlertTimeSec = _TptPolicyNotifyAlertTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 27),
    _TptPolicyNotifyAlertTimeSec_Type()
)
tptPolicyNotifyAlertTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyAlertTimeSec.setStatus("current")
_TptPolicyNotifyAlertTimeNano_Type = Unsigned32
_TptPolicyNotifyAlertTimeNano_Object = MibScalar
tptPolicyNotifyAlertTimeNano = _TptPolicyNotifyAlertTimeNano_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 28),
    _TptPolicyNotifyAlertTimeNano_Type()
)
tptPolicyNotifyAlertTimeNano.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyAlertTimeNano.setStatus("current")
_TptPolicyNotifyPacketTrace_Type = Integer32
_TptPolicyNotifyPacketTrace_Object = MibScalar
tptPolicyNotifyPacketTrace = _TptPolicyNotifyPacketTrace_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 29),
    _TptPolicyNotifyPacketTrace_Type()
)
tptPolicyNotifyPacketTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyPacketTrace.setStatus("current")
_TptPolicyNotifySequence_Type = Counter64
_TptPolicyNotifySequence_Object = MibScalar
tptPolicyNotifySequence = _TptPolicyNotifySequence_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 30),
    _TptPolicyNotifySequence_Type()
)
tptPolicyNotifySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySequence.setStatus("current")
_TptPolicyNotifyTraceBucket_Type = Unsigned32
_TptPolicyNotifyTraceBucket_Object = MibScalar
tptPolicyNotifyTraceBucket = _TptPolicyNotifyTraceBucket_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 36),
    _TptPolicyNotifyTraceBucket_Type()
)
tptPolicyNotifyTraceBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyTraceBucket.setStatus("current")
_TptPolicyNotifyTraceBegin_Type = Unsigned32
_TptPolicyNotifyTraceBegin_Object = MibScalar
tptPolicyNotifyTraceBegin = _TptPolicyNotifyTraceBegin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 37),
    _TptPolicyNotifyTraceBegin_Type()
)
tptPolicyNotifyTraceBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyTraceBegin.setStatus("current")
_TptPolicyNotifyTraceEnd_Type = Unsigned32
_TptPolicyNotifyTraceEnd_Object = MibScalar
tptPolicyNotifyTraceEnd = _TptPolicyNotifyTraceEnd_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 38),
    _TptPolicyNotifyTraceEnd_Type()
)
tptPolicyNotifyTraceEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyTraceEnd.setStatus("current")
_TptPolicyNotifyMessageParams_Type = OctetString
_TptPolicyNotifyMessageParams_Object = MibScalar
tptPolicyNotifyMessageParams = _TptPolicyNotifyMessageParams_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 39),
    _TptPolicyNotifyMessageParams_Type()
)
tptPolicyNotifyMessageParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyMessageParams.setStatus("current")
_TptPolicyNotifyStartTimeNano_Type = Unsigned32
_TptPolicyNotifyStartTimeNano_Object = MibScalar
tptPolicyNotifyStartTimeNano = _TptPolicyNotifyStartTimeNano_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 40),
    _TptPolicyNotifyStartTimeNano_Type()
)
tptPolicyNotifyStartTimeNano.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyStartTimeNano.setStatus("current")
_TptPolicyNotifyAlertType_Type = Unsigned32
_TptPolicyNotifyAlertType_Object = MibScalar
tptPolicyNotifyAlertType = _TptPolicyNotifyAlertType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 41),
    _TptPolicyNotifyAlertType_Type()
)
tptPolicyNotifyAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyAlertType.setStatus("current")
_TptPolicyNotifyInputMphy_Type = Unsigned32
_TptPolicyNotifyInputMphy_Object = MibScalar
tptPolicyNotifyInputMphy = _TptPolicyNotifyInputMphy_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 57),
    _TptPolicyNotifyInputMphy_Type()
)
tptPolicyNotifyInputMphy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyInputMphy.setStatus("current")
_TptPolicyNotifyVlanTag_Type = Unsigned32
_TptPolicyNotifyVlanTag_Object = MibScalar
tptPolicyNotifyVlanTag = _TptPolicyNotifyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 58),
    _TptPolicyNotifyVlanTag_Type()
)
tptPolicyNotifyVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyVlanTag.setStatus("current")


class _TptPolicyNotifyZonePair_Type(OctetString):
    """Custom type tptPolicyNotifyZonePair based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptPolicyNotifyZonePair_Type.__name__ = "OctetString"
_TptPolicyNotifyZonePair_Object = MibScalar
tptPolicyNotifyZonePair = _TptPolicyNotifyZonePair_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 59),
    _TptPolicyNotifyZonePair_Type()
)
tptPolicyNotifyZonePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyZonePair.setStatus("current")


class _TptPolicyLogNotifyDeviceID_Type(OctetString):
    """Custom type tptPolicyLogNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyLogNotifyDeviceID_Type.__name__ = "OctetString"
_TptPolicyLogNotifyDeviceID_Object = MibScalar
tptPolicyLogNotifyDeviceID = _TptPolicyLogNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 121),
    _TptPolicyLogNotifyDeviceID_Type()
)
tptPolicyLogNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyLogNotifyDeviceID.setStatus("current")
_TptPolicyLogNotifyComponentID_Type = PolicyComponent
_TptPolicyLogNotifyComponentID_Object = MibScalar
tptPolicyLogNotifyComponentID = _TptPolicyLogNotifyComponentID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 122),
    _TptPolicyLogNotifyComponentID_Type()
)
tptPolicyLogNotifyComponentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyLogNotifyComponentID.setStatus("current")
_TptPolicyLogNotifyNumber_Type = Unsigned32
_TptPolicyLogNotifyNumber_Object = MibScalar
tptPolicyLogNotifyNumber = _TptPolicyLogNotifyNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 123),
    _TptPolicyLogNotifyNumber_Type()
)
tptPolicyLogNotifyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyLogNotifyNumber.setStatus("current")
_TptPolicyLogNotifyTrigger_Type = Unsigned32
_TptPolicyLogNotifyTrigger_Object = MibScalar
tptPolicyLogNotifyTrigger = _TptPolicyLogNotifyTrigger_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 124),
    _TptPolicyLogNotifyTrigger_Type()
)
tptPolicyLogNotifyTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyLogNotifyTrigger.setStatus("current")
_TptPolicyLogNotifySequence_Type = Counter64
_TptPolicyLogNotifySequence_Object = MibScalar
tptPolicyLogNotifySequence = _TptPolicyLogNotifySequence_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 125),
    _TptPolicyLogNotifySequence_Type()
)
tptPolicyLogNotifySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyLogNotifySequence.setStatus("current")
_TptPolicyNotifySrcNetAddrV6_Type = Ipv6Address
_TptPolicyNotifySrcNetAddrV6_Object = MibScalar
tptPolicyNotifySrcNetAddrV6 = _TptPolicyNotifySrcNetAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 128),
    _TptPolicyNotifySrcNetAddrV6_Type()
)
tptPolicyNotifySrcNetAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySrcNetAddrV6.setStatus("current")
_TptPolicyNotifyDestNetAddrV6_Type = Ipv6Address
_TptPolicyNotifyDestNetAddrV6_Object = MibScalar
tptPolicyNotifyDestNetAddrV6 = _TptPolicyNotifyDestNetAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 129),
    _TptPolicyNotifyDestNetAddrV6_Type()
)
tptPolicyNotifyDestNetAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyDestNetAddrV6.setStatus("current")


class _TptPolicyNotifyActionSetID_Type(OctetString):
    """Custom type tptPolicyNotifyActionSetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifyActionSetID_Type.__name__ = "OctetString"
_TptPolicyNotifyActionSetID_Object = MibScalar
tptPolicyNotifyActionSetID = _TptPolicyNotifyActionSetID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 130),
    _TptPolicyNotifyActionSetID_Type()
)
tptPolicyNotifyActionSetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyActionSetID.setStatus("current")
_TptPolicyNotifyRate_Type = Integer32
_TptPolicyNotifyRate_Object = MibScalar
tptPolicyNotifyRate = _TptPolicyNotifyRate_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 131),
    _TptPolicyNotifyRate_Type()
)
tptPolicyNotifyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyRate.setStatus("current")


class _TptPolicyNotifyFlowControl_Type(OctetString):
    """Custom type tptPolicyNotifyFlowControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifyFlowControl_Type.__name__ = "OctetString"
_TptPolicyNotifyFlowControl_Object = MibScalar
tptPolicyNotifyFlowControl = _TptPolicyNotifyFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 137),
    _TptPolicyNotifyFlowControl_Type()
)
tptPolicyNotifyFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyFlowControl.setStatus("current")


class _TptPolicyNotifyActionSetName_Type(OctetString):
    """Custom type tptPolicyNotifyActionSetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptPolicyNotifyActionSetName_Type.__name__ = "OctetString"
_TptPolicyNotifyActionSetName_Object = MibScalar
tptPolicyNotifyActionSetName = _TptPolicyNotifyActionSetName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 138),
    _TptPolicyNotifyActionSetName_Type()
)
tptPolicyNotifyActionSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyActionSetName.setStatus("current")


class _TptPolicyNotifyClientip_Type(OctetString):
    """Custom type tptPolicyNotifyClientip based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptPolicyNotifyClientip_Type.__name__ = "OctetString"
_TptPolicyNotifyClientip_Object = MibScalar
tptPolicyNotifyClientip = _TptPolicyNotifyClientip_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 139),
    _TptPolicyNotifyClientip_Type()
)
tptPolicyNotifyClientip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyClientip.setStatus("current")


class _TptPolicyNotifyMetadata_Type(OctetString):
    """Custom type tptPolicyNotifyMetadata based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptPolicyNotifyMetadata_Type.__name__ = "OctetString"
_TptPolicyNotifyMetadata_Object = MibScalar
tptPolicyNotifyMetadata = _TptPolicyNotifyMetadata_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 140),
    _TptPolicyNotifyMetadata_Type()
)
tptPolicyNotifyMetadata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifyMetadata.setStatus("current")
_TptPolicyNotifySslInspected_Type = SslInspectedFlag
_TptPolicyNotifySslInspected_Object = MibScalar
tptPolicyNotifySslInspected = _TptPolicyNotifySslInspected_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 180),
    _TptPolicyNotifySslInspected_Type()
)
tptPolicyNotifySslInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspected.setStatus("current")


class _TptPolicyNotifyVirtualSegment_Type(SnmpAdminString):
    """Custom type tptPolicyNotifyVirtualSegment based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TptPolicyNotifyVirtualSegment_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifyVirtualSegment_Object = MibScalar
tptPolicyNotifyVirtualSegment = _TptPolicyNotifyVirtualSegment_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 182),
    _TptPolicyNotifyVirtualSegment_Type()
)
tptPolicyNotifyVirtualSegment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifyVirtualSegment.setStatus("current")
_TptPolicyNotifySslInspEventType_Type = SslInspEventType
_TptPolicyNotifySslInspEventType_Object = MibScalar
tptPolicyNotifySslInspEventType = _TptPolicyNotifySslInspEventType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 190),
    _TptPolicyNotifySslInspEventType_Type()
)
tptPolicyNotifySslInspEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspEventType.setStatus("current")
_TptPolicyNotifySslInspAction_Type = SslInspAction
_TptPolicyNotifySslInspAction_Object = MibScalar
tptPolicyNotifySslInspAction = _TptPolicyNotifySslInspAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 191),
    _TptPolicyNotifySslInspAction_Type()
)
tptPolicyNotifySslInspAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspAction.setStatus("current")


class _TptPolicyNotifySslInspDetails_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspDetails based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptPolicyNotifySslInspDetails_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspDetails_Object = MibScalar
tptPolicyNotifySslInspDetails = _TptPolicyNotifySslInspDetails_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 192),
    _TptPolicyNotifySslInspDetails_Type()
)
tptPolicyNotifySslInspDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspDetails.setStatus("current")


class _TptPolicyNotifySslInspPolicy_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TptPolicyNotifySslInspPolicy_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspPolicy_Object = MibScalar
tptPolicyNotifySslInspPolicy = _TptPolicyNotifySslInspPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 193),
    _TptPolicyNotifySslInspPolicy_Type()
)
tptPolicyNotifySslInspPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspPolicy.setStatus("current")


class _TptPolicyNotifySslInspCert_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspCert based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TptPolicyNotifySslInspCert_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspCert_Object = MibScalar
tptPolicyNotifySslInspCert = _TptPolicyNotifySslInspCert_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 194),
    _TptPolicyNotifySslInspCert_Type()
)
tptPolicyNotifySslInspCert.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspCert.setStatus("current")


class _TptPolicyNotifySslInspCltIF_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspCltIF based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifySslInspCltIF_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspCltIF_Object = MibScalar
tptPolicyNotifySslInspCltIF = _TptPolicyNotifySslInspCltIF_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 195),
    _TptPolicyNotifySslInspCltIF_Type()
)
tptPolicyNotifySslInspCltIF.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspCltIF.setStatus("current")
_TptPolicyNotifySslInspCltSslVer_Type = SslProtocol
_TptPolicyNotifySslInspCltSslVer_Object = MibScalar
tptPolicyNotifySslInspCltSslVer = _TptPolicyNotifySslInspCltSslVer_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 196),
    _TptPolicyNotifySslInspCltSslVer_Type()
)
tptPolicyNotifySslInspCltSslVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspCltSslVer.setStatus("current")


class _TptPolicyNotifySslInspCltCrypto_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspCltCrypto based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptPolicyNotifySslInspCltCrypto_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspCltCrypto_Object = MibScalar
tptPolicyNotifySslInspCltCrypto = _TptPolicyNotifySslInspCltCrypto_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 197),
    _TptPolicyNotifySslInspCltCrypto_Type()
)
tptPolicyNotifySslInspCltCrypto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspCltCrypto.setStatus("current")


class _TptPolicyNotifySslInspSrvIF_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspSrvIF based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPolicyNotifySslInspSrvIF_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspSrvIF_Object = MibScalar
tptPolicyNotifySslInspSrvIF = _TptPolicyNotifySslInspSrvIF_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 198),
    _TptPolicyNotifySslInspSrvIF_Type()
)
tptPolicyNotifySslInspSrvIF.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspSrvIF.setStatus("current")
_TptPolicyNotifySslInspSrvSslVer_Type = SslProtocol
_TptPolicyNotifySslInspSrvSslVer_Object = MibScalar
tptPolicyNotifySslInspSrvSslVer = _TptPolicyNotifySslInspSrvSslVer_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 199),
    _TptPolicyNotifySslInspSrvSslVer_Type()
)
tptPolicyNotifySslInspSrvSslVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspSrvSslVer.setStatus("current")


class _TptPolicyNotifySslInspSrvCrypto_Type(SnmpAdminString):
    """Custom type tptPolicyNotifySslInspSrvCrypto based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptPolicyNotifySslInspSrvCrypto_Type.__name__ = "SnmpAdminString"
_TptPolicyNotifySslInspSrvCrypto_Object = MibScalar
tptPolicyNotifySslInspSrvCrypto = _TptPolicyNotifySslInspSrvCrypto_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 200),
    _TptPolicyNotifySslInspSrvCrypto_Type()
)
tptPolicyNotifySslInspSrvCrypto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptPolicyNotifySslInspSrvCrypto.setStatus("current")

# Managed Objects groups


# Notification objects

tptPolicyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 8)
)
tptPolicyNotify.setObjects(
      *(("TPT-POLICY-MIB", "tptPolicyNotifyDeviceID"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyPolicyID"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySignatureID"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyZonePair"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyInputMphy"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyVlanTag"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySrcNetAddr"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySrcNetPort"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyDestNetAddr"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyDestNetPort"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyProtocol"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyMessageParams"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyHitCount"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAggregationPeriod"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyStartTimeSec"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyStartTimeNano"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAlertTimeSec"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAlertTimeNano"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyPacketTrace"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyTraceBucket"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyTraceBegin"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyTraceEnd"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAlertAction"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyConfigAction"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyComponentID"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAlertType"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySeverity"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySequence"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySrcNetAddrV6"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyDestNetAddrV6"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyActionSetID"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyRate"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyFlowControl"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyActionSetName"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyClientip"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyMetadata"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspected"))
)
if mibBuilder.loadTexts:
    tptPolicyNotify.setStatus(
        "current"
    )

tptPolicyLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 19)
)
tptPolicyLogNotify.setObjects(
      *(("TPT-POLICY-MIB", "tptPolicyLogNotifyDeviceID"),
        ("TPT-POLICY-MIB", "tptPolicyLogNotifyComponentID"),
        ("TPT-POLICY-MIB", "tptPolicyLogNotifyNumber"),
        ("TPT-POLICY-MIB", "tptPolicyLogNotifyTrigger"),
        ("TPT-POLICY-MIB", "tptPolicyLogNotifySequence"))
)
if mibBuilder.loadTexts:
    tptPolicyLogNotify.setStatus(
        "current"
    )

tptPolicySslInspNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 27)
)
tptPolicySslInspNotify.setObjects(
      *(("TPT-POLICY-MIB", "tptPolicyNotifyDeviceID"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAlertTimeSec"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyAlertTimeNano"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspEventType"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySeverity"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspAction"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspDetails"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyVirtualSegment"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspPolicy"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspCert"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspCltIF"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspCltSslVer"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspCltCrypto"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspSrvIF"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspSrvSslVer"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySslInspSrvCrypto"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySrcNetAddr"),
        ("TPT-POLICY-MIB", "tptPolicyNotifySrcNetPort"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyDestNetAddr"),
        ("TPT-POLICY-MIB", "tptPolicyNotifyDestNetPort"))
)
if mibBuilder.loadTexts:
    tptPolicySslInspNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-POLICY-MIB",
    **{"PolicyProtocol": PolicyProtocol,
       "PolicyFrameSize": PolicyFrameSize,
       "PolicyFrameType": PolicyFrameType,
       "PolicySeverity": PolicySeverity,
       "PolicyAction": PolicyAction,
       "PolicyComponent": PolicyComponent,
       "SslInspectedFlag": SslInspectedFlag,
       "SslProtocol": SslProtocol,
       "SslInspEventType": SslInspEventType,
       "SslInspAction": SslInspAction,
       "tpt-policy": tpt_policy,
       "policyPacketsDropped": policyPacketsDropped,
       "policyPacketsBlocked": policyPacketsBlocked,
       "policyPacketsIncoming": policyPacketsIncoming,
       "policyPacketsOutgoing": policyPacketsOutgoing,
       "policyCounterTable": policyCounterTable,
       "policyCounterEntry": policyCounterEntry,
       "policyGlobalID": policyGlobalID,
       "policyDescriptiveName": policyDescriptiveName,
       "policyCountBytes": policyCountBytes,
       "policyCountPackets": policyCountPackets,
       "policyCreationTime": policyCreationTime,
       "policyPacketsInvalid": policyPacketsInvalid,
       "policyPacketsPermitted": policyPacketsPermitted,
       "policyDVObjs": policyDVObjs,
       "policyDVVersion": policyDVVersion,
       "topTenHitsByPolicyTable": topTenHitsByPolicyTable,
       "topTenHitsByPolicyEntry": topTenHitsByPolicyEntry,
       "topTenRank": topTenRank,
       "policyHitCount": policyHitCount,
       "policyName": policyName,
       "policyUUID": policyUUID,
       "alertsBySeverityTable": alertsBySeverityTable,
       "alertsBySeverityEntry": alertsBySeverityEntry,
       "alertSeverity": alertSeverity,
       "severityAlertCount": severityAlertCount,
       "alertsByProtocolTable": alertsByProtocolTable,
       "alertsByProtocolEntry": alertsByProtocolEntry,
       "alertProtocol": alertProtocol,
       "protocolAlertCount": protocolAlertCount,
       "alertsByZoneTable": alertsByZoneTable,
       "alertsByZoneEntry": alertsByZoneEntry,
       "alertSlot": alertSlot,
       "alertPort": alertPort,
       "zoneAlertCount": zoneAlertCount,
       "permitsByZoneTable": permitsByZoneTable,
       "permitsByZoneEntry": permitsByZoneEntry,
       "permitSlot": permitSlot,
       "permitPort": permitPort,
       "zonePermitCount": zonePermitCount,
       "blocksByZoneTable": blocksByZoneTable,
       "blocksByZoneEntry": blocksByZoneEntry,
       "blockSlot": blockSlot,
       "blockPort": blockPort,
       "zoneBlockCount": zoneBlockCount,
       "p2psByZoneTable": p2psByZoneTable,
       "p2psByZoneEntry": p2psByZoneEntry,
       "p2pSlot": p2pSlot,
       "p2pPort": p2pPort,
       "zoneP2pCount": zoneP2pCount,
       "framesBySizeTable": framesBySizeTable,
       "framesBySizeEntry": framesBySizeEntry,
       "frameSize": frameSize,
       "sizeFrameCount": sizeFrameCount,
       "framesByTypeTable": framesByTypeTable,
       "framesByTypeEntry": framesByTypeEntry,
       "frameType": frameType,
       "typeFrameCount": typeFrameCount,
       "packetsByProtocolTable": packetsByProtocolTable,
       "packetsByProtocolEntry": packetsByProtocolEntry,
       "packetProtocol": packetProtocol,
       "protocolPacketCount": protocolPacketCount,
       "policyByNumberTable": policyByNumberTable,
       "policyByNumberEntry": policyByNumberEntry,
       "policyNumber": policyNumber,
       "numberName": numberName,
       "numberDesc": numberDesc,
       "securityZonePairTable": securityZonePairTable,
       "securityZonePairEntry": securityZonePairEntry,
       "szpName": szpName,
       "szpInZoneName": szpInZoneName,
       "szpOutZoneName": szpOutZoneName,
       "szpUUID": szpUUID,
       "szpInZoneUUID": szpInZoneUUID,
       "szpOutZoneUUID": szpOutZoneUUID,
       "szpInPackets": szpInPackets,
       "szpInOctets": szpInOctets,
       "szpAlerts": szpAlerts,
       "szpBlocks": szpBlocks,
       "szpPermits": szpPermits,
       "szpPrecedence": szpPrecedence,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "portNumber": portNumber,
       "portName": portName,
       "portVlanTranslations": portVlanTranslations,
       "policyPacketsDropped64": policyPacketsDropped64,
       "policyPacketsBlocked64": policyPacketsBlocked64,
       "policyPacketsIncoming64": policyPacketsIncoming64,
       "policyPacketsOutgoing64": policyPacketsOutgoing64,
       "policyPacketsInvalid64": policyPacketsInvalid64,
       "policyPacketsPermitted64": policyPacketsPermitted64,
       "policyPacketsRateLimited64": policyPacketsRateLimited64,
       "policyPacketsTrusted64": policyPacketsTrusted64,
       "tptPolicyNotify": tptPolicyNotify,
       "tptPolicyLogNotify": tptPolicyLogNotify,
       "tptPolicySslInspNotify": tptPolicySslInspNotify,
       "tptPolicyNotifyDeviceID": tptPolicyNotifyDeviceID,
       "tptPolicyNotifyPolicyID": tptPolicyNotifyPolicyID,
       "tptPolicyNotifySignatureID": tptPolicyNotifySignatureID,
       "tptPolicyNotifySegmentName": tptPolicyNotifySegmentName,
       "tptPolicyNotifySrcNetAddr": tptPolicyNotifySrcNetAddr,
       "tptPolicyNotifySrcNetPort": tptPolicyNotifySrcNetPort,
       "tptPolicyNotifyDestNetAddr": tptPolicyNotifyDestNetAddr,
       "tptPolicyNotifyDestNetPort": tptPolicyNotifyDestNetPort,
       "tptPolicyNotifyStartTimeSec": tptPolicyNotifyStartTimeSec,
       "tptPolicyNotifyAlertAction": tptPolicyNotifyAlertAction,
       "tptPolicyNotifyConfigAction": tptPolicyNotifyConfigAction,
       "tptPolicyNotifyComponentID": tptPolicyNotifyComponentID,
       "tptPolicyNotifyHitCount": tptPolicyNotifyHitCount,
       "tptPolicyNotifyAggregationPeriod": tptPolicyNotifyAggregationPeriod,
       "tptPolicyNotifySeverity": tptPolicyNotifySeverity,
       "tptPolicyNotifyProtocol": tptPolicyNotifyProtocol,
       "tptPolicyNotifyAlertTimeSec": tptPolicyNotifyAlertTimeSec,
       "tptPolicyNotifyAlertTimeNano": tptPolicyNotifyAlertTimeNano,
       "tptPolicyNotifyPacketTrace": tptPolicyNotifyPacketTrace,
       "tptPolicyNotifySequence": tptPolicyNotifySequence,
       "tptPolicyNotifyTraceBucket": tptPolicyNotifyTraceBucket,
       "tptPolicyNotifyTraceBegin": tptPolicyNotifyTraceBegin,
       "tptPolicyNotifyTraceEnd": tptPolicyNotifyTraceEnd,
       "tptPolicyNotifyMessageParams": tptPolicyNotifyMessageParams,
       "tptPolicyNotifyStartTimeNano": tptPolicyNotifyStartTimeNano,
       "tptPolicyNotifyAlertType": tptPolicyNotifyAlertType,
       "tptPolicyNotifyInputMphy": tptPolicyNotifyInputMphy,
       "tptPolicyNotifyVlanTag": tptPolicyNotifyVlanTag,
       "tptPolicyNotifyZonePair": tptPolicyNotifyZonePair,
       "tptPolicyLogNotifyDeviceID": tptPolicyLogNotifyDeviceID,
       "tptPolicyLogNotifyComponentID": tptPolicyLogNotifyComponentID,
       "tptPolicyLogNotifyNumber": tptPolicyLogNotifyNumber,
       "tptPolicyLogNotifyTrigger": tptPolicyLogNotifyTrigger,
       "tptPolicyLogNotifySequence": tptPolicyLogNotifySequence,
       "tptPolicyNotifySrcNetAddrV6": tptPolicyNotifySrcNetAddrV6,
       "tptPolicyNotifyDestNetAddrV6": tptPolicyNotifyDestNetAddrV6,
       "tptPolicyNotifyActionSetID": tptPolicyNotifyActionSetID,
       "tptPolicyNotifyRate": tptPolicyNotifyRate,
       "tptPolicyNotifyFlowControl": tptPolicyNotifyFlowControl,
       "tptPolicyNotifyActionSetName": tptPolicyNotifyActionSetName,
       "tptPolicyNotifyClientip": tptPolicyNotifyClientip,
       "tptPolicyNotifyMetadata": tptPolicyNotifyMetadata,
       "tptPolicyNotifySslInspected": tptPolicyNotifySslInspected,
       "tptPolicyNotifyVirtualSegment": tptPolicyNotifyVirtualSegment,
       "tptPolicyNotifySslInspEventType": tptPolicyNotifySslInspEventType,
       "tptPolicyNotifySslInspAction": tptPolicyNotifySslInspAction,
       "tptPolicyNotifySslInspDetails": tptPolicyNotifySslInspDetails,
       "tptPolicyNotifySslInspPolicy": tptPolicyNotifySslInspPolicy,
       "tptPolicyNotifySslInspCert": tptPolicyNotifySslInspCert,
       "tptPolicyNotifySslInspCltIF": tptPolicyNotifySslInspCltIF,
       "tptPolicyNotifySslInspCltSslVer": tptPolicyNotifySslInspCltSslVer,
       "tptPolicyNotifySslInspCltCrypto": tptPolicyNotifySslInspCltCrypto,
       "tptPolicyNotifySslInspSrvIF": tptPolicyNotifySslInspSrvIF,
       "tptPolicyNotifySslInspSrvSslVer": tptPolicyNotifySslInspSrvSslVer,
       "tptPolicyNotifySslInspSrvCrypto": tptPolicyNotifySslInspSrvCrypto}
)
