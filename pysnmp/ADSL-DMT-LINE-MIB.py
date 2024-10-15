# SNMP MIB module (ADSL-DMT-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADSL-DMT-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:55 2024
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

(adslLCSMib,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLCSMib",
    "adslLineConfProfileName")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adslLineDmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdslLineDmtMIBObjects_ObjectIdentity = ObjectIdentity
adslLineDmtMIBObjects = _AdslLineDmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1)
)
_AdslLineDmtTable_Object = MibTable
adslLineDmtTable = _AdslLineDmtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adslLineDmtTable.setStatus("current")
_AdslLineDmtEntry_Object = MibTableRow
adslLineDmtEntry = _AdslLineDmtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 1, 1)
)
adslLineDmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslLineDmtEntry.setStatus("current")


class _AdslLineDmtTrellis_Type(Integer32):
    """Custom type adslLineDmtTrellis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trellisOff", 2),
          ("trellisOn", 1))
    )


_AdslLineDmtTrellis_Type.__name__ = "Integer32"
_AdslLineDmtTrellis_Object = MibTableColumn
adslLineDmtTrellis = _AdslLineDmtTrellis_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 1, 1, 1),
    _AdslLineDmtTrellis_Type()
)
adslLineDmtTrellis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineDmtTrellis.setStatus("current")


class _AdslLineDmtEOC_Type(Integer32):
    """Custom type adslLineDmtEOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("streaming", 3),
          ("transaction", 2),
          ("unknown", 1))
    )


_AdslLineDmtEOC_Type.__name__ = "Integer32"
_AdslLineDmtEOC_Object = MibTableColumn
adslLineDmtEOC = _AdslLineDmtEOC_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 1, 1, 2),
    _AdslLineDmtEOC_Type()
)
adslLineDmtEOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineDmtEOC.setStatus("current")
_AdslAtucDmtPhysTable_Object = MibTable
adslAtucDmtPhysTable = _AdslAtucDmtPhysTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 2)
)
if mibBuilder.loadTexts:
    adslAtucDmtPhysTable.setStatus("current")
_AdslAtucDmtPhysEntry_Object = MibTableRow
adslAtucDmtPhysEntry = _AdslAtucDmtPhysEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 2, 1)
)
adslAtucDmtPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAtucDmtPhysEntry.setStatus("current")


class _AdslAtucDmtIssue_Type(Integer32):
    """Custom type adslAtucDmtIssue based on Integer32"""
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
        *(("etsiIssue1", 6),
          ("gdmtIssue1", 5),
          ("other", 1),
          ("t1413Issue1", 2),
          ("t1413Issue2", 3),
          ("t1413Issue3", 4))
    )


_AdslAtucDmtIssue_Type.__name__ = "Integer32"
_AdslAtucDmtIssue_Object = MibTableColumn
adslAtucDmtIssue = _AdslAtucDmtIssue_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 2, 1, 1),
    _AdslAtucDmtIssue_Type()
)
adslAtucDmtIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDmtIssue.setStatus("current")


class _AdslAtucDmtState_Type(Integer32):
    """Custom type adslAtucDmtState based on Integer32"""
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
        *(("activating", 7),
          ("analyzing", 9),
          ("configure", 3),
          ("exchange", 10),
          ("idle", 4),
          ("notResponding", 12),
          ("other", 1),
          ("powerUp", 2),
          ("quiet", 5),
          ("steadyState", 11),
          ("tone", 6),
          ("training", 8))
    )


_AdslAtucDmtState_Type.__name__ = "Integer32"
_AdslAtucDmtState_Object = MibTableColumn
adslAtucDmtState = _AdslAtucDmtState_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 2, 1, 2),
    _AdslAtucDmtState_Type()
)
adslAtucDmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDmtState.setStatus("current")


class _AdslAtucDmtInterleavePath_Type(Integer32):
    """Custom type adslAtucDmtInterleavePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as0", 2),
          ("as1", 3),
          ("none", 1))
    )


_AdslAtucDmtInterleavePath_Type.__name__ = "Integer32"
_AdslAtucDmtInterleavePath_Object = MibTableColumn
adslAtucDmtInterleavePath = _AdslAtucDmtInterleavePath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 2, 1, 3),
    _AdslAtucDmtInterleavePath_Type()
)
adslAtucDmtInterleavePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDmtInterleavePath.setStatus("current")


class _AdslAtucDmtFastPath_Type(Integer32):
    """Custom type adslAtucDmtFastPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as0", 2),
          ("as1", 3),
          ("none", 1))
    )


_AdslAtucDmtFastPath_Type.__name__ = "Integer32"
_AdslAtucDmtFastPath_Object = MibTableColumn
adslAtucDmtFastPath = _AdslAtucDmtFastPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 2, 1, 4),
    _AdslAtucDmtFastPath_Type()
)
adslAtucDmtFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDmtFastPath.setStatus("current")
_AdslAturDmtPhysTable_Object = MibTable
adslAturDmtPhysTable = _AdslAturDmtPhysTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 3)
)
if mibBuilder.loadTexts:
    adslAturDmtPhysTable.setStatus("current")
_AdslAturDmtPhysEntry_Object = MibTableRow
adslAturDmtPhysEntry = _AdslAturDmtPhysEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 3, 1)
)
adslAturDmtPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAturDmtPhysEntry.setStatus("current")


class _AdslAturDmtIssue_Type(Integer32):
    """Custom type adslAturDmtIssue based on Integer32"""
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
        *(("etsiIssue1", 6),
          ("gdmtIssue1", 5),
          ("other", 1),
          ("t1413Issue1", 2),
          ("t1413Issue2", 3),
          ("t1413Issue3", 4))
    )


_AdslAturDmtIssue_Type.__name__ = "Integer32"
_AdslAturDmtIssue_Object = MibTableColumn
adslAturDmtIssue = _AdslAturDmtIssue_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 3, 1, 1),
    _AdslAturDmtIssue_Type()
)
adslAturDmtIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDmtIssue.setStatus("current")


class _AdslAturDmtState_Type(Integer32):
    """Custom type adslAturDmtState based on Integer32"""
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
        *(("activating", 2),
          ("analyzing", 4),
          ("exchange", 5),
          ("other", 1),
          ("steadyState", 6),
          ("training", 3))
    )


_AdslAturDmtState_Type.__name__ = "Integer32"
_AdslAturDmtState_Object = MibTableColumn
adslAturDmtState = _AdslAturDmtState_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 3, 1, 2),
    _AdslAturDmtState_Type()
)
adslAturDmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDmtState.setStatus("current")


class _AdslAturDmtInterleavePath_Type(Integer32):
    """Custom type adslAturDmtInterleavePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ls0", 2),
          ("ls1", 3),
          ("none", 1))
    )


_AdslAturDmtInterleavePath_Type.__name__ = "Integer32"
_AdslAturDmtInterleavePath_Object = MibTableColumn
adslAturDmtInterleavePath = _AdslAturDmtInterleavePath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 3, 1, 3),
    _AdslAturDmtInterleavePath_Type()
)
adslAturDmtInterleavePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDmtInterleavePath.setStatus("current")


class _AdslAturDmtFastPath_Type(Integer32):
    """Custom type adslAturDmtFastPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ls0", 2),
          ("ls1", 3),
          ("none", 1))
    )


_AdslAturDmtFastPath_Type.__name__ = "Integer32"
_AdslAturDmtFastPath_Object = MibTableColumn
adslAturDmtFastPath = _AdslAturDmtFastPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 3, 1, 4),
    _AdslAturDmtFastPath_Type()
)
adslAturDmtFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDmtFastPath.setStatus("current")
_AdslAtucDmtChanTable_ObjectIdentity = ObjectIdentity
adslAtucDmtChanTable = _AdslAtucDmtChanTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 4)
)
_AdslAturDmtChanTable_ObjectIdentity = ObjectIdentity
adslAturDmtChanTable = _AdslAturDmtChanTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 5)
)
_AdslAtucDmtPerfDataTable_ObjectIdentity = ObjectIdentity
adslAtucDmtPerfDataTable = _AdslAtucDmtPerfDataTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 6)
)
_AdslAturDmtPerfDataTable_ObjectIdentity = ObjectIdentity
adslAturDmtPerfDataTable = _AdslAturDmtPerfDataTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 7)
)
_AdslAtucDmtIntervalTable_ObjectIdentity = ObjectIdentity
adslAtucDmtIntervalTable = _AdslAtucDmtIntervalTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 8)
)
_AdslAturDmtIntervalTable_ObjectIdentity = ObjectIdentity
adslAturDmtIntervalTable = _AdslAturDmtIntervalTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 9)
)
_AdslAtucDmtChanPerfDataTable_ObjectIdentity = ObjectIdentity
adslAtucDmtChanPerfDataTable = _AdslAtucDmtChanPerfDataTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 10)
)
_AdslAturDmtChanPerfDataTable_ObjectIdentity = ObjectIdentity
adslAturDmtChanPerfDataTable = _AdslAturDmtChanPerfDataTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 11)
)
_AdslAtucDmtChanIntervalTable_ObjectIdentity = ObjectIdentity
adslAtucDmtChanIntervalTable = _AdslAtucDmtChanIntervalTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 12)
)
_AdslAturDmtChanIntervalTable_ObjectIdentity = ObjectIdentity
adslAturDmtChanIntervalTable = _AdslAturDmtChanIntervalTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 13)
)
_AdslLineDmtConfProfileIndexNext_ObjectIdentity = ObjectIdentity
adslLineDmtConfProfileIndexNext = _AdslLineDmtConfProfileIndexNext_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 14)
)
_AdslLineDmtConfProfileTable_Object = MibTable
adslLineDmtConfProfileTable = _AdslLineDmtConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15)
)
if mibBuilder.loadTexts:
    adslLineDmtConfProfileTable.setStatus("current")
_AdslLineDmtConfProfileEntry_Object = MibTableRow
adslLineDmtConfProfileEntry = _AdslLineDmtConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1)
)
adslLineDmtConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    adslLineDmtConfProfileEntry.setStatus("current")


class _AdslAtucDmtConfFreqBins_Type(OctetString):
    """Custom type adslAtucDmtConfFreqBins based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AdslAtucDmtConfFreqBins_Type.__name__ = "OctetString"
_AdslAtucDmtConfFreqBins_Object = MibTableColumn
adslAtucDmtConfFreqBins = _AdslAtucDmtConfFreqBins_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 1),
    _AdslAtucDmtConfFreqBins_Type()
)
adslAtucDmtConfFreqBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucDmtConfFreqBins.setStatus("current")


class _AdslAturDmtConfFreqBins_Type(OctetString):
    """Custom type adslAturDmtConfFreqBins based on OctetString"""
    defaultHexValue = "0000000000000000000000000000000000000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AdslAturDmtConfFreqBins_Type.__name__ = "OctetString"
_AdslAturDmtConfFreqBins_Object = MibTableColumn
adslAturDmtConfFreqBins = _AdslAturDmtConfFreqBins_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 2),
    _AdslAturDmtConfFreqBins_Type()
)
adslAturDmtConfFreqBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturDmtConfFreqBins.setStatus("current")


class _AdslLineDmtConfMode_Type(Integer32):
    """Custom type adslLineDmtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("echoCancel", 1),
          ("freqDivMux", 2))
    )


_AdslLineDmtConfMode_Type.__name__ = "Integer32"
_AdslLineDmtConfMode_Object = MibTableColumn
adslLineDmtConfMode = _AdslLineDmtConfMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 3),
    _AdslLineDmtConfMode_Type()
)
adslLineDmtConfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslLineDmtConfMode.setStatus("current")


class _AdslLineDmtConfTrellis_Type(Integer32):
    """Custom type adslLineDmtConfTrellis based on Integer32"""
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


_AdslLineDmtConfTrellis_Type.__name__ = "Integer32"
_AdslLineDmtConfTrellis_Object = MibTableColumn
adslLineDmtConfTrellis = _AdslLineDmtConfTrellis_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 4),
    _AdslLineDmtConfTrellis_Type()
)
adslLineDmtConfTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslLineDmtConfTrellis.setStatus("current")


class _AdslLineDmtConfEOC_Type(Integer32):
    """Custom type adslLineDmtConfEOC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("streaming", 2))
    )


_AdslLineDmtConfEOC_Type.__name__ = "Integer32"
_AdslLineDmtConfEOC_Object = MibTableColumn
adslLineDmtConfEOC = _AdslLineDmtConfEOC_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 5),
    _AdslLineDmtConfEOC_Type()
)
adslLineDmtConfEOC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslLineDmtConfEOC.setStatus("current")


class _AdslAtucDmtConfInterleavePath_Type(Integer32):
    """Custom type adslAtucDmtConfInterleavePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as0", 2),
          ("as1", 3),
          ("none", 1))
    )


_AdslAtucDmtConfInterleavePath_Type.__name__ = "Integer32"
_AdslAtucDmtConfInterleavePath_Object = MibTableColumn
adslAtucDmtConfInterleavePath = _AdslAtucDmtConfInterleavePath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 6),
    _AdslAtucDmtConfInterleavePath_Type()
)
adslAtucDmtConfInterleavePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucDmtConfInterleavePath.setStatus("current")


class _AdslAtucDmtConfFastPath_Type(Integer32):
    """Custom type adslAtucDmtConfFastPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as0", 2),
          ("as1", 3),
          ("none", 1))
    )


_AdslAtucDmtConfFastPath_Type.__name__ = "Integer32"
_AdslAtucDmtConfFastPath_Object = MibTableColumn
adslAtucDmtConfFastPath = _AdslAtucDmtConfFastPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 7),
    _AdslAtucDmtConfFastPath_Type()
)
adslAtucDmtConfFastPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucDmtConfFastPath.setStatus("current")


class _AdslAturDmtConfInterleavePath_Type(Integer32):
    """Custom type adslAturDmtConfInterleavePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ls0", 2),
          ("ls1", 3),
          ("none", 1))
    )


_AdslAturDmtConfInterleavePath_Type.__name__ = "Integer32"
_AdslAturDmtConfInterleavePath_Object = MibTableColumn
adslAturDmtConfInterleavePath = _AdslAturDmtConfInterleavePath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 8),
    _AdslAturDmtConfInterleavePath_Type()
)
adslAturDmtConfInterleavePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturDmtConfInterleavePath.setStatus("current")


class _AdslAturDmtConfFastPath_Type(Integer32):
    """Custom type adslAturDmtConfFastPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ls0", 2),
          ("ls1", 3),
          ("none", 1))
    )


_AdslAturDmtConfFastPath_Type.__name__ = "Integer32"
_AdslAturDmtConfFastPath_Object = MibTableColumn
adslAturDmtConfFastPath = _AdslAturDmtConfFastPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 15, 1, 9),
    _AdslAturDmtConfFastPath_Type()
)
adslAturDmtConfFastPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturDmtConfFastPath.setStatus("current")
_AdslLineDmtAlarmConfProfileIndexNext_ObjectIdentity = ObjectIdentity
adslLineDmtAlarmConfProfileIndexNext = _AdslLineDmtAlarmConfProfileIndexNext_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 16)
)
_AdslLineDmtAlarmConfProfileTable_ObjectIdentity = ObjectIdentity
adslLineDmtAlarmConfProfileTable = _AdslLineDmtAlarmConfProfileTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 1, 17)
)
_AdslDmtLineMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
adslDmtLineMIBNotificationsPrefix = _AdslDmtLineMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 2)
)
_AdslDmtLineMIBNotifications_ObjectIdentity = ObjectIdentity
adslDmtLineMIBNotifications = _AdslDmtLineMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 2, 0)
)
_AdslLineDmtMIBConformance_ObjectIdentity = ObjectIdentity
adslLineDmtMIBConformance = _AdslLineDmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3)
)
_AdslLineDmtMIBCompliances_ObjectIdentity = ObjectIdentity
adslLineDmtMIBCompliances = _AdslLineDmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 1)
)
_AdslLineDmtMIBGroups_ObjectIdentity = ObjectIdentity
adslLineDmtMIBGroups = _AdslLineDmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 2)
)

# Managed Objects groups

adslLineDmtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 2, 1)
)
adslLineDmtGroup.setObjects(
      *(("ADSL-DMT-LINE-MIB", "adslLineDmtTrellis"),
        ("ADSL-DMT-LINE-MIB", "adslLineDmtEOC"))
)
if mibBuilder.loadTexts:
    adslLineDmtGroup.setStatus("current")

adslAtucDmtPhysGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 2, 2)
)
adslAtucDmtPhysGroup.setObjects(
      *(("ADSL-DMT-LINE-MIB", "adslAtucDmtIssue"),
        ("ADSL-DMT-LINE-MIB", "adslAtucDmtState"),
        ("ADSL-DMT-LINE-MIB", "adslAtucDmtInterleavePath"),
        ("ADSL-DMT-LINE-MIB", "adslAtucDmtFastPath"))
)
if mibBuilder.loadTexts:
    adslAtucDmtPhysGroup.setStatus("current")

adslAturDmtPhysGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 2, 3)
)
adslAturDmtPhysGroup.setObjects(
      *(("ADSL-DMT-LINE-MIB", "adslAturDmtIssue"),
        ("ADSL-DMT-LINE-MIB", "adslAturDmtState"),
        ("ADSL-DMT-LINE-MIB", "adslAturDmtInterleavePath"),
        ("ADSL-DMT-LINE-MIB", "adslAturDmtFastPath"))
)
if mibBuilder.loadTexts:
    adslAturDmtPhysGroup.setStatus("current")

adslLineDmtConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 2, 4)
)
adslLineDmtConfProfileGroup.setObjects(
      *(("ADSL-DMT-LINE-MIB", "adslAtucDmtConfFreqBins"),
        ("ADSL-DMT-LINE-MIB", "adslAturDmtConfFreqBins"),
        ("ADSL-DMT-LINE-MIB", "adslLineDmtConfMode"),
        ("ADSL-DMT-LINE-MIB", "adslLineDmtConfTrellis"),
        ("ADSL-DMT-LINE-MIB", "adslLineDmtConfEOC"),
        ("ADSL-DMT-LINE-MIB", "adslAtucDmtConfInterleavePath"),
        ("ADSL-DMT-LINE-MIB", "adslAtucDmtConfFastPath"),
        ("ADSL-DMT-LINE-MIB", "adslAturDmtConfInterleavePath"),
        ("ADSL-DMT-LINE-MIB", "adslAturDmtConfFastPath"))
)
if mibBuilder.loadTexts:
    adslLineDmtConfProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adslDMTLineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    adslDMTLineMibCompliance.setStatus(
        "current"
    )

adslLineDmtMIBAturCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    adslLineDmtMIBAturCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADSL-DMT-LINE-MIB",
    **{"adslLineDmtMIB": adslLineDmtMIB,
       "adslLineDmtMIBObjects": adslLineDmtMIBObjects,
       "adslLineDmtTable": adslLineDmtTable,
       "adslLineDmtEntry": adslLineDmtEntry,
       "adslLineDmtTrellis": adslLineDmtTrellis,
       "adslLineDmtEOC": adslLineDmtEOC,
       "adslAtucDmtPhysTable": adslAtucDmtPhysTable,
       "adslAtucDmtPhysEntry": adslAtucDmtPhysEntry,
       "adslAtucDmtIssue": adslAtucDmtIssue,
       "adslAtucDmtState": adslAtucDmtState,
       "adslAtucDmtInterleavePath": adslAtucDmtInterleavePath,
       "adslAtucDmtFastPath": adslAtucDmtFastPath,
       "adslAturDmtPhysTable": adslAturDmtPhysTable,
       "adslAturDmtPhysEntry": adslAturDmtPhysEntry,
       "adslAturDmtIssue": adslAturDmtIssue,
       "adslAturDmtState": adslAturDmtState,
       "adslAturDmtInterleavePath": adslAturDmtInterleavePath,
       "adslAturDmtFastPath": adslAturDmtFastPath,
       "adslAtucDmtChanTable": adslAtucDmtChanTable,
       "adslAturDmtChanTable": adslAturDmtChanTable,
       "adslAtucDmtPerfDataTable": adslAtucDmtPerfDataTable,
       "adslAturDmtPerfDataTable": adslAturDmtPerfDataTable,
       "adslAtucDmtIntervalTable": adslAtucDmtIntervalTable,
       "adslAturDmtIntervalTable": adslAturDmtIntervalTable,
       "adslAtucDmtChanPerfDataTable": adslAtucDmtChanPerfDataTable,
       "adslAturDmtChanPerfDataTable": adslAturDmtChanPerfDataTable,
       "adslAtucDmtChanIntervalTable": adslAtucDmtChanIntervalTable,
       "adslAturDmtChanIntervalTable": adslAturDmtChanIntervalTable,
       "adslLineDmtConfProfileIndexNext": adslLineDmtConfProfileIndexNext,
       "adslLineDmtConfProfileTable": adslLineDmtConfProfileTable,
       "adslLineDmtConfProfileEntry": adslLineDmtConfProfileEntry,
       "adslAtucDmtConfFreqBins": adslAtucDmtConfFreqBins,
       "adslAturDmtConfFreqBins": adslAturDmtConfFreqBins,
       "adslLineDmtConfMode": adslLineDmtConfMode,
       "adslLineDmtConfTrellis": adslLineDmtConfTrellis,
       "adslLineDmtConfEOC": adslLineDmtConfEOC,
       "adslAtucDmtConfInterleavePath": adslAtucDmtConfInterleavePath,
       "adslAtucDmtConfFastPath": adslAtucDmtConfFastPath,
       "adslAturDmtConfInterleavePath": adslAturDmtConfInterleavePath,
       "adslAturDmtConfFastPath": adslAturDmtConfFastPath,
       "adslLineDmtAlarmConfProfileIndexNext": adslLineDmtAlarmConfProfileIndexNext,
       "adslLineDmtAlarmConfProfileTable": adslLineDmtAlarmConfProfileTable,
       "adslDmtLineMIBNotificationsPrefix": adslDmtLineMIBNotificationsPrefix,
       "adslDmtLineMIBNotifications": adslDmtLineMIBNotifications,
       "adslLineDmtMIBConformance": adslLineDmtMIBConformance,
       "adslLineDmtMIBCompliances": adslLineDmtMIBCompliances,
       "adslDMTLineMibCompliance": adslDMTLineMibCompliance,
       "adslLineDmtMIBAturCompliance": adslLineDmtMIBAturCompliance,
       "adslLineDmtMIBGroups": adslLineDmtMIBGroups,
       "adslLineDmtGroup": adslLineDmtGroup,
       "adslAtucDmtPhysGroup": adslAtucDmtPhysGroup,
       "adslAturDmtPhysGroup": adslAturDmtPhysGroup,
       "adslLineDmtConfProfileGroup": adslLineDmtConfProfileGroup}
)
