# SNMP MIB module (CISCO-DMN-DSG-SDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-SDI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:32 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGSDI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32)
)
ciscoDSGSDI.setRevisions(
        ("2012-03-20 11:00",
         "2010-08-24 07:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdiInfo_ObjectIdentity = ObjectIdentity
sdiInfo = _SdiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1)
)


class _SdiVii_Type(Integer32):
    """Custom type sdiVii based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SdiVii_Type.__name__ = "Integer32"
_SdiVii_Object = MibScalar
sdiVii = _SdiVii_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 1),
    _SdiVii_Type()
)
sdiVii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdiVii.setStatus("current")


class _VancGlobalStatusInterlaced_Type(Integer32):
    """Custom type vancGlobalStatusInterlaced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VancGlobalStatusInterlaced_Type.__name__ = "Integer32"
_VancGlobalStatusInterlaced_Object = MibScalar
vancGlobalStatusInterlaced = _VancGlobalStatusInterlaced_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 2),
    _VancGlobalStatusInterlaced_Type()
)
vancGlobalStatusInterlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusInterlaced.setStatus("current")
_VancGlobalStatusFrames_Type = Counter32
_VancGlobalStatusFrames_Object = MibScalar
vancGlobalStatusFrames = _VancGlobalStatusFrames_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 3),
    _VancGlobalStatusFrames_Type()
)
vancGlobalStatusFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusFrames.setStatus("current")
_VancGlobalStatusLines_Type = Counter32
_VancGlobalStatusLines_Object = MibScalar
vancGlobalStatusLines = _VancGlobalStatusLines_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 4),
    _VancGlobalStatusLines_Type()
)
vancGlobalStatusLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusLines.setStatus("current")
_VancGlobalStatusWords_Type = Counter32
_VancGlobalStatusWords_Object = MibScalar
vancGlobalStatusWords = _VancGlobalStatusWords_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 5),
    _VancGlobalStatusWords_Type()
)
vancGlobalStatusWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusWords.setStatus("current")
_VancGlobalStatusFirst_Type = Counter32
_VancGlobalStatusFirst_Object = MibScalar
vancGlobalStatusFirst = _VancGlobalStatusFirst_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 6),
    _VancGlobalStatusFirst_Type()
)
vancGlobalStatusFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusFirst.setStatus("current")
_VancGlobalStatusLast_Type = Counter32
_VancGlobalStatusLast_Object = MibScalar
vancGlobalStatusLast = _VancGlobalStatusLast_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 7),
    _VancGlobalStatusLast_Type()
)
vancGlobalStatusLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusLast.setStatus("current")
_VancGlobalStatusSwitch_Type = Counter32
_VancGlobalStatusSwitch_Object = MibScalar
vancGlobalStatusSwitch = _VancGlobalStatusSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 8),
    _VancGlobalStatusSwitch_Type()
)
vancGlobalStatusSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusSwitch.setStatus("current")


class _VancGlobalStatusMultiLine_Type(Integer32):
    """Custom type vancGlobalStatusMultiLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VancGlobalStatusMultiLine_Type.__name__ = "Integer32"
_VancGlobalStatusMultiLine_Object = MibScalar
vancGlobalStatusMultiLine = _VancGlobalStatusMultiLine_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 1, 9),
    _VancGlobalStatusMultiLine_Type()
)
vancGlobalStatusMultiLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancGlobalStatusMultiLine.setStatus("current")
_SdiTable_ObjectIdentity = ObjectIdentity
sdiTable = _SdiTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2)
)
_VancCfgTable_Object = MibTable
vancCfgTable = _VancCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 1)
)
if mibBuilder.loadTexts:
    vancCfgTable.setStatus("current")
_VancCfgEntry_Object = MibTableRow
vancCfgEntry = _VancCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 1, 1)
)
vancCfgEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-SDI-MIB", "vancCfgSvcID"),
)
if mibBuilder.loadTexts:
    vancCfgEntry.setStatus("current")


class _VancCfgSvcID_Type(Integer32):
    """Custom type vancCfgSvcID based on Integer32"""
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
        *(("afd", 2),
          ("dpi", 3),
          ("eia708", 1),
          ("multiOP47", 6),
          ("sdpOP47", 5),
          ("smpte2031", 4))
    )


_VancCfgSvcID_Type.__name__ = "Integer32"
_VancCfgSvcID_Object = MibTableColumn
vancCfgSvcID = _VancCfgSvcID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 1, 1, 1),
    _VancCfgSvcID_Type()
)
vancCfgSvcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancCfgSvcID.setStatus("current")


class _VancCfgEnable_Type(Integer32):
    """Custom type vancCfgEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VancCfgEnable_Type.__name__ = "Integer32"
_VancCfgEnable_Object = MibTableColumn
vancCfgEnable = _VancCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 1, 1, 2),
    _VancCfgEnable_Type()
)
vancCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vancCfgEnable.setStatus("current")


class _VancCfgOffset_Type(Integer32):
    """Custom type vancCfgOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_VancCfgOffset_Type.__name__ = "Integer32"
_VancCfgOffset_Object = MibTableColumn
vancCfgOffset = _VancCfgOffset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 1, 1, 3),
    _VancCfgOffset_Type()
)
vancCfgOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vancCfgOffset.setStatus("current")
_SdiAudioSlotTable_Object = MibTable
sdiAudioSlotTable = _SdiAudioSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 2)
)
if mibBuilder.loadTexts:
    sdiAudioSlotTable.setStatus("current")
_SdiAudioSlotEntry_Object = MibTableRow
sdiAudioSlotEntry = _SdiAudioSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 2, 1)
)
sdiAudioSlotEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-SDI-MIB", "sdiAudioSlotGroup"),
    (0, "CISCO-DMN-DSG-SDI-MIB", "sdiAudioSlotPosition"),
)
if mibBuilder.loadTexts:
    sdiAudioSlotEntry.setStatus("current")


class _SdiAudioSlotGroup_Type(Integer32):
    """Custom type sdiAudioSlotGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SdiAudioSlotGroup_Type.__name__ = "Integer32"
_SdiAudioSlotGroup_Object = MibTableColumn
sdiAudioSlotGroup = _SdiAudioSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 2, 1, 1),
    _SdiAudioSlotGroup_Type()
)
sdiAudioSlotGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdiAudioSlotGroup.setStatus("current")


class _SdiAudioSlotPosition_Type(Integer32):
    """Custom type sdiAudioSlotPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SdiAudioSlotPosition_Type.__name__ = "Integer32"
_SdiAudioSlotPosition_Object = MibTableColumn
sdiAudioSlotPosition = _SdiAudioSlotPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 2, 1, 2),
    _SdiAudioSlotPosition_Type()
)
sdiAudioSlotPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdiAudioSlotPosition.setStatus("current")


class _SdiAudioSlotAud_Type(Integer32):
    """Custom type sdiAudioSlotAud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SdiAudioSlotAud_Type.__name__ = "Integer32"
_SdiAudioSlotAud_Object = MibTableColumn
sdiAudioSlotAud = _SdiAudioSlotAud_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 2, 1, 3),
    _SdiAudioSlotAud_Type()
)
sdiAudioSlotAud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdiAudioSlotAud.setStatus("current")


class _SdiAudioSlotChan_Type(Integer32):
    """Custom type sdiAudioSlotChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SdiAudioSlotChan_Type.__name__ = "Integer32"
_SdiAudioSlotChan_Object = MibTableColumn
sdiAudioSlotChan = _SdiAudioSlotChan_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 2, 1, 4),
    _SdiAudioSlotChan_Type()
)
sdiAudioSlotChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdiAudioSlotChan.setStatus("current")
_VancServiceStatusTable_Object = MibTable
vancServiceStatusTable = _VancServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3)
)
if mibBuilder.loadTexts:
    vancServiceStatusTable.setStatus("current")
_VancServiceStatusEntry_Object = MibTableRow
vancServiceStatusEntry = _VancServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1)
)
vancServiceStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-SDI-MIB", "vancServiceStatusServiceID"),
)
if mibBuilder.loadTexts:
    vancServiceStatusEntry.setStatus("current")


class _VancServiceStatusServiceID_Type(Integer32):
    """Custom type vancServiceStatusServiceID based on Integer32"""
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
        *(("afd", 2),
          ("dpi", 3),
          ("eia708", 1),
          ("multiOP47", 6),
          ("sdpOP47", 5),
          ("smpte2031", 4))
    )


_VancServiceStatusServiceID_Type.__name__ = "Integer32"
_VancServiceStatusServiceID_Object = MibTableColumn
vancServiceStatusServiceID = _VancServiceStatusServiceID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 1),
    _VancServiceStatusServiceID_Type()
)
vancServiceStatusServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusServiceID.setStatus("current")


class _VancServiceStatusActive_Type(Integer32):
    """Custom type vancServiceStatusActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VancServiceStatusActive_Type.__name__ = "Integer32"
_VancServiceStatusActive_Object = MibTableColumn
vancServiceStatusActive = _VancServiceStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 2),
    _VancServiceStatusActive_Type()
)
vancServiceStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusActive.setStatus("current")
_VancServiceStatusADJLine_Type = Counter32
_VancServiceStatusADJLine_Object = MibTableColumn
vancServiceStatusADJLine = _VancServiceStatusADJLine_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 3),
    _VancServiceStatusADJLine_Type()
)
vancServiceStatusADJLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusADJLine.setStatus("current")
_VancServiceStatusACTLineF1_Type = Counter32
_VancServiceStatusACTLineF1_Object = MibTableColumn
vancServiceStatusACTLineF1 = _VancServiceStatusACTLineF1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 4),
    _VancServiceStatusACTLineF1_Type()
)
vancServiceStatusACTLineF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusACTLineF1.setStatus("current")
_VancServiceStatusACTLineF2_Type = Counter32
_VancServiceStatusACTLineF2_Object = MibTableColumn
vancServiceStatusACTLineF2 = _VancServiceStatusACTLineF2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 5),
    _VancServiceStatusACTLineF2_Type()
)
vancServiceStatusACTLineF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusACTLineF2.setStatus("current")
_VancServiceStatusLinesMAX_Type = Counter32
_VancServiceStatusLinesMAX_Object = MibTableColumn
vancServiceStatusLinesMAX = _VancServiceStatusLinesMAX_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 6),
    _VancServiceStatusLinesMAX_Type()
)
vancServiceStatusLinesMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusLinesMAX.setStatus("current")
_VancServiceStatusDataAvg_Type = Counter32
_VancServiceStatusDataAvg_Object = MibTableColumn
vancServiceStatusDataAvg = _VancServiceStatusDataAvg_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 7),
    _VancServiceStatusDataAvg_Type()
)
vancServiceStatusDataAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusDataAvg.setStatus("current")
_VancServiceStatusPacketsOKAvg_Type = Counter32
_VancServiceStatusPacketsOKAvg_Object = MibTableColumn
vancServiceStatusPacketsOKAvg = _VancServiceStatusPacketsOKAvg_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 8),
    _VancServiceStatusPacketsOKAvg_Type()
)
vancServiceStatusPacketsOKAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusPacketsOKAvg.setStatus("current")
_VancServiceStatusPacketsDroppedAvg_Type = Counter32
_VancServiceStatusPacketsDroppedAvg_Object = MibTableColumn
vancServiceStatusPacketsDroppedAvg = _VancServiceStatusPacketsDroppedAvg_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 32, 2, 3, 1, 9),
    _VancServiceStatusPacketsDroppedAvg_Type()
)
vancServiceStatusPacketsDroppedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vancServiceStatusPacketsDroppedAvg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-SDI-MIB",
    **{"ciscoDSGSDI": ciscoDSGSDI,
       "sdiInfo": sdiInfo,
       "sdiVii": sdiVii,
       "vancGlobalStatusInterlaced": vancGlobalStatusInterlaced,
       "vancGlobalStatusFrames": vancGlobalStatusFrames,
       "vancGlobalStatusLines": vancGlobalStatusLines,
       "vancGlobalStatusWords": vancGlobalStatusWords,
       "vancGlobalStatusFirst": vancGlobalStatusFirst,
       "vancGlobalStatusLast": vancGlobalStatusLast,
       "vancGlobalStatusSwitch": vancGlobalStatusSwitch,
       "vancGlobalStatusMultiLine": vancGlobalStatusMultiLine,
       "sdiTable": sdiTable,
       "vancCfgTable": vancCfgTable,
       "vancCfgEntry": vancCfgEntry,
       "vancCfgSvcID": vancCfgSvcID,
       "vancCfgEnable": vancCfgEnable,
       "vancCfgOffset": vancCfgOffset,
       "sdiAudioSlotTable": sdiAudioSlotTable,
       "sdiAudioSlotEntry": sdiAudioSlotEntry,
       "sdiAudioSlotGroup": sdiAudioSlotGroup,
       "sdiAudioSlotPosition": sdiAudioSlotPosition,
       "sdiAudioSlotAud": sdiAudioSlotAud,
       "sdiAudioSlotChan": sdiAudioSlotChan,
       "vancServiceStatusTable": vancServiceStatusTable,
       "vancServiceStatusEntry": vancServiceStatusEntry,
       "vancServiceStatusServiceID": vancServiceStatusServiceID,
       "vancServiceStatusActive": vancServiceStatusActive,
       "vancServiceStatusADJLine": vancServiceStatusADJLine,
       "vancServiceStatusACTLineF1": vancServiceStatusACTLineF1,
       "vancServiceStatusACTLineF2": vancServiceStatusACTLineF2,
       "vancServiceStatusLinesMAX": vancServiceStatusLinesMAX,
       "vancServiceStatusDataAvg": vancServiceStatusDataAvg,
       "vancServiceStatusPacketsOKAvg": vancServiceStatusPacketsOKAvg,
       "vancServiceStatusPacketsDroppedAvg": vancServiceStatusPacketsDroppedAvg}
)
