# SNMP MIB module (Juniper-DHCPv6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DHCPv6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:57 2024
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

(Ipv6AddressPrefix,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressPrefix")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

juniDhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69)
)
juniDhcpv6MIB.setRevisions(
        ("2003-05-08 17:15",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniDhcpv6LocalServerModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localServerModeTypeEqualAccess", 1),
          ("localServerModeTypeStandalone", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JuniDhcpv6Objects_ObjectIdentity = ObjectIdentity
juniDhcpv6Objects = _JuniDhcpv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1)
)
_JuniDhcpv6LocalServerObjects_ObjectIdentity = ObjectIdentity
juniDhcpv6LocalServerObjects = _JuniDhcpv6LocalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1)
)
_JuniDhcpv6LocalServerStatistics_ObjectIdentity = ObjectIdentity
juniDhcpv6LocalServerStatistics = _JuniDhcpv6LocalServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1)
)
_JuniDhcpv6LocalServerMemUsage_Type = Counter32
_JuniDhcpv6LocalServerMemUsage_Object = MibScalar
juniDhcpv6LocalServerMemUsage = _JuniDhcpv6LocalServerMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 1),
    _JuniDhcpv6LocalServerMemUsage_Type()
)
juniDhcpv6LocalServerMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerMemUsage.setStatus("current")
_JuniDhcpv6LocalServerNumBindings_Type = Counter32
_JuniDhcpv6LocalServerNumBindings_Object = MibScalar
juniDhcpv6LocalServerNumBindings = _JuniDhcpv6LocalServerNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 2),
    _JuniDhcpv6LocalServerNumBindings_Type()
)
juniDhcpv6LocalServerNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerNumBindings.setStatus("current")
_JuniDhcpv6LocalServerRxSolicits_Type = Counter32
_JuniDhcpv6LocalServerRxSolicits_Object = MibScalar
juniDhcpv6LocalServerRxSolicits = _JuniDhcpv6LocalServerRxSolicits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 3),
    _JuniDhcpv6LocalServerRxSolicits_Type()
)
juniDhcpv6LocalServerRxSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxSolicits.setStatus("current")
_JuniDhcpv6LocalServerRxAccepts_Type = Counter32
_JuniDhcpv6LocalServerRxAccepts_Object = MibScalar
juniDhcpv6LocalServerRxAccepts = _JuniDhcpv6LocalServerRxAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 4),
    _JuniDhcpv6LocalServerRxAccepts_Type()
)
juniDhcpv6LocalServerRxAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxAccepts.setStatus("current")
_JuniDhcpv6LocalServerRxRenews_Type = Counter32
_JuniDhcpv6LocalServerRxRenews_Object = MibScalar
juniDhcpv6LocalServerRxRenews = _JuniDhcpv6LocalServerRxRenews_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 5),
    _JuniDhcpv6LocalServerRxRenews_Type()
)
juniDhcpv6LocalServerRxRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxRenews.setStatus("current")
_JuniDhcpv6LocalServerRxDeclines_Type = Counter32
_JuniDhcpv6LocalServerRxDeclines_Object = MibScalar
juniDhcpv6LocalServerRxDeclines = _JuniDhcpv6LocalServerRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 6),
    _JuniDhcpv6LocalServerRxDeclines_Type()
)
juniDhcpv6LocalServerRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxDeclines.setStatus("current")
_JuniDhcpv6LocalServerRxReleases_Type = Counter32
_JuniDhcpv6LocalServerRxReleases_Object = MibScalar
juniDhcpv6LocalServerRxReleases = _JuniDhcpv6LocalServerRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 7),
    _JuniDhcpv6LocalServerRxReleases_Type()
)
juniDhcpv6LocalServerRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxReleases.setStatus("current")
_JuniDhcpv6LocalServerRxInforms_Type = Counter32
_JuniDhcpv6LocalServerRxInforms_Object = MibScalar
juniDhcpv6LocalServerRxInforms = _JuniDhcpv6LocalServerRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 8),
    _JuniDhcpv6LocalServerRxInforms_Type()
)
juniDhcpv6LocalServerRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxInforms.setStatus("current")
_JuniDhcpv6LocalServerRxConfirms_Type = Counter32
_JuniDhcpv6LocalServerRxConfirms_Object = MibScalar
juniDhcpv6LocalServerRxConfirms = _JuniDhcpv6LocalServerRxConfirms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 9),
    _JuniDhcpv6LocalServerRxConfirms_Type()
)
juniDhcpv6LocalServerRxConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxConfirms.setStatus("current")
_JuniDhcpv6LocalServerRxRebinds_Type = Counter32
_JuniDhcpv6LocalServerRxRebinds_Object = MibScalar
juniDhcpv6LocalServerRxRebinds = _JuniDhcpv6LocalServerRxRebinds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 10),
    _JuniDhcpv6LocalServerRxRebinds_Type()
)
juniDhcpv6LocalServerRxRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerRxRebinds.setStatus("current")
_JuniDhcpv6LocalServerTxReconfigures_Type = Counter32
_JuniDhcpv6LocalServerTxReconfigures_Object = MibScalar
juniDhcpv6LocalServerTxReconfigures = _JuniDhcpv6LocalServerTxReconfigures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 11),
    _JuniDhcpv6LocalServerTxReconfigures_Type()
)
juniDhcpv6LocalServerTxReconfigures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerTxReconfigures.setStatus("current")
_JuniDhcpv6LocalServerTxAdvertises_Type = Counter32
_JuniDhcpv6LocalServerTxAdvertises_Object = MibScalar
juniDhcpv6LocalServerTxAdvertises = _JuniDhcpv6LocalServerTxAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 12),
    _JuniDhcpv6LocalServerTxAdvertises_Type()
)
juniDhcpv6LocalServerTxAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerTxAdvertises.setStatus("current")
_JuniDhcpv6LocalServerTxSuccessfulReplies_Type = Counter32
_JuniDhcpv6LocalServerTxSuccessfulReplies_Object = MibScalar
juniDhcpv6LocalServerTxSuccessfulReplies = _JuniDhcpv6LocalServerTxSuccessfulReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 13),
    _JuniDhcpv6LocalServerTxSuccessfulReplies_Type()
)
juniDhcpv6LocalServerTxSuccessfulReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerTxSuccessfulReplies.setStatus("current")
_JuniDhcpv6LocalServerTxFailedReplies_Type = Counter32
_JuniDhcpv6LocalServerTxFailedReplies_Object = MibScalar
juniDhcpv6LocalServerTxFailedReplies = _JuniDhcpv6LocalServerTxFailedReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 14),
    _JuniDhcpv6LocalServerTxFailedReplies_Type()
)
juniDhcpv6LocalServerTxFailedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerTxFailedReplies.setStatus("current")
_JuniDhcpv6LocalServerUnknownMessages_Type = Counter32
_JuniDhcpv6LocalServerUnknownMessages_Object = MibScalar
juniDhcpv6LocalServerUnknownMessages = _JuniDhcpv6LocalServerUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 15),
    _JuniDhcpv6LocalServerUnknownMessages_Type()
)
juniDhcpv6LocalServerUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerUnknownMessages.setStatus("current")
_JuniDhcpv6LocalServerBadMessages_Type = Counter32
_JuniDhcpv6LocalServerBadMessages_Object = MibScalar
juniDhcpv6LocalServerBadMessages = _JuniDhcpv6LocalServerBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 16),
    _JuniDhcpv6LocalServerBadMessages_Type()
)
juniDhcpv6LocalServerBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBadMessages.setStatus("current")
_JuniDhcpv6LocalServerPacketsIn_Type = Counter32
_JuniDhcpv6LocalServerPacketsIn_Object = MibScalar
juniDhcpv6LocalServerPacketsIn = _JuniDhcpv6LocalServerPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 17),
    _JuniDhcpv6LocalServerPacketsIn_Type()
)
juniDhcpv6LocalServerPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerPacketsIn.setStatus("current")
_JuniDhcpv6LocalServerPacketsOut_Type = Counter32
_JuniDhcpv6LocalServerPacketsOut_Object = MibScalar
juniDhcpv6LocalServerPacketsOut = _JuniDhcpv6LocalServerPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 18),
    _JuniDhcpv6LocalServerPacketsOut_Type()
)
juniDhcpv6LocalServerPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerPacketsOut.setStatus("current")
_JuniDhcpv6LocalServerAttributes_ObjectIdentity = ObjectIdentity
juniDhcpv6LocalServerAttributes = _JuniDhcpv6LocalServerAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 2)
)
_JuniDhcpv6LocalServerAttributesMode_Type = JuniDhcpv6LocalServerModeType
_JuniDhcpv6LocalServerAttributesMode_Object = MibScalar
juniDhcpv6LocalServerAttributesMode = _JuniDhcpv6LocalServerAttributesMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 2, 1),
    _JuniDhcpv6LocalServerAttributesMode_Type()
)
juniDhcpv6LocalServerAttributesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerAttributesMode.setStatus("current")
_JuniDhcpv6LocalServerBindings_ObjectIdentity = ObjectIdentity
juniDhcpv6LocalServerBindings = _JuniDhcpv6LocalServerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3)
)
_JuniDhcpv6LocalServerBindingsTable_Object = MibTable
juniDhcpv6LocalServerBindingsTable = _JuniDhcpv6LocalServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsTable.setStatus("current")
_JuniDhcpv6LocalServerBindingsEntry_Object = MibTableRow
juniDhcpv6LocalServerBindingsEntry = _JuniDhcpv6LocalServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1)
)
juniDhcpv6LocalServerBindingsEntry.setIndexNames(
    (0, "Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsPrefix"),
    (0, "Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsLength"),
)
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsEntry.setStatus("current")
_JuniDhcpv6LocalServerBindingsPrefix_Type = Ipv6AddressPrefix
_JuniDhcpv6LocalServerBindingsPrefix_Object = MibTableColumn
juniDhcpv6LocalServerBindingsPrefix = _JuniDhcpv6LocalServerBindingsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 1),
    _JuniDhcpv6LocalServerBindingsPrefix_Type()
)
juniDhcpv6LocalServerBindingsPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsPrefix.setStatus("current")


class _JuniDhcpv6LocalServerBindingsLength_Type(Integer32):
    """Custom type juniDhcpv6LocalServerBindingsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_JuniDhcpv6LocalServerBindingsLength_Type.__name__ = "Integer32"
_JuniDhcpv6LocalServerBindingsLength_Object = MibTableColumn
juniDhcpv6LocalServerBindingsLength = _JuniDhcpv6LocalServerBindingsLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 2),
    _JuniDhcpv6LocalServerBindingsLength_Type()
)
juniDhcpv6LocalServerBindingsLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsLength.setStatus("current")


class _JuniDhcpv6LocalServerBindingsClientDuid_Type(OctetString):
    """Custom type juniDhcpv6LocalServerBindingsClientDuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_JuniDhcpv6LocalServerBindingsClientDuid_Type.__name__ = "OctetString"
_JuniDhcpv6LocalServerBindingsClientDuid_Object = MibTableColumn
juniDhcpv6LocalServerBindingsClientDuid = _JuniDhcpv6LocalServerBindingsClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 3),
    _JuniDhcpv6LocalServerBindingsClientDuid_Type()
)
juniDhcpv6LocalServerBindingsClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsClientDuid.setStatus("current")
_JuniDhcpv6LocalServerBindingsInfinite_Type = TruthValue
_JuniDhcpv6LocalServerBindingsInfinite_Object = MibTableColumn
juniDhcpv6LocalServerBindingsInfinite = _JuniDhcpv6LocalServerBindingsInfinite_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 4),
    _JuniDhcpv6LocalServerBindingsInfinite_Type()
)
juniDhcpv6LocalServerBindingsInfinite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsInfinite.setStatus("current")
_JuniDhcpv6LocalServerBindingsExpireTime_Type = TimeInterval
_JuniDhcpv6LocalServerBindingsExpireTime_Object = MibTableColumn
juniDhcpv6LocalServerBindingsExpireTime = _JuniDhcpv6LocalServerBindingsExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 5),
    _JuniDhcpv6LocalServerBindingsExpireTime_Type()
)
juniDhcpv6LocalServerBindingsExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsExpireTime.setStatus("current")


class _JuniDhcpv6LocalServerBindingsIf_Type(OctetString):
    """Custom type juniDhcpv6LocalServerBindingsIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniDhcpv6LocalServerBindingsIf_Type.__name__ = "OctetString"
_JuniDhcpv6LocalServerBindingsIf_Object = MibTableColumn
juniDhcpv6LocalServerBindingsIf = _JuniDhcpv6LocalServerBindingsIf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 6),
    _JuniDhcpv6LocalServerBindingsIf_Type()
)
juniDhcpv6LocalServerBindingsIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerBindingsIf.setStatus("current")
_JuniDhcpv6MIBConformance_ObjectIdentity = ObjectIdentity
juniDhcpv6MIBConformance = _JuniDhcpv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2)
)
_JuniDhcpv6MIBCompliances_ObjectIdentity = ObjectIdentity
juniDhcpv6MIBCompliances = _JuniDhcpv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 1)
)
_JuniDhcpv6MIBGroups_ObjectIdentity = ObjectIdentity
juniDhcpv6MIBGroups = _JuniDhcpv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 2)
)

# Managed Objects groups

juniDhcpv6LocalServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 2, 1)
)
juniDhcpv6LocalServerGroup.setObjects(
      *(("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerMemUsage"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerNumBindings"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxSolicits"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxAccepts"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxRenews"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxDeclines"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxReleases"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxInforms"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxConfirms"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxRebinds"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxReconfigures"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxAdvertises"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxSuccessfulReplies"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxFailedReplies"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerUnknownMessages"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBadMessages"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerPacketsIn"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerPacketsOut"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsClientDuid"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsInfinite"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsExpireTime"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsIf"),
        ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerAttributesMode"))
)
if mibBuilder.loadTexts:
    juniDhcpv6LocalServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniDhcpv6Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniDhcpv6Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DHCPv6-MIB",
    **{"JuniDhcpv6LocalServerModeType": JuniDhcpv6LocalServerModeType,
       "juniDhcpv6MIB": juniDhcpv6MIB,
       "juniDhcpv6Objects": juniDhcpv6Objects,
       "juniDhcpv6LocalServerObjects": juniDhcpv6LocalServerObjects,
       "juniDhcpv6LocalServerStatistics": juniDhcpv6LocalServerStatistics,
       "juniDhcpv6LocalServerMemUsage": juniDhcpv6LocalServerMemUsage,
       "juniDhcpv6LocalServerNumBindings": juniDhcpv6LocalServerNumBindings,
       "juniDhcpv6LocalServerRxSolicits": juniDhcpv6LocalServerRxSolicits,
       "juniDhcpv6LocalServerRxAccepts": juniDhcpv6LocalServerRxAccepts,
       "juniDhcpv6LocalServerRxRenews": juniDhcpv6LocalServerRxRenews,
       "juniDhcpv6LocalServerRxDeclines": juniDhcpv6LocalServerRxDeclines,
       "juniDhcpv6LocalServerRxReleases": juniDhcpv6LocalServerRxReleases,
       "juniDhcpv6LocalServerRxInforms": juniDhcpv6LocalServerRxInforms,
       "juniDhcpv6LocalServerRxConfirms": juniDhcpv6LocalServerRxConfirms,
       "juniDhcpv6LocalServerRxRebinds": juniDhcpv6LocalServerRxRebinds,
       "juniDhcpv6LocalServerTxReconfigures": juniDhcpv6LocalServerTxReconfigures,
       "juniDhcpv6LocalServerTxAdvertises": juniDhcpv6LocalServerTxAdvertises,
       "juniDhcpv6LocalServerTxSuccessfulReplies": juniDhcpv6LocalServerTxSuccessfulReplies,
       "juniDhcpv6LocalServerTxFailedReplies": juniDhcpv6LocalServerTxFailedReplies,
       "juniDhcpv6LocalServerUnknownMessages": juniDhcpv6LocalServerUnknownMessages,
       "juniDhcpv6LocalServerBadMessages": juniDhcpv6LocalServerBadMessages,
       "juniDhcpv6LocalServerPacketsIn": juniDhcpv6LocalServerPacketsIn,
       "juniDhcpv6LocalServerPacketsOut": juniDhcpv6LocalServerPacketsOut,
       "juniDhcpv6LocalServerAttributes": juniDhcpv6LocalServerAttributes,
       "juniDhcpv6LocalServerAttributesMode": juniDhcpv6LocalServerAttributesMode,
       "juniDhcpv6LocalServerBindings": juniDhcpv6LocalServerBindings,
       "juniDhcpv6LocalServerBindingsTable": juniDhcpv6LocalServerBindingsTable,
       "juniDhcpv6LocalServerBindingsEntry": juniDhcpv6LocalServerBindingsEntry,
       "juniDhcpv6LocalServerBindingsPrefix": juniDhcpv6LocalServerBindingsPrefix,
       "juniDhcpv6LocalServerBindingsLength": juniDhcpv6LocalServerBindingsLength,
       "juniDhcpv6LocalServerBindingsClientDuid": juniDhcpv6LocalServerBindingsClientDuid,
       "juniDhcpv6LocalServerBindingsInfinite": juniDhcpv6LocalServerBindingsInfinite,
       "juniDhcpv6LocalServerBindingsExpireTime": juniDhcpv6LocalServerBindingsExpireTime,
       "juniDhcpv6LocalServerBindingsIf": juniDhcpv6LocalServerBindingsIf,
       "juniDhcpv6MIBConformance": juniDhcpv6MIBConformance,
       "juniDhcpv6MIBCompliances": juniDhcpv6MIBCompliances,
       "juniDhcpv6Compliance2": juniDhcpv6Compliance2,
       "juniDhcpv6MIBGroups": juniDhcpv6MIBGroups,
       "juniDhcpv6LocalServerGroup": juniDhcpv6LocalServerGroup}
)
