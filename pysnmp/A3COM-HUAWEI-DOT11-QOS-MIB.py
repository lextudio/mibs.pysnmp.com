# SNMP MIB module (A3COM-HUAWEI-DOT11-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:39 2024
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

(H3cDot11ObjectIDType,
 H3cDot11QosAcType,
 H3cDot11RadioElementIndex,
 H3cDot11RadioScopeType,
 h3cDot11) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    "H3cDot11ObjectIDType",
    "H3cDot11QosAcType",
    "H3cDot11RadioElementIndex",
    "H3cDot11RadioScopeType",
    "h3cDot11")

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

h3cDot11QoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9)
)
h3cDot11QoS.setRevisions(
        ("2008-07-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cDot11WMMSVPMapAC(Integer32, TextualConvention):
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



class H3cDot11WMMCACPolicy(Integer32, TextualConvention):
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

_H3cDot11WmmCfgGroup_ObjectIdentity = ObjectIdentity
h3cDot11WmmCfgGroup = _H3cDot11WmmCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1)
)
_H3cDot11RadioWmmCfgTable_Object = MibTable
h3cDot11RadioWmmCfgTable = _H3cDot11RadioWmmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11RadioWmmCfgTable.setStatus("current")
_H3cDot11RadioWmmCfgEntry_Object = MibTableRow
h3cDot11RadioWmmCfgEntry = _H3cDot11RadioWmmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1)
)
h3cDot11RadioWmmCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11WmmRadioIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioWmmCfgEntry.setStatus("current")
_H3cDot11WmmRadioIndex_Type = H3cDot11RadioElementIndex
_H3cDot11WmmRadioIndex_Object = MibTableColumn
h3cDot11WmmRadioIndex = _H3cDot11WmmRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1, 1),
    _H3cDot11WmmRadioIndex_Type()
)
h3cDot11WmmRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WmmRadioIndex.setStatus("current")
_H3cDot11RadioWmmEnabled_Type = TruthValue
_H3cDot11RadioWmmEnabled_Object = MibTableColumn
h3cDot11RadioWmmEnabled = _H3cDot11RadioWmmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1, 2),
    _H3cDot11RadioWmmEnabled_Type()
)
h3cDot11RadioWmmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEnabled.setStatus("current")
_H3cDot11RadioSVPMapToAC_Type = H3cDot11WMMSVPMapAC
_H3cDot11RadioSVPMapToAC_Object = MibTableColumn
h3cDot11RadioSVPMapToAC = _H3cDot11RadioSVPMapToAC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1, 3),
    _H3cDot11RadioSVPMapToAC_Type()
)
h3cDot11RadioSVPMapToAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioSVPMapToAC.setStatus("current")
_H3cDot11RadioCacPolicy_Type = H3cDot11WMMCACPolicy
_H3cDot11RadioCacPolicy_Object = MibTableColumn
h3cDot11RadioCacPolicy = _H3cDot11RadioCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1, 4),
    _H3cDot11RadioCacPolicy_Type()
)
h3cDot11RadioCacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCacPolicy.setStatus("current")


class _H3cDot11RadioCacChlUtlValue_Type(Integer32):
    """Custom type h3cDot11RadioCacChlUtlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RadioCacChlUtlValue_Type.__name__ = "Integer32"
_H3cDot11RadioCacChlUtlValue_Object = MibTableColumn
h3cDot11RadioCacChlUtlValue = _H3cDot11RadioCacChlUtlValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1, 5),
    _H3cDot11RadioCacChlUtlValue_Type()
)
h3cDot11RadioCacChlUtlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCacChlUtlValue.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RadioCacChlUtlValue.setUnits("percent")


class _H3cDot11RadioCacUserNum_Type(Integer32):
    """Custom type h3cDot11RadioCacUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_H3cDot11RadioCacUserNum_Type.__name__ = "Integer32"
_H3cDot11RadioCacUserNum_Object = MibTableColumn
h3cDot11RadioCacUserNum = _H3cDot11RadioCacUserNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 1, 1, 6),
    _H3cDot11RadioCacUserNum_Type()
)
h3cDot11RadioCacUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCacUserNum.setStatus("current")
_H3cDot11RadioWmmEdcaCfgTable_Object = MibTable
h3cDot11RadioWmmEdcaCfgTable = _H3cDot11RadioWmmEdcaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEdcaCfgTable.setStatus("current")
_H3cDot11RadioWmmEdcaCfgEntry_Object = MibTableRow
h3cDot11RadioWmmEdcaCfgEntry = _H3cDot11RadioWmmEdcaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1)
)
h3cDot11RadioWmmEdcaCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11WmmRadioIndex"),
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11RadioWmmAC"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEdcaCfgEntry.setStatus("current")
_H3cDot11RadioWmmAC_Type = H3cDot11QosAcType
_H3cDot11RadioWmmAC_Object = MibTableColumn
h3cDot11RadioWmmAC = _H3cDot11RadioWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1, 1),
    _H3cDot11RadioWmmAC_Type()
)
h3cDot11RadioWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmAC.setStatus("current")


class _H3cDot11RadioWmmAifsn_Type(Integer32):
    """Custom type h3cDot11RadioWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_H3cDot11RadioWmmAifsn_Type.__name__ = "Integer32"
_H3cDot11RadioWmmAifsn_Object = MibTableColumn
h3cDot11RadioWmmAifsn = _H3cDot11RadioWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1, 2),
    _H3cDot11RadioWmmAifsn_Type()
)
h3cDot11RadioWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmAifsn.setStatus("current")


class _H3cDot11RadioWmmEcwMin_Type(Integer32):
    """Custom type h3cDot11RadioWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cDot11RadioWmmEcwMin_Type.__name__ = "Integer32"
_H3cDot11RadioWmmEcwMin_Object = MibTableColumn
h3cDot11RadioWmmEcwMin = _H3cDot11RadioWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1, 3),
    _H3cDot11RadioWmmEcwMin_Type()
)
h3cDot11RadioWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEcwMin.setStatus("current")


class _H3cDot11RadioWmmEcwMax_Type(Integer32):
    """Custom type h3cDot11RadioWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cDot11RadioWmmEcwMax_Type.__name__ = "Integer32"
_H3cDot11RadioWmmEcwMax_Object = MibTableColumn
h3cDot11RadioWmmEcwMax = _H3cDot11RadioWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1, 4),
    _H3cDot11RadioWmmEcwMax_Type()
)
h3cDot11RadioWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEcwMax.setStatus("current")


class _H3cDot11RadioWmmTxoplimit_Type(Integer32):
    """Custom type h3cDot11RadioWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11RadioWmmTxoplimit_Type.__name__ = "Integer32"
_H3cDot11RadioWmmTxoplimit_Object = MibTableColumn
h3cDot11RadioWmmTxoplimit = _H3cDot11RadioWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1, 5),
    _H3cDot11RadioWmmTxoplimit_Type()
)
h3cDot11RadioWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmTxoplimit.setStatus("current")
_H3cDot11RadioWmmNoAck_Type = TruthValue
_H3cDot11RadioWmmNoAck_Object = MibTableColumn
h3cDot11RadioWmmNoAck = _H3cDot11RadioWmmNoAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 2, 1, 6),
    _H3cDot11RadioWmmNoAck_Type()
)
h3cDot11RadioWmmNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWmmNoAck.setStatus("current")
_H3cDot11StationWmmEdcaTable_Object = MibTable
h3cDot11StationWmmEdcaTable = _H3cDot11StationWmmEdcaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot11StationWmmEdcaTable.setStatus("current")
_H3cDot11StationWmmEdcaEntry_Object = MibTableRow
h3cDot11StationWmmEdcaEntry = _H3cDot11StationWmmEdcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1)
)
h3cDot11StationWmmEdcaEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11WmmRadioIndex"),
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11StationWmmAC"),
)
if mibBuilder.loadTexts:
    h3cDot11StationWmmEdcaEntry.setStatus("current")
_H3cDot11StationWmmAC_Type = H3cDot11QosAcType
_H3cDot11StationWmmAC_Object = MibTableColumn
h3cDot11StationWmmAC = _H3cDot11StationWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1, 1),
    _H3cDot11StationWmmAC_Type()
)
h3cDot11StationWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11StationWmmAC.setStatus("current")


class _H3cDot11StationWmmAifsn_Type(Integer32):
    """Custom type h3cDot11StationWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_H3cDot11StationWmmAifsn_Type.__name__ = "Integer32"
_H3cDot11StationWmmAifsn_Object = MibTableColumn
h3cDot11StationWmmAifsn = _H3cDot11StationWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1, 2),
    _H3cDot11StationWmmAifsn_Type()
)
h3cDot11StationWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StationWmmAifsn.setStatus("current")


class _H3cDot11StationWmmEcwMin_Type(Integer32):
    """Custom type h3cDot11StationWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cDot11StationWmmEcwMin_Type.__name__ = "Integer32"
_H3cDot11StationWmmEcwMin_Object = MibTableColumn
h3cDot11StationWmmEcwMin = _H3cDot11StationWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1, 3),
    _H3cDot11StationWmmEcwMin_Type()
)
h3cDot11StationWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StationWmmEcwMin.setStatus("current")


class _H3cDot11StationWmmEcwMax_Type(Integer32):
    """Custom type h3cDot11StationWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cDot11StationWmmEcwMax_Type.__name__ = "Integer32"
_H3cDot11StationWmmEcwMax_Object = MibTableColumn
h3cDot11StationWmmEcwMax = _H3cDot11StationWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1, 4),
    _H3cDot11StationWmmEcwMax_Type()
)
h3cDot11StationWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StationWmmEcwMax.setStatus("current")


class _H3cDot11StationWmmTxoplimit_Type(Integer32):
    """Custom type h3cDot11StationWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11StationWmmTxoplimit_Type.__name__ = "Integer32"
_H3cDot11StationWmmTxoplimit_Object = MibTableColumn
h3cDot11StationWmmTxoplimit = _H3cDot11StationWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1, 5),
    _H3cDot11StationWmmTxoplimit_Type()
)
h3cDot11StationWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StationWmmTxoplimit.setStatus("current")
_H3cDot11StationWmmCacEnabled_Type = TruthValue
_H3cDot11StationWmmCacEnabled_Object = MibTableColumn
h3cDot11StationWmmCacEnabled = _H3cDot11StationWmmCacEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 3, 1, 6),
    _H3cDot11StationWmmCacEnabled_Type()
)
h3cDot11StationWmmCacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StationWmmCacEnabled.setStatus("current")
_H3cDot11WmmResetGroup_ObjectIdentity = ObjectIdentity
h3cDot11WmmResetGroup = _H3cDot11WmmResetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 4)
)
_H3cDot11WmmResetRadioByAP_Type = Integer32
_H3cDot11WmmResetRadioByAP_Object = MibScalar
h3cDot11WmmResetRadioByAP = _H3cDot11WmmResetRadioByAP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 4, 1),
    _H3cDot11WmmResetRadioByAP_Type()
)
h3cDot11WmmResetRadioByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WmmResetRadioByAP.setStatus("current")
_H3cDot11WmmResetStationByAP_Type = Integer32
_H3cDot11WmmResetStationByAP_Object = MibScalar
h3cDot11WmmResetStationByAP = _H3cDot11WmmResetStationByAP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 4, 2),
    _H3cDot11WmmResetStationByAP_Type()
)
h3cDot11WmmResetStationByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WmmResetStationByAP.setStatus("current")
_H3cDot11RadioWmmEdcaCfg2Table_Object = MibTable
h3cDot11RadioWmmEdcaCfg2Table = _H3cDot11RadioWmmEdcaCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEdcaCfg2Table.setStatus("current")
_H3cDot11RadioWmmEdcaCfg2Entry_Object = MibTableRow
h3cDot11RadioWmmEdcaCfg2Entry = _H3cDot11RadioWmmEdcaCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1)
)
h3cDot11RadioWmmEdcaCfg2Entry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11WMMAPSerialID"),
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11WMMRdId"),
    (0, "A3COM-HUAWEI-DOT11-QOS-MIB", "h3cDot11RdWmmAC"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioWmmEdcaCfg2Entry.setStatus("current")
_H3cDot11WMMAPSerialID_Type = H3cDot11ObjectIDType
_H3cDot11WMMAPSerialID_Object = MibTableColumn
h3cDot11WMMAPSerialID = _H3cDot11WMMAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 1),
    _H3cDot11WMMAPSerialID_Type()
)
h3cDot11WMMAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WMMAPSerialID.setStatus("current")
_H3cDot11WMMRdId_Type = H3cDot11RadioScopeType
_H3cDot11WMMRdId_Object = MibTableColumn
h3cDot11WMMRdId = _H3cDot11WMMRdId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 2),
    _H3cDot11WMMRdId_Type()
)
h3cDot11WMMRdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WMMRdId.setStatus("current")
_H3cDot11RdWmmAC_Type = H3cDot11QosAcType
_H3cDot11RdWmmAC_Object = MibTableColumn
h3cDot11RdWmmAC = _H3cDot11RdWmmAC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 3),
    _H3cDot11RdWmmAC_Type()
)
h3cDot11RdWmmAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RdWmmAC.setStatus("current")


class _H3cDot11RdWmmAifsn_Type(Integer32):
    """Custom type h3cDot11RdWmmAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_H3cDot11RdWmmAifsn_Type.__name__ = "Integer32"
_H3cDot11RdWmmAifsn_Object = MibTableColumn
h3cDot11RdWmmAifsn = _H3cDot11RdWmmAifsn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 4),
    _H3cDot11RdWmmAifsn_Type()
)
h3cDot11RdWmmAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RdWmmAifsn.setStatus("current")


class _H3cDot11RdWmmEcwMin_Type(Integer32):
    """Custom type h3cDot11RdWmmEcwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cDot11RdWmmEcwMin_Type.__name__ = "Integer32"
_H3cDot11RdWmmEcwMin_Object = MibTableColumn
h3cDot11RdWmmEcwMin = _H3cDot11RdWmmEcwMin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 5),
    _H3cDot11RdWmmEcwMin_Type()
)
h3cDot11RdWmmEcwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RdWmmEcwMin.setStatus("current")


class _H3cDot11RdWmmEcwMax_Type(Integer32):
    """Custom type h3cDot11RdWmmEcwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cDot11RdWmmEcwMax_Type.__name__ = "Integer32"
_H3cDot11RdWmmEcwMax_Object = MibTableColumn
h3cDot11RdWmmEcwMax = _H3cDot11RdWmmEcwMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 6),
    _H3cDot11RdWmmEcwMax_Type()
)
h3cDot11RdWmmEcwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RdWmmEcwMax.setStatus("current")


class _H3cDot11RdWmmTxoplimit_Type(Integer32):
    """Custom type h3cDot11RdWmmTxoplimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11RdWmmTxoplimit_Type.__name__ = "Integer32"
_H3cDot11RdWmmTxoplimit_Object = MibTableColumn
h3cDot11RdWmmTxoplimit = _H3cDot11RdWmmTxoplimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 9, 1, 5, 1, 7),
    _H3cDot11RdWmmTxoplimit_Type()
)
h3cDot11RdWmmTxoplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RdWmmTxoplimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-QOS-MIB",
    **{"H3cDot11WMMSVPMapAC": H3cDot11WMMSVPMapAC,
       "H3cDot11WMMCACPolicy": H3cDot11WMMCACPolicy,
       "h3cDot11QoS": h3cDot11QoS,
       "h3cDot11WmmCfgGroup": h3cDot11WmmCfgGroup,
       "h3cDot11RadioWmmCfgTable": h3cDot11RadioWmmCfgTable,
       "h3cDot11RadioWmmCfgEntry": h3cDot11RadioWmmCfgEntry,
       "h3cDot11WmmRadioIndex": h3cDot11WmmRadioIndex,
       "h3cDot11RadioWmmEnabled": h3cDot11RadioWmmEnabled,
       "h3cDot11RadioSVPMapToAC": h3cDot11RadioSVPMapToAC,
       "h3cDot11RadioCacPolicy": h3cDot11RadioCacPolicy,
       "h3cDot11RadioCacChlUtlValue": h3cDot11RadioCacChlUtlValue,
       "h3cDot11RadioCacUserNum": h3cDot11RadioCacUserNum,
       "h3cDot11RadioWmmEdcaCfgTable": h3cDot11RadioWmmEdcaCfgTable,
       "h3cDot11RadioWmmEdcaCfgEntry": h3cDot11RadioWmmEdcaCfgEntry,
       "h3cDot11RadioWmmAC": h3cDot11RadioWmmAC,
       "h3cDot11RadioWmmAifsn": h3cDot11RadioWmmAifsn,
       "h3cDot11RadioWmmEcwMin": h3cDot11RadioWmmEcwMin,
       "h3cDot11RadioWmmEcwMax": h3cDot11RadioWmmEcwMax,
       "h3cDot11RadioWmmTxoplimit": h3cDot11RadioWmmTxoplimit,
       "h3cDot11RadioWmmNoAck": h3cDot11RadioWmmNoAck,
       "h3cDot11StationWmmEdcaTable": h3cDot11StationWmmEdcaTable,
       "h3cDot11StationWmmEdcaEntry": h3cDot11StationWmmEdcaEntry,
       "h3cDot11StationWmmAC": h3cDot11StationWmmAC,
       "h3cDot11StationWmmAifsn": h3cDot11StationWmmAifsn,
       "h3cDot11StationWmmEcwMin": h3cDot11StationWmmEcwMin,
       "h3cDot11StationWmmEcwMax": h3cDot11StationWmmEcwMax,
       "h3cDot11StationWmmTxoplimit": h3cDot11StationWmmTxoplimit,
       "h3cDot11StationWmmCacEnabled": h3cDot11StationWmmCacEnabled,
       "h3cDot11WmmResetGroup": h3cDot11WmmResetGroup,
       "h3cDot11WmmResetRadioByAP": h3cDot11WmmResetRadioByAP,
       "h3cDot11WmmResetStationByAP": h3cDot11WmmResetStationByAP,
       "h3cDot11RadioWmmEdcaCfg2Table": h3cDot11RadioWmmEdcaCfg2Table,
       "h3cDot11RadioWmmEdcaCfg2Entry": h3cDot11RadioWmmEdcaCfg2Entry,
       "h3cDot11WMMAPSerialID": h3cDot11WMMAPSerialID,
       "h3cDot11WMMRdId": h3cDot11WMMRdId,
       "h3cDot11RdWmmAC": h3cDot11RdWmmAC,
       "h3cDot11RdWmmAifsn": h3cDot11RdWmmAifsn,
       "h3cDot11RdWmmEcwMin": h3cDot11RdWmmEcwMin,
       "h3cDot11RdWmmEcwMax": h3cDot11RdWmmEcwMax,
       "h3cDot11RdWmmTxoplimit": h3cDot11RdWmmTxoplimit}
)
