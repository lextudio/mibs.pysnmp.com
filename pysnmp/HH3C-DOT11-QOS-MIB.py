# SNMP MIB module (HH3C-DOT11-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:52 2024
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

(Hh3cDot11ObjectIDType,
 Hh3cDot11QosAcType,
 Hh3cDot11RadioElementIndex,
 Hh3cDot11RadioScopeType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11QosAcType",
    "Hh3cDot11RadioElementIndex",
    "Hh3cDot11RadioScopeType",
    "hh3cDot11")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11QoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9)
)
hh3cDot11QoS.setRevisions(
        ("2008-07-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11WMMSVPMapAC(Integer32, TextualConvention):
    status = "current"
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
        *(("acbe", 2),
          ("acbk", 1),
          ("acvi", 3),
          ("acvo", 4),
          ("disable", 5))
    )



class Hh3cDot11WMMCACPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelUtilization", 1),
          ("userNumber", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11WmmCfgGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WmmCfgGroup = _Hh3cDot11WmmCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1)
)
_Hh3cDot11RadioWmmCfgTable_Object = MibTable
hh3cDot11RadioWmmCfgTable = _Hh3cDot11RadioWmmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmCfgTable.setStatus("current")
_Hh3cDot11RadioWmmCfgEntry_Object = MibTableRow
hh3cDot11RadioWmmCfgEntry = _Hh3cDot11RadioWmmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1)
)
hh3cDot11RadioWmmCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WmmRadioIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmCfgEntry.setStatus("current")
_Hh3cDot11WmmRadioIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11WmmRadioIndex_Object = MibTableColumn
hh3cDot11WmmRadioIndex = _Hh3cDot11WmmRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 1),
    _Hh3cDot11WmmRadioIndex_Type()
)
hh3cDot11WmmRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WmmRadioIndex.setStatus("current")
_Hh3cDot11RadioWmmEnabled_Type = TruthValue
_Hh3cDot11RadioWmmEnabled_Object = MibTableColumn
hh3cDot11RadioWmmEnabled = _Hh3cDot11RadioWmmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 2),
    _Hh3cDot11RadioWmmEnabled_Type()
)
hh3cDot11RadioWmmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEnabled.setStatus("current")
_Hh3cDot11RadioSVPMapToAC_Type = Hh3cDot11WMMSVPMapAC
_Hh3cDot11RadioSVPMapToAC_Object = MibTableColumn
hh3cDot11RadioSVPMapToAC = _Hh3cDot11RadioSVPMapToAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 3),
    _Hh3cDot11RadioSVPMapToAC_Type()
)
hh3cDot11RadioSVPMapToAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioSVPMapToAC.setStatus("current")
_Hh3cDot11RadioCacPolicy_Type = Hh3cDot11WMMCACPolicy
_Hh3cDot11RadioCacPolicy_Object = MibTableColumn
hh3cDot11RadioCacPolicy = _Hh3cDot11RadioCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 4),
    _Hh3cDot11RadioCacPolicy_Type()
)
hh3cDot11RadioCacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCacPolicy.setStatus("current")


class _Hh3cDot11RadioCacChlUtlValue_Type(Integer32):
    """Custom type hh3cDot11RadioCacChlUtlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RadioCacChlUtlValue_Type.__name__ = "Integer32"
_Hh3cDot11RadioCacChlUtlValue_Object = MibTableColumn
hh3cDot11RadioCacChlUtlValue = _Hh3cDot11RadioCacChlUtlValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 5),
    _Hh3cDot11RadioCacChlUtlValue_Type()
)
hh3cDot11RadioCacChlUtlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCacChlUtlValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCacChlUtlValue.setUnits("percent")


class _Hh3cDot11RadioCacUserNum_Type(Integer32):
    """Custom type hh3cDot11RadioCacUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cDot11RadioCacUserNum_Type.__name__ = "Integer32"
_Hh3cDot11RadioCacUserNum_Object = MibTableColumn
hh3cDot11RadioCacUserNum = _Hh3cDot11RadioCacUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 6),
    _Hh3cDot11RadioCacUserNum_Type()
)
hh3cDot11RadioCacUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCacUserNum.setStatus("current")
_Hh3cDot11RadioWmmEdcaCfgTable_Object = MibTable
hh3cDot11RadioWmmEdcaCfgTable = _Hh3cDot11RadioWmmEdcaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEdcaCfgTable.setStatus("current")
_Hh3cDot11RadioWmmEdcaCfgEntry_Object = MibTableRow
hh3cDot11RadioWmmEdcaCfgEntry = _Hh3cDot11RadioWmmEdcaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1)
)
hh3cDot11RadioWmmEdcaCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WmmRadioIndex"),
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11RadioWmmAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEdcaCfgEntry.setStatus("current")
_Hh3cDot11RadioWmmAC_Type = Hh3cDot11QosAcType
_Hh3cDot11RadioWmmAC_Object = MibTableColumn
hh3cDot11RadioWmmAC = _Hh3cDot11RadioWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 1),
    _Hh3cDot11RadioWmmAC_Type()
)
hh3cDot11RadioWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmAC.setStatus("current")


class _Hh3cDot11RadioWmmAifsn_Type(Integer32):
    """Custom type hh3cDot11RadioWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cDot11RadioWmmAifsn_Type.__name__ = "Integer32"
_Hh3cDot11RadioWmmAifsn_Object = MibTableColumn
hh3cDot11RadioWmmAifsn = _Hh3cDot11RadioWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 2),
    _Hh3cDot11RadioWmmAifsn_Type()
)
hh3cDot11RadioWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmAifsn.setStatus("current")


class _Hh3cDot11RadioWmmEcwMin_Type(Integer32):
    """Custom type hh3cDot11RadioWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cDot11RadioWmmEcwMin_Type.__name__ = "Integer32"
_Hh3cDot11RadioWmmEcwMin_Object = MibTableColumn
hh3cDot11RadioWmmEcwMin = _Hh3cDot11RadioWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 3),
    _Hh3cDot11RadioWmmEcwMin_Type()
)
hh3cDot11RadioWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEcwMin.setStatus("current")


class _Hh3cDot11RadioWmmEcwMax_Type(Integer32):
    """Custom type hh3cDot11RadioWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cDot11RadioWmmEcwMax_Type.__name__ = "Integer32"
_Hh3cDot11RadioWmmEcwMax_Object = MibTableColumn
hh3cDot11RadioWmmEcwMax = _Hh3cDot11RadioWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 4),
    _Hh3cDot11RadioWmmEcwMax_Type()
)
hh3cDot11RadioWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEcwMax.setStatus("current")


class _Hh3cDot11RadioWmmTxoplimit_Type(Integer32):
    """Custom type hh3cDot11RadioWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11RadioWmmTxoplimit_Type.__name__ = "Integer32"
_Hh3cDot11RadioWmmTxoplimit_Object = MibTableColumn
hh3cDot11RadioWmmTxoplimit = _Hh3cDot11RadioWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 5),
    _Hh3cDot11RadioWmmTxoplimit_Type()
)
hh3cDot11RadioWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmTxoplimit.setStatus("current")
_Hh3cDot11RadioWmmNoAck_Type = TruthValue
_Hh3cDot11RadioWmmNoAck_Object = MibTableColumn
hh3cDot11RadioWmmNoAck = _Hh3cDot11RadioWmmNoAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 6),
    _Hh3cDot11RadioWmmNoAck_Type()
)
hh3cDot11RadioWmmNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmNoAck.setStatus("current")
_Hh3cDot11StationWmmEdcaTable_Object = MibTable
hh3cDot11StationWmmEdcaTable = _Hh3cDot11StationWmmEdcaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11StationWmmEdcaTable.setStatus("current")
_Hh3cDot11StationWmmEdcaEntry_Object = MibTableRow
hh3cDot11StationWmmEdcaEntry = _Hh3cDot11StationWmmEdcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1)
)
hh3cDot11StationWmmEdcaEntry.setIndexNames(
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WmmRadioIndex"),
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11StationWmmAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationWmmEdcaEntry.setStatus("current")
_Hh3cDot11StationWmmAC_Type = Hh3cDot11QosAcType
_Hh3cDot11StationWmmAC_Object = MibTableColumn
hh3cDot11StationWmmAC = _Hh3cDot11StationWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 1),
    _Hh3cDot11StationWmmAC_Type()
)
hh3cDot11StationWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmAC.setStatus("current")


class _Hh3cDot11StationWmmAifsn_Type(Integer32):
    """Custom type hh3cDot11StationWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Hh3cDot11StationWmmAifsn_Type.__name__ = "Integer32"
_Hh3cDot11StationWmmAifsn_Object = MibTableColumn
hh3cDot11StationWmmAifsn = _Hh3cDot11StationWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 2),
    _Hh3cDot11StationWmmAifsn_Type()
)
hh3cDot11StationWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmAifsn.setStatus("current")


class _Hh3cDot11StationWmmEcwMin_Type(Integer32):
    """Custom type hh3cDot11StationWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cDot11StationWmmEcwMin_Type.__name__ = "Integer32"
_Hh3cDot11StationWmmEcwMin_Object = MibTableColumn
hh3cDot11StationWmmEcwMin = _Hh3cDot11StationWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 3),
    _Hh3cDot11StationWmmEcwMin_Type()
)
hh3cDot11StationWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmEcwMin.setStatus("current")


class _Hh3cDot11StationWmmEcwMax_Type(Integer32):
    """Custom type hh3cDot11StationWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cDot11StationWmmEcwMax_Type.__name__ = "Integer32"
_Hh3cDot11StationWmmEcwMax_Object = MibTableColumn
hh3cDot11StationWmmEcwMax = _Hh3cDot11StationWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 4),
    _Hh3cDot11StationWmmEcwMax_Type()
)
hh3cDot11StationWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmEcwMax.setStatus("current")


class _Hh3cDot11StationWmmTxoplimit_Type(Integer32):
    """Custom type hh3cDot11StationWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11StationWmmTxoplimit_Type.__name__ = "Integer32"
_Hh3cDot11StationWmmTxoplimit_Object = MibTableColumn
hh3cDot11StationWmmTxoplimit = _Hh3cDot11StationWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 5),
    _Hh3cDot11StationWmmTxoplimit_Type()
)
hh3cDot11StationWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmTxoplimit.setStatus("current")
_Hh3cDot11StationWmmCacEnabled_Type = TruthValue
_Hh3cDot11StationWmmCacEnabled_Object = MibTableColumn
hh3cDot11StationWmmCacEnabled = _Hh3cDot11StationWmmCacEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 6),
    _Hh3cDot11StationWmmCacEnabled_Type()
)
hh3cDot11StationWmmCacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmCacEnabled.setStatus("current")
_Hh3cDot11WmmResetGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WmmResetGroup = _Hh3cDot11WmmResetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 4)
)
_Hh3cDot11WmmResetRadioByAP_Type = Integer32
_Hh3cDot11WmmResetRadioByAP_Object = MibScalar
hh3cDot11WmmResetRadioByAP = _Hh3cDot11WmmResetRadioByAP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 4, 1),
    _Hh3cDot11WmmResetRadioByAP_Type()
)
hh3cDot11WmmResetRadioByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WmmResetRadioByAP.setStatus("current")
_Hh3cDot11WmmResetStationByAP_Type = Integer32
_Hh3cDot11WmmResetStationByAP_Object = MibScalar
hh3cDot11WmmResetStationByAP = _Hh3cDot11WmmResetStationByAP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 4, 2),
    _Hh3cDot11WmmResetStationByAP_Type()
)
hh3cDot11WmmResetStationByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WmmResetStationByAP.setStatus("current")
_Hh3cDot11RadioWmmEdcaCfg2Table_Object = MibTable
hh3cDot11RadioWmmEdcaCfg2Table = _Hh3cDot11RadioWmmEdcaCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEdcaCfg2Table.setStatus("current")
_Hh3cDot11RadioWmmEdcaCfg2Entry_Object = MibTableRow
hh3cDot11RadioWmmEdcaCfg2Entry = _Hh3cDot11RadioWmmEdcaCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1)
)
hh3cDot11RadioWmmEdcaCfg2Entry.setIndexNames(
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WMMAPSerialID"),
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WMMRdId"),
    (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11RdWmmAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWmmEdcaCfg2Entry.setStatus("current")
_Hh3cDot11WMMAPSerialID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11WMMAPSerialID_Object = MibTableColumn
hh3cDot11WMMAPSerialID = _Hh3cDot11WMMAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 1),
    _Hh3cDot11WMMAPSerialID_Type()
)
hh3cDot11WMMAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WMMAPSerialID.setStatus("current")
_Hh3cDot11WMMRdId_Type = Hh3cDot11RadioScopeType
_Hh3cDot11WMMRdId_Object = MibTableColumn
hh3cDot11WMMRdId = _Hh3cDot11WMMRdId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 2),
    _Hh3cDot11WMMRdId_Type()
)
hh3cDot11WMMRdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WMMRdId.setStatus("current")
_Hh3cDot11RdWmmAC_Type = Hh3cDot11QosAcType
_Hh3cDot11RdWmmAC_Object = MibTableColumn
hh3cDot11RdWmmAC = _Hh3cDot11RdWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 3),
    _Hh3cDot11RdWmmAC_Type()
)
hh3cDot11RdWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RdWmmAC.setStatus("current")


class _Hh3cDot11RdWmmAifsn_Type(Integer32):
    """Custom type hh3cDot11RdWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cDot11RdWmmAifsn_Type.__name__ = "Integer32"
_Hh3cDot11RdWmmAifsn_Object = MibTableColumn
hh3cDot11RdWmmAifsn = _Hh3cDot11RdWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 4),
    _Hh3cDot11RdWmmAifsn_Type()
)
hh3cDot11RdWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RdWmmAifsn.setStatus("current")


class _Hh3cDot11RdWmmEcwMin_Type(Integer32):
    """Custom type hh3cDot11RdWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cDot11RdWmmEcwMin_Type.__name__ = "Integer32"
_Hh3cDot11RdWmmEcwMin_Object = MibTableColumn
hh3cDot11RdWmmEcwMin = _Hh3cDot11RdWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 5),
    _Hh3cDot11RdWmmEcwMin_Type()
)
hh3cDot11RdWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RdWmmEcwMin.setStatus("current")


class _Hh3cDot11RdWmmEcwMax_Type(Integer32):
    """Custom type hh3cDot11RdWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cDot11RdWmmEcwMax_Type.__name__ = "Integer32"
_Hh3cDot11RdWmmEcwMax_Object = MibTableColumn
hh3cDot11RdWmmEcwMax = _Hh3cDot11RdWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 6),
    _Hh3cDot11RdWmmEcwMax_Type()
)
hh3cDot11RdWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RdWmmEcwMax.setStatus("current")


class _Hh3cDot11RdWmmTxoplimit_Type(Integer32):
    """Custom type hh3cDot11RdWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11RdWmmTxoplimit_Type.__name__ = "Integer32"
_Hh3cDot11RdWmmTxoplimit_Object = MibTableColumn
hh3cDot11RdWmmTxoplimit = _Hh3cDot11RdWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 7),
    _Hh3cDot11RdWmmTxoplimit_Type()
)
hh3cDot11RdWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RdWmmTxoplimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-QOS-MIB",
    **{"Hh3cDot11WMMSVPMapAC": Hh3cDot11WMMSVPMapAC,
       "Hh3cDot11WMMCACPolicy": Hh3cDot11WMMCACPolicy,
       "hh3cDot11QoS": hh3cDot11QoS,
       "hh3cDot11WmmCfgGroup": hh3cDot11WmmCfgGroup,
       "hh3cDot11RadioWmmCfgTable": hh3cDot11RadioWmmCfgTable,
       "hh3cDot11RadioWmmCfgEntry": hh3cDot11RadioWmmCfgEntry,
       "hh3cDot11WmmRadioIndex": hh3cDot11WmmRadioIndex,
       "hh3cDot11RadioWmmEnabled": hh3cDot11RadioWmmEnabled,
       "hh3cDot11RadioSVPMapToAC": hh3cDot11RadioSVPMapToAC,
       "hh3cDot11RadioCacPolicy": hh3cDot11RadioCacPolicy,
       "hh3cDot11RadioCacChlUtlValue": hh3cDot11RadioCacChlUtlValue,
       "hh3cDot11RadioCacUserNum": hh3cDot11RadioCacUserNum,
       "hh3cDot11RadioWmmEdcaCfgTable": hh3cDot11RadioWmmEdcaCfgTable,
       "hh3cDot11RadioWmmEdcaCfgEntry": hh3cDot11RadioWmmEdcaCfgEntry,
       "hh3cDot11RadioWmmAC": hh3cDot11RadioWmmAC,
       "hh3cDot11RadioWmmAifsn": hh3cDot11RadioWmmAifsn,
       "hh3cDot11RadioWmmEcwMin": hh3cDot11RadioWmmEcwMin,
       "hh3cDot11RadioWmmEcwMax": hh3cDot11RadioWmmEcwMax,
       "hh3cDot11RadioWmmTxoplimit": hh3cDot11RadioWmmTxoplimit,
       "hh3cDot11RadioWmmNoAck": hh3cDot11RadioWmmNoAck,
       "hh3cDot11StationWmmEdcaTable": hh3cDot11StationWmmEdcaTable,
       "hh3cDot11StationWmmEdcaEntry": hh3cDot11StationWmmEdcaEntry,
       "hh3cDot11StationWmmAC": hh3cDot11StationWmmAC,
       "hh3cDot11StationWmmAifsn": hh3cDot11StationWmmAifsn,
       "hh3cDot11StationWmmEcwMin": hh3cDot11StationWmmEcwMin,
       "hh3cDot11StationWmmEcwMax": hh3cDot11StationWmmEcwMax,
       "hh3cDot11StationWmmTxoplimit": hh3cDot11StationWmmTxoplimit,
       "hh3cDot11StationWmmCacEnabled": hh3cDot11StationWmmCacEnabled,
       "hh3cDot11WmmResetGroup": hh3cDot11WmmResetGroup,
       "hh3cDot11WmmResetRadioByAP": hh3cDot11WmmResetRadioByAP,
       "hh3cDot11WmmResetStationByAP": hh3cDot11WmmResetStationByAP,
       "hh3cDot11RadioWmmEdcaCfg2Table": hh3cDot11RadioWmmEdcaCfg2Table,
       "hh3cDot11RadioWmmEdcaCfg2Entry": hh3cDot11RadioWmmEdcaCfg2Entry,
       "hh3cDot11WMMAPSerialID": hh3cDot11WMMAPSerialID,
       "hh3cDot11WMMRdId": hh3cDot11WMMRdId,
       "hh3cDot11RdWmmAC": hh3cDot11RdWmmAC,
       "hh3cDot11RdWmmAifsn": hh3cDot11RdWmmAifsn,
       "hh3cDot11RdWmmEcwMin": hh3cDot11RdWmmEcwMin,
       "hh3cDot11RdWmmEcwMax": hh3cDot11RdWmmEcwMax,
       "hh3cDot11RdWmmTxoplimit": hh3cDot11RdWmmTxoplimit}
)
