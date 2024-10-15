# SNMP MIB module (Wellfleet-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:41 2024
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

(wfHwModuleGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfHwModuleGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfHwModuleTable_Object = MibTable
wfHwModuleTable = _WfHwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wfHwModuleTable.setStatus("mandatory")
_WfHwModuleEntry_Object = MibTableRow
wfHwModuleEntry = _WfHwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1)
)
wfHwModuleEntry.setIndexNames(
    (0, "Wellfleet-MODULE-MIB", "wfHwModuleSlot"),
    (0, "Wellfleet-MODULE-MIB", "wfHwModuleModule"),
)
if mibBuilder.loadTexts:
    wfHwModuleEntry.setStatus("mandatory")
_WfHwModuleSlot_Type = Integer32
_WfHwModuleSlot_Object = MibTableColumn
wfHwModuleSlot = _WfHwModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 1),
    _WfHwModuleSlot_Type()
)
wfHwModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleSlot.setStatus("mandatory")
_WfHwModuleModule_Type = Integer32
_WfHwModuleModule_Object = MibTableColumn
wfHwModuleModule = _WfHwModuleModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 2),
    _WfHwModuleModule_Type()
)
wfHwModuleModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleModule.setStatus("mandatory")


class _WfHwModuleModIdOpt_Type(Integer32):
    """Custom type wfHwModuleModIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(512,
              768,
              769,
              1280,
              1281,
              1408,
              1536,
              1537,
              1538,
              1540,
              1541,
              1542,
              1544,
              1545,
              1546,
              1584,
              1585,
              1586,
              1588,
              1589,
              1590,
              1592,
              1593,
              1594,
              1664,
              1792,
              1793,
              1800,
              1801,
              1808,
              1809,
              1825,
              1833,
              1856,
              1857,
              1864,
              1865,
              1872,
              1873,
              1889,
              1897,
              2048,
              2049,
              2176,
              2304,
              2560,
              2816,
              2944,
              3072,
              3073,
              3328,
              3329,
              3330,
              3584,
              8000,
              8160,
              8161,
              8320,
              8321,
              8500,
              8501,
              8704,
              8720,
              8728,
              8729,
              8736,
              8744,
              8752,
              8768,
              8776,
              8780,
              8784,
              8800,
              8808,
              8816,
              8832,
              8848,
              8864,
              8872,
              8873,
              8880,
              8890,
              8891,
              8896,
              8912,
              8928,
              8944,
              8960,
              8972,
              8976,
              16384,
              16640,
              16896,
              16897,
              16898,
              16899,
              17152,
              17153,
              17154,
              17155,
              17408,
              17664,
              17920,
              18176,
              18432,
              18688,
              18944,
              524288,
              524544)
        )
    )
    namedValues = NamedValues(
        *(("ahwcompnm128", 3329),
          ("ahwcompnm256", 3330),
          ("ahwcompnm32", 3328),
          ("arn7sync", 8873),
          ("arndcsu", 8768),
          ("arne7sync", 8872),
          ("arnentsync", 8864),
          ("arnfe1", 8780),
          ("arnft1", 8776),
          ("arnisdb", 8808),
          ("arnisdns", 8784),
          ("arnisdnu", 8800),
          ("arnmbenx10", 8896),
          ("arnmbsen", 8720),
          ("arnmbsfefx", 8729),
          ("arnmbsfetx", 8728),
          ("arnmbstr", 8704),
          ("arnmbtrx10", 8912),
          ("arnpbe7sx10", 8972),
          ("arnpbenx10", 8928),
          ("arnpbtenx10", 8960),
          ("arnpbtrx10", 8944),
          ("arnpbttrx10", 8976),
          ("arnsenet", 8832),
          ("arnssync", 8736),
          ("arnstkrg", 8816),
          ("arntrtsync", 8880),
          ("arntsync", 8848),
          ("arnv34", 8752),
          ("arnvoice", 8890),
          ("arnvoicedsync", 8891),
          ("asnqbri", 2560),
          ("atm5000ah", 524288),
          ("atm5000bh", 524544),
          ("cam", 2049),
          ("denm", 1280),
          ("denmhwf", 1281),
          ("dmct1nm", 2944),
          ("ds1e1atm", 8160),
          ("ds3e3atm", 8161),
          ("dsnm11", 1541),
          ("dsnm11isdn", 1589),
          ("dsnm12", 1542),
          ("dsnm12isdn", 1590),
          ("dsnm1n", 1540),
          ("dsnm1nisdn", 1588),
          ("dsnm21", 1545),
          ("dsnm21isdn", 1593),
          ("dsnm22", 1546),
          ("dsnm22isdn", 1594),
          ("dsnm2n", 1544),
          ("dsnm2nisdn", 1592),
          ("dsnmn1", 1537),
          ("dsnmn1isdn", 1585),
          ("dsnmn2", 1538),
          ("dsnmn2isdn", 1586),
          ("dsnmnn", 1536),
          ("dsnmnnisdn", 1584),
          ("dtnm", 2048),
          ("fbrmbdfen", 8000),
          ("fvoippmcc", 8500),
          ("fvoipt1e1pmc", 8501),
          ("hwcompnm128", 3073),
          ("hwcompnm32", 3072),
          ("iqe", 1408),
          ("iqtok", 2176),
          ("litembsfetx", 8744),
          ("mce1nm", 2816),
          ("mmasmbdas", 1833),
          ("mmasmbdashwf", 1897),
          ("mmfsddas", 1793),
          ("mmfsddashwf", 1857),
          ("mmfsdsas", 1792),
          ("mmfsdsashwf", 1856),
          ("mmscdas", 1809),
          ("mmscdashwf", 1873),
          ("mmscsas", 1808),
          ("mmscsashwf", 1872),
          ("pmcdsync", 8320),
          ("pmcqsync", 8321),
          ("qsyncnm", 1664),
          ("se100nm", 2304),
          ("shssinm", 3584),
          ("smammbdas", 1825),
          ("smammbdashwf", 1889),
          ("smfsddas", 1801),
          ("smfsddashwf", 1865),
          ("smfsdsas", 1800),
          ("smfsdsashwf", 1864),
          ("snm100f2", 17664),
          ("snm100t16", 18688),
          ("snm100t2", 16640),
          ("snm100t2p4", 18176),
          ("snm10f8", 17408),
          ("snm10t14100f1", 18944),
          ("snm10t14100t1", 18432),
          ("snm10t16", 16384),
          ("snm10t16p4", 17920),
          ("snmatmoc31dmm", 16897),
          ("snmatmoc31dsm", 16899),
          ("snmatmoc31mm", 16896),
          ("snmatmoc31sm", 16898),
          ("snmfddismm", 17152),
          ("snmfddisms", 17153),
          ("snmfddissm", 17154),
          ("snmfddisss", 17155),
          ("spex", 512),
          ("spexhsd", 769),
          ("spexhss", 768))
    )


_WfHwModuleModIdOpt_Type.__name__ = "Integer32"
_WfHwModuleModIdOpt_Object = MibTableColumn
wfHwModuleModIdOpt = _WfHwModuleModIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 3),
    _WfHwModuleModIdOpt_Type()
)
wfHwModuleModIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleModIdOpt.setStatus("mandatory")
_WfHwModuleModRev_Type = OctetString
_WfHwModuleModRev_Object = MibTableColumn
wfHwModuleModRev = _WfHwModuleModRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 4),
    _WfHwModuleModRev_Type()
)
wfHwModuleModRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleModRev.setStatus("mandatory")
_WfHwModuleModSerialNumber_Type = OctetString
_WfHwModuleModSerialNumber_Object = MibTableColumn
wfHwModuleModSerialNumber = _WfHwModuleModSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 5),
    _WfHwModuleModSerialNumber_Type()
)
wfHwModuleModSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleModSerialNumber.setStatus("mandatory")
_WfHwModuleArtworkRev_Type = DisplayString
_WfHwModuleArtworkRev_Object = MibTableColumn
wfHwModuleArtworkRev = _WfHwModuleArtworkRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 6),
    _WfHwModuleArtworkRev_Type()
)
wfHwModuleArtworkRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleArtworkRev.setStatus("mandatory")
_WfHwModuleMemorySize1_Type = Integer32
_WfHwModuleMemorySize1_Object = MibTableColumn
wfHwModuleMemorySize1 = _WfHwModuleMemorySize1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 7),
    _WfHwModuleMemorySize1_Type()
)
wfHwModuleMemorySize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleMemorySize1.setStatus("mandatory")
_WfHwModuleMemorySize2_Type = Integer32
_WfHwModuleMemorySize2_Object = MibTableColumn
wfHwModuleMemorySize2 = _WfHwModuleMemorySize2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 8),
    _WfHwModuleMemorySize2_Type()
)
wfHwModuleMemorySize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleMemorySize2.setStatus("mandatory")
_WfHwModuleDaughterBdIdOpt_Type = Integer32
_WfHwModuleDaughterBdIdOpt_Object = MibTableColumn
wfHwModuleDaughterBdIdOpt = _WfHwModuleDaughterBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 9),
    _WfHwModuleDaughterBdIdOpt_Type()
)
wfHwModuleDaughterBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleDaughterBdIdOpt.setStatus("mandatory")
_WfHwModuleLEDStatus1_Type = Integer32
_WfHwModuleLEDStatus1_Object = MibTableColumn
wfHwModuleLEDStatus1 = _WfHwModuleLEDStatus1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 10),
    _WfHwModuleLEDStatus1_Type()
)
wfHwModuleLEDStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleLEDStatus1.setStatus("mandatory")
_WfHwModuleLEDState1_Type = Integer32
_WfHwModuleLEDState1_Object = MibTableColumn
wfHwModuleLEDState1 = _WfHwModuleLEDState1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 11),
    _WfHwModuleLEDState1_Type()
)
wfHwModuleLEDState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleLEDState1.setStatus("mandatory")
_WfHwModuleLEDStatus2_Type = Integer32
_WfHwModuleLEDStatus2_Object = MibTableColumn
wfHwModuleLEDStatus2 = _WfHwModuleLEDStatus2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 12),
    _WfHwModuleLEDStatus2_Type()
)
wfHwModuleLEDStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleLEDStatus2.setStatus("mandatory")
_WfHwModuleLEDState2_Type = Integer32
_WfHwModuleLEDState2_Object = MibTableColumn
wfHwModuleLEDState2 = _WfHwModuleLEDState2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 13),
    _WfHwModuleLEDState2_Type()
)
wfHwModuleLEDState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleLEDState2.setStatus("mandatory")
_WfHwModuleLEDStatus3_Type = Integer32
_WfHwModuleLEDStatus3_Object = MibTableColumn
wfHwModuleLEDStatus3 = _WfHwModuleLEDStatus3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 14),
    _WfHwModuleLEDStatus3_Type()
)
wfHwModuleLEDStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleLEDStatus3.setStatus("mandatory")
_WfHwModuleLEDState3_Type = Integer32
_WfHwModuleLEDState3_Object = MibTableColumn
wfHwModuleLEDState3 = _WfHwModuleLEDState3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 1, 1, 15),
    _WfHwModuleLEDState3_Type()
)
wfHwModuleLEDState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModuleLEDState3.setStatus("mandatory")
_WfModuleTable_Object = MibTable
wfModuleTable = _WfModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wfModuleTable.setStatus("mandatory")
_WfModuleEntry_Object = MibTableRow
wfModuleEntry = _WfModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1)
)
wfModuleEntry.setIndexNames(
    (0, "Wellfleet-MODULE-MIB", "wfModuleSlot"),
)
if mibBuilder.loadTexts:
    wfModuleEntry.setStatus("mandatory")


class _WfModuleDelete_Type(Integer32):
    """Custom type wfModuleDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfModuleDelete_Type.__name__ = "Integer32"
_WfModuleDelete_Object = MibTableColumn
wfModuleDelete = _WfModuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 1),
    _WfModuleDelete_Type()
)
wfModuleDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleDelete.setStatus("mandatory")
_WfModuleSlot_Type = Integer32
_WfModuleSlot_Object = MibTableColumn
wfModuleSlot = _WfModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 2),
    _WfModuleSlot_Type()
)
wfModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModuleSlot.setStatus("mandatory")


class _WfModuleTimerFrequency_Type(Integer32):
    """Custom type wfModuleTimerFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("timerdefault", 1)
    )


_WfModuleTimerFrequency_Type.__name__ = "Integer32"
_WfModuleTimerFrequency_Object = MibTableColumn
wfModuleTimerFrequency = _WfModuleTimerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 3),
    _WfModuleTimerFrequency_Type()
)
wfModuleTimerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleTimerFrequency.setStatus("mandatory")


class _WfModuleBufferBalance_Type(Integer32):
    """Custom type wfModuleBufferBalance based on Integer32"""
    defaultValue = 1

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
        *(("none", 2),
          ("rx", 3),
          ("tx", 4),
          ("txrx", 1))
    )


_WfModuleBufferBalance_Type.__name__ = "Integer32"
_WfModuleBufferBalance_Object = MibTableColumn
wfModuleBufferBalance = _WfModuleBufferBalance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 4),
    _WfModuleBufferBalance_Type()
)
wfModuleBufferBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleBufferBalance.setStatus("mandatory")


class _WfModuleFddiWeight_Type(Integer32):
    """Custom type wfModuleFddiWeight based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleFddiWeight_Type.__name__ = "Integer32"
_WfModuleFddiWeight_Object = MibTableColumn
wfModuleFddiWeight = _WfModuleFddiWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 5),
    _WfModuleFddiWeight_Type()
)
wfModuleFddiWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleFddiWeight.setStatus("mandatory")


class _WfModuleTokenRingWeight_Type(Integer32):
    """Custom type wfModuleTokenRingWeight based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleTokenRingWeight_Type.__name__ = "Integer32"
_WfModuleTokenRingWeight_Object = MibTableColumn
wfModuleTokenRingWeight = _WfModuleTokenRingWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 6),
    _WfModuleTokenRingWeight_Type()
)
wfModuleTokenRingWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleTokenRingWeight.setStatus("mandatory")


class _WfModuleCsmacdWeight_Type(Integer32):
    """Custom type wfModuleCsmacdWeight based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleCsmacdWeight_Type.__name__ = "Integer32"
_WfModuleCsmacdWeight_Object = MibTableColumn
wfModuleCsmacdWeight = _WfModuleCsmacdWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 7),
    _WfModuleCsmacdWeight_Type()
)
wfModuleCsmacdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleCsmacdWeight.setStatus("mandatory")


class _WfModuleSyncWeight_Type(Integer32):
    """Custom type wfModuleSyncWeight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleSyncWeight_Type.__name__ = "Integer32"
_WfModuleSyncWeight_Object = MibTableColumn
wfModuleSyncWeight = _WfModuleSyncWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 8),
    _WfModuleSyncWeight_Type()
)
wfModuleSyncWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleSyncWeight.setStatus("mandatory")
_WfModuleFreeBufferCredits_Type = Integer32
_WfModuleFreeBufferCredits_Object = MibTableColumn
wfModuleFreeBufferCredits = _WfModuleFreeBufferCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 9),
    _WfModuleFreeBufferCredits_Type()
)
wfModuleFreeBufferCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModuleFreeBufferCredits.setStatus("mandatory")
_WfModuleTotalBufferCredits_Type = Integer32
_WfModuleTotalBufferCredits_Object = MibTableColumn
wfModuleTotalBufferCredits = _WfModuleTotalBufferCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 10),
    _WfModuleTotalBufferCredits_Type()
)
wfModuleTotalBufferCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModuleTotalBufferCredits.setStatus("mandatory")
_WfModuleRestart_Type = Integer32
_WfModuleRestart_Object = MibTableColumn
wfModuleRestart = _WfModuleRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 11),
    _WfModuleRestart_Type()
)
wfModuleRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleRestart.setStatus("mandatory")


class _WfModuleCsmacd100Weight_Type(Integer32):
    """Custom type wfModuleCsmacd100Weight based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleCsmacd100Weight_Type.__name__ = "Integer32"
_WfModuleCsmacd100Weight_Object = MibTableColumn
wfModuleCsmacd100Weight = _WfModuleCsmacd100Weight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 12),
    _WfModuleCsmacd100Weight_Type()
)
wfModuleCsmacd100Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleCsmacd100Weight.setStatus("mandatory")


class _WfModuleBisyncWeight_Type(Integer32):
    """Custom type wfModuleBisyncWeight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleBisyncWeight_Type.__name__ = "Integer32"
_WfModuleBisyncWeight_Object = MibTableColumn
wfModuleBisyncWeight = _WfModuleBisyncWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 13),
    _WfModuleBisyncWeight_Type()
)
wfModuleBisyncWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleBisyncWeight.setStatus("mandatory")


class _WfModuleHssiWeight_Type(Integer32):
    """Custom type wfModuleHssiWeight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModuleHssiWeight_Type.__name__ = "Integer32"
_WfModuleHssiWeight_Object = MibTableColumn
wfModuleHssiWeight = _WfModuleHssiWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4, 2, 1, 14),
    _WfModuleHssiWeight_Type()
)
wfModuleHssiWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModuleHssiWeight.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MODULE-MIB",
    **{"wfHwModuleTable": wfHwModuleTable,
       "wfHwModuleEntry": wfHwModuleEntry,
       "wfHwModuleSlot": wfHwModuleSlot,
       "wfHwModuleModule": wfHwModuleModule,
       "wfHwModuleModIdOpt": wfHwModuleModIdOpt,
       "wfHwModuleModRev": wfHwModuleModRev,
       "wfHwModuleModSerialNumber": wfHwModuleModSerialNumber,
       "wfHwModuleArtworkRev": wfHwModuleArtworkRev,
       "wfHwModuleMemorySize1": wfHwModuleMemorySize1,
       "wfHwModuleMemorySize2": wfHwModuleMemorySize2,
       "wfHwModuleDaughterBdIdOpt": wfHwModuleDaughterBdIdOpt,
       "wfHwModuleLEDStatus1": wfHwModuleLEDStatus1,
       "wfHwModuleLEDState1": wfHwModuleLEDState1,
       "wfHwModuleLEDStatus2": wfHwModuleLEDStatus2,
       "wfHwModuleLEDState2": wfHwModuleLEDState2,
       "wfHwModuleLEDStatus3": wfHwModuleLEDStatus3,
       "wfHwModuleLEDState3": wfHwModuleLEDState3,
       "wfModuleTable": wfModuleTable,
       "wfModuleEntry": wfModuleEntry,
       "wfModuleDelete": wfModuleDelete,
       "wfModuleSlot": wfModuleSlot,
       "wfModuleTimerFrequency": wfModuleTimerFrequency,
       "wfModuleBufferBalance": wfModuleBufferBalance,
       "wfModuleFddiWeight": wfModuleFddiWeight,
       "wfModuleTokenRingWeight": wfModuleTokenRingWeight,
       "wfModuleCsmacdWeight": wfModuleCsmacdWeight,
       "wfModuleSyncWeight": wfModuleSyncWeight,
       "wfModuleFreeBufferCredits": wfModuleFreeBufferCredits,
       "wfModuleTotalBufferCredits": wfModuleTotalBufferCredits,
       "wfModuleRestart": wfModuleRestart,
       "wfModuleCsmacd100Weight": wfModuleCsmacd100Weight,
       "wfModuleBisyncWeight": wfModuleBisyncWeight,
       "wfModuleHssiWeight": wfModuleHssiWeight}
)
