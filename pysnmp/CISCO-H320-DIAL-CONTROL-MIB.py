# SNMP MIB module (CISCO-H320-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-H320-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:07 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CvcGUid,
 CvcH320CallType,
 CvcVideoCoderRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcGUid",
    "CvcH320CallType",
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

ciscoH320DialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128)
)
ciscoH320DialControlMIB.setRevisions(
        ("2006-02-23 00:00",
         "2005-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoH320DialControlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoH320DialControlMIBNotifs = _CiscoH320DialControlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 0)
)
_CiscoH320DialControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoH320DialControlMIBObjects = _CiscoH320DialControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1)
)
_CvH320CallHistory_ObjectIdentity = ObjectIdentity
cvH320CallHistory = _CvH320CallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1)
)
_CvH320CallHistoryTable_Object = MibTable
cvH320CallHistoryTable = _CvH320CallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvH320CallHistoryTable.setStatus("current")
_CvH320CallHistoryEntry_Object = MibTableRow
cvH320CallHistoryEntry = _CvH320CallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1)
)
cvH320CallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvH320CallHistoryEntry.setStatus("current")
_CvH320CallHistoryConnectionId_Type = CvcGUid
_CvH320CallHistoryConnectionId_Object = MibTableColumn
cvH320CallHistoryConnectionId = _CvH320CallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 1),
    _CvH320CallHistoryConnectionId_Type()
)
cvH320CallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryConnectionId.setStatus("current")
_CvH320CallHistoryIncomingConnectionId_Type = CvcGUid
_CvH320CallHistoryIncomingConnectionId_Object = MibTableColumn
cvH320CallHistoryIncomingConnectionId = _CvH320CallHistoryIncomingConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 2),
    _CvH320CallHistoryIncomingConnectionId_Type()
)
cvH320CallHistoryIncomingConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryIncomingConnectionId.setStatus("current")
_CvH320CallHistoryH320CallType_Type = CvcH320CallType
_CvH320CallHistoryH320CallType_Object = MibTableColumn
cvH320CallHistoryH320CallType = _CvH320CallHistoryH320CallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 3),
    _CvH320CallHistoryH320CallType_Type()
)
cvH320CallHistoryH320CallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryH320CallType.setStatus("current")


class _CvH320CallHistoryUsedBandwidth_Type(Integer32):
    """Custom type cvH320CallHistoryUsedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CvH320CallHistoryUsedBandwidth_Type.__name__ = "Integer32"
_CvH320CallHistoryUsedBandwidth_Object = MibTableColumn
cvH320CallHistoryUsedBandwidth = _CvH320CallHistoryUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 4),
    _CvH320CallHistoryUsedBandwidth_Type()
)
cvH320CallHistoryUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryUsedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cvH320CallHistoryUsedBandwidth.setUnits("kilobits per second")
_CvH320CallHistoryTxVideoCodec_Type = CvcVideoCoderRate
_CvH320CallHistoryTxVideoCodec_Object = MibTableColumn
cvH320CallHistoryTxVideoCodec = _CvH320CallHistoryTxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 5),
    _CvH320CallHistoryTxVideoCodec_Type()
)
cvH320CallHistoryTxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryTxVideoCodec.setStatus("current")
_CvH320CallHistoryTxVideoPackets_Type = AbsoluteCounter32
_CvH320CallHistoryTxVideoPackets_Object = MibTableColumn
cvH320CallHistoryTxVideoPackets = _CvH320CallHistoryTxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 6),
    _CvH320CallHistoryTxVideoPackets_Type()
)
cvH320CallHistoryTxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryTxVideoPackets.setStatus("current")
_CvH320CallHistoryTxVideoBytes_Type = AbsoluteCounter32
_CvH320CallHistoryTxVideoBytes_Object = MibTableColumn
cvH320CallHistoryTxVideoBytes = _CvH320CallHistoryTxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 7),
    _CvH320CallHistoryTxVideoBytes_Type()
)
cvH320CallHistoryTxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryTxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cvH320CallHistoryTxVideoBytes.setUnits("bytes")
_CvH320CallHistoryRxVideoCodec_Type = CvcVideoCoderRate
_CvH320CallHistoryRxVideoCodec_Object = MibTableColumn
cvH320CallHistoryRxVideoCodec = _CvH320CallHistoryRxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 8),
    _CvH320CallHistoryRxVideoCodec_Type()
)
cvH320CallHistoryRxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryRxVideoCodec.setStatus("current")
_CvH320CallHistoryRxVideoPackets_Type = AbsoluteCounter32
_CvH320CallHistoryRxVideoPackets_Object = MibTableColumn
cvH320CallHistoryRxVideoPackets = _CvH320CallHistoryRxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 9),
    _CvH320CallHistoryRxVideoPackets_Type()
)
cvH320CallHistoryRxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryRxVideoPackets.setStatus("current")
_CvH320CallHistoryRxVideoBytes_Type = AbsoluteCounter32
_CvH320CallHistoryRxVideoBytes_Object = MibTableColumn
cvH320CallHistoryRxVideoBytes = _CvH320CallHistoryRxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 1, 1, 1, 10),
    _CvH320CallHistoryRxVideoBytes_Type()
)
cvH320CallHistoryRxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallHistoryRxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cvH320CallHistoryRxVideoBytes.setUnits("bytes")
_CvH320CallActive_ObjectIdentity = ObjectIdentity
cvH320CallActive = _CvH320CallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2)
)
_CvH320CallActiveTable_Object = MibTable
cvH320CallActiveTable = _CvH320CallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvH320CallActiveTable.setStatus("current")
_CvH320CallActiveEntry_Object = MibTableRow
cvH320CallActiveEntry = _CvH320CallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1)
)
cvH320CallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cvH320CallActiveEntry.setStatus("current")
_CvH320CallActiveConnectionId_Type = CvcGUid
_CvH320CallActiveConnectionId_Object = MibTableColumn
cvH320CallActiveConnectionId = _CvH320CallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 1),
    _CvH320CallActiveConnectionId_Type()
)
cvH320CallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveConnectionId.setStatus("current")
_CvH320CallActiveIncomingConnectionId_Type = CvcGUid
_CvH320CallActiveIncomingConnectionId_Object = MibTableColumn
cvH320CallActiveIncomingConnectionId = _CvH320CallActiveIncomingConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 2),
    _CvH320CallActiveIncomingConnectionId_Type()
)
cvH320CallActiveIncomingConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveIncomingConnectionId.setStatus("current")
_CvH320CallActiveH320CallType_Type = CvcH320CallType
_CvH320CallActiveH320CallType_Object = MibTableColumn
cvH320CallActiveH320CallType = _CvH320CallActiveH320CallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 3),
    _CvH320CallActiveH320CallType_Type()
)
cvH320CallActiveH320CallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveH320CallType.setStatus("current")


class _CvH320CallActiveUsedBandwidth_Type(Integer32):
    """Custom type cvH320CallActiveUsedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CvH320CallActiveUsedBandwidth_Type.__name__ = "Integer32"
_CvH320CallActiveUsedBandwidth_Object = MibTableColumn
cvH320CallActiveUsedBandwidth = _CvH320CallActiveUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 4),
    _CvH320CallActiveUsedBandwidth_Type()
)
cvH320CallActiveUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveUsedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cvH320CallActiveUsedBandwidth.setUnits("kilobits per second")
_CvH320CallActiveTxVideoCodec_Type = CvcVideoCoderRate
_CvH320CallActiveTxVideoCodec_Object = MibTableColumn
cvH320CallActiveTxVideoCodec = _CvH320CallActiveTxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 5),
    _CvH320CallActiveTxVideoCodec_Type()
)
cvH320CallActiveTxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveTxVideoCodec.setStatus("current")
_CvH320CallActiveTxVideoPackets_Type = AbsoluteCounter32
_CvH320CallActiveTxVideoPackets_Object = MibTableColumn
cvH320CallActiveTxVideoPackets = _CvH320CallActiveTxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 6),
    _CvH320CallActiveTxVideoPackets_Type()
)
cvH320CallActiveTxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveTxVideoPackets.setStatus("current")
_CvH320CallActiveTxVideoBytes_Type = AbsoluteCounter32
_CvH320CallActiveTxVideoBytes_Object = MibTableColumn
cvH320CallActiveTxVideoBytes = _CvH320CallActiveTxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 7),
    _CvH320CallActiveTxVideoBytes_Type()
)
cvH320CallActiveTxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveTxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cvH320CallActiveTxVideoBytes.setUnits("bytes")
_CvH320CallActiveRxVideoCodec_Type = CvcVideoCoderRate
_CvH320CallActiveRxVideoCodec_Object = MibTableColumn
cvH320CallActiveRxVideoCodec = _CvH320CallActiveRxVideoCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 8),
    _CvH320CallActiveRxVideoCodec_Type()
)
cvH320CallActiveRxVideoCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveRxVideoCodec.setStatus("current")
_CvH320CallActiveRxVideoPackets_Type = AbsoluteCounter32
_CvH320CallActiveRxVideoPackets_Object = MibTableColumn
cvH320CallActiveRxVideoPackets = _CvH320CallActiveRxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 9),
    _CvH320CallActiveRxVideoPackets_Type()
)
cvH320CallActiveRxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveRxVideoPackets.setStatus("current")
_CvH320CallActiveRxVideoBytes_Type = AbsoluteCounter32
_CvH320CallActiveRxVideoBytes_Object = MibTableColumn
cvH320CallActiveRxVideoBytes = _CvH320CallActiveRxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 1, 2, 1, 1, 10),
    _CvH320CallActiveRxVideoBytes_Type()
)
cvH320CallActiveRxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvH320CallActiveRxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cvH320CallActiveRxVideoBytes.setUnits("bytes")
_CiscoH320DialControlMIBConform_ObjectIdentity = ObjectIdentity
ciscoH320DialControlMIBConform = _CiscoH320DialControlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2)
)
_CiscoH320DialControlMIBConformance_ObjectIdentity = ObjectIdentity
ciscoH320DialControlMIBConformance = _CiscoH320DialControlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2, 1)
)
_CiscoH320DialControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoH320DialControlMIBCompliances = _CiscoH320DialControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2, 1, 1)
)
_CiscoH320DialControlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoH320DialControlMIBGroups = _CiscoH320DialControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2, 1, 2)
)

# Managed Objects groups

cvH320CallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2, 1, 2, 1)
)
cvH320CallHistoryGroup.setObjects(
      *(("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryConnectionId"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryIncomingConnectionId"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryH320CallType"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryUsedBandwidth"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryTxVideoCodec"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryTxVideoPackets"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryTxVideoBytes"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryRxVideoCodec"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryRxVideoPackets"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallHistoryRxVideoBytes"))
)
if mibBuilder.loadTexts:
    cvH320CallHistoryGroup.setStatus("current")

cvH320CallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2, 1, 2, 2)
)
cvH320CallActiveGroup.setObjects(
      *(("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveConnectionId"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveIncomingConnectionId"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveH320CallType"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveUsedBandwidth"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveTxVideoCodec"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveTxVideoPackets"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveTxVideoBytes"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveRxVideoCodec"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveRxVideoPackets"),
        ("CISCO-H320-DIAL-CONTROL-MIB", "cvH320CallActiveRxVideoBytes"))
)
if mibBuilder.loadTexts:
    cvH320CallActiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoH320DialControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 128, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoH320DialControlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-H320-DIAL-CONTROL-MIB",
    **{"ciscoH320DialControlMIB": ciscoH320DialControlMIB,
       "ciscoH320DialControlMIBNotifs": ciscoH320DialControlMIBNotifs,
       "ciscoH320DialControlMIBObjects": ciscoH320DialControlMIBObjects,
       "cvH320CallHistory": cvH320CallHistory,
       "cvH320CallHistoryTable": cvH320CallHistoryTable,
       "cvH320CallHistoryEntry": cvH320CallHistoryEntry,
       "cvH320CallHistoryConnectionId": cvH320CallHistoryConnectionId,
       "cvH320CallHistoryIncomingConnectionId": cvH320CallHistoryIncomingConnectionId,
       "cvH320CallHistoryH320CallType": cvH320CallHistoryH320CallType,
       "cvH320CallHistoryUsedBandwidth": cvH320CallHistoryUsedBandwidth,
       "cvH320CallHistoryTxVideoCodec": cvH320CallHistoryTxVideoCodec,
       "cvH320CallHistoryTxVideoPackets": cvH320CallHistoryTxVideoPackets,
       "cvH320CallHistoryTxVideoBytes": cvH320CallHistoryTxVideoBytes,
       "cvH320CallHistoryRxVideoCodec": cvH320CallHistoryRxVideoCodec,
       "cvH320CallHistoryRxVideoPackets": cvH320CallHistoryRxVideoPackets,
       "cvH320CallHistoryRxVideoBytes": cvH320CallHistoryRxVideoBytes,
       "cvH320CallActive": cvH320CallActive,
       "cvH320CallActiveTable": cvH320CallActiveTable,
       "cvH320CallActiveEntry": cvH320CallActiveEntry,
       "cvH320CallActiveConnectionId": cvH320CallActiveConnectionId,
       "cvH320CallActiveIncomingConnectionId": cvH320CallActiveIncomingConnectionId,
       "cvH320CallActiveH320CallType": cvH320CallActiveH320CallType,
       "cvH320CallActiveUsedBandwidth": cvH320CallActiveUsedBandwidth,
       "cvH320CallActiveTxVideoCodec": cvH320CallActiveTxVideoCodec,
       "cvH320CallActiveTxVideoPackets": cvH320CallActiveTxVideoPackets,
       "cvH320CallActiveTxVideoBytes": cvH320CallActiveTxVideoBytes,
       "cvH320CallActiveRxVideoCodec": cvH320CallActiveRxVideoCodec,
       "cvH320CallActiveRxVideoPackets": cvH320CallActiveRxVideoPackets,
       "cvH320CallActiveRxVideoBytes": cvH320CallActiveRxVideoBytes,
       "ciscoH320DialControlMIBConform": ciscoH320DialControlMIBConform,
       "ciscoH320DialControlMIBConformance": ciscoH320DialControlMIBConformance,
       "ciscoH320DialControlMIBCompliances": ciscoH320DialControlMIBCompliances,
       "ciscoH320DialControlMIBCompliance": ciscoH320DialControlMIBCompliance,
       "ciscoH320DialControlMIBGroups": ciscoH320DialControlMIBGroups,
       "cvH320CallHistoryGroup": cvH320CallHistoryGroup,
       "cvH320CallActiveGroup": cvH320CallActiveGroup}
)
