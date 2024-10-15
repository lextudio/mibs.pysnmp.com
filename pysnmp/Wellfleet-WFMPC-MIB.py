# SNMP MIB module (Wellfleet-WFMPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-WFMPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:31 2024
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

(wfmpcObjects,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfmpcObjects")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfmpcEntryTable_Object = MibTable
wfmpcEntryTable = _WfmpcEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1)
)
if mibBuilder.loadTexts:
    wfmpcEntryTable.setStatus("mandatory")
_WfmpcEntry_Object = MibTableRow
wfmpcEntry = _WfmpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1)
)
wfmpcEntry.setIndexNames(
    (0, "Wellfleet-WFMPC-MIB", "wfmpcSlot"),
)
if mibBuilder.loadTexts:
    wfmpcEntry.setStatus("mandatory")


class _WfmpcDelete_Type(Integer32):
    """Custom type wfmpcDelete based on Integer32"""
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


_WfmpcDelete_Type.__name__ = "Integer32"
_WfmpcDelete_Object = MibTableColumn
wfmpcDelete = _WfmpcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 1),
    _WfmpcDelete_Type()
)
wfmpcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcDelete.setStatus("mandatory")


class _WfmpcDisable_Type(Integer32):
    """Custom type wfmpcDisable based on Integer32"""
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


_WfmpcDisable_Type.__name__ = "Integer32"
_WfmpcDisable_Object = MibTableColumn
wfmpcDisable = _WfmpcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 2),
    _WfmpcDisable_Type()
)
wfmpcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcDisable.setStatus("mandatory")
_WfmpcSlot_Type = Integer32
_WfmpcSlot_Object = MibTableColumn
wfmpcSlot = _WfmpcSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 3),
    _WfmpcSlot_Type()
)
wfmpcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcSlot.setStatus("mandatory")
_WfmpcCct_Type = Integer32
_WfmpcCct_Object = MibTableColumn
wfmpcCct = _WfmpcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 4),
    _WfmpcCct_Type()
)
wfmpcCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcCct.setStatus("mandatory")
_WfmpcMsgNum_Type = Integer32
_WfmpcMsgNum_Object = MibTableColumn
wfmpcMsgNum = _WfmpcMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 5),
    _WfmpcMsgNum_Type()
)
wfmpcMsgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcMsgNum.setStatus("mandatory")


class _WfmpcMsgSendEnable_Type(Integer32):
    """Custom type wfmpcMsgSendEnable based on Integer32"""
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


_WfmpcMsgSendEnable_Type.__name__ = "Integer32"
_WfmpcMsgSendEnable_Object = MibTableColumn
wfmpcMsgSendEnable = _WfmpcMsgSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 6),
    _WfmpcMsgSendEnable_Type()
)
wfmpcMsgSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcMsgSendEnable.setStatus("mandatory")


class _WfmpcMPSAtmAddr_Type(OctetString):
    """Custom type wfmpcMPSAtmAddr based on OctetString"""
    defaultValue = OctetString("0x390000000000000000000000000000A2CB2C2804")


_WfmpcMPSAtmAddr_Object = MibTableColumn
wfmpcMPSAtmAddr = _WfmpcMPSAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 7),
    _WfmpcMPSAtmAddr_Type()
)
wfmpcMPSAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcMPSAtmAddr.setStatus("mandatory")


class _WfmpcSetupVCtoMPS_Type(Integer32):
    """Custom type wfmpcSetupVCtoMPS based on Integer32"""
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


_WfmpcSetupVCtoMPS_Type.__name__ = "Integer32"
_WfmpcSetupVCtoMPS_Object = MibTableColumn
wfmpcSetupVCtoMPS = _WfmpcSetupVCtoMPS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 8),
    _WfmpcSetupVCtoMPS_Type()
)
wfmpcSetupVCtoMPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcSetupVCtoMPS.setStatus("mandatory")
_WfmpcMPCAtmAddr_Type = OctetString
_WfmpcMPCAtmAddr_Object = MibTableColumn
wfmpcMPCAtmAddr = _WfmpcMPCAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 9),
    _WfmpcMPCAtmAddr_Type()
)
wfmpcMPCAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcMPCAtmAddr.setStatus("mandatory")


class _WfmpcCIPNackFlag_Type(Integer32):
    """Custom type wfmpcCIPNackFlag based on Integer32"""
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


_WfmpcCIPNackFlag_Type.__name__ = "Integer32"
_WfmpcCIPNackFlag_Object = MibTableColumn
wfmpcCIPNackFlag = _WfmpcCIPNackFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 10),
    _WfmpcCIPNackFlag_Type()
)
wfmpcCIPNackFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpcCIPNackFlag.setStatus("mandatory")
_WfmpcStatisticsTable_Object = MibTable
wfmpcStatisticsTable = _WfmpcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2)
)
if mibBuilder.loadTexts:
    wfmpcStatisticsTable.setStatus("mandatory")
_WfmpcStatisticsEntry_Object = MibTableRow
wfmpcStatisticsEntry = _WfmpcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1)
)
wfmpcStatisticsEntry.setIndexNames(
    (0, "Wellfleet-WFMPC-MIB", "wfmpcStatSlot"),
    (0, "Wellfleet-WFMPC-MIB", "wfmpcStatIndex"),
)
if mibBuilder.loadTexts:
    wfmpcStatisticsEntry.setStatus("mandatory")
_WfmpcStatIndex_Type = Integer32
_WfmpcStatIndex_Object = MibTableColumn
wfmpcStatIndex = _WfmpcStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 1),
    _WfmpcStatIndex_Type()
)
wfmpcStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatIndex.setStatus("mandatory")
_WfmpcStatRxMpoaResolveRequests_Type = Counter32
_WfmpcStatRxMpoaResolveRequests_Object = MibTableColumn
wfmpcStatRxMpoaResolveRequests = _WfmpcStatRxMpoaResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 2),
    _WfmpcStatRxMpoaResolveRequests_Type()
)
wfmpcStatRxMpoaResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaResolveRequests.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyAcks_Type = Counter32
_WfmpcStatTxMpoaResolveReplyAcks_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyAcks = _WfmpcStatTxMpoaResolveReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 3),
    _WfmpcStatTxMpoaResolveReplyAcks_Type()
)
wfmpcStatTxMpoaResolveReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyAcks.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyInsufECResources_Type = Counter32
_WfmpcStatTxMpoaResolveReplyInsufECResources_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyInsufECResources = _WfmpcStatTxMpoaResolveReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 4),
    _WfmpcStatTxMpoaResolveReplyInsufECResources_Type()
)
wfmpcStatTxMpoaResolveReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyInsufECResources.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyInsufSCResources_Type = Counter32
_WfmpcStatTxMpoaResolveReplyInsufSCResources_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyInsufSCResources = _WfmpcStatTxMpoaResolveReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 5),
    _WfmpcStatTxMpoaResolveReplyInsufSCResources_Type()
)
wfmpcStatTxMpoaResolveReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyInsufSCResources.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyInsufEitherResources_Type = Counter32
_WfmpcStatTxMpoaResolveReplyInsufEitherResources_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyInsufEitherResources = _WfmpcStatTxMpoaResolveReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 6),
    _WfmpcStatTxMpoaResolveReplyInsufEitherResources_Type()
)
wfmpcStatTxMpoaResolveReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyInsufEitherResources.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyUnsupportedInetProt_Type = Counter32
_WfmpcStatTxMpoaResolveReplyUnsupportedInetProt_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyUnsupportedInetProt = _WfmpcStatTxMpoaResolveReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 7),
    _WfmpcStatTxMpoaResolveReplyUnsupportedInetProt_Type()
)
wfmpcStatTxMpoaResolveReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyUnsupportedInetProt.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps_Type = Counter32
_WfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps = _WfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 8),
    _WfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps_Type()
)
wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyUnspecifiedOther_Type = Counter32
_WfmpcStatTxMpoaResolveReplyUnspecifiedOther_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyUnspecifiedOther = _WfmpcStatTxMpoaResolveReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 9),
    _WfmpcStatTxMpoaResolveReplyUnspecifiedOther_Type()
)
wfmpcStatTxMpoaResolveReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyUnspecifiedOther.setStatus("mandatory")
_WfmpcStatTxMpoaResolveReplyOtherOther_Type = Counter32
_WfmpcStatTxMpoaResolveReplyOtherOther_Object = MibTableColumn
wfmpcStatTxMpoaResolveReplyOtherOther = _WfmpcStatTxMpoaResolveReplyOtherOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 10),
    _WfmpcStatTxMpoaResolveReplyOtherOther_Type()
)
wfmpcStatTxMpoaResolveReplyOtherOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaResolveReplyOtherOther.setStatus("mandatory")
_WfmpcStatGiveupTimeExpireds_Type = Counter32
_WfmpcStatGiveupTimeExpireds_Object = MibTableColumn
wfmpcStatGiveupTimeExpireds = _WfmpcStatGiveupTimeExpireds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 11),
    _WfmpcStatGiveupTimeExpireds_Type()
)
wfmpcStatGiveupTimeExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatGiveupTimeExpireds.setStatus("mandatory")
_WfmpcStatTxMpoaImpRequests_Type = Counter32
_WfmpcStatTxMpoaImpRequests_Object = MibTableColumn
wfmpcStatTxMpoaImpRequests = _WfmpcStatTxMpoaImpRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 12),
    _WfmpcStatTxMpoaImpRequests_Type()
)
wfmpcStatTxMpoaImpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaImpRequests.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyAcks_Type = Counter32
_WfmpcStatRxMpoaImpReplyAcks_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyAcks = _WfmpcStatRxMpoaImpReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 13),
    _WfmpcStatRxMpoaImpReplyAcks_Type()
)
wfmpcStatRxMpoaImpReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyAcks.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyInsufECResources_Type = Counter32
_WfmpcStatRxMpoaImpReplyInsufECResources_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyInsufECResources = _WfmpcStatRxMpoaImpReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 14),
    _WfmpcStatRxMpoaImpReplyInsufECResources_Type()
)
wfmpcStatRxMpoaImpReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyInsufECResources.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyInsufSCResources_Type = Counter32
_WfmpcStatRxMpoaImpReplyInsufSCResources_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyInsufSCResources = _WfmpcStatRxMpoaImpReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 15),
    _WfmpcStatRxMpoaImpReplyInsufSCResources_Type()
)
wfmpcStatRxMpoaImpReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyInsufSCResources.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyInsufEitherResources_Type = Counter32
_WfmpcStatRxMpoaImpReplyInsufEitherResources_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyInsufEitherResources = _WfmpcStatRxMpoaImpReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 16),
    _WfmpcStatRxMpoaImpReplyInsufEitherResources_Type()
)
wfmpcStatRxMpoaImpReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyInsufEitherResources.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyUnsupportedInetProt_Type = Counter32
_WfmpcStatRxMpoaImpReplyUnsupportedInetProt_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyUnsupportedInetProt = _WfmpcStatRxMpoaImpReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 17),
    _WfmpcStatRxMpoaImpReplyUnsupportedInetProt_Type()
)
wfmpcStatRxMpoaImpReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyUnsupportedInetProt.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyUnsupportedMacEncaps_Type = Counter32
_WfmpcStatRxMpoaImpReplyUnsupportedMacEncaps_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps = _WfmpcStatRxMpoaImpReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 18),
    _WfmpcStatRxMpoaImpReplyUnsupportedMacEncaps_Type()
)
wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyUnspecifiedOther_Type = Counter32
_WfmpcStatRxMpoaImpReplyUnspecifiedOther_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyUnspecifiedOther = _WfmpcStatRxMpoaImpReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 19),
    _WfmpcStatRxMpoaImpReplyUnspecifiedOther_Type()
)
wfmpcStatRxMpoaImpReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyUnspecifiedOther.setStatus("mandatory")
_WfmpcStatRxMpoaImpReplyOtherOther_Type = Counter32
_WfmpcStatRxMpoaImpReplyOtherOther_Object = MibTableColumn
wfmpcStatRxMpoaImpReplyOtherOther = _WfmpcStatRxMpoaImpReplyOtherOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 20),
    _WfmpcStatRxMpoaImpReplyOtherOther_Type()
)
wfmpcStatRxMpoaImpReplyOtherOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaImpReplyOtherOther.setStatus("mandatory")
_WfmpcStatRxMpoaEgressCachePurgeRequests_Type = Counter32
_WfmpcStatRxMpoaEgressCachePurgeRequests_Object = MibTableColumn
wfmpcStatRxMpoaEgressCachePurgeRequests = _WfmpcStatRxMpoaEgressCachePurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 21),
    _WfmpcStatRxMpoaEgressCachePurgeRequests_Type()
)
wfmpcStatRxMpoaEgressCachePurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatRxMpoaEgressCachePurgeRequests.setStatus("mandatory")
_WfmpcStatTxMpoaEgressCachePurgeReplies_Type = Counter32
_WfmpcStatTxMpoaEgressCachePurgeReplies_Object = MibTableColumn
wfmpcStatTxMpoaEgressCachePurgeReplies = _WfmpcStatTxMpoaEgressCachePurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 22),
    _WfmpcStatTxMpoaEgressCachePurgeReplies_Type()
)
wfmpcStatTxMpoaEgressCachePurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaEgressCachePurgeReplies.setStatus("mandatory")
_WfmpcStatTxMpoaTriggers_Type = Counter32
_WfmpcStatTxMpoaTriggers_Object = MibTableColumn
wfmpcStatTxMpoaTriggers = _WfmpcStatTxMpoaTriggers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 23),
    _WfmpcStatTxMpoaTriggers_Type()
)
wfmpcStatTxMpoaTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatTxMpoaTriggers.setStatus("mandatory")
_WfmpcStatSlot_Type = Integer32
_WfmpcStatSlot_Object = MibTableColumn
wfmpcStatSlot = _WfmpcStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 24),
    _WfmpcStatSlot_Type()
)
wfmpcStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpcStatSlot.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-WFMPC-MIB",
    **{"wfmpcEntryTable": wfmpcEntryTable,
       "wfmpcEntry": wfmpcEntry,
       "wfmpcDelete": wfmpcDelete,
       "wfmpcDisable": wfmpcDisable,
       "wfmpcSlot": wfmpcSlot,
       "wfmpcCct": wfmpcCct,
       "wfmpcMsgNum": wfmpcMsgNum,
       "wfmpcMsgSendEnable": wfmpcMsgSendEnable,
       "wfmpcMPSAtmAddr": wfmpcMPSAtmAddr,
       "wfmpcSetupVCtoMPS": wfmpcSetupVCtoMPS,
       "wfmpcMPCAtmAddr": wfmpcMPCAtmAddr,
       "wfmpcCIPNackFlag": wfmpcCIPNackFlag,
       "wfmpcStatisticsTable": wfmpcStatisticsTable,
       "wfmpcStatisticsEntry": wfmpcStatisticsEntry,
       "wfmpcStatIndex": wfmpcStatIndex,
       "wfmpcStatRxMpoaResolveRequests": wfmpcStatRxMpoaResolveRequests,
       "wfmpcStatTxMpoaResolveReplyAcks": wfmpcStatTxMpoaResolveReplyAcks,
       "wfmpcStatTxMpoaResolveReplyInsufECResources": wfmpcStatTxMpoaResolveReplyInsufECResources,
       "wfmpcStatTxMpoaResolveReplyInsufSCResources": wfmpcStatTxMpoaResolveReplyInsufSCResources,
       "wfmpcStatTxMpoaResolveReplyInsufEitherResources": wfmpcStatTxMpoaResolveReplyInsufEitherResources,
       "wfmpcStatTxMpoaResolveReplyUnsupportedInetProt": wfmpcStatTxMpoaResolveReplyUnsupportedInetProt,
       "wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps": wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps,
       "wfmpcStatTxMpoaResolveReplyUnspecifiedOther": wfmpcStatTxMpoaResolveReplyUnspecifiedOther,
       "wfmpcStatTxMpoaResolveReplyOtherOther": wfmpcStatTxMpoaResolveReplyOtherOther,
       "wfmpcStatGiveupTimeExpireds": wfmpcStatGiveupTimeExpireds,
       "wfmpcStatTxMpoaImpRequests": wfmpcStatTxMpoaImpRequests,
       "wfmpcStatRxMpoaImpReplyAcks": wfmpcStatRxMpoaImpReplyAcks,
       "wfmpcStatRxMpoaImpReplyInsufECResources": wfmpcStatRxMpoaImpReplyInsufECResources,
       "wfmpcStatRxMpoaImpReplyInsufSCResources": wfmpcStatRxMpoaImpReplyInsufSCResources,
       "wfmpcStatRxMpoaImpReplyInsufEitherResources": wfmpcStatRxMpoaImpReplyInsufEitherResources,
       "wfmpcStatRxMpoaImpReplyUnsupportedInetProt": wfmpcStatRxMpoaImpReplyUnsupportedInetProt,
       "wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps": wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps,
       "wfmpcStatRxMpoaImpReplyUnspecifiedOther": wfmpcStatRxMpoaImpReplyUnspecifiedOther,
       "wfmpcStatRxMpoaImpReplyOtherOther": wfmpcStatRxMpoaImpReplyOtherOther,
       "wfmpcStatRxMpoaEgressCachePurgeRequests": wfmpcStatRxMpoaEgressCachePurgeRequests,
       "wfmpcStatTxMpoaEgressCachePurgeReplies": wfmpcStatTxMpoaEgressCachePurgeReplies,
       "wfmpcStatTxMpoaTriggers": wfmpcStatTxMpoaTriggers,
       "wfmpcStatSlot": wfmpcStatSlot}
)
