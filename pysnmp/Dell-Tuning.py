# SNMP MIB module (Dell-Tuning) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-Tuning
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:09 2024
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

(VlanList1,
 VlanList2,
 VlanList3,
 VlanList4) = mibBuilder.importSymbols(
    "Dell-BRIDGEMIBOBJECTS-MIB",
    "VlanList1",
    "VlanList2",
    "VlanList3",
    "VlanList4")

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsTunning = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29)
)
rsTunning.setRevisions(
        ("2009-03-03 00:00",
         "2006-02-12 00:00",
         "2004-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsHighPriority_Type = Integer32
_RsHighPriority_Object = MibScalar
rsHighPriority = _RsHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 1),
    _RsHighPriority_Type()
)
rsHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsHighPriority.setStatus("current")
_RsLowPriority_Type = Integer32
_RsLowPriority_Object = MibScalar
rsLowPriority = _RsLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 2),
    _RsLowPriority_Type()
)
rsLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLowPriority.setStatus("current")
_RsDbgLevel_Type = Integer32
_RsDbgLevel_Object = MibScalar
rsDbgLevel = _RsDbgLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 3),
    _RsDbgLevel_Type()
)
rsDbgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDbgLevel.setStatus("current")
_RsDiagnosticsTable_Object = MibTable
rsDiagnosticsTable = _RsDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4)
)
if mibBuilder.loadTexts:
    rsDiagnosticsTable.setStatus("current")
_RsDiagnosticsEntry_Object = MibTableRow
rsDiagnosticsEntry = _RsDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4, 1)
)
rsDiagnosticsEntry.setIndexNames(
    (0, "Dell-Tuning", "rsDiagnosticsRequestId"),
)
if mibBuilder.loadTexts:
    rsDiagnosticsEntry.setStatus("current")
_RsDiagnosticsRequestId_Type = Integer32
_RsDiagnosticsRequestId_Object = MibTableColumn
rsDiagnosticsRequestId = _RsDiagnosticsRequestId_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4, 1, 1),
    _RsDiagnosticsRequestId_Type()
)
rsDiagnosticsRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiagnosticsRequestId.setStatus("current")
_RsDiagnosticsCode_Type = Integer32
_RsDiagnosticsCode_Object = MibTableColumn
rsDiagnosticsCode = _RsDiagnosticsCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4, 1, 2),
    _RsDiagnosticsCode_Type()
)
rsDiagnosticsCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiagnosticsCode.setStatus("current")
_RsDiagnosticsLocation_Type = Integer32
_RsDiagnosticsLocation_Object = MibTableColumn
rsDiagnosticsLocation = _RsDiagnosticsLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4, 1, 3),
    _RsDiagnosticsLocation_Type()
)
rsDiagnosticsLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiagnosticsLocation.setStatus("current")


class _RsDiagnosticsText_Type(DisplayString):
    """Custom type rsDiagnosticsText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RsDiagnosticsText_Type.__name__ = "DisplayString"
_RsDiagnosticsText_Object = MibTableColumn
rsDiagnosticsText = _RsDiagnosticsText_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4, 1, 4),
    _RsDiagnosticsText_Type()
)
rsDiagnosticsText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiagnosticsText.setStatus("current")
_RsConfirmMessagTab_Type = Integer32
_RsConfirmMessagTab_Object = MibScalar
rsConfirmMessagTab = _RsConfirmMessagTab_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 5),
    _RsConfirmMessagTab_Type()
)
rsConfirmMessagTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsConfirmMessagTab.setStatus("current")
_EventMessageTable_Object = MibTable
eventMessageTable = _EventMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6)
)
if mibBuilder.loadTexts:
    eventMessageTable.setStatus("current")
_EventMessageEntry_Object = MibTableRow
eventMessageEntry = _EventMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1)
)
eventMessageEntry.setIndexNames(
    (0, "Dell-Tuning", "eventNum"),
)
if mibBuilder.loadTexts:
    eventMessageEntry.setStatus("current")
_EventNum_Type = Integer32
_EventNum_Object = MibTableColumn
eventNum = _EventNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1, 1),
    _EventNum_Type()
)
eventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNum.setStatus("current")
_EventDesc_Type = DisplayString
_EventDesc_Object = MibTableColumn
eventDesc = _EventDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1, 2),
    _EventDesc_Type()
)
eventDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDesc.setStatus("current")
_ReaTunning_ObjectIdentity = ObjectIdentity
reaTunning = _ReaTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 7)
)


class _ReaIpForwardEnable_Type(Integer32):
    """Custom type reaIpForwardEnable based on Integer32"""
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


_ReaIpForwardEnable_Type.__name__ = "Integer32"
_ReaIpForwardEnable_Object = MibScalar
reaIpForwardEnable = _ReaIpForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 4),
    _ReaIpForwardEnable_Type()
)
reaIpForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpForwardEnable.setStatus("current")


class _ReaIpxForwardEnable_Type(Integer32):
    """Custom type reaIpxForwardEnable based on Integer32"""
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


_ReaIpxForwardEnable_Type.__name__ = "Integer32"
_ReaIpxForwardEnable_Object = MibScalar
reaIpxForwardEnable = _ReaIpxForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 5),
    _ReaIpxForwardEnable_Type()
)
reaIpxForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpxForwardEnable.setStatus("current")
_RsMaxEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxEntriesTuning = _RsMaxEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8)
)
_RsMaxBridgeForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxBridgeForwardingEntriesTuning = _RsMaxBridgeForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1)
)
_RsMaxBrgFrwEntries_Type = Integer32
_RsMaxBrgFrwEntries_Object = MibScalar
rsMaxBrgFrwEntries = _RsMaxBrgFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1, 1),
    _RsMaxBrgFrwEntries_Type()
)
rsMaxBrgFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxBrgFrwEntries.setStatus("current")
_RsMaxBrgFrwEntriesAfterReset_Type = Integer32
_RsMaxBrgFrwEntriesAfterReset_Object = MibScalar
rsMaxBrgFrwEntriesAfterReset = _RsMaxBrgFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1, 2),
    _RsMaxBrgFrwEntriesAfterReset_Type()
)
rsMaxBrgFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxBrgFrwEntriesAfterReset.setStatus("current")
_RsMaxIpForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpForwardingEntriesTuning = _RsMaxIpForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2)
)
_RsMaxIpFrwEntries_Type = Integer32
_RsMaxIpFrwEntries_Object = MibScalar
rsMaxIpFrwEntries = _RsMaxIpFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2, 1),
    _RsMaxIpFrwEntries_Type()
)
rsMaxIpFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpFrwEntries.setStatus("current")
_RsMaxIpFrwEntriesAfterReset_Type = Integer32
_RsMaxIpFrwEntriesAfterReset_Object = MibScalar
rsMaxIpFrwEntriesAfterReset = _RsMaxIpFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2, 2),
    _RsMaxIpFrwEntriesAfterReset_Type()
)
rsMaxIpFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpFrwEntriesAfterReset.setStatus("current")
_RsMaxArpEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxArpEntriesTuning = _RsMaxArpEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3)
)
_RsMaxArpEntries_Type = Integer32
_RsMaxArpEntries_Object = MibScalar
rsMaxArpEntries = _RsMaxArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3, 1),
    _RsMaxArpEntries_Type()
)
rsMaxArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxArpEntries.setStatus("current")
_RsMaxArpEntriesAfterReset_Type = Integer32
_RsMaxArpEntriesAfterReset_Object = MibScalar
rsMaxArpEntriesAfterReset = _RsMaxArpEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3, 2),
    _RsMaxArpEntriesAfterReset_Type()
)
rsMaxArpEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxArpEntriesAfterReset.setStatus("current")
_RsMaxIpxForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxForwardingEntriesTuning = _RsMaxIpxForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4)
)
_RsMaxIpxFrwEntries_Type = Integer32
_RsMaxIpxFrwEntries_Object = MibScalar
rsMaxIpxFrwEntries = _RsMaxIpxFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4, 1),
    _RsMaxIpxFrwEntries_Type()
)
rsMaxIpxFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxFrwEntries.setStatus("current")
_RsMaxIpxFrwEntriesAfterReset_Type = Integer32
_RsMaxIpxFrwEntriesAfterReset_Object = MibScalar
rsMaxIpxFrwEntriesAfterReset = _RsMaxIpxFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4, 2),
    _RsMaxIpxFrwEntriesAfterReset_Type()
)
rsMaxIpxFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxFrwEntriesAfterReset.setStatus("current")
_RsMaxIpxSapEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxSapEntriesTuning = _RsMaxIpxSapEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5)
)
_RsMaxIpxSapEntries_Type = Integer32
_RsMaxIpxSapEntries_Object = MibScalar
rsMaxIpxSapEntries = _RsMaxIpxSapEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5, 1),
    _RsMaxIpxSapEntries_Type()
)
rsMaxIpxSapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxSapEntries.setStatus("current")
_RsMaxIpxSapEntriesAfterReset_Type = Integer32
_RsMaxIpxSapEntriesAfterReset_Object = MibScalar
rsMaxIpxSapEntriesAfterReset = _RsMaxIpxSapEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5, 2),
    _RsMaxIpxSapEntriesAfterReset_Type()
)
rsMaxIpxSapEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxSapEntriesAfterReset.setStatus("current")
_RsMaxDspClntEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxDspClntEntriesTuning = _RsMaxDspClntEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6)
)
_RsMaxDspClntEntries_Type = Integer32
_RsMaxDspClntEntries_Object = MibScalar
rsMaxDspClntEntries = _RsMaxDspClntEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6, 1),
    _RsMaxDspClntEntries_Type()
)
rsMaxDspClntEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDspClntEntries.setStatus("current")
_RsMaxDspClntEntriesAfterReset_Type = Integer32
_RsMaxDspClntEntriesAfterReset_Object = MibScalar
rsMaxDspClntEntriesAfterReset = _RsMaxDspClntEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6, 2),
    _RsMaxDspClntEntriesAfterReset_Type()
)
rsMaxDspClntEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDspClntEntriesAfterReset.setStatus("current")
_RsMaxIpFftEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpFftEntriesTuning = _RsMaxIpFftEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9)
)
_RsMaxIpSFftEntries_Type = Integer32
_RsMaxIpSFftEntries_Object = MibScalar
rsMaxIpSFftEntries = _RsMaxIpSFftEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 1),
    _RsMaxIpSFftEntries_Type()
)
rsMaxIpSFftEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpSFftEntries.setStatus("current")
_RsMaxIpSFftEntriesAfterReset_Type = Integer32
_RsMaxIpSFftEntriesAfterReset_Object = MibScalar
rsMaxIpSFftEntriesAfterReset = _RsMaxIpSFftEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 2),
    _RsMaxIpSFftEntriesAfterReset_Type()
)
rsMaxIpSFftEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpSFftEntriesAfterReset.setStatus("current")
_RsMaxIpNFftEntries_Type = Integer32
_RsMaxIpNFftEntries_Object = MibScalar
rsMaxIpNFftEntries = _RsMaxIpNFftEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 3),
    _RsMaxIpNFftEntries_Type()
)
rsMaxIpNFftEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpNFftEntries.setStatus("current")
_RsMaxIpNFftEntriesAfterReset_Type = Integer32
_RsMaxIpNFftEntriesAfterReset_Object = MibScalar
rsMaxIpNFftEntriesAfterReset = _RsMaxIpNFftEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 4),
    _RsMaxIpNFftEntriesAfterReset_Type()
)
rsMaxIpNFftEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpNFftEntriesAfterReset.setStatus("current")
_RsMaxIpSFftSysEntries_Type = Integer32
_RsMaxIpSFftSysEntries_Object = MibScalar
rsMaxIpSFftSysEntries = _RsMaxIpSFftSysEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 5),
    _RsMaxIpSFftSysEntries_Type()
)
rsMaxIpSFftSysEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpSFftSysEntries.setStatus("current")
_RsMaxIpSFftSysEntriesAfterReset_Type = Integer32
_RsMaxIpSFftSysEntriesAfterReset_Object = MibScalar
rsMaxIpSFftSysEntriesAfterReset = _RsMaxIpSFftSysEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 6),
    _RsMaxIpSFftSysEntriesAfterReset_Type()
)
rsMaxIpSFftSysEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpSFftSysEntriesAfterReset.setStatus("current")
_RsMaxIpNFftSysEntries_Type = Integer32
_RsMaxIpNFftSysEntries_Object = MibScalar
rsMaxIpNFftSysEntries = _RsMaxIpNFftSysEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 7),
    _RsMaxIpNFftSysEntries_Type()
)
rsMaxIpNFftSysEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpNFftSysEntries.setStatus("current")
_RsMaxIpNFftSysEntriesAfterReset_Type = Integer32
_RsMaxIpNFftSysEntriesAfterReset_Object = MibScalar
rsMaxIpNFftSysEntriesAfterReset = _RsMaxIpNFftSysEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 8),
    _RsMaxIpNFftSysEntriesAfterReset_Type()
)
rsMaxIpNFftSysEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpNFftSysEntriesAfterReset.setStatus("current")
_RsMaxIpNextHopEntries_Type = Integer32
_RsMaxIpNextHopEntries_Object = MibScalar
rsMaxIpNextHopEntries = _RsMaxIpNextHopEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 9),
    _RsMaxIpNextHopEntries_Type()
)
rsMaxIpNextHopEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpNextHopEntries.setStatus("current")
_RsMaxIpNextHopEntriesAfterReset_Type = Integer32
_RsMaxIpNextHopEntriesAfterReset_Object = MibScalar
rsMaxIpNextHopEntriesAfterReset = _RsMaxIpNextHopEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 10),
    _RsMaxIpNextHopEntriesAfterReset_Type()
)
rsMaxIpNextHopEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpNextHopEntriesAfterReset.setStatus("current")
_RsMaxIpxFftEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxFftEntriesTuning = _RsMaxIpxFftEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10)
)
_RsMaxIpxSFftEntries_Type = Integer32
_RsMaxIpxSFftEntries_Object = MibScalar
rsMaxIpxSFftEntries = _RsMaxIpxSFftEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 1),
    _RsMaxIpxSFftEntries_Type()
)
rsMaxIpxSFftEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxSFftEntries.setStatus("current")
_RsMaxIpxSFftEntriesAfterReset_Type = Integer32
_RsMaxIpxSFftEntriesAfterReset_Object = MibScalar
rsMaxIpxSFftEntriesAfterReset = _RsMaxIpxSFftEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 2),
    _RsMaxIpxSFftEntriesAfterReset_Type()
)
rsMaxIpxSFftEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxSFftEntriesAfterReset.setStatus("current")
_RsMaxIpxNFftEntries_Type = Integer32
_RsMaxIpxNFftEntries_Object = MibScalar
rsMaxIpxNFftEntries = _RsMaxIpxNFftEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 3),
    _RsMaxIpxNFftEntries_Type()
)
rsMaxIpxNFftEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxNFftEntries.setStatus("current")
_RsMaxIpxNFftEntriesAfterReset_Type = Integer32
_RsMaxIpxNFftEntriesAfterReset_Object = MibScalar
rsMaxIpxNFftEntriesAfterReset = _RsMaxIpxNFftEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 4),
    _RsMaxIpxNFftEntriesAfterReset_Type()
)
rsMaxIpxNFftEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxNFftEntriesAfterReset.setStatus("current")
_RsMaxIpxSFftSysEntries_Type = Integer32
_RsMaxIpxSFftSysEntries_Object = MibScalar
rsMaxIpxSFftSysEntries = _RsMaxIpxSFftSysEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 5),
    _RsMaxIpxSFftSysEntries_Type()
)
rsMaxIpxSFftSysEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxSFftSysEntries.setStatus("current")
_RsMaxIpxSFftSysEntriesAfterReset_Type = Integer32
_RsMaxIpxSFftSysEntriesAfterReset_Object = MibScalar
rsMaxIpxSFftSysEntriesAfterReset = _RsMaxIpxSFftSysEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 6),
    _RsMaxIpxSFftSysEntriesAfterReset_Type()
)
rsMaxIpxSFftSysEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxSFftSysEntriesAfterReset.setStatus("current")
_RsMaxIpxNFftSysEntries_Type = Integer32
_RsMaxIpxNFftSysEntries_Object = MibScalar
rsMaxIpxNFftSysEntries = _RsMaxIpxNFftSysEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 7),
    _RsMaxIpxNFftSysEntries_Type()
)
rsMaxIpxNFftSysEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxNFftSysEntries.setStatus("current")
_RsMaxIpxNFftSysEntriesAfterReset_Type = Integer32
_RsMaxIpxNFftSysEntriesAfterReset_Object = MibScalar
rsMaxIpxNFftSysEntriesAfterReset = _RsMaxIpxNFftSysEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 10, 8),
    _RsMaxIpxNFftSysEntriesAfterReset_Type()
)
rsMaxIpxNFftSysEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxNFftSysEntriesAfterReset.setStatus("current")
_RsMaxDhcpTuning_ObjectIdentity = ObjectIdentity
rsMaxDhcpTuning = _RsMaxDhcpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 11)
)
_RsMaxDhcpConns_Type = Integer32
_RsMaxDhcpConns_Object = MibScalar
rsMaxDhcpConns = _RsMaxDhcpConns_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 11, 1),
    _RsMaxDhcpConns_Type()
)
rsMaxDhcpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDhcpConns.setStatus("current")
_RsMaxDhcpConnsAfterReset_Type = Integer32
_RsMaxDhcpConnsAfterReset_Object = MibScalar
rsMaxDhcpConnsAfterReset = _RsMaxDhcpConnsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 11, 2),
    _RsMaxDhcpConnsAfterReset_Type()
)
rsMaxDhcpConnsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDhcpConnsAfterReset.setStatus("current")
_RsMaxIpmTuning_ObjectIdentity = ObjectIdentity
rsMaxIpmTuning = _RsMaxIpmTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12)
)
_RsMaxIpmFftEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpmFftEntriesTuning = _RsMaxIpmFftEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 1)
)
_RsMaxIpmFftEntries_Type = Integer32
_RsMaxIpmFftEntries_Object = MibScalar
rsMaxIpmFftEntries = _RsMaxIpmFftEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 1, 1),
    _RsMaxIpmFftEntries_Type()
)
rsMaxIpmFftEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpmFftEntries.setStatus("current")
_RsMaxIpmFftEntriesAfterReset_Type = Integer32
_RsMaxIpmFftEntriesAfterReset_Object = MibScalar
rsMaxIpmFftEntriesAfterReset = _RsMaxIpmFftEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 1, 2),
    _RsMaxIpmFftEntriesAfterReset_Type()
)
rsMaxIpmFftEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpmFftEntriesAfterReset.setStatus("current")
_RsIpmFftAging_Type = Integer32
_RsIpmFftAging_Object = MibScalar
rsIpmFftAging = _RsIpmFftAging_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 1, 3),
    _RsIpmFftAging_Type()
)
rsIpmFftAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpmFftAging.setStatus("current")
_RsMaxIgmpTuning_ObjectIdentity = ObjectIdentity
rsMaxIgmpTuning = _RsMaxIgmpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 2)
)
_RsMaxIgmpInterfaceEntries_Type = Integer32
_RsMaxIgmpInterfaceEntries_Object = MibScalar
rsMaxIgmpInterfaceEntries = _RsMaxIgmpInterfaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 2, 1),
    _RsMaxIgmpInterfaceEntries_Type()
)
rsMaxIgmpInterfaceEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIgmpInterfaceEntries.setStatus("current")
_RsMaxIgmpInterfaceEntriesAfterReset_Type = Integer32
_RsMaxIgmpInterfaceEntriesAfterReset_Object = MibScalar
rsMaxIgmpInterfaceEntriesAfterReset = _RsMaxIgmpInterfaceEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 2, 2),
    _RsMaxIgmpInterfaceEntriesAfterReset_Type()
)
rsMaxIgmpInterfaceEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIgmpInterfaceEntriesAfterReset.setStatus("current")
_RsMaxIgmpCacheEntries_Type = Integer32
_RsMaxIgmpCacheEntries_Object = MibScalar
rsMaxIgmpCacheEntries = _RsMaxIgmpCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 2, 3),
    _RsMaxIgmpCacheEntries_Type()
)
rsMaxIgmpCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIgmpCacheEntries.setStatus("current")
_RsMaxIgmpCacheEntriesAfterReset_Type = Integer32
_RsMaxIgmpCacheEntriesAfterReset_Object = MibScalar
rsMaxIgmpCacheEntriesAfterReset = _RsMaxIgmpCacheEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 2, 4),
    _RsMaxIgmpCacheEntriesAfterReset_Type()
)
rsMaxIgmpCacheEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIgmpCacheEntriesAfterReset.setStatus("current")
_RsMaxPimTuning_ObjectIdentity = ObjectIdentity
rsMaxPimTuning = _RsMaxPimTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3)
)
_RsMaxPimNeighborEntries_Type = Integer32
_RsMaxPimNeighborEntries_Object = MibScalar
rsMaxPimNeighborEntries = _RsMaxPimNeighborEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 1),
    _RsMaxPimNeighborEntries_Type()
)
rsMaxPimNeighborEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimNeighborEntries.setStatus("current")
_RsMaxPimNeighborEntriesAfterReset_Type = Integer32
_RsMaxPimNeighborEntriesAfterReset_Object = MibScalar
rsMaxPimNeighborEntriesAfterReset = _RsMaxPimNeighborEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 2),
    _RsMaxPimNeighborEntriesAfterReset_Type()
)
rsMaxPimNeighborEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimNeighborEntriesAfterReset.setStatus("current")
_RsMaxPimRouteEntries_Type = Integer32
_RsMaxPimRouteEntries_Object = MibScalar
rsMaxPimRouteEntries = _RsMaxPimRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 3),
    _RsMaxPimRouteEntries_Type()
)
rsMaxPimRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimRouteEntries.setStatus("current")
_RsMaxPimRouteEntriesAfterReset_Type = Integer32
_RsMaxPimRouteEntriesAfterReset_Object = MibScalar
rsMaxPimRouteEntriesAfterReset = _RsMaxPimRouteEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 4),
    _RsMaxPimRouteEntriesAfterReset_Type()
)
rsMaxPimRouteEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimRouteEntriesAfterReset.setStatus("current")
_RsMaxPimRouteNextHopEntries_Type = Integer32
_RsMaxPimRouteNextHopEntries_Object = MibScalar
rsMaxPimRouteNextHopEntries = _RsMaxPimRouteNextHopEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 5),
    _RsMaxPimRouteNextHopEntries_Type()
)
rsMaxPimRouteNextHopEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimRouteNextHopEntries.setStatus("current")
_RsMaxPimRouteNextHopEntriesAfterReset_Type = Integer32
_RsMaxPimRouteNextHopEntriesAfterReset_Object = MibScalar
rsMaxPimRouteNextHopEntriesAfterReset = _RsMaxPimRouteNextHopEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 6),
    _RsMaxPimRouteNextHopEntriesAfterReset_Type()
)
rsMaxPimRouteNextHopEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimRouteNextHopEntriesAfterReset.setStatus("current")
_RsMaxPimInterfaceEntriesAfterReset_Type = Integer32
_RsMaxPimInterfaceEntriesAfterReset_Object = MibScalar
rsMaxPimInterfaceEntriesAfterReset = _RsMaxPimInterfaceEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 7),
    _RsMaxPimInterfaceEntriesAfterReset_Type()
)
rsMaxPimInterfaceEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimInterfaceEntriesAfterReset.setStatus("current")
_RsMaxPimInterfaceEntries_Type = Integer32
_RsMaxPimInterfaceEntries_Object = MibScalar
rsMaxPimInterfaceEntries = _RsMaxPimInterfaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 3, 8),
    _RsMaxPimInterfaceEntries_Type()
)
rsMaxPimInterfaceEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimInterfaceEntries.setStatus("current")
_RsMaxDvmrpTuning_ObjectIdentity = ObjectIdentity
rsMaxDvmrpTuning = _RsMaxDvmrpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4)
)
_RsMaxDvmrpNeighborEntries_Type = Integer32
_RsMaxDvmrpNeighborEntries_Object = MibScalar
rsMaxDvmrpNeighborEntries = _RsMaxDvmrpNeighborEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 1),
    _RsMaxDvmrpNeighborEntries_Type()
)
rsMaxDvmrpNeighborEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDvmrpNeighborEntries.setStatus("current")
_RsMaxDvmrpNeighborEntriesAfterReset_Type = Integer32
_RsMaxDvmrpNeighborEntriesAfterReset_Object = MibScalar
rsMaxDvmrpNeighborEntriesAfterReset = _RsMaxDvmrpNeighborEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 2),
    _RsMaxDvmrpNeighborEntriesAfterReset_Type()
)
rsMaxDvmrpNeighborEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDvmrpNeighborEntriesAfterReset.setStatus("current")
_RsMaxDvmrpRouteEntries_Type = Integer32
_RsMaxDvmrpRouteEntries_Object = MibScalar
rsMaxDvmrpRouteEntries = _RsMaxDvmrpRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 3),
    _RsMaxDvmrpRouteEntries_Type()
)
rsMaxDvmrpRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDvmrpRouteEntries.setStatus("current")
_RsMaxDvmrpRouteEntriesAfterReset_Type = Integer32
_RsMaxDvmrpRouteEntriesAfterReset_Object = MibScalar
rsMaxDvmrpRouteEntriesAfterReset = _RsMaxDvmrpRouteEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 4),
    _RsMaxDvmrpRouteEntriesAfterReset_Type()
)
rsMaxDvmrpRouteEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDvmrpRouteEntriesAfterReset.setStatus("current")
_RsMaxDvmrpMRouteEntries_Type = Integer32
_RsMaxDvmrpMRouteEntries_Object = MibScalar
rsMaxDvmrpMRouteEntries = _RsMaxDvmrpMRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 5),
    _RsMaxDvmrpMRouteEntries_Type()
)
rsMaxDvmrpMRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDvmrpMRouteEntries.setStatus("current")
_RsMaxDvmrpMRouteEntriesAfterReset_Type = Integer32
_RsMaxDvmrpMRouteEntriesAfterReset_Object = MibScalar
rsMaxDvmrpMRouteEntriesAfterReset = _RsMaxDvmrpMRouteEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 6),
    _RsMaxDvmrpMRouteEntriesAfterReset_Type()
)
rsMaxDvmrpMRouteEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDvmrpMRouteEntriesAfterReset.setStatus("current")
_RsMaxDvmrpInterfaceEntries_Type = Integer32
_RsMaxDvmrpInterfaceEntries_Object = MibScalar
rsMaxDvmrpInterfaceEntries = _RsMaxDvmrpInterfaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 7),
    _RsMaxDvmrpInterfaceEntries_Type()
)
rsMaxDvmrpInterfaceEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDvmrpInterfaceEntries.setStatus("current")
_RsMaxDvmrpInterfaceEntriesAfterReset_Type = Integer32
_RsMaxDvmrpInterfaceEntriesAfterReset_Object = MibScalar
rsMaxDvmrpInterfaceEntriesAfterReset = _RsMaxDvmrpInterfaceEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 4, 8),
    _RsMaxDvmrpInterfaceEntriesAfterReset_Type()
)
rsMaxDvmrpInterfaceEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDvmrpInterfaceEntriesAfterReset.setStatus("current")
_RsMaxPigmpTuning_ObjectIdentity = ObjectIdentity
rsMaxPigmpTuning = _RsMaxPigmpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 5)
)
_RsMaxPigmpRouteEntries_Type = Integer32
_RsMaxPigmpRouteEntries_Object = MibScalar
rsMaxPigmpRouteEntries = _RsMaxPigmpRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 5, 1),
    _RsMaxPigmpRouteEntries_Type()
)
rsMaxPigmpRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPigmpRouteEntries.setStatus("current")
_RsMaxPigmpRouteEntriesAfterReset_Type = Integer32
_RsMaxPigmpRouteEntriesAfterReset_Object = MibScalar
rsMaxPigmpRouteEntriesAfterReset = _RsMaxPigmpRouteEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 5, 2),
    _RsMaxPigmpRouteEntriesAfterReset_Type()
)
rsMaxPigmpRouteEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPigmpRouteEntriesAfterReset.setStatus("current")
_RsMaxPimSmTuning_ObjectIdentity = ObjectIdentity
rsMaxPimSmTuning = _RsMaxPimSmTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6)
)
_RsMaxPimSmNeighborEntries_Type = Integer32
_RsMaxPimSmNeighborEntries_Object = MibScalar
rsMaxPimSmNeighborEntries = _RsMaxPimSmNeighborEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 1),
    _RsMaxPimSmNeighborEntries_Type()
)
rsMaxPimSmNeighborEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimSmNeighborEntries.setStatus("current")
_RsMaxPimSmNeighborEntriesAfterReset_Type = Integer32
_RsMaxPimSmNeighborEntriesAfterReset_Object = MibScalar
rsMaxPimSmNeighborEntriesAfterReset = _RsMaxPimSmNeighborEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 2),
    _RsMaxPimSmNeighborEntriesAfterReset_Type()
)
rsMaxPimSmNeighborEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimSmNeighborEntriesAfterReset.setStatus("current")
_RsMaxPimSmRouteEntries_Type = Integer32
_RsMaxPimSmRouteEntries_Object = MibScalar
rsMaxPimSmRouteEntries = _RsMaxPimSmRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 3),
    _RsMaxPimSmRouteEntries_Type()
)
rsMaxPimSmRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimSmRouteEntries.setStatus("current")
_RsMaxPimSmRouteEntriesAfterReset_Type = Integer32
_RsMaxPimSmRouteEntriesAfterReset_Object = MibScalar
rsMaxPimSmRouteEntriesAfterReset = _RsMaxPimSmRouteEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 4),
    _RsMaxPimSmRouteEntriesAfterReset_Type()
)
rsMaxPimSmRouteEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimSmRouteEntriesAfterReset.setStatus("current")
_RsMaxPimSmInterfaceEntries_Type = Integer32
_RsMaxPimSmInterfaceEntries_Object = MibScalar
rsMaxPimSmInterfaceEntries = _RsMaxPimSmInterfaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 5),
    _RsMaxPimSmInterfaceEntries_Type()
)
rsMaxPimSmInterfaceEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimSmInterfaceEntries.setStatus("current")
_RsMaxPimSmInterfaceEntriesAfterReset_Type = Integer32
_RsMaxPimSmInterfaceEntriesAfterReset_Object = MibScalar
rsMaxPimSmInterfaceEntriesAfterReset = _RsMaxPimSmInterfaceEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 6),
    _RsMaxPimSmInterfaceEntriesAfterReset_Type()
)
rsMaxPimSmInterfaceEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimSmInterfaceEntriesAfterReset.setStatus("current")
_RsMaxPimSmRPSetEntries_Type = Integer32
_RsMaxPimSmRPSetEntries_Object = MibScalar
rsMaxPimSmRPSetEntries = _RsMaxPimSmRPSetEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 7),
    _RsMaxPimSmRPSetEntries_Type()
)
rsMaxPimSmRPSetEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimSmRPSetEntries.setStatus("current")
_RsMaxPimSmRPSetEntriesAfterReset_Type = Integer32
_RsMaxPimSmRPSetEntriesAfterReset_Object = MibScalar
rsMaxPimSmRPSetEntriesAfterReset = _RsMaxPimSmRPSetEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 8),
    _RsMaxPimSmRPSetEntriesAfterReset_Type()
)
rsMaxPimSmRPSetEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimSmRPSetEntriesAfterReset.setStatus("current")
_RsMaxPimSmCRPEntries_Type = Integer32
_RsMaxPimSmCRPEntries_Object = MibScalar
rsMaxPimSmCRPEntries = _RsMaxPimSmCRPEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 9),
    _RsMaxPimSmCRPEntries_Type()
)
rsMaxPimSmCRPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPimSmCRPEntries.setStatus("current")
_RsMaxPimSmCRPEntriesAfterReset_Type = Integer32
_RsMaxPimSmCRPEntriesAfterReset_Object = MibScalar
rsMaxPimSmCRPEntriesAfterReset = _RsMaxPimSmCRPEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 10),
    _RsMaxPimSmCRPEntriesAfterReset_Type()
)
rsMaxPimSmCRPEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPimSmCRPEntriesAfterReset.setStatus("current")
_RsMaxNumberRpAddresesInGroupRange_Type = Integer32
_RsMaxNumberRpAddresesInGroupRange_Object = MibScalar
rsMaxNumberRpAddresesInGroupRange = _RsMaxNumberRpAddresesInGroupRange_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 11),
    _RsMaxNumberRpAddresesInGroupRange_Type()
)
rsMaxNumberRpAddresesInGroupRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxNumberRpAddresesInGroupRange.setStatus("current")
_RsMaxNumberRpAddresesInGroupRangeAfterReset_Type = Integer32
_RsMaxNumberRpAddresesInGroupRangeAfterReset_Object = MibScalar
rsMaxNumberRpAddresesInGroupRangeAfterReset = _RsMaxNumberRpAddresesInGroupRangeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 12, 6, 12),
    _RsMaxNumberRpAddresesInGroupRangeAfterReset_Type()
)
rsMaxNumberRpAddresesInGroupRangeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxNumberRpAddresesInGroupRangeAfterReset.setStatus("current")
_RsMaxRmonTuning_ObjectIdentity = ObjectIdentity
rsMaxRmonTuning = _RsMaxRmonTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 13)
)
_RsMaxRmonLogEntries_Type = Integer32
_RsMaxRmonLogEntries_Object = MibScalar
rsMaxRmonLogEntries = _RsMaxRmonLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 13, 1),
    _RsMaxRmonLogEntries_Type()
)
rsMaxRmonLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxRmonLogEntries.setStatus("current")
_RsMaxRmonLogEntriesAfterReset_Type = Integer32
_RsMaxRmonLogEntriesAfterReset_Object = MibScalar
rsMaxRmonLogEntriesAfterReset = _RsMaxRmonLogEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 13, 2),
    _RsMaxRmonLogEntriesAfterReset_Type()
)
rsMaxRmonLogEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxRmonLogEntriesAfterReset.setStatus("current")
_RsMaxRmonEtherHistoryEntries_Type = Integer32
_RsMaxRmonEtherHistoryEntries_Object = MibScalar
rsMaxRmonEtherHistoryEntries = _RsMaxRmonEtherHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 13, 3),
    _RsMaxRmonEtherHistoryEntries_Type()
)
rsMaxRmonEtherHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxRmonEtherHistoryEntries.setStatus("current")
_RsMaxRmonEtherHistoryEntriesAfterReset_Type = Integer32
_RsMaxRmonEtherHistoryEntriesAfterReset_Object = MibScalar
rsMaxRmonEtherHistoryEntriesAfterReset = _RsMaxRmonEtherHistoryEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 13, 4),
    _RsMaxRmonEtherHistoryEntriesAfterReset_Type()
)
rsMaxRmonEtherHistoryEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxRmonEtherHistoryEntriesAfterReset.setStatus("current")
_RsMaxIgmpSnoopTuning_ObjectIdentity = ObjectIdentity
rsMaxIgmpSnoopTuning = _RsMaxIgmpSnoopTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 14)
)
_RsMaxIgmpSnoopGroupEntries_Type = Integer32
_RsMaxIgmpSnoopGroupEntries_Object = MibScalar
rsMaxIgmpSnoopGroupEntries = _RsMaxIgmpSnoopGroupEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 14, 1),
    _RsMaxIgmpSnoopGroupEntries_Type()
)
rsMaxIgmpSnoopGroupEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIgmpSnoopGroupEntries.setStatus("current")
_RsMaxIgmpSnoopGroupEntriesAfterReset_Type = Integer32
_RsMaxIgmpSnoopGroupEntriesAfterReset_Object = MibScalar
rsMaxIgmpSnoopGroupEntriesAfterReset = _RsMaxIgmpSnoopGroupEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 14, 2),
    _RsMaxIgmpSnoopGroupEntriesAfterReset_Type()
)
rsMaxIgmpSnoopGroupEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIgmpSnoopGroupEntriesAfterReset.setStatus("current")
_RsMaxVlansTuning_ObjectIdentity = ObjectIdentity
rsMaxVlansTuning = _RsMaxVlansTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 15)
)
_RsMaxVlansEntries_Type = Integer32
_RsMaxVlansEntries_Object = MibScalar
rsMaxVlansEntries = _RsMaxVlansEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 15, 1),
    _RsMaxVlansEntries_Type()
)
rsMaxVlansEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxVlansEntries.setStatus("current")
_RsMaxVlansEntriesAfterReset_Type = Integer32
_RsMaxVlansEntriesAfterReset_Object = MibScalar
rsMaxVlansEntriesAfterReset = _RsMaxVlansEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 15, 2),
    _RsMaxVlansEntriesAfterReset_Type()
)
rsMaxVlansEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxVlansEntriesAfterReset.setStatus("current")
_RsMaxPolicyTuning_ObjectIdentity = ObjectIdentity
rsMaxPolicyTuning = _RsMaxPolicyTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16)
)
_RsMaxPolicyMaxRulesEntries_Type = Integer32
_RsMaxPolicyMaxRulesEntries_Object = MibScalar
rsMaxPolicyMaxRulesEntries = _RsMaxPolicyMaxRulesEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16, 1),
    _RsMaxPolicyMaxRulesEntries_Type()
)
rsMaxPolicyMaxRulesEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPolicyMaxRulesEntries.setStatus("current")
_RsMaxPolicyMaxRulesEntriesAfterReset_Type = Integer32
_RsMaxPolicyMaxRulesEntriesAfterReset_Object = MibScalar
rsMaxPolicyMaxRulesEntriesAfterReset = _RsMaxPolicyMaxRulesEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16, 2),
    _RsMaxPolicyMaxRulesEntriesAfterReset_Type()
)
rsMaxPolicyMaxRulesEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPolicyMaxRulesEntriesAfterReset.setStatus("current")
_RsMaxPolicySimpleMibMaxRulesEntries_Type = Integer32
_RsMaxPolicySimpleMibMaxRulesEntries_Object = MibScalar
rsMaxPolicySimpleMibMaxRulesEntries = _RsMaxPolicySimpleMibMaxRulesEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16, 3),
    _RsMaxPolicySimpleMibMaxRulesEntries_Type()
)
rsMaxPolicySimpleMibMaxRulesEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPolicySimpleMibMaxRulesEntries.setStatus("current")
_RsMaxPolicySimpleMibMaxRulesEntriesAfterReset_Type = Integer32
_RsMaxPolicySimpleMibMaxRulesEntriesAfterReset_Object = MibScalar
rsMaxPolicySimpleMibMaxRulesEntriesAfterReset = _RsMaxPolicySimpleMibMaxRulesEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16, 4),
    _RsMaxPolicySimpleMibMaxRulesEntriesAfterReset_Type()
)
rsMaxPolicySimpleMibMaxRulesEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPolicySimpleMibMaxRulesEntriesAfterReset.setStatus("current")
_RsMaxPolicySimpleMibMaxProfilesEntries_Type = Integer32
_RsMaxPolicySimpleMibMaxProfilesEntries_Object = MibScalar
rsMaxPolicySimpleMibMaxProfilesEntries = _RsMaxPolicySimpleMibMaxProfilesEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16, 5),
    _RsMaxPolicySimpleMibMaxProfilesEntries_Type()
)
rsMaxPolicySimpleMibMaxProfilesEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxPolicySimpleMibMaxProfilesEntries.setStatus("current")
_RsMaxPolicySimpleMibMaxProfilesEntriesAfterReset_Type = Integer32
_RsMaxPolicySimpleMibMaxProfilesEntriesAfterReset_Object = MibScalar
rsMaxPolicySimpleMibMaxProfilesEntriesAfterReset = _RsMaxPolicySimpleMibMaxProfilesEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 16, 6),
    _RsMaxPolicySimpleMibMaxProfilesEntriesAfterReset_Type()
)
rsMaxPolicySimpleMibMaxProfilesEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxPolicySimpleMibMaxProfilesEntriesAfterReset.setStatus("current")
_RsMaxGvrpVlansTuning_ObjectIdentity = ObjectIdentity
rsMaxGvrpVlansTuning = _RsMaxGvrpVlansTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 17)
)
_RsMaxGvrpVlans_Type = Integer32
_RsMaxGvrpVlans_Object = MibScalar
rsMaxGvrpVlans = _RsMaxGvrpVlans_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 17, 1),
    _RsMaxGvrpVlans_Type()
)
rsMaxGvrpVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxGvrpVlans.setStatus("current")
_RsMaxGvrpVlansAfterReset_Type = Integer32
_RsMaxGvrpVlansAfterReset_Object = MibScalar
rsMaxGvrpVlansAfterReset = _RsMaxGvrpVlansAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 17, 2),
    _RsMaxGvrpVlansAfterReset_Type()
)
rsMaxGvrpVlansAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxGvrpVlansAfterReset.setStatus("current")
_RsMaxTraceRouteTuning_ObjectIdentity = ObjectIdentity
rsMaxTraceRouteTuning = _RsMaxTraceRouteTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 18)
)
_RsMaxTraceRouteControlEntries_Type = Integer32
_RsMaxTraceRouteControlEntries_Object = MibScalar
rsMaxTraceRouteControlEntries = _RsMaxTraceRouteControlEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 18, 1),
    _RsMaxTraceRouteControlEntries_Type()
)
rsMaxTraceRouteControlEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxTraceRouteControlEntries.setStatus("current")
_RsMaxTraceRouteControlEntriesAfterReset_Type = Integer32
_RsMaxTraceRouteControlEntriesAfterReset_Object = MibScalar
rsMaxTraceRouteControlEntriesAfterReset = _RsMaxTraceRouteControlEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 18, 2),
    _RsMaxTraceRouteControlEntriesAfterReset_Type()
)
rsMaxTraceRouteControlEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxTraceRouteControlEntriesAfterReset.setStatus("current")
_RsMaxTraceRouteProbeHistoryEntries_Type = Integer32
_RsMaxTraceRouteProbeHistoryEntries_Object = MibScalar
rsMaxTraceRouteProbeHistoryEntries = _RsMaxTraceRouteProbeHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 18, 3),
    _RsMaxTraceRouteProbeHistoryEntries_Type()
)
rsMaxTraceRouteProbeHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxTraceRouteProbeHistoryEntries.setStatus("current")
_RsMaxTraceRouteProbeHistoryEntriesAfterReset_Type = Integer32
_RsMaxTraceRouteProbeHistoryEntriesAfterReset_Object = MibScalar
rsMaxTraceRouteProbeHistoryEntriesAfterReset = _RsMaxTraceRouteProbeHistoryEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 18, 4),
    _RsMaxTraceRouteProbeHistoryEntriesAfterReset_Type()
)
rsMaxTraceRouteProbeHistoryEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxTraceRouteProbeHistoryEntriesAfterReset.setStatus("current")
_RsMaxSnmpTuning_ObjectIdentity = ObjectIdentity
rsMaxSnmpTuning = _RsMaxSnmpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 19)
)
_RsMaxSnmpCommunityEntries_Type = Integer32
_RsMaxSnmpCommunityEntries_Object = MibScalar
rsMaxSnmpCommunityEntries = _RsMaxSnmpCommunityEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 19, 1),
    _RsMaxSnmpCommunityEntries_Type()
)
rsMaxSnmpCommunityEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxSnmpCommunityEntries.setStatus("current")


class _RsMaxSnmpCommunityEntriesAfterReset_Type(Integer32):
    """Custom type rsMaxSnmpCommunityEntriesAfterReset based on Integer32"""
    defaultValue = 16


_RsMaxSnmpCommunityEntriesAfterReset_Object = MibScalar
rsMaxSnmpCommunityEntriesAfterReset = _RsMaxSnmpCommunityEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 19, 2),
    _RsMaxSnmpCommunityEntriesAfterReset_Type()
)
rsMaxSnmpCommunityEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxSnmpCommunityEntriesAfterReset.setStatus("current")
_RsMaxSocketTuning_ObjectIdentity = ObjectIdentity
rsMaxSocketTuning = _RsMaxSocketTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 20)
)
_RsMaxNumberOfSockets_Type = Integer32
_RsMaxNumberOfSockets_Object = MibScalar
rsMaxNumberOfSockets = _RsMaxNumberOfSockets_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 20, 1),
    _RsMaxNumberOfSockets_Type()
)
rsMaxNumberOfSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxNumberOfSockets.setStatus("current")
_RsMaxNumberOfSocketsAfterReset_Type = Integer32
_RsMaxNumberOfSocketsAfterReset_Object = MibScalar
rsMaxNumberOfSocketsAfterReset = _RsMaxNumberOfSocketsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 20, 2),
    _RsMaxNumberOfSocketsAfterReset_Type()
)
rsMaxNumberOfSocketsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxNumberOfSocketsAfterReset.setStatus("current")
_RsMaxSizeOfSocketDataPool_Type = Integer32
_RsMaxSizeOfSocketDataPool_Object = MibScalar
rsMaxSizeOfSocketDataPool = _RsMaxSizeOfSocketDataPool_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 20, 3),
    _RsMaxSizeOfSocketDataPool_Type()
)
rsMaxSizeOfSocketDataPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxSizeOfSocketDataPool.setStatus("current")
_RsMaxSizeOfSocketDataPoolAfterReset_Type = Integer32
_RsMaxSizeOfSocketDataPoolAfterReset_Object = MibScalar
rsMaxSizeOfSocketDataPoolAfterReset = _RsMaxSizeOfSocketDataPoolAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 20, 4),
    _RsMaxSizeOfSocketDataPoolAfterReset_Type()
)
rsMaxSizeOfSocketDataPoolAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxSizeOfSocketDataPoolAfterReset.setStatus("current")
_RsMaxIpRouteTuning_ObjectIdentity = ObjectIdentity
rsMaxIpRouteTuning = _RsMaxIpRouteTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 21)
)
_RsMaxIpPrefixes_Type = Integer32
_RsMaxIpPrefixes_Object = MibScalar
rsMaxIpPrefixes = _RsMaxIpPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 21, 1),
    _RsMaxIpPrefixes_Type()
)
rsMaxIpPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpPrefixes.setStatus("current")
_RsMaxIpPrefixesAfterReset_Type = Integer32
_RsMaxIpPrefixesAfterReset_Object = MibScalar
rsMaxIpPrefixesAfterReset = _RsMaxIpPrefixesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 21, 2),
    _RsMaxIpPrefixesAfterReset_Type()
)
rsMaxIpPrefixesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpPrefixesAfterReset.setStatus("current")
_RsMaxIpNextHopSetTuning_ObjectIdentity = ObjectIdentity
rsMaxIpNextHopSetTuning = _RsMaxIpNextHopSetTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 22)
)
_RsMaxIpNextHopSetEntries_Type = Integer32
_RsMaxIpNextHopSetEntries_Object = MibScalar
rsMaxIpNextHopSetEntries = _RsMaxIpNextHopSetEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 22, 1),
    _RsMaxIpNextHopSetEntries_Type()
)
rsMaxIpNextHopSetEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpNextHopSetEntries.setStatus("current")
_RsMaxIpNextHopSetEntriesAfterReset_Type = Integer32
_RsMaxIpNextHopSetEntriesAfterReset_Object = MibScalar
rsMaxIpNextHopSetEntriesAfterReset = _RsMaxIpNextHopSetEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 22, 2),
    _RsMaxIpNextHopSetEntriesAfterReset_Type()
)
rsMaxIpNextHopSetEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpNextHopSetEntriesAfterReset.setStatus("current")
_RsMaxIpEcmpTuning_ObjectIdentity = ObjectIdentity
rsMaxIpEcmpTuning = _RsMaxIpEcmpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 23)
)
_RsMaxIpEcmpEntrySize_Type = Integer32
_RsMaxIpEcmpEntrySize_Object = MibScalar
rsMaxIpEcmpEntrySize = _RsMaxIpEcmpEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 23, 1),
    _RsMaxIpEcmpEntrySize_Type()
)
rsMaxIpEcmpEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpEcmpEntrySize.setStatus("current")
_RsMaxIpEcmpEntrySizeAfterReset_Type = Integer32
_RsMaxIpEcmpEntrySizeAfterReset_Object = MibScalar
rsMaxIpEcmpEntrySizeAfterReset = _RsMaxIpEcmpEntrySizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 23, 2),
    _RsMaxIpEcmpEntrySizeAfterReset_Type()
)
rsMaxIpEcmpEntrySizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpEcmpEntrySizeAfterReset.setStatus("current")
_RsMaxdot1xEapRequestTuning_ObjectIdentity = ObjectIdentity
rsMaxdot1xEapRequestTuning = _RsMaxdot1xEapRequestTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 24)
)
_RsMaxdot1xEapRequestEntries_Type = Integer32
_RsMaxdot1xEapRequestEntries_Object = MibScalar
rsMaxdot1xEapRequestEntries = _RsMaxdot1xEapRequestEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 24, 1),
    _RsMaxdot1xEapRequestEntries_Type()
)
rsMaxdot1xEapRequestEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxdot1xEapRequestEntries.setStatus("current")
_RsMaxdot1xEapRequestEntriesAfterReset_Type = Integer32
_RsMaxdot1xEapRequestEntriesAfterReset_Object = MibScalar
rsMaxdot1xEapRequestEntriesAfterReset = _RsMaxdot1xEapRequestEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 24, 2),
    _RsMaxdot1xEapRequestEntriesAfterReset_Type()
)
rsMaxdot1xEapRequestEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxdot1xEapRequestEntriesAfterReset.setStatus("current")
_RsMaxIpInterfaceTuning_ObjectIdentity = ObjectIdentity
rsMaxIpInterfaceTuning = _RsMaxIpInterfaceTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 25)
)
_RsMaxIpInterfaces_Type = Integer32
_RsMaxIpInterfaces_Object = MibScalar
rsMaxIpInterfaces = _RsMaxIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 25, 1),
    _RsMaxIpInterfaces_Type()
)
rsMaxIpInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpInterfaces.setStatus("current")
_RsMaxIpInterfacesAfterReset_Type = Integer32
_RsMaxIpInterfacesAfterReset_Object = MibScalar
rsMaxIpInterfacesAfterReset = _RsMaxIpInterfacesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 25, 2),
    _RsMaxIpInterfacesAfterReset_Type()
)
rsMaxIpInterfacesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpInterfacesAfterReset.setStatus("current")
_RsMaxIpv6FftEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpv6FftEntriesTuning = _RsMaxIpv6FftEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26)
)
_RsMaxIpv6SFftEntries_Type = Integer32
_RsMaxIpv6SFftEntries_Object = MibScalar
rsMaxIpv6SFftEntries = _RsMaxIpv6SFftEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 1),
    _RsMaxIpv6SFftEntries_Type()
)
rsMaxIpv6SFftEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6SFftEntries.setStatus("current")
_RsMaxIpv6SFftEntriesAfterReset_Type = Integer32
_RsMaxIpv6SFftEntriesAfterReset_Object = MibScalar
rsMaxIpv6SFftEntriesAfterReset = _RsMaxIpv6SFftEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 2),
    _RsMaxIpv6SFftEntriesAfterReset_Type()
)
rsMaxIpv6SFftEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6SFftEntriesAfterReset.setStatus("current")
_RsMaxIpv6SFftSysEntries_Type = Integer32
_RsMaxIpv6SFftSysEntries_Object = MibScalar
rsMaxIpv6SFftSysEntries = _RsMaxIpv6SFftSysEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 3),
    _RsMaxIpv6SFftSysEntries_Type()
)
rsMaxIpv6SFftSysEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6SFftSysEntries.setStatus("current")
_RsMaxIpv6SFftSysEntriesAfterReset_Type = Integer32
_RsMaxIpv6SFftSysEntriesAfterReset_Object = MibScalar
rsMaxIpv6SFftSysEntriesAfterReset = _RsMaxIpv6SFftSysEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 4),
    _RsMaxIpv6SFftSysEntriesAfterReset_Type()
)
rsMaxIpv6SFftSysEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6SFftSysEntriesAfterReset.setStatus("current")
_RsMaxIpv6Prefixes_Type = Integer32
_RsMaxIpv6Prefixes_Object = MibScalar
rsMaxIpv6Prefixes = _RsMaxIpv6Prefixes_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 5),
    _RsMaxIpv6Prefixes_Type()
)
rsMaxIpv6Prefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6Prefixes.setStatus("current")
_RsMaxIpv6PrefixesAfterReset_Type = Integer32
_RsMaxIpv6PrefixesAfterReset_Object = MibScalar
rsMaxIpv6PrefixesAfterReset = _RsMaxIpv6PrefixesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 6),
    _RsMaxIpv6PrefixesAfterReset_Type()
)
rsMaxIpv6PrefixesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6PrefixesAfterReset.setStatus("current")
_RsMaxIpv6NextHopEntries_Type = Integer32
_RsMaxIpv6NextHopEntries_Object = MibScalar
rsMaxIpv6NextHopEntries = _RsMaxIpv6NextHopEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 7),
    _RsMaxIpv6NextHopEntries_Type()
)
rsMaxIpv6NextHopEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6NextHopEntries.setStatus("current")
_RsMaxIpv6NextHopEntriesAfterReset_Type = Integer32
_RsMaxIpv6NextHopEntriesAfterReset_Object = MibScalar
rsMaxIpv6NextHopEntriesAfterReset = _RsMaxIpv6NextHopEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 8),
    _RsMaxIpv6NextHopEntriesAfterReset_Type()
)
rsMaxIpv6NextHopEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6NextHopEntriesAfterReset.setStatus("current")
_RsMaxIpv6NextHopSetEntries_Type = Integer32
_RsMaxIpv6NextHopSetEntries_Object = MibScalar
rsMaxIpv6NextHopSetEntries = _RsMaxIpv6NextHopSetEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 9),
    _RsMaxIpv6NextHopSetEntries_Type()
)
rsMaxIpv6NextHopSetEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6NextHopSetEntries.setStatus("current")
_RsMaxIpv6NextHopSetEntriesAfterReset_Type = Integer32
_RsMaxIpv6NextHopSetEntriesAfterReset_Object = MibScalar
rsMaxIpv6NextHopSetEntriesAfterReset = _RsMaxIpv6NextHopSetEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 10),
    _RsMaxIpv6NextHopSetEntriesAfterReset_Type()
)
rsMaxIpv6NextHopSetEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6NextHopSetEntriesAfterReset.setStatus("current")
_RsMaxIpv6GlobalAddresses_Type = Integer32
_RsMaxIpv6GlobalAddresses_Object = MibScalar
rsMaxIpv6GlobalAddresses = _RsMaxIpv6GlobalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 11),
    _RsMaxIpv6GlobalAddresses_Type()
)
rsMaxIpv6GlobalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6GlobalAddresses.setStatus("current")
_RsMaxIpv6GlobalAddressesAfterReset_Type = Integer32
_RsMaxIpv6GlobalAddressesAfterReset_Object = MibScalar
rsMaxIpv6GlobalAddressesAfterReset = _RsMaxIpv6GlobalAddressesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 12),
    _RsMaxIpv6GlobalAddressesAfterReset_Type()
)
rsMaxIpv6GlobalAddressesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6GlobalAddressesAfterReset.setStatus("current")
_RsMaxArpTunnelStartEntries_Type = Integer32
_RsMaxArpTunnelStartEntries_Object = MibScalar
rsMaxArpTunnelStartEntries = _RsMaxArpTunnelStartEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 13),
    _RsMaxArpTunnelStartEntries_Type()
)
rsMaxArpTunnelStartEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxArpTunnelStartEntries.setStatus("current")
_RsMaxArpTunnelStartEntriesAfterReset_Type = Integer32
_RsMaxArpTunnelStartEntriesAfterReset_Object = MibScalar
rsMaxArpTunnelStartEntriesAfterReset = _RsMaxArpTunnelStartEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 26, 14),
    _RsMaxArpTunnelStartEntriesAfterReset_Type()
)
rsMaxArpTunnelStartEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxArpTunnelStartEntriesAfterReset.setStatus("current")
_RsMaxIpv6InterfaceTuning_ObjectIdentity = ObjectIdentity
rsMaxIpv6InterfaceTuning = _RsMaxIpv6InterfaceTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 27)
)
_RsMaxIpv6Interfaces_Type = Integer32
_RsMaxIpv6Interfaces_Object = MibScalar
rsMaxIpv6Interfaces = _RsMaxIpv6Interfaces_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 27, 1),
    _RsMaxIpv6Interfaces_Type()
)
rsMaxIpv6Interfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6Interfaces.setStatus("current")
_RsMaxIpv6InterfacesAfterReset_Type = Integer32
_RsMaxIpv6InterfacesAfterReset_Object = MibScalar
rsMaxIpv6InterfacesAfterReset = _RsMaxIpv6InterfacesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 27, 2),
    _RsMaxIpv6InterfacesAfterReset_Type()
)
rsMaxIpv6InterfacesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6InterfacesAfterReset.setStatus("current")
_RsMaxIpv6AddrPerInterfaces_Type = Integer32
_RsMaxIpv6AddrPerInterfaces_Object = MibScalar
rsMaxIpv6AddrPerInterfaces = _RsMaxIpv6AddrPerInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 27, 3),
    _RsMaxIpv6AddrPerInterfaces_Type()
)
rsMaxIpv6AddrPerInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6AddrPerInterfaces.setStatus("current")
_RsMaxIpv6AddrPerInterfacesAfterReset_Type = Integer32
_RsMaxIpv6AddrPerInterfacesAfterReset_Object = MibScalar
rsMaxIpv6AddrPerInterfacesAfterReset = _RsMaxIpv6AddrPerInterfacesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 27, 4),
    _RsMaxIpv6AddrPerInterfacesAfterReset_Type()
)
rsMaxIpv6AddrPerInterfacesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6AddrPerInterfacesAfterReset.setStatus("current")
_RsMaxIpRoutesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpRoutesTuning = _RsMaxIpRoutesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28)
)
_RsMaxIpv4Routes_Type = Integer32
_RsMaxIpv4Routes_Object = MibScalar
rsMaxIpv4Routes = _RsMaxIpv4Routes_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 1),
    _RsMaxIpv4Routes_Type()
)
rsMaxIpv4Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv4Routes.setStatus("current")
_RsMaxIpv4RoutesAfterReset_Type = Integer32
_RsMaxIpv4RoutesAfterReset_Object = MibScalar
rsMaxIpv4RoutesAfterReset = _RsMaxIpv4RoutesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 2),
    _RsMaxIpv4RoutesAfterReset_Type()
)
rsMaxIpv4RoutesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv4RoutesAfterReset.setStatus("current")
_RsMaxIpv6Routes_Type = Integer32
_RsMaxIpv6Routes_Object = MibScalar
rsMaxIpv6Routes = _RsMaxIpv6Routes_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 3),
    _RsMaxIpv6Routes_Type()
)
rsMaxIpv6Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpv6Routes.setStatus("current")
_RsMaxIpv6RoutesAfterReset_Type = Integer32
_RsMaxIpv6RoutesAfterReset_Object = MibScalar
rsMaxIpv6RoutesAfterReset = _RsMaxIpv6RoutesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 4),
    _RsMaxIpv6RoutesAfterReset_Type()
)
rsMaxIpv6RoutesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpv6RoutesAfterReset.setStatus("current")
_RsMaxIpmv4Routes_Type = Integer32
_RsMaxIpmv4Routes_Object = MibScalar
rsMaxIpmv4Routes = _RsMaxIpmv4Routes_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 5),
    _RsMaxIpmv4Routes_Type()
)
rsMaxIpmv4Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpmv4Routes.setStatus("current")
_RsMaxIpmv4RoutesAfterReset_Type = Integer32
_RsMaxIpmv4RoutesAfterReset_Object = MibScalar
rsMaxIpmv4RoutesAfterReset = _RsMaxIpmv4RoutesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 6),
    _RsMaxIpmv4RoutesAfterReset_Type()
)
rsMaxIpmv4RoutesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpmv4RoutesAfterReset.setStatus("current")
_RsMaxIpmv6Routes_Type = Integer32
_RsMaxIpmv6Routes_Object = MibScalar
rsMaxIpmv6Routes = _RsMaxIpmv6Routes_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 7),
    _RsMaxIpmv6Routes_Type()
)
rsMaxIpmv6Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpmv6Routes.setStatus("current")
_RsMaxIpmv6RoutesAfterReset_Type = Integer32
_RsMaxIpmv6RoutesAfterReset_Object = MibScalar
rsMaxIpmv6RoutesAfterReset = _RsMaxIpmv6RoutesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 28, 8),
    _RsMaxIpmv6RoutesAfterReset_Type()
)
rsMaxIpmv6RoutesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpmv6RoutesAfterReset.setStatus("current")
_RsTcpTuning_ObjectIdentity = ObjectIdentity
rsTcpTuning = _RsTcpTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 11)
)
_RsTcpMemoryPoolSizeAfterReset_Type = Integer32
_RsTcpMemoryPoolSizeAfterReset_Object = MibScalar
rsTcpMemoryPoolSizeAfterReset = _RsTcpMemoryPoolSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 11, 1),
    _RsTcpMemoryPoolSizeAfterReset_Type()
)
rsTcpMemoryPoolSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTcpMemoryPoolSizeAfterReset.setStatus("current")
_RsTcpMemoryPoolSize_Type = Integer32
_RsTcpMemoryPoolSize_Object = MibScalar
rsTcpMemoryPoolSize = _RsTcpMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 11, 2),
    _RsTcpMemoryPoolSize_Type()
)
rsTcpMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTcpMemoryPoolSize.setStatus("current")
_RsRadiusTuning_ObjectIdentity = ObjectIdentity
rsRadiusTuning = _RsRadiusTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 12)
)
_RsRadiusMemoryPoolSizeAfterReset_Type = Integer32
_RsRadiusMemoryPoolSizeAfterReset_Object = MibScalar
rsRadiusMemoryPoolSizeAfterReset = _RsRadiusMemoryPoolSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 12, 1),
    _RsRadiusMemoryPoolSizeAfterReset_Type()
)
rsRadiusMemoryPoolSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMemoryPoolSizeAfterReset.setStatus("current")
_RsRadiusMemoryPoolSize_Type = Integer32
_RsRadiusMemoryPoolSize_Object = MibScalar
rsRadiusMemoryPoolSize = _RsRadiusMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 12, 2),
    _RsRadiusMemoryPoolSize_Type()
)
rsRadiusMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusMemoryPoolSize.setStatus("current")
_RlSyslogTuning_ObjectIdentity = ObjectIdentity
rlSyslogTuning = _RlSyslogTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 13)
)
_RlSyslogFilePercentToDeleteWhenCompacting_Type = Unsigned32
_RlSyslogFilePercentToDeleteWhenCompacting_Object = MibScalar
rlSyslogFilePercentToDeleteWhenCompacting = _RlSyslogFilePercentToDeleteWhenCompacting_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 13, 3),
    _RlSyslogFilePercentToDeleteWhenCompacting_Type()
)
rlSyslogFilePercentToDeleteWhenCompacting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogFilePercentToDeleteWhenCompacting.setStatus("current")
_RlSyslogFilePercentToDeleteWhenCompactingAfterReset_Type = Unsigned32
_RlSyslogFilePercentToDeleteWhenCompactingAfterReset_Object = MibScalar
rlSyslogFilePercentToDeleteWhenCompactingAfterReset = _RlSyslogFilePercentToDeleteWhenCompactingAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 13, 4),
    _RlSyslogFilePercentToDeleteWhenCompactingAfterReset_Type()
)
rlSyslogFilePercentToDeleteWhenCompactingAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogFilePercentToDeleteWhenCompactingAfterReset.setStatus("current")
_RlSyslogCacheSize_Type = Unsigned32
_RlSyslogCacheSize_Object = MibScalar
rlSyslogCacheSize = _RlSyslogCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 13, 5),
    _RlSyslogCacheSize_Type()
)
rlSyslogCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCacheSize.setStatus("current")
_RlSyslogCacheSizeAfterReset_Type = Unsigned32
_RlSyslogCacheSizeAfterReset_Object = MibScalar
rlSyslogCacheSizeAfterReset = _RlSyslogCacheSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 13, 6),
    _RlSyslogCacheSizeAfterReset_Type()
)
rlSyslogCacheSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogCacheSizeAfterReset.setStatus("current")
_RlMngInfTuning_ObjectIdentity = ObjectIdentity
rlMngInfTuning = _RlMngInfTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 14)
)
_RlMaxNumberOfAccessRules_Type = Integer32
_RlMaxNumberOfAccessRules_Object = MibScalar
rlMaxNumberOfAccessRules = _RlMaxNumberOfAccessRules_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 14, 1),
    _RlMaxNumberOfAccessRules_Type()
)
rlMaxNumberOfAccessRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxNumberOfAccessRules.setStatus("current")
_RlMaxNumberOfAccessRulesAfterReset_Type = Integer32
_RlMaxNumberOfAccessRulesAfterReset_Object = MibScalar
rlMaxNumberOfAccessRulesAfterReset = _RlMaxNumberOfAccessRulesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 14, 2),
    _RlMaxNumberOfAccessRulesAfterReset_Type()
)
rlMaxNumberOfAccessRulesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxNumberOfAccessRulesAfterReset.setStatus("current")


class _RsDiagnosticTextSource_Type(Integer32):
    """Custom type rsDiagnosticTextSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromCLI", 1),
          ("fromDiagnosticsTable", 2))
    )


_RsDiagnosticTextSource_Type.__name__ = "Integer32"
_RsDiagnosticTextSource_Object = MibScalar
rsDiagnosticTextSource = _RsDiagnosticTextSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 16),
    _RsDiagnosticTextSource_Type()
)
rsDiagnosticTextSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDiagnosticTextSource.setStatus("current")
_RsMultiSession_ObjectIdentity = ObjectIdentity
rsMultiSession = _RsMultiSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 17)
)
_RsMultiSessionMaxSessionsAfterReset_Type = Integer32
_RsMultiSessionMaxSessionsAfterReset_Object = MibScalar
rsMultiSessionMaxSessionsAfterReset = _RsMultiSessionMaxSessionsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 17, 1),
    _RsMultiSessionMaxSessionsAfterReset_Type()
)
rsMultiSessionMaxSessionsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMultiSessionMaxSessionsAfterReset.setStatus("current")
_RsMultiSessionMaxSessions_Type = Integer32
_RsMultiSessionMaxSessions_Object = MibScalar
rsMultiSessionMaxSessions = _RsMultiSessionMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 17, 2),
    _RsMultiSessionMaxSessions_Type()
)
rsMultiSessionMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMultiSessionMaxSessions.setStatus("current")
_RlDnsClTuning_ObjectIdentity = ObjectIdentity
rlDnsClTuning = _RlDnsClTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 18)
)
_RlMaxDnsClCacheRREntries_Type = Integer32
_RlMaxDnsClCacheRREntries_Object = MibScalar
rlMaxDnsClCacheRREntries = _RlMaxDnsClCacheRREntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 18, 1),
    _RlMaxDnsClCacheRREntries_Type()
)
rlMaxDnsClCacheRREntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxDnsClCacheRREntries.setStatus("current")
_RlMaxDnsClCacheRREntriesAfterReset_Type = Integer32
_RlMaxDnsClCacheRREntriesAfterReset_Object = MibScalar
rlMaxDnsClCacheRREntriesAfterReset = _RlMaxDnsClCacheRREntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 18, 2),
    _RlMaxDnsClCacheRREntriesAfterReset_Type()
)
rlMaxDnsClCacheRREntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxDnsClCacheRREntriesAfterReset.setStatus("current")
_RlMaxDnsClNCacheErrEntries_Type = Integer32
_RlMaxDnsClNCacheErrEntries_Object = MibScalar
rlMaxDnsClNCacheErrEntries = _RlMaxDnsClNCacheErrEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 18, 3),
    _RlMaxDnsClNCacheErrEntries_Type()
)
rlMaxDnsClNCacheErrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxDnsClNCacheErrEntries.setStatus("current")
_RlMaxDnsClNCacheErrEntriesAfterReset_Type = Integer32
_RlMaxDnsClNCacheErrEntriesAfterReset_Object = MibScalar
rlMaxDnsClNCacheErrEntriesAfterReset = _RlMaxDnsClNCacheErrEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 18, 4),
    _RlMaxDnsClNCacheErrEntriesAfterReset_Type()
)
rlMaxDnsClNCacheErrEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxDnsClNCacheErrEntriesAfterReset.setStatus("current")
_RlMaxDnsClNamesEntries_Type = Integer32
_RlMaxDnsClNamesEntries_Object = MibScalar
rlMaxDnsClNamesEntries = _RlMaxDnsClNamesEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 18, 5),
    _RlMaxDnsClNamesEntries_Type()
)
rlMaxDnsClNamesEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxDnsClNamesEntries.setStatus("current")
_RlMaxDnsClNamesEntriesAfterReset_Type = Integer32
_RlMaxDnsClNamesEntriesAfterReset_Object = MibScalar
rlMaxDnsClNamesEntriesAfterReset = _RlMaxDnsClNamesEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 18, 6),
    _RlMaxDnsClNamesEntriesAfterReset_Type()
)
rlMaxDnsClNamesEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxDnsClNamesEntriesAfterReset.setStatus("current")
_RlTuningParamsTable_Object = MibTable
rlTuningParamsTable = _RlTuningParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19)
)
if mibBuilder.loadTexts:
    rlTuningParamsTable.setStatus("current")
_RlTuningParamsEntry_Object = MibTableRow
rlTuningParamsEntry = _RlTuningParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1)
)
rlTuningParamsEntry.setIndexNames(
    (1, "Dell-Tuning", "rlTuningParamsName"),
)
if mibBuilder.loadTexts:
    rlTuningParamsEntry.setStatus("current")


class _RlTuningParamsName_Type(DisplayString):
    """Custom type rlTuningParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RlTuningParamsName_Type.__name__ = "DisplayString"
_RlTuningParamsName_Object = MibTableColumn
rlTuningParamsName = _RlTuningParamsName_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1, 1),
    _RlTuningParamsName_Type()
)
rlTuningParamsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTuningParamsName.setStatus("current")
_RlTuningParamsCurrentValue_Type = Integer32
_RlTuningParamsCurrentValue_Object = MibTableColumn
rlTuningParamsCurrentValue = _RlTuningParamsCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1, 2),
    _RlTuningParamsCurrentValue_Type()
)
rlTuningParamsCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTuningParamsCurrentValue.setStatus("current")
_RlTuningParamsAfterResetValue_Type = Integer32
_RlTuningParamsAfterResetValue_Object = MibTableColumn
rlTuningParamsAfterResetValue = _RlTuningParamsAfterResetValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1, 3),
    _RlTuningParamsAfterResetValue_Type()
)
rlTuningParamsAfterResetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTuningParamsAfterResetValue.setStatus("current")
_RlTuningParamsDefaultValue_Type = Integer32
_RlTuningParamsDefaultValue_Object = MibTableColumn
rlTuningParamsDefaultValue = _RlTuningParamsDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1, 4),
    _RlTuningParamsDefaultValue_Type()
)
rlTuningParamsDefaultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTuningParamsDefaultValue.setStatus("current")
_RlTuningParamsMinimalValue_Type = Integer32
_RlTuningParamsMinimalValue_Object = MibTableColumn
rlTuningParamsMinimalValue = _RlTuningParamsMinimalValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1, 5),
    _RlTuningParamsMinimalValue_Type()
)
rlTuningParamsMinimalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTuningParamsMinimalValue.setStatus("current")
_RlTuningParamsMaximalValue_Type = Integer32
_RlTuningParamsMaximalValue_Object = MibTableColumn
rlTuningParamsMaximalValue = _RlTuningParamsMaximalValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 19, 1, 6),
    _RlTuningParamsMaximalValue_Type()
)
rlTuningParamsMaximalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTuningParamsMaximalValue.setStatus("current")
_RlHostParamTable_Object = MibTable
rlHostParamTable = _RlHostParamTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20)
)
if mibBuilder.loadTexts:
    rlHostParamTable.setStatus("current")
_RlHostParamEntry_Object = MibTableRow
rlHostParamEntry = _RlHostParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1)
)
rlHostParamEntry.setIndexNames(
    (1, "Dell-Tuning", "rlHostParamName"),
)
if mibBuilder.loadTexts:
    rlHostParamEntry.setStatus("current")


class _RlHostParamName_Type(DisplayString):
    """Custom type rlHostParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RlHostParamName_Type.__name__ = "DisplayString"
_RlHostParamName_Object = MibTableColumn
rlHostParamName = _RlHostParamName_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 1),
    _RlHostParamName_Type()
)
rlHostParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamName.setStatus("current")
_RlHostParamValue_Type = Integer32
_RlHostParamValue_Object = MibTableColumn
rlHostParamValue = _RlHostParamValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 2),
    _RlHostParamValue_Type()
)
rlHostParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamValue.setStatus("current")


class _RlHostParamType_Type(Integer32):
    """Custom type rlHostParamType based on Integer32"""
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
        *(("displayString", 10),
          ("inetAddress", 7),
          ("int", 1),
          ("ipV4address", 4),
          ("ipV6address", 5),
          ("ipV6zAddress", 6),
          ("macAddress", 8),
          ("objectIdentifier", 9),
          ("octetString", 3),
          ("portlist", 12),
          ("truthValue", 11),
          ("uint", 2))
    )


_RlHostParamType_Type.__name__ = "Integer32"
_RlHostParamType_Object = MibTableColumn
rlHostParamType = _RlHostParamType_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 3),
    _RlHostParamType_Type()
)
rlHostParamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamType.setStatus("current")
_RlHostParamUINT_Type = Unsigned32
_RlHostParamUINT_Object = MibTableColumn
rlHostParamUINT = _RlHostParamUINT_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 4),
    _RlHostParamUINT_Type()
)
rlHostParamUINT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamUINT.setStatus("current")
_RlHostParamOctetString_Type = OctetString
_RlHostParamOctetString_Object = MibTableColumn
rlHostParamOctetString = _RlHostParamOctetString_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 5),
    _RlHostParamOctetString_Type()
)
rlHostParamOctetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamOctetString.setStatus("current")
_RlHostParamIpAddress_Type = IpAddress
_RlHostParamIpAddress_Object = MibTableColumn
rlHostParamIpAddress = _RlHostParamIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 6),
    _RlHostParamIpAddress_Type()
)
rlHostParamIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamIpAddress.setStatus("current")
_RlHostParamObjectId_Type = ObjectIdentifier
_RlHostParamObjectId_Object = MibTableColumn
rlHostParamObjectId = _RlHostParamObjectId_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 20, 1, 7),
    _RlHostParamObjectId_Type()
)
rlHostParamObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHostParamObjectId.setStatus("current")
_RlOspfTuning_ObjectIdentity = ObjectIdentity
rlOspfTuning = _RlOspfTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 21)
)
_RlMaxOspfInterfaces_Type = Integer32
_RlMaxOspfInterfaces_Object = MibScalar
rlMaxOspfInterfaces = _RlMaxOspfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 1),
    _RlMaxOspfInterfaces_Type()
)
rlMaxOspfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxOspfInterfaces.setStatus("current")
_RlMaxOspfInterfacesAfterReset_Type = Integer32
_RlMaxOspfInterfacesAfterReset_Object = MibScalar
rlMaxOspfInterfacesAfterReset = _RlMaxOspfInterfacesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 2),
    _RlMaxOspfInterfacesAfterReset_Type()
)
rlMaxOspfInterfacesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxOspfInterfacesAfterReset.setStatus("current")
_RlMaxOspfAreas_Type = Integer32
_RlMaxOspfAreas_Object = MibScalar
rlMaxOspfAreas = _RlMaxOspfAreas_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 3),
    _RlMaxOspfAreas_Type()
)
rlMaxOspfAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxOspfAreas.setStatus("current")
_RlMaxOspfAreasAfterReset_Type = Integer32
_RlMaxOspfAreasAfterReset_Object = MibScalar
rlMaxOspfAreasAfterReset = _RlMaxOspfAreasAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 4),
    _RlMaxOspfAreasAfterReset_Type()
)
rlMaxOspfAreasAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxOspfAreasAfterReset.setStatus("current")
_RlMaxOspfNeighbors_Type = Integer32
_RlMaxOspfNeighbors_Object = MibScalar
rlMaxOspfNeighbors = _RlMaxOspfNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 5),
    _RlMaxOspfNeighbors_Type()
)
rlMaxOspfNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxOspfNeighbors.setStatus("current")
_RlMaxOspfNeighborsAfterReset_Type = Integer32
_RlMaxOspfNeighborsAfterReset_Object = MibScalar
rlMaxOspfNeighborsAfterReset = _RlMaxOspfNeighborsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 6),
    _RlMaxOspfNeighborsAfterReset_Type()
)
rlMaxOspfNeighborsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxOspfNeighborsAfterReset.setStatus("current")
_RlMaxOspfAbrPerArea_Type = Integer32
_RlMaxOspfAbrPerArea_Object = MibScalar
rlMaxOspfAbrPerArea = _RlMaxOspfAbrPerArea_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 7),
    _RlMaxOspfAbrPerArea_Type()
)
rlMaxOspfAbrPerArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxOspfAbrPerArea.setStatus("current")
_RlMaxOspfAbrPerAreaAfterReset_Type = Integer32
_RlMaxOspfAbrPerAreaAfterReset_Object = MibScalar
rlMaxOspfAbrPerAreaAfterReset = _RlMaxOspfAbrPerAreaAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 8),
    _RlMaxOspfAbrPerAreaAfterReset_Type()
)
rlMaxOspfAbrPerAreaAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxOspfAbrPerAreaAfterReset.setStatus("current")
_RlMaxOspfNetsInAs_Type = Integer32
_RlMaxOspfNetsInAs_Object = MibScalar
rlMaxOspfNetsInAs = _RlMaxOspfNetsInAs_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 9),
    _RlMaxOspfNetsInAs_Type()
)
rlMaxOspfNetsInAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxOspfNetsInAs.setStatus("current")
_RlMaxOspfNetsInAsAfterReset_Type = Integer32
_RlMaxOspfNetsInAsAfterReset_Object = MibScalar
rlMaxOspfNetsInAsAfterReset = _RlMaxOspfNetsInAsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 21, 10),
    _RlMaxOspfNetsInAsAfterReset_Type()
)
rlMaxOspfNetsInAsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxOspfNetsInAsAfterReset.setStatus("current")
_RlVlanTuning_ObjectIdentity = ObjectIdentity
rlVlanTuning = _RlVlanTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 22)
)
_RlVlanDefaultVID_Type = Integer32
_RlVlanDefaultVID_Object = MibScalar
rlVlanDefaultVID = _RlVlanDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 1),
    _RlVlanDefaultVID_Type()
)
rlVlanDefaultVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVlanDefaultVID.setStatus("current")
_RlVlanDefaultVIDAfterReset_Type = Integer32
_RlVlanDefaultVIDAfterReset_Object = MibScalar
rlVlanDefaultVIDAfterReset = _RlVlanDefaultVIDAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 2),
    _RlVlanDefaultVIDAfterReset_Type()
)
rlVlanDefaultVIDAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanDefaultVIDAfterReset.setStatus("current")
_RlVlanUsageForbiddenListTable_Object = MibTable
rlVlanUsageForbiddenListTable = _RlVlanUsageForbiddenListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3)
)
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListTable.setStatus("current")
_RlVlanUsageForbiddenListEntry_Object = MibTableRow
rlVlanUsageForbiddenListEntry = _RlVlanUsageForbiddenListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3, 1)
)
rlVlanUsageForbiddenListEntry.setIndexNames(
    (0, "Dell-Tuning", "rlVlanUsageForbiddenListIndex"),
)
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListEntry.setStatus("current")


class _RlVlanUsageForbiddenListIndex_Type(Integer32):
    """Custom type rlVlanUsageForbiddenListIndex based on Integer32"""
    defaultValue = 0


_RlVlanUsageForbiddenListIndex_Object = MibTableColumn
rlVlanUsageForbiddenListIndex = _RlVlanUsageForbiddenListIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3, 1, 1),
    _RlVlanUsageForbiddenListIndex_Type()
)
rlVlanUsageForbiddenListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListIndex.setStatus("current")


class _RlVlanUsageForbiddenList1to1024_Type(VlanList1):
    """Custom type rlVlanUsageForbiddenList1to1024 based on VlanList1"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenList1to1024_Object = MibTableColumn
rlVlanUsageForbiddenList1to1024 = _RlVlanUsageForbiddenList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3, 1, 2),
    _RlVlanUsageForbiddenList1to1024_Type()
)
rlVlanUsageForbiddenList1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenList1to1024.setStatus("current")


class _RlVlanUsageForbiddenList1025to2048_Type(VlanList2):
    """Custom type rlVlanUsageForbiddenList1025to2048 based on VlanList2"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenList1025to2048_Object = MibTableColumn
rlVlanUsageForbiddenList1025to2048 = _RlVlanUsageForbiddenList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3, 1, 3),
    _RlVlanUsageForbiddenList1025to2048_Type()
)
rlVlanUsageForbiddenList1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenList1025to2048.setStatus("current")


class _RlVlanUsageForbiddenList2049to3072_Type(VlanList3):
    """Custom type rlVlanUsageForbiddenList2049to3072 based on VlanList3"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenList2049to3072_Object = MibTableColumn
rlVlanUsageForbiddenList2049to3072 = _RlVlanUsageForbiddenList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3, 1, 4),
    _RlVlanUsageForbiddenList2049to3072_Type()
)
rlVlanUsageForbiddenList2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenList2049to3072.setStatus("current")


class _RlVlanUsageForbiddenList3073to4094_Type(VlanList4):
    """Custom type rlVlanUsageForbiddenList3073to4094 based on VlanList4"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenList3073to4094_Object = MibTableColumn
rlVlanUsageForbiddenList3073to4094 = _RlVlanUsageForbiddenList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 3, 1, 5),
    _RlVlanUsageForbiddenList3073to4094_Type()
)
rlVlanUsageForbiddenList3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenList3073to4094.setStatus("current")
_RlVlanUsageForbiddenListAfterResetTable_Object = MibTable
rlVlanUsageForbiddenListAfterResetTable = _RlVlanUsageForbiddenListAfterResetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4)
)
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterResetTable.setStatus("current")
_RlVlanUsageForbiddenListAfterResetEntry_Object = MibTableRow
rlVlanUsageForbiddenListAfterResetEntry = _RlVlanUsageForbiddenListAfterResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4, 1)
)
rlVlanUsageForbiddenListAfterResetEntry.setIndexNames(
    (0, "Dell-Tuning", "rlVlanUsageForbiddenListAfterResetIndex"),
)
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterResetEntry.setStatus("current")


class _RlVlanUsageForbiddenListAfterResetIndex_Type(Integer32):
    """Custom type rlVlanUsageForbiddenListAfterResetIndex based on Integer32"""
    defaultValue = 0


_RlVlanUsageForbiddenListAfterResetIndex_Object = MibTableColumn
rlVlanUsageForbiddenListAfterResetIndex = _RlVlanUsageForbiddenListAfterResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4, 1, 1),
    _RlVlanUsageForbiddenListAfterResetIndex_Type()
)
rlVlanUsageForbiddenListAfterResetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterResetIndex.setStatus("current")


class _RlVlanUsageForbiddenListAfterReset1to1024_Type(VlanList1):
    """Custom type rlVlanUsageForbiddenListAfterReset1to1024 based on VlanList1"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenListAfterReset1to1024_Object = MibTableColumn
rlVlanUsageForbiddenListAfterReset1to1024 = _RlVlanUsageForbiddenListAfterReset1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4, 1, 2),
    _RlVlanUsageForbiddenListAfterReset1to1024_Type()
)
rlVlanUsageForbiddenListAfterReset1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterReset1to1024.setStatus("current")


class _RlVlanUsageForbiddenListAfterReset1025to2048_Type(VlanList2):
    """Custom type rlVlanUsageForbiddenListAfterReset1025to2048 based on VlanList2"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenListAfterReset1025to2048_Object = MibTableColumn
rlVlanUsageForbiddenListAfterReset1025to2048 = _RlVlanUsageForbiddenListAfterReset1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4, 1, 3),
    _RlVlanUsageForbiddenListAfterReset1025to2048_Type()
)
rlVlanUsageForbiddenListAfterReset1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterReset1025to2048.setStatus("current")


class _RlVlanUsageForbiddenListAfterReset2049to3072_Type(VlanList3):
    """Custom type rlVlanUsageForbiddenListAfterReset2049to3072 based on VlanList3"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenListAfterReset2049to3072_Object = MibTableColumn
rlVlanUsageForbiddenListAfterReset2049to3072 = _RlVlanUsageForbiddenListAfterReset2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4, 1, 4),
    _RlVlanUsageForbiddenListAfterReset2049to3072_Type()
)
rlVlanUsageForbiddenListAfterReset2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterReset2049to3072.setStatus("current")


class _RlVlanUsageForbiddenListAfterReset3073to4094_Type(VlanList4):
    """Custom type rlVlanUsageForbiddenListAfterReset3073to4094 based on VlanList4"""
    defaultHexValue = "00"


_RlVlanUsageForbiddenListAfterReset3073to4094_Object = MibTableColumn
rlVlanUsageForbiddenListAfterReset3073to4094 = _RlVlanUsageForbiddenListAfterReset3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 22, 4, 1, 5),
    _RlVlanUsageForbiddenListAfterReset3073to4094_Type()
)
rlVlanUsageForbiddenListAfterReset3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanUsageForbiddenListAfterReset3073to4094.setStatus("current")
_RlDependendFeaturesEnableTuning_ObjectIdentity = ObjectIdentity
rlDependendFeaturesEnableTuning = _RlDependendFeaturesEnableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 23)
)


class _RlDependendFeaturesEnabled_Type(Bits):
    """Custom type rlDependendFeaturesEnabled based on Bits"""
    namedValues = NamedValues(
        *(("ipV4routingEnabled", 0),
          ("iscsiEnabled", 3),
          ("policyBasedVlanEnabled", 1),
          ("qualityOfServiceEnables", 2))
    )

_RlDependendFeaturesEnabled_Type.__name__ = "Bits"
_RlDependendFeaturesEnabled_Object = MibScalar
rlDependendFeaturesEnabled = _RlDependendFeaturesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 23, 1),
    _RlDependendFeaturesEnabled_Type()
)
rlDependendFeaturesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDependendFeaturesEnabled.setStatus("current")


class _RlDependendFeaturesEnabledAfterReset_Type(Bits):
    """Custom type rlDependendFeaturesEnabledAfterReset based on Bits"""
    namedValues = NamedValues(
        *(("ipV4routingEnabled", 0),
          ("iscsiEnabled", 3),
          ("policyBasedVlanEnabled", 1),
          ("qualityOfServiceEnables", 2))
    )

_RlDependendFeaturesEnabledAfterReset_Type.__name__ = "Bits"
_RlDependendFeaturesEnabledAfterReset_Object = MibScalar
rlDependendFeaturesEnabledAfterReset = _RlDependendFeaturesEnabledAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 23, 2),
    _RlDependendFeaturesEnabledAfterReset_Type()
)
rlDependendFeaturesEnabledAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDependendFeaturesEnabledAfterReset.setStatus("current")
_RlIpDhcpSnoopingTuning_ObjectIdentity = ObjectIdentity
rlIpDhcpSnoopingTuning = _RlIpDhcpSnoopingTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 24)
)
_RlMaxIpDhcpSnoopingEntries_Type = Integer32
_RlMaxIpDhcpSnoopingEntries_Object = MibScalar
rlMaxIpDhcpSnoopingEntries = _RlMaxIpDhcpSnoopingEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 24, 1),
    _RlMaxIpDhcpSnoopingEntries_Type()
)
rlMaxIpDhcpSnoopingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMaxIpDhcpSnoopingEntries.setStatus("current")
_RlMaxIpDhcpSnoopingEntriesAfterReset_Type = Integer32
_RlMaxIpDhcpSnoopingEntriesAfterReset_Object = MibScalar
rlMaxIpDhcpSnoopingEntriesAfterReset = _RlMaxIpDhcpSnoopingEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 24, 2),
    _RlMaxIpDhcpSnoopingEntriesAfterReset_Type()
)
rlMaxIpDhcpSnoopingEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMaxIpDhcpSnoopingEntriesAfterReset.setStatus("current")
_RlIscsiSnoopTuning_ObjectIdentity = ObjectIdentity
rlIscsiSnoopTuning = _RlIscsiSnoopTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 25)
)
_RlIscsiSnoopMaxNumOfConnections_Type = Integer32
_RlIscsiSnoopMaxNumOfConnections_Object = MibScalar
rlIscsiSnoopMaxNumOfConnections = _RlIscsiSnoopMaxNumOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 25, 1),
    _RlIscsiSnoopMaxNumOfConnections_Type()
)
rlIscsiSnoopMaxNumOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopMaxNumOfConnections.setStatus("current")
_RlIscsiSnoopMaxNumOfConnectionsAfterReset_Type = Integer32
_RlIscsiSnoopMaxNumOfConnectionsAfterReset_Object = MibScalar
rlIscsiSnoopMaxNumOfConnectionsAfterReset = _RlIscsiSnoopMaxNumOfConnectionsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 25, 2),
    _RlIscsiSnoopMaxNumOfConnectionsAfterReset_Type()
)
rlIscsiSnoopMaxNumOfConnectionsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopMaxNumOfConnectionsAfterReset.setStatus("current")
_RlDhcpServerTuning_ObjectIdentity = ObjectIdentity
rlDhcpServerTuning = _RlDhcpServerTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 26)
)
_RlDhcpSrvMaxAllocatedAddresses_Type = Integer32
_RlDhcpSrvMaxAllocatedAddresses_Object = MibScalar
rlDhcpSrvMaxAllocatedAddresses = _RlDhcpSrvMaxAllocatedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 26, 1),
    _RlDhcpSrvMaxAllocatedAddresses_Type()
)
rlDhcpSrvMaxAllocatedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvMaxAllocatedAddresses.setStatus("current")
_RlDhcpSrvMaxAllocatedAddressesAfterReset_Type = Integer32
_RlDhcpSrvMaxAllocatedAddressesAfterReset_Object = MibScalar
rlDhcpSrvMaxAllocatedAddressesAfterReset = _RlDhcpSrvMaxAllocatedAddressesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 26, 2),
    _RlDhcpSrvMaxAllocatedAddressesAfterReset_Type()
)
rlDhcpSrvMaxAllocatedAddressesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvMaxAllocatedAddressesAfterReset.setStatus("current")
_RlBrgMacHashChainLen_Type = Integer32
_RlBrgMacHashChainLen_Object = MibScalar
rlBrgMacHashChainLen = _RlBrgMacHashChainLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 27),
    _RlBrgMacHashChainLen_Type()
)
rlBrgMacHashChainLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacHashChainLen.setStatus("current")


class _RlBrgMacHashChainLenAfterReset_Type(Integer32):
    """Custom type rlBrgMacHashChainLenAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlBrgMacHashChainLenAfterReset_Type.__name__ = "Integer32"
_RlBrgMacHashChainLenAfterReset_Object = MibScalar
rlBrgMacHashChainLenAfterReset = _RlBrgMacHashChainLenAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 28),
    _RlBrgMacHashChainLenAfterReset_Type()
)
rlBrgMacHashChainLenAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacHashChainLenAfterReset.setStatus("current")


class _RlBrgMacHashFunction_Type(Integer32):
    """Custom type rlBrgMacHashFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macRndVlanRnd", 3),
          ("macRndVlanSqn", 1),
          ("macSqnVlanRnd", 2),
          ("macSqnVlanSqn", 0))
    )


_RlBrgMacHashFunction_Type.__name__ = "Integer32"
_RlBrgMacHashFunction_Object = MibScalar
rlBrgMacHashFunction = _RlBrgMacHashFunction_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 29),
    _RlBrgMacHashFunction_Type()
)
rlBrgMacHashFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacHashFunction.setStatus("current")


class _RlBrgMacHashFunctionAfterReset_Type(Integer32):
    """Custom type rlBrgMacHashFunctionAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macRndVlanRnd", 3),
          ("macRndVlanSqn", 1),
          ("macSqnVlanRnd", 2),
          ("macSqnVlanSqn", 0))
    )


_RlBrgMacHashFunctionAfterReset_Type.__name__ = "Integer32"
_RlBrgMacHashFunctionAfterReset_Object = MibScalar
rlBrgMacHashFunctionAfterReset = _RlBrgMacHashFunctionAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 30),
    _RlBrgMacHashFunctionAfterReset_Type()
)
rlBrgMacHashFunctionAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacHashFunctionAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-Tuning",
    **{"rsTunning": rsTunning,
       "rsHighPriority": rsHighPriority,
       "rsLowPriority": rsLowPriority,
       "rsDbgLevel": rsDbgLevel,
       "rsDiagnosticsTable": rsDiagnosticsTable,
       "rsDiagnosticsEntry": rsDiagnosticsEntry,
       "rsDiagnosticsRequestId": rsDiagnosticsRequestId,
       "rsDiagnosticsCode": rsDiagnosticsCode,
       "rsDiagnosticsLocation": rsDiagnosticsLocation,
       "rsDiagnosticsText": rsDiagnosticsText,
       "rsConfirmMessagTab": rsConfirmMessagTab,
       "eventMessageTable": eventMessageTable,
       "eventMessageEntry": eventMessageEntry,
       "eventNum": eventNum,
       "eventDesc": eventDesc,
       "reaTunning": reaTunning,
       "reaIpForwardEnable": reaIpForwardEnable,
       "reaIpxForwardEnable": reaIpxForwardEnable,
       "rsMaxEntriesTuning": rsMaxEntriesTuning,
       "rsMaxBridgeForwardingEntriesTuning": rsMaxBridgeForwardingEntriesTuning,
       "rsMaxBrgFrwEntries": rsMaxBrgFrwEntries,
       "rsMaxBrgFrwEntriesAfterReset": rsMaxBrgFrwEntriesAfterReset,
       "rsMaxIpForwardingEntriesTuning": rsMaxIpForwardingEntriesTuning,
       "rsMaxIpFrwEntries": rsMaxIpFrwEntries,
       "rsMaxIpFrwEntriesAfterReset": rsMaxIpFrwEntriesAfterReset,
       "rsMaxArpEntriesTuning": rsMaxArpEntriesTuning,
       "rsMaxArpEntries": rsMaxArpEntries,
       "rsMaxArpEntriesAfterReset": rsMaxArpEntriesAfterReset,
       "rsMaxIpxForwardingEntriesTuning": rsMaxIpxForwardingEntriesTuning,
       "rsMaxIpxFrwEntries": rsMaxIpxFrwEntries,
       "rsMaxIpxFrwEntriesAfterReset": rsMaxIpxFrwEntriesAfterReset,
       "rsMaxIpxSapEntriesTuning": rsMaxIpxSapEntriesTuning,
       "rsMaxIpxSapEntries": rsMaxIpxSapEntries,
       "rsMaxIpxSapEntriesAfterReset": rsMaxIpxSapEntriesAfterReset,
       "rsMaxDspClntEntriesTuning": rsMaxDspClntEntriesTuning,
       "rsMaxDspClntEntries": rsMaxDspClntEntries,
       "rsMaxDspClntEntriesAfterReset": rsMaxDspClntEntriesAfterReset,
       "rsMaxIpFftEntriesTuning": rsMaxIpFftEntriesTuning,
       "rsMaxIpSFftEntries": rsMaxIpSFftEntries,
       "rsMaxIpSFftEntriesAfterReset": rsMaxIpSFftEntriesAfterReset,
       "rsMaxIpNFftEntries": rsMaxIpNFftEntries,
       "rsMaxIpNFftEntriesAfterReset": rsMaxIpNFftEntriesAfterReset,
       "rsMaxIpSFftSysEntries": rsMaxIpSFftSysEntries,
       "rsMaxIpSFftSysEntriesAfterReset": rsMaxIpSFftSysEntriesAfterReset,
       "rsMaxIpNFftSysEntries": rsMaxIpNFftSysEntries,
       "rsMaxIpNFftSysEntriesAfterReset": rsMaxIpNFftSysEntriesAfterReset,
       "rsMaxIpNextHopEntries": rsMaxIpNextHopEntries,
       "rsMaxIpNextHopEntriesAfterReset": rsMaxIpNextHopEntriesAfterReset,
       "rsMaxIpxFftEntriesTuning": rsMaxIpxFftEntriesTuning,
       "rsMaxIpxSFftEntries": rsMaxIpxSFftEntries,
       "rsMaxIpxSFftEntriesAfterReset": rsMaxIpxSFftEntriesAfterReset,
       "rsMaxIpxNFftEntries": rsMaxIpxNFftEntries,
       "rsMaxIpxNFftEntriesAfterReset": rsMaxIpxNFftEntriesAfterReset,
       "rsMaxIpxSFftSysEntries": rsMaxIpxSFftSysEntries,
       "rsMaxIpxSFftSysEntriesAfterReset": rsMaxIpxSFftSysEntriesAfterReset,
       "rsMaxIpxNFftSysEntries": rsMaxIpxNFftSysEntries,
       "rsMaxIpxNFftSysEntriesAfterReset": rsMaxIpxNFftSysEntriesAfterReset,
       "rsMaxDhcpTuning": rsMaxDhcpTuning,
       "rsMaxDhcpConns": rsMaxDhcpConns,
       "rsMaxDhcpConnsAfterReset": rsMaxDhcpConnsAfterReset,
       "rsMaxIpmTuning": rsMaxIpmTuning,
       "rsMaxIpmFftEntriesTuning": rsMaxIpmFftEntriesTuning,
       "rsMaxIpmFftEntries": rsMaxIpmFftEntries,
       "rsMaxIpmFftEntriesAfterReset": rsMaxIpmFftEntriesAfterReset,
       "rsIpmFftAging": rsIpmFftAging,
       "rsMaxIgmpTuning": rsMaxIgmpTuning,
       "rsMaxIgmpInterfaceEntries": rsMaxIgmpInterfaceEntries,
       "rsMaxIgmpInterfaceEntriesAfterReset": rsMaxIgmpInterfaceEntriesAfterReset,
       "rsMaxIgmpCacheEntries": rsMaxIgmpCacheEntries,
       "rsMaxIgmpCacheEntriesAfterReset": rsMaxIgmpCacheEntriesAfterReset,
       "rsMaxPimTuning": rsMaxPimTuning,
       "rsMaxPimNeighborEntries": rsMaxPimNeighborEntries,
       "rsMaxPimNeighborEntriesAfterReset": rsMaxPimNeighborEntriesAfterReset,
       "rsMaxPimRouteEntries": rsMaxPimRouteEntries,
       "rsMaxPimRouteEntriesAfterReset": rsMaxPimRouteEntriesAfterReset,
       "rsMaxPimRouteNextHopEntries": rsMaxPimRouteNextHopEntries,
       "rsMaxPimRouteNextHopEntriesAfterReset": rsMaxPimRouteNextHopEntriesAfterReset,
       "rsMaxPimInterfaceEntriesAfterReset": rsMaxPimInterfaceEntriesAfterReset,
       "rsMaxPimInterfaceEntries": rsMaxPimInterfaceEntries,
       "rsMaxDvmrpTuning": rsMaxDvmrpTuning,
       "rsMaxDvmrpNeighborEntries": rsMaxDvmrpNeighborEntries,
       "rsMaxDvmrpNeighborEntriesAfterReset": rsMaxDvmrpNeighborEntriesAfterReset,
       "rsMaxDvmrpRouteEntries": rsMaxDvmrpRouteEntries,
       "rsMaxDvmrpRouteEntriesAfterReset": rsMaxDvmrpRouteEntriesAfterReset,
       "rsMaxDvmrpMRouteEntries": rsMaxDvmrpMRouteEntries,
       "rsMaxDvmrpMRouteEntriesAfterReset": rsMaxDvmrpMRouteEntriesAfterReset,
       "rsMaxDvmrpInterfaceEntries": rsMaxDvmrpInterfaceEntries,
       "rsMaxDvmrpInterfaceEntriesAfterReset": rsMaxDvmrpInterfaceEntriesAfterReset,
       "rsMaxPigmpTuning": rsMaxPigmpTuning,
       "rsMaxPigmpRouteEntries": rsMaxPigmpRouteEntries,
       "rsMaxPigmpRouteEntriesAfterReset": rsMaxPigmpRouteEntriesAfterReset,
       "rsMaxPimSmTuning": rsMaxPimSmTuning,
       "rsMaxPimSmNeighborEntries": rsMaxPimSmNeighborEntries,
       "rsMaxPimSmNeighborEntriesAfterReset": rsMaxPimSmNeighborEntriesAfterReset,
       "rsMaxPimSmRouteEntries": rsMaxPimSmRouteEntries,
       "rsMaxPimSmRouteEntriesAfterReset": rsMaxPimSmRouteEntriesAfterReset,
       "rsMaxPimSmInterfaceEntries": rsMaxPimSmInterfaceEntries,
       "rsMaxPimSmInterfaceEntriesAfterReset": rsMaxPimSmInterfaceEntriesAfterReset,
       "rsMaxPimSmRPSetEntries": rsMaxPimSmRPSetEntries,
       "rsMaxPimSmRPSetEntriesAfterReset": rsMaxPimSmRPSetEntriesAfterReset,
       "rsMaxPimSmCRPEntries": rsMaxPimSmCRPEntries,
       "rsMaxPimSmCRPEntriesAfterReset": rsMaxPimSmCRPEntriesAfterReset,
       "rsMaxNumberRpAddresesInGroupRange": rsMaxNumberRpAddresesInGroupRange,
       "rsMaxNumberRpAddresesInGroupRangeAfterReset": rsMaxNumberRpAddresesInGroupRangeAfterReset,
       "rsMaxRmonTuning": rsMaxRmonTuning,
       "rsMaxRmonLogEntries": rsMaxRmonLogEntries,
       "rsMaxRmonLogEntriesAfterReset": rsMaxRmonLogEntriesAfterReset,
       "rsMaxRmonEtherHistoryEntries": rsMaxRmonEtherHistoryEntries,
       "rsMaxRmonEtherHistoryEntriesAfterReset": rsMaxRmonEtherHistoryEntriesAfterReset,
       "rsMaxIgmpSnoopTuning": rsMaxIgmpSnoopTuning,
       "rsMaxIgmpSnoopGroupEntries": rsMaxIgmpSnoopGroupEntries,
       "rsMaxIgmpSnoopGroupEntriesAfterReset": rsMaxIgmpSnoopGroupEntriesAfterReset,
       "rsMaxVlansTuning": rsMaxVlansTuning,
       "rsMaxVlansEntries": rsMaxVlansEntries,
       "rsMaxVlansEntriesAfterReset": rsMaxVlansEntriesAfterReset,
       "rsMaxPolicyTuning": rsMaxPolicyTuning,
       "rsMaxPolicyMaxRulesEntries": rsMaxPolicyMaxRulesEntries,
       "rsMaxPolicyMaxRulesEntriesAfterReset": rsMaxPolicyMaxRulesEntriesAfterReset,
       "rsMaxPolicySimpleMibMaxRulesEntries": rsMaxPolicySimpleMibMaxRulesEntries,
       "rsMaxPolicySimpleMibMaxRulesEntriesAfterReset": rsMaxPolicySimpleMibMaxRulesEntriesAfterReset,
       "rsMaxPolicySimpleMibMaxProfilesEntries": rsMaxPolicySimpleMibMaxProfilesEntries,
       "rsMaxPolicySimpleMibMaxProfilesEntriesAfterReset": rsMaxPolicySimpleMibMaxProfilesEntriesAfterReset,
       "rsMaxGvrpVlansTuning": rsMaxGvrpVlansTuning,
       "rsMaxGvrpVlans": rsMaxGvrpVlans,
       "rsMaxGvrpVlansAfterReset": rsMaxGvrpVlansAfterReset,
       "rsMaxTraceRouteTuning": rsMaxTraceRouteTuning,
       "rsMaxTraceRouteControlEntries": rsMaxTraceRouteControlEntries,
       "rsMaxTraceRouteControlEntriesAfterReset": rsMaxTraceRouteControlEntriesAfterReset,
       "rsMaxTraceRouteProbeHistoryEntries": rsMaxTraceRouteProbeHistoryEntries,
       "rsMaxTraceRouteProbeHistoryEntriesAfterReset": rsMaxTraceRouteProbeHistoryEntriesAfterReset,
       "rsMaxSnmpTuning": rsMaxSnmpTuning,
       "rsMaxSnmpCommunityEntries": rsMaxSnmpCommunityEntries,
       "rsMaxSnmpCommunityEntriesAfterReset": rsMaxSnmpCommunityEntriesAfterReset,
       "rsMaxSocketTuning": rsMaxSocketTuning,
       "rsMaxNumberOfSockets": rsMaxNumberOfSockets,
       "rsMaxNumberOfSocketsAfterReset": rsMaxNumberOfSocketsAfterReset,
       "rsMaxSizeOfSocketDataPool": rsMaxSizeOfSocketDataPool,
       "rsMaxSizeOfSocketDataPoolAfterReset": rsMaxSizeOfSocketDataPoolAfterReset,
       "rsMaxIpRouteTuning": rsMaxIpRouteTuning,
       "rsMaxIpPrefixes": rsMaxIpPrefixes,
       "rsMaxIpPrefixesAfterReset": rsMaxIpPrefixesAfterReset,
       "rsMaxIpNextHopSetTuning": rsMaxIpNextHopSetTuning,
       "rsMaxIpNextHopSetEntries": rsMaxIpNextHopSetEntries,
       "rsMaxIpNextHopSetEntriesAfterReset": rsMaxIpNextHopSetEntriesAfterReset,
       "rsMaxIpEcmpTuning": rsMaxIpEcmpTuning,
       "rsMaxIpEcmpEntrySize": rsMaxIpEcmpEntrySize,
       "rsMaxIpEcmpEntrySizeAfterReset": rsMaxIpEcmpEntrySizeAfterReset,
       "rsMaxdot1xEapRequestTuning": rsMaxdot1xEapRequestTuning,
       "rsMaxdot1xEapRequestEntries": rsMaxdot1xEapRequestEntries,
       "rsMaxdot1xEapRequestEntriesAfterReset": rsMaxdot1xEapRequestEntriesAfterReset,
       "rsMaxIpInterfaceTuning": rsMaxIpInterfaceTuning,
       "rsMaxIpInterfaces": rsMaxIpInterfaces,
       "rsMaxIpInterfacesAfterReset": rsMaxIpInterfacesAfterReset,
       "rsMaxIpv6FftEntriesTuning": rsMaxIpv6FftEntriesTuning,
       "rsMaxIpv6SFftEntries": rsMaxIpv6SFftEntries,
       "rsMaxIpv6SFftEntriesAfterReset": rsMaxIpv6SFftEntriesAfterReset,
       "rsMaxIpv6SFftSysEntries": rsMaxIpv6SFftSysEntries,
       "rsMaxIpv6SFftSysEntriesAfterReset": rsMaxIpv6SFftSysEntriesAfterReset,
       "rsMaxIpv6Prefixes": rsMaxIpv6Prefixes,
       "rsMaxIpv6PrefixesAfterReset": rsMaxIpv6PrefixesAfterReset,
       "rsMaxIpv6NextHopEntries": rsMaxIpv6NextHopEntries,
       "rsMaxIpv6NextHopEntriesAfterReset": rsMaxIpv6NextHopEntriesAfterReset,
       "rsMaxIpv6NextHopSetEntries": rsMaxIpv6NextHopSetEntries,
       "rsMaxIpv6NextHopSetEntriesAfterReset": rsMaxIpv6NextHopSetEntriesAfterReset,
       "rsMaxIpv6GlobalAddresses": rsMaxIpv6GlobalAddresses,
       "rsMaxIpv6GlobalAddressesAfterReset": rsMaxIpv6GlobalAddressesAfterReset,
       "rsMaxArpTunnelStartEntries": rsMaxArpTunnelStartEntries,
       "rsMaxArpTunnelStartEntriesAfterReset": rsMaxArpTunnelStartEntriesAfterReset,
       "rsMaxIpv6InterfaceTuning": rsMaxIpv6InterfaceTuning,
       "rsMaxIpv6Interfaces": rsMaxIpv6Interfaces,
       "rsMaxIpv6InterfacesAfterReset": rsMaxIpv6InterfacesAfterReset,
       "rsMaxIpv6AddrPerInterfaces": rsMaxIpv6AddrPerInterfaces,
       "rsMaxIpv6AddrPerInterfacesAfterReset": rsMaxIpv6AddrPerInterfacesAfterReset,
       "rsMaxIpRoutesTuning": rsMaxIpRoutesTuning,
       "rsMaxIpv4Routes": rsMaxIpv4Routes,
       "rsMaxIpv4RoutesAfterReset": rsMaxIpv4RoutesAfterReset,
       "rsMaxIpv6Routes": rsMaxIpv6Routes,
       "rsMaxIpv6RoutesAfterReset": rsMaxIpv6RoutesAfterReset,
       "rsMaxIpmv4Routes": rsMaxIpmv4Routes,
       "rsMaxIpmv4RoutesAfterReset": rsMaxIpmv4RoutesAfterReset,
       "rsMaxIpmv6Routes": rsMaxIpmv6Routes,
       "rsMaxIpmv6RoutesAfterReset": rsMaxIpmv6RoutesAfterReset,
       "rsTcpTuning": rsTcpTuning,
       "rsTcpMemoryPoolSizeAfterReset": rsTcpMemoryPoolSizeAfterReset,
       "rsTcpMemoryPoolSize": rsTcpMemoryPoolSize,
       "rsRadiusTuning": rsRadiusTuning,
       "rsRadiusMemoryPoolSizeAfterReset": rsRadiusMemoryPoolSizeAfterReset,
       "rsRadiusMemoryPoolSize": rsRadiusMemoryPoolSize,
       "rlSyslogTuning": rlSyslogTuning,
       "rlSyslogFilePercentToDeleteWhenCompacting": rlSyslogFilePercentToDeleteWhenCompacting,
       "rlSyslogFilePercentToDeleteWhenCompactingAfterReset": rlSyslogFilePercentToDeleteWhenCompactingAfterReset,
       "rlSyslogCacheSize": rlSyslogCacheSize,
       "rlSyslogCacheSizeAfterReset": rlSyslogCacheSizeAfterReset,
       "rlMngInfTuning": rlMngInfTuning,
       "rlMaxNumberOfAccessRules": rlMaxNumberOfAccessRules,
       "rlMaxNumberOfAccessRulesAfterReset": rlMaxNumberOfAccessRulesAfterReset,
       "rsDiagnosticTextSource": rsDiagnosticTextSource,
       "rsMultiSession": rsMultiSession,
       "rsMultiSessionMaxSessionsAfterReset": rsMultiSessionMaxSessionsAfterReset,
       "rsMultiSessionMaxSessions": rsMultiSessionMaxSessions,
       "rlDnsClTuning": rlDnsClTuning,
       "rlMaxDnsClCacheRREntries": rlMaxDnsClCacheRREntries,
       "rlMaxDnsClCacheRREntriesAfterReset": rlMaxDnsClCacheRREntriesAfterReset,
       "rlMaxDnsClNCacheErrEntries": rlMaxDnsClNCacheErrEntries,
       "rlMaxDnsClNCacheErrEntriesAfterReset": rlMaxDnsClNCacheErrEntriesAfterReset,
       "rlMaxDnsClNamesEntries": rlMaxDnsClNamesEntries,
       "rlMaxDnsClNamesEntriesAfterReset": rlMaxDnsClNamesEntriesAfterReset,
       "rlTuningParamsTable": rlTuningParamsTable,
       "rlTuningParamsEntry": rlTuningParamsEntry,
       "rlTuningParamsName": rlTuningParamsName,
       "rlTuningParamsCurrentValue": rlTuningParamsCurrentValue,
       "rlTuningParamsAfterResetValue": rlTuningParamsAfterResetValue,
       "rlTuningParamsDefaultValue": rlTuningParamsDefaultValue,
       "rlTuningParamsMinimalValue": rlTuningParamsMinimalValue,
       "rlTuningParamsMaximalValue": rlTuningParamsMaximalValue,
       "rlHostParamTable": rlHostParamTable,
       "rlHostParamEntry": rlHostParamEntry,
       "rlHostParamName": rlHostParamName,
       "rlHostParamValue": rlHostParamValue,
       "rlHostParamType": rlHostParamType,
       "rlHostParamUINT": rlHostParamUINT,
       "rlHostParamOctetString": rlHostParamOctetString,
       "rlHostParamIpAddress": rlHostParamIpAddress,
       "rlHostParamObjectId": rlHostParamObjectId,
       "rlOspfTuning": rlOspfTuning,
       "rlMaxOspfInterfaces": rlMaxOspfInterfaces,
       "rlMaxOspfInterfacesAfterReset": rlMaxOspfInterfacesAfterReset,
       "rlMaxOspfAreas": rlMaxOspfAreas,
       "rlMaxOspfAreasAfterReset": rlMaxOspfAreasAfterReset,
       "rlMaxOspfNeighbors": rlMaxOspfNeighbors,
       "rlMaxOspfNeighborsAfterReset": rlMaxOspfNeighborsAfterReset,
       "rlMaxOspfAbrPerArea": rlMaxOspfAbrPerArea,
       "rlMaxOspfAbrPerAreaAfterReset": rlMaxOspfAbrPerAreaAfterReset,
       "rlMaxOspfNetsInAs": rlMaxOspfNetsInAs,
       "rlMaxOspfNetsInAsAfterReset": rlMaxOspfNetsInAsAfterReset,
       "rlVlanTuning": rlVlanTuning,
       "rlVlanDefaultVID": rlVlanDefaultVID,
       "rlVlanDefaultVIDAfterReset": rlVlanDefaultVIDAfterReset,
       "rlVlanUsageForbiddenListTable": rlVlanUsageForbiddenListTable,
       "rlVlanUsageForbiddenListEntry": rlVlanUsageForbiddenListEntry,
       "rlVlanUsageForbiddenListIndex": rlVlanUsageForbiddenListIndex,
       "rlVlanUsageForbiddenList1to1024": rlVlanUsageForbiddenList1to1024,
       "rlVlanUsageForbiddenList1025to2048": rlVlanUsageForbiddenList1025to2048,
       "rlVlanUsageForbiddenList2049to3072": rlVlanUsageForbiddenList2049to3072,
       "rlVlanUsageForbiddenList3073to4094": rlVlanUsageForbiddenList3073to4094,
       "rlVlanUsageForbiddenListAfterResetTable": rlVlanUsageForbiddenListAfterResetTable,
       "rlVlanUsageForbiddenListAfterResetEntry": rlVlanUsageForbiddenListAfterResetEntry,
       "rlVlanUsageForbiddenListAfterResetIndex": rlVlanUsageForbiddenListAfterResetIndex,
       "rlVlanUsageForbiddenListAfterReset1to1024": rlVlanUsageForbiddenListAfterReset1to1024,
       "rlVlanUsageForbiddenListAfterReset1025to2048": rlVlanUsageForbiddenListAfterReset1025to2048,
       "rlVlanUsageForbiddenListAfterReset2049to3072": rlVlanUsageForbiddenListAfterReset2049to3072,
       "rlVlanUsageForbiddenListAfterReset3073to4094": rlVlanUsageForbiddenListAfterReset3073to4094,
       "rlDependendFeaturesEnableTuning": rlDependendFeaturesEnableTuning,
       "rlDependendFeaturesEnabled": rlDependendFeaturesEnabled,
       "rlDependendFeaturesEnabledAfterReset": rlDependendFeaturesEnabledAfterReset,
       "rlIpDhcpSnoopingTuning": rlIpDhcpSnoopingTuning,
       "rlMaxIpDhcpSnoopingEntries": rlMaxIpDhcpSnoopingEntries,
       "rlMaxIpDhcpSnoopingEntriesAfterReset": rlMaxIpDhcpSnoopingEntriesAfterReset,
       "rlIscsiSnoopTuning": rlIscsiSnoopTuning,
       "rlIscsiSnoopMaxNumOfConnections": rlIscsiSnoopMaxNumOfConnections,
       "rlIscsiSnoopMaxNumOfConnectionsAfterReset": rlIscsiSnoopMaxNumOfConnectionsAfterReset,
       "rlDhcpServerTuning": rlDhcpServerTuning,
       "rlDhcpSrvMaxAllocatedAddresses": rlDhcpSrvMaxAllocatedAddresses,
       "rlDhcpSrvMaxAllocatedAddressesAfterReset": rlDhcpSrvMaxAllocatedAddressesAfterReset,
       "rlBrgMacHashChainLen": rlBrgMacHashChainLen,
       "rlBrgMacHashChainLenAfterReset": rlBrgMacHashChainLenAfterReset,
       "rlBrgMacHashFunction": rlBrgMacHashFunction,
       "rlBrgMacHashFunctionAfterReset": rlBrgMacHashFunctionAfterReset}
)
