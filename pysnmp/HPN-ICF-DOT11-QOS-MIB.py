# SNMP MIB module (HPN-ICF-DOT11-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:52 2024
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

(HpnicfDot11ObjectIDType,
 HpnicfDot11QosAcType,
 HpnicfDot11RadioElementIndex,
 HpnicfDot11RadioScopeType,
 hpnicfDot11) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11QosAcType",
    "HpnicfDot11RadioElementIndex",
    "HpnicfDot11RadioScopeType",
    "hpnicfDot11")

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

hpnicfDot11QoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9)
)
hpnicfDot11QoS.setRevisions(
        ("2008-07-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfDot11WMMSVPMapAC(Integer32, TextualConvention):
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



class HpnicfDot11WMMCACPolicy(Integer32, TextualConvention):
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

_HpnicfDot11WmmCfgGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11WmmCfgGroup = _HpnicfDot11WmmCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1)
)
_HpnicfDot11RadioWmmCfgTable_Object = MibTable
hpnicfDot11RadioWmmCfgTable = _HpnicfDot11RadioWmmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmCfgTable.setStatus("current")
_HpnicfDot11RadioWmmCfgEntry_Object = MibTableRow
hpnicfDot11RadioWmmCfgEntry = _HpnicfDot11RadioWmmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1)
)
hpnicfDot11RadioWmmCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11WmmRadioIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmCfgEntry.setStatus("current")
_HpnicfDot11WmmRadioIndex_Type = HpnicfDot11RadioElementIndex
_HpnicfDot11WmmRadioIndex_Object = MibTableColumn
hpnicfDot11WmmRadioIndex = _HpnicfDot11WmmRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1, 1),
    _HpnicfDot11WmmRadioIndex_Type()
)
hpnicfDot11WmmRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WmmRadioIndex.setStatus("current")
_HpnicfDot11RadioWmmEnabled_Type = TruthValue
_HpnicfDot11RadioWmmEnabled_Object = MibTableColumn
hpnicfDot11RadioWmmEnabled = _HpnicfDot11RadioWmmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1, 2),
    _HpnicfDot11RadioWmmEnabled_Type()
)
hpnicfDot11RadioWmmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEnabled.setStatus("current")
_HpnicfDot11RadioSVPMapToAC_Type = HpnicfDot11WMMSVPMapAC
_HpnicfDot11RadioSVPMapToAC_Object = MibTableColumn
hpnicfDot11RadioSVPMapToAC = _HpnicfDot11RadioSVPMapToAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1, 3),
    _HpnicfDot11RadioSVPMapToAC_Type()
)
hpnicfDot11RadioSVPMapToAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioSVPMapToAC.setStatus("current")
_HpnicfDot11RadioCacPolicy_Type = HpnicfDot11WMMCACPolicy
_HpnicfDot11RadioCacPolicy_Object = MibTableColumn
hpnicfDot11RadioCacPolicy = _HpnicfDot11RadioCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1, 4),
    _HpnicfDot11RadioCacPolicy_Type()
)
hpnicfDot11RadioCacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCacPolicy.setStatus("current")


class _HpnicfDot11RadioCacChlUtlValue_Type(Integer32):
    """Custom type hpnicfDot11RadioCacChlUtlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RadioCacChlUtlValue_Type.__name__ = "Integer32"
_HpnicfDot11RadioCacChlUtlValue_Object = MibTableColumn
hpnicfDot11RadioCacChlUtlValue = _HpnicfDot11RadioCacChlUtlValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1, 5),
    _HpnicfDot11RadioCacChlUtlValue_Type()
)
hpnicfDot11RadioCacChlUtlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCacChlUtlValue.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCacChlUtlValue.setUnits("percent")


class _HpnicfDot11RadioCacUserNum_Type(Integer32):
    """Custom type hpnicfDot11RadioCacUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_HpnicfDot11RadioCacUserNum_Type.__name__ = "Integer32"
_HpnicfDot11RadioCacUserNum_Object = MibTableColumn
hpnicfDot11RadioCacUserNum = _HpnicfDot11RadioCacUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 1, 1, 6),
    _HpnicfDot11RadioCacUserNum_Type()
)
hpnicfDot11RadioCacUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCacUserNum.setStatus("current")
_HpnicfDot11RadioWmmEdcaCfgTable_Object = MibTable
hpnicfDot11RadioWmmEdcaCfgTable = _HpnicfDot11RadioWmmEdcaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEdcaCfgTable.setStatus("current")
_HpnicfDot11RadioWmmEdcaCfgEntry_Object = MibTableRow
hpnicfDot11RadioWmmEdcaCfgEntry = _HpnicfDot11RadioWmmEdcaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1)
)
hpnicfDot11RadioWmmEdcaCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11WmmRadioIndex"),
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11RadioWmmAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEdcaCfgEntry.setStatus("current")
_HpnicfDot11RadioWmmAC_Type = HpnicfDot11QosAcType
_HpnicfDot11RadioWmmAC_Object = MibTableColumn
hpnicfDot11RadioWmmAC = _HpnicfDot11RadioWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1, 1),
    _HpnicfDot11RadioWmmAC_Type()
)
hpnicfDot11RadioWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmAC.setStatus("current")


class _HpnicfDot11RadioWmmAifsn_Type(Integer32):
    """Custom type hpnicfDot11RadioWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfDot11RadioWmmAifsn_Type.__name__ = "Integer32"
_HpnicfDot11RadioWmmAifsn_Object = MibTableColumn
hpnicfDot11RadioWmmAifsn = _HpnicfDot11RadioWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1, 2),
    _HpnicfDot11RadioWmmAifsn_Type()
)
hpnicfDot11RadioWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmAifsn.setStatus("current")


class _HpnicfDot11RadioWmmEcwMin_Type(Integer32):
    """Custom type hpnicfDot11RadioWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfDot11RadioWmmEcwMin_Type.__name__ = "Integer32"
_HpnicfDot11RadioWmmEcwMin_Object = MibTableColumn
hpnicfDot11RadioWmmEcwMin = _HpnicfDot11RadioWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1, 3),
    _HpnicfDot11RadioWmmEcwMin_Type()
)
hpnicfDot11RadioWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEcwMin.setStatus("current")


class _HpnicfDot11RadioWmmEcwMax_Type(Integer32):
    """Custom type hpnicfDot11RadioWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfDot11RadioWmmEcwMax_Type.__name__ = "Integer32"
_HpnicfDot11RadioWmmEcwMax_Object = MibTableColumn
hpnicfDot11RadioWmmEcwMax = _HpnicfDot11RadioWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1, 4),
    _HpnicfDot11RadioWmmEcwMax_Type()
)
hpnicfDot11RadioWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEcwMax.setStatus("current")


class _HpnicfDot11RadioWmmTxoplimit_Type(Integer32):
    """Custom type hpnicfDot11RadioWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11RadioWmmTxoplimit_Type.__name__ = "Integer32"
_HpnicfDot11RadioWmmTxoplimit_Object = MibTableColumn
hpnicfDot11RadioWmmTxoplimit = _HpnicfDot11RadioWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1, 5),
    _HpnicfDot11RadioWmmTxoplimit_Type()
)
hpnicfDot11RadioWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmTxoplimit.setStatus("current")
_HpnicfDot11RadioWmmNoAck_Type = TruthValue
_HpnicfDot11RadioWmmNoAck_Object = MibTableColumn
hpnicfDot11RadioWmmNoAck = _HpnicfDot11RadioWmmNoAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 2, 1, 6),
    _HpnicfDot11RadioWmmNoAck_Type()
)
hpnicfDot11RadioWmmNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmNoAck.setStatus("current")
_HpnicfDot11StationWmmEdcaTable_Object = MibTable
hpnicfDot11StationWmmEdcaTable = _HpnicfDot11StationWmmEdcaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmEdcaTable.setStatus("current")
_HpnicfDot11StationWmmEdcaEntry_Object = MibTableRow
hpnicfDot11StationWmmEdcaEntry = _HpnicfDot11StationWmmEdcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1)
)
hpnicfDot11StationWmmEdcaEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11WmmRadioIndex"),
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11StationWmmAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmEdcaEntry.setStatus("current")
_HpnicfDot11StationWmmAC_Type = HpnicfDot11QosAcType
_HpnicfDot11StationWmmAC_Object = MibTableColumn
hpnicfDot11StationWmmAC = _HpnicfDot11StationWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1, 1),
    _HpnicfDot11StationWmmAC_Type()
)
hpnicfDot11StationWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmAC.setStatus("current")


class _HpnicfDot11StationWmmAifsn_Type(Integer32):
    """Custom type hpnicfDot11StationWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_HpnicfDot11StationWmmAifsn_Type.__name__ = "Integer32"
_HpnicfDot11StationWmmAifsn_Object = MibTableColumn
hpnicfDot11StationWmmAifsn = _HpnicfDot11StationWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1, 2),
    _HpnicfDot11StationWmmAifsn_Type()
)
hpnicfDot11StationWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmAifsn.setStatus("current")


class _HpnicfDot11StationWmmEcwMin_Type(Integer32):
    """Custom type hpnicfDot11StationWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfDot11StationWmmEcwMin_Type.__name__ = "Integer32"
_HpnicfDot11StationWmmEcwMin_Object = MibTableColumn
hpnicfDot11StationWmmEcwMin = _HpnicfDot11StationWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1, 3),
    _HpnicfDot11StationWmmEcwMin_Type()
)
hpnicfDot11StationWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmEcwMin.setStatus("current")


class _HpnicfDot11StationWmmEcwMax_Type(Integer32):
    """Custom type hpnicfDot11StationWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfDot11StationWmmEcwMax_Type.__name__ = "Integer32"
_HpnicfDot11StationWmmEcwMax_Object = MibTableColumn
hpnicfDot11StationWmmEcwMax = _HpnicfDot11StationWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1, 4),
    _HpnicfDot11StationWmmEcwMax_Type()
)
hpnicfDot11StationWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmEcwMax.setStatus("current")


class _HpnicfDot11StationWmmTxoplimit_Type(Integer32):
    """Custom type hpnicfDot11StationWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11StationWmmTxoplimit_Type.__name__ = "Integer32"
_HpnicfDot11StationWmmTxoplimit_Object = MibTableColumn
hpnicfDot11StationWmmTxoplimit = _HpnicfDot11StationWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1, 5),
    _HpnicfDot11StationWmmTxoplimit_Type()
)
hpnicfDot11StationWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmTxoplimit.setStatus("current")
_HpnicfDot11StationWmmCacEnabled_Type = TruthValue
_HpnicfDot11StationWmmCacEnabled_Object = MibTableColumn
hpnicfDot11StationWmmCacEnabled = _HpnicfDot11StationWmmCacEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 3, 1, 6),
    _HpnicfDot11StationWmmCacEnabled_Type()
)
hpnicfDot11StationWmmCacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmCacEnabled.setStatus("current")
_HpnicfDot11WmmResetGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11WmmResetGroup = _HpnicfDot11WmmResetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 4)
)
_HpnicfDot11WmmResetRadioByAP_Type = Integer32
_HpnicfDot11WmmResetRadioByAP_Object = MibScalar
hpnicfDot11WmmResetRadioByAP = _HpnicfDot11WmmResetRadioByAP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 4, 1),
    _HpnicfDot11WmmResetRadioByAP_Type()
)
hpnicfDot11WmmResetRadioByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WmmResetRadioByAP.setStatus("current")
_HpnicfDot11WmmResetStationByAP_Type = Integer32
_HpnicfDot11WmmResetStationByAP_Object = MibScalar
hpnicfDot11WmmResetStationByAP = _HpnicfDot11WmmResetStationByAP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 4, 2),
    _HpnicfDot11WmmResetStationByAP_Type()
)
hpnicfDot11WmmResetStationByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WmmResetStationByAP.setStatus("current")
_HpnicfDot11RadioWmmEdcaCfg2Table_Object = MibTable
hpnicfDot11RadioWmmEdcaCfg2Table = _HpnicfDot11RadioWmmEdcaCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEdcaCfg2Table.setStatus("current")
_HpnicfDot11RadioWmmEdcaCfg2Entry_Object = MibTableRow
hpnicfDot11RadioWmmEdcaCfg2Entry = _HpnicfDot11RadioWmmEdcaCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1)
)
hpnicfDot11RadioWmmEdcaCfg2Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11WMMAPSerialID"),
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11WMMRdId"),
    (0, "HPN-ICF-DOT11-QOS-MIB", "hpnicfDot11RdWmmAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWmmEdcaCfg2Entry.setStatus("current")
_HpnicfDot11WMMAPSerialID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11WMMAPSerialID_Object = MibTableColumn
hpnicfDot11WMMAPSerialID = _HpnicfDot11WMMAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 1),
    _HpnicfDot11WMMAPSerialID_Type()
)
hpnicfDot11WMMAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WMMAPSerialID.setStatus("current")
_HpnicfDot11WMMRdId_Type = HpnicfDot11RadioScopeType
_HpnicfDot11WMMRdId_Object = MibTableColumn
hpnicfDot11WMMRdId = _HpnicfDot11WMMRdId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 2),
    _HpnicfDot11WMMRdId_Type()
)
hpnicfDot11WMMRdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WMMRdId.setStatus("current")
_HpnicfDot11RdWmmAC_Type = HpnicfDot11QosAcType
_HpnicfDot11RdWmmAC_Object = MibTableColumn
hpnicfDot11RdWmmAC = _HpnicfDot11RdWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 3),
    _HpnicfDot11RdWmmAC_Type()
)
hpnicfDot11RdWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RdWmmAC.setStatus("current")


class _HpnicfDot11RdWmmAifsn_Type(Integer32):
    """Custom type hpnicfDot11RdWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfDot11RdWmmAifsn_Type.__name__ = "Integer32"
_HpnicfDot11RdWmmAifsn_Object = MibTableColumn
hpnicfDot11RdWmmAifsn = _HpnicfDot11RdWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 4),
    _HpnicfDot11RdWmmAifsn_Type()
)
hpnicfDot11RdWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RdWmmAifsn.setStatus("current")


class _HpnicfDot11RdWmmEcwMin_Type(Integer32):
    """Custom type hpnicfDot11RdWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfDot11RdWmmEcwMin_Type.__name__ = "Integer32"
_HpnicfDot11RdWmmEcwMin_Object = MibTableColumn
hpnicfDot11RdWmmEcwMin = _HpnicfDot11RdWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 5),
    _HpnicfDot11RdWmmEcwMin_Type()
)
hpnicfDot11RdWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RdWmmEcwMin.setStatus("current")


class _HpnicfDot11RdWmmEcwMax_Type(Integer32):
    """Custom type hpnicfDot11RdWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfDot11RdWmmEcwMax_Type.__name__ = "Integer32"
_HpnicfDot11RdWmmEcwMax_Object = MibTableColumn
hpnicfDot11RdWmmEcwMax = _HpnicfDot11RdWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 6),
    _HpnicfDot11RdWmmEcwMax_Type()
)
hpnicfDot11RdWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RdWmmEcwMax.setStatus("current")


class _HpnicfDot11RdWmmTxoplimit_Type(Integer32):
    """Custom type hpnicfDot11RdWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11RdWmmTxoplimit_Type.__name__ = "Integer32"
_HpnicfDot11RdWmmTxoplimit_Object = MibTableColumn
hpnicfDot11RdWmmTxoplimit = _HpnicfDot11RdWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 9, 1, 5, 1, 7),
    _HpnicfDot11RdWmmTxoplimit_Type()
)
hpnicfDot11RdWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RdWmmTxoplimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-QOS-MIB",
    **{"HpnicfDot11WMMSVPMapAC": HpnicfDot11WMMSVPMapAC,
       "HpnicfDot11WMMCACPolicy": HpnicfDot11WMMCACPolicy,
       "hpnicfDot11QoS": hpnicfDot11QoS,
       "hpnicfDot11WmmCfgGroup": hpnicfDot11WmmCfgGroup,
       "hpnicfDot11RadioWmmCfgTable": hpnicfDot11RadioWmmCfgTable,
       "hpnicfDot11RadioWmmCfgEntry": hpnicfDot11RadioWmmCfgEntry,
       "hpnicfDot11WmmRadioIndex": hpnicfDot11WmmRadioIndex,
       "hpnicfDot11RadioWmmEnabled": hpnicfDot11RadioWmmEnabled,
       "hpnicfDot11RadioSVPMapToAC": hpnicfDot11RadioSVPMapToAC,
       "hpnicfDot11RadioCacPolicy": hpnicfDot11RadioCacPolicy,
       "hpnicfDot11RadioCacChlUtlValue": hpnicfDot11RadioCacChlUtlValue,
       "hpnicfDot11RadioCacUserNum": hpnicfDot11RadioCacUserNum,
       "hpnicfDot11RadioWmmEdcaCfgTable": hpnicfDot11RadioWmmEdcaCfgTable,
       "hpnicfDot11RadioWmmEdcaCfgEntry": hpnicfDot11RadioWmmEdcaCfgEntry,
       "hpnicfDot11RadioWmmAC": hpnicfDot11RadioWmmAC,
       "hpnicfDot11RadioWmmAifsn": hpnicfDot11RadioWmmAifsn,
       "hpnicfDot11RadioWmmEcwMin": hpnicfDot11RadioWmmEcwMin,
       "hpnicfDot11RadioWmmEcwMax": hpnicfDot11RadioWmmEcwMax,
       "hpnicfDot11RadioWmmTxoplimit": hpnicfDot11RadioWmmTxoplimit,
       "hpnicfDot11RadioWmmNoAck": hpnicfDot11RadioWmmNoAck,
       "hpnicfDot11StationWmmEdcaTable": hpnicfDot11StationWmmEdcaTable,
       "hpnicfDot11StationWmmEdcaEntry": hpnicfDot11StationWmmEdcaEntry,
       "hpnicfDot11StationWmmAC": hpnicfDot11StationWmmAC,
       "hpnicfDot11StationWmmAifsn": hpnicfDot11StationWmmAifsn,
       "hpnicfDot11StationWmmEcwMin": hpnicfDot11StationWmmEcwMin,
       "hpnicfDot11StationWmmEcwMax": hpnicfDot11StationWmmEcwMax,
       "hpnicfDot11StationWmmTxoplimit": hpnicfDot11StationWmmTxoplimit,
       "hpnicfDot11StationWmmCacEnabled": hpnicfDot11StationWmmCacEnabled,
       "hpnicfDot11WmmResetGroup": hpnicfDot11WmmResetGroup,
       "hpnicfDot11WmmResetRadioByAP": hpnicfDot11WmmResetRadioByAP,
       "hpnicfDot11WmmResetStationByAP": hpnicfDot11WmmResetStationByAP,
       "hpnicfDot11RadioWmmEdcaCfg2Table": hpnicfDot11RadioWmmEdcaCfg2Table,
       "hpnicfDot11RadioWmmEdcaCfg2Entry": hpnicfDot11RadioWmmEdcaCfg2Entry,
       "hpnicfDot11WMMAPSerialID": hpnicfDot11WMMAPSerialID,
       "hpnicfDot11WMMRdId": hpnicfDot11WMMRdId,
       "hpnicfDot11RdWmmAC": hpnicfDot11RdWmmAC,
       "hpnicfDot11RdWmmAifsn": hpnicfDot11RdWmmAifsn,
       "hpnicfDot11RdWmmEcwMin": hpnicfDot11RdWmmEcwMin,
       "hpnicfDot11RdWmmEcwMax": hpnicfDot11RdWmmEcwMax,
       "hpnicfDot11RdWmmTxoplimit": hpnicfDot11RdWmmTxoplimit}
)
