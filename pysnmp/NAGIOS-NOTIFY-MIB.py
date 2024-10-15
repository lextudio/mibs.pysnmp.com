# SNMP MIB module (NAGIOS-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NAGIOS-NOTIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:36 2024
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

(HostStateID,
 HostStateType,
 NotifyType,
 ServiceStateID,
 nagios) = mibBuilder.importSymbols(
    "NAGIOS-ROOT-MIB",
    "HostStateID",
    "HostStateType",
    "NotifyType",
    "ServiceStateID",
    "nagios")

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

nagiosNotify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20006, 1)
)
nagiosNotify.setRevisions(
        ("2005-03-09 00:00",
         "2005-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NagiosHostEventTable_Object = MibTable
nagiosHostEventTable = _NagiosHostEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1)
)
if mibBuilder.loadTexts:
    nagiosHostEventTable.setStatus("current")
_NagiosHostEventEntry_Object = MibTableRow
nagiosHostEventEntry = _NagiosHostEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1)
)
nagiosHostEventEntry.setIndexNames(
    (0, "NAGIOS-NOTIFY-MIB", "nHostEventIndex"),
)
if mibBuilder.loadTexts:
    nagiosHostEventEntry.setStatus("current")


class _NHostEventIndex_Type(Integer32):
    """Custom type nHostEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NHostEventIndex_Type.__name__ = "Integer32"
_NHostEventIndex_Object = MibTableColumn
nHostEventIndex = _NHostEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 1),
    _NHostEventIndex_Type()
)
nHostEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nHostEventIndex.setStatus("current")
_NHostname_Type = OctetString
_NHostname_Object = MibTableColumn
nHostname = _NHostname_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 2),
    _NHostname_Type()
)
nHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostname.setStatus("current")
_NHostAlias_Type = OctetString
_NHostAlias_Object = MibTableColumn
nHostAlias = _NHostAlias_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 3),
    _NHostAlias_Type()
)
nHostAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostAlias.setStatus("current")
_NHostStateID_Type = HostStateID
_NHostStateID_Object = MibTableColumn
nHostStateID = _NHostStateID_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 4),
    _NHostStateID_Type()
)
nHostStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostStateID.setStatus("current")
_NHostStateType_Type = HostStateType
_NHostStateType_Object = MibTableColumn
nHostStateType = _NHostStateType_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 5),
    _NHostStateType_Type()
)
nHostStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostStateType.setStatus("current")
_NHostAttempt_Type = Integer32
_NHostAttempt_Object = MibTableColumn
nHostAttempt = _NHostAttempt_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 6),
    _NHostAttempt_Type()
)
nHostAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostAttempt.setStatus("current")
_NHostDurationSec_Type = Integer32
_NHostDurationSec_Object = MibTableColumn
nHostDurationSec = _NHostDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 7),
    _NHostDurationSec_Type()
)
nHostDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostDurationSec.setStatus("current")
_NHostGroupName_Type = OctetString
_NHostGroupName_Object = MibTableColumn
nHostGroupName = _NHostGroupName_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 8),
    _NHostGroupName_Type()
)
nHostGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostGroupName.setStatus("current")
_NHostLastCheck_Type = Integer32
_NHostLastCheck_Object = MibTableColumn
nHostLastCheck = _NHostLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 9),
    _NHostLastCheck_Type()
)
nHostLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostLastCheck.setStatus("current")
_NHostLastChange_Type = Integer32
_NHostLastChange_Object = MibTableColumn
nHostLastChange = _NHostLastChange_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 10),
    _NHostLastChange_Type()
)
nHostLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostLastChange.setStatus("current")
_NHostLastUp_Type = Integer32
_NHostLastUp_Object = MibTableColumn
nHostLastUp = _NHostLastUp_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 11),
    _NHostLastUp_Type()
)
nHostLastUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostLastUp.setStatus("current")
_NHostLastDown_Type = Integer32
_NHostLastDown_Object = MibTableColumn
nHostLastDown = _NHostLastDown_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 12),
    _NHostLastDown_Type()
)
nHostLastDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostLastDown.setStatus("current")
_NHostLastUnreachable_Type = Integer32
_NHostLastUnreachable_Object = MibTableColumn
nHostLastUnreachable = _NHostLastUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 13),
    _NHostLastUnreachable_Type()
)
nHostLastUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostLastUnreachable.setStatus("current")
_NHostOutput_Type = OctetString
_NHostOutput_Object = MibTableColumn
nHostOutput = _NHostOutput_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 14),
    _NHostOutput_Type()
)
nHostOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostOutput.setStatus("current")
_NHostPerfData_Type = OctetString
_NHostPerfData_Object = MibTableColumn
nHostPerfData = _NHostPerfData_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 1, 1, 15),
    _NHostPerfData_Type()
)
nHostPerfData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostPerfData.setStatus("current")
_NagiosHostNotifyTable_Object = MibTable
nagiosHostNotifyTable = _NagiosHostNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 2)
)
if mibBuilder.loadTexts:
    nagiosHostNotifyTable.setStatus("current")
_NagiosHostNotifyEntry_Object = MibTableRow
nagiosHostNotifyEntry = _NagiosHostNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 2, 1)
)
nagiosHostNotifyEntry.setIndexNames(
    (0, "NAGIOS-NOTIFY-MIB", "nHostEventIndex"),
)
if mibBuilder.loadTexts:
    nagiosHostNotifyEntry.setStatus("current")
_NHostNotifyType_Type = NotifyType
_NHostNotifyType_Object = MibTableColumn
nHostNotifyType = _NHostNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 2, 1, 1),
    _NHostNotifyType_Type()
)
nHostNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostNotifyType.setStatus("current")
_NHostNotifyNum_Type = Gauge32
_NHostNotifyNum_Object = MibTableColumn
nHostNotifyNum = _NHostNotifyNum_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 2, 1, 2),
    _NHostNotifyNum_Type()
)
nHostNotifyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostNotifyNum.setStatus("current")
_NHostAckAuthor_Type = OctetString
_NHostAckAuthor_Object = MibTableColumn
nHostAckAuthor = _NHostAckAuthor_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 2, 1, 3),
    _NHostAckAuthor_Type()
)
nHostAckAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostAckAuthor.setStatus("current")
_NHostAckComment_Type = OctetString
_NHostAckComment_Object = MibTableColumn
nHostAckComment = _NHostAckComment_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 2, 1, 4),
    _NHostAckComment_Type()
)
nHostAckComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nHostAckComment.setStatus("current")
_NagiosSvcEventTable_Object = MibTable
nagiosSvcEventTable = _NagiosSvcEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3)
)
if mibBuilder.loadTexts:
    nagiosSvcEventTable.setStatus("current")
_NagiosSvcEventEntry_Object = MibTableRow
nagiosSvcEventEntry = _NagiosSvcEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1)
)
nagiosSvcEventEntry.setIndexNames(
    (0, "NAGIOS-NOTIFY-MIB", "nSvcEventIndex"),
)
if mibBuilder.loadTexts:
    nagiosSvcEventEntry.setStatus("current")


class _NSvcEventIndex_Type(Integer32):
    """Custom type nSvcEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NSvcEventIndex_Type.__name__ = "Integer32"
_NSvcEventIndex_Object = MibTableColumn
nSvcEventIndex = _NSvcEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 1),
    _NSvcEventIndex_Type()
)
nSvcEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nSvcEventIndex.setStatus("current")
_NSvcHostname_Type = OctetString
_NSvcHostname_Object = MibTableColumn
nSvcHostname = _NSvcHostname_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 2),
    _NSvcHostname_Type()
)
nSvcHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcHostname.setStatus("current")
_NSvcHostAlias_Type = OctetString
_NSvcHostAlias_Object = MibTableColumn
nSvcHostAlias = _NSvcHostAlias_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 3),
    _NSvcHostAlias_Type()
)
nSvcHostAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcHostAlias.setStatus("current")
_NSvcHostStateID_Type = HostStateID
_NSvcHostStateID_Object = MibTableColumn
nSvcHostStateID = _NSvcHostStateID_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 4),
    _NSvcHostStateID_Type()
)
nSvcHostStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcHostStateID.setStatus("current")
_NSvcHostStateType_Type = HostStateType
_NSvcHostStateType_Object = MibTableColumn
nSvcHostStateType = _NSvcHostStateType_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 5),
    _NSvcHostStateType_Type()
)
nSvcHostStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcHostStateType.setStatus("current")
_NSvcDesc_Type = OctetString
_NSvcDesc_Object = MibTableColumn
nSvcDesc = _NSvcDesc_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 6),
    _NSvcDesc_Type()
)
nSvcDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcDesc.setStatus("current")
_NSvcStateID_Type = ServiceStateID
_NSvcStateID_Object = MibTableColumn
nSvcStateID = _NSvcStateID_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 7),
    _NSvcStateID_Type()
)
nSvcStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcStateID.setStatus("current")
_NSvcAttempt_Type = Integer32
_NSvcAttempt_Object = MibTableColumn
nSvcAttempt = _NSvcAttempt_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 8),
    _NSvcAttempt_Type()
)
nSvcAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcAttempt.setStatus("current")
_NSvcDurationSec_Type = Integer32
_NSvcDurationSec_Object = MibTableColumn
nSvcDurationSec = _NSvcDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 9),
    _NSvcDurationSec_Type()
)
nSvcDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcDurationSec.setStatus("current")
_NSvcGroupName_Type = OctetString
_NSvcGroupName_Object = MibTableColumn
nSvcGroupName = _NSvcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 10),
    _NSvcGroupName_Type()
)
nSvcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcGroupName.setStatus("current")
_NSvcLastCheck_Type = Integer32
_NSvcLastCheck_Object = MibTableColumn
nSvcLastCheck = _NSvcLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 11),
    _NSvcLastCheck_Type()
)
nSvcLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcLastCheck.setStatus("current")
_NSvcLastChange_Type = Integer32
_NSvcLastChange_Object = MibTableColumn
nSvcLastChange = _NSvcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 12),
    _NSvcLastChange_Type()
)
nSvcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcLastChange.setStatus("current")
_NSvcLastOK_Type = Integer32
_NSvcLastOK_Object = MibTableColumn
nSvcLastOK = _NSvcLastOK_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 13),
    _NSvcLastOK_Type()
)
nSvcLastOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcLastOK.setStatus("current")
_NSvcLastWarn_Type = Integer32
_NSvcLastWarn_Object = MibTableColumn
nSvcLastWarn = _NSvcLastWarn_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 14),
    _NSvcLastWarn_Type()
)
nSvcLastWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcLastWarn.setStatus("current")
_NSvcLastCrit_Type = Integer32
_NSvcLastCrit_Object = MibTableColumn
nSvcLastCrit = _NSvcLastCrit_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 15),
    _NSvcLastCrit_Type()
)
nSvcLastCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcLastCrit.setStatus("current")
_NSvcLastUnkn_Type = Integer32
_NSvcLastUnkn_Object = MibTableColumn
nSvcLastUnkn = _NSvcLastUnkn_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 16),
    _NSvcLastUnkn_Type()
)
nSvcLastUnkn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcLastUnkn.setStatus("current")
_NSvcOutput_Type = OctetString
_NSvcOutput_Object = MibTableColumn
nSvcOutput = _NSvcOutput_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 17),
    _NSvcOutput_Type()
)
nSvcOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcOutput.setStatus("current")
_NSvcPerfData_Type = OctetString
_NSvcPerfData_Object = MibTableColumn
nSvcPerfData = _NSvcPerfData_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 3, 1, 18),
    _NSvcPerfData_Type()
)
nSvcPerfData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcPerfData.setStatus("current")
_NagiosSvcNotifyTable_Object = MibTable
nagiosSvcNotifyTable = _NagiosSvcNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 4)
)
if mibBuilder.loadTexts:
    nagiosSvcNotifyTable.setStatus("current")
_NagiosSvcNotifyEntry_Object = MibTableRow
nagiosSvcNotifyEntry = _NagiosSvcNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 4, 1)
)
nagiosSvcNotifyEntry.setIndexNames(
    (0, "NAGIOS-NOTIFY-MIB", "nSvcEventIndex"),
)
if mibBuilder.loadTexts:
    nagiosSvcNotifyEntry.setStatus("current")
_NSvcNotifyType_Type = NotifyType
_NSvcNotifyType_Object = MibTableColumn
nSvcNotifyType = _NSvcNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 4, 1, 1),
    _NSvcNotifyType_Type()
)
nSvcNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcNotifyType.setStatus("current")
_NSvcNotifyNum_Type = Gauge32
_NSvcNotifyNum_Object = MibTableColumn
nSvcNotifyNum = _NSvcNotifyNum_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 4, 1, 2),
    _NSvcNotifyNum_Type()
)
nSvcNotifyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcNotifyNum.setStatus("current")
_NSvcAckAuthor_Type = OctetString
_NSvcAckAuthor_Object = MibTableColumn
nSvcAckAuthor = _NSvcAckAuthor_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 4, 1, 3),
    _NSvcAckAuthor_Type()
)
nSvcAckAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcAckAuthor.setStatus("current")
_NSvcAckComment_Type = OctetString
_NSvcAckComment_Object = MibTableColumn
nSvcAckComment = _NSvcAckComment_Object(
    (1, 3, 6, 1, 4, 1, 20006, 1, 4, 1, 4),
    _NSvcAckComment_Type()
)
nSvcAckComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSvcAckComment.setStatus("current")

# Managed Objects groups


# Notification objects

nHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 20006, 1, 5)
)
nHostEvent.setObjects(
      *(("NAGIOS-NOTIFY-MIB", "nHostname"),
        ("NAGIOS-NOTIFY-MIB", "nHostStateID"),
        ("NAGIOS-NOTIFY-MIB", "nHostStateType"),
        ("NAGIOS-NOTIFY-MIB", "nHostAttempt"),
        ("NAGIOS-NOTIFY-MIB", "nHostDurationSec"),
        ("NAGIOS-NOTIFY-MIB", "nHostGroupName"),
        ("NAGIOS-NOTIFY-MIB", "nHostLastCheck"),
        ("NAGIOS-NOTIFY-MIB", "nHostLastChange"),
        ("NAGIOS-NOTIFY-MIB", "nHostOutput"))
)
if mibBuilder.loadTexts:
    nHostEvent.setStatus(
        "current"
    )

nHostNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 20006, 1, 6)
)
nHostNotify.setObjects(
      *(("NAGIOS-NOTIFY-MIB", "nHostNotifyType"),
        ("NAGIOS-NOTIFY-MIB", "nHostNotifyNum"),
        ("NAGIOS-NOTIFY-MIB", "nHostAckAuthor"),
        ("NAGIOS-NOTIFY-MIB", "nHostAckComment"),
        ("NAGIOS-NOTIFY-MIB", "nHostname"),
        ("NAGIOS-NOTIFY-MIB", "nHostStateID"),
        ("NAGIOS-NOTIFY-MIB", "nHostStateType"),
        ("NAGIOS-NOTIFY-MIB", "nHostAttempt"),
        ("NAGIOS-NOTIFY-MIB", "nHostDurationSec"),
        ("NAGIOS-NOTIFY-MIB", "nHostGroupName"),
        ("NAGIOS-NOTIFY-MIB", "nHostLastCheck"),
        ("NAGIOS-NOTIFY-MIB", "nHostLastChange"),
        ("NAGIOS-NOTIFY-MIB", "nHostOutput"))
)
if mibBuilder.loadTexts:
    nHostNotify.setStatus(
        "current"
    )

nSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 20006, 1, 7)
)
nSvcEvent.setObjects(
      *(("NAGIOS-NOTIFY-MIB", "nHostname"),
        ("NAGIOS-NOTIFY-MIB", "nHostStateID"),
        ("NAGIOS-NOTIFY-MIB", "nSvcDesc"),
        ("NAGIOS-NOTIFY-MIB", "nSvcStateID"),
        ("NAGIOS-NOTIFY-MIB", "nSvcAttempt"),
        ("NAGIOS-NOTIFY-MIB", "nSvcDurationSec"),
        ("NAGIOS-NOTIFY-MIB", "nSvcGroupName"),
        ("NAGIOS-NOTIFY-MIB", "nSvcLastCheck"),
        ("NAGIOS-NOTIFY-MIB", "nSvcLastChange"),
        ("NAGIOS-NOTIFY-MIB", "nSvcOutput"))
)
if mibBuilder.loadTexts:
    nSvcEvent.setStatus(
        "current"
    )

nSvcNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 20006, 1, 8)
)
nSvcNotify.setObjects(
      *(("NAGIOS-NOTIFY-MIB", "nSvcNotifyType"),
        ("NAGIOS-NOTIFY-MIB", "nSvcNotifyNum"),
        ("NAGIOS-NOTIFY-MIB", "nSvcAckAuthor"),
        ("NAGIOS-NOTIFY-MIB", "nSvcAckComment"),
        ("NAGIOS-NOTIFY-MIB", "nHostname"),
        ("NAGIOS-NOTIFY-MIB", "nHostStateID"),
        ("NAGIOS-NOTIFY-MIB", "nSvcDesc"),
        ("NAGIOS-NOTIFY-MIB", "nSvcStateID"),
        ("NAGIOS-NOTIFY-MIB", "nSvcAttempt"),
        ("NAGIOS-NOTIFY-MIB", "nSvcDurationSec"),
        ("NAGIOS-NOTIFY-MIB", "nSvcGroupName"),
        ("NAGIOS-NOTIFY-MIB", "nSvcLastCheck"),
        ("NAGIOS-NOTIFY-MIB", "nSvcLastChange"),
        ("NAGIOS-NOTIFY-MIB", "nSvcOutput"))
)
if mibBuilder.loadTexts:
    nSvcNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NAGIOS-NOTIFY-MIB",
    **{"nagiosNotify": nagiosNotify,
       "nagiosHostEventTable": nagiosHostEventTable,
       "nagiosHostEventEntry": nagiosHostEventEntry,
       "nHostEventIndex": nHostEventIndex,
       "nHostname": nHostname,
       "nHostAlias": nHostAlias,
       "nHostStateID": nHostStateID,
       "nHostStateType": nHostStateType,
       "nHostAttempt": nHostAttempt,
       "nHostDurationSec": nHostDurationSec,
       "nHostGroupName": nHostGroupName,
       "nHostLastCheck": nHostLastCheck,
       "nHostLastChange": nHostLastChange,
       "nHostLastUp": nHostLastUp,
       "nHostLastDown": nHostLastDown,
       "nHostLastUnreachable": nHostLastUnreachable,
       "nHostOutput": nHostOutput,
       "nHostPerfData": nHostPerfData,
       "nagiosHostNotifyTable": nagiosHostNotifyTable,
       "nagiosHostNotifyEntry": nagiosHostNotifyEntry,
       "nHostNotifyType": nHostNotifyType,
       "nHostNotifyNum": nHostNotifyNum,
       "nHostAckAuthor": nHostAckAuthor,
       "nHostAckComment": nHostAckComment,
       "nagiosSvcEventTable": nagiosSvcEventTable,
       "nagiosSvcEventEntry": nagiosSvcEventEntry,
       "nSvcEventIndex": nSvcEventIndex,
       "nSvcHostname": nSvcHostname,
       "nSvcHostAlias": nSvcHostAlias,
       "nSvcHostStateID": nSvcHostStateID,
       "nSvcHostStateType": nSvcHostStateType,
       "nSvcDesc": nSvcDesc,
       "nSvcStateID": nSvcStateID,
       "nSvcAttempt": nSvcAttempt,
       "nSvcDurationSec": nSvcDurationSec,
       "nSvcGroupName": nSvcGroupName,
       "nSvcLastCheck": nSvcLastCheck,
       "nSvcLastChange": nSvcLastChange,
       "nSvcLastOK": nSvcLastOK,
       "nSvcLastWarn": nSvcLastWarn,
       "nSvcLastCrit": nSvcLastCrit,
       "nSvcLastUnkn": nSvcLastUnkn,
       "nSvcOutput": nSvcOutput,
       "nSvcPerfData": nSvcPerfData,
       "nagiosSvcNotifyTable": nagiosSvcNotifyTable,
       "nagiosSvcNotifyEntry": nagiosSvcNotifyEntry,
       "nSvcNotifyType": nSvcNotifyType,
       "nSvcNotifyNum": nSvcNotifyNum,
       "nSvcAckAuthor": nSvcAckAuthor,
       "nSvcAckComment": nSvcAckComment,
       "nHostEvent": nHostEvent,
       "nHostNotify": nHostNotify,
       "nSvcEvent": nSvcEvent,
       "nSvcNotify": nSvcNotify}
)
