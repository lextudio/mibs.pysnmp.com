# SNMP MIB module (ALTIGA-SEP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-SEP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:21 2024
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

(alSepMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alSepMibModule")

(alSepGroup,
 alStatsSep) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alSepGroup",
    "alStatsSep")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaSepStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 35, 2)
)
altigaSepStatsMibModule.setRevisions(
        ("2003-03-27 00:00",
         "2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaSepStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaSepStatsMibConformance = _AltigaSepStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 35, 2, 1)
)
_AltigaSepStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaSepStatsMibCompliances = _AltigaSepStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 35, 2, 1, 1)
)
_AlSepModuleStatsTable_Object = MibTable
alSepModuleStatsTable = _AlSepModuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2)
)
if mibBuilder.loadTexts:
    alSepModuleStatsTable.setStatus("current")
_AlSepModuleStatsEntry_Object = MibTableRow
alSepModuleStatsEntry = _AlSepModuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1)
)
alSepModuleStatsEntry.setIndexNames(
    (0, "ALTIGA-SEP-STATS-MIB", "alSepModuleStatsSlotNum"),
)
if mibBuilder.loadTexts:
    alSepModuleStatsEntry.setStatus("current")
_AlSepModuleStatsRowStatus_Type = RowStatus
_AlSepModuleStatsRowStatus_Object = MibTableColumn
alSepModuleStatsRowStatus = _AlSepModuleStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 1),
    _AlSepModuleStatsRowStatus_Type()
)
alSepModuleStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alSepModuleStatsRowStatus.setStatus("current")


class _AlSepModuleStatsSlotNum_Type(Integer32):
    """Custom type alSepModuleStatsSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AlSepModuleStatsSlotNum_Type.__name__ = "Integer32"
_AlSepModuleStatsSlotNum_Object = MibTableColumn
alSepModuleStatsSlotNum = _AlSepModuleStatsSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 2),
    _AlSepModuleStatsSlotNum_Type()
)
alSepModuleStatsSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alSepModuleStatsSlotNum.setStatus("current")


class _AlSepModuleStatsType_Type(Integer32):
    """Custom type alSepModuleStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bcm582x", 3),
          ("cryptIc", 2),
          ("cryptSet", 1))
    )


_AlSepModuleStatsType_Type.__name__ = "Integer32"
_AlSepModuleStatsType_Object = MibTableColumn
alSepModuleStatsType = _AlSepModuleStatsType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 3),
    _AlSepModuleStatsType_Type()
)
alSepModuleStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsType.setStatus("current")


class _AlSepModuleStatsState_Type(Integer32):
    """Custom type alSepModuleStatsState based on Integer32"""
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
        *(("sepDiagFailure", 3),
          ("sepDisabled", 8),
          ("sepFound", 2),
          ("sepInitializing", 6),
          ("sepLoading", 5),
          ("sepNotFound", 1),
          ("sepNotOperational", 4),
          ("sepOperational", 7))
    )


_AlSepModuleStatsState_Type.__name__ = "Integer32"
_AlSepModuleStatsState_Object = MibTableColumn
alSepModuleStatsState = _AlSepModuleStatsState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 4),
    _AlSepModuleStatsState_Type()
)
alSepModuleStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsState.setStatus("current")
_AlSepModuleStatsDspCodeVersion_Type = DisplayString
_AlSepModuleStatsDspCodeVersion_Object = MibTableColumn
alSepModuleStatsDspCodeVersion = _AlSepModuleStatsDspCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 5),
    _AlSepModuleStatsDspCodeVersion_Type()
)
alSepModuleStatsDspCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDspCodeVersion.setStatus("current")
_AlSepModuleStatsHashOutboundPackets_Type = Counter32
_AlSepModuleStatsHashOutboundPackets_Object = MibTableColumn
alSepModuleStatsHashOutboundPackets = _AlSepModuleStatsHashOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 6),
    _AlSepModuleStatsHashOutboundPackets_Type()
)
alSepModuleStatsHashOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsHashOutboundPackets.setStatus("current")
_AlSepModuleStatsHashOutboundOctets_Type = Counter32
_AlSepModuleStatsHashOutboundOctets_Object = MibTableColumn
alSepModuleStatsHashOutboundOctets = _AlSepModuleStatsHashOutboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 7),
    _AlSepModuleStatsHashOutboundOctets_Type()
)
alSepModuleStatsHashOutboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsHashOutboundOctets.setStatus("current")
_AlSepModuleStatsHashInboundPackets_Type = Counter32
_AlSepModuleStatsHashInboundPackets_Object = MibTableColumn
alSepModuleStatsHashInboundPackets = _AlSepModuleStatsHashInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 8),
    _AlSepModuleStatsHashInboundPackets_Type()
)
alSepModuleStatsHashInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsHashInboundPackets.setStatus("current")
_AlSepModuleStatsHashInboundOctets_Type = Counter32
_AlSepModuleStatsHashInboundOctets_Object = MibTableColumn
alSepModuleStatsHashInboundOctets = _AlSepModuleStatsHashInboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 9),
    _AlSepModuleStatsHashInboundOctets_Type()
)
alSepModuleStatsHashInboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsHashInboundOctets.setStatus("current")
_AlSepModuleStatsEncPackets_Type = Counter32
_AlSepModuleStatsEncPackets_Object = MibTableColumn
alSepModuleStatsEncPackets = _AlSepModuleStatsEncPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 10),
    _AlSepModuleStatsEncPackets_Type()
)
alSepModuleStatsEncPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsEncPackets.setStatus("current")
_AlSepModuleStatsEncOctets_Type = Counter32
_AlSepModuleStatsEncOctets_Object = MibTableColumn
alSepModuleStatsEncOctets = _AlSepModuleStatsEncOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 11),
    _AlSepModuleStatsEncOctets_Type()
)
alSepModuleStatsEncOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsEncOctets.setStatus("current")
_AlSepModuleStatsDecPackets_Type = Counter32
_AlSepModuleStatsDecPackets_Object = MibTableColumn
alSepModuleStatsDecPackets = _AlSepModuleStatsDecPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 12),
    _AlSepModuleStatsDecPackets_Type()
)
alSepModuleStatsDecPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDecPackets.setStatus("current")
_AlSepModuleStatsDecOctets_Type = Counter32
_AlSepModuleStatsDecOctets_Object = MibTableColumn
alSepModuleStatsDecOctets = _AlSepModuleStatsDecOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 13),
    _AlSepModuleStatsDecOctets_Type()
)
alSepModuleStatsDecOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDecOctets.setStatus("current")
_AlSepModuleStatsHashEncPackets_Type = Counter32
_AlSepModuleStatsHashEncPackets_Object = MibTableColumn
alSepModuleStatsHashEncPackets = _AlSepModuleStatsHashEncPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 14),
    _AlSepModuleStatsHashEncPackets_Type()
)
alSepModuleStatsHashEncPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsHashEncPackets.setStatus("current")
_AlSepModuleStatsHashDecPackets_Type = Counter32
_AlSepModuleStatsHashDecPackets_Object = MibTableColumn
alSepModuleStatsHashDecPackets = _AlSepModuleStatsHashDecPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 15),
    _AlSepModuleStatsHashDecPackets_Type()
)
alSepModuleStatsHashDecPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsHashDecPackets.setStatus("current")
_AlSepModuleStatsCryptoTransformsTotal_Type = Counter32
_AlSepModuleStatsCryptoTransformsTotal_Object = MibTableColumn
alSepModuleStatsCryptoTransformsTotal = _AlSepModuleStatsCryptoTransformsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 16),
    _AlSepModuleStatsCryptoTransformsTotal_Type()
)
alSepModuleStatsCryptoTransformsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsCryptoTransformsTotal.setStatus("current")
_AlSepModuleStatsPacketDrops_Type = Counter32
_AlSepModuleStatsPacketDrops_Object = MibTableColumn
alSepModuleStatsPacketDrops = _AlSepModuleStatsPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 17),
    _AlSepModuleStatsPacketDrops_Type()
)
alSepModuleStatsPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsPacketDrops.setStatus("current")
_AlSepModuleStatsRandRequests_Type = Counter32
_AlSepModuleStatsRandRequests_Object = MibTableColumn
alSepModuleStatsRandRequests = _AlSepModuleStatsRandRequests_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 18),
    _AlSepModuleStatsRandRequests_Type()
)
alSepModuleStatsRandRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRandRequests.setStatus("current")
_AlSepModuleStatsRandReplens_Type = Counter32
_AlSepModuleStatsRandReplens_Object = MibTableColumn
alSepModuleStatsRandReplens = _AlSepModuleStatsRandReplens_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 19),
    _AlSepModuleStatsRandReplens_Type()
)
alSepModuleStatsRandReplens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRandReplens.setStatus("current")
_AlSepModuleStatsRandBytesAvail_Type = Integer32
_AlSepModuleStatsRandBytesAvail_Object = MibTableColumn
alSepModuleStatsRandBytesAvail = _AlSepModuleStatsRandBytesAvail_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 20),
    _AlSepModuleStatsRandBytesAvail_Type()
)
alSepModuleStatsRandBytesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRandBytesAvail.setStatus("current")
_AlSepModuleStatsRandCacheEmpty_Type = Counter32
_AlSepModuleStatsRandCacheEmpty_Object = MibTableColumn
alSepModuleStatsRandCacheEmpty = _AlSepModuleStatsRandCacheEmpty_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 21),
    _AlSepModuleStatsRandCacheEmpty_Type()
)
alSepModuleStatsRandCacheEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRandCacheEmpty.setStatus("current")
_AlSepModuleStatsDHKeysGenerated_Type = Counter32
_AlSepModuleStatsDHKeysGenerated_Object = MibTableColumn
alSepModuleStatsDHKeysGenerated = _AlSepModuleStatsDHKeysGenerated_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 22),
    _AlSepModuleStatsDHKeysGenerated_Type()
)
alSepModuleStatsDHKeysGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDHKeysGenerated.setStatus("current")
_AlSepModuleStatsDHDerivedSecretKeys_Type = Counter32
_AlSepModuleStatsDHDerivedSecretKeys_Object = MibTableColumn
alSepModuleStatsDHDerivedSecretKeys = _AlSepModuleStatsDHDerivedSecretKeys_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 23),
    _AlSepModuleStatsDHDerivedSecretKeys_Type()
)
alSepModuleStatsDHDerivedSecretKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDHDerivedSecretKeys.setStatus("current")
_AlSepModuleStatsRSASignings_Type = Counter32
_AlSepModuleStatsRSASignings_Object = MibTableColumn
alSepModuleStatsRSASignings = _AlSepModuleStatsRSASignings_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 24),
    _AlSepModuleStatsRSASignings_Type()
)
alSepModuleStatsRSASignings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSASignings.setStatus("current")
_AlSepModuleStatsRSAVerifications_Type = Counter32
_AlSepModuleStatsRSAVerifications_Object = MibTableColumn
alSepModuleStatsRSAVerifications = _AlSepModuleStatsRSAVerifications_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 25),
    _AlSepModuleStatsRSAVerifications_Type()
)
alSepModuleStatsRSAVerifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSAVerifications.setStatus("current")
_AlSepModuleStatsRSAEncPackets_Type = Counter32
_AlSepModuleStatsRSAEncPackets_Object = MibTableColumn
alSepModuleStatsRSAEncPackets = _AlSepModuleStatsRSAEncPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 26),
    _AlSepModuleStatsRSAEncPackets_Type()
)
alSepModuleStatsRSAEncPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSAEncPackets.setStatus("current")
_AlSepModuleStatsRSAEncOctets_Type = Counter32
_AlSepModuleStatsRSAEncOctets_Object = MibTableColumn
alSepModuleStatsRSAEncOctets = _AlSepModuleStatsRSAEncOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 27),
    _AlSepModuleStatsRSAEncOctets_Type()
)
alSepModuleStatsRSAEncOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSAEncOctets.setStatus("current")
_AlSepModuleStatsRSADecPackets_Type = Counter32
_AlSepModuleStatsRSADecPackets_Object = MibTableColumn
alSepModuleStatsRSADecPackets = _AlSepModuleStatsRSADecPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 28),
    _AlSepModuleStatsRSADecPackets_Type()
)
alSepModuleStatsRSADecPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSADecPackets.setStatus("current")
_AlSepModuleStatsRSADecOctets_Type = Counter32
_AlSepModuleStatsRSADecOctets_Object = MibTableColumn
alSepModuleStatsRSADecOctets = _AlSepModuleStatsRSADecOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 29),
    _AlSepModuleStatsRSADecOctets_Type()
)
alSepModuleStatsRSADecOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSADecOctets.setStatus("current")
_AlSepModuleStatsDSAKeysGenerated_Type = Counter32
_AlSepModuleStatsDSAKeysGenerated_Object = MibTableColumn
alSepModuleStatsDSAKeysGenerated = _AlSepModuleStatsDSAKeysGenerated_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 30),
    _AlSepModuleStatsDSAKeysGenerated_Type()
)
alSepModuleStatsDSAKeysGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDSAKeysGenerated.setStatus("current")
_AlSepModuleStatsDSASignings_Type = Counter32
_AlSepModuleStatsDSASignings_Object = MibTableColumn
alSepModuleStatsDSASignings = _AlSepModuleStatsDSASignings_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 31),
    _AlSepModuleStatsDSASignings_Type()
)
alSepModuleStatsDSASignings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDSASignings.setStatus("current")
_AlSepModuleStatsDSAVerifications_Type = Counter32
_AlSepModuleStatsDSAVerifications_Object = MibTableColumn
alSepModuleStatsDSAVerifications = _AlSepModuleStatsDSAVerifications_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 32),
    _AlSepModuleStatsDSAVerifications_Type()
)
alSepModuleStatsDSAVerifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsDSAVerifications.setStatus("current")
_AlSepModuleStatsRSAKeysGenerated_Type = Counter32
_AlSepModuleStatsRSAKeysGenerated_Object = MibTableColumn
alSepModuleStatsRSAKeysGenerated = _AlSepModuleStatsRSAKeysGenerated_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 30, 2, 1, 33),
    _AlSepModuleStatsRSAKeysGenerated_Type()
)
alSepModuleStatsRSAKeysGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSepModuleStatsRSAKeysGenerated.setStatus("current")

# Managed Objects groups

altigaSepStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 30, 2)
)
altigaSepStatsGroup.setObjects(
      *(("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRowStatus"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsType"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsState"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDspCodeVersion"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsHashOutboundPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsHashOutboundOctets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsHashInboundPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsHashInboundOctets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsEncPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsEncOctets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDecPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDecOctets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsHashEncPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsHashDecPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsCryptoTransformsTotal"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsPacketDrops"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRandRequests"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRandReplens"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRandBytesAvail"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRandCacheEmpty"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDHKeysGenerated"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDHDerivedSecretKeys"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSASignings"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSAVerifications"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSAEncPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSAEncOctets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSADecPackets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSADecOctets"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDSAKeysGenerated"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDSASignings"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsDSAVerifications"),
        ("ALTIGA-SEP-STATS-MIB", "alSepModuleStatsRSAKeysGenerated"))
)
if mibBuilder.loadTexts:
    altigaSepStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaSepStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 35, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaSepStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-SEP-STATS-MIB",
    **{"altigaSepStatsMibModule": altigaSepStatsMibModule,
       "altigaSepStatsMibConformance": altigaSepStatsMibConformance,
       "altigaSepStatsMibCompliances": altigaSepStatsMibCompliances,
       "altigaSepStatsMibCompliance": altigaSepStatsMibCompliance,
       "altigaSepStatsGroup": altigaSepStatsGroup,
       "alSepModuleStatsTable": alSepModuleStatsTable,
       "alSepModuleStatsEntry": alSepModuleStatsEntry,
       "alSepModuleStatsRowStatus": alSepModuleStatsRowStatus,
       "alSepModuleStatsSlotNum": alSepModuleStatsSlotNum,
       "alSepModuleStatsType": alSepModuleStatsType,
       "alSepModuleStatsState": alSepModuleStatsState,
       "alSepModuleStatsDspCodeVersion": alSepModuleStatsDspCodeVersion,
       "alSepModuleStatsHashOutboundPackets": alSepModuleStatsHashOutboundPackets,
       "alSepModuleStatsHashOutboundOctets": alSepModuleStatsHashOutboundOctets,
       "alSepModuleStatsHashInboundPackets": alSepModuleStatsHashInboundPackets,
       "alSepModuleStatsHashInboundOctets": alSepModuleStatsHashInboundOctets,
       "alSepModuleStatsEncPackets": alSepModuleStatsEncPackets,
       "alSepModuleStatsEncOctets": alSepModuleStatsEncOctets,
       "alSepModuleStatsDecPackets": alSepModuleStatsDecPackets,
       "alSepModuleStatsDecOctets": alSepModuleStatsDecOctets,
       "alSepModuleStatsHashEncPackets": alSepModuleStatsHashEncPackets,
       "alSepModuleStatsHashDecPackets": alSepModuleStatsHashDecPackets,
       "alSepModuleStatsCryptoTransformsTotal": alSepModuleStatsCryptoTransformsTotal,
       "alSepModuleStatsPacketDrops": alSepModuleStatsPacketDrops,
       "alSepModuleStatsRandRequests": alSepModuleStatsRandRequests,
       "alSepModuleStatsRandReplens": alSepModuleStatsRandReplens,
       "alSepModuleStatsRandBytesAvail": alSepModuleStatsRandBytesAvail,
       "alSepModuleStatsRandCacheEmpty": alSepModuleStatsRandCacheEmpty,
       "alSepModuleStatsDHKeysGenerated": alSepModuleStatsDHKeysGenerated,
       "alSepModuleStatsDHDerivedSecretKeys": alSepModuleStatsDHDerivedSecretKeys,
       "alSepModuleStatsRSASignings": alSepModuleStatsRSASignings,
       "alSepModuleStatsRSAVerifications": alSepModuleStatsRSAVerifications,
       "alSepModuleStatsRSAEncPackets": alSepModuleStatsRSAEncPackets,
       "alSepModuleStatsRSAEncOctets": alSepModuleStatsRSAEncOctets,
       "alSepModuleStatsRSADecPackets": alSepModuleStatsRSADecPackets,
       "alSepModuleStatsRSADecOctets": alSepModuleStatsRSADecOctets,
       "alSepModuleStatsDSAKeysGenerated": alSepModuleStatsDSAKeysGenerated,
       "alSepModuleStatsDSASignings": alSepModuleStatsDSASignings,
       "alSepModuleStatsDSAVerifications": alSepModuleStatsDSAVerifications,
       "alSepModuleStatsRSAKeysGenerated": alSepModuleStatsRSAKeysGenerated}
)
