# SNMP MIB module (ALTIGA-NAT-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-NAT-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:17 2024
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

(alNatMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alNatMibModule")

(alNatGroup,
 alStatsNat) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alNatGroup",
    "alStatsNat")

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


# MODULE-IDENTITY

altigaNatStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 28, 2)
)
altigaNatStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaNatStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaNatStatsMibConformance = _AltigaNatStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 28, 2, 1)
)
_AltigaNatStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaNatStatsMibCompliances = _AltigaNatStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 28, 2, 1, 1)
)
_AlStatsNatGlobal_ObjectIdentity = ObjectIdentity
alStatsNatGlobal = _AlStatsNatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 1)
)
_AlNatStatsPacketsIn_Type = Counter32
_AlNatStatsPacketsIn_Object = MibScalar
alNatStatsPacketsIn = _AlNatStatsPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 1, 1),
    _AlNatStatsPacketsIn_Type()
)
alNatStatsPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatStatsPacketsIn.setStatus("current")
_AlNatStatsPacketsOut_Type = Counter32
_AlNatStatsPacketsOut_Object = MibScalar
alNatStatsPacketsOut = _AlNatStatsPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 1, 2),
    _AlNatStatsPacketsOut_Type()
)
alNatStatsPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatStatsPacketsOut.setStatus("current")
_AlNatStatsTotalTranslations_Type = Counter32
_AlNatStatsTotalTranslations_Object = MibScalar
alNatStatsTotalTranslations = _AlNatStatsTotalTranslations_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 1, 3),
    _AlNatStatsTotalTranslations_Type()
)
alNatStatsTotalTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatStatsTotalTranslations.setStatus("current")
_AlNatStatsActiveTranslations_Type = Counter32
_AlNatStatsActiveTranslations_Object = MibScalar
alNatStatsActiveTranslations = _AlNatStatsActiveTranslations_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 1, 4),
    _AlNatStatsActiveTranslations_Type()
)
alNatStatsActiveTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatStatsActiveTranslations.setStatus("current")
_AlNatStatsMaxTranslations_Type = Counter32
_AlNatStatsMaxTranslations_Object = MibScalar
alNatStatsMaxTranslations = _AlNatStatsMaxTranslations_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 1, 5),
    _AlNatStatsMaxTranslations_Type()
)
alNatStatsMaxTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatStatsMaxTranslations.setStatus("current")
_AlNatTranslationTable_Object = MibTable
alNatTranslationTable = _AlNatTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2)
)
if mibBuilder.loadTexts:
    alNatTranslationTable.setStatus("current")
_AlNatTranslationEntry_Object = MibTableRow
alNatTranslationEntry = _AlNatTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1)
)
alNatTranslationEntry.setIndexNames(
    (0, "ALTIGA-NAT-STATS-MIB", "alNatTranslationSrcAddress"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatTranslationSrcPort"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatTranslationDestAddress"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatTranslationDestPort"),
)
if mibBuilder.loadTexts:
    alNatTranslationEntry.setStatus("current")
_AlNatTranslationSrcAddress_Type = IpAddress
_AlNatTranslationSrcAddress_Object = MibTableColumn
alNatTranslationSrcAddress = _AlNatTranslationSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 1),
    _AlNatTranslationSrcAddress_Type()
)
alNatTranslationSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationSrcAddress.setStatus("current")


class _AlNatTranslationSrcPort_Type(Integer32):
    """Custom type alNatTranslationSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlNatTranslationSrcPort_Type.__name__ = "Integer32"
_AlNatTranslationSrcPort_Object = MibTableColumn
alNatTranslationSrcPort = _AlNatTranslationSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 2),
    _AlNatTranslationSrcPort_Type()
)
alNatTranslationSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationSrcPort.setStatus("current")
_AlNatTranslationDestAddress_Type = IpAddress
_AlNatTranslationDestAddress_Object = MibTableColumn
alNatTranslationDestAddress = _AlNatTranslationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 3),
    _AlNatTranslationDestAddress_Type()
)
alNatTranslationDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationDestAddress.setStatus("current")


class _AlNatTranslationDestPort_Type(Integer32):
    """Custom type alNatTranslationDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlNatTranslationDestPort_Type.__name__ = "Integer32"
_AlNatTranslationDestPort_Object = MibTableColumn
alNatTranslationDestPort = _AlNatTranslationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 4),
    _AlNatTranslationDestPort_Type()
)
alNatTranslationDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationDestPort.setStatus("current")
_AlNatTranslationAddress_Type = IpAddress
_AlNatTranslationAddress_Object = MibTableColumn
alNatTranslationAddress = _AlNatTranslationAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 5),
    _AlNatTranslationAddress_Type()
)
alNatTranslationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationAddress.setStatus("current")


class _AlNatTranslationPort_Type(Integer32):
    """Custom type alNatTranslationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlNatTranslationPort_Type.__name__ = "Integer32"
_AlNatTranslationPort_Object = MibTableColumn
alNatTranslationPort = _AlNatTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 6),
    _AlNatTranslationPort_Type()
)
alNatTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationPort.setStatus("current")
_AlNatTranslationAge_Type = Unsigned32
_AlNatTranslationAge_Object = MibTableColumn
alNatTranslationAge = _AlNatTranslationAge_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 7),
    _AlNatTranslationAge_Type()
)
alNatTranslationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationAge.setStatus("current")


class _AlNatTranslationType_Type(Integer32):
    """Custom type alNatTranslationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4095)
        )
    )
    namedValues = NamedValues(
        *(("all", 4095),
          ("ftpProxy", 8),
          ("h225TcpProxy", 256),
          ("h245Proxy", 512),
          ("ilsProxy", 2048),
          ("nbdgsvcProxy", 128),
          ("nbnsTcpProxy", 32),
          ("nbnsUdpProxy", 64),
          ("noPortMap", 4),
          ("portMapTcp", 1),
          ("portMapTcpUdp", 3),
          ("portMapUdp", 2),
          ("rasProxy", 1024),
          ("tftpProxy", 16),
          ("unknown", 0))
    )


_AlNatTranslationType_Type.__name__ = "Integer32"
_AlNatTranslationType_Object = MibTableColumn
alNatTranslationType = _AlNatTranslationType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 8),
    _AlNatTranslationType_Type()
)
alNatTranslationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationType.setStatus("current")


class _AlNatTranslationDirection_Type(Integer32):
    """Custom type alNatTranslationDirection based on Integer32"""
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


_AlNatTranslationDirection_Type.__name__ = "Integer32"
_AlNatTranslationDirection_Object = MibTableColumn
alNatTranslationDirection = _AlNatTranslationDirection_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 9),
    _AlNatTranslationDirection_Type()
)
alNatTranslationDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationDirection.setStatus("current")
_AlNatTranslationBytes_Type = Counter32
_AlNatTranslationBytes_Object = MibTableColumn
alNatTranslationBytes = _AlNatTranslationBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 10),
    _AlNatTranslationBytes_Type()
)
alNatTranslationBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationBytes.setStatus("current")
_AlNatTranslationPackets_Type = Counter32
_AlNatTranslationPackets_Object = MibTableColumn
alNatTranslationPackets = _AlNatTranslationPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 2, 1, 11),
    _AlNatTranslationPackets_Type()
)
alNatTranslationPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatTranslationPackets.setStatus("current")
_AlNatAllTranslationTable_Object = MibTable
alNatAllTranslationTable = _AlNatAllTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3)
)
if mibBuilder.loadTexts:
    alNatAllTranslationTable.setStatus("current")
_AlNatAllTranslationEntry_Object = MibTableRow
alNatAllTranslationEntry = _AlNatAllTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1)
)
alNatAllTranslationEntry.setIndexNames(
    (0, "ALTIGA-NAT-STATS-MIB", "alNatAllTranslationSrcAddress"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatAllTranslationSrcPort"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatAllTranslationDestAddress"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatAllTranslationDestPort"),
    (0, "ALTIGA-NAT-STATS-MIB", "alNatAllTranslationType"),
)
if mibBuilder.loadTexts:
    alNatAllTranslationEntry.setStatus("current")
_AlNatAllTranslationSrcAddress_Type = IpAddress
_AlNatAllTranslationSrcAddress_Object = MibTableColumn
alNatAllTranslationSrcAddress = _AlNatAllTranslationSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 1),
    _AlNatAllTranslationSrcAddress_Type()
)
alNatAllTranslationSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationSrcAddress.setStatus("current")


class _AlNatAllTranslationSrcPort_Type(Integer32):
    """Custom type alNatAllTranslationSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlNatAllTranslationSrcPort_Type.__name__ = "Integer32"
_AlNatAllTranslationSrcPort_Object = MibTableColumn
alNatAllTranslationSrcPort = _AlNatAllTranslationSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 2),
    _AlNatAllTranslationSrcPort_Type()
)
alNatAllTranslationSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationSrcPort.setStatus("current")
_AlNatAllTranslationDestAddress_Type = IpAddress
_AlNatAllTranslationDestAddress_Object = MibTableColumn
alNatAllTranslationDestAddress = _AlNatAllTranslationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 3),
    _AlNatAllTranslationDestAddress_Type()
)
alNatAllTranslationDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationDestAddress.setStatus("current")


class _AlNatAllTranslationDestPort_Type(Integer32):
    """Custom type alNatAllTranslationDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlNatAllTranslationDestPort_Type.__name__ = "Integer32"
_AlNatAllTranslationDestPort_Object = MibTableColumn
alNatAllTranslationDestPort = _AlNatAllTranslationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 4),
    _AlNatAllTranslationDestPort_Type()
)
alNatAllTranslationDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationDestPort.setStatus("current")
_AlNatAllTranslationAddress_Type = IpAddress
_AlNatAllTranslationAddress_Object = MibTableColumn
alNatAllTranslationAddress = _AlNatAllTranslationAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 5),
    _AlNatAllTranslationAddress_Type()
)
alNatAllTranslationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationAddress.setStatus("current")


class _AlNatAllTranslationPort_Type(Integer32):
    """Custom type alNatAllTranslationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlNatAllTranslationPort_Type.__name__ = "Integer32"
_AlNatAllTranslationPort_Object = MibTableColumn
alNatAllTranslationPort = _AlNatAllTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 6),
    _AlNatAllTranslationPort_Type()
)
alNatAllTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationPort.setStatus("current")
_AlNatAllTranslationAge_Type = Unsigned32
_AlNatAllTranslationAge_Object = MibTableColumn
alNatAllTranslationAge = _AlNatAllTranslationAge_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 7),
    _AlNatAllTranslationAge_Type()
)
alNatAllTranslationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationAge.setStatus("current")


class _AlNatAllTranslationType_Type(Integer32):
    """Custom type alNatAllTranslationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4095)
        )
    )
    namedValues = NamedValues(
        *(("all", 4095),
          ("ftpProxy", 8),
          ("h225TcpProxy", 256),
          ("h245Proxy", 512),
          ("ilsProxy", 2048),
          ("nbdgsvcProxy", 128),
          ("nbnsTcpProxy", 32),
          ("nbnsUdpProxy", 64),
          ("noPortMap", 4),
          ("portMapTcp", 1),
          ("portMapTcpUdp", 3),
          ("portMapUdp", 2),
          ("rasProxy", 1024),
          ("tftpProxy", 16),
          ("unknown", 0))
    )


_AlNatAllTranslationType_Type.__name__ = "Integer32"
_AlNatAllTranslationType_Object = MibTableColumn
alNatAllTranslationType = _AlNatAllTranslationType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 8),
    _AlNatAllTranslationType_Type()
)
alNatAllTranslationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationType.setStatus("current")


class _AlNatAllTranslationDirection_Type(Integer32):
    """Custom type alNatAllTranslationDirection based on Integer32"""
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


_AlNatAllTranslationDirection_Type.__name__ = "Integer32"
_AlNatAllTranslationDirection_Object = MibTableColumn
alNatAllTranslationDirection = _AlNatAllTranslationDirection_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 9),
    _AlNatAllTranslationDirection_Type()
)
alNatAllTranslationDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationDirection.setStatus("current")
_AlNatAllTranslationBytes_Type = Counter32
_AlNatAllTranslationBytes_Object = MibTableColumn
alNatAllTranslationBytes = _AlNatAllTranslationBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 10),
    _AlNatAllTranslationBytes_Type()
)
alNatAllTranslationBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationBytes.setStatus("current")
_AlNatAllTranslationPackets_Type = Counter32
_AlNatAllTranslationPackets_Object = MibTableColumn
alNatAllTranslationPackets = _AlNatAllTranslationPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 23, 3, 1, 11),
    _AlNatAllTranslationPackets_Type()
)
alNatAllTranslationPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNatAllTranslationPackets.setStatus("current")

# Managed Objects groups

altigaNatStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 23, 2)
)
altigaNatStatsGroup.setObjects(
      *(("ALTIGA-NAT-STATS-MIB", "alNatStatsPacketsIn"),
        ("ALTIGA-NAT-STATS-MIB", "alNatStatsPacketsOut"),
        ("ALTIGA-NAT-STATS-MIB", "alNatStatsTotalTranslations"),
        ("ALTIGA-NAT-STATS-MIB", "alNatStatsActiveTranslations"),
        ("ALTIGA-NAT-STATS-MIB", "alNatStatsMaxTranslations"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationSrcAddress"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationSrcPort"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationDestAddress"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationDestPort"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationAddress"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationPort"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationAge"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationType"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationDirection"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationBytes"),
        ("ALTIGA-NAT-STATS-MIB", "alNatTranslationPackets"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationSrcAddress"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationSrcPort"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationDestAddress"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationDestPort"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationAddress"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationPort"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationAge"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationType"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationDirection"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationBytes"),
        ("ALTIGA-NAT-STATS-MIB", "alNatAllTranslationPackets"))
)
if mibBuilder.loadTexts:
    altigaNatStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaNatStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 28, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaNatStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-NAT-STATS-MIB",
    **{"altigaNatStatsMibModule": altigaNatStatsMibModule,
       "altigaNatStatsMibConformance": altigaNatStatsMibConformance,
       "altigaNatStatsMibCompliances": altigaNatStatsMibCompliances,
       "altigaNatStatsMibCompliance": altigaNatStatsMibCompliance,
       "altigaNatStatsGroup": altigaNatStatsGroup,
       "alStatsNatGlobal": alStatsNatGlobal,
       "alNatStatsPacketsIn": alNatStatsPacketsIn,
       "alNatStatsPacketsOut": alNatStatsPacketsOut,
       "alNatStatsTotalTranslations": alNatStatsTotalTranslations,
       "alNatStatsActiveTranslations": alNatStatsActiveTranslations,
       "alNatStatsMaxTranslations": alNatStatsMaxTranslations,
       "alNatTranslationTable": alNatTranslationTable,
       "alNatTranslationEntry": alNatTranslationEntry,
       "alNatTranslationSrcAddress": alNatTranslationSrcAddress,
       "alNatTranslationSrcPort": alNatTranslationSrcPort,
       "alNatTranslationDestAddress": alNatTranslationDestAddress,
       "alNatTranslationDestPort": alNatTranslationDestPort,
       "alNatTranslationAddress": alNatTranslationAddress,
       "alNatTranslationPort": alNatTranslationPort,
       "alNatTranslationAge": alNatTranslationAge,
       "alNatTranslationType": alNatTranslationType,
       "alNatTranslationDirection": alNatTranslationDirection,
       "alNatTranslationBytes": alNatTranslationBytes,
       "alNatTranslationPackets": alNatTranslationPackets,
       "alNatAllTranslationTable": alNatAllTranslationTable,
       "alNatAllTranslationEntry": alNatAllTranslationEntry,
       "alNatAllTranslationSrcAddress": alNatAllTranslationSrcAddress,
       "alNatAllTranslationSrcPort": alNatAllTranslationSrcPort,
       "alNatAllTranslationDestAddress": alNatAllTranslationDestAddress,
       "alNatAllTranslationDestPort": alNatAllTranslationDestPort,
       "alNatAllTranslationAddress": alNatAllTranslationAddress,
       "alNatAllTranslationPort": alNatAllTranslationPort,
       "alNatAllTranslationAge": alNatAllTranslationAge,
       "alNatAllTranslationType": alNatAllTranslationType,
       "alNatAllTranslationDirection": alNatAllTranslationDirection,
       "alNatAllTranslationBytes": alNatAllTranslationBytes,
       "alNatAllTranslationPackets": alNatAllTranslationPackets}
)
