# SNMP MIB module (A3COM-HUAWEI-VOANALOGIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VOANALOGIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:18 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

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

h3cVoiceAnalogInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3)
)
h3cVoiceAnalogInterface.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoAnalogIfCommonObjects_ObjectIdentity = ObjectIdentity
h3cVoAnalogIfCommonObjects = _H3cVoAnalogIfCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 1)
)
_H3cVoAnalogIfCommonCfgTable_Object = MibTable
h3cVoAnalogIfCommonCfgTable = _H3cVoAnalogIfCommonCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfCommonCfgTable.setStatus("current")
_H3cVoAnalogIfCommonCfgEntry_Object = MibTableRow
h3cVoAnalogIfCommonCfgEntry = _H3cVoAnalogIfCommonCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 1, 1, 1)
)
h3cVoAnalogIfCommonCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfCfgPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfCommonCfgEntry.setStatus("current")
_H3cVoAIfCfgPortIndex_Type = Integer32
_H3cVoAIfCfgPortIndex_Object = MibTableColumn
h3cVoAIfCfgPortIndex = _H3cVoAIfCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 1, 1, 1, 1),
    _H3cVoAIfCfgPortIndex_Type()
)
h3cVoAIfCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoAIfCfgPortIndex.setStatus("current")


class _H3cVoAIfCfgPortType_Type(Integer32):
    """Custom type h3cVoAIfCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 3),
          ("fxo", 2),
          ("fxs", 1))
    )


_H3cVoAIfCfgPortType_Type.__name__ = "Integer32"
_H3cVoAIfCfgPortType_Object = MibTableColumn
h3cVoAIfCfgPortType = _H3cVoAIfCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 1, 1, 1, 2),
    _H3cVoAIfCfgPortType_Type()
)
h3cVoAIfCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfCfgPortType.setStatus("current")
_H3cVoAIfCfgPortSubLine_Type = OctetString
_H3cVoAIfCfgPortSubLine_Object = MibTableColumn
h3cVoAIfCfgPortSubLine = _H3cVoAIfCfgPortSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 1, 1, 1, 3),
    _H3cVoAIfCfgPortSubLine_Type()
)
h3cVoAIfCfgPortSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfCfgPortSubLine.setStatus("current")
_H3cVoAnalogIfFXSObjects_ObjectIdentity = ObjectIdentity
h3cVoAnalogIfFXSObjects = _H3cVoAnalogIfFXSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2)
)
_H3cVoAnalogIfFXSCfgTable_Object = MibTable
h3cVoAnalogIfFXSCfgTable = _H3cVoAnalogIfFXSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXSCfgTable.setStatus("current")
_H3cVoAnalogIfFXSCfgEntry_Object = MibTableRow
h3cVoAnalogIfFXSCfgEntry = _H3cVoAnalogIfFXSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1, 1)
)
h3cVoAnalogIfFXSCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfFXSCfgPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXSCfgEntry.setStatus("current")
_H3cVoAIfFXSCfgPortIndex_Type = Integer32
_H3cVoAIfFXSCfgPortIndex_Object = MibTableColumn
h3cVoAIfFXSCfgPortIndex = _H3cVoAIfFXSCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1, 1, 1),
    _H3cVoAIfFXSCfgPortIndex_Type()
)
h3cVoAIfFXSCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoAIfFXSCfgPortIndex.setStatus("current")


class _H3cVoAIfFXSCfgCidDisplay_Type(Integer32):
    """Custom type h3cVoAIfFXSCfgCidDisplay based on Integer32"""
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


_H3cVoAIfFXSCfgCidDisplay_Type.__name__ = "Integer32"
_H3cVoAIfFXSCfgCidDisplay_Object = MibTableColumn
h3cVoAIfFXSCfgCidDisplay = _H3cVoAIfFXSCfgCidDisplay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1, 1, 3),
    _H3cVoAIfFXSCfgCidDisplay_Type()
)
h3cVoAIfFXSCfgCidDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXSCfgCidDisplay.setStatus("current")


class _H3cVoAIfFXSCfgCidSend_Type(Integer32):
    """Custom type h3cVoAIfFXSCfgCidSend based on Integer32"""
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


_H3cVoAIfFXSCfgCidSend_Type.__name__ = "Integer32"
_H3cVoAIfFXSCfgCidSend_Object = MibTableColumn
h3cVoAIfFXSCfgCidSend = _H3cVoAIfFXSCfgCidSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1, 1, 4),
    _H3cVoAIfFXSCfgCidSend_Type()
)
h3cVoAIfFXSCfgCidSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXSCfgCidSend.setStatus("current")


class _H3cVoAIfFXSCfgCidType_Type(Integer32):
    """Custom type h3cVoAIfFXSCfgCidType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complex", 1),
          ("simple", 2))
    )


_H3cVoAIfFXSCfgCidType_Type.__name__ = "Integer32"
_H3cVoAIfFXSCfgCidType_Object = MibTableColumn
h3cVoAIfFXSCfgCidType = _H3cVoAIfFXSCfgCidType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1, 1, 5),
    _H3cVoAIfFXSCfgCidType_Type()
)
h3cVoAIfFXSCfgCidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXSCfgCidType.setStatus("current")
_H3cVoAIfFXSCfgSubLine_Type = OctetString
_H3cVoAIfFXSCfgSubLine_Object = MibTableColumn
h3cVoAIfFXSCfgSubLine = _H3cVoAIfFXSCfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 1, 1, 6),
    _H3cVoAIfFXSCfgSubLine_Type()
)
h3cVoAIfFXSCfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfFXSCfgSubLine.setStatus("current")
_H3cVoAnalogIfFXSTimerTable_Object = MibTable
h3cVoAnalogIfFXSTimerTable = _H3cVoAnalogIfFXSTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXSTimerTable.setStatus("current")
_H3cVoAnalogIfFXSTimerEntry_Object = MibTableRow
h3cVoAnalogIfFXSTimerEntry = _H3cVoAnalogIfFXSTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3, 1)
)
h3cVoAnalogIfFXSTimerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfFXSTimerPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXSTimerEntry.setStatus("current")
_H3cVoAIfFXSTimerPortIndex_Type = Integer32
_H3cVoAIfFXSTimerPortIndex_Object = MibTableColumn
h3cVoAIfFXSTimerPortIndex = _H3cVoAIfFXSTimerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3, 1, 1),
    _H3cVoAIfFXSTimerPortIndex_Type()
)
h3cVoAIfFXSTimerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoAIfFXSTimerPortIndex.setStatus("current")


class _H3cVoAIfFXSTimerDialInterval_Type(Integer32):
    """Custom type h3cVoAIfFXSTimerDialInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_H3cVoAIfFXSTimerDialInterval_Type.__name__ = "Integer32"
_H3cVoAIfFXSTimerDialInterval_Object = MibTableColumn
h3cVoAIfFXSTimerDialInterval = _H3cVoAIfFXSTimerDialInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3, 1, 4),
    _H3cVoAIfFXSTimerDialInterval_Type()
)
h3cVoAIfFXSTimerDialInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXSTimerDialInterval.setStatus("current")


class _H3cVoAIfFXSTimerFirstDial_Type(Integer32):
    """Custom type h3cVoAIfFXSTimerFirstDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_H3cVoAIfFXSTimerFirstDial_Type.__name__ = "Integer32"
_H3cVoAIfFXSTimerFirstDial_Object = MibTableColumn
h3cVoAIfFXSTimerFirstDial = _H3cVoAIfFXSTimerFirstDial_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3, 1, 5),
    _H3cVoAIfFXSTimerFirstDial_Type()
)
h3cVoAIfFXSTimerFirstDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXSTimerFirstDial.setStatus("current")
_H3cVoAIfFXSTimerRingBack_Type = Integer32
_H3cVoAIfFXSTimerRingBack_Object = MibTableColumn
h3cVoAIfFXSTimerRingBack = _H3cVoAIfFXSTimerRingBack_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3, 1, 6),
    _H3cVoAIfFXSTimerRingBack_Type()
)
h3cVoAIfFXSTimerRingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXSTimerRingBack.setStatus("current")
_H3cVoAIfFXSTimerSubLine_Type = OctetString
_H3cVoAIfFXSTimerSubLine_Object = MibTableColumn
h3cVoAIfFXSTimerSubLine = _H3cVoAIfFXSTimerSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 2, 3, 1, 7),
    _H3cVoAIfFXSTimerSubLine_Type()
)
h3cVoAIfFXSTimerSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfFXSTimerSubLine.setStatus("current")
_H3cVoAnalogIfFXOObjects_ObjectIdentity = ObjectIdentity
h3cVoAnalogIfFXOObjects = _H3cVoAnalogIfFXOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3)
)
_H3cVoAnalogIfFXOCfgTable_Object = MibTable
h3cVoAnalogIfFXOCfgTable = _H3cVoAnalogIfFXOCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXOCfgTable.setStatus("current")
_H3cVoAnalogIfFXOCfgEntry_Object = MibTableRow
h3cVoAnalogIfFXOCfgEntry = _H3cVoAnalogIfFXOCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1)
)
h3cVoAnalogIfFXOCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfFXOCfgPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXOCfgEntry.setStatus("current")
_H3cVoAIfFXOCfgPortIndex_Type = Integer32
_H3cVoAIfFXOCfgPortIndex_Object = MibTableColumn
h3cVoAIfFXOCfgPortIndex = _H3cVoAIfFXOCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 1),
    _H3cVoAIfFXOCfgPortIndex_Type()
)
h3cVoAIfFXOCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoAIfFXOCfgPortIndex.setStatus("current")


class _H3cVoAIfFXOCfgArea_Type(Integer32):
    """Custom type h3cVoAIfFXOCfgArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("europe", 2),
          ("northmerica", 3))
    )


_H3cVoAIfFXOCfgArea_Type.__name__ = "Integer32"
_H3cVoAIfFXOCfgArea_Object = MibTableColumn
h3cVoAIfFXOCfgArea = _H3cVoAIfFXOCfgArea_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 4),
    _H3cVoAIfFXOCfgArea_Type()
)
h3cVoAIfFXOCfgArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOCfgArea.setStatus("current")


class _H3cVoAIfFXOPreDialDelay_Type(Integer32):
    """Custom type h3cVoAIfFXOPreDialDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_H3cVoAIfFXOPreDialDelay_Type.__name__ = "Integer32"
_H3cVoAIfFXOPreDialDelay_Object = MibTableColumn
h3cVoAIfFXOPreDialDelay = _H3cVoAIfFXOPreDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 5),
    _H3cVoAIfFXOPreDialDelay_Type()
)
h3cVoAIfFXOPreDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOPreDialDelay.setStatus("current")


class _H3cVoAIfFXOCfgPortImpedance_Type(Integer32):
    """Custom type h3cVoAIfFXOCfgPortImpedance based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("australia", 1),
          ("austria", 2),
          ("belgiumLong", 3),
          ("belgiumShort", 4),
          ("brazil", 5),
          ("china", 7),
          ("czechRepublic", 9),
          ("denmark", 10),
          ("eTSIHarmanized", 11),
          ("finland", 12),
          ("france", 13),
          ("germanSwiss", 6),
          ("greece", 8),
          ("hungary", 14),
          ("india", 15),
          ("italy", 16),
          ("japan", 17),
          ("korea", 18),
          ("mexico", 19),
          ("netherlands", 20),
          ("norway", 21),
          ("portugal", 22),
          ("r550", 30),
          ("r600", 31),
          ("r650", 32),
          ("r700", 33),
          ("r750", 34),
          ("r800", 35),
          ("r850", 36),
          ("r900", 37),
          ("r950", 38),
          ("slovakia", 23),
          ("spain", 24),
          ("sweden", 25),
          ("uk", 26),
          ("usLoadedLine", 27),
          ("usNonLoaded", 28),
          ("usSpecialService", 29))
    )


_H3cVoAIfFXOCfgPortImpedance_Type.__name__ = "Integer32"
_H3cVoAIfFXOCfgPortImpedance_Object = MibTableColumn
h3cVoAIfFXOCfgPortImpedance = _H3cVoAIfFXOCfgPortImpedance_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 6),
    _H3cVoAIfFXOCfgPortImpedance_Type()
)
h3cVoAIfFXOCfgPortImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOCfgPortImpedance.setStatus("current")


class _H3cVoAIfFXOCfgCidEnable_Type(Integer32):
    """Custom type h3cVoAIfFXOCfgCidEnable based on Integer32"""
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


_H3cVoAIfFXOCfgCidEnable_Type.__name__ = "Integer32"
_H3cVoAIfFXOCfgCidEnable_Object = MibTableColumn
h3cVoAIfFXOCfgCidEnable = _H3cVoAIfFXOCfgCidEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 7),
    _H3cVoAIfFXOCfgCidEnable_Type()
)
h3cVoAIfFXOCfgCidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOCfgCidEnable.setStatus("current")


class _H3cVoAnalogIfFXOCfgCidSend_Type(Integer32):
    """Custom type h3cVoAnalogIfFXOCfgCidSend based on Integer32"""
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


_H3cVoAnalogIfFXOCfgCidSend_Type.__name__ = "Integer32"
_H3cVoAnalogIfFXOCfgCidSend_Object = MibTableColumn
h3cVoAnalogIfFXOCfgCidSend = _H3cVoAnalogIfFXOCfgCidSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 8),
    _H3cVoAnalogIfFXOCfgCidSend_Type()
)
h3cVoAnalogIfFXOCfgCidSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXOCfgCidSend.setStatus("current")


class _H3cVoAIfFXOCfgCidType_Type(Integer32):
    """Custom type h3cVoAIfFXOCfgCidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complex", 1),
          ("simple", 2))
    )


_H3cVoAIfFXOCfgCidType_Type.__name__ = "Integer32"
_H3cVoAIfFXOCfgCidType_Object = MibTableColumn
h3cVoAIfFXOCfgCidType = _H3cVoAIfFXOCfgCidType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 9),
    _H3cVoAIfFXOCfgCidType_Type()
)
h3cVoAIfFXOCfgCidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOCfgCidType.setStatus("current")
_H3cVoAIfFXOCfgSubLine_Type = OctetString
_H3cVoAIfFXOCfgSubLine_Object = MibTableColumn
h3cVoAIfFXOCfgSubLine = _H3cVoAIfFXOCfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 1, 1, 10),
    _H3cVoAIfFXOCfgSubLine_Type()
)
h3cVoAIfFXOCfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfFXOCfgSubLine.setStatus("current")
_H3cVoAnalogIfFXOTimerTable_Object = MibTable
h3cVoAnalogIfFXOTimerTable = _H3cVoAnalogIfFXOTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXOTimerTable.setStatus("current")
_H3cVoAnalogIfFXOTimerEntry_Object = MibTableRow
h3cVoAnalogIfFXOTimerEntry = _H3cVoAnalogIfFXOTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1)
)
h3cVoAnalogIfFXOTimerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfFXOTimerPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfFXOTimerEntry.setStatus("current")
_H3cVoAIfFXOTimerPortIndex_Type = Integer32
_H3cVoAIfFXOTimerPortIndex_Object = MibTableColumn
h3cVoAIfFXOTimerPortIndex = _H3cVoAIfFXOTimerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 1),
    _H3cVoAIfFXOTimerPortIndex_Type()
)
h3cVoAIfFXOTimerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerPortIndex.setStatus("current")
_H3cVoAIfFXOTimerDtmf_Type = Integer32
_H3cVoAIfFXOTimerDtmf_Object = MibTableColumn
h3cVoAIfFXOTimerDtmf = _H3cVoAIfFXOTimerDtmf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 2),
    _H3cVoAIfFXOTimerDtmf_Type()
)
h3cVoAIfFXOTimerDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerDtmf.setStatus("current")
_H3cVoAIfFXOTimerDtmfInterval_Type = Integer32
_H3cVoAIfFXOTimerDtmfInterval_Object = MibTableColumn
h3cVoAIfFXOTimerDtmfInterval = _H3cVoAIfFXOTimerDtmfInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 3),
    _H3cVoAIfFXOTimerDtmfInterval_Type()
)
h3cVoAIfFXOTimerDtmfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerDtmfInterval.setStatus("current")
_H3cVoAIfFXOTimerDialInterval_Type = Integer32
_H3cVoAIfFXOTimerDialInterval_Object = MibTableColumn
h3cVoAIfFXOTimerDialInterval = _H3cVoAIfFXOTimerDialInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 4),
    _H3cVoAIfFXOTimerDialInterval_Type()
)
h3cVoAIfFXOTimerDialInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerDialInterval.setStatus("current")
_H3cVoAIfFXOTimerFirstDial_Type = Integer32
_H3cVoAIfFXOTimerFirstDial_Object = MibTableColumn
h3cVoAIfFXOTimerFirstDial = _H3cVoAIfFXOTimerFirstDial_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 5),
    _H3cVoAIfFXOTimerFirstDial_Type()
)
h3cVoAIfFXOTimerFirstDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerFirstDial.setStatus("current")
_H3cVoAIfFXOTimerRingBack_Type = Integer32
_H3cVoAIfFXOTimerRingBack_Object = MibTableColumn
h3cVoAIfFXOTimerRingBack = _H3cVoAIfFXOTimerRingBack_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 6),
    _H3cVoAIfFXOTimerRingBack_Type()
)
h3cVoAIfFXOTimerRingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerRingBack.setStatus("current")
_H3cVoAIfFXOTimerSubLine_Type = OctetString
_H3cVoAIfFXOTimerSubLine_Object = MibTableColumn
h3cVoAIfFXOTimerSubLine = _H3cVoAIfFXOTimerSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 3, 3, 1, 7),
    _H3cVoAIfFXOTimerSubLine_Type()
)
h3cVoAIfFXOTimerSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfFXOTimerSubLine.setStatus("current")
_H3cVoAnalogIfEMObjects_ObjectIdentity = ObjectIdentity
h3cVoAnalogIfEMObjects = _H3cVoAnalogIfEMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4)
)
_H3cVoAnalogIfEMCfgTable_Object = MibTable
h3cVoAnalogIfEMCfgTable = _H3cVoAnalogIfEMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfEMCfgTable.setStatus("current")
_H3cVoAnalogIfEMCfgEntry_Object = MibTableRow
h3cVoAnalogIfEMCfgEntry = _H3cVoAnalogIfEMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1)
)
h3cVoAnalogIfEMCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfEMCfgPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfEMCfgEntry.setStatus("current")
_H3cVoAIfEMCfgPortIndex_Type = Integer32
_H3cVoAIfEMCfgPortIndex_Object = MibTableColumn
h3cVoAIfEMCfgPortIndex = _H3cVoAIfEMCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 1),
    _H3cVoAIfEMCfgPortIndex_Type()
)
h3cVoAIfEMCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgPortIndex.setStatus("current")


class _H3cVoAIfEMCfgSignalMode_Type(Integer32):
    """Custom type h3cVoAIfEMCfgSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayDial", 1),
          ("immediateDial", 2),
          ("winkStart", 3))
    )


_H3cVoAIfEMCfgSignalMode_Type.__name__ = "Integer32"
_H3cVoAIfEMCfgSignalMode_Object = MibTableColumn
h3cVoAIfEMCfgSignalMode = _H3cVoAIfEMCfgSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 2),
    _H3cVoAIfEMCfgSignalMode_Type()
)
h3cVoAIfEMCfgSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgSignalMode.setStatus("current")


class _H3cVoAIfEMCfgPhyParm_Type(Integer32):
    """Custom type h3cVoAIfEMCfgPhyParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWiresOperation", 2),
          ("twoWiresOperation", 1))
    )


_H3cVoAIfEMCfgPhyParm_Type.__name__ = "Integer32"
_H3cVoAIfEMCfgPhyParm_Object = MibTableColumn
h3cVoAIfEMCfgPhyParm = _H3cVoAIfEMCfgPhyParm_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 3),
    _H3cVoAIfEMCfgPhyParm_Type()
)
h3cVoAIfEMCfgPhyParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgPhyParm.setStatus("current")


class _H3cVoAIfEMCfgPhyType_Type(Integer32):
    """Custom type h3cVoAIfEMCfgPhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type5", 5))
    )


_H3cVoAIfEMCfgPhyType_Type.__name__ = "Integer32"
_H3cVoAIfEMCfgPhyType_Object = MibTableColumn
h3cVoAIfEMCfgPhyType = _H3cVoAIfEMCfgPhyType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 4),
    _H3cVoAIfEMCfgPhyType_Type()
)
h3cVoAIfEMCfgPhyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgPhyType.setStatus("current")


class _H3cVoAIfEMCfgTimeoutRing_Type(Integer32):
    """Custom type h3cVoAIfEMCfgTimeoutRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_H3cVoAIfEMCfgTimeoutRing_Type.__name__ = "Integer32"
_H3cVoAIfEMCfgTimeoutRing_Object = MibTableColumn
h3cVoAIfEMCfgTimeoutRing = _H3cVoAIfEMCfgTimeoutRing_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 5),
    _H3cVoAIfEMCfgTimeoutRing_Type()
)
h3cVoAIfEMCfgTimeoutRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgTimeoutRing.setStatus("current")
_H3cVoAIfEMCfgTimeoutWaitDigit_Type = Integer32
_H3cVoAIfEMCfgTimeoutWaitDigit_Object = MibTableColumn
h3cVoAIfEMCfgTimeoutWaitDigit = _H3cVoAIfEMCfgTimeoutWaitDigit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 6),
    _H3cVoAIfEMCfgTimeoutWaitDigit_Type()
)
h3cVoAIfEMCfgTimeoutWaitDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgTimeoutWaitDigit.setStatus("current")
_H3cVoAIfEMCfgSubLine_Type = OctetString
_H3cVoAIfEMCfgSubLine_Object = MibTableColumn
h3cVoAIfEMCfgSubLine = _H3cVoAIfEMCfgSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 1, 1, 7),
    _H3cVoAIfEMCfgSubLine_Type()
)
h3cVoAIfEMCfgSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfEMCfgSubLine.setStatus("current")
_H3cVoAnalogIfEMTimerTable_Object = MibTable
h3cVoAnalogIfEMTimerTable = _H3cVoAnalogIfEMTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3)
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfEMTimerTable.setStatus("current")
_H3cVoAnalogIfEMTimerEntry_Object = MibTableRow
h3cVoAnalogIfEMTimerEntry = _H3cVoAnalogIfEMTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1)
)
h3cVoAnalogIfEMTimerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOANALOGIF-MIB", "h3cVoAIfEMTimerPortIndex"),
)
if mibBuilder.loadTexts:
    h3cVoAnalogIfEMTimerEntry.setStatus("current")
_H3cVoAIfEMTimerPortIndex_Type = Integer32
_H3cVoAIfEMTimerPortIndex_Object = MibTableColumn
h3cVoAIfEMTimerPortIndex = _H3cVoAIfEMTimerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 1),
    _H3cVoAIfEMTimerPortIndex_Type()
)
h3cVoAIfEMTimerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerPortIndex.setStatus("current")
_H3cVoAIfEMTimerDtmf_Type = Integer32
_H3cVoAIfEMTimerDtmf_Object = MibTableColumn
h3cVoAIfEMTimerDtmf = _H3cVoAIfEMTimerDtmf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 2),
    _H3cVoAIfEMTimerDtmf_Type()
)
h3cVoAIfEMTimerDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerDtmf.setStatus("current")
_H3cVoAIfEMTimerDtmfInterval_Type = Integer32
_H3cVoAIfEMTimerDtmfInterval_Object = MibTableColumn
h3cVoAIfEMTimerDtmfInterval = _H3cVoAIfEMTimerDtmfInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 3),
    _H3cVoAIfEMTimerDtmfInterval_Type()
)
h3cVoAIfEMTimerDtmfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerDtmfInterval.setStatus("current")


class _H3cVoAIfEMTimerSendWink_Type(Integer32):
    """Custom type h3cVoAIfEMTimerSendWink based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_H3cVoAIfEMTimerSendWink_Type.__name__ = "Integer32"
_H3cVoAIfEMTimerSendWink_Object = MibTableColumn
h3cVoAIfEMTimerSendWink = _H3cVoAIfEMTimerSendWink_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 5),
    _H3cVoAIfEMTimerSendWink_Type()
)
h3cVoAIfEMTimerSendWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerSendWink.setStatus("current")
_H3cVoAIfEMTimerWinkRising_Type = Integer32
_H3cVoAIfEMTimerWinkRising_Object = MibTableColumn
h3cVoAIfEMTimerWinkRising = _H3cVoAIfEMTimerWinkRising_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 6),
    _H3cVoAIfEMTimerWinkRising_Type()
)
h3cVoAIfEMTimerWinkRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerWinkRising.setStatus("current")
_H3cVoAIfEMTimerWinkHold_Type = Integer32
_H3cVoAIfEMTimerWinkHold_Object = MibTableColumn
h3cVoAIfEMTimerWinkHold = _H3cVoAIfEMTimerWinkHold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 7),
    _H3cVoAIfEMTimerWinkHold_Type()
)
h3cVoAIfEMTimerWinkHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerWinkHold.setStatus("current")
_H3cVoAIfEMTimerDialoutDelay_Type = Integer32
_H3cVoAIfEMTimerDialoutDelay_Object = MibTableColumn
h3cVoAIfEMTimerDialoutDelay = _H3cVoAIfEMTimerDialoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 8),
    _H3cVoAIfEMTimerDialoutDelay_Type()
)
h3cVoAIfEMTimerDialoutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerDialoutDelay.setStatus("current")
_H3cVoAIfEMTimerDelayRising_Type = Integer32
_H3cVoAIfEMTimerDelayRising_Object = MibTableColumn
h3cVoAIfEMTimerDelayRising = _H3cVoAIfEMTimerDelayRising_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 9),
    _H3cVoAIfEMTimerDelayRising_Type()
)
h3cVoAIfEMTimerDelayRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerDelayRising.setStatus("current")
_H3cVoAIfEMTimerDelayHold_Type = Integer32
_H3cVoAIfEMTimerDelayHold_Object = MibTableColumn
h3cVoAIfEMTimerDelayHold = _H3cVoAIfEMTimerDelayHold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 10),
    _H3cVoAIfEMTimerDelayHold_Type()
)
h3cVoAIfEMTimerDelayHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerDelayHold.setStatus("current")
_H3cVoAIfEMTimerSubLine_Type = OctetString
_H3cVoAIfEMTimerSubLine_Object = MibTableColumn
h3cVoAIfEMTimerSubLine = _H3cVoAIfEMTimerSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 3, 4, 3, 1, 11),
    _H3cVoAIfEMTimerSubLine_Type()
)
h3cVoAIfEMTimerSubLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoAIfEMTimerSubLine.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOANALOGIF-MIB",
    **{"h3cVoiceAnalogInterface": h3cVoiceAnalogInterface,
       "h3cVoAnalogIfCommonObjects": h3cVoAnalogIfCommonObjects,
       "h3cVoAnalogIfCommonCfgTable": h3cVoAnalogIfCommonCfgTable,
       "h3cVoAnalogIfCommonCfgEntry": h3cVoAnalogIfCommonCfgEntry,
       "h3cVoAIfCfgPortIndex": h3cVoAIfCfgPortIndex,
       "h3cVoAIfCfgPortType": h3cVoAIfCfgPortType,
       "h3cVoAIfCfgPortSubLine": h3cVoAIfCfgPortSubLine,
       "h3cVoAnalogIfFXSObjects": h3cVoAnalogIfFXSObjects,
       "h3cVoAnalogIfFXSCfgTable": h3cVoAnalogIfFXSCfgTable,
       "h3cVoAnalogIfFXSCfgEntry": h3cVoAnalogIfFXSCfgEntry,
       "h3cVoAIfFXSCfgPortIndex": h3cVoAIfFXSCfgPortIndex,
       "h3cVoAIfFXSCfgCidDisplay": h3cVoAIfFXSCfgCidDisplay,
       "h3cVoAIfFXSCfgCidSend": h3cVoAIfFXSCfgCidSend,
       "h3cVoAIfFXSCfgCidType": h3cVoAIfFXSCfgCidType,
       "h3cVoAIfFXSCfgSubLine": h3cVoAIfFXSCfgSubLine,
       "h3cVoAnalogIfFXSTimerTable": h3cVoAnalogIfFXSTimerTable,
       "h3cVoAnalogIfFXSTimerEntry": h3cVoAnalogIfFXSTimerEntry,
       "h3cVoAIfFXSTimerPortIndex": h3cVoAIfFXSTimerPortIndex,
       "h3cVoAIfFXSTimerDialInterval": h3cVoAIfFXSTimerDialInterval,
       "h3cVoAIfFXSTimerFirstDial": h3cVoAIfFXSTimerFirstDial,
       "h3cVoAIfFXSTimerRingBack": h3cVoAIfFXSTimerRingBack,
       "h3cVoAIfFXSTimerSubLine": h3cVoAIfFXSTimerSubLine,
       "h3cVoAnalogIfFXOObjects": h3cVoAnalogIfFXOObjects,
       "h3cVoAnalogIfFXOCfgTable": h3cVoAnalogIfFXOCfgTable,
       "h3cVoAnalogIfFXOCfgEntry": h3cVoAnalogIfFXOCfgEntry,
       "h3cVoAIfFXOCfgPortIndex": h3cVoAIfFXOCfgPortIndex,
       "h3cVoAIfFXOCfgArea": h3cVoAIfFXOCfgArea,
       "h3cVoAIfFXOPreDialDelay": h3cVoAIfFXOPreDialDelay,
       "h3cVoAIfFXOCfgPortImpedance": h3cVoAIfFXOCfgPortImpedance,
       "h3cVoAIfFXOCfgCidEnable": h3cVoAIfFXOCfgCidEnable,
       "h3cVoAnalogIfFXOCfgCidSend": h3cVoAnalogIfFXOCfgCidSend,
       "h3cVoAIfFXOCfgCidType": h3cVoAIfFXOCfgCidType,
       "h3cVoAIfFXOCfgSubLine": h3cVoAIfFXOCfgSubLine,
       "h3cVoAnalogIfFXOTimerTable": h3cVoAnalogIfFXOTimerTable,
       "h3cVoAnalogIfFXOTimerEntry": h3cVoAnalogIfFXOTimerEntry,
       "h3cVoAIfFXOTimerPortIndex": h3cVoAIfFXOTimerPortIndex,
       "h3cVoAIfFXOTimerDtmf": h3cVoAIfFXOTimerDtmf,
       "h3cVoAIfFXOTimerDtmfInterval": h3cVoAIfFXOTimerDtmfInterval,
       "h3cVoAIfFXOTimerDialInterval": h3cVoAIfFXOTimerDialInterval,
       "h3cVoAIfFXOTimerFirstDial": h3cVoAIfFXOTimerFirstDial,
       "h3cVoAIfFXOTimerRingBack": h3cVoAIfFXOTimerRingBack,
       "h3cVoAIfFXOTimerSubLine": h3cVoAIfFXOTimerSubLine,
       "h3cVoAnalogIfEMObjects": h3cVoAnalogIfEMObjects,
       "h3cVoAnalogIfEMCfgTable": h3cVoAnalogIfEMCfgTable,
       "h3cVoAnalogIfEMCfgEntry": h3cVoAnalogIfEMCfgEntry,
       "h3cVoAIfEMCfgPortIndex": h3cVoAIfEMCfgPortIndex,
       "h3cVoAIfEMCfgSignalMode": h3cVoAIfEMCfgSignalMode,
       "h3cVoAIfEMCfgPhyParm": h3cVoAIfEMCfgPhyParm,
       "h3cVoAIfEMCfgPhyType": h3cVoAIfEMCfgPhyType,
       "h3cVoAIfEMCfgTimeoutRing": h3cVoAIfEMCfgTimeoutRing,
       "h3cVoAIfEMCfgTimeoutWaitDigit": h3cVoAIfEMCfgTimeoutWaitDigit,
       "h3cVoAIfEMCfgSubLine": h3cVoAIfEMCfgSubLine,
       "h3cVoAnalogIfEMTimerTable": h3cVoAnalogIfEMTimerTable,
       "h3cVoAnalogIfEMTimerEntry": h3cVoAnalogIfEMTimerEntry,
       "h3cVoAIfEMTimerPortIndex": h3cVoAIfEMTimerPortIndex,
       "h3cVoAIfEMTimerDtmf": h3cVoAIfEMTimerDtmf,
       "h3cVoAIfEMTimerDtmfInterval": h3cVoAIfEMTimerDtmfInterval,
       "h3cVoAIfEMTimerSendWink": h3cVoAIfEMTimerSendWink,
       "h3cVoAIfEMTimerWinkRising": h3cVoAIfEMTimerWinkRising,
       "h3cVoAIfEMTimerWinkHold": h3cVoAIfEMTimerWinkHold,
       "h3cVoAIfEMTimerDialoutDelay": h3cVoAIfEMTimerDialoutDelay,
       "h3cVoAIfEMTimerDelayRising": h3cVoAIfEMTimerDelayRising,
       "h3cVoAIfEMTimerDelayHold": h3cVoAIfEMTimerDelayHold,
       "h3cVoAIfEMTimerSubLine": h3cVoAIfEMTimerSubLine}
)
