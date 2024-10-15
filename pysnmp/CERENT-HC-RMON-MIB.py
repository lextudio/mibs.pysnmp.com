# SNMP MIB module (CERENT-HC-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-HC-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:25 2024
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

(cerentGeneric,
 cerentModules,
 cerentRequirements) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentGeneric",
    "cerentModules",
    "cerentRequirements")

(mediaIndependentIndex,) = mibBuilder.importSymbols(
    "HC-RMON-MIB",
    "mediaIndependentIndex")

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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

cerentHcRMON = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 110)
)
cerentHcRMON.setRevisions(
        ("1912-01-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CerentHcRmonMIBObjects_ObjectIdentity = ObjectIdentity
cerentHcRmonMIBObjects = _CerentHcRmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70)
)
_CerentHcRmon_ObjectIdentity = ObjectIdentity
cerentHcRmon = _CerentHcRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10)
)
_CMediaIndependentTable_Object = MibTable
cMediaIndependentTable = _CMediaIndependentTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10)
)
if mibBuilder.loadTexts:
    cMediaIndependentTable.setStatus("current")
_CMediaIndependentEntry_Object = MibTableRow
cMediaIndependentEntry = _CMediaIndependentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1)
)
cMediaIndependentEntry.setIndexNames(
    (0, "HC-RMON-MIB", "mediaIndependentIndex"),
)
if mibBuilder.loadTexts:
    cMediaIndependentEntry.setStatus("current")
_CMediaIndependentInBadCRC_Type = Counter32
_CMediaIndependentInBadCRC_Object = MibTableColumn
cMediaIndependentInBadCRC = _CMediaIndependentInBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 10),
    _CMediaIndependentInBadCRC_Type()
)
cMediaIndependentInBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInBadCRC.setStatus("current")
_CMediaIndependentOutBadCRC_Type = Counter32
_CMediaIndependentOutBadCRC_Object = MibTableColumn
cMediaIndependentOutBadCRC = _CMediaIndependentOutBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 20),
    _CMediaIndependentOutBadCRC_Type()
)
cMediaIndependentOutBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutBadCRC.setStatus("current")
_CMediaIndependentInFramesTruncated_Type = Counter32
_CMediaIndependentInFramesTruncated_Object = MibTableColumn
cMediaIndependentInFramesTruncated = _CMediaIndependentInFramesTruncated_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 30),
    _CMediaIndependentInFramesTruncated_Type()
)
cMediaIndependentInFramesTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInFramesTruncated.setStatus("current")
_CMediaIndependentInFramesTooLong_Type = Counter32
_CMediaIndependentInFramesTooLong_Object = MibTableColumn
cMediaIndependentInFramesTooLong = _CMediaIndependentInFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 40),
    _CMediaIndependentInFramesTooLong_Type()
)
cMediaIndependentInFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInFramesTooLong.setStatus("current")
_CMediaIndependentLinkRecoveries_Type = Counter32
_CMediaIndependentLinkRecoveries_Object = MibTableColumn
cMediaIndependentLinkRecoveries = _CMediaIndependentLinkRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 50),
    _CMediaIndependentLinkRecoveries_Type()
)
cMediaIndependentLinkRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentLinkRecoveries.setStatus("current")
_CMediaIndependentInDistanceExtBuffers_Type = Counter32
_CMediaIndependentInDistanceExtBuffers_Object = MibTableColumn
cMediaIndependentInDistanceExtBuffers = _CMediaIndependentInDistanceExtBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 60),
    _CMediaIndependentInDistanceExtBuffers_Type()
)
cMediaIndependentInDistanceExtBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInDistanceExtBuffers.setStatus("current")
_CMediaIndependentOutDistanceExtBuffers_Type = Counter32
_CMediaIndependentOutDistanceExtBuffers_Object = MibTableColumn
cMediaIndependentOutDistanceExtBuffers = _CMediaIndependentOutDistanceExtBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 70),
    _CMediaIndependentOutDistanceExtBuffers_Type()
)
cMediaIndependentOutDistanceExtBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutDistanceExtBuffers.setStatus("current")
_CMediaIndependentInCredits_Type = Counter32
_CMediaIndependentInCredits_Object = MibTableColumn
cMediaIndependentInCredits = _CMediaIndependentInCredits_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 80),
    _CMediaIndependentInCredits_Type()
)
cMediaIndependentInCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInCredits.setStatus("current")
_CMediaIndependentOutCredits_Type = Counter32
_CMediaIndependentOutCredits_Object = MibTableColumn
cMediaIndependentOutCredits = _CMediaIndependentOutCredits_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 90),
    _CMediaIndependentOutCredits_Type()
)
cMediaIndependentOutCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutCredits.setStatus("current")
_CMediaIndependentOutZeroCredits_Type = Counter32
_CMediaIndependentOutZeroCredits_Object = MibTableColumn
cMediaIndependentOutZeroCredits = _CMediaIndependentOutZeroCredits_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 100),
    _CMediaIndependentOutZeroCredits_Type()
)
cMediaIndependentOutZeroCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutZeroCredits.setStatus("current")
_CMediaIndependentInGfpSBitErr_Type = Counter32
_CMediaIndependentInGfpSBitErr_Object = MibTableColumn
cMediaIndependentInGfpSBitErr = _CMediaIndependentInGfpSBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 110),
    _CMediaIndependentInGfpSBitErr_Type()
)
cMediaIndependentInGfpSBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpSBitErr.setStatus("current")
_CMediaIndependentInGfpMBitErr_Type = Counter32
_CMediaIndependentInGfpMBitErr_Object = MibTableColumn
cMediaIndependentInGfpMBitErr = _CMediaIndependentInGfpMBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 120),
    _CMediaIndependentInGfpMBitErr_Type()
)
cMediaIndependentInGfpMBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpMBitErr.setStatus("current")
_CMediaIndependentInGfpCRCErr_Type = Counter32
_CMediaIndependentInGfpCRCErr_Object = MibTableColumn
cMediaIndependentInGfpCRCErr = _CMediaIndependentInGfpCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 130),
    _CMediaIndependentInGfpCRCErr_Type()
)
cMediaIndependentInGfpCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpCRCErr.setStatus("current")
_CMediaIndependentInGfpFrames_Type = Counter32
_CMediaIndependentInGfpFrames_Object = MibTableColumn
cMediaIndependentInGfpFrames = _CMediaIndependentInGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 140),
    _CMediaIndependentInGfpFrames_Type()
)
cMediaIndependentInGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpFrames.setStatus("current")
_CMediaIndependentInOverflowGfpFrames_Type = Counter32
_CMediaIndependentInOverflowGfpFrames_Object = MibTableColumn
cMediaIndependentInOverflowGfpFrames = _CMediaIndependentInOverflowGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 150),
    _CMediaIndependentInOverflowGfpFrames_Type()
)
cMediaIndependentInOverflowGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInOverflowGfpFrames.setStatus("current")
_CMediaIndependentInHighCapacityGfpFrames_Type = Counter64
_CMediaIndependentInHighCapacityGfpFrames_Object = MibTableColumn
cMediaIndependentInHighCapacityGfpFrames = _CMediaIndependentInHighCapacityGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 160),
    _CMediaIndependentInHighCapacityGfpFrames_Type()
)
cMediaIndependentInHighCapacityGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInHighCapacityGfpFrames.setStatus("current")
_CMediaIndependentOutGfpFrames_Type = Counter32
_CMediaIndependentOutGfpFrames_Object = MibTableColumn
cMediaIndependentOutGfpFrames = _CMediaIndependentOutGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 170),
    _CMediaIndependentOutGfpFrames_Type()
)
cMediaIndependentOutGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutGfpFrames.setStatus("current")
_CMediaIndependentOutOverflowGfpFrames_Type = Counter32
_CMediaIndependentOutOverflowGfpFrames_Object = MibTableColumn
cMediaIndependentOutOverflowGfpFrames = _CMediaIndependentOutOverflowGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 180),
    _CMediaIndependentOutOverflowGfpFrames_Type()
)
cMediaIndependentOutOverflowGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutOverflowGfpFrames.setStatus("current")
_CMediaIndependentOutHighCapacityGfpFrames_Type = Counter64
_CMediaIndependentOutHighCapacityGfpFrames_Object = MibTableColumn
cMediaIndependentOutHighCapacityGfpFrames = _CMediaIndependentOutHighCapacityGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 190),
    _CMediaIndependentOutHighCapacityGfpFrames_Type()
)
cMediaIndependentOutHighCapacityGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutHighCapacityGfpFrames.setStatus("current")
_CMediaIndependentInGfpOctets_Type = Counter32
_CMediaIndependentInGfpOctets_Object = MibTableColumn
cMediaIndependentInGfpOctets = _CMediaIndependentInGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 200),
    _CMediaIndependentInGfpOctets_Type()
)
cMediaIndependentInGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpOctets.setStatus("current")
_CMediaIndependentInOverflowGfpOctets_Type = Counter32
_CMediaIndependentInOverflowGfpOctets_Object = MibTableColumn
cMediaIndependentInOverflowGfpOctets = _CMediaIndependentInOverflowGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 210),
    _CMediaIndependentInOverflowGfpOctets_Type()
)
cMediaIndependentInOverflowGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInOverflowGfpOctets.setStatus("current")
_CMediaIndependentInHighCapacityGfpOctets_Type = Counter64
_CMediaIndependentInHighCapacityGfpOctets_Object = MibTableColumn
cMediaIndependentInHighCapacityGfpOctets = _CMediaIndependentInHighCapacityGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 220),
    _CMediaIndependentInHighCapacityGfpOctets_Type()
)
cMediaIndependentInHighCapacityGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInHighCapacityGfpOctets.setStatus("current")
_CMediaIndependentOutGfpOctets_Type = Counter32
_CMediaIndependentOutGfpOctets_Object = MibTableColumn
cMediaIndependentOutGfpOctets = _CMediaIndependentOutGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 230),
    _CMediaIndependentOutGfpOctets_Type()
)
cMediaIndependentOutGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutGfpOctets.setStatus("current")
_CMediaIndependentOutOverflowGfpOctets_Type = Counter32
_CMediaIndependentOutOverflowGfpOctets_Object = MibTableColumn
cMediaIndependentOutOverflowGfpOctets = _CMediaIndependentOutOverflowGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 240),
    _CMediaIndependentOutOverflowGfpOctets_Type()
)
cMediaIndependentOutOverflowGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutOverflowGfpOctets.setStatus("current")
_CMediaIndependentOutHighCapacityGfpOctets_Type = Counter64
_CMediaIndependentOutHighCapacityGfpOctets_Object = MibTableColumn
cMediaIndependentOutHighCapacityGfpOctets = _CMediaIndependentOutHighCapacityGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 250),
    _CMediaIndependentOutHighCapacityGfpOctets_Type()
)
cMediaIndependentOutHighCapacityGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutHighCapacityGfpOctets.setStatus("current")
_CMediaIndependentInGfpTypeInvalid_Type = Counter32
_CMediaIndependentInGfpTypeInvalid_Object = MibTableColumn
cMediaIndependentInGfpTypeInvalid = _CMediaIndependentInGfpTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 260),
    _CMediaIndependentInGfpTypeInvalid_Type()
)
cMediaIndependentInGfpTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpTypeInvalid.setStatus("current")
_CMediaIndependentInGfpCIDInvalid_Type = Counter32
_CMediaIndependentInGfpCIDInvalid_Object = MibTableColumn
cMediaIndependentInGfpCIDInvalid = _CMediaIndependentInGfpCIDInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 270),
    _CMediaIndependentInGfpCIDInvalid_Type()
)
cMediaIndependentInGfpCIDInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpCIDInvalid.setStatus("current")
_CMediaIndependentInGfpLFDRaised_Type = Counter32
_CMediaIndependentInGfpLFDRaised_Object = MibTableColumn
cMediaIndependentInGfpLFDRaised = _CMediaIndependentInGfpLFDRaised_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 280),
    _CMediaIndependentInGfpLFDRaised_Type()
)
cMediaIndependentInGfpLFDRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpLFDRaised.setStatus("current")
_CMediaIndependentInGfpCSFRaised_Type = Counter32
_CMediaIndependentInGfpCSFRaised_Object = MibTableColumn
cMediaIndependentInGfpCSFRaised = _CMediaIndependentInGfpCSFRaised_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 290),
    _CMediaIndependentInGfpCSFRaised_Type()
)
cMediaIndependentInGfpCSFRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpCSFRaised.setStatus("current")
_CMediaIndependentGfpRoundTripLatency_Type = Counter32
_CMediaIndependentGfpRoundTripLatency_Object = MibTableColumn
cMediaIndependentGfpRoundTripLatency = _CMediaIndependentGfpRoundTripLatency_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 300),
    _CMediaIndependentGfpRoundTripLatency_Type()
)
cMediaIndependentGfpRoundTripLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentGfpRoundTripLatency.setStatus("current")
_CMediaIndependent8b10bIdleSets_Type = Counter32
_CMediaIndependent8b10bIdleSets_Object = MibTableColumn
cMediaIndependent8b10bIdleSets = _CMediaIndependent8b10bIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 310),
    _CMediaIndependent8b10bIdleSets_Type()
)
cMediaIndependent8b10bIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bIdleSets.setStatus("current")
_CMediaIndependentOverflow8b10bIdleSets_Type = Counter32
_CMediaIndependentOverflow8b10bIdleSets_Object = MibTableColumn
cMediaIndependentOverflow8b10bIdleSets = _CMediaIndependentOverflow8b10bIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 320),
    _CMediaIndependentOverflow8b10bIdleSets_Type()
)
cMediaIndependentOverflow8b10bIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOverflow8b10bIdleSets.setStatus("current")
_CMediaIndependentHighCapacity8b10bIdleSets_Type = Counter64
_CMediaIndependentHighCapacity8b10bIdleSets_Object = MibTableColumn
cMediaIndependentHighCapacity8b10bIdleSets = _CMediaIndependentHighCapacity8b10bIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 330),
    _CMediaIndependentHighCapacity8b10bIdleSets_Type()
)
cMediaIndependentHighCapacity8b10bIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHighCapacity8b10bIdleSets.setStatus("current")
_CMediaIndependent8b10bNonIdleSets_Type = Counter32
_CMediaIndependent8b10bNonIdleSets_Object = MibTableColumn
cMediaIndependent8b10bNonIdleSets = _CMediaIndependent8b10bNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 340),
    _CMediaIndependent8b10bNonIdleSets_Type()
)
cMediaIndependent8b10bNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bNonIdleSets.setStatus("current")
_CMediaIndependentOverflow8b10bNonIdleSets_Type = Counter32
_CMediaIndependentOverflow8b10bNonIdleSets_Object = MibTableColumn
cMediaIndependentOverflow8b10bNonIdleSets = _CMediaIndependentOverflow8b10bNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 350),
    _CMediaIndependentOverflow8b10bNonIdleSets_Type()
)
cMediaIndependentOverflow8b10bNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOverflow8b10bNonIdleSets.setStatus("current")
_CMediaIndependentHighCapacity8b10bNonIdleSets_Type = Counter64
_CMediaIndependentHighCapacity8b10bNonIdleSets_Object = MibTableColumn
cMediaIndependentHighCapacity8b10bNonIdleSets = _CMediaIndependentHighCapacity8b10bNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 360),
    _CMediaIndependentHighCapacity8b10bNonIdleSets_Type()
)
cMediaIndependentHighCapacity8b10bNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHighCapacity8b10bNonIdleSets.setStatus("current")
_CMediaIndependent8b10bDataSets_Type = Counter32
_CMediaIndependent8b10bDataSets_Object = MibTableColumn
cMediaIndependent8b10bDataSets = _CMediaIndependent8b10bDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 370),
    _CMediaIndependent8b10bDataSets_Type()
)
cMediaIndependent8b10bDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bDataSets.setStatus("current")
_CMediaIndependentOverflow8b10bDataSets_Type = Counter32
_CMediaIndependentOverflow8b10bDataSets_Object = MibTableColumn
cMediaIndependentOverflow8b10bDataSets = _CMediaIndependentOverflow8b10bDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 380),
    _CMediaIndependentOverflow8b10bDataSets_Type()
)
cMediaIndependentOverflow8b10bDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOverflow8b10bDataSets.setStatus("current")
_CMediaIndependentHighCapacity8b10bDataSets_Type = Counter64
_CMediaIndependentHighCapacity8b10bDataSets_Object = MibTableColumn
cMediaIndependentHighCapacity8b10bDataSets = _CMediaIndependentHighCapacity8b10bDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 390),
    _CMediaIndependentHighCapacity8b10bDataSets_Type()
)
cMediaIndependentHighCapacity8b10bDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHighCapacity8b10bDataSets.setStatus("current")
_CMediaIndependent8b10bInvalidOrdSets_Type = Counter32
_CMediaIndependent8b10bInvalidOrdSets_Object = MibTableColumn
cMediaIndependent8b10bInvalidOrdSets = _CMediaIndependent8b10bInvalidOrdSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 400),
    _CMediaIndependent8b10bInvalidOrdSets_Type()
)
cMediaIndependent8b10bInvalidOrdSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bInvalidOrdSets.setStatus("current")
_CMediaIndependent8b10bEncodingDispErr_Type = Counter32
_CMediaIndependent8b10bEncodingDispErr_Object = MibTableColumn
cMediaIndependent8b10bEncodingDispErr = _CMediaIndependent8b10bEncodingDispErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 410),
    _CMediaIndependent8b10bEncodingDispErr_Type()
)
cMediaIndependent8b10bEncodingDispErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bEncodingDispErr.setStatus("current")
_CMediaIndependent8b10bLossOfSync_Type = Counter32
_CMediaIndependent8b10bLossOfSync_Object = MibTableColumn
cMediaIndependent8b10bLossOfSync = _CMediaIndependent8b10bLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 420),
    _CMediaIndependent8b10bLossOfSync_Type()
)
cMediaIndependent8b10bLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bLossOfSync.setStatus("current")
_CMediaIndependentInPauseFrames_Type = Counter32
_CMediaIndependentInPauseFrames_Object = MibTableColumn
cMediaIndependentInPauseFrames = _CMediaIndependentInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 430),
    _CMediaIndependentInPauseFrames_Type()
)
cMediaIndependentInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInPauseFrames.setStatus("current")
_CMediaIndependentOutPauseFrames_Type = Counter32
_CMediaIndependentOutPauseFrames_Object = MibTableColumn
cMediaIndependentOutPauseFrames = _CMediaIndependentOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 440),
    _CMediaIndependentOutPauseFrames_Type()
)
cMediaIndependentOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutPauseFrames.setStatus("current")
_CMediaIndependentInPktsDroppedInternalCongestion_Type = Counter32
_CMediaIndependentInPktsDroppedInternalCongestion_Object = MibTableColumn
cMediaIndependentInPktsDroppedInternalCongestion = _CMediaIndependentInPktsDroppedInternalCongestion_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 450),
    _CMediaIndependentInPktsDroppedInternalCongestion_Type()
)
cMediaIndependentInPktsDroppedInternalCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInPktsDroppedInternalCongestion.setStatus("current")
_CMediaIndependentOutPktsDroppedInternalCongestion_Type = Counter32
_CMediaIndependentOutPktsDroppedInternalCongestion_Object = MibTableColumn
cMediaIndependentOutPktsDroppedInternalCongestion = _CMediaIndependentOutPktsDroppedInternalCongestion_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 460),
    _CMediaIndependentOutPktsDroppedInternalCongestion_Type()
)
cMediaIndependentOutPktsDroppedInternalCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutPktsDroppedInternalCongestion.setStatus("current")
_CMediaIndependentInControlFrames_Type = Counter32
_CMediaIndependentInControlFrames_Object = MibTableColumn
cMediaIndependentInControlFrames = _CMediaIndependentInControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 470),
    _CMediaIndependentInControlFrames_Type()
)
cMediaIndependentInControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInControlFrames.setStatus("current")
_CMediaIndependentInUnknownOpcodeFrames_Type = Counter32
_CMediaIndependentInUnknownOpcodeFrames_Object = MibTableColumn
cMediaIndependentInUnknownOpcodeFrames = _CMediaIndependentInUnknownOpcodeFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 480),
    _CMediaIndependentInUnknownOpcodeFrames_Type()
)
cMediaIndependentInUnknownOpcodeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInUnknownOpcodeFrames.setStatus("current")
_CMediaIndependentHdlcPktDrops_Type = Counter32
_CMediaIndependentHdlcPktDrops_Object = MibTableColumn
cMediaIndependentHdlcPktDrops = _CMediaIndependentHdlcPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 490),
    _CMediaIndependentHdlcPktDrops_Type()
)
cMediaIndependentHdlcPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHdlcPktDrops.setStatus("current")
_CMediaIndependentHdlcInOctets_Type = Counter32
_CMediaIndependentHdlcInOctets_Object = MibTableColumn
cMediaIndependentHdlcInOctets = _CMediaIndependentHdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 500),
    _CMediaIndependentHdlcInOctets_Type()
)
cMediaIndependentHdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHdlcInOctets.setStatus("current")
_CMediaIndependentHdlcOutOctets_Type = Counter32
_CMediaIndependentHdlcOutOctets_Object = MibTableColumn
cMediaIndependentHdlcOutOctets = _CMediaIndependentHdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 510),
    _CMediaIndependentHdlcOutOctets_Type()
)
cMediaIndependentHdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHdlcOutOctets.setStatus("current")
_CMediaIndependentHdlcInAborts_Type = Counter32
_CMediaIndependentHdlcInAborts_Object = MibTableColumn
cMediaIndependentHdlcInAborts = _CMediaIndependentHdlcInAborts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 520),
    _CMediaIndependentHdlcInAborts_Type()
)
cMediaIndependentHdlcInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHdlcInAborts.setStatus("current")
_CMediaIndependentInShortPkts_Type = Counter32
_CMediaIndependentInShortPkts_Object = MibTableColumn
cMediaIndependentInShortPkts = _CMediaIndependentInShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 530),
    _CMediaIndependentInShortPkts_Type()
)
cMediaIndependentInShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInShortPkts.setStatus("current")
_CMediaIndependentOutShortPkts_Type = Counter32
_CMediaIndependentOutShortPkts_Object = MibTableColumn
cMediaIndependentOutShortPkts = _CMediaIndependentOutShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 535),
    _CMediaIndependentOutShortPkts_Type()
)
cMediaIndependentOutShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutShortPkts.setStatus("current")
_CMediaIndependentOversizeDropped_Type = Counter32
_CMediaIndependentOversizeDropped_Object = MibTableColumn
cMediaIndependentOversizeDropped = _CMediaIndependentOversizeDropped_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 540),
    _CMediaIndependentOversizeDropped_Type()
)
cMediaIndependentOversizeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOversizeDropped.setStatus("current")
_CMediaIndependentInErrorBytePkts_Type = Counter32
_CMediaIndependentInErrorBytePkts_Object = MibTableColumn
cMediaIndependentInErrorBytePkts = _CMediaIndependentInErrorBytePkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 550),
    _CMediaIndependentInErrorBytePkts_Type()
)
cMediaIndependentInErrorBytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInErrorBytePkts.setStatus("current")
_CMediaIndependentInFramingErrorPkts_Type = Counter32
_CMediaIndependentInFramingErrorPkts_Object = MibTableColumn
cMediaIndependentInFramingErrorPkts = _CMediaIndependentInFramingErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 560),
    _CMediaIndependentInFramingErrorPkts_Type()
)
cMediaIndependentInFramingErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInFramingErrorPkts.setStatus("current")
_CMediaIndependentInJunkInterPkts_Type = Counter32
_CMediaIndependentInJunkInterPkts_Object = MibTableColumn
cMediaIndependentInJunkInterPkts = _CMediaIndependentInJunkInterPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 570),
    _CMediaIndependentInJunkInterPkts_Type()
)
cMediaIndependentInJunkInterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInJunkInterPkts.setStatus("current")
_CMediaIndependentOutOversizePkts_Type = Counter32
_CMediaIndependentOutOversizePkts_Object = MibTableColumn
cMediaIndependentOutOversizePkts = _CMediaIndependentOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 580),
    _CMediaIndependentOutOversizePkts_Type()
)
cMediaIndependentOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutOversizePkts.setStatus("current")
_CMediaIndependentInPayloadCrcErrors_Type = Counter32
_CMediaIndependentInPayloadCrcErrors_Object = MibTableColumn
cMediaIndependentInPayloadCrcErrors = _CMediaIndependentInPayloadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 590),
    _CMediaIndependentInPayloadCrcErrors_Type()
)
cMediaIndependentInPayloadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInPayloadCrcErrors.setStatus("current")
_CMediaIndependentOutPayloadCrcErrors_Type = Counter32
_CMediaIndependentOutPayloadCrcErrors_Object = MibTableColumn
cMediaIndependentOutPayloadCrcErrors = _CMediaIndependentOutPayloadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 600),
    _CMediaIndependentOutPayloadCrcErrors_Type()
)
cMediaIndependentOutPayloadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutPayloadCrcErrors.setStatus("current")
_CMediaIndependentInRecvrReady_Type = Counter32
_CMediaIndependentInRecvrReady_Object = MibTableColumn
cMediaIndependentInRecvrReady = _CMediaIndependentInRecvrReady_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 610),
    _CMediaIndependentInRecvrReady_Type()
)
cMediaIndependentInRecvrReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInRecvrReady.setStatus("current")
_CMediaIndependentOutRecvrReady_Type = Counter32
_CMediaIndependentOutRecvrReady_Object = MibTableColumn
cMediaIndependentOutRecvrReady = _CMediaIndependentOutRecvrReady_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 620),
    _CMediaIndependentOutRecvrReady_Type()
)
cMediaIndependentOutRecvrReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutRecvrReady.setStatus("current")
_CMediaIndependent8b10bInvalidOrdSetsDispErrorsSum_Type = Counter32
_CMediaIndependent8b10bInvalidOrdSetsDispErrorsSum_Object = MibTableColumn
cMediaIndependent8b10bInvalidOrdSetsDispErrorsSum = _CMediaIndependent8b10bInvalidOrdSetsDispErrorsSum_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 630),
    _CMediaIndependent8b10bInvalidOrdSetsDispErrorsSum_Type()
)
cMediaIndependent8b10bInvalidOrdSetsDispErrorsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependent8b10bInvalidOrdSetsDispErrorsSum.setStatus("current")
_CMediaIndependentInGfpSblkCRCErr_Type = Counter32
_CMediaIndependentInGfpSblkCRCErr_Object = MibTableColumn
cMediaIndependentInGfpSblkCRCErr = _CMediaIndependentInGfpSblkCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 640),
    _CMediaIndependentInGfpSblkCRCErr_Type()
)
cMediaIndependentInGfpSblkCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentInGfpSblkCRCErr.setStatus("current")
_CMediaIndependentOutFramesTooLong_Type = Counter32
_CMediaIndependentOutFramesTooLong_Object = MibTableColumn
cMediaIndependentOutFramesTooLong = _CMediaIndependentOutFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 650),
    _CMediaIndependentOutFramesTooLong_Type()
)
cMediaIndependentOutFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutFramesTooLong.setStatus("current")
_CMediaIndependentPkts1519to1522Octets_Type = Counter32
_CMediaIndependentPkts1519to1522Octets_Object = MibTableColumn
cMediaIndependentPkts1519to1522Octets = _CMediaIndependentPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 660),
    _CMediaIndependentPkts1519to1522Octets_Type()
)
cMediaIndependentPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPkts1519to1522Octets.setStatus("current")
_CMediaIndependentOutFramesTruncated_Type = Counter32
_CMediaIndependentOutFramesTruncated_Object = MibTableColumn
cMediaIndependentOutFramesTruncated = _CMediaIndependentOutFramesTruncated_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 670),
    _CMediaIndependentOutFramesTruncated_Type()
)
cMediaIndependentOutFramesTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentOutFramesTruncated.setStatus("current")
_CMediaIndependentPcsErrCount_Type = Counter32
_CMediaIndependentPcsErrCount_Object = MibTableColumn
cMediaIndependentPcsErrCount = _CMediaIndependentPcsErrCount_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 680),
    _CMediaIndependentPcsErrCount_Type()
)
cMediaIndependentPcsErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPcsErrCount.setStatus("current")
_CMediaIndependentPcsErrCount2_Type = Counter32
_CMediaIndependentPcsErrCount2_Object = MibTableColumn
cMediaIndependentPcsErrCount2 = _CMediaIndependentPcsErrCount2_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 690),
    _CMediaIndependentPcsErrCount2_Type()
)
cMediaIndependentPcsErrCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPcsErrCount2.setStatus("current")
_CMediaIndependentPcs49RxErrBer_Type = Counter32
_CMediaIndependentPcs49RxErrBer_Object = MibTableColumn
cMediaIndependentPcs49RxErrBer = _CMediaIndependentPcs49RxErrBer_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 700),
    _CMediaIndependentPcs49RxErrBer_Type()
)
cMediaIndependentPcs49RxErrBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPcs49RxErrBer.setStatus("current")
_CMediaIndependentPcs49RxErrDec_Type = Counter32
_CMediaIndependentPcs49RxErrDec_Object = MibTableColumn
cMediaIndependentPcs49RxErrDec = _CMediaIndependentPcs49RxErrDec_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 710),
    _CMediaIndependentPcs49RxErrDec_Type()
)
cMediaIndependentPcs49RxErrDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPcs49RxErrDec.setStatus("current")
_CMediaIndependentPkts1519toMaxOctets_Type = Counter32
_CMediaIndependentPkts1519toMaxOctets_Object = MibTableColumn
cMediaIndependentPkts1519toMaxOctets = _CMediaIndependentPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 720),
    _CMediaIndependentPkts1519toMaxOctets_Type()
)
cMediaIndependentPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPkts1519toMaxOctets.setStatus("current")
_CMediaIndependentRxLcvErrors_Type = Counter32
_CMediaIndependentRxLcvErrors_Object = MibTableColumn
cMediaIndependentRxLcvErrors = _CMediaIndependentRxLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 730),
    _CMediaIndependentRxLcvErrors_Type()
)
cMediaIndependentRxLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentRxLcvErrors.setStatus("current")
_CMediaIndependentTxLcvErrors_Type = Counter32
_CMediaIndependentTxLcvErrors_Object = MibTableColumn
cMediaIndependentTxLcvErrors = _CMediaIndependentTxLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 740),
    _CMediaIndependentTxLcvErrors_Type()
)
cMediaIndependentTxLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentTxLcvErrors.setStatus("current")
_CMediaIndependentGfpRxCmfFrame_Type = Counter32
_CMediaIndependentGfpRxCmfFrame_Object = MibTableColumn
cMediaIndependentGfpRxCmfFrame = _CMediaIndependentGfpRxCmfFrame_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 750),
    _CMediaIndependentGfpRxCmfFrame_Type()
)
cMediaIndependentGfpRxCmfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentGfpRxCmfFrame.setStatus("current")
_CMediaIndependentGfpTxCmfFrame_Type = Counter32
_CMediaIndependentGfpTxCmfFrame_Object = MibTableColumn
cMediaIndependentGfpTxCmfFrame = _CMediaIndependentGfpTxCmfFrame_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 760),
    _CMediaIndependentGfpTxCmfFrame_Type()
)
cMediaIndependentGfpTxCmfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentGfpTxCmfFrame.setStatus("current")
_CMediaIndependentPcsEgRxErrFrames_Type = Counter32
_CMediaIndependentPcsEgRxErrFrames_Object = MibTableColumn
cMediaIndependentPcsEgRxErrFrames = _CMediaIndependentPcsEgRxErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 10, 1, 770),
    _CMediaIndependentPcsEgRxErrFrames_Type()
)
cMediaIndependentPcsEgRxErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentPcsEgRxErrFrames.setStatus("current")
_CMediaIndependentHistoryControlTable_Object = MibTable
cMediaIndependentHistoryControlTable = _CMediaIndependentHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20)
)
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlTable.setStatus("current")
_CMediaIndependentHistoryControlEntry_Object = MibTableRow
cMediaIndependentHistoryControlEntry = _CMediaIndependentHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1)
)
cMediaIndependentHistoryControlEntry.setIndexNames(
    (0, "CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlEntry.setStatus("current")


class _CMediaIndependentHistoryControlIndex_Type(Integer32):
    """Custom type cMediaIndependentHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMediaIndependentHistoryControlIndex_Type.__name__ = "Integer32"
_CMediaIndependentHistoryControlIndex_Object = MibTableColumn
cMediaIndependentHistoryControlIndex = _CMediaIndependentHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 10),
    _CMediaIndependentHistoryControlIndex_Type()
)
cMediaIndependentHistoryControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlIndex.setStatus("current")
_CMediaIndependentHistoryControlDataSource_Type = ObjectIdentifier
_CMediaIndependentHistoryControlDataSource_Object = MibTableColumn
cMediaIndependentHistoryControlDataSource = _CMediaIndependentHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 20),
    _CMediaIndependentHistoryControlDataSource_Type()
)
cMediaIndependentHistoryControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlDataSource.setStatus("current")


class _CMediaIndependentHistoryControlBucketsRequested_Type(Integer32):
    """Custom type cMediaIndependentHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMediaIndependentHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_CMediaIndependentHistoryControlBucketsRequested_Object = MibTableColumn
cMediaIndependentHistoryControlBucketsRequested = _CMediaIndependentHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 30),
    _CMediaIndependentHistoryControlBucketsRequested_Type()
)
cMediaIndependentHistoryControlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlBucketsRequested.setStatus("current")


class _CMediaIndependentHistoryControlBucketsGranted_Type(Integer32):
    """Custom type cMediaIndependentHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMediaIndependentHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_CMediaIndependentHistoryControlBucketsGranted_Object = MibTableColumn
cMediaIndependentHistoryControlBucketsGranted = _CMediaIndependentHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 40),
    _CMediaIndependentHistoryControlBucketsGranted_Type()
)
cMediaIndependentHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlBucketsGranted.setStatus("current")


class _CMediaIndependentHistoryControlInterval_Type(Integer32):
    """Custom type cMediaIndependentHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CMediaIndependentHistoryControlInterval_Type.__name__ = "Integer32"
_CMediaIndependentHistoryControlInterval_Object = MibTableColumn
cMediaIndependentHistoryControlInterval = _CMediaIndependentHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 50),
    _CMediaIndependentHistoryControlInterval_Type()
)
cMediaIndependentHistoryControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlInterval.setUnits("Seconds")
_CMediaIndependentHistoryControlOwner_Type = OwnerString
_CMediaIndependentHistoryControlOwner_Object = MibTableColumn
cMediaIndependentHistoryControlOwner = _CMediaIndependentHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 60),
    _CMediaIndependentHistoryControlOwner_Type()
)
cMediaIndependentHistoryControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlOwner.setStatus("current")
_CMediaIndependentHistoryControlStatus_Type = EntryStatus
_CMediaIndependentHistoryControlStatus_Object = MibTableColumn
cMediaIndependentHistoryControlStatus = _CMediaIndependentHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 20, 1, 70),
    _CMediaIndependentHistoryControlStatus_Type()
)
cMediaIndependentHistoryControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryControlStatus.setStatus("current")
_CMediaIndependentHistoryTable_Object = MibTable
cMediaIndependentHistoryTable = _CMediaIndependentHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30)
)
if mibBuilder.loadTexts:
    cMediaIndependentHistoryTable.setStatus("current")
_CMediaIndependentHistoryEntry_Object = MibTableRow
cMediaIndependentHistoryEntry = _CMediaIndependentHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1)
)
cMediaIndependentHistoryEntry.setIndexNames(
    (0, "CERENT-HC-RMON-MIB", "cMediaIndependentHistoryIndex"),
    (0, "CERENT-HC-RMON-MIB", "cMediaIndependentHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    cMediaIndependentHistoryEntry.setStatus("current")


class _CMediaIndependentHistoryIndex_Type(Integer32):
    """Custom type cMediaIndependentHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMediaIndependentHistoryIndex_Type.__name__ = "Integer32"
_CMediaIndependentHistoryIndex_Object = MibTableColumn
cMediaIndependentHistoryIndex = _CMediaIndependentHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 10),
    _CMediaIndependentHistoryIndex_Type()
)
cMediaIndependentHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryIndex.setStatus("current")


class _CMediaIndependentHistorySampleIndex_Type(Integer32):
    """Custom type cMediaIndependentHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CMediaIndependentHistorySampleIndex_Type.__name__ = "Integer32"
_CMediaIndependentHistorySampleIndex_Object = MibTableColumn
cMediaIndependentHistorySampleIndex = _CMediaIndependentHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 20),
    _CMediaIndependentHistorySampleIndex_Type()
)
cMediaIndependentHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMediaIndependentHistorySampleIndex.setStatus("current")
_CMediaIndependentHistoryDropEvents_Type = Counter32
_CMediaIndependentHistoryDropEvents_Object = MibTableColumn
cMediaIndependentHistoryDropEvents = _CMediaIndependentHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 30),
    _CMediaIndependentHistoryDropEvents_Type()
)
cMediaIndependentHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryDropEvents.setStatus("current")
_CMediaIndependentHistoryDroppedFrames_Type = Counter32
_CMediaIndependentHistoryDroppedFrames_Object = MibTableColumn
cMediaIndependentHistoryDroppedFrames = _CMediaIndependentHistoryDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 40),
    _CMediaIndependentHistoryDroppedFrames_Type()
)
cMediaIndependentHistoryDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryDroppedFrames.setStatus("current")
_CMediaIndependentHistoryInPkts_Type = Counter32
_CMediaIndependentHistoryInPkts_Object = MibTableColumn
cMediaIndependentHistoryInPkts = _CMediaIndependentHistoryInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 50),
    _CMediaIndependentHistoryInPkts_Type()
)
cMediaIndependentHistoryInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInPkts.setStatus("current")
_CMediaIndependentHistoryInOverflowPkts_Type = Counter32
_CMediaIndependentHistoryInOverflowPkts_Object = MibTableColumn
cMediaIndependentHistoryInOverflowPkts = _CMediaIndependentHistoryInOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 60),
    _CMediaIndependentHistoryInOverflowPkts_Type()
)
cMediaIndependentHistoryInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInOverflowPkts.setStatus("current")
_CMediaIndependentHistoryInHighCapacityPkts_Type = Counter64
_CMediaIndependentHistoryInHighCapacityPkts_Object = MibTableColumn
cMediaIndependentHistoryInHighCapacityPkts = _CMediaIndependentHistoryInHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 70),
    _CMediaIndependentHistoryInHighCapacityPkts_Type()
)
cMediaIndependentHistoryInHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInHighCapacityPkts.setStatus("current")
_CMediaIndependentHistoryOutPkts_Type = Counter32
_CMediaIndependentHistoryOutPkts_Object = MibTableColumn
cMediaIndependentHistoryOutPkts = _CMediaIndependentHistoryOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 80),
    _CMediaIndependentHistoryOutPkts_Type()
)
cMediaIndependentHistoryOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutPkts.setStatus("current")
_CMediaIndependentHistoryOutOverflowPkts_Type = Counter32
_CMediaIndependentHistoryOutOverflowPkts_Object = MibTableColumn
cMediaIndependentHistoryOutOverflowPkts = _CMediaIndependentHistoryOutOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 90),
    _CMediaIndependentHistoryOutOverflowPkts_Type()
)
cMediaIndependentHistoryOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutOverflowPkts.setStatus("current")
_CMediaIndependentHistoryOutHighCapacityPkts_Type = Counter64
_CMediaIndependentHistoryOutHighCapacityPkts_Object = MibTableColumn
cMediaIndependentHistoryOutHighCapacityPkts = _CMediaIndependentHistoryOutHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 100),
    _CMediaIndependentHistoryOutHighCapacityPkts_Type()
)
cMediaIndependentHistoryOutHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutHighCapacityPkts.setStatus("current")
_CMediaIndependentHistoryInOctets_Type = Counter32
_CMediaIndependentHistoryInOctets_Object = MibTableColumn
cMediaIndependentHistoryInOctets = _CMediaIndependentHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 110),
    _CMediaIndependentHistoryInOctets_Type()
)
cMediaIndependentHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInOctets.setStatus("current")
_CMediaIndependentHistoryInOverflowOctets_Type = Counter32
_CMediaIndependentHistoryInOverflowOctets_Object = MibTableColumn
cMediaIndependentHistoryInOverflowOctets = _CMediaIndependentHistoryInOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 120),
    _CMediaIndependentHistoryInOverflowOctets_Type()
)
cMediaIndependentHistoryInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInOverflowOctets.setStatus("current")
_CMediaIndependentHistoryInHighCapacityOctets_Type = Counter64
_CMediaIndependentHistoryInHighCapacityOctets_Object = MibTableColumn
cMediaIndependentHistoryInHighCapacityOctets = _CMediaIndependentHistoryInHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 130),
    _CMediaIndependentHistoryInHighCapacityOctets_Type()
)
cMediaIndependentHistoryInHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInHighCapacityOctets.setStatus("current")
_CMediaIndependentHistoryOutOctets_Type = Counter32
_CMediaIndependentHistoryOutOctets_Object = MibTableColumn
cMediaIndependentHistoryOutOctets = _CMediaIndependentHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 140),
    _CMediaIndependentHistoryOutOctets_Type()
)
cMediaIndependentHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutOctets.setStatus("current")
_CMediaIndependentHistoryOutOverflowOctets_Type = Counter32
_CMediaIndependentHistoryOutOverflowOctets_Object = MibTableColumn
cMediaIndependentHistoryOutOverflowOctets = _CMediaIndependentHistoryOutOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 150),
    _CMediaIndependentHistoryOutOverflowOctets_Type()
)
cMediaIndependentHistoryOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutOverflowOctets.setStatus("current")
_CMediaIndependentHistoryOutHighCapacityOctets_Type = Counter64
_CMediaIndependentHistoryOutHighCapacityOctets_Object = MibTableColumn
cMediaIndependentHistoryOutHighCapacityOctets = _CMediaIndependentHistoryOutHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 160),
    _CMediaIndependentHistoryOutHighCapacityOctets_Type()
)
cMediaIndependentHistoryOutHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutHighCapacityOctets.setStatus("current")
_CMediaIndependentHistoryInNUCastPkts_Type = Counter32
_CMediaIndependentHistoryInNUCastPkts_Object = MibTableColumn
cMediaIndependentHistoryInNUCastPkts = _CMediaIndependentHistoryInNUCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 170),
    _CMediaIndependentHistoryInNUCastPkts_Type()
)
cMediaIndependentHistoryInNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInNUCastPkts.setStatus("current")
_CMediaIndependentHistoryInNUCastOverflowPkts_Type = Counter32
_CMediaIndependentHistoryInNUCastOverflowPkts_Object = MibTableColumn
cMediaIndependentHistoryInNUCastOverflowPkts = _CMediaIndependentHistoryInNUCastOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 180),
    _CMediaIndependentHistoryInNUCastOverflowPkts_Type()
)
cMediaIndependentHistoryInNUCastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInNUCastOverflowPkts.setStatus("current")
_CMediaIndependentHistoryInNUCastHighCapacityPkts_Type = Counter64
_CMediaIndependentHistoryInNUCastHighCapacityPkts_Object = MibTableColumn
cMediaIndependentHistoryInNUCastHighCapacityPkts = _CMediaIndependentHistoryInNUCastHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 190),
    _CMediaIndependentHistoryInNUCastHighCapacityPkts_Type()
)
cMediaIndependentHistoryInNUCastHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInNUCastHighCapacityPkts.setStatus("current")
_CMediaIndependentHistoryOutNUCastPkts_Type = Counter32
_CMediaIndependentHistoryOutNUCastPkts_Object = MibTableColumn
cMediaIndependentHistoryOutNUCastPkts = _CMediaIndependentHistoryOutNUCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 200),
    _CMediaIndependentHistoryOutNUCastPkts_Type()
)
cMediaIndependentHistoryOutNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutNUCastPkts.setStatus("current")
_CMediaIndependentHistoryOutNUCastOverflowPkts_Type = Counter32
_CMediaIndependentHistoryOutNUCastOverflowPkts_Object = MibTableColumn
cMediaIndependentHistoryOutNUCastOverflowPkts = _CMediaIndependentHistoryOutNUCastOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 210),
    _CMediaIndependentHistoryOutNUCastOverflowPkts_Type()
)
cMediaIndependentHistoryOutNUCastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutNUCastOverflowPkts.setStatus("current")
_CMediaIndependentHistoryOutNUCastHighCapacityPkts_Type = Counter64
_CMediaIndependentHistoryOutNUCastHighCapacityPkts_Object = MibTableColumn
cMediaIndependentHistoryOutNUCastHighCapacityPkts = _CMediaIndependentHistoryOutNUCastHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 220),
    _CMediaIndependentHistoryOutNUCastHighCapacityPkts_Type()
)
cMediaIndependentHistoryOutNUCastHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutNUCastHighCapacityPkts.setStatus("current")
_CMediaIndependentHistoryInErrors_Type = Counter32
_CMediaIndependentHistoryInErrors_Object = MibTableColumn
cMediaIndependentHistoryInErrors = _CMediaIndependentHistoryInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 230),
    _CMediaIndependentHistoryInErrors_Type()
)
cMediaIndependentHistoryInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInErrors.setStatus("current")
_CMediaIndependentHistoryOutErrors_Type = Counter32
_CMediaIndependentHistoryOutErrors_Object = MibTableColumn
cMediaIndependentHistoryOutErrors = _CMediaIndependentHistoryOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 240),
    _CMediaIndependentHistoryOutErrors_Type()
)
cMediaIndependentHistoryOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutErrors.setStatus("current")
_CMediaIndependentHistoryInBadCRC_Type = Counter32
_CMediaIndependentHistoryInBadCRC_Object = MibTableColumn
cMediaIndependentHistoryInBadCRC = _CMediaIndependentHistoryInBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 250),
    _CMediaIndependentHistoryInBadCRC_Type()
)
cMediaIndependentHistoryInBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInBadCRC.setStatus("current")
_CMediaIndependentHistoryOutBadCRC_Type = Counter32
_CMediaIndependentHistoryOutBadCRC_Object = MibTableColumn
cMediaIndependentHistoryOutBadCRC = _CMediaIndependentHistoryOutBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 260),
    _CMediaIndependentHistoryOutBadCRC_Type()
)
cMediaIndependentHistoryOutBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutBadCRC.setStatus("current")
_CMediaIndependentHistoryInFramesTruncated_Type = Counter32
_CMediaIndependentHistoryInFramesTruncated_Object = MibTableColumn
cMediaIndependentHistoryInFramesTruncated = _CMediaIndependentHistoryInFramesTruncated_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 270),
    _CMediaIndependentHistoryInFramesTruncated_Type()
)
cMediaIndependentHistoryInFramesTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInFramesTruncated.setStatus("current")
_CMediaIndependentHistoryInFramesTooLong_Type = Counter32
_CMediaIndependentHistoryInFramesTooLong_Object = MibTableColumn
cMediaIndependentHistoryInFramesTooLong = _CMediaIndependentHistoryInFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 280),
    _CMediaIndependentHistoryInFramesTooLong_Type()
)
cMediaIndependentHistoryInFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInFramesTooLong.setStatus("current")
_CMediaIndependentHistoryLinkRecoveries_Type = Counter32
_CMediaIndependentHistoryLinkRecoveries_Object = MibTableColumn
cMediaIndependentHistoryLinkRecoveries = _CMediaIndependentHistoryLinkRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 290),
    _CMediaIndependentHistoryLinkRecoveries_Type()
)
cMediaIndependentHistoryLinkRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryLinkRecoveries.setStatus("current")
_CMediaIndependentHistoryInDistanceExtBuffers_Type = Counter32
_CMediaIndependentHistoryInDistanceExtBuffers_Object = MibTableColumn
cMediaIndependentHistoryInDistanceExtBuffers = _CMediaIndependentHistoryInDistanceExtBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 300),
    _CMediaIndependentHistoryInDistanceExtBuffers_Type()
)
cMediaIndependentHistoryInDistanceExtBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInDistanceExtBuffers.setStatus("current")
_CMediaIndependentHistoryOutDistanceExtBuffers_Type = Counter32
_CMediaIndependentHistoryOutDistanceExtBuffers_Object = MibTableColumn
cMediaIndependentHistoryOutDistanceExtBuffers = _CMediaIndependentHistoryOutDistanceExtBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 310),
    _CMediaIndependentHistoryOutDistanceExtBuffers_Type()
)
cMediaIndependentHistoryOutDistanceExtBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutDistanceExtBuffers.setStatus("current")
_CMediaIndependentHistoryInCredits_Type = Counter32
_CMediaIndependentHistoryInCredits_Object = MibTableColumn
cMediaIndependentHistoryInCredits = _CMediaIndependentHistoryInCredits_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 320),
    _CMediaIndependentHistoryInCredits_Type()
)
cMediaIndependentHistoryInCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInCredits.setStatus("current")
_CMediaIndependentHistoryOutCredits_Type = Counter32
_CMediaIndependentHistoryOutCredits_Object = MibTableColumn
cMediaIndependentHistoryOutCredits = _CMediaIndependentHistoryOutCredits_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 330),
    _CMediaIndependentHistoryOutCredits_Type()
)
cMediaIndependentHistoryOutCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutCredits.setStatus("current")
_CMediaIndependentHistoryOutZeroCredits_Type = Counter32
_CMediaIndependentHistoryOutZeroCredits_Object = MibTableColumn
cMediaIndependentHistoryOutZeroCredits = _CMediaIndependentHistoryOutZeroCredits_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 340),
    _CMediaIndependentHistoryOutZeroCredits_Type()
)
cMediaIndependentHistoryOutZeroCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutZeroCredits.setStatus("current")
_CMediaIndependentHistoryInGfpSBitErr_Type = Counter32
_CMediaIndependentHistoryInGfpSBitErr_Object = MibTableColumn
cMediaIndependentHistoryInGfpSBitErr = _CMediaIndependentHistoryInGfpSBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 350),
    _CMediaIndependentHistoryInGfpSBitErr_Type()
)
cMediaIndependentHistoryInGfpSBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpSBitErr.setStatus("current")
_CMediaIndependentHistoryInGfpMBitErr_Type = Counter32
_CMediaIndependentHistoryInGfpMBitErr_Object = MibTableColumn
cMediaIndependentHistoryInGfpMBitErr = _CMediaIndependentHistoryInGfpMBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 360),
    _CMediaIndependentHistoryInGfpMBitErr_Type()
)
cMediaIndependentHistoryInGfpMBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpMBitErr.setStatus("current")
_CMediaIndependentHistoryInGfpCRCErr_Type = Counter32
_CMediaIndependentHistoryInGfpCRCErr_Object = MibTableColumn
cMediaIndependentHistoryInGfpCRCErr = _CMediaIndependentHistoryInGfpCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 370),
    _CMediaIndependentHistoryInGfpCRCErr_Type()
)
cMediaIndependentHistoryInGfpCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpCRCErr.setStatus("current")
_CMediaIndependentHistoryInGfpFrames_Type = Counter32
_CMediaIndependentHistoryInGfpFrames_Object = MibTableColumn
cMediaIndependentHistoryInGfpFrames = _CMediaIndependentHistoryInGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 380),
    _CMediaIndependentHistoryInGfpFrames_Type()
)
cMediaIndependentHistoryInGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpFrames.setStatus("current")
_CMediaIndependentHistoryInOverflowGfpFrames_Type = Counter32
_CMediaIndependentHistoryInOverflowGfpFrames_Object = MibTableColumn
cMediaIndependentHistoryInOverflowGfpFrames = _CMediaIndependentHistoryInOverflowGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 390),
    _CMediaIndependentHistoryInOverflowGfpFrames_Type()
)
cMediaIndependentHistoryInOverflowGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInOverflowGfpFrames.setStatus("current")
_CMediaIndependentHistoryInHighCapacityGfpFrames_Type = Counter64
_CMediaIndependentHistoryInHighCapacityGfpFrames_Object = MibTableColumn
cMediaIndependentHistoryInHighCapacityGfpFrames = _CMediaIndependentHistoryInHighCapacityGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 400),
    _CMediaIndependentHistoryInHighCapacityGfpFrames_Type()
)
cMediaIndependentHistoryInHighCapacityGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInHighCapacityGfpFrames.setStatus("current")
_CMediaIndependentHistoryOutGfpFrames_Type = Counter32
_CMediaIndependentHistoryOutGfpFrames_Object = MibTableColumn
cMediaIndependentHistoryOutGfpFrames = _CMediaIndependentHistoryOutGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 410),
    _CMediaIndependentHistoryOutGfpFrames_Type()
)
cMediaIndependentHistoryOutGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutGfpFrames.setStatus("current")
_CMediaIndependentHistoryOutOverflowGfpFrames_Type = Counter32
_CMediaIndependentHistoryOutOverflowGfpFrames_Object = MibTableColumn
cMediaIndependentHistoryOutOverflowGfpFrames = _CMediaIndependentHistoryOutOverflowGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 420),
    _CMediaIndependentHistoryOutOverflowGfpFrames_Type()
)
cMediaIndependentHistoryOutOverflowGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutOverflowGfpFrames.setStatus("current")
_CMediaIndependentHistoryOutHighCapacityGfpFrames_Type = Counter64
_CMediaIndependentHistoryOutHighCapacityGfpFrames_Object = MibTableColumn
cMediaIndependentHistoryOutHighCapacityGfpFrames = _CMediaIndependentHistoryOutHighCapacityGfpFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 430),
    _CMediaIndependentHistoryOutHighCapacityGfpFrames_Type()
)
cMediaIndependentHistoryOutHighCapacityGfpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutHighCapacityGfpFrames.setStatus("current")
_CMediaIndependentHistoryInGfpOctets_Type = Counter32
_CMediaIndependentHistoryInGfpOctets_Object = MibTableColumn
cMediaIndependentHistoryInGfpOctets = _CMediaIndependentHistoryInGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 440),
    _CMediaIndependentHistoryInGfpOctets_Type()
)
cMediaIndependentHistoryInGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpOctets.setStatus("current")
_CMediaIndependentHistoryInOverflowGfpOctets_Type = Counter32
_CMediaIndependentHistoryInOverflowGfpOctets_Object = MibTableColumn
cMediaIndependentHistoryInOverflowGfpOctets = _CMediaIndependentHistoryInOverflowGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 450),
    _CMediaIndependentHistoryInOverflowGfpOctets_Type()
)
cMediaIndependentHistoryInOverflowGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInOverflowGfpOctets.setStatus("current")
_CMediaIndependentHistoryInHighCapacityGfpOctets_Type = Counter64
_CMediaIndependentHistoryInHighCapacityGfpOctets_Object = MibTableColumn
cMediaIndependentHistoryInHighCapacityGfpOctets = _CMediaIndependentHistoryInHighCapacityGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 460),
    _CMediaIndependentHistoryInHighCapacityGfpOctets_Type()
)
cMediaIndependentHistoryInHighCapacityGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInHighCapacityGfpOctets.setStatus("current")
_CMediaIndependentHistoryOutGfpOctets_Type = Counter32
_CMediaIndependentHistoryOutGfpOctets_Object = MibTableColumn
cMediaIndependentHistoryOutGfpOctets = _CMediaIndependentHistoryOutGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 470),
    _CMediaIndependentHistoryOutGfpOctets_Type()
)
cMediaIndependentHistoryOutGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutGfpOctets.setStatus("current")
_CMediaIndependentHistoryOutOverflowGfpOctets_Type = Counter32
_CMediaIndependentHistoryOutOverflowGfpOctets_Object = MibTableColumn
cMediaIndependentHistoryOutOverflowGfpOctets = _CMediaIndependentHistoryOutOverflowGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 480),
    _CMediaIndependentHistoryOutOverflowGfpOctets_Type()
)
cMediaIndependentHistoryOutOverflowGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutOverflowGfpOctets.setStatus("current")
_CMediaIndependentHistoryOutHighCapacityGfpOctets_Type = Counter64
_CMediaIndependentHistoryOutHighCapacityGfpOctets_Object = MibTableColumn
cMediaIndependentHistoryOutHighCapacityGfpOctets = _CMediaIndependentHistoryOutHighCapacityGfpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 490),
    _CMediaIndependentHistoryOutHighCapacityGfpOctets_Type()
)
cMediaIndependentHistoryOutHighCapacityGfpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutHighCapacityGfpOctets.setStatus("current")
_CMediaIndependentHistoryInGfpTypeInvalid_Type = Counter32
_CMediaIndependentHistoryInGfpTypeInvalid_Object = MibTableColumn
cMediaIndependentHistoryInGfpTypeInvalid = _CMediaIndependentHistoryInGfpTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 500),
    _CMediaIndependentHistoryInGfpTypeInvalid_Type()
)
cMediaIndependentHistoryInGfpTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpTypeInvalid.setStatus("current")
_CMediaIndependentHistoryInGfpCIDInvalid_Type = Counter32
_CMediaIndependentHistoryInGfpCIDInvalid_Object = MibTableColumn
cMediaIndependentHistoryInGfpCIDInvalid = _CMediaIndependentHistoryInGfpCIDInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 510),
    _CMediaIndependentHistoryInGfpCIDInvalid_Type()
)
cMediaIndependentHistoryInGfpCIDInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpCIDInvalid.setStatus("current")
_CMediaIndependentHistoryInGfpLFDRaised_Type = Counter32
_CMediaIndependentHistoryInGfpLFDRaised_Object = MibTableColumn
cMediaIndependentHistoryInGfpLFDRaised = _CMediaIndependentHistoryInGfpLFDRaised_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 520),
    _CMediaIndependentHistoryInGfpLFDRaised_Type()
)
cMediaIndependentHistoryInGfpLFDRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpLFDRaised.setStatus("current")
_CMediaIndependentHistoryInGfpCSFRaised_Type = Counter32
_CMediaIndependentHistoryInGfpCSFRaised_Object = MibTableColumn
cMediaIndependentHistoryInGfpCSFRaised = _CMediaIndependentHistoryInGfpCSFRaised_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 530),
    _CMediaIndependentHistoryInGfpCSFRaised_Type()
)
cMediaIndependentHistoryInGfpCSFRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpCSFRaised.setStatus("current")
_CMediaIndependentHistoryGfpRoundTripLatency_Type = Counter32
_CMediaIndependentHistoryGfpRoundTripLatency_Object = MibTableColumn
cMediaIndependentHistoryGfpRoundTripLatency = _CMediaIndependentHistoryGfpRoundTripLatency_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 540),
    _CMediaIndependentHistoryGfpRoundTripLatency_Type()
)
cMediaIndependentHistoryGfpRoundTripLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryGfpRoundTripLatency.setStatus("current")
_CMediaIndependentHistory8b10bIdleSets_Type = Counter32
_CMediaIndependentHistory8b10bIdleSets_Object = MibTableColumn
cMediaIndependentHistory8b10bIdleSets = _CMediaIndependentHistory8b10bIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 550),
    _CMediaIndependentHistory8b10bIdleSets_Type()
)
cMediaIndependentHistory8b10bIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bIdleSets.setStatus("current")
_CMediaIndependentHistoryOverflow8b10bIdleSets_Type = Counter32
_CMediaIndependentHistoryOverflow8b10bIdleSets_Object = MibTableColumn
cMediaIndependentHistoryOverflow8b10bIdleSets = _CMediaIndependentHistoryOverflow8b10bIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 560),
    _CMediaIndependentHistoryOverflow8b10bIdleSets_Type()
)
cMediaIndependentHistoryOverflow8b10bIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOverflow8b10bIdleSets.setStatus("current")
_CMediaIndependentHistoryHighCapacity8b10bIdleSets_Type = Counter64
_CMediaIndependentHistoryHighCapacity8b10bIdleSets_Object = MibTableColumn
cMediaIndependentHistoryHighCapacity8b10bIdleSets = _CMediaIndependentHistoryHighCapacity8b10bIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 570),
    _CMediaIndependentHistoryHighCapacity8b10bIdleSets_Type()
)
cMediaIndependentHistoryHighCapacity8b10bIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHighCapacity8b10bIdleSets.setStatus("current")
_CMediaIndependentHistory8b10bNonIdleSets_Type = Counter32
_CMediaIndependentHistory8b10bNonIdleSets_Object = MibTableColumn
cMediaIndependentHistory8b10bNonIdleSets = _CMediaIndependentHistory8b10bNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 580),
    _CMediaIndependentHistory8b10bNonIdleSets_Type()
)
cMediaIndependentHistory8b10bNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bNonIdleSets.setStatus("current")
_CMediaIndependentHistoryOverflow8b10bNonIdleSets_Type = Counter32
_CMediaIndependentHistoryOverflow8b10bNonIdleSets_Object = MibTableColumn
cMediaIndependentHistoryOverflow8b10bNonIdleSets = _CMediaIndependentHistoryOverflow8b10bNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 590),
    _CMediaIndependentHistoryOverflow8b10bNonIdleSets_Type()
)
cMediaIndependentHistoryOverflow8b10bNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOverflow8b10bNonIdleSets.setStatus("current")
_CMediaIndependentHistoryHighCapacity8b10bNonIdleSets_Type = Counter64
_CMediaIndependentHistoryHighCapacity8b10bNonIdleSets_Object = MibTableColumn
cMediaIndependentHistoryHighCapacity8b10bNonIdleSets = _CMediaIndependentHistoryHighCapacity8b10bNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 600),
    _CMediaIndependentHistoryHighCapacity8b10bNonIdleSets_Type()
)
cMediaIndependentHistoryHighCapacity8b10bNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHighCapacity8b10bNonIdleSets.setStatus("current")
_CMediaIndependentHistory8b10bDataSets_Type = Counter32
_CMediaIndependentHistory8b10bDataSets_Object = MibTableColumn
cMediaIndependentHistory8b10bDataSets = _CMediaIndependentHistory8b10bDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 610),
    _CMediaIndependentHistory8b10bDataSets_Type()
)
cMediaIndependentHistory8b10bDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bDataSets.setStatus("current")
_CMediaIndependentHistoryOverflow8b10bDataSets_Type = Counter32
_CMediaIndependentHistoryOverflow8b10bDataSets_Object = MibTableColumn
cMediaIndependentHistoryOverflow8b10bDataSets = _CMediaIndependentHistoryOverflow8b10bDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 620),
    _CMediaIndependentHistoryOverflow8b10bDataSets_Type()
)
cMediaIndependentHistoryOverflow8b10bDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOverflow8b10bDataSets.setStatus("current")
_CMediaIndependentHistoryHighCapacity8b10bDataSets_Type = Counter64
_CMediaIndependentHistoryHighCapacity8b10bDataSets_Object = MibTableColumn
cMediaIndependentHistoryHighCapacity8b10bDataSets = _CMediaIndependentHistoryHighCapacity8b10bDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 630),
    _CMediaIndependentHistoryHighCapacity8b10bDataSets_Type()
)
cMediaIndependentHistoryHighCapacity8b10bDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHighCapacity8b10bDataSets.setStatus("current")
_CMediaIndependentHistory8b10bInvalidOrdSets_Type = Counter32
_CMediaIndependentHistory8b10bInvalidOrdSets_Object = MibTableColumn
cMediaIndependentHistory8b10bInvalidOrdSets = _CMediaIndependentHistory8b10bInvalidOrdSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 640),
    _CMediaIndependentHistory8b10bInvalidOrdSets_Type()
)
cMediaIndependentHistory8b10bInvalidOrdSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bInvalidOrdSets.setStatus("current")
_CMediaIndependentHistory8b10bEncodingDispErr_Type = Counter32
_CMediaIndependentHistory8b10bEncodingDispErr_Object = MibTableColumn
cMediaIndependentHistory8b10bEncodingDispErr = _CMediaIndependentHistory8b10bEncodingDispErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 650),
    _CMediaIndependentHistory8b10bEncodingDispErr_Type()
)
cMediaIndependentHistory8b10bEncodingDispErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bEncodingDispErr.setStatus("current")
_CMediaIndependentHistory8b10bLossOfSync_Type = Counter32
_CMediaIndependentHistory8b10bLossOfSync_Object = MibTableColumn
cMediaIndependentHistory8b10bLossOfSync = _CMediaIndependentHistory8b10bLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 660),
    _CMediaIndependentHistory8b10bLossOfSync_Type()
)
cMediaIndependentHistory8b10bLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bLossOfSync.setStatus("current")
_CMediaIndependentHistoryInPauseFrames_Type = Counter32
_CMediaIndependentHistoryInPauseFrames_Object = MibTableColumn
cMediaIndependentHistoryInPauseFrames = _CMediaIndependentHistoryInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 670),
    _CMediaIndependentHistoryInPauseFrames_Type()
)
cMediaIndependentHistoryInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInPauseFrames.setStatus("current")
_CMediaIndependentHistoryOutPauseFrames_Type = Counter32
_CMediaIndependentHistoryOutPauseFrames_Object = MibTableColumn
cMediaIndependentHistoryOutPauseFrames = _CMediaIndependentHistoryOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 680),
    _CMediaIndependentHistoryOutPauseFrames_Type()
)
cMediaIndependentHistoryOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutPauseFrames.setStatus("current")
_CMediaIndependentHistoryInPktsDroppedInternalCongestion_Type = Counter32
_CMediaIndependentHistoryInPktsDroppedInternalCongestion_Object = MibTableColumn
cMediaIndependentHistoryInPktsDroppedInternalCongestion = _CMediaIndependentHistoryInPktsDroppedInternalCongestion_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 690),
    _CMediaIndependentHistoryInPktsDroppedInternalCongestion_Type()
)
cMediaIndependentHistoryInPktsDroppedInternalCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInPktsDroppedInternalCongestion.setStatus("current")
_CMediaIndependentHistoryOutPktsDroppedInternalCongestion_Type = Counter32
_CMediaIndependentHistoryOutPktsDroppedInternalCongestion_Object = MibTableColumn
cMediaIndependentHistoryOutPktsDroppedInternalCongestion = _CMediaIndependentHistoryOutPktsDroppedInternalCongestion_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 700),
    _CMediaIndependentHistoryOutPktsDroppedInternalCongestion_Type()
)
cMediaIndependentHistoryOutPktsDroppedInternalCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutPktsDroppedInternalCongestion.setStatus("current")
_CMediaIndependentHistoryInControlFrames_Type = Counter32
_CMediaIndependentHistoryInControlFrames_Object = MibTableColumn
cMediaIndependentHistoryInControlFrames = _CMediaIndependentHistoryInControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 710),
    _CMediaIndependentHistoryInControlFrames_Type()
)
cMediaIndependentHistoryInControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInControlFrames.setStatus("current")
_CMediaIndependentHistoryInUnknownOpcodeFrames_Type = Counter32
_CMediaIndependentHistoryInUnknownOpcodeFrames_Object = MibTableColumn
cMediaIndependentHistoryInUnknownOpcodeFrames = _CMediaIndependentHistoryInUnknownOpcodeFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 720),
    _CMediaIndependentHistoryInUnknownOpcodeFrames_Type()
)
cMediaIndependentHistoryInUnknownOpcodeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInUnknownOpcodeFrames.setStatus("current")
_CMediaIndependentHistoryHdlcPktDrops_Type = Counter32
_CMediaIndependentHistoryHdlcPktDrops_Object = MibTableColumn
cMediaIndependentHistoryHdlcPktDrops = _CMediaIndependentHistoryHdlcPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 730),
    _CMediaIndependentHistoryHdlcPktDrops_Type()
)
cMediaIndependentHistoryHdlcPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHdlcPktDrops.setStatus("current")
_CMediaIndependentHistoryHdlcInOctets_Type = Counter32
_CMediaIndependentHistoryHdlcInOctets_Object = MibTableColumn
cMediaIndependentHistoryHdlcInOctets = _CMediaIndependentHistoryHdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 740),
    _CMediaIndependentHistoryHdlcInOctets_Type()
)
cMediaIndependentHistoryHdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHdlcInOctets.setStatus("current")
_CMediaIndependentHistoryHdlcOutOctets_Type = Counter32
_CMediaIndependentHistoryHdlcOutOctets_Object = MibTableColumn
cMediaIndependentHistoryHdlcOutOctets = _CMediaIndependentHistoryHdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 750),
    _CMediaIndependentHistoryHdlcOutOctets_Type()
)
cMediaIndependentHistoryHdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHdlcOutOctets.setStatus("current")
_CMediaIndependentHistoryHdlcInAborts_Type = Counter32
_CMediaIndependentHistoryHdlcInAborts_Object = MibTableColumn
cMediaIndependentHistoryHdlcInAborts = _CMediaIndependentHistoryHdlcInAborts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 760),
    _CMediaIndependentHistoryHdlcInAborts_Type()
)
cMediaIndependentHistoryHdlcInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryHdlcInAborts.setStatus("current")
_CMediaIndependentHistoryInShortPkts_Type = Counter32
_CMediaIndependentHistoryInShortPkts_Object = MibTableColumn
cMediaIndependentHistoryInShortPkts = _CMediaIndependentHistoryInShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 770),
    _CMediaIndependentHistoryInShortPkts_Type()
)
cMediaIndependentHistoryInShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInShortPkts.setStatus("current")
_CMediaIndependentHistoryOutShortPkts_Type = Counter32
_CMediaIndependentHistoryOutShortPkts_Object = MibTableColumn
cMediaIndependentHistoryOutShortPkts = _CMediaIndependentHistoryOutShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 775),
    _CMediaIndependentHistoryOutShortPkts_Type()
)
cMediaIndependentHistoryOutShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutShortPkts.setStatus("current")
_CMediaIndependentHistoryOversizeDropped_Type = Counter32
_CMediaIndependentHistoryOversizeDropped_Object = MibTableColumn
cMediaIndependentHistoryOversizeDropped = _CMediaIndependentHistoryOversizeDropped_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 780),
    _CMediaIndependentHistoryOversizeDropped_Type()
)
cMediaIndependentHistoryOversizeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOversizeDropped.setStatus("current")
_CMediaIndependentHistoryInErrorBytePkts_Type = Counter32
_CMediaIndependentHistoryInErrorBytePkts_Object = MibTableColumn
cMediaIndependentHistoryInErrorBytePkts = _CMediaIndependentHistoryInErrorBytePkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 790),
    _CMediaIndependentHistoryInErrorBytePkts_Type()
)
cMediaIndependentHistoryInErrorBytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInErrorBytePkts.setStatus("current")
_CMediaIndependentHistoryInFramingErrorPkts_Type = Counter32
_CMediaIndependentHistoryInFramingErrorPkts_Object = MibTableColumn
cMediaIndependentHistoryInFramingErrorPkts = _CMediaIndependentHistoryInFramingErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 800),
    _CMediaIndependentHistoryInFramingErrorPkts_Type()
)
cMediaIndependentHistoryInFramingErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInFramingErrorPkts.setStatus("current")
_CMediaIndependentHistoryInJunkInterPkts_Type = Counter32
_CMediaIndependentHistoryInJunkInterPkts_Object = MibTableColumn
cMediaIndependentHistoryInJunkInterPkts = _CMediaIndependentHistoryInJunkInterPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 810),
    _CMediaIndependentHistoryInJunkInterPkts_Type()
)
cMediaIndependentHistoryInJunkInterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInJunkInterPkts.setStatus("current")
_CMediaIndependentHistoryOutOversizePkts_Type = Counter32
_CMediaIndependentHistoryOutOversizePkts_Object = MibTableColumn
cMediaIndependentHistoryOutOversizePkts = _CMediaIndependentHistoryOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 820),
    _CMediaIndependentHistoryOutOversizePkts_Type()
)
cMediaIndependentHistoryOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutOversizePkts.setStatus("current")
_CMediaIndependentHistoryInPayloadCrcErrors_Type = Counter32
_CMediaIndependentHistoryInPayloadCrcErrors_Object = MibTableColumn
cMediaIndependentHistoryInPayloadCrcErrors = _CMediaIndependentHistoryInPayloadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 830),
    _CMediaIndependentHistoryInPayloadCrcErrors_Type()
)
cMediaIndependentHistoryInPayloadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInPayloadCrcErrors.setStatus("current")
_CMediaIndependentHistoryOutPayloadCrcErrors_Type = Counter32
_CMediaIndependentHistoryOutPayloadCrcErrors_Object = MibTableColumn
cMediaIndependentHistoryOutPayloadCrcErrors = _CMediaIndependentHistoryOutPayloadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 840),
    _CMediaIndependentHistoryOutPayloadCrcErrors_Type()
)
cMediaIndependentHistoryOutPayloadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutPayloadCrcErrors.setStatus("current")
_CMediaIndependentHistoryInRecvrReady_Type = Counter32
_CMediaIndependentHistoryInRecvrReady_Object = MibTableColumn
cMediaIndependentHistoryInRecvrReady = _CMediaIndependentHistoryInRecvrReady_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 850),
    _CMediaIndependentHistoryInRecvrReady_Type()
)
cMediaIndependentHistoryInRecvrReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInRecvrReady.setStatus("current")
_CMediaIndependentHistoryOutRecvrReady_Type = Counter32
_CMediaIndependentHistoryOutRecvrReady_Object = MibTableColumn
cMediaIndependentHistoryOutRecvrReady = _CMediaIndependentHistoryOutRecvrReady_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 860),
    _CMediaIndependentHistoryOutRecvrReady_Type()
)
cMediaIndependentHistoryOutRecvrReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutRecvrReady.setStatus("current")
_CMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum_Type = Counter32
_CMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum_Object = MibTableColumn
cMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum = _CMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 870),
    _CMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum_Type()
)
cMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum.setStatus("current")
_CMediaIndependentHistoryInGfpSblkCRCErr_Type = Counter32
_CMediaIndependentHistoryInGfpSblkCRCErr_Object = MibTableColumn
cMediaIndependentHistoryInGfpSblkCRCErr = _CMediaIndependentHistoryInGfpSblkCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 880),
    _CMediaIndependentHistoryInGfpSblkCRCErr_Type()
)
cMediaIndependentHistoryInGfpSblkCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryInGfpSblkCRCErr.setStatus("current")
_CMediaIndependentHistoryOutFramesTooLong_Type = Counter32
_CMediaIndependentHistoryOutFramesTooLong_Object = MibTableColumn
cMediaIndependentHistoryOutFramesTooLong = _CMediaIndependentHistoryOutFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 890),
    _CMediaIndependentHistoryOutFramesTooLong_Type()
)
cMediaIndependentHistoryOutFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutFramesTooLong.setStatus("current")
_CMediaIndependentHistoryPkts1519to1522Octets_Type = Counter32
_CMediaIndependentHistoryPkts1519to1522Octets_Object = MibTableColumn
cMediaIndependentHistoryPkts1519to1522Octets = _CMediaIndependentHistoryPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 900),
    _CMediaIndependentHistoryPkts1519to1522Octets_Type()
)
cMediaIndependentHistoryPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPkts1519to1522Octets.setStatus("current")
_CMediaIndependentHistoryOutFramesTruncated_Type = Counter32
_CMediaIndependentHistoryOutFramesTruncated_Object = MibTableColumn
cMediaIndependentHistoryOutFramesTruncated = _CMediaIndependentHistoryOutFramesTruncated_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 910),
    _CMediaIndependentHistoryOutFramesTruncated_Type()
)
cMediaIndependentHistoryOutFramesTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryOutFramesTruncated.setStatus("current")
_CMediaIndependentHistoryPcsErrCount_Type = Counter32
_CMediaIndependentHistoryPcsErrCount_Object = MibTableColumn
cMediaIndependentHistoryPcsErrCount = _CMediaIndependentHistoryPcsErrCount_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 920),
    _CMediaIndependentHistoryPcsErrCount_Type()
)
cMediaIndependentHistoryPcsErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPcsErrCount.setStatus("current")
_CMediaIndependentHistoryPcsErrCount2_Type = Counter32
_CMediaIndependentHistoryPcsErrCount2_Object = MibTableColumn
cMediaIndependentHistoryPcsErrCount2 = _CMediaIndependentHistoryPcsErrCount2_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 930),
    _CMediaIndependentHistoryPcsErrCount2_Type()
)
cMediaIndependentHistoryPcsErrCount2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPcsErrCount2.setStatus("current")
_CMediaIndependentHistoryPcs49RxErrBer_Type = Counter32
_CMediaIndependentHistoryPcs49RxErrBer_Object = MibTableColumn
cMediaIndependentHistoryPcs49RxErrBer = _CMediaIndependentHistoryPcs49RxErrBer_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 940),
    _CMediaIndependentHistoryPcs49RxErrBer_Type()
)
cMediaIndependentHistoryPcs49RxErrBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPcs49RxErrBer.setStatus("current")
_CMediaIndependentHistoryPcs49RxErrDec_Type = Counter32
_CMediaIndependentHistoryPcs49RxErrDec_Object = MibTableColumn
cMediaIndependentHistoryPcs49RxErrDec = _CMediaIndependentHistoryPcs49RxErrDec_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 950),
    _CMediaIndependentHistoryPcs49RxErrDec_Type()
)
cMediaIndependentHistoryPcs49RxErrDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPcs49RxErrDec.setStatus("current")
_CMediaIndependentHistoryPkts1519toMaxOctets_Type = Counter32
_CMediaIndependentHistoryPkts1519toMaxOctets_Object = MibTableColumn
cMediaIndependentHistoryPkts1519toMaxOctets = _CMediaIndependentHistoryPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 960),
    _CMediaIndependentHistoryPkts1519toMaxOctets_Type()
)
cMediaIndependentHistoryPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPkts1519toMaxOctets.setStatus("current")
_CMediaIndependentHistoryRxLcvErrors_Type = Counter32
_CMediaIndependentHistoryRxLcvErrors_Object = MibTableColumn
cMediaIndependentHistoryRxLcvErrors = _CMediaIndependentHistoryRxLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 970),
    _CMediaIndependentHistoryRxLcvErrors_Type()
)
cMediaIndependentHistoryRxLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryRxLcvErrors.setStatus("current")
_CMediaIndependentHistoryTxLcvErrors_Type = Counter32
_CMediaIndependentHistoryTxLcvErrors_Object = MibTableColumn
cMediaIndependentHistoryTxLcvErrors = _CMediaIndependentHistoryTxLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 980),
    _CMediaIndependentHistoryTxLcvErrors_Type()
)
cMediaIndependentHistoryTxLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryTxLcvErrors.setStatus("current")
_CMediaIndependentHistoryPcsEgRxErrFrames_Type = Counter32
_CMediaIndependentHistoryPcsEgRxErrFrames_Object = MibTableColumn
cMediaIndependentHistoryPcsEgRxErrFrames = _CMediaIndependentHistoryPcsEgRxErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 70, 10, 30, 1, 990),
    _CMediaIndependentHistoryPcsEgRxErrFrames_Type()
)
cMediaIndependentHistoryPcsEgRxErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMediaIndependentHistoryPcsEgRxErrFrames.setStatus("current")
_CerentHcRmonMIBConformance_ObjectIdentity = ObjectIdentity
cerentHcRmonMIBConformance = _CerentHcRmonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60)
)
_CerentHcRmonMIBCompliances_ObjectIdentity = ObjectIdentity
cerentHcRmonMIBCompliances = _CerentHcRmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60, 10)
)
_CerentHcRmonMIBGroups_ObjectIdentity = ObjectIdentity
cerentHcRmonMIBGroups = _CerentHcRmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60, 20)
)

# Managed Objects groups

cMediaIndependentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60, 20, 10)
)
cMediaIndependentGroup.setObjects(
      *(("CERENT-HC-RMON-MIB", "cMediaIndependentInBadCRC"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutBadCRC"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInFramesTruncated"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInFramesTooLong"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentLinkRecoveries"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInDistanceExtBuffers"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutDistanceExtBuffers"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInCredits"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutCredits"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutZeroCredits"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpSBitErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpMBitErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpCRCErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInOverflowGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInHighCapacityGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutOverflowGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutHighCapacityGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInOverflowGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInHighCapacityGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutOverflowGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutHighCapacityGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpTypeInvalid"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpCIDInvalid"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpLFDRaised"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpCSFRaised"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentGfpRoundTripLatency"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOverflow8b10bIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHighCapacity8b10bIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bNonIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOverflow8b10bNonIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHighCapacity8b10bNonIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bDataSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOverflow8b10bDataSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHighCapacity8b10bDataSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bInvalidOrdSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bEncodingDispErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bLossOfSync"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInPauseFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutPauseFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInPktsDroppedInternalCongestion"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutPktsDroppedInternalCongestion"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInControlFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInUnknownOpcodeFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHdlcPktDrops"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHdlcInOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHdlcOutOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHdlcInAborts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInShortPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutShortPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOversizeDropped"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInErrorBytePkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInFramingErrorPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInJunkInterPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutOversizePkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInPayloadCrcErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutPayloadCrcErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInRecvrReady"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutRecvrReady"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependent8b10bInvalidOrdSetsDispErrorsSum"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentInGfpSblkCRCErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutFramesTooLong"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPkts1519to1522Octets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentOutFramesTruncated"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPcsErrCount"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPcsErrCount2"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPcs49RxErrBer"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPcs49RxErrDec"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPkts1519toMaxOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentRxLcvErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentTxLcvErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentGfpRxCmfFrame"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentGfpTxCmfFrame"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentPcsEgRxErrFrames"))
)
if mibBuilder.loadTexts:
    cMediaIndependentGroup.setStatus("current")

cMediaIndependenHistoryControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60, 20, 20)
)
cMediaIndependenHistoryControlGroup.setObjects(
      *(("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlDataSource"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlBucketsRequested"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlBucketsGranted"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlInterval"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlOwner"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryControlStatus"))
)
if mibBuilder.loadTexts:
    cMediaIndependenHistoryControlGroup.setStatus("current")

cMediaIndependentHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60, 20, 30)
)
cMediaIndependentHistoryGroup.setObjects(
      *(("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryDropEvents"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryDroppedFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInOverflowPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInHighCapacityPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutOverflowPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutHighCapacityPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInOverflowOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInHighCapacityOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutOverflowOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutHighCapacityOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInNUCastPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInNUCastOverflowPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInNUCastHighCapacityPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutNUCastPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutNUCastOverflowPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutNUCastHighCapacityPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInBadCRC"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutBadCRC"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInFramesTruncated"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInFramesTooLong"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryLinkRecoveries"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInDistanceExtBuffers"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutDistanceExtBuffers"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInCredits"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutCredits"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutZeroCredits"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpSBitErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpMBitErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpCRCErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInOverflowGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInHighCapacityGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutOverflowGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutHighCapacityGfpFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInOverflowGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInHighCapacityGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutOverflowGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutHighCapacityGfpOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpTypeInvalid"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpCIDInvalid"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpLFDRaised"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpCSFRaised"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryGfpRoundTripLatency"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOverflow8b10bIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHighCapacity8b10bIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bNonIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOverflow8b10bNonIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHighCapacity8b10bNonIdleSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bDataSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOverflow8b10bDataSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHighCapacity8b10bDataSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bInvalidOrdSets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bEncodingDispErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bLossOfSync"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInPauseFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutPauseFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInPktsDroppedInternalCongestion"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutPktsDroppedInternalCongestion"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInControlFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInUnknownOpcodeFrames"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHdlcPktDrops"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHdlcInOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHdlcOutOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryHdlcInAborts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInShortPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutShortPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOversizeDropped"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInErrorBytePkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInFramingErrorPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInJunkInterPkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutOversizePkts"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInPayloadCrcErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutPayloadCrcErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInRecvrReady"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutRecvrReady"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryInGfpSblkCRCErr"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutFramesTooLong"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPkts1519to1522Octets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryOutFramesTruncated"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPcsErrCount"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPcsErrCount2"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPcs49RxErrBer"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPcs49RxErrDec"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPkts1519toMaxOctets"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryRxLcvErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryTxLcvErrors"),
        ("CERENT-HC-RMON-MIB", "cMediaIndependentHistoryPcsEgRxErrFrames"))
)
if mibBuilder.loadTexts:
    cMediaIndependentHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentHcMediaIndependentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 60, 10, 10)
)
if mibBuilder.loadTexts:
    cerentHcMediaIndependentCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-HC-RMON-MIB",
    **{"cerentHcRMON": cerentHcRMON,
       "cerentHcRmonMIBObjects": cerentHcRmonMIBObjects,
       "cerentHcRmon": cerentHcRmon,
       "cMediaIndependentTable": cMediaIndependentTable,
       "cMediaIndependentEntry": cMediaIndependentEntry,
       "cMediaIndependentInBadCRC": cMediaIndependentInBadCRC,
       "cMediaIndependentOutBadCRC": cMediaIndependentOutBadCRC,
       "cMediaIndependentInFramesTruncated": cMediaIndependentInFramesTruncated,
       "cMediaIndependentInFramesTooLong": cMediaIndependentInFramesTooLong,
       "cMediaIndependentLinkRecoveries": cMediaIndependentLinkRecoveries,
       "cMediaIndependentInDistanceExtBuffers": cMediaIndependentInDistanceExtBuffers,
       "cMediaIndependentOutDistanceExtBuffers": cMediaIndependentOutDistanceExtBuffers,
       "cMediaIndependentInCredits": cMediaIndependentInCredits,
       "cMediaIndependentOutCredits": cMediaIndependentOutCredits,
       "cMediaIndependentOutZeroCredits": cMediaIndependentOutZeroCredits,
       "cMediaIndependentInGfpSBitErr": cMediaIndependentInGfpSBitErr,
       "cMediaIndependentInGfpMBitErr": cMediaIndependentInGfpMBitErr,
       "cMediaIndependentInGfpCRCErr": cMediaIndependentInGfpCRCErr,
       "cMediaIndependentInGfpFrames": cMediaIndependentInGfpFrames,
       "cMediaIndependentInOverflowGfpFrames": cMediaIndependentInOverflowGfpFrames,
       "cMediaIndependentInHighCapacityGfpFrames": cMediaIndependentInHighCapacityGfpFrames,
       "cMediaIndependentOutGfpFrames": cMediaIndependentOutGfpFrames,
       "cMediaIndependentOutOverflowGfpFrames": cMediaIndependentOutOverflowGfpFrames,
       "cMediaIndependentOutHighCapacityGfpFrames": cMediaIndependentOutHighCapacityGfpFrames,
       "cMediaIndependentInGfpOctets": cMediaIndependentInGfpOctets,
       "cMediaIndependentInOverflowGfpOctets": cMediaIndependentInOverflowGfpOctets,
       "cMediaIndependentInHighCapacityGfpOctets": cMediaIndependentInHighCapacityGfpOctets,
       "cMediaIndependentOutGfpOctets": cMediaIndependentOutGfpOctets,
       "cMediaIndependentOutOverflowGfpOctets": cMediaIndependentOutOverflowGfpOctets,
       "cMediaIndependentOutHighCapacityGfpOctets": cMediaIndependentOutHighCapacityGfpOctets,
       "cMediaIndependentInGfpTypeInvalid": cMediaIndependentInGfpTypeInvalid,
       "cMediaIndependentInGfpCIDInvalid": cMediaIndependentInGfpCIDInvalid,
       "cMediaIndependentInGfpLFDRaised": cMediaIndependentInGfpLFDRaised,
       "cMediaIndependentInGfpCSFRaised": cMediaIndependentInGfpCSFRaised,
       "cMediaIndependentGfpRoundTripLatency": cMediaIndependentGfpRoundTripLatency,
       "cMediaIndependent8b10bIdleSets": cMediaIndependent8b10bIdleSets,
       "cMediaIndependentOverflow8b10bIdleSets": cMediaIndependentOverflow8b10bIdleSets,
       "cMediaIndependentHighCapacity8b10bIdleSets": cMediaIndependentHighCapacity8b10bIdleSets,
       "cMediaIndependent8b10bNonIdleSets": cMediaIndependent8b10bNonIdleSets,
       "cMediaIndependentOverflow8b10bNonIdleSets": cMediaIndependentOverflow8b10bNonIdleSets,
       "cMediaIndependentHighCapacity8b10bNonIdleSets": cMediaIndependentHighCapacity8b10bNonIdleSets,
       "cMediaIndependent8b10bDataSets": cMediaIndependent8b10bDataSets,
       "cMediaIndependentOverflow8b10bDataSets": cMediaIndependentOverflow8b10bDataSets,
       "cMediaIndependentHighCapacity8b10bDataSets": cMediaIndependentHighCapacity8b10bDataSets,
       "cMediaIndependent8b10bInvalidOrdSets": cMediaIndependent8b10bInvalidOrdSets,
       "cMediaIndependent8b10bEncodingDispErr": cMediaIndependent8b10bEncodingDispErr,
       "cMediaIndependent8b10bLossOfSync": cMediaIndependent8b10bLossOfSync,
       "cMediaIndependentInPauseFrames": cMediaIndependentInPauseFrames,
       "cMediaIndependentOutPauseFrames": cMediaIndependentOutPauseFrames,
       "cMediaIndependentInPktsDroppedInternalCongestion": cMediaIndependentInPktsDroppedInternalCongestion,
       "cMediaIndependentOutPktsDroppedInternalCongestion": cMediaIndependentOutPktsDroppedInternalCongestion,
       "cMediaIndependentInControlFrames": cMediaIndependentInControlFrames,
       "cMediaIndependentInUnknownOpcodeFrames": cMediaIndependentInUnknownOpcodeFrames,
       "cMediaIndependentHdlcPktDrops": cMediaIndependentHdlcPktDrops,
       "cMediaIndependentHdlcInOctets": cMediaIndependentHdlcInOctets,
       "cMediaIndependentHdlcOutOctets": cMediaIndependentHdlcOutOctets,
       "cMediaIndependentHdlcInAborts": cMediaIndependentHdlcInAborts,
       "cMediaIndependentInShortPkts": cMediaIndependentInShortPkts,
       "cMediaIndependentOutShortPkts": cMediaIndependentOutShortPkts,
       "cMediaIndependentOversizeDropped": cMediaIndependentOversizeDropped,
       "cMediaIndependentInErrorBytePkts": cMediaIndependentInErrorBytePkts,
       "cMediaIndependentInFramingErrorPkts": cMediaIndependentInFramingErrorPkts,
       "cMediaIndependentInJunkInterPkts": cMediaIndependentInJunkInterPkts,
       "cMediaIndependentOutOversizePkts": cMediaIndependentOutOversizePkts,
       "cMediaIndependentInPayloadCrcErrors": cMediaIndependentInPayloadCrcErrors,
       "cMediaIndependentOutPayloadCrcErrors": cMediaIndependentOutPayloadCrcErrors,
       "cMediaIndependentInRecvrReady": cMediaIndependentInRecvrReady,
       "cMediaIndependentOutRecvrReady": cMediaIndependentOutRecvrReady,
       "cMediaIndependent8b10bInvalidOrdSetsDispErrorsSum": cMediaIndependent8b10bInvalidOrdSetsDispErrorsSum,
       "cMediaIndependentInGfpSblkCRCErr": cMediaIndependentInGfpSblkCRCErr,
       "cMediaIndependentOutFramesTooLong": cMediaIndependentOutFramesTooLong,
       "cMediaIndependentPkts1519to1522Octets": cMediaIndependentPkts1519to1522Octets,
       "cMediaIndependentOutFramesTruncated": cMediaIndependentOutFramesTruncated,
       "cMediaIndependentPcsErrCount": cMediaIndependentPcsErrCount,
       "cMediaIndependentPcsErrCount2": cMediaIndependentPcsErrCount2,
       "cMediaIndependentPcs49RxErrBer": cMediaIndependentPcs49RxErrBer,
       "cMediaIndependentPcs49RxErrDec": cMediaIndependentPcs49RxErrDec,
       "cMediaIndependentPkts1519toMaxOctets": cMediaIndependentPkts1519toMaxOctets,
       "cMediaIndependentRxLcvErrors": cMediaIndependentRxLcvErrors,
       "cMediaIndependentTxLcvErrors": cMediaIndependentTxLcvErrors,
       "cMediaIndependentGfpRxCmfFrame": cMediaIndependentGfpRxCmfFrame,
       "cMediaIndependentGfpTxCmfFrame": cMediaIndependentGfpTxCmfFrame,
       "cMediaIndependentPcsEgRxErrFrames": cMediaIndependentPcsEgRxErrFrames,
       "cMediaIndependentHistoryControlTable": cMediaIndependentHistoryControlTable,
       "cMediaIndependentHistoryControlEntry": cMediaIndependentHistoryControlEntry,
       "cMediaIndependentHistoryControlIndex": cMediaIndependentHistoryControlIndex,
       "cMediaIndependentHistoryControlDataSource": cMediaIndependentHistoryControlDataSource,
       "cMediaIndependentHistoryControlBucketsRequested": cMediaIndependentHistoryControlBucketsRequested,
       "cMediaIndependentHistoryControlBucketsGranted": cMediaIndependentHistoryControlBucketsGranted,
       "cMediaIndependentHistoryControlInterval": cMediaIndependentHistoryControlInterval,
       "cMediaIndependentHistoryControlOwner": cMediaIndependentHistoryControlOwner,
       "cMediaIndependentHistoryControlStatus": cMediaIndependentHistoryControlStatus,
       "cMediaIndependentHistoryTable": cMediaIndependentHistoryTable,
       "cMediaIndependentHistoryEntry": cMediaIndependentHistoryEntry,
       "cMediaIndependentHistoryIndex": cMediaIndependentHistoryIndex,
       "cMediaIndependentHistorySampleIndex": cMediaIndependentHistorySampleIndex,
       "cMediaIndependentHistoryDropEvents": cMediaIndependentHistoryDropEvents,
       "cMediaIndependentHistoryDroppedFrames": cMediaIndependentHistoryDroppedFrames,
       "cMediaIndependentHistoryInPkts": cMediaIndependentHistoryInPkts,
       "cMediaIndependentHistoryInOverflowPkts": cMediaIndependentHistoryInOverflowPkts,
       "cMediaIndependentHistoryInHighCapacityPkts": cMediaIndependentHistoryInHighCapacityPkts,
       "cMediaIndependentHistoryOutPkts": cMediaIndependentHistoryOutPkts,
       "cMediaIndependentHistoryOutOverflowPkts": cMediaIndependentHistoryOutOverflowPkts,
       "cMediaIndependentHistoryOutHighCapacityPkts": cMediaIndependentHistoryOutHighCapacityPkts,
       "cMediaIndependentHistoryInOctets": cMediaIndependentHistoryInOctets,
       "cMediaIndependentHistoryInOverflowOctets": cMediaIndependentHistoryInOverflowOctets,
       "cMediaIndependentHistoryInHighCapacityOctets": cMediaIndependentHistoryInHighCapacityOctets,
       "cMediaIndependentHistoryOutOctets": cMediaIndependentHistoryOutOctets,
       "cMediaIndependentHistoryOutOverflowOctets": cMediaIndependentHistoryOutOverflowOctets,
       "cMediaIndependentHistoryOutHighCapacityOctets": cMediaIndependentHistoryOutHighCapacityOctets,
       "cMediaIndependentHistoryInNUCastPkts": cMediaIndependentHistoryInNUCastPkts,
       "cMediaIndependentHistoryInNUCastOverflowPkts": cMediaIndependentHistoryInNUCastOverflowPkts,
       "cMediaIndependentHistoryInNUCastHighCapacityPkts": cMediaIndependentHistoryInNUCastHighCapacityPkts,
       "cMediaIndependentHistoryOutNUCastPkts": cMediaIndependentHistoryOutNUCastPkts,
       "cMediaIndependentHistoryOutNUCastOverflowPkts": cMediaIndependentHistoryOutNUCastOverflowPkts,
       "cMediaIndependentHistoryOutNUCastHighCapacityPkts": cMediaIndependentHistoryOutNUCastHighCapacityPkts,
       "cMediaIndependentHistoryInErrors": cMediaIndependentHistoryInErrors,
       "cMediaIndependentHistoryOutErrors": cMediaIndependentHistoryOutErrors,
       "cMediaIndependentHistoryInBadCRC": cMediaIndependentHistoryInBadCRC,
       "cMediaIndependentHistoryOutBadCRC": cMediaIndependentHistoryOutBadCRC,
       "cMediaIndependentHistoryInFramesTruncated": cMediaIndependentHistoryInFramesTruncated,
       "cMediaIndependentHistoryInFramesTooLong": cMediaIndependentHistoryInFramesTooLong,
       "cMediaIndependentHistoryLinkRecoveries": cMediaIndependentHistoryLinkRecoveries,
       "cMediaIndependentHistoryInDistanceExtBuffers": cMediaIndependentHistoryInDistanceExtBuffers,
       "cMediaIndependentHistoryOutDistanceExtBuffers": cMediaIndependentHistoryOutDistanceExtBuffers,
       "cMediaIndependentHistoryInCredits": cMediaIndependentHistoryInCredits,
       "cMediaIndependentHistoryOutCredits": cMediaIndependentHistoryOutCredits,
       "cMediaIndependentHistoryOutZeroCredits": cMediaIndependentHistoryOutZeroCredits,
       "cMediaIndependentHistoryInGfpSBitErr": cMediaIndependentHistoryInGfpSBitErr,
       "cMediaIndependentHistoryInGfpMBitErr": cMediaIndependentHistoryInGfpMBitErr,
       "cMediaIndependentHistoryInGfpCRCErr": cMediaIndependentHistoryInGfpCRCErr,
       "cMediaIndependentHistoryInGfpFrames": cMediaIndependentHistoryInGfpFrames,
       "cMediaIndependentHistoryInOverflowGfpFrames": cMediaIndependentHistoryInOverflowGfpFrames,
       "cMediaIndependentHistoryInHighCapacityGfpFrames": cMediaIndependentHistoryInHighCapacityGfpFrames,
       "cMediaIndependentHistoryOutGfpFrames": cMediaIndependentHistoryOutGfpFrames,
       "cMediaIndependentHistoryOutOverflowGfpFrames": cMediaIndependentHistoryOutOverflowGfpFrames,
       "cMediaIndependentHistoryOutHighCapacityGfpFrames": cMediaIndependentHistoryOutHighCapacityGfpFrames,
       "cMediaIndependentHistoryInGfpOctets": cMediaIndependentHistoryInGfpOctets,
       "cMediaIndependentHistoryInOverflowGfpOctets": cMediaIndependentHistoryInOverflowGfpOctets,
       "cMediaIndependentHistoryInHighCapacityGfpOctets": cMediaIndependentHistoryInHighCapacityGfpOctets,
       "cMediaIndependentHistoryOutGfpOctets": cMediaIndependentHistoryOutGfpOctets,
       "cMediaIndependentHistoryOutOverflowGfpOctets": cMediaIndependentHistoryOutOverflowGfpOctets,
       "cMediaIndependentHistoryOutHighCapacityGfpOctets": cMediaIndependentHistoryOutHighCapacityGfpOctets,
       "cMediaIndependentHistoryInGfpTypeInvalid": cMediaIndependentHistoryInGfpTypeInvalid,
       "cMediaIndependentHistoryInGfpCIDInvalid": cMediaIndependentHistoryInGfpCIDInvalid,
       "cMediaIndependentHistoryInGfpLFDRaised": cMediaIndependentHistoryInGfpLFDRaised,
       "cMediaIndependentHistoryInGfpCSFRaised": cMediaIndependentHistoryInGfpCSFRaised,
       "cMediaIndependentHistoryGfpRoundTripLatency": cMediaIndependentHistoryGfpRoundTripLatency,
       "cMediaIndependentHistory8b10bIdleSets": cMediaIndependentHistory8b10bIdleSets,
       "cMediaIndependentHistoryOverflow8b10bIdleSets": cMediaIndependentHistoryOverflow8b10bIdleSets,
       "cMediaIndependentHistoryHighCapacity8b10bIdleSets": cMediaIndependentHistoryHighCapacity8b10bIdleSets,
       "cMediaIndependentHistory8b10bNonIdleSets": cMediaIndependentHistory8b10bNonIdleSets,
       "cMediaIndependentHistoryOverflow8b10bNonIdleSets": cMediaIndependentHistoryOverflow8b10bNonIdleSets,
       "cMediaIndependentHistoryHighCapacity8b10bNonIdleSets": cMediaIndependentHistoryHighCapacity8b10bNonIdleSets,
       "cMediaIndependentHistory8b10bDataSets": cMediaIndependentHistory8b10bDataSets,
       "cMediaIndependentHistoryOverflow8b10bDataSets": cMediaIndependentHistoryOverflow8b10bDataSets,
       "cMediaIndependentHistoryHighCapacity8b10bDataSets": cMediaIndependentHistoryHighCapacity8b10bDataSets,
       "cMediaIndependentHistory8b10bInvalidOrdSets": cMediaIndependentHistory8b10bInvalidOrdSets,
       "cMediaIndependentHistory8b10bEncodingDispErr": cMediaIndependentHistory8b10bEncodingDispErr,
       "cMediaIndependentHistory8b10bLossOfSync": cMediaIndependentHistory8b10bLossOfSync,
       "cMediaIndependentHistoryInPauseFrames": cMediaIndependentHistoryInPauseFrames,
       "cMediaIndependentHistoryOutPauseFrames": cMediaIndependentHistoryOutPauseFrames,
       "cMediaIndependentHistoryInPktsDroppedInternalCongestion": cMediaIndependentHistoryInPktsDroppedInternalCongestion,
       "cMediaIndependentHistoryOutPktsDroppedInternalCongestion": cMediaIndependentHistoryOutPktsDroppedInternalCongestion,
       "cMediaIndependentHistoryInControlFrames": cMediaIndependentHistoryInControlFrames,
       "cMediaIndependentHistoryInUnknownOpcodeFrames": cMediaIndependentHistoryInUnknownOpcodeFrames,
       "cMediaIndependentHistoryHdlcPktDrops": cMediaIndependentHistoryHdlcPktDrops,
       "cMediaIndependentHistoryHdlcInOctets": cMediaIndependentHistoryHdlcInOctets,
       "cMediaIndependentHistoryHdlcOutOctets": cMediaIndependentHistoryHdlcOutOctets,
       "cMediaIndependentHistoryHdlcInAborts": cMediaIndependentHistoryHdlcInAborts,
       "cMediaIndependentHistoryInShortPkts": cMediaIndependentHistoryInShortPkts,
       "cMediaIndependentHistoryOutShortPkts": cMediaIndependentHistoryOutShortPkts,
       "cMediaIndependentHistoryOversizeDropped": cMediaIndependentHistoryOversizeDropped,
       "cMediaIndependentHistoryInErrorBytePkts": cMediaIndependentHistoryInErrorBytePkts,
       "cMediaIndependentHistoryInFramingErrorPkts": cMediaIndependentHistoryInFramingErrorPkts,
       "cMediaIndependentHistoryInJunkInterPkts": cMediaIndependentHistoryInJunkInterPkts,
       "cMediaIndependentHistoryOutOversizePkts": cMediaIndependentHistoryOutOversizePkts,
       "cMediaIndependentHistoryInPayloadCrcErrors": cMediaIndependentHistoryInPayloadCrcErrors,
       "cMediaIndependentHistoryOutPayloadCrcErrors": cMediaIndependentHistoryOutPayloadCrcErrors,
       "cMediaIndependentHistoryInRecvrReady": cMediaIndependentHistoryInRecvrReady,
       "cMediaIndependentHistoryOutRecvrReady": cMediaIndependentHistoryOutRecvrReady,
       "cMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum": cMediaIndependentHistory8b10bInvalidOrdSetsDispErrorsSum,
       "cMediaIndependentHistoryInGfpSblkCRCErr": cMediaIndependentHistoryInGfpSblkCRCErr,
       "cMediaIndependentHistoryOutFramesTooLong": cMediaIndependentHistoryOutFramesTooLong,
       "cMediaIndependentHistoryPkts1519to1522Octets": cMediaIndependentHistoryPkts1519to1522Octets,
       "cMediaIndependentHistoryOutFramesTruncated": cMediaIndependentHistoryOutFramesTruncated,
       "cMediaIndependentHistoryPcsErrCount": cMediaIndependentHistoryPcsErrCount,
       "cMediaIndependentHistoryPcsErrCount2": cMediaIndependentHistoryPcsErrCount2,
       "cMediaIndependentHistoryPcs49RxErrBer": cMediaIndependentHistoryPcs49RxErrBer,
       "cMediaIndependentHistoryPcs49RxErrDec": cMediaIndependentHistoryPcs49RxErrDec,
       "cMediaIndependentHistoryPkts1519toMaxOctets": cMediaIndependentHistoryPkts1519toMaxOctets,
       "cMediaIndependentHistoryRxLcvErrors": cMediaIndependentHistoryRxLcvErrors,
       "cMediaIndependentHistoryTxLcvErrors": cMediaIndependentHistoryTxLcvErrors,
       "cMediaIndependentHistoryPcsEgRxErrFrames": cMediaIndependentHistoryPcsEgRxErrFrames,
       "cerentHcRmonMIBConformance": cerentHcRmonMIBConformance,
       "cerentHcRmonMIBCompliances": cerentHcRmonMIBCompliances,
       "cerentHcMediaIndependentCompliance": cerentHcMediaIndependentCompliance,
       "cerentHcRmonMIBGroups": cerentHcRmonMIBGroups,
       "cMediaIndependentGroup": cMediaIndependentGroup,
       "cMediaIndependenHistoryControlGroup": cMediaIndependenHistoryControlGroup,
       "cMediaIndependentHistoryGroup": cMediaIndependentHistoryGroup}
)
