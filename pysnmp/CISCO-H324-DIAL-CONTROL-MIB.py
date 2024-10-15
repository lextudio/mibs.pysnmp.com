# SNMP MIB module (CISCO-H324-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-H324-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:09 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcGUid,
 CvcVideoCoderRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcGUid",
    "CvcVideoCoderRate")

(AbsoluteCounter32,
 callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32",
    "callActiveIndex",
    "callActiveSetupTime")

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

ciscoH324DialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621)
)
ciscoH324DialControlMIB.setRevisions(
        ("2007-02-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CH324CallType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h324", 1)
    )



# MIB Managed Objects in the order of their OIDs

_CiscoH324DialControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoH324DialControlMIBObjects = _CiscoH324DialControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1)
)
_CH324DialControlCallHistory_ObjectIdentity = ObjectIdentity
cH324DialControlCallHistory = _CH324DialControlCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1)
)
_CH324CallHistoryTable_Object = MibTable
cH324CallHistoryTable = _CH324CallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cH324CallHistoryTable.setStatus("current")
_CH324CallHistoryEntry_Object = MibTableRow
cH324CallHistoryEntry = _CH324CallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1)
)
cH324CallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cH324CallHistoryEntry.setStatus("current")
_CH324CallHistoryConnectionId_Type = CvcGUid
_CH324CallHistoryConnectionId_Object = MibTableColumn
cH324CallHistoryConnectionId = _CH324CallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 1),
    _CH324CallHistoryConnectionId_Type()
)
cH324CallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryConnectionId.setStatus("current")
_CH324CallHistoryIncomingConnectionId_Type = CvcGUid
_CH324CallHistoryIncomingConnectionId_Object = MibTableColumn
cH324CallHistoryIncomingConnectionId = _CH324CallHistoryIncomingConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 2),
    _CH324CallHistoryIncomingConnectionId_Type()
)
cH324CallHistoryIncomingConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryIncomingConnectionId.setStatus("current")
_CH324CallHistoryH324CallType_Type = CH324CallType
_CH324CallHistoryH324CallType_Object = MibTableColumn
cH324CallHistoryH324CallType = _CH324CallHistoryH324CallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 3),
    _CH324CallHistoryH324CallType_Type()
)
cH324CallHistoryH324CallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryH324CallType.setStatus("current")


class _CH324CallHistoryUsedBandwidth_Type(Unsigned32):
    """Custom type cH324CallHistoryUsedBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CH324CallHistoryUsedBandwidth_Type.__name__ = "Unsigned32"
_CH324CallHistoryUsedBandwidth_Object = MibTableColumn
cH324CallHistoryUsedBandwidth = _CH324CallHistoryUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 4),
    _CH324CallHistoryUsedBandwidth_Type()
)
cH324CallHistoryUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryUsedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cH324CallHistoryUsedBandwidth.setUnits("kilobits per second")
_CH324CallHistoryTxVideoCodec_Type = CvcVideoCoderRate
_CH324CallHistoryTxVideoCodec_Object = MibTableColumn
cH324CallHistoryTxVideoCodec = _CH324CallHistoryTxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 5),
    _CH324CallHistoryTxVideoCodec_Type()
)
cH324CallHistoryTxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryTxVideoCodec.setStatus("current")
_CH324CallHistoryTxVideoPackets_Type = AbsoluteCounter32
_CH324CallHistoryTxVideoPackets_Object = MibTableColumn
cH324CallHistoryTxVideoPackets = _CH324CallHistoryTxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 6),
    _CH324CallHistoryTxVideoPackets_Type()
)
cH324CallHistoryTxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryTxVideoPackets.setStatus("current")
_CH324CallHistoryTxVideoBytes_Type = AbsoluteCounter32
_CH324CallHistoryTxVideoBytes_Object = MibTableColumn
cH324CallHistoryTxVideoBytes = _CH324CallHistoryTxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 7),
    _CH324CallHistoryTxVideoBytes_Type()
)
cH324CallHistoryTxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryTxVideoBytes.setStatus("current")
_CH324CallHistoryRxVideoCodec_Type = CvcVideoCoderRate
_CH324CallHistoryRxVideoCodec_Object = MibTableColumn
cH324CallHistoryRxVideoCodec = _CH324CallHistoryRxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 8),
    _CH324CallHistoryRxVideoCodec_Type()
)
cH324CallHistoryRxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryRxVideoCodec.setStatus("current")
_CH324CallHistoryRxVideoPackets_Type = AbsoluteCounter32
_CH324CallHistoryRxVideoPackets_Object = MibTableColumn
cH324CallHistoryRxVideoPackets = _CH324CallHistoryRxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 9),
    _CH324CallHistoryRxVideoPackets_Type()
)
cH324CallHistoryRxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryRxVideoPackets.setStatus("current")
_CH324CallHistoryRxVideoBytes_Type = AbsoluteCounter32
_CH324CallHistoryRxVideoBytes_Object = MibTableColumn
cH324CallHistoryRxVideoBytes = _CH324CallHistoryRxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 1, 1, 1, 10),
    _CH324CallHistoryRxVideoBytes_Type()
)
cH324CallHistoryRxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallHistoryRxVideoBytes.setStatus("current")
_CH324DialControlCallActive_ObjectIdentity = ObjectIdentity
cH324DialControlCallActive = _CH324DialControlCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2)
)
_CH324CallActiveTable_Object = MibTable
cH324CallActiveTable = _CH324CallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cH324CallActiveTable.setStatus("current")
_CH324CallActiveEntry_Object = MibTableRow
cH324CallActiveEntry = _CH324CallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1)
)
cH324CallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cH324CallActiveEntry.setStatus("current")
_CH324CallActiveConnectionId_Type = CvcGUid
_CH324CallActiveConnectionId_Object = MibTableColumn
cH324CallActiveConnectionId = _CH324CallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 1),
    _CH324CallActiveConnectionId_Type()
)
cH324CallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveConnectionId.setStatus("current")
_CH324CallActiveIncomingConnectionId_Type = CvcGUid
_CH324CallActiveIncomingConnectionId_Object = MibTableColumn
cH324CallActiveIncomingConnectionId = _CH324CallActiveIncomingConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 2),
    _CH324CallActiveIncomingConnectionId_Type()
)
cH324CallActiveIncomingConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveIncomingConnectionId.setStatus("current")
_CH324CallActiveH324CallType_Type = CH324CallType
_CH324CallActiveH324CallType_Object = MibTableColumn
cH324CallActiveH324CallType = _CH324CallActiveH324CallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 3),
    _CH324CallActiveH324CallType_Type()
)
cH324CallActiveH324CallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveH324CallType.setStatus("current")


class _CH324CallActiveUsedBandwidth_Type(Unsigned32):
    """Custom type cH324CallActiveUsedBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CH324CallActiveUsedBandwidth_Type.__name__ = "Unsigned32"
_CH324CallActiveUsedBandwidth_Object = MibTableColumn
cH324CallActiveUsedBandwidth = _CH324CallActiveUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 4),
    _CH324CallActiveUsedBandwidth_Type()
)
cH324CallActiveUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveUsedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cH324CallActiveUsedBandwidth.setUnits("kilobits per second")
_CH324CallActiveTxVideoCodec_Type = CvcVideoCoderRate
_CH324CallActiveTxVideoCodec_Object = MibTableColumn
cH324CallActiveTxVideoCodec = _CH324CallActiveTxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 5),
    _CH324CallActiveTxVideoCodec_Type()
)
cH324CallActiveTxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveTxVideoCodec.setStatus("current")
_CH324CallActiveTxVideoPackets_Type = AbsoluteCounter32
_CH324CallActiveTxVideoPackets_Object = MibTableColumn
cH324CallActiveTxVideoPackets = _CH324CallActiveTxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 6),
    _CH324CallActiveTxVideoPackets_Type()
)
cH324CallActiveTxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveTxVideoPackets.setStatus("current")
_CH324CallActiveTxVideoBytes_Type = AbsoluteCounter32
_CH324CallActiveTxVideoBytes_Object = MibTableColumn
cH324CallActiveTxVideoBytes = _CH324CallActiveTxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 7),
    _CH324CallActiveTxVideoBytes_Type()
)
cH324CallActiveTxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveTxVideoBytes.setStatus("current")
_CH324CallActiveRxVideoCodec_Type = CvcVideoCoderRate
_CH324CallActiveRxVideoCodec_Object = MibTableColumn
cH324CallActiveRxVideoCodec = _CH324CallActiveRxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 8),
    _CH324CallActiveRxVideoCodec_Type()
)
cH324CallActiveRxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveRxVideoCodec.setStatus("current")
_CH324CallActiveRxVideoPackets_Type = AbsoluteCounter32
_CH324CallActiveRxVideoPackets_Object = MibTableColumn
cH324CallActiveRxVideoPackets = _CH324CallActiveRxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 9),
    _CH324CallActiveRxVideoPackets_Type()
)
cH324CallActiveRxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveRxVideoPackets.setStatus("current")
_CH324CallActiveRxVideoBytes_Type = AbsoluteCounter32
_CH324CallActiveRxVideoBytes_Object = MibTableColumn
cH324CallActiveRxVideoBytes = _CH324CallActiveRxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 1, 2, 1, 1, 10),
    _CH324CallActiveRxVideoBytes_Type()
)
cH324CallActiveRxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cH324CallActiveRxVideoBytes.setStatus("current")
_CiscoH324DialControlMIBConform_ObjectIdentity = ObjectIdentity
ciscoH324DialControlMIBConform = _CiscoH324DialControlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2)
)
_CiscoH324DialControlMIBConformance_ObjectIdentity = ObjectIdentity
ciscoH324DialControlMIBConformance = _CiscoH324DialControlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2, 1)
)
_CiscoH324DialControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoH324DialControlMIBCompliances = _CiscoH324DialControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2, 1, 1)
)
_CiscoH324DialControlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoH324DialControlMIBGroups = _CiscoH324DialControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2, 1, 2)
)

# Managed Objects groups

cH324CallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2, 1, 2, 1)
)
cH324CallHistoryGroup.setObjects(
      *(("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryConnectionId"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryIncomingConnectionId"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryH324CallType"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryUsedBandwidth"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryTxVideoCodec"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryTxVideoPackets"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryTxVideoBytes"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryRxVideoCodec"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryRxVideoPackets"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallHistoryRxVideoBytes"))
)
if mibBuilder.loadTexts:
    cH324CallHistoryGroup.setStatus("current")

cH324CallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2, 1, 2, 2)
)
cH324CallActiveGroup.setObjects(
      *(("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveConnectionId"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveIncomingConnectionId"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveH324CallType"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveUsedBandwidth"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveTxVideoCodec"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveTxVideoPackets"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveTxVideoBytes"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveRxVideoCodec"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveRxVideoPackets"),
        ("CISCO-H324-DIAL-CONTROL-MIB", "cH324CallActiveRxVideoBytes"))
)
if mibBuilder.loadTexts:
    cH324CallActiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoH324DialControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 621, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoH324DialControlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-H324-DIAL-CONTROL-MIB",
    **{"CH324CallType": CH324CallType,
       "ciscoH324DialControlMIB": ciscoH324DialControlMIB,
       "ciscoH324DialControlMIBObjects": ciscoH324DialControlMIBObjects,
       "cH324DialControlCallHistory": cH324DialControlCallHistory,
       "cH324CallHistoryTable": cH324CallHistoryTable,
       "cH324CallHistoryEntry": cH324CallHistoryEntry,
       "cH324CallHistoryConnectionId": cH324CallHistoryConnectionId,
       "cH324CallHistoryIncomingConnectionId": cH324CallHistoryIncomingConnectionId,
       "cH324CallHistoryH324CallType": cH324CallHistoryH324CallType,
       "cH324CallHistoryUsedBandwidth": cH324CallHistoryUsedBandwidth,
       "cH324CallHistoryTxVideoCodec": cH324CallHistoryTxVideoCodec,
       "cH324CallHistoryTxVideoPackets": cH324CallHistoryTxVideoPackets,
       "cH324CallHistoryTxVideoBytes": cH324CallHistoryTxVideoBytes,
       "cH324CallHistoryRxVideoCodec": cH324CallHistoryRxVideoCodec,
       "cH324CallHistoryRxVideoPackets": cH324CallHistoryRxVideoPackets,
       "cH324CallHistoryRxVideoBytes": cH324CallHistoryRxVideoBytes,
       "cH324DialControlCallActive": cH324DialControlCallActive,
       "cH324CallActiveTable": cH324CallActiveTable,
       "cH324CallActiveEntry": cH324CallActiveEntry,
       "cH324CallActiveConnectionId": cH324CallActiveConnectionId,
       "cH324CallActiveIncomingConnectionId": cH324CallActiveIncomingConnectionId,
       "cH324CallActiveH324CallType": cH324CallActiveH324CallType,
       "cH324CallActiveUsedBandwidth": cH324CallActiveUsedBandwidth,
       "cH324CallActiveTxVideoCodec": cH324CallActiveTxVideoCodec,
       "cH324CallActiveTxVideoPackets": cH324CallActiveTxVideoPackets,
       "cH324CallActiveTxVideoBytes": cH324CallActiveTxVideoBytes,
       "cH324CallActiveRxVideoCodec": cH324CallActiveRxVideoCodec,
       "cH324CallActiveRxVideoPackets": cH324CallActiveRxVideoPackets,
       "cH324CallActiveRxVideoBytes": cH324CallActiveRxVideoBytes,
       "ciscoH324DialControlMIBConform": ciscoH324DialControlMIBConform,
       "ciscoH324DialControlMIBConformance": ciscoH324DialControlMIBConformance,
       "ciscoH324DialControlMIBCompliances": ciscoH324DialControlMIBCompliances,
       "ciscoH324DialControlMIBCompliance": ciscoH324DialControlMIBCompliance,
       "ciscoH324DialControlMIBGroups": ciscoH324DialControlMIBGroups,
       "cH324CallHistoryGroup": cH324CallHistoryGroup,
       "cH324CallActiveGroup": cH324CallActiveGroup}
)
