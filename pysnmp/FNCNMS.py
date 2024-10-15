# SNMP MIB module (FNCNMS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNCNMS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:16 2024
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

(netsmart,) = mibBuilder.importSymbols(
    "FNC-COMMON-SMI",
    "netsmart")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(system,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "system")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netsmart1500 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500)
)
netsmart1500.setRevisions(
        ("2012-02-06 16:00",
         "2011-06-16 16:00",
         "2003-08-02 16:00")
)


# Types definitions



class NMSMgdNE(DisplayString):
    """Custom type NMSMgdNE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )




# TEXTUAL-CONVENTIONS



class NMSSeverity(Integer32, TextualConvention):
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
        *(("cleared", 1),
          ("critical", 5),
          ("info", 2),
          ("major", 4),
          ("minor", 3))
    )



class NMSCondDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("receive", 3),
          ("transmit", 2))
    )



class NMSCondLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("farEnd", 3),
          ("na", 1),
          ("nearEnd", 2))
    )



class NMSServiceEffect(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("nonServiceAffecting", 3),
          ("serviceAffecting", 2))
    )



class NMSTrapSeqNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )



class NMSNEConnState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NmsNEMgmtMIB_ObjectIdentity = ObjectIdentity
nmsNEMgmtMIB = _NmsNEMgmtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1)
)
_NmsNEMgmt_ObjectIdentity = ObjectIdentity
nmsNEMgmt = _NmsNEMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 1)
)
_NmsNETable_Object = MibTable
nmsNETable = _NmsNETable_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nmsNETable.setStatus("current")
_NmsNEEntry_Object = MibTableRow
nmsNEEntry = _NmsNEEntry_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 1, 1, 1)
)
nmsNEEntry.setIndexNames(
    (1, "FNCNMS", "neTID"),
)
if mibBuilder.loadTexts:
    nmsNEEntry.setStatus("current")
_NeTID_Type = NMSMgdNE
_NeTID_Object = MibTableColumn
neTID = _NeTID_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 1, 1, 1, 1),
    _NeTID_Type()
)
neTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTID.setStatus("current")
_NeType_Type = OctetString
_NeType_Object = MibTableColumn
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 1, 1, 1, 2),
    _NeType_Type()
)
neType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neType.setStatus("current")
_NeConnState_Type = NMSNEConnState
_NeConnState_Object = MibTableColumn
neConnState = _NeConnState_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 1, 1, 1, 3),
    _NeConnState_Type()
)
neConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neConnState.setStatus("current")
_NmsNEAlarm_ObjectIdentity = ObjectIdentity
nmsNEAlarm = _NmsNEAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2)
)
_NmsNotificationTrapBase_ObjectIdentity = ObjectIdentity
nmsNotificationTrapBase = _NmsNotificationTrapBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 0)
)
_NmsNEAlarmTable_Object = MibTable
nmsNEAlarmTable = _NmsNEAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nmsNEAlarmTable.setStatus("current")
_NmsNEAlarmListEntry_Object = MibTableRow
nmsNEAlarmListEntry = _NmsNEAlarmListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1)
)
nmsNEAlarmListEntry.setIndexNames(
    (0, "FNCNMS", "alarmTID"),
    (0, "FNCNMS", "alarmIndex"),
)
if mibBuilder.loadTexts:
    nmsNEAlarmListEntry.setStatus("current")
_AlarmTID_Type = NMSMgdNE
_AlarmTID_Object = MibTableColumn
alarmTID = _AlarmTID_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 1),
    _AlarmTID_Type()
)
alarmTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTID.setStatus("current")


class _AlarmIndex_Type(Integer32):
    """Custom type alarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AlarmIndex_Type.__name__ = "Integer32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 2),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmEntityId_Type = OctetString
_AlarmEntityId_Object = MibTableColumn
alarmEntityId = _AlarmEntityId_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 3),
    _AlarmEntityId_Type()
)
alarmEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEntityId.setStatus("current")
_AlarmEntityType_Type = OctetString
_AlarmEntityType_Object = MibTableColumn
alarmEntityType = _AlarmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 4),
    _AlarmEntityType_Type()
)
alarmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEntityType.setStatus("current")
_AlarmSeverity_Type = NMSSeverity
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 5),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmCondType_Type = OctetString
_AlarmCondType_Object = MibTableColumn
alarmCondType = _AlarmCondType_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 6),
    _AlarmCondType_Type()
)
alarmCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCondType.setStatus("current")
_AlarmServEffect_Type = NMSServiceEffect
_AlarmServEffect_Object = MibTableColumn
alarmServEffect = _AlarmServEffect_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 7),
    _AlarmServEffect_Type()
)
alarmServEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmServEffect.setStatus("current")
_AlarmLocation_Type = NMSCondLocation
_AlarmLocation_Object = MibTableColumn
alarmLocation = _AlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 8),
    _AlarmLocation_Type()
)
alarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLocation.setStatus("current")
_AlarmDirection_Type = NMSCondDirection
_AlarmDirection_Object = MibTableColumn
alarmDirection = _AlarmDirection_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 9),
    _AlarmDirection_Type()
)
alarmDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDirection.setStatus("current")
_AlarmDescription_Type = OctetString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 10),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_NeAlarmTimeStamp_Type = DateAndTime
_NeAlarmTimeStamp_Object = MibTableColumn
neAlarmTimeStamp = _NeAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 11),
    _NeAlarmTimeStamp_Type()
)
neAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmTimeStamp.setStatus("current")
_NmsAlarmTimeStamp_Type = DateAndTime
_NmsAlarmTimeStamp_Object = MibTableColumn
nmsAlarmTimeStamp = _NmsAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 1, 1, 12),
    _NmsAlarmTimeStamp_Type()
)
nmsAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsAlarmTimeStamp.setStatus("current")
_NmsLastMsgNumber_Type = NMSTrapSeqNumber
_NmsLastMsgNumber_Object = MibScalar
nmsLastMsgNumber = _NmsLastMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 2),
    _NmsLastMsgNumber_Type()
)
nmsLastMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsLastMsgNumber.setStatus("current")
_NmsTrapHistoryTable_Object = MibTable
nmsTrapHistoryTable = _NmsTrapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 3)
)
if mibBuilder.loadTexts:
    nmsTrapHistoryTable.setStatus("current")
_NmsTrapHistoryTableEntry_Object = MibTableRow
nmsTrapHistoryTableEntry = _NmsTrapHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 3, 1)
)
nmsTrapHistoryTableEntry.setIndexNames(
    (0, "FNCNMS", "nmsTrapHistoryIndex"),
)
if mibBuilder.loadTexts:
    nmsTrapHistoryTableEntry.setStatus("current")
_NmsTrapHistoryIndex_Type = NMSTrapSeqNumber
_NmsTrapHistoryIndex_Object = MibTableColumn
nmsTrapHistoryIndex = _NmsTrapHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 3, 1, 1),
    _NmsTrapHistoryIndex_Type()
)
nmsTrapHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsTrapHistoryIndex.setStatus("current")
_NmsTrapHistoryTID_Type = NMSMgdNE
_NmsTrapHistoryTID_Object = MibTableColumn
nmsTrapHistoryTID = _NmsTrapHistoryTID_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 3, 1, 2),
    _NmsTrapHistoryTID_Type()
)
nmsTrapHistoryTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsTrapHistoryTID.setStatus("current")
_NmsNotificationBase_ObjectIdentity = ObjectIdentity
nmsNotificationBase = _NmsNotificationBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4)
)
_NotifTID_Type = NMSMgdNE
_NotifTID_Object = MibScalar
notifTID = _NotifTID_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 1),
    _NotifTID_Type()
)
notifTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifTID.setStatus("current")
_NeEntityID_Type = OctetString
_NeEntityID_Object = MibScalar
neEntityID = _NeEntityID_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 2),
    _NeEntityID_Type()
)
neEntityID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEntityID.setStatus("current")
_NeEntityType_Type = OctetString
_NeEntityType_Object = MibScalar
neEntityType = _NeEntityType_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 3),
    _NeEntityType_Type()
)
neEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEntityType.setStatus("current")
_NeSeverity_Type = NMSSeverity
_NeSeverity_Object = MibScalar
neSeverity = _NeSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 4),
    _NeSeverity_Type()
)
neSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neSeverity.setStatus("current")
_NeCondType_Type = OctetString
_NeCondType_Object = MibScalar
neCondType = _NeCondType_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 5),
    _NeCondType_Type()
)
neCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neCondType.setStatus("current")
_NeServEffect_Type = NMSServiceEffect
_NeServEffect_Object = MibScalar
neServEffect = _NeServEffect_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 6),
    _NeServEffect_Type()
)
neServEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neServEffect.setStatus("current")
_NeLocation_Type = NMSCondLocation
_NeLocation_Object = MibScalar
neLocation = _NeLocation_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 7),
    _NeLocation_Type()
)
neLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLocation.setStatus("current")
_NeDirection_Type = NMSCondDirection
_NeDirection_Object = MibScalar
neDirection = _NeDirection_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 8),
    _NeDirection_Type()
)
neDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neDirection.setStatus("current")
_NeCondDescription_Type = OctetString
_NeCondDescription_Object = MibScalar
neCondDescription = _NeCondDescription_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 9),
    _NeCondDescription_Type()
)
neCondDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neCondDescription.setStatus("current")
_NmsNotifTimeStamp_Type = DateAndTime
_NmsNotifTimeStamp_Object = MibScalar
nmsNotifTimeStamp = _NmsNotifTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 10),
    _NmsNotifTimeStamp_Type()
)
nmsNotifTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNotifTimeStamp.setStatus("current")
_NeNotifTimeStamp_Type = DateAndTime
_NeNotifTimeStamp_Object = MibScalar
neNotifTimeStamp = _NeNotifTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 11),
    _NeNotifTimeStamp_Type()
)
neNotifTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNotifTimeStamp.setStatus("current")
_NmsTrapSeqNumber_Type = NMSTrapSeqNumber
_NmsTrapSeqNumber_Object = MibScalar
nmsTrapSeqNumber = _NmsTrapSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 12),
    _NmsTrapSeqNumber_Type()
)
nmsTrapSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsTrapSeqNumber.setStatus("current")
_NmsNEConnState_Type = NMSNEConnState
_NmsNEConnState_Object = MibScalar
nmsNEConnState = _NmsNEConnState_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 13),
    _NmsNEConnState_Type()
)
nmsNEConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNEConnState.setStatus("current")


class _NeOperation_Type(Integer32):
    """Custom type neOperation based on Integer32"""
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


_NeOperation_Type.__name__ = "Integer32"
_NeOperation_Object = MibScalar
neOperation = _NeOperation_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 14),
    _NeOperation_Type()
)
neOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neOperation.setStatus("current")
_NotifServer_Type = OctetString
_NotifServer_Object = MibScalar
notifServer = _NotifServer_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 15),
    _NotifServer_Type()
)
notifServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifServer.setStatus("current")


class _NmsKeepAliveState_Type(Integer32):
    """Custom type nmsKeepAliveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("alive", 1)
    )


_NmsKeepAliveState_Type.__name__ = "Integer32"
_NmsKeepAliveState_Object = MibScalar
nmsKeepAliveState = _NmsKeepAliveState_Object(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 4, 16),
    _NmsKeepAliveState_Type()
)
nmsKeepAliveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsKeepAliveState.setStatus("current")
_FncNMSMIBConformance_ObjectIdentity = ObjectIdentity
fncNMSMIBConformance = _FncNMSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3)
)
_FncNMSMIBCompliances_ObjectIdentity = ObjectIdentity
fncNMSMIBCompliances = _FncNMSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 1)
)
_FncNMSMIBGroups_ObjectIdentity = ObjectIdentity
fncNMSMIBGroups = _FncNMSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2)
)

# Managed Objects groups

nmsNEMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2, 1)
)
nmsNEMgmtGroup.setObjects(
      *(("FNCNMS", "neTID"),
        ("FNCNMS", "neType"),
        ("FNCNMS", "neConnState"))
)
if mibBuilder.loadTexts:
    nmsNEMgmtGroup.setStatus("current")

nmsNEAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2, 2)
)
nmsNEAlarmGroup.setObjects(
      *(("FNCNMS", "alarmTID"),
        ("FNCNMS", "alarmIndex"),
        ("FNCNMS", "alarmEntityId"),
        ("FNCNMS", "alarmEntityType"),
        ("FNCNMS", "alarmSeverity"),
        ("FNCNMS", "alarmCondType"),
        ("FNCNMS", "alarmServEffect"),
        ("FNCNMS", "alarmLocation"),
        ("FNCNMS", "alarmDirection"),
        ("FNCNMS", "alarmDescription"),
        ("FNCNMS", "neAlarmTimeStamp"),
        ("FNCNMS", "nmsAlarmTimeStamp"),
        ("FNCNMS", "nmsLastMsgNumber"),
        ("FNCNMS", "nmsTrapHistoryIndex"),
        ("FNCNMS", "nmsTrapHistoryTID"))
)
if mibBuilder.loadTexts:
    nmsNEAlarmGroup.setStatus("current")

nmsNETrapObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2, 4)
)
nmsNETrapObjects.setObjects(
      *(("FNCNMS", "notifTID"),
        ("FNCNMS", "neEntityID"),
        ("FNCNMS", "neEntityType"),
        ("FNCNMS", "neSeverity"),
        ("FNCNMS", "neCondType"),
        ("FNCNMS", "neServEffect"),
        ("FNCNMS", "neLocation"),
        ("FNCNMS", "neDirection"),
        ("FNCNMS", "neCondDescription"),
        ("FNCNMS", "nmsNotifTimeStamp"),
        ("FNCNMS", "neNotifTimeStamp"),
        ("FNCNMS", "nmsTrapSeqNumber"),
        ("FNCNMS", "nmsNEConnState"),
        ("FNCNMS", "neOperation"))
)
if mibBuilder.loadTexts:
    nmsNETrapObjects.setStatus("current")

nmsServerTrapObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2, 6)
)
nmsServerTrapObjects.setObjects(
      *(("FNCNMS", "notifServer"),
        ("FNCNMS", "nmsKeepAliveState"))
)
if mibBuilder.loadTexts:
    nmsServerTrapObjects.setStatus("current")


# Notification objects

nmsNEEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 0, 1)
)
nmsNEEvent.setObjects(
      *(("FNCNMS", "notifTID"),
        ("FNCNMS", "neEntityID"),
        ("FNCNMS", "neEntityType"),
        ("FNCNMS", "neSeverity"),
        ("FNCNMS", "neCondType"),
        ("FNCNMS", "neServEffect"),
        ("FNCNMS", "neLocation"),
        ("FNCNMS", "neDirection"),
        ("FNCNMS", "neCondDescription"),
        ("FNCNMS", "nmsNotifTimeStamp"),
        ("FNCNMS", "neNotifTimeStamp"),
        ("FNCNMS", "nmsTrapSeqNumber"))
)
if mibBuilder.loadTexts:
    nmsNEEvent.setStatus(
        "current"
    )

nmsNEStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 0, 2)
)
nmsNEStateChangeEvent.setObjects(
      *(("FNCNMS", "notifTID"),
        ("FNCNMS", "nmsNEConnState"),
        ("FNCNMS", "nmsTrapSeqNumber"))
)
if mibBuilder.loadTexts:
    nmsNEStateChangeEvent.setStatus(
        "current"
    )

nmsNEOperationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 0, 3)
)
nmsNEOperationEvent.setObjects(
      *(("FNCNMS", "notifTID"),
        ("FNCNMS", "neOperation"),
        ("FNCNMS", "nmsTrapSeqNumber"))
)
if mibBuilder.loadTexts:
    nmsNEOperationEvent.setStatus(
        "current"
    )

nmsKeepAliveEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 2, 0, 4)
)
nmsKeepAliveEvent.setObjects(
      *(("FNCNMS", "notifServer"),
        ("FNCNMS", "nmsKeepAliveState"))
)
if mibBuilder.loadTexts:
    nmsKeepAliveEvent.setStatus(
        "current"
    )


# Notifications groups

nmsNETrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2, 3)
)
nmsNETrapGroup.setObjects(
      *(("FNCNMS", "nmsNEEvent"),
        ("FNCNMS", "nmsNEStateChangeEvent"),
        ("FNCNMS", "nmsNEOperationEvent"))
)
if mibBuilder.loadTexts:
    nmsNETrapGroup.setStatus(
        "current"
    )

nmsServerTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 2, 5)
)
nmsServerTrapGroup.setObjects(
    ("FNCNMS", "nmsKeepAliveEvent")
)
if mibBuilder.loadTexts:
    nmsServerTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fncNMSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3861, 4, 1500, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fncNMSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNCNMS",
    **{"NMSSeverity": NMSSeverity,
       "NMSCondDirection": NMSCondDirection,
       "NMSCondLocation": NMSCondLocation,
       "NMSServiceEffect": NMSServiceEffect,
       "NMSTrapSeqNumber": NMSTrapSeqNumber,
       "NMSMgdNE": NMSMgdNE,
       "NMSNEConnState": NMSNEConnState,
       "netsmart1500": netsmart1500,
       "nmsNEMgmtMIB": nmsNEMgmtMIB,
       "nmsNEMgmt": nmsNEMgmt,
       "nmsNETable": nmsNETable,
       "nmsNEEntry": nmsNEEntry,
       "neTID": neTID,
       "neType": neType,
       "neConnState": neConnState,
       "nmsNEAlarm": nmsNEAlarm,
       "nmsNotificationTrapBase": nmsNotificationTrapBase,
       "nmsNEEvent": nmsNEEvent,
       "nmsNEStateChangeEvent": nmsNEStateChangeEvent,
       "nmsNEOperationEvent": nmsNEOperationEvent,
       "nmsKeepAliveEvent": nmsKeepAliveEvent,
       "nmsNEAlarmTable": nmsNEAlarmTable,
       "nmsNEAlarmListEntry": nmsNEAlarmListEntry,
       "alarmTID": alarmTID,
       "alarmIndex": alarmIndex,
       "alarmEntityId": alarmEntityId,
       "alarmEntityType": alarmEntityType,
       "alarmSeverity": alarmSeverity,
       "alarmCondType": alarmCondType,
       "alarmServEffect": alarmServEffect,
       "alarmLocation": alarmLocation,
       "alarmDirection": alarmDirection,
       "alarmDescription": alarmDescription,
       "neAlarmTimeStamp": neAlarmTimeStamp,
       "nmsAlarmTimeStamp": nmsAlarmTimeStamp,
       "nmsLastMsgNumber": nmsLastMsgNumber,
       "nmsTrapHistoryTable": nmsTrapHistoryTable,
       "nmsTrapHistoryTableEntry": nmsTrapHistoryTableEntry,
       "nmsTrapHistoryIndex": nmsTrapHistoryIndex,
       "nmsTrapHistoryTID": nmsTrapHistoryTID,
       "nmsNotificationBase": nmsNotificationBase,
       "notifTID": notifTID,
       "neEntityID": neEntityID,
       "neEntityType": neEntityType,
       "neSeverity": neSeverity,
       "neCondType": neCondType,
       "neServEffect": neServEffect,
       "neLocation": neLocation,
       "neDirection": neDirection,
       "neCondDescription": neCondDescription,
       "nmsNotifTimeStamp": nmsNotifTimeStamp,
       "neNotifTimeStamp": neNotifTimeStamp,
       "nmsTrapSeqNumber": nmsTrapSeqNumber,
       "nmsNEConnState": nmsNEConnState,
       "neOperation": neOperation,
       "notifServer": notifServer,
       "nmsKeepAliveState": nmsKeepAliveState,
       "fncNMSMIBConformance": fncNMSMIBConformance,
       "fncNMSMIBCompliances": fncNMSMIBCompliances,
       "fncNMSMIBCompliance": fncNMSMIBCompliance,
       "fncNMSMIBGroups": fncNMSMIBGroups,
       "nmsNEMgmtGroup": nmsNEMgmtGroup,
       "nmsNEAlarmGroup": nmsNEAlarmGroup,
       "nmsNETrapGroup": nmsNETrapGroup,
       "nmsNETrapObjects": nmsNETrapObjects,
       "nmsServerTrapGroup": nmsServerTrapGroup,
       "nmsServerTrapObjects": nmsServerTrapObjects}
)
