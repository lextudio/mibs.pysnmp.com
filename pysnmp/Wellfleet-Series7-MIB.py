# SNMP MIB module (Wellfleet-Series7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-Series7-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:14 2024
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
 Opaque,
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
    "Opaque",
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

_Wellfleet_ObjectIdentity = ObjectIdentity
wellfleet = _Wellfleet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18)
)
_WfSwSeries7_ObjectIdentity = ObjectIdentity
wfSwSeries7 = _WfSwSeries7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3)
)
_WfHardwareConfig_ObjectIdentity = ObjectIdentity
wfHardwareConfig = _WfHardwareConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1)
)
_WfHwBase_ObjectIdentity = ObjectIdentity
wfHwBase = _WfHwBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1)
)


class _WfHwBpIdOpt_Type(Integer32):
    """Custom type wfHwBpIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              16640,
              16896)
        )
    )
    namedValues = NamedValues(
        *(("acecn", 3),
          ("acefn", 1),
          ("aceln", 2),
          ("fns", 4),
          ("frecn", 16896),
          ("freln", 16640),
          ("in", 5))
    )


_WfHwBpIdOpt_Type.__name__ = "Integer32"
_WfHwBpIdOpt_Object = MibScalar
wfHwBpIdOpt = _WfHwBpIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 1),
    _WfHwBpIdOpt_Type()
)
wfHwBpIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBpIdOpt.setStatus("mandatory")
_WfHwBpRev_Type = OctetString
_WfHwBpRev_Object = MibScalar
wfHwBpRev = _WfHwBpRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 2),
    _WfHwBpRev_Type()
)
wfHwBpRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBpRev.setStatus("mandatory")
_WfHwBpSerialNumber_Type = OctetString
_WfHwBpSerialNumber_Object = MibScalar
wfHwBpSerialNumber = _WfHwBpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 3),
    _WfHwBpSerialNumber_Type()
)
wfHwBpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBpSerialNumber.setStatus("mandatory")


class _WfBCNPwrSupply1_Type(Integer32):
    """Custom type wfBCNPwrSupply1 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply1_Type.__name__ = "Integer32"
_WfBCNPwrSupply1_Object = MibScalar
wfBCNPwrSupply1 = _WfBCNPwrSupply1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 4),
    _WfBCNPwrSupply1_Type()
)
wfBCNPwrSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply1.setStatus("mandatory")


class _WfBCNPwrSupply2_Type(Integer32):
    """Custom type wfBCNPwrSupply2 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply2_Type.__name__ = "Integer32"
_WfBCNPwrSupply2_Object = MibScalar
wfBCNPwrSupply2 = _WfBCNPwrSupply2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 5),
    _WfBCNPwrSupply2_Type()
)
wfBCNPwrSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply2.setStatus("mandatory")


class _WfBCNPwrSupply3_Type(Integer32):
    """Custom type wfBCNPwrSupply3 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply3_Type.__name__ = "Integer32"
_WfBCNPwrSupply3_Object = MibScalar
wfBCNPwrSupply3 = _WfBCNPwrSupply3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 6),
    _WfBCNPwrSupply3_Type()
)
wfBCNPwrSupply3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply3.setStatus("mandatory")


class _WfBCNPwrSupply4_Type(Integer32):
    """Custom type wfBCNPwrSupply4 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply4_Type.__name__ = "Integer32"
_WfBCNPwrSupply4_Object = MibScalar
wfBCNPwrSupply4 = _WfBCNPwrSupply4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 7),
    _WfBCNPwrSupply4_Type()
)
wfBCNPwrSupply4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply4.setStatus("mandatory")


class _WfBCNFanStatus_Type(Integer32):
    """Custom type wfBCNFanStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNFanStatus_Type.__name__ = "Integer32"
_WfBCNFanStatus_Object = MibScalar
wfBCNFanStatus = _WfBCNFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 8),
    _WfBCNFanStatus_Type()
)
wfBCNFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNFanStatus.setStatus("mandatory")


class _WfBCNTemperature_Type(Integer32):
    """Custom type wfBCNTemperature based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("caution", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNTemperature_Type.__name__ = "Integer32"
_WfBCNTemperature_Object = MibScalar
wfBCNTemperature = _WfBCNTemperature_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 9),
    _WfBCNTemperature_Type()
)
wfBCNTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNTemperature.setStatus("mandatory")
_WfHwTable_Object = MibTable
wfHwTable = _WfHwTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wfHwTable.setStatus("mandatory")
_WfHwEntry_Object = MibTableRow
wfHwEntry = _WfHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1)
)
wfHwEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfHwSlot"),
)
if mibBuilder.loadTexts:
    wfHwEntry.setStatus("mandatory")
_WfHwSlot_Type = Integer32
_WfHwSlot_Object = MibTableColumn
wfHwSlot = _WfHwSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 1),
    _WfHwSlot_Type()
)
wfHwSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSlot.setStatus("mandatory")


class _WfHwModIdOpt_Type(Integer32):
    """Custom type wfHwModIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              16,
              17,
              24,
              32,
              33,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              56,
              57,
              58,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              88,
              89,
              104,
              112,
              113,
              114,
              116,
              117,
              118,
              119,
              120,
              132,
              156,
              160,
              161,
              162,
              164,
              165,
              168,
              176,
              184,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              208,
              216,
              217,
              224,
              225,
              8448)
        )
    )
    namedValues = NamedValues(
        *(("cmcfddi", 88),
          ("def", 165),
          ("denf", 161),
          ("dhssi", 224),
          ("dsde1", 112),
          ("dsde10bt", 120),
          ("dsde1a", 113),
          ("dsde2", 156),
          ("dse1", 32),
          ("dse1a", 33),
          ("dse2", 116),
          ("dse2a", 117),
          ("dst4", 42),
          ("dst416", 40),
          ("dt", 104),
          ("dtok", 176),
          ("e1", 61),
          ("e1n", 68),
          ("enet", 114),
          ("enet1", 1),
          ("enet2", 8),
          ("enet3", 132),
          ("floppy", 48),
          ("fnsdsdt", 216),
          ("fnsdse", 208),
          ("fnsdst", 217),
          ("iphfddi", 89),
          ("mce1", 184),
          ("mct1", 168),
          ("oldqenf", 160),
          ("qef", 164),
          ("qenf", 162),
          ("se1", 63),
          ("se1n", 69),
          ("shssi", 225),
          ("srml", 8448),
          ("sse", 118),
          ("ssea", 119),
          ("sst4", 46),
          ("sst416", 44),
          ("sst416a", 41),
          ("sst4a", 43),
          ("st1", 58),
          ("st156k", 62),
          ("st156kn", 67),
          ("st1n", 65),
          ("stok4", 47),
          ("stok416", 45),
          ("sync", 80),
          ("sync1", 16),
          ("sync1a", 17),
          ("sync2a", 81),
          ("t11", 24),
          ("t12", 56),
          ("t12a", 57),
          ("t12n", 64),
          ("t156k", 60),
          ("t156kn", 66),
          ("wffddi1m", 193),
          ("wffddi1mf", 197),
          ("wffddi1s", 195),
          ("wffddi1sf", 199),
          ("wffddi2m", 192),
          ("wffddi2mf", 196),
          ("wffddi2s", 194),
          ("wffddi2sf", 198))
    )


_WfHwModIdOpt_Type.__name__ = "Integer32"
_WfHwModIdOpt_Object = MibTableColumn
wfHwModIdOpt = _WfHwModIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 2),
    _WfHwModIdOpt_Type()
)
wfHwModIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModIdOpt.setStatus("mandatory")
_WfHwModRev_Type = OctetString
_WfHwModRev_Object = MibTableColumn
wfHwModRev = _WfHwModRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 3),
    _WfHwModRev_Type()
)
wfHwModRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModRev.setStatus("mandatory")
_WfHwModSerialNumber_Type = OctetString
_WfHwModSerialNumber_Object = MibTableColumn
wfHwModSerialNumber = _WfHwModSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 4),
    _WfHwModSerialNumber_Type()
)
wfHwModSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModSerialNumber.setStatus("mandatory")


class _WfHwMotherBdIdOpt_Type(Integer32):
    """Custom type wfHwMotherBdIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              256,
              8704)
        )
    )
    namedValues = NamedValues(
        *(("ace12", 2),
          ("ace25", 3),
          ("ace32", 4),
          ("fns", 5),
          ("fre", 256),
          ("in", 6),
          ("srmf", 8704),
          ("sysctrl", 1))
    )


_WfHwMotherBdIdOpt_Type.__name__ = "Integer32"
_WfHwMotherBdIdOpt_Object = MibTableColumn
wfHwMotherBdIdOpt = _WfHwMotherBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 5),
    _WfHwMotherBdIdOpt_Type()
)
wfHwMotherBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdIdOpt.setStatus("mandatory")
_WfHwMotherBdRev_Type = OctetString
_WfHwMotherBdRev_Object = MibTableColumn
wfHwMotherBdRev = _WfHwMotherBdRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 6),
    _WfHwMotherBdRev_Type()
)
wfHwMotherBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdRev.setStatus("mandatory")
_WfHwMotherBdSerialNumber_Type = OctetString
_WfHwMotherBdSerialNumber_Object = MibTableColumn
wfHwMotherBdSerialNumber = _WfHwMotherBdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 7),
    _WfHwMotherBdSerialNumber_Type()
)
wfHwMotherBdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdSerialNumber.setStatus("mandatory")


class _WfHwDaughterBdIdOpt_Type(Integer32):
    """Custom type wfHwDaughterBdIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              4352,
              4608)
        )
    )
    namedValues = NamedValues(
        *(("ace68020mhz12", 2),
          ("ace68020mhz25", 3),
          ("ace68030mhz32", 4),
          ("fre68040mhz25", 4352),
          ("fre68040mhz33", 4608),
          ("sysctrl", 1))
    )


_WfHwDaughterBdIdOpt_Type.__name__ = "Integer32"
_WfHwDaughterBdIdOpt_Object = MibTableColumn
wfHwDaughterBdIdOpt = _WfHwDaughterBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 8),
    _WfHwDaughterBdIdOpt_Type()
)
wfHwDaughterBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDaughterBdIdOpt.setStatus("mandatory")
_WfHwDaughterBdRev_Type = OctetString
_WfHwDaughterBdRev_Object = MibTableColumn
wfHwDaughterBdRev = _WfHwDaughterBdRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 9),
    _WfHwDaughterBdRev_Type()
)
wfHwDaughterBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDaughterBdRev.setStatus("mandatory")
_WfHwDaughterBdSerialNumber_Type = OctetString
_WfHwDaughterBdSerialNumber_Object = MibTableColumn
wfHwDaughterBdSerialNumber = _WfHwDaughterBdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 10),
    _WfHwDaughterBdSerialNumber_Type()
)
wfHwDaughterBdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDaughterBdSerialNumber.setStatus("mandatory")
_WfHwBabyBdIdOpt_Type = Integer32
_WfHwBabyBdIdOpt_Object = MibTableColumn
wfHwBabyBdIdOpt = _WfHwBabyBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 11),
    _WfHwBabyBdIdOpt_Type()
)
wfHwBabyBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBabyBdIdOpt.setStatus("mandatory")
_WfHwBabyBdRev_Type = OctetString
_WfHwBabyBdRev_Object = MibTableColumn
wfHwBabyBdRev = _WfHwBabyBdRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 12),
    _WfHwBabyBdRev_Type()
)
wfHwBabyBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBabyBdRev.setStatus("mandatory")
_WfHwBabyBdSerialNumber_Type = OctetString
_WfHwBabyBdSerialNumber_Object = MibTableColumn
wfHwBabyBdSerialNumber = _WfHwBabyBdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 13),
    _WfHwBabyBdSerialNumber_Type()
)
wfHwBabyBdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBabyBdSerialNumber.setStatus("mandatory")
_WfHwDiagPromRev_Type = OctetString
_WfHwDiagPromRev_Object = MibTableColumn
wfHwDiagPromRev = _WfHwDiagPromRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 14),
    _WfHwDiagPromRev_Type()
)
wfHwDiagPromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDiagPromRev.setStatus("mandatory")
_WfHwDiagPromDate_Type = DisplayString
_WfHwDiagPromDate_Object = MibTableColumn
wfHwDiagPromDate = _WfHwDiagPromDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 15),
    _WfHwDiagPromDate_Type()
)
wfHwDiagPromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDiagPromDate.setStatus("mandatory")
_WfHwDiagPromSource_Type = DisplayString
_WfHwDiagPromSource_Object = MibTableColumn
wfHwDiagPromSource = _WfHwDiagPromSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 16),
    _WfHwDiagPromSource_Type()
)
wfHwDiagPromSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDiagPromSource.setStatus("mandatory")
_WfHwBootPromRev_Type = OctetString
_WfHwBootPromRev_Object = MibTableColumn
wfHwBootPromRev = _WfHwBootPromRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 17),
    _WfHwBootPromRev_Type()
)
wfHwBootPromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBootPromRev.setStatus("mandatory")
_WfHwBootPromDate_Type = DisplayString
_WfHwBootPromDate_Object = MibTableColumn
wfHwBootPromDate = _WfHwBootPromDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 18),
    _WfHwBootPromDate_Type()
)
wfHwBootPromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBootPromDate.setStatus("mandatory")
_WfHwBootPromSource_Type = DisplayString
_WfHwBootPromSource_Object = MibTableColumn
wfHwBootPromSource = _WfHwBootPromSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 19),
    _WfHwBootPromSource_Type()
)
wfHwBootPromSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBootPromSource.setStatus("mandatory")
_WfHwSparePromRev_Type = OctetString
_WfHwSparePromRev_Object = MibTableColumn
wfHwSparePromRev = _WfHwSparePromRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 20),
    _WfHwSparePromRev_Type()
)
wfHwSparePromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSparePromRev.setStatus("mandatory")
_WfHwSparePromDate_Type = DisplayString
_WfHwSparePromDate_Object = MibTableColumn
wfHwSparePromDate = _WfHwSparePromDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 21),
    _WfHwSparePromDate_Type()
)
wfHwSparePromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSparePromDate.setStatus("mandatory")
_WfHwSparePromSource_Type = DisplayString
_WfHwSparePromSource_Object = MibTableColumn
wfHwSparePromSource = _WfHwSparePromSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 22),
    _WfHwSparePromSource_Type()
)
wfHwSparePromSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSparePromSource.setStatus("mandatory")


class _WfHwFileSysPresent_Type(Integer32):
    """Custom type wfHwFileSysPresent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filesys", 1),
          ("nofilesys", 2))
    )


_WfHwFileSysPresent_Type.__name__ = "Integer32"
_WfHwFileSysPresent_Object = MibTableColumn
wfHwFileSysPresent = _WfHwFileSysPresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 23),
    _WfHwFileSysPresent_Type()
)
wfHwFileSysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwFileSysPresent.setStatus("mandatory")
_WfMod_ObjectIdentity = ObjectIdentity
wfMod = _WfMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3)
)


class _WfModState_Type(Integer32):
    """Custom type wfModState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("init", 1)
    )


_WfModState_Type.__name__ = "Integer32"
_WfModState_Object = MibScalar
wfModState = _WfModState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 1),
    _WfModState_Type()
)
wfModState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModState.setStatus("mandatory")
_WfModSlot_Type = Integer32
_WfModSlot_Object = MibScalar
wfModSlot = _WfModSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 2),
    _WfModSlot_Type()
)
wfModSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSlot.setStatus("mandatory")
_WfModIdOpt_Type = Integer32
_WfModIdOpt_Object = MibScalar
wfModIdOpt = _WfModIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 3),
    _WfModIdOpt_Type()
)
wfModIdOpt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIdOpt.setStatus("mandatory")
_WfModRev_Type = Integer32
_WfModRev_Object = MibScalar
wfModRev = _WfModRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 4),
    _WfModRev_Type()
)
wfModRev.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModRev.setStatus("mandatory")
_WfModProm_Type = Integer32
_WfModProm_Object = MibScalar
wfModProm = _WfModProm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 5),
    _WfModProm_Type()
)
wfModProm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModProm.setStatus("mandatory")
_WfModMidr_Type = Integer32
_WfModMidr_Object = MibScalar
wfModMidr = _WfModMidr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 6),
    _WfModMidr_Type()
)
wfModMidr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMidr.setStatus("mandatory")
_WfModMled_Type = Integer32
_WfModMled_Object = MibScalar
wfModMled = _WfModMled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 7),
    _WfModMled_Type()
)
wfModMled.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMled.setStatus("mandatory")
_WfModMisr_Type = Integer32
_WfModMisr_Object = MibScalar
wfModMisr = _WfModMisr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 8),
    _WfModMisr_Type()
)
wfModMisr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMisr.setStatus("mandatory")
_WfModSnprom_Type = Integer32
_WfModSnprom_Object = MibScalar
wfModSnprom = _WfModSnprom_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 9),
    _WfModSnprom_Type()
)
wfModSnprom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSnprom.setStatus("mandatory")
_WfModMadr1_Type = OctetString
_WfModMadr1_Object = MibScalar
wfModMadr1 = _WfModMadr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 10),
    _WfModMadr1_Type()
)
wfModMadr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr1.setStatus("mandatory")
_WfModMadr2_Type = OctetString
_WfModMadr2_Object = MibScalar
wfModMadr2 = _WfModMadr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 11),
    _WfModMadr2_Type()
)
wfModMadr2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr2.setStatus("mandatory")
_WfModMadr3_Type = OctetString
_WfModMadr3_Object = MibScalar
wfModMadr3 = _WfModMadr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 12),
    _WfModMadr3_Type()
)
wfModMadr3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr3.setStatus("mandatory")
_WfModMadr4_Type = OctetString
_WfModMadr4_Object = MibScalar
wfModMadr4 = _WfModMadr4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 13),
    _WfModMadr4_Type()
)
wfModMadr4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMadr4.setStatus("mandatory")
_WfModLance1_Type = Integer32
_WfModLance1_Object = MibScalar
wfModLance1 = _WfModLance1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 14),
    _WfModLance1_Type()
)
wfModLance1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModLance1.setStatus("mandatory")
_WfModLance2_Type = Integer32
_WfModLance2_Object = MibScalar
wfModLance2 = _WfModLance2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 15),
    _WfModLance2_Type()
)
wfModLance2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModLance2.setStatus("mandatory")
_WfModMk50251_Type = Integer32
_WfModMk50251_Object = MibScalar
wfModMk50251 = _WfModMk50251_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 16),
    _WfModMk50251_Type()
)
wfModMk50251.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50251.setStatus("mandatory")
_WfModMk50252_Type = Integer32
_WfModMk50252_Object = MibScalar
wfModMk50252 = _WfModMk50252_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 17),
    _WfModMk50252_Type()
)
wfModMk50252.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50252.setStatus("mandatory")
_WfModMk50253_Type = Integer32
_WfModMk50253_Object = MibScalar
wfModMk50253 = _WfModMk50253_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 18),
    _WfModMk50253_Type()
)
wfModMk50253.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50253.setStatus("mandatory")
_WfModMk50254_Type = Integer32
_WfModMk50254_Object = MibScalar
wfModMk50254 = _WfModMk50254_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 19),
    _WfModMk50254_Type()
)
wfModMk50254.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMk50254.setStatus("mandatory")
_WfModSicr_Type = Integer32
_WfModSicr_Object = MibScalar
wfModSicr = _WfModSicr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 20),
    _WfModSicr_Type()
)
wfModSicr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSicr.setStatus("mandatory")
_WfModSbrr_Type = Integer32
_WfModSbrr_Object = MibScalar
wfModSbrr = _WfModSbrr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 21),
    _WfModSbrr_Type()
)
wfModSbrr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModSbrr.setStatus("mandatory")
_WfMod8530_Type = Integer32
_WfMod8530_Object = MibScalar
wfMod8530 = _WfMod8530_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 22),
    _WfMod8530_Type()
)
wfMod8530.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfMod8530.setStatus("mandatory")
_WfModCar_Type = Integer32
_WfModCar_Object = MibScalar
wfModCar = _WfModCar_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 23),
    _WfModCar_Type()
)
wfModCar.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCar.setStatus("mandatory")
_WfModDefaA_Type = Integer32
_WfModDefaA_Object = MibScalar
wfModDefaA = _WfModDefaA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 24),
    _WfModDefaA_Type()
)
wfModDefaA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModDefaA.setStatus("mandatory")
_WfModCamALock_Type = Integer32
_WfModCamALock_Object = MibScalar
wfModCamALock = _WfModCamALock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 25),
    _WfModCamALock_Type()
)
wfModCamALock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamALock.setStatus("mandatory")
_WfModCamAUnlock_Type = Integer32
_WfModCamAUnlock_Object = MibScalar
wfModCamAUnlock = _WfModCamAUnlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 26),
    _WfModCamAUnlock_Type()
)
wfModCamAUnlock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamAUnlock.setStatus("mandatory")
_WfModDefaB_Type = Integer32
_WfModDefaB_Object = MibScalar
wfModDefaB = _WfModDefaB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 27),
    _WfModDefaB_Type()
)
wfModDefaB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModDefaB.setStatus("mandatory")
_WfModCamBLock_Type = Integer32
_WfModCamBLock_Object = MibScalar
wfModCamBLock = _WfModCamBLock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 28),
    _WfModCamBLock_Type()
)
wfModCamBLock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamBLock.setStatus("mandatory")
_WfModCamBUnlock_Type = Integer32
_WfModCamBUnlock_Object = MibScalar
wfModCamBUnlock = _WfModCamBUnlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 29),
    _WfModCamBUnlock_Type()
)
wfModCamBUnlock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModCamBUnlock.setStatus("mandatory")
_WfModIlacc1_Type = Integer32
_WfModIlacc1_Object = MibScalar
wfModIlacc1 = _WfModIlacc1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 30),
    _WfModIlacc1_Type()
)
wfModIlacc1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc1.setStatus("mandatory")
_WfModIlacc2_Type = Integer32
_WfModIlacc2_Object = MibScalar
wfModIlacc2 = _WfModIlacc2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 31),
    _WfModIlacc2_Type()
)
wfModIlacc2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc2.setStatus("mandatory")
_WfModIlacc3_Type = Integer32
_WfModIlacc3_Object = MibScalar
wfModIlacc3 = _WfModIlacc3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 32),
    _WfModIlacc3_Type()
)
wfModIlacc3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc3.setStatus("mandatory")
_WfModIlacc4_Type = Integer32
_WfModIlacc4_Object = MibScalar
wfModIlacc4 = _WfModIlacc4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 33),
    _WfModIlacc4_Type()
)
wfModIlacc4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModIlacc4.setStatus("mandatory")
_WfModTms3801_Type = Integer32
_WfModTms3801_Object = MibScalar
wfModTms3801 = _WfModTms3801_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 34),
    _WfModTms3801_Type()
)
wfModTms3801.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTms3801.setStatus("mandatory")
_WfModTms3802_Type = Integer32
_WfModTms3802_Object = MibScalar
wfModTms3802 = _WfModTms3802_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 35),
    _WfModTms3802_Type()
)
wfModTms3802.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTms3802.setStatus("mandatory")
_WfModTocr_Type = Integer32
_WfModTocr_Object = MibScalar
wfModTocr = _WfModTocr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 36),
    _WfModTocr_Type()
)
wfModTocr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTocr.setStatus("mandatory")
_WfModTsra_Type = Integer32
_WfModTsra_Object = MibScalar
wfModTsra = _WfModTsra_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 37),
    _WfModTsra_Type()
)
wfModTsra.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTsra.setStatus("mandatory")
_WfModMuxram1_Type = Integer32
_WfModMuxram1_Object = MibScalar
wfModMuxram1 = _WfModMuxram1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 38),
    _WfModMuxram1_Type()
)
wfModMuxram1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMuxram1.setStatus("mandatory")
_WfModMuxram2_Type = Integer32
_WfModMuxram2_Object = MibScalar
wfModMuxram2 = _WfModMuxram2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 39),
    _WfModMuxram2_Type()
)
wfModMuxram2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMuxram2.setStatus("mandatory")
_WfModTicr_Type = Integer32
_WfModTicr_Object = MibScalar
wfModTicr = _WfModTicr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 40),
    _WfModTicr_Type()
)
wfModTicr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModTicr.setStatus("mandatory")
_WfModFramer1_Type = Integer32
_WfModFramer1_Object = MibScalar
wfModFramer1 = _WfModFramer1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 41),
    _WfModFramer1_Type()
)
wfModFramer1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFramer1.setStatus("mandatory")
_WfModFramer2_Type = Integer32
_WfModFramer2_Object = MibScalar
wfModFramer2 = _WfModFramer2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 42),
    _WfModFramer2_Type()
)
wfModFramer2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFramer2.setStatus("mandatory")
_WfModFsi1_Type = Integer32
_WfModFsi1_Object = MibScalar
wfModFsi1 = _WfModFsi1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 43),
    _WfModFsi1_Type()
)
wfModFsi1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModFsi1.setStatus("mandatory")
_WfModMac1_Type = Integer32
_WfModMac1_Object = MibScalar
wfModMac1 = _WfModMac1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 44),
    _WfModMac1_Type()
)
wfModMac1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMac1.setStatus("mandatory")
_WfModElmA1_Type = Integer32
_WfModElmA1_Object = MibScalar
wfModElmA1 = _WfModElmA1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 45),
    _WfModElmA1_Type()
)
wfModElmA1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModElmA1.setStatus("mandatory")
_WfModElmB1_Type = Integer32
_WfModElmB1_Object = MibScalar
wfModElmB1 = _WfModElmB1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 46),
    _WfModElmB1_Type()
)
wfModElmB1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModElmB1.setStatus("mandatory")
_WfModMcr1_Type = Integer32
_WfModMcr1_Object = MibScalar
wfModMcr1 = _WfModMcr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 47),
    _WfModMcr1_Type()
)
wfModMcr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModMcr1.setStatus("mandatory")
_WfModHssiFsi1_Type = Integer32
_WfModHssiFsi1_Object = MibScalar
wfModHssiFsi1 = _WfModHssiFsi1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 48),
    _WfModHssiFsi1_Type()
)
wfModHssiFsi1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiFsi1.setStatus("mandatory")
_WfModHssiFsi2_Type = Integer32
_WfModHssiFsi2_Object = MibScalar
wfModHssiFsi2 = _WfModHssiFsi2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 49),
    _WfModHssiFsi2_Type()
)
wfModHssiFsi2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiFsi2.setStatus("mandatory")
_WfModHssiUga1_Type = Integer32
_WfModHssiUga1_Object = MibScalar
wfModHssiUga1 = _WfModHssiUga1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 50),
    _WfModHssiUga1_Type()
)
wfModHssiUga1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiUga1.setStatus("mandatory")
_WfModHssiUga2_Type = Integer32
_WfModHssiUga2_Object = MibScalar
wfModHssiUga2 = _WfModHssiUga2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 51),
    _WfModHssiUga2_Type()
)
wfModHssiUga2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHssiUga2.setStatus("mandatory")
_WfModHicr_Type = Integer32
_WfModHicr_Object = MibScalar
wfModHicr = _WfModHicr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 52),
    _WfModHicr_Type()
)
wfModHicr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHicr.setStatus("mandatory")
_WfModHicrData_Type = Integer32
_WfModHicrData_Object = MibScalar
wfModHicrData = _WfModHicrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 53),
    _WfModHicrData_Type()
)
wfModHicrData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHicrData.setStatus("mandatory")
_WfModHlsr_Type = Integer32
_WfModHlsr_Object = MibScalar
wfModHlsr = _WfModHlsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 54),
    _WfModHlsr_Type()
)
wfModHlsr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHlsr.setStatus("mandatory")
_WfModHlsrData_Type = Integer32
_WfModHlsrData_Object = MibScalar
wfModHlsrData = _WfModHlsrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 3, 55),
    _WfModHlsrData_Type()
)
wfModHlsrData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfModHlsrData.setStatus("mandatory")
_WfSoftwareConfig_ObjectIdentity = ObjectIdentity
wfSoftwareConfig = _WfSoftwareConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2)
)
_WfProtocols_ObjectIdentity = ObjectIdentity
wfProtocols = _WfProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1)
)
_WfIPROTOLoad_Type = Counter32
_WfIPROTOLoad_Object = MibScalar
wfIPROTOLoad = _WfIPROTOLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 1),
    _WfIPROTOLoad_Type()
)
wfIPROTOLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPROTOLoad.setStatus("mandatory")
_WfDECNETLoad_Type = Counter32
_WfDECNETLoad_Object = MibScalar
wfDECNETLoad = _WfDECNETLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 2),
    _WfDECNETLoad_Type()
)
wfDECNETLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDECNETLoad.setStatus("mandatory")
_WfATLoad_Type = Counter32
_WfATLoad_Object = MibScalar
wfATLoad = _WfATLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 3),
    _WfATLoad_Type()
)
wfATLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATLoad.setStatus("mandatory")
_WfXNSLoad_Type = Counter32
_WfXNSLoad_Object = MibScalar
wfXNSLoad = _WfXNSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 4),
    _WfXNSLoad_Type()
)
wfXNSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXNSLoad.setStatus("mandatory")
_WfIPXLoad_Type = Counter32
_WfIPXLoad_Object = MibScalar
wfIPXLoad = _WfIPXLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 5),
    _WfIPXLoad_Type()
)
wfIPXLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPXLoad.setStatus("mandatory")
_WfOSILoad_Type = Counter32
_WfOSILoad_Object = MibScalar
wfOSILoad = _WfOSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 6),
    _WfOSILoad_Type()
)
wfOSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOSILoad.setStatus("mandatory")
_WfX25DTELoad_Type = Counter32
_WfX25DTELoad_Object = MibScalar
wfX25DTELoad = _WfX25DTELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 7),
    _WfX25DTELoad_Type()
)
wfX25DTELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25DTELoad.setStatus("mandatory")
_WfX25DCELoad_Type = Counter32
_WfX25DCELoad_Object = MibScalar
wfX25DCELoad = _WfX25DCELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 8),
    _WfX25DCELoad_Type()
)
wfX25DCELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25DCELoad.setStatus("mandatory")
_WfVINESLoad_Type = Counter32
_WfVINESLoad_Object = MibScalar
wfVINESLoad = _WfVINESLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 9),
    _WfVINESLoad_Type()
)
wfVINESLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVINESLoad.setStatus("mandatory")
_WfLinkModules_ObjectIdentity = ObjectIdentity
wfLinkModules = _WfLinkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2)
)
_WfENETIILoad_Type = Counter32
_WfENETIILoad_Object = MibScalar
wfENETIILoad = _WfENETIILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 1),
    _WfENETIILoad_Type()
)
wfENETIILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfENETIILoad.setStatus("mandatory")
_WfQENETLoad_Type = Counter32
_WfQENETLoad_Object = MibScalar
wfQENETLoad = _WfQENETLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 2),
    _WfQENETLoad_Type()
)
wfQENETLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQENETLoad.setStatus("mandatory")
_WfFDDILoad_Type = Counter32
_WfFDDILoad_Object = MibScalar
wfFDDILoad = _WfFDDILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 3),
    _WfFDDILoad_Type()
)
wfFDDILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDILoad.setStatus("mandatory")
_WfDSDELoad_Type = Counter32
_WfDSDELoad_Object = MibScalar
wfDSDELoad = _WfDSDELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 4),
    _WfDSDELoad_Type()
)
wfDSDELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDSDELoad.setStatus("mandatory")
_WfDSDEIILoad_Type = Counter32
_WfDSDEIILoad_Object = MibScalar
wfDSDEIILoad = _WfDSDEIILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 5),
    _WfDSDEIILoad_Type()
)
wfDSDEIILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDSDEIILoad.setStatus("mandatory")
_WfQSYNCLoad_Type = Counter32
_WfQSYNCLoad_Object = MibScalar
wfQSYNCLoad = _WfQSYNCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 6),
    _WfQSYNCLoad_Type()
)
wfQSYNCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQSYNCLoad.setStatus("mandatory")
_WfDTLoad_Type = Counter32
_WfDTLoad_Object = MibScalar
wfDTLoad = _WfDTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 7),
    _WfDTLoad_Type()
)
wfDTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDTLoad.setStatus("mandatory")
_WfDSTLoad_Type = Counter32
_WfDSTLoad_Object = MibScalar
wfDSTLoad = _WfDSTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 8),
    _WfDSTLoad_Type()
)
wfDSTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDSTLoad.setStatus("mandatory")
_WfT1IILoad_Type = Counter32
_WfT1IILoad_Object = MibScalar
wfT1IILoad = _WfT1IILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 9),
    _WfT1IILoad_Type()
)
wfT1IILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1IILoad.setStatus("mandatory")
_WfE1IILoad_Type = Counter32
_WfE1IILoad_Object = MibScalar
wfE1IILoad = _WfE1IILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 10),
    _WfE1IILoad_Type()
)
wfE1IILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1IILoad.setStatus("mandatory")
_WfHSSILoad_Type = Counter32
_WfHSSILoad_Object = MibScalar
wfHSSILoad = _WfHSSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 11),
    _WfHSSILoad_Type()
)
wfHSSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHSSILoad.setStatus("mandatory")
_WfFNSDSELoad_Type = Counter32
_WfFNSDSELoad_Object = MibScalar
wfFNSDSELoad = _WfFNSDSELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 12),
    _WfFNSDSELoad_Type()
)
wfFNSDSELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFNSDSELoad.setStatus("mandatory")
_WfFNSDSDTLoad_Type = Counter32
_WfFNSDSDTLoad_Object = MibScalar
wfFNSDSDTLoad = _WfFNSDSDTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 13),
    _WfFNSDSDTLoad_Type()
)
wfFNSDSDTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFNSDSDTLoad.setStatus("mandatory")
_WfDrivers_ObjectIdentity = ObjectIdentity
wfDrivers = _WfDrivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3)
)
_WfLANCELoad_Type = Counter32
_WfLANCELoad_Object = MibScalar
wfLANCELoad = _WfLANCELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 1),
    _WfLANCELoad_Type()
)
wfLANCELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLANCELoad.setStatus("mandatory")
_WfILACCLoad_Type = Counter32
_WfILACCLoad_Object = MibScalar
wfILACCLoad = _WfILACCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 2),
    _WfILACCLoad_Type()
)
wfILACCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfILACCLoad.setStatus("mandatory")
_WfFSILoad_Type = Counter32
_WfFSILoad_Object = MibScalar
wfFSILoad = _WfFSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 3),
    _WfFSILoad_Type()
)
wfFSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFSILoad.setStatus("mandatory")
_WfTMS380Load_Type = Counter32
_WfTMS380Load_Object = MibScalar
wfTMS380Load = _WfTMS380Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 4),
    _WfTMS380Load_Type()
)
wfTMS380Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTMS380Load.setStatus("mandatory")
_WfMK5025Load_Type = Counter32
_WfMK5025Load_Object = MibScalar
wfMK5025Load = _WfMK5025Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 5),
    _WfMK5025Load_Type()
)
wfMK5025Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMK5025Load.setStatus("mandatory")
_WfDS2180Load_Type = Counter32
_WfDS2180Load_Object = MibScalar
wfDS2180Load = _WfDS2180Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 6),
    _WfDS2180Load_Type()
)
wfDS2180Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDS2180Load.setStatus("mandatory")
_WfDS2181Load_Type = Counter32
_WfDS2181Load_Object = MibScalar
wfDS2181Load = _WfDS2181Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 7),
    _WfDS2181Load_Type()
)
wfDS2181Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDS2181Load.setStatus("mandatory")
_WfDEFALoad_Type = Counter32
_WfDEFALoad_Object = MibScalar
wfDEFALoad = _WfDEFALoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 8),
    _WfDEFALoad_Type()
)
wfDEFALoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDEFALoad.setStatus("mandatory")
_WfAMZ8530Load_Type = Counter32
_WfAMZ8530Load_Object = MibScalar
wfAMZ8530Load = _WfAMZ8530Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 9),
    _WfAMZ8530Load_Type()
)
wfAMZ8530Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAMZ8530Load.setStatus("mandatory")
_WfHSSIFSILoad_Type = Counter32
_WfHSSIFSILoad_Object = MibScalar
wfHSSIFSILoad = _WfHSSIFSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 10),
    _WfHSSIFSILoad_Type()
)
wfHSSIFSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHSSIFSILoad.setStatus("mandatory")
_WfSystem_ObjectIdentity = ObjectIdentity
wfSystem = _WfSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3)
)
_WfSys_ObjectIdentity = ObjectIdentity
wfSys = _WfSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1)
)
_WfSysDescr_Type = DisplayString
_WfSysDescr_Object = MibScalar
wfSysDescr = _WfSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 1),
    _WfSysDescr_Type()
)
wfSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysDescr.setStatus("mandatory")
_WfSysObjectID_Type = ObjectIdentifier
_WfSysObjectID_Object = MibScalar
wfSysObjectID = _WfSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 2),
    _WfSysObjectID_Type()
)
wfSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysObjectID.setStatus("mandatory")
_WfSysUpTime_Type = TimeTicks
_WfSysUpTime_Object = MibScalar
wfSysUpTime = _WfSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 3),
    _WfSysUpTime_Type()
)
wfSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysUpTime.setStatus("mandatory")
_WfSysContact_Type = DisplayString
_WfSysContact_Object = MibScalar
wfSysContact = _WfSysContact_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 4),
    _WfSysContact_Type()
)
wfSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysContact.setStatus("mandatory")
_WfSysName_Type = DisplayString
_WfSysName_Object = MibScalar
wfSysName = _WfSysName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 5),
    _WfSysName_Type()
)
wfSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysName.setStatus("mandatory")
_WfSysLocation_Type = DisplayString
_WfSysLocation_Object = MibScalar
wfSysLocation = _WfSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 6),
    _WfSysLocation_Type()
)
wfSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSysLocation.setStatus("mandatory")


class _WfSysServices_Type(Integer32):
    """Custom type wfSysServices based on Integer32"""
    defaultValue = 78


_WfSysServices_Object = MibScalar
wfSysServices = _WfSysServices_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 7),
    _WfSysServices_Type()
)
wfSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysServices.setStatus("mandatory")
_WfSysGmtOffset_Type = Integer32
_WfSysGmtOffset_Object = MibScalar
wfSysGmtOffset = _WfSysGmtOffset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 8),
    _WfSysGmtOffset_Type()
)
wfSysGmtOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysGmtOffset.setStatus("mandatory")
_WfSysMibVersion_Type = DisplayString
_WfSysMibVersion_Object = MibScalar
wfSysMibVersion = _WfSysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 1, 9),
    _WfSysMibVersion_Type()
)
wfSysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSysMibVersion.setStatus("mandatory")
_WfServices_ObjectIdentity = ObjectIdentity
wfServices = _WfServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2)
)
_WfConsole_ObjectIdentity = ObjectIdentity
wfConsole = _WfConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1)
)


class _WfBaudRate_Type(Integer32):
    """Custom type wfBaudRate based on Integer32"""
    defaultValue = 9600


_WfBaudRate_Object = MibScalar
wfBaudRate = _WfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 1),
    _WfBaudRate_Type()
)
wfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBaudRate.setStatus("mandatory")


class _WfDataBits_Type(Integer32):
    """Custom type wfDataBits based on Integer32"""
    defaultValue = 8


_WfDataBits_Object = MibScalar
wfDataBits = _WfDataBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 2),
    _WfDataBits_Type()
)
wfDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDataBits.setStatus("mandatory")


class _WfParity_Type(Integer32):
    """Custom type wfParity based on Integer32"""
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
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_WfParity_Type.__name__ = "Integer32"
_WfParity_Object = MibScalar
wfParity = _WfParity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 3),
    _WfParity_Type()
)
wfParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfParity.setStatus("mandatory")


class _WfStopBits_Type(Integer32):
    """Custom type wfStopBits based on Integer32"""
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
        *(("s15bit", 2),
          ("s1bit", 1),
          ("s2bit", 3))
    )


_WfStopBits_Type.__name__ = "Integer32"
_WfStopBits_Object = MibScalar
wfStopBits = _WfStopBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 4),
    _WfStopBits_Type()
)
wfStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStopBits.setStatus("mandatory")


class _WfModemEnable_Type(Integer32):
    """Custom type wfModemEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfModemEnable_Type.__name__ = "Integer32"
_WfModemEnable_Object = MibScalar
wfModemEnable = _WfModemEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 5),
    _WfModemEnable_Type()
)
wfModemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemEnable.setStatus("mandatory")


class _WfLinesPerScreen_Type(Integer32):
    """Custom type wfLinesPerScreen based on Integer32"""
    defaultValue = 24


_WfLinesPerScreen_Object = MibScalar
wfLinesPerScreen = _WfLinesPerScreen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 6),
    _WfLinesPerScreen_Type()
)
wfLinesPerScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLinesPerScreen.setStatus("mandatory")


class _WfMoreEnable_Type(Integer32):
    """Custom type wfMoreEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfMoreEnable_Type.__name__ = "Integer32"
_WfMoreEnable_Object = MibScalar
wfMoreEnable = _WfMoreEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 7),
    _WfMoreEnable_Type()
)
wfMoreEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMoreEnable.setStatus("mandatory")
_WfPrompt_Type = DisplayString
_WfPrompt_Object = MibScalar
wfPrompt = _WfPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 8),
    _WfPrompt_Type()
)
wfPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPrompt.setStatus("mandatory")


class _WfLoginTimeOut_Type(Integer32):
    """Custom type wfLoginTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 99),
          ("minimum", 1))
    )


_WfLoginTimeOut_Type.__name__ = "Integer32"
_WfLoginTimeOut_Object = MibScalar
wfLoginTimeOut = _WfLoginTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 9),
    _WfLoginTimeOut_Type()
)
wfLoginTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLoginTimeOut.setStatus("mandatory")


class _WfPasswordTimeOut_Type(Integer32):
    """Custom type wfPasswordTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 99),
          ("minimum", 1))
    )


_WfPasswordTimeOut_Type.__name__ = "Integer32"
_WfPasswordTimeOut_Object = MibScalar
wfPasswordTimeOut = _WfPasswordTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 10),
    _WfPasswordTimeOut_Type()
)
wfPasswordTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPasswordTimeOut.setStatus("mandatory")


class _WfCommandTimeOut_Type(Integer32):
    """Custom type wfCommandTimeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              15,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 15),
          ("maximum", 99),
          ("minimum", 1))
    )


_WfCommandTimeOut_Type.__name__ = "Integer32"
_WfCommandTimeOut_Object = MibScalar
wfCommandTimeOut = _WfCommandTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 11),
    _WfCommandTimeOut_Type()
)
wfCommandTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCommandTimeOut.setStatus("mandatory")


class _WfLoginRetries_Type(Integer32):
    """Custom type wfLoginRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("maximum", 99),
          ("minimum", 1))
    )


_WfLoginRetries_Type.__name__ = "Integer32"
_WfLoginRetries_Object = MibScalar
wfLoginRetries = _WfLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 12),
    _WfLoginRetries_Type()
)
wfLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLoginRetries.setStatus("mandatory")
_WfTotalLogins_Type = Counter32
_WfTotalLogins_Object = MibScalar
wfTotalLogins = _WfTotalLogins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 13),
    _WfTotalLogins_Type()
)
wfTotalLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTotalLogins.setStatus("mandatory")
_WfUserLoginErrors_Type = Counter32
_WfUserLoginErrors_Object = MibScalar
wfUserLoginErrors = _WfUserLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 14),
    _WfUserLoginErrors_Type()
)
wfUserLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserLoginErrors.setStatus("mandatory")
_WfManagerLoginErrors_Type = Counter32
_WfManagerLoginErrors_Object = MibScalar
wfManagerLoginErrors = _WfManagerLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 15),
    _WfManagerLoginErrors_Type()
)
wfManagerLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfManagerLoginErrors.setStatus("mandatory")
_WfOtherLoginErrors_Type = Counter32
_WfOtherLoginErrors_Object = MibScalar
wfOtherLoginErrors = _WfOtherLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 16),
    _WfOtherLoginErrors_Type()
)
wfOtherLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOtherLoginErrors.setStatus("mandatory")
_WfTtyFrameErrors_Type = Counter32
_WfTtyFrameErrors_Object = MibScalar
wfTtyFrameErrors = _WfTtyFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 17),
    _WfTtyFrameErrors_Type()
)
wfTtyFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyFrameErrors.setStatus("mandatory")
_WfTtyOverrunErrors_Type = Counter32
_WfTtyOverrunErrors_Object = MibScalar
wfTtyOverrunErrors = _WfTtyOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 18),
    _WfTtyOverrunErrors_Type()
)
wfTtyOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyOverrunErrors.setStatus("mandatory")
_WfTtyParityErrors_Type = Counter32
_WfTtyParityErrors_Object = MibScalar
wfTtyParityErrors = _WfTtyParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 19),
    _WfTtyParityErrors_Type()
)
wfTtyParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyParityErrors.setStatus("mandatory")
_WfTtyInfifoErrors_Type = Counter32
_WfTtyInfifoErrors_Object = MibScalar
wfTtyInfifoErrors = _WfTtyInfifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 20),
    _WfTtyInfifoErrors_Type()
)
wfTtyInfifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyInfifoErrors.setStatus("mandatory")
_WfTiRui_ObjectIdentity = ObjectIdentity
wfTiRui = _WfTiRui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2)
)


class _WfTiRuiState_Type(Integer32):
    """Custom type wfTiRuiState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 1))
    )


_WfTiRuiState_Type.__name__ = "Integer32"
_WfTiRuiState_Object = MibScalar
wfTiRuiState = _WfTiRuiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 1),
    _WfTiRuiState_Type()
)
wfTiRuiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiState.setStatus("optional")
_WfTiRuiAction_Type = DisplayString
_WfTiRuiAction_Object = MibScalar
wfTiRuiAction = _WfTiRuiAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 2),
    _WfTiRuiAction_Type()
)
wfTiRuiAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTiRuiAction.setStatus("optional")
_WfTiRuiResult_Type = DisplayString
_WfTiRuiResult_Object = MibScalar
wfTiRuiResult = _WfTiRuiResult_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 3),
    _WfTiRuiResult_Type()
)
wfTiRuiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiResult.setStatus("optional")
_WfTiRuiInReqs_Type = Counter32
_WfTiRuiInReqs_Object = MibScalar
wfTiRuiInReqs = _WfTiRuiInReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 4),
    _WfTiRuiInReqs_Type()
)
wfTiRuiInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiInReqs.setStatus("optional")
_WfTiRuiOutResults_Type = Counter32
_WfTiRuiOutResults_Object = MibScalar
wfTiRuiOutResults = _WfTiRuiOutResults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 5),
    _WfTiRuiOutResults_Type()
)
wfTiRuiOutResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiOutResults.setStatus("optional")
_WfTiRuiOutResultsErr_Type = Counter32
_WfTiRuiOutResultsErr_Object = MibScalar
wfTiRuiOutResultsErr = _WfTiRuiOutResultsErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 6),
    _WfTiRuiOutResultsErr_Type()
)
wfTiRuiOutResultsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiOutResultsErr.setStatus("optional")
_WfCircuitNameTable_Object = MibTable
wfCircuitNameTable = _WfCircuitNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    wfCircuitNameTable.setStatus("mandatory")
_WfCircuitNameEntry_Object = MibTableRow
wfCircuitNameEntry = _WfCircuitNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1)
)
wfCircuitNameEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfCircuitNumber"),
)
if mibBuilder.loadTexts:
    wfCircuitNameEntry.setStatus("mandatory")


class _WfCircuitNameDelete_Type(Integer32):
    """Custom type wfCircuitNameDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfCircuitNameDelete_Type.__name__ = "Integer32"
_WfCircuitNameDelete_Object = MibTableColumn
wfCircuitNameDelete = _WfCircuitNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 1),
    _WfCircuitNameDelete_Type()
)
wfCircuitNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitNameDelete.setStatus("mandatory")
_WfCircuitNumber_Type = Integer32
_WfCircuitNumber_Object = MibTableColumn
wfCircuitNumber = _WfCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 2),
    _WfCircuitNumber_Type()
)
wfCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCircuitNumber.setStatus("mandatory")
_WfCircuitName_Type = DisplayString
_WfCircuitName_Object = MibTableColumn
wfCircuitName = _WfCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 3),
    _WfCircuitName_Type()
)
wfCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitName.setStatus("mandatory")


class _WfCircuitIfType_Type(Integer32):
    """Custom type wfCircuitIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70)
        )
    )
    namedValues = NamedValues(
        *(("csmacd", 10),
          ("e1", 40),
          ("fddi", 60),
          ("hssi", 70),
          ("sync", 20),
          ("t1", 30),
          ("token", 50))
    )


_WfCircuitIfType_Type.__name__ = "Integer32"
_WfCircuitIfType_Object = MibTableColumn
wfCircuitIfType = _WfCircuitIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 4),
    _WfCircuitIfType_Type()
)
wfCircuitIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitIfType.setStatus("mandatory")
_WfCircuitProtoMap_Type = OctetString
_WfCircuitProtoMap_Object = MibTableColumn
wfCircuitProtoMap = _WfCircuitProtoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 3, 1, 5),
    _WfCircuitProtoMap_Type()
)
wfCircuitProtoMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCircuitProtoMap.setStatus("mandatory")
_WfGameGroup_ObjectIdentity = ObjectIdentity
wfGameGroup = _WfGameGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5)
)
_WfKernelTable_Object = MibTable
wfKernelTable = _WfKernelTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    wfKernelTable.setStatus("mandatory")
_WfKernelEntry_Object = MibTableRow
wfKernelEntry = _WfKernelEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1)
)
wfKernelEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfKernelSlot"),
)
if mibBuilder.loadTexts:
    wfKernelEntry.setStatus("mandatory")
_WfKernelSlot_Type = Integer32
_WfKernelSlot_Object = MibTableColumn
wfKernelSlot = _WfKernelSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 1),
    _WfKernelSlot_Type()
)
wfKernelSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelSlot.setStatus("mandatory")
_WfKernelMemorySize_Type = Integer32
_WfKernelMemorySize_Object = MibTableColumn
wfKernelMemorySize = _WfKernelMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 2),
    _WfKernelMemorySize_Type()
)
wfKernelMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemorySize.setStatus("mandatory")
_WfKernelMemoryFree_Type = Integer32
_WfKernelMemoryFree_Object = MibTableColumn
wfKernelMemoryFree = _WfKernelMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 3),
    _WfKernelMemoryFree_Type()
)
wfKernelMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemoryFree.setStatus("mandatory")
_WfKernelMemorySegsTotal_Type = Integer32
_WfKernelMemorySegsTotal_Object = MibTableColumn
wfKernelMemorySegsTotal = _WfKernelMemorySegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 4),
    _WfKernelMemorySegsTotal_Type()
)
wfKernelMemorySegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemorySegsTotal.setStatus("mandatory")
_WfKernelMemorySegsFree_Type = Integer32
_WfKernelMemorySegsFree_Object = MibTableColumn
wfKernelMemorySegsFree = _WfKernelMemorySegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 5),
    _WfKernelMemorySegsFree_Type()
)
wfKernelMemorySegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemorySegsFree.setStatus("mandatory")
_WfKernelMemoryMaxSegFree_Type = Integer32
_WfKernelMemoryMaxSegFree_Object = MibTableColumn
wfKernelMemoryMaxSegFree = _WfKernelMemoryMaxSegFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 6),
    _WfKernelMemoryMaxSegFree_Type()
)
wfKernelMemoryMaxSegFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemoryMaxSegFree.setStatus("mandatory")
_WfKernelBuffersTotal_Type = Integer32
_WfKernelBuffersTotal_Object = MibTableColumn
wfKernelBuffersTotal = _WfKernelBuffersTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 7),
    _WfKernelBuffersTotal_Type()
)
wfKernelBuffersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBuffersTotal.setStatus("mandatory")
_WfKernelBuffersFree_Type = Integer32
_WfKernelBuffersFree_Object = MibTableColumn
wfKernelBuffersFree = _WfKernelBuffersFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 8),
    _WfKernelBuffersFree_Type()
)
wfKernelBuffersFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBuffersFree.setStatus("mandatory")
_WfKernelTasksTotal_Type = Integer32
_WfKernelTasksTotal_Object = MibTableColumn
wfKernelTasksTotal = _WfKernelTasksTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 9),
    _WfKernelTasksTotal_Type()
)
wfKernelTasksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTasksTotal.setStatus("mandatory")
_WfKernelTasksInQueue_Type = Integer32
_WfKernelTasksInQueue_Object = MibTableColumn
wfKernelTasksInQueue = _WfKernelTasksInQueue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 10),
    _WfKernelTasksInQueue_Type()
)
wfKernelTasksInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTasksInQueue.setStatus("mandatory")
_WfKernelTimersTotal_Type = Integer32
_WfKernelTimersTotal_Object = MibTableColumn
wfKernelTimersTotal = _WfKernelTimersTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 11),
    _WfKernelTimersTotal_Type()
)
wfKernelTimersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTimersTotal.setStatus("mandatory")
_WfKernelTimersActive_Type = Integer32
_WfKernelTimersActive_Object = MibTableColumn
wfKernelTimersActive = _WfKernelTimersActive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 12),
    _WfKernelTimersActive_Type()
)
wfKernelTimersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTimersActive.setStatus("mandatory")
_WfKernelBufOwnerTask1_Type = DisplayString
_WfKernelBufOwnerTask1_Object = MibTableColumn
wfKernelBufOwnerTask1 = _WfKernelBufOwnerTask1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 13),
    _WfKernelBufOwnerTask1_Type()
)
wfKernelBufOwnerTask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask1.setStatus("mandatory")
_WfKernelBufOwnerTask1Bufs_Type = Integer32
_WfKernelBufOwnerTask1Bufs_Object = MibTableColumn
wfKernelBufOwnerTask1Bufs = _WfKernelBufOwnerTask1Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 14),
    _WfKernelBufOwnerTask1Bufs_Type()
)
wfKernelBufOwnerTask1Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask1Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask2_Type = DisplayString
_WfKernelBufOwnerTask2_Object = MibTableColumn
wfKernelBufOwnerTask2 = _WfKernelBufOwnerTask2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 15),
    _WfKernelBufOwnerTask2_Type()
)
wfKernelBufOwnerTask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask2.setStatus("mandatory")
_WfKernelBufOwnerTask2Bufs_Type = Integer32
_WfKernelBufOwnerTask2Bufs_Object = MibTableColumn
wfKernelBufOwnerTask2Bufs = _WfKernelBufOwnerTask2Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 16),
    _WfKernelBufOwnerTask2Bufs_Type()
)
wfKernelBufOwnerTask2Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask2Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask3_Type = DisplayString
_WfKernelBufOwnerTask3_Object = MibTableColumn
wfKernelBufOwnerTask3 = _WfKernelBufOwnerTask3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 17),
    _WfKernelBufOwnerTask3_Type()
)
wfKernelBufOwnerTask3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask3.setStatus("mandatory")
_WfKernelBufOwnerTask3Bufs_Type = Integer32
_WfKernelBufOwnerTask3Bufs_Object = MibTableColumn
wfKernelBufOwnerTask3Bufs = _WfKernelBufOwnerTask3Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 18),
    _WfKernelBufOwnerTask3Bufs_Type()
)
wfKernelBufOwnerTask3Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask3Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask4_Type = DisplayString
_WfKernelBufOwnerTask4_Object = MibTableColumn
wfKernelBufOwnerTask4 = _WfKernelBufOwnerTask4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 19),
    _WfKernelBufOwnerTask4_Type()
)
wfKernelBufOwnerTask4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask4.setStatus("mandatory")
_WfKernelBufOwnerTask4Bufs_Type = Integer32
_WfKernelBufOwnerTask4Bufs_Object = MibTableColumn
wfKernelBufOwnerTask4Bufs = _WfKernelBufOwnerTask4Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 20),
    _WfKernelBufOwnerTask4Bufs_Type()
)
wfKernelBufOwnerTask4Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask4Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask5_Type = DisplayString
_WfKernelBufOwnerTask5_Object = MibTableColumn
wfKernelBufOwnerTask5 = _WfKernelBufOwnerTask5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 21),
    _WfKernelBufOwnerTask5_Type()
)
wfKernelBufOwnerTask5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask5.setStatus("mandatory")
_WfKernelBufOwnerTask5Bufs_Type = Integer32
_WfKernelBufOwnerTask5Bufs_Object = MibTableColumn
wfKernelBufOwnerTask5Bufs = _WfKernelBufOwnerTask5Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 22),
    _WfKernelBufOwnerTask5Bufs_Type()
)
wfKernelBufOwnerTask5Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask5Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask6_Type = DisplayString
_WfKernelBufOwnerTask6_Object = MibTableColumn
wfKernelBufOwnerTask6 = _WfKernelBufOwnerTask6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 23),
    _WfKernelBufOwnerTask6_Type()
)
wfKernelBufOwnerTask6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask6.setStatus("mandatory")
_WfKernelBufOwnerTask6Bufs_Type = Integer32
_WfKernelBufOwnerTask6Bufs_Object = MibTableColumn
wfKernelBufOwnerTask6Bufs = _WfKernelBufOwnerTask6Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 24),
    _WfKernelBufOwnerTask6Bufs_Type()
)
wfKernelBufOwnerTask6Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask6Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask7_Type = DisplayString
_WfKernelBufOwnerTask7_Object = MibTableColumn
wfKernelBufOwnerTask7 = _WfKernelBufOwnerTask7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 25),
    _WfKernelBufOwnerTask7_Type()
)
wfKernelBufOwnerTask7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask7.setStatus("mandatory")
_WfKernelBufOwnerTask7Bufs_Type = Integer32
_WfKernelBufOwnerTask7Bufs_Object = MibTableColumn
wfKernelBufOwnerTask7Bufs = _WfKernelBufOwnerTask7Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 26),
    _WfKernelBufOwnerTask7Bufs_Type()
)
wfKernelBufOwnerTask7Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask7Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask8_Type = DisplayString
_WfKernelBufOwnerTask8_Object = MibTableColumn
wfKernelBufOwnerTask8 = _WfKernelBufOwnerTask8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 27),
    _WfKernelBufOwnerTask8_Type()
)
wfKernelBufOwnerTask8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask8.setStatus("mandatory")
_WfKernelBufOwnerTask8Bufs_Type = Integer32
_WfKernelBufOwnerTask8Bufs_Object = MibTableColumn
wfKernelBufOwnerTask8Bufs = _WfKernelBufOwnerTask8Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 28),
    _WfKernelBufOwnerTask8Bufs_Type()
)
wfKernelBufOwnerTask8Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask8Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask9_Type = DisplayString
_WfKernelBufOwnerTask9_Object = MibTableColumn
wfKernelBufOwnerTask9 = _WfKernelBufOwnerTask9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 29),
    _WfKernelBufOwnerTask9_Type()
)
wfKernelBufOwnerTask9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask9.setStatus("mandatory")
_WfKernelBufOwnerTask9Bufs_Type = Integer32
_WfKernelBufOwnerTask9Bufs_Object = MibTableColumn
wfKernelBufOwnerTask9Bufs = _WfKernelBufOwnerTask9Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 30),
    _WfKernelBufOwnerTask9Bufs_Type()
)
wfKernelBufOwnerTask9Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask9Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask10_Type = DisplayString
_WfKernelBufOwnerTask10_Object = MibTableColumn
wfKernelBufOwnerTask10 = _WfKernelBufOwnerTask10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 31),
    _WfKernelBufOwnerTask10_Type()
)
wfKernelBufOwnerTask10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask10.setStatus("mandatory")
_WfKernelBufOwnerTask10Bufs_Type = Integer32
_WfKernelBufOwnerTask10Bufs_Object = MibTableColumn
wfKernelBufOwnerTask10Bufs = _WfKernelBufOwnerTask10Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 32),
    _WfKernelBufOwnerTask10Bufs_Type()
)
wfKernelBufOwnerTask10Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask10Bufs.setStatus("mandatory")
_WfKernelMemOwnerTask1_Type = DisplayString
_WfKernelMemOwnerTask1_Object = MibTableColumn
wfKernelMemOwnerTask1 = _WfKernelMemOwnerTask1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 33),
    _WfKernelMemOwnerTask1_Type()
)
wfKernelMemOwnerTask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask1.setStatus("mandatory")
_WfKernelMemOwnerTask1Size_Type = Integer32
_WfKernelMemOwnerTask1Size_Object = MibTableColumn
wfKernelMemOwnerTask1Size = _WfKernelMemOwnerTask1Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 34),
    _WfKernelMemOwnerTask1Size_Type()
)
wfKernelMemOwnerTask1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask1Size.setStatus("mandatory")
_WfKernelMemOwnerTask2_Type = DisplayString
_WfKernelMemOwnerTask2_Object = MibTableColumn
wfKernelMemOwnerTask2 = _WfKernelMemOwnerTask2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 35),
    _WfKernelMemOwnerTask2_Type()
)
wfKernelMemOwnerTask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask2.setStatus("mandatory")
_WfKernelMemOwnerTask2Size_Type = Integer32
_WfKernelMemOwnerTask2Size_Object = MibTableColumn
wfKernelMemOwnerTask2Size = _WfKernelMemOwnerTask2Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 36),
    _WfKernelMemOwnerTask2Size_Type()
)
wfKernelMemOwnerTask2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask2Size.setStatus("mandatory")
_WfKernelMemOwnerTask3_Type = DisplayString
_WfKernelMemOwnerTask3_Object = MibTableColumn
wfKernelMemOwnerTask3 = _WfKernelMemOwnerTask3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 37),
    _WfKernelMemOwnerTask3_Type()
)
wfKernelMemOwnerTask3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask3.setStatus("mandatory")
_WfKernelMemOwnerTask3Size_Type = Integer32
_WfKernelMemOwnerTask3Size_Object = MibTableColumn
wfKernelMemOwnerTask3Size = _WfKernelMemOwnerTask3Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 38),
    _WfKernelMemOwnerTask3Size_Type()
)
wfKernelMemOwnerTask3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask3Size.setStatus("mandatory")
_WfKernelMemOwnerTask4_Type = DisplayString
_WfKernelMemOwnerTask4_Object = MibTableColumn
wfKernelMemOwnerTask4 = _WfKernelMemOwnerTask4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 39),
    _WfKernelMemOwnerTask4_Type()
)
wfKernelMemOwnerTask4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask4.setStatus("mandatory")
_WfKernelMemOwnerTask4Size_Type = Integer32
_WfKernelMemOwnerTask4Size_Object = MibTableColumn
wfKernelMemOwnerTask4Size = _WfKernelMemOwnerTask4Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 40),
    _WfKernelMemOwnerTask4Size_Type()
)
wfKernelMemOwnerTask4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask4Size.setStatus("mandatory")
_WfKernelMemOwnerTask5_Type = DisplayString
_WfKernelMemOwnerTask5_Object = MibTableColumn
wfKernelMemOwnerTask5 = _WfKernelMemOwnerTask5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 41),
    _WfKernelMemOwnerTask5_Type()
)
wfKernelMemOwnerTask5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask5.setStatus("mandatory")
_WfKernelMemOwnerTask5Size_Type = Integer32
_WfKernelMemOwnerTask5Size_Object = MibTableColumn
wfKernelMemOwnerTask5Size = _WfKernelMemOwnerTask5Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 42),
    _WfKernelMemOwnerTask5Size_Type()
)
wfKernelMemOwnerTask5Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask5Size.setStatus("mandatory")
_WfKernelMemOwnerTask6_Type = DisplayString
_WfKernelMemOwnerTask6_Object = MibTableColumn
wfKernelMemOwnerTask6 = _WfKernelMemOwnerTask6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 43),
    _WfKernelMemOwnerTask6_Type()
)
wfKernelMemOwnerTask6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask6.setStatus("mandatory")
_WfKernelMemOwnerTask6Size_Type = Integer32
_WfKernelMemOwnerTask6Size_Object = MibTableColumn
wfKernelMemOwnerTask6Size = _WfKernelMemOwnerTask6Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 44),
    _WfKernelMemOwnerTask6Size_Type()
)
wfKernelMemOwnerTask6Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask6Size.setStatus("mandatory")
_WfKernelMemOwnerTask7_Type = DisplayString
_WfKernelMemOwnerTask7_Object = MibTableColumn
wfKernelMemOwnerTask7 = _WfKernelMemOwnerTask7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 45),
    _WfKernelMemOwnerTask7_Type()
)
wfKernelMemOwnerTask7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask7.setStatus("mandatory")
_WfKernelMemOwnerTask7Size_Type = Integer32
_WfKernelMemOwnerTask7Size_Object = MibTableColumn
wfKernelMemOwnerTask7Size = _WfKernelMemOwnerTask7Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 46),
    _WfKernelMemOwnerTask7Size_Type()
)
wfKernelMemOwnerTask7Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask7Size.setStatus("mandatory")
_WfKernelMemOwnerTask8_Type = DisplayString
_WfKernelMemOwnerTask8_Object = MibTableColumn
wfKernelMemOwnerTask8 = _WfKernelMemOwnerTask8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 47),
    _WfKernelMemOwnerTask8_Type()
)
wfKernelMemOwnerTask8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask8.setStatus("mandatory")
_WfKernelMemOwnerTask8Size_Type = Integer32
_WfKernelMemOwnerTask8Size_Object = MibTableColumn
wfKernelMemOwnerTask8Size = _WfKernelMemOwnerTask8Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 48),
    _WfKernelMemOwnerTask8Size_Type()
)
wfKernelMemOwnerTask8Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask8Size.setStatus("mandatory")
_WfKernelMemOwnerTask9_Type = DisplayString
_WfKernelMemOwnerTask9_Object = MibTableColumn
wfKernelMemOwnerTask9 = _WfKernelMemOwnerTask9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 49),
    _WfKernelMemOwnerTask9_Type()
)
wfKernelMemOwnerTask9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask9.setStatus("mandatory")
_WfKernelMemOwnerTask9Size_Type = Integer32
_WfKernelMemOwnerTask9Size_Object = MibTableColumn
wfKernelMemOwnerTask9Size = _WfKernelMemOwnerTask9Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 50),
    _WfKernelMemOwnerTask9Size_Type()
)
wfKernelMemOwnerTask9Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask9Size.setStatus("mandatory")
_WfKernelMemOwnerTask10_Type = DisplayString
_WfKernelMemOwnerTask10_Object = MibTableColumn
wfKernelMemOwnerTask10 = _WfKernelMemOwnerTask10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 51),
    _WfKernelMemOwnerTask10_Type()
)
wfKernelMemOwnerTask10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask10.setStatus("mandatory")
_WfKernelMemOwnerTask10Size_Type = Integer32
_WfKernelMemOwnerTask10Size_Object = MibTableColumn
wfKernelMemOwnerTask10Size = _WfKernelMemOwnerTask10Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 52),
    _WfKernelMemOwnerTask10Size_Type()
)
wfKernelMemOwnerTask10Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask10Size.setStatus("mandatory")
_WfLine_ObjectIdentity = ObjectIdentity
wfLine = _WfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4)
)
_WfCSMACDTable_Object = MibTable
wfCSMACDTable = _WfCSMACDTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1)
)
if mibBuilder.loadTexts:
    wfCSMACDTable.setStatus("mandatory")
_WfCSMACDEntry_Object = MibTableRow
wfCSMACDEntry = _WfCSMACDEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1)
)
wfCSMACDEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfCSMACDSlot"),
    (0, "Wellfleet-Series7-MIB", "wfCSMACDConnector"),
)
if mibBuilder.loadTexts:
    wfCSMACDEntry.setStatus("mandatory")


class _WfCSMACDDelete_Type(Integer32):
    """Custom type wfCSMACDDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfCSMACDDelete_Type.__name__ = "Integer32"
_WfCSMACDDelete_Object = MibTableColumn
wfCSMACDDelete = _WfCSMACDDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 1),
    _WfCSMACDDelete_Type()
)
wfCSMACDDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDDelete.setStatus("mandatory")


class _WfCSMACDEnable_Type(Integer32):
    """Custom type wfCSMACDEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfCSMACDEnable_Type.__name__ = "Integer32"
_WfCSMACDEnable_Object = MibTableColumn
wfCSMACDEnable = _WfCSMACDEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 2),
    _WfCSMACDEnable_Type()
)
wfCSMACDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDEnable.setStatus("mandatory")


class _WfCSMACDState_Type(Integer32):
    """Custom type wfCSMACDState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfCSMACDState_Type.__name__ = "Integer32"
_WfCSMACDState_Object = MibTableColumn
wfCSMACDState = _WfCSMACDState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 3),
    _WfCSMACDState_Type()
)
wfCSMACDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDState.setStatus("mandatory")


class _WfCSMACDSlot_Type(Integer32):
    """Custom type wfCSMACDSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfCSMACDSlot_Type.__name__ = "Integer32"
_WfCSMACDSlot_Object = MibTableColumn
wfCSMACDSlot = _WfCSMACDSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 4),
    _WfCSMACDSlot_Type()
)
wfCSMACDSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDSlot.setStatus("mandatory")


class _WfCSMACDConnector_Type(Integer32):
    """Custom type wfCSMACDConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfCSMACDConnector_Type.__name__ = "Integer32"
_WfCSMACDConnector_Object = MibTableColumn
wfCSMACDConnector = _WfCSMACDConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 5),
    _WfCSMACDConnector_Type()
)
wfCSMACDConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDConnector.setStatus("mandatory")


class _WfCSMACDCct_Type(Integer32):
    """Custom type wfCSMACDCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfCSMACDCct_Type.__name__ = "Integer32"
_WfCSMACDCct_Object = MibTableColumn
wfCSMACDCct = _WfCSMACDCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 6),
    _WfCSMACDCct_Type()
)
wfCSMACDCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDCct.setStatus("mandatory")


class _WfCSMACDBofl_Type(Integer32):
    """Custom type wfCSMACDBofl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfCSMACDBofl_Type.__name__ = "Integer32"
_WfCSMACDBofl_Object = MibTableColumn
wfCSMACDBofl = _WfCSMACDBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 7),
    _WfCSMACDBofl_Type()
)
wfCSMACDBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDBofl.setStatus("mandatory")


class _WfCSMACDBoflTmo_Type(Integer32):
    """Custom type wfCSMACDBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              60)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("maximum", 60),
          ("minimum", 1))
    )


_WfCSMACDBoflTmo_Type.__name__ = "Integer32"
_WfCSMACDBoflTmo_Object = MibTableColumn
wfCSMACDBoflTmo = _WfCSMACDBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 8),
    _WfCSMACDBoflTmo_Type()
)
wfCSMACDBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDBoflTmo.setStatus("mandatory")


class _WfCSMACDMtu_Type(Integer32):
    """Custom type wfCSMACDMtu based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1518
        )
    )
    namedValues = NamedValues(
        ("default", 1518)
    )


_WfCSMACDMtu_Type.__name__ = "Integer32"
_WfCSMACDMtu_Object = MibTableColumn
wfCSMACDMtu = _WfCSMACDMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 9),
    _WfCSMACDMtu_Type()
)
wfCSMACDMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMtu.setStatus("mandatory")
_WfCSMACDMadr_Type = OctetString
_WfCSMACDMadr_Object = MibTableColumn
wfCSMACDMadr = _WfCSMACDMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 10),
    _WfCSMACDMadr_Type()
)
wfCSMACDMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMadr.setStatus("mandatory")
_WfCSMACDOctetsRxOk_Type = Counter32
_WfCSMACDOctetsRxOk_Object = MibTableColumn
wfCSMACDOctetsRxOk = _WfCSMACDOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 11),
    _WfCSMACDOctetsRxOk_Type()
)
wfCSMACDOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOctetsRxOk.setStatus("mandatory")
_WfCSMACDFramesRxOk_Type = Counter32
_WfCSMACDFramesRxOk_Object = MibTableColumn
wfCSMACDFramesRxOk = _WfCSMACDFramesRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 12),
    _WfCSMACDFramesRxOk_Type()
)
wfCSMACDFramesRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDFramesRxOk.setStatus("mandatory")
_WfCSMACDOctetsTxOk_Type = Counter32
_WfCSMACDOctetsTxOk_Object = MibTableColumn
wfCSMACDOctetsTxOk = _WfCSMACDOctetsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 13),
    _WfCSMACDOctetsTxOk_Type()
)
wfCSMACDOctetsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOctetsTxOk.setStatus("mandatory")
_WfCSMACDFramesTxOk_Type = Counter32
_WfCSMACDFramesTxOk_Object = MibTableColumn
wfCSMACDFramesTxOk = _WfCSMACDFramesTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 14),
    _WfCSMACDFramesTxOk_Type()
)
wfCSMACDFramesTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDFramesTxOk.setStatus("mandatory")
_WfCSMACDDeferredTx_Type = Counter32
_WfCSMACDDeferredTx_Object = MibTableColumn
wfCSMACDDeferredTx = _WfCSMACDDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 15),
    _WfCSMACDDeferredTx_Type()
)
wfCSMACDDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDDeferredTx.setStatus("mandatory")
_WfCSMACDLateCollnTx_Type = Counter32
_WfCSMACDLateCollnTx_Object = MibTableColumn
wfCSMACDLateCollnTx = _WfCSMACDLateCollnTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 16),
    _WfCSMACDLateCollnTx_Type()
)
wfCSMACDLateCollnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLateCollnTx.setStatus("mandatory")
_WfCSMACDExcessvCollnTx_Type = Counter32
_WfCSMACDExcessvCollnTx_Object = MibTableColumn
wfCSMACDExcessvCollnTx = _WfCSMACDExcessvCollnTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 17),
    _WfCSMACDExcessvCollnTx_Type()
)
wfCSMACDExcessvCollnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDExcessvCollnTx.setStatus("mandatory")
_WfCSMACDBablErrorTx_Type = Counter32
_WfCSMACDBablErrorTx_Object = MibTableColumn
wfCSMACDBablErrorTx = _WfCSMACDBablErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 18),
    _WfCSMACDBablErrorTx_Type()
)
wfCSMACDBablErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDBablErrorTx.setStatus("mandatory")
_WfCSMACDBufErrorTx_Type = Counter32
_WfCSMACDBufErrorTx_Object = MibTableColumn
wfCSMACDBufErrorTx = _WfCSMACDBufErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 19),
    _WfCSMACDBufErrorTx_Type()
)
wfCSMACDBufErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDBufErrorTx.setStatus("mandatory")
_WfCSMACDLcarTx_Type = Counter32
_WfCSMACDLcarTx_Object = MibTableColumn
wfCSMACDLcarTx = _WfCSMACDLcarTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 20),
    _WfCSMACDLcarTx_Type()
)
wfCSMACDLcarTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLcarTx.setStatus("mandatory")
_WfCSMACDUfloTx_Type = Counter32
_WfCSMACDUfloTx_Object = MibTableColumn
wfCSMACDUfloTx = _WfCSMACDUfloTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 21),
    _WfCSMACDUfloTx_Type()
)
wfCSMACDUfloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDUfloTx.setStatus("mandatory")
_WfCSMACDFcsErrorRx_Type = Counter32
_WfCSMACDFcsErrorRx_Object = MibTableColumn
wfCSMACDFcsErrorRx = _WfCSMACDFcsErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 22),
    _WfCSMACDFcsErrorRx_Type()
)
wfCSMACDFcsErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDFcsErrorRx.setStatus("mandatory")
_WfCSMACDAlignErrorRx_Type = Counter32
_WfCSMACDAlignErrorRx_Object = MibTableColumn
wfCSMACDAlignErrorRx = _WfCSMACDAlignErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 23),
    _WfCSMACDAlignErrorRx_Type()
)
wfCSMACDAlignErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAlignErrorRx.setStatus("mandatory")
_WfCSMACDLackRescErrorRx_Type = Counter32
_WfCSMACDLackRescErrorRx_Object = MibTableColumn
wfCSMACDLackRescErrorRx = _WfCSMACDLackRescErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 24),
    _WfCSMACDLackRescErrorRx_Type()
)
wfCSMACDLackRescErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLackRescErrorRx.setStatus("mandatory")
_WfCSMACDTooLongErrorRx_Type = Counter32
_WfCSMACDTooLongErrorRx_Object = MibTableColumn
wfCSMACDTooLongErrorRx = _WfCSMACDTooLongErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 25),
    _WfCSMACDTooLongErrorRx_Type()
)
wfCSMACDTooLongErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTooLongErrorRx.setStatus("mandatory")
_WfCSMACDOfloRx_Type = Counter32
_WfCSMACDOfloRx_Object = MibTableColumn
wfCSMACDOfloRx = _WfCSMACDOfloRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 26),
    _WfCSMACDOfloRx_Type()
)
wfCSMACDOfloRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOfloRx.setStatus("mandatory")
_WfCSMACDMerr_Type = Counter32
_WfCSMACDMerr_Object = MibTableColumn
wfCSMACDMerr = _WfCSMACDMerr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 27),
    _WfCSMACDMerr_Type()
)
wfCSMACDMerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMerr.setStatus("mandatory")
_WfCSMACDCerr_Type = Counter32
_WfCSMACDCerr_Object = MibTableColumn
wfCSMACDCerr = _WfCSMACDCerr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 28),
    _WfCSMACDCerr_Type()
)
wfCSMACDCerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDCerr.setStatus("mandatory")


class _WfCSMACDHardwareFilter_Type(Integer32):
    """Custom type wfCSMACDHardwareFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfCSMACDHardwareFilter_Type.__name__ = "Integer32"
_WfCSMACDHardwareFilter_Object = MibTableColumn
wfCSMACDHardwareFilter = _WfCSMACDHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 29),
    _WfCSMACDHardwareFilter_Type()
)
wfCSMACDHardwareFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDHardwareFilter.setStatus("mandatory")


class _WfCSMACDTxQueueLength_Type(Integer32):
    """Custom type wfCSMACDTxQueueLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 32),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfCSMACDTxQueueLength_Type.__name__ = "Integer32"
_WfCSMACDTxQueueLength_Object = MibTableColumn
wfCSMACDTxQueueLength = _WfCSMACDTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 30),
    _WfCSMACDTxQueueLength_Type()
)
wfCSMACDTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDTxQueueLength.setStatus("mandatory")


class _WfCSMACDRxQueueLength_Type(Integer32):
    """Custom type wfCSMACDRxQueueLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 32),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfCSMACDRxQueueLength_Type.__name__ = "Integer32"
_WfCSMACDRxQueueLength_Object = MibTableColumn
wfCSMACDRxQueueLength = _WfCSMACDRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 31),
    _WfCSMACDRxQueueLength_Type()
)
wfCSMACDRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDRxQueueLength.setStatus("mandatory")
_WfCSMACDTxClipFrames_Type = Counter32
_WfCSMACDTxClipFrames_Object = MibTableColumn
wfCSMACDTxClipFrames = _WfCSMACDTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 32),
    _WfCSMACDTxClipFrames_Type()
)
wfCSMACDTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxClipFrames.setStatus("mandatory")
_WfCSMACDRxReplenMisses_Type = Counter32
_WfCSMACDRxReplenMisses_Object = MibTableColumn
wfCSMACDRxReplenMisses = _WfCSMACDRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 33),
    _WfCSMACDRxReplenMisses_Type()
)
wfCSMACDRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxReplenMisses.setStatus("mandatory")
_WfTokenRingTable_Object = MibTable
wfTokenRingTable = _WfTokenRingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2)
)
if mibBuilder.loadTexts:
    wfTokenRingTable.setStatus("mandatory")
_WfTokenRingEntry_Object = MibTableRow
wfTokenRingEntry = _WfTokenRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1)
)
wfTokenRingEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfTokenRingSlot"),
    (0, "Wellfleet-Series7-MIB", "wfTokenRingConnector"),
)
if mibBuilder.loadTexts:
    wfTokenRingEntry.setStatus("mandatory")


class _WfTokenRingDelete_Type(Integer32):
    """Custom type wfTokenRingDelete based on Integer32"""
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


_WfTokenRingDelete_Type.__name__ = "Integer32"
_WfTokenRingDelete_Object = MibTableColumn
wfTokenRingDelete = _WfTokenRingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 1),
    _WfTokenRingDelete_Type()
)
wfTokenRingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingDelete.setStatus("mandatory")


class _WfTokenRingDisable_Type(Integer32):
    """Custom type wfTokenRingDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfTokenRingDisable_Type.__name__ = "Integer32"
_WfTokenRingDisable_Object = MibTableColumn
wfTokenRingDisable = _WfTokenRingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 2),
    _WfTokenRingDisable_Type()
)
wfTokenRingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingDisable.setStatus("mandatory")


class _WfTokenRingState_Type(Integer32):
    """Custom type wfTokenRingState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfTokenRingState_Type.__name__ = "Integer32"
_WfTokenRingState_Object = MibTableColumn
wfTokenRingState = _WfTokenRingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 3),
    _WfTokenRingState_Type()
)
wfTokenRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingState.setStatus("mandatory")


class _WfTokenRingSlot_Type(Integer32):
    """Custom type wfTokenRingSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfTokenRingSlot_Type.__name__ = "Integer32"
_WfTokenRingSlot_Object = MibTableColumn
wfTokenRingSlot = _WfTokenRingSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 4),
    _WfTokenRingSlot_Type()
)
wfTokenRingSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSlot.setStatus("mandatory")


class _WfTokenRingConnector_Type(Integer32):
    """Custom type wfTokenRingConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfTokenRingConnector_Type.__name__ = "Integer32"
_WfTokenRingConnector_Object = MibTableColumn
wfTokenRingConnector = _WfTokenRingConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 5),
    _WfTokenRingConnector_Type()
)
wfTokenRingConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingConnector.setStatus("mandatory")


class _WfTokenRingCct_Type(Integer32):
    """Custom type wfTokenRingCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfTokenRingCct_Type.__name__ = "Integer32"
_WfTokenRingCct_Object = MibTableColumn
wfTokenRingCct = _WfTokenRingCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 6),
    _WfTokenRingCct_Type()
)
wfTokenRingCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCct.setStatus("mandatory")


class _WfTokenRingMtu_Type(Integer32):
    """Custom type wfTokenRingMtu based on Integer32"""
    defaultValue = 4568

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4568
        )
    )
    namedValues = NamedValues(
        ("default", 4568)
    )


_WfTokenRingMtu_Type.__name__ = "Integer32"
_WfTokenRingMtu_Object = MibTableColumn
wfTokenRingMtu = _WfTokenRingMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 7),
    _WfTokenRingMtu_Type()
)
wfTokenRingMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMtu.setStatus("mandatory")
_WfTokenRingMadr_Type = OctetString
_WfTokenRingMadr_Object = MibTableColumn
wfTokenRingMadr = _WfTokenRingMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 8),
    _WfTokenRingMadr_Type()
)
wfTokenRingMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMadr.setStatus("mandatory")
_WfTokenRingCfgMadr_Type = OctetString
_WfTokenRingCfgMadr_Object = MibTableColumn
wfTokenRingCfgMadr = _WfTokenRingCfgMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 9),
    _WfTokenRingCfgMadr_Type()
)
wfTokenRingCfgMadr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCfgMadr.setStatus("mandatory")


class _WfTokenRingMadrSelect_Type(Integer32):
    """Custom type wfTokenRingMadrSelect based on Integer32"""
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
        *(("boxwide", 1),
          ("cnfg", 3),
          ("prom", 2))
    )


_WfTokenRingMadrSelect_Type.__name__ = "Integer32"
_WfTokenRingMadrSelect_Object = MibTableColumn
wfTokenRingMadrSelect = _WfTokenRingMadrSelect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 10),
    _WfTokenRingMadrSelect_Type()
)
wfTokenRingMadrSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingMadrSelect.setStatus("mandatory")


class _WfTokenRingSpeed_Type(Integer32):
    """Custom type wfTokenRingSpeed based on Integer32"""
    defaultValue = 16777216

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4194304,
              16777216)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 16777216),
          ("mbps4", 4194304))
    )


_WfTokenRingSpeed_Type.__name__ = "Integer32"
_WfTokenRingSpeed_Object = MibTableColumn
wfTokenRingSpeed = _WfTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 11),
    _WfTokenRingSpeed_Type()
)
wfTokenRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingSpeed.setStatus("mandatory")


class _WfTokenRingEarlyTokenRelease_Type(Integer32):
    """Custom type wfTokenRingEarlyTokenRelease based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfTokenRingEarlyTokenRelease_Type.__name__ = "Integer32"
_WfTokenRingEarlyTokenRelease_Object = MibTableColumn
wfTokenRingEarlyTokenRelease = _WfTokenRingEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 12),
    _WfTokenRingEarlyTokenRelease_Type()
)
wfTokenRingEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingEarlyTokenRelease.setStatus("mandatory")
_WfTokenRingStatus_Type = Integer32
_WfTokenRingStatus_Object = MibTableColumn
wfTokenRingStatus = _WfTokenRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 13),
    _WfTokenRingStatus_Type()
)
wfTokenRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingStatus.setStatus("mandatory")


class _WfTokenRingOpenState_Type(Integer32):
    """Custom type wfTokenRingOpenState based on Integer32"""
    defaultValue = 6

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
        *(("closed", 6),
          ("closing", 3),
          ("opened", 1),
          ("openfailure", 4),
          ("opening", 2),
          ("ringfailure", 5))
    )


_WfTokenRingOpenState_Type.__name__ = "Integer32"
_WfTokenRingOpenState_Object = MibTableColumn
wfTokenRingOpenState = _WfTokenRingOpenState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 14),
    _WfTokenRingOpenState_Type()
)
wfTokenRingOpenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOpenState.setStatus("mandatory")


class _WfTokenRingOpenStatus_Type(Integer32):
    """Custom type wfTokenRingOpenStatus based on Integer32"""
    defaultValue = 12

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
        *(("badparam", 2),
          ("beaconing", 7),
          ("duplicatemac", 8),
          ("insertiontimeout", 5),
          ("lobefailed", 3),
          ("noopen", 12),
          ("open", 1),
          ("removereceived", 10),
          ("requestfailed", 9),
          ("ringfailed", 6),
          ("signalloss", 4),
          ("unkerror", 11))
    )


_WfTokenRingOpenStatus_Type.__name__ = "Integer32"
_WfTokenRingOpenStatus_Object = MibTableColumn
wfTokenRingOpenStatus = _WfTokenRingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 15),
    _WfTokenRingOpenStatus_Type()
)
wfTokenRingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOpenStatus.setStatus("mandatory")
_WfTokenRingUpStream_Type = OctetString
_WfTokenRingUpStream_Object = MibTableColumn
wfTokenRingUpStream = _WfTokenRingUpStream_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 16),
    _WfTokenRingUpStream_Type()
)
wfTokenRingUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingUpStream.setStatus("mandatory")
_WfTokenRingRxOctets_Type = Counter32
_WfTokenRingRxOctets_Object = MibTableColumn
wfTokenRingRxOctets = _WfTokenRingRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 17),
    _WfTokenRingRxOctets_Type()
)
wfTokenRingRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxOctets.setStatus("mandatory")
_WfTokenRingRxFrames_Type = Counter32
_WfTokenRingRxFrames_Object = MibTableColumn
wfTokenRingRxFrames = _WfTokenRingRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 18),
    _WfTokenRingRxFrames_Type()
)
wfTokenRingRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxFrames.setStatus("mandatory")
_WfTokenRingTxOctets_Type = Counter32
_WfTokenRingTxOctets_Object = MibTableColumn
wfTokenRingTxOctets = _WfTokenRingTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 19),
    _WfTokenRingTxOctets_Type()
)
wfTokenRingTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxOctets.setStatus("mandatory")
_WfTokenRingTxFrames_Type = Counter32
_WfTokenRingTxFrames_Object = MibTableColumn
wfTokenRingTxFrames = _WfTokenRingTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 20),
    _WfTokenRingTxFrames_Type()
)
wfTokenRingTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxFrames.setStatus("mandatory")
_WfTokenRingInDiscards_Type = Counter32
_WfTokenRingInDiscards_Object = MibTableColumn
wfTokenRingInDiscards = _WfTokenRingInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 21),
    _WfTokenRingInDiscards_Type()
)
wfTokenRingInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingInDiscards.setStatus("mandatory")
_WfTokenRingInErrors_Type = Counter32
_WfTokenRingInErrors_Object = MibTableColumn
wfTokenRingInErrors = _WfTokenRingInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 22),
    _WfTokenRingInErrors_Type()
)
wfTokenRingInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingInErrors.setStatus("mandatory")
_WfTokenRingOutDiscards_Type = Counter32
_WfTokenRingOutDiscards_Object = MibTableColumn
wfTokenRingOutDiscards = _WfTokenRingOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 23),
    _WfTokenRingOutDiscards_Type()
)
wfTokenRingOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOutDiscards.setStatus("mandatory")
_WfTokenRingOutErrors_Type = Counter32
_WfTokenRingOutErrors_Object = MibTableColumn
wfTokenRingOutErrors = _WfTokenRingOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 24),
    _WfTokenRingOutErrors_Type()
)
wfTokenRingOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOutErrors.setStatus("mandatory")
_WfTokenRingTxClipFrames_Type = Counter32
_WfTokenRingTxClipFrames_Object = MibTableColumn
wfTokenRingTxClipFrames = _WfTokenRingTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 25),
    _WfTokenRingTxClipFrames_Type()
)
wfTokenRingTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxClipFrames.setStatus("mandatory")
_WfTokenRingRxReplenMisses_Type = Counter32
_WfTokenRingRxReplenMisses_Object = MibTableColumn
wfTokenRingRxReplenMisses = _WfTokenRingRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 26),
    _WfTokenRingRxReplenMisses_Type()
)
wfTokenRingRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxReplenMisses.setStatus("mandatory")
_WfTokenRingSignalLosses_Type = Counter32
_WfTokenRingSignalLosses_Object = MibTableColumn
wfTokenRingSignalLosses = _WfTokenRingSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 27),
    _WfTokenRingSignalLosses_Type()
)
wfTokenRingSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSignalLosses.setStatus("mandatory")
_WfTokenRingHardErrors_Type = Counter32
_WfTokenRingHardErrors_Object = MibTableColumn
wfTokenRingHardErrors = _WfTokenRingHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 28),
    _WfTokenRingHardErrors_Type()
)
wfTokenRingHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingHardErrors.setStatus("mandatory")
_WfTokenRingSoftErrors_Type = Counter32
_WfTokenRingSoftErrors_Object = MibTableColumn
wfTokenRingSoftErrors = _WfTokenRingSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 29),
    _WfTokenRingSoftErrors_Type()
)
wfTokenRingSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSoftErrors.setStatus("mandatory")
_WfTokenRingTransmitBeacons_Type = Counter32
_WfTokenRingTransmitBeacons_Object = MibTableColumn
wfTokenRingTransmitBeacons = _WfTokenRingTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 30),
    _WfTokenRingTransmitBeacons_Type()
)
wfTokenRingTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTransmitBeacons.setStatus("mandatory")
_WfTokenRingLobeWireFaults_Type = Counter32
_WfTokenRingLobeWireFaults_Object = MibTableColumn
wfTokenRingLobeWireFaults = _WfTokenRingLobeWireFaults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 31),
    _WfTokenRingLobeWireFaults_Type()
)
wfTokenRingLobeWireFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLobeWireFaults.setStatus("mandatory")
_WfTokenRingAutoRemovalErrors_Type = Counter32
_WfTokenRingAutoRemovalErrors_Object = MibTableColumn
wfTokenRingAutoRemovalErrors = _WfTokenRingAutoRemovalErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 32),
    _WfTokenRingAutoRemovalErrors_Type()
)
wfTokenRingAutoRemovalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingAutoRemovalErrors.setStatus("mandatory")
_WfTokenRingRequestRemoves_Type = Counter32
_WfTokenRingRequestRemoves_Object = MibTableColumn
wfTokenRingRequestRemoves = _WfTokenRingRequestRemoves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 33),
    _WfTokenRingRequestRemoves_Type()
)
wfTokenRingRequestRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRequestRemoves.setStatus("mandatory")
_WfTokenRingCounterOverflows_Type = Counter32
_WfTokenRingCounterOverflows_Object = MibTableColumn
wfTokenRingCounterOverflows = _WfTokenRingCounterOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 34),
    _WfTokenRingCounterOverflows_Type()
)
wfTokenRingCounterOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingCounterOverflows.setStatus("mandatory")
_WfTokenRingSingleStations_Type = Counter32
_WfTokenRingSingleStations_Object = MibTableColumn
wfTokenRingSingleStations = _WfTokenRingSingleStations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 35),
    _WfTokenRingSingleStations_Type()
)
wfTokenRingSingleStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSingleStations.setStatus("mandatory")
_WfTokenRingRingRecoveries_Type = Counter32
_WfTokenRingRingRecoveries_Object = MibTableColumn
wfTokenRingRingRecoveries = _WfTokenRingRingRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 36),
    _WfTokenRingRingRecoveries_Type()
)
wfTokenRingRingRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRingRecoveries.setStatus("mandatory")
_WfTokenRingAdapterChecks_Type = Counter32
_WfTokenRingAdapterChecks_Object = MibTableColumn
wfTokenRingAdapterChecks = _WfTokenRingAdapterChecks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 37),
    _WfTokenRingAdapterChecks_Type()
)
wfTokenRingAdapterChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingAdapterChecks.setStatus("mandatory")
_WfTokenRingFirstAdapterCheckCode_Type = Integer32
_WfTokenRingFirstAdapterCheckCode_Object = MibTableColumn
wfTokenRingFirstAdapterCheckCode = _WfTokenRingFirstAdapterCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 38),
    _WfTokenRingFirstAdapterCheckCode_Type()
)
wfTokenRingFirstAdapterCheckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingFirstAdapterCheckCode.setStatus("mandatory")
_WfTokenRingLastAdapterCheckCode_Type = Integer32
_WfTokenRingLastAdapterCheckCode_Object = MibTableColumn
wfTokenRingLastAdapterCheckCode = _WfTokenRingLastAdapterCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 39),
    _WfTokenRingLastAdapterCheckCode_Type()
)
wfTokenRingLastAdapterCheckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLastAdapterCheckCode.setStatus("mandatory")
_WfTokenRingLineErrors_Type = Counter32
_WfTokenRingLineErrors_Object = MibTableColumn
wfTokenRingLineErrors = _WfTokenRingLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 40),
    _WfTokenRingLineErrors_Type()
)
wfTokenRingLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLineErrors.setStatus("mandatory")
_WfTokenRingBurstErrors_Type = Counter32
_WfTokenRingBurstErrors_Object = MibTableColumn
wfTokenRingBurstErrors = _WfTokenRingBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 41),
    _WfTokenRingBurstErrors_Type()
)
wfTokenRingBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingBurstErrors.setStatus("mandatory")
_WfTokenRingAriFciErrors_Type = Counter32
_WfTokenRingAriFciErrors_Object = MibTableColumn
wfTokenRingAriFciErrors = _WfTokenRingAriFciErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 42),
    _WfTokenRingAriFciErrors_Type()
)
wfTokenRingAriFciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingAriFciErrors.setStatus("mandatory")
_WfTokenRingLostFrameErrors_Type = Counter32
_WfTokenRingLostFrameErrors_Object = MibTableColumn
wfTokenRingLostFrameErrors = _WfTokenRingLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 43),
    _WfTokenRingLostFrameErrors_Type()
)
wfTokenRingLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLostFrameErrors.setStatus("mandatory")
_WfTokenRingRxCongestionErrors_Type = Counter32
_WfTokenRingRxCongestionErrors_Object = MibTableColumn
wfTokenRingRxCongestionErrors = _WfTokenRingRxCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 44),
    _WfTokenRingRxCongestionErrors_Type()
)
wfTokenRingRxCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxCongestionErrors.setStatus("mandatory")
_WfTokenRingFrameCopiedErrors_Type = Counter32
_WfTokenRingFrameCopiedErrors_Object = MibTableColumn
wfTokenRingFrameCopiedErrors = _WfTokenRingFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 45),
    _WfTokenRingFrameCopiedErrors_Type()
)
wfTokenRingFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingFrameCopiedErrors.setStatus("mandatory")
_WfTokenRingTokenErrors_Type = Counter32
_WfTokenRingTokenErrors_Object = MibTableColumn
wfTokenRingTokenErrors = _WfTokenRingTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 46),
    _WfTokenRingTokenErrors_Type()
)
wfTokenRingTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTokenErrors.setStatus("mandatory")
_WfTokenRingDmaBusErrors_Type = Counter32
_WfTokenRingDmaBusErrors_Object = MibTableColumn
wfTokenRingDmaBusErrors = _WfTokenRingDmaBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 47),
    _WfTokenRingDmaBusErrors_Type()
)
wfTokenRingDmaBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingDmaBusErrors.setStatus("mandatory")
_WfTokenRingDmaParityErrors_Type = Counter32
_WfTokenRingDmaParityErrors_Object = MibTableColumn
wfTokenRingDmaParityErrors = _WfTokenRingDmaParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 48),
    _WfTokenRingDmaParityErrors_Type()
)
wfTokenRingDmaParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingDmaParityErrors.setStatus("mandatory")
_WfTokenRingSrbNotFreeCmdAborts_Type = Counter32
_WfTokenRingSrbNotFreeCmdAborts_Object = MibTableColumn
wfTokenRingSrbNotFreeCmdAborts = _WfTokenRingSrbNotFreeCmdAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 49),
    _WfTokenRingSrbNotFreeCmdAborts_Type()
)
wfTokenRingSrbNotFreeCmdAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSrbNotFreeCmdAborts.setStatus("mandatory")
_WfTokenRingRxProcessings_Type = Counter32
_WfTokenRingRxProcessings_Object = MibTableColumn
wfTokenRingRxProcessings = _WfTokenRingRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 50),
    _WfTokenRingRxProcessings_Type()
)
wfTokenRingRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxProcessings.setStatus("mandatory")
_WfTokenRingTxProcessings_Type = Counter32
_WfTokenRingTxProcessings_Object = MibTableColumn
wfTokenRingTxProcessings = _WfTokenRingTxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 51),
    _WfTokenRingTxProcessings_Type()
)
wfTokenRingTxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxProcessings.setStatus("mandatory")
_WfTokenRingTxCmplProcessings_Type = Counter32
_WfTokenRingTxCmplProcessings_Object = MibTableColumn
wfTokenRingTxCmplProcessings = _WfTokenRingTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 52),
    _WfTokenRingTxCmplProcessings_Type()
)
wfTokenRingTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxCmplProcessings.setStatus("mandatory")
_WfTokenRingRxTimeouts_Type = Counter32
_WfTokenRingRxTimeouts_Object = MibTableColumn
wfTokenRingRxTimeouts = _WfTokenRingRxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 53),
    _WfTokenRingRxTimeouts_Type()
)
wfTokenRingRxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxTimeouts.setStatus("mandatory")
_WfTokenRingCmdTimeouts_Type = Counter32
_WfTokenRingCmdTimeouts_Object = MibTableColumn
wfTokenRingCmdTimeouts = _WfTokenRingCmdTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 54),
    _WfTokenRingCmdTimeouts_Type()
)
wfTokenRingCmdTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingCmdTimeouts.setStatus("mandatory")
_WfTokenRingRxHostIntErrors_Type = Counter32
_WfTokenRingRxHostIntErrors_Object = MibTableColumn
wfTokenRingRxHostIntErrors = _WfTokenRingRxHostIntErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 55),
    _WfTokenRingRxHostIntErrors_Type()
)
wfTokenRingRxHostIntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxHostIntErrors.setStatus("mandatory")
_WfTokenRingRxTxBufferSize_Type = Integer32
_WfTokenRingRxTxBufferSize_Object = MibTableColumn
wfTokenRingRxTxBufferSize = _WfTokenRingRxTxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 56),
    _WfTokenRingRxTxBufferSize_Type()
)
wfTokenRingRxTxBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxTxBufferSize.setStatus("mandatory")
_WfFddiTable_Object = MibTable
wfFddiTable = _WfFddiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4)
)
if mibBuilder.loadTexts:
    wfFddiTable.setStatus("mandatory")
_WfFddiEntry_Object = MibTableRow
wfFddiEntry = _WfFddiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1)
)
wfFddiEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfFDDISlot"),
    (0, "Wellfleet-Series7-MIB", "wfFDDINode"),
)
if mibBuilder.loadTexts:
    wfFddiEntry.setStatus("mandatory")


class _WfFDDIDelete_Type(Integer32):
    """Custom type wfFDDIDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfFDDIDelete_Type.__name__ = "Integer32"
_WfFDDIDelete_Object = MibTableColumn
wfFDDIDelete = _WfFDDIDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 1),
    _WfFDDIDelete_Type()
)
wfFDDIDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIDelete.setStatus("mandatory")


class _WfFDDIEnable_Type(Integer32):
    """Custom type wfFDDIEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFDDIEnable_Type.__name__ = "Integer32"
_WfFDDIEnable_Object = MibTableColumn
wfFDDIEnable = _WfFDDIEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 2),
    _WfFDDIEnable_Type()
)
wfFDDIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIEnable.setStatus("mandatory")


class _WfFDDIState_Type(Integer32):
    """Custom type wfFDDIState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfFDDIState_Type.__name__ = "Integer32"
_WfFDDIState_Object = MibTableColumn
wfFDDIState = _WfFDDIState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 3),
    _WfFDDIState_Type()
)
wfFDDIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIState.setStatus("mandatory")


class _WfFDDISlot_Type(Integer32):
    """Custom type wfFDDISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfFDDISlot_Type.__name__ = "Integer32"
_WfFDDISlot_Object = MibTableColumn
wfFDDISlot = _WfFDDISlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 4),
    _WfFDDISlot_Type()
)
wfFDDISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISlot.setStatus("mandatory")


class _WfFDDINode_Type(Integer32):
    """Custom type wfFDDINode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfFDDINode_Type.__name__ = "Integer32"
_WfFDDINode_Object = MibTableColumn
wfFDDINode = _WfFDDINode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 5),
    _WfFDDINode_Type()
)
wfFDDINode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDINode.setStatus("mandatory")


class _WfFDDICct_Type(Integer32):
    """Custom type wfFDDICct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfFDDICct_Type.__name__ = "Integer32"
_WfFDDICct_Object = MibTableColumn
wfFDDICct = _WfFDDICct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 6),
    _WfFDDICct_Type()
)
wfFDDICct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDICct.setStatus("mandatory")


class _WfFDDIBofl_Type(Integer32):
    """Custom type wfFDDIBofl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFDDIBofl_Type.__name__ = "Integer32"
_WfFDDIBofl_Object = MibTableColumn
wfFDDIBofl = _WfFDDIBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 7),
    _WfFDDIBofl_Type()
)
wfFDDIBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIBofl.setStatus("mandatory")


class _WfFDDIBoflTmo_Type(Integer32):
    """Custom type wfFDDIBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              60)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("maximum", 60),
          ("minimum", 1))
    )


_WfFDDIBoflTmo_Type.__name__ = "Integer32"
_WfFDDIBoflTmo_Object = MibTableColumn
wfFDDIBoflTmo = _WfFDDIBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 8),
    _WfFDDIBoflTmo_Type()
)
wfFDDIBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIBoflTmo.setStatus("mandatory")


class _WfFDDIMtu_Type(Integer32):
    """Custom type wfFDDIMtu based on Integer32"""
    defaultValue = 4495

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4495
        )
    )
    namedValues = NamedValues(
        ("default", 4495)
    )


_WfFDDIMtu_Type.__name__ = "Integer32"
_WfFDDIMtu_Object = MibTableColumn
wfFDDIMtu = _WfFDDIMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 9),
    _WfFDDIMtu_Type()
)
wfFDDIMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMtu.setStatus("mandatory")
_WfFDDIMadr_Type = OctetString
_WfFDDIMadr_Object = MibTableColumn
wfFDDIMadr = _WfFDDIMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 10),
    _WfFDDIMadr_Type()
)
wfFDDIMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMadr.setStatus("mandatory")
_WfFDDIOctetsRxOk_Type = Counter32
_WfFDDIOctetsRxOk_Object = MibTableColumn
wfFDDIOctetsRxOk = _WfFDDIOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 11),
    _WfFDDIOctetsRxOk_Type()
)
wfFDDIOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOctetsRxOk.setStatus("mandatory")
_WfFDDIFramesRxOk_Type = Counter32
_WfFDDIFramesRxOk_Object = MibTableColumn
wfFDDIFramesRxOk = _WfFDDIFramesRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 12),
    _WfFDDIFramesRxOk_Type()
)
wfFDDIFramesRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIFramesRxOk.setStatus("mandatory")
_WfFDDIOctetsTxOk_Type = Counter32
_WfFDDIOctetsTxOk_Object = MibTableColumn
wfFDDIOctetsTxOk = _WfFDDIOctetsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 13),
    _WfFDDIOctetsTxOk_Type()
)
wfFDDIOctetsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOctetsTxOk.setStatus("mandatory")
_WfFDDIFramesTxOk_Type = Counter32
_WfFDDIFramesTxOk_Object = MibTableColumn
wfFDDIFramesTxOk = _WfFDDIFramesTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 14),
    _WfFDDIFramesTxOk_Type()
)
wfFDDIFramesTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIFramesTxOk.setStatus("mandatory")
_WfFDDICrcErrRx_Type = Counter32
_WfFDDICrcErrRx_Object = MibTableColumn
wfFDDICrcErrRx = _WfFDDICrcErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 15),
    _WfFDDICrcErrRx_Type()
)
wfFDDICrcErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDICrcErrRx.setStatus("mandatory")
_WfFDDIOverrunRx_Type = Counter32
_WfFDDIOverrunRx_Object = MibTableColumn
wfFDDIOverrunRx = _WfFDDIOverrunRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 16),
    _WfFDDIOverrunRx_Type()
)
wfFDDIOverrunRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOverrunRx.setStatus("mandatory")
_WfFDDIParityErrRx_Type = Counter32
_WfFDDIParityErrRx_Object = MibTableColumn
wfFDDIParityErrRx = _WfFDDIParityErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 17),
    _WfFDDIParityErrRx_Type()
)
wfFDDIParityErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIParityErrRx.setStatus("mandatory")
_WfFDDIMacErrRx_Type = Counter32
_WfFDDIMacErrRx_Object = MibTableColumn
wfFDDIMacErrRx = _WfFDDIMacErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 18),
    _WfFDDIMacErrRx_Type()
)
wfFDDIMacErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacErrRx.setStatus("mandatory")
_WfFDDIRingErrRx_Type = Counter32
_WfFDDIRingErrRx_Object = MibTableColumn
wfFDDIRingErrRx = _WfFDDIRingErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 19),
    _WfFDDIRingErrRx_Type()
)
wfFDDIRingErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRingErrRx.setStatus("mandatory")
_WfFDDISmtRingErrRx_Type = Counter32
_WfFDDISmtRingErrRx_Object = MibTableColumn
wfFDDISmtRingErrRx = _WfFDDISmtRingErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 20),
    _WfFDDISmtRingErrRx_Type()
)
wfFDDISmtRingErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISmtRingErrRx.setStatus("mandatory")
_WfFDDIRingOverrunRx_Type = Counter32
_WfFDDIRingOverrunRx_Object = MibTableColumn
wfFDDIRingOverrunRx = _WfFDDIRingOverrunRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 21),
    _WfFDDIRingOverrunRx_Type()
)
wfFDDIRingOverrunRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRingOverrunRx.setStatus("mandatory")
_WfFDDISmtRingOverrunRx_Type = Counter32
_WfFDDISmtRingOverrunRx_Object = MibTableColumn
wfFDDISmtRingOverrunRx = _WfFDDISmtRingOverrunRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 22),
    _WfFDDISmtRingOverrunRx_Type()
)
wfFDDISmtRingOverrunRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISmtRingOverrunRx.setStatus("mandatory")
_WfFDDIAbortTx_Type = Counter32
_WfFDDIAbortTx_Object = MibTableColumn
wfFDDIAbortTx = _WfFDDIAbortTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 23),
    _WfFDDIAbortTx_Type()
)
wfFDDIAbortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIAbortTx.setStatus("mandatory")
_WfFDDIUnderrunTx_Type = Counter32
_WfFDDIUnderrunTx_Object = MibTableColumn
wfFDDIUnderrunTx = _WfFDDIUnderrunTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 24),
    _WfFDDIUnderrunTx_Type()
)
wfFDDIUnderrunTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIUnderrunTx.setStatus("mandatory")
_WfFDDIParityErrTx_Type = Counter32
_WfFDDIParityErrTx_Object = MibTableColumn
wfFDDIParityErrTx = _WfFDDIParityErrTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 25),
    _WfFDDIParityErrTx_Type()
)
wfFDDIParityErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIParityErrTx.setStatus("mandatory")
_WfFDDIRingErrTx_Type = Counter32
_WfFDDIRingErrTx_Object = MibTableColumn
wfFDDIRingErrTx = _WfFDDIRingErrTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 26),
    _WfFDDIRingErrTx_Type()
)
wfFDDIRingErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRingErrTx.setStatus("mandatory")
_WfFDDIPortOpErr_Type = Counter32
_WfFDDIPortOpErr_Object = MibTableColumn
wfFDDIPortOpErr = _WfFDDIPortOpErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 27),
    _WfFDDIPortOpErr_Type()
)
wfFDDIPortOpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIPortOpErr.setStatus("mandatory")
_WfFDDIInternOpErr_Type = Counter32
_WfFDDIInternOpErr_Object = MibTableColumn
wfFDDIInternOpErr = _WfFDDIInternOpErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 28),
    _WfFDDIInternOpErr_Type()
)
wfFDDIInternOpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIInternOpErr.setStatus("mandatory")
_WfFDDIHostErr_Type = Counter32
_WfFDDIHostErr_Object = MibTableColumn
wfFDDIHostErr = _WfFDDIHostErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 29),
    _WfFDDIHostErr_Type()
)
wfFDDIHostErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIHostErr.setStatus("mandatory")


class _WfFDDISmtConnectionPolicy_Type(Integer32):
    """Custom type wfFDDISmtConnectionPolicy based on Integer32"""
    defaultValue = 65381

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65381
        )
    )
    namedValues = NamedValues(
        ("default", 65381)
    )


_WfFDDISmtConnectionPolicy_Type.__name__ = "Integer32"
_WfFDDISmtConnectionPolicy_Object = MibTableColumn
wfFDDISmtConnectionPolicy = _WfFDDISmtConnectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 30),
    _WfFDDISmtConnectionPolicy_Type()
)
wfFDDISmtConnectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDISmtConnectionPolicy.setStatus("mandatory")


class _WfFDDISmtTNotify_Type(Integer32):
    """Custom type wfFDDISmtTNotify based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              22,
              30)
        )
    )
    namedValues = NamedValues(
        *(("default", 22),
          ("max", 30),
          ("min", 2))
    )


_WfFDDISmtTNotify_Type.__name__ = "Integer32"
_WfFDDISmtTNotify_Object = MibTableColumn
wfFDDISmtTNotify = _WfFDDISmtTNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 31),
    _WfFDDISmtTNotify_Type()
)
wfFDDISmtTNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDISmtTNotify.setStatus("mandatory")


class _WfFDDIMacTReq_Type(Integer32):
    """Custom type wfFDDIMacTReq based on Integer32"""
    defaultValue = 2062500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2062500
        )
    )
    namedValues = NamedValues(
        ("default", 2062500)
    )


_WfFDDIMacTReq_Type.__name__ = "Integer32"
_WfFDDIMacTReq_Object = MibTableColumn
wfFDDIMacTReq = _WfFDDIMacTReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 32),
    _WfFDDIMacTReq_Type()
)
wfFDDIMacTReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIMacTReq.setStatus("mandatory")


class _WfFDDIMacTMax_Type(Integer32):
    """Custom type wfFDDIMacTMax based on Integer32"""
    defaultValue = 2097152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2097152
        )
    )
    namedValues = NamedValues(
        ("default", 2097152)
    )


_WfFDDIMacTMax_Type.__name__ = "Integer32"
_WfFDDIMacTMax_Object = MibTableColumn
wfFDDIMacTMax = _WfFDDIMacTMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 33),
    _WfFDDIMacTMax_Type()
)
wfFDDIMacTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacTMax.setStatus("mandatory")


class _WfFDDIMacTvxValue_Type(Integer32):
    """Custom type wfFDDIMacTvxValue based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            32768
        )
    )
    namedValues = NamedValues(
        ("default", 32768)
    )


_WfFDDIMacTvxValue_Type.__name__ = "Integer32"
_WfFDDIMacTvxValue_Object = MibTableColumn
wfFDDIMacTvxValue = _WfFDDIMacTvxValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 34),
    _WfFDDIMacTvxValue_Type()
)
wfFDDIMacTvxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacTvxValue.setStatus("mandatory")


class _WfFDDIMacTMin_Type(Integer32):
    """Custom type wfFDDIMacTMin based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50000
        )
    )
    namedValues = NamedValues(
        ("default", 50000)
    )


_WfFDDIMacTMin_Type.__name__ = "Integer32"
_WfFDDIMacTMin_Object = MibTableColumn
wfFDDIMacTMin = _WfFDDIMacTMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 35),
    _WfFDDIMacTMin_Type()
)
wfFDDIMacTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacTMin.setStatus("mandatory")


class _WfFDDIHardwareFilter_Type(Integer32):
    """Custom type wfFDDIHardwareFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFDDIHardwareFilter_Type.__name__ = "Integer32"
_WfFDDIHardwareFilter_Object = MibTableColumn
wfFDDIHardwareFilter = _WfFDDIHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 36),
    _WfFDDIHardwareFilter_Type()
)
wfFDDIHardwareFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIHardwareFilter.setStatus("mandatory")


class _WfFDDISmtEnable_Type(Integer32):
    """Custom type wfFDDISmtEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFDDISmtEnable_Type.__name__ = "Integer32"
_WfFDDISmtEnable_Object = MibTableColumn
wfFDDISmtEnable = _WfFDDISmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 37),
    _WfFDDISmtEnable_Type()
)
wfFDDISmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDISmtEnable.setStatus("mandatory")


class _WfFDDITxQueueLength_Type(Integer32):
    """Custom type wfFDDITxQueueLength based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 127),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfFDDITxQueueLength_Type.__name__ = "Integer32"
_WfFDDITxQueueLength_Object = MibTableColumn
wfFDDITxQueueLength = _WfFDDITxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 38),
    _WfFDDITxQueueLength_Type()
)
wfFDDITxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDITxQueueLength.setStatus("mandatory")


class _WfFDDIRxQueueLength_Type(Integer32):
    """Custom type wfFDDIRxQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 64),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfFDDIRxQueueLength_Type.__name__ = "Integer32"
_WfFDDIRxQueueLength_Object = MibTableColumn
wfFDDIRxQueueLength = _WfFDDIRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 39),
    _WfFDDIRxQueueLength_Type()
)
wfFDDIRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIRxQueueLength.setStatus("mandatory")
_WfFDDITxClipFrames_Type = Counter32
_WfFDDITxClipFrames_Object = MibTableColumn
wfFDDITxClipFrames = _WfFDDITxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 40),
    _WfFDDITxClipFrames_Type()
)
wfFDDITxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDITxClipFrames.setStatus("mandatory")
_WfFDDIRxReplenMisses_Type = Counter32
_WfFDDIRxReplenMisses_Object = MibTableColumn
wfFDDIRxReplenMisses = _WfFDDIRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 41),
    _WfFDDIRxReplenMisses_Type()
)
wfFDDIRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxReplenMisses.setStatus("mandatory")
_WfSyncTable_Object = MibTable
wfSyncTable = _WfSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5)
)
if mibBuilder.loadTexts:
    wfSyncTable.setStatus("mandatory")
_WfSyncEntry_Object = MibTableRow
wfSyncEntry = _WfSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1)
)
wfSyncEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSyncSlot"),
    (0, "Wellfleet-Series7-MIB", "wfSyncConnector"),
)
if mibBuilder.loadTexts:
    wfSyncEntry.setStatus("mandatory")


class _WfSyncDelete_Type(Integer32):
    """Custom type wfSyncDelete based on Integer32"""
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


_WfSyncDelete_Type.__name__ = "Integer32"
_WfSyncDelete_Object = MibTableColumn
wfSyncDelete = _WfSyncDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 1),
    _WfSyncDelete_Type()
)
wfSyncDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncDelete.setStatus("mandatory")


class _WfSyncDisable_Type(Integer32):
    """Custom type wfSyncDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncDisable_Type.__name__ = "Integer32"
_WfSyncDisable_Object = MibTableColumn
wfSyncDisable = _WfSyncDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 2),
    _WfSyncDisable_Type()
)
wfSyncDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncDisable.setStatus("mandatory")


class _WfSyncState_Type(Integer32):
    """Custom type wfSyncState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 5),
          ("up", 1),
          ("wait", 4))
    )


_WfSyncState_Type.__name__ = "Integer32"
_WfSyncState_Object = MibTableColumn
wfSyncState = _WfSyncState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 3),
    _WfSyncState_Type()
)
wfSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncState.setStatus("mandatory")


class _WfSyncSlot_Type(Integer32):
    """Custom type wfSyncSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfSyncSlot_Type.__name__ = "Integer32"
_WfSyncSlot_Object = MibTableColumn
wfSyncSlot = _WfSyncSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 4),
    _WfSyncSlot_Type()
)
wfSyncSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncSlot.setStatus("mandatory")


class _WfSyncConnector_Type(Integer32):
    """Custom type wfSyncConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfSyncConnector_Type.__name__ = "Integer32"
_WfSyncConnector_Object = MibTableColumn
wfSyncConnector = _WfSyncConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 5),
    _WfSyncConnector_Type()
)
wfSyncConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncConnector.setStatus("mandatory")


class _WfSyncCct_Type(Integer32):
    """Custom type wfSyncCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfSyncCct_Type.__name__ = "Integer32"
_WfSyncCct_Object = MibTableColumn
wfSyncCct = _WfSyncCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 6),
    _WfSyncCct_Type()
)
wfSyncCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCct.setStatus("mandatory")


class _WfSyncBofl_Type(Integer32):
    """Custom type wfSyncBofl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncBofl_Type.__name__ = "Integer32"
_WfSyncBofl_Object = MibTableColumn
wfSyncBofl = _WfSyncBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 7),
    _WfSyncBofl_Type()
)
wfSyncBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBofl.setStatus("mandatory")


class _WfSyncBoflTmo_Type(Integer32):
    """Custom type wfSyncBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              60)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("maximum", 60),
          ("minimum", 1))
    )


_WfSyncBoflTmo_Type.__name__ = "Integer32"
_WfSyncBoflTmo_Object = MibTableColumn
wfSyncBoflTmo = _WfSyncBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 8),
    _WfSyncBoflTmo_Type()
)
wfSyncBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBoflTmo.setStatus("mandatory")


class _WfSyncMtu_Type(Integer32):
    """Custom type wfSyncMtu based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              1600,
              4500)
        )
    )
    namedValues = NamedValues(
        *(("default", 1600),
          ("maximum", 4500),
          ("minimum", 3))
    )


_WfSyncMtu_Type.__name__ = "Integer32"
_WfSyncMtu_Object = MibTableColumn
wfSyncMtu = _WfSyncMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 9),
    _WfSyncMtu_Type()
)
wfSyncMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMtu.setStatus("mandatory")
_WfSyncMadr_Type = OctetString
_WfSyncMadr_Object = MibTableColumn
wfSyncMadr = _WfSyncMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 10),
    _WfSyncMadr_Type()
)
wfSyncMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncMadr.setStatus("mandatory")


class _WfSyncPromiscuous_Type(Integer32):
    """Custom type wfSyncPromiscuous based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncPromiscuous_Type.__name__ = "Integer32"
_WfSyncPromiscuous_Object = MibTableColumn
wfSyncPromiscuous = _WfSyncPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 11),
    _WfSyncPromiscuous_Type()
)
wfSyncPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPromiscuous.setStatus("mandatory")


class _WfSyncXid_Type(Integer32):
    """Custom type wfSyncXid based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncXid_Type.__name__ = "Integer32"
_WfSyncXid_Object = MibTableColumn
wfSyncXid = _WfSyncXid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 12),
    _WfSyncXid_Type()
)
wfSyncXid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncXid.setStatus("mandatory")


class _WfSyncClkSource_Type(Integer32):
    """Custom type wfSyncClkSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_WfSyncClkSource_Type.__name__ = "Integer32"
_WfSyncClkSource_Object = MibTableColumn
wfSyncClkSource = _WfSyncClkSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 13),
    _WfSyncClkSource_Type()
)
wfSyncClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncClkSource.setStatus("mandatory")


class _WfSyncClkSpeed_Type(Integer32):
    """Custom type wfSyncClkSpeed based on Integer32"""
    defaultValue = 64102

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2401,
              4807,
              7204,
              9615,
              19230,
              32051,
              38461,
              56818,
              64102,
              125000,
              227272,
              416666,
              625000,
              833333,
              1250000,
              2500000,
              5000000)
        )
    )
    namedValues = NamedValues(
        *(("clk1200b", 1200),
          ("clk125k", 125000),
          ("clk19200b", 19230),
          ("clk1mb", 1250000),
          ("clk230k", 227272),
          ("clk2400b", 2401),
          ("clk2mb", 2500000),
          ("clk32000b", 32051),
          ("clk38400b", 38461),
          ("clk420k", 416666),
          ("clk4800b", 4807),
          ("clk56k", 56818),
          ("clk5mb", 5000000),
          ("clk625k", 625000),
          ("clk64k", 64102),
          ("clk7200b", 7204),
          ("clk833k", 833333),
          ("clk9600b", 9615))
    )


_WfSyncClkSpeed_Type.__name__ = "Integer32"
_WfSyncClkSpeed_Object = MibTableColumn
wfSyncClkSpeed = _WfSyncClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 14),
    _WfSyncClkSpeed_Type()
)
wfSyncClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncClkSpeed.setStatus("mandatory")


class _WfSyncSignalMode_Type(Integer32):
    """Custom type wfSyncSignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 1),
          ("unbalanced", 2))
    )


_WfSyncSignalMode_Type.__name__ = "Integer32"
_WfSyncSignalMode_Object = MibTableColumn
wfSyncSignalMode = _WfSyncSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 15),
    _WfSyncSignalMode_Type()
)
wfSyncSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncSignalMode.setStatus("mandatory")


class _WfSyncRtsEnable_Type(Integer32):
    """Custom type wfSyncRtsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncRtsEnable_Type.__name__ = "Integer32"
_WfSyncRtsEnable_Object = MibTableColumn
wfSyncRtsEnable = _WfSyncRtsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 16),
    _WfSyncRtsEnable_Type()
)
wfSyncRtsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRtsEnable.setStatus("mandatory")


class _WfSyncBurstCount_Type(Integer32):
    """Custom type wfSyncBurstCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncBurstCount_Type.__name__ = "Integer32"
_WfSyncBurstCount_Object = MibTableColumn
wfSyncBurstCount = _WfSyncBurstCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 17),
    _WfSyncBurstCount_Type()
)
wfSyncBurstCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBurstCount.setStatus("mandatory")


class _WfSyncService_Type(Integer32):
    """Custom type wfSyncService based on Integer32"""
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
        *(("llc1", 2),
          ("llc2", 3),
          ("transparent", 1))
    )


_WfSyncService_Type.__name__ = "Integer32"
_WfSyncService_Object = MibTableColumn
wfSyncService = _WfSyncService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 18),
    _WfSyncService_Type()
)
wfSyncService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncService.setStatus("mandatory")


class _WfSyncRetryCount_Type(Integer32):
    """Custom type wfSyncRetryCount based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              64)
        )
    )
    namedValues = NamedValues(
        *(("default", 16),
          ("maximum", 64),
          ("minimum", 1))
    )


_WfSyncRetryCount_Type.__name__ = "Integer32"
_WfSyncRetryCount_Object = MibTableColumn
wfSyncRetryCount = _WfSyncRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 19),
    _WfSyncRetryCount_Type()
)
wfSyncRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRetryCount.setStatus("mandatory")


class _WfSyncLinkIdleTimer_Type(Integer32):
    """Custom type wfSyncLinkIdleTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("maximum", 9999),
          ("minimum", 1))
    )


_WfSyncLinkIdleTimer_Type.__name__ = "Integer32"
_WfSyncLinkIdleTimer_Object = MibTableColumn
wfSyncLinkIdleTimer = _WfSyncLinkIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 20),
    _WfSyncLinkIdleTimer_Type()
)
wfSyncLinkIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncLinkIdleTimer.setStatus("mandatory")


class _WfSyncRetryTimer_Type(Integer32):
    """Custom type wfSyncRetryTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("maximum", 9999),
          ("minimum", 1))
    )


_WfSyncRetryTimer_Type.__name__ = "Integer32"
_WfSyncRetryTimer_Object = MibTableColumn
wfSyncRetryTimer = _WfSyncRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 21),
    _WfSyncRetryTimer_Type()
)
wfSyncRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRetryTimer.setStatus("mandatory")


class _WfSyncExtendedAddress_Type(Integer32):
    """Custom type wfSyncExtendedAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncExtendedAddress_Type.__name__ = "Integer32"
_WfSyncExtendedAddress_Object = MibTableColumn
wfSyncExtendedAddress = _WfSyncExtendedAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 22),
    _WfSyncExtendedAddress_Type()
)
wfSyncExtendedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedAddress.setStatus("mandatory")


class _WfSyncExtendedAddressForce_Type(Integer32):
    """Custom type wfSyncExtendedAddressForce based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncExtendedAddressForce_Type.__name__ = "Integer32"
_WfSyncExtendedAddressForce_Object = MibTableColumn
wfSyncExtendedAddressForce = _WfSyncExtendedAddressForce_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 23),
    _WfSyncExtendedAddressForce_Type()
)
wfSyncExtendedAddressForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedAddressForce.setStatus("mandatory")


class _WfSyncExtendedControl_Type(Integer32):
    """Custom type wfSyncExtendedControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncExtendedControl_Type.__name__ = "Integer32"
_WfSyncExtendedControl_Object = MibTableColumn
wfSyncExtendedControl = _WfSyncExtendedControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 24),
    _WfSyncExtendedControl_Type()
)
wfSyncExtendedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedControl.setStatus("mandatory")


class _WfSyncExtendedControlForce_Type(Integer32):
    """Custom type wfSyncExtendedControlForce based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSyncExtendedControlForce_Type.__name__ = "Integer32"
_WfSyncExtendedControlForce_Object = MibTableColumn
wfSyncExtendedControlForce = _WfSyncExtendedControlForce_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 25),
    _WfSyncExtendedControlForce_Type()
)
wfSyncExtendedControlForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedControlForce.setStatus("mandatory")


class _WfSyncConnectAttempts_Type(Integer32):
    """Custom type wfSyncConnectAttempts based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("default", 10),
          ("maximum", 9999),
          ("minimum", 1))
    )


_WfSyncConnectAttempts_Type.__name__ = "Integer32"
_WfSyncConnectAttempts_Object = MibTableColumn
wfSyncConnectAttempts = _WfSyncConnectAttempts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 26),
    _WfSyncConnectAttempts_Type()
)
wfSyncConnectAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncConnectAttempts.setStatus("mandatory")


class _WfSyncWindowSizeTx_Type(Integer32):
    """Custom type wfSyncWindowSizeTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 7),
          ("minimum", 1))
    )


_WfSyncWindowSizeTx_Type.__name__ = "Integer32"
_WfSyncWindowSizeTx_Object = MibTableColumn
wfSyncWindowSizeTx = _WfSyncWindowSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 27),
    _WfSyncWindowSizeTx_Type()
)
wfSyncWindowSizeTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWindowSizeTx.setStatus("mandatory")


class _WfSyncWindowSizeTxExtc_Type(Integer32):
    """Custom type wfSyncWindowSizeTxExtc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 7),
          ("minimum", 1))
    )


_WfSyncWindowSizeTxExtc_Type.__name__ = "Integer32"
_WfSyncWindowSizeTxExtc_Object = MibTableColumn
wfSyncWindowSizeTxExtc = _WfSyncWindowSizeTxExtc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 28),
    _WfSyncWindowSizeTxExtc_Type()
)
wfSyncWindowSizeTxExtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWindowSizeTxExtc.setStatus("mandatory")


class _WfSyncMinFrameSpace_Type(Integer32):
    """Custom type wfSyncMinFrameSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              32)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 32),
          ("minimum", 1))
    )


_WfSyncMinFrameSpace_Type.__name__ = "Integer32"
_WfSyncMinFrameSpace_Object = MibTableColumn
wfSyncMinFrameSpace = _WfSyncMinFrameSpace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 29),
    _WfSyncMinFrameSpace_Type()
)
wfSyncMinFrameSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMinFrameSpace.setStatus("mandatory")


class _WfSyncLocalAddress_Type(Integer32):
    """Custom type wfSyncLocalAddress based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addressdce", 3),
          ("addressdte", 1),
          ("addressexplicit", 7))
    )


_WfSyncLocalAddress_Type.__name__ = "Integer32"
_WfSyncLocalAddress_Object = MibTableColumn
wfSyncLocalAddress = _WfSyncLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 30),
    _WfSyncLocalAddress_Type()
)
wfSyncLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncLocalAddress.setStatus("mandatory")


class _WfSyncRemoteAddress_Type(Integer32):
    """Custom type wfSyncRemoteAddress based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addressdce", 3),
          ("addressdte", 1),
          ("addressexplicit", 7))
    )


_WfSyncRemoteAddress_Type.__name__ = "Integer32"
_WfSyncRemoteAddress_Object = MibTableColumn
wfSyncRemoteAddress = _WfSyncRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 31),
    _WfSyncRemoteAddress_Type()
)
wfSyncRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRemoteAddress.setStatus("mandatory")
_WfSyncPassThruLocalMadr_Type = OctetString
_WfSyncPassThruLocalMadr_Object = MibTableColumn
wfSyncPassThruLocalMadr = _WfSyncPassThruLocalMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 32),
    _WfSyncPassThruLocalMadr_Type()
)
wfSyncPassThruLocalMadr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPassThruLocalMadr.setStatus("mandatory")
_WfSyncPassThruRemoteMadr_Type = OctetString
_WfSyncPassThruRemoteMadr_Object = MibTableColumn
wfSyncPassThruRemoteMadr = _WfSyncPassThruRemoteMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 33),
    _WfSyncPassThruRemoteMadr_Type()
)
wfSyncPassThruRemoteMadr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPassThruRemoteMadr.setStatus("mandatory")


class _WfSyncWanProtocol_Type(Integer32):
    """Custom type wfSyncWanProtocol based on Integer32"""
    defaultValue = 1

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
        *(("framerelay", 5),
          ("passthru", 2),
          ("ppp", 3),
          ("smds", 4),
          ("standard", 1))
    )


_WfSyncWanProtocol_Type.__name__ = "Integer32"
_WfSyncWanProtocol_Object = MibTableColumn
wfSyncWanProtocol = _WfSyncWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 34),
    _WfSyncWanProtocol_Type()
)
wfSyncWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWanProtocol.setStatus("mandatory")


class _WfSyncCrcSize_Type(Integer32):
    """Custom type wfSyncCrcSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16bit", 1),
          ("crc32bit", 2))
    )


_WfSyncCrcSize_Type.__name__ = "Integer32"
_WfSyncCrcSize_Object = MibTableColumn
wfSyncCrcSize = _WfSyncCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 35),
    _WfSyncCrcSize_Type()
)
wfSyncCrcSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCrcSize.setStatus("mandatory")
_WfSyncRxOctets_Type = Counter32
_WfSyncRxOctets_Object = MibTableColumn
wfSyncRxOctets = _WfSyncRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 36),
    _WfSyncRxOctets_Type()
)
wfSyncRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxOctets.setStatus("mandatory")
_WfSyncRxFrames_Type = Counter32
_WfSyncRxFrames_Object = MibTableColumn
wfSyncRxFrames = _WfSyncRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 37),
    _WfSyncRxFrames_Type()
)
wfSyncRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxFrames.setStatus("mandatory")
_WfSyncTxOctets_Type = Counter32
_WfSyncTxOctets_Object = MibTableColumn
wfSyncTxOctets = _WfSyncTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 38),
    _WfSyncTxOctets_Type()
)
wfSyncTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxOctets.setStatus("mandatory")
_WfSyncTxFrames_Type = Counter32
_WfSyncTxFrames_Object = MibTableColumn
wfSyncTxFrames = _WfSyncTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 39),
    _WfSyncTxFrames_Type()
)
wfSyncTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxFrames.setStatus("mandatory")
_WfSyncRxErrors_Type = Counter32
_WfSyncRxErrors_Object = MibTableColumn
wfSyncRxErrors = _WfSyncRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 40),
    _WfSyncRxErrors_Type()
)
wfSyncRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxErrors.setStatus("mandatory")
_WfSyncTxErrors_Type = Counter32
_WfSyncTxErrors_Object = MibTableColumn
wfSyncTxErrors = _WfSyncTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 41),
    _WfSyncTxErrors_Type()
)
wfSyncTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxErrors.setStatus("mandatory")
_WfSyncLackRescRx_Type = Counter32
_WfSyncLackRescRx_Object = MibTableColumn
wfSyncLackRescRx = _WfSyncLackRescRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 42),
    _WfSyncLackRescRx_Type()
)
wfSyncLackRescRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLackRescRx.setStatus("mandatory")
_WfSyncLackRescTx_Type = Counter32
_WfSyncLackRescTx_Object = MibTableColumn
wfSyncLackRescTx = _WfSyncLackRescTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 43),
    _WfSyncLackRescTx_Type()
)
wfSyncLackRescTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLackRescTx.setStatus("mandatory")
_WfSyncUnderFlowTx_Type = Counter32
_WfSyncUnderFlowTx_Object = MibTableColumn
wfSyncUnderFlowTx = _WfSyncUnderFlowTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 44),
    _WfSyncUnderFlowTx_Type()
)
wfSyncUnderFlowTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncUnderFlowTx.setStatus("mandatory")
_WfSyncRejectsTx_Type = Counter32
_WfSyncRejectsTx_Object = MibTableColumn
wfSyncRejectsTx = _WfSyncRejectsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 45),
    _WfSyncRejectsTx_Type()
)
wfSyncRejectsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRejectsTx.setStatus("mandatory")
_WfSyncRejectsRx_Type = Counter32
_WfSyncRejectsRx_Object = MibTableColumn
wfSyncRejectsRx = _WfSyncRejectsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 46),
    _WfSyncRejectsRx_Type()
)
wfSyncRejectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRejectsRx.setStatus("mandatory")
_WfSyncOverFlowRx_Type = Counter32
_WfSyncOverFlowRx_Object = MibTableColumn
wfSyncOverFlowRx = _WfSyncOverFlowRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 47),
    _WfSyncOverFlowRx_Type()
)
wfSyncOverFlowRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncOverFlowRx.setStatus("mandatory")
_WfSyncFramesIncompRx_Type = Counter32
_WfSyncFramesIncompRx_Object = MibTableColumn
wfSyncFramesIncompRx = _WfSyncFramesIncompRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 48),
    _WfSyncFramesIncompRx_Type()
)
wfSyncFramesIncompRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncFramesIncompRx.setStatus("mandatory")
_WfSyncBadFramesRx_Type = Counter32
_WfSyncBadFramesRx_Object = MibTableColumn
wfSyncBadFramesRx = _WfSyncBadFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 49),
    _WfSyncBadFramesRx_Type()
)
wfSyncBadFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncBadFramesRx.setStatus("mandatory")
_WfSyncFrameRejectsRx_Type = Counter32
_WfSyncFrameRejectsRx_Object = MibTableColumn
wfSyncFrameRejectsRx = _WfSyncFrameRejectsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 50),
    _WfSyncFrameRejectsRx_Type()
)
wfSyncFrameRejectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncFrameRejectsRx.setStatus("mandatory")
_WfSyncRuntsRx_Type = Counter32
_WfSyncRuntsRx_Object = MibTableColumn
wfSyncRuntsRx = _WfSyncRuntsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 51),
    _WfSyncRuntsRx_Type()
)
wfSyncRuntsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRuntsRx.setStatus("mandatory")
_WfSyncT1Timeouts_Type = Counter32
_WfSyncT1Timeouts_Object = MibTableColumn
wfSyncT1Timeouts = _WfSyncT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 52),
    _WfSyncT1Timeouts_Type()
)
wfSyncT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncT1Timeouts.setStatus("mandatory")
_WfSyncMemoryErrors_Type = Counter32
_WfSyncMemoryErrors_Object = MibTableColumn
wfSyncMemoryErrors = _WfSyncMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 53),
    _WfSyncMemoryErrors_Type()
)
wfSyncMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncMemoryErrors.setStatus("mandatory")


class _WfSyncMediaType_Type(Integer32):
    """Custom type wfSyncMediaType based on Integer32"""
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
        *(("default", 1),
          ("e1", 3),
          ("t1", 2))
    )


_WfSyncMediaType_Type.__name__ = "Integer32"
_WfSyncMediaType_Object = MibTableColumn
wfSyncMediaType = _WfSyncMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 54),
    _WfSyncMediaType_Type()
)
wfSyncMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMediaType.setStatus("mandatory")
_WfHwFGroup_ObjectIdentity = ObjectIdentity
wfHwFGroup = _WfHwFGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6)
)
_WfHwfTable_Object = MibTable
wfHwfTable = _WfHwfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    wfHwfTable.setStatus("mandatory")
_WfHwfEntry_Object = MibTableRow
wfHwfEntry = _WfHwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1)
)
wfHwfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfHwfSlot"),
)
if mibBuilder.loadTexts:
    wfHwfEntry.setStatus("mandatory")


class _WfHwfDelete_Type(Integer32):
    """Custom type wfHwfDelete based on Integer32"""
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


_WfHwfDelete_Type.__name__ = "Integer32"
_WfHwfDelete_Object = MibTableColumn
wfHwfDelete = _WfHwfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 1),
    _WfHwfDelete_Type()
)
wfHwfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHwfDelete.setStatus("mandatory")


class _WfHwfEnable_Type(Integer32):
    """Custom type wfHwfEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfHwfEnable_Type.__name__ = "Integer32"
_WfHwfEnable_Object = MibTableColumn
wfHwfEnable = _WfHwfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 2),
    _WfHwfEnable_Type()
)
wfHwfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHwfEnable.setStatus("mandatory")


class _WfHwfState_Type(Integer32):
    """Custom type wfHwfState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfHwfState_Type.__name__ = "Integer32"
_WfHwfState_Object = MibTableColumn
wfHwfState = _WfHwfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 3),
    _WfHwfState_Type()
)
wfHwfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfState.setStatus("mandatory")


class _WfHwfSlot_Type(Integer32):
    """Custom type wfHwfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfHwfSlot_Type.__name__ = "Integer32"
_WfHwfSlot_Object = MibTableColumn
wfHwfSlot = _WfHwfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 4),
    _WfHwfSlot_Type()
)
wfHwfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfSlot.setStatus("mandatory")
_WfHwfAvailableLines_Type = Integer32
_WfHwfAvailableLines_Object = MibTableColumn
wfHwfAvailableLines = _WfHwfAvailableLines_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 5),
    _WfHwfAvailableLines_Type()
)
wfHwfAvailableLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfAvailableLines.setStatus("mandatory")
_WfHwfLineTable_Object = MibTable
wfHwfLineTable = _WfHwfLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    wfHwfLineTable.setStatus("mandatory")
_WfHwfLineEntry_Object = MibTableRow
wfHwfLineEntry = _WfHwfLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1)
)
wfHwfLineEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfHwfLineSlot"),
    (0, "Wellfleet-Series7-MIB", "wfHwfLineNumber"),
)
if mibBuilder.loadTexts:
    wfHwfLineEntry.setStatus("mandatory")


class _WfHwfLineState_Type(Integer32):
    """Custom type wfHwfLineState based on Integer32"""
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
        *(("disabled", 2),
          ("full", 3),
          ("operational", 1))
    )


_WfHwfLineState_Type.__name__ = "Integer32"
_WfHwfLineState_Object = MibTableColumn
wfHwfLineState = _WfHwfLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 1),
    _WfHwfLineState_Type()
)
wfHwfLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineState.setStatus("mandatory")
_WfHwfLineSlot_Type = Integer32
_WfHwfLineSlot_Object = MibTableColumn
wfHwfLineSlot = _WfHwfLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 2),
    _WfHwfLineSlot_Type()
)
wfHwfLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineSlot.setStatus("mandatory")


class _WfHwfLineNumber_Type(Integer32):
    """Custom type wfHwfLineNumber based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfHwfLineNumber_Type.__name__ = "Integer32"
_WfHwfLineNumber_Object = MibTableColumn
wfHwfLineNumber = _WfHwfLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 3),
    _WfHwfLineNumber_Type()
)
wfHwfLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineNumber.setStatus("mandatory")
_WfHwfLineCct_Type = Integer32
_WfHwfLineCct_Object = MibTableColumn
wfHwfLineCct = _WfHwfLineCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 4),
    _WfHwfLineCct_Type()
)
wfHwfLineCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCct.setStatus("mandatory")
_WfHwfLineCapableMaxTblSize_Type = Integer32
_WfHwfLineCapableMaxTblSize_Object = MibTableColumn
wfHwfLineCapableMaxTblSize = _WfHwfLineCapableMaxTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 5),
    _WfHwfLineCapableMaxTblSize_Type()
)
wfHwfLineCapableMaxTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCapableMaxTblSize.setStatus("mandatory")
_WfHwfLineCurrentTblSize_Type = Integer32
_WfHwfLineCurrentTblSize_Object = MibTableColumn
wfHwfLineCurrentTblSize = _WfHwfLineCurrentTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 6),
    _WfHwfLineCurrentTblSize_Type()
)
wfHwfLineCurrentTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCurrentTblSize.setStatus("mandatory")
_WfHwfLineCurrentUsedEntries_Type = Integer32
_WfHwfLineCurrentUsedEntries_Object = MibTableColumn
wfHwfLineCurrentUsedEntries = _WfHwfLineCurrentUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 7),
    _WfHwfLineCurrentUsedEntries_Type()
)
wfHwfLineCurrentUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCurrentUsedEntries.setStatus("mandatory")
_WfHwfLineDroppedFrames_Type = Integer32
_WfHwfLineDroppedFrames_Object = MibTableColumn
wfHwfLineDroppedFrames = _WfHwfLineDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 8),
    _WfHwfLineDroppedFrames_Type()
)
wfHwfLineDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineDroppedFrames.setStatus("mandatory")
_WfHssiTable_Object = MibTable
wfHssiTable = _WfHssiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7)
)
if mibBuilder.loadTexts:
    wfHssiTable.setStatus("mandatory")
_WfHssiEntry_Object = MibTableRow
wfHssiEntry = _WfHssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1)
)
wfHssiEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfHssiSlot"),
    (0, "Wellfleet-Series7-MIB", "wfHssiConnector"),
)
if mibBuilder.loadTexts:
    wfHssiEntry.setStatus("mandatory")


class _WfHssiDelete_Type(Integer32):
    """Custom type wfHssiDelete based on Integer32"""
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


_WfHssiDelete_Type.__name__ = "Integer32"
_WfHssiDelete_Object = MibTableColumn
wfHssiDelete = _WfHssiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 1),
    _WfHssiDelete_Type()
)
wfHssiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiDelete.setStatus("mandatory")


class _WfHssiDisable_Type(Integer32):
    """Custom type wfHssiDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfHssiDisable_Type.__name__ = "Integer32"
_WfHssiDisable_Object = MibTableColumn
wfHssiDisable = _WfHssiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 2),
    _WfHssiDisable_Type()
)
wfHssiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiDisable.setStatus("mandatory")


class _WfHssiState_Type(Integer32):
    """Custom type wfHssiState based on Integer32"""
    defaultValue = 6

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
        *(("boflwait", 3),
          ("cawait", 4),
          ("init", 5),
          ("lmiwait", 2),
          ("notpresent", 6),
          ("up", 1))
    )


_WfHssiState_Type.__name__ = "Integer32"
_WfHssiState_Object = MibTableColumn
wfHssiState = _WfHssiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 3),
    _WfHssiState_Type()
)
wfHssiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiState.setStatus("mandatory")


class _WfHssiSlot_Type(Integer32):
    """Custom type wfHssiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfHssiSlot_Type.__name__ = "Integer32"
_WfHssiSlot_Object = MibTableColumn
wfHssiSlot = _WfHssiSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 4),
    _WfHssiSlot_Type()
)
wfHssiSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiSlot.setStatus("mandatory")


class _WfHssiConnector_Type(Integer32):
    """Custom type wfHssiConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfHssiConnector_Type.__name__ = "Integer32"
_WfHssiConnector_Object = MibTableColumn
wfHssiConnector = _WfHssiConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 5),
    _WfHssiConnector_Type()
)
wfHssiConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiConnector.setStatus("mandatory")


class _WfHssiCct_Type(Integer32):
    """Custom type wfHssiCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfHssiCct_Type.__name__ = "Integer32"
_WfHssiCct_Object = MibTableColumn
wfHssiCct = _WfHssiCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 6),
    _WfHssiCct_Type()
)
wfHssiCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCct.setStatus("mandatory")


class _WfHssiBofl_Type(Integer32):
    """Custom type wfHssiBofl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfHssiBofl_Type.__name__ = "Integer32"
_WfHssiBofl_Object = MibTableColumn
wfHssiBofl = _WfHssiBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 7),
    _WfHssiBofl_Type()
)
wfHssiBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBofl.setStatus("mandatory")


class _WfHssiBoflTmo_Type(Integer32):
    """Custom type wfHssiBoflTmo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              60)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 60),
          ("minimum", 1))
    )


_WfHssiBoflTmo_Type.__name__ = "Integer32"
_WfHssiBoflTmo_Object = MibTableColumn
wfHssiBoflTmo = _WfHssiBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 8),
    _WfHssiBoflTmo_Type()
)
wfHssiBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBoflTmo.setStatus("mandatory")


class _WfHssiMtu_Type(Integer32):
    """Custom type wfHssiMtu based on Integer32"""
    defaultValue = 4495

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4495,
              4500)
        )
    )
    namedValues = NamedValues(
        *(("default", 4495),
          ("maximum", 4500),
          ("minimum", 3))
    )


_WfHssiMtu_Type.__name__ = "Integer32"
_WfHssiMtu_Object = MibTableColumn
wfHssiMtu = _WfHssiMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 9),
    _WfHssiMtu_Type()
)
wfHssiMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiMtu.setStatus("mandatory")
_WfHssiMadr_Type = OctetString
_WfHssiMadr_Object = MibTableColumn
wfHssiMadr = _WfHssiMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 10),
    _WfHssiMadr_Type()
)
wfHssiMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiMadr.setStatus("mandatory")


class _WfHssiService_Type(Integer32):
    """Custom type wfHssiService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("undefined", 2))
    )


_WfHssiService_Type.__name__ = "Integer32"
_WfHssiService_Object = MibTableColumn
wfHssiService = _WfHssiService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 11),
    _WfHssiService_Type()
)
wfHssiService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiService.setStatus("mandatory")


class _WfHssiWanProtocol_Type(Integer32):
    """Custom type wfHssiWanProtocol based on Integer32"""
    defaultValue = 1

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
        *(("framerelay", 5),
          ("passthru", 2),
          ("ppp", 3),
          ("smds", 4),
          ("standard", 1))
    )


_WfHssiWanProtocol_Type.__name__ = "Integer32"
_WfHssiWanProtocol_Object = MibTableColumn
wfHssiWanProtocol = _WfHssiWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 12),
    _WfHssiWanProtocol_Type()
)
wfHssiWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiWanProtocol.setStatus("mandatory")


class _WfHssiTransmissionInterface_Type(Integer32):
    """Custom type wfHssiTransmissionInterface based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsone", 1),
          ("dsthree", 3))
    )


_WfHssiTransmissionInterface_Type.__name__ = "Integer32"
_WfHssiTransmissionInterface_Object = MibTableColumn
wfHssiTransmissionInterface = _WfHssiTransmissionInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 13),
    _WfHssiTransmissionInterface_Type()
)
wfHssiTransmissionInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTransmissionInterface.setStatus("mandatory")


class _WfHssiExternalClkSpeed_Type(Integer32):
    """Custom type wfHssiExternalClkSpeed based on Integer32"""
    defaultValue = 46359642

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(307200,
              46359642,
              52638515)
        )
    )
    namedValues = NamedValues(
        *(("default", 46359642),
          ("maximum", 52638515),
          ("minimum", 307200))
    )


_WfHssiExternalClkSpeed_Type.__name__ = "Integer32"
_WfHssiExternalClkSpeed_Object = MibTableColumn
wfHssiExternalClkSpeed = _WfHssiExternalClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 14),
    _WfHssiExternalClkSpeed_Type()
)
wfHssiExternalClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiExternalClkSpeed.setStatus("mandatory")


class _WfHssiCrcSize_Type(Integer32):
    """Custom type wfHssiCrcSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16bit", 1),
          ("crc32bit", 2))
    )


_WfHssiCrcSize_Type.__name__ = "Integer32"
_WfHssiCrcSize_Object = MibTableColumn
wfHssiCrcSize = _WfHssiCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 15),
    _WfHssiCrcSize_Type()
)
wfHssiCrcSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCrcSize.setStatus("mandatory")


class _WfHssiInternalClkTestMode_Type(Integer32):
    """Custom type wfHssiInternalClkTestMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfHssiInternalClkTestMode_Type.__name__ = "Integer32"
_WfHssiInternalClkTestMode_Object = MibTableColumn
wfHssiInternalClkTestMode = _WfHssiInternalClkTestMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 16),
    _WfHssiInternalClkTestMode_Type()
)
wfHssiInternalClkTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiInternalClkTestMode.setStatus("mandatory")
_WfHssiRxOctets_Type = Counter32
_WfHssiRxOctets_Object = MibTableColumn
wfHssiRxOctets = _WfHssiRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 17),
    _WfHssiRxOctets_Type()
)
wfHssiRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxOctets.setStatus("mandatory")
_WfHssiRxFrames_Type = Counter32
_WfHssiRxFrames_Object = MibTableColumn
wfHssiRxFrames = _WfHssiRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 18),
    _WfHssiRxFrames_Type()
)
wfHssiRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxFrames.setStatus("mandatory")
_WfHssiTxOctets_Type = Counter32
_WfHssiTxOctets_Object = MibTableColumn
wfHssiTxOctets = _WfHssiTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 19),
    _WfHssiTxOctets_Type()
)
wfHssiTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxOctets.setStatus("mandatory")
_WfHssiTxFrames_Type = Counter32
_WfHssiTxFrames_Object = MibTableColumn
wfHssiTxFrames = _WfHssiTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 20),
    _WfHssiTxFrames_Type()
)
wfHssiTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxFrames.setStatus("mandatory")
_WfHssiInDiscards_Type = Counter32
_WfHssiInDiscards_Object = MibTableColumn
wfHssiInDiscards = _WfHssiInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 21),
    _WfHssiInDiscards_Type()
)
wfHssiInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiInDiscards.setStatus("mandatory")
_WfHssiInErrors_Type = Counter32
_WfHssiInErrors_Object = MibTableColumn
wfHssiInErrors = _WfHssiInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 22),
    _WfHssiInErrors_Type()
)
wfHssiInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiInErrors.setStatus("mandatory")
_WfHssiOutDiscards_Type = Counter32
_WfHssiOutDiscards_Object = MibTableColumn
wfHssiOutDiscards = _WfHssiOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 23),
    _WfHssiOutDiscards_Type()
)
wfHssiOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiOutDiscards.setStatus("mandatory")
_WfHssiOutErrors_Type = Counter32
_WfHssiOutErrors_Object = MibTableColumn
wfHssiOutErrors = _WfHssiOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 24),
    _WfHssiOutErrors_Type()
)
wfHssiOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiOutErrors.setStatus("mandatory")
_WfHssiRxLongFrames_Type = Counter32
_WfHssiRxLongFrames_Object = MibTableColumn
wfHssiRxLongFrames = _WfHssiRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 25),
    _WfHssiRxLongFrames_Type()
)
wfHssiRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxLongFrames.setStatus("mandatory")
_WfHssiTxClipFrames_Type = Counter32
_WfHssiTxClipFrames_Object = MibTableColumn
wfHssiTxClipFrames = _WfHssiTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 26),
    _WfHssiTxClipFrames_Type()
)
wfHssiTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxClipFrames.setStatus("mandatory")
_WfHssiRxReplenMisses_Type = Counter32
_WfHssiRxReplenMisses_Object = MibTableColumn
wfHssiRxReplenMisses = _WfHssiRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 27),
    _WfHssiRxReplenMisses_Type()
)
wfHssiRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxReplenMisses.setStatus("mandatory")
_WfHssiLastRxErrorCtrl_Type = Integer32
_WfHssiLastRxErrorCtrl_Object = MibTableColumn
wfHssiLastRxErrorCtrl = _WfHssiLastRxErrorCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 28),
    _WfHssiLastRxErrorCtrl_Type()
)
wfHssiLastRxErrorCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastRxErrorCtrl.setStatus("mandatory")
_WfHssiRxCrcErrors_Type = Counter32
_WfHssiRxCrcErrors_Object = MibTableColumn
wfHssiRxCrcErrors = _WfHssiRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 29),
    _WfHssiRxCrcErrors_Type()
)
wfHssiRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxCrcErrors.setStatus("mandatory")
_WfHssiRxOverruns_Type = Counter32
_WfHssiRxOverruns_Object = MibTableColumn
wfHssiRxOverruns = _WfHssiRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 30),
    _WfHssiRxOverruns_Type()
)
wfHssiRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxOverruns.setStatus("mandatory")
_WfHssiRxAborts_Type = Counter32
_WfHssiRxAborts_Object = MibTableColumn
wfHssiRxAborts = _WfHssiRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 31),
    _WfHssiRxAborts_Type()
)
wfHssiRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxAborts.setStatus("mandatory")
_WfHssiLastTxErrorCtrl_Type = Integer32
_WfHssiLastTxErrorCtrl_Object = MibTableColumn
wfHssiLastTxErrorCtrl = _WfHssiLastTxErrorCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 32),
    _WfHssiLastTxErrorCtrl_Type()
)
wfHssiLastTxErrorCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastTxErrorCtrl.setStatus("mandatory")
_WfHssiTxAborts_Type = Counter32
_WfHssiTxAborts_Object = MibTableColumn
wfHssiTxAborts = _WfHssiTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 33),
    _WfHssiTxAborts_Type()
)
wfHssiTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxAborts.setStatus("mandatory")
_WfHssiTxUnderruns_Type = Counter32
_WfHssiTxUnderruns_Object = MibTableColumn
wfHssiTxUnderruns = _WfHssiTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 34),
    _WfHssiTxUnderruns_Type()
)
wfHssiTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxUnderruns.setStatus("mandatory")
_WfHssiRxRingErrors_Type = Counter32
_WfHssiRxRingErrors_Object = MibTableColumn
wfHssiRxRingErrors = _WfHssiRxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 35),
    _WfHssiRxRingErrors_Type()
)
wfHssiRxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxRingErrors.setStatus("mandatory")
_WfHssiLastRxRingState_Type = Integer32
_WfHssiLastRxRingState_Object = MibTableColumn
wfHssiLastRxRingState = _WfHssiLastRxRingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 36),
    _WfHssiLastRxRingState_Type()
)
wfHssiLastRxRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastRxRingState.setStatus("mandatory")
_WfHssiRxRingOverruns_Type = Counter32
_WfHssiRxRingOverruns_Object = MibTableColumn
wfHssiRxRingOverruns = _WfHssiRxRingOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 37),
    _WfHssiRxRingOverruns_Type()
)
wfHssiRxRingOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxRingOverruns.setStatus("mandatory")
_WfHssiTxRingErrors_Type = Counter32
_WfHssiTxRingErrors_Object = MibTableColumn
wfHssiTxRingErrors = _WfHssiTxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 38),
    _WfHssiTxRingErrors_Type()
)
wfHssiTxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxRingErrors.setStatus("mandatory")
_WfHssiLastTxRingState_Type = Integer32
_WfHssiLastTxRingState_Object = MibTableColumn
wfHssiLastTxRingState = _WfHssiLastTxRingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 39),
    _WfHssiLastTxRingState_Type()
)
wfHssiLastTxRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastTxRingState.setStatus("mandatory")
_WfHssiPortOpErrors_Type = Counter32
_WfHssiPortOpErrors_Object = MibTableColumn
wfHssiPortOpErrors = _WfHssiPortOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 40),
    _WfHssiPortOpErrors_Type()
)
wfHssiPortOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiPortOpErrors.setStatus("mandatory")
_WfHssiInternOpErrors_Type = Counter32
_WfHssiInternOpErrors_Object = MibTableColumn
wfHssiInternOpErrors = _WfHssiInternOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 41),
    _WfHssiInternOpErrors_Type()
)
wfHssiInternOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiInternOpErrors.setStatus("mandatory")
_WfHssiHostErrors_Type = Counter32
_WfHssiHostErrors_Object = MibTableColumn
wfHssiHostErrors = _WfHssiHostErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 42),
    _WfHssiHostErrors_Type()
)
wfHssiHostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiHostErrors.setStatus("mandatory")
_WfHssiRxProcessings_Type = Counter32
_WfHssiRxProcessings_Object = MibTableColumn
wfHssiRxProcessings = _WfHssiRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 43),
    _WfHssiRxProcessings_Type()
)
wfHssiRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxProcessings.setStatus("mandatory")
_WfHssiTxProcessings_Type = Counter32
_WfHssiTxProcessings_Object = MibTableColumn
wfHssiTxProcessings = _WfHssiTxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 44),
    _WfHssiTxProcessings_Type()
)
wfHssiTxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxProcessings.setStatus("mandatory")
_WfHssiTxCmplProcessings_Type = Counter32
_WfHssiTxCmplProcessings_Object = MibTableColumn
wfHssiTxCmplProcessings = _WfHssiTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 45),
    _WfHssiTxCmplProcessings_Type()
)
wfHssiTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxCmplProcessings.setStatus("mandatory")
_WfHssiIntrProcessings_Type = Counter32
_WfHssiIntrProcessings_Object = MibTableColumn
wfHssiIntrProcessings = _WfHssiIntrProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 46),
    _WfHssiIntrProcessings_Type()
)
wfHssiIntrProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiIntrProcessings.setStatus("mandatory")


class _WfHssiBoflNum_Type(Integer32):
    """Custom type wfHssiBoflNum based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              127)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("maximum", 127),
          ("minimum", 1))
    )


_WfHssiBoflNum_Type.__name__ = "Integer32"
_WfHssiBoflNum_Object = MibTableColumn
wfHssiBoflNum = _WfHssiBoflNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 47),
    _WfHssiBoflNum_Type()
)
wfHssiBoflNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBoflNum.setStatus("mandatory")


class _WfHssiBoflLen_Type(Integer32):
    """Custom type wfHssiBoflLen based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(22,
              100,
              4450)
        )
    )
    namedValues = NamedValues(
        *(("default", 100),
          ("maximum", 4450),
          ("minimum", 22))
    )


_WfHssiBoflLen_Type.__name__ = "Integer32"
_WfHssiBoflLen_Object = MibTableColumn
wfHssiBoflLen = _WfHssiBoflLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 48),
    _WfHssiBoflLen_Type()
)
wfHssiBoflLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBoflLen.setStatus("mandatory")


class _WfHssiRxBufferLength_Type(Integer32):
    """Custom type wfHssiRxBufferLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("length4k", 64),
          ("length8k", 128))
    )


_WfHssiRxBufferLength_Type.__name__ = "Integer32"
_WfHssiRxBufferLength_Object = MibTableColumn
wfHssiRxBufferLength = _WfHssiRxBufferLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 49),
    _WfHssiRxBufferLength_Type()
)
wfHssiRxBufferLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiRxBufferLength.setStatus("mandatory")


class _WfHssiMemPageLength_Type(Integer32):
    """Custom type wfHssiMemPageLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("length256", 3),
          ("length32", 1))
    )


_WfHssiMemPageLength_Type.__name__ = "Integer32"
_WfHssiMemPageLength_Object = MibTableColumn
wfHssiMemPageLength = _WfHssiMemPageLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 50),
    _WfHssiMemPageLength_Type()
)
wfHssiMemPageLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiMemPageLength.setStatus("mandatory")


class _WfHssiRxRingLength_Type(Integer32):
    """Custom type wfHssiRxRingLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 64),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfHssiRxRingLength_Type.__name__ = "Integer32"
_WfHssiRxRingLength_Object = MibTableColumn
wfHssiRxRingLength = _WfHssiRxRingLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 51),
    _WfHssiRxRingLength_Type()
)
wfHssiRxRingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiRxRingLength.setStatus("mandatory")


class _WfHssiTxRingLength_Type(Integer32):
    """Custom type wfHssiTxRingLength based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 127),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfHssiTxRingLength_Type.__name__ = "Integer32"
_WfHssiTxRingLength_Object = MibTableColumn
wfHssiTxRingLength = _WfHssiTxRingLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 52),
    _WfHssiTxRingLength_Type()
)
wfHssiTxRingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTxRingLength.setStatus("mandatory")


class _WfHssiRxFifoWatermark_Type(Integer32):
    """Custom type wfHssiRxFifoWatermark based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("maximum", 255),
          ("minimum", 2))
    )


_WfHssiRxFifoWatermark_Type.__name__ = "Integer32"
_WfHssiRxFifoWatermark_Object = MibTableColumn
wfHssiRxFifoWatermark = _WfHssiRxFifoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 53),
    _WfHssiRxFifoWatermark_Type()
)
wfHssiRxFifoWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiRxFifoWatermark.setStatus("mandatory")


class _WfHssiTxFifoWatermark_Type(Integer32):
    """Custom type wfHssiTxFifoWatermark based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 16),
          ("maximum", 255),
          ("minimum", 2))
    )


_WfHssiTxFifoWatermark_Type.__name__ = "Integer32"
_WfHssiTxFifoWatermark_Object = MibTableColumn
wfHssiTxFifoWatermark = _WfHssiTxFifoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 54),
    _WfHssiTxFifoWatermark_Type()
)
wfHssiTxFifoWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTxFifoWatermark.setStatus("mandatory")


class _WfHssiMaxRxMemory_Type(Integer32):
    """Custom type wfHssiMaxRxMemory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfHssiMaxRxMemory_Type.__name__ = "Integer32"
_WfHssiMaxRxMemory_Object = MibTableColumn
wfHssiMaxRxMemory = _WfHssiMaxRxMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 55),
    _WfHssiMaxRxMemory_Type()
)
wfHssiMaxRxMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiMaxRxMemory.setStatus("mandatory")


class _WfHssiLinkInterface_Type(Integer32):
    """Custom type wfHssiLinkInterface based on Integer32"""
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
        *(("ace25", 2),
          ("ace32", 3),
          ("default", 1))
    )


_WfHssiLinkInterface_Type.__name__ = "Integer32"
_WfHssiLinkInterface_Object = MibTableColumn
wfHssiLinkInterface = _WfHssiLinkInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 56),
    _WfHssiLinkInterface_Type()
)
wfHssiLinkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiLinkInterface.setStatus("mandatory")


class _WfHssiTurboBofl_Type(Integer32):
    """Custom type wfHssiTurboBofl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfHssiTurboBofl_Type.__name__ = "Integer32"
_WfHssiTurboBofl_Object = MibTableColumn
wfHssiTurboBofl = _WfHssiTurboBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 57),
    _WfHssiTurboBofl_Type()
)
wfHssiTurboBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTurboBofl.setStatus("mandatory")
_WfT1Table_Object = MibTable
wfT1Table = _WfT1Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10)
)
if mibBuilder.loadTexts:
    wfT1Table.setStatus("mandatory")
_WfT1Entry_Object = MibTableRow
wfT1Entry = _WfT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1)
)
wfT1Entry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfT1Slot"),
    (0, "Wellfleet-Series7-MIB", "wfT1Connector"),
)
if mibBuilder.loadTexts:
    wfT1Entry.setStatus("mandatory")


class _WfT1Delete_Type(Integer32):
    """Custom type wfT1Delete based on Integer32"""
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


_WfT1Delete_Type.__name__ = "Integer32"
_WfT1Delete_Object = MibTableColumn
wfT1Delete = _WfT1Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 1),
    _WfT1Delete_Type()
)
wfT1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1Delete.setStatus("mandatory")


class _WfT1Disable_Type(Integer32):
    """Custom type wfT1Disable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfT1Disable_Type.__name__ = "Integer32"
_WfT1Disable_Object = MibTableColumn
wfT1Disable = _WfT1Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 2),
    _WfT1Disable_Type()
)
wfT1Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1Disable.setStatus("mandatory")


class _WfT1State_Type(Integer32):
    """Custom type wfT1State based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfT1State_Type.__name__ = "Integer32"
_WfT1State_Object = MibTableColumn
wfT1State = _WfT1State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 3),
    _WfT1State_Type()
)
wfT1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1State.setStatus("mandatory")


class _WfT1Slot_Type(Integer32):
    """Custom type wfT1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfT1Slot_Type.__name__ = "Integer32"
_WfT1Slot_Object = MibTableColumn
wfT1Slot = _WfT1Slot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 4),
    _WfT1Slot_Type()
)
wfT1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1Slot.setStatus("mandatory")


class _WfT1Connector_Type(Integer32):
    """Custom type wfT1Connector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfT1Connector_Type.__name__ = "Integer32"
_WfT1Connector_Object = MibTableColumn
wfT1Connector = _WfT1Connector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 5),
    _WfT1Connector_Type()
)
wfT1Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1Connector.setStatus("mandatory")
_WfT1Madr_Type = OctetString
_WfT1Madr_Object = MibTableColumn
wfT1Madr = _WfT1Madr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 6),
    _WfT1Madr_Type()
)
wfT1Madr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1Madr.setStatus("mandatory")


class _WfT1FrameType_Type(Integer32):
    """Custom type wfT1FrameType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_WfT1FrameType_Type.__name__ = "Integer32"
_WfT1FrameType_Object = MibTableColumn
wfT1FrameType = _WfT1FrameType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 7),
    _WfT1FrameType_Type()
)
wfT1FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1FrameType.setStatus("mandatory")


class _WfT1LineBuildout_Type(Integer32):
    """Custom type wfT1LineBuildout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              655)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("maximum", 655),
          ("minimum", 1))
    )


_WfT1LineBuildout_Type.__name__ = "Integer32"
_WfT1LineBuildout_Object = MibTableColumn
wfT1LineBuildout = _WfT1LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 8),
    _WfT1LineBuildout_Type()
)
wfT1LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1LineBuildout.setStatus("mandatory")


class _WfT1B8ZSSupport_Type(Integer32):
    """Custom type wfT1B8ZSSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfT1B8ZSSupport_Type.__name__ = "Integer32"
_WfT1B8ZSSupport_Object = MibTableColumn
wfT1B8ZSSupport = _WfT1B8ZSSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 9),
    _WfT1B8ZSSupport_Type()
)
wfT1B8ZSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1B8ZSSupport.setStatus("mandatory")


class _WfT1ClockMode_Type(Integer32):
    """Custom type wfT1ClockMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("internal", 1),
          ("manual", 4),
          ("slave", 2))
    )


_WfT1ClockMode_Type.__name__ = "Integer32"
_WfT1ClockMode_Object = MibTableColumn
wfT1ClockMode = _WfT1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 10),
    _WfT1ClockMode_Type()
)
wfT1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1ClockMode.setStatus("mandatory")
_WfT1MiniDacs_Type = DisplayString
_WfT1MiniDacs_Object = MibTableColumn
wfT1MiniDacs = _WfT1MiniDacs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 11),
    _WfT1MiniDacs_Type()
)
wfT1MiniDacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1MiniDacs.setStatus("mandatory")
_WfT1BipolarVios_Type = Counter32
_WfT1BipolarVios_Object = MibTableColumn
wfT1BipolarVios = _WfT1BipolarVios_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 12),
    _WfT1BipolarVios_Type()
)
wfT1BipolarVios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1BipolarVios.setStatus("mandatory")
_WfT1FrameBitErrs_Type = Counter32
_WfT1FrameBitErrs_Object = MibTableColumn
wfT1FrameBitErrs = _WfT1FrameBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 13),
    _WfT1FrameBitErrs_Type()
)
wfT1FrameBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1FrameBitErrs.setStatus("mandatory")
_WfT1OutOfFrameErrs_Type = Counter32
_WfT1OutOfFrameErrs_Object = MibTableColumn
wfT1OutOfFrameErrs = _WfT1OutOfFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 14),
    _WfT1OutOfFrameErrs_Type()
)
wfT1OutOfFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1OutOfFrameErrs.setStatus("mandatory")
_WfT1SuperFrameErrs_Type = Counter32
_WfT1SuperFrameErrs_Object = MibTableColumn
wfT1SuperFrameErrs = _WfT1SuperFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 15),
    _WfT1SuperFrameErrs_Type()
)
wfT1SuperFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1SuperFrameErrs.setStatus("mandatory")
_WfT1RcvYelAlarms_Type = Counter32
_WfT1RcvYelAlarms_Object = MibTableColumn
wfT1RcvYelAlarms = _WfT1RcvYelAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 16),
    _WfT1RcvYelAlarms_Type()
)
wfT1RcvYelAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1RcvYelAlarms.setStatus("mandatory")
_WfT1RcvCarrierLoss_Type = Counter32
_WfT1RcvCarrierLoss_Object = MibTableColumn
wfT1RcvCarrierLoss = _WfT1RcvCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 17),
    _WfT1RcvCarrierLoss_Type()
)
wfT1RcvCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1RcvCarrierLoss.setStatus("mandatory")
_WfT1RcvRedAlarms_Type = Counter32
_WfT1RcvRedAlarms_Object = MibTableColumn
wfT1RcvRedAlarms = _WfT1RcvRedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 18),
    _WfT1RcvRedAlarms_Type()
)
wfT1RcvRedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1RcvRedAlarms.setStatus("mandatory")
_WfE1Table_Object = MibTable
wfE1Table = _WfE1Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11)
)
if mibBuilder.loadTexts:
    wfE1Table.setStatus("mandatory")
_WfE1Entry_Object = MibTableRow
wfE1Entry = _WfE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1)
)
wfE1Entry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfE1Slot"),
    (0, "Wellfleet-Series7-MIB", "wfE1Connector"),
)
if mibBuilder.loadTexts:
    wfE1Entry.setStatus("mandatory")


class _WfE1Delete_Type(Integer32):
    """Custom type wfE1Delete based on Integer32"""
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


_WfE1Delete_Type.__name__ = "Integer32"
_WfE1Delete_Object = MibTableColumn
wfE1Delete = _WfE1Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 1),
    _WfE1Delete_Type()
)
wfE1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1Delete.setStatus("mandatory")


class _WfE1Disable_Type(Integer32):
    """Custom type wfE1Disable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfE1Disable_Type.__name__ = "Integer32"
_WfE1Disable_Object = MibTableColumn
wfE1Disable = _WfE1Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 2),
    _WfE1Disable_Type()
)
wfE1Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1Disable.setStatus("mandatory")


class _WfE1State_Type(Integer32):
    """Custom type wfE1State based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfE1State_Type.__name__ = "Integer32"
_WfE1State_Object = MibTableColumn
wfE1State = _WfE1State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 3),
    _WfE1State_Type()
)
wfE1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1State.setStatus("mandatory")


class _WfE1Slot_Type(Integer32):
    """Custom type wfE1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 14),
          ("minimum", 1))
    )


_WfE1Slot_Type.__name__ = "Integer32"
_WfE1Slot_Object = MibTableColumn
wfE1Slot = _WfE1Slot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 4),
    _WfE1Slot_Type()
)
wfE1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1Slot.setStatus("mandatory")


class _WfE1Connector_Type(Integer32):
    """Custom type wfE1Connector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfE1Connector_Type.__name__ = "Integer32"
_WfE1Connector_Object = MibTableColumn
wfE1Connector = _WfE1Connector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 5),
    _WfE1Connector_Type()
)
wfE1Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1Connector.setStatus("mandatory")
_WfE1Madr_Type = OctetString
_WfE1Madr_Object = MibTableColumn
wfE1Madr = _WfE1Madr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 6),
    _WfE1Madr_Type()
)
wfE1Madr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1Madr.setStatus("mandatory")


class _WfE1HDB3Support_Type(Integer32):
    """Custom type wfE1HDB3Support based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfE1HDB3Support_Type.__name__ = "Integer32"
_WfE1HDB3Support_Object = MibTableColumn
wfE1HDB3Support = _WfE1HDB3Support_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 7),
    _WfE1HDB3Support_Type()
)
wfE1HDB3Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1HDB3Support.setStatus("mandatory")


class _WfE1ClockMode_Type(Integer32):
    """Custom type wfE1ClockMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("internal", 1),
          ("manual", 4),
          ("slave", 2))
    )


_WfE1ClockMode_Type.__name__ = "Integer32"
_WfE1ClockMode_Object = MibTableColumn
wfE1ClockMode = _WfE1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 8),
    _WfE1ClockMode_Type()
)
wfE1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1ClockMode.setStatus("mandatory")
_WfE1MiniDacs_Type = DisplayString
_WfE1MiniDacs_Object = MibTableColumn
wfE1MiniDacs = _WfE1MiniDacs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 9),
    _WfE1MiniDacs_Type()
)
wfE1MiniDacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1MiniDacs.setStatus("mandatory")
_WfE1BipolarVios_Type = Counter32
_WfE1BipolarVios_Object = MibTableColumn
wfE1BipolarVios = _WfE1BipolarVios_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 10),
    _WfE1BipolarVios_Type()
)
wfE1BipolarVios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1BipolarVios.setStatus("mandatory")
_WfE1FrameErrs_Type = Counter32
_WfE1FrameErrs_Object = MibTableColumn
wfE1FrameErrs = _WfE1FrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 11),
    _WfE1FrameErrs_Type()
)
wfE1FrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1FrameErrs.setStatus("mandatory")
_WfE1RcvRemAlms_Type = Counter32
_WfE1RcvRemAlms_Object = MibTableColumn
wfE1RcvRemAlms = _WfE1RcvRemAlms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 12),
    _WfE1RcvRemAlms_Type()
)
wfE1RcvRemAlms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvRemAlms.setStatus("mandatory")
_WfE1RcvMfmAlms_Type = Counter32
_WfE1RcvMfmAlms_Object = MibTableColumn
wfE1RcvMfmAlms = _WfE1RcvMfmAlms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 13),
    _WfE1RcvMfmAlms_Type()
)
wfE1RcvMfmAlms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvMfmAlms.setStatus("mandatory")
_WfE1MfsErrs_Type = Counter32
_WfE1MfsErrs_Object = MibTableColumn
wfE1MfsErrs = _WfE1MfsErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 14),
    _WfE1MfsErrs_Type()
)
wfE1MfsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1MfsErrs.setStatus("mandatory")
_WfE1SyncLoss_Type = Counter32
_WfE1SyncLoss_Object = MibTableColumn
wfE1SyncLoss = _WfE1SyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 15),
    _WfE1SyncLoss_Type()
)
wfE1SyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1SyncLoss.setStatus("mandatory")
_WfE1RcvSig1s_Type = Counter32
_WfE1RcvSig1s_Object = MibTableColumn
wfE1RcvSig1s = _WfE1RcvSig1s_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 16),
    _WfE1RcvSig1s_Type()
)
wfE1RcvSig1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvSig1s.setStatus("mandatory")
_WfE1RcvUnfrm1s_Type = Counter32
_WfE1RcvUnfrm1s_Object = MibTableColumn
wfE1RcvUnfrm1s = _WfE1RcvUnfrm1s_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 17),
    _WfE1RcvUnfrm1s_Type()
)
wfE1RcvUnfrm1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvUnfrm1s.setStatus("mandatory")
_WfDs1Group_ObjectIdentity = ObjectIdentity
wfDs1Group = _WfDs1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12)
)
_WfDs1Config_Object = MibTable
wfDs1Config = _WfDs1Config_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1)
)
if mibBuilder.loadTexts:
    wfDs1Config.setStatus("mandatory")
_WfDs1ConfigEntry_Object = MibTableRow
wfDs1ConfigEntry = _WfDs1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1)
)
wfDs1ConfigEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1LineIndex"),
)
if mibBuilder.loadTexts:
    wfDs1ConfigEntry.setStatus("mandatory")


class _WfDs1LineIndex_Type(Integer32):
    """Custom type wfDs1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1LineIndex_Type.__name__ = "Integer32"
_WfDs1LineIndex_Object = MibTableColumn
wfDs1LineIndex = _WfDs1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 1),
    _WfDs1LineIndex_Type()
)
wfDs1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LineIndex.setStatus("mandatory")
_WfDs1TimeElapsed_Type = Integer32
_WfDs1TimeElapsed_Object = MibTableColumn
wfDs1TimeElapsed = _WfDs1TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 2),
    _WfDs1TimeElapsed_Type()
)
wfDs1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TimeElapsed.setStatus("mandatory")
_WfDs1ValidIntervals_Type = Integer32
_WfDs1ValidIntervals_Object = MibTableColumn
wfDs1ValidIntervals = _WfDs1ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 3),
    _WfDs1ValidIntervals_Type()
)
wfDs1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1ValidIntervals.setStatus("mandatory")


class _WfDs1LineType_Type(Integer32):
    """Custom type wfDs1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("ds1ansi-esf", 4)
    )


_WfDs1LineType_Type.__name__ = "Integer32"
_WfDs1LineType_Object = MibTableColumn
wfDs1LineType = _WfDs1LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 4),
    _WfDs1LineType_Type()
)
wfDs1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LineType.setStatus("mandatory")


class _WfDs1ZeroCoding_Type(Integer32):
    """Custom type wfDs1ZeroCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds1b8zs", 2),
          ("ds1zbtsi", 5))
    )


_WfDs1ZeroCoding_Type.__name__ = "Integer32"
_WfDs1ZeroCoding_Object = MibTableColumn
wfDs1ZeroCoding = _WfDs1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 5),
    _WfDs1ZeroCoding_Type()
)
wfDs1ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1ZeroCoding.setStatus("mandatory")


class _WfDs1SendCode_Type(Integer32):
    """Custom type wfDs1SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ds1sendnocode", 2)
    )


_WfDs1SendCode_Type.__name__ = "Integer32"
_WfDs1SendCode_Object = MibTableColumn
wfDs1SendCode = _WfDs1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 6),
    _WfDs1SendCode_Type()
)
wfDs1SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1SendCode.setStatus("mandatory")
_WfDs1CircuitIdentifier_Type = DisplayString
_WfDs1CircuitIdentifier_Object = MibTableColumn
wfDs1CircuitIdentifier = _WfDs1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 7),
    _WfDs1CircuitIdentifier_Type()
)
wfDs1CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CircuitIdentifier.setStatus("mandatory")


class _WfDs1LoopbackConfig_Type(Integer32):
    """Custom type wfDs1LoopbackConfig based on Integer32"""
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
        *(("ds1mgrlineloop", 3),
          ("ds1mgrpayloadloop", 2),
          ("ds1netreqlineloop", 5),
          ("ds1netreqpayloadloop", 4),
          ("ds1noloop", 1),
          ("ds1otherloop", 6))
    )


_WfDs1LoopbackConfig_Type.__name__ = "Integer32"
_WfDs1LoopbackConfig_Object = MibTableColumn
wfDs1LoopbackConfig = _WfDs1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 8),
    _WfDs1LoopbackConfig_Type()
)
wfDs1LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LoopbackConfig.setStatus("mandatory")


class _WfDs1LineStatus_Type(Integer32):
    """Custom type wfDs1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ds1alarmindicationsignal", 4),
          ("ds1farendalarm", 2),
          ("ds1loopbackstate", 32),
          ("ds1lossofframe", 8),
          ("ds1lossofsignal", 16),
          ("ds1noalarm", 1))
    )


_WfDs1LineStatus_Type.__name__ = "Integer32"
_WfDs1LineStatus_Object = MibTableColumn
wfDs1LineStatus = _WfDs1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 9),
    _WfDs1LineStatus_Type()
)
wfDs1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LineStatus.setStatus("mandatory")
_WfDs1Current_Object = MibTable
wfDs1Current = _WfDs1Current_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2)
)
if mibBuilder.loadTexts:
    wfDs1Current.setStatus("mandatory")
_WfDs1CurrentEntry_Object = MibTableRow
wfDs1CurrentEntry = _WfDs1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1)
)
wfDs1CurrentEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1CurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs1CurrentEntry.setStatus("mandatory")


class _WfDs1CurrentIndex_Type(Integer32):
    """Custom type wfDs1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1CurrentIndex_Type.__name__ = "Integer32"
_WfDs1CurrentIndex_Object = MibTableColumn
wfDs1CurrentIndex = _WfDs1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 1),
    _WfDs1CurrentIndex_Type()
)
wfDs1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentIndex.setStatus("mandatory")
_WfDs1CurrentESs_Type = Counter32
_WfDs1CurrentESs_Object = MibTableColumn
wfDs1CurrentESs = _WfDs1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 2),
    _WfDs1CurrentESs_Type()
)
wfDs1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentESs.setStatus("mandatory")
_WfDs1CurrentSESs_Type = Counter32
_WfDs1CurrentSESs_Object = MibTableColumn
wfDs1CurrentSESs = _WfDs1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 3),
    _WfDs1CurrentSESs_Type()
)
wfDs1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentSESs.setStatus("mandatory")
_WfDs1CurrentSEFs_Type = Counter32
_WfDs1CurrentSEFs_Object = MibTableColumn
wfDs1CurrentSEFs = _WfDs1CurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 4),
    _WfDs1CurrentSEFs_Type()
)
wfDs1CurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentSEFs.setStatus("mandatory")
_WfDs1CurrentUASs_Type = Counter32
_WfDs1CurrentUASs_Object = MibTableColumn
wfDs1CurrentUASs = _WfDs1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 5),
    _WfDs1CurrentUASs_Type()
)
wfDs1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentUASs.setStatus("mandatory")
_WfDs1CurrentBPVs_Type = Counter32
_WfDs1CurrentBPVs_Object = MibTableColumn
wfDs1CurrentBPVs = _WfDs1CurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 6),
    _WfDs1CurrentBPVs_Type()
)
wfDs1CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentBPVs.setStatus("mandatory")
_WfDs1CurrentCVs_Type = Counter32
_WfDs1CurrentCVs_Object = MibTableColumn
wfDs1CurrentCVs = _WfDs1CurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 7),
    _WfDs1CurrentCVs_Type()
)
wfDs1CurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentCVs.setStatus("mandatory")
_WfDs1Interval_Object = MibTable
wfDs1Interval = _WfDs1Interval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3)
)
if mibBuilder.loadTexts:
    wfDs1Interval.setStatus("mandatory")
_WfDs1IntervalEntry_Object = MibTableRow
wfDs1IntervalEntry = _WfDs1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1)
)
wfDs1IntervalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1IntervalIndex"),
    (0, "Wellfleet-Series7-MIB", "wfDs1IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1IntervalEntry.setStatus("mandatory")


class _WfDs1IntervalIndex_Type(Integer32):
    """Custom type wfDs1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1IntervalIndex_Type.__name__ = "Integer32"
_WfDs1IntervalIndex_Object = MibTableColumn
wfDs1IntervalIndex = _WfDs1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 1),
    _WfDs1IntervalIndex_Type()
)
wfDs1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalIndex.setStatus("mandatory")


class _WfDs1IntervalNumber_Type(Integer32):
    """Custom type wfDs1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              96)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 96),
          ("minimum", 1))
    )


_WfDs1IntervalNumber_Type.__name__ = "Integer32"
_WfDs1IntervalNumber_Object = MibTableColumn
wfDs1IntervalNumber = _WfDs1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 2),
    _WfDs1IntervalNumber_Type()
)
wfDs1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalNumber.setStatus("mandatory")
_WfDs1IntervalESs_Type = Gauge32
_WfDs1IntervalESs_Object = MibTableColumn
wfDs1IntervalESs = _WfDs1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 3),
    _WfDs1IntervalESs_Type()
)
wfDs1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalESs.setStatus("mandatory")
_WfDs1IntervalSESs_Type = Gauge32
_WfDs1IntervalSESs_Object = MibTableColumn
wfDs1IntervalSESs = _WfDs1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 4),
    _WfDs1IntervalSESs_Type()
)
wfDs1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalSESs.setStatus("mandatory")
_WfDs1IntervalSEFs_Type = Gauge32
_WfDs1IntervalSEFs_Object = MibTableColumn
wfDs1IntervalSEFs = _WfDs1IntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 5),
    _WfDs1IntervalSEFs_Type()
)
wfDs1IntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalSEFs.setStatus("mandatory")
_WfDs1IntervalUASs_Type = Gauge32
_WfDs1IntervalUASs_Object = MibTableColumn
wfDs1IntervalUASs = _WfDs1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 6),
    _WfDs1IntervalUASs_Type()
)
wfDs1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalUASs.setStatus("mandatory")
_WfDs1IntervalBPVs_Type = Gauge32
_WfDs1IntervalBPVs_Object = MibTableColumn
wfDs1IntervalBPVs = _WfDs1IntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 7),
    _WfDs1IntervalBPVs_Type()
)
wfDs1IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalBPVs.setStatus("mandatory")
_WfDs1IntervalCVs_Type = Gauge32
_WfDs1IntervalCVs_Object = MibTableColumn
wfDs1IntervalCVs = _WfDs1IntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 8),
    _WfDs1IntervalCVs_Type()
)
wfDs1IntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalCVs.setStatus("mandatory")
_WfDs1Total_Object = MibTable
wfDs1Total = _WfDs1Total_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4)
)
if mibBuilder.loadTexts:
    wfDs1Total.setStatus("mandatory")
_WfDs1TotalEntry_Object = MibTableRow
wfDs1TotalEntry = _WfDs1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1)
)
wfDs1TotalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1TotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs1TotalEntry.setStatus("mandatory")


class _WfDs1TotalIndex_Type(Integer32):
    """Custom type wfDs1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1TotalIndex_Type.__name__ = "Integer32"
_WfDs1TotalIndex_Object = MibTableColumn
wfDs1TotalIndex = _WfDs1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 1),
    _WfDs1TotalIndex_Type()
)
wfDs1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalIndex.setStatus("mandatory")
_WfDs1TotalESs_Type = Gauge32
_WfDs1TotalESs_Object = MibTableColumn
wfDs1TotalESs = _WfDs1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 2),
    _WfDs1TotalESs_Type()
)
wfDs1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalESs.setStatus("mandatory")
_WfDs1TotalSESs_Type = Gauge32
_WfDs1TotalSESs_Object = MibTableColumn
wfDs1TotalSESs = _WfDs1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 3),
    _WfDs1TotalSESs_Type()
)
wfDs1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalSESs.setStatus("mandatory")
_WfDs1TotalSEFs_Type = Gauge32
_WfDs1TotalSEFs_Object = MibTableColumn
wfDs1TotalSEFs = _WfDs1TotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 4),
    _WfDs1TotalSEFs_Type()
)
wfDs1TotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalSEFs.setStatus("mandatory")
_WfDs1TotalUASs_Type = Gauge32
_WfDs1TotalUASs_Object = MibTableColumn
wfDs1TotalUASs = _WfDs1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 5),
    _WfDs1TotalUASs_Type()
)
wfDs1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalUASs.setStatus("mandatory")
_WfDs1TotalBPVs_Type = Gauge32
_WfDs1TotalBPVs_Object = MibTableColumn
wfDs1TotalBPVs = _WfDs1TotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 6),
    _WfDs1TotalBPVs_Type()
)
wfDs1TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalBPVs.setStatus("mandatory")
_WfDs1TotalCVs_Type = Gauge32
_WfDs1TotalCVs_Object = MibTableColumn
wfDs1TotalCVs = _WfDs1TotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 7),
    _WfDs1TotalCVs_Type()
)
wfDs1TotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalCVs.setStatus("mandatory")
_WfDs1FeCurrent_Object = MibTable
wfDs1FeCurrent = _WfDs1FeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5)
)
if mibBuilder.loadTexts:
    wfDs1FeCurrent.setStatus("mandatory")
_WfDs1FeCurrentEntry_Object = MibTableRow
wfDs1FeCurrentEntry = _WfDs1FeCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1)
)
wfDs1FeCurrentEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1FeCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs1FeCurrentEntry.setStatus("mandatory")


class _WfDs1FeCurrentIndex_Type(Integer32):
    """Custom type wfDs1FeCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1FeCurrentIndex_Type.__name__ = "Integer32"
_WfDs1FeCurrentIndex_Object = MibTableColumn
wfDs1FeCurrentIndex = _WfDs1FeCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 1),
    _WfDs1FeCurrentIndex_Type()
)
wfDs1FeCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentIndex.setStatus("mandatory")
_WfDs1FeCurrentESs_Type = Counter32
_WfDs1FeCurrentESs_Object = MibTableColumn
wfDs1FeCurrentESs = _WfDs1FeCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 2),
    _WfDs1FeCurrentESs_Type()
)
wfDs1FeCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentESs.setStatus("mandatory")
_WfDs1FeCurrentSESs_Type = Counter32
_WfDs1FeCurrentSESs_Object = MibTableColumn
wfDs1FeCurrentSESs = _WfDs1FeCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 3),
    _WfDs1FeCurrentSESs_Type()
)
wfDs1FeCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentSESs.setStatus("mandatory")
_WfDs1FeCurrentSEFs_Type = Counter32
_WfDs1FeCurrentSEFs_Object = MibTableColumn
wfDs1FeCurrentSEFs = _WfDs1FeCurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 4),
    _WfDs1FeCurrentSEFs_Type()
)
wfDs1FeCurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentSEFs.setStatus("mandatory")
_WfDs1FeCurrentBPVs_Type = Counter32
_WfDs1FeCurrentBPVs_Object = MibTableColumn
wfDs1FeCurrentBPVs = _WfDs1FeCurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 5),
    _WfDs1FeCurrentBPVs_Type()
)
wfDs1FeCurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentBPVs.setStatus("mandatory")
_WfDs1FeCurrentCVs_Type = Counter32
_WfDs1FeCurrentCVs_Object = MibTableColumn
wfDs1FeCurrentCVs = _WfDs1FeCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 6),
    _WfDs1FeCurrentCVs_Type()
)
wfDs1FeCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentCVs.setStatus("mandatory")
_WfDs1FeInterval_Object = MibTable
wfDs1FeInterval = _WfDs1FeInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6)
)
if mibBuilder.loadTexts:
    wfDs1FeInterval.setStatus("mandatory")
_WfDs1FeIntervalEntry_Object = MibTableRow
wfDs1FeIntervalEntry = _WfDs1FeIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1)
)
wfDs1FeIntervalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1FeIntervalIndex"),
    (0, "Wellfleet-Series7-MIB", "wfDs1FeIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1FeIntervalEntry.setStatus("mandatory")


class _WfDs1FeIntervalIndex_Type(Integer32):
    """Custom type wfDs1FeIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1FeIntervalIndex_Type.__name__ = "Integer32"
_WfDs1FeIntervalIndex_Object = MibTableColumn
wfDs1FeIntervalIndex = _WfDs1FeIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 1),
    _WfDs1FeIntervalIndex_Type()
)
wfDs1FeIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalIndex.setStatus("mandatory")


class _WfDs1FeIntervalNumber_Type(Integer32):
    """Custom type wfDs1FeIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              96)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 96),
          ("minimum", 1))
    )


_WfDs1FeIntervalNumber_Type.__name__ = "Integer32"
_WfDs1FeIntervalNumber_Object = MibTableColumn
wfDs1FeIntervalNumber = _WfDs1FeIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 2),
    _WfDs1FeIntervalNumber_Type()
)
wfDs1FeIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalNumber.setStatus("mandatory")
_WfDs1FeIntervalESs_Type = Gauge32
_WfDs1FeIntervalESs_Object = MibTableColumn
wfDs1FeIntervalESs = _WfDs1FeIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 3),
    _WfDs1FeIntervalESs_Type()
)
wfDs1FeIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalESs.setStatus("mandatory")
_WfDs1FeIntervalSESs_Type = Gauge32
_WfDs1FeIntervalSESs_Object = MibTableColumn
wfDs1FeIntervalSESs = _WfDs1FeIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 4),
    _WfDs1FeIntervalSESs_Type()
)
wfDs1FeIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalSESs.setStatus("mandatory")
_WfDs1FeIntervalSEFs_Type = Gauge32
_WfDs1FeIntervalSEFs_Object = MibTableColumn
wfDs1FeIntervalSEFs = _WfDs1FeIntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 5),
    _WfDs1FeIntervalSEFs_Type()
)
wfDs1FeIntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalSEFs.setStatus("mandatory")
_WfDs1FeIntervalBPVs_Type = Gauge32
_WfDs1FeIntervalBPVs_Object = MibTableColumn
wfDs1FeIntervalBPVs = _WfDs1FeIntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 6),
    _WfDs1FeIntervalBPVs_Type()
)
wfDs1FeIntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalBPVs.setStatus("mandatory")
_WfDs1FeIntervalCVs_Type = Gauge32
_WfDs1FeIntervalCVs_Object = MibTableColumn
wfDs1FeIntervalCVs = _WfDs1FeIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 7),
    _WfDs1FeIntervalCVs_Type()
)
wfDs1FeIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalCVs.setStatus("mandatory")
_WfDs1FeTotal_Object = MibTable
wfDs1FeTotal = _WfDs1FeTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7)
)
if mibBuilder.loadTexts:
    wfDs1FeTotal.setStatus("mandatory")
_WfDs1FeTotalEntry_Object = MibTableRow
wfDs1FeTotalEntry = _WfDs1FeTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1)
)
wfDs1FeTotalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs1FeTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs1FeTotalEntry.setStatus("mandatory")


class _WfDs1FeTotalIndex_Type(Integer32):
    """Custom type wfDs1FeTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs1FeTotalIndex_Type.__name__ = "Integer32"
_WfDs1FeTotalIndex_Object = MibTableColumn
wfDs1FeTotalIndex = _WfDs1FeTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 1),
    _WfDs1FeTotalIndex_Type()
)
wfDs1FeTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalIndex.setStatus("mandatory")
_WfDs1FeTotalESs_Type = Gauge32
_WfDs1FeTotalESs_Object = MibTableColumn
wfDs1FeTotalESs = _WfDs1FeTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 2),
    _WfDs1FeTotalESs_Type()
)
wfDs1FeTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalESs.setStatus("mandatory")
_WfDs1FeTotalSESs_Type = Gauge32
_WfDs1FeTotalSESs_Object = MibTableColumn
wfDs1FeTotalSESs = _WfDs1FeTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 3),
    _WfDs1FeTotalSESs_Type()
)
wfDs1FeTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalSESs.setStatus("mandatory")
_WfDs1FeTotalSEFs_Type = Gauge32
_WfDs1FeTotalSEFs_Object = MibTableColumn
wfDs1FeTotalSEFs = _WfDs1FeTotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 4),
    _WfDs1FeTotalSEFs_Type()
)
wfDs1FeTotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalSEFs.setStatus("mandatory")
_WfDs1FeTotalBPVs_Type = Gauge32
_WfDs1FeTotalBPVs_Object = MibTableColumn
wfDs1FeTotalBPVs = _WfDs1FeTotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 5),
    _WfDs1FeTotalBPVs_Type()
)
wfDs1FeTotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalBPVs.setStatus("mandatory")
_WfDs1FeTotalCVs_Type = Gauge32
_WfDs1FeTotalCVs_Object = MibTableColumn
wfDs1FeTotalCVs = _WfDs1FeTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 6),
    _WfDs1FeTotalCVs_Type()
)
wfDs1FeTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalCVs.setStatus("mandatory")
_WfDs3Group_ObjectIdentity = ObjectIdentity
wfDs3Group = _WfDs3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13)
)
_WfDs3Config_Object = MibTable
wfDs3Config = _WfDs3Config_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1)
)
if mibBuilder.loadTexts:
    wfDs3Config.setStatus("mandatory")
_WfDs3ConfigEntry_Object = MibTableRow
wfDs3ConfigEntry = _WfDs3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1)
)
wfDs3ConfigEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3LineIndex"),
)
if mibBuilder.loadTexts:
    wfDs3ConfigEntry.setStatus("mandatory")


class _WfDs3LineIndex_Type(Integer32):
    """Custom type wfDs3LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3LineIndex_Type.__name__ = "Integer32"
_WfDs3LineIndex_Object = MibTableColumn
wfDs3LineIndex = _WfDs3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 1),
    _WfDs3LineIndex_Type()
)
wfDs3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LineIndex.setStatus("mandatory")
_WfDs3TimeElapsed_Type = Integer32
_WfDs3TimeElapsed_Object = MibTableColumn
wfDs3TimeElapsed = _WfDs3TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 2),
    _WfDs3TimeElapsed_Type()
)
wfDs3TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TimeElapsed.setStatus("mandatory")
_WfDs3ValidIntervals_Type = Integer32
_WfDs3ValidIntervals_Object = MibTableColumn
wfDs3ValidIntervals = _WfDs3ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 3),
    _WfDs3ValidIntervals_Type()
)
wfDs3ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3ValidIntervals.setStatus("mandatory")


class _WfDs3LineType_Type(Integer32):
    """Custom type wfDs3LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds3cbitparity", 4),
          ("ds3clearchannel", 5),
          ("other", 1))
    )


_WfDs3LineType_Type.__name__ = "Integer32"
_WfDs3LineType_Object = MibTableColumn
wfDs3LineType = _WfDs3LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 4),
    _WfDs3LineType_Type()
)
wfDs3LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LineType.setStatus("mandatory")


class _WfDs3ZeroCoding_Type(Integer32):
    """Custom type wfDs3ZeroCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ds3b3zs", 2)
    )


_WfDs3ZeroCoding_Type.__name__ = "Integer32"
_WfDs3ZeroCoding_Object = MibTableColumn
wfDs3ZeroCoding = _WfDs3ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 5),
    _WfDs3ZeroCoding_Type()
)
wfDs3ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3ZeroCoding.setStatus("mandatory")


class _WfDs3SendCode_Type(Integer32):
    """Custom type wfDs3SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ds3sendnocode", 2)
    )


_WfDs3SendCode_Type.__name__ = "Integer32"
_WfDs3SendCode_Object = MibTableColumn
wfDs3SendCode = _WfDs3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 6),
    _WfDs3SendCode_Type()
)
wfDs3SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3SendCode.setStatus("mandatory")
_WfDs3CircuitIdentifier_Type = DisplayString
_WfDs3CircuitIdentifier_Object = MibTableColumn
wfDs3CircuitIdentifier = _WfDs3CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 7),
    _WfDs3CircuitIdentifier_Type()
)
wfDs3CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CircuitIdentifier.setStatus("mandatory")


class _WfDs3LoopbackConfig_Type(Integer32):
    """Custom type wfDs3LoopbackConfig based on Integer32"""
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
        *(("ds3mgrlineloop", 3),
          ("ds3mgrpayloadloop", 2),
          ("ds3netreqlineloop", 5),
          ("ds3netreqpayloadloop", 4),
          ("ds3noloop", 1),
          ("ds3otherloop", 6))
    )


_WfDs3LoopbackConfig_Type.__name__ = "Integer32"
_WfDs3LoopbackConfig_Object = MibTableColumn
wfDs3LoopbackConfig = _WfDs3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 8),
    _WfDs3LoopbackConfig_Type()
)
wfDs3LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LoopbackConfig.setStatus("mandatory")


class _WfDs3LineStatus_Type(Integer32):
    """Custom type wfDs3LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ds3alarmindicationsignal", 4),
          ("ds3farendalarm", 2),
          ("ds3loopbackstate", 32),
          ("ds3lossofframe", 8),
          ("ds3lossofsignal", 16),
          ("ds3noalarm", 1))
    )


_WfDs3LineStatus_Type.__name__ = "Integer32"
_WfDs3LineStatus_Object = MibTableColumn
wfDs3LineStatus = _WfDs3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 9),
    _WfDs3LineStatus_Type()
)
wfDs3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LineStatus.setStatus("mandatory")
_WfDs3Current_Object = MibTable
wfDs3Current = _WfDs3Current_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2)
)
if mibBuilder.loadTexts:
    wfDs3Current.setStatus("mandatory")
_WfDs3CurrentEntry_Object = MibTableRow
wfDs3CurrentEntry = _WfDs3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1)
)
wfDs3CurrentEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3CurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs3CurrentEntry.setStatus("mandatory")


class _WfDs3CurrentIndex_Type(Integer32):
    """Custom type wfDs3CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3CurrentIndex_Type.__name__ = "Integer32"
_WfDs3CurrentIndex_Object = MibTableColumn
wfDs3CurrentIndex = _WfDs3CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 1),
    _WfDs3CurrentIndex_Type()
)
wfDs3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentIndex.setStatus("mandatory")
_WfDs3CurrentESs_Type = Counter32
_WfDs3CurrentESs_Object = MibTableColumn
wfDs3CurrentESs = _WfDs3CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 2),
    _WfDs3CurrentESs_Type()
)
wfDs3CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentESs.setStatus("mandatory")
_WfDs3CurrentSESs_Type = Counter32
_WfDs3CurrentSESs_Object = MibTableColumn
wfDs3CurrentSESs = _WfDs3CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 3),
    _WfDs3CurrentSESs_Type()
)
wfDs3CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentSESs.setStatus("mandatory")
_WfDs3CurrentSEFs_Type = Counter32
_WfDs3CurrentSEFs_Object = MibTableColumn
wfDs3CurrentSEFs = _WfDs3CurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 4),
    _WfDs3CurrentSEFs_Type()
)
wfDs3CurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentSEFs.setStatus("mandatory")
_WfDs3CurrentUASs_Type = Counter32
_WfDs3CurrentUASs_Object = MibTableColumn
wfDs3CurrentUASs = _WfDs3CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 5),
    _WfDs3CurrentUASs_Type()
)
wfDs3CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentUASs.setStatus("mandatory")
_WfDs3CurrentBPVs_Type = Counter32
_WfDs3CurrentBPVs_Object = MibTableColumn
wfDs3CurrentBPVs = _WfDs3CurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 6),
    _WfDs3CurrentBPVs_Type()
)
wfDs3CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentBPVs.setStatus("mandatory")
_WfDs3CurrentCVs_Type = Counter32
_WfDs3CurrentCVs_Object = MibTableColumn
wfDs3CurrentCVs = _WfDs3CurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 7),
    _WfDs3CurrentCVs_Type()
)
wfDs3CurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentCVs.setStatus("mandatory")
_WfDs3Interval_Object = MibTable
wfDs3Interval = _WfDs3Interval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3)
)
if mibBuilder.loadTexts:
    wfDs3Interval.setStatus("mandatory")
_WfDs3IntervalEntry_Object = MibTableRow
wfDs3IntervalEntry = _WfDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1)
)
wfDs3IntervalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3IntervalIndex"),
    (0, "Wellfleet-Series7-MIB", "wfDs3IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs3IntervalEntry.setStatus("mandatory")


class _WfDs3IntervalIndex_Type(Integer32):
    """Custom type wfDs3IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3IntervalIndex_Type.__name__ = "Integer32"
_WfDs3IntervalIndex_Object = MibTableColumn
wfDs3IntervalIndex = _WfDs3IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 1),
    _WfDs3IntervalIndex_Type()
)
wfDs3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalIndex.setStatus("mandatory")


class _WfDs3IntervalNumber_Type(Integer32):
    """Custom type wfDs3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              96)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 96),
          ("minimum", 1))
    )


_WfDs3IntervalNumber_Type.__name__ = "Integer32"
_WfDs3IntervalNumber_Object = MibTableColumn
wfDs3IntervalNumber = _WfDs3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 2),
    _WfDs3IntervalNumber_Type()
)
wfDs3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalNumber.setStatus("mandatory")
_WfDs3IntervalESs_Type = Gauge32
_WfDs3IntervalESs_Object = MibTableColumn
wfDs3IntervalESs = _WfDs3IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 3),
    _WfDs3IntervalESs_Type()
)
wfDs3IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalESs.setStatus("mandatory")
_WfDs3IntervalSESs_Type = Gauge32
_WfDs3IntervalSESs_Object = MibTableColumn
wfDs3IntervalSESs = _WfDs3IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 4),
    _WfDs3IntervalSESs_Type()
)
wfDs3IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalSESs.setStatus("mandatory")
_WfDs3IntervalSEFs_Type = Gauge32
_WfDs3IntervalSEFs_Object = MibTableColumn
wfDs3IntervalSEFs = _WfDs3IntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 5),
    _WfDs3IntervalSEFs_Type()
)
wfDs3IntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalSEFs.setStatus("mandatory")
_WfDs3IntervalUASs_Type = Gauge32
_WfDs3IntervalUASs_Object = MibTableColumn
wfDs3IntervalUASs = _WfDs3IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 6),
    _WfDs3IntervalUASs_Type()
)
wfDs3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalUASs.setStatus("mandatory")
_WfDs3IntervalBPVs_Type = Gauge32
_WfDs3IntervalBPVs_Object = MibTableColumn
wfDs3IntervalBPVs = _WfDs3IntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 7),
    _WfDs3IntervalBPVs_Type()
)
wfDs3IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalBPVs.setStatus("mandatory")
_WfDs3IntervalCVs_Type = Gauge32
_WfDs3IntervalCVs_Object = MibTableColumn
wfDs3IntervalCVs = _WfDs3IntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 8),
    _WfDs3IntervalCVs_Type()
)
wfDs3IntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalCVs.setStatus("mandatory")
_WfDs3Total_Object = MibTable
wfDs3Total = _WfDs3Total_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4)
)
if mibBuilder.loadTexts:
    wfDs3Total.setStatus("mandatory")
_WfDs3TotalEntry_Object = MibTableRow
wfDs3TotalEntry = _WfDs3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1)
)
wfDs3TotalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3TotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs3TotalEntry.setStatus("mandatory")


class _WfDs3TotalIndex_Type(Integer32):
    """Custom type wfDs3TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3TotalIndex_Type.__name__ = "Integer32"
_WfDs3TotalIndex_Object = MibTableColumn
wfDs3TotalIndex = _WfDs3TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 1),
    _WfDs3TotalIndex_Type()
)
wfDs3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalIndex.setStatus("mandatory")
_WfDs3TotalESs_Type = Gauge32
_WfDs3TotalESs_Object = MibTableColumn
wfDs3TotalESs = _WfDs3TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 2),
    _WfDs3TotalESs_Type()
)
wfDs3TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalESs.setStatus("mandatory")
_WfDs3TotalSESs_Type = Gauge32
_WfDs3TotalSESs_Object = MibTableColumn
wfDs3TotalSESs = _WfDs3TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 3),
    _WfDs3TotalSESs_Type()
)
wfDs3TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalSESs.setStatus("mandatory")
_WfDs3TotalSEFs_Type = Gauge32
_WfDs3TotalSEFs_Object = MibTableColumn
wfDs3TotalSEFs = _WfDs3TotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 4),
    _WfDs3TotalSEFs_Type()
)
wfDs3TotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalSEFs.setStatus("mandatory")
_WfDs3TotalUASs_Type = Gauge32
_WfDs3TotalUASs_Object = MibTableColumn
wfDs3TotalUASs = _WfDs3TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 5),
    _WfDs3TotalUASs_Type()
)
wfDs3TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalUASs.setStatus("mandatory")
_WfDs3TotalBPVs_Type = Gauge32
_WfDs3TotalBPVs_Object = MibTableColumn
wfDs3TotalBPVs = _WfDs3TotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 6),
    _WfDs3TotalBPVs_Type()
)
wfDs3TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalBPVs.setStatus("mandatory")
_WfDs3TotalCVs_Type = Gauge32
_WfDs3TotalCVs_Object = MibTableColumn
wfDs3TotalCVs = _WfDs3TotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 7),
    _WfDs3TotalCVs_Type()
)
wfDs3TotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalCVs.setStatus("mandatory")
_WfDs3FeConfig_Object = MibTable
wfDs3FeConfig = _WfDs3FeConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5)
)
if mibBuilder.loadTexts:
    wfDs3FeConfig.setStatus("mandatory")
_WfDs3FeConfigEntry_Object = MibTableRow
wfDs3FeConfigEntry = _WfDs3FeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1)
)
wfDs3FeConfigEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3FeConfigIndex"),
)
if mibBuilder.loadTexts:
    wfDs3FeConfigEntry.setStatus("mandatory")


class _WfDs3FeConfigIndex_Type(Integer32):
    """Custom type wfDs3FeConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3FeConfigIndex_Type.__name__ = "Integer32"
_WfDs3FeConfigIndex_Object = MibTableColumn
wfDs3FeConfigIndex = _WfDs3FeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 1),
    _WfDs3FeConfigIndex_Type()
)
wfDs3FeConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeConfigIndex.setStatus("mandatory")
_WfDs3FarEndEquipCode_Type = DisplayString
_WfDs3FarEndEquipCode_Object = MibTableColumn
wfDs3FarEndEquipCode = _WfDs3FarEndEquipCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 2),
    _WfDs3FarEndEquipCode_Type()
)
wfDs3FarEndEquipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndEquipCode.setStatus("mandatory")
_WfDs3FarEndLocationIDCode_Type = DisplayString
_WfDs3FarEndLocationIDCode_Object = MibTableColumn
wfDs3FarEndLocationIDCode = _WfDs3FarEndLocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 3),
    _WfDs3FarEndLocationIDCode_Type()
)
wfDs3FarEndLocationIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndLocationIDCode.setStatus("mandatory")
_WfDs3FarEndFrameIDCode_Type = DisplayString
_WfDs3FarEndFrameIDCode_Object = MibTableColumn
wfDs3FarEndFrameIDCode = _WfDs3FarEndFrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 4),
    _WfDs3FarEndFrameIDCode_Type()
)
wfDs3FarEndFrameIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndFrameIDCode.setStatus("mandatory")
_WfDs3FarEndUnitCode_Type = DisplayString
_WfDs3FarEndUnitCode_Object = MibTableColumn
wfDs3FarEndUnitCode = _WfDs3FarEndUnitCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 5),
    _WfDs3FarEndUnitCode_Type()
)
wfDs3FarEndUnitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndUnitCode.setStatus("mandatory")
_WfDs3FarEndFacilityIDCode_Type = DisplayString
_WfDs3FarEndFacilityIDCode_Object = MibTableColumn
wfDs3FarEndFacilityIDCode = _WfDs3FarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 6),
    _WfDs3FarEndFacilityIDCode_Type()
)
wfDs3FarEndFacilityIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndFacilityIDCode.setStatus("mandatory")
_WfDs3FeCurrent_Object = MibTable
wfDs3FeCurrent = _WfDs3FeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6)
)
if mibBuilder.loadTexts:
    wfDs3FeCurrent.setStatus("mandatory")
_WfDs3FeCurrentEntry_Object = MibTableRow
wfDs3FeCurrentEntry = _WfDs3FeCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1)
)
wfDs3FeCurrentEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3FeCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs3FeCurrentEntry.setStatus("mandatory")


class _WfDs3FeCurrentIndex_Type(Integer32):
    """Custom type wfDs3FeCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3FeCurrentIndex_Type.__name__ = "Integer32"
_WfDs3FeCurrentIndex_Object = MibTableColumn
wfDs3FeCurrentIndex = _WfDs3FeCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 1),
    _WfDs3FeCurrentIndex_Type()
)
wfDs3FeCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentIndex.setStatus("mandatory")
_WfDs3FeCurrentESs_Type = Counter32
_WfDs3FeCurrentESs_Object = MibTableColumn
wfDs3FeCurrentESs = _WfDs3FeCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 2),
    _WfDs3FeCurrentESs_Type()
)
wfDs3FeCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentESs.setStatus("mandatory")
_WfDs3FeCurrentSESs_Type = Counter32
_WfDs3FeCurrentSESs_Object = MibTableColumn
wfDs3FeCurrentSESs = _WfDs3FeCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 3),
    _WfDs3FeCurrentSESs_Type()
)
wfDs3FeCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentSESs.setStatus("mandatory")
_WfDs3FeCurrentCVs_Type = Counter32
_WfDs3FeCurrentCVs_Object = MibTableColumn
wfDs3FeCurrentCVs = _WfDs3FeCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 4),
    _WfDs3FeCurrentCVs_Type()
)
wfDs3FeCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentCVs.setStatus("mandatory")
_WfDs3FeInterval_Object = MibTable
wfDs3FeInterval = _WfDs3FeInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7)
)
if mibBuilder.loadTexts:
    wfDs3FeInterval.setStatus("mandatory")
_WfDs3FeIntervalEntry_Object = MibTableRow
wfDs3FeIntervalEntry = _WfDs3FeIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1)
)
wfDs3FeIntervalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3FeIntervalIndex"),
    (0, "Wellfleet-Series7-MIB", "wfDs3FeIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs3FeIntervalEntry.setStatus("mandatory")


class _WfDs3FeIntervalIndex_Type(Integer32):
    """Custom type wfDs3FeIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3FeIntervalIndex_Type.__name__ = "Integer32"
_WfDs3FeIntervalIndex_Object = MibTableColumn
wfDs3FeIntervalIndex = _WfDs3FeIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 1),
    _WfDs3FeIntervalIndex_Type()
)
wfDs3FeIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalIndex.setStatus("mandatory")


class _WfDs3FeIntervalNumber_Type(Integer32):
    """Custom type wfDs3FeIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              96)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 96),
          ("minimum", 1))
    )


_WfDs3FeIntervalNumber_Type.__name__ = "Integer32"
_WfDs3FeIntervalNumber_Object = MibTableColumn
wfDs3FeIntervalNumber = _WfDs3FeIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 2),
    _WfDs3FeIntervalNumber_Type()
)
wfDs3FeIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalNumber.setStatus("mandatory")
_WfDs3FeIntervalESs_Type = Gauge32
_WfDs3FeIntervalESs_Object = MibTableColumn
wfDs3FeIntervalESs = _WfDs3FeIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 3),
    _WfDs3FeIntervalESs_Type()
)
wfDs3FeIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalESs.setStatus("mandatory")
_WfDs3FeIntervalSESs_Type = Gauge32
_WfDs3FeIntervalSESs_Object = MibTableColumn
wfDs3FeIntervalSESs = _WfDs3FeIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 4),
    _WfDs3FeIntervalSESs_Type()
)
wfDs3FeIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalSESs.setStatus("mandatory")
_WfDs3FeIntervalCVs_Type = Gauge32
_WfDs3FeIntervalCVs_Object = MibTableColumn
wfDs3FeIntervalCVs = _WfDs3FeIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 5),
    _WfDs3FeIntervalCVs_Type()
)
wfDs3FeIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalCVs.setStatus("mandatory")
_WfDs3FeTotal_Object = MibTable
wfDs3FeTotal = _WfDs3FeTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8)
)
if mibBuilder.loadTexts:
    wfDs3FeTotal.setStatus("mandatory")
_WfDs3FeTotalEntry_Object = MibTableRow
wfDs3FeTotalEntry = _WfDs3FeTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1)
)
wfDs3FeTotalEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfDs3FeTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs3FeTotalEntry.setStatus("mandatory")


class _WfDs3FeTotalIndex_Type(Integer32):
    """Custom type wfDs3FeTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfDs3FeTotalIndex_Type.__name__ = "Integer32"
_WfDs3FeTotalIndex_Object = MibTableColumn
wfDs3FeTotalIndex = _WfDs3FeTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 1),
    _WfDs3FeTotalIndex_Type()
)
wfDs3FeTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalIndex.setStatus("mandatory")
_WfDs3FeTotalESs_Type = Gauge32
_WfDs3FeTotalESs_Object = MibTableColumn
wfDs3FeTotalESs = _WfDs3FeTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 2),
    _WfDs3FeTotalESs_Type()
)
wfDs3FeTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalESs.setStatus("mandatory")
_WfDs3FeTotalSESs_Type = Gauge32
_WfDs3FeTotalSESs_Object = MibTableColumn
wfDs3FeTotalSESs = _WfDs3FeTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 3),
    _WfDs3FeTotalSESs_Type()
)
wfDs3FeTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalSESs.setStatus("mandatory")
_WfDs3FeTotalCVs_Type = Gauge32
_WfDs3FeTotalCVs_Object = MibTableColumn
wfDs3FeTotalCVs = _WfDs3FeTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 4),
    _WfDs3FeTotalCVs_Type()
)
wfDs3FeTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalCVs.setStatus("mandatory")
_WfSipGroup_ObjectIdentity = ObjectIdentity
wfSipGroup = _WfSipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14)
)
_WfSipL2_Object = MibTable
wfSipL2 = _WfSipL2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1)
)
if mibBuilder.loadTexts:
    wfSipL2.setStatus("mandatory")
_WfSipL2Entry_Object = MibTableRow
wfSipL2Entry = _WfSipL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1)
)
wfSipL2Entry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSipL2Index"),
)
if mibBuilder.loadTexts:
    wfSipL2Entry.setStatus("mandatory")


class _WfSipL2Index_Type(Integer32):
    """Custom type wfSipL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfSipL2Index_Type.__name__ = "Integer32"
_WfSipL2Index_Object = MibTableColumn
wfSipL2Index = _WfSipL2Index_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 1),
    _WfSipL2Index_Type()
)
wfSipL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2Index.setStatus("mandatory")
_WfSipL2ReceivedCounts_Type = Counter32
_WfSipL2ReceivedCounts_Object = MibTableColumn
wfSipL2ReceivedCounts = _WfSipL2ReceivedCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 2),
    _WfSipL2ReceivedCounts_Type()
)
wfSipL2ReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2ReceivedCounts.setStatus("mandatory")
_WfSipL2SentCounts_Type = Counter32
_WfSipL2SentCounts_Object = MibTableColumn
wfSipL2SentCounts = _WfSipL2SentCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 3),
    _WfSipL2SentCounts_Type()
)
wfSipL2SentCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2SentCounts.setStatus("mandatory")
_WfSipHcsOrCRCErrors_Type = Counter32
_WfSipHcsOrCRCErrors_Object = MibTableColumn
wfSipHcsOrCRCErrors = _WfSipHcsOrCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 4),
    _WfSipHcsOrCRCErrors_Type()
)
wfSipHcsOrCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipHcsOrCRCErrors.setStatus("mandatory")
_WfSipL2PayloadLengthErrors_Type = Counter32
_WfSipL2PayloadLengthErrors_Object = MibTableColumn
wfSipL2PayloadLengthErrors = _WfSipL2PayloadLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 5),
    _WfSipL2PayloadLengthErrors_Type()
)
wfSipL2PayloadLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2PayloadLengthErrors.setStatus("mandatory")
_WfSipL2SequenceNumberErrors_Type = Counter32
_WfSipL2SequenceNumberErrors_Object = MibTableColumn
wfSipL2SequenceNumberErrors = _WfSipL2SequenceNumberErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 6),
    _WfSipL2SequenceNumberErrors_Type()
)
wfSipL2SequenceNumberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2SequenceNumberErrors.setStatus("mandatory")
_WfSipL2MidCurrentlyActiveErrors_Type = Counter32
_WfSipL2MidCurrentlyActiveErrors_Object = MibTableColumn
wfSipL2MidCurrentlyActiveErrors = _WfSipL2MidCurrentlyActiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 7),
    _WfSipL2MidCurrentlyActiveErrors_Type()
)
wfSipL2MidCurrentlyActiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2MidCurrentlyActiveErrors.setStatus("mandatory")
_WfSipL2BomOrSSMsMIDErrors_Type = Counter32
_WfSipL2BomOrSSMsMIDErrors_Object = MibTableColumn
wfSipL2BomOrSSMsMIDErrors = _WfSipL2BomOrSSMsMIDErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 8),
    _WfSipL2BomOrSSMsMIDErrors_Type()
)
wfSipL2BomOrSSMsMIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2BomOrSSMsMIDErrors.setStatus("mandatory")
_WfSipL2EomsMIDErrors_Type = Counter32
_WfSipL2EomsMIDErrors_Object = MibTableColumn
wfSipL2EomsMIDErrors = _WfSipL2EomsMIDErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 9),
    _WfSipL2EomsMIDErrors_Type()
)
wfSipL2EomsMIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipL2EomsMIDErrors.setStatus("mandatory")
_WfSipPlcpGroup_ObjectIdentity = ObjectIdentity
wfSipPlcpGroup = _WfSipPlcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2)
)
_WfSipDs1Plcp_Object = MibTable
wfSipDs1Plcp = _WfSipDs1Plcp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1)
)
if mibBuilder.loadTexts:
    wfSipDs1Plcp.setStatus("mandatory")
_WfSipDs1PlcpEntry_Object = MibTableRow
wfSipDs1PlcpEntry = _WfSipDs1PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1)
)
wfSipDs1PlcpEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSipDs1PlcpIndex"),
)
if mibBuilder.loadTexts:
    wfSipDs1PlcpEntry.setStatus("mandatory")


class _WfSipDs1PlcpIndex_Type(Integer32):
    """Custom type wfSipDs1PlcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfSipDs1PlcpIndex_Type.__name__ = "Integer32"
_WfSipDs1PlcpIndex_Object = MibTableColumn
wfSipDs1PlcpIndex = _WfSipDs1PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 1),
    _WfSipDs1PlcpIndex_Type()
)
wfSipDs1PlcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpIndex.setStatus("mandatory")
_WfSipDs1PlcpSEFs_Type = Counter32
_WfSipDs1PlcpSEFs_Object = MibTableColumn
wfSipDs1PlcpSEFs = _WfSipDs1PlcpSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 2),
    _WfSipDs1PlcpSEFs_Type()
)
wfSipDs1PlcpSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpSEFs.setStatus("mandatory")


class _WfSipDs1PlcpAlarmState_Type(Integer32):
    """Custom type wfSipDs1PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incominglof", 3),
          ("noalarm", 1),
          ("receivedfarendalarm", 2))
    )


_WfSipDs1PlcpAlarmState_Type.__name__ = "Integer32"
_WfSipDs1PlcpAlarmState_Object = MibTableColumn
wfSipDs1PlcpAlarmState = _WfSipDs1PlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 3),
    _WfSipDs1PlcpAlarmState_Type()
)
wfSipDs1PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpAlarmState.setStatus("mandatory")
_WfSipDs1PlcpUASs_Type = Counter32
_WfSipDs1PlcpUASs_Object = MibTableColumn
wfSipDs1PlcpUASs = _WfSipDs1PlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 4),
    _WfSipDs1PlcpUASs_Type()
)
wfSipDs1PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs1PlcpUASs.setStatus("mandatory")
_WfSipDs3Plcp_Object = MibTable
wfSipDs3Plcp = _WfSipDs3Plcp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2)
)
if mibBuilder.loadTexts:
    wfSipDs3Plcp.setStatus("mandatory")
_WfSipDs3PlcpEntry_Object = MibTableRow
wfSipDs3PlcpEntry = _WfSipDs3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1)
)
wfSipDs3PlcpEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSipDs3PlcpIndex"),
)
if mibBuilder.loadTexts:
    wfSipDs3PlcpEntry.setStatus("mandatory")


class _WfSipDs3PlcpIndex_Type(Integer32):
    """Custom type wfSipDs3PlcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1024),
          ("minimum", 1))
    )


_WfSipDs3PlcpIndex_Type.__name__ = "Integer32"
_WfSipDs3PlcpIndex_Object = MibTableColumn
wfSipDs3PlcpIndex = _WfSipDs3PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 1),
    _WfSipDs3PlcpIndex_Type()
)
wfSipDs3PlcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpIndex.setStatus("mandatory")
_WfSipDs3PlcpSEFs_Type = Counter32
_WfSipDs3PlcpSEFs_Object = MibTableColumn
wfSipDs3PlcpSEFs = _WfSipDs3PlcpSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 2),
    _WfSipDs3PlcpSEFs_Type()
)
wfSipDs3PlcpSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpSEFs.setStatus("mandatory")


class _WfSipDs3PlcpAlarmState_Type(Integer32):
    """Custom type wfSipDs3PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incominglof", 3),
          ("noalarm", 1),
          ("receivedfarendalarm", 2))
    )


_WfSipDs3PlcpAlarmState_Type.__name__ = "Integer32"
_WfSipDs3PlcpAlarmState_Object = MibTableColumn
wfSipDs3PlcpAlarmState = _WfSipDs3PlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 3),
    _WfSipDs3PlcpAlarmState_Type()
)
wfSipDs3PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpAlarmState.setStatus("mandatory")
_WfSipDs3PlcpUASs_Type = Counter32
_WfSipDs3PlcpUASs_Object = MibTableColumn
wfSipDs3PlcpUASs = _WfSipDs3PlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 4),
    _WfSipDs3PlcpUASs_Type()
)
wfSipDs3PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSipDs3PlcpUASs.setStatus("mandatory")
_WfFddiGroup_ObjectIdentity = ObjectIdentity
wfFddiGroup = _WfFddiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15)
)
_WfFddiSmtGroup_ObjectIdentity = ObjectIdentity
wfFddiSmtGroup = _WfFddiSmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1)
)
_WfFddiSmtTable_Object = MibTable
wfFddiSmtTable = _WfFddiSmtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2)
)
if mibBuilder.loadTexts:
    wfFddiSmtTable.setStatus("mandatory")
_WfFddiSmtEntry_Object = MibTableRow
wfFddiSmtEntry = _WfFddiSmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1)
)
wfFddiSmtEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfFddiSmtSlot"),
    (0, "Wellfleet-Series7-MIB", "wfFddiSmtNode"),
)
if mibBuilder.loadTexts:
    wfFddiSmtEntry.setStatus("mandatory")
_WfFddiSmtSlot_Type = Integer32
_WfFddiSmtSlot_Object = MibTableColumn
wfFddiSmtSlot = _WfFddiSmtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 1),
    _WfFddiSmtSlot_Type()
)
wfFddiSmtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtSlot.setStatus("mandatory")
_WfFddiSmtNode_Type = Integer32
_WfFddiSmtNode_Object = MibTableColumn
wfFddiSmtNode = _WfFddiSmtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 2),
    _WfFddiSmtNode_Type()
)
wfFddiSmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtNode.setStatus("mandatory")
_WfFddiSmtCct_Type = Integer32
_WfFddiSmtCct_Object = MibTableColumn
wfFddiSmtCct = _WfFddiSmtCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 3),
    _WfFddiSmtCct_Type()
)
wfFddiSmtCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtCct.setStatus("mandatory")
_WfFddiSmtStationId_Type = OctetString
_WfFddiSmtStationId_Object = MibTableColumn
wfFddiSmtStationId = _WfFddiSmtStationId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 4),
    _WfFddiSmtStationId_Type()
)
wfFddiSmtStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtStationId.setStatus("mandatory")
_WfFddiSmtOpVersionId_Type = Integer32
_WfFddiSmtOpVersionId_Object = MibTableColumn
wfFddiSmtOpVersionId = _WfFddiSmtOpVersionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 5),
    _WfFddiSmtOpVersionId_Type()
)
wfFddiSmtOpVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtOpVersionId.setStatus("mandatory")
_WfFddiSmtMacCt_Type = Integer32
_WfFddiSmtMacCt_Object = MibTableColumn
wfFddiSmtMacCt = _WfFddiSmtMacCt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 6),
    _WfFddiSmtMacCt_Type()
)
wfFddiSmtMacCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtMacCt.setStatus("mandatory")
_WfFddiSmtNonMasterCt_Type = Integer32
_WfFddiSmtNonMasterCt_Object = MibTableColumn
wfFddiSmtNonMasterCt = _WfFddiSmtNonMasterCt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 7),
    _WfFddiSmtNonMasterCt_Type()
)
wfFddiSmtNonMasterCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtNonMasterCt.setStatus("mandatory")


class _WfFddiSmtEcmState_Type(Integer32):
    """Custom type wfFddiSmtEcmState based on Integer32"""
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
        *(("check", 7),
          ("deinsert", 8),
          ("in", 2),
          ("insert", 6),
          ("leave", 4),
          ("out", 1),
          ("pathtest", 5),
          ("trace", 3))
    )


_WfFddiSmtEcmState_Type.__name__ = "Integer32"
_WfFddiSmtEcmState_Object = MibTableColumn
wfFddiSmtEcmState = _WfFddiSmtEcmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 8),
    _WfFddiSmtEcmState_Type()
)
wfFddiSmtEcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtEcmState.setStatus("mandatory")


class _WfFddiSmtCfState_Type(Integer32):
    """Custom type wfFddiSmtCfState based on Integer32"""
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
        *(("isolated", 1),
          ("thru", 6),
          ("wrapa", 3),
          ("wrapab", 5),
          ("wrapb", 4),
          ("wraps", 2))
    )


_WfFddiSmtCfState_Type.__name__ = "Integer32"
_WfFddiSmtCfState_Object = MibTableColumn
wfFddiSmtCfState = _WfFddiSmtCfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 9),
    _WfFddiSmtCfState_Type()
)
wfFddiSmtCfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtCfState.setStatus("mandatory")
_WfFddiMacGroup_ObjectIdentity = ObjectIdentity
wfFddiMacGroup = _WfFddiMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2)
)
_WfFddiMacTable_Object = MibTable
wfFddiMacTable = _WfFddiMacTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2)
)
if mibBuilder.loadTexts:
    wfFddiMacTable.setStatus("mandatory")
_WfFddiMacEntry_Object = MibTableRow
wfFddiMacEntry = _WfFddiMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1)
)
wfFddiMacEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfFddiMacSlot"),
    (0, "Wellfleet-Series7-MIB", "wfFddiMacNode"),
)
if mibBuilder.loadTexts:
    wfFddiMacEntry.setStatus("mandatory")
_WfFddiMacSlot_Type = Integer32
_WfFddiMacSlot_Object = MibTableColumn
wfFddiMacSlot = _WfFddiMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 1),
    _WfFddiMacSlot_Type()
)
wfFddiMacSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacSlot.setStatus("mandatory")
_WfFddiMacNode_Type = Integer32
_WfFddiMacNode_Object = MibTableColumn
wfFddiMacNode = _WfFddiMacNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 2),
    _WfFddiMacNode_Type()
)
wfFddiMacNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacNode.setStatus("mandatory")
_WfFddiMacCct_Type = Integer32
_WfFddiMacCct_Object = MibTableColumn
wfFddiMacCct = _WfFddiMacCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 3),
    _WfFddiMacCct_Type()
)
wfFddiMacCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacCct.setStatus("mandatory")
_WfFddiMacUpstreamNbr_Type = OctetString
_WfFddiMacUpstreamNbr_Object = MibTableColumn
wfFddiMacUpstreamNbr = _WfFddiMacUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 4),
    _WfFddiMacUpstreamNbr_Type()
)
wfFddiMacUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacUpstreamNbr.setStatus("mandatory")
_WfFddiMacDownstreamNbr_Type = OctetString
_WfFddiMacDownstreamNbr_Object = MibTableColumn
wfFddiMacDownstreamNbr = _WfFddiMacDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 5),
    _WfFddiMacDownstreamNbr_Type()
)
wfFddiMacDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacDownstreamNbr.setStatus("mandatory")
_WfFddiMacSmtAddress_Type = OctetString
_WfFddiMacSmtAddress_Object = MibTableColumn
wfFddiMacSmtAddress = _WfFddiMacSmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 6),
    _WfFddiMacSmtAddress_Type()
)
wfFddiMacSmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacSmtAddress.setStatus("mandatory")
_WfFddiMacTNeg_Type = Integer32
_WfFddiMacTNeg_Object = MibTableColumn
wfFddiMacTNeg = _WfFddiMacTNeg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 7),
    _WfFddiMacTNeg_Type()
)
wfFddiMacTNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacTNeg.setStatus("mandatory")


class _WfFddiMacRmtState_Type(Integer32):
    """Custom type wfFddiMacRmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("detect", 8),
          ("directed", 64),
          ("isolated", 1),
          ("nonop", 2),
          ("nonopdup", 16),
          ("ringop", 4),
          ("ringopdup", 32),
          ("trace", 128))
    )


_WfFddiMacRmtState_Type.__name__ = "Integer32"
_WfFddiMacRmtState_Object = MibTableColumn
wfFddiMacRmtState = _WfFddiMacRmtState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 8),
    _WfFddiMacRmtState_Type()
)
wfFddiMacRmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacRmtState.setStatus("mandatory")
_WfFddiPathGroup_ObjectIdentity = ObjectIdentity
wfFddiPathGroup = _WfFddiPathGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3)
)
_WfFddiPortGroup_ObjectIdentity = ObjectIdentity
wfFddiPortGroup = _WfFddiPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4)
)
_WfFddiPortTable_Object = MibTable
wfFddiPortTable = _WfFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2)
)
if mibBuilder.loadTexts:
    wfFddiPortTable.setStatus("mandatory")
_WfFddiPortEntry_Object = MibTableRow
wfFddiPortEntry = _WfFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1)
)
wfFddiPortEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfFddiPortSlot"),
    (0, "Wellfleet-Series7-MIB", "wfFddiPortNode"),
    (0, "Wellfleet-Series7-MIB", "wfFddiPortIndex"),
)
if mibBuilder.loadTexts:
    wfFddiPortEntry.setStatus("mandatory")
_WfFddiPortSlot_Type = Integer32
_WfFddiPortSlot_Object = MibTableColumn
wfFddiPortSlot = _WfFddiPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 1),
    _WfFddiPortSlot_Type()
)
wfFddiPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortSlot.setStatus("mandatory")
_WfFddiPortNode_Type = Integer32
_WfFddiPortNode_Object = MibTableColumn
wfFddiPortNode = _WfFddiPortNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 2),
    _WfFddiPortNode_Type()
)
wfFddiPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortNode.setStatus("mandatory")
_WfFddiPortCct_Type = Integer32
_WfFddiPortCct_Object = MibTableColumn
wfFddiPortCct = _WfFddiPortCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 3),
    _WfFddiPortCct_Type()
)
wfFddiPortCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortCct.setStatus("mandatory")
_WfFddiPortIndex_Type = Integer32
_WfFddiPortIndex_Object = MibTableColumn
wfFddiPortIndex = _WfFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 4),
    _WfFddiPortIndex_Type()
)
wfFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortIndex.setStatus("mandatory")


class _WfFddiPortPcType_Type(Integer32):
    """Custom type wfFddiPortPcType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("s", 3))
    )


_WfFddiPortPcType_Type.__name__ = "Integer32"
_WfFddiPortPcType_Object = MibTableColumn
wfFddiPortPcType = _WfFddiPortPcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 5),
    _WfFddiPortPcType_Type()
)
wfFddiPortPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcType.setStatus("mandatory")


class _WfFddiPortPcNeighbor_Type(Integer32):
    """Custom type wfFddiPortPcNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("s", 3),
          ("unknown", 5))
    )


_WfFddiPortPcNeighbor_Type.__name__ = "Integer32"
_WfFddiPortPcNeighbor_Object = MibTableColumn
wfFddiPortPcNeighbor = _WfFddiPortPcNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 6),
    _WfFddiPortPcNeighbor_Type()
)
wfFddiPortPcNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcNeighbor.setStatus("mandatory")


class _WfFddiPortPcmState_Type(Integer32):
    """Custom type wfFddiPortPcmState based on Integer32"""
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
        *(("active", 9),
          ("break", 2),
          ("connect", 4),
          ("join", 7),
          ("maint", 10),
          ("next", 5),
          ("off", 1),
          ("signal", 6),
          ("trace", 3),
          ("verify", 8))
    )


_WfFddiPortPcmState_Type.__name__ = "Integer32"
_WfFddiPortPcmState_Object = MibTableColumn
wfFddiPortPcmState = _WfFddiPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 7),
    _WfFddiPortPcmState_Type()
)
wfFddiPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcmState.setStatus("mandatory")
_WfApplication_ObjectIdentity = ObjectIdentity
wfApplication = _WfApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5)
)
_WfDataLink_ObjectIdentity = ObjectIdentity
wfDataLink = _WfDataLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1)
)
_WfBridgeGroup_ObjectIdentity = ObjectIdentity
wfBridgeGroup = _WfBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1)
)
_WfBrLearning_ObjectIdentity = ObjectIdentity
wfBrLearning = _WfBrLearning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1)
)
_WfBrTp_ObjectIdentity = ObjectIdentity
wfBrTp = _WfBrTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1)
)


class _WfBrTpBaseDelete_Type(Integer32):
    """Custom type wfBrTpBaseDelete based on Integer32"""
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


_WfBrTpBaseDelete_Type.__name__ = "Integer32"
_WfBrTpBaseDelete_Object = MibScalar
wfBrTpBaseDelete = _WfBrTpBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 1),
    _WfBrTpBaseDelete_Type()
)
wfBrTpBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseDelete.setStatus("mandatory")


class _WfBrTpBaseEnable_Type(Integer32):
    """Custom type wfBrTpBaseEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrTpBaseEnable_Type.__name__ = "Integer32"
_WfBrTpBaseEnable_Object = MibScalar
wfBrTpBaseEnable = _WfBrTpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 2),
    _WfBrTpBaseEnable_Type()
)
wfBrTpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseEnable.setStatus("mandatory")


class _WfBrTpBaseState_Type(Integer32):
    """Custom type wfBrTpBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("pres", 4),
          ("up", 1))
    )


_WfBrTpBaseState_Type.__name__ = "Integer32"
_WfBrTpBaseState_Object = MibScalar
wfBrTpBaseState = _WfBrTpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 3),
    _WfBrTpBaseState_Type()
)
wfBrTpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseState.setStatus("mandatory")
_WfBrTpFdbTable_Object = MibTable
wfBrTpFdbTable = _WfBrTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wfBrTpFdbTable.setStatus("mandatory")
_WfBrTpFdbEntry_Object = MibTableRow
wfBrTpFdbEntry = _WfBrTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1)
)
wfBrTpFdbEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrTpBaseFdbAddress"),
)
if mibBuilder.loadTexts:
    wfBrTpFdbEntry.setStatus("mandatory")
_WfBrTpBaseFdbAddress_Type = OctetString
_WfBrTpBaseFdbAddress_Object = MibTableColumn
wfBrTpBaseFdbAddress = _WfBrTpBaseFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1, 1),
    _WfBrTpBaseFdbAddress_Type()
)
wfBrTpBaseFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFdbAddress.setStatus("mandatory")
_WfBrTpBaseFdbPort_Type = Integer32
_WfBrTpBaseFdbPort_Object = MibTableColumn
wfBrTpBaseFdbPort = _WfBrTpBaseFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1, 2),
    _WfBrTpBaseFdbPort_Type()
)
wfBrTpBaseFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFdbPort.setStatus("mandatory")


class _WfBrTpBaseFdbStatus_Type(Integer32):
    """Custom type wfBrTpBaseFdbStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_WfBrTpBaseFdbStatus_Type.__name__ = "Integer32"
_WfBrTpBaseFdbStatus_Object = MibTableColumn
wfBrTpBaseFdbStatus = _WfBrTpBaseFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1, 3),
    _WfBrTpBaseFdbStatus_Type()
)
wfBrTpBaseFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFdbStatus.setStatus("mandatory")
_WfBrSourceRouting_ObjectIdentity = ObjectIdentity
wfBrSourceRouting = _WfBrSourceRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2)
)
_WfBrSr_ObjectIdentity = ObjectIdentity
wfBrSr = _WfBrSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1)
)


class _WfBrSrBaseDelete_Type(Integer32):
    """Custom type wfBrSrBaseDelete based on Integer32"""
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


_WfBrSrBaseDelete_Type.__name__ = "Integer32"
_WfBrSrBaseDelete_Object = MibScalar
wfBrSrBaseDelete = _WfBrSrBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 1),
    _WfBrSrBaseDelete_Type()
)
wfBrSrBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseDelete.setStatus("mandatory")


class _WfBrSrBaseDisable_Type(Integer32):
    """Custom type wfBrSrBaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrSrBaseDisable_Type.__name__ = "Integer32"
_WfBrSrBaseDisable_Object = MibScalar
wfBrSrBaseDisable = _WfBrSrBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 2),
    _WfBrSrBaseDisable_Type()
)
wfBrSrBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseDisable.setStatus("mandatory")


class _WfBrSrBaseState_Type(Integer32):
    """Custom type wfBrSrBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBrSrBaseState_Type.__name__ = "Integer32"
_WfBrSrBaseState_Object = MibScalar
wfBrSrBaseState = _WfBrSrBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 3),
    _WfBrSrBaseState_Type()
)
wfBrSrBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseState.setStatus("mandatory")
_WfBrSrBaseInternalLanId_Type = Integer32
_WfBrSrBaseInternalLanId_Object = MibScalar
wfBrSrBaseInternalLanId = _WfBrSrBaseInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 4),
    _WfBrSrBaseInternalLanId_Type()
)
wfBrSrBaseInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseInternalLanId.setStatus("mandatory")
_WfBrSrBaseBridgeId_Type = Integer32
_WfBrSrBaseBridgeId_Object = MibScalar
wfBrSrBaseBridgeId = _WfBrSrBaseBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 5),
    _WfBrSrBaseBridgeId_Type()
)
wfBrSrBaseBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseBridgeId.setStatus("mandatory")


class _WfBrSrBaseGroupLanId_Type(Integer32):
    """Custom type wfBrSrBaseGroupLanId based on Integer32"""
    defaultValue = 4095


_WfBrSrBaseGroupLanId_Object = MibScalar
wfBrSrBaseGroupLanId = _WfBrSrBaseGroupLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 6),
    _WfBrSrBaseGroupLanId_Type()
)
wfBrSrBaseGroupLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseGroupLanId.setStatus("mandatory")


class _WfBrSrBaseIpEncapsDisable_Type(Integer32):
    """Custom type wfBrSrBaseIpEncapsDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrSrBaseIpEncapsDisable_Type.__name__ = "Integer32"
_WfBrSrBaseIpEncapsDisable_Object = MibScalar
wfBrSrBaseIpEncapsDisable = _WfBrSrBaseIpEncapsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 7),
    _WfBrSrBaseIpEncapsDisable_Type()
)
wfBrSrBaseIpEncapsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseIpEncapsDisable.setStatus("mandatory")
_WfBrSrBaseIpNetworkRingId_Type = Integer32
_WfBrSrBaseIpNetworkRingId_Object = MibScalar
wfBrSrBaseIpNetworkRingId = _WfBrSrBaseIpNetworkRingId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 8),
    _WfBrSrBaseIpNetworkRingId_Type()
)
wfBrSrBaseIpNetworkRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseIpNetworkRingId.setStatus("mandatory")
_WfBrSrBaseIpInReceives_Type = Counter32
_WfBrSrBaseIpInReceives_Object = MibScalar
wfBrSrBaseIpInReceives = _WfBrSrBaseIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 9),
    _WfBrSrBaseIpInReceives_Type()
)
wfBrSrBaseIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseIpInReceives.setStatus("mandatory")
_WfBrSrBaseIpSeqErrors_Type = Counter32
_WfBrSrBaseIpSeqErrors_Object = MibScalar
wfBrSrBaseIpSeqErrors = _WfBrSrBaseIpSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 10),
    _WfBrSrBaseIpSeqErrors_Type()
)
wfBrSrBaseIpSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseIpSeqErrors.setStatus("mandatory")


class _WfBrSrBaseIpMtuSize_Type(Integer32):
    """Custom type wfBrSrBaseIpMtuSize based on Integer32"""
    defaultValue = 4562


_WfBrSrBaseIpMtuSize_Object = MibScalar
wfBrSrBaseIpMtuSize = _WfBrSrBaseIpMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 11),
    _WfBrSrBaseIpMtuSize_Type()
)
wfBrSrBaseIpMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseIpMtuSize.setStatus("mandatory")
_WfBrSrInterfaceTable_Object = MibTable
wfBrSrInterfaceTable = _WfBrSrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfBrSrInterfaceTable.setStatus("mandatory")
_WfBrSrInterfaceEntry_Object = MibTableRow
wfBrSrInterfaceEntry = _WfBrSrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1)
)
wfBrSrInterfaceEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrSrInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfBrSrInterfaceEntry.setStatus("mandatory")


class _WfBrSrInterfaceDelete_Type(Integer32):
    """Custom type wfBrSrInterfaceDelete based on Integer32"""
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


_WfBrSrInterfaceDelete_Type.__name__ = "Integer32"
_WfBrSrInterfaceDelete_Object = MibTableColumn
wfBrSrInterfaceDelete = _WfBrSrInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 1),
    _WfBrSrInterfaceDelete_Type()
)
wfBrSrInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDelete.setStatus("mandatory")


class _WfBrSrInterfaceDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrSrInterfaceDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceDisable_Object = MibTableColumn
wfBrSrInterfaceDisable = _WfBrSrInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 2),
    _WfBrSrInterfaceDisable_Type()
)
wfBrSrInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDisable.setStatus("mandatory")


class _WfBrSrInterfaceState_Type(Integer32):
    """Custom type wfBrSrInterfaceState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBrSrInterfaceState_Type.__name__ = "Integer32"
_WfBrSrInterfaceState_Object = MibTableColumn
wfBrSrInterfaceState = _WfBrSrInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 3),
    _WfBrSrInterfaceState_Type()
)
wfBrSrInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceState.setStatus("mandatory")
_WfBrSrInterfaceCircuit_Type = Integer32
_WfBrSrInterfaceCircuit_Object = MibTableColumn
wfBrSrInterfaceCircuit = _WfBrSrInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 4),
    _WfBrSrInterfaceCircuit_Type()
)
wfBrSrInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceCircuit.setStatus("mandatory")


class _WfBrSrInterfaceMaxRds_Type(Integer32):
    """Custom type wfBrSrInterfaceMaxRds based on Integer32"""
    defaultValue = 7


_WfBrSrInterfaceMaxRds_Object = MibTableColumn
wfBrSrInterfaceMaxRds = _WfBrSrInterfaceMaxRds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 5),
    _WfBrSrInterfaceMaxRds_Type()
)
wfBrSrInterfaceMaxRds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceMaxRds.setStatus("mandatory")
_WfBrSrInterfaceRing_Type = Integer32
_WfBrSrInterfaceRing_Object = MibTableColumn
wfBrSrInterfaceRing = _WfBrSrInterfaceRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 6),
    _WfBrSrInterfaceRing_Type()
)
wfBrSrInterfaceRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceRing.setStatus("mandatory")


class _WfBrSrInterfaceBlockOutSte_Type(Integer32):
    """Custom type wfBrSrInterfaceBlockOutSte based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("block", 1))
    )


_WfBrSrInterfaceBlockOutSte_Type.__name__ = "Integer32"
_WfBrSrInterfaceBlockOutSte_Object = MibTableColumn
wfBrSrInterfaceBlockOutSte = _WfBrSrInterfaceBlockOutSte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 7),
    _WfBrSrInterfaceBlockOutSte_Type()
)
wfBrSrInterfaceBlockOutSte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceBlockOutSte.setStatus("mandatory")


class _WfBrSrInterfaceBlockInSte_Type(Integer32):
    """Custom type wfBrSrInterfaceBlockInSte based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("block", 1))
    )


_WfBrSrInterfaceBlockInSte_Type.__name__ = "Integer32"
_WfBrSrInterfaceBlockInSte_Object = MibTableColumn
wfBrSrInterfaceBlockInSte = _WfBrSrInterfaceBlockInSte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 8),
    _WfBrSrInterfaceBlockInSte_Type()
)
wfBrSrInterfaceBlockInSte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceBlockInSte.setStatus("mandatory")


class _WfBrSrInterfaceBlockIp_Type(Integer32):
    """Custom type wfBrSrInterfaceBlockIp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("block", 1))
    )


_WfBrSrInterfaceBlockIp_Type.__name__ = "Integer32"
_WfBrSrInterfaceBlockIp_Object = MibTableColumn
wfBrSrInterfaceBlockIp = _WfBrSrInterfaceBlockIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 9),
    _WfBrSrInterfaceBlockIp_Type()
)
wfBrSrInterfaceBlockIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceBlockIp.setStatus("mandatory")
_WfBrSrInterfaceIpAddress_Type = IpAddress
_WfBrSrInterfaceIpAddress_Object = MibTableColumn
wfBrSrInterfaceIpAddress = _WfBrSrInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 10),
    _WfBrSrInterfaceIpAddress_Type()
)
wfBrSrInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceIpAddress.setStatus("mandatory")
_WfBrSrInterfaceInFrames_Type = Counter32
_WfBrSrInterfaceInFrames_Object = MibTableColumn
wfBrSrInterfaceInFrames = _WfBrSrInterfaceInFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 11),
    _WfBrSrInterfaceInFrames_Type()
)
wfBrSrInterfaceInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceInFrames.setStatus("mandatory")
_WfBrSrInterfaceOutFrames_Type = Counter32
_WfBrSrInterfaceOutFrames_Object = MibTableColumn
wfBrSrInterfaceOutFrames = _WfBrSrInterfaceOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 12),
    _WfBrSrInterfaceOutFrames_Type()
)
wfBrSrInterfaceOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceOutFrames.setStatus("mandatory")
_WfBrSrInterfaceOutIpFrames_Type = Counter32
_WfBrSrInterfaceOutIpFrames_Object = MibTableColumn
wfBrSrInterfaceOutIpFrames = _WfBrSrInterfaceOutIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 13),
    _WfBrSrInterfaceOutIpFrames_Type()
)
wfBrSrInterfaceOutIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceOutIpFrames.setStatus("mandatory")
_WfBrSrInterfaceDropInvalidRcs_Type = Counter32
_WfBrSrInterfaceDropInvalidRcs_Object = MibTableColumn
wfBrSrInterfaceDropInvalidRcs = _WfBrSrInterfaceDropInvalidRcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 14),
    _WfBrSrInterfaceDropInvalidRcs_Type()
)
wfBrSrInterfaceDropInvalidRcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDropInvalidRcs.setStatus("mandatory")
_WfBrSrInterfaceDropInvalidRings_Type = Counter32
_WfBrSrInterfaceDropInvalidRings_Object = MibTableColumn
wfBrSrInterfaceDropInvalidRings = _WfBrSrInterfaceDropInvalidRings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 15),
    _WfBrSrInterfaceDropInvalidRings_Type()
)
wfBrSrInterfaceDropInvalidRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDropInvalidRings.setStatus("mandatory")
_WfBrSrInterfaceDropSrfs_Type = Counter32
_WfBrSrInterfaceDropSrfs_Object = MibTableColumn
wfBrSrInterfaceDropSrfs = _WfBrSrInterfaceDropSrfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 16),
    _WfBrSrInterfaceDropSrfs_Type()
)
wfBrSrInterfaceDropSrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDropSrfs.setStatus("mandatory")
_WfBrSrBridgeTable_Object = MibTable
wfBrSrBridgeTable = _WfBrSrBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wfBrSrBridgeTable.setStatus("mandatory")
_WfBrSrBridgeEntry_Object = MibTableRow
wfBrSrBridgeEntry = _WfBrSrBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3, 1)
)
wfBrSrBridgeEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrSrBridgeId"),
)
if mibBuilder.loadTexts:
    wfBrSrBridgeEntry.setStatus("mandatory")


class _WfBrSrBridgeDelete_Type(Integer32):
    """Custom type wfBrSrBridgeDelete based on Integer32"""
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


_WfBrSrBridgeDelete_Type.__name__ = "Integer32"
_WfBrSrBridgeDelete_Object = MibTableColumn
wfBrSrBridgeDelete = _WfBrSrBridgeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3, 1, 1),
    _WfBrSrBridgeDelete_Type()
)
wfBrSrBridgeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBridgeDelete.setStatus("mandatory")
_WfBrSrBridgeId_Type = Integer32
_WfBrSrBridgeId_Object = MibTableColumn
wfBrSrBridgeId = _WfBrSrBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3, 1, 2),
    _WfBrSrBridgeId_Type()
)
wfBrSrBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBridgeId.setStatus("mandatory")
_WfBrSrIpExplorerTable_Object = MibTable
wfBrSrIpExplorerTable = _WfBrSrIpExplorerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wfBrSrIpExplorerTable.setStatus("mandatory")
_WfBrSrIpExplorerEntry_Object = MibTableRow
wfBrSrIpExplorerEntry = _WfBrSrIpExplorerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1)
)
wfBrSrIpExplorerEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrSrIpExplorerAddr"),
)
if mibBuilder.loadTexts:
    wfBrSrIpExplorerEntry.setStatus("mandatory")


class _WfBrSrIpExplorerDelete_Type(Integer32):
    """Custom type wfBrSrIpExplorerDelete based on Integer32"""
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


_WfBrSrIpExplorerDelete_Type.__name__ = "Integer32"
_WfBrSrIpExplorerDelete_Object = MibTableColumn
wfBrSrIpExplorerDelete = _WfBrSrIpExplorerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1, 1),
    _WfBrSrIpExplorerDelete_Type()
)
wfBrSrIpExplorerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrIpExplorerDelete.setStatus("mandatory")
_WfBrSrIpExplorerAddr_Type = IpAddress
_WfBrSrIpExplorerAddr_Object = MibTableColumn
wfBrSrIpExplorerAddr = _WfBrSrIpExplorerAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1, 2),
    _WfBrSrIpExplorerAddr_Type()
)
wfBrSrIpExplorerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpExplorerAddr.setStatus("mandatory")
_WfBrSrIpEncapsTable_Object = MibTable
wfBrSrIpEncapsTable = _WfBrSrIpEncapsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wfBrSrIpEncapsTable.setStatus("mandatory")
_WfBrSrIpEncapsEntry_Object = MibTableRow
wfBrSrIpEncapsEntry = _WfBrSrIpEncapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1)
)
wfBrSrIpEncapsEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrSrIpEncapsRing"),
)
if mibBuilder.loadTexts:
    wfBrSrIpEncapsEntry.setStatus("mandatory")
_WfBrSrIpEncapsRing_Type = Integer32
_WfBrSrIpEncapsRing_Object = MibTableColumn
wfBrSrIpEncapsRing = _WfBrSrIpEncapsRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1, 1),
    _WfBrSrIpEncapsRing_Type()
)
wfBrSrIpEncapsRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRing.setStatus("mandatory")
_WfBrSrIpEncapsIpAddress_Type = IpAddress
_WfBrSrIpEncapsIpAddress_Object = MibTableColumn
wfBrSrIpEncapsIpAddress = _WfBrSrIpEncapsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1, 2),
    _WfBrSrIpEncapsIpAddress_Type()
)
wfBrSrIpEncapsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsIpAddress.setStatus("mandatory")


class _WfBrSrIpEncapsStatus_Type(Integer32):
    """Custom type wfBrSrIpEncapsStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_WfBrSrIpEncapsStatus_Type.__name__ = "Integer32"
_WfBrSrIpEncapsStatus_Object = MibTableColumn
wfBrSrIpEncapsStatus = _WfBrSrIpEncapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1, 3),
    _WfBrSrIpEncapsStatus_Type()
)
wfBrSrIpEncapsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsStatus.setStatus("mandatory")
_WfBrSrTrafficFilterTable_Object = MibTable
wfBrSrTrafficFilterTable = _WfBrSrTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterTable.setStatus("mandatory")
_WfBrSrTrafficFilterEntry_Object = MibTableRow
wfBrSrTrafficFilterEntry = _WfBrSrTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1)
)
wfBrSrTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrSrTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfBrSrTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfBrSrTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterEntry.setStatus("mandatory")


class _WfBrSrTrafficFilterCreate_Type(Integer32):
    """Custom type wfBrSrTrafficFilterCreate based on Integer32"""
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


_WfBrSrTrafficFilterCreate_Type.__name__ = "Integer32"
_WfBrSrTrafficFilterCreate_Object = MibTableColumn
wfBrSrTrafficFilterCreate = _WfBrSrTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 1),
    _WfBrSrTrafficFilterCreate_Type()
)
wfBrSrTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterCreate.setStatus("mandatory")


class _WfBrSrTrafficFilterEnable_Type(Integer32):
    """Custom type wfBrSrTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrSrTrafficFilterEnable_Type.__name__ = "Integer32"
_WfBrSrTrafficFilterEnable_Object = MibTableColumn
wfBrSrTrafficFilterEnable = _WfBrSrTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 2),
    _WfBrSrTrafficFilterEnable_Type()
)
wfBrSrTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterEnable.setStatus("mandatory")


class _WfBrSrTrafficFilterStatus_Type(Integer32):
    """Custom type wfBrSrTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfBrSrTrafficFilterStatus_Type.__name__ = "Integer32"
_WfBrSrTrafficFilterStatus_Object = MibTableColumn
wfBrSrTrafficFilterStatus = _WfBrSrTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 3),
    _WfBrSrTrafficFilterStatus_Type()
)
wfBrSrTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterStatus.setStatus("mandatory")
_WfBrSrTrafficFilterCounter_Type = Counter32
_WfBrSrTrafficFilterCounter_Object = MibTableColumn
wfBrSrTrafficFilterCounter = _WfBrSrTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 4),
    _WfBrSrTrafficFilterCounter_Type()
)
wfBrSrTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterCounter.setStatus("mandatory")
_WfBrSrTrafficFilterDefinition_Type = OctetString
_WfBrSrTrafficFilterDefinition_Object = MibTableColumn
wfBrSrTrafficFilterDefinition = _WfBrSrTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 5),
    _WfBrSrTrafficFilterDefinition_Type()
)
wfBrSrTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterDefinition.setStatus("mandatory")
_WfBrSrTrafficFilterReserved_Type = Integer32
_WfBrSrTrafficFilterReserved_Object = MibTableColumn
wfBrSrTrafficFilterReserved = _WfBrSrTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 6),
    _WfBrSrTrafficFilterReserved_Type()
)
wfBrSrTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterReserved.setStatus("mandatory")
_WfBrSrTrafficFilterCircuit_Type = Integer32
_WfBrSrTrafficFilterCircuit_Object = MibTableColumn
wfBrSrTrafficFilterCircuit = _WfBrSrTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 7),
    _WfBrSrTrafficFilterCircuit_Type()
)
wfBrSrTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterCircuit.setStatus("mandatory")
_WfBrSrTrafficFilterRuleNumber_Type = Integer32
_WfBrSrTrafficFilterRuleNumber_Object = MibTableColumn
wfBrSrTrafficFilterRuleNumber = _WfBrSrTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 8),
    _WfBrSrTrafficFilterRuleNumber_Type()
)
wfBrSrTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterRuleNumber.setStatus("mandatory")
_WfBrSrTrafficFilterFragment_Type = Integer32
_WfBrSrTrafficFilterFragment_Object = MibTableColumn
wfBrSrTrafficFilterFragment = _WfBrSrTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 9),
    _WfBrSrTrafficFilterFragment_Type()
)
wfBrSrTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterFragment.setStatus("mandatory")
_WfBrSrEsRifTable_Object = MibTable
wfBrSrEsRifTable = _WfBrSrEsRifTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wfBrSrEsRifTable.setStatus("mandatory")
_WfBrSrEsRifEntry_Object = MibTableRow
wfBrSrEsRifEntry = _WfBrSrEsRifEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1)
)
wfBrSrEsRifEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrSrEsRifCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfBrSrEsRifProtocol"),
    (0, "Wellfleet-Series7-MIB", "wfBrSrEsRifMacAddr"),
)
if mibBuilder.loadTexts:
    wfBrSrEsRifEntry.setStatus("mandatory")
_WfBrSrEsRifCircuit_Type = Integer32
_WfBrSrEsRifCircuit_Object = MibTableColumn
wfBrSrEsRifCircuit = _WfBrSrEsRifCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 1),
    _WfBrSrEsRifCircuit_Type()
)
wfBrSrEsRifCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifCircuit.setStatus("mandatory")
_WfBrSrEsRifProtocol_Type = OctetString
_WfBrSrEsRifProtocol_Object = MibTableColumn
wfBrSrEsRifProtocol = _WfBrSrEsRifProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 2),
    _WfBrSrEsRifProtocol_Type()
)
wfBrSrEsRifProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifProtocol.setStatus("mandatory")
_WfBrSrEsRifMacAddr_Type = OctetString
_WfBrSrEsRifMacAddr_Object = MibTableColumn
wfBrSrEsRifMacAddr = _WfBrSrEsRifMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 3),
    _WfBrSrEsRifMacAddr_Type()
)
wfBrSrEsRifMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifMacAddr.setStatus("mandatory")
_WfBrSrEsRifRoute_Type = OctetString
_WfBrSrEsRifRoute_Object = MibTableColumn
wfBrSrEsRifRoute = _WfBrSrEsRifRoute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 4),
    _WfBrSrEsRifRoute_Type()
)
wfBrSrEsRifRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifRoute.setStatus("mandatory")
_WfBrTpInterface_Object = MibTable
wfBrTpInterface = _WfBrTpInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wfBrTpInterface.setStatus("mandatory")
_WfBrTpInterfaceEntry_Object = MibTableRow
wfBrTpInterfaceEntry = _WfBrTpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1)
)
wfBrTpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrTpInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfBrTpInterfaceEntry.setStatus("mandatory")


class _WfBrTpInterfaceDelete_Type(Integer32):
    """Custom type wfBrTpInterfaceDelete based on Integer32"""
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


_WfBrTpInterfaceDelete_Type.__name__ = "Integer32"
_WfBrTpInterfaceDelete_Object = MibTableColumn
wfBrTpInterfaceDelete = _WfBrTpInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 1),
    _WfBrTpInterfaceDelete_Type()
)
wfBrTpInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpInterfaceDelete.setStatus("mandatory")


class _WfBrTpInterfaceEnable_Type(Integer32):
    """Custom type wfBrTpInterfaceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrTpInterfaceEnable_Type.__name__ = "Integer32"
_WfBrTpInterfaceEnable_Object = MibTableColumn
wfBrTpInterfaceEnable = _WfBrTpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 2),
    _WfBrTpInterfaceEnable_Type()
)
wfBrTpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpInterfaceEnable.setStatus("mandatory")


class _WfBrTpInterfaceState_Type(Integer32):
    """Custom type wfBrTpInterfaceState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("pres", 4),
          ("up", 1))
    )


_WfBrTpInterfaceState_Type.__name__ = "Integer32"
_WfBrTpInterfaceState_Object = MibTableColumn
wfBrTpInterfaceState = _WfBrTpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 3),
    _WfBrTpInterfaceState_Type()
)
wfBrTpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceState.setStatus("mandatory")
_WfBrTpInterfaceCircuit_Type = Integer32
_WfBrTpInterfaceCircuit_Object = MibTableColumn
wfBrTpInterfaceCircuit = _WfBrTpInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 4),
    _WfBrTpInterfaceCircuit_Type()
)
wfBrTpInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceCircuit.setStatus("mandatory")
_WfBrTpInterfaceMaxInfo_Type = Integer32
_WfBrTpInterfaceMaxInfo_Object = MibTableColumn
wfBrTpInterfaceMaxInfo = _WfBrTpInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 5),
    _WfBrTpInterfaceMaxInfo_Type()
)
wfBrTpInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceMaxInfo.setStatus("mandatory")
_WfBrTpInterfaceInFrames_Type = Counter32
_WfBrTpInterfaceInFrames_Object = MibTableColumn
wfBrTpInterfaceInFrames = _WfBrTpInterfaceInFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 6),
    _WfBrTpInterfaceInFrames_Type()
)
wfBrTpInterfaceInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceInFrames.setStatus("mandatory")
_WfBrTpInterfaceOutFrames_Type = Counter32
_WfBrTpInterfaceOutFrames_Object = MibTableColumn
wfBrTpInterfaceOutFrames = _WfBrTpInterfaceOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 7),
    _WfBrTpInterfaceOutFrames_Type()
)
wfBrTpInterfaceOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceOutFrames.setStatus("mandatory")
_WfBrTpInterfaceInDiscards_Type = Counter32
_WfBrTpInterfaceInDiscards_Object = MibTableColumn
wfBrTpInterfaceInDiscards = _WfBrTpInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 8),
    _WfBrTpInterfaceInDiscards_Type()
)
wfBrTpInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceInDiscards.setStatus("mandatory")
_WfBrTrafficFilterTable_Object = MibTable
wfBrTrafficFilterTable = _WfBrTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wfBrTrafficFilterTable.setStatus("mandatory")
_WfBrTrafficFilterEntry_Object = MibTableRow
wfBrTrafficFilterEntry = _WfBrTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1)
)
wfBrTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfBrTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfBrTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfBrTrafficFilterEntry.setStatus("mandatory")


class _WfBrTrafficFilterCreate_Type(Integer32):
    """Custom type wfBrTrafficFilterCreate based on Integer32"""
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


_WfBrTrafficFilterCreate_Type.__name__ = "Integer32"
_WfBrTrafficFilterCreate_Object = MibTableColumn
wfBrTrafficFilterCreate = _WfBrTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 1),
    _WfBrTrafficFilterCreate_Type()
)
wfBrTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterCreate.setStatus("mandatory")


class _WfBrTrafficFilterEnable_Type(Integer32):
    """Custom type wfBrTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrTrafficFilterEnable_Type.__name__ = "Integer32"
_WfBrTrafficFilterEnable_Object = MibTableColumn
wfBrTrafficFilterEnable = _WfBrTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 2),
    _WfBrTrafficFilterEnable_Type()
)
wfBrTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterEnable.setStatus("mandatory")


class _WfBrTrafficFilterStatus_Type(Integer32):
    """Custom type wfBrTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfBrTrafficFilterStatus_Type.__name__ = "Integer32"
_WfBrTrafficFilterStatus_Object = MibTableColumn
wfBrTrafficFilterStatus = _WfBrTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 3),
    _WfBrTrafficFilterStatus_Type()
)
wfBrTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterStatus.setStatus("mandatory")
_WfBrTrafficFilterCounter_Type = Counter32
_WfBrTrafficFilterCounter_Object = MibTableColumn
wfBrTrafficFilterCounter = _WfBrTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 4),
    _WfBrTrafficFilterCounter_Type()
)
wfBrTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterCounter.setStatus("mandatory")
_WfBrTrafficFilterDefinition_Type = Opaque
_WfBrTrafficFilterDefinition_Object = MibTableColumn
wfBrTrafficFilterDefinition = _WfBrTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 5),
    _WfBrTrafficFilterDefinition_Type()
)
wfBrTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterDefinition.setStatus("mandatory")
_WfBrTrafficFilterReserved_Type = Integer32
_WfBrTrafficFilterReserved_Object = MibTableColumn
wfBrTrafficFilterReserved = _WfBrTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 6),
    _WfBrTrafficFilterReserved_Type()
)
wfBrTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfBrTrafficFilterReserved.setStatus("mandatory")
_WfBrTrafficFilterCircuit_Type = Integer32
_WfBrTrafficFilterCircuit_Object = MibTableColumn
wfBrTrafficFilterCircuit = _WfBrTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 7),
    _WfBrTrafficFilterCircuit_Type()
)
wfBrTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterCircuit.setStatus("mandatory")
_WfBrTrafficFilterRuleNumber_Type = Integer32
_WfBrTrafficFilterRuleNumber_Object = MibTableColumn
wfBrTrafficFilterRuleNumber = _WfBrTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 8),
    _WfBrTrafficFilterRuleNumber_Type()
)
wfBrTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterRuleNumber.setStatus("mandatory")
_WfBrTrafficFilterFragment_Type = Integer32
_WfBrTrafficFilterFragment_Object = MibTableColumn
wfBrTrafficFilterFragment = _WfBrTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 9),
    _WfBrTrafficFilterFragment_Type()
)
wfBrTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterFragment.setStatus("mandatory")
_WfSpanningTree_ObjectIdentity = ObjectIdentity
wfSpanningTree = _WfSpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2)
)
_WfBrStp_ObjectIdentity = ObjectIdentity
wfBrStp = _WfBrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1)
)


class _WfBrStpBaseDelete_Type(Integer32):
    """Custom type wfBrStpBaseDelete based on Integer32"""
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


_WfBrStpBaseDelete_Type.__name__ = "Integer32"
_WfBrStpBaseDelete_Object = MibScalar
wfBrStpBaseDelete = _WfBrStpBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 1),
    _WfBrStpBaseDelete_Type()
)
wfBrStpBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBaseDelete.setStatus("mandatory")


class _WfBrStpBaseEnable_Type(Integer32):
    """Custom type wfBrStpBaseEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrStpBaseEnable_Type.__name__ = "Integer32"
_WfBrStpBaseEnable_Object = MibScalar
wfBrStpBaseEnable = _WfBrStpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 2),
    _WfBrStpBaseEnable_Type()
)
wfBrStpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBaseEnable.setStatus("mandatory")


class _WfBrStpBaseState_Type(Integer32):
    """Custom type wfBrStpBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("pres", 4),
          ("up", 1))
    )


_WfBrStpBaseState_Type.__name__ = "Integer32"
_WfBrStpBaseState_Object = MibScalar
wfBrStpBaseState = _WfBrStpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 3),
    _WfBrStpBaseState_Type()
)
wfBrStpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpBaseState.setStatus("mandatory")


class _WfBrStpProtocolSpecification_Type(Integer32):
    """Custom type wfBrStpProtocolSpecification based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("declb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_WfBrStpProtocolSpecification_Type.__name__ = "Integer32"
_WfBrStpProtocolSpecification_Object = MibScalar
wfBrStpProtocolSpecification = _WfBrStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 4),
    _WfBrStpProtocolSpecification_Type()
)
wfBrStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpProtocolSpecification.setStatus("mandatory")
_WfBrStpBridgeID_Type = OctetString
_WfBrStpBridgeID_Object = MibScalar
wfBrStpBridgeID = _WfBrStpBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 5),
    _WfBrStpBridgeID_Type()
)
wfBrStpBridgeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeID.setStatus("mandatory")
_WfBrStpTimeSinceTopologyChange_Type = Counter32
_WfBrStpTimeSinceTopologyChange_Object = MibScalar
wfBrStpTimeSinceTopologyChange = _WfBrStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 6),
    _WfBrStpTimeSinceTopologyChange_Type()
)
wfBrStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpTimeSinceTopologyChange.setStatus("mandatory")
_WfBrStpTopChanges_Type = Counter32
_WfBrStpTopChanges_Object = MibScalar
wfBrStpTopChanges = _WfBrStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 7),
    _WfBrStpTopChanges_Type()
)
wfBrStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpTopChanges.setStatus("mandatory")
_WfBrStpDesignatedRoot_Type = OctetString
_WfBrStpDesignatedRoot_Object = MibScalar
wfBrStpDesignatedRoot = _WfBrStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 8),
    _WfBrStpDesignatedRoot_Type()
)
wfBrStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpDesignatedRoot.setStatus("mandatory")
_WfBrStpRootCost_Type = Integer32
_WfBrStpRootCost_Object = MibScalar
wfBrStpRootCost = _WfBrStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 9),
    _WfBrStpRootCost_Type()
)
wfBrStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpRootCost.setStatus("mandatory")
_WfBrStpRootPort_Type = Integer32
_WfBrStpRootPort_Object = MibScalar
wfBrStpRootPort = _WfBrStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 10),
    _WfBrStpRootPort_Type()
)
wfBrStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpRootPort.setStatus("mandatory")
_WfBrStpMaxAge_Type = Integer32
_WfBrStpMaxAge_Object = MibScalar
wfBrStpMaxAge = _WfBrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 11),
    _WfBrStpMaxAge_Type()
)
wfBrStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpMaxAge.setStatus("mandatory")
_WfBrStpHelloTime_Type = Integer32
_WfBrStpHelloTime_Object = MibScalar
wfBrStpHelloTime = _WfBrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 12),
    _WfBrStpHelloTime_Type()
)
wfBrStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpHelloTime.setStatus("mandatory")


class _WfBrStpHoldTime_Type(Integer32):
    """Custom type wfBrStpHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("time", 100)
    )


_WfBrStpHoldTime_Type.__name__ = "Integer32"
_WfBrStpHoldTime_Object = MibScalar
wfBrStpHoldTime = _WfBrStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 13),
    _WfBrStpHoldTime_Type()
)
wfBrStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpHoldTime.setStatus("mandatory")
_WfBrStpForwardDelay_Type = Integer32
_WfBrStpForwardDelay_Object = MibScalar
wfBrStpForwardDelay = _WfBrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 14),
    _WfBrStpForwardDelay_Type()
)
wfBrStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpForwardDelay.setStatus("mandatory")


class _WfBrStpBridgeMaxAge_Type(Integer32):
    """Custom type wfBrStpBridgeMaxAge based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(600,
              2000,
              4000)
        )
    )
    namedValues = NamedValues(
        *(("default", 2000),
          ("maximum", 4000),
          ("minimum", 600))
    )


_WfBrStpBridgeMaxAge_Type.__name__ = "Integer32"
_WfBrStpBridgeMaxAge_Object = MibScalar
wfBrStpBridgeMaxAge = _WfBrStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 15),
    _WfBrStpBridgeMaxAge_Type()
)
wfBrStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeMaxAge.setStatus("mandatory")


class _WfBrStpBridgeHelloTime_Type(Integer32):
    """Custom type wfBrStpBridgeHelloTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("default", 200),
          ("maximum", 1000),
          ("minimum", 100))
    )


_WfBrStpBridgeHelloTime_Type.__name__ = "Integer32"
_WfBrStpBridgeHelloTime_Object = MibScalar
wfBrStpBridgeHelloTime = _WfBrStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 16),
    _WfBrStpBridgeHelloTime_Type()
)
wfBrStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeHelloTime.setStatus("mandatory")


class _WfBrStpBridgeForwardDelay_Type(Integer32):
    """Custom type wfBrStpBridgeForwardDelay based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(400,
              1500,
              3000)
        )
    )
    namedValues = NamedValues(
        *(("default", 1500),
          ("maximum", 3000),
          ("minimum", 400))
    )


_WfBrStpBridgeForwardDelay_Type.__name__ = "Integer32"
_WfBrStpBridgeForwardDelay_Object = MibScalar
wfBrStpBridgeForwardDelay = _WfBrStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 17),
    _WfBrStpBridgeForwardDelay_Type()
)
wfBrStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeForwardDelay.setStatus("mandatory")
_WfBrStpInterface_Object = MibTable
wfBrStpInterface = _WfBrStpInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfBrStpInterface.setStatus("mandatory")
_WfBrStpInterfaceEntry_Object = MibTableRow
wfBrStpInterfaceEntry = _WfBrStpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1)
)
wfBrStpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfBrStpInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfBrStpInterfaceEntry.setStatus("mandatory")


class _WfBrStpInterfaceDelete_Type(Integer32):
    """Custom type wfBrStpInterfaceDelete based on Integer32"""
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


_WfBrStpInterfaceDelete_Type.__name__ = "Integer32"
_WfBrStpInterfaceDelete_Object = MibTableColumn
wfBrStpInterfaceDelete = _WfBrStpInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 1),
    _WfBrStpInterfaceDelete_Type()
)
wfBrStpInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDelete.setStatus("mandatory")


class _WfBrStpInterfaceEnable_Type(Integer32):
    """Custom type wfBrStpInterfaceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfBrStpInterfaceEnable_Type.__name__ = "Integer32"
_WfBrStpInterfaceEnable_Object = MibTableColumn
wfBrStpInterfaceEnable = _WfBrStpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 2),
    _WfBrStpInterfaceEnable_Type()
)
wfBrStpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfaceEnable.setStatus("mandatory")
_WfBrStpInterfaceCircuit_Type = Integer32
_WfBrStpInterfaceCircuit_Object = MibTableColumn
wfBrStpInterfaceCircuit = _WfBrStpInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 3),
    _WfBrStpInterfaceCircuit_Type()
)
wfBrStpInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceCircuit.setStatus("mandatory")


class _WfBrStpInterfacePriority_Type(Integer32):
    """Custom type wfBrStpInterfacePriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 128),
          ("maximum", 255))
    )


_WfBrStpInterfacePriority_Type.__name__ = "Integer32"
_WfBrStpInterfacePriority_Object = MibTableColumn
wfBrStpInterfacePriority = _WfBrStpInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 4),
    _WfBrStpInterfacePriority_Type()
)
wfBrStpInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfacePriority.setStatus("mandatory")


class _WfBrStpInterfaceState_Type(Integer32):
    """Custom type wfBrStpInterfaceState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_WfBrStpInterfaceState_Type.__name__ = "Integer32"
_WfBrStpInterfaceState_Object = MibTableColumn
wfBrStpInterfaceState = _WfBrStpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 5),
    _WfBrStpInterfaceState_Type()
)
wfBrStpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceState.setStatus("mandatory")
_WfBrStpInterfaceMultiCastAddr_Type = OctetString
_WfBrStpInterfaceMultiCastAddr_Object = MibTableColumn
wfBrStpInterfaceMultiCastAddr = _WfBrStpInterfaceMultiCastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 6),
    _WfBrStpInterfaceMultiCastAddr_Type()
)
wfBrStpInterfaceMultiCastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceMultiCastAddr.setStatus("mandatory")


class _WfBrStpInterfacePathCost_Type(Integer32):
    """Custom type wfBrStpInterfacePathCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 65535),
          ("minimum", 1))
    )


_WfBrStpInterfacePathCost_Type.__name__ = "Integer32"
_WfBrStpInterfacePathCost_Object = MibTableColumn
wfBrStpInterfacePathCost = _WfBrStpInterfacePathCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 7),
    _WfBrStpInterfacePathCost_Type()
)
wfBrStpInterfacePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfacePathCost.setStatus("mandatory")
_WfBrStpInterfaceDesignatedRoot_Type = OctetString
_WfBrStpInterfaceDesignatedRoot_Object = MibTableColumn
wfBrStpInterfaceDesignatedRoot = _WfBrStpInterfaceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 8),
    _WfBrStpInterfaceDesignatedRoot_Type()
)
wfBrStpInterfaceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedRoot.setStatus("mandatory")
_WfBrStpInterfaceDesignatedCost_Type = Integer32
_WfBrStpInterfaceDesignatedCost_Object = MibTableColumn
wfBrStpInterfaceDesignatedCost = _WfBrStpInterfaceDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 9),
    _WfBrStpInterfaceDesignatedCost_Type()
)
wfBrStpInterfaceDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedCost.setStatus("mandatory")
_WfBrStpInterfaceDesignatedBridge_Type = OctetString
_WfBrStpInterfaceDesignatedBridge_Object = MibTableColumn
wfBrStpInterfaceDesignatedBridge = _WfBrStpInterfaceDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 10),
    _WfBrStpInterfaceDesignatedBridge_Type()
)
wfBrStpInterfaceDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedBridge.setStatus("mandatory")
_WfBrStpInterfaceDesignatedPort_Type = Integer32
_WfBrStpInterfaceDesignatedPort_Object = MibTableColumn
wfBrStpInterfaceDesignatedPort = _WfBrStpInterfaceDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 11),
    _WfBrStpInterfaceDesignatedPort_Type()
)
wfBrStpInterfaceDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedPort.setStatus("mandatory")
_WfBrStpInterfaceForwardTransitions_Type = Counter32
_WfBrStpInterfaceForwardTransitions_Object = MibTableColumn
wfBrStpInterfaceForwardTransitions = _WfBrStpInterfaceForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 12),
    _WfBrStpInterfaceForwardTransitions_Type()
)
wfBrStpInterfaceForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceForwardTransitions.setStatus("mandatory")
_WfBrStpInterfacePktsXmitd_Type = Counter32
_WfBrStpInterfacePktsXmitd_Object = MibTableColumn
wfBrStpInterfacePktsXmitd = _WfBrStpInterfacePktsXmitd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 13),
    _WfBrStpInterfacePktsXmitd_Type()
)
wfBrStpInterfacePktsXmitd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfacePktsXmitd.setStatus("mandatory")
_WfBrStpInterfacePktsRcvd_Type = Counter32
_WfBrStpInterfacePktsRcvd_Object = MibTableColumn
wfBrStpInterfacePktsRcvd = _WfBrStpInterfacePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 14),
    _WfBrStpInterfacePktsRcvd_Type()
)
wfBrStpInterfacePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfacePktsRcvd.setStatus("mandatory")
_WfIfGroup_ObjectIdentity = ObjectIdentity
wfIfGroup = _WfIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3)
)
_WfIf_ObjectIdentity = ObjectIdentity
wfIf = _WfIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1)
)
_WfIfNumber_Type = Integer32
_WfIfNumber_Object = MibScalar
wfIfNumber = _WfIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1, 1),
    _WfIfNumber_Type()
)
wfIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfNumber.setStatus("mandatory")
_WfIfTable_Object = MibTable
wfIfTable = _WfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wfIfTable.setStatus("mandatory")
_WfIfEntry_Object = MibTableRow
wfIfEntry = _WfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1)
)
wfIfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIfIndex"),
)
if mibBuilder.loadTexts:
    wfIfEntry.setStatus("mandatory")
_WfIfIndex_Type = Integer32
_WfIfIndex_Object = MibTableColumn
wfIfIndex = _WfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 1),
    _WfIfIndex_Type()
)
wfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfIndex.setStatus("mandatory")
_WfIfDescr_Type = DisplayString
_WfIfDescr_Object = MibTableColumn
wfIfDescr = _WfIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 2),
    _WfIfDescr_Type()
)
wfIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfDescr.setStatus("mandatory")
_WfIfType_Type = Integer32
_WfIfType_Object = MibTableColumn
wfIfType = _WfIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 3),
    _WfIfType_Type()
)
wfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfType.setStatus("mandatory")
_WfIfMtu_Type = Integer32
_WfIfMtu_Object = MibTableColumn
wfIfMtu = _WfIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 4),
    _WfIfMtu_Type()
)
wfIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfMtu.setStatus("mandatory")
_WfIfSpeed_Type = Gauge32
_WfIfSpeed_Object = MibTableColumn
wfIfSpeed = _WfIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 5),
    _WfIfSpeed_Type()
)
wfIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfSpeed.setStatus("mandatory")
_WfIfPhysAddress_Type = OctetString
_WfIfPhysAddress_Object = MibTableColumn
wfIfPhysAddress = _WfIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 6),
    _WfIfPhysAddress_Type()
)
wfIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfPhysAddress.setStatus("mandatory")
_WfIfAdminStatus_Type = Integer32
_WfIfAdminStatus_Object = MibTableColumn
wfIfAdminStatus = _WfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 7),
    _WfIfAdminStatus_Type()
)
wfIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfAdminStatus.setStatus("mandatory")
_WfIfOperStatus_Type = Integer32
_WfIfOperStatus_Object = MibTableColumn
wfIfOperStatus = _WfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 8),
    _WfIfOperStatus_Type()
)
wfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOperStatus.setStatus("mandatory")
_WfIfLastChange_Type = TimeTicks
_WfIfLastChange_Object = MibTableColumn
wfIfLastChange = _WfIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 9),
    _WfIfLastChange_Type()
)
wfIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfLastChange.setStatus("mandatory")
_WfIfInOctets_Type = Counter32
_WfIfInOctets_Object = MibTableColumn
wfIfInOctets = _WfIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 10),
    _WfIfInOctets_Type()
)
wfIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInOctets.setStatus("mandatory")
_WfIfInUcastPkts_Type = Counter32
_WfIfInUcastPkts_Object = MibTableColumn
wfIfInUcastPkts = _WfIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 11),
    _WfIfInUcastPkts_Type()
)
wfIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInUcastPkts.setStatus("mandatory")
_WfIfInNUCastPkts_Type = Counter32
_WfIfInNUCastPkts_Object = MibTableColumn
wfIfInNUCastPkts = _WfIfInNUCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 12),
    _WfIfInNUCastPkts_Type()
)
wfIfInNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInNUCastPkts.setStatus("mandatory")
_WfIfInDiscards_Type = Counter32
_WfIfInDiscards_Object = MibTableColumn
wfIfInDiscards = _WfIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 13),
    _WfIfInDiscards_Type()
)
wfIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInDiscards.setStatus("mandatory")
_WfIfInErrors_Type = Counter32
_WfIfInErrors_Object = MibTableColumn
wfIfInErrors = _WfIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 14),
    _WfIfInErrors_Type()
)
wfIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInErrors.setStatus("mandatory")
_WfIfInUnknownProtos_Type = Counter32
_WfIfInUnknownProtos_Object = MibTableColumn
wfIfInUnknownProtos = _WfIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 15),
    _WfIfInUnknownProtos_Type()
)
wfIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfInUnknownProtos.setStatus("mandatory")
_WfIfOutOctets_Type = Counter32
_WfIfOutOctets_Object = MibTableColumn
wfIfOutOctets = _WfIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 16),
    _WfIfOutOctets_Type()
)
wfIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutOctets.setStatus("mandatory")
_WfIfOutUcastPkts_Type = Counter32
_WfIfOutUcastPkts_Object = MibTableColumn
wfIfOutUcastPkts = _WfIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 17),
    _WfIfOutUcastPkts_Type()
)
wfIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutUcastPkts.setStatus("mandatory")
_WfIfOutNUcastPkts_Type = Counter32
_WfIfOutNUcastPkts_Object = MibTableColumn
wfIfOutNUcastPkts = _WfIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 18),
    _WfIfOutNUcastPkts_Type()
)
wfIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutNUcastPkts.setStatus("mandatory")
_WfIfOutDiscards_Type = Counter32
_WfIfOutDiscards_Object = MibTableColumn
wfIfOutDiscards = _WfIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 19),
    _WfIfOutDiscards_Type()
)
wfIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutDiscards.setStatus("mandatory")
_WfIfOutErrors_Type = Counter32
_WfIfOutErrors_Object = MibTableColumn
wfIfOutErrors = _WfIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 20),
    _WfIfOutErrors_Type()
)
wfIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutErrors.setStatus("mandatory")
_WfIfOutQLen_Type = Gauge32
_WfIfOutQLen_Object = MibTableColumn
wfIfOutQLen = _WfIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 21),
    _WfIfOutQLen_Type()
)
wfIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfOutQLen.setStatus("mandatory")
_WfIfSpecific_Type = ObjectIdentifier
_WfIfSpecific_Object = MibTableColumn
wfIfSpecific = _WfIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 22),
    _WfIfSpecific_Type()
)
wfIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfSpecific.setStatus("mandatory")
_WfCircuitOptsGroup_ObjectIdentity = ObjectIdentity
wfCircuitOptsGroup = _WfCircuitOptsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4)
)
_WfCctOptsTable_Object = MibTable
wfCctOptsTable = _WfCctOptsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wfCctOptsTable.setStatus("mandatory")
_WfCctOptsEntry_Object = MibTableRow
wfCctOptsEntry = _WfCctOptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1)
)
wfCctOptsEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfCctOptsCct"),
)
if mibBuilder.loadTexts:
    wfCctOptsEntry.setStatus("mandatory")


class _WfCctOptsDelete_Type(Integer32):
    """Custom type wfCctOptsDelete based on Integer32"""
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


_WfCctOptsDelete_Type.__name__ = "Integer32"
_WfCctOptsDelete_Object = MibTableColumn
wfCctOptsDelete = _WfCctOptsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 1),
    _WfCctOptsDelete_Type()
)
wfCctOptsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsDelete.setStatus("mandatory")


class _WfCctOptsPriorityQueueingDisable_Type(Integer32):
    """Custom type wfCctOptsPriorityQueueingDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfCctOptsPriorityQueueingDisable_Type.__name__ = "Integer32"
_WfCctOptsPriorityQueueingDisable_Object = MibTableColumn
wfCctOptsPriorityQueueingDisable = _WfCctOptsPriorityQueueingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 2),
    _WfCctOptsPriorityQueueingDisable_Type()
)
wfCctOptsPriorityQueueingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsPriorityQueueingDisable.setStatus("mandatory")
_WfCctOptsCct_Type = Integer32
_WfCctOptsCct_Object = MibTableColumn
wfCctOptsCct = _WfCctOptsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 3),
    _WfCctOptsCct_Type()
)
wfCctOptsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsCct.setStatus("mandatory")


class _WfCctOptsHighPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsHighPriorityQueueLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsHighPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsHighPriorityQueueLimit_Object = MibTableColumn
wfCctOptsHighPriorityQueueLimit = _WfCctOptsHighPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 4),
    _WfCctOptsHighPriorityQueueLimit_Type()
)
wfCctOptsHighPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsHighPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsNormalPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsNormalPriorityQueueLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsNormalPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsNormalPriorityQueueLimit_Object = MibTableColumn
wfCctOptsNormalPriorityQueueLimit = _WfCctOptsNormalPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 5),
    _WfCctOptsNormalPriorityQueueLimit_Type()
)
wfCctOptsNormalPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsNormalPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsLowPriorityQueueLimit_Type(Integer32):
    """Custom type wfCctOptsLowPriorityQueueLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfCctOptsLowPriorityQueueLimit_Type.__name__ = "Integer32"
_WfCctOptsLowPriorityQueueLimit_Object = MibTableColumn
wfCctOptsLowPriorityQueueLimit = _WfCctOptsLowPriorityQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 6),
    _WfCctOptsLowPriorityQueueLimit_Type()
)
wfCctOptsLowPriorityQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLowPriorityQueueLimit.setStatus("mandatory")


class _WfCctOptsMaxInterruptQueueLatency_Type(Integer32):
    """Custom type wfCctOptsMaxInterruptQueueLatency based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              2500,
              5000)
        )
    )
    namedValues = NamedValues(
        *(("default", 2500),
          ("maximum", 5000),
          ("minimum", 100))
    )


_WfCctOptsMaxInterruptQueueLatency_Type.__name__ = "Integer32"
_WfCctOptsMaxInterruptQueueLatency_Object = MibTableColumn
wfCctOptsMaxInterruptQueueLatency = _WfCctOptsMaxInterruptQueueLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 7),
    _WfCctOptsMaxInterruptQueueLatency_Type()
)
wfCctOptsMaxInterruptQueueLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsMaxInterruptQueueLatency.setStatus("mandatory")


class _WfCctOptsMaxHighPriorityQueueLatency_Type(Integer32):
    """Custom type wfCctOptsMaxHighPriorityQueueLatency based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              250,
              5000)
        )
    )
    namedValues = NamedValues(
        *(("default", 250),
          ("maximum", 5000),
          ("minimum", 100))
    )


_WfCctOptsMaxHighPriorityQueueLatency_Type.__name__ = "Integer32"
_WfCctOptsMaxHighPriorityQueueLatency_Object = MibTableColumn
wfCctOptsMaxHighPriorityQueueLatency = _WfCctOptsMaxHighPriorityQueueLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 8),
    _WfCctOptsMaxHighPriorityQueueLatency_Type()
)
wfCctOptsMaxHighPriorityQueueLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsMaxHighPriorityQueueLatency.setStatus("mandatory")
_WfCctOptsHiXmits_Type = Counter32
_WfCctOptsHiXmits_Object = MibTableColumn
wfCctOptsHiXmits = _WfCctOptsHiXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 9),
    _WfCctOptsHiXmits_Type()
)
wfCctOptsHiXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiXmits.setStatus("mandatory")
_WfCctOptsNormalXmits_Type = Counter32
_WfCctOptsNormalXmits_Object = MibTableColumn
wfCctOptsNormalXmits = _WfCctOptsNormalXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 10),
    _WfCctOptsNormalXmits_Type()
)
wfCctOptsNormalXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalXmits.setStatus("mandatory")
_WfCctOptsLoXmits_Type = Counter32
_WfCctOptsLoXmits_Object = MibTableColumn
wfCctOptsLoXmits = _WfCctOptsLoXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 11),
    _WfCctOptsLoXmits_Type()
)
wfCctOptsLoXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoXmits.setStatus("mandatory")
_WfCctOptsHiClippedPkts_Type = Counter32
_WfCctOptsHiClippedPkts_Object = MibTableColumn
wfCctOptsHiClippedPkts = _WfCctOptsHiClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 12),
    _WfCctOptsHiClippedPkts_Type()
)
wfCctOptsHiClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiClippedPkts.setStatus("mandatory")
_WfCctOptsNormalClippedPkts_Type = Counter32
_WfCctOptsNormalClippedPkts_Object = MibTableColumn
wfCctOptsNormalClippedPkts = _WfCctOptsNormalClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 13),
    _WfCctOptsNormalClippedPkts_Type()
)
wfCctOptsNormalClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalClippedPkts.setStatus("mandatory")
_WfCctOptsLoClippedPkts_Type = Counter32
_WfCctOptsLoClippedPkts_Object = MibTableColumn
wfCctOptsLoClippedPkts = _WfCctOptsLoClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 14),
    _WfCctOptsLoClippedPkts_Type()
)
wfCctOptsLoClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoClippedPkts.setStatus("mandatory")
_WfCctOptsIntrQHighWaterPkts_Type = Gauge32
_WfCctOptsIntrQHighWaterPkts_Object = MibTableColumn
wfCctOptsIntrQHighWaterPkts = _WfCctOptsIntrQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 15),
    _WfCctOptsIntrQHighWaterPkts_Type()
)
wfCctOptsIntrQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIntrQHighWaterPkts.setStatus("mandatory")
_WfCctOptsHiQHighWaterPkts_Type = Gauge32
_WfCctOptsHiQHighWaterPkts_Object = MibTableColumn
wfCctOptsHiQHighWaterPkts = _WfCctOptsHiQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 16),
    _WfCctOptsHiQHighWaterPkts_Type()
)
wfCctOptsHiQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsHiQHighWaterPkts.setStatus("mandatory")
_WfCctOptsNormalQHighWaterPkts_Type = Gauge32
_WfCctOptsNormalQHighWaterPkts_Object = MibTableColumn
wfCctOptsNormalQHighWaterPkts = _WfCctOptsNormalQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 17),
    _WfCctOptsNormalQHighWaterPkts_Type()
)
wfCctOptsNormalQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsNormalQHighWaterPkts.setStatus("mandatory")
_WfCctOptsLoQHighWaterPkts_Type = Gauge32
_WfCctOptsLoQHighWaterPkts_Object = MibTableColumn
wfCctOptsLoQHighWaterPkts = _WfCctOptsLoQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 18),
    _WfCctOptsLoQHighWaterPkts_Type()
)
wfCctOptsLoQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLoQHighWaterPkts.setStatus("mandatory")
_WfCctOptsHighWaterPktsClear_Type = Integer32
_WfCctOptsHighWaterPktsClear_Object = MibTableColumn
wfCctOptsHighWaterPktsClear = _WfCctOptsHighWaterPktsClear_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 19),
    _WfCctOptsHighWaterPktsClear_Type()
)
wfCctOptsHighWaterPktsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsHighWaterPktsClear.setStatus("mandatory")
_WfCctOptsDroppedPkts_Type = Counter32
_WfCctOptsDroppedPkts_Object = MibTableColumn
wfCctOptsDroppedPkts = _WfCctOptsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 20),
    _WfCctOptsDroppedPkts_Type()
)
wfCctOptsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsDroppedPkts.setStatus("mandatory")
_WfCctOptsLargePkts_Type = Counter32
_WfCctOptsLargePkts_Object = MibTableColumn
wfCctOptsLargePkts = _WfCctOptsLargePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 21),
    _WfCctOptsLargePkts_Type()
)
wfCctOptsLargePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLargePkts.setStatus("mandatory")
_WfCctOptsRxPkts_Type = Counter32
_WfCctOptsRxPkts_Object = MibTableColumn
wfCctOptsRxPkts = _WfCctOptsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 1, 1, 22),
    _WfCctOptsRxPkts_Type()
)
wfCctOptsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsRxPkts.setStatus("mandatory")
_WfCctOptsBrFilterTable_Object = MibTable
wfCctOptsBrFilterTable = _WfCctOptsBrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wfCctOptsBrFilterTable.setStatus("mandatory")
_WfCctOptsBrFilterEntry_Object = MibTableRow
wfCctOptsBrFilterEntry = _WfCctOptsBrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1)
)
wfCctOptsBrFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfCctOptsBrFilterCct"),
    (0, "Wellfleet-Series7-MIB", "wfCctOptsBrFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfCctOptsBrFilterFragment"),
)
if mibBuilder.loadTexts:
    wfCctOptsBrFilterEntry.setStatus("mandatory")


class _WfCctOptsBrFilterCreate_Type(Integer32):
    """Custom type wfCctOptsBrFilterCreate based on Integer32"""
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


_WfCctOptsBrFilterCreate_Type.__name__ = "Integer32"
_WfCctOptsBrFilterCreate_Object = MibTableColumn
wfCctOptsBrFilterCreate = _WfCctOptsBrFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 1),
    _WfCctOptsBrFilterCreate_Type()
)
wfCctOptsBrFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterCreate.setStatus("mandatory")


class _WfCctOptsBrFilterEnable_Type(Integer32):
    """Custom type wfCctOptsBrFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfCctOptsBrFilterEnable_Type.__name__ = "Integer32"
_WfCctOptsBrFilterEnable_Object = MibTableColumn
wfCctOptsBrFilterEnable = _WfCctOptsBrFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 2),
    _WfCctOptsBrFilterEnable_Type()
)
wfCctOptsBrFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterEnable.setStatus("mandatory")


class _WfCctOptsBrFilterState_Type(Integer32):
    """Custom type wfCctOptsBrFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsBrFilterState_Type.__name__ = "Integer32"
_WfCctOptsBrFilterState_Object = MibTableColumn
wfCctOptsBrFilterState = _WfCctOptsBrFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 3),
    _WfCctOptsBrFilterState_Type()
)
wfCctOptsBrFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterState.setStatus("mandatory")
_WfCctOptsBrFilterCounter_Type = Counter32
_WfCctOptsBrFilterCounter_Object = MibTableColumn
wfCctOptsBrFilterCounter = _WfCctOptsBrFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 4),
    _WfCctOptsBrFilterCounter_Type()
)
wfCctOptsBrFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterCounter.setStatus("mandatory")
_WfCctOptsBrFilterDefinition_Type = OctetString
_WfCctOptsBrFilterDefinition_Object = MibTableColumn
wfCctOptsBrFilterDefinition = _WfCctOptsBrFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 5),
    _WfCctOptsBrFilterDefinition_Type()
)
wfCctOptsBrFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterDefinition.setStatus("mandatory")
_WfCctOptsBrFilterReserved_Type = Integer32
_WfCctOptsBrFilterReserved_Object = MibTableColumn
wfCctOptsBrFilterReserved = _WfCctOptsBrFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 6),
    _WfCctOptsBrFilterReserved_Type()
)
wfCctOptsBrFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterReserved.setStatus("mandatory")
_WfCctOptsBrFilterCct_Type = Integer32
_WfCctOptsBrFilterCct_Object = MibTableColumn
wfCctOptsBrFilterCct = _WfCctOptsBrFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 7),
    _WfCctOptsBrFilterCct_Type()
)
wfCctOptsBrFilterCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterCct.setStatus("mandatory")
_WfCctOptsBrFilterRuleNumber_Type = Integer32
_WfCctOptsBrFilterRuleNumber_Object = MibTableColumn
wfCctOptsBrFilterRuleNumber = _WfCctOptsBrFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 8),
    _WfCctOptsBrFilterRuleNumber_Type()
)
wfCctOptsBrFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterRuleNumber.setStatus("mandatory")
_WfCctOptsBrFilterFragment_Type = Integer32
_WfCctOptsBrFilterFragment_Object = MibTableColumn
wfCctOptsBrFilterFragment = _WfCctOptsBrFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 2, 1, 9),
    _WfCctOptsBrFilterFragment_Type()
)
wfCctOptsBrFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsBrFilterFragment.setStatus("mandatory")
_WfCctOptsIpFilterTable_Object = MibTable
wfCctOptsIpFilterTable = _WfCctOptsIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wfCctOptsIpFilterTable.setStatus("mandatory")
_WfCctOptsIpFilterEntry_Object = MibTableRow
wfCctOptsIpFilterEntry = _WfCctOptsIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1)
)
wfCctOptsIpFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfCctOptsIpFilterCct"),
    (0, "Wellfleet-Series7-MIB", "wfCctOptsIpFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfCctOptsIpFilterFragment"),
)
if mibBuilder.loadTexts:
    wfCctOptsIpFilterEntry.setStatus("mandatory")


class _WfCctOptsIpFilterCreate_Type(Integer32):
    """Custom type wfCctOptsIpFilterCreate based on Integer32"""
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


_WfCctOptsIpFilterCreate_Type.__name__ = "Integer32"
_WfCctOptsIpFilterCreate_Object = MibTableColumn
wfCctOptsIpFilterCreate = _WfCctOptsIpFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 1),
    _WfCctOptsIpFilterCreate_Type()
)
wfCctOptsIpFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterCreate.setStatus("mandatory")


class _WfCctOptsIpFilterEnable_Type(Integer32):
    """Custom type wfCctOptsIpFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfCctOptsIpFilterEnable_Type.__name__ = "Integer32"
_WfCctOptsIpFilterEnable_Object = MibTableColumn
wfCctOptsIpFilterEnable = _WfCctOptsIpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 2),
    _WfCctOptsIpFilterEnable_Type()
)
wfCctOptsIpFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterEnable.setStatus("mandatory")


class _WfCctOptsIpFilterState_Type(Integer32):
    """Custom type wfCctOptsIpFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsIpFilterState_Type.__name__ = "Integer32"
_WfCctOptsIpFilterState_Object = MibTableColumn
wfCctOptsIpFilterState = _WfCctOptsIpFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 3),
    _WfCctOptsIpFilterState_Type()
)
wfCctOptsIpFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterState.setStatus("mandatory")
_WfCctOptsIpFilterCounter_Type = Counter32
_WfCctOptsIpFilterCounter_Object = MibTableColumn
wfCctOptsIpFilterCounter = _WfCctOptsIpFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 4),
    _WfCctOptsIpFilterCounter_Type()
)
wfCctOptsIpFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterCounter.setStatus("mandatory")
_WfCctOptsIpFilterDefinition_Type = OctetString
_WfCctOptsIpFilterDefinition_Object = MibTableColumn
wfCctOptsIpFilterDefinition = _WfCctOptsIpFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 5),
    _WfCctOptsIpFilterDefinition_Type()
)
wfCctOptsIpFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterDefinition.setStatus("mandatory")
_WfCctOptsIpFilterReserved_Type = Integer32
_WfCctOptsIpFilterReserved_Object = MibTableColumn
wfCctOptsIpFilterReserved = _WfCctOptsIpFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 6),
    _WfCctOptsIpFilterReserved_Type()
)
wfCctOptsIpFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterReserved.setStatus("mandatory")
_WfCctOptsIpFilterCct_Type = Integer32
_WfCctOptsIpFilterCct_Object = MibTableColumn
wfCctOptsIpFilterCct = _WfCctOptsIpFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 7),
    _WfCctOptsIpFilterCct_Type()
)
wfCctOptsIpFilterCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterCct.setStatus("mandatory")
_WfCctOptsIpFilterRuleNumber_Type = Integer32
_WfCctOptsIpFilterRuleNumber_Object = MibTableColumn
wfCctOptsIpFilterRuleNumber = _WfCctOptsIpFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 8),
    _WfCctOptsIpFilterRuleNumber_Type()
)
wfCctOptsIpFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterRuleNumber.setStatus("mandatory")
_WfCctOptsIpFilterFragment_Type = Integer32
_WfCctOptsIpFilterFragment_Object = MibTableColumn
wfCctOptsIpFilterFragment = _WfCctOptsIpFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 3, 1, 9),
    _WfCctOptsIpFilterFragment_Type()
)
wfCctOptsIpFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsIpFilterFragment.setStatus("mandatory")
_WfCctOptsLengthBasedTable_Object = MibTable
wfCctOptsLengthBasedTable = _WfCctOptsLengthBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedTable.setStatus("mandatory")
_WfCctOptsLengthBasedEntry_Object = MibTableRow
wfCctOptsLengthBasedEntry = _WfCctOptsLengthBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1)
)
wfCctOptsLengthBasedEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfCctOptsLengthBasedCct"),
    (0, "Wellfleet-Series7-MIB", "wfCctOptsLengthBasedMux"),
    (0, "Wellfleet-Series7-MIB", "wfCctOptsLengthBasedData"),
)
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedEntry.setStatus("mandatory")


class _WfCctOptsLengthBasedDelete_Type(Integer32):
    """Custom type wfCctOptsLengthBasedDelete based on Integer32"""
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


_WfCctOptsLengthBasedDelete_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedDelete_Object = MibTableColumn
wfCctOptsLengthBasedDelete = _WfCctOptsLengthBasedDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 1),
    _WfCctOptsLengthBasedDelete_Type()
)
wfCctOptsLengthBasedDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedDelete.setStatus("mandatory")


class _WfCctOptsLengthBasedDisable_Type(Integer32):
    """Custom type wfCctOptsLengthBasedDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfCctOptsLengthBasedDisable_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedDisable_Object = MibTableColumn
wfCctOptsLengthBasedDisable = _WfCctOptsLengthBasedDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 2),
    _WfCctOptsLengthBasedDisable_Type()
)
wfCctOptsLengthBasedDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedDisable.setStatus("mandatory")


class _WfCctOptsLengthBasedState_Type(Integer32):
    """Custom type wfCctOptsLengthBasedState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfCctOptsLengthBasedState_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedState_Object = MibTableColumn
wfCctOptsLengthBasedState = _WfCctOptsLengthBasedState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 3),
    _WfCctOptsLengthBasedState_Type()
)
wfCctOptsLengthBasedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedState.setStatus("mandatory")
_WfCctOptsLengthBasedCct_Type = Integer32
_WfCctOptsLengthBasedCct_Object = MibTableColumn
wfCctOptsLengthBasedCct = _WfCctOptsLengthBasedCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 4),
    _WfCctOptsLengthBasedCct_Type()
)
wfCctOptsLengthBasedCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedCct.setStatus("mandatory")


class _WfCctOptsLengthBasedMux_Type(Integer32):
    """Custom type wfCctOptsLengthBasedMux based on Integer32"""
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
        *(("etype", 1),
          ("lsap", 2),
          ("snap", 3))
    )


_WfCctOptsLengthBasedMux_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedMux_Object = MibTableColumn
wfCctOptsLengthBasedMux = _WfCctOptsLengthBasedMux_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 5),
    _WfCctOptsLengthBasedMux_Type()
)
wfCctOptsLengthBasedMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedMux.setStatus("mandatory")
_WfCctOptsLengthBasedData_Type = OctetString
_WfCctOptsLengthBasedData_Object = MibTableColumn
wfCctOptsLengthBasedData = _WfCctOptsLengthBasedData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 6),
    _WfCctOptsLengthBasedData_Type()
)
wfCctOptsLengthBasedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedData.setStatus("mandatory")
_WfCctOptsLengthBasedLength_Type = Integer32
_WfCctOptsLengthBasedLength_Object = MibTableColumn
wfCctOptsLengthBasedLength = _WfCctOptsLengthBasedLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 7),
    _WfCctOptsLengthBasedLength_Type()
)
wfCctOptsLengthBasedLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedLength.setStatus("mandatory")


class _WfCctOptsLengthBasedLessThanQ_Type(Integer32):
    """Custom type wfCctOptsLengthBasedLessThanQ based on Integer32"""
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
        *(("hi", 3),
          ("lo", 1),
          ("normal", 2))
    )


_WfCctOptsLengthBasedLessThanQ_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedLessThanQ_Object = MibTableColumn
wfCctOptsLengthBasedLessThanQ = _WfCctOptsLengthBasedLessThanQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 8),
    _WfCctOptsLengthBasedLessThanQ_Type()
)
wfCctOptsLengthBasedLessThanQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedLessThanQ.setStatus("mandatory")


class _WfCctOptsLengthBasedGreaterThanQ_Type(Integer32):
    """Custom type wfCctOptsLengthBasedGreaterThanQ based on Integer32"""
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
        *(("hi", 3),
          ("lo", 1),
          ("normal", 2))
    )


_WfCctOptsLengthBasedGreaterThanQ_Type.__name__ = "Integer32"
_WfCctOptsLengthBasedGreaterThanQ_Object = MibTableColumn
wfCctOptsLengthBasedGreaterThanQ = _WfCctOptsLengthBasedGreaterThanQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4, 4, 1, 9),
    _WfCctOptsLengthBasedGreaterThanQ_Type()
)
wfCctOptsLengthBasedGreaterThanQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCctOptsLengthBasedGreaterThanQ.setStatus("mandatory")
_WfDecGroup_ObjectIdentity = ObjectIdentity
wfDecGroup = _WfDecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2)
)
_WfivRouteGroup_ObjectIdentity = ObjectIdentity
wfivRouteGroup = _WfivRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1)
)


class _WfivRouteCreateDelete_Type(Integer32):
    """Custom type wfivRouteCreateDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfivRouteCreateDelete_Type.__name__ = "Integer32"
_WfivRouteCreateDelete_Object = MibScalar
wfivRouteCreateDelete = _WfivRouteCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 1),
    _WfivRouteCreateDelete_Type()
)
wfivRouteCreateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteCreateDelete.setStatus("mandatory")


class _WfivRouteEnableDisable_Type(Integer32):
    """Custom type wfivRouteEnableDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfivRouteEnableDisable_Type.__name__ = "Integer32"
_WfivRouteEnableDisable_Object = MibScalar
wfivRouteEnableDisable = _WfivRouteEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 2),
    _WfivRouteEnableDisable_Type()
)
wfivRouteEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteEnableDisable.setStatus("mandatory")


class _WfivRouteState_Type(Integer32):
    """Custom type wfivRouteState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("initializing", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfivRouteState_Type.__name__ = "Integer32"
_WfivRouteState_Object = MibScalar
wfivRouteState = _WfivRouteState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 3),
    _WfivRouteState_Type()
)
wfivRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteState.setStatus("mandatory")


class _WfivRouteBroadcastRouteTimer_Type(Integer32):
    """Custom type wfivRouteBroadcastRouteTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              180,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("routetimerdflt", 180),
          ("routetimermax", 65535),
          ("routetimermin", 1))
    )


_WfivRouteBroadcastRouteTimer_Type.__name__ = "Integer32"
_WfivRouteBroadcastRouteTimer_Object = MibScalar
wfivRouteBroadcastRouteTimer = _WfivRouteBroadcastRouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 4),
    _WfivRouteBroadcastRouteTimer_Type()
)
wfivRouteBroadcastRouteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteBroadcastRouteTimer.setStatus("mandatory")
_WfivRouteRoutingVers_Type = DisplayString
_WfivRouteRoutingVers_Object = MibScalar
wfivRouteRoutingVers = _WfivRouteRoutingVers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 5),
    _WfivRouteRoutingVers_Type()
)
wfivRouteRoutingVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteRoutingVers.setStatus("mandatory")


class _WfivRouteMaxAddr_Type(Integer32):
    """Custom type wfivRouteMaxAddr based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maxaddr", 1023),
          ("minaddr", 1))
    )


_WfivRouteMaxAddr_Type.__name__ = "Integer32"
_WfivRouteMaxAddr_Object = MibScalar
wfivRouteMaxAddr = _WfivRouteMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 6),
    _WfivRouteMaxAddr_Type()
)
wfivRouteMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxAddr.setStatus("mandatory")


class _WfivRouteMaxBdcastNonRouters_Type(Integer32):
    """Custom type wfivRouteMaxBdcastNonRouters based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("nonroutersdflt", 64),
          ("nonroutersmax", 1023))
    )


_WfivRouteMaxBdcastNonRouters_Type.__name__ = "Integer32"
_WfivRouteMaxBdcastNonRouters_Object = MibScalar
wfivRouteMaxBdcastNonRouters = _WfivRouteMaxBdcastNonRouters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 7),
    _WfivRouteMaxBdcastNonRouters_Type()
)
wfivRouteMaxBdcastNonRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxBdcastNonRouters.setStatus("mandatory")


class _WfivRouteMaxBdcastRouters_Type(Integer32):
    """Custom type wfivRouteMaxBdcastRouters based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("routersdflt", 32),
          ("routersdmax", 1023))
    )


_WfivRouteMaxBdcastRouters_Type.__name__ = "Integer32"
_WfivRouteMaxBdcastRouters_Object = MibScalar
wfivRouteMaxBdcastRouters = _WfivRouteMaxBdcastRouters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 8),
    _WfivRouteMaxBdcastRouters_Type()
)
wfivRouteMaxBdcastRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxBdcastRouters.setStatus("mandatory")


class _WfivRouteMaxCircuits_Type(Integer32):
    """Custom type wfivRouteMaxCircuits based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              1024,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("circuitsdflt", 16),
          ("circuitsmax", 65535),
          ("circuitsmin", 1),
          ("circuitswfmax", 1024))
    )


_WfivRouteMaxCircuits_Type.__name__ = "Integer32"
_WfivRouteMaxCircuits_Object = MibScalar
wfivRouteMaxCircuits = _WfivRouteMaxCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 9),
    _WfivRouteMaxCircuits_Type()
)
wfivRouteMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxCircuits.setStatus("mandatory")


class _WfivRouteMaxCost_Type(Integer32):
    """Custom type wfivRouteMaxCost based on Integer32"""
    defaultValue = 1022

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1022)
        )
    )
    namedValues = NamedValues(
        *(("maxcost", 1022),
          ("mincost", 1))
    )


_WfivRouteMaxCost_Type.__name__ = "Integer32"
_WfivRouteMaxCost_Object = MibScalar
wfivRouteMaxCost = _WfivRouteMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 10),
    _WfivRouteMaxCost_Type()
)
wfivRouteMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxCost.setStatus("mandatory")


class _WfivRouteMaxHops_Type(Integer32):
    """Custom type wfivRouteMaxHops based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              30)
        )
    )
    namedValues = NamedValues(
        *(("maxhops", 30),
          ("minhops", 1))
    )


_WfivRouteMaxHops_Type.__name__ = "Integer32"
_WfivRouteMaxHops_Object = MibScalar
wfivRouteMaxHops = _WfivRouteMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 11),
    _WfivRouteMaxHops_Type()
)
wfivRouteMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxHops.setStatus("mandatory")


class _WfivRouteMaxVisits_Type(Integer32):
    """Custom type wfivRouteMaxVisits based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            63
        )
    )
    namedValues = NamedValues(
        ("maxvisits", 63)
    )


_WfivRouteMaxVisits_Type.__name__ = "Integer32"
_WfivRouteMaxVisits_Object = MibScalar
wfivRouteMaxVisits = _WfivRouteMaxVisits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 12),
    _WfivRouteMaxVisits_Type()
)
wfivRouteMaxVisits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxVisits.setStatus("mandatory")


class _WfivRouteAreaMaxCost_Type(Integer32):
    """Custom type wfivRouteAreaMaxCost based on Integer32"""
    defaultValue = 1022

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1022)
        )
    )
    namedValues = NamedValues(
        *(("amaxcost", 1022),
          ("amincost", 1))
    )


_WfivRouteAreaMaxCost_Type.__name__ = "Integer32"
_WfivRouteAreaMaxCost_Object = MibScalar
wfivRouteAreaMaxCost = _WfivRouteAreaMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 13),
    _WfivRouteAreaMaxCost_Type()
)
wfivRouteAreaMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteAreaMaxCost.setStatus("mandatory")


class _WfivRouteAreaMaxHops_Type(Integer32):
    """Custom type wfivRouteAreaMaxHops based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              30)
        )
    )
    namedValues = NamedValues(
        *(("amaxhops", 30),
          ("aminhops", 1))
    )


_WfivRouteAreaMaxHops_Type.__name__ = "Integer32"
_WfivRouteAreaMaxHops_Object = MibScalar
wfivRouteAreaMaxHops = _WfivRouteAreaMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 14),
    _WfivRouteAreaMaxHops_Type()
)
wfivRouteAreaMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteAreaMaxHops.setStatus("mandatory")


class _WfivRouteMaxArea_Type(Integer32):
    """Custom type wfivRouteMaxArea based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              63)
        )
    )
    namedValues = NamedValues(
        *(("maxarea", 63),
          ("minarea", 1))
    )


_WfivRouteMaxArea_Type.__name__ = "Integer32"
_WfivRouteMaxArea_Object = MibScalar
wfivRouteMaxArea = _WfivRouteMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 15),
    _WfivRouteMaxArea_Type()
)
wfivRouteMaxArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxArea.setStatus("mandatory")


class _WfivRouteType_Type(Integer32):
    """Custom type wfivRouteType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("area", 3),
          ("nonroutingiv", 5),
          ("routingiv", 4))
    )


_WfivRouteType_Type.__name__ = "Integer32"
_WfivRouteType_Object = MibScalar
wfivRouteType = _WfivRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 16),
    _WfivRouteType_Type()
)
wfivRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteType.setStatus("mandatory")
_WfivCircuitTable_Object = MibTable
wfivCircuitTable = _WfivCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    wfivCircuitTable.setStatus("mandatory")
_WfivCircuitEntry_Object = MibTableRow
wfivCircuitEntry = _WfivCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1)
)
wfivCircuitEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfivCircuitID"),
)
if mibBuilder.loadTexts:
    wfivCircuitEntry.setStatus("mandatory")


class _WfivCircuitCreateDelete_Type(Integer32):
    """Custom type wfivCircuitCreateDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfivCircuitCreateDelete_Type.__name__ = "Integer32"
_WfivCircuitCreateDelete_Object = MibTableColumn
wfivCircuitCreateDelete = _WfivCircuitCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 1),
    _WfivCircuitCreateDelete_Type()
)
wfivCircuitCreateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitCreateDelete.setStatus("mandatory")


class _WfivCircuitEnableDisable_Type(Integer32):
    """Custom type wfivCircuitEnableDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfivCircuitEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitEnableDisable_Object = MibTableColumn
wfivCircuitEnableDisable = _WfivCircuitEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 2),
    _WfivCircuitEnableDisable_Type()
)
wfivCircuitEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitEnableDisable.setStatus("mandatory")


class _WfivCircuitCommonState_Type(Integer32):
    """Custom type wfivCircuitCommonState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("initializing", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfivCircuitCommonState_Type.__name__ = "Integer32"
_WfivCircuitCommonState_Object = MibTableColumn
wfivCircuitCommonState = _WfivCircuitCommonState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 3),
    _WfivCircuitCommonState_Type()
)
wfivCircuitCommonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCommonState.setStatus("mandatory")


class _WfivCircuitArea_Type(Integer32):
    """Custom type wfivCircuitArea based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              63)
        )
    )
    namedValues = NamedValues(
        *(("defarea", 1),
          ("maxarea", 63),
          ("minarea", 1))
    )


_WfivCircuitArea_Type.__name__ = "Integer32"
_WfivCircuitArea_Object = MibTableColumn
wfivCircuitArea = _WfivCircuitArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 4),
    _WfivCircuitArea_Type()
)
wfivCircuitArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitArea.setStatus("mandatory")


class _WfivCircuitNodeid_Type(Integer32):
    """Custom type wfivCircuitNodeid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("defnodeid", 1),
          ("maxnodeid", 1023),
          ("minnodeid", 1))
    )


_WfivCircuitNodeid_Type.__name__ = "Integer32"
_WfivCircuitNodeid_Object = MibTableColumn
wfivCircuitNodeid = _WfivCircuitNodeid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 5),
    _WfivCircuitNodeid_Type()
)
wfivCircuitNodeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitNodeid.setStatus("mandatory")
_WfivCircuitNodeAddr_Type = DisplayString
_WfivCircuitNodeAddr_Object = MibTableColumn
wfivCircuitNodeAddr = _WfivCircuitNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 6),
    _WfivCircuitNodeAddr_Type()
)
wfivCircuitNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitNodeAddr.setStatus("mandatory")
_WfivCircuitID_Type = Integer32
_WfivCircuitID_Object = MibTableColumn
wfivCircuitID = _WfivCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 7),
    _WfivCircuitID_Type()
)
wfivCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitID.setStatus("mandatory")


class _WfivCircuitCommonType_Type(Integer32):
    """Custom type wfivCircuitCommonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6,
              15,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 6),
          ("fddi", 15),
          ("fr", 101),
          ("smds", 100),
          ("sync", 1),
          ("x25", 4))
    )


_WfivCircuitCommonType_Type.__name__ = "Integer32"
_WfivCircuitCommonType_Object = MibTableColumn
wfivCircuitCommonType = _WfivCircuitCommonType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 8),
    _WfivCircuitCommonType_Type()
)
wfivCircuitCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCommonType.setStatus("mandatory")


class _WfivCircuitExecCost_Type(Integer32):
    """Custom type wfivCircuitExecCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              63)
        )
    )
    namedValues = NamedValues(
        *(("defcost", 10),
          ("maxcost", 63),
          ("mincost", 1))
    )


_WfivCircuitExecCost_Type.__name__ = "Integer32"
_WfivCircuitExecCost_Object = MibTableColumn
wfivCircuitExecCost = _WfivCircuitExecCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 9),
    _WfivCircuitExecCost_Type()
)
wfivCircuitExecCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitExecCost.setStatus("mandatory")


class _WfivCircuitExecHelloTimer_Type(Integer32):
    """Custom type wfivCircuitExecHelloTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              15,
              8191)
        )
    )
    namedValues = NamedValues(
        *(("hellodef", 15),
          ("hellomax", 8191),
          ("hellomin", 1))
    )


_WfivCircuitExecHelloTimer_Type.__name__ = "Integer32"
_WfivCircuitExecHelloTimer_Object = MibTableColumn
wfivCircuitExecHelloTimer = _WfivCircuitExecHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 10),
    _WfivCircuitExecHelloTimer_Type()
)
wfivCircuitExecHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitExecHelloTimer.setStatus("mandatory")
_WfivCircuitDesigRouterNodeAddr_Type = DisplayString
_WfivCircuitDesigRouterNodeAddr_Object = MibTableColumn
wfivCircuitDesigRouterNodeAddr = _WfivCircuitDesigRouterNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 11),
    _WfivCircuitDesigRouterNodeAddr_Type()
)
wfivCircuitDesigRouterNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitDesigRouterNodeAddr.setStatus("mandatory")


class _WfivCircuitMaxRouters_Type(Integer32):
    """Custom type wfivCircuitMaxRouters based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              33)
        )
    )
    namedValues = NamedValues(
        *(("maxroutersdef", 33),
          ("maxroutersmax", 33))
    )


_WfivCircuitMaxRouters_Type.__name__ = "Integer32"
_WfivCircuitMaxRouters_Object = MibTableColumn
wfivCircuitMaxRouters = _WfivCircuitMaxRouters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 12),
    _WfivCircuitMaxRouters_Type()
)
wfivCircuitMaxRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitMaxRouters.setStatus("mandatory")


class _WfivCircuitRouterPri_Type(Integer32):
    """Custom type wfivCircuitRouterPri based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              127)
        )
    )
    namedValues = NamedValues(
        *(("routerpridef", 64),
          ("routerprimax", 127))
    )


_WfivCircuitRouterPri_Type.__name__ = "Integer32"
_WfivCircuitRouterPri_Object = MibTableColumn
wfivCircuitRouterPri = _WfivCircuitRouterPri_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 13),
    _WfivCircuitRouterPri_Type()
)
wfivCircuitRouterPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitRouterPri.setStatus("mandatory")
_WfivCircuitCountAgedPktLoss_Type = Counter32
_WfivCircuitCountAgedPktLoss_Object = MibTableColumn
wfivCircuitCountAgedPktLoss = _WfivCircuitCountAgedPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 14),
    _WfivCircuitCountAgedPktLoss_Type()
)
wfivCircuitCountAgedPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountAgedPktLoss.setStatus("mandatory")
_WfivCircuitCountNodeUnrPktLoss_Type = Counter32
_WfivCircuitCountNodeUnrPktLoss_Object = MibTableColumn
wfivCircuitCountNodeUnrPktLoss = _WfivCircuitCountNodeUnrPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 15),
    _WfivCircuitCountNodeUnrPktLoss_Type()
)
wfivCircuitCountNodeUnrPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountNodeUnrPktLoss.setStatus("mandatory")
_WfivCircuitCountOutRngePktLoss_Type = Counter32
_WfivCircuitCountOutRngePktLoss_Object = MibTableColumn
wfivCircuitCountOutRngePktLoss = _WfivCircuitCountOutRngePktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 16),
    _WfivCircuitCountOutRngePktLoss_Type()
)
wfivCircuitCountOutRngePktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountOutRngePktLoss.setStatus("mandatory")
_WfivCircuitCountOverSzePktLoss_Type = Counter32
_WfivCircuitCountOverSzePktLoss_Object = MibTableColumn
wfivCircuitCountOverSzePktLoss = _WfivCircuitCountOverSzePktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 17),
    _WfivCircuitCountOverSzePktLoss_Type()
)
wfivCircuitCountOverSzePktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountOverSzePktLoss.setStatus("mandatory")
_WfivCircuitCountPacketFmtErr_Type = Counter32
_WfivCircuitCountPacketFmtErr_Object = MibTableColumn
wfivCircuitCountPacketFmtErr = _WfivCircuitCountPacketFmtErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 18),
    _WfivCircuitCountPacketFmtErr_Type()
)
wfivCircuitCountPacketFmtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountPacketFmtErr.setStatus("mandatory")
_WfivCircuitCountPtlRteUpdtLoss_Type = Counter32
_WfivCircuitCountPtlRteUpdtLoss_Object = MibTableColumn
wfivCircuitCountPtlRteUpdtLoss = _WfivCircuitCountPtlRteUpdtLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 19),
    _WfivCircuitCountPtlRteUpdtLoss_Type()
)
wfivCircuitCountPtlRteUpdtLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountPtlRteUpdtLoss.setStatus("mandatory")
_WfivCircuitCountTransitPksRecd_Type = Counter32
_WfivCircuitCountTransitPksRecd_Object = MibTableColumn
wfivCircuitCountTransitPksRecd = _WfivCircuitCountTransitPksRecd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 20),
    _WfivCircuitCountTransitPksRecd_Type()
)
wfivCircuitCountTransitPksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountTransitPksRecd.setStatus("mandatory")
_WfivCircuitCountTransitPkSent_Type = Counter32
_WfivCircuitCountTransitPkSent_Object = MibTableColumn
wfivCircuitCountTransitPkSent = _WfivCircuitCountTransitPkSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 21),
    _WfivCircuitCountTransitPkSent_Type()
)
wfivCircuitCountTransitPkSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountTransitPkSent.setStatus("mandatory")
_WfivCircuitCountRtHelloSent_Type = Counter32
_WfivCircuitCountRtHelloSent_Object = MibTableColumn
wfivCircuitCountRtHelloSent = _WfivCircuitCountRtHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 22),
    _WfivCircuitCountRtHelloSent_Type()
)
wfivCircuitCountRtHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountRtHelloSent.setStatus("mandatory")
_WfivCircuitCountRtHelloRcvd_Type = Counter32
_WfivCircuitCountRtHelloRcvd_Object = MibTableColumn
wfivCircuitCountRtHelloRcvd = _WfivCircuitCountRtHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 23),
    _WfivCircuitCountRtHelloRcvd_Type()
)
wfivCircuitCountRtHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountRtHelloRcvd.setStatus("mandatory")
_WfivCircuitCountHelloSent_Type = Counter32
_WfivCircuitCountHelloSent_Object = MibTableColumn
wfivCircuitCountHelloSent = _WfivCircuitCountHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 24),
    _WfivCircuitCountHelloSent_Type()
)
wfivCircuitCountHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountHelloSent.setStatus("mandatory")
_WfivCircuitCountHelloRcvd_Type = Counter32
_WfivCircuitCountHelloRcvd_Object = MibTableColumn
wfivCircuitCountHelloRcvd = _WfivCircuitCountHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 25),
    _WfivCircuitCountHelloRcvd_Type()
)
wfivCircuitCountHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountHelloRcvd.setStatus("mandatory")
_WfivCircuitCountL1UpdSent_Type = Counter32
_WfivCircuitCountL1UpdSent_Object = MibTableColumn
wfivCircuitCountL1UpdSent = _WfivCircuitCountL1UpdSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 26),
    _WfivCircuitCountL1UpdSent_Type()
)
wfivCircuitCountL1UpdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountL1UpdSent.setStatus("mandatory")
_WfivCircuitCountL1UpdRcvd_Type = Counter32
_WfivCircuitCountL1UpdRcvd_Object = MibTableColumn
wfivCircuitCountL1UpdRcvd = _WfivCircuitCountL1UpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 27),
    _WfivCircuitCountL1UpdRcvd_Type()
)
wfivCircuitCountL1UpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountL1UpdRcvd.setStatus("mandatory")
_WfivCircuitCountAreaUpdSent_Type = Counter32
_WfivCircuitCountAreaUpdSent_Object = MibTableColumn
wfivCircuitCountAreaUpdSent = _WfivCircuitCountAreaUpdSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 28),
    _WfivCircuitCountAreaUpdSent_Type()
)
wfivCircuitCountAreaUpdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountAreaUpdSent.setStatus("mandatory")
_WfivCircuitCountAreaUpdRcvd_Type = Counter32
_WfivCircuitCountAreaUpdRcvd_Object = MibTableColumn
wfivCircuitCountAreaUpdRcvd = _WfivCircuitCountAreaUpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 29),
    _WfivCircuitCountAreaUpdRcvd_Type()
)
wfivCircuitCountAreaUpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountAreaUpdRcvd.setStatus("mandatory")
_WfivCircuitCountDropped_Type = Counter32
_WfivCircuitCountDropped_Object = MibTableColumn
wfivCircuitCountDropped = _WfivCircuitCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 30),
    _WfivCircuitCountDropped_Type()
)
wfivCircuitCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountDropped.setStatus("mandatory")
_WfivCircuitAllEndnodesMac_Type = OctetString
_WfivCircuitAllEndnodesMac_Object = MibTableColumn
wfivCircuitAllEndnodesMac = _WfivCircuitAllEndnodesMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 31),
    _WfivCircuitAllEndnodesMac_Type()
)
wfivCircuitAllEndnodesMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitAllEndnodesMac.setStatus("mandatory")
_WfivCircuitAllRoutersMac_Type = OctetString
_WfivCircuitAllRoutersMac_Object = MibTableColumn
wfivCircuitAllRoutersMac = _WfivCircuitAllRoutersMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 32),
    _WfivCircuitAllRoutersMac_Type()
)
wfivCircuitAllRoutersMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitAllRoutersMac.setStatus("mandatory")
_WfivCircuitAllAreaRoutersMac_Type = OctetString
_WfivCircuitAllAreaRoutersMac_Object = MibTableColumn
wfivCircuitAllAreaRoutersMac = _WfivCircuitAllAreaRoutersMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 33),
    _WfivCircuitAllAreaRoutersMac_Type()
)
wfivCircuitAllAreaRoutersMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitAllAreaRoutersMac.setStatus("mandatory")


class _WfivCircuitHelloEnableDisable_Type(Integer32):
    """Custom type wfivCircuitHelloEnableDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfivCircuitHelloEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitHelloEnableDisable_Object = MibTableColumn
wfivCircuitHelloEnableDisable = _WfivCircuitHelloEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 34),
    _WfivCircuitHelloEnableDisable_Type()
)
wfivCircuitHelloEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitHelloEnableDisable.setStatus("mandatory")


class _WfivCircuitRtHelloEnableDisable_Type(Integer32):
    """Custom type wfivCircuitRtHelloEnableDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfivCircuitRtHelloEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitRtHelloEnableDisable_Object = MibTableColumn
wfivCircuitRtHelloEnableDisable = _WfivCircuitRtHelloEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 35),
    _WfivCircuitRtHelloEnableDisable_Type()
)
wfivCircuitRtHelloEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitRtHelloEnableDisable.setStatus("mandatory")


class _WfivCircuitL1UpdateEnableDisable_Type(Integer32):
    """Custom type wfivCircuitL1UpdateEnableDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfivCircuitL1UpdateEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitL1UpdateEnableDisable_Object = MibTableColumn
wfivCircuitL1UpdateEnableDisable = _WfivCircuitL1UpdateEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 36),
    _WfivCircuitL1UpdateEnableDisable_Type()
)
wfivCircuitL1UpdateEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitL1UpdateEnableDisable.setStatus("mandatory")
_WfivLevel1RouteTable_Object = MibTable
wfivLevel1RouteTable = _WfivLevel1RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3)
)
if mibBuilder.loadTexts:
    wfivLevel1RouteTable.setStatus("mandatory")
_WfivLevel1RouteEntry_Object = MibTableRow
wfivLevel1RouteEntry = _WfivLevel1RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1)
)
wfivLevel1RouteEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfivLevel1AreaId"),
    (0, "Wellfleet-Series7-MIB", "wfivLevel1NodeId"),
)
if mibBuilder.loadTexts:
    wfivLevel1RouteEntry.setStatus("mandatory")
_WfivLevel1AreaId_Type = Integer32
_WfivLevel1AreaId_Object = MibTableColumn
wfivLevel1AreaId = _WfivLevel1AreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 1),
    _WfivLevel1AreaId_Type()
)
wfivLevel1AreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1AreaId.setStatus("mandatory")
_WfivLevel1NodeId_Type = Integer32
_WfivLevel1NodeId_Object = MibTableColumn
wfivLevel1NodeId = _WfivLevel1NodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 2),
    _WfivLevel1NodeId_Type()
)
wfivLevel1NodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1NodeId.setStatus("mandatory")
_WfivLevel1RouteNodeAddr_Type = DisplayString
_WfivLevel1RouteNodeAddr_Object = MibTableColumn
wfivLevel1RouteNodeAddr = _WfivLevel1RouteNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 3),
    _WfivLevel1RouteNodeAddr_Type()
)
wfivLevel1RouteNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteNodeAddr.setStatus("mandatory")
_WfivLevel1RouteCircuitID_Type = Integer32
_WfivLevel1RouteCircuitID_Object = MibTableColumn
wfivLevel1RouteCircuitID = _WfivLevel1RouteCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 4),
    _WfivLevel1RouteCircuitID_Type()
)
wfivLevel1RouteCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteCircuitID.setStatus("mandatory")
_WfivLevel1RouteCost_Type = Integer32
_WfivLevel1RouteCost_Object = MibTableColumn
wfivLevel1RouteCost = _WfivLevel1RouteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 5),
    _WfivLevel1RouteCost_Type()
)
wfivLevel1RouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteCost.setStatus("mandatory")
_WfivLevel1RouteHops_Type = Integer32
_WfivLevel1RouteHops_Object = MibTableColumn
wfivLevel1RouteHops = _WfivLevel1RouteHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 6),
    _WfivLevel1RouteHops_Type()
)
wfivLevel1RouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteHops.setStatus("mandatory")
_WfivLevel1RouteNextNode_Type = DisplayString
_WfivLevel1RouteNextNode_Object = MibTableColumn
wfivLevel1RouteNextNode = _WfivLevel1RouteNextNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 7),
    _WfivLevel1RouteNextNode_Type()
)
wfivLevel1RouteNextNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteNextNode.setStatus("mandatory")
_WfivAreaTable_Object = MibTable
wfivAreaTable = _WfivAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    wfivAreaTable.setStatus("mandatory")
_WfivAreaEntry_Object = MibTableRow
wfivAreaEntry = _WfivAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1)
)
wfivAreaEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfivAreaNum"),
)
if mibBuilder.loadTexts:
    wfivAreaEntry.setStatus("mandatory")
_WfivAreaNum_Type = Integer32
_WfivAreaNum_Object = MibTableColumn
wfivAreaNum = _WfivAreaNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 1),
    _WfivAreaNum_Type()
)
wfivAreaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaNum.setStatus("mandatory")


class _WfivAreaState_Type(Integer32):
    """Custom type wfivAreaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 4),
          ("unreachable", 5))
    )


_WfivAreaState_Type.__name__ = "Integer32"
_WfivAreaState_Object = MibTableColumn
wfivAreaState = _WfivAreaState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 2),
    _WfivAreaState_Type()
)
wfivAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaState.setStatus("mandatory")
_WfivAreaCost_Type = Integer32
_WfivAreaCost_Object = MibTableColumn
wfivAreaCost = _WfivAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 3),
    _WfivAreaCost_Type()
)
wfivAreaCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaCost.setStatus("mandatory")
_WfivAreaHops_Type = Integer32
_WfivAreaHops_Object = MibTableColumn
wfivAreaHops = _WfivAreaHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 4),
    _WfivAreaHops_Type()
)
wfivAreaHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaHops.setStatus("mandatory")
_WfivAreaCircuitID_Type = Integer32
_WfivAreaCircuitID_Object = MibTableColumn
wfivAreaCircuitID = _WfivAreaCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 5),
    _WfivAreaCircuitID_Type()
)
wfivAreaCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaCircuitID.setStatus("mandatory")
_WfivAreaNextNode_Type = DisplayString
_WfivAreaNextNode_Object = MibTableColumn
wfivAreaNextNode = _WfivAreaNextNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 6),
    _WfivAreaNextNode_Type()
)
wfivAreaNextNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaNextNode.setStatus("mandatory")
_WfivAdjTable_Object = MibTable
wfivAdjTable = _WfivAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5)
)
if mibBuilder.loadTexts:
    wfivAdjTable.setStatus("mandatory")
_WfivAdjEntry_Object = MibTableRow
wfivAdjEntry = _WfivAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1)
)
wfivAdjEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfivAdjIndex"),
)
if mibBuilder.loadTexts:
    wfivAdjEntry.setStatus("mandatory")
_WfivAdjIndex_Type = Integer32
_WfivAdjIndex_Object = MibTableColumn
wfivAdjIndex = _WfivAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 1),
    _WfivAdjIndex_Type()
)
wfivAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjIndex.setStatus("mandatory")
_WfivAdjNodeAddr_Type = DisplayString
_WfivAdjNodeAddr_Object = MibTableColumn
wfivAdjNodeAddr = _WfivAdjNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 2),
    _WfivAdjNodeAddr_Type()
)
wfivAdjNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjNodeAddr.setStatus("mandatory")
_WfivAdjBlockSize_Type = Integer32
_WfivAdjBlockSize_Object = MibTableColumn
wfivAdjBlockSize = _WfivAdjBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 3),
    _WfivAdjBlockSize_Type()
)
wfivAdjBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjBlockSize.setStatus("mandatory")
_WfivAdjListenTimer_Type = Integer32
_WfivAdjListenTimer_Object = MibTableColumn
wfivAdjListenTimer = _WfivAdjListenTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 4),
    _WfivAdjListenTimer_Type()
)
wfivAdjListenTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjListenTimer.setStatus("mandatory")
_WfivAdjCircuitID_Type = Integer32
_WfivAdjCircuitID_Object = MibTableColumn
wfivAdjCircuitID = _WfivAdjCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 5),
    _WfivAdjCircuitID_Type()
)
wfivAdjCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjCircuitID.setStatus("mandatory")
_WfivAdjType_Type = Integer32
_WfivAdjType_Object = MibTableColumn
wfivAdjType = _WfivAdjType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 6),
    _WfivAdjType_Type()
)
wfivAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjType.setStatus("mandatory")


class _WfivAdjState_Type(Integer32):
    """Custom type wfivAdjState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("up", 2))
    )


_WfivAdjState_Type.__name__ = "Integer32"
_WfivAdjState_Object = MibTableColumn
wfivAdjState = _WfivAdjState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 7),
    _WfivAdjState_Type()
)
wfivAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjState.setStatus("mandatory")
_WfivAdjPriority_Type = Integer32
_WfivAdjPriority_Object = MibTableColumn
wfivAdjPriority = _WfivAdjPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 8),
    _WfivAdjPriority_Type()
)
wfivAdjPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjPriority.setStatus("mandatory")
_WfivAdjClass_Type = Integer32
_WfivAdjClass_Object = MibTableColumn
wfivAdjClass = _WfivAdjClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 9),
    _WfivAdjClass_Type()
)
wfivAdjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjClass.setStatus("mandatory")
_WfivTrafficFilterTable_Object = MibTable
wfivTrafficFilterTable = _WfivTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6)
)
if mibBuilder.loadTexts:
    wfivTrafficFilterTable.setStatus("mandatory")
_WfivTrafficFilterEntry_Object = MibTableRow
wfivTrafficFilterEntry = _WfivTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1)
)
wfivTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfivTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfivTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfivTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfivTrafficFilterEntry.setStatus("mandatory")


class _WfivTrafficFilterCreate_Type(Integer32):
    """Custom type wfivTrafficFilterCreate based on Integer32"""
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


_WfivTrafficFilterCreate_Type.__name__ = "Integer32"
_WfivTrafficFilterCreate_Object = MibTableColumn
wfivTrafficFilterCreate = _WfivTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 1),
    _WfivTrafficFilterCreate_Type()
)
wfivTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterCreate.setStatus("mandatory")


class _WfivTrafficFilterEnable_Type(Integer32):
    """Custom type wfivTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfivTrafficFilterEnable_Type.__name__ = "Integer32"
_WfivTrafficFilterEnable_Object = MibTableColumn
wfivTrafficFilterEnable = _WfivTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 2),
    _WfivTrafficFilterEnable_Type()
)
wfivTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterEnable.setStatus("mandatory")


class _WfivTrafficFilterStatus_Type(Integer32):
    """Custom type wfivTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfivTrafficFilterStatus_Type.__name__ = "Integer32"
_WfivTrafficFilterStatus_Object = MibTableColumn
wfivTrafficFilterStatus = _WfivTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 3),
    _WfivTrafficFilterStatus_Type()
)
wfivTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterStatus.setStatus("mandatory")
_WfivTrafficFilterCounter_Type = Counter32
_WfivTrafficFilterCounter_Object = MibTableColumn
wfivTrafficFilterCounter = _WfivTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 4),
    _WfivTrafficFilterCounter_Type()
)
wfivTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterCounter.setStatus("mandatory")
_WfivTrafficFilterDefinition_Type = Opaque
_WfivTrafficFilterDefinition_Object = MibTableColumn
wfivTrafficFilterDefinition = _WfivTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 5),
    _WfivTrafficFilterDefinition_Type()
)
wfivTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterDefinition.setStatus("mandatory")
_WfivTrafficFilterReserved_Type = Integer32
_WfivTrafficFilterReserved_Object = MibTableColumn
wfivTrafficFilterReserved = _WfivTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 6),
    _WfivTrafficFilterReserved_Type()
)
wfivTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfivTrafficFilterReserved.setStatus("mandatory")
_WfivTrafficFilterCircuit_Type = Integer32
_WfivTrafficFilterCircuit_Object = MibTableColumn
wfivTrafficFilterCircuit = _WfivTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 7),
    _WfivTrafficFilterCircuit_Type()
)
wfivTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterCircuit.setStatus("mandatory")
_WfivTrafficFilterRuleNumber_Type = Integer32
_WfivTrafficFilterRuleNumber_Object = MibTableColumn
wfivTrafficFilterRuleNumber = _WfivTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 8),
    _WfivTrafficFilterRuleNumber_Type()
)
wfivTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterRuleNumber.setStatus("mandatory")
_WfivTrafficFilterFragment_Type = Integer32
_WfivTrafficFilterFragment_Object = MibTableColumn
wfivTrafficFilterFragment = _WfivTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 9),
    _WfivTrafficFilterFragment_Type()
)
wfivTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterFragment.setStatus("mandatory")
_WfivStaticAdjTable_Object = MibTable
wfivStaticAdjTable = _WfivStaticAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7)
)
if mibBuilder.loadTexts:
    wfivStaticAdjTable.setStatus("mandatory")
_WfivStaticAdjEntry_Object = MibTableRow
wfivStaticAdjEntry = _WfivStaticAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1)
)
wfivStaticAdjEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfivStaticAdjCircuitID"),
    (0, "Wellfleet-Series7-MIB", "wfivStaticAdjArea"),
    (0, "Wellfleet-Series7-MIB", "wfivStaticAdjNodeid"),
)
if mibBuilder.loadTexts:
    wfivStaticAdjEntry.setStatus("mandatory")


class _WfivStaticAdjCreateDelete_Type(Integer32):
    """Custom type wfivStaticAdjCreateDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfivStaticAdjCreateDelete_Type.__name__ = "Integer32"
_WfivStaticAdjCreateDelete_Object = MibTableColumn
wfivStaticAdjCreateDelete = _WfivStaticAdjCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 1),
    _WfivStaticAdjCreateDelete_Type()
)
wfivStaticAdjCreateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjCreateDelete.setStatus("mandatory")


class _WfivStaticAdjEnableDisable_Type(Integer32):
    """Custom type wfivStaticAdjEnableDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfivStaticAdjEnableDisable_Type.__name__ = "Integer32"
_WfivStaticAdjEnableDisable_Object = MibTableColumn
wfivStaticAdjEnableDisable = _WfivStaticAdjEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 2),
    _WfivStaticAdjEnableDisable_Type()
)
wfivStaticAdjEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjEnableDisable.setStatus("mandatory")
_WfivStaticAdjArea_Type = Integer32
_WfivStaticAdjArea_Object = MibTableColumn
wfivStaticAdjArea = _WfivStaticAdjArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 3),
    _WfivStaticAdjArea_Type()
)
wfivStaticAdjArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjArea.setStatus("mandatory")
_WfivStaticAdjNodeid_Type = Integer32
_WfivStaticAdjNodeid_Object = MibTableColumn
wfivStaticAdjNodeid = _WfivStaticAdjNodeid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 4),
    _WfivStaticAdjNodeid_Type()
)
wfivStaticAdjNodeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjNodeid.setStatus("mandatory")
_WfivStaticAdjCircuitID_Type = Integer32
_WfivStaticAdjCircuitID_Object = MibTableColumn
wfivStaticAdjCircuitID = _WfivStaticAdjCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 5),
    _WfivStaticAdjCircuitID_Type()
)
wfivStaticAdjCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjCircuitID.setStatus("mandatory")
_WfivStaticAdjNodeAddr_Type = DisplayString
_WfivStaticAdjNodeAddr_Object = MibTableColumn
wfivStaticAdjNodeAddr = _WfivStaticAdjNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 6),
    _WfivStaticAdjNodeAddr_Type()
)
wfivStaticAdjNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjNodeAddr.setStatus("mandatory")


class _WfivStaticAdjType_Type(Integer32):
    """Custom type wfivStaticAdjType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("area", 3),
          ("nonroutingiv", 5),
          ("routingiv", 4))
    )


_WfivStaticAdjType_Type.__name__ = "Integer32"
_WfivStaticAdjType_Object = MibTableColumn
wfivStaticAdjType = _WfivStaticAdjType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 7),
    _WfivStaticAdjType_Type()
)
wfivStaticAdjType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjType.setStatus("mandatory")
_WfivStaticAdjPriority_Type = Integer32
_WfivStaticAdjPriority_Object = MibTableColumn
wfivStaticAdjPriority = _WfivStaticAdjPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 8),
    _WfivStaticAdjPriority_Type()
)
wfivStaticAdjPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjPriority.setStatus("mandatory")
_WfivStaticAdjDestMACAddr_Type = OctetString
_WfivStaticAdjDestMACAddr_Object = MibTableColumn
wfivStaticAdjDestMACAddr = _WfivStaticAdjDestMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 9),
    _WfivStaticAdjDestMACAddr_Type()
)
wfivStaticAdjDestMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjDestMACAddr.setStatus("mandatory")
_WfInternet_ObjectIdentity = ObjectIdentity
wfInternet = _WfInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3)
)
_WfArpGroup_ObjectIdentity = ObjectIdentity
wfArpGroup = _WfArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1)
)
_WfArpBase_ObjectIdentity = ObjectIdentity
wfArpBase = _WfArpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1)
)


class _WfArpBaseCreate_Type(Integer32):
    """Custom type wfArpBaseCreate based on Integer32"""
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


_WfArpBaseCreate_Type.__name__ = "Integer32"
_WfArpBaseCreate_Object = MibScalar
wfArpBaseCreate = _WfArpBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 1),
    _WfArpBaseCreate_Type()
)
wfArpBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseCreate.setStatus("mandatory")


class _WfArpBaseEnable_Type(Integer32):
    """Custom type wfArpBaseEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfArpBaseEnable_Type.__name__ = "Integer32"
_WfArpBaseEnable_Object = MibScalar
wfArpBaseEnable = _WfArpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 2),
    _WfArpBaseEnable_Type()
)
wfArpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseEnable.setStatus("mandatory")


class _WfArpBaseForwarding_Type(Integer32):
    """Custom type wfArpBaseForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_WfArpBaseForwarding_Type.__name__ = "Integer32"
_WfArpBaseForwarding_Object = MibScalar
wfArpBaseForwarding = _WfArpBaseForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 1, 3),
    _WfArpBaseForwarding_Type()
)
wfArpBaseForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpBaseForwarding.setStatus("mandatory")
_WfArpIntfTable_Object = MibTable
wfArpIntfTable = _WfArpIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wfArpIntfTable.setStatus("mandatory")
_WfArpIntfEntry_Object = MibTableRow
wfArpIntfEntry = _WfArpIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1)
)
wfArpIntfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfArpCctno"),
)
if mibBuilder.loadTexts:
    wfArpIntfEntry.setStatus("mandatory")


class _WfArpCreate_Type(Integer32):
    """Custom type wfArpCreate based on Integer32"""
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


_WfArpCreate_Type.__name__ = "Integer32"
_WfArpCreate_Object = MibTableColumn
wfArpCreate = _WfArpCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1, 1),
    _WfArpCreate_Type()
)
wfArpCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpCreate.setStatus("mandatory")


class _WfArpEnable_Type(Integer32):
    """Custom type wfArpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfArpEnable_Type.__name__ = "Integer32"
_WfArpEnable_Object = MibTableColumn
wfArpEnable = _WfArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1, 2),
    _WfArpEnable_Type()
)
wfArpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArpEnable.setStatus("mandatory")
_WfArpCctno_Type = Integer32
_WfArpCctno_Object = MibTableColumn
wfArpCctno = _WfArpCctno_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1, 2, 1, 3),
    _WfArpCctno_Type()
)
wfArpCctno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfArpCctno.setStatus("mandatory")
_WfIpRouting_ObjectIdentity = ObjectIdentity
wfIpRouting = _WfIpRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2)
)
_WfIpGroup_ObjectIdentity = ObjectIdentity
wfIpGroup = _WfIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1)
)
_WfIpBase_ObjectIdentity = ObjectIdentity
wfIpBase = _WfIpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1)
)


class _WfIpBaseCreate_Type(Integer32):
    """Custom type wfIpBaseCreate based on Integer32"""
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


_WfIpBaseCreate_Type.__name__ = "Integer32"
_WfIpBaseCreate_Object = MibScalar
wfIpBaseCreate = _WfIpBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 1),
    _WfIpBaseCreate_Type()
)
wfIpBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseCreate.setStatus("mandatory")


class _WfIpBaseEnable_Type(Integer32):
    """Custom type wfIpBaseEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpBaseEnable_Type.__name__ = "Integer32"
_WfIpBaseEnable_Object = MibScalar
wfIpBaseEnable = _WfIpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 2),
    _WfIpBaseEnable_Type()
)
wfIpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseEnable.setStatus("mandatory")


class _WfIpBaseState_Type(Integer32):
    """Custom type wfIpBaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfIpBaseState_Type.__name__ = "Integer32"
_WfIpBaseState_Object = MibScalar
wfIpBaseState = _WfIpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 3),
    _WfIpBaseState_Type()
)
wfIpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseState.setStatus("mandatory")


class _WfIpBaseForwarding_Type(Integer32):
    """Custom type wfIpBaseForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_WfIpBaseForwarding_Type.__name__ = "Integer32"
_WfIpBaseForwarding_Object = MibScalar
wfIpBaseForwarding = _WfIpBaseForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 4),
    _WfIpBaseForwarding_Type()
)
wfIpBaseForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseForwarding.setStatus("mandatory")


class _WfIpBaseDefaultTTL_Type(Integer32):
    """Custom type wfIpBaseDefaultTTL based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 30),
          ("ttlmax", 255))
    )


_WfIpBaseDefaultTTL_Type.__name__ = "Integer32"
_WfIpBaseDefaultTTL_Object = MibScalar
wfIpBaseDefaultTTL = _WfIpBaseDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 5),
    _WfIpBaseDefaultTTL_Type()
)
wfIpBaseDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDefaultTTL.setStatus("mandatory")


class _WfIpBaseRipDiameter_Type(Integer32):
    """Custom type wfIpBaseRipDiameter based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dflt", 15),
          ("maximum", 15))
    )


_WfIpBaseRipDiameter_Type.__name__ = "Integer32"
_WfIpBaseRipDiameter_Object = MibScalar
wfIpBaseRipDiameter = _WfIpBaseRipDiameter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 6),
    _WfIpBaseRipDiameter_Type()
)
wfIpBaseRipDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRipDiameter.setStatus("mandatory")
_WfIpBaseRtEntryTable_Object = MibTable
wfIpBaseRtEntryTable = _WfIpBaseRtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wfIpBaseRtEntryTable.setStatus("mandatory")
_WfIpBaseRtEntry_Object = MibTableRow
wfIpBaseRtEntry = _WfIpBaseRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1)
)
wfIpBaseRtEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpBaseRouteDest"),
)
if mibBuilder.loadTexts:
    wfIpBaseRtEntry.setStatus("mandatory")
_WfIpBaseRouteDest_Type = IpAddress
_WfIpBaseRouteDest_Object = MibTableColumn
wfIpBaseRouteDest = _WfIpBaseRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 1),
    _WfIpBaseRouteDest_Type()
)
wfIpBaseRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteDest.setStatus("mandatory")
_WfIpBaseRouteIfIndex_Type = Integer32
_WfIpBaseRouteIfIndex_Object = MibTableColumn
wfIpBaseRouteIfIndex = _WfIpBaseRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 2),
    _WfIpBaseRouteIfIndex_Type()
)
wfIpBaseRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteIfIndex.setStatus("mandatory")
_WfIpBaseRouteMetric1_Type = Integer32
_WfIpBaseRouteMetric1_Object = MibTableColumn
wfIpBaseRouteMetric1 = _WfIpBaseRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 3),
    _WfIpBaseRouteMetric1_Type()
)
wfIpBaseRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric1.setStatus("mandatory")
_WfIpBaseRouteMetric2_Type = Integer32
_WfIpBaseRouteMetric2_Object = MibTableColumn
wfIpBaseRouteMetric2 = _WfIpBaseRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 4),
    _WfIpBaseRouteMetric2_Type()
)
wfIpBaseRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric2.setStatus("mandatory")
_WfIpBaseRouteMetric3_Type = Integer32
_WfIpBaseRouteMetric3_Object = MibTableColumn
wfIpBaseRouteMetric3 = _WfIpBaseRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 5),
    _WfIpBaseRouteMetric3_Type()
)
wfIpBaseRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric3.setStatus("mandatory")
_WfIpBaseRouteMetric4_Type = Integer32
_WfIpBaseRouteMetric4_Object = MibTableColumn
wfIpBaseRouteMetric4 = _WfIpBaseRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 6),
    _WfIpBaseRouteMetric4_Type()
)
wfIpBaseRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric4.setStatus("mandatory")
_WfIpBaseRouteNextHop_Type = IpAddress
_WfIpBaseRouteNextHop_Object = MibTableColumn
wfIpBaseRouteNextHop = _WfIpBaseRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 7),
    _WfIpBaseRouteNextHop_Type()
)
wfIpBaseRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteNextHop.setStatus("mandatory")


class _WfIpBaseRouteType_Type(Integer32):
    """Custom type wfIpBaseRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_WfIpBaseRouteType_Type.__name__ = "Integer32"
_WfIpBaseRouteType_Object = MibTableColumn
wfIpBaseRouteType = _WfIpBaseRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 8),
    _WfIpBaseRouteType_Type()
)
wfIpBaseRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteType.setStatus("mandatory")


class _WfIpBaseRouteProto_Type(Integer32):
    """Custom type wfIpBaseRouteProto based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 14),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_WfIpBaseRouteProto_Type.__name__ = "Integer32"
_WfIpBaseRouteProto_Object = MibTableColumn
wfIpBaseRouteProto = _WfIpBaseRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 9),
    _WfIpBaseRouteProto_Type()
)
wfIpBaseRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteProto.setStatus("mandatory")
_WfIpBaseRouteAge_Type = Integer32
_WfIpBaseRouteAge_Object = MibTableColumn
wfIpBaseRouteAge = _WfIpBaseRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 10),
    _WfIpBaseRouteAge_Type()
)
wfIpBaseRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteAge.setStatus("mandatory")
_WfIpBaseRouteMask_Type = IpAddress
_WfIpBaseRouteMask_Object = MibTableColumn
wfIpBaseRouteMask = _WfIpBaseRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 11),
    _WfIpBaseRouteMask_Type()
)
wfIpBaseRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMask.setStatus("mandatory")
_WfIpBaseRouteMetric5_Type = Integer32
_WfIpBaseRouteMetric5_Object = MibTableColumn
wfIpBaseRouteMetric5 = _WfIpBaseRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 12),
    _WfIpBaseRouteMetric5_Type()
)
wfIpBaseRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric5.setStatus("mandatory")
_WfIpBaseRouteInfo_Type = ObjectIdentifier
_WfIpBaseRouteInfo_Object = MibTableColumn
wfIpBaseRouteInfo = _WfIpBaseRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 13),
    _WfIpBaseRouteInfo_Type()
)
wfIpBaseRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteInfo.setStatus("mandatory")
_WfIpBaseHostEntryTable_Object = MibTable
wfIpBaseHostEntryTable = _WfIpBaseHostEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wfIpBaseHostEntryTable.setStatus("mandatory")
_WfIpBaseHostEntry_Object = MibTableRow
wfIpBaseHostEntry = _WfIpBaseHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1)
)
wfIpBaseHostEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpBaseNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    wfIpBaseHostEntry.setStatus("mandatory")
_WfIpBaseNetToMediaIfIndex_Type = Integer32
_WfIpBaseNetToMediaIfIndex_Object = MibTableColumn
wfIpBaseNetToMediaIfIndex = _WfIpBaseNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 1),
    _WfIpBaseNetToMediaIfIndex_Type()
)
wfIpBaseNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaIfIndex.setStatus("mandatory")
_WfIpBaseNetToMediaPhysAddress_Type = OctetString
_WfIpBaseNetToMediaPhysAddress_Object = MibTableColumn
wfIpBaseNetToMediaPhysAddress = _WfIpBaseNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 2),
    _WfIpBaseNetToMediaPhysAddress_Type()
)
wfIpBaseNetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaPhysAddress.setStatus("mandatory")
_WfIpBaseNetToMediaNetAddress_Type = IpAddress
_WfIpBaseNetToMediaNetAddress_Object = MibTableColumn
wfIpBaseNetToMediaNetAddress = _WfIpBaseNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 3),
    _WfIpBaseNetToMediaNetAddress_Type()
)
wfIpBaseNetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaNetAddress.setStatus("mandatory")


class _WfIpBaseNetToMediaType_Type(Integer32):
    """Custom type wfIpBaseNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_WfIpBaseNetToMediaType_Type.__name__ = "Integer32"
_WfIpBaseNetToMediaType_Object = MibTableColumn
wfIpBaseNetToMediaType = _WfIpBaseNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 4),
    _WfIpBaseNetToMediaType_Type()
)
wfIpBaseNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaType.setStatus("mandatory")
_WfIpInterfaceTable_Object = MibTable
wfIpInterfaceTable = _WfIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    wfIpInterfaceTable.setStatus("mandatory")
_WfIpInterfaceEntry_Object = MibTableRow
wfIpInterfaceEntry = _WfIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1)
)
wfIpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpInterfaceAddr"),
    (0, "Wellfleet-Series7-MIB", "wfIpInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfIpInterfaceEntry.setStatus("mandatory")


class _WfIpInterfaceCreate_Type(Integer32):
    """Custom type wfIpInterfaceCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpInterfaceCreate_Type.__name__ = "Integer32"
_WfIpInterfaceCreate_Object = MibTableColumn
wfIpInterfaceCreate = _WfIpInterfaceCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 1),
    _WfIpInterfaceCreate_Type()
)
wfIpInterfaceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCreate.setStatus("mandatory")


class _WfIpInterfaceEnable_Type(Integer32):
    """Custom type wfIpInterfaceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpInterfaceEnable_Type.__name__ = "Integer32"
_WfIpInterfaceEnable_Object = MibTableColumn
wfIpInterfaceEnable = _WfIpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 2),
    _WfIpInterfaceEnable_Type()
)
wfIpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceEnable.setStatus("mandatory")


class _WfIpInterfaceState_Type(Integer32):
    """Custom type wfIpInterfaceState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfIpInterfaceState_Type.__name__ = "Integer32"
_WfIpInterfaceState_Object = MibTableColumn
wfIpInterfaceState = _WfIpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 3),
    _WfIpInterfaceState_Type()
)
wfIpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceState.setStatus("mandatory")
_WfIpInterfaceAddr_Type = IpAddress
_WfIpInterfaceAddr_Object = MibTableColumn
wfIpInterfaceAddr = _WfIpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 4),
    _WfIpInterfaceAddr_Type()
)
wfIpInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAddr.setStatus("mandatory")
_WfIpInterfaceCircuit_Type = Integer32
_WfIpInterfaceCircuit_Object = MibTableColumn
wfIpInterfaceCircuit = _WfIpInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 5),
    _WfIpInterfaceCircuit_Type()
)
wfIpInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceCircuit.setStatus("mandatory")
_WfIpInterfaceMask_Type = IpAddress
_WfIpInterfaceMask_Object = MibTableColumn
wfIpInterfaceMask = _WfIpInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 6),
    _WfIpInterfaceMask_Type()
)
wfIpInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMask.setStatus("mandatory")


class _WfIpInterfaceCost_Type(Integer32):
    """Custom type wfIpInterfaceCost based on Integer32"""
    defaultValue = 1


_WfIpInterfaceCost_Object = MibTableColumn
wfIpInterfaceCost = _WfIpInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 7),
    _WfIpInterfaceCost_Type()
)
wfIpInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCost.setStatus("mandatory")
_WfIpInterfaceCfgBcastAddr_Type = IpAddress
_WfIpInterfaceCfgBcastAddr_Object = MibTableColumn
wfIpInterfaceCfgBcastAddr = _WfIpInterfaceCfgBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 8),
    _WfIpInterfaceCfgBcastAddr_Type()
)
wfIpInterfaceCfgBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCfgBcastAddr.setStatus("mandatory")
_WfIpInterfaceBcastAddr_Type = IpAddress
_WfIpInterfaceBcastAddr_Object = MibTableColumn
wfIpInterfaceBcastAddr = _WfIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 9),
    _WfIpInterfaceBcastAddr_Type()
)
wfIpInterfaceBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceBcastAddr.setStatus("mandatory")


class _WfIpInterfaceMTUDiscovery_Type(Integer32):
    """Custom type wfIpInterfaceMTUDiscovery based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceMTUDiscovery_Type.__name__ = "Integer32"
_WfIpInterfaceMTUDiscovery_Object = MibTableColumn
wfIpInterfaceMTUDiscovery = _WfIpInterfaceMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 10),
    _WfIpInterfaceMTUDiscovery_Type()
)
wfIpInterfaceMTUDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMTUDiscovery.setStatus("mandatory")


class _WfIpInterfaceAMR_Type(Integer32):
    """Custom type wfIpInterfaceAMR based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceAMR_Type.__name__ = "Integer32"
_WfIpInterfaceAMR_Object = MibTableColumn
wfIpInterfaceAMR = _WfIpInterfaceAMR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 11),
    _WfIpInterfaceAMR_Type()
)
wfIpInterfaceAMR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAMR.setStatus("mandatory")


class _WfIpInterfaceASB_Type(Integer32):
    """Custom type wfIpInterfaceASB based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceASB_Type.__name__ = "Integer32"
_WfIpInterfaceASB_Object = MibTableColumn
wfIpInterfaceASB = _WfIpInterfaceASB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 12),
    _WfIpInterfaceASB_Type()
)
wfIpInterfaceASB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceASB.setStatus("mandatory")


class _WfIpInterfaceAddressResolutionType_Type(Integer32):
    """Custom type wfIpInterfaceAddressResolutionType based on Integer32"""
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
        *(("arp", 1),
          ("arpinarp", 6),
          ("ddn", 3),
          ("inarp", 5),
          ("pdn", 4),
          ("probe", 2))
    )


_WfIpInterfaceAddressResolutionType_Type.__name__ = "Integer32"
_WfIpInterfaceAddressResolutionType_Object = MibTableColumn
wfIpInterfaceAddressResolutionType = _WfIpInterfaceAddressResolutionType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 13),
    _WfIpInterfaceAddressResolutionType_Type()
)
wfIpInterfaceAddressResolutionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAddressResolutionType.setStatus("mandatory")


class _WfIpInterfaceProxy_Type(Integer32):
    """Custom type wfIpInterfaceProxy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceProxy_Type.__name__ = "Integer32"
_WfIpInterfaceProxy_Object = MibTableColumn
wfIpInterfaceProxy = _WfIpInterfaceProxy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 14),
    _WfIpInterfaceProxy_Type()
)
wfIpInterfaceProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceProxy.setStatus("mandatory")


class _WfIpInterfaceHostCache_Type(Integer32):
    """Custom type wfIpInterfaceHostCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              120,
              180,
              240,
              300,
              600,
              900,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("cache120", 120),
          ("cache1200", 1200),
          ("cache180", 180),
          ("cache240", 240),
          ("cache300", 300),
          ("cache600", 600),
          ("cache900", 900),
          ("cacheoff", 1))
    )


_WfIpInterfaceHostCache_Type.__name__ = "Integer32"
_WfIpInterfaceHostCache_Object = MibTableColumn
wfIpInterfaceHostCache = _WfIpInterfaceHostCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 15),
    _WfIpInterfaceHostCache_Type()
)
wfIpInterfaceHostCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceHostCache.setStatus("mandatory")


class _WfIpInterfaceUdpXsumOn_Type(Integer32):
    """Custom type wfIpInterfaceUdpXsumOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceUdpXsumOn_Type.__name__ = "Integer32"
_WfIpInterfaceUdpXsumOn_Object = MibTableColumn
wfIpInterfaceUdpXsumOn = _WfIpInterfaceUdpXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 16),
    _WfIpInterfaceUdpXsumOn_Type()
)
wfIpInterfaceUdpXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceUdpXsumOn.setStatus("mandatory")
_WfIpInterfaceCfgMacAddress_Type = OctetString
_WfIpInterfaceCfgMacAddress_Object = MibTableColumn
wfIpInterfaceCfgMacAddress = _WfIpInterfaceCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 17),
    _WfIpInterfaceCfgMacAddress_Type()
)
wfIpInterfaceCfgMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCfgMacAddress.setStatus("mandatory")
_WfIpInterfaceMacAddress_Type = OctetString
_WfIpInterfaceMacAddress_Object = MibTableColumn
wfIpInterfaceMacAddress = _WfIpInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 18),
    _WfIpInterfaceMacAddress_Type()
)
wfIpInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceMacAddress.setStatus("mandatory")
_WfIpInterfaceReasmMaxSize_Type = Integer32
_WfIpInterfaceReasmMaxSize_Object = MibTableColumn
wfIpInterfaceReasmMaxSize = _WfIpInterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 19),
    _WfIpInterfaceReasmMaxSize_Type()
)
wfIpInterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmMaxSize.setStatus("mandatory")
_WfIpInterfaceMaxInfo_Type = Integer32
_WfIpInterfaceMaxInfo_Object = MibTableColumn
wfIpInterfaceMaxInfo = _WfIpInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 20),
    _WfIpInterfaceMaxInfo_Type()
)
wfIpInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceMaxInfo.setStatus("mandatory")
_WfIpInterfaceInReceives_Type = Counter32
_WfIpInterfaceInReceives_Object = MibTableColumn
wfIpInterfaceInReceives = _WfIpInterfaceInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 21),
    _WfIpInterfaceInReceives_Type()
)
wfIpInterfaceInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInReceives.setStatus("mandatory")
_WfIpInterfaceInHdrErrors_Type = Counter32
_WfIpInterfaceInHdrErrors_Object = MibTableColumn
wfIpInterfaceInHdrErrors = _WfIpInterfaceInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 22),
    _WfIpInterfaceInHdrErrors_Type()
)
wfIpInterfaceInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInHdrErrors.setStatus("mandatory")
_WfIpInterfaceInAddrErrors_Type = Counter32
_WfIpInterfaceInAddrErrors_Object = MibTableColumn
wfIpInterfaceInAddrErrors = _WfIpInterfaceInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 23),
    _WfIpInterfaceInAddrErrors_Type()
)
wfIpInterfaceInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInAddrErrors.setStatus("mandatory")
_WfIpInterfaceForwDatagrams_Type = Counter32
_WfIpInterfaceForwDatagrams_Object = MibTableColumn
wfIpInterfaceForwDatagrams = _WfIpInterfaceForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 24),
    _WfIpInterfaceForwDatagrams_Type()
)
wfIpInterfaceForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceForwDatagrams.setStatus("mandatory")
_WfIpInterfaceInUnknownProtos_Type = Counter32
_WfIpInterfaceInUnknownProtos_Object = MibTableColumn
wfIpInterfaceInUnknownProtos = _WfIpInterfaceInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 25),
    _WfIpInterfaceInUnknownProtos_Type()
)
wfIpInterfaceInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInUnknownProtos.setStatus("mandatory")
_WfIpInterfaceInDiscards_Type = Counter32
_WfIpInterfaceInDiscards_Object = MibTableColumn
wfIpInterfaceInDiscards = _WfIpInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 26),
    _WfIpInterfaceInDiscards_Type()
)
wfIpInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInDiscards.setStatus("mandatory")
_WfIpInterfaceInDelivers_Type = Counter32
_WfIpInterfaceInDelivers_Object = MibTableColumn
wfIpInterfaceInDelivers = _WfIpInterfaceInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 27),
    _WfIpInterfaceInDelivers_Type()
)
wfIpInterfaceInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInDelivers.setStatus("mandatory")
_WfIpInterfaceOutRequests_Type = Counter32
_WfIpInterfaceOutRequests_Object = MibTableColumn
wfIpInterfaceOutRequests = _WfIpInterfaceOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 28),
    _WfIpInterfaceOutRequests_Type()
)
wfIpInterfaceOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceOutRequests.setStatus("mandatory")
_WfIpInterfaceOutDiscards_Type = Counter32
_WfIpInterfaceOutDiscards_Object = MibTableColumn
wfIpInterfaceOutDiscards = _WfIpInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 29),
    _WfIpInterfaceOutDiscards_Type()
)
wfIpInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceOutDiscards.setStatus("mandatory")
_WfIpInterfaceOutNoRoutes_Type = Counter32
_WfIpInterfaceOutNoRoutes_Object = MibTableColumn
wfIpInterfaceOutNoRoutes = _WfIpInterfaceOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 30),
    _WfIpInterfaceOutNoRoutes_Type()
)
wfIpInterfaceOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceOutNoRoutes.setStatus("mandatory")
_WfIpInterfaceReasmTimeout_Type = Integer32
_WfIpInterfaceReasmTimeout_Object = MibTableColumn
wfIpInterfaceReasmTimeout = _WfIpInterfaceReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 31),
    _WfIpInterfaceReasmTimeout_Type()
)
wfIpInterfaceReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmTimeout.setStatus("mandatory")
_WfIpInterfaceReasmReqds_Type = Counter32
_WfIpInterfaceReasmReqds_Object = MibTableColumn
wfIpInterfaceReasmReqds = _WfIpInterfaceReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 32),
    _WfIpInterfaceReasmReqds_Type()
)
wfIpInterfaceReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmReqds.setStatus("mandatory")
_WfIpInterfaceReasmOKs_Type = Counter32
_WfIpInterfaceReasmOKs_Object = MibTableColumn
wfIpInterfaceReasmOKs = _WfIpInterfaceReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 33),
    _WfIpInterfaceReasmOKs_Type()
)
wfIpInterfaceReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmOKs.setStatus("mandatory")
_WfIpInterfaceReasmFails_Type = Counter32
_WfIpInterfaceReasmFails_Object = MibTableColumn
wfIpInterfaceReasmFails = _WfIpInterfaceReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 34),
    _WfIpInterfaceReasmFails_Type()
)
wfIpInterfaceReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmFails.setStatus("mandatory")
_WfIpInterfaceFragOKs_Type = Counter32
_WfIpInterfaceFragOKs_Object = MibTableColumn
wfIpInterfaceFragOKs = _WfIpInterfaceFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 35),
    _WfIpInterfaceFragOKs_Type()
)
wfIpInterfaceFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceFragOKs.setStatus("mandatory")
_WfIpInterfaceFragFails_Type = Counter32
_WfIpInterfaceFragFails_Object = MibTableColumn
wfIpInterfaceFragFails = _WfIpInterfaceFragFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 36),
    _WfIpInterfaceFragFails_Type()
)
wfIpInterfaceFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceFragFails.setStatus("mandatory")
_WfIpInterfaceFragCreates_Type = Counter32
_WfIpInterfaceFragCreates_Object = MibTableColumn
wfIpInterfaceFragCreates = _WfIpInterfaceFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 37),
    _WfIpInterfaceFragCreates_Type()
)
wfIpInterfaceFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceFragCreates.setStatus("mandatory")
_WfIpInterfaceIcmpInMsgs_Type = Counter32
_WfIpInterfaceIcmpInMsgs_Object = MibTableColumn
wfIpInterfaceIcmpInMsgs = _WfIpInterfaceIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 38),
    _WfIpInterfaceIcmpInMsgs_Type()
)
wfIpInterfaceIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInMsgs.setStatus("mandatory")
_WfIpInterfaceIcmpInErrors_Type = Counter32
_WfIpInterfaceIcmpInErrors_Object = MibTableColumn
wfIpInterfaceIcmpInErrors = _WfIpInterfaceIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 39),
    _WfIpInterfaceIcmpInErrors_Type()
)
wfIpInterfaceIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInErrors.setStatus("mandatory")
_WfIpInterfaceIcmpInDestUnreachs_Type = Counter32
_WfIpInterfaceIcmpInDestUnreachs_Object = MibTableColumn
wfIpInterfaceIcmpInDestUnreachs = _WfIpInterfaceIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 40),
    _WfIpInterfaceIcmpInDestUnreachs_Type()
)
wfIpInterfaceIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInDestUnreachs.setStatus("mandatory")
_WfIpInterfaceIcmpInTimeExcds_Type = Counter32
_WfIpInterfaceIcmpInTimeExcds_Object = MibTableColumn
wfIpInterfaceIcmpInTimeExcds = _WfIpInterfaceIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 41),
    _WfIpInterfaceIcmpInTimeExcds_Type()
)
wfIpInterfaceIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInTimeExcds.setStatus("mandatory")
_WfIpInterfaceIcmpInParmProbs_Type = Counter32
_WfIpInterfaceIcmpInParmProbs_Object = MibTableColumn
wfIpInterfaceIcmpInParmProbs = _WfIpInterfaceIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 42),
    _WfIpInterfaceIcmpInParmProbs_Type()
)
wfIpInterfaceIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInParmProbs.setStatus("mandatory")
_WfIpInterfaceIcmpInSrcQuenchs_Type = Counter32
_WfIpInterfaceIcmpInSrcQuenchs_Object = MibTableColumn
wfIpInterfaceIcmpInSrcQuenchs = _WfIpInterfaceIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 43),
    _WfIpInterfaceIcmpInSrcQuenchs_Type()
)
wfIpInterfaceIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInSrcQuenchs.setStatus("mandatory")
_WfIpInterfaceIcmpInRedirects_Type = Counter32
_WfIpInterfaceIcmpInRedirects_Object = MibTableColumn
wfIpInterfaceIcmpInRedirects = _WfIpInterfaceIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 44),
    _WfIpInterfaceIcmpInRedirects_Type()
)
wfIpInterfaceIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInRedirects.setStatus("mandatory")
_WfIpInterfaceIcmpInEchos_Type = Counter32
_WfIpInterfaceIcmpInEchos_Object = MibTableColumn
wfIpInterfaceIcmpInEchos = _WfIpInterfaceIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 45),
    _WfIpInterfaceIcmpInEchos_Type()
)
wfIpInterfaceIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInEchos.setStatus("mandatory")
_WfIpInterfaceIcmpInEchoReps_Type = Counter32
_WfIpInterfaceIcmpInEchoReps_Object = MibTableColumn
wfIpInterfaceIcmpInEchoReps = _WfIpInterfaceIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 46),
    _WfIpInterfaceIcmpInEchoReps_Type()
)
wfIpInterfaceIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInEchoReps.setStatus("mandatory")
_WfIpInterfaceIcmpInTimestamps_Type = Counter32
_WfIpInterfaceIcmpInTimestamps_Object = MibTableColumn
wfIpInterfaceIcmpInTimestamps = _WfIpInterfaceIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 47),
    _WfIpInterfaceIcmpInTimestamps_Type()
)
wfIpInterfaceIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInTimestamps.setStatus("mandatory")
_WfIpInterfaceIcmpInTimestampReps_Type = Counter32
_WfIpInterfaceIcmpInTimestampReps_Object = MibTableColumn
wfIpInterfaceIcmpInTimestampReps = _WfIpInterfaceIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 48),
    _WfIpInterfaceIcmpInTimestampReps_Type()
)
wfIpInterfaceIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInTimestampReps.setStatus("mandatory")
_WfIpInterfaceIcmpInAddrMasks_Type = Counter32
_WfIpInterfaceIcmpInAddrMasks_Object = MibTableColumn
wfIpInterfaceIcmpInAddrMasks = _WfIpInterfaceIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 49),
    _WfIpInterfaceIcmpInAddrMasks_Type()
)
wfIpInterfaceIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInAddrMasks.setStatus("mandatory")
_WfIpInterfaceIcmpInAddrMaskReps_Type = Counter32
_WfIpInterfaceIcmpInAddrMaskReps_Object = MibTableColumn
wfIpInterfaceIcmpInAddrMaskReps = _WfIpInterfaceIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 50),
    _WfIpInterfaceIcmpInAddrMaskReps_Type()
)
wfIpInterfaceIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInAddrMaskReps.setStatus("mandatory")
_WfIpInterfaceIcmpOutMsgs_Type = Counter32
_WfIpInterfaceIcmpOutMsgs_Object = MibTableColumn
wfIpInterfaceIcmpOutMsgs = _WfIpInterfaceIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 51),
    _WfIpInterfaceIcmpOutMsgs_Type()
)
wfIpInterfaceIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutMsgs.setStatus("mandatory")
_WfIpInterfaceIcmpOutErrors_Type = Counter32
_WfIpInterfaceIcmpOutErrors_Object = MibTableColumn
wfIpInterfaceIcmpOutErrors = _WfIpInterfaceIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 52),
    _WfIpInterfaceIcmpOutErrors_Type()
)
wfIpInterfaceIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutErrors.setStatus("mandatory")
_WfIpInterfaceIcmpOutDestUnreachs_Type = Counter32
_WfIpInterfaceIcmpOutDestUnreachs_Object = MibTableColumn
wfIpInterfaceIcmpOutDestUnreachs = _WfIpInterfaceIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 53),
    _WfIpInterfaceIcmpOutDestUnreachs_Type()
)
wfIpInterfaceIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutDestUnreachs.setStatus("mandatory")
_WfIpInterfaceIcmpOutTimeExcds_Type = Counter32
_WfIpInterfaceIcmpOutTimeExcds_Object = MibTableColumn
wfIpInterfaceIcmpOutTimeExcds = _WfIpInterfaceIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 54),
    _WfIpInterfaceIcmpOutTimeExcds_Type()
)
wfIpInterfaceIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutTimeExcds.setStatus("mandatory")
_WfIpInterfaceIcmpOutParmProbs_Type = Counter32
_WfIpInterfaceIcmpOutParmProbs_Object = MibTableColumn
wfIpInterfaceIcmpOutParmProbs = _WfIpInterfaceIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 55),
    _WfIpInterfaceIcmpOutParmProbs_Type()
)
wfIpInterfaceIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutParmProbs.setStatus("mandatory")
_WfIpInterfaceIcmpOutSrcQuenchs_Type = Counter32
_WfIpInterfaceIcmpOutSrcQuenchs_Object = MibTableColumn
wfIpInterfaceIcmpOutSrcQuenchs = _WfIpInterfaceIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 56),
    _WfIpInterfaceIcmpOutSrcQuenchs_Type()
)
wfIpInterfaceIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutSrcQuenchs.setStatus("mandatory")
_WfIpInterfaceIcmpOutRedirects_Type = Counter32
_WfIpInterfaceIcmpOutRedirects_Object = MibTableColumn
wfIpInterfaceIcmpOutRedirects = _WfIpInterfaceIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 57),
    _WfIpInterfaceIcmpOutRedirects_Type()
)
wfIpInterfaceIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutRedirects.setStatus("mandatory")
_WfIpInterfaceIcmpOutEchos_Type = Counter32
_WfIpInterfaceIcmpOutEchos_Object = MibTableColumn
wfIpInterfaceIcmpOutEchos = _WfIpInterfaceIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 58),
    _WfIpInterfaceIcmpOutEchos_Type()
)
wfIpInterfaceIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutEchos.setStatus("mandatory")
_WfIpInterfaceIcmpOutEchoReps_Type = Counter32
_WfIpInterfaceIcmpOutEchoReps_Object = MibTableColumn
wfIpInterfaceIcmpOutEchoReps = _WfIpInterfaceIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 59),
    _WfIpInterfaceIcmpOutEchoReps_Type()
)
wfIpInterfaceIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutEchoReps.setStatus("mandatory")
_WfIpInterfaceIcmpOutTimestamps_Type = Counter32
_WfIpInterfaceIcmpOutTimestamps_Object = MibTableColumn
wfIpInterfaceIcmpOutTimestamps = _WfIpInterfaceIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 60),
    _WfIpInterfaceIcmpOutTimestamps_Type()
)
wfIpInterfaceIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutTimestamps.setStatus("mandatory")
_WfIpInterfaceIcmpOutTimestampReps_Type = Counter32
_WfIpInterfaceIcmpOutTimestampReps_Object = MibTableColumn
wfIpInterfaceIcmpOutTimestampReps = _WfIpInterfaceIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 61),
    _WfIpInterfaceIcmpOutTimestampReps_Type()
)
wfIpInterfaceIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutTimestampReps.setStatus("mandatory")
_WfIpInterfaceIcmpOutAddrMasks_Type = Counter32
_WfIpInterfaceIcmpOutAddrMasks_Object = MibTableColumn
wfIpInterfaceIcmpOutAddrMasks = _WfIpInterfaceIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 62),
    _WfIpInterfaceIcmpOutAddrMasks_Type()
)
wfIpInterfaceIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutAddrMasks.setStatus("mandatory")
_WfIpInterfaceIcmpOutAddrMaskReps_Type = Counter32
_WfIpInterfaceIcmpOutAddrMaskReps_Object = MibTableColumn
wfIpInterfaceIcmpOutAddrMaskReps = _WfIpInterfaceIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 63),
    _WfIpInterfaceIcmpOutAddrMaskReps_Type()
)
wfIpInterfaceIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutAddrMaskReps.setStatus("mandatory")


class _WfIpInterfaceTrEndStation_Type(Integer32):
    """Custom type wfIpInterfaceTrEndStation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceTrEndStation_Type.__name__ = "Integer32"
_WfIpInterfaceTrEndStation_Object = MibTableColumn
wfIpInterfaceTrEndStation = _WfIpInterfaceTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 64),
    _WfIpInterfaceTrEndStation_Type()
)
wfIpInterfaceTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceTrEndStation.setStatus("mandatory")
_WfIpInterfaceSMDSGroupAddress_Type = OctetString
_WfIpInterfaceSMDSGroupAddress_Object = MibTableColumn
wfIpInterfaceSMDSGroupAddress = _WfIpInterfaceSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 65),
    _WfIpInterfaceSMDSGroupAddress_Type()
)
wfIpInterfaceSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceSMDSGroupAddress.setStatus("mandatory")
_WfIpInterfaceSMDSArpReqAddress_Type = OctetString
_WfIpInterfaceSMDSArpReqAddress_Object = MibTableColumn
wfIpInterfaceSMDSArpReqAddress = _WfIpInterfaceSMDSArpReqAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 66),
    _WfIpInterfaceSMDSArpReqAddress_Type()
)
wfIpInterfaceSMDSArpReqAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceSMDSArpReqAddress.setStatus("mandatory")
_WfIpInterfaceFRBcastDlci_Type = Integer32
_WfIpInterfaceFRBcastDlci_Object = MibTableColumn
wfIpInterfaceFRBcastDlci = _WfIpInterfaceFRBcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 67),
    _WfIpInterfaceFRBcastDlci_Type()
)
wfIpInterfaceFRBcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFRBcastDlci.setStatus("mandatory")
_WfIpInterfaceFRMcast1Dlci_Type = Integer32
_WfIpInterfaceFRMcast1Dlci_Object = MibTableColumn
wfIpInterfaceFRMcast1Dlci = _WfIpInterfaceFRMcast1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 68),
    _WfIpInterfaceFRMcast1Dlci_Type()
)
wfIpInterfaceFRMcast1Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFRMcast1Dlci.setStatus("mandatory")
_WfIpInterfaceFRMcast2Dlci_Type = Integer32
_WfIpInterfaceFRMcast2Dlci_Object = MibTableColumn
wfIpInterfaceFRMcast2Dlci = _WfIpInterfaceFRMcast2Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 69),
    _WfIpInterfaceFRMcast2Dlci_Type()
)
wfIpInterfaceFRMcast2Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFRMcast2Dlci.setStatus("mandatory")


class _WfIpInterfaceRedirect_Type(Integer32):
    """Custom type wfIpInterfaceRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceRedirect_Type.__name__ = "Integer32"
_WfIpInterfaceRedirect_Object = MibTableColumn
wfIpInterfaceRedirect = _WfIpInterfaceRedirect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 70),
    _WfIpInterfaceRedirect_Type()
)
wfIpInterfaceRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceRedirect.setStatus("mandatory")


class _WfIpInterfaceEnetArpEncaps_Type(Integer32):
    """Custom type wfIpInterfaceEnetArpEncaps based on Integer32"""
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
        *(("both", 3),
          ("enet", 1),
          ("snap", 2))
    )


_WfIpInterfaceEnetArpEncaps_Type.__name__ = "Integer32"
_WfIpInterfaceEnetArpEncaps_Object = MibTableColumn
wfIpInterfaceEnetArpEncaps = _WfIpInterfaceEnetArpEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 71),
    _WfIpInterfaceEnetArpEncaps_Type()
)
wfIpInterfaceEnetArpEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceEnetArpEncaps.setStatus("mandatory")
_WfIpStaticRouteTable_Object = MibTable
wfIpStaticRouteTable = _WfIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    wfIpStaticRouteTable.setStatus("mandatory")
_WfIpStaticRouteEntry_Object = MibTableRow
wfIpStaticRouteEntry = _WfIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1)
)
wfIpStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpSrIpAddress"),
    (0, "Wellfleet-Series7-MIB", "wfIpSrIpNetMask"),
    (0, "Wellfleet-Series7-MIB", "wfIpSrIpAddressRt"),
)
if mibBuilder.loadTexts:
    wfIpStaticRouteEntry.setStatus("mandatory")


class _WfIpSrCreate_Type(Integer32):
    """Custom type wfIpSrCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpSrCreate_Type.__name__ = "Integer32"
_WfIpSrCreate_Object = MibTableColumn
wfIpSrCreate = _WfIpSrCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 1),
    _WfIpSrCreate_Type()
)
wfIpSrCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrCreate.setStatus("mandatory")


class _WfIpSrEnable_Type(Integer32):
    """Custom type wfIpSrEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpSrEnable_Type.__name__ = "Integer32"
_WfIpSrEnable_Object = MibTableColumn
wfIpSrEnable = _WfIpSrEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 2),
    _WfIpSrEnable_Type()
)
wfIpSrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrEnable.setStatus("mandatory")
_WfIpSrIpAddress_Type = IpAddress
_WfIpSrIpAddress_Object = MibTableColumn
wfIpSrIpAddress = _WfIpSrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 3),
    _WfIpSrIpAddress_Type()
)
wfIpSrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrIpAddress.setStatus("mandatory")
_WfIpSrIpNetMask_Type = IpAddress
_WfIpSrIpNetMask_Object = MibTableColumn
wfIpSrIpNetMask = _WfIpSrIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 4),
    _WfIpSrIpNetMask_Type()
)
wfIpSrIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrIpNetMask.setStatus("mandatory")


class _WfIpSrCost_Type(Integer32):
    """Custom type wfIpSrCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cost", 1)
    )


_WfIpSrCost_Type.__name__ = "Integer32"
_WfIpSrCost_Object = MibTableColumn
wfIpSrCost = _WfIpSrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 5),
    _WfIpSrCost_Type()
)
wfIpSrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrCost.setStatus("mandatory")
_WfIpSrNextHopAddr_Type = IpAddress
_WfIpSrNextHopAddr_Object = MibTableColumn
wfIpSrNextHopAddr = _WfIpSrNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 6),
    _WfIpSrNextHopAddr_Type()
)
wfIpSrNextHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrNextHopAddr.setStatus("mandatory")
_WfIpSrNextHopMask_Type = IpAddress
_WfIpSrNextHopMask_Object = MibTableColumn
wfIpSrNextHopMask = _WfIpSrNextHopMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 7),
    _WfIpSrNextHopMask_Type()
)
wfIpSrNextHopMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrNextHopMask.setStatus("mandatory")


class _WfIpSrPreference_Type(Integer32):
    """Custom type wfIpSrPreference based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16
        )
    )
    namedValues = NamedValues(
        ("pref", 16)
    )


_WfIpSrPreference_Type.__name__ = "Integer32"
_WfIpSrPreference_Object = MibTableColumn
wfIpSrPreference = _WfIpSrPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 8),
    _WfIpSrPreference_Type()
)
wfIpSrPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrPreference.setStatus("mandatory")
_WfIpSrIpAddressRt_Type = Integer32
_WfIpSrIpAddressRt_Object = MibTableColumn
wfIpSrIpAddressRt = _WfIpSrIpAddressRt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 9),
    _WfIpSrIpAddressRt_Type()
)
wfIpSrIpAddressRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrIpAddressRt.setStatus("mandatory")


class _WfIpSrValid_Type(Integer32):
    """Custom type wfIpSrValid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpSrValid_Type.__name__ = "Integer32"
_WfIpSrValid_Object = MibTableColumn
wfIpSrValid = _WfIpSrValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 10),
    _WfIpSrValid_Type()
)
wfIpSrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrValid.setStatus("mandatory")
_WfIpAdjacentHostTable_Object = MibTable
wfIpAdjacentHostTable = _WfIpAdjacentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    wfIpAdjacentHostTable.setStatus("mandatory")
_WfIpAdjacentHostEntry_Object = MibTableRow
wfIpAdjacentHostEntry = _WfIpAdjacentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1)
)
wfIpAdjacentHostEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpAdjHostIpAddress"),
)
if mibBuilder.loadTexts:
    wfIpAdjacentHostEntry.setStatus("mandatory")


class _WfIpAdjHostCreate_Type(Integer32):
    """Custom type wfIpAdjHostCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpAdjHostCreate_Type.__name__ = "Integer32"
_WfIpAdjHostCreate_Object = MibTableColumn
wfIpAdjHostCreate = _WfIpAdjHostCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 1),
    _WfIpAdjHostCreate_Type()
)
wfIpAdjHostCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostCreate.setStatus("mandatory")


class _WfIpAdjHostEnable_Type(Integer32):
    """Custom type wfIpAdjHostEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpAdjHostEnable_Type.__name__ = "Integer32"
_WfIpAdjHostEnable_Object = MibTableColumn
wfIpAdjHostEnable = _WfIpAdjHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 2),
    _WfIpAdjHostEnable_Type()
)
wfIpAdjHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostEnable.setStatus("mandatory")
_WfIpAdjHostIpAddress_Type = IpAddress
_WfIpAdjHostIpAddress_Object = MibTableColumn
wfIpAdjHostIpAddress = _WfIpAdjHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 3),
    _WfIpAdjHostIpAddress_Type()
)
wfIpAdjHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdjHostIpAddress.setStatus("mandatory")
_WfIpAdjHostIntf_Type = IpAddress
_WfIpAdjHostIntf_Object = MibTableColumn
wfIpAdjHostIntf = _WfIpAdjHostIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 4),
    _WfIpAdjHostIntf_Type()
)
wfIpAdjHostIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostIntf.setStatus("mandatory")
_WfIpAdjHostIntfMask_Type = IpAddress
_WfIpAdjHostIntfMask_Object = MibTableColumn
wfIpAdjHostIntfMask = _WfIpAdjHostIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 5),
    _WfIpAdjHostIntfMask_Type()
)
wfIpAdjHostIntfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostIntfMask.setStatus("mandatory")
_WfIpAdjHostMacAddr_Type = OctetString
_WfIpAdjHostMacAddr_Object = MibTableColumn
wfIpAdjHostMacAddr = _WfIpAdjHostMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 6),
    _WfIpAdjHostMacAddr_Type()
)
wfIpAdjHostMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostMacAddr.setStatus("mandatory")


class _WfIpAdjHostEncaps_Type(Integer32):
    """Custom type wfIpAdjHostEncaps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enet", 1),
          ("snap", 2))
    )


_WfIpAdjHostEncaps_Type.__name__ = "Integer32"
_WfIpAdjHostEncaps_Object = MibTableColumn
wfIpAdjHostEncaps = _WfIpAdjHostEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 7),
    _WfIpAdjHostEncaps_Type()
)
wfIpAdjHostEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostEncaps.setStatus("mandatory")


class _WfIpAdjHostValid_Type(Integer32):
    """Custom type wfIpAdjHostValid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpAdjHostValid_Type.__name__ = "Integer32"
_WfIpAdjHostValid_Object = MibTableColumn
wfIpAdjHostValid = _WfIpAdjHostValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 8),
    _WfIpAdjHostValid_Type()
)
wfIpAdjHostValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdjHostValid.setStatus("mandatory")
_WfIpTrafficFilterTable_Object = MibTable
wfIpTrafficFilterTable = _WfIpTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7)
)
if mibBuilder.loadTexts:
    wfIpTrafficFilterTable.setStatus("mandatory")
_WfIpTrafficFilterEntry_Object = MibTableRow
wfIpTrafficFilterEntry = _WfIpTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1)
)
wfIpTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpTrafficFilterInterface"),
    (0, "Wellfleet-Series7-MIB", "wfIpTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfIpTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfIpTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfIpTrafficFilterEntry.setStatus("mandatory")


class _WfIpTrafficFilterCreate_Type(Integer32):
    """Custom type wfIpTrafficFilterCreate based on Integer32"""
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


_WfIpTrafficFilterCreate_Type.__name__ = "Integer32"
_WfIpTrafficFilterCreate_Object = MibTableColumn
wfIpTrafficFilterCreate = _WfIpTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 1),
    _WfIpTrafficFilterCreate_Type()
)
wfIpTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterCreate.setStatus("mandatory")


class _WfIpTrafficFilterEnable_Type(Integer32):
    """Custom type wfIpTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpTrafficFilterEnable_Type.__name__ = "Integer32"
_WfIpTrafficFilterEnable_Object = MibTableColumn
wfIpTrafficFilterEnable = _WfIpTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 2),
    _WfIpTrafficFilterEnable_Type()
)
wfIpTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterEnable.setStatus("mandatory")


class _WfIpTrafficFilterStatus_Type(Integer32):
    """Custom type wfIpTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfIpTrafficFilterStatus_Type.__name__ = "Integer32"
_WfIpTrafficFilterStatus_Object = MibTableColumn
wfIpTrafficFilterStatus = _WfIpTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 3),
    _WfIpTrafficFilterStatus_Type()
)
wfIpTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterStatus.setStatus("mandatory")
_WfIpTrafficFilterCounter_Type = Counter32
_WfIpTrafficFilterCounter_Object = MibTableColumn
wfIpTrafficFilterCounter = _WfIpTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 4),
    _WfIpTrafficFilterCounter_Type()
)
wfIpTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterCounter.setStatus("mandatory")
_WfIpTrafficFilterDefinition_Type = Opaque
_WfIpTrafficFilterDefinition_Object = MibTableColumn
wfIpTrafficFilterDefinition = _WfIpTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 5),
    _WfIpTrafficFilterDefinition_Type()
)
wfIpTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterDefinition.setStatus("mandatory")
_WfIpTrafficFilterReserved_Type = Integer32
_WfIpTrafficFilterReserved_Object = MibTableColumn
wfIpTrafficFilterReserved = _WfIpTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 6),
    _WfIpTrafficFilterReserved_Type()
)
wfIpTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfIpTrafficFilterReserved.setStatus("mandatory")
_WfIpTrafficFilterInterface_Type = IpAddress
_WfIpTrafficFilterInterface_Object = MibTableColumn
wfIpTrafficFilterInterface = _WfIpTrafficFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 7),
    _WfIpTrafficFilterInterface_Type()
)
wfIpTrafficFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterInterface.setStatus("mandatory")
_WfIpTrafficFilterCircuit_Type = Integer32
_WfIpTrafficFilterCircuit_Object = MibTableColumn
wfIpTrafficFilterCircuit = _WfIpTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 8),
    _WfIpTrafficFilterCircuit_Type()
)
wfIpTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterCircuit.setStatus("mandatory")
_WfIpTrafficFilterRuleNumber_Type = Integer32
_WfIpTrafficFilterRuleNumber_Object = MibTableColumn
wfIpTrafficFilterRuleNumber = _WfIpTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 9),
    _WfIpTrafficFilterRuleNumber_Type()
)
wfIpTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterRuleNumber.setStatus("mandatory")
_WfIpTrafficFilterFragment_Type = Integer32
_WfIpTrafficFilterFragment_Object = MibTableColumn
wfIpTrafficFilterFragment = _WfIpTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 10),
    _WfIpTrafficFilterFragment_Type()
)
wfIpTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterFragment.setStatus("mandatory")
_WfIpRfRipImportTable_Object = MibTable
wfIpRfRipImportTable = _WfIpRfRipImportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    wfIpRfRipImportTable.setStatus("mandatory")
_WfIpRfRipImportEntry_Object = MibTableRow
wfIpRfRipImportEntry = _WfIpRfRipImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1)
)
wfIpRfRipImportEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipImportAddress"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipImportMask"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipImportRipGateway"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipImportRipInterface"),
)
if mibBuilder.loadTexts:
    wfIpRfRipImportEntry.setStatus("mandatory")


class _WfIpRfRipImportCreate_Type(Integer32):
    """Custom type wfIpRfRipImportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfRipImportCreate_Type.__name__ = "Integer32"
_WfIpRfRipImportCreate_Object = MibTableColumn
wfIpRfRipImportCreate = _WfIpRfRipImportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 1),
    _WfIpRfRipImportCreate_Type()
)
wfIpRfRipImportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportCreate.setStatus("mandatory")


class _WfIpRfRipImportEnable_Type(Integer32):
    """Custom type wfIpRfRipImportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfRipImportEnable_Type.__name__ = "Integer32"
_WfIpRfRipImportEnable_Object = MibTableColumn
wfIpRfRipImportEnable = _WfIpRfRipImportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 2),
    _WfIpRfRipImportEnable_Type()
)
wfIpRfRipImportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportEnable.setStatus("mandatory")
_WfIpRfRipImportAddress_Type = IpAddress
_WfIpRfRipImportAddress_Object = MibTableColumn
wfIpRfRipImportAddress = _WfIpRfRipImportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 3),
    _WfIpRfRipImportAddress_Type()
)
wfIpRfRipImportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportAddress.setStatus("mandatory")
_WfIpRfRipImportMask_Type = IpAddress
_WfIpRfRipImportMask_Object = MibTableColumn
wfIpRfRipImportMask = _WfIpRfRipImportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 4),
    _WfIpRfRipImportMask_Type()
)
wfIpRfRipImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportMask.setStatus("mandatory")


class _WfIpRfRipImportAction_Type(Integer32):
    """Custom type wfIpRfRipImportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRfRipImportAction_Type.__name__ = "Integer32"
_WfIpRfRipImportAction_Object = MibTableColumn
wfIpRfRipImportAction = _WfIpRfRipImportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 5),
    _WfIpRfRipImportAction_Type()
)
wfIpRfRipImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportAction.setStatus("mandatory")


class _WfIpRfRipImportPreference_Type(Integer32):
    """Custom type wfIpRfRipImportPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16
        )
    )
    namedValues = NamedValues(
        ("maximum", 16)
    )


_WfIpRfRipImportPreference_Type.__name__ = "Integer32"
_WfIpRfRipImportPreference_Object = MibTableColumn
wfIpRfRipImportPreference = _WfIpRfRipImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 6),
    _WfIpRfRipImportPreference_Type()
)
wfIpRfRipImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportPreference.setStatus("mandatory")
_WfIpRfRipImportRipGateway_Type = IpAddress
_WfIpRfRipImportRipGateway_Object = MibTableColumn
wfIpRfRipImportRipGateway = _WfIpRfRipImportRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 7),
    _WfIpRfRipImportRipGateway_Type()
)
wfIpRfRipImportRipGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportRipGateway.setStatus("mandatory")
_WfIpRfRipImportRipInterface_Type = IpAddress
_WfIpRfRipImportRipInterface_Object = MibTableColumn
wfIpRfRipImportRipInterface = _WfIpRfRipImportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 8),
    _WfIpRfRipImportRipInterface_Type()
)
wfIpRfRipImportRipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportRipInterface.setStatus("mandatory")
_WfIpRfRipExportTable_Object = MibTable
wfIpRfRipExportTable = _WfIpRfRipExportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9)
)
if mibBuilder.loadTexts:
    wfIpRfRipExportTable.setStatus("mandatory")
_WfIpRfRipExportEntry_Object = MibTableRow
wfIpRfRipExportEntry = _WfIpRfRipExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1)
)
wfIpRfRipExportEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipExportAddress"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipExportMask"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipExportFromProtocol"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfRipExportInterface"),
)
if mibBuilder.loadTexts:
    wfIpRfRipExportEntry.setStatus("mandatory")


class _WfIpRfRipExportCreate_Type(Integer32):
    """Custom type wfIpRfRipExportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfRipExportCreate_Type.__name__ = "Integer32"
_WfIpRfRipExportCreate_Object = MibTableColumn
wfIpRfRipExportCreate = _WfIpRfRipExportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 1),
    _WfIpRfRipExportCreate_Type()
)
wfIpRfRipExportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportCreate.setStatus("mandatory")


class _WfIpRfRipExportEnable_Type(Integer32):
    """Custom type wfIpRfRipExportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfRipExportEnable_Type.__name__ = "Integer32"
_WfIpRfRipExportEnable_Object = MibTableColumn
wfIpRfRipExportEnable = _WfIpRfRipExportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 2),
    _WfIpRfRipExportEnable_Type()
)
wfIpRfRipExportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportEnable.setStatus("mandatory")
_WfIpRfRipExportAddress_Type = IpAddress
_WfIpRfRipExportAddress_Object = MibTableColumn
wfIpRfRipExportAddress = _WfIpRfRipExportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 3),
    _WfIpRfRipExportAddress_Type()
)
wfIpRfRipExportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportAddress.setStatus("mandatory")
_WfIpRfRipExportMask_Type = IpAddress
_WfIpRfRipExportMask_Object = MibTableColumn
wfIpRfRipExportMask = _WfIpRfRipExportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 4),
    _WfIpRfRipExportMask_Type()
)
wfIpRfRipExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportMask.setStatus("mandatory")


class _WfIpRfRipExportFromProtocol_Type(Integer32):
    """Custom type wfIpRfRipExportFromProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("direct", 4),
          ("ospf", 3),
          ("rip", 1),
          ("static", 5))
    )


_WfIpRfRipExportFromProtocol_Type.__name__ = "Integer32"
_WfIpRfRipExportFromProtocol_Object = MibTableColumn
wfIpRfRipExportFromProtocol = _WfIpRfRipExportFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 5),
    _WfIpRfRipExportFromProtocol_Type()
)
wfIpRfRipExportFromProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportFromProtocol.setStatus("mandatory")


class _WfIpRfRipExportAction_Type(Integer32):
    """Custom type wfIpRfRipExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("propa", 2))
    )


_WfIpRfRipExportAction_Type.__name__ = "Integer32"
_WfIpRfRipExportAction_Object = MibTableColumn
wfIpRfRipExportAction = _WfIpRfRipExportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 6),
    _WfIpRfRipExportAction_Type()
)
wfIpRfRipExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportAction.setStatus("mandatory")
_WfIpRfRipExportInterface_Type = IpAddress
_WfIpRfRipExportInterface_Object = MibTableColumn
wfIpRfRipExportInterface = _WfIpRfRipExportInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 7),
    _WfIpRfRipExportInterface_Type()
)
wfIpRfRipExportInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportInterface.setStatus("mandatory")


class _WfIpRfRipExportRipMetric_Type(Integer32):
    """Custom type wfIpRfRipExportRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            15
        )
    )
    namedValues = NamedValues(
        ("maximum", 15)
    )


_WfIpRfRipExportRipMetric_Type.__name__ = "Integer32"
_WfIpRfRipExportRipMetric_Object = MibTableColumn
wfIpRfRipExportRipMetric = _WfIpRfRipExportRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 8),
    _WfIpRfRipExportRipMetric_Type()
)
wfIpRfRipExportRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportRipMetric.setStatus("mandatory")
_WfIpRfOspfImportTable_Object = MibTable
wfIpRfOspfImportTable = _WfIpRfOspfImportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10)
)
if mibBuilder.loadTexts:
    wfIpRfOspfImportTable.setStatus("mandatory")
_WfIpRfOspfImportEntry_Object = MibTableRow
wfIpRfOspfImportEntry = _WfIpRfOspfImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1)
)
wfIpRfOspfImportEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfImportAddress"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfImportMask"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfImportType"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfImportTag"),
)
if mibBuilder.loadTexts:
    wfIpRfOspfImportEntry.setStatus("mandatory")


class _WfIpRfOspfImportCreate_Type(Integer32):
    """Custom type wfIpRfOspfImportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfOspfImportCreate_Type.__name__ = "Integer32"
_WfIpRfOspfImportCreate_Object = MibTableColumn
wfIpRfOspfImportCreate = _WfIpRfOspfImportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 1),
    _WfIpRfOspfImportCreate_Type()
)
wfIpRfOspfImportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportCreate.setStatus("mandatory")


class _WfIpRfOspfImportEnable_Type(Integer32):
    """Custom type wfIpRfOspfImportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfOspfImportEnable_Type.__name__ = "Integer32"
_WfIpRfOspfImportEnable_Object = MibTableColumn
wfIpRfOspfImportEnable = _WfIpRfOspfImportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 2),
    _WfIpRfOspfImportEnable_Type()
)
wfIpRfOspfImportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportEnable.setStatus("mandatory")
_WfIpRfOspfImportAddress_Type = IpAddress
_WfIpRfOspfImportAddress_Object = MibTableColumn
wfIpRfOspfImportAddress = _WfIpRfOspfImportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 3),
    _WfIpRfOspfImportAddress_Type()
)
wfIpRfOspfImportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportAddress.setStatus("mandatory")
_WfIpRfOspfImportMask_Type = IpAddress
_WfIpRfOspfImportMask_Object = MibTableColumn
wfIpRfOspfImportMask = _WfIpRfOspfImportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 4),
    _WfIpRfOspfImportMask_Type()
)
wfIpRfOspfImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportMask.setStatus("mandatory")


class _WfIpRfOspfImportAction_Type(Integer32):
    """Custom type wfIpRfOspfImportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRfOspfImportAction_Type.__name__ = "Integer32"
_WfIpRfOspfImportAction_Object = MibTableColumn
wfIpRfOspfImportAction = _WfIpRfOspfImportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 5),
    _WfIpRfOspfImportAction_Type()
)
wfIpRfOspfImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportAction.setStatus("mandatory")


class _WfIpRfOspfImportPreference_Type(Integer32):
    """Custom type wfIpRfOspfImportPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16
        )
    )
    namedValues = NamedValues(
        ("maximum", 16)
    )


_WfIpRfOspfImportPreference_Type.__name__ = "Integer32"
_WfIpRfOspfImportPreference_Object = MibTableColumn
wfIpRfOspfImportPreference = _WfIpRfOspfImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 6),
    _WfIpRfOspfImportPreference_Type()
)
wfIpRfOspfImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportPreference.setStatus("mandatory")
_WfIpRfOspfImportType_Type = Integer32
_WfIpRfOspfImportType_Object = MibTableColumn
wfIpRfOspfImportType = _WfIpRfOspfImportType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 7),
    _WfIpRfOspfImportType_Type()
)
wfIpRfOspfImportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportType.setStatus("mandatory")
_WfIpRfOspfImportTag_Type = Integer32
_WfIpRfOspfImportTag_Object = MibTableColumn
wfIpRfOspfImportTag = _WfIpRfOspfImportTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 8),
    _WfIpRfOspfImportTag_Type()
)
wfIpRfOspfImportTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportTag.setStatus("mandatory")
_WfIpRfOspfExportTable_Object = MibTable
wfIpRfOspfExportTable = _WfIpRfOspfExportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11)
)
if mibBuilder.loadTexts:
    wfIpRfOspfExportTable.setStatus("mandatory")
_WfIpRfOspfExportEntry_Object = MibTableRow
wfIpRfOspfExportEntry = _WfIpRfOspfExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1)
)
wfIpRfOspfExportEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfExportAddress"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfExportMask"),
    (0, "Wellfleet-Series7-MIB", "wfIpRfOspfExportFromProtocol"),
)
if mibBuilder.loadTexts:
    wfIpRfOspfExportEntry.setStatus("mandatory")


class _WfIpRfOspfExportCreate_Type(Integer32):
    """Custom type wfIpRfOspfExportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfOspfExportCreate_Type.__name__ = "Integer32"
_WfIpRfOspfExportCreate_Object = MibTableColumn
wfIpRfOspfExportCreate = _WfIpRfOspfExportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 1),
    _WfIpRfOspfExportCreate_Type()
)
wfIpRfOspfExportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportCreate.setStatus("mandatory")


class _WfIpRfOspfExportEnable_Type(Integer32):
    """Custom type wfIpRfOspfExportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfOspfExportEnable_Type.__name__ = "Integer32"
_WfIpRfOspfExportEnable_Object = MibTableColumn
wfIpRfOspfExportEnable = _WfIpRfOspfExportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 2),
    _WfIpRfOspfExportEnable_Type()
)
wfIpRfOspfExportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportEnable.setStatus("mandatory")
_WfIpRfOspfExportAddress_Type = IpAddress
_WfIpRfOspfExportAddress_Object = MibTableColumn
wfIpRfOspfExportAddress = _WfIpRfOspfExportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 3),
    _WfIpRfOspfExportAddress_Type()
)
wfIpRfOspfExportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfExportAddress.setStatus("mandatory")
_WfIpRfOspfExportMask_Type = IpAddress
_WfIpRfOspfExportMask_Object = MibTableColumn
wfIpRfOspfExportMask = _WfIpRfOspfExportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 4),
    _WfIpRfOspfExportMask_Type()
)
wfIpRfOspfExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfExportMask.setStatus("mandatory")


class _WfIpRfOspfExportFromProtocol_Type(Integer32):
    """Custom type wfIpRfOspfExportFromProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("direct", 4),
          ("ospf", 3),
          ("rip", 1),
          ("static", 5))
    )


_WfIpRfOspfExportFromProtocol_Type.__name__ = "Integer32"
_WfIpRfOspfExportFromProtocol_Object = MibTableColumn
wfIpRfOspfExportFromProtocol = _WfIpRfOspfExportFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 5),
    _WfIpRfOspfExportFromProtocol_Type()
)
wfIpRfOspfExportFromProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfExportFromProtocol.setStatus("mandatory")


class _WfIpRfOspfExportAction_Type(Integer32):
    """Custom type wfIpRfOspfExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("propa", 2))
    )


_WfIpRfOspfExportAction_Type.__name__ = "Integer32"
_WfIpRfOspfExportAction_Object = MibTableColumn
wfIpRfOspfExportAction = _WfIpRfOspfExportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 6),
    _WfIpRfOspfExportAction_Type()
)
wfIpRfOspfExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportAction.setStatus("mandatory")


class _WfIpRfOspfExportType_Type(Integer32):
    """Custom type wfIpRfOspfExportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_WfIpRfOspfExportType_Type.__name__ = "Integer32"
_WfIpRfOspfExportType_Object = MibTableColumn
wfIpRfOspfExportType = _WfIpRfOspfExportType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 7),
    _WfIpRfOspfExportType_Type()
)
wfIpRfOspfExportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportType.setStatus("mandatory")
_WfIpRfOspfExportTag_Type = Integer32
_WfIpRfOspfExportTag_Object = MibTableColumn
wfIpRfOspfExportTag = _WfIpRfOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 8),
    _WfIpRfOspfExportTag_Type()
)
wfIpRfOspfExportTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportTag.setStatus("mandatory")
_WfRipGroup_ObjectIdentity = ObjectIdentity
wfRipGroup = _WfRipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2)
)
_WfRipIntfTable_Object = MibTable
wfRipIntfTable = _WfRipIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wfRipIntfTable.setStatus("mandatory")
_WfRipIntfEntry_Object = MibTableRow
wfRipIntfEntry = _WfRipIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1)
)
wfRipIntfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfRipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfRipIntfEntry.setStatus("mandatory")


class _WfRipInterfaceCreate_Type(Integer32):
    """Custom type wfRipInterfaceCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfRipInterfaceCreate_Type.__name__ = "Integer32"
_WfRipInterfaceCreate_Object = MibTableColumn
wfRipInterfaceCreate = _WfRipInterfaceCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 1),
    _WfRipInterfaceCreate_Type()
)
wfRipInterfaceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceCreate.setStatus("mandatory")


class _WfRipInterfaceEnable_Type(Integer32):
    """Custom type wfRipInterfaceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfRipInterfaceEnable_Type.__name__ = "Integer32"
_WfRipInterfaceEnable_Object = MibTableColumn
wfRipInterfaceEnable = _WfRipInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 2),
    _WfRipInterfaceEnable_Type()
)
wfRipInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceEnable.setStatus("mandatory")


class _WfRipInterfaceState_Type(Integer32):
    """Custom type wfRipInterfaceState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfRipInterfaceState_Type.__name__ = "Integer32"
_WfRipInterfaceState_Object = MibTableColumn
wfRipInterfaceState = _WfRipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 3),
    _WfRipInterfaceState_Type()
)
wfRipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipInterfaceState.setStatus("mandatory")
_WfRipInterfaceIndex_Type = IpAddress
_WfRipInterfaceIndex_Object = MibTableColumn
wfRipInterfaceIndex = _WfRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 4),
    _WfRipInterfaceIndex_Type()
)
wfRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipInterfaceIndex.setStatus("mandatory")


class _WfRipInterfaceSupply_Type(Integer32):
    """Custom type wfRipInterfaceSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfRipInterfaceSupply_Type.__name__ = "Integer32"
_WfRipInterfaceSupply_Object = MibTableColumn
wfRipInterfaceSupply = _WfRipInterfaceSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 5),
    _WfRipInterfaceSupply_Type()
)
wfRipInterfaceSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceSupply.setStatus("mandatory")


class _WfRipInterfaceListen_Type(Integer32):
    """Custom type wfRipInterfaceListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfRipInterfaceListen_Type.__name__ = "Integer32"
_WfRipInterfaceListen_Object = MibTableColumn
wfRipInterfaceListen = _WfRipInterfaceListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 6),
    _WfRipInterfaceListen_Type()
)
wfRipInterfaceListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceListen.setStatus("mandatory")


class _WfRipInterfaceDefaultRouteSupply_Type(Integer32):
    """Custom type wfRipInterfaceDefaultRouteSupply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfRipInterfaceDefaultRouteSupply_Type.__name__ = "Integer32"
_WfRipInterfaceDefaultRouteSupply_Object = MibTableColumn
wfRipInterfaceDefaultRouteSupply = _WfRipInterfaceDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 7),
    _WfRipInterfaceDefaultRouteSupply_Type()
)
wfRipInterfaceDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceDefaultRouteSupply.setStatus("mandatory")


class _WfRipInterfaceDefaultRouteListen_Type(Integer32):
    """Custom type wfRipInterfaceDefaultRouteListen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfRipInterfaceDefaultRouteListen_Type.__name__ = "Integer32"
_WfRipInterfaceDefaultRouteListen_Object = MibTableColumn
wfRipInterfaceDefaultRouteListen = _WfRipInterfaceDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 8),
    _WfRipInterfaceDefaultRouteListen_Type()
)
wfRipInterfaceDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceDefaultRouteListen.setStatus("mandatory")


class _WfRipInterfacePoisonedReversed_Type(Integer32):
    """Custom type wfRipInterfacePoisonedReversed based on Integer32"""
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
        *(("actual", 2),
          ("poisoned", 1),
          ("split", 3))
    )


_WfRipInterfacePoisonedReversed_Type.__name__ = "Integer32"
_WfRipInterfacePoisonedReversed_Object = MibTableColumn
wfRipInterfacePoisonedReversed = _WfRipInterfacePoisonedReversed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 9),
    _WfRipInterfacePoisonedReversed_Type()
)
wfRipInterfacePoisonedReversed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfacePoisonedReversed.setStatus("mandatory")
_WfOspfGroup_ObjectIdentity = ObjectIdentity
wfOspfGroup = _WfOspfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3)
)
_WfOspfGeneralGroup_ObjectIdentity = ObjectIdentity
wfOspfGeneralGroup = _WfOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1)
)


class _WfOspfGeneralDelete_Type(Integer32):
    """Custom type wfOspfGeneralDelete based on Integer32"""
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


_WfOspfGeneralDelete_Type.__name__ = "Integer32"
_WfOspfGeneralDelete_Object = MibScalar
wfOspfGeneralDelete = _WfOspfGeneralDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 1),
    _WfOspfGeneralDelete_Type()
)
wfOspfGeneralDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfGeneralDelete.setStatus("mandatory")


class _WfOspfGeneralDisable_Type(Integer32):
    """Custom type wfOspfGeneralDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOspfGeneralDisable_Type.__name__ = "Integer32"
_WfOspfGeneralDisable_Object = MibScalar
wfOspfGeneralDisable = _WfOspfGeneralDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 2),
    _WfOspfGeneralDisable_Type()
)
wfOspfGeneralDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfGeneralDisable.setStatus("mandatory")


class _WfOspfGeneralState_Type(Integer32):
    """Custom type wfOspfGeneralState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfOspfGeneralState_Type.__name__ = "Integer32"
_WfOspfGeneralState_Object = MibScalar
wfOspfGeneralState = _WfOspfGeneralState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 3),
    _WfOspfGeneralState_Type()
)
wfOspfGeneralState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfGeneralState.setStatus("mandatory")
_WfOspfRouterId_Type = IpAddress
_WfOspfRouterId_Object = MibScalar
wfOspfRouterId = _WfOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 4),
    _WfOspfRouterId_Type()
)
wfOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfRouterId.setStatus("mandatory")
_WfOspfVersionNumber_Type = Integer32
_WfOspfVersionNumber_Object = MibScalar
wfOspfVersionNumber = _WfOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 5),
    _WfOspfVersionNumber_Type()
)
wfOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVersionNumber.setStatus("mandatory")


class _WfOspfAreaBdrRtrStatus_Type(Integer32):
    """Custom type wfOspfAreaBdrRtrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfAreaBdrRtrStatus_Type.__name__ = "Integer32"
_WfOspfAreaBdrRtrStatus_Object = MibScalar
wfOspfAreaBdrRtrStatus = _WfOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 6),
    _WfOspfAreaBdrRtrStatus_Type()
)
wfOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaBdrRtrStatus.setStatus("mandatory")


class _WfOspfASBdrRtrStatus_Type(Integer32):
    """Custom type wfOspfASBdrRtrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfASBdrRtrStatus_Type.__name__ = "Integer32"
_WfOspfASBdrRtrStatus_Object = MibScalar
wfOspfASBdrRtrStatus = _WfOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 7),
    _WfOspfASBdrRtrStatus_Type()
)
wfOspfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfASBdrRtrStatus.setStatus("mandatory")


class _WfOspfTOSSupport_Type(Integer32):
    """Custom type wfOspfTOSSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfTOSSupport_Type.__name__ = "Integer32"
_WfOspfTOSSupport_Object = MibScalar
wfOspfTOSSupport = _WfOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 8),
    _WfOspfTOSSupport_Type()
)
wfOspfTOSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfTOSSupport.setStatus("mandatory")


class _WfOspfSpfHoldDown_Type(Integer32):
    """Custom type wfOspfSpfHoldDown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 10))
    )


_WfOspfSpfHoldDown_Type.__name__ = "Integer32"
_WfOspfSpfHoldDown_Object = MibScalar
wfOspfSpfHoldDown = _WfOspfSpfHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 9),
    _WfOspfSpfHoldDown_Type()
)
wfOspfSpfHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfSpfHoldDown.setStatus("mandatory")


class _WfOspfSlotMask_Type(Integer32):
    """Custom type wfOspfSlotMask based on Integer32"""
    defaultValue = 16383

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16383
        )
    )
    namedValues = NamedValues(
        ("slotmask", 16383)
    )


_WfOspfSlotMask_Type.__name__ = "Integer32"
_WfOspfSlotMask_Object = MibScalar
wfOspfSlotMask = _WfOspfSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 1, 10),
    _WfOspfSlotMask_Type()
)
wfOspfSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfSlotMask.setStatus("mandatory")
_WfOspfAreaTable_Object = MibTable
wfOspfAreaTable = _WfOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wfOspfAreaTable.setStatus("mandatory")
_WfOspfAreaEntry_Object = MibTableRow
wfOspfAreaEntry = _WfOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1)
)
wfOspfAreaEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfAreaId"),
)
if mibBuilder.loadTexts:
    wfOspfAreaEntry.setStatus("mandatory")


class _WfOspfAreaDelete_Type(Integer32):
    """Custom type wfOspfAreaDelete based on Integer32"""
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


_WfOspfAreaDelete_Type.__name__ = "Integer32"
_WfOspfAreaDelete_Object = MibTableColumn
wfOspfAreaDelete = _WfOspfAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 1),
    _WfOspfAreaDelete_Type()
)
wfOspfAreaDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaDelete.setStatus("mandatory")


class _WfOspfAreaDisable_Type(Integer32):
    """Custom type wfOspfAreaDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOspfAreaDisable_Type.__name__ = "Integer32"
_WfOspfAreaDisable_Object = MibTableColumn
wfOspfAreaDisable = _WfOspfAreaDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 2),
    _WfOspfAreaDisable_Type()
)
wfOspfAreaDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaDisable.setStatus("mandatory")


class _WfOspfAreaState_Type(Integer32):
    """Custom type wfOspfAreaState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfOspfAreaState_Type.__name__ = "Integer32"
_WfOspfAreaState_Object = MibTableColumn
wfOspfAreaState = _WfOspfAreaState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 3),
    _WfOspfAreaState_Type()
)
wfOspfAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaState.setStatus("mandatory")
_WfOspfAreaId_Type = IpAddress
_WfOspfAreaId_Object = MibTableColumn
wfOspfAreaId = _WfOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 4),
    _WfOspfAreaId_Type()
)
wfOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaId.setStatus("mandatory")


class _WfOspfAuthType_Type(Integer32):
    """Custom type wfOspfAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nopassword", 1),
          ("simplepassword", 2))
    )


_WfOspfAuthType_Type.__name__ = "Integer32"
_WfOspfAuthType_Object = MibTableColumn
wfOspfAuthType = _WfOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 5),
    _WfOspfAuthType_Type()
)
wfOspfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAuthType.setStatus("mandatory")


class _WfOspfImportASExtern_Type(Integer32):
    """Custom type wfOspfImportASExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfImportASExtern_Type.__name__ = "Integer32"
_WfOspfImportASExtern_Object = MibTableColumn
wfOspfImportASExtern = _WfOspfImportASExtern_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 6),
    _WfOspfImportASExtern_Type()
)
wfOspfImportASExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfImportASExtern.setStatus("mandatory")


class _WfOspfStubMetric_Type(Integer32):
    """Custom type wfOspfStubMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16777215)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 16777215),
          ("minimum", 1))
    )


_WfOspfStubMetric_Type.__name__ = "Integer32"
_WfOspfStubMetric_Object = MibTableColumn
wfOspfStubMetric = _WfOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 7),
    _WfOspfStubMetric_Type()
)
wfOspfStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfStubMetric.setStatus("mandatory")


class _WfOspfImportSum_Type(Integer32):
    """Custom type wfOspfImportSum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfOspfImportSum_Type.__name__ = "Integer32"
_WfOspfImportSum_Object = MibTableColumn
wfOspfImportSum = _WfOspfImportSum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 2, 1, 8),
    _WfOspfImportSum_Type()
)
wfOspfImportSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfImportSum.setStatus("mandatory")
_WfOspfLsdbTable_Object = MibTable
wfOspfLsdbTable = _WfOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    wfOspfLsdbTable.setStatus("mandatory")
_WfOspfLsdbEntry_Object = MibTableRow
wfOspfLsdbEntry = _WfOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1)
)
wfOspfLsdbEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfLsdbAreaId"),
    (0, "Wellfleet-Series7-MIB", "wfOspfLsdbType"),
    (0, "Wellfleet-Series7-MIB", "wfOspfLsdbLSID"),
    (0, "Wellfleet-Series7-MIB", "wfOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    wfOspfLsdbEntry.setStatus("mandatory")
_WfOspfLsdbAreaId_Type = IpAddress
_WfOspfLsdbAreaId_Object = MibTableColumn
wfOspfLsdbAreaId = _WfOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 1),
    _WfOspfLsdbAreaId_Type()
)
wfOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbAreaId.setStatus("mandatory")


class _WfOspfLsdbType_Type(Integer32):
    """Custom type wfOspfLsdbType based on Integer32"""
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
        *(("asexternallink", 5),
          ("assummarylink", 4),
          ("networklink", 2),
          ("routerlink", 1),
          ("summarylink", 3))
    )


_WfOspfLsdbType_Type.__name__ = "Integer32"
_WfOspfLsdbType_Object = MibTableColumn
wfOspfLsdbType = _WfOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 2),
    _WfOspfLsdbType_Type()
)
wfOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbType.setStatus("mandatory")
_WfOspfLsdbLSID_Type = IpAddress
_WfOspfLsdbLSID_Object = MibTableColumn
wfOspfLsdbLSID = _WfOspfLsdbLSID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 3),
    _WfOspfLsdbLSID_Type()
)
wfOspfLsdbLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbLSID.setStatus("mandatory")
_WfOspfLsdbRouterId_Type = IpAddress
_WfOspfLsdbRouterId_Object = MibTableColumn
wfOspfLsdbRouterId = _WfOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 4),
    _WfOspfLsdbRouterId_Type()
)
wfOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbRouterId.setStatus("mandatory")
_WfOspfLsdbSequence_Type = Integer32
_WfOspfLsdbSequence_Object = MibTableColumn
wfOspfLsdbSequence = _WfOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 5),
    _WfOspfLsdbSequence_Type()
)
wfOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbSequence.setStatus("mandatory")


class _WfOspfLsdbAge_Type(Integer32):
    """Custom type wfOspfLsdbAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3600
        )
    )
    namedValues = NamedValues(
        ("lsdbmaxage", 3600)
    )


_WfOspfLsdbAge_Type.__name__ = "Integer32"
_WfOspfLsdbAge_Object = MibTableColumn
wfOspfLsdbAge = _WfOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 6),
    _WfOspfLsdbAge_Type()
)
wfOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbAge.setStatus("mandatory")
_WfOspfLsdbChecksum_Type = Integer32
_WfOspfLsdbChecksum_Object = MibTableColumn
wfOspfLsdbChecksum = _WfOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 7),
    _WfOspfLsdbChecksum_Type()
)
wfOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbChecksum.setStatus("mandatory")
_WfOspfLsdbAdvLen_Type = Integer32
_WfOspfLsdbAdvLen_Object = MibTableColumn
wfOspfLsdbAdvLen = _WfOspfLsdbAdvLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 3, 1, 8),
    _WfOspfLsdbAdvLen_Type()
)
wfOspfLsdbAdvLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfLsdbAdvLen.setStatus("mandatory")
_WfOspfAreaRangeTable_Object = MibTable
wfOspfAreaRangeTable = _WfOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    wfOspfAreaRangeTable.setStatus("mandatory")
_WfOspfAreaRangeEntry_Object = MibTableRow
wfOspfAreaRangeEntry = _WfOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1)
)
wfOspfAreaRangeEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfAreaRangeAreaID"),
    (0, "Wellfleet-Series7-MIB", "wfOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    wfOspfAreaRangeEntry.setStatus("mandatory")


class _WfOspfAreaRangeDelete_Type(Integer32):
    """Custom type wfOspfAreaRangeDelete based on Integer32"""
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


_WfOspfAreaRangeDelete_Type.__name__ = "Integer32"
_WfOspfAreaRangeDelete_Object = MibTableColumn
wfOspfAreaRangeDelete = _WfOspfAreaRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 1),
    _WfOspfAreaRangeDelete_Type()
)
wfOspfAreaRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaRangeDelete.setStatus("mandatory")


class _WfOspfAreaRangeDisable_Type(Integer32):
    """Custom type wfOspfAreaRangeDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOspfAreaRangeDisable_Type.__name__ = "Integer32"
_WfOspfAreaRangeDisable_Object = MibTableColumn
wfOspfAreaRangeDisable = _WfOspfAreaRangeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 2),
    _WfOspfAreaRangeDisable_Type()
)
wfOspfAreaRangeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaRangeDisable.setStatus("mandatory")


class _WfOspfAreaRangeState_Type(Integer32):
    """Custom type wfOspfAreaRangeState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfOspfAreaRangeState_Type.__name__ = "Integer32"
_WfOspfAreaRangeState_Object = MibTableColumn
wfOspfAreaRangeState = _WfOspfAreaRangeState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 3),
    _WfOspfAreaRangeState_Type()
)
wfOspfAreaRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaRangeState.setStatus("mandatory")
_WfOspfAreaRangeAreaID_Type = IpAddress
_WfOspfAreaRangeAreaID_Object = MibTableColumn
wfOspfAreaRangeAreaID = _WfOspfAreaRangeAreaID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 4),
    _WfOspfAreaRangeAreaID_Type()
)
wfOspfAreaRangeAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaRangeAreaID.setStatus("mandatory")
_WfOspfAreaRangeNet_Type = IpAddress
_WfOspfAreaRangeNet_Object = MibTableColumn
wfOspfAreaRangeNet = _WfOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 5),
    _WfOspfAreaRangeNet_Type()
)
wfOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAreaRangeNet.setStatus("mandatory")
_WfOspfAreaRangeMask_Type = IpAddress
_WfOspfAreaRangeMask_Object = MibTableColumn
wfOspfAreaRangeMask = _WfOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 4, 1, 6),
    _WfOspfAreaRangeMask_Type()
)
wfOspfAreaRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfAreaRangeMask.setStatus("mandatory")
_WfOspfIfTable_Object = MibTable
wfOspfIfTable = _WfOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    wfOspfIfTable.setStatus("mandatory")
_WfOspfIfEntry_Object = MibTableRow
wfOspfIfEntry = _WfOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1)
)
wfOspfIfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfIfIpAddress"),
    (0, "Wellfleet-Series7-MIB", "wfOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    wfOspfIfEntry.setStatus("mandatory")


class _WfOspfIfDelete_Type(Integer32):
    """Custom type wfOspfIfDelete based on Integer32"""
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


_WfOspfIfDelete_Type.__name__ = "Integer32"
_WfOspfIfDelete_Object = MibTableColumn
wfOspfIfDelete = _WfOspfIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 1),
    _WfOspfIfDelete_Type()
)
wfOspfIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfDelete.setStatus("mandatory")


class _WfOspfIfDisable_Type(Integer32):
    """Custom type wfOspfIfDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOspfIfDisable_Type.__name__ = "Integer32"
_WfOspfIfDisable_Object = MibTableColumn
wfOspfIfDisable = _WfOspfIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 2),
    _WfOspfIfDisable_Type()
)
wfOspfIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfDisable.setStatus("mandatory")


class _WfOspfIfState_Type(Integer32):
    """Custom type wfOspfIfState based on Integer32"""
    defaultValue = 1

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
        *(("backupdesignatedrouter", 6),
          ("designatedrouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherdesignatedrouter", 7),
          ("pointtopoint", 4),
          ("waiting", 3))
    )


_WfOspfIfState_Type.__name__ = "Integer32"
_WfOspfIfState_Object = MibTableColumn
wfOspfIfState = _WfOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 3),
    _WfOspfIfState_Type()
)
wfOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfState.setStatus("mandatory")
_WfOspfIfIpAddress_Type = IpAddress
_WfOspfIfIpAddress_Object = MibTableColumn
wfOspfIfIpAddress = _WfOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 4),
    _WfOspfIfIpAddress_Type()
)
wfOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfIpAddress.setStatus("mandatory")
_WfOspfAddressLessIf_Type = Integer32
_WfOspfAddressLessIf_Object = MibTableColumn
wfOspfAddressLessIf = _WfOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 5),
    _WfOspfAddressLessIf_Type()
)
wfOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfAddressLessIf.setStatus("mandatory")
_WfOspfIfAreaId_Type = IpAddress
_WfOspfIfAreaId_Object = MibTableColumn
wfOspfIfAreaId = _WfOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 6),
    _WfOspfIfAreaId_Type()
)
wfOspfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfAreaId.setStatus("mandatory")


class _WfOspfIfType_Type(Integer32):
    """Custom type wfOspfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointtopoint", 3))
    )


_WfOspfIfType_Type.__name__ = "Integer32"
_WfOspfIfType_Object = MibTableColumn
wfOspfIfType = _WfOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 7),
    _WfOspfIfType_Type()
)
wfOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfType.setStatus("mandatory")


class _WfOspfIfRtrPriority_Type(Integer32):
    """Custom type wfOspfIfRtrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 255))
    )


_WfOspfIfRtrPriority_Type.__name__ = "Integer32"
_WfOspfIfRtrPriority_Object = MibTableColumn
wfOspfIfRtrPriority = _WfOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 8),
    _WfOspfIfRtrPriority_Type()
)
wfOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfRtrPriority.setStatus("mandatory")


class _WfOspfIfTransitDelay_Type(Integer32):
    """Custom type wfOspfIfTransitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfIfTransitDelay_Type.__name__ = "Integer32"
_WfOspfIfTransitDelay_Object = MibTableColumn
wfOspfIfTransitDelay = _WfOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 9),
    _WfOspfIfTransitDelay_Type()
)
wfOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfTransitDelay.setStatus("mandatory")


class _WfOspfIfRetransInterval_Type(Integer32):
    """Custom type wfOspfIfRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("defval", 5),
          ("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfIfRetransInterval_Type.__name__ = "Integer32"
_WfOspfIfRetransInterval_Object = MibTableColumn
wfOspfIfRetransInterval = _WfOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 10),
    _WfOspfIfRetransInterval_Type()
)
wfOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfRetransInterval.setStatus("mandatory")


class _WfOspfIfHelloInterval_Type(Integer32):
    """Custom type wfOspfIfHelloInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("defval", 10),
          ("maximum", 65535),
          ("minimum", 1))
    )


_WfOspfIfHelloInterval_Type.__name__ = "Integer32"
_WfOspfIfHelloInterval_Object = MibTableColumn
wfOspfIfHelloInterval = _WfOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 11),
    _WfOspfIfHelloInterval_Type()
)
wfOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfHelloInterval.setStatus("mandatory")


class _WfOspfIfRtrDeadInterval_Type(Integer32):
    """Custom type wfOspfIfRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              40,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("defval", 40),
          ("maximum", 2147483647),
          ("minimum", 1))
    )


_WfOspfIfRtrDeadInterval_Type.__name__ = "Integer32"
_WfOspfIfRtrDeadInterval_Object = MibTableColumn
wfOspfIfRtrDeadInterval = _WfOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 12),
    _WfOspfIfRtrDeadInterval_Type()
)
wfOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfRtrDeadInterval.setStatus("mandatory")


class _WfOspfIfPollInterval_Type(Integer32):
    """Custom type wfOspfIfPollInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              120,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("defval", 120),
          ("maximum", 2147483647),
          ("minimum", 1))
    )


_WfOspfIfPollInterval_Type.__name__ = "Integer32"
_WfOspfIfPollInterval_Object = MibTableColumn
wfOspfIfPollInterval = _WfOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 13),
    _WfOspfIfPollInterval_Type()
)
wfOspfIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfPollInterval.setStatus("mandatory")
_WfOspfIfDesignatedRouter_Type = IpAddress
_WfOspfIfDesignatedRouter_Object = MibTableColumn
wfOspfIfDesignatedRouter = _WfOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 14),
    _WfOspfIfDesignatedRouter_Type()
)
wfOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfDesignatedRouter.setStatus("mandatory")
_WfOspfIfBackupDesignatedRouter_Type = IpAddress
_WfOspfIfBackupDesignatedRouter_Object = MibTableColumn
wfOspfIfBackupDesignatedRouter = _WfOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 15),
    _WfOspfIfBackupDesignatedRouter_Type()
)
wfOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfBackupDesignatedRouter.setStatus("mandatory")


class _WfOspfIfMetricCost_Type(Integer32):
    """Custom type wfOspfIfMetricCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 65535),
          ("minimum", 1))
    )


_WfOspfIfMetricCost_Type.__name__ = "Integer32"
_WfOspfIfMetricCost_Object = MibTableColumn
wfOspfIfMetricCost = _WfOspfIfMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 16),
    _WfOspfIfMetricCost_Type()
)
wfOspfIfMetricCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfMetricCost.setStatus("mandatory")
_WfOspfIfAuthKey_Type = OctetString
_WfOspfIfAuthKey_Object = MibTableColumn
wfOspfIfAuthKey = _WfOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 17),
    _WfOspfIfAuthKey_Type()
)
wfOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfIfAuthKey.setStatus("mandatory")
_WfOspfIfTxHellos_Type = Counter32
_WfOspfIfTxHellos_Object = MibTableColumn
wfOspfIfTxHellos = _WfOspfIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 18),
    _WfOspfIfTxHellos_Type()
)
wfOspfIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxHellos.setStatus("mandatory")
_WfOspfIfTxDBDescripts_Type = Counter32
_WfOspfIfTxDBDescripts_Object = MibTableColumn
wfOspfIfTxDBDescripts = _WfOspfIfTxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 19),
    _WfOspfIfTxDBDescripts_Type()
)
wfOspfIfTxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxDBDescripts.setStatus("mandatory")
_WfOspfIfTxLinkStateReqs_Type = Counter32
_WfOspfIfTxLinkStateReqs_Object = MibTableColumn
wfOspfIfTxLinkStateReqs = _WfOspfIfTxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 20),
    _WfOspfIfTxLinkStateReqs_Type()
)
wfOspfIfTxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxLinkStateReqs.setStatus("mandatory")
_WfOspfIfTxLinkStateUpds_Type = Counter32
_WfOspfIfTxLinkStateUpds_Object = MibTableColumn
wfOspfIfTxLinkStateUpds = _WfOspfIfTxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 21),
    _WfOspfIfTxLinkStateUpds_Type()
)
wfOspfIfTxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxLinkStateUpds.setStatus("mandatory")
_WfOspfIfTxLinkStateAcks_Type = Counter32
_WfOspfIfTxLinkStateAcks_Object = MibTableColumn
wfOspfIfTxLinkStateAcks = _WfOspfIfTxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 22),
    _WfOspfIfTxLinkStateAcks_Type()
)
wfOspfIfTxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfTxLinkStateAcks.setStatus("mandatory")
_WfOspfIfRxHellos_Type = Counter32
_WfOspfIfRxHellos_Object = MibTableColumn
wfOspfIfRxHellos = _WfOspfIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 23),
    _WfOspfIfRxHellos_Type()
)
wfOspfIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxHellos.setStatus("mandatory")
_WfOspfIfRxDBDescripts_Type = Counter32
_WfOspfIfRxDBDescripts_Object = MibTableColumn
wfOspfIfRxDBDescripts = _WfOspfIfRxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 24),
    _WfOspfIfRxDBDescripts_Type()
)
wfOspfIfRxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxDBDescripts.setStatus("mandatory")
_WfOspfIfRxLinkStateReqs_Type = Counter32
_WfOspfIfRxLinkStateReqs_Object = MibTableColumn
wfOspfIfRxLinkStateReqs = _WfOspfIfRxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 25),
    _WfOspfIfRxLinkStateReqs_Type()
)
wfOspfIfRxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxLinkStateReqs.setStatus("mandatory")
_WfOspfIfRxLinkStateUpds_Type = Counter32
_WfOspfIfRxLinkStateUpds_Object = MibTableColumn
wfOspfIfRxLinkStateUpds = _WfOspfIfRxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 26),
    _WfOspfIfRxLinkStateUpds_Type()
)
wfOspfIfRxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxLinkStateUpds.setStatus("mandatory")
_WfOspfIfRxLinkStateAcks_Type = Counter32
_WfOspfIfRxLinkStateAcks_Object = MibTableColumn
wfOspfIfRxLinkStateAcks = _WfOspfIfRxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 27),
    _WfOspfIfRxLinkStateAcks_Type()
)
wfOspfIfRxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfRxLinkStateAcks.setStatus("mandatory")
_WfOspfIfDrops_Type = Counter32
_WfOspfIfDrops_Object = MibTableColumn
wfOspfIfDrops = _WfOspfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 5, 1, 28),
    _WfOspfIfDrops_Type()
)
wfOspfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfIfDrops.setStatus("mandatory")
_WfOspfVirtIfTable_Object = MibTable
wfOspfVirtIfTable = _WfOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    wfOspfVirtIfTable.setStatus("mandatory")
_WfOspfVirtIfEntry_Object = MibTableRow
wfOspfVirtIfEntry = _WfOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1)
)
wfOspfVirtIfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfVirtIfAreaID"),
    (0, "Wellfleet-Series7-MIB", "wfOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    wfOspfVirtIfEntry.setStatus("mandatory")


class _WfOspfVirtIfDelete_Type(Integer32):
    """Custom type wfOspfVirtIfDelete based on Integer32"""
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


_WfOspfVirtIfDelete_Type.__name__ = "Integer32"
_WfOspfVirtIfDelete_Object = MibTableColumn
wfOspfVirtIfDelete = _WfOspfVirtIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 1),
    _WfOspfVirtIfDelete_Type()
)
wfOspfVirtIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfDelete.setStatus("mandatory")


class _WfOspfVirtIfDisable_Type(Integer32):
    """Custom type wfOspfVirtIfDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOspfVirtIfDisable_Type.__name__ = "Integer32"
_WfOspfVirtIfDisable_Object = MibTableColumn
wfOspfVirtIfDisable = _WfOspfVirtIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 2),
    _WfOspfVirtIfDisable_Type()
)
wfOspfVirtIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfDisable.setStatus("mandatory")


class _WfOspfVirtIfState_Type(Integer32):
    """Custom type wfOspfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointtopoint", 4))
    )


_WfOspfVirtIfState_Type.__name__ = "Integer32"
_WfOspfVirtIfState_Object = MibTableColumn
wfOspfVirtIfState = _WfOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 3),
    _WfOspfVirtIfState_Type()
)
wfOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfState.setStatus("mandatory")
_WfOspfVirtIfAreaID_Type = IpAddress
_WfOspfVirtIfAreaID_Object = MibTableColumn
wfOspfVirtIfAreaID = _WfOspfVirtIfAreaID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 4),
    _WfOspfVirtIfAreaID_Type()
)
wfOspfVirtIfAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfAreaID.setStatus("mandatory")
_WfOspfVirtIfNeighbor_Type = IpAddress
_WfOspfVirtIfNeighbor_Object = MibTableColumn
wfOspfVirtIfNeighbor = _WfOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 5),
    _WfOspfVirtIfNeighbor_Type()
)
wfOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfNeighbor.setStatus("mandatory")


class _WfOspfVirtIfTransitDelay_Type(Integer32):
    """Custom type wfOspfVirtIfTransitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfVirtIfTransitDelay_Type.__name__ = "Integer32"
_WfOspfVirtIfTransitDelay_Object = MibTableColumn
wfOspfVirtIfTransitDelay = _WfOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 6),
    _WfOspfVirtIfTransitDelay_Type()
)
wfOspfVirtIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfTransitDelay.setStatus("mandatory")


class _WfOspfVirtIfRetransInterval_Type(Integer32):
    """Custom type wfOspfVirtIfRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              3600)
        )
    )
    namedValues = NamedValues(
        *(("defval", 5),
          ("maximum", 3600),
          ("minimum", 1))
    )


_WfOspfVirtIfRetransInterval_Type.__name__ = "Integer32"
_WfOspfVirtIfRetransInterval_Object = MibTableColumn
wfOspfVirtIfRetransInterval = _WfOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 7),
    _WfOspfVirtIfRetransInterval_Type()
)
wfOspfVirtIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfRetransInterval.setStatus("mandatory")


class _WfOspfVirtIfHelloInterval_Type(Integer32):
    """Custom type wfOspfVirtIfHelloInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("defval", 15),
          ("maximum", 65535),
          ("minimum", 1))
    )


_WfOspfVirtIfHelloInterval_Type.__name__ = "Integer32"
_WfOspfVirtIfHelloInterval_Object = MibTableColumn
wfOspfVirtIfHelloInterval = _WfOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 8),
    _WfOspfVirtIfHelloInterval_Type()
)
wfOspfVirtIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfHelloInterval.setStatus("mandatory")


class _WfOspfVirtIfRtrDeadInterval_Type(Integer32):
    """Custom type wfOspfVirtIfRtrDeadInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              60,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("defval", 60),
          ("maximum", 2147483647),
          ("minimum", 1))
    )


_WfOspfVirtIfRtrDeadInterval_Type.__name__ = "Integer32"
_WfOspfVirtIfRtrDeadInterval_Object = MibTableColumn
wfOspfVirtIfRtrDeadInterval = _WfOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 9),
    _WfOspfVirtIfRtrDeadInterval_Type()
)
wfOspfVirtIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfRtrDeadInterval.setStatus("mandatory")
_WfOspfVirtIfAuthKey_Type = OctetString
_WfOspfVirtIfAuthKey_Object = MibTableColumn
wfOspfVirtIfAuthKey = _WfOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 10),
    _WfOspfVirtIfAuthKey_Type()
)
wfOspfVirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfVirtIfAuthKey.setStatus("mandatory")
_WfOspfVirtIfTxHellos_Type = Counter32
_WfOspfVirtIfTxHellos_Object = MibTableColumn
wfOspfVirtIfTxHellos = _WfOspfVirtIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 11),
    _WfOspfVirtIfTxHellos_Type()
)
wfOspfVirtIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxHellos.setStatus("mandatory")
_WfOspfVirtIfTxDBDescripts_Type = Counter32
_WfOspfVirtIfTxDBDescripts_Object = MibTableColumn
wfOspfVirtIfTxDBDescripts = _WfOspfVirtIfTxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 12),
    _WfOspfVirtIfTxDBDescripts_Type()
)
wfOspfVirtIfTxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxDBDescripts.setStatus("mandatory")
_WfOspfVirtIfTxLinkStateReqs_Type = Counter32
_WfOspfVirtIfTxLinkStateReqs_Object = MibTableColumn
wfOspfVirtIfTxLinkStateReqs = _WfOspfVirtIfTxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 13),
    _WfOspfVirtIfTxLinkStateReqs_Type()
)
wfOspfVirtIfTxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxLinkStateReqs.setStatus("mandatory")
_WfOspfVirtIfTxLinkStateUpds_Type = Counter32
_WfOspfVirtIfTxLinkStateUpds_Object = MibTableColumn
wfOspfVirtIfTxLinkStateUpds = _WfOspfVirtIfTxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 14),
    _WfOspfVirtIfTxLinkStateUpds_Type()
)
wfOspfVirtIfTxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxLinkStateUpds.setStatus("mandatory")
_WfOspfVirtIfTxLinkStateAcks_Type = Counter32
_WfOspfVirtIfTxLinkStateAcks_Object = MibTableColumn
wfOspfVirtIfTxLinkStateAcks = _WfOspfVirtIfTxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 15),
    _WfOspfVirtIfTxLinkStateAcks_Type()
)
wfOspfVirtIfTxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfTxLinkStateAcks.setStatus("mandatory")
_WfOspfVirtIfRxHellos_Type = Counter32
_WfOspfVirtIfRxHellos_Object = MibTableColumn
wfOspfVirtIfRxHellos = _WfOspfVirtIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 16),
    _WfOspfVirtIfRxHellos_Type()
)
wfOspfVirtIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxHellos.setStatus("mandatory")
_WfOspfVirtIfRxDBDescripts_Type = Counter32
_WfOspfVirtIfRxDBDescripts_Object = MibTableColumn
wfOspfVirtIfRxDBDescripts = _WfOspfVirtIfRxDBDescripts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 17),
    _WfOspfVirtIfRxDBDescripts_Type()
)
wfOspfVirtIfRxDBDescripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxDBDescripts.setStatus("mandatory")
_WfOspfVirtIfRxLinkStateReqs_Type = Counter32
_WfOspfVirtIfRxLinkStateReqs_Object = MibTableColumn
wfOspfVirtIfRxLinkStateReqs = _WfOspfVirtIfRxLinkStateReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 18),
    _WfOspfVirtIfRxLinkStateReqs_Type()
)
wfOspfVirtIfRxLinkStateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxLinkStateReqs.setStatus("mandatory")
_WfOspfVirtIfRxLinkStateUpds_Type = Counter32
_WfOspfVirtIfRxLinkStateUpds_Object = MibTableColumn
wfOspfVirtIfRxLinkStateUpds = _WfOspfVirtIfRxLinkStateUpds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 19),
    _WfOspfVirtIfRxLinkStateUpds_Type()
)
wfOspfVirtIfRxLinkStateUpds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxLinkStateUpds.setStatus("mandatory")
_WfOspfVirtIfRxLinkStateAcks_Type = Counter32
_WfOspfVirtIfRxLinkStateAcks_Object = MibTableColumn
wfOspfVirtIfRxLinkStateAcks = _WfOspfVirtIfRxLinkStateAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 20),
    _WfOspfVirtIfRxLinkStateAcks_Type()
)
wfOspfVirtIfRxLinkStateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfRxLinkStateAcks.setStatus("mandatory")
_WfOspfVirtIfDrops_Type = Counter32
_WfOspfVirtIfDrops_Object = MibTableColumn
wfOspfVirtIfDrops = _WfOspfVirtIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 6, 1, 21),
    _WfOspfVirtIfDrops_Type()
)
wfOspfVirtIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtIfDrops.setStatus("mandatory")
_WfOspfNbrTable_Object = MibTable
wfOspfNbrTable = _WfOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7)
)
if mibBuilder.loadTexts:
    wfOspfNbrTable.setStatus("mandatory")
_WfOspfNbrEntry_Object = MibTableRow
wfOspfNbrEntry = _WfOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1)
)
wfOspfNbrEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfNbrIpAddr"),
    (0, "Wellfleet-Series7-MIB", "wfOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    wfOspfNbrEntry.setStatus("mandatory")


class _WfOspfNbrDelete_Type(Integer32):
    """Custom type wfOspfNbrDelete based on Integer32"""
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


_WfOspfNbrDelete_Type.__name__ = "Integer32"
_WfOspfNbrDelete_Object = MibTableColumn
wfOspfNbrDelete = _WfOspfNbrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 1),
    _WfOspfNbrDelete_Type()
)
wfOspfNbrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrDelete.setStatus("mandatory")


class _WfOspfNbrDisable_Type(Integer32):
    """Custom type wfOspfNbrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOspfNbrDisable_Type.__name__ = "Integer32"
_WfOspfNbrDisable_Object = MibTableColumn
wfOspfNbrDisable = _WfOspfNbrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 2),
    _WfOspfNbrDisable_Type()
)
wfOspfNbrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrDisable.setStatus("mandatory")


class _WfOspfNbrState_Type(Integer32):
    """Custom type wfOspfNbrState based on Integer32"""
    defaultValue = 1

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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangstart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_WfOspfNbrState_Type.__name__ = "Integer32"
_WfOspfNbrState_Object = MibTableColumn
wfOspfNbrState = _WfOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 3),
    _WfOspfNbrState_Type()
)
wfOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrState.setStatus("mandatory")
_WfOspfNbrIpAddr_Type = IpAddress
_WfOspfNbrIpAddr_Object = MibTableColumn
wfOspfNbrIpAddr = _WfOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 4),
    _WfOspfNbrIpAddr_Type()
)
wfOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrIpAddr.setStatus("mandatory")
_WfOspfNbrIfAddr_Type = IpAddress
_WfOspfNbrIfAddr_Object = MibTableColumn
wfOspfNbrIfAddr = _WfOspfNbrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 5),
    _WfOspfNbrIfAddr_Type()
)
wfOspfNbrIfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrIfAddr.setStatus("mandatory")
_WfOspfNbrAddressLessIndex_Type = Integer32
_WfOspfNbrAddressLessIndex_Object = MibTableColumn
wfOspfNbrAddressLessIndex = _WfOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 6),
    _WfOspfNbrAddressLessIndex_Type()
)
wfOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrAddressLessIndex.setStatus("mandatory")
_WfOspfNbrRtrId_Type = IpAddress
_WfOspfNbrRtrId_Object = MibTableColumn
wfOspfNbrRtrId = _WfOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 7),
    _WfOspfNbrRtrId_Type()
)
wfOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrRtrId.setStatus("mandatory")
_WfOspfNbrOptions_Type = Integer32
_WfOspfNbrOptions_Object = MibTableColumn
wfOspfNbrOptions = _WfOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 8),
    _WfOspfNbrOptions_Type()
)
wfOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrOptions.setStatus("mandatory")


class _WfOspfNbrPriority_Type(Integer32):
    """Custom type wfOspfNbrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defval", 1),
          ("maximum", 255))
    )


_WfOspfNbrPriority_Type.__name__ = "Integer32"
_WfOspfNbrPriority_Object = MibTableColumn
wfOspfNbrPriority = _WfOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 9),
    _WfOspfNbrPriority_Type()
)
wfOspfNbrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOspfNbrPriority.setStatus("mandatory")
_WfOspfNbrEvents_Type = Counter32
_WfOspfNbrEvents_Object = MibTableColumn
wfOspfNbrEvents = _WfOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 10),
    _WfOspfNbrEvents_Type()
)
wfOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrEvents.setStatus("mandatory")
_WfOspfNbrLSRetransQLen_Type = Gauge32
_WfOspfNbrLSRetransQLen_Object = MibTableColumn
wfOspfNbrLSRetransQLen = _WfOspfNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 7, 1, 11),
    _WfOspfNbrLSRetransQLen_Type()
)
wfOspfNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfNbrLSRetransQLen.setStatus("mandatory")
_WfOspfVirtNbrTable_Object = MibTable
wfOspfVirtNbrTable = _WfOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8)
)
if mibBuilder.loadTexts:
    wfOspfVirtNbrTable.setStatus("mandatory")
_WfOspfVirtNbrEntry_Object = MibTableRow
wfOspfVirtNbrEntry = _WfOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1)
)
wfOspfVirtNbrEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfVirtNbrArea"),
    (0, "Wellfleet-Series7-MIB", "wfOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    wfOspfVirtNbrEntry.setStatus("mandatory")
_WfOspfVirtNbrArea_Type = IpAddress
_WfOspfVirtNbrArea_Object = MibTableColumn
wfOspfVirtNbrArea = _WfOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 1),
    _WfOspfVirtNbrArea_Type()
)
wfOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrArea.setStatus("mandatory")
_WfOspfVirtNbrRtrId_Type = IpAddress
_WfOspfVirtNbrRtrId_Object = MibTableColumn
wfOspfVirtNbrRtrId = _WfOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 2),
    _WfOspfVirtNbrRtrId_Type()
)
wfOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrRtrId.setStatus("mandatory")
_WfOspfVirtNbrIpAddr_Type = IpAddress
_WfOspfVirtNbrIpAddr_Object = MibTableColumn
wfOspfVirtNbrIpAddr = _WfOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 3),
    _WfOspfVirtNbrIpAddr_Type()
)
wfOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrIpAddr.setStatus("mandatory")
_WfOspfVirtNbrOptions_Type = Integer32
_WfOspfVirtNbrOptions_Object = MibTableColumn
wfOspfVirtNbrOptions = _WfOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 4),
    _WfOspfVirtNbrOptions_Type()
)
wfOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrOptions.setStatus("mandatory")


class _WfOspfVirtNbrState_Type(Integer32):
    """Custom type wfOspfVirtNbrState based on Integer32"""
    defaultValue = 1

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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangstart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_WfOspfVirtNbrState_Type.__name__ = "Integer32"
_WfOspfVirtNbrState_Object = MibTableColumn
wfOspfVirtNbrState = _WfOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 5),
    _WfOspfVirtNbrState_Type()
)
wfOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrState.setStatus("mandatory")
_WfOspfVirtNbrEvents_Type = Counter32
_WfOspfVirtNbrEvents_Object = MibTableColumn
wfOspfVirtNbrEvents = _WfOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 6),
    _WfOspfVirtNbrEvents_Type()
)
wfOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrEvents.setStatus("mandatory")
_WfOspfVirtNbrLSRetransQLen_Type = Gauge32
_WfOspfVirtNbrLSRetransQLen_Object = MibTableColumn
wfOspfVirtNbrLSRetransQLen = _WfOspfVirtNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 8, 1, 7),
    _WfOspfVirtNbrLSRetransQLen_Type()
)
wfOspfVirtNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfVirtNbrLSRetransQLen.setStatus("mandatory")
_WfOspfDynNbrTable_Object = MibTable
wfOspfDynNbrTable = _WfOspfDynNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9)
)
if mibBuilder.loadTexts:
    wfOspfDynNbrTable.setStatus("mandatory")
_WfOspfDynNbrEntry_Object = MibTableRow
wfOspfDynNbrEntry = _WfOspfDynNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1)
)
wfOspfDynNbrEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfOspfDynNbrIpAddr"),
    (0, "Wellfleet-Series7-MIB", "wfOspfDynNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    wfOspfDynNbrEntry.setStatus("mandatory")


class _WfOspfDynNbrState_Type(Integer32):
    """Custom type wfOspfDynNbrState based on Integer32"""
    defaultValue = 1

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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangstart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_WfOspfDynNbrState_Type.__name__ = "Integer32"
_WfOspfDynNbrState_Object = MibTableColumn
wfOspfDynNbrState = _WfOspfDynNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 1),
    _WfOspfDynNbrState_Type()
)
wfOspfDynNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrState.setStatus("mandatory")
_WfOspfDynNbrIpAddr_Type = IpAddress
_WfOspfDynNbrIpAddr_Object = MibTableColumn
wfOspfDynNbrIpAddr = _WfOspfDynNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 2),
    _WfOspfDynNbrIpAddr_Type()
)
wfOspfDynNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrIpAddr.setStatus("mandatory")
_WfOspfDynNbrIfAddr_Type = IpAddress
_WfOspfDynNbrIfAddr_Object = MibTableColumn
wfOspfDynNbrIfAddr = _WfOspfDynNbrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 3),
    _WfOspfDynNbrIfAddr_Type()
)
wfOspfDynNbrIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrIfAddr.setStatus("mandatory")
_WfOspfDynNbrAddressLessIndex_Type = Integer32
_WfOspfDynNbrAddressLessIndex_Object = MibTableColumn
wfOspfDynNbrAddressLessIndex = _WfOspfDynNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 4),
    _WfOspfDynNbrAddressLessIndex_Type()
)
wfOspfDynNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrAddressLessIndex.setStatus("mandatory")
_WfOspfDynNbrRtrId_Type = IpAddress
_WfOspfDynNbrRtrId_Object = MibTableColumn
wfOspfDynNbrRtrId = _WfOspfDynNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 5),
    _WfOspfDynNbrRtrId_Type()
)
wfOspfDynNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrRtrId.setStatus("mandatory")
_WfOspfDynNbrOptions_Type = Integer32
_WfOspfDynNbrOptions_Object = MibTableColumn
wfOspfDynNbrOptions = _WfOspfDynNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 6),
    _WfOspfDynNbrOptions_Type()
)
wfOspfDynNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrOptions.setStatus("mandatory")
_WfOspfDynNbrPriority_Type = Integer32
_WfOspfDynNbrPriority_Object = MibTableColumn
wfOspfDynNbrPriority = _WfOspfDynNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 7),
    _WfOspfDynNbrPriority_Type()
)
wfOspfDynNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrPriority.setStatus("mandatory")
_WfOspfDynNbrEvents_Type = Counter32
_WfOspfDynNbrEvents_Object = MibTableColumn
wfOspfDynNbrEvents = _WfOspfDynNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 8),
    _WfOspfDynNbrEvents_Type()
)
wfOspfDynNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrEvents.setStatus("mandatory")
_WfOspfDynNbrLSRetransQLen_Type = Gauge32
_WfOspfDynNbrLSRetransQLen_Object = MibTableColumn
wfOspfDynNbrLSRetransQLen = _WfOspfDynNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3, 9, 1, 9),
    _WfOspfDynNbrLSRetransQLen_Type()
)
wfOspfDynNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOspfDynNbrLSRetransQLen.setStatus("mandatory")
_WfEgpGroup_ObjectIdentity = ObjectIdentity
wfEgpGroup = _WfEgpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4)
)
_WfBgpGroup_ObjectIdentity = ObjectIdentity
wfBgpGroup = _WfBgpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5)
)
_WfTcpGroup_ObjectIdentity = ObjectIdentity
wfTcpGroup = _WfTcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3)
)
_WfUdpGroup_ObjectIdentity = ObjectIdentity
wfUdpGroup = _WfUdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4)
)
_WfSnmpGroup_ObjectIdentity = ObjectIdentity
wfSnmpGroup = _WfSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5)
)
_WfSnmp_ObjectIdentity = ObjectIdentity
wfSnmp = _WfSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1)
)


class _WfSnmpDisable_Type(Integer32):
    """Custom type wfSnmpDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSnmpDisable_Type.__name__ = "Integer32"
_WfSnmpDisable_Object = MibScalar
wfSnmpDisable = _WfSnmpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 1),
    _WfSnmpDisable_Type()
)
wfSnmpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpDisable.setStatus("mandatory")


class _WfSnmpUseLock_Type(Integer32):
    """Custom type wfSnmpUseLock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSnmpUseLock_Type.__name__ = "Integer32"
_WfSnmpUseLock_Object = MibScalar
wfSnmpUseLock = _WfSnmpUseLock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 2),
    _WfSnmpUseLock_Type()
)
wfSnmpUseLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpUseLock.setStatus("mandatory")
_WfSnmpLockAddress_Type = IpAddress
_WfSnmpLockAddress_Object = MibScalar
wfSnmpLockAddress = _WfSnmpLockAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 3),
    _WfSnmpLockAddress_Type()
)
wfSnmpLockAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpLockAddress.setStatus("mandatory")


class _WfSnmpLockTimeOut_Type(Integer32):
    """Custom type wfSnmpLockTimeOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              60)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("maximum", 60),
          ("minimum", 1))
    )


_WfSnmpLockTimeOut_Type.__name__ = "Integer32"
_WfSnmpLockTimeOut_Object = MibScalar
wfSnmpLockTimeOut = _WfSnmpLockTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 4),
    _WfSnmpLockTimeOut_Type()
)
wfSnmpLockTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpLockTimeOut.setStatus("mandatory")


class _WfSnmpAuth_Type(Integer32):
    """Custom type wfSnmpAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("party", 2),
          ("trivial", 1))
    )


_WfSnmpAuth_Type.__name__ = "Integer32"
_WfSnmpAuth_Object = MibScalar
wfSnmpAuth = _WfSnmpAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 5),
    _WfSnmpAuth_Type()
)
wfSnmpAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpAuth.setStatus("mandatory")
_WfSnmpInPkts_Type = Counter32
_WfSnmpInPkts_Object = MibScalar
wfSnmpInPkts = _WfSnmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 6),
    _WfSnmpInPkts_Type()
)
wfSnmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInPkts.setStatus("mandatory")
_WfSnmpOutPkts_Type = Counter32
_WfSnmpOutPkts_Object = MibScalar
wfSnmpOutPkts = _WfSnmpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 7),
    _WfSnmpOutPkts_Type()
)
wfSnmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutPkts.setStatus("mandatory")
_WfSnmpInBadVersions_Type = Counter32
_WfSnmpInBadVersions_Object = MibScalar
wfSnmpInBadVersions = _WfSnmpInBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 8),
    _WfSnmpInBadVersions_Type()
)
wfSnmpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadVersions.setStatus("mandatory")
_WfSnmpInBadCommunityNames_Type = Counter32
_WfSnmpInBadCommunityNames_Object = MibScalar
wfSnmpInBadCommunityNames = _WfSnmpInBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 9),
    _WfSnmpInBadCommunityNames_Type()
)
wfSnmpInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadCommunityNames.setStatus("mandatory")
_WfSnmpInBadCommunityUses_Type = Counter32
_WfSnmpInBadCommunityUses_Object = MibScalar
wfSnmpInBadCommunityUses = _WfSnmpInBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 10),
    _WfSnmpInBadCommunityUses_Type()
)
wfSnmpInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadCommunityUses.setStatus("mandatory")
_WfSnmpInASNParseErrs_Type = Counter32
_WfSnmpInASNParseErrs_Object = MibScalar
wfSnmpInASNParseErrs = _WfSnmpInASNParseErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 11),
    _WfSnmpInASNParseErrs_Type()
)
wfSnmpInASNParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInASNParseErrs.setStatus("mandatory")
_WfSnmpInBadTypes_Type = Counter32
_WfSnmpInBadTypes_Object = MibScalar
wfSnmpInBadTypes = _WfSnmpInBadTypes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 12),
    _WfSnmpInBadTypes_Type()
)
wfSnmpInBadTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadTypes.setStatus("mandatory")
_WfSnmpInTooBigs_Type = Counter32
_WfSnmpInTooBigs_Object = MibScalar
wfSnmpInTooBigs = _WfSnmpInTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 13),
    _WfSnmpInTooBigs_Type()
)
wfSnmpInTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTooBigs.setStatus("mandatory")
_WfSnmpInNoSuchNames_Type = Counter32
_WfSnmpInNoSuchNames_Object = MibScalar
wfSnmpInNoSuchNames = _WfSnmpInNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 14),
    _WfSnmpInNoSuchNames_Type()
)
wfSnmpInNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInNoSuchNames.setStatus("mandatory")
_WfSnmpInBadValues_Type = Counter32
_WfSnmpInBadValues_Object = MibScalar
wfSnmpInBadValues = _WfSnmpInBadValues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 15),
    _WfSnmpInBadValues_Type()
)
wfSnmpInBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInBadValues.setStatus("mandatory")
_WfSnmpInReadOnlys_Type = Counter32
_WfSnmpInReadOnlys_Object = MibScalar
wfSnmpInReadOnlys = _WfSnmpInReadOnlys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 16),
    _WfSnmpInReadOnlys_Type()
)
wfSnmpInReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInReadOnlys.setStatus("mandatory")
_WfSnmpInGenErrs_Type = Counter32
_WfSnmpInGenErrs_Object = MibScalar
wfSnmpInGenErrs = _WfSnmpInGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 17),
    _WfSnmpInGenErrs_Type()
)
wfSnmpInGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGenErrs.setStatus("mandatory")
_WfSnmpInTotalReqVars_Type = Counter32
_WfSnmpInTotalReqVars_Object = MibScalar
wfSnmpInTotalReqVars = _WfSnmpInTotalReqVars_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 18),
    _WfSnmpInTotalReqVars_Type()
)
wfSnmpInTotalReqVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTotalReqVars.setStatus("mandatory")
_WfSnmpInTotalSetVars_Type = Counter32
_WfSnmpInTotalSetVars_Object = MibScalar
wfSnmpInTotalSetVars = _WfSnmpInTotalSetVars_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 19),
    _WfSnmpInTotalSetVars_Type()
)
wfSnmpInTotalSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTotalSetVars.setStatus("mandatory")
_WfSnmpInGetRequests_Type = Counter32
_WfSnmpInGetRequests_Object = MibScalar
wfSnmpInGetRequests = _WfSnmpInGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 20),
    _WfSnmpInGetRequests_Type()
)
wfSnmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGetRequests.setStatus("mandatory")
_WfSnmpInGetNexts_Type = Counter32
_WfSnmpInGetNexts_Object = MibScalar
wfSnmpInGetNexts = _WfSnmpInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 21),
    _WfSnmpInGetNexts_Type()
)
wfSnmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGetNexts.setStatus("mandatory")
_WfSnmpInSetRequests_Type = Counter32
_WfSnmpInSetRequests_Object = MibScalar
wfSnmpInSetRequests = _WfSnmpInSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 22),
    _WfSnmpInSetRequests_Type()
)
wfSnmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInSetRequests.setStatus("mandatory")
_WfSnmpInGetResponses_Type = Counter32
_WfSnmpInGetResponses_Object = MibScalar
wfSnmpInGetResponses = _WfSnmpInGetResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 23),
    _WfSnmpInGetResponses_Type()
)
wfSnmpInGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInGetResponses.setStatus("mandatory")
_WfSnmpInTraps_Type = Counter32
_WfSnmpInTraps_Object = MibScalar
wfSnmpInTraps = _WfSnmpInTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 24),
    _WfSnmpInTraps_Type()
)
wfSnmpInTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpInTraps.setStatus("mandatory")
_WfSnmpOutTooBigs_Type = Counter32
_WfSnmpOutTooBigs_Object = MibScalar
wfSnmpOutTooBigs = _WfSnmpOutTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 25),
    _WfSnmpOutTooBigs_Type()
)
wfSnmpOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutTooBigs.setStatus("mandatory")
_WfSnmpOutNoSuchNames_Type = Counter32
_WfSnmpOutNoSuchNames_Object = MibScalar
wfSnmpOutNoSuchNames = _WfSnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 26),
    _WfSnmpOutNoSuchNames_Type()
)
wfSnmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutNoSuchNames.setStatus("mandatory")
_WfSnmpOutBadValues_Type = Counter32
_WfSnmpOutBadValues_Object = MibScalar
wfSnmpOutBadValues = _WfSnmpOutBadValues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 27),
    _WfSnmpOutBadValues_Type()
)
wfSnmpOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutBadValues.setStatus("mandatory")
_WfSnmpOutReadOnlys_Type = Counter32
_WfSnmpOutReadOnlys_Object = MibScalar
wfSnmpOutReadOnlys = _WfSnmpOutReadOnlys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 28),
    _WfSnmpOutReadOnlys_Type()
)
wfSnmpOutReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutReadOnlys.setStatus("mandatory")
_WfSnmpOutGenErrs_Type = Counter32
_WfSnmpOutGenErrs_Object = MibScalar
wfSnmpOutGenErrs = _WfSnmpOutGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 29),
    _WfSnmpOutGenErrs_Type()
)
wfSnmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGenErrs.setStatus("mandatory")
_WfSnmpOutGetRequests_Type = Counter32
_WfSnmpOutGetRequests_Object = MibScalar
wfSnmpOutGetRequests = _WfSnmpOutGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 30),
    _WfSnmpOutGetRequests_Type()
)
wfSnmpOutGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGetRequests.setStatus("mandatory")
_WfSnmpOutGetNexts_Type = Counter32
_WfSnmpOutGetNexts_Object = MibScalar
wfSnmpOutGetNexts = _WfSnmpOutGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 31),
    _WfSnmpOutGetNexts_Type()
)
wfSnmpOutGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGetNexts.setStatus("mandatory")
_WfSnmpOutSetRequests_Type = Counter32
_WfSnmpOutSetRequests_Object = MibScalar
wfSnmpOutSetRequests = _WfSnmpOutSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 32),
    _WfSnmpOutSetRequests_Type()
)
wfSnmpOutSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutSetRequests.setStatus("mandatory")
_WfSnmpOutGetResponses_Type = Counter32
_WfSnmpOutGetResponses_Object = MibScalar
wfSnmpOutGetResponses = _WfSnmpOutGetResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 33),
    _WfSnmpOutGetResponses_Type()
)
wfSnmpOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutGetResponses.setStatus("mandatory")
_WfSnmpOutTraps_Type = Counter32
_WfSnmpOutTraps_Object = MibScalar
wfSnmpOutTraps = _WfSnmpOutTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 34),
    _WfSnmpOutTraps_Type()
)
wfSnmpOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpOutTraps.setStatus("mandatory")


class _WfSnmpEnableAuthTraps_Type(Integer32):
    """Custom type wfSnmpEnableAuthTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSnmpEnableAuthTraps_Type.__name__ = "Integer32"
_WfSnmpEnableAuthTraps_Object = MibScalar
wfSnmpEnableAuthTraps = _WfSnmpEnableAuthTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 35),
    _WfSnmpEnableAuthTraps_Type()
)
wfSnmpEnableAuthTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpEnableAuthTraps.setStatus("mandatory")


class _WfSnmpTrapDebug_Type(Integer32):
    """Custom type wfSnmpTrapDebug based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapDebug_Type.__name__ = "Integer32"
_WfSnmpTrapDebug_Object = MibScalar
wfSnmpTrapDebug = _WfSnmpTrapDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 36),
    _WfSnmpTrapDebug_Type()
)
wfSnmpTrapDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapDebug.setStatus("mandatory")


class _WfSnmpTrapTrace_Type(Integer32):
    """Custom type wfSnmpTrapTrace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapTrace_Type.__name__ = "Integer32"
_WfSnmpTrapTrace_Object = MibScalar
wfSnmpTrapTrace = _WfSnmpTrapTrace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 37),
    _WfSnmpTrapTrace_Type()
)
wfSnmpTrapTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapTrace.setStatus("mandatory")


class _WfSnmpTrapInfo_Type(Integer32):
    """Custom type wfSnmpTrapInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapInfo_Type.__name__ = "Integer32"
_WfSnmpTrapInfo_Object = MibScalar
wfSnmpTrapInfo = _WfSnmpTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 38),
    _WfSnmpTrapInfo_Type()
)
wfSnmpTrapInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapInfo.setStatus("mandatory")


class _WfSnmpTrapWarn_Type(Integer32):
    """Custom type wfSnmpTrapWarn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapWarn_Type.__name__ = "Integer32"
_WfSnmpTrapWarn_Object = MibScalar
wfSnmpTrapWarn = _WfSnmpTrapWarn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 39),
    _WfSnmpTrapWarn_Type()
)
wfSnmpTrapWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapWarn.setStatus("mandatory")


class _WfSnmpTrapFault_Type(Integer32):
    """Custom type wfSnmpTrapFault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfSnmpTrapFault_Type.__name__ = "Integer32"
_WfSnmpTrapFault_Object = MibScalar
wfSnmpTrapFault = _WfSnmpTrapFault_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 40),
    _WfSnmpTrapFault_Type()
)
wfSnmpTrapFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpTrapFault.setStatus("mandatory")
_WfSnmpCommTable_Object = MibTable
wfSnmpCommTable = _WfSnmpCommTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2)
)
if mibBuilder.loadTexts:
    wfSnmpCommTable.setStatus("mandatory")
_WfSnmpCommEntry_Object = MibTableRow
wfSnmpCommEntry = _WfSnmpCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1)
)
wfSnmpCommEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSnmpCommIndex"),
)
if mibBuilder.loadTexts:
    wfSnmpCommEntry.setStatus("mandatory")


class _WfSnmpCommDelete_Type(Integer32):
    """Custom type wfSnmpCommDelete based on Integer32"""
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


_WfSnmpCommDelete_Type.__name__ = "Integer32"
_WfSnmpCommDelete_Object = MibTableColumn
wfSnmpCommDelete = _WfSnmpCommDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 1),
    _WfSnmpCommDelete_Type()
)
wfSnmpCommDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommDelete.setStatus("mandatory")
_WfSnmpCommIndex_Type = Integer32
_WfSnmpCommIndex_Object = MibTableColumn
wfSnmpCommIndex = _WfSnmpCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 2),
    _WfSnmpCommIndex_Type()
)
wfSnmpCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpCommIndex.setStatus("mandatory")
_WfSnmpCommName_Type = DisplayString
_WfSnmpCommName_Object = MibTableColumn
wfSnmpCommName = _WfSnmpCommName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 3),
    _WfSnmpCommName_Type()
)
wfSnmpCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommName.setStatus("mandatory")


class _WfSnmpCommAccess_Type(Integer32):
    """Custom type wfSnmpCommAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_WfSnmpCommAccess_Type.__name__ = "Integer32"
_WfSnmpCommAccess_Object = MibTableColumn
wfSnmpCommAccess = _WfSnmpCommAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 4),
    _WfSnmpCommAccess_Type()
)
wfSnmpCommAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpCommAccess.setStatus("mandatory")
_WfSnmpMgrTable_Object = MibTable
wfSnmpMgrTable = _WfSnmpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3)
)
if mibBuilder.loadTexts:
    wfSnmpMgrTable.setStatus("mandatory")
_WfSnmpMgrEntry_Object = MibTableRow
wfSnmpMgrEntry = _WfSnmpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1)
)
wfSnmpMgrEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSnmpMgrCommIndex"),
    (0, "Wellfleet-Series7-MIB", "wfSnmpMgrAddress"),
)
if mibBuilder.loadTexts:
    wfSnmpMgrEntry.setStatus("mandatory")


class _WfSnmpMgrDelete_Type(Integer32):
    """Custom type wfSnmpMgrDelete based on Integer32"""
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


_WfSnmpMgrDelete_Type.__name__ = "Integer32"
_WfSnmpMgrDelete_Object = MibTableColumn
wfSnmpMgrDelete = _WfSnmpMgrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 1),
    _WfSnmpMgrDelete_Type()
)
wfSnmpMgrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrDelete.setStatus("mandatory")
_WfSnmpMgrCommIndex_Type = Integer32
_WfSnmpMgrCommIndex_Object = MibTableColumn
wfSnmpMgrCommIndex = _WfSnmpMgrCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 2),
    _WfSnmpMgrCommIndex_Type()
)
wfSnmpMgrCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrCommIndex.setStatus("mandatory")
_WfSnmpMgrAddress_Type = IpAddress
_WfSnmpMgrAddress_Object = MibTableColumn
wfSnmpMgrAddress = _WfSnmpMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 3),
    _WfSnmpMgrAddress_Type()
)
wfSnmpMgrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSnmpMgrAddress.setStatus("mandatory")
_WfSnmpMgrName_Type = DisplayString
_WfSnmpMgrName_Object = MibTableColumn
wfSnmpMgrName = _WfSnmpMgrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 4),
    _WfSnmpMgrName_Type()
)
wfSnmpMgrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrName.setStatus("mandatory")


class _WfSnmpMgrTrapPort_Type(Integer32):
    """Custom type wfSnmpMgrTrapPort based on Integer32"""
    defaultValue = 162


_WfSnmpMgrTrapPort_Object = MibTableColumn
wfSnmpMgrTrapPort = _WfSnmpMgrTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 5),
    _WfSnmpMgrTrapPort_Type()
)
wfSnmpMgrTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrTrapPort.setStatus("mandatory")


class _WfSnmpMgrTraps_Type(Integer32):
    """Custom type wfSnmpMgrTraps based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("generic", 2),
          ("none", 1),
          ("specific", 4))
    )


_WfSnmpMgrTraps_Type.__name__ = "Integer32"
_WfSnmpMgrTraps_Object = MibTableColumn
wfSnmpMgrTraps = _WfSnmpMgrTraps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 6),
    _WfSnmpMgrTraps_Type()
)
wfSnmpMgrTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSnmpMgrTraps.setStatus("mandatory")
_WfFakeEvent_ObjectIdentity = ObjectIdentity
wfFakeEvent = _WfFakeEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4)
)
_WfFakeEventString_Type = DisplayString
_WfFakeEventString_Object = MibScalar
wfFakeEventString = _WfFakeEventString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4, 1),
    _WfFakeEventString_Type()
)
wfFakeEventString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFakeEventString.setStatus("optional")
_WfTftp_ObjectIdentity = ObjectIdentity
wfTftp = _WfTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6)
)


class _WfTftpDisable_Type(Integer32):
    """Custom type wfTftpDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfTftpDisable_Type.__name__ = "Integer32"
_WfTftpDisable_Object = MibScalar
wfTftpDisable = _WfTftpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 1),
    _WfTftpDisable_Type()
)
wfTftpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpDisable.setStatus("mandatory")


class _WfTftpDefaultVolume_Type(Integer32):
    """Custom type wfTftpDefaultVolume based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              2,
              14)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("maximum", 14),
          ("minimum", 2))
    )


_WfTftpDefaultVolume_Type.__name__ = "Integer32"
_WfTftpDefaultVolume_Object = MibScalar
wfTftpDefaultVolume = _WfTftpDefaultVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 2),
    _WfTftpDefaultVolume_Type()
)
wfTftpDefaultVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpDefaultVolume.setStatus("mandatory")
_WfTftpXfers_Type = Counter32
_WfTftpXfers_Object = MibScalar
wfTftpXfers = _WfTftpXfers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 3),
    _WfTftpXfers_Type()
)
wfTftpXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpXfers.setStatus("mandatory")


class _WfTftpTimeOut_Type(Integer32):
    """Custom type wfTftpTimeOut based on Integer32"""
    defaultValue = 5


_WfTftpTimeOut_Object = MibScalar
wfTftpTimeOut = _WfTftpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 4),
    _WfTftpTimeOut_Type()
)
wfTftpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpTimeOut.setStatus("mandatory")


class _WfTftpCloseTimeOut_Type(Integer32):
    """Custom type wfTftpCloseTimeOut based on Integer32"""
    defaultValue = 25


_WfTftpCloseTimeOut_Object = MibScalar
wfTftpCloseTimeOut = _WfTftpCloseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 5),
    _WfTftpCloseTimeOut_Type()
)
wfTftpCloseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpCloseTimeOut.setStatus("mandatory")


class _WfTftpRexmit_Type(Integer32):
    """Custom type wfTftpRexmit based on Integer32"""
    defaultValue = 5


_WfTftpRexmit_Object = MibScalar
wfTftpRexmit = _WfTftpRexmit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 6),
    _WfTftpRexmit_Type()
)
wfTftpRexmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpRexmit.setStatus("mandatory")
_WfTftpInFiles_Type = Counter32
_WfTftpInFiles_Object = MibScalar
wfTftpInFiles = _WfTftpInFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 7),
    _WfTftpInFiles_Type()
)
wfTftpInFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInFiles.setStatus("mandatory")
_WfTftpOutFiles_Type = Counter32
_WfTftpOutFiles_Object = MibScalar
wfTftpOutFiles = _WfTftpOutFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 8),
    _WfTftpOutFiles_Type()
)
wfTftpOutFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutFiles.setStatus("mandatory")
_WfTftpInWRQ_Type = Counter32
_WfTftpInWRQ_Object = MibScalar
wfTftpInWRQ = _WfTftpInWRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 9),
    _WfTftpInWRQ_Type()
)
wfTftpInWRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInWRQ.setStatus("mandatory")
_WfTftpOutWRQ_Type = Counter32
_WfTftpOutWRQ_Object = MibScalar
wfTftpOutWRQ = _WfTftpOutWRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 10),
    _WfTftpOutWRQ_Type()
)
wfTftpOutWRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutWRQ.setStatus("mandatory")
_WfTftpInRRQ_Type = Counter32
_WfTftpInRRQ_Object = MibScalar
wfTftpInRRQ = _WfTftpInRRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 11),
    _WfTftpInRRQ_Type()
)
wfTftpInRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInRRQ.setStatus("mandatory")
_WfTftpOutRRQ_Type = Counter32
_WfTftpOutRRQ_Object = MibScalar
wfTftpOutRRQ = _WfTftpOutRRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 12),
    _WfTftpOutRRQ_Type()
)
wfTftpOutRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutRRQ.setStatus("mandatory")
_WfTftpRexmitPkts_Type = Counter32
_WfTftpRexmitPkts_Object = MibScalar
wfTftpRexmitPkts = _WfTftpRexmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 13),
    _WfTftpRexmitPkts_Type()
)
wfTftpRexmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpRexmitPkts.setStatus("mandatory")
_WfTftpInErr_Type = Counter32
_WfTftpInErr_Object = MibScalar
wfTftpInErr = _WfTftpInErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 14),
    _WfTftpInErr_Type()
)
wfTftpInErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInErr.setStatus("mandatory")
_WfTftpOutErr_Type = Counter32
_WfTftpOutErr_Object = MibScalar
wfTftpOutErr = _WfTftpOutErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 15),
    _WfTftpOutErr_Type()
)
wfTftpOutErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutErr.setStatus("mandatory")
_WfTftpAborts_Type = Counter32
_WfTftpAborts_Object = MibScalar
wfTftpAborts = _WfTftpAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 16),
    _WfTftpAborts_Type()
)
wfTftpAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpAborts.setStatus("mandatory")
_WfTelnetGroup_ObjectIdentity = ObjectIdentity
wfTelnetGroup = _WfTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7)
)
_WfBootpGroup_ObjectIdentity = ObjectIdentity
wfBootpGroup = _WfBootpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8)
)
_WfAppletalkGroup_ObjectIdentity = ObjectIdentity
wfAppletalkGroup = _WfAppletalkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4)
)
_WfAppleBase_ObjectIdentity = ObjectIdentity
wfAppleBase = _WfAppleBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1)
)


class _WfAppleBaseDelete_Type(Integer32):
    """Custom type wfAppleBaseDelete based on Integer32"""
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


_WfAppleBaseDelete_Type.__name__ = "Integer32"
_WfAppleBaseDelete_Object = MibScalar
wfAppleBaseDelete = _WfAppleBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 1),
    _WfAppleBaseDelete_Type()
)
wfAppleBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDelete.setStatus("mandatory")


class _WfAppleBaseDisable_Type(Integer32):
    """Custom type wfAppleBaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfAppleBaseDisable_Type.__name__ = "Integer32"
_WfAppleBaseDisable_Object = MibScalar
wfAppleBaseDisable = _WfAppleBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 2),
    _WfAppleBaseDisable_Type()
)
wfAppleBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDisable.setStatus("mandatory")


class _WfAppleBaseState_Type(Integer32):
    """Custom type wfAppleBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfAppleBaseState_Type.__name__ = "Integer32"
_WfAppleBaseState_Object = MibScalar
wfAppleBaseState = _WfAppleBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 3),
    _WfAppleBaseState_Type()
)
wfAppleBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseState.setStatus("mandatory")
_WfAppleBaseDebugLevel_Type = Integer32
_WfAppleBaseDebugLevel_Object = MibScalar
wfAppleBaseDebugLevel = _WfAppleBaseDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 4),
    _WfAppleBaseDebugLevel_Type()
)
wfAppleBaseDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDebugLevel.setStatus("mandatory")


class _WfAppleBaseDdpQueLen_Type(Integer32):
    """Custom type wfAppleBaseDdpQueLen based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfAppleBaseDdpQueLen_Type.__name__ = "Integer32"
_WfAppleBaseDdpQueLen_Object = MibScalar
wfAppleBaseDdpQueLen = _WfAppleBaseDdpQueLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 5),
    _WfAppleBaseDdpQueLen_Type()
)
wfAppleBaseDdpQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDdpQueLen.setStatus("mandatory")
_WfAppleBaseHomedPort_Type = Integer32
_WfAppleBaseHomedPort_Object = MibScalar
wfAppleBaseHomedPort = _WfAppleBaseHomedPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 6),
    _WfAppleBaseHomedPort_Type()
)
wfAppleBaseHomedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseHomedPort.setStatus("mandatory")
_WfAppleBaseTotalNets_Type = Integer32
_WfAppleBaseTotalNets_Object = MibScalar
wfAppleBaseTotalNets = _WfAppleBaseTotalNets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 7),
    _WfAppleBaseTotalNets_Type()
)
wfAppleBaseTotalNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseTotalNets.setStatus("mandatory")
_WfAppleBaseTotalZones_Type = Integer32
_WfAppleBaseTotalZones_Object = MibScalar
wfAppleBaseTotalZones = _WfAppleBaseTotalZones_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 8),
    _WfAppleBaseTotalZones_Type()
)
wfAppleBaseTotalZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseTotalZones.setStatus("mandatory")
_WfAppleRtmpTable_Object = MibTable
wfAppleRtmpTable = _WfAppleRtmpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    wfAppleRtmpTable.setStatus("mandatory")
_WfAppleRtmpEntry_Object = MibTableRow
wfAppleRtmpEntry = _WfAppleRtmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1)
)
wfAppleRtmpEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfAppleRtmpNetStart"),
    (0, "Wellfleet-Series7-MIB", "wfAppleRtmpNetEnd"),
)
if mibBuilder.loadTexts:
    wfAppleRtmpEntry.setStatus("mandatory")
_WfAppleRtmpNetStart_Type = Integer32
_WfAppleRtmpNetStart_Object = MibTableColumn
wfAppleRtmpNetStart = _WfAppleRtmpNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 1),
    _WfAppleRtmpNetStart_Type()
)
wfAppleRtmpNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNetStart.setStatus("mandatory")
_WfAppleRtmpNetEnd_Type = Integer32
_WfAppleRtmpNetEnd_Object = MibTableColumn
wfAppleRtmpNetEnd = _WfAppleRtmpNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 2),
    _WfAppleRtmpNetEnd_Type()
)
wfAppleRtmpNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNetEnd.setStatus("mandatory")
_WfAppleRtmpPort_Type = Integer32
_WfAppleRtmpPort_Object = MibTableColumn
wfAppleRtmpPort = _WfAppleRtmpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 3),
    _WfAppleRtmpPort_Type()
)
wfAppleRtmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpPort.setStatus("mandatory")
_WfAppleRtmpHops_Type = Integer32
_WfAppleRtmpHops_Object = MibTableColumn
wfAppleRtmpHops = _WfAppleRtmpHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 4),
    _WfAppleRtmpHops_Type()
)
wfAppleRtmpHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpHops.setStatus("mandatory")
_WfAppleRtmpNextHopNet_Type = Integer32
_WfAppleRtmpNextHopNet_Object = MibTableColumn
wfAppleRtmpNextHopNet = _WfAppleRtmpNextHopNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 5),
    _WfAppleRtmpNextHopNet_Type()
)
wfAppleRtmpNextHopNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNextHopNet.setStatus("mandatory")
_WfAppleRtmpNextHopNode_Type = Integer32
_WfAppleRtmpNextHopNode_Object = MibTableColumn
wfAppleRtmpNextHopNode = _WfAppleRtmpNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 6),
    _WfAppleRtmpNextHopNode_Type()
)
wfAppleRtmpNextHopNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNextHopNode.setStatus("mandatory")


class _WfAppleRtmpState_Type(Integer32):
    """Custom type wfAppleRtmpState based on Integer32"""
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
        *(("bad", 4),
          ("goingbad", 3),
          ("good", 1),
          ("suspect", 2))
    )


_WfAppleRtmpState_Type.__name__ = "Integer32"
_WfAppleRtmpState_Object = MibTableColumn
wfAppleRtmpState = _WfAppleRtmpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 7),
    _WfAppleRtmpState_Type()
)
wfAppleRtmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleRtmpState.setStatus("mandatory")
_WfApplePortTable_Object = MibTable
wfApplePortTable = _WfApplePortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    wfApplePortTable.setStatus("mandatory")
_WfApplePortEntry_Object = MibTableRow
wfApplePortEntry = _WfApplePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1)
)
wfApplePortEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfApplePortCircuit"),
)
if mibBuilder.loadTexts:
    wfApplePortEntry.setStatus("mandatory")


class _WfApplePortDelete_Type(Integer32):
    """Custom type wfApplePortDelete based on Integer32"""
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


_WfApplePortDelete_Type.__name__ = "Integer32"
_WfApplePortDelete_Object = MibTableColumn
wfApplePortDelete = _WfApplePortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 1),
    _WfApplePortDelete_Type()
)
wfApplePortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortDelete.setStatus("mandatory")


class _WfApplePortDisable_Type(Integer32):
    """Custom type wfApplePortDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfApplePortDisable_Type.__name__ = "Integer32"
_WfApplePortDisable_Object = MibTableColumn
wfApplePortDisable = _WfApplePortDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 2),
    _WfApplePortDisable_Type()
)
wfApplePortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortDisable.setStatus("mandatory")
_WfApplePortCircuit_Type = Integer32
_WfApplePortCircuit_Object = MibTableColumn
wfApplePortCircuit = _WfApplePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 3),
    _WfApplePortCircuit_Type()
)
wfApplePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCircuit.setStatus("mandatory")


class _WfApplePortState_Type(Integer32):
    """Custom type wfApplePortState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfApplePortState_Type.__name__ = "Integer32"
_WfApplePortState_Object = MibTableColumn
wfApplePortState = _WfApplePortState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 4),
    _WfApplePortState_Type()
)
wfApplePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortState.setStatus("mandatory")
_WfApplePortType_Type = Integer32
_WfApplePortType_Object = MibTableColumn
wfApplePortType = _WfApplePortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 5),
    _WfApplePortType_Type()
)
wfApplePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortType.setStatus("mandatory")


class _WfApplePortCksumDisable_Type(Integer32):
    """Custom type wfApplePortCksumDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfApplePortCksumDisable_Type.__name__ = "Integer32"
_WfApplePortCksumDisable_Object = MibTableColumn
wfApplePortCksumDisable = _WfApplePortCksumDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 6),
    _WfApplePortCksumDisable_Type()
)
wfApplePortCksumDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortCksumDisable.setStatus("mandatory")


class _WfApplePortTrEndStation_Type(Integer32):
    """Custom type wfApplePortTrEndStation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfApplePortTrEndStation_Type.__name__ = "Integer32"
_WfApplePortTrEndStation_Object = MibTableColumn
wfApplePortTrEndStation = _WfApplePortTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 7),
    _WfApplePortTrEndStation_Type()
)
wfApplePortTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortTrEndStation.setStatus("mandatory")
_WfApplePortGniForever_Type = Integer32
_WfApplePortGniForever_Object = MibTableColumn
wfApplePortGniForever = _WfApplePortGniForever_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 8),
    _WfApplePortGniForever_Type()
)
wfApplePortGniForever.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortGniForever.setStatus("mandatory")
_WfApplePortAarpFlush_Type = Integer32
_WfApplePortAarpFlush_Object = MibTableColumn
wfApplePortAarpFlush = _WfApplePortAarpFlush_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 9),
    _WfApplePortAarpFlush_Type()
)
wfApplePortAarpFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpFlush.setStatus("mandatory")
_WfApplePortMacAddress_Type = OctetString
_WfApplePortMacAddress_Object = MibTableColumn
wfApplePortMacAddress = _WfApplePortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 10),
    _WfApplePortMacAddress_Type()
)
wfApplePortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortMacAddress.setStatus("mandatory")
_WfApplePortNodeId_Type = Integer32
_WfApplePortNodeId_Object = MibTableColumn
wfApplePortNodeId = _WfApplePortNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 11),
    _WfApplePortNodeId_Type()
)
wfApplePortNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNodeId.setStatus("mandatory")
_WfApplePortNetwork_Type = Integer32
_WfApplePortNetwork_Object = MibTableColumn
wfApplePortNetwork = _WfApplePortNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 12),
    _WfApplePortNetwork_Type()
)
wfApplePortNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNetwork.setStatus("mandatory")
_WfApplePortNetStart_Type = Integer32
_WfApplePortNetStart_Object = MibTableColumn
wfApplePortNetStart = _WfApplePortNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 13),
    _WfApplePortNetStart_Type()
)
wfApplePortNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNetStart.setStatus("mandatory")
_WfApplePortNetEnd_Type = Integer32
_WfApplePortNetEnd_Object = MibTableColumn
wfApplePortNetEnd = _WfApplePortNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 14),
    _WfApplePortNetEnd_Type()
)
wfApplePortNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNetEnd.setStatus("mandatory")
_WfApplePortDfltZone_Type = DisplayString
_WfApplePortDfltZone_Object = MibTableColumn
wfApplePortDfltZone = _WfApplePortDfltZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 15),
    _WfApplePortDfltZone_Type()
)
wfApplePortDfltZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortDfltZone.setStatus("mandatory")
_WfApplePortCurMacAddress_Type = OctetString
_WfApplePortCurMacAddress_Object = MibTableColumn
wfApplePortCurMacAddress = _WfApplePortCurMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 16),
    _WfApplePortCurMacAddress_Type()
)
wfApplePortCurMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurMacAddress.setStatus("mandatory")
_WfApplePortCurNodeId_Type = Integer32
_WfApplePortCurNodeId_Object = MibTableColumn
wfApplePortCurNodeId = _WfApplePortCurNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 17),
    _WfApplePortCurNodeId_Type()
)
wfApplePortCurNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNodeId.setStatus("mandatory")
_WfApplePortCurNetwork_Type = Integer32
_WfApplePortCurNetwork_Object = MibTableColumn
wfApplePortCurNetwork = _WfApplePortCurNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 18),
    _WfApplePortCurNetwork_Type()
)
wfApplePortCurNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNetwork.setStatus("mandatory")
_WfApplePortCurNetStart_Type = Integer32
_WfApplePortCurNetStart_Object = MibTableColumn
wfApplePortCurNetStart = _WfApplePortCurNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 19),
    _WfApplePortCurNetStart_Type()
)
wfApplePortCurNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNetStart.setStatus("mandatory")
_WfApplePortCurNetEnd_Type = Integer32
_WfApplePortCurNetEnd_Object = MibTableColumn
wfApplePortCurNetEnd = _WfApplePortCurNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 20),
    _WfApplePortCurNetEnd_Type()
)
wfApplePortCurNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNetEnd.setStatus("mandatory")
_WfApplePortCurDfltZone_Type = DisplayString
_WfApplePortCurDfltZone_Object = MibTableColumn
wfApplePortCurDfltZone = _WfApplePortCurDfltZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 21),
    _WfApplePortCurDfltZone_Type()
)
wfApplePortCurDfltZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurDfltZone.setStatus("mandatory")
_WfApplePortAarpProbeRxs_Type = Counter32
_WfApplePortAarpProbeRxs_Object = MibTableColumn
wfApplePortAarpProbeRxs = _WfApplePortAarpProbeRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 22),
    _WfApplePortAarpProbeRxs_Type()
)
wfApplePortAarpProbeRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpProbeRxs.setStatus("mandatory")
_WfApplePortAarpProbeTxs_Type = Counter32
_WfApplePortAarpProbeTxs_Object = MibTableColumn
wfApplePortAarpProbeTxs = _WfApplePortAarpProbeTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 23),
    _WfApplePortAarpProbeTxs_Type()
)
wfApplePortAarpProbeTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpProbeTxs.setStatus("mandatory")
_WfApplePortAarpReqRxs_Type = Counter32
_WfApplePortAarpReqRxs_Object = MibTableColumn
wfApplePortAarpReqRxs = _WfApplePortAarpReqRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 24),
    _WfApplePortAarpReqRxs_Type()
)
wfApplePortAarpReqRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpReqRxs.setStatus("mandatory")
_WfApplePortAarpReqTxs_Type = Counter32
_WfApplePortAarpReqTxs_Object = MibTableColumn
wfApplePortAarpReqTxs = _WfApplePortAarpReqTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 25),
    _WfApplePortAarpReqTxs_Type()
)
wfApplePortAarpReqTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpReqTxs.setStatus("mandatory")
_WfApplePortAarpRspRxs_Type = Counter32
_WfApplePortAarpRspRxs_Object = MibTableColumn
wfApplePortAarpRspRxs = _WfApplePortAarpRspRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 26),
    _WfApplePortAarpRspRxs_Type()
)
wfApplePortAarpRspRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpRspRxs.setStatus("mandatory")
_WfApplePortAarpRspTxs_Type = Counter32
_WfApplePortAarpRspTxs_Object = MibTableColumn
wfApplePortAarpRspTxs = _WfApplePortAarpRspTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 27),
    _WfApplePortAarpRspTxs_Type()
)
wfApplePortAarpRspTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpRspTxs.setStatus("mandatory")
_WfApplePortDdpOutRequests_Type = Counter32
_WfApplePortDdpOutRequests_Object = MibTableColumn
wfApplePortDdpOutRequests = _WfApplePortDdpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 28),
    _WfApplePortDdpOutRequests_Type()
)
wfApplePortDdpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpOutRequests.setStatus("mandatory")
_WfApplePortDdpInReceives_Type = Counter32
_WfApplePortDdpInReceives_Object = MibTableColumn
wfApplePortDdpInReceives = _WfApplePortDdpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 29),
    _WfApplePortDdpInReceives_Type()
)
wfApplePortDdpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpInReceives.setStatus("mandatory")
_WfApplePortDdpInLocalDatagrams_Type = Counter32
_WfApplePortDdpInLocalDatagrams_Object = MibTableColumn
wfApplePortDdpInLocalDatagrams = _WfApplePortDdpInLocalDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 30),
    _WfApplePortDdpInLocalDatagrams_Type()
)
wfApplePortDdpInLocalDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpInLocalDatagrams.setStatus("mandatory")
_WfApplePortDdpNoProtocolHandlers_Type = Counter32
_WfApplePortDdpNoProtocolHandlers_Object = MibTableColumn
wfApplePortDdpNoProtocolHandlers = _WfApplePortDdpNoProtocolHandlers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 31),
    _WfApplePortDdpNoProtocolHandlers_Type()
)
wfApplePortDdpNoProtocolHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpNoProtocolHandlers.setStatus("mandatory")
_WfApplePortDdpTooShortErrors_Type = Counter32
_WfApplePortDdpTooShortErrors_Object = MibTableColumn
wfApplePortDdpTooShortErrors = _WfApplePortDdpTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 32),
    _WfApplePortDdpTooShortErrors_Type()
)
wfApplePortDdpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpTooShortErrors.setStatus("mandatory")
_WfApplePortDdpTooLongErrors_Type = Counter32
_WfApplePortDdpTooLongErrors_Object = MibTableColumn
wfApplePortDdpTooLongErrors = _WfApplePortDdpTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 33),
    _WfApplePortDdpTooLongErrors_Type()
)
wfApplePortDdpTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpTooLongErrors.setStatus("mandatory")
_WfApplePortDdpChecksumErrors_Type = Counter32
_WfApplePortDdpChecksumErrors_Object = MibTableColumn
wfApplePortDdpChecksumErrors = _WfApplePortDdpChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 34),
    _WfApplePortDdpChecksumErrors_Type()
)
wfApplePortDdpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpChecksumErrors.setStatus("mandatory")
_WfApplePortDdpForwRequests_Type = Counter32
_WfApplePortDdpForwRequests_Object = MibTableColumn
wfApplePortDdpForwRequests = _WfApplePortDdpForwRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 35),
    _WfApplePortDdpForwRequests_Type()
)
wfApplePortDdpForwRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpForwRequests.setStatus("mandatory")
_WfApplePortDdpOutNoRoutes_Type = Counter32
_WfApplePortDdpOutNoRoutes_Object = MibTableColumn
wfApplePortDdpOutNoRoutes = _WfApplePortDdpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 36),
    _WfApplePortDdpOutNoRoutes_Type()
)
wfApplePortDdpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpOutNoRoutes.setStatus("mandatory")
_WfApplePortDdpBroadcastErrors_Type = Counter32
_WfApplePortDdpBroadcastErrors_Object = MibTableColumn
wfApplePortDdpBroadcastErrors = _WfApplePortDdpBroadcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 37),
    _WfApplePortDdpBroadcastErrors_Type()
)
wfApplePortDdpBroadcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpBroadcastErrors.setStatus("mandatory")
_WfApplePortDdpHopCountErrors_Type = Counter32
_WfApplePortDdpHopCountErrors_Object = MibTableColumn
wfApplePortDdpHopCountErrors = _WfApplePortDdpHopCountErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 38),
    _WfApplePortDdpHopCountErrors_Type()
)
wfApplePortDdpHopCountErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpHopCountErrors.setStatus("mandatory")
_WfApplePortRtmpInDataPkts_Type = Counter32
_WfApplePortRtmpInDataPkts_Object = MibTableColumn
wfApplePortRtmpInDataPkts = _WfApplePortRtmpInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 39),
    _WfApplePortRtmpInDataPkts_Type()
)
wfApplePortRtmpInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpInDataPkts.setStatus("mandatory")
_WfApplePortRtmpOutDataPkts_Type = Counter32
_WfApplePortRtmpOutDataPkts_Object = MibTableColumn
wfApplePortRtmpOutDataPkts = _WfApplePortRtmpOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 40),
    _WfApplePortRtmpOutDataPkts_Type()
)
wfApplePortRtmpOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpOutDataPkts.setStatus("mandatory")
_WfApplePortRtmpInRequestPkts_Type = Counter32
_WfApplePortRtmpInRequestPkts_Object = MibTableColumn
wfApplePortRtmpInRequestPkts = _WfApplePortRtmpInRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 41),
    _WfApplePortRtmpInRequestPkts_Type()
)
wfApplePortRtmpInRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpInRequestPkts.setStatus("mandatory")
_WfApplePortRtmpNextIREqualChanges_Type = Counter32
_WfApplePortRtmpNextIREqualChanges_Object = MibTableColumn
wfApplePortRtmpNextIREqualChanges = _WfApplePortRtmpNextIREqualChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 42),
    _WfApplePortRtmpNextIREqualChanges_Type()
)
wfApplePortRtmpNextIREqualChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpNextIREqualChanges.setStatus("mandatory")
_WfApplePortRtmpNextIRLessChanges_Type = Counter32
_WfApplePortRtmpNextIRLessChanges_Object = MibTableColumn
wfApplePortRtmpNextIRLessChanges = _WfApplePortRtmpNextIRLessChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 43),
    _WfApplePortRtmpNextIRLessChanges_Type()
)
wfApplePortRtmpNextIRLessChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpNextIRLessChanges.setStatus("mandatory")
_WfApplePortRtmpRouteDeletes_Type = Counter32
_WfApplePortRtmpRouteDeletes_Object = MibTableColumn
wfApplePortRtmpRouteDeletes = _WfApplePortRtmpRouteDeletes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 44),
    _WfApplePortRtmpRouteDeletes_Type()
)
wfApplePortRtmpRouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpRouteDeletes.setStatus("mandatory")
_WfApplePortRtmpNetworkMismatchErrors_Type = Counter32
_WfApplePortRtmpNetworkMismatchErrors_Object = MibTableColumn
wfApplePortRtmpNetworkMismatchErrors = _WfApplePortRtmpNetworkMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 45),
    _WfApplePortRtmpNetworkMismatchErrors_Type()
)
wfApplePortRtmpNetworkMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpNetworkMismatchErrors.setStatus("mandatory")
_WfApplePortRtmpRoutingTableOverflows_Type = Counter32
_WfApplePortRtmpRoutingTableOverflows_Object = MibTableColumn
wfApplePortRtmpRoutingTableOverflows = _WfApplePortRtmpRoutingTableOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 46),
    _WfApplePortRtmpRoutingTableOverflows_Type()
)
wfApplePortRtmpRoutingTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpRoutingTableOverflows.setStatus("mandatory")
_WfApplePortZipInZipQueries_Type = Counter32
_WfApplePortZipInZipQueries_Object = MibTableColumn
wfApplePortZipInZipQueries = _WfApplePortZipInZipQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 47),
    _WfApplePortZipInZipQueries_Type()
)
wfApplePortZipInZipQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInZipQueries.setStatus("mandatory")
_WfApplePortZipInZipReplies_Type = Counter32
_WfApplePortZipInZipReplies_Object = MibTableColumn
wfApplePortZipInZipReplies = _WfApplePortZipInZipReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 48),
    _WfApplePortZipInZipReplies_Type()
)
wfApplePortZipInZipReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInZipReplies.setStatus("mandatory")
_WfApplePortZipOutZipReplies_Type = Counter32
_WfApplePortZipOutZipReplies_Object = MibTableColumn
wfApplePortZipOutZipReplies = _WfApplePortZipOutZipReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 49),
    _WfApplePortZipOutZipReplies_Type()
)
wfApplePortZipOutZipReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutZipReplies.setStatus("mandatory")
_WfApplePortZipInZipExtendedReplies_Type = Counter32
_WfApplePortZipInZipExtendedReplies_Object = MibTableColumn
wfApplePortZipInZipExtendedReplies = _WfApplePortZipInZipExtendedReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 50),
    _WfApplePortZipInZipExtendedReplies_Type()
)
wfApplePortZipInZipExtendedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInZipExtendedReplies.setStatus("mandatory")
_WfApplePortZipOutZipExtendedReplies_Type = Counter32
_WfApplePortZipOutZipExtendedReplies_Object = MibTableColumn
wfApplePortZipOutZipExtendedReplies = _WfApplePortZipOutZipExtendedReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 51),
    _WfApplePortZipOutZipExtendedReplies_Type()
)
wfApplePortZipOutZipExtendedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutZipExtendedReplies.setStatus("mandatory")
_WfApplePortZipInGetZoneLists_Type = Counter32
_WfApplePortZipInGetZoneLists_Object = MibTableColumn
wfApplePortZipInGetZoneLists = _WfApplePortZipInGetZoneLists_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 52),
    _WfApplePortZipInGetZoneLists_Type()
)
wfApplePortZipInGetZoneLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetZoneLists.setStatus("mandatory")
_WfApplePortZipOutGetZoneListReplies_Type = Counter32
_WfApplePortZipOutGetZoneListReplies_Object = MibTableColumn
wfApplePortZipOutGetZoneListReplies = _WfApplePortZipOutGetZoneListReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 53),
    _WfApplePortZipOutGetZoneListReplies_Type()
)
wfApplePortZipOutGetZoneListReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetZoneListReplies.setStatus("mandatory")
_WfApplePortZipInGetLocalZones_Type = Counter32
_WfApplePortZipInGetLocalZones_Object = MibTableColumn
wfApplePortZipInGetLocalZones = _WfApplePortZipInGetLocalZones_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 54),
    _WfApplePortZipInGetLocalZones_Type()
)
wfApplePortZipInGetLocalZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetLocalZones.setStatus("mandatory")
_WfApplePortZipOutGetLocalZoneReplies_Type = Counter32
_WfApplePortZipOutGetLocalZoneReplies_Object = MibTableColumn
wfApplePortZipOutGetLocalZoneReplies = _WfApplePortZipOutGetLocalZoneReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 55),
    _WfApplePortZipOutGetLocalZoneReplies_Type()
)
wfApplePortZipOutGetLocalZoneReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetLocalZoneReplies.setStatus("mandatory")
_WfApplePortZipInGetMyZones_Type = Counter32
_WfApplePortZipInGetMyZones_Object = MibTableColumn
wfApplePortZipInGetMyZones = _WfApplePortZipInGetMyZones_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 56),
    _WfApplePortZipInGetMyZones_Type()
)
wfApplePortZipInGetMyZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetMyZones.setStatus("mandatory")
_WfApplePortZipOutGetMyZoneReplies_Type = Counter32
_WfApplePortZipOutGetMyZoneReplies_Object = MibTableColumn
wfApplePortZipOutGetMyZoneReplies = _WfApplePortZipOutGetMyZoneReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 57),
    _WfApplePortZipOutGetMyZoneReplies_Type()
)
wfApplePortZipOutGetMyZoneReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetMyZoneReplies.setStatus("mandatory")
_WfApplePortZipZoneConflictErrors_Type = Counter32
_WfApplePortZipZoneConflictErrors_Object = MibTableColumn
wfApplePortZipZoneConflictErrors = _WfApplePortZipZoneConflictErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 58),
    _WfApplePortZipZoneConflictErrors_Type()
)
wfApplePortZipZoneConflictErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipZoneConflictErrors.setStatus("mandatory")
_WfApplePortZipInGetNetInfos_Type = Counter32
_WfApplePortZipInGetNetInfos_Object = MibTableColumn
wfApplePortZipInGetNetInfos = _WfApplePortZipInGetNetInfos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 59),
    _WfApplePortZipInGetNetInfos_Type()
)
wfApplePortZipInGetNetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetNetInfos.setStatus("mandatory")
_WfApplePortZipOutGetNetInfoReplies_Type = Counter32
_WfApplePortZipOutGetNetInfoReplies_Object = MibTableColumn
wfApplePortZipOutGetNetInfoReplies = _WfApplePortZipOutGetNetInfoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 60),
    _WfApplePortZipOutGetNetInfoReplies_Type()
)
wfApplePortZipOutGetNetInfoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetNetInfoReplies.setStatus("mandatory")
_WfApplePortZipZoneOutInvalids_Type = Counter32
_WfApplePortZipZoneOutInvalids_Object = MibTableColumn
wfApplePortZipZoneOutInvalids = _WfApplePortZipZoneOutInvalids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 61),
    _WfApplePortZipZoneOutInvalids_Type()
)
wfApplePortZipZoneOutInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipZoneOutInvalids.setStatus("mandatory")
_WfApplePortZipAddressInvalids_Type = Counter32
_WfApplePortZipAddressInvalids_Object = MibTableColumn
wfApplePortZipAddressInvalids = _WfApplePortZipAddressInvalids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 62),
    _WfApplePortZipAddressInvalids_Type()
)
wfApplePortZipAddressInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipAddressInvalids.setStatus("mandatory")
_WfApplePortZipOutGetNetInfos_Type = Counter32
_WfApplePortZipOutGetNetInfos_Object = MibTableColumn
wfApplePortZipOutGetNetInfos = _WfApplePortZipOutGetNetInfos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 63),
    _WfApplePortZipOutGetNetInfos_Type()
)
wfApplePortZipOutGetNetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetNetInfos.setStatus("mandatory")
_WfApplePortZipInGetNetInfoReplies_Type = Counter32
_WfApplePortZipInGetNetInfoReplies_Object = MibTableColumn
wfApplePortZipInGetNetInfoReplies = _WfApplePortZipInGetNetInfoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 64),
    _WfApplePortZipInGetNetInfoReplies_Type()
)
wfApplePortZipInGetNetInfoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetNetInfoReplies.setStatus("mandatory")
_WfApplePortZipOutZipQueries_Type = Counter32
_WfApplePortZipOutZipQueries_Object = MibTableColumn
wfApplePortZipOutZipQueries = _WfApplePortZipOutZipQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 65),
    _WfApplePortZipOutZipQueries_Type()
)
wfApplePortZipOutZipQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutZipQueries.setStatus("mandatory")
_WfApplePortZipInErrors_Type = Counter32
_WfApplePortZipInErrors_Object = MibTableColumn
wfApplePortZipInErrors = _WfApplePortZipInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 66),
    _WfApplePortZipInErrors_Type()
)
wfApplePortZipInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInErrors.setStatus("mandatory")
_WfApplePortNbpInLookUpRequests_Type = Counter32
_WfApplePortNbpInLookUpRequests_Object = MibTableColumn
wfApplePortNbpInLookUpRequests = _WfApplePortNbpInLookUpRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 67),
    _WfApplePortNbpInLookUpRequests_Type()
)
wfApplePortNbpInLookUpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInLookUpRequests.setStatus("mandatory")
_WfApplePortNbpInLookUpReplies_Type = Counter32
_WfApplePortNbpInLookUpReplies_Object = MibTableColumn
wfApplePortNbpInLookUpReplies = _WfApplePortNbpInLookUpReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 68),
    _WfApplePortNbpInLookUpReplies_Type()
)
wfApplePortNbpInLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInLookUpReplies.setStatus("mandatory")
_WfApplePortNbpInBroadcastRequests_Type = Counter32
_WfApplePortNbpInBroadcastRequests_Object = MibTableColumn
wfApplePortNbpInBroadcastRequests = _WfApplePortNbpInBroadcastRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 69),
    _WfApplePortNbpInBroadcastRequests_Type()
)
wfApplePortNbpInBroadcastRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInBroadcastRequests.setStatus("mandatory")
_WfApplePortNbpInForwardRequests_Type = Counter32
_WfApplePortNbpInForwardRequests_Object = MibTableColumn
wfApplePortNbpInForwardRequests = _WfApplePortNbpInForwardRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 70),
    _WfApplePortNbpInForwardRequests_Type()
)
wfApplePortNbpInForwardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInForwardRequests.setStatus("mandatory")
_WfApplePortNbpOutLookUpRequests_Type = Counter32
_WfApplePortNbpOutLookUpRequests_Object = MibTableColumn
wfApplePortNbpOutLookUpRequests = _WfApplePortNbpOutLookUpRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 71),
    _WfApplePortNbpOutLookUpRequests_Type()
)
wfApplePortNbpOutLookUpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutLookUpRequests.setStatus("mandatory")
_WfApplePortNbpOutLookUpReplies_Type = Counter32
_WfApplePortNbpOutLookUpReplies_Object = MibTableColumn
wfApplePortNbpOutLookUpReplies = _WfApplePortNbpOutLookUpReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 72),
    _WfApplePortNbpOutLookUpReplies_Type()
)
wfApplePortNbpOutLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutLookUpReplies.setStatus("mandatory")
_WfApplePortNbpOutBroadcastRequests_Type = Counter32
_WfApplePortNbpOutBroadcastRequests_Object = MibTableColumn
wfApplePortNbpOutBroadcastRequests = _WfApplePortNbpOutBroadcastRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 73),
    _WfApplePortNbpOutBroadcastRequests_Type()
)
wfApplePortNbpOutBroadcastRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutBroadcastRequests.setStatus("mandatory")
_WfApplePortNbpOutForwardRequests_Type = Counter32
_WfApplePortNbpOutForwardRequests_Object = MibTableColumn
wfApplePortNbpOutForwardRequests = _WfApplePortNbpOutForwardRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 74),
    _WfApplePortNbpOutForwardRequests_Type()
)
wfApplePortNbpOutForwardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutForwardRequests.setStatus("mandatory")
_WfApplePortNbpRegistrationFailures_Type = Counter32
_WfApplePortNbpRegistrationFailures_Object = MibTableColumn
wfApplePortNbpRegistrationFailures = _WfApplePortNbpRegistrationFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 75),
    _WfApplePortNbpRegistrationFailures_Type()
)
wfApplePortNbpRegistrationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpRegistrationFailures.setStatus("mandatory")
_WfApplePortNbpInErrors_Type = Counter32
_WfApplePortNbpInErrors_Object = MibTableColumn
wfApplePortNbpInErrors = _WfApplePortNbpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 76),
    _WfApplePortNbpInErrors_Type()
)
wfApplePortNbpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInErrors.setStatus("mandatory")
_WfApplePortEchoRequests_Type = Counter32
_WfApplePortEchoRequests_Object = MibTableColumn
wfApplePortEchoRequests = _WfApplePortEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 77),
    _WfApplePortEchoRequests_Type()
)
wfApplePortEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortEchoRequests.setStatus("mandatory")
_WfApplePortEchoReplies_Type = Counter32
_WfApplePortEchoReplies_Object = MibTableColumn
wfApplePortEchoReplies = _WfApplePortEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 78),
    _WfApplePortEchoReplies_Type()
)
wfApplePortEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortEchoReplies.setStatus("mandatory")
_WfAppleLclZoneTable_Object = MibTable
wfAppleLclZoneTable = _WfAppleLclZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    wfAppleLclZoneTable.setStatus("mandatory")
_WfAppleLclZoneEntry_Object = MibTableRow
wfAppleLclZoneEntry = _WfAppleLclZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1)
)
wfAppleLclZoneEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfAppleLclZonePortCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfAppleLclZoneIndex"),
)
if mibBuilder.loadTexts:
    wfAppleLclZoneEntry.setStatus("mandatory")


class _WfAppleLclZoneDelete_Type(Integer32):
    """Custom type wfAppleLclZoneDelete based on Integer32"""
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


_WfAppleLclZoneDelete_Type.__name__ = "Integer32"
_WfAppleLclZoneDelete_Object = MibTableColumn
wfAppleLclZoneDelete = _WfAppleLclZoneDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 1),
    _WfAppleLclZoneDelete_Type()
)
wfAppleLclZoneDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleLclZoneDelete.setStatus("mandatory")
_WfAppleLclZonePortCircuit_Type = Integer32
_WfAppleLclZonePortCircuit_Object = MibTableColumn
wfAppleLclZonePortCircuit = _WfAppleLclZonePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 2),
    _WfAppleLclZonePortCircuit_Type()
)
wfAppleLclZonePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleLclZonePortCircuit.setStatus("mandatory")
_WfAppleLclZoneIndex_Type = Integer32
_WfAppleLclZoneIndex_Object = MibTableColumn
wfAppleLclZoneIndex = _WfAppleLclZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 3),
    _WfAppleLclZoneIndex_Type()
)
wfAppleLclZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleLclZoneIndex.setStatus("mandatory")
_WfAppleLclZoneName_Type = DisplayString
_WfAppleLclZoneName_Object = MibTableColumn
wfAppleLclZoneName = _WfAppleLclZoneName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 4),
    _WfAppleLclZoneName_Type()
)
wfAppleLclZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleLclZoneName.setStatus("mandatory")
_WfAppleAarpTable_Object = MibTable
wfAppleAarpTable = _WfAppleAarpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5)
)
if mibBuilder.loadTexts:
    wfAppleAarpTable.setStatus("mandatory")
_WfAppleAarpEntry_Object = MibTableRow
wfAppleAarpEntry = _WfAppleAarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1)
)
wfAppleAarpEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfAppleAarpNet"),
    (0, "Wellfleet-Series7-MIB", "wfAppleAarpNode"),
    (0, "Wellfleet-Series7-MIB", "wfAppleAarpIfIndex"),
)
if mibBuilder.loadTexts:
    wfAppleAarpEntry.setStatus("mandatory")
_WfAppleAarpIfIndex_Type = Integer32
_WfAppleAarpIfIndex_Object = MibTableColumn
wfAppleAarpIfIndex = _WfAppleAarpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 1),
    _WfAppleAarpIfIndex_Type()
)
wfAppleAarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpIfIndex.setStatus("mandatory")
_WfAppleAarpNet_Type = Integer32
_WfAppleAarpNet_Object = MibTableColumn
wfAppleAarpNet = _WfAppleAarpNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 2),
    _WfAppleAarpNet_Type()
)
wfAppleAarpNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpNet.setStatus("mandatory")
_WfAppleAarpNode_Type = Integer32
_WfAppleAarpNode_Object = MibTableColumn
wfAppleAarpNode = _WfAppleAarpNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 3),
    _WfAppleAarpNode_Type()
)
wfAppleAarpNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpNode.setStatus("mandatory")
_WfAppleAarpPhysAddress_Type = OctetString
_WfAppleAarpPhysAddress_Object = MibTableColumn
wfAppleAarpPhysAddress = _WfAppleAarpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 4),
    _WfAppleAarpPhysAddress_Type()
)
wfAppleAarpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpPhysAddress.setStatus("mandatory")
_WfAppleZipTable_Object = MibTable
wfAppleZipTable = _WfAppleZipTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6)
)
if mibBuilder.loadTexts:
    wfAppleZipTable.setStatus("mandatory")
_WfAppleZipEntry_Object = MibTableRow
wfAppleZipEntry = _WfAppleZipEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1)
)
wfAppleZipEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfAppleZipZoneNetStart"),
    (0, "Wellfleet-Series7-MIB", "wfAppleZipIndex"),
)
if mibBuilder.loadTexts:
    wfAppleZipEntry.setStatus("mandatory")
_WfAppleZipZoneNetStart_Type = Integer32
_WfAppleZipZoneNetStart_Object = MibTableColumn
wfAppleZipZoneNetStart = _WfAppleZipZoneNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 1),
    _WfAppleZipZoneNetStart_Type()
)
wfAppleZipZoneNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneNetStart.setStatus("mandatory")
_WfAppleZipZoneNetEnd_Type = Integer32
_WfAppleZipZoneNetEnd_Object = MibTableColumn
wfAppleZipZoneNetEnd = _WfAppleZipZoneNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 2),
    _WfAppleZipZoneNetEnd_Type()
)
wfAppleZipZoneNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneNetEnd.setStatus("mandatory")
_WfAppleZipIndex_Type = Integer32
_WfAppleZipIndex_Object = MibTableColumn
wfAppleZipIndex = _WfAppleZipIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 3),
    _WfAppleZipIndex_Type()
)
wfAppleZipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipIndex.setStatus("mandatory")
_WfAppleZipZoneName_Type = DisplayString
_WfAppleZipZoneName_Object = MibTableColumn
wfAppleZipZoneName = _WfAppleZipZoneName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 4),
    _WfAppleZipZoneName_Type()
)
wfAppleZipZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneName.setStatus("mandatory")


class _WfAppleZipZoneState_Type(Integer32):
    """Custom type wfAppleZipZoneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfAppleZipZoneState_Type.__name__ = "Integer32"
_WfAppleZipZoneState_Object = MibTableColumn
wfAppleZipZoneState = _WfAppleZipZoneState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 5),
    _WfAppleZipZoneState_Type()
)
wfAppleZipZoneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneState.setStatus("mandatory")
_WfIpxGroup_ObjectIdentity = ObjectIdentity
wfIpxGroup = _WfIpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5)
)
_WfIpxBase_ObjectIdentity = ObjectIdentity
wfIpxBase = _WfIpxBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1)
)


class _WfIpxBaseDelete_Type(Integer32):
    """Custom type wfIpxBaseDelete based on Integer32"""
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


_WfIpxBaseDelete_Type.__name__ = "Integer32"
_WfIpxBaseDelete_Object = MibScalar
wfIpxBaseDelete = _WfIpxBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 1),
    _WfIpxBaseDelete_Type()
)
wfIpxBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseDelete.setStatus("mandatory")


class _WfIpxBaseDisable_Type(Integer32):
    """Custom type wfIpxBaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxBaseDisable_Type.__name__ = "Integer32"
_WfIpxBaseDisable_Object = MibScalar
wfIpxBaseDisable = _WfIpxBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 2),
    _WfIpxBaseDisable_Type()
)
wfIpxBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseDisable.setStatus("mandatory")


class _WfIpxBaseState_Type(Integer32):
    """Custom type wfIpxBaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("in", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxBaseState_Type.__name__ = "Integer32"
_WfIpxBaseState_Object = MibScalar
wfIpxBaseState = _WfIpxBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 3),
    _WfIpxBaseState_Type()
)
wfIpxBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseState.setStatus("mandatory")
_WfIpxBaseCfgHostNumber_Type = OctetString
_WfIpxBaseCfgHostNumber_Object = MibScalar
wfIpxBaseCfgHostNumber = _WfIpxBaseCfgHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 4),
    _WfIpxBaseCfgHostNumber_Type()
)
wfIpxBaseCfgHostNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseCfgHostNumber.setStatus("mandatory")
_WfIpxBaseActiveHostNumber_Type = OctetString
_WfIpxBaseActiveHostNumber_Object = MibScalar
wfIpxBaseActiveHostNumber = _WfIpxBaseActiveHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 5),
    _WfIpxBaseActiveHostNumber_Type()
)
wfIpxBaseActiveHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseActiveHostNumber.setStatus("mandatory")
_WfIpxBaseNetCount_Type = Counter32
_WfIpxBaseNetCount_Object = MibScalar
wfIpxBaseNetCount = _WfIpxBaseNetCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 6),
    _WfIpxBaseNetCount_Type()
)
wfIpxBaseNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseNetCount.setStatus("mandatory")
_WfIpxBaseServiceCount_Type = Counter32
_WfIpxBaseServiceCount_Object = MibScalar
wfIpxBaseServiceCount = _WfIpxBaseServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 7),
    _WfIpxBaseServiceCount_Type()
)
wfIpxBaseServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseServiceCount.setStatus("mandatory")


class _WfIpxBaseLogFilter_Type(Integer32):
    """Custom type wfIpxBaseLogFilter based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("debug", 1),
          ("debuginfo", 3),
          ("debuginfotrace", 19),
          ("debugtrace", 17),
          ("info", 2),
          ("infotrace", 18),
          ("trace", 16))
    )


_WfIpxBaseLogFilter_Type.__name__ = "Integer32"
_WfIpxBaseLogFilter_Object = MibScalar
wfIpxBaseLogFilter = _WfIpxBaseLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 8),
    _WfIpxBaseLogFilter_Type()
)
wfIpxBaseLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseLogFilter.setStatus("mandatory")


class _WfIpxBaseNetTblSize_Type(Integer32):
    """Custom type wfIpxBaseNetTblSize based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            250
        )
    )
    namedValues = NamedValues(
        ("size", 250)
    )


_WfIpxBaseNetTblSize_Type.__name__ = "Integer32"
_WfIpxBaseNetTblSize_Object = MibScalar
wfIpxBaseNetTblSize = _WfIpxBaseNetTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 1, 9),
    _WfIpxBaseNetTblSize_Type()
)
wfIpxBaseNetTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxBaseNetTblSize.setStatus("mandatory")
_WfIpxBaseRtEntryTable_Object = MibTable
wfIpxBaseRtEntryTable = _WfIpxBaseRtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2)
)
if mibBuilder.loadTexts:
    wfIpxBaseRtEntryTable.setStatus("mandatory")
_WfIpxBaseRtEntry_Object = MibTableRow
wfIpxBaseRtEntry = _WfIpxBaseRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1)
)
wfIpxBaseRtEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxBaseRouteDest"),
)
if mibBuilder.loadTexts:
    wfIpxBaseRtEntry.setStatus("mandatory")
_WfIpxBaseRouteDest_Type = OctetString
_WfIpxBaseRouteDest_Object = MibTableColumn
wfIpxBaseRouteDest = _WfIpxBaseRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 1),
    _WfIpxBaseRouteDest_Type()
)
wfIpxBaseRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteDest.setStatus("mandatory")
_WfIpxBaseRouteIfIndex_Type = Integer32
_WfIpxBaseRouteIfIndex_Object = MibTableColumn
wfIpxBaseRouteIfIndex = _WfIpxBaseRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 2),
    _WfIpxBaseRouteIfIndex_Type()
)
wfIpxBaseRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteIfIndex.setStatus("mandatory")
_WfIpxBaseRouteMetric_Type = Integer32
_WfIpxBaseRouteMetric_Object = MibTableColumn
wfIpxBaseRouteMetric = _WfIpxBaseRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 3),
    _WfIpxBaseRouteMetric_Type()
)
wfIpxBaseRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteMetric.setStatus("mandatory")
_WfIpxBaseRouteNextHopNetwork_Type = OctetString
_WfIpxBaseRouteNextHopNetwork_Object = MibTableColumn
wfIpxBaseRouteNextHopNetwork = _WfIpxBaseRouteNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 4),
    _WfIpxBaseRouteNextHopNetwork_Type()
)
wfIpxBaseRouteNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteNextHopNetwork.setStatus("mandatory")
_WfIpxBaseRouteNextHopHost_Type = OctetString
_WfIpxBaseRouteNextHopHost_Object = MibTableColumn
wfIpxBaseRouteNextHopHost = _WfIpxBaseRouteNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 5),
    _WfIpxBaseRouteNextHopHost_Type()
)
wfIpxBaseRouteNextHopHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteNextHopHost.setStatus("mandatory")


class _WfIpxBaseRouteType_Type(Integer32):
    """Custom type wfIpxBaseRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1),
          ("static", 5))
    )


_WfIpxBaseRouteType_Type.__name__ = "Integer32"
_WfIpxBaseRouteType_Object = MibTableColumn
wfIpxBaseRouteType = _WfIpxBaseRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 6),
    _WfIpxBaseRouteType_Type()
)
wfIpxBaseRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteType.setStatus("mandatory")


class _WfIpxBaseRouteProto_Type(Integer32):
    """Custom type wfIpxBaseRouteProto based on Integer32"""
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
        *(("local", 2),
          ("netmgmt", 3),
          ("other", 1),
          ("rip", 4))
    )


_WfIpxBaseRouteProto_Type.__name__ = "Integer32"
_WfIpxBaseRouteProto_Object = MibTableColumn
wfIpxBaseRouteProto = _WfIpxBaseRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 7),
    _WfIpxBaseRouteProto_Type()
)
wfIpxBaseRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteProto.setStatus("mandatory")
_WfIpxBaseRouteAge_Type = Integer32
_WfIpxBaseRouteAge_Object = MibTableColumn
wfIpxBaseRouteAge = _WfIpxBaseRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 8),
    _WfIpxBaseRouteAge_Type()
)
wfIpxBaseRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteAge.setStatus("mandatory")
_WfIpxBaseRouteInfo_Type = OctetString
_WfIpxBaseRouteInfo_Object = MibTableColumn
wfIpxBaseRouteInfo = _WfIpxBaseRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 2, 1, 9),
    _WfIpxBaseRouteInfo_Type()
)
wfIpxBaseRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseRouteInfo.setStatus("mandatory")
_WfIpxBaseSapEntryTable_Object = MibTable
wfIpxBaseSapEntryTable = _WfIpxBaseSapEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3)
)
if mibBuilder.loadTexts:
    wfIpxBaseSapEntryTable.setStatus("mandatory")
_WfIpxBaseSapEntry_Object = MibTableRow
wfIpxBaseSapEntry = _WfIpxBaseSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1)
)
wfIpxBaseSapEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxBaseSapIndex"),
)
if mibBuilder.loadTexts:
    wfIpxBaseSapEntry.setStatus("mandatory")
_WfIpxBaseSapType_Type = OctetString
_WfIpxBaseSapType_Object = MibTableColumn
wfIpxBaseSapType = _WfIpxBaseSapType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 1),
    _WfIpxBaseSapType_Type()
)
wfIpxBaseSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapType.setStatus("mandatory")
_WfIpxBaseSapNetwork_Type = OctetString
_WfIpxBaseSapNetwork_Object = MibTableColumn
wfIpxBaseSapNetwork = _WfIpxBaseSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 2),
    _WfIpxBaseSapNetwork_Type()
)
wfIpxBaseSapNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapNetwork.setStatus("mandatory")
_WfIpxBaseSapHost_Type = OctetString
_WfIpxBaseSapHost_Object = MibTableColumn
wfIpxBaseSapHost = _WfIpxBaseSapHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 3),
    _WfIpxBaseSapHost_Type()
)
wfIpxBaseSapHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapHost.setStatus("mandatory")
_WfIpxBaseSapSocket_Type = OctetString
_WfIpxBaseSapSocket_Object = MibTableColumn
wfIpxBaseSapSocket = _WfIpxBaseSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 4),
    _WfIpxBaseSapSocket_Type()
)
wfIpxBaseSapSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapSocket.setStatus("mandatory")
_WfIpxBaseSapName_Type = DisplayString
_WfIpxBaseSapName_Object = MibTableColumn
wfIpxBaseSapName = _WfIpxBaseSapName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 5),
    _WfIpxBaseSapName_Type()
)
wfIpxBaseSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapName.setStatus("mandatory")
_WfIpxBaseSapAge_Type = Integer32
_WfIpxBaseSapAge_Object = MibTableColumn
wfIpxBaseSapAge = _WfIpxBaseSapAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 6),
    _WfIpxBaseSapAge_Type()
)
wfIpxBaseSapAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapAge.setStatus("mandatory")
_WfIpxBaseSapHops_Type = Integer32
_WfIpxBaseSapHops_Object = MibTableColumn
wfIpxBaseSapHops = _WfIpxBaseSapHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 7),
    _WfIpxBaseSapHops_Type()
)
wfIpxBaseSapHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapHops.setStatus("mandatory")
_WfIpxBaseSapIndex_Type = OctetString
_WfIpxBaseSapIndex_Object = MibTableColumn
wfIpxBaseSapIndex = _WfIpxBaseSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 8),
    _WfIpxBaseSapIndex_Type()
)
wfIpxBaseSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapIndex.setStatus("mandatory")
_WfIpxBaseSapIntf_Type = OctetString
_WfIpxBaseSapIntf_Object = MibTableColumn
wfIpxBaseSapIntf = _WfIpxBaseSapIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 3, 1, 9),
    _WfIpxBaseSapIntf_Type()
)
wfIpxBaseSapIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxBaseSapIntf.setStatus("mandatory")
_WfIpxInterfaceTable_Object = MibTable
wfIpxInterfaceTable = _WfIpxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4)
)
if mibBuilder.loadTexts:
    wfIpxInterfaceTable.setStatus("mandatory")
_WfIpxInterfaceEntry_Object = MibTableRow
wfIpxInterfaceEntry = _WfIpxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1)
)
wfIpxInterfaceEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxInterfaceNetworkNumber"),
    (0, "Wellfleet-Series7-MIB", "wfIpxInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfIpxInterfaceEntry.setStatus("mandatory")
_WfIpxInterfaceIndex_Type = Integer32
_WfIpxInterfaceIndex_Object = MibTableColumn
wfIpxInterfaceIndex = _WfIpxInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 1),
    _WfIpxInterfaceIndex_Type()
)
wfIpxInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceIndex.setStatus("mandatory")


class _WfIpxInterfaceDelete_Type(Integer32):
    """Custom type wfIpxInterfaceDelete based on Integer32"""
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


_WfIpxInterfaceDelete_Type.__name__ = "Integer32"
_WfIpxInterfaceDelete_Object = MibTableColumn
wfIpxInterfaceDelete = _WfIpxInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 2),
    _WfIpxInterfaceDelete_Type()
)
wfIpxInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceDelete.setStatus("mandatory")


class _WfIpxInterfaceDisable_Type(Integer32):
    """Custom type wfIpxInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceDisable_Type.__name__ = "Integer32"
_WfIpxInterfaceDisable_Object = MibTableColumn
wfIpxInterfaceDisable = _WfIpxInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 3),
    _WfIpxInterfaceDisable_Type()
)
wfIpxInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceDisable.setStatus("mandatory")


class _WfIpxInterfaceState_Type(Integer32):
    """Custom type wfIpxInterfaceState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxInterfaceState_Type.__name__ = "Integer32"
_WfIpxInterfaceState_Object = MibTableColumn
wfIpxInterfaceState = _WfIpxInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 4),
    _WfIpxInterfaceState_Type()
)
wfIpxInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceState.setStatus("mandatory")
_WfIpxInterfaceCircuit_Type = Integer32
_WfIpxInterfaceCircuit_Object = MibTableColumn
wfIpxInterfaceCircuit = _WfIpxInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 5),
    _WfIpxInterfaceCircuit_Type()
)
wfIpxInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceCircuit.setStatus("mandatory")
_WfIpxInterfaceNetworkNumber_Type = OctetString
_WfIpxInterfaceNetworkNumber_Object = MibTableColumn
wfIpxInterfaceNetworkNumber = _WfIpxInterfaceNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 6),
    _WfIpxInterfaceNetworkNumber_Type()
)
wfIpxInterfaceNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceNetworkNumber.setStatus("mandatory")


class _WfIpxInterfaceCost_Type(Integer32):
    """Custom type wfIpxInterfaceCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cost", 1)
    )


_WfIpxInterfaceCost_Type.__name__ = "Integer32"
_WfIpxInterfaceCost_Object = MibTableColumn
wfIpxInterfaceCost = _WfIpxInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 7),
    _WfIpxInterfaceCost_Type()
)
wfIpxInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceCost.setStatus("mandatory")


class _WfIpxInterfaceXsumOn_Type(Integer32):
    """Custom type wfIpxInterfaceXsumOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceXsumOn_Type.__name__ = "Integer32"
_WfIpxInterfaceXsumOn_Object = MibTableColumn
wfIpxInterfaceXsumOn = _WfIpxInterfaceXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 8),
    _WfIpxInterfaceXsumOn_Type()
)
wfIpxInterfaceXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceXsumOn.setStatus("mandatory")


class _WfIpxInterfaceCfgEncaps_Type(Integer32):
    """Custom type wfIpxInterfaceCfgEncaps based on Integer32"""
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
        *(("ethernet", 1),
          ("lsap", 2),
          ("novell", 3),
          ("snap", 4))
    )


_WfIpxInterfaceCfgEncaps_Type.__name__ = "Integer32"
_WfIpxInterfaceCfgEncaps_Object = MibTableColumn
wfIpxInterfaceCfgEncaps = _WfIpxInterfaceCfgEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 9),
    _WfIpxInterfaceCfgEncaps_Type()
)
wfIpxInterfaceCfgEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceCfgEncaps.setStatus("mandatory")
_WfIpxInterfaceMacAddress_Type = OctetString
_WfIpxInterfaceMacAddress_Object = MibTableColumn
wfIpxInterfaceMacAddress = _WfIpxInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 10),
    _WfIpxInterfaceMacAddress_Type()
)
wfIpxInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceMacAddress.setStatus("mandatory")
_WfIpxInterfaceSMDSGroupAddress_Type = OctetString
_WfIpxInterfaceSMDSGroupAddress_Object = MibTableColumn
wfIpxInterfaceSMDSGroupAddress = _WfIpxInterfaceSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 11),
    _WfIpxInterfaceSMDSGroupAddress_Type()
)
wfIpxInterfaceSMDSGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceSMDSGroupAddress.setStatus("mandatory")
_WfIpxInterfaceMaxInfo_Type = Integer32
_WfIpxInterfaceMaxInfo_Object = MibTableColumn
wfIpxInterfaceMaxInfo = _WfIpxInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 12),
    _WfIpxInterfaceMaxInfo_Type()
)
wfIpxInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceMaxInfo.setStatus("mandatory")
_WfIpxInterfaceInReceives_Type = Counter32
_WfIpxInterfaceInReceives_Object = MibTableColumn
wfIpxInterfaceInReceives = _WfIpxInterfaceInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 13),
    _WfIpxInterfaceInReceives_Type()
)
wfIpxInterfaceInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInReceives.setStatus("mandatory")
_WfIpxInterfaceInHdrErrors_Type = Counter32
_WfIpxInterfaceInHdrErrors_Object = MibTableColumn
wfIpxInterfaceInHdrErrors = _WfIpxInterfaceInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 14),
    _WfIpxInterfaceInHdrErrors_Type()
)
wfIpxInterfaceInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInHdrErrors.setStatus("mandatory")
_WfIpxInterfaceInAddrErrors_Type = Counter32
_WfIpxInterfaceInAddrErrors_Object = MibTableColumn
wfIpxInterfaceInAddrErrors = _WfIpxInterfaceInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 15),
    _WfIpxInterfaceInAddrErrors_Type()
)
wfIpxInterfaceInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInAddrErrors.setStatus("mandatory")
_WfIpxInterfaceForwDatagrams_Type = Counter32
_WfIpxInterfaceForwDatagrams_Object = MibTableColumn
wfIpxInterfaceForwDatagrams = _WfIpxInterfaceForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 16),
    _WfIpxInterfaceForwDatagrams_Type()
)
wfIpxInterfaceForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceForwDatagrams.setStatus("mandatory")
_WfIpxInterfaceInUnknownProtos_Type = Counter32
_WfIpxInterfaceInUnknownProtos_Object = MibTableColumn
wfIpxInterfaceInUnknownProtos = _WfIpxInterfaceInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 17),
    _WfIpxInterfaceInUnknownProtos_Type()
)
wfIpxInterfaceInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInUnknownProtos.setStatus("mandatory")
_WfIpxInterfaceInDiscards_Type = Counter32
_WfIpxInterfaceInDiscards_Object = MibTableColumn
wfIpxInterfaceInDiscards = _WfIpxInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 18),
    _WfIpxInterfaceInDiscards_Type()
)
wfIpxInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInDiscards.setStatus("mandatory")
_WfIpxInterfaceInDelivers_Type = Counter32
_WfIpxInterfaceInDelivers_Object = MibTableColumn
wfIpxInterfaceInDelivers = _WfIpxInterfaceInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 19),
    _WfIpxInterfaceInDelivers_Type()
)
wfIpxInterfaceInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceInDelivers.setStatus("mandatory")
_WfIpxInterfaceOutRequests_Type = Counter32
_WfIpxInterfaceOutRequests_Object = MibTableColumn
wfIpxInterfaceOutRequests = _WfIpxInterfaceOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 20),
    _WfIpxInterfaceOutRequests_Type()
)
wfIpxInterfaceOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceOutRequests.setStatus("mandatory")
_WfIpxInterfaceOutDiscards_Type = Counter32
_WfIpxInterfaceOutDiscards_Object = MibTableColumn
wfIpxInterfaceOutDiscards = _WfIpxInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 21),
    _WfIpxInterfaceOutDiscards_Type()
)
wfIpxInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceOutDiscards.setStatus("mandatory")
_WfIpxInterfaceOutNoRoutes_Type = Counter32
_WfIpxInterfaceOutNoRoutes_Object = MibTableColumn
wfIpxInterfaceOutNoRoutes = _WfIpxInterfaceOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 22),
    _WfIpxInterfaceOutNoRoutes_Type()
)
wfIpxInterfaceOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceOutNoRoutes.setStatus("mandatory")


class _WfIpxInterfaceTrEndStation_Type(Integer32):
    """Custom type wfIpxInterfaceTrEndStation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceTrEndStation_Type.__name__ = "Integer32"
_WfIpxInterfaceTrEndStation_Object = MibTableColumn
wfIpxInterfaceTrEndStation = _WfIpxInterfaceTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 23),
    _WfIpxInterfaceTrEndStation_Type()
)
wfIpxInterfaceTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceTrEndStation.setStatus("mandatory")


class _WfIpxInterfaceNetbiosAccept_Type(Integer32):
    """Custom type wfIpxInterfaceNetbiosAccept based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceNetbiosAccept_Type.__name__ = "Integer32"
_WfIpxInterfaceNetbiosAccept_Object = MibTableColumn
wfIpxInterfaceNetbiosAccept = _WfIpxInterfaceNetbiosAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 24),
    _WfIpxInterfaceNetbiosAccept_Type()
)
wfIpxInterfaceNetbiosAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceNetbiosAccept.setStatus("mandatory")


class _WfIpxInterfaceNetbiosDeliver_Type(Integer32):
    """Custom type wfIpxInterfaceNetbiosDeliver based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceNetbiosDeliver_Type.__name__ = "Integer32"
_WfIpxInterfaceNetbiosDeliver_Object = MibTableColumn
wfIpxInterfaceNetbiosDeliver = _WfIpxInterfaceNetbiosDeliver_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 25),
    _WfIpxInterfaceNetbiosDeliver_Type()
)
wfIpxInterfaceNetbiosDeliver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceNetbiosDeliver.setStatus("mandatory")


class _WfIpxInterfaceWanSapPeriod_Type(Integer32):
    """Custom type wfIpxInterfaceWanSapPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("default", 1)
    )


_WfIpxInterfaceWanSapPeriod_Type.__name__ = "Integer32"
_WfIpxInterfaceWanSapPeriod_Object = MibTableColumn
wfIpxInterfaceWanSapPeriod = _WfIpxInterfaceWanSapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 26),
    _WfIpxInterfaceWanSapPeriod_Type()
)
wfIpxInterfaceWanSapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceWanSapPeriod.setStatus("mandatory")
_WfIpxInterfaceFRBcast_Type = OctetString
_WfIpxInterfaceFRBcast_Object = MibTableColumn
wfIpxInterfaceFRBcast = _WfIpxInterfaceFRBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 27),
    _WfIpxInterfaceFRBcast_Type()
)
wfIpxInterfaceFRBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceFRBcast.setStatus("mandatory")
_WfIpxInterfaceFRMcast_Type = OctetString
_WfIpxInterfaceFRMcast_Object = MibTableColumn
wfIpxInterfaceFRMcast = _WfIpxInterfaceFRMcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 28),
    _WfIpxInterfaceFRMcast_Type()
)
wfIpxInterfaceFRMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceFRMcast.setStatus("mandatory")


class _WfIpxInterfaceEncaps_Type(Integer32):
    """Custom type wfIpxInterfaceEncaps based on Integer32"""
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
        *(("ethernet", 1),
          ("lsap", 2),
          ("novell", 3),
          ("snap", 4))
    )


_WfIpxInterfaceEncaps_Type.__name__ = "Integer32"
_WfIpxInterfaceEncaps_Object = MibTableColumn
wfIpxInterfaceEncaps = _WfIpxInterfaceEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 29),
    _WfIpxInterfaceEncaps_Type()
)
wfIpxInterfaceEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceEncaps.setStatus("mandatory")


class _WfIpxInterfaceSplit_Type(Integer32):
    """Custom type wfIpxInterfaceSplit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxInterfaceSplit_Type.__name__ = "Integer32"
_WfIpxInterfaceSplit_Object = MibTableColumn
wfIpxInterfaceSplit = _WfIpxInterfaceSplit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 30),
    _WfIpxInterfaceSplit_Type()
)
wfIpxInterfaceSplit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxInterfaceSplit.setStatus("mandatory")
_WfIpxInterfaceCacheHit_Type = Counter32
_WfIpxInterfaceCacheHit_Object = MibTableColumn
wfIpxInterfaceCacheHit = _WfIpxInterfaceCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 4, 1, 31),
    _WfIpxInterfaceCacheHit_Type()
)
wfIpxInterfaceCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxInterfaceCacheHit.setStatus("mandatory")
_WfIpxRipIntfTable_Object = MibTable
wfIpxRipIntfTable = _WfIpxRipIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5)
)
if mibBuilder.loadTexts:
    wfIpxRipIntfTable.setStatus("mandatory")
_WfIpxRipIntfEntry_Object = MibTableRow
wfIpxRipIntfEntry = _WfIpxRipIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1)
)
wfIpxRipIntfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxRipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfIpxRipIntfEntry.setStatus("mandatory")


class _WfIpxRipInterfaceDelete_Type(Integer32):
    """Custom type wfIpxRipInterfaceDelete based on Integer32"""
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


_WfIpxRipInterfaceDelete_Type.__name__ = "Integer32"
_WfIpxRipInterfaceDelete_Object = MibTableColumn
wfIpxRipInterfaceDelete = _WfIpxRipInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 1),
    _WfIpxRipInterfaceDelete_Type()
)
wfIpxRipInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceDelete.setStatus("mandatory")


class _WfIpxRipInterfaceDisable_Type(Integer32):
    """Custom type wfIpxRipInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxRipInterfaceDisable_Type.__name__ = "Integer32"
_WfIpxRipInterfaceDisable_Object = MibTableColumn
wfIpxRipInterfaceDisable = _WfIpxRipInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 2),
    _WfIpxRipInterfaceDisable_Type()
)
wfIpxRipInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceDisable.setStatus("mandatory")


class _WfIpxRipInterfaceState_Type(Integer32):
    """Custom type wfIpxRipInterfaceState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpxRipInterfaceState_Type.__name__ = "Integer32"
_WfIpxRipInterfaceState_Object = MibTableColumn
wfIpxRipInterfaceState = _WfIpxRipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 3),
    _WfIpxRipInterfaceState_Type()
)
wfIpxRipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceState.setStatus("mandatory")
_WfIpxRipInterfaceIndex_Type = OctetString
_WfIpxRipInterfaceIndex_Object = MibTableColumn
wfIpxRipInterfaceIndex = _WfIpxRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 4),
    _WfIpxRipInterfaceIndex_Type()
)
wfIpxRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceIndex.setStatus("mandatory")


class _WfIpxRipInterfaceSupply_Type(Integer32):
    """Custom type wfIpxRipInterfaceSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxRipInterfaceSupply_Type.__name__ = "Integer32"
_WfIpxRipInterfaceSupply_Object = MibTableColumn
wfIpxRipInterfaceSupply = _WfIpxRipInterfaceSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 5),
    _WfIpxRipInterfaceSupply_Type()
)
wfIpxRipInterfaceSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceSupply.setStatus("mandatory")


class _WfIpxRipInterfaceListen_Type(Integer32):
    """Custom type wfIpxRipInterfaceListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxRipInterfaceListen_Type.__name__ = "Integer32"
_WfIpxRipInterfaceListen_Object = MibTableColumn
wfIpxRipInterfaceListen = _WfIpxRipInterfaceListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 5, 1, 6),
    _WfIpxRipInterfaceListen_Type()
)
wfIpxRipInterfaceListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxRipInterfaceListen.setStatus("mandatory")
_WfIpxAdjacentHostTable_Object = MibTable
wfIpxAdjacentHostTable = _WfIpxAdjacentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6)
)
if mibBuilder.loadTexts:
    wfIpxAdjacentHostTable.setStatus("mandatory")
_WfIpxAdjacentHostEntry_Object = MibTableRow
wfIpxAdjacentHostEntry = _WfIpxAdjacentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1)
)
wfIpxAdjacentHostEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxAhTargHostNetwork"),
    (0, "Wellfleet-Series7-MIB", "wfIpxAhTargHostId"),
)
if mibBuilder.loadTexts:
    wfIpxAdjacentHostEntry.setStatus("mandatory")


class _WfIpxAhDelete_Type(Integer32):
    """Custom type wfIpxAhDelete based on Integer32"""
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


_WfIpxAhDelete_Type.__name__ = "Integer32"
_WfIpxAhDelete_Object = MibTableColumn
wfIpxAhDelete = _WfIpxAhDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 1),
    _WfIpxAhDelete_Type()
)
wfIpxAhDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhDelete.setStatus("mandatory")


class _WfIpxAhDisable_Type(Integer32):
    """Custom type wfIpxAhDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxAhDisable_Type.__name__ = "Integer32"
_WfIpxAhDisable_Object = MibTableColumn
wfIpxAhDisable = _WfIpxAhDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 2),
    _WfIpxAhDisable_Type()
)
wfIpxAhDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhDisable.setStatus("mandatory")
_WfIpxAhTargHostNetwork_Type = OctetString
_WfIpxAhTargHostNetwork_Object = MibTableColumn
wfIpxAhTargHostNetwork = _WfIpxAhTargHostNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 3),
    _WfIpxAhTargHostNetwork_Type()
)
wfIpxAhTargHostNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAhTargHostNetwork.setStatus("mandatory")
_WfIpxAhTargHostId_Type = OctetString
_WfIpxAhTargHostId_Object = MibTableColumn
wfIpxAhTargHostId = _WfIpxAhTargHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 4),
    _WfIpxAhTargHostId_Type()
)
wfIpxAhTargHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxAhTargHostId.setStatus("mandatory")
_WfIpxAhNextHopIntf_Type = OctetString
_WfIpxAhNextHopIntf_Object = MibTableColumn
wfIpxAhNextHopIntf = _WfIpxAhNextHopIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 5),
    _WfIpxAhNextHopIntf_Type()
)
wfIpxAhNextHopIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhNextHopIntf.setStatus("mandatory")
_WfIpxAhDlci_Type = OctetString
_WfIpxAhDlci_Object = MibTableColumn
wfIpxAhDlci = _WfIpxAhDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 6, 1, 6),
    _WfIpxAhDlci_Type()
)
wfIpxAhDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxAhDlci.setStatus("mandatory")
_WfIpxStaticRouteTable_Object = MibTable
wfIpxStaticRouteTable = _WfIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7)
)
if mibBuilder.loadTexts:
    wfIpxStaticRouteTable.setStatus("mandatory")
_WfIpxStaticRouteEntry_Object = MibTableRow
wfIpxStaticRouteEntry = _WfIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1)
)
wfIpxStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxSrTargNetwork"),
    (0, "Wellfleet-Series7-MIB", "wfIpxSrNextHopNetwork"),
)
if mibBuilder.loadTexts:
    wfIpxStaticRouteEntry.setStatus("mandatory")


class _WfIpxSrDelete_Type(Integer32):
    """Custom type wfIpxSrDelete based on Integer32"""
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


_WfIpxSrDelete_Type.__name__ = "Integer32"
_WfIpxSrDelete_Object = MibTableColumn
wfIpxSrDelete = _WfIpxSrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 1),
    _WfIpxSrDelete_Type()
)
wfIpxSrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrDelete.setStatus("mandatory")


class _WfIpxSrDisable_Type(Integer32):
    """Custom type wfIpxSrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxSrDisable_Type.__name__ = "Integer32"
_WfIpxSrDisable_Object = MibTableColumn
wfIpxSrDisable = _WfIpxSrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 2),
    _WfIpxSrDisable_Type()
)
wfIpxSrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrDisable.setStatus("mandatory")
_WfIpxSrTargNetwork_Type = OctetString
_WfIpxSrTargNetwork_Object = MibTableColumn
wfIpxSrTargNetwork = _WfIpxSrTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 3),
    _WfIpxSrTargNetwork_Type()
)
wfIpxSrTargNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSrTargNetwork.setStatus("mandatory")
_WfIpxSrCost_Type = Integer32
_WfIpxSrCost_Object = MibTableColumn
wfIpxSrCost = _WfIpxSrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 4),
    _WfIpxSrCost_Type()
)
wfIpxSrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrCost.setStatus("mandatory")
_WfIpxSrNextHopNetwork_Type = OctetString
_WfIpxSrNextHopNetwork_Object = MibTableColumn
wfIpxSrNextHopNetwork = _WfIpxSrNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 5),
    _WfIpxSrNextHopNetwork_Type()
)
wfIpxSrNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSrNextHopNetwork.setStatus("mandatory")
_WfIpxSrNextHopHost_Type = OctetString
_WfIpxSrNextHopHost_Object = MibTableColumn
wfIpxSrNextHopHost = _WfIpxSrNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 6),
    _WfIpxSrNextHopHost_Type()
)
wfIpxSrNextHopHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSrNextHopHost.setStatus("mandatory")
_WfIpxSrTargNetworkRt_Type = Integer32
_WfIpxSrTargNetworkRt_Object = MibTableColumn
wfIpxSrTargNetworkRt = _WfIpxSrTargNetworkRt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 7, 1, 7),
    _WfIpxSrTargNetworkRt_Type()
)
wfIpxSrTargNetworkRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSrTargNetworkRt.setStatus("mandatory")
_WfIpxNetBiosStaticRouteTable_Object = MibTable
wfIpxNetBiosStaticRouteTable = _WfIpxNetBiosStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8)
)
if mibBuilder.loadTexts:
    wfIpxNetBiosStaticRouteTable.setStatus("mandatory")
_WfIpxNetBiosStaticRouteEntry_Object = MibTableRow
wfIpxNetBiosStaticRouteEntry = _WfIpxNetBiosStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1)
)
wfIpxNetBiosStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxNetBiosSrTargNetwork"),
    (0, "Wellfleet-Series7-MIB", "wfIpxNetBiosSrIntf"),
)
if mibBuilder.loadTexts:
    wfIpxNetBiosStaticRouteEntry.setStatus("mandatory")


class _WfIpxNetBiosSrDelete_Type(Integer32):
    """Custom type wfIpxNetBiosSrDelete based on Integer32"""
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


_WfIpxNetBiosSrDelete_Type.__name__ = "Integer32"
_WfIpxNetBiosSrDelete_Object = MibTableColumn
wfIpxNetBiosSrDelete = _WfIpxNetBiosSrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 1),
    _WfIpxNetBiosSrDelete_Type()
)
wfIpxNetBiosSrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrDelete.setStatus("mandatory")


class _WfIpxNetBiosSrDisable_Type(Integer32):
    """Custom type wfIpxNetBiosSrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxNetBiosSrDisable_Type.__name__ = "Integer32"
_WfIpxNetBiosSrDisable_Object = MibTableColumn
wfIpxNetBiosSrDisable = _WfIpxNetBiosSrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 2),
    _WfIpxNetBiosSrDisable_Type()
)
wfIpxNetBiosSrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrDisable.setStatus("mandatory")
_WfIpxNetBiosSrTargNetwork_Type = OctetString
_WfIpxNetBiosSrTargNetwork_Object = MibTableColumn
wfIpxNetBiosSrTargNetwork = _WfIpxNetBiosSrTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 3),
    _WfIpxNetBiosSrTargNetwork_Type()
)
wfIpxNetBiosSrTargNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrTargNetwork.setStatus("mandatory")
_WfIpxNetBiosSrName_Type = OctetString
_WfIpxNetBiosSrName_Object = MibTableColumn
wfIpxNetBiosSrName = _WfIpxNetBiosSrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 4),
    _WfIpxNetBiosSrName_Type()
)
wfIpxNetBiosSrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrName.setStatus("mandatory")
_WfIpxNetBiosSrIntf_Type = OctetString
_WfIpxNetBiosSrIntf_Object = MibTableColumn
wfIpxNetBiosSrIntf = _WfIpxNetBiosSrIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 5),
    _WfIpxNetBiosSrIntf_Type()
)
wfIpxNetBiosSrIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrIntf.setStatus("mandatory")
_WfIpxNetBiosSrIndex_Type = Integer32
_WfIpxNetBiosSrIndex_Object = MibTableColumn
wfIpxNetBiosSrIndex = _WfIpxNetBiosSrIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 8, 1, 6),
    _WfIpxNetBiosSrIndex_Type()
)
wfIpxNetBiosSrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxNetBiosSrIndex.setStatus("mandatory")
_WfIpxSapNetLvlFilterTable_Object = MibTable
wfIpxSapNetLvlFilterTable = _WfIpxSapNetLvlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9)
)
if mibBuilder.loadTexts:
    wfIpxSapNetLvlFilterTable.setStatus("mandatory")
_WfIpxSapNetLvlFilter_Object = MibTableRow
wfIpxSapNetLvlFilter = _WfIpxSapNetLvlFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1)
)
wfIpxSapNetLvlFilter.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxSapNetLvlIntf"),
    (0, "Wellfleet-Series7-MIB", "wfIpxSapNetLvlIndex"),
)
if mibBuilder.loadTexts:
    wfIpxSapNetLvlFilter.setStatus("mandatory")


class _WfIpxSapNetLvlDelete_Type(Integer32):
    """Custom type wfIpxSapNetLvlDelete based on Integer32"""
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


_WfIpxSapNetLvlDelete_Type.__name__ = "Integer32"
_WfIpxSapNetLvlDelete_Object = MibTableColumn
wfIpxSapNetLvlDelete = _WfIpxSapNetLvlDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 1),
    _WfIpxSapNetLvlDelete_Type()
)
wfIpxSapNetLvlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlDelete.setStatus("mandatory")


class _WfIpxSapNetLvlDisable_Type(Integer32):
    """Custom type wfIpxSapNetLvlDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxSapNetLvlDisable_Type.__name__ = "Integer32"
_WfIpxSapNetLvlDisable_Object = MibTableColumn
wfIpxSapNetLvlDisable = _WfIpxSapNetLvlDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 2),
    _WfIpxSapNetLvlDisable_Type()
)
wfIpxSapNetLvlDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlDisable.setStatus("mandatory")
_WfIpxSapNetLvlTargNetwork_Type = OctetString
_WfIpxSapNetLvlTargNetwork_Object = MibTableColumn
wfIpxSapNetLvlTargNetwork = _WfIpxSapNetLvlTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 3),
    _WfIpxSapNetLvlTargNetwork_Type()
)
wfIpxSapNetLvlTargNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlTargNetwork.setStatus("mandatory")
_WfIpxSapNetLvlType_Type = OctetString
_WfIpxSapNetLvlType_Object = MibTableColumn
wfIpxSapNetLvlType = _WfIpxSapNetLvlType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 4),
    _WfIpxSapNetLvlType_Type()
)
wfIpxSapNetLvlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlType.setStatus("mandatory")


class _WfIpxSapNetLvlAction_Type(Integer32):
    """Custom type wfIpxSapNetLvlAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfIpxSapNetLvlAction_Type.__name__ = "Integer32"
_WfIpxSapNetLvlAction_Object = MibTableColumn
wfIpxSapNetLvlAction = _WfIpxSapNetLvlAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 5),
    _WfIpxSapNetLvlAction_Type()
)
wfIpxSapNetLvlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlAction.setStatus("mandatory")
_WfIpxSapNetLvlIntf_Type = OctetString
_WfIpxSapNetLvlIntf_Object = MibTableColumn
wfIpxSapNetLvlIntf = _WfIpxSapNetLvlIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 6),
    _WfIpxSapNetLvlIntf_Type()
)
wfIpxSapNetLvlIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlIntf.setStatus("mandatory")
_WfIpxSapNetLvlIndex_Type = Integer32
_WfIpxSapNetLvlIndex_Object = MibTableColumn
wfIpxSapNetLvlIndex = _WfIpxSapNetLvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 9, 1, 7),
    _WfIpxSapNetLvlIndex_Type()
)
wfIpxSapNetLvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapNetLvlIndex.setStatus("mandatory")
_WfIpxSapServtLvlFilterTable_Object = MibTable
wfIpxSapServtLvlFilterTable = _WfIpxSapServtLvlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10)
)
if mibBuilder.loadTexts:
    wfIpxSapServtLvlFilterTable.setStatus("mandatory")
_WfIpxSapServLvlFilter_Object = MibTableRow
wfIpxSapServLvlFilter = _WfIpxSapServLvlFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1)
)
wfIpxSapServLvlFilter.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxSapServLvlIntf"),
    (0, "Wellfleet-Series7-MIB", "wfIpxSapServLvlIndex"),
)
if mibBuilder.loadTexts:
    wfIpxSapServLvlFilter.setStatus("mandatory")


class _WfIpxSapServLvlDelete_Type(Integer32):
    """Custom type wfIpxSapServLvlDelete based on Integer32"""
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


_WfIpxSapServLvlDelete_Type.__name__ = "Integer32"
_WfIpxSapServLvlDelete_Object = MibTableColumn
wfIpxSapServLvlDelete = _WfIpxSapServLvlDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 1),
    _WfIpxSapServLvlDelete_Type()
)
wfIpxSapServLvlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlDelete.setStatus("mandatory")


class _WfIpxSapServLvlDisable_Type(Integer32):
    """Custom type wfIpxSapServLvlDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxSapServLvlDisable_Type.__name__ = "Integer32"
_WfIpxSapServLvlDisable_Object = MibTableColumn
wfIpxSapServLvlDisable = _WfIpxSapServLvlDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 2),
    _WfIpxSapServLvlDisable_Type()
)
wfIpxSapServLvlDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlDisable.setStatus("mandatory")
_WfIpxSapServLvlTargServer_Type = DisplayString
_WfIpxSapServLvlTargServer_Object = MibTableColumn
wfIpxSapServLvlTargServer = _WfIpxSapServLvlTargServer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 3),
    _WfIpxSapServLvlTargServer_Type()
)
wfIpxSapServLvlTargServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlTargServer.setStatus("mandatory")
_WfIpxSapServLvlType_Type = OctetString
_WfIpxSapServLvlType_Object = MibTableColumn
wfIpxSapServLvlType = _WfIpxSapServLvlType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 4),
    _WfIpxSapServLvlType_Type()
)
wfIpxSapServLvlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlType.setStatus("mandatory")


class _WfIpxSapServLvlAction_Type(Integer32):
    """Custom type wfIpxSapServLvlAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfIpxSapServLvlAction_Type.__name__ = "Integer32"
_WfIpxSapServLvlAction_Object = MibTableColumn
wfIpxSapServLvlAction = _WfIpxSapServLvlAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 5),
    _WfIpxSapServLvlAction_Type()
)
wfIpxSapServLvlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxSapServLvlAction.setStatus("mandatory")
_WfIpxSapServLvlIntf_Type = OctetString
_WfIpxSapServLvlIntf_Object = MibTableColumn
wfIpxSapServLvlIntf = _WfIpxSapServLvlIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 6),
    _WfIpxSapServLvlIntf_Type()
)
wfIpxSapServLvlIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapServLvlIntf.setStatus("mandatory")
_WfIpxSapServLvlIndex_Type = Integer32
_WfIpxSapServLvlIndex_Object = MibTableColumn
wfIpxSapServLvlIndex = _WfIpxSapServLvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 10, 1, 7),
    _WfIpxSapServLvlIndex_Type()
)
wfIpxSapServLvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxSapServLvlIndex.setStatus("mandatory")
_WfIpxTrafficFilterTable_Object = MibTable
wfIpxTrafficFilterTable = _WfIpxTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11)
)
if mibBuilder.loadTexts:
    wfIpxTrafficFilterTable.setStatus("mandatory")
_WfIpxTrafficFilterEntry_Object = MibTableRow
wfIpxTrafficFilterEntry = _WfIpxTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1)
)
wfIpxTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfIpxTrafficFilterInterface"),
    (0, "Wellfleet-Series7-MIB", "wfIpxTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfIpxTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfIpxTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfIpxTrafficFilterEntry.setStatus("mandatory")


class _WfIpxTrafficFilterCreate_Type(Integer32):
    """Custom type wfIpxTrafficFilterCreate based on Integer32"""
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


_WfIpxTrafficFilterCreate_Type.__name__ = "Integer32"
_WfIpxTrafficFilterCreate_Object = MibTableColumn
wfIpxTrafficFilterCreate = _WfIpxTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 1),
    _WfIpxTrafficFilterCreate_Type()
)
wfIpxTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterCreate.setStatus("mandatory")


class _WfIpxTrafficFilterEnable_Type(Integer32):
    """Custom type wfIpxTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpxTrafficFilterEnable_Type.__name__ = "Integer32"
_WfIpxTrafficFilterEnable_Object = MibTableColumn
wfIpxTrafficFilterEnable = _WfIpxTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 2),
    _WfIpxTrafficFilterEnable_Type()
)
wfIpxTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterEnable.setStatus("mandatory")


class _WfIpxTrafficFilterStatus_Type(Integer32):
    """Custom type wfIpxTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfIpxTrafficFilterStatus_Type.__name__ = "Integer32"
_WfIpxTrafficFilterStatus_Object = MibTableColumn
wfIpxTrafficFilterStatus = _WfIpxTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 3),
    _WfIpxTrafficFilterStatus_Type()
)
wfIpxTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterStatus.setStatus("mandatory")
_WfIpxTrafficFilterCounter_Type = Counter32
_WfIpxTrafficFilterCounter_Object = MibTableColumn
wfIpxTrafficFilterCounter = _WfIpxTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 4),
    _WfIpxTrafficFilterCounter_Type()
)
wfIpxTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterCounter.setStatus("mandatory")
_WfIpxTrafficFilterDefinition_Type = Opaque
_WfIpxTrafficFilterDefinition_Object = MibTableColumn
wfIpxTrafficFilterDefinition = _WfIpxTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 5),
    _WfIpxTrafficFilterDefinition_Type()
)
wfIpxTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterDefinition.setStatus("mandatory")
_WfIpxTrafficFilterReserved_Type = Integer32
_WfIpxTrafficFilterReserved_Object = MibTableColumn
wfIpxTrafficFilterReserved = _WfIpxTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 6),
    _WfIpxTrafficFilterReserved_Type()
)
wfIpxTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterReserved.setStatus("mandatory")
_WfIpxTrafficFilterInterface_Type = OctetString
_WfIpxTrafficFilterInterface_Object = MibTableColumn
wfIpxTrafficFilterInterface = _WfIpxTrafficFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 7),
    _WfIpxTrafficFilterInterface_Type()
)
wfIpxTrafficFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterInterface.setStatus("mandatory")
_WfIpxTrafficFilterCircuit_Type = Integer32
_WfIpxTrafficFilterCircuit_Object = MibTableColumn
wfIpxTrafficFilterCircuit = _WfIpxTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 8),
    _WfIpxTrafficFilterCircuit_Type()
)
wfIpxTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterCircuit.setStatus("mandatory")
_WfIpxTrafficFilterRuleNumber_Type = Integer32
_WfIpxTrafficFilterRuleNumber_Object = MibTableColumn
wfIpxTrafficFilterRuleNumber = _WfIpxTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 9),
    _WfIpxTrafficFilterRuleNumber_Type()
)
wfIpxTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterRuleNumber.setStatus("mandatory")
_WfIpxTrafficFilterFragment_Type = Integer32
_WfIpxTrafficFilterFragment_Object = MibTableColumn
wfIpxTrafficFilterFragment = _WfIpxTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 11, 1, 10),
    _WfIpxTrafficFilterFragment_Type()
)
wfIpxTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpxTrafficFilterFragment.setStatus("mandatory")
_WfOsiGroup_ObjectIdentity = ObjectIdentity
wfOsiGroup = _WfOsiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6)
)
_WfVinesGroup_ObjectIdentity = ObjectIdentity
wfVinesGroup = _WfVinesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8)
)
_WfVinesBase_ObjectIdentity = ObjectIdentity
wfVinesBase = _WfVinesBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1)
)


class _WfVinesBaseDelete_Type(Integer32):
    """Custom type wfVinesBaseDelete based on Integer32"""
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


_WfVinesBaseDelete_Type.__name__ = "Integer32"
_WfVinesBaseDelete_Object = MibScalar
wfVinesBaseDelete = _WfVinesBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 1),
    _WfVinesBaseDelete_Type()
)
wfVinesBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseDelete.setStatus("mandatory")


class _WfVinesBaseDisable_Type(Integer32):
    """Custom type wfVinesBaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesBaseDisable_Type.__name__ = "Integer32"
_WfVinesBaseDisable_Object = MibScalar
wfVinesBaseDisable = _WfVinesBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 2),
    _WfVinesBaseDisable_Type()
)
wfVinesBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseDisable.setStatus("mandatory")


class _WfVinesBaseState_Type(Integer32):
    """Custom type wfVinesBaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfVinesBaseState_Type.__name__ = "Integer32"
_WfVinesBaseState_Object = MibScalar
wfVinesBaseState = _WfVinesBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 3),
    _WfVinesBaseState_Type()
)
wfVinesBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesBaseState.setStatus("mandatory")


class _WfVinesBaseUserNetid_Type(Integer32):
    """Custom type wfVinesBaseUserNetid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2097151)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 2097151),
          ("minimum", 1))
    )


_WfVinesBaseUserNetid_Type.__name__ = "Integer32"
_WfVinesBaseUserNetid_Object = MibScalar
wfVinesBaseUserNetid = _WfVinesBaseUserNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 4),
    _WfVinesBaseUserNetid_Type()
)
wfVinesBaseUserNetid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseUserNetid.setStatus("mandatory")
_WfVinesBaseRouterNetid_Type = Counter32
_WfVinesBaseRouterNetid_Object = MibScalar
wfVinesBaseRouterNetid = _WfVinesBaseRouterNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 5),
    _WfVinesBaseRouterNetid_Type()
)
wfVinesBaseRouterNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesBaseRouterNetid.setStatus("mandatory")


class _WfVinesBaseBcastClass_Type(Integer32):
    """Custom type wfVinesBaseBcastClass based on Integer32"""
    defaultValue = 1

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
        *(("alllans", 8),
          ("bcast", 1),
          ("chrg", 2),
          ("cost", 3),
          ("lans", 4),
          ("locost", 7),
          ("nochrg", 6),
          ("srvr", 5))
    )


_WfVinesBaseBcastClass_Type.__name__ = "Integer32"
_WfVinesBaseBcastClass_Object = MibScalar
wfVinesBaseBcastClass = _WfVinesBaseBcastClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 6),
    _WfVinesBaseBcastClass_Type()
)
wfVinesBaseBcastClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseBcastClass.setStatus("mandatory")
_WfVinesIp_ObjectIdentity = ObjectIdentity
wfVinesIp = _WfVinesIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2)
)
_WfVinesIpTotIn_Type = Counter32
_WfVinesIpTotIn_Object = MibScalar
wfVinesIpTotIn = _WfVinesIpTotIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 1),
    _WfVinesIpTotIn_Type()
)
wfVinesIpTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpTotIn.setStatus("mandatory")
_WfVinesIpTotOut_Type = Counter32
_WfVinesIpTotOut_Object = MibScalar
wfVinesIpTotOut = _WfVinesIpTotOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 2),
    _WfVinesIpTotOut_Type()
)
wfVinesIpTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpTotOut.setStatus("mandatory")
_WfVinesIpBad_Type = Counter32
_WfVinesIpBad_Object = MibScalar
wfVinesIpBad = _WfVinesIpBad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 3),
    _WfVinesIpBad_Type()
)
wfVinesIpBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpBad.setStatus("mandatory")
_WfVinesIpRouted_Type = Counter32
_WfVinesIpRouted_Object = MibScalar
wfVinesIpRouted = _WfVinesIpRouted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 4),
    _WfVinesIpRouted_Type()
)
wfVinesIpRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpRouted.setStatus("mandatory")
_WfVinesIpRoutedHWM_Type = Integer32
_WfVinesIpRoutedHWM_Object = MibScalar
wfVinesIpRoutedHWM = _WfVinesIpRoutedHWM_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 5),
    _WfVinesIpRoutedHWM_Type()
)
wfVinesIpRoutedHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpRoutedHWM.setStatus("mandatory")
_WfVinesIpBcast_Type = Counter32
_WfVinesIpBcast_Object = MibScalar
wfVinesIpBcast = _WfVinesIpBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 6),
    _WfVinesIpBcast_Type()
)
wfVinesIpBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpBcast.setStatus("mandatory")
_WfVinesIpBcastHWM_Type = Integer32
_WfVinesIpBcastHWM_Object = MibScalar
wfVinesIpBcastHWM = _WfVinesIpBcastHWM_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 7),
    _WfVinesIpBcastHWM_Type()
)
wfVinesIpBcastHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpBcastHWM.setStatus("mandatory")
_WfVinesIpReass_Type = Counter32
_WfVinesIpReass_Object = MibScalar
wfVinesIpReass = _WfVinesIpReass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 8),
    _WfVinesIpReass_Type()
)
wfVinesIpReass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpReass.setStatus("mandatory")
_WfVinesIpFrags_Type = Counter32
_WfVinesIpFrags_Object = MibScalar
wfVinesIpFrags = _WfVinesIpFrags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 9),
    _WfVinesIpFrags_Type()
)
wfVinesIpFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpFrags.setStatus("mandatory")
_WfVinesIpToDodIP_Type = Counter32
_WfVinesIpToDodIP_Object = MibScalar
wfVinesIpToDodIP = _WfVinesIpToDodIP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 10),
    _WfVinesIpToDodIP_Type()
)
wfVinesIpToDodIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpToDodIP.setStatus("mandatory")
_WfVinesIpFromDodIP_Type = Counter32
_WfVinesIpFromDodIP_Object = MibScalar
wfVinesIpFromDodIP = _WfVinesIpFromDodIP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 11),
    _WfVinesIpFromDodIP_Type()
)
wfVinesIpFromDodIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpFromDodIP.setStatus("mandatory")
_WfVinesRtpNbr_ObjectIdentity = ObjectIdentity
wfVinesRtpNbr = _WfVinesRtpNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 3)
)
_WfVinesRtpNbrNumber_Type = Integer32
_WfVinesRtpNbrNumber_Object = MibScalar
wfVinesRtpNbrNumber = _WfVinesRtpNbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 3, 1),
    _WfVinesRtpNbrNumber_Type()
)
wfVinesRtpNbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrNumber.setStatus("mandatory")
_WfVinesRtpNbrTable_Object = MibTable
wfVinesRtpNbrTable = _WfVinesRtpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4)
)
if mibBuilder.loadTexts:
    wfVinesRtpNbrTable.setStatus("mandatory")
_WfVinesRtpNbrEntry_Object = MibTableRow
wfVinesRtpNbrEntry = _WfVinesRtpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1)
)
wfVinesRtpNbrEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfVinesRtpNbrNetId"),
)
if mibBuilder.loadTexts:
    wfVinesRtpNbrEntry.setStatus("mandatory")
_WfVinesRtpNbrNetId_Type = Counter32
_WfVinesRtpNbrNetId_Object = MibTableColumn
wfVinesRtpNbrNetId = _WfVinesRtpNbrNetId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 1),
    _WfVinesRtpNbrNetId_Type()
)
wfVinesRtpNbrNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrNetId.setStatus("mandatory")
_WfVinesRtpNbrSubNetId_Type = Integer32
_WfVinesRtpNbrSubNetId_Object = MibTableColumn
wfVinesRtpNbrSubNetId = _WfVinesRtpNbrSubNetId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 2),
    _WfVinesRtpNbrSubNetId_Type()
)
wfVinesRtpNbrSubNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrSubNetId.setStatus("mandatory")


class _WfVinesRtpNbrType_Type(Integer32):
    """Custom type wfVinesRtpNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 2),
          ("workst", 1))
    )


_WfVinesRtpNbrType_Type.__name__ = "Integer32"
_WfVinesRtpNbrType_Object = MibTableColumn
wfVinesRtpNbrType = _WfVinesRtpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 3),
    _WfVinesRtpNbrType_Type()
)
wfVinesRtpNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrType.setStatus("mandatory")


class _WfVinesRtpNbrIfType_Type(Integer32):
    """Custom type wfVinesRtpNbrIfType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("async1200", 8),
          ("async4800", 9),
          ("async56000", 11),
          ("async9600", 10),
          ("enet", 1),
          ("fddi", 31),
          ("hdlc1200", 4),
          ("hdlc4800", 5),
          ("hdlc56000", 7),
          ("hdlc9600", 6),
          ("t11088k", 28),
          ("t1128k", 17),
          ("t11344k", 29),
          ("t1192k", 18),
          ("t1256k", 19),
          ("t1320k", 20),
          ("t1384k", 21),
          ("t1448k", 22),
          ("t145k", 16),
          ("t1512k", 23),
          ("t1576k", 24),
          ("t1640k", 25),
          ("t1704k", 26),
          ("t1896k", 27),
          ("tr16k", 3),
          ("tr4k", 2),
          ("tunnel", 30),
          ("x251200", 12),
          ("x254800", 13),
          ("x2556000", 15),
          ("x259600", 14))
    )


_WfVinesRtpNbrIfType_Type.__name__ = "Integer32"
_WfVinesRtpNbrIfType_Object = MibTableColumn
wfVinesRtpNbrIfType = _WfVinesRtpNbrIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 4),
    _WfVinesRtpNbrIfType_Type()
)
wfVinesRtpNbrIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrIfType.setStatus("mandatory")
_WfVinesRtpNbrRemAdr_Type = OctetString
_WfVinesRtpNbrRemAdr_Object = MibTableColumn
wfVinesRtpNbrRemAdr = _WfVinesRtpNbrRemAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 5),
    _WfVinesRtpNbrRemAdr_Type()
)
wfVinesRtpNbrRemAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrRemAdr.setStatus("mandatory")
_WfVinesRtpNbrLocAdr_Type = OctetString
_WfVinesRtpNbrLocAdr_Object = MibTableColumn
wfVinesRtpNbrLocAdr = _WfVinesRtpNbrLocAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 6),
    _WfVinesRtpNbrLocAdr_Type()
)
wfVinesRtpNbrLocAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrLocAdr.setStatus("mandatory")
_WfVinesRtpNbrLocSlot_Type = Integer32
_WfVinesRtpNbrLocSlot_Object = MibTableColumn
wfVinesRtpNbrLocSlot = _WfVinesRtpNbrLocSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 7),
    _WfVinesRtpNbrLocSlot_Type()
)
wfVinesRtpNbrLocSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrLocSlot.setStatus("mandatory")
_WfVinesRtpNbrLocLine_Type = Integer32
_WfVinesRtpNbrLocLine_Object = MibTableColumn
wfVinesRtpNbrLocLine = _WfVinesRtpNbrLocLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 8),
    _WfVinesRtpNbrLocLine_Type()
)
wfVinesRtpNbrLocLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrLocLine.setStatus("mandatory")
_WfVinesRtpNbrSvrName_Type = OctetString
_WfVinesRtpNbrSvrName_Object = MibTableColumn
wfVinesRtpNbrSvrName = _WfVinesRtpNbrSvrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 9),
    _WfVinesRtpNbrSvrName_Type()
)
wfVinesRtpNbrSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrSvrName.setStatus("mandatory")
_WfVinesRtpNbrCost_Type = Integer32
_WfVinesRtpNbrCost_Object = MibTableColumn
wfVinesRtpNbrCost = _WfVinesRtpNbrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 10),
    _WfVinesRtpNbrCost_Type()
)
wfVinesRtpNbrCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrCost.setStatus("mandatory")
_WfVinesRtpRt_ObjectIdentity = ObjectIdentity
wfVinesRtpRt = _WfVinesRtpRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 5)
)
_WfVinesRtpRtNumber_Type = Integer32
_WfVinesRtpRtNumber_Object = MibScalar
wfVinesRtpRtNumber = _WfVinesRtpRtNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 5, 1),
    _WfVinesRtpRtNumber_Type()
)
wfVinesRtpRtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtNumber.setStatus("mandatory")
_WfVinesRtpRtTable_Object = MibTable
wfVinesRtpRtTable = _WfVinesRtpRtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6)
)
if mibBuilder.loadTexts:
    wfVinesRtpRtTable.setStatus("mandatory")
_WfVinesRtpRtEntry_Object = MibTableRow
wfVinesRtpRtEntry = _WfVinesRtpRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1)
)
wfVinesRtpRtEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfVinesRtpRtNetid"),
)
if mibBuilder.loadTexts:
    wfVinesRtpRtEntry.setStatus("mandatory")
_WfVinesRtpRtNetid_Type = Counter32
_WfVinesRtpRtNetid_Object = MibTableColumn
wfVinesRtpRtNetid = _WfVinesRtpRtNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 1),
    _WfVinesRtpRtNetid_Type()
)
wfVinesRtpRtNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtNetid.setStatus("mandatory")
_WfVinesRtpRtMetric_Type = Integer32
_WfVinesRtpRtMetric_Object = MibTableColumn
wfVinesRtpRtMetric = _WfVinesRtpRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 2),
    _WfVinesRtpRtMetric_Type()
)
wfVinesRtpRtMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtMetric.setStatus("mandatory")
_WfVinesRtpRtIdle_Type = Integer32
_WfVinesRtpRtIdle_Object = MibTableColumn
wfVinesRtpRtIdle = _WfVinesRtpRtIdle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 3),
    _WfVinesRtpRtIdle_Type()
)
wfVinesRtpRtIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtIdle.setStatus("mandatory")
_WfVinesRtpRtGateNetid_Type = Counter32
_WfVinesRtpRtGateNetid_Object = MibTableColumn
wfVinesRtpRtGateNetid = _WfVinesRtpRtGateNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 4),
    _WfVinesRtpRtGateNetid_Type()
)
wfVinesRtpRtGateNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtGateNetid.setStatus("mandatory")
_WfVinesRtpRtSvrName_Type = OctetString
_WfVinesRtpRtSvrName_Object = MibTableColumn
wfVinesRtpRtSvrName = _WfVinesRtpRtSvrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 5),
    _WfVinesRtpRtSvrName_Type()
)
wfVinesRtpRtSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtSvrName.setStatus("mandatory")
_WfVinesRtpRtGateSvrName_Type = OctetString
_WfVinesRtpRtGateSvrName_Object = MibTableColumn
wfVinesRtpRtGateSvrName = _WfVinesRtpRtGateSvrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 6),
    _WfVinesRtpRtGateSvrName_Type()
)
wfVinesRtpRtGateSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtGateSvrName.setStatus("mandatory")
_WfVinesIf_ObjectIdentity = ObjectIdentity
wfVinesIf = _WfVinesIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 7)
)
_WfVinesIfNumber_Type = Integer32
_WfVinesIfNumber_Object = MibScalar
wfVinesIfNumber = _WfVinesIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 7, 1),
    _WfVinesIfNumber_Type()
)
wfVinesIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfNumber.setStatus("mandatory")
_WfVinesIfTable_Object = MibTable
wfVinesIfTable = _WfVinesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8)
)
if mibBuilder.loadTexts:
    wfVinesIfTable.setStatus("mandatory")
_WfVinesIfEntry_Object = MibTableRow
wfVinesIfEntry = _WfVinesIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1)
)
wfVinesIfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfVinesIfCct"),
)
if mibBuilder.loadTexts:
    wfVinesIfEntry.setStatus("mandatory")


class _WfVinesIfDelete_Type(Integer32):
    """Custom type wfVinesIfDelete based on Integer32"""
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


_WfVinesIfDelete_Type.__name__ = "Integer32"
_WfVinesIfDelete_Object = MibTableColumn
wfVinesIfDelete = _WfVinesIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 1),
    _WfVinesIfDelete_Type()
)
wfVinesIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfDelete.setStatus("mandatory")


class _WfVinesIfDisable_Type(Integer32):
    """Custom type wfVinesIfDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesIfDisable_Type.__name__ = "Integer32"
_WfVinesIfDisable_Object = MibTableColumn
wfVinesIfDisable = _WfVinesIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 2),
    _WfVinesIfDisable_Type()
)
wfVinesIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfDisable.setStatus("mandatory")


class _WfVinesIfState_Type(Integer32):
    """Custom type wfVinesIfState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfVinesIfState_Type.__name__ = "Integer32"
_WfVinesIfState_Object = MibTableColumn
wfVinesIfState = _WfVinesIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 3),
    _WfVinesIfState_Type()
)
wfVinesIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfState.setStatus("mandatory")
_WfVinesIfSlot_Type = Integer32
_WfVinesIfSlot_Object = MibTableColumn
wfVinesIfSlot = _WfVinesIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 4),
    _WfVinesIfSlot_Type()
)
wfVinesIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSlot.setStatus("mandatory")
_WfVinesIfLine_Type = Integer32
_WfVinesIfLine_Object = MibTableColumn
wfVinesIfLine = _WfVinesIfLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 5),
    _WfVinesIfLine_Type()
)
wfVinesIfLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfLine.setStatus("mandatory")
_WfVinesIfCct_Type = Integer32
_WfVinesIfCct_Object = MibTableColumn
wfVinesIfCct = _WfVinesIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 6),
    _WfVinesIfCct_Type()
)
wfVinesIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfCct.setStatus("mandatory")
_WfVinesIfSession_Type = Integer32
_WfVinesIfSession_Object = MibTableColumn
wfVinesIfSession = _WfVinesIfSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 7),
    _WfVinesIfSession_Type()
)
wfVinesIfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSession.setStatus("mandatory")


class _WfVinesIfType_Type(Integer32):
    """Custom type wfVinesIfType based on Integer32"""
    defaultValue = 1

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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("async1200", 8),
          ("async4800", 9),
          ("async56000", 11),
          ("async9600", 10),
          ("enet", 1),
          ("fddi", 31),
          ("hdlc1200", 4),
          ("hdlc4800", 5),
          ("hdlc56000", 7),
          ("hdlc9600", 6),
          ("t11088k", 28),
          ("t1128k", 17),
          ("t11344k", 29),
          ("t1192k", 18),
          ("t1256k", 19),
          ("t1320k", 20),
          ("t1384k", 21),
          ("t1448k", 22),
          ("t145k", 16),
          ("t1512k", 23),
          ("t1576k", 24),
          ("t1640k", 25),
          ("t1704k", 26),
          ("t1896k", 27),
          ("tr16k", 3),
          ("tr4k", 2),
          ("tunnel", 30),
          ("x251200", 12),
          ("x254800", 13),
          ("x2556000", 15),
          ("x259600", 14))
    )


_WfVinesIfType_Type.__name__ = "Integer32"
_WfVinesIfType_Object = MibTableColumn
wfVinesIfType = _WfVinesIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 8),
    _WfVinesIfType_Type()
)
wfVinesIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfType.setStatus("mandatory")
_WfVinesIfDescr_Type = OctetString
_WfVinesIfDescr_Object = MibTableColumn
wfVinesIfDescr = _WfVinesIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 9),
    _WfVinesIfDescr_Type()
)
wfVinesIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfDescr.setStatus("mandatory")
_WfVinesIfAdr_Type = OctetString
_WfVinesIfAdr_Object = MibTableColumn
wfVinesIfAdr = _WfVinesIfAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 10),
    _WfVinesIfAdr_Type()
)
wfVinesIfAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfAdr.setStatus("mandatory")


class _WfVinesIfDodIpDisable_Type(Integer32):
    """Custom type wfVinesIfDodIpDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesIfDodIpDisable_Type.__name__ = "Integer32"
_WfVinesIfDodIpDisable_Object = MibTableColumn
wfVinesIfDodIpDisable = _WfVinesIfDodIpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 11),
    _WfVinesIfDodIpDisable_Type()
)
wfVinesIfDodIpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfDodIpDisable.setStatus("mandatory")


class _WfVinesIfArpDisable_Type(Integer32):
    """Custom type wfVinesIfArpDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesIfArpDisable_Type.__name__ = "Integer32"
_WfVinesIfArpDisable_Object = MibTableColumn
wfVinesIfArpDisable = _WfVinesIfArpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 12),
    _WfVinesIfArpDisable_Type()
)
wfVinesIfArpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfArpDisable.setStatus("mandatory")


class _WfVinesIfTrEndStation_Type(Integer32):
    """Custom type wfVinesIfTrEndStation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesIfTrEndStation_Type.__name__ = "Integer32"
_WfVinesIfTrEndStation_Object = MibTableColumn
wfVinesIfTrEndStation = _WfVinesIfTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 13),
    _WfVinesIfTrEndStation_Type()
)
wfVinesIfTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfTrEndStation.setStatus("mandatory")
_WfVinesIfInPkts_Type = Counter32
_WfVinesIfInPkts_Object = MibTableColumn
wfVinesIfInPkts = _WfVinesIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 14),
    _WfVinesIfInPkts_Type()
)
wfVinesIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInPkts.setStatus("mandatory")
_WfVinesIfInErrs_Type = Counter32
_WfVinesIfInErrs_Object = MibTableColumn
wfVinesIfInErrs = _WfVinesIfInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 15),
    _WfVinesIfInErrs_Type()
)
wfVinesIfInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInErrs.setStatus("mandatory")
_WfVinesIfOutPkts_Type = Counter32
_WfVinesIfOutPkts_Object = MibTableColumn
wfVinesIfOutPkts = _WfVinesIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 16),
    _WfVinesIfOutPkts_Type()
)
wfVinesIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutPkts.setStatus("mandatory")
_WfVinesIfOutErrs_Type = Counter32
_WfVinesIfOutErrs_Object = MibTableColumn
wfVinesIfOutErrs = _WfVinesIfOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 17),
    _WfVinesIfOutErrs_Type()
)
wfVinesIfOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutErrs.setStatus("mandatory")
_WfVinesIfInMsgs_Type = Counter32
_WfVinesIfInMsgs_Object = MibTableColumn
wfVinesIfInMsgs = _WfVinesIfInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 18),
    _WfVinesIfInMsgs_Type()
)
wfVinesIfInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInMsgs.setStatus("mandatory")


class _WfVinesIfMux_Type(Integer32):
    """Custom type wfVinesIfMux based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enet", 1),
          ("snap", 2))
    )


_WfVinesIfMux_Type.__name__ = "Integer32"
_WfVinesIfMux_Object = MibTableColumn
wfVinesIfMux = _WfVinesIfMux_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 19),
    _WfVinesIfMux_Type()
)
wfVinesIfMux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfMux.setStatus("mandatory")
_WfVinesIfFwdDrops_Type = Counter32
_WfVinesIfFwdDrops_Object = MibTableColumn
wfVinesIfFwdDrops = _WfVinesIfFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 20),
    _WfVinesIfFwdDrops_Type()
)
wfVinesIfFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfFwdDrops.setStatus("mandatory")
_WfVinesIfZeroHopDrops_Type = Counter32
_WfVinesIfZeroHopDrops_Object = MibTableColumn
wfVinesIfZeroHopDrops = _WfVinesIfZeroHopDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 21),
    _WfVinesIfZeroHopDrops_Type()
)
wfVinesIfZeroHopDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfZeroHopDrops.setStatus("mandatory")
_WfVinesIfIcpInErrorNotifs_Type = Counter32
_WfVinesIfIcpInErrorNotifs_Object = MibTableColumn
wfVinesIfIcpInErrorNotifs = _WfVinesIfIcpInErrorNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 22),
    _WfVinesIfIcpInErrorNotifs_Type()
)
wfVinesIfIcpInErrorNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpInErrorNotifs.setStatus("mandatory")
_WfVinesIfIcpInMetricNotifs_Type = Counter32
_WfVinesIfIcpInMetricNotifs_Object = MibTableColumn
wfVinesIfIcpInMetricNotifs = _WfVinesIfIcpInMetricNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 23),
    _WfVinesIfIcpInMetricNotifs_Type()
)
wfVinesIfIcpInMetricNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpInMetricNotifs.setStatus("mandatory")
_WfVinesIfIcpInErrors_Type = Counter32
_WfVinesIfIcpInErrors_Object = MibTableColumn
wfVinesIfIcpInErrors = _WfVinesIfIcpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 24),
    _WfVinesIfIcpInErrors_Type()
)
wfVinesIfIcpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpInErrors.setStatus("mandatory")
_WfVinesIfIcpOutErrorNotifs_Type = Counter32
_WfVinesIfIcpOutErrorNotifs_Object = MibTableColumn
wfVinesIfIcpOutErrorNotifs = _WfVinesIfIcpOutErrorNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 25),
    _WfVinesIfIcpOutErrorNotifs_Type()
)
wfVinesIfIcpOutErrorNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpOutErrorNotifs.setStatus("mandatory")
_WfVinesIfIcpOutMetricNotifs_Type = Counter32
_WfVinesIfIcpOutMetricNotifs_Object = MibTableColumn
wfVinesIfIcpOutMetricNotifs = _WfVinesIfIcpOutMetricNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 26),
    _WfVinesIfIcpOutMetricNotifs_Type()
)
wfVinesIfIcpOutMetricNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpOutMetricNotifs.setStatus("mandatory")
_WfVinesIfArpInQueries_Type = Counter32
_WfVinesIfArpInQueries_Object = MibTableColumn
wfVinesIfArpInQueries = _WfVinesIfArpInQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 27),
    _WfVinesIfArpInQueries_Type()
)
wfVinesIfArpInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpInQueries.setStatus("mandatory")
_WfVinesIfArpInAssgReqs_Type = Counter32
_WfVinesIfArpInAssgReqs_Object = MibTableColumn
wfVinesIfArpInAssgReqs = _WfVinesIfArpInAssgReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 28),
    _WfVinesIfArpInAssgReqs_Type()
)
wfVinesIfArpInAssgReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpInAssgReqs.setStatus("mandatory")
_WfVinesIfArpInErrors_Type = Counter32
_WfVinesIfArpInErrors_Object = MibTableColumn
wfVinesIfArpInErrors = _WfVinesIfArpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 29),
    _WfVinesIfArpInErrors_Type()
)
wfVinesIfArpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpInErrors.setStatus("mandatory")
_WfVinesIfArpOutServRsps_Type = Counter32
_WfVinesIfArpOutServRsps_Object = MibTableColumn
wfVinesIfArpOutServRsps = _WfVinesIfArpOutServRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 30),
    _WfVinesIfArpOutServRsps_Type()
)
wfVinesIfArpOutServRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpOutServRsps.setStatus("mandatory")
_WfVinesIfArpOutAssgRsps_Type = Counter32
_WfVinesIfArpOutAssgRsps_Object = MibTableColumn
wfVinesIfArpOutAssgRsps = _WfVinesIfArpOutAssgRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 31),
    _WfVinesIfArpOutAssgRsps_Type()
)
wfVinesIfArpOutAssgRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpOutAssgRsps.setStatus("mandatory")
_WfVinesIfInRedirects_Type = Counter32
_WfVinesIfInRedirects_Object = MibTableColumn
wfVinesIfInRedirects = _WfVinesIfInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 32),
    _WfVinesIfInRedirects_Type()
)
wfVinesIfInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInRedirects.setStatus("mandatory")
_WfVinesIfOutRedirects_Type = Counter32
_WfVinesIfOutRedirects_Object = MibTableColumn
wfVinesIfOutRedirects = _WfVinesIfOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 33),
    _WfVinesIfOutRedirects_Type()
)
wfVinesIfOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutRedirects.setStatus("mandatory")
_WfVinesIfEchoInPkts_Type = Counter32
_WfVinesIfEchoInPkts_Object = MibTableColumn
wfVinesIfEchoInPkts = _WfVinesIfEchoInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 34),
    _WfVinesIfEchoInPkts_Type()
)
wfVinesIfEchoInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfEchoInPkts.setStatus("mandatory")
_WfVinesIfEchoOutPkts_Type = Counter32
_WfVinesIfEchoOutPkts_Object = MibTableColumn
wfVinesIfEchoOutPkts = _WfVinesIfEchoOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 35),
    _WfVinesIfEchoOutPkts_Type()
)
wfVinesIfEchoOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfEchoOutPkts.setStatus("mandatory")
_WfVinesIfReassFails_Type = Counter32
_WfVinesIfReassFails_Object = MibTableColumn
wfVinesIfReassFails = _WfVinesIfReassFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 36),
    _WfVinesIfReassFails_Type()
)
wfVinesIfReassFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfReassFails.setStatus("mandatory")


class _WfVinesIfRemClientPrivDisable_Type(Integer32):
    """Custom type wfVinesIfRemClientPrivDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesIfRemClientPrivDisable_Type.__name__ = "Integer32"
_WfVinesIfRemClientPrivDisable_Object = MibTableColumn
wfVinesIfRemClientPrivDisable = _WfVinesIfRemClientPrivDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 37),
    _WfVinesIfRemClientPrivDisable_Type()
)
wfVinesIfRemClientPrivDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfRemClientPrivDisable.setStatus("mandatory")
_WfVinesIfX25VC_ObjectIdentity = ObjectIdentity
wfVinesIfX25VC = _WfVinesIfX25VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 9)
)
_WfVinesIfX25VCNumber_Type = Integer32
_WfVinesIfX25VCNumber_Object = MibScalar
wfVinesIfX25VCNumber = _WfVinesIfX25VCNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 9, 1),
    _WfVinesIfX25VCNumber_Type()
)
wfVinesIfX25VCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCNumber.setStatus("mandatory")
_WfVinesIfX25VCTable_Object = MibTable
wfVinesIfX25VCTable = _WfVinesIfX25VCTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10)
)
if mibBuilder.loadTexts:
    wfVinesIfX25VCTable.setStatus("mandatory")
_WfVinesIfX25VCEntry_Object = MibTableRow
wfVinesIfX25VCEntry = _WfVinesIfX25VCEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1)
)
wfVinesIfX25VCEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfVinesIfX25VCCct"),
)
if mibBuilder.loadTexts:
    wfVinesIfX25VCEntry.setStatus("mandatory")
_WfVinesIfX25VCSlot_Type = Integer32
_WfVinesIfX25VCSlot_Object = MibTableColumn
wfVinesIfX25VCSlot = _WfVinesIfX25VCSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 1),
    _WfVinesIfX25VCSlot_Type()
)
wfVinesIfX25VCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCSlot.setStatus("mandatory")
_WfVinesIfX25VCLine_Type = Integer32
_WfVinesIfX25VCLine_Object = MibTableColumn
wfVinesIfX25VCLine = _WfVinesIfX25VCLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 2),
    _WfVinesIfX25VCLine_Type()
)
wfVinesIfX25VCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCLine.setStatus("mandatory")
_WfVinesIfX25VCCct_Type = Integer32
_WfVinesIfX25VCCct_Object = MibTableColumn
wfVinesIfX25VCCct = _WfVinesIfX25VCCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 3),
    _WfVinesIfX25VCCct_Type()
)
wfVinesIfX25VCCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCCct.setStatus("mandatory")
_WfVinesIfX25VCSession_Type = Integer32
_WfVinesIfX25VCSession_Object = MibTableColumn
wfVinesIfX25VCSession = _WfVinesIfX25VCSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 4),
    _WfVinesIfX25VCSession_Type()
)
wfVinesIfX25VCSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCSession.setStatus("mandatory")
_WfVinesIfX25VCTotIn_Type = Counter32
_WfVinesIfX25VCTotIn_Object = MibTableColumn
wfVinesIfX25VCTotIn = _WfVinesIfX25VCTotIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 5),
    _WfVinesIfX25VCTotIn_Type()
)
wfVinesIfX25VCTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCTotIn.setStatus("mandatory")
_WfVinesIfX25VCTotOut_Type = Counter32
_WfVinesIfX25VCTotOut_Object = MibTableColumn
wfVinesIfX25VCTotOut = _WfVinesIfX25VCTotOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 6),
    _WfVinesIfX25VCTotOut_Type()
)
wfVinesIfX25VCTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCTotOut.setStatus("mandatory")
_WfVinesIfX25VCInErrs_Type = Counter32
_WfVinesIfX25VCInErrs_Object = MibTableColumn
wfVinesIfX25VCInErrs = _WfVinesIfX25VCInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 7),
    _WfVinesIfX25VCInErrs_Type()
)
wfVinesIfX25VCInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCInErrs.setStatus("mandatory")
_WfVinesIfX25VCOutErrs_Type = Counter32
_WfVinesIfX25VCOutErrs_Object = MibTableColumn
wfVinesIfX25VCOutErrs = _WfVinesIfX25VCOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 8),
    _WfVinesIfX25VCOutErrs_Type()
)
wfVinesIfX25VCOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCOutErrs.setStatus("mandatory")
_WfVinesIfX25VCPktsOut_Type = Counter32
_WfVinesIfX25VCPktsOut_Object = MibTableColumn
wfVinesIfX25VCPktsOut = _WfVinesIfX25VCPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 9),
    _WfVinesIfX25VCPktsOut_Type()
)
wfVinesIfX25VCPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCPktsOut.setStatus("mandatory")
_WfVinesIfX25VCPktsAwaitAck_Type = Integer32
_WfVinesIfX25VCPktsAwaitAck_Object = MibTableColumn
wfVinesIfX25VCPktsAwaitAck = _WfVinesIfX25VCPktsAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 10),
    _WfVinesIfX25VCPktsAwaitAck_Type()
)
wfVinesIfX25VCPktsAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCPktsAwaitAck.setStatus("mandatory")
_WfVinesIfX25VCBytesOut_Type = Counter32
_WfVinesIfX25VCBytesOut_Object = MibTableColumn
wfVinesIfX25VCBytesOut = _WfVinesIfX25VCBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 11),
    _WfVinesIfX25VCBytesOut_Type()
)
wfVinesIfX25VCBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCBytesOut.setStatus("mandatory")
_WfVinesIfX25VCBytesAwaitAck_Type = Integer32
_WfVinesIfX25VCBytesAwaitAck_Object = MibTableColumn
wfVinesIfX25VCBytesAwaitAck = _WfVinesIfX25VCBytesAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 12),
    _WfVinesIfX25VCBytesAwaitAck_Type()
)
wfVinesIfX25VCBytesAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCBytesAwaitAck.setStatus("mandatory")
_WfVinesIfX25VCPktsIn_Type = Counter32
_WfVinesIfX25VCPktsIn_Object = MibTableColumn
wfVinesIfX25VCPktsIn = _WfVinesIfX25VCPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 13),
    _WfVinesIfX25VCPktsIn_Type()
)
wfVinesIfX25VCPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCPktsIn.setStatus("mandatory")
_WfVinesIfX25VCBytesIn_Type = Counter32
_WfVinesIfX25VCBytesIn_Object = MibTableColumn
wfVinesIfX25VCBytesIn = _WfVinesIfX25VCBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 14),
    _WfVinesIfX25VCBytesIn_Type()
)
wfVinesIfX25VCBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCBytesIn.setStatus("mandatory")
_WfVinesIfX25VCResetsIn_Type = Counter32
_WfVinesIfX25VCResetsIn_Object = MibTableColumn
wfVinesIfX25VCResetsIn = _WfVinesIfX25VCResetsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 15),
    _WfVinesIfX25VCResetsIn_Type()
)
wfVinesIfX25VCResetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCResetsIn.setStatus("mandatory")
_WfVinesIfX25VCResetsOut_Type = Counter32
_WfVinesIfX25VCResetsOut_Object = MibTableColumn
wfVinesIfX25VCResetsOut = _WfVinesIfX25VCResetsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 16),
    _WfVinesIfX25VCResetsOut_Type()
)
wfVinesIfX25VCResetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCResetsOut.setStatus("mandatory")
_WfVinesTrafficFilterTable_Object = MibTable
wfVinesTrafficFilterTable = _WfVinesTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11)
)
if mibBuilder.loadTexts:
    wfVinesTrafficFilterTable.setStatus("mandatory")
_WfVinesTrafficFilterEntry_Object = MibTableRow
wfVinesTrafficFilterEntry = _WfVinesTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1)
)
wfVinesTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfVinesTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfVinesTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfVinesTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfVinesTrafficFilterEntry.setStatus("mandatory")


class _WfVinesTrafficFilterCreate_Type(Integer32):
    """Custom type wfVinesTrafficFilterCreate based on Integer32"""
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


_WfVinesTrafficFilterCreate_Type.__name__ = "Integer32"
_WfVinesTrafficFilterCreate_Object = MibTableColumn
wfVinesTrafficFilterCreate = _WfVinesTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 1),
    _WfVinesTrafficFilterCreate_Type()
)
wfVinesTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterCreate.setStatus("mandatory")


class _WfVinesTrafficFilterEnable_Type(Integer32):
    """Custom type wfVinesTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesTrafficFilterEnable_Type.__name__ = "Integer32"
_WfVinesTrafficFilterEnable_Object = MibTableColumn
wfVinesTrafficFilterEnable = _WfVinesTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 2),
    _WfVinesTrafficFilterEnable_Type()
)
wfVinesTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterEnable.setStatus("mandatory")


class _WfVinesTrafficFilterStatus_Type(Integer32):
    """Custom type wfVinesTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfVinesTrafficFilterStatus_Type.__name__ = "Integer32"
_WfVinesTrafficFilterStatus_Object = MibTableColumn
wfVinesTrafficFilterStatus = _WfVinesTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 3),
    _WfVinesTrafficFilterStatus_Type()
)
wfVinesTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterStatus.setStatus("mandatory")
_WfVinesTrafficFilterCounter_Type = Counter32
_WfVinesTrafficFilterCounter_Object = MibTableColumn
wfVinesTrafficFilterCounter = _WfVinesTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 4),
    _WfVinesTrafficFilterCounter_Type()
)
wfVinesTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterCounter.setStatus("mandatory")
_WfVinesTrafficFilterDefinition_Type = OctetString
_WfVinesTrafficFilterDefinition_Object = MibTableColumn
wfVinesTrafficFilterDefinition = _WfVinesTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 5),
    _WfVinesTrafficFilterDefinition_Type()
)
wfVinesTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterDefinition.setStatus("mandatory")
_WfVinesTrafficFilterReserved_Type = Integer32
_WfVinesTrafficFilterReserved_Object = MibTableColumn
wfVinesTrafficFilterReserved = _WfVinesTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 6),
    _WfVinesTrafficFilterReserved_Type()
)
wfVinesTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterReserved.setStatus("mandatory")
_WfVinesTrafficFilterCircuit_Type = Integer32
_WfVinesTrafficFilterCircuit_Object = MibTableColumn
wfVinesTrafficFilterCircuit = _WfVinesTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 7),
    _WfVinesTrafficFilterCircuit_Type()
)
wfVinesTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterCircuit.setStatus("mandatory")
_WfVinesTrafficFilterRuleNumber_Type = Integer32
_WfVinesTrafficFilterRuleNumber_Object = MibTableColumn
wfVinesTrafficFilterRuleNumber = _WfVinesTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 8),
    _WfVinesTrafficFilterRuleNumber_Type()
)
wfVinesTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterRuleNumber.setStatus("mandatory")
_WfVinesTrafficFilterFragment_Type = Integer32
_WfVinesTrafficFilterFragment_Object = MibTableColumn
wfVinesTrafficFilterFragment = _WfVinesTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 9),
    _WfVinesTrafficFilterFragment_Type()
)
wfVinesTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterFragment.setStatus("mandatory")
_WfVinesNameTable_Object = MibTable
wfVinesNameTable = _WfVinesNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12)
)
if mibBuilder.loadTexts:
    wfVinesNameTable.setStatus("mandatory")
_WfVinesNameEntry_Object = MibTableRow
wfVinesNameEntry = _WfVinesNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1)
)
wfVinesNameEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfVinesNameNetid"),
)
if mibBuilder.loadTexts:
    wfVinesNameEntry.setStatus("mandatory")


class _WfVinesNameDelete_Type(Integer32):
    """Custom type wfVinesNameDelete based on Integer32"""
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


_WfVinesNameDelete_Type.__name__ = "Integer32"
_WfVinesNameDelete_Object = MibTableColumn
wfVinesNameDelete = _WfVinesNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 1),
    _WfVinesNameDelete_Type()
)
wfVinesNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameDelete.setStatus("mandatory")


class _WfVinesNameDisable_Type(Integer32):
    """Custom type wfVinesNameDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesNameDisable_Type.__name__ = "Integer32"
_WfVinesNameDisable_Object = MibTableColumn
wfVinesNameDisable = _WfVinesNameDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 2),
    _WfVinesNameDisable_Type()
)
wfVinesNameDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameDisable.setStatus("mandatory")
_WfVinesNameNetid_Type = Counter32
_WfVinesNameNetid_Object = MibTableColumn
wfVinesNameNetid = _WfVinesNameNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 3),
    _WfVinesNameNetid_Type()
)
wfVinesNameNetid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameNetid.setStatus("mandatory")
_WfVinesNameHost_Type = DisplayString
_WfVinesNameHost_Object = MibTableColumn
wfVinesNameHost = _WfVinesNameHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 4),
    _WfVinesNameHost_Type()
)
wfVinesNameHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameHost.setStatus("mandatory")
_WfVinesNameSubNetid_Type = Integer32
_WfVinesNameSubNetid_Object = MibTableColumn
wfVinesNameSubNetid = _WfVinesNameSubNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 5),
    _WfVinesNameSubNetid_Type()
)
wfVinesNameSubNetid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameSubNetid.setStatus("mandatory")
_WfVinesArp_ObjectIdentity = ObjectIdentity
wfVinesArp = _WfVinesArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13)
)


class _WfVinesArpDelete_Type(Integer32):
    """Custom type wfVinesArpDelete based on Integer32"""
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


_WfVinesArpDelete_Type.__name__ = "Integer32"
_WfVinesArpDelete_Object = MibScalar
wfVinesArpDelete = _WfVinesArpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 1),
    _WfVinesArpDelete_Type()
)
wfVinesArpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesArpDelete.setStatus("mandatory")


class _WfVinesArpDisable_Type(Integer32):
    """Custom type wfVinesArpDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVinesArpDisable_Type.__name__ = "Integer32"
_WfVinesArpDisable_Object = MibScalar
wfVinesArpDisable = _WfVinesArpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 2),
    _WfVinesArpDisable_Type()
)
wfVinesArpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesArpDisable.setStatus("mandatory")


class _WfVinesArpState_Type(Integer32):
    """Custom type wfVinesArpState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfVinesArpState_Type.__name__ = "Integer32"
_WfVinesArpState_Object = MibScalar
wfVinesArpState = _WfVinesArpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 3),
    _WfVinesArpState_Type()
)
wfVinesArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesArpState.setStatus("mandatory")
_WfVinesArpSubnetid_Type = Integer32
_WfVinesArpSubnetid_Object = MibScalar
wfVinesArpSubnetid = _WfVinesArpSubnetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 4),
    _WfVinesArpSubnetid_Type()
)
wfVinesArpSubnetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesArpSubnetid.setStatus("mandatory")


class _WfVinesArpSubnetBlock_Type(Integer32):
    """Custom type wfVinesArpSubnetBlock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              32)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("maximum", 32),
          ("minimum", 1))
    )


_WfVinesArpSubnetBlock_Type.__name__ = "Integer32"
_WfVinesArpSubnetBlock_Object = MibScalar
wfVinesArpSubnetBlock = _WfVinesArpSubnetBlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 5),
    _WfVinesArpSubnetBlock_Type()
)
wfVinesArpSubnetBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesArpSubnetBlock.setStatus("mandatory")
_WfVinesArpAssignDeniedPkts_Type = Counter32
_WfVinesArpAssignDeniedPkts_Object = MibScalar
wfVinesArpAssignDeniedPkts = _WfVinesArpAssignDeniedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 6),
    _WfVinesArpAssignDeniedPkts_Type()
)
wfVinesArpAssignDeniedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesArpAssignDeniedPkts.setStatus("mandatory")
_WfWanGroup_ObjectIdentity = ObjectIdentity
wfWanGroup = _WfWanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9)
)
_WfFrameRelayGroup_ObjectIdentity = ObjectIdentity
wfFrameRelayGroup = _WfFrameRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1)
)
_WfFrDlcmiTable_Object = MibTable
wfFrDlcmiTable = _WfFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1)
)
if mibBuilder.loadTexts:
    wfFrDlcmiTable.setStatus("mandatory")
_WfFrDlcmiEntry_Object = MibTableRow
wfFrDlcmiEntry = _WfFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1)
)
wfFrDlcmiEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfFrDlcmiCircuit"),
)
if mibBuilder.loadTexts:
    wfFrDlcmiEntry.setStatus("mandatory")


class _WfFrDlcmiDelete_Type(Integer32):
    """Custom type wfFrDlcmiDelete based on Integer32"""
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


_WfFrDlcmiDelete_Type.__name__ = "Integer32"
_WfFrDlcmiDelete_Object = MibTableColumn
wfFrDlcmiDelete = _WfFrDlcmiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 1),
    _WfFrDlcmiDelete_Type()
)
wfFrDlcmiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiDelete.setStatus("mandatory")


class _WfFrDlcmiDisable_Type(Integer32):
    """Custom type wfFrDlcmiDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfFrDlcmiDisable_Type.__name__ = "Integer32"
_WfFrDlcmiDisable_Object = MibTableColumn
wfFrDlcmiDisable = _WfFrDlcmiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 2),
    _WfFrDlcmiDisable_Type()
)
wfFrDlcmiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiDisable.setStatus("mandatory")


class _WfFrDlcmiState_Type(Integer32):
    """Custom type wfFrDlcmiState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfFrDlcmiState_Type.__name__ = "Integer32"
_WfFrDlcmiState_Object = MibTableColumn
wfFrDlcmiState = _WfFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 3),
    _WfFrDlcmiState_Type()
)
wfFrDlcmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiState.setStatus("mandatory")
_WfFrDlcmiCircuit_Type = Integer32
_WfFrDlcmiCircuit_Object = MibTableColumn
wfFrDlcmiCircuit = _WfFrDlcmiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 4),
    _WfFrDlcmiCircuit_Type()
)
wfFrDlcmiCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiCircuit.setStatus("mandatory")


class _WfFrDlcmiManagementType_Type(Integer32):
    """Custom type wfFrDlcmiManagementType based on Integer32"""
    defaultValue = 3

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
        *(("annexa", 5),
          ("annexaswitch", 8),
          ("annexdswitch", 7),
          ("lmi", 2),
          ("lmiswitch", 6),
          ("none", 1),
          ("t1617b", 4),
          ("t1617d", 3))
    )


_WfFrDlcmiManagementType_Type.__name__ = "Integer32"
_WfFrDlcmiManagementType_Object = MibTableColumn
wfFrDlcmiManagementType = _WfFrDlcmiManagementType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 5),
    _WfFrDlcmiManagementType_Type()
)
wfFrDlcmiManagementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiManagementType.setStatus("mandatory")


class _WfFrDlcmiStatus_Type(Integer32):
    """Custom type wfFrDlcmiStatus based on Integer32"""
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
        *(("fault", 3),
          ("recovered", 4),
          ("running", 2),
          ("start", 1))
    )


_WfFrDlcmiStatus_Type.__name__ = "Integer32"
_WfFrDlcmiStatus_Object = MibTableColumn
wfFrDlcmiStatus = _WfFrDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 6),
    _WfFrDlcmiStatus_Type()
)
wfFrDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiStatus.setStatus("mandatory")


class _WfFrDlcmiAddress_Type(Integer32):
    """Custom type wfFrDlcmiAddress based on Integer32"""
    defaultValue = 4

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
        *(("q921", 1),
          ("q922", 4),
          ("q922march90", 2),
          ("q922november90", 3))
    )


_WfFrDlcmiAddress_Type.__name__ = "Integer32"
_WfFrDlcmiAddress_Object = MibTableColumn
wfFrDlcmiAddress = _WfFrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 7),
    _WfFrDlcmiAddress_Type()
)
wfFrDlcmiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiAddress.setStatus("mandatory")


class _WfFrDlcmiAddressLen_Type(Integer32):
    """Custom type wfFrDlcmiAddressLen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourbyte", 4),
          ("threebyte", 3),
          ("twobyte", 2))
    )


_WfFrDlcmiAddressLen_Type.__name__ = "Integer32"
_WfFrDlcmiAddressLen_Object = MibTableColumn
wfFrDlcmiAddressLen = _WfFrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 8),
    _WfFrDlcmiAddressLen_Type()
)
wfFrDlcmiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiAddressLen.setStatus("mandatory")


class _WfFrDlcmiPollingInterval_Type(Integer32):
    """Custom type wfFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              30)
        )
    )
    namedValues = NamedValues(
        *(("default", 10),
          ("maximum", 30),
          ("minimum", 5))
    )


_WfFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_WfFrDlcmiPollingInterval_Object = MibTableColumn
wfFrDlcmiPollingInterval = _WfFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 9),
    _WfFrDlcmiPollingInterval_Type()
)
wfFrDlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiPollingInterval.setStatus("mandatory")


class _WfFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type wfFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 6),
          ("maximum", 255),
          ("minimum", 1))
    )


_WfFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_WfFrDlcmiFullEnquiryInterval_Object = MibTableColumn
wfFrDlcmiFullEnquiryInterval = _WfFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 10),
    _WfFrDlcmiFullEnquiryInterval_Type()
)
wfFrDlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiFullEnquiryInterval.setStatus("mandatory")


class _WfFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type wfFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3


_WfFrDlcmiErrorThreshold_Object = MibTableColumn
wfFrDlcmiErrorThreshold = _WfFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 11),
    _WfFrDlcmiErrorThreshold_Type()
)
wfFrDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiErrorThreshold.setStatus("mandatory")


class _WfFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type wfFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4


_WfFrDlcmiMonitoredEvents_Object = MibTableColumn
wfFrDlcmiMonitoredEvents = _WfFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 12),
    _WfFrDlcmiMonitoredEvents_Type()
)
wfFrDlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiMonitoredEvents.setStatus("mandatory")
_WfFrDlcmiMaxSupportedVCs_Type = Integer32
_WfFrDlcmiMaxSupportedVCs_Object = MibTableColumn
wfFrDlcmiMaxSupportedVCs = _WfFrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 13),
    _WfFrDlcmiMaxSupportedVCs_Type()
)
wfFrDlcmiMaxSupportedVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiMaxSupportedVCs.setStatus("mandatory")


class _WfFrDlcmiMulticast_Type(Integer32):
    """Custom type wfFrDlcmiMulticast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfFrDlcmiMulticast_Type.__name__ = "Integer32"
_WfFrDlcmiMulticast_Object = MibTableColumn
wfFrDlcmiMulticast = _WfFrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 14),
    _WfFrDlcmiMulticast_Type()
)
wfFrDlcmiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiMulticast.setStatus("mandatory")


class _WfFrDlcmiSeqCount_Type(Integer32):
    """Custom type wfFrDlcmiSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 255),
          ("minimum", 1))
    )


_WfFrDlcmiSeqCount_Type.__name__ = "Integer32"
_WfFrDlcmiSeqCount_Object = MibTableColumn
wfFrDlcmiSeqCount = _WfFrDlcmiSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 15),
    _WfFrDlcmiSeqCount_Type()
)
wfFrDlcmiSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiSeqCount.setStatus("mandatory")


class _WfFrDlcmiLastReceived_Type(Integer32):
    """Custom type wfFrDlcmiLastReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 255),
          ("minimum", 1))
    )


_WfFrDlcmiLastReceived_Type.__name__ = "Integer32"
_WfFrDlcmiLastReceived_Object = MibTableColumn
wfFrDlcmiLastReceived = _WfFrDlcmiLastReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 16),
    _WfFrDlcmiLastReceived_Type()
)
wfFrDlcmiLastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiLastReceived.setStatus("mandatory")


class _WfFrDlcmiPassiveSeqCount_Type(Integer32):
    """Custom type wfFrDlcmiPassiveSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 255),
          ("minimum", 1))
    )


_WfFrDlcmiPassiveSeqCount_Type.__name__ = "Integer32"
_WfFrDlcmiPassiveSeqCount_Object = MibTableColumn
wfFrDlcmiPassiveSeqCount = _WfFrDlcmiPassiveSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 17),
    _WfFrDlcmiPassiveSeqCount_Type()
)
wfFrDlcmiPassiveSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiPassiveSeqCount.setStatus("mandatory")


class _WfFrDlcmiPassiveReceived_Type(Integer32):
    """Custom type wfFrDlcmiPassiveReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 255),
          ("minimum", 1))
    )


_WfFrDlcmiPassiveReceived_Type.__name__ = "Integer32"
_WfFrDlcmiPassiveReceived_Object = MibTableColumn
wfFrDlcmiPassiveReceived = _WfFrDlcmiPassiveReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 18),
    _WfFrDlcmiPassiveReceived_Type()
)
wfFrDlcmiPassiveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiPassiveReceived.setStatus("mandatory")
_WfFrDlcmiPolls_Type = Integer32
_WfFrDlcmiPolls_Object = MibTableColumn
wfFrDlcmiPolls = _WfFrDlcmiPolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 19),
    _WfFrDlcmiPolls_Type()
)
wfFrDlcmiPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiPolls.setStatus("mandatory")
_WfFrDlcmiAlarmTimer_Type = Integer32
_WfFrDlcmiAlarmTimer_Object = MibTableColumn
wfFrDlcmiAlarmTimer = _WfFrDlcmiAlarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 20),
    _WfFrDlcmiAlarmTimer_Type()
)
wfFrDlcmiAlarmTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiAlarmTimer.setStatus("mandatory")


class _WfFrErrType_Type(Integer32):
    """Custom type wfFrErrType based on Integer32"""
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
        *(("cntrl", 11),
          ("illegaldlci", 4),
          ("long", 3),
          ("protoerr", 6),
          ("reset", 10),
          ("sequenceerr", 8),
          ("short", 2),
          ("unknown", 1),
          ("unknowndlci", 5),
          ("unknownie", 7),
          ("unknownrpt", 9))
    )


_WfFrErrType_Type.__name__ = "Integer32"
_WfFrErrType_Object = MibTableColumn
wfFrErrType = _WfFrErrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 21),
    _WfFrErrType_Type()
)
wfFrErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrType.setStatus("mandatory")
_WfFrErrData_Type = OctetString
_WfFrErrData_Object = MibTableColumn
wfFrErrData = _WfFrErrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 22),
    _WfFrErrData_Type()
)
wfFrErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrData.setStatus("mandatory")
_WfFrErrTime_Type = TimeTicks
_WfFrErrTime_Object = MibTableColumn
wfFrErrTime = _WfFrErrTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 23),
    _WfFrErrTime_Type()
)
wfFrErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrTime.setStatus("mandatory")
_WfFrErrDiscards_Type = Counter32
_WfFrErrDiscards_Object = MibTableColumn
wfFrErrDiscards = _WfFrErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 24),
    _WfFrErrDiscards_Type()
)
wfFrErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrDiscards.setStatus("mandatory")
_WfFrErrDrops_Type = Counter32
_WfFrErrDrops_Object = MibTableColumn
wfFrErrDrops = _WfFrErrDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 25),
    _WfFrErrDrops_Type()
)
wfFrErrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrDrops.setStatus("mandatory")
_WfFrCircuitTable_Object = MibTable
wfFrCircuitTable = _WfFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2)
)
if mibBuilder.loadTexts:
    wfFrCircuitTable.setStatus("mandatory")
_WfFrCircuitEntry_Object = MibTableRow
wfFrCircuitEntry = _WfFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1)
)
wfFrCircuitEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfFrCircuitNumber"),
    (0, "Wellfleet-Series7-MIB", "wfFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    wfFrCircuitEntry.setStatus("mandatory")


class _WfFrCircuitDelete_Type(Integer32):
    """Custom type wfFrCircuitDelete based on Integer32"""
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
        *(("created", 1),
          ("deleted", 2),
          ("system", 3))
    )


_WfFrCircuitDelete_Type.__name__ = "Integer32"
_WfFrCircuitDelete_Object = MibTableColumn
wfFrCircuitDelete = _WfFrCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 1),
    _WfFrCircuitDelete_Type()
)
wfFrCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitDelete.setStatus("mandatory")
_WfFrCircuitNumber_Type = Integer32
_WfFrCircuitNumber_Object = MibTableColumn
wfFrCircuitNumber = _WfFrCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 2),
    _WfFrCircuitNumber_Type()
)
wfFrCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitNumber.setStatus("mandatory")


class _WfFrCircuitDlci_Type(Integer32):
    """Custom type wfFrCircuitDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              1007,
              1024,
              64511,
              131072,
              8257535)
        )
    )
    namedValues = NamedValues(
        *(("fourbytemaximum", 8257535),
          ("fourbyteminimum", 131072),
          ("threebytemaximum", 64511),
          ("threebyteminimum", 1024),
          ("twobytemaximum", 1007),
          ("twobyteminimum", 16))
    )


_WfFrCircuitDlci_Type.__name__ = "Integer32"
_WfFrCircuitDlci_Object = MibTableColumn
wfFrCircuitDlci = _WfFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 3),
    _WfFrCircuitDlci_Type()
)
wfFrCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitDlci.setStatus("mandatory")


class _WfFrCircuitState_Type(Integer32):
    """Custom type wfFrCircuitState based on Integer32"""
    defaultValue = 1

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
        *(("active", 2),
          ("control", 5),
          ("inactive", 3),
          ("invalid", 1),
          ("xoff", 4))
    )


_WfFrCircuitState_Type.__name__ = "Integer32"
_WfFrCircuitState_Object = MibTableColumn
wfFrCircuitState = _WfFrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 4),
    _WfFrCircuitState_Type()
)
wfFrCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitState.setStatus("mandatory")


class _WfFrCircuitStateSet_Type(Integer32):
    """Custom type wfFrCircuitStateSet based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_WfFrCircuitStateSet_Type.__name__ = "Integer32"
_WfFrCircuitStateSet_Object = MibTableColumn
wfFrCircuitStateSet = _WfFrCircuitStateSet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 5),
    _WfFrCircuitStateSet_Type()
)
wfFrCircuitStateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitStateSet.setStatus("mandatory")
_WfFrCircuitReceivedFECNs_Type = Counter32
_WfFrCircuitReceivedFECNs_Object = MibTableColumn
wfFrCircuitReceivedFECNs = _WfFrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 6),
    _WfFrCircuitReceivedFECNs_Type()
)
wfFrCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedFECNs.setStatus("mandatory")
_WfFrCircuitReceivedBECNs_Type = Counter32
_WfFrCircuitReceivedBECNs_Object = MibTableColumn
wfFrCircuitReceivedBECNs = _WfFrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 7),
    _WfFrCircuitReceivedBECNs_Type()
)
wfFrCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedBECNs.setStatus("mandatory")
_WfFrCircuitSentFrames_Type = Counter32
_WfFrCircuitSentFrames_Object = MibTableColumn
wfFrCircuitSentFrames = _WfFrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 8),
    _WfFrCircuitSentFrames_Type()
)
wfFrCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitSentFrames.setStatus("mandatory")
_WfFrCircuitSentOctets_Type = Counter32
_WfFrCircuitSentOctets_Object = MibTableColumn
wfFrCircuitSentOctets = _WfFrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 9),
    _WfFrCircuitSentOctets_Type()
)
wfFrCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitSentOctets.setStatus("mandatory")
_WfFrCircuitReceivedFrames_Type = Counter32
_WfFrCircuitReceivedFrames_Object = MibTableColumn
wfFrCircuitReceivedFrames = _WfFrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 10),
    _WfFrCircuitReceivedFrames_Type()
)
wfFrCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedFrames.setStatus("mandatory")
_WfFrCircuitReceivedOctets_Type = Counter32
_WfFrCircuitReceivedOctets_Object = MibTableColumn
wfFrCircuitReceivedOctets = _WfFrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 11),
    _WfFrCircuitReceivedOctets_Type()
)
wfFrCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedOctets.setStatus("mandatory")
_WfFrCircuitCreationTime_Type = TimeTicks
_WfFrCircuitCreationTime_Object = MibTableColumn
wfFrCircuitCreationTime = _WfFrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 12),
    _WfFrCircuitCreationTime_Type()
)
wfFrCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitCreationTime.setStatus("mandatory")
_WfFrCircuitLastTimeChange_Type = TimeTicks
_WfFrCircuitLastTimeChange_Object = MibTableColumn
wfFrCircuitLastTimeChange = _WfFrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 13),
    _WfFrCircuitLastTimeChange_Type()
)
wfFrCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitLastTimeChange.setStatus("mandatory")
_WfFrCircuitCommittedBurst_Type = Integer32
_WfFrCircuitCommittedBurst_Object = MibTableColumn
wfFrCircuitCommittedBurst = _WfFrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 14),
    _WfFrCircuitCommittedBurst_Type()
)
wfFrCircuitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitCommittedBurst.setStatus("mandatory")
_WfFrCircuitExcessBurst_Type = Integer32
_WfFrCircuitExcessBurst_Object = MibTableColumn
wfFrCircuitExcessBurst = _WfFrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 15),
    _WfFrCircuitExcessBurst_Type()
)
wfFrCircuitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitExcessBurst.setStatus("mandatory")
_WfFrCircuitThroughput_Type = Integer32
_WfFrCircuitThroughput_Object = MibTableColumn
wfFrCircuitThroughput = _WfFrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 16),
    _WfFrCircuitThroughput_Type()
)
wfFrCircuitThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitThroughput.setStatus("mandatory")


class _WfFrCircuitMulticast_Type(Integer32):
    """Custom type wfFrCircuitMulticast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2))
    )


_WfFrCircuitMulticast_Type.__name__ = "Integer32"
_WfFrCircuitMulticast_Object = MibTableColumn
wfFrCircuitMulticast = _WfFrCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 17),
    _WfFrCircuitMulticast_Type()
)
wfFrCircuitMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitMulticast.setStatus("mandatory")
_WfFrCircuitDiscards_Type = Counter32
_WfFrCircuitDiscards_Object = MibTableColumn
wfFrCircuitDiscards = _WfFrCircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 18),
    _WfFrCircuitDiscards_Type()
)
wfFrCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitDiscards.setStatus("mandatory")
_WfFrCircuitDrops_Type = Counter32
_WfFrCircuitDrops_Object = MibTableColumn
wfFrCircuitDrops = _WfFrCircuitDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 19),
    _WfFrCircuitDrops_Type()
)
wfFrCircuitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitDrops.setStatus("mandatory")
_WfFrCircuitSubCct_Type = Integer32
_WfFrCircuitSubCct_Object = MibTableColumn
wfFrCircuitSubCct = _WfFrCircuitSubCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 20),
    _WfFrCircuitSubCct_Type()
)
wfFrCircuitSubCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitSubCct.setStatus("mandatory")


class _WfFrCircuitMode_Type(Integer32):
    """Custom type wfFrCircuitMode based on Integer32"""
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
        *(("direct", 3),
          ("group", 1),
          ("hybrid", 2))
    )


_WfFrCircuitMode_Type.__name__ = "Integer32"
_WfFrCircuitMode_Object = MibTableColumn
wfFrCircuitMode = _WfFrCircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 21),
    _WfFrCircuitMode_Type()
)
wfFrCircuitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitMode.setStatus("mandatory")
_WfPppGroup_ObjectIdentity = ObjectIdentity
wfPppGroup = _WfPppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2)
)
_WfSmdsCircuitTable_Object = MibTable
wfSmdsCircuitTable = _WfSmdsCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3)
)
if mibBuilder.loadTexts:
    wfSmdsCircuitTable.setStatus("mandatory")
_WfSmdsCircuitEntry_Object = MibTableRow
wfSmdsCircuitEntry = _WfSmdsCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1)
)
wfSmdsCircuitEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfSmdsCircuitID"),
)
if mibBuilder.loadTexts:
    wfSmdsCircuitEntry.setStatus("mandatory")


class _WfSmdsCircuitDelete_Type(Integer32):
    """Custom type wfSmdsCircuitDelete based on Integer32"""
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


_WfSmdsCircuitDelete_Type.__name__ = "Integer32"
_WfSmdsCircuitDelete_Object = MibTableColumn
wfSmdsCircuitDelete = _WfSmdsCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 1),
    _WfSmdsCircuitDelete_Type()
)
wfSmdsCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDelete.setStatus("mandatory")


class _WfSmdsCircuitDisable_Type(Integer32):
    """Custom type wfSmdsCircuitDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSmdsCircuitDisable_Type.__name__ = "Integer32"
_WfSmdsCircuitDisable_Object = MibTableColumn
wfSmdsCircuitDisable = _WfSmdsCircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 2),
    _WfSmdsCircuitDisable_Type()
)
wfSmdsCircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisable.setStatus("mandatory")


class _WfSmdsCircuitState_Type(Integer32):
    """Custom type wfSmdsCircuitState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfSmdsCircuitState_Type.__name__ = "Integer32"
_WfSmdsCircuitState_Object = MibTableColumn
wfSmdsCircuitState = _WfSmdsCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 3),
    _WfSmdsCircuitState_Type()
)
wfSmdsCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitState.setStatus("mandatory")


class _WfSmdsCircuitID_Type(Integer32):
    """Custom type wfSmdsCircuitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1023),
          ("minimum", 1))
    )


_WfSmdsCircuitID_Type.__name__ = "Integer32"
_WfSmdsCircuitID_Object = MibTableColumn
wfSmdsCircuitID = _WfSmdsCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 4),
    _WfSmdsCircuitID_Type()
)
wfSmdsCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitID.setStatus("mandatory")
_WfSmdsCircuitIndivAddr_Type = OctetString
_WfSmdsCircuitIndivAddr_Object = MibTableColumn
wfSmdsCircuitIndivAddr = _WfSmdsCircuitIndivAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 5),
    _WfSmdsCircuitIndivAddr_Type()
)
wfSmdsCircuitIndivAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitIndivAddr.setStatus("mandatory")
_WfSmdsCircuitGroupAddr_Type = OctetString
_WfSmdsCircuitGroupAddr_Object = MibTableColumn
wfSmdsCircuitGroupAddr = _WfSmdsCircuitGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 6),
    _WfSmdsCircuitGroupAddr_Type()
)
wfSmdsCircuitGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitGroupAddr.setStatus("mandatory")
_WfSmdsCircuitArpAddr_Type = OctetString
_WfSmdsCircuitArpAddr_Object = MibTableColumn
wfSmdsCircuitArpAddr = _WfSmdsCircuitArpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 7),
    _WfSmdsCircuitArpAddr_Type()
)
wfSmdsCircuitArpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitArpAddr.setStatus("mandatory")


class _WfSmdsCircuitDisableHrtbtPoll_Type(Integer32):
    """Custom type wfSmdsCircuitDisableHrtbtPoll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSmdsCircuitDisableHrtbtPoll_Type.__name__ = "Integer32"
_WfSmdsCircuitDisableHrtbtPoll_Object = MibTableColumn
wfSmdsCircuitDisableHrtbtPoll = _WfSmdsCircuitDisableHrtbtPoll_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 8),
    _WfSmdsCircuitDisableHrtbtPoll_Type()
)
wfSmdsCircuitDisableHrtbtPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisableHrtbtPoll.setStatus("mandatory")


class _WfSmdsCircuitHrtbtPollInterval_Type(Integer32):
    """Custom type wfSmdsCircuitHrtbtPollInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("default", 10),
          ("minimum", 6))
    )


_WfSmdsCircuitHrtbtPollInterval_Type.__name__ = "Integer32"
_WfSmdsCircuitHrtbtPollInterval_Object = MibTableColumn
wfSmdsCircuitHrtbtPollInterval = _WfSmdsCircuitHrtbtPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 9),
    _WfSmdsCircuitHrtbtPollInterval_Type()
)
wfSmdsCircuitHrtbtPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitHrtbtPollInterval.setStatus("mandatory")


class _WfSmdsCircuitHrtbtPollDownCount_Type(Integer32):
    """Custom type wfSmdsCircuitHrtbtPollDownCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("minimum", 1))
    )


_WfSmdsCircuitHrtbtPollDownCount_Type.__name__ = "Integer32"
_WfSmdsCircuitHrtbtPollDownCount_Object = MibTableColumn
wfSmdsCircuitHrtbtPollDownCount = _WfSmdsCircuitHrtbtPollDownCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 10),
    _WfSmdsCircuitHrtbtPollDownCount_Type()
)
wfSmdsCircuitHrtbtPollDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitHrtbtPollDownCount.setStatus("mandatory")


class _WfSmdsCircuitDisableNetMgmt_Type(Integer32):
    """Custom type wfSmdsCircuitDisableNetMgmt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfSmdsCircuitDisableNetMgmt_Type.__name__ = "Integer32"
_WfSmdsCircuitDisableNetMgmt_Object = MibTableColumn
wfSmdsCircuitDisableNetMgmt = _WfSmdsCircuitDisableNetMgmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 11),
    _WfSmdsCircuitDisableNetMgmt_Type()
)
wfSmdsCircuitDisableNetMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisableNetMgmt.setStatus("mandatory")
_WfSmdsCircuitSipL3ReceivedIndividualDAs_Type = Counter32
_WfSmdsCircuitSipL3ReceivedIndividualDAs_Object = MibTableColumn
wfSmdsCircuitSipL3ReceivedIndividualDAs = _WfSmdsCircuitSipL3ReceivedIndividualDAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 12),
    _WfSmdsCircuitSipL3ReceivedIndividualDAs_Type()
)
wfSmdsCircuitSipL3ReceivedIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3ReceivedIndividualDAs.setStatus("mandatory")
_WfSmdsCircuitSipL3ReceivedGAs_Type = Counter32
_WfSmdsCircuitSipL3ReceivedGAs_Object = MibTableColumn
wfSmdsCircuitSipL3ReceivedGAs = _WfSmdsCircuitSipL3ReceivedGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 13),
    _WfSmdsCircuitSipL3ReceivedGAs_Type()
)
wfSmdsCircuitSipL3ReceivedGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3ReceivedGAs.setStatus("mandatory")
_WfSmdsCircuitSipL3SentIndividualDAs_Type = Counter32
_WfSmdsCircuitSipL3SentIndividualDAs_Object = MibTableColumn
wfSmdsCircuitSipL3SentIndividualDAs = _WfSmdsCircuitSipL3SentIndividualDAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 14),
    _WfSmdsCircuitSipL3SentIndividualDAs_Type()
)
wfSmdsCircuitSipL3SentIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3SentIndividualDAs.setStatus("mandatory")
_WfSmdsCircuitSipL3SentGAs_Type = Counter32
_WfSmdsCircuitSipL3SentGAs_Object = MibTableColumn
wfSmdsCircuitSipL3SentGAs = _WfSmdsCircuitSipL3SentGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 15),
    _WfSmdsCircuitSipL3SentGAs_Type()
)
wfSmdsCircuitSipL3SentGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3SentGAs.setStatus("mandatory")


class _WfSmdsCircuitSipL3VersionSupport_Type(Integer32):
    """Custom type wfSmdsCircuitSipL3VersionSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version", 1)
    )


_WfSmdsCircuitSipL3VersionSupport_Type.__name__ = "Integer32"
_WfSmdsCircuitSipL3VersionSupport_Object = MibTableColumn
wfSmdsCircuitSipL3VersionSupport = _WfSmdsCircuitSipL3VersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 16),
    _WfSmdsCircuitSipL3VersionSupport_Type()
)
wfSmdsCircuitSipL3VersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3VersionSupport.setStatus("mandatory")
_WfX25Group_ObjectIdentity = ObjectIdentity
wfX25Group = _WfX25Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4)
)
_WfAtmGroup_ObjectIdentity = ObjectIdentity
wfAtmGroup = _WfAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5)
)
_WfXnsGroup_ObjectIdentity = ObjectIdentity
wfXnsGroup = _WfXnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10)
)
_WfXnsBase_ObjectIdentity = ObjectIdentity
wfXnsBase = _WfXnsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1)
)


class _WfXnsBaseDelete_Type(Integer32):
    """Custom type wfXnsBaseDelete based on Integer32"""
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


_WfXnsBaseDelete_Type.__name__ = "Integer32"
_WfXnsBaseDelete_Object = MibScalar
wfXnsBaseDelete = _WfXnsBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 1),
    _WfXnsBaseDelete_Type()
)
wfXnsBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseDelete.setStatus("mandatory")


class _WfXnsBaseDisable_Type(Integer32):
    """Custom type wfXnsBaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsBaseDisable_Type.__name__ = "Integer32"
_WfXnsBaseDisable_Object = MibScalar
wfXnsBaseDisable = _WfXnsBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 2),
    _WfXnsBaseDisable_Type()
)
wfXnsBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseDisable.setStatus("mandatory")


class _WfXnsBaseState_Type(Integer32):
    """Custom type wfXnsBaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfXnsBaseState_Type.__name__ = "Integer32"
_WfXnsBaseState_Object = MibScalar
wfXnsBaseState = _WfXnsBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 3),
    _WfXnsBaseState_Type()
)
wfXnsBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseState.setStatus("mandatory")
_WfXnsBaseHostNumber_Type = OctetString
_WfXnsBaseHostNumber_Object = MibScalar
wfXnsBaseHostNumber = _WfXnsBaseHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 1, 4),
    _WfXnsBaseHostNumber_Type()
)
wfXnsBaseHostNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsBaseHostNumber.setStatus("mandatory")
_WfXnsBaseRtEntryTable_Object = MibTable
wfXnsBaseRtEntryTable = _WfXnsBaseRtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2)
)
if mibBuilder.loadTexts:
    wfXnsBaseRtEntryTable.setStatus("mandatory")
_WfXnsBaseRtEntry_Object = MibTableRow
wfXnsBaseRtEntry = _WfXnsBaseRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1)
)
wfXnsBaseRtEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfXnsBaseRouteDest"),
)
if mibBuilder.loadTexts:
    wfXnsBaseRtEntry.setStatus("mandatory")
_WfXnsBaseRouteDest_Type = OctetString
_WfXnsBaseRouteDest_Object = MibTableColumn
wfXnsBaseRouteDest = _WfXnsBaseRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 1),
    _WfXnsBaseRouteDest_Type()
)
wfXnsBaseRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteDest.setStatus("mandatory")
_WfXnsBaseRouteIfIndex_Type = Integer32
_WfXnsBaseRouteIfIndex_Object = MibTableColumn
wfXnsBaseRouteIfIndex = _WfXnsBaseRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 2),
    _WfXnsBaseRouteIfIndex_Type()
)
wfXnsBaseRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteIfIndex.setStatus("mandatory")
_WfXnsBaseRouteMetric_Type = Integer32
_WfXnsBaseRouteMetric_Object = MibTableColumn
wfXnsBaseRouteMetric = _WfXnsBaseRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 3),
    _WfXnsBaseRouteMetric_Type()
)
wfXnsBaseRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteMetric.setStatus("mandatory")
_WfXnsBaseRouteNextHopNetwork_Type = OctetString
_WfXnsBaseRouteNextHopNetwork_Object = MibTableColumn
wfXnsBaseRouteNextHopNetwork = _WfXnsBaseRouteNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 4),
    _WfXnsBaseRouteNextHopNetwork_Type()
)
wfXnsBaseRouteNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteNextHopNetwork.setStatus("mandatory")
_WfXnsBaseRouteNextHopHost_Type = OctetString
_WfXnsBaseRouteNextHopHost_Object = MibTableColumn
wfXnsBaseRouteNextHopHost = _WfXnsBaseRouteNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 5),
    _WfXnsBaseRouteNextHopHost_Type()
)
wfXnsBaseRouteNextHopHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteNextHopHost.setStatus("mandatory")


class _WfXnsBaseRouteType_Type(Integer32):
    """Custom type wfXnsBaseRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1),
          ("static", 5))
    )


_WfXnsBaseRouteType_Type.__name__ = "Integer32"
_WfXnsBaseRouteType_Object = MibTableColumn
wfXnsBaseRouteType = _WfXnsBaseRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 6),
    _WfXnsBaseRouteType_Type()
)
wfXnsBaseRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteType.setStatus("mandatory")


class _WfXnsBaseRouteProto_Type(Integer32):
    """Custom type wfXnsBaseRouteProto based on Integer32"""
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
        *(("local", 2),
          ("netmgmt", 3),
          ("other", 1),
          ("rip", 4))
    )


_WfXnsBaseRouteProto_Type.__name__ = "Integer32"
_WfXnsBaseRouteProto_Object = MibTableColumn
wfXnsBaseRouteProto = _WfXnsBaseRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 7),
    _WfXnsBaseRouteProto_Type()
)
wfXnsBaseRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteProto.setStatus("mandatory")
_WfXnsBaseRouteAge_Type = Integer32
_WfXnsBaseRouteAge_Object = MibTableColumn
wfXnsBaseRouteAge = _WfXnsBaseRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 8),
    _WfXnsBaseRouteAge_Type()
)
wfXnsBaseRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteAge.setStatus("mandatory")
_WfXnsBaseRouteInfo_Type = OctetString
_WfXnsBaseRouteInfo_Object = MibTableColumn
wfXnsBaseRouteInfo = _WfXnsBaseRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 2, 1, 9),
    _WfXnsBaseRouteInfo_Type()
)
wfXnsBaseRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsBaseRouteInfo.setStatus("mandatory")
_WfXnsInterfaceTable_Object = MibTable
wfXnsInterfaceTable = _WfXnsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3)
)
if mibBuilder.loadTexts:
    wfXnsInterfaceTable.setStatus("mandatory")
_WfXnsInterfaceEntry_Object = MibTableRow
wfXnsInterfaceEntry = _WfXnsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1)
)
wfXnsInterfaceEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfXnsInterfaceNetworkNumber"),
    (0, "Wellfleet-Series7-MIB", "wfXnsInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfXnsInterfaceEntry.setStatus("mandatory")
_WfXnsInterfaceIndex_Type = Integer32
_WfXnsInterfaceIndex_Object = MibTableColumn
wfXnsInterfaceIndex = _WfXnsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 1),
    _WfXnsInterfaceIndex_Type()
)
wfXnsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceIndex.setStatus("mandatory")


class _WfXnsInterfaceDelete_Type(Integer32):
    """Custom type wfXnsInterfaceDelete based on Integer32"""
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


_WfXnsInterfaceDelete_Type.__name__ = "Integer32"
_WfXnsInterfaceDelete_Object = MibTableColumn
wfXnsInterfaceDelete = _WfXnsInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 2),
    _WfXnsInterfaceDelete_Type()
)
wfXnsInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceDelete.setStatus("mandatory")


class _WfXnsInterfaceDisable_Type(Integer32):
    """Custom type wfXnsInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsInterfaceDisable_Type.__name__ = "Integer32"
_WfXnsInterfaceDisable_Object = MibTableColumn
wfXnsInterfaceDisable = _WfXnsInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 3),
    _WfXnsInterfaceDisable_Type()
)
wfXnsInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceDisable.setStatus("mandatory")


class _WfXnsInterfaceState_Type(Integer32):
    """Custom type wfXnsInterfaceState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfXnsInterfaceState_Type.__name__ = "Integer32"
_WfXnsInterfaceState_Object = MibTableColumn
wfXnsInterfaceState = _WfXnsInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 4),
    _WfXnsInterfaceState_Type()
)
wfXnsInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceState.setStatus("mandatory")
_WfXnsInterfaceCircuit_Type = Integer32
_WfXnsInterfaceCircuit_Object = MibTableColumn
wfXnsInterfaceCircuit = _WfXnsInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 5),
    _WfXnsInterfaceCircuit_Type()
)
wfXnsInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceCircuit.setStatus("mandatory")
_WfXnsInterfaceNetworkNumber_Type = OctetString
_WfXnsInterfaceNetworkNumber_Object = MibTableColumn
wfXnsInterfaceNetworkNumber = _WfXnsInterfaceNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 6),
    _WfXnsInterfaceNetworkNumber_Type()
)
wfXnsInterfaceNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceNetworkNumber.setStatus("mandatory")
_WfXnsInterfaceCost_Type = Integer32
_WfXnsInterfaceCost_Object = MibTableColumn
wfXnsInterfaceCost = _WfXnsInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 7),
    _WfXnsInterfaceCost_Type()
)
wfXnsInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceCost.setStatus("mandatory")


class _WfXnsInterfaceXsumOn_Type(Integer32):
    """Custom type wfXnsInterfaceXsumOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsInterfaceXsumOn_Type.__name__ = "Integer32"
_WfXnsInterfaceXsumOn_Object = MibTableColumn
wfXnsInterfaceXsumOn = _WfXnsInterfaceXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 8),
    _WfXnsInterfaceXsumOn_Type()
)
wfXnsInterfaceXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceXsumOn.setStatus("mandatory")


class _WfXnsInterfaceEncaps_Type(Integer32):
    """Custom type wfXnsInterfaceEncaps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("snap", 2))
    )


_WfXnsInterfaceEncaps_Type.__name__ = "Integer32"
_WfXnsInterfaceEncaps_Object = MibTableColumn
wfXnsInterfaceEncaps = _WfXnsInterfaceEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 9),
    _WfXnsInterfaceEncaps_Type()
)
wfXnsInterfaceEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceEncaps.setStatus("mandatory")
_WfXnsInterfaceMacAddress_Type = OctetString
_WfXnsInterfaceMacAddress_Object = MibTableColumn
wfXnsInterfaceMacAddress = _WfXnsInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 10),
    _WfXnsInterfaceMacAddress_Type()
)
wfXnsInterfaceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceMacAddress.setStatus("mandatory")
_WfXnsInterfaceSMDSGroupAddress_Type = OctetString
_WfXnsInterfaceSMDSGroupAddress_Object = MibTableColumn
wfXnsInterfaceSMDSGroupAddress = _WfXnsInterfaceSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 11),
    _WfXnsInterfaceSMDSGroupAddress_Type()
)
wfXnsInterfaceSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceSMDSGroupAddress.setStatus("mandatory")
_WfXnsInterfaceMaxInfo_Type = Integer32
_WfXnsInterfaceMaxInfo_Object = MibTableColumn
wfXnsInterfaceMaxInfo = _WfXnsInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 12),
    _WfXnsInterfaceMaxInfo_Type()
)
wfXnsInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceMaxInfo.setStatus("mandatory")


class _WfXnsInterfaceExtServer_Type(Integer32):
    """Custom type wfXnsInterfaceExtServer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsInterfaceExtServer_Type.__name__ = "Integer32"
_WfXnsInterfaceExtServer_Object = MibTableColumn
wfXnsInterfaceExtServer = _WfXnsInterfaceExtServer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 13),
    _WfXnsInterfaceExtServer_Type()
)
wfXnsInterfaceExtServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExtServer.setStatus("mandatory")
_WfXnsInterfaceExServNetwork_Type = OctetString
_WfXnsInterfaceExServNetwork_Object = MibTableColumn
wfXnsInterfaceExServNetwork = _WfXnsInterfaceExServNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 14),
    _WfXnsInterfaceExServNetwork_Type()
)
wfXnsInterfaceExServNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServNetwork.setStatus("mandatory")
_WfXnsInterfaceExServHostId_Type = OctetString
_WfXnsInterfaceExServHostId_Object = MibTableColumn
wfXnsInterfaceExServHostId = _WfXnsInterfaceExServHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 15),
    _WfXnsInterfaceExServHostId_Type()
)
wfXnsInterfaceExServHostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServHostId.setStatus("mandatory")
_WfXnsInterfaceExServPktType_Type = OctetString
_WfXnsInterfaceExServPktType_Object = MibTableColumn
wfXnsInterfaceExServPktType = _WfXnsInterfaceExServPktType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 16),
    _WfXnsInterfaceExServPktType_Type()
)
wfXnsInterfaceExServPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServPktType.setStatus("mandatory")
_WfXnsInterfaceExServSockNm_Type = OctetString
_WfXnsInterfaceExServSockNm_Object = MibTableColumn
wfXnsInterfaceExServSockNm = _WfXnsInterfaceExServSockNm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 17),
    _WfXnsInterfaceExServSockNm_Type()
)
wfXnsInterfaceExServSockNm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceExServSockNm.setStatus("mandatory")
_WfXnsInterfaceInReceives_Type = Counter32
_WfXnsInterfaceInReceives_Object = MibTableColumn
wfXnsInterfaceInReceives = _WfXnsInterfaceInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 18),
    _WfXnsInterfaceInReceives_Type()
)
wfXnsInterfaceInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInReceives.setStatus("mandatory")
_WfXnsInterfaceInHdrErrors_Type = Counter32
_WfXnsInterfaceInHdrErrors_Object = MibTableColumn
wfXnsInterfaceInHdrErrors = _WfXnsInterfaceInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 19),
    _WfXnsInterfaceInHdrErrors_Type()
)
wfXnsInterfaceInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInHdrErrors.setStatus("mandatory")
_WfXnsInterfaceInAddrErrors_Type = Counter32
_WfXnsInterfaceInAddrErrors_Object = MibTableColumn
wfXnsInterfaceInAddrErrors = _WfXnsInterfaceInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 20),
    _WfXnsInterfaceInAddrErrors_Type()
)
wfXnsInterfaceInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInAddrErrors.setStatus("mandatory")
_WfXnsInterfaceForwDatagrams_Type = Counter32
_WfXnsInterfaceForwDatagrams_Object = MibTableColumn
wfXnsInterfaceForwDatagrams = _WfXnsInterfaceForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 21),
    _WfXnsInterfaceForwDatagrams_Type()
)
wfXnsInterfaceForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceForwDatagrams.setStatus("mandatory")
_WfXnsInterfaceInUnknownProtos_Type = Counter32
_WfXnsInterfaceInUnknownProtos_Object = MibTableColumn
wfXnsInterfaceInUnknownProtos = _WfXnsInterfaceInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 22),
    _WfXnsInterfaceInUnknownProtos_Type()
)
wfXnsInterfaceInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInUnknownProtos.setStatus("mandatory")
_WfXnsInterfaceInDiscards_Type = Counter32
_WfXnsInterfaceInDiscards_Object = MibTableColumn
wfXnsInterfaceInDiscards = _WfXnsInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 23),
    _WfXnsInterfaceInDiscards_Type()
)
wfXnsInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInDiscards.setStatus("mandatory")
_WfXnsInterfaceInDelivers_Type = Counter32
_WfXnsInterfaceInDelivers_Object = MibTableColumn
wfXnsInterfaceInDelivers = _WfXnsInterfaceInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 24),
    _WfXnsInterfaceInDelivers_Type()
)
wfXnsInterfaceInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceInDelivers.setStatus("mandatory")
_WfXnsInterfaceOutRequests_Type = Counter32
_WfXnsInterfaceOutRequests_Object = MibTableColumn
wfXnsInterfaceOutRequests = _WfXnsInterfaceOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 25),
    _WfXnsInterfaceOutRequests_Type()
)
wfXnsInterfaceOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceOutRequests.setStatus("mandatory")
_WfXnsInterfaceOutDiscards_Type = Counter32
_WfXnsInterfaceOutDiscards_Object = MibTableColumn
wfXnsInterfaceOutDiscards = _WfXnsInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 26),
    _WfXnsInterfaceOutDiscards_Type()
)
wfXnsInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceOutDiscards.setStatus("mandatory")
_WfXnsInterfaceOutNoRoutes_Type = Counter32
_WfXnsInterfaceOutNoRoutes_Object = MibTableColumn
wfXnsInterfaceOutNoRoutes = _WfXnsInterfaceOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 27),
    _WfXnsInterfaceOutNoRoutes_Type()
)
wfXnsInterfaceOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsInterfaceOutNoRoutes.setStatus("mandatory")
_WfXnsInterfaceFRBcast_Type = OctetString
_WfXnsInterfaceFRBcast_Object = MibTableColumn
wfXnsInterfaceFRBcast = _WfXnsInterfaceFRBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 28),
    _WfXnsInterfaceFRBcast_Type()
)
wfXnsInterfaceFRBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceFRBcast.setStatus("mandatory")
_WfXnsInterfaceFRMcast_Type = OctetString
_WfXnsInterfaceFRMcast_Object = MibTableColumn
wfXnsInterfaceFRMcast = _WfXnsInterfaceFRMcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 3, 1, 29),
    _WfXnsInterfaceFRMcast_Type()
)
wfXnsInterfaceFRMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsInterfaceFRMcast.setStatus("mandatory")
_WfXnsRipIntfTable_Object = MibTable
wfXnsRipIntfTable = _WfXnsRipIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4)
)
if mibBuilder.loadTexts:
    wfXnsRipIntfTable.setStatus("mandatory")
_WfXnsRipIntfEntry_Object = MibTableRow
wfXnsRipIntfEntry = _WfXnsRipIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1)
)
wfXnsRipIntfEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfXnsRipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfXnsRipIntfEntry.setStatus("mandatory")


class _WfXnsRipInterfaceDelete_Type(Integer32):
    """Custom type wfXnsRipInterfaceDelete based on Integer32"""
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


_WfXnsRipInterfaceDelete_Type.__name__ = "Integer32"
_WfXnsRipInterfaceDelete_Object = MibTableColumn
wfXnsRipInterfaceDelete = _WfXnsRipInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 1),
    _WfXnsRipInterfaceDelete_Type()
)
wfXnsRipInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceDelete.setStatus("mandatory")


class _WfXnsRipInterfaceDisable_Type(Integer32):
    """Custom type wfXnsRipInterfaceDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsRipInterfaceDisable_Type.__name__ = "Integer32"
_WfXnsRipInterfaceDisable_Object = MibTableColumn
wfXnsRipInterfaceDisable = _WfXnsRipInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 2),
    _WfXnsRipInterfaceDisable_Type()
)
wfXnsRipInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceDisable.setStatus("mandatory")


class _WfXnsRipInterfaceState_Type(Integer32):
    """Custom type wfXnsRipInterfaceState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfXnsRipInterfaceState_Type.__name__ = "Integer32"
_WfXnsRipInterfaceState_Object = MibTableColumn
wfXnsRipInterfaceState = _WfXnsRipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 3),
    _WfXnsRipInterfaceState_Type()
)
wfXnsRipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceState.setStatus("mandatory")
_WfXnsRipInterfaceIndex_Type = OctetString
_WfXnsRipInterfaceIndex_Object = MibTableColumn
wfXnsRipInterfaceIndex = _WfXnsRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 4),
    _WfXnsRipInterfaceIndex_Type()
)
wfXnsRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceIndex.setStatus("mandatory")


class _WfXnsRipInterfaceSupply_Type(Integer32):
    """Custom type wfXnsRipInterfaceSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsRipInterfaceSupply_Type.__name__ = "Integer32"
_WfXnsRipInterfaceSupply_Object = MibTableColumn
wfXnsRipInterfaceSupply = _WfXnsRipInterfaceSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 5),
    _WfXnsRipInterfaceSupply_Type()
)
wfXnsRipInterfaceSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceSupply.setStatus("mandatory")


class _WfXnsRipInterfaceListen_Type(Integer32):
    """Custom type wfXnsRipInterfaceListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsRipInterfaceListen_Type.__name__ = "Integer32"
_WfXnsRipInterfaceListen_Object = MibTableColumn
wfXnsRipInterfaceListen = _WfXnsRipInterfaceListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 4, 1, 6),
    _WfXnsRipInterfaceListen_Type()
)
wfXnsRipInterfaceListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsRipInterfaceListen.setStatus("mandatory")
_WfXnsAdjacentHostTable_Object = MibTable
wfXnsAdjacentHostTable = _WfXnsAdjacentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5)
)
if mibBuilder.loadTexts:
    wfXnsAdjacentHostTable.setStatus("mandatory")
_WfXnsAdjacentHostEntry_Object = MibTableRow
wfXnsAdjacentHostEntry = _WfXnsAdjacentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1)
)
wfXnsAdjacentHostEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfXnsAhTargHostNetwork"),
    (0, "Wellfleet-Series7-MIB", "wfXnsAhTargHostId"),
)
if mibBuilder.loadTexts:
    wfXnsAdjacentHostEntry.setStatus("mandatory")


class _WfXnsAhDelete_Type(Integer32):
    """Custom type wfXnsAhDelete based on Integer32"""
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


_WfXnsAhDelete_Type.__name__ = "Integer32"
_WfXnsAhDelete_Object = MibTableColumn
wfXnsAhDelete = _WfXnsAhDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 1),
    _WfXnsAhDelete_Type()
)
wfXnsAhDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhDelete.setStatus("mandatory")


class _WfXnsAhDisable_Type(Integer32):
    """Custom type wfXnsAhDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsAhDisable_Type.__name__ = "Integer32"
_WfXnsAhDisable_Object = MibTableColumn
wfXnsAhDisable = _WfXnsAhDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 2),
    _WfXnsAhDisable_Type()
)
wfXnsAhDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhDisable.setStatus("mandatory")
_WfXnsAhTargHostNetwork_Type = OctetString
_WfXnsAhTargHostNetwork_Object = MibTableColumn
wfXnsAhTargHostNetwork = _WfXnsAhTargHostNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 3),
    _WfXnsAhTargHostNetwork_Type()
)
wfXnsAhTargHostNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAhTargHostNetwork.setStatus("mandatory")
_WfXnsAhTargHostId_Type = OctetString
_WfXnsAhTargHostId_Object = MibTableColumn
wfXnsAhTargHostId = _WfXnsAhTargHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 4),
    _WfXnsAhTargHostId_Type()
)
wfXnsAhTargHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsAhTargHostId.setStatus("mandatory")
_WfXnsAhNextHopIntf_Type = OctetString
_WfXnsAhNextHopIntf_Object = MibTableColumn
wfXnsAhNextHopIntf = _WfXnsAhNextHopIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 5),
    _WfXnsAhNextHopIntf_Type()
)
wfXnsAhNextHopIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhNextHopIntf.setStatus("mandatory")
_WfXnsAhDlci_Type = OctetString
_WfXnsAhDlci_Object = MibTableColumn
wfXnsAhDlci = _WfXnsAhDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 5, 1, 6),
    _WfXnsAhDlci_Type()
)
wfXnsAhDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsAhDlci.setStatus("mandatory")
_WfXnsStaticRouteTable_Object = MibTable
wfXnsStaticRouteTable = _WfXnsStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6)
)
if mibBuilder.loadTexts:
    wfXnsStaticRouteTable.setStatus("mandatory")
_WfXnsStaticRouteEntry_Object = MibTableRow
wfXnsStaticRouteEntry = _WfXnsStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1)
)
wfXnsStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfXnsSrTargNetwork"),
    (0, "Wellfleet-Series7-MIB", "wfXnsSrNextHopNetwork"),
)
if mibBuilder.loadTexts:
    wfXnsStaticRouteEntry.setStatus("mandatory")


class _WfXnsSrDelete_Type(Integer32):
    """Custom type wfXnsSrDelete based on Integer32"""
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


_WfXnsSrDelete_Type.__name__ = "Integer32"
_WfXnsSrDelete_Object = MibTableColumn
wfXnsSrDelete = _WfXnsSrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 1),
    _WfXnsSrDelete_Type()
)
wfXnsSrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrDelete.setStatus("mandatory")


class _WfXnsSrDisable_Type(Integer32):
    """Custom type wfXnsSrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsSrDisable_Type.__name__ = "Integer32"
_WfXnsSrDisable_Object = MibTableColumn
wfXnsSrDisable = _WfXnsSrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 2),
    _WfXnsSrDisable_Type()
)
wfXnsSrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrDisable.setStatus("mandatory")
_WfXnsSrTargNetwork_Type = OctetString
_WfXnsSrTargNetwork_Object = MibTableColumn
wfXnsSrTargNetwork = _WfXnsSrTargNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 3),
    _WfXnsSrTargNetwork_Type()
)
wfXnsSrTargNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsSrTargNetwork.setStatus("mandatory")
_WfXnsSrCost_Type = Integer32
_WfXnsSrCost_Object = MibTableColumn
wfXnsSrCost = _WfXnsSrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 4),
    _WfXnsSrCost_Type()
)
wfXnsSrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrCost.setStatus("mandatory")
_WfXnsSrNextHopNetwork_Type = OctetString
_WfXnsSrNextHopNetwork_Object = MibTableColumn
wfXnsSrNextHopNetwork = _WfXnsSrNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 5),
    _WfXnsSrNextHopNetwork_Type()
)
wfXnsSrNextHopNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsSrNextHopNetwork.setStatus("mandatory")
_WfXnsSrNextHopHost_Type = OctetString
_WfXnsSrNextHopHost_Object = MibTableColumn
wfXnsSrNextHopHost = _WfXnsSrNextHopHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 6),
    _WfXnsSrNextHopHost_Type()
)
wfXnsSrNextHopHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsSrNextHopHost.setStatus("mandatory")
_WfXnsSrTargNetworkRt_Type = Integer32
_WfXnsSrTargNetworkRt_Object = MibTableColumn
wfXnsSrTargNetworkRt = _WfXnsSrTargNetworkRt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 6, 1, 7),
    _WfXnsSrTargNetworkRt_Type()
)
wfXnsSrTargNetworkRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsSrTargNetworkRt.setStatus("mandatory")
_WfXnsTrafficFilterTable_Object = MibTable
wfXnsTrafficFilterTable = _WfXnsTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7)
)
if mibBuilder.loadTexts:
    wfXnsTrafficFilterTable.setStatus("mandatory")
_WfXnsTrafficFilterEntry_Object = MibTableRow
wfXnsTrafficFilterEntry = _WfXnsTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1)
)
wfXnsTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-Series7-MIB", "wfXnsTrafficFilterInterface"),
    (0, "Wellfleet-Series7-MIB", "wfXnsTrafficFilterCircuit"),
    (0, "Wellfleet-Series7-MIB", "wfXnsTrafficFilterRuleNumber"),
    (0, "Wellfleet-Series7-MIB", "wfXnsTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfXnsTrafficFilterEntry.setStatus("mandatory")


class _WfXnsTrafficFilterCreate_Type(Integer32):
    """Custom type wfXnsTrafficFilterCreate based on Integer32"""
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


_WfXnsTrafficFilterCreate_Type.__name__ = "Integer32"
_WfXnsTrafficFilterCreate_Object = MibTableColumn
wfXnsTrafficFilterCreate = _WfXnsTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 1),
    _WfXnsTrafficFilterCreate_Type()
)
wfXnsTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterCreate.setStatus("mandatory")


class _WfXnsTrafficFilterEnable_Type(Integer32):
    """Custom type wfXnsTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfXnsTrafficFilterEnable_Type.__name__ = "Integer32"
_WfXnsTrafficFilterEnable_Object = MibTableColumn
wfXnsTrafficFilterEnable = _WfXnsTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 2),
    _WfXnsTrafficFilterEnable_Type()
)
wfXnsTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterEnable.setStatus("mandatory")


class _WfXnsTrafficFilterStatus_Type(Integer32):
    """Custom type wfXnsTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfXnsTrafficFilterStatus_Type.__name__ = "Integer32"
_WfXnsTrafficFilterStatus_Object = MibTableColumn
wfXnsTrafficFilterStatus = _WfXnsTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 3),
    _WfXnsTrafficFilterStatus_Type()
)
wfXnsTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterStatus.setStatus("mandatory")
_WfXnsTrafficFilterCounter_Type = Counter32
_WfXnsTrafficFilterCounter_Object = MibTableColumn
wfXnsTrafficFilterCounter = _WfXnsTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 4),
    _WfXnsTrafficFilterCounter_Type()
)
wfXnsTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterCounter.setStatus("mandatory")
_WfXnsTrafficFilterDefinition_Type = Opaque
_WfXnsTrafficFilterDefinition_Object = MibTableColumn
wfXnsTrafficFilterDefinition = _WfXnsTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 5),
    _WfXnsTrafficFilterDefinition_Type()
)
wfXnsTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterDefinition.setStatus("mandatory")
_WfXnsTrafficFilterReserved_Type = Integer32
_WfXnsTrafficFilterReserved_Object = MibTableColumn
wfXnsTrafficFilterReserved = _WfXnsTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 6),
    _WfXnsTrafficFilterReserved_Type()
)
wfXnsTrafficFilterReserved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterReserved.setStatus("mandatory")
_WfXnsTrafficFilterInterface_Type = OctetString
_WfXnsTrafficFilterInterface_Object = MibTableColumn
wfXnsTrafficFilterInterface = _WfXnsTrafficFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 7),
    _WfXnsTrafficFilterInterface_Type()
)
wfXnsTrafficFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterInterface.setStatus("mandatory")
_WfXnsTrafficFilterCircuit_Type = Integer32
_WfXnsTrafficFilterCircuit_Object = MibTableColumn
wfXnsTrafficFilterCircuit = _WfXnsTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 8),
    _WfXnsTrafficFilterCircuit_Type()
)
wfXnsTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterCircuit.setStatus("mandatory")
_WfXnsTrafficFilterRuleNumber_Type = Integer32
_WfXnsTrafficFilterRuleNumber_Object = MibTableColumn
wfXnsTrafficFilterRuleNumber = _WfXnsTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 9),
    _WfXnsTrafficFilterRuleNumber_Type()
)
wfXnsTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterRuleNumber.setStatus("mandatory")
_WfXnsTrafficFilterFragment_Type = Integer32
_WfXnsTrafficFilterFragment_Object = MibTableColumn
wfXnsTrafficFilterFragment = _WfXnsTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10, 7, 1, 10),
    _WfXnsTrafficFilterFragment_Type()
)
wfXnsTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfXnsTrafficFilterFragment.setStatus("mandatory")
_WfTestGroup_ObjectIdentity = ObjectIdentity
wfTestGroup = _WfTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-Series7-MIB",
    **{"wellfleet": wellfleet,
       "wfSwSeries7": wfSwSeries7,
       "wfHardwareConfig": wfHardwareConfig,
       "wfHwBase": wfHwBase,
       "wfHwBpIdOpt": wfHwBpIdOpt,
       "wfHwBpRev": wfHwBpRev,
       "wfHwBpSerialNumber": wfHwBpSerialNumber,
       "wfBCNPwrSupply1": wfBCNPwrSupply1,
       "wfBCNPwrSupply2": wfBCNPwrSupply2,
       "wfBCNPwrSupply3": wfBCNPwrSupply3,
       "wfBCNPwrSupply4": wfBCNPwrSupply4,
       "wfBCNFanStatus": wfBCNFanStatus,
       "wfBCNTemperature": wfBCNTemperature,
       "wfHwTable": wfHwTable,
       "wfHwEntry": wfHwEntry,
       "wfHwSlot": wfHwSlot,
       "wfHwModIdOpt": wfHwModIdOpt,
       "wfHwModRev": wfHwModRev,
       "wfHwModSerialNumber": wfHwModSerialNumber,
       "wfHwMotherBdIdOpt": wfHwMotherBdIdOpt,
       "wfHwMotherBdRev": wfHwMotherBdRev,
       "wfHwMotherBdSerialNumber": wfHwMotherBdSerialNumber,
       "wfHwDaughterBdIdOpt": wfHwDaughterBdIdOpt,
       "wfHwDaughterBdRev": wfHwDaughterBdRev,
       "wfHwDaughterBdSerialNumber": wfHwDaughterBdSerialNumber,
       "wfHwBabyBdIdOpt": wfHwBabyBdIdOpt,
       "wfHwBabyBdRev": wfHwBabyBdRev,
       "wfHwBabyBdSerialNumber": wfHwBabyBdSerialNumber,
       "wfHwDiagPromRev": wfHwDiagPromRev,
       "wfHwDiagPromDate": wfHwDiagPromDate,
       "wfHwDiagPromSource": wfHwDiagPromSource,
       "wfHwBootPromRev": wfHwBootPromRev,
       "wfHwBootPromDate": wfHwBootPromDate,
       "wfHwBootPromSource": wfHwBootPromSource,
       "wfHwSparePromRev": wfHwSparePromRev,
       "wfHwSparePromDate": wfHwSparePromDate,
       "wfHwSparePromSource": wfHwSparePromSource,
       "wfHwFileSysPresent": wfHwFileSysPresent,
       "wfMod": wfMod,
       "wfModState": wfModState,
       "wfModSlot": wfModSlot,
       "wfModIdOpt": wfModIdOpt,
       "wfModRev": wfModRev,
       "wfModProm": wfModProm,
       "wfModMidr": wfModMidr,
       "wfModMled": wfModMled,
       "wfModMisr": wfModMisr,
       "wfModSnprom": wfModSnprom,
       "wfModMadr1": wfModMadr1,
       "wfModMadr2": wfModMadr2,
       "wfModMadr3": wfModMadr3,
       "wfModMadr4": wfModMadr4,
       "wfModLance1": wfModLance1,
       "wfModLance2": wfModLance2,
       "wfModMk50251": wfModMk50251,
       "wfModMk50252": wfModMk50252,
       "wfModMk50253": wfModMk50253,
       "wfModMk50254": wfModMk50254,
       "wfModSicr": wfModSicr,
       "wfModSbrr": wfModSbrr,
       "wfMod8530": wfMod8530,
       "wfModCar": wfModCar,
       "wfModDefaA": wfModDefaA,
       "wfModCamALock": wfModCamALock,
       "wfModCamAUnlock": wfModCamAUnlock,
       "wfModDefaB": wfModDefaB,
       "wfModCamBLock": wfModCamBLock,
       "wfModCamBUnlock": wfModCamBUnlock,
       "wfModIlacc1": wfModIlacc1,
       "wfModIlacc2": wfModIlacc2,
       "wfModIlacc3": wfModIlacc3,
       "wfModIlacc4": wfModIlacc4,
       "wfModTms3801": wfModTms3801,
       "wfModTms3802": wfModTms3802,
       "wfModTocr": wfModTocr,
       "wfModTsra": wfModTsra,
       "wfModMuxram1": wfModMuxram1,
       "wfModMuxram2": wfModMuxram2,
       "wfModTicr": wfModTicr,
       "wfModFramer1": wfModFramer1,
       "wfModFramer2": wfModFramer2,
       "wfModFsi1": wfModFsi1,
       "wfModMac1": wfModMac1,
       "wfModElmA1": wfModElmA1,
       "wfModElmB1": wfModElmB1,
       "wfModMcr1": wfModMcr1,
       "wfModHssiFsi1": wfModHssiFsi1,
       "wfModHssiFsi2": wfModHssiFsi2,
       "wfModHssiUga1": wfModHssiUga1,
       "wfModHssiUga2": wfModHssiUga2,
       "wfModHicr": wfModHicr,
       "wfModHicrData": wfModHicrData,
       "wfModHlsr": wfModHlsr,
       "wfModHlsrData": wfModHlsrData,
       "wfSoftwareConfig": wfSoftwareConfig,
       "wfProtocols": wfProtocols,
       "wfIPROTOLoad": wfIPROTOLoad,
       "wfDECNETLoad": wfDECNETLoad,
       "wfATLoad": wfATLoad,
       "wfXNSLoad": wfXNSLoad,
       "wfIPXLoad": wfIPXLoad,
       "wfOSILoad": wfOSILoad,
       "wfX25DTELoad": wfX25DTELoad,
       "wfX25DCELoad": wfX25DCELoad,
       "wfVINESLoad": wfVINESLoad,
       "wfLinkModules": wfLinkModules,
       "wfENETIILoad": wfENETIILoad,
       "wfQENETLoad": wfQENETLoad,
       "wfFDDILoad": wfFDDILoad,
       "wfDSDELoad": wfDSDELoad,
       "wfDSDEIILoad": wfDSDEIILoad,
       "wfQSYNCLoad": wfQSYNCLoad,
       "wfDTLoad": wfDTLoad,
       "wfDSTLoad": wfDSTLoad,
       "wfT1IILoad": wfT1IILoad,
       "wfE1IILoad": wfE1IILoad,
       "wfHSSILoad": wfHSSILoad,
       "wfFNSDSELoad": wfFNSDSELoad,
       "wfFNSDSDTLoad": wfFNSDSDTLoad,
       "wfDrivers": wfDrivers,
       "wfLANCELoad": wfLANCELoad,
       "wfILACCLoad": wfILACCLoad,
       "wfFSILoad": wfFSILoad,
       "wfTMS380Load": wfTMS380Load,
       "wfMK5025Load": wfMK5025Load,
       "wfDS2180Load": wfDS2180Load,
       "wfDS2181Load": wfDS2181Load,
       "wfDEFALoad": wfDEFALoad,
       "wfAMZ8530Load": wfAMZ8530Load,
       "wfHSSIFSILoad": wfHSSIFSILoad,
       "wfSystem": wfSystem,
       "wfSys": wfSys,
       "wfSysDescr": wfSysDescr,
       "wfSysObjectID": wfSysObjectID,
       "wfSysUpTime": wfSysUpTime,
       "wfSysContact": wfSysContact,
       "wfSysName": wfSysName,
       "wfSysLocation": wfSysLocation,
       "wfSysServices": wfSysServices,
       "wfSysGmtOffset": wfSysGmtOffset,
       "wfSysMibVersion": wfSysMibVersion,
       "wfServices": wfServices,
       "wfConsole": wfConsole,
       "wfBaudRate": wfBaudRate,
       "wfDataBits": wfDataBits,
       "wfParity": wfParity,
       "wfStopBits": wfStopBits,
       "wfModemEnable": wfModemEnable,
       "wfLinesPerScreen": wfLinesPerScreen,
       "wfMoreEnable": wfMoreEnable,
       "wfPrompt": wfPrompt,
       "wfLoginTimeOut": wfLoginTimeOut,
       "wfPasswordTimeOut": wfPasswordTimeOut,
       "wfCommandTimeOut": wfCommandTimeOut,
       "wfLoginRetries": wfLoginRetries,
       "wfTotalLogins": wfTotalLogins,
       "wfUserLoginErrors": wfUserLoginErrors,
       "wfManagerLoginErrors": wfManagerLoginErrors,
       "wfOtherLoginErrors": wfOtherLoginErrors,
       "wfTtyFrameErrors": wfTtyFrameErrors,
       "wfTtyOverrunErrors": wfTtyOverrunErrors,
       "wfTtyParityErrors": wfTtyParityErrors,
       "wfTtyInfifoErrors": wfTtyInfifoErrors,
       "wfTiRui": wfTiRui,
       "wfTiRuiState": wfTiRuiState,
       "wfTiRuiAction": wfTiRuiAction,
       "wfTiRuiResult": wfTiRuiResult,
       "wfTiRuiInReqs": wfTiRuiInReqs,
       "wfTiRuiOutResults": wfTiRuiOutResults,
       "wfTiRuiOutResultsErr": wfTiRuiOutResultsErr,
       "wfCircuitNameTable": wfCircuitNameTable,
       "wfCircuitNameEntry": wfCircuitNameEntry,
       "wfCircuitNameDelete": wfCircuitNameDelete,
       "wfCircuitNumber": wfCircuitNumber,
       "wfCircuitName": wfCircuitName,
       "wfCircuitIfType": wfCircuitIfType,
       "wfCircuitProtoMap": wfCircuitProtoMap,
       "wfGameGroup": wfGameGroup,
       "wfKernelTable": wfKernelTable,
       "wfKernelEntry": wfKernelEntry,
       "wfKernelSlot": wfKernelSlot,
       "wfKernelMemorySize": wfKernelMemorySize,
       "wfKernelMemoryFree": wfKernelMemoryFree,
       "wfKernelMemorySegsTotal": wfKernelMemorySegsTotal,
       "wfKernelMemorySegsFree": wfKernelMemorySegsFree,
       "wfKernelMemoryMaxSegFree": wfKernelMemoryMaxSegFree,
       "wfKernelBuffersTotal": wfKernelBuffersTotal,
       "wfKernelBuffersFree": wfKernelBuffersFree,
       "wfKernelTasksTotal": wfKernelTasksTotal,
       "wfKernelTasksInQueue": wfKernelTasksInQueue,
       "wfKernelTimersTotal": wfKernelTimersTotal,
       "wfKernelTimersActive": wfKernelTimersActive,
       "wfKernelBufOwnerTask1": wfKernelBufOwnerTask1,
       "wfKernelBufOwnerTask1Bufs": wfKernelBufOwnerTask1Bufs,
       "wfKernelBufOwnerTask2": wfKernelBufOwnerTask2,
       "wfKernelBufOwnerTask2Bufs": wfKernelBufOwnerTask2Bufs,
       "wfKernelBufOwnerTask3": wfKernelBufOwnerTask3,
       "wfKernelBufOwnerTask3Bufs": wfKernelBufOwnerTask3Bufs,
       "wfKernelBufOwnerTask4": wfKernelBufOwnerTask4,
       "wfKernelBufOwnerTask4Bufs": wfKernelBufOwnerTask4Bufs,
       "wfKernelBufOwnerTask5": wfKernelBufOwnerTask5,
       "wfKernelBufOwnerTask5Bufs": wfKernelBufOwnerTask5Bufs,
       "wfKernelBufOwnerTask6": wfKernelBufOwnerTask6,
       "wfKernelBufOwnerTask6Bufs": wfKernelBufOwnerTask6Bufs,
       "wfKernelBufOwnerTask7": wfKernelBufOwnerTask7,
       "wfKernelBufOwnerTask7Bufs": wfKernelBufOwnerTask7Bufs,
       "wfKernelBufOwnerTask8": wfKernelBufOwnerTask8,
       "wfKernelBufOwnerTask8Bufs": wfKernelBufOwnerTask8Bufs,
       "wfKernelBufOwnerTask9": wfKernelBufOwnerTask9,
       "wfKernelBufOwnerTask9Bufs": wfKernelBufOwnerTask9Bufs,
       "wfKernelBufOwnerTask10": wfKernelBufOwnerTask10,
       "wfKernelBufOwnerTask10Bufs": wfKernelBufOwnerTask10Bufs,
       "wfKernelMemOwnerTask1": wfKernelMemOwnerTask1,
       "wfKernelMemOwnerTask1Size": wfKernelMemOwnerTask1Size,
       "wfKernelMemOwnerTask2": wfKernelMemOwnerTask2,
       "wfKernelMemOwnerTask2Size": wfKernelMemOwnerTask2Size,
       "wfKernelMemOwnerTask3": wfKernelMemOwnerTask3,
       "wfKernelMemOwnerTask3Size": wfKernelMemOwnerTask3Size,
       "wfKernelMemOwnerTask4": wfKernelMemOwnerTask4,
       "wfKernelMemOwnerTask4Size": wfKernelMemOwnerTask4Size,
       "wfKernelMemOwnerTask5": wfKernelMemOwnerTask5,
       "wfKernelMemOwnerTask5Size": wfKernelMemOwnerTask5Size,
       "wfKernelMemOwnerTask6": wfKernelMemOwnerTask6,
       "wfKernelMemOwnerTask6Size": wfKernelMemOwnerTask6Size,
       "wfKernelMemOwnerTask7": wfKernelMemOwnerTask7,
       "wfKernelMemOwnerTask7Size": wfKernelMemOwnerTask7Size,
       "wfKernelMemOwnerTask8": wfKernelMemOwnerTask8,
       "wfKernelMemOwnerTask8Size": wfKernelMemOwnerTask8Size,
       "wfKernelMemOwnerTask9": wfKernelMemOwnerTask9,
       "wfKernelMemOwnerTask9Size": wfKernelMemOwnerTask9Size,
       "wfKernelMemOwnerTask10": wfKernelMemOwnerTask10,
       "wfKernelMemOwnerTask10Size": wfKernelMemOwnerTask10Size,
       "wfLine": wfLine,
       "wfCSMACDTable": wfCSMACDTable,
       "wfCSMACDEntry": wfCSMACDEntry,
       "wfCSMACDDelete": wfCSMACDDelete,
       "wfCSMACDEnable": wfCSMACDEnable,
       "wfCSMACDState": wfCSMACDState,
       "wfCSMACDSlot": wfCSMACDSlot,
       "wfCSMACDConnector": wfCSMACDConnector,
       "wfCSMACDCct": wfCSMACDCct,
       "wfCSMACDBofl": wfCSMACDBofl,
       "wfCSMACDBoflTmo": wfCSMACDBoflTmo,
       "wfCSMACDMtu": wfCSMACDMtu,
       "wfCSMACDMadr": wfCSMACDMadr,
       "wfCSMACDOctetsRxOk": wfCSMACDOctetsRxOk,
       "wfCSMACDFramesRxOk": wfCSMACDFramesRxOk,
       "wfCSMACDOctetsTxOk": wfCSMACDOctetsTxOk,
       "wfCSMACDFramesTxOk": wfCSMACDFramesTxOk,
       "wfCSMACDDeferredTx": wfCSMACDDeferredTx,
       "wfCSMACDLateCollnTx": wfCSMACDLateCollnTx,
       "wfCSMACDExcessvCollnTx": wfCSMACDExcessvCollnTx,
       "wfCSMACDBablErrorTx": wfCSMACDBablErrorTx,
       "wfCSMACDBufErrorTx": wfCSMACDBufErrorTx,
       "wfCSMACDLcarTx": wfCSMACDLcarTx,
       "wfCSMACDUfloTx": wfCSMACDUfloTx,
       "wfCSMACDFcsErrorRx": wfCSMACDFcsErrorRx,
       "wfCSMACDAlignErrorRx": wfCSMACDAlignErrorRx,
       "wfCSMACDLackRescErrorRx": wfCSMACDLackRescErrorRx,
       "wfCSMACDTooLongErrorRx": wfCSMACDTooLongErrorRx,
       "wfCSMACDOfloRx": wfCSMACDOfloRx,
       "wfCSMACDMerr": wfCSMACDMerr,
       "wfCSMACDCerr": wfCSMACDCerr,
       "wfCSMACDHardwareFilter": wfCSMACDHardwareFilter,
       "wfCSMACDTxQueueLength": wfCSMACDTxQueueLength,
       "wfCSMACDRxQueueLength": wfCSMACDRxQueueLength,
       "wfCSMACDTxClipFrames": wfCSMACDTxClipFrames,
       "wfCSMACDRxReplenMisses": wfCSMACDRxReplenMisses,
       "wfTokenRingTable": wfTokenRingTable,
       "wfTokenRingEntry": wfTokenRingEntry,
       "wfTokenRingDelete": wfTokenRingDelete,
       "wfTokenRingDisable": wfTokenRingDisable,
       "wfTokenRingState": wfTokenRingState,
       "wfTokenRingSlot": wfTokenRingSlot,
       "wfTokenRingConnector": wfTokenRingConnector,
       "wfTokenRingCct": wfTokenRingCct,
       "wfTokenRingMtu": wfTokenRingMtu,
       "wfTokenRingMadr": wfTokenRingMadr,
       "wfTokenRingCfgMadr": wfTokenRingCfgMadr,
       "wfTokenRingMadrSelect": wfTokenRingMadrSelect,
       "wfTokenRingSpeed": wfTokenRingSpeed,
       "wfTokenRingEarlyTokenRelease": wfTokenRingEarlyTokenRelease,
       "wfTokenRingStatus": wfTokenRingStatus,
       "wfTokenRingOpenState": wfTokenRingOpenState,
       "wfTokenRingOpenStatus": wfTokenRingOpenStatus,
       "wfTokenRingUpStream": wfTokenRingUpStream,
       "wfTokenRingRxOctets": wfTokenRingRxOctets,
       "wfTokenRingRxFrames": wfTokenRingRxFrames,
       "wfTokenRingTxOctets": wfTokenRingTxOctets,
       "wfTokenRingTxFrames": wfTokenRingTxFrames,
       "wfTokenRingInDiscards": wfTokenRingInDiscards,
       "wfTokenRingInErrors": wfTokenRingInErrors,
       "wfTokenRingOutDiscards": wfTokenRingOutDiscards,
       "wfTokenRingOutErrors": wfTokenRingOutErrors,
       "wfTokenRingTxClipFrames": wfTokenRingTxClipFrames,
       "wfTokenRingRxReplenMisses": wfTokenRingRxReplenMisses,
       "wfTokenRingSignalLosses": wfTokenRingSignalLosses,
       "wfTokenRingHardErrors": wfTokenRingHardErrors,
       "wfTokenRingSoftErrors": wfTokenRingSoftErrors,
       "wfTokenRingTransmitBeacons": wfTokenRingTransmitBeacons,
       "wfTokenRingLobeWireFaults": wfTokenRingLobeWireFaults,
       "wfTokenRingAutoRemovalErrors": wfTokenRingAutoRemovalErrors,
       "wfTokenRingRequestRemoves": wfTokenRingRequestRemoves,
       "wfTokenRingCounterOverflows": wfTokenRingCounterOverflows,
       "wfTokenRingSingleStations": wfTokenRingSingleStations,
       "wfTokenRingRingRecoveries": wfTokenRingRingRecoveries,
       "wfTokenRingAdapterChecks": wfTokenRingAdapterChecks,
       "wfTokenRingFirstAdapterCheckCode": wfTokenRingFirstAdapterCheckCode,
       "wfTokenRingLastAdapterCheckCode": wfTokenRingLastAdapterCheckCode,
       "wfTokenRingLineErrors": wfTokenRingLineErrors,
       "wfTokenRingBurstErrors": wfTokenRingBurstErrors,
       "wfTokenRingAriFciErrors": wfTokenRingAriFciErrors,
       "wfTokenRingLostFrameErrors": wfTokenRingLostFrameErrors,
       "wfTokenRingRxCongestionErrors": wfTokenRingRxCongestionErrors,
       "wfTokenRingFrameCopiedErrors": wfTokenRingFrameCopiedErrors,
       "wfTokenRingTokenErrors": wfTokenRingTokenErrors,
       "wfTokenRingDmaBusErrors": wfTokenRingDmaBusErrors,
       "wfTokenRingDmaParityErrors": wfTokenRingDmaParityErrors,
       "wfTokenRingSrbNotFreeCmdAborts": wfTokenRingSrbNotFreeCmdAborts,
       "wfTokenRingRxProcessings": wfTokenRingRxProcessings,
       "wfTokenRingTxProcessings": wfTokenRingTxProcessings,
       "wfTokenRingTxCmplProcessings": wfTokenRingTxCmplProcessings,
       "wfTokenRingRxTimeouts": wfTokenRingRxTimeouts,
       "wfTokenRingCmdTimeouts": wfTokenRingCmdTimeouts,
       "wfTokenRingRxHostIntErrors": wfTokenRingRxHostIntErrors,
       "wfTokenRingRxTxBufferSize": wfTokenRingRxTxBufferSize,
       "wfFddiTable": wfFddiTable,
       "wfFddiEntry": wfFddiEntry,
       "wfFDDIDelete": wfFDDIDelete,
       "wfFDDIEnable": wfFDDIEnable,
       "wfFDDIState": wfFDDIState,
       "wfFDDISlot": wfFDDISlot,
       "wfFDDINode": wfFDDINode,
       "wfFDDICct": wfFDDICct,
       "wfFDDIBofl": wfFDDIBofl,
       "wfFDDIBoflTmo": wfFDDIBoflTmo,
       "wfFDDIMtu": wfFDDIMtu,
       "wfFDDIMadr": wfFDDIMadr,
       "wfFDDIOctetsRxOk": wfFDDIOctetsRxOk,
       "wfFDDIFramesRxOk": wfFDDIFramesRxOk,
       "wfFDDIOctetsTxOk": wfFDDIOctetsTxOk,
       "wfFDDIFramesTxOk": wfFDDIFramesTxOk,
       "wfFDDICrcErrRx": wfFDDICrcErrRx,
       "wfFDDIOverrunRx": wfFDDIOverrunRx,
       "wfFDDIParityErrRx": wfFDDIParityErrRx,
       "wfFDDIMacErrRx": wfFDDIMacErrRx,
       "wfFDDIRingErrRx": wfFDDIRingErrRx,
       "wfFDDISmtRingErrRx": wfFDDISmtRingErrRx,
       "wfFDDIRingOverrunRx": wfFDDIRingOverrunRx,
       "wfFDDISmtRingOverrunRx": wfFDDISmtRingOverrunRx,
       "wfFDDIAbortTx": wfFDDIAbortTx,
       "wfFDDIUnderrunTx": wfFDDIUnderrunTx,
       "wfFDDIParityErrTx": wfFDDIParityErrTx,
       "wfFDDIRingErrTx": wfFDDIRingErrTx,
       "wfFDDIPortOpErr": wfFDDIPortOpErr,
       "wfFDDIInternOpErr": wfFDDIInternOpErr,
       "wfFDDIHostErr": wfFDDIHostErr,
       "wfFDDISmtConnectionPolicy": wfFDDISmtConnectionPolicy,
       "wfFDDISmtTNotify": wfFDDISmtTNotify,
       "wfFDDIMacTReq": wfFDDIMacTReq,
       "wfFDDIMacTMax": wfFDDIMacTMax,
       "wfFDDIMacTvxValue": wfFDDIMacTvxValue,
       "wfFDDIMacTMin": wfFDDIMacTMin,
       "wfFDDIHardwareFilter": wfFDDIHardwareFilter,
       "wfFDDISmtEnable": wfFDDISmtEnable,
       "wfFDDITxQueueLength": wfFDDITxQueueLength,
       "wfFDDIRxQueueLength": wfFDDIRxQueueLength,
       "wfFDDITxClipFrames": wfFDDITxClipFrames,
       "wfFDDIRxReplenMisses": wfFDDIRxReplenMisses,
       "wfSyncTable": wfSyncTable,
       "wfSyncEntry": wfSyncEntry,
       "wfSyncDelete": wfSyncDelete,
       "wfSyncDisable": wfSyncDisable,
       "wfSyncState": wfSyncState,
       "wfSyncSlot": wfSyncSlot,
       "wfSyncConnector": wfSyncConnector,
       "wfSyncCct": wfSyncCct,
       "wfSyncBofl": wfSyncBofl,
       "wfSyncBoflTmo": wfSyncBoflTmo,
       "wfSyncMtu": wfSyncMtu,
       "wfSyncMadr": wfSyncMadr,
       "wfSyncPromiscuous": wfSyncPromiscuous,
       "wfSyncXid": wfSyncXid,
       "wfSyncClkSource": wfSyncClkSource,
       "wfSyncClkSpeed": wfSyncClkSpeed,
       "wfSyncSignalMode": wfSyncSignalMode,
       "wfSyncRtsEnable": wfSyncRtsEnable,
       "wfSyncBurstCount": wfSyncBurstCount,
       "wfSyncService": wfSyncService,
       "wfSyncRetryCount": wfSyncRetryCount,
       "wfSyncLinkIdleTimer": wfSyncLinkIdleTimer,
       "wfSyncRetryTimer": wfSyncRetryTimer,
       "wfSyncExtendedAddress": wfSyncExtendedAddress,
       "wfSyncExtendedAddressForce": wfSyncExtendedAddressForce,
       "wfSyncExtendedControl": wfSyncExtendedControl,
       "wfSyncExtendedControlForce": wfSyncExtendedControlForce,
       "wfSyncConnectAttempts": wfSyncConnectAttempts,
       "wfSyncWindowSizeTx": wfSyncWindowSizeTx,
       "wfSyncWindowSizeTxExtc": wfSyncWindowSizeTxExtc,
       "wfSyncMinFrameSpace": wfSyncMinFrameSpace,
       "wfSyncLocalAddress": wfSyncLocalAddress,
       "wfSyncRemoteAddress": wfSyncRemoteAddress,
       "wfSyncPassThruLocalMadr": wfSyncPassThruLocalMadr,
       "wfSyncPassThruRemoteMadr": wfSyncPassThruRemoteMadr,
       "wfSyncWanProtocol": wfSyncWanProtocol,
       "wfSyncCrcSize": wfSyncCrcSize,
       "wfSyncRxOctets": wfSyncRxOctets,
       "wfSyncRxFrames": wfSyncRxFrames,
       "wfSyncTxOctets": wfSyncTxOctets,
       "wfSyncTxFrames": wfSyncTxFrames,
       "wfSyncRxErrors": wfSyncRxErrors,
       "wfSyncTxErrors": wfSyncTxErrors,
       "wfSyncLackRescRx": wfSyncLackRescRx,
       "wfSyncLackRescTx": wfSyncLackRescTx,
       "wfSyncUnderFlowTx": wfSyncUnderFlowTx,
       "wfSyncRejectsTx": wfSyncRejectsTx,
       "wfSyncRejectsRx": wfSyncRejectsRx,
       "wfSyncOverFlowRx": wfSyncOverFlowRx,
       "wfSyncFramesIncompRx": wfSyncFramesIncompRx,
       "wfSyncBadFramesRx": wfSyncBadFramesRx,
       "wfSyncFrameRejectsRx": wfSyncFrameRejectsRx,
       "wfSyncRuntsRx": wfSyncRuntsRx,
       "wfSyncT1Timeouts": wfSyncT1Timeouts,
       "wfSyncMemoryErrors": wfSyncMemoryErrors,
       "wfSyncMediaType": wfSyncMediaType,
       "wfHwFGroup": wfHwFGroup,
       "wfHwfTable": wfHwfTable,
       "wfHwfEntry": wfHwfEntry,
       "wfHwfDelete": wfHwfDelete,
       "wfHwfEnable": wfHwfEnable,
       "wfHwfState": wfHwfState,
       "wfHwfSlot": wfHwfSlot,
       "wfHwfAvailableLines": wfHwfAvailableLines,
       "wfHwfLineTable": wfHwfLineTable,
       "wfHwfLineEntry": wfHwfLineEntry,
       "wfHwfLineState": wfHwfLineState,
       "wfHwfLineSlot": wfHwfLineSlot,
       "wfHwfLineNumber": wfHwfLineNumber,
       "wfHwfLineCct": wfHwfLineCct,
       "wfHwfLineCapableMaxTblSize": wfHwfLineCapableMaxTblSize,
       "wfHwfLineCurrentTblSize": wfHwfLineCurrentTblSize,
       "wfHwfLineCurrentUsedEntries": wfHwfLineCurrentUsedEntries,
       "wfHwfLineDroppedFrames": wfHwfLineDroppedFrames,
       "wfHssiTable": wfHssiTable,
       "wfHssiEntry": wfHssiEntry,
       "wfHssiDelete": wfHssiDelete,
       "wfHssiDisable": wfHssiDisable,
       "wfHssiState": wfHssiState,
       "wfHssiSlot": wfHssiSlot,
       "wfHssiConnector": wfHssiConnector,
       "wfHssiCct": wfHssiCct,
       "wfHssiBofl": wfHssiBofl,
       "wfHssiBoflTmo": wfHssiBoflTmo,
       "wfHssiMtu": wfHssiMtu,
       "wfHssiMadr": wfHssiMadr,
       "wfHssiService": wfHssiService,
       "wfHssiWanProtocol": wfHssiWanProtocol,
       "wfHssiTransmissionInterface": wfHssiTransmissionInterface,
       "wfHssiExternalClkSpeed": wfHssiExternalClkSpeed,
       "wfHssiCrcSize": wfHssiCrcSize,
       "wfHssiInternalClkTestMode": wfHssiInternalClkTestMode,
       "wfHssiRxOctets": wfHssiRxOctets,
       "wfHssiRxFrames": wfHssiRxFrames,
       "wfHssiTxOctets": wfHssiTxOctets,
       "wfHssiTxFrames": wfHssiTxFrames,
       "wfHssiInDiscards": wfHssiInDiscards,
       "wfHssiInErrors": wfHssiInErrors,
       "wfHssiOutDiscards": wfHssiOutDiscards,
       "wfHssiOutErrors": wfHssiOutErrors,
       "wfHssiRxLongFrames": wfHssiRxLongFrames,
       "wfHssiTxClipFrames": wfHssiTxClipFrames,
       "wfHssiRxReplenMisses": wfHssiRxReplenMisses,
       "wfHssiLastRxErrorCtrl": wfHssiLastRxErrorCtrl,
       "wfHssiRxCrcErrors": wfHssiRxCrcErrors,
       "wfHssiRxOverruns": wfHssiRxOverruns,
       "wfHssiRxAborts": wfHssiRxAborts,
       "wfHssiLastTxErrorCtrl": wfHssiLastTxErrorCtrl,
       "wfHssiTxAborts": wfHssiTxAborts,
       "wfHssiTxUnderruns": wfHssiTxUnderruns,
       "wfHssiRxRingErrors": wfHssiRxRingErrors,
       "wfHssiLastRxRingState": wfHssiLastRxRingState,
       "wfHssiRxRingOverruns": wfHssiRxRingOverruns,
       "wfHssiTxRingErrors": wfHssiTxRingErrors,
       "wfHssiLastTxRingState": wfHssiLastTxRingState,
       "wfHssiPortOpErrors": wfHssiPortOpErrors,
       "wfHssiInternOpErrors": wfHssiInternOpErrors,
       "wfHssiHostErrors": wfHssiHostErrors,
       "wfHssiRxProcessings": wfHssiRxProcessings,
       "wfHssiTxProcessings": wfHssiTxProcessings,
       "wfHssiTxCmplProcessings": wfHssiTxCmplProcessings,
       "wfHssiIntrProcessings": wfHssiIntrProcessings,
       "wfHssiBoflNum": wfHssiBoflNum,
       "wfHssiBoflLen": wfHssiBoflLen,
       "wfHssiRxBufferLength": wfHssiRxBufferLength,
       "wfHssiMemPageLength": wfHssiMemPageLength,
       "wfHssiRxRingLength": wfHssiRxRingLength,
       "wfHssiTxRingLength": wfHssiTxRingLength,
       "wfHssiRxFifoWatermark": wfHssiRxFifoWatermark,
       "wfHssiTxFifoWatermark": wfHssiTxFifoWatermark,
       "wfHssiMaxRxMemory": wfHssiMaxRxMemory,
       "wfHssiLinkInterface": wfHssiLinkInterface,
       "wfHssiTurboBofl": wfHssiTurboBofl,
       "wfT1Table": wfT1Table,
       "wfT1Entry": wfT1Entry,
       "wfT1Delete": wfT1Delete,
       "wfT1Disable": wfT1Disable,
       "wfT1State": wfT1State,
       "wfT1Slot": wfT1Slot,
       "wfT1Connector": wfT1Connector,
       "wfT1Madr": wfT1Madr,
       "wfT1FrameType": wfT1FrameType,
       "wfT1LineBuildout": wfT1LineBuildout,
       "wfT1B8ZSSupport": wfT1B8ZSSupport,
       "wfT1ClockMode": wfT1ClockMode,
       "wfT1MiniDacs": wfT1MiniDacs,
       "wfT1BipolarVios": wfT1BipolarVios,
       "wfT1FrameBitErrs": wfT1FrameBitErrs,
       "wfT1OutOfFrameErrs": wfT1OutOfFrameErrs,
       "wfT1SuperFrameErrs": wfT1SuperFrameErrs,
       "wfT1RcvYelAlarms": wfT1RcvYelAlarms,
       "wfT1RcvCarrierLoss": wfT1RcvCarrierLoss,
       "wfT1RcvRedAlarms": wfT1RcvRedAlarms,
       "wfE1Table": wfE1Table,
       "wfE1Entry": wfE1Entry,
       "wfE1Delete": wfE1Delete,
       "wfE1Disable": wfE1Disable,
       "wfE1State": wfE1State,
       "wfE1Slot": wfE1Slot,
       "wfE1Connector": wfE1Connector,
       "wfE1Madr": wfE1Madr,
       "wfE1HDB3Support": wfE1HDB3Support,
       "wfE1ClockMode": wfE1ClockMode,
       "wfE1MiniDacs": wfE1MiniDacs,
       "wfE1BipolarVios": wfE1BipolarVios,
       "wfE1FrameErrs": wfE1FrameErrs,
       "wfE1RcvRemAlms": wfE1RcvRemAlms,
       "wfE1RcvMfmAlms": wfE1RcvMfmAlms,
       "wfE1MfsErrs": wfE1MfsErrs,
       "wfE1SyncLoss": wfE1SyncLoss,
       "wfE1RcvSig1s": wfE1RcvSig1s,
       "wfE1RcvUnfrm1s": wfE1RcvUnfrm1s,
       "wfDs1Group": wfDs1Group,
       "wfDs1Config": wfDs1Config,
       "wfDs1ConfigEntry": wfDs1ConfigEntry,
       "wfDs1LineIndex": wfDs1LineIndex,
       "wfDs1TimeElapsed": wfDs1TimeElapsed,
       "wfDs1ValidIntervals": wfDs1ValidIntervals,
       "wfDs1LineType": wfDs1LineType,
       "wfDs1ZeroCoding": wfDs1ZeroCoding,
       "wfDs1SendCode": wfDs1SendCode,
       "wfDs1CircuitIdentifier": wfDs1CircuitIdentifier,
       "wfDs1LoopbackConfig": wfDs1LoopbackConfig,
       "wfDs1LineStatus": wfDs1LineStatus,
       "wfDs1Current": wfDs1Current,
       "wfDs1CurrentEntry": wfDs1CurrentEntry,
       "wfDs1CurrentIndex": wfDs1CurrentIndex,
       "wfDs1CurrentESs": wfDs1CurrentESs,
       "wfDs1CurrentSESs": wfDs1CurrentSESs,
       "wfDs1CurrentSEFs": wfDs1CurrentSEFs,
       "wfDs1CurrentUASs": wfDs1CurrentUASs,
       "wfDs1CurrentBPVs": wfDs1CurrentBPVs,
       "wfDs1CurrentCVs": wfDs1CurrentCVs,
       "wfDs1Interval": wfDs1Interval,
       "wfDs1IntervalEntry": wfDs1IntervalEntry,
       "wfDs1IntervalIndex": wfDs1IntervalIndex,
       "wfDs1IntervalNumber": wfDs1IntervalNumber,
       "wfDs1IntervalESs": wfDs1IntervalESs,
       "wfDs1IntervalSESs": wfDs1IntervalSESs,
       "wfDs1IntervalSEFs": wfDs1IntervalSEFs,
       "wfDs1IntervalUASs": wfDs1IntervalUASs,
       "wfDs1IntervalBPVs": wfDs1IntervalBPVs,
       "wfDs1IntervalCVs": wfDs1IntervalCVs,
       "wfDs1Total": wfDs1Total,
       "wfDs1TotalEntry": wfDs1TotalEntry,
       "wfDs1TotalIndex": wfDs1TotalIndex,
       "wfDs1TotalESs": wfDs1TotalESs,
       "wfDs1TotalSESs": wfDs1TotalSESs,
       "wfDs1TotalSEFs": wfDs1TotalSEFs,
       "wfDs1TotalUASs": wfDs1TotalUASs,
       "wfDs1TotalBPVs": wfDs1TotalBPVs,
       "wfDs1TotalCVs": wfDs1TotalCVs,
       "wfDs1FeCurrent": wfDs1FeCurrent,
       "wfDs1FeCurrentEntry": wfDs1FeCurrentEntry,
       "wfDs1FeCurrentIndex": wfDs1FeCurrentIndex,
       "wfDs1FeCurrentESs": wfDs1FeCurrentESs,
       "wfDs1FeCurrentSESs": wfDs1FeCurrentSESs,
       "wfDs1FeCurrentSEFs": wfDs1FeCurrentSEFs,
       "wfDs1FeCurrentBPVs": wfDs1FeCurrentBPVs,
       "wfDs1FeCurrentCVs": wfDs1FeCurrentCVs,
       "wfDs1FeInterval": wfDs1FeInterval,
       "wfDs1FeIntervalEntry": wfDs1FeIntervalEntry,
       "wfDs1FeIntervalIndex": wfDs1FeIntervalIndex,
       "wfDs1FeIntervalNumber": wfDs1FeIntervalNumber,
       "wfDs1FeIntervalESs": wfDs1FeIntervalESs,
       "wfDs1FeIntervalSESs": wfDs1FeIntervalSESs,
       "wfDs1FeIntervalSEFs": wfDs1FeIntervalSEFs,
       "wfDs1FeIntervalBPVs": wfDs1FeIntervalBPVs,
       "wfDs1FeIntervalCVs": wfDs1FeIntervalCVs,
       "wfDs1FeTotal": wfDs1FeTotal,
       "wfDs1FeTotalEntry": wfDs1FeTotalEntry,
       "wfDs1FeTotalIndex": wfDs1FeTotalIndex,
       "wfDs1FeTotalESs": wfDs1FeTotalESs,
       "wfDs1FeTotalSESs": wfDs1FeTotalSESs,
       "wfDs1FeTotalSEFs": wfDs1FeTotalSEFs,
       "wfDs1FeTotalBPVs": wfDs1FeTotalBPVs,
       "wfDs1FeTotalCVs": wfDs1FeTotalCVs,
       "wfDs3Group": wfDs3Group,
       "wfDs3Config": wfDs3Config,
       "wfDs3ConfigEntry": wfDs3ConfigEntry,
       "wfDs3LineIndex": wfDs3LineIndex,
       "wfDs3TimeElapsed": wfDs3TimeElapsed,
       "wfDs3ValidIntervals": wfDs3ValidIntervals,
       "wfDs3LineType": wfDs3LineType,
       "wfDs3ZeroCoding": wfDs3ZeroCoding,
       "wfDs3SendCode": wfDs3SendCode,
       "wfDs3CircuitIdentifier": wfDs3CircuitIdentifier,
       "wfDs3LoopbackConfig": wfDs3LoopbackConfig,
       "wfDs3LineStatus": wfDs3LineStatus,
       "wfDs3Current": wfDs3Current,
       "wfDs3CurrentEntry": wfDs3CurrentEntry,
       "wfDs3CurrentIndex": wfDs3CurrentIndex,
       "wfDs3CurrentESs": wfDs3CurrentESs,
       "wfDs3CurrentSESs": wfDs3CurrentSESs,
       "wfDs3CurrentSEFs": wfDs3CurrentSEFs,
       "wfDs3CurrentUASs": wfDs3CurrentUASs,
       "wfDs3CurrentBPVs": wfDs3CurrentBPVs,
       "wfDs3CurrentCVs": wfDs3CurrentCVs,
       "wfDs3Interval": wfDs3Interval,
       "wfDs3IntervalEntry": wfDs3IntervalEntry,
       "wfDs3IntervalIndex": wfDs3IntervalIndex,
       "wfDs3IntervalNumber": wfDs3IntervalNumber,
       "wfDs3IntervalESs": wfDs3IntervalESs,
       "wfDs3IntervalSESs": wfDs3IntervalSESs,
       "wfDs3IntervalSEFs": wfDs3IntervalSEFs,
       "wfDs3IntervalUASs": wfDs3IntervalUASs,
       "wfDs3IntervalBPVs": wfDs3IntervalBPVs,
       "wfDs3IntervalCVs": wfDs3IntervalCVs,
       "wfDs3Total": wfDs3Total,
       "wfDs3TotalEntry": wfDs3TotalEntry,
       "wfDs3TotalIndex": wfDs3TotalIndex,
       "wfDs3TotalESs": wfDs3TotalESs,
       "wfDs3TotalSESs": wfDs3TotalSESs,
       "wfDs3TotalSEFs": wfDs3TotalSEFs,
       "wfDs3TotalUASs": wfDs3TotalUASs,
       "wfDs3TotalBPVs": wfDs3TotalBPVs,
       "wfDs3TotalCVs": wfDs3TotalCVs,
       "wfDs3FeConfig": wfDs3FeConfig,
       "wfDs3FeConfigEntry": wfDs3FeConfigEntry,
       "wfDs3FeConfigIndex": wfDs3FeConfigIndex,
       "wfDs3FarEndEquipCode": wfDs3FarEndEquipCode,
       "wfDs3FarEndLocationIDCode": wfDs3FarEndLocationIDCode,
       "wfDs3FarEndFrameIDCode": wfDs3FarEndFrameIDCode,
       "wfDs3FarEndUnitCode": wfDs3FarEndUnitCode,
       "wfDs3FarEndFacilityIDCode": wfDs3FarEndFacilityIDCode,
       "wfDs3FeCurrent": wfDs3FeCurrent,
       "wfDs3FeCurrentEntry": wfDs3FeCurrentEntry,
       "wfDs3FeCurrentIndex": wfDs3FeCurrentIndex,
       "wfDs3FeCurrentESs": wfDs3FeCurrentESs,
       "wfDs3FeCurrentSESs": wfDs3FeCurrentSESs,
       "wfDs3FeCurrentCVs": wfDs3FeCurrentCVs,
       "wfDs3FeInterval": wfDs3FeInterval,
       "wfDs3FeIntervalEntry": wfDs3FeIntervalEntry,
       "wfDs3FeIntervalIndex": wfDs3FeIntervalIndex,
       "wfDs3FeIntervalNumber": wfDs3FeIntervalNumber,
       "wfDs3FeIntervalESs": wfDs3FeIntervalESs,
       "wfDs3FeIntervalSESs": wfDs3FeIntervalSESs,
       "wfDs3FeIntervalCVs": wfDs3FeIntervalCVs,
       "wfDs3FeTotal": wfDs3FeTotal,
       "wfDs3FeTotalEntry": wfDs3FeTotalEntry,
       "wfDs3FeTotalIndex": wfDs3FeTotalIndex,
       "wfDs3FeTotalESs": wfDs3FeTotalESs,
       "wfDs3FeTotalSESs": wfDs3FeTotalSESs,
       "wfDs3FeTotalCVs": wfDs3FeTotalCVs,
       "wfSipGroup": wfSipGroup,
       "wfSipL2": wfSipL2,
       "wfSipL2Entry": wfSipL2Entry,
       "wfSipL2Index": wfSipL2Index,
       "wfSipL2ReceivedCounts": wfSipL2ReceivedCounts,
       "wfSipL2SentCounts": wfSipL2SentCounts,
       "wfSipHcsOrCRCErrors": wfSipHcsOrCRCErrors,
       "wfSipL2PayloadLengthErrors": wfSipL2PayloadLengthErrors,
       "wfSipL2SequenceNumberErrors": wfSipL2SequenceNumberErrors,
       "wfSipL2MidCurrentlyActiveErrors": wfSipL2MidCurrentlyActiveErrors,
       "wfSipL2BomOrSSMsMIDErrors": wfSipL2BomOrSSMsMIDErrors,
       "wfSipL2EomsMIDErrors": wfSipL2EomsMIDErrors,
       "wfSipPlcpGroup": wfSipPlcpGroup,
       "wfSipDs1Plcp": wfSipDs1Plcp,
       "wfSipDs1PlcpEntry": wfSipDs1PlcpEntry,
       "wfSipDs1PlcpIndex": wfSipDs1PlcpIndex,
       "wfSipDs1PlcpSEFs": wfSipDs1PlcpSEFs,
       "wfSipDs1PlcpAlarmState": wfSipDs1PlcpAlarmState,
       "wfSipDs1PlcpUASs": wfSipDs1PlcpUASs,
       "wfSipDs3Plcp": wfSipDs3Plcp,
       "wfSipDs3PlcpEntry": wfSipDs3PlcpEntry,
       "wfSipDs3PlcpIndex": wfSipDs3PlcpIndex,
       "wfSipDs3PlcpSEFs": wfSipDs3PlcpSEFs,
       "wfSipDs3PlcpAlarmState": wfSipDs3PlcpAlarmState,
       "wfSipDs3PlcpUASs": wfSipDs3PlcpUASs,
       "wfFddiGroup": wfFddiGroup,
       "wfFddiSmtGroup": wfFddiSmtGroup,
       "wfFddiSmtTable": wfFddiSmtTable,
       "wfFddiSmtEntry": wfFddiSmtEntry,
       "wfFddiSmtSlot": wfFddiSmtSlot,
       "wfFddiSmtNode": wfFddiSmtNode,
       "wfFddiSmtCct": wfFddiSmtCct,
       "wfFddiSmtStationId": wfFddiSmtStationId,
       "wfFddiSmtOpVersionId": wfFddiSmtOpVersionId,
       "wfFddiSmtMacCt": wfFddiSmtMacCt,
       "wfFddiSmtNonMasterCt": wfFddiSmtNonMasterCt,
       "wfFddiSmtEcmState": wfFddiSmtEcmState,
       "wfFddiSmtCfState": wfFddiSmtCfState,
       "wfFddiMacGroup": wfFddiMacGroup,
       "wfFddiMacTable": wfFddiMacTable,
       "wfFddiMacEntry": wfFddiMacEntry,
       "wfFddiMacSlot": wfFddiMacSlot,
       "wfFddiMacNode": wfFddiMacNode,
       "wfFddiMacCct": wfFddiMacCct,
       "wfFddiMacUpstreamNbr": wfFddiMacUpstreamNbr,
       "wfFddiMacDownstreamNbr": wfFddiMacDownstreamNbr,
       "wfFddiMacSmtAddress": wfFddiMacSmtAddress,
       "wfFddiMacTNeg": wfFddiMacTNeg,
       "wfFddiMacRmtState": wfFddiMacRmtState,
       "wfFddiPathGroup": wfFddiPathGroup,
       "wfFddiPortGroup": wfFddiPortGroup,
       "wfFddiPortTable": wfFddiPortTable,
       "wfFddiPortEntry": wfFddiPortEntry,
       "wfFddiPortSlot": wfFddiPortSlot,
       "wfFddiPortNode": wfFddiPortNode,
       "wfFddiPortCct": wfFddiPortCct,
       "wfFddiPortIndex": wfFddiPortIndex,
       "wfFddiPortPcType": wfFddiPortPcType,
       "wfFddiPortPcNeighbor": wfFddiPortPcNeighbor,
       "wfFddiPortPcmState": wfFddiPortPcmState,
       "wfApplication": wfApplication,
       "wfDataLink": wfDataLink,
       "wfBridgeGroup": wfBridgeGroup,
       "wfBrLearning": wfBrLearning,
       "wfBrTp": wfBrTp,
       "wfBrTpBaseDelete": wfBrTpBaseDelete,
       "wfBrTpBaseEnable": wfBrTpBaseEnable,
       "wfBrTpBaseState": wfBrTpBaseState,
       "wfBrTpFdbTable": wfBrTpFdbTable,
       "wfBrTpFdbEntry": wfBrTpFdbEntry,
       "wfBrTpBaseFdbAddress": wfBrTpBaseFdbAddress,
       "wfBrTpBaseFdbPort": wfBrTpBaseFdbPort,
       "wfBrTpBaseFdbStatus": wfBrTpBaseFdbStatus,
       "wfBrSourceRouting": wfBrSourceRouting,
       "wfBrSr": wfBrSr,
       "wfBrSrBaseDelete": wfBrSrBaseDelete,
       "wfBrSrBaseDisable": wfBrSrBaseDisable,
       "wfBrSrBaseState": wfBrSrBaseState,
       "wfBrSrBaseInternalLanId": wfBrSrBaseInternalLanId,
       "wfBrSrBaseBridgeId": wfBrSrBaseBridgeId,
       "wfBrSrBaseGroupLanId": wfBrSrBaseGroupLanId,
       "wfBrSrBaseIpEncapsDisable": wfBrSrBaseIpEncapsDisable,
       "wfBrSrBaseIpNetworkRingId": wfBrSrBaseIpNetworkRingId,
       "wfBrSrBaseIpInReceives": wfBrSrBaseIpInReceives,
       "wfBrSrBaseIpSeqErrors": wfBrSrBaseIpSeqErrors,
       "wfBrSrBaseIpMtuSize": wfBrSrBaseIpMtuSize,
       "wfBrSrInterfaceTable": wfBrSrInterfaceTable,
       "wfBrSrInterfaceEntry": wfBrSrInterfaceEntry,
       "wfBrSrInterfaceDelete": wfBrSrInterfaceDelete,
       "wfBrSrInterfaceDisable": wfBrSrInterfaceDisable,
       "wfBrSrInterfaceState": wfBrSrInterfaceState,
       "wfBrSrInterfaceCircuit": wfBrSrInterfaceCircuit,
       "wfBrSrInterfaceMaxRds": wfBrSrInterfaceMaxRds,
       "wfBrSrInterfaceRing": wfBrSrInterfaceRing,
       "wfBrSrInterfaceBlockOutSte": wfBrSrInterfaceBlockOutSte,
       "wfBrSrInterfaceBlockInSte": wfBrSrInterfaceBlockInSte,
       "wfBrSrInterfaceBlockIp": wfBrSrInterfaceBlockIp,
       "wfBrSrInterfaceIpAddress": wfBrSrInterfaceIpAddress,
       "wfBrSrInterfaceInFrames": wfBrSrInterfaceInFrames,
       "wfBrSrInterfaceOutFrames": wfBrSrInterfaceOutFrames,
       "wfBrSrInterfaceOutIpFrames": wfBrSrInterfaceOutIpFrames,
       "wfBrSrInterfaceDropInvalidRcs": wfBrSrInterfaceDropInvalidRcs,
       "wfBrSrInterfaceDropInvalidRings": wfBrSrInterfaceDropInvalidRings,
       "wfBrSrInterfaceDropSrfs": wfBrSrInterfaceDropSrfs,
       "wfBrSrBridgeTable": wfBrSrBridgeTable,
       "wfBrSrBridgeEntry": wfBrSrBridgeEntry,
       "wfBrSrBridgeDelete": wfBrSrBridgeDelete,
       "wfBrSrBridgeId": wfBrSrBridgeId,
       "wfBrSrIpExplorerTable": wfBrSrIpExplorerTable,
       "wfBrSrIpExplorerEntry": wfBrSrIpExplorerEntry,
       "wfBrSrIpExplorerDelete": wfBrSrIpExplorerDelete,
       "wfBrSrIpExplorerAddr": wfBrSrIpExplorerAddr,
       "wfBrSrIpEncapsTable": wfBrSrIpEncapsTable,
       "wfBrSrIpEncapsEntry": wfBrSrIpEncapsEntry,
       "wfBrSrIpEncapsRing": wfBrSrIpEncapsRing,
       "wfBrSrIpEncapsIpAddress": wfBrSrIpEncapsIpAddress,
       "wfBrSrIpEncapsStatus": wfBrSrIpEncapsStatus,
       "wfBrSrTrafficFilterTable": wfBrSrTrafficFilterTable,
       "wfBrSrTrafficFilterEntry": wfBrSrTrafficFilterEntry,
       "wfBrSrTrafficFilterCreate": wfBrSrTrafficFilterCreate,
       "wfBrSrTrafficFilterEnable": wfBrSrTrafficFilterEnable,
       "wfBrSrTrafficFilterStatus": wfBrSrTrafficFilterStatus,
       "wfBrSrTrafficFilterCounter": wfBrSrTrafficFilterCounter,
       "wfBrSrTrafficFilterDefinition": wfBrSrTrafficFilterDefinition,
       "wfBrSrTrafficFilterReserved": wfBrSrTrafficFilterReserved,
       "wfBrSrTrafficFilterCircuit": wfBrSrTrafficFilterCircuit,
       "wfBrSrTrafficFilterRuleNumber": wfBrSrTrafficFilterRuleNumber,
       "wfBrSrTrafficFilterFragment": wfBrSrTrafficFilterFragment,
       "wfBrSrEsRifTable": wfBrSrEsRifTable,
       "wfBrSrEsRifEntry": wfBrSrEsRifEntry,
       "wfBrSrEsRifCircuit": wfBrSrEsRifCircuit,
       "wfBrSrEsRifProtocol": wfBrSrEsRifProtocol,
       "wfBrSrEsRifMacAddr": wfBrSrEsRifMacAddr,
       "wfBrSrEsRifRoute": wfBrSrEsRifRoute,
       "wfBrTpInterface": wfBrTpInterface,
       "wfBrTpInterfaceEntry": wfBrTpInterfaceEntry,
       "wfBrTpInterfaceDelete": wfBrTpInterfaceDelete,
       "wfBrTpInterfaceEnable": wfBrTpInterfaceEnable,
       "wfBrTpInterfaceState": wfBrTpInterfaceState,
       "wfBrTpInterfaceCircuit": wfBrTpInterfaceCircuit,
       "wfBrTpInterfaceMaxInfo": wfBrTpInterfaceMaxInfo,
       "wfBrTpInterfaceInFrames": wfBrTpInterfaceInFrames,
       "wfBrTpInterfaceOutFrames": wfBrTpInterfaceOutFrames,
       "wfBrTpInterfaceInDiscards": wfBrTpInterfaceInDiscards,
       "wfBrTrafficFilterTable": wfBrTrafficFilterTable,
       "wfBrTrafficFilterEntry": wfBrTrafficFilterEntry,
       "wfBrTrafficFilterCreate": wfBrTrafficFilterCreate,
       "wfBrTrafficFilterEnable": wfBrTrafficFilterEnable,
       "wfBrTrafficFilterStatus": wfBrTrafficFilterStatus,
       "wfBrTrafficFilterCounter": wfBrTrafficFilterCounter,
       "wfBrTrafficFilterDefinition": wfBrTrafficFilterDefinition,
       "wfBrTrafficFilterReserved": wfBrTrafficFilterReserved,
       "wfBrTrafficFilterCircuit": wfBrTrafficFilterCircuit,
       "wfBrTrafficFilterRuleNumber": wfBrTrafficFilterRuleNumber,
       "wfBrTrafficFilterFragment": wfBrTrafficFilterFragment,
       "wfSpanningTree": wfSpanningTree,
       "wfBrStp": wfBrStp,
       "wfBrStpBaseDelete": wfBrStpBaseDelete,
       "wfBrStpBaseEnable": wfBrStpBaseEnable,
       "wfBrStpBaseState": wfBrStpBaseState,
       "wfBrStpProtocolSpecification": wfBrStpProtocolSpecification,
       "wfBrStpBridgeID": wfBrStpBridgeID,
       "wfBrStpTimeSinceTopologyChange": wfBrStpTimeSinceTopologyChange,
       "wfBrStpTopChanges": wfBrStpTopChanges,
       "wfBrStpDesignatedRoot": wfBrStpDesignatedRoot,
       "wfBrStpRootCost": wfBrStpRootCost,
       "wfBrStpRootPort": wfBrStpRootPort,
       "wfBrStpMaxAge": wfBrStpMaxAge,
       "wfBrStpHelloTime": wfBrStpHelloTime,
       "wfBrStpHoldTime": wfBrStpHoldTime,
       "wfBrStpForwardDelay": wfBrStpForwardDelay,
       "wfBrStpBridgeMaxAge": wfBrStpBridgeMaxAge,
       "wfBrStpBridgeHelloTime": wfBrStpBridgeHelloTime,
       "wfBrStpBridgeForwardDelay": wfBrStpBridgeForwardDelay,
       "wfBrStpInterface": wfBrStpInterface,
       "wfBrStpInterfaceEntry": wfBrStpInterfaceEntry,
       "wfBrStpInterfaceDelete": wfBrStpInterfaceDelete,
       "wfBrStpInterfaceEnable": wfBrStpInterfaceEnable,
       "wfBrStpInterfaceCircuit": wfBrStpInterfaceCircuit,
       "wfBrStpInterfacePriority": wfBrStpInterfacePriority,
       "wfBrStpInterfaceState": wfBrStpInterfaceState,
       "wfBrStpInterfaceMultiCastAddr": wfBrStpInterfaceMultiCastAddr,
       "wfBrStpInterfacePathCost": wfBrStpInterfacePathCost,
       "wfBrStpInterfaceDesignatedRoot": wfBrStpInterfaceDesignatedRoot,
       "wfBrStpInterfaceDesignatedCost": wfBrStpInterfaceDesignatedCost,
       "wfBrStpInterfaceDesignatedBridge": wfBrStpInterfaceDesignatedBridge,
       "wfBrStpInterfaceDesignatedPort": wfBrStpInterfaceDesignatedPort,
       "wfBrStpInterfaceForwardTransitions": wfBrStpInterfaceForwardTransitions,
       "wfBrStpInterfacePktsXmitd": wfBrStpInterfacePktsXmitd,
       "wfBrStpInterfacePktsRcvd": wfBrStpInterfacePktsRcvd,
       "wfIfGroup": wfIfGroup,
       "wfIf": wfIf,
       "wfIfNumber": wfIfNumber,
       "wfIfTable": wfIfTable,
       "wfIfEntry": wfIfEntry,
       "wfIfIndex": wfIfIndex,
       "wfIfDescr": wfIfDescr,
       "wfIfType": wfIfType,
       "wfIfMtu": wfIfMtu,
       "wfIfSpeed": wfIfSpeed,
       "wfIfPhysAddress": wfIfPhysAddress,
       "wfIfAdminStatus": wfIfAdminStatus,
       "wfIfOperStatus": wfIfOperStatus,
       "wfIfLastChange": wfIfLastChange,
       "wfIfInOctets": wfIfInOctets,
       "wfIfInUcastPkts": wfIfInUcastPkts,
       "wfIfInNUCastPkts": wfIfInNUCastPkts,
       "wfIfInDiscards": wfIfInDiscards,
       "wfIfInErrors": wfIfInErrors,
       "wfIfInUnknownProtos": wfIfInUnknownProtos,
       "wfIfOutOctets": wfIfOutOctets,
       "wfIfOutUcastPkts": wfIfOutUcastPkts,
       "wfIfOutNUcastPkts": wfIfOutNUcastPkts,
       "wfIfOutDiscards": wfIfOutDiscards,
       "wfIfOutErrors": wfIfOutErrors,
       "wfIfOutQLen": wfIfOutQLen,
       "wfIfSpecific": wfIfSpecific,
       "wfCircuitOptsGroup": wfCircuitOptsGroup,
       "wfCctOptsTable": wfCctOptsTable,
       "wfCctOptsEntry": wfCctOptsEntry,
       "wfCctOptsDelete": wfCctOptsDelete,
       "wfCctOptsPriorityQueueingDisable": wfCctOptsPriorityQueueingDisable,
       "wfCctOptsCct": wfCctOptsCct,
       "wfCctOptsHighPriorityQueueLimit": wfCctOptsHighPriorityQueueLimit,
       "wfCctOptsNormalPriorityQueueLimit": wfCctOptsNormalPriorityQueueLimit,
       "wfCctOptsLowPriorityQueueLimit": wfCctOptsLowPriorityQueueLimit,
       "wfCctOptsMaxInterruptQueueLatency": wfCctOptsMaxInterruptQueueLatency,
       "wfCctOptsMaxHighPriorityQueueLatency": wfCctOptsMaxHighPriorityQueueLatency,
       "wfCctOptsHiXmits": wfCctOptsHiXmits,
       "wfCctOptsNormalXmits": wfCctOptsNormalXmits,
       "wfCctOptsLoXmits": wfCctOptsLoXmits,
       "wfCctOptsHiClippedPkts": wfCctOptsHiClippedPkts,
       "wfCctOptsNormalClippedPkts": wfCctOptsNormalClippedPkts,
       "wfCctOptsLoClippedPkts": wfCctOptsLoClippedPkts,
       "wfCctOptsIntrQHighWaterPkts": wfCctOptsIntrQHighWaterPkts,
       "wfCctOptsHiQHighWaterPkts": wfCctOptsHiQHighWaterPkts,
       "wfCctOptsNormalQHighWaterPkts": wfCctOptsNormalQHighWaterPkts,
       "wfCctOptsLoQHighWaterPkts": wfCctOptsLoQHighWaterPkts,
       "wfCctOptsHighWaterPktsClear": wfCctOptsHighWaterPktsClear,
       "wfCctOptsDroppedPkts": wfCctOptsDroppedPkts,
       "wfCctOptsLargePkts": wfCctOptsLargePkts,
       "wfCctOptsRxPkts": wfCctOptsRxPkts,
       "wfCctOptsBrFilterTable": wfCctOptsBrFilterTable,
       "wfCctOptsBrFilterEntry": wfCctOptsBrFilterEntry,
       "wfCctOptsBrFilterCreate": wfCctOptsBrFilterCreate,
       "wfCctOptsBrFilterEnable": wfCctOptsBrFilterEnable,
       "wfCctOptsBrFilterState": wfCctOptsBrFilterState,
       "wfCctOptsBrFilterCounter": wfCctOptsBrFilterCounter,
       "wfCctOptsBrFilterDefinition": wfCctOptsBrFilterDefinition,
       "wfCctOptsBrFilterReserved": wfCctOptsBrFilterReserved,
       "wfCctOptsBrFilterCct": wfCctOptsBrFilterCct,
       "wfCctOptsBrFilterRuleNumber": wfCctOptsBrFilterRuleNumber,
       "wfCctOptsBrFilterFragment": wfCctOptsBrFilterFragment,
       "wfCctOptsIpFilterTable": wfCctOptsIpFilterTable,
       "wfCctOptsIpFilterEntry": wfCctOptsIpFilterEntry,
       "wfCctOptsIpFilterCreate": wfCctOptsIpFilterCreate,
       "wfCctOptsIpFilterEnable": wfCctOptsIpFilterEnable,
       "wfCctOptsIpFilterState": wfCctOptsIpFilterState,
       "wfCctOptsIpFilterCounter": wfCctOptsIpFilterCounter,
       "wfCctOptsIpFilterDefinition": wfCctOptsIpFilterDefinition,
       "wfCctOptsIpFilterReserved": wfCctOptsIpFilterReserved,
       "wfCctOptsIpFilterCct": wfCctOptsIpFilterCct,
       "wfCctOptsIpFilterRuleNumber": wfCctOptsIpFilterRuleNumber,
       "wfCctOptsIpFilterFragment": wfCctOptsIpFilterFragment,
       "wfCctOptsLengthBasedTable": wfCctOptsLengthBasedTable,
       "wfCctOptsLengthBasedEntry": wfCctOptsLengthBasedEntry,
       "wfCctOptsLengthBasedDelete": wfCctOptsLengthBasedDelete,
       "wfCctOptsLengthBasedDisable": wfCctOptsLengthBasedDisable,
       "wfCctOptsLengthBasedState": wfCctOptsLengthBasedState,
       "wfCctOptsLengthBasedCct": wfCctOptsLengthBasedCct,
       "wfCctOptsLengthBasedMux": wfCctOptsLengthBasedMux,
       "wfCctOptsLengthBasedData": wfCctOptsLengthBasedData,
       "wfCctOptsLengthBasedLength": wfCctOptsLengthBasedLength,
       "wfCctOptsLengthBasedLessThanQ": wfCctOptsLengthBasedLessThanQ,
       "wfCctOptsLengthBasedGreaterThanQ": wfCctOptsLengthBasedGreaterThanQ,
       "wfDecGroup": wfDecGroup,
       "wfivRouteGroup": wfivRouteGroup,
       "wfivRouteCreateDelete": wfivRouteCreateDelete,
       "wfivRouteEnableDisable": wfivRouteEnableDisable,
       "wfivRouteState": wfivRouteState,
       "wfivRouteBroadcastRouteTimer": wfivRouteBroadcastRouteTimer,
       "wfivRouteRoutingVers": wfivRouteRoutingVers,
       "wfivRouteMaxAddr": wfivRouteMaxAddr,
       "wfivRouteMaxBdcastNonRouters": wfivRouteMaxBdcastNonRouters,
       "wfivRouteMaxBdcastRouters": wfivRouteMaxBdcastRouters,
       "wfivRouteMaxCircuits": wfivRouteMaxCircuits,
       "wfivRouteMaxCost": wfivRouteMaxCost,
       "wfivRouteMaxHops": wfivRouteMaxHops,
       "wfivRouteMaxVisits": wfivRouteMaxVisits,
       "wfivRouteAreaMaxCost": wfivRouteAreaMaxCost,
       "wfivRouteAreaMaxHops": wfivRouteAreaMaxHops,
       "wfivRouteMaxArea": wfivRouteMaxArea,
       "wfivRouteType": wfivRouteType,
       "wfivCircuitTable": wfivCircuitTable,
       "wfivCircuitEntry": wfivCircuitEntry,
       "wfivCircuitCreateDelete": wfivCircuitCreateDelete,
       "wfivCircuitEnableDisable": wfivCircuitEnableDisable,
       "wfivCircuitCommonState": wfivCircuitCommonState,
       "wfivCircuitArea": wfivCircuitArea,
       "wfivCircuitNodeid": wfivCircuitNodeid,
       "wfivCircuitNodeAddr": wfivCircuitNodeAddr,
       "wfivCircuitID": wfivCircuitID,
       "wfivCircuitCommonType": wfivCircuitCommonType,
       "wfivCircuitExecCost": wfivCircuitExecCost,
       "wfivCircuitExecHelloTimer": wfivCircuitExecHelloTimer,
       "wfivCircuitDesigRouterNodeAddr": wfivCircuitDesigRouterNodeAddr,
       "wfivCircuitMaxRouters": wfivCircuitMaxRouters,
       "wfivCircuitRouterPri": wfivCircuitRouterPri,
       "wfivCircuitCountAgedPktLoss": wfivCircuitCountAgedPktLoss,
       "wfivCircuitCountNodeUnrPktLoss": wfivCircuitCountNodeUnrPktLoss,
       "wfivCircuitCountOutRngePktLoss": wfivCircuitCountOutRngePktLoss,
       "wfivCircuitCountOverSzePktLoss": wfivCircuitCountOverSzePktLoss,
       "wfivCircuitCountPacketFmtErr": wfivCircuitCountPacketFmtErr,
       "wfivCircuitCountPtlRteUpdtLoss": wfivCircuitCountPtlRteUpdtLoss,
       "wfivCircuitCountTransitPksRecd": wfivCircuitCountTransitPksRecd,
       "wfivCircuitCountTransitPkSent": wfivCircuitCountTransitPkSent,
       "wfivCircuitCountRtHelloSent": wfivCircuitCountRtHelloSent,
       "wfivCircuitCountRtHelloRcvd": wfivCircuitCountRtHelloRcvd,
       "wfivCircuitCountHelloSent": wfivCircuitCountHelloSent,
       "wfivCircuitCountHelloRcvd": wfivCircuitCountHelloRcvd,
       "wfivCircuitCountL1UpdSent": wfivCircuitCountL1UpdSent,
       "wfivCircuitCountL1UpdRcvd": wfivCircuitCountL1UpdRcvd,
       "wfivCircuitCountAreaUpdSent": wfivCircuitCountAreaUpdSent,
       "wfivCircuitCountAreaUpdRcvd": wfivCircuitCountAreaUpdRcvd,
       "wfivCircuitCountDropped": wfivCircuitCountDropped,
       "wfivCircuitAllEndnodesMac": wfivCircuitAllEndnodesMac,
       "wfivCircuitAllRoutersMac": wfivCircuitAllRoutersMac,
       "wfivCircuitAllAreaRoutersMac": wfivCircuitAllAreaRoutersMac,
       "wfivCircuitHelloEnableDisable": wfivCircuitHelloEnableDisable,
       "wfivCircuitRtHelloEnableDisable": wfivCircuitRtHelloEnableDisable,
       "wfivCircuitL1UpdateEnableDisable": wfivCircuitL1UpdateEnableDisable,
       "wfivLevel1RouteTable": wfivLevel1RouteTable,
       "wfivLevel1RouteEntry": wfivLevel1RouteEntry,
       "wfivLevel1AreaId": wfivLevel1AreaId,
       "wfivLevel1NodeId": wfivLevel1NodeId,
       "wfivLevel1RouteNodeAddr": wfivLevel1RouteNodeAddr,
       "wfivLevel1RouteCircuitID": wfivLevel1RouteCircuitID,
       "wfivLevel1RouteCost": wfivLevel1RouteCost,
       "wfivLevel1RouteHops": wfivLevel1RouteHops,
       "wfivLevel1RouteNextNode": wfivLevel1RouteNextNode,
       "wfivAreaTable": wfivAreaTable,
       "wfivAreaEntry": wfivAreaEntry,
       "wfivAreaNum": wfivAreaNum,
       "wfivAreaState": wfivAreaState,
       "wfivAreaCost": wfivAreaCost,
       "wfivAreaHops": wfivAreaHops,
       "wfivAreaCircuitID": wfivAreaCircuitID,
       "wfivAreaNextNode": wfivAreaNextNode,
       "wfivAdjTable": wfivAdjTable,
       "wfivAdjEntry": wfivAdjEntry,
       "wfivAdjIndex": wfivAdjIndex,
       "wfivAdjNodeAddr": wfivAdjNodeAddr,
       "wfivAdjBlockSize": wfivAdjBlockSize,
       "wfivAdjListenTimer": wfivAdjListenTimer,
       "wfivAdjCircuitID": wfivAdjCircuitID,
       "wfivAdjType": wfivAdjType,
       "wfivAdjState": wfivAdjState,
       "wfivAdjPriority": wfivAdjPriority,
       "wfivAdjClass": wfivAdjClass,
       "wfivTrafficFilterTable": wfivTrafficFilterTable,
       "wfivTrafficFilterEntry": wfivTrafficFilterEntry,
       "wfivTrafficFilterCreate": wfivTrafficFilterCreate,
       "wfivTrafficFilterEnable": wfivTrafficFilterEnable,
       "wfivTrafficFilterStatus": wfivTrafficFilterStatus,
       "wfivTrafficFilterCounter": wfivTrafficFilterCounter,
       "wfivTrafficFilterDefinition": wfivTrafficFilterDefinition,
       "wfivTrafficFilterReserved": wfivTrafficFilterReserved,
       "wfivTrafficFilterCircuit": wfivTrafficFilterCircuit,
       "wfivTrafficFilterRuleNumber": wfivTrafficFilterRuleNumber,
       "wfivTrafficFilterFragment": wfivTrafficFilterFragment,
       "wfivStaticAdjTable": wfivStaticAdjTable,
       "wfivStaticAdjEntry": wfivStaticAdjEntry,
       "wfivStaticAdjCreateDelete": wfivStaticAdjCreateDelete,
       "wfivStaticAdjEnableDisable": wfivStaticAdjEnableDisable,
       "wfivStaticAdjArea": wfivStaticAdjArea,
       "wfivStaticAdjNodeid": wfivStaticAdjNodeid,
       "wfivStaticAdjCircuitID": wfivStaticAdjCircuitID,
       "wfivStaticAdjNodeAddr": wfivStaticAdjNodeAddr,
       "wfivStaticAdjType": wfivStaticAdjType,
       "wfivStaticAdjPriority": wfivStaticAdjPriority,
       "wfivStaticAdjDestMACAddr": wfivStaticAdjDestMACAddr,
       "wfInternet": wfInternet,
       "wfArpGroup": wfArpGroup,
       "wfArpBase": wfArpBase,
       "wfArpBaseCreate": wfArpBaseCreate,
       "wfArpBaseEnable": wfArpBaseEnable,
       "wfArpBaseForwarding": wfArpBaseForwarding,
       "wfArpIntfTable": wfArpIntfTable,
       "wfArpIntfEntry": wfArpIntfEntry,
       "wfArpCreate": wfArpCreate,
       "wfArpEnable": wfArpEnable,
       "wfArpCctno": wfArpCctno,
       "wfIpRouting": wfIpRouting,
       "wfIpGroup": wfIpGroup,
       "wfIpBase": wfIpBase,
       "wfIpBaseCreate": wfIpBaseCreate,
       "wfIpBaseEnable": wfIpBaseEnable,
       "wfIpBaseState": wfIpBaseState,
       "wfIpBaseForwarding": wfIpBaseForwarding,
       "wfIpBaseDefaultTTL": wfIpBaseDefaultTTL,
       "wfIpBaseRipDiameter": wfIpBaseRipDiameter,
       "wfIpBaseRtEntryTable": wfIpBaseRtEntryTable,
       "wfIpBaseRtEntry": wfIpBaseRtEntry,
       "wfIpBaseRouteDest": wfIpBaseRouteDest,
       "wfIpBaseRouteIfIndex": wfIpBaseRouteIfIndex,
       "wfIpBaseRouteMetric1": wfIpBaseRouteMetric1,
       "wfIpBaseRouteMetric2": wfIpBaseRouteMetric2,
       "wfIpBaseRouteMetric3": wfIpBaseRouteMetric3,
       "wfIpBaseRouteMetric4": wfIpBaseRouteMetric4,
       "wfIpBaseRouteNextHop": wfIpBaseRouteNextHop,
       "wfIpBaseRouteType": wfIpBaseRouteType,
       "wfIpBaseRouteProto": wfIpBaseRouteProto,
       "wfIpBaseRouteAge": wfIpBaseRouteAge,
       "wfIpBaseRouteMask": wfIpBaseRouteMask,
       "wfIpBaseRouteMetric5": wfIpBaseRouteMetric5,
       "wfIpBaseRouteInfo": wfIpBaseRouteInfo,
       "wfIpBaseHostEntryTable": wfIpBaseHostEntryTable,
       "wfIpBaseHostEntry": wfIpBaseHostEntry,
       "wfIpBaseNetToMediaIfIndex": wfIpBaseNetToMediaIfIndex,
       "wfIpBaseNetToMediaPhysAddress": wfIpBaseNetToMediaPhysAddress,
       "wfIpBaseNetToMediaNetAddress": wfIpBaseNetToMediaNetAddress,
       "wfIpBaseNetToMediaType": wfIpBaseNetToMediaType,
       "wfIpInterfaceTable": wfIpInterfaceTable,
       "wfIpInterfaceEntry": wfIpInterfaceEntry,
       "wfIpInterfaceCreate": wfIpInterfaceCreate,
       "wfIpInterfaceEnable": wfIpInterfaceEnable,
       "wfIpInterfaceState": wfIpInterfaceState,
       "wfIpInterfaceAddr": wfIpInterfaceAddr,
       "wfIpInterfaceCircuit": wfIpInterfaceCircuit,
       "wfIpInterfaceMask": wfIpInterfaceMask,
       "wfIpInterfaceCost": wfIpInterfaceCost,
       "wfIpInterfaceCfgBcastAddr": wfIpInterfaceCfgBcastAddr,
       "wfIpInterfaceBcastAddr": wfIpInterfaceBcastAddr,
       "wfIpInterfaceMTUDiscovery": wfIpInterfaceMTUDiscovery,
       "wfIpInterfaceAMR": wfIpInterfaceAMR,
       "wfIpInterfaceASB": wfIpInterfaceASB,
       "wfIpInterfaceAddressResolutionType": wfIpInterfaceAddressResolutionType,
       "wfIpInterfaceProxy": wfIpInterfaceProxy,
       "wfIpInterfaceHostCache": wfIpInterfaceHostCache,
       "wfIpInterfaceUdpXsumOn": wfIpInterfaceUdpXsumOn,
       "wfIpInterfaceCfgMacAddress": wfIpInterfaceCfgMacAddress,
       "wfIpInterfaceMacAddress": wfIpInterfaceMacAddress,
       "wfIpInterfaceReasmMaxSize": wfIpInterfaceReasmMaxSize,
       "wfIpInterfaceMaxInfo": wfIpInterfaceMaxInfo,
       "wfIpInterfaceInReceives": wfIpInterfaceInReceives,
       "wfIpInterfaceInHdrErrors": wfIpInterfaceInHdrErrors,
       "wfIpInterfaceInAddrErrors": wfIpInterfaceInAddrErrors,
       "wfIpInterfaceForwDatagrams": wfIpInterfaceForwDatagrams,
       "wfIpInterfaceInUnknownProtos": wfIpInterfaceInUnknownProtos,
       "wfIpInterfaceInDiscards": wfIpInterfaceInDiscards,
       "wfIpInterfaceInDelivers": wfIpInterfaceInDelivers,
       "wfIpInterfaceOutRequests": wfIpInterfaceOutRequests,
       "wfIpInterfaceOutDiscards": wfIpInterfaceOutDiscards,
       "wfIpInterfaceOutNoRoutes": wfIpInterfaceOutNoRoutes,
       "wfIpInterfaceReasmTimeout": wfIpInterfaceReasmTimeout,
       "wfIpInterfaceReasmReqds": wfIpInterfaceReasmReqds,
       "wfIpInterfaceReasmOKs": wfIpInterfaceReasmOKs,
       "wfIpInterfaceReasmFails": wfIpInterfaceReasmFails,
       "wfIpInterfaceFragOKs": wfIpInterfaceFragOKs,
       "wfIpInterfaceFragFails": wfIpInterfaceFragFails,
       "wfIpInterfaceFragCreates": wfIpInterfaceFragCreates,
       "wfIpInterfaceIcmpInMsgs": wfIpInterfaceIcmpInMsgs,
       "wfIpInterfaceIcmpInErrors": wfIpInterfaceIcmpInErrors,
       "wfIpInterfaceIcmpInDestUnreachs": wfIpInterfaceIcmpInDestUnreachs,
       "wfIpInterfaceIcmpInTimeExcds": wfIpInterfaceIcmpInTimeExcds,
       "wfIpInterfaceIcmpInParmProbs": wfIpInterfaceIcmpInParmProbs,
       "wfIpInterfaceIcmpInSrcQuenchs": wfIpInterfaceIcmpInSrcQuenchs,
       "wfIpInterfaceIcmpInRedirects": wfIpInterfaceIcmpInRedirects,
       "wfIpInterfaceIcmpInEchos": wfIpInterfaceIcmpInEchos,
       "wfIpInterfaceIcmpInEchoReps": wfIpInterfaceIcmpInEchoReps,
       "wfIpInterfaceIcmpInTimestamps": wfIpInterfaceIcmpInTimestamps,
       "wfIpInterfaceIcmpInTimestampReps": wfIpInterfaceIcmpInTimestampReps,
       "wfIpInterfaceIcmpInAddrMasks": wfIpInterfaceIcmpInAddrMasks,
       "wfIpInterfaceIcmpInAddrMaskReps": wfIpInterfaceIcmpInAddrMaskReps,
       "wfIpInterfaceIcmpOutMsgs": wfIpInterfaceIcmpOutMsgs,
       "wfIpInterfaceIcmpOutErrors": wfIpInterfaceIcmpOutErrors,
       "wfIpInterfaceIcmpOutDestUnreachs": wfIpInterfaceIcmpOutDestUnreachs,
       "wfIpInterfaceIcmpOutTimeExcds": wfIpInterfaceIcmpOutTimeExcds,
       "wfIpInterfaceIcmpOutParmProbs": wfIpInterfaceIcmpOutParmProbs,
       "wfIpInterfaceIcmpOutSrcQuenchs": wfIpInterfaceIcmpOutSrcQuenchs,
       "wfIpInterfaceIcmpOutRedirects": wfIpInterfaceIcmpOutRedirects,
       "wfIpInterfaceIcmpOutEchos": wfIpInterfaceIcmpOutEchos,
       "wfIpInterfaceIcmpOutEchoReps": wfIpInterfaceIcmpOutEchoReps,
       "wfIpInterfaceIcmpOutTimestamps": wfIpInterfaceIcmpOutTimestamps,
       "wfIpInterfaceIcmpOutTimestampReps": wfIpInterfaceIcmpOutTimestampReps,
       "wfIpInterfaceIcmpOutAddrMasks": wfIpInterfaceIcmpOutAddrMasks,
       "wfIpInterfaceIcmpOutAddrMaskReps": wfIpInterfaceIcmpOutAddrMaskReps,
       "wfIpInterfaceTrEndStation": wfIpInterfaceTrEndStation,
       "wfIpInterfaceSMDSGroupAddress": wfIpInterfaceSMDSGroupAddress,
       "wfIpInterfaceSMDSArpReqAddress": wfIpInterfaceSMDSArpReqAddress,
       "wfIpInterfaceFRBcastDlci": wfIpInterfaceFRBcastDlci,
       "wfIpInterfaceFRMcast1Dlci": wfIpInterfaceFRMcast1Dlci,
       "wfIpInterfaceFRMcast2Dlci": wfIpInterfaceFRMcast2Dlci,
       "wfIpInterfaceRedirect": wfIpInterfaceRedirect,
       "wfIpInterfaceEnetArpEncaps": wfIpInterfaceEnetArpEncaps,
       "wfIpStaticRouteTable": wfIpStaticRouteTable,
       "wfIpStaticRouteEntry": wfIpStaticRouteEntry,
       "wfIpSrCreate": wfIpSrCreate,
       "wfIpSrEnable": wfIpSrEnable,
       "wfIpSrIpAddress": wfIpSrIpAddress,
       "wfIpSrIpNetMask": wfIpSrIpNetMask,
       "wfIpSrCost": wfIpSrCost,
       "wfIpSrNextHopAddr": wfIpSrNextHopAddr,
       "wfIpSrNextHopMask": wfIpSrNextHopMask,
       "wfIpSrPreference": wfIpSrPreference,
       "wfIpSrIpAddressRt": wfIpSrIpAddressRt,
       "wfIpSrValid": wfIpSrValid,
       "wfIpAdjacentHostTable": wfIpAdjacentHostTable,
       "wfIpAdjacentHostEntry": wfIpAdjacentHostEntry,
       "wfIpAdjHostCreate": wfIpAdjHostCreate,
       "wfIpAdjHostEnable": wfIpAdjHostEnable,
       "wfIpAdjHostIpAddress": wfIpAdjHostIpAddress,
       "wfIpAdjHostIntf": wfIpAdjHostIntf,
       "wfIpAdjHostIntfMask": wfIpAdjHostIntfMask,
       "wfIpAdjHostMacAddr": wfIpAdjHostMacAddr,
       "wfIpAdjHostEncaps": wfIpAdjHostEncaps,
       "wfIpAdjHostValid": wfIpAdjHostValid,
       "wfIpTrafficFilterTable": wfIpTrafficFilterTable,
       "wfIpTrafficFilterEntry": wfIpTrafficFilterEntry,
       "wfIpTrafficFilterCreate": wfIpTrafficFilterCreate,
       "wfIpTrafficFilterEnable": wfIpTrafficFilterEnable,
       "wfIpTrafficFilterStatus": wfIpTrafficFilterStatus,
       "wfIpTrafficFilterCounter": wfIpTrafficFilterCounter,
       "wfIpTrafficFilterDefinition": wfIpTrafficFilterDefinition,
       "wfIpTrafficFilterReserved": wfIpTrafficFilterReserved,
       "wfIpTrafficFilterInterface": wfIpTrafficFilterInterface,
       "wfIpTrafficFilterCircuit": wfIpTrafficFilterCircuit,
       "wfIpTrafficFilterRuleNumber": wfIpTrafficFilterRuleNumber,
       "wfIpTrafficFilterFragment": wfIpTrafficFilterFragment,
       "wfIpRfRipImportTable": wfIpRfRipImportTable,
       "wfIpRfRipImportEntry": wfIpRfRipImportEntry,
       "wfIpRfRipImportCreate": wfIpRfRipImportCreate,
       "wfIpRfRipImportEnable": wfIpRfRipImportEnable,
       "wfIpRfRipImportAddress": wfIpRfRipImportAddress,
       "wfIpRfRipImportMask": wfIpRfRipImportMask,
       "wfIpRfRipImportAction": wfIpRfRipImportAction,
       "wfIpRfRipImportPreference": wfIpRfRipImportPreference,
       "wfIpRfRipImportRipGateway": wfIpRfRipImportRipGateway,
       "wfIpRfRipImportRipInterface": wfIpRfRipImportRipInterface,
       "wfIpRfRipExportTable": wfIpRfRipExportTable,
       "wfIpRfRipExportEntry": wfIpRfRipExportEntry,
       "wfIpRfRipExportCreate": wfIpRfRipExportCreate,
       "wfIpRfRipExportEnable": wfIpRfRipExportEnable,
       "wfIpRfRipExportAddress": wfIpRfRipExportAddress,
       "wfIpRfRipExportMask": wfIpRfRipExportMask,
       "wfIpRfRipExportFromProtocol": wfIpRfRipExportFromProtocol,
       "wfIpRfRipExportAction": wfIpRfRipExportAction,
       "wfIpRfRipExportInterface": wfIpRfRipExportInterface,
       "wfIpRfRipExportRipMetric": wfIpRfRipExportRipMetric,
       "wfIpRfOspfImportTable": wfIpRfOspfImportTable,
       "wfIpRfOspfImportEntry": wfIpRfOspfImportEntry,
       "wfIpRfOspfImportCreate": wfIpRfOspfImportCreate,
       "wfIpRfOspfImportEnable": wfIpRfOspfImportEnable,
       "wfIpRfOspfImportAddress": wfIpRfOspfImportAddress,
       "wfIpRfOspfImportMask": wfIpRfOspfImportMask,
       "wfIpRfOspfImportAction": wfIpRfOspfImportAction,
       "wfIpRfOspfImportPreference": wfIpRfOspfImportPreference,
       "wfIpRfOspfImportType": wfIpRfOspfImportType,
       "wfIpRfOspfImportTag": wfIpRfOspfImportTag,
       "wfIpRfOspfExportTable": wfIpRfOspfExportTable,
       "wfIpRfOspfExportEntry": wfIpRfOspfExportEntry,
       "wfIpRfOspfExportCreate": wfIpRfOspfExportCreate,
       "wfIpRfOspfExportEnable": wfIpRfOspfExportEnable,
       "wfIpRfOspfExportAddress": wfIpRfOspfExportAddress,
       "wfIpRfOspfExportMask": wfIpRfOspfExportMask,
       "wfIpRfOspfExportFromProtocol": wfIpRfOspfExportFromProtocol,
       "wfIpRfOspfExportAction": wfIpRfOspfExportAction,
       "wfIpRfOspfExportType": wfIpRfOspfExportType,
       "wfIpRfOspfExportTag": wfIpRfOspfExportTag,
       "wfRipGroup": wfRipGroup,
       "wfRipIntfTable": wfRipIntfTable,
       "wfRipIntfEntry": wfRipIntfEntry,
       "wfRipInterfaceCreate": wfRipInterfaceCreate,
       "wfRipInterfaceEnable": wfRipInterfaceEnable,
       "wfRipInterfaceState": wfRipInterfaceState,
       "wfRipInterfaceIndex": wfRipInterfaceIndex,
       "wfRipInterfaceSupply": wfRipInterfaceSupply,
       "wfRipInterfaceListen": wfRipInterfaceListen,
       "wfRipInterfaceDefaultRouteSupply": wfRipInterfaceDefaultRouteSupply,
       "wfRipInterfaceDefaultRouteListen": wfRipInterfaceDefaultRouteListen,
       "wfRipInterfacePoisonedReversed": wfRipInterfacePoisonedReversed,
       "wfOspfGroup": wfOspfGroup,
       "wfOspfGeneralGroup": wfOspfGeneralGroup,
       "wfOspfGeneralDelete": wfOspfGeneralDelete,
       "wfOspfGeneralDisable": wfOspfGeneralDisable,
       "wfOspfGeneralState": wfOspfGeneralState,
       "wfOspfRouterId": wfOspfRouterId,
       "wfOspfVersionNumber": wfOspfVersionNumber,
       "wfOspfAreaBdrRtrStatus": wfOspfAreaBdrRtrStatus,
       "wfOspfASBdrRtrStatus": wfOspfASBdrRtrStatus,
       "wfOspfTOSSupport": wfOspfTOSSupport,
       "wfOspfSpfHoldDown": wfOspfSpfHoldDown,
       "wfOspfSlotMask": wfOspfSlotMask,
       "wfOspfAreaTable": wfOspfAreaTable,
       "wfOspfAreaEntry": wfOspfAreaEntry,
       "wfOspfAreaDelete": wfOspfAreaDelete,
       "wfOspfAreaDisable": wfOspfAreaDisable,
       "wfOspfAreaState": wfOspfAreaState,
       "wfOspfAreaId": wfOspfAreaId,
       "wfOspfAuthType": wfOspfAuthType,
       "wfOspfImportASExtern": wfOspfImportASExtern,
       "wfOspfStubMetric": wfOspfStubMetric,
       "wfOspfImportSum": wfOspfImportSum,
       "wfOspfLsdbTable": wfOspfLsdbTable,
       "wfOspfLsdbEntry": wfOspfLsdbEntry,
       "wfOspfLsdbAreaId": wfOspfLsdbAreaId,
       "wfOspfLsdbType": wfOspfLsdbType,
       "wfOspfLsdbLSID": wfOspfLsdbLSID,
       "wfOspfLsdbRouterId": wfOspfLsdbRouterId,
       "wfOspfLsdbSequence": wfOspfLsdbSequence,
       "wfOspfLsdbAge": wfOspfLsdbAge,
       "wfOspfLsdbChecksum": wfOspfLsdbChecksum,
       "wfOspfLsdbAdvLen": wfOspfLsdbAdvLen,
       "wfOspfAreaRangeTable": wfOspfAreaRangeTable,
       "wfOspfAreaRangeEntry": wfOspfAreaRangeEntry,
       "wfOspfAreaRangeDelete": wfOspfAreaRangeDelete,
       "wfOspfAreaRangeDisable": wfOspfAreaRangeDisable,
       "wfOspfAreaRangeState": wfOspfAreaRangeState,
       "wfOspfAreaRangeAreaID": wfOspfAreaRangeAreaID,
       "wfOspfAreaRangeNet": wfOspfAreaRangeNet,
       "wfOspfAreaRangeMask": wfOspfAreaRangeMask,
       "wfOspfIfTable": wfOspfIfTable,
       "wfOspfIfEntry": wfOspfIfEntry,
       "wfOspfIfDelete": wfOspfIfDelete,
       "wfOspfIfDisable": wfOspfIfDisable,
       "wfOspfIfState": wfOspfIfState,
       "wfOspfIfIpAddress": wfOspfIfIpAddress,
       "wfOspfAddressLessIf": wfOspfAddressLessIf,
       "wfOspfIfAreaId": wfOspfIfAreaId,
       "wfOspfIfType": wfOspfIfType,
       "wfOspfIfRtrPriority": wfOspfIfRtrPriority,
       "wfOspfIfTransitDelay": wfOspfIfTransitDelay,
       "wfOspfIfRetransInterval": wfOspfIfRetransInterval,
       "wfOspfIfHelloInterval": wfOspfIfHelloInterval,
       "wfOspfIfRtrDeadInterval": wfOspfIfRtrDeadInterval,
       "wfOspfIfPollInterval": wfOspfIfPollInterval,
       "wfOspfIfDesignatedRouter": wfOspfIfDesignatedRouter,
       "wfOspfIfBackupDesignatedRouter": wfOspfIfBackupDesignatedRouter,
       "wfOspfIfMetricCost": wfOspfIfMetricCost,
       "wfOspfIfAuthKey": wfOspfIfAuthKey,
       "wfOspfIfTxHellos": wfOspfIfTxHellos,
       "wfOspfIfTxDBDescripts": wfOspfIfTxDBDescripts,
       "wfOspfIfTxLinkStateReqs": wfOspfIfTxLinkStateReqs,
       "wfOspfIfTxLinkStateUpds": wfOspfIfTxLinkStateUpds,
       "wfOspfIfTxLinkStateAcks": wfOspfIfTxLinkStateAcks,
       "wfOspfIfRxHellos": wfOspfIfRxHellos,
       "wfOspfIfRxDBDescripts": wfOspfIfRxDBDescripts,
       "wfOspfIfRxLinkStateReqs": wfOspfIfRxLinkStateReqs,
       "wfOspfIfRxLinkStateUpds": wfOspfIfRxLinkStateUpds,
       "wfOspfIfRxLinkStateAcks": wfOspfIfRxLinkStateAcks,
       "wfOspfIfDrops": wfOspfIfDrops,
       "wfOspfVirtIfTable": wfOspfVirtIfTable,
       "wfOspfVirtIfEntry": wfOspfVirtIfEntry,
       "wfOspfVirtIfDelete": wfOspfVirtIfDelete,
       "wfOspfVirtIfDisable": wfOspfVirtIfDisable,
       "wfOspfVirtIfState": wfOspfVirtIfState,
       "wfOspfVirtIfAreaID": wfOspfVirtIfAreaID,
       "wfOspfVirtIfNeighbor": wfOspfVirtIfNeighbor,
       "wfOspfVirtIfTransitDelay": wfOspfVirtIfTransitDelay,
       "wfOspfVirtIfRetransInterval": wfOspfVirtIfRetransInterval,
       "wfOspfVirtIfHelloInterval": wfOspfVirtIfHelloInterval,
       "wfOspfVirtIfRtrDeadInterval": wfOspfVirtIfRtrDeadInterval,
       "wfOspfVirtIfAuthKey": wfOspfVirtIfAuthKey,
       "wfOspfVirtIfTxHellos": wfOspfVirtIfTxHellos,
       "wfOspfVirtIfTxDBDescripts": wfOspfVirtIfTxDBDescripts,
       "wfOspfVirtIfTxLinkStateReqs": wfOspfVirtIfTxLinkStateReqs,
       "wfOspfVirtIfTxLinkStateUpds": wfOspfVirtIfTxLinkStateUpds,
       "wfOspfVirtIfTxLinkStateAcks": wfOspfVirtIfTxLinkStateAcks,
       "wfOspfVirtIfRxHellos": wfOspfVirtIfRxHellos,
       "wfOspfVirtIfRxDBDescripts": wfOspfVirtIfRxDBDescripts,
       "wfOspfVirtIfRxLinkStateReqs": wfOspfVirtIfRxLinkStateReqs,
       "wfOspfVirtIfRxLinkStateUpds": wfOspfVirtIfRxLinkStateUpds,
       "wfOspfVirtIfRxLinkStateAcks": wfOspfVirtIfRxLinkStateAcks,
       "wfOspfVirtIfDrops": wfOspfVirtIfDrops,
       "wfOspfNbrTable": wfOspfNbrTable,
       "wfOspfNbrEntry": wfOspfNbrEntry,
       "wfOspfNbrDelete": wfOspfNbrDelete,
       "wfOspfNbrDisable": wfOspfNbrDisable,
       "wfOspfNbrState": wfOspfNbrState,
       "wfOspfNbrIpAddr": wfOspfNbrIpAddr,
       "wfOspfNbrIfAddr": wfOspfNbrIfAddr,
       "wfOspfNbrAddressLessIndex": wfOspfNbrAddressLessIndex,
       "wfOspfNbrRtrId": wfOspfNbrRtrId,
       "wfOspfNbrOptions": wfOspfNbrOptions,
       "wfOspfNbrPriority": wfOspfNbrPriority,
       "wfOspfNbrEvents": wfOspfNbrEvents,
       "wfOspfNbrLSRetransQLen": wfOspfNbrLSRetransQLen,
       "wfOspfVirtNbrTable": wfOspfVirtNbrTable,
       "wfOspfVirtNbrEntry": wfOspfVirtNbrEntry,
       "wfOspfVirtNbrArea": wfOspfVirtNbrArea,
       "wfOspfVirtNbrRtrId": wfOspfVirtNbrRtrId,
       "wfOspfVirtNbrIpAddr": wfOspfVirtNbrIpAddr,
       "wfOspfVirtNbrOptions": wfOspfVirtNbrOptions,
       "wfOspfVirtNbrState": wfOspfVirtNbrState,
       "wfOspfVirtNbrEvents": wfOspfVirtNbrEvents,
       "wfOspfVirtNbrLSRetransQLen": wfOspfVirtNbrLSRetransQLen,
       "wfOspfDynNbrTable": wfOspfDynNbrTable,
       "wfOspfDynNbrEntry": wfOspfDynNbrEntry,
       "wfOspfDynNbrState": wfOspfDynNbrState,
       "wfOspfDynNbrIpAddr": wfOspfDynNbrIpAddr,
       "wfOspfDynNbrIfAddr": wfOspfDynNbrIfAddr,
       "wfOspfDynNbrAddressLessIndex": wfOspfDynNbrAddressLessIndex,
       "wfOspfDynNbrRtrId": wfOspfDynNbrRtrId,
       "wfOspfDynNbrOptions": wfOspfDynNbrOptions,
       "wfOspfDynNbrPriority": wfOspfDynNbrPriority,
       "wfOspfDynNbrEvents": wfOspfDynNbrEvents,
       "wfOspfDynNbrLSRetransQLen": wfOspfDynNbrLSRetransQLen,
       "wfEgpGroup": wfEgpGroup,
       "wfBgpGroup": wfBgpGroup,
       "wfTcpGroup": wfTcpGroup,
       "wfUdpGroup": wfUdpGroup,
       "wfSnmpGroup": wfSnmpGroup,
       "wfSnmp": wfSnmp,
       "wfSnmpDisable": wfSnmpDisable,
       "wfSnmpUseLock": wfSnmpUseLock,
       "wfSnmpLockAddress": wfSnmpLockAddress,
       "wfSnmpLockTimeOut": wfSnmpLockTimeOut,
       "wfSnmpAuth": wfSnmpAuth,
       "wfSnmpInPkts": wfSnmpInPkts,
       "wfSnmpOutPkts": wfSnmpOutPkts,
       "wfSnmpInBadVersions": wfSnmpInBadVersions,
       "wfSnmpInBadCommunityNames": wfSnmpInBadCommunityNames,
       "wfSnmpInBadCommunityUses": wfSnmpInBadCommunityUses,
       "wfSnmpInASNParseErrs": wfSnmpInASNParseErrs,
       "wfSnmpInBadTypes": wfSnmpInBadTypes,
       "wfSnmpInTooBigs": wfSnmpInTooBigs,
       "wfSnmpInNoSuchNames": wfSnmpInNoSuchNames,
       "wfSnmpInBadValues": wfSnmpInBadValues,
       "wfSnmpInReadOnlys": wfSnmpInReadOnlys,
       "wfSnmpInGenErrs": wfSnmpInGenErrs,
       "wfSnmpInTotalReqVars": wfSnmpInTotalReqVars,
       "wfSnmpInTotalSetVars": wfSnmpInTotalSetVars,
       "wfSnmpInGetRequests": wfSnmpInGetRequests,
       "wfSnmpInGetNexts": wfSnmpInGetNexts,
       "wfSnmpInSetRequests": wfSnmpInSetRequests,
       "wfSnmpInGetResponses": wfSnmpInGetResponses,
       "wfSnmpInTraps": wfSnmpInTraps,
       "wfSnmpOutTooBigs": wfSnmpOutTooBigs,
       "wfSnmpOutNoSuchNames": wfSnmpOutNoSuchNames,
       "wfSnmpOutBadValues": wfSnmpOutBadValues,
       "wfSnmpOutReadOnlys": wfSnmpOutReadOnlys,
       "wfSnmpOutGenErrs": wfSnmpOutGenErrs,
       "wfSnmpOutGetRequests": wfSnmpOutGetRequests,
       "wfSnmpOutGetNexts": wfSnmpOutGetNexts,
       "wfSnmpOutSetRequests": wfSnmpOutSetRequests,
       "wfSnmpOutGetResponses": wfSnmpOutGetResponses,
       "wfSnmpOutTraps": wfSnmpOutTraps,
       "wfSnmpEnableAuthTraps": wfSnmpEnableAuthTraps,
       "wfSnmpTrapDebug": wfSnmpTrapDebug,
       "wfSnmpTrapTrace": wfSnmpTrapTrace,
       "wfSnmpTrapInfo": wfSnmpTrapInfo,
       "wfSnmpTrapWarn": wfSnmpTrapWarn,
       "wfSnmpTrapFault": wfSnmpTrapFault,
       "wfSnmpCommTable": wfSnmpCommTable,
       "wfSnmpCommEntry": wfSnmpCommEntry,
       "wfSnmpCommDelete": wfSnmpCommDelete,
       "wfSnmpCommIndex": wfSnmpCommIndex,
       "wfSnmpCommName": wfSnmpCommName,
       "wfSnmpCommAccess": wfSnmpCommAccess,
       "wfSnmpMgrTable": wfSnmpMgrTable,
       "wfSnmpMgrEntry": wfSnmpMgrEntry,
       "wfSnmpMgrDelete": wfSnmpMgrDelete,
       "wfSnmpMgrCommIndex": wfSnmpMgrCommIndex,
       "wfSnmpMgrAddress": wfSnmpMgrAddress,
       "wfSnmpMgrName": wfSnmpMgrName,
       "wfSnmpMgrTrapPort": wfSnmpMgrTrapPort,
       "wfSnmpMgrTraps": wfSnmpMgrTraps,
       "wfFakeEvent": wfFakeEvent,
       "wfFakeEventString": wfFakeEventString,
       "wfTftp": wfTftp,
       "wfTftpDisable": wfTftpDisable,
       "wfTftpDefaultVolume": wfTftpDefaultVolume,
       "wfTftpXfers": wfTftpXfers,
       "wfTftpTimeOut": wfTftpTimeOut,
       "wfTftpCloseTimeOut": wfTftpCloseTimeOut,
       "wfTftpRexmit": wfTftpRexmit,
       "wfTftpInFiles": wfTftpInFiles,
       "wfTftpOutFiles": wfTftpOutFiles,
       "wfTftpInWRQ": wfTftpInWRQ,
       "wfTftpOutWRQ": wfTftpOutWRQ,
       "wfTftpInRRQ": wfTftpInRRQ,
       "wfTftpOutRRQ": wfTftpOutRRQ,
       "wfTftpRexmitPkts": wfTftpRexmitPkts,
       "wfTftpInErr": wfTftpInErr,
       "wfTftpOutErr": wfTftpOutErr,
       "wfTftpAborts": wfTftpAborts,
       "wfTelnetGroup": wfTelnetGroup,
       "wfBootpGroup": wfBootpGroup,
       "wfAppletalkGroup": wfAppletalkGroup,
       "wfAppleBase": wfAppleBase,
       "wfAppleBaseDelete": wfAppleBaseDelete,
       "wfAppleBaseDisable": wfAppleBaseDisable,
       "wfAppleBaseState": wfAppleBaseState,
       "wfAppleBaseDebugLevel": wfAppleBaseDebugLevel,
       "wfAppleBaseDdpQueLen": wfAppleBaseDdpQueLen,
       "wfAppleBaseHomedPort": wfAppleBaseHomedPort,
       "wfAppleBaseTotalNets": wfAppleBaseTotalNets,
       "wfAppleBaseTotalZones": wfAppleBaseTotalZones,
       "wfAppleRtmpTable": wfAppleRtmpTable,
       "wfAppleRtmpEntry": wfAppleRtmpEntry,
       "wfAppleRtmpNetStart": wfAppleRtmpNetStart,
       "wfAppleRtmpNetEnd": wfAppleRtmpNetEnd,
       "wfAppleRtmpPort": wfAppleRtmpPort,
       "wfAppleRtmpHops": wfAppleRtmpHops,
       "wfAppleRtmpNextHopNet": wfAppleRtmpNextHopNet,
       "wfAppleRtmpNextHopNode": wfAppleRtmpNextHopNode,
       "wfAppleRtmpState": wfAppleRtmpState,
       "wfApplePortTable": wfApplePortTable,
       "wfApplePortEntry": wfApplePortEntry,
       "wfApplePortDelete": wfApplePortDelete,
       "wfApplePortDisable": wfApplePortDisable,
       "wfApplePortCircuit": wfApplePortCircuit,
       "wfApplePortState": wfApplePortState,
       "wfApplePortType": wfApplePortType,
       "wfApplePortCksumDisable": wfApplePortCksumDisable,
       "wfApplePortTrEndStation": wfApplePortTrEndStation,
       "wfApplePortGniForever": wfApplePortGniForever,
       "wfApplePortAarpFlush": wfApplePortAarpFlush,
       "wfApplePortMacAddress": wfApplePortMacAddress,
       "wfApplePortNodeId": wfApplePortNodeId,
       "wfApplePortNetwork": wfApplePortNetwork,
       "wfApplePortNetStart": wfApplePortNetStart,
       "wfApplePortNetEnd": wfApplePortNetEnd,
       "wfApplePortDfltZone": wfApplePortDfltZone,
       "wfApplePortCurMacAddress": wfApplePortCurMacAddress,
       "wfApplePortCurNodeId": wfApplePortCurNodeId,
       "wfApplePortCurNetwork": wfApplePortCurNetwork,
       "wfApplePortCurNetStart": wfApplePortCurNetStart,
       "wfApplePortCurNetEnd": wfApplePortCurNetEnd,
       "wfApplePortCurDfltZone": wfApplePortCurDfltZone,
       "wfApplePortAarpProbeRxs": wfApplePortAarpProbeRxs,
       "wfApplePortAarpProbeTxs": wfApplePortAarpProbeTxs,
       "wfApplePortAarpReqRxs": wfApplePortAarpReqRxs,
       "wfApplePortAarpReqTxs": wfApplePortAarpReqTxs,
       "wfApplePortAarpRspRxs": wfApplePortAarpRspRxs,
       "wfApplePortAarpRspTxs": wfApplePortAarpRspTxs,
       "wfApplePortDdpOutRequests": wfApplePortDdpOutRequests,
       "wfApplePortDdpInReceives": wfApplePortDdpInReceives,
       "wfApplePortDdpInLocalDatagrams": wfApplePortDdpInLocalDatagrams,
       "wfApplePortDdpNoProtocolHandlers": wfApplePortDdpNoProtocolHandlers,
       "wfApplePortDdpTooShortErrors": wfApplePortDdpTooShortErrors,
       "wfApplePortDdpTooLongErrors": wfApplePortDdpTooLongErrors,
       "wfApplePortDdpChecksumErrors": wfApplePortDdpChecksumErrors,
       "wfApplePortDdpForwRequests": wfApplePortDdpForwRequests,
       "wfApplePortDdpOutNoRoutes": wfApplePortDdpOutNoRoutes,
       "wfApplePortDdpBroadcastErrors": wfApplePortDdpBroadcastErrors,
       "wfApplePortDdpHopCountErrors": wfApplePortDdpHopCountErrors,
       "wfApplePortRtmpInDataPkts": wfApplePortRtmpInDataPkts,
       "wfApplePortRtmpOutDataPkts": wfApplePortRtmpOutDataPkts,
       "wfApplePortRtmpInRequestPkts": wfApplePortRtmpInRequestPkts,
       "wfApplePortRtmpNextIREqualChanges": wfApplePortRtmpNextIREqualChanges,
       "wfApplePortRtmpNextIRLessChanges": wfApplePortRtmpNextIRLessChanges,
       "wfApplePortRtmpRouteDeletes": wfApplePortRtmpRouteDeletes,
       "wfApplePortRtmpNetworkMismatchErrors": wfApplePortRtmpNetworkMismatchErrors,
       "wfApplePortRtmpRoutingTableOverflows": wfApplePortRtmpRoutingTableOverflows,
       "wfApplePortZipInZipQueries": wfApplePortZipInZipQueries,
       "wfApplePortZipInZipReplies": wfApplePortZipInZipReplies,
       "wfApplePortZipOutZipReplies": wfApplePortZipOutZipReplies,
       "wfApplePortZipInZipExtendedReplies": wfApplePortZipInZipExtendedReplies,
       "wfApplePortZipOutZipExtendedReplies": wfApplePortZipOutZipExtendedReplies,
       "wfApplePortZipInGetZoneLists": wfApplePortZipInGetZoneLists,
       "wfApplePortZipOutGetZoneListReplies": wfApplePortZipOutGetZoneListReplies,
       "wfApplePortZipInGetLocalZones": wfApplePortZipInGetLocalZones,
       "wfApplePortZipOutGetLocalZoneReplies": wfApplePortZipOutGetLocalZoneReplies,
       "wfApplePortZipInGetMyZones": wfApplePortZipInGetMyZones,
       "wfApplePortZipOutGetMyZoneReplies": wfApplePortZipOutGetMyZoneReplies,
       "wfApplePortZipZoneConflictErrors": wfApplePortZipZoneConflictErrors,
       "wfApplePortZipInGetNetInfos": wfApplePortZipInGetNetInfos,
       "wfApplePortZipOutGetNetInfoReplies": wfApplePortZipOutGetNetInfoReplies,
       "wfApplePortZipZoneOutInvalids": wfApplePortZipZoneOutInvalids,
       "wfApplePortZipAddressInvalids": wfApplePortZipAddressInvalids,
       "wfApplePortZipOutGetNetInfos": wfApplePortZipOutGetNetInfos,
       "wfApplePortZipInGetNetInfoReplies": wfApplePortZipInGetNetInfoReplies,
       "wfApplePortZipOutZipQueries": wfApplePortZipOutZipQueries,
       "wfApplePortZipInErrors": wfApplePortZipInErrors,
       "wfApplePortNbpInLookUpRequests": wfApplePortNbpInLookUpRequests,
       "wfApplePortNbpInLookUpReplies": wfApplePortNbpInLookUpReplies,
       "wfApplePortNbpInBroadcastRequests": wfApplePortNbpInBroadcastRequests,
       "wfApplePortNbpInForwardRequests": wfApplePortNbpInForwardRequests,
       "wfApplePortNbpOutLookUpRequests": wfApplePortNbpOutLookUpRequests,
       "wfApplePortNbpOutLookUpReplies": wfApplePortNbpOutLookUpReplies,
       "wfApplePortNbpOutBroadcastRequests": wfApplePortNbpOutBroadcastRequests,
       "wfApplePortNbpOutForwardRequests": wfApplePortNbpOutForwardRequests,
       "wfApplePortNbpRegistrationFailures": wfApplePortNbpRegistrationFailures,
       "wfApplePortNbpInErrors": wfApplePortNbpInErrors,
       "wfApplePortEchoRequests": wfApplePortEchoRequests,
       "wfApplePortEchoReplies": wfApplePortEchoReplies,
       "wfAppleLclZoneTable": wfAppleLclZoneTable,
       "wfAppleLclZoneEntry": wfAppleLclZoneEntry,
       "wfAppleLclZoneDelete": wfAppleLclZoneDelete,
       "wfAppleLclZonePortCircuit": wfAppleLclZonePortCircuit,
       "wfAppleLclZoneIndex": wfAppleLclZoneIndex,
       "wfAppleLclZoneName": wfAppleLclZoneName,
       "wfAppleAarpTable": wfAppleAarpTable,
       "wfAppleAarpEntry": wfAppleAarpEntry,
       "wfAppleAarpIfIndex": wfAppleAarpIfIndex,
       "wfAppleAarpNet": wfAppleAarpNet,
       "wfAppleAarpNode": wfAppleAarpNode,
       "wfAppleAarpPhysAddress": wfAppleAarpPhysAddress,
       "wfAppleZipTable": wfAppleZipTable,
       "wfAppleZipEntry": wfAppleZipEntry,
       "wfAppleZipZoneNetStart": wfAppleZipZoneNetStart,
       "wfAppleZipZoneNetEnd": wfAppleZipZoneNetEnd,
       "wfAppleZipIndex": wfAppleZipIndex,
       "wfAppleZipZoneName": wfAppleZipZoneName,
       "wfAppleZipZoneState": wfAppleZipZoneState,
       "wfIpxGroup": wfIpxGroup,
       "wfIpxBase": wfIpxBase,
       "wfIpxBaseDelete": wfIpxBaseDelete,
       "wfIpxBaseDisable": wfIpxBaseDisable,
       "wfIpxBaseState": wfIpxBaseState,
       "wfIpxBaseCfgHostNumber": wfIpxBaseCfgHostNumber,
       "wfIpxBaseActiveHostNumber": wfIpxBaseActiveHostNumber,
       "wfIpxBaseNetCount": wfIpxBaseNetCount,
       "wfIpxBaseServiceCount": wfIpxBaseServiceCount,
       "wfIpxBaseLogFilter": wfIpxBaseLogFilter,
       "wfIpxBaseNetTblSize": wfIpxBaseNetTblSize,
       "wfIpxBaseRtEntryTable": wfIpxBaseRtEntryTable,
       "wfIpxBaseRtEntry": wfIpxBaseRtEntry,
       "wfIpxBaseRouteDest": wfIpxBaseRouteDest,
       "wfIpxBaseRouteIfIndex": wfIpxBaseRouteIfIndex,
       "wfIpxBaseRouteMetric": wfIpxBaseRouteMetric,
       "wfIpxBaseRouteNextHopNetwork": wfIpxBaseRouteNextHopNetwork,
       "wfIpxBaseRouteNextHopHost": wfIpxBaseRouteNextHopHost,
       "wfIpxBaseRouteType": wfIpxBaseRouteType,
       "wfIpxBaseRouteProto": wfIpxBaseRouteProto,
       "wfIpxBaseRouteAge": wfIpxBaseRouteAge,
       "wfIpxBaseRouteInfo": wfIpxBaseRouteInfo,
       "wfIpxBaseSapEntryTable": wfIpxBaseSapEntryTable,
       "wfIpxBaseSapEntry": wfIpxBaseSapEntry,
       "wfIpxBaseSapType": wfIpxBaseSapType,
       "wfIpxBaseSapNetwork": wfIpxBaseSapNetwork,
       "wfIpxBaseSapHost": wfIpxBaseSapHost,
       "wfIpxBaseSapSocket": wfIpxBaseSapSocket,
       "wfIpxBaseSapName": wfIpxBaseSapName,
       "wfIpxBaseSapAge": wfIpxBaseSapAge,
       "wfIpxBaseSapHops": wfIpxBaseSapHops,
       "wfIpxBaseSapIndex": wfIpxBaseSapIndex,
       "wfIpxBaseSapIntf": wfIpxBaseSapIntf,
       "wfIpxInterfaceTable": wfIpxInterfaceTable,
       "wfIpxInterfaceEntry": wfIpxInterfaceEntry,
       "wfIpxInterfaceIndex": wfIpxInterfaceIndex,
       "wfIpxInterfaceDelete": wfIpxInterfaceDelete,
       "wfIpxInterfaceDisable": wfIpxInterfaceDisable,
       "wfIpxInterfaceState": wfIpxInterfaceState,
       "wfIpxInterfaceCircuit": wfIpxInterfaceCircuit,
       "wfIpxInterfaceNetworkNumber": wfIpxInterfaceNetworkNumber,
       "wfIpxInterfaceCost": wfIpxInterfaceCost,
       "wfIpxInterfaceXsumOn": wfIpxInterfaceXsumOn,
       "wfIpxInterfaceCfgEncaps": wfIpxInterfaceCfgEncaps,
       "wfIpxInterfaceMacAddress": wfIpxInterfaceMacAddress,
       "wfIpxInterfaceSMDSGroupAddress": wfIpxInterfaceSMDSGroupAddress,
       "wfIpxInterfaceMaxInfo": wfIpxInterfaceMaxInfo,
       "wfIpxInterfaceInReceives": wfIpxInterfaceInReceives,
       "wfIpxInterfaceInHdrErrors": wfIpxInterfaceInHdrErrors,
       "wfIpxInterfaceInAddrErrors": wfIpxInterfaceInAddrErrors,
       "wfIpxInterfaceForwDatagrams": wfIpxInterfaceForwDatagrams,
       "wfIpxInterfaceInUnknownProtos": wfIpxInterfaceInUnknownProtos,
       "wfIpxInterfaceInDiscards": wfIpxInterfaceInDiscards,
       "wfIpxInterfaceInDelivers": wfIpxInterfaceInDelivers,
       "wfIpxInterfaceOutRequests": wfIpxInterfaceOutRequests,
       "wfIpxInterfaceOutDiscards": wfIpxInterfaceOutDiscards,
       "wfIpxInterfaceOutNoRoutes": wfIpxInterfaceOutNoRoutes,
       "wfIpxInterfaceTrEndStation": wfIpxInterfaceTrEndStation,
       "wfIpxInterfaceNetbiosAccept": wfIpxInterfaceNetbiosAccept,
       "wfIpxInterfaceNetbiosDeliver": wfIpxInterfaceNetbiosDeliver,
       "wfIpxInterfaceWanSapPeriod": wfIpxInterfaceWanSapPeriod,
       "wfIpxInterfaceFRBcast": wfIpxInterfaceFRBcast,
       "wfIpxInterfaceFRMcast": wfIpxInterfaceFRMcast,
       "wfIpxInterfaceEncaps": wfIpxInterfaceEncaps,
       "wfIpxInterfaceSplit": wfIpxInterfaceSplit,
       "wfIpxInterfaceCacheHit": wfIpxInterfaceCacheHit,
       "wfIpxRipIntfTable": wfIpxRipIntfTable,
       "wfIpxRipIntfEntry": wfIpxRipIntfEntry,
       "wfIpxRipInterfaceDelete": wfIpxRipInterfaceDelete,
       "wfIpxRipInterfaceDisable": wfIpxRipInterfaceDisable,
       "wfIpxRipInterfaceState": wfIpxRipInterfaceState,
       "wfIpxRipInterfaceIndex": wfIpxRipInterfaceIndex,
       "wfIpxRipInterfaceSupply": wfIpxRipInterfaceSupply,
       "wfIpxRipInterfaceListen": wfIpxRipInterfaceListen,
       "wfIpxAdjacentHostTable": wfIpxAdjacentHostTable,
       "wfIpxAdjacentHostEntry": wfIpxAdjacentHostEntry,
       "wfIpxAhDelete": wfIpxAhDelete,
       "wfIpxAhDisable": wfIpxAhDisable,
       "wfIpxAhTargHostNetwork": wfIpxAhTargHostNetwork,
       "wfIpxAhTargHostId": wfIpxAhTargHostId,
       "wfIpxAhNextHopIntf": wfIpxAhNextHopIntf,
       "wfIpxAhDlci": wfIpxAhDlci,
       "wfIpxStaticRouteTable": wfIpxStaticRouteTable,
       "wfIpxStaticRouteEntry": wfIpxStaticRouteEntry,
       "wfIpxSrDelete": wfIpxSrDelete,
       "wfIpxSrDisable": wfIpxSrDisable,
       "wfIpxSrTargNetwork": wfIpxSrTargNetwork,
       "wfIpxSrCost": wfIpxSrCost,
       "wfIpxSrNextHopNetwork": wfIpxSrNextHopNetwork,
       "wfIpxSrNextHopHost": wfIpxSrNextHopHost,
       "wfIpxSrTargNetworkRt": wfIpxSrTargNetworkRt,
       "wfIpxNetBiosStaticRouteTable": wfIpxNetBiosStaticRouteTable,
       "wfIpxNetBiosStaticRouteEntry": wfIpxNetBiosStaticRouteEntry,
       "wfIpxNetBiosSrDelete": wfIpxNetBiosSrDelete,
       "wfIpxNetBiosSrDisable": wfIpxNetBiosSrDisable,
       "wfIpxNetBiosSrTargNetwork": wfIpxNetBiosSrTargNetwork,
       "wfIpxNetBiosSrName": wfIpxNetBiosSrName,
       "wfIpxNetBiosSrIntf": wfIpxNetBiosSrIntf,
       "wfIpxNetBiosSrIndex": wfIpxNetBiosSrIndex,
       "wfIpxSapNetLvlFilterTable": wfIpxSapNetLvlFilterTable,
       "wfIpxSapNetLvlFilter": wfIpxSapNetLvlFilter,
       "wfIpxSapNetLvlDelete": wfIpxSapNetLvlDelete,
       "wfIpxSapNetLvlDisable": wfIpxSapNetLvlDisable,
       "wfIpxSapNetLvlTargNetwork": wfIpxSapNetLvlTargNetwork,
       "wfIpxSapNetLvlType": wfIpxSapNetLvlType,
       "wfIpxSapNetLvlAction": wfIpxSapNetLvlAction,
       "wfIpxSapNetLvlIntf": wfIpxSapNetLvlIntf,
       "wfIpxSapNetLvlIndex": wfIpxSapNetLvlIndex,
       "wfIpxSapServtLvlFilterTable": wfIpxSapServtLvlFilterTable,
       "wfIpxSapServLvlFilter": wfIpxSapServLvlFilter,
       "wfIpxSapServLvlDelete": wfIpxSapServLvlDelete,
       "wfIpxSapServLvlDisable": wfIpxSapServLvlDisable,
       "wfIpxSapServLvlTargServer": wfIpxSapServLvlTargServer,
       "wfIpxSapServLvlType": wfIpxSapServLvlType,
       "wfIpxSapServLvlAction": wfIpxSapServLvlAction,
       "wfIpxSapServLvlIntf": wfIpxSapServLvlIntf,
       "wfIpxSapServLvlIndex": wfIpxSapServLvlIndex,
       "wfIpxTrafficFilterTable": wfIpxTrafficFilterTable,
       "wfIpxTrafficFilterEntry": wfIpxTrafficFilterEntry,
       "wfIpxTrafficFilterCreate": wfIpxTrafficFilterCreate,
       "wfIpxTrafficFilterEnable": wfIpxTrafficFilterEnable,
       "wfIpxTrafficFilterStatus": wfIpxTrafficFilterStatus,
       "wfIpxTrafficFilterCounter": wfIpxTrafficFilterCounter,
       "wfIpxTrafficFilterDefinition": wfIpxTrafficFilterDefinition,
       "wfIpxTrafficFilterReserved": wfIpxTrafficFilterReserved,
       "wfIpxTrafficFilterInterface": wfIpxTrafficFilterInterface,
       "wfIpxTrafficFilterCircuit": wfIpxTrafficFilterCircuit,
       "wfIpxTrafficFilterRuleNumber": wfIpxTrafficFilterRuleNumber,
       "wfIpxTrafficFilterFragment": wfIpxTrafficFilterFragment,
       "wfOsiGroup": wfOsiGroup,
       "wfVinesGroup": wfVinesGroup,
       "wfVinesBase": wfVinesBase,
       "wfVinesBaseDelete": wfVinesBaseDelete,
       "wfVinesBaseDisable": wfVinesBaseDisable,
       "wfVinesBaseState": wfVinesBaseState,
       "wfVinesBaseUserNetid": wfVinesBaseUserNetid,
       "wfVinesBaseRouterNetid": wfVinesBaseRouterNetid,
       "wfVinesBaseBcastClass": wfVinesBaseBcastClass,
       "wfVinesIp": wfVinesIp,
       "wfVinesIpTotIn": wfVinesIpTotIn,
       "wfVinesIpTotOut": wfVinesIpTotOut,
       "wfVinesIpBad": wfVinesIpBad,
       "wfVinesIpRouted": wfVinesIpRouted,
       "wfVinesIpRoutedHWM": wfVinesIpRoutedHWM,
       "wfVinesIpBcast": wfVinesIpBcast,
       "wfVinesIpBcastHWM": wfVinesIpBcastHWM,
       "wfVinesIpReass": wfVinesIpReass,
       "wfVinesIpFrags": wfVinesIpFrags,
       "wfVinesIpToDodIP": wfVinesIpToDodIP,
       "wfVinesIpFromDodIP": wfVinesIpFromDodIP,
       "wfVinesRtpNbr": wfVinesRtpNbr,
       "wfVinesRtpNbrNumber": wfVinesRtpNbrNumber,
       "wfVinesRtpNbrTable": wfVinesRtpNbrTable,
       "wfVinesRtpNbrEntry": wfVinesRtpNbrEntry,
       "wfVinesRtpNbrNetId": wfVinesRtpNbrNetId,
       "wfVinesRtpNbrSubNetId": wfVinesRtpNbrSubNetId,
       "wfVinesRtpNbrType": wfVinesRtpNbrType,
       "wfVinesRtpNbrIfType": wfVinesRtpNbrIfType,
       "wfVinesRtpNbrRemAdr": wfVinesRtpNbrRemAdr,
       "wfVinesRtpNbrLocAdr": wfVinesRtpNbrLocAdr,
       "wfVinesRtpNbrLocSlot": wfVinesRtpNbrLocSlot,
       "wfVinesRtpNbrLocLine": wfVinesRtpNbrLocLine,
       "wfVinesRtpNbrSvrName": wfVinesRtpNbrSvrName,
       "wfVinesRtpNbrCost": wfVinesRtpNbrCost,
       "wfVinesRtpRt": wfVinesRtpRt,
       "wfVinesRtpRtNumber": wfVinesRtpRtNumber,
       "wfVinesRtpRtTable": wfVinesRtpRtTable,
       "wfVinesRtpRtEntry": wfVinesRtpRtEntry,
       "wfVinesRtpRtNetid": wfVinesRtpRtNetid,
       "wfVinesRtpRtMetric": wfVinesRtpRtMetric,
       "wfVinesRtpRtIdle": wfVinesRtpRtIdle,
       "wfVinesRtpRtGateNetid": wfVinesRtpRtGateNetid,
       "wfVinesRtpRtSvrName": wfVinesRtpRtSvrName,
       "wfVinesRtpRtGateSvrName": wfVinesRtpRtGateSvrName,
       "wfVinesIf": wfVinesIf,
       "wfVinesIfNumber": wfVinesIfNumber,
       "wfVinesIfTable": wfVinesIfTable,
       "wfVinesIfEntry": wfVinesIfEntry,
       "wfVinesIfDelete": wfVinesIfDelete,
       "wfVinesIfDisable": wfVinesIfDisable,
       "wfVinesIfState": wfVinesIfState,
       "wfVinesIfSlot": wfVinesIfSlot,
       "wfVinesIfLine": wfVinesIfLine,
       "wfVinesIfCct": wfVinesIfCct,
       "wfVinesIfSession": wfVinesIfSession,
       "wfVinesIfType": wfVinesIfType,
       "wfVinesIfDescr": wfVinesIfDescr,
       "wfVinesIfAdr": wfVinesIfAdr,
       "wfVinesIfDodIpDisable": wfVinesIfDodIpDisable,
       "wfVinesIfArpDisable": wfVinesIfArpDisable,
       "wfVinesIfTrEndStation": wfVinesIfTrEndStation,
       "wfVinesIfInPkts": wfVinesIfInPkts,
       "wfVinesIfInErrs": wfVinesIfInErrs,
       "wfVinesIfOutPkts": wfVinesIfOutPkts,
       "wfVinesIfOutErrs": wfVinesIfOutErrs,
       "wfVinesIfInMsgs": wfVinesIfInMsgs,
       "wfVinesIfMux": wfVinesIfMux,
       "wfVinesIfFwdDrops": wfVinesIfFwdDrops,
       "wfVinesIfZeroHopDrops": wfVinesIfZeroHopDrops,
       "wfVinesIfIcpInErrorNotifs": wfVinesIfIcpInErrorNotifs,
       "wfVinesIfIcpInMetricNotifs": wfVinesIfIcpInMetricNotifs,
       "wfVinesIfIcpInErrors": wfVinesIfIcpInErrors,
       "wfVinesIfIcpOutErrorNotifs": wfVinesIfIcpOutErrorNotifs,
       "wfVinesIfIcpOutMetricNotifs": wfVinesIfIcpOutMetricNotifs,
       "wfVinesIfArpInQueries": wfVinesIfArpInQueries,
       "wfVinesIfArpInAssgReqs": wfVinesIfArpInAssgReqs,
       "wfVinesIfArpInErrors": wfVinesIfArpInErrors,
       "wfVinesIfArpOutServRsps": wfVinesIfArpOutServRsps,
       "wfVinesIfArpOutAssgRsps": wfVinesIfArpOutAssgRsps,
       "wfVinesIfInRedirects": wfVinesIfInRedirects,
       "wfVinesIfOutRedirects": wfVinesIfOutRedirects,
       "wfVinesIfEchoInPkts": wfVinesIfEchoInPkts,
       "wfVinesIfEchoOutPkts": wfVinesIfEchoOutPkts,
       "wfVinesIfReassFails": wfVinesIfReassFails,
       "wfVinesIfRemClientPrivDisable": wfVinesIfRemClientPrivDisable,
       "wfVinesIfX25VC": wfVinesIfX25VC,
       "wfVinesIfX25VCNumber": wfVinesIfX25VCNumber,
       "wfVinesIfX25VCTable": wfVinesIfX25VCTable,
       "wfVinesIfX25VCEntry": wfVinesIfX25VCEntry,
       "wfVinesIfX25VCSlot": wfVinesIfX25VCSlot,
       "wfVinesIfX25VCLine": wfVinesIfX25VCLine,
       "wfVinesIfX25VCCct": wfVinesIfX25VCCct,
       "wfVinesIfX25VCSession": wfVinesIfX25VCSession,
       "wfVinesIfX25VCTotIn": wfVinesIfX25VCTotIn,
       "wfVinesIfX25VCTotOut": wfVinesIfX25VCTotOut,
       "wfVinesIfX25VCInErrs": wfVinesIfX25VCInErrs,
       "wfVinesIfX25VCOutErrs": wfVinesIfX25VCOutErrs,
       "wfVinesIfX25VCPktsOut": wfVinesIfX25VCPktsOut,
       "wfVinesIfX25VCPktsAwaitAck": wfVinesIfX25VCPktsAwaitAck,
       "wfVinesIfX25VCBytesOut": wfVinesIfX25VCBytesOut,
       "wfVinesIfX25VCBytesAwaitAck": wfVinesIfX25VCBytesAwaitAck,
       "wfVinesIfX25VCPktsIn": wfVinesIfX25VCPktsIn,
       "wfVinesIfX25VCBytesIn": wfVinesIfX25VCBytesIn,
       "wfVinesIfX25VCResetsIn": wfVinesIfX25VCResetsIn,
       "wfVinesIfX25VCResetsOut": wfVinesIfX25VCResetsOut,
       "wfVinesTrafficFilterTable": wfVinesTrafficFilterTable,
       "wfVinesTrafficFilterEntry": wfVinesTrafficFilterEntry,
       "wfVinesTrafficFilterCreate": wfVinesTrafficFilterCreate,
       "wfVinesTrafficFilterEnable": wfVinesTrafficFilterEnable,
       "wfVinesTrafficFilterStatus": wfVinesTrafficFilterStatus,
       "wfVinesTrafficFilterCounter": wfVinesTrafficFilterCounter,
       "wfVinesTrafficFilterDefinition": wfVinesTrafficFilterDefinition,
       "wfVinesTrafficFilterReserved": wfVinesTrafficFilterReserved,
       "wfVinesTrafficFilterCircuit": wfVinesTrafficFilterCircuit,
       "wfVinesTrafficFilterRuleNumber": wfVinesTrafficFilterRuleNumber,
       "wfVinesTrafficFilterFragment": wfVinesTrafficFilterFragment,
       "wfVinesNameTable": wfVinesNameTable,
       "wfVinesNameEntry": wfVinesNameEntry,
       "wfVinesNameDelete": wfVinesNameDelete,
       "wfVinesNameDisable": wfVinesNameDisable,
       "wfVinesNameNetid": wfVinesNameNetid,
       "wfVinesNameHost": wfVinesNameHost,
       "wfVinesNameSubNetid": wfVinesNameSubNetid,
       "wfVinesArp": wfVinesArp,
       "wfVinesArpDelete": wfVinesArpDelete,
       "wfVinesArpDisable": wfVinesArpDisable,
       "wfVinesArpState": wfVinesArpState,
       "wfVinesArpSubnetid": wfVinesArpSubnetid,
       "wfVinesArpSubnetBlock": wfVinesArpSubnetBlock,
       "wfVinesArpAssignDeniedPkts": wfVinesArpAssignDeniedPkts,
       "wfWanGroup": wfWanGroup,
       "wfFrameRelayGroup": wfFrameRelayGroup,
       "wfFrDlcmiTable": wfFrDlcmiTable,
       "wfFrDlcmiEntry": wfFrDlcmiEntry,
       "wfFrDlcmiDelete": wfFrDlcmiDelete,
       "wfFrDlcmiDisable": wfFrDlcmiDisable,
       "wfFrDlcmiState": wfFrDlcmiState,
       "wfFrDlcmiCircuit": wfFrDlcmiCircuit,
       "wfFrDlcmiManagementType": wfFrDlcmiManagementType,
       "wfFrDlcmiStatus": wfFrDlcmiStatus,
       "wfFrDlcmiAddress": wfFrDlcmiAddress,
       "wfFrDlcmiAddressLen": wfFrDlcmiAddressLen,
       "wfFrDlcmiPollingInterval": wfFrDlcmiPollingInterval,
       "wfFrDlcmiFullEnquiryInterval": wfFrDlcmiFullEnquiryInterval,
       "wfFrDlcmiErrorThreshold": wfFrDlcmiErrorThreshold,
       "wfFrDlcmiMonitoredEvents": wfFrDlcmiMonitoredEvents,
       "wfFrDlcmiMaxSupportedVCs": wfFrDlcmiMaxSupportedVCs,
       "wfFrDlcmiMulticast": wfFrDlcmiMulticast,
       "wfFrDlcmiSeqCount": wfFrDlcmiSeqCount,
       "wfFrDlcmiLastReceived": wfFrDlcmiLastReceived,
       "wfFrDlcmiPassiveSeqCount": wfFrDlcmiPassiveSeqCount,
       "wfFrDlcmiPassiveReceived": wfFrDlcmiPassiveReceived,
       "wfFrDlcmiPolls": wfFrDlcmiPolls,
       "wfFrDlcmiAlarmTimer": wfFrDlcmiAlarmTimer,
       "wfFrErrType": wfFrErrType,
       "wfFrErrData": wfFrErrData,
       "wfFrErrTime": wfFrErrTime,
       "wfFrErrDiscards": wfFrErrDiscards,
       "wfFrErrDrops": wfFrErrDrops,
       "wfFrCircuitTable": wfFrCircuitTable,
       "wfFrCircuitEntry": wfFrCircuitEntry,
       "wfFrCircuitDelete": wfFrCircuitDelete,
       "wfFrCircuitNumber": wfFrCircuitNumber,
       "wfFrCircuitDlci": wfFrCircuitDlci,
       "wfFrCircuitState": wfFrCircuitState,
       "wfFrCircuitStateSet": wfFrCircuitStateSet,
       "wfFrCircuitReceivedFECNs": wfFrCircuitReceivedFECNs,
       "wfFrCircuitReceivedBECNs": wfFrCircuitReceivedBECNs,
       "wfFrCircuitSentFrames": wfFrCircuitSentFrames,
       "wfFrCircuitSentOctets": wfFrCircuitSentOctets,
       "wfFrCircuitReceivedFrames": wfFrCircuitReceivedFrames,
       "wfFrCircuitReceivedOctets": wfFrCircuitReceivedOctets,
       "wfFrCircuitCreationTime": wfFrCircuitCreationTime,
       "wfFrCircuitLastTimeChange": wfFrCircuitLastTimeChange,
       "wfFrCircuitCommittedBurst": wfFrCircuitCommittedBurst,
       "wfFrCircuitExcessBurst": wfFrCircuitExcessBurst,
       "wfFrCircuitThroughput": wfFrCircuitThroughput,
       "wfFrCircuitMulticast": wfFrCircuitMulticast,
       "wfFrCircuitDiscards": wfFrCircuitDiscards,
       "wfFrCircuitDrops": wfFrCircuitDrops,
       "wfFrCircuitSubCct": wfFrCircuitSubCct,
       "wfFrCircuitMode": wfFrCircuitMode,
       "wfPppGroup": wfPppGroup,
       "wfSmdsCircuitTable": wfSmdsCircuitTable,
       "wfSmdsCircuitEntry": wfSmdsCircuitEntry,
       "wfSmdsCircuitDelete": wfSmdsCircuitDelete,
       "wfSmdsCircuitDisable": wfSmdsCircuitDisable,
       "wfSmdsCircuitState": wfSmdsCircuitState,
       "wfSmdsCircuitID": wfSmdsCircuitID,
       "wfSmdsCircuitIndivAddr": wfSmdsCircuitIndivAddr,
       "wfSmdsCircuitGroupAddr": wfSmdsCircuitGroupAddr,
       "wfSmdsCircuitArpAddr": wfSmdsCircuitArpAddr,
       "wfSmdsCircuitDisableHrtbtPoll": wfSmdsCircuitDisableHrtbtPoll,
       "wfSmdsCircuitHrtbtPollInterval": wfSmdsCircuitHrtbtPollInterval,
       "wfSmdsCircuitHrtbtPollDownCount": wfSmdsCircuitHrtbtPollDownCount,
       "wfSmdsCircuitDisableNetMgmt": wfSmdsCircuitDisableNetMgmt,
       "wfSmdsCircuitSipL3ReceivedIndividualDAs": wfSmdsCircuitSipL3ReceivedIndividualDAs,
       "wfSmdsCircuitSipL3ReceivedGAs": wfSmdsCircuitSipL3ReceivedGAs,
       "wfSmdsCircuitSipL3SentIndividualDAs": wfSmdsCircuitSipL3SentIndividualDAs,
       "wfSmdsCircuitSipL3SentGAs": wfSmdsCircuitSipL3SentGAs,
       "wfSmdsCircuitSipL3VersionSupport": wfSmdsCircuitSipL3VersionSupport,
       "wfX25Group": wfX25Group,
       "wfAtmGroup": wfAtmGroup,
       "wfXnsGroup": wfXnsGroup,
       "wfXnsBase": wfXnsBase,
       "wfXnsBaseDelete": wfXnsBaseDelete,
       "wfXnsBaseDisable": wfXnsBaseDisable,
       "wfXnsBaseState": wfXnsBaseState,
       "wfXnsBaseHostNumber": wfXnsBaseHostNumber,
       "wfXnsBaseRtEntryTable": wfXnsBaseRtEntryTable,
       "wfXnsBaseRtEntry": wfXnsBaseRtEntry,
       "wfXnsBaseRouteDest": wfXnsBaseRouteDest,
       "wfXnsBaseRouteIfIndex": wfXnsBaseRouteIfIndex,
       "wfXnsBaseRouteMetric": wfXnsBaseRouteMetric,
       "wfXnsBaseRouteNextHopNetwork": wfXnsBaseRouteNextHopNetwork,
       "wfXnsBaseRouteNextHopHost": wfXnsBaseRouteNextHopHost,
       "wfXnsBaseRouteType": wfXnsBaseRouteType,
       "wfXnsBaseRouteProto": wfXnsBaseRouteProto,
       "wfXnsBaseRouteAge": wfXnsBaseRouteAge,
       "wfXnsBaseRouteInfo": wfXnsBaseRouteInfo,
       "wfXnsInterfaceTable": wfXnsInterfaceTable,
       "wfXnsInterfaceEntry": wfXnsInterfaceEntry,
       "wfXnsInterfaceIndex": wfXnsInterfaceIndex,
       "wfXnsInterfaceDelete": wfXnsInterfaceDelete,
       "wfXnsInterfaceDisable": wfXnsInterfaceDisable,
       "wfXnsInterfaceState": wfXnsInterfaceState,
       "wfXnsInterfaceCircuit": wfXnsInterfaceCircuit,
       "wfXnsInterfaceNetworkNumber": wfXnsInterfaceNetworkNumber,
       "wfXnsInterfaceCost": wfXnsInterfaceCost,
       "wfXnsInterfaceXsumOn": wfXnsInterfaceXsumOn,
       "wfXnsInterfaceEncaps": wfXnsInterfaceEncaps,
       "wfXnsInterfaceMacAddress": wfXnsInterfaceMacAddress,
       "wfXnsInterfaceSMDSGroupAddress": wfXnsInterfaceSMDSGroupAddress,
       "wfXnsInterfaceMaxInfo": wfXnsInterfaceMaxInfo,
       "wfXnsInterfaceExtServer": wfXnsInterfaceExtServer,
       "wfXnsInterfaceExServNetwork": wfXnsInterfaceExServNetwork,
       "wfXnsInterfaceExServHostId": wfXnsInterfaceExServHostId,
       "wfXnsInterfaceExServPktType": wfXnsInterfaceExServPktType,
       "wfXnsInterfaceExServSockNm": wfXnsInterfaceExServSockNm,
       "wfXnsInterfaceInReceives": wfXnsInterfaceInReceives,
       "wfXnsInterfaceInHdrErrors": wfXnsInterfaceInHdrErrors,
       "wfXnsInterfaceInAddrErrors": wfXnsInterfaceInAddrErrors,
       "wfXnsInterfaceForwDatagrams": wfXnsInterfaceForwDatagrams,
       "wfXnsInterfaceInUnknownProtos": wfXnsInterfaceInUnknownProtos,
       "wfXnsInterfaceInDiscards": wfXnsInterfaceInDiscards,
       "wfXnsInterfaceInDelivers": wfXnsInterfaceInDelivers,
       "wfXnsInterfaceOutRequests": wfXnsInterfaceOutRequests,
       "wfXnsInterfaceOutDiscards": wfXnsInterfaceOutDiscards,
       "wfXnsInterfaceOutNoRoutes": wfXnsInterfaceOutNoRoutes,
       "wfXnsInterfaceFRBcast": wfXnsInterfaceFRBcast,
       "wfXnsInterfaceFRMcast": wfXnsInterfaceFRMcast,
       "wfXnsRipIntfTable": wfXnsRipIntfTable,
       "wfXnsRipIntfEntry": wfXnsRipIntfEntry,
       "wfXnsRipInterfaceDelete": wfXnsRipInterfaceDelete,
       "wfXnsRipInterfaceDisable": wfXnsRipInterfaceDisable,
       "wfXnsRipInterfaceState": wfXnsRipInterfaceState,
       "wfXnsRipInterfaceIndex": wfXnsRipInterfaceIndex,
       "wfXnsRipInterfaceSupply": wfXnsRipInterfaceSupply,
       "wfXnsRipInterfaceListen": wfXnsRipInterfaceListen,
       "wfXnsAdjacentHostTable": wfXnsAdjacentHostTable,
       "wfXnsAdjacentHostEntry": wfXnsAdjacentHostEntry,
       "wfXnsAhDelete": wfXnsAhDelete,
       "wfXnsAhDisable": wfXnsAhDisable,
       "wfXnsAhTargHostNetwork": wfXnsAhTargHostNetwork,
       "wfXnsAhTargHostId": wfXnsAhTargHostId,
       "wfXnsAhNextHopIntf": wfXnsAhNextHopIntf,
       "wfXnsAhDlci": wfXnsAhDlci,
       "wfXnsStaticRouteTable": wfXnsStaticRouteTable,
       "wfXnsStaticRouteEntry": wfXnsStaticRouteEntry,
       "wfXnsSrDelete": wfXnsSrDelete,
       "wfXnsSrDisable": wfXnsSrDisable,
       "wfXnsSrTargNetwork": wfXnsSrTargNetwork,
       "wfXnsSrCost": wfXnsSrCost,
       "wfXnsSrNextHopNetwork": wfXnsSrNextHopNetwork,
       "wfXnsSrNextHopHost": wfXnsSrNextHopHost,
       "wfXnsSrTargNetworkRt": wfXnsSrTargNetworkRt,
       "wfXnsTrafficFilterTable": wfXnsTrafficFilterTable,
       "wfXnsTrafficFilterEntry": wfXnsTrafficFilterEntry,
       "wfXnsTrafficFilterCreate": wfXnsTrafficFilterCreate,
       "wfXnsTrafficFilterEnable": wfXnsTrafficFilterEnable,
       "wfXnsTrafficFilterStatus": wfXnsTrafficFilterStatus,
       "wfXnsTrafficFilterCounter": wfXnsTrafficFilterCounter,
       "wfXnsTrafficFilterDefinition": wfXnsTrafficFilterDefinition,
       "wfXnsTrafficFilterReserved": wfXnsTrafficFilterReserved,
       "wfXnsTrafficFilterInterface": wfXnsTrafficFilterInterface,
       "wfXnsTrafficFilterCircuit": wfXnsTrafficFilterCircuit,
       "wfXnsTrafficFilterRuleNumber": wfXnsTrafficFilterRuleNumber,
       "wfXnsTrafficFilterFragment": wfXnsTrafficFilterFragment,
       "wfTestGroup": wfTestGroup}
)
