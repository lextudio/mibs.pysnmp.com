# SNMP MIB module (JUNIPER-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:27 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(jnxMplsLdpSesState,) = mibBuilder.importSymbols(
    "JUNIPER-MPLS-LDP-MIB",
    "jnxMplsLdpSesState")

(jnxLdpTraps,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxLdpTraps",
    "jnxMibs")

(MplsVpnName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnName")

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

jnxLdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14)
)
jnxLdp.setRevisions(
        ("2004-08-10 00:00",
         "2004-06-23 00:00",
         "2004-06-22 00:00",
         "2002-01-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLdpTrapVars_ObjectIdentity = ObjectIdentity
jnxLdpTrapVars = _JnxLdpTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1)
)
_JnxLdpLspFec_Type = IpAddress
_JnxLdpLspFec_Object = MibScalar
jnxLdpLspFec = _JnxLdpLspFec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 1),
    _JnxLdpLspFec_Type()
)
jnxLdpLspFec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpLspFec.setStatus("current")
_JnxLdpRtrid_Type = IpAddress
_JnxLdpRtrid_Object = MibScalar
jnxLdpRtrid = _JnxLdpRtrid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 2),
    _JnxLdpRtrid_Type()
)
jnxLdpRtrid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpRtrid.setStatus("current")


class _JnxLdpLspDownReason_Type(Integer32):
    """Custom type jnxLdpLspDownReason based on Integer32"""
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
        *(("bfdSessionDown", 5),
          ("filterChanged", 4),
          ("lspingDown", 7),
          ("neighborDown", 3),
          ("receivedWithdrawl", 2),
          ("topologyChanged", 1),
          ("unknown", 6))
    )


_JnxLdpLspDownReason_Type.__name__ = "Integer32"
_JnxLdpLspDownReason_Object = MibScalar
jnxLdpLspDownReason = _JnxLdpLspDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 3),
    _JnxLdpLspDownReason_Type()
)
jnxLdpLspDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpLspDownReason.setStatus("current")


class _JnxLdpSesDownReason_Type(Integer32):
    """Custom type jnxLdpSesDownReason based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("allAdjacenciesDown", 3),
          ("authenticationChanged", 10),
          ("badPDU", 5),
          ("badTLV", 4),
          ("cliCommand", 13),
          ("connectionError", 6),
          ("connectionExpired", 2),
          ("connectionReset", 7),
          ("gracefulRestartAbort", 12),
          ("gracefulRestartChanged", 14),
          ("holdExpired", 1),
          ("initError", 11),
          ("peerSentNotification", 8),
          ("unexpectedEOF", 9),
          ("unknown", 0))
    )


_JnxLdpSesDownReason_Type.__name__ = "Integer32"
_JnxLdpSesDownReason_Object = MibScalar
jnxLdpSesDownReason = _JnxLdpSesDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 4),
    _JnxLdpSesDownReason_Type()
)
jnxLdpSesDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpSesDownReason.setStatus("current")
_JnxLdpSesDownIf_Type = InterfaceIndexOrZero
_JnxLdpSesDownIf_Object = MibScalar
jnxLdpSesDownIf = _JnxLdpSesDownIf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 5),
    _JnxLdpSesDownIf_Type()
)
jnxLdpSesDownIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpSesDownIf.setStatus("current")


class _JnxLdpLspFecLen_Type(Integer32):
    """Custom type jnxLdpLspFecLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JnxLdpLspFecLen_Type.__name__ = "Integer32"
_JnxLdpLspFecLen_Object = MibScalar
jnxLdpLspFecLen = _JnxLdpLspFecLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 6),
    _JnxLdpLspFecLen_Type()
)
jnxLdpLspFecLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpLspFecLen.setStatus("current")
_JnxLdpSesUpIf_Type = InterfaceIndexOrZero
_JnxLdpSesUpIf_Object = MibScalar
jnxLdpSesUpIf = _JnxLdpSesUpIf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 7),
    _JnxLdpSesUpIf_Type()
)
jnxLdpSesUpIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpSesUpIf.setStatus("current")
_JnxLdpInstanceName_Type = MplsVpnName
_JnxLdpInstanceName_Object = MibScalar
jnxLdpInstanceName = _JnxLdpInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 1, 8),
    _JnxLdpInstanceName_Type()
)
jnxLdpInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxLdpInstanceName.setStatus("current")
_JnxLdpStatsTable_Object = MibTable
jnxLdpStatsTable = _JnxLdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2)
)
if mibBuilder.loadTexts:
    jnxLdpStatsTable.setStatus("current")
_JnxLdpStatsEntry_Object = MibTableRow
jnxLdpStatsEntry = _JnxLdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1)
)
jnxLdpStatsEntry.setIndexNames(
    (0, "JUNIPER-LDP-MIB", "jnxLdpInstanceId"),
    (0, "JUNIPER-LDP-MIB", "jnxLdpFecType"),
    (0, "JUNIPER-LDP-MIB", "jnxLdpFec"),
    (0, "JUNIPER-LDP-MIB", "jnxLdpFecLength"),
)
if mibBuilder.loadTexts:
    jnxLdpStatsEntry.setStatus("current")
_JnxLdpInstanceId_Type = Unsigned32
_JnxLdpInstanceId_Object = MibTableColumn
jnxLdpInstanceId = _JnxLdpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 1),
    _JnxLdpInstanceId_Type()
)
jnxLdpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLdpInstanceId.setStatus("current")
_JnxLdpFecType_Type = InetAddressType
_JnxLdpFecType_Object = MibTableColumn
jnxLdpFecType = _JnxLdpFecType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 2),
    _JnxLdpFecType_Type()
)
jnxLdpFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLdpFecType.setStatus("current")


class _JnxLdpFec_Type(InetAddress):
    """Custom type jnxLdpFec based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_JnxLdpFec_Type.__name__ = "InetAddress"
_JnxLdpFec_Object = MibTableColumn
jnxLdpFec = _JnxLdpFec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 3),
    _JnxLdpFec_Type()
)
jnxLdpFec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLdpFec.setStatus("current")


class _JnxLdpFecLength_Type(InetAddressPrefixLength):
    """Custom type jnxLdpFecLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JnxLdpFecLength_Type.__name__ = "InetAddressPrefixLength"
_JnxLdpFecLength_Object = MibTableColumn
jnxLdpFecLength = _JnxLdpFecLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 4),
    _JnxLdpFecLength_Type()
)
jnxLdpFecLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLdpFecLength.setStatus("current")


class _JnxLdpFecStatisticsStatus_Type(Integer32):
    """Custom type jnxLdpFecStatisticsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ok", 1),
          ("unavailable", 3))
    )


_JnxLdpFecStatisticsStatus_Type.__name__ = "Integer32"
_JnxLdpFecStatisticsStatus_Object = MibTableColumn
jnxLdpFecStatisticsStatus = _JnxLdpFecStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 5),
    _JnxLdpFecStatisticsStatus_Type()
)
jnxLdpFecStatisticsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLdpFecStatisticsStatus.setStatus("current")
_JnxLdpIngressOctets_Type = Counter64
_JnxLdpIngressOctets_Object = MibTableColumn
jnxLdpIngressOctets = _JnxLdpIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 6),
    _JnxLdpIngressOctets_Type()
)
jnxLdpIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLdpIngressOctets.setStatus("current")
_JnxLdpIngressPackets_Type = Counter64
_JnxLdpIngressPackets_Object = MibTableColumn
jnxLdpIngressPackets = _JnxLdpIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 7),
    _JnxLdpIngressPackets_Type()
)
jnxLdpIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLdpIngressPackets.setStatus("current")
_JnxLdpTransitOctets_Type = Counter64
_JnxLdpTransitOctets_Object = MibTableColumn
jnxLdpTransitOctets = _JnxLdpTransitOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 8),
    _JnxLdpTransitOctets_Type()
)
jnxLdpTransitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLdpTransitOctets.setStatus("current")
_JnxLdpTransitPackets_Type = Counter64
_JnxLdpTransitPackets_Object = MibTableColumn
jnxLdpTransitPackets = _JnxLdpTransitPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 14, 2, 1, 9),
    _JnxLdpTransitPackets_Type()
)
jnxLdpTransitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLdpTransitPackets.setStatus("current")
_JnxLdpTrapPrefix_ObjectIdentity = ObjectIdentity
jnxLdpTrapPrefix = _JnxLdpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4, 0)
)

# Managed Objects groups


# Notification objects

jnxLdpLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4, 0, 1)
)
jnxLdpLspUp.setObjects(
      *(("JUNIPER-LDP-MIB", "jnxLdpLspFec"),
        ("JUNIPER-LDP-MIB", "jnxLdpRtrid"),
        ("JUNIPER-LDP-MIB", "jnxLdpLspFecLen"),
        ("JUNIPER-LDP-MIB", "jnxLdpInstanceName"))
)
if mibBuilder.loadTexts:
    jnxLdpLspUp.setStatus(
        "current"
    )

jnxLdpLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4, 0, 2)
)
jnxLdpLspDown.setObjects(
      *(("JUNIPER-LDP-MIB", "jnxLdpLspFec"),
        ("JUNIPER-LDP-MIB", "jnxLdpRtrid"),
        ("JUNIPER-LDP-MIB", "jnxLdpLspDownReason"),
        ("JUNIPER-LDP-MIB", "jnxLdpLspFecLen"),
        ("JUNIPER-LDP-MIB", "jnxLdpInstanceName"))
)
if mibBuilder.loadTexts:
    jnxLdpLspDown.setStatus(
        "current"
    )

jnxLdpSesUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4, 0, 3)
)
jnxLdpSesUp.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesState"),
        ("JUNIPER-LDP-MIB", "jnxLdpSesUpIf"))
)
if mibBuilder.loadTexts:
    jnxLdpSesUp.setStatus(
        "current"
    )

jnxLdpSesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4, 0, 4)
)
jnxLdpSesDown.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesState"),
        ("JUNIPER-LDP-MIB", "jnxLdpSesDownReason"),
        ("JUNIPER-LDP-MIB", "jnxLdpSesDownIf"))
)
if mibBuilder.loadTexts:
    jnxLdpSesDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LDP-MIB",
    **{"jnxLdp": jnxLdp,
       "jnxLdpTrapVars": jnxLdpTrapVars,
       "jnxLdpLspFec": jnxLdpLspFec,
       "jnxLdpRtrid": jnxLdpRtrid,
       "jnxLdpLspDownReason": jnxLdpLspDownReason,
       "jnxLdpSesDownReason": jnxLdpSesDownReason,
       "jnxLdpSesDownIf": jnxLdpSesDownIf,
       "jnxLdpLspFecLen": jnxLdpLspFecLen,
       "jnxLdpSesUpIf": jnxLdpSesUpIf,
       "jnxLdpInstanceName": jnxLdpInstanceName,
       "jnxLdpStatsTable": jnxLdpStatsTable,
       "jnxLdpStatsEntry": jnxLdpStatsEntry,
       "jnxLdpInstanceId": jnxLdpInstanceId,
       "jnxLdpFecType": jnxLdpFecType,
       "jnxLdpFec": jnxLdpFec,
       "jnxLdpFecLength": jnxLdpFecLength,
       "jnxLdpFecStatisticsStatus": jnxLdpFecStatisticsStatus,
       "jnxLdpIngressOctets": jnxLdpIngressOctets,
       "jnxLdpIngressPackets": jnxLdpIngressPackets,
       "jnxLdpTransitOctets": jnxLdpTransitOctets,
       "jnxLdpTransitPackets": jnxLdpTransitPackets,
       "jnxLdpTrapPrefix": jnxLdpTrapPrefix,
       "jnxLdpLspUp": jnxLdpLspUp,
       "jnxLdpLspDown": jnxLdpLspDown,
       "jnxLdpSesUp": jnxLdpSesUp,
       "jnxLdpSesDown": jnxLdpSesDown}
)
