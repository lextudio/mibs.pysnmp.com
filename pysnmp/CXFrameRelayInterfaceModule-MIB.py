# SNMP MIB module (CXFrameRelayInterfaceModule-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFrameRelayInterfaceModule-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:28 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "CXFrameRelay-MIB",
    "DLCI")

(Alias,
 SapIndex,
 cxFrameRelayInterfaceModule) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxFrameRelayInterfaceModule")

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


# Types definitions



class SubRef(Integer32):
    """Custom type SubRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _FrimSRConnectInterval_Type(Integer32):
    """Custom type frimSRConnectInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrimSRConnectInterval_Type.__name__ = "Integer32"
_FrimSRConnectInterval_Object = MibScalar
frimSRConnectInterval = _FrimSRConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 1),
    _FrimSRConnectInterval_Type()
)
frimSRConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSRConnectInterval.setStatus("mandatory")
_FrimServiceCost_Type = Integer32
_FrimServiceCost_Object = MibScalar
frimServiceCost = _FrimServiceCost_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 2),
    _FrimServiceCost_Type()
)
frimServiceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimServiceCost.setStatus("mandatory")
_FrimSapTable_Object = MibTable
frimSapTable = _FrimSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    frimSapTable.setStatus("mandatory")
_FrimSapEntry_Object = MibTableRow
frimSapEntry = _FrimSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1)
)
frimSapEntry.setIndexNames(
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSapId"),
)
if mibBuilder.loadTexts:
    frimSapEntry.setStatus("mandatory")
_FrimSapId_Type = SapIndex
_FrimSapId_Object = MibTableColumn
frimSapId = _FrimSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 1),
    _FrimSapId_Type()
)
frimSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapId.setStatus("mandatory")


class _FrimSapRowStatus_Type(Integer32):
    """Custom type frimSapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_FrimSapRowStatus_Type.__name__ = "Integer32"
_FrimSapRowStatus_Object = MibTableColumn
frimSapRowStatus = _FrimSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 2),
    _FrimSapRowStatus_Type()
)
frimSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapRowStatus.setStatus("mandatory")


class _FrimSapType_Type(Integer32):
    """Custom type frimSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_FrimSapType_Type.__name__ = "Integer32"
_FrimSapType_Object = MibTableColumn
frimSapType = _FrimSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 3),
    _FrimSapType_Type()
)
frimSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapType.setStatus("mandatory")
_FrimSapAlias_Type = Alias
_FrimSapAlias_Object = MibTableColumn
frimSapAlias = _FrimSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 4),
    _FrimSapAlias_Type()
)
frimSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapAlias.setStatus("mandatory")
_FrimSapCompanionAlias_Type = Alias
_FrimSapCompanionAlias_Object = MibTableColumn
frimSapCompanionAlias = _FrimSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 5),
    _FrimSapCompanionAlias_Type()
)
frimSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapCompanionAlias.setStatus("mandatory")


class _FrimSapMaxDlcis_Type(Integer32):
    """Custom type frimSapMaxDlcis based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_FrimSapMaxDlcis_Type.__name__ = "Integer32"
_FrimSapMaxDlcis_Object = MibTableColumn
frimSapMaxDlcis = _FrimSapMaxDlcis_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 6),
    _FrimSapMaxDlcis_Type()
)
frimSapMaxDlcis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapMaxDlcis.setStatus("mandatory")


class _FrimSapMaxErrorFrames_Type(Integer32):
    """Custom type frimSapMaxErrorFrames based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_FrimSapMaxErrorFrames_Type.__name__ = "Integer32"
_FrimSapMaxErrorFrames_Object = MibTableColumn
frimSapMaxErrorFrames = _FrimSapMaxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 7),
    _FrimSapMaxErrorFrames_Type()
)
frimSapMaxErrorFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapMaxErrorFrames.setStatus("mandatory")


class _FrimSapMonitorFrames_Type(Integer32):
    """Custom type frimSapMonitorFrames based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_FrimSapMonitorFrames_Type.__name__ = "Integer32"
_FrimSapMonitorFrames_Object = MibTableColumn
frimSapMonitorFrames = _FrimSapMonitorFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 8),
    _FrimSapMonitorFrames_Type()
)
frimSapMonitorFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapMonitorFrames.setStatus("mandatory")


class _FrimSapFrWindowSize_Type(Integer32):
    """Custom type frimSapFrWindowSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 300),
    )


_FrimSapFrWindowSize_Type.__name__ = "Integer32"
_FrimSapFrWindowSize_Object = MibTableColumn
frimSapFrWindowSize = _FrimSapFrWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 9),
    _FrimSapFrWindowSize_Type()
)
frimSapFrWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSapFrWindowSize.setStatus("mandatory")


class _FrimSapControlStats_Type(Integer32):
    """Custom type frimSapControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSapStats", 1)
    )


_FrimSapControlStats_Type.__name__ = "Integer32"
_FrimSapControlStats_Object = MibTableColumn
frimSapControlStats = _FrimSapControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 19),
    _FrimSapControlStats_Type()
)
frimSapControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frimSapControlStats.setStatus("mandatory")
_FrimSapstatRxDataFrames_Type = Counter32
_FrimSapstatRxDataFrames_Object = MibTableColumn
frimSapstatRxDataFrames = _FrimSapstatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 20),
    _FrimSapstatRxDataFrames_Type()
)
frimSapstatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatRxDataFrames.setStatus("mandatory")
_FrimSapstatRxDataOctets_Type = Counter32
_FrimSapstatRxDataOctets_Object = MibTableColumn
frimSapstatRxDataOctets = _FrimSapstatRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 21),
    _FrimSapstatRxDataOctets_Type()
)
frimSapstatRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatRxDataOctets.setStatus("mandatory")
_FrimSapstatTxDataFrames_Type = Counter32
_FrimSapstatTxDataFrames_Object = MibTableColumn
frimSapstatTxDataFrames = _FrimSapstatTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 22),
    _FrimSapstatTxDataFrames_Type()
)
frimSapstatTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatTxDataFrames.setStatus("mandatory")
_FrimSapstatTxDataOctets_Type = Counter32
_FrimSapstatTxDataOctets_Object = MibTableColumn
frimSapstatTxDataOctets = _FrimSapstatTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 23),
    _FrimSapstatTxDataOctets_Type()
)
frimSapstatTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatTxDataOctets.setStatus("mandatory")
_FrimSapstatUnopenedServiceDiscards_Type = Counter32
_FrimSapstatUnopenedServiceDiscards_Object = MibTableColumn
frimSapstatUnopenedServiceDiscards = _FrimSapstatUnopenedServiceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 24),
    _FrimSapstatUnopenedServiceDiscards_Type()
)
frimSapstatUnopenedServiceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatUnopenedServiceDiscards.setStatus("mandatory")
_FrimSapstatPvcDownDiscards_Type = Counter32
_FrimSapstatPvcDownDiscards_Object = MibTableColumn
frimSapstatPvcDownDiscards = _FrimSapstatPvcDownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 25),
    _FrimSapstatPvcDownDiscards_Type()
)
frimSapstatPvcDownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatPvcDownDiscards.setStatus("mandatory")
_FrimSapstatUserSuccessfulOpens_Type = Counter32
_FrimSapstatUserSuccessfulOpens_Object = MibTableColumn
frimSapstatUserSuccessfulOpens = _FrimSapstatUserSuccessfulOpens_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 26),
    _FrimSapstatUserSuccessfulOpens_Type()
)
frimSapstatUserSuccessfulOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatUserSuccessfulOpens.setStatus("mandatory")
_FrimSapstatUserUnsuccessfulOpens_Type = Counter32
_FrimSapstatUserUnsuccessfulOpens_Object = MibTableColumn
frimSapstatUserUnsuccessfulOpens = _FrimSapstatUserUnsuccessfulOpens_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 27),
    _FrimSapstatUserUnsuccessfulOpens_Type()
)
frimSapstatUserUnsuccessfulOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatUserUnsuccessfulOpens.setStatus("mandatory")
_FrimSapstatSRSuccessfulConnects_Type = Counter32
_FrimSapstatSRSuccessfulConnects_Object = MibTableColumn
frimSapstatSRSuccessfulConnects = _FrimSapstatSRSuccessfulConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 28),
    _FrimSapstatSRSuccessfulConnects_Type()
)
frimSapstatSRSuccessfulConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatSRSuccessfulConnects.setStatus("mandatory")
_FrimSapstatSRUnsuccessfulConnects_Type = Counter32
_FrimSapstatSRUnsuccessfulConnects_Object = MibTableColumn
frimSapstatSRUnsuccessfulConnects = _FrimSapstatSRUnsuccessfulConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 29),
    _FrimSapstatSRUnsuccessfulConnects_Type()
)
frimSapstatSRUnsuccessfulConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatSRUnsuccessfulConnects.setStatus("mandatory")
_FrimSapstatTxResets_Type = Counter32
_FrimSapstatTxResets_Object = MibTableColumn
frimSapstatTxResets = _FrimSapstatTxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 30),
    _FrimSapstatTxResets_Type()
)
frimSapstatTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatTxResets.setStatus("mandatory")
_FrimSapstatRxBECN_Type = Counter32
_FrimSapstatRxBECN_Object = MibTableColumn
frimSapstatRxBECN = _FrimSapstatRxBECN_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 31),
    _FrimSapstatRxBECN_Type()
)
frimSapstatRxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatRxBECN.setStatus("mandatory")
_FrimSapstatRxFECN_Type = Counter32
_FrimSapstatRxFECN_Object = MibTableColumn
frimSapstatRxFECN = _FrimSapstatRxFECN_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 3, 1, 32),
    _FrimSapstatRxFECN_Type()
)
frimSapstatRxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSapstatRxFECN.setStatus("mandatory")
_FrimSysConTable_Object = MibTable
frimSysConTable = _FrimSysConTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5)
)
if mibBuilder.loadTexts:
    frimSysConTable.setStatus("mandatory")
_FrimSysConEntry_Object = MibTableRow
frimSysConEntry = _FrimSysConEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1)
)
frimSysConEntry.setIndexNames(
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSysConSapId"),
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSysConDlci"),
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSysConPid"),
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSysConRef"),
)
if mibBuilder.loadTexts:
    frimSysConEntry.setStatus("mandatory")
_FrimSysConSapId_Type = SapIndex
_FrimSysConSapId_Object = MibTableColumn
frimSysConSapId = _FrimSysConSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 1),
    _FrimSysConSapId_Type()
)
frimSysConSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConSapId.setStatus("mandatory")
_FrimSysConDlci_Type = DLCI
_FrimSysConDlci_Object = MibTableColumn
frimSysConDlci = _FrimSysConDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 2),
    _FrimSysConDlci_Type()
)
frimSysConDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConDlci.setStatus("mandatory")


class _FrimSysConPid_Type(Integer32):
    """Custom type frimSysConPid based on Integer32"""
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
        *(("pidCcm", 4),
          ("pidFr", 1),
          ("pidGmf", 5),
          ("pidLan", 2),
          ("pidLlc2", 6),
          ("pidX25", 3))
    )


_FrimSysConPid_Type.__name__ = "Integer32"
_FrimSysConPid_Object = MibTableColumn
frimSysConPid = _FrimSysConPid_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 3),
    _FrimSysConPid_Type()
)
frimSysConPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConPid.setStatus("mandatory")
_FrimSysConRef_Type = SubRef
_FrimSysConRef_Object = MibTableColumn
frimSysConRef = _FrimSysConRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 4),
    _FrimSysConRef_Type()
)
frimSysConRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConRef.setStatus("mandatory")
_FrimSysConRemoteSlot_Type = Integer32
_FrimSysConRemoteSlot_Object = MibTableColumn
frimSysConRemoteSlot = _FrimSysConRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 5),
    _FrimSysConRemoteSlot_Type()
)
frimSysConRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConRemoteSlot.setStatus("mandatory")
_FrimSysConCreationTime_Type = TimeTicks
_FrimSysConCreationTime_Object = MibTableColumn
frimSysConCreationTime = _FrimSysConCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 6),
    _FrimSysConCreationTime_Type()
)
frimSysConCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConCreationTime.setStatus("mandatory")
_FrimSysConReqDataSize_Type = Integer32
_FrimSysConReqDataSize_Object = MibTableColumn
frimSysConReqDataSize = _FrimSysConReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 7),
    _FrimSysConReqDataSize_Type()
)
frimSysConReqDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConReqDataSize.setStatus("mandatory")
_FrimSysConNegDataSize_Type = Integer32
_FrimSysConNegDataSize_Object = MibTableColumn
frimSysConNegDataSize = _FrimSysConNegDataSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 8),
    _FrimSysConNegDataSize_Type()
)
frimSysConNegDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConNegDataSize.setStatus("mandatory")
_FrimSysConNegSizeExceededFrames_Type = Counter32
_FrimSysConNegSizeExceededFrames_Object = MibTableColumn
frimSysConNegSizeExceededFrames = _FrimSysConNegSizeExceededFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 9),
    _FrimSysConNegSizeExceededFrames_Type()
)
frimSysConNegSizeExceededFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConNegSizeExceededFrames.setStatus("mandatory")
_FrimSysConRefRangeEnd_Type = SubRef
_FrimSysConRefRangeEnd_Object = MibTableColumn
frimSysConRefRangeEnd = _FrimSysConRefRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 5, 1, 10),
    _FrimSysConRefRangeEnd_Type()
)
frimSysConRefRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSysConRefRangeEnd.setStatus("mandatory")
_FrimSRTable_Object = MibTable
frimSRTable = _FrimSRTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6)
)
if mibBuilder.loadTexts:
    frimSRTable.setStatus("mandatory")
_FrimSREntry_Object = MibTableRow
frimSREntry = _FrimSREntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1)
)
frimSREntry.setIndexNames(
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSRFrpCircuitSapId"),
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSRFrpCircuitDlci"),
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSRProtocolId"),
    (0, "CXFrameRelayInterfaceModule-MIB", "frimSRSubRef"),
)
if mibBuilder.loadTexts:
    frimSREntry.setStatus("mandatory")
_FrimSRFrpCircuitSapId_Type = SapIndex
_FrimSRFrpCircuitSapId_Object = MibTableColumn
frimSRFrpCircuitSapId = _FrimSRFrpCircuitSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 1),
    _FrimSRFrpCircuitSapId_Type()
)
frimSRFrpCircuitSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSRFrpCircuitSapId.setStatus("mandatory")
_FrimSRFrpCircuitDlci_Type = DLCI
_FrimSRFrpCircuitDlci_Object = MibTableColumn
frimSRFrpCircuitDlci = _FrimSRFrpCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 2),
    _FrimSRFrpCircuitDlci_Type()
)
frimSRFrpCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSRFrpCircuitDlci.setStatus("mandatory")


class _FrimSRProtocolId_Type(Integer32):
    """Custom type frimSRProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FrimSRProtocolId_Type.__name__ = "Integer32"
_FrimSRProtocolId_Object = MibTableColumn
frimSRProtocolId = _FrimSRProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 3),
    _FrimSRProtocolId_Type()
)
frimSRProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSRProtocolId.setStatus("mandatory")
_FrimSRSubRef_Type = SubRef
_FrimSRSubRef_Object = MibTableColumn
frimSRSubRef = _FrimSRSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 4),
    _FrimSRSubRef_Type()
)
frimSRSubRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSRSubRef.setStatus("mandatory")
_FrimSRRefRangeEnd_Type = SubRef
_FrimSRRefRangeEnd_Object = MibTableColumn
frimSRRefRangeEnd = _FrimSRRefRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 5),
    _FrimSRRefRangeEnd_Type()
)
frimSRRefRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSRRefRangeEnd.setStatus("mandatory")


class _FrimSRRowStatus_Type(Integer32):
    """Custom type frimSRRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_FrimSRRowStatus_Type.__name__ = "Integer32"
_FrimSRRowStatus_Object = MibTableColumn
frimSRRowStatus = _FrimSRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 6),
    _FrimSRRowStatus_Type()
)
frimSRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSRRowStatus.setStatus("mandatory")
_FrimSRDestFrpCircuitAlias_Type = Alias
_FrimSRDestFrpCircuitAlias_Object = MibTableColumn
frimSRDestFrpCircuitAlias = _FrimSRDestFrpCircuitAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 7),
    _FrimSRDestFrpCircuitAlias_Type()
)
frimSRDestFrpCircuitAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSRDestFrpCircuitAlias.setStatus("mandatory")
_FrimSRDestSubRef_Type = SubRef
_FrimSRDestSubRef_Object = MibTableColumn
frimSRDestSubRef = _FrimSRDestSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 8),
    _FrimSRDestSubRef_Type()
)
frimSRDestSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frimSRDestSubRef.setStatus("mandatory")


class _FrimSRRouteStatus_Type(Integer32):
    """Custom type frimSRRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("inProgress", 2),
          ("notConnected", 1))
    )


_FrimSRRouteStatus_Type.__name__ = "Integer32"
_FrimSRRouteStatus_Object = MibTableColumn
frimSRRouteStatus = _FrimSRRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 15),
    _FrimSRRouteStatus_Type()
)
frimSRRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSRRouteStatus.setStatus("mandatory")


class _FrimSRClearStatus_Type(Integer32):
    """Custom type frimSRClearStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 2),
          ("localAllocFailure", 3),
          ("localDsnFailure", 13),
          ("localFcnFailure", 11),
          ("localNoAccess", 5),
          ("localPvcBusy", 9),
          ("localPvcDown", 7),
          ("localRefInUse", 14),
          ("noFailure", 1),
          ("remoteAliasNotFound", 15),
          ("remoteAllocFailure", 4),
          ("remoteFcnFailure", 12),
          ("remoteNoAccess", 6),
          ("remoteNoPvcService", 16),
          ("remotePvcBusy", 10),
          ("remotePvcDown", 8))
    )


_FrimSRClearStatus_Type.__name__ = "Integer32"
_FrimSRClearStatus_Object = MibTableColumn
frimSRClearStatus = _FrimSRClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2, 6, 1, 16),
    _FrimSRClearStatus_Type()
)
frimSRClearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frimSRClearStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFrameRelayInterfaceModule-MIB",
    **{"SubRef": SubRef,
       "frimSRConnectInterval": frimSRConnectInterval,
       "frimServiceCost": frimServiceCost,
       "frimSapTable": frimSapTable,
       "frimSapEntry": frimSapEntry,
       "frimSapId": frimSapId,
       "frimSapRowStatus": frimSapRowStatus,
       "frimSapType": frimSapType,
       "frimSapAlias": frimSapAlias,
       "frimSapCompanionAlias": frimSapCompanionAlias,
       "frimSapMaxDlcis": frimSapMaxDlcis,
       "frimSapMaxErrorFrames": frimSapMaxErrorFrames,
       "frimSapMonitorFrames": frimSapMonitorFrames,
       "frimSapFrWindowSize": frimSapFrWindowSize,
       "frimSapControlStats": frimSapControlStats,
       "frimSapstatRxDataFrames": frimSapstatRxDataFrames,
       "frimSapstatRxDataOctets": frimSapstatRxDataOctets,
       "frimSapstatTxDataFrames": frimSapstatTxDataFrames,
       "frimSapstatTxDataOctets": frimSapstatTxDataOctets,
       "frimSapstatUnopenedServiceDiscards": frimSapstatUnopenedServiceDiscards,
       "frimSapstatPvcDownDiscards": frimSapstatPvcDownDiscards,
       "frimSapstatUserSuccessfulOpens": frimSapstatUserSuccessfulOpens,
       "frimSapstatUserUnsuccessfulOpens": frimSapstatUserUnsuccessfulOpens,
       "frimSapstatSRSuccessfulConnects": frimSapstatSRSuccessfulConnects,
       "frimSapstatSRUnsuccessfulConnects": frimSapstatSRUnsuccessfulConnects,
       "frimSapstatTxResets": frimSapstatTxResets,
       "frimSapstatRxBECN": frimSapstatRxBECN,
       "frimSapstatRxFECN": frimSapstatRxFECN,
       "frimSysConTable": frimSysConTable,
       "frimSysConEntry": frimSysConEntry,
       "frimSysConSapId": frimSysConSapId,
       "frimSysConDlci": frimSysConDlci,
       "frimSysConPid": frimSysConPid,
       "frimSysConRef": frimSysConRef,
       "frimSysConRemoteSlot": frimSysConRemoteSlot,
       "frimSysConCreationTime": frimSysConCreationTime,
       "frimSysConReqDataSize": frimSysConReqDataSize,
       "frimSysConNegDataSize": frimSysConNegDataSize,
       "frimSysConNegSizeExceededFrames": frimSysConNegSizeExceededFrames,
       "frimSysConRefRangeEnd": frimSysConRefRangeEnd,
       "frimSRTable": frimSRTable,
       "frimSREntry": frimSREntry,
       "frimSRFrpCircuitSapId": frimSRFrpCircuitSapId,
       "frimSRFrpCircuitDlci": frimSRFrpCircuitDlci,
       "frimSRProtocolId": frimSRProtocolId,
       "frimSRSubRef": frimSRSubRef,
       "frimSRRefRangeEnd": frimSRRefRangeEnd,
       "frimSRRowStatus": frimSRRowStatus,
       "frimSRDestFrpCircuitAlias": frimSRDestFrpCircuitAlias,
       "frimSRDestSubRef": frimSRDestSubRef,
       "frimSRRouteStatus": frimSRRouteStatus,
       "frimSRClearStatus": frimSRClearStatus}
)
