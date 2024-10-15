# SNMP MIB module (Wellfleet-PROTOPRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-PROTOPRI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:56 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfProtocolPriorityGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfProtocolPriorityGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfProtoPriQTable_Object = MibTable
wfProtoPriQTable = _WfProtoPriQTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1)
)
if mibBuilder.loadTexts:
    wfProtoPriQTable.setStatus("mandatory")
_WfProtoPriQEntry_Object = MibTableRow
wfProtoPriQEntry = _WfProtoPriQEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1)
)
wfProtoPriQEntry.setIndexNames(
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriPeerAddr"),
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriClientId"),
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriQueueNumber"),
)
if mibBuilder.loadTexts:
    wfProtoPriQEntry.setStatus("mandatory")


class _WfProtoPriQueueDelete_Type(Integer32):
    """Custom type wfProtoPriQueueDelete based on Integer32"""
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


_WfProtoPriQueueDelete_Type.__name__ = "Integer32"
_WfProtoPriQueueDelete_Object = MibTableColumn
wfProtoPriQueueDelete = _WfProtoPriQueueDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 1),
    _WfProtoPriQueueDelete_Type()
)
wfProtoPriQueueDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfProtoPriQueueDelete.setStatus("mandatory")
_WfProtoPriClientId_Type = Integer32
_WfProtoPriClientId_Object = MibTableColumn
wfProtoPriClientId = _WfProtoPriClientId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 2),
    _WfProtoPriClientId_Type()
)
wfProtoPriClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriClientId.setStatus("mandatory")
_WfProtoPriQueueNumber_Type = Integer32
_WfProtoPriQueueNumber_Object = MibTableColumn
wfProtoPriQueueNumber = _WfProtoPriQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 3),
    _WfProtoPriQueueNumber_Type()
)
wfProtoPriQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueNumber.setStatus("mandatory")


class _WfProtoPriQueueBandwidthPercent_Type(Integer32):
    """Custom type wfProtoPriQueueBandwidthPercent based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("default", 10)
    )


_WfProtoPriQueueBandwidthPercent_Type.__name__ = "Integer32"
_WfProtoPriQueueBandwidthPercent_Object = MibTableColumn
wfProtoPriQueueBandwidthPercent = _WfProtoPriQueueBandwidthPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 4),
    _WfProtoPriQueueBandwidthPercent_Type()
)
wfProtoPriQueueBandwidthPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfProtoPriQueueBandwidthPercent.setStatus("mandatory")
_WfProtoPriQueueHighWaterPkts_Type = Gauge32
_WfProtoPriQueueHighWaterPkts_Object = MibTableColumn
wfProtoPriQueueHighWaterPkts = _WfProtoPriQueueHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 5),
    _WfProtoPriQueueHighWaterPkts_Type()
)
wfProtoPriQueueHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueHighWaterPkts.setStatus("mandatory")
_WfProtoPriQueueTxPkts_Type = Counter32
_WfProtoPriQueueTxPkts_Object = MibTableColumn
wfProtoPriQueueTxPkts = _WfProtoPriQueueTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 6),
    _WfProtoPriQueueTxPkts_Type()
)
wfProtoPriQueueTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueTxPkts.setStatus("mandatory")
_WfProtoPriQueueTotalTxOctets_Type = Counter32
_WfProtoPriQueueTotalTxOctets_Object = MibTableColumn
wfProtoPriQueueTotalTxOctets = _WfProtoPriQueueTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 7),
    _WfProtoPriQueueTotalTxOctets_Type()
)
wfProtoPriQueueTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueTotalTxOctets.setStatus("mandatory")
_WfProtoPriQueueLargePkts_Type = Counter32
_WfProtoPriQueueLargePkts_Object = MibTableColumn
wfProtoPriQueueLargePkts = _WfProtoPriQueueLargePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 8),
    _WfProtoPriQueueLargePkts_Type()
)
wfProtoPriQueueLargePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueLargePkts.setStatus("mandatory")
_WfProtoPriQueueClippedPkts_Type = Counter32
_WfProtoPriQueueClippedPkts_Object = MibTableColumn
wfProtoPriQueueClippedPkts = _WfProtoPriQueueClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 9),
    _WfProtoPriQueueClippedPkts_Type()
)
wfProtoPriQueueClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueClippedPkts.setStatus("mandatory")
_WfProtoPriPeerAddr_Type = IpAddress
_WfProtoPriPeerAddr_Object = MibTableColumn
wfProtoPriPeerAddr = _WfProtoPriPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 10),
    _WfProtoPriPeerAddr_Type()
)
wfProtoPriPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriPeerAddr.setStatus("mandatory")
_WfProtoPriQueueHighWaterBytes_Type = Gauge32
_WfProtoPriQueueHighWaterBytes_Object = MibTableColumn
wfProtoPriQueueHighWaterBytes = _WfProtoPriQueueHighWaterBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 11),
    _WfProtoPriQueueHighWaterBytes_Type()
)
wfProtoPriQueueHighWaterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriQueueHighWaterBytes.setStatus("mandatory")
_WfProtoPriCCPkts_Type = Counter32
_WfProtoPriCCPkts_Object = MibTableColumn
wfProtoPriCCPkts = _WfProtoPriCCPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 12),
    _WfProtoPriCCPkts_Type()
)
wfProtoPriCCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriCCPkts.setStatus("mandatory")
_WfProtoPriCCOctets_Type = Counter32
_WfProtoPriCCOctets_Object = MibTableColumn
wfProtoPriCCOctets = _WfProtoPriCCOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 13),
    _WfProtoPriCCOctets_Type()
)
wfProtoPriCCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriCCOctets.setStatus("mandatory")
_WfProtoPriCCHighWaterPkts_Type = Gauge32
_WfProtoPriCCHighWaterPkts_Object = MibTableColumn
wfProtoPriCCHighWaterPkts = _WfProtoPriCCHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 14),
    _WfProtoPriCCHighWaterPkts_Type()
)
wfProtoPriCCHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriCCHighWaterPkts.setStatus("mandatory")
_WfProtoPriCCHighWaterBytes_Type = Gauge32
_WfProtoPriCCHighWaterBytes_Object = MibTableColumn
wfProtoPriCCHighWaterBytes = _WfProtoPriCCHighWaterBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 1, 1, 15),
    _WfProtoPriCCHighWaterBytes_Type()
)
wfProtoPriCCHighWaterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriCCHighWaterBytes.setStatus("mandatory")
_WfProtoPriFilterTable_Object = MibTable
wfProtoPriFilterTable = _WfProtoPriFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2)
)
if mibBuilder.loadTexts:
    wfProtoPriFilterTable.setStatus("mandatory")
_WfProtoPriFilterEntry_Object = MibTableRow
wfProtoPriFilterEntry = _WfProtoPriFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1)
)
wfProtoPriFilterEntry.setIndexNames(
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriFilterPeerAddr"),
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriFilterClientId"),
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriFilterRuleNumber"),
    (0, "Wellfleet-PROTOPRI-MIB", "wfProtoPriFilterFragment"),
)
if mibBuilder.loadTexts:
    wfProtoPriFilterEntry.setStatus("mandatory")


class _WfProtoPriFilterCreate_Type(Integer32):
    """Custom type wfProtoPriFilterCreate based on Integer32"""
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


_WfProtoPriFilterCreate_Type.__name__ = "Integer32"
_WfProtoPriFilterCreate_Object = MibTableColumn
wfProtoPriFilterCreate = _WfProtoPriFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 1),
    _WfProtoPriFilterCreate_Type()
)
wfProtoPriFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfProtoPriFilterCreate.setStatus("mandatory")


class _WfProtoPriFilterEnable_Type(Integer32):
    """Custom type wfProtoPriFilterEnable based on Integer32"""
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


_WfProtoPriFilterEnable_Type.__name__ = "Integer32"
_WfProtoPriFilterEnable_Object = MibTableColumn
wfProtoPriFilterEnable = _WfProtoPriFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 2),
    _WfProtoPriFilterEnable_Type()
)
wfProtoPriFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfProtoPriFilterEnable.setStatus("mandatory")


class _WfProtoPriFilterState_Type(Integer32):
    """Custom type wfProtoPriFilterState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfProtoPriFilterState_Type.__name__ = "Integer32"
_WfProtoPriFilterState_Object = MibTableColumn
wfProtoPriFilterState = _WfProtoPriFilterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 3),
    _WfProtoPriFilterState_Type()
)
wfProtoPriFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterState.setStatus("mandatory")
_WfProtoPriFilterCounter_Type = Counter32
_WfProtoPriFilterCounter_Object = MibTableColumn
wfProtoPriFilterCounter = _WfProtoPriFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 4),
    _WfProtoPriFilterCounter_Type()
)
wfProtoPriFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterCounter.setStatus("mandatory")
_WfProtoPriFilterDefinition_Type = OctetString
_WfProtoPriFilterDefinition_Object = MibTableColumn
wfProtoPriFilterDefinition = _WfProtoPriFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 5),
    _WfProtoPriFilterDefinition_Type()
)
wfProtoPriFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfProtoPriFilterDefinition.setStatus("mandatory")
_WfProtoPriFilterReserved_Type = Integer32
_WfProtoPriFilterReserved_Object = MibTableColumn
wfProtoPriFilterReserved = _WfProtoPriFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 6),
    _WfProtoPriFilterReserved_Type()
)
wfProtoPriFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterReserved.setStatus("mandatory")
_WfProtoPriFilterPeerAddr_Type = IpAddress
_WfProtoPriFilterPeerAddr_Object = MibTableColumn
wfProtoPriFilterPeerAddr = _WfProtoPriFilterPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 7),
    _WfProtoPriFilterPeerAddr_Type()
)
wfProtoPriFilterPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterPeerAddr.setStatus("mandatory")
_WfProtoPriFilterClientId_Type = Integer32
_WfProtoPriFilterClientId_Object = MibTableColumn
wfProtoPriFilterClientId = _WfProtoPriFilterClientId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 8),
    _WfProtoPriFilterClientId_Type()
)
wfProtoPriFilterClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterClientId.setStatus("mandatory")
_WfProtoPriFilterRuleNumber_Type = Integer32
_WfProtoPriFilterRuleNumber_Object = MibTableColumn
wfProtoPriFilterRuleNumber = _WfProtoPriFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 9),
    _WfProtoPriFilterRuleNumber_Type()
)
wfProtoPriFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterRuleNumber.setStatus("mandatory")
_WfProtoPriFilterFragment_Type = Integer32
_WfProtoPriFilterFragment_Object = MibTableColumn
wfProtoPriFilterFragment = _WfProtoPriFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 10),
    _WfProtoPriFilterFragment_Type()
)
wfProtoPriFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfProtoPriFilterFragment.setStatus("mandatory")
_WfProtoPriFilterName_Type = DisplayString
_WfProtoPriFilterName_Object = MibTableColumn
wfProtoPriFilterName = _WfProtoPriFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9, 2, 1, 11),
    _WfProtoPriFilterName_Type()
)
wfProtoPriFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfProtoPriFilterName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-PROTOPRI-MIB",
    **{"wfProtoPriQTable": wfProtoPriQTable,
       "wfProtoPriQEntry": wfProtoPriQEntry,
       "wfProtoPriQueueDelete": wfProtoPriQueueDelete,
       "wfProtoPriClientId": wfProtoPriClientId,
       "wfProtoPriQueueNumber": wfProtoPriQueueNumber,
       "wfProtoPriQueueBandwidthPercent": wfProtoPriQueueBandwidthPercent,
       "wfProtoPriQueueHighWaterPkts": wfProtoPriQueueHighWaterPkts,
       "wfProtoPriQueueTxPkts": wfProtoPriQueueTxPkts,
       "wfProtoPriQueueTotalTxOctets": wfProtoPriQueueTotalTxOctets,
       "wfProtoPriQueueLargePkts": wfProtoPriQueueLargePkts,
       "wfProtoPriQueueClippedPkts": wfProtoPriQueueClippedPkts,
       "wfProtoPriPeerAddr": wfProtoPriPeerAddr,
       "wfProtoPriQueueHighWaterBytes": wfProtoPriQueueHighWaterBytes,
       "wfProtoPriCCPkts": wfProtoPriCCPkts,
       "wfProtoPriCCOctets": wfProtoPriCCOctets,
       "wfProtoPriCCHighWaterPkts": wfProtoPriCCHighWaterPkts,
       "wfProtoPriCCHighWaterBytes": wfProtoPriCCHighWaterBytes,
       "wfProtoPriFilterTable": wfProtoPriFilterTable,
       "wfProtoPriFilterEntry": wfProtoPriFilterEntry,
       "wfProtoPriFilterCreate": wfProtoPriFilterCreate,
       "wfProtoPriFilterEnable": wfProtoPriFilterEnable,
       "wfProtoPriFilterState": wfProtoPriFilterState,
       "wfProtoPriFilterCounter": wfProtoPriFilterCounter,
       "wfProtoPriFilterDefinition": wfProtoPriFilterDefinition,
       "wfProtoPriFilterReserved": wfProtoPriFilterReserved,
       "wfProtoPriFilterPeerAddr": wfProtoPriFilterPeerAddr,
       "wfProtoPriFilterClientId": wfProtoPriFilterClientId,
       "wfProtoPriFilterRuleNumber": wfProtoPriFilterRuleNumber,
       "wfProtoPriFilterFragment": wfProtoPriFilterFragment,
       "wfProtoPriFilterName": wfProtoPriFilterName}
)
