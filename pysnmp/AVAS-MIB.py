# SNMP MIB module (AVAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:29 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
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

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniAVAS_ObjectIdentity = ObjectIdentity
sniAVAS = _SniAVAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24)
)
_AvasProc_ObjectIdentity = ObjectIdentity
avasProc = _AvasProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1)
)


class _AvasPSumStat_Type(Integer32):
    """Custom type avasPSumStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              50,
              99,
              255)
        )
    )
    namedValues = NamedValues(
        *(("errorNet", 5),
          ("errorSignon", 50),
          ("errorSystem", 4),
          ("missing", 1),
          ("ready", 2),
          ("running", 3),
          ("undefined", 255),
          ("unknown", 99))
    )


_AvasPSumStat_Type.__name__ = "Integer32"
_AvasPSumStat_Object = MibScalar
avasPSumStat = _AvasPSumStat_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 1),
    _AvasPSumStat_Type()
)
avasPSumStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasPSumStat.setStatus("mandatory")


class _AvasPUpamStat_Type(Integer32):
    """Custom type avasPUpamStat based on Integer32"""
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
              99,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abended", 5),
          ("ended", 4),
          ("hold", 7),
          ("kill", 9),
          ("ready", 2),
          ("running", 3),
          ("shutdown", 8),
          ("started", 1),
          ("stop", 6),
          ("undefined", 255),
          ("unknown", 99))
    )


_AvasPUpamStat_Type.__name__ = "Integer32"
_AvasPUpamStat_Object = MibScalar
avasPUpamStat = _AvasPUpamStat_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 2),
    _AvasPUpamStat_Type()
)
avasPUpamStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasPUpamStat.setStatus("mandatory")


class _AvasPPlamStat_Type(Integer32):
    """Custom type avasPPlamStat based on Integer32"""
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
              99,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abended", 5),
          ("ended", 4),
          ("hold", 7),
          ("kill", 9),
          ("ready", 2),
          ("running", 3),
          ("shutdown", 8),
          ("started", 1),
          ("stop", 6),
          ("undefined", 255),
          ("unknown", 99))
    )


_AvasPPlamStat_Type.__name__ = "Integer32"
_AvasPPlamStat_Object = MibScalar
avasPPlamStat = _AvasPPlamStat_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 3),
    _AvasPPlamStat_Type()
)
avasPPlamStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasPPlamStat.setStatus("mandatory")


class _AvasPCentrStat_Type(Integer32):
    """Custom type avasPCentrStat based on Integer32"""
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
              99,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abended", 5),
          ("ended", 4),
          ("hold", 7),
          ("kill", 9),
          ("ready", 2),
          ("running", 3),
          ("shutdown", 8),
          ("started", 1),
          ("stop", 6),
          ("undefined", 255),
          ("unknown", 99))
    )


_AvasPCentrStat_Type.__name__ = "Integer32"
_AvasPCentrStat_Object = MibScalar
avasPCentrStat = _AvasPCentrStat_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 4),
    _AvasPCentrStat_Type()
)
avasPCentrStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasPCentrStat.setStatus("mandatory")
_AvasPAvakNum_Type = Integer32
_AvasPAvakNum_Object = MibScalar
avasPAvakNum = _AvasPAvakNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 5),
    _AvasPAvakNum_Type()
)
avasPAvakNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasPAvakNum.setStatus("mandatory")
_AvasPAvakTab_Object = MibTable
avasPAvakTab = _AvasPAvakTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6)
)
if mibBuilder.loadTexts:
    avasPAvakTab.setStatus("mandatory")
_AvasPAvakTabEntry_Object = MibTableRow
avasPAvakTabEntry = _AvasPAvakTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1)
)
avasPAvakTabEntry.setIndexNames(
    (0, "AVAS-MIB", "avasPAvakTabIndex"),
)
if mibBuilder.loadTexts:
    avasPAvakTabEntry.setStatus("mandatory")
_AvasPAvakTabIndex_Type = Integer32
_AvasPAvakTabIndex_Object = MibTableColumn
avasPAvakTabIndex = _AvasPAvakTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1, 1),
    _AvasPAvakTabIndex_Type()
)
avasPAvakTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasPAvakTabIndex.setStatus("mandatory")
_AvasPAvakJvName_Type = DisplayString
_AvasPAvakJvName_Object = MibTableColumn
avasPAvakJvName = _AvasPAvakJvName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1, 2),
    _AvasPAvakJvName_Type()
)
avasPAvakJvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasPAvakJvName.setStatus("mandatory")


class _AvasPAvakState_Type(Integer32):
    """Custom type avasPAvakState based on Integer32"""
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
              99,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abended", 5),
          ("ended", 4),
          ("hold", 7),
          ("kill", 9),
          ("ready", 2),
          ("running", 3),
          ("shutdown", 8),
          ("started", 1),
          ("stop", 6),
          ("undefined", 255),
          ("unknown", 99))
    )


_AvasPAvakState_Type.__name__ = "Integer32"
_AvasPAvakState_Object = MibTableColumn
avasPAvakState = _AvasPAvakState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1, 3),
    _AvasPAvakState_Type()
)
avasPAvakState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasPAvakState.setStatus("mandatory")
_AvasNet_ObjectIdentity = ObjectIdentity
avasNet = _AvasNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2)
)


class _AvasNStateF_Type(Integer32):
    """Custom type avasNStateF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              100)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("condwait", 9),
          ("error", 5),
          ("hold", 6),
          ("problem", 1),
          ("running", 7),
          ("waiting", 8))
    )


_AvasNStateF_Type.__name__ = "Integer32"
_AvasNStateF_Object = MibScalar
avasNStateF = _AvasNStateF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 1),
    _AvasNStateF_Type()
)
avasNStateF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasNStateF.setStatus("mandatory")
_AvasNPatF_Type = DisplayString
_AvasNPatF_Object = MibScalar
avasNPatF = _AvasNPatF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 2),
    _AvasNPatF_Type()
)
avasNPatF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasNPatF.setStatus("mandatory")
_AvasNNum_Type = Integer32
_AvasNNum_Object = MibScalar
avasNNum = _AvasNNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 3),
    _AvasNNum_Type()
)
avasNNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNNum.setStatus("mandatory")
_AvasNTab_Object = MibTable
avasNTab = _AvasNTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4)
)
if mibBuilder.loadTexts:
    avasNTab.setStatus("mandatory")
_AvasNTabEntry_Object = MibTableRow
avasNTabEntry = _AvasNTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1)
)
avasNTabEntry.setIndexNames(
    (0, "AVAS-MIB", "avasNTabIndex"),
)
if mibBuilder.loadTexts:
    avasNTabEntry.setStatus("mandatory")
_AvasNTabIndex_Type = Integer32
_AvasNTabIndex_Object = MibTableColumn
avasNTabIndex = _AvasNTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 1),
    _AvasNTabIndex_Type()
)
avasNTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNTabIndex.setStatus("mandatory")
_AvasNName_Type = DisplayString
_AvasNName_Object = MibTableColumn
avasNName = _AvasNName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 2),
    _AvasNName_Type()
)
avasNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNName.setStatus("mandatory")
_AvasNStart_Type = DisplayString
_AvasNStart_Object = MibTableColumn
avasNStart = _AvasNStart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 3),
    _AvasNStart_Type()
)
avasNStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNStart.setStatus("mandatory")


class _AvasNState_Type(Integer32):
    """Custom type avasNState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              14,
              17,
              21,
              99)
        )
    )
    namedValues = NamedValues(
        *(("abended", 3),
          ("condwait", 9),
          ("ended", 4),
          ("error", 5),
          ("hold", 6),
          ("ignored", 14),
          ("opwait", 12),
          ("restarted", 10),
          ("resumed", 11),
          ("running", 7),
          ("shifted", 21),
          ("start", 17),
          ("unknown", 99),
          ("waiting", 8))
    )


_AvasNState_Type.__name__ = "Integer32"
_AvasNState_Object = MibTableColumn
avasNState = _AvasNState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 4),
    _AvasNState_Type()
)
avasNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNState.setStatus("mandatory")


class _AvasNStateOfError_Type(Integer32):
    """Custom type avasNStateOfError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_AvasNStateOfError_Type.__name__ = "Integer32"
_AvasNStateOfError_Object = MibTableColumn
avasNStateOfError = _AvasNStateOfError_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 5),
    _AvasNStateOfError_Type()
)
avasNStateOfError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNStateOfError.setStatus("mandatory")


class _AvasNStateOfRestart_Type(Integer32):
    """Custom type avasNStateOfRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_AvasNStateOfRestart_Type.__name__ = "Integer32"
_AvasNStateOfRestart_Object = MibTableColumn
avasNStateOfRestart = _AvasNStateOfRestart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 6),
    _AvasNStateOfRestart_Type()
)
avasNStateOfRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNStateOfRestart.setStatus("mandatory")


class _AvasNStateOfCondwait_Type(Integer32):
    """Custom type avasNStateOfCondwait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_AvasNStateOfCondwait_Type.__name__ = "Integer32"
_AvasNStateOfCondwait_Object = MibTableColumn
avasNStateOfCondwait = _AvasNStateOfCondwait_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 7),
    _AvasNStateOfCondwait_Type()
)
avasNStateOfCondwait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNStateOfCondwait.setStatus("mandatory")


class _AvasNStateOfHold_Type(Integer32):
    """Custom type avasNStateOfHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_AvasNStateOfHold_Type.__name__ = "Integer32"
_AvasNStateOfHold_Object = MibTableColumn
avasNStateOfHold = _AvasNStateOfHold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 8),
    _AvasNStateOfHold_Type()
)
avasNStateOfHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNStateOfHold.setStatus("mandatory")
_AvasNAvak_Type = DisplayString
_AvasNAvak_Object = MibTableColumn
avasNAvak = _AvasNAvak_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 9),
    _AvasNAvak_Type()
)
avasNAvak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNAvak.setStatus("mandatory")
_AvasNStartedIndex_Type = Integer32
_AvasNStartedIndex_Object = MibTableColumn
avasNStartedIndex = _AvasNStartedIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 10),
    _AvasNStartedIndex_Type()
)
avasNStartedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNStartedIndex.setStatus("mandatory")
_AvasNText_Type = DisplayString
_AvasNText_Object = MibTableColumn
avasNText = _AvasNText_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 11),
    _AvasNText_Type()
)
avasNText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasNText.setStatus("mandatory")
_AvasElem_ObjectIdentity = ObjectIdentity
avasElem = _AvasElem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3)
)


class _AvasEEStateF_Type(Integer32):
    """Custom type avasEEStateF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8,
              13,
              23)
        )
    )
    namedValues = NamedValues(
        *(("abended", 3),
          ("all", 1),
          ("error", 5),
          ("hold", 6),
          ("no-occure", 23),
          ("running-exec", 7),
          ("skipped", 13),
          ("waiting", 8))
    )


_AvasEEStateF_Type.__name__ = "Integer32"
_AvasEEStateF_Object = MibScalar
avasEEStateF = _AvasEEStateF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 1),
    _AvasEEStateF_Type()
)
avasEEStateF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasEEStateF.setStatus("mandatory")


class _AvasEETypeF_Type(Integer32):
    """Custom type avasEETypeF based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ext", 4),
          ("job", 7),
          ("jva", 3),
          ("mod", 5),
          ("net", 2),
          ("res", 8),
          ("std", 6),
          ("tim", 10),
          ("val", 9))
    )


_AvasEETypeF_Type.__name__ = "Integer32"
_AvasEETypeF_Object = MibScalar
avasEETypeF = _AvasEETypeF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 2),
    _AvasEETypeF_Type()
)
avasEETypeF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasEETypeF.setStatus("mandatory")


class _AvasEEFuncF_Type(Integer32):
    """Custom type avasEEFuncF based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("add", 5),
          ("all", 1),
          ("comp", 4),
          ("delete", 6),
          ("job", 2),
          ("modify", 7),
          ("net", 8),
          ("proc", 3),
          ("wait", 9))
    )


_AvasEEFuncF_Type.__name__ = "Integer32"
_AvasEEFuncF_Object = MibScalar
avasEEFuncF = _AvasEEFuncF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 3),
    _AvasEEFuncF_Type()
)
avasEEFuncF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasEEFuncF.setStatus("mandatory")


class _AvasENStateF_Type(Integer32):
    """Custom type avasENStateF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              100)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("condwait", 9),
          ("error", 5),
          ("hold", 6),
          ("problem", 1),
          ("running", 7),
          ("waiting", 8))
    )


_AvasENStateF_Type.__name__ = "Integer32"
_AvasENStateF_Object = MibScalar
avasENStateF = _AvasENStateF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 4),
    _AvasENStateF_Type()
)
avasENStateF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasENStateF.setStatus("mandatory")
_AvasENPatF_Type = DisplayString
_AvasENPatF_Object = MibScalar
avasENPatF = _AvasENPatF_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 5),
    _AvasENPatF_Type()
)
avasENPatF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasENPatF.setStatus("mandatory")
_AvasENum_Type = Integer32
_AvasENum_Object = MibScalar
avasENum = _AvasENum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 6),
    _AvasENum_Type()
)
avasENum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasENum.setStatus("mandatory")
_AvasETab_Object = MibTable
avasETab = _AvasETab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7)
)
if mibBuilder.loadTexts:
    avasETab.setStatus("mandatory")
_AvasETabEntry_Object = MibTableRow
avasETabEntry = _AvasETabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1)
)
avasETabEntry.setIndexNames(
    (0, "AVAS-MIB", "avasETabIndex"),
)
if mibBuilder.loadTexts:
    avasETabEntry.setStatus("mandatory")
_AvasETabIndex_Type = Integer32
_AvasETabIndex_Object = MibTableColumn
avasETabIndex = _AvasETabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 1),
    _AvasETabIndex_Type()
)
avasETabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasETabIndex.setStatus("mandatory")
_AvasEName_Type = DisplayString
_AvasEName_Object = MibTableColumn
avasEName = _AvasEName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 2),
    _AvasEName_Type()
)
avasEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEName.setStatus("mandatory")


class _AvasEFu_Type(Integer32):
    """Custom type avasEFu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              99)
        )
    )
    namedValues = NamedValues(
        *(("add", 5),
          ("comp", 4),
          ("delete", 6),
          ("job", 2),
          ("modify", 7),
          ("net", 8),
          ("proc", 3),
          ("unknown", 99),
          ("wait", 9))
    )


_AvasEFu_Type.__name__ = "Integer32"
_AvasEFu_Object = MibTableColumn
avasEFu = _AvasEFu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 3),
    _AvasEFu_Type()
)
avasEFu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEFu.setStatus("mandatory")


class _AvasEType_Type(Integer32):
    """Custom type avasEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ext", 4),
          ("job", 7),
          ("jva", 3),
          ("mod", 5),
          ("net", 2),
          ("res", 8),
          ("std", 6),
          ("tim", 10),
          ("unknown", 99),
          ("val", 9))
    )


_AvasEType_Type.__name__ = "Integer32"
_AvasEType_Object = MibTableColumn
avasEType = _AvasEType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 4),
    _AvasEType_Type()
)
avasEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEType.setStatus("mandatory")


class _AvasEInd_Type(Integer32):
    """Custom type avasEInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AvasEInd_Type.__name__ = "Integer32"
_AvasEInd_Object = MibTableColumn
avasEInd = _AvasEInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 5),
    _AvasEInd_Type()
)
avasEInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEInd.setStatus("mandatory")


class _AvasESynInd_Type(Integer32):
    """Custom type avasESynInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AvasESynInd_Type.__name__ = "Integer32"
_AvasESynInd_Object = MibTableColumn
avasESynInd = _AvasESynInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 6),
    _AvasESynInd_Type()
)
avasESynInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasESynInd.setStatus("mandatory")


class _AvasEState_Type(Integer32):
    """Custom type avasEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              13,
              14,
              16,
              18,
              19,
              20,
              22,
              23,
              66,
              99)
        )
    )
    namedValues = NamedValues(
        *(("abended", 3),
          ("created", 2),
          ("deleted", 19),
          ("ended", 4),
          ("error", 5),
          ("error-cat", 66),
          ("executed", 16),
          ("hold", 6),
          ("ignored", 14),
          ("no-occure", 23),
          ("no-plan", 18),
          ("no-submit", 20),
          ("occurred", 22),
          ("running", 7),
          ("skipped", 13),
          ("unknown", 99),
          ("waiting", 8))
    )


_AvasEState_Type.__name__ = "Integer32"
_AvasEState_Object = MibTableColumn
avasEState = _AvasEState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 7),
    _AvasEState_Type()
)
avasEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEState.setStatus("mandatory")
_AvasENet_Type = DisplayString
_AvasENet_Object = MibTableColumn
avasENet = _AvasENet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 8),
    _AvasENet_Type()
)
avasENet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasENet.setStatus("mandatory")


class _AvasEDelSolution_Type(Integer32):
    """Custom type avasEDelSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("ignore", 2),
          ("start", 1),
          ("unknown", 99))
    )


_AvasEDelSolution_Type.__name__ = "Integer32"
_AvasEDelSolution_Object = MibTableColumn
avasEDelSolution = _AvasEDelSolution_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 9),
    _AvasEDelSolution_Type()
)
avasEDelSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEDelSolution.setStatus("mandatory")
_AvasELatest_Type = DisplayString
_AvasELatest_Object = MibTableColumn
avasELatest = _AvasELatest_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 10),
    _AvasELatest_Type()
)
avasELatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasELatest.setStatus("mandatory")
_AvasEJva_Type = DisplayString
_AvasEJva_Object = MibTableColumn
avasEJva = _AvasEJva_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 11),
    _AvasEJva_Type()
)
avasEJva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEJva.setStatus("mandatory")
_AvasEJvaValue_Type = DisplayString
_AvasEJvaValue_Object = MibTableColumn
avasEJvaValue = _AvasEJvaValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 12),
    _AvasEJvaValue_Type()
)
avasEJvaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasEJvaValue.setStatus("mandatory")
_AvasCond_ObjectIdentity = ObjectIdentity
avasCond = _AvasCond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4)
)


class _AvasCFlag_Type(Integer32):
    """Custom type avasCFlag based on Integer32"""
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
        *(("all", 1),
          ("error", 3),
          ("exclusiv", 5),
          ("free", 2),
          ("share", 4))
    )


_AvasCFlag_Type.__name__ = "Integer32"
_AvasCFlag_Object = MibScalar
avasCFlag = _AvasCFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 1),
    _AvasCFlag_Type()
)
avasCFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avasCFlag.setStatus("mandatory")
_AvasCNum_Type = Integer32
_AvasCNum_Object = MibScalar
avasCNum = _AvasCNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 2),
    _AvasCNum_Type()
)
avasCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCNum.setStatus("mandatory")
_AvasCTab_Object = MibTable
avasCTab = _AvasCTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3)
)
if mibBuilder.loadTexts:
    avasCTab.setStatus("mandatory")
_AvasCTabEntry_Object = MibTableRow
avasCTabEntry = _AvasCTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1)
)
avasCTabEntry.setIndexNames(
    (0, "AVAS-MIB", "avasCTabIndex"),
)
if mibBuilder.loadTexts:
    avasCTabEntry.setStatus("mandatory")
_AvasCTabIndex_Type = Integer32
_AvasCTabIndex_Object = MibTableColumn
avasCTabIndex = _AvasCTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 1),
    _AvasCTabIndex_Type()
)
avasCTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCTabIndex.setStatus("mandatory")
_AvasCName_Type = DisplayString
_AvasCName_Object = MibTableColumn
avasCName = _AvasCName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 2),
    _AvasCName_Type()
)
avasCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCName.setStatus("mandatory")


class _AvasCType_Type(Integer32):
    """Custom type avasCType based on Integer32"""
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
        *(("job", 2),
          ("net", 1),
          ("res", 3),
          ("val", 4))
    )


_AvasCType_Type.__name__ = "Integer32"
_AvasCType_Object = MibTableColumn
avasCType = _AvasCType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 3),
    _AvasCType_Type()
)
avasCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCType.setStatus("mandatory")


class _AvasCInd_Type(Integer32):
    """Custom type avasCInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AvasCInd_Type.__name__ = "Integer32"
_AvasCInd_Object = MibTableColumn
avasCInd = _AvasCInd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 4),
    _AvasCInd_Type()
)
avasCInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCInd.setStatus("mandatory")


class _AvasCState_Type(Integer32):
    """Custom type avasCState based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("abended", 4),
          ("created", 1),
          ("deleted", 2),
          ("ended", 3),
          ("error", 6),
          ("exclusiv", 12),
          ("free", 5),
          ("ignored", 7),
          ("no-plan", 8),
          ("no-submit", 9),
          ("shared", 11),
          ("skipped", 10))
    )


_AvasCState_Type.__name__ = "Integer32"
_AvasCState_Object = MibTableColumn
avasCState = _AvasCState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 5),
    _AvasCState_Type()
)
avasCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCState.setStatus("mandatory")


class _AvasCValue_Type(Integer32):
    """Custom type avasCValue based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("abended", 3),
          ("created", 1),
          ("deleted", 7),
          ("ended", 2),
          ("error", 6),
          ("exclusiv", 12),
          ("free", 5),
          ("ignored", 4),
          ("no-plan", 8),
          ("no-submit", 9),
          ("shared", 11),
          ("skipped", 10),
          ("value", 13))
    )


_AvasCValue_Type.__name__ = "Integer32"
_AvasCValue_Object = MibTableColumn
avasCValue = _AvasCValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 6),
    _AvasCValue_Type()
)
avasCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCValue.setStatus("mandatory")
_AvasCCreateBy_Type = DisplayString
_AvasCCreateBy_Object = MibTableColumn
avasCCreateBy = _AvasCCreateBy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 7),
    _AvasCCreateBy_Type()
)
avasCCreateBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCCreateBy.setStatus("mandatory")
_AvasCCreateDate_Type = DisplayString
_AvasCCreateDate_Object = MibTableColumn
avasCCreateDate = _AvasCCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 8),
    _AvasCCreateDate_Type()
)
avasCCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCCreateDate.setStatus("mandatory")
_AvasCUpdate_Type = DisplayString
_AvasCUpdate_Object = MibTableColumn
avasCUpdate = _AvasCUpdate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 9),
    _AvasCUpdate_Type()
)
avasCUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCUpdate.setStatus("mandatory")
_AvasCLifeTime_Type = DisplayString
_AvasCLifeTime_Object = MibTableColumn
avasCLifeTime = _AvasCLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 10),
    _AvasCLifeTime_Type()
)
avasCLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasCLifeTime.setStatus("mandatory")
_AvasGlobalData_ObjectIdentity = ObjectIdentity
avasGlobalData = _AvasGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 10)
)
_AvasagtVersion_Type = DisplayString
_AvasagtVersion_Object = MibScalar
avasagtVersion = _AvasagtVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 10, 1),
    _AvasagtVersion_Type()
)
avasagtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasagtVersion.setStatus("mandatory")
_AvasSystemID_Type = DisplayString
_AvasSystemID_Object = MibScalar
avasSystemID = _AvasSystemID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 10, 2),
    _AvasSystemID_Type()
)
avasSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasSystemID.setStatus("mandatory")
_AvasTraps_ObjectIdentity = ObjectIdentity
avasTraps = _AvasTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11)
)
_AvasTrapData_ObjectIdentity = ObjectIdentity
avasTrapData = _AvasTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 1)
)
_AvasLastMsg_Type = DisplayString
_AvasLastMsg_Object = MibScalar
avasLastMsg = _AvasLastMsg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 1, 1),
    _AvasLastMsg_Type()
)
avasLastMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avasLastMsg.setStatus("mandatory")
_AvasStateTraps_ObjectIdentity = ObjectIdentity
avasStateTraps = _AvasStateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10)
)
_AvasProblemTraps_ObjectIdentity = ObjectIdentity
avasProblemTraps = _AvasProblemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11)
)

# Managed Objects groups


# Notification objects

avasMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 301)
)
avasMissing.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasMissing.setStatus(
        ""
    )

avasReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 302)
)
avasReady.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasReady.setStatus(
        ""
    )

avasRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 303)
)
avasRunning.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasRunning.setStatus(
        ""
    )

avasErrorSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 304)
)
avasErrorSystem.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasErrorSystem.setStatus(
        ""
    )

avasErrorNet = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 305)
)
avasErrorNet.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasErrorNet.setStatus(
        ""
    )

avasProblemNet = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 307)
)
avasProblemNet.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasProblemNet.setStatus(
        ""
    )

avasErrorSignon = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10, 0, 350)
)
avasErrorSignon.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasErrorSignon.setStatus(
        ""
    )

avasNetAbended = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 311)
)
avasNetAbended.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasNetAbended.setStatus(
        ""
    )

avasNetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 312)
)
avasNetError.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasNetError.setStatus(
        ""
    )

avasNetRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 313)
)
avasNetRestarted.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasNetRestarted.setStatus(
        ""
    )

avasNetCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 314)
)
avasNetCancelled.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasNetCancelled.setStatus(
        ""
    )

avasJobAbended = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 321)
)
avasJobAbended.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasJobAbended.setStatus(
        ""
    )

avasJobError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 322)
)
avasJobError.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasJobError.setStatus(
        ""
    )

avasJobRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 323)
)
avasJobRestarted.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasJobRestarted.setStatus(
        ""
    )

avasJobCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 324)
)
avasJobCancelled.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasJobCancelled.setStatus(
        ""
    )

avasProcAbended = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 331)
)
avasProcAbended.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasProcAbended.setStatus(
        ""
    )

avasProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 332)
)
avasProcError.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasProcError.setStatus(
        ""
    )

avasProcRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 333)
)
avasProcRestarted.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasProcRestarted.setStatus(
        ""
    )

avasProcCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 334)
)
avasProcCancelled.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasProcCancelled.setStatus(
        ""
    )

avasUJobAbended = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 341)
)
avasUJobAbended.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasUJobAbended.setStatus(
        ""
    )

avasUJobError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 342)
)
avasUJobError.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasUJobError.setStatus(
        ""
    )

avasUJobRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 343)
)
avasUJobRestarted.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasUJobRestarted.setStatus(
        ""
    )

avasUJobCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11, 0, 344)
)
avasUJobCancelled.setObjects(
      *(("AVAS-MIB", "avasSystemID"),
        ("AVAS-MIB", "avasLastMsg"))
)
if mibBuilder.loadTexts:
    avasUJobCancelled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAS-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniAVAS": sniAVAS,
       "avasProc": avasProc,
       "avasPSumStat": avasPSumStat,
       "avasPUpamStat": avasPUpamStat,
       "avasPPlamStat": avasPPlamStat,
       "avasPCentrStat": avasPCentrStat,
       "avasPAvakNum": avasPAvakNum,
       "avasPAvakTab": avasPAvakTab,
       "avasPAvakTabEntry": avasPAvakTabEntry,
       "avasPAvakTabIndex": avasPAvakTabIndex,
       "avasPAvakJvName": avasPAvakJvName,
       "avasPAvakState": avasPAvakState,
       "avasNet": avasNet,
       "avasNStateF": avasNStateF,
       "avasNPatF": avasNPatF,
       "avasNNum": avasNNum,
       "avasNTab": avasNTab,
       "avasNTabEntry": avasNTabEntry,
       "avasNTabIndex": avasNTabIndex,
       "avasNName": avasNName,
       "avasNStart": avasNStart,
       "avasNState": avasNState,
       "avasNStateOfError": avasNStateOfError,
       "avasNStateOfRestart": avasNStateOfRestart,
       "avasNStateOfCondwait": avasNStateOfCondwait,
       "avasNStateOfHold": avasNStateOfHold,
       "avasNAvak": avasNAvak,
       "avasNStartedIndex": avasNStartedIndex,
       "avasNText": avasNText,
       "avasElem": avasElem,
       "avasEEStateF": avasEEStateF,
       "avasEETypeF": avasEETypeF,
       "avasEEFuncF": avasEEFuncF,
       "avasENStateF": avasENStateF,
       "avasENPatF": avasENPatF,
       "avasENum": avasENum,
       "avasETab": avasETab,
       "avasETabEntry": avasETabEntry,
       "avasETabIndex": avasETabIndex,
       "avasEName": avasEName,
       "avasEFu": avasEFu,
       "avasEType": avasEType,
       "avasEInd": avasEInd,
       "avasESynInd": avasESynInd,
       "avasEState": avasEState,
       "avasENet": avasENet,
       "avasEDelSolution": avasEDelSolution,
       "avasELatest": avasELatest,
       "avasEJva": avasEJva,
       "avasEJvaValue": avasEJvaValue,
       "avasCond": avasCond,
       "avasCFlag": avasCFlag,
       "avasCNum": avasCNum,
       "avasCTab": avasCTab,
       "avasCTabEntry": avasCTabEntry,
       "avasCTabIndex": avasCTabIndex,
       "avasCName": avasCName,
       "avasCType": avasCType,
       "avasCInd": avasCInd,
       "avasCState": avasCState,
       "avasCValue": avasCValue,
       "avasCCreateBy": avasCCreateBy,
       "avasCCreateDate": avasCCreateDate,
       "avasCUpdate": avasCUpdate,
       "avasCLifeTime": avasCLifeTime,
       "avasGlobalData": avasGlobalData,
       "avasagtVersion": avasagtVersion,
       "avasSystemID": avasSystemID,
       "avasTraps": avasTraps,
       "avasTrapData": avasTrapData,
       "avasLastMsg": avasLastMsg,
       "avasStateTraps": avasStateTraps,
       "avasMissing": avasMissing,
       "avasReady": avasReady,
       "avasRunning": avasRunning,
       "avasErrorSystem": avasErrorSystem,
       "avasErrorNet": avasErrorNet,
       "avasProblemNet": avasProblemNet,
       "avasErrorSignon": avasErrorSignon,
       "avasProblemTraps": avasProblemTraps,
       "avasNetAbended": avasNetAbended,
       "avasNetError": avasNetError,
       "avasNetRestarted": avasNetRestarted,
       "avasNetCancelled": avasNetCancelled,
       "avasJobAbended": avasJobAbended,
       "avasJobError": avasJobError,
       "avasJobRestarted": avasJobRestarted,
       "avasJobCancelled": avasJobCancelled,
       "avasProcAbended": avasProcAbended,
       "avasProcError": avasProcError,
       "avasProcRestarted": avasProcRestarted,
       "avasProcCancelled": avasProcCancelled,
       "avasUJobAbended": avasUJobAbended,
       "avasUJobError": avasUJobError,
       "avasUJobRestarted": avasUJobRestarted,
       "avasUJobCancelled": avasUJobCancelled}
)
