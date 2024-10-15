# SNMP MIB module (APCODEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APCODEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:12 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApPercentage,) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApPercentage")

(apSigRealmStatsEntry,) = mibBuilder.importSymbols(
    "APSYSMGMT-MIB",
    "apSigRealmStatsEntry")

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

apCodecModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7)
)
apCodecModule.setRevisions(
        ("2012-07-16 00:00",
         "2012-06-22 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApCodecDigitTypes(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("inband", 2),
          ("inbandDual", 6),
          ("inbandTrans", 5),
          ("none", 1),
          ("noneDual", 4),
          ("rfc2833", 3),
          ("rfc2833Dual", 8),
          ("rfc2833Trans", 7),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_ApCodecMIBObjects_ObjectIdentity = ObjectIdentity
apCodecMIBObjects = _ApCodecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1)
)
_ApCodecRealmStatsTable_Object = MibTable
apCodecRealmStatsTable = _ApCodecRealmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    apCodecRealmStatsTable.setStatus("current")
_ApCodecRealmStatsEntry_Object = MibTableRow
apCodecRealmStatsEntry = _ApCodecRealmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apCodecRealmStatsEntry.setStatus("current")
_ApCodecRealmCountOther_Type = Counter32
_ApCodecRealmCountOther_Object = MibTableColumn
apCodecRealmCountOther = _ApCodecRealmCountOther_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 1),
    _ApCodecRealmCountOther_Type()
)
apCodecRealmCountOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountOther.setStatus("current")
_ApCodecRealmCountPCMU_Type = Counter32
_ApCodecRealmCountPCMU_Object = MibTableColumn
apCodecRealmCountPCMU = _ApCodecRealmCountPCMU_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 2),
    _ApCodecRealmCountPCMU_Type()
)
apCodecRealmCountPCMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountPCMU.setStatus("current")
_ApCodecRealmCountPCMA_Type = Counter32
_ApCodecRealmCountPCMA_Object = MibTableColumn
apCodecRealmCountPCMA = _ApCodecRealmCountPCMA_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 3),
    _ApCodecRealmCountPCMA_Type()
)
apCodecRealmCountPCMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountPCMA.setStatus("current")
_ApCodecRealmCountG722_Type = Counter32
_ApCodecRealmCountG722_Object = MibTableColumn
apCodecRealmCountG722 = _ApCodecRealmCountG722_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 4),
    _ApCodecRealmCountG722_Type()
)
apCodecRealmCountG722.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG722.setStatus("current")
_ApCodecRealmCountG723_Type = Counter32
_ApCodecRealmCountG723_Object = MibTableColumn
apCodecRealmCountG723 = _ApCodecRealmCountG723_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 5),
    _ApCodecRealmCountG723_Type()
)
apCodecRealmCountG723.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG723.setStatus("current")
_ApCodecRealmCountG726_16_Type = Counter32
_ApCodecRealmCountG726_16_Object = MibScalar
apCodecRealmCountG726_16 = _ApCodecRealmCountG726_16_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 6),
    _ApCodecRealmCountG726_16_Type()
)
apCodecRealmCountG726_16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG726_16.setStatus("current")
_ApCodecRealmCountG726_24_Type = Counter32
_ApCodecRealmCountG726_24_Object = MibScalar
apCodecRealmCountG726_24 = _ApCodecRealmCountG726_24_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 7),
    _ApCodecRealmCountG726_24_Type()
)
apCodecRealmCountG726_24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG726_24.setStatus("current")
_ApCodecRealmCountG726_32_Type = Counter32
_ApCodecRealmCountG726_32_Object = MibScalar
apCodecRealmCountG726_32 = _ApCodecRealmCountG726_32_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 8),
    _ApCodecRealmCountG726_32_Type()
)
apCodecRealmCountG726_32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG726_32.setStatus("current")
_ApCodecRealmCountG726_40_Type = Counter32
_ApCodecRealmCountG726_40_Object = MibScalar
apCodecRealmCountG726_40 = _ApCodecRealmCountG726_40_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 9),
    _ApCodecRealmCountG726_40_Type()
)
apCodecRealmCountG726_40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG726_40.setStatus("current")
_ApCodecRealmCountG728_Type = Counter32
_ApCodecRealmCountG728_Object = MibTableColumn
apCodecRealmCountG728 = _ApCodecRealmCountG728_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 10),
    _ApCodecRealmCountG728_Type()
)
apCodecRealmCountG728.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG728.setStatus("current")
_ApCodecRealmCountG729_Type = Counter32
_ApCodecRealmCountG729_Object = MibTableColumn
apCodecRealmCountG729 = _ApCodecRealmCountG729_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 11),
    _ApCodecRealmCountG729_Type()
)
apCodecRealmCountG729.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountG729.setStatus("current")
_ApCodecRealmCountGSM_Type = Counter32
_ApCodecRealmCountGSM_Object = MibTableColumn
apCodecRealmCountGSM = _ApCodecRealmCountGSM_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 12),
    _ApCodecRealmCountGSM_Type()
)
apCodecRealmCountGSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountGSM.setStatus("current")
_ApCodecRealmCountILBC_Type = Counter32
_ApCodecRealmCountILBC_Object = MibTableColumn
apCodecRealmCountILBC = _ApCodecRealmCountILBC_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 13),
    _ApCodecRealmCountILBC_Type()
)
apCodecRealmCountILBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountILBC.setStatus("current")
_ApCodecRealmCountAMR_Type = Counter32
_ApCodecRealmCountAMR_Object = MibTableColumn
apCodecRealmCountAMR = _ApCodecRealmCountAMR_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 14),
    _ApCodecRealmCountAMR_Type()
)
apCodecRealmCountAMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountAMR.setStatus("current")
_ApCodecRealmCountEVRC_Type = Counter32
_ApCodecRealmCountEVRC_Object = MibTableColumn
apCodecRealmCountEVRC = _ApCodecRealmCountEVRC_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 15),
    _ApCodecRealmCountEVRC_Type()
)
apCodecRealmCountEVRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountEVRC.setStatus("current")
_ApCodecRealmCountH261_Type = Counter32
_ApCodecRealmCountH261_Object = MibTableColumn
apCodecRealmCountH261 = _ApCodecRealmCountH261_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 16),
    _ApCodecRealmCountH261_Type()
)
apCodecRealmCountH261.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountH261.setStatus("current")
_ApCodecRealmCountH263_Type = Counter32
_ApCodecRealmCountH263_Object = MibTableColumn
apCodecRealmCountH263 = _ApCodecRealmCountH263_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 17),
    _ApCodecRealmCountH263_Type()
)
apCodecRealmCountH263.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountH263.setStatus("current")
_ApCodecRealmCountT38_Type = Counter32
_ApCodecRealmCountT38_Object = MibTableColumn
apCodecRealmCountT38 = _ApCodecRealmCountT38_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 18),
    _ApCodecRealmCountT38_Type()
)
apCodecRealmCountT38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmCountT38.setStatus("current")
_ApCodecTranscodingMIBObjects_ObjectIdentity = ObjectIdentity
apCodecTranscodingMIBObjects = _ApCodecTranscodingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2)
)
_ApCodecTranscodingRealmStatsTable_Object = MibTable
apCodecTranscodingRealmStatsTable = _ApCodecTranscodingRealmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    apCodecTranscodingRealmStatsTable.setStatus("current")
_ApCodecTranscodingRealmStatsEntry_Object = MibTableRow
apCodecTranscodingRealmStatsEntry = _ApCodecTranscodingRealmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    apCodecTranscodingRealmStatsEntry.setStatus("current")
_ApCodecRealmSessionsTransparent_Type = Counter32
_ApCodecRealmSessionsTransparent_Object = MibTableColumn
apCodecRealmSessionsTransparent = _ApCodecRealmSessionsTransparent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1, 1),
    _ApCodecRealmSessionsTransparent_Type()
)
apCodecRealmSessionsTransparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmSessionsTransparent.setStatus("current")
_ApCodecRealmSessionsTransrated_Type = Counter32
_ApCodecRealmSessionsTransrated_Object = MibTableColumn
apCodecRealmSessionsTransrated = _ApCodecRealmSessionsTransrated_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1, 2),
    _ApCodecRealmSessionsTransrated_Type()
)
apCodecRealmSessionsTransrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmSessionsTransrated.setStatus("current")
_ApCodecRealmSessionsTranscoded_Type = Counter32
_ApCodecRealmSessionsTranscoded_Object = MibTableColumn
apCodecRealmSessionsTranscoded = _ApCodecRealmSessionsTranscoded_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1, 3),
    _ApCodecRealmSessionsTranscoded_Type()
)
apCodecRealmSessionsTranscoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecRealmSessionsTranscoded.setStatus("current")
_ApCodecTranscodingResourceMIBObjects_ObjectIdentity = ObjectIdentity
apCodecTranscodingResourceMIBObjects = _ApCodecTranscodingResourceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2)
)


class _ApCodecTranscodingResourcesTotal_Type(Integer32):
    """Custom type apCodecTranscodingResourcesTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApCodecTranscodingResourcesTotal_Type.__name__ = "Integer32"
_ApCodecTranscodingResourcesTotal_Object = MibScalar
apCodecTranscodingResourcesTotal = _ApCodecTranscodingResourcesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 1),
    _ApCodecTranscodingResourcesTotal_Type()
)
apCodecTranscodingResourcesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecTranscodingResourcesTotal.setStatus("current")
_ApCodecTranscodingResourcesCurrent_Type = Gauge32
_ApCodecTranscodingResourcesCurrent_Object = MibScalar
apCodecTranscodingResourcesCurrent = _ApCodecTranscodingResourcesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 2),
    _ApCodecTranscodingResourcesCurrent_Type()
)
apCodecTranscodingResourcesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecTranscodingResourcesCurrent.setStatus("current")
_ApCodecTranscodingResourcesHigh_Type = Counter32
_ApCodecTranscodingResourcesHigh_Object = MibScalar
apCodecTranscodingResourcesHigh = _ApCodecTranscodingResourcesHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 3),
    _ApCodecTranscodingResourcesHigh_Type()
)
apCodecTranscodingResourcesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecTranscodingResourcesHigh.setStatus("current")
_ApCodecTranscodingInUsePercentCurrent_Type = ApPercentage
_ApCodecTranscodingInUsePercentCurrent_Object = MibScalar
apCodecTranscodingInUsePercentCurrent = _ApCodecTranscodingInUsePercentCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 4),
    _ApCodecTranscodingInUsePercentCurrent_Type()
)
apCodecTranscodingInUsePercentCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecTranscodingInUsePercentCurrent.setStatus("current")
_ApCodecTranscodingInUsePercentHigh_Type = ApPercentage
_ApCodecTranscodingInUsePercentHigh_Object = MibScalar
apCodecTranscodingInUsePercentHigh = _ApCodecTranscodingInUsePercentHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 5),
    _ApCodecTranscodingInUsePercentHigh_Type()
)
apCodecTranscodingInUsePercentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecTranscodingInUsePercentHigh.setStatus("current")
_ApCodecTable_Object = MibTable
apCodecTable = _ApCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3)
)
if mibBuilder.loadTexts:
    apCodecTable.setStatus("current")
_ApCodecEntry_Object = MibTableRow
apCodecEntry = _ApCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3, 1)
)
apCodecEntry.setIndexNames(
    (0, "APCODEC-MIB", "apCodecIndex"),
)
if mibBuilder.loadTexts:
    apCodecEntry.setStatus("current")


class _ApCodecIndex_Type(Integer32):
    """Custom type apCodecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApCodecIndex_Type.__name__ = "Integer32"
_ApCodecIndex_Object = MibTableColumn
apCodecIndex = _ApCodecIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3, 1, 1),
    _ApCodecIndex_Type()
)
apCodecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecIndex.setStatus("current")


class _ApCodecName_Type(DisplayString):
    """Custom type apCodecName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApCodecName_Type.__name__ = "DisplayString"
_ApCodecName_Object = MibTableColumn
apCodecName = _ApCodecName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3, 1, 2),
    _ApCodecName_Type()
)
apCodecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecName.setStatus("current")
_ApCodecPairStatsTable_Object = MibTable
apCodecPairStatsTable = _ApCodecPairStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4)
)
if mibBuilder.loadTexts:
    apCodecPairStatsTable.setStatus("current")
_ApCodecPairStatsEntry_Object = MibTableRow
apCodecPairStatsEntry = _ApCodecPairStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1)
)
apCodecPairStatsEntry.setIndexNames(
    (0, "APCODEC-MIB", "apCodecPairAIndex"),
    (0, "APCODEC-MIB", "apCodecPairBIndex"),
    (0, "APCODEC-MIB", "apCodecPairAPValue"),
    (0, "APCODEC-MIB", "apCodecPairBPValue"),
    (0, "APCODEC-MIB", "apCodecPairADigitType"),
    (0, "APCODEC-MIB", "apCodecPairBDigitType"),
)
if mibBuilder.loadTexts:
    apCodecPairStatsEntry.setStatus("current")
_ApCodecPairAIndex_Type = Integer32
_ApCodecPairAIndex_Object = MibTableColumn
apCodecPairAIndex = _ApCodecPairAIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 1),
    _ApCodecPairAIndex_Type()
)
apCodecPairAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecPairAIndex.setStatus("current")
_ApCodecPairBIndex_Type = Integer32
_ApCodecPairBIndex_Object = MibTableColumn
apCodecPairBIndex = _ApCodecPairBIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 2),
    _ApCodecPairBIndex_Type()
)
apCodecPairBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecPairBIndex.setStatus("current")


class _ApCodecPairAPValue_Type(Integer32):
    """Custom type apCodecPairAPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApCodecPairAPValue_Type.__name__ = "Integer32"
_ApCodecPairAPValue_Object = MibTableColumn
apCodecPairAPValue = _ApCodecPairAPValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 3),
    _ApCodecPairAPValue_Type()
)
apCodecPairAPValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecPairAPValue.setStatus("current")


class _ApCodecPairBPValue_Type(Integer32):
    """Custom type apCodecPairBPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApCodecPairBPValue_Type.__name__ = "Integer32"
_ApCodecPairBPValue_Object = MibTableColumn
apCodecPairBPValue = _ApCodecPairBPValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 4),
    _ApCodecPairBPValue_Type()
)
apCodecPairBPValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecPairBPValue.setStatus("current")
_ApCodecPairADigitType_Type = ApCodecDigitTypes
_ApCodecPairADigitType_Object = MibTableColumn
apCodecPairADigitType = _ApCodecPairADigitType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 5),
    _ApCodecPairADigitType_Type()
)
apCodecPairADigitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecPairADigitType.setStatus("current")
_ApCodecPairBDigitType_Type = ApCodecDigitTypes
_ApCodecPairBDigitType_Object = MibTableColumn
apCodecPairBDigitType = _ApCodecPairBDigitType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 6),
    _ApCodecPairBDigitType_Type()
)
apCodecPairBDigitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCodecPairBDigitType.setStatus("current")
_ApCodecPairTranscodingCurrent_Type = Gauge32
_ApCodecPairTranscodingCurrent_Object = MibTableColumn
apCodecPairTranscodingCurrent = _ApCodecPairTranscodingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 7),
    _ApCodecPairTranscodingCurrent_Type()
)
apCodecPairTranscodingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecPairTranscodingCurrent.setStatus("current")
_ApCodecPairTranscodingHigh_Type = Counter32
_ApCodecPairTranscodingHigh_Object = MibTableColumn
apCodecPairTranscodingHigh = _ApCodecPairTranscodingHigh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 8),
    _ApCodecPairTranscodingHigh_Type()
)
apCodecPairTranscodingHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCodecPairTranscodingHigh.setStatus("current")
_ApCodecNotificationObjects_ObjectIdentity = ObjectIdentity
apCodecNotificationObjects = _ApCodecNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 3)
)
_ApCodecNotificationPrefix_ObjectIdentity = ObjectIdentity
apCodecNotificationPrefix = _ApCodecNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 4)
)
_ApCodecNotifications_ObjectIdentity = ObjectIdentity
apCodecNotifications = _ApCodecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 4, 0)
)
_ApCodecConformance_ObjectIdentity = ObjectIdentity
apCodecConformance = _ApCodecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5)
)
_ApCodecCompliances_ObjectIdentity = ObjectIdentity
apCodecCompliances = _ApCodecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 1)
)
_ApCodecGroups_ObjectIdentity = ObjectIdentity
apCodecGroups = _ApCodecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2)
)
_ApCodecNotificationsGroups_ObjectIdentity = ObjectIdentity
apCodecNotificationsGroups = _ApCodecNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 3)
)
apSigRealmStatsEntry.registerAugmentions(
    ("APCODEC-MIB",
     "apCodecRealmStatsEntry")
)
apCodecRealmStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())
apSigRealmStatsEntry.registerAugmentions(
    ("APCODEC-MIB",
     "apCodecTranscodingRealmStatsEntry")
)
apCodecTranscodingRealmStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())

# Managed Objects groups

apCodecRealmStatsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 1)
)
apCodecRealmStatsObjectsGroup.setObjects(
      *(("APCODEC-MIB", "apCodecRealmCountOther"),
        ("APCODEC-MIB", "apCodecRealmCountPCMU"),
        ("APCODEC-MIB", "apCodecRealmCountPCMA"),
        ("APCODEC-MIB", "apCodecRealmCountG722"),
        ("APCODEC-MIB", "apCodecRealmCountG723"),
        ("APCODEC-MIB", "apCodecRealmCountG726_16"),
        ("APCODEC-MIB", "apCodecRealmCountG726_24"),
        ("APCODEC-MIB", "apCodecRealmCountG726_32"),
        ("APCODEC-MIB", "apCodecRealmCountG726_40"),
        ("APCODEC-MIB", "apCodecRealmCountG728"),
        ("APCODEC-MIB", "apCodecRealmCountG729"),
        ("APCODEC-MIB", "apCodecRealmCountGSM"),
        ("APCODEC-MIB", "apCodecRealmCountILBC"),
        ("APCODEC-MIB", "apCodecRealmCountH261"),
        ("APCODEC-MIB", "apCodecRealmCountH263"),
        ("APCODEC-MIB", "apCodecRealmCountT38"))
)
if mibBuilder.loadTexts:
    apCodecRealmStatsObjectsGroup.setStatus("current")

apCodecMediaProcessingObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 2)
)
apCodecMediaProcessingObjectsGroup.setObjects(
      *(("APCODEC-MIB", "apCodecRealmSessionsTransparent"),
        ("APCODEC-MIB", "apCodecRealmSessionsTransrated"),
        ("APCODEC-MIB", "apCodecRealmSessionsTranscoded"))
)
if mibBuilder.loadTexts:
    apCodecMediaProcessingObjectsGroup.setStatus("current")

apCodecRealmStatsObjectsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 3)
)
apCodecRealmStatsObjectsGroup2.setObjects(
      *(("APCODEC-MIB", "apCodecRealmCountAMR"),
        ("APCODEC-MIB", "apCodecRealmCountEVRC"))
)
if mibBuilder.loadTexts:
    apCodecRealmStatsObjectsGroup2.setStatus("current")

apCodecTranscodingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 4)
)
apCodecTranscodingStatsGroup.setObjects(
      *(("APCODEC-MIB", "apCodecTranscodingResourcesTotal"),
        ("APCODEC-MIB", "apCodecTranscodingResourcesCurrent"),
        ("APCODEC-MIB", "apCodecTranscodingResourcesHigh"),
        ("APCODEC-MIB", "apCodecTranscodingInUsePercentCurrent"),
        ("APCODEC-MIB", "apCodecTranscodingInUsePercentHigh"),
        ("APCODEC-MIB", "apCodecName"),
        ("APCODEC-MIB", "apCodecPairTranscodingCurrent"),
        ("APCODEC-MIB", "apCodecPairTranscodingHigh"))
)
if mibBuilder.loadTexts:
    apCodecTranscodingStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APCODEC-MIB",
    **{"ApCodecDigitTypes": ApCodecDigitTypes,
       "apCodecModule": apCodecModule,
       "apCodecMIBObjects": apCodecMIBObjects,
       "apCodecRealmStatsTable": apCodecRealmStatsTable,
       "apCodecRealmStatsEntry": apCodecRealmStatsEntry,
       "apCodecRealmCountOther": apCodecRealmCountOther,
       "apCodecRealmCountPCMU": apCodecRealmCountPCMU,
       "apCodecRealmCountPCMA": apCodecRealmCountPCMA,
       "apCodecRealmCountG722": apCodecRealmCountG722,
       "apCodecRealmCountG723": apCodecRealmCountG723,
       "apCodecRealmCountG726-16": apCodecRealmCountG726_16,
       "apCodecRealmCountG726-24": apCodecRealmCountG726_24,
       "apCodecRealmCountG726-32": apCodecRealmCountG726_32,
       "apCodecRealmCountG726-40": apCodecRealmCountG726_40,
       "apCodecRealmCountG728": apCodecRealmCountG728,
       "apCodecRealmCountG729": apCodecRealmCountG729,
       "apCodecRealmCountGSM": apCodecRealmCountGSM,
       "apCodecRealmCountILBC": apCodecRealmCountILBC,
       "apCodecRealmCountAMR": apCodecRealmCountAMR,
       "apCodecRealmCountEVRC": apCodecRealmCountEVRC,
       "apCodecRealmCountH261": apCodecRealmCountH261,
       "apCodecRealmCountH263": apCodecRealmCountH263,
       "apCodecRealmCountT38": apCodecRealmCountT38,
       "apCodecTranscodingMIBObjects": apCodecTranscodingMIBObjects,
       "apCodecTranscodingRealmStatsTable": apCodecTranscodingRealmStatsTable,
       "apCodecTranscodingRealmStatsEntry": apCodecTranscodingRealmStatsEntry,
       "apCodecRealmSessionsTransparent": apCodecRealmSessionsTransparent,
       "apCodecRealmSessionsTransrated": apCodecRealmSessionsTransrated,
       "apCodecRealmSessionsTranscoded": apCodecRealmSessionsTranscoded,
       "apCodecTranscodingResourceMIBObjects": apCodecTranscodingResourceMIBObjects,
       "apCodecTranscodingResourcesTotal": apCodecTranscodingResourcesTotal,
       "apCodecTranscodingResourcesCurrent": apCodecTranscodingResourcesCurrent,
       "apCodecTranscodingResourcesHigh": apCodecTranscodingResourcesHigh,
       "apCodecTranscodingInUsePercentCurrent": apCodecTranscodingInUsePercentCurrent,
       "apCodecTranscodingInUsePercentHigh": apCodecTranscodingInUsePercentHigh,
       "apCodecTable": apCodecTable,
       "apCodecEntry": apCodecEntry,
       "apCodecIndex": apCodecIndex,
       "apCodecName": apCodecName,
       "apCodecPairStatsTable": apCodecPairStatsTable,
       "apCodecPairStatsEntry": apCodecPairStatsEntry,
       "apCodecPairAIndex": apCodecPairAIndex,
       "apCodecPairBIndex": apCodecPairBIndex,
       "apCodecPairAPValue": apCodecPairAPValue,
       "apCodecPairBPValue": apCodecPairBPValue,
       "apCodecPairADigitType": apCodecPairADigitType,
       "apCodecPairBDigitType": apCodecPairBDigitType,
       "apCodecPairTranscodingCurrent": apCodecPairTranscodingCurrent,
       "apCodecPairTranscodingHigh": apCodecPairTranscodingHigh,
       "apCodecNotificationObjects": apCodecNotificationObjects,
       "apCodecNotificationPrefix": apCodecNotificationPrefix,
       "apCodecNotifications": apCodecNotifications,
       "apCodecConformance": apCodecConformance,
       "apCodecCompliances": apCodecCompliances,
       "apCodecGroups": apCodecGroups,
       "apCodecRealmStatsObjectsGroup": apCodecRealmStatsObjectsGroup,
       "apCodecMediaProcessingObjectsGroup": apCodecMediaProcessingObjectsGroup,
       "apCodecRealmStatsObjectsGroup2": apCodecRealmStatsObjectsGroup2,
       "apCodecTranscodingStatsGroup": apCodecTranscodingStatsGroup,
       "apCodecNotificationsGroups": apCodecNotificationsGroups}
)
