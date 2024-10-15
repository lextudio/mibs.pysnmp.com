# SNMP MIB module (ACC-IPSEC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-IPSEC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:25 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccIpsec_ObjectIdentity = ObjectIdentity
accIpsec = _AccIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81)
)
_AccIpsecConfig_ObjectIdentity = ObjectIdentity
accIpsecConfig = _AccIpsecConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 1)
)


class _AccIpsecConfigMessageLevel_Type(Integer32):
    """Custom type accIpsecConfigMessageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccIpsecConfigMessageLevel_Type.__name__ = "Integer32"
_AccIpsecConfigMessageLevel_Object = MibScalar
accIpsecConfigMessageLevel = _AccIpsecConfigMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 1, 1),
    _AccIpsecConfigMessageLevel_Type()
)
accIpsecConfigMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecConfigMessageLevel.setStatus("mandatory")
_AccIpsecConfigDebugMask_Type = Integer32
_AccIpsecConfigDebugMask_Object = MibScalar
accIpsecConfigDebugMask = _AccIpsecConfigDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 1, 2),
    _AccIpsecConfigDebugMask_Type()
)
accIpsecConfigDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecConfigDebugMask.setStatus("mandatory")
_AccIpsecConfigSANumber_Type = Integer32
_AccIpsecConfigSANumber_Object = MibScalar
accIpsecConfigSANumber = _AccIpsecConfigSANumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 1, 3),
    _AccIpsecConfigSANumber_Type()
)
accIpsecConfigSANumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecConfigSANumber.setStatus("mandatory")


class _AccIpsecConfigAuthenticationAllowed_Type(Integer32):
    """Custom type accIpsecConfigAuthenticationAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccIpsecConfigAuthenticationAllowed_Type.__name__ = "Integer32"
_AccIpsecConfigAuthenticationAllowed_Object = MibScalar
accIpsecConfigAuthenticationAllowed = _AccIpsecConfigAuthenticationAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 1, 4),
    _AccIpsecConfigAuthenticationAllowed_Type()
)
accIpsecConfigAuthenticationAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecConfigAuthenticationAllowed.setStatus("mandatory")
_AccIpsecConfigEncryptionKeyLength_Type = Integer32
_AccIpsecConfigEncryptionKeyLength_Object = MibScalar
accIpsecConfigEncryptionKeyLength = _AccIpsecConfigEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 1, 5),
    _AccIpsecConfigEncryptionKeyLength_Type()
)
accIpsecConfigEncryptionKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecConfigEncryptionKeyLength.setStatus("mandatory")
_AccIpsecStats_ObjectIdentity = ObjectIdentity
accIpsecStats = _AccIpsecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2)
)
_AccIpsecStatsInOkPackets_Type = Counter32
_AccIpsecStatsInOkPackets_Object = MibScalar
accIpsecStatsInOkPackets = _AccIpsecStatsInOkPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 1),
    _AccIpsecStatsInOkPackets_Type()
)
accIpsecStatsInOkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsInOkPackets.setStatus("mandatory")
_AccIpsecStatsOutOkPackets_Type = Counter32
_AccIpsecStatsOutOkPackets_Object = MibScalar
accIpsecStatsOutOkPackets = _AccIpsecStatsOutOkPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 2),
    _AccIpsecStatsOutOkPackets_Type()
)
accIpsecStatsOutOkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsOutOkPackets.setStatus("mandatory")
_AccIpsecStatsIllegalInSpis_Type = Counter32
_AccIpsecStatsIllegalInSpis_Object = MibScalar
accIpsecStatsIllegalInSpis = _AccIpsecStatsIllegalInSpis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 3),
    _AccIpsecStatsIllegalInSpis_Type()
)
accIpsecStatsIllegalInSpis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsIllegalInSpis.setStatus("mandatory")
_AccIpsecStatsIllegalProtos_Type = Counter32
_AccIpsecStatsIllegalProtos_Object = MibScalar
accIpsecStatsIllegalProtos = _AccIpsecStatsIllegalProtos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 4),
    _AccIpsecStatsIllegalProtos_Type()
)
accIpsecStatsIllegalProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsIllegalProtos.setStatus("mandatory")
_AccIpsecStatsUnsuppAHLens_Type = Counter32
_AccIpsecStatsUnsuppAHLens_Object = MibScalar
accIpsecStatsUnsuppAHLens = _AccIpsecStatsUnsuppAHLens_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 5),
    _AccIpsecStatsUnsuppAHLens_Type()
)
accIpsecStatsUnsuppAHLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsUnsuppAHLens.setStatus("mandatory")
_AccIpsecStatsUnsuppOpts_Type = Counter32
_AccIpsecStatsUnsuppOpts_Object = MibScalar
accIpsecStatsUnsuppOpts = _AccIpsecStatsUnsuppOpts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 6),
    _AccIpsecStatsUnsuppOpts_Type()
)
accIpsecStatsUnsuppOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsUnsuppOpts.setStatus("mandatory")
_AccIpsecStatsPacketTooSmalls_Type = Counter32
_AccIpsecStatsPacketTooSmalls_Object = MibScalar
accIpsecStatsPacketTooSmalls = _AccIpsecStatsPacketTooSmalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 7),
    _AccIpsecStatsPacketTooSmalls_Type()
)
accIpsecStatsPacketTooSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsPacketTooSmalls.setStatus("mandatory")
_AccIpsecStatsMalformedOpts_Type = Counter32
_AccIpsecStatsMalformedOpts_Object = MibScalar
accIpsecStatsMalformedOpts = _AccIpsecStatsMalformedOpts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 8),
    _AccIpsecStatsMalformedOpts_Type()
)
accIpsecStatsMalformedOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsMalformedOpts.setStatus("mandatory")
_AccIpsecStatsUnsuppIPVersions_Type = Counter32
_AccIpsecStatsUnsuppIPVersions_Object = MibScalar
accIpsecStatsUnsuppIPVersions = _AccIpsecStatsUnsuppIPVersions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 9),
    _AccIpsecStatsUnsuppIPVersions_Type()
)
accIpsecStatsUnsuppIPVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsUnsuppIPVersions.setStatus("mandatory")
_AccIpsecStatsNoRoutes_Type = Counter32
_AccIpsecStatsNoRoutes_Object = MibScalar
accIpsecStatsNoRoutes = _AccIpsecStatsNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 10),
    _AccIpsecStatsNoRoutes_Type()
)
accIpsecStatsNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsNoRoutes.setStatus("mandatory")
_AccIpsecStatsMissingGWs_Type = Counter32
_AccIpsecStatsMissingGWs_Object = MibScalar
accIpsecStatsMissingGWs = _AccIpsecStatsMissingGWs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 11),
    _AccIpsecStatsMissingGWs_Type()
)
accIpsecStatsMissingGWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsMissingGWs.setStatus("mandatory")
_AccIpsecStatsSha1Mismatches_Type = Counter32
_AccIpsecStatsSha1Mismatches_Object = MibScalar
accIpsecStatsSha1Mismatches = _AccIpsecStatsSha1Mismatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 12),
    _AccIpsecStatsSha1Mismatches_Type()
)
accIpsecStatsSha1Mismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsSha1Mismatches.setStatus("mandatory")
_AccIpsecStatsMd5Mistmatches_Type = Counter32
_AccIpsecStatsMd5Mistmatches_Object = MibScalar
accIpsecStatsMd5Mistmatches = _AccIpsecStatsMd5Mistmatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 13),
    _AccIpsecStatsMd5Mistmatches_Type()
)
accIpsecStatsMd5Mistmatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsMd5Mistmatches.setStatus("mandatory")
_AccIpsecStatsReplayCheckFaileds_Type = Counter32
_AccIpsecStatsReplayCheckFaileds_Object = MibScalar
accIpsecStatsReplayCheckFaileds = _AccIpsecStatsReplayCheckFaileds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 14),
    _AccIpsecStatsReplayCheckFaileds_Type()
)
accIpsecStatsReplayCheckFaileds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsReplayCheckFaileds.setStatus("mandatory")
_AccIpsecStatsIllegalPads_Type = Counter32
_AccIpsecStatsIllegalPads_Object = MibScalar
accIpsecStatsIllegalPads = _AccIpsecStatsIllegalPads_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 15),
    _AccIpsecStatsIllegalPads_Type()
)
accIpsecStatsIllegalPads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsIllegalPads.setStatus("mandatory")
_AccIpsecStatsSeqnoCycles_Type = Counter32
_AccIpsecStatsSeqnoCycles_Object = MibScalar
accIpsecStatsSeqnoCycles = _AccIpsecStatsSeqnoCycles_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 16),
    _AccIpsecStatsSeqnoCycles_Type()
)
accIpsecStatsSeqnoCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsSeqnoCycles.setStatus("mandatory")
_AccIpsecStatsInsufficientPads_Type = Counter32
_AccIpsecStatsInsufficientPads_Object = MibScalar
accIpsecStatsInsufficientPads = _AccIpsecStatsInsufficientPads_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 17),
    _AccIpsecStatsInsufficientPads_Type()
)
accIpsecStatsInsufficientPads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsInsufficientPads.setStatus("mandatory")
_AccIpsecStatsTtlZeros_Type = Counter32
_AccIpsecStatsTtlZeros_Object = MibScalar
accIpsecStatsTtlZeros = _AccIpsecStatsTtlZeros_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 18),
    _AccIpsecStatsTtlZeros_Type()
)
accIpsecStatsTtlZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsTtlZeros.setStatus("mandatory")
_AccIpsecStatsNoKeys_Type = Counter32
_AccIpsecStatsNoKeys_Object = MibScalar
accIpsecStatsNoKeys = _AccIpsecStatsNoKeys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 19),
    _AccIpsecStatsNoKeys_Type()
)
accIpsecStatsNoKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsNoKeys.setStatus("mandatory")
_AccIpsecStatsIllegalFragments_Type = Counter32
_AccIpsecStatsIllegalFragments_Object = MibScalar
accIpsecStatsIllegalFragments = _AccIpsecStatsIllegalFragments_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 20),
    _AccIpsecStatsIllegalFragments_Type()
)
accIpsecStatsIllegalFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsIllegalFragments.setStatus("mandatory")
_AccIpsecStatsCpuOverloads_Type = Counter32
_AccIpsecStatsCpuOverloads_Object = MibScalar
accIpsecStatsCpuOverloads = _AccIpsecStatsCpuOverloads_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 21),
    _AccIpsecStatsCpuOverloads_Type()
)
accIpsecStatsCpuOverloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsCpuOverloads.setStatus("mandatory")
_AccIpsecStatsHdrAllocs_Type = Counter32
_AccIpsecStatsHdrAllocs_Object = MibScalar
accIpsecStatsHdrAllocs = _AccIpsecStatsHdrAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 22),
    _AccIpsecStatsHdrAllocs_Type()
)
accIpsecStatsHdrAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsHdrAllocs.setStatus("mandatory")
_AccIpsecStatsTlrAllocs_Type = Counter32
_AccIpsecStatsTlrAllocs_Object = MibScalar
accIpsecStatsTlrAllocs = _AccIpsecStatsTlrAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 23),
    _AccIpsecStatsTlrAllocs_Type()
)
accIpsecStatsTlrAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsTlrAllocs.setStatus("mandatory")
_AccIpsecStatsBlockJoins_Type = Counter32
_AccIpsecStatsBlockJoins_Object = MibScalar
accIpsecStatsBlockJoins = _AccIpsecStatsBlockJoins_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 2, 24),
    _AccIpsecStatsBlockJoins_Type()
)
accIpsecStatsBlockJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecStatsBlockJoins.setStatus("mandatory")
_AccIpsecSAConfig_ObjectIdentity = ObjectIdentity
accIpsecSAConfig = _AccIpsecSAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3)
)
_AccIpsecSAConfigTable_Object = MibTable
accIpsecSAConfigTable = _AccIpsecSAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1)
)
if mibBuilder.loadTexts:
    accIpsecSAConfigTable.setStatus("mandatory")
_AccIpsecSAConfigEntry_Object = MibTableRow
accIpsecSAConfigEntry = _AccIpsecSAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1)
)
accIpsecSAConfigEntry.setIndexNames(
    (0, "ACC-IPSEC", "accIpsecSAConfigIndex"),
)
if mibBuilder.loadTexts:
    accIpsecSAConfigEntry.setStatus("mandatory")
_AccIpsecSAConfigIndex_Type = OctetString
_AccIpsecSAConfigIndex_Object = MibTableColumn
accIpsecSAConfigIndex = _AccIpsecSAConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 1),
    _AccIpsecSAConfigIndex_Type()
)
accIpsecSAConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigIndex.setStatus("mandatory")


class _AccIpsecSAConfigDir_Type(Integer32):
    """Custom type accIpsecSAConfigDir based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AccIpsecSAConfigDir_Type.__name__ = "Integer32"
_AccIpsecSAConfigDir_Object = MibTableColumn
accIpsecSAConfigDir = _AccIpsecSAConfigDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 2),
    _AccIpsecSAConfigDir_Type()
)
accIpsecSAConfigDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigDir.setStatus("mandatory")


class _AccIpsecSAConfigMode_Type(Integer32):
    """Custom type accIpsecSAConfigMode based on Integer32"""
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
        *(("transport", 1),
          ("tunnel", 2),
          ("wildcard", 3))
    )


_AccIpsecSAConfigMode_Type.__name__ = "Integer32"
_AccIpsecSAConfigMode_Object = MibTableColumn
accIpsecSAConfigMode = _AccIpsecSAConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 3),
    _AccIpsecSAConfigMode_Type()
)
accIpsecSAConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigMode.setStatus("mandatory")


class _AccIpsecSAConfigProtocol_Type(Integer32):
    """Custom type accIpsecSAConfigProtocol based on Integer32"""
    defaultValue = 51

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("esp", 50))
    )


_AccIpsecSAConfigProtocol_Type.__name__ = "Integer32"
_AccIpsecSAConfigProtocol_Object = MibTableColumn
accIpsecSAConfigProtocol = _AccIpsecSAConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 4),
    _AccIpsecSAConfigProtocol_Type()
)
accIpsecSAConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigProtocol.setStatus("mandatory")


class _AccIpsecSAConfigSPI_Type(Integer32):
    """Custom type accIpsecSAConfigSPI based on Integer32"""
    defaultValue = 0


_AccIpsecSAConfigSPI_Object = MibTableColumn
accIpsecSAConfigSPI = _AccIpsecSAConfigSPI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 5),
    _AccIpsecSAConfigSPI_Type()
)
accIpsecSAConfigSPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigSPI.setStatus("mandatory")


class _AccIpsecSAConfigAuthAlgorithm_Type(Integer32):
    """Custom type accIpsecSAConfigAuthAlgorithm based on Integer32"""
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
        *(("hmac-md5", 2),
          ("hmac-sha1", 1),
          ("null", 3))
    )


_AccIpsecSAConfigAuthAlgorithm_Type.__name__ = "Integer32"
_AccIpsecSAConfigAuthAlgorithm_Object = MibTableColumn
accIpsecSAConfigAuthAlgorithm = _AccIpsecSAConfigAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 6),
    _AccIpsecSAConfigAuthAlgorithm_Type()
)
accIpsecSAConfigAuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigAuthAlgorithm.setStatus("mandatory")


class _AccIpsecSAConfigReplayCheck_Type(Integer32):
    """Custom type accIpsecSAConfigReplayCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccIpsecSAConfigReplayCheck_Type.__name__ = "Integer32"
_AccIpsecSAConfigReplayCheck_Object = MibTableColumn
accIpsecSAConfigReplayCheck = _AccIpsecSAConfigReplayCheck_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 7),
    _AccIpsecSAConfigReplayCheck_Type()
)
accIpsecSAConfigReplayCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigReplayCheck.setStatus("mandatory")


class _AccIpsecSAConfigOverflowAudit_Type(Integer32):
    """Custom type accIpsecSAConfigOverflowAudit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccIpsecSAConfigOverflowAudit_Type.__name__ = "Integer32"
_AccIpsecSAConfigOverflowAudit_Object = MibTableColumn
accIpsecSAConfigOverflowAudit = _AccIpsecSAConfigOverflowAudit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 8),
    _AccIpsecSAConfigOverflowAudit_Type()
)
accIpsecSAConfigOverflowAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigOverflowAudit.setStatus("mandatory")


class _AccIpsecSAConfigCopyDF_Type(Integer32):
    """Custom type accIpsecSAConfigCopyDF based on Integer32"""
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
        *(("copy", 3),
          ("reset", 1),
          ("set", 2))
    )


_AccIpsecSAConfigCopyDF_Type.__name__ = "Integer32"
_AccIpsecSAConfigCopyDF_Object = MibTableColumn
accIpsecSAConfigCopyDF = _AccIpsecSAConfigCopyDF_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 9),
    _AccIpsecSAConfigCopyDF_Type()
)
accIpsecSAConfigCopyDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigCopyDF.setStatus("mandatory")
_AccIpsecSAConfigDestAddr_Type = IpAddress
_AccIpsecSAConfigDestAddr_Object = MibTableColumn
accIpsecSAConfigDestAddr = _AccIpsecSAConfigDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 10),
    _AccIpsecSAConfigDestAddr_Type()
)
accIpsecSAConfigDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigDestAddr.setStatus("mandatory")
_AccIpsecSAConfigSharedAuthSecret_Type = OctetString
_AccIpsecSAConfigSharedAuthSecret_Object = MibTableColumn
accIpsecSAConfigSharedAuthSecret = _AccIpsecSAConfigSharedAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 11),
    _AccIpsecSAConfigSharedAuthSecret_Type()
)
accIpsecSAConfigSharedAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigSharedAuthSecret.setStatus("mandatory")


class _AccIpsecSAConfigEncrAlgorithm_Type(Integer32):
    """Custom type accIpsecSAConfigEncrAlgorithm based on Integer32"""
    defaultValue = 1

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
        *(("blowfish", 4),
          ("cast", 3),
          ("des", 5),
          ("des3", 6),
          ("none", 1),
          ("null", 2))
    )


_AccIpsecSAConfigEncrAlgorithm_Type.__name__ = "Integer32"
_AccIpsecSAConfigEncrAlgorithm_Object = MibTableColumn
accIpsecSAConfigEncrAlgorithm = _AccIpsecSAConfigEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 12),
    _AccIpsecSAConfigEncrAlgorithm_Type()
)
accIpsecSAConfigEncrAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigEncrAlgorithm.setStatus("mandatory")
_AccIpsecSAConfigSharedEncrSecret_Type = OctetString
_AccIpsecSAConfigSharedEncrSecret_Object = MibTableColumn
accIpsecSAConfigSharedEncrSecret = _AccIpsecSAConfigSharedEncrSecret_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 13),
    _AccIpsecSAConfigSharedEncrSecret_Type()
)
accIpsecSAConfigSharedEncrSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigSharedEncrSecret.setStatus("mandatory")


class _AccIpsecSAConfigPriority_Type(Integer32):
    """Custom type accIpsecSAConfigPriority based on Integer32"""
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
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_AccIpsecSAConfigPriority_Type.__name__ = "Integer32"
_AccIpsecSAConfigPriority_Object = MibTableColumn
accIpsecSAConfigPriority = _AccIpsecSAConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 14),
    _AccIpsecSAConfigPriority_Type()
)
accIpsecSAConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigPriority.setStatus("mandatory")


class _AccIpsecSAConfigSequenceNumber_Type(Integer32):
    """Custom type accIpsecSAConfigSequenceNumber based on Integer32"""
    defaultValue = 1


_AccIpsecSAConfigSequenceNumber_Object = MibTableColumn
accIpsecSAConfigSequenceNumber = _AccIpsecSAConfigSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 15),
    _AccIpsecSAConfigSequenceNumber_Type()
)
accIpsecSAConfigSequenceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigSequenceNumber.setStatus("mandatory")
_AccIpsecSAConfigStatus_Type = RowStatus
_AccIpsecSAConfigStatus_Object = MibTableColumn
accIpsecSAConfigStatus = _AccIpsecSAConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 3, 1, 1, 16),
    _AccIpsecSAConfigStatus_Type()
)
accIpsecSAConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAConfigStatus.setStatus("mandatory")
_AccIpsecSAStats_ObjectIdentity = ObjectIdentity
accIpsecSAStats = _AccIpsecSAStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4)
)
_AccIpsecSAStatsTable_Object = MibTable
accIpsecSAStatsTable = _AccIpsecSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1)
)
if mibBuilder.loadTexts:
    accIpsecSAStatsTable.setStatus("mandatory")
_AccIpsecSAStatsEntry_Object = MibTableRow
accIpsecSAStatsEntry = _AccIpsecSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1, 1)
)
accIpsecSAStatsEntry.setIndexNames(
    (0, "ACC-IPSEC", "accIpsecSAStatsIndex"),
)
if mibBuilder.loadTexts:
    accIpsecSAStatsEntry.setStatus("mandatory")
_AccIpsecSAStatsIndex_Type = OctetString
_AccIpsecSAStatsIndex_Object = MibTableColumn
accIpsecSAStatsIndex = _AccIpsecSAStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1, 1, 1),
    _AccIpsecSAStatsIndex_Type()
)
accIpsecSAStatsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpsecSAStatsIndex.setStatus("mandatory")
_AccIpsecSAStatsOKPackets_Type = Counter32
_AccIpsecSAStatsOKPackets_Object = MibTableColumn
accIpsecSAStatsOKPackets = _AccIpsecSAStatsOKPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1, 1, 2),
    _AccIpsecSAStatsOKPackets_Type()
)
accIpsecSAStatsOKPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecSAStatsOKPackets.setStatus("mandatory")
_AccIpsecSAStatsNotOKPackets_Type = Counter32
_AccIpsecSAStatsNotOKPackets_Object = MibTableColumn
accIpsecSAStatsNotOKPackets = _AccIpsecSAStatsNotOKPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1, 1, 3),
    _AccIpsecSAStatsNotOKPackets_Type()
)
accIpsecSAStatsNotOKPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecSAStatsNotOKPackets.setStatus("mandatory")
_AccIpsecSAStatsCurrTicks_Type = TimeTicks
_AccIpsecSAStatsCurrTicks_Object = MibTableColumn
accIpsecSAStatsCurrTicks = _AccIpsecSAStatsCurrTicks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1, 1, 4),
    _AccIpsecSAStatsCurrTicks_Type()
)
accIpsecSAStatsCurrTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecSAStatsCurrTicks.setStatus("mandatory")
_AccIpsecSAStatsCurrBytes_Type = Counter32
_AccIpsecSAStatsCurrBytes_Object = MibTableColumn
accIpsecSAStatsCurrBytes = _AccIpsecSAStatsCurrBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 4, 1, 1, 5),
    _AccIpsecSAStatsCurrBytes_Type()
)
accIpsecSAStatsCurrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecSAStatsCurrBytes.setStatus("mandatory")
_AccIpsecTraps_ObjectIdentity = ObjectIdentity
accIpsecTraps = _AccIpsecTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5)
)
_AccIpsecTrapMsg_Type = DisplayString
_AccIpsecTrapMsg_Object = MibScalar
accIpsecTrapMsg = _AccIpsecTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 1),
    _AccIpsecTrapMsg_Type()
)
accIpsecTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpsecTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accIpSecsameSAIndxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 1)
)
accIpSecsameSAIndxTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsameSAIndxTrap.setStatus(
        ""
    )

accIpSecbadSAIndxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 2)
)
accIpSecbadSAIndxTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecbadSAIndxTrap.setStatus(
        ""
    )

accIpSecexpKeyFldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 3)
)
accIpSecexpKeyFldTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecexpKeyFldTrap.setStatus(
        ""
    )

accIpSecmsgSpiZeroTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 4)
)
accIpSecmsgSpiZeroTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigSPI"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecmsgSpiZeroTrap.setStatus(
        ""
    )

accIpSecauthencAlgoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 5)
)
accIpSecauthencAlgoTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigAuthAlgorithm"),
        ("ACC-IPSEC", "accIpsecSAConfigEncrAlgorithm"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecauthencAlgoTrap.setStatus(
        ""
    )

accIpSeccwauthAhAlgoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 6)
)
accIpSeccwauthAhAlgoTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigAuthAlgorithm"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSeccwauthAhAlgoTrap.setStatus(
        ""
    )

accIpSecmsgOflowOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 7)
)
accIpSecmsgOflowOutTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecmsgOflowOutTrap.setStatus(
        ""
    )

accIpSecdfTunnSATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 8)
)
accIpSecdfTunnSATrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigCopyDF"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecdfTunnSATrap.setStatus(
        ""
    )

accIpSecdfNotSuppTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 9)
)
accIpSecdfNotSuppTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigCopyDF"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecdfNotSuppTrap.setStatus(
        ""
    )

accIpSecunsuppAlgoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 10)
)
accIpSecunsuppAlgoTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigEncrAlgorithm"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecunsuppAlgoTrap.setStatus(
        ""
    )

accIpSecencAlgESPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 11)
)
accIpSecencAlgESPTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigEncrAlgorithm"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecencAlgESPTrap.setStatus(
        ""
    )

accIpSecvldIPAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 12)
)
accIpSecvldIPAddrTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigDestAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecvldIPAddrTrap.setStatus(
        ""
    )

accIpSecipAddrSAInTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 13)
)
accIpSecipAddrSAInTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigDestAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecipAddrSAInTrap.setStatus(
        ""
    )

accIpSecpeerGateAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 14)
)
accIpSecpeerGateAddrTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigDestAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecpeerGateAddrTrap.setStatus(
        ""
    )

accIpSeckeyLenZeroTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 15)
)
accIpSeckeyLenZeroTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigAuthAlgorithm"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSeckeyLenZeroTrap.setStatus(
        ""
    )

accIpSecencKeyLenZeroTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 16)
)
accIpSecencKeyLenZeroTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigEncrAlgorithm"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecencKeyLenZeroTrap.setStatus(
        ""
    )

accIpSecseqZeroTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 17)
)
accIpSecseqZeroTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-IPSEC", "accIpsecSAConfigSequenceNumber"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecseqZeroTrap.setStatus(
        ""
    )

accIpSecallocBytsFaildTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 18)
)
accIpSecallocBytsFaildTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecallocBytsFaildTrap.setStatus(
        ""
    )

accIpSecnoSpcSATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 19)
)
accIpSecnoSpcSATrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecnoSpcSATrap.setStatus(
        ""
    )

accIpSecsaNameLenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 20)
)
accIpSecsaNameLenTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsaNameLenTrap.setStatus(
        ""
    )

accIpSecauthKeyMaxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 21)
)
accIpSecauthKeyMaxTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecauthKeyMaxTrap.setStatus(
        ""
    )

accIpSechmacMD5KeyLenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 22)
)
accIpSechmacMD5KeyLenTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSechmacMD5KeyLenTrap.setStatus(
        ""
    )

accIpSechmacSha1KeyLenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 23)
)
accIpSechmacSha1KeyLenTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSechmacSha1KeyLenTrap.setStatus(
        ""
    )

accIpSecencMaxKeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 24)
)
accIpSecencMaxKeyTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecencMaxKeyTrap.setStatus(
        ""
    )

accIpSecencKeyLenMaxPhyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 25)
)
accIpSecencKeyLenMaxPhyTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecencKeyLenMaxPhyTrap.setStatus(
        ""
    )

accIpSecdesKeyLen8OctTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 26)
)
accIpSecdesKeyLen8OctTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecdesKeyLen8OctTrap.setStatus(
        ""
    )

accIpSec3desKeyLenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 27)
)
accIpSec3desKeyLenTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSec3desKeyLenTrap.setStatus(
        ""
    )

accIpSeccastKeyLenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 28)
)
accIpSeccastKeyLenTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSeccastKeyLenTrap.setStatus(
        ""
    )

accIpSecblowKeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 29)
)
accIpSecblowKeyTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecblowKeyTrap.setStatus(
        ""
    )

accIpSecsaAreaSzTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 30)
)
accIpSecsaAreaSzTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsaAreaSzTrap.setStatus(
        ""
    )

accIpSecsameSPIAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 31)
)
accIpSecsameSPIAddrTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsameSPIAddrTrap.setStatus(
        ""
    )

accIpSecnotHexDigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 32)
)
accIpSecnotHexDigTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecnotHexDigTrap.setStatus(
        ""
    )

accIpSecsecOddDigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 33)
)
accIpSecsecOddDigTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsecOddDigTrap.setStatus(
        ""
    )

accIpSecnoSANameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 34)
)
accIpSecnoSANameTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecnoSANameTrap.setStatus(
        ""
    )

accIpSecsaInptFiltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 35)
)
accIpSecsaInptFiltTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsaInptFiltTrap.setStatus(
        ""
    )

accIpSecsaOtptFiltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 81, 5, 0, 36)
)
accIpSecsaOtptFiltTrap.setObjects(
      *(("ACC-IPSEC", "accIpsecTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIpSecsaOtptFiltTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-IPSEC",
    **{"accIpsec": accIpsec,
       "accIpsecConfig": accIpsecConfig,
       "accIpsecConfigMessageLevel": accIpsecConfigMessageLevel,
       "accIpsecConfigDebugMask": accIpsecConfigDebugMask,
       "accIpsecConfigSANumber": accIpsecConfigSANumber,
       "accIpsecConfigAuthenticationAllowed": accIpsecConfigAuthenticationAllowed,
       "accIpsecConfigEncryptionKeyLength": accIpsecConfigEncryptionKeyLength,
       "accIpsecStats": accIpsecStats,
       "accIpsecStatsInOkPackets": accIpsecStatsInOkPackets,
       "accIpsecStatsOutOkPackets": accIpsecStatsOutOkPackets,
       "accIpsecStatsIllegalInSpis": accIpsecStatsIllegalInSpis,
       "accIpsecStatsIllegalProtos": accIpsecStatsIllegalProtos,
       "accIpsecStatsUnsuppAHLens": accIpsecStatsUnsuppAHLens,
       "accIpsecStatsUnsuppOpts": accIpsecStatsUnsuppOpts,
       "accIpsecStatsPacketTooSmalls": accIpsecStatsPacketTooSmalls,
       "accIpsecStatsMalformedOpts": accIpsecStatsMalformedOpts,
       "accIpsecStatsUnsuppIPVersions": accIpsecStatsUnsuppIPVersions,
       "accIpsecStatsNoRoutes": accIpsecStatsNoRoutes,
       "accIpsecStatsMissingGWs": accIpsecStatsMissingGWs,
       "accIpsecStatsSha1Mismatches": accIpsecStatsSha1Mismatches,
       "accIpsecStatsMd5Mistmatches": accIpsecStatsMd5Mistmatches,
       "accIpsecStatsReplayCheckFaileds": accIpsecStatsReplayCheckFaileds,
       "accIpsecStatsIllegalPads": accIpsecStatsIllegalPads,
       "accIpsecStatsSeqnoCycles": accIpsecStatsSeqnoCycles,
       "accIpsecStatsInsufficientPads": accIpsecStatsInsufficientPads,
       "accIpsecStatsTtlZeros": accIpsecStatsTtlZeros,
       "accIpsecStatsNoKeys": accIpsecStatsNoKeys,
       "accIpsecStatsIllegalFragments": accIpsecStatsIllegalFragments,
       "accIpsecStatsCpuOverloads": accIpsecStatsCpuOverloads,
       "accIpsecStatsHdrAllocs": accIpsecStatsHdrAllocs,
       "accIpsecStatsTlrAllocs": accIpsecStatsTlrAllocs,
       "accIpsecStatsBlockJoins": accIpsecStatsBlockJoins,
       "accIpsecSAConfig": accIpsecSAConfig,
       "accIpsecSAConfigTable": accIpsecSAConfigTable,
       "accIpsecSAConfigEntry": accIpsecSAConfigEntry,
       "accIpsecSAConfigIndex": accIpsecSAConfigIndex,
       "accIpsecSAConfigDir": accIpsecSAConfigDir,
       "accIpsecSAConfigMode": accIpsecSAConfigMode,
       "accIpsecSAConfigProtocol": accIpsecSAConfigProtocol,
       "accIpsecSAConfigSPI": accIpsecSAConfigSPI,
       "accIpsecSAConfigAuthAlgorithm": accIpsecSAConfigAuthAlgorithm,
       "accIpsecSAConfigReplayCheck": accIpsecSAConfigReplayCheck,
       "accIpsecSAConfigOverflowAudit": accIpsecSAConfigOverflowAudit,
       "accIpsecSAConfigCopyDF": accIpsecSAConfigCopyDF,
       "accIpsecSAConfigDestAddr": accIpsecSAConfigDestAddr,
       "accIpsecSAConfigSharedAuthSecret": accIpsecSAConfigSharedAuthSecret,
       "accIpsecSAConfigEncrAlgorithm": accIpsecSAConfigEncrAlgorithm,
       "accIpsecSAConfigSharedEncrSecret": accIpsecSAConfigSharedEncrSecret,
       "accIpsecSAConfigPriority": accIpsecSAConfigPriority,
       "accIpsecSAConfigSequenceNumber": accIpsecSAConfigSequenceNumber,
       "accIpsecSAConfigStatus": accIpsecSAConfigStatus,
       "accIpsecSAStats": accIpsecSAStats,
       "accIpsecSAStatsTable": accIpsecSAStatsTable,
       "accIpsecSAStatsEntry": accIpsecSAStatsEntry,
       "accIpsecSAStatsIndex": accIpsecSAStatsIndex,
       "accIpsecSAStatsOKPackets": accIpsecSAStatsOKPackets,
       "accIpsecSAStatsNotOKPackets": accIpsecSAStatsNotOKPackets,
       "accIpsecSAStatsCurrTicks": accIpsecSAStatsCurrTicks,
       "accIpsecSAStatsCurrBytes": accIpsecSAStatsCurrBytes,
       "accIpsecTraps": accIpsecTraps,
       "accIpSecsameSAIndxTrap": accIpSecsameSAIndxTrap,
       "accIpSecbadSAIndxTrap": accIpSecbadSAIndxTrap,
       "accIpSecexpKeyFldTrap": accIpSecexpKeyFldTrap,
       "accIpSecmsgSpiZeroTrap": accIpSecmsgSpiZeroTrap,
       "accIpSecauthencAlgoTrap": accIpSecauthencAlgoTrap,
       "accIpSeccwauthAhAlgoTrap": accIpSeccwauthAhAlgoTrap,
       "accIpSecmsgOflowOutTrap": accIpSecmsgOflowOutTrap,
       "accIpSecdfTunnSATrap": accIpSecdfTunnSATrap,
       "accIpSecdfNotSuppTrap": accIpSecdfNotSuppTrap,
       "accIpSecunsuppAlgoTrap": accIpSecunsuppAlgoTrap,
       "accIpSecencAlgESPTrap": accIpSecencAlgESPTrap,
       "accIpSecvldIPAddrTrap": accIpSecvldIPAddrTrap,
       "accIpSecipAddrSAInTrap": accIpSecipAddrSAInTrap,
       "accIpSecpeerGateAddrTrap": accIpSecpeerGateAddrTrap,
       "accIpSeckeyLenZeroTrap": accIpSeckeyLenZeroTrap,
       "accIpSecencKeyLenZeroTrap": accIpSecencKeyLenZeroTrap,
       "accIpSecseqZeroTrap": accIpSecseqZeroTrap,
       "accIpSecallocBytsFaildTrap": accIpSecallocBytsFaildTrap,
       "accIpSecnoSpcSATrap": accIpSecnoSpcSATrap,
       "accIpSecsaNameLenTrap": accIpSecsaNameLenTrap,
       "accIpSecauthKeyMaxTrap": accIpSecauthKeyMaxTrap,
       "accIpSechmacMD5KeyLenTrap": accIpSechmacMD5KeyLenTrap,
       "accIpSechmacSha1KeyLenTrap": accIpSechmacSha1KeyLenTrap,
       "accIpSecencMaxKeyTrap": accIpSecencMaxKeyTrap,
       "accIpSecencKeyLenMaxPhyTrap": accIpSecencKeyLenMaxPhyTrap,
       "accIpSecdesKeyLen8OctTrap": accIpSecdesKeyLen8OctTrap,
       "accIpSec3desKeyLenTrap": accIpSec3desKeyLenTrap,
       "accIpSeccastKeyLenTrap": accIpSeccastKeyLenTrap,
       "accIpSecblowKeyTrap": accIpSecblowKeyTrap,
       "accIpSecsaAreaSzTrap": accIpSecsaAreaSzTrap,
       "accIpSecsameSPIAddrTrap": accIpSecsameSPIAddrTrap,
       "accIpSecnotHexDigTrap": accIpSecnotHexDigTrap,
       "accIpSecsecOddDigTrap": accIpSecsecOddDigTrap,
       "accIpSecnoSANameTrap": accIpSecnoSANameTrap,
       "accIpSecsaInptFiltTrap": accIpSecsaInptFiltTrap,
       "accIpSecsaOtptFiltTrap": accIpSecsaOtptFiltTrap,
       "accIpsecTrapMsg": accIpsecTrapMsg}
)
