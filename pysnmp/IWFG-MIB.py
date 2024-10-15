# SNMP MIB module (IWFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IWFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:29 2024
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_IwfGWY_ObjectIdentity = ObjectIdentity
iwfGWY = _IwfGWY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25)
)
_IwfCfgFrRly_ObjectIdentity = ObjectIdentity
iwfCfgFrRly = _IwfCfgFrRly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1)
)
_IwfCfgFrRlyTable_Object = MibTable
iwfCfgFrRlyTable = _IwfCfgFrRlyTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1, 1)
)
if mibBuilder.loadTexts:
    iwfCfgFrRlyTable.setStatus("mandatory")
_IwfCfgFrRlyEntry_Object = MibTableRow
iwfCfgFrRlyEntry = _IwfCfgFrRlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1, 1, 1)
)
iwfCfgFrRlyEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgFrRlyIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgFrRlyEntry.setStatus("mandatory")
_IwfCfgFrRlyIndex_Type = Integer32
_IwfCfgFrRlyIndex_Object = MibTableColumn
iwfCfgFrRlyIndex = _IwfCfgFrRlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1, 1, 1, 1),
    _IwfCfgFrRlyIndex_Type()
)
iwfCfgFrRlyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgFrRlyIndex.setStatus("mandatory")
_IwfCfgFrRlyT391StatusEnqryTimr_Type = Integer32
_IwfCfgFrRlyT391StatusEnqryTimr_Object = MibTableColumn
iwfCfgFrRlyT391StatusEnqryTimr = _IwfCfgFrRlyT391StatusEnqryTimr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1, 1, 1, 2),
    _IwfCfgFrRlyT391StatusEnqryTimr_Type()
)
iwfCfgFrRlyT391StatusEnqryTimr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgFrRlyT391StatusEnqryTimr.setStatus("mandatory")
_IwfCfgFrRlyT392StatusTimer_Type = Integer32
_IwfCfgFrRlyT392StatusTimer_Object = MibTableColumn
iwfCfgFrRlyT392StatusTimer = _IwfCfgFrRlyT392StatusTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1, 1, 1, 3),
    _IwfCfgFrRlyT392StatusTimer_Type()
)
iwfCfgFrRlyT392StatusTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgFrRlyT392StatusTimer.setStatus("mandatory")
_IwfCfgFrRlyN391StatusEnqrySent_Type = Integer32
_IwfCfgFrRlyN391StatusEnqrySent_Object = MibTableColumn
iwfCfgFrRlyN391StatusEnqrySent = _IwfCfgFrRlyN391StatusEnqrySent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 1, 1, 1, 4),
    _IwfCfgFrRlyN391StatusEnqrySent_Type()
)
iwfCfgFrRlyN391StatusEnqrySent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgFrRlyN391StatusEnqrySent.setStatus("mandatory")
_IwfCfgQ921_ObjectIdentity = ObjectIdentity
iwfCfgQ921 = _IwfCfgQ921_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2)
)
_IwfCfgQ921Table_Object = MibTable
iwfCfgQ921Table = _IwfCfgQ921Table_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1)
)
if mibBuilder.loadTexts:
    iwfCfgQ921Table.setStatus("mandatory")
_IwfCfgQ921Entry_Object = MibTableRow
iwfCfgQ921Entry = _IwfCfgQ921Entry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1)
)
iwfCfgQ921Entry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgQ921Index"),
)
if mibBuilder.loadTexts:
    iwfCfgQ921Entry.setStatus("mandatory")
_IwfCfgQ921Index_Type = Integer32
_IwfCfgQ921Index_Object = MibTableColumn
iwfCfgQ921Index = _IwfCfgQ921Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 1),
    _IwfCfgQ921Index_Type()
)
iwfCfgQ921Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgQ921Index.setStatus("mandatory")
_IwfCfgQ921KmaxOutStandPkt_Type = Integer32
_IwfCfgQ921KmaxOutStandPkt_Object = MibTableColumn
iwfCfgQ921KmaxOutStandPkt = _IwfCfgQ921KmaxOutStandPkt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 2),
    _IwfCfgQ921KmaxOutStandPkt_Type()
)
iwfCfgQ921KmaxOutStandPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ921KmaxOutStandPkt.setStatus("mandatory")
_IwfCfgQ921T200IframeAckTimer_Type = Integer32
_IwfCfgQ921T200IframeAckTimer_Object = MibTableColumn
iwfCfgQ921T200IframeAckTimer = _IwfCfgQ921T200IframeAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 3),
    _IwfCfgQ921T200IframeAckTimer_Type()
)
iwfCfgQ921T200IframeAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ921T200IframeAckTimer.setStatus("mandatory")
_IwfCfgQ921T203MaxTimeNoIframe_Type = Integer32
_IwfCfgQ921T203MaxTimeNoIframe_Object = MibTableColumn
iwfCfgQ921T203MaxTimeNoIframe = _IwfCfgQ921T203MaxTimeNoIframe_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 4),
    _IwfCfgQ921T203MaxTimeNoIframe_Type()
)
iwfCfgQ921T203MaxTimeNoIframe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ921T203MaxTimeNoIframe.setStatus("mandatory")
_IwfCfgQ921N200MaxFrameRetrans_Type = Integer32
_IwfCfgQ921N200MaxFrameRetrans_Object = MibTableColumn
iwfCfgQ921N200MaxFrameRetrans = _IwfCfgQ921N200MaxFrameRetrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 5),
    _IwfCfgQ921N200MaxFrameRetrans_Type()
)
iwfCfgQ921N200MaxFrameRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ921N200MaxFrameRetrans.setStatus("mandatory")
_IwfCfgQ921N201RxMaxOctetInfo_Type = Integer32
_IwfCfgQ921N201RxMaxOctetInfo_Object = MibTableColumn
iwfCfgQ921N201RxMaxOctetInfo = _IwfCfgQ921N201RxMaxOctetInfo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 6),
    _IwfCfgQ921N201RxMaxOctetInfo_Type()
)
iwfCfgQ921N201RxMaxOctetInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ921N201RxMaxOctetInfo.setStatus("mandatory")
_IwfCfgQ921N201TxMaxOctetInfo_Type = Integer32
_IwfCfgQ921N201TxMaxOctetInfo_Object = MibTableColumn
iwfCfgQ921N201TxMaxOctetInfo = _IwfCfgQ921N201TxMaxOctetInfo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 2, 1, 1, 7),
    _IwfCfgQ921N201TxMaxOctetInfo_Type()
)
iwfCfgQ921N201TxMaxOctetInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ921N201TxMaxOctetInfo.setStatus("mandatory")
_IwfCfgQ933_ObjectIdentity = ObjectIdentity
iwfCfgQ933 = _IwfCfgQ933_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3)
)
_IwfCfgQ933Table_Object = MibTable
iwfCfgQ933Table = _IwfCfgQ933Table_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1)
)
if mibBuilder.loadTexts:
    iwfCfgQ933Table.setStatus("mandatory")
_IwfCfgQ933Entry_Object = MibTableRow
iwfCfgQ933Entry = _IwfCfgQ933Entry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1)
)
iwfCfgQ933Entry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgQ933Index"),
)
if mibBuilder.loadTexts:
    iwfCfgQ933Entry.setStatus("mandatory")
_IwfCfgQ933Index_Type = Integer32
_IwfCfgQ933Index_Object = MibTableColumn
iwfCfgQ933Index = _IwfCfgQ933Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 1),
    _IwfCfgQ933Index_Type()
)
iwfCfgQ933Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgQ933Index.setStatus("mandatory")
_IwfCfgQ933T303SetupTimer_Type = Integer32
_IwfCfgQ933T303SetupTimer_Object = MibTableColumn
iwfCfgQ933T303SetupTimer = _IwfCfgQ933T303SetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 2),
    _IwfCfgQ933T303SetupTimer_Type()
)
iwfCfgQ933T303SetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ933T303SetupTimer.setStatus("mandatory")
_IwfCfgQ933T305DisconnectTimer_Type = Integer32
_IwfCfgQ933T305DisconnectTimer_Object = MibTableColumn
iwfCfgQ933T305DisconnectTimer = _IwfCfgQ933T305DisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 3),
    _IwfCfgQ933T305DisconnectTimer_Type()
)
iwfCfgQ933T305DisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ933T305DisconnectTimer.setStatus("mandatory")
_IwfCfgQ933T308ReleaseTimer_Type = Integer32
_IwfCfgQ933T308ReleaseTimer_Object = MibTableColumn
iwfCfgQ933T308ReleaseTimer = _IwfCfgQ933T308ReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 4),
    _IwfCfgQ933T308ReleaseTimer_Type()
)
iwfCfgQ933T308ReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ933T308ReleaseTimer.setStatus("mandatory")
_IwfCfgQ933T309DataLinkDiscTimr_Type = Integer32
_IwfCfgQ933T309DataLinkDiscTimr_Object = MibTableColumn
iwfCfgQ933T309DataLinkDiscTimr = _IwfCfgQ933T309DataLinkDiscTimr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 5),
    _IwfCfgQ933T309DataLinkDiscTimr_Type()
)
iwfCfgQ933T309DataLinkDiscTimr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ933T309DataLinkDiscTimr.setStatus("mandatory")
_IwfCfgQ933T310CallProceedTimer_Type = Integer32
_IwfCfgQ933T310CallProceedTimer_Object = MibTableColumn
iwfCfgQ933T310CallProceedTimer = _IwfCfgQ933T310CallProceedTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 6),
    _IwfCfgQ933T310CallProceedTimer_Type()
)
iwfCfgQ933T310CallProceedTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ933T310CallProceedTimer.setStatus("mandatory")
_IwfCfgQ933T313ConnectSentTimer_Type = Integer32
_IwfCfgQ933T313ConnectSentTimer_Object = MibTableColumn
iwfCfgQ933T313ConnectSentTimer = _IwfCfgQ933T313ConnectSentTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 3, 1, 1, 7),
    _IwfCfgQ933T313ConnectSentTimer_Type()
)
iwfCfgQ933T313ConnectSentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQ933T313ConnectSentTimer.setStatus("mandatory")
_IwfCfgCallStats_ObjectIdentity = ObjectIdentity
iwfCfgCallStats = _IwfCfgCallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4)
)
_IwfCfgCallStatsTable_Object = MibTable
iwfCfgCallStatsTable = _IwfCfgCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1)
)
if mibBuilder.loadTexts:
    iwfCfgCallStatsTable.setStatus("mandatory")
_IwfCfgCallStatsEntry_Object = MibTableRow
iwfCfgCallStatsEntry = _IwfCfgCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1)
)
iwfCfgCallStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgCsIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgCallStatsEntry.setStatus("mandatory")
_IwfCfgCsIndex_Type = Integer32
_IwfCfgCsIndex_Object = MibTableColumn
iwfCfgCsIndex = _IwfCfgCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 1),
    _IwfCfgCsIndex_Type()
)
iwfCfgCsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgCsIndex.setStatus("mandatory")


class _IwfCfgCsMobOrigAdStats_Type(Integer32):
    """Custom type iwfCfgCsMobOrigAdStats based on Integer32"""
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


_IwfCfgCsMobOrigAdStats_Type.__name__ = "Integer32"
_IwfCfgCsMobOrigAdStats_Object = MibTableColumn
iwfCfgCsMobOrigAdStats = _IwfCfgCsMobOrigAdStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 2),
    _IwfCfgCsMobOrigAdStats_Type()
)
iwfCfgCsMobOrigAdStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgCsMobOrigAdStats.setStatus("mandatory")


class _IwfCfgCsMobOrigFaxStats_Type(Integer32):
    """Custom type iwfCfgCsMobOrigFaxStats based on Integer32"""
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


_IwfCfgCsMobOrigFaxStats_Type.__name__ = "Integer32"
_IwfCfgCsMobOrigFaxStats_Object = MibTableColumn
iwfCfgCsMobOrigFaxStats = _IwfCfgCsMobOrigFaxStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 3),
    _IwfCfgCsMobOrigFaxStats_Type()
)
iwfCfgCsMobOrigFaxStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgCsMobOrigFaxStats.setStatus("mandatory")


class _IwfCfgCsMobTermAdStats_Type(Integer32):
    """Custom type iwfCfgCsMobTermAdStats based on Integer32"""
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


_IwfCfgCsMobTermAdStats_Type.__name__ = "Integer32"
_IwfCfgCsMobTermAdStats_Object = MibTableColumn
iwfCfgCsMobTermAdStats = _IwfCfgCsMobTermAdStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 4),
    _IwfCfgCsMobTermAdStats_Type()
)
iwfCfgCsMobTermAdStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgCsMobTermAdStats.setStatus("mandatory")


class _IwfCfgCsMobTermFaxStats_Type(Integer32):
    """Custom type iwfCfgCsMobTermFaxStats based on Integer32"""
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


_IwfCfgCsMobTermFaxStats_Type.__name__ = "Integer32"
_IwfCfgCsMobTermFaxStats_Object = MibTableColumn
iwfCfgCsMobTermFaxStats = _IwfCfgCsMobTermFaxStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 5),
    _IwfCfgCsMobTermFaxStats_Type()
)
iwfCfgCsMobTermFaxStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgCsMobTermFaxStats.setStatus("mandatory")


class _IwfCfgCsLogStartTrapEna_Type(Integer32):
    """Custom type iwfCfgCsLogStartTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLogs", 3),
          ("enableTraps", 1))
    )


_IwfCfgCsLogStartTrapEna_Type.__name__ = "Integer32"
_IwfCfgCsLogStartTrapEna_Object = MibTableColumn
iwfCfgCsLogStartTrapEna = _IwfCfgCsLogStartTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 6),
    _IwfCfgCsLogStartTrapEna_Type()
)
iwfCfgCsLogStartTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgCsLogStartTrapEna.setStatus("mandatory")


class _IwfCfgCsLogTermTrapEna_Type(Integer32):
    """Custom type iwfCfgCsLogTermTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLogs", 3),
          ("enableTraps", 1))
    )


_IwfCfgCsLogTermTrapEna_Type.__name__ = "Integer32"
_IwfCfgCsLogTermTrapEna_Object = MibTableColumn
iwfCfgCsLogTermTrapEna = _IwfCfgCsLogTermTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 4, 1, 1, 7),
    _IwfCfgCsLogTermTrapEna_Type()
)
iwfCfgCsLogTermTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgCsLogTermTrapEna.setStatus("mandatory")
_IwfCfgPppParam_ObjectIdentity = ObjectIdentity
iwfCfgPppParam = _IwfCfgPppParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5)
)
_IwfCfgPppParamTable_Object = MibTable
iwfCfgPppParamTable = _IwfCfgPppParamTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1)
)
if mibBuilder.loadTexts:
    iwfCfgPppParamTable.setStatus("mandatory")
_IwfCfgPppParamEntry_Object = MibTableRow
iwfCfgPppParamEntry = _IwfCfgPppParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1)
)
iwfCfgPppParamEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgPppIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgPppParamEntry.setStatus("mandatory")
_IwfCfgPppIndex_Type = Integer32
_IwfCfgPppIndex_Object = MibTableColumn
iwfCfgPppIndex = _IwfCfgPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 1),
    _IwfCfgPppIndex_Type()
)
iwfCfgPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgPppIndex.setStatus("mandatory")
_IwfCfgPppForceEncryptData_Type = Integer32
_IwfCfgPppForceEncryptData_Object = MibTableColumn
iwfCfgPppForceEncryptData = _IwfCfgPppForceEncryptData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 2),
    _IwfCfgPppForceEncryptData_Type()
)
iwfCfgPppForceEncryptData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppForceEncryptData.setStatus("mandatory")
_IwfCfgPppForceEncryptpassword_Type = Integer32
_IwfCfgPppForceEncryptpassword_Object = MibTableColumn
iwfCfgPppForceEncryptpassword = _IwfCfgPppForceEncryptpassword_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 3),
    _IwfCfgPppForceEncryptpassword_Type()
)
iwfCfgPppForceEncryptpassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppForceEncryptpassword.setStatus("mandatory")
_IwfCfgPppMaxNumbConfigRequests_Type = Integer32
_IwfCfgPppMaxNumbConfigRequests_Object = MibTableColumn
iwfCfgPppMaxNumbConfigRequests = _IwfCfgPppMaxNumbConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 4),
    _IwfCfgPppMaxNumbConfigRequests_Type()
)
iwfCfgPppMaxNumbConfigRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppMaxNumbConfigRequests.setStatus("mandatory")
_IwfCfgPppMaxNumbConfigNAK_Type = Integer32
_IwfCfgPppMaxNumbConfigNAK_Object = MibTableColumn
iwfCfgPppMaxNumbConfigNAK = _IwfCfgPppMaxNumbConfigNAK_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 5),
    _IwfCfgPppMaxNumbConfigNAK_Type()
)
iwfCfgPppMaxNumbConfigNAK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppMaxNumbConfigNAK.setStatus("mandatory")
_IwfCfgPppMaxNumbRejects_Type = Integer32
_IwfCfgPppMaxNumbRejects_Object = MibTableColumn
iwfCfgPppMaxNumbRejects = _IwfCfgPppMaxNumbRejects_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 6),
    _IwfCfgPppMaxNumbRejects_Type()
)
iwfCfgPppMaxNumbRejects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppMaxNumbRejects.setStatus("mandatory")
_IwfCfgPppMaxNumbTermRequests_Type = Integer32
_IwfCfgPppMaxNumbTermRequests_Object = MibTableColumn
iwfCfgPppMaxNumbTermRequests = _IwfCfgPppMaxNumbTermRequests_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 7),
    _IwfCfgPppMaxNumbTermRequests_Type()
)
iwfCfgPppMaxNumbTermRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppMaxNumbTermRequests.setStatus("mandatory")
_IwfCfgPppNegotiateTime_Type = Integer32
_IwfCfgPppNegotiateTime_Object = MibTableColumn
iwfCfgPppNegotiateTime = _IwfCfgPppNegotiateTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 8),
    _IwfCfgPppNegotiateTime_Type()
)
iwfCfgPppNegotiateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppNegotiateTime.setStatus("mandatory")
_IwfCfgPppRestartTime_Type = Integer32
_IwfCfgPppRestartTime_Object = MibTableColumn
iwfCfgPppRestartTime = _IwfCfgPppRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 9),
    _IwfCfgPppRestartTime_Type()
)
iwfCfgPppRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppRestartTime.setStatus("mandatory")
_IwfCfgPppIpAddressPoolMax_Type = IpAddress
_IwfCfgPppIpAddressPoolMax_Object = MibTableColumn
iwfCfgPppIpAddressPoolMax = _IwfCfgPppIpAddressPoolMax_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 10),
    _IwfCfgPppIpAddressPoolMax_Type()
)
iwfCfgPppIpAddressPoolMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppIpAddressPoolMax.setStatus("mandatory")
_IwfCfgPppIpAddressPoolMin_Type = IpAddress
_IwfCfgPppIpAddressPoolMin_Object = MibTableColumn
iwfCfgPppIpAddressPoolMin = _IwfCfgPppIpAddressPoolMin_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 5, 1, 1, 11),
    _IwfCfgPppIpAddressPoolMin_Type()
)
iwfCfgPppIpAddressPoolMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgPppIpAddressPoolMin.setStatus("mandatory")
_IwfCfgTcpIp_ObjectIdentity = ObjectIdentity
iwfCfgTcpIp = _IwfCfgTcpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6)
)
_IwfCfgTcpIpTable_Object = MibTable
iwfCfgTcpIpTable = _IwfCfgTcpIpTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1)
)
if mibBuilder.loadTexts:
    iwfCfgTcpIpTable.setStatus("mandatory")
_IwfCfgTcpIpEntry_Object = MibTableRow
iwfCfgTcpIpEntry = _IwfCfgTcpIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1)
)
iwfCfgTcpIpEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgTiIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgTcpIpEntry.setStatus("mandatory")
_IwfCfgTiIndex_Type = Integer32
_IwfCfgTiIndex_Object = MibTableColumn
iwfCfgTiIndex = _IwfCfgTiIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 1),
    _IwfCfgTiIndex_Type()
)
iwfCfgTiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgTiIndex.setStatus("mandatory")


class _IwfCfgTiDefaultServiceType_Type(Integer32):
    """Custom type iwfCfgTiDefaultServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IwfCfgTiDefaultServiceType_Type.__name__ = "Integer32"
_IwfCfgTiDefaultServiceType_Object = MibTableColumn
iwfCfgTiDefaultServiceType = _IwfCfgTiDefaultServiceType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 2),
    _IwfCfgTiDefaultServiceType_Type()
)
iwfCfgTiDefaultServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiDefaultServiceType.setStatus("mandatory")


class _IwfCfgTiDefaultTimeToLive_Type(Integer32):
    """Custom type iwfCfgTiDefaultTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IwfCfgTiDefaultTimeToLive_Type.__name__ = "Integer32"
_IwfCfgTiDefaultTimeToLive_Object = MibTableColumn
iwfCfgTiDefaultTimeToLive = _IwfCfgTiDefaultTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 3),
    _IwfCfgTiDefaultTimeToLive_Type()
)
iwfCfgTiDefaultTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiDefaultTimeToLive.setStatus("mandatory")
_IwfCfgTiMtuDiscovery_Type = Integer32
_IwfCfgTiMtuDiscovery_Object = MibTableColumn
iwfCfgTiMtuDiscovery = _IwfCfgTiMtuDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 4),
    _IwfCfgTiMtuDiscovery_Type()
)
iwfCfgTiMtuDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiMtuDiscovery.setStatus("mandatory")
_IwfCfgTiKeepAliveInterval_Type = Integer32
_IwfCfgTiKeepAliveInterval_Object = MibTableColumn
iwfCfgTiKeepAliveInterval = _IwfCfgTiKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 5),
    _IwfCfgTiKeepAliveInterval_Type()
)
iwfCfgTiKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiKeepAliveInterval.setStatus("mandatory")
_IwfCfgTiKeepAliveTime_Type = Integer32
_IwfCfgTiKeepAliveTime_Object = MibTableColumn
iwfCfgTiKeepAliveTime = _IwfCfgTiKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 6),
    _IwfCfgTiKeepAliveTime_Type()
)
iwfCfgTiKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiKeepAliveTime.setStatus("mandatory")
_IwfCfgTiMaxMtuSize_Type = Integer32
_IwfCfgTiMaxMtuSize_Object = MibTableColumn
iwfCfgTiMaxMtuSize = _IwfCfgTiMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 7),
    _IwfCfgTiMaxMtuSize_Type()
)
iwfCfgTiMaxMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiMaxMtuSize.setStatus("mandatory")
_IwfCfgTiMaxConnectReTrans_Type = Integer32
_IwfCfgTiMaxConnectReTrans_Object = MibTableColumn
iwfCfgTiMaxConnectReTrans = _IwfCfgTiMaxConnectReTrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 8),
    _IwfCfgTiMaxConnectReTrans_Type()
)
iwfCfgTiMaxConnectReTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiMaxConnectReTrans.setStatus("mandatory")
_IwfCfgTiMaxDataRetrans_Type = Integer32
_IwfCfgTiMaxDataRetrans_Object = MibTableColumn
iwfCfgTiMaxDataRetrans = _IwfCfgTiMaxDataRetrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 9),
    _IwfCfgTiMaxDataRetrans_Type()
)
iwfCfgTiMaxDataRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiMaxDataRetrans.setStatus("mandatory")
_IwfCfgTiMaxNumberConnections_Type = Integer32
_IwfCfgTiMaxNumberConnections_Object = MibTableColumn
iwfCfgTiMaxNumberConnections = _IwfCfgTiMaxNumberConnections_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 10),
    _IwfCfgTiMaxNumberConnections_Type()
)
iwfCfgTiMaxNumberConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiMaxNumberConnections.setStatus("mandatory")
_IwfCfgTiWindowSize_Type = Integer32
_IwfCfgTiWindowSize_Object = MibTableColumn
iwfCfgTiWindowSize = _IwfCfgTiWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 11),
    _IwfCfgTiWindowSize_Type()
)
iwfCfgTiWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiWindowSize.setStatus("mandatory")
_IwfCfgTiLocalIpAddress_Type = IpAddress
_IwfCfgTiLocalIpAddress_Object = MibTableColumn
iwfCfgTiLocalIpAddress = _IwfCfgTiLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 12),
    _IwfCfgTiLocalIpAddress_Type()
)
iwfCfgTiLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiLocalIpAddress.setStatus("mandatory")
_IwfCfgTiSubnetIpMask_Type = IpAddress
_IwfCfgTiSubnetIpMask_Object = MibTableColumn
iwfCfgTiSubnetIpMask = _IwfCfgTiSubnetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 13),
    _IwfCfgTiSubnetIpMask_Type()
)
iwfCfgTiSubnetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiSubnetIpMask.setStatus("mandatory")
_IwfCfgTiDefualtGatewayIp_Type = IpAddress
_IwfCfgTiDefualtGatewayIp_Object = MibTableColumn
iwfCfgTiDefualtGatewayIp = _IwfCfgTiDefualtGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 6, 1, 1, 14),
    _IwfCfgTiDefualtGatewayIp_Type()
)
iwfCfgTiDefualtGatewayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgTiDefualtGatewayIp.setStatus("mandatory")
_IwfEthernetNicStat_ObjectIdentity = ObjectIdentity
iwfEthernetNicStat = _IwfEthernetNicStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7)
)
_IwfEthernetNicStatTable_Object = MibTable
iwfEthernetNicStatTable = _IwfEthernetNicStatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1)
)
if mibBuilder.loadTexts:
    iwfEthernetNicStatTable.setStatus("mandatory")
_IwfEthernetNicStatEntry_Object = MibTableRow
iwfEthernetNicStatEntry = _IwfEthernetNicStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1)
)
iwfEthernetNicStatEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfEnsIndex"),
)
if mibBuilder.loadTexts:
    iwfEthernetNicStatEntry.setStatus("mandatory")
_IwfEnsIndex_Type = Integer32
_IwfEnsIndex_Object = MibTableColumn
iwfEnsIndex = _IwfEnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 1),
    _IwfEnsIndex_Type()
)
iwfEnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsIndex.setStatus("mandatory")
_IwfEnsPacketsRxPerSec_Type = Counter32
_IwfEnsPacketsRxPerSec_Object = MibTableColumn
iwfEnsPacketsRxPerSec = _IwfEnsPacketsRxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 2),
    _IwfEnsPacketsRxPerSec_Type()
)
iwfEnsPacketsRxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsPacketsRxPerSec.setStatus("mandatory")
_IwfEnsPacketsTxPerSec_Type = Counter32
_IwfEnsPacketsTxPerSec_Object = MibTableColumn
iwfEnsPacketsTxPerSec = _IwfEnsPacketsTxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 3),
    _IwfEnsPacketsTxPerSec_Type()
)
iwfEnsPacketsTxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsPacketsTxPerSec.setStatus("mandatory")
_IwfEnsBytesRxPerSec_Type = Counter32
_IwfEnsBytesRxPerSec_Object = MibTableColumn
iwfEnsBytesRxPerSec = _IwfEnsBytesRxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 4),
    _IwfEnsBytesRxPerSec_Type()
)
iwfEnsBytesRxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsBytesRxPerSec.setStatus("mandatory")
_IwfEnsBytesTxPerSec_Type = Counter32
_IwfEnsBytesTxPerSec_Object = MibTableColumn
iwfEnsBytesTxPerSec = _IwfEnsBytesTxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 5),
    _IwfEnsBytesTxPerSec_Type()
)
iwfEnsBytesTxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsBytesTxPerSec.setStatus("mandatory")
_IwfEnsPacketsRxErrors_Type = Counter32
_IwfEnsPacketsRxErrors_Object = MibTableColumn
iwfEnsPacketsRxErrors = _IwfEnsPacketsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 6),
    _IwfEnsPacketsRxErrors_Type()
)
iwfEnsPacketsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsPacketsRxErrors.setStatus("mandatory")
_IwfEnsPacketsRxUnknown_Type = Counter32
_IwfEnsPacketsRxUnknown_Object = MibTableColumn
iwfEnsPacketsRxUnknown = _IwfEnsPacketsRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 7),
    _IwfEnsPacketsRxUnknown_Type()
)
iwfEnsPacketsRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsPacketsRxUnknown.setStatus("mandatory")
_IwfEnsPacketsOutBoundDiscarded_Type = Counter32
_IwfEnsPacketsOutBoundDiscarded_Object = MibTableColumn
iwfEnsPacketsOutBoundDiscarded = _IwfEnsPacketsOutBoundDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 8),
    _IwfEnsPacketsOutBoundDiscarded_Type()
)
iwfEnsPacketsOutBoundDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsPacketsOutBoundDiscarded.setStatus("mandatory")
_IwfEnsPacketsOutBoundErrors_Type = Counter32
_IwfEnsPacketsOutBoundErrors_Object = MibTableColumn
iwfEnsPacketsOutBoundErrors = _IwfEnsPacketsOutBoundErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 9),
    _IwfEnsPacketsOutBoundErrors_Type()
)
iwfEnsPacketsOutBoundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsPacketsOutBoundErrors.setStatus("mandatory")
_IwfEnsOutputQueueLength_Type = Counter32
_IwfEnsOutputQueueLength_Object = MibTableColumn
iwfEnsOutputQueueLength = _IwfEnsOutputQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 7, 1, 1, 10),
    _IwfEnsOutputQueueLength_Type()
)
iwfEnsOutputQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfEnsOutputQueueLength.setStatus("mandatory")
_IwfIpStats_ObjectIdentity = ObjectIdentity
iwfIpStats = _IwfIpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8)
)
_IwfIpStatsTable_Object = MibTable
iwfIpStatsTable = _IwfIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1)
)
if mibBuilder.loadTexts:
    iwfIpStatsTable.setStatus("mandatory")
_IwfIpStatsEntry_Object = MibTableRow
iwfIpStatsEntry = _IwfIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1)
)
iwfIpStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfIsIndex"),
)
if mibBuilder.loadTexts:
    iwfIpStatsEntry.setStatus("mandatory")
_IwfIsIndex_Type = Integer32
_IwfIsIndex_Object = MibTableColumn
iwfIsIndex = _IwfIsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 1),
    _IwfIsIndex_Type()
)
iwfIsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsIndex.setStatus("mandatory")
_IwfIsPacketsRx_Type = Counter32
_IwfIsPacketsRx_Object = MibTableColumn
iwfIsPacketsRx = _IwfIsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 2),
    _IwfIsPacketsRx_Type()
)
iwfIsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsPacketsRx.setStatus("mandatory")
_IwfIsRxHeaderErrors_Type = Counter32
_IwfIsRxHeaderErrors_Object = MibTableColumn
iwfIsRxHeaderErrors = _IwfIsRxHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 3),
    _IwfIsRxHeaderErrors_Type()
)
iwfIsRxHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsRxHeaderErrors.setStatus("mandatory")
_IwfIsIpReceived_Type = Counter32
_IwfIsIpReceived_Object = MibTableColumn
iwfIsIpReceived = _IwfIsIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 4),
    _IwfIsIpReceived_Type()
)
iwfIsIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsIpReceived.setStatus("mandatory")
_IwfIsDatagramsForwarded_Type = Counter32
_IwfIsDatagramsForwarded_Object = MibTableColumn
iwfIsDatagramsForwarded = _IwfIsDatagramsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 5),
    _IwfIsDatagramsForwarded_Type()
)
iwfIsDatagramsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsDatagramsForwarded.setStatus("mandatory")
_IwfIsUnknownProtocolRx_Type = Counter32
_IwfIsUnknownProtocolRx_Object = MibTableColumn
iwfIsUnknownProtocolRx = _IwfIsUnknownProtocolRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 6),
    _IwfIsUnknownProtocolRx_Type()
)
iwfIsUnknownProtocolRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsUnknownProtocolRx.setStatus("mandatory")
_IwfIsRxPacketsDiscarded_Type = Counter32
_IwfIsRxPacketsDiscarded_Object = MibTableColumn
iwfIsRxPacketsDiscarded = _IwfIsRxPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 7),
    _IwfIsRxPacketsDiscarded_Type()
)
iwfIsRxPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsRxPacketsDiscarded.setStatus("mandatory")
_IwfIsRxPacketsDelivered_Type = Counter32
_IwfIsRxPacketsDelivered_Object = MibTableColumn
iwfIsRxPacketsDelivered = _IwfIsRxPacketsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 8),
    _IwfIsRxPacketsDelivered_Type()
)
iwfIsRxPacketsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsRxPacketsDelivered.setStatus("mandatory")
_IwfIsOutputRequests_Type = Counter32
_IwfIsOutputRequests_Object = MibTableColumn
iwfIsOutputRequests = _IwfIsOutputRequests_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 9),
    _IwfIsOutputRequests_Type()
)
iwfIsOutputRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsOutputRequests.setStatus("mandatory")
_IwfIsRoutingDiscarded_Type = Counter32
_IwfIsRoutingDiscarded_Object = MibTableColumn
iwfIsRoutingDiscarded = _IwfIsRoutingDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 10),
    _IwfIsRoutingDiscarded_Type()
)
iwfIsRoutingDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsRoutingDiscarded.setStatus("mandatory")
_IwfIsDiscardedOutputPackets_Type = Counter32
_IwfIsDiscardedOutputPackets_Object = MibTableColumn
iwfIsDiscardedOutputPackets = _IwfIsDiscardedOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 11),
    _IwfIsDiscardedOutputPackets_Type()
)
iwfIsDiscardedOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsDiscardedOutputPackets.setStatus("mandatory")
_IwfIsOutputPacketsNoRoute_Type = Counter32
_IwfIsOutputPacketsNoRoute_Object = MibTableColumn
iwfIsOutputPacketsNoRoute = _IwfIsOutputPacketsNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 12),
    _IwfIsOutputPacketsNoRoute_Type()
)
iwfIsOutputPacketsNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsOutputPacketsNoRoute.setStatus("mandatory")
_IwfIsReAssemblyRequired_Type = Counter32
_IwfIsReAssemblyRequired_Object = MibTableColumn
iwfIsReAssemblyRequired = _IwfIsReAssemblyRequired_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 13),
    _IwfIsReAssemblyRequired_Type()
)
iwfIsReAssemblyRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsReAssemblyRequired.setStatus("mandatory")
_IwfIsReAssemblySuccessful_Type = Counter32
_IwfIsReAssemblySuccessful_Object = MibTableColumn
iwfIsReAssemblySuccessful = _IwfIsReAssemblySuccessful_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 14),
    _IwfIsReAssemblySuccessful_Type()
)
iwfIsReAssemblySuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsReAssemblySuccessful.setStatus("mandatory")
_IwfIsReAssmeblyFailures_Type = Counter32
_IwfIsReAssmeblyFailures_Object = MibTableColumn
iwfIsReAssmeblyFailures = _IwfIsReAssmeblyFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 15),
    _IwfIsReAssmeblyFailures_Type()
)
iwfIsReAssmeblyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsReAssmeblyFailures.setStatus("mandatory")
_IwfIsDatagramsSuccessFragment_Type = Counter32
_IwfIsDatagramsSuccessFragment_Object = MibTableColumn
iwfIsDatagramsSuccessFragment = _IwfIsDatagramsSuccessFragment_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 16),
    _IwfIsDatagramsSuccessFragment_Type()
)
iwfIsDatagramsSuccessFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsDatagramsSuccessFragment.setStatus("mandatory")
_IwfIsDatagramsFailFragment_Type = Counter32
_IwfIsDatagramsFailFragment_Object = MibTableColumn
iwfIsDatagramsFailFragment = _IwfIsDatagramsFailFragment_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 17),
    _IwfIsDatagramsFailFragment_Type()
)
iwfIsDatagramsFailFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsDatagramsFailFragment.setStatus("mandatory")
_IwfIsFragmentCreated_Type = Counter32
_IwfIsFragmentCreated_Object = MibTableColumn
iwfIsFragmentCreated = _IwfIsFragmentCreated_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 8, 1, 1, 18),
    _IwfIsFragmentCreated_Type()
)
iwfIsFragmentCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIsFragmentCreated.setStatus("mandatory")
_IwfIcmpStats_ObjectIdentity = ObjectIdentity
iwfIcmpStats = _IwfIcmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9)
)
_IwfIcmpStatsTable_Object = MibTable
iwfIcmpStatsTable = _IwfIcmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1)
)
if mibBuilder.loadTexts:
    iwfIcmpStatsTable.setStatus("mandatory")
_IwfIcmpStatsEntry_Object = MibTableRow
iwfIcmpStatsEntry = _IwfIcmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1)
)
iwfIcmpStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfIcmpStIndex"),
)
if mibBuilder.loadTexts:
    iwfIcmpStatsEntry.setStatus("mandatory")
_IwfIcmpStIndex_Type = Integer32
_IwfIcmpStIndex_Object = MibTableColumn
iwfIcmpStIndex = _IwfIcmpStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 1),
    _IwfIcmpStIndex_Type()
)
iwfIcmpStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStIndex.setStatus("mandatory")
_IwfIcmpStMessagesRx_Type = Counter32
_IwfIcmpStMessagesRx_Object = MibTableColumn
iwfIcmpStMessagesRx = _IwfIcmpStMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 2),
    _IwfIcmpStMessagesRx_Type()
)
iwfIcmpStMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStMessagesRx.setStatus("mandatory")
_IwfIcmpStMessagesTx_Type = Counter32
_IwfIcmpStMessagesTx_Object = MibTableColumn
iwfIcmpStMessagesTx = _IwfIcmpStMessagesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 3),
    _IwfIcmpStMessagesTx_Type()
)
iwfIcmpStMessagesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStMessagesTx.setStatus("mandatory")
_IwfIcmpStErrorsRx_Type = Counter32
_IwfIcmpStErrorsRx_Object = MibTableColumn
iwfIcmpStErrorsRx = _IwfIcmpStErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 4),
    _IwfIcmpStErrorsRx_Type()
)
iwfIcmpStErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStErrorsRx.setStatus("mandatory")
_IwfIcmpStErrorsTx_Type = Counter32
_IwfIcmpStErrorsTx_Object = MibTableColumn
iwfIcmpStErrorsTx = _IwfIcmpStErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 5),
    _IwfIcmpStErrorsTx_Type()
)
iwfIcmpStErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStErrorsTx.setStatus("mandatory")
_IwfIcmpStDestUnreachableTx_Type = Counter32
_IwfIcmpStDestUnreachableTx_Object = MibTableColumn
iwfIcmpStDestUnreachableTx = _IwfIcmpStDestUnreachableTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 6),
    _IwfIcmpStDestUnreachableTx_Type()
)
iwfIcmpStDestUnreachableTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStDestUnreachableTx.setStatus("mandatory")
_IwfIcmpStDestUnreachableRx_Type = Counter32
_IwfIcmpStDestUnreachableRx_Object = MibTableColumn
iwfIcmpStDestUnreachableRx = _IwfIcmpStDestUnreachableRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 7),
    _IwfIcmpStDestUnreachableRx_Type()
)
iwfIcmpStDestUnreachableRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStDestUnreachableRx.setStatus("mandatory")
_IwfIcmpStTimeExceededTx_Type = Counter32
_IwfIcmpStTimeExceededTx_Object = MibTableColumn
iwfIcmpStTimeExceededTx = _IwfIcmpStTimeExceededTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 8),
    _IwfIcmpStTimeExceededTx_Type()
)
iwfIcmpStTimeExceededTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStTimeExceededTx.setStatus("mandatory")
_IwfIcmpStTimeExceededRx_Type = Counter32
_IwfIcmpStTimeExceededRx_Object = MibTableColumn
iwfIcmpStTimeExceededRx = _IwfIcmpStTimeExceededRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 9),
    _IwfIcmpStTimeExceededRx_Type()
)
iwfIcmpStTimeExceededRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStTimeExceededRx.setStatus("mandatory")
_IwfIcmpStParameterProblemsTx_Type = Counter32
_IwfIcmpStParameterProblemsTx_Object = MibTableColumn
iwfIcmpStParameterProblemsTx = _IwfIcmpStParameterProblemsTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 10),
    _IwfIcmpStParameterProblemsTx_Type()
)
iwfIcmpStParameterProblemsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStParameterProblemsTx.setStatus("mandatory")
_IwfIcmpStParameterProblemsRx_Type = Counter32
_IwfIcmpStParameterProblemsRx_Object = MibTableColumn
iwfIcmpStParameterProblemsRx = _IwfIcmpStParameterProblemsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 11),
    _IwfIcmpStParameterProblemsRx_Type()
)
iwfIcmpStParameterProblemsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStParameterProblemsRx.setStatus("mandatory")
_IwfIcmpStSourceQuenchsTx_Type = Counter32
_IwfIcmpStSourceQuenchsTx_Object = MibTableColumn
iwfIcmpStSourceQuenchsTx = _IwfIcmpStSourceQuenchsTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 12),
    _IwfIcmpStSourceQuenchsTx_Type()
)
iwfIcmpStSourceQuenchsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStSourceQuenchsTx.setStatus("mandatory")
_IwfIcmpStSourceQuenchsRx_Type = Counter32
_IwfIcmpStSourceQuenchsRx_Object = MibTableColumn
iwfIcmpStSourceQuenchsRx = _IwfIcmpStSourceQuenchsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 13),
    _IwfIcmpStSourceQuenchsRx_Type()
)
iwfIcmpStSourceQuenchsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStSourceQuenchsRx.setStatus("mandatory")
_IwfIcmpStRedirectsTx_Type = Counter32
_IwfIcmpStRedirectsTx_Object = MibTableColumn
iwfIcmpStRedirectsTx = _IwfIcmpStRedirectsTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 14),
    _IwfIcmpStRedirectsTx_Type()
)
iwfIcmpStRedirectsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStRedirectsTx.setStatus("mandatory")
_IwfIcmpStRedirectsRx_Type = Counter32
_IwfIcmpStRedirectsRx_Object = MibTableColumn
iwfIcmpStRedirectsRx = _IwfIcmpStRedirectsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 15),
    _IwfIcmpStRedirectsRx_Type()
)
iwfIcmpStRedirectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStRedirectsRx.setStatus("mandatory")
_IwfIcmpStEchosTx_Type = Counter32
_IwfIcmpStEchosTx_Object = MibTableColumn
iwfIcmpStEchosTx = _IwfIcmpStEchosTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 16),
    _IwfIcmpStEchosTx_Type()
)
iwfIcmpStEchosTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStEchosTx.setStatus("mandatory")
_IwfIcmpStEchosRx_Type = Counter32
_IwfIcmpStEchosRx_Object = MibTableColumn
iwfIcmpStEchosRx = _IwfIcmpStEchosRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 17),
    _IwfIcmpStEchosRx_Type()
)
iwfIcmpStEchosRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStEchosRx.setStatus("mandatory")
_IwfIcmpStEchosRepliesTx_Type = Counter32
_IwfIcmpStEchosRepliesTx_Object = MibTableColumn
iwfIcmpStEchosRepliesTx = _IwfIcmpStEchosRepliesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 18),
    _IwfIcmpStEchosRepliesTx_Type()
)
iwfIcmpStEchosRepliesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStEchosRepliesTx.setStatus("mandatory")
_IwfIcmpStEchosRepliesRx_Type = Counter32
_IwfIcmpStEchosRepliesRx_Object = MibTableColumn
iwfIcmpStEchosRepliesRx = _IwfIcmpStEchosRepliesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 19),
    _IwfIcmpStEchosRepliesRx_Type()
)
iwfIcmpStEchosRepliesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStEchosRepliesRx.setStatus("mandatory")
_IwfIcmpStTimeStampsTx_Type = Counter32
_IwfIcmpStTimeStampsTx_Object = MibTableColumn
iwfIcmpStTimeStampsTx = _IwfIcmpStTimeStampsTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 20),
    _IwfIcmpStTimeStampsTx_Type()
)
iwfIcmpStTimeStampsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStTimeStampsTx.setStatus("mandatory")
_IwfIcmpStTimeStampsRx_Type = Counter32
_IwfIcmpStTimeStampsRx_Object = MibTableColumn
iwfIcmpStTimeStampsRx = _IwfIcmpStTimeStampsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 21),
    _IwfIcmpStTimeStampsRx_Type()
)
iwfIcmpStTimeStampsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStTimeStampsRx.setStatus("mandatory")
_IwfIcmpStAddressMasksTx_Type = Counter32
_IwfIcmpStAddressMasksTx_Object = MibTableColumn
iwfIcmpStAddressMasksTx = _IwfIcmpStAddressMasksTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 22),
    _IwfIcmpStAddressMasksTx_Type()
)
iwfIcmpStAddressMasksTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStAddressMasksTx.setStatus("mandatory")
_IwfIcmpStAddressMasksRx_Type = Counter32
_IwfIcmpStAddressMasksRx_Object = MibTableColumn
iwfIcmpStAddressMasksRx = _IwfIcmpStAddressMasksRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 23),
    _IwfIcmpStAddressMasksRx_Type()
)
iwfIcmpStAddressMasksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStAddressMasksRx.setStatus("mandatory")
_IwfIcmpStAddressMasksRepliesTx_Type = Counter32
_IwfIcmpStAddressMasksRepliesTx_Object = MibTableColumn
iwfIcmpStAddressMasksRepliesTx = _IwfIcmpStAddressMasksRepliesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 24),
    _IwfIcmpStAddressMasksRepliesTx_Type()
)
iwfIcmpStAddressMasksRepliesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStAddressMasksRepliesTx.setStatus("mandatory")
_IwfIcmpStAddressMasksRepliesRx_Type = Counter32
_IwfIcmpStAddressMasksRepliesRx_Object = MibTableColumn
iwfIcmpStAddressMasksRepliesRx = _IwfIcmpStAddressMasksRepliesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 9, 1, 1, 25),
    _IwfIcmpStAddressMasksRepliesRx_Type()
)
iwfIcmpStAddressMasksRepliesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfIcmpStAddressMasksRepliesRx.setStatus("mandatory")
_IwfTcpStats_ObjectIdentity = ObjectIdentity
iwfTcpStats = _IwfTcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10)
)
_IwfTcpStatsTable_Object = MibTable
iwfTcpStatsTable = _IwfTcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1)
)
if mibBuilder.loadTexts:
    iwfTcpStatsTable.setStatus("mandatory")
_IwfTcpStatsEntry_Object = MibTableRow
iwfTcpStatsEntry = _IwfTcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1)
)
iwfTcpStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfTcpStIndex"),
)
if mibBuilder.loadTexts:
    iwfTcpStatsEntry.setStatus("mandatory")
_IwfTcpStIndex_Type = Integer32
_IwfTcpStIndex_Object = MibTableColumn
iwfTcpStIndex = _IwfTcpStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 1),
    _IwfTcpStIndex_Type()
)
iwfTcpStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStIndex.setStatus("mandatory")
_IwfTcpStActiveOpens_Type = Counter32
_IwfTcpStActiveOpens_Object = MibTableColumn
iwfTcpStActiveOpens = _IwfTcpStActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 2),
    _IwfTcpStActiveOpens_Type()
)
iwfTcpStActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStActiveOpens.setStatus("mandatory")
_IwfTcpStPassiveOpens_Type = Counter32
_IwfTcpStPassiveOpens_Object = MibTableColumn
iwfTcpStPassiveOpens = _IwfTcpStPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 3),
    _IwfTcpStPassiveOpens_Type()
)
iwfTcpStPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStPassiveOpens.setStatus("mandatory")
_IwfTcpStFailedConnectAttempts_Type = Counter32
_IwfTcpStFailedConnectAttempts_Object = MibTableColumn
iwfTcpStFailedConnectAttempts = _IwfTcpStFailedConnectAttempts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 4),
    _IwfTcpStFailedConnectAttempts_Type()
)
iwfTcpStFailedConnectAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStFailedConnectAttempts.setStatus("mandatory")
_IwfTcpStResetConnections_Type = Counter32
_IwfTcpStResetConnections_Object = MibTableColumn
iwfTcpStResetConnections = _IwfTcpStResetConnections_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 5),
    _IwfTcpStResetConnections_Type()
)
iwfTcpStResetConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStResetConnections.setStatus("mandatory")
_IwfTcpStCurrentConnections_Type = Counter32
_IwfTcpStCurrentConnections_Object = MibTableColumn
iwfTcpStCurrentConnections = _IwfTcpStCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 6),
    _IwfTcpStCurrentConnections_Type()
)
iwfTcpStCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStCurrentConnections.setStatus("mandatory")
_IwfTcpStSegmentRx_Type = Counter32
_IwfTcpStSegmentRx_Object = MibTableColumn
iwfTcpStSegmentRx = _IwfTcpStSegmentRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 7),
    _IwfTcpStSegmentRx_Type()
)
iwfTcpStSegmentRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStSegmentRx.setStatus("mandatory")
_IwfTcpStSegmentTx_Type = Counter32
_IwfTcpStSegmentTx_Object = MibTableColumn
iwfTcpStSegmentTx = _IwfTcpStSegmentTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 8),
    _IwfTcpStSegmentTx_Type()
)
iwfTcpStSegmentTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStSegmentTx.setStatus("mandatory")
_IwfTcpStSegmentRetransmitted_Type = Counter32
_IwfTcpStSegmentRetransmitted_Object = MibTableColumn
iwfTcpStSegmentRetransmitted = _IwfTcpStSegmentRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 10, 1, 1, 9),
    _IwfTcpStSegmentRetransmitted_Type()
)
iwfTcpStSegmentRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpStSegmentRetransmitted.setStatus("mandatory")
_IwfUdpStats_ObjectIdentity = ObjectIdentity
iwfUdpStats = _IwfUdpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11)
)
_IwfUdpStatsTable_Object = MibTable
iwfUdpStatsTable = _IwfUdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1)
)
if mibBuilder.loadTexts:
    iwfUdpStatsTable.setStatus("mandatory")
_IwfUdpStatsEntry_Object = MibTableRow
iwfUdpStatsEntry = _IwfUdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1, 1)
)
iwfUdpStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfUdpStIndex"),
)
if mibBuilder.loadTexts:
    iwfUdpStatsEntry.setStatus("mandatory")
_IwfUdpStIndex_Type = Integer32
_IwfUdpStIndex_Object = MibTableColumn
iwfUdpStIndex = _IwfUdpStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1, 1, 1),
    _IwfUdpStIndex_Type()
)
iwfUdpStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfUdpStIndex.setStatus("mandatory")
_IwfUdpStDatagramRx_Type = Counter32
_IwfUdpStDatagramRx_Object = MibTableColumn
iwfUdpStDatagramRx = _IwfUdpStDatagramRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1, 1, 2),
    _IwfUdpStDatagramRx_Type()
)
iwfUdpStDatagramRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfUdpStDatagramRx.setStatus("mandatory")
_IwfUdpStDatagramNoPorts_Type = Counter32
_IwfUdpStDatagramNoPorts_Object = MibTableColumn
iwfUdpStDatagramNoPorts = _IwfUdpStDatagramNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1, 1, 3),
    _IwfUdpStDatagramNoPorts_Type()
)
iwfUdpStDatagramNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfUdpStDatagramNoPorts.setStatus("mandatory")
_IwfUdpStErrorsRx_Type = Counter32
_IwfUdpStErrorsRx_Object = MibTableColumn
iwfUdpStErrorsRx = _IwfUdpStErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1, 1, 4),
    _IwfUdpStErrorsRx_Type()
)
iwfUdpStErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfUdpStErrorsRx.setStatus("mandatory")
_IwfUdpStDatagramtx_Type = Counter32
_IwfUdpStDatagramtx_Object = MibTableColumn
iwfUdpStDatagramtx = _IwfUdpStDatagramtx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 11, 1, 1, 5),
    _IwfUdpStDatagramtx_Type()
)
iwfUdpStDatagramtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfUdpStDatagramtx.setStatus("mandatory")
_IwfPppStats_ObjectIdentity = ObjectIdentity
iwfPppStats = _IwfPppStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12)
)
_IwfPppStatsTable_Object = MibTable
iwfPppStatsTable = _IwfPppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1)
)
if mibBuilder.loadTexts:
    iwfPppStatsTable.setStatus("mandatory")
_IwfPppStatsEntry_Object = MibTableRow
iwfPppStatsEntry = _IwfPppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1)
)
iwfPppStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfPppStIndex"),
)
if mibBuilder.loadTexts:
    iwfPppStatsEntry.setStatus("mandatory")
_IwfPppStIndex_Type = Integer32
_IwfPppStIndex_Object = MibTableColumn
iwfPppStIndex = _IwfPppStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 1),
    _IwfPppStIndex_Type()
)
iwfPppStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStIndex.setStatus("mandatory")
_IwfPppStBytesTx_Type = Counter32
_IwfPppStBytesTx_Object = MibTableColumn
iwfPppStBytesTx = _IwfPppStBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 2),
    _IwfPppStBytesTx_Type()
)
iwfPppStBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStBytesTx.setStatus("mandatory")
_IwfPppStBytesRx_Type = Counter32
_IwfPppStBytesRx_Object = MibTableColumn
iwfPppStBytesRx = _IwfPppStBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 3),
    _IwfPppStBytesRx_Type()
)
iwfPppStBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStBytesRx.setStatus("mandatory")
_IwfPppStFramesTx_Type = Counter32
_IwfPppStFramesTx_Object = MibTableColumn
iwfPppStFramesTx = _IwfPppStFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 4),
    _IwfPppStFramesTx_Type()
)
iwfPppStFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStFramesTx.setStatus("mandatory")
_IwfPppStFramesRx_Type = Counter32
_IwfPppStFramesRx_Object = MibTableColumn
iwfPppStFramesRx = _IwfPppStFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 5),
    _IwfPppStFramesRx_Type()
)
iwfPppStFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStFramesRx.setStatus("mandatory")
_IwfPppStPercentCompressionOut_Type = Counter32
_IwfPppStPercentCompressionOut_Object = MibTableColumn
iwfPppStPercentCompressionOut = _IwfPppStPercentCompressionOut_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 6),
    _IwfPppStPercentCompressionOut_Type()
)
iwfPppStPercentCompressionOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStPercentCompressionOut.setStatus("mandatory")
_IwfPppStPercentCompressionIn_Type = Counter32
_IwfPppStPercentCompressionIn_Object = MibTableColumn
iwfPppStPercentCompressionIn = _IwfPppStPercentCompressionIn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 7),
    _IwfPppStPercentCompressionIn_Type()
)
iwfPppStPercentCompressionIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStPercentCompressionIn.setStatus("mandatory")
_IwfPppStCrcErrors_Type = Counter32
_IwfPppStCrcErrors_Object = MibTableColumn
iwfPppStCrcErrors = _IwfPppStCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 8),
    _IwfPppStCrcErrors_Type()
)
iwfPppStCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStCrcErrors.setStatus("mandatory")
_IwfPppStAlignmentErrors_Type = Counter32
_IwfPppStAlignmentErrors_Object = MibTableColumn
iwfPppStAlignmentErrors = _IwfPppStAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 9),
    _IwfPppStAlignmentErrors_Type()
)
iwfPppStAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStAlignmentErrors.setStatus("mandatory")
_IwfPppStTimeOutErrors_Type = Counter32
_IwfPppStTimeOutErrors_Object = MibTableColumn
iwfPppStTimeOutErrors = _IwfPppStTimeOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 10),
    _IwfPppStTimeOutErrors_Type()
)
iwfPppStTimeOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStTimeOutErrors.setStatus("mandatory")
_IwfPppStTotalErrors_Type = Counter32
_IwfPppStTotalErrors_Object = MibTableColumn
iwfPppStTotalErrors = _IwfPppStTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 11),
    _IwfPppStTotalErrors_Type()
)
iwfPppStTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStTotalErrors.setStatus("mandatory")
_IwfPppStBytesTxPerSec_Type = Counter32
_IwfPppStBytesTxPerSec_Object = MibTableColumn
iwfPppStBytesTxPerSec = _IwfPppStBytesTxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 12),
    _IwfPppStBytesTxPerSec_Type()
)
iwfPppStBytesTxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStBytesTxPerSec.setStatus("mandatory")
_IwfPppStBytesRxPerSec_Type = Counter32
_IwfPppStBytesRxPerSec_Object = MibTableColumn
iwfPppStBytesRxPerSec = _IwfPppStBytesRxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 13),
    _IwfPppStBytesRxPerSec_Type()
)
iwfPppStBytesRxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStBytesRxPerSec.setStatus("mandatory")
_IwfPppStFramesTxPerSec_Type = Counter32
_IwfPppStFramesTxPerSec_Object = MibTableColumn
iwfPppStFramesTxPerSec = _IwfPppStFramesTxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 14),
    _IwfPppStFramesTxPerSec_Type()
)
iwfPppStFramesTxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStFramesTxPerSec.setStatus("mandatory")
_IwfPppStFramesRxPerSec_Type = Counter32
_IwfPppStFramesRxPerSec_Object = MibTableColumn
iwfPppStFramesRxPerSec = _IwfPppStFramesRxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 15),
    _IwfPppStFramesRxPerSec_Type()
)
iwfPppStFramesRxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStFramesRxPerSec.setStatus("mandatory")
_IwfPppStTotalErrorPerSec_Type = Counter32
_IwfPppStTotalErrorPerSec_Object = MibTableColumn
iwfPppStTotalErrorPerSec = _IwfPppStTotalErrorPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 16),
    _IwfPppStTotalErrorPerSec_Type()
)
iwfPppStTotalErrorPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStTotalErrorPerSec.setStatus("mandatory")
_IwfPppStTotalConnections_Type = Counter32
_IwfPppStTotalConnections_Object = MibTableColumn
iwfPppStTotalConnections = _IwfPppStTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 12, 1, 1, 17),
    _IwfPppStTotalConnections_Type()
)
iwfPppStTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppStTotalConnections.setStatus("mandatory")
_IwfTdmStats_ObjectIdentity = ObjectIdentity
iwfTdmStats = _IwfTdmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13)
)
_IwfTdmStatsTable_Object = MibTable
iwfTdmStatsTable = _IwfTdmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1)
)
if mibBuilder.loadTexts:
    iwfTdmStatsTable.setStatus("mandatory")
_IwfTdmStatsEntry_Object = MibTableRow
iwfTdmStatsEntry = _IwfTdmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1)
)
iwfTdmStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfTdmStIndex"),
)
if mibBuilder.loadTexts:
    iwfTdmStatsEntry.setStatus("mandatory")
_IwfTdmStIndex_Type = Integer32
_IwfTdmStIndex_Object = MibTableColumn
iwfTdmStIndex = _IwfTdmStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 1),
    _IwfTdmStIndex_Type()
)
iwfTdmStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStIndex.setStatus("mandatory")
_IwfTdmStFramesOverruns_Type = Counter32
_IwfTdmStFramesOverruns_Object = MibTableColumn
iwfTdmStFramesOverruns = _IwfTdmStFramesOverruns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 2),
    _IwfTdmStFramesOverruns_Type()
)
iwfTdmStFramesOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStFramesOverruns.setStatus("mandatory")
_IwfTdmStAbortFramesrx_Type = Counter32
_IwfTdmStAbortFramesrx_Object = MibTableColumn
iwfTdmStAbortFramesrx = _IwfTdmStAbortFramesrx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 3),
    _IwfTdmStAbortFramesrx_Type()
)
iwfTdmStAbortFramesrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStAbortFramesrx.setStatus("mandatory")
_IwfTdmStCrcErrors_Type = Counter32
_IwfTdmStCrcErrors_Object = MibTableColumn
iwfTdmStCrcErrors = _IwfTdmStCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 4),
    _IwfTdmStCrcErrors_Type()
)
iwfTdmStCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStCrcErrors.setStatus("mandatory")
_IwfTdmStClockLossis_Type = Counter32
_IwfTdmStClockLossis_Object = MibTableColumn
iwfTdmStClockLossis = _IwfTdmStClockLossis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 5),
    _IwfTdmStClockLossis_Type()
)
iwfTdmStClockLossis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStClockLossis.setStatus("mandatory")
_IwfTdmStAccumSubsystemErrors_Type = Counter32
_IwfTdmStAccumSubsystemErrors_Object = MibTableColumn
iwfTdmStAccumSubsystemErrors = _IwfTdmStAccumSubsystemErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 6),
    _IwfTdmStAccumSubsystemErrors_Type()
)
iwfTdmStAccumSubsystemErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStAccumSubsystemErrors.setStatus("mandatory")


class _IwfTdmStClkStatus_Type(Integer32):
    """Custom type iwfTdmStClkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockDown", 2),
          ("clockUp", 1))
    )


_IwfTdmStClkStatus_Type.__name__ = "Integer32"
_IwfTdmStClkStatus_Object = MibTableColumn
iwfTdmStClkStatus = _IwfTdmStClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 13, 1, 1, 7),
    _IwfTdmStClkStatus_Type()
)
iwfTdmStClkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmStClkStatus.setStatus("mandatory")
_IwfPbStats_ObjectIdentity = ObjectIdentity
iwfPbStats = _IwfPbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14)
)
_IwfPbStatsTable_Object = MibTable
iwfPbStatsTable = _IwfPbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1)
)
if mibBuilder.loadTexts:
    iwfPbStatsTable.setStatus("mandatory")
_IwfPbStatsEntry_Object = MibTableRow
iwfPbStatsEntry = _IwfPbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1)
)
iwfPbStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfPbStIndex"),
)
if mibBuilder.loadTexts:
    iwfPbStatsEntry.setStatus("mandatory")
_IwfPbStIndex_Type = Integer32
_IwfPbStIndex_Object = MibTableColumn
iwfPbStIndex = _IwfPbStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 1),
    _IwfPbStIndex_Type()
)
iwfPbStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStIndex.setStatus("mandatory")
_IwfPbStFramesOverruns_Type = Counter32
_IwfPbStFramesOverruns_Object = MibTableColumn
iwfPbStFramesOverruns = _IwfPbStFramesOverruns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 2),
    _IwfPbStFramesOverruns_Type()
)
iwfPbStFramesOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStFramesOverruns.setStatus("mandatory")
_IwfPbStAbortFramesrx_Type = Counter32
_IwfPbStAbortFramesrx_Object = MibTableColumn
iwfPbStAbortFramesrx = _IwfPbStAbortFramesrx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 3),
    _IwfPbStAbortFramesrx_Type()
)
iwfPbStAbortFramesrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStAbortFramesrx.setStatus("mandatory")
_IwfPbStCrcErrors_Type = Counter32
_IwfPbStCrcErrors_Object = MibTableColumn
iwfPbStCrcErrors = _IwfPbStCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 4),
    _IwfPbStCrcErrors_Type()
)
iwfPbStCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStCrcErrors.setStatus("mandatory")
_IwfPbStClockLosses_Type = Counter32
_IwfPbStClockLosses_Object = MibTableColumn
iwfPbStClockLosses = _IwfPbStClockLosses_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 5),
    _IwfPbStClockLosses_Type()
)
iwfPbStClockLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStClockLosses.setStatus("mandatory")
_IwfPbStAccumSubsystemErrors_Type = Counter32
_IwfPbStAccumSubsystemErrors_Object = MibTableColumn
iwfPbStAccumSubsystemErrors = _IwfPbStAccumSubsystemErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 6),
    _IwfPbStAccumSubsystemErrors_Type()
)
iwfPbStAccumSubsystemErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStAccumSubsystemErrors.setStatus("mandatory")


class _IwfPbStClkStatus_Type(Integer32):
    """Custom type iwfPbStClkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockDown", 2),
          ("clockUp", 1))
    )


_IwfPbStClkStatus_Type.__name__ = "Integer32"
_IwfPbStClkStatus_Object = MibTableColumn
iwfPbStClkStatus = _IwfPbStClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 7),
    _IwfPbStClkStatus_Type()
)
iwfPbStClkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStClkStatus.setStatus("mandatory")
_IwfPbStLinkLosses_Type = Counter32
_IwfPbStLinkLosses_Object = MibTableColumn
iwfPbStLinkLosses = _IwfPbStLinkLosses_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 14, 1, 1, 8),
    _IwfPbStLinkLosses_Type()
)
iwfPbStLinkLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbStLinkLosses.setStatus("mandatory")
_IwfQ921Stats_ObjectIdentity = ObjectIdentity
iwfQ921Stats = _IwfQ921Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 15)
)
_IwfQ921StatsTable_Object = MibTable
iwfQ921StatsTable = _IwfQ921StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 15, 1)
)
if mibBuilder.loadTexts:
    iwfQ921StatsTable.setStatus("mandatory")
_IwfQ921StatsEntry_Object = MibTableRow
iwfQ921StatsEntry = _IwfQ921StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 15, 1, 1)
)
iwfQ921StatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfQ921StIndex"),
)
if mibBuilder.loadTexts:
    iwfQ921StatsEntry.setStatus("mandatory")
_IwfQ921StIndex_Type = Integer32
_IwfQ921StIndex_Object = MibTableColumn
iwfQ921StIndex = _IwfQ921StIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 15, 1, 1, 1),
    _IwfQ921StIndex_Type()
)
iwfQ921StIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQ921StIndex.setStatus("mandatory")
_IwfQ921StAccumLinkLosses_Type = Counter32
_IwfQ921StAccumLinkLosses_Object = MibTableColumn
iwfQ921StAccumLinkLosses = _IwfQ921StAccumLinkLosses_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 15, 1, 1, 2),
    _IwfQ921StAccumLinkLosses_Type()
)
iwfQ921StAccumLinkLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQ921StAccumLinkLosses.setStatus("mandatory")
_IwfQ921StAccumFrsvcSusSysError_Type = Counter32
_IwfQ921StAccumFrsvcSusSysError_Object = MibTableColumn
iwfQ921StAccumFrsvcSusSysError = _IwfQ921StAccumFrsvcSusSysError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 15, 1, 1, 3),
    _IwfQ921StAccumFrsvcSusSysError_Type()
)
iwfQ921StAccumFrsvcSusSysError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQ921StAccumFrsvcSusSysError.setStatus("mandatory")
_IwfQ933Stats_ObjectIdentity = ObjectIdentity
iwfQ933Stats = _IwfQ933Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 16)
)
_IwfQ933StatsTable_Object = MibTable
iwfQ933StatsTable = _IwfQ933StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 16, 1)
)
if mibBuilder.loadTexts:
    iwfQ933StatsTable.setStatus("mandatory")
_IwfQ933StatsEntry_Object = MibTableRow
iwfQ933StatsEntry = _IwfQ933StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 16, 1, 1)
)
iwfQ933StatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfQ933StIndex"),
)
if mibBuilder.loadTexts:
    iwfQ933StatsEntry.setStatus("mandatory")
_IwfQ933StIndex_Type = Integer32
_IwfQ933StIndex_Object = MibTableColumn
iwfQ933StIndex = _IwfQ933StIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 16, 1, 1, 1),
    _IwfQ933StIndex_Type()
)
iwfQ933StIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQ933StIndex.setStatus("mandatory")
_IwfQ933StAccumUknownIframes_Type = Counter32
_IwfQ933StAccumUknownIframes_Object = MibTableColumn
iwfQ933StAccumUknownIframes = _IwfQ933StAccumUknownIframes_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 16, 1, 1, 2),
    _IwfQ933StAccumUknownIframes_Type()
)
iwfQ933StAccumUknownIframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQ933StAccumUknownIframes.setStatus("mandatory")
_IwfQ933StAccumOutOfSeqIframes_Type = Counter32
_IwfQ933StAccumOutOfSeqIframes_Object = MibTableColumn
iwfQ933StAccumOutOfSeqIframes = _IwfQ933StAccumOutOfSeqIframes_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 16, 1, 1, 3),
    _IwfQ933StAccumOutOfSeqIframes_Type()
)
iwfQ933StAccumOutOfSeqIframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQ933StAccumOutOfSeqIframes.setStatus("mandatory")
_IwfMdmStats_ObjectIdentity = ObjectIdentity
iwfMdmStats = _IwfMdmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 17)
)
_IwfMdmStatsTable_Object = MibTable
iwfMdmStatsTable = _IwfMdmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 17, 1)
)
if mibBuilder.loadTexts:
    iwfMdmStatsTable.setStatus("mandatory")
_IwfMdmStatsEntry_Object = MibTableRow
iwfMdmStatsEntry = _IwfMdmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 17, 1, 1)
)
iwfMdmStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfMdmStIndex"),
)
if mibBuilder.loadTexts:
    iwfMdmStatsEntry.setStatus("mandatory")
_IwfMdmStIndex_Type = Integer32
_IwfMdmStIndex_Object = MibTableColumn
iwfMdmStIndex = _IwfMdmStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 17, 1, 1, 1),
    _IwfMdmStIndex_Type()
)
iwfMdmStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfMdmStIndex.setStatus("mandatory")
_IwfMdmStAccumInvalidAtCmd_Type = Integer32
_IwfMdmStAccumInvalidAtCmd_Object = MibTableColumn
iwfMdmStAccumInvalidAtCmd = _IwfMdmStAccumInvalidAtCmd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 17, 1, 1, 2),
    _IwfMdmStAccumInvalidAtCmd_Type()
)
iwfMdmStAccumInvalidAtCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfMdmStAccumInvalidAtCmd.setStatus("mandatory")
_IwfCmpStats_ObjectIdentity = ObjectIdentity
iwfCmpStats = _IwfCmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 18)
)
_IwfCmpStatsTable_Object = MibTable
iwfCmpStatsTable = _IwfCmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 18, 1)
)
if mibBuilder.loadTexts:
    iwfCmpStatsTable.setStatus("mandatory")
_IwfCmpStatsEntry_Object = MibTableRow
iwfCmpStatsEntry = _IwfCmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 18, 1, 1)
)
iwfCmpStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCmpStIndex"),
)
if mibBuilder.loadTexts:
    iwfCmpStatsEntry.setStatus("mandatory")
_IwfCmpStIndex_Type = Integer32
_IwfCmpStIndex_Object = MibTableColumn
iwfCmpStIndex = _IwfCmpStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 18, 1, 1, 1),
    _IwfCmpStIndex_Type()
)
iwfCmpStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCmpStIndex.setStatus("mandatory")
_IwfCmpStAccumSubsysErrors_Type = Counter32
_IwfCmpStAccumSubsysErrors_Object = MibTableColumn
iwfCmpStAccumSubsysErrors = _IwfCmpStAccumSubsysErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 18, 1, 1, 2),
    _IwfCmpStAccumSubsysErrors_Type()
)
iwfCmpStAccumSubsysErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCmpStAccumSubsysErrors.setStatus("mandatory")
_IwfCallStats_ObjectIdentity = ObjectIdentity
iwfCallStats = _IwfCallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19)
)
_IwfCallStatsTable_Object = MibTable
iwfCallStatsTable = _IwfCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1)
)
if mibBuilder.loadTexts:
    iwfCallStatsTable.setStatus("mandatory")
_IwfCallStatsEntry_Object = MibTableRow
iwfCallStatsEntry = _IwfCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1)
)
iwfCallStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCallStIndex"),
)
if mibBuilder.loadTexts:
    iwfCallStatsEntry.setStatus("mandatory")
_IwfCallStIndex_Type = Integer32
_IwfCallStIndex_Object = MibTableColumn
iwfCallStIndex = _IwfCallStIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 1),
    _IwfCallStIndex_Type()
)
iwfCallStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStIndex.setStatus("mandatory")
_IwfCallStTotConnAd9600MobOrg_Type = Counter32
_IwfCallStTotConnAd9600MobOrg_Object = MibTableColumn
iwfCallStTotConnAd9600MobOrg = _IwfCallStTotConnAd9600MobOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 2),
    _IwfCallStTotConnAd9600MobOrg_Type()
)
iwfCallStTotConnAd9600MobOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnAd9600MobOrg.setStatus("mandatory")
_IwfCallStTotConnAd14400MobOrg_Type = Counter32
_IwfCallStTotConnAd14400MobOrg_Object = MibTableColumn
iwfCallStTotConnAd14400MobOrg = _IwfCallStTotConnAd14400MobOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 3),
    _IwfCallStTotConnAd14400MobOrg_Type()
)
iwfCallStTotConnAd14400MobOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnAd14400MobOrg.setStatus("mandatory")
_IwfCallStTotConnFax9600MobOrg_Type = Counter32
_IwfCallStTotConnFax9600MobOrg_Object = MibTableColumn
iwfCallStTotConnFax9600MobOrg = _IwfCallStTotConnFax9600MobOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 4),
    _IwfCallStTotConnFax9600MobOrg_Type()
)
iwfCallStTotConnFax9600MobOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnFax9600MobOrg.setStatus("mandatory")
_IwfCallStTotConnFax14400MobOrg_Type = Counter32
_IwfCallStTotConnFax14400MobOrg_Object = MibTableColumn
iwfCallStTotConnFax14400MobOrg = _IwfCallStTotConnFax14400MobOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 5),
    _IwfCallStTotConnFax14400MobOrg_Type()
)
iwfCallStTotConnFax14400MobOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnFax14400MobOrg.setStatus("mandatory")
_IwfCallStTotConnAd9600MoTerm_Type = Counter32
_IwfCallStTotConnAd9600MoTerm_Object = MibTableColumn
iwfCallStTotConnAd9600MoTerm = _IwfCallStTotConnAd9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 6),
    _IwfCallStTotConnAd9600MoTerm_Type()
)
iwfCallStTotConnAd9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnAd9600MoTerm.setStatus("mandatory")
_IwfCallStTotConnAd14400MoTerm_Type = Counter32
_IwfCallStTotConnAd14400MoTerm_Object = MibTableColumn
iwfCallStTotConnAd14400MoTerm = _IwfCallStTotConnAd14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 7),
    _IwfCallStTotConnAd14400MoTerm_Type()
)
iwfCallStTotConnAd14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnAd14400MoTerm.setStatus("mandatory")
_IwfCallStTotConnFax9600MoTerm_Type = Counter32
_IwfCallStTotConnFax9600MoTerm_Object = MibTableColumn
iwfCallStTotConnFax9600MoTerm = _IwfCallStTotConnFax9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 8),
    _IwfCallStTotConnFax9600MoTerm_Type()
)
iwfCallStTotConnFax9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnFax9600MoTerm.setStatus("mandatory")
_IwfCallStTotConnFax14400MoTerm_Type = Counter32
_IwfCallStTotConnFax14400MoTerm_Object = MibTableColumn
iwfCallStTotConnFax14400MoTerm = _IwfCallStTotConnFax14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 9),
    _IwfCallStTotConnFax14400MoTerm_Type()
)
iwfCallStTotConnFax14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotConnFax14400MoTerm.setStatus("mandatory")
_IwfCallStTotTermAd9600MoOrg_Type = Counter32
_IwfCallStTotTermAd9600MoOrg_Object = MibTableColumn
iwfCallStTotTermAd9600MoOrg = _IwfCallStTotTermAd9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 10),
    _IwfCallStTotTermAd9600MoOrg_Type()
)
iwfCallStTotTermAd9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermAd9600MoOrg.setStatus("mandatory")
_IwfCallStTotTermAd14400MoOrg_Type = Counter32
_IwfCallStTotTermAd14400MoOrg_Object = MibTableColumn
iwfCallStTotTermAd14400MoOrg = _IwfCallStTotTermAd14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 11),
    _IwfCallStTotTermAd14400MoOrg_Type()
)
iwfCallStTotTermAd14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermAd14400MoOrg.setStatus("mandatory")
_IwfCallStTotTermFax9600MoOrg_Type = Counter32
_IwfCallStTotTermFax9600MoOrg_Object = MibTableColumn
iwfCallStTotTermFax9600MoOrg = _IwfCallStTotTermFax9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 12),
    _IwfCallStTotTermFax9600MoOrg_Type()
)
iwfCallStTotTermFax9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermFax9600MoOrg.setStatus("mandatory")
_IwfCallStTotTermFax14400MoOrg_Type = Counter32
_IwfCallStTotTermFax14400MoOrg_Object = MibTableColumn
iwfCallStTotTermFax14400MoOrg = _IwfCallStTotTermFax14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 13),
    _IwfCallStTotTermFax14400MoOrg_Type()
)
iwfCallStTotTermFax14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermFax14400MoOrg.setStatus("mandatory")
_IwfCallStTotTermAd9600MoTerm_Type = Counter32
_IwfCallStTotTermAd9600MoTerm_Object = MibTableColumn
iwfCallStTotTermAd9600MoTerm = _IwfCallStTotTermAd9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 14),
    _IwfCallStTotTermAd9600MoTerm_Type()
)
iwfCallStTotTermAd9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermAd9600MoTerm.setStatus("mandatory")
_IwfCallStTotTermAd14400MoTerm_Type = Counter32
_IwfCallStTotTermAd14400MoTerm_Object = MibTableColumn
iwfCallStTotTermAd14400MoTerm = _IwfCallStTotTermAd14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 15),
    _IwfCallStTotTermAd14400MoTerm_Type()
)
iwfCallStTotTermAd14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermAd14400MoTerm.setStatus("mandatory")
_IwfCallStTotTermFax9600MoTerm_Type = Counter32
_IwfCallStTotTermFax9600MoTerm_Object = MibTableColumn
iwfCallStTotTermFax9600MoTerm = _IwfCallStTotTermFax9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 16),
    _IwfCallStTotTermFax9600MoTerm_Type()
)
iwfCallStTotTermFax9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermFax9600MoTerm.setStatus("mandatory")
_IwfCallStTotTermFax14400MoTerm_Type = Counter32
_IwfCallStTotTermFax14400MoTerm_Object = MibTableColumn
iwfCallStTotTermFax14400MoTerm = _IwfCallStTotTermFax14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 17),
    _IwfCallStTotTermFax14400MoTerm_Type()
)
iwfCallStTotTermFax14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotTermFax14400MoTerm.setStatus("mandatory")
_IwfCallStTotCntgAd9600MoOrg_Type = Counter32
_IwfCallStTotCntgAd9600MoOrg_Object = MibTableColumn
iwfCallStTotCntgAd9600MoOrg = _IwfCallStTotCntgAd9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 18),
    _IwfCallStTotCntgAd9600MoOrg_Type()
)
iwfCallStTotCntgAd9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgAd9600MoOrg.setStatus("mandatory")
_IwfCallStTotCntgAd14400MoOrg_Type = Counter32
_IwfCallStTotCntgAd14400MoOrg_Object = MibTableColumn
iwfCallStTotCntgAd14400MoOrg = _IwfCallStTotCntgAd14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 19),
    _IwfCallStTotCntgAd14400MoOrg_Type()
)
iwfCallStTotCntgAd14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgAd14400MoOrg.setStatus("mandatory")
_IwfCallStTotCntgFax9600MoOrg_Type = Counter32
_IwfCallStTotCntgFax9600MoOrg_Object = MibTableColumn
iwfCallStTotCntgFax9600MoOrg = _IwfCallStTotCntgFax9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 20),
    _IwfCallStTotCntgFax9600MoOrg_Type()
)
iwfCallStTotCntgFax9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgFax9600MoOrg.setStatus("mandatory")
_IwfCallStTotCntgFax14400MoOrg_Type = Counter32
_IwfCallStTotCntgFax14400MoOrg_Object = MibTableColumn
iwfCallStTotCntgFax14400MoOrg = _IwfCallStTotCntgFax14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 21),
    _IwfCallStTotCntgFax14400MoOrg_Type()
)
iwfCallStTotCntgFax14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgFax14400MoOrg.setStatus("mandatory")
_IwfCallStTotCntgAd9600MoTerm_Type = Counter32
_IwfCallStTotCntgAd9600MoTerm_Object = MibTableColumn
iwfCallStTotCntgAd9600MoTerm = _IwfCallStTotCntgAd9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 22),
    _IwfCallStTotCntgAd9600MoTerm_Type()
)
iwfCallStTotCntgAd9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgAd9600MoTerm.setStatus("mandatory")
_IwfCallStTotCntgAd14400MoTerm_Type = Counter32
_IwfCallStTotCntgAd14400MoTerm_Object = MibTableColumn
iwfCallStTotCntgAd14400MoTerm = _IwfCallStTotCntgAd14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 23),
    _IwfCallStTotCntgAd14400MoTerm_Type()
)
iwfCallStTotCntgAd14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgAd14400MoTerm.setStatus("mandatory")
_IwfCallStTotCntgFax9600MoTerm_Type = Counter32
_IwfCallStTotCntgFax9600MoTerm_Object = MibTableColumn
iwfCallStTotCntgFax9600MoTerm = _IwfCallStTotCntgFax9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 24),
    _IwfCallStTotCntgFax9600MoTerm_Type()
)
iwfCallStTotCntgFax9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgFax9600MoTerm.setStatus("mandatory")
_IwfCallStTotCntgFax14400MoTerm_Type = Counter32
_IwfCallStTotCntgFax14400MoTerm_Object = MibTableColumn
iwfCallStTotCntgFax14400MoTerm = _IwfCallStTotCntgFax14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 25),
    _IwfCallStTotCntgFax14400MoTerm_Type()
)
iwfCallStTotCntgFax14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCntgFax14400MoTerm.setStatus("mandatory")
_IwfCallStTotDiscAd9600MoOrg_Type = Counter32
_IwfCallStTotDiscAd9600MoOrg_Object = MibTableColumn
iwfCallStTotDiscAd9600MoOrg = _IwfCallStTotDiscAd9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 26),
    _IwfCallStTotDiscAd9600MoOrg_Type()
)
iwfCallStTotDiscAd9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscAd9600MoOrg.setStatus("mandatory")
_IwfCallStTotDiscAd14400MoOrg_Type = Counter32
_IwfCallStTotDiscAd14400MoOrg_Object = MibTableColumn
iwfCallStTotDiscAd14400MoOrg = _IwfCallStTotDiscAd14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 27),
    _IwfCallStTotDiscAd14400MoOrg_Type()
)
iwfCallStTotDiscAd14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscAd14400MoOrg.setStatus("mandatory")
_IwfCallStTotDiscFax9600MoOrg_Type = Counter32
_IwfCallStTotDiscFax9600MoOrg_Object = MibTableColumn
iwfCallStTotDiscFax9600MoOrg = _IwfCallStTotDiscFax9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 28),
    _IwfCallStTotDiscFax9600MoOrg_Type()
)
iwfCallStTotDiscFax9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscFax9600MoOrg.setStatus("mandatory")
_IwfCallStTotDiscFax14400MoOrg_Type = Counter32
_IwfCallStTotDiscFax14400MoOrg_Object = MibTableColumn
iwfCallStTotDiscFax14400MoOrg = _IwfCallStTotDiscFax14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 29),
    _IwfCallStTotDiscFax14400MoOrg_Type()
)
iwfCallStTotDiscFax14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscFax14400MoOrg.setStatus("mandatory")
_IwfCallStTotDiscAd9600MoTerm_Type = Counter32
_IwfCallStTotDiscAd9600MoTerm_Object = MibTableColumn
iwfCallStTotDiscAd9600MoTerm = _IwfCallStTotDiscAd9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 30),
    _IwfCallStTotDiscAd9600MoTerm_Type()
)
iwfCallStTotDiscAd9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscAd9600MoTerm.setStatus("mandatory")
_IwfCallStTotDiscAd14400MoTerm_Type = Counter32
_IwfCallStTotDiscAd14400MoTerm_Object = MibTableColumn
iwfCallStTotDiscAd14400MoTerm = _IwfCallStTotDiscAd14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 31),
    _IwfCallStTotDiscAd14400MoTerm_Type()
)
iwfCallStTotDiscAd14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscAd14400MoTerm.setStatus("mandatory")
_IwfCallStTotDiscFax9600MoTerm_Type = Counter32
_IwfCallStTotDiscFax9600MoTerm_Object = MibTableColumn
iwfCallStTotDiscFax9600MoTerm = _IwfCallStTotDiscFax9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 32),
    _IwfCallStTotDiscFax9600MoTerm_Type()
)
iwfCallStTotDiscFax9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscFax9600MoTerm.setStatus("mandatory")
_IwfCallStTotDiscFax14400MoTerm_Type = Counter32
_IwfCallStTotDiscFax14400MoTerm_Object = MibTableColumn
iwfCallStTotDiscFax14400MoTerm = _IwfCallStTotDiscFax14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 33),
    _IwfCallStTotDiscFax14400MoTerm_Type()
)
iwfCallStTotDiscFax14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotDiscFax14400MoTerm.setStatus("mandatory")
_IwfCallStTotCompv42MoOrg_Type = Counter32
_IwfCallStTotCompv42MoOrg_Object = MibTableColumn
iwfCallStTotCompv42MoOrg = _IwfCallStTotCompv42MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 34),
    _IwfCallStTotCompv42MoOrg_Type()
)
iwfCallStTotCompv42MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCompv42MoOrg.setStatus("mandatory")
_IwfCallStTotCompMmrMoOrg_Type = Counter32
_IwfCallStTotCompMmrMoOrg_Object = MibTableColumn
iwfCallStTotCompMmrMoOrg = _IwfCallStTotCompMmrMoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 35),
    _IwfCallStTotCompMmrMoOrg_Type()
)
iwfCallStTotCompMmrMoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCompMmrMoOrg.setStatus("mandatory")
_IwfCallStTotCompv42MoTerm_Type = Counter32
_IwfCallStTotCompv42MoTerm_Object = MibTableColumn
iwfCallStTotCompv42MoTerm = _IwfCallStTotCompv42MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 36),
    _IwfCallStTotCompv42MoTerm_Type()
)
iwfCallStTotCompv42MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCompv42MoTerm.setStatus("mandatory")
_IwfCallStTotCompMmrMoTerm_Type = Counter32
_IwfCallStTotCompMmrMoTerm_Object = MibTableColumn
iwfCallStTotCompMmrMoTerm = _IwfCallStTotCompMmrMoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 37),
    _IwfCallStTotCompMmrMoTerm_Type()
)
iwfCallStTotCompMmrMoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotCompMmrMoTerm.setStatus("mandatory")
_IwfCallStTotFailAd9600MoOrg_Type = Counter32
_IwfCallStTotFailAd9600MoOrg_Object = MibTableColumn
iwfCallStTotFailAd9600MoOrg = _IwfCallStTotFailAd9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 38),
    _IwfCallStTotFailAd9600MoOrg_Type()
)
iwfCallStTotFailAd9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailAd9600MoOrg.setStatus("mandatory")
_IwfCallStTotFailAd14400MoOrg_Type = Counter32
_IwfCallStTotFailAd14400MoOrg_Object = MibTableColumn
iwfCallStTotFailAd14400MoOrg = _IwfCallStTotFailAd14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 39),
    _IwfCallStTotFailAd14400MoOrg_Type()
)
iwfCallStTotFailAd14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailAd14400MoOrg.setStatus("mandatory")
_IwfCallStTotFailFax9600MoOrg_Type = Counter32
_IwfCallStTotFailFax9600MoOrg_Object = MibTableColumn
iwfCallStTotFailFax9600MoOrg = _IwfCallStTotFailFax9600MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 40),
    _IwfCallStTotFailFax9600MoOrg_Type()
)
iwfCallStTotFailFax9600MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailFax9600MoOrg.setStatus("mandatory")
_IwfCallStTotFailFax14400MoOrg_Type = Counter32
_IwfCallStTotFailFax14400MoOrg_Object = MibTableColumn
iwfCallStTotFailFax14400MoOrg = _IwfCallStTotFailFax14400MoOrg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 41),
    _IwfCallStTotFailFax14400MoOrg_Type()
)
iwfCallStTotFailFax14400MoOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailFax14400MoOrg.setStatus("mandatory")
_IwfCallStTotFailAd9600MoTerm_Type = Counter32
_IwfCallStTotFailAd9600MoTerm_Object = MibTableColumn
iwfCallStTotFailAd9600MoTerm = _IwfCallStTotFailAd9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 42),
    _IwfCallStTotFailAd9600MoTerm_Type()
)
iwfCallStTotFailAd9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailAd9600MoTerm.setStatus("mandatory")
_IwfCallStTotFailAd14400MoTerm_Type = Counter32
_IwfCallStTotFailAd14400MoTerm_Object = MibTableColumn
iwfCallStTotFailAd14400MoTerm = _IwfCallStTotFailAd14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 43),
    _IwfCallStTotFailAd14400MoTerm_Type()
)
iwfCallStTotFailAd14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailAd14400MoTerm.setStatus("mandatory")
_IwfCallStTotFailFax9600MoTerm_Type = Counter32
_IwfCallStTotFailFax9600MoTerm_Object = MibTableColumn
iwfCallStTotFailFax9600MoTerm = _IwfCallStTotFailFax9600MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 44),
    _IwfCallStTotFailFax9600MoTerm_Type()
)
iwfCallStTotFailFax9600MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailFax9600MoTerm.setStatus("mandatory")
_IwfCallStTotFailFax14400MoTerm_Type = Counter32
_IwfCallStTotFailFax14400MoTerm_Object = MibTableColumn
iwfCallStTotFailFax14400MoTerm = _IwfCallStTotFailFax14400MoTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 45),
    _IwfCallStTotFailFax14400MoTerm_Type()
)
iwfCallStTotFailFax14400MoTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStTotFailFax14400MoTerm.setStatus("mandatory")
_IwfCallStCurrentNumConnCalls_Type = Counter32
_IwfCallStCurrentNumConnCalls_Object = MibTableColumn
iwfCallStCurrentNumConnCalls = _IwfCallStCurrentNumConnCalls_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 46),
    _IwfCallStCurrentNumConnCalls_Type()
)
iwfCallStCurrentNumConnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStCurrentNumConnCalls.setStatus("mandatory")
_IwfCallStCurrentNumCompCalls_Type = Counter32
_IwfCallStCurrentNumCompCalls_Object = MibTableColumn
iwfCallStCurrentNumCompCalls = _IwfCallStCurrentNumCompCalls_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 47),
    _IwfCallStCurrentNumCompCalls_Type()
)
iwfCallStCurrentNumCompCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStCurrentNumCompCalls.setStatus("mandatory")
_IwfCallStQncConnectedSs9600_Type = Counter32
_IwfCallStQncConnectedSs9600_Object = MibTableColumn
iwfCallStQncConnectedSs9600 = _IwfCallStQncConnectedSs9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 48),
    _IwfCallStQncConnectedSs9600_Type()
)
iwfCallStQncConnectedSs9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedSs9600.setStatus("mandatory")
_IwfCallStQncConnectedL2tp9600_Type = Counter32
_IwfCallStQncConnectedL2tp9600_Object = MibTableColumn
iwfCallStQncConnectedL2tp9600 = _IwfCallStQncConnectedL2tp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 49),
    _IwfCallStQncConnectedL2tp9600_Type()
)
iwfCallStQncConnectedL2tp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedL2tp9600.setStatus("mandatory")
_IwfCallStQncConnectedPptp9600_Type = Counter32
_IwfCallStQncConnectedPptp9600_Object = MibTableColumn
iwfCallStQncConnectedPptp9600 = _IwfCallStQncConnectedPptp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 50),
    _IwfCallStQncConnectedPptp9600_Type()
)
iwfCallStQncConnectedPptp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedPptp9600.setStatus("mandatory")
_IwfCallStQncConnectedPpp9600_Type = Counter32
_IwfCallStQncConnectedPpp9600_Object = MibTableColumn
iwfCallStQncConnectedPpp9600 = _IwfCallStQncConnectedPpp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 51),
    _IwfCallStQncConnectedPpp9600_Type()
)
iwfCallStQncConnectedPpp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedPpp9600.setStatus("mandatory")
_IwfCallStQncTerminatedSs9600_Type = Counter32
_IwfCallStQncTerminatedSs9600_Object = MibTableColumn
iwfCallStQncTerminatedSs9600 = _IwfCallStQncTerminatedSs9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 52),
    _IwfCallStQncTerminatedSs9600_Type()
)
iwfCallStQncTerminatedSs9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedSs9600.setStatus("mandatory")
_IwfCallStQncTerminatedL2tp9600_Type = Counter32
_IwfCallStQncTerminatedL2tp9600_Object = MibTableColumn
iwfCallStQncTerminatedL2tp9600 = _IwfCallStQncTerminatedL2tp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 53),
    _IwfCallStQncTerminatedL2tp9600_Type()
)
iwfCallStQncTerminatedL2tp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedL2tp9600.setStatus("mandatory")
_IwfCallStQncTerminatedPptp9600_Type = Counter32
_IwfCallStQncTerminatedPptp9600_Object = MibTableColumn
iwfCallStQncTerminatedPptp9600 = _IwfCallStQncTerminatedPptp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 54),
    _IwfCallStQncTerminatedPptp9600_Type()
)
iwfCallStQncTerminatedPptp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedPptp9600.setStatus("mandatory")
_IwfCallStQncTerminatedPpp9600_Type = Counter32
_IwfCallStQncTerminatedPpp9600_Object = MibTableColumn
iwfCallStQncTerminatedPpp9600 = _IwfCallStQncTerminatedPpp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 55),
    _IwfCallStQncTerminatedPpp9600_Type()
)
iwfCallStQncTerminatedPpp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedPpp9600.setStatus("mandatory")
_IwfCallStQncConnectingSs9600_Type = Counter32
_IwfCallStQncConnectingSs9600_Object = MibTableColumn
iwfCallStQncConnectingSs9600 = _IwfCallStQncConnectingSs9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 56),
    _IwfCallStQncConnectingSs9600_Type()
)
iwfCallStQncConnectingSs9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingSs9600.setStatus("mandatory")
_IwfCallStQncConnectingL2tp9600_Type = Counter32
_IwfCallStQncConnectingL2tp9600_Object = MibTableColumn
iwfCallStQncConnectingL2tp9600 = _IwfCallStQncConnectingL2tp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 57),
    _IwfCallStQncConnectingL2tp9600_Type()
)
iwfCallStQncConnectingL2tp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingL2tp9600.setStatus("mandatory")
_IwfCallStQncConnectingPptp9600_Type = Counter32
_IwfCallStQncConnectingPptp9600_Object = MibTableColumn
iwfCallStQncConnectingPptp9600 = _IwfCallStQncConnectingPptp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 58),
    _IwfCallStQncConnectingPptp9600_Type()
)
iwfCallStQncConnectingPptp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingPptp9600.setStatus("mandatory")
_IwfCallStQncConnectingPpp9600_Type = Counter32
_IwfCallStQncConnectingPpp9600_Object = MibTableColumn
iwfCallStQncConnectingPpp9600 = _IwfCallStQncConnectingPpp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 59),
    _IwfCallStQncConnectingPpp9600_Type()
)
iwfCallStQncConnectingPpp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingPpp9600.setStatus("mandatory")
_IwfCallStQncDisconnectingSs9600_Type = Counter32
_IwfCallStQncDisconnectingSs9600_Object = MibTableColumn
iwfCallStQncDisconnectingSs9600 = _IwfCallStQncDisconnectingSs9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 60),
    _IwfCallStQncDisconnectingSs9600_Type()
)
iwfCallStQncDisconnectingSs9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDisconnectingSs9600.setStatus("mandatory")
_IwfCallStQncDisconnectingL2tp9600_Type = Counter32
_IwfCallStQncDisconnectingL2tp9600_Object = MibTableColumn
iwfCallStQncDisconnectingL2tp9600 = _IwfCallStQncDisconnectingL2tp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 61),
    _IwfCallStQncDisconnectingL2tp9600_Type()
)
iwfCallStQncDisconnectingL2tp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDisconnectingL2tp9600.setStatus("mandatory")
_IwfCallStQncDisconnectingPptp9600_Type = Counter32
_IwfCallStQncDisconnectingPptp9600_Object = MibTableColumn
iwfCallStQncDisconnectingPptp9600 = _IwfCallStQncDisconnectingPptp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 62),
    _IwfCallStQncDisconnectingPptp9600_Type()
)
iwfCallStQncDisconnectingPptp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDisconnectingPptp9600.setStatus("mandatory")
_IwfCallStQncDisconnectingPpp9600_Type = Counter32
_IwfCallStQncDisconnectingPpp9600_Object = MibTableColumn
iwfCallStQncDisconnectingPpp9600 = _IwfCallStQncDisconnectingPpp9600_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 63),
    _IwfCallStQncDisconnectingPpp9600_Type()
)
iwfCallStQncDisconnectingPpp9600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDisconnectingPpp9600.setStatus("mandatory")
_IwfCallStQncConnectedSs14400_Type = Counter32
_IwfCallStQncConnectedSs14400_Object = MibTableColumn
iwfCallStQncConnectedSs14400 = _IwfCallStQncConnectedSs14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 64),
    _IwfCallStQncConnectedSs14400_Type()
)
iwfCallStQncConnectedSs14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedSs14400.setStatus("mandatory")
_IwfCallStQncConnectedL2tp14400_Type = Counter32
_IwfCallStQncConnectedL2tp14400_Object = MibTableColumn
iwfCallStQncConnectedL2tp14400 = _IwfCallStQncConnectedL2tp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 65),
    _IwfCallStQncConnectedL2tp14400_Type()
)
iwfCallStQncConnectedL2tp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedL2tp14400.setStatus("mandatory")
_IwfCallStQncConnectedPptp14400_Type = Counter32
_IwfCallStQncConnectedPptp14400_Object = MibTableColumn
iwfCallStQncConnectedPptp14400 = _IwfCallStQncConnectedPptp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 66),
    _IwfCallStQncConnectedPptp14400_Type()
)
iwfCallStQncConnectedPptp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedPptp14400.setStatus("mandatory")
_IwfCallStQncConnectedPpp14400_Type = Counter32
_IwfCallStQncConnectedPpp14400_Object = MibTableColumn
iwfCallStQncConnectedPpp14400 = _IwfCallStQncConnectedPpp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 67),
    _IwfCallStQncConnectedPpp14400_Type()
)
iwfCallStQncConnectedPpp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectedPpp14400.setStatus("mandatory")
_IwfCallStQncTerminatedSs14400_Type = Counter32
_IwfCallStQncTerminatedSs14400_Object = MibTableColumn
iwfCallStQncTerminatedSs14400 = _IwfCallStQncTerminatedSs14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 68),
    _IwfCallStQncTerminatedSs14400_Type()
)
iwfCallStQncTerminatedSs14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedSs14400.setStatus("mandatory")
_IwfCallStQncTerminatedL2tp14400_Type = Counter32
_IwfCallStQncTerminatedL2tp14400_Object = MibTableColumn
iwfCallStQncTerminatedL2tp14400 = _IwfCallStQncTerminatedL2tp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 69),
    _IwfCallStQncTerminatedL2tp14400_Type()
)
iwfCallStQncTerminatedL2tp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedL2tp14400.setStatus("mandatory")
_IwfCallStQncTerminatedPptp14400_Type = Counter32
_IwfCallStQncTerminatedPptp14400_Object = MibTableColumn
iwfCallStQncTerminatedPptp14400 = _IwfCallStQncTerminatedPptp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 70),
    _IwfCallStQncTerminatedPptp14400_Type()
)
iwfCallStQncTerminatedPptp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedPptp14400.setStatus("mandatory")
_IwfCallStQncTerminatedPpp14400_Type = Counter32
_IwfCallStQncTerminatedPpp14400_Object = MibTableColumn
iwfCallStQncTerminatedPpp14400 = _IwfCallStQncTerminatedPpp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 71),
    _IwfCallStQncTerminatedPpp14400_Type()
)
iwfCallStQncTerminatedPpp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncTerminatedPpp14400.setStatus("mandatory")
_IwfCallStQncConnectingSs14400_Type = Counter32
_IwfCallStQncConnectingSs14400_Object = MibTableColumn
iwfCallStQncConnectingSs14400 = _IwfCallStQncConnectingSs14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 72),
    _IwfCallStQncConnectingSs14400_Type()
)
iwfCallStQncConnectingSs14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingSs14400.setStatus("mandatory")
_IwfCallStQncConnectingL2tp14400_Type = Counter32
_IwfCallStQncConnectingL2tp14400_Object = MibTableColumn
iwfCallStQncConnectingL2tp14400 = _IwfCallStQncConnectingL2tp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 73),
    _IwfCallStQncConnectingL2tp14400_Type()
)
iwfCallStQncConnectingL2tp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingL2tp14400.setStatus("mandatory")
_IwfCallStQncConnectingPptp14400_Type = Counter32
_IwfCallStQncConnectingPptp14400_Object = MibTableColumn
iwfCallStQncConnectingPptp14400 = _IwfCallStQncConnectingPptp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 74),
    _IwfCallStQncConnectingPptp14400_Type()
)
iwfCallStQncConnectingPptp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingPptp14400.setStatus("mandatory")
_IwfCallStQncConnectingPpp14400_Type = Counter32
_IwfCallStQncConnectingPpp14400_Object = MibTableColumn
iwfCallStQncConnectingPpp14400 = _IwfCallStQncConnectingPpp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 75),
    _IwfCallStQncConnectingPpp14400_Type()
)
iwfCallStQncConnectingPpp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncConnectingPpp14400.setStatus("mandatory")
_IwfCallStQncDiscconnectingSs14400_Type = Counter32
_IwfCallStQncDiscconnectingSs14400_Object = MibTableColumn
iwfCallStQncDiscconnectingSs14400 = _IwfCallStQncDiscconnectingSs14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 76),
    _IwfCallStQncDiscconnectingSs14400_Type()
)
iwfCallStQncDiscconnectingSs14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDiscconnectingSs14400.setStatus("mandatory")
_IwfCallStQncDiscconnectingL2tp14400_Type = Counter32
_IwfCallStQncDiscconnectingL2tp14400_Object = MibTableColumn
iwfCallStQncDiscconnectingL2tp14400 = _IwfCallStQncDiscconnectingL2tp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 77),
    _IwfCallStQncDiscconnectingL2tp14400_Type()
)
iwfCallStQncDiscconnectingL2tp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDiscconnectingL2tp14400.setStatus("mandatory")
_IwfCallStQncDiscconnectingPptp14400_Type = Counter32
_IwfCallStQncDiscconnectingPptp14400_Object = MibTableColumn
iwfCallStQncDiscconnectingPptp14400 = _IwfCallStQncDiscconnectingPptp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 78),
    _IwfCallStQncDiscconnectingPptp14400_Type()
)
iwfCallStQncDiscconnectingPptp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDiscconnectingPptp14400.setStatus("mandatory")
_IwfCallStQncDiscconnectingPpp14400_Type = Counter32
_IwfCallStQncDiscconnectingPpp14400_Object = MibTableColumn
iwfCallStQncDiscconnectingPpp14400 = _IwfCallStQncDiscconnectingPpp14400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 19, 1, 1, 79),
    _IwfCallStQncDiscconnectingPpp14400_Type()
)
iwfCallStQncDiscconnectingPpp14400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCallStQncDiscconnectingPpp14400.setStatus("mandatory")
_IwfCfgTdmTrap_ObjectIdentity = ObjectIdentity
iwfCfgTdmTrap = _IwfCfgTdmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20)
)
_IwfCfgTdmTrapTable_Object = MibTable
iwfCfgTdmTrapTable = _IwfCfgTdmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1)
)
if mibBuilder.loadTexts:
    iwfCfgTdmTrapTable.setStatus("mandatory")
_IwfCfgTdmTrapEntry_Object = MibTableRow
iwfCfgTdmTrapEntry = _IwfCfgTdmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1)
)
iwfCfgTdmTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfTdmTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgTdmTrapEntry.setStatus("mandatory")
_IwfTdmTrIndex_Type = Integer32
_IwfTdmTrIndex_Object = MibTableColumn
iwfTdmTrIndex = _IwfTdmTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 1),
    _IwfTdmTrIndex_Type()
)
iwfTdmTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrIndex.setStatus("mandatory")


class _IwfTdmTrChanMrgOperStatus_Type(Integer32):
    """Custom type iwfTdmTrChanMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmTrChanMrgOperStatus_Type.__name__ = "Integer32"
_IwfTdmTrChanMrgOperStatus_Object = MibTableColumn
iwfTdmTrChanMrgOperStatus = _IwfTdmTrChanMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 2),
    _IwfTdmTrChanMrgOperStatus_Type()
)
iwfTdmTrChanMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanMrgOperStatus.setStatus("mandatory")


class _IwfTdmTrChanNonOperStatus_Type(Integer32):
    """Custom type iwfTdmTrChanNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmTrChanNonOperStatus_Type.__name__ = "Integer32"
_IwfTdmTrChanNonOperStatus_Object = MibTableColumn
iwfTdmTrChanNonOperStatus = _IwfTdmTrChanNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 3),
    _IwfTdmTrChanNonOperStatus_Type()
)
iwfTdmTrChanNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanNonOperStatus.setStatus("mandatory")


class _IwfTdmTrChanClearStatus_Type(Integer32):
    """Custom type iwfTdmTrChanClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmTrChanClearStatus_Type.__name__ = "Integer32"
_IwfTdmTrChanClearStatus_Object = MibTableColumn
iwfTdmTrChanClearStatus = _IwfTdmTrChanClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 4),
    _IwfTdmTrChanClearStatus_Type()
)
iwfTdmTrChanClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanClearStatus.setStatus("mandatory")
_IwfTdmTrChanMrgOperBitMask_Type = Integer32
_IwfTdmTrChanMrgOperBitMask_Object = MibTableColumn
iwfTdmTrChanMrgOperBitMask = _IwfTdmTrChanMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 5),
    _IwfTdmTrChanMrgOperBitMask_Type()
)
iwfTdmTrChanMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanMrgOperBitMask.setStatus("mandatory")
_IwfTdmTrChanMrgOperThreshCnt_Type = Integer32
_IwfTdmTrChanMrgOperThreshCnt_Object = MibTableColumn
iwfTdmTrChanMrgOperThreshCnt = _IwfTdmTrChanMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 6),
    _IwfTdmTrChanMrgOperThreshCnt_Type()
)
iwfTdmTrChanMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanMrgOperThreshCnt.setStatus("mandatory")
_IwfTdmTrChanNonOperThreshCnt_Type = Integer32
_IwfTdmTrChanNonOperThreshCnt_Object = MibTableColumn
iwfTdmTrChanNonOperThreshCnt = _IwfTdmTrChanNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 7),
    _IwfTdmTrChanNonOperThreshCnt_Type()
)
iwfTdmTrChanNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanNonOperThreshCnt.setStatus("mandatory")
_IwfTdmTrChanClearThreshCnt_Type = Integer32
_IwfTdmTrChanClearThreshCnt_Object = MibTableColumn
iwfTdmTrChanClearThreshCnt = _IwfTdmTrChanClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 8),
    _IwfTdmTrChanClearThreshCnt_Type()
)
iwfTdmTrChanClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanClearThreshCnt.setStatus("mandatory")
_IwfTdmTrChanMrgOperThreshTime_Type = Integer32
_IwfTdmTrChanMrgOperThreshTime_Object = MibTableColumn
iwfTdmTrChanMrgOperThreshTime = _IwfTdmTrChanMrgOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 9),
    _IwfTdmTrChanMrgOperThreshTime_Type()
)
iwfTdmTrChanMrgOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanMrgOperThreshTime.setStatus("mandatory")
_IwfTdmTrChanNonOperThreshTime_Type = Integer32
_IwfTdmTrChanNonOperThreshTime_Object = MibTableColumn
iwfTdmTrChanNonOperThreshTime = _IwfTdmTrChanNonOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 10),
    _IwfTdmTrChanNonOperThreshTime_Type()
)
iwfTdmTrChanNonOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanNonOperThreshTime.setStatus("mandatory")
_IwfTdmTrChanClearThreshTime_Type = Integer32
_IwfTdmTrChanClearThreshTime_Object = MibTableColumn
iwfTdmTrChanClearThreshTime = _IwfTdmTrChanClearThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 11),
    _IwfTdmTrChanClearThreshTime_Type()
)
iwfTdmTrChanClearThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmTrChanClearThreshTime.setStatus("mandatory")
_IwfTdmTrChCrcErrCnt_Type = Integer32
_IwfTdmTrChCrcErrCnt_Object = MibTableColumn
iwfTdmTrChCrcErrCnt = _IwfTdmTrChCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 12),
    _IwfTdmTrChCrcErrCnt_Type()
)
iwfTdmTrChCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrChCrcErrCnt.setStatus("mandatory")
_IwfTdmTrChAbortErrCnt_Type = Integer32
_IwfTdmTrChAbortErrCnt_Object = MibTableColumn
iwfTdmTrChAbortErrCnt = _IwfTdmTrChAbortErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 13),
    _IwfTdmTrChAbortErrCnt_Type()
)
iwfTdmTrChAbortErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrChAbortErrCnt.setStatus("mandatory")
_IwfTdmTrChFrameOverflowCnt_Type = Integer32
_IwfTdmTrChFrameOverflowCnt_Object = MibTableColumn
iwfTdmTrChFrameOverflowCnt = _IwfTdmTrChFrameOverflowCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 14),
    _IwfTdmTrChFrameOverflowCnt_Type()
)
iwfTdmTrChFrameOverflowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrChFrameOverflowCnt.setStatus("mandatory")


class _IwfTdmTrStatus_Type(Integer32):
    """Custom type iwfTdmTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfTdmTrStatus_Type.__name__ = "Integer32"
_IwfTdmTrStatus_Object = MibTableColumn
iwfTdmTrStatus = _IwfTdmTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 15),
    _IwfTdmTrStatus_Type()
)
iwfTdmTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrStatus.setStatus("mandatory")
_IwfTdmTrTdmChannel_Type = Integer32
_IwfTdmTrTdmChannel_Object = MibTableColumn
iwfTdmTrTdmChannel = _IwfTdmTrTdmChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 16),
    _IwfTdmTrTdmChannel_Type()
)
iwfTdmTrTdmChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrTdmChannel.setStatus("mandatory")
_IwfTdmTrMunichChip_Type = Integer32
_IwfTdmTrMunichChip_Object = MibTableColumn
iwfTdmTrMunichChip = _IwfTdmTrMunichChip_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 17),
    _IwfTdmTrMunichChip_Type()
)
iwfTdmTrMunichChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrMunichChip.setStatus("mandatory")
_IwfTdmTrMunichChannel_Type = Integer32
_IwfTdmTrMunichChannel_Object = MibTableColumn
iwfTdmTrMunichChannel = _IwfTdmTrMunichChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 20, 1, 1, 18),
    _IwfTdmTrMunichChannel_Type()
)
iwfTdmTrMunichChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmTrMunichChannel.setStatus("mandatory")
_IwfCfgTdmSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgTdmSsTrap = _IwfCfgTdmSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21)
)
_IwfCfgTdmSsTrapTable_Object = MibTable
iwfCfgTdmSsTrapTable = _IwfCfgTdmSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1)
)
if mibBuilder.loadTexts:
    iwfCfgTdmSsTrapTable.setStatus("mandatory")
_IwfCfgTdmSsTrapEntry_Object = MibTableRow
iwfCfgTdmSsTrapEntry = _IwfCfgTdmSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1)
)
iwfCfgTdmSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgTdmSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgTdmSsTrapEntry.setStatus("mandatory")
_IwfCfgTdmSsTrIndex_Type = Integer32
_IwfCfgTdmSsTrIndex_Object = MibTableColumn
iwfCfgTdmSsTrIndex = _IwfCfgTdmSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 1),
    _IwfCfgTdmSsTrIndex_Type()
)
iwfCfgTdmSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgTdmSsTrIndex.setStatus("mandatory")


class _IwfTdmSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfTdmSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfTdmSsTrMrgOperStatus_Object = MibTableColumn
iwfTdmSsTrMrgOperStatus = _IwfTdmSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 2),
    _IwfTdmSsTrMrgOperStatus_Type()
)
iwfTdmSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrMrgOperStatus.setStatus("mandatory")


class _IwfTdmSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfTdmSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfTdmSsTrNonOperStatus_Object = MibTableColumn
iwfTdmSsTrNonOperStatus = _IwfTdmSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 3),
    _IwfTdmSsTrNonOperStatus_Type()
)
iwfTdmSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrNonOperStatus.setStatus("mandatory")


class _IwfTdmSsTrClearStatus_Type(Integer32):
    """Custom type iwfTdmSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmSsTrClearStatus_Type.__name__ = "Integer32"
_IwfTdmSsTrClearStatus_Object = MibTableColumn
iwfTdmSsTrClearStatus = _IwfTdmSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 4),
    _IwfTdmSsTrClearStatus_Type()
)
iwfTdmSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrClearStatus.setStatus("mandatory")
_IwfTdmSsTrMrgOperThreshCnt_Type = Integer32
_IwfTdmSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfTdmSsTrMrgOperThreshCnt = _IwfTdmSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 5),
    _IwfTdmSsTrMrgOperThreshCnt_Type()
)
iwfTdmSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfTdmSsTrNonOperThreshCnt_Type = Integer32
_IwfTdmSsTrNonOperThreshCnt_Object = MibTableColumn
iwfTdmSsTrNonOperThreshCnt = _IwfTdmSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 6),
    _IwfTdmSsTrNonOperThreshCnt_Type()
)
iwfTdmSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfTdmSsTrClearThreshCnt_Type = Integer32
_IwfTdmSsTrClearThreshCnt_Object = MibTableColumn
iwfTdmSsTrClearThreshCnt = _IwfTdmSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 7),
    _IwfTdmSsTrClearThreshCnt_Type()
)
iwfTdmSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrClearThreshCnt.setStatus("mandatory")
_IwfTdmSsTrMrgOperThreshTime_Type = Integer32
_IwfTdmSsTrMrgOperThreshTime_Object = MibTableColumn
iwfTdmSsTrMrgOperThreshTime = _IwfTdmSsTrMrgOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 8),
    _IwfTdmSsTrMrgOperThreshTime_Type()
)
iwfTdmSsTrMrgOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrMrgOperThreshTime.setStatus("mandatory")
_IwfTdmSsTrNonOperThreshTime_Type = Integer32
_IwfTdmSsTrNonOperThreshTime_Object = MibTableColumn
iwfTdmSsTrNonOperThreshTime = _IwfTdmSsTrNonOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 9),
    _IwfTdmSsTrNonOperThreshTime_Type()
)
iwfTdmSsTrNonOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrNonOperThreshTime.setStatus("mandatory")
_IwfTdmSsTrClearThreshTime_Type = Integer32
_IwfTdmSsTrClearThreshTime_Object = MibTableColumn
iwfTdmSsTrClearThreshTime = _IwfTdmSsTrClearThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 10),
    _IwfTdmSsTrClearThreshTime_Type()
)
iwfTdmSsTrClearThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmSsTrClearThreshTime.setStatus("mandatory")


class _IwfTdmSsTrStatus_Type(Integer32):
    """Custom type iwfTdmSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfTdmSsTrStatus_Type.__name__ = "Integer32"
_IwfTdmSsTrStatus_Object = MibTableColumn
iwfTdmSsTrStatus = _IwfTdmSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 21, 1, 1, 11),
    _IwfTdmSsTrStatus_Type()
)
iwfTdmSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmSsTrStatus.setStatus("mandatory")
_IwfCfgPbTrap_ObjectIdentity = ObjectIdentity
iwfCfgPbTrap = _IwfCfgPbTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22)
)
_IwfCfgPbTrapTable_Object = MibTable
iwfCfgPbTrapTable = _IwfCfgPbTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1)
)
if mibBuilder.loadTexts:
    iwfCfgPbTrapTable.setStatus("mandatory")
_IwfCfgPbTrapEntry_Object = MibTableRow
iwfCfgPbTrapEntry = _IwfCfgPbTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1)
)
iwfCfgPbTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfPbTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgPbTrapEntry.setStatus("mandatory")
_IwfPbTrIndex_Type = Integer32
_IwfPbTrIndex_Object = MibTableColumn
iwfPbTrIndex = _IwfPbTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 1),
    _IwfPbTrIndex_Type()
)
iwfPbTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrIndex.setStatus("mandatory")


class _IwfPbTrChanMrgOperStatus_Type(Integer32):
    """Custom type iwfPbTrChanMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbTrChanMrgOperStatus_Type.__name__ = "Integer32"
_IwfPbTrChanMrgOperStatus_Object = MibTableColumn
iwfPbTrChanMrgOperStatus = _IwfPbTrChanMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 2),
    _IwfPbTrChanMrgOperStatus_Type()
)
iwfPbTrChanMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanMrgOperStatus.setStatus("mandatory")


class _IwfPbTrChanNonOperStatus_Type(Integer32):
    """Custom type iwfPbTrChanNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbTrChanNonOperStatus_Type.__name__ = "Integer32"
_IwfPbTrChanNonOperStatus_Object = MibTableColumn
iwfPbTrChanNonOperStatus = _IwfPbTrChanNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 3),
    _IwfPbTrChanNonOperStatus_Type()
)
iwfPbTrChanNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanNonOperStatus.setStatus("mandatory")


class _IwfPbTrChanClearStatus_Type(Integer32):
    """Custom type iwfPbTrChanClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbTrChanClearStatus_Type.__name__ = "Integer32"
_IwfPbTrChanClearStatus_Object = MibTableColumn
iwfPbTrChanClearStatus = _IwfPbTrChanClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 4),
    _IwfPbTrChanClearStatus_Type()
)
iwfPbTrChanClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanClearStatus.setStatus("mandatory")
_IwfPbTrChanMrgOperBitMask_Type = Integer32
_IwfPbTrChanMrgOperBitMask_Object = MibTableColumn
iwfPbTrChanMrgOperBitMask = _IwfPbTrChanMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 5),
    _IwfPbTrChanMrgOperBitMask_Type()
)
iwfPbTrChanMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanMrgOperBitMask.setStatus("mandatory")
_IwfPbTrChanMrgOperThreshCnt_Type = Integer32
_IwfPbTrChanMrgOperThreshCnt_Object = MibTableColumn
iwfPbTrChanMrgOperThreshCnt = _IwfPbTrChanMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 6),
    _IwfPbTrChanMrgOperThreshCnt_Type()
)
iwfPbTrChanMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanMrgOperThreshCnt.setStatus("mandatory")
_IwfPbTrChanNonOperThreshCnt_Type = Integer32
_IwfPbTrChanNonOperThreshCnt_Object = MibTableColumn
iwfPbTrChanNonOperThreshCnt = _IwfPbTrChanNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 7),
    _IwfPbTrChanNonOperThreshCnt_Type()
)
iwfPbTrChanNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanNonOperThreshCnt.setStatus("mandatory")
_IwfPbTrChanClearThreshCnt_Type = Integer32
_IwfPbTrChanClearThreshCnt_Object = MibTableColumn
iwfPbTrChanClearThreshCnt = _IwfPbTrChanClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 8),
    _IwfPbTrChanClearThreshCnt_Type()
)
iwfPbTrChanClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanClearThreshCnt.setStatus("mandatory")
_IwfPbTrChanMrgOperThreshTime_Type = Integer32
_IwfPbTrChanMrgOperThreshTime_Object = MibTableColumn
iwfPbTrChanMrgOperThreshTime = _IwfPbTrChanMrgOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 9),
    _IwfPbTrChanMrgOperThreshTime_Type()
)
iwfPbTrChanMrgOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanMrgOperThreshTime.setStatus("mandatory")
_IwfPbTrChanNonOperThreshTime_Type = Integer32
_IwfPbTrChanNonOperThreshTime_Object = MibTableColumn
iwfPbTrChanNonOperThreshTime = _IwfPbTrChanNonOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 10),
    _IwfPbTrChanNonOperThreshTime_Type()
)
iwfPbTrChanNonOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanNonOperThreshTime.setStatus("mandatory")
_IwfPbTrChanClearThreshTime_Type = Integer32
_IwfPbTrChanClearThreshTime_Object = MibTableColumn
iwfPbTrChanClearThreshTime = _IwfPbTrChanClearThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 11),
    _IwfPbTrChanClearThreshTime_Type()
)
iwfPbTrChanClearThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbTrChanClearThreshTime.setStatus("mandatory")
_IwfPbTrChCrcErrCnt_Type = Integer32
_IwfPbTrChCrcErrCnt_Object = MibTableColumn
iwfPbTrChCrcErrCnt = _IwfPbTrChCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 12),
    _IwfPbTrChCrcErrCnt_Type()
)
iwfPbTrChCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrChCrcErrCnt.setStatus("mandatory")
_IwfPbTrChAbortErrCnt_Type = Integer32
_IwfPbTrChAbortErrCnt_Object = MibTableColumn
iwfPbTrChAbortErrCnt = _IwfPbTrChAbortErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 13),
    _IwfPbTrChAbortErrCnt_Type()
)
iwfPbTrChAbortErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrChAbortErrCnt.setStatus("mandatory")
_IwfPbTrChFrameOverflowCnt_Type = Integer32
_IwfPbTrChFrameOverflowCnt_Object = MibTableColumn
iwfPbTrChFrameOverflowCnt = _IwfPbTrChFrameOverflowCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 14),
    _IwfPbTrChFrameOverflowCnt_Type()
)
iwfPbTrChFrameOverflowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrChFrameOverflowCnt.setStatus("mandatory")


class _IwfPbTrChStatus_Type(Integer32):
    """Custom type iwfPbTrChStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfPbTrChStatus_Type.__name__ = "Integer32"
_IwfPbTrChStatus_Object = MibTableColumn
iwfPbTrChStatus = _IwfPbTrChStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 15),
    _IwfPbTrChStatus_Type()
)
iwfPbTrChStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrChStatus.setStatus("mandatory")
_IwfPbTrModemSlot_Type = Integer32
_IwfPbTrModemSlot_Object = MibTableColumn
iwfPbTrModemSlot = _IwfPbTrModemSlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 16),
    _IwfPbTrModemSlot_Type()
)
iwfPbTrModemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrModemSlot.setStatus("mandatory")
_IwfPbTrModemChannel_Type = Integer32
_IwfPbTrModemChannel_Object = MibTableColumn
iwfPbTrModemChannel = _IwfPbTrModemChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 22, 1, 1, 17),
    _IwfPbTrModemChannel_Type()
)
iwfPbTrModemChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbTrModemChannel.setStatus("mandatory")
_IwfCfgPbSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgPbSsTrap = _IwfCfgPbSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23)
)
_IwfCfgPbSsTrapTable_Object = MibTable
iwfCfgPbSsTrapTable = _IwfCfgPbSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1)
)
if mibBuilder.loadTexts:
    iwfCfgPbSsTrapTable.setStatus("mandatory")
_IwfCfgPbSsTrapEntry_Object = MibTableRow
iwfCfgPbSsTrapEntry = _IwfCfgPbSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1)
)
iwfCfgPbSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfPbSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgPbSsTrapEntry.setStatus("mandatory")
_IwfPbSsTrIndex_Type = Integer32
_IwfPbSsTrIndex_Object = MibTableColumn
iwfPbSsTrIndex = _IwfPbSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 1),
    _IwfPbSsTrIndex_Type()
)
iwfPbSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbSsTrIndex.setStatus("mandatory")


class _IwfPbSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfPbSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfPbSsTrMrgOperStatus_Object = MibTableColumn
iwfPbSsTrMrgOperStatus = _IwfPbSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 2),
    _IwfPbSsTrMrgOperStatus_Type()
)
iwfPbSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrMrgOperStatus.setStatus("mandatory")


class _IwfPbSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfPbSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfPbSsTrNonOperStatus_Object = MibTableColumn
iwfPbSsTrNonOperStatus = _IwfPbSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 3),
    _IwfPbSsTrNonOperStatus_Type()
)
iwfPbSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrNonOperStatus.setStatus("mandatory")


class _IwfPbSsTrClearStatus_Type(Integer32):
    """Custom type iwfPbSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbSsTrClearStatus_Type.__name__ = "Integer32"
_IwfPbSsTrClearStatus_Object = MibTableColumn
iwfPbSsTrClearStatus = _IwfPbSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 4),
    _IwfPbSsTrClearStatus_Type()
)
iwfPbSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrClearStatus.setStatus("mandatory")
_IwfPbSsTrMrgOperThreshCnt_Type = Integer32
_IwfPbSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfPbSsTrMrgOperThreshCnt = _IwfPbSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 5),
    _IwfPbSsTrMrgOperThreshCnt_Type()
)
iwfPbSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfPbSsTrNonOperThreshCnt_Type = Integer32
_IwfPbSsTrNonOperThreshCnt_Object = MibTableColumn
iwfPbSsTrNonOperThreshCnt = _IwfPbSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 6),
    _IwfPbSsTrNonOperThreshCnt_Type()
)
iwfPbSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfPbSsTrClearThreshCnt_Type = Integer32
_IwfPbSsTrClearThreshCnt_Object = MibTableColumn
iwfPbSsTrClearThreshCnt = _IwfPbSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 7),
    _IwfPbSsTrClearThreshCnt_Type()
)
iwfPbSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrClearThreshCnt.setStatus("mandatory")
_IwfPbSsTrMrgOperThreshTime_Type = Integer32
_IwfPbSsTrMrgOperThreshTime_Object = MibTableColumn
iwfPbSsTrMrgOperThreshTime = _IwfPbSsTrMrgOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 8),
    _IwfPbSsTrMrgOperThreshTime_Type()
)
iwfPbSsTrMrgOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrMrgOperThreshTime.setStatus("mandatory")
_IwfPbSsTrNonOperThreshTime_Type = Integer32
_IwfPbSsTrNonOperThreshTime_Object = MibTableColumn
iwfPbSsTrNonOperThreshTime = _IwfPbSsTrNonOperThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 9),
    _IwfPbSsTrNonOperThreshTime_Type()
)
iwfPbSsTrNonOperThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrNonOperThreshTime.setStatus("mandatory")
_IwfPbSsTrClearThreshtime_Type = Integer32
_IwfPbSsTrClearThreshtime_Object = MibTableColumn
iwfPbSsTrClearThreshtime = _IwfPbSsTrClearThreshtime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 10),
    _IwfPbSsTrClearThreshtime_Type()
)
iwfPbSsTrClearThreshtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbSsTrClearThreshtime.setStatus("mandatory")


class _IwfPbSsTrStatus_Type(Integer32):
    """Custom type iwfPbSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfPbSsTrStatus_Type.__name__ = "Integer32"
_IwfPbSsTrStatus_Object = MibTableColumn
iwfPbSsTrStatus = _IwfPbSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 23, 1, 1, 11),
    _IwfPbSsTrStatus_Type()
)
iwfPbSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbSsTrStatus.setStatus("mandatory")
_IwfCfgPbClkTrap_ObjectIdentity = ObjectIdentity
iwfCfgPbClkTrap = _IwfCfgPbClkTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24)
)
_IwfCfgPbClkTrapTable_Object = MibTable
iwfCfgPbClkTrapTable = _IwfCfgPbClkTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24, 1)
)
if mibBuilder.loadTexts:
    iwfCfgPbClkTrapTable.setStatus("mandatory")
_IwfCfgPbClkTrapEntry_Object = MibTableRow
iwfCfgPbClkTrapEntry = _IwfCfgPbClkTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24, 1, 1)
)
iwfCfgPbClkTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfPbClkTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgPbClkTrapEntry.setStatus("mandatory")
_IwfPbClkTrIndex_Type = Integer32
_IwfPbClkTrIndex_Object = MibTableColumn
iwfPbClkTrIndex = _IwfPbClkTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24, 1, 1, 1),
    _IwfPbClkTrIndex_Type()
)
iwfPbClkTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPbClkTrIndex.setStatus("mandatory")


class _IwfPbClkTrNonOperStatus_Type(Integer32):
    """Custom type iwfPbClkTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbClkTrNonOperStatus_Type.__name__ = "Integer32"
_IwfPbClkTrNonOperStatus_Object = MibTableColumn
iwfPbClkTrNonOperStatus = _IwfPbClkTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24, 1, 1, 2),
    _IwfPbClkTrNonOperStatus_Type()
)
iwfPbClkTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbClkTrNonOperStatus.setStatus("mandatory")


class _IwfPbClkTrClearStatus_Type(Integer32):
    """Custom type iwfPbClkTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPbClkTrClearStatus_Type.__name__ = "Integer32"
_IwfPbClkTrClearStatus_Object = MibTableColumn
iwfPbClkTrClearStatus = _IwfPbClkTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24, 1, 1, 3),
    _IwfPbClkTrClearStatus_Type()
)
iwfPbClkTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbClkTrClearStatus.setStatus("mandatory")
_IwfPbClkTrNonOperThreshTimer_Type = Integer32
_IwfPbClkTrNonOperThreshTimer_Object = MibTableColumn
iwfPbClkTrNonOperThreshTimer = _IwfPbClkTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 24, 1, 1, 4),
    _IwfPbClkTrNonOperThreshTimer_Type()
)
iwfPbClkTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPbClkTrNonOperThreshTimer.setStatus("mandatory")
_IwfCfgTdmClkTrap_ObjectIdentity = ObjectIdentity
iwfCfgTdmClkTrap = _IwfCfgTdmClkTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25)
)
_IwfCfgTdmClkTrapTable_Object = MibTable
iwfCfgTdmClkTrapTable = _IwfCfgTdmClkTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25, 1)
)
if mibBuilder.loadTexts:
    iwfCfgTdmClkTrapTable.setStatus("mandatory")
_IwfCfgTdmClkTrapEntry_Object = MibTableRow
iwfCfgTdmClkTrapEntry = _IwfCfgTdmClkTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25, 1, 1)
)
iwfCfgTdmClkTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfTdmClkTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgTdmClkTrapEntry.setStatus("mandatory")
_IwfTdmClkTrIndex_Type = Integer32
_IwfTdmClkTrIndex_Object = MibTableColumn
iwfTdmClkTrIndex = _IwfTdmClkTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25, 1, 1, 1),
    _IwfTdmClkTrIndex_Type()
)
iwfTdmClkTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTdmClkTrIndex.setStatus("mandatory")


class _IwfTdmClkTrNonOperStatus_Type(Integer32):
    """Custom type iwfTdmClkTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmClkTrNonOperStatus_Type.__name__ = "Integer32"
_IwfTdmClkTrNonOperStatus_Object = MibTableColumn
iwfTdmClkTrNonOperStatus = _IwfTdmClkTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25, 1, 1, 2),
    _IwfTdmClkTrNonOperStatus_Type()
)
iwfTdmClkTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmClkTrNonOperStatus.setStatus("mandatory")


class _IwfTdmClkTrClearStatus_Type(Integer32):
    """Custom type iwfTdmClkTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTdmClkTrClearStatus_Type.__name__ = "Integer32"
_IwfTdmClkTrClearStatus_Object = MibTableColumn
iwfTdmClkTrClearStatus = _IwfTdmClkTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25, 1, 1, 3),
    _IwfTdmClkTrClearStatus_Type()
)
iwfTdmClkTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmClkTrClearStatus.setStatus("mandatory")
_IwfTdmClkTrNonOperThreshTimer_Type = Integer32
_IwfTdmClkTrNonOperThreshTimer_Object = MibTableColumn
iwfTdmClkTrNonOperThreshTimer = _IwfTdmClkTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 25, 1, 1, 4),
    _IwfTdmClkTrNonOperThreshTimer_Type()
)
iwfTdmClkTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTdmClkTrNonOperThreshTimer.setStatus("mandatory")
_IwfCfgCcSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgCcSsTrap = _IwfCfgCcSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26)
)
_IwfCfgCcSsTrapTable_Object = MibTable
iwfCfgCcSsTrapTable = _IwfCfgCcSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1)
)
if mibBuilder.loadTexts:
    iwfCfgCcSsTrapTable.setStatus("mandatory")
_IwfCfgCcSsTrapEntry_Object = MibTableRow
iwfCfgCcSsTrapEntry = _IwfCfgCcSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1)
)
iwfCfgCcSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCcSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgCcSsTrapEntry.setStatus("mandatory")
_IwfCcSsTrIndex_Type = Integer32
_IwfCcSsTrIndex_Object = MibTableColumn
iwfCcSsTrIndex = _IwfCcSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 1),
    _IwfCcSsTrIndex_Type()
)
iwfCcSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrIndex.setStatus("mandatory")


class _IwfCcSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfCcSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfCcSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfCcSsTrMrgOperStatus_Object = MibTableColumn
iwfCcSsTrMrgOperStatus = _IwfCcSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 2),
    _IwfCcSsTrMrgOperStatus_Type()
)
iwfCcSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrMrgOperStatus.setStatus("mandatory")


class _IwfCcSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfCcSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfCcSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfCcSsTrNonOperStatus_Object = MibTableColumn
iwfCcSsTrNonOperStatus = _IwfCcSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 3),
    _IwfCcSsTrNonOperStatus_Type()
)
iwfCcSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrNonOperStatus.setStatus("mandatory")


class _IwfCcSsTrClearStatus_Type(Integer32):
    """Custom type iwfCcSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfCcSsTrClearStatus_Type.__name__ = "Integer32"
_IwfCcSsTrClearStatus_Object = MibTableColumn
iwfCcSsTrClearStatus = _IwfCcSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 4),
    _IwfCcSsTrClearStatus_Type()
)
iwfCcSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrClearStatus.setStatus("mandatory")
_IwfCcSsTrMrgOperBitMask_Type = Integer32
_IwfCcSsTrMrgOperBitMask_Object = MibTableColumn
iwfCcSsTrMrgOperBitMask = _IwfCcSsTrMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 5),
    _IwfCcSsTrMrgOperBitMask_Type()
)
iwfCcSsTrMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrMrgOperBitMask.setStatus("mandatory")
_IwfCcSsTrMrgOperThreshCnt_Type = Integer32
_IwfCcSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfCcSsTrMrgOperThreshCnt = _IwfCcSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 6),
    _IwfCcSsTrMrgOperThreshCnt_Type()
)
iwfCcSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfCcSsTrNonOperThreshCnt_Type = Integer32
_IwfCcSsTrNonOperThreshCnt_Object = MibTableColumn
iwfCcSsTrNonOperThreshCnt = _IwfCcSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 7),
    _IwfCcSsTrNonOperThreshCnt_Type()
)
iwfCcSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfCcSsTrClearThreshCnt_Type = Integer32
_IwfCcSsTrClearThreshCnt_Object = MibTableColumn
iwfCcSsTrClearThreshCnt = _IwfCcSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 8),
    _IwfCcSsTrClearThreshCnt_Type()
)
iwfCcSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrClearThreshCnt.setStatus("mandatory")
_IwfCcSsTrMrgOperThreshTimer_Type = Integer32
_IwfCcSsTrMrgOperThreshTimer_Object = MibTableColumn
iwfCcSsTrMrgOperThreshTimer = _IwfCcSsTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 9),
    _IwfCcSsTrMrgOperThreshTimer_Type()
)
iwfCcSsTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrMrgOperThreshTimer.setStatus("mandatory")
_IwfCcSsTrNonOperThreshTimer_Type = Integer32
_IwfCcSsTrNonOperThreshTimer_Object = MibTableColumn
iwfCcSsTrNonOperThreshTimer = _IwfCcSsTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 10),
    _IwfCcSsTrNonOperThreshTimer_Type()
)
iwfCcSsTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrNonOperThreshTimer.setStatus("mandatory")
_IwfCcSsTrClearThreshTimer_Type = Integer32
_IwfCcSsTrClearThreshTimer_Object = MibTableColumn
iwfCcSsTrClearThreshTimer = _IwfCcSsTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 11),
    _IwfCcSsTrClearThreshTimer_Type()
)
iwfCcSsTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCcSsTrClearThreshTimer.setStatus("mandatory")
_IwfCcSsTrAd9600NoSysResCnt_Type = Integer32
_IwfCcSsTrAd9600NoSysResCnt_Object = MibTableColumn
iwfCcSsTrAd9600NoSysResCnt = _IwfCcSsTrAd9600NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 12),
    _IwfCcSsTrAd9600NoSysResCnt_Type()
)
iwfCcSsTrAd9600NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd9600NoSysResCnt.setStatus("mandatory")
_IwfCcSsTrAd14400NoSysResCnt_Type = Integer32
_IwfCcSsTrAd14400NoSysResCnt_Object = MibTableColumn
iwfCcSsTrAd14400NoSysResCnt = _IwfCcSsTrAd14400NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 13),
    _IwfCcSsTrAd14400NoSysResCnt_Type()
)
iwfCcSsTrAd14400NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd14400NoSysResCnt.setStatus("mandatory")
_IwfCcSsTrFax9600NoSysResCnt_Type = Integer32
_IwfCcSsTrFax9600NoSysResCnt_Object = MibTableColumn
iwfCcSsTrFax9600NoSysResCnt = _IwfCcSsTrFax9600NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 14),
    _IwfCcSsTrFax9600NoSysResCnt_Type()
)
iwfCcSsTrFax9600NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax9600NoSysResCnt.setStatus("mandatory")
_IwfCcSsTrFax14400NoSysResCnt_Type = Integer32
_IwfCcSsTrFax14400NoSysResCnt_Object = MibTableColumn
iwfCcSsTrFax14400NoSysResCnt = _IwfCcSsTrFax14400NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 15),
    _IwfCcSsTrFax14400NoSysResCnt_Type()
)
iwfCcSsTrFax14400NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax14400NoSysResCnt.setStatus("mandatory")
_IwfCcSsTrAd9600SktErrCnt_Type = Integer32
_IwfCcSsTrAd9600SktErrCnt_Object = MibTableColumn
iwfCcSsTrAd9600SktErrCnt = _IwfCcSsTrAd9600SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 16),
    _IwfCcSsTrAd9600SktErrCnt_Type()
)
iwfCcSsTrAd9600SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd9600SktErrCnt.setStatus("mandatory")
_IwfCcSsTrAd14400SktErrCnt_Type = Integer32
_IwfCcSsTrAd14400SktErrCnt_Object = MibTableColumn
iwfCcSsTrAd14400SktErrCnt = _IwfCcSsTrAd14400SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 17),
    _IwfCcSsTrAd14400SktErrCnt_Type()
)
iwfCcSsTrAd14400SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd14400SktErrCnt.setStatus("mandatory")
_IwfCcSsTrFax9600SktErrCnt_Type = Integer32
_IwfCcSsTrFax9600SktErrCnt_Object = MibTableColumn
iwfCcSsTrFax9600SktErrCnt = _IwfCcSsTrFax9600SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 18),
    _IwfCcSsTrFax9600SktErrCnt_Type()
)
iwfCcSsTrFax9600SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax9600SktErrCnt.setStatus("mandatory")
_IwfCcSsTrFax14400SktErrCnt_Type = Integer32
_IwfCcSsTrFax14400SktErrCnt_Object = MibTableColumn
iwfCcSsTrFax14400SktErrCnt = _IwfCcSsTrFax14400SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 19),
    _IwfCcSsTrFax14400SktErrCnt_Type()
)
iwfCcSsTrFax14400SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax14400SktErrCnt.setStatus("mandatory")
_IwfCcSsTrAd9600PrtErrCnt_Type = Integer32
_IwfCcSsTrAd9600PrtErrCnt_Object = MibTableColumn
iwfCcSsTrAd9600PrtErrCnt = _IwfCcSsTrAd9600PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 20),
    _IwfCcSsTrAd9600PrtErrCnt_Type()
)
iwfCcSsTrAd9600PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd9600PrtErrCnt.setStatus("mandatory")
_IwfCcSsTrAd14400PrtErrCnt_Type = Integer32
_IwfCcSsTrAd14400PrtErrCnt_Object = MibTableColumn
iwfCcSsTrAd14400PrtErrCnt = _IwfCcSsTrAd14400PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 21),
    _IwfCcSsTrAd14400PrtErrCnt_Type()
)
iwfCcSsTrAd14400PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd14400PrtErrCnt.setStatus("mandatory")
_IwfCcSsTrFax9600PrtErrCnt_Type = Integer32
_IwfCcSsTrFax9600PrtErrCnt_Object = MibTableColumn
iwfCcSsTrFax9600PrtErrCnt = _IwfCcSsTrFax9600PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 22),
    _IwfCcSsTrFax9600PrtErrCnt_Type()
)
iwfCcSsTrFax9600PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax9600PrtErrCnt.setStatus("mandatory")
_IwfCcSsTrFax14400PrtErrCnt_Type = Integer32
_IwfCcSsTrFax14400PrtErrCnt_Object = MibTableColumn
iwfCcSsTrFax14400PrtErrCnt = _IwfCcSsTrFax14400PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 23),
    _IwfCcSsTrFax14400PrtErrCnt_Type()
)
iwfCcSsTrFax14400PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax14400PrtErrCnt.setStatus("mandatory")
_IwfCcSsTrAd9600NoMdmResCnt_Type = Integer32
_IwfCcSsTrAd9600NoMdmResCnt_Object = MibTableColumn
iwfCcSsTrAd9600NoMdmResCnt = _IwfCcSsTrAd9600NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 24),
    _IwfCcSsTrAd9600NoMdmResCnt_Type()
)
iwfCcSsTrAd9600NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd9600NoMdmResCnt.setStatus("mandatory")
_IwfCcSsTrAd14400NoMdmResCnt_Type = Integer32
_IwfCcSsTrAd14400NoMdmResCnt_Object = MibTableColumn
iwfCcSsTrAd14400NoMdmResCnt = _IwfCcSsTrAd14400NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 25),
    _IwfCcSsTrAd14400NoMdmResCnt_Type()
)
iwfCcSsTrAd14400NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrAd14400NoMdmResCnt.setStatus("mandatory")
_IwfCcSsTrFax9600NoMdmResCnt_Type = Integer32
_IwfCcSsTrFax9600NoMdmResCnt_Object = MibTableColumn
iwfCcSsTrFax9600NoMdmResCnt = _IwfCcSsTrFax9600NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 26),
    _IwfCcSsTrFax9600NoMdmResCnt_Type()
)
iwfCcSsTrFax9600NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax9600NoMdmResCnt.setStatus("mandatory")
_IwfCcSsTrFax14400NoMdmResCnt_Type = Integer32
_IwfCcSsTrFax14400NoMdmResCnt_Object = MibTableColumn
iwfCcSsTrFax14400NoMdmResCnt = _IwfCcSsTrFax14400NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 27),
    _IwfCcSsTrFax14400NoMdmResCnt_Type()
)
iwfCcSsTrFax14400NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrFax14400NoMdmResCnt.setStatus("mandatory")
_IwfCcSsTrNoResponse_Type = Integer32
_IwfCcSsTrNoResponse_Object = MibTableColumn
iwfCcSsTrNoResponse = _IwfCcSsTrNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 28),
    _IwfCcSsTrNoResponse_Type()
)
iwfCcSsTrNoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrNoResponse.setStatus("mandatory")


class _IwfCcSsTrStatus_Type(Integer32):
    """Custom type iwfCcSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfCcSsTrStatus_Type.__name__ = "Integer32"
_IwfCcSsTrStatus_Object = MibTableColumn
iwfCcSsTrStatus = _IwfCcSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 26, 1, 1, 29),
    _IwfCcSsTrStatus_Type()
)
iwfCcSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCcSsTrStatus.setStatus("mandatory")
_IwfCfgDxSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgDxSsTrap = _IwfCfgDxSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27)
)
_IwfCfgDxSsTrapTable_Object = MibTable
iwfCfgDxSsTrapTable = _IwfCfgDxSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1)
)
if mibBuilder.loadTexts:
    iwfCfgDxSsTrapTable.setStatus("mandatory")
_IwfCfgDxSsTrapEntry_Object = MibTableRow
iwfCfgDxSsTrapEntry = _IwfCfgDxSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1)
)
iwfCfgDxSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfDxSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgDxSsTrapEntry.setStatus("mandatory")
_IwfDxSsTrIndex_Type = Integer32
_IwfDxSsTrIndex_Object = MibTableColumn
iwfDxSsTrIndex = _IwfDxSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 1),
    _IwfDxSsTrIndex_Type()
)
iwfDxSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrIndex.setStatus("mandatory")


class _IwfDxSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfDxSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfDxSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfDxSsTrMrgOperStatus_Object = MibTableColumn
iwfDxSsTrMrgOperStatus = _IwfDxSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 2),
    _IwfDxSsTrMrgOperStatus_Type()
)
iwfDxSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrMrgOperStatus.setStatus("mandatory")


class _IwfDxSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfDxSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfDxSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfDxSsTrNonOperStatus_Object = MibTableColumn
iwfDxSsTrNonOperStatus = _IwfDxSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 3),
    _IwfDxSsTrNonOperStatus_Type()
)
iwfDxSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrNonOperStatus.setStatus("mandatory")


class _IwfDxSsTrClearStatus_Type(Integer32):
    """Custom type iwfDxSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfDxSsTrClearStatus_Type.__name__ = "Integer32"
_IwfDxSsTrClearStatus_Object = MibTableColumn
iwfDxSsTrClearStatus = _IwfDxSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 4),
    _IwfDxSsTrClearStatus_Type()
)
iwfDxSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrClearStatus.setStatus("mandatory")
_IwfDxSsTrMrgOperBitMask_Type = Integer32
_IwfDxSsTrMrgOperBitMask_Object = MibTableColumn
iwfDxSsTrMrgOperBitMask = _IwfDxSsTrMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 5),
    _IwfDxSsTrMrgOperBitMask_Type()
)
iwfDxSsTrMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrMrgOperBitMask.setStatus("mandatory")
_IwfDxSsTrMrgOperThreshCnt_Type = Integer32
_IwfDxSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfDxSsTrMrgOperThreshCnt = _IwfDxSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 6),
    _IwfDxSsTrMrgOperThreshCnt_Type()
)
iwfDxSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfDxSsTrNonOperThreshCnt_Type = Integer32
_IwfDxSsTrNonOperThreshCnt_Object = MibTableColumn
iwfDxSsTrNonOperThreshCnt = _IwfDxSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 7),
    _IwfDxSsTrNonOperThreshCnt_Type()
)
iwfDxSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfDxSsTrClearThreshCnt_Type = Integer32
_IwfDxSsTrClearThreshCnt_Object = MibTableColumn
iwfDxSsTrClearThreshCnt = _IwfDxSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 8),
    _IwfDxSsTrClearThreshCnt_Type()
)
iwfDxSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrClearThreshCnt.setStatus("mandatory")
_IwfDxSsTrMrgOperThreshTimer_Type = Integer32
_IwfDxSsTrMrgOperThreshTimer_Object = MibTableColumn
iwfDxSsTrMrgOperThreshTimer = _IwfDxSsTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 9),
    _IwfDxSsTrMrgOperThreshTimer_Type()
)
iwfDxSsTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrMrgOperThreshTimer.setStatus("mandatory")
_IwfDxSsTrNonOperThreshTimer_Type = Integer32
_IwfDxSsTrNonOperThreshTimer_Object = MibTableColumn
iwfDxSsTrNonOperThreshTimer = _IwfDxSsTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 10),
    _IwfDxSsTrNonOperThreshTimer_Type()
)
iwfDxSsTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrNonOperThreshTimer.setStatus("mandatory")
_IwfDxSsTrClearThreshTimer_Type = Integer32
_IwfDxSsTrClearThreshTimer_Object = MibTableColumn
iwfDxSsTrClearThreshTimer = _IwfDxSsTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 11),
    _IwfDxSsTrClearThreshTimer_Type()
)
iwfDxSsTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfDxSsTrClearThreshTimer.setStatus("mandatory")
_IwfDxSsTrAd9600NoSysResCnt_Type = Integer32
_IwfDxSsTrAd9600NoSysResCnt_Object = MibTableColumn
iwfDxSsTrAd9600NoSysResCnt = _IwfDxSsTrAd9600NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 12),
    _IwfDxSsTrAd9600NoSysResCnt_Type()
)
iwfDxSsTrAd9600NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd9600NoSysResCnt.setStatus("mandatory")
_IwfDxSsTrAd14400NoSysResCnt_Type = Integer32
_IwfDxSsTrAd14400NoSysResCnt_Object = MibTableColumn
iwfDxSsTrAd14400NoSysResCnt = _IwfDxSsTrAd14400NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 13),
    _IwfDxSsTrAd14400NoSysResCnt_Type()
)
iwfDxSsTrAd14400NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd14400NoSysResCnt.setStatus("mandatory")
_IwfDxSsTrFax9600NoSysResCnt_Type = Integer32
_IwfDxSsTrFax9600NoSysResCnt_Object = MibTableColumn
iwfDxSsTrFax9600NoSysResCnt = _IwfDxSsTrFax9600NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 14),
    _IwfDxSsTrFax9600NoSysResCnt_Type()
)
iwfDxSsTrFax9600NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax9600NoSysResCnt.setStatus("mandatory")
_IwfDxSsTrFax14400NoSysResCnt_Type = Integer32
_IwfDxSsTrFax14400NoSysResCnt_Object = MibTableColumn
iwfDxSsTrFax14400NoSysResCnt = _IwfDxSsTrFax14400NoSysResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 15),
    _IwfDxSsTrFax14400NoSysResCnt_Type()
)
iwfDxSsTrFax14400NoSysResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax14400NoSysResCnt.setStatus("mandatory")
_IwfDxSsTrAd9600SktErrCnt_Type = Integer32
_IwfDxSsTrAd9600SktErrCnt_Object = MibTableColumn
iwfDxSsTrAd9600SktErrCnt = _IwfDxSsTrAd9600SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 16),
    _IwfDxSsTrAd9600SktErrCnt_Type()
)
iwfDxSsTrAd9600SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd9600SktErrCnt.setStatus("mandatory")
_IwfDxSsTrAd14400SktErrCnt_Type = Integer32
_IwfDxSsTrAd14400SktErrCnt_Object = MibTableColumn
iwfDxSsTrAd14400SktErrCnt = _IwfDxSsTrAd14400SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 17),
    _IwfDxSsTrAd14400SktErrCnt_Type()
)
iwfDxSsTrAd14400SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd14400SktErrCnt.setStatus("mandatory")
_IwfDxSsTrFax9600SktErrCnt_Type = Integer32
_IwfDxSsTrFax9600SktErrCnt_Object = MibTableColumn
iwfDxSsTrFax9600SktErrCnt = _IwfDxSsTrFax9600SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 18),
    _IwfDxSsTrFax9600SktErrCnt_Type()
)
iwfDxSsTrFax9600SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax9600SktErrCnt.setStatus("mandatory")
_IwfDxSsTrFax14400SktErrCnt_Type = Integer32
_IwfDxSsTrFax14400SktErrCnt_Object = MibTableColumn
iwfDxSsTrFax14400SktErrCnt = _IwfDxSsTrFax14400SktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 19),
    _IwfDxSsTrFax14400SktErrCnt_Type()
)
iwfDxSsTrFax14400SktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax14400SktErrCnt.setStatus("mandatory")
_IwfDxSsTrAd9600PrtErrCnt_Type = Integer32
_IwfDxSsTrAd9600PrtErrCnt_Object = MibTableColumn
iwfDxSsTrAd9600PrtErrCnt = _IwfDxSsTrAd9600PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 20),
    _IwfDxSsTrAd9600PrtErrCnt_Type()
)
iwfDxSsTrAd9600PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd9600PrtErrCnt.setStatus("mandatory")
_IwfDxSsTrAd14400PrtErrCnt_Type = Integer32
_IwfDxSsTrAd14400PrtErrCnt_Object = MibTableColumn
iwfDxSsTrAd14400PrtErrCnt = _IwfDxSsTrAd14400PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 21),
    _IwfDxSsTrAd14400PrtErrCnt_Type()
)
iwfDxSsTrAd14400PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd14400PrtErrCnt.setStatus("mandatory")
_IwfDxSsTrFax9600PrtErrCnt_Type = Integer32
_IwfDxSsTrFax9600PrtErrCnt_Object = MibTableColumn
iwfDxSsTrFax9600PrtErrCnt = _IwfDxSsTrFax9600PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 22),
    _IwfDxSsTrFax9600PrtErrCnt_Type()
)
iwfDxSsTrFax9600PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax9600PrtErrCnt.setStatus("mandatory")
_IwfDxSsTrFax14400PrtErrCnt_Type = Integer32
_IwfDxSsTrFax14400PrtErrCnt_Object = MibTableColumn
iwfDxSsTrFax14400PrtErrCnt = _IwfDxSsTrFax14400PrtErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 23),
    _IwfDxSsTrFax14400PrtErrCnt_Type()
)
iwfDxSsTrFax14400PrtErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax14400PrtErrCnt.setStatus("mandatory")
_IwfDxSsTrAd9600NoMdmResCnt_Type = Integer32
_IwfDxSsTrAd9600NoMdmResCnt_Object = MibTableColumn
iwfDxSsTrAd9600NoMdmResCnt = _IwfDxSsTrAd9600NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 24),
    _IwfDxSsTrAd9600NoMdmResCnt_Type()
)
iwfDxSsTrAd9600NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd9600NoMdmResCnt.setStatus("mandatory")
_IwfDxSsTrAd14400NoMdmResCnt_Type = Integer32
_IwfDxSsTrAd14400NoMdmResCnt_Object = MibTableColumn
iwfDxSsTrAd14400NoMdmResCnt = _IwfDxSsTrAd14400NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 25),
    _IwfDxSsTrAd14400NoMdmResCnt_Type()
)
iwfDxSsTrAd14400NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrAd14400NoMdmResCnt.setStatus("mandatory")
_IwfDxSsTrFax9600NoMdmResCnt_Type = Integer32
_IwfDxSsTrFax9600NoMdmResCnt_Object = MibTableColumn
iwfDxSsTrFax9600NoMdmResCnt = _IwfDxSsTrFax9600NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 26),
    _IwfDxSsTrFax9600NoMdmResCnt_Type()
)
iwfDxSsTrFax9600NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax9600NoMdmResCnt.setStatus("mandatory")
_IwfDxSsTrFax14400NoMdmResCnt_Type = Integer32
_IwfDxSsTrFax14400NoMdmResCnt_Object = MibTableColumn
iwfDxSsTrFax14400NoMdmResCnt = _IwfDxSsTrFax14400NoMdmResCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 27),
    _IwfDxSsTrFax14400NoMdmResCnt_Type()
)
iwfDxSsTrFax14400NoMdmResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrFax14400NoMdmResCnt.setStatus("mandatory")
_IwfDxSsTrNoRespCnt_Type = Integer32
_IwfDxSsTrNoRespCnt_Object = MibTableColumn
iwfDxSsTrNoRespCnt = _IwfDxSsTrNoRespCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 28),
    _IwfDxSsTrNoRespCnt_Type()
)
iwfDxSsTrNoRespCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrNoRespCnt.setStatus("mandatory")


class _IwfDxSsTrStatus_Type(Integer32):
    """Custom type iwfDxSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfDxSsTrStatus_Type.__name__ = "Integer32"
_IwfDxSsTrStatus_Object = MibTableColumn
iwfDxSsTrStatus = _IwfDxSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 27, 1, 1, 29),
    _IwfDxSsTrStatus_Type()
)
iwfDxSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfDxSsTrStatus.setStatus("mandatory")
_IwfCfgCoSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgCoSsTrap = _IwfCfgCoSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28)
)
_IwfCfgCoSsTrapTable_Object = MibTable
iwfCfgCoSsTrapTable = _IwfCfgCoSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1)
)
if mibBuilder.loadTexts:
    iwfCfgCoSsTrapTable.setStatus("mandatory")
_IwfCfgCoSsTrapEntry_Object = MibTableRow
iwfCfgCoSsTrapEntry = _IwfCfgCoSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1)
)
iwfCfgCoSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCoSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgCoSsTrapEntry.setStatus("mandatory")
_IwfCoSsTrIndex_Type = Integer32
_IwfCoSsTrIndex_Object = MibTableColumn
iwfCoSsTrIndex = _IwfCoSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 1),
    _IwfCoSsTrIndex_Type()
)
iwfCoSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCoSsTrIndex.setStatus("mandatory")


class _IwfCoSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfCoSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfCoSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfCoSsTrMrgOperStatus_Object = MibTableColumn
iwfCoSsTrMrgOperStatus = _IwfCoSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 2),
    _IwfCoSsTrMrgOperStatus_Type()
)
iwfCoSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrMrgOperStatus.setStatus("mandatory")


class _IwfCoSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfCoSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfCoSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfCoSsTrNonOperStatus_Object = MibTableColumn
iwfCoSsTrNonOperStatus = _IwfCoSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 3),
    _IwfCoSsTrNonOperStatus_Type()
)
iwfCoSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrNonOperStatus.setStatus("mandatory")


class _IwfCoSsTrClearStatus_Type(Integer32):
    """Custom type iwfCoSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfCoSsTrClearStatus_Type.__name__ = "Integer32"
_IwfCoSsTrClearStatus_Object = MibTableColumn
iwfCoSsTrClearStatus = _IwfCoSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 4),
    _IwfCoSsTrClearStatus_Type()
)
iwfCoSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrClearStatus.setStatus("mandatory")
_IwfCoSsTrMrgOperBitMask_Type = Integer32
_IwfCoSsTrMrgOperBitMask_Object = MibTableColumn
iwfCoSsTrMrgOperBitMask = _IwfCoSsTrMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 5),
    _IwfCoSsTrMrgOperBitMask_Type()
)
iwfCoSsTrMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrMrgOperBitMask.setStatus("mandatory")
_IwfCoSsTrMrgOperThreshCnt_Type = Integer32
_IwfCoSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfCoSsTrMrgOperThreshCnt = _IwfCoSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 6),
    _IwfCoSsTrMrgOperThreshCnt_Type()
)
iwfCoSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfCoSsTrNonOperThreshCnt_Type = Integer32
_IwfCoSsTrNonOperThreshCnt_Object = MibTableColumn
iwfCoSsTrNonOperThreshCnt = _IwfCoSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 7),
    _IwfCoSsTrNonOperThreshCnt_Type()
)
iwfCoSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfCoSsTrClearThreshCnt_Type = Integer32
_IwfCoSsTrClearThreshCnt_Object = MibTableColumn
iwfCoSsTrClearThreshCnt = _IwfCoSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 8),
    _IwfCoSsTrClearThreshCnt_Type()
)
iwfCoSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrClearThreshCnt.setStatus("mandatory")
_IwfCoSsTrMrgOperThreshTimer_Type = Integer32
_IwfCoSsTrMrgOperThreshTimer_Object = MibTableColumn
iwfCoSsTrMrgOperThreshTimer = _IwfCoSsTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 9),
    _IwfCoSsTrMrgOperThreshTimer_Type()
)
iwfCoSsTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrMrgOperThreshTimer.setStatus("mandatory")
_IwfCoSsTrNonOperThreshTimer_Type = Integer32
_IwfCoSsTrNonOperThreshTimer_Object = MibTableColumn
iwfCoSsTrNonOperThreshTimer = _IwfCoSsTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 10),
    _IwfCoSsTrNonOperThreshTimer_Type()
)
iwfCoSsTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrNonOperThreshTimer.setStatus("mandatory")
_IwfCoSsTrClearThreshTimer_Type = Integer32
_IwfCoSsTrClearThreshTimer_Object = MibTableColumn
iwfCoSsTrClearThreshTimer = _IwfCoSsTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 11),
    _IwfCoSsTrClearThreshTimer_Type()
)
iwfCoSsTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCoSsTrClearThreshTimer.setStatus("mandatory")
_IwfCoSsTrSysNoRespErrCnt_Type = Integer32
_IwfCoSsTrSysNoRespErrCnt_Object = MibTableColumn
iwfCoSsTrSysNoRespErrCnt = _IwfCoSsTrSysNoRespErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 12),
    _IwfCoSsTrSysNoRespErrCnt_Type()
)
iwfCoSsTrSysNoRespErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCoSsTrSysNoRespErrCnt.setStatus("mandatory")
_IwfCoSsTrDictOutOfSyncCnt_Type = Integer32
_IwfCoSsTrDictOutOfSyncCnt_Object = MibTableColumn
iwfCoSsTrDictOutOfSyncCnt = _IwfCoSsTrDictOutOfSyncCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 13),
    _IwfCoSsTrDictOutOfSyncCnt_Type()
)
iwfCoSsTrDictOutOfSyncCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCoSsTrDictOutOfSyncCnt.setStatus("mandatory")


class _IwfCoSsTrStatus_Type(Integer32):
    """Custom type iwfCoSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfCoSsTrStatus_Type.__name__ = "Integer32"
_IwfCoSsTrStatus_Object = MibTableColumn
iwfCoSsTrStatus = _IwfCoSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 28, 1, 1, 14),
    _IwfCoSsTrStatus_Type()
)
iwfCoSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCoSsTrStatus.setStatus("mandatory")
_IwfCfgPppSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgPppSsTrap = _IwfCfgPppSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29)
)
_IwfCfgPppSsTrapTable_Object = MibTable
iwfCfgPppSsTrapTable = _IwfCfgPppSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1)
)
if mibBuilder.loadTexts:
    iwfCfgPppSsTrapTable.setStatus("mandatory")
_IwfCfgPppSsTrapEntry_Object = MibTableRow
iwfCfgPppSsTrapEntry = _IwfCfgPppSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1)
)
iwfCfgPppSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfPppSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgPppSsTrapEntry.setStatus("mandatory")
_IwfPppSsTrIndex_Type = Integer32
_IwfPppSsTrIndex_Object = MibTableColumn
iwfPppSsTrIndex = _IwfPppSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 1),
    _IwfPppSsTrIndex_Type()
)
iwfPppSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppSsTrIndex.setStatus("mandatory")


class _IwfPppSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfPppSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPppSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfPppSsTrMrgOperStatus_Object = MibTableColumn
iwfPppSsTrMrgOperStatus = _IwfPppSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 2),
    _IwfPppSsTrMrgOperStatus_Type()
)
iwfPppSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrMrgOperStatus.setStatus("mandatory")


class _IwfPppSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfPppSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPppSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfPppSsTrNonOperStatus_Object = MibTableColumn
iwfPppSsTrNonOperStatus = _IwfPppSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 3),
    _IwfPppSsTrNonOperStatus_Type()
)
iwfPppSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrNonOperStatus.setStatus("mandatory")


class _IwfPppSsTrClearStatus_Type(Integer32):
    """Custom type iwfPppSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfPppSsTrClearStatus_Type.__name__ = "Integer32"
_IwfPppSsTrClearStatus_Object = MibTableColumn
iwfPppSsTrClearStatus = _IwfPppSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 4),
    _IwfPppSsTrClearStatus_Type()
)
iwfPppSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrClearStatus.setStatus("mandatory")
_IwfPppSsTrMrgOperBitMask_Type = Integer32
_IwfPppSsTrMrgOperBitMask_Object = MibTableColumn
iwfPppSsTrMrgOperBitMask = _IwfPppSsTrMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 5),
    _IwfPppSsTrMrgOperBitMask_Type()
)
iwfPppSsTrMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrMrgOperBitMask.setStatus("mandatory")
_IwfPppSsTrMrgOperThreshCnt_Type = Integer32
_IwfPppSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfPppSsTrMrgOperThreshCnt = _IwfPppSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 6),
    _IwfPppSsTrMrgOperThreshCnt_Type()
)
iwfPppSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfPppSsTrNonOperThreshCnt_Type = Integer32
_IwfPppSsTrNonOperThreshCnt_Object = MibTableColumn
iwfPppSsTrNonOperThreshCnt = _IwfPppSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 7),
    _IwfPppSsTrNonOperThreshCnt_Type()
)
iwfPppSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfPppSsTrClearThreshCnt_Type = Integer32
_IwfPppSsTrClearThreshCnt_Object = MibTableColumn
iwfPppSsTrClearThreshCnt = _IwfPppSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 8),
    _IwfPppSsTrClearThreshCnt_Type()
)
iwfPppSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrClearThreshCnt.setStatus("mandatory")
_IwfPppSsTrMrgOperThreshTimer_Type = Integer32
_IwfPppSsTrMrgOperThreshTimer_Object = MibTableColumn
iwfPppSsTrMrgOperThreshTimer = _IwfPppSsTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 9),
    _IwfPppSsTrMrgOperThreshTimer_Type()
)
iwfPppSsTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrMrgOperThreshTimer.setStatus("mandatory")
_IwfPppSsTrNonOperThreshTimer_Type = Integer32
_IwfPppSsTrNonOperThreshTimer_Object = MibTableColumn
iwfPppSsTrNonOperThreshTimer = _IwfPppSsTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 10),
    _IwfPppSsTrNonOperThreshTimer_Type()
)
iwfPppSsTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrNonOperThreshTimer.setStatus("mandatory")
_IwfPppSsTrClearThreshTimer_Type = Integer32
_IwfPppSsTrClearThreshTimer_Object = MibTableColumn
iwfPppSsTrClearThreshTimer = _IwfPppSsTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 11),
    _IwfPppSsTrClearThreshTimer_Type()
)
iwfPppSsTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfPppSsTrClearThreshTimer.setStatus("mandatory")
_IwfPppSsTrSysNoRespErrCnt_Type = Integer32
_IwfPppSsTrSysNoRespErrCnt_Object = MibTableColumn
iwfPppSsTrSysNoRespErrCnt = _IwfPppSsTrSysNoRespErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 12),
    _IwfPppSsTrSysNoRespErrCnt_Type()
)
iwfPppSsTrSysNoRespErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppSsTrSysNoRespErrCnt.setStatus("mandatory")
_IwfPppSsTrCrcErrCnt_Type = Integer32
_IwfPppSsTrCrcErrCnt_Object = MibTableColumn
iwfPppSsTrCrcErrCnt = _IwfPppSsTrCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 13),
    _IwfPppSsTrCrcErrCnt_Type()
)
iwfPppSsTrCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppSsTrCrcErrCnt.setStatus("mandatory")


class _IwfPppSsTrStatus_Type(Integer32):
    """Custom type iwfPppSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfPppSsTrStatus_Type.__name__ = "Integer32"
_IwfPppSsTrStatus_Object = MibTableColumn
iwfPppSsTrStatus = _IwfPppSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 29, 1, 1, 14),
    _IwfPppSsTrStatus_Type()
)
iwfPppSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfPppSsTrStatus.setStatus("mandatory")
_IwfCfgTcpSsTrap_ObjectIdentity = ObjectIdentity
iwfCfgTcpSsTrap = _IwfCfgTcpSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30)
)
_IwfCfgTcpSsTrapTable_Object = MibTable
iwfCfgTcpSsTrapTable = _IwfCfgTcpSsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1)
)
if mibBuilder.loadTexts:
    iwfCfgTcpSsTrapTable.setStatus("mandatory")
_IwfCfgTcpSsTrapEntry_Object = MibTableRow
iwfCfgTcpSsTrapEntry = _IwfCfgTcpSsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1)
)
iwfCfgTcpSsTrapEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfTcpSsTrIndex"),
)
if mibBuilder.loadTexts:
    iwfCfgTcpSsTrapEntry.setStatus("mandatory")
_IwfTcpSsTrIndex_Type = Integer32
_IwfTcpSsTrIndex_Object = MibTableColumn
iwfTcpSsTrIndex = _IwfTcpSsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 1),
    _IwfTcpSsTrIndex_Type()
)
iwfTcpSsTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpSsTrIndex.setStatus("mandatory")


class _IwfTcpSsTrMrgOperStatus_Type(Integer32):
    """Custom type iwfTcpSsTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTcpSsTrMrgOperStatus_Type.__name__ = "Integer32"
_IwfTcpSsTrMrgOperStatus_Object = MibTableColumn
iwfTcpSsTrMrgOperStatus = _IwfTcpSsTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 2),
    _IwfTcpSsTrMrgOperStatus_Type()
)
iwfTcpSsTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrMrgOperStatus.setStatus("mandatory")


class _IwfTcpSsTrNonOperStatus_Type(Integer32):
    """Custom type iwfTcpSsTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTcpSsTrNonOperStatus_Type.__name__ = "Integer32"
_IwfTcpSsTrNonOperStatus_Object = MibTableColumn
iwfTcpSsTrNonOperStatus = _IwfTcpSsTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 3),
    _IwfTcpSsTrNonOperStatus_Type()
)
iwfTcpSsTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrNonOperStatus.setStatus("mandatory")


class _IwfTcpSsTrClearStatus_Type(Integer32):
    """Custom type iwfTcpSsTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTrap", 2),
          ("enableTrap", 1))
    )


_IwfTcpSsTrClearStatus_Type.__name__ = "Integer32"
_IwfTcpSsTrClearStatus_Object = MibTableColumn
iwfTcpSsTrClearStatus = _IwfTcpSsTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 4),
    _IwfTcpSsTrClearStatus_Type()
)
iwfTcpSsTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrClearStatus.setStatus("mandatory")
_IwfTcpSsTrMrgOperBitMask_Type = Integer32
_IwfTcpSsTrMrgOperBitMask_Object = MibTableColumn
iwfTcpSsTrMrgOperBitMask = _IwfTcpSsTrMrgOperBitMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 5),
    _IwfTcpSsTrMrgOperBitMask_Type()
)
iwfTcpSsTrMrgOperBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrMrgOperBitMask.setStatus("mandatory")
_IwfTcpSsTrMrgOperThreshCnt_Type = Integer32
_IwfTcpSsTrMrgOperThreshCnt_Object = MibTableColumn
iwfTcpSsTrMrgOperThreshCnt = _IwfTcpSsTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 6),
    _IwfTcpSsTrMrgOperThreshCnt_Type()
)
iwfTcpSsTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrMrgOperThreshCnt.setStatus("mandatory")
_IwfTcpSsTrNonOperThreshCnt_Type = Integer32
_IwfTcpSsTrNonOperThreshCnt_Object = MibTableColumn
iwfTcpSsTrNonOperThreshCnt = _IwfTcpSsTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 7),
    _IwfTcpSsTrNonOperThreshCnt_Type()
)
iwfTcpSsTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrNonOperThreshCnt.setStatus("mandatory")
_IwfTcpSsTrClearThreshCnt_Type = Integer32
_IwfTcpSsTrClearThreshCnt_Object = MibTableColumn
iwfTcpSsTrClearThreshCnt = _IwfTcpSsTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 8),
    _IwfTcpSsTrClearThreshCnt_Type()
)
iwfTcpSsTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrClearThreshCnt.setStatus("mandatory")
_IwfTcpSsTrMrgOperThreshTimer_Type = Integer32
_IwfTcpSsTrMrgOperThreshTimer_Object = MibTableColumn
iwfTcpSsTrMrgOperThreshTimer = _IwfTcpSsTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 9),
    _IwfTcpSsTrMrgOperThreshTimer_Type()
)
iwfTcpSsTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrMrgOperThreshTimer.setStatus("mandatory")
_IwfTcpSsTrNonOperThreshTimer_Type = Integer32
_IwfTcpSsTrNonOperThreshTimer_Object = MibTableColumn
iwfTcpSsTrNonOperThreshTimer = _IwfTcpSsTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 10),
    _IwfTcpSsTrNonOperThreshTimer_Type()
)
iwfTcpSsTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrNonOperThreshTimer.setStatus("mandatory")
_IwfTcpSsTrClearThreshTimer_Type = Integer32
_IwfTcpSsTrClearThreshTimer_Object = MibTableColumn
iwfTcpSsTrClearThreshTimer = _IwfTcpSsTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 11),
    _IwfTcpSsTrClearThreshTimer_Type()
)
iwfTcpSsTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfTcpSsTrClearThreshTimer.setStatus("mandatory")
_IwfTcpSsTrSysNoRespErrCnt_Type = Integer32
_IwfTcpSsTrSysNoRespErrCnt_Object = MibTableColumn
iwfTcpSsTrSysNoRespErrCnt = _IwfTcpSsTrSysNoRespErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 12),
    _IwfTcpSsTrSysNoRespErrCnt_Type()
)
iwfTcpSsTrSysNoRespErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpSsTrSysNoRespErrCnt.setStatus("mandatory")


class _IwfTcpSsTrStatus_Type(Integer32):
    """Custom type iwfTcpSsTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_IwfTcpSsTrStatus_Type.__name__ = "Integer32"
_IwfTcpSsTrStatus_Object = MibTableColumn
iwfTcpSsTrStatus = _IwfTcpSsTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 30, 1, 1, 13),
    _IwfTcpSsTrStatus_Type()
)
iwfTcpSsTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfTcpSsTrStatus.setStatus("mandatory")
_IwfOprFrRly_ObjectIdentity = ObjectIdentity
iwfOprFrRly = _IwfOprFrRly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31)
)
_IwfOprFrRlyTable_Object = MibTable
iwfOprFrRlyTable = _IwfOprFrRlyTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31, 1)
)
if mibBuilder.loadTexts:
    iwfOprFrRlyTable.setStatus("mandatory")
_IwfOprFrRlyEntry_Object = MibTableRow
iwfOprFrRlyEntry = _IwfOprFrRlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31, 1, 1)
)
iwfOprFrRlyEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfOprFrRlyIndex"),
)
if mibBuilder.loadTexts:
    iwfOprFrRlyEntry.setStatus("mandatory")
_IwfOprFrRlyIndex_Type = Integer32
_IwfOprFrRlyIndex_Object = MibTableColumn
iwfOprFrRlyIndex = _IwfOprFrRlyIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31, 1, 1, 1),
    _IwfOprFrRlyIndex_Type()
)
iwfOprFrRlyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprFrRlyIndex.setStatus("mandatory")
_IwfOprFrRlyT391StatusEnqryTimr_Type = Integer32
_IwfOprFrRlyT391StatusEnqryTimr_Object = MibTableColumn
iwfOprFrRlyT391StatusEnqryTimr = _IwfOprFrRlyT391StatusEnqryTimr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31, 1, 1, 2),
    _IwfOprFrRlyT391StatusEnqryTimr_Type()
)
iwfOprFrRlyT391StatusEnqryTimr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprFrRlyT391StatusEnqryTimr.setStatus("mandatory")
_IwfOprFrRlyT392StatusTimer_Type = Integer32
_IwfOprFrRlyT392StatusTimer_Object = MibTableColumn
iwfOprFrRlyT392StatusTimer = _IwfOprFrRlyT392StatusTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31, 1, 1, 3),
    _IwfOprFrRlyT392StatusTimer_Type()
)
iwfOprFrRlyT392StatusTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprFrRlyT392StatusTimer.setStatus("mandatory")
_IwfOprFrRlyN391StatusEnqrySent_Type = Integer32
_IwfOprFrRlyN391StatusEnqrySent_Object = MibTableColumn
iwfOprFrRlyN391StatusEnqrySent = _IwfOprFrRlyN391StatusEnqrySent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 31, 1, 1, 4),
    _IwfOprFrRlyN391StatusEnqrySent_Type()
)
iwfOprFrRlyN391StatusEnqrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprFrRlyN391StatusEnqrySent.setStatus("mandatory")
_IwfOprQ921_ObjectIdentity = ObjectIdentity
iwfOprQ921 = _IwfOprQ921_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32)
)
_IwfOprQ921Table_Object = MibTable
iwfOprQ921Table = _IwfOprQ921Table_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1)
)
if mibBuilder.loadTexts:
    iwfOprQ921Table.setStatus("mandatory")
_IwfOprQ921Entry_Object = MibTableRow
iwfOprQ921Entry = _IwfOprQ921Entry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1)
)
iwfOprQ921Entry.setIndexNames(
    (0, "IWFG-MIB", "iwfOprQ921Index"),
)
if mibBuilder.loadTexts:
    iwfOprQ921Entry.setStatus("mandatory")
_IwfOprQ921Index_Type = Integer32
_IwfOprQ921Index_Object = MibTableColumn
iwfOprQ921Index = _IwfOprQ921Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 1),
    _IwfOprQ921Index_Type()
)
iwfOprQ921Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921Index.setStatus("mandatory")
_IwfOprQ921KmaxOutStandPkt_Type = Integer32
_IwfOprQ921KmaxOutStandPkt_Object = MibTableColumn
iwfOprQ921KmaxOutStandPkt = _IwfOprQ921KmaxOutStandPkt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 2),
    _IwfOprQ921KmaxOutStandPkt_Type()
)
iwfOprQ921KmaxOutStandPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921KmaxOutStandPkt.setStatus("mandatory")
_IwfOprQ921T200IframeAckTimer_Type = Integer32
_IwfOprQ921T200IframeAckTimer_Object = MibTableColumn
iwfOprQ921T200IframeAckTimer = _IwfOprQ921T200IframeAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 3),
    _IwfOprQ921T200IframeAckTimer_Type()
)
iwfOprQ921T200IframeAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921T200IframeAckTimer.setStatus("mandatory")
_IwfOprQ921T203MaxTimeNoIframe_Type = Integer32
_IwfOprQ921T203MaxTimeNoIframe_Object = MibTableColumn
iwfOprQ921T203MaxTimeNoIframe = _IwfOprQ921T203MaxTimeNoIframe_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 4),
    _IwfOprQ921T203MaxTimeNoIframe_Type()
)
iwfOprQ921T203MaxTimeNoIframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921T203MaxTimeNoIframe.setStatus("mandatory")
_IwfOprQ921N200MaxFrameRetrans_Type = Integer32
_IwfOprQ921N200MaxFrameRetrans_Object = MibTableColumn
iwfOprQ921N200MaxFrameRetrans = _IwfOprQ921N200MaxFrameRetrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 5),
    _IwfOprQ921N200MaxFrameRetrans_Type()
)
iwfOprQ921N200MaxFrameRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921N200MaxFrameRetrans.setStatus("mandatory")
_IwfOprQ921N201RxMaxOctetInfo_Type = Integer32
_IwfOprQ921N201RxMaxOctetInfo_Object = MibTableColumn
iwfOprQ921N201RxMaxOctetInfo = _IwfOprQ921N201RxMaxOctetInfo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 6),
    _IwfOprQ921N201RxMaxOctetInfo_Type()
)
iwfOprQ921N201RxMaxOctetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921N201RxMaxOctetInfo.setStatus("mandatory")
_IwfOprQ921N201TxMaxOctetInfo_Type = Integer32
_IwfOprQ921N201TxMaxOctetInfo_Object = MibTableColumn
iwfOprQ921N201TxMaxOctetInfo = _IwfOprQ921N201TxMaxOctetInfo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 32, 1, 1, 7),
    _IwfOprQ921N201TxMaxOctetInfo_Type()
)
iwfOprQ921N201TxMaxOctetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ921N201TxMaxOctetInfo.setStatus("mandatory")
_IwfOprQ933_ObjectIdentity = ObjectIdentity
iwfOprQ933 = _IwfOprQ933_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33)
)
_IwfOprQ933Table_Object = MibTable
iwfOprQ933Table = _IwfOprQ933Table_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1)
)
if mibBuilder.loadTexts:
    iwfOprQ933Table.setStatus("mandatory")
_IwfOprQ933Entry_Object = MibTableRow
iwfOprQ933Entry = _IwfOprQ933Entry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1)
)
iwfOprQ933Entry.setIndexNames(
    (0, "IWFG-MIB", "iwfOprQ933Index"),
)
if mibBuilder.loadTexts:
    iwfOprQ933Entry.setStatus("mandatory")
_IwfOprQ933Index_Type = Integer32
_IwfOprQ933Index_Object = MibTableColumn
iwfOprQ933Index = _IwfOprQ933Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 1),
    _IwfOprQ933Index_Type()
)
iwfOprQ933Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933Index.setStatus("mandatory")
_IwfOprQ933T303SetupTimer_Type = Integer32
_IwfOprQ933T303SetupTimer_Object = MibTableColumn
iwfOprQ933T303SetupTimer = _IwfOprQ933T303SetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 2),
    _IwfOprQ933T303SetupTimer_Type()
)
iwfOprQ933T303SetupTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933T303SetupTimer.setStatus("mandatory")
_IwfOprQ933T305DisconnectTimer_Type = Integer32
_IwfOprQ933T305DisconnectTimer_Object = MibTableColumn
iwfOprQ933T305DisconnectTimer = _IwfOprQ933T305DisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 3),
    _IwfOprQ933T305DisconnectTimer_Type()
)
iwfOprQ933T305DisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933T305DisconnectTimer.setStatus("mandatory")
_IwfOprQ933T308ReleaseTimer_Type = Integer32
_IwfOprQ933T308ReleaseTimer_Object = MibTableColumn
iwfOprQ933T308ReleaseTimer = _IwfOprQ933T308ReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 4),
    _IwfOprQ933T308ReleaseTimer_Type()
)
iwfOprQ933T308ReleaseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933T308ReleaseTimer.setStatus("mandatory")
_IwfOprQ933T309DataLinkDiscTimr_Type = Integer32
_IwfOprQ933T309DataLinkDiscTimr_Object = MibTableColumn
iwfOprQ933T309DataLinkDiscTimr = _IwfOprQ933T309DataLinkDiscTimr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 5),
    _IwfOprQ933T309DataLinkDiscTimr_Type()
)
iwfOprQ933T309DataLinkDiscTimr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933T309DataLinkDiscTimr.setStatus("mandatory")
_IwfOprQ933T310CallProceedTimer_Type = Integer32
_IwfOprQ933T310CallProceedTimer_Object = MibTableColumn
iwfOprQ933T310CallProceedTimer = _IwfOprQ933T310CallProceedTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 6),
    _IwfOprQ933T310CallProceedTimer_Type()
)
iwfOprQ933T310CallProceedTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933T310CallProceedTimer.setStatus("mandatory")
_IwfOprQ933T313ConnectSentTimer_Type = Integer32
_IwfOprQ933T313ConnectSentTimer_Object = MibTableColumn
iwfOprQ933T313ConnectSentTimer = _IwfOprQ933T313ConnectSentTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 33, 1, 1, 7),
    _IwfOprQ933T313ConnectSentTimer_Type()
)
iwfOprQ933T313ConnectSentTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprQ933T313ConnectSentTimer.setStatus("mandatory")
_IwfOprCallStats_ObjectIdentity = ObjectIdentity
iwfOprCallStats = _IwfOprCallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34)
)
_IwfOprCallStatsTable_Object = MibTable
iwfOprCallStatsTable = _IwfOprCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1)
)
if mibBuilder.loadTexts:
    iwfOprCallStatsTable.setStatus("mandatory")
_IwfOprCallStatsEntry_Object = MibTableRow
iwfOprCallStatsEntry = _IwfOprCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1, 1)
)
iwfOprCallStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfOprCsIndex"),
)
if mibBuilder.loadTexts:
    iwfOprCallStatsEntry.setStatus("mandatory")
_IwfOprCsIndex_Type = Integer32
_IwfOprCsIndex_Object = MibTableColumn
iwfOprCsIndex = _IwfOprCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1, 1, 1),
    _IwfOprCsIndex_Type()
)
iwfOprCsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprCsIndex.setStatus("mandatory")


class _IwfOprCsMobOrigAdStats_Type(Integer32):
    """Custom type iwfOprCsMobOrigAdStats based on Integer32"""
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


_IwfOprCsMobOrigAdStats_Type.__name__ = "Integer32"
_IwfOprCsMobOrigAdStats_Object = MibTableColumn
iwfOprCsMobOrigAdStats = _IwfOprCsMobOrigAdStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1, 1, 2),
    _IwfOprCsMobOrigAdStats_Type()
)
iwfOprCsMobOrigAdStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprCsMobOrigAdStats.setStatus("mandatory")


class _IwfOprCsMobOrigFaxStats_Type(Integer32):
    """Custom type iwfOprCsMobOrigFaxStats based on Integer32"""
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


_IwfOprCsMobOrigFaxStats_Type.__name__ = "Integer32"
_IwfOprCsMobOrigFaxStats_Object = MibTableColumn
iwfOprCsMobOrigFaxStats = _IwfOprCsMobOrigFaxStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1, 1, 3),
    _IwfOprCsMobOrigFaxStats_Type()
)
iwfOprCsMobOrigFaxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprCsMobOrigFaxStats.setStatus("mandatory")


class _IwfOprCsMobTermAdStats_Type(Integer32):
    """Custom type iwfOprCsMobTermAdStats based on Integer32"""
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


_IwfOprCsMobTermAdStats_Type.__name__ = "Integer32"
_IwfOprCsMobTermAdStats_Object = MibTableColumn
iwfOprCsMobTermAdStats = _IwfOprCsMobTermAdStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1, 1, 4),
    _IwfOprCsMobTermAdStats_Type()
)
iwfOprCsMobTermAdStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprCsMobTermAdStats.setStatus("mandatory")


class _IwfOprCsMobTermFaxStats_Type(Integer32):
    """Custom type iwfOprCsMobTermFaxStats based on Integer32"""
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


_IwfOprCsMobTermFaxStats_Type.__name__ = "Integer32"
_IwfOprCsMobTermFaxStats_Object = MibTableColumn
iwfOprCsMobTermFaxStats = _IwfOprCsMobTermFaxStats_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 34, 1, 1, 5),
    _IwfOprCsMobTermFaxStats_Type()
)
iwfOprCsMobTermFaxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprCsMobTermFaxStats.setStatus("mandatory")
_IwfOprPppParam_ObjectIdentity = ObjectIdentity
iwfOprPppParam = _IwfOprPppParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35)
)
_IwfOprPppParamTable_Object = MibTable
iwfOprPppParamTable = _IwfOprPppParamTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1)
)
if mibBuilder.loadTexts:
    iwfOprPppParamTable.setStatus("mandatory")
_IwfOprPppParamEntry_Object = MibTableRow
iwfOprPppParamEntry = _IwfOprPppParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1)
)
iwfOprPppParamEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfOprPppIndex"),
)
if mibBuilder.loadTexts:
    iwfOprPppParamEntry.setStatus("mandatory")
_IwfOprPppIndex_Type = Integer32
_IwfOprPppIndex_Object = MibTableColumn
iwfOprPppIndex = _IwfOprPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 1),
    _IwfOprPppIndex_Type()
)
iwfOprPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppIndex.setStatus("mandatory")
_IwfOprPppForceEncryptData_Type = Integer32
_IwfOprPppForceEncryptData_Object = MibTableColumn
iwfOprPppForceEncryptData = _IwfOprPppForceEncryptData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 2),
    _IwfOprPppForceEncryptData_Type()
)
iwfOprPppForceEncryptData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppForceEncryptData.setStatus("mandatory")
_IwfOprPppForceEncryptpassword_Type = Integer32
_IwfOprPppForceEncryptpassword_Object = MibTableColumn
iwfOprPppForceEncryptpassword = _IwfOprPppForceEncryptpassword_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 3),
    _IwfOprPppForceEncryptpassword_Type()
)
iwfOprPppForceEncryptpassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppForceEncryptpassword.setStatus("mandatory")
_IwfOprMaxNumbConfigRequests_Type = Integer32
_IwfOprMaxNumbConfigRequests_Object = MibTableColumn
iwfOprMaxNumbConfigRequests = _IwfOprMaxNumbConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 4),
    _IwfOprMaxNumbConfigRequests_Type()
)
iwfOprMaxNumbConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprMaxNumbConfigRequests.setStatus("mandatory")
_IwfOprMaxNumbConfigNAK_Type = Integer32
_IwfOprMaxNumbConfigNAK_Object = MibTableColumn
iwfOprMaxNumbConfigNAK = _IwfOprMaxNumbConfigNAK_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 5),
    _IwfOprMaxNumbConfigNAK_Type()
)
iwfOprMaxNumbConfigNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprMaxNumbConfigNAK.setStatus("mandatory")
_IwfOprPppMaxNumbRejects_Type = Integer32
_IwfOprPppMaxNumbRejects_Object = MibTableColumn
iwfOprPppMaxNumbRejects = _IwfOprPppMaxNumbRejects_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 6),
    _IwfOprPppMaxNumbRejects_Type()
)
iwfOprPppMaxNumbRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppMaxNumbRejects.setStatus("mandatory")
_IwfOprPppMaxNumbTermRequests_Type = Integer32
_IwfOprPppMaxNumbTermRequests_Object = MibTableColumn
iwfOprPppMaxNumbTermRequests = _IwfOprPppMaxNumbTermRequests_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 7),
    _IwfOprPppMaxNumbTermRequests_Type()
)
iwfOprPppMaxNumbTermRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppMaxNumbTermRequests.setStatus("mandatory")
_IwfOprPppNegotiateTime_Type = Integer32
_IwfOprPppNegotiateTime_Object = MibTableColumn
iwfOprPppNegotiateTime = _IwfOprPppNegotiateTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 8),
    _IwfOprPppNegotiateTime_Type()
)
iwfOprPppNegotiateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppNegotiateTime.setStatus("mandatory")
_IwfOprPppRestartTime_Type = Integer32
_IwfOprPppRestartTime_Object = MibTableColumn
iwfOprPppRestartTime = _IwfOprPppRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 9),
    _IwfOprPppRestartTime_Type()
)
iwfOprPppRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppRestartTime.setStatus("mandatory")
_IwfOprPppIpAddressPoolMax_Type = IpAddress
_IwfOprPppIpAddressPoolMax_Object = MibTableColumn
iwfOprPppIpAddressPoolMax = _IwfOprPppIpAddressPoolMax_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 10),
    _IwfOprPppIpAddressPoolMax_Type()
)
iwfOprPppIpAddressPoolMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppIpAddressPoolMax.setStatus("mandatory")
_IwfOprPppIpAddressPoolMin_Type = IpAddress
_IwfOprPppIpAddressPoolMin_Object = MibTableColumn
iwfOprPppIpAddressPoolMin = _IwfOprPppIpAddressPoolMin_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 35, 1, 1, 11),
    _IwfOprPppIpAddressPoolMin_Type()
)
iwfOprPppIpAddressPoolMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprPppIpAddressPoolMin.setStatus("mandatory")
_IwfOprTcpIp_ObjectIdentity = ObjectIdentity
iwfOprTcpIp = _IwfOprTcpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36)
)
_IwfOprTcpIpTable_Object = MibTable
iwfOprTcpIpTable = _IwfOprTcpIpTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1)
)
if mibBuilder.loadTexts:
    iwfOprTcpIpTable.setStatus("mandatory")
_IwfOprTcpIpEntry_Object = MibTableRow
iwfOprTcpIpEntry = _IwfOprTcpIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1)
)
iwfOprTcpIpEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfOprTiIndex"),
)
if mibBuilder.loadTexts:
    iwfOprTcpIpEntry.setStatus("mandatory")
_IwfOprTiIndex_Type = Integer32
_IwfOprTiIndex_Object = MibTableColumn
iwfOprTiIndex = _IwfOprTiIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 1),
    _IwfOprTiIndex_Type()
)
iwfOprTiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiIndex.setStatus("mandatory")


class _IwfOprTiDefaultServiceType_Type(Integer32):
    """Custom type iwfOprTiDefaultServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IwfOprTiDefaultServiceType_Type.__name__ = "Integer32"
_IwfOprTiDefaultServiceType_Object = MibTableColumn
iwfOprTiDefaultServiceType = _IwfOprTiDefaultServiceType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 2),
    _IwfOprTiDefaultServiceType_Type()
)
iwfOprTiDefaultServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiDefaultServiceType.setStatus("mandatory")


class _IwfOprTiDefaultTimeToLive_Type(Integer32):
    """Custom type iwfOprTiDefaultTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IwfOprTiDefaultTimeToLive_Type.__name__ = "Integer32"
_IwfOprTiDefaultTimeToLive_Object = MibTableColumn
iwfOprTiDefaultTimeToLive = _IwfOprTiDefaultTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 3),
    _IwfOprTiDefaultTimeToLive_Type()
)
iwfOprTiDefaultTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiDefaultTimeToLive.setStatus("mandatory")
_IwfOprTiMtuDiscovery_Type = Integer32
_IwfOprTiMtuDiscovery_Object = MibTableColumn
iwfOprTiMtuDiscovery = _IwfOprTiMtuDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 4),
    _IwfOprTiMtuDiscovery_Type()
)
iwfOprTiMtuDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiMtuDiscovery.setStatus("mandatory")
_IwfOprTiKeepAliveInterval_Type = Integer32
_IwfOprTiKeepAliveInterval_Object = MibTableColumn
iwfOprTiKeepAliveInterval = _IwfOprTiKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 5),
    _IwfOprTiKeepAliveInterval_Type()
)
iwfOprTiKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiKeepAliveInterval.setStatus("mandatory")
_IwfOprTiKeepAliveTime_Type = Integer32
_IwfOprTiKeepAliveTime_Object = MibTableColumn
iwfOprTiKeepAliveTime = _IwfOprTiKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 6),
    _IwfOprTiKeepAliveTime_Type()
)
iwfOprTiKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiKeepAliveTime.setStatus("mandatory")
_IwfOprTiMaxMtuSize_Type = Integer32
_IwfOprTiMaxMtuSize_Object = MibTableColumn
iwfOprTiMaxMtuSize = _IwfOprTiMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 7),
    _IwfOprTiMaxMtuSize_Type()
)
iwfOprTiMaxMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiMaxMtuSize.setStatus("mandatory")
_IwfOprTiMaxConnectReTrans_Type = Integer32
_IwfOprTiMaxConnectReTrans_Object = MibTableColumn
iwfOprTiMaxConnectReTrans = _IwfOprTiMaxConnectReTrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 8),
    _IwfOprTiMaxConnectReTrans_Type()
)
iwfOprTiMaxConnectReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiMaxConnectReTrans.setStatus("mandatory")
_IwfOprTiMaxDataRetrans_Type = Integer32
_IwfOprTiMaxDataRetrans_Object = MibTableColumn
iwfOprTiMaxDataRetrans = _IwfOprTiMaxDataRetrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 9),
    _IwfOprTiMaxDataRetrans_Type()
)
iwfOprTiMaxDataRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiMaxDataRetrans.setStatus("mandatory")
_IwfOprTiMaxNumberConnections_Type = Integer32
_IwfOprTiMaxNumberConnections_Object = MibTableColumn
iwfOprTiMaxNumberConnections = _IwfOprTiMaxNumberConnections_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 10),
    _IwfOprTiMaxNumberConnections_Type()
)
iwfOprTiMaxNumberConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiMaxNumberConnections.setStatus("mandatory")
_IwfOprTiWindowSize_Type = Integer32
_IwfOprTiWindowSize_Object = MibTableColumn
iwfOprTiWindowSize = _IwfOprTiWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 11),
    _IwfOprTiWindowSize_Type()
)
iwfOprTiWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiWindowSize.setStatus("mandatory")
_IwfOprTiLocalIpAddress_Type = IpAddress
_IwfOprTiLocalIpAddress_Object = MibTableColumn
iwfOprTiLocalIpAddress = _IwfOprTiLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 12),
    _IwfOprTiLocalIpAddress_Type()
)
iwfOprTiLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiLocalIpAddress.setStatus("mandatory")
_IwfOprTiSubnetIpMask_Type = IpAddress
_IwfOprTiSubnetIpMask_Object = MibTableColumn
iwfOprTiSubnetIpMask = _IwfOprTiSubnetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 13),
    _IwfOprTiSubnetIpMask_Type()
)
iwfOprTiSubnetIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiSubnetIpMask.setStatus("mandatory")
_IwfOprTiDefualtGatewayIp_Type = IpAddress
_IwfOprTiDefualtGatewayIp_Object = MibTableColumn
iwfOprTiDefualtGatewayIp = _IwfOprTiDefualtGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 36, 1, 1, 14),
    _IwfOprTiDefualtGatewayIp_Type()
)
iwfOprTiDefualtGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfOprTiDefualtGatewayIp.setStatus("mandatory")
_IwfLogStats_ObjectIdentity = ObjectIdentity
iwfLogStats = _IwfLogStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37)
)
_IwfLogStatsTable_Object = MibTable
iwfLogStatsTable = _IwfLogStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1)
)
if mibBuilder.loadTexts:
    iwfLogStatsTable.setStatus("mandatory")
_IwfLogStatsEntry_Object = MibTableRow
iwfLogStatsEntry = _IwfLogStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1)
)
iwfLogStatsEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfLogStsIndex"),
    (0, "IWFG-MIB", "iwfLogStsIndex2"),
)
if mibBuilder.loadTexts:
    iwfLogStatsEntry.setStatus("mandatory")
_IwfLogStsIndex_Type = Integer32
_IwfLogStsIndex_Object = MibTableColumn
iwfLogStsIndex = _IwfLogStsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 1),
    _IwfLogStsIndex_Type()
)
iwfLogStsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogStsIndex.setStatus("mandatory")
_IwfLogStsIndex2_Type = Integer32
_IwfLogStsIndex2_Object = MibTableColumn
iwfLogStsIndex2 = _IwfLogStsIndex2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 2),
    _IwfLogStsIndex2_Type()
)
iwfLogStsIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogStsIndex2.setStatus("mandatory")
_IwfLogCallRefNum_Type = Integer32
_IwfLogCallRefNum_Object = MibTableColumn
iwfLogCallRefNum = _IwfLogCallRefNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 3),
    _IwfLogCallRefNum_Type()
)
iwfLogCallRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCallRefNum.setStatus("mandatory")
_IwfLogMobileIpAddr_Type = IpAddress
_IwfLogMobileIpAddr_Object = MibTableColumn
iwfLogMobileIpAddr = _IwfLogMobileIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 4),
    _IwfLogMobileIpAddr_Type()
)
iwfLogMobileIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogMobileIpAddr.setStatus("mandatory")


class _IwfLogCallingPartyNum_Type(DisplayString):
    """Custom type iwfLogCallingPartyNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_IwfLogCallingPartyNum_Type.__name__ = "DisplayString"
_IwfLogCallingPartyNum_Object = MibTableColumn
iwfLogCallingPartyNum = _IwfLogCallingPartyNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 5),
    _IwfLogCallingPartyNum_Type()
)
iwfLogCallingPartyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCallingPartyNum.setStatus("mandatory")


class _IwfLogCalledPartyNum_Type(DisplayString):
    """Custom type iwfLogCalledPartyNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_IwfLogCalledPartyNum_Type.__name__ = "DisplayString"
_IwfLogCalledPartyNum_Object = MibTableColumn
iwfLogCalledPartyNum = _IwfLogCalledPartyNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 6),
    _IwfLogCalledPartyNum_Type()
)
iwfLogCalledPartyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCalledPartyNum.setStatus("mandatory")


class _IwfLogCallType_Type(Integer32):
    """Custom type iwfLogCallType based on Integer32"""
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
        *(("iNFORMCHGPKTMOBILITY", 4),
          ("mobileOriginate", 1),
          ("mobileTerminate", 2),
          ("rEQINFORMOFDORMANTLL", 3))
    )


_IwfLogCallType_Type.__name__ = "Integer32"
_IwfLogCallType_Object = MibTableColumn
iwfLogCallType = _IwfLogCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 7),
    _IwfLogCallType_Type()
)
iwfLogCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCallType.setStatus("mandatory")


class _IwfLogESN_Type(OctetString):
    """Custom type iwfLogESN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IwfLogESN_Type.__name__ = "OctetString"
_IwfLogESN_Object = MibTableColumn
iwfLogESN = _IwfLogESN_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 8),
    _IwfLogESN_Type()
)
iwfLogESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogESN.setStatus("mandatory")


class _IwfLogCallId_Type(Integer32):
    """Custom type iwfLogCallId based on Integer32"""
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
        *(("iwfQncSingleStackCall", 2),
          ("mobileIpCall", 4),
          ("pSTNCALL", 1),
          ("qncL2tpCall", 5),
          ("qncPppCall", 6),
          ("qncPptpCall", 3))
    )


_IwfLogCallId_Type.__name__ = "Integer32"
_IwfLogCallId_Object = MibTableColumn
iwfLogCallId = _IwfLogCallId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 9),
    _IwfLogCallId_Type()
)
iwfLogCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCallId.setStatus("mandatory")


class _IwfLogIMSI_Type(OctetString):
    """Custom type iwfLogIMSI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IwfLogIMSI_Type.__name__ = "OctetString"
_IwfLogIMSI_Object = MibTableColumn
iwfLogIMSI = _IwfLogIMSI_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 10),
    _IwfLogIMSI_Type()
)
iwfLogIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogIMSI.setStatus("mandatory")


class _IwfLogServiceOption_Type(Integer32):
    """Custom type iwfLogServiceOption based on Integer32"""
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
        *(("asyncDataService14dot4Kbs", 7),
          ("asyncDataServie9dot6kbs", 4),
          ("basicVoiceService", 1),
          ("enhancedRateCode", 3),
          ("group3faxService14dot4Kbs", 8),
          ("group3faxService9dot6kbs", 5),
          ("mobileLoopBack", 2),
          ("shortMessageService", 6))
    )


_IwfLogServiceOption_Type.__name__ = "Integer32"
_IwfLogServiceOption_Object = MibTableColumn
iwfLogServiceOption = _IwfLogServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 11),
    _IwfLogServiceOption_Type()
)
iwfLogServiceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogServiceOption.setStatus("mandatory")
_IwfLogDisconnectCause_Type = Integer32
_IwfLogDisconnectCause_Object = MibTableColumn
iwfLogDisconnectCause = _IwfLogDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 12),
    _IwfLogDisconnectCause_Type()
)
iwfLogDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogDisconnectCause.setStatus("mandatory")
_IwfLogMobileNumBytesTxed_Type = Integer32
_IwfLogMobileNumBytesTxed_Object = MibTableColumn
iwfLogMobileNumBytesTxed = _IwfLogMobileNumBytesTxed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 13),
    _IwfLogMobileNumBytesTxed_Type()
)
iwfLogMobileNumBytesTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogMobileNumBytesTxed.setStatus("mandatory")
_IwfLogMobileNumBytesRxed_Type = Integer32
_IwfLogMobileNumBytesRxed_Object = MibTableColumn
iwfLogMobileNumBytesRxed = _IwfLogMobileNumBytesRxed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 14),
    _IwfLogMobileNumBytesRxed_Type()
)
iwfLogMobileNumBytesRxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogMobileNumBytesRxed.setStatus("mandatory")
_IwfLogNumFaxPagesProcessed_Type = Integer32
_IwfLogNumFaxPagesProcessed_Object = MibTableColumn
iwfLogNumFaxPagesProcessed = _IwfLogNumFaxPagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 15),
    _IwfLogNumFaxPagesProcessed_Type()
)
iwfLogNumFaxPagesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogNumFaxPagesProcessed.setStatus("mandatory")


class _IwfLogCompType_Type(Integer32):
    """Custom type iwfLogCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 1),
          ("oN", 2))
    )


_IwfLogCompType_Type.__name__ = "Integer32"
_IwfLogCompType_Object = MibTableColumn
iwfLogCompType = _IwfLogCompType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 16),
    _IwfLogCompType_Type()
)
iwfLogCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCompType.setStatus("mandatory")
_IwfLogCallErrorCode_Type = Integer32
_IwfLogCallErrorCode_Object = MibTableColumn
iwfLogCallErrorCode = _IwfLogCallErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 17),
    _IwfLogCallErrorCode_Type()
)
iwfLogCallErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCallErrorCode.setStatus("mandatory")
_IwfLogModemSetupTime_Type = Integer32
_IwfLogModemSetupTime_Object = MibTableColumn
iwfLogModemSetupTime = _IwfLogModemSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 18),
    _IwfLogModemSetupTime_Type()
)
iwfLogModemSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogModemSetupTime.setStatus("mandatory")
_IwfLogCallConnectingTime_Type = Integer32
_IwfLogCallConnectingTime_Object = MibTableColumn
iwfLogCallConnectingTime = _IwfLogCallConnectingTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 19),
    _IwfLogCallConnectingTime_Type()
)
iwfLogCallConnectingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogCallConnectingTime.setStatus("mandatory")
_IwfLogTotConnectTime_Type = Integer32
_IwfLogTotConnectTime_Object = MibTableColumn
iwfLogTotConnectTime = _IwfLogTotConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 37, 1, 1, 20),
    _IwfLogTotConnectTime_Type()
)
iwfLogTotConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfLogTotConnectTime.setStatus("mandatory")
_IwfCfgQncSrv_ObjectIdentity = ObjectIdentity
iwfCfgQncSrv = _IwfCfgQncSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38)
)
_IwfCfgQncSrvTable_Object = MibTable
iwfCfgQncSrvTable = _IwfCfgQncSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1)
)
if mibBuilder.loadTexts:
    iwfCfgQncSrvTable.setStatus("mandatory")
_IwfCfgQncSrvEntry_Object = MibTableRow
iwfCfgQncSrvEntry = _IwfCfgQncSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1)
)
iwfCfgQncSrvEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfCfgQncSrvIndex"),
    (0, "IWFG-MIB", "iwfCfgQncSrvIndex2"),
)
if mibBuilder.loadTexts:
    iwfCfgQncSrvEntry.setStatus("mandatory")
_IwfCfgQncSrvIndex_Type = Integer32
_IwfCfgQncSrvIndex_Object = MibTableColumn
iwfCfgQncSrvIndex = _IwfCfgQncSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1, 1),
    _IwfCfgQncSrvIndex_Type()
)
iwfCfgQncSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgQncSrvIndex.setStatus("mandatory")
_IwfCfgQncSrvIndex2_Type = Integer32
_IwfCfgQncSrvIndex2_Object = MibTableColumn
iwfCfgQncSrvIndex2 = _IwfCfgQncSrvIndex2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1, 2),
    _IwfCfgQncSrvIndex2_Type()
)
iwfCfgQncSrvIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfCfgQncSrvIndex2.setStatus("mandatory")


class _IwfCfgQncDialedNumber_Type(DisplayString):
    """Custom type iwfCfgQncDialedNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_IwfCfgQncDialedNumber_Type.__name__ = "DisplayString"
_IwfCfgQncDialedNumber_Object = MibTableColumn
iwfCfgQncDialedNumber = _IwfCfgQncDialedNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1, 3),
    _IwfCfgQncDialedNumber_Type()
)
iwfCfgQncDialedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQncDialedNumber.setStatus("mandatory")


class _IwfCfgQncServiceType_Type(Integer32):
    """Custom type iwfCfgQncServiceType based on Integer32"""
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
        *(("notApplicable", 1),
          ("twoStackQncL2tpTunneling", 3),
          ("twoStackQncPptpTunneling", 4),
          ("twoStackQncTunneling", 2))
    )


_IwfCfgQncServiceType_Type.__name__ = "Integer32"
_IwfCfgQncServiceType_Object = MibTableColumn
iwfCfgQncServiceType = _IwfCfgQncServiceType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1, 4),
    _IwfCfgQncServiceType_Type()
)
iwfCfgQncServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQncServiceType.setStatus("mandatory")
_IwfCfgQncPrimaryIpAddress_Type = IpAddress
_IwfCfgQncPrimaryIpAddress_Object = MibTableColumn
iwfCfgQncPrimaryIpAddress = _IwfCfgQncPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1, 5),
    _IwfCfgQncPrimaryIpAddress_Type()
)
iwfCfgQncPrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQncPrimaryIpAddress.setStatus("mandatory")
_IwfCfgQncSecondaryIpAddress_Type = IpAddress
_IwfCfgQncSecondaryIpAddress_Object = MibTableColumn
iwfCfgQncSecondaryIpAddress = _IwfCfgQncSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 38, 1, 1, 6),
    _IwfCfgQncSecondaryIpAddress_Type()
)
iwfCfgQncSecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iwfCfgQncSecondaryIpAddress.setStatus("mandatory")
_IwfOprQncSrv_ObjectIdentity = ObjectIdentity
iwfOprQncSrv = _IwfOprQncSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39)
)
_IwfOprQncSrvTable_Object = MibTable
iwfOprQncSrvTable = _IwfOprQncSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1)
)
if mibBuilder.loadTexts:
    iwfOprQncSrvTable.setStatus("mandatory")
_IwfOprQncSrvEntry_Object = MibTableRow
iwfOprQncSrvEntry = _IwfOprQncSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1)
)
iwfOprQncSrvEntry.setIndexNames(
    (0, "IWFG-MIB", "iwfQncSrvIndex"),
    (0, "IWFG-MIB", "iwfQncSrvIndex2"),
)
if mibBuilder.loadTexts:
    iwfOprQncSrvEntry.setStatus("mandatory")
_IwfQncSrvIndex_Type = Integer32
_IwfQncSrvIndex_Object = MibTableColumn
iwfQncSrvIndex = _IwfQncSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1, 1),
    _IwfQncSrvIndex_Type()
)
iwfQncSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQncSrvIndex.setStatus("mandatory")
_IwfQncSrvIndex2_Type = Integer32
_IwfQncSrvIndex2_Object = MibTableColumn
iwfQncSrvIndex2 = _IwfQncSrvIndex2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1, 2),
    _IwfQncSrvIndex2_Type()
)
iwfQncSrvIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQncSrvIndex2.setStatus("mandatory")


class _IwfQncDialedNumber_Type(DisplayString):
    """Custom type iwfQncDialedNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_IwfQncDialedNumber_Type.__name__ = "DisplayString"
_IwfQncDialedNumber_Object = MibTableColumn
iwfQncDialedNumber = _IwfQncDialedNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1, 3),
    _IwfQncDialedNumber_Type()
)
iwfQncDialedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQncDialedNumber.setStatus("mandatory")


class _IwfQncServiceType_Type(Integer32):
    """Custom type iwfQncServiceType based on Integer32"""
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
        *(("notApplicable", 1),
          ("twoStackQncL2tpTunneling", 3),
          ("twoStackQncPptpTunneling", 4),
          ("twoStackQncTunneling", 2))
    )


_IwfQncServiceType_Type.__name__ = "Integer32"
_IwfQncServiceType_Object = MibTableColumn
iwfQncServiceType = _IwfQncServiceType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1, 4),
    _IwfQncServiceType_Type()
)
iwfQncServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQncServiceType.setStatus("mandatory")
_IwfQncPrimaryIpAddress_Type = IpAddress
_IwfQncPrimaryIpAddress_Object = MibTableColumn
iwfQncPrimaryIpAddress = _IwfQncPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1, 5),
    _IwfQncPrimaryIpAddress_Type()
)
iwfQncPrimaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQncPrimaryIpAddress.setStatus("mandatory")
_IwfQncSecondaryIpAddress_Type = IpAddress
_IwfQncSecondaryIpAddress_Object = MibTableColumn
iwfQncSecondaryIpAddress = _IwfQncSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 25, 39, 1, 1, 6),
    _IwfQncSecondaryIpAddress_Type()
)
iwfQncSecondaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwfQncSecondaryIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IWFG-MIB",
    **{"usr": usr,
       "nas": nas,
       "iwfGWY": iwfGWY,
       "iwfCfgFrRly": iwfCfgFrRly,
       "iwfCfgFrRlyTable": iwfCfgFrRlyTable,
       "iwfCfgFrRlyEntry": iwfCfgFrRlyEntry,
       "iwfCfgFrRlyIndex": iwfCfgFrRlyIndex,
       "iwfCfgFrRlyT391StatusEnqryTimr": iwfCfgFrRlyT391StatusEnqryTimr,
       "iwfCfgFrRlyT392StatusTimer": iwfCfgFrRlyT392StatusTimer,
       "iwfCfgFrRlyN391StatusEnqrySent": iwfCfgFrRlyN391StatusEnqrySent,
       "iwfCfgQ921": iwfCfgQ921,
       "iwfCfgQ921Table": iwfCfgQ921Table,
       "iwfCfgQ921Entry": iwfCfgQ921Entry,
       "iwfCfgQ921Index": iwfCfgQ921Index,
       "iwfCfgQ921KmaxOutStandPkt": iwfCfgQ921KmaxOutStandPkt,
       "iwfCfgQ921T200IframeAckTimer": iwfCfgQ921T200IframeAckTimer,
       "iwfCfgQ921T203MaxTimeNoIframe": iwfCfgQ921T203MaxTimeNoIframe,
       "iwfCfgQ921N200MaxFrameRetrans": iwfCfgQ921N200MaxFrameRetrans,
       "iwfCfgQ921N201RxMaxOctetInfo": iwfCfgQ921N201RxMaxOctetInfo,
       "iwfCfgQ921N201TxMaxOctetInfo": iwfCfgQ921N201TxMaxOctetInfo,
       "iwfCfgQ933": iwfCfgQ933,
       "iwfCfgQ933Table": iwfCfgQ933Table,
       "iwfCfgQ933Entry": iwfCfgQ933Entry,
       "iwfCfgQ933Index": iwfCfgQ933Index,
       "iwfCfgQ933T303SetupTimer": iwfCfgQ933T303SetupTimer,
       "iwfCfgQ933T305DisconnectTimer": iwfCfgQ933T305DisconnectTimer,
       "iwfCfgQ933T308ReleaseTimer": iwfCfgQ933T308ReleaseTimer,
       "iwfCfgQ933T309DataLinkDiscTimr": iwfCfgQ933T309DataLinkDiscTimr,
       "iwfCfgQ933T310CallProceedTimer": iwfCfgQ933T310CallProceedTimer,
       "iwfCfgQ933T313ConnectSentTimer": iwfCfgQ933T313ConnectSentTimer,
       "iwfCfgCallStats": iwfCfgCallStats,
       "iwfCfgCallStatsTable": iwfCfgCallStatsTable,
       "iwfCfgCallStatsEntry": iwfCfgCallStatsEntry,
       "iwfCfgCsIndex": iwfCfgCsIndex,
       "iwfCfgCsMobOrigAdStats": iwfCfgCsMobOrigAdStats,
       "iwfCfgCsMobOrigFaxStats": iwfCfgCsMobOrigFaxStats,
       "iwfCfgCsMobTermAdStats": iwfCfgCsMobTermAdStats,
       "iwfCfgCsMobTermFaxStats": iwfCfgCsMobTermFaxStats,
       "iwfCfgCsLogStartTrapEna": iwfCfgCsLogStartTrapEna,
       "iwfCfgCsLogTermTrapEna": iwfCfgCsLogTermTrapEna,
       "iwfCfgPppParam": iwfCfgPppParam,
       "iwfCfgPppParamTable": iwfCfgPppParamTable,
       "iwfCfgPppParamEntry": iwfCfgPppParamEntry,
       "iwfCfgPppIndex": iwfCfgPppIndex,
       "iwfCfgPppForceEncryptData": iwfCfgPppForceEncryptData,
       "iwfCfgPppForceEncryptpassword": iwfCfgPppForceEncryptpassword,
       "iwfCfgPppMaxNumbConfigRequests": iwfCfgPppMaxNumbConfigRequests,
       "iwfCfgPppMaxNumbConfigNAK": iwfCfgPppMaxNumbConfigNAK,
       "iwfCfgPppMaxNumbRejects": iwfCfgPppMaxNumbRejects,
       "iwfCfgPppMaxNumbTermRequests": iwfCfgPppMaxNumbTermRequests,
       "iwfCfgPppNegotiateTime": iwfCfgPppNegotiateTime,
       "iwfCfgPppRestartTime": iwfCfgPppRestartTime,
       "iwfCfgPppIpAddressPoolMax": iwfCfgPppIpAddressPoolMax,
       "iwfCfgPppIpAddressPoolMin": iwfCfgPppIpAddressPoolMin,
       "iwfCfgTcpIp": iwfCfgTcpIp,
       "iwfCfgTcpIpTable": iwfCfgTcpIpTable,
       "iwfCfgTcpIpEntry": iwfCfgTcpIpEntry,
       "iwfCfgTiIndex": iwfCfgTiIndex,
       "iwfCfgTiDefaultServiceType": iwfCfgTiDefaultServiceType,
       "iwfCfgTiDefaultTimeToLive": iwfCfgTiDefaultTimeToLive,
       "iwfCfgTiMtuDiscovery": iwfCfgTiMtuDiscovery,
       "iwfCfgTiKeepAliveInterval": iwfCfgTiKeepAliveInterval,
       "iwfCfgTiKeepAliveTime": iwfCfgTiKeepAliveTime,
       "iwfCfgTiMaxMtuSize": iwfCfgTiMaxMtuSize,
       "iwfCfgTiMaxConnectReTrans": iwfCfgTiMaxConnectReTrans,
       "iwfCfgTiMaxDataRetrans": iwfCfgTiMaxDataRetrans,
       "iwfCfgTiMaxNumberConnections": iwfCfgTiMaxNumberConnections,
       "iwfCfgTiWindowSize": iwfCfgTiWindowSize,
       "iwfCfgTiLocalIpAddress": iwfCfgTiLocalIpAddress,
       "iwfCfgTiSubnetIpMask": iwfCfgTiSubnetIpMask,
       "iwfCfgTiDefualtGatewayIp": iwfCfgTiDefualtGatewayIp,
       "iwfEthernetNicStat": iwfEthernetNicStat,
       "iwfEthernetNicStatTable": iwfEthernetNicStatTable,
       "iwfEthernetNicStatEntry": iwfEthernetNicStatEntry,
       "iwfEnsIndex": iwfEnsIndex,
       "iwfEnsPacketsRxPerSec": iwfEnsPacketsRxPerSec,
       "iwfEnsPacketsTxPerSec": iwfEnsPacketsTxPerSec,
       "iwfEnsBytesRxPerSec": iwfEnsBytesRxPerSec,
       "iwfEnsBytesTxPerSec": iwfEnsBytesTxPerSec,
       "iwfEnsPacketsRxErrors": iwfEnsPacketsRxErrors,
       "iwfEnsPacketsRxUnknown": iwfEnsPacketsRxUnknown,
       "iwfEnsPacketsOutBoundDiscarded": iwfEnsPacketsOutBoundDiscarded,
       "iwfEnsPacketsOutBoundErrors": iwfEnsPacketsOutBoundErrors,
       "iwfEnsOutputQueueLength": iwfEnsOutputQueueLength,
       "iwfIpStats": iwfIpStats,
       "iwfIpStatsTable": iwfIpStatsTable,
       "iwfIpStatsEntry": iwfIpStatsEntry,
       "iwfIsIndex": iwfIsIndex,
       "iwfIsPacketsRx": iwfIsPacketsRx,
       "iwfIsRxHeaderErrors": iwfIsRxHeaderErrors,
       "iwfIsIpReceived": iwfIsIpReceived,
       "iwfIsDatagramsForwarded": iwfIsDatagramsForwarded,
       "iwfIsUnknownProtocolRx": iwfIsUnknownProtocolRx,
       "iwfIsRxPacketsDiscarded": iwfIsRxPacketsDiscarded,
       "iwfIsRxPacketsDelivered": iwfIsRxPacketsDelivered,
       "iwfIsOutputRequests": iwfIsOutputRequests,
       "iwfIsRoutingDiscarded": iwfIsRoutingDiscarded,
       "iwfIsDiscardedOutputPackets": iwfIsDiscardedOutputPackets,
       "iwfIsOutputPacketsNoRoute": iwfIsOutputPacketsNoRoute,
       "iwfIsReAssemblyRequired": iwfIsReAssemblyRequired,
       "iwfIsReAssemblySuccessful": iwfIsReAssemblySuccessful,
       "iwfIsReAssmeblyFailures": iwfIsReAssmeblyFailures,
       "iwfIsDatagramsSuccessFragment": iwfIsDatagramsSuccessFragment,
       "iwfIsDatagramsFailFragment": iwfIsDatagramsFailFragment,
       "iwfIsFragmentCreated": iwfIsFragmentCreated,
       "iwfIcmpStats": iwfIcmpStats,
       "iwfIcmpStatsTable": iwfIcmpStatsTable,
       "iwfIcmpStatsEntry": iwfIcmpStatsEntry,
       "iwfIcmpStIndex": iwfIcmpStIndex,
       "iwfIcmpStMessagesRx": iwfIcmpStMessagesRx,
       "iwfIcmpStMessagesTx": iwfIcmpStMessagesTx,
       "iwfIcmpStErrorsRx": iwfIcmpStErrorsRx,
       "iwfIcmpStErrorsTx": iwfIcmpStErrorsTx,
       "iwfIcmpStDestUnreachableTx": iwfIcmpStDestUnreachableTx,
       "iwfIcmpStDestUnreachableRx": iwfIcmpStDestUnreachableRx,
       "iwfIcmpStTimeExceededTx": iwfIcmpStTimeExceededTx,
       "iwfIcmpStTimeExceededRx": iwfIcmpStTimeExceededRx,
       "iwfIcmpStParameterProblemsTx": iwfIcmpStParameterProblemsTx,
       "iwfIcmpStParameterProblemsRx": iwfIcmpStParameterProblemsRx,
       "iwfIcmpStSourceQuenchsTx": iwfIcmpStSourceQuenchsTx,
       "iwfIcmpStSourceQuenchsRx": iwfIcmpStSourceQuenchsRx,
       "iwfIcmpStRedirectsTx": iwfIcmpStRedirectsTx,
       "iwfIcmpStRedirectsRx": iwfIcmpStRedirectsRx,
       "iwfIcmpStEchosTx": iwfIcmpStEchosTx,
       "iwfIcmpStEchosRx": iwfIcmpStEchosRx,
       "iwfIcmpStEchosRepliesTx": iwfIcmpStEchosRepliesTx,
       "iwfIcmpStEchosRepliesRx": iwfIcmpStEchosRepliesRx,
       "iwfIcmpStTimeStampsTx": iwfIcmpStTimeStampsTx,
       "iwfIcmpStTimeStampsRx": iwfIcmpStTimeStampsRx,
       "iwfIcmpStAddressMasksTx": iwfIcmpStAddressMasksTx,
       "iwfIcmpStAddressMasksRx": iwfIcmpStAddressMasksRx,
       "iwfIcmpStAddressMasksRepliesTx": iwfIcmpStAddressMasksRepliesTx,
       "iwfIcmpStAddressMasksRepliesRx": iwfIcmpStAddressMasksRepliesRx,
       "iwfTcpStats": iwfTcpStats,
       "iwfTcpStatsTable": iwfTcpStatsTable,
       "iwfTcpStatsEntry": iwfTcpStatsEntry,
       "iwfTcpStIndex": iwfTcpStIndex,
       "iwfTcpStActiveOpens": iwfTcpStActiveOpens,
       "iwfTcpStPassiveOpens": iwfTcpStPassiveOpens,
       "iwfTcpStFailedConnectAttempts": iwfTcpStFailedConnectAttempts,
       "iwfTcpStResetConnections": iwfTcpStResetConnections,
       "iwfTcpStCurrentConnections": iwfTcpStCurrentConnections,
       "iwfTcpStSegmentRx": iwfTcpStSegmentRx,
       "iwfTcpStSegmentTx": iwfTcpStSegmentTx,
       "iwfTcpStSegmentRetransmitted": iwfTcpStSegmentRetransmitted,
       "iwfUdpStats": iwfUdpStats,
       "iwfUdpStatsTable": iwfUdpStatsTable,
       "iwfUdpStatsEntry": iwfUdpStatsEntry,
       "iwfUdpStIndex": iwfUdpStIndex,
       "iwfUdpStDatagramRx": iwfUdpStDatagramRx,
       "iwfUdpStDatagramNoPorts": iwfUdpStDatagramNoPorts,
       "iwfUdpStErrorsRx": iwfUdpStErrorsRx,
       "iwfUdpStDatagramtx": iwfUdpStDatagramtx,
       "iwfPppStats": iwfPppStats,
       "iwfPppStatsTable": iwfPppStatsTable,
       "iwfPppStatsEntry": iwfPppStatsEntry,
       "iwfPppStIndex": iwfPppStIndex,
       "iwfPppStBytesTx": iwfPppStBytesTx,
       "iwfPppStBytesRx": iwfPppStBytesRx,
       "iwfPppStFramesTx": iwfPppStFramesTx,
       "iwfPppStFramesRx": iwfPppStFramesRx,
       "iwfPppStPercentCompressionOut": iwfPppStPercentCompressionOut,
       "iwfPppStPercentCompressionIn": iwfPppStPercentCompressionIn,
       "iwfPppStCrcErrors": iwfPppStCrcErrors,
       "iwfPppStAlignmentErrors": iwfPppStAlignmentErrors,
       "iwfPppStTimeOutErrors": iwfPppStTimeOutErrors,
       "iwfPppStTotalErrors": iwfPppStTotalErrors,
       "iwfPppStBytesTxPerSec": iwfPppStBytesTxPerSec,
       "iwfPppStBytesRxPerSec": iwfPppStBytesRxPerSec,
       "iwfPppStFramesTxPerSec": iwfPppStFramesTxPerSec,
       "iwfPppStFramesRxPerSec": iwfPppStFramesRxPerSec,
       "iwfPppStTotalErrorPerSec": iwfPppStTotalErrorPerSec,
       "iwfPppStTotalConnections": iwfPppStTotalConnections,
       "iwfTdmStats": iwfTdmStats,
       "iwfTdmStatsTable": iwfTdmStatsTable,
       "iwfTdmStatsEntry": iwfTdmStatsEntry,
       "iwfTdmStIndex": iwfTdmStIndex,
       "iwfTdmStFramesOverruns": iwfTdmStFramesOverruns,
       "iwfTdmStAbortFramesrx": iwfTdmStAbortFramesrx,
       "iwfTdmStCrcErrors": iwfTdmStCrcErrors,
       "iwfTdmStClockLossis": iwfTdmStClockLossis,
       "iwfTdmStAccumSubsystemErrors": iwfTdmStAccumSubsystemErrors,
       "iwfTdmStClkStatus": iwfTdmStClkStatus,
       "iwfPbStats": iwfPbStats,
       "iwfPbStatsTable": iwfPbStatsTable,
       "iwfPbStatsEntry": iwfPbStatsEntry,
       "iwfPbStIndex": iwfPbStIndex,
       "iwfPbStFramesOverruns": iwfPbStFramesOverruns,
       "iwfPbStAbortFramesrx": iwfPbStAbortFramesrx,
       "iwfPbStCrcErrors": iwfPbStCrcErrors,
       "iwfPbStClockLosses": iwfPbStClockLosses,
       "iwfPbStAccumSubsystemErrors": iwfPbStAccumSubsystemErrors,
       "iwfPbStClkStatus": iwfPbStClkStatus,
       "iwfPbStLinkLosses": iwfPbStLinkLosses,
       "iwfQ921Stats": iwfQ921Stats,
       "iwfQ921StatsTable": iwfQ921StatsTable,
       "iwfQ921StatsEntry": iwfQ921StatsEntry,
       "iwfQ921StIndex": iwfQ921StIndex,
       "iwfQ921StAccumLinkLosses": iwfQ921StAccumLinkLosses,
       "iwfQ921StAccumFrsvcSusSysError": iwfQ921StAccumFrsvcSusSysError,
       "iwfQ933Stats": iwfQ933Stats,
       "iwfQ933StatsTable": iwfQ933StatsTable,
       "iwfQ933StatsEntry": iwfQ933StatsEntry,
       "iwfQ933StIndex": iwfQ933StIndex,
       "iwfQ933StAccumUknownIframes": iwfQ933StAccumUknownIframes,
       "iwfQ933StAccumOutOfSeqIframes": iwfQ933StAccumOutOfSeqIframes,
       "iwfMdmStats": iwfMdmStats,
       "iwfMdmStatsTable": iwfMdmStatsTable,
       "iwfMdmStatsEntry": iwfMdmStatsEntry,
       "iwfMdmStIndex": iwfMdmStIndex,
       "iwfMdmStAccumInvalidAtCmd": iwfMdmStAccumInvalidAtCmd,
       "iwfCmpStats": iwfCmpStats,
       "iwfCmpStatsTable": iwfCmpStatsTable,
       "iwfCmpStatsEntry": iwfCmpStatsEntry,
       "iwfCmpStIndex": iwfCmpStIndex,
       "iwfCmpStAccumSubsysErrors": iwfCmpStAccumSubsysErrors,
       "iwfCallStats": iwfCallStats,
       "iwfCallStatsTable": iwfCallStatsTable,
       "iwfCallStatsEntry": iwfCallStatsEntry,
       "iwfCallStIndex": iwfCallStIndex,
       "iwfCallStTotConnAd9600MobOrg": iwfCallStTotConnAd9600MobOrg,
       "iwfCallStTotConnAd14400MobOrg": iwfCallStTotConnAd14400MobOrg,
       "iwfCallStTotConnFax9600MobOrg": iwfCallStTotConnFax9600MobOrg,
       "iwfCallStTotConnFax14400MobOrg": iwfCallStTotConnFax14400MobOrg,
       "iwfCallStTotConnAd9600MoTerm": iwfCallStTotConnAd9600MoTerm,
       "iwfCallStTotConnAd14400MoTerm": iwfCallStTotConnAd14400MoTerm,
       "iwfCallStTotConnFax9600MoTerm": iwfCallStTotConnFax9600MoTerm,
       "iwfCallStTotConnFax14400MoTerm": iwfCallStTotConnFax14400MoTerm,
       "iwfCallStTotTermAd9600MoOrg": iwfCallStTotTermAd9600MoOrg,
       "iwfCallStTotTermAd14400MoOrg": iwfCallStTotTermAd14400MoOrg,
       "iwfCallStTotTermFax9600MoOrg": iwfCallStTotTermFax9600MoOrg,
       "iwfCallStTotTermFax14400MoOrg": iwfCallStTotTermFax14400MoOrg,
       "iwfCallStTotTermAd9600MoTerm": iwfCallStTotTermAd9600MoTerm,
       "iwfCallStTotTermAd14400MoTerm": iwfCallStTotTermAd14400MoTerm,
       "iwfCallStTotTermFax9600MoTerm": iwfCallStTotTermFax9600MoTerm,
       "iwfCallStTotTermFax14400MoTerm": iwfCallStTotTermFax14400MoTerm,
       "iwfCallStTotCntgAd9600MoOrg": iwfCallStTotCntgAd9600MoOrg,
       "iwfCallStTotCntgAd14400MoOrg": iwfCallStTotCntgAd14400MoOrg,
       "iwfCallStTotCntgFax9600MoOrg": iwfCallStTotCntgFax9600MoOrg,
       "iwfCallStTotCntgFax14400MoOrg": iwfCallStTotCntgFax14400MoOrg,
       "iwfCallStTotCntgAd9600MoTerm": iwfCallStTotCntgAd9600MoTerm,
       "iwfCallStTotCntgAd14400MoTerm": iwfCallStTotCntgAd14400MoTerm,
       "iwfCallStTotCntgFax9600MoTerm": iwfCallStTotCntgFax9600MoTerm,
       "iwfCallStTotCntgFax14400MoTerm": iwfCallStTotCntgFax14400MoTerm,
       "iwfCallStTotDiscAd9600MoOrg": iwfCallStTotDiscAd9600MoOrg,
       "iwfCallStTotDiscAd14400MoOrg": iwfCallStTotDiscAd14400MoOrg,
       "iwfCallStTotDiscFax9600MoOrg": iwfCallStTotDiscFax9600MoOrg,
       "iwfCallStTotDiscFax14400MoOrg": iwfCallStTotDiscFax14400MoOrg,
       "iwfCallStTotDiscAd9600MoTerm": iwfCallStTotDiscAd9600MoTerm,
       "iwfCallStTotDiscAd14400MoTerm": iwfCallStTotDiscAd14400MoTerm,
       "iwfCallStTotDiscFax9600MoTerm": iwfCallStTotDiscFax9600MoTerm,
       "iwfCallStTotDiscFax14400MoTerm": iwfCallStTotDiscFax14400MoTerm,
       "iwfCallStTotCompv42MoOrg": iwfCallStTotCompv42MoOrg,
       "iwfCallStTotCompMmrMoOrg": iwfCallStTotCompMmrMoOrg,
       "iwfCallStTotCompv42MoTerm": iwfCallStTotCompv42MoTerm,
       "iwfCallStTotCompMmrMoTerm": iwfCallStTotCompMmrMoTerm,
       "iwfCallStTotFailAd9600MoOrg": iwfCallStTotFailAd9600MoOrg,
       "iwfCallStTotFailAd14400MoOrg": iwfCallStTotFailAd14400MoOrg,
       "iwfCallStTotFailFax9600MoOrg": iwfCallStTotFailFax9600MoOrg,
       "iwfCallStTotFailFax14400MoOrg": iwfCallStTotFailFax14400MoOrg,
       "iwfCallStTotFailAd9600MoTerm": iwfCallStTotFailAd9600MoTerm,
       "iwfCallStTotFailAd14400MoTerm": iwfCallStTotFailAd14400MoTerm,
       "iwfCallStTotFailFax9600MoTerm": iwfCallStTotFailFax9600MoTerm,
       "iwfCallStTotFailFax14400MoTerm": iwfCallStTotFailFax14400MoTerm,
       "iwfCallStCurrentNumConnCalls": iwfCallStCurrentNumConnCalls,
       "iwfCallStCurrentNumCompCalls": iwfCallStCurrentNumCompCalls,
       "iwfCallStQncConnectedSs9600": iwfCallStQncConnectedSs9600,
       "iwfCallStQncConnectedL2tp9600": iwfCallStQncConnectedL2tp9600,
       "iwfCallStQncConnectedPptp9600": iwfCallStQncConnectedPptp9600,
       "iwfCallStQncConnectedPpp9600": iwfCallStQncConnectedPpp9600,
       "iwfCallStQncTerminatedSs9600": iwfCallStQncTerminatedSs9600,
       "iwfCallStQncTerminatedL2tp9600": iwfCallStQncTerminatedL2tp9600,
       "iwfCallStQncTerminatedPptp9600": iwfCallStQncTerminatedPptp9600,
       "iwfCallStQncTerminatedPpp9600": iwfCallStQncTerminatedPpp9600,
       "iwfCallStQncConnectingSs9600": iwfCallStQncConnectingSs9600,
       "iwfCallStQncConnectingL2tp9600": iwfCallStQncConnectingL2tp9600,
       "iwfCallStQncConnectingPptp9600": iwfCallStQncConnectingPptp9600,
       "iwfCallStQncConnectingPpp9600": iwfCallStQncConnectingPpp9600,
       "iwfCallStQncDisconnectingSs9600": iwfCallStQncDisconnectingSs9600,
       "iwfCallStQncDisconnectingL2tp9600": iwfCallStQncDisconnectingL2tp9600,
       "iwfCallStQncDisconnectingPptp9600": iwfCallStQncDisconnectingPptp9600,
       "iwfCallStQncDisconnectingPpp9600": iwfCallStQncDisconnectingPpp9600,
       "iwfCallStQncConnectedSs14400": iwfCallStQncConnectedSs14400,
       "iwfCallStQncConnectedL2tp14400": iwfCallStQncConnectedL2tp14400,
       "iwfCallStQncConnectedPptp14400": iwfCallStQncConnectedPptp14400,
       "iwfCallStQncConnectedPpp14400": iwfCallStQncConnectedPpp14400,
       "iwfCallStQncTerminatedSs14400": iwfCallStQncTerminatedSs14400,
       "iwfCallStQncTerminatedL2tp14400": iwfCallStQncTerminatedL2tp14400,
       "iwfCallStQncTerminatedPptp14400": iwfCallStQncTerminatedPptp14400,
       "iwfCallStQncTerminatedPpp14400": iwfCallStQncTerminatedPpp14400,
       "iwfCallStQncConnectingSs14400": iwfCallStQncConnectingSs14400,
       "iwfCallStQncConnectingL2tp14400": iwfCallStQncConnectingL2tp14400,
       "iwfCallStQncConnectingPptp14400": iwfCallStQncConnectingPptp14400,
       "iwfCallStQncConnectingPpp14400": iwfCallStQncConnectingPpp14400,
       "iwfCallStQncDiscconnectingSs14400": iwfCallStQncDiscconnectingSs14400,
       "iwfCallStQncDiscconnectingL2tp14400": iwfCallStQncDiscconnectingL2tp14400,
       "iwfCallStQncDiscconnectingPptp14400": iwfCallStQncDiscconnectingPptp14400,
       "iwfCallStQncDiscconnectingPpp14400": iwfCallStQncDiscconnectingPpp14400,
       "iwfCfgTdmTrap": iwfCfgTdmTrap,
       "iwfCfgTdmTrapTable": iwfCfgTdmTrapTable,
       "iwfCfgTdmTrapEntry": iwfCfgTdmTrapEntry,
       "iwfTdmTrIndex": iwfTdmTrIndex,
       "iwfTdmTrChanMrgOperStatus": iwfTdmTrChanMrgOperStatus,
       "iwfTdmTrChanNonOperStatus": iwfTdmTrChanNonOperStatus,
       "iwfTdmTrChanClearStatus": iwfTdmTrChanClearStatus,
       "iwfTdmTrChanMrgOperBitMask": iwfTdmTrChanMrgOperBitMask,
       "iwfTdmTrChanMrgOperThreshCnt": iwfTdmTrChanMrgOperThreshCnt,
       "iwfTdmTrChanNonOperThreshCnt": iwfTdmTrChanNonOperThreshCnt,
       "iwfTdmTrChanClearThreshCnt": iwfTdmTrChanClearThreshCnt,
       "iwfTdmTrChanMrgOperThreshTime": iwfTdmTrChanMrgOperThreshTime,
       "iwfTdmTrChanNonOperThreshTime": iwfTdmTrChanNonOperThreshTime,
       "iwfTdmTrChanClearThreshTime": iwfTdmTrChanClearThreshTime,
       "iwfTdmTrChCrcErrCnt": iwfTdmTrChCrcErrCnt,
       "iwfTdmTrChAbortErrCnt": iwfTdmTrChAbortErrCnt,
       "iwfTdmTrChFrameOverflowCnt": iwfTdmTrChFrameOverflowCnt,
       "iwfTdmTrStatus": iwfTdmTrStatus,
       "iwfTdmTrTdmChannel": iwfTdmTrTdmChannel,
       "iwfTdmTrMunichChip": iwfTdmTrMunichChip,
       "iwfTdmTrMunichChannel": iwfTdmTrMunichChannel,
       "iwfCfgTdmSsTrap": iwfCfgTdmSsTrap,
       "iwfCfgTdmSsTrapTable": iwfCfgTdmSsTrapTable,
       "iwfCfgTdmSsTrapEntry": iwfCfgTdmSsTrapEntry,
       "iwfCfgTdmSsTrIndex": iwfCfgTdmSsTrIndex,
       "iwfTdmSsTrMrgOperStatus": iwfTdmSsTrMrgOperStatus,
       "iwfTdmSsTrNonOperStatus": iwfTdmSsTrNonOperStatus,
       "iwfTdmSsTrClearStatus": iwfTdmSsTrClearStatus,
       "iwfTdmSsTrMrgOperThreshCnt": iwfTdmSsTrMrgOperThreshCnt,
       "iwfTdmSsTrNonOperThreshCnt": iwfTdmSsTrNonOperThreshCnt,
       "iwfTdmSsTrClearThreshCnt": iwfTdmSsTrClearThreshCnt,
       "iwfTdmSsTrMrgOperThreshTime": iwfTdmSsTrMrgOperThreshTime,
       "iwfTdmSsTrNonOperThreshTime": iwfTdmSsTrNonOperThreshTime,
       "iwfTdmSsTrClearThreshTime": iwfTdmSsTrClearThreshTime,
       "iwfTdmSsTrStatus": iwfTdmSsTrStatus,
       "iwfCfgPbTrap": iwfCfgPbTrap,
       "iwfCfgPbTrapTable": iwfCfgPbTrapTable,
       "iwfCfgPbTrapEntry": iwfCfgPbTrapEntry,
       "iwfPbTrIndex": iwfPbTrIndex,
       "iwfPbTrChanMrgOperStatus": iwfPbTrChanMrgOperStatus,
       "iwfPbTrChanNonOperStatus": iwfPbTrChanNonOperStatus,
       "iwfPbTrChanClearStatus": iwfPbTrChanClearStatus,
       "iwfPbTrChanMrgOperBitMask": iwfPbTrChanMrgOperBitMask,
       "iwfPbTrChanMrgOperThreshCnt": iwfPbTrChanMrgOperThreshCnt,
       "iwfPbTrChanNonOperThreshCnt": iwfPbTrChanNonOperThreshCnt,
       "iwfPbTrChanClearThreshCnt": iwfPbTrChanClearThreshCnt,
       "iwfPbTrChanMrgOperThreshTime": iwfPbTrChanMrgOperThreshTime,
       "iwfPbTrChanNonOperThreshTime": iwfPbTrChanNonOperThreshTime,
       "iwfPbTrChanClearThreshTime": iwfPbTrChanClearThreshTime,
       "iwfPbTrChCrcErrCnt": iwfPbTrChCrcErrCnt,
       "iwfPbTrChAbortErrCnt": iwfPbTrChAbortErrCnt,
       "iwfPbTrChFrameOverflowCnt": iwfPbTrChFrameOverflowCnt,
       "iwfPbTrChStatus": iwfPbTrChStatus,
       "iwfPbTrModemSlot": iwfPbTrModemSlot,
       "iwfPbTrModemChannel": iwfPbTrModemChannel,
       "iwfCfgPbSsTrap": iwfCfgPbSsTrap,
       "iwfCfgPbSsTrapTable": iwfCfgPbSsTrapTable,
       "iwfCfgPbSsTrapEntry": iwfCfgPbSsTrapEntry,
       "iwfPbSsTrIndex": iwfPbSsTrIndex,
       "iwfPbSsTrMrgOperStatus": iwfPbSsTrMrgOperStatus,
       "iwfPbSsTrNonOperStatus": iwfPbSsTrNonOperStatus,
       "iwfPbSsTrClearStatus": iwfPbSsTrClearStatus,
       "iwfPbSsTrMrgOperThreshCnt": iwfPbSsTrMrgOperThreshCnt,
       "iwfPbSsTrNonOperThreshCnt": iwfPbSsTrNonOperThreshCnt,
       "iwfPbSsTrClearThreshCnt": iwfPbSsTrClearThreshCnt,
       "iwfPbSsTrMrgOperThreshTime": iwfPbSsTrMrgOperThreshTime,
       "iwfPbSsTrNonOperThreshTime": iwfPbSsTrNonOperThreshTime,
       "iwfPbSsTrClearThreshtime": iwfPbSsTrClearThreshtime,
       "iwfPbSsTrStatus": iwfPbSsTrStatus,
       "iwfCfgPbClkTrap": iwfCfgPbClkTrap,
       "iwfCfgPbClkTrapTable": iwfCfgPbClkTrapTable,
       "iwfCfgPbClkTrapEntry": iwfCfgPbClkTrapEntry,
       "iwfPbClkTrIndex": iwfPbClkTrIndex,
       "iwfPbClkTrNonOperStatus": iwfPbClkTrNonOperStatus,
       "iwfPbClkTrClearStatus": iwfPbClkTrClearStatus,
       "iwfPbClkTrNonOperThreshTimer": iwfPbClkTrNonOperThreshTimer,
       "iwfCfgTdmClkTrap": iwfCfgTdmClkTrap,
       "iwfCfgTdmClkTrapTable": iwfCfgTdmClkTrapTable,
       "iwfCfgTdmClkTrapEntry": iwfCfgTdmClkTrapEntry,
       "iwfTdmClkTrIndex": iwfTdmClkTrIndex,
       "iwfTdmClkTrNonOperStatus": iwfTdmClkTrNonOperStatus,
       "iwfTdmClkTrClearStatus": iwfTdmClkTrClearStatus,
       "iwfTdmClkTrNonOperThreshTimer": iwfTdmClkTrNonOperThreshTimer,
       "iwfCfgCcSsTrap": iwfCfgCcSsTrap,
       "iwfCfgCcSsTrapTable": iwfCfgCcSsTrapTable,
       "iwfCfgCcSsTrapEntry": iwfCfgCcSsTrapEntry,
       "iwfCcSsTrIndex": iwfCcSsTrIndex,
       "iwfCcSsTrMrgOperStatus": iwfCcSsTrMrgOperStatus,
       "iwfCcSsTrNonOperStatus": iwfCcSsTrNonOperStatus,
       "iwfCcSsTrClearStatus": iwfCcSsTrClearStatus,
       "iwfCcSsTrMrgOperBitMask": iwfCcSsTrMrgOperBitMask,
       "iwfCcSsTrMrgOperThreshCnt": iwfCcSsTrMrgOperThreshCnt,
       "iwfCcSsTrNonOperThreshCnt": iwfCcSsTrNonOperThreshCnt,
       "iwfCcSsTrClearThreshCnt": iwfCcSsTrClearThreshCnt,
       "iwfCcSsTrMrgOperThreshTimer": iwfCcSsTrMrgOperThreshTimer,
       "iwfCcSsTrNonOperThreshTimer": iwfCcSsTrNonOperThreshTimer,
       "iwfCcSsTrClearThreshTimer": iwfCcSsTrClearThreshTimer,
       "iwfCcSsTrAd9600NoSysResCnt": iwfCcSsTrAd9600NoSysResCnt,
       "iwfCcSsTrAd14400NoSysResCnt": iwfCcSsTrAd14400NoSysResCnt,
       "iwfCcSsTrFax9600NoSysResCnt": iwfCcSsTrFax9600NoSysResCnt,
       "iwfCcSsTrFax14400NoSysResCnt": iwfCcSsTrFax14400NoSysResCnt,
       "iwfCcSsTrAd9600SktErrCnt": iwfCcSsTrAd9600SktErrCnt,
       "iwfCcSsTrAd14400SktErrCnt": iwfCcSsTrAd14400SktErrCnt,
       "iwfCcSsTrFax9600SktErrCnt": iwfCcSsTrFax9600SktErrCnt,
       "iwfCcSsTrFax14400SktErrCnt": iwfCcSsTrFax14400SktErrCnt,
       "iwfCcSsTrAd9600PrtErrCnt": iwfCcSsTrAd9600PrtErrCnt,
       "iwfCcSsTrAd14400PrtErrCnt": iwfCcSsTrAd14400PrtErrCnt,
       "iwfCcSsTrFax9600PrtErrCnt": iwfCcSsTrFax9600PrtErrCnt,
       "iwfCcSsTrFax14400PrtErrCnt": iwfCcSsTrFax14400PrtErrCnt,
       "iwfCcSsTrAd9600NoMdmResCnt": iwfCcSsTrAd9600NoMdmResCnt,
       "iwfCcSsTrAd14400NoMdmResCnt": iwfCcSsTrAd14400NoMdmResCnt,
       "iwfCcSsTrFax9600NoMdmResCnt": iwfCcSsTrFax9600NoMdmResCnt,
       "iwfCcSsTrFax14400NoMdmResCnt": iwfCcSsTrFax14400NoMdmResCnt,
       "iwfCcSsTrNoResponse": iwfCcSsTrNoResponse,
       "iwfCcSsTrStatus": iwfCcSsTrStatus,
       "iwfCfgDxSsTrap": iwfCfgDxSsTrap,
       "iwfCfgDxSsTrapTable": iwfCfgDxSsTrapTable,
       "iwfCfgDxSsTrapEntry": iwfCfgDxSsTrapEntry,
       "iwfDxSsTrIndex": iwfDxSsTrIndex,
       "iwfDxSsTrMrgOperStatus": iwfDxSsTrMrgOperStatus,
       "iwfDxSsTrNonOperStatus": iwfDxSsTrNonOperStatus,
       "iwfDxSsTrClearStatus": iwfDxSsTrClearStatus,
       "iwfDxSsTrMrgOperBitMask": iwfDxSsTrMrgOperBitMask,
       "iwfDxSsTrMrgOperThreshCnt": iwfDxSsTrMrgOperThreshCnt,
       "iwfDxSsTrNonOperThreshCnt": iwfDxSsTrNonOperThreshCnt,
       "iwfDxSsTrClearThreshCnt": iwfDxSsTrClearThreshCnt,
       "iwfDxSsTrMrgOperThreshTimer": iwfDxSsTrMrgOperThreshTimer,
       "iwfDxSsTrNonOperThreshTimer": iwfDxSsTrNonOperThreshTimer,
       "iwfDxSsTrClearThreshTimer": iwfDxSsTrClearThreshTimer,
       "iwfDxSsTrAd9600NoSysResCnt": iwfDxSsTrAd9600NoSysResCnt,
       "iwfDxSsTrAd14400NoSysResCnt": iwfDxSsTrAd14400NoSysResCnt,
       "iwfDxSsTrFax9600NoSysResCnt": iwfDxSsTrFax9600NoSysResCnt,
       "iwfDxSsTrFax14400NoSysResCnt": iwfDxSsTrFax14400NoSysResCnt,
       "iwfDxSsTrAd9600SktErrCnt": iwfDxSsTrAd9600SktErrCnt,
       "iwfDxSsTrAd14400SktErrCnt": iwfDxSsTrAd14400SktErrCnt,
       "iwfDxSsTrFax9600SktErrCnt": iwfDxSsTrFax9600SktErrCnt,
       "iwfDxSsTrFax14400SktErrCnt": iwfDxSsTrFax14400SktErrCnt,
       "iwfDxSsTrAd9600PrtErrCnt": iwfDxSsTrAd9600PrtErrCnt,
       "iwfDxSsTrAd14400PrtErrCnt": iwfDxSsTrAd14400PrtErrCnt,
       "iwfDxSsTrFax9600PrtErrCnt": iwfDxSsTrFax9600PrtErrCnt,
       "iwfDxSsTrFax14400PrtErrCnt": iwfDxSsTrFax14400PrtErrCnt,
       "iwfDxSsTrAd9600NoMdmResCnt": iwfDxSsTrAd9600NoMdmResCnt,
       "iwfDxSsTrAd14400NoMdmResCnt": iwfDxSsTrAd14400NoMdmResCnt,
       "iwfDxSsTrFax9600NoMdmResCnt": iwfDxSsTrFax9600NoMdmResCnt,
       "iwfDxSsTrFax14400NoMdmResCnt": iwfDxSsTrFax14400NoMdmResCnt,
       "iwfDxSsTrNoRespCnt": iwfDxSsTrNoRespCnt,
       "iwfDxSsTrStatus": iwfDxSsTrStatus,
       "iwfCfgCoSsTrap": iwfCfgCoSsTrap,
       "iwfCfgCoSsTrapTable": iwfCfgCoSsTrapTable,
       "iwfCfgCoSsTrapEntry": iwfCfgCoSsTrapEntry,
       "iwfCoSsTrIndex": iwfCoSsTrIndex,
       "iwfCoSsTrMrgOperStatus": iwfCoSsTrMrgOperStatus,
       "iwfCoSsTrNonOperStatus": iwfCoSsTrNonOperStatus,
       "iwfCoSsTrClearStatus": iwfCoSsTrClearStatus,
       "iwfCoSsTrMrgOperBitMask": iwfCoSsTrMrgOperBitMask,
       "iwfCoSsTrMrgOperThreshCnt": iwfCoSsTrMrgOperThreshCnt,
       "iwfCoSsTrNonOperThreshCnt": iwfCoSsTrNonOperThreshCnt,
       "iwfCoSsTrClearThreshCnt": iwfCoSsTrClearThreshCnt,
       "iwfCoSsTrMrgOperThreshTimer": iwfCoSsTrMrgOperThreshTimer,
       "iwfCoSsTrNonOperThreshTimer": iwfCoSsTrNonOperThreshTimer,
       "iwfCoSsTrClearThreshTimer": iwfCoSsTrClearThreshTimer,
       "iwfCoSsTrSysNoRespErrCnt": iwfCoSsTrSysNoRespErrCnt,
       "iwfCoSsTrDictOutOfSyncCnt": iwfCoSsTrDictOutOfSyncCnt,
       "iwfCoSsTrStatus": iwfCoSsTrStatus,
       "iwfCfgPppSsTrap": iwfCfgPppSsTrap,
       "iwfCfgPppSsTrapTable": iwfCfgPppSsTrapTable,
       "iwfCfgPppSsTrapEntry": iwfCfgPppSsTrapEntry,
       "iwfPppSsTrIndex": iwfPppSsTrIndex,
       "iwfPppSsTrMrgOperStatus": iwfPppSsTrMrgOperStatus,
       "iwfPppSsTrNonOperStatus": iwfPppSsTrNonOperStatus,
       "iwfPppSsTrClearStatus": iwfPppSsTrClearStatus,
       "iwfPppSsTrMrgOperBitMask": iwfPppSsTrMrgOperBitMask,
       "iwfPppSsTrMrgOperThreshCnt": iwfPppSsTrMrgOperThreshCnt,
       "iwfPppSsTrNonOperThreshCnt": iwfPppSsTrNonOperThreshCnt,
       "iwfPppSsTrClearThreshCnt": iwfPppSsTrClearThreshCnt,
       "iwfPppSsTrMrgOperThreshTimer": iwfPppSsTrMrgOperThreshTimer,
       "iwfPppSsTrNonOperThreshTimer": iwfPppSsTrNonOperThreshTimer,
       "iwfPppSsTrClearThreshTimer": iwfPppSsTrClearThreshTimer,
       "iwfPppSsTrSysNoRespErrCnt": iwfPppSsTrSysNoRespErrCnt,
       "iwfPppSsTrCrcErrCnt": iwfPppSsTrCrcErrCnt,
       "iwfPppSsTrStatus": iwfPppSsTrStatus,
       "iwfCfgTcpSsTrap": iwfCfgTcpSsTrap,
       "iwfCfgTcpSsTrapTable": iwfCfgTcpSsTrapTable,
       "iwfCfgTcpSsTrapEntry": iwfCfgTcpSsTrapEntry,
       "iwfTcpSsTrIndex": iwfTcpSsTrIndex,
       "iwfTcpSsTrMrgOperStatus": iwfTcpSsTrMrgOperStatus,
       "iwfTcpSsTrNonOperStatus": iwfTcpSsTrNonOperStatus,
       "iwfTcpSsTrClearStatus": iwfTcpSsTrClearStatus,
       "iwfTcpSsTrMrgOperBitMask": iwfTcpSsTrMrgOperBitMask,
       "iwfTcpSsTrMrgOperThreshCnt": iwfTcpSsTrMrgOperThreshCnt,
       "iwfTcpSsTrNonOperThreshCnt": iwfTcpSsTrNonOperThreshCnt,
       "iwfTcpSsTrClearThreshCnt": iwfTcpSsTrClearThreshCnt,
       "iwfTcpSsTrMrgOperThreshTimer": iwfTcpSsTrMrgOperThreshTimer,
       "iwfTcpSsTrNonOperThreshTimer": iwfTcpSsTrNonOperThreshTimer,
       "iwfTcpSsTrClearThreshTimer": iwfTcpSsTrClearThreshTimer,
       "iwfTcpSsTrSysNoRespErrCnt": iwfTcpSsTrSysNoRespErrCnt,
       "iwfTcpSsTrStatus": iwfTcpSsTrStatus,
       "iwfOprFrRly": iwfOprFrRly,
       "iwfOprFrRlyTable": iwfOprFrRlyTable,
       "iwfOprFrRlyEntry": iwfOprFrRlyEntry,
       "iwfOprFrRlyIndex": iwfOprFrRlyIndex,
       "iwfOprFrRlyT391StatusEnqryTimr": iwfOprFrRlyT391StatusEnqryTimr,
       "iwfOprFrRlyT392StatusTimer": iwfOprFrRlyT392StatusTimer,
       "iwfOprFrRlyN391StatusEnqrySent": iwfOprFrRlyN391StatusEnqrySent,
       "iwfOprQ921": iwfOprQ921,
       "iwfOprQ921Table": iwfOprQ921Table,
       "iwfOprQ921Entry": iwfOprQ921Entry,
       "iwfOprQ921Index": iwfOprQ921Index,
       "iwfOprQ921KmaxOutStandPkt": iwfOprQ921KmaxOutStandPkt,
       "iwfOprQ921T200IframeAckTimer": iwfOprQ921T200IframeAckTimer,
       "iwfOprQ921T203MaxTimeNoIframe": iwfOprQ921T203MaxTimeNoIframe,
       "iwfOprQ921N200MaxFrameRetrans": iwfOprQ921N200MaxFrameRetrans,
       "iwfOprQ921N201RxMaxOctetInfo": iwfOprQ921N201RxMaxOctetInfo,
       "iwfOprQ921N201TxMaxOctetInfo": iwfOprQ921N201TxMaxOctetInfo,
       "iwfOprQ933": iwfOprQ933,
       "iwfOprQ933Table": iwfOprQ933Table,
       "iwfOprQ933Entry": iwfOprQ933Entry,
       "iwfOprQ933Index": iwfOprQ933Index,
       "iwfOprQ933T303SetupTimer": iwfOprQ933T303SetupTimer,
       "iwfOprQ933T305DisconnectTimer": iwfOprQ933T305DisconnectTimer,
       "iwfOprQ933T308ReleaseTimer": iwfOprQ933T308ReleaseTimer,
       "iwfOprQ933T309DataLinkDiscTimr": iwfOprQ933T309DataLinkDiscTimr,
       "iwfOprQ933T310CallProceedTimer": iwfOprQ933T310CallProceedTimer,
       "iwfOprQ933T313ConnectSentTimer": iwfOprQ933T313ConnectSentTimer,
       "iwfOprCallStats": iwfOprCallStats,
       "iwfOprCallStatsTable": iwfOprCallStatsTable,
       "iwfOprCallStatsEntry": iwfOprCallStatsEntry,
       "iwfOprCsIndex": iwfOprCsIndex,
       "iwfOprCsMobOrigAdStats": iwfOprCsMobOrigAdStats,
       "iwfOprCsMobOrigFaxStats": iwfOprCsMobOrigFaxStats,
       "iwfOprCsMobTermAdStats": iwfOprCsMobTermAdStats,
       "iwfOprCsMobTermFaxStats": iwfOprCsMobTermFaxStats,
       "iwfOprPppParam": iwfOprPppParam,
       "iwfOprPppParamTable": iwfOprPppParamTable,
       "iwfOprPppParamEntry": iwfOprPppParamEntry,
       "iwfOprPppIndex": iwfOprPppIndex,
       "iwfOprPppForceEncryptData": iwfOprPppForceEncryptData,
       "iwfOprPppForceEncryptpassword": iwfOprPppForceEncryptpassword,
       "iwfOprMaxNumbConfigRequests": iwfOprMaxNumbConfigRequests,
       "iwfOprMaxNumbConfigNAK": iwfOprMaxNumbConfigNAK,
       "iwfOprPppMaxNumbRejects": iwfOprPppMaxNumbRejects,
       "iwfOprPppMaxNumbTermRequests": iwfOprPppMaxNumbTermRequests,
       "iwfOprPppNegotiateTime": iwfOprPppNegotiateTime,
       "iwfOprPppRestartTime": iwfOprPppRestartTime,
       "iwfOprPppIpAddressPoolMax": iwfOprPppIpAddressPoolMax,
       "iwfOprPppIpAddressPoolMin": iwfOprPppIpAddressPoolMin,
       "iwfOprTcpIp": iwfOprTcpIp,
       "iwfOprTcpIpTable": iwfOprTcpIpTable,
       "iwfOprTcpIpEntry": iwfOprTcpIpEntry,
       "iwfOprTiIndex": iwfOprTiIndex,
       "iwfOprTiDefaultServiceType": iwfOprTiDefaultServiceType,
       "iwfOprTiDefaultTimeToLive": iwfOprTiDefaultTimeToLive,
       "iwfOprTiMtuDiscovery": iwfOprTiMtuDiscovery,
       "iwfOprTiKeepAliveInterval": iwfOprTiKeepAliveInterval,
       "iwfOprTiKeepAliveTime": iwfOprTiKeepAliveTime,
       "iwfOprTiMaxMtuSize": iwfOprTiMaxMtuSize,
       "iwfOprTiMaxConnectReTrans": iwfOprTiMaxConnectReTrans,
       "iwfOprTiMaxDataRetrans": iwfOprTiMaxDataRetrans,
       "iwfOprTiMaxNumberConnections": iwfOprTiMaxNumberConnections,
       "iwfOprTiWindowSize": iwfOprTiWindowSize,
       "iwfOprTiLocalIpAddress": iwfOprTiLocalIpAddress,
       "iwfOprTiSubnetIpMask": iwfOprTiSubnetIpMask,
       "iwfOprTiDefualtGatewayIp": iwfOprTiDefualtGatewayIp,
       "iwfLogStats": iwfLogStats,
       "iwfLogStatsTable": iwfLogStatsTable,
       "iwfLogStatsEntry": iwfLogStatsEntry,
       "iwfLogStsIndex": iwfLogStsIndex,
       "iwfLogStsIndex2": iwfLogStsIndex2,
       "iwfLogCallRefNum": iwfLogCallRefNum,
       "iwfLogMobileIpAddr": iwfLogMobileIpAddr,
       "iwfLogCallingPartyNum": iwfLogCallingPartyNum,
       "iwfLogCalledPartyNum": iwfLogCalledPartyNum,
       "iwfLogCallType": iwfLogCallType,
       "iwfLogESN": iwfLogESN,
       "iwfLogCallId": iwfLogCallId,
       "iwfLogIMSI": iwfLogIMSI,
       "iwfLogServiceOption": iwfLogServiceOption,
       "iwfLogDisconnectCause": iwfLogDisconnectCause,
       "iwfLogMobileNumBytesTxed": iwfLogMobileNumBytesTxed,
       "iwfLogMobileNumBytesRxed": iwfLogMobileNumBytesRxed,
       "iwfLogNumFaxPagesProcessed": iwfLogNumFaxPagesProcessed,
       "iwfLogCompType": iwfLogCompType,
       "iwfLogCallErrorCode": iwfLogCallErrorCode,
       "iwfLogModemSetupTime": iwfLogModemSetupTime,
       "iwfLogCallConnectingTime": iwfLogCallConnectingTime,
       "iwfLogTotConnectTime": iwfLogTotConnectTime,
       "iwfCfgQncSrv": iwfCfgQncSrv,
       "iwfCfgQncSrvTable": iwfCfgQncSrvTable,
       "iwfCfgQncSrvEntry": iwfCfgQncSrvEntry,
       "iwfCfgQncSrvIndex": iwfCfgQncSrvIndex,
       "iwfCfgQncSrvIndex2": iwfCfgQncSrvIndex2,
       "iwfCfgQncDialedNumber": iwfCfgQncDialedNumber,
       "iwfCfgQncServiceType": iwfCfgQncServiceType,
       "iwfCfgQncPrimaryIpAddress": iwfCfgQncPrimaryIpAddress,
       "iwfCfgQncSecondaryIpAddress": iwfCfgQncSecondaryIpAddress,
       "iwfOprQncSrv": iwfOprQncSrv,
       "iwfOprQncSrvTable": iwfOprQncSrvTable,
       "iwfOprQncSrvEntry": iwfOprQncSrvEntry,
       "iwfQncSrvIndex": iwfQncSrvIndex,
       "iwfQncSrvIndex2": iwfQncSrvIndex2,
       "iwfQncDialedNumber": iwfQncDialedNumber,
       "iwfQncServiceType": iwfQncServiceType,
       "iwfQncPrimaryIpAddress": iwfQncPrimaryIpAddress,
       "iwfQncSecondaryIpAddress": iwfQncSecondaryIpAddress}
)
